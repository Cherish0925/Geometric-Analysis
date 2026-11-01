# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/data/step74/neck_and_screen.json",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md",
    "Knowledge/objects/papers/Ricci-Curvature-Minimal-Volumes-and-Seiberg-Witten-Theory--995c93498a8f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Kodaira-dimension-and-the-Yamabe-problem--d0edcef7bc67--1bd338503143/object.md"
  ]
}
```

## Task

Independently verify the mathematical correctness and exact scope of A01 Step-74 Theorem 74.A. Check: transfer of the smooth scalar-curvature lower bound through arbitrary A1 orbifold resolution; all characteristic-number normalizations; the weighted-mean lower bound for the human defect; the Green-football cap construction and its topology/asymptotics; exact values of P_{*,orb} and alpha_orb; equality and nonattainment statements; and what this genuinely supersedes in A02 Theorem 87.O. Pay special attention to whether the scalar lower bound needs the stated SW supply or follows unconditionally for general-type blowups from the Yamabe invariant, and to fake-projective-plane/b^+=1 scope. Give precise corrections if needed.

## Output

# Verification memo: Theorem 74.A (exact paired-A1 orbifold law) and its relation to Theorem 87.O

## 0. Verdict

Theorem 74.A is correct as mathematics. Both exact values hold for every ball-quotient host and every \(m\ge1\):
\[
P_{*,\rm orb}(V_m)=8\pi^2k,\qquad \alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}\qquad(k=2m).
\]
Three corrections affect how the theorem should be stated.

1. **The (SW) "supply hypothesis" is not a hypothesis.** The scalar bound is LeBrun's inherited Yamabe theorem, with no \(b^+\) restriction. The fake-projective-plane case needs no separate chamber statement for any input the theorem uses (§2).
2. **The attainment discussion can be sharpened.** A \(P\)-minimizer automatically has constant \(s<0\). For \(k<A/3\), the \(P\)- and \(\mathscr D\)-attainment problems are therefore the same problem. The \(k>A/3\) nonattainment is an orbifold Hitchin–Thorpe statement that needs no Seiberg–Witten input (§5).
3. **The lower half of 74.A is literally 87.O plus LeBrun's scalar bound.** What 74.A adds is the exclusion of Einstein orbifold metrics at every \(m\), a construction that controls \(P\), \(S\) and \(L_s\) simultaneously, and the exact \(\alpha_{\rm orb}\) (§6).

## 1. Normalizations

All of the following were rechecked.

- **Host invariants.** \(\chi(X)=A/3\) and \(\tau(X)=(c_1^2-2c_2)/3=A/9\).
- **Football invariants.** \(\chi_{\rm orb}(S^4/\mathbb Z_2)=2/2=1\) and \(\tau_{\rm orb}=0\).
- **Link correction.** \(\eta(2,1)=-4s(1,2)=0\). Equivalently, \(\mathbb{RP}^3\) has an orientation-reversing self-diffeomorphism, so the A1 link term vanishes.
- **\(V_m\) invariants.** \(\chi_{\rm orb}(V_m)=A/3-m\) and \(\tau_{\rm orb}=A/9\).
- **Chern–Weil identities.** In LeBrun's norm (the one in which Kähler metrics satisfy \(|W^+|^2=s^2/24\)):
  - \(4\pi^2(2\chi+3\tau)=2I_++S/24-P/2\);
  - \(12\pi^2\tau=I_+-I_-\);
  - hence \(16\pi^2\chi=S/12+2W-P\), which matches the note.
- **Mixed constant.** LeBrun 2001, Thm 2.3, multiplied by \(9/4\), gives \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2(c_1^+)^2\), since \(3\sqrt{2/3}=\sqrt6\).
- **Charge formula (0.2).** For EH, \(\chi=2\), \(\tau=-1\), \(\eta=0\):
  - \(c_+=1-4+3=0\);
  - \(c_-=1-4-3=-6=-4(2-\tfrac12)\).
  
  So \(C_-=-6k\), and (0.1) gives \(T_-(V_m)=A/3-k\) and \(T_+(V_m)=A-k\). These agree with the direct values \(2\chi_{\rm orb}\mp3\tau_{\rm orb}\).
- **Ricci-flat filler identity.** \(I_\pm(N)=-2\pi^2c_\pm(N)\) follows from \(P(N)=0\). For EH it gives \(I_-=12\pi^2\).

## 2. The scalar lower bound: the source, the FPP case, and which resolution carries it

**The smooth bound is unconditional.** For every metric on \(M_k=X\#k\overline{\mathbb{CP}}^2\), with \(X\) of general type:
- LeBrun 1999, Lemma 1, gives \(\int s^2\ge Y_{[g]}^2\) on any conformal class with \(Y_{[g]}\le0\).
- LeBrun 1999, Thm 2, gives \(Y_{[g]}\le Y(M_k)=-4\pi\sqrt{2A}\).
- Together: \(S\ge32\pi^2A\). The Hölder form gives the stronger \(\int(s^-)^2\ge32\pi^2A\).

Theorem 2 is stated in the supplied source for every surface of Kodaira dimension 2. General-type surfaces are algebraic, so the \(b_1\)-even proviso of Theorem A is automatic. The package (§24.0, L1) already records this source reading. The "(SW)" box should therefore be replaced by these citations.

**The b⁺=1 (fake projective plane) mechanism.** The mechanism is visible directly where it matters:
- Since \(b^+(M_k)=1\), the class \(c_1(L)=c_1(X)-\sum E_j\) has \(c_1(L)^2=A-k\).
- For \(k<A\) this class is timelike for every metric. Its self-dual projection never vanishes, so no wall is ever crossed.
- The inequality 74.A needs Seiberg–Witten input only for \(k\le A/3<A\): this is the range in which \(P\ge8\pi^2k\) is used for the \(\alpha\)-value, and the mixed transfer is used only at \(P=8\pi^2k\) with \(k\le A/3\).
- For \(k>A/3\), the \(\alpha\)-value follows from signature alone (§5).
- Only the value \(P_{*,\rm orb}=8\pi^2k\) for FPP hosts with \(k\ge9\) leans on LeBrun's general statement, and that statement covers it.

The sentence "the chamber issue is confined to fake projective planes" should therefore become: "no chamber input beyond LeBrun 1999 Thm 2 / LeBrun 2001 Prop. 3.2 is used." The arithmetic in the note is correct: \(b^+=1\) gives \(p_g=0\), then \(A/9=1-q\), so \(A=9\).

**The mixed bound.** \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2A\) is LeBrun 2001, Thm 2.3 applied with the class of Prop. 3.2, stated there for every metric and all \(b^+\). The note's citation "Prop. 3.8 of LeBrun 2023" is the same inequality.

**The transfer through resolution.** The transfer uses one specific resolution, not an arbitrary one.
- At each \(\mathbb R^4/\pm1\) point both orientations of EH fit, because \(-I\) lies in \(SU(2)_+\cap SU(2)_-\).
- Only the complex-oriented choice produces \(-2\) spheres. The two classes \(e,f\) then span an index-2 sublattice of the definite unimodular rank-2 lattice \(\mathrm{diag}(-1,-1)\), with \(E_{1,2}=(e\pm f)/2\). The result is \(X\#2m\overline{\mathbb{CP}}^2\).
- The reversed choice produces \(X\#2m\mathbb{CP}^2\). Its Seiberg–Witten invariants vanish (\(b^+\ge1\) on both summands), and no scalar bound is available for it.
- Because the bound is a property of the orbifold metric \(g\) itself, one matched resolution suffices, and one always exists.

**The convergence step.** Convergence uses Lemma 86.S with \(\tau=4\) and \(\rho=\varepsilon^{2/3}\). The annulus error is \(\eta=\rho^2+(\varepsilon/\rho)^4=2\varepsilon^{4/3}\), curvature is \(O(1)\), and the volume is \(O(\rho^4)\). This gives \(S(g_\varepsilon)\to S(g)\) and \(\|s^-_{g_\varepsilon}\|_2\to\|s^-_g\|_2\). The hypothesis \(\mathrm{Ric}\not\equiv0\) of 86.S is needed only for continuity of \(\mathscr D\), not for this step.

**Conclusion of the transfer.** Every orbifold metric on \(V_m\) satisfies \(\int(s^-)^2\ge32\pi^2A\), unconditionally. The smooth identification (R) of the resolved football with \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\) is the inherited \(T^2\)-equivariant Orlik–Raymond argument (Lemma 52.6). EH is \(U(2)\)-invariant, so the glued structure is \(T^2\)-invariant.

## 3. Lower bound and the weighted mean

**The weighted mean.** Put \(\sigma=S-32\pi^2A\) and \(w=W-4\pi^2A/3=2I_-\). Then
- \(P=8\pi^2k+\sigma/12+2w\);
- \(R=8\pi^2(A+k)+\sigma/3+2w\);
- \(4P=4k/(A+k)\cdot8\pi^2(A+k)+1\cdot\sigma/3+4\cdot2w\).

So \(4P/R\) is the stated weighted mean, and \(\mathscr D=(4P+L_s)/R\ge\min\{1,4k/(A+k)\}\) holds, with \(R>0\) automatic.

**Relation to 87.O.** Since \(d=8\pi^2\chi_{\rm orb}-W=S/24-P/2\),
\[
P=S/12-2d\ \ge\ \tfrac{32\pi^2A}{12}-8\pi^2(\tfrac A3-2m)=16\pi^2m .
\]
The lower half of 74.A is therefore exactly 87.O combined with the scalar bound.

**Independent cross-check.** Signature gives \(W-8\pi^2\chi_{\rm orb}\ge-4\pi^2T_-(V_m)=4\pi^2(k-A/3)\). The identity \(\mathscr D-1=[6(W-8\pi^2\chi)+L_s]/R\) then gives \(\mathscr D>1\) for \(k>A/3\) with no Seiberg–Witten input at all.

## 4. The Green football cap: independent recomputation

**Curvature of the neck.** For \(h=u^2\delta\) with \(u=1+r^{-2}\), the function \(u\) is harmonic on \(\mathbb R^4\setminus0\). Hence \(s=-6u^{-3}\Delta u=0\), and \(W=0\). The Euclidean components of the trace-free Ricci tensor are
\[
\mathrm{Ric}^\circ=-16\,u^{-2}r^{-6}\,(x x^T-\tfrac{r^2}{4}\delta),\qquad |xx^T-\tfrac{r^2}4\delta|^2=\tfrac34r^4 .
\]
So \(|\mathrm{Ric}^\circ|_h^2=192\,r^{-8}u^{-8}\), and
\[
P(h)=384\pi^2\int_0^\infty\frac{r^3\,dr}{(1+r^2)^4}=384\pi^2\cdot\tfrac1{12}=32\pi^2 .
\]
In addition, \(|\mathrm{Ric}^\circ|\sim8\sqrt3\,r^{-4}\), and the tail beyond \(\varrho\) is \(96\pi^2\varrho^{-4}\). These agree with the JSON.

**The involution \(\iota(x)=\sigma x/|x|^2\).** It has the following properties:
- It is an isometry of \(h\), because inversion pulls \(\delta\) back to \(r^{-4}\delta\).
- It squares to the identity.
- It is orientation-preserving: inversion and \(\sigma\) each reverse orientation.
- Its fixed set is \(\{|x|=1,\ \sigma x=x\}=\{\pm e_4\}\).
- Its differential there is \(\sigma(I-2e_4e_4^T)=-I\).

On the compactified \(S^4\) it is an orientation-preserving involution with two isolated fixed points that exchanges \(0\) and \(\infty\). Its quotient is the football \(O\). Therefore \(G\) is \(O\) minus one regular point, with a single trivial-group AE end \(\{|x|>1\}\) and \(P(G)=16\pi^2\). The Euler check is \(-P/2+8\pi^2=-8\pi^2+8\pi^2=0=8\pi^2\chi_{\rm orb}(G)\).

**Gluing.** In \(y=\varepsilon x\), the cap is \((1+\varepsilon^2/|y|^2)^2\delta\). With \(\rho=\varepsilon^{1/2}\):
- both the host error \(\rho^2\) and the cap error \(\varepsilon^2\rho^{-2}\) equal \(\varepsilon\), so annulus curvature is \(O(1)\) on volume \(\varepsilon^2\);
- the truncated tail is \(96\pi^2(\varepsilon/\rho)^4=96\pi^2\varepsilon^2\). For \(\varrho>1\) the region \(|x|>\varrho\) embeds in the fundamental domain, so this one-end value applies to \(G\);
- the cap volume is \(O(\rho^4)+O(\varepsilon^4)\), so \(L_s\to0\).

All stated limits hold, and \(\mathscr D\to4k/(A+k)\).

**The ceiling 1.** The cylinder numbers are \(s=6\), \(|\mathrm{Ric}|^2=12\) and \(|\mathrm{Ric}^\circ|^2=3\), with \(L_s=O(1)\). The dumbbell is local at a regular point, so it applies to orbifolds without change.

**Relation to 87.O's construction.** Kobayashi's conformal connected sum, used in 87.O, controls only \(\int|W|^2\). The Green cap is the scalar-flat representative of that same conformally flat cap class, and it fixes \(P\), \(S\) and \(L_s\) separately. This is a real addition.

## 5. Exact values, equality, and attainment

**Exact values.** \(P_{*,\rm orb}(V_m)=8\pi^2k\) holds for all \(m\ge1\). \(\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}\). There is no Einstein orbifold metric on \(V_m\) for any \(m\), and this is now unconditional. Since \(4k/(A+k)>1\iff 3k>A\), the two branches meet exactly at \(k=A/3\).

**The equality chain is correct.** At \(P=8\pi^2k\):
- \(\sigma=0\) and \(I_-=0\);
- \(I_+=12\pi^2\tau_{\rm orb}=4\pi^2A/3\);
- the bound \((\sqrt S+\sqrt{6I_+})^2=(4\sqrt2+2\sqrt2)^2\pi^2A=72\pi^2A\) is attained;
- the Minkowski and Cauchy–Schwarz equality conditions give \(\sqrt6|W^+|=|s|/2\) (so \(|W^+|^2=s^2/24\)) and \(s|W^+|\le0\);
- \(B_+=0\) holds because complex-oriented EH has \(W^+=0\).

**Strengthening 1: constant scalar curvature.** In dimension four, the trace of the Euler–Lagrange operator of \(P\) is a nonzero multiple of \(\Delta s\): \(\tfrac12\Delta s\) from \(\int|\mathrm{Ric}|^2-\tfrac14\int s^2\). A minimizer of \(P\) on the compact orbifold therefore has \(s\equiv s_0\).
- \(s_0=0\) would force \(W^\pm=0\) and \(S=0<32\pi^2A\), which is impossible.
- \(s_0>0\) is excluded by \(\int(s^-)^2\ge32\pi^2A\) (§2).
- Hence \(s_0<0\), and \(|W^+|\) is constant.

So a \(P\)-minimizer has \(L_s=0\) automatically. For \(k<A/3\), attainment of \(\alpha_{\rm orb}\) is then equivalent to attainment of \(P_{*,\rm orb}\). The residual object is an orbifold metric on \(V_m\) with:
- \(W^-=0\) in the complex orientation;
- \(s\equiv s_0<0\) and \(|W^+|^2=s_0^2/24\);
- the Euler–Lagrange equation reducing to a Bach equation of the form \(B_g=c_0\,s_0\,\mathrm{Ric}^\circ\) with a universal \(c_0\ne0\);
- \(\mathrm{Ric}^\circ\not\equiv0\).

Its existence is open. LeBrun's equality analysis (Prop. 2.4) does not transfer, because equality is reached only in the limit of resolved metrics.

**Strengthening 2: the value \(k=A/3\)** (possible only when \(A\in18\mathbb Z\)). Here \(\alpha_{\rm orb}=1\) is attained iff some orbifold metric on \(V_m\) has \(W^-=0\) and constant \(s\). The sign \(s<0\) is forced by the \(s^-\) bound. The quantity \(\sigma\) is unconstrained.

**The value \(k>A/3\).** Nonattainment is correct. Since \(T_-(V_m)=A/3-k<0\), it is the orbifold version of A02 §22.4 and uses signature only.

## 6. What 74.A supersedes

**Superseded in 87.O.** 87.O's deficit formula \(d_{*,\rm orb}=4\pi^2(A/3-2m)\) stays exact and is an input to 74.A. 74.A replaces the following.

1. The Einstein clause "a nonzero-scale Einstein orbifold on \(V_m\) requires \(2m<A/3\)." It becomes: no Einstein orbifold metric on \(V_m\) exists for any \(m\ge1\). The same replacement is needed at:
   - §13, last paragraph;
   - §24.1(4)(b);
   - §24.4, "for this type also \(2m<A/3\)";
   - state_of_problems §1 and §5, "ordinary \(S^4/\mathbb Z_2\) absorption … needs \(2m<A/3\)."
   
   For ball-quotient hosts this absorbing type is eliminated outright.
2. **Corollary for involution-invariant metrics.** For ball-quotient \(X\), there is no \(\iota\)-invariant Einstein metric on \(X\#X\). More generally there is none on the double cover \(X\#X\#(m-1)(S^1\times S^3)\) of \(V_m\). Moreover:
   - \(P^\iota_*=2P_{*,\rm orb}=32\pi^2m\);
   - \(\alpha^\iota=\min\{1,8m/(A+2m)\}\).
3. **Corollary 52.8 becomes explicit.** It now reads \(\alpha(X\#2m\overline{\mathbb{CP}}^2)\le\min\{1,4k/(A+k)\}\). This is strictly weaker than 69.KE for \(k<A/3\). The orbifold channel therefore lies strictly above the smooth infimum: \(\alpha(M_{2m})<\alpha_{\rm orb}(V_m)\). For \(1/3<h<1/3+\eta\beta_0\) on deep covers, the same strict separation follows from 74.W.
4. **Per-class cost.** The orbifold channel costs exactly \(8\pi^2\) per class, with no finite-scale saving possible, because the lower bound is rigid. This explains §5 of the note: a minimizing sequence cannot converge smoothly on the regular locus to an orbifold metric on \(V_m\). The Fatou argument there is correct under the stated hypotheses (i)–(iii), and (SW) can be dropped from (iii).

**Extension to non-ball hosts** (my derivation, same proof). For general-type \(X\) with \(\tau(X)\ge0\):
\[
P_{*,\rm orb}(X\#m\,O)\ \ge\ 8\pi^2\max\Big\{k-\tfrac A3,\ k-\tfrac43(3c_2-A)\Big\}.
\]
The first term is LeBrun's \(C_+\ge2A/3\) transferred (\(B_+=0\)). The second is scalar bound plus signature, using \(\chi-3\tau=3c_2-c_1^2\ge0\) by BMY. Einstein orbifold metrics on \(X\#m\,O\) are excluded once \(k\) exceeds either quantity. The ball-quotient case is exactly the case \(3c_2=A\), which is why 74.A is sharp there.

## 7. Notes on 74.B–74.D (not the main task)

**Formula checks.** The following were rechecked and are consistent:
- \(I_\pm=2\pi^2(T_\pm-x)\) at Einstein metrics;
- the reduction of the mixed inequality to \([\sqrt{8x}+\sqrt{T_+-x}]^2\ge6A+C_+\);
- the maximum \(9T_+\) at \(x=8T_+/9\).

**A structural point on the screening survivors.** A Ricci-flat filler that is Kähler in either orientation has \(c_+=0\) or \(c_-=0\). All 8 cyclic \(b_2=1\) survivors, all 7 hypothetical ADE-end survivors, and the rational-ball rows with \(c_\pm<0\) together would require a Ricci-flat ALE space with both chiral Weyl parts nonzero, that is, one that is not locally hyperkähler for either orientation. No such metric appears in the session material. So for these rows the open input (a) of §4 is more specific than "existence of a Ricci-flat ALE metric": it is existence of a non-Kähler Ricci-flat ALE space. Only the \(c_+=0\) rows (Kronheimer and T-type/Šuvaina) are backed by actual metrics.