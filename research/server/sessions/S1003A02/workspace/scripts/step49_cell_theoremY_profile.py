#!/usr/bin/env python3
"""Step 49: numerical Theorem-Y spectral profile of a frozen perpendicular CH cell.

The input is a floating DualCell record.  The script reconstructs the diagonal
Bianchi-IX metric, its diagonal self-dual Weyl operator in the orientation where
CH has spectrum (-4,2,2) at Ric=-6, and the constant-scalar Yamabe representative
u^2 g from the finite-volume solver in cell_yamabe_rv.py.

Conformal scaling: W^+ as an endomorphism scales by u^{-2}; dmu scales by u^4,
so the integral of any homogeneous quadratic Weyl expression is invariant, but
Psi contains the fixed scalar--4 Kähler orbit and must be evaluated from W/u^2
with the hatted volume u^4 dmu.  All reported integrals are divided by 8 pi^2.
This is floating quadrature, not an interval certificate.
"""
from pathlib import Path
import argparse, json, sys
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

HERE = Path(__file__).resolve().parent
WS = HERE.parent
PEER = WS.parents[1] / 'S1003A01' / 'workspace'
sys.path.insert(0, str(PEER / 'scripts'))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402


def phi_fun(x):
    x = np.asarray(x)
    r = (6*x + 14)/9
    return np.where(x <= 2/3, 0.5*r**3 - 4/3, 4*x)


def psi_from_eigs(eigs_hat):
    mu = np.sort(eigs_hat, axis=1)
    x = -mu[:, 0]
    psi = 4/3 + 2*np.sum(mu*mu, axis=1) - phi_fun(x)
    dist2 = (mu[:, 0]+2/3)**2 + (mu[:, 1]-1/3)**2 + (mu[:, 2]-1/3)**2
    split = 0.5*(mu[:, 2]-mu[:, 1])
    return psi, dist2, x, split, mu


def solve_yamabe(z, x, v, G, sigma, hz=0.006, xmax=1e11, tol=3e-14):
    """Solve 6 Delta w = sigma(1+w)+24(1+w)(2w+w^2), w->0.

    Inputs are sampled at arbitrary increasing z=log x nodes on the cell.  Append
    exact CH exterior (v=x/8, G=x+x^2, sigma=0) on a uniform logarithmic mesh.
    Finite-volume discretisation in z; node-volume weights use adjacent half cells.
    """
    ze = np.arange(z[-1]+hz, np.log(xmax)+hz, hz)
    zz = np.r_[z, ze]
    xx = np.exp(zz)
    ncell = len(z)
    vv = np.r_[v, xx[ncell:]/8]
    GG = np.r_[G, xx[ncell:] + xx[ncell:]**2]
    sig = np.r_[sigma, np.zeros(len(ze))]
    A = vv * 4*GG/xx
    B = vv * xx
    dh = np.diff(zz)
    Am = 2*A[:-1]*A[1:]/np.maximum(A[:-1]+A[1:], 1e-300)  # stable harmonic face mean
    D = np.zeros_like(zz)
    D[:-1] += dh/2
    D[1:] += dh/2
    w = np.zeros_like(zz)
    for it in range(80):
        f = sig*(1+w) + 24*(1+w)*(2*w+w*w)
        fp = sig + 24*(2+6*w+3*w*w)
        c = 6*Am/dh
        flux = c*np.diff(w)
        R = np.zeros_like(w)
        R[:-1] += flux
        R[1:] -= flux
        R -= B*D*f
        R[-1] = w[-1]
        main = np.zeros_like(w)
        main[:-1] -= c
        main[1:] -= c
        main -= B*D*fp
        lo = c.copy(); up = c.copy()
        lo[-1] = 0
        main[-1] = 1
        J = sps.diags([lo, main, up], [-1,0,1], format='csc')
        dw = spla.spsolve(J, -R)
        w += dw
        if np.max(np.abs(dw)) < tol:
            break
    return w[:ncell], it+1, float(w[-1]), float(w.min()), float(w.max())


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('record')
    ap.add_argument('--out',required=True)
    ap.add_argument('--panels',type=int,default=1600)
    ap.add_argument('--order',type=int,default=16)
    ap.add_argument('--xmax',type=float,default=1e11)
    ap.add_argument('--yamabe-ledger',help='Step-39 cell_yamabe_rv JSON for stable relative-volume/Weyl ledger')
    args=ap.parse_args()
    rec=load_record(args.record)
    x0=float(rec['x0']); X=float(rec['X']); deg=int(rec.get('deg',rec.get('degU',6)))
    cell=make_cell(x0,deg,400,smooth_mode=True,X=X)
    zcoef=jnp.asarray(seed_vector(cell,rec)); prof=cell.prof_factory(zcoef)
    def slots(x):
        G,h=prof(x); d=jnp.diag(h)
        return G,jnp.sqrt(jnp.array([d[2],d[1],d[0]])) # (f,g,h)
    def jet(x):
        G,A=slots(x)
        Ax=jax.jacfwd(lambda xx: slots(xx)[1])(x)
        Axx=jax.jacfwd(jax.jacfwd(lambda xx: slots(xx)[1]))(x)
        Gx=jax.grad(lambda xx: slots(xx)[0])(x)
        At=2*jnp.sqrt(G)*Ax
        Att=4*G*Axx+2*Gx*Ax
        return G,A,At,Att

    # GL panels in u, with geometric resolution of the bolt layer.
    edges=np.unique(np.concatenate([[0.0],np.geomspace(1e-10,1e-3,48),
                                    np.geomspace(1e-3,5e-2,40),
                                    np.linspace(5e-2,1.0,args.panels+1)]))
    qg,wg=np.polynomial.legendre.leggauss(args.order)
    uq=np.concatenate([(lo+hi)/2+(hi-lo)/2*qg for lo,hi in zip(edges[:-1],edges[1:])])
    wu=np.concatenate([(hi-lo)/2*wg for lo,hi in zip(edges[:-1],edges[1:])])
    ell=np.log(X/x0); xs=x0*np.exp(ell*uq); wx=wu*ell*xs
    G,A,At,Att=[np.asarray(t) for t in jax.vmap(jet)(jnp.asarray(xs))]
    af,ag,ah=A.T; Wvol=af*ag*ah; dtdx=1/(2*np.sqrt(G)); measure=Wvol*dtdx*wx
    y=At/A; yt=Att/A-y*y; S=y.sum(1)
    def Porb(ai,aj,ak): return 2*(ai**4-(aj**2-ak**2)**2)/(Wvol**2)
    P=np.stack([Porb(af,ag,ah),Porb(ag,ah,af),Porb(ah,af,ag)],1)
    R00=-(yt+y*y).sum(1); Rii=-yt-S[:,None]*y+P; scal=R00+Rii.sum(1)
    ric0sq=(R00-scal/4)**2+np.sum((Rii-scal[:,None]/4)**2,axis=1)

    gam=np.stack([(ag**2+ah**2-af**2)/(ag*ah),(ah**2+af**2-ag**2)/(ah*af),
                  (af**2+ag**2-ah**2)/(af*ag)],1)
    def gdot(ai,aj,ak,di,dj,dk):
        N=aj**2+ak**2-ai**2; M=aj*ak
        return (2*(aj*dj+ak*dk-ai*di)*M-N*(dj*ak+aj*dk))/M**2
    dfa,dga,dha=At.T
    gamt=np.stack([gdot(af,ag,ah,dfa,dga,dha),gdot(ag,ah,af,dga,dha,dfa),
                   gdot(ah,af,ag,dha,dfa,dga)],1)
    vv=At-gam; vvt=Att-gamt
    vj=np.roll(vv,-1,1); vk=np.roll(vv,-2,1); aj=np.roll(A,-1,1); ak=np.roll(A,-2,1)
    Rp=-vvt/(2*A)+(-vv-vj*vk/2)/(aj*ak)
    Wplus=Rp-scal[:,None]/12

    # Solve Yamabe factor on a separate monotone finite-volume node grid; interpolate to GL nodes.
    un=np.unique(np.concatenate([np.geomspace(1e-12,1e-3,600),
                                 np.geomspace(1e-3,5e-2,600),np.linspace(5e-2,1.0,5000)]))
    xn=x0*np.exp(ell*un); zn=np.log(xn)
    Gn,An,Atn,Attn=[np.asarray(t) for t in jax.vmap(jet)(jnp.asarray(xn))]
    yn=Atn/An; ytn=Attn/An-yn*yn; Sn=yn.sum(1); Wn=np.prod(An,axis=1)
    afn,agn,ahn=An.T
    Pn=np.stack([2*(afn**4-(agn**2-ahn**2)**2)/Wn**2,
                 2*(agn**4-(ahn**2-afn**2)**2)/Wn**2,
                 2*(ahn**4-(afn**2-agn**2)**2)/Wn**2],1)
    scn=-(ytn+yn*yn).sum(1)+(-ytn-Sn[:,None]*yn+Pn).sum(1)
    # dmu/(8pi^2 dx)=W/(8 sqrt(G)); the constant 1/8 is immaterial
    # to the PDE, but the radial factor 1/sqrt(G) is essential.
    vn=Wn/(8*np.sqrt(Gn))
    wn,nit,wend,wmin,wmax=solve_yamabe(zn,xn,vn,Gn,scn+24,xmax=args.xmax)
    w=np.interp(uq,un,wn); uconf=1+w
    # First conformally solve at scalar -24, then scale by 6 to the scalar -4
    # normalization used in Theorem Y.  Endomorphism W scales by 1/(6u^2),
    # while dmu/(8pi^2) becomes 9*u^4*(W dt) in radial normalization.
    # Under the scale-6 change to scalar -4, the chiral Weyl endomorphism scales
    # by 1/(6u^2); CH is (-4,2,2) here and (-2/3,1/3,1/3) after scaling.
    eig_hat=Wplus/(6*uconf[:,None]**2)
    psi,dist2,xspec,split,mu=psi_from_eigs(eig_hat)
    mhat=9*measure*uconf**4

    def integ(f,m=measure): return float(np.sum(m*f))
    # Relative model terms: CH has W=(-4,2,2) at Ric=-6 and
    # W=(-2/3,1/3,1/3) after the scalar -4 scaling.
    Pnorm=integ(ric0sq/4)
    # Direct radial differences of the volume and Weyl terms subtract quantities
    # of order X^2 and are not reliable at the present floating precision.  The
    # stable relative values below come from --yamabe-ledger and Y0.
    Psi=integ(psi,mhat); Dist2=integ(dist2,mhat)
    saving=1-Pnorm
    leb_u=np.sqrt(6*np.sum(eig_hat*eig_hat,axis=1))-2
    leb_pen=(4/9)*integ(leb_u*leb_u,mhat)
    stable_ledger=None
    closed_replica=None
    if args.yamabe_ledger:
        led=json.loads(Path(args.yamabe_ledger).read_text())['rows'][-1]
        # Ledger quantities are in physical /(8pi^2) units at scalar -24.
        # Constant scaling to scalar -4 multiplies relative volume by 36.
        dV_stable=36*float(led['RV_hat'])
        conformal_defect=float(led['Q_square'])+float(led['Q_grad'])
        P_hat=float(led['P'])-conformal_defect
        saving_hat=1-P_hat
        DW_stable=dV_stable+saving_hat/4  # closed/Y0 local contribution in a replica
        stable_ledger={'DeltaV_hat':dV_stable,'P_hat':P_hat,'saving_hat':saving_hat,
                       'D_W_hat_identity_derived':DW_stable,'D_W_over_DeltaV':DW_stable/dV_stable,
                       'four_conformal_Weyl_deficit':4*(DW_stable-(2/3)*dV_stable),
                       'conformal_defect_P_minus_Phat':conformal_defect}
        closed_replica={'Y0_saving_4DW_minus_4DeltaV':4*DW_stable-4*dV_stable,
                        'TheoremY_rhs_4DeltaV_minus_2Psi':4*dV_stable-2*Psi,
                        'TheoremY_slack':4*dV_stable-2*Psi-saving_hat,
                        'LeBrun_rhs':4*dV_stable-leb_pen,
                        'LeBrun_slack':4*dV_stable-leb_pen-saving_hat,
                        'scope':'formal closed replication with sign-family fields and zero period term; isolated cell alone does not satisfy these closed inequalities'}
    # Cumulative radial location of signed and nonnegative channels.
    order=np.argsort(xs); xo=xs[order]
    def quantiles(dens, qs=(0.1,0.5,0.9)):
        dd=np.asarray(dens)[order]
        cs=np.cumsum(dd); total=cs[-1]
        if total<=0: return None
        return {str(q):float(xo[min(np.searchsorted(cs,q*total),len(xo)-1)]) for q in qs}
    # deviations from CH in hatted spectral variables.
    orbit_energy=mhat*dist2
    psi_energy=mhat*psi
    split_energy=mhat*(4*split*split)
    out={
      'status':'floating quadrature; not interval certified', 'record':args.record,
      'normalization':'energies divided by 8pi^2; original cell Ric_CH=-6; Theorem-Y hatted metric scaled to scalar=-4',
      'quadrature':{'panels':args.panels,'order':args.order,'nodes':len(xs)},
      'yamabe_solver':{'nodes':len(un),'iterations':nit,'w_end':wend,'w_min':wmin,'w_max':wmax,
                       'w_bolt':float(wn[0])},
      'integrals':{'P':Pnorm,'saving_1_minus_P':saving,'stable_ledger':stable_ledger,
                   'Psi':Psi,'dist2_to_K':Dist2,'Psi_over_dist2':Psi/Dist2,
                   'LeBrun_magnitude_penalty':leb_pen,'closed_replica_comparison':closed_replica,
                   'upper_pair_splitting_contribution_4sigma2':integ(4*split*split,mhat)},
      'pointwise':{'x_minus_mu_min_hat_minmax':[float(xspec.min()),float(xspec.max())],
                   'sigma_upper_pair_halfgap_minmax':[float(split.min()),float(split.max())],
                   'Psi_minmax':[float(psi.min()),float(psi.max())],
                   'dist2_minmax':[float(dist2.min()),float(dist2.max())],
                   'mu_hat_at_max_Psi':[float(v) for v in mu[np.argmax(psi)]],
                   'x_at_max_Psi':float(xs[np.argmax(psi)])},
      'radial_quantiles':{'Psi':quantiles(psi_energy),'orbit_dist2':quantiles(orbit_energy),
                          'upper_pair_split_term':quantiles(split_energy),
                          'Ricci_defect':quantiles(measure*ric0sq/4)},
      'record_values':{'P':rec.get('P'),'J':rec.get('J')}
    }
    Path(args.out).write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps(out,indent=1))

if __name__=='__main__': main()
