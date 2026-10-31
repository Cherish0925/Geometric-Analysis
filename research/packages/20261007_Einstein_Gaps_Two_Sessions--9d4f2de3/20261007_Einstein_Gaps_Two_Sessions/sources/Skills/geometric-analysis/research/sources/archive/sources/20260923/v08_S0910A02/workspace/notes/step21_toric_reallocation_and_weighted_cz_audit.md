# Step 21: toric rod identity, alpha-family verdict, and weighted-CZ audit

Session S0910A02. Agent3/Actuator. Phase Execute.

## 0. Scope relative to Yau 26

The active target remains the full Yau-26 proposition for all dimensions and both
possible signs of the Ricci interval.  This note records two execution checks:

1. a cleanup of the four-dimensional positive toric `#_k(S^2 x S^2)`
   BUILD/BREAK line, using the exact rod identity emphasized in the strategist
   note; and
2. a cheap adversarial scaling audit of the A01/A03 negative-branch weighted
   smoothing route, testing whether the Step-11 opposite-warp/CZ spike immediately
   breaks the proposed weighted parabolic estimate.

Neither check proves or refutes Yau-26.  The goal of this step is to prevent two
specific forms of drift: over-investing in a small-m hexagon computation that
cannot see the large-`m` collapse regime, and assuming without test that the old
elliptic CZ counterexample also breaks the new weighted parabolic route.

## 1. Exact rod identity and volume bookkeeping

On a diagonal toric rod, let `Q` be the surviving fiber length along a collapsing
rod and let `K_edge` be the base Gaussian curvature restricted to the rod.  The
edge equation is

\[
  Q'' + (1-2K_{edge})Q = 0,
  \qquad Q(0)=Q(L)=0,
  \qquad Q'(0)=1,
  \qquad Q'(L)=-1 .
\]

Integrating gives

\[
  Q'(L)-Q'(0) + \int_0^L (1-2K_{edge})Q\,ds=0,
\]

hence

\[
  \int_0^L (1-2K_{edge})Q\,ds=2.
\]

Writing the rod flux as

\[
  \Phi_i=\int_{rod_i}Q_i\,ds,
\]

the identity becomes

\[
  \Phi_i=2+2\int_{rod_i}K_{edge}Q_i\,ds.
\]

With the normalization used throughout Steps 12--20,

\[
  \operatorname{Vol}_4 = 2\pi^2\sum_i\Phi_i.
\]

For constant edge curvature `K_edge=-A`, the exact profile is

\[
  Q(s)=\frac{\sin(\sqrt{1+2A}\,s)}{\sqrt{1+2A}},
  \qquad L=\frac{\pi}{\sqrt{1+2A}},
\]

so

\[
  \Phi_i=\frac{2}{1+2A}=\frac{2L_i^2}{\pi^2},
  \qquad
  \boxed{\operatorname{Vol}_4=4\sum_i L_i^2}.
\]

The script `workspace/scripts/step21_toric_rod_identity_alpha_audit.py` verifies
this against the three exact toric anchors:

| anchor | m | length L | identity volume | known volume | relative error |
|---|---:|---:|---:|---:|---:|
| `S^4` | 2 | `π√3` | `24π²` | `24π²` | `1.2e-16` |
| `CP^2` | 3 | `π√(3/2)` | `18π²` | `18π²` | `3.2e-16` |
| `S^2 x S^2` | 4 | `π` | `16π²` | `16π²` | `0` |

Data: `workspace/data/step21_toric_rod_identity_alpha_audit.json`.

## 2. Consequence for the previous modulus/perimeter route

Cauchy--Schwarz gives

\[
  \operatorname{Vol}_4=4\sum_iL_i^2
  \ge \frac{4}{m}\left(\sum_iL_i\right)^2 .
\]

Therefore any global input that only gives an `O(1)` lower bound on total
perimeter, total length, a comparable coarse scale, or a modulus tied only to
that scale can at best yield a `C/m` lower volume bound.  Such a lower bound is
not topology-uniform and cannot feed Proposition A's finite-cover amplifier: a
bound `v_0(\chi) -> 0` leaves the cover argument circular.

Thus Step 20's proposed modulus program is not by itself a route to the needed
`\chi`-uniform volume gap unless it proves something stronger, e.g. that at
least one rod length/flux stays bounded below independently of `m`, or that the
weighted quantity `\int(-K_edge)Q_i` is uniformly controlled in a way that forces
`\sum_i\Phi_i >= c_0`.

This is a route verdict, not a theorem that no toric volume gap exists.  The
unclosed possible BUILD obstruction is now concentrated in the full horizontal
and transition equations, not in the scalar rod-length/perimeter/modulus
bookkeeping already tested.

## 3. The alpha-family passes all scalar/local necessary tests currently on record

For `1 < alpha <= 2`, take

\[
  A_m=m^\alpha,
  \qquad L_m=\frac{\pi}{\sqrt{1+2m^\alpha}},
  \qquad \Phi_i=\frac{2}{1+2m^\alpha}.
\]

Then

\[
  \sum_i\Phi_i\sim m^{1-\alpha}\to0,
  \qquad
  \operatorname{Vol}_4=2\pi^2\sum_i\Phi_i\to0.
\]

For `1<alpha<2`, the total perimeter is

\[
  mL_m\sim \frac{\pi}{\sqrt2}m^{1-\alpha/2}\to\infty,
\]

while for `alpha=2` it tends to `π/√2`.  The signed Gauss--Bonnet curvature
burden of an `m`-gon with right angles is

\[
  \left|\int K_B\right|=\pi\left(\frac m2-2\right).
\]

If a constant `-A_m` boundary collar carries this curvature, its total area is
`~(πm/2)/A_m`, and the per-rod collar width is approximately

\[
  \frac{\pi/(2A_m)}{L_m}\sim \frac{1}{\sqrt{2A_m}},
  \qquad \frac{\text{width}}{L_m}\to\frac1\pi\approx0.318.
\]

The numerical audit records this stable width/length ratio: for example, at
`m=200`, `alpha=1.5`, `Vol_4≈1.396`, `perimeter≈8.353`, and
`width/L≈0.312`; at `alpha=1.9`, `Vol_4≈0.168`, `perimeter≈2.895`, and
`width/L≈0.312`.  Bishop's positive-Ricci volume upper bound is vastly satisfied.

Hence the alpha-family simultaneously satisfies the rod ODE, unit corner slopes,
finite/local corner compatibility from Step 19, signed Gauss--Bonnet scale,
Bishop upper-volume scale, and the scalar flux identity while collapsing volume.
All these are necessary conditions only, but together they show that no
`\chi`-uniform toric gap can be proved from the conditions currently exhausted.

## 4. Regular right-angled polygon mismatch: real but narrow

The one inexpensive geometric obstruction that remains visible at the scalar
level is the constant-curvature regular-polygon mismatch.  In a regular
right-angled `m`-gon of curvature `-A`, the side length is

\[
  s_{reg}(m,A)=\frac{2}{\sqrt A}\operatorname{arcosh}
   \left(\frac{\cos(\pi/m)}{\sin(\pi/4)}\right).
\]

For large `m`, this is

\[
  s_{reg}\sim \frac{1.762747\ldots}{\sqrt A},
\]

whereas the rod ODE asks for

\[
  L_{rod}\sim \frac{\pi}{\sqrt{2A}}=\frac{2.221441\ldots}{\sqrt A}.
\]

The asymptotic ratio is

\[
  L_{rod}/s_{reg}\to 1.2602155895\ldots .
\]

Solving `L_rod=s_reg` gives `A_match≈0.849` as `m -> ∞`; large `A` is impossible
in a globally regular *constant-curvature regular* polygon.  This is a genuine
check on a too-symmetric model, but it does not defeat the strip-like BREAK
geometry: there the large negative curvature is localized in collars of width
`~L/π`, while the interior is nearly flat and need not be a regular constant-
curvature polygon.  Therefore the mismatch is a useful diagnostic for numerical
setups (do not use regular constant-curvature polygons as the BREAK model), but
not a BUILD theorem.

## 5. Toric verdict and allocation

The toric work has reached a clean interim verdict:

* The previous Step-20 modulus/perimeter path does **not** supply the topology-
  uniform volume lower bound needed by Proposition A.
* The alpha-family shows that all scalar/global/local necessary conditions on
  record allow collapsing volume in the periodic-label toric family.
* A true BUILD result must now control the collar-to-interior transition through
  the full horizontal/traceless reduced equations, or through a stronger
  Q-weighted curvature/holonomy/Chern--Weil mechanism not yet formulated.
* A true BREAK result still requires an actual smooth global metric with
  `||Ric-g||_op -> 0`; the alpha-family is only a formal necessary-condition
  certificate.

This closes the *current toric proof route* as a candidate for quickly obtaining
Proposition A's `\chi`-uniform volume gap.  It does not close the mathematical
question of toric BUILD/BREAK, and it does not decide `P_4^+`, because Einstein
existence on `#_k(S^2 x S^2)` is still open.

Given this, further small-`m` hexagon numerics would be misleading: small `m` is
precisely where the system is forced toward O(1) flux, while the formal collapse
regime is asymptotic in `m`.  I did not run a hexagon solver.

## 6. Weighted CZ/heat audit for the negative-branch smoothing route

The strategist suggested using the Step-11 CZ spike to test A01/A03's weighted
regularity target.  The target estimate, schematically, is

\[
  |a\operatorname{Rm}|(x,t)\le C\beta/t,
  \qquad a=\chi^2,
\]

where `beta=A^2||Rm||_2` is the local critical Sobolev product.  I ran the cheap
scaling model

\[
  u_t=a_0\Delta u,
  \qquad u_0=B\exp(-|x|^2/(2\sigma^2))
\]

with constant diffusivity `a_0=chi_0^2`, both for full four-active-dimensional
spikes and for two-active-dimensional fiber-invariant CZ-type spikes.  For `k`
active Gaussian dimensions,

\[
  u(0,t)=B\left(\frac{\sigma^2}{\sigma^2+2a_0t}\right)^{k/2},
  \qquad
  ||u_0||_2=B\pi^{k/4}\sigma^{k/2}.
\]

The quantity testing the estimate is

\[
  R(t)=\frac{t a_0 u(0,t)}{||u_0||_2}.
\]

The audit found:

* for `k=4`, `sup_t R(t)=1/(8π)≈0.0397887`, independent of `sigma` and
  independent of `chi_0`;
* for `k=2`, `sup_t R(t)=O(sigma)`, so it tends to zero for a CZ-type spike
  localized in two variables and extended in the two fiber directions;
* by contrast, the elliptic initial ratio `a_0 B/||u_0||_2` can be arbitrarily
  large, which is exactly why Step 11 killed elliptic pointwise regularity.

Data: `workspace/data/step21_weighted_cz_heat_scaling_audit.json`, script:
`workspace/scripts/step21_weighted_cz_heat_scaling_audit.py`.

Interpretation: the old CZ spike does **not** immediately falsify the weighted
positive-time parabolic estimate.  The degeneracy weight `a` cancels the slow
diffusion scale in the constant-coefficient/Whitney model.  Therefore A01/A03's
zero-order weighted smoothing route remains plausible at the scaling level,
though not proved.  The remaining falsification target is the exact localized
weak recurrence/finite-neighbor estimate under the evolving normalized cutoff
flow, especially transition leakage and Hessian/cutoff terms after integration
by parts—not merely high pointwise curvature at the initial time.

I also reran peer verification scripts:

* `S0910A03/workspace/scripts/verify_step20_moser_recurrence_products.py`:
  confirms the `q -> 3q/2` exponent products converge and the endpoints give
  `gamma/t` for curvature and `delta(r^2/t)^(1/3)` for defect.
* `S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py`:
  confirms the exact weights in the `H_q` and `J_m` hierarchies.
* `S0910A01/workspace/scripts/step21_finite_exponent_smoothing.py`:
  confirms the finite-exponent route's arithmetic: 4D parabolic Sobolev gives
  spacetime `L^3`, `L^3` is supercritical over `n/2=2`, Whitney time scaling is
  independent of `chi_0`, and only fixed `q=2,3` critical absorption is needed
  before local boundedness.

These checks do not certify the PDE theorem, but they move A02's judgment from
"likely CZ-breakable" to "not broken by the obvious CZ scaling; the proof target
is now the rigorous localized weak moment inequality and finite-neighbor closure."

## 7. Next research direction

The most valuable next work is no longer toric small-`m` numerics.  It is an
independent critical audit of the negative-branch weighted smoothing theorem,
where A01/A03 now have the only route in the group that might close an entire
sign branch.  The sharp task is to derive or break the localized weak estimate
under the normalized cutoff flow

\[
  \partial_tg=-2\chi^2(\operatorname{Ric}+g),
\]

with finite-neighbor spatial cutoffs and evolving measure:

\[
\sup_{I'}H_{q,k'}+
\int_{I'}D_{q,k'}
\le Cq^\sigma 4^j(t^{-1}+r^{-2})M_q(Q_j),
\]

for the weighted moments

\[
 H_q=\int\eta^2a^{q-2}F^q,
 \qquad
 J_m=\int\eta^2a^{m-2}|E|^m.
\]

A good next step should not assume this inequality from Wang/Li; it should write
the local tensor energy with all cutoff, Hessian-`a`, evolving-measure,
normalization, and neighbor terms visible, then identify whether every term is
absorbed by the critical product and triangular defect structure.  A counterexample
would have to exploit one of those exact terms, since simple CZ pointwise spikes
are not enough.
