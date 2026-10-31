"""Exact spin-connection diagnostics for fixed-slot perpendicular O11 profiles.

Checks the TTCS-derived relative Chern--Simons completion against the independent JAX
curvature integral.  In bolt-adapted cyclic axes (a,b,c)=(old s2,old s3,old s1), set

  u_i = adot_i - (a_j^2+a_k^2-a_i^2)/(a_j a_k),
  H_i = u_i + u_j u_k/2, lambda_i=a_j a_k/a_i.

Then C=T/(8pi^2)=sum u_i^2+u1u2u3 and the candidate exact completion is

 P/(8pi^2)-1 = int [S1+S2+S3+2u1u2u3/lambda2] dt,
 S1=lambda1/4(udot1+2H1/lambda1)^2,
 S2=lambda2/4(udot2-(2u2-u1u3)/lambda2)^2,
 S3=lambda3/4(udot3+2H3/lambda3)^2.

The script also records the independent scalar square giving J-P and cumulative terms.
It accepts a record produced either by the peer script or by perp_dual_cost.py.

Usage: python perp_spin_diagnostics.py RECORD [--out FILE] [--n 1200]
"""
from pathlib import Path
import argparse, json, math, sys
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector, PI, ANG, metric_from, curvature_scalars


def cell_record(path, nq=600):
    r=load_record(path)
    # Dual records store final metadata and z at top level; peer records store opt and wpow.
    x0=float(r['x0']); deg=int(r.get('deg',r.get('degU',6)))
    wpow=int(r.get('wpow',2)); c=make_cell(x0,deg,nq,smooth_mode=(wpow==2),X=float(r.get('X',1.0)))
    z=jnp.asarray(seed_vector(c,r))
    return c,z,r


def axes_u(c,z,x):
    prof=c.prof_factory(z)
    G,h=prof(x)
    old=jnp.sqrt(jnp.diag(h))
    a=jnp.array([old[1],old[2],old[0]])
    da=jax.jacfwd(lambda xx: jnp.array([
        jnp.sqrt(jnp.diag(prof(xx)[1]))[1],
        jnp.sqrt(jnp.diag(prof(xx)[1]))[2],
        jnp.sqrt(jnp.diag(prof(xx)[1]))[0]]))(x)
    adot=2*jnp.sqrt(G)*da
    u=jnp.empty(3,dtype=x.dtype)
    u=u.at[0].set(adot[0]-(a[1]**2+a[2]**2-a[0]**2)/(a[1]*a[2]))
    u=u.at[1].set(adot[1]-(a[2]**2+a[0]**2-a[1]**2)/(a[2]*a[0]))
    u=u.at[2].set(adot[2]-(a[0]**2+a[1]**2-a[2]**2)/(a[0]*a[1]))
    return G,a,u


def point(c,z,x):
    G,a,u=axes_u(c,z,x)
    du_dx=jax.jacfwd(lambda xx: axes_u(c,z,xx)[2])(x)
    udot=2*jnp.sqrt(G)*du_dx
    H=jnp.array([u[0]+u[1]*u[2]/2,u[1]+u[2]*u[0]/2,u[2]+u[0]*u[1]/2])
    lam=jnp.array([a[1]*a[2]/a[0],a[2]*a[0]/a[1],a[0]*a[1]/a[2]])
    C=jnp.sum(u*u)+jnp.prod(u)
    sq1=lam[0]/4*(udot[0]+2*H[0]/lam[0])**2
    sq2=lam[1]/4*(udot[1]-(2*u[1]-u[0]*u[2])/lam[1])**2
    sq3=lam[2]/4*(udot[2]+2*H[2]/lam[2])**2
    cubic=2*jnp.prod(u)/lam[1]
    # Original positive P square, as a second exact representation.
    psq=jnp.sum(lam/4*(udot-2*H/lam)**2)
    Sigma=jnp.sum(udot/a+2*H/(jnp.roll(a,-1)*jnp.roll(a,-2)))
    scalar= jnp.prod(a)/4*(Sigma-12)**2
    # Convert dt density to dx density.
    inv=1/(2*jnp.sqrt(G))
    return u,C,sq1*inv,sq2*inv,sq3*inv,cubic*inv,psq*inv,scalar*inv,lam,H,udot


def diagnostics(path,n=1200):
    c,z,r=cell_record(path)
    # Gauss integration in u=log(x/x0)/ell split near bolt.
    e,w=np.polynomial.legendre.leggauss(n//2)
    us=np.concatenate([0.1*(e+1)/2,0.1+(0.9)*(e+1)/2])
    wu=np.concatenate([0.1*w/2,0.9*w/2])
    xs=c.x0*np.exp(c.ell*us); dxdu=c.ell*xs
    vals=jax.vmap(lambda x: point(c,z,x))(jnp.asarray(xs))
    u,C,s1,s2,s3,cub,psq,scal,lam,H,udot=[np.asarray(v) for v in vals]
    weights=wu*dxdu
    integ=lambda y: float(np.sum(weights*y))
    terms=dict(S1=integ(s1),S2=integ(s2),S3=integ(s3),cubic=integ(cub),
               negative_cubic=integ(np.minimum(cub,0)),positive_cubic=integ(np.maximum(cub,0)),
               P_positive_square=integ(psq),scalar_square=integ(scal))
    terms['relative_total']=terms['S1']+terms['S2']+terms['S3']+terms['cubic']
    costs=c.full_report(z)
    # Fine log grid for sign/chamber geometry and cumulative profiles.
    ug=np.linspace(1e-7,1,1201); xg=c.x0*np.exp(c.ell*ug)
    vg=jax.vmap(lambda x: point(c,z,x))(jnp.asarray(xg))
    uu,CC,gs1,gs2,gs3,gcub,gpsq,gscal=[np.asarray(v) for v in vg[:8]]
    # cumulative x integrals
    def cum(y): return np.concatenate([[0],np.cumsum((y[1:]+y[:-1])*np.diff(xg)/2)])
    relcum=cum(gs1+gs2+gs3+gcub); pcum=cum(gpsq); qcum=cum(gscal)
    prod=np.prod(uu,axis=1)
    k=int(np.argmin(CC)); kn=int(np.argmin(prod))
    out=dict(source=str(path),x0=c.x0,deg=c.degU,wpow=c.wpow,costs=costs,terms=terms,
             residual_P_positive=terms['P_positive_square']-costs['P_direct'],
             residual_relative=1+terms['relative_total']-costs['P_direct'],
             residual_scalar=terms['scalar_square']-costs['scalar_deviation'],
             C_bolt=float(CC[0]),C_collar=float(CC[-1]),C_min=float(CC[k]),x_Cmin=float(xg[k]),
             cubic_product_min=float(prod[kn]),x_cubic_min=float(xg[kn]),
             chamber_fraction_negative=float(np.mean(prod<0)),
             cumulative=dict(relative_end=float(relcum[-1]),P_end=float(pcum[-1]),scalar_end=float(qcum[-1])),
             profile=[dict(x=float(x),u1=float(q[0]),u2=float(q[1]),u3=float(q[2]),C=float(cc),
                           cubic_product=float(pr),relative_cum=float(rc),P_cum=float(pc),scalar_cum=float(qc))
                      for x,q,cc,pr,rc,pc,qc in zip(xg,uu,CC,prod,relcum,pcum,qcum)])
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--out'); ap.add_argument('--n',type=int,default=1200)
    a=ap.parse_args(); out=diagnostics(a.record,a.n); text=json.dumps(out); print(text)
    if a.out: Path(a.out).write_text(text+'\n')

if __name__=='__main__': main()
