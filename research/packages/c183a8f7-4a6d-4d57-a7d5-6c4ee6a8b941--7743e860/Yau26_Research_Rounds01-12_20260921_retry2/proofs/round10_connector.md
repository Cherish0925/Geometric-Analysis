# Charge transport and forced geometric escape for near-Einstein connectors

21 September 2026.

## 1. Main result

The exact obstruction in `round9_connector.md` does not itself give a
positive uniform Ricci-defect gap. The result here identifies two specific
escapes required by a small-error continuation of a fixed charged core.
Charge is not assumed conserved. Its actual variation is bounded using
the mixed Ricci equation.

Let \(g\) be a complete smooth metric on \((0,1)\times T^3\), with two
smooth conformally compact AH ends and a free marked isometric \(T^2\)
action extending freely to the compactification. On the annular quotient
\(B\), write
\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
\rho=\sqrt{\det G},\quad dA^a=f^a\,d\mu_\gamma,
\quad q=\rho Gf.
\tag{1.1}
\]
Fix \(2\pi\)-periodic marked torus coordinates and an orientation of
\(B\). Put
\[
E=\operatorname{Ric}_g+3g,\qquad
\|g^{-1}E\|_{\infty,\mathrm{op}}\le\epsilon.
\tag{1.2}
\]
For a primitive lattice vector \(v\in\mathbb Z^2\), define
\[
V_v^2=v^{\mathsf T}Gv,\qquad q_v=v^{\mathsf T}q,
\qquad a_v=\rho V_v,
\qquad d_v=d_{a_v^2\gamma}.
\tag{1.3}
\]
The circle direction \(v\) and its period are fixed geometric data,
not parameters rescaled separately for each estimate.

**Theorem 1.** For each \(v\), there is a smooth essential loop
\(c_v\subset B\) whose lift is a fully stable minimal two-torus in the
quotient by the \(v\)-circle. It satisfies
\[
\boxed{|dq_v|_\gamma\le2\epsilon a_v,\qquad
\int_{c_v}\frac{q_v^2}{a_v}\,ds_\gamma
\le4\epsilon\int_{c_v}a_v\,ds_\gamma.}
\tag{1.4}
\]
In particular, fix a point \(p_0\in B\) with
\(|q_v(p_0)|\ge q_*>0\). At least one of the following occurs:

1. Some \(p\in c_v\) has \(|q_v(p)|\le q_*/2\). Every path from
   \(p_0\) to this point has \(a_v^2\gamma\)-length at least
   \(q_*/(4\epsilon)\).
2. The separator has the orbit-scale bound
   \[
   \boxed{
   \frac{\int_{c_v}a_v\,ds_\gamma}
        {\int_{c_v}a_v^{-1}\,ds_\gamma}
   \ge\frac{q_*^2}{16\epsilon}.}
   \tag{1.5}
   \]

Thus fixed nonzero core charge cannot be continued with vanishing error
while keeping both charge-transport distance and separator orbit scale
bounded. This statement permits arbitrary rotating shape and connection
curvature. It requires neither derivative bounds on \(E\) nor a conserved
approximate charge.

## 2. The exact mixed equation with error

Let \(H_i\) be horizontal lifts and \(K_a=\partial_{\xi^a}\). The
abelian submersion Ricci formula is
\[
\operatorname{Ric}_g(H_i,K_a)
=\frac1{2\rho}\nabla^j\bigl(\rho G_{ab}F^b_{ij}\bigr),
\qquad F^b=f^b d\mu_\gamma.
\tag{2.1}
\]
Since \(\nabla d\mu_\gamma=0\), the right side is the oriented rotation
of \(dq_a/(2\rho)\). For example in oriented conformal coordinates
\(\gamma=b^2(dx^2+dy^2)\),
\[
E(H_x,K_a)=\frac{\partial_yq_a}{2\rho},\qquad
E(H_y,K_a)=-\frac{\partial_xq_a}{2\rho}.
\tag{2.2}
\]
The cosmological term has no mixed block. The full operator error bound
therefore yields
\[
|dq(X)|_{G^{-1}}\le2\epsilon\rho|X|_\gamma,
\quad |dq_v(X)|\le2\epsilon\rho V_v|X|_\gamma.
\tag{2.3}
\]
Integrating along paths gives
\[
|q_v(p)-q_v(p_0)|\le2\epsilon d_v(p,p_0).
\tag{2.4}
\]
This exact formula replaces the false assumption \(dq=0\) for a metric
that merely has small mixed Ricci error.

## 3. A stable separator in the circle quotient

Extend \(v\) to an oriented unimodular lattice basis, writing it as the
first generator. Define
\[
V^2=G_{11},\qquad W=\rho/V,\qquad s=G_{12}/G_{11}.
\]
Then the circle quotient metric and connection are
\[
h=\gamma+W^2(d\xi^2+A^2)^2,
\qquad\alpha=A^1+s(d\xi^2+A^2),
\qquad g=V^2(d\xi^1+\alpha)^2+h.
\tag{3.1}
\]
A shortest essential loop for \(W^2\gamma\) exists in \(B\). Indeed at
either AH end, \(W\) is comparable to \(x^{-1}\), and \(\gamma\) to
\(x^{-2}(dx^2+d\theta^2)\). Bounded-length essential loops cannot escape
or make excursions arbitrarily far into the ends. Minimization on a
compact annulus then gives a smooth embedded shortest loop \(c_v\).
Its lift \(\Sigma\) in \((N,h)\) is a minimal two-torus, with
\[
dA_\Sigma=W\,ds_\gamma\,d\xi^2.
\tag{3.2}
\]
It is stable for all normal variations. It is minimizing under invariant
variations by construction. The lowest Jacobi eigenfunction on a compact
connected hypersurface is positive and unique up to normalization; the
residual isometric circle preserves it, so it is invariant. Thus the
lowest full eigenvalue equals the lowest invariant eigenvalue.

The general circle-reduction formulas can be read from Hwang, *A note
on the circle actions on Einstein manifolds*, Lemma 1
([primary source](https://doi.org/10.1017/S0004972700019134)). Applying
them with the error \(E\), as in `round9_riemannian.md`, gives
\[
J_\Sigma V=-V\left(
|\mathrm{II}|^2+\frac{V^2}{4}|F|_{\rm tens}^2
+\frac{V^2}{2}|\iota_nF|^2+E(n,n)-E(U,U)\right),
\tag{3.3}
\]
where \(F=d\alpha\), \(U=V^{-1}\partial_{\xi^1}\), \(n\) is the
quotient unit normal lifted horizontally, and
\(|F|_{\rm tens}^2=F_{ij}F^{ij}\). Stability with test function \(V\)
implies
\[
\int_\Sigma V^2\left(|\mathrm{II}|^2
+\frac{V^2}{4}|F|_{\rm tens}^2
+\frac{V^2}{2}|\iota_nF|^2\right)
\le2\epsilon\int_\Sigma V^2.
\tag{3.4}
\]

The horizontal part of the actual circle curvature is
\[
F=(f^1+s f^2)d\mu_\gamma
+ds\wedge(d\xi^2+A^2),\qquad
f^1+s f^2=\frac{q_v}{\rho V^2}.
\tag{3.5}
\]
Therefore \(|F|_{\rm tens}^2\ge2q_v^2/(\rho^2V^4)\).
Keeping just this nonnegative term in (3.4), and using (3.2), gives
\[
\frac12\int_{c_v}\frac{q_v^2}{\rho V}\,ds_\gamma
\le2\epsilon\int_{c_v}\rho V\,ds_\gamma.
\tag{3.6}
\]
The \(2\pi\) residual circle period cancels. This proves (1.4).

For the dichotomy, if \(|q_v(p)|\le q_*/2\), (2.4) gives the first
alternative. Otherwise \(|q_v|>q_*/2\) everywhere on \(c_v\), and
(3.6) gives (1.5). This completes the proof. \(\square\)

## 4. A usable conditional defect gap

Define finite constants for the actual separator
\[
A=\max_{c_v}a_v,\qquad
D=\max_{p\in c_v}d_v(p_0,p).
\]
Equation (1.4) guarantees at least one point of \(c_v\) with
\(|q_v|/a_v\le2\sqrt\epsilon\). At that point, (2.4) yields
\[
q_*\le2\epsilon D+2A\sqrt\epsilon.
\tag{4.1}
\]
Consequently,
\[
\boxed{
\epsilon\ge
\frac{q_*^2}{\bigl(A+\sqrt{A^2+2Dq_*}\bigr)^2}.}
\tag{4.2}
\]
This is a uniform positive gap on a family with fixed positive seed
charge and common bounds on \(A,D\). It is not dimension-only: both
bounds describe actual geometry that can degenerate. It also does not
force every candidate to retain a charged seed; a sequence with core
charge tending to zero lies outside that hypothesis.

The transport scale is realized by an existing **one-ended** family,
which prevents strengthening (2.4) merely by ignoring large orbit factors.
In `round6_global.md`, the variable-mass metric has
\[
V_R(r)=r^2-m_R(r)/r,\quad
D_R=r^2+c^2V_R,\quad \rho=r\sqrt{D_R},
\quad V_v=\sqrt{D_R},\quad q_v=c(3m_R-rm_R'),
\]
where \(m_R(r)=\chi(r/R)\) decreases from one to zero on \([R,2R]\).
Its full Ricci error is \(O(R^{-3})\), while \(q_v\) changes from
\(3c\) to zero. The radial weighted transport length is
\[
\int_R^{2R}a_v\,ds_\gamma
=\int_R^{2R}\frac{rD_R}{\sqrt{V_R}}\,dr
\sim\frac73(1+c^2)R^3.
\tag{4.3}
\]
Thus the inverse-error order in charge transport is compatible with a
genuine full-metric construction. This family has disk quotient and one
AH end: it is not a two-ended connector or a counterexample to Theorem 1.

## 5. Quantized circle curvature gives an independent escape condition

There is a second constraint that does not require a marked nonzero
torus charge. Suppose a free \(2\pi\)-periodic circle metric
\(g=V^2\eta^2+h\) with the same Ricci error bound admits a compact
oriented two-sided stable quotient separator \(\Sigma\). Its restricted
circle bundle has Chern number
\[
m=\frac1{2\pi}\int_\Sigma F\in\mathbb Z.
\tag{5.1}
\]
The estimate (3.4) and Cauchy--Schwarz imply
\[
2\epsilon\int_\Sigma V^2
\ge\frac12\int_\Sigma V^4(F|_{T\Sigma})^2
\ge\frac{2\pi^2m^2}{\int_\Sigma V^{-4}}.
\]
Hence, if \(m\ne0\),
\[
\boxed{\epsilon\ge
\frac{\pi^2m^2}
{\left(\int_\Sigma V^2\right)
 \left(\int_\Sigma V^{-4}\right)}.}
\tag{5.2}
\]
Here \(F|_{T\Sigma}\) means its scalar coefficient in the oriented
surface area form. The inequality uses
\(|F|_{\rm tens}^2\ge2(F|_{T\Sigma})^2\).
For example, if \(0<v_0\le V\le v_1\) on \(\Sigma\) and
\(\operatorname{Area}\Sigma\le S\), then
\(\epsilon\ge\pi^2m^2v_0^4/(v_1^2S^2)\).
Thus topologically nonzero circle curvature requires weighted area
escape or lapse degeneration as the defect vanishes. Unlike the variable
\(q_v\), this integral is genuinely topological and cannot leak under a
small mixed Ricci error.

This Chern-number estimate does not automatically apply with \(m\ne0\)
to the marked \(T^2\)-annulus: its circle bundles are trivial and that
Chern number is zero. It is an additional obstruction for different
circle-bundle topologies, not a relabeling of torus charge.

The [surface-cusp doubling construction](round10_cusp_doubling.md)
realizes this allowed degeneration on a fixed nontrivial circle bundle.
At its stable central separator, \(V=d\) and the quotient area is fixed.
The denominator in (5.2) grows as \(d^{-2}\), whereas the actual twist
contribution to the Ricci error is \(O(d^2)\). Thus nonzero Chern number
alone does not turn (5.2) into a uniform near-Einstein gap.

## 6. What has changed

The small-error problem now has quantitative alternatives that can be
tested on an actual proposed continuation. A fixed charged seed requires
large weighted transport distance or large separator orbit scale;
nonzero quantized circle curvature requires a divergent weighted area
product. These complement the optical-geodesic constraint in
`round10_optical.md`. None follows from a formal persistence of exact
charge conservation.

A fixed closed-topology volume upper bound alone does not bound the
weighted path distance or the circle lapse on a separator. Controlling
their simultaneous escape requires an additional geometric estimate;
it is not supplied by Chern--Gauss--Bonnet or (1.4) alone.

`round10_connector_check.py` reconstructs Ricci from the coordinate
metric for two nonconstant, nondiagonal torus examples. It checks the
mixed equation, its full norm, the circle curvature component and the
conditional-gap algebra. Six exact checks pass. No complete connector
or continuous-region numerical certificate is asserted by those checks.
