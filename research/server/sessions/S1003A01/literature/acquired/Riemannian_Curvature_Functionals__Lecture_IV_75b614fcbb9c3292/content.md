---
retention_scope: session
part: 1
total_parts: 1
---

# Riemannian Curvature Functionals: Lecture IV

> Source: https://webapps.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf
> Fetched: 2026-10-04 22:10
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
  "source": "serper",
  "source_url": "https://webapps.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf",
  "metadata": {
    "provenance_urls": [
      "https://webapps.math.uci.edu/~jviaclov/lecturenotes/Park_City_Lecture_IV_Final.pdf"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "Gursky Viaclovsky connected sum Bach-flat metrics Weyl tensor Green function interaction formula"
      },
      {
        "source": "tavily",
        "query": "Gursky Viaclovsky connected sum Bach-flat metrics Weyl tensor Green function interaction formula"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

The first step in the gluing procedure is to construct an asymptotically flat metric, called the Green's function metric. The conformal ...

## Retrieved source content

## Riemannian Curvature Functionals: Lecture IV

### Jeff Viaclovsky

Park City Mathematics Institute

July 19, 2013

---

Lecture Outline

Today we will discuss the following:

*•* Strict local minimization of quadratic functionals in
dimension 4.

*•* A local reverse Bishop’s inequality.

• B<sup>t</sup>-flat metrics.

$$
B^{t}
$$

*•* Construction of critical points of quadratic functionals using
gluing methods.

---

## Strict local minimzation

We saw that critical points of the Einstein-Hilbert functional in
general have a saddle-point structure. However, critical points for
certain quadratic functionals have a nicer local variational
structure. For example, one result we will discuss today is the
following:

### Theorem (Gursky-V 2011)

On S<sup>4</sup>, g<sub>S</sub> is a strict local minimizer (modulo diffeomorphisms) for
∫ ∫

$$
S^{4}
$$

$$
\mathcal{F}_{\tau}=\int|R i c|^{2}d V+\tau\int\boldsymbol{R}^{2}d V,
$$

*provided that*

$$
-\frac{1}{3}<\tau<\frac{1}{6}.
$$

---

## Splitting

Just as in the case of the Einstein-Hilbert functional, the second
variation is orthogonal with respect to the splitting

$$
S^{2}(T^{*}M)=\{f\cdot g\}\oplus\{\mathcal{L}(\alpha)\}\oplus\{\delta h=0,t r_{g}(h)=0\}.
$$

Therefore, if *h* is any symmetric 2-tensor, then decompose *h* as

$$
h=f\cdot g+\mathcal{L}\alpha+z,
$$

where *z* is TT. Then

$$
z
$$

$$
\mathcal{F}_{\tau}^{\prime\prime}(h,h)=\mathcal{F}_{\tau}^{\prime\prime}(f\cdot g,\bar{f}\cdot g)+\mathcal{F}_{\tau}^{\prime\prime}(z,z).
$$

*•* To check the second variation, we only need to consider
conformal variations and TT variations separately.

---

## The Jacobi operator

We will not write out the Euler-Lagrange equations, but point out
that Einstein metrics are indeed critical for F<sub>τ</sub>. Let us write the
second variation as
∫

$$
\mathcal{F}_{\tau}
$$

$$
\mathcal{F}_{\tau}^{\prime\prime}(h_{1},h_{2})=\int_{M}\langle h_{1},J h_{2}\rangle d V.
$$

We have:

### Proposition

*if g is Einstein with Ric* = *λ · g and h is TT, then the Jacobi*
operator of F<sub>τ</sub> is

$$
Ric=\lambda\cdot g
$$

$$
\mathcal{F}_{\tau}
$$

$$
J h=\frac{1}{2}\Big(\Delta_{L}+2\lambda\Big)\Big(\Delta_{L}+4\Big(1+2\tau\Big)\lambda\Big)h,
$$

*where*

$$
\Delta_{L}h_{i j}=\Delta h_{i j}+2R_{i p j q}h^{p q}-2\boldsymbol{\lambda}\cdot\boldsymbol{h}_{i j}.
$$

---

## 4 The case of (S , g<sub>S</sub>)

$$
\textcircled{6}\sqrt{3}
$$

In this case, the Lichnerowicz Laplacian on TT-tensors is

$$
\Delta_{L}h=\Delta h-8h.
$$

### Proposition

*The least eigenvalue of the rough Laplacian on TT-tensors is 8.*

The proof is left as an exercise. Hint: use the inequality
∫

$$
\int_{S^{4}}|\nabla_{i}h_{j k}+\nabla_{j}h_{k i}+\nabla_{k}h_{i j}|^{2}d V\geq0.
$$

Consequently, least eigenvalue of the Lichnerowicz Laplacian on
TT-tensors is 16. The previous proposition then implies that if

$$
\tau<\frac{1}{6},
$$

then the Jacobi operator is positive definite when restricted to
TT-tensors.

---

### Proposition

*if g is Einstein with Ric* = *λ · g and h* = *fg, then*

$$
Ric=\lambda\cdot g
$$

$$
h=f g
$$

$$
t r(J f)=\frac{4+12\tau}{2}(3\Delta+4\lambda)\Delta f.
$$

This implies that the Jacobi operator is non-negative in conformal
directions for

$$
-\frac{1}{3}<\tau,
$$

with the zero eigenvalues given by *h* = *f · g,* where *f* is a lowest
nontrival eigenfunction of ∆ (by Lichnerowicz’ Theorem).

$$
\mathit{h}=\mathit{f}\cdot\mathit{g}
$$

$$
\Delta
$$

---

## Strict stability

• On (S<sup>4</sup>,g<sub>S</sub>) the second variation is strictly positive on
*TT*-tensors, and strictly positive in conformal directions
(except for lowest nontrivial eigenfunction directions) in the
range

$$
(S^{4},g_{S})
$$

$$
-\frac{1}{3}<\tau<\frac{1}{6}.
$$

*•* Using a modification of the Ebin-Palais slicing, we can ignore
Lie derivative directions (as before), but we can also ignore
the conformal zero eigentensors using conformal
diffeomorphisms, so the functional is in fact strictly localy
minimized at the spherical metric modulo diffeomorphisms.

∫
Notice that for τ = −(1/4), the functional is |E|<sup>2</sup>, so is
obviously strictly minimized for this *τ,* but our improvement of the
range of *τ* for minimization has an interesting application:

$$
\tau=-(1/4)
$$

$$
\int|E|^{2}
$$

$$
\tau
$$

$$
\tau
$$

---

## A reverse Bishop’s inequality

The classical Bishop’s inequality implies that if (M<sup>4</sup>,g) is a closed
manifold with Ric(g) ≥ Ric(S<sup>4</sup>,g<sub>S</sub>) = 3g, then the volume
satisfies Vol(g) ≤ Vol(S<sup>4</sup>,g<sub>S</sub>), and equality holds only if (M,g) is
isometric to (S<sup>4</sup>,g<sub>S</sub>). An interesting consequence of strict local
minimization for *τ* = 0 is that, locally, a “reverse Bishop’s
inequality” holds:

$$
(M^{4},g)
$$

$$
Ric(g)\geq Ric(S^4,g_S)=3g
$$

$$
Vol(g)\leq Vol(S^4,g_S)
$$

$$
(M,g)
$$

$$
(S^{4},g_{S})
$$

$$
\tau=0
$$

### Corollary (Gursky-V 2011)

On (S<sup>4</sup>,g<sub>S</sub>), there exists a C<sup>2,α</sup>-neighborhood U of g<sub>S</sub> such that if
g˜ ∈ U with Ric(˜g) ≤ 3˜g, then Vol(˜g) ≥ Vol(g<sub>S</sub>) with equality if
and only if g˜ = φ<sup>∗</sup>g for some diffeomorphism φ : M → M.

$$
(S^{4},g_{S})
$$

$$
C^{2,\alpha}
$$

$$
\tilde{g}\in U
$$

$$
Ric(\tilde{g})\leq3\tilde{g}
$$

$$
{V o l}(\tilde{g})\geq{V o l}(g_{S})
$$

$$
\tilde{g}=\phi^{*}g
$$

$$
\phi:M\rightarrow M
$$

Interesting questions:

*•* What is the largest neighborhood *U* for which this holds?

∫
• Is the functional4|Ric|<sup>2</sup>dV globally minimized at g<sub>S</sub>?
S

$$
\int_{S^{4}}|Ric|^{2}dV
$$

$$
g_{S}?
$$

---

B<sup>t</sup>-flat metrics

We will be interested in the functional
∫

$$
\mathcal{B}_{t}[g]=\int|W|^{2}d V+t\int\boldsymbol{R}^{2}d V.
$$

The Euler-Lagrange equations of B<sub>t</sub> are given by

$$
\mathcal{B}_{t}
$$

$$
B^{t}\equiv B+t C=0,
$$

where *B* is the *Bach tensor* defined by

$$
B_{i j}\equiv-4\Big(\nabla^{k}\nabla^{l}W_{i k j l}+\frac{1}{2}R^{k l}W_{i k j l}\Big),
$$

and *C* is the tensor defined by

$$
C_{i j}=2\nabla_{i}\nabla_{j}R-2(\Delta R)g_{i j}-2R R_{i j}+\frac{1}{2}R^{2}g_{i j}.
$$

---

## B<sup>t</sup>-flat metrics

Note:

• Any Einstein metric is critical for B<sub>t</sub>.

$$
\mathcal{B}_{t}
$$

• We will refer to such a critical metric as a B<sup>t</sup>-flat metric.

$$
B^{t}
$$

For *t 6=* 0, by taking a trace of the E-L equations:

$$
t\neq0
$$

$$
\Delta R=0.
$$

If *M* is compact, this implies *R* = *constant.*

$$
R=\mathrm{constant}.
$$

Consequently, the B<sup>t</sup>-flat condition is equivalent to

$$
B^{t}-\mathsf{f}\mathsf{l}\mathsf{a}
$$

$$
\boxed{B=2tR\cdot E},
$$

where *E* denotes the traceless Ricci tensor. In other words:

*•* The Bach tensor is a constant multiple of the traceless Ricci
tensor.

---

## Orbifold Limits

The B<sup>t</sup>-flat equation can be rewritten as

$$
B^{t}
$$

$$
\Delta\mathrm{Ric}=\mathrm{Rm}*\mathrm{Rc}
$$

(1)

### Theorem (Tian-V)

(M<sub>i</sub>,g<sub>i</sub>) sequence of 4-dimensional manifolds satisfying (1) and
∫

$$
(M_{i},g_{i})
$$

$$
\int|R m|^{2}<\Lambda,{V o l}(B(q,s))>V s^{4},b_{1}(\mathit{M}_{i})<B.
$$

*Then for a subsequence {j}⊂{i},*

$$
\{j\}\subset\{i\}
$$

$$
(M_{j},g_{j})\xrightarrow{\operatorname{C h e e g e r-G r o m o v}}(M_{\infty},g_{\infty}),
$$

*where* (*M*<sub>∞</sub>*,g*<sub>∞</sub>) *is a multi-fold satisyfing* (1), *with finitely many
singular points.*

$$
\left(M_{\infty},g_{\infty}\right)
$$

Rescaling such a sequence to have bounded curvature near a
singular point yields non-compact limits called *asympotically
locally Euclidean* spaces (ALE spaces).

---

Can you reverse this process?

I.e., start with an critical orbifold, “glue on” critical ALE metrics
at the singular points, and resolve to a smooth critical metric?

Answer is “no” in general, because this is a self-adjoint gluing
problem.

However, the following theorem says that the answer is “YES” in
certain cases:

---

### Theorem (Gursky-V 2013)

A B<sup>t</sup>-flat metric exists on the manifolds in the table for some t
*near the indicated value of t<sub>0</sub>.*

$$
B^{t}
$$

$$
t_{0}
$$

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| \(\mathbb{CP}^2 \#\overline{\mathbb{CP}}^2\) | -1/3 |
| \(S^2 × S^2 \#\overline{\mathbb{CP}}^2 = \mathbb{CP}^2 \#2\overline{\mathbb{CP}}^2\) | -1/3, -(9m1)-1 |
| 2#S2 × S2 | -2(9m1)-1 |

$$
\overline{\mathbb{C}\mathbb{P}^2\#\overline{\mathbb{C}\mathbb{P}}^2}
$$

$$
S^{2}\times S^{2}\#\overline{\mathbb{C}}\overline{\mathbb{P}}^{2}=\mathbb{C}\mathbb{P}^{2}\#2\overline{\mathbb{C}}\overline{\mathbb{P}}^{2}
$$

$$
-1/3,-(9m_1)^{-1}
$$

$$
2\#S^{2}\times S^{2}
$$

$$
-2(9m_{1})^{-1}
$$

The constant *m<sub>1</sub>* is a geometric invariant called the *mass* of an
certain asymptotically flat metric: the Green’s function metric of
the product metric S<sup>2</sup> × S<sup>2</sup>.

$$
m_{1}
$$

$$
S^{2}\times S^{2}
$$

---

## Remarks

*• M* = CP<sup>2</sup>#CP<sup>2</sup> admits an U(2)-invariant Einstein metric
called the “Page metric”. *M* does not admit any
K¨ahler-Einstein metric, but the Page metric is conformal to an
extremal K¨ahler metric.

$$
M=\mathbb{C}\mathbb{P}^2\#\overline{\mathbb{C}\mathbb{P}}^2
$$

*• M* = CP<sup>2</sup>#2CP<sup>2</sup> admits a toric invariant Einstein metric
called “Chen-LeBrun-Weber metric”. Again, *M* does not
admit any K¨ahler-Einstein metric, but the
Chen-LeBrun-Weber metric is conformal to an extremal
K¨ahler metric.

$$
M=\mathbb{C}\mathbb{P}^2\#2\mathbb{C}\mathbb{P}^2
$$

• M = S<sup>2</sup> × S<sup>2</sup>#S<sup>2</sup> × S<sup>2</sup> does not admit any K¨ahler metric, it
does not even admit an almost complex structure. Our metric
is the first known example of a “canonical” metric on this
manifold.

$$
M=S^{2}\times S^{2}\#S^{2}\times S^{2}
$$

---

## Green’s function metric

The first step in the gluing procedure is to construct an
asymptotically flat metric, called the Green’s function metric.
The conformal Laplacian:

$$
Lu=-6\Delta u+Ru.
$$

If *(M,g)* is compact and *R* > 0, then for any *p ∈ M,* there is a
unique positive solution to the equation

$$
(M,g)
$$

$$
R>0
$$

$$
p\in M
$$

$$
LG=0\ on\ M\setminus\{p\}
$$

$$
G=\rho^{-2}(1+o(1))
$$

as *ρ →* 0, where *ρ* is geodesic distance to the basepoint *p.*

$$
\rho\to0
$$

$$
\rho
$$

$$
p
$$

• Denote N = M \{p} with metric g<sub>N</sub> = G<sup>2</sup>g<sub>M</sub>. The metric
g<sub>N</sub> is scalar-flat and asymptotically flat of order 2.

$$
N=M\setminus\{p\}
$$

$$
g_{N}=G^{2}g_{M}
$$

$$
g_{N}
$$

• If (M,g) is Bach-flat, then (N,g<sub>N</sub>) is also Bach-flat (from
conformal invariance) and scalar-flat (since we used the
Green’s function). Consequently, g<sub>N</sub> is B<sup>t</sup>-flat for all t ∈ R.

$$
\mathsf{If}\left(M,g\right)
$$

$$
(N,g_N)
$$

$$
g_{N}
$$

$$
B^{t}
$$

$$
t\in\mathbb{R}
$$

---

## The approximate metric

• Let (Z,g<sub>Z</sub>) and (Y,g<sub>Y</sub>) be Einstein manifolds, and assume
that g<sub>Y</sub> has positive scalar curvature.

$$
\left(Z,g_{Z}\right)
$$

$$
\left(Y,g_{Y}\right)
$$

*•* Choose basepoints *z<sub>0</sub> ∈ Z* and *y<sub>0</sub> ∈ Y.*

$$
z_{0}\in Z
$$

$$
y_{0}\in Y
$$

• Convert (Y,g<sub>Y</sub>) into an asymptotically flat (AF) metric
(N,g<sub>N</sub>) using the Green’s function for the conformal
Laplacian based at y<sub>0</sub>. As pointed out above, g<sub>N</sub> is B<sup>t</sup>-flat for
any *t.*

$$
\left(Y,g_{Y}\right)
$$

$$
\left(N,g_{N}\right)
$$

$$
y_{0}
$$

$$
g_{N}
$$

$$
B^{t}-\mathsf{f}\mathsf{l}\mathsf{a}\mathsf{t}
$$

*•* Let *a* > 0 be small, and consider *Z\B(z<sub>0</sub>,a).* Scale the
compact metric to (Z, g˜ = a<sup>−4</sup>g<sub>Z</sub>). Attach this metric to the
metric (N \ B(a<sup>−1</sup>),g<sub>N</sub>) using cutoff functions near the
boundary, to obtain a smooth metric on the connect sum
*Z#Y.*

$$
a>0
$$

$$
Z\setminus B(z_{0},a)
$$

$$
\left(Z,\tilde{g}=a^{-4}g_{Z}\right)
$$

$$
(N\setminus B(a^{-1}),g_N)
$$

$$
Z\#\overline{Y}
$$

---

Compact Einstein Damage zone
metric
AF metric

Figure: The approximate metric.

Since both g<sub>Z</sub> and g<sub>N</sub> are B<sup>t</sup>-flat, this metric is an “approximate”
B<sup>t</sup>-flat metric, with vanishing B<sup>t</sup> tensor away from the “damage
zone”, where cutoff functions were used.

$$
g_{Z}
$$

$$
g_{N}
$$

$$
B^{t}-\mathsf{f}\mathsf{l}\mathsf{a}\mathsf{t}
$$

$$
B^{t_{1}}
$$

$$
B^{t}
$$

---

## Gluing parameters

In general, there are several degrees of freedom in this approximate
metric.

*•* The scaling parameter *a* (1-dimensional).

*•* Rotational freedom when attaching (6-dimensional).

*•* Freedom to move the base points of either factor
(8-dimensional).

Total of 15 gluing parameters.

---

Lyapunov-Schmidt reduction

These 15 gluing parameters yield a 15-dimensional space of
“approximate” kernel of the linearized operator. Using a
Lyapunov-Schmidt reduction argument, one can reduce the
problem to that of finding a zero of the *Kuranishi map*

$$
\Psi:U\subset\mathbb{R}^{15}\rightarrow\mathbb{R}^{15}.
$$

*•* It is crucial to use certain weighted norms to find a bounded
right inverse for the linearized operator.

*•* This 15-dimensional problem is too difficult in general: we will
take advantage of various symmetries in order to reduce to
only 1 free parameter: the scaling parameter *a.*

---

## Technical theorem

The leading term of the Kuranishi map corresponding to the
scaling parameter is given by:

### Theorem (Gursky-V 2013)

*As a → 0, then for any* > *0,*

$$
a\to0
$$

$$
\epsilon>0
$$

()
<u>2</u>
Ψ<sub>1</sub> = W (z<sub>0</sub>) ~ W (y<sub>0</sub>) + 4tR(z<sub>0</sub>)mass(g<sub>N</sub>) ω<sub>3</sub>a<sup>4</sup> + O(a<sup>6−</sup>),
3

$$
\Psi_{1}=\Big(\frac{2}{3}W\big(z_{0}\big)\circledast W\big(y_{0}\big)+4t R\big(z_{0}\big)\mathrm{mass}\big(g_{N}\big)\Big)\omega_{3}a^{4}+O\big(a^{6-\epsilon}\big),
$$

where ω<sub>3</sub> = Vol(S<sup>3</sup>), and the product of the Weyl tensors is given
*by*

$$
\omega_{3}=Vol(S^{3})
$$

∑
W (z<sub>0</sub>) ~ W (y<sub>0</sub>) = W<sub>ijkl</sub>(z<sub>0</sub>)(W<sub>ijkl</sub>(y<sub>0</sub>) + W<sub>ilkj</sub>(y<sub>0</sub>)),
*ijkl*

$$
W(z_{0})\circledast W(y_{0})=\sum_{i j k l}W_{i j k l}(z_{0})(W_{i j k l}(y_{0})+W_{i l k j}(y_{0})),
$$

where W<sub>ijkl</sub>(·) denotes the components of the Weyl tensor in a
*normal coordinate system at the corresponding point.*

$$
W_{i j k l}(\cdot)
$$

---

(CP<sup>2</sup>,g<sub>FS</sub>), the Fubini-Study metric, Ric = 6g.

$$
\left(\mathbb{C}\mathbb{P}^2,g_{FS}\right)
$$

$$
Ric=6g
$$

Torus action:

$$
[z_{0},z_{1},z_{2}]\mapsto[z_{0},e^{i\theta_{1}}z_{1},e^{i\theta_{2}}z_{2}].
$$

Flip symmetry:

$$
[z_{0},z_{1},z_{2}]\mapsto[z_{0},z_{2},z_{1}].
$$

---

[0,0,1]
[1,0,0] [0,1,0]

Figure: Orbit space of the torus action on CP<sup>2</sup>.

$$
\mathbb{C P}^{2}
$$

---

(S<sup>2</sup> × S<sup>2</sup>,g<sub>S</sub>2×S2), the product of 2-dimensional spheres of
Gaussian curvature 1, *Ric* = *g.*

$$
(S^{2}\times S^{2},g_{S^{2}\times S^{2}})
$$

Torus action:

Product of rotations fixing north and south poles.

Flip symmetry:

$$
(p_{1},p_{2})\mapsto(p_{2},p_{1}).
$$

---

(s,n) (s,s)
(n,n) (n,s)

Figure: Orbit space of the torus action on S<sup>2</sup> × S<sup>2</sup>.

$$
S^{2}\times S^{2}
$$

---

Recall the mass of an AF space is defined by
∫

$$
\mathrm{mass}(g_{N})=\lim_{R\rightarrow\infty}\omega_{3}^{-1}\int_{S(R)}\sum_{i,j}(\partial_{i}g_{i j}-\partial_{j}g_{i i})(\partial_{i}\lrcorner d V),
$$

with ω<sub>3</sub> = Vol(S<sup>3</sup>).

$$
\omega_{3}=Vol(S^{3})
$$

The Green’s function metric of the Fubini-Study metric ĝ<sub>FS</sub> is also
known as the Burns metric, and is completely explicit, with mass
given by

$$
\hat{g}_{FS}
$$

$$
\mathrm{mass}(\hat{g}_{FS})=2.
$$

---

Mass of Green’s function metric

However, the Green’s function metric ĝ<sub>S</sub>2×S2 of the product metric
does not seem to have a known explicit description. We will denote

$$
\hat{g}_{S^{2}\times S^{2}}
$$

$$
m_{1}=\operatorname{mass}(\hat{g}_{S^{2}\times S^{2}}).
$$

By the positive mass theorem of Schoen-Yau, *m<sub>1</sub>* > 0. Note that
since *S<sup>2</sup> × S<sup>2</sup>* is spin, this also follows from Witten’s proof of the
positive mass theorem.

$$
\mathsf{\cdot Y a u},\:m_{1}>0
$$

$$
S^{2}\times S^{2}
$$

### Remark

*For the curious, the mass m<sub>1</sub> =.5872...., which implies that*
(−9m<sub>1</sub>)<sup>−1</sup> = −.1892.....

$$
m_{1}=.5872....,
$$

$$
(-9m_{1})^{-1}=-.1892
$$

---

*•* We impose the toric symmetry and “flip” symmetry in order
to reduce the number of free parameters to 1 (only the scaling
parameter). That is, we perform an equivariant gluing.

*•* The special value of *t<sub>0</sub>* is computed by

$$
t_{0}
$$

$$
\frac{2}{3}W\left(z_{0}\right)\circledast W\left(y_{0}\right)+4t_{0}R\left(z_{0}\right)\mathrm{mass}\left(g_{N}\right)=0.
$$

*•* This choice of *t<sub>0</sub>* makes the leading term of the Kuranishi
map vanish, and is furthermore a *nondegenerate* zero (if
R(z<sub>0</sub>) > 0; mass(g<sub>N</sub>) > 0 by the positive mass theorem).

$$
t_{0}
$$

$$
R(z_{0})>0;\quad\operatorname{mass}(g_{N})>0
$$

---

## First case

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| \(\mathbb{CP}^{2}\)#\(\overline{\mathbb{CP}}^{2}\) | -1/3 |

$$
\overline{\mathbb{C}\mathbb{P}^2\#\overline{\mathbb{C}\mathbb{P}}^2}
$$

*•* The compact metric is the Fubini-Study metric, with a Burns
AF metric glued on, a computation yields *t<sub>0</sub>* = −1/3.

---

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| \(S^{2} × S^{2} \# \overline{\mathbb{C}P}^{2} = \mathbb{C}P^{2} \# 2 \overline{\mathbb{C}P}^{2}\) | -1/3, -(9m_{1})^{-1} |

$$
\overline{\mathsf{V}\mathsf{a}\mathsf{l}\mathsf{u}\mathsf{e}(\mathsf{s})}
$$

$$
S^{2}\times S^{2}\#\overline{\mathbb{C}}\overline{\mathbb{P}}^{2}=\mathbb{C}\mathbb{P}^{2}\#2\overline{\mathbb{C}}\overline{\mathbb{P}}^{2}
$$

$$
-1/3,-(9m_1)^{-1}
$$

• The compact metric is the product metric on S<sup>2</sup> × S<sup>2</sup>, with a
Burns AF metric glued on, this gives *t<sub>0</sub>* = −1/3.

$$
S^{2}\times S^{2}
$$

$$
t_{0}=-1/3
$$

• Alternatively, take the compact metric to be (CP<sup>2</sup>,g<sub>FS</sub>), with
a Green’s function *S<sup>2</sup> × S<sup>2</sup>* metric glued on. In this case,
t<sub>0</sub> = −(9m<sub>1</sub>)<sup>−1</sup>.

$$
\left(\mathbb{C}\mathbb{P}^2,g_{FS}\right)
$$

$$
S^{2}\times S^{2}
$$

$$
t_{0}=-(9m_{1})^{-1}
$$

---

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| 2#S2 × S2 | -2(9m1)-1 |

$$
\overline{\mathsf{V}\mathsf{a}\mathsf{l}\mathsf{u}\mathsf{e}(\mathsf{s})}
$$

$$
\overline{2\#S^{2}\times S^{2}}
$$

$$
\overline{-2(9m_{1})^{-1}}
$$

• The compact metric is the product metric on S<sup>2</sup> × S<sup>2</sup>, with a
Green’s function *S<sup>2</sup> × S<sup>2</sup>* metric glued on. In this case,
t<sub>0</sub> = −2(9m<sub>1</sub>)<sup>−1</sup>.

$$
S^{2}\times S^{2}
$$

$$
S^{2}\times S^{2}
$$

$$
t_{0}=-2(9m_{1})^{-1}
$$

---

## Technical Points

• Ellipticity and gauging. The B<sup>t</sup>-flat equations are not elliptic
due to diffeomorphism invariance. A gauging procedure
analogous to the Bianchi gauge is used.

$$
B^{t}
$$

• Rigidity of g<sub>FS</sub> and g<sub>S</sub>2×S2. Follows from the formulas
discussed at the beginning of today’s lecture, together with
some eigenvalue estimates.

$$
g_{S^{2}\times S^{2}}
$$

*•* Refined approximate metric. The approximate metric
described above is not good enough. It must be improved by
matching up leading terms of the metrics by solving certain
auxiliary linear equations, so that the cutoff function
disappears from the leading term. We will not have time to
discuss this today.

---

## Ellipticity and gauging

The linearized operator of the B<sup>t</sup>-flat equation is not elliptic, due
to diffeomorphism invariance. However, consider the “gauged”
nonlinear map *P* given by

$$
B^{t_{1}}
$$

$$
P_{g}(\theta)=(B+t C)(g+\theta)+\mathcal{K}_{g+\theta}[\delta_{g}\mathcal{K}_{g}\delta_{g}\stackrel{\circ}{\theta}].
$$

Let S<sup>t</sup> ≡ P <sup>′</sup>(0) denote the linearized operator at θ = 0.

$$
S^{t}\equiv P^{\prime}(0)
$$

$$
\theta=0
$$

### Proposition

If t 6= 0, then S<sup>t</sup> is elliptic. Furthermore, if P(θ) = 0, and
∞
θ ∈ C<sup>4,α</sup> for some 0 < α < 1, then B<sup>t</sup>(g + θ) = 0 and θ ∈ C.

$$
If t\neq0
$$

$$
S^{t}
$$

$$
P(\theta)=0
$$

$$
\theta\in C^{4,\alpha}
$$

$$
0<\alpha<1
$$

$$
B^{t}(g+\theta)=0
$$

$$
\theta\in C^{\infty}
$$

• Proof is an integration-by-parts. It is crucial that the B<sup>t</sup>-flat
equations are variational (recall B<sub>t</sub> is the functional), so
δB<sup>t</sup> = 0. Equivalent to diffeomorphism invariance of B<sub>t</sub>.

$$
B^{t}-\mathsf{f}\mathsf{l}\mathsf{a}\mathsf{t}
$$

$$
\mathcal{B}_{t}
$$

$$
\delta B^{t}=0
$$

$$
\mathcal{B}_{t}
$$

---

## Rigidity

For *h* transverse-traceless (TT), the linearized operator at an
Einstein metric is given by

$$
h
$$

$$
S^{t}h=\Big(\Delta_{L}+\frac{1}{2}R\Big)\Big(\Delta_{L}+\Big(\frac{1}{3}+t\Big)R\Big)h,
$$

where ∆<sub>L</sub> is the Lichnerowicz Laplacian, defined by

$$
\Delta_{L}
$$

$$
\Delta_{L}h_{i j}=\Delta h_{i j}+2R_{i p j q}h^{p q}-\frac{1}{2}R h_{i j}.
$$

*•* Recall that infinitesimal Einstein deformations given by TT
kernel of the operator ∆<sub>L</sub> + <sup>1</sup><sub>2</sub>R. We still have those, but
there are now more possibilities of deformations.

$$
\Delta_{L}+\tfrac{1}{2}R
$$

---

## Rigidity

For *h* = *fg,* we have

$$
h=f g
$$

$$
t r_{g}(S^{t}h)=6t(3\Delta+R)(\Delta f).
$$

(1)

The rigidity question is then reduced to a separate analysis of the
eigenvalues of ∆<sub>L</sub> on transverse-traceless tensors, and of ∆ on
functions.

$$
\Delta_{L}
$$

$$
\Delta\text{on}
$$

### Theorem (Gursky-V)

On (CP<sup>2</sup>,g<sub>FS</sub>), H<sup>1</sup><sub>t</sub> = {0} provided that t < 1.

$$
(\mathbb{C P}^{2},g_{F S}),H_{t}^{1}=\{0\}
$$

$$
t<1
$$

### Theorem (Gursky-V)

On (S<sup>2</sup> × S<sup>2</sup>,g<sub>S</sub>2×S2), H<sup>1</sup><sub>t</sub> = {0} provided that t < 2/3 and
t 6= −1/3. If t = −1/3, then H<sup>1</sup><sub>t</sub> is one-dimensional and spanned
*by the element g<sub>1</sub> − g<sub>2</sub>.*

$$
(S^{2}\times S^{2},g_{S^{2}\times S^{2}}),H_{t}^{1}=\{0\}
$$

$$
t<2/3
$$

$$
t\neq-1/3
$$

$$
t=-1/3
$$

$$
H_{t}^{1}
$$

$$
g_{1}-g_{2}
$$

---

## Rigidity

*•* Positive mass theorem says that *t<sub>0</sub>* < 0, so luckily we are in
the rigidity range of the factors.

$$
t_{0}<0
$$

*•* Gauge term is carefully chosen so that solutions of the
linearized equation must be in the transverse-traceless gauge.
That is, if S<sup>t</sup>h = 0 then

$$
S^{t}h=0
$$

$$
(B^{t})'(h)+\mathcal{K}\delta\mathcal{K}\delta\stackrel{\circ}{h}=0
$$

implies that separately,

$$
(B ^ {t}) ^ {\prime} (h) = 0 \text {a n d} \delta^ {\circ} h = 0.
$$

---

## Final remarks

The proof shows that there is a dichotomy. Either

*•* (i) there is a critical metric at exactly the critical *t<sub>0</sub>,* in which
case there would necessarily be a 1-dimensional moduli space
of solutions for this fixed *t<sub>0</sub>,* or

$$
t_{0}
$$

*•* (ii) for each value of the gluing parameter *a* sufficiently small,
there will be a critical metric for a corresponding value of
*t<sub>0</sub>* = *t<sub>0</sub>(a).* The dependence of *t<sub>0</sub>* on *a* will depend on the
next term in the expansion of the Kuranishi map.

$$
t_{0}=t_{0}(a)
$$

$$
t_{0}
$$

*•* Which case actually happens?