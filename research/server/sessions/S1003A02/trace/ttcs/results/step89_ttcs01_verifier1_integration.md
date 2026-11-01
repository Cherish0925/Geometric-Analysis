# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 89,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step89_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step89_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Scientist-reader check of Step-88 integration and the oldest package §§2–12. Read the actual theorem package, the Step-87 verifier memos, the current hypothesis ledger, and the Step-54 source note. Identify only mathematically consequential remaining errors or scope mismatches, especially: (i) Theorem 87.O and whether its signature and connected-sum lower construction justify the exact orbifold supremum; (ii) the negative-Yamabe exclusion; (iii) the Γ-vertex replacement for Lemma 54.3, including factorization of the classifying map and multi-ended cap compactification; (iv) stale P_* versus human α language, retired status statements, and historical route headings in §§2–12. Give exact replacement prose/equations for any issue and say when current text is sound. Do not propose new computations or weaken the active open problem.

## Integrated Scientific Memo

# Scientist-reader memo

**The Step-88 integration is sound on its three principal mathematical conclusions:** the exact supremum in Theorem 87.O, the negative-Yamabe exclusion within the stated resolution/smoothing architectures, and the Γ-vertex replacement for Lemma 54.3. The remaining consequential problems are stale statements in the Step-54 body and Step-58 ledger, several outdated claims of openness in §§2–12, and one surviving collision between the exceptional-area parameter and the human \(\alpha\).

## 1. Theorem 87.O: the exact supremum is justified

For the **fixed orbifold**
\[
V_m=X\#m(S^4/\mathbb Z_2),
\]
with complex-oriented ball-quotient host \(X\), \(A=c_1^2(X)\), and sums at regular points, the current calculation is correct:
\[
\chi_{\rm orb}(V_m)=\frac A3-m,\qquad \tau(V_m)=\frac A9.
\]
Here \(\chi_{\rm orb}\) is the Satake Euler characteristic. The signature is unchanged by these summands; all \(A_1\)-link signature corrections vanish. Thus every orbifold metric satisfies
\[
I_+-I_-=\frac{4\pi^2A}{3},
\qquad
I_++I_-\ge\frac{4\pi^2A}{3},
\]
and consequently
\[
d_{\rm orb}(g)\le4\pi^2\left(\frac A3-2m\right).
\]

The matching lower construction is legitimate, not merely formal bookkeeping. It changes metrics only in regular-point gluing balls, so the ordinary conformal connected-sum argument applies without modifying the singular charts. The complex-hyperbolic host has \(I_-=0\), while the round quotient summands have zero Weyl curvature. Their connected-sum metrics therefore satisfy
\[
I_++I_-\longrightarrow\frac{4\pi^2A}{3}.
\]
This proves the claimed **supremum**, without asserting attainment:
\[
\boxed{d_{*,\rm orb}(V_m)=4\pi^2(A/3-2m).}
\]

The proof needs no new hypothesis. The following replacement makes its lower side explicit:

> Each regular-point connected sum with \(S^4/\mathbb Z_2\) changes \(\chi_{\rm orb}\) by \(1-2=-1\) and leaves the signature unchanged. Conversely, perform conformal connected sums in regular-point balls disjoint from all singularities. The Kobayashi construction is local to those balls and gives orbifold metrics with
> \[
> I_++I_-\to4\pi^2A/3.
> \]
> Equivalently,
> \[
> d_{*,\rm orb}(V_m)\ge d_*(X)+m\,d_{*,\rm orb}(S^4/\mathbb Z_2)-16\pi^2m
> =4\pi^2(A/3-2m),
> \]
> matching the signature upper bound.

### Resolution and Einstein consequences

The current resolution ledger is also correct. A Ricci-flat ALE filler satisfies
\[
\int_N|W|^2=8\pi^2\left(\chi(N)-|\Gamma|^{-1}\right),
\]
which cancels precisely the Euler increment. For \(2m\) Eguchi–Hanson replacements,
\[
\Delta\chi=3m,\qquad \Delta\mathcal W=24\pi^2m,
\]
and
\[
d(g_\varepsilon)\to d_{\rm orb}(g).
\]

For a **nonzero-scale** Einstein orbifold,
\[
R=6d>0,
\]
so this type requires
\[
2m<A/3.
\]
The package states the nonzero-scale qualification correctly; the strict inequality must retain it.

The current warning that this is **not an upper bound for all smooth metrics on the resolution** is essential and correct. At \(h=1/3\), a positive finite-scale smooth correction tending to zero is not excluded. Above \(1/3\), a vanishing-error resolution family cannot overcome the fixed negative orbifold upper bound. Neither observation contradicts Theorem 74.W.

One overstatement remains at the end of §22.6(6), echoed in §24.4: “the orbifold channel is equivalent to the cell problem” is not an established equivalence. Also, failure of connected-sum additivity cannot defeat the signature bound on this fixed \(V_m\). Replace that closing discussion by:

> No orbifold metric on this fixed \(V_m\) can exceed the displayed deficit bound, whether or not its metric resembles an additive connected sum. Other orbifold topologies or other hosts require separate Weyl-infimum information. The supplied results establish neither an equality between their optimized orbifold values and marked-cell infima nor a reduction of the unrestricted smooth problem to those infima.

## 2. Negative-Yamabe exclusion: correct, with architectural scope

The proof is valid. Its complete inequality chain is
\[
-\|s_g^-\|_2\le Y([g])\le\mathcal Y(M)
=-4\pi\sqrt{2A},
\]
hence
\[
\boxed{\int_M(s_g^-)^2\,d\mu_g\ge32\pi^2A.}
\]

For the derivative-controlled Ricci-flat ALE or Wahl cutoff constructions:

- a Ricci-flat bulk has scalar curvature only in shrinking transition regions;
- a positive-Einstein bulk has positive scalar curvature outside those regions and zero scalar curvature in the fillers;
- the transition scalar-square energy tends to zero.

Both would give \(\|s^-\|_2\to0\), a contradiction. Therefore the Einstein constant must be negative.

The detailed formulations in §§13, 17 and 24 are sound. To prevent the introductory summary from appearing to concern arbitrary degenerations, use:

> Whenever a compact Einstein orbifold admits a compatible derivative-controlled Ricci-flat ALE resolution or Wahl smoothing whose smooth result is \(X\#k\overline{\mathbb{CP}}^2\), its Einstein constant satisfies \(\lambda<0\). Indeed,
> \[
> -\|s_g^-\|_2\le Y([g])\le\mathcal Y(M)=-4\pi\sqrt{2A},
> \]
> whereas the stated cutoffs over a Ricci-flat or positive-Einstein bulk would give \(\|s^-\|_2\to0\).

This is not a compactness theorem for arbitrary near-Einstein sequences. The package correctly keeps that distinction.

## 3. Γ-vertex proof: valid, but replace the superseded Step-54 body

The package’s revised proof order is supported by the supplied Mantione–Torres text. **Proposition 2** applies to essential four-manifolds whose fundamental group is that of a closed nonpositively curved four-manifold, without a spin hypothesis. Its application here requires essentialness, not merely identification of the group.

### Exact factorization argument

Use \(Y\) consistently for the **closed capped vertex**, including when the underlying bubble has several ends. The factorization is up to homotopy, not a literal factorization of a chosen map.

Replace the compressed factorization sentence in package §15 and the old Step-54 proof of (i) by:

> The capped graph decomposition gives
> \[
> \pi_1(M_k)\cong\left(*_v\pi_1(Y_v)\right)*F_{b_1(\mathcal G)}.
> \]
> Since \(\Gamma=\pi_1(X)\) is one-ended and freely indecomposable, and is not \(\mathbb Z\), the graph has no loops, exactly one closed capped vertex \(Y\) carries \(\Gamma\), and all other vertex groups are trivial. Let \(q:M_k\to Y\) be the degree-one connected-sum pinch map, and choose \(f_Y:Y\to X=B\Gamma\) inducing the identified isomorphism on fundamental groups. The degree-one blowdown/classifying map \(c:M_k\to X\) and \(f_Y\circ q\) induce the same fundamental-group homomorphism, so
> \[
> c\simeq f_Y\circ q.
> \]
> Consequently,
> \[
> (f_Y)_*[Y]=[X].
> \]
> Thus \(Y\) is essential and \(f_Y\) has degree one. In particular,
> \[
> f_Y^*:H^2(X;\mathbb Q)\hookrightarrow H^2(Y;\mathbb Q)
> \]
> preserves the intersection pairing, giving \(b^+(Y)\ge b^+(X)\ge3\).

One should **not** describe the closed \(Y\) as literally included in \(M_k\): its punctured summand is included; the pinch map is the appropriate closed-manifold object.

### Multi-ended caps

The PSC step must refer to compactification of **all ends**, rather than invoke a one-ended lemma before one-endedness has been proved:

> If \(Y\) is a bubble vertex with \(e\) AE ends, its cap is obtained by filling all \(e\) end spheres, equivalently adding a distinct compactification point at each end. Under \(\mathrm H_{\rm dec}\), the all-end form of Lemma 53.Y gives this closed cap a PSC metric. The compactification argument uses a positive conformal factor tending to zero like \(r^{-2}\) on every end; its conformal-Laplacian equation has positive point sources at every added point. Thus the positive-Yamabe conclusion is not restricted to \(e=1\). Since \(Y\to X\) has degree one, Mantione–Torres Proposition 2 forbids PSC. Hence \(Y\) is a bulk vertex.

This states the analytic dependency already recorded in Step-54 Lemma 54.2. Smoothness of a naïve inverted metric is not required or automatically supplied by arbitrary order-\(\tau\) decay; the derivative-controlled compactification/Yamabe argument is the relevant input.

Every bubble complement now contains \(Y\), so ordinary two-positive-side SW vanishing yields
\[
b^+(\widehat N_j)=0.
\]
The charge estimate then gives
\[
\sum_j\left[4(e_j-1)+4b_1(\widehat N_j)+b_2(\widehat N_j)\right]<k.
\]
For \(k=1\), the caps are simply connected integral homology spheres, hence homotopy spheres; bubbles are one-ended and the bulk is connected. The attainment conclusion still needs the recorded energy-equality/removability hypotheses and standard caps for attainment on the original smooth \(M\).

### Negative scalar curvature without SW transfer

The Step-54 body still uses \(SW_{V\#\Sigma}=SW_V\), despite the binding erratum. Replace that paragraph in (iii) by:

> The bulk \(V\) is essential and has \(\pi_1(V)=\Gamma\), so Mantione–Torres Proposition 2 excludes PSC on \(V\). The smooth \(P\)-critical metric \(g_0\) has constant scalar curvature. If that constant were zero, Bourguignon’s theorem would make \(g_0\) Ricci-flat, and the nonnegative-Ricci fundamental-group theorem would make \(\Gamma\) virtually abelian, impossible for a cocompact complex-hyperbolic lattice. Hence \(s_{g_0}<0\). At nonzero constant scalar curvature, a \(P\)-critical Bach-flat metric is Einstein; otherwise \(g_0\) is a non-Bach-flat global \(P\)-minimizer on \(V\).

The Step-54 remarks about the “indefinite subcase \(b^+(R)=0\)” and its verification bullets must likewise be labeled superseded for ball-quotient hosts. The present dependency is:

> \(\mathrm H_{\rm dec}\) supplies PSC of the hypothetical Γ-carrying bubble cap; essentialness excludes that vertex; ordinary connected-sum vanishing then eliminates every positive bubble intersection form.

Lemma 54.3 may remain a standalone `[P*]` result with its cylindrical-end compactness dependency. It is neither needed here nor a discharge of the one-sided orbifold-cap SW\(_L\) hypothesis.

## 4. The “current” Step-58 ledger still contains substantive obsolete claims

A notation-only erratum does not repair these statements. The ledger should use
\[
P_*(M)=\inf_gP(g),\qquad
P_{*,\rm orb}(V)=\inf_{g\ {\rm orbifold}}P(g),\qquad
\alpha(M)=\inf_g\mathscr D(g).
\]
All of its Anderson selection, energy and replacement statements concern \(P_*\).

### Required replacements

**Theorem 56.A(i):**
\[
\boxed{P_*(M)=P_{*,\rm orb}(V)=P(V,g_0),}
\]
not \(P(V,g_0)=\alpha_{\rm orb}(V)\).

**Corollary 56.B:**

> A compatible Ricci-flat ALE resolution or Wahl smoothing of an Einstein orbifold gives \(P_*(M')=0\). If the Einstein constant is nonzero, Lemma 86.S also gives \(\alpha(M')=0\). A Ricci-flat bulk alone gives no such \(\alpha\)-conclusion. When \(M'\) is a general-type blow-up, the negative-Yamabe exclusion forces the Einstein constant to be negative.

**Upper input (U):**

> For ball quotients, the analytic CH-collar construction proves \(P_*(M_k)<8\pi^2k\) on every fixed host. The fixed numerical certificate supplies its stated quantitative endpoint only where its collar fits. For arbitrary minimal general-type hosts, the current strict upper theorem is Corollary 59.KE, using the KE canonical model and ALE localization.

The certificate \(0.995662732771115\) is not a uniform numerical upper bound on every ball quotient without its fitting hypothesis.

**Theorem 57.Φ and open gate IV.5:**

> The historical matched-coefficient calculation is superseded by Theorem 59.R: on a \(P\)-critical insertion region,
> \[
> P(\widetilde g_\varepsilon)
> =P(g)+8\pi^2-8\pi^2\varepsilon R^+_p(\zeta,\zeta)
> +4\pi^2\Phi(\mathrm{Rm}_p,\zeta,K)\varepsilon^2\log(1/\varepsilon)
> +O(\varepsilon^2).
> \]
> When \(\mathrm{Ric}^\circ_p=0\) and \(\zeta\) is an eigenvector,
> \[
> \Phi_{\rm opt}
> =-\frac12\mu_1(\mu_1-\mu_2-\mu_3)
> -\frac12(\mu_2-\mu_3)^2.
> \]
> The logarithmic \(W^-\) and Ricci-trace-free corrector sectors are closed. Corollary 59.KE gives the rigorous strict upper bound. This does not assert the same optimized theorem on arbitrary non-\(P\)-critical backgrounds.

**Rigidity §III.C:**

> Under the relocation hypotheses, a minimizing bulk carrying Burns-type bubbles has \(R^+\le0\). The kernel restriction on a general \(P\)-critical bulk is
> \[
> |T|^2\le Q_{\rm Ric}(\mathrm{Ric}^\circ_p).
> \]
> Only in the Einstein specialization does it force equality of the two remaining eigenvalues on a kernel direction and the strict bound \(|W^+|^2<s^2/24\) when \(s<0\).

The current ledger’s unconditional eigenvalue-equality claim for a merely \(P\)-critical bulk is too strong.

**Proposition 58.O:**

> The spherical/hyperbolic bulk has nonzero Einstein constant. ALE gluing gives \(P_*=0\), and Lemma 86.S supplies the additional scalar/Ricci control proving \(\mathscr D(g_\varepsilon)\to0\). Attainment at \(\alpha=0\) is equivalent to existence of an Einstein metric with nonzero Einstein constant. With an \(A_1\) point, the cited Ozuch theorem excludes a sequence of Einstein metrics converging in GH sense to this orbifold.

The old \(P\to0\) proof alone is insufficient for \(\alpha=0\). “Any such Einstein metric is GH-far” should be replaced by the sequence statement; no quantitative distance is supplied.

Finally, the analytic-gate description should use the Step-54 §5(c) correction:

> Compact replacement yields bubble \(P\)-criticality when an actual \(P\)-minimizing sequence converges strongly enough at bubble scales. The unresolved analytic inputs are that convergence and derivative-controlled AE decay. Proposition 54.4 is an alternative conditional argument, not an unconditional assertion that the rescaled perturbation vanishes.

## 5. Consequential repairs in §§2–12

### 5.1 Surviving exceptional-area \(\alpha\)

In §3.6 the sentence

> “it is the \(\alpha=0\) equality case of Theorem AKΓ”

still uses the retired exceptional-area variable, despite its renaming in §3.7. Replace it by:

> The common mode is the formal \(\eta=1,\varpi=0\) boundary equality profile of Theorem AKΓ, with \(\beta(r)=2\theta-3\theta^2\). It is not a closed almost-Kähler equality metric: Lemma T forces \(\varpi>0\).

This has no implication that the human infimum \(\alpha(M)\) is zero.

### 5.2 Cell-infimum notation and scope

The early \(p_{1,0}\) symbols are ambiguous against §1’s convention. Use
\[
\mathfrak p^{\rm diag}_{1,0}
=\inf_{\rm diagonal}\frac{P}{8\pi^2},
\qquad
\mathfrak P_{1,0}=\inf_{\rm all\ marked\ cells}P,
\]
consistently. These are different domains.

In particular, §6.3 should not replace its unqualified cell question by a diagonal-only question. Use:

> The nonstandard-boundary filling supplies neither a zero exact-CH-collar cell nor a proof that \(\mathfrak P_{1,0}=0\); it also does not establish \(\mathfrak p^{\rm diag}_{1,0}=0\).

The normalized lower-case metric value \(p_c\) in §5.3 is not problematic: it is explicitly a value/enclosure endpoint for one metric, not an infimum.

### 5.3 Retired openness statements

In §7 replace “the full \(-9\) remainder” by:

> The local second-order remainder on \(P\)-critical backgrounds is Theorem 59.R. The unrestricted global passage, positivity of \(\mathfrak P_{1,0}\), global–cell asymptotic equality, standard-CR diagonal nonexistence and degeneration control remain unresolved. No unrestricted remainder theorem for arbitrary non-\(P\)-critical backgrounds is asserted.

In §9, item 5, avoid listing already-proved diagonal truncation as wholly open:

> Truncation is proved in the recorded diagonal ACH class and in the marked rate-\(>4\) setting supplied by Theorem C/Theorem T. Extension beyond those hypotheses, positivity of the unrestricted cell infimum and identification of global near-minimizers with such cells remain unresolved.

### 5.4 Historical headings and O10 status

The opening “O10 has not advanced since §2.2” contradicts the additional necessary escape asymptotics in §10. Replace it by:

> **O10 current status.** The density-free actual-field lower estimate remains unresolved. Section 2.2 supplies the finite-\(\beta\) alignment theorem; §10 adds necessary asymptotics for a hypothetical \(\beta\to\infty,\kappa_\beta\to0\) sequence. Neither result supplies the missing density-free endpoint theorem.

Relabel §9 as:

> **Historical research targets, with current theorem status supplied by later sections**

and replace §10’s “Highest-value next object” paragraph by:

> **Step-47 localization target and subsequent result.** The Riemannian localized coercivity target was subsequently realized under the CH-entrance and gauge hypotheses of Theorem 48.L, with the Yamabe/core formulation in 48.LY. Unrestricted entrance and the per-core Weyl–volume inequality remain unresolved.

The supersession discussion in §3.9 is already clear and should remain: the failed \(H^2\subset L^\infty\) premise is explicitly withdrawn, while the linear gaps are retained. Historical numerical mechanisms in §4 need no new theorem status merely because their headings are old.

## 6. What is already sound, and what remains open

No further human-\(\alpha\)/\(P_*\) interchange is needed in the principal early constructions:

- §§3.1–3.2 have nonzero-scale Einstein exteriors, so their \(\alpha=0\) conclusions are justified.
- The conditional hyperbolic sharp theorem retains its missing Yamabe identity.
- The balanced upper law uses the correct conformal quotient and packing hypotheses.
- §§11–12 correctly distinguish CH-entered localized estimates from an unrestricted concentration-count theorem.
- Corollary 52.8 correctly has a factor \(1/2\) for \(P\), and **none** for \(\alpha\).
- The Ricci-flat support argument and the positive-denominator clause in Lemma 86.S′ are correctly integrated.

These repairs leave the active problem unchanged. For a fixed general-type blow-up in
\[
0<k<A/3,
\]
the package has
\[
P_*<8\pi^2k,\qquad
0\le\alpha<\frac{4k}{A+k},\qquad
P_*=0\iff\alpha=0.
\]
Apart from the inherited actual-supply window, it does not establish general positivity, a zero-infimum construction on a fixed blow-up, or Einstein existence/nonexistence. The exact orbifold computation restricts one possible degeneration architecture; it does not remove that architecture from the hard range or replace the global joint-realizability problem.