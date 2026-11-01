---
retention_scope: session
part: 2
total_parts: 6
---

[Part 2/6 of: EGUCHI-HANSON]

2.5. Recap of blow-up limits of singularities. As mentioned above, every complete Riemannian manifold *(M,g)* of bounded curvature admits a short-time Ricci
flow starting from *g,* however singularities may develop in finite time. Similar to
the study of other nonlinear equations, it is very useful to consider blow-up limits
of singularities. We briefly sketch the idea here: Assume (M,g(t)), t ∈ [0,T<sub>sing</sub>),
is a Ricci flow encountering a curvature singularity as t → T<sub>sing</sub>. Let (p<sub>i</sub>,t<sub>i</sub>) with
p<sub>i</sub> ∈ M and t<sub>i</sub> → T<sub>sing</sub> be a sequence of points in spacetime such that

$$
(M,g)
$$

$$
(M,g(t)),t\in[0,T_{\mathrm{sign}})
$$

$$
t\rightarrow T_{\mathit{sign}}
$$

$$
(p_{i},t_{i})
$$

$$
p_{i}\in M
$$

$$
t_{i}\rightarrow T_{\textit{sign}}
$$

$$
K_{i}:=|R m_{g(t_{i})}|_{g(t_{i})}(p_{i})=\operatorname*{s u p}_{t\leq t_{i}}|R m_{g(t)}|_{g(t)}
$$

and

$$
K_{i}\rightarrow\infty as i\rightarrow\infty.
$$

Take the rescaled metrics

$$
g_{i}(t)=K_{i}g\left(t_{i}+\frac{t}{K_{i}}\right),\quad t\in[-K_{i}t_{i},0].
$$

Then (M<sub>k</sub>,g<sub>i</sub>(t),p<sub>i</sub>) subsequentially converge, in the Cheeger-Gromov sense, to a
pointed ancient Ricci flow solution (*M*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>*),t ∈* (*−∞,0*] (see [ChI, Theorem 6.68] for more details). Note that in general *M*<sub>∞</sub>6= *M.* A Ricci flow is called
ancient if it can be extended to a time interval of the form (*−∞,T), T ∈* R. The
blow-up limit (*M*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>) is called the singularity model and yields important
geometrical information on the shape of the singularity. Hamilton [Ham95] distinguishes between Type I and II singularities, depending on the rate of curvature
blow-up, i.e. for Type I

$$
\left(M_{k},g_{i}(t),p_{i}\right)
$$

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right),t\in\left(-\infty,0\right]
$$

$$
M_{\infty}\neq M.
$$

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right)
$$

$$
(-\infty,T),T\in\mathbb{R}
$$

$$
\sup_{M\times[0,T)}\left(T_{sign}-t\right)|R m_{g(t)}|_{g(t)}<\infty
$$

and for Type II

$$
\sup_{M\times[0,T)}\left(T_{s i n g}-t\right)|R m_{g(t)}|_{g(t)}=\infty.
$$

---

By the work of Naber [N10], and Enders, M¨uller and Topping [EMT11] it is known
that Type I singularities are modeled on shrinking Ricci solitons. One hopes —
although it has not been proven — that all Type II singularities are modeled on
steady solitons, as to date all known examples are.

## 3. The maximum principle

Assume we are given a Ricci flow (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1. We make the
following definition:

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

∞
Definition 3.1. Let CU<sub>(2)</sub>(M<sub>k</sub> ×[0,T]) be the space of smooth U(2)-invariant functions

$$
C_{U(2)}^{\infty}(M_k\times[0,T])
$$

$$
u:M_{k}\times[0,T]\rightarrow\mathbb{R}.
$$

In this section we prove a maximum principle for operators

$$
P:C_{U(2)}^{\infty}(M_{k}\times[0,T])\rightarrow C_{U(2)}^{\infty}(M_{k}\times[0,T])
$$

that in (ξ,t) coordinates and away from the non-principal orbit S<sup>2</sup><sub>o</sub> of M<sub>k</sub> can be
written in the form
()

$$
S_{o}^{2}
$$

$$
M_{k}
$$

(3.1)

$$
P[u]=\partial_{s s}u+\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}\right)u_{s}+c u-\partial_{t}u,\quad m,n\in\mathbb{R},
$$

∞
where c ∈ CU<sub>(2)</sub>(M<sub>k</sub> ×[0,T]). Recall from section 2.4 that we are interpreting the s
derivative as
<u><em>∂</em></u> <u>1</u> <u><em>∂</em></u>

$$
c\in C_{U(2)}^{\infty}(M_k\times[0,T])
$$

$$
\frac{\partial}{\partial s}=\frac{1}{u}\frac{\partial}{\partial\xi}.
$$

It is useful to work in *(s,t)* coordinates, in which case the operator *P* [u] can be
expressed as
()
∣

$$
(s,t)
$$

$$
P[u]
$$

(3.2)

$$
P[u]=\partial_{s s}u+\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}-\frac{\partial s}{\partial t}\right)u_{s}+c u-\partial_{t}\Big|_{s}u,
$$

∂s
where we recall the expression (2.15) for. Note *P* [u] is degenerate at the origin
*∂t*
*s* = 0 as
*a b ∂s m*

$$
\frac{\partial s}{\partial t}
$$

$$
P[u]
$$

$$
s=0
$$

$$
m\frac{a_{s}}{a}+n\frac{b_{s}}{b}-\frac{\partial s}{\partial t}\sim\frac{m}{s}for0<|s|\ll1.
$$

However, in *(s,t)* coordinates the smoothness of *u* and *c* is equivalent to saying that
*u(s,t),c(s,t*) can be extended to smooth even functions around *s* = 0 by defining
u(s,t) = u(−s,t) and v(s,t) = v(−s,t) for s ≤ 0. Hence we see that u<sub>s</sub> = c<sub>s</sub> = 0
at *s* = 0 and via L’Ĥopital’s Rule we obtain the following representation of *P* [u] on
the principal orbit S<sub>0</sub><sup>2</sup>:

$$
u(s,t),c(s,t)
$$

$$
u(s,t)=u(-s,t)
$$

$$
s=0
$$

$$
u_{s}=c_{s}=0
$$

$$
v(s,t)=v(-s,t)
$$

$$
s\leq0
$$

$$
s=0
$$

$$
P[u]
$$

$$
S_{0}^{2}
$$

$$
P[u]=(m+1)\partial_{s s}u+c u-\partial_{t}u.
$$

The maximum principle derived for *P* below depends on the sign of (*m* + 1):

$$
(m+1)
$$

---

Theorem 3.2. Let (M<sub>k</sub>,g(t)), k ∈ N, t ∈ [0,T] be a Ricci flow with bounded
∞
curvature. Let P be an operator of the form (3.1) and u ∈ CU<sub>(2)</sub>(M<sub>k</sub> × [0,T]). If

$$
(M_{k},g(t)),\quad k\in\mathbb{N},\quad t\in[0,T]
$$

$$
u\in C_{U(2)}^{\infty}(M_k\times[0,T])
$$

$$
P[u]\leq0\quad{\it i n}\quad M_{k}\times[0,T]
$$

*and there exist constants M,σ* > 0 *such that the growth conditions*

$$
\sigma>0
$$

$$
u(s,t)\geq-M\exp(-\sigma s^2)
$$

$$
c(s,t)\leq M\left(|s|^2+1\right)
$$

*are satisfied, then the following holds true:*

Case 1: *(1* + *m ≤ 0) If*

$$
(1+m\leq0)If
$$

$$
u(s,0)\geq0\quad\text{for}\quad s\geq0
$$

$$
u(0,t)\geq0\quad\text{for}\quad t\in[0,T]
$$

*then u(s,t*) *≥* 0 *on* [0, *∞*) *×* [*0,T*
(0, *∞*) *×* (0,T] *then u* = 0 *everywhere.*

*]. Furthermore, if u* = 0 *somewhere on*

$$
u(s,t)\geq0
$$

$$
[0,\infty)\times[0,T]
$$

$$
(0,\infty)\times(0,T]
$$

$$
u=0
$$

$$
(1+m>0)If
$$

Case 2: *(1* + *m* > *0) If*

$$
u(s,0)\geq0\quad\text{for}\quad s\geq0
$$

*then u(s,t*) *≥* 0 *on* [0, *∞*) *×* [*0,T]. Furthermore, if u* = 0 *somewhere on*
[0, *∞*) *×* (0,T] *then u* = 0 *everywhere.*

$$
u(s,t)\geq0
$$

$$
[0,\infty)\times[0,T]
$$

$$
[0,\infty)\times(0,T]
$$

a bs 1
Before proving Theorem 3.2 we need to derive some bounds on <sup>s</sup>, and2
a b b
for metrics *g* of bounded curvature. This will allow us to bound the coefficients
appearing in the expression (3.2) of the operator *P* [u].

$$
\frac{a_{s}}{a},\frac{b_{s}}{b}
$$

$$
\frac{1}{b^{2}}
$$

$$
P[u]
$$

Lemma 3.3. Let (M<sub>k</sub>,g), k ∈ N, and K > 0 such that |Rm<sub>g</sub>|<sub>g</sub> ≤ K on M<sub>k</sub>. Then
everywhere on M<sub>k</sub> we have

$$
(M_k,g),k\in\mathbb{N}
$$

$$
K>0
$$

$$
|R m_{g}|_{g}\leq K
$$

$$
M_{k}
$$

$$
M_{k}
$$

*(1) b<sup>2</sup>*
(2)

$$
b^{2}\geq\frac{1}{K}
$$

$$
\left(\frac{b_{s}}{b}\right)^{2}\leq5K
$$

*(3)*

$$
\frac{Q^{2}}{b^{2}}\leq\frac{5}{3}K
$$

*Proof.* From the curvature components derived in subsection 2.3 we see that

(3.3)

$$
b^{2}H_{23}=4-3Q^{2}-b_{s}^{2}
$$

$$
b^{2}H_{12}=Q^{2}-\frac{a_{s}b_{s}}{Q}
$$

(3.4)

$$
b_{s}=0
$$

At a local minimum b<sub>s</sub> = 0 we thus have

$$
b^{2}=\frac{4}{3H_{12}+H_{23}}\geq\frac{1}{K}
$$

Now we argue by contradiction. Assume that there exists a s<sup>∗</sup> > 0 and δ > 0 such
that at s = s<sup>∗</sup> we have b<sup>2</sup> < <sup>1−δ</sup>. From above it follows that b<sub>s</sub> < 0 for s ≥ s<sup>∗</sup> and
*K*

$$
s^{*}>0
$$

$$
\delta>0
$$

$$
s=s^{*}
$$

$$
b^{2}<\frac{1-\delta}{K}
$$

$$
b_{s}<0
$$

$$
s\geq s^{*}
$$ hence, because b > 0 everywhere, lims→∞b<sub>s</sub> = 0. Equation (3.3) then shows that
1 ()

$$
b>0
$$

$$
\lim_{s\to\infty}b_s=0
$$

$$
\begin{aligned}Q^{2}&=\frac{1}{3}\left(4-b^{2}H_{23}-b_{s}^{2}\right)\\&\geq1+\frac{\delta}{3}-\frac{b_{s}^{2}}{3}\\&\geq1+\frac{\delta}{4}\end{aligned}
$$

for *s* sufficiently large. Then (3.4) implies that eventually

$$
a_{s}\frac{b_{s}}{Q}\geq\frac{5}{4}\delta.
$$

bs
Dividing by shows that
*Q*

$$
\frac{b_{s}}{Q}
$$

$$
a_{s}\rightarrow-\infty\quad as\quad s\rightarrow\infty
$$

contradicting *a ≥* 0. This proves the first bound. To prove the second bound note
that
()<sub>2</sub>
*b* 4 *− 3Q<sup>2</sup>* 4

$$
a\geq0
$$

$$
\left(\frac{b_{s}}{b}\right)^{2}=\frac{4-3Q^{2}}{b^{2}}-H_{23}\leq\frac{4}{b^{2}}+K\leq5K,
$$

where the last inequality follows from (1). For the third bound we have
()
()<sub>2</sub>

$$
\frac{Q^{2}}{b^{2}}=\frac{1}{3}\left(\frac{4}{b^{2}}-\left(\frac{b_{s}}{b}\right)^{2}-H_{23}\right)\leq\frac{5}{3}K.
$$

Lemma 3.4. Let (M<sub>k</sub>,g), k ∈ N, and K > 0 such that |Rm<sub>g</sub>|<sub>g</sub> ≤ K on M<sub>k</sub>. Then
everywhere on M<sub>k</sub> we have
*√* a 1 *√*

$$
\left(M_{k},g\right),k\in\mathbb{N}
$$

$$
K>0
$$

$$
|R m_{g}|_{g}\leq K
$$

$$
M_{k}
$$

$$
M_{k}
$$

(3.5)

$$
-2\sqrt{K}<\frac{a_{s}}{a}<\frac{1}{s}+\sqrt{K}
$$

a
Proof. The quantity φ = <sup>s</sup> s satisfies the ODE
*a*

$$
\phi=\frac{a_{s}}{a}s
$$

$$
\frac{d\phi}{ds}=s\frac{a_{ss}}{a}+\frac{\phi(1-\phi)}{s}
$$

and by L’Ĥopital’s rule we have φ(0) = 1. Note that the function *φ* can be extended
to an even function on R. Therefore <sup>dφ</sup><sub>ds</sub> (0) = 0 and there exists a small > 0 such
that
*√*
*φ ≤* 1 + *Ks* for 0 *≤ s ≤ .*

$$
\phi(0)=1
$$

$$
\phi
$$

$$
\begin{array}{l}\frac{d\phi}{d s}(0)=0\end{array}
$$

$$
\epsilon>0
$$

$$
\phi\leq1+\sqrt{K}s\quad for\quad0\leq s\leq\epsilon.
$$

*√*
Actually the inequality holds for all *s ≥* 0, since whenever *φ(s*) = 1 + *Ks* we have
() *√*

$$
s\geq0
$$

$$
\phi(s)=1+\sqrt{K}s
$$

$$
\frac{d\phi}{d s}=s\left(\frac{a_{s s}}{a}-K\right)-\sqrt{K}<0,
$$

since |<sup>a</sup><sup>ss</sup> | = |R<sub>0101</sub>|≤ K. this proves the the upper bound of (3.5).
*a*

$$
\left|\frac{a_{ss}}{a}\right|=\left|R_{0101}\right|\leq K
$$

To prove the lower bound assume that a<sub>s</sub>(s<sub>0</sub>) < 0. For every s<sub>1</sub> > s<sub>0</sub> there exists
a s<sup>∗</sup> ∈ (s<sub>0</sub>,s<sub>1</sub>) such that

$$
a_{s}(s_{0})<0
$$

$$
s_{1}>s_{0}
$$

$$
s^{*}\in\left(s_{0},s_{1}\right)
$$

$$
a_{s}(s_{1})-a_{s}(s_{0})=(s_{1}-s_{0})a_{ss}(s^{*})\leq(s_{1}-s_{0})K|a(s^{*})|
$$ by the mean value theorem. It follows that

$$
a_{s}(s)\leq\frac{1}{2}a_{s}(s_{0})\quad\mathrm{for}\quad s_{0}\leq s\leq s_{0}+\frac{1}{2K}\Big|\frac{a_{s}(s_{0})}{a(s_{0})}\Big|.
$$

Therefore

$$
0\leq a\left(s_{0}+\frac{1}{2K}\Big|\frac{a_{s}(s_{0})}{a(s_{0})}\Big|\right)\leq a(s_{0})+\frac{1}{2K}\Big|\frac{a_{s}(s_{0})}{a(s_{0})}\Big|\frac{a_{s}(s_{0})}{2}
$$

which implies

$$
\frac{a_{s}(s_{0})}{a(s_{0})}\geq-2\sqrt{K}.
$$

This concludes the proof.

Now we may proceed to proving the maximum principle of Theorem 3.2.

*Proof of Case 1 of Theorem 3.2.* Let *K* > 0 such that

$$
K>0
$$

$$
\operatorname*{s u p}_{M_{k}\times[0,T]}|{R m}_{g(t)}|_{g(t)}\leq K.
$$

Introduce the new variable *r* := *r(s,t*) defined by

$$
r:=r(s,t)
$$

$$
r(r+2)=s^{2}
$$

and let

$$
\overline{u}(r,t)=u\left(\sqrt{r(r+2)},t\right).
$$

Note that *2r ∼ s<sup>2</sup>* for *s* 1 and *r ∼ s* for *s* 1. We make this substitution to
remove the apparent singularity at *s* = 0 in the *(s,t)* coordinate representation (3.2)
of the operator *P* [u]. The function *u* is smooth, because *u* is extendable to an even
function around the origin (see [W43]). Rewriting (3.2) in terms of *(r,t)* coordinates
we see that *u* satisfies the inequality
∣
∣

$$
2r\sim s^{2}
$$

$$
s\ll1
$$

$$
r\sim s
$$

$$
s\gg1
$$

$$
P[u]
$$

$$
\partial_{t}\overline{{u}}\big|_{r}\geq A(r)\partial_{r r}\overline{{u}}+B(r,t)\partial_{r}\overline{{u}}+C(r,t)\overline{{u}}
$$

where *A, B* and *C* are smooth functions defined by

$$
A(r)=\frac{r(r+2)}{(r+1)^2}
$$

$$
B(r,t)=\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}-\frac{\partial s}{\partial t}\right)\frac{s}{r+1}+\frac{1}{(r+1)^{3}}
$$

$$
C(r,t)=c(s,t)
$$

Note that above we regard *s* as a function of *r.* Recall that by Lemma 2.2 the
functions *a* and *b* can be extended to an odd and even function, respectively, around
the origin. Therefore the quantity
()

$$
r.
$$

(3.6)

$$
\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}-\frac{\partial s}{\partial t}\right)s,
$$

considered as a function of *s,* can be extended to an even function around the origin
by [W43]. Hence this expression depends smoothly on *r,* showing that *B(r,t*) is

$$
r,
$$

$$
B(r,t)
$$

---

∂s
smooth. Similarly, we see that *C(r,t*) is smooth. From the expression (2.15) for
∂t
and the curvature components listed in subsection 2.3 it follows that
∣ ∣ ∣ ∫ s ∣

$$
C(r,t)
$$

$$
\frac{\partial s}{\partial t}
$$

(3.7)

$$
\Big|\frac{\partial s}{\partial t}\Big|=\Big|\int_{0}^{s}-K_{1}-2K_{2}\mathrm{d}s\Big|\leq3K s.
$$

By Lemma 3.3 and Lemma 3.4 we hence see that

$$
|B(r,t)|\leq M(r+1)
$$

for some some positive constant *M* depending on *K.* Finally, noting that *A(r*) is
bounded and positive for *r* > 0, we can apply [F64, Theorem 9, p.43] to deduce that
the weak maximum principle holds. Note that for any compact U ⊂ M<sub>k</sub> × [0,T]
we may assume that c < 0 on U by performing the transformation u ← ue<sup>−γt</sup>, for
*γ* = *γ(U*) chosen sufficiently large. Therefore the strong maximum principle follows
from a slight adaptation of [F64, Theorem 1, p.34].

$$
A(r)
$$

$$
r>0
$$

$$
U\subset M_{k}\times[0,T]
$$

$$
c<0
$$

$$
\overline{u}\leftarrow\overline{u}e^{-\gamma t}
$$

$$
\gamma=\gamma(U)
$$

*Proof of Case 2 of Theorem 3.2.* We first prove the weak maximum principle. Taking u<sup>′</sup> = ue<sup>−γt</sup> we see that u<sup>′</sup> satisfies
()

$$
u^{\prime}=u e^{-\gamma t}
$$

$$
\partial_{t}u^{\prime}\geq\partial_{s s}u^{\prime}+\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}\right)u_{s}^{\prime}+(c-\gamma)u^{\prime}.
$$

As *c* is a smooth function of (*s,t),* we can choose
neighborhood of *{s* = *0}×* [0,T] we have *c − γ* <
cannot attain a negative minimum on *{s* = *0}×*

*γ* sufficiently large such that in a
0. Since m+ 1 > 0 we see that u<sup>′</sup>
(0,T], as otherwise

$$
\gamma
$$

$$
(s,t)
$$

$$
\left\{s=0\right\}\times\left[0,T\right]
$$

$$
c-\gamma<0
$$

$$
m+1>0
$$

$$
u^{\prime}
$$

$$
\{s=0\}\times(0,T]
$$

$$
0\leq\partial_{t}u^{\prime}=(1+m)u_{s s}^{\prime}+c u^{\prime}>0,
$$

which is a contradiction. The weak maximum principle now follows by the proof of
[F64, Theorem 9, p.43].

In this paper we only apply the strong maximum principle for *m ∈* N and therefore
only prove this case here. For the general case refer to [Fee13, Theorem 5.17]. Given
a Ricci flow (M<sub>k</sub>,g(t)), t ∈ [0,T], define the corresponding family of rotationally
symmetric spaces (R<sup>m+1</sup>,h(t)), t ∈ [0,T], by

$$
m\in\mathbb{N}
$$

$$
(M_{k},g(t)),\;t\in[0,T]
$$

$$
t\in[0,T]
$$

$$
h=d s^{2}+a^{2}(s,t)g_{S^{m}(\frac{1}{k})},
$$

where g<sub>S</sub>m 1 is the round metric on S<sup>m</sup> of sectional curvature k<sup>2</sup>. A sufficient
()
k
condition for *h* to be smooth at *s* = 0 is that *a* is extendable to an odd function
around the origin and
*a* (0) = *k.*

$$
g_{S^m(\frac{1}{k})}
$$

$$
S^{m}
$$

$$
k^{2}
$$

$$
s=0
$$

$$
h
$$

$$
a_{s}(0)=k.
$$

Both these conditions are satisfied and we conclude that
Laplacian of a rotationally symmetric function

*h* is a smooth metric. The
f on (R<sup>m+1</sup>,h) is given by
<u><em>a</em></u>

$$
h
$$

$$
\left(\mathbb{R}^{m+1},h\right)
$$

$$
\Delta_{h}f=f_{ss}+m\frac{a_{s}}{a}f_{s}
$$

and thus the condition *P* [u] *≤* 0 may be written as

$$
P[u]\leq0
$$

$$
\partial_{t}u\geq\Delta_{h(t)}u+n\frac{b_{s}}{b}u_{s}+c u
$$

---

$$
U\subset M_{k}\times[0,T]
$$

Note that for any bounded U⊂M<sub>k</sub> × [0,T] we may assume that c < 0 on U by
performing the transformation u ← ue<sup>−γt</sup>, for γ = γ(U) chosen sufficiently large.
Hence the desired result follows from [ChII, Theorem 12.40].

$$
c<0
$$

$$
u\leftarrow u e^{-\gamma t}
$$

$$
\gamma=\gamma(U)
$$

*Remark* 3.5. It was crucial in our analysis that *u* is extendable to an even function
around the origin, as the following example demonstrates:

Consider the degenerate parabolic equation
u

(3.8)

$$
u_{t}=u_{xx}-2\frac{u_{x}}{x}+2\frac{u}{x^{2}}
$$

on *x,t ≥* 0 with initial data satisfying *u(x,0*) *≤* 0. If we take

$$
x,t\geq0
$$

$$
u(x,0)\leq0
$$

$$
u=xv
$$

a computation shows that the above PDE corresponds to

(3.9)

$$
v_{t}=v_{xx}
$$

Now considering (3.9) as the heat equation on all of R we can set up initial data
*v(x,0*) such that
v(x,0) ≤ 0 for x ≥ 0,

$$
\mathbb{R}
$$

$$
v(x,0)
$$

$$
v(x,0)\leq0\quad\mathrm{for}\quad x\geq0,
$$

however the solution *v* to the heat equation becomes positive at some later time
*t* > 0 and *x* > 0. This shows that *u ≤* 0 is not necessarily preserved by (3.8).

$$
t>0
$$

$$
x>0
$$

$$
u\leq0
$$

In this paper we also rely on a maximum principle for a system of parabolic
∞
inequalities on u<sub>1</sub>,u<sub>2</sub> ∈ CU<sub>(2)</sub>(M<sub>k</sub> × [0,T]) of the form
()

$$
u_{1},u_{2}\in C_{U(2)}^{\infty}(M_{k}\times[0,T])
$$

(3.10)

$$
\partial_{t}u_{1}\geq(u_{1})_{s s}+\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}\right)(u_{1})_{s}+h_{11}u_{1}+h_{12}u_{2}
$$

(3.11)

$$
\partial_{t}u_{2}\geq(u_{2})_{s s}+\left(m\frac{a_{s}}{a}+n\frac{b_{s}}{b}\right)(u_{2})_{s}+h_{21}u_{1}+h_{22}u_{2},
$$

∞
where h<sub>ij</sub> ∈ CU<sub>(2)</sub>(M<sub>k</sub> × [0,T]), i,j = 1,2, are bounded and satisfy

$$
h_{i j}\in C_{U(2)}^{\infty}\left(M_{k}\times[0,T]\right),i,j=1,2,
$$

$$
h_{12},h_{21}\geq0on M_k\times[0,T].
$$

We prove the following Lemma:

Lemma 3.6. *Let* (*M*
∞
Assume u<sub>1</sub>,u<sub>2</sub> ∈ CU<sub>(2)</sub>
*inequalities and for some constants M,σ* >

<sub>k</sub>,g(t)), t ∈ [0,T], be a Ricci flow with bounded curvature.
(M<sub>k</sub>×[0,T]) satisfy the above system (3.10)-(3.11) of parabolic
0

$$
(M_{k},g(t)),t\in[0,T]
$$

$$
u_{1},u_{2}\in C_{U(2)}^{\infty}(M_{k}\times[0,T])
$$

$$
M,\sigma>0
$$

$$
u_{1}(s,t),u_{2}(s,t)\geq-M\exp(\sigma s^{2})\quad\mathrm{~\it~f o r~}t\in[0,T].
$$

*If*

$$
u_{1}(s,0),u_{2}(s,0)\geq0\;{~\mathit{f o r\;}}s\geq0
$$

$$
u_{1}(0,t),u_{2}(0,t)\geq0\quad\text{for}t\in[0,T]
$$

then u<sub>1</sub>,u<sub>2</sub> ≥ 0 on M<sub>k</sub> × [0,T].

$$
u_{1},u_{2}\geq0
$$

$$
M_{\underline{{k}}}\times[0,T].
$$

---

*Proof.* Writing the equation in terms of *(r,t)* as in the proof of Theorem 3.2 we
obtain
∣
∣

$$
(r,t)
$$

$$
\partial_{t}u_{1}\Big|_{r}\geq A(r)(u_{1})_{r r}+B(r,t)(u_{1})_{r}+H_{11}u_{1}+H_{12}u_{2}
$$

$$
\partial_{t}u_{2}\Big|_{r}\geq A(r)(u_{2})_{r r}+B(r,t)(u_{2})_{r}+H_{21}u_{1}+H_{22}u_{2},
$$

where A(r), *B(r,t*) are as in the proof of Theorem 3.2 and

$$
A(r),B(r,t)
$$

$$
H_{i j}(r,t)=h_{i j}(s(r),t),\quad i,j=1,2.
$$

After constructing a barrier function of the form
[]

$$
H(s,t)=\exp\left[\frac{k|s|^{2}}{1-\mu t}+\nu t\right],\quad0\leq t\leq\frac{1}{2\mu},
$$

the result follows combining the arguments of [F64, Theorem 1, p.34] and [PW84,
Theorem 13, p. 190].

## 4. Kähler quantities and the Eguchi-Hanson space

Recall that a complex structure *J* on a Riemannian manifold *(M,g)* satisfying

$$
(M,g)
$$

(1) *g(V<sub>1</sub>,V<sub>2</sub>*) = *g(JV<sub>1</sub>,JV<sub>2</sub>*) for all *V<sub>1</sub>,V<sub>2</sub> ∈ TM*

$$
g(V_{1},V_{2})=g(JV_{1},JV_{2})
$$

$$
V_{1},V_{2}\in TM
$$

(2) *∇J* = 0

$$
\nabla J=0
$$

defines a K¨ahler structure. On the manifolds M<sub>k</sub>, k ≥ 1, we define two complex
structures *J<sub>1</sub>* and *J<sub>2</sub>* by
*J<sub>1</sub>e<sub>1</sub>* = *e<sub>0</sub> J<sub>1</sub>e<sub>2</sub>* = *e<sub>3</sub>*

$$
M_{k},\;k\geq1
$$

$$
J_{1}
$$

$$
J_{2}
$$

$$
J_{1}e_{1}=e_{0}\qquad J_{1}e_{2}=e_{3}
$$

and

$$
J_{2}e_{0}=e_{2}\qquad J_{2}e_{1}=e_{3}.
$$

A computation shows that (M<sub>k</sub>,g,J<sub>1</sub>) is K¨ahler if and only if

$$
\left(M_{k},g,J_{1}\right)
$$

$$
b_{s}-Q=0.
$$

Similarly, (M<sub>k</sub>,g,J<sub>2</sub>) is K¨ahler if and only if

$$
\left(M_{k},g,J_{2}\right)
$$

$$
a_{s}+Q^{2}-2=0\quad and\quad b_{s}-Q=0.
$$

Note that being K¨ahler with respect to *J<sub>2</sub>* automatically implies K¨ahlerity with respect to *J<sub>1</sub>.* This motivates the definition of the following *scale-invariant* quantities

$$
J_{2}
$$

$$
J_{1}
$$

$$
\begin{aligned}&x:=a_{s}+Q^{2}-2\\&y:=b_{s}-Q\\ \end{aligned}
$$

to measure the deviation of a metric from being K¨ahler with respect to the complex
structures *J<sub>1</sub>* and *J<sub>2</sub>.* For example, the FIK shrinker [FIK03] is K¨ahler with respect
to the complex structure *J<sub>1</sub>* and in our notation satisfies *y* = 0. The Eguchi-Hanson
space is the unique K¨ahler manifold with respect to *J<sub>2</sub>* as the following lemma shows.

$$
J_{1}
$$

$$
J_{2}
$$

$$
J_{1}
$$

$$
y=0
$$

$$
J_{2}
$$

---

Lemma 4.1. Amongst all Riemannian manifolds (M<sub>k</sub>,g),k ≥ 1, equipped with U(2)-
*invariant metric g of the form (2.3), up to scaling the Eguchi-Hanson space is the*
*unique K¨ahler manifold with respect to the complex structure J<sub>2</sub>. Furthermore being*
*K¨ahler with respect to J<sub>2</sub> is equivalent to x* = *y* = *0.*

$$
(M_{k},g),k\geq1
$$

$$
U(2)
$$

$$
J_{2}
$$

$$
x=y=0
$$

$$
J_{2}
$$

*Proof.* By the above discussion being K¨ahler with respect to *J<sub>2</sub>* is equivalent to

$$
J_{2}
$$

(4.1)

$$
x=y=0.
$$

Notice at *s* = 0 we have

$$
s=0
$$

$$
x=a_{s}-2=0
$$

forcing the underlying manifold to be diffeomorphic to *M<sub>2</sub>* by the boundary conditions (1.3). Then in terms of *a* and *b* the condition *x* = *y* = 0 is equivalent to the
first order system of equations

$$
M_{2}
$$

$$
x=y=0
$$

(4.2)

(4.3)

$$
\begin{aligned}a_{s}&=2-Q^{2}\\b_{s}&=Q\end{aligned}
$$

Let a<sup>E</sup> and b
tions

<sup>E</sup> be a solution to this system of equations satisfying the initial condi-

$$
a^{E}
$$

$$
b^{E}
$$

$$
\begin{aligned}a^{E}&=0,\\b^{E}&=1\end{aligned}
$$

at *s* = 0. Then by the scale-invariance of condition (4.1), for every *λ* > 0 the metric
given by the warping functions λa<sup>E</sup>(λs) and λb<sup>E</sup>(λs) also satisfies (4.1). Hence up
to rescaling there is a unique K¨ahler manifold with respect to the complex structure
J<sub>2</sub>. From [EH79] or [Cal79] we see that the metric given by a<sup>E</sup> and b<sup>E</sup> is homothetic
to the Eguchi-Hanson metric.

$$
s=0
$$

$$
\lambda>0
$$

$$
\lambda a^{E}(\lambda s)
$$

$$
\lambda b^{E}\big(\lambda\dot{s}\big)
$$

$$
J_{2}
$$

$$
a^{E}
$$

$$
b^{E}
$$

In the rest of the paper we denote by g<sub>E</sub> the Eguchi-Hanson metric with warping
functions a<sup>E</sup> and b<sup>E</sup> normalized such that b<sup>E</sup> = 1 on S<sub>o</sub><sup>2</sup>. Note that the normalization
condition is equivalent to saying that the area of the exceptional divisor S<sup>2</sup><sub>o</sub> is equal
to 2π.

$$
g_{E}
$$

$$
a^{E}
$$

$$
b^{E}
$$

$$
b^{E}=1
$$

$$
S_{o}^{2}
$$

$$
S_{o}^{2}
$$

$$
2\pi
$$

$$
a^{E}
$$

$$
b^{E}
$$

Lemma 4.2. The warping functions a<sup>E</sup> and b
*the following properties*

<sup>E</sup> of the Eguchi-Hanson metric satisfy

$$
\begin{aligned}a^{E},b^{E}&\sim s\quad\mathit{as}\quad s\rightarrow\infty\\a_{ss}^{E}&<0\quad\mathit{for}\quad s\geq0\\b_{ss}^{E}&>0\quad\mathit{for}\quad s\geq0\\\frac{a^{E}}{b^{E}}&<1\quad\mathit{for}\quad s\geq0\end{aligned}
$$

---

$$
a^{E}
$$

Proof. For brevity write a and b for a<sup>E</sup> and
Eguchi-Hanson background we have
1

b<sup>E</sup>, respectively. Note that on the
2 ()

$$
b^{E}
$$

$$
Q_{s}=\frac{1}{b}\left(a_{s}-Q b_{s}\right)=\frac{2}{b}\left(1-Q^{2}\right),
$$

where the last equality follows from (4.2) and (4.3).
that
*Q* < 1 for

As *Q* = 0 at *s* = 0 it follows
*≥* 0

$$
s=0
$$

$$
Q=0
$$

$$
Q<1\quad for\quad\geq0
$$

and hence

$$
Q_{s}>0for s\geq0.
$$

As

$$
a_{s}=Q_{s}b+Qb_{s}=2-Q^{2}
$$

$$
a_{ss}=-2QQ_{s}<0.
$$

it follows that

$$
b_{ss}=Q_{s}>0.
$$

Similarly

Therefore the limits

$$
a_{\infty}:=\lim_{s\to\infty}a_{s}
$$

and

$$
b_{\infty}:=\lim_{s\to\infty}b_{s}
$$

both exist. From the system of differential equations (4.2) and (4.3) we then see
that
*a* = *b* = *1.*

$$
a_{\infty}=b_{\infty}=1.
$$

This concludes the proof.

## 5. Some preserved conditions

In this section we derive various *scale-invariant* inequalities that are preserved
by a Ricci flow (M<sub>k</sub>,g(t)), t ∈ [0,T], k ∈ N. The scale-invariance is crucial, as it
ensures that the inequalities pass to blow-up limits and therefore also constrain their
geometry. The preserved inequalities we list in this section will play an important
role in all subsequent sections.

$$
\left(M_{k},g(t)\right),t\in[0,T],k\in\mathbb{N}
$$

Section Outline. A central quantity in our analysis is
<u><em>a</em></u>

$$
Q=\frac{a}{b}.
$$

In geometric terms, Q measures the deviation of the cross-sectional S<sup>3</sup>/Z<sub>k</sub> in M<sub>k</sub>
from being round. That is, when *Q* = 1 the cross-section is round and as *Q →* 0
the cross-sectional S<sup>3</sup>/Z<sub>k</sub> collapses along the S<sup>1</sup> Hopf fibres to a two-sphere. A
computation shows that the evolution equation of *Q* is
b 4

$$
Q
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
M_{k}
$$

$$
Q=1
$$

$$
Q\to0
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
S^{1}
$$

$$
Q
$$

(5.1)

$$
\partial_{t}Q=Q_{s s}+3\frac{b_{s}}{b}Q_{s}+\frac{4}{b^{2}}Q(1-Q^{2}).
$$

---

Therefore one expects that the inequality *Q ≤* 1 is preserved by Ricci flow, which
in Lemma 5.2 we prove to be the case.

$$
Q\leq1
$$

Apart from *Q,* the K¨ahler quantities *x* and *y* introduced in section 4 are used
throughout this paper and are one of the key ingredients in showing that certain
Ricci flows on *M<sub>2</sub>* develop singularities modeled on the Eguchi-Hanson space. We
show in Lemma 5.3 and Lemma 5.5 that the inequalities

$$
Q,
$$

$$
M_{2}
$$

$$
x\leq0
$$

and

$$
y\leq0
$$

are both preserved. Furthermore, using the maximum principle for systems of weakly
coupled parabolic equations of Lemma 3.6, we show in Lemma 5.6 that

$$
a_{s},b_{s}\geq0
$$

is preserved. In Lemma 5.7 we show that on a Ricci flow background satisfying
Q ≤ 1 and y ≤ 0, for any C > 2 the inequality a<sub>s</sub> ≤ C is preserved. In the following
sections we will mainly consider Ricci flows satisfying a<sub>s</sub>,b<sub>s</sub> ≥ 0, y ≤ 0, Q ≤ 1 and
a<sub>s</sub> ≤ C. This gives us enough control on a and b to prove many interesting results.

$$
Q\leq1
$$

$$
y\leq0
$$

$$
C>2
$$

$$
a_{s}\leq C
$$

$$
a_{s},b_{s}\geq0,y\leq0,Q\leq1
$$

$$
a_{s}\leq C
$$

Finally, we show that whenever a subset of the inequalities *Q ≤* 1, *y ≤* 0 and
a<sub>s</sub>,b<sub>s</sub> ≥ 0 hold, the details of which are discussed below, the following inequalities

$$
Q\leq1,\;y\leq0
$$

$$
a_{s},b_{s}\geq0
$$

$$
T_{1}=a_{s}+2Q^{2}-2\geq0
$$

$$
T_{2}=Qy-x=-a_{s}+Qb_{s}+2\left(1-Q^{2}\right)\geq0
$$

$$
T_{3}=a_{s}-Qb_{s}-Q^{2}+1\geq0
$$

$$
\min(T_{1},T_{4})\geq0
$$

where

$$
T_{4}=a_{s}-\frac{1}{2}Qb_{s}-\left(1-Q^{2}\right)
$$

are preserved by the Ricci flow. The precise statements and proofs of these preserved
inequalities can be found in Lemmas 5.8, 5.9, 5.10 and 5.11 below.

The main idea in constructing the above inequalities is to study the evolution
equation of the scale-invariant quantities

(5.2)

$$
T_{(\alpha,\beta,\gamma)}=\alpha a_{s}+\beta Q b_{s}+\gamma Q^{2},\quad\alpha,\beta,\gamma\in\mathbb{R}.
$$

For this we need to compute the evolution equations of a<sub>s</sub>, Qb<sub>s</sub> and Q<sup>2</sup>. Recall
∞
Definition 3.1 of CU<sub>(2)</sub>(M<sub>k</sub> × [0,T]). To simplify the formulae slightly, define the
linear operator
*∞ ∞*
L : CU (M × [0,T]) → CU (M × [0,T])

$$
a_{s},\;Qb_{s}
$$

$$
C_{U(2)}^{\infty}(M_k\times[0,T])
$$

$$
Q^{2}
$$

$$
L:C_{U(2)}^{\infty}(M_{k}\times[0,T])\rightarrow C_{U(2)}^{\infty}(M_{k}\times[0,T])
$$

by

$$
L[u]=u_{s s}+\left(2\frac{b_{s}}{b}-\frac{a_{s}}{a}\right)u_{s}
$$ away from the non-principal orbit S<sub>o</sub><sup>2</sup>. As in section 3 we may use L’Ĥoptital’s rule
to find a representation of L on the non-principal orbit S<sub>o</sub><sup>2</sup>. Then, as we show in the
Appendix A, the evolution equations of a<sub>s</sub>, Qb<sub>s</sub> and Q<sup>2</sup> can be written as
()

$$
S_{o}^{2}
$$

$$
L
$$

$$
S_{o}^{2}
$$

$$
A.
$$

$$
a_{s},Qb_{s}
$$

$$
Q^{2}
$$

(5.3)

$$
\partial_{t}a_{s}=L[a_{s}]+\frac{1}{b^{2}}\left(-2a_{s}b_{s}^{2}-6Q^{2}a_{s}+8Q^{3}b_{s}\right)
$$

(5.4)

$$
\partial_{t}Q b_{s}=L[Q b_{s}]+\frac{1}{b^{2}}\left(4Q^{2}a_{s}-10Q^{3}b_{s}-2Q b_{s}^{3}+8Q b_{s}\right)
$$

(5.5)

$$
\partial_{t}Q^{2}=L[Q^{2}]+\frac{1}{b^{2}}\left(4Q a_{s}b_{s}-4Q^{2}b_{s}^{2}-8Q^{4}+8Q^{2}\right).
$$

Since the operator *L* is linear, one sees that
of the form

*T*

<sub>(α,β,γ)</sub> satisfies an evolution equation
1

$$
L
$$

$$
T_{(\alpha,\beta,\gamma)}
$$

$$
\partial_{t}T_{(\alpha,\beta,\gamma)}=L[T_{(\alpha,\beta,\gamma)}]+\frac{1}{b^{2}}C_{(\alpha,\beta,\gamma)},
$$

(5.6)

where C<sub>(α,β,γ)</sub> is a function of a<sub>s</sub>, b<sub>s</sub> and Q. This evolution equation is very useful,
as it allows us to systematically search for preserved inequalities. In particular, if
we can find α,β,γ,δ ∈ R for which we can determine the sign of C<sub>(α,β,γ)</sub> at a local
extrema of T<sub>(α,β,γ)</sub> at which T<sub>(α,β,γ)</sub> = δ, it follows from the maximum principle of
Theorem 3.2 that, depending on the sign, either

$$
a_{s},\;b_{s}
$$

$$
C_{(\alpha,\beta,\gamma)}
$$

$$
Q.
$$

$$
\alpha,\beta,\gamma,\delta\in\mathbb{R}
$$

$$
C_{(\alpha,\beta,\gamma)}
$$

$$
T_{(\alpha,\beta,\gamma)}
$$

$$
T_{(\alpha,\beta,\gamma)}=\delta
$$

$$
T_{(\alpha,\beta,\gamma)}\geq\delta
$$

or

$$
T_{(\alpha,\beta,\gamma)}\leq\delta
$$

is a preserved inequality.

We searched for real numbers *α,β,γ* and *δ* leading to preserved conditions that
yield the most useful control of the geometry of the flow. This is how we found the
quantities *T<sub>1</sub>, T<sub>2</sub>, T<sub>3</sub>* and *T<sub>4</sub>.* In later sections we will make heavy use of each of
their respective inequalities. For instance, we use the preserved inequalities *T<sub>1</sub> ≥* 0
to exclude shrinking solitons on M<sub>k</sub>, k ≥ 2, in the next section. Finally, in section
11 we generalize the above idea to find a continuously varying family of conserved
inequalities.

$$
\alpha,\beta,\gamma
$$

$$
\delta
$$

$$
T_{1},\;T_{2},\;T_{3}
$$

$$
T_{4}
$$

$$
T_{1}\geq0
$$

$$
M_{k},k\geq2
$$

Statement and proof of results. In this subsection we list the precise statements
and proofs of the results stated in the section outline. Before we begin, we prove
the following technical lemma, which we need for verifying the growth conditions of
the maximum principle of Theorem 7.5.

Lemma 5.1. Let (M<sub>k</sub>,g), k ∈ N, satisfy |Rm<sub>g</sub>|<sub>g</sub> ≤ K. Then
*√*

$$
|R m_{g}|_{g}\leq K
$$

$$
\big(M_{k},g\big),\:k\in\mathbb{N},
$$

$$
|a_{s}|,|Q b_{s}|,|Q^{2}|=O\left(\exp(2\sqrt{K}s)\right).
$$

*Proof.* By the curvature components listed in section 2.3 we see that
∣∣ ∣∣
∣ ∣

$$
\left|\frac{a_{{s s}}}{a}\right|,\left|\frac{b_{{s s}}}{b}\right|\leq K.
$$

---

Integrating

$$
b_{ss}\leq bK,
$$

shows that

$$
b=O\left(\exp\left(\sqrt{K}s\right)\right).
$$

From Lemma 3.3 we have

$$
Q^{2}\leq\frac{5}{3}Kb^{2}
$$

from which we conclude that

$$
Q^{2}=O\left(\exp\left(2\sqrt{K}s\right)\right).
$$

Similarly, Lemma 3.3 shows

$$
|b_{s}|\leq\sqrt{5K}b
$$

from which we deduce that

$$
|Q b_{s}|\leq\sqrt{\frac{25}{3}}K b^{2}
$$

and hence

$$
|Q b_{s}|=O(\exp(2\sqrt{K}s)).
$$

Finally,

$$
\left|a_{ss}\right|\leq aK
$$

shows that

$$
|a_{s}|=O(\exp(\sqrt{K}s)).
$$

This concludes the proof.

Now we begin proving the conserved inequalities listed above.

Lemma 5.2. Let (M<sub>k</sub>,g(t)), t ∈ [0,T]
*ture. Then the inequality*

*, k ≥ 1, be a Ricci flow with bounded curva*-
Q ≤ 1

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

$$
Q\leq1
$$

*is preserved by the Ricci flow.*

˜ = 1
*Proof.* Define the quantity *Q − Q.*
see
<u><em>b</em></u>
˜ = ˜ ˜

From the evolution equation (5.1) of *Q* we
()
<u>4</u>
˜

$$
\tilde{Q}=1-Q
$$

$$
Q
$$

$$
\partial_{t}\tilde{Q}=\tilde{Q}_{s s}+3\frac{b_{s}}{b}\tilde{Q}_{s}+\tilde{Q}\left(-\frac{4}{b^{2}}Q(1+Q)\right).
$$

As *Q ≥* 0 everywhere, the coefficient *−*
˜
by Lemma 5.1 we have *|Q|* = o(exp(s<sup>2</sup>
principle of Theorem 3.2 to deduce that
thus follows.

<sub>b</sub><sup>4</sup><sub>2</sub>Q(1 + Q) is non-positive. Furthermore,
)). Therefore we may apply the maximum
˜
Q ≥ 0 on M<sub>k</sub> × [0,T]. The desired result

$$
Q\geq0
$$

$$
-\frac{4}{b^{2}}Q(1+Q)
$$

$$
|\tilde{Q}|=o(\exp(s^2))
$$

$$
\tilde{Q}\geq0
$$

$$
M_{k}\times[0,T]
$$

Lemma 5.3. Let (M<sub>k</sub>,g(t)), t ∈ [0,T
*curvature. Then the inequality*

*], k* = *1,2, be a Ricci flow with bounded
x ≤* 0

$$
(M_{k},g(t)),\quad t\in[0,T],\quad k=1,2,
$$

$$
x\leq0
$$

*is preserved by the Ricci flow.*

---

*Proof.* The evolution equation of *x,* as derived in the Appendix A, is

$$
x,
$$

$$
A,
$$

(5.7)

$$
\begin{aligned}\partial_{t}x&=L[x]-\frac{2}{b^{2}}\left(2Q^{2}+y^{2}\right)x-\frac{2}{b^{2}}\left(Q^{2}+2\right)y^{2}\\&\leq L[x]-\frac{2}{b^{2}}\left(2Q^{2}+y^{2}\right)x\end{aligned}
$$

Note that *|x|* = o(exp(s<sup>2</sup>)) by Lemma 5.1. Therefore applying the maximum principle of Theorem 3.2 yields the desired result.

$$
|x|=o(\exp(s^2))
$$

*Remark* 5.4. Note that *x* = 2 *− k* at *s* = 0 by the boundary conditions (1.3).
Therefore the result can only hold for *k* = 1,2.

$$
x\;=\;2-k
$$

$$
s\;=\;0
$$

$$
k=1,2.
$$

Lemma 5.5. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1, be a Ricci flow with bounded curva-
*ture. Then the inequality*

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

$$
y\leq0
$$

*is preserved by the Ricci flow.*

*Proof.* Let *K* > 0 such that

$$
K>0
$$

$$
\operatorname*{s u p}_{M_{k}\times[0,T]}|{R m}_{g(t)}|_{g(t)}<K.
$$

Since y is an odd quantity, we consider the quantity Qy = Qb<sub>s</sub> − Q<sup>2</sup> instead. Its
evolution equation is

$$
y
$$

$$
Qy=Qb_{s}-Q^{2}
$$

(5.8)

$$
\partial_{t}Q y=L[Q y]-2\frac{Q y}{b^{2}}\left(2(Q^{2}+x)+Q y+y^{2}\right).
$$

Note that

$$
\begin{align*}-\frac{2}{b^2}\left(2(Q^2+x)+Qy+y^2\right)&=-\frac{2}{b^2}\left(4Q^2-4+b^2M_1+Qb_s+b_s^2\right)\\&\leq\frac{8}{b^2}+2K+2\frac{|Q\|b_s|}{b^2}\\&\leq\frac{8}{b^2}+2K+\frac{Q^2}{b^2}+\frac{b_s^2}{b^2},\end{align*}
$$

where *M<sub>1</sub>* is one of the curvature components listed in section 2.3. By Lemma 3.3
we see that for some *C* > 0
()

$$
M_{1}
$$

$$
C>0
$$

$$
-\frac{2}{b^{2}}\left(2(Q^{2}+x)+Qy+y^{2}\right)\leq CK\quad on\quad M_{k}\times[0,T]
$$

Furthermore *|Qy|* = o(exp(s<sup>2</sup>)) by Lemma 5.1. Now the result follows from applying
the maximum principle of Theorem 3.2.

$$
\left|Q y\right|=o\left(\exp\left(s^{2}\right)\right)
$$

Lemma 5.6. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1, be a Ricci flow with bounded curvature. If the initial metric g(0) satisfies a<sub>s</sub>,b<sub>s</sub> ≥ 0, then a<sub>s</sub>,b<sub>s</sub> ≥ 0 for all times
*t ∈* [*0,T].*

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

$$
g(0)
$$

$$
a_{s},b_{s}\geq0
$$

$$
a_{s},b_{s}\geq0
$$

$$
t\in[0,T]
$$

---

Proof. The evolution equations (5.3) and (5.4) of a<sub>s</sub> and Qb
system of weakly coupled parabolic equations
()
()<sub>2</sub>

<sub>s</sub> can be written as a

$$
a_{s}
$$

$$
Qb_{s}
$$

)(5.9)

$$
\partial_{t}a_{s}=L[a_{s}]-\left(2\left(\frac{b_{s}}{b}\right)^{2}+6\frac{Q^{2}}{b^{2}}\right)a_{s}+8\frac{Q^{2}}{b^{2}}(Q b_{s})
$$

$$
\partial_{t}Q b_{s}=L[Q b_{s}]+4\frac{Q^{2}}{b^{2}}a_{s}+\left(\frac{8-10Q^{2}}{b^{2}}-2\left(\frac{b_{s}}{b}\right)^{2}\right)(Q b_{s}),
$$

(5.10)

By Lemma 3.3 and Lemma 3.4 the zeroth order coefficients of a<sub>s</sub> and Qb<sub>s</sub> are
bounded. Lemma 5.1 shows that |a<sub>s</sub>|, |b<sub>s</sub>| = o(exp(s<sup>2</sup>)). Finally, note that the
3 2
off-diagonal coefficients 8<sup>Q</sup><sub>b</sub>2and 4<sup>Q</sup><sub>b</sub>2are non-negative. Thus the desired result follows by the maximum principle for weakly coupled parabolic equations of Lemma
3.6.

$$
a_{s}
$$

$$
Qb_{s}
$$

$$
|a_{s}|,|b_{s}|=o(\exp(s^{2}))
$$

$$
8\frac{Q^{3}}{b^{2}}
$$

$$
4\frac{Q^{\vec{2}}}{b^{2}}
$$

Lemma 5.7. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1, be a Ricci flow with bounded curvature
satisfying y ≤ 0,Q≤ 1 and a<sub>s</sub>,b<sub>s</sub> ≥ 0. Then for C ≥ 2 the inequality

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

$$
y\leq0,Q\leq1
$$

$$
a_{s},b_{s}\geq0
$$

$$
C\geq2
$$

$$
a_{s}\leq C
$$

*is preserved by the Ricci flow.*

Proof. Define the quantity A := a<sub>s</sub>
a<sub>s</sub> it follows that
(
()<sub>2</sub>

*− C.* Then from the evolution equation (5.9) of
)

$$
A:=a_{s}-C
$$

$$
a_{s}
$$

$$
\partial_{t}A=L[A]-\left(2\left(\frac{b_{s}}{b}\right)^{2}+6\frac{Q^{2}}{b^{2}}\right)A+\frac{1}{b^{2}}\left(8Q^{3}b_{s}-C Q^{2}-2C b_{s}^{2}\right).
$$

Fix *C ≥* 2. Then

$$
C\geq2
$$

$$
8Q^{3}b_{s}-6CQ^{2}-2Cb_{s}^{2}\leq8Q^{4}-CQ^{2}\leq(8-6C)Q^{2}\leq0,
$$

where we used Q ≤ 1 and y = b<sub>s</sub> −Q≤ 0. As |A| = o(exp(s<sup>2</sup>)) by Lemma 5.1 it
follows from the maximum principle of Theorem 7.5 that the inequality *A ≤* 0 is
preserved by the Ricci flow. This proves the desired result.

$$
Q\leq1
$$

$$
y=b_{s}-Q\leq0
$$

$$
|A|=o(\exp(s^2))
$$

$$
A\leq0
$$

Lemma 5.8. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1, be a Ricci flow with bounded curvature
satisfying y ≤ 0, b<sub>s</sub> ≥ 0 and Q ≤ 1. Then the inequality

$$
\left(M_{k},g(t)\right),t\in[0,T],k\geq1
$$

$$
y\leq0,b_s\geq0
$$

$$
Q\leq1
$$

$$
T_{1}=a_{s}+2Q^{2}-2\geq0
$$

*is preserved by the Ricci flow.*

(5.11)

$$
T_{1}
$$

$$
\begin{aligned}{\partial_{t}T_{1}=L[T_{1}]}&{{}+\frac{1}{b^{2}}\left[-4\left(1+Q^{2}\right)y^{2}+8Q\left(1-2Q^{2}\right)y+16Q^{2}\left(1-Q^{2}\right)\right]}\\ {}&{{}+T_{1}\frac{2y}{b^{2}}\left(2Q-y\right),}\\ \end{aligned}
$$ which can be derived from the evolution equations (5.3), (5.4) and (5.5) for a<sub>s</sub>, Qb<sub>s</sub>
and *Q<sup>2</sup>* listed above. Inspecting the quadratic expression
() () ()

$$
a_{s},Qb_{s}
$$

$$
Q^{2}
$$

(5.12)

$$
-4\left(1+Q^{2}\right)y^{2}+8Q\left(1-2Q^{2}\right)y+16Q^{2}\left(1-Q^{2}\right)
$$

we see that when *y* = 0 it is equal to
(

$$
y=0
$$

$$
16Q^{2}\left(1-Q^{2}\right)\geq0
$$

and when *y* = *−Q* it is equal to

$$
y=-Q
$$

$$
4Q^{2}\left(1-Q^{2}\right)\geq0
$$

As y = b<sub>s</sub> − Q ∈ [−Q,0] by the assumptions
furthermore the quadratic expression (5.12) is concave in
2y

y ≤ 0, b<sub>s</sub> ≥ 0 and Q ≤ 1, and
*y,* we conclude that

$$
y=b_{s}-Q\in[-Q,0]
$$

$$
y\leq0,\;b_s\geq0
$$

$$
Q\leq1
$$

$$
\partial_{t}T_{1}\geq L[T_{1}]+\frac{2y}{b^{2}}\left(2Q-y\right)T_{1}
$$

Note that the zeroth order coefficient of *T<sub>1</sub>* is bounded by Lemma 3.3. Furthermore *|T<sub>1</sub>|* = o(exp(s<sup>2</sup>)) by Lemma 5.1. Hence the result follows from applying the
maximum principle of Theorem 3.2.

$$
T_{1}
$$

$$
|T_{1}|=o(\exp(s^{2}))
$$

Below we prove some further preserved conditions. These can be skipped on the
first reading of the paper.

Lemma 5.9. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k = 1,2, be a Ricci flow with bounded
*curvature satisfying Q ≤ 1. Then the condition*
()

$$
\left(M_{k},g(t)\right),t\in[0,T]
$$

$$
Q\leq1
$$

$$
T_{2}=Qy-x=-a_{s}+Qb_{s}+2\left(1-Q^{2}\right)\geq0
$$

*is preserved by the Ricci flow.*

*Proof.* Note that *T<sub>2</sub>* = *2− k* when *s* = 0 by the boundary conditions (1.3). Therefore
the result can only hold true for *k* = 1,2. The evolution equations of *T<sub>2</sub>* is
4 () T<sub>2</sub> ()

$$
T_{2}=2-k
$$

$$
s=0
$$

$$
k=1,2
$$

$$
T_{2}
$$

(5.13)

$$
\partial_{t}T_{2}=L[T_{2}]+\frac{4}{b^{2}}\left(1-Q^{2}\right)y^{2}-2\frac{T_{2}}{b^{2}}\left(\left(b_{s}-2Q\right)^{2}+Q^{2}\right).
$$

$$
|T_{2}|\;=\;o(\exp(s^{2}))
$$

Lemma 5.10. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k
*curvature satisfying Q ≤ 1. Then the inequality*

*≥ 1, be a Ricci flow with bounded*

$$
(M_{k},g(t)),\quad t\in[0,T],\quad k\geq1
$$

$$
Q\leq1
$$

$$
T_{3}=a_{s}-Qb_{s}-Q^{2}+1\geq0
$$

*is preserved by the Ricci flow.*

(5.14)

$$
T_{3}
$$

$$
\partial_{t}T_{3}=L[T_{3}]+\frac{2}{b^{2}}\left(1-Q^{2}\right)y^{2}-2\frac{T_{3}}{b^{2}}\left((b_{s}+Q)^{2}+4Q^{2}\right)
$$

Note that the coefficients are bounded by Lemma 3.3. Furthermore *|T<sub>3</sub>|* = o(exp(s<sup>2</sup>))
by Lemma 5.1. Applying the maximum principle of Theorem 3.2 yields the desired
result.

$$
|T_{3}|=o(\exp(s^{2}))
$$

---

Lemma 5.11. Let (M<sub>k</sub>,g(t)), t ∈ [0,T], k ≥ 1, be a Ricci flow with bounded
curvature satisfying y ≤ 0, b<sub>s</sub> ≥ 0 and Q ≤ 1. Then the inequality

$$
(M_{k},g(t)),\quad t\in[0,T],\quad k\geq1
$$

$$
y\leq0,b_s\geq0and Q\leq1
$$

$$
\min(T_{1},T_{4})\geq0
$$

*is preserved by the Ricci flow. Here*

$$
T_{1}=a_{s}+2Q^{2}-2
$$

$$
T_{4}=a_{s}-\frac{1}{2}Q b_{s}-\left(1-Q^{2}\right).
$$

*Proof.* By Lemma 5.8 we already know that the inequality

$$
T_{1}=a_{s}-2+2Q^{2}\geq0
$$

is preserved. Thus we only need to show that *T<sub>4</sub> ≥* 0 is preserved whenever the
Ricci flow satisfies *T<sub>1</sub> ≥* 0. The evolution equation of *T<sub>4</sub>* is
1 ( () ())

$$
T_{4}\geq0
$$

$$
T_{1}\geq0
$$

$$
T_{4}
$$

$$
\partial_{t}T_{4}=L[T_{4}]+\frac{1}{b^{2}}\left(b_{s}\left(5Q^{3}-2b_{s}\right)-2T_{4}\left(4Q^{2}-2Q b_{s}+b_{s}^{2}\right)\right).
$$

A computation shows

$$
\frac{1}{2}Q b_s=T_1-T_4+1-Q^2.
$$

2
By the assumption *y ≤* 0 we have

$$
y\leq0
$$

$$
\frac{Q^{2}}{2}\geq\frac{1}{2}Q b_{s}
$$

and hence it follows that

$$
Q^{2}\geq\frac{2}{3}\left(1-T_{4}\right).
$$

Therefore

$$
5Q^{3}-2b_{s}\geq5Q^{3}-2Q\geq Q\left(\frac{4}{3}-\frac{10}{3}T_{4}\right),
$$

which implies that

$$
\partial_{t}T_{4}\geq L[T_{4}]-\frac{2T_{4}}{b^{2}}\left(4Q^{2}-\frac{1}{3}Q b_{s}+b_{s}^{2}\right)
$$

since b<sub>s</sub> ≥ 0. Note that the zeroth order coefficient of T<sub>4</sub> is bounded by Lemma 3.3.
Furthermore *|T<sub>4</sub>|* = o(exp(s<sup>2</sup>)) by Lemma 5.1. Applying the maximum principle of
Theorem 3.2 yields the desired result.

$$
b_{s}\geq0
$$

$$
T_{4}
$$

## 6. Exclusion of shrinking solitons

In this section we rule out U(2)-invariant shrinking solitons on M<sub>k</sub>, k ≥ 2, within
a large class of metrics. In particular, we show

$$
M_{k},k\geq2
$$

Theorem 6.1 (No shrinker). On M<sub>k</sub>, k ≥ 2, there does not exists a complete U(2)-
*invariant shrinking Ricci soliton of bounded curvature satisfying the conditions*

$$
M_{k},k\geq2
$$

$$
U(2).
$$

(1) supp∈M|b<sub>s</sub>|<∞
k
*(2) T<sub>1</sub>* = *a* + *2Q<sup>2</sup> −* 2

$$
\sup_{p\in M_{k}}\left|b_{s}\right|<\infty
$$

$$
\bar{T}_{1}=a_{s}+2Q^{2}-2>0for s>0
$$ a
*(3) Q* = *≤* 1
*b*

$$
Q=\frac{a}{b}\leq1
$$

This theorem is the key ingredient in section 10, where we show that certain Ricci
flows on M<sub>k</sub>, k ≥ 3, develop Type II singularities in finite time.

$$
M_{k},k\geq3
$$

$$
\left(M,g(t)\right)
$$

Soliton equations. Recall that a shrinking Ricci soliton *(M,g(t))* is a solution to
the Ricci flow equation that up to diffeomorphism homothetically shrinks. Such a
soliton solution may be written as

$$
g(t)=\sigma^{2}(t)\Phi_{t}^{*}g(0),
$$

where

$$
\sigma(t)=\sqrt{1-2\rho t}
$$

for some ρ > 0 and Φ<sub>t</sub> is a family of diffeomorphisms. The reader may consult [Top06] for more details. Hence for a U(2)-invariant shrinking Ricci soliton
(M<sub>k</sub>,g(t)), k ≥ 1, the corresponding warping functions can be written as
()

$$
\rho>0
$$

$$
\Phi_{t}
$$

$$
U(2)
$$

$$
(M_{k},g(t)),\;k\geq1
$$

(6.1)

$$
a(s,t)=\sigma(t)a\left(\frac{s}{\sigma(t)},0\right)
$$

(6.2)

$$
b(s,t)=\sigma(t)b\left(\frac{s}{\sigma(t)},0\right).
$$

The above formulae are with respect to the radial coordinate *s,* which is equivalent
to fixing a gauge. For this reason the family of diffeomorphisms Φ<sub>t</sub> does not appear
explicitly. Differentiating with respect to *t* at time 0 yields
()

$$
s,
$$

$$
\Phi_{t}
$$

$$
\begin{align*}\partial_{t}|_{t=0}a(s,t)&=a_{s}(s,0)\left(\frac{\partial s}{\partial t}+\rho s\right)-\rho a(s,0)\\&=a_{s}(s,0)f_{s}-\rho a(s,0),\end{align*}
$$

where f : M<sub>k</sub> → R is the potential function satisfying

$$
f_{ss}=\rho+\frac{a_{ss}}{a}+2\frac{b_{ss}}{b}
$$

$$
f:M_{k}\rightarrow\mathbb{R}
$$

∂s
and we used the expression (2.15) for derived in section 2.4. Similarly we obtain
*∂t*

$$
\frac{\partial s}{\partial t}
$$

$$
\partial_{t}|_{t=0}b\big(s,t\big)=b_{s}\big(s,0\big)f_{s}\big(s\big)-\rho b\big(s,0\big).
$$

Substituting the expressions ∂<sub>t</sub>a and ∂<sub>t</sub>b from the Ricci flow equations (2.11) and
(2.12), respectively, we see that the soliton equations for the warping functions *a*
and *b* at time *t* = 0 read (c.f. [A17])

$$
\partial_{t}a
$$

$$
\partial_{t}b
$$

(6.3)

$$
t=0
$$

$$
f_{ss}=\frac{a_{ss}}{a}+2\frac{b_{ss}}{b}+\rho
$$

(6.4)

$$
a_{s s}=2\frac{a^{3}}{b^{4}}-2\frac{a_{s}\dot{b}_{s}}{b}+a_{s}f_{s}-\rho a
$$

(6.5)

$$
b_{s s}=\frac{4}{b}-2\frac{a^{2}}{b^{3}}-\frac{a_{s}b_{s}}{a}-\frac{b_{s}^{2}}{b}+b_{s}f_{s}-\rho b
$$

---

In a slight abuse of notation we will denote *a* and *b* as functions of *s* only when
we are considering Ricci solitons. In that case *a* and *b* should be interpreted as the
initial data *a(s,0*) and *b(s,0*) at time zero that leads to a Ricci soliton solution, via
the correspondence (6.1) and (6.2).

$$
a(s,0)
$$

$$
b(s,0)
$$

Remark 6.2. The above shows that all U(2)-invariant Ricci solitons on M<sub>k</sub> are automatically gradient Ricci solitons with potential function *f.*

$$
U(2)
$$

$$
M_{k}
$$

$$
f
$$

Evolution of *x, y* and *Q* on soliton background. Since *x, y* and *Q* are *scaleinvariant* quantities, their evolution on a Ricci soliton background can be expressed
as follows:
()

$$
x,y
$$

$$
Q
$$

$$
Q
$$

$$
x(s,t)=x\left(\frac{s}{\sigma(t)},0\right)
$$

$$
y(s,t)=y\left(\frac{s}{\sigma(t)},0\right)
$$

$$
Q(s,t)=Q\left(\frac{s}{\sigma(t)},0\right)
$$

Differentiating, we therefore obtain

$$
\partial_{t}|_{t=0}x(s,t)=x_{s}(s,0)f_{s}(s)
$$

$$
\partial_{t}|_{t=0}y(s,t)=y_{s}(s,0)f_{s}(s)
$$

$$
\partial_{t}|_{t=0}Q(s,t)=Q_{s}(s,0)f_{s}(s).
$$

With help of the evolution equations (5.7), (12.7) and (5.1) for *x, y* and *Q,* this
yields the following ordinary differential equations for *x, y* and *Q* at time zero on a
soliton background
()

$$
Q,
$$

$$
x,y
$$

$$
Q
$$

(6.6)

$$
0=x_{s s}+\left(2\frac{b_{s}}{b}-\frac{a_{s}}{a}-f_{s}\right)x_{s}-\frac{1}{b^{2}}\left(2Q^{2}\left(2x+y^{2}\right)+2y^{2}\left(2+x\right)\right)
$$

(6.7)

$$
0=y_{ss}+\left(\frac{a_s}{a}-f_s\right)y_s-\frac{y}{a^2}\left((x+2)^2+Q^2\left(2x+y^2\right)\right)
$$

(6.8)

$$
0=Q_{s s}+\left(3\frac{\bar{b}_{s}}{b}-f_{s}\right)Q_{s}+\frac{4}{b^{2}}Q\left(1-Q^{2}\right).
$$

Alternatively these equations can be derived from the soliton equations (6.3)-(6.5).
In a slight abuse of notation we will often denote *x, y* and *Q* as functions of *s* only
when we are considering Ricci solitons.

Exclusion of shrinking solitons. By [CZ10] we know that the potential function
of a non-compact complete shrinking Ricci soliton grows quadratically with the
distance to some fixed point. In our setting this translates into the following lemma:

---

Lemma 6.3. Let (M<sub>k</sub>,g), k ≥ 1, be a complete non-compact shrinking Ricci soliton
*of bounded curvature. Then*
<u><em>ρ</em></u>

$$
(M_{k},g),k\geq1
$$

$$
\begin{aligned}{f}&{{}\sim\frac{\rho}{2}s^{2}}\\ {f_{s}}&{{}\sim\rho s}\\ \end{aligned}
$$

*as s →∞.*

$$
s\to\infty.
$$

*Proof.* See Theorem 1.1, equation (2.3) and equation (2.8) of [CZ10].

This allows us to prove the following lemma:

Lemma 6.4. Let (M<sub>k</sub>,g), k ≥ 1, be a complete non-compact shrinking Ricci soliton
of bounded curvature with Q ≤ 1 on M<sub>k</sub>. Then Q<sub>s</sub> ≥ 0 on M<sub>k</sub>.

$$
(M_k,g),k\geq1
$$

$$
Q\leq1
$$

$$
Q_{s}\geq0
$$

$$
M_{k}
$$

$$
M_{k}
$$

*Proof.* First notice that for a complete shrinking Ricci soliton with *Q ≤* 1, the strong
maximum principle applied to the evolution equation (5.1) of *Q* forces

$$
Q\leq1
$$

$$
Q<1\quad\mathrm{for}\quad s\geq0,
$$

$$
Q
$$

as otherwise we would have *Q* = 1 everywhere, which cannot be the case. Similarly,

$$
Q=1
$$

$$
Q>0
$$

unless we are at the origin *s* = 0. By equation (6.8) we have
()

$$
s=0
$$

(6.9)

$$
Q_{s s}=\left(f_{s}-3\frac{b_{s}}{b}\right)Q_{s}-\frac{4}{b^{2}}Q\left(1-Q^{2}\right).
$$

We now argue by contradiction. Assume there exists an s<sub>∗</sub> > 0 such that Q<sub>s</sub>(s<sub>∗</sub>) < 0.
Then Q<sub>s</sub>(s) < 0 for all s > s<sub>∗</sub>, because at any extremum of Q we have Q<sub>s</sub> = 0 and
4 ()

$$
s_{*}>0
$$

$$
Q_{s}(s_{*})<0
$$

$$
Q_{s}(s)<0
$$

$$
s>s_{*}
$$

$$
Q
$$

$$
Q_{s}=0
$$

$$
Q_{ss}=-\frac{4}{b^{2}}Q\left(1-Q^{2}\right)<0.
$$

bs
Lemma 3.3 shows that is bounded and from Lemma 6.3 it follows that
*b*

$$
\frac{b_{s}}{b}
$$

$$
f_{s}\rightarrow\infty\quad as\quad s\rightarrow\infty.
$$

Therefore eventually

$$
f_{s}-3\frac{b_{s}}{b}>0
$$

from which it follows by equation (6.9) that

$$
Q_{ss}<0
$$

for sufficiently large *s.* This, however, contradicts that *Q* > 0 unless *s* = 0.

$$
s=0
$$

$$
Q>0
$$

In the lemma below we bound the term

$$
G:=(x+2)^2+Q^2(2x+y^2),
$$

which appears in the evolution equation (6.7) of *y,* away from zero.

$$
y,
$$

Lemma 6.5. Whenever Q<sub>s</sub> ≥ 0 and Q,T<sub>1</sub> > 0 we have G > 0.

$$
Q_{s}\geq0
$$

$$
Q,T_{1}>0
$$

$$
G>0
$$

---

*Proof.* We have

$$
\frac{Q_{s}}{Q}=\frac{a_{s}}{a}-\frac{b_{s}}{b}=\frac{x}{a}-\frac{y}{b}+\frac{2}{a}-\frac{2a}{b^{2}}.
$$

For Q<sub>s</sub> ≥ 0 it follows that

$$
Q_{s}\geq0
$$

$$
x-Qy\geq2\left(Q^{2}-1\right).
$$

Recall the quantity

$$
T_{1}=a_{s}+2Q^{2}-2
$$

defined in section 5. Then
(

$$
\begin{aligned}G&\geq\left(x+2\right)^{2}+Q^{2}\left(2\left(Q y+2\left(Q^{2}-1\right)\right)+y^{2}\right)\\ &=x^{2}+4x+4+2Q^{3}y+4Q^{4}-4Q^{2}+Q^{2}y^{2}\\ &=\left(a_{s}+Q^{2}-2\right)^{2}+4\left(a_{s}+Q^{2}-2\right)+4+3Q^{4}-4Q^{2}+Q^{2}\left(y+Q\right)^{2}\\ &=a_{s}^{2}+2Q^{2}a_{s}+4\left(Q^{4}-Q^{2}\right)+Q^{2}\left(y+Q\right)^{2}\\ &=a_{s}^{2}+2Q^{2}T_{1}+Q^{2}\left(y+Q\right)^{2}\\ &=a_{s}^{2}+Q^{2}b_{s}^{2}+2Q^{2}T_{1}>0\end{aligned}
$$

Now we prove the non-existence of shrinking solitons.

*Proof of Theorem 6.1.* We argue by contradiction. Assume such a shrinking Ricci
soliton exists. Applying L’Ĥopital’s Rule to the evolution equation (2.12) of *b* shows
that at *s* = 0
∣
∣ <u>4</u>

$$
s=0
$$

$$
\begin{aligned}\partial_{t}b\Big|_{s=0}&=2b_{s s}-\frac{4}{b}\\&=2\left(y_{s}+\frac{k-2}{b}\right).\end{aligned}
$$

Clearly, every shrinking soliton satisfies
∣
∣

$$
\partial_{t}b\Big|_{s=0}<0.
$$

The boundary conditions (1.3) of *a* and *b* at *s* = 0 imply that

$$
y(0)=0.
$$

and thus we deduce from the above that

$$
y_{s}(0)<0,
$$

as *k ≥* 2 by assumption. The ordinary differential equation (6.7) for *y* can be written
as
()
<u><em>a y</em></u>

$$
k\geq2
$$

(6.10)

$$
y_{ss}=\left(f_s-\frac{a_s}{a}\right)y_s+\frac{y}{a^2}G.
$$

Lemma 6.4 and Lemma 6.5 imply that

$$
G>0\quad\mathrm{for}\quad s>0,
$$ which in turn shows that y<sub>s</sub> ≤ 0 everywhere, as at a negative local minimum of y
we would have
<u><em>y</em></u>

$$
y_{s}\leq0
$$

$$
y
$$

$$
y_{ss}=\frac{y}{a^2}G<0.
$$

as
The asymptotic properties of *f* listed in Lemma 6.3 and the bounds on proven
*a*
in Lemma 3.4 show that eventually

$$
\frac{a_{s}}{a}
$$

$$
f_{s}-\frac{a_{s}}{a}>0
$$

and hence from the equation (6.10) it follows that

$$
y_{ss}<0
$$

for *s* sufficiently large. From this it follows that

$$
\lim_{s\rightarrow\infty}y=\lim_{s\rightarrow\infty}\left(b_{s}-Q\right)=-\infty,
$$

which contradicts our assumptions on b<sub>s</sub> and Q.

$$
b_{s}
$$

$$
Q
$$

## 7. Curvature bound

The aim of this section is to prove that a Ricci flow (M<sub>k</sub>,g(t)), k ∈ N, t ∈ [0,T),
starting from an initial metric g(0) *∈ I* — where *I* is a class of metrics to be
discussed below — with supp∈Mb(p,0) < *∞* satisfies the curvature bound
*k*

$$
\left(M_{k},g(t)\right),k\in\mathbb{N},t\in[0,T)
$$

$$
g(0)\in\mathcal{I}—
$$

$$
\sup_{p\in M_{k}}b(p,0)<\infty
$$

$$
|R m_{g(t)}|_{g(t)}\leq C_{1}b^{-2}\quad\mathrm{for}\quad t\in(0,T),
$$

where *C<sub>1</sub>* > 0 is some constant. This allows us to control the geometry via the
warping function *b,* which will be crucial for constructing blow-up limits in the
following parts of the paper. Note that this bound was already derived in the
compact case in [IKS17] and we will follow their strategy to prove it in our noncompact setting.

$$
C_{1}>0
$$

Recall the following definition (see also [ChI][Definition 8.23]):

Definition 7.1 (*κ*-non-collapsing). Let (M,g(t)), *t ∈* [0,T), be a Ricci flow and
*κ* > 0. We say that the Ricci flow is *κ*-non-collapsed at a point *(p<sub>0</sub>,t<sub>0</sub>)* in spacetime
at scale *ρ* if the following two conditions hold for all *r ≤ ρ:*

$$
(M,g(t)),t\in[0,T)
$$

$$
\kappa>0
$$

$$
\left(p_{0},t_{0}\right)
$$

$$
\rho
$$

$$
r\leq\rho;
$$

• (bounded normalized curvature) We have |Rm(p,t)|≤ r<sup>−2</sup> for every (p,t) ∈
B<sub>g(t</sub>0<sub>)</sub>(p<sub>0</sub>,r) × [t<sub>0</sub> − r<sup>2</sup>,t<sub>0</sub>]. In particular we assume [t<sub>0</sub> − r<sup>2</sup>,t<sub>0</sub>] ⊂ [0,T).

$$
\left|R m(p,t)\right|\leq r^{-2}
$$

$$
B_{g(t_0)}(p_0,r)\times[t_0-r^2,t_0]
$$

$$
(p,t)\in
$$

$$
\left[t_{0}-r^{2},t_{0}\right]\subset\left[0,T\right)
$$

• (non collapsed volume) At time t<sub>0</sub> the ball B<sub>g(t</sub>0<sub>)</sub>(p<sub>0</sub>,r) has volume at least
*κr<sup>4</sup>.*

$$
t_{0}
$$

$$
\kappa r^{4}
$$

$$
B_{g(t_{0})}(p_{0},r)
$$

We now define the class of metrics *I.*

Definition 7.2. For *K* > 0 let *IK* be the set of all complete *bounded curvature*
metrics of the form (2.3) on M<sub>k</sub>, k ≥ 1, with positive injectivity radius that satisfy

$$
K>0
$$

$$
\mathcal{I}_{K}
$$

$$
M_{k},k\geq1
$$ the following scale-invariant inequalities:

$$
Q\leq1
$$

1(7.1)

0(7.2)

$$
a_{s},b_{s}\geq0
$$

0(7.3)

$$
y\leq0
$$

(7.4)

$$
\sup a_{s}<K
$$

(7.5)

Denote by *I* the set of metrics *g* such that for sufficiently large *K* > 0 we have
*g ∈IK.*

$$
g\in\mathcal{I}_{K}
$$

$$
K>0
$$

Note that for any k ∈ N the set I of metrics on M<sub>k</sub> is non-empty, as for example
the metric on M<sub>k</sub> defined by

$$
k\in\mathbb{N}
$$

$$
M_{k}
$$

$$
M_{k}
$$

$$
\begin{aligned}a(s)&=Q=\tanh(ks),\quad k\in\mathbb{N}\\b(s)&=1\end{aligned}
$$

is contained in *I.* In Lemma 7.9 below we show that if g(0) *∈IK<sub>0</sub>* for some *K<sub>0</sub>* > 0
then there exists a *K > K<sub>0</sub>* such that *g(t*) *∈IK* for *t ∈* [0,T). Note that conditions
(7.1)- (7.5) are scale-invariant, and therefore pass to blow-up limits.

$$
\mathcal{I}.
$$

$$
g(0)\in\mathcal{I}_{K_0}
$$

$$
K_{0}>0
$$

$$
K>K_{0}
$$

$$
g(t)\in\mathcal{I}_{K}
$$

$$
t\in[0,T)
$$

An adaptation of [ChI, Theorem 8.26] to our setting yields the following result:

Theorem 7.3 (No local collapsing). *Let g(t), t ∈* [*0,T), T < ∞, be a Ricci flow
starting from an initial metric* g(0) *∈ I. Then there exists a κ* > 0 *depending*
on T, inj(g(0)) and supM ×<sub>[0,T/2]</sub> Ric such that g(t) is κ-non-collapsed at every
<sup>g(t)</sup>√
(p,t) ∈M× (<sup>T</sup><sub>2</sub>,T) at every scale ρ < T/2.

$$
g(t),\;t\in[0,T)
$$

$$
T<\infty
$$

$$
g(0)\in\mathcal{I}
$$

$$
a\ \kappa\ >\ 0
$$

$$
T,\mathrm{inj}(g(0))
$$

$$
\sup_{M\times[0,T/2]}{R i c}_{g(t)}
$$

$$
g(t)
$$

$$
(p,t)\in M\times\left(\frac{T}{2},T\right)
$$

$$
\rho<\sqrt{T/2}
$$

*Remark* 7.4. Recall that if a Ricci flow *g(t*) is *κ*-non-collapsed at scale *ρ,* then the
parabolically dilated Ricci flow α<sup>2</sup>g(α<sup>−2</sup>t) is κ-non-collapsed at scale αρ. As the
*κ*-non-collapsedness property is preserved under Cheeger-Gromov limits, a blow-up
limit of a Ricci flow (M<sub>k</sub>,g(t)), [0,T<sub>sing</sub>) is κ-non-collapsed at all scales.

$$
g(t)
$$

$$
\rho,
$$

$$
\alpha^{2}g\left(\alpha^{-2}t\right)
$$

$$
\alpha\rho.
$$

$$
(M_{k},g(t)),[0,T_{\mathrm{sing}})
$$

Having set up the necessary terminology, we may now state the main theorem of
this section:

Theorem 7.5 (Curvature bound). Let (M<sub>k</sub>,g(t)), t ∈ [0,T), be a Ricci flow starting
*from an initial metric* g(0) *∈I (see Definition 7.2) with*

$$
\left(M_{k},g(t)\right),t\in[0,T)
$$

$$
g(0)\in\mathcal{I}
$$

$$
\operatorname*{s u p}_{p\in M_{k}}b(p,0)<\infty.
$$

*Then there exists a constant C<sub>1</sub>* > 0 *such that*

$$
C_{1}>0
$$

$$
\left|R m_{g(t)}\right|_{g(t)}(p)\leq C_{1}b(p,t)^{-2}
$$

for (p,t) ∈ M<sub>k</sub> × (0,T).

$$
(p,t)\in M_k\times(0,T)
$$

A useful variant of Theorem 7.5 is:

---

Corollary 7.6. Let (M<sub>k</sub>,g(t)) with g(t) ∈I (see Definition 7.2) for t ∈ (−∞,0]
*be an ancient Ricci flow solution which is κ-non-collapsed at all scales. Then there
exists a constant C<sub>1</sub>* > 0 *such that*

$$
\left(M_{k},g(t)\right)
$$

$$
g(t)\in\mathcal{I}
$$

$$
t\in(-\infty,0]
$$

$$
C_{1}>0
$$

$$
|R m_{g(t)}|_{g(t)}(p)\leq C_{1}b(p,t)^{-2}
$$

for (p,t) ∈ M<sub>k</sub> × (−∞,0].

$$
(p,t)\in M_{k}\times(-\infty,0].
$$

*Remark* 7.7. Corollary 7.6 follows immediately from Theorem 7.5 for ancient *κ*-
non-collapsed Ricci flows that arise as blow up limits of Ricci flows (M<sub>k</sub>,g(t)), t ∈
[0,T<sub>sing</sub>), g(0) ∈I, as the curvature bound is scale-invariant. Nevertheless, we give
a proof of the general case.

$$
\mathcal{K}^{-}
$$

$$
(M_{k},g(t)),t\in
$$

$$
\left[0,T_{\mathrm{sing}}\right),g(0)\in\mathcal{I}
$$

Let us now prove the assertions made above. We begin with the following lemma:

Lemma 7.8. Let K<sub>0</sub> > 0 and assume that (M<sub>k</sub>,g(t)), k ≥ 1, t ∈ [0,T), is a Ricci
*flow starting from an initial metric* g(0) *∈IK<sub>0</sub>. Then there exists a constant K ≥ 0,
depending only on the initial metric* g(0), *such that*

$$
K_{0}>0
$$

$$
\left(M_{k},g(t)\right),k\geq1,t\in[0,T)
$$

$$
g(0)\in\mathcal{I}_{K_0}
$$

$$
K\geq0
$$

$$
g(0)
$$

$$
\left|b b_{s s}\right|\leq K
$$

(7.6)

on M<sub>k</sub> × [0,T).

$$
M_{k}\times[0,T)
$$

*Proof.* We follow the proof strategy of [IKS17, Lemma 7]. Consider the quantities

$$
H_{-}=b b_{s s}+a_{s}^{2}-b_{s}^{2}-C
$$

$$
H_{+}=b b_{s s}-a_{s}^{2}-b_{s}^{2}+C,
$$

where *C* > 0 is a constant to be determined later. The goal is to show that the
inequalities H<sub>+</sub> ≥ 0 and H<sub>−</sub> ≤ 0 are preserved by the Ricci flow for sufficiently large
*C* > 0. The quantities *H*<sub>±</sub>satisfy the evolution equations
() ()

$$
C>0
$$

$$
H_{+}\geq0
$$

$$
H_{-}\leq0
$$

$$
C>0
$$

$$
H_{\pm}
$$

$$
\begin{aligned}\partial_{t}H_{\pm}&=[H_{\pm}]_{s s}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{\pm}]_{s}+H_{\pm}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}\right)\\&\pm C\left(\frac{2a_{s}^{2}}{a^{2}}+\frac{4a^{2}}{b^{4}}+\frac{4b_{s}^{2}}{b^{2}}\right)\\&\pm2a_{s s}^{2}+a_{s s}\left(-\frac{2b a_{s}b_{s}}{a^{2}}\mp\frac{8a_{s}b_{s}}{b}\pm\frac{4a_{s}^{2}}{a}+\frac{4a}{b^{2}}\right)\\&+\frac{2b a_{s}^{3}b_{s}}{a^{3}}-\frac{32a a_{s}b_{s}}{b^{3}}\mp\frac{16a^{3}a_{s}b_{s}}{b^{5}}+\frac{4a_{s}^{2}}{b^{2}}\pm\frac{8a^{2}a_{s}^{2}}{b^{4}}\\&\mp\frac{2a_{s}^{4}}{a^{2}}+\frac{32a^{2}b_{s}^{2}}{b^{4}}-\frac{16b_{s}^{2}}{b^{2}}.\\ \end{aligned}
$$

In the Appendix A we carry out the derivation of the evolution equation. We now
show that H<sub>−</sub> ≤ 0 is preserved. Using Young’s inequality to bound the terms

$$
H_{-}\leq0
$$ involving a<sub>ss</sub> and then disregarding non-positive terms not involving C, we obtain
() ()

$$
a_{ss}
$$

$$
C,
$$

$$
\begin{aligned}\partial_{t}H_{-}&\leq[H_{-}]_{ss}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{-}]_{s}+H_{-}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}\right)\\ &-C\left(\frac{2a_{s}^{2}}{a^{2}}+\frac{4a^{2}}{b^{4}}+\frac{4b_{s}^{2}}{b^{2}}\right)\\ &+\frac{1}{2}\left(\left(\frac{2ba_{s}b_{s}}{a^{2}}\right)^{2}+\left(\frac{8a_{s}b_{s}}{b}\right)^{2}+\left(\frac{4a_{s}^{2}}{a}\right)^{2}+\left(\frac{4a}{b^{2}}\right)^{2}\right)\\ &+\frac{2ba_{s}^{3}b_{s}}{a^{3}}+\frac{16a^{3}a_{s}b_{s}}{b^{5}}+\frac{4a_{s}^{2}}{b^{2}}+\frac{2a_{s}^{4}}{a^{2}}+\frac{32a^{2}b_{s}^{2}}{b^{4}}\end{aligned}
$$

Recall that on M<sub>k</sub> ×[0,T) we have y = b<sub>s</sub> − Q ≤ 0, Q ≤ 1, a<sub>s</sub>,b<sub>s</sub> ≥ 0 and a<sub>s</sub> ≤ C<sup>′</sup> for
some C<sup>′</sup> > 0 by Lemma 5.5, Lemma 5.2, Lemma 5.6 and Lemma 5.7, respectively.
Therefore we obtain the following bounds away from the non-principal orbit S<sub>o</sub><sup>2</sup>:
()<sub>2</sub> ()<sub>2</sub>

$$
M_{k}\times[0,T)
$$

$$
y=b_{s}-Q\leq0,Q\leq1,a_{s},b_{s}\geq0
$$

$$
a_{s}\leq C'
$$

$$
C^{\prime}>0
$$

$$
5.7.
$$

$$
S_{o}^{2}
$$

$$
\left(\frac{2ba_s b_s}{a^2}\right)^2=\left(\frac{2a_s b_s}{aQ}\right)^2\leq\frac{4a_s^2}{a^2}
$$

$$
\left(\frac{8a_{s}b_{s}}{b}\right)^{2}=\left(8\frac{a_{s}}{a}Qb_{s}\right)^{2}\leq64\frac{a_{s}^{2}}{a^{2}}
$$

$$
\left(\frac{4a_{s}^{2}}{a}\right)^{2}=16C^{\prime2}\frac{a_{s}^{2}}{a^{2}}
$$

$$
\frac{2ba_{s}^{3}b_{s}}{a^{3}}=\frac{2a_{s}^{3}}{a^{2}}\frac{b_{s}}{Q}\leq2C^{\prime}\frac{a_{s}^{2}}{a^{2}}
$$

$$
\frac{16a^{3}a_{s}b_{s}}{b^{5}}=16Q^{3}\frac{a_{s}b_{s}}{b^{2}}\leq8Q^{3}\left(\frac{a_{s}^{2}}{b^{2}}+\frac{b_{s}^{2}}{b^{2}}\right)\leq8\left(\frac{a_{s}^{2}}{a^{2}}+\frac{b_{s}^{2}}{b^{2}}\right)
$$

$$
\frac{4a_{s}^{2}}{b^{2}}\leq4\frac{a_{s}^{2}}{a^{2}}
$$

$$
\frac{2a_{s}^{4}}{a^{2}}\leq2C^{\prime2}\frac{a_{s}^{2}}{a^{2}}
$$

$$
\frac{32a^{2}b_{s}^{2}}{b^{4}}=32Q^{2}\frac{b_{s}^{2}}{b^{2}}\leq32\frac{b_{s}^{2}}{b^{2}}
$$

Hence for a sufficiently large *C* > 0 it follows that
()

$$
\partial_{t}H_{-}\leq[H_{-}]_{s s}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{-}]_{s}+H_{-}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}\right)
$$

away from the non-principal orbit *S*
for *s* > 0
(
∣

<sub>o</sub><sup>2</sup>. Switching to coordinates (s,t) we see that
) ()

$$
S_{o}^{2}
$$

$$
s>0
$$

(7.7)

$$
\partial_{t}\Big|_{s}H_{-}\leq[H_{-}]_{s s}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{-}]_{s}+H_{-}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}-\frac{\partial s}{\partial t}\right).
$$

---

On the non-principal orbit S<sub>o</sub><sup>2</sup>, or equivalently when s = 0, we have

$$
S_{o}^{2}
$$

$$
s=0
$$

$$
H_{-}=b b_{s s}+k^{2}-C\leq b Q_{s}+k^{2}-C\leq k+k^{2}-C,
$$

where we used that y = b<sub>s</sub> − Q ≤ 0 with equality at
have H<sub>−</sub> < 0 on {s = 0}× [0,T). Hence for every
such that
*H (s,t) ≤* 0 on *[0,s<sub>0</sub>] ×*

*s* = 0. Choosing *C > k<sup>2</sup>* + *k* we
T <sup>′</sup> ∈ [0,T) there exists a s<sub>0</sub> > 0
[0,T <sup>′</sup>],

$$
y=b_s-Q\leq0
$$

$$
s=0
$$

$$
C>k^{2}+k
$$

$$
H_{-}<0
$$

$$
\{s=0\}\times[0,T)
$$

$$
s_{0}>0
$$

$$
T^{\prime}\in[0,T)
$$

$$
H_{-}(s,t)\leq0\mathrm{on}[0,s_{0}]\times[0,T^{\prime}],
$$

as H<sub>−</sub>(s,t) is a smooth function on R≥0× [0,T <sup>′</sup>]. Furthermore note that

$$
H_{-}(s,t)
$$

$$
\mathbb{R}_{\geq0}\times[0,T^{\prime}]
$$

$$
|H_{-}|\leq|R m_{g(t)}|_{g(t)}b^{2}+C^{\prime2}+1+C,
$$

where we used the expression for the curvature component *R<sub>0202</sub>* derived in section
2.3. This shows that for each time t < T <sup>′</sup> the function H<sub>−</sub>(s,t) grows subexponentially. Note that by Lemma 3.3 and Lemma 3.4 the coefficient
a b

$$
R_{0202}
$$

$$
t<T'
$$

$$
H_{-}(s,t)
$$

$$
\frac{a_{s}}{a}-2\frac{b_{s}}{b}
$$

∂s
is bounded on [s<sub>0</sub>, ∞) × [0,T <sup>′</sup>]. Similarly, we see from the bound (3.7) on | |
∂t
presented in the proof of the maximum principle of Theorem 3.2, Case 1, that the
coefficient
*2a<sup>2</sup> 4a<sup>2</sup> 4b<sup>2</sup> ∂s*

$$
[s_{0},\infty)\times[0,T^{\prime}]
$$

$$
\left\lceil\frac{\partial s}{\partial t}\right\rceil
$$

$$
-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}-\frac{\partial s}{\partial t}
$$

grows at most linearly on every times slice of [s<sub>0</sub>, ∞) × [0,T <sup>′</sup>]. Therefore, applying
the weak maximum principle to the evolution equation (7.7) of H<sub>−</sub> on the parabolic
neighborhood [s<sub>0</sub>, ∞) × [0,T <sup>′</sup>], we deduce that

$$
[s_{0},\infty)\times[0,T^{\prime}]
$$

$$
H_{-}
$$

$$
[s_{0},\infty)\times[0,T^{\prime}]
$$

$$
H_{-}\leq0on M_{k}\times[0,T'].
$$

As T <sup>′</sup> ∈ [0,T) was arbitrary it follows that

H<sub>−</sub> ≤ 0 is preserved by the Ricci flow.

$$
T^{\prime}\in[0,T)
$$

$$
H_{-}\leq0
$$

We repeat the same process to prove that
inequality to bound terms involving
not involving *C,* we see that
(

H<sub>+</sub> ≥ 0 is preserved. Applying Young’s
a<sub>ss</sub> and then disregarding non-negative terms
) ()

$$
H_{+}\geq0
$$

$$
a_{ss}
$$

$$
C,
$$

$$
\begin{aligned}\partial_{t}H_{+}&\geq[H_{+}]_{ss}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{+}]_{s}+H_{+}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}\right)\\ &+C\left(\frac{2a_{s}^{2}}{a^{2}}+\frac{4a^{2}}{b^{4}}+\frac{4b_{s}^{2}}{b^{2}}\right)\\ &-\frac{1}{2}\left(\left(\frac{2ba_{s}b_{s}}{a^{2}}\right)^{2}+\left(\frac{8a_{s}b_{s}}{b}\right)^{2}+\left(\frac{4a_{s}^{2}}{a}\right)^{2}+\left(\frac{4a}{b^{2}}\right)^{2}\right)\\ &-\frac{32aa_{s}b_{s}}{b^{3}}-\frac{16a^{3}a_{s}b_{s}}{b^{5}}-\frac{2a_{s}^{4}}{a^{2}}-\frac{16b_{s}^{2}}{b^{2}}.\end{aligned}
$$

Bounding the zeroth order terms via Young’s inequality as above, we see that for
*C* > 0 sufficiently large
() ()

$$
C>0
$$

$$
\partial_{t}H_{+}\geq[H_{+}]_{s s}+\left(\frac{a_{s}}{a}-2\frac{b_{s}}{b}\right)[H_{+}]_{s}+H_{+}\left(-\frac{2a_{s}^{2}}{a^{2}}-\frac{4a^{2}}{b^{4}}-\frac{4b_{s}^{2}}{b^{2}}\right)
$$ away from the non-principal orbit S<sub>o</sub><sup>2</sup>. On the non-principal orbit S<sup>2</sup><sub>o</sub> we have

$$
S_{o}^{2}
$$

$$
S_{o}^{2}
$$

$$
H_{+}=b b_{s s}-k^{2}+C\geq-k^{2}+C,
$$

where we used that b<sub>s</sub> ≥ 0 with equality at s = 0 to deduce that b<sub>ss</sub> ≥ 0 at s = 0.
From here the above proof that H<sub>−</sub> ≤ 0 is preserved carries over and we may
conclude that H<sub>+</sub> ≥ 0 is preserved as well. Recalling the bounds on a<sub>s</sub> and b<sub>s</sub>, the
desired result now follows.

$$
b_{s}\geq0
$$

$$
s=0
$$

$$
b_{ss}\geq0
$$

$$
s=0
$$

$$
H_{-}\leq0
$$

$$
H_{+}\geq0
$$

$$
a_{s}
$$

$$
b_{s}
$$

Now we can prove that *I* (see Definition 7.2) is preserved by Ricci flow:

Lemma 7.9. *Let K<sub>0</sub>* > *0. Then there exists a K ≥ K<sub>0</sub> such that the following*
holds: Let (M<sub>k</sub>,g(t)), k ≥ 1, t ∈ [0,T), be a Ricci flow solution starting from an
*initial metric* g(0) *∈IK<sub>0</sub>. Then g(t*) *∈IK for every t ∈* [*0,T).*

$$
K_{0}>0
$$

$$
K\geq K_{0}
$$

$$
\left(M_{k},g(t)\right),k\geq1,t\in[0,T)
$$

$$
t\in[0,T)
$$

$$
g(t)\in\mathcal{I}_{K}
$$

$$
g(0)\in\mathcal{I}_{K_0}
$$

*Proof.* By Lemma 5.2, Lemma 5.6, Lemma 5.5, Lemma 5.7 we see that for *K* > 2
the conditions (7.1) - (7.4) are preserved. By Lemma 7.8 we see that there exists a
*K≥K<sub>0</sub>* such that inequality (7.5) holds for *t ∈* [0,T).

$$
K>2
$$

$$
(7.1)-(7.4)
$$

$$
K\geq K_{0}
$$

$$
t\in[0,T)
$$

Now we only need to prove that for every time *t ∈* [0,T) the metric *g(t*) has
bounded curvature and positive injectivity radius. As the curvature of g(0) is
bounded by the assumption that g(0) *∈ IK,* it follows by Shi’s Theorem [Shi89]
that for every time T <sup>′</sup> ∈ [0,T) the Ricci flow g(t) has bounded curvature on the
time interval [0,T <sup>′</sup>]. As inj<sub>g(0)</sub> > 0 it follows that the metric g(0) is non-collapsed.
By standard volume distortion estimates it follows that for each *t ∈* [0,T/2] the
metric g(t) is non-collapsed, and hence inj<sub>g(t)</sub> > 0. By Theorem 7.3 there exists a
*κ* > 0 and√ρ > 0 such that for each *t ∈* [0,T) the metric *g(t*) is *κ*-non-collapsed at
scale ρ < T/2. This shows that inj<sub>g(t)</sub> > 0 for all t ∈ [T/2,T).

$$
t\in[0,T)
$$

$$
g(t)
$$

$$
g(0)
$$

$$
g(0)\in\mathcal{I}_K
$$

$$
T^{\prime}\in[0,T)
$$

$$
g(t)
$$

$$
\left[0,T^{\prime}\right]
$$

$$
g(0)
$$

$$
\mathrm{inj}_{g(0)}>0
$$

$$
t\in[0,T/2]
$$

$$
g(t)
$$

$$
\mathrm{inj}_{g(t)}>0
$$

$$
\kappa>0
$$

$$
\rho>0
$$

$$
t\in[0,T)
$$

$$
g(t)
$$

$$
\rho<\sqrt{T/2}
$$

$$
\mathrm{inj}_{g(t)}>0
$$

$$
t\in[T/2,T)
$$

Before proving Theorem 7.5, we need to prove the following two lemmas in preparation:

Lemma 7.10. Let (M<sub>k</sub>,g(t)), k ≥ 1, t ∈ [0,T), be a Ricci flow starting from an
*initial metric* g(0) *∈I. Then there exists a constant C<sub>0</sub> ≥ 0, depending only on the
initial metric* g(0), *such that*

$$
\left(M_{k},g(t)\right),k\geq1,t\in[0,T)
$$

$$
g(0)\in\mathcal{I}
$$

$$
C_{0}\geq0
$$

(7.8)

$$
\left|\partial_{t}b^{2}\right|\leq C_{0}
$$

*Proof.* By Lemma 7.9 there exists a *K* > 0 such that *g(t*) *∈IK* for *t ∈* [0,T). From
the evolution equation (2.12) of *b* and Definition 7.2 of *IK* it follows that
∣ ∣

$$
K>0
$$

$$
g(t)\in\mathcal{I}_{K}
$$

$$
t\in[0,T)
$$

$$
\mathcal{I}_{K}
$$

$$
\begin{aligned}|\partial_{t}b^{2}|&=\left|2b b_{s s}-8+4Q^{2}+2\frac{a_{s}b_{s}}{Q}+2b_{s}^{2}\right|\\&\leq2K+8+4+2K+2\\&=4K+14\\ \end{aligned}
$$

This concludes the proof.

---

Lemma 7.11. Let (M<sub>k</sub>,g(t)), k ≥ 1, t ∈ [0,T
*initial metric* g(0) *∈I. Then*

*), be a Ricci flow starting from an*

$$
\left(M_{k},g(t)\right),k\geq1,t\in[0,T)
$$

$$
g(0)\in\mathcal{I}
$$

$$
\operatorname*{s u p}_{p\in M_{k}}b(p,t)\leq\operatorname*{s u p}_{p\in M_{k}}b(p,0)
$$

*for all t ∈* [*0,T).*

$$
t\in[0,T)
$$

*Proof.* From the evolution equation (2.12) of *b* and expression (2.4) for the Laplacian
with respect to the background metric *g(t*) it follows

$$
\begin{align*}\partial_{t}b^{2}&=\Delta_{g(t)}b^{2}-8+4Q^{2}-4b_{s}^{2}\\&\leq\Delta_{g(t)}b^{2}-4.\end{align*}
$$

Applying the maximum principle [ChII, Theorem 12.14] yields the desired result.

We now proceed to proving Theorem 7.5.

*Proof of Theorem 7.5.* We argue by contradiction. Assume there exists a sequence
of points (p<sub>i</sub>,t<sub>i</sub>) in spacetime and constants D<sub>i</sub> →∞ as i →∞ such that

$$
D_{i}\rightarrow\infty
$$

$$
(p_{i},t_{i})
$$

$$
i\to\infty
$$

$$
\begin{align*}|Rm_{g(t_i)}|_{g(t_i)}(p_i)=D_ib(p_i,t_i)^{-2}:=K_i\end{align*}
$$

and

$$
|R m_{g(t)}|_{g(t)}\leq D_{i}b^{-2}\quad\mathrm{on}\quad M_{k}\times[0,t_{i}].
$$

$$
g(0)
$$

By the assumption that g(0) *∈ I* the initial metric g(0) has bounded curvature.
Hence by Shi’s theorem [Shi89] we have that for every T <sup>′</sup> ∈ [0,T) the metric g(t)
has bounded curvature on M<sub>k</sub> × [0,T <sup>′</sup>]. As by Lemma 7.11 the warping function b
is uniformly bounded on M<sub>k</sub> ×[0,T), we thus see that D<sub>i</sub> →∞ forces K<sub>i</sub> →∞ and
therefore t<sub>i</sub> → T.

$$
g(0)\in\mathcal{I}
$$

$$
T^{\prime}\in[0,T)
$$

$$
g(t)
$$

$$
M_{k}\times[0,T']
$$

$$
M_{k}\times[0,T)
$$

$$
D_{i}\rightarrow\infty
$$

$$
K_{i}\rightarrow\infty
$$

$$
\bar{t}_{i}\rightarrow T
$$

Consider the rescaled Ricci flows
(

$$
g_{i}(t)=K_{i}g\left(t_{i}+K_{i}^{-1}t\right),\quad t\in[-K_{i}\Delta t_{i},0],
$$

where ∆t<sub>i</sub> > 0 is to be determined below. As K<sub>i</sub> →∞ we see that g<sub>i</sub>(t) are blow-ups
rather than blow-downs, which is important for the following reason: By Theorem
√
7.3 there exists a *κ* > 0 such that *g(t*) is *κ*-non-collapsed *at* every scale *p ≤ T/2*
at every spacetime point (p,t) ∈ M<sub>k</sub> × [T/2,T). As K<sub>i</sub> →∞ we see that g<sub>i</sub>(t) are
*κ*-non-collapsed at scales tending to infinity as *i →∞.*

$$
\Delta t_{i}>0
$$

$$
K_{i}\rightarrow\infty
$$

$$
g_{i}(t)
$$

$$
\kappa>0
$$

$$
g(t)
$$

$$
p\leq\sqrt{T/2}
$$

$$
(p,t)\in M_{k}\times[T/2,T)
$$

$$
K_{i}\rightarrow\infty
$$

$$
g_{i}(t)
$$

$$
i\to\infty
$$

By Lemma 7.9 there exists a *K* > 0 such that
Furthermore, by Lemma 7.10 there exists a *C<sub>0</sub>*
Recall the Definition 2.1 of C<sub>g</sub>(p,r). Set
(

*g(t*) *∈ IK* for all *t ∈* [0,T).
such that |∂<sub>t</sub>b<sup>2</sup>|≤ C<sub>0</sub> on M<sub>k</sub> ×[0,T).
)

$$
g(t)\in\mathcal{I}_K
$$

$$
K>0
$$

$$
t\;\in\;[0,T)
$$

$$
C_{0}
$$

$$
|\partial_{t}b^{2}|\leq C_{0}
$$

$$
C_{g}(p,r)
$$

$$
M_{k}\times[0,T)
$$

$$
\Delta t_{i}=\min\left(\frac{t_{i}}{2},\frac{b^{2}(p_{i},t_{i})}{8C_{0}}\right)
$$

and consider the parabolic neighborhoods
(

$$
\Omega_{i}=C_{g(t_{i})}\left(p_{i},\frac{b(p_{i},t_{i})}{2}\right)\times[t_{i}-\Delta t_{i},t_{i}].
$$

---

As g(t) ∈ IK for t ∈ [0,T) we have that y = b<sub>s</sub> − Q ≤ 0, Q ≤ 1 and b<sub>s</sub> ≥ 0
everywhere on M<sub>k</sub> × [0,T). Therefore

$$
g(t)\in\mathcal{I}_K
$$

$$
t\in[0,T)
$$

$$
y=b_s-Q\leq0,Q\leq1
$$

$$
b_{s}\geq0
$$

$$
M_{k}\times[0,T)
$$

$$
b(p,t_i)\geq\frac{b(p_i,t_i)}{2}on\Omega_i\cap\{t=t_i\}
$$

By Lemma 7.10

$$
b^{2}(p,t_{i})-b^{2}(p,t)\leq C_{0}(t_{i}-t)
$$

for all (p,t) ∈ Ω<sub>i</sub> from which it follows that

$$
(p,t)\in\Omega_i
$$

$$
\frac{1}{4}b(p_{i},t_{i})^{2}-b(p,t)^{2}\leq b^{2}(p,t_{i})-b^{2}(p,t)\leq C_{0}(t_{i}-t)\leq C_{0}\Delta t\leq\frac{1}{8}b(p_{i},t_{i})^{2}.
$$

Thus we deduce that

(7.9)

$$
b^{2}(p,t)\geq\frac{1}{8}b^{2}(p_{i},t_{i})\mathrm{on}\Omega_{i}.
$$

It follows that for (p,t) ∈ Ω<sub>i</sub>

$$
(p,t)\in\Omega_{i}
$$

$$
\begin{aligned}{|R m_{g(t)}|_{g(t)}(p)\leq}&{{}D_{i}b(p,t)^{-2}}\\ {\leq}&{{}8D_{i}b(p_{i},t_{i})^{-2}}\\ {=}&{{}8K_{i}}\\ \end{aligned}
$$

and hence the curvatures of the rescaled metrics g<sub>i</sub>(t) satisfy

$$
g_{i}(t)
$$

$$
\left|{R m}_{g_{i}(t)}\right|_{g_{i}(t)}\leq8
$$

on the parabolic neighborhoods Ω<sup>′i</sup>
(
√

$$
\Omega_{i}^{\prime}
$$

$$
\Omega_{i}^{\prime}:=C_{g_{i}(0)}\left(p_{i},\sqrt{K_{i}}\frac{b(p_{i},t_{i})}{2}\right)\times[-K_{i}\Delta t_{i},0].
$$

Note that

$$
K_{i}\Delta t_{i}\rightarrow\infty as i\rightarrow\infty
$$

and

$$
\sqrt{K_i}\frac{b(p_i,t_i)}{2}\geq\frac{\sqrt{D_i}}{2}\rightarrow\infty\quad as\quad i\rightarrow\infty.
$$

( *√*)
Hence C<sub>g</sub> <sub>(t)</sub>(p<sub>i</sub>, D<sub>i</sub>/2),g<sub>i</sub>(t),p<sub>i</sub>, t ∈ [−K<sub>i</sub>∆t<sub>i</sub>,0], subsequentially converges, in
i
the Cheeger-Gromov sense, to an ancient pointed Ricci flow (*M*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>), *t ∈*
(−∞,0].

$$
\left(C_{g_{i}(t)}(p_{i},\sqrt{D_{i}}/2),g_{i}(t),p_{i}\right),t\in\left[-K_{i}\Delta t_{i},0\right]
$$

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right)
$$

$$
(-\infty,0]
$$

Claim 1: The Ricci flow (M∞,g∞(t),p∞), t ∈ (−∞,0], splits as (R<sup>2</sup> × N,g<sub>eucl</sub> +
g<sub>N</sub>(t)), t ∈ (−∞,0], where g<sub>eucl</sub> is the flat euclidean metric, and (N,g<sub>N</sub>(t)) is a
non-compact ancient Ricci flow.

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right),t\in(-\infty,0]
$$

$$
(\mathbb{R}^{2}\times N,g_{\mathit{eucl}}+
g_{N}(t)),\;t\in(-\infty,0]
$$

$$
g_{e u c l}
$$

$$
\left(N,g_{N}(t)\right)
$$

Proof of Claim: Denote by a<sub>i</sub> and b<sub>i</sub> the warping functions of the rescaled metrics
g<sub>i</sub>(t). Then by (7.9) we see that
√

$$
a_{i}
$$

$$
b_{i}
$$

$$
g_{i}(t)
$$

(7.10)

$$
b_{i}(p,t)\geq\sqrt{\frac{D_{i}}{8}}\operatorname{on}\Omega_{i}^{\prime}
$$

---

As D<sub>i</sub> →∞, the warping functions b<sub>i</sub> tend to infinity uniformly. As b<sub>i</sub> describes the
size of the base *S<sup>2</sup>* in the Hopf fibration,intuitively one can see that this claim is
true. Nevertheless, we provide a formal proof below:

$$
D_{i}\rightarrow\infty
$$

$$
b_{i}
$$

$$
b_{i}
$$

$$
S^{2}
$$

As *g(t*) *∈IK* for *t ∈* [0,T) we have
∣ ∣
∣ ∣

$$
t\in[0,T)
$$

$$
g(t)\in\mathcal{I}_{K}
$$

$$
\left|-\frac{b_{ss}}{b}\right|\leq\frac{K}{b^2}\quad on\quad M_k\times[0,T).
$$