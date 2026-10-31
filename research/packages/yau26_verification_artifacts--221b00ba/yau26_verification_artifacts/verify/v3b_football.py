# Football log-Weyl check with exact symbolic derivatives (sympy) + high-precision evaluation (mpmath).
import sympy as sp, mpmath as mp, sys, pickle
r = sp.symbols('r', positive=True)
d = pickle.load(open('biaxial_ricci.pkl','rb'))
Xs,Ys,Zs = sp.Function('X')(r), sp.Function('Y')(r), sp.Function('Z')(r)

def eig_exprs(X,Y,Z):
    D=lambda f,n=1: sp.diff(f,r,n)
    R0=-D(Z,2)/(2*X*Z)+D(Z)**2/(4*X*Z**2)-D(Y,2)/(X*Y)+D(Y)**2/(2*X*Y**2)+D(X)*D(Z)/(4*X**2*Z)+D(X)*D(Y)/(2*X**2*Y)
    R1=1/Y-Z/(2*Y**2)-D(Y,2)/(2*X*Y)-D(Y)*D(Z)/(4*X*Y*Z)+D(X)*D(Y)/(4*X**2*Y)
    R3=Z/(2*Y**2)-D(Z,2)/(2*X*Z)+D(Z)**2/(4*X*Z**2)-D(Y)*D(Z)/(2*X*Y*Z)+D(X)*D(Z)/(4*X**2*Z)
    return [R0,R1,R3]

def sstep(t):
    f=lambda u: sp.exp(-1/u)
    return f(t)/(f(t)+f(1-t))

def build(ex, sigma=1):
    a = sp.Rational(1,10**ex); b = sp.Rational(1,10**(ex//2)); R = sp.Rational(1,10**(ex//4))
    L = sp.log(R/(8*b))
    rho = r/a
    W = 1-rho**-4
    h_rr = -rho**2*(7*rho**2-5)/(36*(rho**2-1)*(rho**2+1)**2)
    h_12 = -5*(rho**4-1)/144
    h_33 = -rho**4/72+sp.Rational(1,16)-rho**-2/12+5*rho**-4/144
    core = (1/W+a**2*sigma*h_rr, a**2*(rho**2/4+a**2*sigma*h_12), a**2*(rho**2*W/4+a**2*sigma*h_33))
    qH1 = (sp.Integer(1), r**2/4-sigma*5*r**4/144, r**2/4-sigma*r**4/72)
    qH0 = (sp.Integer(1), r**2/4-sigma*r**4/36, r**2/4-sigma*r**4/36)
    s3 = sp.sqrt(3)
    yex = sp.Rational(3,4)*(sp.sin(r/s3)**2 if sigma==1 else sp.sinh(r/s3)**2)
    ex0 = (sp.Integer(1), yex, yex)
    chi1 = sstep((r-b)/b)
    innercut = tuple(qH1[i]+(1-chi1)*(core[i]-qH1[i]) for i in range(3))
    eta = sstep(sp.log(r/(4*b))/L)
    logring = tuple(qH1[i]+eta*(qH0[i]-qH1[i]) for i in range(3))
    chi2 = sstep((r-R/2)/(R/2))
    outercut = tuple(qH0[i]+chi2*(ex0[i]-qH0[i]) for i in range(3))
    regions = [('core', a*(1+sp.Rational(1,1000)), b, core),
               ('innercut', b, 2*b, innercut),
               ('plateau', 2*b, 4*b, qH1),
               ('logring', 4*b, R/2, logring),
               ('outercut', R/2, R, outercut)]
    return regions, dict(a=a,b=b,R=R,L=L)

def scan(ex, sigma=1, npts=400):
    mp.mp.dps = 3*ex+60
    regions, par = build(ex, sigma)
    res={}
    for name, lo, hi, (X,Y,Z) in regions:
        exprs = eig_exprs(X,Y,Z)
        fs = [sp.lambdify(r, e, modules='mpmath') for e in exprs]
        lo_m = mp.log(mp.mpf(sp.Rational(lo).p)/mp.mpf(sp.Rational(lo).q)); hi_m = mp.log(mp.mpf(sp.Rational(hi).p)/mp.mpf(sp.Rational(hi).q))
        worst=mp.mpf(0); where=None
        for j in range(npts):
            u = lo_m+(hi_m-lo_m)*(mp.mpf(j)+mp.mpf('0.5'))/npts
            rv = mp.e**u
            dev = max(abs(f(rv)-sigma) for f in fs)
            if dev>worst: worst=dev; where=rv
        res[name]=(worst,where)
    return res, par

if __name__=='__main__':
    sigma=int(sys.argv[1]) if len(sys.argv)>1 else 1
    exps=[int(x) for x in sys.argv[2:]] or [8,16,32,64]
    for ex in exps:
        res,par=scan(ex,sigma)
        L=mp.mpf(sp.N(par['L'],30))
        tot=max(v[0] for v in res.values())
        print(f"sigma={sigma} a=1e-{ex}: L={mp.nstr(L,6)} delta={mp.nstr(tot,6)} delta*L={mp.nstr(tot*L,6)}")
        print('   ', {k:(mp.nstr(v[0],4)) for k,v in res.items()})
        sys.stdout.flush()
