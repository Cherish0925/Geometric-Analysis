---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Integrability of Einstein deformations and desingularizations]

−
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
,
$$\begin{equation*} \partial _{s^{l}{|s= 0}}^{l} {\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}\left(\partial _{s^l{|s= 0}}^lg_{sv}\right)= \partial _{s^{l}{|s= 0}}^{l}\operatorname{\operatorname{E}}(g_{sv}) -\operatorname{\operatorname{E}}_{\bm{g}_b}^{(1)}\left(\partial _{s^l{|s= 0}}^lg_{sv}\right), \end{equation*}$$
we can therefore focus on showing that the integral of
∂
s
l
|
s
=
0
l
E
g
b
(
g
s
v
)
$\partial _{s^{l}{|s= 0}}^{l} \operatorname{\operatorname{E}}_{\bm{g}_b}(g_{sv})$
against
g
b
is equal to a boundary term. Since the
l
−
1
$l-1$
first derivatives vanish, we have:
2
2
−
d
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
E
(
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
d
l
d
s
l
|
s
=
0
∫
Ω
R
(
g
s
v
)
d
v
g
s
v
=
−
d
l
−
1
d
s
l
−
1
|
s
=
0
∫
Ω
E
(
g
s
v
)
,
∂
s
g
s
v
g
s
v
d
v
g
s
v
−
d
l
−
1
d
s
l
−
1
|
s
=
0
∫
∂
Ω
δ
g
s
v
(
∂
s
g
s
v
)
+
d
tr
g
s
v
(
∂
s
g
s
v
)
(
n
∂
Ω
)
d
v
g
s
v
|
∂
Ω
,
$$\begin{eqnarray} \hspace*{-18pt}\frac{2}{2-d}\int _\Omega {\left\langle \bm{g}_b,\partial _{s^{l}{|s= 0}}^{l} \operatorname{\operatorname{E}}(g_{sv}) \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} &=& \frac{d^l}{ds^l}_{|s= 0}\int _\Omega \operatorname{\operatorname{R}}(g_{sv})dv_{g_{sv}}\nonumber\\ &=& -\frac{d^{l-1}}{ds^{l-1}}_{|s= 0}\int _\Omega {\left\langle \operatorname{\operatorname{E}}(g_{sv}),\partial _sg_{sv} \right\rangle} _{g_{sv}} dv_{g_{sv}}\nonumber\\ &&- \frac{d^{l-1}}{ds^{l-1}}_{|s= 0}\int _{\partial \Omega } {\left(\delta _{g_{sv}}(\partial _{s}g_{sv})+d\operatorname{\operatorname{tr}}_{g_{sv}} (\partial _{s}g_{sv})\right)}(n_{\partial \Omega }) dv_{{g_{sv}}_{|\partial _\Omega }},\end{eqnarray}$$
(68)
where the first term vanishes because
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
$\partial ^k_{s^k{|s= 0}}\operatorname{\operatorname{E}}(g_{sv}) = 0$
for all
k
⩽
l
−
1
$k\leqslant l-1$
by the first point. Together with (
67
), this proves the result.
□
$\Box$
The point of Lemma
5.12
is that if the different
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
$\partial ^k_{s^k|s= 0}g_{sv}$
decay faster than
r
−
2
+
ε
$r^{-2+\epsilon }$
at infinity for some small
ε
>
0
$\epsilon &gt;0$
in dimension 4, then, the boundary term
lim
r
→
∞
∫
r
S
3
∕
Γ
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
$$\begin{equation*} \lim _{r\rightarrow \infty }\int _{r\mathbb {S}^3\slash \Gamma }Q^{(l)}\left(\partial _{s{|s= 0}}g_{sv},\ldots,\partial _{s^{l-1}{|s= 0}}^{l-1}g_{sv}\right) \end{equation*}$$
which will appear in the following proof will always vanish.
Proof of Proposition 1.12.
Using the results of Appendix
B.2
(very close to the proof of [
32
]), we know that for any
v
∈
O
(
g
b
)
$v\in \bm{O}(\bm{g}_b)$
small enough, the map
s
∈
(
−
1
,
1
)
↦
g
s
v
$s\in (-1,1)\mapsto g_{sv}$
is real-analytic in the so-called
C
β
2
,
α
(
g
b
)
$ C^{2,\alpha }_{\beta }(\bm{g}_b)$
-topology defined in Appendix
B.1
for
0
<
β
<
2
$0&lt;\beta &lt;2$
close to 2, say
β
=
1.9
$\beta = 1.9$
. We mainly use the following consequence. We have a
C
β
2
,
α
(
g
b
)
$C^{2,\alpha }_{\beta }(\bm{g}_b)$
-converging development
g
s
v
=
g
b
+
s
v
+
∑
k
⩾
2
s
k
w
k
$g_{sv} = \bm{g}_b + sv +\sum _{k\geqslant 2}s^kw_k$
around
s
=
0
$s=0$
where for any
k
, there exists
C
=
C
(
k
)
>
0
$C= C(k)&gt;0$
with for
l
∈
{
0
,
1
,
2
}
$l\in \lbrace 0,1,2\rbrace$
:
r
1.9
+
l
|
∇
g
b
l
w
k
|
g
b
⩽
C
.
$$\begin{equation} r^{1.9+l}|\nabla _{\bm{g}_b}^lw_k|_{\bm{g}_b}\leqslant C.\end{equation}$$
(69)
This induces a
C
β
+
2
α
$ C^\alpha _{\beta +2}$
-converging development (see again Appendix
B
):
Φ
g
b
(
g
s
v
)
=
s
2
Φ
g
b
(
1
)
(
w
2
)
+
Φ
g
b
(
2
)
(
v
,
v
)
∈
O
(
g
b
)
+
s
3
Φ
g
b
(
1
)
(
w
3
)
+
2
Φ
g
b
(
2
)
(
w
2
,
v
)
+
Φ
g
b
(
2
)
(
v
,
v
,
v
)
∈
O
(
g
b
)
+
⋯
∈
O
(
g
b
)
+
s
l
l
!
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
∈
O
(
g
b
)
+
⋯
∈
O
(
g
b
)
$$\begin{eqnarray*} {\Phi}_{{\bm{g}}_{b}}(g_{sv}) &=& s^{2}{\left({\Phi }_{{\bm{g}}_{b}}^{(1)}(w_{2})+{\Phi }_{{\bm{g}}_{b}}^{(2)}(v,v)\right)} \qquad \qquad \qquad \qquad \qquad \in {\bm{O}}({\bm{g}}_{b})\\ && +s^{3}\left({\Phi }_{{\bm{g}}_{b}}^{(1)}(w_3)+{\left(2{\Phi }_{{\bm{g}}_{b}}^{(2)}(w_{2},v)+{\Phi }_{{\bm{g}}_{b}}^{(2)}(v,v,v)\right)} \qquad \in {\bm{O}}({\bm{g}}_{b})\right.\\ && +\cdots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \in {\bm{O}}({\bm{g}}_{b})\\ &&+\frac{s^{l}}{l!}\partial ^{l}_{s^{l}|s=0}{\Phi }_{{\bm{g}}_{b}}(g_{sv})\quad \qquad \qquad \qquad \qquad \qquad \qquad \in {\bm{O}}({\bm{g}}_{b})\\ &&+\cdots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \in {\bm{O}}({\bm{g}}_{b})\\ \end{eqnarray*}$$
Now, by the analysis of the Fredholm properties of
Φ
g
b
${\Phi }_{\bm{g}_b}$
in [
37
], we know that the
Φ
g
b
(
1
)
(
w
l
)
=
1
l
!
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
${\Phi }_{\bm{g}_b}^{(1)}(w_l) = \frac{1}{l!}{\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv})$
are
L
2
(
g
b
)
$L^2(\bm{g}_b)$
-orthogonal to
O
(
g
b
), hence we need to study the
L
2
(
g
b
)
$L^2(\bm{g}_b)$
-projection of
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
$\partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv})-{\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv})$
on
O
(
g
b
).
If
Φ
g
b
(
g
s
v
)
${\Phi }_{\bm{g}_b}(g_{sv})$
is identically vanishing, then we are done. If not, assume that
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
$\partial ^k_{s^k|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) = 0$
for all
k
⩽
l
−
1
$k\leqslant l-1$
, but
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
:
o
v
≠
0
$\partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) =: \bm{o}_v\ne 0$
. We want to show that
o
v
⊥
(
L
X
g
b
)
∘
$\bm{o}_v\perp (\mathcal {L}_X\bm{g}_b)^\circ$
and
o
v
⊥
L
Y
′
g
b
$\bm{o}_v\perp \mathcal {L}_{Y^{\prime }}\bm{g}_b$
for
Y
′
$Y^{\prime }$
harmonic vector field asymptotic to a Killing vector field.
Let us now apply our integration by parts formula (
20
) to the divergence-free 2-tensor
S
(
l
)
(
v
)
:
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
$S^{(l)}(v):=\partial ^l_{s^l|s=0}{\Phi }_{\bm{g}_b}(g_{sv}) - {\Phi }_{\bm{g}_b}^{(1)}(\partial ^l_{s^l|s=0}g_{sv})$
, this gives
0
=
lim
r
→
∞
∫
r
S
3
/
Γ
S
(
l
)
(
v
)
(
X
,
∂
r
)
d
v
r
S
3
/
Γ
=
1
2
∫
N
S
(
l
)
(
v
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
+
∫
N
tr
g
b
S
(
l
)
(
v
)
d
v
g
b
,
$$\begin{align*} 0=&\;\lim _{r\rightarrow \infty }\int _{r\mathbb {S}^3/\Gamma } S^{(l)}(v)(X,\partial _r)dv_{r\mathbb {S}^3/\Gamma }\\ =&\; \frac{1}{2}\int _N {\left\langle S^{(l)}(v),(\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} \\ &+\int _N \operatorname{\operatorname{tr}}_{\bm{g}_b}S^{(l)}(v)dv_{\bm{g}_b}, \end{align*}$$
where the first boundary term vanishes because it is a finite linear combination of terms of the form
E
g
b
(
k
)
(
∂
s
j
1
j
1
g
s
v
,
…
,
∂
s
j
k
j
k
g
s
v
)
$\operatorname{\operatorname{E}}^{(k)}_{\bm{g}_b}(\partial _{s^{j_1}}^{j_1}g_{sv},\ldots,\partial _{s^{j_k}}^{j_k}g_{sv})$
with
k
⩾
2
$k\geqslant 2$
and
j
i
⩾
1
$j_i\geqslant 1$
. Indeed, we know from the results of Section
B.2
in the appendix (or (
69
)) that
∂
s
j
j
g
s
v
∈
C
1.9
2
,
α
$\partial _{s^{j}}^{j}g_{sv}\in C^{2,\alpha }_{1.9}$
for every
j
⩾
1
$j\geqslant 1$
, which implies that for any
a
∈
{
0
,
1
,
2
}
$a\in \lbrace 0,1,2\rbrace$
,
r
a
+
1.9
|
∇
a
∂
s
j
j
g
s
v
|
⩽
C
j
$r^{a+1.9}|\nabla ^a\partial _{s^{j}}^{j}g_{sv}|\leqslant C_j$
for some
C
j
>
0
$C_j&gt;0$
. This gives:
E
g
b
(
k
)
(
∂
s
j
1
j
1
g
s
v
,
…
,
∂
s
j
k
j
k
g
s
v
)
=
O
(
r
−
2
−
k
·
1.9
)
=
o
(
r
−
4
)
$\operatorname{\operatorname{E}}^{(k)}_{\bm{g}_b}(\partial _{s^{j_1}}^{j_1}g_{sv},\ldots,\partial _{s^{j_k}}^{j_k}g_{sv}) = \mathcal {O}(r^{-2-k\cdot 1.9}) = o(r^{-4})$
. Similarly, the last term
∫
N
tr
g
b
S
(
l
)
(
v
)
d
v
g
b
$\int _N \operatorname{\operatorname{tr}}_{\bm{g}_b}S^{(l)}(v)dv_{\bm{g}_b}$
is a boundary term of the same type by Lemma
5.12
and it vanishes for the same reason.
The proof for the different
L
Y
′
g
b
$\mathcal {L}_{Y^{\prime }}\bm{g}_b$
is similar and easier because there is no trace term to deal with.
□
$\Box$
Remark 5.13.
Again, the proof is very close to that of Theorem
3.8
because in volume gauge, one has
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
5.3.2 Obstruction to the desingularization of spherical and hyperbolic orbifolds
Let us now prove our main result. The main new ingredients from [
36
,
37
] are the new more flexible expression of our obstruction in Theorem
5.6
, and more crucially Proposition
1.12
(based on Lemma
5.12
). Indeed, the problem left in [
36
,
37
] was that the Ricci-flat ALE metric
g
b
might not be integrable, and these obstructions to integrability could compensate our obstructions to desingularizations. Proposition
1.12
however tells us that the obstruction to the integrability of the Ricci-flat ALE metric
g
b
is negligible against
(
L
X
g
b
)
$(\mathcal {L}_X\bm{g}_b)$
. The obstruction to integrability consequently cannot compensate the obstruction to desingularization.
Proof of Theorem 1.9.
Let us assume that there exists a sequence of Einstein metrics
(
M
,
g
n
)
n
$(M,\bm{g}_n)_n$
converging to an Einstein orbifold
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
with
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
$\operatorname{\operatorname{E}}(\bm{g}_o)+\lambda \bm{g}_o=0$
. Then, according to [
36
,
37
,
39
], up to taking a subsequence, there exist
(
t
n
)
n
$(t_n)_n$
,
t
n
>
0
$t_n&gt;0$
,
(
v
n
)
n
$(v_n)_n$
,
v
n
∈
O
(
g
b
)
$v_n\in \bm{O}(\bm{g}_b)$
such that
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
is close to
(
N
,
g
b
)
$(N,\bm{g}_b)$
in the following sense: for all
r
≪
t
n
−
1
2
$r\ll t_n^{-\frac{1}{2}}$
, we have for some
0
<
β
<
1
$0&lt;\beta &lt;1$
(
1
+
r
)
k
+
β
∇
g
b
k
g
n
t
n
−
g
v
n
+
t
n
h
2
g
b
=
o
(
t
n
)
$$\begin{equation} (1+r)^{k+\beta }\left|\nabla _{\bm{g}_b}^k{\left(\frac{\bm{g}_n}{t_n} - {\left(g_{v_n} + t_n h_2\right)}\right)}\right |_{\bm{g}_b} = o(t_n)\end{equation}$$
(70)
where
h
2
is a solution to the following equation:
Φ
g
b
(
1
)
(
h
2
)
+
λ
g
b
∈
O
(
g
b
)
.
$$\begin{equation} {\Phi }_{\bm{g}_b}^{(1)}(h_2)+\lambda \bm{g}_b \in \bm{O}(\bm{g}_b). \end{equation}$$
(71)
It was shown in [
37
] that the first obstruction against
(
L
X
g
b
)
∘
$(\mathcal {L}_{X}\bm{g}_b)^\circ$
to the desingularization is:
∫
N
Φ
g
b
(
g
n
/
t
n
)
+
t
n
λ
(
g
n
/
t
n
)
,
χ
t
n
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
0
.
$$\begin{equation} \int _N{\left\langle {\Phi }_{\bm{g}_b}(\bm{g}_n/t_n)+t_n\lambda (\bm{g}_n/t_n) , \chi _{t_n}(\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b}=0.\end{equation}$$
(72)
Or goal is to show that it cannot be satisfied when desingularizing a spherical or hyperbolic orbifold.
Recall from Proposition
1.12
that one has
Φ
(
g
v
n
)
=
o
v
n
+
O
(
∥
v
n
∥
L
2
(
g
b
)
∥
o
v
n
∥
L
2
(
g
b
)
)
∈
O
(
g
b
)
${\Phi }(g_{v_n}) = \bm{o}_{v_n} \,+\, \mathcal {O}(\Vert v_n\Vert _{L^2(\bm{g}_b)}\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)})\in \bm{O}(\bm{g}_b)$
. If
o
v
n
=
0
$ \bm{o}_{v_n} \,=\, 0$
, then we are done by [
38
], so let us now assume that it is not satisfied. The obstruction against the deformation
w
v
n
:
=
o
v
n
∥
o
v
n
∥
L
2
(
g
b
)
$\bm{w}_{v_n}:=\frac{\bm{o}_{v_n}}{\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)}}$
is
∫
N
Φ
g
b
(
g
n
/
t
n
)
+
t
n
λ
(
g
n
/
t
n
)
,
χ
t
n
w
v
n
g
b
d
v
g
b
=
0
.
$$\begin{equation} \int _N{\left\langle {\Phi }_{\bm{g}_b}(\bm{g}_n/t_n)+t_n\lambda (\bm{g}_n/t_n) , \chi _{t_n}\bm{w}_{v_n} \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b}=0.\end{equation}$$
(73)
Let us now estimate (
72
). We use the control (
70
) which tells us that:
Φ
g
b
(
g
n
/
t
n
)
+
t
n
λ
(
g
n
/
t
n
)
=
Φ
g
b
(
g
v
n
)
+
t
n
Φ
g
b
(
1
)
(
h
2
)
+
t
n
λ
g
b
+
o
t
n
(
1
+
r
)
−
2
−
β
.
$$\begin{equation} {\Phi }_{\bm{g}_b}(\bm{g}_n/t_n)+t_n\lambda (\bm{g}_n/t_n) = {\Phi }_{\bm{g}_b}(g_{v_n}) + t_n{\Phi }^{(1)}_{\bm{g}_b}(h_2) + t_n\lambda \bm{g}_b +o\left(t_n (1+r)^{-2-\beta }\right).\end{equation}$$
(74)
We will therefore decompose (
72
) thanks to (
74
) and estimate each part of the integral.
(1)
For the first integral
∫
N
⟨
Φ
(
g
v
n
)
,
χ
t
n
(
L
X
g
b
)
∘
⟩
g
b
d
v
g
b
$\int _N\langle {\Phi }(g_{v_n}) , \chi _{t_n} (\mathcal {L}_{X}\bm{g}_b)^\circ \rangle _{\bm{g}_b}dv_{\bm{g}_b}$
we use the estimate
∫
N
Φ
(
g
v
n
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
O
(
∥
v
n
∥
L
2
∥
o
v
n
∥
L
2
)
$$\begin{equation*} \int _N{\left\langle {\Phi }(g_{v_n}) , (\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b}=\mathcal {O}(\Vert v_n\Vert _{L^2}\Vert \bm{o}_{v_n}\Vert _{L^2}) \end{equation*}$$
together with
Φ
(
g
v
n
)
=
O
(
∥
o
v
n
∥
L
2
r
−
4
)
${\Phi }(g_{v_n}) = \mathcal {O}(\Vert \bm{o}_{v_n}\Vert _{L^2}r^{-4})$
, which gives
∫
N
Φ
(
g
v
n
)
,
(
1
−
χ
t
n
)
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
O
∫
t
n
−
1
4
∞
∥
o
v
n
∥
L
2
r
−
6
r
−
4
r
3
d
r
=
O
(
t
n
∥
o
v
n
∥
L
2
)
.
$$\begin{align*} \int _N{\left\langle {\Phi }(g_{v_n}) , (1-\chi _{t_n}) (\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} &= \mathcal {O}{\left(\int _{t_n^{-\frac{1}{4}}}^\infty \Vert \bm{o}_{v_n}\Vert _{L^2}r^{-6} r^{-4} r^3dr \right)} \\ &= \mathcal {O}(t_n\Vert \bm{o}_{v_n}\Vert _{L^2}). \end{align*}$$
We finally find
∫
N
Φ
(
g
v
n
)
,
χ
t
n
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
O
(
(
∥
v
n
∥
L
2
+
t
n
)
∥
o
v
n
∥
L
2
)
,
$$\begin{equation} \int _N{\left\langle {\Phi }(g_{v_n}) , \chi _{t_n} (\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = \mathcal {O}((\Vert v_n\Vert _{L^2}+t_n)\Vert \bm{o}_{v_n}\Vert _{L^2}), \end{equation}$$
(75)
(2)
let us denote
λ
1
:
=
∫
N
⟨
Φ
g
b
(
1
)
(
h
2
)
+
λ
g
b
,
(
L
X
g
b
)
∘
⟩
g
b
d
v
g
b
$\lambda _1:=\int _N\langle {\Phi }^{(1)}_{\bm{g}_b}(h_2)+ \lambda \bm{g}_b, (\mathcal {L}_{X}\bm{g}_b)^\circ \rangle _{\bm{g}_b}dv_{\bm{g}_b}$
. We find:
t
n
∫
N
Φ
g
b
(
1
)
(
h
2
)
+
λ
g
b
,
χ
t
n
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
t
n
λ
1
+
o
(
t
n
)
,
$$\begin{equation*} t_n\int _N {\left\langle {\Phi }^{(1)}_{\bm{g}_b}(h_2) + \lambda \bm{g}_b, \chi _{t_n}(\mathcal {L}_{X}\bm{g}_b)^\circ \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = t_n\lambda _1 + o(t_n), \end{equation*}$$
(3)
for the error term, we have
o
(
t
n
)
∫
N
⟨
(
1
+
r
)
−
2
−
β
,
χ
t
n
(
L
X
g
b
)
∘
⟩
g
b
d
v
g
b
=
o
(
t
n
)
$o(t_n)\int _N \langle (1+r)^{-2-\beta }, \chi _{t_n}(\mathcal {L}_{X}\bm{g}_b)^\circ \rangle _{\bm{g}_b}dv_{\bm{g}_b} = o(t_n)$
.
From (
72
), we finally find the estimate:
0
=
t
n
λ
1
+
O
(
∥
v
n
∥
L
2
∥
o
v
n
∥
L
2
)
+
o
(
t
n
)
.
$$\begin{equation} 0 = t_n \lambda _1+\mathcal {O}(\Vert v_n\Vert _{L^2}\Vert \bm{o}_{v_n}\Vert _{L^2})+o(t_n).\end{equation}$$
(76)
Similarly, using again (
74
), we then estimate (
73
) in three parts:
(1)
For the first integral
∫
N
⟨
Φ
(
g
v
n
)
,
χ
t
n
w
v
n
⟩
g
b
d
v
g
b
$\int _N\langle {\Phi }(g_{v_n}) , \chi _{t_n}\bm{w}_{v_n} \rangle _{\bm{g}_b}dv_{\bm{g}_b}$
, we use Proposition
1.12
which implies that
∫
N
Φ
(
g
v
n
)
,
w
v
n
g
b
d
v
g
b
=
∥
o
v
n
∥
L
2
(
g
b
)
+
O
(
∥
v
n
∥
L
2
(
g
b
)
∥
o
v
n
∥
L
2
(
g
b
)
)
.
$$\begin{equation*} \int _N{\left\langle {\Phi }(g_{v_n}) , \bm{w}_{v_n} \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = \Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)}+\mathcal {O}(\Vert v_n\Vert _{L^2(\bm{g}_b)}\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)}). \end{equation*}$$
Since
Φ
(
g
v
n
)
=
O
(
∥
o
v
n
∥
L
2
r
−
4
)
${\Phi }(g_{v_n}) = \mathcal {O}(\Vert \bm{o}_{v_n}\Vert _{L^2}r^{-4})$
, we estimate the difference
∫
N
Φ
(
g
v
n
)
,
(
1
−
χ
t
n
)
w
v
n
g
b
d
v
g
b
=
O
∫
t
n
−
1
4
∞
∥
o
v
n
∥
L
2
r
−
6
r
−
4
r
3
d
r
=
O
(
t
n
∥
o
v
n
∥
L
2
)
,
$$\begin{align*} \int _N{\left\langle {\Phi }(g_{v_n}) , (1-\chi _{t_n})\bm{w}_{v_n} \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} &= \mathcal {O}{\left(\int _{t_n^{-\frac{1}{4}}}^\infty \Vert \bm{o}_{v_n}\Vert _{L^2}r^{-6} r^{-4} r^3dr \right)} \\ &= \mathcal {O}(t_n\Vert \bm{o}_{v_n}\Vert _{L^2}), \end{align*}$$
and finally
∫
N
Φ
(
g
v
n
)
,
χ
t
n
w
v
n
g
b
d
v
g
b
=
∥
o
v
n
∥
L
2
+
O
(
(
t
n
+
∥
v
n
∥
L
2
)
∥
o
v
n
∥
L
2
)
,
$$\begin{equation} \int _N{\left\langle {\Phi }(g_{v_n}) , \chi _{t_n}\bm{w}_{v_n} \right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = \Vert \bm{o}_{v_n}\Vert _{L^2} + \mathcal {O}((t_n+\Vert {v_n}\Vert _{L^2})\Vert \bm{o}_{v_n}\Vert _{L^2}), \end{equation}$$
(77)
(2)
let us denote
μ
v
n
:
=
∫
N
⟨
Φ
g
b
(
1
)
(
h
2
)
+
λ
g
b
,
w
v
n
⟩
g
b
d
v
g
b
$\mu _{v_n}:=\int _N\langle {\Phi }^{(1)}_{\bm{g}_b}(h_2)+ \lambda \bm{g}_b,\bm{w}_{v_n} \rangle _{\bm{g}_b}dv_{\bm{g}_b}$
. We find:
t
n
∫
N
Φ
g
b
(
1
)
(
h
2
)
+
λ
g
b
,
χ
t
n
w
v
n
g
b
d
v
g
b
=
t
n
μ
v
n
+
o
(
t
n
)
,
$$\begin{equation*} t_n\int _N{\left\langle {\Phi }^{(1)}_{\bm{g}_b}(h_2) + \lambda \bm{g}_b, \chi _{t_n}\bm{w}_{v_n}\right\rangle} _{\bm{g}_b}dv_{\bm{g}_b} = t_n\mu _{v_n} + o(t_n), \end{equation*}$$
(3)
for the error term, we have
o
(
t
n
)
∫
N
⟨
(
1
+
r
)
−
2
−
β
,
χ
t
n
w
v
n
⟩
g
b
d
v
g
b
=
o
(
t
n
)
$o(t_n)\int _N \langle (1+r)^{-2-\beta }, \chi _{t_n}\bm{w}_{v_n}\rangle _{\bm{g}_b}dv_{\bm{g}_b} = o(t_n)$
.
From (
73
), we finally find the estimate
0
=
∥
o
v
n
∥
L
2
(
g
b
)
+
t
n
μ
v
n
+
o
(
t
n
+
∥
o
v
n
∥
L
2
(
g
b
)
)
.
$$\begin{equation} 0 = \Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)} + t_n \mu _{v_n}+o(t_n+\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)}).\end{equation}$$
(78)
which gives
∥
o
v
n
∥
L
2
(
g
b
)
=
O
(
t
n
)
$\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)} =\mathcal {O}(t_n)$
because
μ
v
n
$\mu _{v_n}$
is bounded since
O
(
g
b
) is finite-dimensional.
Finally by plugging
∥
o
v
n
∥
L
2
(
g
b
)
=
O
(
t
n
)
$\Vert \bm{o}_{v_n}\Vert _{L^2(\bm{g}_b)} =\mathcal {O}(t_n)$
in (
76
), we find
|
λ
1
|
=
O
(
∥
v
n
∥
L
2
)
$ |\lambda _1| =\mathcal {O}(\Vert v_n\Vert _{L^2})$
. Now, since λ
1
is a constant, and since
(
t
n
,
v
n
)
→
0
$(t_n,v_n)\rightarrow 0$
, we obtain
λ
1
=
0
$\lambda _1 = 0$
. It is impossible to satisfy if
H
2
is the quadratic term of the development of a spherical or hyperbolic orbifold by Corollary
5.11
.
□
$\Box$
Remark 5.14.
The above proof applies indifferently to other Einstein orbifolds and to the other deformations
L
Y
′
g
b
$\mathcal {L}_{Y^{\prime }}\bm{g}_b$
. In particular, it shows that the integrability assumption in Theorem
5.6
is superfluous.
We believe that the result should hold for spherical and hyperbolic orbifolds with more general singularities than
R
4
∕
Z
2
$\mathbb {R}^4\slash \mathbb {Z}_2$
, but this requires dealing with trees of singularities. The main difficulty is that it is not known whether the projection on the obstruction is a real-analytic map or not in this degenerate situation.
Conjecture 5.15.
Let
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
be a singular spherical or hyperbolic compact orbifold. Then, it is not limit of smooth Einstein metrics in the Gromov-Hausdorff sense.
5.4 Higher dimensional Einstein orbifolds with isolated singularities
The work of [
36
,
37
] extends almost verbatim to the degeneration of Einstein
d
-manifolds (
d
⩾
5
$d\geqslant 5$
) satisfying the (non natural) assumption that the
L
d
2
$L^{\frac{d}{2}}$
-norm of its curvature is bounded. It shows that, exactly like in dimension 4, the possible Gromov-Hausdorff limits are Einstein orbifolds with isolated singularities and the singularity models are Ricci-flat ALE orbifolds. Indeed the results of [
36
-
38
] only use the fact that the dimension is 4 to obtain a bound on the
L
2
-norm of the Riemannian curvature from the noncollapsedness assumption.
An obstruction to the desingularization under essentially the same assumptions as [
11
] was proven in [
33
] for higher dimensional desingularizations. Namely, one considers the desingularization by the so-called
Calabi metric
denoted
g
c
a
l
$\bm{g}_{cal}$
which is 2-dimensional, Ricci-flat ALE and asymptotic to
R
2
d
∕
Z
d
$\mathbb {R}^{2d}\slash \mathbb {Z}_d$
.
Lemma 5.16.
The kernel
O
(
g
c
a
l
)
$\bm{O}(\bm{g}_{cal})$
is 1-dimensional and spanned by
(
L
X
g
c
a
l
)
∘
$(\mathcal {L}_X\bm{g}_{cal})^\circ$
, where
X
is a harmonic vector field asymptotic to
r
∂
r
$r\partial _r$
.
Proof.
The proof that
O
(
g
c
a
l
)
$\bm{O}(\bm{g}_{cal})$
is 1-dimensional is found in [
33
]. We therefore simply have to prove the existence of
X
and the fact that
(
L
X
g
c
a
l
)
∘
$(\mathcal {L}_X\bm{g}_{cal})^\circ$
is divergence-free.
Like in [
14
,
38
], we consider the unique function
u
=
r
2
+
O
(
r
−
2
d
+
2
)
$u=r^2+\mathcal {O}(r^{-2d+2})$
satisfying
Δ
g
c
a
l
u
=
2
d
$\Delta _{\bm{g}_{cal}} u = 2d$
. One then defines
X
=
1
2
∇
g
c
a
l
u
=
r
∂
r
+
O
(
r
−
2
d
+
1
)
$X = \frac{1}{2}\nabla _{\bm{g}_{cal}} u = r\partial _r+\mathcal {O}(r^{-2d+1})$
which satisfies
δ
g
c
a
l
(
L
X
g
c
a
l
)
∘
=
0
$$\begin{equation*} \delta _{\bm{g}_{cal}}(\mathcal {L}_X\bm{g}_{cal})^\circ = 0 \end{equation*}$$
by construction.
A last step is to ensure that
(
L
X
g
c
a
l
)
∘
≠
0
$(\mathcal {L}_X\bm{g}_{cal})^\circ \ne 0$
following [
14
]. If
(
L
X
g
c
a
l
)
∘
=
0
$(\mathcal {L}_X\bm{g}_{cal})^\circ = 0$
, then since
Δ
g
c
a
l
u
=
2
d
$\Delta _{\bm{g}_{cal}} u = 2d$
,
X
would generate 1-parameter group of homotheties. By considering the maximum of the curvature tensor, this is impossible for the non flat metric
g
c
a
l
$\bm{g}_{cal}$
.
□
$\Box$
This implies that the obstruction found in [
33
] is of the same type.
Corollary 5.17.
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
2
d
∕
Z
d
$\mathbb {R}^{2d}\slash \mathbb {Z}_d$
at
p
o
$p_o$
. The obstruction to the desingularization of
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
at
p
o
$p_o$
by
g
c
a
l
$\bm{g}_{cal}$
found in [
33
], namely
d
·
R
g
o
(
p
o
)
ω
,
ω
+
2
(
d
−
2
)
R
g
o
(
p
o
)
=
0
$$\begin{equation*} d\cdot {\left\langle \bm{R}_{\bm{g}_o}(p_o)\omega ,\omega \right\rangle} + 2(d-2) \operatorname{\operatorname{R}}_{\bm{g}_o}(p_o) = 0 \end{equation*}$$
is equivalent to the obstruction against
(
L
X
g
b
)
∘
$(\mathcal {L}_{X}\bm{g}_b)^\circ$
.
ACKNOWLEDGMENTS
The author would like to thank Olivier Biquard and Hans-Joachim Hein for inspiring discussions and for sharing some of their early results which lead to [
14
].
APPENDIX A: DEVELOPMENT OF EINSTEIN 4-METRICS
Let
(
M
o
,
g
o
)
$(M_o,\bm{g}_o)$
be an Einstein orbifold (smooth or singular) and assume that at a point
p
, it has a development:
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
$\bm{g}_o=\bm{e}+H_2+\mathcal {O}(r^3)$
. We start by showing that up to a
gauge
term, the term
H
2
has an explicit correspondence with the curvature.
A.1 A local gauge for Einstein metrics
Proposition A.1.
Let
H
2
be a quadratic symmetric 2-tensor satisfying
Ric
e
(
1
)
(
H
2
)
=
Λ
e
$\operatorname{\operatorname{Ric}}^{(1)}_{\bm{e}}(H_2) = \Lambda \bm{e}$
, for
Λ
∈
R
$\Lambda \in \mathbb {R}$
and such that:
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
=
Λ
3
∑
i
ω
i
±
⊗
ω
i
±
+
∑
i
j
W
i
j
±
ω
i
±
⊗
ω
j
±
$$\begin{equation*} \bm{R}^{\pm ,(1)}_{\bm{e}}(H_2) = \frac{\Lambda }{3}\sum _{i}\omega _i^\pm \otimes \omega _i^\pm + \sum _{ij}W_{ij}^\pm \omega _i^\pm \otimes \omega _j^\pm \end{equation*}$$
where we identified
Ω
e
+
⊗
Ω
e
+
∼
(
Ω
e
+
)
∗
⊗
Ω
e
+
∼
End
(
Ω
e
+
)
$\Omega ^+_{\bm{e}}\otimes \Omega ^+_{\bm{e}} \sim (\Omega ^+_{\bm{e}})^*\otimes \Omega ^+_{\bm{e}} \sim \operatorname{End}(\Omega ^+_{\bm{e}})$
and where the
W
i
j
±
$W^\pm _{ij}$
are the coefficients of the (anti-)selfdual Weyl curvature.
Then, there exists a cubic vector field
V
3
such that
H
2
=
−
Λ
9
r
4
g
S
3
+
r
2
6
∑
i
j
W
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
W
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
+
L
V
3
e
.
$$\begin{equation} H_2 =-\frac{\Lambda }{9}r^4g_{\mathbb {S}^3} +\frac{r^2}{6}{\left(\sum _{ij}W_{ij}^+\theta _i^{-}\circ \omega _j^+ + \sum _{kl}W_{kl}^-\theta _k^{+}\circ \omega _l^-\right)} + \mathcal {L}_{V_3}\bm{e}. \end{equation}$$
(A.1)
where
g
S
3
$g_{\mathbb {S}^3}$
is the usual round metric on the unit 3-sphere.
Proof.
Let us first show that the infinitesimal curvature induced by
H
∼
2
:
=
−
Λ
9
r
4
g
S
3
+
r
2
6
∑
i
j
W
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
W
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
$$\begin{equation*} \tilde{H}_2:=-\frac{\Lambda }{9}r^4g_{\mathbb {S}^3}+\frac{r^2}{6}{\left(\sum _{ij}W_{ij}^+\theta _i^{-}\circ \omega _j^+ + \sum _{kl}W_{kl}^-\theta _k^{+}\circ \omega _l^-\right)} \end{equation*}$$
is the same as that of
H
2
. For the spherical metric in geodesic coordinates,
g
S
4
$ g_{\mathbb {S}^4}$
with
Λ
=
3
$\Lambda =3$
, one has the development:
g
S
4
=
e
−
1
3
r
4
g
S
3
+
O
(
r
3
)
,
$$\begin{equation} g_{\mathbb {S}^4} = \bm{e} - \frac{1}{3}r^4g_{\mathbb {S}^3} + \mathcal {O}(r^{3}),\end{equation}$$
(A.2)
and therefore, by linearity of
H
2
↦
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
$H_2\mapsto \bm{R}^{\pm ,(1)}_{\bm{e}}(H_2)$
, we just have to deal with Ricci-flat deformations and their Weyl curvature. We rely on the formalism of [
12
] for this computation.
We first note that each term
r
2
θ
i
∓
∘
ω
j
±
$r^2\theta _i^\mp \circ \omega _j^\pm$
is traceless and harmonic, hence is in the kernel of
Ric
˚
e
(
1
)
$\mathring{\operatorname{\operatorname{Ric}}}_{\bm{e}}^{(1)}$
. We have the following formula
d
(
r
2
θ
i
−
)
=
6
r
d
r
∧
θ
i
−
$d(r^2\theta _i^-) = 6r dr\wedge \theta _i^-$
, hence
∗
d
(
r
2
θ
i
−
)
=
−
6
r
2
α
i
+
.
$$\begin{equation} *d(r^2\theta _i^-) = -6r^2\alpha _i^+.\end{equation}$$
(A.3)
From this, we see that the term is in the Bianchi gauge (
46
) since
W
i
j
+
=
W
j
i
+
$W^+_{ij}=W^+_{ji}$
, and
−
r
2
6
∑
i
W
i
i
+
(
−
6
ω
i
+
(
α
i
+
)
)
=
−
r
∑
i
W
i
i
+
d
r
=
0
$ -\frac{r^2}{6}\sum _{i}W^+_{ii}(-6\omega _i^+(\alpha _i^+)) = -r\sum _iW_{ii}^+dr = 0$
because
r
ω
i
+
(
α
i
+
)
=
−
d
r
$r\omega _i^+(\alpha _i^+) = -dr$
and
∑
i
W
i
i
+
=
0
$ \sum _iW_{ii}^+=0$
.
From (
A.3
), we moreover obtain:
−
d
∗
d
(
r
2
θ
i
−
)
=
6
ω
i
+
,
$$\begin{equation} -d*d(r^2\theta _i^-) = 6\omega _i^+,\end{equation}$$
(A.4)
and therefore we have the following curvature induced by
H
2
+
:
=
r
2
6
∑
i
j
W
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
$H_2^+:=\frac{r^2}{6}\sum _{ij}W_{ij}^+\theta _i^{-}\circ \omega _j^+$
:
Ric
˚
e
(
1
)
(
H
2
+
)
=
0
$\mathring{\operatorname{\operatorname{Ric}}}^{(1)}_{\bm{e}}(H_2^+) = 0$
,
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
+
)
=
W
11
+
W
12
+
W
13
+
W
21
+
W
22
+
W
23
+
W
31
+
W
32
+
W
33
+
$\bm{R}^{+,(1)}_{\bm{e}}(H_2^+) = \def\eqcellsep{&}\begin{bmatrix} W^+_{11}&W^+_{12}&W^+_{13}\\  W^+_{21}&W^+_{22}&W^+_{23}\\  W^+_{31}&W^+_{32}&W^+_{33} \end{bmatrix}$
.
Let us now prove that the induced anti-selfdual curvature
R
e
−
,
(
1
)
(
H
2
+
)
$\bm{R}^{-,(1)}_{\bm{e}}(H_2^+)$
vanishes. On the other hand that seeing,
e
as a hyperkähler metric with the opposite orientation, we have the expression
r
2
θ
i
−
=
∑
l
⟨
ω
i
+
(
r
∂
r
)
,
ω
l
−
(
r
∂
r
)
⟩
ω
l
−
$r^2\theta _i^- = \sum _l \langle \omega _i^+(r\partial _r),\omega _l^-(r\partial _r)\rangle \omega _l^-$
, hence
r
2
θ
i
−
∘
ω
j
+
=
∑
l
ω
i
+
(
r
∂
r
)
,
ω
l
−
(
r
∂
r
)
ω
l
−
∘
ω
j
+
,
$$\begin{equation*} r^2\theta _i^-\circ \omega _j^+ = \sum _l {\left\langle \omega _i^+(r\partial _r),\omega _l^-(r\partial _r)\right\rangle} \omega _l^-\circ \omega _j^+, \end{equation*}$$
and we also find
d
∑
l
ω
i
+
(
r
∂
r
)
,
ω
l
−
(
r
∂
r
)
ω
l
−
=
−
∑
l
ω
l
−
∘
ω
i
+
(
r
d
r
)
∧
ω
j
+
.
$$\begin{equation} d{\left(\sum _l {\left\langle \omega _i^+(r\partial _r),\omega _l^-(r\partial _r)\right\rangle} \omega _l^-\right)} = -\sum _l{\left(\omega _l^-\circ \omega _i^+(rd_r)\right)}\wedge \omega _j^+.\end{equation}$$
(A.5)
Now, recall that for any 1-form β,
∗
(
β
∧
ω
j
+
)
=
ω
j
+
(
β
)
$ * (\beta \wedge \omega _j^+) = \omega _j^+(\beta )$
, where we identify
ω
j
+
$\omega _j^+$
and the associated endomorphism by the metric. By (
A.5
), this gives
∗
d
∑
l
ω
i
+
(
r
∂
r
)
,
ω
l
−
(
r
∂
r
)
ω
j
+
=
−
∑
l
ω
j
+
∘
ω
i
+
∘
ω
l
−
(
r
d
r
)
.
$$\begin{equation*} *d{\left(\sum _l {\left\langle \omega _i^+(r\partial _r),\omega _l^-(r\partial _r)\right\rangle} \omega _j^+\right)} = -\sum _l\omega _j^+\circ \omega _i^+\circ \omega _l^-(rd_r). \end{equation*}$$
From the expression of
R
e
−
,
(
1
)
(
H
2
+
)
(
ω
l
−
)
$\bm{R}^{-,(1)}_{\bm{e}}(H_2^+) (\omega _l^-)$
and using that
W
i
j
+
=
W
j
i
+
$W^+_{ij} = W^+_{ji}$
,
ω
j
+
∘
ω
i
+
=
−
ω
i
+
∘
ω
j
+
$\omega _j^+\circ \omega _i^+ =-\omega _i^+\circ \omega _j^+$
as well as
∑
i
W
i
i
+
=
0
$\sum _i W^+_{ii}= 0$
, we find:
R
e
−
,
(
1
)
(
H
2
+
)
=
0
$\bm{R}^{-,(1)}_{\bm{e}}(H_2^+) = 0$
. The proof is exactly the same for the rest of the tensor coming from
W
−
$W^-$
.
Let us now show that a quadratic 2-tensor satisfying
R
e
(
1
)
(
H
2
′
)
=
0
$\bm{R}_{\bm{e}}^{(1)}(H^{\prime }_2)=0$
is necessarily of gauge type, that is:
H
2
′
=
L
V
3
e
$H^{\prime }_2 = \mathcal {L}_{V_3}\bm{e}$
for some cubic vector field
V
3
. According to [
11
, (28)], there exists
V
3
such that
H
2
′
′
:
=
H
2
′
−
L
V
3
e
$H^{\prime \prime }_2:=H^{\prime }_2 - \mathcal {L}_{V_3}\bm{e}$
is
radial
, that is
H
2
′
′
(
∂
r
,
.
)
=
0
$H^{\prime \prime }_2(\partial _r,.)=0$
, and in particular, there exist
H
i
j
$H_{ij}$
with
H
2
′
′
=
r
4
∑
i
j
H
i
j
α
i
+
α
j
+
$$\begin{equation} H^{\prime \prime }_2 = r^4\sum _{ij}H_{ij}\alpha _i^+\alpha _j^+\end{equation}$$
(A.6)
and still
R
e
(
1
)
(
H
2
′
′
)
=
0
$\bm{R}_{\bm{e}}^{(1)}(H^{\prime \prime }_2)=0$
. We now need to prove that
H
2
′
′
=
0
$H^{\prime \prime }_2=0$
.
Now according to [
11
, (38)], from (
A.6
), one has:
0
=
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
′
′
)
=
−
6
∑
i
j
H
i
j
ω
i
+
⊗
ω
j
+
+
(
H
11
+
H
22
+
H
33
)
Id
Ω
e
+
.
$$\begin{equation} 0=\bm{R}_{\bm{e}}^{+,(1)}(H^{\prime \prime }_2)= -6\sum _{ij}H_{ij}\omega _{i}^+\otimes \omega _{j}^++(H_{11}+H_{22}+H_{33}) \mbox{Id}_{\Omega _{\bm{e}}^+}.\end{equation}$$
(A.7)
We therefore directly find
H
i
j
=
0
$H_{ij}=0$
when
i
≠
j
$i\ne j$
, and taking the trace of (
A.7
), we get
0
=
−
6
(
H
11
+
H
22
+
H
33
)
+
3
(
H
11
+
H
22
+
H
33
)
$ 0=-6(H_{11}+H_{22}+H_{33}) + 3(H_{11}+H_{22}+H_{33})$
and consequently
H
11
+
H
22
+
H
33
=
0
$H_{11}+H_{22}+H_{33} = 0$
. Finally, we see that
H
2
′
′
=
0
$ H^{\prime \prime }_2 =0$
and this ends the proof.
□
$\Box$
A.2 Vanishing of the obstructions to Einstein deformations
Proposition A.2.
For any quadratic 2-tensor
H
2
on
(
R
4
,
e
)
$(\mathbb {R}^4,\bm{e})$
with:
Ric
e
(
H
2
)
=
Λ
e
$\operatorname{\operatorname{Ric}}_{\bm{e}}(H_2) = \Lambda \bm{e}$
for
Λ
∈
R
$\Lambda \in \mathbb {R}$
, the obstructions (
26
) and (
32
) vanish.
Remark A.3.
The result is true from Propositions
2.8
and
3.3
and by [
24
]. We however prefer to give another much simpler way to see that it holds.
Sketch of proof.
We only sketch the proof as the result can essentially be found by bilinearity of the obstructions (
32
) and (
27
) and thanks to the curvature of the known examples of Einstein metrics.
Let us use the bilinear nature of our obstructions and decompose any quadratic 2-tensor as in Proposition
A.1
, that is as
H
2
=
H
R
+
H
W
+
+
H
W
−
+
H
0
$H_2 = H_{\operatorname{\operatorname{R}}}+ H_{W_+}+ H_{W_-} + H_{0}$
where
H
R
=
Λ
r
4
9
g
S
3
$ H_{\operatorname{\operatorname{R}}} =\frac{\Lambda r^4}{9}g_{\mathbb {S}^3}$
,
H
W
±
=
r
2
6
∑
W
i
j
±
θ
i
∓
∘
ω
j
±
$H_{W_\pm } = \frac{r^2}{6}\sum W^\pm _{ij}\theta _i^\mp \circ \omega _j^\pm$
and
H
0
=
L
V
e
$H_{0}=\mathcal {L}_V\bm{e}$
for some vector field
V
satisfying
|
V
|
e
∼
r
3
$|V|_{\bm{e}}\sim r^3$
.
Note that any term combined with a gauge term
H
0
will make the obstructions vanish by invariance, see Proposition
2.6
and Remark
3.6
. There remain several situations which can be settled thanks to the known examples of Einstein metrics:
the obstructions for
(
H
R
,
H
R
)
$(H_{\operatorname{\operatorname{R}}},H_{\operatorname{\operatorname{R}}})$
vanish because they do on the sphere,
the obstructions of the form
(
H
R
,
H
W
±
)
$(H_{\operatorname{\operatorname{R}}}, H_{W_\pm })$
vanish by bilinearity and because of the examples of (anti-)selfdual Kähler-Einstein metrics such as the Fubini-Study metric on
C
P
2
$\mathbb {C}P^2$
,
the obstructions of the form
(
H
W
±
,
H
W
±
)
$(H_{W_\pm }, H_{W_\pm })$
vanish by bilinearity and because of the examples of orbifold hyperkähler metrics such as the ones produced in [
39
], where it is clear that the (anti-)selfdual curvature can take arbitrary values,
lastly, the obstructions of the form
(
H
W
±
,
H
W
∓
)
$(H_{W_\pm }, H_{W_\mp })$
vanish by bilinerarity and because of the examples of non selfdual Einstein metrics, like the Euclidean Schwarzschild metric or the product metric
S
2
×
S
2
$\mathbb {S}^2\times \mathbb {S}^2$
.
□
$\Box$
Remark A.4.
One can also use the expression of the quadratic terms of the Ricci curvature directly from (
48
). The computations are not straightforward but the different terms remarkably cancel out as expected.
APPENDIX B: FUNCTION SPACES AND ANALYTICITY ON ALE SPACES
In this appendix, we define function spaces from [
38
] and use it to show the analytic dependence of Einstein modulo obstructions deformations of Ricci-flat ALE metrics needed in the last section of the article. The proofs in the compact situation can be found in [
32
] and [
38
, Chapter 1, Section 3.1].
B.1 Function spaces
For a tensor
s
, a point
x
,
α
>
0
$\alpha &gt;0$
and a Riemannian manifold
(
M
,
g
)
$(M,g)$
. The Hölder seminorm is defined as
[
s
]
C
α
(
g
)
(
x
)
:
=
sup
{
y
∈
T
x
M
,
|
y
|
<
inj
g
(
x
)
}
|
s
(
x
)
−
s
(
exp
x
g
(
y
)
)
|
y
|
α
|
g
.
$$\begin{equation*} [s]_{C^\alpha (g)}(x):= \sup _{\lbrace y\in T_xM,|y|&lt; \mbox{inj}_g(x)\rbrace } \Big | \frac{s(x)-s(\exp ^g_x(y))}{|y|^\alpha } \Big |_g. \end{equation*}$$
For ALE manifolds, we will consider a norm which is bounded for tensors decaying at infinity. Denote
r
a smooth positive function equal to the parameter
d
e
(0, .) in a neighborhood of infinity where
(
N
,
g
b
)
$(N,\bm{g}_b)$
has ALE coordinates.
Definition B.1. (Weighted Hölder norms on an ALE manifold)
Let
β
∈
R
$\beta \in \mathbb {R}$
,
k
∈
N
$k\in \mathbb {N}$
,
0
<
α
<
1
$0&lt;\alpha &lt;1$
and
(
N
,
g
b
)
$(N,g_b)$
be an ALE manifold. Then, for any tensor
s
on
N
, we define
∥
s
∥
C
β
k
,
α
:
=
sup
N
(
1
+
r
)
β
∑
i
=
0
k
(
1
+
r
)
i
|
∇
g
b
i
s
|
g
b
+
(
1
+
r
)
k
+
α
[
∇
g
b
k
s
]
C
α
(
g
b
)
.
$$\begin{align*} \Vert s \Vert _{C^{k,\alpha }_{\beta }}:= \sup _{N}(1+r)^\beta {\left(\sum _{i=0}^k(1+r)^{i}|\nabla _{g_b}^i s|_{g_b} + (1+r)^{k+\alpha }[\nabla _{g_b}^ks]_{C^\alpha ({g_b})}\right)}. \end{align*}$$
Lemma B.2. ([[
11
], Lemma 2.1],[[
38
]])
Let
(
N
,
g
b
)
$(N,\bm{g}_b)$
be an ALE orbifold. Then, for any
β
∈
(
0
,
2
)
∪
(
2
,
4
)
$\beta \in (0,2)\cup (2,4)$
there exists
C
>
0
$C&gt;0$
such that for any
h
∈
C
β
2
,
α
$h\in C^{2,\alpha }_{\beta }$
,
h
⊥
O
(
g
b
)
$h\perp \bm{O}(\bm{g}_b)$
, we have
∥
h
∥
C
β
2
,
α
⩽
C
∥
Φ
g
b
(
1
)
h
∥
C
β
+
2
α
.
$$\begin{equation} \Vert h\Vert _{C^{2,\alpha }_{\beta }}\leqslant C \Vert {\Phi }^{(1)}_{\bm{g}_b}h\Vert _{C^{\alpha }_{\beta +2}}.\end{equation}$$
(B.1)
B.2 Real-analytic dependence of Einstein modulo obstructions metrics
Let us consider
β
∈
(
0
,
2
)
$\beta \in (0,2)$
to ensure that the kernel
and
cokernel of the linearization of
Φ
g
b
${\Phi }_{\bm{g}_b}$
is reduced to
O
(
g
b
). The map
g
∈
C
β
2
,
α
↦
Φ
g
b
(
g
)
∈
C
β
+
2
α
$g\in C^{2,\alpha }_{\beta }\mapsto {\Phi }_{\bm{g}_b}(g) \in C^{\alpha }_{\beta +2}$
is a real-analytic map between Banach spaces because the “weights”
(
1
+
r
)
β
$(1+r)^{\beta }$
or
(
1
+
r
)
2
+
β
$(1+r)^{2+\beta }$
in both the starting and target spaces are larger than 1. This condition on the weight ensures that multilinear operations are continuous in this topology, see the theory of [
40
] for the source of this requirement and [
11
, Proof of Lemma 8.2] for a discussion of the weight larger than 1 in the case of weighted Hölder norms.
We can therefore apply the implicit function theorem to the following analytic map:
Ψ
:
C
β
2
,
α
×
O
(
g
b
)
×
O
(
g
b
)
↦
C
β
+
2
α
×
C
β
2
,
α
$\bm{\Psi }:C^{2,\alpha }_{\beta }\times \bm{O}(\bm{g}_b)\times \bm{O}(\bm{g}_b) \mapsto C^{\alpha }_{\beta +2}\times C^{2,\alpha }_{\beta }$
defined by
Ψ
(
g
,
o
,
v
)
↦
Φ
g
b
(
g
)
+
o
,
π
O
(
g
b
)
(
g
−
g
b
−
v
)
,
$$\begin{equation*} \bm{\Psi }(g,\bm{o},v)\mapsto {\left({\Phi }_{\bm{g}_b}(g)+\bm{o}, \pi _{\bm{O}(\bm{g}_b)}(g-\bm{g}_b-v)\right)}, \end{equation*}$$
where
π
O
(
g
b
)
$\pi _{\bm{O}(\bm{g}_b)}$
is the
L
2
(
g
b
)
$L^2(\bm{g}_b)$
-projection on
O
(
g
b
) which is linear (hence real-analytic).
The map
Ψ
is real-analytic between Banach spaces and it satisfies the assumptions of the implicit function theorem for real-analytic maps between Banach spaces of [
44
] about
g
b
. Namely, it satisfies:
(1)
Ψ
(
g
b
,
0
,
0
)
=
0
$\bm{\Psi }(\bm{g}_b,0,0) =0$
, and
(2)
the linearization
(
g
,
o
)
↦
Ψ
(
g
,
o
,
0
)
$(g,\bm{o})\mapsto \bm{\Psi }(g,\bm{o}, 0)$
is a homeomorphism by construction.
We conclude that for any
v
∈
O
(
g
b
)
$v\in \bm{O}(\bm{g}_b)$
small enough, there exists a unique
(
g
¯
v
,
o
¯
v
)
∈
(
g
b
+
C
β
2
,
α
)
×
O
(
g
b
)
$(\bar{g}_v, \bar{\bm{o}}_v)\in (\bm{g}_b+C^{2,\alpha }_{\beta })\times \bm{O}(\bm{g}_b)$
satisfying:
Ψ
(
g
¯
v
,
o
¯
v
,
v
)
=
0
$$\begin{equation*} \bm{\Psi }(\bar{g}_v, \bar{\bm{o}}_v,v)=0 \end{equation*}$$
and that
v
↦
(
g
¯
v
,
o
¯
v
)
$v\mapsto (\bar{g}_v, \bar{\bm{o}}_v)$
is real-analytic.
REFERENCES
1
M. T. Anderson
,
Ricci curvature bounds and einstein metrics on compact manifolds
,
J. Amer. Math. Soc.
2
(
1989
), no.
3
,
455
–
490
.
10.1090/S0894-0347-1989-0999661-1
Google Scholar
2
M. T. Anderson
,
The
L
2
structure of moduli spaces of Einstein metrics on 4-manifolds
,
Geom. funct. anal.
2
(
1992
),
29
–
89
.
10.1007/BF01895705
Google Scholar
3
M. T. Anderson
,
On boundary value problems for Einstein metrics
,
Geom. Topol.
12
(
2008
), no.
4
,
2009
–
2045
.
10.2140/gt.2008.12.2009
Google Scholar
4
M. T. Anderson
,
A survey of Einstein metrics on 4-manifolds
,
Handbook of geometric analysis
, No. 3, vol.
14
, Adv. Lect. Math. (ALM), Int. Press,
Somerville, MA
,
2010
, pp.
1
–
39
.
Google Scholar
5
J. Arms
,
J. Marsden
, and
V. Moncrief
,
The structure of the space of solutions of Einstein's equations II: several Killing fields and the Einstein-Yang-Mills equations
,
Ann. Physics
144
(
1982
), no.
1
,
81
–
106
.
10.1016/0003-4916(82)90105-1
Web of Science®
Google Scholar
6
M. Artin
,
On the solutions of analytic equations
,
Invent. Math.
5
(
1968
),
277
–
291
.
10.1007/BF01389777
Google Scholar
7
H. Auvray
,
From ALE to ALF gravitational instantons
,
Compos. Math.
154
(
2018
), no.
6
,
1159
–
1221
.
10.1112/S0010437X18007030
Web of Science®
Google Scholar
8
S. Bando
,
A. Kasue
, and
A. Nakajima
,
On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth
,
Invent. Math.
97
(
1989
), no.
2
,
313
–
349
.
10.1007/BF01389045
Web of Science®
Google Scholar
9
A. L. Besse
,
Einstein manifolds
,
Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]
, vol.
10
, Springer-Verlag,
Berlin
,
1987
.
10.1007/978-3-540-74311-8
Google Scholar
10
R. Bielawski
and
L. Foscolo
,
Deformations of hyperkähler cones
,
arXiv preprint, arXiv:2012.14895 [math.DG]
.
Google Scholar
11
O. Biquard
,
Désingularisation de métriques d'Einstein. I
,
Invent. Math.
192
(
2013
), no.
1
,
197
–
252
.
10.1007/s00222-012-0410-7
Google Scholar
12
O. Biquard
,
Désingularisation de métriques d'Einstein. II
,
Invent. Math.
204
(
2016
), no.
2
,
473
–
504
.
10.1007/s00222-015-0619-3
Web of Science®
Google Scholar
13
O. Biquard
,
Métriques hyperkählériennes piées
,
Bull. Soc. Math. France
147
(
2019
),
303
–
340
.
10.24033/bsmf.2783
Google Scholar
14
O. Biquard
and
H. Hein
,
The renormalized volume of a 4-dimensional Ricci-flat ALE space
,
arXiv preprint arXiv:1901.03647 [math.DG]
.
Google Scholar
15
J. Cheeger
and
G. Tian
,
On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay
,
Invent. Math.
118
(
1994
), no.
3
,
493
–
571
.
10.1007/BF01231543
Web of Science®
Google Scholar
16
O. Chodosh
,
M. Eichmair
, and
A. Volkmann
,
Isoperimetric structure of asymptotically conical manifolds
,
J. Differ. Geom.
105
(
2017
),
1
–
19
.
10.4310/jdg/1483655857
Web of Science®
Google Scholar
17
G. Cox
,
Scalar curvature rigidity theorems for the upper hemisphere
, PhD thesis,
Duke University
,
2011
.
Google Scholar
18
A. Deruelle
and
T. Ozuch
,
A Łojasiewicz inequality for ALE metrics
,
arXiv preprint, arXiv:2007.09937 [math.DG]
.
Google Scholar
19
A. Deruelle
and
T. Ozuch
,
Dynamical (in)stability of Ricci-flat ALE metrics along the Ricci flow
,
arXiv preprint, arXiv:2104.10630 [math.DG]
.
Google Scholar
20
T. Eguchi
and
A. Hanson
,
Asymptotically flat selfdual solutions to Euclidean gravity
,
Phys. Lett. B
74
(
1978
),
249
–
251
.
10.1016/0370-2693(78)90566-X
Web of Science®
Google Scholar
21
J. Fine
,
A gauge theoretic approach to the anti-selfdual Einstein equations
,
arXiv preprint arXiv:1111.5005
,
2011
.
Google Scholar
22
J. Fine
,
J. D. Lotay
, and
M. Singer
,
The space of hyperkhler metrics on a 4-manifold with boundary
,
Forum Math. Sigma
5
(
2017
), e6,
50
.
10.1017/fms.2017.3
Web of Science®
Google Scholar
23
A. Fischer
,
J. Marsden
, and
V. Moncrief
,
The structure of the space of solutions of Einstein's equations. I. One Killing field
,
Ann. Inst. Henri Poincaré
33
(
1980
),
147
–
194
.
Google Scholar
24
J. Gasqui
,
Sur la résolubilité locale des équations d'Einstein
,
Compositio Math.
47
(
1982
), no.
1
,
43
–
69
.
Web of Science®
Google Scholar
25
R. Haslhofer
,
A renormalized Perelman-functional and a lower bound for the ADM-mass
,
J. Geom. Phys.
61
(
2011
), no.
11
,
2162
–
2167
.
10.1016/j.geomphys.2011.06.016
Web of Science®
Google Scholar
26
R. Haslhofer
,
Perelman's lambda-functional and the stability of Ricci-flat metrics
,
Calc. Var. PDE
45
(
2012
), no.
3-4
,
481
–
504
.
10.1007/s00526-011-0468-x
Web of Science®
Google Scholar
27
R. Haslhofer
and
R. Müller
,
Dynamical stability and instability of Ricci-flat metrics
,
Math. Ann.
360
(
2014
), no.
1-2
,
547
–
553
.
10.1007/s00208-014-1047-1
Web of Science®
Google Scholar
28
M. Herzlich
,
Computing asymptotic invariants with the Ricci tensor on asymptotically flat and asymptotically hyperbolic manifolds
,
Ann. Henri Poincaré
17
(
2016
), no.
12
,
3605
–
3617
. MR 3568027
10.1007/s00023-016-0494-5
Web of Science®
Google Scholar
29
K. Kroencke
and
O. L. Petersen
,
L
p
$L^{p}$
-stability and positive scalar curvature rigidity of Ricci-flat ALE manifolds
, arXiv preprint,
arXiv:2009.11854
[math.DG].
Google Scholar
30
P. B. Kronheimer
,
The construction of ALE spaces as hyper-Kähler quotients
,
J. Differential Geom.
29
(
1989
), no.
3
,
665
–
683
.
10.4310/jdg/1214443066
Web of Science®
Google Scholar
31
N. Koiso
,
Rigidity and infinitesimal deformability of Einstein metrics
,
Osaka J. Math.
19
(
1982
), no.
3
,
643
–
668
.
Web of Science®
Google Scholar
32
N. Koiso
,
Einstein metrics and complex structures
,
Invent. Math.
73
(
1983
), no.
1
,
71
–
106
.
10.1007/BF01393826
Web of Science®
Google Scholar
33
P. Morteza
and
J. Viaclovsky
,
The Calabi metric and desingularization of Einstein orbifolds
,
J. Eur. Math. Soc.
22
(
2020
),
1201
–
1245
.
10.4171/JEMS/943
Web of Science®
Google Scholar
34
A. Naber
,
Characterizations of bounded ricci curvature on smooth and NonSmooth spaces
,
arXiv preprint, arXiv:1306.6512 [math.DG]
.
Google Scholar
35
H. Nakajima
,
Self-Duality of ALE Ricci-Flat 4-Manifolds and positive mass theorem
, In
Recent topics in differential and analytic geometry
, vol.
18
, Academic Press,
Boston, MA
,
1990
, pp.
385
–
396
.
Google Scholar
36
T. Ozuch
,
Noncollapsed degeneration of Einstein 4-manifolds I
,
Geom. Topol.
26
(
2022
)
1483
–
1528
.
10.2140/gt.2022.26.1483
Google Scholar
37
T. Ozuch
,
Noncollapsed degeneration of Einstein 4-manifolds II
,
Geom. Topol.
26
(
2022
)
1529
–
1634
.
10.2140/gt.2022.26.1529
Google Scholar
38
T. Ozuch
,
Complétion de l'espace de modules des métriques d'Einstein en dimension 4
,
École Normale Supérieure (Paris)
,
2020
. Français.
https://theses.hal.science/tel-03137993
Google Scholar
39
T. Ozuch
,
Higher order obstructions to the desingularization of Einstein metrics
,
arXiv preprint, arXiv:2012.13316 [math.DG]
.
Google Scholar
40
R. Palais
,
Foundations of global non-linear analysis
, W. A. Benjamin, Inc.,
New York-Amsterdam
,
1968
.
Google Scholar
41
R. Schoen
,
The existence of weak solutions with prescribed singular behaviour for a conformally invariant scalar equation
,
Commun. Pure Appl. Math.
41
(
1988
),
317
–
392
.
10.1002/cpa.3160410305
Web of Science®
Google Scholar
42
L. M. Sibner
,
R. J. Sibner
, and
K. Uhlenbeck
,
Solutions to Yang–Mills equations that are not self-dual
,
Proc. Natl. Acad. Sci. USA.
86
(
1989
), no.
22
,
8610
–
8613
.
10.1073/pnas.86.22.8610
CAS
PubMed
Web of Science®
Google Scholar
43
A.H. Taub
,
Variational principles in general relativity
, In:
C. Cattanes
(ed.),
Relativistic Fluid Dynamics. C.I.M.E. Summer Schools
, vol 52.
Springer, Berlin, Heidelberg
,
1970
,
https://doi.org/10.1007/978-3-642-11099-3_3
.
Google Scholar
44
E. F. Whittlesey
,
Analytic functions in banach spaces
,
Proc. Amer. Math. Soc.
16
(
1965
),
1077
–
1083
.
10.1090/S0002-9939-1965-0184092-2
Web of Science®
Google Scholar
Citing Literature
Volume
77
,
Issue
1
January 2024
Pages
177-220
References
Related
Information
Article Metrics
Full text views/downloads:
1596
Total unique accesses to an article’s full text in HTML or PDF/ePDF format.
More metric information
Citations
(CrossRef):
2
When publishers deposit their content metadata to CrossRef, article citations are tracked and linked, allowing you to see how many times each article has been cited.
Altmetrics:
Scite metrics
Scite uses AI to classify citations by whether they support, contradict, or merely mention the referenced claims.
Explore this article's citation statements on
scite.ai
powered by
Share QR Code
Generating QR code
QR code copied to clipboard!
Select Format
PNG
SVG
JPG
PDF
Something went wrong while generating your QR code. Please try again in a moment. If the issue persists, refresh the page or contact support.
copy
download
back
download
retry
Export citation
Unable to load citation data. Please try again in a moment.
RETRY
How to cite
Ozuch, T. (2024), Integrability of Einstein deformations and desingularizations. Comm. Pure Appl. Math., 77: 177-220.
https://doi.org/10.1002/cpa.22129
How to cite text copied to clipboard!
COPY TEXT
Download Citation
If you have the appropriate software installed, you can download article citation data to the citation manager of your choice.
Simply select your manager software from the list below and click on download.
Select format
Plain text
RIS (ProCite, Reference Manager)
EndNote
BibTeX
Medlars
RefWorks
METADATA
EXPAND
Citation metadata copied to clipboard!
COPY TEXT
DOWNLOAD
Submit to RefWorks
Tips on downloading citation
This feature enables you to download the bibliographic information (also called citation data, header data, or metadata) for the articles on our site.
Citation manager file format
Use the dropdown list to choose how to format the bibliographic data you're harvesting. Several citation manager formats are available, including EndNote and BibTex. You can then copy the formatted citation (as displayed) or download it as file, to your device. If the RefWorks format is chosen, the 'Download' button will be replaced with an option to directly export to RefWorks
Close Figure Viewer
Previous Figure
Next Figure
Caption
Download PDF
Log in to Wiley Online Library
Email or Customer ID
Password
Forgot password?
NEW USER
>
INSTITUTIONAL LOGIN
>
Change Password
Old Password
New Password
Too Short
Weak
Medium
Strong
Very Strong
Too Long
Your password must have 10 characters or more:
a lower case character,
an upper case character,
a special character
or a digit
Too Short
Password Changed Successfully
Your password has been changed
Create a new account
Email
Returning user
Forgot your password?
Enter your email address below.
Email
Please check your email for instructions on resetting your password.
                    If you do not receive an email within 10 minutes, your email address may not be registered,
                    and you may need to create a new Wiley Online Library account.
Request Username
Can't sign in? Forgot your username?
Enter your email address below and we will send you your username
Email
Close
If the address matches an existing account you will receive an email with instructions to retrieve your username
The full text of this article hosted at iucr.org is unavailable due to technical difficulties.