# Independent numerical verification of the log-Weyl construction (thm:A1) on the football S^4/Z_2,
# sigma=+1, in the U(2)-invariant (biaxial) class where everything is explicit.
import mpmath as mp, sys
mp.mp.dps = 60

def step(t):
    # smooth step: 0 for t<=0, 1 for t>=1
    if t<=0: return mp.mpf(0)
    if t>=1: return mp.mpf(1)
    f=lambda u: mp.e**(-1/u)
    return f(t)/(f(t)+f(1-t))

def make_metric(a, gamma=mp.mpf(1)/2, kappa=mp.mpf(1)/4, sigma=1):
    a=mp.mpf(a); b=a**gamma; R=a**kappa
    L=mp.log(R/(8*b))
    s3=mp.sqrt(3)
    def W(rho): return 1-rho**-4
    def h_rr(rho): return -rho**2*(7*rho**2-5)/(36*(rho**2-1)*(rho**2+1)**2)
    def h_12(rho): return -5*(rho**4-1)/144
    def h_33(rho): return -rho**4/72+mp.mpf(1)/16-rho**-2/12+5*rho**-4/144
    def core(r):
        rho=r/a
        X=1/W(rho)+a**2*sigma*h_rr(rho)
        Y=a**2*(rho**2/4+a**2*sigma*h_12(rho))
        Z=a**2*(rho**2*W(rho)/4+a**2*sigma*h_33(rho))
        return X,Y,Z
    def quadH1(r):
        return mp.mpf(1), r**2/4-sigma*5*r**4/144, r**2/4-sigma*r**4/72
    def quadH0(r):
        return mp.mpf(1), r**2/4-sigma*r**4/36, r**2/4-sigma*r**4/36
    def exact0(r):
        if sigma==1:
            y=mp.mpf(3)/4*mp.sin(r/s3)**2
        else:
            y=mp.mpf(3)/4*mp.sinh(r/s3)**2
        return mp.mpf(1), y, y
    def K(r):
        q0=quadH0(r); q1=quadH1(r)
        return tuple(q0[i]-q1[i] for i in range(3))
    def metric(r):
        r=mp.mpf(r)
        if r<=b:
            return core(r)
        if r<=2*b:
            c=core(r); q=quadH1(r); chi=step((r-b)/b)
            return tuple(q[i]+(1-chi)*(c[i]-q[i]) for i in range(3))
        if r<=4*b:
            return quadH1(r)
        if r<=R/2:
            eta=step(mp.log(r/(4*b))/L); q=quadH1(r); k=K(r)
            return tuple(q[i]+eta*k[i] for i in range(3))
        if r<=R:
            q=quadH0(r); ex=exact0(r); chi=step((r-R/2)/(R/2))
            return tuple(q[i]+chi*(ex[i]-q[i]) for i in range(3))
        return exact0(r)
    return metric, dict(a=a,b=b,R=R,L=L)

def ricci_eigs(metric, r, hrel=mp.mpf('1e-12')):
    r=mp.mpf(r)
    # numerical derivatives w.r.t. log r for scale robustness
    def comp(i): return lambda u: metric(mp.e**u)[i]
    u=mp.log(r)
    vals=[]; d1=[]; d2=[]
    for i in range(3):
        f=comp(i)
        h=mp.mpf('1e-10')
        f0=f(u); fp=f(u+h); fm=f(u-h); fpp=f(u+2*h); fmm=f(u-2*h)
        D1=(-fpp+8*fp-8*fm+fmm)/(12*h)
        D2=(-fpp+16*fp-30*f0+16*fm-fmm)/(12*h*h)
        # convert to r-derivatives: d/dr = (1/r) d/du ; d2/dr2 = (1/r^2)(d2/du2 - d/du)
        vals.append(f0); d1.append(D1/r); d2.append((D2-D1)/r**2)
    X,Y,Z=vals; Xp,Yp,Zp=d1; Xpp,Ypp,Zpp=d2
    R0=-Zpp/(2*X*Z)+Zp**2/(4*X*Z**2)-Ypp/(X*Y)+Yp**2/(2*X*Y**2)+Xp*Zp/(4*X**2*Z)+Xp*Yp/(2*X**2*Y)
    R1=1/Y-Z/(2*Y**2)-Ypp/(2*X*Y)-Yp*Zp/(4*X*Y*Z)+Xp*Yp/(4*X**2*Y)
    R3=Z/(2*Y**2)-Zpp/(2*X*Z)+Zp**2/(4*X*Z**2)-Yp*Zp/(2*X*Y*Z)+Xp*Zp/(4*X**2*Z)
    return R0,R1,R3

def scan(a, sigma=1, npts=1500):
    metric,par=make_metric(a,sigma=sigma)
    aa=par['a']; R=par['R']; b=par['b']
    # log-spaced sample from just outside the bolt (rho=1+1e-3) to 1.5 R, avoiding exact breakpoints
    lo=mp.log(aa*(1+mp.mpf('1e-3'))); hi=mp.log(1.5*R)
    worst=0; where=None; regionmax={}
    for j in range(npts+1):
        u=lo+(hi-lo)*(mp.mpf(j)+mp.mpf('0.37'))/(npts+1)
        r=mp.e**u
        e=ricci_eigs(metric,r)
        dev=max(abs(x-sigma) for x in e)
        reg=('core' if r<=b else 'innercut' if r<=2*b else 'plateau' if r<=4*b else 'logring' if r<=R/2 else 'outercut' if r<=R else 'exact')
        regionmax[reg]=max(regionmax.get(reg,0),dev)
        if dev>worst: worst=dev; where=(r,reg)
    return worst,where,regionmax,par

if __name__=='__main__':
    sigma=int(sys.argv[1]) if len(sys.argv)>1 else 1
    print('sigma=',sigma)
    for ex in [8,16,32,64,128,256,512]:
        a=mp.mpf(10)**(-ex)
        worst,where,regionmax,par=scan(a,sigma=sigma)
        L=par['L']
        print(f"a=1e-{ex}: L={mp.nstr(L,6)}  delta={mp.nstr(worst,6)}  delta*L={mp.nstr(worst*L,6)}  at r={mp.nstr(where[0],4)} [{where[1]}]")
        print('    per region:', {k:mp.nstr(v,4) for k,v in regionmax.items()})
