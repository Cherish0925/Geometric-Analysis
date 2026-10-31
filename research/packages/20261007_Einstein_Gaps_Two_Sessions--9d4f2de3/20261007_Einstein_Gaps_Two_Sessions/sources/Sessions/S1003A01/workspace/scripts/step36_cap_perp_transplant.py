"""Step 36: transplant the certified perpendicular CH blow-up core into the exact Calabi cap.

This is a realizable finite-amplitude trial, not a response calculation.  The old cell is kept
unchanged up to the Euclidean chart radius ``a`` and is joined on ``a<|xi|<b`` to the exact
Calabi cap by a positive convex interpolation.  The whole transition is evaluated with the
coordinate Ricci tensor.  Compactly supported path, conformal, and horizontal/normal response
modes may be added on the transition.

Normalizations:
  * the stored perpendicular cell has Ric=-6 g and J6=integral |Ric+6g|^2;
  * after scaling by 6 use the CH exponential chart xi=r v, x=sinh^2(r/sqrt(6));
    its integrated defect equals J6;
  * the Calabi cap has Ric=-g and
      gC=u(dX^2+dY^2)+du^2/q+q(dPsi+(X dY-Y dX)/2)^2,
      u=cosh(sqrt(3/2)*sqrt(Z^2+W^2))^(2/3), q=(2/3)(u^2-u^{-1}).
    Thus Z,W are proper normal exponential coordinates.

The first pilot used scaled CH ball coordinates and algebraic cap normal coordinates,
which produced a large transition cost.  The current implementation changes the marking
on the overlap to exponential coordinates; the pilot remains a record of the old chart.

The cell closes smoothly at its O(-1) bolt, so the core is integrated in the old radial
coordinates.  Only the nonsingular overlap annulus is evaluated in Cartesian coordinates.
The output includes D, P, volume, scalar integral and scalar-square changes against the exact
cap ball.  The chiral quantities a=delta int|W+|^2 and b=delta int|W-|^2 are reconstructed from
the exact relative ledger; they are not an independent curvature check.

Examples:
  python step36_cap_perp_transplant.py RECORD --pairs 0.9:1.8,1.2:2.1 --nlog2 10 --out OUT
  python step36_cap_perp_transplant.py RECORD --pairs 1.2:2.1 --nlog2 11 --opt --out OUT
"""
import argparse
import json
import math
import sys
import time
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize
from scipy.stats import qmc

jax.config.update("jax_enable_x64", True)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "Sessions" / "S1003A02" / "workspace" / "scripts"))
from perp_dual_cost import DualCell, load_record, seed_vector  # noqa: E402
from o11_perp_cell import ANG, PI, metric_from, curvature_scalars  # noqa: E402

THRESHOLD = 0.995670030355131
SQ6 = math.sqrt(6.0)


def bergman(q):
    """CH metric with Ric=-6 in real ball coordinates q=(Re z1,Im z1,Re z2,Im z2)."""
    z = jnp.array([q[0] + 1j*q[1], q[2] + 1j*q[3]])
    r2 = jnp.real(jnp.vdot(z, z)); aa = 1.0/(1.0-r2); bb = aa*aa
    eye = jnp.eye(4)
    vv = jax.vmap(lambda e: jnp.array([e[0]+1j*e[1], e[2]+1j*e[3]]))(eye)
    hz = vv @ jnp.conj(vv).T
    vz = vv @ jnp.conj(z)
    return jnp.real(aa*hz + bb*jnp.outer(vz, jnp.conj(vz)))


def frames0(z):
    """Cell eigenframes: radial, perpendicular bolt, its mate, CH Hopf fibre."""
    z1, z2 = z[0], z[1]
    return [z,
            jnp.array([-jnp.conj(z2), jnp.conj(z1)]),
            jnp.array([-1j*jnp.conj(z2), 1j*jnp.conj(z1)]),
            1j*z]


def real2(z):
    return jnp.array([z[0].real, z[0].imag, z[1].real, z[1].imag])


def make_cell_metric(rec):
    deg = int(rec["deg"]); x0 = float(rec["x0"]); X = float(rec["X"])
    cell = DualCell(x0, X, deg, deg, 100)
    cell.aligned = False; cell.wpow = 2
    zz = jnp.asarray(np.asarray(seed_vector(cell, rec), float))
    prof = cell.prof_factory(zz)

    def metric_xi(xi):
        rr = jnp.linalg.norm(xi)
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        x = jnp.sinh(rr/SQ6)**2
        G, h = prof(x)
        # Pullback by the CH exponential chart at its center.  Radial distance is rr.
        lam = jnp.array([(x+x*x)/G, 6*h[0,0]/(rr*rr), 6*h[1,1]/(rr*rr), 6*h[2,2]/(rr*rr)])
        H = jnp.zeros((4,4))
        for k, v in enumerate(frames0(z)):
            vr = real2(v)/rr
            H = H + lam[k]*jnp.outer(vr, vr)
        return H
    return cell, zz, prof, metric_xi


def _safe_ratio(num, den, limit):
    """Smooth removable quotient; the branch is used only at/very near den=0."""
    return jnp.where(den > 1e-12, num/den, limit)


def cap_metric(xi):
    """Exact cap with Z,W the proper normal exponential chart, symmetric gauge.

    du/dn=sqrt(q), hence u(n)=cosh(sqrt(3/2)*n)^(2/3).  No truncation is used.
    Annulus nodes avoid the coordinate axis; its smooth analytic extension is used
    for construction and independent symbolic checks.
    """
    X, Y, Z, W = xi
    ss = Z*Z + W*W
    u = jnp.cosh(jnp.sqrt(1.5*ss))**(2.0/3.0)
    q = (2.0/3.0)*(u*u-1.0/u)
    # Expansions: q/ss=1+ss^2/10+O(ss^3), (1-q/ss)/ss=-ss/10+O(ss^2).
    ff = _safe_ratio(q,ss,1.0+ss*ss/10.0)
    cc = jnp.where(ss > 1e-12,(1.0-ff)/ss,-ss/10.0)
    vh = jnp.array([-0.5*Y, 0.5*X])
    vn = jnp.array([-W, Z])
    vr = jnp.array([Z, W])
    hh = u*jnp.eye(2) + q*jnp.outer(vh, vh)
    nn = ff*jnp.eye(2) + cc*jnp.outer(vr, vr)
    hn = ff*jnp.outer(vh, vn)
    g = jnp.zeros((4,4))
    g = g.at[:2,:2].set(hh)
    g = g.at[2:,2:].set(nn)
    g = g.at[:2,2:].set(hn)
    g = g.at[2:,:2].set(hn.T)
    return g


def smoother7(t):
    return t**4*(35.0-84.0*t+70.0*t*t-20.0*t**3)


def response_bump(t):
    return 256.0*t**4*(1.0-t)**4


def make_trial(cell_metric, outer_metric):
    S = jnp.diag(jnp.array([-1.0,-1.0,1.0,1.0]))
    def metric(xi, coeff, a, b):
        rr = jnp.linalg.norm(xi)
        t = (rr-a)/(b-a)
        ch = smoother7(t)
        fb = response_bump(t)
        gc = cell_metric(xi); gp = outer_metric(xi)
        base = (1.0-ch)*gc + ch*gp
        # Three smooth compactly supported tensors on the transition:
        # change interpolation path; conformal response; horizontal/normal trace-free response.
        m0 = fb*(gp-gc)
        m1 = fb*base
        m2 = 0.5*fb*(base@S + S@base)
        return base + coeff[0]*m0 + coeff[1]*m1 + coeff[2]*m2
    return metric


def ricci_of(metric):
    def Gamma(x, coeff, a, b):
        g = metric(x, coeff, a, b); gi = jnp.linalg.inv(g)
        dg = jax.jacfwd(metric, 0)(x, coeff, a, b)  # dg[i,j,k]=partial_k g_ij
        gl = 0.5*(jnp.einsum("jli->lij",dg)+jnp.einsum("ilj->lij",dg)-jnp.einsum("ijl->lij",dg))
        return jnp.einsum("kl,lij->kij",gi,gl)
    def Ric(x, coeff, a, b):
        G = Gamma(x,coeff,a,b)
        dG = jax.jacfwd(Gamma,0)(x,coeff,a,b)
        return (jnp.einsum("kijk->ij",dG)-jnp.einsum("kikj->ij",dG)
                +jnp.einsum("kkl,lij->ij",G,G)-jnp.einsum("kjl,lik->ij",G,G))
    return Ric


def point_fields(metric, Ric):
    def fields(x, coeff, a, b):
        g = metric(x,coeff,a,b); gi = jnp.linalg.inv(g); ric = Ric(x,coeff,a,b)
        scal = jnp.trace(gi@ric)
        r0 = ric-scal*g/4.0
        p = jnp.trace(gi@r0@gi@r0)
        ee = ric+g
        defect = jnp.trace(gi@ee@gi@ee)
        dv = jnp.sqrt(jnp.linalg.det(g))
        return jnp.array([defect*dv,p*dv,dv,scal*dv,scal*scal*dv,jnp.min(jnp.linalg.eigvalsh(g))])
    return fields


def qmc_annulus(a,b,nlog2,seed):
    U=qmc.Sobol(4,scramble=True,seed=seed).random_base2(nlog2)
    r=(a**4+(b**4-a**4)*U[:,0])**0.25
    alpha=2*np.pi*U[:,1]; beta=2*np.pi*U[:,2]; v=U[:,3]
    c=np.sqrt(1-v); s=np.sqrt(v)
    pts=np.stack([r*c*np.cos(alpha),r*c*np.sin(alpha),r*s*np.cos(beta),r*s*np.sin(beta)],axis=1)
    vol=0.5*np.pi**2*(b**4-a**4)
    return pts,vol


def core_integrals(cell, z, prof, a, nq=900):
    x0=cell.x0; xa=math.sinh(a/SQ6)**2
    if not (x0 < xa < cell.X):
        raise ValueError(f"core endpoint xa={xa} not in ({x0},{cell.X})")
    e,w=leggauss(nq); xs=0.5*(xa-x0)*e+0.5*(xa+x0); ww=0.5*(xa-x0)*w
    gm=metric_from(prof)
    def at(x):
        y=jnp.concatenate([jnp.array([x]),ANG])
        scal,r0,_,_=curvature_scalars(gm,y)
        G,h=prof(x); dv=PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
        return jnp.array([(r0+(scal+24.0)**2/4.0)*dv,r0*dv,dv,scal*dv,scal*scal*dv])
    vals=np.asarray(jax.jit(jax.vmap(at))(jnp.asarray(xs)))
    old=(ww[:,None]*vals).sum(0)
    # D and P are scale invariant; V, int s, int s^2 scale by 36,6,1.
    return np.array([old[0],old[1],36.0*old[2],6.0*old[3],old[4]]),xa


def cap_ball_volume(b):
    # sqrt(det gC)=u(n)*sqrt(q(u(n)))/n.  Integrate the normal radius first.
    from scipy.integrate import quad
    def integrand(n):
        u=math.cosh(math.sqrt(1.5)*n)**(2.0/3.0)
        q=(2.0/3.0)*(u*u-1.0/u)
        return 2*np.pi**2*(b*b-n*n)*u*math.sqrt(max(q,0.0))
    return quad(integrand,0,b,epsabs=1e-10,epsrel=1e-11)[0]


def integrate_batches(vfields,pts,coeff,a,b,batch=512):
    out=[]
    for i in range(0,len(pts),batch):
        out.append(np.asarray(vfields(jnp.asarray(pts[i:i+batch]),jnp.asarray(coeff),a,b)))
    return np.concatenate(out,axis=0)


def summarize(core,ann,vol_shell,b,coeff,a,xa,seed,n,reference_volume=None):
    aa=ann[:,:5].mean(0)*vol_shell
    trial=core+aa
    Vbg=cap_ball_volume(b) if reference_volume is None else reference_volume
    bg=np.array([0.0,0.0,Vbg,-4.0*Vbg,16.0*Vbg])
    diff=trial-bg
    Dn=trial[0]/(8*np.pi**2); Pn=trial[1]/(8*np.pi**2)
    dS2=diff[4]
    aval=(trial[1]-8*np.pi**2-dS2/12.0)/4.0
    bval=aval+12*np.pi**2
    return dict(a=a,b=b,xa=xa,coeff=[float(x) for x in coeff],seed=seed,n=n,
                D_over_8pi2=float(Dn),P_over_8pi2=float(Pn),margin_vs_certified=float(Dn-THRESHOLD),
                core_D_over_8pi2=float(core[0]/(8*np.pi**2)),annulus_D_over_8pi2=float(aa[0]/(8*np.pi**2)),
                volume=float(trial[2]),delta_volume=float(diff[2]),scalar_integral=float(trial[3]),
                delta_scalar_integral=float(diff[3]),scalar_square=float(trial[4]),delta_scalar_square=float(dS2),
                quarter_scalar_residual_square=float(trial[0]-trial[1]),
                ledger_a_over_8pi2=float(aval/(8*np.pi**2)),ledger_b_over_8pi2=float(bval/(8*np.pi**2)),
                ledger_b_minus_a_over_8pi2=float((bval-aval)/(8*np.pi**2)),
                min_metric_eigenvalue=float(ann[:,5].min()))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("record")
    ap.add_argument("--pairs",default="0.9:1.8,1.2:2.1,1.5:2.3")
    ap.add_argument("--nlog2",type=int,default=10); ap.add_argument("--seeds",default="0")
    ap.add_argument("--coeff",default="0,0,0"); ap.add_argument("--opt",action="store_true")
    ap.add_argument("--outer",choices=["cap","ch"],default="cap")
    ap.add_argument("--maxiter",type=int,default=20); ap.add_argument("--out")
    args=ap.parse_args(); rec=load_record(args.record)
    cell,z,prof,cell_metric=make_cell_metric(rec)
    if args.outer=="cap":
        outer_metric=cap_metric
    else:
        def outer_metric(xi):
            rr=jnp.linalg.norm(xi); x=jnp.sinh(rr/SQ6)**2
            zc=jnp.array([xi[0]+1j*xi[1],xi[2]+1j*xi[3]])
            lam=jnp.array([1.0,6*x/(rr*rr),6*x/(rr*rr),6*x*(1+x)/(rr*rr)])
            return sum((lam[k]*jnp.outer(real2(v)/rr,real2(v)/rr) for k,v in enumerate(frames0(zc))),jnp.zeros((4,4)))
    trial=make_trial(cell_metric,outer_metric)
    Ric=ricci_of(trial); fields=point_fields(trial,Ric)
    vfields=jax.jit(jax.vmap(fields,in_axes=(0,None,None,None)))
    pairs=[tuple(map(float,p.split(":"))) for p in args.pairs.split(",")]
    seeds=[int(s) for s in args.seeds.split(",")]
    cinit=np.array([float(s) for s in args.coeff.split(",")])
    records=[]; start=time.time()

    # Exact-cap curvature smoke test away from the divisor using the same generic Ricci code.
    captrial=lambda x,c,a,b: cap_metric(x)
    capRic=ricci_of(captrial)
    cappts=jnp.asarray([[.2,.1,.3,.4],[.7,-.2,.0,.5]])
    capres=[]
    for x in cappts:
        g=cap_metric(x); ri=capRic(x,jnp.zeros(3),1.0,2.0); capres.append(float(jnp.max(jnp.abs(ri+g))))

    for a,b in pairs:
        if not (cell.x0 < math.sinh(a/SQ6)**2 < cell.X and a<b<SQ6*math.asinh(math.sqrt(cell.X))):
            raise ValueError(f"bad pair {a,b}")
        core,xa=core_integrals(cell,z,prof,a)
        pts,vol=qmc_annulus(a,b,args.nlog2,seeds[0])
        # Compile and baseline.
        _=integrate_batches(vfields,pts[:min(8,len(pts))],cinit,a,b,batch=8)
        chosen=cinit.copy()
        opt_record=None
        if args.opt:
            # Fixed QMC nodes; bounded modes preserve positivity in the useful local range.
            def fg(cc):
                vals=integrate_batches(vfields,pts,cc,a,b)
                if not np.isfinite(vals).all() or vals[:,5].min()<=1e-6:
                    return 1e6, np.zeros(3)
                # Differentiate the QMC objective in one compiled pass.  This is slower than
                # the evaluation batches but keeps the response calculation exact.
                def obj(cj):
                    vv=jax.vmap(fields,in_axes=(0,None,None,None))(jnp.asarray(pts),cj,a,b)
                    return jnp.mean(vv[:,0])*vol/(8*np.pi**2)+core[0]/(8*np.pi**2)
                val,gr=jax.jit(jax.value_and_grad(obj))(jnp.asarray(cc))
                return float(val),np.asarray(gr,float)
            res=minimize(lambda cc:fg(cc)[0],chosen,jac=lambda cc:fg(cc)[1],method="L-BFGS-B",
                         bounds=[(-.7,.7),(-.3,.3),(-.3,.3)],options=dict(maxiter=args.maxiter,ftol=1e-11,gtol=2e-6,maxls=20))
            chosen=np.asarray(res.x,float)
            opt_record=dict(success=bool(res.success),message=str(res.message),nit=int(res.nit),
                            fun=float(res.fun),jac=[float(x) for x in res.jac])
        for seed in seeds:
            pseed,vseed=qmc_annulus(a,b,args.nlog2,seed)
            vals=integrate_batches(vfields,pseed,chosen,a,b)
            if args.outer=="cap":
                refvol=None
            else:
                # CH ball volume in Ric=-1 normalization: 36*pi^2 integral_0^X x dx,
                # X=sinh^2(b/sqrt(6)).
                xb=math.sinh(b/SQ6)**2
                refvol=18*np.pi**2*xb*xb
            rr=summarize(core,vals,vseed,b,chosen,a,xa,seed,len(pseed),refvol); rr["optimization"]=opt_record
            print(json.dumps(rr),flush=True); records.append(rr)
    out=dict(record=args.record,outer=args.outer,threshold=THRESHOLD,nlog2=args.nlog2,seeds=seeds,
             cap_einstein_max_residual=capres,records=records,seconds=time.time()-start,
             status="floating QMC construction experiment; topology and bolt are inherited from certified cell; ledger a,b derived, not independently integrated")
    text=json.dumps(out,indent=1)
    if args.out: Path(args.out).write_text(text+"\n")
    print(json.dumps({"saved":args.out,"seconds":out["seconds"],"cap_residual":capres}),flush=True)


if __name__=="__main__":
    main()
