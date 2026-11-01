# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step56_soldered_instanton_and_SU2_AKE.md",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A02/workspace/notes/step76_Q4_chern_weil_density_and_prolongation.md"
  ]
}
```

## Task

Independently check A02's new zero-index algebra and its relevance to the closed negative Goldberg problem. Starting with the exact soldered equation and a nondegenerate torsion zero f(z)=c z+B bar(z), B=S+A with S complex symmetric and A complex antisymmetric, verify the real Jacobian determinant formula det_R Df=|c|^4-|c|^2(||S||^2-||A||^2)+|det B|^2 under the stated norm conventions. Derive the sharp implications for negative versus positive local index, test the examples f=z, f=A bar(z), and f=(z1+2 bar z1,z2), and explain which pure modes are scientifically decisive for the first nonlinear prolongation. Also assess whether any pointwise Weyl localization or Chern–Weil density currently constrains these indices. Ground the reading in the A01/A02 notes; do not infer existence of a full Einstein germ from principal-symbol algebra.

## Output

# Independent verification memo: torsion-zero index algebra

## 1. First jet from the exact soldered equation

For an almost-Kähler Einstein four-manifold, A02 Step 75 gives the exact equation
\[
\mathcal P\alpha=\bigl(d_b\alpha\bigr)^{1,1}_0=0,
\]
where \(\alpha\) is the complex rank-two torsion section. At a zero \(p\), the connection term \(b\wedge\alpha\) vanishes. In unitary coordinates and a unitary frame at \(p\), the first jet \(f=(f_1,f_2)\) therefore satisfies
\[
\partial_{z_1}f_2=0,\qquad
\partial_{z_2}f_1=0,\qquad
\partial_{z_1}f_1=\partial_{z_2}f_2.
\]
Consequently,
\[
f(z)=cz+B\bar z+O(|z|^2),\qquad c\in\mathbb C,\quad B\in M_2(\mathbb C).
\]
Write
\[
S=\frac{B+B^T}{2},\qquad A=\frac{B-B^T}{2},
\]
so \(S^T=S\), \(A^T=-A\). Here \(c\) is the \(W_2^+\) or \(\eta\) channel, \(A\) is the \(W_3^+\) channel, and \(S\) is the symmetric twistor derivative unseen by the exterior derivative and divergence at this order.

The relevant matrix norms are the full Hilbert–Schmidt norms
\[
\|S\|^2=\operatorname{tr}(S^*S)=\sum_{i,j}|S_{ij}|^2,
\qquad
\|A\|^2=\operatorname{tr}(A^*A).
\]
Thus an off-diagonal entry is counted twice. In particular, for
\[
A=\begin{pmatrix}0&a\\-a&0\end{pmatrix},
\qquad \|A\|^2=2|a|^2.
\]

## 2. Real Jacobian determinant

The complexification of the real derivative of \(f(z)=cz+B\bar z\), in variables \((z,\bar z)\), is
\[
M=
\begin{pmatrix}
cI&B\\
\bar B&\bar c I
\end{pmatrix}.
\]
Its complex determinant equals the determinant of the underlying real Jacobian. For \(c\ne0\), the Schur complement gives
\[
\det_{\mathbb R}Df
=\det_{\mathbb C}M
=\det\bigl(|c|^2I-\bar B B\bigr).
\]
Both sides are polynomial in the entries, so the identity also holds at \(c=0\). Expanding the \(2\times2\) determinant,
\[
\det_{\mathbb R}Df
=|c|^4-|c|^2\operatorname{tr}(\bar BB)+|\det B|^2.
\]

The transpose decomposition gives
\[
\operatorname{tr}(\bar SS)=\|S\|^2,\qquad
\operatorname{tr}(\bar AA)=-\|A\|^2,
\]
while
\[
\operatorname{tr}(\bar SA)=\operatorname{tr}(\bar AS)=0.
\]
Hence
\[
\boxed{
\det_{\mathbb R}Df
=
|c|^4-|c|^2\bigl(\|S\|^2-\|A\|^2\bigr)+|\det B|^2.
}
\]
Thus A02 equation (75.5) is correct with the Hilbert–Schmidt convention above.

## 3. Exact sign classification

Set
\[
t=|c|^2,\qquad d=\|S\|^2-\|A\|^2,\qquad r=|\det B|.
\]
Then
\[
D:=\det_{\mathbb R}Df=t^2-dt+r^2.
\]
For a nondegenerate zero, \(D\ne0\), and its local index is \(\operatorname{sign}D\).

The exact condition for index \(-1\) is
\[
d>2r
\]
together with
\[
\frac{d-\sqrt{d^2-4r^2}}2
<t<
\frac{d+\sqrt{d^2-4r^2}}2.
\]
In particular, index \(-1\) requires
\[
c\ne0,\qquad S\ne0,\qquad
\|S\|^2-\|A\|^2>2|\det B|.
\]
The strict inequality sharpens the weak inequality stated in Step 75. At equality,
\[
D=(t-r)^2,
\]
so one obtains either index \(+1\) or a degenerate zero, never index \(-1\).

For index \(+1\):

- If \(d\le2r\), every nondegenerate zero has \(D>0\).
- If \(d>2r\), one has \(D>0\) when \(t\) lies outside the closed interval between the two roots.
- In particular, \(c=0\), \(S=0\), or \(\|S\|\le\|A\|\) gives index \(+1\), provided the zero is nondegenerate.

## 4. Test examples

### Pure \(c\)-mode: \(f=z\)

Here \(c=1\), \(B=0\), so
\[
D=|c|^4=1.
\]
The index is \(+1\).

### Pure \(A\)-mode: \(f=A\bar z\)

For
\[
A=\begin{pmatrix}0&a\\-a&0\end{pmatrix},\qquad a\ne0,
\]
one has \(c=0\), \(S=0\), \(\det A=a^2\), and therefore
\[
D=|\det A|^2=|a|^4>0.
\]
The index is \(+1\). This is also consistent with the fact that conjugation on \(\mathbb C^2\) preserves the real orientation.

### A01’s mixed example

For
\[
f=(z_1+2\bar z_1,z_2),
\]
one has
\[
c=1,\qquad B=S=\begin{pmatrix}2&0\\0&0\end{pmatrix},\qquad A=0.
\]
Thus
\[
\|S\|^2=4,\qquad \det B=0,\qquad D=1-4=-3.
\]
The index is \(-1\). Directly,
\[
z_1+2\bar z_1=3x_1-iy_1,
\]
whose real \(2\times2\) determinant is \(-3\), while the second component contributes \(+1\).

## 5. Relevance to the closed \(s<0\) Goldberg problem

For the torsion bundle
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
A01 Step 59 computes
\[
\langle c_2(E),[M]\rangle=5\chi+6\tau
=\chi+2(2\chi+3\tau)>0
\]
for a closed Einstein four-manifold with nonzero scalar curvature. If all torsion zeros are isolated and nondegenerate,
\[
\sum_{p:T(p)=0}\operatorname{ind}_p(T)=5\chi+6\tau.
\]
The first-order soldered equation permits both signs, including abundant \(+1\) models. Hence the Euler number and the exact first-order equation are mutually compatible; they do not produce a contradiction.

The two clean curvature-visible representatives for the first nonlinear prolongation are:

1. \(f=cz\), isolating the \(W_2^+\) or \(\eta\) channel;
2. \(f=A\bar z\), isolating the \(W_3^+\) channel.

Both carry index \(+1\), so each directly tests whether the positive Euler charge can survive the first quadratic Einstein/AAD compatibility equations. The relevant new terms are precisely those identified in A01 Step 59 and A02 Step 76:
\[
\nabla^2q(0)=2\langle\nabla T,\nabla T\rangle,\qquad
\nabla^2\kappa(0)=3\langle\nabla T,\nabla T\rangle,
\]
together with differentiated Bianchi identities and the Darboux-form quadratic term
\[
Q(H_2,H_2)-\lambda H_2.
\]

The \(c\)- and \(A\)-modes do not exhaust the first-jet space. A pure symmetric mode \(f=S\bar z\), with \(S\) invertible, also has
\[
D=|\det S|^2>0.
\]
Thus even incompatibility of both curvature-visible pure modes would leave the symmetric \(S^2\) component and mixed orbits unresolved. Step 76 ends before reporting the order-two computation, so the supplied material contains no nonlinear compatibility result for any of these jets. Principal-symbol algebra alone constructs no Einstein germ, and compatibility through one finite prolongation would still not establish a convergent germ.

## 6. Weyl data and Chern–Weil densities

There is one partial pointwise implication: \(W_2^+(p)=0\) gives \(c=0\), so every nondegenerate zero at that point has index \(+1\). Beyond this, pointwise Weyl data do not determine the index because the symmetric component \(S\) is invisible to curvature at first order.

A concrete demonstration is
\[
c=1,\qquad A=0,\qquad S=\operatorname{diag}(s,0),
\]
for which the curvature-visible data \(c,A\) remain fixed while
\[
D=1-|s|^2
\]
changes sign through a degenerate jet at \(|s|=1\).

The canonical-connection representative from A02 Step 76 is
\[
4\pi^2c_2(E)_{\bar\nabla}
=
\left(
42-\frac{27}{8}q+\frac94|\eta|^2+\frac12|W^-|^2
\right)d\mu
\qquad(s=-12).
\]
At a torsion zero, \(q=0\), so this density is strictly positive:
\[
4\pi^2c_2(E)_{\bar\nabla}(p)
=
42+\frac94|\eta|^2+\frac12|W^-|^2.
\]
It contains no information about \(S\) or the orientation of \(Df\), and therefore does not distinguish index \(+1\) from index \(-1\). The Levi-Civita representative has the same issue.

This is reinforced by A01’s complete strict Bianchi-VIII pair: the canonical density is positive everywhere, ranging from \(6/(4\pi^2)\) at the bolt to \(42/(4\pi^2)\) at infinity, even though the torsion has no finite zero. Thus the current smooth Chern–Weil densities are not zero-localized. Recovering individual indices would require a torsion-section localization such as a Thom or Mathai–Quillen representative, or a connection defined through the opposite structure off the zero set.