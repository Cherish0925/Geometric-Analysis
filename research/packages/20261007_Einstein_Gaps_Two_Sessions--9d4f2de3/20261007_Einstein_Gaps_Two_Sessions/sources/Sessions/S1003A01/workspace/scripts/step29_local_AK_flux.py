"""Step 29: verify the boundary-corrected local almost-Kahler identity on an actual cell.

For a smooth diagonal perpendicular exact-CH cell, the local identity supplied in Step 29 is
  Phat[t0,t1] = int L_AK dt + B(t1)-B(t0),
  B=b_+ - 3 F - 9 Pm^2 - 6 W u u',
  F=4 Pm cosh(q)-Pm Pm_TT-Pm_T^2/2.
Here Pm is the canonical AK moment (called mathcal P in the note), prime on u is
original arclength t, and L_AK is the complete all-scalar density of Theorem A.
The exact CH value is B=2.  This script checks the relation on terminal intervals of
actual optimized cells and compares B-2 to its linear CH expression -A(x)w^2 from
step29_ak_exterior_bridge.py.

Usage: python step29_local_AK_flux.py RECORD --out OUT.json
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import cumulative_trapezoid

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--out')
    ap.add_argument('--npanel',type=int,default=1200); a=ap.parse_args()
    rec=load_record(a.record); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec.get('deg',rec.get('degU',6)))
    cell=make_cell(x0,deg,400,smooth_mode=True,X=X); z=jnp.asarray(seed_vector(cell,rec)); prof=cell.prof_factory(z)

    def slots(x):
        G,h=prof(x); d=jnp.diag(h)
        return G,jnp.sqrt(jnp.array([d[2],d[1],d[0]])) # f,g,h
    def jet(x):
        G,A=slots(x); Ax=jax.jacfwd(lambda xx: slots(xx)[1])(x)
        Axx=jax.jacfwd(jax.jacfwd(lambda xx: slots(xx)[1]))(x)
        Gx=jax.grad(lambda xx: slots(xx)[0])(x)
        return G,A,2*jnp.sqrt(G)*Ax,4*G*Axx+2*Gx*Ax

    ell=np.log(X/x0)
    # canonical moment Pm, normalized by Pm(X)=X.
    ud=np.concatenate([np.geomspace(1e-10,1e-3,20000,endpoint=False),np.linspace(1e-3,1.0,200000)])
    xd=x0*np.exp(ell*ud); Gd,Ad=[np.asarray(v) for v in jax.vmap(slots)(jnp.asarray(xd))]
    dlogPm_du=2*Ad[:,0]/(Ad[:,1]*Ad[:,2])/(2*np.sqrt(Gd))*ell*xd
    logPm=cumulative_trapezoid(dlogPm_du,ud,initial=0.0); logPm+=np.log(X)-logPm[-1]
    def pm_interp(x): return np.exp(np.interp(np.log(x/x0)/ell,ud,logPm))

    # Panel edges include scientifically useful interfaces.
    sections=np.array([v for v in [0.1,0.2,0.5,1.0,2.0,5.0,10.0,20.0,50.0] if x0<v<X])
    edges=np.unique(np.concatenate([np.geomspace(max(0.08,x0*(1+1e-8)),X,a.npanel+1),sections,[X]]))
    gx,gw=np.polynomial.legendre.leggauss(16)
    xs=np.concatenate([(lo+hi)/2+(hi-lo)/2*gx for lo,hi in zip(edges[:-1],edges[1:])])
    wx=np.concatenate([(hi-lo)/2*gw for lo,hi in zip(edges[:-1],edges[1:])])
    G,A,At,Att=[np.asarray(v) for v in jax.vmap(jet)(jnp.asarray(xs))]
    af,ag,ah=A.T; y=At/A; yt=Att/A-y*y; S=y.sum(1); W=af*ag*ah
    def Porb(ai,aj,ak): return 2*(ai**4-(aj**2-ak**2)**2)/W**2
    Por=np.stack([Porb(af,ag,ah),Porb(ag,ah,af),Porb(ah,af,ag)],1)
    R00=-(yt+y*y).sum(1); Rii=-yt-S[:,None]*y+Por; s=R00+Rii.sum(1)
    ric0sq=(R00-s/4)**2+((Rii-s[:,None]/4)**2).sum(1)
    gam=np.stack([(ag**2+ah**2-af**2)/(ag*ah),(ah**2+af**2-ag**2)/(ah*af),(af**2+ag**2-ah**2)/(af*ag)],1)
    def gdot(ai,aj,ak,di,dj,dk):
        N=aj**2+ak**2-ai**2; M=aj*ak
        return (2*(aj*dj+ak*dk-ai*di)*M-N*(dj*ak+aj*dk))/M**2
    dfa,dga,dha=At.T
    gamt=np.stack([gdot(af,ag,ah,dfa,dga,dha),gdot(ag,ah,af,dga,dha,dfa),gdot(ah,af,ag,dha,dfa,dga)],1)
    vv=At-gam; vt=Att-gamt; vj=np.roll(vv,-1,1); vk=np.roll(vv,-2,1); aj=np.roll(A,-1,1); ak=np.roll(A,-2,1)
    Rp=-vt/(2*A)+(-vv-vj*vk/2)/(aj*ak); Wp=Rp-s[:,None]/12
    Pm=pm_interp(xs); u2=Pm/(ag*ah); uu=np.sqrt(u2)
    lam_t=2*af/(ag*ah); upr=.5*uu*(lam_t-y[:,1]-y[:,2])
    q=np.log(ag/ah); qt=y[:,1]-y[:,2]; nu=-(qt+4*np.sinh(q)/af)/(2*uu)
    lam=(Wp[:,1]-Wp[:,2])/(2*u2); delta=Wp[:,0]/u2+4; dVh=W*u2*u2
    Pdens=W*ric0sq/4
    Ldens=12*W*(u2+s/24)**2+6*W*upr**2+1.5*delta**2*dVh+2*lam**2*dVh-6*nu**2*dVh
    dtdx=1/(2*np.sqrt(G)); Ppiece=Pdens*dtdx*wx; Lpiece=Ldens*dtdx*wx
    # Sum the 16 Gauss nodes per panel.
    npan=len(edges)-1; Ppan=Ppiece.reshape(npan,16).sum(1); Lpan=Lpiece.reshape(npan,16).sum(1)
    Ptail=np.cumsum(Ppan[::-1])[::-1]; Ltail=np.cumsum(Lpan[::-1])[::-1]

    def boundary_values(x):
        G0,A0,At0,Att0=[np.asarray(v) for v in jet(jnp.asarray(x))]
        af0,ag0,ah0=A0; y0=At0/A0; W0=np.prod(A0)
        gam0=np.array([(ag0**2+ah0**2-af0**2)/(ag0*ah0),(ah0**2+af0**2-ag0**2)/(ah0*af0),(af0**2+ag0**2-ah0**2)/(af0*ag0)])
        v0=At0-gam0; bp=2-np.dot(v0,v0)-np.prod(v0)
        uf=float(v0[0])  # a_f' - gamma_f; the bracket in Step 30's B-b_+ formula
        pm=float(pm_interp(x)); u20=pm/(ag0*ah0); u0=np.sqrt(u20)
        up0=.5*u0*(2*af0/(ag0*ah0)-y0[1]-y0[2])
        pT=2*u0*af0; pTT=2*((up0/u0)*af0+At0[0]) # d/dT(2u af)=2[(u'/u)af+af']
        F=4*pm*np.cosh(np.log(ag0/ah0))-pm*pTT-.5*pT*pT
        B=bp-3*F-9*pm*pm-6*W0*u0*up0
        # linear exterior variables reconstructed by contact closure.
        q0=np.log(ag0/ah0)
        qx=float(jax.grad(lambda xx: jnp.log(slots(xx)[1][1]/slots(xx)[1][2]))(jnp.asarray(x)))
        kval=(x/(1+x))**2; kx=2*x/(1+x)**3; f2=x*x/(1+x)**5
        wlin=2*(kx*q0+kval*qx)/f2
        Ach=-x*x*(3*x-2)/(4*(1+x)**5)
        Bminusbp_simple=6*pm*uf-9*pm*pm
        return {'x':float(x),'B':float(B),'B_minus_2':float(B-2),'bplus':float(bp),'F':float(F),'Pm':float(pm),
                'u_f':uf,'B_minus_bplus_direct':float(B-bp),'B_minus_bplus_simple':float(Bminusbp_simple),
                'B_minus_bplus_residual':float((B-bp)-Bminusbp_simple),
                'u':float(u0),'uprime':float(up0),'w_linear':float(wlin),'minus_Aw2':float(-Ach*wlin*wlin)}

    Bend=boundary_values(X)
    rows=[]
    for r in sections:
        i=int(np.where(np.isclose(edges,r,rtol=0,atol=1e-13))[0][0])
        Be=boundary_values(r)
        p=float(Ptail[i]); l=float(Ltail[i]); flux=float(Bend['B']-Be['B'])
        rows.append({'entry':Be,'P_tail':p,'int_L_AK_tail':l,'B_end_minus_B_entry':flux,
                     'local_identity_residual':p-l-flux,
                     'AK_tail_minus_raw':l-p,'B_entry_minus_B_end':-flux})
    out={'record':a.record,'x0':x0,'X':X,'B_end':Bend,'rows':rows,
         'normalization':'P/(8pi^2); W dt units; terminal exact-CH B=2'}
    txt=json.dumps(out,indent=1); print(txt)
    if a.out: Path(a.out).write_text(txt+'\n')
if __name__=='__main__': main()
