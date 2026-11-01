# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step57_kernel_burns_coefficient_general_background.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md"
  ]
}
```

## Task

Verify the formal Theorem 57.Φ and the Step-58 cross-checks. The claim is:

(a) For a Burns insertion on a 4-manifold at a point p with zeta an eigenvector of R⁺ = W⁺ + s/12 having eigenvalue μ₁ (other: μ₂, μ₃), the ε²log(1/ε) coefficient in P(g̃)/(8π²) is Φ = -μ₁(μ₁-μ₂-μ₃)/2 - (μ₂-μ₃)²/2. In the kernel μ₁=0: Φ = -(μ₂-μ₃)²/2 ≤ 0.

(b) Φ depends only on s and W⁺(p), not on W⁻, Ric°, ∇Rm, or ∇²Rm. The proof of W⁻/Ric° independence is: P(g̃) - P(g) - 8π² = Δ(4∫|W⁺|² + ∫s²/12) by Chern-Weil; if W⁺=0,s=0 at p the right side is ≥ 0, so W⁻/Ric° coefficients are nonneg, and D=4 attains 0. Check this argument.

(c) Lemma 57.1: ∇²Rm drops out because the Burns family δ+εA is P-critical for all ε, so the C-linear coefficient is a divergence of a degree -3 field on S³, with zero integrated coefficient. ∇Rm drops out by parity under U(1)_ζ.

(d) Product-background test: Σ₁(K₁)×Σ₂(K₂) has R⁺=diag(s/4,0,0), s=2(K₁+K₂). Both par (μ₁=s/4) and perp (μ₁=0) layouts should give Φ = -s²/32. The computation uses conformal coordinates (nonzero quartic C). Does the corrector convergence rate depend on the gauge of the background jet?

(e) The strategist question: do degree-0 correctors exhaust the contributions to the log coefficient? That is, correctors of higher homogeneity feed other powers of r, not the ε²log corner.

(f) Consequence: every compact KE surface has R⁺=diag(s/4,0,0). The kernel circle ζ⊥ω gives Φ=-s²/32<0 at every point. Does this give p_*(X#kCP̄²) < 8π²k for ALL minimal general-type X? Scope: formal (needs the rigorous remainder).

(g) Minimizer rigidity: R⁺≤0, and μ_max(R⁺)=0 ⟹ μ₂=μ₃. Combined with |W⁺|²≤s²/24 on R⁺≤0, does this strengthen to |W⁺|²<s²/24 strictly?

(h) The unification reading: R⁺<0 (interior of the cone) is decided at first order (positive cost -εμ₁>0); the boundary at second order (Φ≤0). Real-hyperbolic = Theorem H regime (cost, bubbling allowed); KE = saving regime (bubbling excluded at minimizers). Is this consistent and complete?

## Output

# Scientific verification memo: Theorem 57.Φ and Step 58

The reported formula is algebraically consistent, and the product tests agree with its normalization. Two distinctions are essential:

- **\(\Phi\) is the optimized spherical coefficient; the coefficient multiplying \(\varepsilon^2\log(1/\varepsilon)\) in \(P/(8\pi^2)\) is \(\Phi/2\).**
- The formula concerns a specified Burns-tail construction, minimized over its degree-zero corrector. It is not the coefficient of every metric construction having a Burns core.

The supplied excerpts contain numerical summaries, but not the script bodies or JSON arrays. Thus the numerical assessment below verifies the recorded values and their mathematical interpretation, rather than independently executing the computations.

## 1. Formula, normalization, and the role of optimization — (a)

At an eigenframe, write
\[
w=W^+(\zeta,\zeta),\qquad
\mu_1=w+\frac{s}{12},\qquad
\mu_2+\mu_3=\frac{s}{6}-w.
\]
The trace-free restriction of \(W^+\) to \(\zeta^\perp\) satisfies
\[
|W^+_{\perp\perp}|^2=\frac{(\mu_2-\mu_3)^2}{2}.
\]
Consequently,
\[
-\left(w+\frac{s}{12}\right)\left(w-\frac{s}{24}\right)
-|W^+_{\perp\perp}|^2
=
-\frac{\mu_1(\mu_1-\mu_2-\mu_3)}2
-\frac{(\mu_2-\mu_3)^2}2.
\]
This reproduces the fitted coefficients
\[
\frac{s^2}{288}-\frac{sw}{24}-w^2-|W^+_{\perp\perp}|^2.
\]

With the notes’ definition of \(\Phi\), the expansion is
\[
\boxed{
\frac{P(\tilde g)-P(g)}{8\pi^2}
=
1-\varepsilon\mu_1
+\frac{\Phi}{2}\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2).
}
\]
The factor \(1/2\) comes from
\[
\int_{\asymp\sqrt{\varepsilon}}^R\frac{dr}{r}
=\frac12\log(1/\varepsilon)+O_R(1).
\]
For CH with \(s=-24\), therefore, \(\Phi=-18\) means an actual logarithmic term \(-9\varepsilon^2\log(1/\varepsilon)\), as recorded in the ledger. A dimensionally precise logarithm is \(\log(R^2/\varepsilon)\); changing the fixed reference scale changes only the \(O(\varepsilon^2)\) term.

**Optimization is substantive.** For perpendicular CH,
\[
s=-24,\quad w=2,\quad |W^+_{\perp\perp}|^2=18.
\]
The recorded \(K=0\) column gives
\[
\Phi_{K=0}
=\frac{576}{144}-\frac{5(-48)}{24}+2(4)-\frac59(18)
=12,
\]
whereas the optimized value is \(-18\). Thus the saving comes from the corrector, not simply from attaching an uncorrected Burns metric.

The rational formula is strongly supported by the recorded fits. The excerpts do not yet contain an exact evaluation of the complete minimized quadratic form.

## 2. Chern–Weil and \(W^-/\operatorname{Ric}^\circ\) independence — (b)

In the stated norm convention,
\[
P(g)=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2(2\chi+3\tau).
\]
A blow-up changes \(2\chi+3\tau\) by \(-1\), giving exactly
\[
P(\tilde g)-P(g)-8\pi^2
=
F_+(\tilde g)-F_+(g),
\qquad
F_+(g)=4\int|W^+|^2+\frac1{12}\int s^2.
\]

The inference
\[
W^+(p)=s(p)=0
\quad\Longrightarrow\quad
F_+(\tilde g)-F_+(g)\ge0
\]
does **not** follow directly. The expression is a difference of two integrals. Vanishing at one point does not make the second integral vanish.

There is, however, a direct formal square argument that supplies the intended conclusion without requiring an exact local ASD scalar-flat representative.

Set
\[
\mathcal C(g)=\left(2W^+(g),\,s(g)/\sqrt{12}\right).
\]
For Burns, \(\mathcal C(\delta+\varepsilon A)=0\) identically. If the quadratic background jet \(B\) has only \(W^-\) and traceless-Ricci curvature, then
\[
D\mathcal C_\delta[B]=0.
\]
For
\[
g_{\varepsilon,\nu}
=\delta+\varepsilon A+\nu B+\varepsilon\nu K,
\]
the expansion on \(r=1\) therefore begins as
\[
\mathcal C(g_{\varepsilon,\nu})
=
\varepsilon\nu
\left(\mathcal A_B+D\mathcal C_\delta[K]\right)
+O(\varepsilon^2\nu,\nu^2),
\]
where \(\mathcal A_B\) is the mixed Burns–background response. Hence
\[
[\varepsilon^2\nu^2]\,
|\mathcal C(g_{\varepsilon,\nu})|^2\,d\mu
=
\left|\mathcal A_B+D\mathcal C_\delta[K]\right|^2\,d\omega.
\]
Its spherical integral is \(\ge0\).

This establishes the lower estimate for the pure \(W^-\) and Ricci sectors. **Exact zero requires an exact corrector satisfying**
\[
D\mathcal C_\delta[K]=-\mathcal A_B.
\]
The reported \(D=4\) zeros are excellent numerical evidence for this identity. The quoted A01 expression
\[
k_0^W=\frac32\operatorname{sym}(h_Wk_B)
-\frac14\operatorname{tr}(h_Wk_B)\delta
\]
provides a concrete \(W^-\) corrector, with symbolic verification reported in Step 58. Corresponding explicit Ricci-sector correctors are not displayed in the supplied excerpts.

Once these pure-sector zeros are established, \(U(2)_\zeta\) equivariance eliminates mixed terms with the \(s,W^+\) sector: \(W^-\), Hermitian traceless Ricci, and anti-Hermitian Ricci occupy distinct representation types. Thus the independence argument is sound in this strengthened form:

1. a chiral square gives a lower estimate of zero;
2. an explicit corrector attains zero;
3. representation decomposition removes cross terms.

A floating-point zero alone does not supply step 2 as an exact identity.

## 3. Quartic and cubic jets — (c)

The mechanism in Lemma 57.1 is valid for the prescribed Burns family.

Burns is scalar-flat and \(W^+=0\), so it is locally \(P\)-critical by the preceding Chern–Weil identity. For a quartic jet \(C\),
\[
\left.\partial_c\right|_{c=0}
\bigl(|\operatorname{Ric}^\circ|^2d\mu\bigr)
(\delta+\varepsilon A+cC)
=
\operatorname{div}V_\varepsilon.
\]
The \(\varepsilon^2C\) component has a vector field homogeneous of degree \(-3\). Its flux through a radius-\(r\) sphere is independent of \(r\):
\[
\int_{S_r}\langle V,n\rangle\,dS
=r^{-3}r^3\int_{S^3}\langle V,n\rangle\,d\omega.
\]
Therefore its integral over every spherical shell is zero, and it has no logarithmic coefficient.

There is an even simpler interpretation using \(F_+\): because both chiral curvature quantities vanish on Burns, the first variation of its \(F_+\) density is zero **pointwise**, for every \(C\). The Ricci density differs by characteristic-density divergences.

This removes the entire linear quartic-jet contribution, including both \(\nabla^2\mathrm{Rm}\) and the quadratic-curvature terms contained in normal-coordinate \(C\). Those quantities can still enter the \(O(\varepsilon^2)\) term.

For the cubic jet, \(-I\in U(1)_\zeta\) preserves the Burns tail and changes its sign. Linear cubic-jet contributions consequently have zero spherical average. A quadratic \(\nabla\mathrm{Rm}\) term has spatial weight six, rather than four, so it does not occupy the \(\varepsilon^2\) logarithmic term. This reasoning uses coordinates with no linear background metric jet, as in the stated setup.

## 4. Product tests and coordinate gauge — (d)

In the complex orientation of a Kähler surface,
\[
W^+=\operatorname{diag}(s/6,-s/12,-s/12),
\qquad
R^+=\operatorname{diag}(s/4,0,0).
\]
For \(\Sigma_1(K_1)\times\Sigma_2(K_2)\),
\[
s=2(K_1+K_2).
\]
Both layouts therefore give
\[
\Phi_{\rm par}
=-\frac12(s/4)^2
=-\frac{s^2}{32},
\qquad
\Phi_{\rm perp}
=-\frac12(s/4-0)^2
=-\frac{s^2}{32}.
\]

All recorded predictions are correct:

| \((K_1,K_2)\) | \(s\) | Predicted \(\Phi\) |
|---|---:|---:|
| \((-1,-1)\) | \(-4\) | \(-1/2\) |
| \((-1,-3)\) | \(-8\) | \(-2\) |
| \((-1,1)\) | \(0\) | \(0\) |
| \((-2,1/2)\) | \(-3\) | \(-9/32\) |
| \((1,2)\) | \(6\) | \(-9/8\) |

The reported \(D=6\) values match these numbers. The \(D=4\) values being larger is consistent with minimization over nested spaces.

**Finite-degree convergence genuinely depends on the coordinate gauge.** A cubic coordinate change generated by \(X_3\) changes the quadratic background jet by
\[
B'\!-\!B=\mathcal L_{X_3}\delta
\]
and changes the degree-zero corrector by a term proportional to
\[
\mathcal L_{X_3}A.
\]
Since \(X_3\) has degree three and \(A\) has degree \(-2\), this term has degree zero. Its angular expression can contain degree-six numerators divided by powers of \(r\). Thus a \(D=4\) angular representation in one gauge need not remain \(D=4\) in another.

The Step-58 contrast between normal and conformal coordinates is therefore geometrically meaningful, not contradictory. The complete minimum should be coordinate invariant; its representation in a truncated polynomial space need not be.

The density comparison is also consistent: characteristic-density differences have zero logarithmic spherical average. Agreement of the reported raw and effective matrices is a useful check on normalization, though it is not pointwise equality of the two densities.

## 5. Do degree-zero correctors exhaust the logarithmic contribution? — (e)

Power counting identifies degree zero as the principal corrector sector, but the statement “higher homogeneity produces other powers” is insufficient.

For example, a correction
\[
\varepsilon\,(\mathrm{Rm})^2H_2(x),
\qquad H_2(tx)=t^2H_2(x),
\]
can pair with \(\varepsilon A_{-2}\). Their degrees add to zero; four curvature derivatives then produce an \(r^{-4}\) density. This **does** occupy the logarithmic term. Its integrated contribution vanishes because it is a Burns first-variation term, not because its radial power is different.

There is useful symmetry information for the complete angular minimization. In normal coordinates, the \(s,W^+\) background sector and the Burns tail are \(SU(2)_-\)-invariant. If
\[
\Phi_B(K)=c(B)+b_B(K)+Q(K),\qquad Q(K)\ge0,
\]
then averaging \(K\) over \(SU(2)_-\) preserves \(b_B\) and cannot increase \(Q\). Because \(SU(2)_-\) acts transitively on \(S^3\), its invariant symmetric two-tensors form the ten-dimensional invariant-frame space already used in the CH calculation. Thus arbitrary angular modes cannot improve the \(s,W^+\) answer beyond that space. Together with exact zero-square correctors for the other curvature sectors, this would establish the full degree-zero minimum without extrapolating from \(D=6\).

For **arbitrary additional metric modifications**, a universal coefficient depending only on \(s,W^+(p)\) is not valid when the background is not \(P\)-critical. A concrete illustration leaves the Burns core unchanged. Define \(E_P\) by
\[
DP_g[h]=\int\langle E_P(g),h\rangle\,d\mu.
\]
On an annulus \(\varepsilon^\alpha<r<R\), with \(0<\alpha<1/4\), add
\[
h_\varepsilon=\varepsilon^2\chi_\varepsilon(r)r^{-4}T
\]
for a fixed tensor \(T\). Then
\[
DP_g[h_\varepsilon]
=
2\pi^2\alpha\,\varepsilon^2\log(1/\varepsilon)
\langle E_P(g)(p),T\rangle
+O(\varepsilon^2),
\]
while its quadratic curvature cost is
\[
O(\varepsilon^{4-8\alpha})=o(\varepsilon^2).
\]
This higher-order tail can therefore alter the logarithmic coefficient whenever \(E_P(g)(p)\ne0\).

The formal theorem remains meaningful for its specified matched ansatz. Its extension to general constructions requires both the first-variation cancellations and an explicit description of the permitted tails. At a \(P\)-critical bulk, the displayed extra term vanishes.

## 6. General-type surfaces — (f)

For a KE metric with \(s\ne0\),
\[
R^+=\operatorname{diag}(s/4,0,0).
\]
Unit \(\zeta\perp\omega\) form a circle, and
\[
\Phi=-\frac{s^2}{32},\qquad
\frac{\Phi}{2}=-\frac{s^2}{64}.
\]
For \(\operatorname{Ric}=\lambda g\), this is \(-\lambda^2/4\), matching Step 58. The statement with strict saving does not include Ricci-flat KE metrics, for which \(s=0\).

For a smooth general-type surface with ample canonical bundle, the KE bulk has \(P=0\). Subject to the stated remainder estimate, \(k\) disjoint corrected cells give
\[
P<8\pi^2k,\qquad k\ge1.
\]

Smooth KE metrics alone do not cover every minimal general-type surface: a surface with \((-2)\)-curves is represented instead by its canonical orbifold. The extension described in Step 57 uses:

- a KE metric on that canonical orbifold;
- Burns cells at \(k\) regular points;
- Ricci-flat Kronheimer resolutions of its ADE points, each with \(P=0\).

There is no need to synchronize all scales. Fix the Burns scales so that the sum of their savings is positive; then send the ADE-resolution scales to zero so their gluing errors are smaller than that saving. This yields the same strict inequality on the smooth minimal resolution.

Thus the extension to all minimal general-type surfaces has a coherent geometric mechanism. Its realization depends on the general KE-cell remainder and the orbifold-resolution gluing input. The present computations establish the coefficient, not those estimates.

## 7. Strict Weyl inequality at a minimizing bulk — (g)

Assume the transplantation and energy-equality hypotheses in the notes, \(s<0\), and the rigorous second-order formula. Then the proposed strengthening is correct.

Put \(c=|s|/12\). From \(R^+\le0\), the eigenvalues \(w_i\) of \(W^+\) satisfy
\[
w_i\le c,\qquad \sum_iw_i=0.
\]
The maximum of \(\sum_iw_i^2\) is
\[
6c^2=\frac{s^2}{24},
\]
attained only at permutations of
\[
(c,c,-2c).
\]
The corresponding \(R^+\) spectrum is
\[
(0,0,s/4).
\]
Its two eigenvalues transverse to a chosen kernel vector are unequal, so the second-order saving excludes this spectrum in a minimizing configuration carrying a transplantable Burns component. Therefore
\[
\boxed{|W^+|^2<s^2/24.}
\]

The assumption \(s<0\) matters: if \(s=0\), then \(R^+\le0\) forces \(W^+=0\), and equality holds.

The permitted spectrum with a zero top eigenvalue is instead
\[
R^+=(0,s/8,s/8),
\qquad |W^+|^2=s^2/96.
\]
Pointwise strictness does not itself give a uniform numerical separation from \(s^2/24\) across varying bulks.

## 8. Hyperbolic and KE interpretation — (h)

The interpretation is consistent, but it has three distinct asymptotic cases:

1. **\(\lambda_{\max}(R^+)>0\):** an optimally oriented cell saves at order \(\varepsilon\).
2. **\(\lambda_{\max}(R^+)<0\):** every orientation costs at order \(\varepsilon\).
3. **\(\lambda_{\max}(R^+)=0\):**
   - unequal transverse eigenvalues give saving at order \(\varepsilon^2\log(1/\varepsilon)\);
   - equal transverse eigenvalues give zero at this order.

Real-hyperbolic curvature has
\[
R^+=(s/12)I,\qquad s<0,
\]
so its Burns construction approaches the topological cost from above. This agrees with the stated Theorem-H interpretation, but the local expansion alone does not establish a global infimum or the existence of a bubbling minimizer.

KE curvature with \(s<0\) has a kernel circle with transverse spectrum \((s/4,0)\), so the optimized construction approaches the topological cost from below. Under the reassembly hypotheses, this excludes a KE bulk carrying a transplantable Burns component.

The zero-transverse-anisotropy case remains undecided by first and logarithmic second order. Its \(O(\varepsilon^2)\) term and subsequent terms contain additional geometric information.

**Overall:** the algebra, normalization, product predictions, coordinate-gauge interpretation, and proposed strict Weyl consequence are consistent. The principal mathematical objects still absent from the supplied excerpts are exact Ricci-sector zero-square identities, an exact evaluation of the remaining invariant quadratic form, and the two-scale \(O(\varepsilon^2)\) remainder. Those objects connect the well-supported formal coefficient to the global strict upper bounds and minimizer rigidity.