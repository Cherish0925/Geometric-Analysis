"""Check the radial conformal Euler equation on a diagonal cell profile.

For Ric=-6 normalization, inherited variation formula:
    delta J6[2 f g] = 4 int f (Delta_+ + 6)e dV,  e=s+24,
where Delta_+=-div grad.  A compactly supported radial critical metric must satisfy
    L e := -(e'' + (W'/W)e') + 6e = 0
in geodesic radius t, W=a1 a2 a3.  Since d/dt=2 sqrt(G)d/dx,
    div grad e = e_tt + (W_t/W)e_t.

This script evaluates e, L e, weighted norms, and the scalar energy for a stored
ordinary or conformal record.  It is a numerical stationarity test, not a proof.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from perp_dual_cost import DualCell,load_record,seed_vector
from perp_conformal_lm import ConformalCell
from perp_lm import residual_fn


def make(rec,nq):
    deg=int(rec['deg']); x0=float(rec['x0']); X=float(rec['X']); dphi=int(rec.get('dphi',0))
    if dphi:
        c=ConformalCell(x0,X,deg,dphi,nq); z=np.asarray(rec['z'],float)
    else:
        c=DualCell(x0,X,deg,deg,nq); c.aligned=False;c.wpow=2;z=np.asarray(seed_vector(c,rec),float)
    return c,jnp.asarray(z)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('record');ap.add_argument('--out');ap.add_argument('--n',type=int,default=4001)
    a=ap.parse_args();rec=load_record(a.record);c,z=make(rec,1200);prof=c.prof_factory(z)
    # State and scalar from the same exact Cartan formulas as the optimization.
    def state(x):
        G,h=prof(x); aa=jnp.sqrt(jnp.array([h[1,1],h[2,2],h[0,0]]))
        da=jax.jacfwd(lambda xx:jnp.sqrt(jnp.array([prof(xx)[1][1,1],prof(xx)[1][2,2],prof(xx)[1][0,0]])))(x)*2*jnp.sqrt(G)
        a1,a2,a3=aa
        u=jnp.array([da[0]-(a2*a2+a3*a3-a1*a1)/(a2*a3),da[1]-(a3*a3+a1*a1-a2*a2)/(a3*a1),da[2]-(a1*a1+a2*a2-a3*a3)/(a1*a2)])
        return G,aa,u
    def scalar(x):
        G,aa,u=state(x);du=jax.jacfwd(lambda xx:state(xx)[2])(x)*2*jnp.sqrt(G)
        u1,u2,u3=u;H=jnp.array([u1+u2*u3/2,u2+u3*u1/2,u3+u1*u2/2])
        r=du/aa;v=2*H/jnp.array([aa[1]*aa[2],aa[2]*aa[0],aa[0]*aa[1]])
        return -2*jnp.sum(r+v)
    def vals(x):
        G,aa,u=state(x);W=jnp.prod(aa);e=scalar(x)+24
        ex=jax.grad(lambda xx:scalar(xx))(x); et=2*jnp.sqrt(G)*ex
        ett=2*jnp.sqrt(G)*jax.grad(lambda xx:2*jnp.sqrt(state(xx)[0])*jax.grad(lambda yy:scalar(yy))(xx))(x)
        Wt=2*jnp.sqrt(G)*jax.grad(lambda xx:jnp.prod(state(xx)[1]))(x)
        Le=-(ett+Wt/W*et)+6*e
        return G,W,e,Le
    us=np.linspace(1e-5,1-1e-5,a.n);xs=c.x0*np.exp(c.ell*us)
    VV=jax.jit(jax.vmap(vals))(jnp.asarray(xs))
    G,W,e,Le=[np.asarray(q) for q in VV];dx=np.diff(xs)
    # int_{SU(2)} sigma1^sigma2^sigma3 = 2 pi^2, dt=dx/(2 sqrt G):
    # dV_radial = pi^2 W dx/sqrt(G).
    dv=math.pi**2*W/np.sqrt(G)
    def trap(q):return float(np.sum(.5*(q[1:]+q[:-1])*dx))
    en=trap(dv*e*e)/(32*math.pi**2);Ln=math.sqrt(trap(dv*Le*Le)/trap(dv));enorm=math.sqrt(trap(dv*e*e)/trap(dv))
    # Interior sup excludes endpoint contact layers and bolt removable-singularity roundoff.
    m=(us>.01)&(us<.99)
    out=dict(record=a.record,x0=c.x0,X=c.X,deg=int(rec['deg']),dphi=int(rec.get('dphi',0)),
             scalar_energy_over_8pi2=en,e_weighted_rms=enorm,Le_weighted_rms=Ln,
             e_sup_interior=float(np.max(np.abs(e[m]))),Le_sup_interior=float(np.max(np.abs(Le[m]))),
             e_min=float(e[m].min()),e_max=float(e[m].max()))
    print(json.dumps(out,indent=1));
    if a.out:Path(a.out).write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':main()
