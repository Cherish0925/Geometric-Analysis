# Consolidated hypothesis ledger and theorem chain: Steps 53–58, rewritten in post-Step-70 notation (Step 90)

Session S1003A02. Originally written by Agent2 at Step 58. Rewritten at Step 90 (Agent2, Express) from the Step-89
scientist-reader verification `trace/ttcs/results/step89_ttcs01_verifier1_integration.md` §4. The authoritative
integrated record is `workspace/notes/theorem_package_v1.md` (§§13–20, 22.6, 24); where this ledger and the package
differ, the package governs. Per-step derivations remain in their original notes (`step53_…`, `step54_…` [proof body
rewritten at Step 90], `step55_…`, `step56_…`, `step57_…`, `step59_…`, `step61_…`).

**Conventions (post-Step-70).** \(P(g)=\int|\mathrm{Ric}^\circ|^2\);
\[
P_*(M)=\inf_gP(g),\qquad P_{*,\rm orb}(V)=\inf_{g\ \text{orbifold}}P(g),\qquad
\alpha(M)=\inf_g\mathscr D(g),\quad \mathscr D=\frac{4P+L_s}{R}.
\]
All Anderson selection, energy and replacement statements below concern \(P_*\), never \(\alpha\). Finite covers
multiply \(P\) and leave \(\mathscr D\) invariant. \(T_+=2\chi+3\tau\), \(A=c_1^2(X)\) for the minimal model,
\(\mathbf R^\pm=W^\pm+\frac s{12}I\); eigenvalues \(\mu_i\) of \(\mathbf R^+\). The older notation \(p_*\), \(\alpha_{\rm orb}\) in
the Step 53–58 notes means \(P_*\), \(P_{*,\rm orb}\).

---

## I. Hypotheses

All refer to a sequence of unit-volume metrics \((M,g_i)\) with \(P(g_i)\to P_*(M)\), on \(M=X\#k\overline{\mathbb{CP}}^2\).

**(I)** Anderson case (I): an \(\varepsilon\to0,\ p\to1\) subsequence of minimizers of
\(Z^{2p}_\varepsilon=P+\varepsilon\int(1+|\mathrm{Ric}|^2)^p\) converges (orbifold Cheeger–Gromov) to a multi-component
configuration \((V_a,g_0)\cup(N_k)\), with \(V_a\) compact orbifold bulk components and \(N_k\) ALE bubble regions at
separated smaller scales. Reference: Anderson, *Canonical Metrics on 3- and 4-Manifolds*, Thm 4.10, used as a published
statement with three named soft spots (local minimality of weak limits; Prop. 4.6 regularity and its uniformity under
rescaling; the case-(I) equality (4.43) by citation). This selects **some** \(P\)-minimizing sequence; it says nothing
about \(\mathscr D\)-small sequences, whose normalized nonzero scale Anderson's selection need not preserve (package §20.5).

**\(\mathrm H_{\rm sm}\)** (smooth cone points): every cone point of \(V\) has trivial group. (The alternative is orbifold
absorption, §III.B.)

**\(\mathrm H_{\rm lsc}\)** (lower semicontinuity): \(P_*(M)\ge\sum_aP(V_a,g_0)+\sum_kP(N_k)\). Standard for weak \(W^{2,2}\)
convergence on compact sets at separated scales.

**\(\mathrm H_{\rm dec}\)** (decay): each bubble \(N_k\) is smooth, complete, AE with derivative-controlled decay of some order
\(\tau>0\), and scalar-flat. Used for PSC of the all-end compactification (Lemma 53.Y, any \(\tau>0\), every end filled)
and for the charge formula.

**\(\mathrm H_{\rm eq}\)** (energy equality): \(P(g_i)=\sum_aP(V_a,g_{i,a})+\sum_kP(N_k)+o(1)\). Anderson (4.43); standard
in bubble-tree theory but not proved for the fourth-order system without extra input.

**\(\mathrm H_{\rm rem}\)** (removability): \(g_0\) extends smoothly across trivial-group cone points. Used only for
attainment.

**Bubble \(P\)-criticality (analytic input, corrected by Step-54 §5(c)).** Compact replacement yields bubble
\(P\)-criticality **when an actual \(P\)-minimizing sequence converges strongly enough at bubble scales**. The unresolved
analytic inputs are that strong bubble-scale convergence and derivative-controlled AE decay. Proposition 54.4 (scaling
identity under \(\mathrm H_{\rm eq}\)) is an alternative conditional argument, not an unconditional proof that the rescaled
perturbation vanishes.

**(SW\(_L\))** two-sided form: SW vanishes for splittings along an \(L\)-space with \(b^+\ge1\) on both sides
(\cite{agolhyperbolic} with Lin's proof; lens spaces and spherical space forms are \(L\)-spaces). The **one-sided** form
(PSC orbifold cap \(+\) \(b^+\ge1\) on the other side) remains a hypothesis. It is not used in the ball-quotient
smooth-bubble theorem 54.A (Γ-vertex proof, §III.A), and is not discharged by Lemma 54.3.

**(N\(_0\))** (Ricci-flat orbifold bubbles): every bubble at a point with nontrivial group is Ricci-flat ALE, \(P=0\).
Eliminates non-Ricci-flat orbifold channels by fiat.

**(U)** (upper input). For ball quotients the analytic CH-collar cell proves \(P_*(M_k)<8\pi^2k\) on every fixed host
(supplement Ch. 5, every fixed collar radius). The certified numerical cell, \(P/(8\pi^2)\le0.995662732771115\),
supplies its quantitative endpoint **only where its collar fits** (injectivity-radius hypothesis); it is not a uniform
bound over all ball quotients. For arbitrary minimal general-type hosts the strict upper theorem is Corollary 59.KE
(KE canonical model, Kronheimer/ALE localization, \(\varepsilon\) fixed before \(\lambda\)):
\(P_*(X\#k\overline{\mathbb{CP}}^2)\le8\pi^2k(1-\tfrac{s^2}{64}\varepsilon^2\log\tfrac1\varepsilon+C\varepsilon^2)<8\pi^2k\).

---

## II. Proved results

**Theorem K\(_\infty\) (Kähler infimum).** For any minimal compact general-type surface \(X\) and \(k\ge1\),
\(\inf_{\text{fixed-complex Kähler}}P=8\pi^2k\), not attained for \(k>0\). Hodge index on total-transform exceptional
classes gives the lower bound; successive Arezzo–Pacard cscK blow-ups on the canonical orbifold give recovery. Scope:
fixed complex structure only.

**Theorem 59.R (second-order Burns expansion; supersedes the formal Theorem 57.Φ and its open remainder).** If
\(E_P(g)=0\) on a ball containing the whole insertion support, \(\zeta\in\Lambda^+_p\) a unit vector and \(K\) a smooth
degree-0 corrector, then
\[
P(\widetilde g_\varepsilon)=P(g)+8\pi^2-8\pi^2\varepsilon\,\mathbf R^+_p(\zeta,\zeta)
+4\pi^2\Phi(\mathrm{Rm}_p,\zeta,K)\,\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]
No eigenvector hypothesis is needed for the expansion. When \(\mathrm{Ric}^\circ_p=0\) and \(\zeta\) is an eigenvector,
\[
\Phi_{\rm opt}=-\tfrac12\mu_1(\mu_1-\mu_2-\mu_3)-\tfrac12(\mu_2-\mu_3)^2,
\]
attained by \(K^*+k_0^W\); the logarithmic \(W^-\) and \(\mathrm{Ric}^\circ\) corrector sectors are closed (Schur
cancellation plus A01's exact \(k_0^W\); the \(\mathrm{Ric}^\circ\) zero is exact, A01 Step 53). The theorem does **not**
assert the same optimized statement on arbitrary non-\(P\)-critical backgrounds. Source:
`step59_rigorous_burns_expansion_and_zero_gap_structure.md` (Part D binding), package §20.1. The Step-57/58 numerical
cross-checks (−18 on CH; eight product backgrounds at \(10^{-15}\); A01 #830 for KE) remain valid consistency evidence.

**Corollary 59.KE (strict upper bound).** For every minimal surface of general type and every \(k\ge1\),
\(P_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k\), with the displayed rate in (U); hence also
\(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/(A+k)\) (Theorem 69.KE). Upper bounds only.

**Proposition 56.U (zero-energy upper bound).** For a compact 4-orbifold \(V\) with Wahl points and Milnor-fibre
smoothing \(M'\): \(P_*(M')\le P(V,g)\) for every smooth orbifold metric, and by Lemma 86.S also
\(\alpha(M')\le\mathscr D(V,g)\). The smoothing error in \(P\) is \(O(\lambda^2)\) (Şuvaina's ALE metrics, \(\tau=4\)).

**Corollary 56.B (corrected).** A compatible Ricci-flat ALE resolution or Wahl smoothing of an Einstein orbifold gives
\(P_*(M')=0\). If the Einstein constant is nonzero, Lemma 86.S also gives \(\alpha(M')=0\). A Ricci-flat bulk alone gives
no \(\alpha\)-conclusion (its naive glued family has \(\mathscr D\to4\)). When \(M'\) is a general-type blow-up, the
negative-Yamabe exclusion (\(-\|s^-\|_2\le Y([g])\le-4\pi\sqrt{2A}\)) forces the Einstein constant to be negative, within
these derivative-controlled resolution/smoothing constructions. The orbifold is non-Kähler if its bulk would be complex
with those quotient singularities (Prop. 55.6 repaired); lattice law \(n\) odd or \(8\mid n\).

**Theorems 87.O and 93.A (exact paired-\(A_1\) orbifold laws; package §22.6(6)).** For a ball quotient \(X\),
\(V_m=X\#m(S^4/\mathbb Z_2)\), and \(k=2m\),
\[
d_{*,\rm orb}(V_m)=4\pi^2(A/3-k),\quad P_{*,\rm orb}(V_m)=8\pi^2k,\quad
\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}.
\]
The signature bound and the scalar bound transferred from the smooth EH resolution are absolute on this fixed \(V_m\); the Green-football caps realize all three infima. The \(P\)-infimum is never attained, and \(\alpha_{\rm orb}\) is nonattained except possibly at \(k=A/3\). No \(V_m\) carries an Einstein orbifold for any \(m>0\). This is not an upper bound for all smooth metrics on the resolution (Theorem 74.W crosses \(1/3\) at finite scale); other orbifold topologies need separate information.

**Theorems 95.S, 95.F, Lemma 96.Ş, Theorem 96.K (transfer through Kähler Ricci-flat fillers; package §22.6(7); necessary conditions).** Hypotheses: compact ball quotient \(X\) (aspherical, torsion-free \(\Gamma\)); compact negative Einstein orbifold \(V\) with isolated spherical-space-form points, each resolved by a Ricci-flat ALE filler with orientation-matched equivariant end chart and derivative-controlled decay (86.S), orientation-preservingly diffeomorphic to \(X\#k\overline{\mathbb{CP}}^2\); finite filler \(\pi_1\); transferred scalar/mixed SW inequalities. (95.S, any minimal general-type host) \(9C_-+2C_++42k+12(3c_2-c_1^2)\ge0\); for ball quotients and Kähler fillers \(S_{\rm cx}+\frac29S_{\rm rev}\le k/6+k_b\), and \(S_{\rm cx}\le k_b+\beta(k,A)\) for complex-oriented ones; \(k_b\) is a rank deficit and the inequalities are class-blind once they pass. (95.F) Full-rank root systems in \(I_k\) are sums of \(D\)-blocks; \(E_{6,7,8}\) never embed. (96.Ş, extended Step 98) \(H_2(N)\cong A_{d-1}(-1)\), torsion-free, \(H_1=\mathbb Z_n\), for every non-simply-connected Kähler Ricci-flat ALE filler, including the minimal resolutions of singular invariant fibres in Şuvaina's Theorem B (equivariantly diffeomorphic to smooth-fibre models). (96.K) Full absorption (\(k_b=0\)) by Kähler fillers requires a Kronheimer \(D_{a\ge6}\) filler, \(k\ge6\); at \(k=6\) a lone \(D_6\), \(A\ge3675/64\). Survivors need prism-manifold gluing, a compact complement and a negative Einstein metric; none is known. Decay for Kronheimer \(D/E\) fillers: Bando–Kasue–Nakajima \cite{lidimensional}.

**Proposition 98.W, Corollary 98.V (integral gluing of Wahl balls; repaired Step 99) [P; step96 note §3].** Hypotheses: \(X\) aspherical with torsion-free \(\pi_1\); disjoint embedded Wahl balls with connected complement. The boundary map vanishes; \(\operatorname{coker}(H_2W\to H_2M)=\oplus\mathbb Z_{n_j}\); torsion is carried isomorphically; the free complement lattice has index \(\prod n_j\), and its discriminant form equals the boundary linking form even when \(H_1(X)\) has torsion. The host lattice splits off, leaving \(L_0\subset-I_k\). Corollary 98.V gives uniform realization for \(k\ge4t\), while explicit low-rank obstructions remain; `step99_wahl_four_coordinate_check.py` verifies 158 one-point cases through \(n=16\). Compatible linking already supplies the abstract primitive resolution-chain embedding and recovers 55.5 at \(k=1\). Remaining inputs are geometric realization, characteristic/spin\(^c\) refinements, and singular curvature data. This replaces the former Question 96.W.

---

## III. Conditional results

### A. Smooth-bubble exclusion and attainment (ball quotient, \(b^+(X)\ge3\))

**Theorem 54.A.** Let \(X\) be a compact ball quotient with \(b^+(X)\ge3\) (all but the fake projective planes),
\(M=X\#\overline{\mathbb{CP}}^2\). Under **(I)**, \(\mathrm H_{\rm sm}\), \(\mathrm H_{\rm lsc}\), \(\mathrm H_{\rm dec}\):

(i) every bubble is one-ended with cap a homotopy sphere; the bulk is connected and carries \(E\);

(ii) the bulk \(V\) is homeomorphic to \(M\), \(M\cong V\#\Sigma\); each \(P(N_k)<8\pi^2\).

Under also \(\mathrm H_{\rm eq}\), \(\mathrm H_{\rm rem}\): \(g_0\) attains \(P_*(V)\) and \(P_*(M)=P_*(V)+\sum P(N_k)\); if all caps
are standard, there are no bubbles and \(g_0\) attains \(P_*(M)\). In all cases \(s_{g_0}<0\) is constant and \(g_0\) is
Einstein or a smooth non-Bach-flat global \(P\)-minimizer.

*Proof order (Γ-vertex; Steps 87–90, `step54_k1_ball_quotient_attainment_theorem.md` §2).* Unique closed capped vertex
\(Y\) carrying \(\Gamma=\pi_1(X)\); degree-one pinch \(q:M\to Y\) and \(c\simeq f_Y\circ q\) make \(Y\) essential with
\(b^+(Y)\ge3\); \(\mathrm H_{\rm dec}\) + all-end Lemma 53.Y + Mantione–Torres Prop. 2 \cite{mantionegeographya} make \(Y\)
bulk; ordinary connected-sum vanishing gives \(b^+=0\) on every bubble; the charge bound and Freedman give (i)–(ii);
essentialness, Bourguignon (\cite{kotschick2004monopole}, appendix) and virtual abelianness
(\cite{barbara2020fundamental}, Thm 2.7) give \(s<0\). Lemma 54.3 and \(SW_{V\#\Sigma}=SW_V\) are not used.

### B. Orbifold-category attainment (\(k=1\), ball quotient)

**Theorem 56.A.** Under **(I)**, \(\mathrm H_{\rm lsc}\), \(\mathrm H_{\rm dec}\) (any group), bubble \(P\)-criticality (§I),
**(SW\(_L\))** one-sided, smooth orbifold regularity, **(N\(_0\))**:

(i) \(P_*(M)=P_{*,\rm orb}(V)=P(V,g_0)\). Orbifold points are cyclic with Ricci-flat rational-ball bubbles.

(ii) \(s_0<0\) constant (LeBrun's \(\int s_-^2\ge32\pi^2c_1^2(X)\) on \(M\) via reassembly).

(iii) \(g_0\) is Einstein or non-Bach-flat. In the Einstein case \(P_*(M)=0\), and \(\alpha(M)=0\) because the Einstein
constant is nonzero (here negative), by Lemma 86.S.

(iv) Wahl points: lattice law, non-complex, degree-one kernel.

### C. Minimizer rigidity (Corollary 59.Rig; conditional on the ledger and 53.B relocation)

Under the relocation hypotheses, a minimizing bulk carrying Burns-type bubbles has \(\mathbf R^+\le0\). On a general
\(P\)-critical bulk the kernel restriction is
\[
|T|^2\le Q_{\rm Ric}(\mathrm{Ric}^\circ_p).
\]
Only in the Einstein specialization does it force \(\mu_2=\mu_3\) on a kernel direction (\(\lambda_{\max}(\mathbf R^+)=0\)) and
the strict bound \(|W^+|^2<s^2/24\) when \(s<0\); in particular an Einstein minimizing bulk has no KE-type point
(eigenvalues \((s/4,0,0)\), \(s\ne0\)). A01's Lemma 52.C needs an Einstein bulk; 53.B gives only a \(P\)-critical one.

### D. General \(k\) (any ball quotient with \(b^+\ge3\))

Under (I), \(\mathrm H_{\rm sm}\), \(\mathrm H_{\rm lsc}\), \(\mathrm H_{\rm dec}\): all bubble caps are simply connected with
\(b^+=0\) (Γ-vertex Steps 0–2 apply for every \(k\)), \(H_2\) of bubbles lies in \(\mathrm{span}\{E_1,\dots,E_k\}\), the total
exceptional rank in smooth bubbles is \(<k\), and the bulk is connected as soon as \(P_*(M_k)<32\pi^2\). Attainment for
\(k\ge2\) needs strict subadditivity \(P_*(M_k)<P_*(M_{k-m})+8\pi^2m\) at bulk minimizers.

---

## IV. Open inputs

1. **Analytic.** Strong bubble-scale convergence of an actual \(P\)-minimizing sequence and derivative-controlled AE
   decay (the content of \(\mathrm H_{\rm dec}\) and bubble criticality); \(\mathrm H_{\rm eq}\); \(\mathrm H_{\rm rem}\).

2. **Orbifold absorption.** (N\(_0\)) removes non-Ricci-flat orbifold channels by fiat; removing it requires pricing
   non-Ricci-flat orbifold bubbles. Ordinary paired-\(A_1\) football absorption over ball quotients is solved by 87.O/93.A and cannot be Einstein at any ratio; any remaining absorbing Einstein orbifold for a general-type blow-up is negative-Einstein, non-Kähler, and has different singular/topological data. Over ball quotients with Kähler fillers this data is now constrained by 95.S/96.K: full absorption needs a Kronheimer \(D_{\ge6}\) filler; retained-rank and Wahl configurations need singular input beyond aggregate transfer. Bilinear gluing can exclude low-rank Wahl configurations but is uniformly realizable for \(k\ge4t\) (98.W/98.V); geometric realization and refined/singular information remain. Whether a
   compact negative non-Kähler Einstein orbifold resolving to \(X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\), exists is open.

3. **Collapse.** Anderson case (II). Free-circle regions are spin and cannot carry the odd class \(E\); ball-quotient
   \(\pi_1\) is freely indecomposable, fibre images cyclic. Missing: finite-isotropy control, graph-manifold interface
   splitting, adiabatic \(\eta\)-analysis.

4. **Exotic homotopy-sphere caps.** Would also disprove smooth 4D Poincaré.

5. **Remainder on non-\(P\)-critical backgrounds.** Theorem 59.R closes the \(P\)-critical case; batch gluing and
   moving backgrounds at fixed density (the balanced lower matching) remain open.

6. **One-sided SW\(_L\)** outside the Γ-vertex argument.

---

## IV′. Zero gap without nearby Einstein metrics: spherical and hyperbolic orbifold resolutions

**Proposition 58.O (corrected \(\alpha\)-reading).** Let \((V,g_o)\) be a compact spherical or hyperbolic 4-orbifold with
isolated singular points of type \(\mathbb R^4/\Gamma_j\), \(\Gamma_j\subset SO(4)\) acting freely on \(S^3\) and conjugate in
\(O(4)\) to the end group of a Ricci-flat ALE space \(N_j\) (EH for \(\{\pm1\}\); Kronheimer ADE; Şuvaina class T), with
derivative-controlled decay and orientation-matched equivariant end charts. Let \(M'\) be the resolution. Then
\(P_*(M')=0\) and \(\alpha(M')=0\).

*Proof.* \(g_o\) is Einstein with nonzero constant. The ALE gluing gives \(P\to0\) (error \(O(\lambda^2)\)); Lemma 86.S
supplies the additional control of \(V,\int s,\int s^2,R,L_s\) at \(O(\rho^4)\), \(\rho=\varepsilon^{\tau/(\tau+2)}\), so
\(\mathscr D(g_\varepsilon)\to\mathscr D(g_o)=0\) with \(R\to4\Lambda^2V_{\rm orb}>0\). The earlier \(P\to0\) argument alone does not
give \(\alpha=0\). \(\square\)

Attainment of \(\alpha(M')=0\) is equivalent to existence of an Einstein metric with nonzero Einstein constant on \(M'\).
If at least one singular point is \(\mathbb R^4/\mathbb Z_2\), Ozuch's theorem (\cite{ozuch2021integrability}, Thm 0.9)
excludes a **sequence of Einstein metrics on \(M'\) converging in the Gromov–Hausdorff sense** to \((V,g_o)\). No
quantitative distance is supplied ("GH-far" in the Step-58 text is withdrawn).

Example: \(S^4/\{\pm1\}\) resolves to \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\); hence
\(\alpha(\mathbb{CP}^2\#\mathbb{CP}^2)=0\), attainment is equivalent to Einstein existence on \(\mathbb{CP}^2\#\mathbb{CP}^2\) (open),
and these degenerations are not limits of Einstein metrics.

**Target 58.Q → Theorem 61.EH (package §20.6).** The quantitative EH obstruction in \(P\) is now proved on weighted
gluing neighbourhoods: \(\pi^2a^4(|\mathbf R^+_p\zeta|-\varepsilon_w)_+^2\le\inf P\le\pi^2a^4|\mathbf R^+_p\zeta|^2+O(a^6)\) (upper
side via Ozuch Lemma 2.3), with \(P=O(a^8\log)\) when \(\mathbf R^+_p\zeta=0\). These are \(P\)-rates on neighbourhoods; the
second-order kernel rate, the \(A_n\)/Wahl extensions, and passage to arbitrary sequences are open. For \(\Lambda\ne0\) the
\(\alpha\)-rate is \(\mathscr D\le(4P+L_s)/R\), \(R\to4\Lambda^2V\); \(L_s\) on Ozuch's metrics is not computed.

---

## V. What is not proved

- Any unrestricted positive gap (\(P_*>0\), equivalently \(\alpha>0\)) on a fixed \(X\#k\overline{\mathbb{CP}}^2\),
  \(0<k<A/3\), outside the inherited N1 actual-supply window.
- A fixed-manifold zero-infimum construction in that range, or a decision on Einstein existence there.
- A universal \(k^2/A\) lower bound, or a closed family realizing \(P/k\to0\).
- An unconditional Anderson decomposition or smooth minimizer on \(X\#\overline{\mathbb{CP}}^2\).
- An unconditional O10 finite-block theorem.
- Any topology-only or field-free per-class tariff.

### Step 102 entry (Wahl orbifold realization; `notes/step102_wahl_orbifold_realization_and_K2_invariance.md`)
- 102.R [P*; embeddings from \cite{parksmoothly}]: actual disjoint \(B_{n_j,1}\subset X\#k\overline{\mathbb{CP}}^2\) for \(k\ge\sum\kappa(n_j)\), orbifold \(V\) with degree-one map to \(X\). Hypotheses: none beyond PPS 4.3/4.4; 98.W lattice identification needs aspherical torsion-free \(\pi_1(X)\).
- 102.K [P; part (d) quotes the orbifold–resolution SW correspondence]: \(K^2\)-invariance, filler transfer of LeBrun scalar/mixed bounds to all orbifold metrics on \(V\), no KE orbifold on \(V\). Existence of a non-Kähler negative Einstein orbifold metric on \(V\) with \(A>3k\): **open**; would give \(\alpha(M)=0\) via 86.S.
- Written by Agent2 at Step 102; not yet independently read.


### Step 103 entry (independent reading of 102.R/102.K; isotropy lemma; `notes/step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`)
- 102.R and 102.K(a)–(c): independently verified by Agent4 at Step 103, including orientation, resolution type and defect sign. Ordinary/orbifold group distinction noted. Part (d): cohomology proved; blanket SW correspondence conditional and unused.
- 103.I [P]: isotropy at \(1/n^2(1,n-1)\), \(n\ge3\), forces both Weyl blocks to have a repeated eigenvalue. No local obstruction. Exact script `scripts/step103_wahl_isotropy_and_signature.py` verifies \(n=3\) through \(n=64\).
- 103.L [P]: CH/Kähler locally symmetric type excluded; RH type excluded for \(\tau_{\rm orb}\ne0\); corrected formula \(\tau_{\rm orb}=A/9-k+\frac23\sum(1-n_j^{-2})\).
- Known non-Kähler Einstein constructions (Fine–Premoselli, Anderson–Bamler, KE/cscK) assessed and found inapplicable.

### Step 104 entry (character analysis and cusp reduction; `notes/step104_character_computation_and_cusp_reduction.md`)
- [WITHDRAWN at Step 105] 104.C [P]: the filler-transfer estimates do not use an orbifold monopole; extending spin\(^c\) classes have \(j=0\) where A01 isotropy is trivial; the isotropy route is dead. Script `scripts/step104_character_analysis.py` → `data/step104/character_analysis.json`.
- 104.M [P, modulo equivariant removability]: shrinking-filler limit gives orbifold monopole in extending structures.
- [WITHDRAWN at Step 105] 104.F [P]: cusp/F-structure channel collapses to orbifold case for ball-quotient hosts (\(\Gamma\) Gromov-hyperbolic, no \(\mathbb Z^2\)). Nonattained-zero alternative has exactly two subchannels: Wahl orbifold and \(D_{\ge6}\) prism complement.

### Step 105 entry (corrections and cap-charge law; `notes/step105_cusp_channel_restored_and_cap_charge_theorem.md`)
- 104.C WITHDRAWN (no supplied j=0 field; character rows reflect a misidentified boundary map). 104.F WITHDRAWN (only injective Z² cusp groups excluded; cusps/collapse remain). 104.M downgraded to Question 105.M (fixed basic class, global L⁴/F_A bounds, equivariant removability, holonomy identification).
- 105.Q [P under (E): C²_loc convergence to finite-volume Einstein Ω, P̂→0, scalar variance→0, volume convergence, stable nested cap topology]: c_j=lim C_+(cap)≥0, scalar part →0 in ordered limits, C_+(Ω)=A−k−Σc_j. For a cap meeting several ends, only the sum of incident Q_+ limits follows without separate end asymptotics; cap-volume control uses the total tail volume.
- 105.L [P, + LeBrun mixed estimate on M]: 9k+8Σc_j≤3A (hence k+Σc_j≤3A/8). The older 2A/3 relation uses the separate scalar estimate.
- 105.H [P, + Dai–Wei fibred circle cusps]: Q_+^∞=−e+3 sign e; S³-Hopf cap with r classes: c_+=4−r (Taub-bolt chirality; other chirality impossible), r≤4. With N exceptional caps and B charge-four ball caps, k+32N+32B≤3A; singleton caps excluded for k>A/11. A four-class cap has c_+=0 but c_−=20 and ∫|W−|²→40π². Orientation verified on Taub–NUT (both), Taub-bolt, A_{m−1} ALF (`data/step105/cap_charge_check.json`).
- Independently read and repaired by Agent4 at Step 106 (`notes/step106_independent_cap_charge_and_D4_candidate.md`; TTCS integrations `trace/ttcs/results/step106_ttcs01_verifier{1,2}_integration.md`). Exact live architecture: rank-four D4 ALF core (−D4, end S³/Q8, charges (−2,2)) plus punctured RP² disk bundle giving the index-two extension to −I4. Topologically/energetically compatible; relative smooth type and collapsing metric transition open. Chen–Chen does not exhaust all bubbles under (E).

### Step 107 entry (Einstein-end constraints; independently read and repaired Step 108; `notes/step107_einstein_end_constraints_D4_object_and_specification.md`, `notes/step108_independent_reading_and_synchronized_close.md`)
- Step-106 D4 ledger rerun: `data/step106/D4_cap_ledger.json` all_ok; JSON now records the Theorem-G orientation convention (cap-outward (−2,2), Ω-outward (2,−2)).
- 107.A [P, under relative metric/Ricci convergence to a fixed-base circle-fibred cusp model; relative C² suffices, Dai–Wei rescaled smoothness alone does not]: Einstein ⇒ λ=−κ², fibre length constant, K_B=λ; base hyperbolic. Fixed S²/Euclidean-T² bases are impossible; shrinking-base CH/RH cusps are untouched. Exact model Ricci checked and rerun in `scripts/step107_cusp_end_constraints.py`.
- 107.A′ [P, + (E) + Dai–Wei charges + smooth-base SW adjunction supply]: c_+=T_+(C)+e−3 sign e over Y_{g,e}, g≥2; ordinary one-surface disc-bundle caps c_+=4−4g+e are excluded when b_+>1 supplies the blow-up basic class (or with stated chamber input). Seifert-orbifold bases and multi-class caps remain open.
- 107.B [P]: no complete finite-volume spherical end whose lift is biaxial, with |Rm|≤K and G(ν,ν)≥0. 107.C [P]: same for diagonal Bianchi IX with liminf σ₂>0 (sufficient: anisotropy (a₁²−a₂²)²/(a₁²a₂²a₃²)<3). Finite-energy replacement of |Rm|≤K uses the quoted unit-scale Einstein ε-regularity theorem. The symmetry-free Hopf-end volume-growth theorem remains open.
- D4 object: Donaldson/Freedman give only N_D4∪W homeomorphic to #4CP̄²; smooth/relative-plumbing type open. Transition, Einstein host and global gluing all remain open. D4-1 should be pursued only while a Hopf host survives.
- Written by Agent2 at Step 107; one TTCS branch completed (the second/integration timed out); independently read and repaired by Agent4 at Step 108.
- TTCS-107 (one complete branch, `trace/ttcs/results/step107_ttcs01_sub1_verifier.md`; second branch/integration timed out): computations of 107.A–C confirmed; scope repairs incorporated — 107.A′ needs relative C²/Ricci asymptotics, not merely Dai–Wei rescaled smoothness; 107.B concerns ends with biaxial U(2)-invariant lift; D4 items are necessary components of this proposal, not an iff; "minimal resolution" form needs relative identification of N_trunc with the D4 plumbing; Donaldson gives Q(M4)=−I4 directly; Seifert-orbifold-base caps not covered by the disc-bundle exclusion.
- A01 Step 93 authoritative §8 independently read at Step 108: WFL 93.A [P under explicit metric-wise supply (S)] and index transfer 93.I stand after gauge/bootstrap and exact-index repairs. Marked Prop. 93.Y covers odd n≥3 and n=2, not arbitrary/even-n≥4 embeddings. Only the + package transfers; T_−, local characters, forced zeros, full SW invariants and moduli do not. Forced-zero classes give strict ∫(s−)²>32π²A but no uniform gap; marked λr₀²/bubble-tree control is open.
