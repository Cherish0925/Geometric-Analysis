# Step 56 — Orbifold-category attainment at k = 1, the zero-energy upper bound, and the local interaction at a Wahl point

> **Binding erratum (Steps 70, 86–88; see `theorem_package_v1.md` §§13, 17).** Written before the Step-70 functional split: \(p_*\) and \(\alpha_{\rm orb}\) in this note denote infima of \(P=\int|\mathrm{Ric}^\circ|^2\) (now \(P_*\), \(P_{*,\rm orb}\)), not of the human defect \(\mathscr D\). In §1(i) and Corollary 56.B, "\(p_*(M)=0\), so \(\alpha(M)=0\)" is valid for \(\mathscr D\) only when the orbifold Einstein constant is nonzero (Lemma 86.S: Milnor-fibre smoothing with Šuvaina's \(\tau=4\) metrics \cite{suvaina2011ale} preserves \(V,\int s,\int s^2,R\) up to \(O(\rho^4)\)). A Ricci-flat bulk gives \(P_*=0\) and a glued family with \(\mathscr D\to4\). On the negative-Yamabe manifolds treated here a Ricci-flat or positive-Einstein bulk cannot occur (\(\mathcal Y\ge-\|s^-\|_2\)), so an Einstein bulk has \(\lambda<0\). The \(O(\lambda^2)\) smoothing error is the established rate; no \(\lambda^4\) law is claimed.

Session S1003A02, Agent2, Execute. This note continues `step55_k1_orbifold_gate_charges_lattices_collapse.md` and makes
the Step-55 verifier corrections binding (§0). It then:
- states the orbifold-category theorem that the conservation law makes stable (§1);
- proves the unconditional zero-energy upper bound (§2);
- fixes the algebraic structure of curvature at a Wahl point (§3);
- computes the leading local interaction between a P-critical bulk and a Ricci-flat Wahl-type Milnor-fibre bubble (§4).

The result of §4 is negative for the cheap exclusion route. The \(\lambda^4\log(1/\lambda)\) interaction vanishes after the
spherical average, so no pointwise Biquard–Ozuch-type obstruction appears at the logarithmic order.

Scripts and data:
- `workspace/scripts/step56_Tpoint_local_structure.py` → `workspace/data/step56_Tpoint_local_structure.json`
  (Γ-invariant curvature, GH quadrupole phase test);
- `workspace/scripts/step56_Tpoint_log_interaction.py` → `workspace/data/step56_Tpoint_log_interaction.json`
  (the \(\lambda^4\log\) coefficient as a quadratic form on invariant curvature);
- `workspace/scripts/step56_log_interaction_controls.py` → `workspace/data/step56_log_interaction_controls.json`
  (generic curvature and wrong-tail controls).

Sources registered by the Step-55 request (partial; read as listed):
- \cite{suvaina2011ale}: ALE Ricci-flat Kähler metrics on every \(\mathbb Q\)-Gorenstein smoothing fibre;
- \cite{rasdeaconu2013ale}: class-T classification and the explicit \((xy=P(z^n))/\mu_n\) model;
- \cite{lisca2007lens}: lens spaces bounding rational balls;
- \cite{fintushel1997rational}: rational blowdown and its SW formula;
- \cite{agolhyperbolic}: SW vanishing for splittings along an \(L\)-space with \(b^+\ge1\) on both sides. This is the
  two-sided (SW\(_L\)) input. Lens spaces and spherical space forms are \(L\)-spaces, so the two-sided form is now
  citable;
- Biquard–Rollin smoothing of class-T cscK orbifolds (Knowledge object `Smoothing-singular-extremal-Kähler-surfaces-and-minimal-Lagrangians--76bcf086d1fb`).

---

## 0. Corrections to Step 55 now in force (verifier `trace/ttcs/results/step55_ttcs01_verifier1_integration.md`)

1. **Retained as proved:** the charge formula (1.1), \(P(\mathcal O(-n),g_{\rm LeB})=8\pi^2(n-2)^2/n\) (exact, since
   \(W^+=0\)), the ledger (1.2) and the conservation identity (1.3) (sums over attachment regions), and Theorem 55.5. In
   55.5 the \(v_2(n)=1\) case is obstructed mod 4, not mod 8. The Wahl-ball charges \((0,-4(1-1/n^2))\) hold for **all**
   \(n\), by the Hirzebruch–Jung formula with \(\sum(b_i-3)=1\) and \(q+q'=n^2-2\).
2. **Lemma 55.1** gives \(\pi_1(N)/\langle\!\langle\pi_1L\rangle\!\rangle=1\), not \(\pi_1(N)=1\). Prop. 55.3 is valid **only
   for simply connected** rank-one regions. Counterexample to the unrestricted cyclic-end exclusion:
   \(N=\bar B_{t,a}\natural(\overline{\mathbb{CP}}^2\setminus B^4)\), with charges \((-3+4/t^2,-5)\); for \(t=2\) the end
   is \(L(4,3)\) and the charges are \((-2,-5)\). In general \(|H_1(L)|=m^2t^2\).
3. **Additive budget:** under (U) and \(\mathrm H_{\rm lsc}\),
   \(\sum_j\max\{c_+(N_j),c_-(N_j),0\}<1\), and the exact threshold is \(C_+(V)+\sum_jw(N_j)<A\).
4. "Zero charge ⇔ Wahl ball" is **not** proved. Charge does not determine the filling, and the rational-ball table is
   hypothetical charge arithmetic.
5. **Prop. 55.6, repaired proof** (replaces the SW/general-type argument):
   - \(\pi_1(Y)=\Gamma\), so \(b_1(Y)\) is even and \(Y\) is Kähler;
   - the degree-one map \(Y\to X\) is homotopic to a harmonic map, which is \(\pm\)holomorphic by Siu rigidity;
   - so the map is birational and \(Y\) is \(X\) blown up \(r+1\) times;
   - since \(X\) has no rational curves, the chain is exceptional, and the counting argument
     \(3r+2\le3r+1\) applies.
   Scope: only the complex-orientation zero-charge Wahl channel with a complex-orbifold bulk.
6. **Collapse ledger (§6 of Step 55) withdrawn.** For a bounded-curvature collapsing region \(C\) with volume \(\to0\),
   \(P(g_i)/8\pi^2=C_+(\Omega_i)-(A-1)+o(1)\). The threshold remains \(C_+(\Omega_i)<A\), because boundary terms compensate
   \(\tau(C)\). What survives is that collapsed regions cost nothing energetically and must be excluded
   topologically. The free-circle spin lemma applies; the cyclic-image lemma only puts classes in \(\mathbb ZE\) and does
   **not** exclude \(E\) (a punctured \(\overline{\mathbb{CP}}^2\) is simply connected).
7. **Theorem 55.7 becomes a coarse trichotomy.** In a case-(I) configuration, under (SW\(_L\)) and its one-sided form,
   exactly one holds:
   - (A) no cone point with nontrivial group;
   - (B) exactly one nontrivial-group attachment region with \(b_2=1\) (image in \(\mathbb QE\)), all others rational
     balls;
   - (C) nontrivial-group points exist and all their regions are rational balls.
   In every case the additive budget of item 3 applies.
8. **The \([5,2]\) model has simply connected complement** (auxiliary-line argument). So
   \(Z=(\#3\overline{\mathbb{CP}}^2)_{C_{9,2}}\) is simply connected with form \(\langle-1\rangle\), hence
   **homeomorphic** to \(\overline{\mathbb{CP}}^2\). A diffeomorphism is still unproved; §2 is therefore stated for the
   smooth manifold \(X\#Z\).
9. Inherited typo in Step 54: reversing Burns exchanges \((1,-5)\).

---

## 1. The orbifold-category theorem

**Conservation law, reread.** Identity (1.3) of Step 55 says that bubbling never changes the Kähler-type baseline
\(T_+(M)=A-1\). It only moves self-dual Weyl charge between bulk and bubbles. So any exclusion of the orbifold channels
must use a lower bound on a non-Kähler bulk. For orbifolds this is the same open-range inequality \(C_+\ge A\) that is open
on \(M\) itself; LeBrun's \(2A/3\) fails there for the same reason. Accordingly the orbifold channels are not treated as a
lemma to be proved. They are carried into the theorem statement.

**Theorem 56.A (attainment in the orbifold category; \(k=1\)).** Let \(X\) be a compact ball quotient other than a fake
projective plane, and \(M=X\#\overline{\mathbb{CP}}^2\). Consider a case-(I) Anderson configuration for \(p_*(M)\).

Assume:
- the step-54 ledger \(\mathrm H_{\rm lsc}\) and \(\mathrm H_{\rm dec}\) (any group);
- bubble criticality by compact replacement;
- (SW\(_L\)): the two-sided form is \cite{agolhyperbolic}; the one-sided PSC-cap form remains a hypothesis;
- smooth orbifold regularity of the bulk \(g_0\);
- **(N\(_0\))**: every bubble region at a point with nontrivial group has \(P=0\), i.e. is Ricci-flat ALE.

Then:

(i) \(p_*(M)=P(V,g_0)=\alpha_{\rm orb}(V)\), where \(V\) is the orbifold bulk. Either \(V=M\) (no orbifold points), or every
orbifold point is a cyclic point whose bubble is a Ricci-flat ALE rational ball. In the latter case the configuration is
case (C) of §0.7, with \(c_+(N_j)\le0\).

(ii) \(g_0\) is \(P\)-critical on \(V\), with constant scalar curvature \(s_0<0\).

(iii) Exactly one of the following holds:
- \(g_0\) is an Einstein orbifold metric. Then \(p_*(M)=0\), so \(\alpha(M)=0\); if \(V\ne M\) the infimum is attained only
  if \(M\) carries an Einstein metric.
- \(g_0\) is not Bach-flat. This is Problem 3 in the orbifold category.

(iv) If \(V\ne M\) and some orbifold point is a Wahl point \(\tfrac1{n^2}(1,na-1)\) with its Milnor fibre in the complex
orientation, then:
- \(n\) is odd or \(8\mid n\) (Thm 55.5);
- \(V\) is not a complex orbifold with that complex quotient singularity (Prop 55.6, repaired);
- the minimal resolution \(Y\) has \(\pi_1=\Gamma\), and \(Y\to X\) has degree one with a unimodular kernel lattice
  containing the chain primitively.

*Proof.*
- (i) Conservation (1.3) with \(P(N_j)=0\) gives \(p_*(M)=P(V,g_0)\) under \(\mathrm H_{\rm lsc}\).
- Zero-energy reassembly (verifier §10, made precise in §2 below) gives \(p_*(M)\le P(V,g)\) for every smooth orbifold
  metric \(g\) on \(V\). Hence \(P(V,g_0)=\alpha_{\rm orb}(V)\).
- Ricci-flat ALE spaces have \(c_+=P/8\pi^2-w=-w\le0\). A Ricci-flat ALE with \(b_2=1\) in case (B) would carry a class of
  square \(-m^2\) on an Einstein ALE space with \(P=0\). We do not exclude this in general. (N\(_0\)) together with case (B)
  is therefore kept in the statement as part of case (i)'s alternative, unless the end is simply connected cyclic with
  \(m\le2\), where \(c_+=1>0\) is impossible.
- (ii) Criticality on \(V\) is the minimizing property of \(g_0\) in \(\alpha_{\rm orb}(V)\). The trace of the
  Euler–Lagrange equation is \(\Delta s=0\), so \(s\) is constant.
- If \(s_0\ge0\), reassembly produces metrics on \(M\) with \(\int s_-^2\to0\), because the bubbles are scalar-flat and
  the gluing error vanishes. This contradicts LeBrun's estimate \(\int s^2\ge\int s_-^2\ge32\pi^2c_1^2(X)\), which holds
  for every metric on \(M\) since \(SW_M\ne0\) and the basic class is \(\pm K_X\pm E\).
- (iii) The proof of Step 53 applies verbatim on orbifolds (local, away from finitely many points, plus removability at
  the cone points for a smooth orbifold metric): Bach-flat + \(P\)-critical + constant \(s\ne0\) ⇒ Einstein. If
  \(g_0\) is Einstein, reassembly gives \(P\to0\).
- (iv) Step 55 with the repairs of §0. \(\square\)

What 56.A does **not** assume away:
- the case-(B) channels with non-simply-connected regions or noncyclic ends;
- non-Ricci-flat rational-ball bubbles of positive cost satisfying the additive budget;
- exotic-homotopy-sphere bubbles;
- collapse.
These remain hypotheses through (N\(_0\)) and case (I).

**Corollary 56.B (orbifold Einstein metrics give zero gap).** If some compact orbifold \(V\) with only Wahl points, whose
Milnor-fibre smoothing is diffeomorphic to \(M\), carries an Einstein orbifold metric, then \(\alpha(M)=0\). This is
Prop. 56.U applied at \(P(V,g)=0\).
- If the Wahl points are complex quotient points of a complex orbifold structure on \(V\), the metric cannot be Kähler
  (56.A(iv)).
- For comparison, Theorem Y at \(P=0\) shows that a smooth Einstein metric on \(M\) would need \(Y^2\ge32\pi^2(A+1)\).
  No orbifold analogue is claimed.

This is the \(k=1\) analogue of the Step-52 Kronheimer absorption, restricted by the lattice law (\(n\) odd or \(8\mid n\)).
Absorption through case-(B) regions is not covered by this corollary.

---

## 2. The unconditional zero-energy upper bound

**Proposition 56.U.** Let \(V\) be a compact oriented 4-orbifold with isolated cyclic points
\(p_j\in V\), \(\Gamma_j=\tfrac1{n_j^2}(1,n_ja_j-1)\). Let \(M'\) be the smooth manifold obtained by replacing a
neighbourhood of each \(p_j\) by the Milnor fibre \(B_{n_j,a_j}\), glued in the complex orientation of the local chart.
Then for every smooth orbifold metric \(g\) on \(V\),
\[
p_*(M')\le P(V,g).
\]

*Proof.*
1. Each \(B_{n,a}\) carries a Ricci-flat Kähler ALE metric \(g_B\) asymptotic to \(\mathbb C^2/\Gamma\) at rate
   \(O(r^{-4})\) with all derivatives \cite{suvaina2011ale,rasdeaconu2013ale}. In GH form it is the free \(\mathbb Z_n\)
   quotient of the \(A_{n-1}\) metric with centres on a \(\mathbb Z_n\)-orbit.
2. In an orbifold chart, \(g=g_{\rm flat}+O(r^2)\), and the \(O(r^2)\) term is a smooth \(\Gamma\)-invariant tensor.
3. Glue \(\lambda^2g_B\) to \(g\) on the annulus \(\rho\le r\le2\rho\) by a cutoff. The interpolation error tensor is
   \(O(\rho^2)+O((\lambda/\rho)^4)\) with \(j\)-th derivatives scaled by \(\rho^{-j}\). The annular volume is \(O(\rho^4)\),
   so the annular \(P\)-error is \(O(\rho^4)+O((\lambda/\rho)^8)\).
4. Inside \(r<\rho\), \(P(\lambda^2g_B)=0\). The deleted orbifold region carries \(\int_{r<\rho}|{\rm Ric}^\circ_g|^2=O(\rho^4)\).
5. With \(\rho=\lambda^{1/2}\) the total error is \(O(\lambda^2)\to0\). \(\square\)

So every orbifold degeneration through Wahl points is a competitor, and any construction of a cheap orbifold cell
bounds the smooth problem from above. For \(V=X\#\mathcal O_{9,2}\) with \(\mathcal O_{9,2}=Z\) with \(B_{3,1}\) collapsed
(\(Z\) from §0.8), \(M'=X\#Z\). This is homeomorphic to \(M\); a diffeomorphism follows if \(Z\cong\overline{\mathbb{CP}}^2\).

Because the gluing in 56.U is \(O(\lambda^2)\) and not more precise, the first-order interaction between \(g\) and the
bubble is not seen. §4 computes it.

---

## 3. Curvature at a Wahl point is forced into a 4-parameter type

Let \(\Gamma=\tfrac1{N}(1,q)\) with \(N=n^2\), \(q=na-1\), \(n\ge3\). In complex coordinates of the chart:
- \(\Lambda^+=\mathbb R\omega\oplus\mathbb C\,dz_1\wedge dz_2\), with characters \(1,\zeta^{1+q}=e^{2\pi ia/n}\);
- \(\Lambda^-=\mathbb R\bar\omega\oplus\mathbb C\,dz_1\wedge d\bar z_2\), with characters \(1,\zeta^{1-q}\).

None of \(\zeta^{1\pm q},\zeta^{2(1\pm q)},\zeta^{2q}\) is trivial for \(n\ge3\) (script, all Wahl points with
\(n\le9\)). Hence the Γ-invariant algebraic curvature tensors form a 4-dimensional space:
\[
R_p=\Bigl(\tfrac{s}{12}+w_+D\Bigr)\oplus\Bigl(\tfrac{s}{12}+w_-D\Bigr),\qquad B=b\,\hat\omega\otimes\hat{\bar\omega},
\qquad D=\operatorname{diag}(2,-1,-1).
\]
Here \(W^\pm\) are degenerate (type D) with the distinguished eigenvector \(\omega\) (resp. \(\bar\omega\)), and
\(\mathrm{Ric}^\circ_p\propto b\,(\omega\circ\bar\omega)\), which is \(J\)-invariant with eigenvalues \((b',b',-b',-b')\)
on \(z_1,z_2\).

For \(n=2\) (\(\tfrac14(1,1)\)) the space is 12-dimensional. It is irrelevant here, since \(n=2\) is excluded by the
lattice law.

So at every Wahl point the curvature of **any** smooth orbifold metric is pointwise of ambi-Kähler algebraic type, with
the Kähler forms of both orientations fixed by Γ. For a \(P\)-critical bulk this is the only local datum the bubble can
couple to at second order.

**Bubble moduli.** For the \(\mathbb Z_n\)-symmetric GH configuration of \(n\ge3\) centres on a circle of radius \(R_c\)
around the \(\omega\)-axis, the leading tail is the quadrupole
\(\delta V=-(n^2R_c^2/4)\,P_2(\cos\theta)/r^3\) on the cover. It is **independent of the phase** of the configuration
(script: \(n=3,\dots,8\); dependent only for \(n=2\)). The axial offset is pure gauge. So the only modulus that affects
the leading interaction is the scale \(\lambda\) (\(\lambda^4\propto R_c^2\)). The relocation and frame freedom used in
Theorem 53.B is absent: the frame is fixed by Γ, and the normaliser torus acts trivially on invariant curvature.

---

## 4. The \(\lambda^4\log(1/\lambda)\) interaction vanishes

**Setup.** On the universal cover \(\mathbb C^2\) of the chart:
- the bulk is \(g_0=\delta+q\) in normal coordinates, \(q_{ij}=-\tfrac13R_{ikjl}y^ky^l\);
- the bubble tail is \(t\), homogeneous of degree \(-4\), obtained from the GH quadrupole in the Hopf/moment coordinates
  of the triholomorphic circle \((e^{it}y_1,e^{-it}y_2)\). The axis is the \(\omega\)-direction, matching §3.

Script checks:
- the flat GH structure reproduces \(\delta\) exactly;
- normal coordinates reproduce \(\mathrm{Ric}_p\);
- the tail is linearized Ricci-flat (\(|{\rm Ric}'(t)|\sim10^{-7}\), round-off level). The opposite orientation of
  \(A_2\) gives \(|{\rm Ric}'|\sim60\), so the sign is fixed.

In the overlap \(\lambda\ll r\ll1\) the glued metric is \(\delta+q+\lambda^4t+\dots\). Since \({\rm Ric}'(t)=0\), the
first term of \(P\) mixing bulk and bubble is the \(e^2m\) coefficient of \(|{\rm Ric}^\circ|^2d\mu\) for
\(\delta+eq+mt\). It is homogeneous of degree \(-4\), so
\[
P(\text{glued})=P(V,g_0)+\lambda^4\log(1/\lambda)\,\frac{c_n}{|\Gamma|}\int_{S^3}c(\hat y)\,d\sigma+O(\lambda^4).
\]
The log coefficient is gauge invariant: a degree \(-3\) Lie-derivative change of \(t\) changes the density by a divergence
with no log.

**Result.**
- The pointwise coefficient \(c(\hat y)\) is nonzero and \(T^2\)-invariant. For example, at \((s,w_+,w_-,b)=(1,.5,-.7,.9)\),
  \(c=-28.98\) at \(\chi=0.6\), the same for three torus angles.
- Its \(S^3\) integral, computed as a quadratic form on the 4-parameter invariant curvature (48-point Gauss–Legendre in
  \(\chi\), Richardson extrapolation in both perturbation parameters), is
  \[
  \int_{S^3}c\,d\sigma=0\qquad(\text{all 10 matrix entries }\lesssim2\times10^{-8},\ \text{against pointwise values }O(10)).
  \]
- With \(k=2\times10^{-3}\) and no extrapolation, the entries were \(O(1)\). That was \(m^3\) contamination, now removed.

Control runs (generic non-invariant \(R_p\); wrong-sign tail) are recorded in §4.1. The vanishing persists in all of them.
§4.1 also gives the structural reason (Lemma 56.L).

**Consequence.** At the logarithmic order a Ricci-flat Wahl-ball bubble does not see the bulk curvature at the singular
point. There is no analogue of the Burns kernel-direction saving \(-9x_0^2\log(1/x_0)\), and no analogue of a
Biquard–Ozuch condition \(\mathbf R^+(\omega,\omega)=0\) at this order. The first interaction is at order \(\lambda^4\)
without a log. Its coefficient is a renormalized local quadratic form \(\mathcal Q_\Gamma(R_p)\), the
\(P\)-polarizability of \(B_{n,a}\). It is obtained by minimizing the second variation of \(P\) on the bubble over
perturbations with prescribed growth \(R_p\,r^2\), after subtracting the bulk's own \(\int|{\rm Ric}^\circ_p|^2\) volume
term (the log term vanishes, as shown).

Minimality of the configuration in 56.A forces \(\mathcal Q_\Gamma(R_p)\ge0\) at each Wahl point. Bulk nonlocal
responses enter only at \(O(\lambda^8)\), because the bubble's source in the bulk is \(O(\lambda^4)\) and \(g_0\) is critical.
Deciding whether \(\mathcal Q_\Gamma\) is indefinite on the 4-dimensional space requires solving a fourth-order
\(\mathbb Z_n\times U(1)\)-symmetric problem on the GH space. If it is indefinite, it gives a pointwise constraint at every
Wahl point of an orbifold minimizer. If it is positive semidefinite, the local mechanism cannot exclude the T-channel, and
the decision returns to the global threshold or to a construction.

### 4.1 Controls, and why the vanishing is structural

The control runs (`step56_log_interaction_controls.json`; 24×12×12 product quadrature over \(S^3\); each pair is
(signed integral, integral of the absolute value)):

| bulk \(R_p\) | tail | \(\int_{S^3}c\) | \(\int_{S^3}|c|\) |
|---|---|---|---|
| generic (random Bianchi tensor, not Γ-invariant) | Ricci-flat (correct) | \(5.5\times10^{-8}\) | 2484 |
| invariant | wrong-sign \(A_2\) (not linearized Ricci-flat) | \(-1.4\times10^{-7}\) | 3086 |
| generic | wrong-sign | \(-9.2\times10^{-7}\) | 6082 |
| invariant | correct | \(1.7\times10^{-8}\) | 467 |

So the vanishing holds for arbitrary curvature and does not use Ricci-flatness of the tail. Its proof is as follows.

**Lemma 56.L (no logarithmic linear interaction).**
- Let \(g_0\) be any smooth metric near \(p\), and let \(t\) be a symmetric 2-tensor homogeneous of degree \(-4\) on the
  cone.
- The part of the \(P\)-density linear in \(t\) is \(\langle\nabla P(g_0),t\rangle\,d\mu+d\iota(B(g_0;t))\), with \(B\)
  bilinear in jets.
- The divergence term contributes, on the annulus \(\{\lambda<r<1\}\), only sphere fluxes. Each homogeneous piece of
  degree \(d\) gives \(\rho^{d+3}\), and a degree \(-3\) piece gives a constant; neither produces \(\log\rho\).
- Hence the \(\lambda^4\log(1/\lambda)\) coefficient equals \(\int_{S^3/\Gamma}\langle[\nabla P(g_0)]_0,t\rangle\), where
  \([\cdot]_0\) is the degree-0 Taylor coefficient at \(p\).

Two consequences:
(a) If \(g_0\) is \(P\)-critical near \(p\), then \(\nabla P(g_0)\equiv0\) and the coefficient is \(0\) for **every** tail.
(b) For the truncated metric \(\delta+q\) used in the script, \([\nabla P]_0=E_2(R_p,R_p)\) is a constant tensor, and the
coefficient is \(\langle E_2,\int_{S^3}t\rangle\). For any tail built equivariantly from a quadrupole
\(Q\in\mathrm{Sym}^2_0\Lambda^+\cong(2,0)\), the average \(\int_{S^3}t_{ij}\) lies in
\(\mathrm{Sym}^2T^*=(0,0)\oplus(1,1)\), which contains no \((2,0)\). So the average is \(0\). This explains the controls,
including the wrong-sign tail.

The numerics therefore confirm Lemma 56.L: the script measures exactly the term the lemma isolates. For the actual
problem, (a) is the operative statement and needs no computation. **At a Wahl point of a \(P\)-critical orbifold bulk
there is no \(\lambda^4\log\) interaction.**

**What the first interaction is.** With the log term gone, the \(\lambda^4\) coefficient has two local parts:
1. **Bulk flux.** The constant (degree \(-3\)) part of \(B(g_0;t)\) pairs the tail's quadrupole with the degree-1 jets of
   \(g_0\)'s curvature (\(\nabla\mathrm{Rm}_p\), Γ-invariant part). This term is linear in the bubble.
2. **Bubble polarizability.** This is the renormalized minimum of the second variation of \(P\) on \(B_{n,a}\) along
   perturbations growing like \(R_p\,r^2\). It is quadratic in \(R_p\) and nonlinear in the bubble.

The nonlocal bulk response is \(O(\lambda^8)\). Minimality in 56.A gives \(\mathcal Q_\Gamma(\nabla\mathrm{Rm}_p,R_p)\ge0\).
The sign structure of this form decides whether any pointwise mechanism exists. Computing it needs a
\(\mathbb Z_n\times U(1)\)-symmetric fourth-order problem on the GH space. This is a finite, well-posed computation, but it
was not done in this Step.

**Judgement.** The strategist's hoped-for analogue of Biquard–Ozuch is not available at the order where Burns and EH
analogues live:
- For Burns, the mass tail \(r^{-2}\) gives an order-\(\lambda^2\) term linear in \(R^+\).
- For Ricci-flat bubbles, criticality kills the log term identically.

So the zero-charge Wahl channel at \(k=1\) cannot be closed by a cheap local sign. It must be decided by the polarizability
form, by a global non-Kähler estimate (§1), or by a construction (§2, 56.U).
