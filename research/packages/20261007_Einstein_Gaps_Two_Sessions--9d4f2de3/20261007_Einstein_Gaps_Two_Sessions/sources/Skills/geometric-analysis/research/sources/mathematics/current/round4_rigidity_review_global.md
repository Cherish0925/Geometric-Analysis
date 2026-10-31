# Independent review of the integral closure and scale-invariant gap

20 September 2026. This bounded review checked Sections 6--8 of
`round4_rigidity.md`, the required weight and approximation estimates in
its earlier sections, and Section 8 of `round3_monopole_input.md`.
No blocking mathematical issue was found in the stated integral theorem
or its topology and scaling consequences. The author's exact checker was
also rerun successfully. This review did not edit the author's proof.

## 1. Intrinsic Hessian, Bianchi and Hodge closure

The Ricci term in the exact bundle Hessian identity can be estimated by
`||Ric||_2 ||nabla u||_4^2`. Thus both it and the bundle-curvature term
are linear in the Hessian norm after using the intrinsic interpolation
`||nabla u||_4^2<=4||u||_infinity ||nabla^2u||_2`. Absorbing their sum
gives exactly the coefficients `32` and `33` in equation (5). No
pointwise Ricci lower bound is hidden in that step.

The modified weight bounds `rho=|Phi|^2` by four. This is enough to
check the two key estimates directly:

\[
 |\nabla_A^*\nabla_A\Phi|^2
 =\frac{\rho}{16}(s+f\rho)^2
 \le\frac12s^2+8f^2,
\]

\[
 \int|F_A|^2=2\int|F_A^+|^2-4\pi^2a^2
 \le4\int f^2+4\pi^2(-a^2)_+.
\]

The positive-spin curvature projection contains W-plus, scalar curvature,
trace-free Ricci, and determinant curvature, but no W-minus term. Their
L2 estimates therefore suffice for (20)--(21). A uniform bound on
`integral f^4` or on scalar curvature is not needed. The polynomial
second derivative of `A_psi` uses precisely `nabla_A^2 Phi` in L2 and
`nabla_A Phi` in L4, together with bounded `Phi`.

The Bianchi identity and the operator-to-four-tensor identification are
covariant and parallel. Hence testing the divergence estimate against
`T=J_psi` only needs `||nabla J_psi||_2<=C||nabla^2 A_psi||_2`, which
has just been established. The factors in (22) divide by volume without
leaving a hidden extra power of volume.

The imported weighted Hodge identity has the correct coefficients
`-1/64,1/16,-5/96,1/8`. At `s=-4,rho=sqrt(2),R=0`, the zeroth-order
term equals `1/16`. For the integral extension, its scalar error is
bounded by a constant times `average |s+4|`, using bounded `rho`;
Cauchy--Schwarz makes this `O(sqrt(kappa))`. The bounded-amplitude
polynomial errors and the Weyl remainder have the same strength. The
derivative errors are `O(kappa)` from the two actual monopole defects.
This verifies (23) without a pointwise scalar hypothesis or a
uniform-integrability assumption on the unweighted gradient energy.

The preceding weight construction accounts for the difference between
the actual curvature moment and the ideal moment; it does not incorrectly
apply harmonic projection directly to the ideal moment. Its scalar cost
is `81/4+9=117/4`, as stated. Smooth-majorant errors can be made
arbitrarily small on each fixed compact metric while the spinor remains
bounded independently of the approximation. This is sufficient for the
final pointwise-in-metric theorem.

## 2. Unrestricted scalar signs and topological transfer

Set `f_alg=2s/3-2alpha`, `b=2s/3+2w`. The inequality `b>=f_alg`
implies `G=f_alg^2-b_-^2>=0` in both cases: if `b<0`, then
`f_alg<=b<0`; if `b>=0`, then `b_-^2=0`. Thus the positive-part
version works without a scalar sign condition.

The completed-square identity and the signed monopole inequality imply

\[
 \int(t^2+18G)\le108P+864\pi^2A d_T.
\]

Writing `Q_E=integral |Ric+g|^2` and `Z=integral(s+4)^2`, the exact
relation `Q_E=P+Z/4` gives

\[
 Q_E+Z+108P=5Q_E+104P\le109Q_E.
\]

This proves equation (26) for unrestricted metrics. It must retain the
term `864pi^2 A d_T`; the bound `integral Phi_*<=109Q_E` alone applies
only when `d_T=0`.

The global orbit-distance bound also checks out. When `s<=-3`,
`G>=8z`, giving the first displayed estimate in the proof. When `s>-3`,
`e>1`, and the two elementary inequalities used there give

\[
 F\le\frac{t^2+e^2}{192}
             +\frac{t^2+7e^2}{96}
       =\frac{t^2+5e^2}{64}.
\]

Thus `F<=e^2+t^2+G` holds globally, including scalar-positive regions.
Because `q_+^2<=q^2`, the completed square gives the claimed upper bound
for `Delta_+`. Consequently

\[
 \kappa\le\frac{245}{2}r+972\pi^2(A/V)d_T.
\]

The scalar monopole estimate gives
`32pi^2 A<=32V+8rV`, so `A/V<=(4+r)/(4pi^2)` with no pointwise bound.
For `r<=1`, the coefficient of `d_T` is at most `972*5/4=1215`,
which also dominates `245/2`. The determinant square factor is at most
`5 C_A/(4pi^2)`, proving the stated family constant.

For the alternative hypothesis `a^2>=T-C_A A`, equation (30) is valid:
the reverse triangle inequality for `s=-4+e`, and `||e||_2<=2sqrt(rV)`,
give its displayed lower bound. It is at least `V/4` for `r<=1/4`.
This supplies `T>0` in the only regime requiring the class-square
estimate. The complementary regime contributes the `1/4` branch of
the final constant. Actual class existence and the selected positive
projection remain necessary inputs.

## 3. Scaling and optimization

For `h=lambda g` in dimension four, the Ricci tensor as a covariant
two-tensor is unchanged, its squared norm acquires `lambda^-2`, and
volume acquires `lambda^2`. Hence

\[
 \fint_h|\operatorname{Ric}_h+h|_h^2
 =\frac{\int_g|\operatorname{Ric}_g+\lambda g|_g^2}
                                  {\lambda^2 V_g}.
\]

Middle-dimensional Hodge projection and the class square are unchanged.
The metricwise theorem can therefore be applied at every positive
scale before taking the infimum; no convergence of minimizing metrics
or classes is needed.

The scalar optimization is of
`R2/(V lambda^2)+2S/(V lambda)+4`. If `S<0`, its unique minimum occurs
at `lambda=-R2/S`; if `S>=0`, the infimum is four. The identity

\[
 4R_2-S^2/V
 =4\int|\operatorname{Ric}^{\circ}|^2
                  +\int(s-\overline s)^2
\]

verifies equation (33). The denominator is nonzero when `S<0`, so no
zero-energy division is hidden in that formula.

One precision to preserve in the synthesis: families using the
alternative square condition must carry the `1/4` branch from Section 7
when naming their universal constant, rather than automatically copying
the `1` branch in equation (25). The current final scale-energy statement
uses an unspecified positive constant and is consistent with this.

The resulting obstruction is an integral Ricci-energy gap for the
stated actual monopole families. It uses no bound on `chi/A`, no
pointwise Ricci or scalar control, and no opposite-chirality curvature
control. It does not become an arbitrary-topology Einstein-existence
theorem.
