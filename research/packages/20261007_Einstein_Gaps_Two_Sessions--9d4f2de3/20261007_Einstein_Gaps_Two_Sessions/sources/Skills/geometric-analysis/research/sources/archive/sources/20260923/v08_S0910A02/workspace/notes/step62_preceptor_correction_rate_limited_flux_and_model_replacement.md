# Step 62: Preceptor correction of Step 61 and corrected rate-limited flux alternative

Session `S0910A02`. Agent4 / Preceptor. Phase Execute.

## 0. Review verdict

The Step-61 toric-cone calculations are useful as a curvature dictionary, but the **specific T²-invariant warped ansatz is not a valid near-pinched realizability model**. Two independent failures are decisive.

1. **The mode is not Ricci-neutral or Einstein-compatible.**  Step 61 computed, for
   \[
   g=dr_1^2+dr_2^2+r_1^2 e^{2\varepsilon A(r_1^2-r_2^2)}d\phi^2+r_2^2 e^{-2\varepsilon A(r_1^2-r_2^2)}d\psi^2,
   \]
   the linear Ricci tensor in an orthonormal frame:
   \[
   \operatorname{Ric}^{(1)}=
   \varepsilon A\begin{pmatrix}
   -4 & 2(r_1^2+r_2^2)/(r_1r_2)&0&0\\
   2(r_1^2+r_2^2)/(r_1r_2)&-4&0&0\\
   0&0&0&0\\
   0&0&0&0
   \end{pmatrix},
   \quad \operatorname{Scal}^{(1)}=-8\varepsilon A.
   \]
   At `r1=r2` this has base eigenvalues `0` and `-8 eps A`, not a scalar multiple of the metric.  Therefore the Step-61 choice `eps*A=Lambda/16`, made to force a zero eigenvalue of `W_pm+(Lambda/3)Id`, imports an order-`Lambda` Ricci defect.  It is Weyl reachability **outside** the pinching class, not reachability under `||Ric-Lambda g|| -> 0`.

2. **The mode violates toric-axis smoothness.**  Smoothness at the `phi`-axis requires
   \[
   v(0,r_2)=0
   \]
   so that the collapsing circle has the standard first derivative; smoothness at the `psi`-axis similarly requires `v(r1,0)=0`.  The unique T²-invariant degree-two harmonic is `r1^2-r2^2`; it restricts to `-r2^2` on one axis and `r1^2` on the other.  No nonzero degree-two T²-invariant harmonic satisfies both harmonicity and the two axis conditions.  Angular cutoffs would reintroduce large second angular derivatives into `Dv`.

3. **The Step-61 energy paragraph used inconsistent scaling.**  The statement `O(t^{-2}) << 8 pi^2 chi` is false.  In the corrected normal-coordinate drift picture, the reason Chern--Weil does not detect the drift is different: if `r=e^{-u}` and the outer matching fixes the perturbation to vanish at macroscopic scale, the accumulated Weyl variation obeys `|delta W| <= C delta u`; hence
   \[
   \int |\delta W|^2 r^3dr \lesssim \delta^2\int_0^{\infty}u^2e^{-4u}\,du=O(\delta^2)\to0.
   \]
   The drift is energy-invisible in the physical annulus because small radii have small four-volume, not because a bubble-frame `t^{-2}` quantity is small.

The reproducible audit is saved in

- `workspace/scripts/step62_step61_model_audit.py`
- `workspace/data/step62_step61_model_audit.json`

The Step-61 Weyl matrices remain a useful **dictionary** for that restricted ansatz, but they must not be used as a construction or obstruction proof.

## 1. The correct local replacement: Einstein-compatible two-jets

The failure of the toric ansatz is not a failure of the logarithmic drift mechanism.  The correct local object is the affine space of Einstein-compatible quadratic metric jets in normal coordinates.

Let `e` be the Euclidean metric at an orbifold point and let
\[
\mathcal E_\Lambda=
\{H_{ij}(x)\,dx^idx^j\text{ homogeneous quadratic}:\delta\operatorname{Ric}_e(H)=\Lambda e\}.
\]
Equivalently, using the normal-coordinate curvature expansion
\[
g_{ij}=\delta_{ij}-\frac13 R_{ikjl}x^kx^l+O(|x|^3),
\]
`mathcal E_Lambda` is the affine space of algebraic curvature tensors with `Ric=Lambda e`.  In dimension four the algebraic curvature space has dimension `20`, the Ricci map has rank `10`, and the Ricci-flat tangent kernel has dimension `10`, exactly the Weyl degrees of freedom
\[
\operatorname{Sym}^2_0(\Lambda^+)\oplus \operatorname{Sym}^2_0(\Lambda^-).
\]
The Step-62 audit verifies this rank count algebraically from a symmetric `6 x 6` curvature operator with the first Bianchi relation.

Thus a path
\[
s\mapsto H(s)\in\mathcal E_\Lambda
\]
can move the two Weyl blocks freely while preserving first-order Ricci and scalar curvature.  A logarithmic neck profile
\[
g=e+H(A(\log r))
\]
has the same mechanism as before: the Ricci defect from the static curvature part is exactly the Einstein one, while the additional defect comes from `A'` and `A''`, hence is `O(delta)` when `|A'|+|A''| <= C delta`, modulo the still-needed nonlinear and matching estimates.  Quadratic jets are smooth and, for an `A1` point, automatically invariant under the local `Z2={±1}` action.  This repairs both Step-61 failures at once: no toric-axis condition is present and the full ten-dimensional Weyl space is available.

This is still a **local jet mechanism**, not a closed near-pinched metric on a compact manifold.  It shows that there is no local algebraic, smoothness, or Weyl-reachability barrier for the exponential drift channel at an `A1` point.

## 2. Corrected rate-limited flux alternative

The noncollapsed positive bubble line should now be carried by a conditional flux alternative, not by the discarded toric model.

### 2.1 Flux hypothesis that still requires proof

Let `(M_i^4,g_i)` satisfy
\[
\|\operatorname{Ric}_{g_i}-\Lambda g_i\|_{op}\le \delta_i\to0,\quad \Lambda>0,
\]
with a noncollapsed Cheeger--Naber limit to an Einstein orbifold and an ADE bubble at `p` with scale `t_i -> 0`.  Fix an effective `Gamma`-invariant `l=2` ALE Jacobi/TT mode `o_k` and subtract the known ambient `H_2/H_4/...` tower in a compatible Bianchi/TT annular gauge.  The still-open analytic input is:

**H_flux.**  The normalized Wronskian coefficient `B_k(r)` satisfies, on the neck,
\[
|B_k(r_2)-B_k(r_1)|
\le C t_i\delta_i\log(r_2/r_1)+o(t_i),
\]
and the inner and outer normalizations identify the signal term with
\[
t_i\,\langle R_\pm(p)\zeta,\zeta_k\rangle,
\quad R_\pm=W_\pm+\frac\Lambda3 I.
\]

This is the tensor/gauge/tower-subtraction version of the scalar Wronskian calculation from Steps 59--60.  It is exactly the part that remains to be proved: one must choose gauges, remove ambient expansion terms that otherwise appear at signal order, control nonlinear/gauge errors, and identify the inner ALE flux.  The Step-11 Hessian spike warning remains relevant: a pointwise differentiated ODE for the metric is not justified by `C^0` Ricci pinching; the proof must be weak/flux-based.

### 2.2 The resulting alternative

Assuming `H_flux`, every effective obstruction component obeys
\[
|\langle R_\pm(p)\zeta,\zeta_k\rangle|
\le C\delta_i\log(1/t_i)+o(1).
\]
Consequently:

- If
  \[
  \delta_i\log(1/t_i)\to0,
  \]
  then the vector obstruction is forced:
  \[
  \Pi_\Gamma(R_\pm(p)\zeta)=0.
  \]
  In the `A1` case, where the invariant space is the full block, this is simply `R_pm(p) zeta=0`.

- If the limiting projected obstruction has norm at least `kappa>0`, then the neck must be exponentially long:
  \[
  \log(1/t_i)\ge \frac{kappa+o(1)}{C\delta_i},
  \qquad\text{equivalently}\qquad
  t_i\le \exp\!\left(-\frac{c\,kappa}{\delta_i}\right).
  \]

This is the honest theorem target:

> **Conditional rate-limited ADE flux alternative.**  Under noncollapsed four-dimensional positive pinching and the tensor flux hypothesis `H_flux`, an ADE bubble either satisfies the projected first Biquard--Ozuch obstruction equation, or its bubble scale is exponentially small relative to the Ricci pinching defect.  Under the additional rate `delta_i log(1/t_i)->0`, the first obstruction equation is necessary.

The alternative is sharp at the level of local `A1` two-jets: the full Weyl tangent space can be traversed with Ricci fixed to first order over a logarithmic length `~1/delta`.  Global capping, matching to an actual EH neck, and preservation of the closed topology are not yet constructed.

## 3. Invariance refinement by ADE type

At an orbifold point, all tensors on the cover are `Gamma`-invariant.  Therefore the effective Weyl block lies in
\[
\operatorname{Sym}^2_0(\mathbb R^3)^{\Gamma/\{\pm1\}}
\]
on the chiral block where `Gamma` acts nontrivially.  This is the Step-47 curvature-block invariant computation, and it bounds the possible drift paths.

Write `a=Lambda/3`.

| type/block | invariant Weyl form | degeneracy equation for `R=aI+W` |
|---|---|---|
| `A1` | arbitrary traceless symmetric `3 x 3` | `det(aI+W)=0` |
| cyclic `A_k`, most `k>=2` | `diag(-u/2,-u/2,u)` | `(a-u/2)^2(a+u)=0`, i.e. `u=2a` or `u=-a` |
| `A3` | `[[x,y,0],[y,z,0],[0,0,-x-z]]` | `(a-x-z)((a+x)(a+z)-y^2)=0` |
| `D4` | `diag(x,y,-x-y)` | `(a+x)(a+y)(a-x-y)=0` |
| higher `D_k` | same one-parameter axisymmetric form as most cyclic cases | `(a-u/2)^2(a+u)=0` |
| `E6,E7,E8` nontrivial block | `W=0` | `det(aI)=a^3>0`, so no positive-kernel degeneracy |

For `A1`, the local group imposes no restriction, and this is precisely why the product-quotient walls of Steps 55--57 have a large kernel.  For `A_k (k>=2)` and `D_k`, the drift question becomes a finite set of scalar reachability equations inside the invariant subspace.  For exceptional types on the nontrivial block, positive `Lambda` gives a scalar positive block and no first-obstruction kernel; under `H_flux` they are excluded at non-exponential scale.

Orientation conventions must be tracked.  In the usual complex Kleinian convention, the group acts trivially on the hyperkähler/Kähler chiral triple and nontrivially on the opposite block; some session notes swap `+/-`.  The invariant statement above is convention-free: apply it to the block on which the isotropy representation is nontrivial.

## 4. Product-quotient wall status after the correction

The positive and negative product-quotient walls use only `A1` points.  Since `Gamma/{±1}` is trivial for `A1`, the full Weyl block is invariant.  The previously computed curvature block on the bi-Kähler product quotient,
\[
R_+=R_-=\operatorname{diag}(\Lambda,0,0),
\]
has a genuine two-dimensional kernel in the actual orbifold curvature, not a flat-cone artifact.  Therefore the first vector obstruction can be killed by choosing `zeta` in that kernel.  The Step-61 `1:(-2):1` toric-mode mismatch with `2:(-1):(-1)` is irrelevant after the ansatz is discarded.

What remains unchanged is the smooth-category ceiling: the mixed rows are a hardness wall, not a counterexample.  The all-compatible and all-reversed endpoints are known Einstein via the smoothed double-cover/Aubin--Yau route and orientation reversal; mixed rows void the standard Kähler and ordinary numerical SW routes, but no smooth Einstein nonexistence theorem is known.

## 5. What is now established, and what is not

Established by Step 62:

- The Step-61 warped ansatz cannot be used for near-pinched Weyl drift because it has order-one Ricci defect at the claimed reachability value and violates toric-axis smoothness.
- The full normal-coordinate Einstein-compatible 2-jet space repairs those two local faults and gives full Weyl freedom at `A1` points.
- The correct noncollapsed positive statement is the conditional rate-limited flux alternative: obstruction or exponential scale, with `delta log(1/t)` as the sharp boundary.
- ADE invariance reduces non-`A1` drift to explicit finite equations, already tabulated in Step 47.

Not established:

- The tensor `H_flux` lemma with Bianchi/TT gauges, ambient tower subtraction, nonlinear error bounds, and inner/outer flux normalization.
- A global compact construction realizing the exponential drift through an EH/ADE neck.
- Any proof or disproof of Yau--26 in dimension four, either sign, or in higher dimensions.
- Any Lean formalization of the global geometric problem.

## 6. Consequence for route choice

The noncollapsed positive bubbling arc should be considered consolidated at a conditional theorem target and a local sharpness mechanism.  Continuing to patch the discarded toric ansatz is low value.  The next work should rebalance toward branches that can still decide the original proposition:

1. audit or independently reconstruct the peer `A01/A03` restricted negative Ishida--LeBrun/cutoff-flow chain, whose current claimed gap is the per-datum smooth existence and terminal-metric spectral contradiction;
2. attack positive collapse using the toric/ALG rod machinery with the **actual rod smoothness conditions** and the saturated energy budget, not the invalid cone-axis ansatz;
3. keep the `n>=5` branch open, where no verified closed no-Einstein reservoir is known.

The current note is not a final proof.  It prevents the noncollapsed line from hardening around a false model and gives the next agents a precise conditional statement to use or challenge.
