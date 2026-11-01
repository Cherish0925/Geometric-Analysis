# Step 53 — Anderson's idealized minimizers as the entrance; attainment transfer under smooth bubbling; first-order bubble exclusion; reduction of the non-Bach-flat optimum problem

Session S1003A02, Agent2, Execute. Conventions: \(P(g)=\int|\operatorname{Ric}^\circ|^2\), operator norms on \(\Lambda^2\);
\(\mathbf R^\pm=W^\pm+\tfrac s{12}I\) on \(\Lambda^\pm\); \(\mathcal K(g)=\int|\mathrm{Rm}_{\rm op}|^2=8\pi^2\chi+P\) on closed \(M\)
(five_research_problems.tex eq. (fullP)). Sources read this step: the 2026-10-07 supplements
(`Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/five_research_problems.tex` §§1–3,
`web_research_collected.tex` Ch. 5 and Ch. 7), Anderson, *Canonical metrics on 3-manifolds and 4-manifolds*,
Asian J. Math. 10 (2006) (Knowledge object `Canonical-Metrics-on-3-Manifolds-and-4-Manifolds--8d02c53d4380--0b5d0f7e0ac4`,
Thm 4.1, Cor 4.4, Lemma 4.5, Prop 4.6, (4.32)–(4.33), Cor 4.8, Thm 4.10 and its proof, Remark 4.12, (4.65)),
Tian–Viaclovsky, *Bach-flat ALE metrics* Thm 1.1/1.3 (Knowledge object `Bach-flat-asymptotically-locally-Euclidean-metrics--3c3dd988289c`),
and our Theorem F (`step20_burns_response_and_neck_quantization.md` §1).

This note supersedes the Step-52 framing in which "step 0" (an own-scale regularization of *arbitrary* minimizing
sequences) was the open entrance. For existence and structure questions one only needs **some** minimizing sequence
with controlled structure, and Anderson's Theorem 4.10 is an existing theorem providing one. The Step-52 residual
analysis remains correct as a statement about arbitrary sequences; it is no longer on the critical path.

---

## 1. The entrance: Anderson's perturbed minimizers

Anderson perturbs exactly our functional:
\[
\mathcal Z^{2p}_\varepsilon(g)=\int\Big(|\operatorname{Ric}|^2-\tfrac14s^2\Big)+\varepsilon\int(1+|\operatorname{Ric}|^2)^p
=P(g)+\varepsilon\int(1+|\operatorname{Ric}|^2)^p ,\qquad p>1 \text{ close to }1,
\]
on unit-volume metrics ((4.32)). A bound on \(\mathcal Z^{2p}_\varepsilon\) bounds \(\int|\operatorname{Ric}|^{2p}\), so his
Theorem 4.1 (convergence under \(L^{2p}\) Ricci bounds) produces minimizing pairs \((\Omega_\varepsilon,g_\varepsilon)\)
(Cor 4.4/4.8); local minimizers are \(L^{2,4}\) (Lemma 4.5) and \(C^\infty\) (Prop 4.6, via the decomposition
\(h=\delta^*X+\phi g+k\) and the elliptic Euler–Lagrange system (4.33)). Since \(P\) is scale invariant and every fixed
smooth \(g\) has \(\varepsilon\int(1+|\operatorname{Ric}_g|^2)^p\to0\), these are minimizing for \(P\) at cost \(o(1)\): this is
the Sacks–Uhlenbeck mechanism, and it replaces the flow-based entrance of Steps 50–52. The sixth-order objection of
Step 19 does not apply: the perturbation is zeroth order in curvature, and the Euler–Lagrange equation stays fourth
order with uniform elliptic estimates on each summand as \(\varepsilon\to0\) once \(C^\alpha\) harmonic control holds
((4.49), proved by contradiction from the \(L^q\)/\(L^2\) curvature radii).

**Theorem 4.10 (Anderson), specialized to \(P\).** For every closed oriented 4-manifold \(M\) there is a minimizing
sequence \(g_i\) for \(P\) (unit volume) converging in pointed Gromov–Hausdorff sense to one of:

- **(I)** a compact, possibly reducible orbifold \((V,g_0)\), \(\operatorname{vol}V=1\), \(g_0\) smooth on \(V_0\) and
  \(C^0\) across the singular points (which may have \(\Gamma=\{e\}\)), together with ALE spaces \((N_k,g^k_\infty)\)
  associated with the singular points, with **energy equality**
  \(\mathcal F(g_0)+\sum_k\mathcal F(N_k)=\inf\mathcal F\);
- **(II)** a maximal orbifold domain \(\Omega\subset\subset M\) (possibly empty) with the inequality \(\le\) in place of
  equality and \(F\)-structure collapse outside a compact set.

In both cases \(\nabla\mathcal F(g_0)=0\) and \(g_0\) minimizes \(\mathcal F\) among compact perturbations. In case (I),
\(M\) is the generalized connected sum of \(V_0\) with the ALE spaces along spherical space forms ((4.65)).

**Lemma 53.0 (the energy equality is the \(P\)-ledger).** In case (I),
\[
p_*(M)=P(V,g_0)+\sum_kP(N_k).
\]
*Proof.* For an orbifold \(V\) and a (possibly orbifold) ALE space \(N\) with group \(\Gamma\) at infinity, Chern–Gauss–Bonnet
reads \(\int|\mathrm{Rm}_{\rm op}|^2=8\pi^2\chi_{\rm orb}+P\), with \(\chi_{\rm orb}(V)=\chi(V)-\sum_j(1-|\Gamma_j|^{-1})\) and
\(\chi_{\rm orb}(N)=\chi(N)-|\Gamma|^{-1}-\sum(\text{interior defects})\). Gluing along \(S^3/\Gamma\) (Euler characteristic 0)
gives \(\chi(M)=\chi(V)-\#\{\text{sing}\}+\sum\chi(N_k)\) at one level, and the \(|\Gamma|^{-1}\) terms cancel pairwise; by
induction on the depth of the bubble tree the Euler terms sum to \(8\pi^2\chi(M)\). Subtracting from Anderson's equality
for \(\mathcal R^2=\mathcal K\) gives the claim. \(\square\)

The same telescoping is the Theorem-G characteristic ledger at the level of Euler terms; the signature/eta ledger
(Step 52, Prop 52.10) is the companion statement for \(T_\pm\).

**What is used from the source, and where its proof is delicate.** (a) The local-minimality of the Cor-4.4 limit pair
among compact perturbations is asserted from a weak \(L^{2,2p}\) limit; a complete proof needs strong convergence
(uniform convexity of \(\int(1+|\operatorname{Ric}|^2)^p\) in \(\partial^2g\), as in Sacks–Uhlenbeck). (b) The case-(I) energy
equality (4.43) is derived by citation to the orbifold compactness/no-neck theory ([8],[9],[11] there); Remark 4.12 lists
the corresponding case-(II) equality as a conjecture. (c) Removability of \(\Gamma=\{e\}\) points and smoothness of
\(g_0\) in orbifold charts use finite-energy removable-singularity theory for critical metrics (Tian–Viaclovsky). We use
Theorem 4.10 as stated, with these dependencies recorded; every result below is stated as conditional on it.

---

## 2. Reassembly and gluing

**Lemma 53.R (reassembly).** Let a case-(I) configuration be given, and suppose each ALE space \(N_k\) has an end of
order \(\tau_k>0\). For any choice of gluing scales \(\lambda_k\to0\) (each tree glued recursively, scales separated) the
glued metrics \(g_\lambda\) live on \(M\) and satisfy \(P(g_\lambda)\to P(g_0)+\sum_kP(N_k)=p_*(M)\). The same holds if any
smooth closed component of \(V\) carries an arbitrary fixed smooth metric \(h\) in place of \(g_0\), with \(P(g_0)\) replaced
by \(P(h)\) for that component.

*Proof sketch.* Topology: (4.65). Energy: on a cut annulus \(\{r\sim r_0\}\) at a gluing point the glued metric is
\(g_0+O(r^2)\) on the bulk side and \(g_N^{\lambda}=\delta+O(\lambda^\tau r^{-\tau})\) on the bubble side; with a cutoff the
curvature error is \(O(1+\lambda^\tau r_0^{-\tau-2})\) on volume \(O(r_0^4)\), so the cut cost is \(O(r_0^4+\lambda^{2\tau}r_0^{-2\tau})\to0\)
for \(\lambda\ll r_0\to0\); outside the annuli the metrics are the unperturbed pieces up to errors that vanish with
\(r_0,\lambda/r_0\). \(\square\)

**Theorem 53.F′ (first-order response of an anti-self-dual scalar-flat AE bubble; general bulk).** Let \((N,g_N)\) be a
complete AE (\(\Gamma=\{e\}\)) manifold with \(W^+_{g_N}\equiv0\), \(s_{g_N}\equiv0\), and an AE chart
\(g_N=\delta+h_2+O(r^{-2-\delta})\) (with derivatives) where \(h_2\) is homogeneous of degree \(-2\). Define its chiral flux
\[
\Phi^{++}(N)=-\int P_+\mathcal R^{\rm lin}_\delta(\chi h_2)P_+\,dx\quad(\text{a symmetric endomorphism of }\Lambda^+_0),
\]
which is independent of the cutoff \(\chi\) because \(P_+\mathcal R^{\rm lin}(h_2)P_+=0\) and \(s^{\rm lin}(h_2)=0\) pointwise
(the degree \(-4\) parts of \(W^+_{g_N}=0\), \(s_{g_N}=0\)). Let \((V,g)\) be closed, \(p\in V\), and let
\(U\in SO(4)\) identify \(T_pV\) with \(\mathbb R^4\); \(U\) acts on \(\Lambda^+\) through \(SO(3)\). Gluing \(N\) at \(p\) at
scale \(\lambda\) (\(g_N\mapsto\lambda^2g_N\)) with cutoff radius \(r_0=\lambda^{2/5}\) gives, on \(V\#\widehat N\),
\[
\boxed{\;P(\hat g_\lambda)=P(g)+P(N)-8\lambda^2\big\langle\mathbf R^+_p,\;U\Phi^{++}(N)U^{T}\big\rangle+O(\lambda^{12/5}).\;}
\]
For Burns (\(\lambda^2=x_0\)) \(\Phi^{++}=\pi^2w_1w_1^T\) and this is Theorem F.

*Proof.* Identical to Theorem F (§1 of the Step-20 note) with two observations. (i) The exact topological reduction
\(P(\hat g)-P(g)=4\Delta\!\int|W^+|^2+\tfrac1{12}\Delta S-8\pi^2(T_+(\widehat N)-4)\), and the same identity on \(N\) itself,
give \(P(\hat g)-P(g)-P(N)=4\Delta W^++\tfrac1{12}\Delta S-4\int_N|W^+_N|^2-\tfrac1{12}\int_Ns_N^2\), and the last two
terms vanish. (ii) In the core and intermediate regions the mixed finite difference argument uses only
\(W^+(\lambda^2g_N)=s(\lambda^2g_N)=0\) identically and the decay \(\lambda^2r^{-2}\) of the tail; the cut annulus produces
\(-2\lambda^2\langle W^+_p,U\Phi^{++}U^T\rangle\) and \(-2\lambda^2s_pF_s\) with \(F_s=4\operatorname{tr}\Phi^{++}\), which assemble
to \(-8\lambda^2\langle\mathbf R^+_p,U\Phi^{++}U^T\rangle\). \(\square\)

By von Neumann's trace inequality, with eigenvalues ordered decreasingly,
\[
\max_{U}\big\langle\mathbf R^+_p,U\Phi^{++}U^T\big\rangle=\sum_{i=1}^3\lambda_i(\mathbf R^+_p)\,\mu_i(\Phi^{++}(N))=: \mathfrak r_N(p).
\]
For Burns, \(\mathfrak r_N(p)=\pi^2\lambda_{\max}(\mathbf R^+_p)\). If \(W^+_N\not\equiv0\) the cross term
\(2\langle W^+_g,W^+(\lambda^2g_N)\rangle\) in the core is of order \(\lambda^2\log(1/\lambda)\) whenever the \(r^{-4}\) tail of
\(W^+_N\) has nonzero spherical mean; the response of non-ASD bubbles must be computed separately.

---

## 3. Bubble exclusion and attainment transfer

Throughout this section a case-(I) configuration is fixed, and the hypotheses of Lemma 53.R hold.

**Theorem 53.B (first-order bubble exclusion).** Suppose the configuration contains a bubble tree at a smooth point
whose outermost bubble \(N\) satisfies the hypotheses of Theorem 53.F′. Then for every component \(V_a\) of \(V\) and every
regular point \(p\in V_a\),
\[
\mathfrak r_N(p)=\sum_i\lambda_i(\mathbf R^+_{g_0}(p))\,\mu_i(\Phi^{++}(N))\le0 .
\]
If \(N\) is Burns, or more generally if \(\widehat N\cong\overline{\mathbb{CP}}^2\) and \(N\) is ASD scalar-flat with
rank-one flux, then \(\mathbf R^+_{g_0}\le0\) on every component of the bulk.

*Proof.* Let \(M'\) be the reassembled configuration without that tree; \(M'\) is connected and \(M\cong M'\#\widehat T\),
\(\widehat T\) the compactified tree. The connected sum with \(\widehat T\) at any point and through any orientation-preserving
frame is well defined up to diffeomorphism (Palais), so gluing the tree at \(p\) with frame \(U\) still gives \(M\). Glue all
other trees by Lemma 53.R at scales tending to 0 first; then glue the tree at \(p\) with optimal \(U\) and a small fixed
\(\lambda\). By Lemma 53.0, Lemma 53.R and Theorem 53.F′,
\(P(\hat g)=p_*(M)-8\lambda^2\mathfrak r_N(p)+O(\lambda^{12/5})+o(1)\). If \(\mathfrak r_N(p)>0\), fixing \(\lambda\) small and then
sending the other scales to zero gives \(P(\hat g)<p_*(M)\). \(\square\)

The point is that a minimizing configuration cannot leave first-order interaction energy unused: a bubble that has
concentrated somewhere may be glued back anywhere, and the energy equality makes the configuration value the
competitor's zeroth-order value.

**Corollary 53.C (curvature of the bulk when \(\overline{\mathbb{CP}}^2\)-bubbling occurs).** Suppose a Burns-type bubble
occurs. Since \(g_0\) is \(P\)-critical, \(\operatorname{tr}\nabla P=-\tfrac12\Delta s\) forces \(s_0\) constant on each component.
Then on every component:

1. \(s_0\le0\) (since \(\operatorname{tr}\mathbf R^+=s/4\));
2. if \(s_0=0\), then \(W^+\equiv0\): the component is scalar-flat anti-self-dual;
3. if \(s_0<0\), then \(\lambda_{\max}(W^+)\le|s_0|/12\), hence \(|W^+|^2\le s_0^2/24\) pointwise, with equality exactly at
   points where \(W^+\) has the Kähler spectrum \((|s|/12,|s|/12,-|s|/6)\); consequently
   \(P(g_0|_{V_a})\le\tfrac14\int_{V_a}s_0^2-8\pi^2T_+^{\rm orb}(V_a)\);
4. no component contains an open set on which \(g_0\) is complex hyperbolic. (On such a ball the Chapter-5 cell of the
   2026-10-07 collection — exact CH outside a fixed collar, \(P/(8\pi^2)=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2)\) —
   replaces the bubble. Every AE bubble with \(\widehat N\cong\overline{\mathbb{CP}}^2\) costs \(P(N)\ge8\pi^2\) by the AE cost
   formula \(P_N=4\int|W^+|^2+\tfrac1{12}\int s^2+8\pi^2b_2+32\pi^2b_1\). Hence the replacement lowers the total below \(p_*(M)\).)

The Kähler–Einstein bulk is exactly the borderline of item 3: \(\mathbf R^+=\operatorname{diag}(s/4,0,0)\le0\) with a 2-sphere
of kernel directions. This is consistent with the fixed-complex-structure recovery sequence (KE canonical model plus
Burns bubbles, \(\inf_{\rm K\ddot ahler}P=8\pi^2k\)). Item 4 says that, for ball quotients, the unrestricted minimizing
configuration is never this one.

**Theorem 53.D (attainment transfer under smooth bubbling).** Suppose the configuration has no orbifold points with
\(\Gamma\ne\{e\}\). Then every component \(V_a\) of the bulk is a smooth closed 4-manifold, \(g_0|_{V_a}\) is smooth, and
\[
P(g_0|_{V_a})=p_*(V_a)\quad\text{for every }a,\qquad p_*(M)=\sum_ap_*(V_a)+\sum_kP(N_k).
\]
Thus each bulk component attains its own infimum. In particular \(p_*(M)\) is attained on \(M\) iff some configuration
is trivial (one component \(V\cong M\), no bubbles).

*Proof.* Smoothness at \(\Gamma=\{e\}\) points: removable singularities. Lemma 53.R with arbitrary smooth metrics
\(h_a\) on the components gives \(p_*(M)\le\sum_aP(h_a)+\sum_kP(N_k)\), hence, by Lemma 53.0,
\(\sum_aP(g_0|_{V_a})\le\sum_ap_*(V_a)\). The reverse holds termwise. \(\square\)

---

## 4. Consequence for the non-Bach-flat global optimum (Problem 3) and for Problem 2

**Lemma 53.Y (Yamabe sign of bubble compactifications).** If \(N\) is AE with \(s\equiv0\) and an end of order
\(\tau>1\), then its one-point compactification \(\widehat N\) has \(Y(\widehat N)>0\). (Multi-ended: compactify each end.)

*Proof.* In inverted coordinates \(\hat g=|y|^4g\) extends to a \(C^{1,\tau-1}\) metric with \(s_{\hat g}\in L^q\),
\(q>2\). The function \(u=|y|^{-2}(1+o(1))\) satisfies \(g=u^2\hat g\), so \(L_{\hat g}u=0\) away from the point and
\(L_{\hat g}u=24\pi^2\delta_0\) as a distribution. If the first eigenfunction \(\phi>0\) of \(L_{\hat g}=-6\Delta+s\) had
eigenvalue \(\lambda_1\le0\), then \(24\pi^2\phi(0)=\langle L u,\phi\rangle=\lambda_1\int u\phi\le0\), a contradiction.
Hence \(Y([\hat g])>0\); smooth approximation in \(W^{2,q}\) keeps \(\lambda_1>0\). \(\square\)

**Theorem 53.E (reduction of Problem 3).** Let \(M\) be closed with \(Y(M)<0\) (e.g. any \(M\) with a monopole class of
positive square, such as \(X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal of general type). Suppose \(P\) on \(M\) has a case-(I)
configuration without \(\Gamma\ne\{e\}\) points whose bubbles have ends of order \(\tau>1\). Then:

1. some bulk component \(V_a\) has \(Y(V_a)<0\); in fact \(Y(M)^2\le\sum_{a:\,Y(V_a)<0}Y(V_a)^2\);
2. on every such component \(g_0\) is a smooth global minimizer of \(P\) which is not scalar-flat;
3. if such a \(V_a\) carries no Einstein metric, \(g_0|_{V_a}\) is a non-Bach-flat global optimum of the total-curvature
   functional on \(V_a\) (five_research_problems.tex Prop. nonbach);
4. otherwise \(g_0|_{V_a}\) is Einstein.

*Proof.* \(M\) is the connected sum of the closed pieces \(V_a\), \(\widehat N_k\) along the gluing graph, together with one
\(S^1\times S^3\) per independent loop. Pieces of the second and third kind have positive Yamabe invariant
(Lemma 53.Y, and \(S^1\times S^3\)). By Kobayashi's connected-sum inequalities, if every \(V_a\) had \(Y\ge0\) then
\(Y(M)\ge0\), and the quantitative form gives item 1. Item 2 is Theorem 53.D together with the fact that \(Y<0\) excludes
scalar-flat metrics. Items 3–4 follow from Prop. nonbach and \(p_*=0\iff\) Einstein attainment. \(\square\)

So **smooth bubbling is no obstruction to Problem 3**. It moves attainment to a bulk manifold that inherits negative
Yamabe invariant. The genuine obstructions to a smooth non-Bach-flat optimum are only:

- (a) collapse (case II);
- (b) orbifold points with nontrivial \(\Gamma\), i.e. Kronheimer-type absorption (Step 52);
- (c) Einstein bulk components.

For \(M=X\#k\overline{\mathbb{CP}}^2\) the third alternative is itself constrained:

- An Einstein bulk \(V_a\) has \(Y(V_a)<0\), and \(Y(V_a)\le Y(M)\) if it is the only negative component.
- It must satisfy Hitchin–Thorpe and, where it carries a monopole class, LeBrun's and N1's obstructions. Which
  summand carries the basic classes needs a separate Seiberg–Witten connected-sum argument; that argument is not
  supplied here.
- If a Burns bubble is present, it must satisfy \(\lambda_{\max}(W^+)\le|s|/12\) (Cor 53.C).
- If \(X\) is a ball quotient and \(V_a\cong X\), Cor 53.C(4) excludes it whenever a \(\overline{\mathbb{CP}}^2\)-bubble is present.

**Consequence for Problem 2 (exact value of \(p_*(X\#k\overline{\mathbb{CP}}^2)\)).** Combine Theorem 53.D with
Theorem 53.B. In any noncollapsed, \(\Gamma\)-free degenerate minimizing configuration,
\(p_*(M)=\sum_ap_*(V_a)+\sum_kP(N_k)\), where the bulk minimizers lie in the cone \(\mathbf R^+\le0\) as soon as a
\(\overline{\mathbb{CP}}^2\)-bubble is present. The strict inequality that rules such a configuration out is therefore
\(p_*(V\#\overline{\mathbb{CP}}^2)<p_*(V)+8\pi^2\) at a minimizer of \(V\). It holds at first order whenever the minimizer has
\(\lambda_{\max}(\mathbf R^+)>0\) somewhere (Theorem F). It holds at second order on CH regions (Chapter 5). It is open
exactly for minimizers with \(\mathbf R^+\le0\) and no CH region. That borderline needs a general-background second-order
(kernel-direction) response formula, uniform in the background. This is the precise location where the "strictly below
every degeneration cost implies smooth attainment" mechanism must be completed.

---

## 5. Status

- **Proved here, conditional only on Anderson Thm 4.10 as stated plus standard gluing/removability:** Lemma 53.0,
  Theorem 53.F′, Theorem 53.B, Cor 53.C, Theorem 53.D, Theorem 53.E. Lemma 53.Y uses order \(\tau>1\). Tian–Viaclovsky give
  \(\tau<2\) arbitrary for ASD scalar-flat or harmonic-curvature ALE; for general Bach-flat scalar-flat ends only order 0
  is in their Thm 1.1, and higher order must be imported from later decay results.
- **Withdrawn framing:** "step 0 is the open entrance" (Step 52 §5) — not needed for existence/structure.
- **Open and decisive:**
  1. exclusion of collapse for \(Y(M)<0\);
  2. exclusion or pricing of nontrivial-\(\Gamma\) points (absorption);
  3. the second-order kernel-direction response in a general background with \(\mathbf R^+\le0\);
  4. responses of non-ASD bubbles.


---

## 6. Corrections after verification (Step 54)

The Step-53 verifier (`trace/ttcs/results/step53_ttcs01_verifier1_integration.md`) confirmed the Euler telescope, the
half-flat response, one-attachment exclusion, and attainment transfer, with the following corrections. They are binding
over §§1–4 above.

- Lemma 53.0: count cone branches at reducible vertices (truncated-piece proof).
- 53.B: one-attachment trees only. The flux must be positive; the positive-mass theorem gives
  \(\operatorname{tr}\Phi^{++}=3\pi^2m_{\rm ADM}>0\).
- 53.C: KE kernel directions form \(S^1\), not \(S^2\). Item 4 needs the CH-cell theorem with its collar-radius scope.
- 53.F′: the \(O(\lambda^{12/5})\) remainder needs the half-flat cancellation, and the homogeneous \(r^{-2}\) expansion is a
  hypothesis. The \(\lambda^2\log\) remark for non-ASD bubbles is deleted (zero spherical mean).
- 53.D: attainment ⇔ existence of a trivial generalized configuration.
- 53.Y: any order \(\tau>0\) with derivative control suffices.
- Prop. nonbach is replaced by: Bach-flat \(+\) \(P\)-critical \(+\) constant \(s\neq0\) ⇒ Einstein.
- Anderson's Prop 4.6 regularity and its uniformity under rescaling are soft points of the source.

The k=1 ball-quotient theorem built on these is in `step54_k1_ball_quotient_attainment_theorem.md`.
