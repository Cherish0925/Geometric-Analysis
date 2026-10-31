# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md"
  ]
}
```

## Task

Independently check the proposed theorem and proof that every smooth complete four-dimensional metric which is exactly complex hyperbolic outside a compact set admits a unique positive conformal factor u→1 giving scalar curvature -24, without any sign assumption on the original scalar curvature. Check the weak sub/supersolution signs including derivative jumps, exhaustion argument, positivity, uniqueness, decay range 4<m<2+2sqrt(3), derivative estimates, Pfaffian and integration-by-parts boundary terms, exact conformal energy identities, and equality of exact-ended J6 and scalar-normalized P infima. Identify and repair any incorrect implication; provide a direct mathematical memo rather than procedural commentary.

## Output

# Memo: Step 22, the conformal factor to scalar curvature −24 on exact-CH-ended cells

## Summary

The theorem is correct. Barriers, exhaustion, positivity, uniqueness, decay and the two energy identities all hold as stated. Three statements need repair:

- **(i)** The comparison class \(\mathcal C_{-24}\) must be defined as conformal to exact-ended metrics. With that definition, uniqueness makes the normalization map surjective.
- **(ii)** The truncation step needs no transgression. Its error is \(O(e^{(4-2m)R})\), and it holds for any \(m>2\).
- **(iii)** The sentence "all integrals are finite because \(m>4\)" mixes two thresholds:
  - \(m>2\) makes the final integrals finite.
  - \(m>4\) is used for the linear sphere-flux terms and for the linear bulk integrand \(-s\Delta u/u\) on the finite domains.

The decay rate can also be sharpened to the endpoint \(m_*=2+2\sqrt3\). Step 21 contains a typo in the characteristic polynomial, which Step 22 implicitly fixes.

## 1. Model quantities

**CH² normalization.** With holomorphic curvature \(-4\), a geodesic sphere of radius \(r\) has principal curvatures \(2\coth 2r\) (once) and \(\coth r\) (twice). Hence
\[
H=\Delta r=2\coth 2r+2\coth r=3\coth r+\tanh r .
\]
Writing \(q=e^{-2r}\),
\[
H-4=3(\coth r-1)-(1-\tanh r)=\frac{6q}{1-q}-\frac{2q}{1+q}>0,
\qquad H-4=4e^{-2r}+O(e^{-4r}).
\]
So \(H>4\) strictly, sphere area is \(\sim e^{4r}\), and \(\lambda_0(\mathbf{CH}^2)=4\).

**Hypothesis on the end.** Everything uses only that the end is isometric to \(\{r>R_0\}\) in \(\mathbf{CH}^2/\Gamma\), with \(\Gamma\subset U(2)\) finite, fixing the centre and acting freely on spheres. This covers lens-type bolt cells. A cusp-type end would change \(H\) and the volume growth, and is not covered. The theorem should state the distance-sphere structure of the end explicitly.

**Scalar curvature transformation.** For \(\hat g=u^2g\):
- \(\hat s=u^{-3}(-6\Delta u+su)\);
- \(\hat s^2\,d\hat V=(s-6\Delta u/u)^2\,dV\);
- \(J_6=P+\tfrac14\int(s+24)^2\), using \(|g|^2=4\).

These are all correct.

**Gauss–Bonnet coefficient.** With the tensor norm,
\[
32\pi^2\,\mathrm{Pf}=|W|^2-2|\mathrm{Ric}^\circ|^2+s^2/6,
\]
so \(P=\tfrac12\int|W|^2+\tfrac1{12}\int s^2-16\pi^2\chi\). This matches Step 21 (1.2).

## 2. Barriers and derivative jumps

**Exponential terms.** On the end, \(\Delta e^{-at}=a(a-H)e^{-at}\). Therefore:
- \(\Delta u_-=a(H-a)e^{-at}\ge0\), giving \(F(u_-)=-6a(H-a)e^{-at}+24u_-(u_-^2-1)\le0\) for \(0\le u_-\le1\).
- \(\Delta u_+=a(a-H)(M-1)e^{-at}\le0\), giving \(F(u_+)\ge0\) for \(u_+\ge1\).
- On the core, \(F(0)=0\) and \(F(M)=M(s+24M^2)\ge0\).

**Jumps at \(r=R\).** The distributional Laplacian of a continuous piecewise-smooth function equals its classical part plus (outer minus inner) \(\partial_r\)-jump times surface measure.
- For \(u_-\) the jump is \(+a\), so \(-6\Delta u_-\) gains a nonpositive singular part. This is the correct sign for a subsolution.
- For \(u_+\) the jump is \(-a(M-1)\le0\), so \(-6\Delta u_+\) gains a nonnegative singular part. This is the correct sign for a supersolution.

**A cleaner formulation.** The jump computation can be replaced by lattice operations:
- \(u_-=\max(0,\,1-e^{-a(r-R)})\) is a maximum of two subsolutions. The second function is negative on \(R_0\le r<R\), so the maximum is \(0\) near the core.
- \(u_+=\min(M,\,1+(M-1)e^{-a(r-R)})\) is a minimum of two supersolutions. The constant \(M\) is a supersolution on the end too, since \(M(-24+24M^2)\ge0\).

Maxima of subsolutions and minima of supersolutions are weak \(H^1_{\rm loc}\) sub- and supersolutions. This requires \(R>R_0\), which the proof assumes.

**Conditions on the constants.**
- The subsolution property needs \(a<4\le H\).
- \(M\) exists because \(s\) is bounded below: \(s=-24\) off a compact core.
- The orderings \(u_-\le1\le u_+\) on \(S_L\) and \(u_-\le u_+\) hold everywhere.

## 3. Exhaustion, positivity, uniqueness

**Exhaustion.** On \(\Omega_L\), adding \(Ku\) with \(K\ge\sup s+72M^2\) makes \(-su-24u^3+Ku\) increasing on \([0,M]\). Monotone iteration from \(u_-\), with weak comparison against \(u_+\), gives a smooth \(u_L\in[u_-,u_+]\) with \(u_L=1\) on \(S_L\).

**Limit.** The bounds \(0\le u_L\le M\) and interior Schauder estimates on compact sets give a diagonal limit \(u\) that solves the equation with \(u_-\le u\le u_+\). Hence \(u\to1\) and \(u>0\) on \(\{r>R\}\).

**Positivity.** Write \(c=s+24u^2=c^+-c^-\). Then \(-6\Delta u+c^+u=c^-u\ge0\), so the strong maximum principle for nonnegative supersolutions applies to an operator with zeroth-order coefficient \(c^+\ge0\). A zero interior minimum would force \(u\equiv0\) on the connected cell, which is impossible. So \(u>0\).

Moreover \(\inf u>0\) because \(u\to1\). Thus \(\hat g\) is bi-Lipschitz to \(g\), hence complete. This step, used implicitly in item 1, should be written out.

**Uniqueness.** With \(w=u_1/u_2\) and \(g_2=u_2^2g\),
\[
-6\Delta_{g_2}w-24w+24w^3=0 .
\]
Because \(w\to1\), any supremum above \(1\) (or infimum below \(1\)) is attained, and there the two terms have the same strict sign. So \(w\equiv1\).

Uniqueness holds among all positive solutions with \(u\to1\), with no decay rate needed. Consequences:
- The solution is independent of the choice of \(a\) and \(M\). This is what lets item 2 use the barriers for every \(a<4\) on the same \(u\).
- Isometries preserving the end preserve \(u\).

## 4. Decay

**Equation for \(v=u-1\).**
\[
-6\Delta v+Vv=0,\qquad V=24(1+v)(2+v)>0 .
\]
This matches Step 22, since \(48+72v+24v^2=24(v^2+3v+2)\).

**Barrier.** For \(Ce^{-mr}\),
\[
(-6\Delta+V)(Ce^{-mr})=C\bigl[6(-m^2+mH+8)+(V-48)\bigr]e^{-mr}.
\]
Since \(V-48=O(e^{-ar})\) and \(-m^2+4m+8>0\) exactly for \(m<2+2\sqrt3\), this is eventually a strict supersolution. Comparing \(\pm v-Ce^{-mr}\) on \(\{r\ge R_1\}\) with \(V>0\) and decay at infinity gives \(|v|\le Ce^{-mr}\). The root is correct: \(m^2-4m-8=0\) gives \(m=2+2\sqrt3\approx5.46\).

**Correction to Step 21.** Step 21 writes "\(m^2+4m-8=0\), \(m=2+2\sqrt3\)". The positive root of \(m^2+4m-8\) is \(-2+2\sqrt3\approx1.46\), so the polynomial there is a typo.

**Endpoint strengthening.** At \(m=m_*\) the bracket equals
\[
6m_*(H-4)+(V-48)\ \ge\ 24m_*e^{-2r}(1+o(1))-Ce^{-ar}.
\]
Since \(a>2\) is available (take \(a\in(2,4)\)), this is eventually positive. Hence \(|v|=O(e^{-(2+2\sqrt3)r})\) with no \(\varepsilon\)-loss. This matches the radial linearized solutions \(e^{-m_*r}\).

**Derivatives.** CH has bounded geometry and \(V\) is a smooth function of \(v\). Bootstrapping on unit balls gives \(|\nabla^kv|(x)\le C_k\sup_{B_1(x)}|v|=O(e^{-mr})\).

## 5. Energy identities on \(C_R\)

**Divergent pieces.** On the cell, \(\int|W|^2\) and \(\int s^2\) diverge separately: CH² has \(|W^+|^2=s^2/24\ne0\). The identity must therefore be assembled on \(C_R\):
- The \(W\)-terms cancel pointwise.
- The \(s^2\)-difference has integrand \(-12s\Delta u/u+36(\Delta u/u)^2\). On the end, the first term is \(288\,\Delta v/(1+v)=O(e^{-mr})\), which is absolutely integrable only for \(m>4\).
- The Pfaffian difference is \(\oint_{S_R}T\mathrm{Pf}\).
- Substituting \(s=-24u^2+6\Delta u/u\) produces \(-24\int_{C_R}u\Delta u=24\int|\nabla u|^2-24\oint u\partial_\nu u\).

**Sphere terms.** The connection difference is \(A=O(|d\log u|)\) and \(DA=O(|\nabla^2\log u|)\). The transgression is \(O(|A|(|R|+|DA|+|A|^2))=O(e^{-mr})\), and \(\oint u\partial_\nu u\) is \(O(e^{-mr})\) pointwise. Against sphere area \(e^{4r}\), both are \(O(e^{(4-m)r})\), which tends to zero for \(m>4\). Section 4 supplies \(m\) up to \(5.46\), so both vanish.

**Why the linear terms are real.** Step 22's correction to Step 21 is right: the linear flux terms are genuinely linear. The linear Pfaffian flux is the Paneitz flux. On the end, \(\tfrac23 s\nabla f-2\mathrm{Ric}(\nabla f)=-4\nabla f\) and \(\Delta f\approx8v\), giving a leading density \(\approx4\partial_rv\). A crude \(m\in(2,4)\) bound would not dispose of it.

**Resulting identities.**
\[
P(g)-P(\hat g)=24\!\int|\nabla u|^2+3\!\int(\Delta u/u)^2,
\]
\[
J_6(g)-J_6(\hat g)=\!\int\Bigl[24|\nabla u|^2+3(\Delta u/u)^2+\tfrac14(s+24)^2\Bigr].
\]
All final integrals are finite once \(m>2\): \(|\nabla v|^2\) and \((\Delta v)^2\) are \(O(e^{-2mr})\), and \(s+24\) has compact support.

**Equality cases.** In either identity, equality forces \(\nabla u=0\), so \(u\equiv1\). In the second it also forces \(s\equiv-24\).

**Consistency checks.**
- \(3(\Delta u/u)^2=(e+24(u^2-1))^2/12\) follows from \(6\Delta u/u=e+24(u^2-1)\).
- Step 21's numerical table, with gains agreeing to about \(10^{-10}\) absolute, is consistent with these identities.

## 6. Equality of infima: required repair

**Defining \(\mathcal C_{-24}\).** "Complete metrics with \(s=-24\) and the decay of item 2" must mean
\[
\mathcal C_{-24}=\{w^2g' : g'\in\mathcal C_{\rm exact},\ s_{w^2g'}=-24,\ w\to1,\ |\nabla^k(w-1)|=O(e^{-m'r}),\ k\le2,\ \text{some } m'>2\}.
\]
A general CH-asymptotic metric with \(s=-24\) and a nonconformal tail \(\hat g-g_{CH}\) is not reached by truncating a conformal factor. Step 22's argument says nothing about such metrics.

**Normalization is surjective.** With the definition above, uniqueness makes the normalization map \(N:\mathcal C_{\rm exact}\to\mathcal C_{-24}\) onto. Given \(\hat g=w^2g'\), set \(g_R=w_R^2g'\) with \(w_R=1+\chi_R(w-1)\), where \(\chi_R\) is a cutoff equal to \(1\) for \(r\le R\) and \(0\) for \(r\ge R+1\). Then \(\hat g=(w/w_R)^2g_R\) with \(w/w_R\to1\), so \(N(g_R)=\hat g\).

**Truncation estimate.** \(J_6\) is a pointwise square, so no transgression enters:
\[
J_6(g_R)=P(\hat g)-P_{\{r>R\}}(\hat g)+J_6\big|_{\{R<r<R+1\}}(g_R).
\]
On the annulus, \(\mathrm{Ric}+6g\) is linear in \(\nabla^2f\), \(\Delta f\) and \(f\) to first order, hence \(O(e^{-m'R})\). Both correction terms are therefore \(O(e^{(4-2m')R})\).

Independently, the \(J_6\)-identity applied to \(g_R\) with factor \(w/w_R\) (supported in \(r\ge R\)) gives the same \(O(e^{(4-2m')R})\). This cross-check confirms that the parenthetical "linear transgression \(O(e^{(4-m)R})\)" in Step 22 is unnecessary.

**Conclusion.** \(\inf_{\mathcal C_{\rm exact}}J_6=\inf_{\mathcal C_{-24}}P\) holds as stated. Symmetry classes are preserved by uniqueness of \(N\).

## 7. Status

What is proved:
- The existence-and-uniqueness statement with no sign condition on \(s\).
- The rate \(m_*=2+2\sqrt3\), including the endpoint.
- The exact identities.
- The infimum reduction, given the corrected \(\mathcal C_{-24}\).

The positivity argument is genuinely global. The conformal Laplacian may have nonpositive spectrum on the core, and the solution may become small there, but it stays positive.

What is not touched:
- Attainment of the infimum.
- Lower bounds on \(\inf P\) over \(\mathcal C_{-24}\).
- Inputs that are only asymptotically CH, which need decay hypotheses on \(g-g_{CH}\) and on \(s+24\).