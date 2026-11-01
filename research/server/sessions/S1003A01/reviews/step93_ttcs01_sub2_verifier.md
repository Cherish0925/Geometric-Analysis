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

## Scientific verification memo on Step 93

### 0. Overall assessment

The Step-93 note is mathematically substantial and, in its main analytic and topological assertions, is essentially correct. The abelian removability argument is elementary but sound once the Hodge solution on the ball is stated with the correct elliptic conditions. The equivariant lift argument is also sound, with one important clarification: the relevant datum is the torsion character of the twisting line, not an ordinary disconnected gauge component. The compactness and energy-transfer parts of Theorem 93.A follow from the Step-92 estimates, with one quantifier repair concerning “every orbifold metric.” The index-transfer argument is plausible and is strongly supported by the exact Kawasaki computations for small \(n\), but the script verifies only a finite range unless one supplies a general identity. The complex realization and self-similarity statements are consistent with PPS and Grauert, but projectivity and the diffeomorphism moving the PPS sphere into the holomorphic model should be stated with their standard inputs. The transfer principle is correct for integral/energy/index obstructions of LeBrun type, but it should not be phrased as equality of all Seiberg–Witten invariants or all moduli-space obstructions.

The most important mathematical repairs are:

1. In Lemma 93.R, state explicitly the Hodge problem
   \[
   da'=F,\qquad d^*a'=0,\qquad \iota_\nu a'|_{\partial B}=0
   \]
   as the absolute Hodge decomposition on the ball, and note uniqueness by the Neumann argument.
2. In Theorem 93.A, item 4 requires either a strengthened supply hypothesis for every gluing family or, for conformal rescalings, the conformal covariance of the already constructed limit solution.
3. In Lemma 93.I, the APS argument is correct in structure but needs the weight window and the absence of indicial roots stated explicitly. The Kawasaki computation supports the local character statement for \(2\le n\le 8\); a general proof should be cited or supplied.
4. In Prop. 93.C, the factor \(h=2^{-1}\bmod n\) is correct once one remembers that the local twist is the twisting line, i.e. half the change in determinant, measured in units of the local canonical class.
5. The “missing implication” is best attacked either through a singular conformal/Green’s-function argument that converts the forced double zero into an end term, or through a Kähler-orbifold construction in which the cost of the forced zero is carried by curves whose areas can be made small.

---

## (a) Lemma 93.R — abelian point removability

### Statement checked

Lemma 93.R says: if \((A,\Phi)\) is an unperturbed abelian Seiberg–Witten solution on the punctured unit ball \(B^*=B\setminus\{0\}\), with
\[
\sup_{B^*}|\Phi|<\infty,\qquad F_A\in L^2(B^*),
\]
then after a gauge transformation the pair extends smoothly over \(0\).

### Capacity argument for \(dF=0\)

Let \(F=-iF_A\), a real closed \(2\)-form on \(B^*\) with \(F\in L^2(B)\). Choose \(\chi_\delta\) with
\[
\chi_\delta=0\ \text{on }B_\delta,\qquad \chi_\delta=1\ \text{off }B_{2\delta},\qquad |d\chi_\delta|\le \frac{2}{\delta}.
\]
In dimension four,
\[
\|d\chi_\delta\|_{L^2}=O(\delta),\qquad \|d\chi_\delta\|_{L^1}=O(\delta^3).
\]
For every test \(1\)-form \(\beta\in C^\infty_c(B)\),
\[
0=\int_{B^*}F\wedge d(\chi_\delta\beta)
 =\int_B \chi_\delta F\wedge d\beta+\int_B F\wedge d\chi_\delta\wedge\beta.
\]
The second term is controlled by
\[
\left|\int F\wedge d\chi_\delta\wedge\beta\right|
 \le \|F\|_{L^2(B_{2\delta})}\,\|d\chi_\delta\|_{L^2}\,\|\beta\|_{L^\infty}
 =o(1).
\]
Thus \(dF=0\) distributionally on all of \(B\). This part is correct.

### Well-posedness of the Coulomb potential

The note solves
\[
da'=F,\qquad d^*a'=0,\qquad \iota_\nu a'|_{\partial B}=0.
\]
This is the standard absolute Hodge problem on the ball. A precise justification is:

- Since \(B\) is contractible, every closed \(L^2\) \(2\)-form is exact in the \(W^{1,2}\) sense.
- The operator \(d\oplus d^*\) on \(1\)-forms with the peripheral condition \(\iota_\nu a'=0\) is elliptic.
- Uniqueness: if \(da=0\), \(d^*a=0\), and \(\iota_\nu a=0\), then on the ball \(a=df\). The equation \(d^*df=0\) gives \(\Delta f=0\), while \(\iota_\nu df=\partial_\nu f=0\). The Neumann problem gives \(f\) constant, hence \(a=0\).
- Existence follows from the Hodge decomposition or, equivalently, from solving the compatible Neumann problem for the gauge function after any primitive of \(F\).

Thus the Coulomb solution exists, is unique, and lies in \(W^{1,2}(B)\). This is the exact repair for the well-posedness point.

### Gauge removal of the singular part

On \(B^*\), write
\[
A=A_0+ia,
\]
where \(A_0\) is the product connection. Since \(da=F=da'\), we have
\[
d(a-a')=0.
\]
Because \(H^1(B^*;\mathbb R)=0\) for the punctured four-ball, there is a real function \(f\in W^{2,2}_{\rm loc}(B^*)\) with
\[
a-a'=df.
\]
After the gauge transformation \(e^{-if}\),
\[
A\mapsto A_0+ia',\qquad \Phi\mapsto \Phi'=e^{-if}\Phi.
\]
The spinor remains bounded. This step is correct.

### Dirac equation across the puncture

With the new gauge,
\[
D_{A_0}\Phi'=-\frac i2 c(a')\Phi'=:\phi.
\]
Since \(a'\in W^{1,2}(B)\subset L^4(B)\) and \(\Phi'\in L^\infty\), one has \(\phi\in L^4(B)\). The same cutoff argument gives, for every test spinor \(\psi\),
\[
\int_B \langle \Phi',D_{A_0}(\chi_\delta\psi)\rangle
   =\int_B \langle \phi,\chi_\delta\psi\rangle+O(\delta^3),
\]
so
\[
D_{A_0}\Phi'=\phi
\]
distributionally on all of \(B\). Ellipticity of \(D_{A_0}\) gives
\[
\Phi'\in W^{1,4}_{\rm loc}.
\]

### Bootstrap

The curvature equation on \(B^*\) is
\[
F_A^+=q(\Phi).
\]
In the gauge \(A=A_0+ia'\), this becomes, up to the fixed Clifford convention,
\[
d^+a'=q(\Phi')
\]
on \(B^*\). Both sides are \(L^1_{\rm loc}\) on \(B\), and equality off a point implies equality distributionally on \(B\). Since \(\Phi'\in W^{1,4}\cap L^\infty\), the quadratic term \(q(\Phi')\) lies in \(W^{1,4}_{\rm loc}\). The elliptic system
\[
d^+a'=q(\Phi'),\qquad d^*a'=0
\]
then gives
\[
a'\in W^{2,4}_{\rm loc}\subset C^{1,\alpha}_{\rm loc}.
\]
Bootstrapping gives smoothness. The spinor equation then gives smoothness of \(\Phi'\). The bootstrap is valid.

### Repairs and hidden hypotheses

- The argument uses essentially that the structure group is abelian. Nonabelian removability would require Uhlenbeck/Feeney–Leness machinery.
- The assumptions \(\Phi\in L^\infty\) and \(F_A\in L^2\) are exactly the needed input. No curvature smallness is used.
- The proof should explicitly say that the equality \(d^+a'=q(\Phi')\) extends across the point because both sides are locally integrable and agree off a set of capacity zero.

### Standard versus new

Point removability for abelian monopoles is known in spirit, but the proof given here is a clean, self-contained version adapted to the orbifold gluing setting. Its value is that it avoids nonabelian removable-singularity theorems entirely.

---

## (b) Lemma 93.Q — equivariant extension and the lift

### Classification of equivariant spin\(^c\) structures

Let \(\Gamma=\frac1{n^2}(1,n-1)\) act linearly on the uniformizer ball \(B\). Since \(B\) equivariantly contracts to \(0\), equivariant spin\(^c\) structures on \(B\) are twists of the canonical complex spin\(^c\) structure by characters
\[
\chi\in \widehat\Gamma\cong \mathbb Z_{n^2}.
\]
On the punctured ball \(B^*\), the quotient is \((0,1)\times L\), where
\[
L=S^3/\Gamma
\]
is a lens space. Equivariant spin\(^c\) structures on \(B^*\) correspond to spin\(^c\) structures on \(L\), hence form an affine space over
\[
H^2(L;\mathbb Z)\cong \mathbb Z_{n^2}.
\]
The restriction map
\[
H^2(B\Gamma;\mathbb Z)\to H^2(L;\mathbb Z)
\]
is an isomorphism for the lens space. Thus the restriction class \(\operatorname{res}(\mathfrak s)\) is well defined as the unique character \(\chi\) such that the pullback of \(\mathfrak s|_{V^{\rm reg}}\) to \(B^*\) is \(S_\chi|_{B^*}\).

This classification is correct.

### Invariance of the Coulomb gauge

In the equivariant trivialization,
\[
S_\chi=B\times \mathbb C^4
\]
with action \(\gamma_0\otimes\chi\), the product connection \(A_0\) is invariant. The original connection is written
\[
A=A_0+ia,
\]
and \(\Gamma\)-invariance of \(A\) means
\[
\gamma^*a=a.
\]
The Coulomb solution \(a'\) constructed in Lemma 93.R is unique for the invariant curvature \(F\) and the invariant metric, with the invariant peripheral condition. Therefore \(a'\) is \(\Gamma\)-invariant.

This step is correct.

### The cocycle \(c_\gamma\)

Since both \(a\) and \(a'\) are invariant,
\[
d(f\circ\gamma-f)=0.
\]
Because \(B^*\) is connected, \(f\circ\gamma-f=c_\gamma\) is constant. The constants satisfy the additive cocycle relation
\[
c_{\gamma\delta}=c_\gamma+c_\delta.
\]
Thus \(c:\Gamma\to\mathbb R\) is a homomorphism. Since \(\Gamma\) is finite and \(\mathbb R\) has no nonzero finite subgroups, \(c_\gamma=0\). Hence the gauge \(e^{-if}\) is \(\Gamma\)-invariant.

This argument is correct. It is important that \(f\) is chosen as a real function on the simply connected punctured ball. If one worked only modulo \(2\pi\), one could see nontrivial characters; the real exactness removes that ambiguity.

### Descent to the orbifold

The gauge-fixed pair \((A_0+ia',\Phi')\) is \(\Gamma\)-invariant and smooth on \(B\). It therefore descends to a smooth orbifold solution on the quotient chart. The orbifold spin\(^c\) structure is exactly \(\operatorname{res}(\mathfrak s)=\chi\).

### Repair and clarification

The note correctly says that the relevant datum is the torsion lift \(\chi\), not a disconnected component of the ordinary gauge group. Indeed,
\[
\pi_0\operatorname{Map}(L,U(1))\cong H^1(L;\mathbb Z)=0.
\]
The nontrivial information is in torsion spin\(^c\) structures and their local characters.

### Standard versus new

The classification of equivariant spin\(^c\) structures on a linear quotient ball is standard. The useful point here is the explicit identification of the lifted orbifold structure with the restriction class and the proof that the removable gauge can be made \(\Gamma\)-invariant without introducing extra holonomy data.

---

## (c) Theorem 93.A — tightness, class transfer, energy convergence, conformal rescaling

### Item 1: spinor mass and irreducibility

The Weitzenböck formula in the normalization of the note is
\[
4\nabla_A^*\nabla_A\Phi+s\Phi+U\Phi=0,
\qquad U=|\Phi|^2.
\]
Taking the inner product with \(\Phi\) gives
\[
4\int|\nabla_A\Phi|^2+\int sU+\int U^2=0.
\]
Therefore
\[
\int U^2\le \int s^-U\le \|s^-\|_{L^2}\|U\|_{L^2},
\]
and hence
\[
\|U\|_{L^2}\le \|s^-\|_{L^2}.
\]
The pointwise maximum principle gives
\[
0\le U_\varepsilon\le \|s^-_\varepsilon\|_{L^\infty}.
\]
The Lemma 86.S gluing family gives a uniform bound
\[
\sup_\varepsilon\|s^-_\varepsilon\|_{L^\infty}\le C_g.
\]
The volume estimate
\[
\operatorname{Vol}_{g_\varepsilon}\{r<R\}\le C(R^4+\rho^4)
\]
then yields
\[
\limsup_{\varepsilon\to0}\int_{\{r<R\}}|\Phi_\varepsilon|^4\le C_gR^4.
\]
Letting \(R\to0\) gives tightness. Combined with the lower bound
\[
\int U_\varepsilon^2=8\int|F^+_{A_\varepsilon}|^2
        \ge 32\pi^2(a^+_{g_\varepsilon})^2
        \ge 32\pi^2 A,
\]
one obtains
\[
\int_V|\Phi_\infty|^4\ge 32\pi^2A.
\]
Thus \(\Phi_\infty\not\equiv0\), and the limit is irreducible. This part is correct.

### Item 2: real determinant class and square

Since the link \(L\) has the rational cohomology of \(S^3\), the maps
\[
H^2(V;\mathbb R)\to H^2(V^{\rm reg};\mathbb R),
\qquad
H^2(M;\mathbb R)\to H^2(M\setminus B;\mathbb R)
\]
are isomorphisms. Pairing \(iF_A/2\pi\) with compactly supported closed forms in the regular part identifies the limiting real class with the image of the smooth determinant class. The rational ball and the cone carry no rational \(H^2\), so the intersection square is preserved:
\[
a_V^2=a_M^2.
\]
This is correct.

### Item 3: energy convergence

Because \(F^+=q(\Phi)\), the spinor tightness gives tightness of the self-dual curvature energy:
\[
\int |F^+_{A_\varepsilon}|^2\to \int |F^+_{A_\infty}|^2.
\]
Chern–Weil gives
\[
\int |F^-_{A_\varepsilon}|^2
   =\int |F^+_{A_\varepsilon}|^2-4\pi^2a_M^2,
\]
and the corresponding identity on \(V\) uses \(a_V^2=a_M^2\). Hence
\[
\int_M|F_{A_\varepsilon}|^2\to\int_V|F_{A_\infty}|^2.
\]
The scalar-spinor term converges because \(s_\varepsilon\) and \(U_\varepsilon\) are uniformly bounded and the filled region has shrinking volume. The integrated Weitzenböck identity then transfers the gradient energy:
\[
\int_M|\nabla_{A_\varepsilon}\Phi_\varepsilon|^2
   \to \int_V|\nabla_{A_\infty}\Phi_\infty|^2.
\]
This is correct.

### Item 4: every orbifold metric and conformal rescaling

This is the main quantifier point.

As written, Theorem 93.A assumes supply for the particular gluing family \(g_\varepsilon\) associated to one orbifold metric \(g\). From that hypothesis alone, one cannot conclude the same theorem for an arbitrary orbifold metric \(g'\) on \(V\). To obtain item 4 literally, one must assume a strengthened supply hypothesis:

> For every orbifold metric \(g'\) on \(V\), and for its associated glued family \(g'_\varepsilon\), some structure in the fixed finite set \(\mathcal S\) carries an unperturbed solution with \((a^+_{g'_\varepsilon})^2\ge A\).

In the main blow-up family \(M=X\#k\overline{\mathbb{CP}}^2\), the \(2^{k+1}\) classes
\[
\pm K_X\pm E_1\cdots\pm E_k
\]
are simultaneously supplied for every metric, and the averaging identity gives a class with projection at least \(A\). Under that stronger application-specific supply, item 4 is valid.

For the LeBrun mixed estimate, however, one does not need the full strength of item 4. It is enough to use conformal covariance of the already constructed limit solution. If
\[
\widehat g=f^{-2}g,
\]
then the Seiberg–Witten equations in dimension four are conformally covariant with
\[
\widehat A=A,\qquad \widehat\Phi=f\Phi.
\]
Then
\[
D_{\widehat A}\widehat\Phi=0,\qquad F_{\widehat A}^+=q_{\widehat g}(\widehat\Phi),
\]
and
\[
\int_V|\widehat\Phi|^4\,d\operatorname{vol}_{\widehat g}
 =\int_V|\Phi|^4\,d\operatorname{vol}_g
 \ge 32\pi^2A.
\]
Thus the conformal family needed for LeBrun’s mixed estimate is obtained from the single limiting solution. The note’s conclusion is therefore correct for the mixed estimate, but the proof should either strengthen the supply hypothesis or explicitly invoke conformal covariance.

### Orbifold LeBrun estimates

From the transferred lower bound
\[
\int_V U^2\ge 32\pi^2A
\]
and the conformal covariance just described, one obtains the scalar estimate
\[
\int_V s^2\ge 32\pi^2A
\]
and the mixed estimate
\[
\int_V(s-\sqrt6|W^+|)^2\ge 72\pi^2A
\]
on \(V\), with the same \(A\) as on \(M\). This is correct, subject to the supply clarification above.

---

## (d) Lemma 93.I — index transfer and the Kawasaki computation

### APS decomposition

Cut both \(M\) and \(V\) along the common link \(L\). The spin\(^c\) Dirac operator on \(L\), with flat determinant twist and the round metric, is invertible. Indeed, \(L\) has positive scalar curvature, and with a flat determinant connection the spin\(^c\) Lichnerowicz formula gives
\[
D^2=\nabla^*\nabla+\frac{s}{4},
\]
so there is no kernel. Therefore APS gluing has no additional link-kernel correction.

One has
\[
\operatorname{ind}(M)
 =\operatorname{ind}_{\rm APS}(V^{\rm reg}_{\rm tr})
  +\operatorname{ind}_{\rm APS}(B_{n,1},\mathfrak s|_B),
\]
and
\[
\operatorname{ind}(V)
 =\operatorname{ind}_{\rm APS}(V^{\rm reg}_{\rm tr})
  +\operatorname{ind}_{\rm APS}(C(L),\chi).
\]
Thus index transfer reduces to showing that both local pieces have APS index zero.

### Filler piece

The rational ball \(B_{n,1}\) has torsion \(H^2\), so every determinant line admits a flat connection. Şuvaina’s ALE metric is Ricci-flat. With a flat determinant connection,
\[
D^2=\nabla^*\nabla.
\]
On the ALE end, in the relevant weight interval containing the \(L^2\) and APS weights, any solution decaying at the required rate is parallel by the Bochner identity, and a nonzero parallel spinor cannot have the required decay on an ALE end of four-dimensional volume growth. Hence there are no solutions in the weight window, and the weighted index is zero. Conformal covariance of the Dirac operator identifies the weighted index with the APS index after writing the end in cylindrical form. Therefore
\[
\operatorname{ind}_{\rm APS}(B_{n,1},\mathfrak s|_B)=0.
\]

This argument is structurally correct. To make it completely explicit, the note should state the weight interval and verify that it contains no indicial roots. This is standard in ALE Dirac theory, but it is the one analytic point that should be written carefully.

### Cone piece

For the cone, replace the flat cone by a \(\Gamma\)-invariant positive-scalar-curvature cap, for example a quotient of a round hemisphere with a cylindrical collar. With a flat determinant twist, the Lichnerowicz formula again gives no kernel in either chirality. The link Dirac is invertible, so the APS index of the cone piece is zero:
\[
\operatorname{ind}_{\rm APS}(C(L),\chi)=0.
\]
This is correct for the characters \(\chi\) that arise as restrictions of smooth structures on \(M\).

### Kawasaki computation

The script computes the Kawasaki fixed-point term for the Dolbeault/spin\(^c\) index twisted by the local character \(\zeta^m\):
\[
\delta(m)=\frac1{n^2}\sum_{k=1}^{n^2-1}
   \frac{\zeta^{km}}
        {(1-\zeta^{-k})(1-\zeta^{-k(n-1)})}.
\]
The data show:

1. \(\delta(0)=(1-1/n^2)/12\), matching the Riemann–Roch/Noether consistency condition.
2. The signature defect is
   \[
   \frac23\left(1-\frac1{n^2}\right),
   \]
   and the identity
   \[
   2e_{\rm orb}+3\tau_{\rm CW}=2e+3\tau
   \]
   holds.
3. For \(n=2,\dots,8\),
   \[
   \{m:\delta(m)=\delta(0)\}=\{0,n,2n,\dots,(n-1)n\}.
   \]
   This is exactly the set of characters extending over the rational ball.

The computation is an independent local confirmation of Lemma 93.I for the characters that come from smooth spin\(^c\) structures. It also shows that non-extendible local twists would change the fixed-point contribution.

### Repair concerning generality

The JSON computation verifies the exact equality only for \(2\le n\le 8\). For the theorem as stated for all \(n\), one needs either:

- a general proof that the APS index of the filler and cone pieces vanishes for every extendible character, which the analytic argument already supplies; or
- a general closed-form evaluation of the Kawasaki sum showing \(\delta(nj)=\delta(0)\) for all \(j\).

The script alone does not prove the all-\(n\) statement, though it strongly supports it.

### Expected dimension

Because the Dirac indices agree, the expected dimensions of the corresponding Seiberg–Witten moduli problems agree. For basic classes of \(X\#k\overline{\mathbb{CP}}^2\) with expected dimension zero on the smooth side, the corresponding orbifold structures have expected dimension zero. This is correct.

---

## (e) Proposition 93.Y — complex realization and self-similarity

### Holomorphic choice of the PPS sphere

For odd \(n\ge3\), PPS embeds \(B_{n,1}\) into a neighbourhood \(V_{-4}\) of a \((-4)\)-sphere. The note chooses the sphere
\[
S=E_1-E_2-E_3-E_4.
\]
This class has square \(-4\) and can be represented by a holomorphic curve obtained by successive blow-ups of an exceptional curve. For \(n=2\), the analogous curve has square \(-3\).

The tubing construction in Theorem 102.R uses a sphere in the class \(E_1+E_2+E_3+E_4\). The two classes differ by sign changes of some exceptional classes. Such sign changes are realized by diffeomorphisms of the blow-up summands; complex conjugation on the \(\overline{\mathbb{CP}}^2\) factors is the standard source. This is plausible and standard, but the note should explicitly cite the smooth classification/diffeomorphism result that realizes these reflections in the required orientation class.

### Grauert linearization

For a holomorphic curve \(C\cong\mathbb P^1\) with normal bundle \(N=\mathcal O(-m)\), \(m\ge1\), Grauert’s linearization theorem applies because
\[
H^1(\mathbb P^1,T_{\mathbb P^1}\otimes N^{-\nu})=
H^1(\mathbb P^1,\mathcal O(2+m\nu))=0,
\]
and
\[
H^1(\mathbb P^1,N^{1-\nu})=
H^1(\mathbb P^1,\mathcal O(m(\nu-1)))=0
\]
for all \(\nu\ge1\). Thus a neighbourhood of the holomorphic \((-m)\)-curve is biholomorphic to the linear disk bundle. This justifies inserting the PPS complex model into a projective surface.

### The PPS family and the orbifold identification

In the PPS construction, the general fibre \(W_t\) is isomorphic to \(V_{-4}\), while the central fibre is obtained by contracting the chain
\[
C_{n,1}=[n+2,2,\dots,2].
\]
The complement of the rational ball in the general fibre matches the complement of the cone point in the central fibre. Therefore replacing the embedded \(B_{n,1}\subset M\) by the cone gives an orbifold diffeomorphic to
\[
Y=\widehat X/C_{n,1},
\]
where \(\widehat X\) is \(X\) blown up at the required points.

This is the correct geometric picture.

### Projectivity of \(Y\)

The note calls \(Y\) a projective complex orbifold. Contracting a negative definite configuration of rational curves in a projective surface yields a normal analytic surface; algebraicity follows from standard contraction theory, for example Artin’s algebraization or Grauert’s contractibility plus Moishezon/projectivity arguments. However, projectivity is not automatic from the analytic contraction alone unless one verifies the existence of an ample divisor or cites the appropriate theorem. The statement should include that standard input.

### \(K_Y\) is not nef

The discrepancies of the minimal resolution chain are
\[
a_i=-\frac{n-i}{n},\qquad i=1,\dots,n-1.
\]
If a curve \(C\) meets the \(i\)-th component of the chain transversely once, then
\[
K_Y\cdot C=-1-a_i=-\frac{i}{n}<0.
\]
The PPS construction supplies such a curve. Hence \(K_Y\) is not nef. This is correct.

One subtlety: the curve meeting the chain may pass through the orbifold point after contraction, and its self-intersection on \(Y\) need not remain \(-1\). That does not affect the computation of \(K_Y\cdot C\), because the formula uses the pullback to the resolution. The conclusion \(K_Y\) not nef remains valid.

### Consequence: no Kähler–Einstein metric in this orientation

Since \(K_Y\) is not nef, the orbifold Aubin–Yau theorem does not supply a Kähler–Einstein metric with \(s<0\). Moreover, the Chern–Weil transfer gives the same LeBrun scalar obstruction as on \(M\). Thus any Einstein orbifold metric on \(V\) in this orientation would be non-Kähler. This conclusion is correct.

### Transfer principle

The note states that every obstruction built from supplied Seiberg–Witten fields, Chern–Weil integrals, and index counts applies identically to \(V\) and \(M\).

This is correct for obstructions of the following type:

- existence of supplied unperturbed solutions;
- the energy identities and the lower bound \(\int U^2\ge32\pi^2A\);
- equality of determinant squares \(a_V^2=a_M^2\);
- equality of the plus-side characteristic number \(2\chi+3\tau\);
- equality of Dirac indices for restricted structures.

It is not, by itself, a proof that full Seiberg–Witten invariants, obstruction bundles, or refined moduli-space structures agree. The note itself lists the orbifold–smooth invariant equality as not proved. The transfer principle should therefore be phrased as an equivalence of integral/energy/index obstructions, not as a blanket equivalence of all Seiberg–Witten moduli obstructions.

---

## (f) Proposition 93.C — local characters and forced zeros

### Restriction to \(V_{-4}\)

For \(x\in H^2(M)\),
\[
x|_{V_{-4}}=(x\cdot S)u,
\]
where \(u\) generates \(H^2(V_{-4})\cong\mathbb Z\). This is standard for a disk bundle over \(S\).

With
\[
S=E_1-E_2-E_3-E_4,
\]
one has
\[
E_i\cdot S=-\varepsilon_i,
\qquad
\varepsilon=(1,-1,-1,-1).
\]
Also
\[
K_M\cdot S=2,
\]
so
\[
K_M|_{V_{-4}}=2u.
\]
This is correct.

### The factor \(h=2^{-1}\bmod n\)

Inside the rational ball,
\[
H^2(B;\mathbb Z)\cong\mathbb Z_n.
\]
The local canonical class has Cartier index \(n\), so \(K|_B\) has order \(n\). Since \(K|_B=2u_B\) and \(n\) is odd, \(2\) is invertible mod \(n\). Put
\[
h=2^{-1}\bmod n.
\]
Then
\[
u_B=hK|_B.
\]

The local twist \(j\) is the class of the twisting line, not the full determinant class. For the basic class
\[
c_1=-K_M+2\sum_{i\in F}E_i,
\]
the twisting line relative to the canonical reference is
\[
\sum_{i\in F}E_i.
\]
Its restriction to \(B\) is
\[
\sum_{i\in F\cap\{1,2,3,4\}}(E_i\cdot S)u_B
 =\sum_{i\in F\cap\{1,2,3,4\}}(-\varepsilon_i)u_B.
\]
Measured in units of \(K|_B\), this becomes
\[
j_F=\sum_{i\in F\cap\{1,2,3,4\}}(-\varepsilon_i h)\pmod n.
\]
Thus the factor \(h\) is correct once the distinction between determinant class and twisting line is made explicit. This is the precise clarification needed in Prop. 93.C.

### Forced-zero counts

Step 89 shows that the spinor value at the orbifold point can be nonzero only for twists
\[
j\in\{0,1\}.
\]
Equivalently,
\[
m\in\{0,n\}\subset \mathbb Z_{n^2}.
\]
For \(n=3\), the script gives the twist multiset
\[
0:5,\quad 1:5,\quad 2:6,
\]
so \(6/16\) classes are forced to vanish at \(p\).

For every odd \(n\ge5\), one can prove the \(8/16\) count directly. Since
\[
h=\frac{n+1}{2},
\]
the four local increments are
\[
(-h,h,h,h).
\]
Subset sums without the first entry are \(rh\), \(r=0,1,2,3\), with multiplicities \(1,3,3,1\). The allowed values are:
\[
r=0\Rightarrow 0,\qquad r=2\Rightarrow 2h=1.
\]
These contribute \(1+3=4\) allowed sums.

Subset sums with the first entry are \(-h+rh\). The allowed values are:
\[
r=1\Rightarrow 0,\qquad r=3\Rightarrow 2h=1.
\]
These contribute \(3+1=4\) allowed sums.

For \(n\ge5\), the remaining sums are not \(0\) or \(1\). Hence exactly \(8\) of the \(16\) local sign classes have nonzero spinor value, and \(8/16\) are forced to vanish. The data file verifies this for \(n=3,5,\dots,15\), and the argument above proves it for all odd \(n\ge5\).

For \(n=2\), the extendible set and the allowed set coincide, so no supplied class has a forced zero. This is consistent with the local isotropy calculation.

### Hidden hypotheses

Prop. 93.C uses:

- the complex-model realization of Prop. 93.Y;
- the identification of the canonical local lift with the Milnor-fibre canonical class;
- the convention that the reference basic class \(-K_M\) has local twist \(j=0\);
- odd \(n\), so that \(2\) is invertible mod \(n\).

If \(X\) has additional basic classes beyond \(\pm K_X\), their intersections with \(S\) would contribute additional local twists. The proposition as stated concerns the standard blow-up family around the four exceptional classes meeting \(V_{-4}\).

---

## (g) Lemma 93.W — local Einstein algebra at a Wahl point

The \(\Gamma\)-weights on complex coordinates are
\[
1,\quad n-1.
\]
Thus \(\Lambda^{2,0}\) has weight
\[
1+(n-1)=n.
\]
The self-dual two-forms decompose as
\[
\Lambda^+_0=\mathbb R\omega_0\oplus \operatorname{Re}\Lambda^{2,0},
\]
with weights
\[
0,\quad \pm n.
\]
The traceless symmetric square \(\operatorname{Sym}^2_0\Lambda^+\) therefore has weights
\[
0,\quad \pm n,\quad \pm2n.
\]
For \(n\ge3\), neither \(n\) nor \(2n\) is zero mod \(n^2\). Hence the invariant part of \(\operatorname{Sym}^2_0\Lambda^+\) is one-dimensional. Consequently every invariant self-dual two-form at \(p\) is a multiple of \(\omega_0\), and every invariant traceless symmetric square element has the algebraic form
\[
W^+(p)=\mu\,\operatorname{diag}(2,-1,-1).
\]
For \(n=2\), the weight \(2n=4\) is zero mod \(4\), so the invariant subspace is larger; the note’s distinction between \(n=2\) and \(n\ge3\) is correct.

Thus for \(n\ge3\), an Einstein orbifold metric has Kähler-type \(W^+\) algebra at the Wahl point, but this does not imply global Kählerness and does not relate \(\mu\) to \(s/12\). The lemma is correct.

---

# Standard versus new material

### Standard ingredients

- Weitzenböck formulas and maximum principle for monopoles.
- LeBrun’s scalar and mixed curvature estimates.
- APS gluing with invertible link Dirac.
- Kawasaki’s orbifold index theorem and Dedekind-sum signature defects.
- Grauert linearization of neighbourhoods of negative curves.
- PPS embeddings of Wahl rational balls.
- Conformal covariance of the four-dimensional Seiberg–Witten equations.

### New or session-specific contributions

- The complete fixed-supply field-limit theorem across a shrinking Wahl filler.
- The elementary abelian removability proof adapted to the orbifold gluing setting.
- The index-transfer lemma identifying smooth and orbifold expected dimensions for restricted spin\(^c\) structures.
- The explicit local character counts for supplied blow-up classes and the resulting forced spinor zeros.
- The self-similarity observation: the Wahl alternative is the same Q1 problem posed on a singular non-minimal general-type orbifold member of the smoothing family.
- The local \(W^+\) algebra at a Wahl point and the distinction between \(n=2\) and \(n\ge3\).

---

# The missing implication in §6

The note identifies the missing implication as a quantitative estimate, for Einstein orbifold metrics with \(s=-\lambda<0\), of something like
\[
\int(\lambda^2-U_\sigma^2)
\quad\text{or}\quad
\|d\alpha_\sigma\|^2
\]
for a class whose spinor is forced to vanish at the orbifold point, uniform in the geometry; or else a construction showing that the cost of that forced zero can be made arbitrarily small.

There are two natural mathematical routes.

---

## Route 1: singular conformal blow-up using the forced double zero

The forced zero is not merely a pointwise condition. Step 89 gives
\[
\Phi(p)=0,\qquad \nabla\Phi(p)=0
\]
for the relevant twists. Thus \(\Phi\) vanishes to order at least two at \(p\).

In four dimensions, the Green’s function of a second-order conformally covariant operator has a pole of order two:
\[
G_p(r)\sim c\,r^{-2}+m+O(r).
\]
The double zero of \(\Phi\) is exactly strong enough to cancel this pole under the conformal spinor transformation.

Let \(L_g\) be a suitable conformally covariant operator, for example a shifted Yamabe operator adapted to the Einstein metric \(s=-\lambda\). Let \(G_p\) be its positive Green’s function at the orbifold point. Consider the conformal metric
\[
\widehat g=G_p^2 g
\]
on \(V\setminus\{p\}\). Under the conformal change, the spinor transforms by
\[
\widehat\Phi=G_p^{-1}\Phi.
\]
Because \(\Phi=O(r^2)\) and \(G_p^{-1}=O(r^2)\), the transformed spinor remains bounded near the new end. Thus the forced double zero makes the singular conformal blow-up admissible.

The new metric \(\widehat g\) is asymptotically flat or ALE near the end corresponding to \(p\). The integrated Weitzenböck identity on \((V\setminus\{p\},\widehat g)\) then acquires an end term. Schematically,
\[
4\int|\widehat\nabla\widehat\Phi|^2
 +\int \widehat s\,\widehat U
 +\int \widehat U^2
 =\text{end term}.
\]
The end term is controlled by the constant part \(m\) of the Green’s function, or equivalently by a Yamabe/Green’s-function mass. If one can prove a uniform lower bound for this mass in terms of \(\lambda\), \(A\), \(k\), and the orbifold group, then the forced zero yields a genuine extra term in the Einstein obstruction.

This is the most promising analytic route by which a point condition could enter a global integral inequality. The reason is that ordinary point zeros have zero \(W^{1,2}\) capacity in dimension four, so they do not by themselves force an \(L^2\) gradient cost. The Green’s-function conformal blow-up is a mechanism that can convert the local vanishing order into a global end contribution.

The unresolved mathematical questions are:

1. existence and positivity of the relevant Green’s function on an Einstein orbifold with \(s<0\);
2. the precise conformal transformation law for the monopole energy and the end term;
3. whether the end term has a universal lower bound, or whether it can vanish in collapsing or degenerating families.

If the end term can be made arbitrarily small, this route will show that forced zeros do not produce a new Einstein obstruction.

---

## Route 2: Kähler-orbifold test metrics with small forced-zero cost

The complex orbifold \(Y\) from Prop. 93.Y is of general type but \(K_Y\) is not nef. There are curves \(C\) through the Wahl point with
\[
K_Y\cdot C<0.
\]
In the resolution, such curves can be chosen to meet the Wahl chain. On the Kähler cone of the resolution, one can take Kähler classes for which the area of \(C\) is arbitrarily small while all other relevant curve areas remain positive. Pushing these classes forward gives Kähler orbifold metrics on \(Y\) in which the curve carrying the forced zero has small area.

In the Kähler monopole picture, spinors correspond to holomorphic sections, and zeros along divisors contribute energy proportional to the area of those divisors. If the forced zero at \(p\) is realized by a holomorphic section vanishing along such a curve \(C\), then the energy cost is of order
\[
\operatorname{Area}_\omega(C).
\]
As \(\operatorname{Area}_\omega(C)\to0\), the cost of the forced zero tends to zero. This gives a concrete Kähler-orbifold family showing that no uniform lower bound can come from the forced zero alone, at least within the Kähler category.

A stronger version of this route would be:

1. Contract all curves \(C\) with \(K_Y\cdot C<0\) that pass through or near the Wahl point.
2. Check whether the resulting orbifold has nef or ample canonical class and only admissible quotient singularities.
3. If so, apply the orbifold Aubin–Yau theorem to obtain a Kähler–Einstein orbifold with \(s<0\).
4. Use the Wahl filler and Lemma 86.S to produce smoothing metrics on \(M\) with Einstein gap tending to zero.

This would directly connect the forced-zero geometry to the second alternative in the Einstein-gap problem.

At present, this is a program rather than a theorem. The essential point is that the local forced zero is carried by curves whose geometric size is not topologically fixed. Unless one can tie the zero to a conformal end term as in Route 1, the local defect can plausibly be made small.

---

# Final summary

The Step-93 theorem package is mathematically coherent after the following repairs:

- State the Hodge problem in Lemma 93.R as the absolute Hodge decomposition with peripheral condition \(\iota_\nu a'=0\).
- Make explicit that the local twist in Prop. 93.C is the twisting line, half the determinant change, measured in units of \(K|_B\).
- Correct the quantifier in Theorem 93.A item 4: arbitrary orbifold metrics require metric-wise supply; conformal rescalings can be handled by conformal covariance of the limit solution.
- Narrow the transfer principle to integral, energy, and index obstructions unless full orbifold–smooth Seiberg–Witten invariant equality is independently established.
- Supplement the Kawasaki computation with a general proof or cite the analytic index-transfer argument for all \(n\).
- Add the standard projectivity/contraction input for the complex orbifold \(Y\).

With these repairs, the Step-93 result is a strong and genuinely useful advance: it shows that the Wahl orbifold channel is not a cheaper route to Q1 but is instead Q1 itself posed on a singular, non-minimal, general-type orbifold with the same transferred field, index, and curvature-integral data. The remaining substance is precisely the missing local-to-global Einstein implication, for which the Green’s-function conformal blow-up and the small-curve Kähler construction are the two most promising directions.