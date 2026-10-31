"""Finite-dimensional joint dual calibration for diagonal O(-1) CH cells (Step 16).

The trace-free diagonal Ricci tensor e=(e0,e1,e2,e3), sum e=0, is represented by
  z_i = r_i-v_i = -(e0+e_i),  i=1,2,3,
and |e|^2=sum z_i^2.  For any three-vector beta(t),
  (1/4) int W |e|^2 >= (1/2) int W z.beta - (1/4) int W |beta|^2.

This script compares three finite test spaces:
  A: scalar Green fields for the two independent orbit-shape equations;
  B: the exact relative-spin calibration direction grad(C-u2^2);
  joint: their union.
The maximum lower bound is (1/4) m^T G^+ m, where
  m_a=int W z.B_a,  G_ab=int W B_a.B_b.
This is a dual lower bound for P/(8 pi^2).  It cannot double-count channels because the
full Gram matrix is optimized once.  It is numerical evidence for the chosen witness,
not yet a competitor-independent calibration theorem.

Usage: python joint_dual_calibration.py RECORD.json [--n 8001] [--out OUT.json]
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import simpson, cumulative_simpson
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import arb, acb, ctx
from perp_rigorous_enclosure import FrozenCell


def load_profile(path, n):
    rec=json.loads(Path(path).read_text()); x0=float(rec.get('x0',.01)); X=float(rec['X'])
    ctx.prec=80; cell=FrozenCell(rec,x0=x0); ell=math.log(X/x0)
    v=np.linspace(0.,1.,n); ve=v.copy(); ve[0]=1e-7
    rows=[]
    for vv in ve:
        u=vv*vv; R,vol,pr=cell.ricci(acb(arb(u)),want_profile=True)
        f=lambda z: float(z.real.mid())
        rows.append([f(pr[k]) for k in ('x','h1','G','h3')]+[f(r) for r in R])
    A=np.asarray(rows); x,h1,G,h3=A[:,:4].T; R=A[:,4:]
    a=np.column_stack([np.sqrt(x),np.sqrt(h3),np.sqrt(h1)]) # bolt-adapted cyclic axes
    dxdu=ell*x; dtdv=dxdu*ve/np.sqrt(G)
    t=cumulative_simpson(dtdv,x=v,initial=0.)
    W=np.prod(a,axis=1); s=R.sum(1); e=R-s[:,None]/4
    # cyclic axes map (old radial,old1,old2,old3) -> (radial,old2,old3,old1)
    ec=np.column_stack([e[:,0],e[:,2],e[:,3],e[:,1]])
    z=-(ec[:,[0]]+ec[:,1:])
    # radii derivatives and spin variables in t
    av=np.empty_like(a)
    for i in range(3): av[:,i]=np.gradient(a[:,i],v,edge_order=2)/dtdv
    gam=np.column_stack([(a[:,1]**2+a[:,2]**2-a[:,0]**2)/(a[:,1]*a[:,2]),
                         (a[:,2]**2+a[:,0]**2-a[:,1]**2)/(a[:,2]*a[:,0]),
                         (a[:,0]**2+a[:,1]**2-a[:,2]**2)/(a[:,0]*a[:,1])])
    uspin=av-gam
    H=np.column_stack([uspin[:,0]+uspin[:,1]*uspin[:,2]/2,
                       uspin[:,1]+uspin[:,2]*uspin[:,0]/2,
                       uspin[:,2]+uspin[:,0]*uspin[:,1]/2])
    bspin=np.column_stack([2*H[:,0],uspin[:,0]*uspin[:,2],2*H[:,2]])
    return rec,v,t,dtdv,W,z,e,ec,uspin,H,bspin,a


def greens(t,W):
    n=len(t); out=[]
    # Both shape equations have the same scalar radial Green kernel, but their tensor
    # directions differ: log(a1/a3) -> (-1,0,1), log(a2/a1) -> (1,-1,0).
    b2=float(W[1]/t[1])
    # regularized G=int_t^T 1/W; use the bolt asymptotic W=b2*t.
    reg=np.zeros(n); reg[1:]=1/W[1:]-1/(b2*t[1:])
    # integrate from zero in t (the first interval error is O(t^2)).
    creg=cumulative_simpson(reg,x=t,initial=0.); Ireg=creg[-1]
    G=np.zeros(n); G[1:]=Ireg-creg[1:]+np.log(t[-1]/t[1:])/b2
    return G


def integrate(y,v):
    a=np.asarray(y,float).copy(); a[~np.isfinite(a)]=0.
    return float(simpson(a,x=v))


def gram_bound(B,z,mu,v,names,offset=None):
    k=B.shape[1]
    G=np.empty((k,k)); m=np.empty(k)
    if offset is None: offset=np.zeros(k)
    offset=np.asarray(offset,float)
    for i in range(k):
        m[i]=integrate(mu*np.sum(z*B[:,i,:],axis=1),v)-offset[i]
        for j in range(k): G[i,j]=integrate(mu*np.sum(B[:,i,:]*B[:,j,:],axis=1),v)
    ev=np.linalg.eigvalsh(G); Gi=np.linalg.pinv(G,rcond=1e-12)
    c=Gi@m
    value=float(m@c)/4
    return dict(names=names,m=m.tolist(),boundary_offset=offset.tolist(),Gram=G.tolist(),eigenvalues=ev.tolist(),coefficients=c.tolist(),bound=value)


def evaluate(path,n):
    rec,v,t,dtdv,W,z,e,ec,u,H,bspin,a=load_profile(path,n)
    mu=W*dtdv; G=greens(t,W)
    ones=np.ones_like(G)
    d13=np.array([-1.,0.,1.]); d21=np.array([1.,-1.,0.])
    fields=[]; names=[]
    # Green normalization from the scalar shape equations: if q=c.z with
    # c in {d13,d21}, then (W q')'=W(V-E) with E=-c.z.  Thus the Ricci
    # moment supplied by transport is c.z=-E; the tensor field uses -c.
    for tag,psi in [('1',ones),('G',G)]:
        fields.extend([-psi[:,None]*d13,-psi[:,None]*d21]); names.extend([tag+'_shape13',tag+'_shape21'])
    Bgreen=np.stack(fields,axis=1)
    # Correct spin beta field for the exact boundary identity:
    # B_i = a_i (partial_i Phi)/W = (partial_i Phi)/(a_j a_k), so
    # W z.B = sum_i (partial_i Phi) a_i z_i = dPhi/dt-2 sum_i p_i H_i/lambda_i.
    # Unlike bspin/a, this is also weighted-L2 integrable at the collapsing bolt.
    Bspin=(a*bspin/W[:,None])[:,None,:]
    P=integrate(mu*np.sum(z*z,axis=1),v)/4
    direct=dict(P_over_8pi2=P,
                z_norm_vs_ric0=integrate(mu*(np.sum(z*z,axis=1)-np.sum(ec*ec,axis=1)),v)/4)
    A=gram_bound(Bgreen,z,mu,v,names)
    S=gram_bound(Bspin,z,mu,v,['spin_grad_Phi'])
    J=gram_bound(np.concatenate([Bgreen,Bspin],axis=1),z,mu,v,names+['spin_grad_Phi'])
    # Scalar shape-channel share: projection onto all constant/G shape fields.
    for r in (A,S,J): r['share_of_P']=r['bound']/P
    return dict(record=path,x0=float(rec.get('x0',.01)),X=float(rec['X']),n=n,direct=direct,
                green_shape=A,spin=S,joint=J,joint_gain_over_max=J['bound']-max(A['bound'],S['bound']))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('records',nargs='+'); ap.add_argument('--n',type=int,default=8001); ap.add_argument('--out')
    a=ap.parse_args(); out=[]
    for p in a.records:
        r=evaluate(p,a.n); out.append(r); print(json.dumps(r,indent=1),flush=True)
    if a.out:
        payload=out[0] if len(out)==1 else out
        Path(a.out).write_text(json.dumps(payload,indent=1)+'\n')
if __name__=='__main__': main()
