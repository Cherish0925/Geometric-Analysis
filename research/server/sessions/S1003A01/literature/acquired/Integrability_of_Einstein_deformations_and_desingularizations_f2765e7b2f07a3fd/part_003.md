---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Integrability of Einstein deformations and desingularizations]

=
2
−
d
2
∫
{
r
<
t
1
/
4
}
R
e
(
2
)
H
2
,
H
4
d
v
e
.
$$\begin{align*} \int _{\lbrace r=t^{1/4}\rbrace }& {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}\left(H_2,H^4\right)\right)}(r\partial _r,\partial _r) dv_{t^{1/4}\mathbb {S}^3\slash \mathbb {Z}_2} = \frac{2-d}{2}\int _{\lbrace r&lt;t^{1/4}\rbrace } \operatorname{\operatorname{R}}^{(2)}_{\bm{e}}\left(H_2,H^4\right) dv_{\bm{e}}. \end{align*}$$
Now, by Corollary
4.7
proven below, one has
R
e
(
2
)
(
H
2
,
H
4
)
=
0
$\operatorname{\operatorname{R}}^{(2)}_{\bm{e}}(H_2,H^4) = 0$
because
H
4
is anti-selfdual, and we recover the obstruction (
36
) in this situation. The other obstructions with Killing vector fields are recovered in the same way.
Remark 3.11.
The coordinates of (
42
) correspond to the
volume gauge
of Definition
4.12
below and one of their properties is that the vector field
r
∂
r
$r\partial _r$
is harmonic, hence
L
r
∂
r
eh
$\mathcal {L}_{r\partial _r}\bm{eh}$
is an infinitesimal Einstein deformation – up to a trace term.
4 THE 4-DIMENSIONAL SITUATION
Let us now specialize our discussion to the dimension
d
=
4
$d=4$
where most of our applications are. In this section, we will test the obstruction to the integrability of infinitesimal Einstein deformations on the development of Einstein 4-manifolds at the infinity of a Ricci-flat ALE metric. See Appendix
A
for the case of a neighborhood of a given point of an Einstein manifold or orbifold. We will see that the obstructions
always
vanish and do not add any restriction.
In order to show this, we will prove the existence of good gauges in which the quadratic term of
h
↦
Ric
(
e
+
h
)
$h\mapsto \operatorname{\operatorname{Ric}}(\bm{e}+h)$
are easily computable. This is an important step towards the next Section
5
where obstructions to the desingularization of some Einstein metrics are found.
4.1 Notations
In dimension 4, the space of 2-forms decomposes into selfdual and anti-selfdual 2-forms which are elements of the eigenspaces of Hodge star operator * (which satisfies
∗
2
=
Id
$*^2 = \mbox{Id}$
) respectively associated to the eigenvalues 1 and −1. We denote
Ω
+
$\Omega ^+$
and
Ω
−
$\Omega ^-$
the associated eigenspaces.
Denote
(
x
1
,
x
2
,
x
3
,
x
4
)
$(x_1,x_2,x_3,x_4)$
coordinates in an orthonormal basis of
R
4
$\mathbb {R}^4$
. We define the 2-forms
ω
1
±
:
=
d
x
1
∧
d
x
2
±
d
x
3
∧
d
x
4
$$\begin{equation*} \omega ^\pm _1 := dx^1\wedge dx^2\pm dx^3\wedge dx^4 \end{equation*}$$
and similarly
ω
2
±
$\omega _2^\pm$
and
ω
3
±
$\omega _3^\pm$
by cyclic permutations of the indices
{
2
,
3
,
4
}
$\lbrace 2,3,4\rbrace$
. The
ω
i
+
$\omega _i^+$
form an orthogonal basis of the space of selfdual 2-forms,
Ω
+
$\Omega ^+$
, and the
ω
i
−
$\omega _i^-$
form an orthogonal basis of the space of anti-selfdual 2-forms,
Ω
−
$\Omega ^-$
.
Thanks to them, we define the following basis of the Killing vector fields preserving 0 on
R
4
$\mathbb {R}^4$
:
Y
i
±
:
=
ω
i
±
(
r
∂
r
)
.
$$\begin{equation} Y_i^\pm := \omega _i^\pm (r\partial _r). \end{equation}$$
(44)
The other Killing vector fields of
R
4
$\mathbb {R}^4$
are given by constant vector fields representing translations. Note that those will not be Γ-invariant for any
Γ
⊂
S
O
(
4
)
$\Gamma \subset SO(4)$
with
Γ
≠
{
Id
}
$\Gamma \ne \lbrace \operatorname{\operatorname{Id}}\rbrace$
.
In each orientation, the frame
(
r
∂
r
,
Y
1
±
,
Y
2
±
,
Y
3
±
)
$(r\partial _r,Y_1^\pm ,Y_2^\pm ,Y_3^\pm )$
is dual to the coframe
(
d
r
/
r
,
α
1
±
,
α
2
±
,
α
3
±
)
$ (dr/r,\alpha _1^\pm ,\alpha _2^\pm ,\alpha _3^\pm )$
where we define
α
i
±
:
=
ω
i
±
(
d
r
/
r
)
$\alpha _i^\pm :=\omega _i^\pm (dr/r)$
. We also define the following 2-forms which also form bases of the spaces of selfdual or anti-selfdual 2-forms:
θ
1
∓
:
=
r
d
r
∧
α
1
±
∓
r
2
α
2
±
∧
α
3
±
,
$$\begin{equation*} \theta _1^\mp := r dr\wedge \alpha _1^\pm \mp r^2\alpha _2^\pm \wedge \alpha _3^\pm , \end{equation*}$$
and similarly
θ
2
∓
$\theta _2^\mp$
and
θ
3
∓
$\theta _3^\mp$
by cyclic permutations.
Remark 4.1.
The notation
θ
i
+
$\theta _i^+$
meant something else in [
39
].
For the above 2-forms, we have the following formula: for
x
=
(
x
1
,
x
2
,
x
3
,
x
4
)
$x = (x_1,x_2,x_3,x_4)$
θ
i
∓
(
x
)
=
∑
j
=
1
3
x
T
(
ω
i
±
∘
ω
j
∓
)
x
|
x
|
2
ω
j
∓
=
−
⟨
Y
i
±
,
Y
j
∓
⟩
r
2
ω
j
∓
,
$$\begin{align} \theta _i^\mp (x) = \sum _{j=1}^3 \frac{x^T(\omega _i^\pm \circ \omega _j^\mp )x}{|x|^2}\omega _j^\mp =- \frac{\langle Y_i^\pm , Y_j^\mp \rangle }{r^2}\omega _j^\mp ,\end{align}$$
(45)
where
ω
i
±
∘
ω
j
∓
$ \omega _i^\pm \circ \omega _j^\mp$
is the symmetric traceless matrix given by the (commuting) product of the antisymmetric matrices associated to
ω
i
±
$\omega _i^\pm$
and
ω
j
∓
$\omega _j^\mp$
, and where
x
T
$x^T$
is the transpose of
x
. We also have the following equalities:
ω
1
±
=
r
d
r
∧
α
1
±
±
r
2
α
2
±
∧
α
3
±
$\omega _1^\pm = r dr\wedge \alpha _1^\pm \pm r^2\alpha _2^\pm \wedge \alpha _3^\pm$
and similar equalities for
ω
i
±
$\omega _i^\pm$
for
i
∈
{
2
,
3
}
$i \in \lbrace 2,3\rbrace$
by cyclic permutations.
4.1.1 Orbifolds and ALE spaces
We will be interested in two types of geometries: Einstein orbifolds and Ricci-flat ALE metrics. They respectively correspond to the singular limits and the singularity models of the degeneration of Einstein 4-manifolds.
Definition 4.2. (Orbifold [with isolated singularities])
We will say that a metric space
(
M
o
,
g
o
)
$(M_o,g_o)$
is an orbifold of dimension
d
⩾
2
$d\geqslant 2$
if there exists
ε
0
>
0
$\epsilon _0&gt;0$
and a finite number of points
(
p
k
)
k
$(p_k)_k$
of
M
o
$M_o$
called
singular
such that we have the following properties:
(1)
the space
(
M
o
∖
{
p
k
}
k
,
g
o
)
$(M_o\backslash \lbrace p_k\rbrace _k,g_o)$
is a manifold of dimension
d
,
(2)
for each singular point
p
k
$p_k$
of
M
o
$M_o$
, there exists a neighborhood of
p
k
$p_k$
,
U
k
⊂
M
o
$ U_k\subset M_o$
, a finite subgroup acting freely on
S
d
−
1
$\mathbb {S}^{d-1}$
,
Γ
k
⊂
S
O
(
n
)
$\Gamma _k\subset SO(n)$
, and a diffeomorphism
Φ
k
:
B
e
(
0
,
ε
0
)
⊂
R
d
∕
Γ
k
→
U
k
⊂
M
o
$ \Phi _k: B_{\bm{e}}(0,\epsilon _0)\subset \mathbb {R}^d\slash \Gamma _k \rightarrow U_k\subset M_o$
for which, the pull-back of
Φ
k
∗
g
o
$\Phi _k^*g_o$
on the covering
R
d
$\mathbb {R}^d$
is smooth.
Remark 4.3.
Note that smooth Einstein metrics are Einstein orbifolds. Einstein orbifold metrics are smooth up to taking a finite local cover at the singular point as seen in [
8
].
Definition 4.4. (ALE orbifold [with isolated singularities])
An ALE orbifold of dimension
d
⩾
4
$d\geqslant 4$
,
(
N
,
g
b
)
$(N,g_b)$
is a metric space for which there exists
ε
0
>
0
$\epsilon _0&gt;0$
, singular points
(
p
k
)
k
$(p_k)_k$
and a compact
K
⊂
N
$K\subset N$
for which we have:
(1)
(
N
,
g
b
)
$(N,g_b)$
is an orbifold of dimension
d
,
(2)
there exists a diffeomorphism
Ψ
∞
:
(
R
d
∕
Γ
∞
)
∖
B
e
(
0
,
ε
0
−
1
)
¯
→
N
∖
K
$\Psi _\infty : (\mathbb {R}^d\slash \Gamma _\infty )\backslash \overline{B_{\bm{e}}(0,\epsilon _0^{-1})} \rightarrow N\backslash K$
such that we have
r
l
|
∇
l
(
Ψ
∞
∗
g
b
−
e
)
|
e
⩽
C
l
r
−
d
$r^l|\nabla ^l(\Psi _\infty ^* g_b - \bm{e})|_{\bm{e}}\leqslant C_l r^{-d}$
.
Note 4.5.
We will often identify
R
d
∕
Γ
$\mathbb {R}^d\slash \Gamma$
and its cover
R
d
$\mathbb {R}^d$
when writing ALE of orbifold spaces in coordinates.
4.1.2 Curvature of Einstein 4-manifolds
Thanks to the direct sum of selfdual and anti-selfdual 2-forms, the symmetric endomorphism on 2-forms,
R
given by the Riemannian curvature decomposes into blocks,
R
=
:
R
+
Ric
˚
Ric
˚
R
−
,
$$\begin{equation*} \bm{R}=: \def\eqcellsep{&}\begin{bmatrix} \bm{R}^+ & \mathring{\operatorname{\operatorname{Ric}}} \\  \mathring{\operatorname{\operatorname{Ric}}} & \bm{R}^- \end{bmatrix}, \end{equation*}$$
where the
Ric
˚
$\mathring{\operatorname{\operatorname{Ric}}}$
is the traceless part of the Ricci curvature, and where
R
±
are the selfdual and anti-selfdual parts of the curvature.
Let us do a quick recap on the curvature of Einstein perturbations of the Euclidean space
(
R
4
,
e
)
$(\mathbb {R}^4,\bm{e})$
. The starting point is the identification of the set of traceless symmetric 2-tensors
Sym
0
2
T
M
$\mbox{Sym}_0^2TM$
with
Ω
+
⊗
Ω
−
$\Omega ^+\otimes \Omega ^-$
thanks to the map:
ω
+
⊗
ω
−
∈
Ω
+
⊗
Ω
−
↦
ω
+
∘
ω
−
=
ω
−
∘
ω
+
∈
Sym
0
2
T
M
$$\begin{equation*} \omega ^+\otimes \omega ^-\in \Omega ^+\otimes \Omega ^- \mapsto \omega ^+\circ \omega ^- =\omega ^-\circ \omega ^+\in \mbox{Sym}_0^2TM \end{equation*}$$
where
ω
+
∘
ω
−
$\omega ^+\circ \omega ^-$
is the 2-tensor associated to the composition of the anti-symmetric endomorphisms of
T
M
$TM$
associated to
ω
+
$\omega ^+$
and
ω
−
$\omega ^-$
by the metric. Therefore, any 2-tensor
h
on
(
R
4
,
e
)
$(\mathbb {R}^4,\bm{e})$
has unique decompositions:
h
=
λ
e
+
∑
i
ϕ
i
−
∘
ω
i
+
=
λ
e
+
∑
j
ϕ
j
+
∘
ω
j
−
$$\begin{equation*} h = \lambda \bm{e} + \sum _i \phi _i^-\circ \omega _i^+ =\lambda \bm{e} + \sum _j \phi _j^+\circ \omega _j^- \end{equation*}$$
for a scalar function λ, and the
ϕ
i
±
$\phi _i^\pm$
with values in
Ω
±
$\Omega ^\pm$
. According to [
12
], the Bianchi gauge condition for
h
rewrites:
d
λ
+
∑
i
=
1
3
∗
ω
i
+
∧
(
∗
d
ϕ
i
−
)
=
d
λ
+
∑
j
=
1
3
∗
ω
j
−
∧
(
∗
d
ϕ
j
+
)
=
0
.
$$\begin{equation} d\lambda + \sum _{i= 1}^3*{\left(\omega _i^+\wedge (*d\phi _i^-)\right)} = d\lambda + \sum _{j= 1}^3*{\left(\omega _j^-\wedge (*d\phi _j^+)\right)} = 0. \end{equation}$$
(46)
Extending the computations of [
12
], we prove the following result.
Proposition 4.6.
Let
h
be a symmetric 2-tensor on
R
4
$\mathbb {R}^4$
decomposed as:
h
=
λ
e
+
∑
i
ϕ
i
−
∘
ω
i
+
=
λ
e
+
∑
j
ϕ
j
+
∘
ω
j
−
$$\begin{equation*} h = \lambda \bm{e} + \sum _i \phi _i^-\circ \omega _i^+ =\lambda \bm{e} + \sum _j \phi _j^+\circ \omega _j^- \end{equation*}$$
and satisfying the condition (
46
).
Then, defining
a
e
+
,
(
1
)
(
h
)
=
∑
i
∗
d
ϕ
i
−
⊗
ω
i
+
$a^{+,(1)}_{\bm{e}}(h) = \sum _i*d\phi _i^-\otimes \omega _i^+$
and
a
e
−
,
(
1
)
(
h
)
=
∑
j
∗
d
ϕ
j
+
⊗
ω
j
−
$a^{-,(1)}_{\bm{e}}(h) = \sum _j*d\phi _j^+\otimes \omega _j^-$
the infinitesimal variations of connections, see [
12
,
21
], we have:
R
e
+
,
(
1
)
(
h
)
=
−
d
+
a
e
+
,
(
1
)
(
h
)
=
−
∑
i
d
+
∗
d
ϕ
i
−
⊗
ω
i
+
$\bm{R}^{+,(1)}_{\bm{e}}(h) = -d_+a^{+,(1)}_{\bm{e}}(h) = -\sum _{i} d_+*d\phi _i^-\otimes \omega _i^+$
where
d
+
$d_+$
is the exterior differential composed with the projection on
Ω
+
$\Omega ^+$
,
R
e
−
,
(
1
)
(
h
)
=
−
d
−
a
e
−
,
(
1
)
(
h
)
=
−
∑
i
d
−
∗
d
ϕ
i
+
⊗
ω
i
−
$\bm{R}^{-,(1)}_{\bm{e}}(h) = -d_-a^{-,(1)}_{\bm{e}}(h) = -\sum _{i} d_-*d\phi _i^+\otimes \omega _i^-$
where
d
−
$d_-$
is the exterior differential composed with the projection on
Ω
−
$\Omega ^-$
, and
Ric
˚
e
(
1
)
(
h
)
=
d
−
a
e
+
,
(
1
)
(
h
)
=
d
+
a
e
−
,
(
1
)
(
h
)
$\mathring{\operatorname{\operatorname{Ric}}}^{(1)}_{\bm{e}}(h) = d_-a^{+,(1)}_{\bm{e}}(h)= d_+a^{-,(1)}_{\bm{e}}(h)$
and in particular,
h
is an infinitesimal Einstein deformation if and only if for all
i
∈
{
1
,
2
,
3
}
$i\in \lbrace 1,2,3\rbrace$
,
d
−
∗
d
ϕ
i
−
=
0
$d_-*d\phi _i^-=0$
or equivalently if and only if for all
j
∈
{
1
,
2
,
3
}
$j\in \lbrace 1,2,3\rbrace$
,
d
+
∗
d
ϕ
j
+
=
0
$d_+*d\phi _j^+=0$
.
Moreover, if
h
is an infinitesimal Einstein deformation, then we have:
R
e
+
,
(
2
)
(
h
,
h
)
=
−
1
2
[
a
e
+
,
(
1
)
(
h
)
,
a
e
+
,
(
1
)
(
h
)
]
+
$\bm{R}^{+,(2)}_{\bm{e}}(h,h) =- \frac{1}{2}[a_{\bm{e}}^{+,(1)}(h),a_{\bm{e}}^{+,(1)}(h)]_+$
,
R
e
−
,
(
2
)
(
h
,
h
)
=
−
1
2
[
a
e
−
,
(
1
)
(
h
)
,
a
e
−
,
(
1
)
(
h
)
]
−
$\bm{R}^{-,(2)}_{\bm{e}}(h,h) =- \frac{1}{2}[a_{\bm{e}}^{-,(1)}(h),a_{\bm{e}}^{-,(1)}(h)]_-$
and
defining linear maps
ϕ
−
:
Ω
+
→
Ω
−
$\phi ^- : \Omega ^+\rightarrow \Omega ^-$
and
ϕ
+
:
Ω
−
→
Ω
+
$\phi ^+ : \Omega ^-\rightarrow \Omega ^+$
by for any
i
and
j
in
{
1
,
2
,
3
}
$\lbrace 1,2,3\rbrace$
,
ϕ
−
(
ω
i
+
)
=
ϕ
i
−
$ \phi ^-(\omega _i^+) = \phi _i^-$
and
ϕ
+
(
ω
j
−
)
=
ϕ
j
+
$ \phi ^+(\omega _j^-) = \phi _j^+$
, we have
Ric
˚
e
(
2
)
(
h
,
h
)
=
1
2
a
e
+
,
(
1
)
(
h
)
,
a
e
+
,
(
1
)
(
h
)
−
+
∑
i
ϕ
−
R
e
+
,
(
1
)
(
h
)
(
ω
i
+
)
⊗
ω
i
+
=
1
2
a
e
−
,
(
1
)
(
h
)
,
a
e
−
,
(
1
)
(
h
)
+
+
∑
j
ϕ
+
R
e
−
,
(
1
)
(
h
)
(
ω
j
−
)
⊗
ω
j
−
.
$$\begin{align*} \mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(h,h) &= \frac{1}{2}{\left[a_{\bm{e}}^{+,(1)}(h),a_{\bm{e}}^{+,(1)}(h)\right]}_- +\sum _i\phi ^-{\left(\bm{R}^{+,(1)}_{\bm{e}}(h)(\omega _i^+)\right)}\otimes \omega _i^+\\ &=\frac{1}{2}{\left[a_{\bm{e}}^{-,(1)}(h),a_{\bm{e}}^{-,(1)}(h)\right]}_+ +\sum _j\phi ^+{\left(\bm{R}^{-,(1)}_{\bm{e}}(h)(\omega _j^-)\right)}\otimes \omega _j^-. \end{align*}$$
Proof.
The only points that are not proven in [
12
] are the values of
R
e
±
,
(
2
)
(
h
,
h
)
$\bm{R}^{\pm ,(2)}_{\bm{e}}(h,h)$
. For this, we recall that
R
+
is the opposite of the selfdual part of the curvature
d
a
+
+
1
2
[
a
+
,
a
+
]
$d a^+ + \frac{1}{2}[a^+,a^+]$
of the bundle
Ω
+
$\Omega ^+$
. The origin of the term
−
1
2
[
a
e
+
,
(
1
)
(
h
)
,
a
e
+
,
(
1
)
(
h
)
]
+
$- \frac{1}{2}[a_{\bm{e}}^{+,(1)}(h),a_{\bm{e}}^{+,(1)}(h)]_+$
is therefore clear. There is another source of variation of
R
+
which are the variations of
Ω
+
$\Omega ^+$
and
Ω
−
$\Omega ^-$
at
e
in the direction
h
=
λ
e
+
∑
i
ϕ
i
−
∘
ω
i
+
=
λ
e
+
∑
j
ϕ
j
+
∘
ω
j
−
$h = \lambda \bm{e} + \sum _i \phi _i^-\circ \omega _i^+=\lambda \bm{e} + \sum _j \phi _j^+\circ \omega _j^-$
. According to [
12
], by blocks given by the direct sum
Ω
e
+
⊕
Ω
e
−
$\Omega ^+_{\bm{e}}\oplus \Omega ^-_{\bm{e}}$
, the variation of the bases
(
ω
i
±
)
i
$(\omega _i^\pm )_i$
as bases of
Ω
±
$\Omega ^\pm$
rewrites:
ω
i
,
e
±
,
(
1
)
(
h
)
=
λ
−
ϕ
−
−
ϕ
+
λ
ω
i
+
,
$$\begin{equation} \omega _{i,\bm{e}}^{\pm ,(1)}(h)=\def\eqcellsep{&}\begin{bmatrix} \lambda & -\phi ^{-}\\  -\phi ^+& \lambda  \end{bmatrix}\omega _i^+, \end{equation}$$
(47)
and therefore, the conjugation by
Id
+
λ
−
ϕ
−
−
ϕ
+
λ
+
O
(
|
h
|
e
2
)
$ \mbox{Id}+\def\eqcellsep{&}\begin{bmatrix} \lambda & -\phi ^{-}\\  -\phi ^+& \lambda  \end{bmatrix} +\mathcal {O}(|h|_{\bm{e}}^2)$
of the first order curvature variation
R
e
+
,
(
1
)
(
h
)
0
0
R
e
−
,
(
1
)
(
h
)
$ \def\eqcellsep{&}\begin{bmatrix} \bm{R}^{+,(1)}_{\bm{e}}(h)&0\\  0&\bm{R}^{-,(1)}_{\bm{e}}(h) \end{bmatrix}$
leaves at second order term:
0
ϕ
−
(
R
e
+
,
(
1
)
(
h
)
)
ϕ
+
(
R
e
−
,
(
1
)
(
h
)
)
0
$ \def\eqcellsep{&}\begin{bmatrix} 0 &\phi ^{-}(\bm{R}^{+,(1)}_{\bm{e}}(h))\\  \phi ^{+}(\bm{R}^{-,(1)}_{\bm{e}}(h))&0 \end{bmatrix}$
, which yields the result.
□
$\Box$
4.1.3 An application to the variation of scalar curvature
Let
h
=
λ
e
+
∑
i
ϕ
i
−
∘
ω
i
+
$h = \lambda \bm{e} + \sum _i \phi _i^-\circ \omega _i^+$
and
k
=
μ
e
+
∑
i
ψ
i
−
∘
ω
i
+
$k=\mu \bm{e} + \sum _i \psi _i^-\circ \omega _i^+$
for λ and μ scalar functions and
ϕ
i
−
,
ψ
i
−
∈
Ω
−
$\phi _i^-,\psi _i^-\in \Omega _-$
.
Corollary 4.7.
Assume that
h
and
k
are infinitesimal Einstein deformations satisfying (
46
) and assume moreover that
h
is anti-selfdual in the sense that
a
e
+
,
(
1
)
(
h
)
=
0
$a^{+,(1)}_{\bm{e}}(h)=0$
.
Then, we have:
R
e
+
,
(
2
)
(
h
,
k
)
=
0
$\bm{R}_{\bm{e}}^{+,(2)}(h,k)=0$
, and moreover:
Ric
˚
e
(
2
)
(
h
,
k
)
=
∑
i
ϕ
i
−
R
e
+
,
(
1
)
(
k
)
(
ω
i
+
)
⊗
ω
i
+
.
$$\begin{equation} \mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(h,k)= \sum _i \phi _i^-{\left(\bm{R}_{\bm{e}}^{+,(1)}(k)(\omega _i^+)\right)}\otimes \omega _i^+.\end{equation}$$
(48)
4.2 Asymptotic curvature of 4-dimensional Ricci-flat ALE metrics
Let us now study the infinity of Ricci-flat ALE metrics of dimension 4.
4.2.1 Development of Ricci-flat ALE metrics
Let us start by understanding the asymptotic terms of Ricci-flat ALE metrics.
Let
(
N
,
g
b
)
$ (N,\bm{g}_b)$
be a 4-dimensional Ricci-flat ALE orbifold asymptotic to
(
R
4
∕
Γ
,
e
)
$ (\mathbb {R}^4\slash \Gamma ,\bm{e})$
for
Γ
⊂
S
O
(
4
)
$\Gamma \subset SO(4)$
, and let
(
Σ
s
)
s
>
s
0
$(\Sigma _s)_{s&gt;s_0}$
for some
s
0
>
0
$s_0&gt;0$
be a CMC (Constant Mean Curvature) foliation of
(
N
,
g
b
)
$ (N,\bm{g}_b)$
in a neighborhood of infinity as in [
14
,
16
] where the mean curvature of
Σ
s
$\Sigma _s$
is equal to
3
s
$\frac{3}{s}$
(like a sphere of radius
s
in
(
R
4
∕
Γ
,
e
)
$(\mathbb {R}^4\slash \Gamma ,\bm{e})$
).
Definition 4.8. (CMC gauge)
Then, by [
14
] there exist a compact
K
⊂
N
$K\subset N$
,
s
0
>
0
$s_0&gt;0$
and a diffeomorphism:
Φ
:
(
R
4
∖
B
e
(
0
,
s
0
)
)
∕
Γ
↦
N
∖
K
$\Phi : (\mathbb {R}^4\backslash B_{\bm{e}}(0,s_0))\slash \Gamma \mapsto N\backslash K$
with:
for all
s
>
s
0
$s&gt;s_0$
,
Φ
(
S
e
(
s
)
)
=
Σ
s
$\Phi (S_{\bm{e}}(s)) = \Sigma _s$
,
Φ
∗
g
b
−
e
=
H
4
+
O
(
r
−
5
)
$\Phi ^*\bm{g}_b-\bm{e} = H^4 + \mathcal {O}(r^{-5})$
at infinity for
|
H
4
|
e
∼
r
−
4
$|H^4|_{\bm{e}}\sim r^{-4}$
,
δ
e
H
4
=
0
$ \delta _{\bm{e}}H^4 = 0$
,
tr
e
H
4
=
0
$\operatorname{\operatorname{tr}}_{\bm{e}} H^4 = 0$
,
H
4
(
∂
r
,
∂
r
)
=
0
$H^4(\partial _r,\partial _r) = 0$
and
one can even arrange Φ so that
H
4
is more precisely of the form:
H
4
=
∑
i
j
h
i
j
+
θ
i
−
∘
ω
j
+
+
∑
k
l
h
k
l
−
θ
k
+
∘
ω
l
−
r
4
$$\begin{equation*} H^4 = \frac{\sum _{ij}h_{ij}^+\theta _i^-\circ \omega _j^+ + \sum _{kl}h_{kl}^-\theta _k^+\circ \omega _l^-}{r^4} \end{equation*}$$
with
∑
i
h
i
i
+
=
0
$\sum _{i}h_{ii}^+=0$
and
∑
k
h
k
k
−
=
0
$ \sum _{k}h_{kk}^- = 0$
. Up to choosing a different basis of (anti)-selfdual
We call these coordinates a
CMC gauge
.
Remark 4.9.
Instead of that last point, in [
14
], a slightly different decomposition is used in so-called
reduced Kronheimer's terms
which are projections of the terms
θ
i
∓
∘
ω
j
±
$\theta _i^\mp \circ \omega _j^\pm$
on their part without
d
r
$dr$
. Our description is actually equivalent to theirs up to
gauge terms
of the form
L
V
$\mathcal {L}_V$
for
V
=
1
r
4
L
(
x
)
$V = \frac{1}{r^4}L(x)$
for a matrix
L
as used in [
14
, (2.14)] to simplify (using a pull-back by a diffeomorphism) a usual
Kronheimer's term
θ
i
∓
∘
ω
j
±
r
4
$\frac{\theta _i^\mp \circ \omega _j^\pm }{r^4}$
like ours into their
reduced Kronheimer's term
. This difference makes the computations of curvatures somewhat simpler here and is more natural for the following volume gauge.
Denote
Ω
s
$\Omega _s$
the interior of the hypersurface
Σ
s
$\Sigma _s$
. The limit:
V
(
N
,
g
b
)
:
=
lim
s
→
∞
Vol
g
b
Ω
s
−
Vol
e
(
B
e
(
s
)
∕
Γ
)
⩽
0
$$\begin{equation} \mathcal {V}(N,\bm{g}_b):=\lim _{s\rightarrow \infty } \operatorname{\operatorname{Vol}}_{\bm{g}_b}\Omega _s - \operatorname{\operatorname{Vol}}_{\bm{e}}(B_{\bm{e}}(s)\slash \Gamma )\leqslant 0 \end{equation}$$
(49)
exists and is called the
renormalized volume
of
(
N
,
g
b
)
$(N,\bm{g}_b)$
in [
14
]. It is vanishing
if and only if
(
N
,
g
b
)
$(N,\bm{g}_b)$
is flat.
Remark 4.10.
An interesting remark of Hans-Joachim Hein is the following. There are examples of Kronheimer's instantons of [
30
] described in Remark
5.8
below for which one has
H
4
=
0
$H^4=0$
in CMC gauge. It is a way to see that the notion of reduced volume is
not
an asymptotic quantity. It essentially does not tell anything about the asymptotics of Ricci-flat ALE metric at infinity which at this point could vanish at any order. It is a global and subtle quantity. This reduced volume is the core quantity of the obstruction (
54
) proven later.
We will also need a particular gauge very close to one introduced by Biquard and Hein in some unpublished notes which led to [
14
]. This is a so-called
volume gauge
in which the volume form of the ALE metric is asymptotically equal to that of the asymptotic flat cone.
Example 4.11.
The volume form of the Eguchi-Hanson metric in its usual form (
42
) is equal to that of the asymptotic cone
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
with its flat metric
d
r
2
+
r
2
(
α
1
2
+
α
2
2
+
α
3
2
)
$dr^2 + r^2 (\alpha _1^2+\alpha _2^2+\alpha _3^2)$
.
Precomposing the above local diffeomorphism Φ of Definition
4.8
with the flow of
r
−
3
∂
r
$r^{-3}\partial _r$
for an adapted amount of time
t
=
C
(
Γ
)
V
(
N
,
g
b
)
$t=C(\Gamma )\mathcal {V}(N,\bm{g}_b)$
for
C
(
Γ
)
>
0
$C(\Gamma )&gt;0$
, one may choose another diffeomorphism Ψ between neighborhoods of infinities with the following properties.
Definition 4.12. (Volume gauge)
There exist a compact
K
′
⊂
N
$K^{\prime }\subset N$
,
r
0
′
>
0
$r^{\prime }_0&gt;0$
and a diffeomorphism:
Ψ
:
(
R
4
∕
Γ
)
∖
B
e
(
0
,
r
0
′
)
↦
N
∖
K
′
$\Psi : (\mathbb {R}^4\slash \Gamma )\backslash B_{\bm{e}}(0,r^{\prime }_0)\mapsto N\backslash K^{\prime }$
with:
Ψ
∗
g
b
−
e
=
H
4
+
O
(
r
−
5
)
$\Psi ^*\bm{g}_b-\bm{e} = H^4 + \mathcal {O}(r^{-5})$
at infinity for
|
H
4
|
e
∼
r
−
4
$|H^4|_{\bm{e}}\sim r^{-4}$
,
Denoting
Ω
s
′
$\Omega ^{\prime }_s$
the interior of
Ψ
∗
(
s
S
3
∕
Γ
)
$\Psi ^*(s\mathbb {S}^3\slash \Gamma )$
,
lim
s
→
∞
Vol
g
b
Ω
s
′
−
Vol
e
(
B
e
(
s
)
∕
Γ
)
=
0
,
$$\begin{equation*} \lim _{s\rightarrow \infty } \operatorname{\operatorname{Vol}}_{\bm{g}_b}\Omega _s^{\prime } - \operatorname{\operatorname{Vol}}_{\bm{e}}(B_{\bm{e}}(s)\slash \Gamma )=0, \end{equation*}$$
δ
e
H
4
=
0
$ \delta _{\bm{e}}H^4 = 0$
,
tr
e
H
4
=
0
$\operatorname{\operatorname{tr}}_{\bm{e}} H^4 = 0$
,
r
4
H
4
(
∂
r
,
∂
r
)
=
c
(
Γ
)
V
(
N
,
g
b
)
$r^4 H^4(\partial _r,\partial _r) =c(\Gamma )\mathcal {V}(N,\bm{g}_b)$
for
c
(
Γ
)
>
0
$c(\Gamma )&gt;0$
.
more precisely,
H
4
=
∑
i
j
h
i
j
+
θ
i
−
∘
ω
j
+
+
∑
k
l
h
k
l
−
θ
k
+
∘
ω
l
−
r
4
$$\begin{equation*} H^4 = \frac{\sum _{ij}h_{ij}^+\theta _i^-\circ \omega _j^+ + \sum _{kl}h_{kl}^-\theta _k^+\circ \omega _l^-}{r^4} \end{equation*}$$
with
∑
i
h
i
i
+
+
∑
k
h
k
k
−
=
c
(
Γ
)
V
(
N
,
g
b
)
⩽
0
$\sum _{i}h_{ii}^+ + \sum _{k}h_{kk}^- = c(\Gamma )\mathcal {V}(N,\bm{g}_b)\leqslant 0$
as in the previous point.
This last point comes from the last point of Definition
4.8
together with the fact that we followed the flow of
r
−
3
∂
r
$r^{-3}\partial _r$
for a time proportional to
V
(
N
,
g
b
)
$\mathcal {V}(N,\bm{g}_b)$
since
−
2
L
r
−
3
∂
r
e
=
1
2
Hess
e
(
r
−
2
)
=
3
d
r
2
−
r
2
g
S
3
r
4
$-2\mathcal {L}_{r^{-3}\partial _r}\bm{e} = \frac{1}{2}\operatorname{\operatorname{Hess}}_{\bm{e}}(r^{-2}) = \frac{3dr^2 - r^2g_{\mathbb {S}^3}}{r^4}$
. Indeed, one only sees the variation of the
r
−
4
$r^{-4}$
terms at this level of precision and they come from a direct integration of the change of the Euclidean metric induced by following the vector field
r
−
3
∂
r
$r^{-3}\partial _r$
.
As in Proposition
A.1
in the Appendix for development of Einstein metrics at a given point, we see the term
H
4
in this volume gauge as only determined by the curvature at infinity and the reduced volume.
Proposition 4.13.
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a non flat Ricci-flat ALE orbifold asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
for
Γ
⊂
S
O
(
4
)
$\Gamma \subset SO(4)$
with reduced volume
V
(
N
,
g
b
)
<
0
$\mathcal {V}(N,\bm{g}_b)&lt;0$
.
Then, in volume gauge as in Definition
4.12
, up to changing the bases
(
ω
i
+
)
i
$(\omega _i^+)_i$
and
(
ω
k
−
)
k
$(\omega _k^-)_k$
to diagonalize the curvature, one has the asymptotic
g
b
=
e
+
H
4
+
O
(
r
−
5
)
$\bm{g}_b = \bm{e} + H^4+\mathcal {O}(r^{-5})$
with
H
4
=
−
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
+
∑
k
h
k
k
−
θ
k
+
∘
ω
l
k
−
r
4
$$\begin{equation} H^4 = -\frac{\sum _{i}h_{ii}^+\theta _i^-\circ \omega _i^+ + \sum _{k}h_{kk}^-\theta _k^+\circ \omega _lk-}{r^4}\end{equation}$$
(50)
and
∑
i
h
i
i
+
+
∑
k
h
k
k
−
=
−
c
(
Γ
)
V
(
N
,
g
b
)
>
0
$\sum _i h_{ii}^+ + \sum _k h_{kk}^- = - c(\Gamma )\mathcal {V}(N,\bm{g}_b)&gt;0$
and the induced asymptotic curvature in the basis
(
θ
i
±
)
i
$(\theta _i^\pm )_i$
satisfies
R
e
∓
,
(
1
)
(
H
4
)
=
8
r
6
2
h
11
±
−
h
22
±
−
h
33
±
0
0
0
−
h
11
±
+
2
h
22
±
−
h
33
±
0
0
0
−
h
11
±
−
h
22
±
+
2
h
33
±
.
$$\begin{equation*} \bm{R}^{\mp ,(1)}_{\bm{e}}(H^4) = \frac{8}{r^6}\def\eqcellsep{&}\begin{bmatrix} 2h^\pm _{11} -h^\pm _{22}-h^\pm _{33}&\quad 0&\quad 0\\[3pt]  0&\quad -h^\pm _{11} +2h^\pm _{22}-h^\pm _{33}&\quad 0\\[3pt]  0&\quad 0\quad &-h^\pm _{11} -h^\pm _{22}+2h^\pm _{33} \end{bmatrix}. \end{equation*}$$
Remark 4.14.
It is possible that the curvature of
(
N
,
g
b
)
$(N,\bm{g}_b)$
is decaying faster than
r
−
6
$r^{-6}$
. In this case, the
H
4
term is purely a gauge term of the form:
1
r
4
∑
i
θ
i
−
∘
ω
i
+
=
1
r
4
∑
k
θ
k
+
∘
ω
k
−
=
3
d
r
2
−
r
2
g
S
3
r
4
=
1
2
Hess
e
(
r
−
2
)
.
$$\begin{equation*} \frac{1}{r^4}\sum _i\theta _i^-\circ \omega _i^+ =\frac{1}{r^4}\sum _k\theta _k^+\circ \omega _k^- = \frac{3 dr^2 - r^2g_{\mathbb {S}^3}}{r^4} = \frac{1}{2}\operatorname{\operatorname{Hess}}_{\bm{e}}(r^{-2}). \end{equation*}$$
See Remark
5.8
below for an example.
Proof.
We first check that
H
+
4
:
=
−
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
r
4
$H^4_+:=-\sum _{i}h_{ii}^+\frac{\theta _i^-\circ \omega _i^+}{r^4}$
only induces anti-selfdual curvature at the first order. The linearization at
e
of the induced connection on
Ω
+
$\Omega ^+$
is actually zero since
d
(
θ
i
+
r
4
)
=
0
$d(\frac{\theta _i^+}{r^4})=0$
and therefore the induced selfdual curvature vanishes as well. This also shows that the term is in Bianchi gauge.
In order to compute the induced curvature, one uses Kronheimer's examples. In particular the curvature of the Eguchi-Hanson metric which with
H
4
=
−
θ
1
−
∘
ω
1
+
2
r
4
$H^4 = -\frac{\theta _1^-\circ \omega _1^+}{2r^4}$
induces the curvature
R
e
∓
,
(
1
)
(
H
4
)
=
4
r
6
2
0
0
0
−
1
0
0
0
−
1
.
$$\begin{equation*} \bm{R}^{\mp ,(1)}_{\bm{e}}(H^4) = \frac{4}{r^6}\def\eqcellsep{&}\begin{bmatrix} 2&0&0\\  0&-1&0\\  0&0&-1 \end{bmatrix}. \end{equation*}$$
by [
20
]. By linearity, one attains any
H
4
as above, and the result follows.
□
$\Box$
In the CMC gauge of Definition
4.8
, we find a simpler expression.
Corollary 4.15.
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE orbifold asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
for
Γ
⊂
S
O
(
4
)
$\Gamma \subset SO(4)$
. Then, in CMC gauge as in Definition
4.8
, up to changing the bases
(
ω
i
+
)
i
$(\omega _i^+)_i$
and
(
ω
k
−
)
k
$(\omega _k^-)_k$
to diagonalize the curvature, one has
g
b
=
e
+
H
4
+
O
(
r
−
5
)
$\bm{g}_b = \bm{e} + H^4+\mathcal {O}(r^{-5})$
with
H
4
=
−
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
+
∑
k
h
k
k
−
θ
k
+
∘
ω
l
k
−
r
4
$$\begin{equation} H^4 = -\frac{\sum _{i}h_{ii}^+\theta _i^-\circ \omega _i^+ + \sum _{k}h_{kk}^-\theta _k^+\circ \omega _lk-}{r^4} \end{equation}$$
(51)
with
∑
i
h
i
i
±
=
0
$\sum _i h_{ii}^\pm =0$
and the induced asymptotic curvature satisfies in the basis
(
θ
i
±
)
i
$(\theta _i^\pm )_i$
R
e
∓
,
(
1
)
(
H
4
)
=
24
r
6
h
11
±
0
0
0
h
22
±
0
0
0
h
33
±
.
$$\begin{equation*} \bm{R}^{\mp ,(1)}_{\bm{e}}(H^4) = \frac{24}{r^6}\def\eqcellsep{&}\begin{bmatrix} h^\pm _{11}&0&0\\  0& h^\pm _{22}&0\\  0&0&h^\pm _{33} \end{bmatrix}. \end{equation*}$$
4.2.2 (Anti-)Selfdual Einstein deformations
Proposition 4.16.
If
H
4
, the
r
−
4
$r^{-4}$
-asymptotic term of a Ricci-flat ALE metric only induces an anti-selfdual (or selfdual) curvature, then it satisfies the obstructions (
26
) and (
32
).
Proof.
By [
14
] or Proposition
4.13
, up to a gauge term, we can assume that
H
4
is a linear combination of
θ
i
−
∘
ω
i
+
r
4
$\frac{\theta _i^-\circ \omega _i^+}{r^4}$
terms.
Thanks to Kronheimer's examples, we can reach any term of the form
−
∑
i
h
i
i
+
θ
i
−
ω
i
+
r
4
$-\sum _ih_{ii}^+\frac{\theta _i^-\omega _i^+}{r^4}$
with
h
i
i
+
⩾
0
$h_{ii}^+\geqslant 0$
. This condition
h
i
i
+
⩾
0
$h_{ii}^+\geqslant 0$
can always be arranged up to adding a gauge term as in Remark
4.14
. Since gauge terms do not matter in satisfying the obstructions (
26
) and (
32
) by Proposition
2.6
, we obtain the result.
□
$\Box$
4.2.3 General deformations
Proposition 4.17.
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE metric whose asymptotic term in CMC gauge is:
H
+
4
+
H
−
4
$H^4_++H^4_-$
where
H
+
4
:
=
−
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
r
4
and
H
−
4
:
=
−
∑
k
h
k
k
−
θ
k
+
∘
ω
k
−
r
4
.
$$\begin{equation*} H_{+}^4 := -\sum _i h_{ii}^+\frac{\theta _i^-\circ \omega _i^+}{r^4} \;\text{ and }\; H_-^4:=-\sum _k h_{kk}^-\frac{\theta _k^+\circ \omega _k^-}{r^4}. \end{equation*}$$
Then, the obstructions (
27
) and (
32
) are satisfied.
Proof.
Let us consider
H
+
4
:
=
−
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
r
4
$H_{+}^4 := -\sum _i h_{ii}^+\frac{\theta _i^-\circ \omega _i^+}{r^4}$
and
H
−
4
:
=
−
∑
k
h
k
k
−
θ
k
+
∘
ω
k
−
r
4
$H_-^4:=-\sum _k h_{kk}^-\frac{\theta _k^+\circ \omega _k^-}{r^4}$
satisfying
∑
i
h
i
i
+
=
∑
k
h
k
k
−
=
0
$\sum _i h_{ii}^+=\sum _k h_{kk}^-=0$
. Recall that these terms only induce a nonvanishing connection respectively in the anti-selfdual and selfdual orientation and the formula
θ
i
±
=
∑
k
⟨
ω
i
∓
(
∂
r
)
,
ω
l
±
(
∂
r
)
⟩
ω
l
±
.
$$\begin{equation*} \theta _i^\pm =\sum _k \langle \omega _i^\mp (\partial _r),\omega _l^\pm (\partial _r)\rangle \omega _l^\pm . \end{equation*}$$
From the formula (
48
) and Corollary
4.15
, we therefore find:
Ric
˚
e
(
2
)
(
H
+
4
,
H
−
4
)
=
24
∑
i
∑
k
h
i
i
+
h
k
k
−
⟨
ω
k
−
(
∂
r
)
,
ω
i
+
(
∂
r
)
⟩
θ
i
−
∘
θ
k
+
r
10
$$\begin{align*} \mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(H_{+}^4,H_{-}^4) &= 24\sum _i\sum _kh_{ii}^+h_{kk}^-\frac{\langle \omega _k^-(\partial _r),\omega _i^+(\partial _r)\rangle \theta _i^-\circ \theta _k^+}{r^{10}} \end{align*}$$
Now, using the fact that
θ
i
∓
(
∂
r
)
=
ω
i
∓
(
∂
r
)
$\theta _i^\mp (\partial _r) = \omega _i^\mp (\partial _r)$
, we see that the obstruction of Proposition
3.8
is proportional to
∑
i
,
k
h
i
i
+
h
k
k
−
∫
S
3
⟨
ω
k
−
(
∂
r
)
,
ω
i
+
(
∂
r
)
⟩
e
2
d
v
S
3
.
$$\begin{equation*} \sum _{i,k}h_{ii}^+h_{kk}^- \int _{\mathbb {S}^3} \langle \omega _k^-(\partial _r),\omega _i^+(\partial _r)\rangle _{\bm{e}}^2 dv_{\mathbb {S}^3}. \end{equation*}$$
Since both
∑
i
h
i
i
+
=
0
$\sum _i h_{ii}^+= 0$
and
∑
k
h
k
k
−
=
0
$\sum _kh_{kk}^- = 0$
, the obstruction (
37
) is satisfied. The proof is similar for the other obstructions (
36
).
□
$\Box$
5 OBSTRUCTION TO THE DESINGULARIZATION OF EINSTEIN METRICS
We finally recover the obstructions of [
11
] to the desingularization of Einstein metrics and many of the additional obstructions of [
37
] (but not the higher order obstructions of [
39
]). We conclude this section by proving that some Einstein orbifolds cannot be desingularized by smooth Einstein manifolds.
5.1 Infinitesimal Einstein deformations of Ricci-flat ALE metrics
On
(
R
4
∕
Γ
,
e
)
$(\mathbb {R}^4\slash \Gamma ,\bm{e})$
, the vector field
r
∂
r
$ r\partial _{r}$
is a conformal Killing vector field. It is moreover half of the gradient of the function
u
:
=
r
2
$u:=r^2$
which is a solution to
−
∇
e
∗
∇
e
u
=
8
$-\nabla _{\bm{e}}^*\nabla _{\bm{e}} u = 8$
, and we have
1
2
L
∇
e
u
e
=
Hess
e
u
=
2
e
$\frac{1}{2}\mathcal {L}_{\nabla _{\bm{e}} u}\bm{e} = \mbox{Hess}_{\bm{e}}u = 2\bm{e}$
. On a Ricci-flat ALE orbifold we can extend this situation on the whole space as follows.
Proposition 5.1. ([[
14
,
37
]])
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE orbifold asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
. Then, there exists a unique vector field
X
on
(
N
,
g
b
)
$(N,\bm{g}_b)$
such that
Φ
∗
X
=
r
∂
r
+
o
(
r
)
$\Phi ^{*}X = r\partial _{r} + o(r)$
, and
∇
g
b
∗
∇
g
b
X
=
0
$\nabla _{\bm{g}_b}^*\nabla _{\bm{g}_b} X =0$
. We actually have
X
=
1
2
∇
g
b
u
$X=\frac{1}{2}\nabla _{\bm{g}_b} u$
, where
u
is the unique solution of
−
∇
g
b
∗
∇
g
b
u
=
8
$-\nabla _{\bm{g}_b}^*\nabla _{\bm{g}_b} u = 8$
, such that
u
=
r
2
+
o
(
1
)
$u = r^2 + o(1)$
. Moreover,
(
L
X
g
b
)
∘
=
L
X
g
b
−
2
g
b
$(\mathcal {L}_X\bm{g}_b)^\circ = \mathcal {L}_X\bm{g}_b-2\bm{g}_b$
, the traceless part of
L
X
g
b
$\mathcal {L}_X\bm{g}_b$
is an infinitesimal Ricci-flat deformation of
g
b
which is trace-free and divergence-free.
Proposition 5.2. ([[
14
], Section 4])
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE orbifold asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
. Then for any Killing vector field
Y
on
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
, there exists a unique harmonic vector field
Y
′
$Y^{\prime }$
on
(
N
,
g
b
)
$(N,\bm{g}_b)$
such that
Y
′
=
Y
+
o
(
r
)
$Y^{\prime } = Y + o(r)$
. Moreover the infinitesimal deformation
L
Y
′
g
b
$\mathcal {L}_{Y^{\prime }}\bm{g}_b$
is divergence-free and trace-free. It vanishes if and only if
Y
′
$Y^{\prime }$
is a Killing vector field of
g
b
.
Remark 5.3.
All
of the infinitesimal Einstein deformations of the Eguchi-Hanson metric (
42
) are of the above types.
5.2 Obstructions to the desingularization
Let us now show that we recover the obstructions of [
11
,
37
] and find another expression for them. This new expression will further highlight the link between these obstructions and the lack of integrability of Einstein desingularizations of [
38
, Chapter 4].
Lemma 5.4.
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE metric in volume gauge as in Definition
4.12
, and choose a basis of
(
ω
i
+
)
i
$(\omega _i^+)_i$
and
(
ω
k
−
)
k
$(\omega _k^-)_k$
to so that
H
4
at infinity is of the form (
50
). And consider its development at infinity in this gauge:
g
b
=
e
+
H
4
+
o
(
r
−
4
)
$ \bm{g}_b=\bm{e}+ H^4 + o(r^{-4})$
. Then, for
(
L
X
g
b
)
∘
∈
O
(
g
b
)
$(\mathcal {L}_{X}\bm{g}_b)^\circ \in \bm{O}(\bm{g}_b)$
defined in Proposition
5.1
, we have:
(
L
X
g
b
)
∘
=
−
4
H
4
+
o
(
r
−
4
)
.
$$\begin{equation*} (\mathcal {L}_{X}\bm{g}_b)^\circ = -4 H^4 + o(r^{-4}). \end{equation*}$$
Proof.
Let us denote
Ω
s
′
$\Omega _s^{\prime }$
the open interior of the hypersurface
Ψ
(
s
S
3
∕
Γ
)
$\Psi (s\mathbb {S}^3\slash \Gamma )$
for the volume gauge diffeomorphism
Ψ
:
(
R
4
∕
Γ
)
∖
B
e
(
s
0
)
↦
N
$\Psi :(\mathbb {R}^4\slash \Gamma )\backslash B_{\bm{e}}(s_0) \mapsto N$
of Definition
4.12
for
s
0
large enough. All along the proof we will abusively omit the diffeomorphism Ψ when pulling back tensors on the infinity of
N
to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
. By Definition
4.12
, we have as
s
→
∞
$s\rightarrow \infty$
Vol
e
(
B
e
(
s
)
∕
Γ
)
=
Vol
g
b
Ω
s
′
+
o
(
1
)
.
$$\begin{equation} \operatorname{\operatorname{Vol}}_{\bm{e}}(B_{\bm{e}}(s)\slash \Gamma )= \operatorname{\operatorname{Vol}}_{\bm{g}_b}\Omega ^{\prime }_s+o(1). \end{equation}$$
(52)
The first step in order to find the asymptotic of
(
L
X
g
b
)
∘
$(\mathcal {L}_{X}\bm{g}_b)^\circ$
is to recall that
X
=
1
2
∇
g
b
u
$X =  \frac{1}{2} \nabla _{\bm{g}_b}u$
where
u
satisfies
Δ
g
b
u
=
8
$ \Delta _{\bm{g}_b}u = 8$
with
u
=
r
2
+
b
r
2
+
o
(
r
−
2
)
$u = r^2 + \frac{b}{r^2}+o(r^{-2})$
for some
b
∈
R
$b\in \mathbb {R}$
similarly to [
14
]. We determine
b
by integrating by parts
Δ
g
b
u
=
8
$\Delta _{\bm{g}_b} u = 8$
as in [
14
]:
8
Vol
e
(
B
e
(
s
)
∕
Γ
)
=
8
Vol
g
b
Ω
s
′
+
o
(
1
)
=
∫
Ω
s
′
Δ
g
b
u
d
v
g
b
+
o
(
1
)
=
8
Vol
e
(
B
e
(
s
)
∕
Γ
)
−
2
b
|
S
3
∕
Γ
|
−
2
r
−
4
|
S
3
∕
Γ
|
H
4
(
∂
r
,
∂
r
)
+
o
(
1
)
.
$$\begin{align*} 8\operatorname{\operatorname{Vol}}_{\bm{e}}(B_{\bm{e}}(s)\slash \Gamma )&= 8 \operatorname{\operatorname{Vol}}_{\bm{g}_b}\Omega ^{\prime }_s+o(1)\\ &=\int _{\Omega _s^{\prime }} \Delta _{\bm{g}_b} u dv_{\bm{g}_b}+o(1)\\ &= 8\operatorname{\operatorname{Vol}}_{\bm{e}}(B_{\bm{e}}(s)\slash \Gamma ) -2b|\mathbb {S}^3\slash \Gamma | -2r^{-4}|\mathbb {S}^3\slash \Gamma | H^4(\partial _r,\partial _r) + o(1). \end{align*}$$
which gives us
b
=
−
r
4
H
4
(
∂
r
,
∂
r
)
$ b= -r^4H^4(\partial _r,\partial _r)$
again mimicking computations of [
14
] in our slightly different coordinates.
Remark 5.5.
This is consistent with
eh
for which
X
=
r
∂
r
=
1
2
∇
eh
1
+
r
4
$X = r\partial _r = \frac{1}{2} \nabla _{\bm{eh}} \sqrt {1+r^4}$
where
u
=
1
+
r
4
$u = \sqrt {1+r^4}$
satisfies
Δ
eh
u
=
8
$\Delta _{\bm{eh}} u=8$
, and
1
+
r
4
=
r
2
+
1
2
r
2
+
o
(
r
−
2
)
$\sqrt {1+r^4} = r^2 +\frac{1}{2r^2}+o(r^{-2})$
. We moreover have
Hess
eh
1
+
r
4
=
2
eh
+
(
L
X
eh
)
∘
$\operatorname{\operatorname{Hess}}_{\bm{eh}}\sqrt {1+r^4} = 2\bm{eh}+(\mathcal {L}_{X}\bm{eh})^\circ$
according to [
11
, Proof of Proposition 2.1].
As in the case of
eh
in (
42
), where
∇
eh
1
+
r
4
=
2
r
∂
r
$\nabla _{\bm{eh}}\sqrt {1+r^4} = 2r\partial _r$
, we find
∇
g
b
u
=
2
r
∂
r
+
o
(
r
−
3
)
$\nabla _{\bm{g}_b}u = 2r\partial _r + o(r^{-3})$
. Indeed, one first has for any vector field
v
,
0
=
d
u
(
v
)
−
d
u
(
v
)
=
g
b
(
∇
g
b
u
,
v
)
−
e
(
∇
e
u
,
v
)
=
2
H
4
(
r
∂
r
,
v
)
+
e
(
∇
e
(
1
)
(
H
4
)
(
u
)
,
v
)
+
o
(
r
−
3
)
$$\begin{align*} 0=du(v)-du(v) &= \bm{g}_b(\nabla _{\bm{g}_b}u,v)-\bm{e}(\nabla _{\bm{e}}u,v)\\ &= 2H^4(r\partial _r,v) + \bm{e}(\nabla ^{(1)}_{\bm{e}}(H^4)(u),v) + o(r^{-3}) \end{align*}$$
where
∇
e
(
1
)
(
H
4
)
$\nabla ^{(1)}_{\bm{e}}(H^4)$
is the first variation of the gradient operator
h
↦
∇
e
+
h
$h\mapsto \nabla _{\bm{e}+h}$
at
h
=
0
$h=0$
in the direction
H
4
. This directly gives:
∇
g
b
u
=
∇
e
u
+
∇
e
(
1
)
(
H
4
)
(
u
)
+
o
(
r
−
3
)
=
2
r
∂
r
−
2
b
r
3
∂
r
+
o
(
r
−
3
)
−
2
H
4
(
r
∂
r
)
+
o
(
r
−
3
)
=
2
r
∂
r
+
o
(
r
−
3
)
$$\begin{align*} \nabla _{\bm{g}_b}u &=\nabla _{\bm{e}}u + \nabla ^{(1)}_{\bm{e}}(H^4)(u) + o(r^{-3})\\ &=2r\partial _r -2\frac{b}{r^3}\partial _r + o(r^{-3})- 2H^4(r\partial _r) + o(r^{-3})\\ &=2r\partial _r+o(r^{-3}) \end{align*}$$
where we used
∇
e
(
1
)
(
H
4
)
(
u
)
=
−
2
H
4
(
r
∂
r
)
=
−
2
r
H
4
(
∂
r
,
∂
r
)
∂
r
+
o
(
r
−
3
)
$\nabla ^{(1)}_{\bm{e}}(H^4)(u) = -2H^4(r\partial _r) = -2rH^4(\partial _r,\partial _r) \partial _r + o(r^{-3})$
because
H
4
has a diagonal form by assumption, and
b
=
−
r
4
H
4
(
∂
r
,
∂
r
)
$b = -r^4H^4(\partial _r,\partial _r)$
(the identification between (1,1) tensor and symmetric 2-tensor is made with respect to
e
or
g
b
indifferently at this level of precision).
We can then develop:
1
2
L
∇
g
b
u
g
b
=
L
(
r
∂
r
+
o
(
r
−
3
)
)
e
+
H
4
+
o
(
r
−
4
)
=
2
e
−
2
H
4
+
o
(
r
−
4
)
=
2
g
b
−
4
H
4
+
o
(
r
−
4
)
.
$$\begin{align*} \frac{1}{2}\mathcal {L}_{\nabla _{\bm{g}_b}u}\bm{g}_b &= \mathcal {L}_{(r\partial _r+o(r^{-3}))}{\left(\bm{e} + H^4 +o(r^{-4})\right)}\\ &= 2\bm{e} -2H^4 + o(r^{-4}) = 2\bm{g}_b -4H^4 + o(r^{-4}). \end{align*}$$
Finally, considering the traceless part with respect to
g
b
, we find the stated result:
(
L
X
g
b
)
∘
=
−
4
H
4
+
o
(
r
−
4
)
.
$$\begin{equation*} (\mathcal {L}_X\bm{g}_b)^\circ = -4H^4 + o(r^{-4}). \end{equation*}$$
□
$\Box$
This lets us state the following obstruction result.
Theorem 5.6.
Let
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
be an Einstein orbifold with a singularity
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
and let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE manifold with
integrable
Ricci-flat ALE deformations asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
. Let us denote
H
4
the asymptotic term of
g
b
in
volume gauge
as in Definition
4.12
and in a diagonal form (
50
):
g
b
=
e
+
H
4
+
O
(
r
−
5
)
$ \bm{g}_b = \bm{e} + H^4 + \mathcal {O}(r^{-5})$
, and let
H
2
be the quadratic terms of
g
o
=
e
+
H
2
+
O
(
r
3
)
$\bm{g}_o = \bm{e}+H_2+\mathcal {O}(r^3)$
in a coordinate system in which
B
e
(
H
2
)
=
0
$B_{\bm{e}}(H_2)=0$
.
Assume that there exists a sequence of Einstein metrics,
(
M
,
g
n
)
n
$(M,\bm{g}_n)_n$
,
d
G
H
$d_{GH}$
-converging to
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
and such that there exists a sequence
(
t
n
)
n
∈
N
$(t_n)_{n\in \mathbb {N}}$
with
t
n
>
0
$t_n&gt;0$
satisfying:
(
M
,
g
n
t
n
)
→
G
H
(
N
,
g
b
)
$ (M,\frac{\bm{g}_n}{t_n}) \xrightarrow [GH]{}(N,\bm{g}_b)$
. Then, we have the following obstructions:
for any Killing vector field
Y
i
±
$Y_i^\pm$
,
∫
S
3
Ric
˚
e
(
2
)
(
H
2
,
H
4
)
(
Y
i
±
,
∂
r
)
d
v
S
3
=
0
,
$$\begin{equation} \int _{\mathbb {S}^{3}} {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H_2,H^4)\right)}(Y_i^\pm ,\partial _r)dv_{\mathbb {S}^{3}} = 0,\end{equation}$$
(53)
for the conformal Killing vector field
r
∂
r
$r\partial _r$
, we have
∫
S
3
Ric
˚
e
(
2
)
(
H
2
,
H
4
)
(
r
∂
r
,
∂
r
)
d
v
S
3
=
0
.
$$\begin{equation} \int _{\mathbb {S}^{3}} {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H_2,H^4)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^{3}} = 0.\end{equation}$$
(54)
Remark 5.7.
As we will see in Corollary
5.11
proven later, the obstruction (
54
) is
never
trivial if
(
N
,
g
b
)
$(N,\bm{g}_b)$
is not flat. That is, if
(
N
,
g
b
)
$(N,\bm{g}_b)$
is not flat, then there are some
H
2
as above for which (
54
) is not satisfied.
Remark 5.8.
By [
7
], the asymptotic terms of Kronheimer's instantons in volume gauge are generally of the form:
H
4
=
−
∑
i
,
j
⟨
ζ
i
,
ζ
j
⟩
θ
i
−
∘
ω
j
+
2
r
4
$ H^4 = -\sum _{i,j} \langle \zeta _i,\zeta _j\rangle \frac{\theta _i^-\circ \omega _j^+}{2r^4}$
for
ζ
1
,
ζ
2
,
ζ
3
∈
R
k
$\zeta _1,\zeta _2,\zeta _3\in \mathbb {R}^k$
for some
k
arbitrarily large depending on the group at infinity (
k
=
1
$k=1$
for the Eguchi-Hanson metric). For
k
⩾
3
$k\geqslant 3$
we can construct
ζ
1
,
ζ
2
,
ζ
3
∈
R
k
$\zeta _1,\zeta _2,\zeta _3\in \mathbb {R}^k$
with
⟨
ζ
i
,
ζ
j
⟩
=
δ
i
j
$\langle \zeta _i,\zeta _j\rangle = \delta _{ij}$
and we check that the obstructions (
53
) vanishes for
any
H
2
.
Proof.
Let us come back to the origin of the obstructions of [
37
,
38
]. They are the obstructions to solving:
Ric
˚
g
b
(
1
)
(
h
2
)
=
0
.
h
2
=
H
2
+
H
2
4
+
O
(
r
−
3
+
ε
)
,
$$\begin{equation} \left\{  \def\eqcellsep{&}\begin{array}{rcl}  \mathring{\operatorname{\operatorname{Ric}}}_{\bm{g}_b}^{(1)}(h_2) &=&0.\\[6pt] h_2&=&H_2 + H^4_2 + \mathcal {O}(r^{-3+\epsilon })\end{array}  \right.,\end{equation}$$
(55)
where
|
H
2
4
|
e
∼
r
−
2
$|H^4_2|_{\bm{e}}\sim r^{-2}$
, see [
39
].
Let us consider the harmonic vector field
X
=
r
∂
r
+
O
(
r
−
3
)
$X = r\partial _r + \mathcal {O}(r^{-3})$
and the harmonic vector fields
Y
i
′
=
Y
i
+
O
(
r
−
3
)
$Y_i^{\prime } = Y_i+\mathcal {O}(r^{-3})$
defined in Section
5.1
. Following the computation of [
11
,
37
], noting that in volume gauge, we have
(
L
X
g
b
)
∘
=
−
4
H
4
+
o
(
r
−
4
)
$(\mathcal {L}_X\bm{g}_b)^\circ = -4 H^4+o(r^{-4})$
by Lemma
5.4
and we moreover have:
0
=
1
2
lim
R
→
+
∞
∫
{
r
⩽
R
}
Ric
˚
g
b
(
1
)
(
h
2
)
,
(
L
X
g
b
)
∘
g
b
d
v
g
b
=
4
∫
S
3
∕
Γ
3
H
2
,
H
4
+
H
4
(
B
e
H
2
,
∂
r
)
d
v
S
3
∕
Γ
$$\begin{eqnarray} 0&=&\frac{1}{2}\lim _{R\rightarrow +\infty }\int _{\lbrace r\leqslant R\rbrace } {\left\langle \mathring{\operatorname{\operatorname{Ric}}}_{\bm{g}_b}^{(1)}(h_2)\;,\;(\mathcal {L}_X\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b}\nonumber\\ &=&4\int _{\mathbb {S}^3\slash \Gamma }3{\left\langle H_2, H^4\right\rangle} + H^4(B_{\bm{e}}H_2,\partial _r) dv_{\mathbb {S}^3\slash \Gamma }\end{eqnarray}$$
(56)
which is manifestly linear in
H
4
. Similarly, for any Killing vector field
Y
i
$Y_i$
and its harmonic extension
Y
i
′
$Y_i^{\prime }$
, we find the obstructions:
∫
S
3
∕
Γ
3
H
2
,
L
Y
i
H
4
+
L
Y
i
H
4
(
B
e
H
2
,
∂
r
)
d
v
S
3
∕
Γ
=
0
.
$$\begin{equation} \int _{\mathbb {S}^3\slash \Gamma }3{\left\langle H_2, \mathcal {L}_{Y_i}H^4\right\rangle} + \mathcal {L}_{Y_i}H^4(B_{\bm{e}}H_2,\partial _r) dv_{\mathbb {S}^3\slash \Gamma }=0.\end{equation}$$
(57)
Now, the interpretation of [
11
,
12
] of the obstruction tells us that for some
C
=
C
(
Γ
)
≠
0
$C=C(\Gamma )\ne 0$
, for any
k
,
l
∈
{
1
,
2
,
3
}
$k,l\in \lbrace 1,2,3\rbrace$
∫
S
3
∕
Γ
H
2
,
θ
k
∓
∘
ω
l
±
r
4
d
v
S
3
∕
Γ
=
C
R
e
±
,
(
1
)
(
H
2
)
(
ω
k
±
)
,
ω
l
±
.
$$\begin{equation} \int _{\mathbb {S}^3\slash \Gamma } {\left\langle H_2, \frac{\theta _k^\mp \circ \omega _l^\pm }{r^4}\right\rangle} dv_{\mathbb {S}^3\slash \Gamma } = C {\left\langle \bm{R}^{\pm ,(1)}_{\bm{e}}(H_2)(\omega _k^\pm ),\omega _l^\pm \right\rangle} .\end{equation}$$
(58)
By linearity, this lets us compute the obstruction for any
H
4
coming from a volume gauge.
On the other hand, let us use the formalism of [
12
] and compute the second variation
Ric
˚
e
(
2
)
(
H
2
,
H
4
)
$\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H_2,H^4)$
when
B
e
(
H
2
)
=
0
$B_{\bm{e}}(H_2) = 0$
. For the quadratic terms
H
2
of the orbifold, we decompose
R
e
+
,
(
1
)
(
H
2
)
=
∑
i
j
R
i
j
+
ω
i
+
⊗
ω
j
+
,
$$\begin{equation} \bm{R}^{+,(1)}_{\bm{e}}(H_2) = \sum _{ij}R^+_{ij}\omega _i^+\otimes \omega _j^+,\end{equation}$$
(59)
and we will consider another term of the form
H
4
=
θ
l
−
∘
ω
k
+
r
4
$H^4 = \frac{\theta _l^-\circ \omega _k^+}{r^4}$
. Using the formula (
48
) for the second variation of the traceless part of the Ricci curvature denoted
Ric
˚
$\mathring{\operatorname{\operatorname{Ric}}}$
applied to the hyperkähler flat metric
e
in the direction
H
4
+
H
2
$H^4+H_2$
, we find
Ric
˚
e
(
2
)
(
H
4
,
H
2
)
=
∑
j
R
k
j
+
θ
l
−
∘
ω
j
+
r
4
.
$$\begin{equation} \mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(H^4,H_2) = \sum _{j}R^+_{kj}\frac{\theta _l^-\circ \omega _j^+}{r^4}.\end{equation}$$
(60)
Now, this lets us compute the obstruction (
53
). For any
i
∈
{
1
,
2
,
3
}
$i\in \lbrace 1,2,3\rbrace$
, define
(
i
l
)
∈
{
1
,
2
,
3
}
$(il)\in \lbrace 1,2,3\rbrace$
by
ω
i
+
∘
ω
(
i
l
)
+
=
±
ω
l
+
$\omega _i^+\circ \omega _{(il)}^+ = \pm \omega _l^+$
. We find the following value for (
53
) with Killing vector field
Y
(
i
l
)
+
=
ω
(
i
l
)
+
(
r
∂
r
)
$Y_{(il)}^+=\omega _{(il)}^+(r\partial _r)$
:
0
=
∑
j
R
k
j
+
∫
S
3
⟨
θ
l
−
(
∂
r
)
,
ω
j
+
(
ω
(
i
l
)
+
(
r
∂
r
)
)
⟩
e
d
v
S
3
=
±
R
k
i
+
∫
S
3
⟨
Y
l
−
,
Y
l
−
⟩
e
d
v
S
3
.
$$\begin{eqnarray}  0&=&\sum _{j}R^+_{kj}\int _{\mathbb {S}^3} \langle \theta _l^-(\partial _r),\omega _j^+(\omega _{(il)}^+(r\partial _r))\rangle _{\bm{e}}dv_{\mathbb {S}^3}\nonumber\\ &=& \pm R_{ki}^+\int _{\mathbb {S}^3} \langle Y_l^-,Y_l^-\rangle _{\bm{e}}dv_{\mathbb {S}^3}. \end{eqnarray}$$
(61)
We therefore see that if (
57
) is satisfied with
Y
(
i
l
)
+
$Y_{(il)}^+$
, then, one has (
53
) satisfied thanks to (
58
). Similarly, from the obstruction (
54
), we find:
0
=
∑
j
R
k
j
+
∫
S
3
⟨
θ
l
−
(
∂
r
)
,
ω
j
+
(
r
∂
r
)
⟩
e
d
v
S
3
=
∑
j
R
k
j
+
∫
S
3
⟨
Y
l
+
,
Y
j
+
⟩
e
d
v
S
3
=
R
k
l
+
∫
S
3
⟨
Y
l
+
,
Y
l
+
⟩
e
d
v
S
3
,
$$\begin{eqnarray} 0&=&\sum _{j}R^+_{kj}\int _{\mathbb {S}^3} \langle \theta _l^-(\partial _r),\omega _j^+(r\partial _r)\rangle _{\bm{e}}dv_{\mathbb {S}^3}\nonumber\\ &=& \sum _{j}R^+_{kj}\int _{\mathbb {S}^3} \langle Y_l^+,Y_j^+\rangle _{\bm{e}}dv_{\mathbb {S}^3}\nonumber\\ &=& R^+_{kl}\int _{\mathbb {S}^3} \langle Y_l^+,Y_l^+\rangle _{\bm{e}}dv_{\mathbb {S}^3}, \end{eqnarray}$$
(62)
and we consequently see that the condition (
54
) is the same as (
56
) thanks to (
58
).
□
$\Box$
Remark 5.9.
It might seem like the proof of Theorem
5.6
is completely disjoint from the obstruction of Theorem
3.8
or those of Section
3.3
. We illustrate below that they actually build on estimates of the exact same quantity but rely on different integrations by parts. Indeed, as noticed along the proof of Lemma
5.4
a special feature of the volume gauge is that
∇
g
b
u
∼
r
∂
r
$ \nabla _{\bm{g}_b}u \sim r\partial _r$
at an order higher than expected.
Let us illustrate this with the Eguchi-Hanson metric
eh
which was already discussed in Section
3.3
. Coming back to the integral quantity in (
56
) and integrating by parts
in the other direction
thanks to (
20
), we find:
0
=
lim
R
→
+
∞
∫
{
r
=
R
}
Ric
˚
eh
(
1
)
(
h
2
)
(
r
∂
r
,
∂
r
)
d
v
eh
|
{
r
=
R
}
=
1
2
lim
R
→
+
∞
∫
{
r
⩽
R
}
Ric
˚
eh
(
1
)
(
h
2
)
,
L
r
∂
r
eh
eh
d
v
eh
=
1
2
lim
R
→
+
∞
∫
{
r
⩽
R
}
Ric
˚
eh
(
1
)
(
h
2
)
,
(
L
r
∂
r
eh
)
∘
eh
d
v
eh
$$\begin{align} 0&=\lim _{R\rightarrow +\infty }\int _{\lbrace r=R\rbrace }{\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{eh}}^{(1)}(h_2)\right)}(r\partial _r,\partial _r)dv_{\bm{eh}|\lbrace r=R\rbrace }\nonumber \\ &= \frac{1}{2}\lim _{R\rightarrow +\infty }\int _{\lbrace r\leqslant R\rbrace } {\left\langle {\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{eh}}^{(1)}(h_2)\right)},\mathcal {L}_{r\partial _r}\bm{eh} \right\rangle} _{\bm{eh}}dv_{\bm{eh}}\nonumber \\ &= \frac{1}{2}\lim _{R\rightarrow +\infty }\int _{\lbrace r\leqslant R\rbrace } {\left\langle {\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{eh}}^{(1)}(h_2)\right)},(\mathcal {L}_{r\partial _r}\bm{eh})^\circ \right\rangle} _{\bm{eh}}dv_{\bm{eh}}\end{align}$$
(63)
The right-hand side term of (
63
) has the following limit as
R
→
+
∞
$R\rightarrow +\infty$
:
0
=
∫
S
3
∕
Z
2
E
e
(
1
)
(
H
2
4
)
+
E
e
(
2
)
(
H
4
,
H
2
)
+
λ
H
4
(
r
∂
r
,
∂
r
)
d
v
S
3
∕
Z
2
=
∫
S
3
∕
Z
2
E
e
(
1
)
(
H
2
4
)
(
r
∂
r
,
∂
r
)
d
v
S
3
∕
Z
2
+
∫
S
3
∕
Z
2
Ric
˚
e
(
2
)
(
H
4
,
H
2
)
(
r
∂
r
,
∂
r
)
d
v
S
3
∕
Z
2
.
$$\begin{align*} 0&=\int _{\mathbb {S}^3\slash \mathbb {Z}_2}{\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(H_2^4) + \operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(H^4,H_2)+\lambda H^4\right)}(r\partial _r,\partial _r) dv_{\mathbb {S}^3\slash \mathbb {Z}_2}\\ &=\int _{\mathbb {S}^3\slash \mathbb {Z}_2}{\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(H_2^4)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^3\slash \mathbb {Z}_2} +\int _{\mathbb {S}^3\slash \mathbb {Z}_2}{\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(H^4,H_2)\right)}(r\partial _r,\partial _r) dv_{\mathbb {S}^3\slash \mathbb {Z}_2}. \end{align*}$$
which is exactly the quantity obtained in (
43
). As in Section
3.3
, we may use
H
2
4
=
0
$H^4_2 = 0$
.
We recover
all
of the obstructions of [
11
].
Corollary 5.10.
With the assumptions of Theorem
5.6
with
(
N
,
g
b
)
=
(
T
∗
S
2
,
eh
)
$(N,\bm{g}_b) = (T^*\mathbb {S}^2,\bm{eh})$
defined in (
42
) with
H
4
=
−
θ
1
−
∘
ω
1
+
2
r
e
4
$H^4 = -\frac{\theta _1^-\circ \omega _1^+}{2 r_{\bm{e}}^4}$
and any
H
2
satisfying
B
e
(
H
2
)
=
0
$B_{\bm{e}}(H_2)=0$
, the following propositions are equivalent:
(1)
R
e
+
,
(
1
)
(
H
2
)
ω
1
+
=
0
$\bm{R}^{+,(1)}_{\bm{e}}(H_2)\omega _1^+ = 0$
,
(2)
∫
S
3
∕
Z
2
(
Ric
˚
e
(
2
)
(
H
4
,
H
2
)
)
(
r
∂
r
,
∂
r
)
d
v
S
3
∕
Z
2
=
0
$\int _{\mathbb {S}^3\slash \mathbb {Z}_2} (\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H^4,H_2))(r\partial _r,\partial _r) dv_{\mathbb {S}^3\slash \mathbb {Z}_2} = 0$
, and for any
i
∈
{
2
,
3
}
$i\in \lbrace 2,3\rbrace$
for the Killing vector field
Y
i
+
$Y_i^+$
,
∫
S
3
∕
Z
2
(
Ric
˚
e
(
2
)
(
H
4
,
H
2
)
)
(
Y
i
+
,
∂
r
)
d
v
S
3
∕
Z
2
=
0
$ \int _{\mathbb {S}^3\slash \mathbb {Z}_2} (\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H^4,H_2))(Y_i^+,\partial _r) dv_{\mathbb {S}^3\slash \mathbb {Z}_2} = 0$
,
(3)
there is a solution
h
2
to the Equation (
55
),
(4)
∫
S
3
∕
Z
2
⟨
H
2
,
H
4
⟩
d
v
S
3
∕
Z
2
=
0
$\int _{\mathbb {S}^3\slash \mathbb {Z}_2}\langle H_2, H^4\rangle dv_{\mathbb {S}^3\slash \mathbb {Z}_2} = 0$
, and
i
∈
{
2
,
3
}
$i\in \lbrace 2,3\rbrace$
:
∫
S
3
∕
Z
2
⟨
H
2
,
L
Y
i
+
H
4
⟩
d
v
S
3
∕
Z
2
=
0
$\int _{\mathbb {S}^3\slash \mathbb {Z}_2}\langle H_2, \mathcal {L}_{Y_i^+}H^4\rangle dv_{\mathbb {S}^3\slash \mathbb {Z}_2} = 0$
.
5.3 Spherical and hyperbolic orbifolds
Using the above new interpretation of the obstruction to the desingularization of Einstein 4-manifolds as well as the integration by parts (
20
), we prove one of the main conjectures of [
37
,
38
] and answer the long-standing question of whether or not Einstein orbifolds can always be
d
G
H
$d_{GH}$
-desingularized by smooth Einstein metrics.
The starting point is that the obstruction (
54
) never vanishes when the orbifold is spherical or hyperbolic.
Corollary 5.11.
If the obstruction (
54
) vanishes, then, the orbifold
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
is not spherical or hyperbolic.
Proof.
Let us consider
H
4
=
∑
i
h
i
i
+
θ
i
−
∘
ω
i
+
r
4
+
∑
k
h
k
k
−
θ
k
+
∘
ω
k
−
r
4
$H^4 = \sum _{i}h_{ii}^+ \frac{\theta _i^-\circ \omega _i^+}{r^4}+\sum _{k}h_{kk}^- \frac{\theta _k^+\circ \omega _k^-}{r^4}$
. From (
60
), by linearity, we have the following expression:
Ric
˚
e
(
2
)
(
H
4
,
H
2
)
=
∑
i
m
h
i
i
+
R
i
m
+
θ
i
−
∘
ω
m
+
r
4
+
∑
k
n
h
k
k
−
R
k
n
−
θ
k
+
∘
ω
k
−
r
4
,
$$\begin{equation} \mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(H^4,H_2) = \sum _{im}h_{ii}^+R^+_{im}\frac{\theta _i^-\circ \omega _m^+}{r^4} +\sum _{kn}h_{kk}^-R^-_{kn}\frac{\theta _k^+\circ \omega _k^-}{r^4},\end{equation}$$
(64)
where
R
i
i
±
$R_{ii}^\pm$
follow the notation of (
59
). Hence, the obstruction (
54
) rewrites:
∑
i
h
i
i
+
R
i
i
+
+
∑
k
h
k
k
−
R
k
k
−
=
0
.
$$\begin{equation} \sum _{i}h_{ii}^+R^+_{ii} +\sum _{k}h_{kk}^-R^-_{kk} = 0.\end{equation}$$
(65)
Denoting
Λ
=
∑
i
R
i
i
+
=
∑
k
R
k
k
−
$\Lambda = \sum _iR^+_{ii} = \sum _k R^-_{kk}$
,
(
W
i
j
±
)
i
j
$(W^\pm _{ij})_{ij}$
the traceless part of
(
R
i
j
±
)
i
j
$(R^\pm _{ij})_{ij}$
, and
h
˚
i
j
±
$ \mathring{h}_{ij}^\pm$
the traceless part of
(
h
i
j
±
)
i
,
j
∈
{
1
,
2
,
3
}
$(h_{ij}^\pm )_{i,j\in \lbrace 1,2,3\rbrace }$
(note that the
h
˚
i
j
±
$\mathring{h}_{ij}^\pm$
are proportional to the asymptotic curvature of
g
b
by Proposition
4.13
) and recall that
∑
i
h
i
i
+
+
∑
k
h
k
k
−
=
c
(
Γ
)
V
(
N
,
g
b
)
<
0
$\sum _{i}h_{ii}^++\sum _kh_{kk}^- = c(\Gamma ) \mathcal {V}(N,\bm{g}_b)&lt;0$
. We therefore write (
65
) as
0
=
Λ
c
(
Γ
)
V
(
N
,
g
b
)
+
∑
i
h
˚
i
i
+
W
i
i
+
+
∑
k
h
˚
k
k
−
W
k
k
−
.
$$\begin{equation} 0=\Lambda c(\Gamma ) \mathcal {V}(N,\bm{g}_b) + \sum _{i}\mathring{h}_{ii}^+ W^+_{ii} + \sum _{k}\mathring{h}_{kk}^- W^-_{kk}.\end{equation}$$
(66)
In the case of a spherical or hyperbolic orbifold, we have
W
±
=
0
$W^\pm =0$
and
Λ
≠
0
$\Lambda \ne 0$
, therefore, since
c
(
Γ
)
V
(
N
,
g
b
)
<
0
$ c(\Gamma ) \mathcal {V}(N,\bm{g}_b)&lt;0$
, the obstruction (
66
) is not satisfied.
□
$\Box$
5.3.1 Cokernel of the linearization of
E
$\operatorname{\operatorname{E}}$
at a Ricci-flat ALE metric
This technical section contains the main innovation from [
36
,
37
] towards getting rid of an integrability assumption for the Ricci-flat ALE metric
g
b
: the proof of Proposition
1.12
.
Let us consider a Ricci-flat ALE orbifold
(
N
,
g
b
)
$ (N,\bm{g}_b)$
, the operator
g
↦
Φ
g
b
(
g
)
:
=
E
(
g
)
+
δ
g
b
∗
δ
g
b
g
,
$$\begin{equation*} g\mapsto {\Phi }_{\bm{g}_b}(g) := \operatorname{\operatorname{E}}(g)+\delta _{\bm{g}_b}^*\delta _{\bm{g}_b} g, \end{equation*}$$
and
O
(
g
b
) the
L
2
(
g
b
)
$L^2(\bm{g}_b)$
-kernel of
Φ
g
b
(
1
)
${\Phi }_{\bm{g}_b}^{(1)}$
, the linearization of
Φ
g
b
${\Phi }_{\bm{g}_b}$
at
g
b
. Note that the elements of
O
(
g
b
) are traceless and divergence-free, see [
37
] for instance. According to [
37
,
38
], for any small enough
v
∈
O
(
g
b
)
$v\in \bm{O}(\bm{g}_b)$
, there exists a unique metric
g
v
$g_v$
which satisfies both
Φ
g
b
(
g
v
)
=
E
(
g
v
)
+
δ
g
b
∗
δ
g
b
g
v
∈
O
(
g
b
)
and
g
v
−
(
g
b
+
v
)
⊥
L
2
(
g
b
)
O
(
g
b
)
.
$$\begin{equation*} {\Phi }_{\bm{g}_b}(g_v) = \operatorname{\operatorname{E}}(g_v) + \delta ^*_{\bm{g}_b}\delta _{\bm{g}_b}g_v\in \bm{O}(\bm{g}_b) \;\text{ and }\; g_v - (\bm{g}_b+v)\perp _{L^2(\bm{g}_b)} \bm{O}(\bm{g}_b). \end{equation*}$$
We will use the following Lemma in order to prove Proposition
1.12
.
Lemma 5.12.
Assume that for all
k
⩽
l
−
1
$k\leqslant l-1$
,
∂
s
k
|
s
=
0
k
Φ
g
b
(
g
s
v
)
=
0
$\partial ^k_{s^k|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) =0$
. Then, we have:
(1)
for all
k
⩽
l
−
1
$k\leqslant l-1$
, we have:
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
=
0
$ \partial _{s^k|s=0}^k\operatorname{\operatorname{E}}(g_{sv}) = 0$
, and for all
k
⩽
l
$k\leqslant l$
, we have
δ
g
b
∂
s
k
|
s
=
0
k
g
s
v
=
0
$\delta _{\bm{g}_b}\partial _{s^k|s=0}^kg_{sv} = 0$
,
(2)
δ
g
b
(
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
)
=
0
$\delta _{\bm{g}_b}(\partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv}))= 0$
, and
(3)
for any
l
, there exist multilinear functions
Q
g
(
l
)
(
h
1
,
…
,
h
l
)
=
∑
m
⩾
2
∑
j
1
,
…
,
j
m
⩾
1
l
∇
g
h
j
1
∗
h
j
2
∗
…
∗
h
j
m
$ Q_g^{(l)}(h_1,\ldots,h_l) = \sum _{m\geqslant 2}\sum _{j_1,\ldots,j_m\geqslant 1}^l \nabla _gh_{j_1}*h_{j_2}*\ldots*h_{j_m}$
, where * denotes various contractions of the tensors. Integrating over an open domain Ω with smooth boundary, we have:
∫
Ω
g
b
,
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
∂
s
l
|
s
=
0
l
g
s
v
g
b
d
v
g
b
=
∫
∂
Ω
Q
(
l
)
∂
s
|
s
=
0
g
s
v
,
…
,
∂
s
l
−
1
|
s
=
0
l
−
1
g
s
v
.
$$\begin{equation*} \int _\Omega {\left\langle \bm{g}_b,\partial _{s^l{|s= 0}}^l {\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}{\left(\partial _{s^l{|s= 0}}^lg_{sv}\right)} \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = \int _{\partial \Omega } Q^{(l)}{\left(\partial _{s{|s= 0}}g_{sv},\ldots,\partial _{s^{l-1}{|s= 0}}^{l-1}g_{sv}\right)}. \end{equation*}$$
Proof.
Let us show these three properties in order.
(1)
Notice that for any
k
,
∂
s
k
k
Φ
g
b
(
g
s
v
)
=
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
+
δ
g
b
∗
δ
g
b
(
∂
s
k
|
s
=
0
k
g
s
v
)
$\partial _{s^k}^k {\Phi }_{\bm{g}_b}(g_{sv}) = \partial _{s^k|s=0}^k\operatorname{\operatorname{E}}(g_{sv}) + \delta _{\bm{g}_b}^*\delta _{\bm{g}_b}(\partial _{s^k|s=0}^kg_{sv})$
. Therefore, since
δ
g
b
Φ
(
g
s
v
)
=
0
$ \delta _{\bm{g}_b}{\Phi }(g_{sv})=0$
because
Φ
(
g
s
v
)
∈
O
(
g
b
)
${\Phi }(g_{sv})\in \bm{O}(\bm{g}_b)$
, then one has:
δ
g
b
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
+
δ
g
b
∗
δ
g
b
∂
s
k
|
s
=
0
k
g
s
v
=
0
.
$$\begin{equation*} \delta _{\bm{g}_b}{\left(\partial _{s^k|s=0}^k\operatorname{\operatorname{E}}(g_{sv}) + \delta _{\bm{g}_b}^*\delta _{\bm{g}_b}\left(\partial _{s^k|s=0}^kg_{sv}\right)\right)} = 0. \end{equation*}$$
If we moreover assume
∂
s
j
j
E
(
g
s
v
)
=
0
$\partial _{s^j}^j\operatorname{\operatorname{E}}(g_{sv}) = 0$
for all
j
⩽
k
−
1
$j\leqslant k-1$
, we find
δ
g
b
δ
g
b
∗
δ
g
b
(
∂
s
k
|
s
=
0
k
g
s
v
)
=
0
$\delta _{\bm{g}_b}\delta _{\bm{g}_b}^*\delta _{\bm{g}_b}(\partial _{s^k|s=0}^kg_{sv}) = 0$
since
0
=
∂
s
k
|
s
=
0
k
(
δ
g
s
v
E
(
g
s
v
)
)
=
δ
g
b
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
$0 = \partial ^k_{s^k|s=0}(\delta _{g_{sv}}\operatorname{\operatorname{E}}(g_{sv})) = \delta _{\bm{g}_b}\partial ^k_{s^k|s=0}\operatorname{\operatorname{E}}(g_{sv})$
. Since
δ
g
b
δ
g
b
∗
$\delta _{\bm{g}_b}\delta _{\bm{g}_b}^*$
is invertible on vector fields (or 1-forms) decaying at infinity by [
11
,
37
], we find
δ
g
b
(
∂
s
k
|
s
=
0
k
g
s
v
)
=
0
$ \delta _{\bm{g}_b}(\partial _{s^k|s=0}^kg_{sv}) =0$
, but that means that
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
=
∂
s
k
|
s
=
0
k
Φ
g
b
(
g
s
v
)
−
δ
g
b
∗
δ
g
b
(
∂
s
k
|
s
=
0
k
g
s
v
)
=
0
$\partial _{s^k|s=0}^k\operatorname{\operatorname{E}}(g_{sv}) = \partial _{s^k|s=0}^k {\Phi }_{\bm{g}_b}(g_{sv}) - \delta _{\bm{g}_b}^*\delta _{\bm{g}_b}(\partial _{s^k|s=0}^kg_{sv}) =0$
. We can iterate this up to
k
=
l
−
1
$k = l-1$
since by assumption
∂
s
k
|
s
=
0
k
Φ
g
b
(
g
s
v
)
=
0
$ \partial _{s^k|s=0}^k {\Phi }_{\bm{g}_b}(g_{sv}) =0$
for all
k
⩽
l
−
1
$k\leqslant l-1$
. This lets us also find
δ
g
b
(
∂
s
l
|
s
=
0
l
g
s
v
)
=
0
$\delta _{\bm{g}_b}(\partial _{s^l|s=0}^lg_{sv}) =0$
.
(2)
For the equality
δ
g
b
(
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
)
=
0
$\delta _{\bm{g}_b}(\partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv}))= 0$
, we first see that
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
=
∂
s
l
|
s
=
0
l
E
(
g
s
v
)
−
E
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
$$\begin{equation*} \partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv}) = \partial ^l_{s^l|s=0}\operatorname{\operatorname{E}}(g_{sv}) - \operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv}) \end{equation*}$$
because
Φ
=
E
+
δ
g
b
∗
δ
g
b
${\Phi } = \operatorname{\operatorname{E}}+ \delta _{\bm{g}_b}^*\delta _{\bm{g}_b}$
. We conclude by noticing as above that
δ
g
b
∂
s
l
|
s
=
0
l
E
(
g
s
v
)
=
∂
s
l
|
s
=
0
l
δ
g
s
v
E
(
g
s
v
)
=
0
$$\begin{equation*} \delta _{\bm{g}_b} \partial ^l_{s^l|s=0}\operatorname{\operatorname{E}}(g_{sv}) = \partial ^l_{s^l|s=0}{\left(\delta _{g_{sv}} \operatorname{\operatorname{E}}(g_{sv})\right)} = 0 \end{equation*}$$
because
∂
s
k
|
s
=
0
k
E
(
g
s
v
)
=
0
$\partial ^k_{s^k|s=0}\operatorname{\operatorname{E}}(g_{sv}) = 0$
for all
k
⩽
l
−
1
$k\leqslant l-1$
and
δ
g
b
E
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
=
0
$\delta _{\bm{g}_b}\operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv})=0$
by Proposition
2.2
.
(3)
The first remark is that
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
=
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
∂
s
l
|
s
=
0
l
g
s
v
+
E
g
b
(
1
)
∂
s
l
|
s
=
0
l
g
s
v
+
δ
g
b
∗
δ
g
b
∂
s
l
|
s
=
0
l
g
s
v
,
$$\begin{align*} \partial _{s^l{|s= 0}}^l {\Phi }_{\bm{g}_b}(g_{sv}) =\;& {\left(\partial _{s^l{|s= 0}}^l {\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}\left(\partial _{s^l{|s= 0}}^lg_{sv}\right)\right)}\\ &+ \operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}\left(\partial _{s^l{|s= 0}}^lg_{sv}\right)\\ &+ \delta _{\bm{g}_b}^*\delta _{\bm{g}_b}\partial _{s^l{|s= 0}}^lg_{sv}, \end{align*}$$
and we will treat separately each of these terms.
We then show, using (
34
), that the integral of the trace of
E
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
$\operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}(\partial _{s^l{|s= 0}}^lg_{sv})$
is a boundary term:
2
2
−
d
∫
Ω
g
b
,
E
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
g
b
d
v
g
b
=
−
∫
∂
Ω
δ
g
b
∂
s
l
|
s
=
0
l
g
s
v
+
d
tr
g
b
∂
s
l
|
s
=
0
l
g
s
v
(
n
∂
Ω
)
d
v
g
b
|
∂
Ω
.
$$\begin{eqnarray} \frac{2}{2-d}\int _\Omega &&{\left\langle \bm{g}_b, \operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}(\partial _{s^l{|s= 0}}^lg_{sv}) \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b}\nonumber \\ &&= - \int _{\partial \Omega } {\left(\delta _{\bm{g}_b}\partial _{s^l{|s= 0}}^lg_{sv}+d\operatorname{\operatorname{tr}}_{\bm{g}_b} \partial _{s^l{|s= 0}}^lg_{sv}\right)}(n_{\partial \Omega }) dv_{{\bm{g}_b}_{|\partial _\Omega }}.\end{eqnarray}$$
(67)
Let us now turn to the remaining linear term
δ
g
b
∗
δ
g
b
∂
s
l
|
s
=
0
l
g
s
v
$\delta ^*_{\bm{g}_b}\delta _{\bm{g}_b}\partial _{s^l{|s= 0}}^lg_{sv}$
in the expression of
Φ
g
b
(
1
)
(
∂
s
l
|
s
=
0
l
g
s
v
)
${\Phi }_{\bm{g}_b}^{(1)}(\partial _{s^l{|s= 0}}^lg_{sv})$
. By integration by parts, denoting
V
=
δ
g
b
∂
s
l
|
s
=
0
l
g
s
v
$V = \delta _{\bm{g}_b}\partial _{s^l{|s= 0}}^lg_{sv}$
, we get:
∫
Ω
g
b
,
δ
g
b
∗
V
g
b
d
v
g
b
=
−
2
∫
Ω
δ
g
b
V
d
v
g
b
=
2
∫
∂
Ω
⟨
V
,
n
⟩
g
b
d
v
g
b
|
∂
Ω
,
$$\begin{equation*} \int _\Omega {\left\langle \bm{g}_b,\delta ^*_{\bm{g}_b}V \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = -2\int _\Omega \delta _{\bm{g}_b} V dv_{\bm{g}_b} = 2 \int _{\partial \Omega } \langle V,n\rangle _{\bm{g}_b} dv_{\bm{g}_b|\partial \Omega }, \end{equation*}$$
which is again a boundary term.
Noticing that
∂
s
l
|
s
=
0
l
Φ
g
b
(
g
s
v
)
−
Φ
g
b
(
1
)
∂
s
l
|
s
=
0
l
g
s
v
=
∂
s
l
|
s
=
0
l
E
(
g
s
v
)