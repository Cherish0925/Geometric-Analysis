# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/notes/step72_orientation_free_weyl_deficit_law.md",
    "Sessions/S1003A02/workspace/notes/step74_packing_weyl_theorem_and_scope.md"
  ]
}
```

## Task

Read the repaired theorem package as a mathematical referee with emphasis on the Step-70 P versus human-defect split: Corollary 52.8 and covering factors, §§13–20 degeneration/attainment statements, Lemma 54.3's one-sided PSC neck argument and status, and §§24.0–24.4. Test the proposed new synthesis that an S^4/Z2 orbifold summand cannot move the Weyl-deficit frontier beyond h=1/3: use orbifold Euler characteristic, d=8pi^2 chi_orb-W, the connected-sum correction -16pi^2, and conservation of d under Ricci-flat ALE resolution. Identify mathematically consequential remaining errors or scope changes and give precise replacement text, while keeping the hard range 0<k<A/3 explicit.

## Output

# Referee memo: P versus the human defect in the theorem package, orbifold summands, and the k = 1 neck lemma

## 0. Summary

The Step-70 split between \(P\) and \(\mathscr D\) is carried correctly through §1, §13 (Corollary 52.8, Lemma 86.S/S′), §20.4–20.6 and §24.0–24.4. One mathematically consequential leftover remains in the canonical source files rather than the package. Three statements can be sharpened or repaired:

- an α-statement about Ricci-flat orbifolds (§20.4) that is stated more generally than its proof;
- the dependency of Theorem 54.A on Lemma 54.3, which can be removed entirely for ball-quotient hosts;
- the λ = 0 alternative in the orbifold zero-gap architecture (§24.1(4)), which is excluded by the Yamabe invariant.

The proposed \(S^4/\mathbb Z_2\) synthesis is correct only in a precise sense. It holds for the additive connected-sum ledger over a host with \(d_*(X)=4\pi^2A/3\). It is false as a statement about the true Weyl-deficit frontier. Its correct form is a clean general theorem: the per-class Weyl loss of any summand is at least its Hitchin–Thorpe number. That theorem is the Weyl-deficit analogue of the bubble charge \(4b_1+b_2\) of Lemma 54.1.

---

## 1. Corollary 52.8, covering factors, and the defect formula

**Checked.**

- **Defect formula.** Minimizing \(\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)\) over \(\mu=1/\lambda\) gives
  \[
  \mathscr D=4-\frac{T_s^2}{VR},\qquad T_s=\int s .
  \]
  This equals \((4P+L_s)/R\), since \(4P=4R-S\) and \(L_s=S-T_s^2/V\). If \(T_s=0\), the infimum 4 is approached as \(\lambda\to\infty\) and is not attained. That is harmless.
- **Covering behaviour.** Under a degree-\(m\) (orbifold) covering, \(R\), \(V\) and \(T_s\) scale by \(m\), so \(\mathscr D\) is unchanged while \(P\) scales by \(m\). The package's [P]/[α] split of 52.8 is therefore right: \(P_{*,\rm orb}(X\#S^4/\mathbb Z_2)=\tfrac12P_*^\iota(X\#X)\), but \(\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)=\alpha^\iota(X\#X)\) with no factor.
- **Smooth invariant metrics.** \(\iota\)-invariant smooth metrics on \(Z\) are exactly orbifold metrics smooth in orbifold charts on \(Z/\iota\). The infimum identity therefore holds without approximation.
- **The \(m>1\) cover.** The cover topology the Step-52 verifier asked for is elementary. Here \(\pi_1^{\rm orb}(X\#m\,S^4/\mathbb Z_2)=\pi_1(X)*\mathbb Z_2^{*m}\). Mapping \(\pi_1(X)\mapsto1\) and every \(\mathbb Z_2\) generator to \(-1\) gives a double cover with:
  - two copies of \(X\), and \(m\) copies of \(S^4\), each joining the two copies;
  - a gluing graph with 2 vertices and \(m\) edges, so \(b_1=m-1\);
  - Euler-characteristic check: \(\chi=2(\chi(X)-m)=2\chi(X)-2+(m-1)(-2)\).

  So the cover is \(X\#X\#(m-1)(S^1\times S^3)\) with \(2m\) isolated fixed points. This sentence can replace the "needs an equivariant argument" status in §13.

**Leftover in source files (consequential for anyone reading the canonical paths).** `step52_residual_norm_selection_absorption.md` still states three things the package has withdrawn or renamed:

- the boxed \(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\tfrac12\alpha^\iota(X\#X)\), in §3 and again in §5.7;
- Corollary 52.9(i) as "\(\alpha(M)=0\) unconditionally";
- Theorem 52.3 with "\(P(g_i)\to\alpha(M)\)".

In that file the symbol α means \(P_*\). Insert at the top:

> *Erratum (Step 86, binding).* In this note \(\alpha\) denotes the trace-free infimum \(P_*\). Every boxed inequality of the form \(\alpha\le\frac12\alpha^\iota\) is a \(P\)-statement. For the human defect \(\mathscr D\) the correct form is \(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\alpha^\iota(X\#X)\), with no factor. Corollary 52.9(i) gives \(\alpha=0\) only when the orbifold Einstein constant is nonzero (Lemma 86.S).

---

## 2. §§13–20: degeneration and attainment statements

**Lemma 86.S.** Correct as stated.

- The cutoff choice \(\rho=\varepsilon^{\tau/(\tau+2)}\) balances \(\rho^2\) against \((\varepsilon/\rho)^\tau\), so \(|\mathrm{Ric}|=O(1)\) on the annulus.
- \(R\), \(T_s\) and \(V\) each move by \(O(\rho^4)\), and \(\mathscr D=4-T_s^2/(VR)\) is continuous on \(\{R>0\}\).
- The numerical exponent 2.64 against \(8/3\) is consistent.

**Lemma 86.S′.** Correct.

- On a scalar-flat bubble, \(|\mathrm{Ric}|^2=|\mathrm{Ric}^\circ|^2\), so the bubble adds \(P(N)\) to \(R\) and \(4P(N)\) to \(4P+L_s\).
- The KE check holds: \(R=4\cdot2\pi^2A=8\pi^2A\) at \(\mathrm{Ric}=-g\), which gives \(4k/(A+k)\).

**§20.4, 59.N: needs repair.** The sentence "For Ricci-flat orbifolds (Kummer \(T^4/\pm1\to\) K3), \(\alpha\ge1\)" is proved only where the resolution satisfies \(2\chi=3|\tau|\), as K3 does (\(\chi=24\), \(\tau=-16\)). For a general Ricci-flat orbifold resolution, near-Ricci-flat metrics give only \(2\chi\pm3\tau\ge0\), possibly strict. Then \(\alpha<1\) is decided by whether some *other* conformal class has \(\mathcal W<8\pi^2\chi\), and nothing in the package settles that. Replacement:

> For Ricci-flat orbifolds the glued metrics give \(P_*=0\) and no information on \(\alpha\). For the Kummer resolution, K3 has \(2\chi=3|\tau|\), so \(\alpha(\mathrm{K3})=1\) by §22.4.

**59.Z α-version.** Checked.

- \(\alpha=0\) forces \(T_\pm>0\), because \(T_+\le0\) gives \(\mathscr D\ge1\) by (72.1).
- After normalizing \(\lambda=\pm1\), the bound \(V\le12\pi^2\chi(1+o(1))\) follows from \(8\pi^2\chi\ge S/24-P/2\approx 2V/3\).

**New exclusion that should be recorded (it closes the λ = 0 branch of §13, §24.1(4) and 24.3).**

> **Lemma (Yamabe exclusion of λ = 0 degenerations).** Let \(\mathcal Y(M)<0\). Then \(M\) is not a Ricci-flat-ALE resolution or Milnor-fibre smoothing of a compact Ricci-flat orbifold. More generally, no family \(g_\varepsilon\) on \(M\) has \(\|s_{g_\varepsilon}\|_{L^2}\to0\).

*Proof.* In dimension four, \(\int su^2\ge-\|s\|_2\|u\|_4^2\), so \(Y([g])\ge-\|s_g\|_{L^2}\). The glued metrics have \(\|s\|_2^2=O(\rho^4)\), hence \(\mathcal Y(M)\ge0\), a contradiction.

For \(M=X\#k\overline{\mathbb{CP}}^2\), LeBrun's \(\mathcal Y(M)=-4\pi\sqrt{2A}\) (L1) therefore makes the proviso "\(\lambda\ne0\)" automatic in every orbifold zero-gap architecture of §24.1(4). It also explains L3 (\(P_*=0\iff\alpha=0\)) at the level of constructions. The parenthetical "with \(\lambda\ne0\)" in §13's open-range consequence can be replaced by "(\(\lambda=0\) is impossible: \(\mathcal Y(M)<0\))".

**§20.6.** Calling the resolved \(S^4/\pm1\) both \(\mathbb{CP}^2\#\mathbb{CP}^2\) (86.S numerics, 61.EH) and \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\) (52.7a) is harmless, since \(\mathscr D\) is orientation-free. One sentence fixing the orientation convention would prevent a reader from inferring two different manifolds.

---

## 3. Lemma 54.3 and its role in Theorem 54.A

**The one-sided argument itself.** The argument is mathematically sound in the form written.

- Uniform energy and the pointwise bound on \(|\Phi|\) give subsequential limits on the PSC side \(Z^\circ\) for every long-neck sequence, so energy cannot "leave" \(Z\).
- The round \(S^3\) has a single nondegenerate reducible critical point.
- Irreducibles on \(Z^\circ\) die by the Weitzenböck formula.
- Reducibles on \(Z^\circ\) impose a codimension-\(b^+(Z)\) condition on the perturbation.

The case actually used has \(b^+(R)=0\) and \(b^+(Z)=b^+(M)\ge2\). There the statement is equivalent to the familiar reduction "SW of \(Z\#R\), \(b^+(R)=0\), is governed by SW of \(Z\)" combined with Witten vanishing on the PSC manifold \(Z\). The [P*] status with an unregistered citation is accurate.

**Consequential observation: Theorem 54.A does not need Lemma 54.3.**

For a ball quotient \(X\), the case \(b^+(R_k)=0\) is the same as the case in which the bubble cap \(\widehat N_k\) is the vertex carrying \(\Gamma=\pi_1(X)\):

- By Stallings, exactly one vertex \(Y\) carries \(\Gamma\).
- The collapse \(M\to Y\), composed with \(Y\to B\Gamma=X\), is the degree-one blow-down. So \(Y\to X\) has degree one and \(Q_X\hookrightarrow Q_Y\), giving \(b^+(Y)\ge b^+(X)\ge3\).
- Hence if \(\widehat N_k\ne Y\), then \(R_k\supset Y\) and \(b^+(R_k)\ge3\).

If \(\widehat N_k=Y\), then \(\widehat N_k\) is an essential closed oriented four-manifold whose fundamental group is that of a closed nonpositively curved manifold. Under \(\mathrm H_{\rm dec}\), Lemma 53.Y gives it a PSC metric. This contradicts Mantione's Proposition 2 (\cite{mantionegeographya}), which is already registered in §24.3 for the real-hyperbolic case and applies verbatim to complex-hyperbolic \(\Gamma\).

So every bubble cap is simply connected *without* Seiberg–Witten theory. Ordinary connected-sum vanishing then gives \(b^+(\widehat N_k)=0\). The hypothesis ledger is unchanged: \(\mathrm H_{\rm dec}\) is still used exactly in the \(\Gamma\)-cap subcase. What changes is that an unsourced lemma is replaced by a registered source.

Replacement text for §15, "Lemma 54.3":

> **Lemma 54.3 (S³ necks) [P*]** — unchanged as a standalone statement. **Not used in Theorem 54.A.** For ball-quotient hosts the proof order is:
> (1) \(\pi_1\), Stallings and degree one: the \(\Gamma\)-vertex \(Y\) has \(b^+(Y)\ge b^+(X)\ge3\);
> (2) a \(\Gamma\)-carrying bubble cap would be essential, nonpositively-curved-\(\pi_1\) and PSC (\(\mathrm H_{\rm dec}\), Lemma 53.Y), which contradicts \cite{mantionegeographya}, Prop. 2;
> (3) hence all caps are simply connected, \(b^+(R_k)\ge3\), and ordinary connected-sum vanishing gives \(b^+(\widehat N_k)=0\);
> (4) the charge bound (1) of Step 54 follows.
> Lemma 54.3 is needed only for hosts whose \(\pi_1\) does not force a \(b^+\)-carrying vertex, e.g. the general \(b^+\ge2\) hosts of §24.3.

In §24.3 ("For general \(b^+\ge2\) hosts the same SW and charge argument…") add: "this uses Lemma 54.3 [P*] in the subcase \(b^+(R)=0\)".

The fake projective planes stay excluded: \(b^+=1\) still prevents chamber-independent vanishing.

---

## 4. §§24.0–24.4: arithmetic and logic

**L2.** Verified.

- \(C_+=T_++\mathfrak p\) follows from \(P=4I_++S/12-8\pi^2T_+\).
- \(S\le96\pi^2C_+\) gives \(R\le8\pi^2(4\mathfrak p+3T_+)\).
- The band bound simplifies correctly:
  \[
  \frac{k-A/3}{(k-A/3)+3(A-k)/4}=\frac{4(3k-A)}{3k+5A}.
  \]

**L3.** The upper half rests on \(Y^2\ge32\pi^2A\) for *every* class. That is LeBrun's all-\(b^+\) supply. Since \(4p/(A+p)\) is increasing in \(p\), passing to \(P(\widehat g)\le P(g)\) is legitimate.

**§24.1(4).** Add the Yamabe exclusion of §2, so the architecture list contains only \(\lambda<0\) orbifolds.

**§24.4.** In "the value \(h=\tfrac13\) appears twice", the Kähler frontier and LeBrun's bound are correctly distinguished. The orbifold synthesis below adds a third, additive-ledger, appearance of \(1/3\). The paragraph should say this frontier is host-dependent, as explained next.

---

## 5. Test of the \(S^4/\mathbb Z_2\) synthesis

**Data.** All curvature integrals use the session operator norm. The Euler characteristic \(\chi_{\rm orb}\) is computed by Satake–Gauss–Bonnet, \(8\pi^2\chi_{\rm orb}=\mathcal W+S/24-P/2\), which has no η-term. So (72.1) and the unit-wall law hold verbatim on orbifolds. The Yamabe minimizer may fail to exist in the positive orbifold case, but the minimization lemma uses only \(S\ge Y^2\), which holds without a minimizer.

1. **The summand.** \(\chi_{\rm orb}(S^4/\mathbb Z_2)=1\). The round metric has \(\mathcal W=0\), so \(d=8\pi^2\). Since \(\mathcal W\ge0\), \(8\pi^2\) is the maximum.
2. **Connected sum at a smooth point.** Kobayashi subadditivity is a gluing construction at smooth points and applies unchanged. It gives
   \[
   d_*^{\rm orb}(X\#m\,S^4/\mathbb Z_2)\ge d_*(X)-8\pi^2m .
   \]
   As a check, \(\chi_{\rm orb}=\chi(X)-m\).
3. **Conservation under Ricci-flat ALE resolution.** For Ricci-flat ALE \(N\) with group \(\Gamma\), Gauss–Bonnet gives \(\int_N|W|^2=8\pi^2(\chi(N)-1/|\Gamma|)\). For Eguchi–Hanson this is \(12\pi^2\), and \(\Delta(8\pi^2\chi)=8\pi^2\cdot\tfrac32\), so \(\Delta d=0\) in the gluing limit. The same holds for \(A_3\) (\(\Delta\chi=15/4\), \(\int|W|^2=30\pi^2\)) and for Wahl balls (\(1-1/n^2\) on both sides). Therefore
   \[
   d_*(X\#2m\overline{\mathbb{CP}}^2)\ge d_*(X)-8\pi^2m,
   \]
   which is *identical* to \(2m\) reversed Fubini–Study summands. Absorption neither gains nor loses Weyl deficit.
4. **The \(\Sigma_4\) case shows why the signature, not \(\mathcal W\ge0\), is the right bound.** Here \(\chi_{\rm orb}=5/4\) would naively allow \(d\le10\pi^2\). But conservation into \(Q_3\) (\(\chi=5\), \(\tau=-3\)) forces \((I_+-I_-)(\Sigma_4)=12\pi^2(-3)+30\pi^2=-6\pi^2\). Hence \(d(\Sigma_4)\le10\pi^2-6\pi^2=4\pi^2=d_*(\#3\overline{\mathbb{CP}}^2)\), and the per-class loss is again \((16\pi^2-4\pi^2)/3=4\pi^2\).

**General statement (correct form of the synthesis).**

> **Proposition (summand ledger).** Let \(Q\) be a closed manifold, or a compact orbifold with isolated points, with \(b^+=0\), \(b_2=m\) and \(b_1=b\). In the orbifold case, use the Weyl signature number \(\sigma_W=(I_+-I_-)/12\pi^2\) fixed by the orbifold signature theorem (η-contribution 0 at \(\mathbb C^2/\pm1\), \(-1/2\) for \(\Sigma_4\)). Then every metric satisfies
> \[
> d(Q)\le8\pi^2\chi_{\rm orb}(Q)-12\pi^2|\sigma_W(Q)|,
> \]
> and in the smooth case \(d(Q)\le4\pi^2(4-4b-m)\). Consequently every construction of the form "host \(\#\) independently optimized summands", including summands later resolved by Ricci-flat ALE (which conserve \(d\)), loses at least \(4\pi^2(m+4b)\) of deficit per summand. Its realized frontier is
> \[
> k<\frac{d_*(X)}{4\pi^2}.
> \]

This is exactly the bubble charge \(4b_1+b_2\) of Lemma 54.1, now read on the deficit side.

**Where the proposed synthesis is wrong and must be restricted.**

- **Host dependence.** The frontier is \(h<d_*(X)/(4\pi^2A)\), not \(h<1/3\). Equality \(d_*(X)=4\pi^2A/3\) is known for ball quotients, where \(\mathcal W_*=12\pi^2\tau\) and \(A=9\tau\). For other minimal general-type surfaces, whether KE minimizes \(\mathcal W\) is open (§21.8). For those surfaces \(d_*(X)>4\pi^2A/3\) is not excluded, and the additive frontier could then lie above \(1/3\) through the host alone.
- **It is not an upper bound on the true frontier.** Kobayashi's inequality is one-sided. Theorem 74.W crosses \(h=1/3\) on ball-quotient covers precisely by host–cell interaction, at cost \(4\pi^2(1-\eta)\) per cell. An \(S^4/\mathbb Z_2\) summand can carry two classes while certified cells carry the others, so a manifold built with an orbifold summand still sits beyond \(1/3\). For any orbifold metric on \(V=X\#m\,S^4/\mathbb Z_2\), the exact relation is
  \[
  d_{\rm orb}(V)=4\pi^2(A-2m)-2I_+(V).
  \]
  The orbifold frontier is therefore the same all-class inequality \(I_+<2\pi^2(A-k)\) as on \(M\). CH-collared \(S^4/\mathbb Z_2\) cells with Weyl saving would move it just as radial Burns cells do.

**Replacement text (new item in §22.6, or §24.4 after "Local models…").**

> **Orbifold summands carry classes at the reversed-Fubini–Study price.** Weyl deficit is conserved under Ricci-flat ALE resolution, since \(\int_N|W|^2=8\pi^2(\chi(N)-1/|\Gamma|)\). A summand with \(b^+=0\) has \(d\le8\pi^2\chi_{\rm orb}-12\pi^2|\sigma_W|\) (\(=4\pi^2(4-m)\) for \(b_1=0\)). Hence, in the connected-sum ledger, round \(S^4/\mathbb Z_2\) (\(d=8\pi^2\), two absorbed classes) and \(\Sigma_4\) (\(d\le4\pi^2\), three classes) each cost exactly \(4\pi^2\) per class, as reversed Fubini–Study does. This gives \(d_*(X\#k\overline{\mathbb{CP}}^2)\ge d_*(X)-4\pi^2k\), whose frontier is \(h=1/3\) for ball-quotient hosts and \(h=d_*(X)/(4\pi^2A)\) in general.
>
> This is a statement about additive constructions only. It does not bound the true frontier: Theorem 74.W exceeds it by host–cell interaction, and on \(V=X\#m\,S^4/\mathbb Z_2\) the identity \(d_{\rm orb}=4\pi^2(A-2m)-2I_+\) reduces the orbifold frontier to the same all-class Weyl inequality. Lattice absorption is deficit-neutral, so any gain below \(4\pi^2\) per class must come from Weyl saving in the host, as in Prop. 52.10.

**Hard range \(0<k<A/3\).** Nothing above bears on whether \(\alpha>0\) there or \(\alpha\to0\) on a fixed blow-up.

- The orbifold route enters the hard range only through \(\lambda<0\) Einstein orbifolds \(V\). Such a \(V\) has \(6d_{\rm orb}=R>0\). The conditional orbifold LeBrun estimate restricts it to \(2m\le A/3\).
- If such a \(V\) existed, Lemma 86.S would give \(\alpha(M)=0\) without deciding Einstein existence on \(M\).
- The lower side still requires an inequality that holds through lattice absorption, the certified cells, and the aligned and cscK ends.

The positivity question in \(0<k<A/3\) remains exactly as stated in §24.4, "The unsolved centre, stated plainly".