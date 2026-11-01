# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step13.md"
  ]
}
```

## Task

For the four-dimensional negative-branch near-Einstein circle collapse problem, consider a rank-one Kaluza-Klein metric g = g_B + ℓ²(dψ+A)² with Ric ≈ -g on a closed 4-manifold. The normalized cover g = g_B + v²(dz+B)² with v(p)=1 removes the fiber period from local coefficients. The reduced Einstein equations are: (V) Δv/v = 1 + v²|F_B|²/2, (M) div(v²F_B) ≈ 0, (H) Ric_B = -I + Hess(v)/v + (v²/2)F_B⊗F_B. The chiral variables a± = u ∓ z/2 (where u=d log v, z=*(vF_B)) satisfy W± = -[sym∇a± + a±⊗a±]₀ and da+ = a+∧a-. The calibrated W+ spectrum is (-1/6, 1/12, 1/12). The key analytical question: on the calibrated bulk where the W+ defect vanishes, does the chiral constraint force the Hessian tensor H = Hess(v)/v to have nonnegative eigenvalues? If H ≥ 0, then Ric_B ≥ -I (since the twist contribution is nonneg), giving a 3D Bishop-Gromov volume lower bound and 4D cover noncollapse. Investigate: (1) Can the calibrated W+ = E + B with E = 1/3·I - H + (|z|²I - z⊗z)/4 and B involving ∇z force H ≥ 0? (2) What is the relationship between the calibrated eigenvalues of E+B and the sign of H eigenvalues? (3) Can a counterexample with calibrated W+ but H having a negative eigenvalue exist? Consider the constraints from the trace mode tr(H) = 1 + |z|²/2 ≥ 1 and the chiral Riccati. Provide a rigorous mathematical assessment of whether H ≥ 0 is forced or can be violated on the calibrated bulk.

## Output

### Algebraic relation between \(H\) and the two chiral Weyl blocks

Write
\[
Q=W^+,\qquad S=W^-,
\qquad
T(z)=\frac14\bigl(|z|^2I-z\otimes z\bigr)\ge 0,
\]
and denote the magnetic Weyl tensor involving \(\nabla z\) by \(\mathsf B\). Since
\[
Q=E+\mathsf B,\qquad S=E-\mathsf B,
\qquad
E=\frac13I-H+T(z),
\]
one has the exact identities
\[
\boxed{
H=\frac13I+T(z)-\frac12(Q+S)
}
\]
and equivalently
\[
\boxed{
H=\frac13I+T(z)+\mathsf B-Q,\qquad
\mathsf B=\frac12(Q-S).
}
\]

Thus calibration of \(W^+\) fixes only one summand. It leaves the anti-self-dual block \(W^-\), or equivalently the derivative-twist tensor \(\mathsf B\), undetermined.

The trace relation follows automatically:
\[
\operatorname{tr}H
=1+\operatorname{tr}T
=1+\frac{|z|^2}{2}.
\]
It controls the sum of the three eigenvalues and gives no individual sign information.

### Sharp pointwise implication

Let \(X\) be unit length. Then
\[
H(X,X)
=
\frac13+\frac14\left(|z|^2-\langle z,X\rangle^2\right)
-\frac12\left(Q(X,X)+S(X,X)\right).
\]
For the calibrated spectrum
\[
\operatorname{Spec}(Q)=
\left\{-\frac16,\frac1{12},\frac1{12}\right\},
\]
one has \(Q(X,X)\le 1/12\). Consequently,
\[
H(X,X)\ge
\frac7{24}-\frac12\lambda_{\max}(S).
\]
In particular,
\[
\boxed{\lambda_{\max}(W^-)\le\frac7{12}\quad\Longrightarrow\quad H\ge0.}
\]

Conversely, if
\[
\lambda_{\min}(H)\le-\eta,\qquad \eta\ge0,
\]
then in a corresponding unit direction \(X\),
\[
S(X,X)
\ge
\frac7{12}+2\eta
+\frac12\left(|z|^2-\langle z,X\rangle^2\right),
\]
hence
\[
\boxed{
\lambda_{\max}(W^-)\ge\frac7{12}+2\eta.
}
\]
Since a trace-free symmetric \(3\times3\) matrix with largest eigenvalue \(m\) satisfies
\[
|S|^2\ge\frac32m^2,
\]
this gives
\[
\boxed{
|W^-|^2\ge
\frac32\left(\frac7{12}+2\eta\right)^2.
}
\]
For arbitrarily small \(\eta>0\), the threshold tends to
\[
\frac{49}{96}.
\]

The same mechanism is especially transparent in terms of derivative twist:
\[
H(X,X)=\frac13+T(X,X)-Q(X,X)+\mathsf B(X,X).
\]
Therefore
\[
H(X,X)\le-\eta
\quad\Longrightarrow\quad
\mathsf B(X,X)\le-\frac14-\eta.
\]
The twist amplitude \(z\) contributes only through the positive-semidefinite tensor \(T(z)\); it cannot create an eigenvalue below zero. Such an eigenvalue must come from the \(\nabla z\) component contained in \(\mathsf B\).

If the calibrated spectrum holds only up to operator error \(\delta\), the estimate becomes
\[
\lambda_{\min}(H)\le-\eta
\quad\Longrightarrow\quad
\lambda_{\max}(W^-)
\ge\frac7{12}+2\eta-\delta-O(\|\operatorname{Ric}+g\|).
\]

### Explicit pointwise countermodel

The constants above are sharp. Work at a regular point \(p\), choose an orthonormal frame, and set
\[
Q=\operatorname{diag}\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
For \(\varepsilon>0\), let
\[
m=\frac7{12}+2\varepsilon,\qquad
S=\operatorname{diag}\left(-\frac m2,m,-\frac m2\right),
\qquad z(p)=0.
\]
Define
\[
H=\frac13I-\frac12(Q+S).
\]
A direct computation gives
\[
\boxed{
H=
\operatorname{diag}\left(
\frac9{16}+\frac{\varepsilon}{2},
-\varepsilon,
\frac7{16}+\frac{\varepsilon}{2}
\right).
}
\]
Thus
\[
\operatorname{tr}H=1,
\]
exactly as required by the vertical equation at \(z=0\), but \(H\) is not positive semidefinite.

The corresponding magnetic tensor is
\[
\mathsf B=\frac12(Q-S)
=
\operatorname{diag}\left(
\frac1{16}+\frac{\varepsilon}{2},
-\frac14-\varepsilon,
\frac3{16}+\frac{\varepsilon}{2}
\right).
\]
It satisfies
\[
Q=\frac13I-H+\mathsf B,\qquad
S=\frac13I-H-\mathsf B.
\]

This algebraic model is compatible with all first-order reduced constraints at \(p\). Set
\[
u(p)=z(p)=0,\qquad \nabla u(p)=H,
\]
and, in the convention from the supplied reduction,
\[
\nabla z(p)=2\mathsf B.
\]
Because \(\mathsf B\) is symmetric and trace-free,
\[
dz(p)=0,\qquad \operatorname{div}z(p)=0.
\]
These are precisely the closure and mixed equations at \(z=u=0\).

Moreover,
\[
a_\pm(p)=0,
\]
and
\[
\nabla a_+=H-\mathsf B=\frac13I-Q,\qquad
\nabla a_-=H+\mathsf B=\frac13I-S.
\]
Hence
\[
-[\operatorname{sym}\nabla a_+]_0=Q,\qquad
-[\operatorname{sym}\nabla a_-]_0=S.
\]
Both Maurer–Cartan equations hold at \(p\): their right-hand sides vanish because \(a_\pm(p)=0\), while the antisymmetric parts of \(\nabla a_\pm\) vanish.

This is realizable by an actual smooth Kaluza–Klein metric jet:

* choose
  \[
  v(x)=1+\frac12H_{ij}x^ix^j+O(|x|^3);
  \]
* choose \(z_i(x)=2\mathsf B_{ij}x^j+O(|x|^2)\);
* since the linear part of \(z\) is symmetric and trace-free, the corresponding first jet of \(F=*z\) is closed and satisfies the mixed equation;
* prescribe
  \[
  \operatorname{Ric}_B(p)=-I+H,
  \]
  which is an arbitrary admissible three-dimensional metric \(2\)-jet.

The lifted metric then has
\[
\operatorname{Ric}_g(p)=-g(p),\qquad
W^+(p)=Q,
\]
while one eigenvalue of \(H(p)\) equals \(-\varepsilon\). By continuity, a sufficiently small neighborhood has arbitrarily small Einstein and calibration residuals while retaining an \(H\)-eigenvalue below zero.

### Why the chiral Riccati system does not restore semipositivity

At \(u=z=0\), the calibration equation determines
\[
\nabla a_+=\frac13I-Q
=\operatorname{diag}\left(\frac12,\frac14,\frac14\right),
\]
which is indeed positive definite. But
\[
H=\frac12\bigl(\nabla a_++\nabla a_-\bigr)
\]
at that point. The symmetric trace-free part of \(\nabla a_-\), equivalently \(W^-\), remains free. The Maurer–Cartan relations determine antisymmetric derivatives; they do not constrain these five symmetric trace-free components. The trace identities fix only \(\operatorname{tr}\nabla a_\pm\). This leaves exactly the freedom used in the matrix construction above.

### Interpretation on calibrated bulk

For
\[
A_\eta=\left\{x:\lambda_{\min}(H(x))\le-\eta
\text{ and }W^+(x)\text{ is calibrated}\right\},
\]
the pointwise estimate gives
\[
\int_{A_\eta}|W^-|^2
\ge
\frac32\left(\frac7{12}+2\eta\right)^2
\operatorname{Vol}(A_\eta).
\]
Thus an \(H\)-eigenvalue below zero has a definite anti-chiral curvature cost. A merely bounded mean of \(|W^-|^2\) does not make \(\operatorname{Vol}(A_\eta)\) vanish; the threshold \(49/96\) is fully compatible with the \(O(1)\) curvature means considered in the collapse argument. Semipositivity would follow from a pointwise upper bound
\[
W^-\le\frac7{12}I,
\]
or from anti-chiral energy below the corresponding threshold, but neither follows from calibration of \(W^+\).

An exact Einstein metric cannot carry the calibrated constant \(W^+\) spectrum throughout an open set: the supplied Derdziński argument produces the incompatible local Kähler spectrum. That excludes the whole exact regular germ, rather than proving \(H\ge0\) inside it. In the collapsing near-Einstein setting, the pointwise derivative-twist freedom remains until fixed-scale regularity makes that open-germ argument accessible.

Finally, even \(\operatorname{Ric}_B\ge-I\) supplies only relative Bishop–Gromov comparison. An absolute base-ball volume lower bound also requires volume at a larger scale or quantitative exclusion of further base collapse; flat \(\mathbb R^2\times S^1_\varepsilon\) already shows that a Ricci lower bound alone does not provide this.

**Conclusion:** the calibrated \(W^+\) spectrum and the trace/chiral equations do not force \(H\ge0\). They yield instead a sharp dichotomy: every direction with \(H<0\) requires an order-one derivative-twist component, equivalently \(\lambda_{\max}(W^-)>7/12\). The explicit Kaluza–Klein jet above realizes this mechanism while satisfying the reduced equations at the calibrated point.