"""Step 37: congruence transport of the full certified perpendicular cell into the Calabi cap.

Construction (Strategist proposal, Step 37).  Let g_* be the recovered perpendicular cell
(Ric=-6 record, scaled by 6 to Ric=-g), extended by exact CH, written in the CH exponential
chart xi in R^4 (same marking as step36).  Off the bolt, g_* and g_CH are simultaneously
diagonal in the Euclidean-orthonormal frames (radial, perpendicular, mate, Hopf), so

    L = (g_CH^{-1} g_*)^{1/2} = sum_k sqrt(lam_k/lamCH_k) v_k v_k^T

is explicit and Euclidean-symmetric.  With bar_g=(1-H)g_CH+H g_C, H=H((r-a)/(b-a)) the
C^3 smoother of step36, define

    G = L bar_g L          for r>=a,      G = g_*  for r<a.

Then G=g_* whenever the outer metric is CH (for every a,b), G is positive by congruence,
and G=g_C exactly for r>=R_cell=sqrt6*arsinh(sqrt X), where the cell is exactly CH.
The whole region a<r<R_cell is integrated by stratified scrambled-Sobol quadrature on
radial shells; the core r<a is integrated radially exactly (step36 core_integrals).

Output: per-shell D, P, volume, scalar moments; totals; CH control (outer=ch) which must
reproduce the radial integral of the certified cell.
"""
import argparse, json, math, sys, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
from scipy.stats import qmc

jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step36_cap_perp_transplant as s36  # noqa: E402
from perp_dual_cost import DualCell, load_record, seed_vector  # noqa: E402

SQ6 = math.sqrt(6.0)


def build(rec, outer, a, b, amp=1.0, taper=None):
    deg = int(rec["deg"]); x0 = float(rec["x0"]); X = float(rec["X"])
    cell = DualCell(x0, X, deg, deg, 100); cell.aligned = False; cell.wpow = 2
    zz = jnp.asarray(np.asarray(seed_vector(cell, rec), float)); prof = cell.prof_factory(zz)
    Rcell = SQ6*math.asinh(math.sqrt(X))

    def frames(xi, rr):
        z = jnp.array([xi[0]+1j*xi[1], xi[2]+1j*xi[3]])
        return [s36.real2(v)/rr for v in s36.frames0(z)]

    def Lmat(xi):
        rr = jnp.linalg.norm(xi)
        x = jnp.minimum(jnp.sinh(rr/SQ6)**2, X)
        G, h = prof(x)
        lam = jnp.array([(x+x*x)/G, h[0,0], h[1,1], h[2,2]])
        lch = jnp.array([1.0, x, x, x*(1+x)])
        rat = lam/lch
        # amp interpolates the transported deformation: amp=1 is the certified cell.
        if taper is None:
            am = amp
        else:
            tc, td = taper
            am = amp*(1.0 - s36.smoother7(jnp.clip((rr-tc)/(td-tc), 0.0, 1.0)))
        sq = jnp.exp(0.5*am*jnp.log(rat))
        V = frames(xi, rr)
        return sum((sq[k]*jnp.outer(V[k], V[k]) for k in range(4)), jnp.zeros((4,4)))

    def gch(xi):
        rr = jnp.linalg.norm(xi); x = jnp.sinh(rr/SQ6)**2
        lam = jnp.array([1.0, 6*x/(rr*rr), 6*x/(rr*rr), 6*x*(1+x)/(rr*rr)])
        V = frames(xi, rr)
        return sum((lam[k]*jnp.outer(V[k], V[k]) for k in range(4)), jnp.zeros((4,4)))

    gout = s36.cap_metric if outer == "cap" else gch

    def metric(xi, coeff, aa, bb):
        rr = jnp.linalg.norm(xi)
        t = jnp.clip((rr-aa)/(bb-aa), 0.0, 1.0)
        H = s36.smoother7(t)
        gbar = (1.0-H)*gch(xi) + H*gout(xi)
        L = Lmat(xi)
        return L@gbar@L
    return cell, zz, prof, metric, Rcell


def shells_qmc(r0, r1, nlog2, seed):
    pts, vol = s36.qmc_annulus(r0, r1, nlog2, seed)
    return pts, vol


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("record")
    ap.add_argument("--outer", choices=["cap", "ch"], default="cap")
    ap.add_argument("--a", type=float, default=0.5); ap.add_argument("--b", type=float, default=1.5)
    ap.add_argument("--amp", type=float, default=1.0)
    ap.add_argument("--edges", default="")
    ap.add_argument("--taper", default="", help="c:d, deformation amplitude tapered to 0 between radii c and d")
    ap.add_argument("--nshell", type=int, default=16)
    ap.add_argument("--nlog2", type=int, default=10); ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out")
    args = ap.parse_args(); rec = load_record(args.record)
    taper = tuple(map(float, args.taper.split(":"))) if args.taper else None
    cell, zz, prof, metric, Rcell = build(rec, args.outer, args.a, args.b, args.amp, taper)
    if taper is not None:
        Rcell = min(Rcell, taper[1])
    Ric = s36.ricci_of(metric); fields = s36.point_fields(metric, Ric)
    vf = jax.jit(jax.vmap(fields, in_axes=(0, None, None, None)))
    core, xa = s36.core_integrals(cell, zz, prof, args.a)
    if args.edges:
        edges = [float(e) for e in args.edges.split(",")]
    else:
        edges = list(np.linspace(args.a, Rcell, args.nshell+1))
    start = time.time(); shells = []; tot = np.zeros(5); minev = 1e9
    c0 = jnp.zeros(3)
    for r0, r1 in zip(edges[:-1], edges[1:]):
        pts, vol = shells_qmc(r0, r1, args.nlog2, args.seed)
        vals = s36.integrate_batches(vf, pts, c0, args.a, args.b)
        good = np.isfinite(vals).all(1)
        m = vals[good, :5].mean(0)*vol
        se = vals[good, 0].std()*vol/math.sqrt(good.sum())
        tot += m; minev = min(minev, float(vals[good, 5].min()))
        sh = dict(r0=r0, r1=r1, D_over_8pi2=float(m[0]/(8*np.pi**2)),
                  D_se_over_8pi2=float(se/(8*np.pi**2)), P_over_8pi2=float(m[1]/(8*np.pi**2)),
                  vol=float(m[2]), int_s=float(m[3]), int_s2=float(m[4]),
                  nbad=int((~good).sum()), min_eig=float(vals[good, 5].min()))
        shells.append(sh); print(json.dumps(sh), flush=True)
    trial = core + tot
    out = dict(record=args.record, outer=args.outer, a=args.a, b=args.b, amp=args.amp, taper=args.taper, Rcell=Rcell,
               core_D_over_8pi2=float(core[0]/(8*np.pi**2)),
               shell_D_over_8pi2=float(tot[0]/(8*np.pi**2)),
               D_over_8pi2=float(trial[0]/(8*np.pi**2)), P_over_8pi2=float(trial[1]/(8*np.pi**2)),
               volume=float(trial[2]), int_s=float(trial[3]), int_s2=float(trial[4]),
               min_eig=minev, shells=shells, nlog2=args.nlog2, seed=args.seed,
               seconds=time.time()-start,
               status="floating stratified QMC; G=L bar_g L congruence transport of full certified cell")
    txt = json.dumps(out, indent=1)
    if args.out: Path(args.out).write_text(txt+"\n")
    print(json.dumps({k: out[k] for k in ["outer", "a", "b", "amp", "core_D_over_8pi2", "shell_D_over_8pi2", "D_over_8pi2", "P_over_8pi2", "seconds"]}))


if __name__ == "__main__":
    main()
