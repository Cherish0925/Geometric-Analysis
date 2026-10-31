# Scoped independent review: exact cores and truncated monopoles

20 September 2026. This review checks `round4_exact_core.md` and Sections
1--5 of `round4_rigidity.md`. It does not independently reprove the
round-three nonlinear existence theorem or review the later integral-gap
closure and topological applications. No error was found in the arguments
within this scope, with the hypotheses and distinctions below retained.

## 1. The exact-core obstruction

The charge convention agrees with the nonlinear construction: angular
order `(y,x)`, base orientation `dt wedge du`, and

\[
 q=vH*_hF,\qquad
 \int F=\frac{\pi^2}{2}(-b_1,B_1)=Mq.
\]

Positive definiteness of M makes nonzero transfer equivalent to nonzero
charge. No sign choice in this identity affects the contradiction, but the
displayed signs also agree with Stokes for the specified orientation.

The fixed-ball decay requirement is justified by the existing face
estimates, not merely decay along a sequence of points. Uniform equivalence
to g0 bounds the G-norms of dt and du. A fixed-radius ball centered at
`(t0,0,uj,0)` therefore has t in a fixed bounded interval and
`u=uj+O(1)`. All background-frame coefficient estimates are independent of
the angular coordinates. Consequently the stated C3 face estimate is
uniform on that whole ball and implies
`sup |nabla Rm| -> 0`, because the limiting face metric is locally the
curvature-minus-one hyperbolic product. This argument uses only three
derivatives, not a parameter neighborhood uniform in every derivative order.

If a cocompact isometry action existed, translate the centers into a compact
set and pass to a limit q. For large j, the fixed ball `B_(r/2)(q)` lies in
the translated radius-r ball. Thus the analytic tensor `nabla Rm` vanishes
on an open ball, and hence everywhere. The face curvature limit then fixes
the algebraic type of the parallel curvature tensor. Completeness and
simple connectedness identify the resulting symmetric space with
`H2(-1) x H2(-1)`.

The Killing-algebra step does not assume that the hypothetical cocompact
group preserves the given angular action. The lifted angular generators
form a two-dimensional abelian subalgebra of `sl2(R) direct-sum sl2(R)`.
Each projection has dimension at most one, since the centralizer of a
nonzero element of sl2 has dimension one. Both projections must therefore
be one-dimensional, and the subalgebra is their full direct sum. Its regular
orbits are products of one-dimensional orbits. Their orthogonal complement
is integrable, so the original mechanical connection has F=0. This
contradicts the nonzero charge.

For the second conclusion, shrink a purported local agreement to a
connected neighborhood and lift it to the two universal covers. Both covers
are complete, simply connected, and analytic Einstein manifolds. The
local-isometry extension theorem then gives a global isometry. The exact
version used is explicitly recalled in the paragraph beginning the proof
of Lemma 2.6 of [Anderson's primary
paper](https://www.math.stonybrook.edu/~anderson/dirichlet.pdf), PDF page 10.
The deck group of the closed manifold would be cocompact, giving the first
contradiction.

This proves an obstruction to unchanged exact open cores. It gives neither
a uniform lower bound for a varying gluing correction nor an obstruction to
approximate gluing, and does not exclude all Einstein metrics on E_D.

## 2. The truncated-monopole estimates through Section 5

For each fixed smooth compact metric, f0 is continuous and strictly
positive. Choose smooth hj with `|hj-f0| <= epsilon_j` uniformly and put
`fj=hj+epsilon_j`. These are positive smooth majorants converging uniformly.
The rescaled monopole hypothesis supplies a solution for each j; convergence
of the solutions is unnecessary. No derivative of fj occurs in the
displayed Weitzenbock subtraction or subsequent moment estimates.

At a positive maximum of rho, `fj rho <= -s` and
`fj >= (-s)_+/4` give `rho <= 4`, hence `u <= 6`, exactly for every j.
The two scalar-cost estimates have the required signs:

* If q<3, then s>-3 and e>1, so `Q^2-q_+^2 <= 9e^2`.
* If `f0^2>Q`, write `r=(-s)_+`. Then `r>4 sqrt(3)>6`, and
  `r <= 3(r-4)=3|e|`. Hence `f0^2-Q <= 9e^2/16`.

The actual and ideal moments are correctly distinguished. Since u squared
is at most 36,

\[
 0\le C_{\rm act}-C\le\frac{81}{4}\int e^2+o(1),\qquad
 \mathcal E_Q-C\le\Delta_++\frac{117}{4}\int e^2+o(1).
\]

Here `Cact >= 72 pi^2 p` is applied only to the actual curvature moment.
Uniform weight approximation and the amplitude bound control the o(1)
errors with the metric fixed, even though the chosen solutions vary.

The ideal moment argument closes without an integral of the fourth power
of fj. The subtraction gives `P=C-Z >= (27/8)D0`; Holder gives
`C <= EQ^(1/3) Z^(2/3)`, so `Z <= C <= EQ`. With
`theta=(Z/EQ)^(1/3)` and `H=EQ^(1/3)Z^(2/3)-C`, direct algebra gives

\[
 \mathcal E_Q-C
 =H+\frac{1+\theta}{\theta^2}(P+H)\ge2P.
\]

The positive monopole projection excludes Z=0. For the probability measure
`Q^2 dmu/EQ` and `r=u/sqrt(Q)`, one has
`E(r^3)<=E(r^2)<=1` and
`E(r^2)^2<=E(r)E(r^3)`. Thus `E(r)>=E(r^2)`, proving
`integral Q(u-sqrt(Q))^2 <= EQ-C`. These justify (14)--(15).

The orbit projection and model estimate also check. On `F<=1/256`, the
ordered-eigenvalue gap is at least `1/4-2sqrt(F)>=1/8`. The eigenvalue
defect controls the orthogonal spinor component there; on the complement,
`rho^2<=16` and `Vol<=256 integral F` give the stated 4096 coefficient.
For `r=rho^2` and `y=(I-Pi)psi`, direct rank-one algebra gives

\[
 |A_\psi-A_0|^2=\frac{(r-2)^2}{96}+\frac{|y|^2}{16}
 \le\frac{r|y|^2}{16}+\frac{(r-2)^2}{48}.
\]

For r>=1 the inequality is immediate. For 0<=r<=1 use `|y|^2<=r`:
the numerator of the difference is bounded below by
`7r^2-10r+4>0`. Combining this with (17)--(18) reproduces

\[
 \|R\|_2^2\le\frac{44}{27}S+8194\int F
                    +\frac19\int(Q-9/2)^2+o(1).
\]

Finally `S<=Delta_++117 Ccal` and
`integral(Q-9/2)^2<=12 Ccal` make the claimed
`2 Delta_++8500 Ccal+o(1)` a valid upper bound. The Ricci-L2 Hessian
estimate (5) also follows from the displayed identity and GN estimate by
Young's inequality, with coefficients 32 and 33 as stated.

These checks concern the analytic replacement of the weight and the
resulting defect/model controls. They do not by themselves certify the
later closure argument, applications, or unrestricted Yau26.
