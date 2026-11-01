---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Integrability of Einstein deformations and desingularizations]

Communications on Pure and Applied Mathematics |Wiley Online Library
Communications on Pure and Applied Mathematics
Volume 77, Issue 1
pp. 177-220
RESEARCH ARTICLE
Open Access
Integrability of Einstein deformations and desingularizations
Tristan Ozuch
,
Corresponding Author
Tristan Ozuch
[email protected]
Massachusetts Institute of Technology, Cambridge, USA
Correspondence
Tristan Ozuch, Massachusetts Institute of Technology, Cambridge, USA.
Email:
[email protected]
Search for more papers by this author
Tristan Ozuch
,
Corresponding Author
Tristan Ozuch
[email protected]
Massachusetts Institute of Technology, Cambridge, USA
Correspondence
Tristan Ozuch, Massachusetts Institute of Technology, Cambridge, USA.
Email:
[email protected]
Search for more papers by this author
First published:
26 July 2023
https://doi.org/10.1002/cpa.22129
Digital Object Identifier (DOI)
view metrics
PDF
Abstract
We study the question of the integrability of Einstein deformations and relate it to the question of the desingularization of Einstein metrics. Our main application is a negative answer to the long-standing question of whether or not every Einstein 4-orbifold (which is an Einstein metric space in a synthetic sense) is limit of smooth Einstein 4-manifolds. We more precisely show that spherical and hyperbolic 4-orbifolds with the simplest singularities cannot be Gromov-Hausdorff limits of smooth Einstein 4-metrics without relying on previous integrability assumptions. For this, we analyze the integrability of deformations of Ricci-flat ALE metrics through variations of Schoen's Pohozaev identity. Inspired by Taub's conserved quantity in General Relativity, we also introduce conserved integral quantities based on the symmetries of Einstein metrics. These quantities are obstructions to the integrability of infinitesimal Einstein deformations “closing up” inside a hypersurface – even with change of topology. We show that many previously identified obstructions to the desingularization of Einstein 4-metrics are equivalent to these quantities on Ricci-flat cones. In particular, all of the obstructions to desingularizations bubbling off Eguchi-Hanson metrics are recovered. This lets us further interpret the obstructions to the desingularization of Einstein metrics as a defect of integrability.
1 INTRODUCTION
An Einstein metric
g
satisfies, for some real number Λ, the equation
Ric
(
g
)
=
Λ
g
.
$$\begin{equation} \operatorname{\operatorname{Ric}}(\bm{g})=\Lambda \bm{g}.\end{equation}$$
(1)
In dimension 4, these metrics are considered optimal due to the homogeneity of their Ricci curvature but also as critical points of the Einstein-Hilbert functional with fixed volume,
g
↦
∫
M
R
g
d
v
g
$g\mapsto \int _M \operatorname{\operatorname{R}}_g dv_g$
, and more importantly as minimizers of the
L
2
-norm of the Riemann curvature tensor,
g
↦
∫
M
|
Rm
g
|
2
d
v
g
$g\mapsto \int _M |\operatorname{\operatorname{Rm}}_g|^2dv_g$
often interpreted as an energy.
From dimension 4, even under natural assumptions of bounded diameter (compactness) and lower bound on the volume (non-collapsing) Einstein metrics can develop singularities. This first issue means that the set of unit-volume Einstein metrics is not complete for the usual Gromov-Hausdorff distance. Moreover, it has been proven that some infinitesimal Einstein deformations may not integrate into curves of actual Einstein metrics in dimension higher than 4. This second issue shows that the moduli space of Einstein metrics itself might have singularities.
In this article, we exhibit links between the two seemingly unrelated above issues and apply the resulting analogy to the question of the desingularization of Einstein 4-manifolds.
Completion of the moduli space of Einstein 4-manifolds
One major goal for 4-dimensional geometry is to understand the structure of the compactification of the moduli space of Einstein metrics on a differentiable manifold
M
4
which is defined as
E
(
M
4
)
:
=
(
M
4
,
g
)
|
∃
Λ
∈
R
,
Ric
(
g
)
=
Λ
g
,
Vol
(
M
4
,
g
)
=
1
∕
D
(
M
4
)
,
$$\begin{equation} \bm{E}(M^4) := {\left\lbrace (M^4,\bm{g})\;|\;\exists \Lambda \in \mathbb {R},\; \operatorname{\operatorname{Ric}}(\bm{g})=\Lambda \bm{g},\; \operatorname{\operatorname{Vol}}(M^4,\bm{g})= 1\right\rbrace} \slash \mathcal {D}(M^4),\end{equation}$$
(2)
where
D
(
M
4
)
$\mathcal {D}(M^4)$
is the group of diffeomorphisms of
M
4
acting on metrics by pull-back. This space is classically equipped with the Gromov-Hausdorff distance,
d
G
H
$d_{GH}$
. The metric spaces which are limits of Einstein 4-manifolds with uniformly controlled diameter and volume, as well as the associated singularity models, have been understood for a long time in the Gromov-Hausdorff sense [
1
,
8
]: they are respectively
Einstein orbifolds
and
Ricci-flat ALE orbifolds
. The
metric completion
of
(
E
(
M
4
)
,
d
G
H
)
$(\bm{E}(M^4),d_{GH})$
is
E
(
M
4
)
∪
∂
o
E
(
M
4
)
,
$$\begin{equation} \bm{E}(M^4)\;\cup \;\partial _o\bm{E}(M^4), \end{equation}$$
(3)
where
∂
o
E
(
M
4
)
$\partial _o\bm{E}(M^4)$
is the set of
d
G
H
$d_{GH}$
-limits with bounded diameter (i.e., at finite
d
G
H
$d_{GH}$
-distance) of Einstein metrics on
M
4
.
The elements of
∂
o
E
(
M
4
)
$\partial _o\bm{E}(M^4)$
are Einstein orbifolds and a question which we answer here is the converse. Quoting Anderson [
4
]: “It has long been an open question whether Einstein orbifold metrics can be resolved to smooth Einstein metrics close to them in the Gromov-Hausdorff topology.” We will prove that this resolution is not possible for some of the simplest Einstein orbifolds: the spherical an hyperbolic ones. These orbifolds should therefore not really be considered as
singular
Einstein metrics. In order to prove this, we use the analogy between such a resolution and an Einstein deformation of a flat cone, and we study the potential nonintegrability of Ricci-flat ALE deformations.
Conserved quantities and integrability
Let
g
be an Einstein manifold on an open subset
U
$\mathcal {U}$
of a manifold. We say that
h
is an
infinitesimal Einstein deformation
of
g
on
U
$\mathcal {U}$
if the perturbation
t
↦
g
+
t
h
$t\mapsto \bm{g}+th$
satisfies (
1
) at the infinitesimal level as
t
→
0
$t\rightarrow 0$
. We say that
h
is an
integrable Einstein deformation
if on any compact in
U
$\mathcal {U}$
, there exists a smooth curve
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
such that
g
0
=
g
,
∂
t
g
t
|
t
=
0
=
h
$\partial _t{\bm{g}_t}_{|t=0} = h$
, and
for any
t
,
g
t
satisfies (
1
) with constant
Λ
(
t
)
∈
R
$\Lambda (t)\in \mathbb {R}$
.
It is clear that an integrable Einstein deformation is an infinitesimal Einstein deformation, but the converse is a very delicate question and is not always true. Counter-examples were found in [
31
] in dimension strictly higher than 4.
The question of integrability of Einstein deformations is crucial in understanding the structure of the moduli space of Einstein metrics, and a major question is whether or not such a moduli space can be really singular, see [
9
, 12.10]. It is also crucial for the behavior of Ricci flow near Einstein metrics: in the compact situation, having integrable deformations ensures optimal rates of convergence or divergence, see for instance [
26
,
27
]. In the noncompact situation, this moreover seems to be a necessary condition for the dynamical stability of Ricci-flat ALE metrics, see [
18
,
19
,
29
].
In the Lorentzian context of General Relativity, it has been proven that the question of integrability of Einstein deformations was completely ruled by the presence of symmetries.
Let us denote
E
g
(
2
)
(
h
,
h
)
$\operatorname{\operatorname{E}}^{(2)}_{\bm{g}}(h,h)$
the quadratic terms terms in the development of the Einstein tensor
h
↦
E
(
g
+
h
)
:
=
Ric
(
g
+
h
)
−
R
(
g
+
h
)
2
(
g
+
h
)
$h\mapsto \operatorname{\operatorname{E}}(\bm{g}+h):= \operatorname{\operatorname{Ric}}(\bm{g}+h) - \frac{\operatorname{\operatorname{R}}(\bm{g}+h)}{2}(\bm{g}+h)$
. For any Killing vector field
X
, a hypersurface Σ with a unit normal
n
Σ
$n_\Sigma$
and any infinitesimal Einstein deformation
h
, we define
Taub's conserved quantity
(sometimes called second Taub's number):
T
X
Σ
(
h
,
h
)
:
=
∫
Σ
E
g
(
2
)
(
h
,
h
)
(
X
,
n
Σ
)
d
v
Σ
.
$$\begin{equation} \mathcal {T}^\Sigma _{X}(h,h):=\int _\Sigma {\left(\operatorname{\operatorname{E}}^{(2)}_{\bm{g}}(h,h)\right)}(X,n_\Sigma )dv_\Sigma .\end{equation}$$
(4)
The link with the integrability of
h
is that if
h
is an integrable
Ricci-flat
deformation, then
T
X
Σ
(
h
,
h
)
$\mathcal {T}_X^\Sigma (h,h)$
has to vanish. In this sense, Taub's conserved quantities for all Killing vector fields
X
are
obstructions
to the integrability of
h
.
A remarkable and beautiful result is that in the Lorentzian context, the above obstructions are the
only
obstructions to the integrability of
h
, see [
5
,
23
]. Namely, if they vanish, then, under mild assumptions, one can construct a smooth curve of Ricci-flat metrics starting at
g
whose first jet is
h
. The hyperbolic nature of the Einstein equations in the Lorentzian context is an important aspect of the proof.
Einstein deformations of Ricci-flat cones
Let
(
C
(
S
)
,
g
C
(
S
)
)
=
(
R
+
×
S
,
d
r
2
+
r
2
g
S
)
$(C(S),\bm{g}_{C(S)})=(\mathbb {R}^+\times S, dr^2 + r^2 \bm{g}_S)$
be a
d
-dimensional Ricci-flat cone with link
(
S
,
g
S
)
$(S,\bm{g}_S)$
satisfying
Ric
(
g
S
)
=
(
d
−
2
)
g
S
$\operatorname{\operatorname{Ric}}(\bm{g}_S)=(d-2)\bm{g}_S$
. Such cones model the asymptotics of singular or complete Einstein metrics at given points or at infinity. We will mostly focus on the usual Euclidean cone
(
R
d
,
e
)
=
(
C
(
S
d
−
1
)
,
g
C
(
S
d
−
1
)
)
$(\mathbb {R}^d,\bm{e})=(C(\mathbb {S}^{d-1}),\bm{g}_{C(\mathbb {S}^{d-1})})$
and its quotients.
We extend the obstructions given by Taub's conserved quantities on the hypersurface
Σ
=
S
$\Sigma = S$
to general Einstein deformations (not necessarily Ricci-flat this time). The condition rewrites: for any Killing vector field
X
of
(
S
,
g
S
)
$(S,\bm{g}_S)$
, if
h
is integrable, then one has
T
X
S
(
h
,
h
)
=
∫
S
Ric
˚
g
C
(
S
)
(
2
)
(
h
,
h
)
(
X
,
∂
r
)
d
v
S
=
0
,
$$\begin{equation} \mathcal {T}^S_{X}(h,h)=\int _S {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{g}_{C(S)}}(h,h)\right)}(X,\partial _r)dv_S =0,\end{equation}$$
(5)
where
Ric
˚
$\mathring{\operatorname{\operatorname{Ric}}}$
is the traceless part of
Ric
$\operatorname{\operatorname{Ric}}$
and
Ric
˚
(
2
)
$ \mathring{\operatorname{\operatorname{Ric}}}^{(2)}$
its second order variation.
We moreover introduce a similar quantity based on the
conformal
Killing vector field
r
∂
r
$r\partial _r$
on the cone
C
(
S
)
$C(S)$
.
Theorem 1.1. (Informal, Proposition
3.3
)
Let
h
be an infinitesimal Einstein deformation of the Ricci-flat cone
(
C
(
S
)
,
g
C
(
S
)
)
$(C(S),\bm{g}_{C(S)})$
. Assume that
h
is either defined and bounded on the interior of
S
or on its exterior and decaying at infinity. Then, we have the following identity:
∫
S
Ric
˚
g
C
(
S
)
(
2
)
(
h
,
h
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
+
other terms
=
0
.
$$\begin{equation} \int _S {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{g}_{C(S)}}(h,h)\right)}(r\partial _r,\partial _r) dv_S+ \mbox{other terms} = 0.\end{equation}$$
(6)
In all of our situations of interest, we are able to find convenient gauges for
h
in which these
other terms
vanish thanks to some variations of Schoen's Pohozaev formula from [
41
].
Remark 1.2.
In the above case, we do not need to assume that
h
is integrable. This should rather be thought of as an obstruction to the existence of an Einstein metric which
closes up
inside
S
, that is the existence of an Einstein deformation on a compact domain whose only boundary is
S
.
As is well-known, a difficulty when considering deformations of cones is verifying that the resulting curve of metric is
complete
, see [
10
] where this is discussed for hyperkähler deformations of cones. The main issue is that such deformations typically require changes of topology. When allowing a change of topology, just as in the desingularization of Einstein 4-manifolds, one needs to consider deformations of
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
with topology
N
=
(
R
4
∕
Γ
)
∖
{
0
}
∪
Σ
$N=(\mathbb {R}^4\slash \Gamma )\backslash \lbrace 0\rbrace \cup \Sigma$
for some lower dimensional manifold Σ. The prototypical example is that of the Eguchi-Hanson metric which can be seen as an Einstein deformation of
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
on
T
∗
S
2
=
(
R
4
∕
Z
2
)
∖
{
0
}
∪
S
2
$T^*\mathbb {S}^2=(\mathbb {R}^4\slash \mathbb {Z}_2)\backslash \lbrace 0\rbrace \cup \mathbb {S}^2$
. Here, we may see the Euclidean metric
e
on
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
as living on
T
∗
S
2
$T^*\mathbb {S}^2$
while being
degenerate
on
S
2
$\mathbb {S}^2$
, that is the restriction of
e
to the submanifold
S
2
$\mathbb {S}^2$
vanishes.
In Section
3.3
, we discuss the situation of an Einstein metric coming out of
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
and closing-up inside with topology
T
∗
S
2
$T^*\mathbb {S}^2$
. Assume that there exists a smooth curve of nondegenerate Einstein metrics
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
on
(
B
e
(
0
,
1
)
∖
{
0
}
)
∪
S
2
⊂
T
∗
S
2
$ (B_{\bm{e}}(0,1)\backslash \lbrace 0\rbrace )\cup \mathbb {S}^2 \subset T^{*}\mathbb{S}^2$
with
g
0
=
e
and
∂
t
|
t
=
0
g
t
=
h
$ {\partial _t}_{|t=0}\bm{g}_t = h$
outside
S
2
$\mathbb {S}^2$
in well-chosen coordinates. Then we have the obstructions:
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
h
,
h
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
,
$$\begin{equation} \int _{\mathbb {S}^{3}\slash \mathbb {Z}_2} {\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(h,h)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^{3}\slash \mathbb {Z}_2} = 0,\end{equation}$$
(7)
and the similar ones from Killing vector fields. In that situation, an Eguchi-Hanson metric bubbles-out of the cone
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
and the link with the question of desingularization becomes clear. For some related results about hyperkähler metrics on manifolds with boundaries, see [
13
,
22
].
A natural question would be whether one could find similar obstructions on typical cones of dimension higher than 4 with codimension 4 singularities.
Question 1.3.
Can we find similar obstructions for Einstein deformations of cones on singular Einstein orbifolds like
R
k
×
(
R
4
∕
Z
2
)
$\mathbb {R}^k\times (\mathbb {R}^4\slash \mathbb {Z}_2)$
for
k
⩾
1
$k\geqslant 1$
?
Vanishing of the obstructions in dimension 4
We then test the conditions (
5
) and (
6
) considering simple Einstein deformations coming from two situations: the rescaling of Einstein metrics at a given point, and the rescaling of Ricci-flat ALE metrics at infinity, and show that they vanish for arbitrary deformations.
The vanishing of the obstructions is not surprising in the case of Einstein metrics around a given point: it has been shown that for any curvature satisfying the Einstein condition at the given point, there exists a germ of Einstein metric with the corresponding curvature in [
24
]. It implies that the obstructions (
5
) and (
7
) in this situation actually vanish in any dimension.
These results in Section
4
and the Appendix
A
can also be seen as consequences of [
3
]. Their proofs have the merit to introduce natural systems of coordinates in which the computations of the quadratic terms of Ricci curvature are convenient (and where the
other terms
of (
7
) are vanishing), we note that the ALE coordinates considered are based on [
14
]. These coordinates are crucial for the next case of the desingularization of an Einstein orbifold, where the obstructions do not vanish.
Obstruction to the desingularization of Einstein 4-manifolds
We finally study the degeneration of Einstein 4-manifolds, that is the
d
G
H
$d_{GH}$
-convergence of metrics in
E
(
M
) to the boundary
∂
o
E
(
M
)
$\partial _o\bm{E}(M)$
, and its reverse operation: the
desingularization
. Given an element in
∂
o
E
(
M
)
$\partial _o\bm{E}(M)$
, the desingularization consists in finding a
d
G
H
$d_{GH}$
-approximating sequence of metrics in
E
(
M
).
Any
smooth Einstein 4-manifold close to a compact Einstein orbifold in a mere Gromov-Hausdorff sense has been recently been produced by a gluing-perturbation procedure [
36
,
37
]. Here, this lets us understand the obstructions to the
d
G
H
$d_{GH}$
-desingularization of an Einstein orbifold through obstructions similar to (
5
) and (
7
).
Theorem 1.4. (Theorem
5.6
)
Assume that there exists a sequence of Einstein metrics
(
M
,
g
n
)
n
$(M,\bm{g}_n)_n$
converging in the Gromov-Hausdorff sense to an Einstein orbifold
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
with a singularity
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
at
p
and satisfying
Ric
(
g
o
)
=
Λ
g
o
$\operatorname{\operatorname{Ric}}(\bm{g}_o) = \Lambda \bm{g}_o$
. Assume that there exist numbers
t
n
>
0
$t_n&gt;0$
such that at
p
,
(
M
,
g
n
/
t
n
)
n
$(M,\bm{g}_n/t_n)_n$
converges to a Ricci-flat ALE
manifold
(
N
,
g
b
)
$(N,\bm{g}_b)$
asymptotic to
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
with
integrable
infinitesimal deformations. Consider the following asymptotics in well-chosen gauges (in a so-called
volume gauge
for
g
b
):
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
and
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
,
$$\begin{equation*} \bm{g}_o = \bm{e} + H_2 + \mathcal {O}(r^3) \;\text{ and }\;\bm{g}_b = \bm{e} + H^4 + \mathcal {O}(r^{-5}), \end{equation*}$$
for
|
H
2
|
e
∼
r
2
$|H_2|_{\bm{e}} \sim r^2$
and
|
H
4
|
e
∼
r
−
4
$|H^4|_{\bm{e}} \sim r^{-4}$
.
Then, the following obstructions analogous to (
5
) and (
7
) hold: for any
Y
Killing vector field of
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
:
∫
S
3
/
Γ
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
Y
,
∂
r
)
d
v
S
3
/
Γ
=
0
,
$$\begin{equation} \int _{\mathbb {S}^{3}/\Gamma } {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H^4,H_2)\right)}(Y,\partial _r) dv_{\mathbb {S}^{3}/\Gamma }=0,\end{equation}$$
(8)
and
∫
S
3
/
Γ
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
/
Γ
=
0
.
$$\begin{equation} \int _{\mathbb {S}^{3}/\Gamma } {\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{e}}(H^4,H_2)\right)}(r\partial _r,\partial _r) dv_{\mathbb {S}^{3}/\Gamma }=0.\end{equation}$$
(9)
Comparing (
5
) to (
8
) and (
7
) to (
9
), we therefore interpret the obstructions to the desingularization of an Einstein orbifold as a defect of integrability of the infinitesimal Einstein deformation
h
=
H
2
+
H
4
$h=H_2+H^4$
of
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
. The proof of these different obstructions actually relies on the control of the same integration by parts as Theorem
1.1
once one notices that in so-called
volume gauge
, the vector field
r
∂
r
$r\partial _r$
is
g
b
-harmonic at an order higher than expected.
Remark 1.5.
Denote
V
(
g
b
)
<
0
$ \mathcal {V}(\bm{g}_b) &lt;0$
the
reduced volume
of
(
N
,
g
b
)
$(N,\bm{g}_b)$
introduced in [
14
], as well as
W
g
o
±
$ W^\pm _{\bm{g}_o}$
the Weyl curvatures of
g
o
at
p
and
W
g
b
±
$W^\pm _{\bm{g}_b}$
the asymptotic Weyl curvatures (the part decaying like
r
−
6
$r^{-6}$
) of
g
b
. Then, it is shown in the proof of Theorem
5.6
that (
9
) may rewrite as:
Λ
V
(
g
b
)
+
Q
W
g
b
+
,
W
g
o
−
+
Q
W
g
b
−
,
W
g
o
+
=
0
$$\begin{equation} \Lambda \mathcal {V}(\bm{g}_b) + Q{\left(W^+_{\bm{g}_b}, W^-_{\bm{g}_o}\right)} + Q{\left(W^-_{\bm{g}_b}, W^+_{\bm{g}_o}\right)}=0\end{equation}$$
(10)
for some explicit quadratic form
Q
. A similar rewriting of (
8
) yields
Q
′
(
W
g
b
+
,
W
g
o
−
)
+
Q
′
(
W
g
b
−
,
W
g
o
+
)
=
0
$Q^{\prime }(W^+_{\bm{g}_b}, W^-_{\bm{g}_o}) + Q^{\prime }(W^-_{\bm{g}_b}, W^+_{\bm{g}_o})=0$
for some other explicit quadratic form
Q
′
$Q^{\prime }$
.
Remark 1.6.
For
g
o
either spherical of hyperbolic, one has
Λ
≠
0
$\Lambda \ne 0$
and
W
g
o
±
=
0
$W^\pm _{\bm{g}_o} =0$
. The obstruction (
10
) is therefore
never
satisfied. We also recover that the obstruction vanishes for the gluing of a hyperkähler ALE to a hyperkähler orbifold since
Λ
=
0
$\Lambda = 0$
,
W
g
o
+
=
0
$W^+_{{\bm{g}_o}} = 0$
and
W
g
b
+
=
0
$W^+_{\bm{g}_b}=0$
.
We recover
all
of the obstructions to the desingularization by Eguchi-Hanson metrics identified in [
11
], see Corollary
5.10
and an extension to higher dimension yields the obstruction of [
33
] as well, see Corollary
5.17
. In these articles, the obstructions were purely
analytical
as projections on the cokernel of the linearized operator. Theorem
1.4
gives a new maybe more
geometric
interpretation of them.
Remark 1.7.
There are higher order obstructions to the existence of Einstein deformations with asymptotic developments
g
t
=
g
+
t
h
1
+
t
2
h
2
+
⋯
$\bm{g}_t =\bm{g} + th_{1} + t^2h_2 +\cdots$
for small
t
which are very similar to the obstructions (
9
) and (
8
).
Question 1.8.
Can these higher order obstructions recover the higher order obstructions of [
39
]? Can they help compute even higher order obstructions?
Desingularization of spherical and hyperbolic orbifolds
We next get to the main application of this article. We answer negatively the classical question of whether or not
all
Einstein 4-orbifolds can be
d
G
H
$d_{GH}$
-desingularized by smooth Einstein 4-manifolds.
Theorem 1.9.
A spherical or hyperbolic 4-orbifold with at least one singularity
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
cannot be limit of smooth Einstein metrics in the Gromov-Hausdorff sense.
Example 1.10.
Consider
S
4
⊂
R
5
$\mathbb {S}^4\subset \mathbb {R}^5$
and the quotient by
Z
2
$\mathbb {Z}_2$
given by
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
,
x
5
)
∼
(
x
1
,
−
x
2
,
−
x
3
,
−
x
4
,
−
x
5
)
$(x_1,x_2,x_3,x_4,x_5) \sim (x_1,-x_2,-x_3,-x_4,-x_5)$
. We will denote this space
S
4
∕
Z
2
$\mathbb {S}^4\slash \mathbb {Z}_2$
which is an Einstein orbifold with two
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
singularities. It is often called the
American football metric
. It is a
synthetic
Einstein space in the sense of [
34
] for instance. By the above Theorem
1.9
, it cannot be a Gromov-Hausdorff limit of smooth Einstein metrics.
Theorem
1.9
was conjectured in the author's PhD thesis [
38
] where it was proven under a technical assumption of integrability for the Ricci-flat ALE spaces. The main remaining difficulty here is thus to deal with the potential non integrability of these deformations. We more precisely prove that Theorem
1.4
holds without the integrability assumption on the Ricci-flat ALE spaces. Remark
1.6
then lets us conclude.
Remark 1.11.
It is often conjectured that the only Ricci-flat ALE metrics are Kähler, hence integrable. However, the motivation of this conjecture formulated in [
8
] for instance, seems to be the analogous conjecture for the selfduality of Yang-Mills connections on
S
U
(
2
)
$SU(2)$
bundles over
S
4
$\mathbb {S}^4$
. This analogous conjecture was disproved the same year in [
42
].
Let us present the main step of the proof of Theorem
1.9
which is of independent interest. Let
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
. Its space of
L
2
-infinitesimal deformations which are traceless and in divergence-free gauge is denoted
O
(
g
b
). There are particular elements in
O
(
g
b
) coming from the symmetries of the asymptotic cone
R
4
∕
Γ
$\mathbb {R}^4\slash \Gamma$
. According to [
38
]:
there exists
X
a harmonic vector field on
(
N
,
g
b
)
$(N,\bm{g}_b)$
asymptotic to the
conformal Killing vector field
r
∂
r
$r\partial _r$
, and
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
$(\mathcal {L}_X\bm{g}_b)^\circ \in \bm{O}(\bm{g}_b)$
, where
(
h
)
∘
$ (h)^\circ$
denotes the traceless part of a symmetric 2-tensor
h
,
for any
Killing vector field
Y
there exists
Y
′
$Y^{\prime }$
a harmonic vector field on
(
N
,
g
b
)
$(N,\bm{g}_b)$
asymptotic to
Y
, and
L
Y
′
g
b
∈
O
(
g
b
)
$\mathcal {L}_{Y^{\prime }}\bm{g}_b\in \bm{O}(\bm{g}_b)$
.
The main step in the proof of Theorem
1.9
is to show that the obstructions to the integrability of an infinitesimal deformation of
g
b
are negligible in the direction of the above deformations
(
L
X
g
b
)
∘
$(\mathcal {L}_X\bm{g}_b)^\circ$
and
L
Y
′
g
b
$\mathcal {L}_{Y^{\prime }}\bm{g}_b$
. More precisely, for
v
∈
O
(
g
b
)
$v\in \bm{O}(\bm{g}_b)$
, let us consider
g
v
$ g_v$
the unique solution to:
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
$$\begin{equation} \begin{aligned} {\Phi}_{\bm{g}_b}(g_v) = \operatorname{\operatorname{E}}(g_v) + \delta ^{*}_{{\bm{g}}_{b}}\delta _{{\bm{g}}_{b}} g_v\in \bm{O}(\bm{g}_b)\end{aligned} \end{equation}$$
(11)
satisfying
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
$g_v - (\bm{g}_b+v)\perp _{L^2(\bm{g}_b)} \bm{O}(\bm{g}_b)$
. We call
Einstein modulo obstructions metrics
such deformations which have been constructed in [
37
] (see also [
32
] in the smooth compact case, where a different vocabulary is used). We study the leading order of the obstruction along curves
s
↦
g
s
v
$s\mapsto g_{sv}$
for
s
∈
(
−
1
,
1
)
$s\in (-1,1)$
at
s
=
0
$s=0$
.
Proposition 1.12.
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be a Ricci-flat ALE metric which has
nonintegrable
Ricci-flat ALE deformations. Then, for any
v
∈
O
(
g
b
)
$v\in \bm{O}(\bm{g}_b)$
, there exists
l
⩾
2
$l\geqslant 2$
such that
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
$\partial ^{k}_{s^{k}|s=0} {\Phi }_{{\bm{g}}_{b}}(g_{sv}) = 0$
for all
k
⩽
l
−
1
$k\leqslant l-1$
and
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
≠
0
$\partial ^{l}_{s^{l}|s=0} {\Phi }_{{\bm{g}}_{b}}(g_{sv}) \ne 0$
. The leading order obstruction
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
$\partial ^{l}_{s^{l}|s=0} {\Phi }_{{\bm{g}}_{b}}(g_{sv})$
is
L
2
(
g
b
)
$L^2(\bm{g}_b)$
-orthogonal to the vector subspace of
O
(
g
b
) spanned by the above elements
(
L
X
g
b
)
∘
$(\mathcal {L}_X\bm{g}_b)^\circ$
and
L
Y
′
g
b
$\mathcal {L}_{Y^{\prime }}\bm{g}_b$
.
The proof relies on careful integrations by parts similar to that of the proof of Theorem
1.1
.
2 SYMMETRIES OF EINSTEIN METRICS AND INTEGRABILITY
In this section, we recall well-known properties of the two first derivatives of the Einstein operator and apply them to define the so-called
Taub's conserved quantity
as introduced in [
43
]. It is a central quantity in the study of the integrability of Einstein deformations in the Lorentzian context.
Note 2.1.
All along the article, we will denote by
F
g
(
m
)
$F_g^{(m)}$
the
m
-linear terms of the development of a functional
h
↦
F
(
g
+
h
)
$h\mapsto F(g+h)$
at 0, we more precisely have (at least formally) for any small enough 2-tensor
h
:
F
(
g
+
h
)
=
∑
m
∈
N
1
m
!
F
g
(
m
)
(
h
,
…
,
h
)
︸
m
times
.
$$\begin{equation*} F(g+h) = \sum _{m\in \mathbb {N}}\frac{1}{m!}F_g^{(m)}\underbrace{(h,\ldots,h)}_{m \text{ times }}. \end{equation*}$$
2.1 Gauge and reparametrization properties
Let us start by recalling various consequences of the Bianchi identity: for any Riemannian metric
g
, one has
B
g
(
Ric
(
g
)
)
=
0
,
$$\begin{equation} B_g(\operatorname{\operatorname{Ric}}(g)) = 0,\end{equation}$$
(12)
where for any 2-tensor
h
, we define the
Bianchi operator
B
g
h
=
δ
g
(
h
−
1
2
tr
(
h
)
g
)
=
δ
g
h
+
1
2
d
tr
(
h
)
$ B_g h = \delta _g(h -  \frac{1}{2}\mbox{tr}(h)g ) = \delta _g h +  \frac{1}{2}d\mbox{tr}(h)$
, where
δ
g
$\delta _g$
is the divergence with the convention that in coordinates, for a 1-form ω,
δ
g
ω
:
=
−
g
i
j
∇
j
ω
i
$\delta _g\omega := -g^{ij}\nabla _j\omega _{i}$
and for a symmetric 2-tensor
h
,
(
δ
g
h
)
k
:
=
−
g
i
j
∇
j
h
i
k
$(\delta _gh)_k := -g^{ij}\nabla _jh_{ik}$
. Denoting the Einstein tensor
E
(
g
)
:
=
Ric
(
g
)
−
R
g
2
g
$\operatorname{\operatorname{E}}(g):=\operatorname{\operatorname{Ric}}(g) - \frac{\operatorname{\operatorname{R}}_g}{2}g$
, the Equation (
12
) rewrites
δ
g
(
E
(
g
)
)
=
0
.
$$\begin{equation} \delta _g(\operatorname{\operatorname{E}}(g)) = 0.\end{equation}$$
(13)
Proposition 2.2. ([[
23
]])
Let us assume that
g
is a Ricci-flat metric on some open domain
U
$\mathcal {U}$
of a Riemannian manifold
M
, and let
h
be a symmetric 2-tensor on
U
$\mathcal {U}$
. We have the following gauge properties:
without assumption, one has
B
g
Ric
g
(
1
)
(
h
)
=
0
,
and
δ
g
E
g
(
1
)
(
h
)
=
0
,
$$\begin{equation} B_{\bm{g}}{\left(\operatorname{\operatorname{Ric}}_{\bm{g}}^{(1)}(h)\right)}= 0, \text{ and } \delta _{\bm{g}}{\left(\operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(h)\right)}= 0,\end{equation}$$
(14)
if
Ric
g
(
1
)
(
h
)
=
Λ
g
$\operatorname{\operatorname{Ric}}_{\bm{g}}^{(1)}(h)=\Lambda g$
for
Λ
∈
R
$\Lambda \in \mathbb {R}$
or equivalently
E
g
(
1
)
(
h
)
+
λ
g
=
0
$\operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(h)+ \lambda g=0$
for
λ
∈
R
$\lambda \in \mathbb {R}$
, then one has
B
g
Ric
g
(
2
)
(
h
,
h
)
=
0
,
and
δ
g
E
g
(
2
)
(
h
,
h
)
=
0
.
$$\begin{equation} B_{\bm{g}}{\left(\operatorname{\operatorname{Ric}}_{\bm{g}}^{(2)}(h,h)\right)}= 0, \text{ and } \delta _{\bm{g}}{\left(\operatorname{\operatorname{E}}_{\bm{g}}^{(2)}(h,h)\right)}= 0.\end{equation}$$
(15)
Let us continue with some identities when
g
is perturbed in the direction of a Lie derivative. These come from differentiation of the following identity: for any diffeomorphism
ϕ
:
M
→
M
$\phi :M\rightarrow M$
and any metric
g
on M
Ric
(
ϕ
∗
g
)
=
ϕ
∗
(
Ric
(
g
)
)
and
E
(
ϕ
∗
g
)
=
ϕ
∗
(
E
(
g
)
)
.
$$\begin{equation} \operatorname{\operatorname{Ric}}(\phi ^*g) = \phi ^*(\operatorname{\operatorname{Ric}}(g)) \text{ and } \operatorname{\operatorname{E}}(\phi ^*g) = \phi ^*(\operatorname{\operatorname{E}}(g)). \end{equation}$$
(16)
Proposition 2.3. ([[
23
]])
Let us assume that
g
is a Riemannian metric on some bounded open domain
U
$\mathcal {U}$
of a Riemannian manifold
M
, let
h
be a symmetric 2-tensor on
U
$\mathcal {U}$
and
X
be a vector field on
U
$\mathcal {U}$
. We have the following reparametrization properties for the derivatives of
Ric
$\operatorname{\operatorname{Ric}}$
: without assumption, one has
Ric
g
(
1
)
(
L
X
g
)
=
L
X
(
Ric
(
g
)
)
and
E
g
(
1
)
(
L
X
g
)
=
L
X
(
E
(
g
)
)
,
$$\begin{equation} \operatorname{\operatorname{Ric}}_g^{(1)}(\mathcal {L}_Xg)= \mathcal {L}_X(\operatorname{\operatorname{Ric}}(g)) \text{ and } \operatorname{\operatorname{E}}_g^{(1)}(\mathcal {L}_Xg)= \mathcal {L}_X(\operatorname{\operatorname{E}}(g)), \end{equation}$$
(17)
Ric
g
(
2
)
(
h
,
L
X
g
)
+
Ric
g
(
1
)
(
L
X
h
)
=
L
X
Ric
g
(
1
)
(
h
)
,
$$\begin{equation} \operatorname{\operatorname{Ric}}_g^{(2)}(h,\mathcal {L}_Xg) + \operatorname{\operatorname{Ric}}_g^{(1)}(\mathcal {L}_Xh)= \mathcal {L}_X\left(\operatorname{\operatorname{Ric}}_g^{(1)}(h)\right), \end{equation}$$
(18)
and
E
g
(
2
)
(
h
,
L
X
g
)
+
E
g
(
1
)
(
L
X
h
)
=
L
X
E
g
(
1
)
(
h
)
$$\begin{equation} \operatorname{\operatorname{E}}_g^{(2)}(h,\mathcal {L}_Xg) + \operatorname{\operatorname{E}}_g^{(1)}(\mathcal {L}_Xh)= \mathcal {L}_X\left(\operatorname{\operatorname{E}}_g^{(1)}(h)\right)\end{equation}$$
(19)
2.2 Taub's conserved quantities and obstructions
Let us start by stating the following classical integrations by parts which are at the core of our proofs.
Lemma 2.4.
Let
g
be a metric on an open set
U
$\mathcal {U}$
,
T
be a
divergence-free
symmetric 2-tensor, and let
X
be a vector field on
U
$\mathcal {U}$
. Then for any smooth compact subset
Ω
⊂
U
$\Omega \subset \mathcal {U}$
with boundary, we have:
∫
∂
Ω
T
(
X
,
n
)
d
v
g
|
∂
Ω
=
∫
Ω
T
,
δ
g
∗
X
g
d
v
g
=
1
2
∫
Ω
T
,
L
X
g
g
d
v
g
,
$$\begin{equation} \int _{\partial \Omega }T(X,n) dv_{g_{|\partial \Omega }}= \int _{\Omega }{\left\langle T,\delta _g^*X \right\rangle} _g dv_g = \frac{1}{2}\int _{\Omega }{\left\langle T,\mathcal {L}_Xg \right\rangle} _g dv_g,\end{equation}$$
(20)
where
n
is the outward unit normal to
∂
Ω
$\partial \Omega$
, and
δ
g
∗
X
:
=
1
2
L
X
g
$\delta _g^*X := \frac{1}{2}\mathcal {L}_{X}g$
is the formal adjoint of the divergence
δ
g
$\delta _g$
.
We also have the following identity close to Schoen's Pohozaev equality [
41
]. Denote
h
˚
$ \mathring{h}$
or
(
h
)
∘
$(h)^\circ$
the traceless part of a symmetric 2-tensor
h
. If
T
is divergence-free, then we have:
∫
∂
Ω
T
˚
(
X
,
n
)
d
v
g
|
∂
Ω
=
∫
Ω
1
2
T
˚
,
L
X
g
g
−
L
X
(
tr
g
T
)
d
d
v
g
=
∫
Ω
1
2
T
,
(
L
X
g
)
∘
g
−
L
X
(
tr
g
T
)
d
d
v
g
,
$$\begin{eqnarray} \int _{\partial \Omega }\mathring{T}(X,n) dv_{g_{|\partial \Omega }} &=& \int _{\Omega }{\left(\frac{1}{2}{\left\langle \mathring{T},\mathcal {L}_Xg \right\rangle} _g - \frac{\mathcal {L}_X (\operatorname{\operatorname{tr}}_g T)}{d}\right)} dv_g \nonumber\\ &=& \int _{\Omega }{\left(\frac{1}{2}{\left\langle T,(\mathcal {L}_Xg)^\circ \right\rangle} _g- \frac{\mathcal {L}_X (\operatorname{\operatorname{tr}}_g T)}{d}\right)} dv_g,\end{eqnarray}$$
(21)
Remark 2.5.
We will often abusively apply our operators to vector fields or 1-forms indifferently, the identification will always be done thanks to the metric involved in the operator. More precisely, a vector field
X
is identified with the 1-form
g
(
X
,
.
)
$g(X,.)$
.
Proof.
The key to this formula is the classical identity:
δ
g
T
(
X
)
=
δ
g
(
T
)
(
X
)
−
⟨
T
,
δ
g
∗
X
⟩
g
=
δ
g
(
T
)
(
X
)
−
1
2
⟨
T
,
L
X
g
⟩
g
$$\begin{equation} \delta _g{\left(T(X)\right)}= \delta _g(T)(X) - \langle T,\delta _g^*X \rangle _g = \delta _g(T)(X) - \frac{1}{2} \langle T,\mathcal {L}_Xg \rangle _g\end{equation}$$
(22)
which may be proven in coordinates using the symmetry of
T
. From the identity (
22
), using the fact that
T
is divergence-free and the divergence theorem, we find the result by the divergence theorem.
The second equality (
21
) then follows by noting that
∫
Ω
tr
g
T
d
⟨
g
,
L
X
g
⟩
g
d
v
g
=
−
1
d
∫
Ω
(
tr
g
T
)
δ
g
(
X
)
d
v
g
=
−
2
∫
Ω
L
X
(
tr
g
T
)
d
v
g
+
∫
∂
Ω
(
tr
g
T
)
g
(
X
,
n
)
.
$$\begin{equation*} \int _\Omega \frac{\operatorname{\operatorname{tr}}_g T}{d}\langle g, \mathcal {L}_Xg \rangle _gdv_g = -\frac{1}{d} \int _\Omega (\operatorname{\operatorname{tr}}_g T) \delta _g(X) dv_g = -2\int _\Omega \mathcal {L}_X(\operatorname{\operatorname{tr}}_g T) dv_g + \int _{\partial \Omega } (\operatorname{\operatorname{tr}}_g T) g(X,n). \end{equation*}$$
□
$\Box$
Let
g
be an Einstein metric on an open subset
U
$\mathcal {U}$
. For a vector field
X
, a closed orientable hypersurface
Σ
⊂
U
$\Sigma \subset \mathcal {U}$
and symmetric 2-tensors
h
and
k
on
U
$\mathcal {U}$
we define the following quantity:
B
X
Σ
(
h
)
:
=
∫
Σ
E
g
(
1
)
(
h
)
(
X
,
n
Σ
)
d
v
Σ
,
$$\begin{equation} \mathcal {B}_X^\Sigma (h):=\int _\Sigma {\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(h)\right)}(X,n_\Sigma )dv_\Sigma ,\end{equation}$$
(23)
where
n
Σ
$n_\Sigma$
is the normal to Σ. We also define the so-called
Taub's conserved quantity
introduced in [
43
]:
T
X
Σ
(
h
,
k
)
:
=
∫
Σ
E
g
(
2
)
(
h
,
k
)
(
X
,
n
Σ
)
d
v
Σ
.
$$\begin{equation} \mathcal {T}_X^\Sigma (h,k):=\int _\Sigma {\left(\operatorname{\operatorname{E}}^{(2)}_{\bm{g}}(h,k)\right)}(X,n_\Sigma )dv_\Sigma .\end{equation}$$
(24)
Together with the gauge properties of Proposition
2.2
, we use Lemma
2.4
to prove the following properties for
T
$\mathcal {T}$
and
B
$\mathcal {B}$
.
Proposition 2.6.
Let
g
be an Einstein metric on an open subset
U
$\mathcal {U}$
,
X
be a Killing vector field,
h
a 2-tensor on
U
$\mathcal {U}$
, and Σ and
Σ
′
$\Sigma ^{\prime }$
two closed hypersurfaces in
U
$\mathcal {U}$
bounding an open subset
Ω
⊂
U
$\Omega \subset \mathcal {U}$
. Then, we have the following properties:
(1)
without additional assumption,
B
X
Σ
(
h
)
=
0
,
$$\begin{equation} \mathcal {B}_X^\Sigma (h) = 0,\end{equation}$$
(25)
(2)
if
E
g
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(h)=0$
, then one has:
T
X
Σ
′
(
h
,
h
)
=
T
X
Σ
(
h
,
h
)
$\mathcal {T}_X^{\Sigma ^{\prime }}(h,h) = \mathcal {T}_{X}^\Sigma (h,h)$
and
(3)
if
E
g
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(h)=0$
, and for any vector field
Y
on
U
$\mathcal {U}$
, we have
T
X
Σ
(
h
+
L
Y
g
,
h
+
L
Y
g
)
=
T
X
Σ
(
h
,
h
)
$\mathcal {T}_X^{\Sigma }(h + \mathcal {L}_Y\bm{g},h+ \mathcal {L}_Y\bm{g}) = \mathcal {T}_{X}^\Sigma (h,h)$
.
Proof.
Consider χ a cut-off function vanishing in the neighborhood of
Σ
′
$\Sigma ^{\prime }$
and equal to 1 on a neighborhood of Σ. We can therefore apply (
20
) on Ω bounded by Σ and
Σ
′
$\Sigma ^{\prime }$
to the Killing vector field
X
and
T
=
E
(
1
)
(
χ
h
)
$T = \operatorname{\operatorname{E}}^{(1)}(\chi h)$
which is divergence-free by (
14
) to find:
B
X
Σ
(
h
)
=
∫
∂
Ω
E
(
1
)
(
χ
h
)
(
X
,
n
)
d
v
∂
Ω
=
0
.
$$\begin{equation*} \mathcal {B}_X^\Sigma (h) =\int _{\partial \Omega } {\left(\operatorname{\operatorname{E}}^{(1)}(\chi h)\right)}(X,n)dv_{\partial \Omega } = 0. \end{equation*}$$
See [
23
] for the other equalities.
□
$\Box$
2.3 Integrability of Einstein deformations
In the Lorentzian context, it is a remarkable result that the quantities
T
Σ
X
(
h
,
h
)
$\mathcal {T}_\Sigma ^X(h,h)$
for the different Killing vector fields
X
of
g
and
h
satisfying
E
g
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(h)=0$
completely characterize the integrability of the infinitesimal Einstein deformation
h
.
Definition 2.7. (Integrable 2-tensor)
Let
g
be an Einstein metric on
U
$\mathcal {U}$
. A 2-tensor
h
is
integrable
if on any compact
K
⊂
U
$K\subset \mathcal {U}$
, there exists a smooth curve of Einstein metrics
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
on
K
satisfying
∂
t
g
t
|
t
=
0
=
h
$ \partial _t{\bm{g}_t}_{|t=0}=h$
.
The link between the integral quantity
T
Σ
X
(
h
,
h
)
$\mathcal {T}_\Sigma ^X(h,h)$
and the integrability of
h
is given by the following proposition.
Proposition 2.8. ([[
23
], Proposition 1.7])
Assume that
g
is a Ricci-flat metric on an open subset
U
$\mathcal {U}$
, that
h
is an integrable 2-tensor which is the first jet of a curve of Ricci-flat metrics and
X
is a Killing vector field. Then, for any compact hypersurface
Σ
⊂
U
$\Sigma \subset \mathcal {U}$
, one has
T
X
Σ
(
h
,
h
)
=
0
.
$$\begin{equation} \mathcal {T}_X^\Sigma (h,h)=0.\end{equation}$$
(26)
Proof.
Let
K
be a compact subset of
U
$\mathcal {U}$
and
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
a smooth curve of Einstein metrics on
K
with
g
0
=
g
satisfying
∂
t
g
t
|
t
=
0
=
h
$\partial _t{\bm{g}_t}_{|t=0}=h$
with
E
(
g
t
)
=
0
$\operatorname{\operatorname{E}}(\bm{g}_t) = 0$
for all
t
∈
[
0
,
1
]
$t\in [0,1]$
. We have
0
=
∂
t
(
E
(
g
t
)
)
|
t
=
0
=
E
g
(
1
)
(
h
)
$ 0=\partial _t (\operatorname{\operatorname{E}}(\bm{g}_t))_{|t=0} = \operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(h)$
, and if we denote
k
:
=
∂
t
2
2
g
t
|
t
=
0
$ k:= \partial ^2_{t^2}{\bm{g}_t}_{|t=0}$
, then we have
0
=
∂
t
2
2
(
E
(
g
t
)
)
|
t
=
0
=
E
g
(
1
)
(
k
)
+
E
g
(
2
)
(
h
,
h
)
.
$$\begin{equation*} 0=\partial ^2_{t^2} (\operatorname{\operatorname{E}}(\bm{g}_t))_{|t=0} = \operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(k) + \operatorname{\operatorname{E}}_{\bm{g}}^{(2)}(h,h). \end{equation*}$$
In particular, we have:
T
X
Σ
(
h
,
h
)
=
−
B
X
Σ
(
k
)
=
0
$\mathcal {T}_X^\Sigma (h,h) = -\mathcal {B}_X^\Sigma (k)=0$
by (
25
).
□
$\Box$
We add an extension to Einstein but not necessarily Ricci-flat deformation of a Ricci-flat metric. This time we need to assume that the Killing vector field is tangent to our hypersurface. This will always be satisfied in our applications.
Proposition 2.9.
Assume that
g
is a Ricci-flat metric on an open subset
U
$\mathcal {U}$
, that
h
is a 2-tensor which is the first jet of a smooth curve of Einstein metrics starting at
g
and
X
is a Killing vector field for
g
. Then, for any compact hypersurface
Σ
⊂
U
$\Sigma \subset \mathcal {U}$
for which
X
is tangent to Σ once restricted to Σ, one has
∫
Σ
Ric
˚
g
(
2
)
(
h
,
h
)
(
X
,
n
Σ
)
d
v
Σ
=
0
.
$$\begin{equation} \int _{\Sigma }{\left(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{g}}(h,h)\right)}(X,n_\Sigma )dv_\Sigma =0.\end{equation}$$
(27)
Proof.
Let
K
⊂
U
$K\subset \mathcal {U}$
be a compact and
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
a smooth curve of Einstein metrics on
K
with
g
0
=
g
satisfying
∂
t
g
t
|
t
=
0
=
h
$\partial _t{\bm{g}_t}_{|t=0}=h$
with
E
(
g
t
)
+
λ
(
t
)
g
t
=
0
$\operatorname{\operatorname{E}}(\bm{g}_t) +\lambda (t)\bm{g}_t=0$
for a smooth function
t
∈
[
0
,
1
]
↦
λ
(
t
)
∈
R
$t\in [0,1]\mapsto \lambda (t)\in \mathbb {R}$
for all
t
∈
[
0
,
1
]
$t\in [0,1]$
. We have
0
=
∂
t
(
E
(
g
t
)
+
λ
(
t
)
g
t
)
|
t
=
0
=
E
g
(
1
)
(
h
)
+
λ
′
(
0
)
g
,
$$\begin{equation*} 0=\partial _t (\operatorname{\operatorname{E}}(\bm{g}_t) +\lambda (t)\bm{g}_t)_{|t=0} = \operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(h)+\lambda ^{\prime }(0)\bm{g}, \end{equation*}$$
and if we denote
k
:
=
∂
t
2
2
g
t
|
t
=
0
$ k:= \partial ^2_{t^2}{\bm{g}_t}_{|t=0}$
, then we find
0
=
∂
t
2
2
(
E
(
g
t
)
+
λ
(
t
)
g
t
)
|
t
=
0
=
E
g
(
1
)
(
k
)
+
E
g
(
2
)
(
h
,
h
)
+
λ
′
′
(
0
)
g
+
2
λ
′
(
0
)
h
.
$$\begin{equation*} 0=\partial ^2_{t^2} (\operatorname{\operatorname{E}}(\bm{g}_t) +\lambda (t)\bm{g}_t)_{|t=0} = \operatorname{\operatorname{E}}_{\bm{g}}^{(1)}(k) + \operatorname{\operatorname{E}}_{\bm{g}}^{(2)}(h,h) +\lambda ^{\prime \prime }(0)\bm{g}+2\lambda ^{\prime }(0)h. \end{equation*}$$
In particular, since for any metric
g
, one has
Ric
˚
(
g
)
=
E
(
g
)
−
tr
g
E
(
g
)
d
g
$\mathring{\operatorname{\operatorname{Ric}}}(g) = \operatorname{\operatorname{E}}(g) -\frac{\operatorname{\operatorname{tr}}_g\operatorname{\operatorname{E}}(g)}{d}g$
in dimension
d
, we find:
Ric
˚
g
(
2
)
(
h
,
h
)
=
E
g
(
2
)
(
h
,
h
)
−
1
d
(
tr
E
)
g
(
2
)
(
h
,
h
)
g
−
2
d
tr
g
E
g
(
1
)
(
h
)
h
=
E
g
(
2
)
(
h
,
h
)
−
1
d
(
tr
E
)
g
(
2
)
(
h
,
h
)
g
+
2
λ
′
(
0
)
h
.
$$\begin{align} \mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{g}}(h,h) &= \operatorname{\operatorname{E}}^{(2)}_{\bm{g}}(h,h) -\frac{1}{d}{\left((\operatorname{\operatorname{tr}}\operatorname{\operatorname{E}})_{\bm{g}}^{(2)}(h,h)\right)}\bm{g} -\frac{2}{d}\operatorname{\operatorname{tr}}_{\bm{g}}\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(h) h\nonumber \\ &=\operatorname{\operatorname{E}}^{(2)}_{\bm{g}}(h,h) -\frac{1}{d}{\left((\operatorname{\operatorname{tr}}\operatorname{\operatorname{E}})_{\bm{g}}^{(2)}(h,h)\right)}\bm{g}+2\lambda ^{\prime }(0) h.\end{align}$$
(28)
We consequently have:
∫
Σ
(
Ric
˚
g
(
2
)
(
h
,
h
)
)
(
X
,
n
Σ
)
d
v
Σ
=
−
∫
Σ
(
E
g
(
1
)
(
k
)
)
(
X
,
n
Σ
)
d
v
Σ
=
0
$\int _{\Sigma }(\mathring{\operatorname{\operatorname{Ric}}}^{(2)}_{\bm{g}}(h,h))(X,n_\Sigma )dv_\Sigma = -\int _{\Sigma } (\operatorname{\operatorname{E}}^{(1)}_{\bm{g}}(k))(X,n_\Sigma )dv_\Sigma = 0$
because
g
(
X
,
n
Σ
)
=
0
$\bm{g}(X,n_\Sigma )=0$
by assumption and thanks to (
25
).
□
$\Box$
Question 2.10.
Can we recover the obstructions to integrability of [
31
] (or new ones) thanks to the above criterion?
3 CONSERVED QUANTITIES ON RICCI-FLAT CONES AND INTEGRABILITY
We introduce another quantity similar to Taub's adapted to perturbations of Ricci-flat cones
(
C
(
Σ
)
,
d
r
2
+
r
2
g
Σ
)
$(C(\Sigma ),dr^2+r^2g_\Sigma )$
. We will mostly work with the Euclidean case
Σ
=
S
d
−
1
$\Sigma =\mathbb {S}^{d-1}$
.
3.1 A conserved quantity on
R
d
$\mathbb {R}^d$
and other Ricci-flat cones
Let us now introduce a functional similar to Taub's conserved quantity dealing this time with
conformal
Killing vector fields with constant conformal factor. The main example for us will be the vector field
r
∂
r
$r\partial _r$
on the Euclidean space
(
R
d
,
e
)
$(\mathbb {R}^d,\bm{e})$
, where
r
:
=
d
e
(
0
,
.
)
$r := d_{\bm{e}}(0,.)$
.
Proposition 3.1.
Let
h
be a symmetric 2-tensor on an open subset
U
⊂
R
d
$\mathcal {U}\subset \mathbb {R}^d$
containing
S
d
−
1
$\mathbb {S}^{d-1}$
. Then, we have the following identity:
∫
S
d
−
1
E
e
(
1
)
(
h
)
(
r
∂
r
,
∂
r
)
+
d
−
2
2
−
δ
e
h
−
d
tr
e
h
(
∂
r
)
d
v
S
d
−
1
=
0
.
$$\begin{equation} \int _{\mathbb {S}^{d-1}} {\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h)\right)}(r\partial _r,\partial _r)+ \frac{d-2}{2} {\left(-\delta _{\bm{e}}h-d\operatorname{\operatorname{tr}}_{\bm{e}}h\right)}(\partial _r) dv_{\mathbb {S}^{d-1}}=0. \end{equation}$$
(29)
Moreover, assume that we have
R
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{R}}^{(1)}_{\bm{e}}(h)= 0$
and that
h
together with its first two derivatives are bounded on
B
e
(
1
+
ε
)
$B_{\bm{e}}(1+\epsilon )$
. Then we have:
∫
S
d
−
1
E
e
(
1
)
(
h
)
(
r
∂
r
,
∂
r
)
=
0
.
$$\begin{equation} \int _{\mathbb {S}^{d-1}} {\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h)\right)}(r\partial _r,\partial _r)=0. \end{equation}$$
(30)
Remark 3.2.
One recognizes (up to a constant) the integrand of the ADM mass in the term
∫
S
d
−
1
(
−
δ
e
h
−
d
tr
e
h
)
(
∂
r
)
d
v
S
d
−
1
$\int _{\mathbb {S}^{d-1}} (-\delta _{\bm{e}}h-d\operatorname{\operatorname{tr}}_{\bm{e}}h)(\partial _r) dv_{\mathbb {S}^{d-1}}$
. This is not surprising from the proof and can be seen as a first order version of the proof of the equality between the mass and the so-called
Ricci version of the mass
given in [
28
].
Proof.
As in the proof of the first point in Proposition
2.6
, without changing the value of the integral on
S
d
−
1
$\mathbb {S}^{d-1}$
, we replace
h
by another 2-tensor equal to
h
in a neighborhood of
S
d
−
1
$\mathbb {S}^{d-1}$
and vanishing in a neighborhood of the sphere
(
1
−
ε
)
S
d
−
1
⊂
U
$(1-\epsilon )\mathbb {S}^{d-1}\subset \mathcal {U}$
for
ε
>
0
$\epsilon &gt;0$
small enough. We denote Ω the open subset bounded by
S
d
−
1
$\mathbb {S}^{d-1}$
and
(
1
−
ε
)
S
d
−
1
$(1-\epsilon )\mathbb {S}^{d-1}$
.
From the identity (
14
) and Lemma
2.4
, we can use the divergence theorem and the equality
δ
e
∗
(
r
∂
r
)
=
e
$\delta ^*_{\bm{e}}(r\partial _r) = \bm{e}$
to find the identity:
∫
S
d
−
1
E
e
(
1
)
(
h
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
d
−
1
=
∫
Ω
tr
e
E
e
(
1
)
(
h
)
d
v
e
.
$$\begin{equation} \int _{\mathbb {S}^{d-1}} {\left(\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^{d-1}} = \int _\Omega \operatorname{\operatorname{tr}}_{\bm{e}} \operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h) dv_{\bm{e}}.\end{equation}$$
(31)
Now, one recognizes that
tr
e
E
e
(
1
)
(
h
)
=
2
−
d
2
R
e
(
1
)
(
h
)
$\operatorname{\operatorname{tr}}_{\bm{e}} \operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h) = \frac{2-d}{2} \operatorname{\operatorname{R}}^{(1)}_{\bm{e}}(h)$
by definition of the scalar curvature
R
g
=
tr
g
Ric
g
$\operatorname{\operatorname{R}}_g=\operatorname{\operatorname{tr}}_g\operatorname{\operatorname{Ric}}_g$
and since
E
e
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}=0$
. From the first variation of the scalar curvature at a Euclidean metric:
R
e
(
1
)
(
h
)
=
δ
e
δ
e
(
h
)
+
d
tr
e
(
h
)
,
$$\begin{equation*} \operatorname{\operatorname{R}}^{(1)}_{\bm{e}}(h) = \delta _{\bm{e}}{\left(\delta _{\bm{e}}(h) +d\operatorname{\operatorname{tr}}_{\bm{e}}(h)\right)}, \end{equation*}$$
using the divergence theorem, we find the stated formula.
Finally, if
h
is defined on
B
e
(
1
+
ε
)
$B_{\bm{e}}(1+\epsilon )$
for some
ε
>
0
$\epsilon &gt;0$
and satisfies
R
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{R}}_{\bm{e}}^{(1)}(h)=0$
then, by (
31
), one has
∫
S
d
−
1
(
E
e
(
1
)
(
h
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
d
−
1
=
0
$\int _{\mathbb {S}^{d-1}} (\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h))(r\partial _r,\partial _r)dv_{\mathbb {S}^{d-1}}=0$
.
□
$\Box$
One finds an obstruction similar to that of Proposition
2.8
for the second order variation of the metric direction.
Proposition 3.3.
Let
h
be a symmetric 2-tensor on an open subset
U
⊂
R
d
$\mathcal {U}\subset \mathbb {R}^d$
containing
S
d
−
1
$\mathbb {S}^{d-1}$
and
B
e
(1) satisfying
E
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(h) = 0$
. Then, we have the following identity:
∫
S
d
−
1
E
e
(
2
)
(
h
,
h
)
(
r
∂
r
,
∂
r
)
+
2
−
d
2
(
δ
+
d
tr
)
e
(
1
)
(
h
)
(
h
)
−
(
δ
e
h
+
d
tr
e
h
)
∘
h
−
1
2
tr
e
h
e
(
∂
r
)
d
v
S
d
−
1
=
0
,
$$\begin{eqnarray} \int _{\mathbb {S}^{d-1}} {\left(\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}(h,h)\right)}(r\partial _r,\partial _r)&+& \frac{2-d}{2}\left[{\left((\delta +d\operatorname{\operatorname{tr}})^{(1)}_{\bm{e}}(h)\right)}(h)\right.\nonumber\\ &-&\left.(\delta _{\bm{e}}h+d\operatorname{\operatorname{tr}}_{\bm{e}}h)\circ{\left(h-{\left(\frac{1}{2}\operatorname{\operatorname{tr}}_{\bm{e}} h\right)}\bm{e}\right)} \right](\partial _r) dv_{\mathbb {S}^{d-1}}=0, \end{eqnarray}$$
(32)
where
h
−
(
tr
e
h
/
2
)
e
$h-(\operatorname{\operatorname{tr}}_{\bm{e}} h/2)\bm{e}$
is seen as a (1,1) tensor while
h
is considered as a symmetric 2-tensor elsewhere.
The same result is true if
h
is defined on an open subset
U
⊂
R
d
$\mathcal {U}\subset \mathbb {R}^d$
containing
S
d
−
1
$\mathbb {S}^{d-1}$
and
R
d
∖
B
e
(
1
)
$\mathbb {R}^d\backslash B_{\bm{e}}(1)$
and if it additionally satisfies the decay assumption:
r
k
|
∇
e
k
h
|
e
=
O
(
r
−
d
−
2
2
)
$r^k|\nabla ^k_{\bm{e}}h|_{\bm{e}}=\mathcal {O}(r^{-\frac{d-2}{2}})$
for
k
∈
{
0
,
1
,
2
}
$k\in \lbrace 0,1,2\rbrace$
.
Remark 3.4.
For
h
and
k
symmetric 2-tensors, we have
δ
e
(
1
)
(
h
)
(
k
)
(
∂
r
)
=
−
δ
e
(
h
×
k
)
(
∂
r
)
−
1
2
k
(
d
tr
e
h
,
∂
r
)
+
1
2
⟨
k
,
∇
∂
r
h
⟩
e
$$\begin{equation*} {\left[{\left(\delta ^{(1)}_{\bm{e}}(h)\right)}(k)\right]}(\partial _r) = -\delta _{\bm{e}}(h\times k)(\partial _r)-\frac{1}{2}k(d\operatorname{\operatorname{tr}}_{\bm{e}}h,\partial _r)+\frac{1}{2}\langle k, \nabla _{\partial _r}h \rangle _{\bm{e}} \end{equation*}$$
where
h
×
k
$h\times k$
is the 2-tensor obtained from the composition of the endomorphisms associated to h and
k
and
d
tr
e
(
1
)
(
h
)
(
k
)
(
∂
r
)
=
−
d
⟨
h
,
k
⟩
e
(
∂
r
)
,
$$\begin{equation*} {\left[{\left(d\operatorname{\operatorname{tr}}^{(1)}_{\bm{e}}(h)\right)}(k)\right]}(\partial _r) =- d{\left(\langle h,k \rangle _{\bm{e}}\right)}(\partial _r), \end{equation*}$$
see [
17
] for instance. We will try not to use these formulas whenever possible and focus on situations for which this additional boundary term vanishes.
Remark 3.5.
The two situations of Proposition
3.3
model Einstein manifolds or orbifolds at a given point or Einstein metrics asymptotic to a quotient of
R
d
$\mathbb {R}^d$
at infinity. The decay condition on
h
is not strong as any
h
decaying at any rate at infinity and in divergence-free gauge (or Bianchi gauge) which satisfies
E
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}^{(1)}_{\bm{e}}(h)=0$
automatically satisfies
r
k
|
∇
e
k
h
|
e
=
O
(
r
−
d
+
1
)
=
o
(
r
−
d
−
2
2
)
$r^k|\nabla ^k_{\bm{e}}h|_{\bm{e}}= \mathcal {O}(r^{-d+1}) = o(r^{-\frac{d-2}{2}})$
by [
15
].
Proof.
Let us assume that
E
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(h)= 0$
on an open set containing
B
e
(1). Using the formula (
20
) with
T
=
E
e
(
2
)
(
h
,
h
)
$T = \operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,h)$
and
Ω
=
B
e
(
1
)
$\Omega = B_{\bm{e}}(1)$
, we find the equality:
∫
S
d
−
1
E
e
(
2
)
(
h
,
h
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
d
−
1
=
∫
Ω
tr
e
E
e
(
2
)
(
h
,
h
)
d
v
e
$$\begin{equation} \begin{aligned} \int _{\mathbb {S}^{d-1}}& {\left(\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}(h,h)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^{d-1}}= \int _\Omega \operatorname{\operatorname{tr}}_{\bm{e}}\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}(h,h) dv_{\bm{e}}\end{aligned} \end{equation}$$
(33)
where we used
δ
e
∗
(
r
∂
r
)
=
e
$\delta _{\bm{e}}^*(r\partial _r)=\bm{e}$
and the fact that there is only
one
nonvanishing boundary term at
S
d
−
1
$\mathbb {S}^{d-1}$
.
There remains to understand the term
∫
Ω
tr
e
E
e
(
2
)
(
h
,
h
)
d
v
e
$ \int _\Omega \operatorname{\operatorname{tr}}_{\bm{e}}\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}(h,h) dv_{\bm{e}}$
as a boundary term. Since
E
e
(
1
)
(
h
)
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(h)=0$
, then,
tr
e
E
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
2
−
d
2
R
e
(
2
)
(
h
,
h
)
$\operatorname{\operatorname{tr}}_{\bm{e}}\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}(h,h) = \frac{2-d}{2} \operatorname{\operatorname{R}}^{(2)}_{\bm{e}}(h,h)$
where we recall that the formula for
R
(
1
)
$\operatorname{\operatorname{R}}^{(1)}$
is given by
R
g
(
1
)
(
v
)
=
δ
g
(
δ
g
v
+
d
tr
g
v
)
−
⟨
v
,
Ric
(
g
)
⟩
$\operatorname{\operatorname{R}}_g^{(1)}(v) = \delta _g(\delta _gv+d\operatorname{\operatorname{tr}}_g v) -\langle v,\operatorname{\operatorname{Ric}}(g)\rangle$
for a general metric
g
and a deformation
v
. This implies that one generally has:
∫
Ω
R
g
(
1
)
(
v
)
d
v
g
=
−
∫
∂
Ω
δ
g
v
+
d
tr
g
v
(
∂
r
)
d
v
∂
Ω
−
∫
Ω
v
,
Ric
(
g
)
d
v
g
.
$$\begin{equation} \int _{\Omega }\operatorname{\operatorname{R}}_g^{(1)}(v)dv_g = -\int _{\partial \Omega }{\left(\delta _gv+d\operatorname{\operatorname{tr}}_g v\right)}(\partial _r) dv_{\partial \Omega } -\int _\Omega {\left\langle v,\operatorname{\operatorname{Ric}}(g)\right\rangle} dv_g.\end{equation}$$
(34)
By differentiating (
34
) with
Ω
=
B
e
(
1
)
$\Omega =B_{\bm{e}}(1)$
at
g
=
e
$g=\bm{e}$
in the direction
h
and for
v
satisfying
E
e
(
1
)
(
v
)
=
Ric
e
(
1
)
(
v
)
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(v)=\operatorname{\operatorname{Ric}}^{(1)}_{\bm{e}}(v) = 0$
we obtain:
∫
B
e
(
1
)
R
e
(
2
)
(
h
,
v
)
d
v
e
=
−
∫
S
d
−
1
(
δ
+
d
tr
)
e
(
1
)
(
h
)
(
v
)
+
tr
e
h
2
(
δ
e
v
+
d
tr
e
v
)
−
(
δ
e
v
+
d
tr
e
v
)
∘
h
(
∂
r
)
d
v
S
d
−
1
,
$$\begin{eqnarray} &&\int _{B_{\bm{e}}(1)}\operatorname{\operatorname{R}}_{\bm{e}}^{(2)}(h,v)dv_{\bm{e}}\nonumber\\  &&\quad= -\int _{\mathbb {S}^{d-1}}{\left[{\left((\delta +d\operatorname{\operatorname{tr}})^{(1)}_{\bm{e}}(h)\right)}(v) +\frac{\operatorname{\operatorname{tr}}_{\bm{e}}h}{2}(\delta _{\bm{e}}v+d\operatorname{\operatorname{tr}}_{\bm{e}}v) - (\delta _{\bm{e}}v+d\operatorname{\operatorname{tr}}_{\bm{e}}v)\circ h \right]}(\partial _r) dv_{\mathbb {S}^{d-1}},\end{eqnarray}$$
(35)
where the last
h
is seen as a (1,1) tensor. Using (
35
) with
v
=
h
$v=h$
yields the result.
The proof is exactly the same when
Ω
=
R
d
∖
B
e
(
1
)
$\Omega = \mathbb {R}^d\backslash B_{\bm{e}}(1)$
if we assume that
r
k
|
∇
e
k
h
|
e
=
o
(
r
−
d
−
2
2
)
$r^k|\nabla ^k_{\bm{e}}h|_{\bm{e}} = o(r^{-\frac{d-2}{2}})$
for
k
⩽
2
$k\leqslant 2$
as this condition ensures that the boundary terms vanish at infinity. Indeed, the integrand of boundary term is of the form
h
∗
∇
h
=
o
(
r
−
d
+
1
)
$h*\nabla h = o(r^{-d+1})$
for * denoting various contraction of tensors, once compared to the volume of the spheres of radius
r
growing like
O
(
r
d
−
1
)
$\mathcal {O}(r^{d-1})$
, we see that the boundary term vanishes. As previously, one then simply has to deal with the boundary
S
d
−
1
$\mathbb {S}^{d-1}$
, and the proof is the argument is the same as for
B
e
(1).
□
$\Box$
Remark 3.6.
Just as in Proposition
2.6
, the left-hand side of (
32
) has invariance properties on the hypersurface or action by diffeomorphism. The invariance by hypersurface is again a consequence of the divergence theorem, and the invariance by Lie derivative comes from Proposition
2.3
.
Remark 3.7.
The conformal Killing vector field
r
∂
r
$r\partial _r$
is present for any Ricci-flat cone. One can therefore define a similar integral quantity which has to vanish with the exact same proof.
3.2 Deformations with constant scalar curvature
In our situations of interest, as we will see later, we will consider Einstein deformations for which the second variation of the scalar curvature is constant. In this case, the obstruction becomes much simpler as we may drop the additional boundary term.
Proposition 3.8.
Let
h
and
k
be infinitesimal Einstein deformations of
e
on
B
e
(
1
+
ε
)
$B_{\bm{e}}(1+\epsilon )$
or
R
d
∖
B
e
(
1
−
ε
)
$\mathbb {R}^d \backslash B_{\bm{e}}(1-\epsilon )$
satisfying
(1)
δ
e
h
=
δ
e
k
=
0
$\delta _{\bm{e}} h = \delta _{\bm{e}}k =0$
(2)
E
e
(
1
)
(
h
)
+
λ
e
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(h) + \lambda \bm{e} =0$
and
E
e
(
1
)
(
k
)
+
μ
e
=
0
$\operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(k) + \mu \bm{e}=0$
,
(3)
and
R
e
(
2
)
(
h
,
k
)
$\operatorname{\operatorname{R}}_{\bm{e}}^{(2)}(h,k)$
is constant.
Then, we have the obstruction:
∫
S
d
−
1
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
d
−
1
=
0
$$\begin{equation} \int _{\mathbb {S}^{d-1}} {\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(h,k)\right)}(r\partial _r,\partial _r)dv_{\mathbb {S}^{d-1}} = 0\end{equation}$$
(36)
and for any Killing vector field
Y
∫
S
d
−
1
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
(
Y
,
∂
r
)
d
v
S
d
−
1
=
0
$$\begin{equation} \int _{\mathbb {S}^{d-1}} {\left(\mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(2)}(h,k)\right)}(Y,\partial _r)dv_{\mathbb {S}^{d-1}} = 0\end{equation}$$
(37)
where
Ric
˚
$\mathring{\operatorname{\operatorname{Ric}}}$
is the traceless part of the Ricci curvature.
Remark 3.9.
The first assumption is a gauge-fixing condition which we will always be able to assume up to acting by a diffeomorphism. Moreover it will always be satisfied if
h
=
k
$h=k$
is an integrable Einstein deformation which is not Ricci-flat. Indeed, differentiating
E
(
g
t
)
+
λ
(
t
)
g
t
=
0
$\operatorname{\operatorname{E}}(g_t)+\lambda (t)g_t = 0$
starting at
g
0
=
e
$g_0 = \bm{e}$
with
∂
t
|
t
=
0
g
t
=
h
$\partial _{t|t=0} {g_t} = h$
, and
∂
t
2
|
t
=
0
2
g
t
=
h
′
$\partial ^2_{t^2|t=0} {g_t} = h^{\prime }$
twice yields
E
e
(
1
)
(
h
′
)
+
E
e
(
2
)
(
h
,
h
)
+
λ
′
′
(
0
)
e
+
2
λ
′
(
0
)
h
=
0
$$\begin{equation*} \operatorname{\operatorname{E}}_{\bm{e}}^{(1)}(h^{\prime }) + \operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,h) + \lambda ^{\prime \prime }(0)\bm{e} + 2\lambda ^{\prime }(0)h = 0 \end{equation*}$$
where every term but maybe
2
λ
′
(
0
)
h
=
2
λ
h
$2\lambda ^{\prime }(0) h = 2\lambda h$
is divergence-free by Lemma
2.2
.
Remark 3.10.
The second assumption just means that we consider infinitesimal Einstein deformations. We will see how to ensure that the third assumption is satisfied in dimension 4 in the next sections.
Proof.
For this situation, we use Schoen's Pohozaev identity (
21
) applied to the 2-tensor
E
e
(
2
)
(
h
,
k
)
$ \operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k)$
which is divergence-free because
h
and
k
are infinitesimal Einstein deformations, see Lemma
2.2
:
∫
∂
Ω
E
e
(
2
)
(
h
,
k
)
∘
(
r
∂
r
,
n
)
d
v
e
|
∂
Ω
=
−
1
2
d
∫
Ω
L
r
∂
r
tr
e
E
e
(
2
)
(
h
,
k
)
d
v
e
.
$$\begin{equation} \begin{aligned} \int _{\partial \Omega }{\left(\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k)\right)}^\circ (r\partial _r,n) dv_{{\bm{e}}_{|\partial \Omega }} &= -\frac{1}{2d}\int _\Omega \mathcal {L}_{r\partial _r} \operatorname{\operatorname{tr}}_{\bm{e}} {\left(\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k)\right)} dv_{\bm{e}}.\end{aligned}\end{equation}$$
(38)
Let us now express both
(
E
e
(
2
)
(
h
,
k
)
)
∘
$(\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k))^\circ$
and
tr
e
(
E
e
(
2
)
(
h
,
k
)
)
$\operatorname{\operatorname{tr}}_{\bm{e}} (\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k))$
in terms of
Ric
˚
(
2
)
(
h
,
k
)
$\mathring{\operatorname{\operatorname{Ric}}}^{(2)}(h,k)$
and
R
e
(
2
)
(
h
,
k
)
$\operatorname{\operatorname{R}}^{(2)}_{\bm{e}}(h,k)$
. For this, we first note that since
tr
g
E
g
=
2
−
d
2
R
g
$\operatorname{\operatorname{tr}}_g \operatorname{\operatorname{E}}_g = \frac{2-d}{2}\operatorname{\operatorname{R}}_g$
for any
g
, we have:
tr
e
E
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
2
−
d
2
R
e
(
2
)
(
h
,
k
)
−
λ
tr
e
k
−
μ
tr
e
h
,
$$\begin{equation} \operatorname{\operatorname{tr}}_{\bm{e}} {\left(\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k)\right)} = \frac{2-d}{2}\operatorname{\operatorname{R}}^{(2)}_{\bm{e}}(h,k) - \lambda \operatorname{\operatorname{tr}}_{\bm{e}}k - \mu \operatorname{\operatorname{tr}}_{\bm{e}}h, \end{equation}$$
(39)
and then, by (
28
), we find:
E
e
(
2
)
(
h
,
k
)
∘
=
Ric
˚
(
2
)
(
h
,
k
)
−
λ
k
˚
−
μ
h
˚
.
$$\begin{equation} {\left(\operatorname{\operatorname{E}}_{\bm{e}}^{(2)}(h,k)\right)}^\circ = \mathring{\operatorname{\operatorname{Ric}}}^{(2)}(h,k) - \lambda \mathring{k} - \mu \mathring{h}. \end{equation}$$
(40)
Finally, since by assumption
δ
e
h
=
δ
e
k
=
0
$\delta _{\bm{e}}h = \delta _{\bm{e}}k =0$
, we can again use (
21
):
∫
∂
Ω
h
˚
(
r
∂
r
,
n
)
d
v
e
|
∂
Ω
=
−
1
2
d
∫
Ω
L
r
∂
r
(
tr
e
h
)
d
v
e
and
∫
∂
Ω
k
˚
(
r
∂
r
,
n
)
d
v
e
|
∂
Ω
=
−
1
2
d
∫
Ω
L
r
∂
r
(
tr
e
k
)
d
v
e
.
$$\begin{eqnarray}  \int _{\partial \Omega }\mathring{h}(r\partial _r,n) dv_{{\bm{e}}_{|\partial \Omega }}&=& -\frac{1}{2d}\int _\Omega \mathcal {L}_{r\partial _r} (\operatorname{\operatorname{tr}}_{\bm{e}}h) dv_{\bm{e}} \text{ and }\int _{\partial \Omega }\mathring{k}(r\partial _r,n) dv_{{\bm{e}}_{|\partial \Omega }}\nonumber\\ &=& -\frac{1}{2d}\int _\Omega \mathcal {L}_{r\partial _r} (\operatorname{\operatorname{tr}}_{\bm{e}}k) dv_{\bm{e}}.\end{eqnarray}$$
(41)
Putting (
38
), (
39
), (
40
) and (
41
), we find
∫
∂
Ω
Ric
˚
(
2
)
(
h
,
k
)
(
r
∂
r
,
n
)
d
v
e
|
∂
Ω
=
−
2
−
d
4
d
∫
Ω
L
r
∂
r
R
e
(
2
)
(
h
,
k
)
d
v
e
,
$$\begin{equation*} \int _{\partial \Omega }\mathring{\operatorname{\operatorname{Ric}}}^{(2)}(h,k)(r\partial _r,n) dv_{{\bm{e}}_{|\partial \Omega }} = -\frac{2-d}{4d}\int _\Omega \mathcal {L}_{r\partial _r} \left(\operatorname{\operatorname{R}}^{(2)}_{\bm{e}}(h,k)\right) dv_{\bm{e}}, \end{equation*}$$
and since
R
e
(
2
)
(
h
,
k
)
$\operatorname{\operatorname{R}}_{\bm{e}}^{(2)}(h,k)$
is assumed to be constant, we find the stated equality. The easier case of a Killing vector field
Y
is treated similarly.
□
$\Box$
3.3 Einstein metrics closing-up inside a hypersurface
Let us consider a topology
N
=
(
R
4
∕
Γ
)
∖
{
0
}
∪
Σ
$ N = (\mathbb {R}^4\slash \Gamma )\backslash \lbrace 0\rbrace \cup \Sigma$
for Σ a lower dimensional submanifold “closing up”
N
where
{
0
}
$\lbrace 0\rbrace$
should be. This should be the topology of a general Ricci-flat ALE, see [
2
]. We see that
(
R
4
∕
Γ
,
e
)
$(\mathbb {R}^4\slash \Gamma ,\bm{e})$
is isometric to a
degenerate
metric on
N
which we still denote
e
for which
e
|
Σ
=
0
$\bm{e}_{|\Sigma }=0$
(meaning the induced metric on Σ, not the restriction of
e
at Σ), the vector field
r
∂
r
$r\partial _r$
also extends to
N
and vanishes on Σ.
The typical situation is that of a minimal resolution of
C
2
∕
Γ
$\mathbb {C}^2\slash \Gamma$
for
Γ
⊂
S
U
(
2
)
$\Gamma \subset SU(2)$
, for instance:
T
∗
S
2
=
(
R
4
∕
Z
2
)
∖
{
0
}
∪
S
2
$T^*\mathbb {S}^2 =(\mathbb {R}^4\slash \mathbb {Z}_2)\backslash \lbrace 0\rbrace \cup \mathbb {S}^2$
is the topology of the Eguchi-Hanson metric:
eh
:
=
r
4
1
+
r
4
d
r
2
+
r
2
α
1
2
+
1
+
r
4
α
2
2
+
α
3
2
.
$$\begin{equation} \bm{eh}:= \sqrt {\frac{r^4}{1+r^4}}\left(dr^2+r^2\alpha _1^2\right) + \sqrt {1+r^4}\left(\alpha _2^2+\alpha _3^2\right).\end{equation}$$
(42)
with metric
α
2
2
+
α
3
2
$ \alpha _2^2+\alpha _3^2$
on
S
2
$\mathbb {S}^2$
. Let us restrict ourselves to this situation and keep our discussion at a somewhat informal level as the last section of the article will prove these obstructions rigorously. Assume that there exists a smooth curve of Einstein metrics
t
∈
[
0
,
1
]
↦
g
t
$t\in [0,1]\mapsto \bm{g}_t$
on
N
=
T
∗
S
2
$N = T^*\mathbb {S}^2$
with
g
t
nondegenerate for
t
>
0
$t&gt;0$
and with
g
0
=
e
. This implies by [
1
,
8
,
35
] that up to a subsequence, some rescaling of
g
t
converges to the Eguchi-Hanson metric (
42
) where, schematically, one has
in the coordinates
of (
42
):
eh
=
e
+
H
4
+
⋯
$$\begin{equation*} \bm{eh} = \bm{e} + H^4 +\cdots \end{equation*}$$
with
|
H
4
|
e
∼
r
−
4
$|H^4|_{\bm{e}} \sim r^{-4}$
, while another rescaling of
g
t
converges to an Einstein orbifold metric with
E
(
g
o
)
+
λ
g
o
=
0
$\operatorname{\operatorname{E}}(\bm{g}_o)+\lambda \bm{g}_o = 0$
for
λ
∈
R
$\lambda \in \mathbb {R}$
and
g
o
=
e
+
H
2
+
⋯
$$\begin{equation*} \bm{g}_o = \bm{e} +H_2 +\cdots \end{equation*}$$
with
|
H
2
|
e
∼
r
2
$|H_2|_{\bm{e}} \sim r^{2}$
, and with singularity
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
. Up to some gauge conditions, we are therefore in the situation of Theorem
5.6
but we may use the integration by parts of Proposition
3.8
to interpret this as an obstruction to the existence of an Einstein metric “closing-up” inside the hypersurface
S
3
∕
Z
2
$\mathbb {S}^3\slash \mathbb {Z}_2$
.
By [
39
], up to rescaling and reparametrizing the curve
t
↦
g
t
$t\mapsto \bm{g}_t$
in well-chosen coordinates, we have a development
g
t
=
e
+
H
2
+
t
2
H
4
+
t
2
H
2
4
+
⋯
$\bm{g}_t = \bm{e} + H_2 + t^2H^4 + t^2H^4_2+\cdots$
with
H
2
4
=
O
(
r
−
2
)
$H^4_2 = \mathcal {O}(r^{-2})$
with remaining term negligible in a region where
t
≪
r
≪
1
$\sqrt {t}\ll r\ll 1$
, hence in particular for
r
close to
t
1
/
4
$t^{1/4}$
for small
t
. We again consider the integration by parts
∫
{
r
=
t
1
/
4
}
E
(
1
)
H
2
4
+
E
e
(
2
)
H
2
,
H
4
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
t
1
/
4
S
3
∕
Z
2
=
∫
{
r
<
t
1
/
4
}
tr
e
E
(
1
)
H
2
4
+
E
e
(
2
)
H
2
,
H
4
+
λ
H
4
d
v
e
.
$$\begin{align} \int _{\lbrace r=t^{1/4}\rbrace }& {\left(\operatorname{\operatorname{E}}^{(1)}\left(H^4_2\right)+\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}\left(H_2,H^4\right)+\lambda H^4\right)}(r\partial _r,\partial _r) dv_{t^{1/4}\mathbb {S}^3\slash \mathbb {Z}_2}\nonumber \\ &= \int _{\lbrace r&lt;t^{1/4}\rbrace } \operatorname{\operatorname{tr}}_{\bm{e}}{\left(\operatorname{\operatorname{E}}^{(1)}\left(H^4_2\right)+\operatorname{\operatorname{E}}^{(2)}_{\bm{e}}\left(H_2,H^4\right)+\lambda H^4\right)} dv_{\bm{e}}.\end{align}$$
(43)
It was proven in [
39
] that in the coordinates of (
42
), one actually has
H
2
4
=
0
$H^4_2=0$
. This yields:
∫
{
r
=
t
1
/
4
}
Ric
˚
e
(
2
)
H
2
,
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
t
1
/
4
S
3
∕
Z
2