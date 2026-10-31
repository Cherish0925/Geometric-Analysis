# Step 95: K_X charge-work identity, Bochner cancellation, and corrected free-T² scope

Session `S0910A03`, Agent2 / Execute.

> **CORRECTION.** An initial claim that the OT ceiling B(δ) applies unchanged to
> charged connectors is **withdrawn**. TTCS verification identified the exact
> cancellation Qe + ⟨dU, D(-Q∇β)⟩ = 3Q⟨dσ, d(β∘U)⟩, which removes the
> favorable +Qe from the Bochner reaction. The OT resolvent ceiling requires
> |τ_σ| ≤ 2δ; with twist, |τ_σ| ≤ Q + Cδ, so the ceiling is Q-dependent.
> The separator floor ≥ 12-8δ+2Q_C is confirmed valid.

## 1. K_X charge-work quadratic form

For A = e^{-3σ}M^{-1} and Q = ½q^TAq, the charge one-form is m_q = q^TAdq.
For any smooth vector field X with q = 0 on the boundary:
\[
\boxed{\int m_q(X)\,d\mu_\sigma = -\frac12\int q^T K_X q\,d\mu_\sigma,}
\tag{1.1}
\]
where
\[
K_X = X(A) + (\operatorname{div}_\sigma X)\,A
= (\operatorname{div}X - 2X(\sigma))A - e^{-3\sigma}M^{-1}X(M)M^{-1}.
\tag{1.2}
\]

**Verification.** Both the IBP identity and the decomposition have zero symbolic
residual: `workspace/scripts/step95_KX_charge_quadratic.py` and
`workspace/data/step95_KX_charge_quadratic.json`.

In the diagonal one-charge case with X = f(r)∂_r:
\[
q^TK_Xq = 2Q\cdot[f'-(2\sigma'+\alpha')f].
\tag{1.3}
\]

## 2. K_X with X = ∇σ: sign structure

For X = ∇σ, the scalar coefficient is
\[
k = L\sigma - 3|\nabla\sigma|^2 - \langle\nabla\alpha,\nabla\sigma\rangle
= 6+Q+T - 3|\nabla\sigma|^2 - \langle\nabla\alpha,\nabla\sigma\rangle.
\tag{2.1}
\]

At the center (|∇σ| ≈ 0): k ≈ 6+Q > 0.
On the cusp (|∇σ| ≈ 2): k ≈ 6-12 = -6 < 0.

Combined with the horizontal Bianchi pairing:
\[
-\frac12\int q^TK_{\nabla\sigma}q\,d\mu_\sigma
= \int[2H:\operatorname{Hess}\sigma - \operatorname{tr}H\cdot L\sigma
+ T\Delta\sigma - Z\cdot dU(\nabla\sigma)]\,d\mu_\sigma.
\tag{2.2}
\]

For small δ, the RHS is O(δ · geometry). The LHS has center and cusp
contributions with opposite signs. This structural split constrains the
charge distribution but does not by itself force Q → 0.

## 3. Area-charge coupling

Multiplying Lσ = 6+Q by Q and integrating by parts:
\[
-\int\langle\nabla Q,\nabla\sigma\rangle\,d\mu_\sigma = \int Q(6+Q)\,d\mu_\sigma.
\tag{3.1}
\]
For constant q: ∇Q = Q(-3∇σ-∇α), giving:
\[
\int Q(3|\nabla\sigma|^2+\langle\nabla\alpha,\nabla\sigma\rangle)\,d\mu_\sigma
= \int Q(6+Q)\,d\mu_\sigma.
\tag{3.2}
\]
This is exactly the K_X identity for X = ∇σ in the exact case, confirming
self-consistency. Combined with Lα = Q tested against Q:
\[
\int Q(3\langle\nabla\alpha,\nabla\sigma\rangle + e)\,d\mu_\sigma
= \int Q^2\,d\mu_\sigma,
\tag{3.3}
\]
which constrains the Q-weighted orbit-shape correlation.

## 4. Critical Bochner cancellation (TTCS-verified)

The drift curvature contributes +Qe to the Bochner. But the twist tension
is τ_σ(U) = -Q∇β + Z, and its covariant derivative gives:
\[
\langle dU, D(-Q\nabla\beta)\rangle = -Qe + 3Q\langle d\sigma, d(\beta\circ U)\rangle.
\tag{4.1}
\]
The +Qe from the drift curvature and -Qe from the tension derivative
**exactly cancel**. The net twist contribution to the Bochner is:
\[
\boxed{+Qe + \langle dU, D(-Q\nabla\beta)\rangle
= 3Q\langle d\sigma, d(\beta\circ U)\rangle,}
\tag{4.2}
\]
which has **no fixed sign**.

By Cauchy-Schwarz: |d(β∘U)| ≤ √e (since |∇β|=1), so:
\[
|3Q\langle d\sigma,d(\beta\circ U)\rangle| \le 3Q|\nabla\sigma|\sqrt{e}.
\tag{4.3}
\]
On a cusp it is small when Q→0. At a general minimal invariant separator, however, |∇σ| need not vanish: minimality cancels the normal area derivative against the base-curve curvature. Thus separator vanishing holds only for special seeds such as the Step 94 charged Koiso data. In the intervening geometry the term depends on the full area-orbit-charge correlation.

**Consequence.** The OT resolvent ceiling B(δ) cannot be applied to charged
connectors by simply dropping +Qe. The tension estimates become
|τ_σ| ≤ Q + Cδ and |V| ≤ (Q+Cδ)√e, both Q-dependent. The resolvent ceiling
grows with Q, as already computed in Step 89 for constant Q.

## 5. What IS established

1. **K_X identity** (1.1): algebraically verified, connects charge to
   horizontal defect via a matrix quadratic form.

2. **Separator floor with twist** (confirmed by TTCS):
   \[
   \langle e_s\rangle_\Sigma \ge 12 - 8\delta + 2\langle|II|^2\rangle
   \ge 12 - 8\delta.
   \]
   Twist raises the floor (from |II|² ≥ 0 including Q).

3. **CD(-(3+δ), 4) still holds** with twist: Ric_f^4 ≥ -(3+δ)γ_B because
   Q ≥ 0 improves the curvature lower bound. Heat kernel and Fisher
   information bounds are unchanged.

4. **The OT obstruction (δ < 0.246) holds for Q = 0** (Steps 85-88).

5. **The Q-dependent ceiling** from Step 89 constant-Q analysis gives a
   weaker obstruction that degrades as Q increases. The threshold drops
   from δ* ≈ 0.246 at Q=0 to δ* ≈ 0 at Q ≈ 0.9.

6. **Exact Bochner net twist contribution** = 3Q⟨dσ, d(β∘U)⟩ (no fixed sign).

## 5a. Step 96 correction to route interpretation

The observation that the twist term vanishes on the exact Step 94 seed and on a redshifted cusp does **not** localize it to a uniformly bounded transition. The area equation is elliptic and supplies no transition-diameter bound; an exterior resolvent also retains uncontrolled entrance data. The radial curved-base BVP proposed from this note is excluded by the flat-slice theorem because all `r`-level `T^3` coefficients remain spatially constant. Step 96 instead evolves the genuinely `s`-dependent charged center locally and formulates the full shared-parameter two-end matching operator; see `workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md`.

## 6. What remains open

The decisive free-T² question is:

**Can Q_+ = sup_B Q be bounded by a function of δ alone on the complete
two-ended connector, so that the Q-dependent ceiling remains below the
separator floor?**

From Step 89: if Q_+ ≤ Q*(δ) where Q*(δ) is the constant-Q threshold,
the obstruction still holds. But:

- The charged Koiso germ (Step 92/94) shows Q can be order 1 locally.
- The redshift taper (Step 94) shows area + Maxwell cannot bound Q_+.
- The backward Maxwell transport (Step 93) shows Q_+ can grow with
  connector length.
- The K_X identity constrains Q through the horizontal pairing but does
  not give a uniform bound without controlling the adjoint field geometry.
- The net Bochner cancellation (4.2) means there is no free +Qe
  surplus to absorb Q-dependent tension costs.

The most promising routes for a Q_+ bound are:
(a) The coupled orbit-area system including (4.2) and the Bochner—not
    just the resolvent with a constant mass.
(b) The K_X horizontal pairing with X chosen to exploit the full
    curvature structure.
(c) A direct weak/energy formulation for the charge that avoids
    differentiating E and uses both end conditions.

If Q_+ cannot be bounded, the construction side must show that a full
near-Einstein metric with Q > 0 can be assembled on a closed manifold
with no Einstein metric.

## Files

- `workspace/scripts/step95_KX_charge_quadratic.py` and
  `workspace/data/step95_KX_charge_quadratic.json`: K_X identity verification.
- `workspace/scripts/step95_charged_obstruction_theorem.py` and
  `workspace/data/step95_charged_obstruction_theorem.json`: **superseded**
  numerical comparison (the ceiling is wrong for Q > 0).
- `trace/ttcs/results/step95_ttcs01_verifier1_integration.md`: TTCS correction
  identifying the Bochner cancellation.
