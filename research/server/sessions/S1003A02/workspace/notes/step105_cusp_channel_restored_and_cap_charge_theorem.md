# Step 105: restoring the cusp channel, proving the cap-charge identity, and testing the Hopf-collapse channel

> **Step-106 binding independent-reading repair.** See `step106_independent_cap_charge_and_D4_candidate.md`. Theorem 105.Q and the bound \(9k+8\sum c_j\le3A\) stand, with these repairs: (i) under (E), a multi-end cap yields the limit of the **sum** of incident charges unless separate end asymptotics are supplied; (ii) scalar-cap vanishing uses the total tail-volume bound and ordered limsup/liminf; (iii) positive-charge ball caps add \(32B\) to Corollary 105.H; (iv) a four-class cap has \(c_+=0\) but \(c_-=20\), hence \(\int|W^-|^2\to40\pi^2\), so it is not energy-free; (v) the generic \(w_2\) exclusion is withdrawn. The matched live object is a rank-four D4 ALF core (end \(S^3/Q_8\), charges \((-2,2)\)) plus the punctured \(\mathbb{RP}^2\)-disk bundle carrying the index-two extension \(-D_4\subset-I_4\). Smooth relative identification and a vanishing-energy collapsing transition remain unproved.

Session S1003A02, Agent2, Execute. Inputs: Spirit #119 and A01 #888 (`Sessions/S1003A01/workspace/notes/spirit_step91_global_reduction_and_carrier_scope.md` §§1–3), both identifying errors in Step 104. Also used: Step-33 Theorem G with its model link charges (`notes/step33_link_charges_global_decomposition_static_channel.md`); the Step-27/29 diagonal charges; Dai–Wei, *Hitchin–Thorpe inequality for noncompact Einstein 4-manifolds* (Knowledge `Hitchin-Thorpe-Inequality-for-Noncompact-Einstein-4--fd6e60eeeaa2--deedf5d03a5f/object.md`, Thm 1.1, Cor 1.2, Thm 3.5, Thm 5.1).
Exact check: `scripts/step105_cap_charge_check.py` writes `data/step105/cap_charge_check.json` (exit 0, `all_ok=True`).

---

## 0. Corrections to Step 104 (binding)

**104.F is withdrawn as an elimination.** The only valid group fact is that a torsion-free cocompact complex-hyperbolic lattice \(\Gamma\) contains no \(\mathbb Z^2\) subgroup. Consequently, a cross-section group containing \(\mathbb Z^2\) cannot map *injectively* into \(\Gamma\). It does not follow that such a cusp is absent from a degeneration: the map can have a kernel, which is exactly what happens under Dehn filling. The intermediate claim that the image must be cyclic is also false; for example, \(\pi_1(\Sigma_g\times S^1)\to\pi_1(\Sigma_g)\) has noncyclic hyperbolic image (A01 #888).

There are three further errors.
- Group theory alone cannot exclude collapse. \(S^1_\varepsilon\times N^3\), with \(N\) closed hyperbolic, collapses with bounded curvature even though its fundamental group is not virtually nilpotent.
- “Spherical cross-section \(\Rightarrow\) orbifold point” conflates Anderson's case I, an ALE bubble at a noncollapsed link, with case III, a Hopf-collapsing \(S^3\) or lens cusp of a finite-volume Einstein domain. Spirit's Step-103 sentence “spherical ends are the orbifold case” is withdrawn for the same reason.
- A map from a noncompact \(\Omega\) to compact \(X\) cannot be proper. Any degree statement belongs to \(\overline\Omega\), relative to its boundary.

Thus the nonattained-zero alternative keeps **three** geometric subchannels: Wahl/Einstein orbifold, \(D_{\ge6}\) prism complement, and Einstein domain with collapsed or cusp complement. Wahl and \(D_{\ge6}\) are sufficient construction routes, not an exhaustive reduction.

**104.C is withdrawn as an identification of a supplied field.**
- All characters \(\zeta^r\) define orbifold line representations at \(\mathbb C^2/\mathbb Z_{n^2}\); \(n\mathbb Z_{n^2}\) is only the subgroup that extends over the smooth rational ball.
- Filler transfer proves inequalities without selecting a spin\(^c\) character, so it supplies no “\(j=0\) field”.
- Every fixed smooth spin\(^c\) structure on \(M\) restricts over the embedded \(B_{n,1}\). Therefore the Step-104 rows with “no extending sign choice” do not describe the realization; they show that the script's formula \(j=\sum\varepsilon_iv_i\) is not the actual boundary map. It also ignores the factor two between spin\(^c\) twist and determinant.

The table in `data/step104/character_analysis.json` is retained only as a record of that misidentification. The valid statement is the one Step 103 recorded: isotropy alone gives no global obstruction.

**104.M is downgraded to a route (Question 105.M).** Step 2 is false as written: an extending structure is not thereby basic. Step 3 is also unsupported, because \(|\Phi|^2\le\max(0,-\min_M s)\) is a global bound and does not become local through convergence of \(s\) on compact subsets of \(W\). A corrected route would need all of the following:
- start from one fixed supplied smooth basic class, passing to a subsequence of the finite signed family;
- obtain a global \(L^4\) spinor bound from the integrated Weitzenböck identity and an \(L^2\) bound on \(F_A\) from \(|F_A^+|=|\Phi|^2/\sqrt8\) and the fixed \(c_1^2\);
- use local elliptic estimates on compact subsets of \(W\);
- prove a \(\mathbb Z_{n^2}\)-equivariant removable-singularity theorem;
- identify the limiting boundary holonomy, hence the orbifold character.

Neither the character nor irreducibility of the limit may be assigned before these steps.

---

## 1. Setting

\(M\) is closed and oriented, \(A=c_1^2(X)\), and \(M=X\#k\overline{\mathbb{CP}}^2\), so \((2\chi+3\tau)(M)=A-k\). For a compact region \(D\) with boundary, write
\[
C_+(g;D)=\frac1{2\pi^2}\int_D|W^+|^2+\frac1{96\pi^2}\int_Ds^2,\qquad \widehat P(g;D)=\frac1{8\pi^2}\int_D|\mathrm{Ric}^\circ|^2 .
\]
Theorem G (Step 33) gives the exact identity
\[
\widehat P(g;D)=C_+(g;D)-(2\chi+3\tau)(D)+\mathcal Q_+(\partial D),\qquad \mathcal Q_+=2\mathcal E-3\mathcal H,
\]
where \(\chi(D)=\int_De+\mathcal E\), \(\int_DL=\tau(D)+\mathcal H\), and \(\mathcal H=\eta+\int T_{p_1}\). Both \(\mathcal E\) and \(\mathcal H\) depend only on the metric near \(\partial D\); reversing the boundary orientation changes their signs.

**Hypotheses (E).** Let \(g_i\) be metrics on \(M\) and \(\Omega\subset M\) an open set.
1. \(g_i\to g_\infty\) in \(C^2_{\rm loc}(\Omega)\), modulo diffeomorphisms. Here \((\Omega,g_\infty)\) is complete with finite volume, has \(s_\infty\) constant and negative, and is Einstein.
2. \(\widehat P(g_i)\to0\), \(\int_M(s_i-\bar s_i)^2\to0\) with \(\bar s_i\to s_\infty\), and \(\mathrm{Vol}(g_i)\to\mathrm{Vol}(g_\infty)\).
3. There is an exhaustion \(\Omega_\rho\uparrow\Omega\) by compact smooth domains, \(\rho\to0\). For each \(\rho\), the components \(C_j\) of \(M\setminus\mathrm{int}\,\Omega_\rho\) have topology independent of \(\rho\), and each meets the ends of \(\Omega\) in a fixed set \(J_j\).

At a nonzero Einstein normalization with \(R\) bounded above and away from zero, \(\mathscr D=(4P+L_s)/R\to0\) gives \(\widehat P\to0\) and scalar variance \(L_s\to0\); local convergence pins \(\bar s_i\to s_\infty\). Total-volume convergence is the additional no-loss hypothesis in (E2). This is the intended structure of Anderson's case III with \(\lambda\ne0\).

---

## 2. Theorem 105.Q (cap-charge identity)

Under (E), for each cap \(C_j\) the limit
\[
c_j:=\lim_{\rho\to0}\lim_{i\to\infty}C_+(g_i;C_j^{(\rho)})
\]
exists and has the following properties.
1. \(c_j=(2\chi+3\tau)(C_j)+\sum_{\ell\in J_j}\mathcal Q_+^\infty(L_\ell)\), where \(\mathcal Q_+^\infty(L_\ell)=\lim_{\rho\to0}\mathcal Q_+(L_{\ell,\rho};g_\infty)\) is computed with \(L_{\ell,\rho}\) oriented as part of \(\partial\Omega_\rho\).
2. \(c_j\ge0\), and the scalar part of the cap energy vanishes in the ordered-limit sense: \(\lim_{\rho\to0}\limsup_i\int_{C_j}s_i^2=0\), while the corresponding limsup and liminf of \((2\pi^2)^{-1}\int_{C_j}|W^+_{g_i}|^2\) both tend to \(c_j\).
3. \(C_+(g_\infty;\Omega)=A-k-\sum_jc_j\). The same argument with \(2\chi-3\tau\) and \(\mathcal Q_-\) gives the identity for \(C_-\).

*Proof.* Fix \(\rho\). Apply Theorem G to \(C_j\) with \(g_i\). The boundary of \(C_j\) is \(-L_\rho\) and lies in the compact set \(\Omega_\rho\), where \(g_i\to g_\infty\) in \(C^2\). The terms \(\mathcal E\) and \(\int T_{p_1}\) are local in the 2-jet. The eta invariant of the odd signature operator depends smoothly on the boundary metric, because the kernel dimension of that operator is topological. Hence \(\mathcal Q_+^{\rm out}(\partial C_j;g_i)\to-\mathcal Q_+(L_\rho;g_\infty)\).

Since \(0\le\widehat P(g_i;C_j)\le\widehat P(g_i)\to0\),
\[
\lim_iC_+(g_i;C_j)=(2\chi+3\tau)(C_j)+\mathcal Q_+(L_\rho;g_\infty).
\]
For the scalar term,
\[
\int_{C_j}s_i^2\le2\int_M(s_i-\bar s_i)^2+2\bar s_i^2\,\mathrm{Vol}(g_i;C_j),
\]
and by (E2) and local convergence,
\[
\sum_j\operatorname{Vol}(g_i;C_j^{(\rho)})\to\operatorname{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]
Thus the limsup of each cap volume is bounded by the Einstein-tail volume, which tends to zero as \(\rho\to0\). For a nested exhaustion, nonnegativity of the \(C_+\)-density makes the fixed-cap limits monotone, hence \(c_j\) exists. The first identity then gives convergence of the **sum** of incident boundary charges. Convergence of each individual end charge requires separate stable collars or Dai–Wei asymptotics. Items 1 and 2 follow in this summed/ordered-limit form.

For item 3, \(C_+(g_i;M)=(2\chi+3\tau)(M)+\widehat P(g_i)\to A-k\). Then
\[
C_+(g_\infty;\Omega_\rho)=\lim_iC_+(g_i;\Omega_\rho)=A-k-\sum_j\lim_iC_+(g_i;C_j^{(\rho)}),
\]
and we let \(\rho\to0\). \(\square\)

**Corollary 105.L (transfer of LeBrun's mixed estimate).** Assume in addition the LeBrun estimate \(\int_M(s-\sqrt6|W^+|)^2\ge72\pi^2A\) for all metrics on \(M\), in the package's scope for general-type \(X\). Then
\[
\boxed{\,9k+8\sum_jc_j\le3A\,}.
\]
This already implies \(k+\sum_jc_j\le3A/8\). With the separate scalar estimate \(\int s^2\ge32\pi^2A\), one also obtains the weaker displayed relation \(k+\sum_jc_j\le2A/3\).

*Proof.* On a cap, \(\int_{C_j}(s-\sqrt6|W^+|)^2\le(\|s\|_{L^2(C_j)}+\sqrt6\|W^+\|_{L^2(C_j)})^2\to12\pi^2c_j\), by item 2. On \(\Omega\), write \(\int s^2=96\pi^2x\) and \(\int|W^+|^2=2\pi^2y\), so \(x+y=C_+(\Omega)\). Then
\[
\int_\Omega(s-\sqrt6|W^+|)^2\le12\pi^2(\sqrt{8x}+\sqrt y)^2\le108\pi^2(x+y)=108\pi^2(A-k-\textstyle\sum c_j).
\]
Adding the two estimates gives \(72\pi^2A\le108\pi^2(A-k-\sum c)+12\pi^2\sum c\), which is the boxed inequality. The second inequality comes from transferring \(\int s^2\ge32\pi^2A\), which gives \(x\ge A/3\). \(\square\)

When there are no caps, this is the inherited smooth statement \(k\le A/3\). Every cap of positive charge tightens it, and zero-charge caps are invisible. This is the charge principle stated precisely: **the visibility of a degeneration to the global Einstein gap is the \(C_+\)-charge \(c\) of the region it removes.** The corollary is the analogue, for caps, of the Wahl filler transfer (102.K), where Kähler Ricci-flat ALE fillers have \(c_+=0\).

*Correction to Spirit #119.* The cap does **not** contribute nothing to \(\int(s-\sqrt6|W^+|)^2\). Item 2 shows that a positive-charge cap must concentrate exactly \(2\pi^2c_j\) of \(W^+\)-energy in vanishing volume, so it bubbles; it is not bounded-curvature collapse. With this contribution included, the singleton-cap threshold is \(A/11\), not \(A/12\).

---

## 3. Circle-collapsed ends: topological values of the charge

Assume an end of \(\Omega\) is asymptotic to a fibred cusp in the sense of Dai–Wei, with fibration a circle bundle over a closed surface of Euler number \(e\), computed with the link oriented as \(\partial\overline\Omega\). Then Dai–Wei Thm 3.5 gives:
- the Euler boundary contribution tends to \(0\), so \(\chi(\Omega)=\int\mathrm{Pf}\);
- the Chern–Simons correction tends to \(0\), and \(\mathcal H\to\frac12\,\mathrm a\text{-}\lim\eta=\frac e3-\operatorname{sign}e\) (Thm 5.1; Cor 1.2).

Hence
\[
\mathcal Q_+^\infty=-e+3\operatorname{sign}e,\qquad \mathcal Q_-^\infty=e-3\operatorname{sign}e .
\]
For a cap whose boundary has Euler number \(e_{\rm out}=-e\), oriented as the boundary of the cap,
\[
c=(2\chi+3\tau)(C)+e_{\rm out}-3\operatorname{sign}e_{\rm out}.
\]

**Orientation check against independent model curvature integrals.** For Ricci-flat caps, Theorem G gives \(C_+(C)=c\) exactly. Every row below is verified by the script.

| cap | \(\chi,\tau\) | \(e_{\rm out}\) | \(c\) | independent value of \(C_+\) |
|---|---|---|---|---|
| Taub–NUT, \(W^-=0\) orientation | \(1,0\) | \(-1\) | 4 | \(\frac1{8\pi^2}\int\lvert W^+\rvert^2=1\) |
| Taub–NUT, \(W^+=0\) orientation | \(1,0\) | \(+1\) | 0 | 0 |
| Taub-bolt on \(O(-1)\), blow-up orientation | \(2,-1\) | \(-1\) | 3 | 3 (Step 27) |
| \(A_{m-1}\) multi-Taub–NUT, hyperkähler (\(W^+=0\)) orientation, \(m=1..8\) | \(m,-(m-1)\) | \(+m\) | 0 | 0 |

The last row, valid for every \(m\), fixes the orientation convention of Dai–Wei's \(e\) independently of the eta formula.

**Charges of exceptional caps.** Let \(C\) have \(\partial C=S^3\), \(b_1=b_3=b_2^+=0\) and \(b_2^-=r\); for instance \(C=\#r\overline{\mathbb{CP}}^2\setminus B^4\). Then \((2\chi+3\tau)(C)=2-r\), and
\[
c=\begin{cases}4-r,& e_{\rm out}=-1\ \text{(Taub-bolt chirality)},\\ -r,& e_{\rm out}=+1.\end{cases}
\]
Two consequences follow.
- *Chirality selection.* An exceptional class cannot sit in an \(S^3\) cap that collapses in the \(e_{\rm out}=+1\) chirality, since \(c<0\) contradicts Theorem 105.Q(2).
- *Four-class bound.* In the admissible chirality each \(S^3\)-Hopf cap carries \(r\le4\) classes and charge \(4-r\).

For disk-bundle caps \(D(-p)\) with boundary \(L(p,1)\), \(c=4-p\) in the disk chirality and \(p-2\) in the opposite one. Table: `data/step105/cap_charge_check.json`.

**Corollary 105.H (Hopf-collapse channel at exact status).** Suppose all exceptional topology lies in \(N\) admissible \(S^3\)-Hopf caps carrying \(r_1,\dots,r_N\ge1\) classes, \(\sum r_j=k\), together with \(B\) further positive-charge ball caps of charge \(4\) (zero-charge balls do not change the formula). Then Corollary 105.L gives
\[
9k+8\!\left[\sum_j(4-r_j)+4B\right]\le3A
\iff k+32N+32B\le3A .
\]
- If every class sits in its own cap (\(N=k\)), then \(k\le A/11\). The channel is excluded on \(A/11<k<A/3\).
- If classes are packed four to a cap (\(N=k/4\)) and \(B=0\), the condition is \(k\le A/3\), exactly the smooth one. The four-class Hopf cap has \(c_+=0\) and is invisible to the scalar/\(W^+\) mixed-LeBrun inequality, like the Kähler Wahl filler.

Hence the collapse channel is **not** excluded in the hard range. The estimate permits configurations satisfying \(k+32N+32B\le3A\), including the single-cap \(k=4\), \(B=0\) case for every \(A\ge12\); this is necessary, not sufficient.

**What a zero-\(C_+\)-charge four-class cap must carry.** In the limit \(\int|W^+|^2\to0\), \(\int s^2\to0\), and \(\widehat P\to0\), but the opposite identity gives \(c_-=20\), hence \(\int|W^-|^2\to40\pi^2\). Any smooth noncollapsed curvature-scale limit is therefore ASD Ricci-flat; a simply connected one is hyperkähler. Hypotheses (E) do not by themselves supply a bubble tree or classify every residual region.

The generic \(w_2\) exclusion is withdrawn. The exact matched architecture found at Step 106 is a rank-four D4 ALF core, whose end is \(S^3/Q_8\) and whose link charges are \((-2,2)\), joined to the punctured real rank-two disk bundle over \(\mathbb{RP}^2\). Mayer–Vietoris supplies precisely the index-two odd extension \(-D_4\subset-I_4\). What remains unproved is the relative smooth identification with \(\#4\overline{\mathbb{CP}}^2\setminus B^4\) and a collapsing transition matching the D4-ALF and Hopf collars with vanishing full transition energy.

---

## 4. Status of the three subchannels after this Step

1. **Wahl/Einstein orbifold.** Unchanged from 102.R/102.K/103.I. Existence of a negative non-Kähler, non-locally-symmetric Einstein orbifold is open, and aggregate methods cannot decide it.
2. **\(D_{\ge6}\) prism complement.** Only the necessary data of 96.K are available.
3. **Einstein domain with collapsed or cusp complement.** Theorem 105.Q holds under (E). For circle-fibred cusps, the charges are topological (§3).
   - Singleton exceptional caps are excluded above \(A/11\).
   - The four-class zero-\(C_+\)-charge Hopf cap is not excluded throughout \(k<A/3\), but it has \(c_-=20\). Its matched D4-ALF/punctured-\(\mathbb{RP}^2\)-disk-bundle architecture is topologically and energetically compatible, not constructed.
   - Lens and Seifert ends (orbifold base, e.g. \(L(n^2,n-1)\)), \(T^2\)-fibred or Nil cusps, and caps meeting several ends require their own adiabatic eta values. Dai's general formula, Dai–Wei §5, covers circle bundles over orbifold bases once their orbifold \(L\)-genus terms are computed. These cases are stated, not decided.

The three alternatives remain: positive gap, nonattained zero, or a smooth negative Einstein metric. Case 3 above now carries a proved charge law and a sharp invisible sector.

**Hypotheses not supplied by any theorem in the corpus.**
- That an actual \(\mathscr D\to0\) sequence has the structure (E). This needs Anderson-type extraction with \(C^2_{\rm loc}\) convergence on the Einstein part and no loss of volume into the caps.
- That the ends of \(\Omega\) have Dai–Wei fibred-cusp asymptotics, needed only for the topological evaluation in §3; Theorem 105.Q itself does not use them.
- Cheeger–Gromov: for complete finite-volume metrics of bounded curvature, \(\chi=\int\mathrm{Pf}\) and the eta limit exists. This makes \(\mathcal E\to0\) general, but the value of \(\mathcal H\) is topological only under fibred asymptotics.
