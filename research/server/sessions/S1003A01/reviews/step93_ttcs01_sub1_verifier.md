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
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md",
    "Sessions/S1003A01/workspace/scripts/step93_wahl_index_transfer.py",
    "Sessions/S1003A01/workspace/data/step93/wahl_index_transfer.json",
    "Sessions/S1003A01/workspace/scripts/step93_wahl_supplied_characters.py",
    "Sessions/S1003A01/workspace/data/step93/wahl_supplied_characters.json",
    "Sessions/S1003A01/workspace/notes/step92_wahl_field_limit_proof_blueprint.md",
    "Sessions/S1003A01/trace/ttcs/results/step92_ttcs02_verifier1_integration.md",
    "Sessions/S1003A02/workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md",
    "Sessions/S1003A01/workspace/scripts/step89_wahl_isotropy.py"
  ]
}
```

## Task

Verify the Step-93 note line by line as a mathematician. Goal context: Einstein gaps on four-manifolds; Q1 asks whether X#kCP2bar (X general type, k<A/3, A=K_X^2) carries Einstein metrics, and the Wahl-orbifold channel V (A02 Theorem 102.R) is one alternative. Check in particular: (a) Lemma 93.R abelian point removability — is the capacity argument correct (dF=0 across 0, Dirac equation across 0), is the Coulomb solution with boundary condition iota_nu a'=0, d*a'=0, da'=F on the ball well-posed and unique, is the bootstrap valid starting from a' in W^{1,2} and bounded Phi? (b) Lemma 93.Q: classification of Gamma-equivariant spin^c structures on B and B*, uniqueness implying Gamma-invariance of a', the cocycle argument c_gamma=0, identification with res(s). (c) Theorem 93.A items 1-4 (tightness, class transfer, energy convergence) and the claim that the orbifold LeBrun mixed estimate follows by applying WFL to conformal rescalings. (d) Lemma 93.I: APS index vanishing on the Ricci-flat ALE Wahl filler (flat determinant, weight window, conformal covariance) and on the cone (psc cap), boundary invertibility, and whether the Kawasaki computation in wahl_index_transfer.json correctly supports it. (e) Prop 93.Y: is the Wahl orbifold of Theorem 102.R really orbifold-diffeomorphic to a complex orbifold Y once the PPS sphere is chosen holomorphic (Grauert linearization; reflection diffeomorphisms; PPS family W_t, W_0); is K_Y not nef (discrepancies a_i=-(n-i)/n, K.C); is the 'transfer principle' that field/index/curvature-integral obstructions coincide on V and M justified? (f) Prop 93.C: restriction maps x|_{V_-4}=(x.S)u, K|_B of order n, the twist formula and forced-zero counts (data file). (g) Lemma 93.W isotropy. Report errors with exact repairs, identify any hidden hypothesis, and say which statements are standard/known versus new. Also give your best mathematical suggestion for the 'missing implication' in §6: is there a plausible route to a quantitative Einstein estimate using forced orbifold zeros, or a construction on the Kahler orbifold Y showing the forced-zero cost can be made small?

## Output

# Scientific verification memo — Step 93

## Overall assessment

The compactness–removability part is mathematically sound after two local corrections:

1. the determinant-connection gauge transformation has a factor of \(2\);
2. \(W^{2,4}\not\subset C^{1,\alpha}\) in dimension four, so the bootstrap needs one additional integrability step.

Theorem 93.A then follows from the explicit Lemma 86.S recovery metrics and the supplied unperturbed Seiberg–Witten structures.

Lemma 93.I is plausible and can be completed with standard APS/weighted Dirac theory, but the present proof compresses several analytic identifications into one paragraph. The JSON computation is high-precision numerical work, not exact cyclotomic arithmetic.

Proposition 93.Y applies to a deliberately chosen complex-model realization for odd \(n\), and analogously for \(n=2\); it does not presently cover every realization in Theorem 102.R, especially the even \(n\ge4\) construction. Its transfer principle is correct for the \(+\)-chirality integrated ingredients used in LeBrun’s argument, but not for arbitrary Chern–Weil or field-theoretic information.

Proposition 93.C has the correct algebra once the canonical marking of the Milnor fibre is established. Its character count contains a stronger fact not used in the note: for every odd \(n\ge3\), the forced-zero sign patterns themselves still furnish a class with
\[
(a_g^+)^2\ge A.
\]
Thus the strongest supplied field can be chosen to have a forced double zero. This yields strict LeBrun inequalities for each fixed metric, though no metric-independent positive excess follows.

---

## 1. Lemma 93.R: abelian removability

### 1.1 Extension of \(dF=0\) through the point

This cutoff argument is correct. With
\[
\chi_\delta=0\ \text{on }B_\delta,\qquad
\chi_\delta=1\ \text{off }B_{2\delta},\qquad
|d\chi_\delta|\le C\delta^{-1},
\]
one has
\[
\|d\chi_\delta\|_{L^2}=O(\delta),\qquad
\|d\chi_\delta\|_{L^1}=O(\delta^3).
\]
For a smooth compactly supported one-form \(\beta\),
\[
\left|\int F\wedge d\chi_\delta\wedge\beta\right|
 \le C\|F\|_{L^2(B_{2\delta})}\|d\chi_\delta\|_{L^2}
 \longrightarrow0.
\]
Hence \(dF=0\) distributionally on \(B\). The local \(L^2\)-norm of \(F\) alone already tends to zero on shrinking balls, so the additional \(O(\delta)\) factor is more than sufficient.

### 1.2 Coulomb primitive

The system
\[
da'=F,\qquad d^*a'=0,\qquad \iota_\nu a'=0
\]
has a unique solution \(a'\in W^{1,2}(B)\), but the reason should be stated more precisely.

- Since \(H^2(B)=0\), an \(L^2\) de Rham/Poincaré theorem gives \(b\in W^{1,2}\) with \(db=F\).
- Solve the scalar Neumann problem for \(v\) so that \(a'=b-dv\) obeys \(d^*a'=0\) and \(\iota_\nu a'=0\).
- If \(a'_1-a'_2=h\), then \(dh=d^*h=0\) and \(\iota_\nu h=0\). Such fields represent \(H^1(B;\mathbb R)=0\), hence \(h=0\).

Thus \(H^2(B)=0\) gives existence of a primitive, while \(H^1(B)=0\) gives uniqueness.

### 1.3 Gauge factor

There is a factor-of-two error. The note uses \(A\) as the determinant connection, as shown by
\[
D_A=D_{A_0}+\frac12c(A-A_0).
\]
For a gauge map \(u\colon B^*\to U(1)\),
\[
A\longmapsto A-2u^{-1}du.
\]
If
\[
a-a'=df,
\]
then the gauge producing \(A_0+ia'\) is
\[
u=e^{if/2}
\]
up to the chosen sign convention, not \(e^{-if}\). The spinor is multiplied by the same \(u\). All subsequent regularity and equivariance arguments survive this correction.

### 1.4 Extension of the Dirac equation

After this gauge correction,
\[
D_{A_0}\Phi'=-\frac{i}{2}c(a')\Phi'=:\phi.
\]
Since \(a'\in W^{1,2}\hookrightarrow L^4\) and \(\Phi'\in L^\infty\),
\[
\phi\in L^4.
\]
The point produces no distributional source:
\[
\left|\int\langle\Phi',c(d\chi_\delta)\psi\rangle\right|
 \le C\|\Phi'\|_\infty\|\psi\|_\infty\|d\chi_\delta\|_{L^1}
 =O(\delta^3).
\]
Thus \(D_{A_0}\Phi'=\phi\) on all of \(B\) distributionally, and
\[
\Phi'\in W^{1,4}_{\mathrm{loc}}.
\]

### 1.5 Bootstrap

The line
\[
a'\in W^{2,4}_{\rm loc}\subset C^{1,\alpha}
\]
is incorrect in real dimension four. At the critical exponent,
\[
W^{2,4}\hookrightarrow C^{0,\alpha}\quad(\alpha<1),
\]
and
\[
W^{2,4}\hookrightarrow W^{1,q}\quad\text{for every finite }q,
\]
but not directly into \(C^{1,\alpha}\).

A valid bootstrap is:

1. \(\Phi'\in W^{1,4}\cap L^\infty\), hence \(q(\Phi')\in W^{1,4}\).
2. From
   \[
   d^+a'=q(\Phi'),\qquad d^*a'=0,
   \]
   interior elliptic regularity gives \(a'\in W^{2,4}\).
3. Therefore \(a'\in C^{0,\alpha}\cap W^{1,q}\) for every finite \(q\).
4. The Dirac equation then yields \(\Phi'\in W^{1,q}\) for every finite \(q\).
5. Choosing \(q>4\), one obtains \(q(\Phi')\in W^{1,q}\), hence
   \[
   a'\in W^{2,q}\subset C^{1,\alpha}.
   \]
6. Standard iteration gives smoothness.

With these corrections, Lemma 93.R is complete. It is an elementary abelian version of a standard removable-point theorem; the particular short proof is useful and does not require nonabelian gauge machinery.

---

## 2. Lemma 93.Q: equivariance and the orbifold lift

### 2.1 Classification

The classification is correct.

- Equivariant complex line bundles over the contractible \(\Gamma\)-space \(B\) are characters of \(\Gamma\).
- Relative to the canonical \(U(2)\)-induced spin\(^c\) lift, equivariant spin\(^c\) structures form a torsor for
  \[
  \widehat\Gamma\cong H^2(B\Gamma;\mathbb Z)\cong\mathbb Z_{n^2}.
  \]
- Since \(\Gamma\) acts freely on \(S^3\), equivariant spin\(^c\) structures on \(B^*\) correspond to spin\(^c\) structures on
  \[
  L=S^3/\Gamma.
  \]
  These form an \(H^2(L;\mathbb Z)\cong\mathbb Z_{n^2}\)-torsor.
- The map
  \[
  H^2(B\Gamma;\mathbb Z)\longrightarrow H^2(L;\mathbb Z)
  \]
  is an isomorphism in degree two.

Consequently every spin\(^c\) structure on the punctured chart determines a unique equivariant lift over the origin. Retaining the full character for even \(n\), rather than only its doubled determinant character, is essential and is handled correctly.

### 2.2 Invariance of the Coulomb representative

If \(A_0\) is invariant and \(A=A_0+ia\) is an orbifold connection, then \(\gamma^*a=a\). The uniqueness of the Coulomb primitive implies
\[
\gamma^*a'=a'.
\]
Thus
\[
d(f\circ\gamma-f)=0.
\]
The constants
\[
c_\gamma=f\circ\gamma-f
\]
form a homomorphism \(\Gamma\to\mathbb R\). Since \(\Gamma\) is finite, \(c_\gamma=0\), so \(f\) is invariant. The corrected gauge \(e^{if/2}\) is therefore invariant as well.

The extended spinor is equivariant, not literally invariant as a vector-valued function; its value transforms by the fixed spin representation tensored with \(\chi\). Continuity then extends this equivariance through the origin.

The distinction
\[
[L,U(1)]\cong H^1(L;\mathbb Z)=0,
\qquad
H^1(L;U(1))\cong\mathbb Z_{n^2}
\]
is correctly understood: ordinary gauge maps have one connected component, while torsion line bundles and flat characters remain nontrivial.

---

## 3. Theorem 93.A

### 3.1 Selection, uniform bounds, and tightness

The finite-pigeonhole selection is correct provided \(\mathcal S\) consists of actual spin\(^c\) structures carrying unperturbed solutions for every recovery metric. For \(b^+>1\), the standard blow-up basic structures have this monopole property. For \(b^+=1\), an explicit chamber supplier remains necessary.

For the Lemma 86.S family,
\[
\rho=\varepsilon^{2/3},\qquad
\rho^{-2}\!\left[\rho^2+(\varepsilon/\rho)^4\right]=O(1).
\]
Hence the scalar curvature is uniformly bounded. The maximum principle gives
\[
0\le U_\varepsilon\le C_g.
\]
Together with
\[
\operatorname{Vol}\{r<R\}\le C(\rho^4+R^4),
\]
this yields the full estimate
\[
\limsup_{\varepsilon\to0}\int_{\{r<R\}}U_\varepsilon^2
 \le C R^4.
\]
This controls both the filler core and every shrinking annular tail.

The normalization
\[
\int U^2=8\int|F_A^+|^2
 \ge32\pi^2(a_g^+)^2
\]
is correct. Thus the selected limit has
\[
\int_V|\Phi_\infty|^4\ge32\pi^2A.
\]

### 3.2 Regular-part compactness

On a compact set \(K\Subset V^{\mathrm{reg}}\), local Coulomb gauge gives \(a_j\in W^{1,2}\). The coupled system
\[
d^+a_j=q(\Phi_j)-F_{A_0}^+,\qquad d^*a_j=0,\qquad
D_{A_0+a_j}\Phi_j=0
\]
then provides the stated smooth compactness. The global connection need not be represented by one one-form; patching on the fixed restricted determinant bundle is the right formulation.

### 3.3 Real class and square

The real cohomology identifications
\[
H^2(M;\mathbb R)\cong H^2(V^{\rm reg};\mathbb R)
 \cong H^2(V;\mathbb R)
\]
are valid because both the rational ball and the cone contribute no real degree-two cohomology, while the link has the real cohomology of \(S^3\). The intersection square is preserved under this identification. Pairing curvature against compactly supported closed two-forms on \(V^{\rm reg}\) identifies the limiting real determinant class.

### 3.4 Energy convergence

The sequence of implications is valid:

1. \(F_A^+=q(\Phi)\) and spinor tightness give
   \[
   \int|F_{A_j}^+|^2\to\int|F_{A_\infty}^+|^2.
   \]
2. Chern–Weil on \(M\) and on \(V\), together with \(a_M^2=a_V^2\), gives
   \[
   \int|F_{A_j}^-|^2\to\int|F_{A_\infty}^-|^2.
   \]
3. Uniform bounds on \(s_j\) and \(U_j\), plus shrinking volume, give
   \[
   \int s_jU_j\to\int sU.
   \]
4. The integrated spinor Weitzenböck identity then gives convergence of
   \[
   \int|\nabla_{A_j}\Phi_j|^2.
   \]

Thus item 3 is correct.

### 3.5 Item 4 and the mixed LeBrun estimate

Item 4 should be read metric by metric: for each orbifold metric \(g\), a new recovery sequence and subsequence produce a solution on \((V,g)\). It does not produce one pair that solves the equations for every metric.

The conformal argument is valid. In four dimensions the Hodge star on two-forms, hence the self-dual projection and \((a^+)^2\), is conformally invariant. For the one conformal metric used in LeBrun’s argument, the finite supplied family again contains a class with \((a^+)^2\ge A\). Orbifold integration and conformal approximation therefore give
\[
\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A.
\]

---

## 4. Lemma 93.I and the computational artifact

### 4.1 APS proof

The index identity is mathematically credible, but a complete proof needs the following standard analytic proposition stated explicitly.

- The round twisted Dirac operator on \(L(n^2,n-1)\) is invertible. Friedrich’s estimate gives
  \[
  |\mu|\ge\frac32
  \]
  for every flat twist.
- On the complete ALE Wahl filling, a harmonic spinor in the APS/decaying weight has asymptotic order at least \(r^{-3}\).
- The Lichnerowicz formula with flat determinant,
  \[
  D^2=\nabla^*\nabla,
  \]
  and integration at infinity then imply that such a spinor is parallel; decay forces it to vanish. This applies in both chiralities.
- After a conformal change of the ALE end to a cylindrical end, Dirac covariance identifies this weighted kernel with the APS kernel on a truncation.
- On the orbifold cone side, a \(\Gamma\)-quotient of a positively curved cap with a product collar has no \(L^2\) harmonic twisted spinors in either chirality. Hence its APS index is zero.

With these statements, excision gives
\[
\operatorname{ind}D_M
 =\operatorname{ind}_{\rm APS}D_W+0,
\qquad
\operatorname{ind}^{\rm orb}D_V
 =\operatorname{ind}_{\rm APS}D_W+0.
\]

The present phrase “the weight window contains \(L^2\) and the APS weight” is too compressed to carry this argument by itself. The indicial convention, conformal spinor factor, and correspondence with the APS trace projection need to be recorded.

The equality of Seiberg–Witten expected dimensions also uses that the real de Rham term is unchanged:
\[
b_1(V)=b_1(M),\qquad b^+(V)=b^+(M).
\]
Dirac-index equality alone does not state this, although the required cohomological equality is available.

### 4.2 What the script establishes

`step93_wahl_index_transfer.py` uses `mpmath` at 50 decimal digits and then `Fraction.limit_denominator`. It therefore does not perform exact cyclotomic arithmetic. The JSON gives strong numerical evidence for \(2\le n\le8\), but not a formal evaluation.

The following entries are internally consistent:

\[
\delta(0)=\frac{1-n^{-2}}{12},
\qquad
\tau_{\rm CW}-\tau_{\rm top}
 =\frac23(1-n^{-2}),
\]
and
\[
2(1-n^{-2})=3(\tau_{\rm CW}-\tau_{\rm top}).
\]

The set
\[
\{m:\delta(m)=\delta(0)\}=n\mathbb Z/n^2\mathbb Z
\]
is detected numerically with tolerance \(10^{-30}\). A proof for all \(n\) can come either from the completed APS local-index argument or from an exact finite Fourier/Dedekind-sum evaluation.

The code computes only the local term \(\delta(m)\). The statement about the total orbifold index additionally uses the separate fact that an extending line twist has the same real Chern–Weil contribution on \(M\) and \(V\).

---

## 5. Proposition 93.Y

### 5.1 Which realizations are covered

The complex construction works for:

- odd \(n\ge3\), using the holomorphic \((-4)\)-curve
  \[
  S=E_1-E_2-E_3-E_4;
  \]
- \(n=2\), using the corresponding holomorphic \((-3)\)-curve.

It does not presently cover the even \(n\ge4\) branch of Theorem 102.R, whose local host is
\[
B_{2,1}\#\overline{\mathbb{CP}}^2.
\]

Complex conjugation on individual \(\overline{\mathbb{CP}}^2\) summands realizes sign changes on exceptional homology classes. This identifies the relevant smooth homology model, but it does not by itself show that an arbitrary ambient-tubed sphere and the holomorphic sphere are equivalent as embedded pairs. The valid statement is existential: Theorem 102.R can be realized by choosing the holomorphic sphere from the outset.

### 5.2 Grauert and PPS

For \(N=\mathcal O_{\mathbb P^1}(-m)\), the displayed cohomology vanishings support formal rigidity of the curve neighborhood. Invoking Grauert’s formal principle for exceptional curves then identifies a sufficiently small analytic neighborhood with the standard PPS model.

The PPS family supplies the local identification
\[
W_t\setminus B_{n,1}\cong W_0\setminus\{\text{orbifold cone region}\}.
\]
With a marked version of this identification, replacing the Milnor fibre by the cone gives the contraction
\[
Y=\widehat X/C_{n,1}.
\]
Since \(X\) is a surface of general type and \(\widehat X\) is a blow-up, \(Y\) remains of general type. Projectivity follows from the algebraic contraction of the quotient chain.

### 5.3 \(K_Y\) is not nef

The discrepancy formula
\[
K_{\widehat X}=\pi^*K_Y+\sum_{i=1}^{n-1}a_iC_i,
\qquad
a_i=-\frac{n-i}{n},
\]
is correct; it follows directly by solving the tridiagonal intersection system for
\([n+2,2,\ldots,2]\).

If a \((-1)\)-curve \(D\) meets \(C_i\) once and no other chain component, then
\[
-1=K_{\widehat X}\cdot D
   =K_Y\cdot\pi(D)+a_i,
\]
so
\[
K_Y\cdot\pi(D)=-1-a_i=-\frac{i}{n}<0.
\]
The PPS curve supplies such a curve. A generic exceptional curve away from the chain also shows non-nefness, but by the simpler formula \(K_Y\cdot E=-1\); it does not meet the specified chain component.

For the chosen complex structure, \(K_Y\) not nef directly precludes an \(s<0\) Kähler–Einstein metric. The stronger statement that every Einstein metric on the underlying orbifold is non-Kähler requires the transferred Seiberg–Witten scalar estimate, as in A02 Proposition 102.K(c), rather than non-nefness of this one complex structure alone.

### 5.4 Transfer principle

The transfer statement should be narrowed to the actual invariant package:
\[
a_V^2=a_M^2,\qquad
2\chi_{\rm orb}(V)+3\tau_{\rm CW}(V)=2\chi(M)+3\tau(M),
\]
equal extendible Dirac indices, and the transferred scalar/\(W^+\) inequalities. These reproduce the usual LeBrun obstruction on \(V\).

Not every Chern–Weil expression is identical. In particular,
\[
2\chi_{\rm orb}-3\tau_{\rm CW}
\]
differs by
\[
-4(1-n^{-2})
\]
per Wahl point. Local torsion characters, pointwise isotropy, forced spinor zeros, and estimates involving \(W^-\) can also distinguish \(V\) from \(M\).

Thus “no stronger one” is justified for the standard \(+\)-chirality integrated LeBrun package, not for every possible argument involving supplied fields or curvature.

---

## 6. Proposition 93.C and Lemma 93.W

### 6.1 Restriction algebra

With \(u\in H^2(V_{-4};\mathbb Z)\) normalized by \(\langle u,[S]\rangle=1\),
\[
x|_{V_{-4}}=(x\cdot S)u.
\]
For
\[
S=E_1-E_2-E_3-E_4,
\]
one gets
\[
E_i|_{V_{-4}}=-\varepsilon_i u,
\qquad
\varepsilon=(1,-1,-1,-1),
\]
and
\[
K_M\cdot S=2,\qquad K_M|_{V_{-4}}=2u.
\]

For odd \(n\), if \(K_M|_B\) has exact order \(n\), then \(u_B\) is a generator and
\[
u_B=hK_M|_B,\qquad h=2^{-1}\pmod n.
\]
The exact-order statement should be grounded in the explicit quotient model of the Milnor fibre: the canonical bundle has flat holonomy of order \(n\). The Cartier index of the central singularity alone does not automatically identify the marked class on the smooth fibre without this relative-canonical comparison.

Once that marking is fixed, the twist formula
\[
j_F=\sum_{i\in F\cap\{1,\dots,4\}}(-\varepsilon_i h)\pmod n,
\qquad m=nj_F
\]
is correct.

### 6.2 Character counts

The JSON counts are correct, and the pattern can be proved for all odd \(n\), not only \(n\le15\).

- \(n=3\): six of the sixteen patterns have \(j\notin\{0,1\}\).
- Every odd \(n\ge5\): eight of the sixteen patterns have \(j\notin\{0,1\}\).

For \(n\ge5\), these eight patterns are precisely the odd-cardinality subsets of \(\{1,2,3,4\}\).

The isotropy weights of \(S^+\otimes\chi^{nj}\) are
\[
nj,\qquad n(j-1)\pmod{n^2}.
\]
A spinor value can therefore be nonzero only for \(j=0,1\). Adding the cotangent weights
\[
\pm1,\qquad\pm(n-1)
\]
never gives zero modulo \(n^2\) when \(n\ge3\), so the first jet also vanishes. The forced zero has order at least two.

### 6.3 Stronger supplied-class selection

Let \(\mathcal F_{\rm forced}\) be the forced local patterns. Since
\[
\sum_{i=1}^4(-\varepsilon_i h)\equiv1\pmod n,
\]
complementation sends
\[
j_F\longmapsto1-j_F.
\]
Hence \(\mathcal F_{\rm forced}\) is closed under complementation, and every local exceptional sign has zero mean over this set.

Averaging also over all signs outside the first four gives
\[
\frac1{|\mathcal F_{\rm forced}|\,2^{k-4}}
 \sum_{\substack{F\in\mathcal F_{\rm forced}\\\text{outer signs}}}
 (a_F^+)^2
 =
 |K_X^+|^2+
 \operatorname{Avg}\left|\sum_{i=1}^4\sigma_iE_i^+\right|^2
 +\sum_{i=5}^k|E_i^+|^2
 \ge |K_X^+|^2\ge A.
\]
Therefore, for every metric and every odd \(n\ge3\), at least one forced-zero supplied class satisfies
\[
(a_F^+)^2\ge A.
\]
For \(b^+>1\), WFL can be run using only this forced subset. The resulting orbifold monopole is irreducible and obeys
\[
\int U_F^2\ge32\pi^2A,
\qquad
\Phi_F(p)=0,\qquad
\nabla\Phi_F(p)=0.
\]

This is stronger than the fraction count in Proposition 93.C and directly links the isotropy information to the optimal LeBrun constant.

### 6.4 Lemma 93.W

The representation calculation is correct. For \(n\ge3\),
\[
\Lambda^+=\mathbb R\omega_0\oplus\operatorname{Re}\Lambda^{2,0}
\]
has weights \(0,\pm n\). In
\(\operatorname{Sym}^2_0\Lambda^+\), the cross terms have weights \(\pm n\), while trace-free quadratic terms on \(\operatorname{Re}\Lambda^{2,0}\) have weights \(\pm2n\). None is zero modulo \(n^2\). Thus the invariant subspace is one-dimensional:
\[
W^+(p)=\mu\,\mathrm{diag}(2,-1,-1).
\]
For \(n=2\), \(2n=n^2\), producing a three-dimensional invariant subspace. The statements about values of harmonic self-dual forms and \(F_A^+\) follow immediately.

---

## 7. The missing Einstein estimate

The strengthened forced-class averaging gives a useful exact result but not a uniform numerical excess. For the selected forced field,
\[
\|U\|_2\le\|s^-\|_2
\]
is strict: equality would force \(\nabla_A\Phi\equiv0\), while a parallel spinor vanishing at \(p\) vanishes everywhere, contradicting
\(\int U^2\ge32\pi^2A\). The mixed LeBrun inequality is likewise strict for each fixed metric.

A metric-independent positive amount does not follow from an isolated zero. In four dimensions a point has zero \(W^{1,2}\) capacity. The field may rise from \(0\) to its typical size inside a ball whose regularity radius tends to zero. Einstein control of Ricci curvature does not provide a uniform lower bound for the full-curvature harmonic radius at the orbifold point; Weyl energy may concentrate there.

A quantitative statement becomes plausible after introducing a coupled regularity radius \(r_{\rm reg}(p)\) controlling both the metric and the local Coulomb representative. Elliptic estimates and the double zero would then give a bound of the form
\[
\int_{B_{c r_{\rm reg}}(p)}(\lambda^2-U^2)
 \ge c\,\lambda^2 r_{\rm reg}^4.
\]
Thus a uniform excess requires a lower bound for \(\lambda r_{\rm reg}^2\). Along an Einstein sequence where this quantity tends to zero, one expects a Ricci-flat ALE bubble and possibly an \(L^2\) anti-self-dual abelian field. An effective route would classify such pointed bubbles and determine whether the forced character can persist through the bubble tree. The present identities do not supply that classification.

The complex orbifold \(Y\) suggests why the excess may tend to zero. Let \(C\) be the PPS curve through the Wahl point and let \(\Omega_t\) approach a Kähler-cone wall with
\[
\Omega_t\cdot C\to0.
\]
For a \((1,1)\)-class,
\[
\|\operatorname{PD}(C)^+\|^2
 =\frac{(\Omega_t\cdot C)^2}{\Omega_t^2}\longrightarrow0.
\]
Hence supplied classes differing by \(2\operatorname{PD}(C)\) become indistinguishable at the level of self-dual projections, even though one spinor is forced to vanish along a divisor through \(p\). This shows that the cohomological part of the LeBrun excess can approach zero.

A full field-level example would require solving the unperturbed orbifold Kähler Seiberg–Witten/vortex equations along such a degenerating family and estimating
\[
\int(\lambda^2-U^2)
\quad\text{or}\quad
\|d\alpha\|_2^2.
\]
No such estimate is contained in the supplied files. The Kähler-wall model is nevertheless the most direct test of whether forced zeros carry any universal integrated cost.

---

## 8. Standard material versus new material in the supplied work

**Standard ingredients**

- abelian Coulomb gauge and removable-point regularity;
- equivariant line-bundle and spin\(^c\) classification by characters;
- APS excision and weighted Dirac theory on ALE ends;
- Grauert formal rigidity and contraction of quotient chains;
- Seiberg–Witten Weitzenböck and LeBrun conformal estimates;
- elementary isotropy representation theory.

**New synthesis within the supplied files**

- the WFL theorem for the explicit Wahl recovery family;
- simultaneous transfer of supplied fields, real determinant classes, and full abelian curvature energy;
- the explicit local character bookkeeping for the blow-up basic classes;
- the comparison of the Wahl channel with the smooth Q1 problem;
- the forced double-zero mechanism at the Wahl point.

**Additional result from the verification**

For every odd \(n\ge3\), the forced-zero patterns form a complement-symmetric supplied subfamily whose average still guarantees a class with
\[
(a_g^+)^2\ge A.
\]
Thus the optimal supplied field can be chosen to have a double zero at the Wahl point. The remaining mathematical issue is not class selection but uniform control of the geometric scale on which that zero affects the global Einstein integral.