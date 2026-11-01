# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Knowledge/objects/papers/Canonical-Metrics-on-3-Manifolds-and-4-Manifolds--8d02c53d4380--0b5d0f7e0ac4/object.md",
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md"
  ]
}
```

## Task

Verify the mathematics of Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md for the four-manifold Einstein-gap problem (P(g)=int|Ric°|^2, p_*(M)=inf P). Check, as a geometric analyst: (1) whether Anderson's Theorem 4.10 (Asian J Math 2006, Knowledge object attached; see Thm 4.1, Cor 4.4, Lemma 4.5, Prop 4.6, (4.32)-(4.33), Cor 4.8, Thm 4.10 proof, Remark 4.12, (4.65)) really gives, for the functional Z^2=P on unit-volume metrics, case (I) energy equality and local minimality, and which steps of his proof are sketchy (local minimality of weak limits, no-neck equality, removability at Gamma=e points); (2) Lemma 53.0 telescoping of orbifold Euler characteristics converting the R^2 energy equality into p_*(M)=P(V,g0)+sum P(N_k), including bubble trees; (3) Theorem 53.F' generalizing Theorem F (attached step20 note) from Burns to ASD scalar-flat AE bubbles with homogeneous r^{-2} leading term and chiral flux Phi^{++}(N), including the topological reduction P(hat g)-P(g)-P(N)=4 Delta W^+ + Delta S/12 and the von Neumann rotation maximization; (4) Theorem 53.B (moving a Gamma=e bubble tree to any point/frame preserves the diffeomorphism type of M; energy equality turns positive first-order interaction into a competitor below p_*), and Corollary 53.C items 1-4, especially item 4 using the analytic CH cell; (5) Theorem 53.D attainment transfer (each bulk component attains p_*(V_a)), including the reducible-orbifold/multi-component case and two-ended necks; (6) Lemma 53.Y (Green-function argument that one-point compactifications of scalar-flat AE ends of order tau>1 have positive Yamabe invariant) and Theorem 53.E using Kobayashi's connected-sum inequalities. Give corrected statements where needed, counterexamples where a claim fails, and identify any hidden hypothesis (e.g. orientation of bubbles: CP^2-type bubbles couple to R^-, decay order of critical ALE ends, whether the bulk metric g0 is smooth enough for Theorem F's C^3 constant, whether p is required to be away from orbifold points). Do not invent literature; name precise knowledge requests if needed.

## Output

# Scientific verification memo

## Overall assessment

The main structural use of Anderson’s Theorem 4.10 is sound:

- Anderson’s \(\mathcal Z^2=\int |\operatorname{Ric}^{\circ}|^2=P\).
- With his curvature-operator normalization,
  \[
  \mathcal R^2(g)=8\pi^2\chi(M)+P(g)
  \]
  on a closed four-manifold.
- Therefore minimizing \(\mathcal R^2\) and minimizing \(P\) are equivalent, and their Euler–Lagrange equations agree.
- In case (I), Theorem 4.10 explicitly states the full \(\mathcal R^2\)-energy identity including the ALE pieces. After a corrected Euler ledger, this gives the asserted \(P\)-identity.
- Theorem 4.10 also explicitly states compactly supported local minimality of the regular metric \(g_0\). Since the variation of the Euler form integrates to zero for compactly supported variations, this transfers from \(\mathcal R^2\) to \(P\).

Several later conclusions require sharper hypotheses than presently written. The most important repairs concern reducible Euler bookkeeping, the decay-dependent remainder in Theorem 53.F′, one-ended versus multi-ended bubbles in Theorem 53.B, positivity of a rank-one flux, and the extra removability and ALE-decay theorems needed for Theorems 53.D–E.

---

## 1. What Anderson’s theorem supplies

### 1.1 The functional is the right one

Equation (4.32) in Anderson is
\[
\mathcal Z^{2p}_{\varepsilon}(g)
=
\int\left(|\operatorname{Ric}|^2-\frac14s^2\right)
+\varepsilon\int(1+|\operatorname{Ric}|^2)^p
=
P(g)+\varepsilon\int(1+|\operatorname{Ric}|^2)^p .
\]
Thus the note correctly identifies the perturbed functional.

For each fixed \(\varepsilon>0\), an upper bound for \(\mathcal Z^{2p}_{\varepsilon}\) gives an \(L^{2p}\) Ricci bound. Corollary 4.8 imports Corollary 4.4 and Proposition 4.6 to this functional, so the source supplies weak minimizing pairs and smoothness on the regular set. The proof of Theorem 4.10 then passes \(\varepsilon\to0\) using the \(L^2\)-curvature radius and the \(L^q\)-curvature radius estimate (4.49).

One nuance: an individual weak pair \((\Omega_\varepsilon,g_\varepsilon)\) need not itself have \(P\)-value within \(o(1)\) of \(p_*(M)\), because energy can sit in unresolved bubbles or collapsed regions. What Anderson ultimately supplies is a minimizing sequence on \(M\) and an idealized limit. The “Sacks–Uhlenbeck entrance” is therefore correct when formulated at the level of Theorem 4.10 rather than only the value of \(P(g_\varepsilon)\) on the regular pair.

### 1.2 Case (I) energy identity

The precise case-(I) statement is
\[
\mathcal R^2(g_0)+\sum_k\mathcal R^2(N_k,g_\infty^k)
=
\inf_{g\in\mathbb M_1}\mathcal R^2(g).
\]
The \(N_k\) are the ALE objects appearing through the complete bubble-tree decomposition described near (4.65). Reading the sum as including every vertex of the bubble tree is essential for Lemma 53.0.

This identity is stated by Anderson, not merely suggested. Its proof is terse: the source refers to the orbifold compactness and bubbling theory in references [8], [9], and [11]. The missing written derivation is precisely the vanishing of curvature energy on all neck annuli and the passage through iterated orbifold bubbles. Thus Step 53 may use the identity as part of Theorem 4.10, while a self-contained proof would need that neck analysis.

### 1.3 Local minimality

The final sentence of Theorem 4.10 states that \(g_0\) minimizes \(\mathcal F\) under compact perturbations. For \(\mathcal F=\mathcal R^2\), this is equivalent to compactly supported local minimality for \(P\), since
\[
\delta\!\int\bigl(|\mathrm{Rm}_{\rm op}|^2-|\operatorname{Ric}^{\circ}|^2\bigr)=0
\]
for a compactly supported variation.

The source gives little detail for the transfer of minimality from weak \(L^{2,2p}\) limits. A complete argument needs a replacement construction in harmonic coordinates and enough strong convergence on a transition annulus. Uniform convexity in the second derivatives after fixing harmonic gauge is a plausible mechanism, but that argument is not written in Anderson.

### 1.4 Trivial local groups are not removed by Anderson alone

Theorem 4.10 permits singular points with \(\Gamma=\{e\}\) and asserts only a \(C^0\) extension. It does not itself state that such a point becomes smooth after adding the puncture.

The precise external result needed for Theorem 53.D is a removable-singularity theorem of the following form:

> A finite-energy \(P\)-critical metric, equivalently a constant-scalar-curvature Bach-flat metric in the scalar-flat bubble case, on \(B^4\setminus\{0\}\), with the local Sobolev and volume properties inherited from orbifold compactness and with trivial link \(S^3\), extends smoothly after a diffeomorphism.

The exact Tian–Viaclovsky theorem and its hypotheses should be identified by theorem number and passage. The attached Anderson source does not provide this upgrade.

---

## 2. Lemma 53.0: the conclusion is right, but the Euler formula needs replacement

The identity
\[
p_*(M)=P(V,g_0)+\sum_kP(N_k)
\]
does follow from Anderson’s case-(I) \(\mathcal R^2\)-identity, provided all bubble-tree vertices are included and neck energy is absent.

The formula
\[
\chi_{\rm orb}(V)=\chi(V)-\sum_j(1-|\Gamma_j|^{-1})
\]
is adequate for an irreducible orbifold with one cone branch at each singular point. It is not adequate for Anderson’s reducible points.

### 2.1 A concrete reducible-point inconsistency

Let two smooth closed components be identified at one point, with both local groups trivial. The underlying wedge has
\[
\chi(V)=\chi(V_1)+\chi(V_2)-1.
\]
The curvature integrals on the two regular branches add as
\[
8\pi^2\bigl(\chi(V_1)+\chi(V_2)\bigr),
\]
not \(8\pi^2\chi(V)\). Thus a reducible trivial-group point requires one contribution for each cone branch, not one contribution for the common topological vertex.

### 2.2 Correct edgewise ledger

Truncate every bulk branch and every ALE bubble at all spherical-space-form ends. For a bulk piece \(B\), define
\[
e(B)=\chi(B^{\rm tr})+\sum_{\text{cone ends }a}\frac1{|\Gamma_a|}.
\]
For an ALE orbifold piece \(N\), possibly with several AE ends and interior orbifold punctures, define
\[
e(N)=
\chi(N^{\rm tr})
-\sum_{\text{AE ends }b}\frac1{|\Gamma_b|}
+\sum_{\text{interior cone ends }c}\frac1{|\Gamma_c|}.
\]
Chern–Gauss–Bonnet gives
\[
\mathcal R^2(B)-P(B)=8\pi^2e(B),\qquad
\mathcal R^2(N)-P(N)=8\pi^2e(N).
\]

Every gluing edge contributes \(+|\Gamma|^{-1}\) on the parent side and \(-|\Gamma|^{-1}\) on the ALE side, so these terms cancel edge by edge. Since every gluing hypersurface \(S^3/\Gamma\) has Euler characteristic zero,
\[
\sum_{\text{all pieces}}\chi(X^{\rm tr})=\chi(M).
\]
Consequently
\[
e(V)+\sum_k e(N_k)=\chi(M),
\]
including reducible vertices, multi-ended bubbles, and all depths of the bubble tree. Subtracting this from Anderson’s \(\mathcal R^2\)-identity proves Lemma 53.0.

Thus the lemma’s result is correct; its current one-level formula should be replaced by this truncated-piece ledger.

---

## 3. Theorem 53.F′: leading term correct, remainder and hypotheses need repair

### 3.1 Exact topological reduction

For a smooth one-ended AE space \(N\) with trivial group at infinity and one-point compactification \(\widehat N\), put
\[
T_+(\widehat N)=2\chi(\widehat N)+3\tau(\widehat N).
\]
The AE Chern–Weil formula is
\[
P(N)
=
4\int_N|W^+|^2+\frac1{12}\int_Ns^2
-8\pi^2\bigl(T_+(\widehat N)-4\bigr).
\]
For \(\widehat M=M\#\widehat N\),
\[
T_+(\widehat M)-T_+(M)=T_+(\widehat N)-4.
\]
Hence
\[
\begin{aligned}
P(\widehat g)-P(g)-P(N)
={}&4\left[
\int_{\widehat M}|W^+_{\widehat g}|^2
-\int_M|W^+_g|^2
-\int_N|W^+_N|^2
\right]\\
&+\frac1{12}\left[
\int_{\widehat M}s_{\widehat g}^2
-\int_Ms_g^2
-\int_Ns_N^2
\right].
\end{aligned}
\]
For \(W_N^+=s_N=0\), this is exactly the reduction used in the note.

### 3.2 Flux and scalar trace

From
\[
P_+\mathcal R P_+=W^++\frac{s}{12}I
\]
one has
\[
\operatorname{tr}(P_+\mathcal R P_+)=\frac{s}{4}.
\]
Therefore
\[
F_s=-\int s^{\rm lin}(\chi h_2)
=4\,\operatorname{tr}\Phi^{++}.
\]
The two cross terms then combine as
\[
-8\lambda^2\langle W_p^+,\Phi^{++}\rangle
-\frac23\lambda^2s_p\operatorname{tr}\Phi^{++}
=
-8\lambda^2\langle\mathbf R_p^+,\Phi^{++}\rangle.
\]
This coefficient is correct.

Cutoff independence also holds, but the reason should include the total-derivative property: if \(\chi_1-\chi_2\) is supported away from the origin, then
\[
\int_{\mathbb R^4}\mathcal R_\delta^{\rm lin}\bigl((\chi_1-\chi_2)h_2\bigr)=0
\]
componentwise. The pointwise equation
\[
P_+\mathcal R_\delta^{\rm lin}(h_2)P_+=0
\]
localizes the flux to the cutoff region but by itself does not prove cutoff independence.

### 3.3 The stated \(O(\lambda^{12/5})\) does not follow for arbitrary \(\delta>0\)

If
\[
g_N=\delta+h_2+O(r^{-2-\delta})
\]
with derivative decay, scaling produces the remainder
\[
O(\lambda^{2+\delta}r^{-2-\delta}).
\]
On the gluing annulus its integrated linear-curvature contribution is generally
\[
O(\lambda^{2+\delta}r_0^{-\delta}).
\]
Together with the Burns-type terms, a natural estimate is
\[
E(\lambda,r_0)
=
O\!\left(
\lambda^2r_0+\lambda^4r_0^{-4}
+\lambda^{2+\delta}r_0^{-\delta}
+\lambda^2r_0^2+\lambda^4|\log\lambda|
\right).
\]
With \(r_0=\lambda^{2/5}\),
\[
E=
O\!\left(
\lambda^{12/5}
+\lambda^{2+3\delta/5}
+\lambda^4|\log\lambda|
\right)
=o(\lambda^2).
\]
The displayed \(O(\lambda^{12/5})\) follows from this estimate when \(\delta\ge 2/3\). For merely \(\delta>0\), the correct general statement is
\[
P(\widehat g_\lambda)
=
P(g)+P(N)
-8\lambda^2\langle\mathbf R_p^+,U\Phi^{++}U^T\rangle
+o(\lambda^2).
\]

### 3.4 Further hypotheses

The theorem should state:

1. \(N\) is smooth and has one AE end. A multi-ended AE space cannot be inserted at a single point without specifying the other attachments.
2. The asymptotic expansion holds with enough derivative estimates to control curvature and cutoff errors.
3. \(\Phi^{++}\) is defined in a fixed normalized AE chart. Invariance under asymptotic gauge changes of order \(r^{-1}\) is not proved in the note. Rotations merely conjugate \(\Phi^{++}\), as already included.
4. The bulk point \(p\) is regular and lies a fixed positive distance from all orbifold points and other gluing regions. Anderson gives \(g_0\in C^\infty\) there, so Theorem F’s \(C^3\) dependence is available.

### 3.5 Rotation maximization

For symmetric \(3\times3\) matrices \(A,B\),
\[
\max_{O\in SO(3)}\operatorname{tr}(AOB O^T)
=
\sum_{i=1}^3\lambda_i(A)\lambda_i(B),
\]
with both eigenvalue lists decreasing. Restricting from \(O(3)\) to \(SO(3)\) does not change the maximum because a sign change commuting with a diagonal \(B\) corrects the determinant. The map \(SO(4)\to SO(\Lambda^+)\cong SO(3)\) is onto. Thus the formula for \(\mathfrak r_N(p)\) is correct.

For a scalar-flat self-dual bubble with \(W^-=0\), the entire statement uses \(\mathbf R^-\) and \(\Phi^{--}\). This is the orientation appropriate to \(\mathbb{CP}^2\)-type rather than \(\overline{\mathbb{CP}}^2\)-type bubbling.

---

## 4. Theorem 53.B and Corollary 53.C

### 4.1 Correct movable-tree formulation

The moving argument is valid for a terminal bubble tree with:

- one outer link \(S^3\);
- smooth total compactification \(\widehat T\);
- decomposition
  \[
  M\cong M'\#\widehat T
  \]
  with \(M'\) connected;
- an outer asymptotic model satisfying the repaired Theorem 53.F′.

Then the connected-sum disk can be moved to any regular point of \(M'\), and an orientation-preserving frame can be changed arbitrarily. Reassemble all other pieces first, fix a small \(\lambda\), and make all remaining gluing errors \(o(\lambda^2)\). If
\[
\mathfrak r_N(p)>0,
\]
the resulting metric has \(P<p_*(M)\), which is impossible. Thus
\[
\mathfrak r_N(p)\le0.
\]

A two-ended Schwarzschild-type bubble is not a one-point connected summand. It is a bridge between two vertices of the gluing graph. Such a bridge may be moved by relocating both attachments, but it cannot be transferred to one arbitrary point by the argument currently written. This supplies a concrete topology where the present formulation is too broad.

For a genuine tree with deeper orbifold vertices, Theorem F′ applies directly only to the smooth outer model. If the outer model has interior orbifold points, the deeper pieces must first be reinserted at scales whose total error is \(o(\lambda^2)\).

### 4.2 Rank-one flux must have positive coefficient

“Rank-one flux” is insufficient. One needs
\[
\Phi^{++}=c\,vv^T,\qquad c>0.
\]
Then
\[
\mathfrak r_N(p)=c\,\lambda_{\max}(\mathbf R_p^+),
\]
and \(\mathfrak r_N\le0\) implies \(\mathbf R^+\le0\).

Without \(c>0\), the implication reverses. For example, if \(\Phi=-vv^T\), then
\[
\max_U\langle A,U\Phi U^T\rangle=-\lambda_{\min}(A).
\]
The inequality \(\max_U\le0\) then says \(A\ge0\), not \(A\le0\). The topology \(\widehat N\cong\overline{\mathbb{CP}}^2\) and rank one alone do not establish the sign of \(c\) from the supplied material.

Burns has \(c=\pi^2>0\), so the Burns conclusion is valid.

### 4.3 Corollary 53.C, items 1–3

Assuming \(\mathbf R^+\le0\), these calculations are correct.

The trace equation for \(P\)-critical metrics is
\[
\operatorname{tr}\nabla P=-\frac12\Delta s.
\]
On each compact orbifold branch, \(s\) extends weakly across isolated points and is constant. Since
\[
\operatorname{tr}\mathbf R^+=\frac{s}{4},
\]
one obtains \(s\le0\).

If \(s=0\), then \(W^+\le0\) and \(\operatorname{tr}W^+=0\), hence \(W^+=0\).

If \(s<0\), let \(a=|s|/12\). The eigenvalues \(w_i\) of \(W^+\) satisfy \(w_i\le a\) and \(\sum w_i=0\). Therefore
\[
|W^+|^2=\sum_iw_i^2\le6a^2=\frac{s^2}{24},
\]
with equality precisely for
\[
(w_1,w_2,w_3)=(a,a,-2a).
\]
Using
\[
P=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2T_+^{\rm orb}
\]
gives
\[
P\le\frac14\int s^2-8\pi^2T_+^{\rm orb}.
\]

### 4.4 Item 4 and the complex-hyperbolic cell

For any one-ended AE \(N\) with \(\widehat N\cong\overline{\mathbb{CP}}^2\),
\[
T_+(\widehat N)=3,
\]
so
\[
P(N)=4\int_N|W^+|^2+\frac1{12}\int_Ns^2+8\pi^2\ge8\pi^2.
\]
Thus the cost comparison used in item 4 is correct without needing the broader Betti-number formula.

The replacement argument is valid under three explicit assumptions:

1. the bubbling topology is the movable standard \(\overline{\mathbb{CP}}^2\) summand;
2. the complex-hyperbolic cell has exactly matching outer collar data;
3. its relative cost is
   \[
   8\pi^2\left(1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2)\right)<8\pi^2
   \]
   for sufficiently small \(\epsilon\).

The analytic cell theorem itself is only quoted in the supplied Step-53 note; its construction and certified error estimate are not among the attached artifacts. Subject to that theorem, item 4 follows. It applies to a regular CH ball disjoint from every other gluing region.

---

## 5. Theorem 53.D: attainment transfer

Let \(V_a\) denote the smooth closed completion of each regular branch of the reducible bulk after adding its trivial-link punctures. Assume:

- each trivial-link puncture is smoothly removable;
- Anderson’s case-(I) energy identity holds;
- every ALE end can be reassembled with vanishing \(P\)-error;
- all vertices and ends of the bubble graph are included in the energy sum.

Then
\[
p_*(M)=\sum_aP(g_0|_{V_a})+\sum_kP(N_k).
\]
Replacing \(g_0|_{V_a}\) by arbitrary smooth metrics \(h_a\), while leaving the bubble graph fixed, gives
\[
p_*(M)\le\sum_aP(h_a)+\sum_kP(N_k).
\]
Taking independent infima over the \(h_a\),
\[
\sum_aP(g_0|_{V_a})\le\sum_ap_*(V_a).
\]
The reverse inequality holds termwise, so
\[
P(g_0|_{V_a})=p_*(V_a)
\]
for every \(a\).

This remains valid when two-ended AE necks connect distinct bulk components or create cycles. Such pieces are retained as fixed vertices of the reassembly graph; only the closed bulk metrics are replaced.

The final “if and only if” sentence needs a definitional clarification. What is established is:

- a trivial case-(I) configuration \((M,g)\) gives a smooth minimizer;
- any smooth minimizer itself defines a trivial energy-equality ideal configuration.

It is not established that the particular configurations produced by Anderson’s \(\varepsilon\)-perturbation become trivial whenever some unrelated smooth minimizer exists. Anderson explicitly notes after Remark 4.12 that approximation of every actual minimizer by perturbed minimizers is not known. A nontrivial ideal configuration may also coexist with a smooth minimizer.

---

## 6. Lemma 53.Y and Theorem 53.E

### 6.1 Yamabe positivity of AE compactifications

A corrected statement is:

> Let \((N,g)\) be smooth, complete, scalar-flat, with finitely many AE ends of trivial group. Assume derivative decay of order \(\tau>1\) at every end. Compactify every end by one point. Then the resulting smooth compact manifold admits a conformal class with positive Yamabe constant.

Choose a positive function \(u\) satisfying \(u\sim |y|^{-2}\) at every added point and define
\[
g=u^2\widehat g.
\]
Conformal covariance gives
\[
L_{\widehat g}u=0
\]
away from the added points, while distributionally
\[
L_{\widehat g}u=\sum_j c_j\delta_{q_j},\qquad c_j>0.
\]
For a standard AE end, \(c_j=24\pi^2\).

If \(\phi>0\) is the first eigenfunction and \(\lambda_1\le0\), then
\[
\sum_jc_j\phi(q_j)
=
\langle L_{\widehat g}u,\phi\rangle
=
\lambda_1\int u\phi\le0,
\]
whereas the left side is positive. Hence \(\lambda_1>0\).

The decay \(\tau>1\) gives a compactified metric with \(C^{1,\alpha}\) regularity and \(W^{2,q}\) regularity for some \(q>4\). Smooth approximation preserves positivity of the first conformal-Laplacian eigenvalue. The Yamabe conclusion is therefore correct.

For a general orbifold end, the same argument gives an orbifold compactification and coefficients scaled by \(|\Gamma|^{-1}\); Theorem 53.E avoids this by requiring all links to be ordinary \(S^3\).

### 6.2 Decay is an additional hypothesis

Anderson’s theorem does not itself provide order \(\tau>1\) for every scalar-flat Bach-flat ALE bubble. The attached note reports:

- ASD scalar-flat and harmonic-curvature ALE metrics admit orders arbitrarily close to \(2\);
- the general Bach-flat scalar-flat theorem initially provides only order \(0\).

Thus Theorem 53.E is valid with its explicit \(\tau>1\) assumption, but this property is not yet inherited automatically by every Anderson bubble from the cited source. A precise later decay theorem would be needed to remove that assumption.

### 6.3 Connected-sum Yamabe calculation

When all links are \(S^3\), the reassembly graph gives
\[
M\cong
\#_a V_a
\#\bigl(\#_k\widehat N_k\bigr)
\#\,r(S^1\times S^3),
\]
where \(r\) is the first Betti number of the gluing graph. Every \(\widehat N_k\) has positive Yamabe invariant by Lemma 53.Y, and \(S^1\times S^3\) also has positive Yamabe invariant.

Repeated Kobayashi inequalities in dimension four give
\[
Y(M)\ge
-\left(\sum_{a:\,Y(V_a)<0}|Y(V_a)|^2\right)^{1/2}.
\]
Therefore, if \(Y(M)<0\),
\[
Y(M)^2\le\sum_{a:\,Y(V_a)<0}Y(V_a)^2,
\]
and at least one bulk component has \(Y(V_a)<0\). Items 1 and 2 of Theorem 53.E follow.

A scalar-flat metric would itself provide a conformal class with Yamabe constant zero, so a manifold with \(Y<0\) cannot carry such a metric.

### 6.4 Einstein versus non-Bach-flat alternatives

On each such \(V_a\), Theorem 53.D gives a smooth global minimizer of \(P\). It has constant \(s\neq0\).

The algebra behind item 3 is:
\[
P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi.
\]
If the metric is both \(P\)-critical and Bach-flat, the Weyl variation vanishes. For constant \(s\), the remaining scalar-square variation is proportional to
\[
s\,\operatorname{Ric}^{\circ}.
\]
Since \(s\neq0\), this forces \(\operatorname{Ric}^{\circ}=0\), hence the metric is Einstein. Therefore, if \(V_a\) admits no Einstein metric, its global \(P\)-minimizer is not Bach-flat.

If \(V_a\) does admit an Einstein metric, then \(p_*(V_a)=0\). Since \(g_0|_{V_a}\) attains that infimum,
\[
P(g_0|_{V_a})=0,
\]
so it is Einstein. Items 3–4 are mathematically consistent.

---

## Corrected theorem package

The central results can be retained in the following form:

1. **Anderson entrance.** Theorem 4.10 for \(\mathcal R^2\), together with \(\mathcal R^2=8\pi^2\chi+P\), supplies a case-(I) ideal minimizer with full bubble energy identity and compactly supported \(P\)-minimality.

2. **Euler telescope.** Use the truncated-piece, edgewise \(1/|\Gamma|\) ledger rather than a single orbifold Euler formula at reducible points.

3. **Half-flat response.**
   \[
   P(\widehat g_\lambda)
   =
   P(g)+P(N)
   -8\lambda^2\langle\mathbf R_p^+,U\Phi^{++}U^T\rangle
   +o(\lambda^2).
   \]
   The stronger \(O(\lambda^{12/5})\) requires at least \(\delta\ge2/3\) under the displayed estimates.

4. **Bubble exclusion.** It applies to a movable terminal one-ended \(S^3\)-linked tree. For \(\Phi=c\,vv^T\) with \(c>0\), it gives \(\mathbf R^+\le0\). The self-dual orientation uses \(\mathbf R^-\).

5. **Attainment transfer.** It holds for smooth removable bulk completions and arbitrary fixed bubble graphs, including two-ended necks.

6. **Yamabe transfer.** It holds when every resolved ALE piece is smooth, scalar-flat, and has end decay \(\tau>1\); Kobayashi’s quantitative inequality is used with the correct sign and exponent.

The remaining source identifications of greatest mathematical importance are the exact trivial-group removability theorem, a \(\tau>1\) decay theorem for general scalar-flat Bach-flat ALE bubbles, the detailed general-critical-metric neck-energy identity underlying Anderson’s (4.43), and the complete CH-cell theorem with its matching collar and certified defect-energy expansion.