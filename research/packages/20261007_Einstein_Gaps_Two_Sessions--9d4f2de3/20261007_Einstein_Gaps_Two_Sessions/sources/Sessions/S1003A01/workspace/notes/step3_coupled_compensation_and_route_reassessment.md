# Step 3 — Coupled compensation in the triaxial cell and route reassessment

Session S1003A01, 4 Oct 2026. This note corrects and sharpens the Step-2 interpretation of O11. Notation follows I54 (`20260928_relative_cell_cost.md`) and I55 (`20260928_localization_and_coupled_filling.md`). The metric on a one-bolt cell is

\[
G=e^{2\phi}K,
\qquad K=\frac{dr^2}{F}+r^2(e^{2w}\sigma_1^2+e^{-2w}\sigma_2^2)+r^2F\sigma_3^2,
\]

with \(r_0^2=\mu\), exact complex-hyperbolic germ on a collar through radius \(R\), and
\(j=J/(2\pi^2)\), \(J=\int|\operatorname{Ric}_G+G|^2\).

## 1. The exact C1 deficit

For a general \(k\)-point conformal almost-Kähler cell, I54 uses

\[
v_K=d-\frac{T_2}{2},\qquad m_0=4d+4\pi T_1,
\qquad N=\frac12\int|\nabla\omega|^2.
\]

The scalar-free part of its conformally Kähler lower bound is

\[
\mathcal K=8\pi^2k+8\pi T_1+2T_2+
 \frac{(2\pi T_1+T_2)^2}{v_K}
 =8\pi^2k-4d+\frac{m_0^2}{4v_K}.
\]

Expanding the first two quadratic terms in I54 (6.6) gives the **exact** identity

\[
\boxed{
J(G)-\mathcal K
=\frac{A_0}{12}+4B_0+\frac14L_G
-\frac{N(2m_0-3N)}{4v_K},
}\tag{1}
\]

where \(L_G=\int(s_G+4)^2\). Thus the conjectured extension C1,
\(J\ge\mathcal K\), is equivalent to

\[
\boxed{
\frac{A_0}{12}+4B_0+\frac14L_G
\ge \frac{N(2m_0-3N)}{4v_K}.
}\tag{2}
\]

Only \(0<N<2m_0/3\) needs new information. This corrects the Step-2 suggestion that one should seek a bound on \(B_0\) alone: scalar transfer \(A_0\), self-dual Weyl anisotropy \(B_0\), and scalar variance \(L_G\) can and generally must pay jointly. Also, C1 is weaker than extending the *full* Theorem-1 remainder \(\mathcal K+L_G/4\), which would require (2) without the \(L_G/4\) term.

For one bolt in the radial normalization,

\[
d=\frac{\pi^2R^4}{2},\quad v_K=\frac{\pi^2}{2}(R^4-\mu^2),\quad
m_0=2\pi^2(R^4+2\mu),
\]

and therefore

\[
\frac{\mathcal K}{2\pi^2}=rac{(2+\mu)^2R^4}{R^4-\mu^2}.
\]

There is no hidden conformal-factor error: I54 writes \(K=u^2G\), I55 writes \(G=e^{2\phi}K\), so \(u=e^{-\phi}\); the conformal gradient term is part of \(A_0\). The exceptional period \(t_E=\pi\mu\) is measured by the canonical almost-Kähler metric \(K\), not directly by \(G\).

## 2. Exact radial form of the same problem

I55 defines

\[
I_R=\frac14(\mu^{-2}-R^{-4}),\quad
P_w=\int\left\{\frac{2F(w')^2}{r}+
\frac{8(\cosh2w-1)}{r^3}+
\frac{8\sinh^2(2w)}{r^3F}\right\}dr,
\]

\[
T_\phi=2\int\frac{F(\phi')^2}{r}dr,
\quad q=T_\phi-P_w,
\quad M_0=1+\frac2\mu,\quad M=M_0-q.
\]

Its Proposition 5 says

\[
j=\frac{M^2}{4I_R}+\mathscr R_{\rm rad},
\]

where

\[
\mathscr R_{\rm rad}=\frac14\int r^3\left(X-\frac{M}{I_Rr^4}\right)^2
+\frac14\int r^3Y^2+\frac12\int r^3Z^2+2\int r^3V_w^2.
\]

Since \(M_0^2/(4I_R)=\mathcal K/(2\pi^2)\), C1 is equivalently

\[
\boxed{
\mathscr R_{\rm rad}\ge
\frac{q(2M_0-q)}{4I_R}
\quad\text{when }0<q<2M_0.
}\tag{3}
\]

This is not a new theorem; it is the sharp profile-level target. It retains all actual variables and all residuals. The scalar mean identity

\[
L_Y=\int r^3Y=4B_\phi-\mu^2-2\mu-n-6G_\phi
\]

and its variance decomposition should be used inside (3), not optimized separately. The I55 zero-moment test shows why: a bolt-scale conformal profile can have \(M=0\) while keeping bounded total cost, and the payment then moves into the \(X,Y,Z\) squares. A scalar zeroth moment or a lower bound on \(|M|\) cannot close the problem.

A second warning is essential. If \(n=N/(2\pi^2)\), then

\[
n=2\int r^3F\left(w'+\frac{2\sinh2w}{rF}\right)^2dr,
\]

whereas \(P_w\) uses inverse radial weights. They are not interchangeable. After integrating its cross term, \(n\) even contains a negative \(-8\int r(\cosh2w-1)\) contribution. Equations (2) and (3) are equivalent global decompositions, but their apparent dangerous variables \(N\) and \(q\) encode different profile moments.

## 3. New computational instrument: measure compensation, not another unconstrained minimum

`workspace/scripts/cell_compensation.py` augments the verified Ricci code with both exact decompositions. For every actual Chebyshev profile it computes

- \(j\), the C1 constant \(K\), and \(j-K\);
- \(N/(2\pi^2)\), \(P_w,T_\phi,q,M\);
- the four radial payments \(R_X,R_Y,R_Z,R_V\);
- \(A_0/(2\pi^2)\), and \(B_0/(2\pi^2)\) inferred from the exact I54 identity;
- the formal gain \(n(2m-3n)/(4v)\);
- exact residuals of I54 and I55 as internal checks.

Pilot runs satisfy the radial decomposition to about \(10^{-13}\) and the I54 decomposition to machine precision. This simultaneously checks the normalizations and avoids implementing a second, unverified self-dual curvature operator merely to evaluate \(B_0\).

The script performs an augmented-Lagrangian minimization of \(j\) at prescribed \(N/m_0\), initialized from an optimized biaxial conformal cell and then seeded in low triaxial modes. This asks the correct scientific question: at a given formal nonintegrability gain, which actual remainder pays, and can their sum fall below it? Early moderate targets (for example \(\mu=0.1,R=2,N/m_0\approx0.05\) or \(0.15\)) are extremely expensive, with \(j\) of order \(20\) or \(60\), rather than near \(K\approx4.413\). Most payment appears in the inferred \(B_0\) and in \(V_w\), while the exact decomposition remains satisfied. These pilot values are numerical behavior of a finite-dimensional constrained optimizer, not lower bounds; they show that the earlier generic searches stayed close to \(N=0\) for a structural reason, but do not settle small \(N\) or finite-amplitude escape.

A broader small-to-middle-\(N\) sweep is running in `data/cell_compensation/sweep_mu01_R2.jsonl` (task reference `s3_t20_tool1`). The highest-value interpretation is the scaling as \(N\downarrow0\): if the minimum excess payment is linear or superlinear compared with the formal gain, that identifies the candidate coercive modulus. Repeating unconstrained optimization above four would add little.

## 4. What outside almost-Kähler identities do and do not give

The retrieved paper `Knowledge/objects/papers/Almost-Kähler-four-manifolds-with-harmonic-self-dual-Weyl-curvature--e2ac226d605a--8b3f793203ff/object.md` records the pointwise algebraic inequality

\[
|W^+|^2-|W^+(\omega)^\perp|^2\ge \frac38[W^+(\omega,\omega)]^2
\]

and, under the additional differential equation \(\delta W^+=0\), a LeBrun integral identity yielding \(\int s^2/24\ge\int|W^+|^2\), with equality only for cscK metrics. This explains how harmonic-Weyl criticality can convert Weyl anisotropy into scalar payment. It does **not** apply to arbitrary cell competitors: neither \(K\) nor \(G\) is assumed to satisfy \(\delta W^+=0\). Therefore the missing estimate is not already present in that literature. A productive inheritance would be to derive a *defect version* in which the failure of \(\delta W^+=0\) is paired with the actual Ricci residuals \(X,Z,V_w\), precisely the terms already visible in (3). This is a more plausible route than importing the harmonic-Weyl theorem verbatim.

## 5. Correction to the general bubbling route

The Step-2 implication “smooth minimizer or all topology paid for by AE bubbles” was too strong. Even after one proves compactness and an energy identity, a minimizing sequence can have an orbifold base, quotient-ended ALE levels, and marked topology distributed across the tree. A quotient-ended Ricci-flat ALE bubble can carry nontrivial \(H_2\) while paying zero \(\int|\operatorname{Ric}|^2\); Gauss–Bonnet and APS signature charges include \(1/|\Gamma|\) and \(\eta(S^3/\Gamma)\), so an individual terminal bubble has no universal \(8\pi^2\) Ricci charge. The smooth no-critical-cell proposition only forces a smooth stationary limit to be CH; it does not rule out a locally CH orbifold base resolved by Ricci-flat ALE pieces. Handles may enter collapsed necks rather than isolated \(H_2\)-bubbles.

Thus a lower-bound proof by degeneration requires, in addition to analytic compactness:

1. the limiting Euler–Lagrange equation on the regular base and classification/exclusion of residual locally CH orbifold geometries compatible with the fixed outer germ;
2. relative Chern–Weil/APS bookkeeping across every interface;
3. preservation and decomposition of the marked primitive exceptional/handle classes;
4. a whole-tree theorem that the **combined** base and bubble configuration pays \(8\pi^2q\).

The relevant charge belongs to a whole marked AE filling, not to each terminal bubble or homology generator. This makes general regularization much broader than C1 and not the best immediate main route.

## 6. Route judgment after the sharpening

The strongest immediate O11 line is the exact diagonal cell problem, but now as a coupled coercivity problem, not more unconstrained minimization:

- derive an inner-scale inequality after \(r=\sqrt\mu\,x\) coupling the inverse-weight conformal moment to \(Z\) and \(V_w\);
- combine it with an outer terminal-value estimate from the exact CH collar and the scalar mean/variance split for \(Y\);
- use constrained profiles to discover the correct coefficient and equality/degeneration mechanism;
- separately retain fixed-scale non-diagonal/MM constructions as the falsification route, because a subthreshold cell would immediately change the balanced first coefficient.

The desired lemma is exactly (3), or at minimum the weaker threshold version \(\mathscr R_{\rm rad}\ge4-M^2/(4I_R)\). The global cell conjecture and all-competitor balanced coefficient still require work outside this symmetric class. O10 and the fixed bundle \(E_D\) remain independent central branches; nothing in this note changes their status.

## 7. Fixed-exterior rigidity removes one major orbifold alternative

The broad warning about orbifold bases can be sharpened substantially for this *fixed-collar* problem. Let \(X=\mathbb{CH}^2/\Gamma\) be the original closed smooth CH surface, with volume \(V\), and choose the cell ball \(D\) with \(d=\operatorname{Vol}(D)<V/2\). Suppose a noncollapsed critical degeneration, after the unchanged exterior is glued back, has a compact connected orbifold base \(\mathcal O\) which is locally CH and contains the original exterior \(U=X\setminus D^\circ\) isometrically. Then \(\mathcal O\) is actually the original smooth CH surface.

Indeed, a complete locally CH orbifold is \(\mathbb{CH}^2/\Gamma'\) for a discrete cocompact isometry group \(\Gamma'\). Since deleting a four-ball does not change the fundamental group, \(\pi_1(U)=\Gamma\). Equality of the CH germ makes the holonomy of the embedded exterior the original faithful lattice representation, so after conjugation \(\Gamma<\Gamma'\). A lattice contained in a discrete group has finite index, and

\[
\operatorname{Vol}(\mathcal O)=\frac{V}{[\Gamma':\Gamma]}.
\]

On the other hand the embedded exterior has volume \(V-d\), hence

\[
V-d\le\frac{V}{[\Gamma':\Gamma]}.
\]

Because \(d<V/2\), the index is strictly below two and must equal one. Thus \(\Gamma'=\Gamma\), which is torsion-free, so \(\mathcal O\cong X\) smoothly and isometrically.

The local Euler–Lagrange equation supplies the locally CH hypothesis without integrating across orbifold points. On the regular base, compactly supported conformal variations give

\[
\Delta_+s+s+4=0.
\]

Since \(s=-4\) on the unchanged open collar, scalar unique continuation gives \(s\equiv-4\) on the connected regular set. The tensor equation then reduces to the I54 equation for \(E=\operatorname{Ric}+g\); because \(E=0\) on the collar, elliptic unique continuation gives \(E=0\). Einstein analyticity and continuation of the CH curvature type make the regular base locally CH, and this statement lifts through each orbifold chart.

Consequences for the bubbling route are precise. Under a noncollapsed orbifold compactness theorem with enough convergence to preserve the full exterior and to pass stationarity to the regular base, **orbifold base singularities are excluded by the exterior-volume argument**. Any bubble tree is attached to a smooth CH base point, so its root has trivial outer end group. Quotient end groups and eta terms may still appear at deeper levels, but they must cancel inside a whole tree whose external interface is \(S^3\). The remaining topological theorem is therefore narrower than stated in Section 5: establish the \(8\pi^2q\) cost for each complete critical whole-tree filling with trivial outer end and the inherited marked relative classes. Collapse and noncritical minimizing sequences remain separate analytic difficulties. This fixed-exterior rigidity does not by itself prove compactness or the cell conjecture, but it removes the most dangerous residual base geometry rather than merely listing it.

## 8. Stronger consequence: the noncollapsed stationary orbifold branch already obeys the threshold

Independent verification sharpened Section 7 in two ways.

First, the volume-smallness assumption is unnecessary once the exterior is a **smooth injective local isometry**, not merely a metric-space image. A precise statement is:

> Let \(X=\mathbb{CH}^2/\Gamma\) be closed and smooth, and let \(D\) be one embedded closed four-ball, or finitely many disjoint such balls, with connected exterior \(U=X\setminus D^\circ\). If a compact connected effective boundaryless locally CH orbifold \(\mathcal O\) admits a smooth injective local isometry \(U\to\mathcal O\), then \(\mathcal O\) is smooth and globally isometric to \(X\), with the global isometry extending the given exterior map.

The proof must use developing maps. The exterior inclusion gives, after conjugacy, \(\Gamma<\Gamma'\) for \(\mathcal O=\mathbb{CH}^2/\Gamma'\). If \(g\in\Gamma'\setminus\Gamma\), injectivity of \(U\to\mathcal O\) forces \(g\widetilde U\cap\widetilde U=\varnothing\). Hence the connected unbounded set \(g\widetilde U\) lies in one bounded lifted ball, impossible. Therefore \(\Gamma'=\Gamma\). Compactness/effectiveness/completeness and the smooth local-isometry hypothesis are essential; equality of a small collar germ alone would not establish the lattice inclusion.

Second, once this rigidity holds, the relative density (I54 (1.2)) makes whole-tree APS accounting unnecessary for the *threshold*. Let

\[
F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0.
\]

On CH, \(F=4\). If a fixed-collar sequence converges in \(C^2_{\rm loc}\) off finitely many points to a stationary orbifold base, Sections 7--8 show that the base is the original CH ball. For compact sets \(K\Subset D\setminus S\),

\[
\int_KF(g_i)\longrightarrow4\operatorname{Vol}(K).
\]

The exact relative identity

\[
J_i-8\pi^2q=\int_CF(g_i)-4d
\]

and nonnegativity on the omitted bubble/neck region give, after \(K\uparrow D\setminus S\),

\[
\boxed{\liminf_iJ_i\ge8\pi^2q.}
\]

Thus stationary noncollapsed finite-point orbifold degeneration cannot be a subthreshold mechanism, regardless of how quotient-ended ALE levels and marked topology are distributed. The remaining cell problem has become more sharply localized: a subthreshold sequence must evade this branch through collapse, failure of stationary/regular convergence, a non-orbifold or multi-fold completion, non-finite concentration, or a genuine smooth finite-amplitude competitor. The analytic compactness theorem remains hard, but the feared base/bubble charge classification is not needed merely to reach the threshold once the fixed exterior survives.

## 9. Result of the fixed-\(N\) compensation sweep

The managed sweep completed 32 constrained optimizations at \(\mu=0.1,R=2\), degree 14, with four low-mode starts at each target \(N/m_0\in\{5\cdot10^{-4},10^{-3},0.003,0.01,0.03,0.1,0.3,0.55\}\). Data are in `workspace/data/cell_compensation/sweep_mu01_R2.jsonl`; the complete execution record is in `workspace/tasks/s3_t20_tool1/`.

Every run stayed above C1, and both exact decompositions closed at roughly \(10^{-14}\). Representative best values are

| target \(N/m_0\) | attained | best \(j-K\) | formal gain | dominant payment |
|---:|---:|---:|---:|---|
| 0.0005 | 0.000507 | 0.1844 | 0.01663 | \(4B_0\approx0.198\), \(R_V\approx0.153\) |
| 0.001 | 0.001005 | 0.3432 | 0.03294 | \(4B_0\approx0.372\), \(R_V\approx0.303\) |
| 0.003 | 0.002998 | 0.9804 | 0.09796 | \(4B_0\approx1.073\), \(R_V\approx0.901\) |
| 0.01 | 0.010000 | 3.236 | 0.3233 | \(4B_0\approx3.547\), \(R_V\approx3.005\) |

At larger targets the separation grows rapidly (best observed \(j-K\approx9.89,36.05,139.41,323.02\) at target fractions \(0.03,0.1,0.3,0.55\)). In all optimized profiles \(q=T_\phi-P_w<0\), so the radial projection term itself lies *above* the C1 value; the constrained solver did not enter I55's dangerous \(q>0\) window. This is evidence of a specific mechanism rather than a theorem: low-cost ways to create almost-Kähler nonintegrability also create enough inverse-weight anisotropy \(P_w\) that conformal transfer cannot compensate it, with \(V_w\) and the self-dual Weyl remainder recording the same obstruction in the two decompositions. The near-linear small-target ratios \((j-K)/(N/m_0)\approx 369,343,327,324\) suggest a positive first-order coercive modulus in this discretization, but the smallest target is still contaminated by the nonzero finite-degree biaxial baseline and constrained optimization error. A rigorous proof should target an inequality linking \(N\) to \(P_w-T_\phi\), \(V_w\), and the scalar residuals, not infer a constant from these values.
