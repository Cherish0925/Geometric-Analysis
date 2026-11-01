# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 87,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the repaired theorem package as a mathematical referee with emphasis on the Step-70 P versus human-defect split: Corollary 52.8 and covering factors, §§13–20 degeneration/attainment statements, Lemma 54.3's one-sided PSC neck argument and status, and §§24.0–24.4. Test the proposed new synthesis that an S^4/Z2 orbifold summand cannot move the Weyl-deficit frontier beyond h=1/3: use orbifold Euler characteristic, d=8pi^2 chi_orb-W, the connected-sum correction -16pi^2, and conservation of d under Ricci-flat ALE resolution. Identify mathematically consequential remaining errors or scope changes and give precise replacement text, while keeping the hard range 0<k<A/3 explicit.

## Integrated Scientific Memo

# Referee memo

The repaired package correctly separates the trace-free infimum \(P_*\) from the human-defect infimum \(\alpha\). The principal remaining mathematical correction concerns the proposed orbifold synthesis:

> **For a ball-quotient host, the \(S^4/\mathbb Z_2\) orbifold frontier is exactly \(h=1/3\), for all orbifold metrics on that fixed orbifold—not merely for additive connected-sum metrics. This does not bound the frontier over all smooth metrics on its resolution.**

The distinction follows from the orbifold signature formula. One supplied analysis overlooked this upper bound and consequently proposed orbifold Weyl-saving competitors that cannot exist in the stated ball-quotient setting.

## 1. Covering factors and the canonical Step-52 note

Write
\[
T_s=\int s\,d\mu,\qquad R=\int|\operatorname{Ric}|^2\,d\mu,\qquad
\mathscr D=4-\frac{T_s^2}{VR}
=\frac{4P+L_s}{R}\quad(R>0).
\]
At \(R=0\), the definition gives \(\mathscr D=4\).

For a degree-\(q\) orbifold covering,
\[
(P,R,L_s,V,T_s)\longmapsto q(P,R,L_s,V,T_s).
\]
Consequently,
\[
\mathscr D(\pi^*g)=\mathscr D(g),\qquad
d(\pi^*g)=q\,d_{\rm orb}(g),\qquad
\frac{d(\pi^*g)}{R(\pi^*g)}=\frac{d_{\rm orb}(g)}{R(g)}.
\]

Thus the package’s repaired Corollary 52.8 is correct:
\[
P_{*,\rm orb}\!\left(X\#S^4/\mathbb Z_2\right)
=\frac12P_*^\iota(X\#X),
\]
but
\[
\alpha_{\rm orb}\!\left(X\#S^4/\mathbb Z_2\right)
=\alpha^\iota(X\#X).
\]
After Eguchi–Hanson resolution,
\[
P_*(X\#2\overline{\mathbb{CP}}^2)
\le\frac12P_*^\iota(X\#X),\qquad
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le\alpha^\iota(X\#X).
\]

The canonical file `step52_residual_norm_selection_absorption.md` still contains the erroneous human-\(\alpha\) factor \(1/2\), including in its “binding” §5.7, and still uses \(\alpha\) for limits of \(P\). These are substantive stale statements, not harmless notation.

**Replacement text at the beginning of that note:**

> **Functional correction, binding throughout.** Every infimum appearing as the limit of \(P(g_i)\), in a \(P\)-flow estimate, or in a \(P\)-Palais–Smale theorem is \(P_*(M)\), not the human-defect infimum \(\alpha(M)\). In particular, the factor \(1/2\) in Corollary 52.8 belongs only to \(P\). For \(\mathscr D\), finite orbifold covers preserve the functional, and
> \[
> \alpha(X\#2\overline{\mathbb{CP}}^2)\le\alpha^\iota(X\#X).
> \]
> Ricci-flat ALE resolution of an Einstein orbifold always gives \(P_*=0\); it gives \(\alpha=0\) when the Einstein constant is nonzero. The structure and selection results of this note concern \(P\)-minimizing sequences.

The multiple-summand double-cover topology can also be justified explicitly. The orbifold cover is constructed from two punctured copies of \(X\) and \(m\) copies of the twice-punctured \(S^4\) cover, joining the two copies of \(X\). Its graph has two vertices and \(m\) edges. Hence
\[
\widetilde V_m\cong X\#X\#(m-1)(S^1\times S^3),
\]
with the deck involution having \(2m\) isolated fixed points. This supplies the equivariant construction missing from the older Step-52 verification.

## 2. Exact test of the \(S^4/\mathbb Z_2\) synthesis

All integrals below use the session curvature-operator norm. The Euler characteristic is the **Satake/Chern–Gauss–Bonnet orbifold Euler characteristic**, not a stringy Euler characteristic.

### 2.1 The orbifold summand

Let
\[
\mathcal O=S^4/\mathbb Z_2
\]
be the quotient with two isolated \(A_1\) points. Then
\[
\chi_{\rm orb}(\mathcal O)=1,\qquad
\tau_{\rm orb}(\mathcal O)=0.
\]
The round quotient is conformally flat, so
\[
\mathcal W_{*,\rm orb}(\mathcal O)=0,\qquad
d_{*,\rm orb}(\mathcal O)=8\pi^2.
\]
Connected sum at smooth points has the correction
\[
d_{*,\rm orb}(V\#U)
\ge d_{*,\rm orb}(V)+d_{*,\rm orb}(U)-16\pi^2.
\]
Thus each independently glued \(\mathcal O\) loses \(8\pi^2\) of deficit while eventually supplying two exceptional classes: the same \(4\pi^2\) per-class loss as reversed Fubini–Study insertion.

This calculation alone is a **lower bound** on the optimized deficit. The following signature calculation is what makes the ball-quotient result exact.

### 2.2 All-metric upper bound on the fixed orbifold

Let \(X\) be a compact ball quotient, with \(A=c_1^2(X)\), in its complex orientation. Then
\[
\chi(X)=\frac A3,\qquad \tau(X)=\frac A9,
\]
and its complex-hyperbolic metric realizes
\[
\mathcal W_*(X)=12\pi^2\tau(X)=\frac{4\pi^2A}{3},
\qquad d_*(X)=\frac{4\pi^2A}{3}.
\]

For
\[
V_m=X\#m\mathcal O,
\]
one has
\[
\chi_{\rm orb}(V_m)=\frac A3-m,\qquad
\tau_{\rm orb}(V_m)=\frac A9.
\]
The \(A_1\) link has zero signature \(\eta\)-correction in the supplied conventions. Therefore every orbifold metric satisfies
\[
I_+-I_-=12\pi^2\tau_{\rm orb}(V_m)=\frac{4\pi^2A}{3},
\]
and hence
\[
I_++I_-\ge\frac{4\pi^2A}{3}.
\]
It follows that
\[
d_{\rm orb}(g)\le
8\pi^2\left(\frac A3-m\right)-\frac{4\pi^2A}{3}
=4\pi^2\left(\frac A3-2m\right).
\]
The connected-sum lower bound matches:
\[
\boxed{\displaystyle
d_{*,\rm orb}(V_m)=4\pi^2\left(\frac A3-2m\right).}
\]

With \(k=2m\),
\[
d_{*,\rm orb}(V_m)>0\iff k<A/3.
\]

This is stronger than an additive-ledger statement. In particular, a CH-collared \(\mathcal O\)-cell cannot improve the host’s self-dual Weyl deficit in this topology. Since its orbifold signature change is zero, exact collar matching gives
\[
\Delta I_+=\Delta I_-.
\]
The removed CH ball has \(I_-=0\), while the inserted cell has \(I_-\ge0\). Thus
\[
\Delta I_+\ge0.
\]
The contrary suggestion that such orbifold cells could have the Weyl-saving effect of the certified Burns cells is incompatible with this signature identity.

For a general minimal general-type host, the additive calculation still gives
\[
d_{*,\rm orb}(X\#m\mathcal O)\ge d_*(X)-8\pi^2m,
\]
but the exact ball-quotient value need not follow. The supplied material does not establish \(d_*(X)=4\pi^2A/3\) for arbitrary such \(X\).

### 2.3 Deficit conservation under shrinking Ricci-flat ALE resolution

A Ricci-flat ALE space \(N\), with asymptotic group \(\Gamma\), satisfies
\[
\int_N|W|^2=8\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right).
\]
Replacing an orbifold point by \(N\) increases the Euler term by precisely the same amount. Under the derivative-controlled cutoff gluing,
\[
\boxed{\displaystyle
d(M,g_\varepsilon)\longrightarrow d_{\rm orb}(V,g).}
\]
Equivalently, use
\[
d=\frac S{24}-\frac P2:
\]
both \(S\) and \(P\) of the glued metrics converge to their orbifold values.

For Eguchi–Hanson,
\[
\chi(N)=2,\qquad |\Gamma|=2,\qquad \int_N|W|^2=12\pi^2.
\]
Resolving all \(2m\) points gives
\[
M=X\#2m\overline{\mathbb{CP}}^2,\qquad
\chi(M)-\chi_{\rm orb}(V_m)=3m,
\]
and
\[
\Delta\mathcal W=24\pi^2m=8\pi^2\Delta\chi.
\]
Thus absorption is deficit-neutral in the shrinking limit.

The same cancellation applies to the supplied \(A_3\) and Wahl fillers. For \(\Sigma_4\), the signature bound gives \(d_{\rm orb}\le4\pi^2\), so its additive loss is at least \(12\pi^2\) for three classes. Equality for its optimized deficit is **not** established by the supplied sources.

### 2.4 Necessary scope restriction

The exact orbifold result does **not** imply
\[
d_*(X\#2m\overline{\mathbb{CP}}^2)
\le4\pi^2(A/3-2m).
\]
Resolution transfers orbifold competitors to smooth competitors; it does not transfer an upper bound to all smooth metrics. Theorem 74.W already constructs smooth metrics with positive deficit above \(h=1/3\) on suitable covers.

At \(h=1/3\), every orbifold metric on \(V_m\) has nonpositive deficit. A shrinking resolution may nevertheless have a positive finite-scale correction tending to zero. Above \(h=1/3\), the orbifold deficit has a uniform strictly negative upper bound; a resolution family with vanishing gluing error cannot obtain positive deficit sufficiently close to that orbifold channel.

**Recommended replacement synthesis:**

> **The \(S^4/\mathbb Z_2\) absorption frontier.** For a compact ball quotient \(X\), \(A=c_1^2(X)\), and \(V_m=X\#m(S^4/\mathbb Z_2)\),
> \[
> d_{*,\rm orb}(V_m)=4\pi^2(A/3-2m).
> \]
> The lower bound follows from smooth-point connected-sum gluing with the correction \(-16\pi^2\); the matching upper bound follows from the orbifold signature formula, since the \(A_1\) links have zero \(\eta\)-correction. Shrinking Ricci-flat Eguchi–Hanson resolution conserves deficit in the limit. Hence this orbifold-resolution channel cannot extend a positive limiting deficit beyond \(h=2m/A=1/3\).
>
> This is not an upper bound for the Weyl deficit of all smooth metrics on \(X\#2m\overline{\mathbb{CP}}^2\). Finite-scale smooth host–cell interaction, including Theorem 74.W, can cross \(1/3\). For non-ball-quotient hosts, the exact orbifold value requires additional information about the host Weyl infimum.

There is also a simple source correction in Step 74’s proof:
\[
\text{“signature formula with }\tau=A_Y/3\text{”}
\quad\longrightarrow\quad
\boxed{\tau(Y)=A_Y/9.}
\]
Its final value \(I_+=4\pi^2A_Y/3\) is already correct.

## 3. §§13–20: degeneration and attainment

### 3.1 Lemmas 86.S and 86.S′

Lemma 86.S is correct on its stated domain \(\operatorname{Ric}_g\not\equiv0\). The choice
\[
\rho=\varepsilon^{\tau/(\tau+2)}
\]
balances the chart error \(O(\rho^2)\) with the ALE error \(O((\varepsilon/\rho)^\tau)\), giving bounded Ricci curvature on an annulus of volume \(O(\rho^4)\). Thus \(R,T_s,V\) converge, and \(\mathscr D\) is continuous when the limiting \(R>0\).

For a scalar-flat bubble ledger, writing \(B=\sum P(N_j)\),
\[
\mathscr D(g_\varepsilon)\longrightarrow
\frac{4P(g)+L_s(g)+4B}{R(g)+B}
=4-\frac{T_s(g)^2}{V(g)(R(g)+B)}.
\]
Positive-\(P\) bubbles move the value toward \(4\); Ricci-flat bubbles preserve it. These are glued-family conclusions, not arbitrary-sequence compactness conclusions.

### 3.2 Ricci-flat bulks: correct conclusion and proof

The sentence in §17 that an Einstein bulk gives \(\alpha=0\) “exactly when” its constant is nonzero is too strong as a statement about the manifold’s infimum.

For a Ricci-flat bulk, the naive glued family does satisfy \(\mathscr D\to4\), but this is not justified merely by dividing two \(O(\rho^4)\) quantities. A valid proof uses support. Scalar curvature is supported in a region \(U_\varepsilon\) with volume tending to zero, so
\[
T_s^2\le \operatorname{Vol}(U_\varepsilon)\,S
\le4\operatorname{Vol}(U_\varepsilon)\,R.
\]
Whenever \(R>0\),
\[
0\le4-\mathscr D
\le4\frac{\operatorname{Vol}(U_\varepsilon)}{V}\longrightarrow0.
\]
If \(R=0\), \(\mathscr D=4\) directly.

**Replacement for §17:**

> An Einstein orbifold bulk with nonzero Einstein constant gives \(\alpha(M)=0\) after Ricci-flat ALE resolution or Wahl smoothing, by Lemma 86.S. A Ricci-flat bulk gives \(P_*(M)=0\); the naive glued family has \(\mathscr D\to4\), and this construction alone does not determine \(\alpha(M)\).

Likewise, §20.4 should not assert \(\alpha\ge1\) for arbitrary Ricci-flat-orbifold resolutions.

> For Ricci-flat orbifolds, the construction gives \(P_*=0\), without a general conclusion about \(\alpha\). For the Kummer resolution specifically, K3 satisfies \(2\chi=3|\tau|\), and therefore \(\alpha(\mathrm{K3})=1\) by the unit-wall theorem.

### 3.3 A useful strengthening on general-type blow-ups

The supplied Yamabe invariant excludes Ricci-flat **and positive-Einstein** orbifold bulks whose stated Ricci-flat resolution or smoothing is a general-type blow-up.

For every smooth metric,
\[
Y([g])\ge-\|s_g^-\|_{L^2}.
\]
Indeed this follows immediately from the Yamabe quotient and Hölder’s inequality. Since \(Y([g])\le\mathcal Y(M)<0\),
\[
\|s_g^-\|_{L^2}\ge|\mathcal Y(M)|.
\]
For
\[
M=X\#k\overline{\mathbb{CP}}^2,\qquad
\mathcal Y(M)=-4\pi\sqrt{2A},
\]
every metric therefore satisfies
\[
\int(s_g^-)^2\ge32\pi^2A.
\]

A glued resolution of a Ricci-flat orbifold has \(S\to0\); a resolution of a positive Einstein orbifold has negative scalar curvature only in shrinking collars, with \(\|s^-\|_2\to0\). Both contradict this inequality.

Thus, **within these resolution/smoothing architectures**, any Einstein orbifold bulk for a general-type blow-up necessarily has
\[
\Lambda<0.
\]
This makes the nonzero-scale condition automatic in §24.1(4), without removing it from the general Lemma 86.S.

### 3.4 Statements that remain conditional

The repaired package correctly leaves Anderson’s structure theory as a theory of selected \(P\)-minimizing sequences. Numerical equivalence \(P_*=0\iff\alpha=0\) on the general-type blow-ups does not identify their minimizing sequences or normalized limits.

The following qualifications remain necessary:

- Theorem 52.3 needs the named residual, Sobolev, harmonic-radius and neck/removability inputs.
- Theorem 52.5 has the unresolved own-scale smoothing entrance; the false fixed-threshold KS statement cannot be restored.
- Theorem 54.A still requires its convergence, decay, energy-equality and removability hypotheses, and standard caps for attainment on the original smooth manifold.
- §14’s bullet “AE ends of order \(\tau>1\)” should be changed to “any \(\tau>0\) with derivative-controlled decay,” matching its binding correction and the Step-54 note.

Finally, “\(k=1\) is never fully absorbed” needs a scope qualification. The Step-52 source proves this when the root span lies in \(\mathbb QE\). It explicitly allows a larger root lattice to mix \(E\) with host classes. The orbifold degree-one reduction excluding such mixing uses the additional SW\(_L\) input.

**Replacement:**

> A single exceptional direction cannot be absorbed by a root lattice contained in its rational span. At \(k=1\), exclusion of more general Kronheimer absorption requires the additional degree-one/lattice hypotheses, including SW\(_L\) where invoked; mixed host–exceptional root lattices are not excluded by the elementary rank-one calculation alone.

## 4. Lemma 54.3: one-sided PSC neck and a stronger proof organization

### 4.1 Standalone lemma

The one-sided \(S^3\)-neck mechanism is sound, with the analytic dependency stated explicitly. For each fixed Spin\(^c\) structure:

1. Equip \(Z\setminus B^4\) with a PSC cylindrical-end metric.
2. Choose a sufficiently small compactly supported perturbation there.
3. Weitzenböck excludes irreducible finite-energy solutions.
4. Reducibles require
   \[
   2\pi\,c_1(L|_Z)^+=\mathcal H^+(\eta)
   \]
   in the \(L^2\) harmonic self-dual space, of dimension \(b^+(Z)\).
5. Generic perturbation avoids that affine condition.
6. Long-neck compactness across the round \(S^3\), with its unique nondegenerate reducible boundary solution, then makes the closed moduli space empty for sufficiently long necks.

The supplied materials do not register an exact literature theorem with these one-sided quantifiers. Therefore `[P*]`, dependent on standard cylindrical-end compactness, is the appropriate status—not a fully sourced standalone literature theorem.

This does not discharge the spherical-space-form/orbifold-cap SW\(_L\) hypothesis. The two-sided \(L\)-space splitting theorem is a different result.

### 4.2 Removing this lemma from the ball-quotient attainment argument

There is a source-supported alternative for Theorem 54.A, using the essential-manifold PSC obstruction already registered in §24.3.

In a trivial-group connected-sum configuration of
\[
M_k=X\#k\overline{\mathbb{CP}}^2,
\]
free indecomposability of \(\Gamma=\pi_1(X)\) identifies a unique cap \(Y\) carrying \(\Gamma\); all other vertex groups and graph-loop free factors are trivial. The classifying map \(M_k\to X\) has degree one. Its fundamental class is supported on \(Y\), so
\[
Y\to X
\]
also has degree one, implying
\[
Q_X\hookrightarrow Q_Y,\qquad b^+(Y)\ge b^+(X)\ge3.
\]

If \(Y\) were a bubble cap, \(\mathrm H_{\rm dec}\) and the compactification lemma would give it PSC. But \(Y\) is essential and has the fundamental group of a closed nonpositively curved four-manifold. The Mantione obstruction quoted in §24.3 forbids PSC. Hence \(Y\) is bulk, every bubble cap is simply connected, and its complement has \(b^+\ge3\).

Ordinary two-positive-side SW connected-sum vanishing now excludes \(b^+>0\) on every bubble. The charge estimate gives
\[
\sum_j\bigl[4(e_j-1)+4b_1(\widehat N_j)+b_2(\widehat N_j)\bigr]<k.
\]
For \(k=1\), this yields the same homotopy-sphere conclusion.

**Replacement proof-order text:**

> For ball-quotient hosts, the one-sided Lemma 54.3 is not needed. First identify the degree-one \(\Gamma\)-vertex; the essential-manifold PSC obstruction excludes its being a bubble cap. Every bubble complement then has \(b^+\ge3\), and ordinary connected-sum SW vanishing eliminates positive bubble intersection form. Apply the two-orientation charge bound afterward.

This changes the dependency, not the attainment conclusion. The general-host statement in §24.3 can still require Lemma 54.3 in the subcase \(b^+(R)=0\).

## 5. §§24.0–24.4: verified links and precise remaining scope

The principal formulas are correct:
\[
\mathscr D(g)\ge
\frac{\mathfrak p(g)}{\mathfrak p(g)+\frac34(A-k)},
\]
and, for \(A/3\le k<A\),
\[
\boxed{\alpha(M)\ge\frac{4(3k-A)}{3k+5A}.}
\]
Together with
\[
\alpha(M)\le\frac{4\mathfrak p_*}{A+\mathfrak p_*},
\]
they imply, for \(1\le k<A\),
\[
P_*=0\iff\alpha=0,\qquad P_*>0\iff\alpha>0.
\]
They do not imply equality of minimizing sequences. Negative Yamabe invariant gives the correct attainment equivalence
\[
M\text{ Einstein}
\iff P_*=0\text{ attained}
\iff\alpha=0\text{ attained}.
\]

Three textual adjustments are needed:

1. **§24.1(4), “realized architecture”:**
   > **A sufficient zero-gap architecture, whose existence remains open for these general-type blow-ups.**
   
   The package constructs its gluing implication, not an Einstein orbifold of the required general-type topology.

2. **“Orbifolds are permitted exactly in the open range”:**
   > Under the stated orbifold SW supply, the numerical necessary condition is \(k\le A/3\). This does not establish existence or admissibility, and does not by itself remove the equality endpoint. It leaves the strict hard range \(0<k<A/3\) unobstructed.

3. **Step 74’s canonical capacity formulation:** replace \(\Theta_*(h)\) by \(\Theta_*(M)\). Positivity in the hard range is not a capacity upper bound alone:
   \[
   p=k-\frac43\kappa+\frac13\upsilon
   \]
   requires uniform separation of the **joint realizable pairs** \((\kappa,\upsilon)\) from \(p=0\). The repaired package already states this correctly; the canonical note does not.

## 6. The hard range remains explicit

For a fixed general-type blow-up in
\[
\boxed{0<k<A/3},
\]
the package establishes
\[
0\le\alpha(M)<\frac{4k}{A+k}<1,\qquad
P_*(M)<8\pi^2k,
\]
and
\[
P_*(M)=0\iff\alpha(M)=0.
\]
It does not establish general positivity, a zero-infimum construction on a fixed blow-up, or Einstein existence/nonexistence throughout this range. The inherited N1 theorem supplies positive gaps only on its stated actual-field window.

The new orbifold calculation adds a genuine restriction. For a ball quotient,
\[
d_{*,\rm orb}\bigl(X\#m(S^4/\mathbb Z_2)\bigr)
=4\pi^2(A/3-2m).
\]
A nonzero-scale Einstein orbifold has \(6d=R>0\), so this particular absorbing Einstein architecture necessarily satisfies
\[
2m<A/3
\]
**strictly**, independently of the conditional orbifold SW estimate.

It therefore cannot move its orbifold frontier beyond \(1/3\), but remains a possible zero-gap architecture precisely inside the unresolved hard range. A positive-gap theorem there must exclude this architecture as well as smooth Einstein metrics and other concentrating or collapsing near-Einstein sequences. The smooth Weyl-frontier crossing of Theorem 74.W addresses a different question and does not resolve that zero-gap problem.