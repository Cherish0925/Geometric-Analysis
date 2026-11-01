# State of the Einstein-gap programme and of Problems 1–4 (front matter, Step 90; repaired through Step 99, synchronized through Step 108)

Session S1003A02. This is the entry point for a later Writing loop and for the End reading. It states, for the human
functional and for the four original problems (`Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/five_research_problems.tex`,
§§1–4), what is proved, with which inherited inputs, what is conditional on which named hypothesis, what is numerical,
and what the unresolved centre requires. Proofs and sources are in `workspace/notes/theorem_package_v1.md` (section
numbers below refer to it); the hypothesis ledger is `workspace/notes/step58_consolidated_hypothesis_ledger.md`.
Tags: **[I]** inherited (literature/corpus), **[P]** proved here and independently read, **[P*]** proved modulo a quoted
external theorem, **[C]** conditional on named hypotheses, **[N]** numerical, **[O]** open.

Notation. \(P=\int|\mathrm{Ric}^\circ|^2\), \(L_s=\int(s-\bar s)^2\), \(R=\int|\mathrm{Ric}|^2\),
\(\mathscr D(g)=\inf_{\lambda\ne0}\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)=4-(\int s)^2/(R\,V)=(4P+L_s)/R\) for \(R>0\); at a
Ricci-flat metric (\(R=0\)) the original definition gives \(\mathscr D=4\). \(\alpha(M)=\inf_g\mathscr D\),
\(P_*(M)=\inf_gP\). \(X\) minimal of general type, \(A=c_1^2(X)\), \(M=X\#k\overline{\mathbb{CP}}^2\), \(h=k/A\).

---

## 0. The human functional \(\alpha\)

- **Range and wall [P, §22.4].** \(\mathscr D-1=[6(\mathcal W-8\pi^2\chi)+L_s]/R\), hence \(0\le\alpha(M)\le1\) on every closed
  four-manifold (long round-\(S^4\) dumbbells give \(\mathscr D\to1\)), \(\alpha(M)<1\iff\inf\mathcal W<8\pi^2\chi\), and
  \(2\chi\le3|\tau|\Rightarrow\alpha=1\). \(\alpha=1\) is attained exactly by half-conformally-flat metrics of nonzero
  constant scalar curvature when \(2\chi=3|\tau|\). Ricci-flat metrics have \(\mathscr D=4\); \(K3\) and \(T^4\) have \(\alpha=1\).
- **Weyl-deficit form [P, §1, §22].** \(\alpha=1-6\sup(\{0\}\cup\{d/(Y^2/3-2d):d>0\})\) over conformal classes,
  \(d=8\pi^2\chi-\int|W|^2\).
- **Zero, attainment, existence [P, §22.4, L1].** \(\alpha=0\) is attained iff an Einstein metric with \(\lambda\ne0\) exists.
  For \(1\le k<A\) on \(M\): \(P_*=0\iff\alpha=0\) and \(P_*>0\iff\alpha>0\) (L3; equality of vanishing only).
- **Covers [P].** \(\mathscr D\) is invariant under finite covers; \(P\) scales by the degree.
- **Orbifold resolution [P, Lemma 86.S].** For orientation-matched equivariant ALE ends with derivative-controlled decay
  of order \(\tau>0\), cutoff radius \(\rho=\varepsilon^{\tau/(\tau+2)}\) gives \(O(\rho^4)\) convergence of
  \(V,\int s,\int s^2,R,P,L_s\). A nonzero-scale Einstein orbifold resolved by Ricci-flat ALE spaces or Wahl Milnor
  fibres (\(\tau=4\) with all derivatives: Gibbons–Hawking for \(A\)-type and Şuvaina spaces \cite{suvaina2011ale};
  Bando–Kasue–Nakajima for Kronheimer \(D/E\) spaces \cite{lidimensional}) has \(\alpha=0\). A Ricci-flat bulk gives only \(P_*=0\) (glued family
  \(\mathscr D\to4\)). On a negative-Yamabe target such as \(M\), \(-\|s^-\|_2\le Y\le-4\pi\sqrt{2A}\) forces any absorbing
  Einstein orbifold in these constructions to have \(\lambda<0\).
- **Examples of \(\alpha=0\) without known attainment [P].** \(\mathbb{CP}^2\#\mathbb{CP}^2\) (round \(S^4/\pm1\) with two EH);
  resolutions of spherical/hyperbolic orbifolds with \(\mathbb Z_2\) points (Prop. 58.O, with Ozuch's theorem excluding
  Einstein sequences converging to the orbifold); canonical-model resolutions of negative KE orbifolds (§3.1).

## 1. Problem 1 — Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\)

- **Settled [I].** No Einstein metric for \(k\ge A/3\) (\cite{lebrun2001ricci} Thm 3.3/Cor. 3.4, all \(b^+\)); none on the
  N1 actual-supply window \((\frac13-\varepsilon)A<k<\frac A3\) (project corpus). Precisely: for every metric on which the
  actual class/field supply of N1 is available, \(J+(\frac13-\frac kA)_+\ge\varepsilon\); with
  \(j_0=\varepsilon-(\frac13-\frac kA)_+>0\) on the window, the human defect dominates \(J\), so \(\alpha\ge j_0\), and
  \(P\ge8\pi^2j_0A/(4-j_0)\) (Yamabe bridge \(\mathscr D(\widehat g)=16P/(4P+Y^2)\), \(Y^2\ge32\pi^2A\)). This is metric-wise only
  where the actual supply is given; it is not a theorem for every general-type blow-up.
- **Proved here [P].** Problem 1 is the attainment of the value \(0\) (L1). For \(1\le k<A/3\):
  \(0\le\alpha<4k/(A+k)\) (69.KE) and \(P_*<8\pi^2k\) (59.KE, Burns second-order saving \(\Phi=-s^2/32\) on negative KE
  backgrounds); the unit per-class tariff is false. Necessary conditions at an Einstein metric: exact harmonic torsion
  part \(\mathsf H^-(t_J^-)=2\pi h_a^-\), \(q^2\ge k\); only the Einstein end \(\delta=1,L=0\) of the flux ledger
  \(p=q^2(1-\delta)^2+L\) carries \(p\to0\). Real-hyperbolic analogue: \(Y\#k\overline{\mathbb{CP}}^2\) has no Einstein metric
  for any \(k\ge1\) (entropy, §3.3).
- **Paired-\(A_1\) orbifold channel solved [P, 87.O and 93.A].** For a ball quotient, \(V_m=X\#m(S^4/\mathbb Z_2)\), and \(k=2m\),
  \[
  d_{*,\rm orb}=4\pi^2(A/3-k),\qquad P_{*,\rm orb}=8\pi^2k,\qquad
  \alpha_{\rm orb}=\min\{1,4k/(A+k)\}.
  \]
  The \(P\)-infimum is never attained; \(\alpha_{\rm orb}\) is nonattained except possibly at \(k=A/3\), where attainment is exactly a constant-negative-scalar half-conformally-flat orbifold question. No \(V_m\) is Einstein for any \(m>0\), so this absorption topology is eliminated even in \(0<k<A/3\). Other orbifold topologies need separate information.
- **Kähler-filler absorption over ball quotients [P as necessary conditions; 95.S, 95.F, 96.Ş, 96.K, package §22.6(7)].**
  For a compact negative Einstein orbifold with spherical-space-form points resolved by Kähler Ricci-flat ALE fillers
  (Kronheimer, or Şuvaina quotients including minimal resolutions of singular invariant fibres; complete by Şuvaina's
  classification) to \(X\#k\overline{\mathbb{CP}}^2\), orientation-preservingly:
  host-general envelope \(9C_-+2C_++42k+12(3c_2-c_1^2)\ge0\); ball-quotient budget \(S_{\rm cx}+\frac29S_{\rm rev}\le k/6+k_b\);
  \(H_2(N)\cong A_{d-1}(-1)\) for every non-simply-connected Kähler filler; and full absorption (\(k_b=0\)) needs a Kronheimer \(D_{a\ge6}\) filler, so \(k\ge6\), with a
  lone \(D_6\) and \(A\ge3675/64\) at \(k=6\). Retained-rank and Wahl configurations are outside the class-sensitive reach of
  this transfer. Their integral bilinear gluing is settled by 98.W/98.V as repaired at Step 99 [P; `notes/step99_independent_verification_and_repairs.md`]:
  over an aspherical host with torsion-free \(\pi_1(X)\) the Wahl boundary maps into the complement vanish (Frattini
  argument), the complement lattice has index exactly \(\prod n_j\), its discriminant form is the lens linking form with
  \(U/L\) the specified metabolizer (no torsion-free-\(H_1(X)\) assumption; the torsion block is eliminated from the pair
  sequence), and asphericity splits \(L=Q_X\oplus L_0\) with \(L_0\subset-I_k\). Hence low-rank bilinear obstructions exist
  (e.g. complex-oriented \(B_{2,1}\) needs norm \(3\bmod4\), excluding ranks one and two), while every collection of \(t\) Wahl
  points is realizable once \(k\ge4t\) (Lagrange; four is sharp uniformly, \((n,a,\sigma)=(8,1,-1)\)). Compatible
  discriminant gluing already makes the minimal-resolution chain primitive, recovering the \(k=1\) parity law of Theorem
  55.5, so the abstract second filling is not an independent condition. What remains is geometric realization (embedded
  balls/plumbings, prescribed complement, degree-one map), characteristic/spin\(^c\) refinement, and singular curvature data.
  (Independently read by Agent4 at Step 101; no repair needed.)
- **Actual Wahl orbifolds and their class-blindness [P, Step 102; `notes/step102_wahl_orbifold_realization_and_K2_invariance.md`;
  embeddings quoted from Park–Park–Shin/Khodorovskiy \cite{parksmoothly}].** Theorem 102.R: for \(k\ge\sum\kappa(n_j)\)
  (\(\kappa=4\) for \(n\ge3\), \(3\) for \(n=2\)), \(M\) contains disjoint embedded \(B_{n_j,1}\) (tube four exceptional spheres to a
  \((-4)\)-sphere, PPS Prop. 4.4; even \(n\) via \(B_{2,1}\#\overline{\mathbb{CP}}^2\subset V_{-3}\#\overline{\mathbb{CP}}^2\)); coning gives an orbifold
  \(V\) with \(\frac1{n_j^2}(1,n_j-1)\) points, degree-one \(V\to X\), \(\pi_1(V)=\pi_1(X)\), resolution
  \(X\#(k+\sum(n_j-1))\overline{\mathbb{CP}}^2\), and the 98.W lattice data. One odd point at \(k=4\) lies in \(0<k<A/3\) iff \(A>12\).
  Exact invariants: \(s(n-1,n^2)=(n^2-1)/(6n^2)\), \(\chi_{\rm orb}=\chi(M)-\sum(1-n_j^{-2})\),
  \(\tau_{\rm orb}=\tau(M)+\frac23\sum(1-n_j^{-2})\), so \(2\chi_{\rm orb}+3\tau_{\rm orb}=A-k\) and
  \(2\chi_{\rm orb}-3\tau_{\rm orb}=T_-(M)-4\sum(1-n_j^{-2})\). Proposition 102.K: via Şuvaina \(d=1\) filler transfer
  (86.S), every orbifold metric has \(\int(s^-)^2\ge32\pi^2A\) and \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2A\); an Einstein orbifold
  metric obeys exactly the smooth constraints \(k\le A/3\) and the mixed edge, the \(W^-\)-side term being slack; no
   Kähler–Einstein orbifold metric exists on \(V\) (it would have \(\int s^2=32\pi^2(A-k)\)). Orbifold spin\(^c\) structures form
   an \(H^2(W)\)-torsor containing \(H^2(M)\) with cokernel \(\oplus\mathbb Z_{n_j}\). Step 103 independently verified
   102.R and 102.K(a)–(c), including orientation, resolution type and defect sign; the cohomology sequence here stands,
   but the quoted orbifold–resolution SW correspondence is conditional and is not used in the class-blindness theorem.
   Hence curvature-integral and SW/Dedekind inequalities cannot decide the Wahl sector; whether some \(V\) with \(A>3k\)
   carries a (necessarily non-Kähler) negative Einstein orbifold metric — which would give \(\alpha(M)=0\) by 86.S — is a
   pure existence problem. At every \(n\ge3\) Wahl point, isotropy forces both Weyl blocks to have a repeated eigenvalue
   (Lemma 103.I), but does not locally obstruct an Einstein germ. CH/Kähler locally symmetric type is excluded;
   real-hyperbolic type is excluded whenever
   \(\tau_{\rm orb}=A/9-k+\frac23\sum(1-n_j^{-2})\ne0\). The stronger blanket positivity with \(A/3\) is false.
   **Step-105 corrections (binding; `notes/step105_cusp_channel_restored_and_cap_charge_theorem.md` §0).** Props.
   104.C/104.F are withdrawn and 104.M is downgraded to a route (Question 105.M: fixed supplied basic class, global
   \(L^4\)/\(F_A\) bounds, equivariant removability and holonomy identification all to be proved). No \(j=0\) supplied field
   is identified; the Step-104 'no extending sign' rows reflect a misidentified boundary map. No-\(\mathbb Z^2\) in
   \(\Gamma\) excludes only injective cusp groups; cusps and collapse remain. The second alternative has **three**
   subchannels; Wahl and \(D_{\ge6}\) are sufficient routes, not an exhaustive reduction.
- **Cap-charge law [P under hypotheses (E); Step 105, independently repaired Step 106].** If \(\mathscr D(g_i)\to0\) with \(C^2_{\rm loc}\) convergence to a finite-volume Einstein domain \(\Omega\), no volume loss, and stable nested caps \(C_j\) (Theorem 105.Q), then \(c_j=\lim C_+(C_j)\ge0\) is pure \(W^+\)-concentration, \(C_+(\Omega)=A-k-\sum c_j\), and LeBrun transfers as \(9k+8\sum c_j\le3A\) (Cor. 105.L). For a cap meeting several ends, (E) gives the limiting **sum** of incident \(\mathcal Q_+\) charges; individual limits need separate end asymptotics. Scalar-cap vanishing uses the total tail volume and ordered limits. For Dai–Wei circle-fibred cusps \(\mathcal Q_+^\infty=-e+3\,\mathrm{sign}\,e\); an \(S^3\)-Hopf cap carrying \(r\) classes has \(c_+=4-r\) (Taub-bolt chirality; the other chirality is impossible), so \(r\le4\). If there are \(N\) exceptional caps and \(B\) additional charge-four ball caps, \(k+32N+32B\le3A\); singleton caps are excluded for \(k>A/11\). A four-class cap has \(c_+=0\), but \(c_-=20\) and \(\int|W^-|^2\to40\pi^2\): it is invisible only to the scalar/\(W^+\) mixed estimate. Orientation is fixed by Taub–NUT (both), Taub-bolt and all \(A_{m-1}\) ALF models (`data/step105/cap_charge_check.json`). Spirit's \(A/12\) omitted the cap's \(W^+\) energy.
- **Conditional [C, 54.A].** At \(k=1\) over a non-fake-plane ball quotient, under (I),
  \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},\mathrm H_{\rm eq},\mathrm H_{\rm rem}\), no collapse and standard
  caps, a smooth global \(P\)-minimizer with \(s<0\) exists and is Einstein or non-Bach-flat.
- **Open [O].** \(1\le k\le(\frac13-\varepsilon)A\) outside the supply window: existence, nonexistence, and positivity of
  the gap.

## 2. Problem 2 — the exact value of \(P_*\) (equivalently of \(\inf\int|\mathrm{Rm}|^2\))

- **Classical interval [I].** \(8\pi^2\max\{0,k-A/3\}\le P_*\le8\pi^2k\) (\cite{lebrun2001ricci} Prop. 3.2; Burns).
- **Proved here [P].** Upper end never sharp (59.KE, rate \(1-\frac{s^2}{64}\varepsilon^2\log\frac1\varepsilon\)); local
  price read from \(R^+=W^++\frac s{12}\) (Theorem F first order; 59.R second order on \(P\)-critical backgrounds; when also
  \(\mathrm{Ric}^\circ_p=0\) and \(\zeta\) is an \(R^+_p\)-eigenvector,
  \(\Phi_{\rm opt}=-\frac12\mu_1(\mu_1-\mu_2-\mu_3)-\frac12(\mu_2-\mu_3)^2\); otherwise the coefficient is \(\Phi(\mathrm{Rm}_p,\zeta,K)\)); Eguchi–Hanson rate \(\pi^2a^4|R^+\zeta|^2\) on
  weighted neighbourhoods (61.EH; upper side [P*] via Ozuch). Fixed-complex Kähler infimum exactly \(8\pi^2k\), not
  attained (\(K_\infty\)). Balanced ball-quotient families: \(\alpha/h\le C_c/(1+C_ch/4)\), \(C_c=3.99614\ldots<4\) (69.B,
  with its packing hypotheses). Band: \(\frac{4(3h-1)}{3h+5}\le\alpha\le1\) for \(\frac13\le h<1\); \(\alpha<1\) for
  \(h<\frac13+\eta\beta_0\) on deep covers (74.W; certified \(\eta_{128}\approx0.0751342\), realized gain packing-limited).
- **Numerical [N].** Certified perpendicular CH cell \(P/8\pi^2\in[0.995662732753,0.995662732772]\) (Arb).
- **Conditional [C].** Real-hyperbolic analogue: \(P_*=8\pi^2k\), \(\alpha=4k/(k+6\chi(Y))\) for \(k\le2\chi(Y)\), given
  \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=\mathcal Y_{\rm hyp}\) (Theorem H) — the only matching lower bound known.
- **Open [O].** \(P_*\) for any single \(M\); positivity at \(k=A/3\) and below; the frontier \(\Theta_*(M)\) on
  \([\frac13,1)\); the leading constant on balanced families.

## 3. Problem 3 — a smooth non-Bach-flat global \(P\)-minimizer

- **Reduction [I].** On a manifold without Einstein and scalar-flat metrics every smooth global \(P\)-minimizer is
  non-Bach-flat. For \(M\) with \(k\ge A/3\) Problem 3 is exactly smooth attainment of \(P_*\).
- **Proved/conditional.** 54.A (above) gives the dichotomy Einstein / non-Bach-flat at \(k=1\) [C]; the Γ-vertex proof uses
  essentialness (\cite{mantionegeographya}), Bourguignon and virtual abelianness instead of an SW transfer [P given the
  ledger]. For \(k\ge1\) over ball quotients fewer than \(k\) exceptional ranks escape into smooth bubbles [C]. Orbifold
  attainment 56.A [C; additionally one-sided SW\(_L\), (N\(_0\)), orbifold regularity].
- **Open [O].** Any unconditional smooth attainment; collapse with finite isotropy; nontrivial-group orbifold limits;
  exotic homotopy-sphere caps. The \(\alpha\)-analogue (a non-Bach-flat \(\mathscr D\)-minimizer) is open; every attained
  \(\alpha\)-minimizer known is Bach-flat.

## 4. Problem 4 — closed negative Goldberg in dimension four

- **Inherited [I].** Sekigawa for \(s\ge0\).
- **Elementary [P].** The torsion \(\nabla\Omega\) of an almost-Kähler structure is a section of
  \(E=\Lambda^{0,2}\otimes T^{1,0}\cong K^{-1}\otimes T^{1,0}\), and \(c_2(E)=c_2+2c_1^2=\chi+2(2\chi+3\tau)=5\chi+6\tau\). On a
  closed Einstein four-manifold with \(s\ne0\), Hitchin–Thorpe gives \(2\chi\ge3|\tau|\) and \(\chi>0\), so
  \(5\chi+6\tau\ge\chi>0\); hence the torsion of a closed negative AKE structure must vanish somewhere; \(c_2(E)\) is the
  localized Euler class of the torsion section, and when the zeros are isolated their local indices sum to
  \(5\chi+6\tau\) (LeBrun 2005 Prop. 2.4 gives a second proof that a torsion zero exists). The vanishing of \(5\chi+6\tau\) for nowhere-vanishing Nijenhuis tensor is the elementary result recorded as
  Apostolov–Armstrong–Drăghici Lemma 2 (attributed there to Armstrong 1997 and LeBrun); Armstrong 2002 is a distinct
  \(W^+\)-eigenform rigidity statement, known here only through metadata and abstract, and is not used.
- **Proved here [P].** Complete noncompact strict AKE pair on \(\mathbb R^4\) (\(\mathrm{Ric}=-3g\), \(W^-=0\)) with nonvanishing
  torsion (answers Fino's question on non-invariant, non-Ricci-flat noncompact strict AKE metrics; no historical-first
  assertion; says nothing on closed manifolds). Half-twistor first-order system
  (75.H); smooth Chern–Weil densities have no sign. At nondegenerate zeros: cone \(\|A\|^2=\|S\|^2+8|c|^2\), index \(+1\)
  (76.Z). Scalar compatibility operator \(\mathcal P(E)=J^i{}_aJ^j{}_b\partial_a\partial_bE_{ij}-\frac12\Delta\operatorname{tr}E\),
  \(\operatorname{coker}L_d=\text{Bianchi}\oplus\mathcal P\) at \(d=4,6,8\) (84.P).
- **Numerical [N].** Conjecture 79.C (no nondegenerate zeros) refuted at order 6; a real formal AKE germ with a
  nondegenerate index-\(+1\) zero exists through order 8 (two independent systems, relative residual \(\sim10^{-15}\));
  no intrinsic scalar compatibility class survives through order 8 (peer #869). Not exact, not convergent.
- **Open [O].** The closed problem. Local formal prolongation gives no obstruction; a proof needs zero-sensitive global
  input (degree/continuation, opposite-orientation \(W^-\) information, or a global identity).
- **Inherited Einstein curvature relation [I/P, Step 99].** For every Einstein metric, with
  \(T:=\int(s^2/24-|W^+|^2)\), Gauss–Bonnet and signature give \(s^2V=32\pi^2(2\chi+3\tau)+16T\); on
  \(M=X\#k\overline{\mathbb{CP}}^2\) (\(2\chi+3\tau=A-k\)) LeBrun's scalar estimate \(\int s^2\ge32\pi^2A\) \cite{lebrun2001ricci}
  then gives \(T\ge2\pi^2k\). The exceptional-curve inequality
  \(\int_C|\nabla\omega|^2\ge8\pi c_1\!\cdot C+|s|\mathrm{Area}(C)\) is LeBrun 2005 Corollary 3.2 rearranged (\(s^*=s+|\nabla\omega|^2\));
  Corollary 3.6 supplies, for the fixed almost-Kähler metric, a possibly singular or disconnected \(J\)-holomorphic cycle
  with \(c_1\cdot C=1\), not necessarily an embedded exceptional sphere \cite{lebruneinsteine} [I].
- **\(D=T_{AK}\) on closed AKE Einstein metrics [P*, read by Agent4 at Step 101; A01 Steps 77/83, peer #879].** With the
  Kim–Blair canonical curvature \(\gamma^+=\sqrt2\eta+(s/4+q/8)\omega\), \(|\gamma^-|^2=q^2/32\) (conventions
  \(W^+=[[r,\eta^*],[\eta,-r/2+V]]\), \(r=s/6+q/4\)), Chern–Weil gives \(8\pi^2c_1^2=s^2V/4-|s|Q/4+4\int|\eta|^2\); the
  AAD/LeBrun balance \(|s|Q/16=\int|\eta|^2+T_{AK}\), \(T_{AK}=\int(\operatorname{tr}V^2+3q^2/32)\) (quoted, the [*] input) yields
  \(s^2V=32\pi^2c_1^2+16T_{AK}\); comparing with the inherited relation above, \(D:=\int(s^2/24-|W^+|^2)=T_{AK}\). Hence
  \(T_{AK}\ge2\pi^2k\) on \(X\#k\overline{\mathbb{CP}}^2\) is exactly LeBrun's scalar estimate rewritten and carries no Goldberg
  information. The canonical-cycle identity \(T_{AK}-\int|\eta|^2=2\pi\int_T|a^\perp|^2\) remains A01's and unused; the
  regularized (\(q+\varepsilon\)) scalar transport family has a null direction (A01 Step 82) and is not duplicated here.
- **Exact AKE degenerations [P at exact scope, A01 Theorem 83.5, read by Agent4 at Step 101].** For a sequence of closed
  AKE Einstein metrics with fixed \(s=s_0<0\), noncollapsed and of bounded diameter, the forms extend across the orbifold
  points of the limit; deficit transfer gives \(D(V)=\lim D(g_i)+m_W\) and torsion splitting gives
  \(\lim T_{AK}(g_i)=T_{AK}(V)+m_T\) with \(m_W,m_T\ge0\); \(D=T_{AK}\) on both sides forces \(m_W=m_T=0\). Every bubble is
  Ricci-flat with \(W^+=0\) and parallel self-dual form, i.e. an orientation-matched Kähler Ricci-flat ALE filler (the class
  of 96.Ş/96.K). Scope: sequences of exact Einstein metrics only (Q4/moduli), not the near-Einstein sequences defining
  \(\alpha\); \(W^-\)-concentration is not excluded; collapse and diameter divergence are open.
- **Mixed Einstein edge [I, LeBrun's mixed estimate at an Einstein metric; Step 93 §4 with \(C_\pm=0\), \(k_b=k\)].** Every
  Einstein metric (smooth, or orbifold transferring to \(M\)) on \(X\#k\overline{\mathbb{CP}}^2\) with \(0<k<A/3\) has
  \(D=T\ge4\pi^2k+\frac{8\pi^2A}9(1-\sqrt{1-3k/A})^2\) (exact check `data/step102/mixed_edge_check.json`); the nominal
  \(4\pi^2k\) endpoint is excluded.

## 5. What remains unsolved, why the attempts stopped, and where the difficulty lies

### 5.1 Problem 1 (Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\), outside the N1 supply window)

**Unsolved.** Whether \(M\) carries an Einstein metric; equivalently whether \(\alpha(M)=0\) is attained; and whether
\(\alpha(M)>0\) (equivalently \(P_*(M)>0\)). On a fixed \(M\) three outcomes remain possible: (a) a positive gap; (b) a
smooth negative Einstein metric; (c) a zero gap without attainment, through a negative non-Kähler Einstein orbifold
that resolves or smooths to \(M\), or through another concentrating or collapsing near-Einstein sequence.

**Why the attempts stopped — one common root.** Every global tool available on these manifolds reads aggregate data.
LeBrun's Seiberg–Witten estimates give \(C_+\ge 2A/3\), a statement about \(A\) and \(k\) only; Gauss–Bonnet and the
signature formula see \(\chi\) and \(\tau\); the Yamabe invariant is \(-4\pi\sqrt{2A}\), independent of \(k\). At an Einstein
metric these combine to \(k<A/3\), and nothing more, because a gap below \(A/3\) is a statement about the individual
exceptional classes. Each attempt in this loop to extract class-sensitive information failed for an identified reason:
- *Local tariffs* (one unit \(8\pi^2\) per class) are false: Burns insertion in a kernel direction of a negative KE metric
  saves at second order (59.KE, \(\Phi=-s^2/32\)), and certified non-Kähler cells cost \(<8\pi^2\) (Arb enclosure
  \(0.99566\ldots\)). Any lower bound must accommodate these.
- *Affine averaging of monopole classes* over sign choices cannot beat LeBrun's \(2/3\): the full-sign Weitzenböck/Walsh
  identities leave only a shallow amplitude band, and the optimization over affine combinations is exactly saturated.
- *Paired monopoles* remember the classes algebraically but not metrically: the relative phase unwinds through the
  second spinor component, and tube scaling makes the relative-rotation cost vanish.
- *Almost-Kähler twist and Chern flux*: small \(P\) controls only the harmonic projection of the twist, \(\mathsf H^-(t_J^-)\),
  not its exact part; algebraic co-rotation is insufficient, and the missing datum is differential transport through
  \(\delta W^+\) and the Cotton tensor.
- *Orbifold transfer (Steps 93–96)*, the first global estimate that bypasses local decomposition: resolve an orbifold
  metric, apply the smooth estimates on \(M\), and pull them back to the whole singular bulk. It settles paired-\(A_1\)
  footballs completely (93.A) and forces Kähler-filler full absorption over a ball quotient to contain a Kronheimer
  \(D_{a\ge6}\) filler (96.K). But it reads only \(\chi(N)-1/|\Gamma|\) and \(A\) for each filler, so it has its own exact
  blind spot (95.S): every exceptional rank the bulk retains (\(k_b>0\)) buys one unit of slack, and once the aggregate
  budget passes, the inequalities carry no class placement, linking, or singular monopole data. Wahl balls carry no
  rank and live in that blind spot.

**Where the difficulty lies, and what to attack next.** A positivity theorem must be a metric-wise inequality that sees
individual classes, is compatible with the certified cells, holds through the aligned (strictly almost-Kähler,
\(J\)-invariant Ricci, Einstein–Maxwell/Blair–Ianus) and cscK structures where natural coercive estimates degenerate, and
separates \((\kappa,\upsilon)\) from \(\frac43\kappa-\frac13\upsilon=k\). The two coercivity-degenerate classes are exactly where
every natural estimate fails, so the inequality must hold quantitatively through them rather than exclude them. The
surviving singular routes need different inputs: (i) \(D_{\ge6}\) full absorption is an existence problem — a compact
complement of a prism-manifold plumbing with compatible linking in the index-\(2^q\) gluing, and a negative Einstein
orbifold metric on it; (ii) retained-rank and Wahl configurations need singular information. Their integral bilinear gluing
is now settled (98.W/98.V as repaired at Step 99: index exactly \(\prod n_j\), discriminant = lens linking form with the
specified metabolizer, no torsion-free-\(H_1(X)\) assumption, \(L=Q_X\oplus L_0\), low-rank obstructions, uniform realization
for \(k\ge4t\), and the abstract primitive resolution chain implied by compatible gluing). What remains is geometric
realization (embedded Wahl balls or plumbings with the prescribed complement and degree-one map),
characteristic/spin\(^c\) refinement (\(w_2|_{B_j}\) for even \(n_j\)), and then
APS/Dedekind terms coupled to a second global identity, orbifold Seiberg–Witten supply, or local analysis at type-T
points; (iii) non-Kähler Ricci-flat ALE fillers, none of which is supplied by the material read here. On the smooth side, the most specific open object is a quantitative control of the *exact* part of the
almost-Kähler twist for an individual best-sign class, or the density-free O10 actual-field endpoint, which would extend
the N1 mechanism below its window.

### 5.2 Problem 2 (the exact value of \(P_*\))

**Unsolved.** \(P_*(M)\) for any single \(M\); whether \(P_*>0\) at \(k\le A/3\); the frontier \(\Theta_*\) on \([\frac13,1)\); the
leading constant on balanced families.

**Why.** The only lower bound is the classical \(8\pi^2(k-A/3)_+\), again aggregate. Each refinement of the upper side
(Burns second order, Eguchi–Hanson obstruction, certified cells, 74.W packing) lowers it without a matching lower side;
separate infima (\(\inf\int s^2\), \(\inf R\)) cannot be subtracted; and positivity below \(A/3\) contains Problem 1. The only
manifolds where a matching bound is known are the real-hyperbolic blow-ups, and there it is conditional on a Yamabe
value (Theorem H). In the complex-hyperbolic case the Yamabe value is known (\(-4\pi\sqrt{2A}\), LeBrun) and yields only
the aggregate bound \(8\pi^2(k-A/3)_+\), because the host's self-dual Weyl energy can be redistributed.

**Where the difficulty lies.** The joint realizable set of \((\int s^2,\int|W^\pm|^2)\), or of \((\kappa,\upsilon)\), under all
metrics including concentrating ones. What is missing is an anti-self-dual Weyl-capacity bound: an upper bound on
\(\kappa=\frac A2-\frac3{8\pi^2}\int|W^+|^2\) in terms of the Yamabe excess \(\upsilon\) (the efficiency threshold is
\(\kappa/\upsilon>\frac14\)). The second-order Burns coefficient on non-\(P\)-critical backgrounds and batch gluing at fixed
density are the concrete open pieces on the upper side.

### 5.3 Problem 3 (a smooth global \(P\)-minimizer that is not Bach-flat)

**Unsolved.** No unconditional smooth attainment of \(P_*\) is known on any candidate.

**Why.** The minimizing route runs through Anderson's decomposition, whose passage from a minimizing sequence to a smooth
bulk with controlled bubbles needs analytic inputs not available for the fourth-order problem from \(L^2\) curvature alone
(\(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},\mathrm H_{\rm eq},\mathrm H_{\rm rem}\)). Ekeland and flow selections were
withdrawn because collapsed data give no uniform own-scale lifetime. Under those inputs, the \(k=1\) ball-quotient
theorem (54.A, Γ-vertex proof) reduces Problem 3 on \(M\) to a negative answer to Problem 1 there, if bubble caps are
standard.

**Where the difficulty lies.** Bubble-scale convergence and derivative decay for an actual minimizing sequence; collapse
with finite isotropy; nontrivial-group orbifold limits; exotic homotopy-sphere caps. For \(k\ge2\), strict subadditivity
\(P_*(M_k)<P_*(M_{k-m})+8\pi^2m\) at bulk minimizers is the additional input.

### 5.4 Problem 4 (closed negative Goldberg in dimension four)

**Unsolved.** Whether a closed almost-Kähler Einstein four-manifold with \(s<0\) is Kähler.

**Why.** The torsion must vanish somewhere (\(c_2(E)=5\chi+6\tau\ge\chi>0\)), but every local tool is silent there: at a
nondegenerate zero the index is \(+1\) and real formal AKE germs exist through order eight; the scalar compatibility
operator \(\mathcal P\) leaves no intrinsic class through order eight; smooth Chern–Weil densities have no sign (the strict
noncompact example has positive density); and the refined Bochner identity has a zeroth-order term of the wrong sign
when \(s<0\).

**Where the difficulty lies.** The problem needs zero-sensitive global input: a degree or continuation argument that
counts the forced zeros (localized Euler class \(5\chi+6\tau\); if zeros are isolated and nondegenerate, \(5\chi+6\tau\) of index \(+1\)) against a global identity that localizes at zeros, information
from the opposite orientation (\(W^-\)), or the primary text of Armstrong 2002 to see whether its \(W^+\)-eigenform rigidity
can be entered from the zero set.

### 5.5 O10

The density-free actual-field endpoint (constraints from fields degenerating jointly with the exterior, or a closed-manifold
escape) is open; finite-density alignment and the \(\beta\to\infty\) necessary asymptotics are the available results.

## 6. State at the close of Discovery loop 1 (Step 100; cap pause, centre open)

**Proved in Steps 93–99 and how each was read.**
- 93.A (paired-\(A_1\) transfer over ball quotients: \(P_{*,\rm orb}(V_m)=8\pi^2k\), \(\alpha_{\rm orb}=\min\{1,4k/(A+k)\}\),
  \(P\)-infimum never attained, no \(V_m\) Einstein for \(m>0\)): the theorem originated in A01 Step 74; A02 Agent4 verified it
  with two TTCS verifiers at Step 93 and added the nonattainment proof there (that addition was checked only by TTCS in
  the Step that wrote it).
- 95.S/95.F (host-general envelope \(9C_-+2C_++42k+12(3c_2-c_1^2)\ge0\), diagonal root-lattice classification, \(D\)-block
  thresholds): written by Agent3 at Step 95 with exact scripts, an independent certificate checker and TTCS; read
  again by Agent4 at Step 97.
- 96.Ş/96.K (Şuvaina filler lattice \(A_{d-1}(-1)\), \(H_1=\mathbb Z_n\); full Kähler-filler absorption needs a Kronheimer
  \(D_{a\ge6}\), \(k\ge6\), lone \(D_6\) with \(A\ge3675/64\) at \(k=6\)): written by Agent2 at Step 96; read by Agent4 at Step 97
  (scope gap found) and Step 99 (lift argument repaired).
- 98.W/98.V (Wahl integral gluing): written by Agent2 at Step 98; read by Agent4 at Step 99, who also strengthened it
  (torsion-block elimination, \(L=Q_X\oplus L_0\), \(k\ge4t\) with low-rank obstructions, implied resolution-chain
  primitivity). The Step-99 strengthenings were checked only by TTCS in Step 99 and by the exact 158-case script; they
  have not yet had a separate Agent reading.

**Conditional, on named hypotheses.** 54.A (\(k=1\), \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},\mathrm H_{\rm eq},
\mathrm H_{\rm rem}\), no collapse, standard caps); 56.A (additionally one-sided SW\(_L\), (N\(_0\)), orbifold regularity);
Theorem H (Yamabe value \(\mathcal Y_{\rm hyp}\)); N1 (metric-wise actual supply); 96.K is a necessary-condition theorem
under its listed orbifold/filler hypotheses, not an existence statement.

**What the centre \(0<k<A/3\) requires.** The orbifold sector has four layers: (1) aggregate curvature transfer —
class-blind once its budget passes; (2) integral bilinear topology — now settled (no universal obstruction above
\(4t\), arithmetic obstructions below); (3) geometric realization — embedded Wahl balls/plumbings or \(D_{\ge6}\) prism
complements with the prescribed complement and degree-one map, plus characteristic refinements; (4) singular
analysis — negative Einstein orbifold existence and class-sensitive APS/Dedekind, orbifold-monopole or type-T
information. Any remaining obstruction lives in layers (3)–(4). The smooth route lacks a metric-wise class-sensitive
relation that remains quantitative through the aligned (strictly almost-Kähler, \(J\)-invariant Ricci,
Einstein–Maxwell) and cscK degeneracies and accommodates the certified sub-unit cells; the density-free O10 endpoint
is the other candidate input. No positive-gap theorem, zero-gap construction or Einstein metric on any \(M\) with
\(0<k<A/3\) has been obtained.

## 7. Continuation Steps 101–104 (owner-authorized; centre still open)

**Readings.** Step 101 (Agent4) independently read the 93.A nonattainment proof (equality forces \(S=32\pi^2A\),
\(W^-=0\); stationarity makes the metric \(\int s^2\)-critical, \(\Delta s=0\), \(s\) constant, \(s\operatorname{Ric}^\circ=0\),
contradicting \(P=8\pi^2k>0\)) and the Step-99 strengthenings of 98.W/98.V (Frattini \(i=0\), torsion-block elimination,
\(L=Q_X\oplus L_0\), four-coordinate realization and sharpness, chain primitivity). No repair was needed; the provenance
caveats in §6 for these two items are discharged. Agent4 also read \(D=T_{AK}\) and A01 Theorem 83.5 (recorded in §4).

**Layer (3) now has an actual family.** Theorem 102.R realizes Wahl points geometrically inside \(M\) (four exceptional
coordinates per point; \(k=4<A/3\) for \(A>12\)), with degree-one map to \(X\). Step 103 independently read the PPS source
and verified complex-orientation compatibility, ordinary \(\pi_1\), and the resolution using PPS Proposition 5.1.
**Layer (4) is reduced.** Proposition 102.K(a)–(c) shows that the transferred scalar/mixed curvature constraints coincide
with the smooth constraints on \(M\) (\(K^2\)-invariance; \(W^-\)-side term slack), and excludes Kähler–Einstein orbifold
metrics. The SW correspondence invoked only in 102.K(d) remains conditional. Lemma 103.I gives the exact local content:
for \(n\ge3\) isotropy forces both Weyl blocks to have repeated eigenvalues at the cone point, but invariant Einstein germs
exist, so there is no local obstruction. Fine–Premoselli ramified covers, Anderson–Bamler toral Dehn filling and cscK/KE
smoothing have no entry data on this family. Thus the Wahl sector asks whether some \(V_{X,\mathbf n,k}\), \(A>3k\), carries
a non-Kähler negative Einstein orbifold metric. CH/Kähler locally symmetric type is excluded; RH type is excluded whenever
\(\tau_{\rm orb}=A/9-k+\frac23\sum(1-n_j^{-2})\ne0\). The blanket positivity asserted with \(A/3\) was corrected.
Proof notes: `notes/step102_wahl_orbifold_realization_and_K2_invariance.md` and
`notes/step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`.

**Step 104 (Agent2).** The boundary character computation (Prop. 104.C) closes the isotropy route: the filler-transfer
estimates on \(V\) do not use an orbifold monopole; extending classes have \(j = 0\) where A01's data gives nonzero
\(\Phi(p)\). [Step 105: this paragraph's 104.C/104.F conclusions are withdrawn; see the Step 105 correction below.] The cusp/F-structure channel (Prop. 104.F) collapses to the orbifold case: \(\Gamma\) is Gromov-hyperbolic
with no \(\mathbb{Z}^2\), non-spherical cusp cross-sections have \(\mathbb{Z}^2 \subset \pi_1\), and total collapse is
excluded. Orbifold monopole existence via shrinking-filler limit (Prop. 104.M, modulo equivariant removability)
partially rehabilitates 102.K(d). Proof note: `notes/step104_character_computation_and_cusp_reduction.md`.

**Step 105 correction.** 104.C/104.F withdrawn, 104.M downgraded to Question 105.M (A01 #888, Spirit #119).
**Step 106 independent reading.** 105.Q/105.L and the \(A/11\) threshold stand after the multi-end, tail-volume and ball-cap repairs above. The first invisible Hopf object is now exact: a rank-four D4 ALF core has \(Q=-D_4\), end \(S^3/Q_8\), and link charges \((-2,2)\); the punctured real rank-two disk bundle over \(\mathbb{RP}^2\) supplies a cobordism to \(S^3\) with \(\chi=\tau=0\) and the index-two extension \(-D_4\subset-I_4\). This is topologically and energetically compatible, not constructed: the relative smooth identification with \(\#4\overline{\mathbb{CP}}^2\setminus B^4\) and a vanishing-full-energy collapsing transition remain open. Chen–Chen classifies fast-decay hyperkähler instantons, not every bubble allowed by (E), so no finite exhaustive decomposition follows.
**The second alternative has three subchannels.** (i) Wahl/Einstein orbifold: concrete topology, existence open; isotropy gives no global obstruction (103.I). (ii) \(D_{\ge6}\) prism complement: necessary data only. (iii) Einstein domain with collapsed/cusp complement: cap-charge law 105.Q/105.L under hypotheses (E), with the matched D4-ALF four-class architecture and other lens/Seifert, \(T^2\)/Nil or multi-end cases still unresolved. Extraction of structure (E) from an arbitrary \(\mathscr D\to0\) sequence is not proved.
**Steps 107–108 (Einstein-end constraints and independent close).** The Step-107 note `notes/step107_einstein_end_constraints_D4_object_and_specification.md`, exact scripts/data and external inputs were independently read at Step 108; see `notes/step108_independent_reading_and_synchronized_close.md`. Both Step-106/107 scripts were rerun and again have `all_ok=true`. Theorem 107.A [P] needs only \(g-g_0=o(1)\) and \(\operatorname{Ric}_g-\operatorname{Ric}_{g_0}=o(1)\) in the model orthonormal frame (relative \(C^2\) is sufficient; Dai–Wei rescaled smoothness alone is not): a fixed-base circle-fibred Einstein cusp has \(\lambda=-\kappa^2\), constant fibre factor and \(K_B=\lambda<0\). Thus fixed \(S^2\)- and Euclidean \(T^2\)-base ends of this class are void; CH/RH and other shrinking-base cusps are untouched. Dai–Wei gives \(c_+=T_+(C)+e-3\operatorname{sign}e\); an ordinary disc bundle over \(\Sigma_g\), \(g\ge2\), has \(c_+=4-4g+e\) and is excluded by nonnegativity plus SW adjunction under the stated smooth-base basic-class supply (\(b_+>1\), or chamber input). Theorem 107.B [P] excludes every finite-volume spherical end whose lift is biaxial; Proposition 107.C [P] excludes diagonal Bianchi IX ends with \(\liminf\sigma_2>0\), including the stated anisotropy range. Finite tail energy supplies bounded curvature only after invoking the quoted unit-scale Einstein ε-regularity theorem. The unresolved Einstein-side target is symmetry-free Hopf-end volume growth: curvature prevents a Hopf \(S^2\) base from simply shrinking, while 107.A eliminates the fixed-base profile, leaving a nonsymmetric/nonstandard (effectively growing-base) profile requiring controlled level sets. A positive theorem voids all Hopf caps.

The D4 object survived independent reading at exact scope. \(N_{D4,\mathrm{trunc}}\cup W\) is simply connected and Donaldson gives form \(-I_4\), hence Freedman gives only a homeomorphism to \(\#4\overline{\mathbb{CP}}^2\); the diffeomorphism/Kirby identification is open. The cone-filled underlying space has \(H_2=\mathbb Z_2\); calling the union its minimal D4 resolution needs a relative plumbing identification. The vanishing-transition charge and the Einstein host remain compatibility requirements, not constructions, and a global gluing theorem would still be needed.

**A01 Step 93 independently read at Step 108 (authoritative §8, including correction #894).** Theorem 93.A proves WFL under explicit finite metric-wise supply (S); removability uses the determinant gauge \(e^{if/2}\) and the corrected \(W^{1,p}\) bootstrap. For \(b_+>1\) the signed canonical blow-up classes supply (S); \(b_+=1\) needs chamber input. Lemma 93.I transfers extendible Dirac indices; its all-\(n\) character statement has an exact proof, while the finite script is numerical. Proposition 93.Y is existential and marked: it covers odd \(n\ge3\) through the holomorphic \((-4)\)-curve and \(n=2\) through \((-3)\), not arbitrary embeddings or even \(n\ge4\). It realizes a projective nonminimal general-type Wahl orbifold with non-nef canonical divisor. This is structural self-similarity, not equivalence of Einstein existence: only \(a^2\), \(T_+\), extendible indices, metric-wise supply and scalar/\(W^+\) LeBrun bounds transfer; \(T_-\), local characters, forced zeros, full SW invariants and moduli geometry do not. For \(n\ge3\), complementary forced-zero classes still average \((a^+)^2\ge A\), yielding \(\Phi(p)=\nabla\Phi(p)=0\) and strict \(\int(s^-)^2>32\pi^2A\), but no uniform gap. The new Wahl target is control of the marked dimensionless regularity scale \(\lambda r_0^2\), or a marked-character bubble tree deciding whether this strictness disappears into shrinking Ricci-flat bubbles. No complex realization of the \(D_{\ge6}\) prism candidate is known.

**Chiral charge principle (final form, conditional on (E) and stated end asymptotics).** The controlled scalar/\(W^+\) mechanism sees a removed region exactly through its \(C_+\)-charge (\(9k+8\sum c_j\le3A\)); topology can hide from that chirality only by paying in \(C_-\) (four-class cap \((c_+,c_-)=(0,20)\)); the Einstein-end equations then decide which links can host a zero-charge cap. This unifies the three subchannels without identifying them.

**Close of Steps 101–108.** For \(0<k<A/3\), positive gap / nonattained zero / smooth negative Einstein remains undecided. The nonattained-zero mechanisms are: (i) marked Wahl orbifolds, now with WFL, forced-zero strictness and the marked-character scale problem but open Einstein existence; (ii) \(D_{\ge6}\) prism data, with no geometric or complex realization; (iii) the (E)-conditional Einstein-domain channel, restricted by 107.A–C but still containing the symmetry-free Hopf question, shrinking-base cusps and multi-class hyperbolic-base caps. The first next moves are the symmetry-free Hopf volume-growth theorem; marked-character Wahl bubble-tree/construction work; geometric/complex realization of \(D_{\ge6}\); D4 Kirby calculus only if the Hopf host survives; and the same-metric smooth relation specified in Step 107 §5. Extraction of (E) remains a named hypothesis. No positive-gap theorem, zero-gap sequence or smooth Einstein metric is known in the hard range.
