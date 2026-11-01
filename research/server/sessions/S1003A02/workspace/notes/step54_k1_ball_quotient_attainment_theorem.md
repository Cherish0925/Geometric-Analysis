# Step 54 — The k = 1 ball-quotient theorem: smooth bubbling is topologically excluded, and the minimizer is Einstein or a non-Bach-flat global optimum

> **Binding proof-order erratum (Steps 87–90; package §15).** The proof of Theorem 54.A in §2 has been rewritten (Step 90) in the Γ-vertex order; the summary below is retained for orientation. For ball-quotient hosts Lemma 54.3 is not needed, and neither is the SW transfer \(SW_{V\#\Sigma}=SW_V\) in (iii). (a) Free indecomposability of \(\Gamma=\pi_1(X)\) gives a unique summand \(Y\) carrying \(\Gamma\); the classifying map factors through \(Y\to X\) of degree one, so \(b^+(Y)\ge b^+(X)\ge3\). (b) \(Y\) cannot be a bubble cap: \(\mathrm{H_{dec}}\) + Lemma 53.Y would give it PSC, but \(Y\) is essential with negatively curved fundamental group (\cite{mantionegeographya}, Prop. 2). (c) Every bubble complement then has \(b^+\ge3\), and ordinary connected-sum vanishing forces \(b^+(\widehat N_k)=0\). (d) In (iii), \(V\) is essential with \(\pi_1=\Gamma\), so no PSC metric; \(s\equiv0\) would be Ricci-flat by Bourguignon (\cite{kotschick2004monopole}, appendix) and then \(\pi_1\) virtually abelian (\cite{barbara2020fundamental}, Thm 2.7), impossible for a cocompact lattice. Hence \(s_{g_0}<0\). Lemma 54.3 remains a standalone [P*] result for other hosts. Notation \(p_*\) below is the trace-free infimum \(P_*\) (Step-70 split).

Session S1003A02, Agent2, Execute. Builds on `step53_anderson_entrance_bubble_exclusion_attainment.md` (as corrected
by the Step-53 verifier, `trace/ttcs/results/step53_ttcs01_verifier1_integration.md`, whose corrections are listed
in §0) and on the supplement `web_research_collected.tex` Ch. 5 (analytic CH-collar cell). Checks:
`workspace/scripts/step54_charge_and_entropy_checks.py` → `workspace/data/step54_charge_and_entropy_checks.json`.

Conventions. \(P(g)=\int|\operatorname{Ric}^\circ|^2\), \(p_*(M)=\inf P\), \(T_+=2\chi+3\tau\). For closed \(V\),
\(P=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2T_+(V)\).

---

## 0. Step-53 corrections now in force

1. Euler bookkeeping counts **cone branches** at reducible vertices; the truncated-piece proof of
   \(p_*(M)=P(V,g_0)+\sum_kP(N_k)\) covers all tree depths, reducible vertices and multi-ended necks (verifier §2).
   Schwarzschild check \(P=32\pi^2\) agrees with A01's neck baseline.
2. Bubble relocation (53.B) needs a one-attachment tree with \(M\cong M'\#\widehat T\); a two-ended neck is not movable.
3. Rank-one flux gives \(\mathbf R^+\le0\) only for **positive** flux; positivity follows from the positive-mass theorem
   (\(\operatorname{tr}\Phi^{++}=3\pi^2m_{\rm ADM}\)), and then exclusion gives \(s\le0\) for every nonflat ASD bubble.
4. Negative KE: \(\mathbf R^+=\operatorname{diag}(s/4,0,0)\), kernel of dimension 2, **unit kernel directions an \(S^1\)**.
5. 53.F′ remainder \(O(\lambda^{12/5})\) is correct but needs the half-flat cancellation \(A(k)=O(r^{-6})\); the
   homogeneous \(r^{-2}\) expansion is a hypothesis; the claimed \(\lambda^2\log\) non-ASD interaction is deleted.
6. Lemma 53.Y holds for any order \(\tau>0\) with derivative-controlled decay (\(2<q<4/(2-\tau)\)).
7. Attainment ⇔ existence of a trivial energy-equality *generalized configuration*, not necessarily Anderson's limit.
8. Bach-flat + \(P\)-critical + \(s\equiv\)const\(\neq0\) ⇒ Einstein (since \(\nabla\!\int s^2=-2s\operatorname{Ric}^\circ\) at constant
   \(s\)); "Prop. nonbach" is replaced by this one-line proof.
9. Anderson's printed proof has three soft spots: local minimality of weak limits; Prop. 4.6 regularity (the
   "linearly independent summands" inference is invalid) and its uniformity under rescaling, where the perturbation
   becomes \(\varepsilon\ell^{4-4p}\int(\ell^4+|\operatorname{Ric}|^2)^p\); the case-(I) equality (4.43) by citation.
   Theorem 4.10 is a published statement; we use it with these dependencies named.

---

## 1. Topological cost of smooth bubbles in both orientations

**Lemma 54.1 (two-orientation bubble cost).** Let \(N\) be a smooth complete AE manifold with \(e\ge1\) ends, all with
trivial group, with derivative-controlled decay of some order \(\tau>0\) (so the Chern–Gauss–Bonnet and signature
boundary terms converge to the flat values). Let \(\widehat N\) be the closed manifold obtained by adding one point
per end. Then
\[
P(N)=4\!\int_N|W^+|^2+\tfrac1{12}\!\int_Ns^2+8\pi^2c(N)=4\!\int_N|W^-|^2+\tfrac1{12}\!\int_Ns^2+8\pi^2c(\bar N),
\]
\[
c(N)=4(e-1)+4b_1+b^- -5b^+,\qquad c(\bar N)=4(e-1)+4b_1+b^+-5b^-,
\]
Betti numbers of \(\widehat N\). Hence \(P(N)\ge8\pi^2\max\{c(N),c(\bar N),0\}\).

*Proof.* \(\chi(N)=\chi(\widehat N)-e\), Gauss–Bonnet integrand total \(e_{GB}(N)=\chi(N)-e\), \(\tau(N)=\tau(\widehat N)\),
\(\chi(\widehat N)=2-2b_1+b_2\). Insert into \(P=4\int|W^\pm|^2+\frac1{12}\int s^2-8\pi^2(2e_{GB}\pm3\tau)\). \(\square\)

Checks (script): Burns \(c=1\); reversed Burns \(c(\bar N)=1\); Schwarzschild \(c=4\) (\(=32\pi^2\)); three-ended neck 8;
\(S^1\times S^3\) cap 4; homotopy-sphere bubble 0; \(S^2\times S^2\) cap \(-4\) in both orientations (no bound).
**[Corrected after verification.]** \(c,\bar c\le0\iff D:=4(e-1)+4b_1\le\min\{5b^+-b^-,5b^--b^+\}\). This does **not**
force \(e=1\) or \(b_1=0\). Example: a two-ended scalar-flat AE metric on \(S^2\times S^2\) minus two points (Green functions
of a PSC metric) has \(c=\bar c=0\); so does \((S^1\times S^3)\#(S^2\times S^2)\) minus a point. The usable form is:
\[
b^+(\widehat N)=0\ \Longrightarrow\ P(N)\ge8\pi^2\,[4(e-1)+4b_1+b_2].\tag{1}
\]
So \(b^+\) must be eliminated first. For ball-quotient hosts this is done in §2 by the Γ-vertex argument (essentialness plus ordinary connected-sum vanishing); Lemma 54.3 is the alternative for hosts without that input.

**Lemma 54.1′ (region form; no bubble equation needed).** Let \(g_i\) converge to a case-(I) configuration, and let
\(p\in V\) be a concentration point with trivial group. Assume the bulk satisfies small-energy regularity on punctured
balls around \(p\): since \(g_0\) is \(P\)-critical on \(V\setminus\{p\}\) with finite energy and a Sobolev bound,
\(|\mathrm{Rm}_{g_0}|(x)=o(d(x,p)^{-2})\) with derivatives. For small \(r_0\), choose by Fubini a good radius
\(r\in(r_0/2,r_0)\). Let \(U_i\subset M\) be the region bounded by the sphere \(S_r(p)\) transplanted to \((M,g_i)\), and
\(\widehat U\) its cap (with \(M\cong\widehat U\#R\)). Then
\[
P(g_i;U_i)\ \ge\ 8\pi^2\max\{c(\widehat U),c(\overline{\widehat U}),0\}-o_{r_0}(1)-o_i(1),
\]
with \(c\) as above and \(e=1\). For a region with \(e\) boundary spheres at bulk points (a neck joining bulk pieces) the
same holds with \(4(e-1)\) included.

*Proof.* Chern–Gauss–Bonnet and the APS-signature formula with boundary on \(U_i\). The boundary integrands (second
fundamental form and tangential curvature, Chern–Simons form) converge, for a.e. good radius, under the
\(C^{1,\alpha}\cap W^{2,q}\) bulk convergence on the annulus. By the punctured small-energy estimate they converge to the
round-sphere values as \(r_0\to0\). These are the values used in Lemma 54.1. \(\square\)

So once \(b^+(\widehat U)=0\) is known, the bound (1) for the region needs **no** bubble equation, decay, or
scalar-flatness. What is needed is only bulk criticality, which Anderson's statement supplies at unit scale where the
perturbation \(\varepsilon\to0\), together with lower semicontinuity. Scalar-flatness and decay of bubbles
(\(\mathrm{H_{dec}}\)) enter only through Lemma 53.Y (PSC of \(\widehat N\)). *[Superseded for ball-quotient hosts, Steps 87–90.]*
The original text used them only in an indefinite subcase \(b^+(R)=0\) via Lemma 54.3. In the §2 proof they are used once,
to give PSC to a hypothetical Γ-carrying bubble cap, which essentialness then excludes; afterwards \(b^+(R_k)\ge3\) for every
bubble and the standard connected-sum vanishing theorem suffices.

**Lemma 54.2 (summand structure).** In a case-(I) configuration with only trivial groups, each capped bubble \(\widehat N_k\)
is a connected summand of \(M\): \(M\cong\widehat N_k\#R_k\) for a closed \(R_k\). Globally
\(M\cong\#_aV_a\#\#_k\widehat N_k\#b_1(\mathcal G)(S^1\times S^3)\), \(\mathcal G\) the gluing graph.
(An \(e\)-ended bubble attached to \(e\) boundary spheres of the rest is \(\widehat N_k\) summed to the rest, with the extra
attachments producing self-sums, i.e. \(S^1\times S^3\) summands.) Each \(\widehat N_k\) carries a metric of positive scalar
curvature if \(N_k\) is scalar-flat (Lemma 53.Y, corrected form, each end compactified separately).

**Lemma 54.3 (PSC summands with \(b^+\ge1\) kill SW).** Let \(M=Z\#R\) be closed with \(b^+(M)\ge2\), where \(Z\) admits a PSC
metric and \(b^+(Z)\ge1\). Then every Seiberg–Witten invariant of \(M\) vanishes.

*Proof.* If \(b^+(R)\ge1\) this is the standard connected-sum vanishing theorem. In general stretch the neck:
\(g_T=\) PSC metric on \(Z\setminus B\) with round cylindrical end \(\cup\,S^3\times[-T,T]\cup\) any metric on \(R\setminus B\).
Choose the self-dual perturbation \(\eta\) supported in \(Z\setminus B\), small and generic. Monopoles for \((g_T,\eta)\)
with \(T\to\infty\) converge, after gauge, on compact subsets to finite-energy monopoles on both cylindrical-end pieces,
whose cylindrical limits are the (unique, nondegenerate) flat reducible of the round \(S^3\). On the \(Z\)-side,
irreducibles are excluded by the Weitzenböck formula (\(s>0\), \(\eta\) small); reducibles require
\(2\pi\,\mathcal H^+(c_1(L)|_Z)=\mathcal H^+(\eta)\) in the \(L^2\) harmonic self-dual space, which is \(\cong H^+(Z)\neq0\), a
codimension-\(b^+(Z)\) condition avoided by generic \(\eta\). So the \(Z\)-side has no limit and the moduli space of \(M\) is
empty for \(T\gg1\); as \(b^+(M)\ge2\) the invariant is metric-independent and vanishes. \(\square\)
(The compactness step is the standard neck-stretching theorem for monopoles across a PSC \(S^3\) neck; to be cited
precisely, e.g. Kronheimer–Mrowka/Morgan–Szabó–Taubes; not re-proved here.)

---

## 2. The theorem

Let \(X\) be a compact complex-hyperbolic surface (smooth ball quotient \(\Gamma\backslash\mathbb{CH}^2\)) other than a fake
projective plane. Since \(\chi(\mathcal O_X)=c_2/3\), \(p_g=c_2/3-1+q\). For \(c_2\ge6\) this gives \(p_g\ge1\); for \(c_2=3\) it
gives \(p_g=q\), and \(q\ge1\) (e.g. Cartwright–Steger) gives \(p_g\ge1\). Thus \(b^+(X)=2p_g+1\ge3\) for every ball
quotient except the fake projective planes (\(c_2=3,q=0\)), which are exactly those with \(b^+=1\). Put \(M=X\#\overline{\mathbb{CP}}^2\), \(A=c_1^2(X)=3c_2(X)\).

**Unconditional input (upper bound).** By the analytic CH-collar cell (supplement Ch. 5: a single blow-up cell equal
to the CH metric outside a fixed collar, \(P/(8\pi^2)=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2)\)), inserted into any
embedded CH ball of \(X\) of radius below the injectivity radius,
\[
p_*(M)<8\pi^2 .\tag{U}
\]
(The certified perpendicular cell, \(P/(8\pi^2)\le0.99566273277\), gives the same where its collar fits.)

**Theorem 54.A.** Let \(X,M\) be as above. Consider a minimizing configuration for \(P\) on \(M\) of Anderson's case (I)
in which every cone point has trivial group (hypothesis \(\mathrm{H_{sm}}\)), and assume:

- \(\mathrm{H_{lsc}}\): \(p_*(M)\ge\sum_aP(V_a,g_0)+\sum_kP(N_k)\) (lower semicontinuity on separated scales);
- \(\mathrm{H_{dec}}\): each bubble \(N_k\) is smooth, complete, AE with derivative-controlled decay of some order \(\tau>0\),
  and scalar-flat;
- for part (iii) also \(\mathrm{H_{eq}}\): Anderson's case-(I) energy equality, and \(\mathrm{H_{rem}}\): smooth removability at
  the trivial-group cone points.

Then:

(i) **No smooth bubble carries homology or connects components.** The bulk \(V\) is connected; every bubble is
one-ended; every \(\widehat N_k\) is a homotopy 4-sphere. In particular \(E\) is carried by the bulk.

(ii) **The bulk is a homeomorphic copy of \(M\).** With \(\Sigma=\#_k\widehat N_k\) (a homotopy sphere), \(M\cong V\#\Sigma\),
so \(V\) is homeomorphic to \(M\); each bubble has \(P(N_k)=4\int|W^+|^2=4\int|W^-|^2<8\pi^2\).

(iii) **Attainment and the dichotomy.** Under \(\mathrm{H_{eq}},\mathrm{H_{rem}}\): \(g_0\) is a smooth metric on \(V\) with
\(P(g_0)=p_*(V)\), and \(p_*(M)=p_*(V)+\sum_kP(N_k)\). If every \(\widehat N_k\) is diffeomorphic to \(S^4\) (automatic if the
smooth 4-dimensional Poincaré conjecture holds), there are **no bubbles**: \(V\cong M\) and \(g_0\) attains \(p_*(M)\).
In all cases \(s_{g_0}\) is a negative constant, and **either \(g_0\) is Einstein, or \(g_0\) is a smooth non-Bach-flat
global minimizer of \(P\)** (equivalently of \(\int|\mathrm{Rm}|^2\)) on \(V\).

*Proof (Γ-vertex order; Steps 87–90, replaces the Step-54 order that used Lemma 54.3 and \(SW_{V\#\Sigma}=SW_V\)).*

*Step 0 (the Γ-vertex).* By Lemma 54.2 the configuration determines a capped graph decomposition
\(M\cong\#_aV_a\#\#_k\widehat N_k\#b_1(\mathcal G)(S^1\times S^3)\), where every vertex is a **closed** manifold: a bulk component
with its cone points filled, or a bubble cap obtained by filling **all** of its ends. Hence
\[
\Gamma=\pi_1(M)\cong\Bigl(*_v\pi_1(Y_v)\Bigr)*F_{b_1(\mathcal G)} .
\]
\(\Gamma\) is torsion-free and a \(PD_4\) group (\(X\) is aspherical), hence one-ended and freely indecomposable (Stallings),
and \(\Gamma\not\cong\mathbb Z\). By Grushko–Kurosh the graph has no loops, exactly one vertex \(Y\) has \(\pi_1(Y)\cong\Gamma\), and
all other vertex groups are trivial. Let \(q:M\to Y\) be the degree-one connected-sum pinch (collapse every other summand);
\(q_*\) is an isomorphism on \(\pi_1\). Choose \(f_Y:Y\to X=B\Gamma\) inducing the identified isomorphism, and let
\(c:M\to X\) be the blowdown map, which has degree one and induces \(\pi_1(M)\cong\Gamma\). Since maps into the
\(K(\Gamma,1)\) space \(X\) are classified up to homotopy by their \(\pi_1\)-homomorphisms (up to conjugacy), \(c\simeq f_Y\circ q\), so
\[
(f_Y)_*[Y]=(f_Y)_*q_*[M]=c_*[M]=[X].
\]
Thus \(Y\) is essential, \(\deg f_Y=1\), and \(f_Y^*:H^2(X;\mathbb Q)\hookrightarrow H^2(Y;\mathbb Q)\) preserves the intersection pairing
(\(\langle f_Y^*a\cup f_Y^*b,[Y]\rangle=\langle a\cup b,[X]\rangle\)); hence \(b^+(Y)\ge b^+(X)\ge3\). (The closed \(Y\) is not literally a
submanifold of \(M\); only its punctured summand is. The pinch map is the closed-manifold object used.)

*Step 1 (Y is bulk).* Suppose \(Y\) were a bubble cap \(\widehat N_j\) with \(e\) AE ends. Under \(\mathrm{H_{dec}}\), the all-end form
of Lemma 53.Y (positive conformal factor decaying like \(r^{-2}\) on every end; the conformal-Laplacian equation has a
positive point source at each added point) gives the closed cap a PSC metric; this does not require \(e=1\). But \(Y\) is
essential with the fundamental group of a closed negatively curved four-manifold, and Mantione–Torres Proposition 2
(\cite{mantionegeographya}; no spin hypothesis) forbids PSC. Hence \(Y\) is a bulk vertex.

*Step 2 (bubbles carry no \(b^+\)).* For every bubble cap, \(M\cong\widehat N_k\#R_k\) with \(R_k\) a connected sum containing the
summand \(Y\), so \(b^+(R_k)\ge b^+(Y)\ge3\). If \(b^+(\widehat N_k)\ge1\), the ordinary connected-sum vanishing theorem (both sides
with \(b^+\ge1\)) gives \(SW_M\equiv0\). But \(b^+(M)\ge3\) and the blow-up formula gives \(SW_M\ne0\) on the classes
\(\pm c_1(X)\pm E\). Hence \(b^+(\widehat N_k)=0\) for every bubble. No energy and no PSC of the bubble is used here.

*Step 3 (charge).* By (U), \(\mathrm{H_{lsc}}\) and (1),
\(\sum_k[4(e_k-1)+4b_1+b_2](\widehat N_k)<1\), so \(e_k=1\) and \(b_1=b_2=0\) for every bubble. The caps are simply connected
(Step 0) rational homology spheres; \(H_2\) of a simply connected closed 4-manifold is torsion-free, so they are integral
homology spheres, hence homotopy spheres, homeomorphic to \(S^4\) (Freedman). One-ended bubbles cannot join bulk
components and the graph has no loops, so the bulk is connected, \(V=Y\), and \(M\cong V\#\Sigma\) with
\(\Sigma=\#_k\widehat N_k\). This proves (i).

(ii) \(\Sigma\) is homeomorphic to \(S^4\), so \(V\approx V\#\Sigma\cong M\). For \(e=1\), \(b_1=b_2=0\), Lemma 54.1 gives
\(P(N_k)=4\int|W^\pm|^2\) (scalar-flat), and the sum is below \(8\pi^2\).

(iii) Theorem 53.D (as corrected, §0.1/0.7) gives \(P(g_0)=p_*(V)\) and \(p_*(M)=p_*(V)+\sum P(N_k)\). If all
\(\widehat N_k\cong S^4\) then \(V\cong M\), \(p_*(V)=p_*(M)\), so \(\sum_kP(N_k)=0\); a scalar-flat AE bubble with \(\Gamma=1\) and
\(P=0\) is Ricci-flat AE, hence flat by Bishop–Gromov — no bubble. \(P\)-criticality gives \(\Delta s=0\), so \(s\) is
constant. *Sign of \(s\) without any SW transfer.* \(V\) is essential with \(\pi_1(V)=\Gamma\) (Step 0), so Mantione–Torres
Proposition 2 excludes PSC on \(V\); hence \(s>0\) is impossible. If \(s\equiv0\), Bourguignon's theorem (a scalar-flat metric on a
manifold carrying no PSC metric is Ricci-flat; \cite{kotschick2004monopole}, appendix) makes \(g_0\) Ricci-flat, and then
\(\pi_1(V)\) is virtually abelian (\cite{barbara2020fundamental}, Thm 2.7), impossible for a cocompact lattice in \(PU(2,1)\).
So \(s<0\) constant, and by §0.8 the metric is Einstein or non-Bach-flat. It is a global minimizer because it attains
\(p_*(V)\). \(\square\)

*Dependency summary.* \(\mathrm{H_{dec}}\) supplies PSC of the hypothetical Γ-carrying bubble cap; essentialness excludes that
vertex; ordinary connected-sum vanishing then eliminates every positive bubble intersection form; the charge bound and
Freedman finish (i)–(ii); essentialness, Bourguignon and virtual abelianness give \(s<0\) in (iii). Lemma 54.3 and the
identity \(SW_{V\#\Sigma}=SW_V\) are not used.

**Remarks on what has been gained.**

0. *Hypothesis accounting (superseded for ball-quotient hosts, Steps 87–90).* The original remark isolated an indefinite
   subcase \(b^+(R)=0\) in which \(\mathrm{H_{dec}}\) and Lemma 54.3 were used. In the Γ-vertex proof that subcase cannot occur:
   every bubble complement contains the essential vertex \(Y\) with \(b^+(Y)\ge3\). \(\mathrm{H_{dec}}\) is used only to exclude a
   Γ-carrying bubble cap.

1. The exclusion of smooth bubbling uses only lower semicontinuity, decay and topology. It needs neither the
   second-order kernel coefficient, nor energy equality, nor the moving-bubble argument. It holds uniformly for every
   non-fake-plane ball quotient at once. The mechanism: the analytic CH cell puts \(p_*(M)\) strictly below the cheapest
   topologically nontrivial smooth bubble. Lemma 54.1 shows the cheapest such bubble costs \(8\pi^2\) — semidefinite
   forms by the two-orientation charge, indefinite forms by essentialness of the Γ-vertex plus connected-sum vanishing,
   \(\pi_1\) by free indecomposability.
2. The Kähler recovery picture (KE ball quotient \(+\) Burns bubble, cost \(\to8\pi^2\)) and the neck-pinch picture
   \(X\sqcup(\overline{\mathbb{CP}}^2,g_{FS})\), both Einstein with \(P=0\), are excluded. The first is excluded by (U). The
   second is excluded because the connecting neck has \(e=2\) and costs \(\ge32\pi^2\). The verifier's Schwarzschild value
   and A01's baseline confirm this number.
3. Problem-level consequence. Under the gates, \(p_*(X\#\overline{\mathbb{CP}}^2)\) is attained (modulo exotic homotopy-sphere
   bubbles) by a smooth constant-negative-scalar \(P\)-critical global minimizer. Either it is Einstein, answering
   Problem 1 at \(k=1\) affirmatively in a range LeBrun's \(k\ge A/3=c_2\) obstruction leaves open. Or it is non-Bach-flat,
   answering Problem 3. Its value satisfies \(p_*(M)<8\pi^2(1-9\epsilon^2\log(1/\epsilon)+O(\epsilon^2))\) for every admissible
   \(\epsilon\), so the minimizer is strictly cheaper than every CH-plus-Burns configuration.
4. Entropy does not decide the dichotomy (script, `BCG_Bishop`). For an Einstein \(g\) with \(\operatorname{Ric}=-6g\) on \(M\), the
   BCG volume-entropy inequality with Bishop's bound \(h\le3\sqrt2\) against \(h(\mathbb{CH}^2)=4\) gives only
   \(\operatorname{Vol}(g)\ge(64/81)\operatorname{Vol}(X)\). LeBrun's scalar estimate \(\int s^2\ge32\pi^2A\) already gives the
   stronger \(\operatorname{Vol}(g)\ge\operatorname{Vol}(X)\). Topology gives only the upper bounds
   \(\operatorname{Vol}(g)/\operatorname{Vol}(X)\le3-1/c_2\) (from \(T_+\)) and \(\le2+2/c_2\) (from \(\chi\)), so the window is
   nonempty. A side remark (direction corrected after verification): for Einstein \(g\) on \(M\),
   \(\int|W^+|^2-\int s^2/24=2\pi^2(A-1)-\int s^2/16\le-2\pi^2\). So any Einstein metric on \(M\) has \(W^+\)-energy strictly
   **below** the Kähler-type value \(\int s^2/24\). Equality would force \(\operatorname{Vol}=(1-\frac1{3c_2})\operatorname{Vol}(X)\),
   which LeBrun's estimate excludes. The real-hyperbolic Sambusetti mechanism does
   not transfer: complex-hyperbolic entropy \(4\) is not extremal among \(\operatorname{Ric}\ge-6\) metrics (\(3\sqrt2\)).

**Extension to general \(k\) (same hypotheses, \(M_k=X\#k\overline{\mathbb{CP}}^2\)).** Disjoint analytic cells give
\(p_*(M_k)<8\pi^2k\) for every fixed \(k\). The same proof shows that in a smooth-point configuration
\[
\sum_k\big[4(e_k-1)+4b_1(\widehat N_k)+\beta(\widehat N_k)\big]<k,\qquad
\beta=\max\{b^--5b^+,\,b^+-5b^-,0\},
\]
with \(b^+(\widehat N_k)=0\) for every bubble (Γ-vertex Steps 0–2 apply verbatim for every \(k\), \(b^+(M_k)\ge3\); Lemma 54.3 not needed). Hence \(\sum_kb_2(\widehat N_k)<k\): **not all
exceptional classes can escape into smooth bubbles**, and the bulk is connected (all \(e_k=1\)) as soon as
\(p_*(M_k)<32\pi^2\). Converting this into attainment for \(k\ge2\) needs strict subadditivity
\(p_*(M_k)<p_*(M_{k-m})+8\pi^2m\) at bulk minimizers, which is the second-order kernel problem of Step 53 §4.

---

## 3. The remaining gates, stated as mathematics

**(G1) Collapse (case II).** Scalar curvature alone cannot exclude it: finite-volume complex-hyperbolic cusps collapse
with bounded curvature and constant \(s<0\). The relevant questions are topological and charge-theoretic.

- *Proved here.* A region \(C\) carrying a free circle action has \(TC\cong\pi^*TB\oplus\underline{\mathbb R}\), with \(B\) an
  orientable 3-manifold, so \(TC\) is trivial and \(w_2(C)=0\). Every class in the image of \(H_2(C)\to H_2(M)\) therefore has
  even square (Wu), and \(E\) (\(E^2=-1\)) is not carried by such a region.
- *Open.* (a) The same statement for positive-rank \(F\)-structures with finite isotropy (Seifert-type pieces). (b) The
  case where \(E\) is split between \(\Omega\) and \(C\): the Mayer–Vietoris intersection form across the graph-manifold
  interface \(\partial\Omega\). (c) Pricing the case-(II) energy loss with the Hopf-adiabatic charges of Theorem G. Anderson's
  case-(II) inequality is only \(\le\), but \(\mathrm{H_{lsc}}\) is all that (i) needs, so (i)'s argument applies verbatim to
  the bubbles of \(\Omega\).

**(G2) Orbifold points.** Here \(E\) can be absorbed only together with an \(X\)-class: roots \(a+mE\) with
\(a^2=m^2-2\), \(a\in H_2(X)\). Kronheimer bubbles cost zero, so the bound must come from the orbifold bulk. The
lattice-free part of the argument above carries over. If the orbifold bulk is good (a global quotient \(\tilde V/G\)),
an orbifold SW package gives a LeBrun bound that is useless here (\(1-A/3<0\)). Pricing must instead come from the CH-germ
interaction (A01's \(S^4/\mathbb Z_2\) baseline \(8\pi^2\) per class). Note that absorption of \(E\) needs \(m\) odd, hence
\(a^2\) odd; for \(m=1\), \(a^2=-1\). So the intersection form of \(X\) must be odd with a class of square \(-1\). The parity
lemma (52.9(v)) makes such absorbing orbifolds non-Kähler. **[Corrected:]** \(a^2=m^2-2\) alone does not force \(m\)
odd. Even \(m\) (e.g. \(a+2E\), \(a^2=2\)) is lattice-allowed. "Absorbing \(E\)" needs a precise definition and an
integral interface computation before any parity statement; the inference to a square-\(-1\) class is withdrawn.

**(G3) Analytic gates.** \(\mathrm{H_{lsc}}\) is standard for weak \(W^{2,2}\) convergence on compact regions at separated
scales. \(\mathrm{H_{dec}}\) needs (a) that bubbles of Anderson's perturbed sequence are critical for \(P\) itself; the
rescaled perturbation coefficient \(\varepsilon\ell^{4-4p}\) must tend to zero, which is the point the strategist and
verifier flag. It also needs (b) a decay theorem for scalar-flat Bach-flat AE ends with trivial group. With \(s=0\)
established, (b) needs only some \(\tau>0\) with derivative control; Bando–Kasue–Nakajima-type arguments for
\(L^2\)-curvature critical ALE limits give order 0, so an improvement is needed. \(\mathrm{H_{eq}}\) (Anderson (4.43)) and
\(\mathrm{H_{rem}}\) are used only in (iii).

**Gate economy.** (i)–(ii) need \(\mathrm{H_{sm}},\mathrm{H_{lsc}},\mathrm{H_{dec}}\) only. The analytic point that must be
proved with our own tools is \(\mathrm{H_{dec}}\)(a): bubble-scale criticality, i.e. the vanishing of the rescaled perturbation.
A route: choose \(p=p(\varepsilon)\downarrow1\) with \(\varepsilon\,\ell_{\min}(\varepsilon)^{4-4p}\to0\). Here
\(\ell_{\min}\) is the smallest \(L^6\)-curvature radius. A lower bound \(\ell_{\min}\ge\exp(-C/\varepsilon)\) would suffice
with \(p-1=o(\varepsilon)\), since then \(\varepsilon\ell^{4-4p}\le\varepsilon e^{4C(p-1)/\varepsilon}\to0\). Such a lower
bound plausibly follows from the energy bound \(\int|\operatorname{Ric}|^{2p}\le C/\varepsilon\) via the \(L^{2p}\)
\(\varepsilon\)-regularity at scale \(\ell\): \(\ell^{4p-4}\int_{B_\ell}|\operatorname{Ric}|^{2p}\ge c\) forces
\(\ell^{4-4p}\le C/(c\varepsilon)\), so \(\varepsilon\ell^{4-4p}\le C/c\) is merely bounded. The bubble equation then carries a
bounded zeroth-order perturbation \(\kappa\,\nabla\!\int|\operatorname{Ric}|^{2p}\), and \(\kappa\to0\) requires a sharper
choice. This is the precise open analytic estimate, recorded rather than claimed.

**[Superseded in part by §5(c): the compact-replacement argument gives bubble \(P\)-criticality directly. The verifier's
estimate \(\varepsilon_iQ_p(g_i)\le I_{\varepsilon_i}-p_*+o(1)\to0\) for genuine smooth near-minimizers makes
\(\kappa_i\to0\) at any scale with a Ricci lower bound. The scaling identity below remains a valid alternative under
\(\mathrm{H_{eq}}\).]**

**Proposition 54.4 (bubble-scale criticality from a scaling identity).** Fix \(p>1\) as in
Anderson. Let \(\hat g_i=\ell_i^{-2}g_{\varepsilon_i}\) be a bubble rescaling (\(\ell_i\to0\)) converging to a nonflat
complete limit \(N\), and put \(\kappa_i=\varepsilon_i\ell_i^{4-4p}\). Then:

(a) **\(\kappa_i\) is bounded** whenever \(\operatorname{Ric}_N\not\equiv0\). Indeed
\(\kappa_i\int_{B_R}|\operatorname{Ric}_{\hat g_i}|^{2p}\le\varepsilon_i\int_M|\operatorname{Ric}_{g_{\varepsilon_i}}|^{2p}\le\mathcal Z_{\varepsilon_i}\le C\),
and the left integral has a positive liminf by lower semicontinuity.

(b) **Scaling (Pohozaev) identity.** Test the Euler–Lagrange equation of \(\hat g_i\) with the conformal variation
\(\phi_R\hat g_i\). Here \(\phi_R=1\) on \(B_R\), \(\phi_R=0\) off \(B_{2R}\), \(|\nabla^2\phi_R|\lesssim R^{-2}\). The perturbed
functional is \(P+\kappa_i\int(\ell_i^4+|\operatorname{Ric}|^2)^p+\) a volume multiplier \(\mu_i\ell_i^4\operatorname{Vol}\), with
\(\mu_i=O(1)\). Since \(P\) is scale invariant, its conformal variation is \(\delta P(\phi)=-2\int\langle\operatorname{Ric}^\circ,\nabla^2\phi\rangle\).
The perturbation's constant-scaling derivative is \((2-2p)\int|\operatorname{Ric}|^{2p}\) up to \(O(\ell_i^4)\). This gives
\[
(2p-2)\,\kappa_i\!\int_{B_R}\!|\operatorname{Ric}_{\hat g_i}|^{2p}
\ \lesssim\ \Big(\int_{A_R}|\operatorname{Ric}^\circ_{\hat g_i}|^2\Big)^{1/2}
+\kappa_i^{1/(2p)}R^{-(2p-2)/p}+O(\ell_i^4R^4),
\]
using Hölder on the annulus \(A_R=B_{2R}\setminus B_R\) together with \(\kappa_i\int|\operatorname{Ric}|^{2p}\le C\).

(c) With case-(I) no-neck energy (\(\mathrm{H_{eq}}\): the \(L^2\) Ricci energy in the neck annuli between the bubble scale
and the parent scale tends to zero), let \(i\to\infty\) and then \(R\to\infty\). This gives
\(\lim\kappa_i\cdot\int|\operatorname{Ric}_N|^{2p}=0\). Hence \(\kappa_i\to0\) or \(\operatorname{Ric}_N\equiv0\). In both cases the limit
equation is that of \(P\): the perturbation gradient tends to zero in distributions, since
\(\kappa_i\int|\operatorname{Ric}|^{2p-1}|\nabla^2\psi|\le C\kappa_i^{1/(2p)}\to0\). By the Step-51/52 trace argument the
limit is then scalar-flat (\(\Delta s=0\), \(s\in L^2\)).

So the strategist's caution is answered. The rescaled perturbation is automatically bounded, and the scaling identity
forces it to vanish on every bubble that is not Ricci-flat. The remaining analytic input is the passage to the limit in
the quadratic curvature terms of the \(P\)-equation. This needs strong local \(L^2\) curvature convergence, which follows
from \(L^q\) curvature control with \(q>4\) and the Prop. 52.1 bootstrap. Together with decay, it is what is left of
\(\mathrm{H_{dec}}\). Note that 54.4 uses \(\mathrm{H_{eq}}\), whereas Theorem 54.A(i) does not.

---

## 4. Answer to A01 #825 (local KE rigidity near \(g_\Gamma\))

On \(\mathbb{CH}^2\) (\(\operatorname{Ric}=-6g\)) the curvature action \(\mathring R\) on trace-free symmetric 2-tensors has
eigenvalues \(-2\) (J-invariant, dim 3) and \(+4\) (J-anti, dim 6) (Step 44, `step44_perturbative_ke.json`). The eigenvalues
alone do not give the gap. The TT Codazzi–Bochner identity \(\|\nabla h\|^2\ge\langle\mathring Rh,h\rangle+6\|h\|^2\) does, as an
**integrated** (not pointwise) estimate: \(\langle(\nabla^*\nabla-2\mathring R)h,h\rangle\ge2\|h\|^2\) on TT tensors. Hence there are no
infinitesimal Einstein deformations, and by Koiso's local rigidity theorem every Einstein metric sufficiently
\(C^{2,\alpha}\)-close (or \(H^s\), \(s>4\), in Bianchi gauge) to \(g_\Gamma\) is isometric to it up to scale. The gap is integrated
and \(\Gamma\)-independent, and Lemma M (Step 45–46) supplies quotient-uniform \(L^\infty\)/Hölder inverses, so the closeness
threshold is uniform over finite covers in the uniformly-local Hölder norm. \(H^2\)-closeness is not enough
(\(H^2\not\subset L^\infty\)). Theorem \(A_C\) is a statement about the canonical monopole branch and is not needed for this
rigidity. For a general negative KE surface (not a ball quotient), Koiso shows that infinitesimal Einstein deformations
are infinitesimal complex deformations. Einstein metrics near a KE metric are KE for a nearby complex structure when the
Kuranishi space is smooth. In general this is the remaining condition.


---

## 5. Verification outcome (binding; `trace/ttcs/results/step54_ttcs01_verifier1_integration.md`)

The verifier confirmed the following:

- the charge formula, with the Schwarzschild value \(32\pi^2\);
- the summand decomposition (2) for arbitrary graphs;
- Lemma 54.3, including the case \(b^+(R)=0\), via the one-sided PSC neck argument (an exact citation is still to be
  registered; **not used** in the Steps 87–90 proof of Theorem 54.A, retained as a standalone [P*] statement);
- the \(\pi_1\)/Hopf/Freedman chain;
- part (iii): \(SW_{V\#\Sigma}=\pm SW_V\), \(s<0\) constant, the Einstein/non-Bach-flat dichotomy, and the no-bubble
  conclusion for standard caps (the SW transfer is **superseded**: \(s<0\) now follows from essentialness, Bourguignon and
  virtual abelianness, §2);
- the BCG arithmetic and the Koiso gap \(2\) (integrated form).

It also confirmed that (U) holds for **every** compact ball quotient, fake planes included: Ch. 5 builds the cell for
every fixed \(R>0\). Corrections applied above: the order of proof (SW first), Remark 4's direction, orbifold parity,
and the Koiso wording. Additional results recorded:

**(a) Degree-one strengthening, general \(k\).** The blowdown \(M_k\to X\) is a classifying map. By free indecomposability,
exactly one vertex cap \(Y\) carries \(\Gamma\), and \(Y\to X\) has degree one, so \(Q_X\hookrightarrow Q_Y\) and
\(b^+(Y)\ge b^+(X)\ge3\). That vertex is bulk: if it were a bubble cap it would carry PSC (\(\mathrm{H_{dec}}\), Lemma 53.Y), contradicting essentialness (\cite{mantionegeographya}); this ordering (Step 87) is what then makes every bubble complement have \(b^+\ge3\) and every bubble \(b^+=0\). Hence **every bubble cap is simply connected**
for every \(k\), and the \(H_2\)-image of the bubbles lies in \(\operatorname{span}\{E_1,\dots,E_k\}\). With
\(p_*(M_k)<8\pi^2k\):
\[
\sum_j[4(e_j-1)+4b_1(\widehat N_j)+b_2(\widehat N_j)]<k ,
\]
so the total exceptional rank in smooth bubbles is \(<k\), and all bubbles are one-ended for \(k\le4\).

**(b) Hypothesis ledger.**

| Conclusion | Hypotheses |
|---|---|
| (U) | Ch. 5 cell only |
| \(b^+(\widehat N_k)=0\) | \(\mathrm{H_{sm}}\), summand topology, \(\mathrm{H_{dec}}\) (PSC of caps, used only to show the Γ-vertex is bulk) + \cite{mantionegeographya}; then ordinary connected-sum vanishing (Step-87 order; Lemma 54.3 not used) |
| one-ended, homologically trivial, simply connected bubbles; connected bulk \(V\approx M\) | add (U), \(\mathrm{H_{lsc}}\) |
| \(P(g_0)=p_*(V)\) | add \(\mathrm{H_{rem}}\), \(\mathrm{H_{eq}}\) |
| \(s<0\), Einstein/non-Bach-flat | essentialness of \(V\) (no PSC, \cite{mantionegeographya}), Bourguignon, virtual abelianness (\cite{barbara2020fundamental}); the PSC-homotopy-sphere SW gluing is no longer needed |
| attainment on \(M\), no bubbles | all caps \(\cong S^4\) |

\(\mathrm{H_{eq}}\) becomes redundant if vanishing-error reassembly is proved (reassembly gives \(\le\), and \(\mathrm{H_{lsc}}\)
gives \(\ge\)).

**(c) Bubble criticality by compact replacement.** Suppose the actual smooth \(P\)-minimizing sequence converges smoothly
on compact sets at a bubble scale. A compactly supported \(P\)-lowering variation of the bubble, transplanted into
\(g_i\), would give \(P<p_*\). So the bubble locally minimizes \(P\), hence is \(P\)-critical, has \(s\equiv0\), and is Bach-flat.
This needs neither \(\mathrm{H_{eq}}\) nor \(\kappa\to0\). The genuine analytic residue of \(\mathrm{H_{dec}}\) is therefore:
smooth (or strong enough) compact convergence at bubble scales, plus derivative-controlled AE decay of some order
\(\tau>0\) for scalar-flat Bach-flat AE ends with trivial group.

**(d) What remains geometrically.** Theorem 54.A excludes all homologically or topologically charged smooth bubbling on
\(X\#\overline{\mathbb{CP}}^2\). The geometries still open are:

1. collapse (case II);
2. nontrivial-group orbifold points (absorption);
3. nonflat bubbles whose caps are exotic homotopy spheres, which would also disprove smooth 4D Poincaré.
