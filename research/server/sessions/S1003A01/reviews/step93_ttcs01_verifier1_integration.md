# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step93_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step93_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-93 note line by line as a mathematician. Goal context: Einstein gaps on four-manifolds; Q1 asks whether X#kCP2bar (X general type, k<A/3, A=K_X^2) carries Einstein metrics, and the Wahl-orbifold channel V (A02 Theorem 102.R) is one alternative. Check in particular: (a) Lemma 93.R abelian point removability — is the capacity argument correct (dF=0 across 0, Dirac equation across 0), is the Coulomb solution with boundary condition iota_nu a'=0, d*a'=0, da'=F on the ball well-posed and unique, is the bootstrap valid starting from a' in W^{1,2} and bounded Phi? (b) Lemma 93.Q: classification of Gamma-equivariant spin^c structures on B and B*, uniqueness implying Gamma-invariance of a', the cocycle argument c_gamma=0, identification with res(s). (c) Theorem 93.A items 1-4 (tightness, class transfer, energy convergence) and the claim that the orbifold LeBrun mixed estimate follows by applying WFL to conformal rescalings. (d) Lemma 93.I: APS index vanishing on the Ricci-flat ALE Wahl filler (flat determinant, weight window, conformal covariance) and on the cone (psc cap), boundary invertibility, and whether the Kawasaki computation in wahl_index_transfer.json correctly supports it. (e) Prop 93.Y: is the Wahl orbifold of Theorem 102.R really orbifold-diffeomorphic to a complex orbifold Y once the PPS sphere is chosen holomorphic (Grauert linearization; reflection diffeomorphisms; PPS family W_t, W_0); is K_Y not nef (discrepancies a_i=-(n-i)/n, K.C); is the 'transfer principle' that field/index/curvature-integral obstructions coincide on V and M justified? (f) Prop 93.C: restriction maps x|_{V_-4}=(x.S)u, K|_B of order n, the twist formula and forced-zero counts (data file). (g) Lemma 93.W isotropy. Report errors with exact repairs, identify any hidden hypothesis, and say which statements are standard/known versus new. Also give your best mathematical suggestion for the 'missing implication' in §6: is there a plausible route to a quantitative Einstein estimate using forced orbifold zeros, or a construction on the Kahler orbifold Y showing the forced-zero cost can be made small?

## Integrated Scientific Memo

# Verification memo: Step 93

## Main verdict

The fixed-field limit is repairable and substantially correct. It proves more than convergence away from the singularity: for the prescribed recovery metrics, **no spinor mass or abelian curvature energy is lost in the filler or neck**.

The note nevertheless contains several actual errors:

- the removable gauge has a determinant/spinor factor-of-two error;
- \(W^{2,4}\not\hookrightarrow C^{1,\alpha}\) in dimension four;
- Theorem 93.A(4) requires stronger supply quantifiers than the stated hypothesis;
- unperturbed Seiberg–Witten equations are **not** conformally covariant in the manner proposed in one verification;
- the index script is numerical, not exact cyclotomic arithmetic;
- the complex realization is justified only for a suitably chosen, marked complex-model embedding—not every embedding in Theorem 102.R;
- the blanket transfer principle is false: the \(W^-\)-side characteristic number changes.

The index identity can be justified by standard ALE–APS analysis, and its local Kawasaki identities admit an elementary all-\(n\) proof given below. The forced-zero computation also yields an important strengthening: **a supplied class retaining the lower bound \(A\) can be selected from the forced-zero subfamily**.

---

## 1. Lemma 93.R: removability

### Distributional extension of curvature

The capacity argument is correct. For the stated cutoffs,
\[
\|d\chi_\delta\|_2=O(\delta),\qquad
\|d\chi_\delta\|_1=O(\delta^3).
\]
Consequently,
\[
\left|\int F\wedge d\chi_\delta\wedge\beta\right|
\le C_\beta\|F\|_{L^2(B_{2\delta})}\,\delta\longrightarrow0.
\]
Thus \(dF=0\) distributionally on \(B\). No point-supported curvature source survives.

### The Coulomb primitive

On a smooth ball, the problem
\[
da'=F,\qquad d^*a'=0,\qquad \iota_\nu a'=0
\]
has a unique \(W^{1,2}\) solution for distributionally closed \(F\in L^2\). The statement is correct, but “because \(H^1=H^2=0\)” should be expanded into the relevant Hodge theorem:

1. The Sobolev de Rham/Poincaré theorem gives a \(W^{1,2}\) primitive \(b\) of \(F\).
2. Solve the compatible scalar Neumann problem to replace \(b\) by \(b-dv\), imposing coclosedness and zero normal component.
3. A difference \(h\) between two solutions satisfies
   \[
   dh=d^*h=0,\qquad \iota_\nu h=0.
   \]
   It is an absolute harmonic one-form and vanishes since \(H^1(B;\mathbb R)=0\).

This is the first-order Hodge problem; it does **not** require an additional boundary condition \(\iota_\nu F=0\).

### Gauge correction: a genuine factor-of-two error

The note uses \(A\) as the **determinant connection**, as witnessed by
\[
D_A=D_{A_0}+\frac i2c(a).
\]
With the convention
\[
(A,\Phi)\mapsto(A-2u^{-1}du,u\Phi),
\]
if \(a-a'=df\), the required gauge is
\[
u=e^{if/2},
\]
not \(e^{-if}\). Indeed,
\[
A-2u^{-1}du=A_0+i(a-df)=A_0+ia'.
\]
An opposite gauge convention changes the sign, but not the factor \(1/2\).

The real primitive \(f\) exists globally on \(B^*\), since \(H^1(B^*;\mathbb R)=0\). Thus taking this square-root gauge causes no topological difficulty.

### Distributional extension of the Dirac equation

After the corrected gauge,
\[
D_{A_0}\Phi'=-\frac i2c(a')\Phi'\in L^4,
\]
because \(a'\in W^{1,2}\subset L^4\) and \(\Phi'\) is bounded. The cutoff error is bounded by
\[
C\|\Phi'\|_\infty\|\psi\|_\infty\|d\chi_\delta\|_1
=O(\delta^3).
\]
The Dirac equation therefore holds distributionally across \(0\), and interior elliptic regularity gives
\[
\Phi'\in W^{1,4}_{\rm loc}.
\]
This argument is correct.

### Bootstrap correction

The asserted embedding
\[
W^{2,4}\subset C^{1,\alpha}
\]
is false in real dimension four. A valid bootstrap is:
\[
\begin{aligned}
&\Phi'\in W^{1,4}\cap L^\infty
   \ \Longrightarrow\ q(\Phi')\in W^{1,4},\\
&(d^*+d^+)a'=(0,\widetilde q(\Phi'))
   \ \Longrightarrow\ a'\in W^{2,4},\\
&a'\in W^{2,4}
   \ \Longrightarrow\ a'\in C^{0,\alpha}\cap W^{1,p}
   \quad(\alpha<1,\ p<\infty),\\
&D_{A_0}\Phi'=-\tfrac i2c(a')\Phi'
   \ \Longrightarrow\ \Phi'\in W^{1,p}\quad(p<\infty),\\
&p>4
   \ \Longrightarrow\ a'\in W^{2,p}\subset C^{1,\alpha}.
\end{aligned}
\]
Iteration gives smoothness. Here \(\widetilde q\) denotes the real-form version of \(q\); the displayed equation \(d^+a'=q(\Phi')\) in the note suppresses the factor converting imaginary curvature to real curvature.

Equality of the curvature equation across the point follows simply because both sides are locally integrable and agree almost everywhere. No further capacity argument is needed for that step.

**Conclusion:** Lemma 93.R is proved after these two corrections. Its ingredients are standard abelian Hodge and elliptic theory; the short proof is a useful adaptation, not a new general removability phenomenon.

---

## 2. Lemma 93.Q: equivariant extension and the marked lift

The classification is correct, with the full spin\(^c\) lift retained.

Relative to the canonical \(U(2)\)-induced lift, equivariant spin\(^c\) structures over \(B\) form a torsor for
\[
\widehat\Gamma=H^2(B\Gamma;\mathbb Z)\cong\mathbb Z_{n^2}.
\]
On \(B^*\), equivariant structures descend to structures on
\[
L=S^3/\Gamma.
\]
Restriction is an affine bijection because
\[
H^2(B\Gamma;\mathbb Z)\longrightarrow H^2(L;\mathbb Z)
\]
is an isomorphism. Thus the **marked structure on the complement** determines a unique orbifold extension. For even \(n\), its determinant alone does not determine it: twisting doubles the character and loses two-torsion information.

For the analytic argument, choose a \(\Gamma\)-invariant ball, metric, reference connection and trivialization. Uniqueness of the Coulomb primitive gives
\[
\gamma^*a'=a'.
\]
Since \(a\) is also invariant,
\[
f\circ\gamma-f=c_\gamma.
\]
The constants are an additive homomorphism from the finite group \(\Gamma\) to \(\mathbb R\), hence vanish. The corrected gauge \(e^{if/2}\) is therefore invariant.

The spinor is **equivariant under its specified fiber representation**, rather than invariant as an ordinary \(\mathbb C^4\)-valued function. Its smooth extension remains equivariant by continuity. This proves that the extension is precisely \(\operatorname{res}(\mathfrak s)\), without an additional character shift.

The note correctly distinguishes
\[
[L,U(1)]=H^1(L;\mathbb Z)=0
\]
from nontrivial torsion line bundles and flat characters. There is no disconnected ordinary gauge sector to preserve.

---

## 3. Theorem 93.A and the mixed estimate

### Items 1–3

These follow with the repaired removability lemma and the recorded recovery-family estimates.

At \(\rho=\varepsilon^{2/3}\),
\[
\rho^{-2}\bigl[\rho^2+(\varepsilon/\rho)^4\bigr]=O(1).
\]
Thus scalar curvature is uniformly bounded, and the monopole maximum principle gives \(U_j\le C_g\). Shrinking volume then yields the **full** tightness estimate
\[
\limsup_{j\to\infty}\int_{\{r<R\}}U_j^2\le CR^4,
\]
including annular tails.

The normalization is consistent:
\[
\int U_j^2=8\int|F_{A_j}^+|^2
\ge32\pi^2(a_{g_j}^+)^2\ge32\pi^2A.
\]
Finite selection must select actual spin\(^c\) structures carrying **unperturbed** solutions, not merely determinant classes or chamber-dependent “basic classes.”

Local abelian gauges and the same repaired elliptic bootstrap give smooth convergence on compact subsets of the regular part. Gauge patching is performed on the fixed restricted bundle. Flat connection parameters are controlled modulo integral gauge periods; they need not change the bundle’s topological class.

The cohomological identifications and square transfer are correct:
\[
H^2(M;\mathbb R)\cong H^2(V^{\rm reg};\mathbb R)
\cong H^2(V;\mathbb R),\qquad a_M^2=a_V^2.
\]
Compactly supported closed two-forms on the regular part detect the class.

Then
\[
\int|F_j^+|^2\to\int|F_\infty^+|^2
\]
follows from spinor tightness, and
\[
\int|F_j^-|^2=\int|F_j^+|^2-4\pi^2a_M^2
\]
gives full curvature-energy convergence. Finally, bounded scalar curvature and bounded \(U_j\) give convergence of \(\int s_jU_j\), and the integrated Weitzenböck identity gives gradient-energy convergence.

This excludes hidden **abelian ASD energy**, not metric \(W^-\)-energy.

### Item 4: repair the quantifiers

As stated, hypothesis (S) concerns the recovery family for one fixed \(g\). It does not imply supply for recovery families associated with arbitrary \(g'\).

Replace item 4 by:

> If the same finite family is metric-wise supplied on \(M\), with the stated projection-selection property, then the theorem applies separately to the recovery family of every orbifold metric on \(V\).

That strengthened hypothesis holds in the intended application when the standard signed blow-up structures are genuinely monopole structures for all smooth metrics. For \(b^+=1\), the appropriate chamber/supply theorem must still be stated.

The limiting structure and solution can vary with the metric. No common solution for all metrics is asserted.

### Conformal rescaling: reject the false shortcut

There is no general conformal covariance of the unperturbed Seiberg–Witten system with \(A\) unchanged and \(\widehat\Phi=f\Phi\).

For \(\widehat g=\Omega^2g\), Dirac covariance under the natural fiber identification is
\[
D_{\widehat g,A}(\Omega^{-3/2}\Phi)
=\Omega^{-5/2}D_{g,A}\Phi.
\]
The curvature equation instead requires spinor scaling \(\Omega^{-1}\). These exponents differ. Scaling by \(\Omega^{-1}\) introduces a derivative term in the Dirac equation.

Accordingly, the mixed estimate should be justified either by:

1. **Fresh supply and WFL for each conformal metric**, followed by the usual orbifold version of LeBrun’s rescaling argument; or
2. **The direct curvature-integral recovery argument already recorded in A02 §4:** the filler has \(s=W^+=0\), while the transition contribution tends to zero, so the smooth mixed estimate passes directly to \(V\).

The second is the shortest source-supported proof:
\[
\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A.
\]
The result is correct; conformal covariance of an existing monopole is not its proof.

---

## 4. Lemma 93.I: index transfer and an exact all-\(n\) local calculation

### Boundary invertibility

For the unit round lens-space metric and a flat determinant connection, the twisted spin\(^c\) Dirac operator is invertible. Friedrich’s estimate in dimension three gives
\[
|\mu|\ge\frac32.
\]
Equivalently, lift to the round \(S^3\): twisting selects equivariant eigenspinors and cannot introduce eigenvalues absent upstairs.

APS gluing therefore has no boundary-kernel correction. The determinant connection on the common collar can be chosen flat, since its class there is torsion.

### ALE filler: make the weight statement explicit

Every determinant line on \(B_{n,1}\) admits a flat connection. With the Ricci-flat ALE metric,
\[
D_A^2=\nabla_A^*\nabla_A.
\]

On the flat model end,
\[
D=r^{-1}c(dr)\bigl(r\partial_r+\tfrac32+D_L\bigr).
\]
An eigenspinor with link eigenvalue \(\mu\) has radial exponent
\[
-\frac32-\mu.
\]
Because \(|\mu|\ge3/2\), there are no indicial exponents in \((-3,0)\).

Under
\[
\widehat h=r^{-2}h,\qquad t=\log r,\qquad
\widehat\psi=r^{3/2}\psi,
\]
the end becomes asymptotically cylindrical. Its \(L^2\) condition corresponds to the radial threshold \(-3/2\); ordinary ALE \(L^2\) corresponds to threshold \(-2\). Both lie in the same root-free interval \((-3,0)\). Standard ALE elliptic asymptotics therefore identify the APS/cylindrical kernels with decaying ALE harmonic spinors; their decay is at least \(O(r^{-3+\eta})\) for arbitrarily small \(\eta>0\), which suffices.

These spinors are ALE \(L^2\). Applying the Bochner identity with cutoffs shows they are parallel; infinite volume and decay then force zero. The argument applies to both chiral kernels, including the adjoint problem.

A deformation of the asymptotically cylindrical end to an exact product end preserves the Fredholm index because the limiting boundary operator is invertible. Hence
\[
\operatorname{ind}_{\rm APS}(B_{n,1},\mathfrak s|_B)=0.
\]

This supplies the missing content behind “the weight window contains \(L^2\) and the APS weight.”

### Cone cap

One may use a rotationally symmetric \(\Gamma\)-invariant positive-scalar-curvature ball with a product collar and attach a half-cylinder. For every equivariant flat twist, the completed cap has no \(L^2\) harmonic spinor in either chirality by Lichnerowicz. Therefore its APS index is zero.

This vanishing holds for **all** local characters, not only the extendible ones. It does not imply that their Kawasaki terms are all equal: the boundary spectral contribution also depends on the character.

Excision now proves
\[
\operatorname{ind}D^{\rm orb}_{\operatorname{res}(\mathfrak s)}(V)
=\operatorname{ind}D_{\mathfrak s}(M).
\]
Expected dimensions agree because, additionally,
\[
b_1(V)=b_1(M),\qquad b^+(V)=b^+(M).
\]

### What the script actually does

`step93_wahl_index_transfer.py` uses 50-digit `mpmath`, rational reconstruction by `limit_denominator`, and a \(10^{-30}\) equality tolerance. Neither its arithmetic nor its equality tests are exact cyclotomic computations. The JSON is convincing finite-range numerical evidence, not an exact proof. Its discrepancy entries are directly assigned formulas, not independently solved intersection equations.

The mathematical identities can nevertheless be proved exactly.

Put \(p=n^2\), \(q=n-1\), and use the note’s inverse-denominator convention. Define
\[
H(a)=\frac1p\sum_{k=1}^{p-1}\frac{\zeta^{ka}}{1-\zeta^{-k}}.
\]
For \(0\le a<p\),
\[
H(a)=\frac{p-1-2a}{2p}.
\]
Since \(q^{-1}\equiv-(n+1)\pmod p\),
\[
\delta(m)-\delta(m-1)
=H\bigl([-(n+1)m]_p\bigr).
\]
Write \(m=an+b\), with \(0\le a<n\), \(0\le b<n\), and put \(c=n-a-1\). Summing this recurrence gives
\[
\delta(an)=\delta(0)
\]
and, for \(1\le b<n\),
\[
2n^2\bigl(\delta(an+b)-\delta(0)\bigr)=
\begin{cases}
b\bigl((n+1)b+2na-n(n-1)\bigr),&b\le c,\\[1mm]
(b-n)\bigl((n+1)b-2nc\bigr),&b>c.
\end{cases}
\]
Neither expression can vanish: a zero of its nontrivial linear factor would require \(n\mid b\), since \(\gcd(n,n+1)=1\). Thus, for every \(n\ge2\),
\[
\boxed{\delta(m)=\delta(0)\iff m\in n\mathbb Z/n^2\mathbb Z.}
\]
The direct-denominator convention replaces \(m\) by \(-m\), leaving this set unchanged.

Finally,
\[
\delta(0)
=\frac{p-1}{4p}
-\frac1{4p}\sum_{k=1}^{p-1}
 \cot\frac{\pi k}{p}\cot\frac{\pi qk}{p}.
\]
Using the Dedekind-sum identity proved in A02 gives
\[
\delta(0)=\frac{1-n^{-2}}{12},\qquad
\tau_{\rm CW}-\tau_{\rm top}=\frac23(1-n^{-2}).
\]
These are exact all-\(n\) replacements for the numerical claims.

Identifying \(n\mathbb Z/n^2\mathbb Z\) as the **extendible spin\(^c\) coset** also requires its canonical marking: line restrictions from \(B\) give the subgroup of order \(n\), while the Milnor-fibre canonical structure fixes its affine origin.

---

## 5. Proposition 93.Y: complex realization and the limits of transfer

### Scope of the realization

The supplied PPS proof structure supports an existential, marked construction for odd \(n\ge3\), and analogously for \(n=2\). It does not establish the claimed complex realization for the even \(n\ge4\) construction through
\[
B_{2,1}\#\overline{\mathbb{CP}}^2.
\]

Moreover, a diffeomorphism sending
\[
E_1+\cdots+E_4\longmapsto E_1-E_2-E_3-E_4
\]
in homology does not by itself identify embedded sphere neighborhoods: equal sphere classes do not establish equivalence of embedded pairs. The valid repair is:

> Choose the holomorphic sphere and the marked PPS complex-model embedding from the outset. Theorem 102.R admits such a realization for the indicated cases.

Individual exceptional sign changes are indeed realizable by orientation-preserving diffeomorphisms of the smooth connected-sum model. They provide compatible homological markings, not a uniqueness theorem for all embeddings.

### Grauert and PPS

For \(N=\mathcal O(-m)\), the displayed cohomology vanishings support formal linearization:
\[
H^1(\mathcal O(2+m\nu))=0,\qquad
H^1(\mathcal O(m(\nu-1)))=0,\quad \nu\ge1.
\]
Together with Grauert’s formal principle for exceptional curves, this identifies sufficiently small analytic neighborhoods.

The PPS smoothing/flip construction supplies the local smooth identification of the Milnor-fibre complement with the central-fibre complement. To glue it into \(X\), this identification must be compatible with the chosen outer boundary marking. It should not be presented as a biholomorphic identification of whole central and general fibers.

With that marking, replacing the ball by the cone gives
\[
Y=\widehat X/C_{n,1}.
\]
General type follows from bigness of \(K_{\widehat X}\) and
\[
\pi^*K_Y=K_{\widehat X}-\sum a_iC_i,
\qquad a_i<0.
\]
Projectivity needs the standard algebraic contraction result for the rational quotient configuration; Grauert’s analytic contraction alone is not the complete projectivity argument.

### Non-nefness

The discrepancy formula is correct:
\[
a_i=-\frac{n-i}{n}.
\]
It solves
\[
\sum_j a_j(C_j\cdot C_i)=K_{\widehat X}\cdot C_i,
\]
where the right side is \(n\) on the \(-(n+2)\) component and zero on the \(-2\) components.

If the PPS \((-1)\)-curve \(D\) meets only \(C_i\), once, then
\[
K_Y\cdot\pi_*D=-1-a_i=-\frac in<0.
\]
A generic exceptional curve disjoint from the chain instead has intersection \(-1\). Thus \(K_Y\) is not nef.

This excludes negative Kähler–Einstein metrics for **that complex structure**. To exclude them for every orientation-compatible complex structure on the underlying orbifold, use the transferred scalar estimate:
\[
\int s^2=32\pi^2K^2
=32\pi^2(A-k)<32\pi^2A
\]
for a negative KE metric when \(k>0\). A nonzero transferred monopole also excludes constant nonnegative scalar curvature. Hence any Einstein metric in this setting must be negative and non-Kähler in the specified orientation.

### The transfer principle is too broad

The following package transfers:
\[
a_V^2=a_M^2,\quad
T_+^{\rm orb}=2\chi_{\rm orb}+3\tau_{\rm CW}=A-k,
\]
extendible Dirac indices, metric-wise field supply, and the scalar/\(W^+\) LeBrun bounds.

But
\[
T_-^{\rm orb}=T_-(M)-4\sum_j(1-n_j^{-2})
\]
does **not** transfer unchanged. Nor do local characters, forced zeros, full SW invariants, moduli-space geometry, or genuinely point-sensitive field estimates.

Accordingly, replace the blanket principle by:

> The standard \(+\)-chirality LeBrun integral argument gives the same numerical threshold on \(V\) and \(M\); the \(W^-\)-side bound differs, although A02 shows it is slack for this family.

A proof on \(M\) using any conceivable field/index/curvature argument does not automatically exclude \(V\). The claim “Wahl is Q1 itself” is a useful analogy between smoothing and singular members, not an established equivalence of Einstein-existence problems.

---

## 6. Proposition 93.C and a stronger selection result

### Restriction and canonical marking

With \(\langle u,[S]\rangle=1\),
\[
x|_{V_{-4}}=(x\cdot S)u,
\]
and for \(S=E_1-E_2-E_3-E_4\),
\[
E_i|=-\varepsilon_i u,\qquad
K_M|=2u,\qquad \varepsilon=(1,-1,-1,-1).
\]
These are correct.

The assertion that \(K_M|_B\) has exact order \(n\) needs the **relative canonical marking of the PPS smoothing**, or the equivalent free-quotient ALE model: the holomorphic volume form on the hyperkähler cover transforms by a character of order \(n\). The Cartier index of the central singularity alone does not identify the marked restriction of a global smooth canonical class.

With that input, for odd \(n\),
\[
u_B=hK_B,\qquad h=2^{-1}\pmod n.
\]
Relative to the canonical spin\(^c\) structure with determinant \(-K_M\), the class
\[
-K_M+2\sum_{i\in F}E_i
\]
is twisted by the line \(\sum_{i\in F}E_i\). Therefore
\[
j_F=\sum_{i\in F\cap\{1,\dots,4\}}(-\varepsilon_i h)\pmod n,
\qquad m=nj_F.
\]
The factor \(h\) is correct; there is no additional determinant factor of two.

### Counts and jets

The two positive-spinor weights are
\[
nj,\qquad n(j-1).
\]
Thus a value is allowed exactly for \(j=0,1\). Adding any cotangent weight
\[
\pm1,\quad\pm(n-1)
\]
cannot produce weight zero for \(n\ge3\). Hence the covariant first jet vanishes for every extendible twist, and a forced-zero spinor has order at least two.

The integer script correctly counts:
\[
6/16\quad(n=3),\qquad 8/16\quad(\text{every odd }n\ge5).
\]
Indeed \(j_F=h(r-f_1)\), where \(r=f_2+f_3+f_4\). For \(n\ge5\), allowed subsets have even cardinality; the eight odd-cardinality subsets are forced. For \(n=3\), the six forced subsets are \(\{1\}\), \(\{2,3,4\}\), and the four choices with \(r-f_1=1\).

For \(n=2\), the canonically marked extendible set is the allowed set \(\{0,2\}\), so this mechanism forces no value zero.

The assertion about simultaneous fields needs all those structures to be supplied—not merely the one selected in hypothesis (S).

### New consequence: the forced subset still supplies the \(A\)-bound

The forced subset is closed under complementation, since
\[
j_{F^c}=1-j_F.
\]
Consequently its local exceptional sign vector has mean zero. Averaging independently over all remaining exceptional signs gives
\[
\operatorname{Avg}_{\rm forced}(a_F^+)^2
=
|K_X^+|^2
+\operatorname{Avg}_{\rm forced}
  \left|\sum_{i=1}^4\sigma_iE_i^+\right|^2
+\sum_{i>4}|E_i^+|^2
\ge A.
\]
No independence among the first four signs is needed: their squared sum is nonnegative.

Thus, under simultaneous supply, WFL can be run **using only forced-zero structures**, retaining
\[
\int U^2\ge32\pi^2A.
\]
The limiting field has
\[
\Phi(p)=0,\qquad \nabla_A\Phi(p)=0.
\]
This resolves the potential mismatch between “a class with a zero” and “a class furnishing the optimal lower bound.”

It also proves the strict scalar inequality for each fixed metric:
\[
\int(s^-)^2>32\pi^2A.
\]
Equality throughout the integrated Weitzenböck estimate would force \(\nabla_A\Phi=0\); a parallel spinor vanishing at \(p\) is identically zero, contradicting its mass bound. This is strictness, not a uniform gap.

---

## 7. Lemma 93.W

The representation calculation is correct. For \(n\ge3\),
\[
\Lambda^+_\mathbb C
\quad\text{has weights}\quad 0,n,-n,
\]
and
\[
\operatorname{Sym}^2_0\Lambda^+
\quad\text{has weights}\quad 0,\pm n,\pm2n.
\]
Only the first is trivial, so
\[
W^+(p)=\mu\,\operatorname{diag}(2,-1,-1).
\]
For \(n=2\), the \(\pm2n\) weights become trivial, giving three real invariant dimensions.

For an arbitrary invariant metric, define \(\omega_0\) using the invariant Hermitian metric at the point. For \(n\ge3\), invariance forces compatibility with the standard complex representation. The displayed basis is then metric-adapted.

Einstein is not needed for the algebraic conclusion, and it does not force \(\mu=s/12\).

---

## 8. The missing implication: what is genuinely plausible

For a negative Einstein metric, \(s=-\lambda\),
\[
0\le U\le\lambda,\qquad
4\int|\nabla_A\Phi|^2=\int U(\lambda-U).
\]
The selected forced-zero field makes
\[
\int(\lambda^2-U^2)>0,
\]
but topology currently gives no positive uniform lower bound.

### A quantitative estimate requires a geometric scale

Suppose an orbifold uniformizer ball of radius \(r_0\) has controlled rescaled metric and connection coefficients, sufficient for uniform elliptic estimates, with \(\lambda r_0^2\) bounded. The double zero gives schematically
\[
|\Phi(x)|\le C\sqrt\lambda\,(d(x,p)/r_0)^2.
\]
On a smaller fixed fraction of that ball, \(U\le\lambda/2\). Volume comparison then gives
\[
\boxed{\int_{B_{cr_0}(p)}(\lambda^2-U^2)
\ge c'\frac{\lambda^2r_0^4}{n^2}.}
\]
Thus the unresolved object is a lower bound for the dimensionless regularity scale \(\lambda r_0^2\), or a substitute controlling the defect when this scale collapses.

Einstein controls Ricci curvature, not Weyl curvature or the coupled connection regularity radius. A degenerating sequence may develop Ricci-flat bubbles at \(p\). A potentially effective route is therefore a **bubble-tree analysis retaining the marked spin\(^c\) character**: determine whether a forced character can migrate into smaller bubbles at vanishing global defect. The present energy-transfer theorem does not answer that question for arbitrary Einstein sequences.

### The proposed Green-function shortcut is not justified

The conformal proposal does not currently supply a missing estimate:

- the claimed monopole conformal law is false;
- the negative-scalar conformal Laplacian does not automatically have a positive Green function;
- shifting it changes its conformal interpretation;
- no established positive mass/end term follows from a double zero.

Under a Green blow-up \(\widehat g=G^2g\), \(G\sim r^{-2}\), the **Dirac** harmonic spinor transforms as \(G^{-3/2}\Phi\). A double zero then produces stronger decay, not automatically a nonzero boundary flux. A viable end argument would need an independently derived coupled identity and a signed end invariant.

### The Kähler-wall test is plausible, but is not yet a construction

A concrete test is to identify a contraction of the exceptional divisor configuration carrying the forced sections and consider orbifold Kähler classes with those divisor areas tending to zero. For a real \((1,1)\)-class \(D\),
\[
\|D^+\|^2=\frac{(D\cdot[\omega])^2}{[\omega]^2}.
\]
Thus small area can make its cohomological contribution arbitrarily small.

However, the note’s assertions that forced zeros are exactly “the \((-1)\)-curves through \(p\)” and that their field cost is proportional to area are unproved. The zero divisor depends on the twisting line, and its image on \(Y\) need not be a smooth \((-1)\)-curve.

A genuine small-cost example requires:

- the effective orbifold line/divisor representing the selected forced twist;
- a realizable Kähler degeneration shrinking its support;
- solutions of the **unperturbed** orbifold Kähler SW/vortex equations;
- estimates for \(\|d\alpha\|_2^2\), gradient energy, or the excess in the curvature inequality.

On non-Einstein Kähler test metrics, \(\lambda^2-U^2\) is not the appropriate defect unless a constant scalar normalization is independently available.

Contracting additional curves and obtaining a KE canonical model would not, by itself, solve the original Wahl channel: it changes topology and introduces additional local replacements whose Einstein-defect cost must be accounted for.

---

## Standard versus session-specific content

The Hodge/removability tools, equivariant spin\(^c\) classification, ALE–APS theory, Kawasaki and Dedekind formulas, Grauert/PPS mechanisms, and LeBrun estimates are standard ingredients. The supplied material supports a session-specific synthesis: fixed supplied fields across this recovery family, marked orbifold extension, full abelian energy transfer, and explicit supplied-character bookkeeping. No literature novelty claim follows from the bounded input.

The strongest additional mathematical consequence is the complement-symmetric forced-subfamily selection. It shows that **class selection is not the missing link**. The remaining link is quantitative control—or a genuine small-cost degeneration—of the geometric scale on which the selected forced double zero affects an Einstein curvature integral.