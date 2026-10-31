# Numerical illustration of the interpolation estimate in thm:W:
# g = dt^2 + e^{2t} [(1-beta) qbar(t) + beta gamma_flat],  beta = step((t-r0)/K);  sup ||g^{-1}(Ric+3g)||_op <= C (1/K + e^{-2 r0})
import sympy as sp, numpy as np
t,z,x,y=sp.symbols('t z x y',real=True); co=[t,z,x,y]
K,r0=sp.symbols('K r0',positive=True)
gam=sp.Matrix([[1+sp.Rational(3,10)*sp.cos(z),0,0],[0,1+sp.sin(z)/5,sp.cos(z)/10],[0,sp.cos(z)/10,1/(1+sp.sin(z)/5)]])   # non-flat T^3 metric
g2=sp.Matrix([[sp.sin(z)/2,0,0],[0,sp.cos(z)/3,0],[0,0,-sp.cos(z)/3]])
qbar=gam+sp.exp(-2*t)*g2
flat=sp.diag(1,2,sp.Rational(1,2))
w=(t-r0)/K
beta=w**3*(10-15*w+6*w**2)
qt=(1-beta)*qbar+beta*flat
g=sp.zeros(4); g[0,0]=1; g[1:,1:]=sp.exp(2*t)*qt
args=co+[K,r0]
G=sp.lambdify(args,g,'numpy'); dG=sp.lambdify(args,[sp.diff(g,c) for c in co],'numpy'); ddG=sp.lambdify(args,[[sp.diff(g,c,e) for e in co] for c in co],'numpy')
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
def arr(M): return np.array([[float(np.asarray(M[i][j])) for j in range(4)] for i in range(4)])
for Kv,r0v in ((5,2),(10,2),(20,2),(20,4),(40,4),(80,4),(80,6),(160,6)):
    worst=0
    for tv in np.linspace(r0v+1e-6,r0v+Kv-1e-6,60):
        for zv in np.linspace(0,2*np.pi,24,endpoint=False):
            a=(tv,zv,0.2,0.4,Kv,r0v)
            gg=arr(G(*a)); dgg=[arr(m) for m in dG(*a)]; ddgg=[[arr(m) for m in row] for row in ddG(*a)]
            # rescale to avoid overflow: work with frame-normalised quantities
            Ric=ricci_num(gg,dgg,ddgg)
            Lc=np.linalg.cholesky(gg); Li=np.linalg.inv(Lc)
            worst=max(worst,np.abs(np.linalg.eigvalsh(Li@(Ric+3*gg)@Li.T)).max())
    print("K=%4d r0=%d : sup defect=%.4e   defect/(1/K+e^{-2r0})=%.3f"%(Kv,r0v,worst,worst/(1/Kv+np.exp(-2*r0v))))
