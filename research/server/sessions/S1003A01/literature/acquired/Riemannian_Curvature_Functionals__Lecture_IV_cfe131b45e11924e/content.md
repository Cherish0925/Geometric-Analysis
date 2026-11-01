---
retention_scope: session
part: 1
total_parts: 1
---

# Riemannian Curvature Functionals: Lecture IV

> Source: https://www.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf
> Fetched: 2026-10-04 22:09
> Method: FULLTEXT_HTML_FIRECRAWL|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "exa",
  "source_url": "https://www.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf",
  "metadata": {
    "provenance_urls": [
      "https://www.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf"
    ],
    "search_origins": [
      {
        "source": "exa",
        "query": "second variation integral |Ric - lambda g|^2 at Einstein metric Lichnerowicz operator gauge fixing"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

### Riemannian Curvature Functionals: Lecture IV

Jeff Viaclovsky

Park City Mathematics Institute

July 19, 2013

### Lecture Outline

Today we will discuss the following:

• Strict local minimization of quadratic functionals in dimension 4. 
• A local reverse Bishop’s inequality. 
• B t-flat metrics. 
• Construction of critical points of quadratic functionals using gluing methods. 

### Strict local minimzation

We saw that critical points of the Einstein-Hilbert functional in 
general have a saddle-point structure. However, critical points for 
certain quadratic functionals have a nicer local variational 
structure. For example, one result we will discuss today is the 
following: 
Theorem (Gursky-V 2011) 

On S 4, gS is a strict local minimizer (modulo diffeomorphisms) for

F τ =Z| Ric| 2dV + τZ R 2dV

provided that

−

1 
3 

< τ <

1 
6 

.

### Splitting

Just as in the case of the Einstein-Hilbert functional, the second 
variation is orthogonal with respect to the splitting 
S 2(T∗M) = { f · g} ⊕ {L (α)} ⊕ { δh = 0, trg(h) = 0} . 
Therefore, if h is any symmetric 2-tensor, then decompose h as 
h = f · g + L α + z, 

where z is TT. Then F 00τ(h, h) = F 00τ(f · g, f · g) + F 00τ(z, z).

• To check the second variation, we only need to consider conformal variations and TT variations separately.

### The Jacobi operator

We will not write out the Euler-Lagrange equations, but point out that Einstein metrics are indeed critical for F τ . Let us write the second variation as

## Retrieved source content

## Riemannian Curvature Functionals: Lecture IV

### Jeff Viaclovsky

Park City Mathematics Institute

July 19, 2013

* * *

Lecture Outline

Today we will discuss the following:

_•_ Strict local minimization of quadratic functionals in
dimension 4.

_•_ A local reverse Bishop’s inequality.

• Bt-flat metrics.

$$
B^{t}
$$

_•_ Construction of critical points of quadratic functionals using
gluing methods.

* * *

## Strict local minimzation

We saw that critical points of the Einstein-Hilbert functional in
general have a saddle-point structure. However, critical points for
certain quadratic functionals have a nicer local variational
structure. For example, one result we will discuss today is the
following:

### Theorem (Gursky-V 2011)

On S4, gS is a strict local minimizer (modulo diffeomorphisms) for
∫ ∫

$$
S^{4}
$$

$$
\\mathcal{F}\_{\\tau}=\\int\|R i c\|^{2}d V+\\tau\\int\\boldsymbol{R}^{2}d V,
$$

_provided that_

$$
-\\frac{1}{3}<\\tau<\\frac{1}{6}.
$$

* * *

## Splitting

Just as in the case of the Einstein-Hilbert functional, the second
variation is orthogonal with respect to the splitting

$$
S^{2}(T^{\*}M)={f\\cdot g}\\oplus{\\mathcal{L}(\\alpha)}\\oplus{\\delta h=0,t r\_{g}(h)=0}.
$$

Therefore, if _h_ is any symmetric 2-tensor, then decompose _h_ as

$$
h=f\\cdot g+\\mathcal{L}\\alpha+z,
$$

where _z_ is TT. Then

$$
z
$$

$$
\\mathcal{F} _{\\tau}^{\\prime\\prime}(h,h)=\\mathcal{F}_{\\tau}^{\\prime\\prime}(f\\cdot g,\\bar{f}\\cdot g)+\\mathcal{F}\_{\\tau}^{\\prime\\prime}(z,z).
$$

_•_ To check the second variation, we only need to consider
conformal variations and TT variations separately.

* * *

## The Jacobi operator

We will not write out the Euler-Lagrange equations, but point out
that Einstein metrics are indeed critical for Fτ. Let us write the
second variation as
∫

$$
\\mathcal{F}\_{\\tau}
$$

$$
\\mathcal{F} _{\\tau}^{\\prime\\prime}(h_{1},h\_{2})=\\int\_{M}\\langle h\_{1},J h\_{2}\\rangle d V.
$$

We have:

### Proposition

_if g is Einstein with Ric_ = _λ · g and h is TT, then the Jacobi_
operator of Fτ is

$$
Ric=\\lambda\\cdot g
$$

$$
\\mathcal{F}\_{\\tau}
$$

$$
J h=\\frac{1}{2}\\Big(\\Delta\_{L}+2\\lambda\\Big)\\Big(\\Delta\_{L}+4\\Big(1+2\\tau\\Big)\\lambda\\Big)h,
$$

_where_

$$
\\Delta\_{L}h\_{i j}=\\Delta h\_{i j}+2R\_{i p j q}h^{p q}-2\\boldsymbol{\\lambda}\\cdot\\boldsymbol{h}\_{i j}.
$$

* * *

## 4 The case of (S , gS)

$$
\\textcircled{6}\\sqrt{3}
$$

In this case, the Lichnerowicz Laplacian on TT-tensors is

$$
\\Delta\_{L}h=\\Delta h-8h.
$$

### Proposition

_The least eigenvalue of the rough Laplacian on TT-tensors is 8._

The proof is left as an exercise. Hint: use the inequality
∫

$$
\\int\_{S^{4}}\|\\nabla\_{i}h\_{j k}+\\nabla\_{j}h\_{k i}+\\nabla\_{k}h\_{i j}\|^{2}d V\\geq0.
$$

Consequently, least eigenvalue of the Lichnerowicz Laplacian on
TT-tensors is 16. The previous proposition then implies that if

$$
\\tau<\\frac{1}{6},
$$

then the Jacobi operator is positive definite when restricted to
TT-tensors.

* * *

### Proposition

_if g is Einstein with Ric_ = _λ · g and h_ = _fg, then_

$$
Ric=\\lambda\\cdot g
$$

$$
h=f g
$$

$$
t r(J f)=\\frac{4+12\\tau}{2}(3\\Delta+4\\lambda)\\Delta f.
$$

This implies that the Jacobi operator is non-negative in conformal
directions for

$$
-\\frac{1}{3}<\\tau,
$$

with the zero eigenvalues given by _h_ = _f · g,_ where _f_ is a lowest
nontrival eigenfunction of ∆ (by Lichnerowicz’ Theorem).

$$
\\mathit{h}=\\mathit{f}\\cdot\\mathit{g}
$$

$$
\\Delta
$$

* * *

## Strict stability

• On (S4,gS) the second variation is strictly positive on
_TT_-tensors, and strictly positive in conformal directions
(except for lowest nontrivial eigenfunction directions) in the
range

$$
(S^{4},g\_{S})
$$

$$
-\\frac{1}{3}<\\tau<\\frac{1}{6}.
$$

_•_ Using a modification of the Ebin-Palais slicing, we can ignore
Lie derivative directions (as before), but we can also ignore
the conformal zero eigentensors using conformal
diffeomorphisms, so the functional is in fact strictly localy
minimized at the spherical metric modulo diffeomorphisms.

∫
Notice that for τ = −(1/4), the functional is \|E\|2, so is
obviously strictly minimized for this _τ,_ but our improvement of the
range of _τ_ for minimization has an interesting application:

$$
\\tau=-(1/4)
$$

$$
\\int\|E\|^{2}
$$

$$
\\tau
$$

$$
\\tau
$$

* * *

## A reverse Bishop’s inequality

The classical Bishop’s inequality implies that if (M4,g) is a closed
manifold with Ric(g) ≥ Ric(S4,gS) = 3g, then the volume
satisfies Vol(g) ≤ Vol(S4,gS), and equality holds only if (M,g) is
isometric to (S4,gS). An interesting consequence of strict local
minimization for _τ_ = 0 is that, locally, a “reverse Bishop’s
inequality” holds:

$$
(M^{4},g)
$$

$$
Ric(g)\\geq Ric(S^4,g\_S)=3g
$$

$$
Vol(g)\\leq Vol(S^4,g\_S)
$$

$$
(M,g)
$$

$$
(S^{4},g\_{S})
$$

$$
\\tau=0
$$

### Corollary (Gursky-V 2011)

On (S4,gS), there exists a C2,α-neighborhood U of gS such that if
g˜ ∈ U with Ric(˜g) ≤ 3˜g, then Vol(˜g) ≥ Vol(gS) with equality if
and only if g˜ = φ∗g for some diffeomorphism φ : M → M.

$$
(S^{4},g\_{S})
$$

$$
C^{2,\\alpha}
$$

$$
\\tilde{g}\\in U
$$

$$
Ric(\\tilde{g})\\leq3\\tilde{g}
$$

$$
{V o l}(\\tilde{g})\\geq{V o l}(g\_{S})
$$

$$
\\tilde{g}=\\phi^{\*}g
$$

$$
\\phi:M\\rightarrow M
$$

Interesting questions:

_•_ What is the largest neighborhood _U_ for which this holds?

∫
• Is the functional4\|Ric\|2dV globally minimized at gS?
S

$$
\\int\_{S^{4}}\|Ric\|^{2}dV
$$

$$
g\_{S}?
$$

* * *

Bt-flat metrics

We will be interested in the functional
∫

$$
\\mathcal{B}\_{t}\[g\]=\\int\|W\|^{2}d V+t\\int\\boldsymbol{R}^{2}d V.
$$

The Euler-Lagrange equations of Bt are given by

$$
\\mathcal{B}\_{t}
$$

$$
B^{t}\\equiv B+t C=0,
$$

where _B_ is the _Bach tensor_ defined by

$$
B\_{i j}\\equiv-4\\Big(\\nabla^{k}\\nabla^{l}W\_{i k j l}+\\frac{1}{2}R^{k l}W\_{i k j l}\\Big),
$$

and _C_ is the tensor defined by

$$
C\_{i j}=2\\nabla\_{i}\\nabla\_{j}R-2(\\Delta R)g\_{i j}-2R R\_{i j}+\\frac{1}{2}R^{2}g\_{i j}.
$$

* * *

## Bt-flat metrics

Note:

• Any Einstein metric is critical for Bt.

$$
\\mathcal{B}\_{t}
$$

• We will refer to such a critical metric as a Bt-flat metric.

$$
B^{t}
$$

For _t 6=_ 0, by taking a trace of the E-L equations:

$$
t\\neq0
$$

$$
\\Delta R=0.
$$

If _M_ is compact, this implies _R_ = _constant._

$$
R=\\mathrm{constant}.
$$

Consequently, the Bt-flat condition is equivalent to

$$
B^{t}-\\mathsf{f}\\mathsf{l}\\mathsf{a}
$$

$$
\\boxed{B=2tR\\cdot E},
$$

where _E_ denotes the traceless Ricci tensor. In other words:

_•_ The Bach tensor is a constant multiple of the traceless Ricci
tensor.

* * *

## Orbifold Limits

The Bt-flat equation can be rewritten as

$$
B^{t}
$$

$$
\\Delta\\mathrm{Ric}=\\mathrm{Rm}\*\\mathrm{Rc}
$$

(1)

### Theorem (Tian-V)

(Mi,gi) sequence of 4-dimensional manifolds satisfying (1) and
∫

$$
(M\_{i},g\_{i})
$$

$$
\\int\|R m\|^{2}<\\Lambda,{V o l}(B(q,s))>V s^{4},b\_{1}(\\mathit{M}\_{i})<B.
$$

_Then for a subsequence {j}⊂{i},_

$$
{j}\\subset{i}
$$

$$
(M\_{j},g\_{j})\\xrightarrow{\\operatorname{C h e e g e r-G r o m o v}}(M\_{\\infty},g\_{\\infty}),
$$

_where_ ( _M_ ∞ _,g_ ∞) _is a multi-fold satisyfing_ (1), _with finitely many_
_singular points._

$$
\\left(M\_{\\infty},g\_{\\infty}\\right)
$$

Rescaling such a sequence to have bounded curvature near a
singular point yields non-compact limits called _asympotically_
_locally Euclidean_ spaces (ALE spaces).

* * *

Can you reverse this process?

I.e., start with an critical orbifold, “glue on” critical ALE metrics
at the singular points, and resolve to a smooth critical metric?

Answer is “no” in general, because this is a self-adjoint gluing
problem.

However, the following theorem says that the answer is “YES” in
certain cases:

* * *

### Theorem (Gursky-V 2013)

A Bt-flat metric exists on the manifolds in the table for some t
_near the indicated value of t0._

$$
B^{t}
$$

$$
t\_{0}
$$

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| (\\mathbb{CP}^2 #\\overline{\\mathbb{CP}}^2) | -1/3 |
| (S^2 × S^2 #\\overline{\\mathbb{CP}}^2 = \\mathbb{CP}^2 #2\\overline{\\mathbb{CP}}^2) | -1/3, -(9m1)-1 |
| 2#S2 × S2 | -2(9m1)-1 |

$$
\\overline{\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2}
$$

$$
S^{2}\\times S^{2}#\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}=\\mathbb{C}\\mathbb{P}^{2}#2\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}
$$

$$
-1/3,-(9m\_1)^{-1}
$$

$$
2#S^{2}\\times S^{2}
$$

$$
-2(9m\_{1})^{-1}
$$

The constant _m1_ is a geometric invariant called the _mass_ of an
certain asymptotically flat metric: the Green’s function metric of
the product metric S2 × S2.

$$
m\_{1}
$$

$$
S^{2}\\times S^{2}
$$

* * *

## Remarks

_• M_ = CP2#CP2 admits an U(2)-invariant Einstein metric
called the “Page metric”. _M_ does not admit any
K¨ahler-Einstein metric, but the Page metric is conformal to an
extremal K¨ahler metric.

$$
M=\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

_• M_ = CP2#2CP2 admits a toric invariant Einstein metric
called “Chen-LeBrun-Weber metric”. Again, _M_ does not
admit any K¨ahler-Einstein metric, but the
Chen-LeBrun-Weber metric is conformal to an extremal
K¨ahler metric.

$$
M=\\mathbb{C}\\mathbb{P}^2#2\\mathbb{C}\\mathbb{P}^2
$$

• M = S2 × S2#S2 × S2 does not admit any K¨ahler metric, it
does not even admit an almost complex structure. Our metric
is the first known example of a “canonical” metric on this
manifold.

$$
M=S^{2}\\times S^{2}#S^{2}\\times S^{2}
$$

* * *

## Green’s function metric

The first step in the gluing procedure is to construct an
asymptotically flat metric, called the Green’s function metric.
The conformal Laplacian:

$$
Lu=-6\\Delta u+Ru.
$$

If _(M,g)_ is compact and _R_ \> 0, then for any _p ∈ M,_ there is a
unique positive solution to the equation

$$
(M,g)
$$

$$
R>0
$$

$$
p\\in M
$$

$$
LG=0\ on\ M\\setminus{p}
$$

$$
G=\\rho^{-2}(1+o(1))
$$

as _ρ →_ 0, where _ρ_ is geodesic distance to the basepoint _p._

$$
\\rho\\to0
$$

$$
\\rho
$$

$$
p
$$

• Denote N = M {p} with metric gN = G2gM. The metric
gN is scalar-flat and asymptotically flat of order 2.

$$
N=M\\setminus{p}
$$

$$
g\_{N}=G^{2}g\_{M}
$$

$$
g\_{N}
$$

• If (M,g) is Bach-flat, then (N,gN) is also Bach-flat (from
conformal invariance) and scalar-flat (since we used the
Green’s function). Consequently, gN is Bt-flat for all t ∈ R.

$$
\\mathsf{If}\\left(M,g\\right)
$$

$$
(N,g\_N)
$$

$$
g\_{N}
$$

$$
B^{t}
$$

$$
t\\in\\mathbb{R}
$$

* * *

## The approximate metric

• Let (Z,gZ) and (Y,gY) be Einstein manifolds, and assume
that gY has positive scalar curvature.

$$
\\left(Z,g\_{Z}\\right)
$$

$$
\\left(Y,g\_{Y}\\right)
$$

_•_ Choose basepoints _z0 ∈ Z_ and _y0 ∈ Y._

$$
z\_{0}\\in Z
$$

$$
y\_{0}\\in Y
$$

• Convert (Y,gY) into an asymptotically flat (AF) metric
(N,gN) using the Green’s function for the conformal
Laplacian based at y0. As pointed out above, gN is Bt-flat for
any _t._

$$
\\left(Y,g\_{Y}\\right)
$$

$$
\\left(N,g\_{N}\\right)
$$

$$
y\_{0}
$$

$$
g\_{N}
$$

$$
B^{t}-\\mathsf{f}\\mathsf{l}\\mathsf{a}\\mathsf{t}
$$

_•_ Let _a_ \> 0 be small, and consider _Z\\B(z0,a)._ Scale the
compact metric to (Z, g˜ = a−4gZ). Attach this metric to the
metric (N \ B(a−1),gN) using cutoff functions near the
boundary, to obtain a smooth metric on the connect sum
_Z#Y._

$$
a>0
$$

$$
Z\\setminus B(z\_{0},a)
$$

$$
\\left(Z,\\tilde{g}=a^{-4}g\_{Z}\\right)
$$

$$
(N\\setminus B(a^{-1}),g\_N)
$$

$$
Z#\\overline{Y}
$$

* * *

Compact Einstein Damage zone
metric
AF metric

Figure: The approximate metric.

Since both gZ and gN are Bt-flat, this metric is an “approximate”
Bt-flat metric, with vanishing Bt tensor away from the “damage
zone”, where cutoff functions were used.

$$
g\_{Z}
$$

$$
g\_{N}
$$

$$
B^{t}-\\mathsf{f}\\mathsf{l}\\mathsf{a}\\mathsf{t}
$$

$$
B^{t\_{1}}
$$

$$
B^{t}
$$

* * *

## Gluing parameters

In general, there are several degrees of freedom in this approximate
metric.

_•_ The scaling parameter _a_ (1-dimensional).

_•_ Rotational freedom when attaching (6-dimensional).

_•_ Freedom to move the base points of either factor
(8-dimensional).

Total of 15 gluing parameters.

* * *

Lyapunov-Schmidt reduction

These 15 gluing parameters yield a 15-dimensional space of
“approximate” kernel of the linearized operator. Using a
Lyapunov-Schmidt reduction argument, one can reduce the
problem to that of finding a zero of the _Kuranishi map_

$$
\\Psi:U\\subset\\mathbb{R}^{15}\\rightarrow\\mathbb{R}^{15}.
$$

_•_ It is crucial to use certain weighted norms to find a bounded
right inverse for the linearized operator.

_•_ This 15-dimensional problem is too difficult in general: we will
take advantage of various symmetries in order to reduce to
only 1 free parameter: the scaling parameter _a._

* * *

## Technical theorem

The leading term of the Kuranishi map corresponding to the
scaling parameter is given by:

### Theorem (Gursky-V 2013)

_As a → 0, then for any_ \> _0,_

$$
a\\to0
$$

$$
\\epsilon>0
$$

()
2
Ψ1 = W (z0) ~ W (y0) \+ 4tR(z0)mass(gN) ω3a4 \+ O(a6−),
3

$$
\\Psi\_{1}=\\Big(\\frac{2}{3}W\\big(z\_{0}\\big)\\circledast W\\big(y\_{0}\\big)+4t R\\big(z\_{0}\\big)\\mathrm{mass}\\big(g\_{N}\\big)\\Big)\\omega\_{3}a^{4}+O\\big(a^{6-\\epsilon}\\big),
$$

where ω3 = Vol(S3), and the product of the Weyl tensors is given
_by_

$$
\\omega\_{3}=Vol(S^{3})
$$

∑
W (z0) ~ W (y0) = Wijkl(z0)(Wijkl(y0) \+ Wilkj(y0)),
_ijkl_

$$
W(z\_{0})\\circledast W(y\_{0})=\\sum\_{i j k l}W\_{i j k l}(z\_{0})(W\_{i j k l}(y\_{0})+W\_{i l k j}(y\_{0})),
$$

where Wijkl(·) denotes the components of the Weyl tensor in a
_normal coordinate system at the corresponding point._

$$
W\_{i j k l}(\\cdot)
$$

* * *

(CP2,gFS), the Fubini-Study metric, Ric = 6g.

$$
\\left(\\mathbb{C}\\mathbb{P}^2,g\_{FS}\\right)
$$

$$
Ric=6g
$$

Torus action:

$$
\[z\_{0},z\_{1},z\_{2}\]\\mapsto\[z\_{0},e^{i\\theta\_{1}}z\_{1},e^{i\\theta\_{2}}z\_{2}\].
$$

Flip symmetry:

$$
\[z\_{0},z\_{1},z\_{2}\]\\mapsto\[z\_{0},z\_{2},z\_{1}\].
$$

* * *

\[0,0,1\]
\[1,0,0\] \[0,1,0\]

Figure: Orbit space of the torus action on CP2.

$$
\\mathbb{C P}^{2}
$$

* * *

(S2 × S2,gS2×S2), the product of 2-dimensional spheres of
Gaussian curvature 1, _Ric_ = _g._

$$
(S^{2}\\times S^{2},g\_{S^{2}\\times S^{2}})
$$

Torus action:

Product of rotations fixing north and south poles.

Flip symmetry:

$$
(p\_{1},p\_{2})\\mapsto(p\_{2},p\_{1}).
$$

* * *

(s,n) (s,s)
(n,n) (n,s)

Figure: Orbit space of the torus action on S2 × S2.

$$
S^{2}\\times S^{2}
$$

* * *

Recall the mass of an AF space is defined by
∫

$$
\\mathrm{mass}(g\_{N})=\\lim\_{R\\rightarrow\\infty}\\omega\_{3}^{-1}\\int\_{S(R)}\\sum\_{i,j}(\\partial\_{i}g\_{i j}-\\partial\_{j}g\_{i i})(\\partial\_{i}\\lrcorner d V),
$$

with ω3 = Vol(S3).

$$
\\omega\_{3}=Vol(S^{3})
$$

The Green’s function metric of the Fubini-Study metric ĝFS is also
known as the Burns metric, and is completely explicit, with mass
given by

$$
\\hat{g}\_{FS}
$$

$$
\\mathrm{mass}(\\hat{g}\_{FS})=2.
$$

* * *

Mass of Green’s function metric

However, the Green’s function metric ĝS2×S2 of the product metric
does not seem to have a known explicit description. We will denote

$$
\\hat{g}\_{S^{2}\\times S^{2}}
$$

$$
m\_{1}=\\operatorname{mass}(\\hat{g}\_{S^{2}\\times S^{2}}).
$$

By the positive mass theorem of Schoen-Yau, _m1_ \> 0\. Note that
since _S2 × S2_ is spin, this also follows from Witten’s proof of the
positive mass theorem.

$$
\\mathsf{\\cdot Y a u},:m\_{1}>0
$$

$$
S^{2}\\times S^{2}
$$

### Remark

_For the curious, the mass m1 =.5872...., which implies that_
(−9m1)−1 = −.1892.....

$$
m\_{1}=.5872....,
$$

$$
(-9m\_{1})^{-1}=-.1892
$$

* * *

_•_ We impose the toric symmetry and “flip” symmetry in order
to reduce the number of free parameters to 1 (only the scaling
parameter). That is, we perform an equivariant gluing.

_•_ The special value of _t0_ is computed by

$$
t\_{0}
$$

$$
\\frac{2}{3}W\\left(z\_{0}\\right)\\circledast W\\left(y\_{0}\\right)+4t\_{0}R\\left(z\_{0}\\right)\\mathrm{mass}\\left(g\_{N}\\right)=0.
$$

_•_ This choice of _t0_ makes the leading term of the Kuranishi
map vanish, and is furthermore a _nondegenerate_ zero (if
R(z0) \> 0; mass(gN) \> 0 by the positive mass theorem).

$$
t\_{0}
$$

$$
R(z\_{0})>0;\\quad\\operatorname{mass}(g\_{N})>0
$$

* * *

## First case

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| (\\mathbb{CP}^{2})#(\\overline{\\mathbb{CP}}^{2}) | -1/3 |

$$
\\overline{\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2}
$$

_•_ The compact metric is the Fubini-Study metric, with a Burns
AF metric glued on, a computation yields _t0_ = −1/3.

* * *

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| (S^{2} × S^{2} # \\overline{\\mathbb{C}P}^{2} = \\mathbb{C}P^{2} # 2 \\overline{\\mathbb{C}P}^{2}) | -1/3, -(9m\_{1})^{-1} |

$$
\\overline{\\mathsf{V}\\mathsf{a}\\mathsf{l}\\mathsf{u}\\mathsf{e}(\\mathsf{s})}
$$

$$
S^{2}\\times S^{2}#\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}=\\mathbb{C}\\mathbb{P}^{2}#2\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}
$$

$$
-1/3,-(9m\_1)^{-1}
$$

• The compact metric is the product metric on S2 × S2, with a
Burns AF metric glued on, this gives _t0_ = −1/3.

$$
S^{2}\\times S^{2}
$$

$$
t\_{0}=-1/3
$$

• Alternatively, take the compact metric to be (CP2,gFS), with
a Green’s function _S2 × S2_ metric glued on. In this case,
t0 = −(9m1)−1.

$$
\\left(\\mathbb{C}\\mathbb{P}^2,g\_{FS}\\right)
$$

$$
S^{2}\\times S^{2}
$$

$$
t\_{0}=-(9m\_{1})^{-1}
$$

* * *

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| 2#S2 × S2 | -2(9m1)-1 |

$$
\\overline{\\mathsf{V}\\mathsf{a}\\mathsf{l}\\mathsf{u}\\mathsf{e}(\\mathsf{s})}
$$

$$
\\overline{2#S^{2}\\times S^{2}}
$$

$$
\\overline{-2(9m\_{1})^{-1}}
$$

• The compact metric is the product metric on S2 × S2, with a
Green’s function _S2 × S2_ metric glued on. In this case,
t0 = −2(9m1)−1.

$$
S^{2}\\times S^{2}
$$

$$
S^{2}\\times S^{2}
$$

$$
t\_{0}=-2(9m\_{1})^{-1}
$$

* * *

## Technical Points

• Ellipticity and gauging. The Bt-flat equations are not elliptic
due to diffeomorphism invariance. A gauging procedure
analogous to the Bianchi gauge is used.

$$
B^{t}
$$

• Rigidity of gFS and gS2×S2. Follows from the formulas
discussed at the beginning of today’s lecture, together with
some eigenvalue estimates.

$$
g\_{S^{2}\\times S^{2}}
$$

_•_ Refined approximate metric. The approximate metric
described above is not good enough. It must be improved by
matching up leading terms of the metrics by solving certain
auxiliary linear equations, so that the cutoff function
disappears from the leading term. We will not have time to
discuss this today.

* * *

## Ellipticity and gauging

The linearized operator of the Bt-flat equation is not elliptic, due
to diffeomorphism invariance. However, consider the “gauged”
nonlinear map _P_ given by

$$
B^{t\_{1}}
$$

$$
P\_{g}(\\theta)=(B+t C)(g+\\theta)+\\mathcal{K} _{g+\\theta}\[\\delta_{g}\\mathcal{K} _{g}\\delta_{g}\\stackrel{\\circ}{\\theta}\].
$$

Let St ≡ P ′(0) denote the linearized operator at θ = 0.

$$
S^{t}\\equiv P^{\\prime}(0)
$$

$$
\\theta=0
$$

### Proposition

If t 6= 0, then St is elliptic. Furthermore, if P(θ) = 0, and
∞
θ ∈ C4,α for some 0 < α < 1, then Bt(g + θ) = 0 and θ ∈ C.

$$
If t\\neq0
$$

$$
S^{t}
$$

$$
P(\\theta)=0
$$

$$
\\theta\\in C^{4,\\alpha}
$$

$$
0<\\alpha<1
$$

$$
B^{t}(g+\\theta)=0
$$

$$
\\theta\\in C^{\\infty}
$$

• Proof is an integration-by-parts. It is crucial that the Bt-flat
equations are variational (recall Bt is the functional), so
δBt = 0\. Equivalent to diffeomorphism invariance of Bt.

$$
B^{t}-\\mathsf{f}\\mathsf{l}\\mathsf{a}\\mathsf{t}
$$

$$
\\mathcal{B}\_{t}
$$

$$
\\delta B^{t}=0
$$

$$
\\mathcal{B}\_{t}
$$

* * *

## Rigidity

For _h_ transverse-traceless (TT), the linearized operator at an
Einstein metric is given by

$$
h
$$

$$
S^{t}h=\\Big(\\Delta\_{L}+\\frac{1}{2}R\\Big)\\Big(\\Delta\_{L}+\\Big(\\frac{1}{3}+t\\Big)R\\Big)h,
$$

where ∆L is the Lichnerowicz Laplacian, defined by

$$
\\Delta\_{L}
$$

$$
\\Delta\_{L}h\_{i j}=\\Delta h\_{i j}+2R\_{i p j q}h^{p q}-\\frac{1}{2}R h\_{i j}.
$$

_•_ Recall that infinitesimal Einstein deformations given by TT
kernel of the operator ∆L \+ 12R. We still have those, but
there are now more possibilities of deformations.

$$
\\Delta\_{L}+\\tfrac{1}{2}R
$$

* * *

## Rigidity

For _h_ = _fg,_ we have

$$
h=f g
$$

$$
t r\_{g}(S^{t}h)=6t(3\\Delta+R)(\\Delta f).
$$

(1)

The rigidity question is then reduced to a separate analysis of the
eigenvalues of ∆L on transverse-traceless tensors, and of ∆ on
functions.

$$
\\Delta\_{L}
$$

$$
\\Delta\\text{on}
$$

### Theorem (Gursky-V)

On (CP2,gFS), H1t = {0} provided that t < 1.

$$
(\\mathbb{C P}^{2},g\_{F S}),H\_{t}^{1}={0}
$$

$$
t<1
$$

### Theorem (Gursky-V)

On (S2 × S2,gS2×S2), H1t = {0} provided that t < 2/3 and
t 6= −1/3. If t = −1/3, then H1t is one-dimensional and spanned
_by the element g1 − g2._

$$
(S^{2}\\times S^{2},g\_{S^{2}\\times S^{2}}),H\_{t}^{1}={0}
$$

$$
t<2/3
$$

$$
t\\neq-1/3
$$

$$
t=-1/3
$$

$$
H\_{t}^{1}
$$

$$
g\_{1}-g\_{2}
$$

* * *

## Rigidity

_•_ Positive mass theorem says that _t0_ < 0, so luckily we are in
the rigidity range of the factors.

$$
t\_{0}<0
$$

_•_ Gauge term is carefully chosen so that solutions of the
linearized equation must be in the transverse-traceless gauge.
That is, if Sth = 0 then

$$
S^{t}h=0
$$

$$
(B^{t})'(h)+\\mathcal{K}\\delta\\mathcal{K}\\delta\\stackrel{\\circ}{h}=0
$$

implies that separately,

$$
(B ^ {t}) ^ {\\prime} (h) = 0 \\text {a n d} \\delta^ {\\circ} h = 0.
$$

* * *

## Final remarks

The proof shows that there is a dichotomy. Either

_•_ (i) there is a critical metric at exactly the critical _t0,_ in which
case there would necessarily be a 1-dimensional moduli space
of solutions for this fixed _t0,_ or

$$
t\_{0}
$$

_•_ (ii) for each value of the gluing parameter _a_ sufficiently small,
there will be a critical metric for a corresponding value of
_t0_ = _t0(a)._ The dependence of _t0_ on _a_ will depend on the
next term in the expansion of the Kuranishi map.

$$
t\_{0}=t\_{0}(a)
$$

$$
t\_{0}
$$

_•_ Which case actually happens?