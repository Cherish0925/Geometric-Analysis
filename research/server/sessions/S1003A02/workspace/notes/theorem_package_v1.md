# Einstein gaps on four-manifolds: dependence-ordered theorem package (v1)

This file is a research map for the Discovery loop. It records the mathematical objects, proved results, certified computations, numerical structures, and open implications in dependency order. It is not a paper and does not turn construction-level information into a theorem about the unrestricted infimum.

**Front matter.** The current state of the human functional and of Problems 1–4 (proved / inherited / conditional / numerical / open, and what the unresolved centre requires) is `workspace/notes/state_of_problems_1_4.md` (synchronized and independently closed through Step 108).
## 1. Functionals, scale, and distinct questions

Let \(M\) be a closed oriented smooth four-manifold. **The human functional** is the corpus defect
\[
\mathscr D(g)=\mathcal E(g)=\inf_{\lambda\ne0}\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}
=\frac{4P+L_s}{R}\quad(R>0),\qquad \alpha(M)=\inf_g\mathcal E(g),
\]
with \(R=\int|\operatorname{Ric}|^2\), \(L_s=\int(s-\bar s)^2\), and \(\mathcal E=4\) when \(\int s=0\) (in particular at Ricci-flat metrics, which are maxima of \(\mathcal E\)). **The principal instrument** is the trace-free energy
\[
P(g)=\int_M |\operatorname{Ric}^{\circ}_g|^2\,d\mu_g,\qquad P_*(M)=\inf_gP,\qquad \mathfrak p_*=P_*/(8\pi^2)
\]
(the older symbol \(p_*\) is retired; lowercase \(p=P/8\pi^2\) always denotes a dimensionless value at one metric). The field-alignment functionals \(\kappa_\beta\) are a third, distinct object.

**How α and P are joined and where they separate** (canonical notes `step71_functional_split_and_unit_wall.md` and `step72_orientation_free_weyl_deficit_law.md`).

1. *Orientation-free Weyl-deficit identity* [Step 72, from Gauss–Bonnet; equivalent to the inherited chiral identity]. With \(\mathcal W=\int|W|^2\), \(d([g])=8\pi^2\chi-\mathcal W([g])\),
   \[
   \mathcal E(g)-1=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R},\qquad
   \alpha<1\iff\exists[g]:Y([g])\ne0,\ \mathcal W([g])<8\pi^2\chi.
   \]
   If \(\widehat g\) is the Yamabe representative, then unconditionally
   \[
   \alpha=1-6\max\left\{0,\sup_{[g]:Y\ne0}
   \frac{8\pi^2\chi-\mathcal W([g])}{P(\widehat g)+Y([g])^2/4}\right\}.
   \]
2. *Universal ceiling and unit wall* [Step 72]. A smooth \(S^4\) dumbbell with a cylinder \([0,L]\times S^3\), followed by a fixed connected-sum replacement, gives \(\alpha(M)\le1\) on every closed four-manifold. Hence
   \[
   0\le\alpha(M)\le1,\qquad 2\chi\le3|\tau|\Longrightarrow\alpha=1.
   \]
   At equality \(2\chi=3|\tau|\), the infimum is attained exactly by a half-conformally-flat class with nonzero constant scalar curvature; strict Hitchin–Thorpe failure gives nonattainment.
3. *Supply-specific exact bridge* [inherited, `Curvature_Realizability.tex` lines 5765–5871]. If every class carries the stated actual positive monopole projection, every class has a unique scalar-\(-4\) representative \(\widehat g\), and for \(\alpha<1\)
   \[\alpha=\inf_{[g]}\frac{4p(\widehat g)}{p(\widehat g)+A+\upsilon},\qquad Y^2=32\pi^2(A+\upsilon),\qquad p=k-\tfrac43\kappa+\tfrac13\upsilon .\]
   On general-type blow-ups, \(\mathfrak p_*/(\mathfrak p_*+\frac34T_+)\le\alpha\le4\mathfrak p_*/(A+\mathfrak p_*)\). On balanced small-\(h\) families the corpus proves \(\alpha=4\rho+O(h^2)\), \(\rho=\inf P/(8\pi^2A)\).
4. *Separation and attained positive gaps.* \(P\to0\) gives \(\alpha\to0\) only with a nonzero Einstein scale (for Ricci-flat ALE resolution and Wahl smoothing of a nonzero-scale Einstein orbifold this suffices, Lemma 86.S in §13). Ricci-flat bulks, ALE rates and bounded-curvature collapse can be P-only. If \(T_+=0\le T_-\), then \(\mathcal E(g)=1\iff W^+=0\) and \(s\) is a nonzero constant. Thus \(\alpha=1\) is attained by non-Einstein metrics on \(S^1\times S^3/\Gamma\), \(S^1\times H^3/\Gamma\), and \(\#4\overline{\mathbb{CP}}^2\).

Every P-statement below is read through 1–4; statements lacking a nonzero scale or a controlled Weyl-deficit ratio are P-rates, not α-rates.

**Step-86 consistency pass.** §§13–24 were reread against this split. The retired \(p_*\) is replaced by \(P_*\) throughout; the \(P\)-flow bound uses \(P(g_0)-P_*\); Corollary 52.8 is restated with its \(P\)-factor \(\tfrac12\) and its α-form without it (finite covers do not change \(\mathscr D\)); Lemma 86.S (§13) proves that Ricci-flat ALE resolution and Milnor-fibre smoothing preserve \(\mathscr D\) in the limit, so the "vanishing scalar variance" proviso on α-zero conclusions is automatic; Lemma 86.S′ gives the 𝒟-ledger of scalar-flat bubbles; the exceptional-area variable of Theorem AKΓ is renamed \(\varpi\); the capacity is \(\Theta_*(M)\); LeBrun 2001 (\cite{lebrun2001ricci}, Prop. 3.2, Thm 3.3, Cor. 3.4) is the source for the all-\(b^+\) lower bound and Einstein exclusion; the real-hyperbolic scalar-flat exclusion is complete with registered sources (§24.3).

**Step-87/88 integration (independent reading, `trace/ttcs/results/step87_ttcs01_verifier{1,2}_integration.md`).** Lemma 86.S now controls \(\int s^2\) and \(L_s\), requires orientation-matched equivariant end charts and relative-scale bookkeeping for trees, and attributes Wahl decay to \cite{suvaina2011ale}. A Ricci-flat bulk's naive glued family has \(\mathscr D\to4\) (support argument), giving only \(P_*=0\). Whenever a compact Einstein orbifold admits a compatible derivative-controlled Ricci-flat ALE resolution or Wahl smoothing whose smooth result is \(X\#k\overline{\mathbb{CP}}^2\), its Einstein constant satisfies \(\lambda<0\): indeed \(-\|s_g^-\|_2\le Y([g])\le\mathcal Y(M)=-4\pi\sqrt{2A}\), whereas the stated cutoffs over a Ricci-flat or positive-Einstein bulk would give \(\|s^-\|_2\to0\). This concerns these constructed families, not arbitrary near-Einstein sequences. Lemma 86.S′ carries its denominator condition. Theorem 87.O (§22.6(6)) computes the \(S^4/\mathbb Z_2\) orbifold deficit over ball quotients exactly, \(4\pi^2(A/3-2m)\): this channel lands on \(h=1/3\). Theorem 54.A is proved in a Γ-vertex order that uses Mantione–Torres instead of Lemma 54.3. §23.6 records A01's lift-quotient correction (#866).

**Step-89/90 integration (`trace/ttcs/results/step89_ttcs01_verifier1_integration.md`).** Theorem 87.O's closing prose and §24.4 are narrowed: on the fixed \(V_m\) the signature bound is absolute, and no reduction of other orbifold optimizations to marked-cell infima is claimed. The exceptional-area parameter is \(\varpi\) throughout (§3.6); diagonal and unrestricted cell infima are written \(\mathfrak p^{\rm diag}_{1,0}\) and \(\mathfrak P_{1,0}\); §§6.3, 7, 9, 10 and 23.5 carry current status (Theorems 48.L/LY, 59.R, proved diagonal truncation, order-8 witness); §23.6 adds peer #869. The Step-54 proof body is rewritten in the Γ-vertex order (factorization \(c\simeq f_Y\circ q\), all-end compactification), and `step58_consolidated_hypothesis_ledger.md` is rewritten in post-Step-70 notation (56.A/56.B, (U), 59.R replacing 57.Φ, 59.Rig with its Ric° term, 58.O via Lemma 86.S, Ozuch's sequence statement).

**Step-91/92 consistency repairs (Agent4 reading, Step 91).** §14 open borderline now names what remains after 59.R (sign with Ricci-tracefree residual, isotropic kernel \(\mathbf R^+=(0,s/8,s/8)\), moving-background/batch uniformity); §15 withdraws the "\(m\) odd" inference and states the single role of \(\mathrm H_{\rm dec}\) in the Γ-vertex proof; §16 restricts Prop. 55.3 to simply connected regions and carries only the coarse 55.7 trichotomy with the additive budget; §17 writes \(P_{*,\rm orb}\); §19 marks the P-critical remainder as resolved by 59.R; §20.7 replaces the false target \(C_+\ge A\) by uniform positivity of \(p=C_+-(A-k)\), i.e. joint \((\kappa,\upsilon)\) separation from \(4\kappa/3-\upsilon/3=k\). The front matter gives the exact N1 formula and an attribution-free derivation of \(c_2(E)=5\chi+6\tau\ge\chi>0\) for Problem 4.

**Step-93 paired-\(A_1\) transfer (`notes/step93_paired_A1_transfer_review.md`; independent TTCS `trace/ttcs/results/step93_ttcs01_verifier{1,2}_integration.md`).** For \(V_m=X\#m(S^4/\mathbb Z_2)\), \(k=2m\), scalar transfer from the smooth EH resolution and the exact Green-football cap give \(P_{*,\rm orb}(V_m)=8\pi^2k\) and \(\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}\). No additional SW hypothesis or fake-plane exception is needed: LeBrun's Yamabe theorem supplies \(\int(s^-)^2\ge32\pi^2A\), and his metric-wise class selection supplies the mixed estimate for all \(b^+\). A first-variation argument proves that the \(P\)-infimum is never attained; \(\alpha_{\rm orb}\) is not attained unless possibly at \(k=A/3\), where the remaining question is a constant-negative-scalar half-conformally-flat orbifold metric. In particular this fixed paired-\(A_1\) topology carries no Einstein orbifold for any \(m>0\), superseding 87.O's weaker necessary condition \(2m<A/3\). Other orbifold topologies remain open.

**Step-94/95/96 filler screen (`notes/step95_verified_transfer_lattice_thresholds.md`, `notes/step96_suvaina_lattice_and_kahler_filler_theorem.md`; exact certificates `data/step95/filler_lattice_screen_certificate.json`, `data/step96/suvaina_lattice.json`; TTCS `trace/ttcs/results/step95_ttcs01_verifier1_integration.md`).** The Step-93 transfer is carried to every orbifold resolving to \(X\#k\overline{\mathbb{CP}}^2\) by Kähler Ricci-flat ALE fillers (§22.6(7)). Exact results: the host-general envelope \(9C_-+2C_++42k+12(3c_2-c_1^2)\ge0\) from the identity \(9x+3T-(\sqrt{8x}+\sqrt{T-x})^2=2(\sqrt{T-x}-\sqrt{2x})^2\); the ball-quotient budget \(S_{\rm cx}+\frac29S_{\rm rev}\le k/6+k_b\); the signed-support classification of full-rank root systems in \(I_k\) (sums of \(D\)-blocks); Lemma 96.Ş, \(H_2(N)\cong A_{d-1}(-1)\) for every non-simply-connected Kähler filler (smooth-fibre quotients and minimal resolutions of singular invariant fibres alike, Step-97/98 extension); and Theorem 96.K: full absorption by Kähler fillers over a ball quotient requires a Kronheimer \(D_{a\ge6}\) filler, so \(k\ge6\), and at \(k=6\) a lone \(D_6\) with \(A\ge3675/64\). The method's scope theorem (95.S): \(k_b\) is a rank deficit, each retained rank adds one unit of aggregate slack, and once the aggregate budgets pass the transfer carries no class-sensitive information. The retained-rank and Wahl sectors therefore need singular information. Steps 98–99 (Proposition 98.W, repaired Corollary 98.V, §22.6(7)) settle the boundary map and sharpen the integral picture: over an aspherical host with torsion-free \(\pi_1\), the Wahl boundary maps into the complement vanish, the complement lattice has index exactly \(\prod n_j\), its discriminant form is the linking form even when \(H_1(X)\) has torsion, and the host lattice splits off. The bilinear condition can obstruct at low rank but is uniformly realizable once \(k\ge4\) per Wahl point; compatible discriminant gluing already supplies the abstract primitive resolution-chain embedding, recovering 55.5 at \(k=1\). Geometric realization, characteristic refinements and singular analysis remain. Survivors are necessary data, never constructions.

**Step-97/98/99 repairs (independent readings `trace/ttcs/results/step97_ttcs01_verifier1_integration.md`, `trace/ttcs/results/step99_ttcs01_verifier{1,2}_integration.md`; proofs in `notes/step96_suvaina_lattice_and_kahler_filler_theorem.md` §§0, 1, 3 and `notes/step99_independent_verification_and_repairs.md`).**
- Şuvaina's classification includes minimal resolutions of singular invariant fibres. Lemma 96.Ş is extended to them by the equivariant Gibbons–Hawking-centre argument; lattice, \(\pi_1\), end, charge and cost are unchanged, and 96.K stands.
- The former Question 96.W is replaced by Proposition 98.W and the Step-99 repair of Corollary 98.V (§22.6(7)). The discriminant result no longer requires torsion-free \(H_1(X)\); four coordinates per Wahl point suffice uniformly, low-rank obstructions remain, and the abstract second-filling chain condition is a consequence rather than an independent input. The Step-94 norm-four-vector reading is withdrawn.
- Lemma 86.S's decay for Kronheimer \(D/E\) fillers is now attributed to Bando–Kasue–Nakajima \cite{lidimensional}.
- §23.1's attribution follows the front matter.
- Peer A01's canonical-cycle equality remains A01's and unused. The exceptional-curve inequality \(\int_C|\nabla\omega|^2\ge8\pi\,c_1\!\cdot C+|s|\mathrm{Area}(C)\) is LeBrun 2005 Corollary 3.2 rearranged (\(s^*=s+|\nabla\omega|^2\)); Corollary 3.6 supplies a possibly singular or disconnected fixed-\(J\) cycle with \(c_1\cdot C=1\), not necessarily an embedded exceptional sphere \cite{lebruneinsteine}.

**Step-101/102/103 integration (proof notes `notes/step102_wahl_orbifold_realization_and_K2_invariance.md`, `notes/step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`; exact scripts under `data/step102`, `data/step103`).**
- The 93.A nonattainment proof and the Step-99 strengthenings of 98.W/98.V were read independently at Step 101; no repair needed.
- \(D=T_{AK}\) [P*]: with A01's Kim–Blair normalization and the AAD/LeBrun balance \(|s|Q/16=\int|\eta|^2+T_{AK}\), \(s^2V=32\pi^2c_1^2+16T_{AK}\), hence \(D=\int(s^2/24-|W^+|^2)=T_{AK}\) on closed AKE Einstein metrics; \(T_{AK}\ge2\pi^2k\) is LeBrun's scalar bound rewritten.
- A01 Theorem 83.5 [P at exact scope]: noncollapsed, bounded-diameter sequences of exact AKE Einstein metrics with fixed \(s_0<0\) have no \(W^+\)- or torsion-energy concentration; bubbles are orientation-matched Kähler Ricci-flat ALE. Not a statement about near-Einstein sequences for \(\alpha\); \(W^-\)-concentration, collapse and diameter divergence open.
- Mixed Einstein edge [I]: \(D\ge4\pi^2k+\frac{8\pi^2A}9(1-\sqrt{1-3k/A})^2\) for Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\) (Step 93 §4 at \(C_\pm=0\), \(k_b=k\)).
- Theorem 102.R [P, independently read Step 103; embeddings quoted from \cite{parksmoothly}]: for \(k\ge\sum\kappa(n_j)\) (\(\kappa=4\), or \(3\) for \(n=2\)) there are disjoint complex-oriented embedded \(B_{n_j,1}\subset M\) in the exceptional summand; coning gives \(V_{X,\mathbf n,k}\) with degree-one map to \(X\), ordinary \(\pi_1=\pi_1(X)\), resolution \(X\#(k+\sum(n_j-1))\overline{\mathbb{CP}}^2\) by PPS Prop. 5.1, and the lattice data of 98.W. Ordinary and orbifold fundamental groups are not identified.
- Proposition 102.K(a)–(c) [P, independently read Step 103]: \(s(n-1,n^2)=(n^2-1)/(6n^2)\), \(2\chi_{\rm orb}+3\tau_{\rm orb}=A-k\), \(2\chi_{\rm orb}-3\tau_{\rm orb}=T_-(M)-4\sum(1-n_j^{-2})\); transferred scalar/mixed constraints on \(V\) equal the smooth ones, and no Kähler–Einstein orbifold metric exists. In (d), the cohomology sequence with cokernel \(\oplus\mathbb Z_{n_j}\) is proved, but the quoted orbifold–resolution SW correspondence is [C] and unused above.
- Lemma 103.I [P]: at a \(1/n^2(1,n-1)\) point with \(n\ge3\), isotropy rotates the plane orthogonal to a fixed axis in each \(\Lambda^\pm\) through a nonzero non-\(\pi\) angle; hence both Weyl blocks have a repeated eigenvalue at the cone. This is not a local Einstein obstruction. CH/Kähler locally symmetric type is excluded; RH type is excluded whenever \(\tau_{\rm orb}=A/9-k+\frac23\sum(1-n_j^{-2})\ne0\). The blanket formula with \(A/3\) is false.
- Fine–Premoselli branched covers, Anderson–Bamler toral Dehn filling, and KE/cscK smoothing have no entry geometry on the realized Wahl family. This bounded comparison is not a nonexistence theorem; the Wahl sector remains a global non-Kähler Einstein existence problem.
- **Step-104 integration (proof note `notes/step104_character_computation_and_cusp_reduction.md`; script `scripts/step104_character_analysis.py` → `data/step104/character_analysis.json`).**
  - **Step-105 binding correction (`notes/step105_cusp_channel_restored_and_cap_charge_theorem.md`), independently read and repaired Step 106 (`notes/step106_independent_cap_charge_and_D4_candidate.md`; TTCS integrations `step106_ttcs01_verifier{1,2}_integration.md`):** 104.C and 104.F below are WITHDRAWN; 104.M is downgraded to Question 105.M (route only). Reasons: no \(j=0\) supplied field is identified and the 'no extending sign' rows reflect a misidentified boundary map (every smooth spin\(^c\) structure restricts over \(B\)); no-\(\mathbb Z^2\) in \(\Gamma\) excludes only injective cusp groups, not cusps (Dehn filling), images need not be cyclic, non-virtual-nilpotence does not prevent collapse, and case-III Hopf cusps are not orbifold points. Theorem 105.Q [P under (E)] gives \(C_+(\Omega)=A-k-\sum c_j\), \(c_j=\lim C_+(C_j)\ge0\) (pure \(W^+\) concentration). A multi-end cap yields the limiting **sum** of incident charges absent separate end asymptotics, and scalar-cap vanishing uses the total tail volume with ordered limits. Cor. 105.L is \(9k+8\sum c_j\le3A\). Cor. 105.H for Dai–Wei circle cusps has \(\mathcal Q_+^\infty=-e+3\,\mathrm{sign}\,e\); an \(S^3\)-Hopf cap with \(r\) classes has \(c_+=4-r\), opposite chirality impossible; with \(N\) exceptional caps and \(B\) charge-four ball caps the exact condition is \(k+32N+32B\le3A\), so singletons are excluded above \(A/11\). A four-class cap has \(c_+=0\) but \(c_-=20\), hence \(\int|W^-|^2\to40\pi^2\); it is invisible only to the scalar/\(W^+\) estimate. Its matched architecture is a rank-four D4 ALF core (\(-D_4\), end \(S^3/Q_8\), charges \((-2,2)\)) plus the punctured \(\mathbb{RP}^2\)-disk bundle giving the index-two extension to \(-I_4\). Relative smooth identification and a collapsing metric transition remain open. Three subchannels of the nonattained zero remain.
  - **Step-107 Einstein-end constraints, independently read Step 108 (`notes/step107_einstein_end_constraints_D4_object_and_specification.md`, `notes/step108_independent_reading_and_synchronized_close.md`; exact scripts/data rerun all_ok):** Theorem 107.A [P] assumes \(g-g_0=o(1)\) and \(\operatorname{Ric}_g-\operatorname{Ric}_{g_0}=o(1)\) in model orthonormal frames (relative \(C^2\) suffices; Dai–Wei rescaled smoothness does not): a fixed-base Einstein circle cusp has \(\lambda=-\kappa^2\), constant fibre factor and hyperbolic base. It excludes fixed \(S^2\)/Euclidean \(T^2\) bases, not shrinking-base CH/RH cusps. Dai–Wei gives \(c_+=T_+(C)+e-3\operatorname{sign}e\); an ordinary one-surface disc-bundle cap over \(g\ge2\) is excluded under the stated smooth-base SW adjunction supply (\(b_+>1\), or chamber input). Theorem 107.B [P] excludes finite-volume spherical ends whose lifts are biaxial; 107.C [P] excludes diagonal Bianchi IX ends with \(\liminf\sigma_2>0\). Finite energy supplies bounded curvature only via the quoted Einstein ε-regularity theorem. The symmetry-free Hopf-end volume-growth question remains open. For D4, Donaldson/Freedman give only \(N_{D4}\cup W\cong_{\rm homeo}\#4\overline{\mathbb{CP}}^2\); relative smooth type, transition, Einstein host and global gluing remain open. §5 specifies the missing class-sensitive relation.
  - [withdrawn at Step 105] Proposition 104.C [P]: the optimal curvature supply class on \(V\) has boundary character \(j = 0\) (extending); for \(j = 0\), A01's isotropy gives nonzero \(\Phi(p)\). The curvature estimate uses filler transfer, not an orbifold monopole. The isotropy route produces no new curvature information.
  - [replaced at Step 108 by A01 Theorem 93.A at exact supply] Former Question 105.M: under explicit finite metric-wise supply (S), the Lemma-86.S Wahl recovery family has an orbifold SW limit. Abelian removability, equivariance and energy transfer are proved; \(b_+>1\) signed canonical blow-up classes supply (S), while \(b_+=1\) needs chamber input. This does not assert equality of full SW invariants.
    - **A01 Step-93 Wahl field/self-similarity package, independently read at Step 108 (authoritative §8 of `Sessions/S1003A01/workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md`):** WFL 93.A [P under supply (S)] and extendible-index transfer 93.I are sound after the determinant-gauge and Sobolev-bootstrap repairs; the all-\(n\) local-index statement has an exact proof. Proposition 93.Y [P at marked existential scope] realizes odd \(n\ge3\) and \(n=2\) Wahl orbifolds as projective nonminimal general-type orbifolds with non-nef canonical divisor; it does not cover arbitrary embeddings or even \(n\ge4\). Only the \(+\)-chirality package transfers (\(a^2,T_+\), extendible indices, metric-wise supply, scalar/\(W^+\) bounds), not \(T_-\), local characters, forced zeros, full SW invariants or moduli. For \(n\ge3\), forced-zero classes yield strict \(\int(s^-)^2>32\pi^2A\) but no uniform gap; the open variable is the marked scale \(\lambda r_0^2\) and its behavior in a Ricci-flat bubble tree.
  - [withdrawn at Step 105] Proposition 104.F [P]: for ball-quotient hosts, the cusp/F-structure channel collapses to the orbifold case (\(\Gamma\) Gromov-hyperbolic with no \(\mathbb Z^2\); non-spherical cusp cross-sections have \(\mathbb Z^2\subset\pi_1\); total collapse excluded because \(\Gamma\) is not virtually nilpotent). The nonattained-zero alternative has exactly two subchannels: Wahl orbifold and \(D_{\ge6}\) prism complement.

**O10 current status.** The density-free actual-field lower estimate remains unresolved. Section 2.2 supplies the finite-\(\beta\) alignment theorem; §10 adds necessary asymptotics for a hypothetical \(\beta\to\infty,\ \kappa_\beta\to0\) sequence (\(\chi/p\to\infty\), \(p/V\to2/(9\pi^2)\), \(W^-/V\to\infty\)). Neither result supplies the missing density-free endpoint theorem, and nothing in the metric \(P\)-programme substitutes for it.

Research status vocabulary used below:

- **Proved:** analytic argument with its hypotheses recorded.
- **Certified:** a fixed explicit metric or flow is enclosed by interval arithmetic, with exact input data.
- **Numerical structure:** reproducible computation that guides a theorem but is not itself a general theorem.
- **Open:** an implication needed for the unrestricted \(\alpha\)-problem has not been established.

## 2. Actual fields control the regular bulk

### 2.1 Bounded-form interface and linear coercivity — Proved

The inherited bounded-form theorem has the form \((1+B_\psi)d_\psi\ge c(K)\). The I40/I41 estimates retain differential information from an actual field; schematically,
\[
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\}.
\]
Formal Chern--Weil and monopole-number budgets do not imply this estimate. Hence a localization theorem for near-minimizers must carry the actual field, or an equivalent differential object, through regular regions and concentration regions.

Primary paths: `Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex`; `Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`; `workspace/notes/step1_field_compatibility_and_route_portfolio.md`.

### 2.2 Density-free finite-\(\beta\) alignment theorem — Proved

Assume metric-wise conformal monopole supply with \(p\ge A>0\), \(a^2\ge T_+\), and \(T_+\le\theta A\) for \(\theta<3/4\). Then every finite \(\beta\ge2\) has a uniform positive lower bound for \(\kappa_\beta\). The algebra is governed by
\[
a(\theta,\beta)=
\frac{(\frac34-\theta)\beta^2+(\frac12-\frac{11}{4}\theta)\beta+6-\theta}
{\beta(9\beta-\theta+6)},
\]
whose numerator has discriminant
\[
\frac{57}{16}\left(\theta-\frac23\right)
\left(\theta+\frac{142}{19}\right).
\]
At \(\theta=2/3\) it is \((\beta-8)^2/12\). This explains the thresholds \(2/3\), \(\beta=8\), and \(3/4\). The verified Kähler application is restricted to the recorded minimal general-type, \(p_g\ge1\), blow-up setting. This is an alignment theorem and does not imply a positive direct Einstein gap.

Primary paths: `workspace/notes/step4_O10_localization_and_orbifold_test.md`; `workspace/scripts/o10_localization.py`; Step-5 records.

### 2.3 Charged concentration tangents — Proved model calculation

One- and multi-centre Gibbons--Hawking spaces carry genuine solutions of the leading coupled tangent equations, with
\[
\int|\nabla v|^2=8\pi^2m_*k\ell^2,
\qquad
\int|d|v|^2|^2=\frac{16\pi^2}{3}m_*^2k\ell^2.
\]
The \(k\)-centre topology has \(b_2=k-1\) and boundary \(L(k,1)\). These tangents rule out a leading-order density-free Liouville argument; they do not by themselves produce closed-manifold escape sequences.

Primary paths: `workspace/scripts/verify_gh_tangent.py`; `workspace/scripts/gh_multicentre_energy.py`.

## 3. Zero gap, attainment, exact Einstein existence, and entropy-supplied nonexistence

### 3.1 Canonical-model resolutions — Proved construction

For the stated minimal Kähler surfaces of general type, resolving canonical negative Kähler--Einstein orbifolds with shrinking Ricci-flat ALE pieces gives smooth metrics with \(\mathcal E\to0\), hence \(\alpha=0\). The core contribution vanishes because its volume tends to zero even though \(|\operatorname{Ric}+g|^2=4\) there. In this zero-gap class, attainment is equivalent to existence of a smooth non-Ricci-flat Einstein metric on the underlying smooth manifold. Ampleness supplies the canonical Kähler--Einstein case; nef/nonample does not exclude all other complex or non-Kähler Einstein metrics.

### 3.2 Rational-blowdown examples — Proved construction with source attribution

Şuvaina-type generalized rational blowdowns provide further zero-gap manifolds, including simply connected minimal symplectic non-Kähler examples. Exact Einstein exterior, scaled Ricci-flat filler, bounded-curvature shrinking collar, and vanishing filler volume yield \(\alpha=0\). The source establishes non-Kählerness, not absence of every complex structure.

Primary paths: `workspace/notes/step6_theorems_and_O11_rotation.md`; `Knowledge/objects/papers/The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d--f4170b4b9bdb/object.md`.

### 3.3 Real-hyperbolic blow-ups: exact Einstein nonexistence from entropy — Proved

Let \(Y\) be a closed oriented real-hyperbolic four-manifold and \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\). The pinch map \(X\to Y\) has degree one, while
\[
\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.
\]
Kotschick's entropy-strengthened Einstein inequality and its Sambusetti/BCG degree corollary require every Einstein \(X\) mapping with degree \(d\ne0\) to \(Y\) to satisfy
\[
\chi(X)\ge\frac32|\sigma(X)|+|d|\chi(Y).
\]
For the pinch map this would give \(k\ge3k/2\), impossible for every \(k\ge1\). Hence no real-hyperbolic blow-up carries an Einstein metric. This is a new actual supplier beyond monopole classes: the input is homological minimal-volume entropy. It is an exact existence obstruction, not by itself a positive critical-\(L^2\) Einstein-gap theorem for the low-blow-up range. The source does not compute the Yamabe invariant of these blow-ups.

Primary paths: `workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md`; `Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/object.md`; `trace/ttcs/results/step21_ttcs01_verifier1_integration.md`.

### 3.4 Real-hyperbolic blow-ups: the gap is the Yamabe problem — Proved identity; sharp value conditional on one Yamabe identity (Step 23)

For every metric on \(X_k=Y\#k\overline{\mathbb{CP}}^2\), with \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\),
\[
P=8\pi^2k+4\int|W^+|^2+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}+3\int(\Delta u/u)^2+24\int|\nabla u|^2\quad(Y[g]<0),
\]
where \(u^2g\) is the \(\hat s=-24\) Yamabe metric (exact form of LeBrun's \(\int s^2\ge Y[g]^2\)). **Theorem H:** if \(\mathcal Y(X_k)=Y_{\rm hyp}\) (Schoen's conjecture plus blow-up invariance), then \(P>8\pi^2k\) for every metric, \(\inf P=8\pi^2k\) (Burns concentration, Theorem F with \(\mathbf R^+=-2I\)), not attained (equality would make \(g\) a Yamabe-invariant-attaining metric, hence Einstein; LeBrun 1996), and \(\alpha(X_k)=\inf\mathcal E=\inf\mathcal J=4k/(k+6\chi(Y))\) for \(1\le k\le2\chi(Y)\), not attained for \(k<2\chi(Y)\). At \(k=2\chi(Y)\) the infimum is unconditionally \(1\) and its attainment is equivalent to an anti-self-dual (for \(\mathcal E\): anti-self-dual constant-scalar) metric, not excluded here. Arbitrary minimizing sequences are globally asymptotically half-conformally-flat and Yamabe-extremal; the allocation of \(8\pi^2\) to each exceptional class is proved only for Burns sequences. Unconditionally, with \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\): \(P\ge8\pi^2k-(1-y_k)16\pi^2\chi(Y)\), and \(\alpha(X_k)>0\) whenever \(y_k>1-k/(2\chi(Y))\); \(y_k=1\) is sufficient, not proved necessary, for \(\inf P=8\pi^2k\). For \(k>2\chi(Y)\), \(\mathcal E\ge\mathcal J>1\) pointwise, while the Step-72 universal dumbbell gives \(\inf\mathcal E=1\); the infimum is not attained because \(T_{\min}<0\). Thus the older interval \([1,4k/(k+6\chi(Y))]\) is superseded. The conformal identity is already implicit in LeBrun's 1996 Lemma 1. Theorem H\(_\varepsilon\) is the pointwise-Ricci shadow. Path: `workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md` §3.
### 3.5 Kähler blow-up tariff and paired actual fields — Proved restricted theorem; global paired coercivity open (Step 38)

For a fixed blow-up complex structure \(M=X\#k\overline{\mathbb{CP}}^2\), \(A=K_X^2\), every Kähler metric in the complex orientation satisfies
\[
 C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2
 =\frac1{32\pi^2}\int s^2\ge A,
 \qquad P\ge8\pi^2k.
\]
Writing \(K_M=K_0+\sum E_i\), \(\Omega=[\omega]\), and \(e_i=\Omega\cdot E_i>0\), the Hodge-index proof is
\[
 C_+=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2,
 \qquad K_0\cdot\Omega\ge\sqrt{A\Omega^2}.
\]
Hence the inequalities are strict when \(k>0\). Equality of the Kähler infimum with \(8\pi^2k\) additionally needs a Kähler recovery family; Theorem F alone is Riemannian and does not supply that input.

For sign-family monopoles \(a_\epsilon=c+\sum\epsilon_iE_i\), the paired inner product is a section of the relative twisting line with
\[
 c_1(u_{\epsilon\epsilon'})=\frac{a_\epsilon-a_{\epsilon'}}2;
\]
a single sign flip therefore gives \(c_1(u)=\pm E_i\), not \(\pm2E_i\). Its zero may be an amplitude vortex or pointwise spinor orthogonality. In scalar \(-4\) normalization, simultaneous actual solutions give the exact nonnegative amplitude form and in particular
\[
 P\ge8\pi^2Q-4\,\mathbb E_\epsilon\int(2-|\Phi_\epsilon|^2).
\]
The paired field recovers individual exceptional topology lost by convex projection, but it is exactly the singleton Walsh sector rather than an additional positive sector. For one sign flip, with relative curvature \(h=(f-f')/2\),
\[
 |h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2},\qquad
 \|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
\]
The fixed negative-square charge lies in the field-undetermined anti-self-dual relative curvature. Moreover the combined bilinear \((u,w)\) lies in a rank-two bundle of \(c_2=0\); its normalized value is \(S^3\)-valued where both spinors are nonzero, so the \(u\)-phase vortex can unwind through \(w\). No metric-uniform vortex/relative-rotation excess follows without extra projection/noncollapse and kinetic-compensation input. The cheap perpendicular cell has zero compatible almost-Kähler period on \(E\), showing that this rotation channel is geometrically real.

The SU(2)-invariant isolated-cell monopole ODE is exact, but the Step-37/38 numerical attempts imposed incorrect finite-end or cutoff conditions and produced no monopole profile. Exact finite-radius matching to the complete canonical CH monopole is impossible in a charged invariant sector by backward uniqueness; asymptotic convergence requires matching the two-dimensional CH stable manifold. Closed-host monopoles need not induce that isolated invariant boundary problem.

For a topology-preserving ramification neighbourhood with the same controlled boundary germ as its Kähler--Einstein model, relative signature and the relative \(P\) identity give exactly
\[
 \Delta B=\frac14P_N-\frac1{48}\Delta S;
\]
in scalar \(-4\) normalization, \(\Delta B=P_N/4-\Delta V/3\). Hence characteristic flux alone has no anti-self-dual retention sign: retention is precisely a relative-volume upper problem, and depletion occurs when \(\Delta V>3P_N/4\).

Primary path: `workspace/notes/step38_kahler_and_paired_field_scope.md`; independent verification: `trace/ttcs/results/step38_ttcs01_verifier1_integration.md`, `step38_ttcs01_verifier2_integration.md`.

### 3.6 The monopole family on arbitrary metrics: amplitude, Nijenhuis and Weyl forms; affine exhaustion at LeBrun's threshold; the common mode — Proved identities; tariff open (Steps 39–40)

*Quantifiers.* Fixed Spin\(^c\) structures \(a_\epsilon=c+\sum\epsilon_iE_i\); for \(b^+\ge2\), chamber-independent nonzero invariants give unperturbed solutions for every metric (LeBrun's limiting argument); if \(A-k>0\) all solutions are irreducible; apply to the scalar \(-4\) Yamabe representative (\(P(g)\ge P(\hat g)\)); benchmark \(8\pi^2Q\) uses simple type; handles need the higher-type supplier. Saving \(\mathfrak S=8\pi^2Q-P\), Walsh part \(\mathcal W\ge0\), \(M=W^+-W_0\), \(x=M(n,n)\).

*Amplitude form (Step 39).* \(\mathfrak S=\mathbb E\int m(\rho)-8\mathbb E\|\zeta\|^2-4\mathbb E\|M\|^2-\mathcal W\), \(m=(2-\rho)(-\rho^3+10\rho^2-2\rho-4)/6\); positive only on \(0.7758<\rho<2\), \(m_{\max}=1.01555\). Hence \(P/(8\pi^2k)\to c<1\) forces \(\mathbb E\int(2-\rho)\ge2\pi^2(1-c)k-o(k)\).

*Lemma 1 (Step 40).* The Dirac equation fixes the Lee (\(\mathcal W_4\)) component of the rotation of the monopole almost-complex structure, \(\rho|v_4|^2=\frac12|a+J'b|^2\) (\(a=d\sqrt\rho\), \(b=\sqrt\rho\beta\)), and does not see the Nijenhuis (\(\mathcal W_2\)) component (\(\ker\) Clifford contraction \(=\mathcal W_2\), \(cc^*=2\)).

*Theorem N (exact).* \(\mathfrak S=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}-\mathbb E\int\frac{(2-\rho)^2(2+2\rho-\rho^2)}6-\mathbb E\int\rho(|a|^2+5|b|^2-2\langle a,J'b\rangle)-4\mathbb E\|M\|^2-\mathcal W\). Corollaries: Hermitian tariff \(P\ge8\pi^2Q\) for scalar \(-4\) metrics admitting a simultaneous integrable choice; near-minimizers with ratio \(c<1\) have \(\liminf k^{-1}\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\ge16\pi^2(1-c)\) (\(\ge0.684914\) per class for a closed replica of the certified cell).

*Theorem W (exact).* \(\mathfrak S=\mathbb E\int[\rho^2x-4|M|^2]+\mathbb E\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3-4\mathbb E\|\zeta\|^2-\mathcal W\), using \(|d\psi|^2=2|\operatorname{Im}\zeta|^2\). Saving is Weyl-type (rise of \(W^+(n,n)\) above \(-\rho^2/6\)) plus volume-type shallow depletion.

*Theorem E (affine pointwise exhaustion).* Constant affine combinations of these forms with \(P=4W_++4V/3-8\pi^2(A-k)\), \(|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2\), \(|M|^2\ge\frac32x^2\) give \(P\ge8\pi^2[k-(1-t)A]+\mathbb E\int g_{t,\lambda}\) with \(g_{2/3,2/3}=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0\) (LeBrun's \(C_+\ge2A/3\)) and \(\max_\lambda g_{t,\lambda}(3/2)=-\frac34(3t-2)\): nothing beyond LeBrun; contact at \(\rho=3/2\), not at KE.

*Formal common mode.* Constant \(\rho=r\), \(\zeta=0\), \(d\psi=0\) (almost-Kähler, all \(E_i\) ASD-harmonic, null periods) gives \(P/(8\pi^2)=k-A\beta(r)\), \(\beta=16/r-5-12/r^2\); \(r=2-k/A\) gives \(P=o(k)\) with uniform torsion \(|\nabla J|^2\approx2k/A\). Thus the exact identities are consistent with \(c\to0\). **Step-42 correction:** the exact mode is topologically excluded for \(b^+\ge2\) (Lemma T of §3.7: a nowhere-zero self-dual harmonic form has positive period on every exceptional class); it is the formal \(\eta=1,\ \varpi=0\) boundary equality profile of Theorem AKΓ (\(\varpi\) the exceptional-area parameter of §3.7, formerly written \(\alpha\); this has no bearing on the human infimum \(\alpha(M)\)), with \(\beta(r)=2\theta-3\theta^2\), \(\theta=h/(2-h)\). Approximate modes (tiny positive exceptional areas, or thin zero sets of the harmonic part) are not excluded, so the obstruction must still be a linear coercivity of diffuse torsion (§3.7, Proposition G).

Paths: `workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md`; `workspace/scripts/step40_nijenhuis_tariff_check.py`; `workspace/data/step40_nijenhuis_tariff_check.json`; verification `trace/ttcs/results/step40_ttcs01_verifier1_integration.md`; mechanisms `trace/ttcs/results/step40_ttcs01_generator1_integration.md`; Step 39: `workspace/scripts/step39_amplitude_band_and_curvature_channels.py`, `trace/ttcs/results/step39_ttcs01_verifier{1,2}_integration.md`.

### 3.7 Blindness theorem, Taubes period lemma, almost-Kähler torsion profile, and the Goldberg reduction — Proved (Step 42); coercive estimate open

*Setting.* \(M=X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal, \(b^+(X)\ge2\), basic classes exactly \(\pm K_X\) modulo torsion (hypothesis), \(A=K_X^2\), \(0<k<A/3\). In this range with \(b^+\ge2\) simple type, nonzero invariants plus \(A-k>0\) give irreducible unperturbed solutions of every sign class for every metric; \(b^+=1\) keeps its chamber input.

*Theorem B (blindness of the self-dual sign-family data; Step 38).* For one sign flip at \(E_i\), the relative curvature \(h=(f_\epsilon-f_{\epsilon^i})/2\) satisfies \(\|h^-\|^2-\|h^+\|^2=4\pi^2\); every self-dual quantity of the family (amplitudes, \(\psi_\epsilon\), Walsh self-dual energy) sees only \(h^+\), which may vanish, and the forced zero of \(u\) unwinds through \(w\) (\(S^3\)-valued pair, \(\pi_1(S^3)=0\)). Consequently no estimate built only from monopole amplitudes and self-dual curvature of the sign family yields a \(k\)-dependent excess; together with Theorem E this closes the Seiberg–Witten-identity route as a source of the tariff.

*Lemma T (Taubes period lemma).* For any symplectic \(\omega\) on \(M\) (e.g. a nowhere-zero self-dual harmonic form of any metric), \(K_\omega\cdot\omega=|K_X\cdot\omega|+\sum_i|E_i\cdot\omega|\) with every \(|E_i\cdot\omega|>0\) (Taubes SW⇒Gr plus the blow-up formula). Corollary: a self-dual harmonic form with a null exceptional period vanishes somewhere. The symmetric perpendicular cell's canonical closed form has null period and vanishes along the bolt (A01 profile: \(|\omega|_g=\sqrt2u^2\), \(u=0.0072\) at the first bolt sample); it is not an almost-Kähler structure. Lemma T packages a standard argument (LeBrun 2001, Prop. 3.2); new is its use against the common mode.

*Theorem AKΓ.* For every almost-Kähler \((g,\omega)\) on \(M\), with \(\ell=8\pi K_\omega\cdot[\omega]\), \(\theta=\ell^{-1}\int|\nabla\omega|^2\), \(\varpi=\sum|E_i\cdot\omega|/\sqrt{2AV}>0\) (exceptional-area ratio; written \(\alpha\) in the Step-40 note, renamed to avoid the global invariant), \(\eta=|K_X\cdot\omega|/\sqrt{2AV}\):
\[
C_+\ge\frac{\ell^2}{128\pi^2V}(3\theta^2-2\theta+1)=A(\eta+\varpi)^2(3\theta^2-2\theta+1).
\]
(Pointwise \(|W^+|^2\ge\frac32W^+(u,u)^2\), \(W^+(u,u)=s/6+|\nabla\omega|^2/4\); Blair's \(\int(s+s^*)=-8\pi K_\omega\cdot\omega\) fixes the means; Jensen; Lemma T.) \(\eta\ge1\) is **not** automatic for \(b^+\ge2\) (verified counter-mechanism \(\omega_0+t\operatorname{Re}\Omega\)); it holds under the Lorentzian hypothesis (H\(_L\)), e.g. in the Kähler case, where then \(P/(8\pi^2)>k-A(2\theta-3\theta^2)\). \(\theta=0\): Kähler tariff strengthened by areas. \(\min\Gamma=2/3\) at \(\theta=1/3\) (\(s^*=s/2\)): LeBrun's constant. Equality iff \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along ω and \(s,s^*\) separately constant (ω lowest only for \(\theta<1/2\)); the Step-40 common mode is the formal \(\eta=1,\varpi=0\) member. Under (H\(_L\)) the saving is \(\le2A\theta\): linear in torsion.

*Proposition G (reduction).* Under (H\(_L\)) (or directly assuming \(p\ge k-2A\theta\)), if \(P\ge8\pi^2\kappa A\theta\) on a class of almost-Kähler metrics, then \(P\ge8\pi^2k\,\kappa/(\kappa+2)\) there. Monopole form (unconditional beyond §3.6 hypotheses): if \(P\ge\kappa\mathcal N\), \(\mathcal N=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\), then \(P\ge8\pi^2k\,\kappa/(1+\kappa)\); conversely \(P/(8\pi^2k)\to c\) forces \(\mathcal N/P\ge(1-c)/c\) (one-way). The tariff in the open range is thus implied by a linear negative-scalar Goldberg estimate. Its \(P=0\) endpoint on the eigenvector class is Armstrong's theorem; the correctly posed coercive target is a near-saturated quantitative Armstrong estimate \(P/(8\pi^2)+C\mathfrak d_{AK}\ge cA\theta\) with period-loss control, or the quartic variant \(\int|\mathrm{Ric}^\circ|^2\ge c\int|\nabla\omega|^4\) on \(W^+(\omega)^\perp=0\).

*Superseded.* The Step-39/41 co-rotation dichotomy: co-rotation is automatic in almost-Kähler geometry; misalignment is quadratic in torsion and the saving linear.

Paths: `workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md`; `workspace/scripts/step42_ak_torsion_profile.py`; `workspace/data/step42_ak_torsion_profile.json`; verification `trace/ttcs/results/step42_ttcs01_verifier1_integration.md`.

### 3.8 The corrected \(W_0\), divergence symbol, Cotton pairing and quadratic-law reduction — exact local identities; global estimate open (Steps 41–43)

For one monopole field, \(W_0=aK_n\), \(a=\rho^2/4\), \(K_n=I/3-n\otimes n\). Hence
\[
\operatorname{spec}(W_0)=(-\rho^2/6,\rho^2/12,\rho^2/12),\qquad |W_0|^2=\rho^4/24.
\]
For unit \(n,m\), \(|aK_n-aK_m|^2=2a^2(1-\langle n,m\rangle^2)=\rho^4\sin^2\theta/8\), and
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge1/3,\\
\frac{2a^2}{3},&c^2\le1/3,
\end{cases}\quad c=\langle n,m\rangle.
\]
Thus Kähler-type co-rotation is forced quantitatively only where \(\rho\) is bounded below. AAD's proper three-symmetric almost-Kähler model proves that this algebraic structure does not force integrability; the differential slack is the Cotton source \(\delta W^+=C^+=\nabla\operatorname{Ric}^\circ\).

**Proposition 43.B (exact divergence symbol).** For a smooth unit \(n\in\Lambda^+\),
\[
\delta W_0=\mathcal A(da)+a\mathcal T(\nabla n).
\]
If \(d(\sqrt2n)=0\) (the almost-Kähler first-jet condition), then in the standard induced tensor norm
\[
|\delta W_0|^2=\frac13|da|^2+\frac{a^2}{2}|\nabla n|^2,
\]
and the amplitude and torsion images are orthogonal. The torsion map has squared singular value \(1/2\), singular value \(1/\sqrt2\). For a general monopole direction the Dirac-controlled Lee component adds \(dn\) and amplitude--Lee cross terms; the restricted formula cannot be applied to the full jet without Theorem N's \(\zeta\) control.

**Proposition 43.C (exact Cotton pairing).** On a closed constant-scalar almost-Kähler four-manifold, write \(\omega=\sqrt2n\), assume \(a\ge a_0>0\), put \(E=W^+-W_0\), \(U=\mathcal T(\nabla n)\). Then
\[
\frac12\int a|\nabla n|^2=\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle-\int\langle E,\delta^*U\rangle,
\]
so
\[
\frac{a_0}{2}\int|\nabla n|^2\le\sqrt P\,\|\mathcal C^*U\|_2+\|E\|_2\,\|\delta^*U\|_2.
\]
No estimate of the adjoint norms by \(C\|\operatorname{Rm}\|_2\) is currently proved: they contain \(\nabla^2n\) and \((\nabla n)^2\). A localized monopole version additionally needs zero-set/band cutoffs, Lee torsion, amplitude-gradient products and control of \(E\). Hence the hoped-for quadratic transport law is conditional, not a theorem.

**Conditional optimization.** Distinguish \(R_\rho=\mathbb E\int\rho^2|\nabla n|_{W_2}^2\) from \(R_0=\mathbb E\int|\nabla n|_{W_2}^2\). Theorem N gives \(8\pi^2k-P\le R_\rho/2\); since \(R_\rho\le4R_0\), it gives \(P\ge8\pi^2k-2R_0\). If an independent theorem gives \(P\ge R_0^2/(\Lambda A)\), then
\[
P\ge\bigl(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\bigr)^2
=\frac{16\pi^4k^2}{\Lambda A}+O(k^3/A^2).
\]
This would give a positive fixed-topology gap of order \(k^2/A\) without a uniform per-class tariff, but it is conditional on the missing transport/error estimate. Perturbative linear coercivity near a negative Kähler--Einstein host remains a separate spectral theorem; cover-uniformity is open.

**Kirchberg--Sekigawa resisting term.** In Kirchberg's norms, for scalar \(S=-4\),
\[
Q(J)+\int\bigl(|\widetilde R|^2+4|\operatorname{Ric}_\star^-|^2-2|\nabla J|^2+|\nabla J|^4\bigr)=0,
\]
with \(Q(J)=2\int\langle\varphi,\psi\rangle\) an explicit torsion--\(\nabla\operatorname{Ric}\) (Cotton) pairing. The adverse \(-2|\nabla J|^2\) and uncontrolled \(Q(J)\) are exactly why the negative-scalar formula does not give nonperturbative linear Goldberg coercivity from \(P\). AAD's proper three-symmetric local test has \(s=-3/4\), \(\kappa=3/4\), \(|\nabla\Omega|^2=1\), \(|\operatorname{Ric}^\circ|^2=9/64\); it allows Kähler-type algebraic curvature with nonzero torsion and caps any pointwise quartic constant at \(9/64\) in those conventions, but is noncompact/local.

Paths: `workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md`; `workspace/scripts/step43_w0_divergence_symbol.py`; `workspace/data/step43_w0_divergence_symbol.json`; `workspace/scripts/step43_proper3symmetric_test.py`; `workspace/data/step43_proper3symmetric_test.json`; verification `trace/ttcs/results/step43_ttcs01_verifier1_integration.md`.

### 3.9 Perturbative coercivity at complex-hyperbolic hosts and the price of \(s^*\ge0\) pockets — linear gaps proved (Step 44); nonlinear neighbourhood corrected to \(A_C\) in §3.10 (Step 46)

Source: `workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md`; computation `workspace/scripts/step44_perturbative_ke.py` → `workspace/data/step44_perturbative_ke.json`; verification `trace/ttcs/results/step44_ttcs01_verifier1_integration.md`.

*Pointwise gaps* (s = −4, λ = −1, any compact ball quotient \(X_\Gamma\)). (G1) On \(\mathbb{CH}^2\), \(\mathring R=-2\) on the \(J\)-invariant (dim 3) and \(+4\) on the \(J\)-anti-invariant (dim 6) trace-free tensors (holomorphic curvature −4, λ = −6). Koiso's identity \(\langle L_Eh,h\rangle=\|d^\nabla h\|^2+\langle(-\lambda-\mathring R)h,h\rangle\) then gives the TT gap \(|\lambda|/3\), and \(2|\lambda|\) on the \(J\)-invariant sector. (G2) \(\|(\nabla^2f)^\circ\|^2=\tfrac34\|\Delta f\|^2+|\lambda|\|\nabla f\|^2\). (G3) The conformal Killing gap is \(2|\lambda|\). (G4) The gauge-fixed linearized SW operator at the canonical Kähler solution: its first-order cross terms cancel exactly (gauge coefficient −1/2), the algebraic potentials are \(\tfrac12\) (1-forms), \(2,1\) (on \(\mathbb C\Phi_0\)) and \(0\) (on \(\Phi_0^\perp\cong K^{-1}\)), and the Landau/Kodaira bound \(\|\nabla\psi_\perp\|^2\ge2|\lambda|\|\psi_\perp\|^2\) gives \(\|\mathcal L v\|^2\ge\tfrac12\|\nabla v\|^2+\tfrac{|\lambda|}2\|v\|^2\). All four constants are curvature-algebraic, hence \(\Gamma\)-independent.

*Theorem A (\(A_H\)) — superseded (Step 46).* The Step-44 global-Sobolev form used \(H^2\subset L^\infty\), which fails in real dimension four (A01, message #811). Its correct replacement is the uniformly local form \(A_C\) of §3.10; an absolute \(H^s\) neighbourhood with \(s\ge5\) and an injectivity-radius bound implies the \(C^{2,\alpha}_b\) hypothesis of \(A_C\), so \(A_H\) holds in that corrected form as a corollary. The linear Bochner gaps (G1)–(G4) are unaffected. The bound is one-sided: near-KE cscK metrics have \(R=0<P\). *Not* a tariff: on blow-ups, bulk field selection and local Einstein deformations (collar terms) block localization. The unconditional global input remains \(R_{\rm tot}\ge16\pi^2(1-c)k\) for \(P\le8\pi^2ck\).

*Proposition Π.* \(\mathbb R^+(\hat\omega,\hat\omega)=s^*/4\) for almost-Kähler structures, so aligned tiny-area Burns spheres save at first order exactly where \(s^*>0\). With \(\varphi=\operatorname{Vol}\{s^*\ge0\}/V\):
\[
C_+\ge\frac{\ell^2}{128\pi^2V}\Bigl[\Gamma(\theta)+\tfrac{\varphi}{1-\varphi}(1-\theta)_+^2\Bigr]\ge\frac{\ell^2}{128\pi^2V}\,\frac2{3-2\varphi}
\]
(exact two-region Jensen; minimum at \(\theta=1/(3-2\varphi)\)). There is a threshold version for \(s^*\ge s_0\). Under \(H_L\) this gives \(P/8\pi^2\ge k-A(1-2\varphi)/(3-2\varphi)\). Per sphere, the Theorem-F saving is \(O(x_0)\) while a pocket costs \(O(r^4)\), \(r\gg\sqrt{x_0}\): convexity does not exclude the route, and the perturbative range of Theorem F limits it to \(c=1-O(x_0)\). The Kähler tariff is global (Hodge index) and does not cover a locally Kähler pocket inside a non-Kähler metric, so nonperturbative aligned cells in \(s^*>0\) pockets remain a legitimate construction target.

### 3.10 Lemma M, the extensive theorem \(A_C\), and the Weyl-departure Theorem K — Proved (Steps 45–46); scope: canonical branch / necessary condition

Sources: `workspace/notes/step45_lemmaM_and_weyl_departure.md`, `workspace/notes/step46_lemmaM_elementary_and_AC.md`; computations `workspace/scripts/step45_resolvent_and_weyl_departure.py`, `workspace/scripts/step46_lemmaM_elementary.py` → `workspace/data/step4{5,6}_*.json`; verification `trace/ttcs/results/step45_ttcs01_verifier1_integration.md`, `trace/ttcs/results/step46_ttcs01_verifier1_integration.md` (Step-46 repairs incorporated: nonlinear gauge, \(L_E\) does not kill \(\delta^*X\), constant \(\kappa/8\), Coulomb slice, numerical-not-certified decimals).

*Normal operator* (hol. curvature −4, λ = −6). At the canonical Kähler solution, \(N=\mathcal L^*\mathcal L=B_1\oplus(\Delta_0+12)\oplus(\Delta_0+6)\oplus\nabla^*\nabla_{K^{-1}}\) exactly, with \(B_1=dd^*+\tfrac12d^*d+6\) (Hodge form; the Bochner form \(\tfrac12\nabla^*\nabla+3\) arises only after dropping \(\tfrac12\|d^*a\|^2\)).

*Lemma M.* On every compact ball quotient, \(\|N^{-1}\|_{L^\infty\to L^\infty}\) and the derivative-kernel norms are bounded by model constants: \(\le\tfrac13+\tfrac16I_{dd}\approx0.679\) (numerical value; finiteness rigorous) (one-forms, via \(B_1^{-1}=2(\nabla^*\nabla+6)^{-1}-\tfrac16d[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}]d^*\), Kato plus the mixed Hessian of the distance), \(1/12\), \(1/6\), and \(\|G_{K^{-1}}\|_{L^1}\approx0.2149\) (\(\ge1/9\) exactly). Proof for \(K^{-1}\): radial gauge \(A=6i\eta\), \(V=9\tanh^2r\); the Landau state \(\cosh^{-3}r\) has eigenvalue 12, which derives the threshold 13 rather than entering it by hand; zero-energy decay \(e^{-(2+\sqrt{13})r}\) beats \(e^{4r}\). Exact one-form decay \(2+\sqrt{10}\); margins \(\sqrt{13}-2\), \(\sqrt{10}-2\). These exponents agree with Will and Carron–Pedon.

*Theorem \(A_C\).* There are \(\varepsilon_0,C\) depending only on \(\mathbb{CH}^2\) with the following property. If \(\|c\phi^*g-g_\Gamma\|_{C^{2,\alpha}_b}\le\varepsilon_0\), the norm being measured on unit balls of the universal cover, then the Yamabe representative \(\hat g\) has a unique canonical SW branch within \(C\varepsilon_0\) in \(C^{1,\alpha}_b\), and \(\int|\nabla n|^2\le CP(\hat g)\le CP(g)\), hence \(R_{\rm can}\le C'P\). The proof is a uniformly local IFT for the Yamabe normalization \(6(\Delta_0+8)\), the DeTurck harmonic-map gauge \(\nabla^*\nabla+6\) (nonlinear gauge, \(\beta h=O(h\nabla h)\)) and the SW branch (Lemma M). It is followed by quotient-independent \(L^2\) coercivity in Bianchi gauge, which uses the exact identity \(\operatorname{Ric}^\circ=\operatorname{Ric}-\lambda g\) at scalar \(4\lambda\) and the TT Koiso gap, and pointwise absorption of the quadratic terms. Scope: only the canonical branch, and only on closed quotients. Branch selection on large covers, localization on blow-ups (outer-layer and collar terms) and tariffs are not covered.

*Theorem K* (field-selection-free Weyl departure). Under the all-metric sign-family hypotheses of Theorems N/W, for the scalar-\(-4\) Yamabe representative,
\[
8\pi^2k-P(g)\le8\pi^2k-P(\hat g)\le\tfrac{4\sqrt6}3\int\operatorname{dist}(W^+_{\hat g},\mathcal K),
\]
where \(\mathcal K\) is the Kähler-type orbit with spectrum \((-\tfrac23,\tfrac13,\tfrac13)\). The constant is sharp and is attained to first order at canonical amplitude with aligned direction. Pointwise, \(f(W_*,r,n)=-(2-r)^2(r+1)-r^2(1-q)\). No pointwise quadratic version exists, since at the equality state \(f=4E(\hat\omega,\hat\omega)-4|E|^2\). Consequence: \(P\le8\pi^2ck\) forces \(\int\operatorname{dist}(W^+_{\hat g},\mathcal K)\ge\sqrt6\pi^2(1-c)k\ge0.10485k\) for the certified cell coefficient. This is a necessary \(L^1\) condition, not a tariff.

*Proposition 46.T (three regimes).* The saving must sit in one of three places. (1) Diffuse canonical-branch rotation in uniformly CH regions: closed by \(A_C\) on closed quotients; the local version is open. (2) \(s^*\ge0\) pockets: priced per unit volume by Π, but the pockets can shrink. (3) Intermediate torsion \(|\nabla\omega|^2\sim|s|\), noncanonical depleted fields, harmonic-form zero sets, collars or cores: not priced, and this is the construction target. Here the quadratic law is conditional on noncircular \(E,\nabla a\) control.

*Proposition 46.V, corrected by A01 Step 41 (the AK representative is the wrong conformal gauge).* A01 realizes subthreshold pure-blow-up metrics conformal to smooth almost-Kähler metrics by rotating the certified cell. The existence proof is qualitative and rigorous: for a monotone rotation cutoff, the exceptional-period derivative is \(p'(0)=-\pi\int\chi'\Phi>0\), the invariant self-dual form is nowhere zero for \(p\ne0\), and strict subthreshold cost persists by continuity. Near the bolt the correct orthonormal model is
\[
f_p^2=|\Omega_p|^2/2=a^2p^2+\kappa^2r^2+O(p^2r^2+r^4),
\]
not the superseded \(|\Omega|=a|p|+br^2\) model. With \(\hat g_{AK}=f_pg\), \(v=\sqrt{f_p}\),
\[
\frac{\Delta v}{v}=\frac{\kappa^2(4a^2p^2+\kappa^2r^2)}{4(a^2p^2+\kappa^2r^2)^2}+O(1),
\quad
\int\hat s^2d\mu_{AK}=C_Ep^{-2}+O(|\log|p||).
\]
For the certified profile, A01 finds \(C_E=1.75135145\), numerically approached by resolved runs. Thus the AK scalar-variance defect diverges like \(p^{-2}\), while the original smooth metrics remain subthreshold; exactly \(P(\hat g_{AK})-P(g)=[S(\hat g_{AK})-S(g)]/12\). AK-gauge lower bounds do not transfer to \(P(g)\) unless this conformal conversion is retained. Coercivity belongs on the Yamabe representative with monopole fields (N, W, K, B) or in conformally invariant form.


## 4. Curvature-sensitive marked blow-up cells

For an exact-complex-hyperbolic-collar marked cell,
\[
P_{\rm cell}-8\pi^2=4\Delta W_++\frac1{12}\Delta S.
\]
This same-metric identity is the reason a Weyl-energy improvement alone does not control the trace-free energy \(P\), nor therefore, through \(\mathscr D=(4P+L_s)/R\), the human defect.

### 4.1 First-order response for a general bulk — Proved (Theorem F, Step 20) as an upper construction

The aligned Kähler seed obeys
\[
\frac{P_K}{8\pi^2}=1+6\kappa x_0+9(\kappa^2+X^{-2})x_0^2+O_X(x_0^3).
\]
**Theorem F.** Let \((M,g)\) be closed and oriented, \(p\in M\), and \(\zeta\in\Lambda^+_p\) a unit form. Glue the Burns metric \(\delta+x_0h\), whose exceptional curve has area \(\pi x_0\), into \(g\)-normal coordinates with cutoff radius \(x_0^{1/5}\). This gives metrics on \(M\#\overline{\mathbb{CP}}^2\) with
\[
P(\hat g_{x_0})=P(g)+8\pi^2\big(1-x_0\mathbf R^+_p(\zeta,\zeta)\big)+O(x_0^{6/5}),
\]
and the same law holds for \(J\) when \(g\) is Einstein. The proof rests on two facts: the Burns tail is pointwise linearly self-dual-flat and scalar-flat, and its exact cut-annulus transgression is \(\Phi^{++}=\pi^2\,\hat\zeta\hat\zeta^T\), \(\Phi^{--}=\frac{\pi^2}3I\), \(\Phi^{+-}=0\) (exact sympy on \(S^3\)). The scalar flux \(4\pi^2x_0=4\pi\,\mathrm{area}(E)\) reproduces the Kähler identity \(\int s=4\pi c_1\cdot[\omega]\). Theorem F recovers the signed complex-space-form slopes \(+6,0,-6\). At a negative Kähler–Einstein point, \(\ker\mathbf R^+=\omega^\perp\) is first-order free and coincides with the directions allowed by the first \(A_1\) desingularization obstruction \(\mathbf R^+\zeta=0\). On real hyperbolic bulk \(\mathbf R^+=\frac s{12}I<0\), so every direction costs at first order. The matching lower bound for the cell infimum is open.

Primary paths: `workspace/notes/step20_burns_response_and_neck_quantization.md`; `workspace/scripts/burns_transgression_flux.py`; `workspace/data/burns_transgression_flux.json`; `workspace/scripts/o11_general_bulk_cell.py`.

**CR pinning (Lemma P, Step 25; independently verified in Step 26) — Proved.** For every diagonal metric, the Rossi variable \(\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q\) obeys exactly \(\widetilde\Phi'=F-\frac14(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh})\), hence \(|\Delta\widetilde\Phi-\int F|\le(\widehat P/2)^{1/2}(\int dt/W)^{1/2}\). In an ACH block, and only with that scope, \(F=\zeta^2G\) with bounded \(G\). Changing the Rossi squashing at radius \(T\) costs at least \(\frac12e^{4T}(\Delta\log\rho)^2\) (units \(8\pi^2\)), and the constant \(\frac12\) is the exact linearized optimum; the null-line value function and Lemma P measure the same charge and are not additive.

**Standard-CR truncation (Theorem T, Step 26) — Proved for diagonal scalar-\(-24\) ends in one small ACH block.** The CH linear rates are \(2,0,-2,-4,-6,-8\). The \(-2\) mode is exactly radial phase, while the physical Einstein modes begin at \(-4\); the \(-8\) mode is a forced constraint response for non-Einstein scalar-normalized ends. After matching radial phase, finite \(P\) and \(\widetilde\Phi\to0\) give transverse deviation \(o(e^{-2t})\), enough to splice on a unit annulus with added squared Einstein residual tending to zero. Hence a complete standard-CR diagonal Einstein ACH filling implies \(p^{\rm diag}_{1,0}=0\), while the converse needs attainment/compactness.

**Euler-flux collapse separation (Step 26) — Proved for diagonal annuli.** For \(\mathfrak b=W(\sum_i y_iK^{(3)}_{jk}-y_1y_2y_3)\), exact Cartan computation gives \(\widehat P(C)=\Delta\mathfrak b+\int|W|^2/(4\pi^2)+\int s^2/(96\pi^2)\). On CH, \(\mathfrak b=2-6\sinh^4t\). Arb evaluation on all 40 validated Theorem-E endpoint boxes gives \(\mathfrak b\in[-64533.462,-64275.416]\) once \(\widetilde\Phi\approx0.7845\). Product and ALF Berger necks have \(\mathfrak b\to0\), so a post-developed-Rossi connector to such a neck costs far above the certified cell value. High-shear scale-invariant connectors and resets before the developed ACH regime remain open.

Theorem E is therefore not a bounded-cost limit of exact-CH diagonal cells whose correction remains in the ACH block, nor can it first develop to the validated orbit and then pass through an ordinary product/ALF neck. The conditional structure Theorem D now has a proved truncation direction; its remaining inputs are compactness, high-shear/interior-collapse and large-bolt control, and validated no-return dynamics. Paths: `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`; `workspace/notes/step26_truncation_flux_and_branch_completeness.md`; `workspace/scripts/cr_pinning_check.py`; `workspace/scripts/squash_escape_cost.py`; `workspace/scripts/verify_euler_flux_identity.py`; `workspace/scripts/ach_euler_flux.py`.

**Chiral transgressions (Theorem X, Step 27) — Proved for diagonal annuli (exact symbolic).** There is an explicit signature transgression \(\mathfrak s\) with \(\mathfrak s'=\frac12W(B_+-B_-)\). With \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\),
\(\widehat P(C)=\Delta\mathfrak b_\pm+\frac1{2\pi^2}\int_C|W^\pm|^2+\frac1{96\pi^2}\int_Cs^2\).

The charges \((\mathfrak b_+,\mathfrak b_-)\) are:
- smooth centre: \((2,2)\);
- \(O(-1)\) bolt in the blow-up orientation: \((1,7)\);
- biaxial or controlled near-biaxial Hopf-collapsed Berger orbit in the Taub–NUT/blow-up chirality: \((-2,2)\), since the Euler flux vanishes on collapse while \(\mathfrak s\) keeps an adiabatic charge; the opposite four-dimensional orientation gives \((2,-2)\), and unrestricted anisotropic collapsed jets have additional shear terms;
- CH orbit: \((2-9\sinh^4t,\ 2-3\sinh^4t)\).

Consequences:
- \(\widehat P[0,t]\ge\mathfrak b_+(t)-1\). This is the sharp, Burns-extremal replacement of Lemma Q′: Burns has \(W^+=s=0\) and \(\widehat P=2-1\).
- A cell with \(\widehat P<1\) has no orbit close to round.
- Decollapse from a collapsed neck to a CH-like orbit of radius \(\tau\) costs at least \(4-9\sinh^4\tau\).
- Taub-bolt is a regular zero-cost core in the blow-up orientation, with \(\frac1{2\pi^2}\int|W^\pm|^2=3,5\).

Step 28 independently verified the formula, signs, orientation and model balances. The normalized transgression is \(\mathfrak s=S_0-6\); raw `chiral_flux.json` fields use \(S_0\), so its `bA,bB` require shifts \(+6,-6\). The Hitchin–Thorpe prefactor is \(4\pi^2(2\chi\pm3\tau)\).

Files: `notes/step27_chiral_transgression_and_small_bolt.md`, `scripts/chiral_flux_identity.py`, `scripts/chiral_flux_models.py`; independent reading `trace/ttcs/results/step28_ttcs01_verifier1_integration.md`.

**Small-bolt Einstein structure (Step 27) — Matched-asymptotic mechanism, numerically confirmed.** As \(b\to0\) the perpendicular ACH separatrix is a Taub-bolt core followed by a collapsed \(\Lambda\)-Taub-NUT neck with circle \(\simeq4n\cosh\sqrt2t\), \(n=b/(2\sqrt3)\), and then saturation at scale one. The triaxial mode grows at rate \(4/\varepsilon\) in the neck, which predicts \(\log(1/d_*)\sim\pi\sqrt{3/2}/b=3.8476/b\); the fit gives \(3.854\). The Rossi parameter behaves as \(\rho\simeq0.8/b\to\infty\). A rigorous matching proof remains open.

**Scale-free saturation problem (Step 28) — Exact reduction; value open.** With \(a_f=re^{2\beta/3}\), \(a_g=re^{-\beta/3+q/2}\), \(a_h=re^{-\beta/3-q/2}\), \(d\tau=dt/r\), and \((\bar H,\bar E,\bar D)=r^2(H,E,D)\), the full diagonal dynamics and action become independent of the bolt scale:
\[
\widehat P=\int\left(3\bar H^2/16+\bar E^2/6+\bar D^2/8\right)d\tau.
\]
The collapsed branch is the control value from the Taub-bolt/\(\Lambda\)-Taub-NUT entry ray to the standard-CR end. All three controls are essential. Path: `notes/step28_saturation_control_and_revised_diagonal_structure.md`.

**Collapsed saturation value (Step 29) — Terminal reduction proved; value \(=4\) numerically.**

*Terminal reduction (Lemma S).* An exact-CH terminal jet followed by the homothetic exact CH collar is a legitimate exact-collar competitor. Two facts make this work: \(\widehat P\) is scale invariant, and zero-control flow is Einstein by the contracted Bianchi identity. By Theorem T this terminal has the same infimum as the standard-CR stable set, so no stable-manifold parameterization is needed. Step 28's rejection of these endpoints came from its checker, which forced the compact section \(\zeta=1/(a_ga_h)=10^{-2}\) and thereby rescaled CH jets.

*Numerical value.* The minimal action rises monotonically along the entry ray:

| \(\varepsilon\) | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 |
|---|---|---|---|---|---|---|---|---|
| minimal action | 2.33 | 3.38 | 3.75 | 3.89 | 3.95 | 3.976 | 3.988 | 3.994 |

Independent actual-metric evaluations of the same runs give 2.52, 3.48, 3.82, 3.93, 3.98 at \(\varepsilon=1/2\) to \(1/32\), 3.98841 at \(1/128\), and 3.9963 at \(1/256\). The values track the chiral gap \(2-\mathfrak b_+(\text{entry})\to4\).

*Structure of the minimizer.* For small \(\varepsilon\) the minimizer rises with \(W^+\approx0\) and \(s\approx0\), an ASD scalar-flat decollapse, to an exactly round orbit with \(\mathfrak b_+=2\). It then follows a CH ball at zero cost. The collapsed branch is therefore an ALF analogue of the Burns bubble. Burns pays \(2-1=1\); the collapsed route pays \(2-(-2)=4\).

*Opening radius.* Opening late is priced at least exponentially, roughly like \(e^{4\tau}\) (Lemma P): at \(\varepsilon=1/16\), windows starting at \(\tau=2.5,3,3.5,4\) cost about 4.1, 7.9, 34, 207.

*What remains.* The diagonal transgression itself now proves the first branch estimate in a precise finite-charge normalized-jet class. If a collapsed normalized first-jet family obeys
\[
x=Xz^3+o(z^3),\qquad p=Pz+o(z),\qquad \chi=Cz+o(z),\qquad \eta=Nz+o(z),
\]
then exact symbolic evaluation gives
\[
\mathfrak b_+^{\rm end}=-2-(C+4X)^2,
\]
so every annulus joining it to a round orbit satisfies the **Q″ inequality**
\[
\liminf\widehat P\ge2-\mathfrak b_+^{\rm end}=4+(C+4X)^2.
\]
Thus anisotropy in this finite-charge normalized-jet class cannot lower the Berger-to-round payment. The opposite charge is \(\mathfrak b_-^{\rm end}=2+(C-4X)^2\); \(P,N\) cancel from both limits. This class is not automatically bounded-curvature geometry: fixed-base-scale bounded orbit/mixed curvature imposes stronger decay, such as \(x=O(z^6)\), \(\chi=O(z^4)\), and radial second-derivative control, which force \(X,C\to0\). Burns and Taub-bolt/ALF decollapse are priced by the same rule: round charge minus bubble-end charge, respectively \(2-1=1\) and \(2-(-2)=4\). What remains for small-bolt matching is to prove that regular bolt trajectories enter a finite-charge or bounded-geometry class, or charge the production of an uncontrolled high-shear first jet.

**Fibre/base pinning (Step 30) — Proved identity.** Put \(v=y_f-(y_g+y_h)/2\) and
\[
\widetilde B=\log\frac{\kappa}{\sqrt{1+\zeta}}+\frac14(v-\kappa^{-1}).
\]
This vanishes on every CH orbit and obeys exactly
\[
\widetilde B'=F_\beta-\frac14\left(\operatorname{Ric}_{ff}-\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2\right),
\]
hence
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le\sqrt{\frac{3\widehat P}{8}}\left(\int\frac{dt}{W}\right)^{1/2}.
\]
On an exact CH tail, \(\int_T^\infty W^{-1}dt=\frac1{2\sinh^2T}-\frac12\log(1+\sinh^{-2}T)\), giving an exponential late-opening payment once the effective mismatch is known. For a general connector this CH denominator requires a separate comparison with its actual \(\int W_g^{-1}dt\). With the CH denominator, overlap with the early-opening bound at \(T=.70\) needs mismatch at least \(0.370125\ldots\); volume comparison and free-drift control on the saturation region remain missing.

An enlarged-entry numerical test confirms why first-jet control matters. At \(\varepsilon=1/16\), imposing a fixed raw \(\Delta\eta=-8\) produces an explicit collocation path of cost \(0.5454\) and independently reconstructed metric cost \(0.5745\), below the certified cell; but this violates the finite-charge scaling above and at \(\varepsilon=1/32\) the same raw perturbation costs \(2.9425\). It is not a regular bolt construction. Its entry charge is already \(1.45194\), so the omitted bolt-to-entry prefix costs at least \(0.45194\); prefix plus reconstructed connector is at least \(1.0264\). It identifies uncontrolled contact-slot shear as the remaining high-shear escape mechanism rather than refuting Q″. Paths: `notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md`, `scripts/collapse_chiral_charge_limit.py`, `scripts/beta_pinning_identity.py`, `scripts/saturation_anisotropic_scan.py`, `data/saturation_control/step30_anisotropic_summary.json`.

**Theorem D (frozen statement, Step 29).**

*Setting.* Let \(p^{\rm diag}_{1,0}\) be the infimum of \(\widehat P\) over diagonal Bianchi-IX metrics on \(O(-1)\) with an exact CH collar. By Theorem C and the Yamabe solution, this equals the scalar-\(-24\) standard-CR value.

*(i) Einstein \(\Rightarrow\) zero — proved, unconditional.* If a complete diagonal Einstein ACH metric on \(O(-1)\) with standard CR infinity exists, then \(p^{\rm diag}_{1,0}=0\). This is Theorem T.

*(ii) Compactness — conditional on four branch inequalities.* Let \(g_j\) be a minimizing sequence. On bounded-shape, bounded-\(W\) regions the chiral identities bound the weighted curvature, and the state equations are affine in the Ricci controls. Hence a subsequence converges to a complete minimizer with standard CR infinity, unless one of four mechanisms occurs. In each case it suffices to show that the mechanism costs more than \(\min(p^{\rm diag}_{1,0}+\delta,\ 0.99585)\).

1. *Small-bolt collapse/saturation.* Finite-charge normalized entries are now priced rigorously by Q″ at \(4+(C+4X)^2\), while genuinely bounded-geometry Berger entries have \(X,C\to0\) and price \(4-o(1)\). The remaining work is the matched-entry theorem showing regular small-bolt sequences satisfy one of these asymptotic regimes; if they do not, the escaping first-jet shear joins mechanism 3.
2. *Large-bolt escape.* Status: open.
3. *Interior high-shear/volume-bounce connector.* The exact formula \(\mathfrak b_+^{\rm end}=-2-(C+4X)^2\) handles the finite-charge normalized-jet class, and bounded-geometry Berger collapse is a stronger subcase. Uncontrolled raw contact shear \(\eta\) can sharply lower finite-scale connector cost and is the remaining escape mechanism; it must either be excluded by regular bolt/interior matching or charged before the selected section.
4. *Conformal-infinity face escape.* Status: the face flow from \(E(q)\) has been computed and shows no return (Step 25, floating); a validated no-return proof is open.

Scale-separated ALE concentration (\(\mathfrak b_+\)), large-volume nonstandard-CR escape (Lemma P) and post-Rossi product/ALF collapse (Euler flux) are already excluded.

*Step-31 revision of (ii) — three inputs.* The chiral identities hold pointwise in \(t\), which yields the charge-variation bound Lemma V:
\[
\widehat P\ge\int\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt,
\qquad
\widehat P\ge\sup_t\max\{\mathfrak b_+(t)-1,\ \mathfrak b_-(t)-7\}.
\]
Here \(\mathfrak b_-=\sum w_i^2-\prod w_i-2\) with \(w_i=a_i'+\gamma_i\), and the bolt charges are \((1,7)\). Two consequences follow. Any round passage costs at least \(1-o(1)\). The raw \(\Delta\eta=-8\) entry has \(\mathfrak b_-=8.5496\), so its bolt prefix alone costs at least \(1.5496\).

Mechanisms 1 and 3 therefore reduce to **(N) non-round late opening**: after a collapsed section, \(\mathfrak b_+\) must stay below \(-1\) until CH shape is reached at \(\tau>0.70\). Constrained collocation (`SAT_BPMAX`) gives non-round values \(6.48\) (cap \(-1\), \(\varepsilon=1/16\), two warm starts; \(N=80\): \(6.44\)), \(5.37\), \(6.55\) and \(6.62\) at \(\varepsilon=1/4,1/32,1/64\), and \(4.03,4.81,5.50,7.89,11.87\) for caps \(1,0,-.5,-1.5,-2.5\). These costs are paid mainly in the \(D\) channel and not by charges.

Lemma N (independently verified, Step 32, and by S1003A01) shows that in the scalar-normalized class \(s\equiv-24\) the \(H\) channel is the Hamiltonian-constraint residual \(\mathcal C=\sigma_2(y)-6-R^{(3)}/2\), with \(\widehat P\supset\int W\mathcal C^2/3\). The normalization is not a literal preservation of the exact CH collar: the exact-ended diagonal infimum equals the scalar-\(-24\) infimum over metrics asymptotic to the marked standard CH end at rate \(>4\), followed by Theorem-T truncation; the bolt radius becomes \(u(0)b\). Lemma N also gives \(\mathcal C'=-2S\mathcal C-\sum(S-y_i)e_i\) and \(S'=18-S^2+R^{(3)}+\mathcal C\). Lemma W (last-crossing proof, repaired Step 33) uses these identities to supply the \(\int W^{-1}\) volume comparison wherever \(R^{(3)}\ge-\rho_0\), \(\rho_0<18\). The constrained collocation values above are feasible paths returned by a local optimizer, not lower estimates.

*Steps 33–34 additions.* Lemma V is exhausted as a static tool for (N): in scale-free jet coordinates \(\mathfrak b_+=2-|u|^2-\prod u\) depends on \(u=a'-\gamma\) only, an explicit path from the collapsed jet \((1,1,-2)\) to the CH jet \((3\sinh^2\tau,0,0)\) makes \(\mathfrak b_+\) monotone, and joint minimization finds triaxial never-round paths with \(\int\max(0,d\mathfrak b_+,d\mathfrak b_-)\approx0.02\) (Lemma Z). The exact control minimization goes further: for \(V=\mathfrak b_++\phi(q,\eta)\), SymPy gives \(\sup_{\bar H,\bar E,\bar D}(\dot{\mathfrak b}_+-L)\equiv0\), so the HJ condition is \(\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le0\). A sampled convex search on the cap-\(-1\) swap trajectories gives zero gain for every quadratic \(\phi(q,\eta)\); \(K\) changes sign from about \(-3.34\) to \(4.46\). Thus decorating the already exact chiral calibration by \((q,\eta)\) does not expose the missing cost. The stronger next structure is S1003A01's exact canonical almost-Kähler identity
\[
\widehat P-1=12H+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N+\Sigma,
\]
whose only negative term is Nijenhuis energy and whose transport/Hardy estimate makes the far zone nonnegative. An independent check confirms the coefficients but also shows that the certified subunit cells realize a genuine negative compact middle-zone mode; this route should determine a sharp subunit lower value and near-extremal mode (or a unit bound only under additional coercive hypotheses), not contradict the certified metrics. The unresolved inequality is the lowest coupled compact action for the forced bolt Nijenhuis charge, conformal factor, and \(W_3^+\) transport. Paths: `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, `scripts/hj_symbolic_reduction.py`, `data/saturation_control/hj_qeta_probe.json`, and `Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md`.

*Step-35 addition (calibration and leaves).* Since \(\dot{\mathfrak b}_+\) is affine in the controls and \(\sup_c(\dot{\mathfrak b}_+-L)\equiv0\), one has exactly \(L(c)-\dot{\mathfrak b}_+=L(c-c^*)\), so \(\widehat P=\Delta\mathfrak b_++\int L(c-c^*)\) with positive-definite weight (no kernel defect); calibrated curves are the ASD scalar-flat diagonal metrics (Burns yes; Taub-bolt and CH no). Calibrated leaves from the collapsed entry converge to the Euclidean round fixed point (transverse eigenvalues \(-2,-4\)); backward leaves from all CH jets stay in the invariant biaxial set \(\Sigma=\{q=\eta=0\}\) and blow up without approaching the collapsed set. The endpoints are therefore leaf-separated in the antisymmetric pair \((q,\eta)\), reachable only through \(\bar D\) — the structural origin of the \(D\)-dominance. The exact transverse block on \(\Sigma\) is attracting on 38% and saddle on 62% of sampled \(\Sigma\cap\{\mathfrak b_+\le-1\}\), so no frozen argument excludes a cheap connector: (N) lacks path weight, not kernel or separation. It is recorded as a numerical-margin input. The proposed route is to match the \(\mathfrak b_+\) calibration on the swap band with S1003A01's CH-renormalized \(B\) (\(B_{\rm bolt}=1,B_{\rm CH}=2\)) on the tail. Paths: `notes/step35_calibration_theorem_and_branch_classification.md`, `scripts/calibrated_flow_leaves.py`, `scripts/transverse_block.py`.

**(L) large bolt:** the Einstein separatrix has an exact face limit, with \(d/b\to0.90535\), \(\rho\sim1.345b\), and the Rossi offset \(\log b\) produced at \(W\asymp b^2\). Shadowing together with Lemma P therefore predicts cost \(\gtrsim b^2(\log b)^2\). **(F)** conformal-face escape is analysed on the same \(\zeta=0\) face. Path: `notes/step31_charge_variation_constraint_pinning_nonround_opening.md`.

*(iii) Zero \(\Rightarrow\) Einstein.* Under (ii), \(p^{\rm diag}_{1,0}\) is attained. If \(p^{\rm diag}_{1,0}=0\), the minimizer is an Einstein metric of this type. Hence
\[
p^{\rm diag}_{1,0}>0\iff \text{no standard-CR diagonal Einstein filling of } O(-1).
\]

*(iv) Expected route to positivity.* Positivity would follow from \(\rho\neq1\) along all Einstein separatrices. Floating fate maps give \(\rho\ge2.19\) on ACH1 and its mirror \(\rho\le1/2.19\) on ACH2 at the sampled \(b\in\{.14,.2,.35,.8,2,20\}\) (minimum near \(b=.8\)), with \(\rho\sim0.8/b\) as \(b\to0\). This requires interval fate enclosure and large/small-\(b\) asymptotics.

### 4.2 Kernel-direction neck response — Exact reduced calculation; general remainder open

The calibrated neck density is
\[
x_0^2\left[\frac{(v_s+2v-3)^2}{4}-6v\right],
\]
with minimum \(-18x_0^2\) at \(v=9/2\). The exact constant-mode expansion gives the common minimizer \((C_1,C_2,C_3)=(9/4,3/4,1/2)\) for \(P\) and \(J\), predicting
\[
\frac{P}{8\pi^2},\frac{J}{8\pi^2}
=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The coefficient and cancellations are exact in the reduced family; a uniform error estimate for general bulk metrics remains open.

Primary paths: `workspace/scripts/o11_neck_density_sympy.py`; `workspace/scripts/o11_perp_logneck.py`; `workspace/data/o11logneck/`.

### 4.3 Explicit subthreshold cells — Certified

The exact-dyadic \(x_0=0.01, X=8\) cell satisfies
\[
P/(8\pi^2)=0.999108702733592648\ldots,
\qquad
J_6/(8\pi^2)=0.999116243135324311\ldots
\]
with pure-Arb enclosures and exact bolt/collar matching data. The stronger area-selected \(x_0=3/100, X=64\) cell satisfies
\[
P/(8\pi^2)\in[0.9958484075845568,0.9958484075911518],
\]
\[
J_6/(8\pi^2)\in[0.9958546908532724,0.9958546908569237].
\]
The authoritative Step-33 extension to \(X=128\), degree 20, has the sharpened exact-dyadic Arb enclosure
\[
P/(8\pi^2)\in[0.995662732753254329\ldots,0.995662732771114200\ldots],
\]
\[
J_6/(8\pi^2)\in[0.995670030344086466\ldots,0.995670030355130639\ldots].
\]
Thus the isolated blow-up cost can be strictly below \(8\pi^2\) in negative Kähler--Einstein bulk. The area/collar sweeps suggest a finite-radius preferred scale, but do not prove existence or uniqueness of a complete-cell minimizer.

Primary paths: `workspace/data/o11_strict_arb_x001_X8_256.json`; `workspace/notes/step11_subthreshold_perpendicular_cell.md`; `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X64_d16.json`; `Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_{P,J,S}_exact.json`.

## 5. Cell infima, handles, and balanced upper bounds

Let \(\mathfrak P_{k,\ell}\) and \(\mathfrak J_{k,\ell}\) denote infima over smooth marked cells of topology \(D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\), exact CH on an outer collar, with radius allowed to vary.

### 5.1 Subadditivity and balanced specific energy — Proved at construction level

Disjoint placement gives subadditivity and therefore
\[
\gamma_{\rm bal}=
\lim_{n\to\infty}\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n}.
\]
This does not identify \(\gamma_{\rm bal}\) with the unrestricted closed-manifold \(\alpha\)-coefficient.

### 5.2 Pure handles — Proved sharp infimum

\[
\mathfrak P_{0,\ell}=\mathfrak J_{0,\ell}=32\pi^2\ell.
\]
For \(\ell>0\), the value is approached by shrinking cores and is not attained by a fixed smooth cell. Mixed-cell nonadditivity remains open.

### 5.3 Balanced ball-quotient upper law — Proved (Step 69, verified; supersedes the existential limsup)

Let \(p_c\) be the exact dyadic upper endpoint of \(P/(8\pi^2)\) for A01's certified \(x_0=3/100,X=128\) perpendicular cell, and put
\[
C_c=\frac{28}{9}+\frac89p_c=3.99614465135210151\ldots
\]
(\(J\)-route value \(3.996151138\); the improvement \(6.49\times10^{-6}\) is the cell's scalar-variance share).

- **Setting.** Fix a compact ball quotient and one preliminary finite cover whose deck group moves every point of a compact fundamental set by more than \(4R_c+2D\) (global injectivity radius \(>2R_c\)).
- **Statement.** For *every* further finite cover \(X_m\) and every \(n\) satisfying the packing inequality, let \(M=X_m\#8n\overline{\mathbb{CP}}^2\#7n(S^1\times S^3)\), with \(Q=36n\) and \(h=Q/A\). Then
  \[
  \frac{\alpha(M)}{h}\le\frac{C_c}{1+C_ch/4}.
  \]
- **Proof.** The cell has zero host mismatch on locally-CH hosts and \(P\) is exactly local where the host is Einstein. Handles are inserted at shrinking radius \(t=\sqrt\delta\) with cost \(32\pi^2+O(\delta^2)\). Conclude by the exact quotient \(\mathcal E(\widehat g)=16P/(4P+Y^2)\), \(Y^2\ge32\pi^2A\).
- **Scope.** Non-asymptotic in \(h\) and in cover degree. Fixed non-ball unramified hosts cannot reach the balanced small-\(h\) slice: there \(\sigma\to\infty\) and only the \(\theta\)-law holds. The lower (matching) side is open; it is the open-range problem of §21. Details: §22, `step69_P_form_upper_law_balanced_towers.md` §6.

## 6. A complete nonstandard-boundary Einstein filling (Theorem E)

### 6.1 Theorem — Proved by analytic local construction and validated flow

There exists a complete real-analytic diagonal Bianchi--IX metric on the total space of \(\mathcal O(-1)\to\mathbb{CP}^1\) satisfying \(\operatorname{Ric}=-6g\). It is ACH with fibre slot 1 and convergence rate at least \(O(e^{-1.99t})\). Its conformal infinity is a nonstandard Rossi sphere with
\[
\rho_\infty\in[2.19013,2.19242].
\]
The bolt has \(b=4/5\), while the free fourth-order anisotropy lies in the validated interval used by the Fuchsian/CAPD passage.

Proof components: analytic Fuchsian solution in \(s=t^2\); exact constraint propagation; source-level equivalence of the compact CAPD vector field and the Einstein system; interval transport of a tiled bolt family to a verified cusp block; opposite unstable-face crossings; Ważewski continuation; and quadratic drift control of
\[
\widetilde\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q.
\]

Primary paths: `workspace/notes/step15_ach_projected_theory.md`; `workspace/scripts/ach_bolt_fuchs.py`; `workspace/data/ach_capd/fuchs_boxes_N6_complex.json`; `workspace/scripts/ach_capd_field_check.py`; `workspace/data/ach_capd/wazewski_T2.75.json`; `workspace/scripts/ach_block_verify.py`; `workspace/scripts/ach_phi_drift.py`; `workspace/data/ach_capd/rossi_enclosure_b0.8.json`.

### 6.2 Exact bolt geometry — Proved

At \(b=4/5\), the scalar curvature is \(-24\). The earlier values \(\operatorname{diag}(-139/16,57/16,41/8)\) and \(\operatorname{diag}(-385/16,203/16,91/8)\) were produced by a symbol-collision bug in the peer script (peer message 771) and are withdrawn. The repaired exact computation, which agrees with the independent coordinate limit (operator norms \(39.3985\), \(194.083\)), gives the unordered chiral curvature-operator Weyl blocks
\[
\operatorname{diag}(-41/16,-41/16,41/8),
\qquad
\operatorname{diag}(-91/16,-91/16,91/8),
\]
   Neither bolt block has the Kähler--Einstein spectrum. More strongly, the CAPD off-bolt calculation now transports all forty outward-rounded analytic Fuchsian boxes to \(t=.5\) and proves that both chiral Weyl blocks have simple spectrum there. The weakest pairwise gap lower bounds are \(0.9669947784\) and \(0.003926698448\), and the discriminant lower bounds are \(66.1883\) and \(0.0006333125\). A point-box comparison with the independent coordinate/JAX curvature calculation agrees within \(5.6\times10^{-15}\). Thus the metric is not conformally Kähler on any nonempty open set in either orientation; analyticity excludes an open conformally Kähler region after the discriminant is nonzero at the certified orbit.

Primary paths: `Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py`; `workspace/scripts/ach_bolt_weyl_series_check.py`; `workspace/scripts/ach_weyl_interval.cpp`; `workspace/scripts/ach_weyl_interval_run.py`; `workspace/data/ach_capd/weyl_discriminant_t0.5.json`.

### 6.3 Relation to the marked-cell problem

Theorem E changes the boundary CR structure and therefore is not an exact-CH-collar zero-cost cell. The certified cheap cells also do not shadow this Einstein trajectory: their positive action is concentrated near a Burns-like core and their collar returns rapidly to CH. The theorem supplies a possible compactness endpoint and an existence result. Notation (used from here on): \(\mathfrak p^{\rm diag}_{1,0}=\inf_{\rm diagonal}P/8\pi^2\) (the diagonal exact-CH-collar infimum written \(p^{\rm diag}_{1,0}\) in §4.1) and \(\mathfrak P_{1,0}=\inf_{\text{all marked cells}}P\) (§5) are infima over different domains. The nonstandard-boundary filling supplies neither a zero exact-CH-collar cell nor a proof that \(\mathfrak P_{1,0}=0\); it also does not establish \(\mathfrak p^{\rm diag}_{1,0}=0\).

The Biquard--Herzlich identity places the convergent combined curvature integral against \(\chi-3\tau+\nu\). For the blown-up ball \(\chi-3\tau=5\); the standard sphere value leaves slack, so topology does not exclude a standard-boundary filling. Numerical branch-wide nonexistence at \(\rho=1\) remains open and would be dynamical even in the diagonal class. The off-bolt conformal-Kähler question is now closed by the interval theorem in §6.2.

## 7. Common mechanism and its present mathematical scope

The proved pieces support the following schema. Actual metric-wise fields and their differential prolongations control regular bulk geometry. A topology change is realized by a complete marked cell whose leading response depends on the ambient self-dual curvature, not solely on the topology. Kernel directions can evade the linear payment and exploit a negative quadratic interaction. Volume entropy supplies a separate field-free obstruction to exact Einstein metrics on real-hyperbolic blow-ups. Pure handles retain the exact \(32\pi^2\) cost, while blow-ups admit certified costs below \(8\pi^2\) in CH bulk. Exact Einstein filling can occur after moving the CR boundary away from the standard CH value. The unrestricted \(\alpha\)-problem requires a compactness/localization theorem linking global near-minimizers to these bulk and cell objects.

The general-bulk first-order law is now proved as an upper construction (Theorem F). The local second-order remainder on \(P\)-critical backgrounds is Theorem 59.R (§20), with the strict KE upper bound Corollary 59.KE. The unrestricted global passage, positivity of \(\mathfrak P_{1,0}\), global–cell asymptotic equality, standard-CR diagonal nonexistence and degeneration control remain unresolved. No unrestricted remainder theorem for arbitrary non-\(P\)-critical backgrounds is asserted. Two rigid inputs constrain degeneration. First, an almost-Euclidean neck enclosing a blow-up class carries \(P\ge8\pi^2-C\varepsilon\), and a scalar-flat ALE bubble with \(\Gamma=1\) carries \(P\ge8\pi^2(k+4\ell)\). Second, no nontrivial exact-CH-collar cell is Einstein: the locally symmetric developing-map argument removes the temporary \(\ell=2k\) exception. Hence \(\mathfrak P_{1,0}<8\pi^2\) forbids almost-flat concentration of the class, and \(\mathfrak P_{k,\ell}=0\) for any \((k,\ell)\ne(0,0)\) requires escape of the collar, collapse, or concentration through curved necks.

The real-hyperbolic contrast now has two theorems beyond the numerical scan. On closed \(Y\#k\overline{\mathbb{CP}}^2\) with \(s=-12\), a Ricci floor \(\operatorname{Ric}\ge-3(1+\varepsilon)g\) gives
\[
P\ge8\pi^2k-12\operatorname{Vol}(Y)[1-(1+\varepsilon)^{-2}]
\]
by BCG entropy and Bishop comparison. For a complete exact-\(H^4\)-exterior cell, the scalar floor \(s\ge-24\) forces the manifold to be hyperbolic by the non-spin Chruściel--Delay positive-energy theorem in dimension four. Details and sources are in `workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md`.

**Two-channel cell identity (Theorem C, Steps 23–24).** For a complete cell of marked topology \((k,\ell)\), exactly equal to the model outside a compact set for a fixed end marking, with Yamabe representative \(\hat g=u^2g\), \(\hat s=-24\), \(u\to1\) (derivative decay faster than inverse volume growth),
\[
P_{\rm cell}-8\pi^2(k+4\ell)=4\Delta W_++48\,\mathrm{RV}(\hat g)+3\int(\Delta u/u)^2+24\int|\nabla u|^2,
\]
where \(\mathrm{RV}\) is the matched relative volume: matched truncations of cell and model plus the whole-cell integral \(\int(u^4-1)d\mu_g\). For exact-CH ends \(u\) exists uniquely for **every** smooth cell (S1003A01 weak-barrier theorem, no sign condition on \(s\)), so the exact-ended \(J_6\) infimum equals the \(P\) infimum over complete scalar \(-24\) metrics asymptotic to the marked CH end at rate \(>4\). The H\(^4\) cell bound \(P\ge8\pi^2\) is reduced to \(\mathrm{RV}(\hat g)\ge0\). Numerically (11 diagonal cells, both bulks, \(x_0\le1\)) \(\mathrm{RV}(\hat g)>0\) always; \(48\mathrm{RV}\approx-x_0s_p/12\) and \(4\Delta W_+\approx-x_0W^+_p(\zeta,\zeta)\) to first order: the two halves of \(\mathbf R^+\) in Theorem F are the volume and Weyl channels. The certified CH witness pays \(+0.0706\) in volume and saves \(-0.0747\) in Weyl (units \(8\pi^2\)). The scalar floor does not separate the two bulks (both families of competitors dip below the background scalar); the Weyl channel does. Relative signature for the one-blow-up CH cell gives \(\Delta W_+-\int|W^-|^2=-12\pi^2\); at \(P=0\) Theorem C then reproduces the relative Biquard–Herzlich identity, \(\mathrm{RV}=5\pi^2/6-\int|W^-|^2/12\), so these identities alone give no obstruction to a standard-CR Einstein filling.

**Monopole estimates give no per-blow-up cell payment (Step 24).** For minimal general type \(X\), LeBrun's convex invariant satisfies \(\beta^2(X\#k\overline{\mathbb{CP}}^2)=c_1^2(X)\), independent of \(k\): averaging the monopole classes \(\pm c_1(X)\pm E_1\pm\cdots\pm E_k\) puts \(c_1(X)\) in the convex hull, and scalar-recovery metrics give the reverse inequality (`Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`). Thus \(\int s^2\) and \(\int(s-\sqrt6|W_+|)^2\) see only the minimal model; the \(k\)-dependence of \(8\pi^2(k-A/3)\) enters only through \(\chi,\tau\) in Chern–Weil. Positivity of \(\mathfrak P_{1,0}\) must come from intrinsic Weyl–volume geometry, not from localizing a Seiberg–Witten estimate.

## 8. The missing global passage

**Steps 33–34: characteristic–constraint link calculus (proved identities and corrected consequences).** For every compact \(\Omega\subset M\) with smooth boundary,
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2+\frac1{96\pi^2}\int_\Omega s^2-(2\chi\pm3\tau)(\Omega)+\mathcal Q_\pm(\partial\Omega),\qquad\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\]
with \(\mathcal E\) Chern's boundary term and \(\mathcal H=\eta+\int T_{p_1}\) the APS boundary term (Theorem G). Verified model charges are: round flat-conical link \((2,2)\); flat-conical/ALE \(S^3/\Gamma\) limit \((2/|\Gamma|\mp3\eta_\Gamma)\), recovering Lemma Q; a fixed-smooth-metric thin tube around a surface of self-intersection \(n\), \((2\chi(\Sigma)\pm3\operatorname{sgn}n)\), giving the bolt \((1,7)\); the controlled Taub–NUT-chirality Hopf-adiabatic link \((-2,2)\), with the opposite chirality \((2,-2)\); and the CH sphere \((2-9\sinh^4\tau,2-3\sinh^4\tau)\). The radial collar jet is part of every charge. For \(D\cong(\#k_D\overline{\mathbb{CP}}^2\#\ell_D S^1\times S^3)\setminus B^4\),
\[
P(g)\ge8\pi^2[k_D+4\ell_D-(2-\mathcal Q_+(\partial D))].
\]
Disjoint regions add. For one blow-up with \(\widehat P<1-\varepsilon\), a standard negative-definite blow-up region has \(\mathcal Q_+\le1+\widehat P<2-\varepsilon\); therefore an exceptional subtree cannot be separated from the bulk by a \(C^2\)-Euclidean-round \(S^3\) germ. This does not exclude orbifold necks, Taub–NUT-chirality collapse, curved/sheared links, bulk bubbling, or regions containing positive intersection form.

The complementary symmetry-free foliation identity is
\[
|\operatorname{Ric}^\circ|^2=\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2,
\quad
\mathcal C=\tfrac12(\Theta^2-|K|^2-R_h)+s/4,
\quad
\mathcal J=\operatorname{div}K-d\Theta,
\]
where \(\mathcal S\) is the trace-free tangential evolution residual. Lemma N is the diagonal Hamiltonian component; Lemma P and fibre/base pinning use the two diagonal tangential-evolution projections, not the Codazzi component. Exact transport identities tested against \((\mathcal C,\mathcal J,\mathcal S)\) give weighted Cauchy–Schwarz lower bounds. Thus characteristic transgressions price topology and boundary-germ changes, while Gauss–Codazzi/evolution residuals price drift-corrected shape changes. Their bounds are generally combined by a maximum unless regions or orthogonal components are separated. **Link regularity** is control/convergence of the intrinsic link geometry, second fundamental form, characteristic and Dai spectral transgressions, and the field boundary data actually used on the bulk. Critical \(L^2\) defect alone does not establish it. Details: `notes/step33_link_charges_global_decomposition_static_channel.md`, `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, and the Step-34 TTCS integrations.

The classical handle-free lower interval is
\[
8\pi^2\max\{0,k-A/3\}\le\inf P\le8\pi^2k,
\]
so present lower information vanishes for \(0<k<A/3\). A successful global passage must do more than extract an ideal limit: it must preserve family-uniform scale control, distinguish collapse from noncollapsed convergence, identify the CH bulk through actual-field coercivity, assign topological charge to complete bubbles or cells, and compare asymptotically CH cells with exact-collar infima by truncation.

On the scalar-minus-four class, put
\[
R_1(g)=\int_M|\nabla\operatorname{Rm}_g|^2\,d\mu_g.
\]
If \(P(g_0)\le p+\delta\), \(0<R_1(g_0)<\infty\), \(\varepsilon=\delta/R_1(g_0)\), and \(g\) is a \(\delta\)-near-minimizer of \(P+\varepsilon R_1\), then the elementary comparison proves
\[
P(g)-p\le3\delta,\qquad R_1(g)\le3R_1(g_0).
\]
This selection lemma is valid and needs neither an attained minimum nor a gauge. It does not yet give a uniform compactness theorem: the comparison \(g_0=g_0(\delta)\) may have \(R_1(g_0)\to\infty\), the certified upper construction is not known to be \(\delta\)-close to the unknown infimum for arbitrarily small \(\delta\), and an intrinsic derivative-curvature bound gives a uniform \(L^4\) bound only after a uniform Sobolev or harmonic-radius input. Across the balanced family, even an extensive bound \(R_1=O(A)\) permits scales of order \(A^{-1/2}\) and is not local equiintegrability. The corrected statement and the independent reading of Theorem E are in `workspace/notes/step19_theorem_package_and_selection_lemma.md`.

## 9. Historical research targets (Step 25 list), with current theorem status supplied by later sections

1. Prove positivity of the absolute cell channel \(\inf\{8\pi^2+4\Delta W_++48\mathrm{RV}(\hat g)\}>0\) over complete scalar \(-24\) metrics asymptotic to the standard marked CH end on \(O(-1)\). (The earlier linear trade-off \(4\Delta W_+\ge-\Lambda48\mathrm{RV}-\eta\), \(\Lambda\in[1.03,1.06]\), is withdrawn: \(\Lambda\to1\) is forced by Theorem F in the kernel direction and \(\Lambda>1\) gives no absolute bound.) The first complete form of this is the diagonal compactness/trichotomy theorem of `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`.
2. Real-hyperbolic: prove \(\mathrm{RV}(\hat g)\ge0\) for \(\hat s\equiv-24\) AH metrics on \(D\#k\overline{\mathbb{CP}}^2\) conformal to exact-collar metrics (local topological Schoen problem), and on the closed side the identity \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}\), which is now the only input missing from the sharp theorem H.
3. Study the regularity profile \(\mathcal R_*(\delta)=\inf\{R_1(g):P(g)\le p+\delta,\ s_g=-4\}\), and either bound it uniformly or derive a local Sobolev/harmonic-radius estimate from the penalized equation with constants that survive \(\varepsilon\to0\).
4. Use actual-field coercivity to identify a noncollapsed bulk and localize topological charge; separately analyze collapse and the entropy/Ricci critical-exponent obstruction.
5. Truncation is proved in the recorded diagonal ACH class and in the marked rate-\(>4\) setting supplied by Theorem C/Theorem T. Extension beyond those hypotheses, positivity of the unrestricted cell infimum \(\mathfrak P_{1,0}\), and identification of global near-minimizers with such cells remain unresolved.
6. Analyze the exact-standard-CR endpoint in and beyond the diagonal class. Theorem E now has certified non-conformal-Kählerness, but its Rossi boundary remains nonstandard.


## 10. Step-47 synthesis: diffuse quadratic scale, new global inputs, and next proof object

Source: `workspace/notes/step47_consolidation_two_scale_program.md`; independent checks: `trace/ttcs/results/step47_ttcs01_{verifier1,reviewer1}_integration.md`; new source collection: `Knowledge/materials/openai-math-20261007/`.

**Formal common-mode/Theorem-K consistency — exact algebra, not a closed construction.** Put \(h=k/A\), \(r=2-h\). Using the axial common-mode ansatz,
\[
\frac{P_{\rm form}}{8\pi^2k}=\frac{h(1+h)}{(2-h)^2},
\qquad
P_{\rm form}=2\pi^2\frac{k^2}{A}(1+2h+O(h^2)).
\]
Moreover
\[
D_{\mathcal K}:=\int\operatorname{dist}(W^+,\mathcal K)
=\frac{4\sqrt6\pi^2k}{(2-h)^2},
\]
while Theorem K requires
\[
D_{\min}=\frac{\sqrt6\pi^2(4-5h)k}{(2-h)^2},
\qquad
\frac{D_{\mathcal K}}{D_{\min}}=\frac4{4-5h}\to1.
\]
The slack satisfies \((4\sqrt6/3)D_{\mathcal K}-(8\pi^2k-P)=5P/(1+h)\), hence is itself order \(k^2/A\). This verifies compatibility and first-order sharpness of K on the formal state; Lemma T excludes the exact state on a closed blow-up, so it is neither an upper construction nor a proved lower law.

**Diffuse quadratic-transport conjecture — open.** For specified pure-blow-up cover families with uniform constants, the evidence supports a diffuse-channel scale \(P\gtrsim k^2/A\), while per-class cost may vanish as \(k/A\to0\). The lower side would follow from a noncircular Cotton/transport bound for the unweighted \(R_0=\mathbb E\int|\nabla n|_{W_2}^2\), together with \(P\ge8\pi^2k-2R_0\); the weighted energy \(R_\rho\) has different normalization. No unrestricted quadratic estimate and no matching closed upper family are proved.

**New source transfers.** The De Giorgi source proves a same-amplitude stability identity with a negative defect-mass term and a branch-combination variance; the naive SW test \((0,\eta\Phi)\) has only positive terms, so an SW transfer requires a genuinely coupled connection–spinor variation. The Coulomb source proves geometry only for finite-volume minimizers and then transfers the bound by one globally compatible dual identity; it reinforces that exact-cell entry must be proved for minimizing objects or replaced by a direct global estimate. Family 348 supports Bianchi-first representation decomposition but its final positivity uses \(\sec\ge0\), retains \(W^-\), and acquires Cotton sources near Einstein metrics. Hypersymplectic Lemma 10.4 gives \(\|h\|_2^2=2\|h^+\|_2^2\) for exact two-forms and can help period-preserving collar correction, but it does not control Weyl-alignment tensors or harmonic exceptional charge. Family-351 collar/tree mechanisms remain conditional and do not automatically preserve the quadratic leading term of \(P\).

**O10 endpoint sharpened.** Under full conformal-class actual supply, resetting the finite-density budget to \(A=p=(a_g^+)^2\) proves that any remaining \(\beta\to\infty\), \(\kappa_\beta\to0\) sequence has \(\chi/p\to\infty\), \(p/V\to2/(9\pi^2)\), and \(W^-/V\to\infty\). Density-free O10 is therefore an unbounded actual-density problem. Positive-current concentration suggests a possible closed limiting object only after the current, positivity, closure and uniform directional/transverse moments are derived from the field equations.

**Additional normalized gap and Ricci-flow consequence.** Assuming the external scalar–simplicial-volume theorem, \(H=a_4\|M\|>0\) and \(b=96\pi^2(2\chi-3|\tau|)_+/H<1\) imply \(\mathcal E\ge\mathcal J\ge4(1-b)/(4-b)\); this does not determine the balanced small-\(h\) coefficient, where \(b>1\). Assuming family 351 Theorem 1.1, \(Y(M)<0\) and \(\inf P>0\) force scalar curvature to become unbounded on every maximal volume-normalized Ricci flow. The immortal argument uses \(\bar s'=2P/V-\frac12\operatorname{Var}(s)\); the finite-time branch converts to unnormalized flow and invokes bounded-scalar extension.

**Step-47 localization target and subsequent result.** The target below was subsequently realized under the CH-entrance and gauge hypotheses of Theorem 48.L, with the Yamabe/core formulation in 48.LY (§11). Unrestricted entrance and the per-core Weyl–volume inequality remain unresolved. Original target: localize the Riemannian half of \(A_C\): on \(\Omega\Subset\Omega_1\) uniformly close to complex hyperbolic geometry in scalar-normalized DeTurck/Bianchi gauge, bound both Weyl-block departures and the quadratic scalar/volume departure on \(\Omega\) by \(\int_{\Omega_1}|\operatorname{Ric}^\circ|^2\) plus an explicit gauge-invariant collar/outer-layer flux. This does not yet select monopole branches. It would force the order-\(k\) curvature budget of subunit metrics into nonperturbative cores/collars and provide the entry needed before marked-cell bounds can govern the unrestricted infimum.


## 11. Step 48 — The Yamabe channel and localized CH coercivity (proved; details `step48_yamabe_channel_and_localized_CH.md`)

**Prop. 48.1 (exact).** The Theorem-W/K saving density simplifies to \(f(W,r,n)=-r^2W(n,n)-4|W|^2+p(r)\); hence \(\sup_{r\le2,n}f=\varphi(-\mu_{\min}W)-4|W|^2\) with \(\varphi(x)=\tfrac12(\tfrac{6x+14}9)^3-\tfrac43\) (\(x\le\tfrac23\)), \(4x\) (\(x\ge\tfrac23\)). Theorem W's pointwise content sees \(W^+\) only through \(\mu_{\min}\) and \(|W^+|\); \(C_{\mathcal K}=4\sqrt6/3\) is recovered.

**Lemma 48.2.** \(\Psi:=\tfrac43+2|W|^2-\varphi\ge\tfrac{10}9\operatorname{dist}(W,\mathcal K)^2\) (sharp, exact eigenvalue formulas).

**Theorem Y.** Under the sign-family hypotheses, with \(\hat g\) the \(s\equiv-4\) Yamabe metric, \(\Delta V=\hat V-2\pi^2A=(Y[g]^2-32\pi^2A)/16\), \(D_W=\int(\tfrac23-|W^+|^2)\): exact (Y0) \(8\pi^2k-P(\hat g)=4D_W-4\Delta V\), and
\[
8\pi^2k-P(g)\le4\Delta V-2\int\Psi\le4\Delta V-\tfrac{20}9\int\operatorname{dist}(W^+,\mathcal K)^2 .
\]
LeBrun's Prop. 4 gives independently \(8\pi^2k-P(\hat g)\le4\Delta V-\tfrac49\int(\sqrt6|W^+|-2)^2-16\pi^2\Pi_g\), \(\Pi_g=(a^+)^2-A\ge|K^-|^2+\sum|E_i^+|^2\), and \(\Delta V\ge2\pi^2\Pi_g\). The leading "saving \(\le4\times\)Yamabe excess" is LeBrun's; Theorem Y adds quadratic control of upper-pair splitting (\(8\sigma^2\), invisible to LeBrun at quadratic order) and of excess magnitude. **Cor. Y1:** \(P\le8\pi^2ck\Rightarrow\Delta V\ge2\pi^2(1-c)k+\tfrac59\int\operatorname{dist}^2\), i.e. \(Y[g]\le-4\pi\sqrt{2(A+(1-c)k)}\). **Cor. Y2:** \(\inf P\ge8\pi^2ck\iff D_W-\Delta V\le2\pi^2(1-c)k\) on Yamabe metrics; fields give \(D_W-\Delta V\le\Delta V-\tfrac12\int\Psi\). The formal common mode saturates LeBrun's estimate exactly (forcing \(\Pi_g=0\), the Lemma-T-forbidden null periods) and Theorem Y to leading order (slack \(O(k^2/A)\)).

**Prop. 48.3 / 48.4 / Theorem 48.L (Riemannian, no field selection).** On every closed ball quotient, \(L=\tfrac12(\nabla^*\nabla-2\mathring R)\ge1\) (TT: Koiso; gauge+trace sector \(\ge6\) by the intertwining \(LT=TD\), using only \(\Delta_H,\Delta_0\ge0\)). Combes–Thomas: \(\|e^\phi L^{-1}e^{-\phi}\|\le(1-a^2/2)^{-1}\), \(|d\phi|\le a<\sqrt2\). Hence, with gauge assumed and smoothed distance, \(\|h\|_{H^2(\tilde d\ge T)}\le C(\|\operatorname{Ric}^\circ\|_{L^2}+e^{-aT}\Lambda)\), constants independent of \(\Gamma,k\) and core positions. Lemma 48.5: bulk volume change \(=\tfrac1{24}\oint\partial_\nu\operatorname{tr}h+O(\|h\|_{H^2}^2)\) at \(\operatorname{Ric}=-6\) (scalar constraint in Bianchi gauge, \(s'=\tfrac12(\Delta+12)\operatorname{tr}h\)).

**Theorem 48.LY.** If \(X\) is a ball quotient and the Yamabe metric is uniformly locally \(C^{2,\alpha}\)-close (in gauge) to it outside enlarged cores \(U_2\), then \(P(g)\ge(8\pi^2k-4\Delta V_U-C\Lambda^2)/(1+C)\) with cover-independent \(C\), where \(\Delta V_U\) is the marked core Yamabe/relative-volume excess (with interface flux). In this regime diffuse bulk saving is absent at linear order; a subunit family must carry core relative-volume excess \(\ge2\pi^2(1-c)k\) or collar mismatch \(\Lambda^2\gtrsim k\).

**Einstein tails (diagonal SU(2) sector of \(\mathbb{CH}^2\)).** Radial-gauge indicial roots: J-anti triaxial \(0,4\) (marginal \(e^{-4r}\) against volume \(e^{4r}\); first-order invisible to \(\mu_{\min},|W^+|\)); U(2) \(-2,0,6\) (\(\nu=8\) of the spatial determinant violates \(E_{00}\)). Step 49 computes the \(\nu=4\) split: \(e^{4r}\partial_\varepsilon W^+|_0\to\operatorname{diag}(-12,12,0)\) at \(\operatorname{Ric}=-6\), hence a marginal linear Theorem-K tail but integrable quadratic \(\Psi\).

**Open after Step 48.** The per-core inequality \(D_{W,U}-\Delta V_U\le(1-c_0)2\pi^2\) for marked cells with CH-asymptotic collars; the far-from-CH regime (where the formal common mode lives, financed by \(\Delta V\approx2\pi^2k\)); non-ball-quotient hosts; full indicial spectrum.


## 12. Step 49 — certified-cell Theorem-Y anatomy and the marginal triaxial tail

**Corrected cell ledger (floating spectral/relative-volume measurement; \(P\) itself remains interval certified separately).** For the authoritative \(x_0=.03,X=128\) cell, in scalar-\(-4\), \(8\pi^2\)-normalized units,
\[
1-P(\widehat g)=0.0043391,\quad \Delta V=0.053096,\quad
\delta W=0.018784,\quad D_W=\delta W+\tfrac23\Delta V\simeq0.05418.
\]
Thus \(4D_W\simeq0.21672\), \(4\Delta V\simeq0.21238\). The old \(0.07513,0.07080\) pair meant \(4\delta W,(4/3)\Delta V\), not \(4D_W,4\Delta V\). The new eigenvalue quadrature gives
\[
\int\Psi/(8\pi^2)=0.0132326119,
\quad \int\operatorname{dist}^2/(8\pi^2)=0.00750240585,
\quad \int4\sigma^2/(8\pi^2)=0.0109217156.
\]
The correct Theorem-Y allowance is \(4\Delta V-(1-P(\widehat g))\simeq0.2081\), not the superseded \(0.0332\). The cell uses only about \(2.04\%\) of \(4\Delta V\) as direct saving and is far from equality in Theorem Y and the zero-period version of LeBrun's estimate; full LeBrun equality also depends on the closed replica's period term. Details and reproducible files: `step49_cell_Y_measurement_bad_set_obstruction.md` and `scripts/step49_cell_theoremY_profile.py`.

**Marginal triaxial Weyl split (exact first order).** For the \(\nu=4\) Einstein tail \(A=\sinh r(1+\varepsilon e^{-4r})\), \(B=\sinh r(1-\varepsilon e^{-4r})\), \(C=\sinh r\cosh r\),
\[
e^{4r}\delta W^+\to\operatorname{diag}(-12,12,0)
\]
at \(\operatorname{Ric}=-6g\) in the two horizontal and fibre spin slots. At scalar \(-4\), the upper pair splits by \((-2,2)\varepsilon e^{-4r}+O(\varepsilon e^{-6r})\), while \(\mu_{\min}\) and \(|W^+|^2\) have zero first variation. For the sorted half-gap, \(\sigma=2|\varepsilon|e^{-4r}+O(|\varepsilon|e^{-6r})+O(\varepsilon^2e^{-8r})\). Hence Theorem K has a marginal linear \(L^1\) tail, whereas \(\Psi=16\varepsilon^2e^{-8r}+O(\varepsilon^2e^{-10r})+\cdots\) is integrable.

**All-metric unit-ball counting is not established.** Scalar normalization and critical \(L^2\) defect do not give small-energy regularity or a pointwise CH entrance for arbitrary metrics; an order-\(k\) Weyl departure may concentrate in one unit ball carrying many exceptional classes; and arbitrary competitors have no canonical marked ball-quotient bulk. What follows unconditionally is a weighted concentration relation using
\[
\int(|W^+|^2+1/3)=2\pi^2(A-k)+P/4,
\]
not a linear lower bound for the number of bad balls. With \(d_K=\operatorname{dist}(W^+,\mathcal K)\), \(\mathcal L=(8\pi^2k-P)_+/(4\sqrt6/3)\), the exact eigenvalue formula gives \(d_K^2\le2(|W^+|^2+1/3)\), hence
\[
\mathcal L^2\le\operatorname{Vol}(M)[4\pi^2(A-k)+P/2],
\]
and \(\operatorname{Vol}\{d_K>\tau\}\ge(\mathcal L-\tau\operatorname{Vol}M)_+^2/[4\pi^2(A-k)+P/2]\). Theorem 48.L controls the flux-corrected bulk volume; the uncorrected bulk volume retains its linear interface flux. A genuine count requires variational selection of near-minimizers, an approximate elliptic equation, small-energy regularity, and a uniform upper bound on the geometric/topological load per concentration atom. Theorem 48.L controls the *bulk* relative volume by bulk defect plus interface flux after CH entrance; it does not control the core part of \(\Delta V_{\rm free}\).


## 13. Steps 50–52 — minimizing-object entry, Kähler infimum, and Kronheimer absorption (details: `step51_residual_entry_link_charges_and_kahler_recovery.md`, `step52_residual_norm_selection_absorption.md`)

**Proved.**
- *Theorem \(K_\infty\).* For a minimal general-type \(X\) and the fixed complex structure \(J\) of any \(k\) successive (possibly infinitely near) blow-ups,
  \(\inf_{\rm K\ddot ahler\ for\ J}P=8\pi^2k\), not attained for \(k\ge1\). Lower bound: total-transform classes and Hodge index for nef and big \(\pi^*K_X\).
  Recovery: Arezzo–Pacard desingularization of the KE canonical orbifold, then successive smooth blow-ups with independent parameters. The recovery metrics
  are Yamabe representatives at \(s=-4\) with \(D_W=0\), \(P-8\pi^2k=4\Delta V\to0\).
- *Weighted descent.* \(Q(\lambda^2g)=\lambda^{-2}Q(g)\); \(\rho^4|Q|^2d\mu\) scale invariant; fixed-weight DeTurck flows are strongly parabolic with
  \(P'=-\int w|Q|^2\); a flow on \([0,S]\) yields \(t_*\) with \(\int w|Q|^2\le\frac2S(P(g_0)-P_*(M))\); a minimizing sequence with flow times \(T_i\gg\delta_i\)
  yields weighted Palais–Smale data. The weighted flow is horizontal for \(\langle h,h\rangle_w=\int w^{-1}|h|^2\).
- *Residual norm (Prop. 52.1–52.2).* An own-scale \(L^2\) residual with \(L^6\) curvature control gives \(W^{4,2}\) harmonic-coordinate bounds, strong \(L^q\)
  convergence of curvature and exact smooth \(P\)-critical limits; it does not give pointwise curvature control (logarithmic-cloud example through
  \(c_0\Delta s=\operatorname{tr}Q\)). Point-picking must use integral radii (\(r_\varepsilon\), \(r^{(6)}\)).
- *Link ledger.* Multi-ended and inner-link Theorem-G formulas; Burns 1, EH 0, Kronheimer 0 (\(3\eta_\Gamma=r-2+2/|\Gamma|\)); single-ended \(\Gamma=1\)
  negative-definite bubbles pay \(\ge b_2+4b_1\).
- *Kronheimer absorption (Lemma 52.6, Theorem 52.7a).* \(X\#2m\overline{\mathbb{CP}}^2\) is the resolution of \(X\#m(S^4/\mathbb Z_2)\) by \(2m\) Eguchi–Hanson
  spaces (\(T^2\)-equivariant; Orlik–Raymond); the exceptional classes \(E_{2j-1},E_{2j}=\tfrac12(e_j\pm f_j)\) lie in the rational span of the bubbles. A direct proof of the smooth identification is recorded in `notes/step93_paired_A1_transfer_review.md`: the resolved football is simply connected, has an effective \(T^2\)-action with four-edge orbit disk and form \(-I_2\), hence is \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\).
  Lattice facts: a single \(A_1,A_2,E_6,E_7,E_8\) absorbs nothing; \(A_1^{\oplus2}\subset\mathbb Z^2\), \(A_3\subset\mathbb Z^3\), \(D_n\subset\mathbb Z^n\) absorb.
  A single exceptional direction cannot be absorbed by a root lattice contained in its rational span. At \(k=1\), exclusion of more general Kronheimer absorption requires additional degree-one/lattice hypotheses, including SW\(_L\) where invoked; mixed host–exceptional root lattices are not excluded by the elementary rank-one calculation alone.
- *Corollary 52.8 (repaired Step 86).* Write \(P_{*,\rm orb}(V)\), \(\alpha_{\rm orb}(V)\) for the infima of \(P\) and \(\mathscr D\) over orbifold metrics on \(V\), and \(P_*^\iota,\alpha^\iota\) for infima over \(\iota\)-invariant metrics, \(\iota\) the summand-exchanging involution of \(X\#X\) with two isolated fixed points, so that \(X\#S^4/\mathbb Z_2=(X\#X)/\iota\).
  - *P-statements [P].* \(P_*(X\#2m\overline{\mathbb{CP}}^2)\le P_{*,\rm orb}(X\#m\,S^4/\mathbb Z_2)\), \(P_*(X\#Q_3)\le P_{*,\rm orb}(X\#\Sigma_4)\); since \(P\) doubles under the double cover, \(P_{*,\rm orb}(X\#S^4/\mathbb Z_2)=\tfrac12P_*^\iota(X\#X)\) and \(P_*(X\#2\overline{\mathbb{CP}}^2)\le\tfrac12P_*^\iota(X\#X)\). For ball-quotient \(X\), Step 93 computes \(P_{*,\rm orb}(X\#mS^4/\mathbb Z_2)=16\pi^2m=8\pi^2k\), and this infimum is not attained.
  - *α-statements [P, via Lemma 86.S].* \(\mathscr D\) is invariant under finite (orbifold) coverings: \(\int|\mathrm{Ric}-\lambda g|^2\) and \(\operatorname{Vol}\) scale by the same degree. Hence \(\alpha(X\#2m\overline{\mathbb{CP}}^2)\le\alpha_{\rm orb}(X\#m\,S^4/\mathbb Z_2)\), \(\alpha(X\#Q_3)\le\alpha_{\rm orb}(X\#\Sigma_4)\), and \(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)=\alpha^\iota(X\#X)\), **with no factor \(\tfrac12\)**. The Step-52 form \(\alpha\le\tfrac12\alpha^\iota\) was written for \(P\) before the Step-70 split and is withdrawn as a statement about \(\mathscr D\). For ball-quotient \(X\), Step 93 gives \(\alpha_{\rm orb}(X\#mS^4/\mathbb Z_2)=\min\{1,8m/(A+2m)\}\), nonattained except possibly at \(2m=A/3\).
- *Lemma 86.S (continuity of \(\mathscr D\) under Ricci-flat ALE resolution) [P, Steps 86–87].* Let \((V,g)\) be a compact orbifold metric, smooth in orbifold charts, with isolated singular points \(p_j\), local groups \(\Gamma_j\subset SO(4)\) acting freely on \(S^3\), and \(\mathrm{Ric}_g\not\equiv0\). Let \((N_j,h_j)\) be Ricci-flat ALE spaces asymptotic to \(\mathbb R^4/\Gamma_j\) with an orientation-matched equivariant end identification and \(h_j-\delta=O(r^{-\tau})\) together with two derivatives, some \(\tau>0\). \(\tau=4\) with all derivatives for every Ricci-flat ALE filler used here. For \(A\)-type (Eguchi–Hanson, Gibbons–Hawking) spaces and Šuvaina's spaces \cite{suvaina2011ale}, including the minimal resolutions of singular fibres (Definition 1.1 records order-four metric decay), derivative control follows from the centred finite-centre Gibbons–Hawking formula and the free finite quotient. For Kronheimer \(D/E\) spaces that formula is unavailable; the derivative-controlled order-four decay is Bando–Kasue–Nakajima's theorem for four-dimensional Ricci-flat manifolds with Euclidean volume growth and finite \(\int|\mathrm{Rm}|^2\), in the all-derivative sense of \cite{lidimensional} Definition 1.2 and Theorem 2.4 (Step-97/98 source repair; the lemma's proof is unchanged). Glue \(\varepsilon^2h_j\) into orbifold normal coordinates at \(p_j\) with a cutoff at \(r\in[\rho,2\rho]\), \(\rho=\varepsilon^{\tau/(\tau+2)}\). For finite ALE trees, every relative inner smoothing parameter must tend to zero independently.
    - *Proof.* On the annulus the scaled \(C^2\) error is \(\eta=\rho^2+(\varepsilon/\rho)^\tau\); the choice of \(\rho\) balances the terms. \(|\mathrm{Ric}|\le C\rho^{-2}\eta=O(1)\) on volume \(O(\rho^4)\). Inside, \(\mathrm{Ric}=0\) on volume \(O(\rho^4)\); outside, the metric is \(g\). Hence \(V\), \(\int s\), \(\int s^2\), \(R=\int|\mathrm{Ric}|^2\), \(P\), and \(L_s\) all change by \(O(\rho^4)\). Since \(\mathscr D=4-(\int s)^2/(\operatorname{Vol}\cdot R)\) is continuous on \(\{R>0\}\), \(\mathscr D(g_\varepsilon)\to\mathscr D(g)\). Bubble trees (ALE orbifolds with further singular points) are handled by iterating at successively smaller scales; each inner parameter contributes its own \(O(\rho_j^4)\) error. \(\square\)
    - *Consequences.* \(\alpha(\text{resolution})\le\alpha_{\rm orb}(V)\). If \(g\) is Einstein with \(\lambda\ne0\), then \(\mathscr D(g_\varepsilon)=O(\rho^4)\to0\), so every Ricci-flat-ALE resolution or Milnor-fibre smoothing of a nonzero-scale Einstein orbifold has \(\alpha=0\). The scalar-variance and Ricci errors are automatically \(O(\rho^4)\): the "vanishing scalar-variance" proviso attached to Cor. 52.9, 56.A–B and Prop. 58.O since Step 71 is a consequence, not an extra hypothesis. A Ricci-flat orbifold gives \(P_*=0\) after resolution. Its naive cutoff gluing has \(\mathscr D\to4\): scalar curvature is supported in a region \(U_\varepsilon\) with \(\operatorname{Vol}(U_\varepsilon)\to0\), so \((\int s)^2\le\operatorname{Vol}(U_\varepsilon)\int s^2\le4\operatorname{Vol}(U_\varepsilon)R\), giving \(4-\mathscr D\le4\operatorname{Vol}(U_\varepsilon)/V\to0\). This construction alone does not determine \(\alpha(M)\); for the Kummer resolution, \(\alpha(\mathrm{K3})=1\) by the unit-wall theorem (\(2\chi=3|\tau|\)). Rates better than \(O(\rho^4)\), such as the \(a^4\) law of §20.6, need corrected (Ozuch-type) metrics; the lemma makes no claim about them, nor about smooth Einstein metrics on the resolution.
    - *Negative-Yamabe exclusion.* For \(M=X\#k\overline{\mathbb{CP}}^2\), \(\mathcal Y(M)=-4\pi\sqrt{2A}<0\), so every metric satisfies \(\int(s^-)^2\ge32\pi^2A\) (Hölder: \(\mathcal Y\ge-\|s^-\|_2\)). A resolution of a Ricci-flat or positive-Einstein orbifold has \(\|s^-\|_2\to0\), contradicting this. Hence within these resolution/smoothing architectures, every absorbing Einstein orbifold for a general-type blow-up necessarily has \(\lambda<0\), making the nonzero-scale condition automatic.
    - *Numerical check [N].* `scripts/step86_lemma86S_check.py` → `data/step86/lemma86S_check.json`: round \(S^4/\pm1\) (\(\mathrm{Ric}=3g\)) resolved by two EH spaces of scale \(a\) with naive \(U(2)\)-invariant cutoff gluing at \(\rho=a^{2/3}\) (a metric on \(\mathbb{CP}^2\#\mathbb{CP}^2\)). Sympy Ricci of the profile reproduces \(s=12,|\mathrm{Ric}|^2=36\) (round) and \(0,0\) (flat, EH). \(\mathscr D=0.0781,\,0.0128,\,0.00204,\,0.000323\) at \(a=0.1,0.05,0.025,0.0125\); fitted exponent \(2.64\) against the predicted \(\rho^4=a^{8/3}\), with \(\mathscr D/\rho^4\approx36\)–\(38\).
- *Lemma 86.S′ (the 𝒟-ledger of scalar-flat bubbles) [P, Steps 86–87; same proof].* Let the bubbles \(N_j\) be scalar-flat ALE (at orbifold points) or AE (at smooth points), with decay \(\tau>0\) and finite \(P(N_j)\), glued by standard cutoffs at scales \(\to0\). Write \(Q=\sum_jP(N_j)\). Since \(s=0\) on \(N_j\) and \(\operatorname{Vol}\) of the scaled bubble region is \(O(\rho^4)\), the bubble contributes \(P(N_j)\) to \(R=\int|\mathrm{Ric}|^2\) and \(4P(N_j)\) to \(4P+L_s\), and nothing else in the limit. When \(R(g)+Q>0\),
  \[
  \mathscr D(g_\varepsilon)\ \longrightarrow\ \frac{4P(g)+L_s(g)+4Q}{R(g)+Q} .
  \]
  When \(R(g)+Q=0\) (all pieces Ricci-flat), the localized cutoff family has \(\mathscr D\to4\) by the support argument in 86.S above. A positive-energy bubble moves the value strictly toward \(4\) exactly when \(Q>0\) and \(\int s_g\ne0\). This needs only the leading order: the interaction terms of Theorem F (\(-x_0R^+_p(\zeta,\zeta)\)) vanish in the limit; finite-scale Burns saving (Theorem 69.KE giving strict \(4k/(A+k)\)) is higher-order information not deducible from this ledger. Check: over a KE orbifold with \(R=8\pi^2A\), \(k\) Burns bubbles (\(P=8\pi^2\) each) give \(4k/(A+k)\). So along any standard glued family, a zero value of \(\alpha\) can only come from a nonzero-scale Einstein bulk carrying exclusively Ricci-flat bubbles. This is a statement about glued families; it is not a lower-semicontinuity theorem for arbitrary sequences.
- *Corollary 52.9(i),(iii)–(v), corrected α-reading.* Einstein-orbifold resolutions by Ricci-flat ALE have \(P_*=0\); they have \(\alpha=0\) when the compact orbifold Einstein constant is nonzero (Lemma 86.S; the scalar-variance error is automatically small). Ricci-flat bulks are excluded from this α-conclusion. Exceptional classes need not lie in the orbifold bulk; the
  orbifold LeBrun estimate, under the stated orbifold SW supply, gives in every absorption pattern the numerical necessary condition \(k\le A/3\) (not existence or admissibility); absorbing Einstein orbifolds are non-Kähler, and on general-type blow-ups have \(\lambda<0\) (86.S).
- *Ledger conservation (52.10).* Conserved linearly for the signed pair \((C_+,C_-)\): \((2,2)+2(0,-6)=(2,-10)\), \((3,0)+(0,-15)=(3,-15)\), equal to the
  \(D\#2\overline{\mathbb{CP}}^2\), \(D\#3\overline{\mathbb{CP}}^2\) ledgers; absorption moves the positive charge from bubbles to orbifold cells.
- *Optimality of the convergence class.* Conformal logarithmic clouds give \((\mathrm{PS}_\varepsilon)\) minimizing sequences without pointwise curvature
  convergence; \(C^{1,\beta}\cap W^{2,q}\) cannot be improved under an own-scale \(L^2\) residual.
- *Parity lemma.* In a complex crepant resolution of \(SU(2)\) points no class of odd square lies in the rational root span (\(K\cdot E\equiv E^2\) mod 2).

**Conditional.**
- *Theorem 52.3 (P-version).* Under \((\mathrm{PS}_\varepsilon)\) \(\int r_\varepsilon^4|Q|^2\to0\) and a uniform local Sobolev bound (no derivative hypothesis), selected P-minimizing
  sequences converge to a \(P\)-critical orbifold bulk plus scalar-flat Bach-flat ALE bubbles, with lower semicontinuity
  \(P_*\ge P(g_\infty)+\sum P(N_b)\), attainment without concentration, and Einstein/Ricci-flat structure when \(P_*=0\) (then 52.9(ii): \(M\) is an
  Einstein-orbifold resolution). This does not itself transfer to arbitrary α-minimizers; see §20.5. Inputs still to pin: the integral-curvature harmonic-radius theorem used in Prop. 52.4.
- *Theorem 52.5 (corrected, §5.6 of the Step-52 note).* The \(P\)-flow in dimension four is Streets' \(L^2\)-curvature flow
  (\(\int|\mathrm{Rm}|^2=32\pi^2\chi+4P\)), so Weyl curvature is smoothed. Lemma 52.KS at a fixed threshold is false (plateau/threshold jumps);
  shifted-threshold comparability (KS′) follows from a localized energy identity without \(\nabla w\) and the transport estimate when dissipation is small.
  For minimizing sequences two frozen-weight steps suffice. The entire open content is **step 0**: reaching own-scale smooth data at \(P\)-cost \(o(1)\)
  from energy + Sobolev data, a logarithmic-drift borderline identical to Streets' open Remarks 1.12/1.14. Flow-free alternative: weighted Ekeland with the
  threshold-averaged radius.
- *Theorem 52.7b.* The \(A_3\) absorption of three classes holds for \(X\#Q_3\), \(Q_3\) homeomorphic to \(\#3\overline{\mathbb{CP}}^2\); diffeomorphism pending.

**Withdrawn.** Step-50 Lemma W, Theorems 50.A–C as stated, the bubble charge \(b_2-2b_1\), "scalar-flat bubbles never save", and the claim that a noncollapsed
zero gap forces every exceptional class into the orbifold bulk.

**Consequence for the open range \(0<k<A/3\).** A positive gap would exclude Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\) and also absorbing Einstein
orbifolds with \(\lambda\ne0\) (Lemma 86.S; for \(k=2\) equivalently \(\iota\)-invariant Einstein metrics on \(X\#X\), for \(k=2m\) on \(X\#X\#(m-1)(S^1\times S^3)\)), whose bulk Seiberg–Witten theory does not see the
exceptional lattice. By the negative-Yamabe exclusion (86.S), such orbifolds necessarily have \(\lambda<0\). Upper-bound side: the \(S^4/\mathbb Z_2\) channel for ball-quotient hosts has exact orbifold deficit \(d_{*,\rm orb}=4\pi^2(A/3-2m)\) (§22.6, item 6) and cannot cross \(h=1/3\); CH-collared \(S^4/\mathbb Z_2\) cells cannot improve the self-dual Weyl deficit, since the orbifold signature identity forces \(\Delta I_+=\Delta I_-\ge0\).


## 14. Step 53 — Anderson entrance, bubble exclusion, attainment transfer (details: `step53_anderson_entrance_bubble_exclusion_attainment.md`; verified by TTCS, `trace/ttcs/results/step53_ttcs01_verifier1_integration.md`, with the corrections of that note's §6 binding over the items below)

All items below are conditional on Anderson, Asian J. Math. 10 (2006), Thm 4.10 as stated, applied to his perturbation \(P+\varepsilon\int(1+|\mathrm{Ric}|^2)^p\). Recorded delicate points of the source: local minimality of the weak limits, no-neck equality (4.43), and removability at points with trivial group.

- **Verifier corrections (binding).** Lemma 53.0 counts cone branches at reducible vertices (truncated-piece proof); 53.B applies to one-attachment trees, and the flux is positive by positive mass (\(\operatorname{tr}\Phi^{++}=3\pi^2m_{\rm ADM}>0\)); in 53.C the KE kernel directions form \(S^1\), and item 4 needs the CH-cell theorem with its collar-radius scope; 53.F′ needs the half-flat cancellation and assumes the homogeneous \(r^{-2}\) expansion; 53.D is: attainment \(\iff\) existence of a trivial generalized configuration; 53.Y holds for any order \(\tau>0\) with derivative control.
- **Lemma 53.0.** In case (I), \(P_*(M)=P(V,g_0)+\sum_kP(N_k)\). The orbifold Euler terms telescope.
- **Theorem 53.F′.** For an ASD scalar-flat AE bubble with homogeneous \(r^{-2}\) tail and flux \(\Phi^{++}(N)\):
  \(P=P(g)+P(N)-8\lambda^2\langle\mathbf R^+_p,U\Phi^{++}U^T\rangle+O(\lambda^{12/5})\). Optimizing over \(U\) gives \(\sum_i\lambda_i(\mathbf R^+)\mu_i(\Phi)\).
- **Theorem 53.B.** A bubble tree at a smooth point can be moved to any point and frame. Therefore a minimizing configuration has \(\mathfrak r_N\le0\) everywhere on the bulk; for Burns-type bubbles this means \(\mathbf R^+_{g_0}\le0\).
- **Cor 53.C.** If such a bubble is present, then \(s_0\le0\) is constant. If \(s_0=0\), the bulk is ASD; if \(s_0<0\), then \(|W^+|^2\le s_0^2/24\). No bulk component contains an exact CH region (by the Chapter-5 analytic cell).
- **Theorem 53.D.** If there are no points with nontrivial group, each bulk component attains \(P_*(V_a)\), and \(P_*(M)=\sum_aP_*(V_a)+\sum P(N_k)\).
- **Lemma 53.Y / Theorem 53.E.** Compactifications of scalar-flat AE ends of any order \(\tau>0\) with derivative-controlled decay have \(Y>0\). If \(Y(M)<0\) and the configuration is of type (I) without nontrivial groups, some bulk component has \(Y<0\) and a smooth minimizer. Problem 3 is then reduced to three obstructions: collapse, orbifold absorption, and Einstein bulk.
- **Open borderline for Problem 2/3.** The strict inequality \(P_*(V\#\overline{\mathbb{CP}}^2)<P_*(V)+8\pi^2\) at minimizers with \(\mathbf R^+\le0\) and no CH region. The second-order kernel-direction expansion on \(P\)-critical backgrounds is now Theorem 59.R (§20.1). What remains is (i) the sign of the optimized coefficient when the Ricci-tracefree residual (\(|T|^2\le Q_{\rm Ric}(\mathrm{Ric}^\circ_p)\), Corollary 59.Rig) can offset the kernel anisotropy \((\mu_2-\mu_3)^2\); (ii) the isotropic Einstein kernel boundary \(\mathbf R^+=(0,s/8,s/8)\), where \(\Phi=0\) and the undetermined \(O(\varepsilon^2)\) term decides; (iii) uniformity under moving backgrounds and batch gluing.


---

## 15. Step 54 — k=1 ball-quotient attainment theorem (conditional; verified by s54_t6_tool1, corrections recorded in the last item and in §17)

Source: `step54_k1_ball_quotient_attainment_theorem.md`; checks `scripts/step54_charge_and_entropy_checks.py`.

- **Lemma 54.1 (proved).** Smooth AE bubble, \(e\) ends, \(\Gamma=1\):
  \(P(N)\ge8\pi^2\max\{c(N),c(\bar N),0\}\) with \(c=4(e-1)+4b_1+b^--5b^+\). Necks cost \(\ge32\pi^2\).
- **Lemma 54.3 (S³ necks) [P*].** If \(M=Z\#R\), \(b^+(M)\ge2\), and \(Z\) is PSC with \(b^+(Z)\ge1\), every SW invariant of \(M\) vanishes. For \(b^+(R)\ge1\) this is ordinary connected-sum vanishing; for \(b^+(R)=0\) the step54 note writes out the standard neck-stretching argument (PSC side has no irreducibles, reducibles avoided by a generic perturbation supported there), resting on standard cylindrical-end compactness. No literature statement of exactly this one-sided form was located (Step 85 search; Frøyshov 2005 gives long-neck compactness, not this statement). The spherical-space-form and orbifold-cap analogue is the separate hypothesis SW\(_L\) (one-sided) of §16; the two-sided \(L\)-space splitting theorem \cite{agolhyperbolic} is a different statement and does not discharge it. Since Step 87 it is not used in Theorem 54.A (Γ-vertex argument below).
- **Theorem 54.A (conditional).** \(X\) a ball quotient, not a fake projective plane; \(M=X\#\overline{\mathbb{CP}}^2\). Inputs:
  the unconditional bound \(P_*(M)<8\pi^2\) from the Ch.-5 analytic cell, and hypotheses
  \(\mathrm{H_{sm}},\mathrm{H_{lsc}},\mathrm{H_{dec}}\) (plus Anderson's Thm 4.10). Lemma 54.3 is **not** used (Step-87 proof order below). Conclusions:
  - every smooth bubble is a one-ended homotopy-sphere bubble;
  - the bulk is connected and homeomorphic to \(M\), and carries \(E\).
  
  Adding \(\mathrm{H_{eq}},\mathrm{H_{rem}}\): \(g_0\) attains \(P_*(V)\). There are no bubbles unless some bubble
  compactifies to an exotic \(S^4\). Moreover \(s_{g_0}<0\) is constant, and \(g_0\) is either Einstein or a smooth
  non-Bach-flat global minimizer.
- **General \(k\).** \(\sum[4(e-1)+4b_1+\beta]<k\): not all exceptional classes can escape into smooth bubbles.
- **Step-87 proof order for ball-quotient hosts (Γ-vertex argument) [P given the stated hypotheses; replaces every use of Lemma 54.3 and of SW transfer through a homotopy sphere].** In a trivial-group case-(I) configuration of \(M_k=X\#k\overline{\mathbb{CP}}^2\) (Lemma 54.2), \(\Gamma=\pi_1(X)\) is torsion-free, one-ended and freely indecomposable, so exactly one closed capped vertex \(Y\) (bulk or cap, all of its ends filled) carries \(\Gamma\); all others are simply connected and there are no graph loops. Let \(q:M_k\to Y\) be the degree-one connected-sum pinch and \(f_Y:Y\to X=B\Gamma\) a map inducing the identified \(\pi_1\)-isomorphism. The degree-one classifying map \(c:M_k\to X\) and \(f_Y\circ q\) induce the same homomorphism on \(\pi_1\), hence \(c\simeq f_Y\circ q\) and \((f_Y)_*[Y]=[X]\): \(Y\) is essential, \(f_Y\) has degree one, and \(f_Y^*:H^2(X;\mathbb Q)\hookrightarrow H^2(Y;\mathbb Q)\) preserves the intersection pairing, so \(b^+(Y)\ge b^+(X)\ge3\). (1) *\(Y\) is bulk.* If \(Y\) were a bubble vertex with \(e\) AE ends, filling all \(e\) ends and applying the all-end form of Lemma 53.Y under \(\mathrm{H_{dec}}\) (positive conformal factor \(\sim r^{-2}\) on every end, point sources at every added point) would give the closed cap a PSC metric; but \(Y\) is essential with the fundamental group of a closed negatively curved four-manifold, which forbids PSC by \cite{mantionegeographya}, Prop. 2. (2) *Bubbles have \(b^+=0\).* Every bubble complement contains \(Y\) and has \(b^+\ge3\); ordinary connected-sum SW vanishing then contradicts \(SW_{M_k}\ne0\) unless \(b^+(\widehat N_j)=0\). (3) The charge bound (1) of the step54 note gives \(\sum_j[4(e_j-1)+4b_1+b_2]<k\); at \(k=1\) every cap is a homotopy sphere and \(M\cong V\#\Sigma\). (4) *Negative scalar curvature of the attained bulk.* \(V\) is essential with \(\pi_1=\Gamma\), so it carries no PSC metric (\cite{mantionegeographya}). The \(P\)-critical \(g_0\) has constant \(s\); \(s>0\) is excluded; \(s=0\) would make \(g_0\) Ricci-flat by Bourguignon (\cite{kotschick2004monopole}, appendix), forcing \(\pi_1\) virtually abelian (\cite{barbara2020fundamental}, Thm 2.7), contradicting that \(\Gamma\) is a cocompact lattice in \(PU(2,1)\). Hence \(s_{g_0}<0\) without any Seiberg–Witten invariant of \(V\). Lemma 54.3 remains a standalone [P*] statement for hosts without this essentialness input (general \(b^+\ge2\) hosts, subcase \(b^+(R)=0\)); SW\(_L\) remains a separate hypothesis in the nontrivial-link analysis of §§16–17.
- **Gates.**
  - Collapse: a free-circle region is spin, so it cannot carry \(E\); finite isotropy and split classes remain open.
  - Orbifold absorption of \(E\): needs a class \(a\in H_2(X)\) with \(a^2=m^2-2\). The earlier inference "\(m\) odd" is withdrawn (the relation does not force parity); constraints on \(m\) come only from the case-specific lattice, primitive-embedding and interface information of §§16–17.
  - Bubble-scale criticality under Anderson's perturbation: \(\varepsilon\ell^{4-4p}\) is only bounded by the naive
    \(\varepsilon\)-regularity count.
- **Entropy.** BCG+Bishop gives only \(\operatorname{Vol}\ge(64/81)\operatorname{Vol}(X)\), weaker than LeBrun's
  \(\operatorname{Vol}\ge\operatorname{Vol}(X)\). It does not decide Einstein versus non-Bach-flat.
- **Koiso.** The TT gap \(2\) gives cover-uniform \(C^{2,\alpha}\) local Einstein rigidity near ball quotients (answer to A01 #825).
- **Prop. 54.4 (conditional on \(\mathrm{H_{eq}}\) and strong local \(L^2\) curvature convergence).** For Anderson's fixed
  \(p>1\), the rescaled coefficient \(\kappa=\varepsilon\ell^{4-4p}\) is automatically bounded on non-Ricci-flat bubbles. The
  conformal scaling identity \((2p-2)\kappa\int|\operatorname{Ric}|^{2p}\to0\) then forces \(\kappa\to0\) or Ricci-flatness.
  Hence every bubble is \(P\)-critical and scalar-flat.
- **Lemma 54.1′.** The semidefinite, \(b_1\) and neck exclusions need no bubble equation, only bulk criticality and
  Chern–Weil with boundary at bulk scale. In the current (Γ-vertex) proof \(\mathrm{H_{dec}}\) is used exactly once: to give the all-end compactification of a hypothetical Γ-carrying bubble cap a PSC metric (all-end Lemma 53.Y), which Mantione–Torres excludes; essentialness and ordinary connected-sum vanishing then do the rest. The old indefinite subcase \(b^+(R)=0\) does not arise for ball-quotient hosts.
- **Verified (s54_t6_tool1).** Theorem 54.A holds with the corrected proof order: SW eliminates \(b^+\) first, then
  \(P(N)\ge8\pi^2[4(e-1)+4b_1+b_2]\). The earlier "c,c̄≤0 ⇒ e=1,b₁=0" is false; \(S^2\times S^2\) two-ended bubbles have
  zero charge. Further verified points:
  - (U) holds for every ball quotient.
  - Degree-one/π₁: all bubble caps are simply connected for every \(k\), and bubble \(H_2\) lies in the span of the
    \(E_i\).
  - Bubble \(P\)-criticality follows by compact replacement once smooth bubble convergence holds.
  - Remark 4 corrected: Einstein metrics on \(M\) have \(\int|W^+|^2\le\int s^2/24-2\pi^2\).
  - The orbifold parity claim is withdrawn.
  - The hypothesis ledger is in step54 note §5(b).


---

## 16. Step 55: the k = 1 orbifold gate (charges with η, degree-one lattices) — status

Source: `workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md`. Data: `workspace/data/step55_orbifold_bubble_charges.json`,
`step55_Tchain_embeddings.json`, `step55_Tchain_discriminants.json`. Verified by TTCS (`trace/ttcs/results/step55_ttcs01_verifier1_integration.md`); the resulting repairs are binding and recorded in §17 ("Step-55 repairs").

**Proved (exact computations / elementary topology).**
- Two-orientation ALE charge with η: \(c_\pm=2/|\Gamma|-2\chi\mp3\tau\mp3\eta\), \(\eta(n,q)=-4s(q,n)\); conventions fixed by Burns/EH/\(A_n\).
  New exact value: LeBrun's scalar-flat Kähler \(\mathcal O(-n)\) has \(P=8\pi^2(n-2)^2/n\) (numerical integration agrees to \(10^{-14}\), \(n\le8\)).
- Ledger: \(T_+^{\rm orb}(V)=T_+(M)+c_+(N)\); total \(=8\pi^2[C_+(V)+w(N)-T_+(M)]\), \(w=\frac1{2\pi^2}\int_N|W^+|^2\).
- T-singularity Milnor fibres: charge \(0\) (complex orientation), \(-4(1-1/n^2)\) (reversed); Ricci-flat Kähler ALE realizes \(P=0\).
- Theorem 55.5 (zero-charge T-channel at \(k=1\)): \(\pi_1(Y)=\Gamma\), degree one, chain spheres in unimodular negative-definite
  \(K\) of rank \(r+1\), \(H_1\)-torsion forces primitivity; primitive embedding exists iff \(1-na\) is a unit square mod \(n^2\) iff
  \(n\) odd or \(8\mid n\). Hence \(\mathrm{EH}/\mathbb Z_2\) (\(n=2\)) cannot occur in the zero-charge orientation; first allowed: \(1/9(1,2)\).
- Prop 55.6: the zero-charge orbifold bulk cannot be complex (blow-up counting \(\sum(-D^2)\le3r+1<3r+2\)).
- Prop 55.3(a) (repaired scope, §17): every **simply connected** rank-one orbifold bubble region carrying \(E\) or \(2E\) through a cyclic end has \(c_+=1\) and is excluded by (U). The unrestricted cyclic-end exclusion is false: \(\bar B_{t,a}\natural(\overline{\mathbb{CP}}^2\setminus B^4)\) has charges \((-3+4/t^2,-5)\).

**Conditional (hypothesis SW\(_L\): SW vanishing for splittings along spherical space forms, one-sided PSC orbifold-cap version).**
- Lemma 55.1: all orbifold bubble regions have \(H_2\subset\mathbb ZE\); at most one has \(b_2=1\); Kronheimer hyperkähler bubbles
  impossible at \(k=1\).
- Theorem 55.7, repaired coarse form (§17; the Step-55 detailed table of charge-allowed \((m,\Gamma)\) is superseded as a classification and survives only as charge arithmetic): in a case-(I) configuration, under (SW\(_L\)) and its one-sided form, exactly one of (A) no cone point with nontrivial group (→ Theorem 54.A); (B) exactly one nontrivial-group attachment region with \(b_2=1\), image in \(\mathbb QE\), all others rational balls; (C) nontrivial-group points exist and all their regions are rational balls. In every case the additive budget \(\sum_j\max\{c_+(N_j),c_-(N_j),0\}<1\) holds and the exact threshold is \(C_+(V)+\sum_jw(N_j)<A\); \(C_+(V)+w\ge A\) is an exclusion target, not an established reduction. Non-complexity of the bulk is proved only for the complex-orientation zero-charge Wahl channel (Prop. 55.6 repaired).

**Open.** Unrestricted lower bound for \(P\) on non-Kähler orbifold degenerations; the smooth identification
\((\#3\overline{\mathbb{CP}}^2)_{C_{9,2}}\cong\overline{\mathbb{CP}}^2\); existence of scalar-flat Bach-flat ALE metrics on the (B) topologies;
collapse (§6: cyclic-image lemma proved; Seifert/torus-isotropy F-structure regions open; charge gives no positive bound).

**Correction to strategist #70 recorded:** the degree-one reduction needs SW\(_L\); \(\mathcal O(-4)\) is excluded (charge exactly 1);
the rational-ball channel is not \(\mathrm{EH}/\mathbb Z_2\) in zero-charge orientation; non-cyclic \(D_5,D_9,E_8\) ends survive charge.


---

## §17 (Step 56) — Orbifold-category attainment at k=1, zero-energy bound, and the Wahl-point interaction

Authoritative note: `workspace/notes/step56_orbifold_attainment_zero_energy_bound_Tpoint_interaction.md`.

**Step-55 repairs (proved).**
- Charges, ledger and conservation are correct; the Wahl-ball charges \((0,-4(1-1/n^2))\) hold for all \(n\).
- Theorem 55.5 (primitive chain; \(n\) odd or \(8\mid n\)) is correct.
- Prop. 55.3 holds only for simply connected regions. Counterexample: \(\bar B_{t,a}\natural\overline{\mathbb{CP}}^2_0\).
- Prop. 55.6 is reproved via Kähler + Siu ⇒ birational + counting.
- The collapse ledger is withdrawn; the threshold stays \(C_+(\Omega)<A\).
- Theorem 55.7 is reduced to a coarse trichotomy plus the additive budget \(\sum\max c_\pm<1\).
- \((\#3\overline{\mathbb{CP}}^2)_{[5,2]}\) is homeomorphic to \(\overline{\mathbb{CP}}^2\).
- (SW\(_L\)), two-sided form: \cite{agolhyperbolic} (\(L\)-space splitting).

**Proved.**
- Prop. 56.U: zero-energy upper bound \(P_*(M')\le P(V,g)\) (and, by Lemma 86.S, \(\alpha(M')\le\mathscr D(V,g)\)) for any smooth orbifold metric on an orbifold with Wahl
  points, where \(M'\) is the Milnor-fibre smoothing. The error is \(O(\lambda^2)\), via the Ricci-flat ALE metrics
  \cite{suvaina2011ale}.
- §3: at a Wahl point with \(n\ge3\), invariant curvature is 4-dimensional, \((s,w_+,w_-,b)\): type-D \(W^\pm\) with the
  Γ-fixed Kähler forms, and \(\mathrm{Ric}^\circ\propto\omega\circ\bar\omega\). The bubble's quadrupole is
  phase-independent, so scale is the only effective modulus.
- Lemma 56.L: the linear-in-tail interaction has no \(\log\) term for a \(P\)-critical bulk. Numerical controls with
  generic and invariant curvature and correct and wrong tails all give \(\int_{S^3}c=0\) to \(10^{-11}\) relative; the
  representation-theoretic reason is that a \((2,0)\) quadrupole has zero average.

**Conditional.** Theorem 56.A: under the case-(I) ledger, (SW\(_L\)), orbifold regularity and (N\(_0\)) (all
nontrivial-group bubbles Ricci-flat):
- \(P_*(M)=P_{*,\rm orb}(V)=P(V,g_0)\), attained by a \(P\)-critical metric with \(s_0<0\) on \(M\) or on an orbifold
  with Ricci-flat rational-ball points;
- \(g_0\) is Einstein or non-Bach-flat; an Einstein orbifold bulk with nonzero Einstein constant gives \(\alpha(M)=0\) after Ricci-flat ALE resolution or Wahl smoothing (Lemma 86.S: the smoothing errors in \(\int|\mathrm{Ric}|^2\), \(\int s\), \(\int s^2\), \(\operatorname{Vol}\) are \(O(\rho^4)\)). A Ricci-flat bulk gives \(P_*(M)=0\); its naive glued family has \(\mathscr D\to4\), and this construction alone does not determine \(\alpha(M)\). On negative-Yamabe \(M\) a Ricci-flat bulk is excluded (86.S negative-Yamabe exclusion), so here the Einstein bulk necessarily has \(\lambda<0\);
- at Wahl points the parity, lattice and non-complex conclusions hold.
Corollary 56.B, corrected α-reading: an Einstein orbifold with Wahl points whose smoothing is \(M\) gives \(P_*(M)=0\); it gives \(\alpha(M)=0\) when the orbifold Einstein constant is nonzero (Lemma 86.S), and nothing about \(\alpha\) when it is zero.

**Open.**
- The \(\lambda^4\) polarizability form \(\mathcal Q_\Gamma(\nabla\mathrm{Rm}_p,R_p)\) of \(B_{n,a}\).
- Case (B) with non-simply-connected regions or noncyclic ends.
- Positive-cost rational-ball bubbles.
- Collapse (topological: finite-isotropy \(F\)-structures carrying odd-square classes).
- The diffeomorphism \(Z\cong\overline{\mathbb{CP}}^2\).
- Construction of a CH-collared \(\mathcal O_{9,2}\) cell.


---

## §18 (Step 57) — Kernel-direction second-order Burns coefficient in a general background (formal; details `step57_kernel_burns_coefficient_general_background.md`)

- **Lemma 57.1.** The ε² log(1/ε) coefficient depends only on Rm_p. ∇Rm drops out by parity. ∇²Rm drops out because the
  Burns family δ+εA is P-critical for all ε, so the term is a divergence; numerically ℓ ≡ 0 to 5·10⁻¹⁵.
- **Theorem 57.Φ (formal, computed and cross-checked).** Let ζ be an R⁺_p-eigenvector with eigenvalue μ1, other
  eigenvalues μ2, μ3. Then
  P̃/8π² = P/8π² + 1 − εμ1 + (Φ/2)ε²log(1/ε) + O(ε²), with Φ = −μ1(μ1−μ2−μ3)/2 − (μ2−μ3)²/2.
  In the kernel, Φ = −(μ2−μ3)²/2 ≤ 0, independent of W⁻, Ric°, ∇Rm and ∇²Rm. CH gives −18, reproduced by general degree-0
  corrections, so the Ch. 5 minimiser is optimal.
- **Consequences (formal at Step 57; now proved where stated in §20).**
  - Every KE surface saves at every point: Φ = −s²/32. Hence P_*(X#kCP̄²) < 8π²k for all minimal general-type X — now
    Corollary 59.KE [P].
  - Minimizing bulks with Burns bubbles (conditional on 53.B) have R⁺ ≤ 0. On a general P-critical bulk the kernel
    restriction is |T|² ≤ Q_Ric(Ric°_p); only an Einstein bulk forces λ_max = 0 ⇒ μ2 = μ3 (Corollary 59.Rig, §20.3).
- **Status of the Step-57 open item.** The rigorous remainder on P-critical backgrounds is Theorem 59.R [P] (§20.1); no
  unrestricted remainder on non-P-critical backgrounds is asserted. Batch gluing for balanced families remains open.

## §19 (Step 58) — Cross-checks, product-background tests, consolidation, A01 coordination

- **D = 6 fit:** identical to D = 4 (s² 1/288, sw −1/24, w² −1, W⁺_⊥⊥ −1, W⁻ 0 (7e−17), Ric° 0 (10⁻¹⁵)).
- **Density code check (F₊ = 4|W⁺|² + s²/12).** D = 2 and D = 4 with `STEP57_DENSITY=fplus`: raw M agrees to 5.6e−16,
  M_eff to 8e−15, Φ_CH = −18 both ways. Invariant fit at D = 4 also gives the 57.Φ coefficients.
- **Eight product backgrounds** Σ₁(K₁)×Σ₂(K₂) in conformal coordinates (Ric° ≠ 0, W⁻ ≠ 0), both layouts.
  All D = 6 values match the predicted Φ = −s²/32 to ≤ 3e−15. D = 4 had systematic positive error up to 0.49 on
  (−1,−3) par, showing that convergence in corrector space depends on the background-jet gauge (conformal needs D=6).
- **A01 #830 confirms F_KE = −18** via the CGB reduction 4|W⁺|² + s²/12, an explicit W⁻ corrector
  k₀^W = (3/2)sym(h_W kB) − (1/4)tr(h_W kB)δ (exact sympy), and degree-6 check.
- **Consolidation:** `step58_consolidated_hypothesis_ledger.md` replaces all layered §0 corrections with a single
  hypothesis reference. Message #831 sent A01 with the formula, 8-test table, division of labour, and specific
  questions.
- **Open at Step 58, since resolved in part:** the rigorous remainder on \(P\)-critical insertion regions is Theorem 59.R [P] (§20.1). Still open: an unrestricted remainder on non-\(P\)-critical backgrounds, and the balanced-family matching law with per-cell saving λ²ε²log/4 at Ric = λg (batch gluing).
- Files: `step57_kernel_burns_coefficient_general_background.md` (updated §6); `step58_consolidated_hypothesis_ledger.md`;
  `step58_msg_to_A01.txt`; `workspace/data/step58_products/` (8 JSON); `workspace/data/step57_general_form_D{2,4,6}_q8_24_fplus.json`.
- **Step-58 verifier (`trace/ttcs/results/step58_ttcs01_verifier1_integration.md`)**: normalization (Φ/2)ε²log confirmed;
  - **Step-58 verifier, updated at Step 64** (`trace/ttcs/results/step58_ttcs01_verifier1_integration.md`; A01 message #834): normalization \((\Phi/2)\varepsilon^2\log\) confirmed. The chiral-square coefficient is \(|\mathcal A_B+D\mathcal C[K]|^2\ge0\). A01's explicit \(k_0^W\) attains zero in the \(W^-\) sector. The Ric° sector is also exactly zero: `S1003A01/workspace/notes/step53_ric0_geometric_corrector.md` writes the pure Ric° jet as \(h_E=2f\delta+\mathcal L_V\delta\) and constructs the Burns-harmonic continuation \(f_\varepsilon=f-\varepsilon q_H/(8u)\), giving a degree-zero \(k_0^E\) which cancels both \(W^+{}''(h_E,k_B)\) and \(s''(h_E,k_B)\). Hence Theorem 57.Φ is all-sector at logarithmic order. Lemma 57.1 wording remains: degree −3 field, constant flux; non-critical backgrounds have a separate singular-tail pairing with \(E_P(p)\). The rigorous P-critical remainder is Theorem 59.R, not A01's Einstein-only Lemma 52.C.
- **Exhaustive (s, W⁺)-sector minimization** (`step58_invariant_exhaustive.py/json`): SU(2)₋ averaging reduces all
  degree-0 correctors to the 10-dim invariant space; coefficients 1/288, −1/24, −1, −1, CH −18 exactly. So 57.Φ is
  not a truncation artefact in that sector.
- **Prop 58.O (proved P-statement, with Ozuch Thm 0.9 \cite{ozuch2021integrability}; α-reading corrected in Steps 71–72):** Ricci-flat-ALE resolutions M′ of compact
  Einstein orbifolds with isolated points have \(P_*(M')=0\). They have \(\alpha(M')=0\) when the orbifold Einstein constant is nonzero (Lemma 86.S; the cutoff errors are automatically \(O(\rho^4)\)); Ricci-flat bulks give no such implication. With an \(\mathbb R^4/\mathbb Z_2\) point, no Einstein metrics on M′
  GH-converge to the orbifold. Example: \(\alpha(\mathbb{CP}^2\#\mathbb{CP}^2)=0\) via \(S^4/\mathbb Z_2\); attainment ⇔ Einstein existence (open), and the degeneration is not an Einstein limit. **Target 58.Q** (superseded on weighted gluing neighbourhoods by Theorem 61.EH, §20.6): \(P=\lambda^4\mathcal Q_{EH}(R_p)+o(\lambda^4)\) at Einstein orbifold points, expected kernel = Biquard
  obstruction locus; would give a quantitative Ozuch theorem P ≥ cλ⁴ along such degenerations. Details:
  `step58_consolidated_hypothesis_ledger.md` §IV′ (ledger rewritten in post-Step-70 notation at Step 90).

## §20 (Steps 59–61) — Exposable proof spine for the local laws and the zero-gap structure

Status tags: [P] proved, after verification by TTCS s60_t24_tool1 with the corrections applied; [P*] proved modulo a quoted
external theorem; [C] conditional on the named ledger; [O] open. Details: `step59_rigorous_burns_expansion_and_zero_gap_structure.md`
(Part D is binding over A–C) and `step61_EH_quantitative_obstruction.md`.

**20.1 Theorem 59.R [P]** (second-order Burns expansion on P-critical backgrounds).
- Hypotheses: g is smooth, and E_P(g) = 0 on B_{2ρ}(p), which contains the whole insertion support. ζ ∈ Λ⁺_p is a unit vector, K is a smooth degree-0 corrector, and the cutoffs ψ_ε, χ_ρ are as in A.1.
- Conclusion: P(g̃_ε) = P(g) + 8π² − 8π²εR⁺_p(ζ,ζ) + 4π²Φ(Rm_p,ζ,K)ε²log(1/ε) + O(ε²).
- No eigenvector hypothesis is needed.
- Proof spine:
  - the exact identity P(g̃) = P(g) + 8π² + ∫(F₊(g̃) − F₊(g)), with F₊ = |𝒞|² and 𝒞 = (2W⁺, s/√12);
  - 𝒞(Burns) ≡ 0;
  - the rescaled family G_{σ,r} = B_σ + r²(q + σK) is smooth in (σ,r,y), and its σ-Taylor expansion gives the log term from σ², with r⁴ coefficient |C₂|²;
  - the order-ε term comes from local criticality plus the distributional potential ∂∂̄(χ log r²), with c_A = −4π²(M_ζ/6, 1/√12).
- Optimised value Φ_opt = −μ₁(μ₁ − s/8) − |T|². This requires Ric°_p = 0 and ζ an eigenvector. It is attained by K* + k₀^W, with K* as in D.2, mixed coefficient 2w₂₃/3. The W⁻ sector is handled by Schur cancellation on the whole σ² coefficient plus A01's exact k₀^W.

**20.2 Corollary 59.KE [P].** For every compact KE surface with s ≠ 0, and for every minimal surface of general type (canonical model, Kronheimer gluing, ε fixed before λ):
P_*(X#kCP̄²) ≤ 8π²k(1 − (s²/64)ε²log(1/ε) + Cε²) < 8π²k.
This is an upper bound only. Together with K∞ [P, §13], the unrestricted P-infimum lies strictly below the Kähler infimum. α-reading (§1, item 2): α(X#kCP̄²) < 4k/(A+k) (Step 69, §22).

**20.3 Corollary 59.Rig [C]** (Anderson ledger, 53.B).
- At a minimising bulk carrying Burns bubbles: R⁺ ≤ 0, and on the kernel, |T|² ≤ Q_Ric(Ric°_p).
- If the bulk is Einstein: μ₂ = μ₃ at λ_max = 0, so |W⁺|² < s²/24 for s < 0.
- A01's Lemma 52.C needs an Einstein bulk; 53.B gives only a P-critical one.

**20.4 Zero-gap mechanisms [P].**
- **Step-71 functional correction (binding).** In Steps 59–61, "α" in 59.N/59.C/59.Z meant the trace-free infimum P_*. The α-readings below follow `step71_functional_split_and_unit_wall.md` §4.
- 59.N: compatible finite Ricci-flat ALE-tree resolutions of compact Einstein orbifolds with isolated irreducible cone points have **P_* = 0**, with P = O(λ²) for derivative-controlled ALE order ≥ 2 (λ the gluing scale). They have **α = 0 when the orbifold Einstein constant is nonzero** (Lemma 86.S), because R → 4Λ²V_orb > 0. For Ricci-flat orbifolds the construction gives P_* = 0 and its naive glued family has 𝒟 → 4, with no general conclusion about α; for the Kummer resolution T⁴/±1 → K3 specifically, 2χ = 3|τ| gives α(K3) = 1 by the unit-wall theorem.
- 59.C: **P_*** ≤ 36 Vol_{|r|} ≤ 36 MinVol (spectral normalisation). MinVol = 0 ⇒ χ = τ = 0 ⇒ T_± = 0; together with the Step-72 universal ceiling this gives **α = 1**. Thus S¹×Y, S²×T² and Kodaira surfaces have P_* = 0 but α = 1. On S¹×S³/Γ and S¹×H³/Γ, the value 1 is attained (Theorem 71.C); attainment on the other examples is separate. The earlier sentence "α = 0 on these manifolds" is withdrawn.
- 59.D:
  - real-hyperbolic doubles: P_neck = 3Vol∫(f'')²e^{−3f} = O(e^{−3T});
  - complex-hyperbolic Heisenberg doubles: O(e^{−4T});
  - every primitive T³-slope filling: O(e^{−2T}).
  - Long slopes are attained by Anderson's Einstein fillings \cite{anderson2003dehn}. Attainment on short slopes and on doubles is undecided; no openness claim is made without a source.

**20.5 Theorem 59.Z [P*] — a P-statement** (Anderson Thm 4.10 for ℛ² = 32π²χ + 4P plus removability). If P_*(M) = 0, some selected P-minimising sequence realises one of three configurations:
- a compact Einstein orbifold;
- a componentwise complete Einstein domain, with s < 0 on noncompact components and F-collapse outside;
- total collapse.
P-attainment ⇔ M admits an Einstein metric of some sign. The configurations are not mutually exclusive across sequences.

**α-version (Steps 71–72).** α(M) = 0 forces T_± > 0, hence χ > 0. After normalising \(\lambda_{\rm opt}=\pm1\), Gauss–Bonnet gives \(V\le12\pi^2\chi(1+o(1))\). A globally bounded-curvature, bubble-free total collapse of that same \(\mathcal E\)-small sequence is impossible. This does not exclude collapse with shrinking curvature-concentration balls, and Anderson's P-selected sequence need not preserve the normalized nonzero scale of an \(\mathcal E\)-small sequence. Thus no complete α-trichotomy has been transferred. If compactness applies to the same normalized sequence, its smooth noncollapsed limits are Einstein with constant \(\pm1\). α-attainment ⇔ an Einstein metric with \(\lambda\ne0\).

**20.6 Theorem 61.EH [P for the lower bound; P* for the matching upper bound via Ozuch Lemma 2.3 \cite{ozuch2020higher}].**
- Setting: EH_a glued in direction ζ at an ℝ⁴/ℤ₂ point of an orbifold that is Einstein near p.
- Exact data: B_i = π²(R⁺_pζ)_i and ‖o‖² = π²/a⁴.
- Lower bound: on the weighted neighbourhood 𝒩_δ(a,ζ), P ≥ π²a⁴(|R⁺ζ| − C(δ + a^{2−w}))².
- Matching upper bound: Ozuch's Einstein-modulo-obstruction metric gives P = π²a⁴|R⁺ζ|² + O(a⁶).
- Near-minimisers have Ric° ≈ a²Σ(R⁺ζ)_i o_i/π² (Cauchy–Schwarz equality).
- Consequences:
  - CP²#CP² (S⁴/±1 with two EH) has \(P=2\pi^2a^4(1+o(1))\) on these neighbourhoods: a local P-rate. The value \(\alpha(\mathbb{CP}^2\#\mathbb{CP}^2)=0\) does not need this rate; it follows from Lemma 86.S applied to the round Einstein orbifold \(S^4/\pm1\) (\(\Lambda=3\)). The sharp α coefficient also depends on \(L_s\) as stated below;
  - KE orbifolds in the holomorphic direction cost π²Λ²a⁴ per A₁ point; in ω^⊥ directions the cost is o(a⁴), and they also pass Ozuch's second obstruction;
  - Burns/EH duality on the kernel stratum: the maximal Burns saving occurs at Ozuch's locus diag(0,0,Λ), and zero Burns saving occurs at the isotropic AdS-Taub–bolt type (0, Λ/2, Λ/2).
- [O]: the second-order kernel rate, the A_n and Wahl extensions, and the passage from neighbourhoods to arbitrary sequences.
- **α-reading (Step 71).** These are P-rates. For an orbifold with Ric = Λg, Λ ≠ 0, the α-rate is ℰ ≤ (4P + L_s)/R with R → 4Λ²V. On CP²#CP² (S⁴/±1, Λ = 3) this is (8π²a⁴ + L_s)/(48π²)(1+o(1)), i.e. a⁴/6 if L_s = o(a⁴); L_s on Ozuch's metrics is not yet computed. For Λ = 0 there is no α-rate.
- **Step-61 verifier corrections (binding; note §5).**
  - The centre is the jet-extended superposition, compared with the exact background.
  - The lower bound improves to π²a⁴(q − ε_w(a,δ))₊², with ε_w → 0 for bounded δ.
  - The adapted upper metric lies in 𝒩_{C₀} only, so the infimum statement is additive: π²a⁴(q − ε)₊² ≤ inf ≤ π²a⁴q² + O(a⁶). The orbifold must be globally Einstein, otherwise add P(g_V).
  - B_EH ĥ₂ = 0 is proved by a Bianchi argument.
  - If R⁺ζ = 0, then P = O(a⁸ log).
  - Ozuch §2.1.4 already gives the second obstruction ∝ det(R⁺|_{ζ⊥}).
  - **Exact unification:** Φ_opt(kernel) = −Λ²/2 + 2det(R⁺|_{ζ⊥}). The second-order Burns saving and the second EH obstruction are the same invariant.
  - KE ω^⊥ directions are not "non-Kähler" (the bolt is Lagrangian); the "exactly unobstructed" phrasing is withdrawn.

**20.7 Open centre [O].**
- The open-range positivity problem for 0 < k < A/3. The inequality C₊ ≥ A is **not** a target: it is false for unrestricted metrics (Corollary 59.KE gives P_* < 8π²k, i.e. inf C₊ < A). The correct target is uniform positivity of p = C₊ − (A − k) = P/8π² over all metrics, equivalently separation of the realizable joint set of (κ,υ) from the Einstein locus 4κ/3 − υ/3 = k (§22.6(4)), which must hold through the aligned and cscK coercivity-degenerate structures and accommodate certified sub-8π² cells.
- The k²/A law.
- The collapse and (N0) gates of 56.A.
- The boundary coefficient at R⁺ = (0, s/8, s/8).
- The **lower** matching on balanced families. The balanced upper law is proved (§5.3, §22).
- O10 actual-field theory.


## §21 (Steps 62–64) — The Weyl channel, exceptional flux, and differential transport (status: mixed proved identities and open realization)

Sources: `step62_weyl_channel_reduction.md` and `step63_frame_twist_flux_and_AK_identity.md`.

- **21.1 Identity 62.1 (proved, Chern–Weil).** At the Yamabe representative,
  p = (k − κ) + (υ − κ)/3,
  where κ = A/2 − (3/8π²)∫|W⁺|² and υ = Y²/32π² − A.
- **21.2 Theorem 62.A (proved).** It follows from LeBrun Prop. 4 together with Cauchy–Schwarz:
  p ≥ (k − κ) + ½(A − κ − √(A² − 2Aκ)) for κ ≤ 4A/9.
  The Kähler tariff is the case κ ≤ 0. The formal common mode lies on the equality locus through O(k³/A²).
- **21.3 Corollaries 62.B–C (conditional; corrected notation, Step 71).**
  - If κ ≤ k for every metric (equivalently inf∫|W⁺|² ≥ (4π²/3)(A−2k)), then P_* ≥ 8π²p_♭ with p_♭ = (A − k − √(A²−2Ak))/2 = (k²/4A)(1+O(k/A)). This is a statement about the dimensional P-infimum.
  - α-translation: at a Yamabe metric υ = 3p − 3k + 4κ ≤ 3p + k. Since 4p/(4p + A + k) increases in p, the exact quotient gives α ≥ min{1, 4p_♭/(4p_♭ + A + k)} = h²(1+O(h)), with h = k/A. **Corollary 62.D is withdrawn:** p/k → 0 does not force κ/k → 1 or Π = o(k), because k−κ can be negative and cancel the Yamabe term.
- **21.4 Theorem 63.T, frame-twist bound (proved: Hodge theory plus the Gauss formula γ_J = R(Ω) + α∧β).** This holds for any metric and any orthogonal J:
  √(P/2) ≥ 2π|c₁(J)⁻| − 𝒯_J, where 𝒯_J = ‖(α∧β)⁻‖.
  On X#kCP̄², the best sign class has |c₁⁻|² ≥ k + Π. No SW input is needed.
  Consequences:
  - The Kähler tariff is the case 𝒯 = 0.
  - Every family with p ≤ ck has 𝒯_J ≥ 2π√k(1 − √c) for **every** J.
- **21.5 Proposition 63.AK (proved from AAD's formulas).** For every almost-Kähler metric,
  P = 2‖γ_J⁻‖² + ∫u(5u + s) + 2∫|ρ_*''|² + 4∫|W₃⁺|², with u = |∇Ω|²/4.
  Remarks:
  - It recovers Sekigawa's theorem.
  - For AK Einstein metrics: ∫u(|s| − 6u) = 2∫|ρ_*''|² + 4∫|W₃|², and ½∫u² ≥ 4π²|c₁⁻|².
  - Pointwise optimization of this identity alone reproduces LeBrun's k − A/3.
- **21.6 Emptiness of the 62.A equality locus for k ≥ 1, k ≠ c₂(X) + 2A (proved for that range; at k = c₂(X) + 2A only argument (b) applies; citations still owed).** Two independent arguments:
  - (a) Equality forces u to be constant. If u > 0 then N ≠ 0 everywhere, which forces 5χ + 6τ = 0 (Armstrong; LeBrun; AAD Lemma 2). On M, however, 5χ + 6τ = c₂(X) + 2A − k > 0. If u = 0, then J is Kähler and κ ≤ 0.
  - (b) Π = 0 is incompatible with E_i·[Ω] > 0 (Taubes / Li–Liu).
  AAD's Theorem 2 needs the third Gray condition, which includes Ric'' = 0. That theorem is not needed here.
- **21.7 Integral-system models (formal only).** Constant torsion gives \(p\ge(A-k)(2-3u)^2/[u(4-3u)]\), so the old common mode with \(u=k/A\) cannot carry the exceptional flux. A two-phase density with \(W^+=0\) patches has \((\kappa,\upsilon,p)=(2k,5k,0)\) only for \(k\le A/4\); AAD excludes it as a smooth AK-Einstein transition, \(\overline{FPP}\) has no compatible ACS, and full Einstein pieces plus ordinary joins give \(p=4k\). These densities neither prove a tariff nor construct a cheap sequence.
- **21.8 Literature status.** Itoh–Sambusetti-type paper `The-Weyl-functional-near-the-Yamabe-invariant`, Theorem C and line 157: whether KE minimises ∫|W|² on a minimal general-type surface is stated as **not known** in general. For ball quotients it holds by the signature identity. So 62.W at k = 0 is itself open beyond ball quotients and products.
- **Open (next).**
  - (Q1) A domain-wall cost estimate for the frame twist.
  - (Q2) Compute \(P_*(X\#k\overline{FPP})\) versus 8π²k (a P-question; written α before the Step-70 split).
  - (Q3) An effective 63.T for non-AK near-minimisers: J from the SW spinor, with the twist controlled in L⁴ by the SW slack.
- **Verification (Step-63 TTCS, binding; details in step63 note §6).**
  - 63.T and 63.AK are confirmed in full. The 62.A equality locus is empty for k ≠ c₂(X) + 2A, k ≥ 1.
  - 62.A is valid for 0 ≤ κ ≤ A/2; for κ < 0 use p ≥ k − 4κ/3.
  - **Corollary 62.D is withdrawn.** p/k → 0 does not force κ/k → 1, because k − κ < 0 can cancel the other term.
  - Formal-mode torsion is u = k/A, so the AK twist bound gives p ≥ k(1 − ½√(k/A))².
  - 21.7 is downgraded to a formal density model. It requires k ≤ A/4; AAD (37) excludes it as a smooth AK-Einstein metric; \overline{FPP} has no ACS; full pieces give p = 4k.
  - Arbitrary-J twist coercivity is false (Σ×Σ' counterexample).
  - New rigorous wall estimate. Let U ≅ (#_m CP̄²)∖B have localized Chern–Weil boundary term 𝔟 and replace a reference ball B with boundary data matched to within δ. Then P_g(U) ≥ 8π²m − Q_h(B) − 2δ, which for a KE reference is 8π²m − 4Vol_h(B) − 2δ. It holds for fat interiors.
  - Open target: transgression coercivity (8π² − 𝔟)₊ ≤ qP(U ∪ collar) + ε, which would give the tariff 1/(1 + 2q).


### 21.9 Step-64 correction: diffuse harmonic twist and AAD transport — Proved identities; lower bound/construction open

Canonical path: `workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md`; verification: `trace/ttcs/results/step64_ttcs01_verifier1_integration.md` and `step64_ttcs02_verifier1_integration.md`.

- **Exact harmonic twist.** For every smooth orthogonal \(J\) with best-sign class \(a\),
  \[
  \mathsf H^-(t_J^-)=2\pi h_a^- -\mathsf H^-(\rho_0^J),\qquad
  \|\mathsf H^-(t_J^-)-2\pi h_a^-\|_2\le\sqrt{P/2}.
  \]
  Thus only the harmonic projection is pinned. A nearly harmonic full twist is an extra efficiency hypothesis. In the AK case,
  \[
  \frac12\int u^2\ge(2\pi\sqrt{k+\Pi}-\sqrt{P/2})_+^2,
  \quad u=|\nabla\Omega|^2/4.
  \]
  At volume \(2\pi^2A(1+o(1))\), the diffuse RMS scale is \(u_{\rm rms}\ge2\sqrt{(k+\Pi)/A}\). This invalidates the old constant mode \(u=k/A\) but does not imply a tariff.

- **AAD amplitude transport.** On a closed AK four-manifold,
  \[
  \|d^Ju\|_{\dot{\mathcal H}^{-1}_u}
  \le C(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P),
  \]
  with all curvature derivatives removed by integration by parts and AAD (26). This controls only nonconstant torsion amplitude and is noncoercive at the diffuse scale, where the exact AK identity forces \(W_2/W_3\) financing energy of order \(\sqrt{kA}\).

- **AAD harmonic-orientation test.** For constant scalar \(s\), harmonic ASD \(h\), and \(\eta_h(Z)=\nabla_{h(Z)}\Omega\),
  \[
  \sum_i\langle\nabla_{Je_i}\Omega,\nabla_{h(e_i)}\Omega\rangle=-4\langle t^-,h\rangle,
  \]
  \[
  s\langle\mathsf H^-(t^-),h\rangle=\mathcal F_h-6\int u\langle t^-,h\rangle.
  \]
  The derivative-free estimate \(|\mathcal F_h|\le C(\|W_3\|+\|\rho_*''\|+\sqrt P)B_h\) is proved using
  \[
  \|\nabla^2\Omega\|_2+\|\nabla\Omega\|_4^2\le C\|\mathrm{Rm}\|_2.
  \]
  Full-norm Cauchy–Schwarz still reproduces the negative Goldberg balance; progress needs cancellation or spectral separation in the specific \(h\)-tested components.

- **Spinor zeros and the finite curvature ledger.** A transverse zero has Hopf Bloch field with logarithmically divergent unweighted \(L^4\) rotation and \(L^2\) twist; exact coefficients for the conformal linear model are \(128\pi^2\) and \(16\pi^2\). Theorem N's amplitude-weighted rotation tends to zero there. The smooth regularization
  \[
  \gamma_\delta^-=w_\delta(R(\Omega)^-+t^-)+(1-w_\delta)F_A^- -2(dw_\delta\wedge\beta)^-
  \]
  retains the best-class ASD flux without normalizing through zeros. The open SW estimate is joint control of the low-amplitude ASD determinant-curvature reservoir and the amplitude-transition term. The self-dual SW equation does not control \(F_A^-\).

- **Route judgment.** Neither a positive per-class tariff nor the \(k^2/A\) law is currently supported. A cheap state must realize a diffuse nearly harmonic quadratic frame twist in the best sign class, large \(W_2/W_3\) financing energy, unit-scale torsion oscillation, zero/core data, and small Ricci defect simultaneously. The lower-bound alternative is an estimate on the specific harmonic-flux-tested AAD functional or the regularized SW reservoir. No closed construction or such estimate is yet proved.


- **21.10 (Step 65) Exceptional Ricci flux and the cell ledger.** Note `step65_cell_exceptional_flux_ledger.md`; script `scripts/step65_cell_twist_flux.py`; data `data/step65_cell_twist_flux.json`, `data/step65_family/`.
  - [P] Metric-only form of 63.T/64. Here B_g is the Ric° block Λ⁺→Λ⁻, and ρ₀ᴶ = B_gΩ for every J. Then ⟨t_J⁻,h⟩ = 2π⟨a,h⟩ − ∫⟨Ω,B_g^*h⟩.
    - Put 𝔉_h(g) = √2∫|B_g^*h|. Every class-a J carries harmonic twist flux ≥ 2π⟨a,h⟩ − 𝔉_h.
    - **Normalization (corrected by the Step-66 verifier; binding).** Use unit \(\widehat h\) and \(q=(h_a^-,\widehat h)\). Then \(P/2\ge\mathfrak F_{\widehat h}^2\), and the exact ledger is \(p=q^2(1-\delta)^2+L\), with \(\delta=1-\mathfrak F_{\widehat h}/(2\pi q)\) and \(L\ge0\) (Ricci misalignment and amplitude error). The earlier form \((1-\delta)^2/\|h\|^2\) is superseded.
  - [Numerical, floating] End-to-end check on A01's perpendicular cells, using exact diagonal Bianchi-IX formulas.
    - Twist sign fixed by dγ_J = 0 (residual 7e-16). Identity holds to 5e-7 for five J-profiles.
    - Certified cell, **metric values** (Step-66 correction): δ_m ≈ 0.00541, Hodge term q²(1−δ_m)² ≈ 0.99023, L_m ≈ 0.00543, p = 0.995663. The earlier printed values δ = 0.00549 / L = 0.00558 were the signed J₁-deficit, not the metric deficit, and are withdrawn from theorem status.
    - The twist flux of the natural smooth structure J₁ is 2πδ exactly; it is pure w₁⁻ and equals the product of two non-Kähler defects, v₂v₃.
    - Its harmonic efficiency is only 3–10%.
    - It is located log-uniformly in the matching annulus, with median x ≈ 0.8√x0, i.e. the annulus that produces the 59.R logarithm.
  - Across x0 = .003–.03:
    - δ is second order (δ/x0² = 20 → 6);
    - L/δ ≈ 0.82–1.02;
    - saving ≈ (1.1–0.8)·δ.
    - Burns-type cells therefore supply only δ ≲ 10⁻² per class.
  - Consequence (reading, not theorem).
    - p ≤ ck needs an O(1) exceptional-Ricci-flux deficit per class. A p ≪ k state cannot be a dilute gas of Burns cells.
    - The rotation Burns→ω_CH through Ricci-flat regions is flux-neutral (pure w₃⁻ twist).
    - The invariant null-period J₃ is singular along E, the codimension-2 analogue of the SW Hopf zero.
  - Weyl/Yamabe signature of the AK template: κ ≲ 3√(kA) − 4.5k and υ ≈ 4κ − 3k at p ≈ 0. Neither excludes p ≪ k.
  - Records x0 = .05 and .10 do not reconstruct (P ≈ 32) and are excluded.


- **21.11 (Steps 66–68) Equality and near-equality structure of the exceptional-flux ledger.** Notes: `step66_rank_one_exceptional_ricci_rigidity.md`, corrected `step67_cK_local_coercivity_at_cscK.md`, and `step68_product_cscK_saddle_verification.md`. Scripts/data: `step66_rank1_bianchi_check.py`, `step67_cK_symbol_check.py`, and the Step-68 product records. The Step-68 TTCS integrations are binding for the product coefficient and the corrected 67.K statement.

  **Organization.** On the constant-scalar slice, use
  \[
  p=q^2(1-\delta)^2+L,
  \quad q=|a^-|_g,
  \quad \delta=1-\mathfrak F_{\widehat h}/(2\pi q),
  \quad L=(P/2-\mathfrak F_{\widehat h}^2)/(4\pi^2)\ge0.
  \]
  The open range has three geometrically distinct ends.
  1. **Einstein end:** \(\delta=1,L=p=0\). A global estimate \(L\ge c\delta\), like any positive lower bound for \(\alpha\), contains Einstein nonexistence below LeBrun's current range rather than bypassing it.
  2. **Aligned end:** \(L=0\), \(0<\delta<1\). The rank-one theorem 66.R gives a strictly almost-Kähler structure with \(J\)-invariant Ricci and \([\rho_0]\parallel a^-\), under the stated bounded-extension hypothesis at the harmonic-form zero set. This is a restricted Blair--Ianus/Einstein--Maxwell class. An aligned cscK-null deformation is first-order Kähler only when its explicit obstruction \(\Xi\) vanishes; blanket infinitesimal isolation is not proved.
  3. **Kähler end:** \(\delta=L=0\), \(p=q^2\). Lemma 67.1 gives unconditional stationarity of \(p-q^2\). Zero-free \(\widehat h\) gives ellipticity and a finite nullspace; positive \(c_K\) is conditional on \(\Xi|_K=0\). Universal second-order minimality \(c_K\ge2\) is false by the product saddles below.

  **Rank-one and almost-Kähler results.**
  - [P] **66.Y.** For a negative conformal class, the Yamabe representative lowers \(P\):
    \[
    P(g)-P(\widehat g)=\frac1{12}\left(\int s_g^2-Y[g]^2\right)\ge0.
    \]
    Application to every conformal class retains the stated Seiberg--Witten/Yamabe negativity input; no positivity conclusion is inferred when this input is absent.
  - [P] **66.D.** For SD \(\phi\) and closed ASD \(\psi\), \(\operatorname{div}(\phi\circ\psi)=\psi(\delta\phi)\), with coefficient one.
  - [P] **66.R.** Under constant scalar curvature, rank alignment with nonzero coefficient and bounded extension across \(Z(h)\) force the aligned SD form to be closed. Bär's theorem gives \(\mathcal H^3(Z(h))=0\) \cite{br1997nodal}. Hence the non-Einstein equality structure is almost-Kähler with \(J\)-invariant Ricci and harmonic \(\rho_0\parallel h\). The zero coefficient is the Einstein end.
  - [P/C] The exact splitting is
    \[
    L=(2\pi^2)^{-1}\left[\|B_\perp\|^2+\int(|B^*h|/|h|^2-c)^2|h|^2\right].
    \]
    Rank alignment gives an Einstein--Maxwell structure only when the aligned SD form is bounded at \(Z(h)\).
  - [P] On the aligned almost-Kähler class,
    \[
    4\Phi^2\delta(1-\delta)=\int u(-s-6u)-2\|\rho^{*\prime\prime}\|^2-4\|W_3\|^2.
    \]
    For \(s\ge0\) this recovers the Kähler-side restriction; at \(s<0\) it leaves the negative-Goldberg/Blair--Ianus branch open. The near-equality Bianchi estimate gives weighted weak closedness only, not coercivity.
  - [P] For every class-\(a\) orthogonal \(J\), \(2\pi q\delta\le(t_J^-,\widehat h)\). Equality requires a smooth Ricci-aligned structure with the same Chern class; zero-freeness alone does not guarantee this global condition.

  **Kähler-end theorem, corrected.**
  - [P] **67.1.** At every non-KE cscK metric, \(D\delta=DL=0\), hence
    \[
    D(P-8\pi^2|c_1^-|^2)=D(C_+-|c_1^+|^2)=0
    \]
    for all Riemannian variations. At KE metrics stationarity follows separately. No zero-set hypothesis is needed.
  - [P] **Moving-line null structure.** Under zero-free or transverse \(Z(\widehat h)\), an \(\ell_2\)-null constant-scalar deformation follows the moving harmonic ASD line and induces a first-order almost-Kähler aligned pair with first-order \(J\)-invariant Ricci.
  - [P, conditional] Define
    \[
    \mathcal P_\omega:H^{0,1}(T^{1,0})\to H^{0,2},\quad[\mu]\mapsto[\mu\lrcorner\omega],
    \qquad \Xi(k)=[\dot\Omega_k]^{0,2}\bmod\operatorname{im}\mathcal P_\omega.
    \]
    If \(\Xi(k)=0\), the null direction is first-order Kähler and lies in \(\operatorname{rad}d_2\). The corrected Blair--Ianus constants are \(\int s=4\pi c_1\cdot[\omega]-E/2\), \(DE=2\int\langle\operatorname{Ric}'',k\rangle\), and \(\operatorname{Hess}E=2\|(\nabla\omega)'\|_2^2\). Products of curves have \(\mathcal P_\omega=0\), so arbitrary class realization is false.
  - [P/C] If \(Z(\widehat h)=\varnothing\), the true augmented symbol is injective after gauge reduction, and \(K=\ker\ell_2\) is finite-dimensional with \(H^2\)-coercivity on \(K^\perp\). If additionally \(\Xi|_K=0\), then \(d_2\le C\ell_2\), \(c_K>0\), and
    \[
    L\ge cq_0^2\delta-C'\|k\|_{C^{2,\alpha}}^3
    \]
    on the linear constraint space. The functionals are nonlocal; no nonlinear isolation follows. The spectral operator is \(T-N\), with \(T\) compact and \(N\ge0\) bounded.
  - [P] The exact deficit is
    \[
    2\pi qd_2=\tau_{\rm ref,2}-\frac1{\sqrt2}\int |w_1|^2/|v_0|,
    \]
    where \(w_1\) is measured relative to the moving reference direction.

  **Product saddle theorem (Step 68).** Let \(K_1\ne K_2<0\), let \(Q\) be the real symmetric tensor underlying a holomorphic quadratic differential on \(\Sigma_1\), and \(\Delta_2f=\mu f\). For the fixed-symplectic compatible family \(g_t|_1=g_1(e^{tf g_1^{-1}Q}\cdot,\cdot)\),
  \[
  \boxed{8\pi^2(p-q^2)_2=\frac\mu4(\mu+K_1-K_2)\|fQ\|_2^2.}
  \]
  The Step-67 generator's factor \(2(K_1-K_2)\) was wrong; form norms give \(\int u_2=\mu\|fQ\|^2/8\). If \(K_1<K_2\), descent occurs exactly for \(0<\mu<K_2-K_1\), and
  \[
  c_K\le \frac{2\lambda_1(\Sigma_2)}{K_2-K_1}.
  \]
  Pinching gives product cscK metrics with \(c_K\to0\), so no uniform positive Kähler-end constant exists. The mode has \(\ell_2>0\), bypasses \(\Xi\), and remains a descent direction after the \(O(t^2)\) constant-scalar correction. This is a near-extremal-structure theorem, not a closed blow-up construction below \(k\).

  **Cell calibration.** At the certified cell, the corrected metric values are \(\delta_m\approx0.00541\), Hodge term \(\approx0.99023\), and \(L_m\approx0.00543\). This perturbative regime neither approaches the Einstein end nor supplies a diffuse product seed.


## §22 (Steps 69–72) — Upper laws for α and the human functional's own structure

Canonical notes: `step69_P_form_upper_law_balanced_towers.md` (§6 binding over §§1–5), `step71_functional_split_and_unit_wall.md` (read with its TTCS corrections), and `step72_orientation_free_weyl_deficit_law.md`. Data: `data/step69_balanced_upper_law.json`, `data/step71_functional_split_examples.json`, `data/step72_weyl_deficit_identity.json`, and `data/step72_dumbbell_numeric.json`.

### 22.1 Yamabe reduction and the upper comparison — [P]

- For a negative conformal class, LeBrun's Lemma 1 \cite{lebrun1996four} gives \(P(g)-P(\widehat g)=|\widehat s|\int|\nabla\varphi|^2+3\int(\Delta\varphi/\varphi)^2\ge0\).
- At the Yamabe metric, \(\mathcal E(\widehat g)=16P(\widehat g)/(4P(\widehat g)+Y^2)\).
- On LeBrun-supply manifolds (\(X\) minimal general type, \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\); \(Y^2\ge32\pi^2A\) for every class by LeBrun 2001, Prop. 3.2), this gives \(\alpha\le4p/(A+p)\) for every metric.
- Reverse comparison, with no monopole input: \(\alpha\ge\mathfrak p_*/(\mathfrak p_*+\frac34T_+)\).
- The exact quotient of §1 item 2 refines both.

### 22.2 Theorem 69.B — [P]

The balanced ball-quotient law \(\alpha/h\le C_c/(1+C_ch/4)\), \(C_c=3.99614465135210151\ldots\), with the quantifiers of §5.3.

### 22.3 Theorem 69.KE — [P]

(a) For every minimal surface of general type and every \(k\ge1\), \(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/(A+k)\). The proof uses Burns-perpendicular cells from 59.R/59.KE, which are scalar-neutral at log order (\(s_1=0\), \(\Phi_D=\Phi=-s^2/32\)), with ADE/Kronheimer localization when \(X\) has \((-2)\)-curves.

(b) For covers of a negative KE host, the strict \(\theta\)-law \(\alpha/h\le4-4\theta\eta_X\) holds with cover-independent local constants.

(c) Fixed non-ball unramified hosts have \(\Delta_m=d_m\Delta_X\), so \(\sigma\to\infty\) as \(h\to0\). Balanced small-\(h\) slices need ball quotients, or varying or ramified hosts with \(\Delta_m/A_m\to0\). This is a necessary condition only.

**Handles.** Insertion at shrinking radius \(t=\sqrt\delta\) gives \(P(\widetilde g)=P(g)+32\pi^2+O(\delta^2)\); the AE handle tariff is exactly \(32\pi^2\). The fixed-radius argument is withdrawn.

### 22.4 The unit wall, universal ceiling, and attained positive gaps — [P] (Steps 71–72)

- For every metric with \(R>0\),
  \[
  \mathcal E-1=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R}.
  \]
  Therefore \(\alpha<1\) iff some conformal class has \(Y\ne0\) and \(\mathcal W<8\pi^2\chi\). The exact all-class ratio is §1 item 1.
- A smooth round-capped dumbbell with a long \(\mathbb R\times S^3\) cylinder, plus a fixed connected-sum replacement, proves \(\alpha(M)\le1\) for every closed four-manifold. Hence \(0\le\alpha\le1\) universally and \(2\chi\le3|\tau|\Rightarrow\alpha=1\).
- If \(T_+<0\), every metric has \(\mathcal E>1\), so the value 1 is not attained. If \(T_+=0\le T_-\), then \(\mathcal E(g)=1\iff W^+=0\) and \(s\) is a nonzero constant. With positive scalar curvature the equality class has \((b_1,b_2)\in\{(0,4),(1,0)\}\).
- \(\alpha=1\) is attained, by non-Einstein metrics, on \(S^1\times S^3/\Gamma\), on \(S^1\times_\phi H^3/\Gamma\), and on \(\#4\overline{\mathbb{CP}}^2\) (LeBrun's hyperbolic-ansatz classes \cite{lebrunself,ishida2003curvature}). K3 and \(T^4\) have value \(\alpha=1\) by the universal ceiling plus their unit-wall lower bound; their Ricci-flat Einstein metrics themselves have \(\mathcal E=4\).
- Constant-scalar ASD metrics on \(k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) have \(\mathcal E=1+9m/(3m+4y)\), with \(m=k+4\ell-4\) and \(y=s^2V/(32\pi^2)\). Replace \(y\) by \(Y^2/(32\pi^2)\) only for Yamabe minimizers.
- The long-circle reservoir remains valid and is subsumed by the dumbbell. It gives \(\alpha(N\#(S^1\times Y))\le1\), but no handle topology is needed for the universal theorem. On general-type handle/blow-up families, \(k+4\ell\ge A\) implies \(\alpha=1\); the converse was not proved in Step 71.
- Under the human functional, positive gap and Einstein existence are independent in both directions. The exact relation is: \(\alpha=0\) attained \(\iff\) Einstein with \(\lambda\ne0\).

### 22.5 Weyl connected sums and the remaining value problems — [P] (Step 72)

Let \(\mathcal W_*(M)=\inf\mathcal W\) and \(d_*(M)=8\pi^2\chi(M)-\mathcal W_*(M)\). Kobayashi subadditivity (quoted in \cite{malchiodiweyla}) gives
\[
 d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.
\]
Signature gives the exact values
\[
 \mathcal W_*(\#_n\overline{\mathbb{CP}}^2)=12n\pi^2,
 \qquad d_*=4\pi^2(4-n).
\]
Thus \(\alpha(\#_n\overline{\mathbb{CP}}^2)<1\) for \(n\le3\), while \(\alpha=1\) for \(n\ge4\). For a surface carrying a smooth negative Kähler–Einstein metric, connected-sum bookkeeping gives positive deficit for \(k<A/3\), so \(\alpha<1\) there. Extension over canonical orbifold singularities uses the separate ADE/ALE transfer and is not implicit in this sentence.

In the intermediate band \(A/3\le k<A\), the question \(\alpha<1\) versus \(\alpha=1\) is exactly whether
\[
 \inf_g\int|W^+|^2<2\pi^2(A-k)
\]
in the session norm. This is the classical all-class Weyl-functional problem; positive-Yamabe inequalities do not settle the negative-Yamabe sector \cite{akutagawaweyl,lebrun2023weyl}.

For \(0<k<A/3\), the value is rigorously in \([0,1)\), but neither a positive lower bound nor a family with \(\alpha\to0\) is known. The sharp object is the normalized conformal ratio \(d([g])/R(\widehat g)\), equivalently the supply coordinates \((p,\upsilon)\). The three structural ends (Einstein, aligned Blair–Ianus/Einstein–Maxwell, cscK) remain as in §21.11.

### 22.6 The intermediate band: realized crossing of 1/3, the Kähler frontier, and one capacity unknown — [P] (Steps 73–75; source `step74_packing_weyl_theorem_and_scope.md` §§1–3, verifier `trace/ttcs/results/step74_ttcs01_verifier1_integration.md`)

Norm: \(I_\pm=\int|W^\pm|^2_{\rm op}\); \(d=8\pi^2\chi-I_+-I_-\); on \(Y\#k\overline{\mathbb{CP}}^2\) with \(A_Y=c_1^2(Y)\), \(d=4\pi^2(A_Y-k)-2I_+\).

1. **Certified cell saving.** For an exact-CH-collared one-blow-up cell, \(p-1=\Delta I_+/2\pi^2+\Delta S/96\pi^2\), with the removed CH core contributing \(3x_0^2\) to \(S/96\pi^2\). The saving \(\eta=-\Delta I_+/2\pi^2\) is certified in \([0.0751342007982264634,\,0.0751342008160864400]\) for \((x_0,X)=(.03,128)\) and \([0.0221945778693642140,\,0.0221945778693642228]\) for \((.01,8)\) (exact dyadics in `workspace/data/step74_weyl_x00*.json`; outward endpoints). A special cell costs \(4\pi^2(1-\eta)\) of deficit instead of \(4\pi^2\).
2. **Theorem 74.W.** Let \(X_0\) be a compact ball quotient, \(X'\to X_0\) a preliminary normal cover with global injectivity radius \(>2R(X)\) (compact-fundamental-set displacement exclusion), \(Y\to X'\) any further finite cover, \(N\) the size of a \(2R\)-separated set. The inherited smoothing keeps the support inside the raw radius and preserves both \(P\) and \(S\) (errors \(O(\delta^3)\), \(O(\delta^2)\)), so for all \(k\) and \(n\le\min\{k,N\}\): \(d_*(Y\#k\overline{\mathbb{CP}}^2)\ge4\pi^2(A_Y/3-k+\eta n)\), hence \(k<A_Y/3+\eta n\Rightarrow\alpha<1\). With \(\beta_0=1/(9[4X(1+X)]^2)\le N/A_Y\le1/(9X^2)\): \(h<1/3+\eta\beta_0\Rightarrow\alpha<1\) (\(0.333333363065\ldots\) for \(X=8\)); disjoint fixed-radius copies can never exceed \(1/3+\eta/(9X^2)\), so the formal all-cell values \(1/[3(1-\eta)]\) are unattainable by them.
3. **Proposition 74.K (fixed-complex Kähler frontier).** On the prescribed blow-up complex structure, \(c_1=-H-\sum E_i\), \([\omega]=\pi^*a-\sum e_iE_i\); Hodge index gives \((c_1\cdot\omega)^2/\omega^2\ge A_Y\), hence \(I_+=S/24\ge4\pi^2A_Y/3\) and \(d\le4\pi^2(A_Y/3-k)\). The Kähler frontier is exactly \(h=1/3\), and 74.W shows that the true \(\alpha<1\) frontier lies strictly beyond it: crossing is intrinsically non-Kähler for that complex structure.
4. **One capacity unknown.** At a scalar \(-4\) Yamabe representative, \(p=k-\frac43\kappa+\frac13\upsilon\) with \(\kappa=A_Y/2-3I_+/8\pi^2\), and \(\alpha<1\iff\exists\) a negative Yamabe representative with \(\kappa>(3k-A_Y)/4\). Writing \(\kappa=\frac{A_Y}2\Theta\), the best-constant object is the capacity of the given manifold, \(\Theta_*(M)=\sup_{\widehat g}2\kappa(\widehat g)/A_Y\) over negative Yamabe representatives, with \(\alpha(M)<1\iff\Theta_*(M)>(3h-1)/2\). It is not known to depend on \(M\) only through \(h\) (earlier notation \(\Theta_*(h)\) withdrawn). The band constructions bound \(\Theta_*\) from below. Open-range positivity \(P_*>0\) in \(0<k<A/3\) is not an upper bound on \(\Theta_*\) alone: since \(\mathfrak p=k-\frac43\kappa+\frac13\upsilon\), it is the statement that the realizable pairs \((\kappa,\upsilon)\) stay uniformly away from the Einstein locus \(\frac43\kappa-\frac13\upsilon=k\) (§24.2(5)).
5. **Scale of the open problem.** By additivity, crossing \(1/3\) by a definite \(\varepsilon\) needs the exceptional insertions to remove a fraction \(\ge3\varepsilon/2\) of the host's total \(I_+\): on average an \(O(1)\) fraction of the \(W^+\)-energy of a region of volume \(\asymp V/k\) per class. Radial cells remove \(\eta/(6X^2)\le6\times10^{-5}\) of their footprint. A definite crossing would therefore need the same diffuse multiclass geometry whose absence (or impossibility) is the open-range positivity question. Radial-cell optimization is closed as a line.
6. **Theorems 87.O and 93.A (exact paired-\(A_1\) orbifold laws for ball-quotient hosts) [P; Step 87 deficit, Step 93 full variational law; `notes/step93_paired_A1_transfer_review.md`].** Let \(X\) be a compact ball quotient, \(A=c_1^2(X)\), complex orientation, and \(V_m=X\#m(S^4/\mathbb Z_2)\) (connected sums at smooth points; Satake orbifold Euler characteristic), with \(k=2m\). Then
   \[
   d_{*,\rm orb}(V_m):=\sup_{g\ \text{orbifold}}\bigl(8\pi^2\chi_{\rm orb}-I_+-I_-\bigr)=4\pi^2\Bigl(\frac A3-2m\Bigr).
   \]
   *Proof.* \(\chi(X)=A/3\), \(\tau(X)=A/9\); \(\chi_{\rm orb}(S^4/\mathbb Z_2)=1\), \(\tau_{\rm orb}=0\); connected sum subtracts \(2\) from \(\chi\), so \(\chi_{\rm orb}(V_m)=A/3-m\), \(\tau_{\rm orb}(V_m)=A/9\). The \(A_1\) links have zero signature \(\eta\)-correction, so every orbifold metric has \(I_+-I_-=12\pi^2\tau_{\rm orb}=4\pi^2A/3\), hence \(I_++I_-\ge4\pi^2A/3\) and \(d_{\rm orb}\le4\pi^2(A/3-2m)\). Conversely, Kobayashi conformal connected sum of the complex-hyperbolic metric (\(I_-=0\), \(I_+=4\pi^2A/3\)) with \(m\) round (conformally flat) \(S^4/\mathbb Z_2\) has \(I_++I_-\to4\pi^2A/3\). \(\square\) Exact arithmetic check: `scripts/step88_thm87O_check.py` → `data/step88/thm87O_check.json` (upper and lower sides equal the claim; EH resolution gives \(\Delta\chi=3m\), \(\Delta\mathcal W-8\pi^2\Delta\chi=0\), \(\chi\) of the resolution \(=\chi(X\#2m\overline{\mathbb{CP}}^2)\); the earlier necessary Einstein condition \(m<A/6\) is superseded by 93.A's exclusion for every \(m>0\)).
   *Conservation under resolution.* A Ricci-flat ALE space has \(\int_N|W|^2=8\pi^2(\chi(N)-1/|\Gamma|)\) (Gauss–Bonnet), exactly the Euler increment of the replacement; with Lemma 86.S (\(S\), \(P\) converge and \(d=S/24-P/2\)) the deficit converges, \(d(M,g_\varepsilon)\to d_{\rm orb}(V,g)\). For EH: \(\chi(N)=2\), \(|\Gamma|=2\), \(\int|W|^2=12\pi^2\); resolving all \(2m\) points gives \(\Delta\chi=3m\), \(\Delta\mathcal W=24\pi^2m=8\pi^2\Delta\chi\).
   *Step-93 strengthening.* Resolving an arbitrary orbifold metric by the orientation-matched EH spaces gives a metric on \(X\#k\overline{\mathbb{CP}}^2\). LeBrun's Yamabe theorem transfers \(\int(s^-)^2\ge32\pi^2A\), with no extra SW or \(b^+\) hypothesis. If \(\sigma=S-32\pi^2A\) and \(w=(I_++I_-)-4\pi^2A/3=2I_-\), then
   \[
   P=8\pi^2k+\sigma/12+2w,\qquad R=8\pi^2(A+k)+\sigma/3+2w.
   \]
   The Green-football cap \((\mathbb R^4\setminus0,(1+r^{-2})^2\delta)/\iota\) has two \(A_1\) points, one ordinary AE end and \(P=16\pi^2\); inserting \(m\) caps realizes the lower limits. Hence
   \[
   \boxed{P_{*,\rm orb}(V_m)=8\pi^2k,\qquad \alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}.}
   \]
   No \(V_m\) carries an Einstein orbifold for \(m>0\). The \(P\)-infimum is never attained: equality would force \(W^-=0\), and stationarity of \(P\) would make the metric critical for \(\int s^2\); the trace gives constant nonzero \(s\), and the trace-free equation gives \(\operatorname{Ric}^\circ=0\), contradicting \(P=8\pi^2k\). The defect infimum is not attained for \(k\ne A/3\); at \(k=A/3\), attainment is equivalent to a constant-negative-scalar metric with \(W^-=0\), which remains open.
   *Consequences and scope.* The limiting deficit \(4\pi^2(A/3-k)\) is still exactly the fixed-complex Kähler frontier of 74.K, and a CH-collared football cell has \(\Delta I_+=\Delta I_-\ge0\). This fixed orbifold topology cannot be an Einstein absorption mechanism even in the open range, and smooth convergence on its regular locus cannot describe a \(P\)-minimizing sequence because \(P_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k\). None of this bounds arbitrary smooth metrics, excludes other orbifold topologies, or reduces their optimization to marked-cell infima; Theorem 74.W's finite-scale smooth crossing is unaffected.
7. **Transfer through Kähler Ricci-flat fillers: Theorems 95.S, 95.F, Lemma 96.Ş, Theorem 96.K [P as necessary conditions; Steps 94–96; proofs `notes/step95_verified_transfer_lattice_thresholds.md`, `notes/step96_suvaina_lattice_and_kahler_filler_theorem.md`].** *Hypotheses.* \(X\) minimal of general type (for 95.F, 96.K: a compact ball quotient, aspherical with torsion-free \(\Gamma\)); \(V\) a compact oriented negative Einstein orbifold with isolated points whose links are spherical space forms, each resolved by a Ricci-flat ALE filler \(N_j\) with orientation-matched equivariant end chart and derivative-controlled decay (86.S), the resolution being orientation-preservingly diffeomorphic to \(M_k=X\#k\overline{\mathbb{CP}}^2\); \(\pi_1(N_j)\) finite (automatic, Şuvaina Lemma 4.1). \(C_\pm\) are the filler charges, \(k_b=k-\sum b_2(N_j)\), \(S_{\rm cx}=\sum_{\rm cx}(1-|\Gamma_j|^{-1})\), \(S_{\rm rev}=\sum_{\rm rev}(1-n_j^{-2})\).
   - *95.S (envelope and scope).* Exactly, \(9C_-+2C_++42k+12(3c_2(X)-c_1^2(X))\ge0\); the only host correction is the BMY defect. For ball quotients and Kähler fillers, \(S_{\rm cx}+\frac29S_{\rm rev}\le\frac k6+k_b\), and for complex-oriented fillers \(S_{\rm cx}\le k_b+\beta(k,A)\), \(\beta=k(5y+1)/[18(1+y)]\), \(y=\sqrt{1-3k/A}\). \(k_b\) is a rank deficit of the blow-up kernel, not a set of embedded exceptional spheres. Each retained rank adds one unit of slack; the inequalities still exclude configurations whose cost exceeds the slack (two \(D_2\) at \(k=5,k_b=1\)), but after they pass they see neither class placement, nor discriminant linking, nor singular monopole data. A Wahl ball absorbs no rank; Wahl points may accompany a full-rank system at \(k_b=0\).
   - *95.F (full-rank root systems).* Norm-two vectors of \(I_k\) are \(\pm e_i\pm e_j\); on each connected signed support the reflection closure is \(A_{m-1}\) (rank \(m-1\)) or \(D_m\) (rank \(m\)). A full-rank ADE subsystem is \(\bigoplus D_{a_i}\), \(\sum a_i=k\) (\(D_2=A_1\oplus A_1\), \(D_3=A_3\)); \(E_{6,7,8}\) embed in no \(I_k\); the sublattice has index \(2^q\) for \(q\) blocks.
   - *96.Ş (Şuvaina fillers; scope extended Step 98, proof repaired Step 99).* By Şuvaina's classification (Prop. 4.4, Theorem B) every non-simply-connected Kähler Ricci-flat ALE surface is \(\widetilde N/\mathbb Z_n\), with \(\widetilde N\) the minimal resolution of a possibly singular invariant fibre \(xy=\prod_{i=1}^d(z^n-c_i^n)\), \(c_i\ne0\), end \(\frac1{dn^2}(1,dnm-1)\). The smooth-fibre quotients do not exhaust this class biholomorphically, but do up to equivariant orientation-preserving diffeomorphism: admissible GH centre sets form a connected configuration space in \(\mathbb R\times\mathbb C^*\), and an equivariant family-bundle/horizontal-lift argument (not ordinary Chern numbers alone) lifts a centre isotopy, fixed near infinity, across the Hopf fillings. For every member \(H_1=\mathbb Z_n\), \(\chi=d\), \(H_2\cong A_{d-1}(-1)\) torsion-free, and transfer maps \(H_2(N)\) onto the invariant lattice.
   - *96.K (full absorption by Kähler fillers).* If \(k_b=0\), every positive-rank filler is complex-oriented and its lattice embeds orthogonally in \(-I_k\); the block structure is \(\bigoplus D_{a_i}\); Şuvaina fillers occur only inside \(D_2\) (\(d=2\)) or as \(D_3\) (\(d=4\)) at higher cost (\(1-1/(dn^2)\), \(n\ge2\)); blocks \(D_{a\ge4}\) are single Kronheimer fillers. Since every block of rank \(\le5\) costs more than rank\(/6\), **some Kronheimer \(D_a\), \(a\ge6\), is required; \(k\ge6\); at \(k=6\) only a lone \(D_6\) without Wahl points, with \(A\ge3675/64\) (\(A\ge63\) for ball quotients).** Exact thresholds: \(D_7\): \(32041/1040\); \(D_8\): \(8281/288\); first mixed rows \(D_3\oplus D_8\): \(9409/96\), \(D_4\oplus D_7\): \(196249/160\), \(D_2\oplus D_{10}\): \(51483/128\) (Step-95 certificate, all partitions \(k\le40\)). At \(A=3k\), \(\beta=k/18\): equality rows belong to the open wall problem.
   *Scope.* Necessary conditions only. Each survivor still needs compatible prism-manifold linking in the index-\(2^q\) gluing, a compact orbifold complement, and a negative Einstein orbifold metric; none is known. Retained-rank and Wahl configurations, and non-Kähler Ricci-flat fillers (none supplied by the material read here; Şuvaina classifies only the Kähler category), are outside 96.K.
   - *98.W (integral gluing of Wahl balls; repaired Step 99) [P; proof `notes/step96_suvaina_lattice_and_kahler_filler_theorem.md` §3].* Let \(X\) be aspherical with torsion-free \(\pi_1\), \(B_j\subset M\) disjoint Wahl balls, and \(W\) their connected complement. Write \(G=\oplus\mathbb Z_{n_j^2}\), \(K=\oplus n_j\mathbb Z_{n_j^2}\), and \(i:G\to H_1(W)\). Mayer–Vietoris and triviality of finite \(\pi_1(B_j)\to\pi_1(X)\) give \(\ker i+K=G\); since \(K\subset\Phi(G)\), \(i=0\). Hence \(0\to H_2W\to H_2M\to K\to0\), \(H_1(W)\cong H_1(X)\), torsion in \(H_2(W)\) maps isomorphically onto that in \(H_2(M)\), and the free lattice has index \(\prod n_j\), determinant \(\prod n_j^2\). Eliminating the isomorphic torsion block in the pair sequence gives \(0\to L\to L^*\to G\to0\) and the discriminant–linking identification even when \(H_1(X)\) has torsion; \(U/L\) is the specified metabolizer \(K\). Asphericity also splits \(L=Q_X\oplus L_0\), \(L_0\subset-I_k\).
   - *98.V (bilinear realization and low-rank obstruction; repaired Step 99) [P].* For any parameters and orientations, \(k\ge4t\) realizes the required forms and metabolizer inside \(-I_k\): choose \(N_j\equiv-\sigma_j(n_ja_j-1)u_j^2\bmod n_j^2\), represent \(N_j\) by four squares, and use congruence kernels on disjoint four-coordinate blocks. Four is sharp uniformly for one point (target \(7\bmod8\) at \((8,1,-1)\)); below the range bilinear data can obstruct (complex-oriented \(B_{2,1}\) needs rank at least three). Exact check `scripts/step99_wahl_four_coordinate_check.py` → `data/step99/wahl_four_coordinate_check.json` (158 single-point cases through \(n=16\), both signs; all pass). Compatible boundary gluing already yields the abstract primitive resolution-chain embedding and recovers Theorem 55.5 at \(k=1\); it is not a separate bilinear input. Remaining inputs are geometric realization of the prescribed complement/embedded pieces, characteristic/spin\(^c\) refinements, and singular curvature data.
    - *102.R / 102.K / 103.I (realized Wahl sector) [P; `notes/step102_wahl_orbifold_realization_and_K2_invariance.md`, independently read in `notes/step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`].* In disjoint exceptional blocks, PPS gives complex-oriented \(B_{n,1}\) embeddings with cost four coordinates for \(n\ge3\) (three for \(n=2\)); coning gives a degree-one orbifold \(V\to X\), ordinary \(\pi_1(V)=\pi_1(X)\), and PPS Prop. 5.1 gives resolution \(X\#(k+\sum(n_j-1))\overline{\mathbb{CP}}^2\). Exact Wahl corrections preserve \(T_+^{\rm orb}=A-k\), so filler transfer reproduces the smooth scalar/mixed Einstein constraints and excludes Kähler–Einstein orbifold metrics; the minus-side correction is slack in the realized block range. The cohomology sequence with cokernel \(\oplus\mathbb Z_{n_j}\) is proved, but the blanket orbifold–resolution SW correspondence is [C]. At every \(n\ge3\) point, local isotropy forces both Weyl blocks to have a repeated eigenvalue; it does not obstruct an invariant Einstein germ. CH/Kähler symmetric type is excluded, and RH type is excluded when \(\tau_{\rm orb}=A/9-k+\frac23\sum(1-n_j^{-2})\ne0\). Fine–Premoselli ramification, toral Dehn filling and KE/cscK smoothing do not apply to this topology; existence remains open.

## §23 (Steps 74–79) — Q4: almost-Kähler Einstein torsion zeros (closed negative Goldberg) — status
Sources: `step75_Q4_half_twistor_torsion_and_zero_index.md` (TTCS-corrected), `step76_Q4_chern_weil_density_and_prolongation.md`, `step77_79_Q4_higher_prolongation.md`; A01 `step62_torsion_zero_prolongation.md`, `step63_SU2_nut_and_clean_zero_surface.md`.

### 23.1 Setting — [P]
On a closed almost-Kähler 4-manifold the Nijenhuis/torsion field is a section of \(E=\Lambda^{0,2}\otimes T^{1,0}\), \(c_2(E)=5\chi+6\tau\); on a closed AKE (Einstein, \(\lambda<0\)) manifold with \(5\chi+6\tau>0\) torsion zeros are forced. This is elementary: \(E\cong K^{-1}\otimes T^{1,0}\), \(c_2(E)=c_2+2c_1^2=5\chi+6\tau\), and Hitchin–Thorpe with \(\chi>0\) gives \(5\chi+6\tau\ge\chi>0\). The nowhere-zero Nijenhuis statement is Apostolov–Armstrong–Drăghici Lemma 2, attributed there to Armstrong 1997 and LeBrun. Armstrong 2002 (\cite{armstrong2002ansatz}; metadata and abstract only) is a distinct \(W^+\)-eigenform rigidity statement and is not used; §23 makes no priority claim about zero structure. Complete noncompact strict AKE examples without zeros exist (Fino/A01 Bianchi-VIII pair, Step 74), so any obstruction must live at zeros or be global.

### 23.2 Theorem 75.H (corrected) — [P]
With \(\alpha=a+iJa\) and \(db=a\wedge Ja-R(\Omega)\), \(d_b\alpha=-R(J\phi+i\phi)\); the primitive \((1,1)\) part of \(d_b\alpha\) equals \(-\tfrac12\widetilde{\operatorname{Ric}}''\). Thus \(\operatorname{Ric}''=0\) is an injective-symbol (overdetermined elliptic) first-order system on the torsion; gradient summands \(\Lambda^{1,1}_0\oplus\mathbb C\Omega\oplus\Lambda^{2,0}\oplus S^{2,0}\); sharp Kato constant \(3/4\). Norm-only Bochner data are index-blind; the canonical Hermitian Chern–Weil density of \(c_2(E)\) has no sign (positive, monotone \(6\to42\) on the exact pair, Step 76): smooth characteristic-density routes are closed.

### 23.3 Theorem 76.Z (order 2) — [P] (A01 62.A invariantly; Darboux computation here)
At a torsion zero with jet \(f=cz+(S+A)\bar z\): \(\|A\|^2=\|S\|^2+8|c|^2\), \(\det_{\mathbb R}Df=9|c|^4+|\det B|^2\ge25|c|^4\). Every nondegenerate zero has index \(+1\); \(W_3^+(p)\ne0\) is forced by a nonzero jet. Consistent with \(5\chi+6\tau>0\); not by itself an obstruction.

### 23.4 Higher prolongation — [P] structure, [N] values (Steps 77–80; 79.C refuted, see 23.5)
- Degree count: \(E_k\) collects jets of total degree \(k+2\) (Ricci) or \(k\) (\(\lambda\)); orders 1–5 are affine in \((H_4,\dots,H_7)\) once \((H_2,H_3)\) are fixed; \(E_6\) is quadratic in \(H_4\) through a universal flat form. Parity: even germs solve all odd orders.
- Linear Hilbert data: excess \(\binom{k+1}{3}\) (one scalar compatibility \(\Phi\)).
- **Order-6 reduction [N].** For fixed \((H_2,H_3)\) the real order-≤6 system reduces exactly to one scalar condition \(\pi\cdot c+j\cdot z+\tfrac12z^TH_rz=0\) with \(H_r\) positive definite (12-dim at \(H_3=0\)), so real solvability \(\iff\Phi_6\le0\). Two independent pipelines agree to \(10^{-11}\).
- **Controls.** Kähler 2-jet: no scalar condition, all rows absorbed, solved to \(2\times10^{-12}\) (as required by KE existence).
- **Values (sampling bias, superseded by 23.5).** The Steps 78–79 sample (≈6 jets chosen by earlier pipelines) happened to lie in \(\{\Phi_6>0\}\): the near-degenerate D6 jet (\(3.98\times10^{-4}\) at \(\lambda=-3\); positive at \(\lambda=0,3\)); a generic jet with \(|c|^2\approx0.04\) of unit torsion norm: \(\Phi_6\approx0.78\) (\(\lambda=-1\)), \(0.86\) (\(\lambda=+1\)), essentially unchanged by shifting the torsion-free (\(W^-\)) part of the 2-jet. A nonzero odd jet \(H_3=t h_3\) adds four order-5 conditions and increased \(\Phi_6\) monotonically along the direction tested (\(t=0.1,0.3,1,3\): \(0.0029,0.0037,0.030,1.59\)).
- **Conjecture 79.C — REFUTED at order 6 (Step 80, independently confirmed by A01 Step 67).** It asserted that no real formal AKE germ has a nondegenerate torsion zero. A wide scan shows \(\Phi_6\) takes both signs on the strict cone, and explicit real jets through order 6 at nondegenerate index-\(+1\) zeros exist (Proposition 80.R, §23.5). A01 re-evaluated the saved jets in its own independent \((g,\omega)\) equations after a polynomial coordinate pullback: system norms \(6.7\times10^{-8},1.4\times10^{-7},8.4\times10^{-9}\), positive control \(4.78\). What order 6 imposes at a nondegenerate zero is the semialgebraic constraint \(\Phi_6\le0\). Lesson recorded: a handful of jets selected by earlier pipelines produced a false uniform sign.


### 23.5 Step-80 correction: Conjecture 79.C fails at order 6 — [N]
Source: `notes/step80_Q4_universal_functional_and_lambda_quadratic.md`; data `data/step80/`.
- The surviving order-6 functional is universal: \(\ell=C_6\pi\) has \(|\cos|=1\) across all tested jets. \(\Phi_6\) has weight 8 under \(x\mapsto\mu x\), and it is exactly quadratic in \(\lambda\): \(\Phi_6=F_0+F_1\lambda+F_2\lambda^2\) with weights 8, 6, 4.
- \(F_0\), \(F_1\) and \(F_2\) each take both signs on the strict cone. Among 8 generic unit-torsion jets, gen2 has \(\Phi_6<0\) at \(\lambda=-5,0,5\), and gen5 and gen6 have \(\Phi_6<0\) at \(\lambda=-5\). All small-\(c\) and large-\(c\) jets sampled have \(\Phi_6>0\). The Steps 78–79 jets (D6 and the A01 shared jet) lie in \(\{\Phi_6>0\}\).
- **Proposition 80.R [N].** Explicit real jets \(H_2,\dots,H_8\) were constructed (`scripts/step80_reconstruct.py`) for gen2 at \(\lambda=0\) and \(\lambda=-5\), and for gen5 at \(\lambda=-5\). In each case the torsion zero is nondegenerate with index \(+1\), the jet lies on the cone, \(H_3=0\), and all unreduced residuals \(E_0,\dots,E_6\) are \(\le1.2\times10^{-7}\) at coefficient norm about \(10^3\). The positive control (lsA jet0, \(\lambda=-1\)) retains its residual, with \(\Phi_6=0.842\). Hence **79.C is false at order 6**: order 6 imposes a semialgebraic constraint \(\Phi_6\le0\), not an obstruction. Order 8 is treated in §23.6: there is no rank obstruction, and a cross-evaluated numerical order-8 witness exists at gen5, \(\lambda=-5\) (two independent equation systems, relative residuals \(\sim10^{-15}\)); it is not an exact certificate or a convergent germ. The earlier \(\lambda=-40\) value is ill-conditioned (\(H_\pi\) min eigenvalue \(7\times10^{-15}\)) and is withdrawn.
- Status for Q4: what survives unconditionally is 76.Z (index \(+1\) at nondegenerate zeros, cone) together with \(\Phi_6\le0\). A local formal route to closed negative Goldberg would need a nonlinear obstruction at order \(\ge8\) on the region \(\{\Phi_6\le0\}\). By §23.6 there is no linear (rank) obstruction there at the jets tested. Otherwise the route needs global input.

### 23.6 Order 8 and the scalar compatibility operator (Steps 81–84) — [P] identification, [N] order-8 solvability at one nondegenerate zero
Sources: `notes/step84_scalar_compat_derivation.md`, `scripts/step84_scalar_compat.py` → `data/step84/scalar_compat.json`; `scripts/step81_order8.py` → `data/step81/order8_*.json`; A01 `step68_scalar_compatibility_and_radial_multiplier.md` (message #860).
- **Proposition 84.P (scalar compatibility) [P; derived in this Session, agreeing with A01 Step 68].** Let \(\mathcal P(E)=J^i{}_aJ^j{}_b\partial_a\partial_bE_{ij}-\tfrac12\Delta\operatorname{tr}E\). For anti-\(J\) (hence tracefree) \(h\), \(\mathcal P(d\mathrm{Ric}_{\rm flat}(h))=0\). Two-line Fourier proof: with \(R=\widehat{d\mathrm{Ric}}(h)\) and \(Jk\perp k\), \((Jk)^TR(Jk)=\tfrac12|k|^2k^Thk\) and \(\operatorname{tr}R=k^Thk\). On the conformal direction \(\mathcal P(d\mathrm{Ric}(f\delta))=\Delta^2f\), so \(\mathcal P\) is not a Bianchi consequence; it is the compatibility created by restricting to fixed-\(\omega\) (Darboux) perturbations. Exact rank counts in our own tower for \(d=4,6,8\): \(\operatorname{coker}L_d=B_d\oplus\mathcal P_d\), with dimensions \(90=80+10\), \(259=224+35\), \(564=480+84\), and \(|B_dL_d|=|\mathcal P_dL_d|=0\). By \(U(2)\)-transitivity on \(S^3\), the only invariant functional is the radial class \(\Delta^{(d-2)/2}\mathcal P(E_d)(0)\) at even \(d\), and there is none at odd \(d\). At \(d=6\), every saved universal multiplier \(\ell\) of §23.5 (four jets) equals this radial class modulo Bianchi, \(|\cos|=1\) to \(2\times10^{-16}\). Hence \(\Phi_6\le0\) is exactly the radial moment \(\Delta^2\mathcal P(E_6)(0)\) of one natural compatibility operator, minimized over the free jets.
- **Order 8 [N].** Kähler control (\(\lambda=-1\)): converged, unreduced \(E_0\ldots E_8\le3.0\times10^{-10}\). Strict jets gen2 (\(\lambda=-1,0\), six LM starts) and gen5 (\(\lambda=-5\), A01's point, task s83_t7): LM was started on the order-6 root (\(r_6\sim10^{-8}\), \(\|r_8\|\sim10^3\)). It ends at residual \(0.10\)–\(0.32\), still slowly decreasing, with \(r_6\) degraded to \(\sim0.1\)–\(0.2\). The projected Jacobian has rank 91 in all seven runs, and **this is full rank**. The variable projection removes the 28-dimensional range of the constant \(w\)-matrix (`M_rank_w_to_r8=28`; the newest jet \(w\in\ker L_6\) reaches 28 of the 84 \(\mathcal P\)-rows, which is A01's count \(28/84\)). The projected system therefore has \(259+564-28=795\) rows, as recorded, and \(35+84-28=91\) nontrivial rows. The earlier reading of 91 out of 119 double-counted the absorbed rows. Our reduced order-8 Jacobian is surjective at both gen2 and gen5, which is A01's rank-84 submersion at gen5 stated after eliminating \(w\) (\(84=28+56\)). The two pipelines agree, and there is no rank obstruction at order 8. The LM failure is a global-path effect: the order-6 surface is curved and the order-8 root is far away. Continuation along \(\{r_6=0\}\) is the appropriate instrument. **Order-8 witness, cross-evaluated [N].** A01 polished an order-8 jet at gen5, \(\lambda=-5\), by continuation (A01 Step 69–71, `S1003A01/workspace/data/step69/order8_polished_{v,h10}_recon_F012_gen5_lam-5.npy`; message #862). It was evaluated here in our own unreduced Darboux tower (`scripts/step84_eval_a01_order8.py` → `data/step84/eval_a01_order8_gen5_lam-5.json`). Residual norms: \(E_0=2.7\times10^{-15}\), \(E_2=3.5\times10^{-12}\), \(E_4=2.6\times10^{-10}\), \(E_6=4.5\times10^{-9}\), \(E_8=9.8\times10^{-7}\); odd orders vanish by parity. For scale, removing \(H_{10}\) gives \(\|E_8\|=1.5\times10^8\) and removing \(H_8\) gives \(\|E_6\|=5.3\times10^6\), so the relative residuals are \(\sim10^{-15}\). The torsion jet is unchanged from our order-6 point: cone defect \(2\times10^{-16}\), \(\det Df=0.02337>0\), index \(+1\). Its \((H_4,H_6)\) differ from our Step-80 reconstruction by relative distances \(2.5\) and \(12.9\): the continuation moved along the large order-\(\le6\) solution variety. Coefficient norms grow fast, \(\|H_4\|,\|H_6\|,\|H_8\|,\|H_{10}\|\approx1.6\times10^3,1.5\times10^4,6.5\times10^5,8.6\times10^6\) at unit torsion norm. Hence a real formal AKE germ with a nondegenerate index-\(+1\) torsion zero exists through order 8 to floating-point accuracy, verified by two independent equation systems. This is a high-accuracy numerical formal jet, not an exact certificate and not a convergent germ. Our own homotopy (`scripts/step84_order8_homotopy.py`) stalled near \(t=0.035\). Its fixed corrector tolerance of \(10^{-8}\) sits at the residual floor for coefficients of this size, so the stall is a property of the instrument. The script is kept with a tolerance of \(5\times10^{-8}\). Once the cross-evaluation above succeeded, the rerun was cancelled as redundant. Local formal prolongation thus gives no obstruction through order 8 at nondegenerate zeros. The local route to closed negative Goldberg is closed in practice: no further order is likely to change the judgment without an organizing reason.
- **Curvature directions and the compatibility rows: lift-quotient computation [N, peer A01 #866, which withdraws the fibre interpretation of #864; not independently rerun here].** At gen5, \(\lambda=-5\), \(\ker(dE_0,dN_1)\) in the 60-dimensional \(H_2\) space has dimension 40; quartic-Hamiltonian gauge has rank 35, leaving exactly five orthonormal physical \(H_2\) curvature directions. Minimum-norm higher lifts give rank-five responses in the order-6 and order-8 compatibility rows, with nonzero radial components; but these responses are not intrinsic. Quotienting by all admissible fixed-\(H_2\) higher corrections kills them: at order 6, \(\operatorname{rank}B=35=\dim\mathcal P_6\), quotient norm \(8.6\times10^{-11}\), radial quotient \(1.8\times10^{-12}\); at order 8, \(\operatorname{rank}B=84=\dim\mathcal P_8\), quotient norm \(4.2\times10^{-10}\), radial quotient \(2.0\times10^{-11}\). Imposing fixed higher coordinate Nijenhuis coefficients with the \(H_2\) source included is inconsistent (residuals 47.8 and 9302): the curvature directions force higher coordinate torsion, so a "fixed-torsion fibre" is not well defined in these coordinates. Consequently neither a torsion-only radial hierarchy nor intrinsic \(W^-\) dependence of the compatibility rows is established; the earlier inference from #864 is withdrawn. A covariant prolonged quotient modulo one prolonged Hamiltonian pullback remains to be formulated (A01 `S1003A01/workspace/notes/step72_H2_curvature_factorization.md`, data `step72/lift_quotient_K{6,8}.json`). Proposition 84.P and the cross-evaluated order-8 witness are unaffected. **Peer refinement #869 [N, A01 Step 72; not rerun here].** The five physical degree-two directions are exactly the \(W^-\) block in the complex orientation (linearized \(W^-\) rank 5; \(W^+\) and both gauge blocks vanish at \(10^{-15}\)). Fixed-\(H_2\) higher corrections map with full rank onto \(\mathcal P_6\) and \(\mathcal P_8\), so the compatibility responses of these \(W^-\) directions factor through admissible higher corrections and no intrinsic scalar compatibility class survives through order 8.
- **Q4 scope after §23.** Forced zeros \(5\chi+6\tau>0\). At nondegenerate zeros: index \(+1\), the order-2 cone, and the single scalar constraint \(\Phi_6\le0\), now identified with \(\mathcal P\). Local prolongation does not obstruct through order 6 (generic sign-indefinite \(\Phi_6\)), and through order 8 at the cross-evaluated witness. Smooth characteristic densities have no sign. A01's degenerate-zero classification and zero-surface degree law cover the degenerate regime (peer results). A closed-manifold argument needs zero-sensitive global input.

## §24 (Step 82) — Problems 1–3 with their original quantifiers, and the common mechanism

Sources for the problem statements: `Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/five_research_problems.tex` §§1–3 (lines 380–632). Tags: **[I]** inherited (literature or project corpus, cited where it first enters this package), **[P]** proved in this Session (verified record named), **[C]** conditional on named hypotheses, **[N]** numerical structure, **[O]** open. Verifier of this section: `trace/ttcs/results/step82_ttcs01_verifier1_integration.md` (corrections applied in Step 82). Throughout, \(X\) is a minimal compact complex surface of general type, \(A=c_1^2(X)>0\), \(M=X\#k\overline{\mathbb{CP}}^2\), \(k\ge1\), \(h=k/A\), \(T_+(M)=2\chi+3\tau=A-k\), and \(\mathfrak p=P/8\pi^2\). Two infima are kept apart: \(P_*(M)=\inf_gP\) (the corpus Problem 2 uses the curvature-operator norm, \(I_R(M)=\inf_g\int|\mathrm{Rm}_{\rm op}|^2=8\pi^2\chi+P_*\); in the full tensor norm \(\int|\mathrm{Rm}|^2=32\pi^2\chi+4P\)) and \(\alpha(M)=\inf_g\mathscr D\) (the human functional, §1).

### 24.0 Elementary links used below — [I] identities, elementary specializations
Attribution. The curvature and conformal identities behind L2 and L3 are inherited from the project corpus: `Skills/geometric-analysis/research/Curvature_Realizability.tex`, equations `eq:lc-E-formula` and `eq:lc-chiral-E` (lines ≈3753–3770: \(\mathscr D=(4P+L_s)/R\ge4P/R\) and \(R-4P=24\pi^2T_+-12\int|W^+|^2\)), together with the Yamabe replacement and convex comparison (lines ≈2800–2864). What this Session adds is the elementary specialization to \(X\#k\overline{\mathbb{CP}}^2\) in the two corollaries below: the band bound and the zero-versus-positive equivalence.

- **(L1) Existence = attainment at zero.** LeBrun's Yamabe theorem \(\mathcal Y(M)=-4\pi\sqrt{2A}<0\) [I; LeBrun, *Kodaira dimension and the Yamabe problem*, CAG 1999, Theorem 2, \cite{lebrun1999kodairaa}: for every compact complex surface of Kodaira dimension 2 with minimal model \(X\), \(\mathcal Y(M)=\mathcal Y(X)=-4\pi\sqrt{2c_1^2(X)}\). Theorem 1 there treats the \(b^+=1\) minimal and non-minimal inputs, so no \(b^+\ge2\) restriction enters L1. Source read Step 83: `Knowledge/objects/papers/Kodaira-dimension-and-the-Yamabe-problem--d0edcef7bc67--1bd338503143/object.md`] excludes scalar-flat and Ricci-flat metrics, so every Einstein metric on \(M\) has \(\lambda<0\). With §22.4 (\(\alpha=0\) attained \(\iff\) Einstein with \(\lambda\ne0\)):
  \[
  M\ \text{carries an Einstein metric}\iff \alpha(M)=0\ \text{and it is attained}\iff P_*(M)=0\ \text{and it is attained}.
  \]
  Positivity \(P_*>0\) or \(\alpha>0\) is strictly stronger than nonexistence: it also excludes non-attained zero gaps.
- **(L2) Chiral comparison on every closed \(M\) with \(T_+>0\).** From \(C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2=T_++\mathfrak p\) one gets \(R\le8\pi^2(4\mathfrak p+3T_+)\), hence pointwise
  \[
  \mathscr D(g)\ \ge\ \frac{\mathfrak p(g)}{\mathfrak p(g)+\tfrac34T_+},\qquad \alpha\ge\frac{\mathfrak p_*}{\mathfrak p_*+\tfrac34T_+}
  \]
  (inherited: immediate from `eq:lc-chiral-E` and \(\mathscr D\ge4P/R\); §22.1; the right side is increasing in \(\mathfrak p\), checked symbolically in Step 82). Combined with LeBrun's \(\mathfrak p_*\ge k-A/3\) [I; \cite{lebrun2001ricci}, Prop. 3.2: \(\frac1{4\pi^2}\int(\frac{s^2}{24}+2|W_+|^2)\ge\frac23A\) for every metric on \(X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), equality only if \(k=\ell=0\); its proof notes that \(A>0\) makes the SW invariant of \(X\) polarization-independent even for \(b^+(X)=1\)] this gives the band lower bound
  \[
  \boxed{\ \alpha(X\#k\overline{\mathbb{CP}}^2)\ \ge\ \frac{4(3k-A)}{3k+5A}\qquad (A/3\le k<A)\ }
  \]
  [I identities + elementary corollary]; it vanishes at \(k=A/3\). At \(k=A\) (\(T_+=0\)) the comparison gives \(\mathscr D\ge1\) directly whenever \(p>0\), and the universal ceiling gives \(\alpha=1\).
- **(L3) Zero versus positive** [I ingredients + elementary corollary]. For \(1\le k<A\), L2 and the supply upper comparison (inherited conformal bridge, `Curvature_Realizability.tex` lines ≈2800–2864, with the scalar budget) \(\alpha\le4\mathfrak p_*/(A+\mathfrak p_*)\) (§22.1) give
  \[
  P_*(M)=0\iff\alpha(M)=0,\qquad P_*(M)>0\iff\alpha(M)>0.
  \]
  This equates only the vanishing of the two infima, not the functionals or their minimizing sequences.

### 24.1 Problem 1 (non-minimality; LeBrun 1996, 2009): does \(M\) carry an Einstein metric, for arbitrary Riemannian metrics?

**Status.** Settled negatively for \(k\ge A/3\) [I; \cite{lebrun2001ricci}, Theorem 3.3 and Corollary 3.4, valid for all \(b^+(X)\) by the polarization remark in the proof of Prop. 3.2; restated as LeBrun 2026 Thm 6.11 in the corpus]. Settled negatively on the window \((\frac13-\varepsilon)A<k<\frac A3\) wherever the metric-wise actual-class supply of the corpus N1 theorem holds, with genuine examples \(X_d\subset\mathbb{CP}^3\), \(d\ge5\), \(k_d=\lceil A_d/3\rceil-1\), \(A_d\ge2/\varepsilon\) [I, project corpus, `five_research_problems.tex` (blowgap)–(threshold)]. On that supply class the corpus also gives the quantitative gap: with \(j_0=\varepsilon-(\frac13-\frac kA)_+>0\), one has \(\mathcal J\ge j_0\), \(\alpha\ge j_0\) and \(P\ge8\pi^2j_0A/(4-j_0)\) [I]. **Open [O]** for \(1\le k\le(\frac13-\varepsilon)A\), in particular for a few blow-ups of large-\(A\) surfaces. No Einstein construction is known either.

**What this Session established about Problem 1.**
1. *Reformulation (L1).* Problem 1 is exactly the question whether the value \(0\) of \(\alpha\) (or of \(P\)) is attained on \(M\). For every minimal general-type \(X\) and \(1\le k<A/3\), \(0\le\alpha(M)<4k/(A+k)<1\) (Theorem 69.KE, including its canonical-model and Kronheimer localization). Since \(4k/(A+k)\to0\) as \(k/A\to0\), families of varying topology with \(\alpha\to0\) exist. The open object is a zero infimum on a fixed blow-up, or rates below this upper scale.
2. *The unit per-class tariff is false* [P]. Corollary 59.KE gives \(P_*<8\pi^2k\) for every fixed minimal general-type \(X\) and every fixed \(k\ge1\), so an unrestricted inequality \(P\ge8\pi^2k\) (equivalently \(C_+\ge A\)) cannot hold. The enclosure \(\mathfrak p_{\rm cell}\in[0.99566273275,0.99566273278]\) concerns CH-collared cells (§4.3), not arbitrary hosts. Other topological, gauge-theoretic or entropy obstructions are not excluded by this.
3. *Necessary conditions an Einstein metric would have to satisfy* [P]. For a realizable best-sign class \(a\) and any orthogonal \(J\) with \(c_1(J)=a\), \(\sqrt{P/2}\ge2\pi|a^-|-\|t_J^-\|_2\) (§21.10); at an Einstein metric the harmonic part is exact, \(\mathsf H^-(t_J^-)=2\pi h_a^-\), so \(\|\mathsf H^-(t_J^-)\|_2=2\pi|a^-|\). For such a class, \(q^2=|a^-|^2\ge k\). (Separately \(|E_i^-|^2=1+|E_i^+|^2\ge1\), but \(E_i\) is not itself an almost-complex Chern class.) An Einstein metric is also the "Einstein end" \(\delta=1,\ L=0\) of the ledger \(p=q^2(1-\delta)^2+L\) (§21.11).
4. *A sufficient zero-gap architecture on a fixed blow-up, whose existence remains open outside the paired-\(A_1\) case* [P for the implications; O for existence]. Let \(V\) be a compact Einstein orbifold with \(\lambda\ne0\) whose Ricci-flat ALE resolution, or Milnor-fibre smoothing at Wahl points, is diffeomorphic to \(M\). Then \(P_*(M)=\alpha(M)=0\) (Lemma 86.S with Cor. 52.8, 52.9(i), 56.B, Prop. 58.O): the defect converges along the gluing, with Ricci and scalar-variance errors \(O(\rho^4)\) automatically, and covers do not change \(\mathscr D\). Since \(\mathcal Y(M)<0\), the negative-Yamabe exclusion of 86.S forces \(\lambda<0\): Ricci-flat and positive-Einstein orbifold bulks cannot resolve or smooth to \(M\) through these cutoffs. The paired-\(A_1\) type \(X\#m(S^4/\mathbb Z_2)\) for \(X\#2m\overline{\mathbb{CP}}^2\) is now excluded over ball quotients by 93.A (equivalently, the corresponding summand-exchanging invariant Einstein architecture on the double cover is absent). Remaining candidate types include \(X\#\Sigma_4\) for \(X\#Q_3\) (diffeomorphism to \(X\#3\overline{\mathbb{CP}}^2\) pending, 52.7b), Wahl-point orbifolds, and other ALE root-lattice absorptions. The exceptional classes are carried by bubble root lattices (\(A_1^{\oplus2},A_3,D_n\) absorb; a single \(A_1,A_2,E_{6,7,8}\) absorbs nothing; at \(k=1\) a root lattice inside \(\mathbb QE\) cannot absorb \(E\), while mixed host–exceptional lattices need the degree-one/SW\(_L\) input) or stay in the bulk lattice (Wahl). Known constraints. (a) Under the stated orbifold SW supply (52.9(iv)), the numerical necessary condition is \(k\le A/3\); this does not establish existence and leaves the strict hard range \(0<k<A/3\) unobstructed. (b) For ball-quotient \(X\) and the \(S^4/\mathbb Z_2\) type, Theorem 93.A strengthens 87.O completely: \(V_m\) carries no Einstein orbifold for any \(m>0\), including \(2m<A/3\); its exact orbifold infima are \(P_{*,\rm orb}=16\pi^2m\) and \(\alpha_{\rm orb}=\min\{1,8m/(A+2m)\}\). (c) The parity lemma (52.9(v)) excludes absorption of even one class in a complex crepant resolution, so an absorbing \(V\) is non-Kähler. (d) At \(k=1\) the zero-charge Wahl bulk is non-complex (Prop. 55.6 as reproved in §17). (e) Over a ball quotient with Kähler Ricci-flat fillers (Kronheimer, or Şuvaina quotients including minimal resolutions of singular invariant fibres; complete by Şuvaina's classification, and diffeomorphic to smooth-fibre models), Theorem 96.K (§22.6(7)): absorbing all \(k\) ranks requires a Kronheimer \(D_{a}\) filler with \(a\ge6\), hence \(k\ge6\), and at \(k=6\) a lone \(D_6\) with \(A\ge3675/64\); configurations retaining rank in the bulk (\(k_b>0\)) or containing Wahl points are not decided by the transferred inequalities once their aggregate budget passes (95.S); bilinear gluing can exclude low-rank Wahl configurations but is uniformly realizable at \(k\ge4t\) (98.W/98.V). Such a \(V\) gives a non-attained zero only if \(M\) has no Einstein metric; it does not supply one, and at \(\mathbb R^4/\mathbb Z_2\) points no Einstein metrics on \(M\) GH-converge to \(V\) (58.O). No such orbifold is known for any general-type \(X\) (A01 #867 reports none in its construction corpus either). A positivity theorem for \(0<k<A/3\) must therefore exclude, by one inequality, smooth Einstein metrics on \(M\), negative Einstein orbifolds that resolve or smooth to \(M\), and other concentrating near-Einstein sequences. Conversely, one such orbifold would give \(\alpha(M)=0\) for that \(M\) without deciding Problem 1.
5. *Analogue with a different supplier* [P]. For real-hyperbolic \(Y\), \(Y\#k\overline{\mathbb{CP}}^2\) carries no Einstein metric for any \(k\ge1\), by minimal-volume entropy and the degree-one pinch map (§3.3). Entropy is a supplier that does not pass through monopoles; for complex-hyperbolic (ball-quotient) hosts with the stated Einstein normalization, the volume-entropy route gives only \(\mathrm{Vol}\ge(64/81)\mathrm{Vol}(X)\) (§15) and does not close the open range.

**What a solution must control.** A proof of nonexistence for \(k<A/3\) must use information that sees individual exceptional classes on an Einstein metric: affine sign-averages of monopole classes stop at LeBrun's \(2/3\) threshold (§3.6), paired monopoles are blind to the individual class (§3.7), and the fixed-Kähler inequality \(C_+\ge A\) (Hodge index, §3.5) is false for unrestricted metrics by 59.KE, so it is not an open target. Nonexistence needs \(C_+>A-k\) at every metric, and a positive gap needs uniform separation from \(A-k\). (This corrects the open target listed in §20.7.) A construction would have to be a complete smooth Einstein metric on \(M\), not an orbifold limit.

### 24.2 Problem 2 (LeBrun 2004, §11): the exact value of \(P_*(M)\), matching lower bounds, and the geometric data deciding it

**Classical interval [I]:** \(8\pi^2\max\{0,k-A/3\}\le P_*(M)\le8\pi^2k\) (lower end \cite{lebrun2001ricci} Prop. 3.2, all \(b^+\); upper end Burns concentration). LeBrun's Theorem 4.3 there computes \(\inf\int|\mathrm{Ric}|^2=8\pi^2(A+k+4\ell)\), a different infimum; it does not give \(P_*\).

**Proved here.**
1. *The upper end is never sharp* [P]. \(P_*(M)\le8\pi^2k\,(1-\frac{s^2}{64}\varepsilon^2\log\frac1\varepsilon+C\varepsilon^2)<8\pi^2k\) for every fixed minimal \(X\) of general type and every fixed \(k\ge1\) (59.KE; KE canonical model, Kronheimer gluing with \(\varepsilon\) fixed before \(\lambda\)). The saving constant is not topology-uniform. The local price is read from \(R^+=W^++\frac s{12}I\). On every smooth bulk, \((P(\widetilde g)-P(g))/8\pi^2=1-x_0R^+_p(\zeta,\zeta)+O(x_0^{6/5})\) (Theorem F). If the bulk is \(P\)-critical on the insertion support, \(\mathrm{Ric}^\circ_p=0\), and \(\zeta\) is an \(R^+_p\)-eigenvector, then the optimized corrector gives \(1-x_0\mu_1+\frac{\Phi_{\rm opt}}2x_0^2\log\frac1{x_0}+O(x_0^2)\), with \(\Phi_{\rm opt}=-\mu_1(\mu_1-\mu_2-\mu_3)/2-(\mu_2-\mu_3)^2/2\) (57.Φ, 59.R). Otherwise the coefficient is \(\Phi(\mathrm{Rm}_p,\zeta,K)\).
2. *The Kähler category is exactly at the old upper end* [P]. For the fixed blow-up complex structure, \(\inf_{\rm K\ddot ahler}P=8\pi^2k\), not attained (Theorem \(K_\infty\), §13). Every metric with \(P<8\pi^2k\), and hence any smooth unrestricted minimizer if one exists, is non-Kähler for the prescribed \(J\). Other complex structures are not examined.
3. *Balanced families* [P]. On the ball-quotient cover families of Theorem 69.B, \(M=X_m\#8n\overline{\mathbb{CP}}^2\#7n(S^1\times S^3)\), \(h=36n/A_m\), with its preliminary-cover and packing hypotheses: \(\alpha/h\le C_c/(1+C_ch/4)\), \(C_c=3.99614465135\ldots<4\) (§5.3). This refutes the project's expectation of leading coefficient \(4\) on these families. The true leading constant is [O]; the inherited linear lower bound \(\alpha\ge ch\) holds under its original balanced-family hypotheses [I].
4. *α-form of the problem* [P]. \(\alpha=1-6\max\{0,\sup_{[g]:Y\ne0}d([g])/(P(\widehat g)+Y^2/4)\}\), \(d=8\pi^2\chi-\mathcal W\) (§1). In \(h\): \(h\ge1\Rightarrow\alpha=1\); \(\frac13\le h<1\Rightarrow\frac{4(3h-1)}{3h+5}\le\alpha\le1\), with \(\alpha<1\iff\inf\int|W^+|^2<2\pi^2(A-k)\) (§22.5, 24.0); \(0<h<\frac13\Rightarrow0\le\alpha<\frac{4h}{1+h}\).
5. *The intermediate band* [P]. On deep ball-quotient covers, \(\alpha<1\) for \(h<\frac13+\eta\beta_0\) (Theorem 74.W), strictly beyond the fixed-complex Kähler frontier \(h=\frac13\) (Prop. 74.K). With the capacity of a given manifold, \(\Theta_*(M)=\sup_{\widehat g}2\kappa(\widehat g)/A\) (not known to depend only on \(h\)), the band question is \(\alpha(M)<1\iff\Theta_*(M)>(3h-1)/2\) (§22.6; this corrects the notation \(\Theta_*(h)\) there). Open-range positivity is a joint realizability problem for \((\kappa,\upsilon)\), since \(\mathfrak p=k-\frac43\kappa+\frac13\upsilon\). An upper bound on \(\Theta_*\) alone does not encode separation from the Einstein ratio.
6. *Joint realizability* [I + P]. \(P_*=\inf_{(x,y)\in\mathcal C(M)}(2y+x/12-16\pi^2\chi)\) on \(\mathcal C(M)=\{(\int s^2,\int|W|^2)\}\) [I]; the α-problem needs the larger datum \((\mathcal W,Y,P(\widehat g))\) per conformal class (§1), so \(P\)- and α-minimizing sequences can choose different conformal classes (Steps 69–72).

**Also inherited [I].** \(\inf R=8\pi^2(A+k)\) and \(\inf\int s^2=32\pi^2A\); these separate infima cannot be subtracted to give \(P_*\). For \(P_*=0\), Anderson's selected sequence gives a compact Einstein orbifold, complete Einstein domains with collapsed exterior, or total collapse (59.Z [P*], §20.5); this is not transferred to normalized α-small sequences. Under their sign-family hypotheses, near-subunit metrics must carry torsion, Weyl departure, Yamabe excess and twist (Theorems N, K, Y, 63.T; constraints, not tariffs); the quadratic law 62.B remains [C].

**Open [O].** The exact value of \(P_*(M)\) for any single \(M\) in the family; at \(k=A/3\), positivity of \(P_*\) (Einstein nonexistence holds there, but the classical lower bound is \(0\)); the lower side for \(0<k<A/3\) (whether \(P_*>0\)); the frontier \(\Theta_*\) in \([\frac13,1)\); the leading constant on balanced families. In the analogue \(Y\#k\overline{\mathbb{CP}}^2\) with \(Y\) real-hyperbolic, \(\inf P=8\pi^2k\) and \(\alpha=4k/(k+6\chi(Y))\) for \(k\le2\chi(Y)\) are proved conditional on \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=\mathcal Y_{\rm hyp}\) (Theorem H, §3.4) — the only place where the matching lower bound is known, and there it is a Yamabe statement.

### 24.3 Problem 3 (LeBrun 2004, §11): a smooth global \(P\)-minimizer that is not Bach-flat

**Reduction [I].** If \(M\) carries neither Einstein nor scalar-flat metrics, every smooth global \(P\)-minimizer is non-Bach-flat (Prop. nonbach). Problem 3 is existential over all closed four-manifolds; the blow-up families below are candidate sources, on which it becomes a smooth-attainment problem.

**Candidate sources.**
- \(X\#k\overline{\mathbb{CP}}^2\) with \(k\ge A/3\): both exclusions hold. Einstein is excluded by LeBrun [I; \cite{lebrun2001ricci} Thm 3.3/Cor. 3.4, with the \(P\)-bound from Prop. 3.2, all \(b^+(X)\) including \(1\)]. Scalar-flat metrics are excluded via \(\mathcal Y<0\) [I, LeBrun 1999 Thm 2, all \(b^+\)]. Problem 3 for these \(M\) is exactly: *is \(P_*\) attained?* No attainment theorem exists [O]. Two facts constrain the answer: Burns concentration is not optimal (59.KE: \(P_*<8\pi^2k\)), so minimizing sequences cannot simply shed all classes into Burns bubbles; and, for non-fake-plane ball quotients under the hypotheses of §15, fewer than \(k\) exceptional ranks can escape into smooth bubbles [C]. For general \(b^+\ge2\) hosts, which need not be aspherical so that the Γ-vertex essentialness step is unavailable, the SW step requires Lemma 54.3 [P*] (one-sided PSC-neck vanishing, uncited) and then the charge argument bounds the total smooth-bubble \(b_2\), \(\sum_b[4(e_b-1)+4b_1+b_2]<k\), but identifying the bubble homology with the exceptional span needs further topology. Smooth bubble convergence of an actual minimizing sequence makes each bubble locally \(P\)-minimal and critical (compact replacement); the analytic input still missing is convergence and decay. 53.D–E give smooth negative-Yamabe bulk minimizers under the Anderson ledger, and 56.A gives conditional orbifold-category attainment. Neither alone gives attainment on \(M\).
- \(Y\#k\overline{\mathbb{CP}}^2\), \(Y\) real-hyperbolic: Einstein excluded for all \(k\) (§3.3). Scalar-flat exclusion [I, three cited links]: (a) no PSC: \cite{mantionegeographya} Proposition 2 (nonpositively curved \(\pi_1\)) and Lemma 2 (aspherical \(\pi_1\)), no spin assumption: an essential oriented 4-manifold with the fundamental group of a closed nonpositively curved or aspherical 4-manifold admits no PSC metric; for \(M=Y\#k\overline{\mathbb{CP}}^2\), \(\pi_1(M)=\pi_1(Y)\) and the classifying map factors through the degree-one pinch \(M\to Y=B\pi_1\), so \(f_*[M]=[Y]\ne0\) and \(M\) is essential (`Knowledge/objects/papers/Geography-of-4-manifolds-with-positive-scalar-curvature--ea1844e3f622--6263e9f8807e/object.md`). (b) Bourguignon: on a manifold admitting no PSC metric every scalar-flat metric is Ricci-flat (as recorded in the Kotschick–Wehrheim appendix of \cite{kotschick2004monopole}). (c) Cheeger–Gromoll: a closed manifold with \(\mathrm{Ric}\ge0\) has virtually abelian \(\pi_1\) (\cite{barbara2020fundamental}, Theorem 2.7). A cocompact lattice in \(\mathrm{Isom}(\mathbb H^4)\) is not virtually abelian, so \(M\) carries no scalar-flat metric. Under \(\mathcal Y=\mathcal Y_{\rm hyp}\), scalar-flat exclusion is immediate, and Theorem H gives \(P_*=8\pi^2k\), not attained [C]. These manifolds are then not Problem-3 examples. Burns sequences approach the value; for arbitrary minimizing sequences, Theorem H gives only asymptotic half-conformal flatness and Yamabe extremality.

**Conditional dichotomy at \(k=1\)** [C; Theorem 54.A with verifier corrections, §15–17, in the Step-87 Γ-vertex proof order: Lemma 54.3 and SW transfer through homotopy spheres are not used, and \(s_{g_0}<0\) follows from essentialness, Bourguignon and non-virtual-abelianness]. Let \(X\) be a ball quotient, not a fake projective plane, \(M=X\#\overline{\mathbb{CP}}^2\). Under Anderson's Theorem 4.10 for his perturbed functional and the hypotheses \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},\mathrm H_{\rm eq},\mathrm H_{\rm rem}\), in case (I) with trivial local groups and no collapse, Theorem 54.A produces a smooth constant-negative-scalar global \(P\)-minimizer \(g_0\) on \(V\), where \(M\cong V\#\Sigma\), \(\Sigma\) is a homotopy sphere and \(V\) is homeomorphic to \(M\), and
\[
g_0\ \text{is Einstein}\quad\text{or}\quad g_0\ \text{is a smooth non-Bach-flat global minimizer}.
\]
If all bubble caps are diffeomorphic to \(S^4\), there are no bubbles, \(V\cong M\), and \(P_*(M)\) is attained. Ball quotients have \(A=9\chi(\mathcal O_X)\ge9\), so \(k=1<A/3\) and the Einstein branch is Problem 1 in its open range. Thus, under these hypotheses plus the standard-cap condition, *a negative answer to Problem 1 on \(M\) gives a positive answer to Problem 3*. Without the cap condition, nonexistence on \(M\) does not exclude an Einstein metric on \(V\). The remaining configurations are [O]:
- collapse, including finite isotropy and classes split across interfaces;
- nontrivial-group orbifold configurations, using the §17 repairs: Prop. 55.3 only for simply connected regions, a coarse trichotomy, and a charge budget conditional on the \(L\)-space splitting input, with \(C_+(V)+w\ge A\) an exclusion target rather than an established reduction;
- exotic homotopy-sphere bubbles.

**The α-attainment questions (human functional; not Problem 3)** [P].
- \(\alpha=0\) attained \(\iff\) Einstein with \(\lambda\ne0\).
- \(2\chi=3|\tau|\): \(\alpha=1\) attained exactly by half-conformally-flat metrics with nonzero constant scalar curvature; realized on \(S^1\times S^3/\Gamma\), \(S^1\times_\phi H^3/\Gamma\), \(\#4\overline{\mathbb{CP}}^2\). Strict Hitchin–Thorpe failure (\(T_+<0\) or \(T_-<0\)): \(\alpha=1\), not attained (§22.4).
- On \(X\#A\overline{\mathbb{CP}}^2\) (\(T_+=0\)): \(\alpha=1\), attained iff an anti-self-dual metric with negative constant scalar curvature exists [O].
- Real-hyperbolic blow-ups, \(k<2\chi(Y)\): \(\alpha\) not attained [C, Theorem H].
- Every attained α-minimizer identified in this package is Bach-flat: either Einstein with \(\lambda\ne0\), or half-conformally-flat with nonzero constant scalar curvature. The package contains no attained example with \(0<\alpha<1\). Whether a non-Bach-flat global \(\mathscr D\)-minimizer exists, the α-analogue of Problem 3, is [O].

### 24.4 The common mechanism

**Topology fixes three references.** For \(\alpha\) the reference is \(8\pi^2\chi\): \(\mathscr D-1=[6(\mathcal W-8\pi^2\chi)+L_s]/R\), so \(\alpha<1\) exactly when some conformal class has Weyl energy below \(8\pi^2\chi\). For \(P\) the reference is the pair \((A,\{E_i\})\): \(C_+=A-k+\mathfrak p\), and the question is how much of the exceptional lattice can be carried below the charge \(1\) per class. For almost-Kähler torsion it is \(c_2(E)=5\chi+6\tau\): the number of torsion zeros forced on a closed almost-Kähler Einstein manifold (§23). Each reference is a characteristic number; no reference alone decides anything, because each is matched by a curvature integral that geometry can redistribute.

**Conformal geometry supplies the only saving channel.** For \(P\) and \(\alpha\) alike, the saving is Weyl deficit \(d=8\pi^2\chi-\mathcal W\), equivalently the capacity \(\kappa=\frac A2-\frac3{8\pi^2}\int|W^+|^2\) at a scalar \(-4\) representative: \(\mathfrak p=k-\frac43\kappa+\frac13\upsilon\). The value \(h=\frac13\) appears twice, from two different inequalities. LeBrun's \(C_+\ge2A/3\) gives \(\mathfrak p\ge k-A/3\), which vanishes at \(h=\frac13\). Fixed-complex Kähler geometry gives \(I_+\ge4\pi^2A/3\), hence \(d\le4\pi^2(A/3-k)\); this frontier is strict at each metric for \(k>0\) and is approached by Kähler recovery. KE metrics saturate the minimal-model scalar estimate \(\int s^2\ge32\pi^2A\) underlying the Kähler frontier. They do *not* saturate the combined estimate behind the \(P\)-bound: at KE, \(\int(s^2/24+2|W^+|^2)=4\pi^2A>\frac{8\pi^2}3A\), and its formal equality profile is the almost-Kähler profile of §3.7. N1's actual-field input pushes positive separation below \(\frac13\) on its supply class, and the certified non-Kähler cells push the \(\alpha<1\) frontier above \(\frac13\) (74.W). So \(\frac13\) is the meeting point of the classical monopole bound and fixed-complex Kähler geometry, not a frontier of \(\alpha\).

**Yamabe scale converts \(P\) into \(\alpha\).** On supply manifolds \(\alpha=\min\{1,\inf_{[g]}4\mathfrak p/(A+\mathfrak p+\upsilon)\}\). At fixed capacity \(\kappa\), the ratio \(F_\kappa(\upsilon)\) has \(F_\kappa'=4(A-3k+4\kappa)/[3(A+k-\frac43\kappa+\frac43\upsilon)^2]\), and \(F_\kappa<1\iff A-3k+4\kappa>0\). So in the subunit region more Yamabe excess *raises* the ratio toward \(1\). Since \(P\) and \(\alpha\) weight \((\kappa,\upsilon)\) differently, their optimal classes can differ. The scale also separates the two infima at degenerations. Ricci-flat bubbles, ALE resolutions and bounded-curvature collapse drive \(P\to0\) but give \(\alpha\to0\) only over a nonzero-scale Einstein bulk; for ALE resolution and Wahl smoothing the scalar-variance error is then automatically small (Lemma 86.S). MinVol \(=0\) gives \(P_*=0\) and \(\alpha=1\).

**Local models read the same \(R^+\) datum and set the price of topology.** A Burns bubble costs \(1-x_0R^+(\zeta,\zeta)\) at first order. Its second-order coefficient in the kernel is \(\Phi_{\rm opt}=-\Lambda^2/2+2\det(R^+|_{\zeta^\perp})\), the same invariant as Ozuch's second Eguchi–Hanson obstruction. An Eguchi–Hanson bubble costs \(\pi^2a^4|R^+\zeta|^2\) on the weighted gluing neighbourhoods of 61.EH. At a Wahl point the linear-tail interaction has no logarithm; the \(\lambda^4\) polarizability is uncomputed, and the established smoothing error is \(O(\lambda^2)\). Negative-KE backgrounds make the perpendicular direction first-order free and the second-order term negative, which is why \(P_*<8\pi^2k\). Exceptional topology is priced by curvature, not by its homology class. Eguchi–Hanson pairs carry two classes at zero cost through nontrivial links (lattice absorption).

**Three ends locate positivity and its proof obstacles.** Since every conformal class of \(M\) is negative and the Yamabe representative lowers \(P\) (66.Y), \(P_*\) may be computed on the constant-scalar slice, where \(p=q^2(1-\delta)^2+L\) with \(L\ge0\) and \(q^2=|a^-|^2\ge k\) for a best-sign class. A sequence with \(p\to0\) therefore has \(L\to0\) and \(|1-\delta|\le\sqrt{p/k}\to0\): it approaches the Einstein end in the integrated ledger sense. This is a necessary algebraic description, not a compactness theorem; a smooth noncollapsed limit would be Einstein (Problem 1), and otherwise the degenerations of 24.1(4) and 24.3 occur. The cscK end has \(p=q^2\ge k\), and an aligned sequence can take part only by also approaching \(\delta=1\). These two equality classes are where natural coercive estimates fail. Under the bounded-extension hypothesis, 66.R characterizes non-Einstein aligned equality structures (strictly almost-Kähler, \(J\)-invariant Ricci, Einstein–Maxwell/Blair–Ianus; with \(s<0\) this is the negative-Goldberg geometry of §23). Their existence on these blow-ups is not established; if they exist, they obstruct a universal \(L\ge c\,\delta\). The product saddles show that Kähler-end coercivity is not uniform across products of curves; they are not a zero-gap construction on \(M\). A positivity proof for \(0<k<A/3\) need not exclude these structures. It must prevent approach to \(p=0\) quantitatively, by an inequality that holds through them. Every proof that \(P_*>0\) contains a proof of Problem 1 in that range.

**Degeneration governs attainment.** \(\alpha=0\) is attained iff an Einstein metric with \(\lambda\ne0\) exists. \(\alpha=1\) is attained at \(2\chi=3|\tau|\) exactly by half-conformally-flat constant-nonzero-scalar metrics. The nonattained infima constructed in this package are approached by concentration (Burns, Eguchi–Hanson), orbifold absorption, long necks (the dumbbell) or collapse. The quoted limit theorems (Anderson, 59.Z, 54.A) organize attainment as the exclusion of these degenerations in turn, as in the \(k=1\) dichotomy.

**Orbifold absorption is priced exactly and is deficit-neutral.** Ricci-flat ALE resolution conserves the Weyl deficit (Gauss–Bonnet on the ALE space cancels the Euler increment) and preserves \(\mathscr D\) (86.S). For ball-quotient hosts, 87.O and 93.A give the full football law: \(d_{*,\rm orb}=4\pi^2(A/3-2m)\), \(P_{*,\rm orb}=16\pi^2m\), and \(\alpha_{\rm orb}=\min\{1,8m/(A+2m)\}\). The \(P\)-infimum is never attained, the defect infimum is nonattained except possibly on the wall \(2m=A/3\), and no fixed \(V_m\) carries an Einstein orbifold at any ratio. Thus ordinary paired-\(A_1\) absorption is excluded as a zero-gap architecture even inside the open range; the former condition \(2m<A/3\) was only necessary and is superseded. A different negative non-Kähler Einstein orbifold topology or singularity pattern could still absorb exceptional topology, and its optimized curvature data must be determined separately; no reduction to marked-cell infima is known. Over ball quotients, the same transfer combined with integral topology (95.S, 95.F, 96.Ş, 96.K) leaves exactly three singular sectors: full absorption through a Kronheimer \(D_{\ge6}\) filler (a pure existence problem for a prism-manifold complement and a negative Einstein orbifold metric), retained-rank/Wahl configurations (outside the class-sensitive reach of aggregate smooth transfer; bilinear gluing can obstruct at low rank but is uniformly realizable for \(k\ge4t\) by 98.W/98.V; next inputs are geometric realization, characteristic/spin\(^c\) refinements and APS/Dedekind, orbifold-monopole or type-T analysis), and non-Kähler Ricci-flat fillers (none supplied by the material read here). Smooth metrics can cross \(1/3\) through finite-scale interaction (74.W), so the orbifold value is not an upper bound for \(M\).

**The unsolved centre, stated plainly.** The complete problem for \(0<k<A/3\) is unresolved. N1 gives positive \(P_*\) and \(\alpha\) on its actual-supply window near \(\frac13\). For lower ratios there is no general positive-gap theorem, no zero-infimum construction on a fixed blow-up, and no decision on Einstein existence.
- *Lower side (the direction for continued research):* a global, metric-wise inequality that sees individual exceptional classes. It must be compatible with the certified sub-\(8\pi^2\) cells and with lattice absorption, must control the joint data \((\kappa,\upsilon)\) away from the Einstein ratio, and must hold through the aligned and cscK structures. A positivity theorem on a fixed \(X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\), must exclude simultaneously (i) a smooth Einstein metric, (ii) a negative Einstein orbifold of one of the remaining absorption topologies (ordinary paired-\(A_1\) footballs over ball quotients are excluded by 93.A; Kähler-filler full absorption needs a \(D_{\ge6}\) Kronheimer filler by 96.K), and (iii) every other concentrating, collapsing or near-Einstein sequence, or else fail exactly when (ii) exists. No local lemma, cell tariff, or orbifold-channel computation in this package supplies such an inequality; a route to it was not opened in the present loop.
- *Upper side:* one proposed mechanism is a diffuse non-Kähler multiclass geometry that removes an \(O(1)\) fraction of the host's \(W^+\)-energy per class; radial cells remove \(\le6\times10^{-5}\) of their footprint. Another is a negative-Einstein-constant orbifold or smoothing with the topology of \(M\), now necessarily involving singular/topological data other than ordinary \(X\#m(S^4/\mathbb Z_2)\) over a ball quotient.


