"""Step 29: contact closure and frozen-profile transport capacities for canonical AK cells.

This is a scientific probe, not a uniform lower theorem.  It evaluates actual optimized profiles,
verifies the exact contact equation
  y_T+4y/A_f=-nu(1-y^2), y=tanh(q/2),
and computes frozen-coefficient minima of QA/2 = 1/2 int rho h_T^2 dT,
where h=mu*nu and rho=w/mu^2.

Capacity 1 fixes h(T0) and h(T1). Capacity 2 additionally fixes the *actual linearized contact
moment* int c(T) h(T)dT on [T0,T1], with c=eta(1-y^2)/mu.  Since this moment depends on y,
A_f and mu produced by the same metric, it is not varied independently; the calculation only asks
how much of the observed transport energy those two traces explain after the geometry is frozen.

Usage: python step29_capacity_contact.py RECORD [--eps 1e-5] [--out OUT.json]
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.integrate import cumulative_trapezoid
HERE=Path(__file__).resolve().parent; sys.path.insert(0,str(HERE))
from perp_dual_cost import make_cell,load_record,seed_vector


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--eps',type=float,default=1e-5); ap.add_argument('--out')
    a=ap.parse_args(); rec=load_record(a.record); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec.get('deg',rec.get('degU',6)))
    cell=make_cell(x0,deg,400,smooth_mode=True,X=X); z=jnp.asarray(seed_vector(cell,rec)); prof=cell.prof_factory(z)
    def slots(x):
        G,h=prof(x); d=jnp.diag(h); return G,jnp.sqrt(jnp.array([d[2],d[1],d[0]]))
    def jet(x):
        G,A=slots(x); Ax=jax.jacfwd(lambda xx:slots(xx)[1])(x); Axx=jax.jacfwd(jax.jacfwd(lambda xx:slots(xx)[1]))(x); Gx=jax.grad(lambda xx:slots(xx)[0])(x)
        return G,A,2*jnp.sqrt(G)*Ax,4*G*Axx+2*Gx*Ax
    ell=np.log(X/x0); ug=np.concatenate([np.geomspace(a.eps,1e-3,8000,endpoint=False),np.geomspace(1e-3,1.0,24000)])
    xs=x0*np.exp(ell*ug); G,A,At,Att=[np.asarray(v) for v in jax.vmap(jet)(jnp.asarray(xs))]
    af,ag,ah=A.T; ylog=At/A; yt=Att/A-ylog*ylog; W=af*ag*ah; dtdx=1/(2*np.sqrt(G)); dxdu=ell*xs; dtdu=dtdx*dxdu
    # canonical u normalized at collar
    logPm=cumulative_trapezoid(2*af/(ag*ah)*dtdu,ug,initial=0); logPm+=np.log(X)-logPm[-1]
    Pm=np.exp(logPm); u2=Pm/(ag*ah); uu=np.sqrt(u2); q=np.log(ag/ah); q_t=ylog[:,1]-ylog[:,2]; qT=q_t/uu
    Af=uu*af; y=np.tanh(q/2); nu=-(qT+4*np.sinh(q)/Af)/2
    # lambda by exact Cartan formula as in Step 28
    S=ylog.sum(1); defP=lambda ai,aj,ak:2*(ai**4-(aj**2-ak**2)**2)/W**2
    Por=np.stack([defP(af,ag,ah),defP(ag,ah,af),defP(ah,af,ag)],1); R00=-(yt+ylog*ylog).sum(1); Rii=-yt-S[:,None]*ylog+Por; s=R00+Rii.sum(1)
    gam=np.stack([(ag**2+ah**2-af**2)/(ag*ah),(ah**2+af**2-ag**2)/(ah*af),(af**2+ag**2-ah**2)/(af*ag)],1)
    def gd(ai,aj,ak,di,dj,dk):
        N=aj**2+ak**2-ai**2;M=aj*ak;return(2*(aj*dj+ak*dk-ai*di)*M-N*(dj*ak+aj*dk))/M**2
    dfa,dga,dha=At.T; gamt=np.stack([gd(af,ag,ah,dfa,dga,dha),gd(ag,ah,af,dga,dha,dfa),gd(ah,af,ag,dha,dfa,dga)],1)
    v=At-gam;vt=Att-gamt;vj=np.roll(v,-1,1);vk=np.roll(v,-2,1);AAj=np.roll(A,-1,1);AAk=np.roll(A,-2,1)
    Rp=-vt/(2*A)+(-v-vj*vk/2)/(AAj*AAk);Wp=Rp-s[:,None]/12;lam=(Wp[:,1]-Wp[:,2])/(2*u2)
    # T coordinate and exact contact residual
    T=cumulative_trapezoid(uu*dtdu,ug,initial=0); yT=np.gradient(y,T,edge_order=2); contact_res=yT+4*y/Af+nu*(1-y*y)
    # integrating factors normalized at the *outer* end to avoid huge ranges.
    # eta_T=4 eta/Af, eta(T1)=1.  mu_T/mu=2beta; use Step-28 closed expression.
    logeta=cumulative_trapezoid(4/Af,T,initial=0); logeta-=logeta[-1]; eta=np.exp(logeta)
    ci=4*np.cosh(q)/af*dtdu; C=cumulative_trapezoid(ci,ug,initial=0); C-=C[-1]; logmu=C-np.log(uu*af); mu=np.exp(logmu)
    h=mu*nu; what=uu**3*W # hatted volume density per dT
    rho=what/(mu*mu); QAhalf=np.trapezoid(2*lam*lam*what,T)
    # Avoid the artificial exact-collar endpoint where rho and h are tiny; keep all nodes with finite positive rho.
    mask=np.isfinite(rho)&(rho>1e-18)&np.isfinite(h); T=T[mask];rho=rho[mask];h=h[mask];eta=eta[mask];y=y[mask];nu=nu[mask];mu=mu[mask]
    # One-constraint capacity with both actual endpoint values.
    R=np.trapezoid(1/rho,T); dh=h[-1]-h[0]; cap1=.5*dh*dh/R
    # Linear contact moment M=int eta nu(1-y^2)dT = int c h dT.
    c=eta*(1-y*y)/mu; M=np.trapezoid(c*h,T)
    # Represent h=hlin+z, z endpoints 0.  Min 1/2 int rho h'^2 at fixed int c h=M.
    hlin=h[0]+dh*cumulative_trapezoid(1/rho,T,initial=0)/R
    Mlin=np.trapezoid(c*hlin,T); mres=M-Mlin
    # Green representer z solves -(rho z')'=c with z=0 at ends.  Integrate flux z'=(C0-int c)/rho.
    Cint=cumulative_trapezoid(c,T,initial=0); C0=np.trapezoid(Cint/rho,T)/R
    zp=(C0-Cint)/rho; zrep=cumulative_trapezoid(zp,T,initial=0); zrep-=zrep[0]
    # endpoint residual is quadrature noise; remove its tiny affine harmonic correction.
    zrep-=zrep[-1]*cumulative_trapezoid(1/rho,T,initial=0)/R
    gram=np.trapezoid(c*zrep,T); cap2=cap1+.5*mres*mres/gram if gram>0 else float('nan')
    # Observed energy reconstructed in h variables.
    hp=np.gradient(h,T,edge_order=2); Eobs=.5*np.trapezoid(rho*hp*hp,T)
    out={'record':a.record,'x0':x0,'X':X,'eps_u':a.eps,'T_interval':[float(T[0]),float(T[-1])],
         'contact':{'max_abs_residual_bulk':float(np.max(np.abs(contact_res[20:-20]))),'moment_actual_interval':float(M),
                    'eta_bolt_sample':float(eta[0]),'eta_outer':float(eta[-1]),'y_bolt_sample':float(y[0]),'y_outer':float(y[-1]),
                    'nu_sign_change':bool(np.any(np.signbit(nu[:-1])!=np.signbit(nu[1:]))),
                    'min_nu':float(np.min(nu)),'max_nu':float(np.max(nu))},
         'transport':{'QA_over_2_direct':float(QAhalf),'observed_half_int_rho_hT2':float(Eobs),'h_inner':float(h[0]),'h_outer':float(h[-1]),
                      'capacity_one_constraint':float(cap1),'one_over_observed':float(cap1/Eobs),
                      'moment_harmonic':float(Mlin),'moment_residual':float(mres),'green_gram':float(gram),
                      'capacity_two_constraint_frozen_linear':float(cap2),'two_over_observed':float(cap2/Eobs)},
         'scope':'Frozen-profile calculation. The weights, moment, and endpoints come from one actual metric; no uniformity over the competitor class is asserted.'}
    txt=json.dumps(out,indent=1);print(txt)
    if a.out:Path(a.out).write_text(txt+'\n')
if __name__=='__main__':main()
