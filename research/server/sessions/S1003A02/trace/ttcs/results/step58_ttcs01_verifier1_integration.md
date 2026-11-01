# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 58,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step58_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step58_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the formal Theorem 57.Φ and the Step-58 cross-checks. The claim is:

(a) For a Burns insertion on a 4-manifold at a point p with zeta an eigenvector of R⁺ = W⁺ + s/12 having eigenvalue μ₁ (other: μ₂, μ₃), the ε²log(1/ε) coefficient in P(g̃)/(8π²) is Φ = -μ₁(μ₁-μ₂-μ₃)/2 - (μ₂-μ₃)²/2. In the kernel μ₁=0: Φ = -(μ₂-μ₃)²/2 ≤ 0.

(b) Φ depends only on s and W⁺(p), not on W⁻, Ric°, ∇Rm, or ∇²Rm. The proof of W⁻/Ric° independence is: P(g̃) - P(g) - 8π² = Δ(4∫|W⁺|² + ∫s²/12) by Chern-Weil; if W⁺=0,s=0 at p the right side is ≥ 0, so W⁻/Ric° coefficients are nonneg, and D=4 attains 0. Check this argument.

(c) Lemma 57.1: ∇²Rm drops out because the Burns family δ+εA is P-critical for all ε, so the C-linear coefficient is a divergence of a degree -3 field on S³, with zero integrated coefficient. ∇Rm drops out by parity under U(1)_ζ.

(d) Product-background test: Σ₁(K₁)×Σ₂(K₂) has R⁺=diag(s/4,0,0), s=2(K₁+K₂). Both par (μ₁=s/4) and perp (μ₁=0) layouts should give Φ = -s²/32. The computation uses conformal coordinates (nonzero quartic C). Does the corrector convergence rate depend on the gauge of the background jet?

(e) The strategist question: do degree-0 correctors exhaust the contributions to the log coefficient? That is, correctors of higher homogeneity feed other powers of r, not the ε²log corner.

(f) Consequence: every compact KE surface has R⁺=diag(s/4,0,0). The kernel circle ζ⊥ω gives Φ=-s²/32<0 at every point. Does this give p_*(X#kCP̄²) < 8π²k for ALL minimal general-type X? Scope: formal (needs the rigorous remainder).

(g) Minimizer rigidity: R⁺≤0, and μ_max(R⁺)=0 ⟹ μ₂=μ₃. Combined with |W⁺|²≤s²/24 on R⁺≤0, does this strengthen to |W⁺|²<s²/24 strictly?

(h) The unification reading: R⁺<0 (interior of the cone) is decided at first order (positive cost -εμ₁>0); the boundary at second order (Φ≤0). Real-hyperbolic = Theorem H regime (cost, bubbling allowed); KE = saving regime (bubbling excluded at minimizers). Is this consistent and complete?

## Integrated Scientific Memo

# Verification memo: Theorem 57.Φ and Step-58 cross-checks

The supplied material supports a consistent **optimized formal Burns coefficient**, but not yet a proved general-background asymptotic theorem. The algebra and recorded cross-checks agree. Three corrections are essential:

1. The coefficient multiplying \(\varepsilon^2\log(1/\varepsilon)\) in \(P/(8\pi^2)\) is **\(\Phi/2\), not \(\Phi\)**.
2. The stated Chern–Weil nonnegativity argument needs repair: vanishing of \(W^+\) and \(s\) at one point does not make a difference of integrals nonnegative.
3. Degree-zero correctors are the relevant optimization sector of the prescribed matched construction, but higher-homogeneity terms require **first-variation cancellations**, not power counting alone.

Only the notes and computational summaries are supplied, not the scripts, arrays, or exact reduced matrices. Thus the numerical values below are checked for consistency, not independently recomputed.

## 1. Formula and normalization — (a)

At an eigenframe, put \(w=W^+(\zeta,\zeta)\). Since \(\operatorname{tr}R^+=s/4\),
\[
\mu_1=w+\frac{s}{12},\qquad
\mu_2+\mu_3=\frac{s}{6}-w,
\qquad
|W^+_{\perp\perp}|^2=\frac{(\mu_2-\mu_3)^2}{2}.
\]
Therefore the reported invariant form becomes
\[
\begin{aligned}
\Phi
&=-\left(w+\frac{s}{12}\right)\left(w-\frac{s}{24}\right)
-|W^+_{\perp\perp}|^2\\
&=\frac{s^2}{288}-\frac{sw}{24}-w^2-|W^+_{\perp\perp}|^2\\
&=-\frac{\mu_1(\mu_1-\mu_2-\mu_3)}2
-\frac{(\mu_2-\mu_3)^2}{2}.
\end{aligned}
\]
This exactly matches the fitted coefficients. In particular,
\[
\mu_1=0
\quad\Longrightarrow\quad
\Phi=-\frac{(\mu_2-\mu_3)^2}{2}\le0.
\]

The correctly normalized expansion is
\[
\boxed{
\frac{P(\tilde g)-P(g)}{8\pi^2}
=
1-\varepsilon\mu_1
+\frac{\Phi}{2}\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2).
}
\]
Indeed, the logarithmic annulus begins at radius comparable to \(\sqrt\varepsilon\), so
\[
\int_{\asymp\sqrt\varepsilon}^{R}\frac{dr}{r}
=\frac12\log(1/\varepsilon)+O_R(1).
\]
A dimensionally precise logarithm is \(\log(R^2/\varepsilon)\); fixing \(R\) changes only the \(O(\varepsilon^2)\) term.

For CH, \(s=-24\) and \(R^+\) has spectrum \((-6,0,0)\). A kernel direction gives \(\Phi=-18\), hence the actual logarithmic term is \(-9\varepsilon^2\log(1/\varepsilon)\).

**Optimization is indispensable.** Using the recorded \(K=0\) column, perpendicular CH gives \(\Phi_{K=0}=12\), whereas optimization gives \(-18\). The theorem is about the corrected, optimized construction—not every insertion with a Burns core.

The supplied numerical fits strongly support the rational formula. They are not an exact evaluation of the full minimized quadratic form.

## 2. Independence of \(W^-\) and \(\operatorname{Ric}^{\circ}\) — (b)

In the stated norm convention, Chern–Weil gives
\[
P(g)=F_+(g)-8\pi^2T_+(M),
\qquad
F_+(g)=\int\left(4|W^+|^2+\frac{s^2}{12}\right),
\quad T_+=2\chi+3\tau.
\]
A blow-up decreases \(T_+\) by one, so
\[
\boxed{
P(\tilde g)-P(g)-8\pi^2=F_+(\tilde g)-F_+(g).
}
\]

This identity is correct. The following inference is not:
\[
W^+(p)=s(p)=0
\quad\Longrightarrow\quad
F_+(\tilde g)-F_+(g)\ge0.
\]
Pointwise vanishing does not imply that \(F_+(g)\) vanishes in the insertion region.

An exact local ASD scalar-flat representative would repair that inference, but existence with arbitrary prescribed \(W^-\) and Ricci jets is not established in the supplied material. Scalar-flat products and hyperkähler examples do not by themselves establish arbitrary prescribed-jet realization.

### A direct formal repair: the chiral square

Write
\[
\mathcal C(g)=\left(2W^+(g),\,s(g)/\sqrt{12}\right),
\qquad F_+(g)=\int|\mathcal C(g)|^2\,d\mu.
\]
Burns satisfies \(\mathcal C(\delta+\varepsilon A)=0\) identically. If the quadratic jet \(B\) contains only \(W^-\) and traceless-Ricci curvature, then
\[
D\mathcal C_\delta[B]=0.
\]
For the formal family
\[
g_{\varepsilon,\nu}
=\delta+\varepsilon A+\nu B+\varepsilon\nu K+\nu^2C+\cdots,
\]
the term linear in \(\nu\) begins as
\[
\mathcal C(g_{\varepsilon,\nu})
=\varepsilon\nu\bigl(\mathcal A_B+D\mathcal C_\delta[K]\bigr)
+O(\varepsilon^2\nu,\nu^2).
\]
Consequently,
\[
[\varepsilon^2\nu^2]\,
|\mathcal C(g_{\varepsilon,\nu})|^2\,d\mu
=
\left|\mathcal A_B+D\mathcal C_\delta[K]\right|^2\,d\omega.
\]
Thus the pure \(W^-\)/Ricci sector has a **nonnegative** formal logarithmic coefficient.

Its optimized value is exactly zero if, and only if, the mixed response can be cancelled:
\[
D\mathcal C_\delta[K]=-\mathcal A_B.
\]
The recorded \(D=4\) and \(D=6\) zeros strongly support such cancellation. Step 58 also quotes an explicit \(W^-\) corrector,
\[
k_0^W=
\frac32\operatorname{sym}(h_Wk_B)
-\frac14\operatorname{tr}(h_Wk_B)\delta,
\qquad
(h_W)_{ij}=-\frac13W^-_{ikjl}x^kx^l,
\]
with symbolic verification reported in the cited A01 work. That underlying calculation is not present here. Exact Ricci-sector correctors are not displayed.

Once the pure-sector zero identities are proved, \(U(2)_\zeta\)-equivariance rules out mixed quadratic terms with the \(s,W^+\) sector: the listed curvature sectors have distinct representation types.

The repaired independence proof is therefore:

- the chiral square gives the lower bound zero;
- exact correctors attain zero;
- equivariance removes cross terms.

The first step follows formally from the supplied setup. The second still requires exact identities beyond floating-point zeros.

## 3. Cubic and quartic jets — (c)

### Quartic jet \(C\)

Burns is scalar-flat and ASD, so it is locally \(P\)-critical. For a quartic perturbation \(C\), the Ricci-density first variation is a divergence:
\[
\left.\partial_c\right|_{0}
\bigl(|\operatorname{Ric}^{\circ}|^2d\mu\bigr)
(\delta+\varepsilon A+cC)
=\operatorname{div}V_\varepsilon.
\]
The \(\varepsilon^2C\) component of \(V_\varepsilon\) is homogeneous of degree **\(-3\)**. Its radial flux is constant:
\[
\int_{S_r}V\cdot n\,dS
=r^{-3}r^3\int_{S^3}V\cdot n\,d\omega.
\]
Hence its divergence integrates to zero on every spherical annulus. Equivalently, the spherical average of its degree-\(-4\) divergence vanishes, so there is no logarithmic coefficient.

This does **not** say that the flux itself is zero, nor that \(V\) is a tangential field whose divergence theorem is applied on \(S^3\). Those formulations would be incorrect.

There is a simpler proof using \(F_+\): since \(W^+=s=0\) on Burns, the first variation of its \(F_+\) density is zero pointwise for every \(C\). The Ricci-density formulation differs by characteristic-density divergences.

This removes the entire linear quartic-jet term, including both \(\nabla^2\mathrm{Rm}\) and the curvature-quadratic pieces of the normal-coordinate quartic jet. These quantities may still affect the regular \(O(\varepsilon^2)\) term.

### Cubic jet

In coordinates with no linear metric jet, the cubic background jet is odd under \(-I\in U(1)_\zeta\), while the Burns tail is even. Its linear spherical contribution vanishes by parity. A quadratic \(\nabla\mathrm{Rm}\) contribution has spatial weight six rather than four and does not enter the \(\varepsilon^2\log\) term.

Thus Lemma 57.1 has a valid formal mechanism; the degree and flux interpretation above are the necessary corrections.

## 4. Product tests and coordinate gauge — (d)

For any Kähler surface in its complex orientation,
\[
W^+=\operatorname{diag}(s/6,-s/12,-s/12),
\qquad
R^+=\operatorname{diag}(s/4,0,0).
\]
For \(\Sigma_1(K_1)\times\Sigma_2(K_2)\), \(s=2(K_1+K_2)\). Therefore
\[
\Phi_{\mathrm{par}}=-\frac12(s/4)^2=-\frac{s^2}{32},
\qquad
\Phi_{\mathrm{perp}}=-\frac12(s/4-0)^2=-\frac{s^2}{32}.
\]

The Step-58 predictions are all correct:
\[
\begin{array}{c|c|c}
(K_1,K_2)&s&\Phi\\ \hline
(-1,-1)&-4&-1/2\\
(-1,-3)&-8&-2\\
(-1,1)&0&0\\
(-2,1/2)&-3&-9/32\\
(1,2)&6&-9/8
\end{array}
\]
The recorded \(D=6\) values agree. The larger \(D=4\) values are consistent with minimization over a smaller corrector space.

### What is gauge-dependent?

Here \(D\) measures **angular polynomial complexity**, not radial homogeneity. All these \(K\)'s are degree-zero homogeneous tensors.

A cubic coordinate change generated by \(X_3\) changes
\[
B\mapsto B+\mathcal L_{X_3}\delta,
\qquad
K\mapsto K+\mathcal L_{X_3}A
\]
at the relevant orders, up to the sign convention for the coordinate change. Since \(X_3\) has degree three and \(A\) degree \(-2\), \(\mathcal L_{X_3}A\) has degree zero. Its angular representation can require higher-degree numerators.

Thus a normal-coordinate minimizer representable at \(D=4\) need not remain in the \(D=4\) space after passage to conformal coordinates. The complete optimized coefficient is coordinate invariant; the complexity required by a truncated angular basis need not be.

The nonzero quartic \(C\) is a useful test of Lemma 57.1, but **it is not the reason that \(D=6\) is needed**. Nor does the source support the assertion that \(D=2\) already captures the full answer: its own \(D=2\) table has positive \(W^-\)/Ricci penalties.

The reported density comparison is also consistent. Chern–Weil transgression implies zero logarithmic spherical average for the difference of the densities, not pointwise equality. The matrix agreement is a strong normalization check.

## 5. Do degree-zero correctors exhaust the log coefficient? — (e)

**For the prescribed matched jet ansatz: plausibly yes as an optimization statement, but the proposed power-counting proof is incomplete. For unrestricted metric modifications: no.**

A higher-homogeneity term can occupy the same radial corner. For example,
\[
\varepsilon\,(\mathrm{Rm})^2H_2(x),
\qquad H_2(tx)=t^2H_2(x),
\]
can pair with the degree-\(-2\) Burns tail. Their degrees sum to zero, and the four derivatives in the quadratic curvature density produce degree \(-4\), hence a possible logarithm.

Its integrated contribution vanishes because it is a first variation about the \(P\)-critical Burns family—not because it has the wrong radial power. A valid exhaustiveness argument must combine:

- power counting to identify all terms at the required parameter order;
- Burns criticality to eliminate higher-homogeneity linear terms;
- parity for odd jets;
- a complete angular minimization of the degree-zero term.

There is a useful route to the last step. For the \(s,W^+\) sector in normal coordinates, the background jet and Burns tail are \(SU(2)_-\)-invariant. If
\[
\Phi_B(K)=c(B)+b_B(K)+Q(K),\qquad Q\ge0,
\]
averaging \(K\) over \(SU(2)_-\) preserves the linear term and cannot increase \(Q\). Since this group acts transitively on \(S^3\), invariant symmetric two-tensors form the ten-dimensional invariant-frame space described in the notes. Exact minimization there would settle **all angular modes** in the \(s,W^+\) sector. Exact zero-square correctors would settle the other sectors.

Thus \(D=4\to6\) stability is supporting evidence, but is not the proof of exhaustive minimization.

### Why the allowed construction must be specified

On a non-\(P\)-critical background, additional singularly scaled tails can change the logarithmic coefficient while leaving the Burns core untouched. Define \(E_P\) by
\[
DP_g[h]=\int\langle E_P(g),h\rangle\,d\mu.
\]
On an annulus \(\varepsilon^\alpha<r<R\), with \(0<\alpha<1/4\), take
\[
h_\varepsilon=\varepsilon^2\chi_\varepsilon(r)r^{-4}T
\]
for a fixed tensor \(T\). Then
\[
DP_g[h_\varepsilon]
=
2\pi^2\alpha\,\varepsilon^2\log(1/\varepsilon)
\langle E_P(g)(p),T\rangle+O(\varepsilon^2),
\]
whereas its quadratic curvature cost is
\[
O(\varepsilon^{4-8\alpha})=o(\varepsilon^2).
\]
Accordingly, the coefficient cannot be universal over arbitrary insertions when \(E_P(g)(p)\ne0\). This does not contradict Theorem 57.Φ understood as the coefficient of its specified matched ansatz. At a \(P\)-critical bulk this particular freedom has zero linear contribution.

## 6. Scope of the general-type consequence — (f)

For a KE surface with \(s\ne0\), the unit kernel directions \(\zeta\perp\omega\) form \(S^1\), and
\[
\Phi=-\frac{s^2}{32},
\qquad
\frac{\Phi}{2}=-\frac{s^2}{64}.
\]
For \(\operatorname{Ric}=\lambda g\), \(s=4\lambda\), so the saving in \(P/(8\pi^2)\) is
\[
\frac{\lambda^2}{4}\varepsilon^2\log(1/\varepsilon).
\]
The phrase “every compact KE surface saves strictly” needs the exception \(s=0\): Ricci-flat KE surfaces have \(\Phi=0\).

For a general-type surface with ample canonical bundle, the negative KE bulk has \(P=0\). Assuming a remainder \(o(\varepsilon^2\log(1/\varepsilon))\), \(k\) disjoint corrected cells give
\[
P(\tilde g)
=
8\pi^2\left[
k-\frac{s^2}{64}\sum_{j=1}^k
\varepsilon_j^2\log(1/\varepsilon_j)
+O\!\left(\sum_j\varepsilon_j^2\right)
\right]
<8\pi^2k.
\]

To cover **all minimal general-type surfaces**, including those with \((-2)\)-curves, the additional mechanism in the sources is essential:

- use the negative KE canonical orbifold;
- place Burns cells at regular points;
- resolve its ADE points using Ricci-flat Kronheimer spaces, with \(P=0\).

Fix Burns scales giving a positive total saving, then choose the ADE-resolution scales sufficiently small that their gluing errors are smaller than that saving. No simultaneous scale balancing is needed for this strict inequality.

Thus the claimed extension has a coherent formal construction and no remaining \(W^-\) or \(c_1^2/c_2\) restriction. It still depends on the KE-cell remainder and zero-energy resolution gluing. The coefficient computation alone does not establish it unconditionally.

For fixed disjoint cells that equal the background outside their supports, \(P\) is additive across those regions. Long-range batch interactions are not an additional obstruction to the fixed-\(k\) strict inequality; they become relevant for moving backgrounds, shrinking cell separation, or quantitative matching laws.

## 7. Minimizer rigidity and strict Weyl bound — (g)

Assume the energy ledger, reassembly hypotheses, a transplantable one-attachment Burns component, and a rigorous version of the logarithmic expansion. Then the first-order argument gives \(R^+\le0\). At a kernel point, unequal transverse eigenvalues give \(\Phi<0\), contradicting minimality by transplanting the bubble there. Hence
\[
\lambda_{\max}(R^+)=0
\quad\Longrightarrow\quad
\mu_2=\mu_3.
\]

For \(s<0\), let \(c=|s|/12\) and let \(w_i\) be the eigenvalues of \(W^+\). Then
\[
w_i\le c,\qquad \sum_iw_i=0.
\]
Set \(t_i=c-w_i\ge0\), so \(\sum_i t_i=3c\). It follows that
\[
|W^+|^2=\sum_i t_i^2-3c^2
\le9c^2-3c^2
=\frac{s^2}{24}.
\]
Equality occurs only at permutations of
\[
W^+=(c,c,-2c),
\qquad
R^+=(0,0,s/4).
\]
For a kernel vector the transverse eigenvalues are \(0\) and \(s/4\), hence unequal. The second-order rigidity excludes equality:
\[
\boxed{|W^+|^2<s^2/24\quad\text{at every regular bulk point with }s<0.}
\]

The permitted zero-top-eigenvalue spectrum is instead
\[
R^+=(0,s/8,s/8),
\qquad
W^+=(c,-c/2,-c/2),
\qquad
|W^+|^2=s^2/96.
\]
If \(s=0\), \(R^+\le0\) forces \(W^+=0\), so the proposed strict inequality is false. Across varying bulks, pointwise strictness supplies no universal quantitative separation.

These conclusions concern configurations with the stated transplantable bubble. They are not restrictions on arbitrary \(P\)-critical metrics.

## 8. Hyperbolic/KE unification and its limits — (h)

The interpretation is consistent but not complete:

| Optimally oriented point | Leading response | Conclusion available from the expansion |
|---|---|---|
| \(\lambda_{\max}(R^+)>0\) | negative order-\(\varepsilon\) term | saving |
| \(\lambda_{\max}(R^+)<0\) | positive order-\(\varepsilon\) term | local cost |
| \(\lambda_{\max}(R^+)=0\), transverse eigenvalues unequal | negative \(\varepsilon^2\log\) term | saving |
| \(\lambda_{\max}(R^+)=0\), transverse eigenvalues equal | both displayed terms vanish | unresolved |

For real-hyperbolic curvature,
\[
R^+=(s/12)I,\qquad s<0,
\]
every direction costs at first order. The formal logarithmic coefficient is also positive, \(\Phi=s^2/288\). This agrees with the stated Theorem-H regime, but the local calculation alone proves neither the global infimum nor existence of a bubbling minimizer.

For negative KE curvature, a kernel direction has transverse spectrum \((s/4,0)\), hence saves at logarithmic second order. Under the transplantation hypotheses this excludes a KE bulk carrying the relevant Burns component—not every possible bubbling channel.

Two source formulations should be corrected:

- A KE insertion family approaches the threshold \(8\pi^2k\) **from below**, but once \(p_*<8\pi^2k\), that family is not a minimizing sequence. It proves nothing by itself about attainment or nonattainment of \(p_*\).
- In the equal-transverse-eigenvalue case, the next unresolved object is already the **regular \(O(\varepsilon^2)\) coefficient**, not necessarily a third-order term.

## Precise remaining mathematical objects

The substantive gap is larger than the remainder alone, though the remainder is essential for applications:

1. **Exact optimized coefficient:** evaluate the invariant quadratic form exactly, with gauge null directions treated explicitly.
2. **Exact sector cancellation:** verify the displayed \(W^-\) corrector and exhibit Ricci-sector correctors satisfying the zero-square equation.
3. **Exhaustiveness:** use symmetry averaging and first-variation cancellations to pass from finite polynomial tests to the complete allowed corrector class.
4. **Matched expansion:** construct an actual positive metric with the chosen corrector and prove the inner flux and a remainder \(o(\varepsilon^2\log(1/\varepsilon))\). The older \(O(\varepsilon^{6/5})\) estimate cannot detect this saving.
5. **Degenerate boundary:** determine the regular second-order response for \(R^+=(0,s/8,s/8)\).

The supplied evidence supports the claimed formal formula and its KE mechanism. It does not yet close these exact identities and analytic estimates, which are what turn the numerical/formal result into the stated global upper bounds and minimizer rigidity.