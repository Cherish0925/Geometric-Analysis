# TTCS Independent Branch Record

```json
{
  "step_id": 85,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/data/step85_bochner_comparison.json",
    "Sessions/S0910A03/workspace/data/step84_corrected_drift_stress.json"
  ]
}
```

## Task

Verify the following Bochner comparison theorem for the OT orbit-map energy density and its application to reflected Einstein connectors.

SETUP: Consider a 4D Einstein metric g with Ric = -3g having T² symmetry, in orthogonally transitive form g = e^{2λ}(dr² + dz²) + e^σ M_{ab}dξ^a dξ^b where M ∈ SL(2)/SO(2) ≅ H². The orbit map U: (B², γ_B) → (H², g_{H²}) satisfies the σ-weighted harmonic map equation div(e^σ M⁻¹dM) = 0, equivalently τ_σ(U) = 0 where L = Δ_{γ_B} + ⟨∇σ,∇·⟩ = ρ⁻¹div(ρ∇) with ρ = e^σ.

CLAIM 1 (Bochner formula): For e = |dU|²_{γ_B}, the exact σ-harmonic case gives
½Le = |DdU|² + ½|dU(∇σ)|² + Q(A) - 3e
where A is the Gram matrix A_{ij} = h(dU(e_i), dU(e_j)), and the Einstein base equation Ric_B - Hess σ = -3γ_B + ½dσ⊗dσ + ½U*h_{H²} + E_B has been used with E_B = 0.

CLAIM 2 (Q bound): Q(A) = ½tr(A²) + 2det(A) ≥ ½(tr A)² = ½e², with equality iff det A = 0 (rank-one dU).

CLAIM 3 (Maximum principle): ½Le ≥ ½e(e-6), so at any interior maximum Le ≤ 0 implies e ≤ 6. On a reflected connector [0,R]×S¹, reflection removes the center boundary, giving sup e ≤ max{6, sup_{exit} e}.

CLAIM 4 (Center identity): At a reflected center (r=0) with scalar curvature -6 on the T³ slice, U_r(0,z) = 0 by reflection, so e(0,z) = |U_s|²(0,z) where s is the physical z-arclength. The Step 82 identity K(0) = ⟨|U_s|² - H²⟩(0) = 12, with H(0) = 0, gives ⟨e(0,·)⟩_μ = 12.

CLAIM 5 (Contradiction): If sup_{exit} e < 12, then sup e < 12, but ⟨e(0,·)⟩_μ = 12 > sup e. This is impossible since ⟨e⟩ ≤ sup e for any positive measure. So every exact reflected OT Einstein connector must have sup_{exit} e ≥ 12.

CLAIM 6 (Forced case identity): For τ_σ = F ≠ 0, the identity ⟨dU, Dτ_σ⟩ = div_σ(V) - |τ_σ|² holds where V(·) = ⟨dU(·), τ_σ⟩. This converts the forced Bochner formula to ½Le = |DdU|² + div_σ(V) - |F|² + Q - 3e + nonneg + E_B·A.

Verify each claim independently. Check all coefficients, signs, the H² curvature term (K = -1), the drift curvature convention, the conformal gauge identification e(0,z) = |U_s|²(0,z), and whether the maximum principle applies to the operator L on a compact reflected domain. Identify any gap or coefficient error.

## Output

# Verification Memo: Bochner Comparison for the OT Orbit-Map Energy Density

## Overall assessment

The theorem is essentially correct. I re-derived the weighted Bochner formula, the algebraic Gram bound, the maximum-principle step, the center energy identity, and the forced-source identity independently, and every coefficient and sign in Statements 1–3, 5, 6 checks out. Statement 4 carries one genuine imprecision (an equality that should be an inequality, plus a symbol slip between two distinct quantities), but the imprecision runs in the favorable direction and does not disturb the conclusion. Below I give the reproduction of each step and flag the one place worth an independent nontrivial-orbit numerical check.

---

## Statement 1 (Bochner formula) — confirmed, all coefficients correct

Weighted (drift) Bochner for maps into a target of constant curvature $K$:
$$
\tfrac12 Le = |DdU|^2 + \langle(\mathrm{Ric}_B-\mathrm{Hess}\,\sigma)\,dU,dU\rangle \;-\;\sum_{i,j}\langle R^N(dU e_i,dU e_j)dU e_j,dU e_i\rangle .
$$
Two sign points I verified explicitly:

- **Drift curvature convention.** With $L=\rho^{-1}\mathrm{div}(\rho\nabla)=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle$, the Bakry–Émery tensor entering Bochner is $\mathrm{Ric}_B+\mathrm{Hess}(f)$ with $f=-\sigma$, i.e. $\mathrm{Ric}_B-\mathrm{Hess}\,\sigma$. This matches the convention recorded in `step84_corrected_drift_stress.json`. The earlier Step 83 sign (Ric+Hess) was indeed the wrong one; the correction is right.

- **Target term at $K=-1$.** $-\sum_{ij}\langle R^N\cdots\rangle=-K[(\mathrm{tr}A)^2-\mathrm{tr}A^2]=-K\cdot2\det A$. With $K=-1$ this is $+2\det A\ge0$, the favorable contribution characteristic of targets of curvature $\le0$.

Substituting the base equation $\mathrm{Ric}_B-\mathrm{Hess}\,\sigma=-3\gamma_B+\tfrac12 d\sigma\otimes d\sigma+\tfrac12U^*h+E_B$ (with $A_{ij}=(U^*h)_{ij}$) gives
$$
\langle(\cdots)dU,dU\rangle=-3e+\tfrac12|dU(\nabla\sigma)|^2+\tfrac12\mathrm{tr}A^2+E_B\!\cdot\!A .
$$
Adding $+2\det A$ from the target and setting $E_B=0$ reproduces exactly
$$
\tfrac12Le=|DdU|^2+\tfrac12|dU(\nabla\sigma)|^2+Q(A)-3e,\qquad Q(A)=\tfrac12\mathrm{tr}A^2+2\det A .
$$
Every term and coefficient agrees.

## Statement 2 (Q bound) — confirmed

For PSD $2\times2$ $A$ with eigenvalues $\ell_1,\ell_2\ge0$: $Q-\tfrac12(\mathrm{tr}A)^2=\ell_1\ell_2=\det A\ge0$, equality iff $dU$ has rank $\le1$. The companion upper end $Q\le\tfrac34e^2$ (equality at $\ell_1=\ell_2$) also holds, $\tfrac34e^2-Q=\tfrac14(\ell_1-\ell_2)^2$. Consistent with both JSON files.

## Statement 3 (maximum principle) — confirmed, standard regularity understood

Dropping the two nonnegative terms and using $Q\ge\tfrac12e^2$ gives $\tfrac12Le\ge\tfrac12e(e-6)$. At an interior maximum $\nabla e=0$, $\Delta e\le0$, and the drift term vanishes, so $Le\le0$, forcing $e(e-6)\le0$, hence $e\le6$. The reflection at $r=0$ extends $U$ evenly across $r=0$ (with $U_r(0)=0$), and $\sigma,\gamma_B$ are even, so $r=0$ becomes an interior point of the doubled cylinder and the only remaining edge is the exit face $r=R$. Therefore $\sup e\le\max\{6,\sup_{\text{exit}}e\}$. The even extension is smooth by elliptic regularity for the reflection-symmetric weighted-harmonic system; this is the standard hypothesis and should simply be stated as such. The argument does not need any zeroth-order sign on $L$; it is the pointwise interior-max argument for the semilinear inequality, which is valid.

## Statement 4 (center identity) — conclusion holds, but with a correction

**The independently verified core.** The scalar-minus-six center is not an added hypothesis: for an exact reflected core the fixed slice is totally geodesic ($S=0$), so Gauss gives
$$
R(q_0)=R(g)-2\mathrm{Ric}(n,n)+H^2-|S|^2=-12+6+0-0=-6
$$
pointwise. Good — this strengthens the setup.

**I re-derived the Step 82 §5 intrinsic identity from scratch** on a diagonal slice $q=dz^2+e^{2f_1}dx^2+e^{2f_2}dy^2$, $f_{1,2}=P\pm\alpha/2$, $P=\tfrac12\log\rho$:
$$
R(q)=-4P''-6P'^2-\tfrac12\alpha'^2=-2h_s-\tfrac32h^2-\tfrac12e,
$$
with $h=(\log\rho)_s=2P'$ and $e=\alpha_s^2=|U_s|^2_{\mathbb H^2}$. This confirms simultaneously (i) the $-\tfrac12e$ coefficient, and (ii) that the $\mathbb H^2$ normalization giving $e=\alpha_s^2$ is exactly the curvature $K=-1$ normalization used in the Bochner target term. The two computations use one mutually consistent $\mathbb H^2$ metric. This was the main thing that could have gone wrong, and it does not.

Integrating against $d\mu=\rho\,ds$ gives $\langle R(q_r)\rangle=-\tfrac12K$ with $K=\langle e-h^2\rangle$, hence at the center $K(0)=-2(-6)=12$.

**The correction.** $K$ is built from the tangential quantity $h=(\log\rho)_s$, **not** from the radial mean curvature $H=u+v$. The task's line "$K(0)=\langle|U_s|^2-H^2\rangle$, with $H(0)=0$" substitutes $H(0)=0$ into a slot that actually contains $h$. Reflection makes radial derivatives vanish ($u(0)=v(0)=0$, so $H(0)=0$), but it does **not** force the tangential $h(0,z)=\partial_s\log\rho$ to vanish. The correct relation is
$$
\langle e(0,\cdot)\rangle_\mu=K(0)+\langle h(0)^2\rangle_\mu=12+\langle h(0)^2\rangle_\mu\ \ge\ 12,
$$
with equality only when the orbit-area is constant along the center slice. So the JSON line "$\langle e(0,\cdot)\rangle_\mu=K(0)=12$" is the homogeneous-slice special case; in general the center average is strictly above 12. Since the argument only needs $\langle e(0)\rangle\ge12$, this correction makes the result more robust, not less. The conformal-gauge identification $e(0,z)=|U_s|^2(0,z)$ (radial part of $dU$ killed by reflection, $\hat z$ = physical arclength direction) is correct.

## Statement 5 (contradiction) — confirmed

$\langle e(0)\rangle_\mu\ge12$ gives $\sup e\ge12$. With $\sup e\le\max\{6,\sup_{\text{exit}}e\}$ and $12>6$, the maximum lives on the exit face, so $\sup_{\text{exit}}e\ge12$. Hence no exact reflected OT Einstein connector can reach the Step 73 expanding-tail face where $e_{\text{exit}}\to0$. This is strictly stronger than the Step 79 constant-exit exclusion ($e_{\text{exit}}=0$), and it supersedes the near-center jet analysis (Step 82 §7, $K''(0)\ge72$) for the exact case: the jet only showed initial worsening, whereas the Bochner comparison closes the exact case globally. The internal number-matching ($x'(0)=3-\tfrac12K(0)=-3$, $y'(0)=6$, threshold $6=2\cdot3$, center $12=2\cdot6$, all tracing to $\mathrm{Ric}=-3g$) is coherent.

## Statement 6 (forced identity) — confirmed, with the right open question identified

I verified $\langle dU,D\tau_\sigma\rangle=\mathrm{div}_\sigma V-|\tau_\sigma|^2$, $V(X)=\langle dU(X),\tau_\sigma\rangle$, from
$$
\mathrm{div}_\sigma V=\langle\tau(U)+dU(\nabla\sigma),\tau_\sigma\rangle+\langle dU,D\tau_\sigma\rangle=|\tau_\sigma|^2+\langle dU,D\tau_\sigma\rangle .
$$
So $\tfrac12Le=|DdU|^2+\mathrm{div}_\sigma V-|F|^2+Q-3e+\tfrac12|dU(\nabla\sigma)|^2+E_B\!\cdot\!A$ with $F=\tau_\sigma$, as stated. The observation is correct that pointwise closure does not go through — $\mathrm{div}_\sigma V$ carries $DF$, a derivative of the Ricci defect — while the integrated form trades $DF$ (via parts) for the favorable $-|F|^2$ plus a cutoff cross term. The decisive unresolved point is exactly the one the notes state: whether Moser iteration on the weighted 2D base yields an $L^\infty$ bound $e\le6+C\delta$ with $C$ independent of connector length $R$ and geometry. Neither the integrated inequality nor the threshold $\delta<3/(8+C)$ is established; the exact-case constant $C=0$ giving $\delta<3/4$ is only the formal endpoint. This is the correct live mathematical object.

---

## What remains to be checked independently

The one coefficient I could not close purely from the supplied material is the **$\tfrac12$ on $U^*h$** in the base equation $\mathrm{Ric}_B-\mathrm{Hess}\,\sigma=-3\gamma_B+\tfrac12d\sigma^2+\tfrac12U^*h+E_B$. The round-cusp benchmark has $U^*h=0$ and cannot test it. My independent scalar-curvature computation pins the $\mathbb H^2$ normalization ($e=\alpha_s^2$, $K=-1$) and the $-\tfrac12e$ intrinsic coefficient, and these are consistent with $\tfrac12U^*h$, but a direct nontrivial-orbit check (e.g. a slice with $\alpha_z\ne0$ or an off-diagonal $\beta\ne0$ profile) verifying the $\tfrac12$ against the full 4D $\mathrm{Ric}=-3g$ reduction would make the derivation of Statement 1 fully self-standing. If that coefficient were, say, $1$ instead of $\tfrac12$, the $Q\ge\tfrac12e^2$ bound and the threshold $6$ would move, so it is the single quantitative hinge deserving a standalone numerical confirmation.

Two smaller items to record in any write-up:

1. Statement 4 should read $\langle e(0,\cdot)\rangle_\mu\ge12$ (with the tangential $h$, not the radial $H$), not $=12$.
2. The smooth even-extension across $r=0$ relies on the standard reflection-regularity for the weighted-harmonic system; worth one sentence rather than silent use.

## Value

For the graph-manifold route on the $\mathrm{Ric}=-3g$ side, this gives a clean and complete exclusion of exact reflected OT Einstein connectors into the expanding tail — a sharper statement than both Step 79 and the Step 82 jet, obtained from a single subsolution inequality with matching center energy. The residual mathematics is precisely the forced/approximate version, where the integrated Bochner + geometry-independent Moser estimate is the fork that would decide whether the vanishing-defect connector can exist. As §9 of Step 82 notes, even a complete connector still leaves the positive normalized branch, the global attachment, and the all-$n$ quantifier untouched; the present result advances only the one geometric module it addresses.