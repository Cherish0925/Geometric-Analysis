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

# Scientific verification memo

## Summary

- Items 1, 3, and 6 have the correct coefficients and signs under the stated normalization of \(\mathbb H^2\).
- Item 2 has the correct inequality. Equality means \(\operatorname{rank}dU\le 1\), including the zero map.
- The conformal-gauge identification in item 4 is correct, but the stated center average is not: Step 82 subtracts the **tangential orbit-area derivative**, not the radial mean curvature. In general,
  \[
  \langle e(0,\cdot)\rangle_\mu
  =12+\left\langle |(\log\rho)_s|^2\right\rangle_\mu\ge 12.
  \]
- Consequently item 5 remains valid and actually strengthens to
  \[
  \sup_{\mathrm{exit}}e\ge
  12+\left\langle |(\log\rho)_s|^2\right\rangle_\mu\ge12.
  \]
- The forced identity is exact, but it does not by itself yield a pointwise estimate from a bound on \(F\), since \(\operatorname{div}_\sigma V\) contains \(DF\).

---

## 1. Drift Bochner formula

Let \(e_i\) be an orthonormal base frame, write
\[
U_i=dU(e_i),\qquad A_{ij}=\langle U_i,U_j\rangle_{\mathbb H^2}.
\]
For
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle,\qquad
\tau_\sigma=\tau+dU(\nabla\sigma),
\]
the standard Bochner identity becomes
\[
\begin{aligned}
\frac12Le
={}&|DdU|^2
+\sum_i\langle U_i,D_{e_i}\tau_\sigma\rangle\\
&+(\operatorname{Ric}_B-\operatorname{Hess}\sigma)_{ij}A_{ij}
-\sum_{i,j}
 \left\langle
 R^{\mathbb H^2}(U_i,U_j)U_j,U_i
 \right\rangle .
\end{aligned}
\tag{1}
\]
The drift tensor is \(\operatorname{Ric}_B-\operatorname{Hess}\sigma\), not the plus-sign version. Indeed,
\[
\sum_i\langle U_i,D_{e_i}\tau_\sigma\rangle
=
\sum_i\langle U_i,D_{e_i}\tau\rangle
+\frac12\langle\nabla\sigma,\nabla e\rangle
+(\operatorname{Hess}\sigma):A.
\]

The horizontal Einstein reduction is consistent with
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=-3\gamma_B+\frac12d\sigma\otimes d\sigma+\frac12U^*h_{\mathbb H^2}.
\tag{2}
\]
One way to see the coefficients is to write
\[
G^{-1}dG=d\sigma\,I+M^{-1}dM,\qquad
h_{\mathbb H^2}=\frac12\operatorname{tr}\bigl((M^{-1}dM)^2\bigr).
\]
The horizontal Ricci formula contains
\[
-\frac14\operatorname{tr}\bigl((G^{-1}dG)_i(G^{-1}dG)_j\bigr)
=-\frac12\sigma_i\sigma_j-\frac12A_{ij},
\]
which gives (2) after imposing \(\operatorname{Ric}_g=-3g\).

For sectional curvature \(-1\),
\[
-\sum_{i,j}
\left\langle R^{\mathbb H^2}(U_i,U_j)U_j,U_i\right\rangle
=2\det A.
\]
Also,
\[
\left(\frac12U^*h_{\mathbb H^2}\right):A
=\frac12\operatorname{tr}(A^2),
\]
and
\[
\left(\frac12d\sigma\otimes d\sigma\right):A
=\frac12|dU(\nabla\sigma)|^2.
\]
Thus, when \(\tau_\sigma=0\),
\[
\boxed{
\frac12Le
=
|DdU|^2+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)+2\det A-3e.
}
\tag{3}
\]

The cusp benchmark in `step84_corrected_drift_stress.json` independently fixes the drift sign:
\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r,
\]
gives, in an orthonormal frame,
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=\operatorname{diag}(-1,-3)
=-3I+\tfrac12d\sigma\otimes d\sigma.
\]

---

## 2. Algebraic estimate for \(Q\)

Define
\[
Q(A)=\frac12\operatorname{tr}(A^2)+2\det A.
\]
For a \(2\times2\) matrix,
\[
\operatorname{tr}(A^2)=(\operatorname{tr}A)^2-2\det A,
\]
so
\[
Q(A)=\frac12(\operatorname{tr}A)^2+\det A.
\]
Since \(A\) is a Gram matrix, \(A\ge0\), hence \(\det A\ge0\). Therefore
\[
\boxed{Q(A)\ge\frac12(\operatorname{tr}A)^2=\frac12e^2.}
\tag{4}
\]
Equality holds exactly when \(\det A=0\), equivalently
\[
\operatorname{rank}dU\le1.
\]
If \(dU\ne0\), this is rank one; the zero map is also an equality case.

---

## 3. Maximum principle on the reflected connector

From (3) and (4),
\[
\boxed{\frac12Le\ge\frac12e(e-6).}
\tag{5}
\]
At an interior maximum of \(e\),
\[
\nabla e=0,\qquad \Delta e\le0,
\]
so the drift term vanishes there and \(Le\le0\). Hence an interior maximum has \(e\le6\).

For a genuine smooth reflection across \(r=0\), doubling across that circle turns \(r=0\) into an interior circle of a smooth compact cylinder. The coefficients of \(L\) remain smooth and uniformly elliptic. Applying the maximum principle on the doubled cylinder gives
\[
\boxed{
\sup_{\Omega}e\le
\max\left\{6,\sup_{\{r=R\}}e\right\}.
}
\tag{6}
\]
Thus the reflected-domain argument is valid, provided “reflection” means a smooth isometric extension, as in the setup.

---

## 4. Center energy and the Step 82 variable mismatch

At \(r=0\), the orthonormal base normal and tangential vectors are
\[
n=e^{-\lambda}\partial_r,\qquad
t=e^{-\lambda}\partial_z=\partial_s.
\]
Therefore
\[
e=e^{-2\lambda}\bigl(|U_r|^2+|U_z|^2\bigr)
=|U_n|^2+|U_s|^2.
\]
Reflection gives \(U_r=0\), hence
\[
\boxed{e(0,z)=|U_s(0,z)|^2.}
\tag{7}
\]

The subsequent center equality in the question confuses two different quantities. Introduce
\[
\eta=(\log\rho)_s,
\]
which is tangential to the center slice. Step 82 uses
\[
K=\left\langle |U_s|^2-\eta^2\right\rangle_\mu,
\]
not the radial mean curvature \(H_{\mathrm{rad}}=u+v\). Reflection gives
\[
H_{\mathrm{rad}}(0,z)=0,
\]
but it does not imply \(\eta(0,z)=0\).

For
\[
q_0=ds^2+\rho M_{ab}\,d\xi^a d\xi^b,
\]
the intrinsic scalar curvature is
\[
R(q_0)
=-2\eta_s-\frac32\eta^2-\frac12|U_s|^2.
\tag{8}
\]
With \(d\mu=\rho\,ds\) and periodic \(s\),
\[
\int\rho\,\eta_s\,ds=-\int\rho\,\eta^2\,ds.
\]
Consequently,
\[
\langle R(q_0)\rangle_\mu
=-\frac12
\left\langle |U_s|^2-\eta^2\right\rangle_\mu.
\tag{9}
\]
A reflected hypersurface is totally geodesic. Since \(R(g)=-12\) and
\(\operatorname{Ric}(n,n)=-3\), the contracted Gauss equation gives
\[
R(q_0)=-6.
\]
Equations (8)–(9) therefore yield
\[
K(0)=12,
\]
but the full base energy satisfies
\[
\boxed{
\langle e(0,\cdot)\rangle_\mu
=
\langle|U_s|^2\rangle_\mu
=
12+\langle\eta^2\rangle_\mu
\ge12.
}
\tag{10}
\]
Equality with \(12\) requires \(\eta\equiv0\), meaning constant orbit area along the center circle. That condition does not follow from reflection alone.

---

## 5. Exit-energy obstruction

Let
\[
m_0=\langle e(0,\cdot)\rangle_\mu
=12+\langle\eta^2\rangle_\mu.
\]
Since normalized averaging uses a positive measure,
\[
m_0\le\sup_\Omega e.
\]
Combining this with (6),
\[
12+\langle\eta^2\rangle_\mu
\le
\max\left\{6,\sup_{\mathrm{exit}}e\right\}.
\]
The left side is at least \(12\), hence exceeds \(6\). Therefore
\[
\boxed{
\sup_{\mathrm{exit}}e
\ge
12+\langle\eta^2\rangle_\mu
\ge12.
}
\tag{11}
\]
Thus the proposed exit estimate is correct, despite the erroneous equality in the center calculation. The corrected center formula makes the result stronger.

---

## 6. Forced weighted-harmonic identity

Suppose
\[
\tau_\sigma(U)=F.
\]
Define the one-form
\[
V(X)=\langle dU(X),F\rangle.
\]
Using
\[
\operatorname{div}_\sigma V
=\operatorname{div}V+V(\nabla\sigma),
\]
one obtains
\[
\begin{aligned}
\operatorname{div}_\sigma V
&=\langle\tau(U),F\rangle
 +\langle dU,DF\rangle
 +\langle dU(\nabla\sigma),F\rangle\\
&=\langle\tau_\sigma(U),F\rangle+\langle dU,DF\rangle\\
&=|F|^2+\langle dU,D\tau_\sigma\rangle.
\end{aligned}
\]
Hence
\[
\boxed{
\langle dU,D\tau_\sigma\rangle
=\operatorname{div}_\sigma V-|F|^2.
}
\tag{12}
\]

If the base equation includes \(E_B\),
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=-3\gamma_B+\frac12d\sigma\otimes d\sigma
+\frac12U^*h_{\mathbb H^2}+E_B,
\]
then substitution into (1) gives
\[
\boxed{
\frac12Le
=
|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+Q(A)-3e
+\frac12|dU(\nabla\sigma)|^2
+E_B:A.
}
\tag{13}
\]
All coefficients and signs in this formula are correct.

Equation (13) alone does not reproduce the exact pointwise maximum argument from a bound on \(|F|\), because \(\operatorname{div}_\sigma V\) contains \(DF\). Weighted integration converts this divergence into cutoff and outer-edge pairings without differentiating \(F\), but a uniform \(L^\infty\) estimate would additionally require weighted Sobolev or Moser constants that remain controlled as the connector length and geometry vary.