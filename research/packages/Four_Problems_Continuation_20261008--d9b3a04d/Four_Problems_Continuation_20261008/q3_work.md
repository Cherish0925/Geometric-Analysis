# Q3: one genuine closure, and the surviving attainment question

## Outcome

The smooth homotopy-sphere cap assumption in Step 58, III.A is unnecessary in the low-energy smooth AE branch. The existing AE hypotheses imply a positive-Yamabe smooth compactification after an arbitrarily small Weyl-energy change. The Chang–Gursky–Yang sphere theorem then identifies the cap as the **standard smooth four-sphere**. This does not use the smooth four-dimensional Poincaré conjecture and does not require Bach-flatness.

It does not remove nontrivial end groups, partial collapse, or establish smooth attainment in an actual example. Those channels remain essential to Q3.

## 1. Conventions

Set

\[
P(g)=\int_N|\operatorname{Ric}^{\circ}|^2\,dV,
\qquad \mathcal W(g)=\int_N|W_{\mathrm{op}}|^2\,dV.
\]

Here Weyl uses the Hilbert–Schmidt curvature-operator norm. The covariant four-tensor norm used by Chang–Gursky–Yang satisfies

\[
|W_{(0,4)}|^2=4|W_{\mathrm{op}}|^2.
\]

## 2. AE cap theorem

**Proposition.** Let \((N^4,g)\) be connected, oriented, complete, scalar-flat, with one asymptotically Euclidean end of trivial group. Assume coordinates at infinity with derivative-controlled decay

\[
|\partial^j(g-\delta)|\le C r^{-\tau-j},\qquad j=0,1,2,
\quad \tau>0.
\]

Assume \(b_1(N)=b_2(N)=0\). If

\[
P(g)<16\pi^2,
\]

then the standard one-point smooth cap \(\widehat N=N\cup\{\infty\}\) is diffeomorphic to \(S^4\). Equivalently, the compact manifold obtained by filling the end with a standard four-ball is a standard smooth four-sphere. No prior simple-connectivity assumption is required.

### Proof

**Step 1: the exact relative energy identity.** A one-ended AE four-manifold has limiting Gauss–Bonnet boundary term 1. Since \(b_1=b_2=0\), the smooth cap has \(\chi(\widehat N)=2\), and \(\chi(N)=1\). The relative Chern–Gauss–Bonnet identity, with \(s=0\), gives

\[
8\pi^2(\chi(N)-1)=\mathcal W(g)-\frac12 P(g)=0.
\]

Consequently

\[
\int_N |W_{(0,4)}|^2\,dV=4\mathcal W(g)=2P(g)<32\pi^2.
\tag{1}
\]

**Step 2: truncate the AE tail, not the compactification singularity.** Choose a fixed cutoff \(\zeta\), equal to 1 for \(r\le R\) and 0 for \(r\ge2R\), with derivatives bounded by the corresponding powers of \(R^{-1}\). Put

\[
g_R=\delta+\zeta(r/R)(g-\delta)
\]

on the end, and retain \(g\) on the interior. For large \(R\), this is positive definite, equals \(g\) before \(R\), and is exactly Euclidean after \(2R\). On the transition annulus,

\[
|\operatorname{Rm}_{g_R}|+|s_{g_R}|\le C R^{-2-\tau}.
\]

Since the annulus has volume \(O(R^4)\),

\[
\|(s_{g_R})_-\|_{L^2}=O(R^{-\tau}),
\qquad
\int_{\{R<r<2R\}}|W_{g_R}|^2=O(R^{-2\tau}).
\tag{2}
\]

The original tail has the same vanishing bound, so

\[
\int_N|W_{(0,4),g_R}|^2\,dV_{g_R}
=2P(g)+o(1).
\tag{3}
\]

**Step 3: positivity of the conformal Laplacian survives the truncation.** A fixed smooth complete AE manifold has a homogeneous Sobolev inequality

\[
\|u\|_{L^4(g)}^2\le C_S\int_N|du|_g^2\,dV_g,
\qquad u\in C_c^\infty(N).
\tag{4}
\]

This is the ordinary Euclidean-end Sobolev inequality: patch the Euclidean inequality on the end with the compact-interior inequality, controlling the compact \(L^2\) term by the end through the connected compact region. The constant depends on this fixed \(N,g\); no uniform Sobolev bound over the minimizing sequence is being introduced.

The metrics \(g_R\) are uniformly equivalent to \(g\), with equivalence tending to 1, so they satisfy (4) with a common constant \(C'_S\). Hölder and (2) yield

\[
\begin{aligned}
Q_{g_R}(u)
&=6\int|du|_{g_R}^2+\int s_{g_R}u^2\\
&\ge\left(6-C'_S\|(s_{g_R})_-\|_2\right)
\int|du|_{g_R}^2\\
&\ge \frac{3}{C'_S}\|u\|_{L^4(g_R)}^2
\end{aligned}
\tag{5}
\]

for large enough \(R\).

**Step 4: the smooth cap has positive Yamabe constant.** Take a smooth positive function \(f\) on \(N\), equal to \(r^{-2}\) on \(r>3R\). The metric \(\bar g_R=f^2g_R\) extends smoothly across the added point: on the far end, Euclidean inversion turns \(r^{-4}\delta\) exactly into the Euclidean metric. Conformal covariance transfers (5) to compactly supported functions away from the point. A point has zero \(H^1\) capacity in dimension four, so cutoff approximation extends it to all smooth functions on \(\widehat N\). Thus

\[
Y(\widehat N,[\bar g_R])>0.
\tag{6}
\]

Weyl energy is conformally invariant, hence (3) and the strict inequality in (1) imply, for large \(R\),

\[
\int_{\widehat N}|W_{(0,4),\bar g_R}|^2
<32\pi^2
=16\pi^2\chi(\widehat N).
\tag{7}
\]

**Step 5: apply the smooth sphere theorem.** Chang–Gursky–Yang, *A conformally invariant sphere theorem in four dimensions*, Theorem A, states that a smooth closed four-manifold satisfying (6)–(7) is diffeomorphic to \(S^4\) or \(\mathbb RP^4\). The cap is oriented and has Euler characteristic 2, so it is \(S^4\). This completes the proof.

### Nature of the result

This is an application and connection of classical analysis, not a claimed new sphere theorem. It removes a specific unnecessary hypothesis from the current project. Its threshold is \(16\pi^2\); the existing project branch has the stronger input \(P<8\pi^2\).

## 3. How to use it in the existing one-blowup argument

The existing source has the charge inequality for scalar-flat AE pieces,

\[
\frac{P(N)}{8\pi^2}
\ge4(e-1)+4b_1+b^- -5b^+.
\tag{8}
\]

If its separate gauge-theoretic/topological argument establishes \(b^+=0\), then \(P(N)<8\pi^2\) forces

\[
e=1,\qquad b_1=b^-=0.
\]

The proposition applies and proves that every cap in this branch is standard \(S^4\). Thus the phrase “assuming the caps are diffeomorphic to \(S^4\)” may be deleted from Step 58, III.A **after** the source's other inputs have genuinely established the listed AE and homology hypotheses.

It would be incorrect to use (8) alone to prove \(b^+=0\), or to use the proposition at an ALE end with nontrivial group.

Given a smooth regular bulk, full energy equality, and the established standard cap type, a positive-energy topologically trivial bubble can be removed and replaced by a vanishing-energy Euclidean cap at the same attachment, producing a competitor on the same smooth manifold with strictly smaller limiting energy. If a surviving bubble has \(P=0\), it is Ricci-flat; an AE Ricci-flat manifold with trivial end group is Euclidean by Bishop–Gromov rigidity, since its asymptotic volume ratio is 1. In this already controlled smooth branch there are therefore no genuine bubbles. The global statements still require the bulk smooth-removability and compact-bulk alternatives rather than assuming them.

## 4. Why this does not already solve Q3

Anderson, *Canonical metrics on 3-manifolds and 4-manifolds*, Theorem 4.10, provides selected ideal minimizing configurations:

* compact orbifold branch: energy equality (4.43);
* open/partially collapsed branch: lower-semicontinuity inequality (4.45);
* criticality and local minimizing behavior on the regular set.

Remark 4.12 explicitly leaves completeness of the open domain and its finite-component structure unresolved in that general statement. The later topology discussion explicitly does not identify the open domain's topology with the original manifold. These conclusions do not select the compact smooth branch.

The new cap argument handles **trivial end groups** and **low-energy homology-sphere caps**. Nontrivial groups permit Ricci-flat ALE bubbles with \(P=0\); they cannot be eliminated by any positive per-bubble \(P\) threshold. Nor does strict insertion saving prove that collapse is impossible. Thus no actual manifold satisfying all of the remaining attainment conditions has been produced here.

For any actual smooth global minimizer on a negative-Yamabe manifold, the conformal Euler–Lagrange equation makes \(s\) constant. If it is Bach-flat, the remaining equation gives \(s\operatorname{Ric}^{\circ}=0\), and hence Einstein. Therefore a verified no-Einstein manifold with smooth attainment gives the requested non-Bach-flat example. The non-Einstein condition itself can be guaranteed in classical blowup-obstruction ranges; smooth attainment is the missing part.

## 5. Nearby new paper does not answer Q3

Branca–Dameno, *On the Bach tensor and quadratic curvature functionals*, arXiv:2610.08628 (October 6, 2026), studies a functional depending on the gradient of the Bach tensor and its conformal critical points/Bach-parallel minima. Its fixed-conformal-class minimizers are not unrestricted minimizers of \(\int|\operatorname{Ric}^{\circ}|^2\). It therefore supplies no immediate answer to Q3.

## Primary sources checked

1. Chang–Gursky–Yang (2003), Theorem A and norm convention, pp. 2–3 in arXiv version: <https://arxiv.org/pdf/math/0309287>. 
2. Anderson (2005/2006), Theorem 4.10, (4.43), (4.45), Remark 4.12 and topology discussion: <https://arxiv.org/pdf/math/0511034>. Refs , .
3. LeBrun (2004), §11: explicit question about non-Bach-flat optimal metrics: <https://arxiv.org/pdf/math/0404251>. Ref .
4. Branca–Dameno (2026), different functional: <https://arxiv.org/html/2610.08628v1>. Ref .

No full solution or unconditional new global minimizer is asserted.
