# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/Geography-of-4-manifolds-with-positive-scalar-curvature--ea1844e3f622--6263e9f8807e/object.md"
  ]
}
```

## Task

Scientist-reader check of Step-88 integration and the oldest package §§2–12. Read the actual theorem package, the Step-87 verifier memos, the current hypothesis ledger, and the Step-54 source note. Identify only mathematically consequential remaining errors or scope mismatches, especially: (i) Theorem 87.O and whether its signature and connected-sum lower construction justify the exact orbifold supremum; (ii) the negative-Yamabe exclusion; (iii) the Γ-vertex replacement for Lemma 54.3, including factorization of the classifying map and multi-ended cap compactification; (iv) stale P_* versus human α language, retired status statements, and historical route headings in §§2–12. Give exact replacement prose/equations for any issue and say when current text is sound. Do not propose new computations or weaken the active open problem.

## Output

# Scientific verification memo

## 1. Theorem 87.O is correct for the fixed orbifold \(V_m\)

Let
\[
\mathcal O=S^4/\mathbb Z_2
\]
with its two isolated \(A_1\) points, and let
\[
V_m=X\#m\mathcal O
\]
where the connected sums are taken at regular points. Use the Satake Euler characteristic and the session operator norm
\[
I_\pm=\int |W^\pm|_{\mathrm{op}}^2.
\]

For a compact ball quotient \(X\), with \(A=c_1^2(X)\) and complex orientation,
\[
\chi(X)=\frac A3,\qquad \tau(X)=\frac A9.
\]
Moreover,
\[
\chi_{\mathrm{orb}}(\mathcal O)=1,\qquad \tau_{\mathrm{orb}}(\mathcal O)=0.
\]
Since each smooth-point connected sum subtracts \(2\) from the orbifold Euler characteristic,
\[
\chi_{\mathrm{orb}}(V_m)=\frac A3-m,\qquad
\tau_{\mathrm{orb}}(V_m)=\frac A9.
\]

The \(A_1\) link has zero signature \(\eta\)-term. Hence every orbifold metric on \(V_m\) satisfies
\[
I_+-I_-=12\pi^2\tau_{\mathrm{orb}}(V_m)
=\frac{4\pi^2A}{3},
\]
and therefore
\[
I_++I_-\ge \frac{4\pi^2A}{3}.
\]
It follows that
\[
d_{\mathrm{orb}}(g)
=8\pi^2\chi_{\mathrm{orb}}(V_m)-I_+-I_-
\le 4\pi^2\left(\frac A3-2m\right).
\tag{1}
\]

The reverse inequality follows from the conformal connected-sum construction. The complex-hyperbolic metric has
\[
I_-=0,\qquad I_+=\frac{4\pi^2A}{3},
\]
while the round metric on \(\mathcal O\) is conformally flat. Gluing at regular points gives orbifold metrics with
\[
I_++I_-\longrightarrow \frac{4\pi^2A}{3}.
\]
Equivalently, the deficit connected-sum law gives
\[
d_{*,\mathrm{orb}}(X\#\mathcal O)
\ge d_*(X)+d_{*,\mathrm{orb}}(\mathcal O)-16\pi^2
=d_*(X)-8\pi^2,
\]
and iteration yields the right side of (1). Thus
\[
\boxed{
d_{*,\mathrm{orb}}(V_m)
=4\pi^2\left(\frac A3-2m\right).
}
\]

The current §22.6(6) is mathematically sound. Its quantifiers are essential: this is the exact supremum over orbifold metrics on the fixed orbifold \(V_m\). It is not an upper estimate for all smooth metrics on the resolution
\[
X\#2m\overline{\mathbb{CP}}^2.
\]

### Resolution ledger

For a Ricci-flat ALE filler \(N\) with group \(\Gamma\),
\[
\int_N|W|^2
=8\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right),
\]
which exactly matches the Euler increment under replacement of the orbifold point. Hence standard derivative-controlled ALE gluing gives
\[
d(M,g_\varepsilon)\longrightarrow d_{\mathrm{orb}}(V,g).
\]
For Eguchi–Hanson,
\[
\chi(N)=2,\qquad |\Gamma|=2,\qquad \int_N|W|^2=12\pi^2.
\]
Resolving the \(2m\) singular points changes
\[
\chi\ \text{by }3m,\qquad
\mathcal W\ \text{by }24\pi^2m
=8\pi^2(3m),
\]
so the deficit is conserved.

For an Einstein orbifold metric,
\[
d=\frac1{24}\int s^2,\qquad
R=\int|\operatorname{Ric}|^2=6d.
\]
Therefore this orbifold type can be Einstein only if
\[
2m<\frac A3.
\]
The strict inequality and the interpretation in the hard range are correct in the package.

A useful exact sentence for §22.6 is:

> Here \(d_{*,\mathrm{orb}}\) is the supremum over orbifold metrics on the fixed Satake orbifold \(V_m\), with connected sums performed at regular points. The matching lower construction uses orbifold conformal connected sum, while the upper estimate uses the orbifold signature formula. Resolution transfers these orbifold competitors to smooth competitors but does not transfer the orbifold upper estimate to all smooth metrics.

---

## 2. The \(\mathcal Y(M)<0\) exclusion is correct with the stated gluing architecture

For
\[
M=X\#k\overline{\mathbb{CP}}^2
\]
with \(X\) minimal of general type,
\[
\mathcal Y(M)=-4\pi\sqrt{2A}.
\]
For every metric \(g\),
\[
Y([g])\ge-\|s_g^-\|_{L^2},
\qquad
\mathcal Y(M)\ge Y([g]).
\]
Consequently,
\[
-4\pi\sqrt{2A}\ge-\|s_g^-\|_{L^2},
\]
and hence
\[
\boxed{\int_M(s_g^-)^2\,d\mu_g\ge32\pi^2A.}
\tag{2}
\]

Suppose a compact Einstein orbifold is resolved or smoothed by the derivative-controlled Ricci-flat ALE or Wahl construction of Lemma 86.S.

* If \(\lambda=0\), scalar curvature is supported only in shrinking transition regions, and the estimates of Lemma 86.S give
  \[
  \int(s^-)^2\longrightarrow0.
  \]
* If \(\lambda>0\), the orbifold exterior has \(s>0\), the fillers have \(s=0\), and again the part with \(s<0\) lies only in the transition regions, with
  \[
  \int(s^-)^2\longrightarrow0.
  \]

Both contradict (2). Thus
\[
\boxed{\lambda<0.}
\]

The current detailed formulations in §§13, 17, and 24 are correct because they restrict this conclusion to orbifolds whose stated resolution or smoothing is the given general-type blow-up. The compressed summary near the beginning would be clearer as:

> Whenever a compact Einstein orbifold admits one of the derivative-controlled Ricci-flat ALE resolutions or Wahl smoothings whose smooth result is \(X\#k\overline{\mathbb{CP}}^2\), its Einstein constant satisfies \(\lambda<0\).

This argument does not concern unrelated orbifolds with the same coarse topological invariants.

---

## 3. The \(\Gamma\)-vertex proof is valid; the Step-54 body still contains the older proof order

Let
\[
\Gamma=\pi_1(X),\qquad M_k=X\#k\overline{\mathbb{CP}}^2,
\]
with \(X\) a non-fake-plane ball quotient. In a trivial-local-group case-(I) decomposition, capping every \(S^3\) link gives a graph of closed pieces. Van Kampen gives
\[
\Gamma\cong
\left(*_v\pi_1(Y_v)\right)*F_{b_1(\mathcal G)}.
\]
Because \(\Gamma\) is torsion-free, one-ended, and freely indecomposable, the graph has no loops, exactly one cap \(Y\) has fundamental group \(\Gamma\), and every other cap is simply connected.

### Classifying-map factorization

Let
\[
c:M_k\longrightarrow X=B\Gamma
\]
be the blowdown/classifying map. It has degree one. The graph decomposition is a connected-sum decomposition
\[
M_k\cong Y\#R,
\]
where \(\pi_1(R)=1\). Let \(q:M_k\to Y\) collapse \(R\) to a point, and choose
\[
f:Y\to B\Gamma
\]
inducing the identified isomorphism on \(\pi_1\). Since maps into \(B\Gamma\) are determined up to homotopy by their induced \(\pi_1\)-homomorphisms,
\[
c\simeq f\circ q.
\]
Therefore
\[
f_*[Y]=c_*[M_k]=[X],
\]
so \(f\) has degree one. It follows that
\[
f^*:H^2(X;\mathbb Q)\hookrightarrow H^2(Y;\mathbb Q)
\]
is injective and preserves the intersection pairing:
\[
\langle f^*a\smile f^*b,[Y]\rangle
=\langle a\smile b,[X]\rangle.
\]
Hence
\[
b^+(Y)\ge b^+(X)\ge3.
\tag{3}
\]

### Multi-ended bubble caps

If the \(\Gamma\)-vertex came from an \(e\)-ended bubble \(N\), the relevant cap is
\[
\widehat N=N\cup\{p_1,\ldots,p_e\},
\]
with all ends compactified. Lemma 53.Y applies to this all-end compactification under the derivative-controlled scalar-flat AE hypotheses. Equivalently, the compactified conformal Laplacian has a positive multipole Green function, which gives positive first eigenvalue and hence a PSC metric on \(\widehat N\).

But \(f:\widehat N\to X=B\Gamma\) has degree one, so \(\widehat N\) is essential. Mantione–Torres, Proposition 2, excludes a PSC metric on such a four-manifold with the fundamental group of the closed nonpositively curved manifold \(X\). Therefore the \(\Gamma\)-vertex is a bulk component.

For every bubble cap \(\widehat N_j\), its connected-sum complement contains \(Y\), so by (3) the complement has \(b^+\ge3\). If \(b^+(\widehat N_j)\ge1\), ordinary connected-sum Seiberg–Witten vanishing contradicts the nonzero invariant of \(M_k\). Hence
\[
b^+(\widehat N_j)=0.
\]
The two-orientation charge estimate then gives
\[
\sum_j
\left[4(e_j-1)+4b_1(\widehat N_j)+b_2(\widehat N_j)\right]<k.
\]
At \(k=1\), every term vanishes, so each bubble is one-ended and each cap is a homotopy sphere.

This proof is correct and removes Lemma 54.3 from Theorem 54.A.

### Exact replacement for the old Step-54 proof paragraph

The proof beginning “Step 1: by Lemma 54.2…” should read:

> By free indecomposability of \(\Gamma=\pi_1(X)\), the capped graph decomposition has exactly one vertex \(Y\) carrying \(\Gamma\), all other vertex groups are trivial, and the graph has no loops. The classifying map \(M_k\to X=B\Gamma\) factors, up to homotopy, through the collapse \(M_k\to Y\). Since the classifying map has degree one, the induced map \(Y\to X\) has degree one; therefore \(Q_X\) embeds in \(Q_Y\) and \(b^+(Y)\ge b^+(X)\ge3\). If \(Y\) were the all-end compactification of a bubble, \(\mathrm H_{\rm dec}\) and Lemma 53.Y would give \(Y\) a PSC metric, contrary to Mantione–Torres Proposition 2 because \(Y\) is essential. Thus \(Y\) is bulk. Every bubble complement contains \(Y\), and ordinary connected-sum Seiberg–Witten vanishing therefore forces \(b^+(\widehat N_j)=0\) for every bubble. The two-orientation charge estimate and \(P_*(M)<8\pi^2\) then imply \(e_j=1\), \(b_1(\widehat N_j)=b_2(\widehat N_j)=0\).

The old paragraph in part (iii) transferring Seiberg–Witten invariants through a homotopy sphere should be replaced by:

> The bulk \(V\) is essential, has \(\pi_1(V)=\Gamma\), and admits no PSC metric by Mantione–Torres. Since a smooth \(P\)-critical metric has constant scalar curvature, \(s>0\) is impossible. If \(s=0\), Bourguignon’s theorem makes the metric Ricci-flat; then \(\pi_1(V)\) would be virtually abelian, contrary to \(\Gamma\). Hence \(s<0\). A constant-scalar \(P\)-critical Bach-flat metric is Einstein; otherwise it is a smooth non-Bach-flat global \(P\)-minimizer.

The binding erratum at the top of the Step-54 note and theorem-package §15 already state this corrected order. The body of the Step-54 note should not be read without that erratum.

Lemma 54.3 remains mathematically plausible as a standalone result dependent on standard cylindrical-end monopole compactness. No exact primary citation with precisely its one-sided quantifiers is registered, so the package’s source-dependent status is appropriate. It is not used for ball-quotient hosts.

---

## 4. Remaining stale entries in the Step-58 hypothesis ledger

Several lines in `step58_consolidated_hypothesis_ledger.md` predate the separation of \(P_*\) and the human functional.

### 4.1 Functional notation

The following replacement block is exact:

> Define
> \[
> P_*(M)=\inf_g\int|\operatorname{Ric}^\circ_g|^2\,d\mu_g,
> \qquad
> P_{*,\mathrm{orb}}(V)=\inf_{g\ \mathrm{orbifold}}P(g).
> \]
> All Anderson selection, bubbling, energy identities, and local replacement arguments in this ledger concern \(P_*\). They do not concern the human infimum \(\alpha=\inf\mathscr D\) unless a separate conformal or nonzero-scale argument is stated.

In Theorem 56.A(i), replace
\[
p_*(M)=P(V,g_0)=\alpha_{\rm orb}(V)
\]
by
\[
\boxed{
P_*(M)=P_{*,\mathrm{orb}}(V)=P(V,g_0).
}
\]

For Corollary 56.B, replace the current sentence by:

> An Einstein orbifold with the stated Ricci-flat ALE or Wahl smoothing gives \(P_*(M')=0\). If its Einstein constant is nonzero, Lemma 86.S gives \(\alpha(M')=0\). When \(M'\) is a general-type blow-up, the Yamabe estimate above forces the Einstein constant to be \(<0\).

### 4.2 Theorem 57.Φ is no longer merely formal

The Step-58 ledger’s formal status and open item IV.5 have been superseded by Theorem 59.R. The precise current statement is:

> On a region where \(E_P(g)=0\), the Burns insertion has the rigorous expansion
> \[
> P(\widetilde g_\varepsilon)
> =P(g)+8\pi^2-8\pi^2\varepsilon\mathbf R^+_p(\zeta,\zeta)
> +4\pi^2\Phi(\operatorname{Rm}_p,\zeta,K)\varepsilon^2\log(1/\varepsilon)
> +O(\varepsilon^2).
> \]
> When \(\operatorname{Ric}^\circ_p=0\) and \(\zeta\) is an eigenvector, optimization gives
> \[
> \Phi_{\mathrm{opt}}
> =-\mu_1(\mu_1-s/8)-|T|^2.
> \]
> The \(W^-\) and \(\operatorname{Ric}^\circ\) corrector sectors have been closed. Corollary 59.KE rigorously yields
> \[
> P_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k.
> \]

The old unrestricted rigidity paragraph in §III.C is too strong. Replace it by:

> Under the Anderson and relocation hypotheses, a minimizing bulk carrying Burns-type bubbles satisfies \(\mathbf R^+\le0\). On a kernel direction,
> \[
> |T|^2\le Q_{\mathrm{Ric}}(\operatorname{Ric}^\circ_p).
> \]
> If the bulk is Einstein, the right side vanishes, so at \(\lambda_{\max}(\mathbf R^+)=0\) the other two eigenvalues agree; consequently \(|W^+|^2<s^2/24\) for \(s<0\).

### 4.3 The upper input and Kähler theorem

The ledger’s CH-cell proof of
\[
P_*(M_k)<8\pi^2k
\]
applies directly to ball quotients. For arbitrary minimal general-type surfaces, the current source is Corollary 59.KE with canonical-model and ALE localization. These two settings should not be merged into “every embedded ball.”

The \(b^+(X)\ge3\) assumption in the ledger’s statement of \(K_\infty\) is no longer part of the theorem-package formulation. The fixed-complex Kähler identity and recovery theorem are stated there for the recorded minimal general-type setting.

### 4.4 Proposition 58.O

For spherical or hyperbolic Einstein orbifolds, the final value \(\alpha(M')=0\) is correct because the Einstein constant is nonzero. The old proof, however, establishes only \(P\to0\) until Lemma 86.S is invoked.

Exact replacement:

> Ricci-flat ALE resolution gives \(P_*(M')=0\). Since the compact orbifold Einstein constant is nonzero, Lemma 86.S also gives \(\mathscr D(g_\varepsilon)\to0\), hence \(\alpha(M')=0\). The value \(0\) is attained exactly by an Einstein metric with nonzero Einstein constant. Ozuch’s theorem says that no sequence of Einstein metrics on \(M'\) converges in the Gromov–Hausdorff sense to the stated orbifold when an \(A_1\) point is present.

“Any such Einstein metric is GH-far” should be replaced by the sequence statement above; no quantitative distance is supplied by the cited theorem.

---

## 5. Status of §§2–12

The mathematical statements in §§2–12 are largely consistent with the later corrections:

* §§3.1–3.2 use nonzero-scale Einstein exteriors, so their conclusions \(\alpha=0\) are valid.
* §§3.4, 5.3, and 10 use the Yamabe quotient or Weyl-deficit identity rather than identifying \(P_*\) with \(\alpha\).
* §7 explicitly separates Ricci-flat \(P\)-degenerations from human-defect behavior.
* §§11–12 correctly state that localized CH coercivity does not itself produce an all-metric count of concentration regions.
* The supersession labels in §§3.9–3.10 are clear and mathematically harmless.

Two status passages should be updated.

### O10 paragraph

The sentence saying that O10 “has not advanced since §2.2” conflicts with the Step-47 asymptotic result in §10. A consistent replacement is:

> **O10 current status.** The density-free actual-field theorem remains unresolved. Section 2.2 proves the finite-\(\beta\) alignment theorem. Section 10 additionally shows that any sequence with \(\beta\to\infty\) and \(\kappa_\beta\to0\) must satisfy
> \[
> \chi/p\to\infty,\qquad
> p/V\to\frac{2}{9\pi^2},\qquad
> W^-/V\to\infty.
> \]
> These are necessary asymptotics for an escaping sequence; they do not supply the density-free lower estimate.

### Historical planning headings

Section 9 and the final “highest-value next object” paragraph of §10 are time-indexed research records. Section 11 subsequently proves part of the localized CH object through Theorems 48.L and 48.LY. Exact relabeling would be:

> **Research targets recorded before Steps 48–88.** The ordering in this section is historical. The current theorem status and unresolved mathematical questions are recorded in §§13–24.

and

> **Step-47 localization target and its later realization.** The Riemannian localized estimate was subsequently obtained in Theorem 48.L, with the Yamabe/core form in Theorem 48.LY. The per-core Weyl-volume inequality and unrestricted entry theorem remain unresolved.

No further \(P_*\)-versus-\(\alpha\) interchange was found in §§2–12.

---

## 6. Effect on the central hard range

These corrections leave the central mathematical situation unchanged. For
\[
0<k<A/3,
\]
the package still provides
\[
0\le\alpha\!\left(X\#k\overline{\mathbb{CP}}^2\right)
<\frac{4k}{A+k}<1,
\qquad
P_*<8\pi^2k,
\]
and
\[
P_*=0\iff\alpha=0.
\]
There is still no general positive lower estimate, no zero-infimum construction on a fixed general-type blow-up, and no general decision on Einstein existence in this range. The exact \(S^4/\mathbb Z_2\) calculation adds a real restriction: that orbifold-resolution architecture can occur only with \(k<A/3\), but it remains a possible mechanism precisely inside the unresolved region.