"""Independent spin/calibration evaluation of an exported diagonal perpendicular profile.

Input is the peer NPZ containing x,G,h and their first two x derivatives.  No
polynomial coefficients or peer curvature routines are used.  In bolt-adapted axes
(a,b,c)=(old sigma2,old sigma3,old sigma1), compute u, udot, C, the original
positive P squares, relative squares/cubic, scalar square, and cut-wise payments.
"""
from pathlib import Path
import argparse,json
import numpy as np


def gamma_and_dx(a,ax):
    n=len(a); gam=np.empty_like(a); gx=np.empty_like(a)
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        ai,aj,ak=a[:,i],a[:,j],a[:,k]
        gam[:,i]=(aj*aj+ak*ak-ai*ai)/(aj*ak)
        di=-2*ai/(aj*ak)
        dj=1/ak-ak/(aj*aj)+ai*ai/(aj*aj*ak)
        dk=1/aj-aj/(ak*ak)+ai*ai/(aj*ak*ak)
        gx[:,i]=di*ax[:,i]+dj*ax[:,j]+dk*ax[:,k]
    return gam,gx

def integ(x,y,i0=1,i1=None):
    if i1 is None:i1=len(x)-1
    return float(np.trapezoid(y[i0:i1+1],x[i0:i1+1]))

def evaluate(path,cuts=(.05,.08,.1,.15,.2,.3,.5)):
    d=np.load(path); x=d['x']; G=d['G']; Gp=d['Gp']; h=d['h']; hp=d['hp']; hpp=d['hpp']
    # even cyclic permutation of orbit axes
    order=[1,2,0]
    q=np.stack([h[:,i,i] for i in order],axis=1)
    qx=np.stack([hp[:,i,i] for i in order],axis=1)
    qxx=np.stack([hpp[:,i,i] for i in order],axis=1)
    a=np.sqrt(q); ax=qx/(2*a); axx=qxx/(2*a)-qx*qx/(4*a**3)
    # Exclude the exact bolt point G=0 from differential densities.
    sqG=np.sqrt(np.maximum(G,0)); adot=2*sqG[:,None]*ax
    dadot=np.full_like(a,np.nan)
    dadot[1:]=(Gp[1:,None]/sqG[1:,None])*ax[1:]+2*sqG[1:,None]*axx[1:]
    gam,gamx=gamma_and_dx(a,ax)
    u=adot-gam; udot=np.full_like(u,np.nan)
    udot[1:]=2*sqG[1:,None]*(dadot[1:]-gamx[1:])
    H=np.column_stack([u[:,0]+u[:,1]*u[:,2]/2,
                       u[:,1]+u[:,2]*u[:,0]/2,
                       u[:,2]+u[:,0]*u[:,1]/2])
    lam=np.column_stack([a[:,1]*a[:,2]/a[:,0],a[:,2]*a[:,0]/a[:,1],a[:,0]*a[:,1]/a[:,2]])
    inv=np.full_like(x,np.nan);inv[1:]=1/(2*sqG[1:])
    C=np.sum(u*u,axis=1)+np.prod(u,axis=1)
    # The bolt-point formulas have removable 0/0 singularities; integrations start
    # at index 1. Replace only index 0 by the exact smooth bolt limits so that
    # sign-split arrays do not propagate NaN into an otherwise valid segment.
    u[0]=np.array([0.0,0.0,-1.0]); C[0]=1.0
    psq=np.sum(lam/4*(udot-2*H/lam)**2,axis=1)*inv
    s1=lam[:,0]/4*(udot[:,0]+2*H[:,0]/lam[:,0])**2*inv
    s2=lam[:,1]/4*(udot[:,1]-(2*u[:,1]-u[:,0]*u[:,2])/lam[:,1])**2*inv
    s3=lam[:,2]/4*(udot[:,2]+2*H[:,2]/lam[:,2])**2*inv
    cub=2*np.prod(u,axis=1)/lam[:,1]*inv
    Sigma=np.sum(udot/a+2*H/(np.roll(a,-1,axis=1)*np.roll(a,-2,axis=1)),axis=1)
    scalar=np.prod(a,axis=1)/4*(Sigma-12)**2*inv
    for arr in (psq,s1,s2,s3,cub,scalar): arr[0]=0.0
    rel=s1+s2+s3+cub
    out=dict(source=str(path),x0=float(d['x0']),X=float(d['X']),theta=float(d['theta']),wpow=int(d['wpow']),
      endpoints=dict(u_near_bolt=u[1].tolist(),u_collar=u[-1].tolist(),C_near_bolt=float(C[1]),C_collar=float(C[-1])),
      minima=dict(C=float(np.nanmin(C)),x_C=float(x[np.nanargmin(C)]),cubic_product=float(np.nanmin(np.prod(u,axis=1))),x_cubic=float(x[np.nanargmin(np.prod(u,axis=1))])),
      integrals=dict(P_positive=integ(x,psq),relative_total=integ(x,rel),relative_squares=integ(x,s1+s2+s3),
        cubic=integ(x,cub),cubic_positive=integ(x,np.maximum(cub,0)),cubic_negative=integ(x,np.minimum(cub,0)),
        scalar=integ(x,scalar),J=integ(x,psq+scalar),relative_residual=integ(x,psq)-(1+integ(x,rel))))
    rows=[]
    for cut in cuts:
        if not x[1]<cut<x[-1]:continue
        k=int(np.searchsorted(x,cut))
        rows.append(dict(xcut=float(x[k]),inner_relative=integ(x,rel,1,k),outer_relative=integ(x,rel,k),
          inner_squares=integ(x,s1+s2+s3,1,k),outer_squares=integ(x,s1+s2+s3,k),
          inner_cubic=integ(x,cub,1,k),outer_cubic=integ(x,cub,k),
          inner_cubic_positive=integ(x,np.maximum(cub,0),1,k),inner_cubic_negative=integ(x,np.minimum(cub,0),1,k),
          outer_cubic_positive=integ(x,np.maximum(cub,0),k),outer_cubic_negative=integ(x,np.minimum(cub,0),k),
          u=u[k].tolist(),C=float(C[k])))
    out['rows']=rows
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('npz');ap.add_argument('--out');a=ap.parse_args()
    out=evaluate(a.npz);txt=json.dumps(out,indent=1);print(txt)
    if a.out:Path(a.out).write_text(txt+'\n')
if __name__=='__main__':main()
