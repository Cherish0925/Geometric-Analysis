# Step 74: graph-center repair and positive-flux scale problem

Session: S0910A01. Agent1 / Orchestrator. Explore.

## 1. Why this step was needed

Step 73 ended with a route comparison that gave too much weight to one
finite-dimensional graph-center search and too much reach to the positive annular
flux program. The core target is still the full Yau--26 proposition. A restricted
negative construction is valuable only if it helps decide a normalized branch, and
a positive proof program must turn tight Ricci pinching into an Einstein metric,
not only into a local flux inequality.

The two corrections developed here are:

1. The reported zero-mean obstruction in the fixed ansatz
   `v=B sin(theta)` is not an obstruction to diagonal analytic Koiso center data
   on `T^3`. A Yamabe normalization gives such data directly.
2. The clean annular flux inequality has leading size `c/L`. If the relevant
   annulus length `L` tends to infinity, a nonzero flux coefficient is compatible
   with `delta -> 0`. The positive branch needs an additional scale relation,
   a fixed-rescaled-annulus extraction, or a different rigidity mechanism.

## 2. Direct construction of analytic diagonal Koiso center data on `T^3`

Let `f` be a nonconstant real analytic periodic function and define

\[
 h_0=d\theta^2+e^{2f(\theta)}dx^2+e^{-2f(\theta)}dy^2
\]

on a three-torus with arbitrary circle periods. In the coordinate frame
`(theta,x,y)`, the volume density is constant and the scalar curvature is

\[
 R(h_0)=-2(f')^2.
\]

Indeed, for a diagonal metric
`ds^2+e^{2b(s)}dx^2+e^{2c(s)}dy^2`,

\[
 R=-2(b''+c'')-2(b'^2+c'^2+b'c'),
\]

and `b=f`, `c=-f` gives the formula. Since `f` is nonconstant,
`\int R(h_0)<0`, hence the conformal Yamabe constant of `[h_0]` is negative.
The Yamabe theorem supplies a smooth positive minimizer. In dimension three,
for `h=psi^4 h_0`,

\[
 R(h)=\psi^{-5}\{-8\Delta_{h_0}\psi+R(h_0)\psi\}.
\]

Because `psi` is unique after fixing the negative scalar normalization, the
`T^2` translations preserve it. Thus `psi=psi(theta)` and, after scaling to
`R(h)=-6`, it solves the periodic analytic ODE

\[
 -8\psi''-2(f')^2\psi=-6\psi^5,\qquad \psi>0.
\]

Elliptic/ODE analytic regularity gives analytic `psi`. The metric

\[
 h=\psi^4 h_0
\]

is diagonal, analytic, `T^2`-invariant, and has scalar curvature `-6`. In
arclength `s` with `ds=psi^2 dtheta`, it becomes

\[
 h=ds^2+e^{2b(s)}dx^2+e^{2c(s)}dy^2,
 \quad b=2\log\psi+f,
 \quad c=2\log\psi-f,
\]

with periodic `b,c` and circle length `\int psi^2 dtheta`. The length need not
be `2pi`; it is still a smooth torus metric. Rescaling the coordinate period is
a harmless presentation choice.

For a four-dimensional Gaussian Einstein collar with `Ric=-3g`, a totally
geodesic center has `S(0)=0`. The constraints reduce to

\[
 R_h=-6,
 \qquad \operatorname{div}S-dH=0,
\]

which are satisfied. The tangential equation gives the first acceleration

\[
 S'(0)=\operatorname{Ric}_h^{\sharp}+3I.
\]

The trace is `R_h+9=3`, matching the normal equation. Thus the construction
supplies admissible analytic Koiso center data. It does not supply a global
half-core, decay to a cusp, or a compact graph-manifold metric with small
operator Ricci defect. Those are the next mathematical questions.

## 3. Numerical instance

For `f(theta)=sin(theta)` I solved the normalized Yamabe ODE with a periodic
boundary condition. The script is

`Sessions/S0910A01/workspace/scripts/step74_torus_yamabe_center.py`,

and the numerical record is

`Sessions/S0910A01/workspace/data/step74_torus_yamabe_center.json`.

The run found a positive periodic solution with

\[
0.6228147217\le \psi\le0.6583452279,
\]

and arclength circle period approximately

\[
\int_0^{2\pi}\psi^2d\theta=2.5788610778.
\]

The ODE residual using the equation right-hand side is algebraic self-consistency, not an independent numerical check; it is recorded as `1.1e-16` only to confirm that the solved ODE was inserted consistently. The independent FFT second-derivative check gives residual about `1.5e-5` and scalar curvature in arclength gauge between `-6.0001469` and `-5.9998782`. The Koiso acceleration eigenvalue ranges are recorded in the JSON; the maximum deviation of `S'(0)` from the isotropic value `I` is about `7.15`, so the center is genuinely anisotropic.

These numbers are not needed for existence, but they validate the formulas and
provide a concrete starting datum for a full graph-neck computation.

## 4. Graph route after the repair

The graph-manifold route is not blocked by the Step 73 `v=B sin(theta)` mean
failure. That failure only says that a particular first-order Riccati
parametrization did not produce a periodic diagonal fiber metric. The Yamabe
construction gives a much larger and natural space of periodic scalar `-6` fiber
metrics.

The remaining graph problem is therefore sharper:

- start from analytic diagonal `T^2`-invariant center data `h` with `R_h=-6` and
  `S=0`;
- solve or approximate the full gauge-fixed Einstein equations, not just the
  normal scalar equation or a spatial block;
- track `||Ric+3g||_{op,\infty}` together with
  `3+\int e^{2t}|S-I|^2dt=-\int e^{2t}E_{00}dt` when an outer cusp match is
  imposed;
- determine whether the actual evolution or elliptic problem enters a regime
  where fiber Ricci differences decay like `e^{-2t}`. The Step 73 fitted rate
  verifies a response law under a prescribed forcing rate; it does not prove
  that these center data generate that forcing rate.

A03's conformal-gauge anisotropy equation adds a serious further obstruction inside the `T^2`-invariant reflected half-core setting: if an exact outer cusp requires constant orbit anisotropy and the drift-Laplacian carries/amplifies nonconstant center anisotropy, the exact `T^2`-invariant graph-neck route may be blocked. The Yamabe construction therefore repairs the existence of admissible center data, but it does not defeat A03's boundary anisotropy obstruction. The next graph work must decide whether that obstruction is rigorous under the actual boundary conditions or whether non-reflected, non-`T^2`, or more global constructions evade it.

This route still addresses the negative branch in dimension four. Even a successful compact graph construction would not refute the original interval proposition unless the positive branch fails in the same dimension.

## 5. Positive annular flux: what it proves and what it lacks

A02's positive-branch allocation correctly identifies the clean annular flux
identity in the manuscript as an important reusable mechanism. The manuscript's
Proposition `FND:flux` says that on an annulus
`A={b<r<R}/Gamma`, `L=log(R/b)`, a nonzero quadratic TT model `K` yields

\[
\|D\operatorname{Ric}_e u\|_{op,\infty}
\ge { (d+2)I_K\over 2LJ_K}.
\]

The constant-scalar refinement gives the sharp leading constant `1/6` in the
spherical `A_1` model, and the manuscript records explicit models with

\[
 s_{\widehat g_a}=4,
 \qquad |\log a|\,\delta_+(\widehat g_a)\to {1\over6}.
\]

This is decisive information about scale: a nonzero flux coefficient produces
an inverse-logarithmic lower bound on that annulus, not a dimension-only lower
bound. If `L` grows like `|log a|`, then `delta -> 0` is compatible with the
nonzero coefficient. The inequality can force the coefficient to vanish only
when the surrounding compactness/bubbling argument supplies one of the following:

- an annulus with controlled `L` and all error terms small;
- an iterated fixed-rescaled-annulus extraction in which the defect contribution
  is `O(delta log R)` for fixed `R`, followed by `delta -> 0` and then `R ->
  infinity`;
- an independent relation such as `delta L -> 0` on the annuli carrying the
  obstruction;
- a global rigidity or existence theorem that bypasses the inverse-log loss.

The known first-obstruction-killed fillings are therefore not just examples to
ignore; they are stress tests for the positive flux program. If their best
possible behavior is `delta L -> 1/6`, the flux identity is sharp but does not
close `P_n^+`. If positive Ricci pinching plus compactness forces a better
relation on genuine countersequences than the constructed fillings have, that
would be a new proof mechanism.

## 6. Corrected topology reservoir for positive refutation

The statement that PSC-compatible no-Einstein manifolds are unknown is too
strong. For instance, `#_5 CP^2` has positive scalar/positive Ricci constructions
in the known connected-sum literature but violates Hitchin--Thorpe, so it cannot
carry an Einstein metric. It is, however, excluded from tight positive pinching
by the four-dimensional Chern--Weil ratio-3/Hitchin--Thorpe filter. The relevant
unknown reservoir is narrower: no currently inspected family combines known
Einstein nonexistence with the whole tight-positive-pinning compatibility class
(strict Hitchin--Thorpe in dimension four, finite fundamental group, `b_1=0`,
positive scalar, and whatever further curvature-energy constraints tight
pinching imposes). This supports continued exploration of a positive proof, but
it does not validate any particular flux architecture by itself.

## 7. A02 Step 74 and A03 Step 72 absorbed

A02's Step 74 strengthens the positive-route correction. The `ell`-mode classification confirms that `ell=2` is the unique unweighted log-critical mode for the Yau--26 maximum-norm Ricci hypothesis. For `ell>2`, the dual mass is power-scale, so the lower bound degenerates like `b^{ell-2}`. A02 also argues that higher Biquard--Ozuch obstructions are subcritical in operator norm once the first obstruction vanishes: a `k`-th obstruction contributes `O(t^{k-1})`, while the explicit log-annulus constructions have dominant defect `O(1/|log a|)`. Thus small `delta` cannot force the whole higher obstruction tower to vanish. This confirms that a positive proof cannot be a simple mode-by-mode flux tower.

A02's product extension is also important: if the four-dimensional positive orbifold-resolution question is resolved for the mixed rows, products with positively Einstein spheres carry the near-pinched input issue to dimensions `n>=6`; dimension `5` remains separate because `S^1` has zero Ricci. Thus the dimension-four positive branch is not a local side issue; it is a bottleneck for most higher dimensions.

A03's Step 72 argues that the `T^2`-invariant reflected graph-neck construction is blocked even after valid Yamabe center data are available: the anisotropy `d=b-c` obeys a drift-Laplacian, nonconstant center anisotropy is amplified toward the cusp, and a flat cusp requires constant orbit anisotropy. I have not independently rebuilt that full conformal-gauge proof in this step, but it changes the graph route's status from `center repaired, globally open` to `center repaired, T^2 reflected boundary matching probably blocked unless A03's boundary assumptions are evaded`.

## 8. Resulting route balance

The strongest next direction is not to abandon graph necks entirely or to accept the positive flux program as complete. The balanced allocation is:

1. Let A03 use the Yamabe-center construction as a corrected local datum, while treating their conformal-gauge anisotropy amplification as the main obstruction to the `T^2`-invariant reflected graph route.
2. Let A02 develop the mixed-row positive Einstein question, but with the now-correct premise that flux detects only the first log-critical obstruction; higher obstructions require tower rigidity or a global existence method, not small-`delta` necessity.
3. For A01, the highest-value next Explore/Execute interface is the mixed-row crux: read the explicit `(S^2 x S^2)/Z2` kernel data and Ozuch/Biquard obstruction formulas, then decide whether we can contribute a finite second-obstruction/tower-rigidity calculation, a global existence idea, or a critical review of the reduction.
4. Keep the restricted IL theorem as a mature negative-branch asset, but do not let it define the full Yau--26 route.

This step therefore changes the research posture: the graph negative branch is less blocked at the center but more constrained at the boundary; the positive branch is still the most scope-relevant path, but only through the four-dimensional mixed-row Einstein problem or a global proof mechanism, not through an unsupported all-mode flux necessity theorem.
