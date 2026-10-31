# Independent spot check of thm:ED (sec4): Ricci defect of  G = g_B + h_{z(x)}  on (base collar) x (fibre collar)
#   g_B = dx^2 + ell^2 cosh^2 x dth^2,   h_z = du^2 + a(u)^2 (ds + z zeta'(u) du)^2,  a = a0 cosh u,   z = z(x)
import sympy as sp, numpy as np
x,th,u,s=sp.symbols('x theta u s',real=True)
co=[x,th,u,s]
w=sp.Symbol('w',positive=True)       # half-width of base collar ~ L
a0=sp.Rational(1,2); ell=sp.Symbol('ell',positive=True)
step=lambda t: t**3*(10-15*t+6*t**2)                 # C^2 step on [0,1]
z=step((x+w)/(2*w))
U0=1                                                  # fibre twist region u in [-U0,U0]
zeta=step((u+U0)/(2*U0))                              # zeta: 0 -> 1 (normalised twist; period of s is 1)
a=a0*sp.cosh(u)
g=sp.zeros(4)
g[0,0]=1; g[1,1]=ell**2*sp.cosh(x)**2
zp=z*sp.diff(zeta,u)
g[2,2]=1+a**2*zp**2; g[2,3]=g[3,2]=a**2*zp; g[3,3]=a**2
args=co+[w,ell]
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
def full(M): 
    out=np.zeros((4,4))
    for i in range(4):
        for j in range(4): out[i,j]=np.asarray(M[i][j],dtype=float) if not np.isscalar(M[i][j]) else M[i][j]
    return out
for W in (4.0,8.0,16.0,32.0):
    ellv=np.exp(-W)     # collar half-width ~ log(1/ell)
    worst=0
    for xv in np.linspace(-W*0.999,W*0.999,81):
        for uv in np.linspace(-0.999,0.999,41):
            gg=np.array(G(xv,0.3,uv,0.1,W,ellv),dtype=float)
            dgg=[np.array(m,dtype=float) for m in dG(xv,0.3,uv,0.1,W,ellv)]
            ddgg=[[np.array(m,dtype=float) for m in row] for row in ddG(xv,0.3,uv,0.1,W,ellv)]
            Ric=ricci_num(gg,dgg,ddgg)
            # defect operator norm of g^{-1}Ric + Id, via g-orthonormal frame (symmetric)
            Lc=np.linalg.cholesky(gg); Li=np.linalg.inv(Lc)
            Dm=Li@(Ric+gg)@Li.T
            worst=max(worst,np.abs(np.linalg.eigvalsh(Dm)).max())
    print("half-width w=%5.1f  sup defect=%.5e   w*defect=%.4f"%(W,worst,W*worst))
