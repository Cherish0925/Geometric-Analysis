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

## Scientific memo on `step94_wahl_monogenic_modes.py`

### 1. What the script computes exactly

The script forms a finite rational linear algebra problem. For a fixed odd \(n\), \(N=n^2\), extendible twist \(m=nj\), and homogeneous degree \(\ell\), it enumerates monomials

\[
z_1^a z_2^b \bar z_1^c \bar z_2^d,\qquad a+b+c+d=\ell,
\]

with coordinate weight

\[
\operatorname{wt}(a,b,c,d)=a+(n-1)b-c-(n-1)d.
\]

It then keeps component \(0\) monomials with

\[
\operatorname{wt}\equiv m \pmod{N}
\]

and component \(1\) monomials with

\[
\operatorname{wt}\equiv m-n \pmod{N},
\]

where the Step-93 positive-spinor fibre weights are recorded as

\[
(m,\;m-n).
\]

It builds the matrix of

\[
D_0=
\begin{pmatrix}
\partial_{\bar z_1} & \partial_{\bar z_2}\\
-\partial_{z_2} & \partial_{z_1}
\end{pmatrix}
\]

on those selected inputs, with integer derivative coefficients, and computes the rational rank. Since all matrix entries are integers and Sympy’s `rank()` is exact over \(\mathbb Q\), the JSON numbers are exact for the linear map that the script actually defines. The exactness of the rank computation is not the main issue.

The issue is that this linear map is not the \(\Gamma\)-equivariant flat Dirac operator for the Step-93 weights \((m,m-n)\) together with the selected equivariance condition.

---

### 2. The equivariance check for the script’s operator

Under the coordinate weight convention used by the script,

\[
\partial_{\bar z_1} : \operatorname{wt}\mapsto \operatorname{wt}+1,
\]
\[
\partial_{\bar z_2} : \operatorname{wt}\mapsto \operatorname{wt}+(n-1),
\]
\[
\partial_{z_1} : \operatorname{wt}\mapsto \operatorname{wt}-1,
\]
\[
\partial_{z_2} : \operatorname{wt}\mapsto \operatorname{wt}-(n-1).
\]

The selected input weights are

\[
w_0=m,\qquad w_1=m-n.
\]

Now inspect the two entries in the first row of \(D_0\).

From component \(0\),

\[
\partial_{\bar z_1}:\quad w_0+1=m+1.
\]

From component \(1\),

\[
\partial_{\bar z_2}:\quad w_1+(n-1)=m-n+n-1=m-1.
\]

Thus the two terms that the script adds into the same first output component have weights

\[
m+1 \quad\text{and}\quad m-1.
\]

Their difference is \(2\). For odd \(n\ge 3\),

\[
2\not\equiv 0 \pmod{n^2}.
\]

So the two summands in row \(0\) belong to different \(\Gamma\)-eigenspaces. The same problem appears in row \(1\):

\[
-\partial_{z_2}:\quad w_0-(n-1)=m-n+1,
\]

whereas

\[
\partial_{z_1}:\quad w_1-1=m-n-1.
\]

Again the two weights differ by \(2\).

Therefore \(D_0\) does not map the selected positive-spinor equivariance sectors into a single negative-spinor equivariance sector. It is not an intertwining operator for the Step-93 fibre weights \((m,m-n)\) with the condition \(\operatorname{wt}=\) fibre weight.

Equivalently, \(D_0\) would be equivariant if the second positive-spinor weight were shifted to

\[
m-n+2
\]

instead of \(m-n\), because then

\[
(m-n+2)+(n-1)=m+1
\]

and

\[
(m-n+2)-1=m-n+1.
\]

But that shifted weight changes the constant-term allowed twists: component \(1\) would allow a constant when \(m-n+2\equiv0\), i.e. \(m\equiv n-2\), not when \(m\equiv n\). That contradicts the Step-89/Step-93 character statement that constant positive spinors occur exactly for \(m\in\{0,n\}\), i.e. \(j\in\{0,1\}\). Hence the script’s operator and the Step-93 weights are not mutually compatible.

---

### 3. The sign/convention mismatch

There are two consistent conventions in common use.

#### Convention A: invariant-jet convention

A homogeneous Taylor coefficient is an element of

\[
\operatorname{Sym}^\ell T^*_p\otimes S^+_p.
\]

The tensor is \(\Gamma\)-invariant when

\[
\operatorname{wt}+\text{fibre weight}\equiv 0 \pmod{N}.
\]

With the Step-93 positive-spinor weights

\[
(m,\;m-n),
\]

the component conditions are

\[
\operatorname{wt}\equiv -m,\qquad \operatorname{wt}\equiv -(m-n)\pmod{N}.
\]

The standard Kähler spin\(^c\) Dirac operator compatible with this convention is, up to irrelevant signs,

\[
D_{\mathrm{std}}=
\begin{pmatrix}
\partial_{\bar z_1} & -\partial_{z_2}\\
\partial_{\bar z_2} & \partial_{z_1}
\end{pmatrix}.
\]

Indeed, the row weights then agree:

- row \(0\): from component \(0\),

\[
-m+1,
\]

from component \(1\),

\[
-(m-n)-(n-1)=1-m;
\]

- row \(1\): from component \(0\),

\[
-m+n-1,
\]

from component \(1\),

\[
-(m-n)-1=n-m-1.
\]

So \(D_{\mathrm{std}}\) preserves the equivariance sectors in this convention.

#### Convention B: section/function convention

One writes an equivariant section as

\[
s(\gamma x)=\rho(\gamma)s(x),
\]

so component functions have weight equal to the fibre weight:

\[
\operatorname{wt}\equiv m,\qquad \operatorname{wt}\equiv m-n.
\]

This is the sign used by the script. The Dirac operator compatible with that sign is the complex conjugate of the standard one:

\[
D_{\mathrm{conj}}=
\begin{pmatrix}
\partial_{z_1} & -\partial_{\bar z_2}\\
\partial_{z_2} & \partial_{\bar z_1}
\end{pmatrix},
\]

again up to Clifford signs. This operator preserves the sectors with weights \((m,m-n)\).

The script mixes the section/function weight condition \(\operatorname{wt}=\) fibre weight with the unrelated Fueter-type matrix \(D_0\). That is the source of the reported \(\ell=n\) pattern.

---

### 4. Corrected first monogenic degree

Use either consistent convention. I will state the result in the invariant-jet convention, with

\[
D_{\mathrm{std}}=
\begin{pmatrix}
\partial_{\bar z_1} & -\partial_{z_2}\\
\partial_{\bar z_2} & \partial_{z_1}
\end{pmatrix},
\qquad
\operatorname{wt}+\text{fibre weight}\equiv0.
\]

For an extendible twist

\[
m=nj,\qquad j=2,\dots,n-1,
\]

the two positive-spinor component conditions are

\[
\operatorname{wt}\equiv -nj \pmod{n^2},
\]

and

\[
\operatorname{wt}\equiv -n(j-1) \pmod{n^2}.
\]

A useful elementary fact is:

> For \(0\le r\le n\), the least homogeneous degree of a monomial whose weight is congruent to \(nr\pmod{n^2}\) is
> \[
> 2\min(r,n-r).
> \]

The two realizing monomials are

\[
(z_1z_2)^r,
\]

with weight \(nr\) and degree \(2r\), and

\[
(\bar z_1\bar z_2)^{\,n-r},
\]

with weight \(-n(n-r)\equiv nr\pmod{n^2}\) and degree \(2(n-r)\).

Applying this to the two component residues gives:

- component \(0\): residue \(-nj\equiv n(n-j)\), minimal degree
  \[
  2\min(j,n-j);
  \]

- component \(1\): residue \(-n(j-1)\), minimal degree
  \[
  2\min(j-1,n-j+1).
  \]

The smaller of these is

\[
\boxed{
\ell_{\min}(n,j)=2\min(j-1,\;n-j).
}
\]

This lower bound is sharp, because explicit monogenic equivariant spinors exist at that degree.

If

\[
j-1\le n-j,
\]

then

\[
\Phi=
\begin{pmatrix}
0\\
(\bar z_1\bar z_2)^{j-1}
\end{pmatrix}
\]

has component \(1\) weight \(-n(j-1)\), is killed by \(D_{\mathrm{std}}\) because the second component is anti-holomorphic, and has degree

\[
2(j-1).
\]

If

\[
n-j\le j-1,
\]

then

\[
\Phi=
\begin{pmatrix}
(z_1z_2)^{n-j}\\
0
\end{pmatrix}
\]

has component \(0\) weight \(n(n-j)\equiv -nj\), is killed by \(D_{\mathrm{std}}\) because the first component is holomorphic, and has degree

\[
2(n-j).
\]

Thus the first nonzero equivariant homogeneous monogenic spinor occurs at

\[
\boxed{
\ell_{\min}(n,j)=2\min(j-1,n-j)
}
\]

for every odd \(n\ge3\) and every forced extendible twist \(j=2,\dots,n-1\).

In the section/function convention, the same result appears with conjugate monomials. Keeping the script’s condition \(\operatorname{wt}=\) fibre weight, the compatible operator is \(D_{\mathrm{conj}}\), and the explicit first modes are:

- if \(j-1\le n-j\),

\[
\Phi=
\begin{pmatrix}
0\\
(z_1z_2)^{j-1}
\end{pmatrix};
\]

- if \(n-j\le j-1\),

\[
\Phi=
\begin{pmatrix}
(\bar z_1\bar z_2)^{n-j}\\
0
\end{pmatrix}.
\]

The degrees are the same.

For small odd \(n\), the corrected table is:

\[
\begin{array}{c|c}
n & \ell_{\min}(j),\ j=2,\dots,n-1\\
\hline
3 & 2\\
5 & 2,\ 4,\ 2\\
7 & 2,\ 4,\ 6,\ 4,\ 2\\
9 & 2,\ 4,\ 6,\ 8,\ 6,\ 4,\ 2\\
11 & 2,\ 4,\ 6,\ 8,\ 10,\ 8,\ 6,\ 4,\ 2
\end{array}
\]

The maximal corrected vanishing order is therefore \(n-1\), attained at the middle twist \(j=(n+1)/2\). In particular, for odd \(n\), the corrected first degree is even, whereas the script reports the odd number \(n\).

---

### 5. Why the script saw \(\ell=n\)

The script’s matrix \(D_0\) annihilates different low-degree modes from the compatible Dirac operator.

For example, take \(n=5\), \(j=2\), so \(m=10\). In the corrected invariant-jet convention, there is a degree-two monogenic spinor

\[
\Phi=
\begin{pmatrix}
0\\
\bar z_1\bar z_2
\end{pmatrix}.
\]

It has component \(1\) weight \(-5\), which matches \(-(m-n)=-5\), and \(D_{\mathrm{std}}\Phi=0\).

The script’s operator gives instead

\[
D_0
\begin{pmatrix}
0\\
\bar z_1\bar z_2
\end{pmatrix}
=
\begin{pmatrix}
\partial_{\bar z_2}(\bar z_1\bar z_2)\\
\partial_{z_1}(\bar z_1\bar z_2)
\end{pmatrix}
=
\begin{pmatrix}
\bar z_1\\
0
\end{pmatrix},
\]

so this mode is not in its kernel. The JSON then records no kernel until degree \(5\). That degree-\(5\) kernel is a property of the particular non-intertwining matrix \(D_0\) restricted to the selected input sectors, not a property of the Step-93 equivariant flat Dirac problem.

Thus the reported pattern

\[
\ell_{\min}=n
\]

is not a geometric theorem about Wahl spinors under the Step-93 character convention. The provable corrected statement is

\[
\ell_{\min}=2\min(j-1,n-j).
\]

---

### 6. Exact rank counting in a corrected computation

For the corrected standard operator, one can avoid large matrix rank computations. The homogeneous Dirac map

\[
D_{\mathrm{std}}: P_\ell\otimes S^+ \longrightarrow P_{\ell-1}\otimes S^-
\]

is surjective on polynomial spaces. Averaging over the finite abelian group \(\Gamma\) preserves surjectivity on invariant subspaces. Therefore the dimension of the invariant kernel in degree \(\ell\) is simply

\[
\dim\ker_\Gamma(D_{\mathrm{std}})_\ell
=
\#\{\text{degree }\ell\text{ domain monomials in the two }S^+\text{ residues}\}
-
\#\{\text{degree }\ell-1\text{ target monomials in the two }S^-\text{ residues}\}.
\]

The first degree where this difference becomes positive is exactly the degree given above. This gives an all-\(n\) proof without relying on finite Sympy rank calculations.

---

### 7. What the vanishing order does imply for \(D_2\)

Step 94 defines the endpoint deficit

\[
D_2=\frac32 S+18W-72\pi^2 p
\]

in the scale where the Einstein metric has \(s=-4\), and relates \(D_2\) to the same-field controls

\[
J_+,\qquad
\|\rho-\rho_0\|_2^2,\qquad
\|W^+-W_0\|_2^2,\qquad
\|\operatorname{Ric}+g\|_2^2,
\]

and to the alignment of the self-dual polynomial form \(\omega=q(\Phi)\) with the harmonic representative \(H_a\).

A forced zero of order \(\ell\) means that near the Wahl point,

\[
\Phi = r^\ell P_\ell(\theta)+O(r^{\ell+1}),
\]

with \(P_\ell\) one of the equivariant monogenic modes described above. Since \(\ell\ge2\), also

\[
\nabla_A\Phi = O(r^{\ell-1}).
\]

This has the following consequences.

#### Fixed-metric strictness

For a fixed orbifold metric and a fixed supplied monopole with a forced marked character, exact \(D_2=0\) would force the limiting model to contain a nowhere-zero constant-length harmonic self-dual form and a spinor compatible with the Kähler endpoint. A spinor vanishing at the Wahl point is incompatible with that exact endpoint. Hence, for each fixed metric carrying such a monopole,

\[
D_2>0.
\]

This recovers the strict scalar excess already noted in Step 93/Step 94.

#### No uniform metric-independent amount

The order \(\ell\) alone does not produce a universal lower amount in \(D_2\). The local energy of a degree-\(\ell\) zero on a ball of radius \(r\) scales with positive powers of \(r\). Schematically,

\[
\int_{B_r} |\nabla_A\Phi|^2 \sim r^{2\ell+2},
\]

and

\[
\int_{B_r} |\Phi|^4 \sim r^{2\ell+4},
\]

up to curvature and connection terms. In a dimensionless Einstein normalization, the relevant quantity is the regularity scale \(\lambda r_0^2\) at the Wahl point. If that scale collapses through Ricci-flat bubbling, the contribution of the forced zero to the global integral can tend to zero.

Thus the corrected order

\[
\ell=2\min(j-1,n-j)
\]

—or the script’s erroneous \(\ell=n\)—does not by itself yield

\[
D_2\ge c>0
\]

uniformly over Einstein orbifold metrics. It gives strictness for each fixed metric, not a uniform Einstein obstruction.

The unresolved analytic quantity remains the one identified in Step 94: a uniform estimate for \(D_2/V\), or for the retained endpoint sum in the \(D_2\)-control inequalities, in terms of the marked character and the local regularity scale. Without control of \(\lambda r_0^2\), or a bubble-tree invariant that prevents the marked character from migrating into arbitrarily small bubbles, the vanishing order does not enter the global Einstein budget as a definite additive term.

---

### 8. What the vanishing order does not supply as a shrinking-link residue

The forced zero also does not create a nonzero shrinking-link residue.

Near the Wahl point,

\[
\Phi=O(r^\ell),\qquad \nabla_A\Phi=O(r^{\ell-1}),\qquad \ell\ge2.
\]

Therefore the usual local fluxes over a small link \(S_r\) vanish as \(r\to0\). Stress-energy-type integrals, Chern-Simons-type terms, and Pohozaev-type fluxes all carry positive powers of \(r\) after integration over the three-sphere. The removability result of Step 93 already shows that the abelian connection extends with \(F_A\in L^2\), so no singular holonomy residue remains on shrinking links.

One may renormalize by powers of \(r\) or by \(|\Phi|^2\) to extract the leading jet \(P_\ell\). That gives a local jet invariant, but not a conserved unscaled charge. It depends on the amplitude of the particular solution and is not a topological payment.

The character itself also supplies no extra APS or eta term. Step 93’s exact Kawasaki computation gives, for every extendible twist \(m=nj\),

\[
\delta(m)=\delta(0),
\]

so the reduced local Dirac defect is the same as the trivial twist. The extendible subgroup is isotropic for the lens-space linking form. The vanishing order \(\ell\) does not alter these facts. It changes the Taylor mode, not the link holonomy, eta invariant, or index transfer.

Hence the marked character plus vanishing order does not currently yield a nonzero shrinking-link residue that could be converted into trace-free Ricci energy or into a uniform contribution to \(D_2\).

---

### 9. Bottom line

The exact rational computation in the script is internally exact for the matrix it constructs, but the matrix \(D_0\) is not the \(\Gamma\)-equivariant flat Dirac operator for the Step-93 positive-spinor weights \((m,m-n)\). The row entries combine terms whose output weights differ by \(2\), so the selected sectors are not preserved.

With a consistent convention, the corrected first equivariant monogenic degree is

\[
\boxed{
\ell_{\min}(n,j)=2\min(j-1,n-j)
}
\]

for odd \(n\ge3\) and forced extendible twists \(j=2,\dots,n-1\). The maximum is \(n-1\), not \(n\), and many forced twists have order \(2\) or \(4\).

This corrected vanishing order strengthens the fixed-metric strictness of the same-field endpoint but does not by itself give a uniform \(D_2\) amount or a nonzero shrinking-link residue. The missing substance remains a uniform control of the local Einstein regularity scale at the Wahl point, or a curvature-sensitive Taylor recursion that produces a sign-definite contribution to the endpoint deficit.