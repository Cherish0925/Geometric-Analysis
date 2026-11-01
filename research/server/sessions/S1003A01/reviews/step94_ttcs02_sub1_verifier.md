# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step94_wahl_monogenic_modes.py",
    "Sessions/S1003A01/workspace/data/step94/wahl_monogenic_modes.json",
    "Sessions/S1003A01/workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md",
    "Sessions/S1003A01/workspace/notes/step94_same_field_budget_and_marked_wahl_route_decision.md"
  ]
}
```

## Task

Verify the exact script and its interpretation. At a Wahl quotient Gamma=1/n^2(1,n-1), Step 93 gives positive-spinor weights (m,m-n), m=nj for extendible twist j. The script enumerates homogeneous complex polynomials in z1,z2,bar z1,bar z2, imposes coefficient weight equal to fibre weight, and computes the kernel of D0=[[d_barz1,d_barz2],[-d_z2,d_z1]] over Q. It reports that for every tested odd n=3,5,7,9,11 and every forced j=2,...,n-1, the first nonzero equivariant homogeneous monogenic spinor has degree ell=n. Check the group-action sign, Clifford/Dirac convention, whether D preserves the selected equivariance sectors, the exact rank calculation concept, and whether ell=n is plausible/provable for all odd n and forced j. If the script convention is wrong, give the corrected result. Then explain what vanishing order ell=n does and does not imply for the same-field Einstein deficit D2 and for shrinking-link residues. Ground the answer in the actual script/data and Step-93 character statement.

## Output

## Scientific verification memo

### 1. Main result

The matrices and ranks in `step94_wahl_monogenic_modes.py` are computed exactly: all entries are integers, and SymPy’s rank over \(\mathbb Q\) equals the rank over \(\mathbb C\). The JSON pattern
\[
\ell_{\mathrm{first}}=n
\]
is also provable for the operator actually encoded.

However, the encoded Dirac matrix is not equivariant for the stated action
\[
\Gamma=\frac1{n^2}(1,n-1)
\]
together with the Step-93 positive-spinor weights
\[
(m,m-n).
\]
With a compatible Clifford convention, the first possible homogeneous monogenic degree is instead
\[
\boxed{\ell_{\min}(n,j)=2\min\{j-1,n-j\}},
\qquad 2\le j\le n-1.
\]
For odd \(n\), this ranges from \(2\) to \(n-1\), rather than being uniformly \(n\).

Thus Step 93’s universal conclusion “order at least two” is sharp across all forced twists. Some middle twists impose higher order, but not every forced twist does.

---

## 2. Group action and coefficient sectors

Write \(N=n^2\), \(\zeta=e^{2\pi i/N}\), and
\[
\gamma(z_1,z_2)=(\zeta z_1,\zeta^{\,n-1}z_2).
\]
For
\[
P=z_1^az_2^b\bar z_1^c\bar z_2^d,
\]
the script assigns
\[
\operatorname{wt}(P)=a+(n-1)b-c-(n-1)d,
\]
so that
\[
P(\gamma z)=\zeta^{\operatorname{wt}(P)}P(z).
\]
If a lifted spinor is represented as an equivariant map satisfying
\[
\Phi(\gamma z)=
\begin{pmatrix}
\zeta^m&0\\0&\zeta^{m-n}
\end{pmatrix}\Phi(z),
\]
then selecting coefficient weights \(m\) and \(m-n\), as the script does, is correct.

If one uses the inverse convention for equivariant coefficient functions, all coefficient weights reverse and the conjugate Dirac matrix must be used. The final formula for \(\ell_{\min}\) is unchanged.

The script comment saying that coefficients transform “contragrediently” is inconsistent with its actual test `wt(e)-fw[comp] == 0`: the implemented convention is direct equivariance.

---

## 3. The encoded Dirac matrix does not preserve these sectors

Differentiation changes coordinate weights by
\[
\begin{aligned}
\partial_{z_1}&:-1,&\partial_{\bar z_1}&:+1,\\
\partial_{z_2}&:-(n-1),&
\partial_{\bar z_2}&:+(n-1).
\end{aligned}
\]

The script uses
\[
D_{\rm code}=
\begin{pmatrix}
\partial_{\bar z_1}&\partial_{\bar z_2}\\
-\partial_{z_2}&\partial_{z_1}
\end{pmatrix}.
\]
For input weights \((m,m-n)\), the two terms in its first row have weights
\[
m+1,\qquad (m-n)+(n-1)=m-1,
\]
and the terms in its second row have weights
\[
m-(n-1)=m-n+1,\qquad (m-n)-1=m-n-1.
\]
The two summands in either row therefore lie in distinct \(\Gamma\)-characters. There is no two-dimensional output representation for which this matrix intertwines the specified action.

For the Step-93 weights, a compatible chiral Dirac matrix is, up to signs and nonzero constants,
\[
\boxed{
D_0^+=
\begin{pmatrix}
\partial_{z_1}&\partial_{\bar z_2}\\
-\partial_{z_2}&\partial_{\bar z_1}
\end{pmatrix}.}
\]
Indeed its output rows have well-defined weights
\[
m-1,\qquad m-n+1:
\]
\[
\begin{aligned}
m-1&=(m-n)+(n-1),\\
m-(n-1)&=(m-n)+1.
\end{aligned}
\]
These are precisely the compatible \(S^-\) weights
\[
(m-1,m-(n-1)).
\]
The symbol also has the usual Dirac property: its adjoint composition is a scalar multiple of the flat Laplacian.

With inverse coefficient equivariance, the conjugate compatible matrix is
\[
\begin{pmatrix}
\partial_{\bar z_1}&\partial_{z_2}\\
-\partial_{\bar z_2}&\partial_{z_1}
\end{pmatrix}.
\]

---

## 4. Why the script nevertheless gives \(\ell=n\) exactly

Because the two terms in each coded row carry distinct characters, they cannot cancel. Hence
\[
D_{\rm code}(f,g)=0
\]
forces
\[
\partial_{\bar z_1}f=\partial_{z_2}f=0,
\qquad
\partial_{\bar z_2}g=\partial_{z_1}g=0.
\]
Thus
\[
f=f(z_1,\bar z_2),\qquad g=g(z_2,\bar z_1).
\]

For a homogeneous monomial \(z_1^a\bar z_2^d\) of degree \(\ell=a+d\),
\[
\operatorname{wt}=\ell-nd.
\]
Equivariance with the first fibre weight \(nj\) implies, after reduction modulo \(n\),
\[
\ell\equiv0\pmod n.
\]
Likewise, for \(z_2^b\bar z_1^c\), with \(b+c=\ell\),
\[
\operatorname{wt}=nb-\ell,
\]
and matching \(n(j-1)\) again gives \(\ell\equiv0\pmod n\).

There are no constant inputs for \(2\le j\le n-1\), so the first possible coded degree is \(n\). At that degree the two kernel monomials are
\[
\left(z_1^{j-1}\bar z_2^{\,n+1-j},0\right),
\qquad
\left(0,z_2^j\bar z_1^{\,n-j}\right).
\]
This proves, for the encoded algebraic object,
\[
\dim_{\mathbb C}\ker D_{\rm code}|_{\ell=n}=2,
\qquad
\ker D_{\rm code}|_{\ell<n}=0,
\]
for every \(n\ge3\) and \(2\le j\le n-1\). Oddness is not used.

Thus the JSON is internally consistent, and the rational-rank computation is sound. The issue lies solely in pairing that matrix with the Step-93 fibre representation.

A concrete trace appears in the JSON for \(n=5,j=2,\ell=2\): it reports one input, rank one, and zero kernel. That unique input is
\[
(0,z_1z_2).
\]
It is annihilated by the compatible operator because the second column uses \(\partial_{\bar z_2},\partial_{\bar z_1}\), but the script applies \(\partial_{\bar z_2},\partial_{z_1}\), producing a nonzero result.

---

## 5. Correct first degree for the Step-93 spinor representation

Let
\[
P=a-c,\qquad Q=b-d.
\]
Then
\[
\operatorname{wt}=P+(n-1)Q=(P-Q)+nQ.
\]
Suppose \(\ell<n\) and the monomial weight is a multiple of \(n\). Reduction modulo \(n\) gives
\[
P-Q\equiv0\pmod n.
\]
Since
\[
|P-Q|\le a+b+c+d=\ell<n,
\]
one must have
\[
P=Q=:r.
\]
Consequently
\[
\operatorname{wt}=nr,
\qquad
\ell\ge2|r|.
\]

For the first component, \(\operatorname{wt}\equiv nj\pmod{n^2}\), so
\[
r\equiv j\pmod n,
\]
and any first-component monomial of degree below \(n\) has
\[
\ell\ge2\min\{j,n-j\}.
\]

For the second component, \(\operatorname{wt}\equiv n(j-1)\pmod{n^2}\), giving
\[
\ell\ge2\min\{j-1,n-j+1\}.
\]

Taking the smaller of these two bounds yields
\[
\ell\ge 2\min\{j-1,n-j\}.
\]
This degree is attained by an actual monogenic polynomial:

- If \(j-1<n-j\),
  \[
  \Phi_{\min}=
  \left(0,(z_1z_2)^{j-1}\right),
  \qquad
  \ell=2(j-1).
  \]
  It has weight \(n(j-1)=m-n\), and both antiholomorphic derivatives in the second column vanish.

- If \(n-j<j-1\),
  \[
  \Phi_{\min}=
  \left((\bar z_1\bar z_2)^{n-j},0\right),
  \qquad
  \ell=2(n-j).
  \]
  Its weight is
  \[
  -n(n-j)\equiv nj\pmod{n^2},
  \]
  and both holomorphic derivatives in the first column vanish.

- For odd \(n\) and \(j=(n+1)/2\), both occur at degree \(n-1\).

Therefore
\[
\boxed{\ell_{\min}=2\min\{j-1,n-j\}.}
\]

For example,
\[
\begin{array}{c|c}
n=5 & (\ell_{\min}(j=2),\ell_{\min}(3),\ell_{\min}(4))=(2,4,2),\\[2mm]
n=7 & (2,4,6,4,2).
\end{array}
\]
At the first degree, the kernel is one-dimensional except at the middle odd-\(n\) twist, where it is two-dimensional.

---

## 6. Meaning for an actual coupled Seiberg–Witten field

In orbifold normal coordinates and a smooth local gauge, the leading homogeneous Taylor coefficient \(P_\ell\) of a nonzero spinor satisfies the flat equation
\[
D_0^+P_\ell=0
\]
and carries the same isotropy character. Hence a forced twist \(j\) gives
\[
\operatorname{ord}_{p_0}\Phi\ge
2\min\{j-1,n-j\}.
\]
It does not force equality: the first permitted coefficient can itself vanish. Unique continuation ensures that a globally nonzero solution has some finite leading order, but it may exceed the representation-theoretic minimum.

The consequences near \(p_0\) are
\[
\Phi=O(r^\ell),\qquad
U=|\Phi|^2=O(r^{2\ell}),\qquad
F_A^+=q(\Phi)=O(r^{2\ell}).
\]
Thus middle characters can impose high-order local flatness. Across all forced characters, however, the common statement remains only
\[
\operatorname{ord}_{p_0}\Phi\ge2,
\]
since \(j=2\) and \(j=n-1\) have \(\ell_{\min}=2\). The Step-93 forced-subfamily averaging supplies some forced class with \(p=(a^+)^2\ge A_0\), but the stated averaging identity does not select a middle character. It therefore does not transfer the higher values of \(\ell_{\min}\) into a uniform estimate.

---

## 7. Consequences for \(D_2\)

The zero still has a genuine same-field consequence. In the endpoint estimates (94.9)–(94.10), \(D_2=0\) forces the actual polynomial form
\[
\omega=q(\Phi)
\]
toward a nonzero constant-length harmonic form and aligns \(W^+\) with the Kähler polynomial model. Since \(\Phi(p_0)=0\) gives \(\omega(p_0)=0\), exact equality is impossible for the supplied irreducible field. Thus, for each fixed metric,
\[
\boxed{D_2>0.}
\]

Higher order makes
\[
\omega=O(r^{2\ell}),\qquad
\nabla\omega=O(r^{2\ell-1}),
\]
but the discrete order alone does not furnish
\[
D_2\ge c(n,j)>0
\quad\text{or}\quad
D_2/V\ge c(n,j)>0.
\]
A model profile that vanishes to order \(\ell\) inside a ball of radius \(r\) and reaches fixed size outside has four-dimensional scaling
\[
\int_{B_r}|\nabla\Phi|^2=O_\ell(r^2),
\qquad
\int_{B_r}(1-|\Phi|^2)^2=O_\ell(r^4).
\]
Both tend to zero as \(r\to0\) for every fixed finite \(\ell\). The factor from the quotient chart contributes another \(1/n^2\). Consequently, even order \(n-1\) does not by itself produce a scale-independent contribution to \(D_2\). Such a contribution would require quantitative control of the regularity radius, the leading coefficient, or a retained curvature pairing in the coupled Taylor recursion.

---

## 8. Shrinking-link residues

If \(\Phi=O(r^\ell)\), a typical unscaled link integral containing one derivative behaves no slower than
\[
\int_{S^3_r/\Gamma}|\Phi|\,|\nabla\Phi|
=O\!\left(\frac{r^{2\ell+2}}{n^2}\right),
\]
while bilinears without derivatives decay even faster. Hence ordinary Dirac, stress, Pohozaev, and related shrinking-link fluxes still tend to zero. Larger \(\ell\) increases the decay exponent; it does not produce a nonzero residue.

The discrete character computations are also unchanged:

\[
m(m-n)=n^2j(j-1)\equiv0\pmod{n^2},
\]
so the normalized-spinor degree congruence quoted in Step 94 forces no fractional local Euler term. Likewise, Step 93’s exact identity
\[
\delta(nj)=\delta(0)
\]
for every extendible twist remains independent of Taylor order. Renormalizing \(r^{-\ell}\Phi\) may recover the leading polynomial \(P_\ell\), but that is a jet datum with unconstrained amplitude, not an unscaled conserved link quantity.

### Final assessment

- The script’s integer matrices and ranks are exact.
- Its \(\ell=n\) pattern is provable for the mismatched operator-sector pair it encodes.
- For the Step-93 weights \((m,m-n)\), the compatible Dirac operator gives
  \[
  \boxed{\ell_{\min}=2\min\{j-1,n-j\}.}
  \]
- The universal forced-zero information remains order at least two.
- Any forced zero gives fixed-metric strictness \(D_2>0\), but neither its order nor the extendible character alone supplies a scale-independent \(D_2\) payment or a nonzero shrinking-link residue.