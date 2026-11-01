# Step 94 — Ricci-flat filler screen for absorbing Einstein orbifolds: exact budget with bulk classes, lattice filter, and the resulting dichotomy; source searches

> **Binding Step-95 correction.** Exact symbolic calculation confirms (94.1) and (94.2), and a signed-support proof plus exhaustive root search confirms that Kronheimer-only full absorption is a sum of \(D\)-blocks and requires some \(D_a\) with \(a\ge6\). The exact first threshold is \(D_6\): \(A_{\rm crit}=3675/64\), hence first off-wall ball-quotient multiple \(A=63\); the earlier \(A\gtrsim48\) estimate is withdrawn. Interpret \(k_b\) only as rank not represented by filler homology, not as identified exceptional spheres. Positive \(k_b\) gives one unit of aggregate budget per rank but does not make every configuration pass. A Wahl ball absorbs no rank, yet it can coexist with full-rank Kronheimer fillers, so its presence does not imply \(k_b>0\). The exact proof, computation, and corrected scope are `step95_verified_transfer_lattice_thresholds.md`; the insertion-ready statement is `step95_package_integration_patch.md`; scripts/data are under `workspace/scripts/step95_*` and `workspace/data/step95/`.

> **Binding Step-97/98/99 correction.** The general-\(k\) Wahl reading below through the norm-four vector \(e_1+e_2+e_3+e_4\) is withdrawn. Proposition 98.W and the Step-99 repair of Corollary 98.V in `step96_suvaina_lattice_and_kahler_filler_theorem.md` §3 are binding: for an aspherical host with torsion-free \(\pi_1\), the complement lattice has index exactly \(\prod n_j\), its discriminant form is the lens linking form even when \(H_1(X)\) has torsion, and the host lattice splits off. Bilinear data can obstruct at low rank but are uniformly realizable for \(k\ge4t\); compatible gluing already gives the abstract primitive resolution-chain embedding. The Şuvaina-lattice conjecture of this note is proved for the full class, including resolved singular fibres, as Lemma 96.Ş.
Session S1003A02, Agent1. Inputs: Spirit #106; `step93_paired_A1_transfer_review.md`; A01 `Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md`, `.../scripts/step74_neck_and_screen.py`, `.../data/step74/neck_and_screen.json`; `step55_k1_orbifold_gate_charges_lattices_collapse.md` (charges (1.1), ledger (1.2), Theorem 55.5); `step56_orbifold_attainment_zero_energy_bound_Tpoint_interaction.md`; `step52_residual_norm_selection_absorption.md` with `data/step52_absorption_lattice.json`; Şuvaina \cite{suvaina2011ale} (Knowledge `ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210`, Theorem B: every ALE Ricci-flat Kähler surface is the minimal resolution of a fibre of a one-parameter Q-Gorenstein deformation of \(\mathbb C^2/H\)); Knowledge `Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771`, Prop. 2.1 (type-T list via Şuvaina and Wright: every ASD Ricci-flat ALE space is Kähler for an orientation-compatible complex structure) and Prop. 2.4 ("or else there are Ricci-flat ALE 4-manifolds that remain to be discovered").

Marks: **[D]** derived in Step 94 with the proof written here, not yet independently checked; **[N]** computation pending; **[S]** source outcome; **[O]** open. Nothing in this note was machine-checked in Step 94.

## 0. Stale-wording readback

A search of `workspace/notes` for "2m<A/3", "m<A/6" and Einstein-requirement phrasing found no residual claim that an Einstein football merely needs \(2m<A/3\). Package §1 (Step-93 paragraph), §22.6(6), §24.1(4), §24.4, the front matter (Problem 1) and ledger II already carry 93.A. The Step-52 binding erratum ended with "cannot cross \(h=1/3\)" without 93.A; it is updated in this Step. The 87.O deficit formula \(d_{*,\rm orb}=4\pi^2(A/3-2m)\) remains valid.

## 1. Source searches [S]

Manifest: `trace/knowledge_request/knowledge_request_1791514794058941098.json` (status partial; external retrieval degraded).

**1a. One-sided SW\(_L\).** No returned source states the needed one-sided statement (a splitting along a spherical space form \(L\) where the side carrying \(b^+\ge1\) has a PSC orbifold cap, or the complementary side is negative definite, forcing \(SW_M=0\)). Returned and read at representation level: \cite{lin2019seiberg} (end-periodic SW; PSC obstruction for homology \(S^1\times S^3\) via \(\lambda_{SW}+h\)); \cite{kronheimer2003monopoles} (cobordism maps: PSC vanishing of the \(j\)-map, negative-definite cobordisms inducing isomorphisms on the bar theory, vanishing for \(b^+>0\) cobordisms — ingredients, not the cap theorem); \cite{wang1996seiberg} (integral homology spheres only); \cite{khandhawit2023unfolded} (relative Bauer–Furuta gluing; Cor. 1.9 for essential square-zero spheres); \cite{mrowka1997seiberg}; \cite{agolhyperbolic} (two-sided \(L\)-space vanishing, already used). SW\(_L\) one-sided stays a named hypothesis. It matters only for non-aspherical \(b^+\ge2\) hosts, since the Γ-vertex proof replaced it for ball quotients. Whether the KMOS negative-definite/PSC cobordism facts assemble into the cap statement for \(L\)-space links was not attempted.

**1b. Armstrong 2002** (\cite{armstrong2002ansatz}, DOI 10.1515/crll.2002.009): metadata and abstract only (paywalled). Abstract: Tod's ansatz describes all known strictly almost-Kähler Einstein 4-manifolds; every weakly \(*\)-Einstein strictly AKE 4-manifold arises from it; the ideas are then applied further (text truncated). LeBrun 2001 (`Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`, line 273) paraphrases it as nonexistence of compact Einstein strictly AK 4-manifolds with \(\omega\) everywhere a \(W^+\)-eigenvector. **The elementary zero obstruction is not from Armstrong 2002**: Apostolov–Armstrong–Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds* (`Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md`, line 190), Lemma 2: if the Nijenhuis tensor vanishes nowhere then \(c_1(I)=3c_1(J)\), and on compact \(M\), \(5\chi=-6\sigma\); attributed there to Armstrong, Quart. J. Math. 48 (1997) [8], and LeBrun [38]. This is exactly \(c_2(K^{-1}\otimes T^{1,0})=5\chi+6\tau=0\). Problem 4's forced-zero item can cite ADK Lemma 2 / Armstrong 1997 (citation key to be read from that object's `citation.bib`).

## 2. Setting

\(X\) compact minimal surface of general type, \(A=c_1^2(X)\), \(c_2=c_2(X)\), \(M_k=X\#k\overline{\mathbb{CP}}^2\), \(T_+(M_k)=A-k\), \(T_-(M_k)=4c_2-A+5k\) (ball quotient: \(A/3+5k\)). \(V\) is a compact oriented orbifold with isolated points \(p_j\), \(\Gamma_j\subset SO(4)\) free on \(S^3\), resolved by Ricci-flat ALE fillers \(N_j\) (orientation-matched equivariant end charts, derivative-controlled decay, Lemma 86.S) to a manifold diffeomorphic to \(M_k\). With Step-55 charges \(c_\pm(N)=2/|\Gamma|-2\chi\mp3\tau\mp3\eta\) and \(C_\pm=\sum_jc_\pm(N_j)\): \(T_\pm^{\rm orb}(V)=T_\pm(M_k)+C_\pm\). For Ricci-flat \(N\): \(c_\pm=-\frac1{2\pi^2}\int_N|W^\pm|^2\le0\) and \(c_++c_-=-4(\chi(N)-1/|\Gamma|)\).

Known Ricci-flat ALE spaces are Kähler (Kronheimer ADE; Şuvaina's fibres = free \(\mathbb Z_n\)-quotients of \(A_{dn-1}\), \(|\Gamma|=dn^2\), \(\chi=d\), \(b_2=d-1\), \(\pi_1=\mathbb Z_n\); \(d=1\) are the Wahl balls). "cx" = complex orientation equal to \(M\)'s: \(c_+=0,\ c_-=-4(\chi-1/|\Gamma|)\). "rev": \(c_-=0,\ c_+=-4(\chi-1/|\Gamma|)\). No non-Kähler Ricci-flat ALE space is supplied in the corpus.

Einstein bulk (\(\lambda<0\) forced by the negative-Yamabe exclusion): \(P=0\Rightarrow I_\pm=2\pi^2(T_\pm^{\rm orb}-x)\), \(x=S/96\pi^2\). Scalar transfer: \(x\ge A/3\). Mixed transfer (Step 93 §4): \(F(x,T_+^{\rm orb})\ge6A+C_+\), \(F(x,T)=(\sqrt{8x}+\sqrt{T-x})^2\).

## 3. Exact transferred screen [D]

**Lemma 94.T.** \(F=g\circ\ell\) with \(g(a,b)=(\sqrt a+\sqrt b)^2\) concave and 1-homogeneous and \(\ell(x,T)=(8x,T-x)\) linear, so \(F\) is concave and 1-homogeneous on \(0\le x\le T\); hence \(F(z)\le\nabla F(z_0)\cdot z\). On the KE ray \(x=T/3\), \(\nabla F=(9,3)\), so
\[F(x,T)\le9x+3T,\]
with equality exactly on that ray. With \(x\le T_-^{\rm orb}\):
\[\boxed{9C_-+2C_++42k+12\,(3c_2-c_1^2)(X)\ge0.}\tag{94.1}\]
(Host term: \(9(4c_2-A+5k)+3(A-k)-6A=36c_2-12A+42k\).) For ball quotients this is A01's exact inequality. The only host dependence is the BMY defect \(3c_2-c_1^2\). Scalar-only: \(C_-+5k+\tfrac43(3c_2-c_1^2)\ge0\). Finite-\(A\), cx fillers only, ball quotient: \(T_-^{\rm orb}\ge x_{\min}=\frac A{27}\bigl(4-\sqrt{1-3k/A}\bigr)^2\) (checked at \(k=0\): \(A/3\); at \(k=A/3\): \(16A/27=8T_+/9\)).

**Corollary 94.T1 (footballs over any host).** \(V_m=X\#m(S^4/\mathbb Z_2)\), EH resolution \(X\#2m\overline{\mathbb{CP}}^2\) by (R), \(C_+=0\), \(C_-=-12m\). Then (94.1) gives \(2m\le3c_2-c_1^2\), so \(V_m\) has no Einstein orbifold metric when \(2m>3c_2(X)-c_1^2(X)\). Ball quotients recover 93.A. Scalar transfer gives \(P_{*,\rm orb}(V_m)\ge8\pi^2\bigl(k-\tfrac43(3c_2-c_1^2)\bigr)_+\), against \(\le8\pi^2k\) from Green caps when \(X\) is KE.

## 4. Lattice filter over aspherical hosts [D]

**Lemma 94.L.** Let \(X\) be aspherical with torsion-free \(\pi_1=\Gamma\) (ball quotients). For every filler with finite \(\pi_1\): the classifying map \(c:M_k\to X\) is null-homotopic on \(N_j\) (finite image in torsion-free Γ, lift to the contractible cover). So \(H_2(N_j;\mathbb Z)/{\rm tors}\to H_2(M_k)\) is an injective isometry (rational Mayer–Vietoris, rational-sphere links) into \(\ker c_*=\oplus\mathbb ZE_i\cong-I_k\) (\(c\simeq\) degree-one pinch, maps to \(K(\Gamma,1)\) being classified by \(\pi_1\)). Images of distinct fillers are mutually orthogonal and orthogonal to the bulk.

Consequences:
- **(L1)** Every filler is negative definite in \(M\)'s orientation. Reversed-orientation Kähler Ricci-flat fillers are rational balls: Wahl \(B_{n,a}\) with \(c_+=-4(1-1/n^2)\), \(c_-=0\). Reversed Kronheimer fillers are excluded.
- **(L2)** Kronheimer: \(\oplus R_j\hookrightarrow\mathbb Z^k\). Roots go to \(\pm e_a\pm e_b\), so \(\oplus R_j\) is a sub-root-system of \(D_k\): only types A and D. \(A_r\) uses \(r+1\) coordinates (except \(A_3=D_3\)); \(D_l\) uses \(l\); \(D_2=A_1\oplus A_1\) is an EH pair \(e_a\pm e_b\) (Lemma 52.6). \(E_6,E_7,E_8\) never occur. For \(E_8\) directly: \(\mathbb Z^k=E_8\oplus E_8^\perp\) would put every unit vector in \(E_8^\perp\). \(E_6/E_7\) and the slot rule rest on the classification of subsystems of \(D_k\) [N: exhaustive check].
- **(L3)** Put \(k_b:=k-\sum_jb_2(N_j)\), the exceptional ranks left in the bulk. Every A-component not inside a \(D_2\) or \(D_3\) forces at least one unit of \(k_b\).
- **(L4)** Full absorption \(k_b=0\) with Kronheimer fillers \(\iff\oplus R_j\) is a full-rank subsystem of \(D_k\) \(\iff\oplus R_j\cong\oplus_iD_{a_i}\), \(\sum a_i=k\). Simply-laced reflection-closed subsets are closed; Borel–de Siebenthal iteration on \(\tilde D_k\) gives \(D_a\oplus D_{k-a}\).
- **Şuvaina \(d\ge2\) fibres.** \(|H_1(\partial N)|=|\det Q_N|\,|{\rm Tors}\,H_1N|^2\) gives \(|\det Q_N|=d\). For odd \(n\) the form is even (transfer: \(\pi^!a\cdot\pi^!b=n\,a\cdot b\)). Conjecture: \(Q_N\cong A_{d-1}(-1)\) [N]. If so, these fibres are dominated by Kronheimer \(A_{d-1}\) in every budget below.
- **Superseded Wahl reading.** The tentative vector and \(k\ge3\) inference are withdrawn by the binding Step-99 correction above. The correct definite-lattice problem lives in \(-I_k\): complex-oriented \(B_{2,1}\) needs rank at least three, four coordinates suffice uniformly for one point, and compatible discriminant gluing recovers Theorem 55.5 at \(k=1\).

## 5. Budget with bulk classes and the dichotomy [D]

**Proposition 94.B.** Take a ball-quotient host and an Einstein \(V\) with Kähler Ricci-flat fillers (sets cx, rev). Then
\[\sum_{\rm cx}\Bigl(1-\tfrac1{|\Gamma_j|}\Bigr)+\tfrac29\sum_{\rm rev}\Bigl(1-\tfrac1{n_j^2}\Bigr)\le\frac k6+k_b,\tag{94.2}\]
and, if rev \(=\varnothing\),
\[\sum_{\rm cx}\Bigl(1-\tfrac1{|\Gamma_j|}\Bigr)\le k_b+\beta(k,A),\qquad \beta=\frac{A/3+k-x_{\min}}4=\frac k6-\frac{k^2}{12A}-\frac{k^3}{8A^2}+O(k^4/A^3).\tag{94.3}\]
*Proof.* \(\sum_{\rm cx}(\chi_j-1/|\Gamma_j|)=(k-k_b)+\sum_{\rm cx}(1-1/|\Gamma_j|)\), using (L1). Insert \(C_-=-4\sum_{\rm cx}(\chi_j-1/|\Gamma_j|)\) and \(C_+=-4\sum_{\rm rev}(1-1/n_j^2)\) into (94.1) and divide by 36. For (94.3): \(T_-^{\rm orb}=A/3+k+4k_b-4\sum_{\rm cx}(1-1/|\Gamma_j|)\ge x_{\min}\). \(\square\)

The transferred inequalities see only \(\chi-1/|\Gamma|\) and \(A=K^2\). Each class left in the bulk enlarges the filler budget by one unit at no transferred cost. The §16 additive budget \(\sum\max\{c_+,c_-,0\}<1\) is automatic for Ricci-flat fillers.

**Corollary 94.F (full absorption).** Costs: \(D_2\) (EH pair) \(1\), \(D_3=A_3\) \(3/4\), \(D_a\) \(1-1/(4a-8)\). (94.3) requires \(\sum_i{\rm cost}(D_{a_i})\le\beta(k,A)<k/6\). Surplus \(\sigma(D_a)=a/6-{\rm cost}\): \(-2/3,-1/4,-5/24,-1/12,+1/16,+13/60\) for \(a=2,\dots,7\); in general \((a-6)/6+1/(4a-8)\). Hence every full absorption contains a \(D_a\) with \(a\ge6\). EH-pair-only (93.A), \(A_3\)-, \(D_4\)- and \(D_5\)-only absorptions are impossible at every \(A\). A01's single-filler survivors \(A_{n\ge6}\) and \(E_6\)–\(E_8\) at \(k={\rm rank}\) are lattice-impossible. Thresholds [N]: \(D_6\) at \(k=6\) needs \(15/16\le\beta(6,A)\) (leading order \(A\gtrsim48\)); \(D_7\) at \(k=7\) needs \(13/60\ge49/12A\) (\(A\gtrsim19\)) together with \(k<A/3\). Large blocks subsidize small ones, e.g. \(\sigma(D_{10})\ge2/3\) offsets one EH pair.

Topology [O]: \(k_b=0\) needs an orbifold whose resolution is \(X\#k\overline{\mathbb{CP}}^2\) with \(b_2(V)=b_2(X)\). For example \(V=X\#W\) with \(W\) built from a rational homology ball \(Q\) bounded by the \(D_a\) prism manifold such that \(Q\cup\)plumbing \(\cong\#a\overline{\mathbb{CP}}^2\setminus B^4\). Not decided.

**Corollary 94.W (channels invisible to transfer).** For \(k_b\ge1\), (94.2)–(94.3) are the only transferred constraints. They pass:
- (i) every unpaired \(A_r\) Kronheimer filler with its forced bulk class (cost \(<1\le k_b\));
- (ii) cx Wahl balls with \(\sum(1-1/n_j^2)\le7k/6\), e.g. \(\tfrac19(1,2)\) at \(k=1\) (cost \(8/9\)), lattice-allowed by 55.5;
- (iii) rev Wahl balls with \(\sum(1-1/n_j^2)\le21k/4\).

In all three the Einstein bulk carries exceptional classes. It obeys the same transferred LeBrun inequality as a smooth Einstein metric on \(M_k\), with a smaller anti-self-dual budget.

**Correction to the target of Spirit #106.** "Over ball-quotient hosts every absorbing Einstein orbifold needs a non-Kähler Ricci-flat ALE filler" does not follow. At the charge-and-lattice level it is contradicted by (II-a) \(D_{\ge6}\)-dominated full absorptions at large \(A\), and by (II-b) all \(k_b\ge1\) channels, including Wahl balls. The second centre alternative therefore splits into:
- (II-a): decided by rational-ball topology and explicit \(A\)-thresholds;
- (II-b): Einstein orbifolds carrying exceptional classes in the bulk, which no transferred inequality distinguishes from Problem 1.

Survivor rows are charge-and-lattice data, not constructions. Separating (II-b) needs class-sensitive orbifold information, e.g. \(\sum_{\rm bulk}|E_i^+|^2\) in the sign-averaged monopole estimate, which vanishes for absorbed classes and not for bulk classes.

## 6. General hosts [D]

(94.1) holds for every minimal general-type \(X\). The slack \(12(3c_2-c_1^2)\) enlarges (94.2) by \((3c_2-c_1^2)/3\). Lemma 94.L needs asphericity and a torsion-free \(\pi_1\). On simply connected hosts filler classes may map nontrivially and positive-definite fillers are not excluded. Ball quotients are exactly the hosts where the transferred screen is tight.

## 7. Wall

At \(k=A/3\) (ball quotient), \(x_{\min}=8T_+/9\) forces \(x=16A/27\) and equality in the Cauchy–Schwarz step on \(V\) (\(|W^+|\propto|s|\) constant). The 93.A wall question (constant \(s<0\), \(W^-=0\)) stays open. Transfer of LeBrun's equality structure to orbifolds is not claimed.

## 8. Checks to run [N]

1. Exhaustive non-embedding of \(E_6,E_7\) into \(\mathbb Z^k\) (\(k\le12\), resp. \(14\)), and the slot rule for \(A_r,D_l\).
2. Exact \(A\)-thresholds for all \(D\)-block partitions with \(k\le40\) (exact \(x_{\min}\), interval arithmetic), including subsidized mixtures.
3. Wahl lattice law at \(k\ge2\), cx and rev: \(C\subset K\) unimodular of rank \(r+k\), \(C^\perp\) of index \(n\) in \(-I_k\), bilinear anti-isometry.
4. Şuvaina \(d\ge2\) lattice from the \(\mathbb Z_n\)-invariant GH homology; test \(A_{d-1}(-1)\).
5. Knowledge: spherical 3-manifolds (prism manifolds of type \(D_a\)) bounding rational homology balls, for (II-a) topology.
