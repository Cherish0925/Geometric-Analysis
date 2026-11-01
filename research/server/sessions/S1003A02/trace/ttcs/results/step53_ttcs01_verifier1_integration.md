# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 53,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step53_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step53_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md for the four-manifold Einstein-gap problem (P(g)=int|Ric°|^2, p_*(M)=inf P). Check, as a geometric analyst: (1) whether Anderson's Theorem 4.10 (Asian J Math 2006, Knowledge object attached; see Thm 4.1, Cor 4.4, Lemma 4.5, Prop 4.6, (4.32)-(4.33), Cor 4.8, Thm 4.10 proof, Remark 4.12, (4.65)) really gives, for the functional Z^2=P on unit-volume metrics, case (I) energy equality and local minimality, and which steps of his proof are sketchy (local minimality of weak limits, no-neck equality, removability at Gamma=e points); (2) Lemma 53.0 telescoping of orbifold Euler characteristics converting the R^2 energy equality into p_*(M)=P(V,g0)+sum P(N_k), including bubble trees; (3) Theorem 53.F' generalizing Theorem F (attached step20 note) from Burns to ASD scalar-flat AE bubbles with homogeneous r^{-2} leading term and chiral flux Phi^{++}(N), including the topological reduction P(hat g)-P(g)-P(N)=4 Delta W^+ + Delta S/12 and the von Neumann rotation maximization; (4) Theorem 53.B (moving a Gamma=e bubble tree to any point/frame preserves the diffeomorphism type of M; energy equality turns positive first-order interaction into a competitor below p_*), and Corollary 53.C items 1-4, especially item 4 using the analytic CH cell; (5) Theorem 53.D attainment transfer (each bulk component attains p_*(V_a)), including the reducible-orbifold/multi-component case and two-ended necks; (6) Lemma 53.Y (Green-function argument that one-point compactifications of scalar-flat AE ends of order tau>1 have positive Yamabe invariant) and Theorem 53.E using Kobayashi's connected-sum inequalities. Give corrected statements where needed, counterexamples where a claim fails, and identify any hidden hypothesis (e.g. orientation of bubbles: CP^2-type bubbles couple to R^-, decay order of critical ALE ends, whether the bulk metric g0 is smooth enough for Theorem F's C^3 constant, whether p is required to be away from orbifold points). Do not invent literature; name precise knowledge requests if needed.

## Integrated Scientific Memo

# Verification memo: Step 53

**The Anderson entrance and attainment-transfer mechanism are valid when formulated with the necessary regularity and reassembly hypotheses.** The main corrections are:

- Euler bookkeeping must count **cone branches**, not merely singular vertices, at reducible points.
- Bubble relocation requires a **one-attachment connected-sum tree**, not an arbitrary multi-ended bubble.
- A rank-one flux gives \(\mathbf R^+\le0\) only when its nonzero eigenvalue is positive.
- Smooth removability, quantitative asymptotic expansions, and the CH-cell theorem are additional inputs, not consequences explicitly supplied by Anderson’s Theorem 4.10.
- The claimed logarithmic interaction for homogeneous \(r^{-2}\) non-ASD tails is incorrect.
- Attainment is equivalent to existence of a trivial **generalized configuration**, but not demonstrably to a trivial limit produced by Anderson’s particular perturbation procedure.

Below, source statements are distinguished from arguments that can be supplied independently.

## 1. Anderson’s theorem: what it states, and what its proof establishes explicitly

### Functional and normalization

The identification is exact:
\[
\mathcal Z_\varepsilon^{2p}
=P+\varepsilon\int(1+|\operatorname{Ric}|^2)^p .
\]
Anderson’s (3.3), in the session’s curvature-operator convention, gives
\[
\mathcal R^2(g)=\mathcal K(g)=8\pi^2\chi(M)+P(g).
\]
Thus Theorem 4.10 for \(\mathcal R^2\) applies to minimizing \(P\) on unit-volume metrics.

**The source explicitly states both**
\[
\mathcal K(g_0)+\sum_k\mathcal K(N_k)
=\inf_{\mathbb M_1}\mathcal K
\tag{1}
\]
in case (I), and minimality of \(g_0\) among compact perturbations. The latter transfers to \(P\): the integral of the Euler-form variation vanishes for a compactly supported metric variation. This is stronger than mere criticality.

A qualification to §1 of Step 53: an individual weak pair \((\Omega_\varepsilon,g_\varepsilon)\) need not have \(P(g_\varepsilon)=p_*(M)+o(1)\). Its regular part can omit concentrated or collapsed energy. The entrance is correctly justified at the level of the minimizing sequences and idealized configurations in Theorem 4.10.

### Proof dependencies and gaps

1. **Local minimality of the weak limit.** Corollary 4.4 supplies weak \(W^{2,2p}\) convergence and a lower-semicontinuity inequality, then treats the limit as a weak minimizer. The competitor-transfer argument is not written. One needs a local replacement argument, including control of interpolation energy on a transition annulus. Uniform convexity after fixing harmonic gauge can help, but does not by itself justify the transfer. Global strong convergence is not necessarily required; suitable local energy convergence or an annular replacement lemma suffices.

2. **Regularity in Proposition 4.6 is not a complete proof as printed.** In particular, the inference that regularity of
   \(\Delta\omega+2\phi\) implies regularity of its two summands because they are “linearly independent” is invalid: cancellation can occur between linearly independent nonsmooth functions. The coupled system requires an actual elliptic estimate, not that inference.

3. **Uniformity as \(\varepsilon\to0\) needs justification.** Theorem 4.10 uses Proposition 4.6 uniformly, including after rescaling in (4.49). Under \(\hat g=\ell^{-2}g\), the perturbation becomes
   \[
   \varepsilon\ell^{4-4p}
   \int(\ell^4+|\operatorname{Ric}_{\hat g}|^2)^p\,dV_{\hat g}.
   \]
   Its effective coefficient need not remain small. This does **not** disprove the theorem—uniform ellipticity estimates may be obtainable—but the assertion of uniform \(C^k\) control is not established merely by citing the fixed-\(\varepsilon\) bootstrap. A scale-uniform regularity theorem for (4.33) is the precise missing estimate.

4. **Case-(I) energy equality.** Anderson explicitly states (1), but proves it by reference to [8], [9], and [11], without displaying the neck-energy argument for the perturbed sequence and all tree levels. Those cited papers are listed in the supplied source; their relevant proofs are not supplied here. Remark 4.12 leaves equality in case (II), including collapsed-region contributions, conjectural. Case-(I) equality must not be extended to case (II).

5. **Removability.** Theorem 4.10 asserts only \(C^0\) extension across singularities, including \(\Gamma=e\). It does not assert smooth extension in uniformizing charts. That upgrade is an additional removable-singularity theorem.

Accordingly, Step 53 may quote Theorem 4.10 **as a published theorem**, but should not describe its printed proof as closing these analytic details. Local minimality is not needed for the downstream competitor arguments once energy equality and smooth reassembly are available.

## 2. Lemma 53.0: correct result, incorrect reducible-point formula

For an irreducible orbifold point the usual defect formula is appropriate. For a reducible vertex \(q\) with cone branches \(C(S^3/\Gamma_{q,j})\), the effective Euler number is instead
\[
e(V)=\chi(V)-\sum_q\left(1-\sum_j|\Gamma_{q,j}|^{-1}\right).
\tag{2}
\]
For example, two smooth closed manifolds identified at a point have
\[
\chi(V)=\chi(V_1)+\chi(V_2)-1,
\qquad e(V)=\chi(V_1)+\chi(V_2).
\]
The formula in Step 53 would miss the correction when both groups are trivial.

The clean proof uses **truncated pieces**. For a bulk piece \(B\),
\[
e(B)=\chi(B^{\rm tr})
+\sum_{\text{cone boundaries}}|\Gamma|^{-1}.
\]
For an ALE orbifold piece \(N\), allowing several ends and reducible interior punctures,
\[
e(N)=\chi(N^{\rm tr})
-\sum_{\text{infinity boundaries}}|\Gamma|^{-1}
+\sum_{\text{interior cone boundaries}}|\Gamma|^{-1}.
\]
The corresponding Chern–Gauss–Bonnet formula is
\[
\mathcal K(X)-P(X)=8\pi^2e(X).
\tag{3}
\]

Every internal gluing edge cancels one positive and one negative \(1/|\Gamma|\) term. Every gluing hypersurface has Euler characteristic zero, so the Euler characteristics of the truncated pieces sum to \(\chi(M)\). Hence
\[
e(V)+\sum_{\text{all tree vertices}}e(N_k)=\chi(M).
\]
Subtracting (3) from (1) proves
\[
\boxed{p_*(M)=P(V,g_0)+\sum_kP(N_k).}
\tag{4}
\]
This handles all tree depths, reducible vertices, and multi-ended necks.

A useful consistency check is Schwarzschild: its underlying manifold is \(S^3\times\mathbb R\), with \(\chi=0\), two AE ends, and \(W=s=0\). Thus \(e=-2\), and (3) together with \(\mathcal K=P/2\) gives
\[
P=32\pi^2.
\]

### Independent repair of energy equality by reassembly

When smooth reassembly is justified, case-(I) equality also follows without a separate quantitative no-neck proof:
\[
P(V)+\sum P(N_k)\le p_*(M)
\]
by convergence on disjoint compact regions at separated scales, while reassembly on the same smooth \(M\) gives the reverse inequality.

This is a genuine alternative argument, but requires:

- the diffeomorphism-level decomposition;
- smooth removable bulk germs;
- sufficiently controlled cone convergence at every end;
- vanishing interpolation energy.

It is not an unconditional replacement for Anderson’s analytic arguments.

The positive-rate hypothesis in Lemma 53.R is sufficient, with the displayed estimate correct. It can be weakened to derivative-controlled cone convergence:
\[
g_N-\delta=o(1),\quad r\,\partial g_N=o(1),\quad r^2\partial^2g_N=o(1)
\]
on dyadic annuli. Cutoff curvature is then \(o(r^{-2})\), giving \(o(1)\) annular energy. A bare assertion “ALE of order zero” is insufficient unless its derivative meaning is specified.

## 3. Theorem 53.F′: coefficient verified; the stronger remainder can be repaired

Assume \(N\) is smooth, complete, **one-ended**, AE, and
\[
W_N^+=s_N=0,\qquad
g_N=\delta+h_2+k,\qquad
\partial^jk=O(r^{-2-\delta-j}),\quad j\le2,
\]
with \(\delta>0\) and \(h_2\) homogeneous of degree \(-2\). Fix the AE chart and an orientation-preserving frame. The bulk point must be regular, with a smooth neighborhood disjoint from other gluing regions.

### Topological reduction

Writing \(T_+=2\chi+3\tau\), the closed and one-ended AE formulas give
\[
P(g)=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2T_+(V),
\]
\[
P(N)=4\int_N|W_N^+|^2+\frac1{12}\int_Ns_N^2
-8\pi^2\bigl(T_+(\widehat N)-4\bigr).
\]
Since connected sum subtracts \(4\) from \(T_+\),
\[
\begin{aligned}
P(\hat g)-P(g)-P(N)
={}&4\left(\int|W_{\hat g}^+|^2-\int|W_g^+|^2-\int_N|W_N^+|^2\right)\\
&+\frac1{12}\left(\int s_{\hat g}^2-\int s_g^2-\int_Ns_N^2\right).
\end{aligned}
\tag{5}
\]
For the stated ASD scalar-flat bubble, the bubble terms vanish. This verifies the reduction.

### Flux and interaction

The degree \(-4\) part of \(W_N^+=s_N=0\) yields
\[
P_+\mathcal R_\delta^{\rm lin}(h_2)P_+=0.
\]
Cutoff independence follows additionally from the constant-coefficient, second-derivative structure of \(\mathcal R^{\rm lin}\): differences of cutoffs produce compactly supported tensors away from the origin whose linear-curvature integrals vanish.

Because \(\operatorname{tr}\mathbf R^+=s/4\),
\[
F_s=4\operatorname{tr}\Phi^{++}.
\]
The annular cross terms therefore combine to
\[
-8\lambda^2\langle W_p^+,U\Phi^{++}U^T\rangle
-\frac23\lambda^2s_p\operatorname{tr}\Phi^{++}
=-8\lambda^2\langle\mathbf R_p^+,U\Phi^{++}U^T\rangle.
\tag{6}
\]

### Resolving the remainder disagreement

A direct absolute estimate of the tail remainder gives
\[
O(\lambda^{2+\delta}r_0^{-\delta}),
\]
which alone would not imply \(O(\lambda^{12/5})\) for small \(\delta\). **That estimate overlooks half-flat cancellation.**

Indeed, putting
\[
A=P_+\mathcal R_\delta^{\rm lin}(\,\cdot\,)P_+,
\]
exact half-flatness gives
\[
A(k)=O(r^{-6}),
\tag{7}
\]
since \(A(h_2)=0\) and all nonlinear curvature/projector corrections are \(O(r^{-6})\). If \(F_k(R)\) is the componentwise boundary flux of \(A(k)\), the decay of \(k\) implies \(F_k(\infty)=0\), while (7) gives
\[
F_k(R)=-\int_{r>R}A(k)\,dx=O(R^{-2}).
\]
Thus the constant-background annular interaction from the remainder is only
\[
O(\lambda^2R^{-2})=O(\lambda^4r_0^{-2}),
\qquad R=r_0/\lambda.
\]
The variation of background curvature across the annulus contributes at most
\[
O(\lambda^{2+\delta}r_0^{1-\delta}).
\]
For \(r_0=\lambda^{2/5}\), this is \(O(\lambda^{12/5+3\delta/5})\). The remaining errors are bounded by
\[
O\!\left(
\lambda^2r_0+\lambda^2r_0^2+
\lambda^4r_0^{-4}+\lambda^4|\log\lambda|
\right).
\]
Consequently the claimed estimate is supportable:
\[
\boxed{
P(\hat g_\lambda)=P(g)+P(N)
-8\lambda^2\langle\mathbf R_p^+,U\Phi^{++}U^T\rangle
+O(\lambda^{12/5}).
}
\tag{8}
\]
Step 53 needs this cancellation argument; “identical to Theorem F” is not enough. The core metric must also be explicitly constructed: extend the bulk quadratic perturbation smoothly over a fixed compact part of \(N\). Its contribution is \(O(\lambda^4)\). No canonical blowdown map is available for general \(N\).

The expansion itself is an additional hypothesis. Decay of every order \(\tau<2\) does **not** establish a homogeneous \(r^{-2}\) leading term.

### Rotation, orientation, and flux sign

The maximization formula is correct:
\[
\max_{U\in SO(4)}
\langle A,U\Phi U^T\rangle
=\sum_{i=1}^3\lambda_i(A)\mu_i(\Phi).
\tag{9}
\]
The action on \(\Lambda^+\) is onto \(SO(3)\); determinant correction does not change a maximizing conjugation.

For \(W_N^-=s_N=0\), use the mirror formula with \(\mathbf R^-\) and \(\Phi^{--}\). Reversed Burns, giving a \(\mathbb{CP}^2\) rather than \(\overline{\mathbb{CP}}^2\) summand, couples to \(\mathbf R^-\).

For rank-one flux, the required condition is
\[
\Phi=c\,vv^T,\qquad c>0.
\tag{10}
\]
Rank one alone is insufficient: \(\Phi=-vv^T\) would give
\(\max_U\langle A,U\Phi U^T\rangle=-\lambda_{\min}(A)\), forcing \(A\ge0\), not \(A\le0\).

There is a natural additional justification of positivity. In the standard ADM normalization in dimension four,
\[
F_s=12\pi^2m_{\rm ADM},\qquad
\operatorname{tr}\Phi^{++}=3\pi^2m_{\rm ADM}.
\]
The positive-mass theorem for smooth complete scalar-flat AE four-manifolds gives positive mass for a nonflat bubble. This is an **additional theorem input**, not established in the attached sources. With it, all nonflat bubbles in (8) have positive flux trace; frame averaging yields
\[
\max_U\langle\mathbf R_p^+,U\Phi U^T\rangle
\ge \frac{s_p}{12}\operatorname{tr}\Phi,
\]
so bubble exclusion implies \(s_p\le0\), even without rank one.

### Non-ASD bubbles: delete the stated logarithmic prediction

For a component \(f\) homogeneous of degree \(-2\),
\[
\int_{1<r<R}\partial_i\partial_jf\,dx=0,
\]
because the boundary flux is radius-independent. Thus every linear-curvature component of its degree \(-4\) tail has zero spherical mean. In particular, the hypothesized nonzero mean of the \(r^{-4}\) Weyl tail cannot occur under the stated homogeneous expansion.

This removes the proposed \(\lambda^2\log(1/\lambda)\) mechanism from that tail. It does **not** prove the proposed general response tensor
\(\Phi-\int_NW_N^+\). Such an integral requires an identified global tensor bundle, and non-ASD core variations themselves contribute at order \(\lambda^2\). A correct general response requires the linearized curvature-energy calculation on the entire bubble. Logarithmic metric terms would be a separate asymptotic regime.

## 4. Theorem 53.B and Corollary 53.C

### Correct relocation statement

Require a resolved bubble tree \(T\) with **one outer boundary \(S^3\)** and
\[
M\cong M'\#\widehat T,\qquad M'\ \text{connected}.
\tag{11}
\]
This is the situation of a tree attached at an irreducible \(\Gamma=e\) point. Orientation-preserving disk/frame changes leave the oriented connected-sum diffeomorphism type unchanged.

The vacated bulk puncture must be smoothly removable. If the outer bubble has interior orbifold points, its descendants must be reinserted before applying the competitor argument; smoothness of the outer bubble, as currently required by F′, cannot simply be ignored.

At any fixed regular bulk point, choose \(\lambda\) first and all other reassembly scales afterward so their error is \(o(\lambda^2)\). Equations (4) and (8) then imply
\[
\boxed{\mathfrak r_N(p)\le0.}
\]
Positive rank-one flux gives \(\mathbf R^+\le0\).

A **two-ended Schwarzschild neck** is a counterexample to the claimed one-point topological description: it joins two attachments. Cutting it can disconnect the remaining configuration. It is not a movable one-point summand by (11). Relocating such a neck requires keeping track of both ends and the gluing graph.

### Corollary C, items 1–3

Assume \(\mathbf R^+\le0\) and smooth orbifold extension on each normalized compact bulk component. Criticality gives
\[
\Delta s=0,
\]
so \(s\) is constant there. Then:

- \(s\le0\), since \(\operatorname{tr}\mathbf R^+=s/4\).
- If \(s=0\), trace-free \(W^+\le0\) implies \(W^+=0\).
- If \(s<0\), setting \(a=|s|/12\), the Weyl eigenvalues satisfy \(w_i\le a\), \(\sum w_i=0\). Their squared norm is at most \(6a^2=s^2/24\), attained exactly at permutations of \((a,a,-2a)\). Hence
  \[
  P(V_a)\le\frac14\int_{V_a}s^2-8\pi^2T_+^{\rm orb}(V_a),
  \]
  with \(T_+^{\rm orb}\) understood through the appropriate orbifold Chern–Weil ledger.

“Kähler spectrum” denotes the algebraic spectrum here; its occurrence at a point does not prove Kähler geometry.

Also correct the dimensional statement: for negative Kähler–Einstein curvature,
\[
\mathbf R^+=\operatorname{diag}(s/4,0,0).
\]
Its kernel is two-dimensional, and its **unit kernel directions form \(S^1\), not a 2-sphere**.

### Item 4: valid conditional replacement, not verified analytic input

For a smooth one-ended AE space with
\(\widehat N\cong\overline{\mathbb{CP}}^2\),
\[
P(N)=4\int|W_N^+|^2+\frac1{12}\int s_N^2+8\pi^2\ge8\pi^2.
\tag{12}
\]
The same lower bound applies to a resolved one-attachment tree whose total compactification is \(\overline{\mathbb{CP}}^2\), by telescoping the characteristic identities.

Thus item 4 follows **if** the quoted CH cell:

- has this oriented topology;
- matches the CH metric exactly on its outer collar;
- fits inside an available regular CH ball;
- has relative \(P\)-cost strictly below \(8\pi^2\).

The analytic cell theorem is not attached. Its allowable collar radius matters: a theorem only for sufficiently large normalized CH balls does not establish replacement in an arbitrary small CH open set.

The broader formula
\[
P_N=4\int|W^+|^2+\tfrac1{12}\int s^2+8\pi^2b_2+32\pi^2b_1
\]
also needs negative-definite intersection form. In general its topological term is
\[
8\pi^2(b_2^- -5b_2^+ +4b_1).
\]
For (12), the compactification identity avoids this issue entirely.

## 5. Theorem 53.D: attainment transfer survives reducibility and two-ended necks

Use the **normalized bulk components** \(V_a\): complete each regular branch separately, rather than treating the reducible wedge itself as a smooth manifold.

Assume all cone punctures have trivial group and are smoothly removable, and the entire fixed bubble graph admits vanishing-error reassembly. Then
\[
p_*(M)=\sum_aP(g_a)+\sum_kP(N_k).
\]
Replacing the bulk metrics independently by arbitrary smooth \(h_a\), while retaining all bubble pieces and attachment edges, gives
\[
p_*(M)\le\sum_aP(h_a)+\sum_kP(N_k).
\]
Taking infima and comparing with the equality yields
\[
\sum_aP(g_a)\le\sum_ap_*(V_a).
\]
The reverse inequality holds termwise. Therefore
\[
\boxed{P(g_a)=p_*(V_a)\quad\text{for every }a.}
\]

This proof includes multi-component bulk, bridge necks, and graph cycles. Volume allocation is irrelevant because \(P\) is scale invariant.

Correct the final equivalence to:

> \(p_*(M)\) is smoothly attained iff there exists a trivial energy-equality generalized configuration on \(M\).

The forward implication is immediate by regarding the smooth minimizer itself as that configuration. It is **not known from this source** that an attaining manifold must have a trivial limit selected by Anderson’s perturbation process. Anderson explicitly discusses that distinction following Remark 4.12.

## 6. Lemma 53.Y and Theorem 53.E

### Yamabe positivity

The original lemma is correct with smoothness, finitely many ends, and derivative decay made explicit. Compactify **each end separately**.

Choose \(u>0\), exactly \(u=|y|^{-2}\) near every compactification point, and set \(\hat g=u^{-2}g\). Then
\[
L_{\hat g}u=0\quad\text{off the added points},
\qquad
L_{\hat g}u=24\pi^2\sum_j\delta_{q_j}
\tag{13}
\]
distributionally. The metric-dependent flux errors tend to zero.

Decay of order \(\tau\) gives
\[
\hat g-\delta=O(|y|^\tau),\qquad
\partial^2\hat g=O(|y|^{\tau-2}).
\]
For \(\tau>1\), one obtains \(C^{1,\alpha}\cap W^{2,q}\) for some \(q>4\); write \(\alpha<\min\{1,\tau-1\}\), rather than an unrestricted \(C^{1,\tau-1}\) exponent.

In fact, **\(\tau>0\) suffices with the same derivative bounds**: choose
\[
2<q<\frac4{2-\tau}
\]
when \(0<\tau<2\). Then \(\hat g\in W^{2,q}\), its scalar curvature is in \(L^q\), and the positive first eigenfunction \(\phi\) is continuous. Pairing (13) with \(\phi\), justified by punctured-domain integration, gives
\[
24\pi^2\sum_j\phi(q_j)
=\lambda_1\int u\phi\,dV_{\hat g}.
\]
The integral is finite, so \(\lambda_1>0\). Smooth approximation preserves this positivity: metric coefficients converge uniformly and scalar-curvature terms converge in \(L^q\), \(q>2\). Hence
\[
Y(\widehat N)>0.
\]

This argument requires derivative-controlled decay, not just pointwise asymptotic flatness. It also assumes the compactified object is a smooth manifold; unresolved interior orbifold points cannot be silently included.

### Yamabe transfer and the non-Bach-flat alternative

When all links are \(S^3\), the fixed reassembly graph gives
\[
M\cong
\#_aV_a\ \#\ \#_k\widehat N_k\ \#\ b_1(\text{graph})(S^1\times S^3).
\]
The bubble compactifications and graph-loop factors have positive Yamabe invariant. Kobayashi’s dimension-four connected-sum inequalities give
\[
Y(M)\ge
-\left(\sum_{Y(V_a)<0}|Y(V_a)|^2\right)^{1/2}.
\]
Thus \(Y(M)<0\) forces a negative bulk component and
\[
Y(M)^2\le\sum_{Y(V_a)<0}Y(V_a)^2.
\]

The remaining assertions of E follow directly, without the absent “Prop. nonbach.” Such a bulk metric is a smooth global \(P\)-minimizer and cannot be scalar-flat. Its scalar curvature is constant and negative.

Since
\[
P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi,
\]
a metric that is both \(P\)-critical and Bach-flat satisfies \(\nabla\int s^2=0\). At constant scalar curvature,
\[
\nabla\int s^2=-2s\,\operatorname{Ric}^\circ.
\]
As \(s\ne0\), it must be Einstein. Consequently:

- if \(V_a\) admits no Einstein metric, its attained minimizer is non-Bach-flat;
- if \(V_a\) admits an Einstein metric, \(p_*(V_a)=0\), and the attained minimizer is Einstein.

Anderson alone does not supply the required decay for all general scalar-flat Bach-flat bubbles. Nor do the attached materials establish universal homogeneous \(r^{-2}\) expansions. These remain separate hypotheses.

## Precise missing knowledge

The smallest source package needed to close the remaining dependencies is:

1. **Removability:** the exact theorem covering finite-energy \(P\)-critical metrics at punctures with \(S^3\) link, including its Sobolev, volume, and initial-regularity assumptions.
2. **Anderson regularity:** a valid coupled elliptic replacement for Proposition 4.6 and estimates uniform under the rescaling of (4.33).
3. **End asymptotics:** derivative meaning of order-zero ALE, improved decay for general scalar-flat Bach-flat ends, and conditions giving homogeneous \(r^{-2}\) expansions without logarithms.
4. **CH cell:** the full analytic construction, oriented topology, exact matching collar, relative-energy expansion, and permissible normalized collar radii.
5. **External sign inequalities:** the precise positive-mass theorem supporting flux positivity and Kobayashi’s mixed-sign connected-sum statement.

With these distinctions, the Euler telescope, first-order half-flat response, one-attachment bubble exclusion, and smooth bulk attainment transfer form a coherent theorem package. The unresolved issues are analytic hypotheses and the general bubble response—not the algebraic characteristic identities or the variational contradiction mechanism.