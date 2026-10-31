# Referee check of region (III) of thm:A1 for a GENERIC Weyl difference K (no U(2) symmetry):
# exact Ricci of g = e + H_1 + eta(log r) K on the log annulus; compare with predicted leading term |eta''+6eta'|/(2r^2)|K|
import sympy as sp, numpy as np, itertools, random, mpmath as mp
n=4
xs=sp.symbols('x1:5',real=True)
J=sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
d=lambda i,j: 1 if i==j else 0
R1={};B={}
for i,k,j,l in itertools.product(range(n),repeat=4):
    R1[i,k,j,l]=d(i,j)*d(k,l)-d(i,l)*d(j,k)
    B[i,k,j,l]=J[i,j]*J[k,l]-J[i,l]*J[k,j]+2*J[i,k]*J[j,l]
Rs={key:sp.Rational(5,12)*R1[key]-sp.Rational(1,12)*B[key] for key in R1}
def KN(a,b):
    return {(i,k,j,l): a[i,j]*b[k,l]+a[k,l]*b[i,j]-a[i,l]*b[k,j]-a[k,j]*b[i,l] for i,k,j,l in itertools.product(range(n),repeat=4)}
random.seed(3)
def rsym():
    m=sp.Matrix(n,n,lambda i,j: sp.Rational(random.randint(-5,5),7)); return m+m.T
Rr={key:0 for key in R1}
for _ in range(10):
    tt=KN(rsym(),rsym())
    for key in Rr: Rr[key]+=tt[key]
ric=lambda R: sp.Matrix(n,n,lambda i,j: sum(R[i,k,j,k] for k in range(n)))
g=sp.eye(4); Rc=ric(Rr); s=Rc.trace(); P=(Rc-s*g/6)/2; PK=KN(P,g)
Wr={key:(Rr[key]-PK[key])/8 for key in Rr}     # random Weyl tensor, O(1) size
X=sp.Matrix(xs)
HR=lambda R: sp.Matrix(n,n,lambda i,j: -sp.Rational(1,3)*sum(R[i,k,j,l]*xs[k]*xs[l] for k in range(n) for l in range(n)))
Hs=HR(Rs); Kw=HR(Wr)
Lsym,bsym=sp.symbols('L b',positive=True)
r=sp.sqrt(sum(v**2 for v in xs)); u=sp.log(r/(4*bsym))/Lsym
psi=lambda w: w**3*(10-15*w+6*w**2)       # C^2 step, max psi' = 15/8
def ricci_num(g,dg,ddg):
    n=g.shape[0]; gi=np.linalg.inv(g); dg=np.array(dg,dtype=float); ddg=np.array(ddg,dtype=float)
    low=np.zeros((n,n,n)); dlow=np.zeros((n,n,n,n))
    for dd in range(n):
        for bb in range(n):
            for c in range(n):
                low[dd,bb,c]=0.5*(dg[bb,dd,c]+dg[c,dd,bb]-dg[dd,bb,c])
                for e in range(n): dlow[e,dd,bb,c]=0.5*(ddg[e,bb,dd,c]+ddg[e,c,dd,bb]-ddg[e,dd,bb,c])
    Gam=np.einsum('ad,dbc->abc',gi,low); dgi=np.array([-gi@dg[e]@gi for e in range(n)])
    dGam=np.einsum('ead,dbc->eabc',dgi,low)+np.einsum('ad,edbc->eabc',gi,dlow)
    return np.einsum('aabc->bc',dGam)-np.einsum('caba->bc',dGam)+np.einsum('aad,dbc->bc',Gam,Gam)-np.einsum('acd,dba->bc',Gam,Gam)
for sigma in (+1,-1):
    gm=sp.eye(4)+sigma*Hs+psi(u)*Kw
    args=list(xs)+[Lsym,bsym]
    G=sp.lambdify(args,gm,'numpy'); dG=sp.lambdify(args,[sp.diff(gm,c) for c in xs],'numpy'); ddG=sp.lambdify(args,[[sp.diff(gm,c,e) for e in xs] for c in xs],'numpy')
    for ex in (8,16,32,64):
        a=10.0**(-ex); b=a**0.5; R=a**0.25; L=np.log(R/(8*b))
        worst=0; worst_pred=0
        rng=np.random.default_rng(5)
        for it in range(400):
            w=rng.uniform(0.02,0.98); rr=4*b*np.exp(w*L)
            v=rng.normal(size=4); v*=rr/np.linalg.norm(v)
            gg=np.array(G(*v,L,b),dtype=float); Ric=ricci_num(gg,dG(*v,L,b),ddG(*v,L,b))
            defect=np.linalg.norm(np.linalg.inv(gg)@Ric-sigma*np.eye(4),2)
            # predicted leading term
            p1=float(sp.diff(psi(sp.Symbol('w')),sp.Symbol('w')).subs(sp.Symbol('w'),w)); p2=float(sp.diff(psi(sp.Symbol('w')),sp.Symbol('w'),2).subs(sp.Symbol('w'),w))
            Kn=np.array(sp.lambdify(xs,Kw,'numpy')(*v),dtype=float)
            pred=abs(p2/L**2+6*p1/L)/(2*rr**2)*np.linalg.norm(Kn,2)
            if defect>worst: worst,worst_pred=defect,pred
        print("sigma=%+d a=1e-%d L=%.3f  sup defect on annulus=%.5e  predicted leading=%.5e  L*defect=%.4f"%(sigma,ex,L,worst,worst_pred,L*worst))
