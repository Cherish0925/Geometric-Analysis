"""Numerical off-bolt Weyl-eigenvalue test for the validated O(-1) ACH Einstein orbit.

At selected geodesic radii, reconstruct the exact radial 2-jet from the Einstein
ODE and evaluate the two chiral Weyl curvature-operator blocks by an independent
coordinate/JAX calculation.  A conformally Kahler Einstein four-metric would,
on the nonzero-Weyl set and in one orientation, have a repeated Weyl eigenvalue
(Derdzinski).  Thus three distinct eigenvalues in both blocks at one point rule
out local conformal Kahler structures in either orientation.

This is a floating-point geometric check of the validated orbit, not an interval
certificate.  The validated parameter interval is so narrow that the displayed
eigenvalue splittings can also be compared at both endpoints.
"""
from pathlib import Path
import json, sys
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from einstein_bolt_shoot import Bolt, shoot, rhs
from o11_rotated_cell import euler_E, LA, LB, PAIRS, ANG


def metric_local(t0,a,ap,app):
    a=jnp.asarray(a);ap=jnp.asarray(ap);app=jnp.asarray(app)
    def g(y):
        dt=y[0]-t0
        av=a+ap*dt+0.5*app*dt*dt
        E=euler_E(y[1:])
        h=jnp.diag(av*av)
        out=jnp.zeros((4,4)).at[0,0].set(1.0)
        return out.at[1:,1:].set(E.T@h@E)
    return g


def blocks(g,y):
    gm=g(y)
    def Gam(yy):
        gg=g(yy); gi=jnp.linalg.inv(gg); dg=jax.jacfwd(g)(yy)
        tt=jnp.einsum('dcb->dbc',dg)+dg-jnp.einsum('bcd->dbc',dg)
        return 0.5*jnp.einsum('ad,dbc->abc',gi,tt)
    Gm=Gam(y); dG=jax.jacfwd(Gam)(y)
    R=(jnp.einsum('adbc->abcd',dG)-jnp.einsum('acbd->abcd',dG)
       +jnp.einsum('ace,edb->abcd',Gm,Gm)-jnp.einsum('ade,ecb->abcd',Gm,Gm))
    Rl=jnp.einsum('ae,ebcd->abcd',gm,R)
    L=jnp.linalg.cholesky(gm); M=jnp.linalg.inv(L).T
    Rh=jnp.einsum('abcd,ai,bj,ck,dl->ijkl',Rl,M,M,M,M)
    ric=jnp.einsum('ijil->jl',Rh); scal=jnp.trace(ric); ric0=ric-scal/4*jnp.eye(4)
    Rop=jnp.array([[Rh[i,j,k,l] for (k,l) in PAIRS] for (i,j) in PAIRS])
    WA=LA@Rop@LA.T-scal/12*jnp.eye(3)
    WB=LB@Rop@LB.T-scal/12*jnp.eye(3)
    return np.asarray(WA),np.asarray(WB),float(scal),float(jnp.linalg.norm(ric0))


def evaluate_d(dval,times):
    b=0.8; solrec=shoot(Bolt(1),b,dval,T=max(times)+0.05,t0=0.002,dense=True)
    sol=solrec.pop('_sol')
    rows=[]
    for t in times:
        z=sol.sol(t); L=z[:3]; yy=z[3:]
        dz=rhs(t,z); yp=dz[3:]
        a=np.exp(L); ap=a*yy; app=a*(yy*yy+yp)
        A,B,s,r0=blocks(metric_local(t,a,ap,app),jnp.concatenate([jnp.array([t]),ANG]))
        rec=dict(t=t,scalar=s,ric0_norm=r0,a=a.tolist(),y=yy.tolist())
        for name,W in [('A',A),('B',B)]:
            ev=np.linalg.eigvalsh(0.5*(W+W.T))
            gaps=np.diff(ev)
            rec[name]=dict(matrix=W.tolist(),eigenvalues=ev.tolist(),adjacent_gaps=gaps.tolist(),
                           min_gap=float(np.min(np.abs(gaps))),norm2=float(np.sum(W*W)))
        rows.append(rec)
    return dict(d=dval,rows=rows,constraint_end=solrec['con_end'])


def main():
    times=[0.01,0.03,0.05,0.1,0.2,0.5,1.0,2.0]
    ds=[0.28697953,0.286999618893,0.28701987]
    out=dict(status='floating point; exact Einstein radial 2-jet from ODE',b=0.8,
             validated_d_interval=[ds[0],ds[-1]],runs=[evaluate_d(d,times) for d in ds])
    path=HERE.parent/'data'/'ach_capd'/'weyl_degeneracy_offbolt.json'
    path.write_text(json.dumps(out,indent=1)+'\n')
    for run in out['runs']:
        print('d',run['d'])
        for r in run['rows']:
            print(r['t'],'s',r['scalar'],'ric0',r['ric0_norm'],'A',r['A']['eigenvalues'],'B',r['B']['eigenvalues'])
if __name__=='__main__':main()
