#!/usr/bin/env python3
"""Convert a Darboux-gauge formal AKE jet to A01's independent (g,omega) jet equations.

The coordinate change y=x+v(x) is chosen order by order so that y are geodesic
normal coordinates for the Darboux metric: solve the geodesic exponential map
x(y) from x''^a+Gamma^a_bc(x)x'^b x'^c=0, x(0)=0, x'(0)=y.
Then pull back g and the constant symplectic form.  This gives a genuinely
independent representation of the same finite jet and can be evaluated by
step62_zero_prolong.system.
"""
import json, os, sys
from pathlib import Path
import numpy as np
import torch
HERE=Path(__file__).resolve().parent
A02=HERE.parents[2]/'S1003A02'/'workspace'
sys.path.insert(0,str(A02/'scripts')); sys.path.insert(0,str(HERE))
import step79_general_order6 as G
from step77_gn_germ import ricci_E, OM
import step62_zero_prolong as Z
from step53_ak_einstein_jets import Poly
OUT=HERE.parent/'data'/'step67'; OUT.mkdir(parents=True,exist_ok=True)

def exp_map_coeffs(T,jets,D=8):
    """Return x(y) coefficients, shape (4,P.M), via Picard iteration in t."""
    R=T.R; H=T.H(jets); _,Gam=ricci_E(R,H,T.lam)
    # Homogeneous polynomial x(y); identity plus corrections. t-weight equals y degree.
    X=torch.zeros((4,R.nm),dtype=G.dt,device=G.dev)
    for a in range(4):
        e=tuple(1 if k==a else 0 for k in range(4)); X[a,R.idx[e]]=1.0
    # Polynomial composition f(x(y)) using powers and R.mm.
    one=torch.zeros(R.nm,dtype=G.dt,device=G.dev); one[0]=1.0
    def pmul(a,b): return R.mm(a,b,'p,p->p')
    def compose(f,Xc):
        powers=[]
        for k in range(4):
            pp=[one]
            for n in range(1,D+1): pp.append(pmul(pp[-1],Xc[k]))
            powers.append(pp)
        out=torch.zeros(R.nm,dtype=G.dt,device=G.dev)
        for i,m in enumerate(R.mons):
            if float(f[i])==0: continue
            p=one
            for k in range(4): p=pmul(p,powers[k][m[k]])
            out=out+f[i]*p
        return out
    # At fixed point, acceleration A^a(y)=-Gamma^a_bc(X)y^b y^c.
    ymono=[]
    for a in range(4):
        v=torch.zeros(R.nm,dtype=G.dt,device=G.dev); v[R.idx[tuple(1 if k==a else 0 for k in range(4))]]=1
        ymono.append(v)
    for it in range(D):
        Acc=torch.zeros_like(X)
        for a in range(4):
            aa=torch.zeros(R.nm,dtype=G.dt,device=G.dev)
            for b in range(4):
                for c in range(4):
                    gc=compose(Gam[a,b,c],X)
                    aa=aa-pmul(pmul(gc,ymono[b]),ymono[c])
            Acc[a]=aa
        Xnew=X.clone()
        # If x(t)=sum x_m(y)t^m, x''=sum m(m-1)x_m t^(m-2);
        # Gamma(x(t)) x'(t)^2 at t=1 is represented by Acc homogeneous degree m,
        # so divide each degree-m component by m(m-1).
        for i,multi in enumerate(R.mons):
            d=sum(multi)
            if d>=2: Xnew[:,i]=Acc[:,i]/(d*(d-1))
        if float((Xnew-X).norm())<1e-14: X=Xnew; break
        X=Xnew
    return X,H

def compose_scalar(R,f,X,D):
    one=torch.zeros(R.nm,dtype=G.dt,device=G.dev); one[0]=1
    def mul(a,b): return R.mm(a,b,'p,p->p')
    powers=[]
    for k in range(4):
        pp=[one]
        for n in range(1,D+1): pp.append(mul(pp[-1],X[k]))
        powers.append(pp)
    out=torch.zeros(R.nm,dtype=G.dt,device=G.dev)
    for i,m in enumerate(R.mons):
        if float(f[i])==0: continue
        p=one
        for k in range(4): p=mul(p,powers[k][m[k]])
        out=out+f[i]*p
    return out

def convert(name):
    meta=json.loads((A02/'data'/'step80'/f'{name}.json').read_text()); lam=float(meta['lam'])
    dd=np.load(A02/'data'/'step80'/f'{name}.npz'); T=G.TowerAll(6,lam); D=8; R=T.R
    jets={k:torch.tensor(dd[f'H{k}'],dtype=G.dt,device=G.dev) for k in T.degs}
    X,H=exp_map_coeffs(T,jets,D)
    g,_=ricci_E(R,H,lam)  # wrong object placeholder; rebuild exp(H) exactly as in ricci_E below
    # Rebuild exp(H), same truncation as source.
    eye=torch.zeros(4,4,R.nm,dtype=G.dt,device=G.dev)
    for i in range(4): eye[i,i,0]=1
    gd=eye+H; Pw=H; fact=1.0
    for n in range(2,D//2+1):
        Pw=R.mm(Pw,H,'ikp,kjp->ijp'); fact*=n; gd=gd+Pw/fact
    # Jacobian dx/dy.
    J=torch.stack([torch.stack([R.diff(X[a],i) for i in range(4)]) for a in range(4)]) # a,i,p
    gc=torch.stack([torch.stack([compose_scalar(R,gd[a,b],X,D) for b in range(4)]) for a in range(4)])
    # pullback metric J^a_i J^b_j g_ab(X)
    tmp=R.mm(J,gc,'aip,abp->ibp'); gn=R.mm(tmp,J,'ibp,bjp->ijp')
    # pullback omega_ab constant
    Om=torch.tensor(OM,dtype=G.dt,device=G.dev)
    tmpw=torch.einsum('aip,ab->ibp',J,Om); wn=R.mm(tmpw,J,'ibp,bjp->ijp')
    # Encode in Step62 z ordering.
    S=Z.setup(D); P=S['P']; assert R.mons==P.L
    idx=np.where(P.deg>=2)[0]; n=len(idx); z=np.zeros(S['nvar'])
    off=0
    for q,(i,j) in enumerate(Z.TRI): z[q*n:(q+1)*n]=gn[i,j,idx].cpu().numpy()
    off=10*n
    for q,(i,j) in enumerate(Z.PAIRS): z[off+q*n:off+(q+1)*n]=wn[i,j,idx].cpu().numpy()
    sysv=np.asarray(S['system'](z,lam))[S['keep']]
    by={}
    for row,val in zip(S['keep'],sysv):
        key=f"E{S['rowtype'][row]}_d{S['rowdeg'][row]}"; by[key]=by.get(key,0.0)+float(val*val)
    # first-order normality
    d1=[i for i,d in enumerate(P.deg) if d==1]
    normal_linear=float(np.linalg.norm(gn[:,:,d1].cpu().numpy()))
    mv=np.asarray(Z.Mvec(S,z)); det=float(np.linalg.det(mv[:16].reshape(4,4)))
    Xid=torch.zeros_like(X)
    for a in range(4): Xid[a,R.idx[tuple(1 if k==a else 0 for k in range(4))]]=1.0
    out={'name':name,'lam':lam,'normal_metric_linear_norm':normal_linear,
         'system_total_norm':float(np.linalg.norm(sysv)),'worst':dict(sorted(((k,v**0.5) for k,v in by.items()),key=lambda kv:-kv[1])[:12]),
         'Mvec_det':det,'Mvec_norm':float(np.linalg.norm(mv)),'coordinate_map_correction_norm':float((X-Xid).norm())}
    return out,z

def main():
    names=sys.argv[1:] or ['recon_F012_gen5_lam-5']
    oo=[]
    for n in names:
        o,z=convert(n); oo.append(o); np.save(OUT/f'normaljet_{n}.npy',z); print(json.dumps(o,indent=1),flush=True)
    (OUT/'normal_coordinate_crosscheck.json').write_text(json.dumps(oo,indent=1)+'\n')
if __name__=='__main__': main()
