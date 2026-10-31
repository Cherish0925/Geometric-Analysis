"""Analyze exact-CH Sturm boundary flux and the full relative compensation on O11 profiles.

Reads any fixed-slot perpendicular record accepted by perp_spin_diagnostics.py.  For
candidate cut positions x_c it records:
  * exact-CH ground-state bulk and endpoint flux of the actual transverse modes
    v_+=u1+u3, v_-=u1-u3 on [x_c,1], as if those modes were propagated over CH;
  * the actual relative-calibration density and its split across [x0,x_c],[x_c,1];
  * signed (not negative-part truncated) cubic contributions;
  * deviations of metric/spin variables from the exact CH branch.

The CH factorization is an exact comparison operator, not an identity for a non-CH
profile. The full relative-density integrals are exact for the numerical profile.
"""
from pathlib import Path
import argparse,json,sys
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from perp_spin_diagnostics import cell_record, point
from perp_dual_cost import adapted_slice


def trap_segment(x,y,i0=0,i1=None):
    if i1 is None: i1=len(x)-1
    return float(np.trapezoid(y[i0:i1+1],x[i0:i1+1]))

def ch_ground(x,v):
    p=x*(1+x)/4
    Vp=(4+18*x+15*x*x)/(16*x*(1+x))
    Vm=(4-18*x+3*x*x)/(16*x*(1+x))
    f=x/(1+x)**2.5
    beta=(2-3*x)/8
    dv=np.gradient(v,x,edge_order=2)
    qplus=p*dv[0]**2+Vp*v[0]**2 if False else None
    return p,Vp,Vm,f,beta

def analyze(path,n=4001,cuts=None):
    c,z,r=cell_record(path,nq=600)
    # log-uniform grid excluding removable bolt point, with exact collar endpoint.
    ug=np.linspace(1e-8,1,n); x=c.x0*np.exp(c.ell*ug)
    vals=jax.vmap(lambda xx: point(c,z,xx))(jnp.asarray(x))
    u,C,s1,s2,s3,cub,psq,scal,lam,H,udot=[np.asarray(q) for q in vals]
    # point returns dx densities for energetic terms.
    rel=s1+s2+s3+cub; possq=s1+s2+s3
    # Get radii and G for exact-CH deviation.
    av=jax.vmap(lambda xx: adapted_slice(c,z,xx))(jnp.asarray(x))
    G=np.asarray(av[0]); abc=np.asarray(av[1])
    uch=np.column_stack([np.zeros_like(x),3*x,np.zeros_like(x)])
    lamch=np.column_stack([np.sqrt(x*(1+x)),np.sqrt(x/(1+x)),np.sqrt(x*(1+x))])
    abcch=np.column_stack([np.sqrt(x),np.sqrt(x*(1+x)),np.sqrt(x)])
    dev=dict(
      max_u=float(np.max(np.abs(u-uch),axis=None)),
      max_lambda_relative=float(np.max(np.abs(lam/lamch-1))),
      max_abc_relative=float(np.max(np.abs(abc/abcch-1))),
      max_G_relative=float(np.max(np.abs(G/(x*(1+x))-1))))
    if cuts is None:
        cuts=[max(c.x0*1.05,q) for q in (0.03,0.05,0.08,0.1,0.15,0.2,0.3,0.5)]
    vp=u[:,0]+u[:,2]; vm=u[:,0]-u[:,2]
    dvp=np.gradient(vp,x,edge_order=2); dvm=np.gradient(vm,x,edge_order=2)
    p,Vplus,Vminus,f,beta=ch_ground(x,vm)
    qp=p*dvp*dvp+Vplus*vp*vp
    qm=p*dvm*dvm+Vminus*vm*vm
    # Ground-state bulk computed directly; endpoint flux beta*v^2.
    wm=vm/f; dwm=np.gradient(wm,x,edge_order=2)
    gbulk=p*f*f*dwm*dwm
    rows=[]
    for xc in cuts:
        if not (x[1]<xc<x[-1]): continue
        k=int(np.searchsorted(x,xc))
        qm_int=trap_segment(x,qm,k)
        bulk=trap_segment(x,gbulk,k)
        bd=float(beta[-1]*vm[-1]**2-beta[k]*vm[k]**2)
        rows.append(dict(xcut=float(x[k]),
          actual_inner_relative=trap_segment(x,rel,0,k),
          actual_outer_relative=trap_segment(x,rel,k),
          actual_inner_squares=trap_segment(x,possq,0,k),
          actual_outer_squares=trap_segment(x,possq,k),
          actual_inner_cubic=trap_segment(x,cub,0,k),
          actual_outer_cubic=trap_segment(x,cub,k),
          actual_inner_cubic_positive=trap_segment(x,np.maximum(cub,0),0,k),
          actual_inner_cubic_negative=trap_segment(x,np.minimum(cub,0),0,k),
          actual_outer_cubic_positive=trap_segment(x,np.maximum(cub,0),k),
          actual_outer_cubic_negative=trap_segment(x,np.minimum(cub,0),k),
          ch_Qminus=qm_int,ch_bulk_minus=bulk,ch_boundary_minus=bd,
          ch_factorization_residual=qm_int-bulk-bd,
          ch_Qplus=trap_segment(x,qp,k),
          vminus_cut=float(vm[k]),vminus_outer=float(vm[-1]),
          beta_cut=float(beta[k]),beta_outer=float(beta[-1]),
          max_outer_u_deviation=float(np.max(np.abs(u[k:]-uch[k:]))),
          max_outer_lambda_relative=float(np.max(np.abs(lam[k:]/lamch[k:]-1))),
          max_outer_abc_relative=float(np.max(np.abs(abc[k:]/abcch[k:]-1))),
          max_outer_G_relative=float(np.max(np.abs(G[k:]/(x[k:]*(1+x[k:]))-1)))))
    costs=c.full_report(z)
    out=dict(source=str(path),x0=c.x0,deg=c.degU,wpow=c.wpow,costs=costs,
      exact_integrals=dict(relative_total=trap_segment(x,rel),squares=trap_segment(x,possq),
        cubic=trap_segment(x,cub),cubic_positive=trap_segment(x,np.maximum(cub,0)),
        cubic_negative=trap_segment(x,np.minimum(cub,0)),scalar=trap_segment(x,scal)),
      whole_profile_deviation_from_CH=dev,rows=rows)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--out'); ap.add_argument('--n',type=int,default=4001)
    args=ap.parse_args(); out=analyze(args.record,args.n); txt=json.dumps(out,indent=1); print(txt)
    if args.out: Path(args.out).write_text(txt+'\n')
if __name__=='__main__': main()
