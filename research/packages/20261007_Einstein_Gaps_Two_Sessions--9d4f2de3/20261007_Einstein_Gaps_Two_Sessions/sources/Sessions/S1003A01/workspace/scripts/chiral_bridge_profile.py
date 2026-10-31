"""Bridge the chiral fluxes to the existing spin variables and sample the certified/floating cell.

For diagonal Bianchi-IX, p_i=a_i' and gamma_i=(a_j^2+a_k^2-a_i^2)/(a_j a_k),
u_i=p_i-gamma_i.  The bridge tested here is
  b_+ = 2 - C(u),       b_- = C(-p-gamma)-2,
  C(v)=sum(v_i^2)+v_1 v_2 v_3.
The profile calculation uses the stable DualCell parametrization and adapted axes
(old 1, old 2, old 0), so the collapsed bolt axis is the third new axis.
It reports b_+, b_-, cumulative P/(8 pi^2), and the exact chiral lower bound
P[bolt,t] >= b_+(t)-1.
"""
from pathlib import Path
import json, sys, math
import numpy as np
import sympy as sp
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
PEER=ROOT/'Sessions'/'S1003A02'/'workspace'/'scripts'
sys.path.insert(0,str(HERE)); sys.path.insert(0,str(PEER))
from perp_dual_cost import DualCell, load_record, seed_vector


def C(v):
    return jnp.sum(v*v)+jnp.prod(v)


def symbolic_bridge():
    # Independent algebra against the peer's solved S and Euler flux.
    pc_path=ROOT/'Sessions'/'S1003A01'/'workspace'/'scripts'
    sys.path.insert(0,str(pc_path))
    import perp_cartan_verify as pc
    d=json.loads((PEER/'..'/'data'/'chiral_flux.json').resolve().read_text())
    # JSON stores the unshifted S; symbols are exactly those of pc.
    S=sp.sympify(d['S'],locals={str(x):x for x in [pc.a,pc.b,pc.c,pc.a1,pc.b1,pc.c1]})
    A=[pc.a,pc.b,pc.c]; P=[pc.a1,pc.b1,pc.c1]; W=pc.a*pc.b*pc.c
    gam=[(A[(i+1)%3]**2+A[(i+2)%3]**2-A[i]**2)/(A[(i+1)%3]*A[(i+2)%3]) for i in range(3)]
    u=[P[i]-gam[i] for i in range(3)]
    Cm=sp.factor(sum(x*x for x in u)+sp.prod(u))
    vm=[-P[i]-gam[i] for i in range(3)]
    Cminus=sp.factor(sum(x*x for x in vm)+sp.prod(vm))
    def K3(i,j,k):
        return ((A[j]**2-A[k]**2)**2+2*A[i]**2*(A[j]**2+A[k]**2)-3*A[i]**4)/(A[i]**2*A[j]**2*A[k]**2)
    y=[P[i]/A[i] for i in range(3)]
    bE=sp.factor(W*(y[0]*K3(0,1,2)+y[1]*K3(1,2,0)+y[2]*K3(2,0,1)-sp.prod(y)))
    # normalized peer fluxes: bA+6 and bB-6.
    bp=sp.factor(bE-S+6); bm=sp.factor(bE+S-6)
    return {'plus_residual':str(sp.factor(bp-(2-Cm))),
            'minus_residual':str(sp.factor(bm-(Cminus-2))),
            'bE_minus_C_relation':str(sp.factor(bE-S+6-(2-Cm))),
            'S_minus_6_at_euclidean':str(sp.simplify((S-6).subs({pc.a:sp.Symbol('r'),pc.b:sp.Symbol('r'),pc.c:sp.Symbol('r'),pc.a1:1,pc.b1:1,pc.c1:1})))}


def sample_profile(record, n=1200):
    rec=load_record(record); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec['deg'])
    c=DualCell(x0,X,deg,deg,n); c.aligned=False; c.wpow=2
    z=np.asarray(seed_vector(c,rec),float); z[int(deg)]=0.0
    prof=c.prof_factory(jnp.asarray(z))
    # New axes = old axis 1, old axis 2, old axis 0.
    def vals(x):
        G,h=prof(x)
        old=jnp.sqrt(jnp.diag(h)); a=jnp.array([old[1],old[2],old[0]])
        da_dx=jax.jacfwd(lambda xx: jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]]))(x)
        p=2*jnp.sqrt(G)*da_dx
        gam=jnp.array([(a[1]**2+a[2]**2-a[0]**2)/(a[1]*a[2]),
                       (a[2]**2+a[0]**2-a[1]**2)/(a[2]*a[0]),
                       (a[0]**2+a[1]**2-a[2]**2)/(a[0]*a[1])])
        u=p-gam; vm=-p-gam
        return jnp.array([C(u),C(vm),*u,*p,*gam,G,jnp.prod(a)])
    # x coordinate quadrature: avoid removable bolt point.
    uu=np.linspace(2e-6,1.0,n)
    xs=x0*np.exp(c.ell*uu)
    arr=np.asarray(jax.vmap(vals)(jnp.asarray(xs)))
    Cp,Cm=arr[:,0],arr[:,1]; bp=2-Cp; bm=Cm-2
    # cumulative P from exact spin formula using c.fields, independent of b bridge.
    s,ric0,wa,wb,dv=c.fields(jnp.asarray(z)); Wq=np.asarray(c.wx*dv)
    # fields grid is quadrature nodes, not our profile grid; integrate cumulative on profile grid directly.
    def dens(x):
        G,h=prof(x); old=jnp.sqrt(jnp.diag(h)); a=jnp.array([old[1],old[2],old[0]])
        da_dx=jax.jacfwd(lambda xx: jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]]))(x)
        p=2*jnp.sqrt(G)*da_dx
        # second derivative of a wrt t via derivative of p(x) times dx/dt
        pdx=jax.jacfwd(lambda xx: 2*jnp.sqrt(prof(xx)[0])*jax.jacfwd(lambda yy: jnp.array([jnp.sqrt(jnp.diag(prof(yy)[1]))[1],jnp.sqrt(jnp.diag(prof(yy)[1]))[2],jnp.sqrt(jnp.diag(prof(yy)[1]))[0]]))(xx))(x)
        pdot=2*jnp.sqrt(G)*pdx
        gam=jnp.array([(a[1]**2+a[2]**2-a[0]**2)/(a[1]*a[2]),(a[2]**2+a[0]**2-a[1]**2)/(a[2]*a[0]),(a[0]**2+a[1]**2-a[2]**2)/(a[0]*a[1])])
        # gamma t derivative by autodiff
        gdot=2*jnp.sqrt(G)*jax.jacfwd(lambda xx: jnp.array([(jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]])[1]**2+jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]])[2]**2-jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(jnp.diag(prof(xx)[1]))[2]),jnp.sqrt(jnp.diag(prof(xx)[1]))[0]])[0]**2)/(jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]])[1]*jnp.array([jnp.sqrt(jnp.diag(prof(xx)[1]))[1],jnp.sqrt(jnp.diag(prof(xx)[1]))[2],jnp.sqrt(jnp.diag(prof(xx)[1]))[0]])[2]),0]))(x)
        # This density helper is intentionally not used; use exact c.fields below.
        return G
    # Use exact quadrature output for P and map its nodes to cumulative arrays.
    qx=np.asarray(c.xx); qw=np.asarray(c.wx)
    # adapted b+ at quadrature via same vals
    qa=np.asarray(jax.vmap(vals)(jnp.asarray(qx))); qbp=2-qa[:,0]
    qp=np.asarray(c.fields(jnp.asarray(z))[1])
    qdens=np.asarray(qw*qp) # qp is |Ric0|^2*volume density including PI^2 factors
    order=np.argsort(qx); qx=qx[order]; qbp=qbp[order]; qdens=qdens[order]
    cum=np.concatenate([[0],np.cumsum((qdens[1:]+qdens[:-1])*(qx[1:]-qx[:-1])/2)])/(8*math.pi**2)
    # Interpolate cumulative to profile grid; qx starts at quadrature interior and ends at X.
    pcum=np.interp(xs,qx,cum,left=0,right=float(cum[-1]))
    gap=pcum-(bp-1)
    return {'record':str(record),'x0':x0,'X':X,'n':n,'P_total':float(cum[-1]),
            'bplus_min':float(bp.min()),'bplus_max':float(bp.max()),
            'bminus_min':float(bm.min()),'bminus_max':float(bm.max()),
            'gap_min_Pminus_bplusminus1':float(gap.min()),
            'argmin_gap_x':float(xs[np.argmin(gap)]),
            'at_bolt':{'bplus':float(bp[0]),'bminus':float(bm[0]),'C_u':float(Cp[0])},
            'at_collar':{'bplus':float(bp[-1]),'bminus':float(bm[-1]),'C_u':float(Cp[-1]),'C_minus':float(Cm[-1])},
            'selected':[{'x':float(xs[i]),'bplus':float(bp[i]),'bminus':float(bm[i]),'Pcum':float(pcum[i]),'gap':float(gap[i])} for i in np.linspace(0,n-1,12,dtype=int)]}

if __name__=='__main__':
    print(json.dumps({'symbolic':symbolic_bridge()},indent=1))
    if len(sys.argv)>1:
        print(json.dumps(sample_profile(sys.argv[1]),indent=1))
