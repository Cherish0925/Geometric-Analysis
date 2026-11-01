# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 13,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step13_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step13_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

For the four-dimensional negative-branch near-Einstein circle collapse problem, consider a rank-one Kaluza-Klein metric g = g_B + ℓ²(dψ+A)² with Ric ≈ -g on a closed 4-manifold. The normalized cover g = g_B + v²(dz+B)² with v(p)=1 removes the fiber period from local coefficients. The reduced Einstein equations are: (V) Δv/v = 1 + v²|F_B|²/2, (M) div(v²F_B) ≈ 0, (H) Ric_B = -I + Hess(v)/v + (v²/2)F_B⊗F_B. The chiral variables a± = u ∓ z/2 (where u=d log v, z=*(vF_B)) satisfy W± = -[sym∇a± + a±⊗a±]₀ and da+ = a+∧a-. The calibrated W+ spectrum is (-1/6, 1/12, 1/12). The key analytical question: on the calibrated bulk where the W+ defect vanishes, does the chiral constraint force the Hessian tensor H = Hess(v)/v to have nonnegative eigenvalues? If H ≥ 0, then Ric_B ≥ -I (since the twist contribution is nonneg), giving a 3D Bishop-Gromov volume lower bound and 4D cover noncollapse. Investigate: (1) Can the calibrated W+ = E + B with E = 1/3·I - H + (|z|²I - z⊗z)/4 and B involving ∇z force H ≥ 0? (2) What is the relationship between the calibrated eigenvalues of E+B and the sign of H eigenvalues? (3) Can a counterexample with calibrated W+ but H having a negative eigenvalue exist? Consider the constraints from the trace mode tr(H) = 1 + |z|²/2 ≥ 1 and the chiral Riccati. Provide a rigorous mathematical assessment of whether H ≥ 0 is forced or can be violated on the calibrated bulk.

## Integrated Scientific Memo

## Rigorous assessment

Let
\[
Q:=W^+,\qquad S:=W^-,
\qquad
T(z):=\frac14\bigl(|z|^2I-z\otimes z\bigr)\ge0.
\]
Since
\[
Q=E+B,\qquad S=E-B,\qquad
E=\frac13I-H+T(z),
\]
one obtains the exact pointwise identity
\[
\boxed{H=\frac13I+T(z)-\frac12(Q+S)}
\]
or, equivalently,
\[
\boxed{H=\frac13I+T(z)+B-Q,\qquad B=\frac12(Q-S).}
\]

This identity resolves the sign question: calibration fixes \(Q=W^+\), but leaves \(S=W^-\), equivalently the derivative-twist tensor \(B\), uncontrolled. Therefore calibrated \(W^+\) alone does **not** force \(H\ge0\).

### 1. Trace information is insufficient

Because \(Q,S\) are trace-free and
\[
\operatorname{tr}T(z)=\frac{|z|^2}{2},
\]
the identity reproduces
\[
\operatorname{tr}H=1+\frac{|z|^2}{2}\ge1.
\]
This controls only the sum of the three eigenvalues. It is compatible with one negative eigenvalue and two larger positive eigenvalues.

The algebraic twist term \(T(z)\) is positive semidefinite, so twist amplitude itself cannot create negativity. Any negative direction of \(H\) must arise through the derivative-twist term \(B\), equivalently through sufficiently large \(W^-\).

## 2. Sharp relation to the anti-self-dual block

For every unit vector \(X\),
\[
H(X,X)=
\frac13+\frac14\bigl(|z|^2-\langle z,X\rangle^2\bigr)
-\frac12\bigl(Q(X,X)+S(X,X)\bigr).
\]
On the calibrated locus,
\[
\operatorname{Spec}(Q)=
\left\{-\frac16,\frac1{12},\frac1{12}\right\},
\qquad Q(X,X)\le\frac1{12}.
\]
Hence
\[
H(X,X)\ge \frac7{24}-\frac12\lambda_{\max}(S),
\]
and therefore
\[
\boxed{\lambda_{\max}(W^-)\le\frac7{12}\quad\Longrightarrow\quad H\ge0.}
\]
A slightly stronger sufficient condition is
\(\|W^-\|_{\mathrm{op}}\le7/12\), but only the upper eigenvalue is relevant.

Conversely, if \(H(X,X)\le-\eta\), then
\[
S(X,X)\ge
\frac7{12}+2\eta+
\frac12\bigl(|z|^2-\langle z,X\rangle^2\bigr),
\]
so
\[
\boxed{\lambda_{\max}(W^-)\ge\frac7{12}+2\eta.}
\]
Since a trace-free symmetric \(3\times3\) matrix with largest eigenvalue \(m\)
satisfies \(|S|^2\ge\frac32m^2\),
\[
\boxed{|W^-|^2\ge
\frac32\left(\frac7{12}+2\eta\right)^2.}
\]
Thus even an arbitrarily small negative eigenvalue has the definite limiting anti-chiral energy cost
\[
|W^-|^2\ge \frac{49}{96}+o(1).
\]

In terms of \(B\), using \(H=\frac13I+T+B-Q\),
\[
H(X,X)\le-\eta
\quad\Longrightarrow\quad
B(X,X)\le
-\frac13-\eta-T(X,X)+Q(X,X)
\le-\frac14-\eta.
\]
Negativity is therefore precisely an order-one derivative-twist phenomenon.

For a calibration error bounded in operator norm by \(\delta\), and a reduced Einstein error \(r\), these estimates acquire the corresponding \(O(\delta+|r|)\) corrections.

## 3. Explicit calibrated pointwise counterexample

Choose an orthonormal frame and set
\[
Q=\operatorname{diag}\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
For \(\varepsilon>0\), put
\[
m=\frac7{12}+2\varepsilon,\qquad
S=\operatorname{diag}\left(-\frac m2,m,-\frac m2\right),
\qquad z=0.
\]
Then define
\[
H=\frac13I-\frac12(Q+S).
\]
A direct calculation gives
\[
\boxed{
H=\operatorname{diag}\left(
\frac9{16}+\frac{\varepsilon}{2},
-\varepsilon,
\frac7{16}+\frac{\varepsilon}{2}
\right).
}
\]
Thus
\[
\operatorname{tr}H=1
\]
as required by the vertical equation at \(z=0\), while \(H\) has the negative eigenvalue \(-\varepsilon\).

The required magnetic tensor is
\[
B=\frac12(Q-S)
=
\operatorname{diag}\left(
\frac1{16}+\frac{\varepsilon}{2},
-\frac14-\varepsilon,
\frac3{16}+\frac{\varepsilon}{2}
\right).
\]
It is symmetric and trace-free and satisfies
\[
Q=\frac13I-H+B,\qquad
S=\frac13I-H-B.
\]

This is compatible with all reduced equations to first order at the point. Set
\[
u(p)=z(p)=0,\qquad \nabla u(p)=H,\qquad \nabla z(p)=2B.
\]
Because \(B\) is symmetric and trace-free,
\[
dz(p)=0,\qquad \operatorname{div}z(p)=0,
\]
which are exactly the mixed/closure constraints at \(u=z=0\).

Moreover \(a_\pm(p)=0\), and
\[
\nabla a_+=H-B=\frac13I-Q,\qquad
\nabla a_-=H+B=\frac13I-S.
\]
Consequently,
\[
-[\operatorname{sym}\nabla a_+]_0=Q,\qquad
-[\operatorname{sym}\nabla a_-]_0=S,
\]
while both Maurer–Cartan equations hold at \(p\): their right sides vanish and the antisymmetric derivative parts vanish.

A smooth Kaluza–Klein jet can be constructed by taking
\[
v(x)=1+\frac12H_{ij}x^ix^j+O(|x|^3),\qquad
z_i(x)=2B_{ij}x^j+O(|x|^2),
\]
choosing \(F=*z\) to the required order, and prescribing the base metric jet so that
\[
\operatorname{Ric}_B(p)=-I+H.
\]
The resulting lifted metric satisfies at \(p\)
\[
\operatorname{Ric}_g=-g,\qquad W^+=Q,
\]
but \(H\ngeq0\). By continuity, on a sufficiently small neighborhood the Einstein and calibration residuals can be made arbitrarily small while \(H\) remains negative somewhere.

This establishes a genuine local near-Einstein countermodel to the proposed implication. It is not, by itself, an exact Einstein solution with calibrated \(W^+\) on an open set.

## 4. Why the chiral Riccati equation does not repair the implication

At \(u=z=0\), calibration determines
\[
\nabla a_+=\frac13I-Q
=\operatorname{diag}\left(\frac12,\frac14,\frac14\right),
\]
but
\[
H=\frac12(\nabla a_++\nabla a_-).
\]
The symmetric trace-free part of \(\nabla a_-\), equivalently \(W^-\), remains free. The Maurer–Cartan relations
\[
da_+=a_+\wedge a_-,
\qquad
da_-=-a_+\wedge a_-
\]
constrain antisymmetric derivatives, not these five symmetric trace-free components. The trace equations likewise fix only scalar modes. Hence neither the Riccati factorization nor the trace mode enforces semipositivity.

The static case is special: \(z=0\) throughout implies \(B=0\), hence \(W^-=W^+\), and
\[
H=\frac13I-W^+
\]
has calibrated spectrum
\[
\left(\frac12,\frac14,\frac14\right).
\]
That conclusion does not survive derivative twisting.

## 5. Open-set rigidity versus local jets

Two statements must be kept separate.

1. **Pointwise or near-calibrated bulk:** sign-indefinite \(H\) is compatible with the reduced equations, as the explicit jet shows.
2. **Exact Einstein metric with exactly calibrated constant \(W^+\) spectrum on an open set:** the supplied Derdziński forbidden-germ argument excludes such an open germ altogether, because it would force a locally Kähler–Einstein structure whose required \(W^+\) norm is incompatible with the calibrated norm.

Thus open-set rigidity does not prove \(H\ge0\); it says the entire exact calibrated germ cannot exist. One should not infer, without an additional local existence theorem, that arbitrary compatible jets prolong to exact calibrated Einstein solutions.

## 6. Consequences for noncollapse

On
\[
A_\eta=\{x:\lambda_{\min}(H)\le-\eta,\ W^+\text{ calibrated}\},
\]
the pointwise estimate yields
\[
\int_{A_\eta}|W^-|^2
\ge
\frac32\left(\frac7{12}+2\eta\right)^2
\operatorname{Vol}(A_\eta).
\]
Therefore a sufficiently small anti-self-dual energy density would force the bad set to have small measure. A merely \(O(1)\) bound on the mean of \(|W^-|^2\), however, does not exclude it; the threshold \(49/96\) is itself order one.

The correct missing estimate is therefore control of \(W^-\) or of the derivative-twist tensor \(B\), not a direct maximum principle for \(H\). Calibration of \(W^+\) supplies no such control.

There is also a separate geometric caveat: even if \(H\ge0\), so that
\[
\operatorname{Ric}_B=-I+H+\frac12(|z|^2I-z\otimes z)\ge-I,
\]
a Ricci lower bound gives relative Bishop–Gromov comparison, not an absolute base-ball volume lower bound. Further base collapse is possible without a volume anchor or injectivity/topological-survival information. Hence \(H\ge0\) alone would not completely prove cover noncollapse.

## Conclusion

\[
\boxed{\text{Calibrated }W^+\text{ does not force }H\ge0.}
\]

The exact replacement is
\[
H=\frac13I+\frac14(|z|^2I-z\otimes z)-\frac12(W^++W^-).
\]
A negative Hessian eigenvalue is possible and is realized by a smooth compatible Kaluza–Klein jet; it necessarily costs order-one derivative twisting:
\[
\lambda_{\min}(H)\le-\eta
\ \Longrightarrow\
\lambda_{\max}(W^-)\ge\frac7{12}+2\eta,
\]
with the stronger positive twist contribution shown above. Thus the calibrated-bulk accessibility problem reduces to obtaining anti-self-dual/derivative-twist control plus an independent quantitative exclusion of further base collapse.