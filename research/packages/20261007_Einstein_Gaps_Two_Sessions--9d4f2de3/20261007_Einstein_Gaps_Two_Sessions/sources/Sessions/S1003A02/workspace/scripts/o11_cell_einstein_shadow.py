"""Empirical comparison of the certified X=8 cell with Einstein bolt trajectories.

The certified fixed-slot cell has bolt radius b=sqrt(x0), exact CH collar, and a
charge-four anisotropy d=(a1-a2)/t^4 at the bolt.  We reconstruct its geodesic
radial state (a_i,y_i), fit d, shoot the Ric=-6 Einstein ODE from the same bolt
jet, and compare the two state curves.  This tests (rather than assumes) the
picture that a low-P cell shadows an Einstein separatrix and pays only in a late
CR-correction layer.
"""
import json, sys
from pathlib import Path
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from einstein_bolt_shoot import Bolt, rhs, constraint
from o11_collar_independent_verify import Metric

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
REC=Path(sys.argv[1]) if len(sys.argv)>1 else (Path(__file__).resolve().parents[4]/"Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json")
if not REC.is_absolute(): REC=(HERE/REC).resolve()
OUT=ROOT/'data'/'o11_cell_einstein_shadow.json'
FIG=ROOT/'figures'/'o11_cell_einstein_shadow.png'

rec=json.loads(REC.read_text().strip().splitlines()[-1]); m=Metric(rec)
# q=sqrt(x-x0) regularizes geodesic distance at the bolt.
qmax=np.sqrt(m.X-m.x0); q=np.linspace(0,qmax,6001); q[0]=1e-7
x=m.x0+q*q
prof=jax.vmap(m.profile)(jnp.asarray(x)); G=np.array(prof[0],copy=True)
avec=np.array(jax.vmap(lambda xx:m.axes(xx)[1])(jnp.asarray(x)),copy=True)
dadx=np.array(jax.vmap(jax.jacfwd(lambda xx:m.axes(xx)[1]))(jnp.asarray(x)),copy=True)
ycell=2*np.sqrt(G)[:,None]*dadx/avec
# dt/dq = q/sqrt(G); fill removable bolt value by extrapolation.
dtdq=q/np.sqrt(G); dtdq[0]=dtdq[1]
t=np.concatenate([[0.0], cumulative_trapezoid(dtdq,q)])
# Reset numerical bolt axes/y.
b=float(np.sqrt(m.x0)); avec[0]=[b,b,0.0]
# Fit (a1-a2)/t^4 = d + O(t^2) on a short but non-roundoff interval.
mask=(t>2e-3)&(t<2e-2)
T2=t[mask]**2; ratio=(avec[mask,0]-avec[mask,1])/t[mask]**4
coef=np.polyfit(T2,ratio,2); dfit=float(coef[-1])
# Direct profile predicts the opposite slot branch depending on sign; shoot the exact same jet.
bolt=Bolt(1); t0=2e-3
z0=bolt.init(b,dfit,t0)
sol=solve_ivp(rhs,(t0,max(6.0,float(t[-1])+0.2)),z0,method='DOP853',rtol=2e-13,atol=2e-14,
              dense_output=True)
# Never extrapolate dense output beyond the actual solver interval.
valid=(t>=0.02)&(t<=sol.t[-1])
Z=sol.sol(t[valid]); aein=np.exp(Z[:3].T); yein=Z[3:].T
logad=np.linalg.norm(np.log(avec[valid]/aein),axis=1)
ydist=np.linalg.norm(ycell[valid]-yein,axis=1)
# ACH coordinates.  Cell collar has fibre slot 2, kappa2=a2/(a3*a1), rho2=a3/a1.
def ach2(a,y):
    kap=a[:,1]/(a[:,2]*a[:,0]); rho=a[:,2]/a[:,0]
    dev=np.sqrt((y[:,1]-2)**2+(y[:,0]-1)**2+(y[:,2]-1)**2)
    return kap,rho,dev
kc,rc,dc=ach2(avec[valid],ycell[valid]); ke,re,de=ach2(aein,yein)
tv=t[valid]
# Cumulative positive Ricci0 action using the independently reconstructed formula.
dens=np.array(jax.vmap(m.density_x)(jnp.asarray(x)),copy=True)
pdx=dens[:,4]  # already includes dx conversion factor 1/(2 sqrt G)
Pc=np.concatenate([[0.0],cumulative_trapezoid(pdx,x)])
Ptot=float(Pc[-1]); Pfrac=Pc/Ptot
quant={}
for qq in [0.1,0.25,0.5,0.75,0.9,0.99]:
    ii=int(np.searchsorted(Pfrac,qq)); quant[str(qq)]={"x":float(x[ii]),"t":float(t[ii])}
# deviation becomes large relative to core scale well before collar if tracking fails.
rows=[]
for ts in [v for v in [0.02,0.05,0.1,0.2,float(sol.t[-1])] if v<=tv[-1]+1e-12]:
    ii=int(np.argmin(np.abs(tv-ts)))
    rows.append(dict(t=float(tv[ii]),x=float(x[valid][ii]),
                     log_axes_distance=float(logad[ii]),y_distance=float(ydist[ii]),
                     cell_kappa2=float(kc[ii]),cell_rho2=float(rc[ii]),cell_ACH2_dev=float(dc[ii]),
                     ein_kappa2=float(ke[ii]),ein_rho2=float(re[ii]),ein_ACH2_dev=float(de[ii])))
out=dict(source=str(REC),b=b,d_fit=dfit,d_fit_poly=[float(v) for v in coef],
         cell_t_outer=float(t[-1]),ein_status=int(sol.status),ein_tend=float(sol.t[-1]),
         ein_constraint_initial=float(constraint(z0)),P_positive=Ptot,
         P_quantiles=quant,comparison=rows,
         interpretation=("The same-bolt Einstein orbit is not an ACH2 separatrix when b=0.1; "
                         "the recorded distances test local shadowing only and stop at the actual solver endpoint."))
OUT.write_text(json.dumps(out,indent=1)+'\n')

fig,ax=plt.subplots(1,3,figsize=(13,3.8))
ax[0].plot(tv,dc,label='cell ACH2 dev'); ax[0].plot(tv,de,label='Einstein ACH2 dev')
ax[0].set_yscale('log'); ax[0].set_xlabel('geodesic t'); ax[0].set_ylabel('ACH2 state deviation'); ax[0].legend()
ax[1].plot(tv,logad,label='log-axis distance'); ax[1].plot(tv,ydist,label='y distance')
ax[1].set_yscale('log'); ax[1].set_xlabel('geodesic t'); ax[1].legend()
ax[2].plot(t,Pfrac,label='cumulative $|Ric^o|^2$ fraction'); ax[2].set_xlabel('geodesic t'); ax[2].set_ylim(0,1.02); ax[2].legend()
fig.suptitle(f'Certified cell vs same-bolt Einstein orbit: b={b:.3f}, d={dfit:.3g}')
fig.tight_layout(); FIG.parent.mkdir(exist_ok=True); fig.savefig(FIG,dpi=190); plt.close(fig)
print(json.dumps(out,indent=1))
