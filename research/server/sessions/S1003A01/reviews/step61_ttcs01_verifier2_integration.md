# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 61,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step61_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step61_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check A02's new zero-index algebra and its relevance to the closed negative Goldberg problem. Starting with the exact soldered equation and a nondegenerate torsion zero f(z)=c z+B bar(z), B=S+A with S complex symmetric and A complex antisymmetric, verify the real Jacobian determinant formula det_R Df=|c|^4-|c|^2(||S||^2-||A||^2)+|det B|^2 under the stated norm conventions. Derive the sharp implications for negative versus positive local index, test the examples f=z, f=A bar(z), and f=(z1+2 bar z1,z2), and explain which pure modes are scientifically decisive for the first nonlinear prolongation. Also assess whether any pointwise Weyl localization or Chern–Weil density currently constrains these indices. Ground the reading in the A01/A02 notes; do not infer existence of a full Einstein germ from principal-symbol algebra.

## Integrated Scientific Memo

## Verification memo

**The determinant formula in A02 Step 75 is correct with full Hilbert–Schmidt matrix norms.** Its negative-index criterion can be sharpened to a strict inequality plus an exact interval for \(|c|^2\). The algebra permits both signs and therefore supplies no contradiction to the positive Euler charge in the closed negative Goldberg problem. The first nonlinear prolongation remains unreported in the supplied Step 76 note.

### 1. From the exact soldered equation to the first jet

A01 Step 56 and A02 Step 75 give the exact Einstein torsion equation
\[
(d_b\alpha)^-=0,
\]
equivalently, the vanishing of the primitive \((1,1)\) component of \(d_b\alpha\), together with the sourced divergence equation
\[
d_b^*\alpha=2\eta
\]
in A01’s conventions. The complex type conventions for \(\alpha\) differ between the notes; using A01’s coefficient coordinates avoids this ambiguity.

At a torsion zero \(p\), connection and moving-frame terms multiplying \(\alpha(p)\) vanish. Thus the first jet obeys
\[
\partial_{z_1}f_2=0,\qquad
\partial_{z_2}f_1=0,\qquad
\partial_{z_1}f_1=\partial_{z_2}f_2,
\]
and hence
\[
T(z)=f(z)+O(|z|^2),\qquad f(z)=cz+B\bar z.
\]
This is the full five-complex-dimensional kernel of the first-jet constraint—not a proof that every such jet extends to an Einstein solution.

Write
\[
S=\frac{B+B^T}{2},\qquad A=\frac{B-B^T}{2}.
\]
At the zero, the notes identify \(c\) with the \(W_2^+\) or \(\eta\) channel, \(A\) with the \(W_3^+\) channel, and \(S\) with the symmetric derivative component invisible to the leading exterior derivative and divergence. The quadratic torsion corrections vanish there.

Use the norms
\[
\|S\|^2=\sum_{i,j}|S_{ij}|^2,\qquad
\|A\|^2=\sum_{i,j}|A_{ij}|^2.
\]
In particular,
\[
A=\begin{pmatrix}0&a\\-a&0\end{pmatrix}
\quad\Longrightarrow\quad \|A\|^2=2|a|^2.
\]
These are matrix Hilbert–Schmidt norms; their conversion to geometric Weyl norms involves the convention-dependent constants not recomputed in Step 75.

### 2. Determinant derivation and sharp sign classification

The complexification of the real derivative is
\[
M=\begin{pmatrix}cI&B\\ \bar B&\bar cI\end{pmatrix}.
\]
Changing from real coordinates to \((z,\bar z)\) is a similarity transformation, so
\[
\det_{\mathbb R}Df=\det_{\mathbb C}M.
\]
For \(c\ne0\), the Schur complement gives
\[
\det_{\mathbb C}M
=\det\bigl(|c|^2I-\bar BB\bigr).
\]
Polynomial continuation establishes the same identity at \(c=0\). Here \(\bar B\) is entrywise conjugation, **not** the adjoint.

Symmetry and antisymmetry imply
\[
\operatorname{tr}(\bar SS)=\|S\|^2,\qquad
\operatorname{tr}(\bar AA)=-\|A\|^2,\qquad
\operatorname{tr}(\bar SA)=\operatorname{tr}(\bar AS)=0.
\]
Since \(\det(\bar BB)=|\det B|^2\),
\[
\boxed{\det_{\mathbb R}Df
=|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2.}
\]

Set
\[
t=|c|^2,\qquad d=\|S\|^2-\|A\|^2,\qquad r=|\det B|.
\]
Then \(D:=\det_{\mathbb R}Df=t^2-dt+r^2\). For a nondegenerate zero,
\[
\operatorname{ind}_p(T)=\operatorname{sign}D.
\]

The **necessary and sufficient** condition for negative index is
\[
\boxed{
d>2r,\qquad
\frac{d-\sqrt{d^2-4r^2}}2
<t<
\frac{d+\sqrt{d^2-4r^2}}2.
}
\]
Consequently, negative index requires
\[
c\ne0,\qquad S\ne0,\qquad
\|S\|^2-\|A\|^2>2|\det B|.
\]
The weak inequality in Proposition 75.I is a valid necessary statement, but not sharp. At equality,
\[
D=(t-r)^2,
\]
so negative index is impossible.

Conversely:

- If \(d\le2r\), every nondegenerate jet has positive index.
- If \(d>2r\), positive index occurs outside the closed interval between the two roots; the endpoints are degenerate.
- In particular, \(c=0\), \(S=0\), or \(\|S\|\le\|A\|\) ensures positive index whenever the jet is nondegenerate.

For \(A=0\), Takagi factorization of \(S\), with singular values \(\sigma_1,\sigma_2\), gives the useful specialization
\[
D=(|c|^2-\sigma_1^2)(|c|^2-\sigma_2^2).
\]
Negative index occurs exactly when \(|c|\) lies strictly between the two singular values.

The source’s assertion that positive-index zeros are “the generic case of the kernel” is not justified: both sign regions are nonempty open subsets of the ten-real-dimensional kernel. The antiholomorphic slice \(c=0\) has positive codimension.

### 3. Required examples

| Model | Determinant | Local index |
|---|---:|---:|
| \(f=z\) | \(1\) | \(+1\) |
| \(f=A\bar z,\ A=\begin{pmatrix}0&a\\-a&0\end{pmatrix}\) | \(|a|^4\) | \(+1\) if \(a\ne0\) |
| \(f=(z_1+2\bar z_1,z_2)\) | \(-3\) | \(-1\) |

For the third example,
\[
c=1,\quad S=\operatorname{diag}(2,0),\quad A=0,
\]
so \(D=1-4=-3\). Directly,
\[
z_1+2\bar z_1=3x_1-iy_1,
\]
whose real determinant is \(-3\), while the second component contributes \(1\).

The positive sign of the pure \(A\)-mode also follows because full conjugation of \(\mathbb C^2\) has real determinant \((-1)^2=+1\). This same observation resolves the full-conjugation convention change between the two torsion descriptions.

### 4. Consequence for the closed negative Goldberg problem

A01 Step 59 computes
\[
c_2(E)=c_2(TM)+2c_1(TM)^2,\qquad
\langle c_2(E),[M]\rangle=5\chi+6\tau.
\]
For a closed Einstein four-manifold with nonzero scalar curvature,
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
If the torsion zeros are isolated and nondegenerate,
\[
\sum_p\operatorname{ind}_p(T)=5\chi+6\tau.
\]
For general zero sets, the supported Euler class remains the appropriate statement.

The first-jet constraint allows the positive indices needed by this topology, as well as negative indices. Thus **topology plus the soldered first-order equation gives no contradiction**. Even a theorem forcing every nondegenerate zero to have positive index would remain compatible with the required total charge.

A theorem excluding every torsion zero of a strict negative Einstein almost-Kähler structure would be decisive. Excluding only nondegenerate zeros would leave degenerate and nonisolated zero sets unresolved.

### 5. Pure modes and the first nonlinear prolongation

The two curvature-visible positive-charge tests proposed in Step 75 are scientifically distinct:
\[
\begin{array}{lll}
f=cz,\ c\ne0: & \eta(p)\ne0,& W_3^+(p)=0,\\
f=A\bar z,\ A\ne0: & \eta(p)=0,& W_3^+(p)\ne0.
\end{array}
\]
They isolate the two curvature channels rather than merely changing coordinates in one model.

A third essential test is
\[
f=S\bar z,\qquad S^T=S,\quad \det S\ne0.
\]
It has
\[
D=|\det S|^2>0,\qquad \eta(p)=W_3^+(p)=0.
\]
Thus \(W^+(p)\) is of Kähler type, yet the torsion has a nondegenerate linear zero. **Kähler-type Weyl curvature at one point does not imply neighborhood integrability.** This pure symmetric mode is precisely the derivative freedom exposed by A01 Step 56’s \(h\)-test.

Pure-mode tests do not exhaust the problem: nonlinear compatibility can involve mixed modes and the remaining curvature variables. In particular, negative index requires mixing the \(c\)- and symmetric sectors.

Step 76 supplies a concrete prolongation framework:
\[
\Omega=dx^{12}+dx^{34},\qquad g=e^H,\qquad
H^T=H,\quad HJ_0=-J_0H,\quad H=H_2+H_3+\cdots.
\]
Its first nonlinear Einstein compatibility conditions have the form
\[
\left\langle\ell,Q(H_2,H_2)-\lambda H_2\right\rangle=0,
\qquad \ell\in\operatorname{coker}L_2,
\]
after accounting for Bianchi relations. Here \(H_2\) must satisfy the order-zero Einstein equation and contain the specified torsion jet plus the remaining compatible curvature data. Contrary to one branch’s wording, \(\lambda\) already enters at order zero; order two is the first **nonlinear** compatibility stage.

The corresponding intrinsic quadratic information includes
\[
\nabla^2q(p)(X,Y)
=2\langle\nabla_XT,\nabla_YT\rangle,
\qquad
\nabla^2\kappa(p)(X,Y)
=3\langle\nabla_XT,\nabla_YT\rangle,
\]
and differentiated Einstein/AAD Bianchi identities.

The unresolved object is the projection of this order-two compatibility variety onto the \((c,A,S)\) first-jet space. The supplied Step 76 ends before reporting that computation. Survival through this stage would establish finite formal compatibility only—not a full formal solution or a convergent Einstein germ.

### 6. What Weyl data and Chern–Weil densities currently constrain

There is one genuine pointwise implication:
\[
\eta(p)=0\iff c=0
\quad\Longrightarrow\quad
\operatorname{ind}_p(T)=+1
\]
for a nondegenerate zero. Beyond it, curvature-visible first-jet data do not determine the index.

Indeed, fix \(c\ne0\) and
\[
A=\begin{pmatrix}0&a\\-a&0\end{pmatrix}.
\]
Taking \(S=0\) gives
\[
D=(|c|^2+|a|^2)^2>0.
\]
Taking instead
\[
S=\operatorname{diag}(R,-a^2/R),\qquad R>0,
\]
gives
\[
\det B=0,\qquad
d=\left(R-\frac{|a|^2}{R}\right)^2,
\qquad D=|c|^2(|c|^2-d)<0
\]
for sufficiently large \(R\). Thus the same \(c,A\), hence the same curvature-visible channels, admit both signs in the necessary first-jet algebra. Whether both extend is exactly the prolongation question.

At \(s=-12\), Step 76 gives the smooth densities
\[
4\pi^2\rho_{\rm LC}
=15+\frac92|W^+|^2+\frac12|W^-|^2,
\]
\[
4\pi^2\rho_{\bar\nabla}
=42-\frac{27}{8}q+\frac94|\eta|^2+\frac12|W^-|^2.
\]
At a torsion zero,
\[
4\pi^2\rho_{\bar\nabla}(p)
=42+\frac94|\eta(p)|^2+\frac12|W^-(p)|^2>0,
\]
independently of \(S\) and the index. Their difference is the Step 76 transgression expression
\[
4\pi^2(\rho_{\rm LC}-\rho_{\bar\nabla})
=\frac94\left(
|\eta|^2+2|W_3^+|^2+\frac3{16}q^2-\frac32q
\right).
\]

These smooth representatives yield the global Euler number, not individual zero degrees. Their positivity cannot be interpreted as positivity of each torsion index. A01’s complete strict pair reinforces this distinction: Step 76 reports positive canonical density everywhere, while Step 59 reports no finite torsion zero.

A section-dependent Thom/Mathai–Quillen localization, or a suitable connection defined off the zero set through the opposite structure, can recover signed local degrees. **No supplied calculation establishes a geometric sign restriction for such a localized representative.** The present obstruction is therefore not the determinant algebra but the missing nonlinear relation constraining the symmetric jet—and, ultimately, the existence or exclusion of actual negative Einstein almost-Kähler germs with torsion zeros.