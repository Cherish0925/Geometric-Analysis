# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 94,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step94_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step94_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the exact script and its interpretation. At a Wahl quotient Gamma=1/n^2(1,n-1), Step 93 gives positive-spinor weights (m,m-n), m=nj for extendible twist j. The script enumerates homogeneous complex polynomials in z1,z2,bar z1,bar z2, imposes coefficient weight equal to fibre weight, and computes the kernel of D0=[[d_barz1,d_barz2],[-d_z2,d_z1]] over Q. It reports that for every tested odd n=3,5,7,9,11 and every forced j=2,...,n-1, the first nonzero equivariant homogeneous monogenic spinor has degree ell=n. Check the group-action sign, Clifford/Dirac convention, whether D preserves the selected equivariance sectors, the exact rank calculation concept, and whether ell=n is plausible/provable for all odd n and forced j. If the script convention is wrong, give the corrected result. Then explain what vanishing order ell=n does and does not imply for the same-field Einstein deficit D2 and for shrinking-link residues. Ground the answer in the actual script/data and Step-93 character statement.

## Integrated Scientific Memo

## Verification result

The rational linear algebra in `step94_wahl_monogenic_modes.py` is sound, but its Dirac matrix is **not equivariant for the Step-93 positive-spinor weights \((m,m-n)\)**. The reported first degree \(\ell=n\) is an exact property of that mismatched operator–sector pair, not of the geometric Dirac problem.

Keeping the script’s coefficient-weight condition and correcting the operator gives
\[
\boxed{\ell_{\min}(n,j)=2\min\{j-1,n-j\}},
\qquad n\ge3\text{ odd},\quad 2\le j\le n-1.
\]
This is the first *permitted* homogeneous monogenic degree; an actual solution can vanish to higher order.

### 1. Equivariance and Clifford convention

Put \(N=n^2\), and let
\[
\gamma(z_1,z_2)=(\zeta z_1,\zeta^{n-1}z_2).
\]
The script correctly computes
\[
\operatorname{wt}(z_1^az_2^b\bar z_1^c\bar z_2^d)
=a+(n-1)b-c-(n-1)d.
\]
For a section represented by
\[
\Phi(\gamma z)=
\operatorname{diag}(\zeta^m,\zeta^{m-n})\Phi(z),
\]
its component functions have weights \(m,m-n\). Thus the implemented test
```python
(wt(e, n) - fw[comp]) % N == 0
```
is correct under this section convention. The comment about “contragredient” coefficients is misleading: on invariant Taylor tensors, the cotangent representation is contragredient to the tangent representation, yielding the same coefficient-weight condition. Merely replacing the test by weight plus fibre weight, while leaving everything else unchanged, is not a consistent repair.

The derivative weight shifts are
\[
\partial_{z_1}:-1,\quad
\partial_{z_2}:-(n-1),\quad
\partial_{\bar z_1}:+1,\quad
\partial_{\bar z_2}:+(n-1).
\]
Consequently the coded operator
\[
D_{\mathrm{code}}=
\begin{pmatrix}
\partial_{\bar z_1}&\partial_{\bar z_2}\\
-\partial_{z_2}&\partial_{z_1}
\end{pmatrix}
\]
has the following output weights:
\[
\begin{array}{c|cc}
&\text{from component }0&\text{from component }1\\ \hline
\text{row }0&m+1&m-1\\
\text{row }1&m-n+1&m-n-1 .
\end{array}
\]
The summands in each row differ in character by \(2\not\equiv0\pmod{n^2}\). There is therefore no negative-spinor fibre representation making this matrix intertwine the stated positive-spinor action.

The matrix itself has a legitimate flat Dirac symbol: its adjoint composition is a scalar Laplacian. The error is its pairing with the stated isotropy representation, not failure of ellipticity. Indeed, it would intertwine input weights \((m,m-n+2)\), but those are not Step 93’s weights and do not have the stated constant-spinor twists \(m=0,n\).

A compatible operator for the implemented coefficient convention is
\[
\boxed{
D^+=
\begin{pmatrix}
\partial_{z_1}&\partial_{\bar z_2}\\
-\partial_{z_2}&\partial_{\bar z_1}
\end{pmatrix}.}
\]
Its output weights are
\[
(m-1,\;m-(n-1)),
\]
since the two summands in each row now agree. Moreover
\[
(D^+)^*D^+
=-\bigl(\partial_{z_1}\partial_{\bar z_1}
+\partial_{z_2}\partial_{\bar z_2}\bigr)I
=-\tfrac14\Delta_{\mathrm{Eucl}}I.
\]
Changing component signs or multiplying the entire matrix by the usual Dirac normalization does not change the degree conclusions.

An entirely inverted representation convention uses negated coefficient weights and the conjugate operator. It gives the same degrees. Sign inversion must be applied coherently to the representation and operator.

### 2. What the existing script and JSON actually establish

Every matrix entry is an integer derivative coefficient. SymPy’s exact rational rank equals its complex rank. Treating \(z_i,\bar z_i\) as independent polynomial variables is appropriate: they form a complex linear coordinate system on the complexified real polynomial algebra.

The output list contains all monomials actually reached by the selected inputs. Omitting unused output rows does not alter rank or kernel, although `output_dim_complex` is not generally the dimension of a complete geometric target sector.

There is an elementary all-\(n\) explanation of the JSON’s \(\ell=n\) pattern. Because the two summands in each coded row have distinct characters, they cannot cancel. Therefore
\[
D_{\mathrm{code}}(f,g)=0
\quad\Longleftrightarrow\quad
\partial_{\bar z_1}f=\partial_{z_2}f=0,\qquad
\partial_{\bar z_2}g=\partial_{z_1}g=0.
\]
Thus
\[
f=f(z_1,\bar z_2),\qquad g=g(z_2,\bar z_1).
\]
For degree \(\ell\), their monomial weights are respectively
\[
\ell-nd,\qquad nb-\ell.
\]
Matching either extendible fibre weight forces \(\ell\equiv0\pmod n\). Forced twists have no constants, and degree \(n\) has exactly the two coded kernel modes
\[
\left(z_1^{j-1}\bar z_2^{n+1-j},0\right),\qquad
\left(0,z_2^j\bar z_1^{n-j}\right).
\]
Hence, for the coded problem,
\[
\ker D_{\mathrm{code}}|_{\ell<n}=0,\qquad
\dim_{\mathbb C}\ker D_{\mathrm{code}}|_{\ell=n}=2.
\]
This explains the data for every tested \(n\) and proves its pattern beyond the tested range. It does **not** validate its geometric interpretation.

A direct source-data witness is \(n=5,j=2,\ell=2\): the JSON records one input, rank one, and zero kernel. That input is \((0,z_1z_2)\). The compatible \(D^+\) annihilates it, whereas the coded operator produces \((0,z_2)\).

The minimal code repair, retaining the weight test, is:
```python
if comp == 0:
    derivative_terms = ((0, 0, 1), (1, 1, -1))
else:
    derivative_terms = ((0, 3, 1), (1, 2, 1))
```
with the documentation and JSON convention updated accordingly.

### 3. Proof of the corrected first degree

Write
\[
P=a-c,\qquad Q=b-d.
\]
Then
\[
\operatorname{wt}=P-Q+nQ.
\]
If a monomial has degree \(\ell<n\) and weight divisible by \(n\), then
\[
P-Q\equiv0\pmod n,\qquad |P-Q|\le\ell<n,
\]
so \(P=Q=r\). Its weight is \(nr\), and its degree satisfies
\[
\ell\ge2|r|.
\]
For the two components, respectively,
\[
r\equiv j\pmod n,\qquad r\equiv j-1\pmod n.
\]
Thus no input—and therefore no monogenic spinor—can occur below
\[
L=2\min\{j-1,n-j\}.
\]
For odd \(n\), \(L\le n-1\), so the preceding \(\ell<n\) argument covers every degree below \(L\).

The bound is attained:
\[
\begin{cases}
\displaystyle
\left(0,(z_1z_2)^{j-1}\right),
&j-1\le n-j,\\[2mm]
\displaystyle
\left((\bar z_1\bar z_2)^{n-j},0\right),
&n-j\le j-1.
\end{cases}
\]
Each has the required character and is killed by \(D^+\). At the first degree, the kernel is one-dimensional except at \(j=(n+1)/2\), where both modes occur and it is two-dimensional.

The corrected table is therefore
\[
\begin{array}{c|c}
n&\ell_{\min}(j),\quad j=2,\ldots,n-1\\ \hline
3&2\\
5&2,4,2\\
7&2,4,6,4,2\\
9&2,4,6,8,6,4,2\\
11&2,4,6,8,10,8,6,4,2 .
\end{array}
\]

For further exact dimension calculations, the compatible homogeneous Dirac map is surjective onto the full degree-\(\ell-1\) polynomial target. This follows from polynomial surjectivity of the scalar Laplacian and \(D^+(D^+)^*=-\Delta/4\). Averaging a preimage over \(\Gamma\) proves surjectivity on equivariant sectors. Thus corrected kernel dimensions can also be obtained by subtracting complete target-sector counts from domain-sector counts.

### 4. Additional consequence for the *actually supplied* Step-93 classes

There is a useful distinction between all forced extendible twists and the forced twists occurring in Proposition 93.C.

For odd \(n\ge5\), Step 93 §8.8 identifies the forced local sign classes with the odd-cardinality subsets of \(\{1,2,3,4\}\). Using its formula
\[
j_F=h(-1_{1\in F}+1_{2\in F}+1_{3\in F}+1_{4\in F}),
\qquad h=(n+1)/2,
\]
their twists and multiplicities are
\[
\begin{array}{c|ccc}
j&(n-1)/2&(n+1)/2&(n+3)/2\\ \hline
\text{multiplicity}&1&6&1\\
\ell_{\min}&n-3&n-1&n-3 .
\end{array}
\]
The \(+K\)-side involution \(j\mapsto1-j\) preserves this distribution.

Therefore the corrected calculation still yields a growing-order statement for the marked supplied family:
\[
\boxed{\operatorname{ord}_{p_0}\Phi\ge n-3
\quad\text{for every supplied forced class when }n\ge5.}
\]
For \(n=3\), the forced twist has minimum degree \(2\). Across *all* forced extendible twists the common lower bound remains only \(2\).

This refinement is compatible with Step 93’s forced-subfamily averaging: the selected class with \((a^+)^2\ge A_0\) belongs to this high-order subfamily. It does not require selecting the middle twist, whose stronger minimum is \(n-1\).

### 5. Meaning for an actual field and for \(D_2\)

For a smooth orbifold monopole, choose equivariant normal coordinates and a smooth local trivialization. Its first nonzero Taylor term satisfies the flat compatible Dirac equation and the Step-93 character condition. Thus
\[
\operatorname{ord}_{p_0}\Phi\ge\ell_{\min}(n,j).
\]
The first allowed coefficient need not be nonzero; representation theory determines a minimum, not the actual order or amplitude. Unique continuation for the smooth Dirac equation ensures finite vanishing order for a nontrivial solution.

If its actual order is \(\ell\), then
\[
\Phi=O(r^\ell),\quad
\nabla_A\Phi=O(r^{\ell-1}),\quad
U=O(r^{2\ell}),\quad
q(\Phi)=F_A^+=O(r^{2\ell}).
\]
Curvature and connection terms affect higher Taylor equations, not this leading flat equation.

For the same-field endpoint
\[
D_2=\tfrac32S+18W-72\pi^2p,
\]
the endpoint controls and equality characterization recorded in Step 94 imply that exact equality requires the retained field to realize the nonzero constant-length Kähler model. A forced zero is incompatible with that equality. Accordingly, **under that recorded endpoint characterization**, the forced same-field endpoint has \(D_2>0\) for each fixed metric. The scalar identity
\[
S-\int U^2=8\int|\nabla_A\Phi|^2+\int(\lambda-U)^2
\]
separately gives fixed-metric strict scalar slack; it must not be identified with the mixed deficit \(D_2\).

Neither the erroneous order \(n\) nor the corrected growing orders establish a uniform positive lower bound for \(D_2/V\). For a fixed leading coefficient,
\[
\int_{B_r/\Gamma}|\nabla_A\Phi|^2
=O(r^{2\ell+2}/n^2),\qquad
\int_{B_r/\Gamma}|\Phi|^4
=O(r^{4\ell+4}/n^2).
\]
More importantly, a profile reaching fixed size outside a shrinking radius \(R\), while vanishing to any prescribed finite order inside it, has schematic costs
\[
\int|\nabla\Phi|^2=O_\ell(R^2/n^2),\qquad
\int(\lambda-U)^2=O_\ell(R^4/n^2).
\]
These are scaling demonstrations, **not constructions of Einstein monopoles**. They show why order alone is not coercive.

The unresolved scientific object remains a same-field estimate for \(D_2/V\), or its retained endpoint terms, with control of the dimensionless geometric scale \(\lambda r_0^2\) or an additional curvature-sensitive mechanism. Even such a positive payment must be combined with the projection term and the full Einstein scalar–Weyl budget; scalar strictness alone does not exclude Einstein metrics.

### 6. Shrinking-link residues

For example,
\[
\int_{S_r^3/\Gamma}|\Phi|\,|\nabla_A\Phi|
=O(r^{2\ell+2}/n^2)\longrightarrow0.
\]
Ordinary unscaled spinor, Weitzenböck and stress fluxes therefore vanish; higher order only accelerates their decay. Smooth lifted curvature likewise supplies no new singular differential flux.

This does **not** mean that quotient-link holonomy disappears: the torsion character survives and may be carried by a flat connection. Nor should every absolute Chern–Simons value be declared zero merely from smoothness on the uniformizer. The relevant source-grounded statements are instead:

- extendibility gives \(\delta(nj)=\delta(0)\), so no new relative local Dirac defect arises;
- the extendible subgroup is isotropic for the lens-space linking form;
- if the spinor zero is isolated, the recorded degree congruence has
  \[
  m(m-n)=n^2j(j-1)\equiv0\pmod{n^2},
  \]
  hence forces no nonzero fractional Euler residue.

The displayed first modes vanish along coordinate divisors, so isolatedness is not supplied by the degree calculation itself. Any normalized-spinor degree requires its own nonvanishing-link hypothesis.

Rescaling \(r^{-\ell}\Phi\) extracts a leading jet, not an unscaled conserved charge. Its amplitude is not fixed by the character. Thus the corrected calculation strengthens the local Taylor information—particularly for the actually supplied marked classes—but supplies neither a uniform \(D_2\) payment nor a new shrinking-link residue.