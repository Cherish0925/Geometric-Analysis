# Independent check of region (I) of thm:A1: defect of G_a = a^2 (k + a^2 sigma htilde) for rho <= a^{-1/2}
import sympy as sp, mpmath as mp
mp.mp.dps=80
rho,th,ph,ps,t=sp.symbols('rho theta phi psi t',real=True)   # t = a^2*sigma
co=[rho,th,ph,ps]
def metric(X,Y,Z):
    g=sp.zeros(4); g[0,0]=X; g[1,1]=Y
    g[2,2]=Y*sp.sin(th)**2+Z*sp.cos(th)**2; g[2,3]=g[3,2]=Z*sp.cos(th); g[3,3]=Z
    return g
def ricci(g):
    gi=g.inv()
    Gam=[[[sum(gi[a,d]*(sp.diff(g[d,b],co[c])+sp.diff(g[d,c],co[b])-sp.diff(g[b,c],co[d])) for d in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric=sp.zeros(4)
    for b in range(4):
        for c in range(4):
            Ric[b,c]=sum(sp.diff(Gam[a][b][c],co[a]) for a in range(4))-sum(sp.diff(Gam[a][b][a],co[c]) for a in range(4))\
              +sum(Gam[a][a][d]*Gam[d][b][c] for a in range(4) for d in range(4))-sum(Gam[a][c][d]*Gam[d][b][a] for a in range(4) for d in range(4))
    return Ric
# generic biaxial functions first, then substitute (keeps expressions small)
Xf,Yf,Zf=[sp.Function(n)(rho) for n in 'XYZ']
g=metric(Xf,Yf,Zf); Ric=ricci(g)
E=sp.simplify(g.inv()*Ric)          # mixed Ricci; should be diagonal in (rho; theta,phi; psi) block sense
lam_r=sp.simplify(E[0,0]); lam_1=sp.simplify(E[1,1]); lam_3=sp.simplify(E[3,3])
print("offdiag check:",sp.simplify(E[0,1]),sp.simplify(E[1,2]),sp.simplify(E[2,3]), sp.simplify(E[3,2]))
W=1-rho**-4
kX,kY,kZ=1/W,rho**2/4,rho**2*W/4
hX=-rho**2*(7*rho**2-5)/(36*(rho**2-1)*(rho**2+1)**2)
hY=-5*(rho**4-1)/144
hZ=-rho**4/72+sp.Rational(1,16)-1/(12*rho**2)+5/(144*rho**4)
def sub(expr):
    e=expr
    for F,val in ((Xf,kX+t*hX),(Yf,kY+t*hY),(Zf,kZ+t*hZ)):
        e=e.subs({sp.Derivative(F,(rho,2)):sp.diff(val,rho,2)}).subs({sp.Derivative(F,rho):sp.diff(val,rho)}).subs({F:val})
    return e
lams=[sp.lambdify((rho,t),sub(l),'mpmath') for l in (lam_r,lam_1,lam_3)]
for sigma in (1,-1):
  for ex in (8,16):
    a=mp.mpf(10)**(-ex); tt=sigma*a**2; worst=0; where=None
    N=400
    for i in range(N+1):
        r_=mp.mpf(1)+mp.mpf(10)**(-6) if i==0 else mp.e**(mp.log(1/mp.sqrt(a))*i/N)
        if i>0 and r_<=1: continue
        # mixed Ricci of G_a = a^2(...) is a^{-2} * mixed Ricci of (k+a^2 h)
        d=max(abs(l(r_,tt)/a**2-sigma) for l in lams)
        if d>worst: worst,where=d,r_
    print("sigma=%+d a=1e-%d: sup core defect = %s  (= %.4f * a) at rho=%s"%(sigma,ex,mp.nstr(worst,6),float(worst/a),mp.nstr(where,6)))
