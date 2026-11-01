---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Gluing Construction of Einstein Manifolds]

Lemma 20. Let (Mm,∂M,x,g) be an AH manifold and let h be a symmetric two tensor
_defined in neighborhood of the boundary. Then there exist a one-form α defined in_
neighborhood of the boundary such that s = h + δ∗α is in radial gauge (i.e. ∂xys = 0).
Furthermore, if \|h\|g = o(xm−1), then α can be chosen to satisfy \|α\|g = o(xm−1) as x → 0.
_Proof._ Using the boundary defining function _x,_ we identify a neighborhood of the boundary with \[0,)× ∂M. Fix any point (0,p) ∈ \[0,)× ∂M. We specify a local orthonormal\
frame on a slice as follows: choose {e0,...,em−1} at (0,q), for q near p so that e0 is\
normal to the slice {0}× ∂M, and {e1,...,em−1} is an local orthonormal frame on the\
\
$$\
\\left(M^{m},\\partial M,x,g\\right)\
$$\
\
$$\
s=h+\\delta^{\*}\\alpha\
$$\
\
$$\
\\partial\_{x}\\lrcorner s=0)\
$$\
\
$$\
\\mathrm{if}\\left\|h\\right\|\_{g}=o\\left(x^{m-1}\\right)\
$$\
\
$$\
\|\\alpha\|\_{g}=o(x^{m-1})\
$$\
\
$$\
x\\to0\
$$\
\
$$\
\\left\[0,\\epsilon\\right)\\times\\partial M\
$$\
\
$$\
\\left(\\epsilon\_{0},p\\right)\\in\\left\[0,\\epsilon\\right)\\times\\partial M\
$$\
\
$$\
{e\_{0},\\ldots,e\_{m-1}}\
$$\
\
$$\
\\left(\\epsilon\_{0},q\\right)\
$$\
\
$$\
e\_{0}\
$$\
\
$$\
{\\epsilon\_{0}}\\times\\partial M\
$$\
\
$$\
{e\_{1},...,e\_{m-1}}\
$$ tangent space of the slice {0}× ∂M. Extend this locally by parallel transport along\
integral curves of _e0_ to an orthonormal frame in a neighborhood of the chosen point.\
Let {e0,...,em−1} denote the dual frame.\
\
$$\
{\\epsilon\_{0}}\\times\\partial M\
$$\
\
$$\
e\_{0}\
$$\
\
$$\
{e^{0},\\ldots,e^{m-1}}\
$$\
\
This frame has the following property\
\
$$\
\\nabla\_{e\_{0}}e^{i}=0\
$$\
\
(7.1)\
\
for _i ∈{0,...,m −_ 1}. Next, we write _h_ in the above frame as follows\
\
$$\
i\\in{0,...,m-1}\
$$\
\
$$\
h=\\sum\_{i=1}^{m-1}h\_{0i}(e^{0}\\otimes e^{i}+e^{i}\\otimes e^{0})+\\sum\_{i,j=1}^{m-1}h\_{i j}(e^{i}\\otimes e^{j}+e^{j}\\otimes e^{i})+h\_{00}e^{0}\\otimes e^{0},\
$$\
\
where h00,h0i,hij are functions defined near the chosen point. Next, for a 1-form of the\
∑m−1\
form α = α0iei, we compute\
i=0\
\
(7.2)\
\
$$\
h\_{00},h\_{0i},h\_{i j}\
$$\
\
$$\
\\alpha=\\sum\_{i=0}^{m-1}\\alpha\_{0i}e^{i}\
$$\
\
$$\
\\nabla\\left(\\alpha\_{0i}e^{i}\\right)=d\\alpha\_{0i}\\otimes e^{i}+\\alpha\_{0i}\\omega\_{i j}\\otimes e^{j}\
$$\
\
(7.3)\
\
$$\
\\delta^{\*}\\alpha=\\frac{1}{2}\\Big(d\\alpha\_{0i}\\odot e^{i}+\\alpha\_{0i}\\omega\_{i j}\\odot e^{j}\\Big).\
$$\
\
(7.4)\
\
We obtain\
\
$$\
\\begin{align\*}e\_{0}\\lrcorner(\\delta^{ _}\\alpha)&=\\frac{1}{2}\\Big(d\\alpha\_{0i}(e\_{0})e^{i}+d\\alpha\_{00}+\\alpha\_{0i}\\omega\_{ij}(e\_{0})e^{j}+\\alpha\_{0i}\\omega\_{i0}\\Big)\\&=\\frac{1}{2}\\Big((d\\alpha\_{0i}(e\_{0}))e^{i}+d\\alpha\_{00}+\\alpha\_{0i}\\omega\_{i0}\\Big),\\end{align_}\
$$\
\
(7.5)\
\
where ωij are the connection 1-forms satisfying\
We also have\
\
∇ej = ωji\
\
⊗ ei, and we also used (7.1).\
\
$$\
\\omega\_{ij}\
$$\
\
$$\
\\nabla e^{j}=\\omega\_{ji}\\otimes e^{i}\
$$\
\
$$\
e\_{0}\\lrcorner h=\\sum\_{i=1}^{m-1}h\_{0i}e^{i}+h\_{00}e^{0}.\
$$\
\
(7.6)\
\
Choosing α00 to be a radial function, we first solve the equation dα0i(e0) = h0i for\
functions α0i when i ≥ 1, which we can solve by integrating along integral curves of e0.\
Then we solve the equation 2 ˙α00 \+ α0iωi0 = h00 for α00. This defines α only locally but\
\
$$\
\\alpha\_{00}\
$$\
\
$$\
d\\alpha\_{0i}(e\_{0})=h\_{0i}\
$$\
\
$$\
\\alpha\_{0i}\
$$\
\
$$\
i\\geq1\
$$\
\
$$\
e\_{0}\
$$\
\
$$\
2\\dot{\\alpha} _{00}+\\alpha_{0i}\\omega\_{i0}=h\_{00}\
$$\
\
$$\
\\alpha\_{00}\
$$ we can extend it to a global form in neighborhood of the boundary by using a partition\
of unity argument. The statement about decay rates follows easily.\
\
We also need the following analytic continuation result for analytic Riemannian manifolds.\
\
Lemma 21. Let (Mm,∂M,g,x) be AHE and let P(s) = 0 in some open set V ⊂ M\
such that s = δ∗α for some one-form α defined in some open ball U ⊂ V then α can\
_be analytically continued to a vector field α˜ defined on any simply connected domain_\
U⊂U1 ⊂ V such that s = δ∗α˜. Furthermore, if V contains a punctured ball around p0,\
and s = O(\|z\|γ) for γ 6= −1 where \|z\| is distance to the point p0, then α˜ = O(\|z\|γ+1) as\
_\|z\|→ 0._\
\
$$\
\\left(M^{m},\\partial M,g,x\\right)\
$$\
\
$$\
P(s)=0\
$$\
\
$$\
V\\subset M\
$$\
\
$$\
s=\\delta^{\*}\\alpha\
$$\
\
$$\
U\\subset V\
$$\
\
$$\
U\\subset U\_{1}\\subset V\
$$\
\
$$\
s=\\delta^{\*}\\tilde{\\alpha}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
s=O(\|z\|^{\\gamma})\
$$\
\
$$\
\\gamma\\neq-1\
$$\
\
$$\
\\left\|z\\right\|\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\tilde{\\alpha}=O(\|z\|^{\\gamma+1})\
$$\
\
$$\
\|z\|\\to0\
$$\
\
_Proof._ Since Einstein metrics are real analytic in harmonic coordinates one can use\
the infinitesimal version of analytic continuation technique (see \[18, Corollary 6.4\]) to\
extend _α_ to a larger domain. We refer to \[2, Lemma 2.6\] for a complete proof. Finally,\
an examination of the proof shows that the solution is obtained by integration, and the\
last statement follows from this (the details are omitted).\
\
Another crucial result we will need is the following unique continuation theorem due\
to Biquard.\
\
Theorem 22 (Biquard \[9\]). Let (Mm,∂M,g,x) be AHE. If h ∈ Γ(S2(T ∗U)), where U\
is a neighborhood of ∂M, is a solution of dgRic(h) = Λh, and h is in radial gauge (i.e\
∂xyh = 0), such that \|h\|g = o(xm−1) as x → 0, then h ≡ 0.\
\
$$\
\\left(M^{m},\\partial M,g,x\\right)\
$$\
\
$$\
h\\in\\Gamma(S^{2}(T^{\*}U))\
$$\
\
$$\
d\_{g}Ric(h)=\\Lambda h\
$$\
\
$$\
\\partial\_{x}\\lrcorner h=0\
$$\
\
$$\
\|h\|\_{g}=o(x^{m-1})\
$$\
\
$$\
x\\to0\
$$\
\
$$\
h\\equiv0\
$$\
\
We next define a mapping on 0-germs\
\
$$\
S\_{0}^{\\infty}:S\_{0}^{2}(T\_{p\_{0}}^{\*}M\_{0})\\rightarrow V\_{0},\
$$\
\
(7.7)\
\
* * *\
\
where V0 was defined in (6.4). Given a traceless symmetric matrix aij, then there is a\
˜ ˜) = 0 satisfying\
unique solution h ∈ Γ(S02(T ∗M0)) of P (h\
\
$$\
V\_{0}\
$$\
\
$$\
a\_{ij}\
$$\
\
$$\
\\tilde{h}\\in\\Gamma(S\_{0}^{2}(T^{\*}M\_{0}))\
$$\
\
$$\
P(\\tilde{h})=0\
$$\
\
$$\
\\tilde{h}=\\frac{a\_{i j}}{\|z\|^{m-2}}d z^{i}\\odot d z^{j}+O\\big(\|z\|^{3-m}\\big)\
$$\
\
(7.8)\
\
˜\
as _\|z\| →_ 0, and such that _h ∈ L2(M0 \ B(p0,))._ The solution is unique since _M0_ is\
˜ admits an expansion\
assumed to be non-degenerate. From Proposition 6.1, _h_\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{h}\\in L^{2}\\left(M\_{0}\\setminus B(p\_{0},\\epsilon)\\right)\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
\\tilde{h}=\\sigma\_{0}x^{m-1}+o(x^{m-1}),\
$$\
\
(7.9)\
\
˜ is unique, the mapping\
with x2σ0 ∈ V 0, as x → 0. Since h\
\
$$\
x^{2}\\sigma\_{0}\\in\\overline{V}\_{0}\
$$\
\
$$\
x\\to0\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
S\_{0}^{\\infty}\\left(a\_{i j}d z^{i}\\odot d z^{j}\\right)\\equiv x^{2}\\sigma\_{0}\| _{\\partial M_{0}}\
$$\
\
(7.10)\
\
is well-defined. Next, let _E0_ = _Im(S0∞)._ In a similar fashion we can define a mapping\
on 1-germs\
\
$$\
E\_{0}=Im(S\_{0}^{\\infty})\
$$\
\
$$\
S\_{\\underline{{1}}}^{\\infty}:F\_{1}\\otimes S\_{\\underline{{0}}}^{2}(T\_{p\_{0}}^{\*}M\_{0})\\rightarrow E\_{0}^{\\perp}\\subset V\_{0},\
$$\
\
(7.11)\
\
with respect to the _L2_ inner product on _∂M0,_ defined by the following. Given\
\
$$\
L^{2}\
$$\
\
$$\
\\partial M\_{0}\
$$\
\
$$\
a\_{ijk}z^i dz^j\\odot dz^k\\in F\_1\\otimes S\_0^2(T\_{p\_0}^\*M\_0)\
$$\
\
(7.12)\
\
˜\
then there is a solution h ∈ Γ(S02(T ∗M0)) of P (\
\
˜) = 0 satisfying\
_h_\
\
$$\
\\tilde{h}\\in\\Gamma(S\_{0}^{2}(T^{\*}M\_{0}))\
$$\
\
$$\
P(\\tilde{h})=0\
$$\
\
$$\
\\tilde{h}=\\frac{a\_{i j k}z^{i}}{\|z\|^{m}}d z^{j}\\odot d z^{k}+O(\|z\|^{2-m})\
$$\
\
(7.13)\
\
˜\
as _\|z\|→_ 0, and such that _h ∈ L2(M0 \ B(p0,))._ Again, from Proposition 6.1 there is\
an expansion\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{h}\\in L^{2}\\left(M\_{0}\\setminus B\\left(p\_{0},\\epsilon\\right)\\right)\
$$\
\
$$\
\\tilde{h}=\\sigma\_{0}x^{m-1}+o(x^{m-1}),\
$$\
\
(7.14)\
\
* * *\
\
˜ is only unique up to the solutions from the∞\
where x2σ0 ∈ V 0, as x → 0. Since h S0\
construction above, the mapping\
\
$$\
x\\to0\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
x^{2}\\sigma\_{0}\\in\\overline{V}\_{0}\
$$\
\
$$\
S\_{0}^{\\infty}\
$$\
\
$$\
S\_{1}^{\\infty}\\big(a\_{i j k}z^{i}d z^{j}\\odot d z^{k}\\big)=x^{2}\\sigma\_{0}\| _{\\partial M_{0}}\
$$\
\
(7.15)\
\
is well-defined modulo the image of _S0∞_ and therefore gives a well-defined mapping to\
⊥ ∞\
_E0._ Letting _E1_ = _Im(S1),_ in a similar fashion, we may define a mapping on 2-germs\
\
$$\
S\_{0}^{\\infty}\
$$\
\
$$\
E\_{0}^{\\perp}\
$$\
\
$$\
E\_{1}=Im(S\_{1}^{\\infty})\
$$\
\
$$\
S\_{2}^{\\infty}:S\_{0}^{2}(\\mathbb{R}^{m})\\otimes S\_{0}^{2}(T\_{p\_{0}}^{\*}M\_{0})\\to(E\_{0}\\oplus E\_{1})^{\\perp}.\
$$\
\
(7.16)\
\
$$\
a\_{i j k l}z^{i}z^{j}d z^{k}\\odot d z^{l}\\in F\_{2}\\otimes S\_{0}^{2}(T\_{p\_{0}}^{\*}M\_{0}),\
$$\
\
by the following. Given\
\
(7.17)\
\
˜\
then there is a solution h ∈ Γ(S02(T ∗M0\
\
˜) = 0 satisfying\
_h_\
\
$$\
\\tilde{h}\\in\\Gamma(S\_{0}^{2}(T^{\*}M\_{0}))\
$$\
\
$$\
P(\\tilde{h})=0\
$$\
\
$$\
\\tilde{h}=\\frac{a\_{i j k l}z^{i}z^{j}}{\|z\|^{m+2}}d z^{k}\\odot d z^{l}+O(\|z\|^{1-m})\
$$\
\
(7.18)\
\
˜\
as _\|z\|→_ 0, and such that _h ∈ L2(M0 \ B(p0,))._ Again, from Proposition 6.1 there is\
an expansion\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{h}\\in L^{2}\\left(M\_{0}\\setminus B\\left(p\_{0},\\epsilon\\right)\\right)\
$$\
\
$$\
\\tilde{h}=\\sigma\_{0}x^{m-1}+o(x^{m-1}),\
$$\
\
(7.19)\
\
˜ is only unique up to the solutions from the∞\
where _x2σ0 ∈ V0_ as _x →_ 0\. Since _h S0_ and\
_S1∞_ constructions above, the mapping\
\
$$\
x^{2}\\sigma\_{0}\\in\\overline{V}\_{0}\
$$\
\
$$\
x\\to0\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
S\_{0}^{\\infty}\
$$\
\
$$\
S\_{1}^{\\infty}\
$$\
\
$$\
S\_{2}^{\\infty}(a\_{i j k l})=x^{2}\\sigma\_{0}\| _{\\partial M_{0}}\
$$\
\
(7.20)\
\
is well-defined modulo the image of _S0∞_ and _S1∞_ and therefore gives a well-defined mapping to ( _E0 ⊕ E1)⊥._\
\
$$\
S\_{0}^{\\infty}\
$$\
\
$$\
S\_{1}^{\\infty}\
$$\
\
$$\
(E\_{0}\\oplus E\_{1})^{\\perp}\
$$\
\
* * *\
\
Proposition 7.1. Let (M0m,∂M0,g,x) be an AHE orbifold with one singular point p0\
of type Γn(m = 2n) and non-degenerate. Then we have the following:\
\
$$\
\\left(M\_{0}^{m},\\partial M\_{0},g,x\\right)\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\Gamma\_{n}(m=2n)\
$$\
\
_1\. S0∞ is injective._\
\
$$\
S\_{0}^{\\infty}\
$$\
\
_2\. S1∞ is injective._\
\
$$\
S\_{1}^{\\infty}\
$$\
\
∞ α1\
3\. The kernel of S2 is the space of 2-germs of the form \|z\|m+2Keuc(m), where α1 is\
\|z\|\
_a one-form with linear coefficients._\
\
$$\
S\_{2}^{\\infty}\
$$\
\
$$\
\|z\|^{m+2}\\mathcal{K}\_{euc}(\\frac{\\alpha\_1}{\|z\|^m})\
$$\
\
$$\
\\alpha\_{1}\
$$\
\
_Proof._ In any of these cases, let _s_ be the solution from the above construction which\
is blowing up at the point, and _L2_ in a neighborhood of infinity, so that top _L2_ weight\
vanishes. By Proposition 6.1, _s_ admits an expansion\
\
$$\
L^{2}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
s=\\sigma\_{1}x^{m}+o(x^{m})\
$$\
\
(7.21)\
\
where x2σ1 ∈ V 1, as x → 0. A straightforward calculation shows that Bs = o(xm) as\
_x →_ 0\. By Lemma 18, _P1(Bs_) = 0, so by Proposition 6.1, we must have\
\
$$\
x^{2}\\sigma\_{1}\\in\\overline{V}\_{1}\
$$\
\
$$\
x\\to0\
$$\
\
$$\
Bs=o(x^m)\
$$\
\
$$\
x\\to0\
$$\
\
$$\
P\_{1}(Bs)=0\
$$\
\
$$\
B s=\\alpha\_{n}x^{\\delta\_{1,P\_{1}}^{+}}+o(x^{\\delta\_{1,P\_{1}}^{+}})\
$$\
\
(7.22)\
\
where αn ∈ Ω1nM0\
the fact that δ1+,P\
1\
\
∣\
∣, as _x →_ 0\. Then, again by the Lemma 18 and Proposition 6.1 and\
\
> δ1+,P2, we have that dBs ≡ 0. We need the following lemma.\
\
$$\
\\alpha\_{n}\\in\\left.\\Omega\_{n}^{1}\\overline{M\_{0}}\\right\[\
$$\
\
$$\
x\\to0\
$$\
\
$$\
\\delta\_{1,P\_{1}}^{+}>\\delta\_{1,P\_{2}}^{+}\
$$\
\
$$\
d B s\\equiv0\
$$\
\
Lemma 23. _The function f_ = _δBs satisfies_\
\
$$\
f=\\delta B s\
$$\
\
$$\
B s=\\frac{1}{\\Lambda}d f,\
$$\
\
(7.23)\
\
$$\
P\_{0}(f)=0.\
$$\
\
(7.24)\
\
* * *\
\
Proof. Since trgs = 0 and dBs = 0, using Lemma 18, we have\
\
$$\
tr\_{g}s=0\
$$\
\
$$\
dBs=0\
$$\
\
$$\
d f=d\\delta\\delta s=(\\Delta\_{H}-\\delta d)\\delta s=\\Lambda\\delta s-\\delta d\\delta s=\\Lambda\\delta s,\
$$\
\
(7.25)\
\
and (7.23) follows. Lemma 18 directly implies (7.24) since _Ps_ = 0.\
\
$$\
Ps=0.\
$$\
\
˜ =2f\
Letting f (2−m)Λ, from Lemma 23, we have that\
\
$$\
\\tilde{f}=\\frac{2f}{(2-m)\\Lambda}\
$$\
\
$$\
P(s+\\tilde{f}g)=0,\
$$\
\
(7.26)\
\
$$\
B(s+\\tilde{f}g)=0.\
$$\
\
(7.27)\
\
Consequently,\
\
$$\
d\_{g}R i c(s+\\tilde{f}g)=\\Lambda(s+\\tilde{f}g),\
$$\
\
(7.28)\
\
$$\
s+\\tilde{f}g=o(x^{m-1}),\
$$\
\
(7.29)\
\
as _x →_ 0.\
\
$$\
x\\to0.\
$$\
\
Then by Theorem 22 and Lemma 20 it follows that\
\
$$\
s+\\tilde{f}g=\\delta^\*(\\alpha)\
$$\
\
(7.30)\
\
for some one-form _α_ defined in a neighborhood of the boundary. Since _(M0,g)_ is a noncompact and complete Riemannian manifold there exists a geodesic ray _γ_ starting from\
_p0_ to infinity. Now applying Lemma 21 inductively on _γ_ we can analytically continue _α_\
to a one-form _˜α_ defined in a neighborhood of _γ_ such that\
\
$$\
\\alpha\
$$\
\
$$\
(M\_{0},g)\
$$\
\
$$\
\\gamma\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\gamma\
$$\
\
$$\
\\tilde{\\alpha}\
$$\
\
$$\
\\gamma\
$$\
\
$$\
s+\\tilde{f}g=\\delta^\*(\\tilde{\\alpha}).\
$$\
\
(7.31)\
\
Equivalently,\
\
$$\
s=\\mathcal{K}\\left(\\tilde{\\alpha}\\right),\
$$\
\
(7.32)\
\
* * *\
\
for a 1-form _˜α_ satisfying\
\
$$\
\\tilde{\\alpha}\
$$\
\
$$\
P\_{1}(\\tilde{\\alpha})=0.\
$$\
\
(7.33)\
\
∞\
In the case of S0, let s be the solution of Ps = 0 whose leading term is \|z\|2−mh0 at\
the point, where h0 is a 0-germ at p0, and s = o(xm−1) as x → 0. Since s = O(\|z\|−m+2)\
around p0 and (7.32) is satisfied, by Lemma 21, ˜α = O(\|z\|−m+3). The Bochner formula\
implies that there is no nontrivial _L2_ kernel for _P1._ Since _P1α˜_ = 0, this implies that\
_α˜_ = 0 by a standard removable singularity theorem for solutions of _P1,_ and therefore\
_h0_ = 0.\
\
$$\
S\_{0}^{\\infty}\
$$\
\
$$\
Ps=0\
$$\
\
$$\
\|z\|^{2-m}h\_0\
$$\
\
$$\
h\_{0}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
s=o(x^{m-1})\
$$\
\
$$\
x\\to0\
$$\
\
$$\
s=O(\|z\|^{-m+2})\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\tilde{\\alpha}=O(\|z\|^{-m+3})\
$$\
\
$$\
L^{2}\
$$\
\
$$\
P\_{1}\
$$\
\
$$\
P\_{1}\\tilde{\\alpha}=0\
$$\
\
$$\
\\tilde{\\alpha}=0\
$$\
\
$$\
h\_{0}=0\
$$\
\
$$\
P\_{1}\
$$\
\
∞\
In case of _S1,_ given any 1-germ _h1_ at _p0_ let _s_ be the solution of _Ps_ = 0 whose leading\
⊥ ∞\
term is \|z\|−mh1 at p0, and x2s\|∂M0∈ E0. If h1 ∈ Ker(S1) then s = o(xm−1) as x → 0.\
Since s = O(\|z\|−m+1) as \|z\|→ 0 and (7.32) is satisfied, by Lemma 21, α˜ = O(\|z\|−m+2).\
This implies that _˜α_ = 0 by the removable singularity theorem, since there is no solution\
with that leading term which is also invariant under group action, and therefore _h1_ = 0.\
\
$$\
S\_{1}^{\\infty}\
$$\
\
$$\
h\_{1}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
Ps=0\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\|z\|^{-m}h\_1\
$$\
\
$$\
x^{2}s\| _{\\partial M_{0}}\\in E\_{0}^{\\perp}\
$$\
\
$$\
h\_{1}\\in K e r(S\_{1}^{\\infty})\
$$\
\
$$\
s=o(x^{m-1})\
$$\
\
$$\
x\\to0\
$$\
\
$$\
s=O(\|z\|^{-m+1})\
$$\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{\\alpha}=O(\|z\|^{-m+2})\
$$\
\
$$\
\\tilde{\\alpha}=0\
$$\
\
$$\
h\_{1}=0\
$$\
\
∞\
In case of _S2,_ given any 2-germ _h2_ at _p0_ let _s_ be the solution of _Ps_ = 0 whose\
⊥ ∞\
leading term is \|z\|−m−2h2 at p0, and x2s\|∂M0∈ (E0 ⊕ E1). If h2 ∈ Ker(S2) then\
s = o(xm−1) as x → 0. Since s = O(\|z\|−m+1) as \|z\| → 0 and (7.32) is satisfied by\
Lemma 21, ˜α = O(\|z\|−m+2). This implies that\
\
$$\
h\_{2}\
$$\
\
$$\
S\_{2}^{\\infty}\
$$\
\
$$\
Ps=0\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\|z\|^{-m-2}h\_2\
$$\
\
$$\
x^{2}s\| _{\\partial M_{0}}\\in(E\_{0}\\oplus E\_{1})^{\\perp}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
h\_{2}\\in Ker(S\_{2}^{\\infty})\
$$\
\
$$\
s=o(x^{m-1})\
$$\
\
$$\
x\\to0\
$$\
\
$$\
s=O(\|z\|^{-m+1})\
$$\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{\\alpha}=O\\big(\|z\|^{-m+2}\\big)\
$$\
\
$$\
\\tilde{\\alpha}=\\frac{\\alpha\_{1}}{\|z\|^{m}}+O(\|z\|^{-m+2}),\
$$\
\
(7.34)\
\
where _α1_ is a one-form with linear coefficients. Then we have\
\
$$\
\\alpha\_{1}\
$$\
\
$$\
s=\\mathcal{K}(\\tilde{\\alpha})=\\mathcal{K} _{e u c}\\left(\\frac{\\alpha_{1}}{\|z\|^{m}}\\right)+O(\|z\|^{-m+1})\
$$\
\
(7.35)\
\
as _\|z\| →_ 0\. For the converse, since there is no nontrivial\
linear form α1 = aijzidzj, there exists a unique solution\
\
_α1˜_\
\
_L2_ kernel for _P1,_ given a\
of _P1(˜α1_) = 0 which is in\
\
$$\
\|z\|\\to0\
$$\
\
$$\
L^{2}\
$$\
\
$$\
P\_{1}\
$$\
\
$$\
\\alpha\_{1}=a\_{ij}z^{i}dz^{j}\
$$\
\
$$\
\\tilde{\\alpha}\_{1}\
$$\
\
$$\
P\_{1}(\\tilde{\\alpha}\_{1})=0\
$$\
\
* * *\
\
_L2(M0 \ B(p0,_)) satisfying\
\
$$\
L^{2}(M\_{0}\\setminus B(p\_{0},\\epsilon))\
$$\
\
$$\
\\tilde{\\alpha} _{1}=\|z\|^{2-m}a_{i j}z^{i}d z^{j}+O\\big(\|z\|^{2-m}\\big),\
$$\
\
(7.36)\
\
as _\|z\|→_ 0\. By Proposition 6.1, _˜α1_ admits an expansion\
\
$$\
\|z\|\\to0\
$$\
\
$$\
\\tilde{\\alpha}\_{1}\
$$\
\
$$\
\\tilde{\\alpha} _{1}=\\alpha_{t}x^{\\delta\_{0,P\_{1}}^{+}}+o(x^{\\delta\_{0,P\_{1}}^{+}}),\
$$\
\
(7.37)\
\
where xαt ∈ Ω1t M0, as x → 0. From Proposition 18, it follows easily that h = Kα1˜ is a\
α1 ∞\
solution of Ph = 0, and thus the 2-germ \|z\|m+2Keuc(m), is in the kernel of S2, where\
\|z\|\
_α1_ is any one-form with linear coefficients.\
\
$$\
x\\alpha\_{t}\\in\\Omega\_{t}^{1}\\overline{{M\_{0}}}\
$$\
\
$$\
x\\to0\
$$\
\
$$\
\\mathit{h}=\\mathcal{K}\\tilde{\\alpha}\_1\
$$\
\
$$\
Ph=0\
$$\
\
$$\
\|z\|^{m+2}\\mathcal{K}\_{euc}(\\frac{\\alpha\_1}{\|z\|^m})\
$$\
\
$$\
S\_{2}^{\\infty}\
$$\
\
$$\
\\alpha\_{1}\
$$\
\
* * *\
\
# From boundary tensors to germs\
\
The following lemma describes a “duality” between boundary tensors and germs. We\
state the following\
\
Lemma 24. Let (Mm,∂M,g,x) be AH with one orbifold point p0 of type Γn. Let σk,τk _be k-germs at p0 and Let s and t be two solutions for P such that_\
\
$$\
\\left(M^{m},\\partial M,g,x\\right)\
$$\
\
$$\
\\Gamma\_{n}\
$$\
\
$$\
\\sigma\_{k},\\tau\_{k}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\begin{align\*}s&=\\sigma\_k\|z\|^{2-m-2k}+o\\big(z^{2-m-k}\\big);\\mathit{as};\|z\|\\rightarrow0,\\s&=\\sigma\_{\\infty}x^{\\delta\_{0,P}^+}+o\\big(x^{\\delta\_{0,P}^+}\\big);\\mathit{as};x\\rightarrow0,\\end{align\*}\
$$\
\
(8.1)\
\
where x2σ∞∈ V 0, and\
\
$$\
x^{2}\\sigma\_{\\infty}\\in\\overline{V}\_{0}\
$$\
\
$$\
\\begin{align\*}t&=\\tau\_k+o(\|z\|^k)\\quad\\mathit{as}\|z\|\\rightarrow0\\t&=\\tau\_{\\infty}x^{\\delta\_{0,P}^{-}}+o(x^{\\delta\_{0,P}^{-}})\\quad\\mathit{as}x\\rightarrow0,\\end{align\*}\
$$\
\
(8.2)\
\
where x2τ∞∈ V 0. For k = 0 we have\
\
$$\
x^{2}\\tau\_{\\infty}\\in\\overline{V}\_{0}\
$$\
\
$$\
(m-2)\\frac{\\omega\_{m-1}}{n}\\langle\\langle\\sigma\_{0},\\tau\_{0}\\rangle\\rangle=(m-1)\\langle x^{2}\\sigma\_{\\infty},x^{2}\\tau\_{\\infty}\\rangle,\
$$\
\
(8.3)\
\
_for k_ = 1 _we have_\
\
(8.4)\
\
$$\
\\frac{\\omega\_{m-1}}{n}\\big\\langle\\big\\langle\\sigma\_{1},\\tau\_{1}\\big\\rangle\\big\\rangle=\\big(m-1\\big)\\big\\langle x^{2}\\sigma\_{\\infty},x^{2}\\tau\_{\\infty}\\big\\rangle,\
$$\
\
_and for k_ = 2 _we have_\
\
$$\
\\frac{2\\omega\_{m-1}}{m n}\\big\\langle\\big\\langle\\sigma\_{2},\\tau\_{2}\\big\\rangle\\big\\rangle=(m-1)\\big\\langle x^{2}\\sigma\_{\\infty},x^{2}\\tau\_{\\infty}\\big\\rangle,\
$$\
\
(8.5)\
\
* * *\
\
_where the left inner product is the germ inner product at p0 (see the proof for the definition), and the right inner product is the L2 inner product on the boundary._\
\
$$\
p\_{0}\
$$\
\
$$\
L^{2}\
$$\
\
(\
Proof. Let M0, = M0 \ B(p0,) ∪ ∂M0 × \[0,\
that\
\
)\
) . Integrating by parts on M0, implies\
\
$$\
M\_{0,\\epsilon}=\\overline{{M}} _{0}\\setminus\\left(B(p_{0},\\epsilon)\\cup\\partial M\_{0}\\times\[0,\\epsilon)\\right)\
$$\
\
$$\
M\_{0,\\epsilon}\
$$\
\
$$\
\\int\_{M\_{0,\\epsilon}}(\\langle P s,t\\rangle-\\langle s,P t\\rangle)d V\_{g}=\\int\_{\\partial M\_{0,\\epsilon}}(\\langle-\\nabla\_{\\vec{n}}s,t\\rangle+\\langle s,\\nabla\_{\\vec{n}}t\\rangle)d S\_{g}.\
$$\
\
(8.6)\
\
The interior boundary integral is given by\
\
$$\
\\operatorname\*{l i m} _{\\epsilon\\to0}\\int_{\\partial B(p\_{0},\\epsilon)}(\\langle-\\nabla\_{\\vec{n}}s,t\\rangle+\\langle s,\\nabla\_{\\vec{n}}t\\rangle)d S\_{g}=(2-m-2k)\\int\_{S^{m-1}/\\Gamma\_{n}}\\langle\\sigma\_{k},\\tau\_{k}\\rangle d S\_{e u c},\
$$\
\
(8.7)\
\
where the inner product denotes contraction on only the indices of the germs corresponding to S02(Tp∗0(M0)).\
\
$$\
S\_{0}^{2}(T\_{p\_{0}}^{\*}(M\_{0}))\
$$\
\
Recall from Proposition 6.1 that δ0+,P =\
_√_\
x1−m detg when we restrict both metrics to\
ary integral is given by\
\
_√_\
m − 1 and δ0−,P = 0\. Since detg =\
_∂M0×{ },_ it follows that the outer bound-\
\
$$\
\\delta\_{0,P}^{+}=m-1\
$$\
\
$$\
\\delta\_{0,P}^{-};=;0\
$$\
\
$$\
\\sqrt{\\det\\bar{g}}=\
x^{1-m}\\sqrt{\\det g}\
$$\
\
$$\
\\partial M\_{0}\\times{\\epsilon}\
$$\
\
$$\
\\operatorname\*{l i m} _{\\epsilon\\to0}\\int_{\\partial M\_{0}\\times{\\epsilon}}(\\langle-\\nabla\_{\\vec{n}}s,t\\rangle+\\langle s,\\nabla\_{\\vec{n}}t\\rangle)d S\_{g}=(m-1)\\int\_{\\partial M\_{0}}\\langle x^{2}\\sigma\_{\\infty},x^{2}\\tau\_{\\infty}\\rangle d S\_{g\_{\\infty}}.\
$$\
\
(8.8)\
\
If _k_ = 0 then then working in a coordinate chart around\
\
p0 with gij(p0) = δij we have\
\
$$\
p\_{0}\
$$\
\
$$\
k=0\
$$\
\
$$\
g\_{ij}(p\_0)=\\delta\_{ij}\
$$\
\
$$\
\\sigma\_{0}=H\_{k l}d z^{k}\\otimes d z^{l},\
$$\
\
(8.9)\
\
$$\
\\tau\_{0}=K\_{k l}d z^{k}\\otimes d z^{l},\
$$\
\
(8.10)\
\
and (8.3) follows immediately, with _〈〈σ0,τ0〉〉_ =\
\
∑\
k,l HklKkl.\
\
$$\
\\left\\langle\\left\\langle\\sigma\_{0},\\tau\_{0}\\right\\rangle\\right\\rangle=\\sum\_{k,l}H\_{k l}K\_{k l}.\
$$\
\
If _k_ = 1, then\
\
$$\
\\sigma\_{1}=H\_{j k l}z^{j}d z^{k}\\otimes d z^{l},\
$$\
\
(8.11)\
\
$$\
\\tau\_{1}=K\_{j k l}z^{j}d z^{k}\\otimes d z^{l},\
$$\
\
(8.12)\
\
* * *\
\
∑\
and (8.4) follows from (3.22) with _〈〈σ1,τ1〉〉_ =\
\
j,k,l HjklKjkl.\
\
$$\
\\left\\langle\\left\\langle\\sigma\_{1},\\tau\_{1}\\right\\rangle\\right\\rangle=\\sum\_{j,k,l}H\_{jkl}K\_{jkl}.\
$$\
\
Finally, if _k_ = 2, then\
\
$$\
k=2\
$$\
\
$$\
\\sigma\_{2}=H\_{i j k l}z^{i}z^{j}d z^{k}\\otimes d z^{l},\
$$\
\
(8.13)\
\
$$\
\\tau\_{2}=K\_{i j k l}z^{i}z^{j}d z^{k}\\otimes d z^{l},\
$$\
\
(8.14)\
\
∑\
and (8.5) follows from (3.23) with _〈〈σ2,τ2〉〉_ =\
\
i,j,k,l HijklKijkl.\
\
$$\
\\left\\langle\\left\\langle\\sigma\_{2},\\tau\_{2}\\right\\rangle\\right\\rangle=\\sum\_{i,j,k,l}H\_{i j k l}K\_{i j k l}.\
$$\
\
Next, we explain how to construct a map which sends boundary tensors to germs\
at _p0._ Identify a neighborhood of the boundary with _∂M0 ×_ \[0,). Let _ϕ_ be a cutoff\
()\
function which is 1 on ∂M0 × \[0, 2) and is zero on M0 \ ∂M0 × \[0,) . Given σ0 ∈ V0,\
consider the tensor ϕx−2σ0. By solving a finite number of terms of a power series, we\
can then find s of the form s = ϕx−2σ0 \+ ˜s, where ˜s are lower order terms supported in a\
neighborhood of the boundary, such that _Ps_ is in _L2_ in a neighborhood of the boundary.\
(For this power series method, see for example \[4\] for the Hodge Laplacian acting on\
forms; the same technique applies to solutions of P.) Then, using the non-degeneracy\
assumption, we can find a solution of _Ps_ = 0 defined on all of _M0,_ which is in _L2_ on any\
compact subset of _M0,_ so that\
\
$$\
\\partial M\_{0}\\times\[0,\\epsilon)\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\varphi\
$$\
\
$$\
\\partial M\_{0}\\times\[0,{\\frac{\\epsilon}{2}})\
$$\
\
$$\
M\_{0}\\setminus\\big(\\partial M\_{0}\\times\[0,\\epsilon)\\big)\
$$\
\
$$\
\\sigma\_{0}\\in V\_{0}\
$$\
\
$$\
\\varphi x^{-2}\\sigma\_{0}\
$$\
\
$$\
s=\\varphi x^{-2}\\sigma\_0+\\tilde{s}\
$$\
\
$$\
\\tilde{s}\
$$\
\
$$\
y,\
$$\
\
$$\
Ps\
$$\
\
$$\
L^{2}\
$$\
\
$$\
\\left\|P.\\right)\
$$\
\
$$\
Ps=0\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
M\_{0},\
$$\
\
$$\
s=x^{-2}\\sigma\_0+o(1)\
$$\
\
(8.15)\
\
as _x →_ 0\. Note that by non-degeneracy, the solution _s_ is unique. The solution _s_ admits\
the following expansion around _p0_\
\
$$\
x\\to0\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
s=h\_{0}+o(1)as\|z\|\\to0,\
$$\
\
(8.16)\
\
where _h0_ is a 0-germ at _p0._ Define a mapping\
\
$$\
h\_{0}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
\\begin{aligned}&S\_{\\infty}^{0}:V\_{0}\\rightarrow S^{2}(T\_{p\_{0}}^{\*}M\_{0}),by\ &\\&S\_{\\infty}^{0}(\\sigma\_{0})\\equiv h\_{0}.\ \\end{aligned}\
$$\
\
(8.17)\
\
* * *\
\
This mapping enjoys the following property.\
\
Lemma 25. _The mapping S0_ ∞: _V0 → S_\
\
2(Tp∗0M0) is surjective.\
\
$$\
S\_{\\infty}^{0}:V\_{0}\\to S^{2}(T\_{p\_{0}}^{\*}M\_{0})\
$$\
\
_Proof._ Assume _S0_ ∞is not surjective. Then there exist a 0-germ _h0_ such that _h0_ is\
˜ be the solution of ˜ = 0 with following leading\
orthogonal to the image of _S0_ ∞. Let _h P h_\
terms\
\
$$\
S\_{\\infty}^{0}\
$$\
\
$$\
h\_{0}\
$$\
\
$$\
h\_{0}\
$$\
\
$$\
S\_{\\infty}^{0}\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
P\\tilde{h}=0\
$$\
\
$$\
\\tilde{h}=h\_{0}\|z\|^{2-m}+o(\|z\|^{2-m})\\mathrm{as}\|z\|\\to0,\
$$\
\
(8.18)\
\
$$\
\\tilde{h}=S\_{0}^{\\infty}(h)x^{\\delta\_{0,P}^{+}}+o\\big(x^{\\delta\_{0,P}^{+}}\\big)\\mathrm{as}x\\to0.\
$$\
\
(8.19)\
\
Also for a boundary tensor _τ ∈ V0,_ let _˜τ_ be the solution of _P τ˜_ = 0 with following leading\
terms\
\
$$\
\\tilde{\\tau}\
$$\
\
$$\
\\tau\\in V\_{0}\
$$\
\
$$\
P\\tilde{\\tau}=0\
$$\
\
$$\
\\begin{aligned}\\tilde{\\tau}&=S\_{\\infty}^{0}(\\tau)+o(1)as\|z\|\\rightarrow0,\\\tilde{\\tau}&=x^{-2}\\tau+o(1)as x\\rightarrow0.\\end{aligned}\
$$\
\
(8.20)\
\
˜ we see that\
By applying Lemma 24 to _˜τ_ and _h_\
\
$$\
\\tilde{\\tau}\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
\\langle\\langle h\_{0},S\_{\\infty}^{0}\\tau\\rangle\\rangle=c\\langle S\_{0}^{\\infty}h\_{0},\\tau\\rangle,\
$$\
\
(8.21)\
\
∞\
for every _τ ∈ V0,_ where _c 6=_ 0, so _S0_ (h) = 0. This implies that _h0_ = 0 by Proposition 7.1 (1), which is a contradiction.\
\
$$\
\\tau\\in V\_{0}\
$$\
\
$$\
c\\neq0\
$$\
\
$$\
S\_{0}^{\\infty}(h)=0\
$$\
\
$$\
h\_{0}=0\
$$\
\
We next define a mapping from _E0⊥ ⊂ V0_ (the orthogonal complement in _L2_) to\
⊥\
1-germs by the following. Given _σ0 ∈ E0,_ as above let _s_ be the solution of _Ps_ = 0\
defined on all of _M0,_ which is in _L2_ on any compact subset of _M0,_ and satisfies\
\
$$\
E\_{0}^{\\perp}\\subset V\_{0}\
$$\
\
$$\
L^{2})\
$$\
\
$$\
\\sigma\_{0}\\in E\_{0}^{\\perp}\
$$\
\
$$\
Ps=0\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
M\_{0},\
$$\
\
$$\
s=x^{-2}\\sigma\_0+o(1),\
$$\
\
(8.22)\
\
* * *\
\
as _x →_ 0\. By Lemma 24, _s_ admits an expansion\
\
$$\
x\\to0\
$$\
\
$$\
s=h\_{1}+o(\|z\|),\
$$\
\
(8.23)\
\
as _\|z\|→_ 0, where _h1_ is a 1-germ at _p0._ We then define the mapping\
\
$$\
\|z\|\\to0\
$$\
\
$$\
h\_{1}\
$$\
\
$$\
p\_{0}\
$$\
\
$$\
S\_{\\infty}^{1}:E\_{0}^{\\perp}\\to F\_{1}\\otimes S^{2}(T\_{p\_{0}}^{\*}M\_{0}),\\mathrm{by}\
$$\
\
(8.24)\
\
$$\
S\_{\\infty}^{1}(\\sigma\_{0})\\equiv h\_{1}.\
$$\
\
(8.25)\
\
This mapping is also onto.\
\
⊥\
Lemma 26. The mapping S1∞: E0 → F1 ⊗ S2(Tp∗0M0) is surjective.\
\
$$\
S\_{\\infty}^{1}:E\_{0}^{\\perp}\\to F\_{1}\\otimes S^{2}(T\_{p\_{0}}^{\*}M\_{0})\
$$\
\
_Proof._ By Proposition 7.1 (2), _S1∞_ is injective, so by the same argument in the proof of\
Lemma 25, it follows that _S1_ ∞is surjective.\
\
$$\
S\_{1}^{\\infty}\
$$\
\
$$\
S\_{\\infty}^{1}\
$$\
\
⊥\
We next define a mapping from _(E0 ⊕ E1) ⊂ V0_ (the orthogonal complement in _L2_)\
⊥\
to 2-germs by the following. Given _σ0 ∈_ ( _E0 ⊕ E1),_ as above let _s_ be the solution of\
_Ps_ = 0 defined on all of _M0,_ which is in _L2_ on any compact subset of _M0,_ and satisfies\
\
$$\
(E\_{0}\\oplus E\_{1})^{\\perp}\\subset V\_{0}\
$$\
\
$$\
L^{2})\
$$\
\
$$\
\\sigma\_{0}\\in(E\_{0}\\oplus E\_{1})^{\\perp}\
$$\
\
$$\
Ps=0\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
M\_{0},\
$$\
\
$$\
s=x^{-2}\\sigma\_0+o(1),\
$$\
\
(8.26)\
\
as _x →_ 0\. By Lemma 24, _s_ admits an expansion\
\
$$\
x\\to0\
$$\
\
$$\
s=h\_{2}+o(\|z\|^{2}),\
$$\
\
(8.27)\
\
$$\
\|z\|\\to0\
$$\
\
as _\|z\|→_ 0, where _h2_ is a 2-germ at _p0._\
\
$$\
h\_{2}\
$$\
\
$$\
p\_{0}\
$$\
\
We then define the mapping\
\
$$\
\\begin{aligned}&S\_{\\infty}^{2}:(E\_{0}\\oplus E\_{1})^{\\perp}\\rightarrow F\_{2}\\otimes S^{2}(T\_{p\_{0}}^{\*}M\_{0}),by\ &\\&S\_{\\infty}^{2}(\\sigma\_{0})\\equiv h\_{2}.\ \\end{aligned}\
$$\
\
(8.28)\
\
The following Lemma says that _S2_ ∞\
terization of its image\
\
is _not_ surjective, and also gives a complete charac-\
\
$$\
S\_{\\infty}^{2}\
$$\
\
* * *\
\
Lemma 27. _Let T_ = _Im(S2_ ∞) _then_\
\
$$\
T=Im(S\_{\\infty}^{2})\
$$\
\
$$\
T=S^{\\perp},\
$$\
\
(8.29)\
\
_where the orthogonal complement is with respect to the_ 2- _germ inner product, and_\
\
$$\
S=\\Big{\|z\|^{m+2}\\mathcal{K}\_{e u c}\\Big(\\frac{\\alpha}{\|z\|^{m}}\\Big)\|\\alpha\\mathit{i s a o n e-f o r m w i t h l i n e a r c o e f f i c i e n t s}\\Big}.\
$$\
\
(8.30)\
\
_Proof._ Let _h2 ∈ T_ so _h2_ = _S2_ ∞(τ) and let\
leading terms\
\
˜ be the solution of ˜ = 0 with following\
h _P h_\
\
$$\
h\_{2}\\in T\
$$\
\
$$\
h\_{2}=S\_{\\infty}^{2}(\\tau)\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
P\\tilde{h}=0\
$$\
\
$$\
\\tilde{h}=h\_{2}+o\\big(\|z\|^{2}\\big)\\mathrm{as}\|z\|\\to0,\
$$\
\
(8.31)\
\
$$\
\\tilde {h} = x ^ {- 2} \\tau + o (1) \\mathrm {a s} x \\rightarrow 0.\
$$\
\
(8.32)\
\
For any _t2 ∈ S,_ Let _t˜_ be the solution of _P t˜_ = 0 with the following leading terms\
\
$$\
t\_{2}\\in S\
$$\
\
$$\
\\tilde{t}\
$$\
\
$$\
P\\tilde{t}=0\
$$\
\
$$\
\\tilde{t}=t\_{2}\|z\|^{-2-m}+o\\big(\|z\|^{-m}\\big)\\mathrm{as}\|z\|\\to0,\
$$\
\
(8.33)\
\
$$\
\\tilde{t}=S\_{2}^{\\infty}(t\_{2})x^{-2}x^{m-1}+o(x^{m-1})\\mathrm{ ~~a s~~}x\\to0.\
$$\
\
(8.34)\
\
˜ and ˜ we obtain\
Applying Lemma 24 to _t h_\
\
$$\
\\tilde{t}\
$$\
\
$$\
\\tilde{h}\
$$\
\
$$\
\\langle\\langle h\_{2},t\_{2}\\rangle\\rangle=\\langle\\langle S\_{\\infty}^{2}(\\tau),t\_{2}\\rangle\\rangle=c\\langle\\tau,S\_{2}^{\\infty}(t\_{2})\\rangle=0,\
$$\
\
(8.35)\
\
$$\
c\\neq0\
$$\
\
⊥\
for some constant _c 6=_ 0, so by Proposition 7.1 it follows that _T ⊂ S._\
\
$$\
T\\subset S^{\\perp}\
$$\
\
⊥\
Next, assume that _S2_ ∞is not surjective onto _S._ Then there exists a nontrivial\
⊥ ⊥\
_s2 ∈ S ∩ T._ Let _˜s_ be the solution of P(˜s) = 0 with the following leading terms\
\
$$\
S\_{\\infty}^{2}\
$$\
\
$$\
S^{\\perp}\
$$\
\
$$\
s\_{2}\\in S^{\\perp}\\cap T^{\\perp}\
$$\
\
$$\
P\\left(\\tilde{s}\\right)=0\
$$\
\
$$\
\\tilde{s}\
$$\
\
$$\
\\tilde{s}=s\_{2}\|z\|^{-2-m}+o\\big(\|z\|^{-m}\\big)\\mathrm{as}\|z\|\\to0,\
$$\
\
(8.36)\
\
$$\
\\tilde{s}=S\_{2}^{\\infty}(s\_{2})x^{-2}x^{m-1}+o(x^{m-1})\\mathrm{as}x\\to0.\
$$\
\
(8.37)\
\
* * *\
\
$$\
\\tau\\in(E\_0\\oplus E\_1)^{\\perp}\
$$\
\
⊥˜ be the solution of\
Also, for any boundary tensor _τ ∈_ ( _E0 ⊕ E1),_ let _t P_ with following\
leading terms\
\
$$\
\\tilde{t}\
$$\
\
$$\
\\tilde{t}=S\_{\\infty}^{2}(\\tau)+o(\|z\|^{2})\\mathrm{as}\|z\|\\to0,\
$$\
\
(8.38)\
\
$$\
\\tilde {t} = x ^ {- 2} \\tau + o (1) \\mathrm {a s} x \\rightarrow 0.\
$$\
\
(8.39)\
\
Applying Lemma 24 to _t˜_ and _˜s_ we obtain\
\
$$\
\\tilde{t}\
$$\
\
$$\
\\tilde{s}\
$$\
\
$$\
\\langle S\_{2}^{\\infty}(s\_{2}),\\tau\\rangle=c\\langle\\langle s\_{2},S\_{\\infty}^{2}(\\tau)\\rangle\\rangle=0,\
$$\
\
(8.40)\
\
∞\
which implies that _S2 (s2)_ = 0 so _s2 ∈ S_ by Proposition 7.1 (3), which gives a contradiction.\
\
$$\
S\_{2}^{\\infty}(s\_{2})=0\
$$\
\
$$\
s\_{2}\\in S\
$$\
\
Next, we give an explicit description of the elements of _S._\
\
α1\
Lemma 28. _Let α =mwhere α1_\
\|z\|\
_Then_\
\
= aijzidzj is a one-form with linear coefficients.\
\
$$\
\\alpha=\\frac{\\alpha\_{1}}{\|z\|^{m}}\
$$\
\
$$\
\\alpha\_{1}=a\_{ij}z\_{i}dz^{j}\
$$\
\
$$\
\\mathcal{K} _{e u c}(\\alpha)_{i j}=\\frac{1}{2}\\Big(\\frac{a\_{i j}+a\_{j i}}{\|z\|^{m}}+\\frac{-m z\_{i}z\_{p}a\_{p j}-m z\_{j}z\_{t}a\_{t i}}{\|z\|^{m+2}}\\Big)+\\frac{1}{m}\\Big(\\frac{-t r(a)}{\|z\|^{m}}+\\frac{m z\_{t}z\_{p}a\_{p t}}{\|z\|^{m+2}}\\Big)\\delta\_{i j}\
$$\
\
(8.41)\
\
_Furthermore, we may write_\
\
$$\
\\mathcal{K} _{e u c}(\\alpha)=\|z\|^{-m-2}K_{k l i j}z^{k}z^{l}d z^{i}d z^{j},\
$$\
\
(8.42)\
\
_where_\
\
$$\
\\begin{align\*}K\_{ijkl}&=\\frac{1}{2}\\Big((a\_{ij}+a\_{ji})\\delta\_{kl}-\\frac{m}{2}(\\delta\_{ik}a\_{lj}+\\delta\_{il}a\_{kj})-\\frac{m}{2}(\\delta\_{kj}a\_{li}+\\delta\_{lj}a\_{ki})\\Big)\\&+\\frac{-tr(a)\\delta\_{kl}\\delta\_{ij}}{m}+\\frac{\\delta\_{ij}}{2}(a\_{lk}+a\_{kl}).\\end{align\*}\
$$\
\
(8.43)\
\
* * *\
\
Proof. Let α1 = aijxidxj be a one-form with linear coefficients. Then we have\
\
$$\
\\alpha\_{1}=a\_{ij}x\_{i}dx^{j}\
$$\
\
$$\
\\begin{align\*}(\\delta\_{euc}^{ _}\\alpha){ij}&=\\frac{1}{2}(\\partial{i}\\alpha\_{j}+\\partial\_{j}\\alpha\_{i})\\&=\\frac{1}{2}\\Big(\\partial\_{i}\\Big(\\frac{a\_{pj}z\_{p}}{\|z\|^{m}}\\Big)+\\partial\_{j}\\Big(\\frac{a\_{ki}z\_{k}}{\|z\|^{m}}\\Big)\\Big).\\end{align_}\
$$\
\
(8.44)\
\
−mzi\
Using ∂i(\|z\|−m) =m+2we obtain\
\|z\|\
\
$$\
\\partial\_{i}(\|z\|^{-m})=\\frac{-m z\_{i}}{\|z\|^{m+2}}\
$$\
\
$$\
(\\delta\_{e u c}^{\*}\\alpha) _{i j}=\\frac{1}{2}\\Big(\\frac{a_{i j}+a\_{j i}}{\|z\|^{m}}+\\frac{-m z\_{i}z\_{p}a\_{p j}-m z\_{j}z\_{k}a\_{k i}}{\|z\|^{m+2}}\\Big).\
$$\
\
(8.45)\
\
Also,\
\
$$\
\\delta\_{e u c}(\\alpha)=-\\partial\_{k}X\_{k}=-\\partial\_{k}\\Big(\\frac{a\_{p k}z\_{p}}{\|z\|^{m}}\\Big)=\\frac{-t r(a)}{\|z\|^{m}}+\\frac{m z\_{k}z\_{p}a\_{p k}}{\|z\|^{m+2}}.\
$$\
\
(8.46)\
\
The formula (8.41) follows directly from these computations, and (8.42) follows easily\
from this.\
\
Lemma 29. The tensor r2geuc = Pijklzizjdzkdzl, where\
\
$$\
r^{2}g\_{euc}=P\_{ijkl}z^{i}z^{j}dz^{k}dz^{l}\
$$\
\
$$\
P\_{ijkl}=\\delta\_{ij}\\delta\_{kl}.\
$$\
\
(8.47)\
\
The tensor r2dr ⊗ dr = Qijklzizjdzkdzl, where\
\
$$\
\\otimes dr=Q\_{ijkl}z^{i}z^{j}dz^{k}dz^{l}\
$$\
\
$$\
Q\_{ijkl}=\\frac{1}{2}(\\delta\_{ik}\\delta\_{jl}+\\delta\_{il}\\delta\_{jk})\
$$\
\
(8.48)\
\
The tensor r4θ ⊗ θ = Aijklzizjdzkdzl, where\
\
$$\
r^{4}\\theta\\otimes\\theta=A\_{ijkl}z^{i}z^{j}dz^{k}dz^{l}\
$$\
\
$$\
A\_{i j k l}=\\frac{1}{2}\\left(J\_{i}^{k}J\_{j}^{l}+J\_{i}^{l}J\_{j}^{k}\\right).\
$$\
\
(8.49)\
\
_Proof._ The proof is immediate.\
\
Lemma 30. _We have the following identities:_\
\
$$\
\\langle\\langle Q,K\\rangle\\rangle=\\frac{2-m^{2}-m}{2}t r(a),\
$$\
\
(8.50)\
\
$$\
\\langle\\langle A,K\\rangle\\rangle=\\frac{m+2}{2}t r(a),\
$$\
\
(8.51)\
\
$$\
\\left\\langle\\left\\langle K,P\\right\\rangle\\right\\rangle=0.\
$$\
\
(8.52)\
\
* * *\
\
_Proof._ We compute\
\
$$\
\\begin{aligned}\\langle\\langle Q,K\\rangle\\rangle&=\\frac{1}{2}\\big((a\_{ij}+a\_{ji})\\delta\_{ij}-\\frac{m}{2}(\\delta\_{ii}a\_{jj}+\\delta\_{ij}a\_{ij})-\\frac{m}{2}(\\delta\_{ij}a\_{ji}+\\delta\_{jj}a\_{ii})\\big)\\&+\\frac{-tr(a)\\delta\_{ij}\\delta\_{ij}}{m}+\\frac{\\delta\_{ij}}{2}(a\_{ji}+a\_{ij})\\&=\\frac{1}{2}\\big(2tr(a)-m^2tr(a)-mtr(a))\\big)=\\frac{2-m^2-m}{2}tr(a).\ \\end{aligned}\
$$\
\
(8.53)\
\
This proves the first identity. For the second identity, we have\
(\
\
$$\
\\begin{align\*}\\langle\\langle A,K\\rangle\\rangle=&\\frac{1}{2}\\Big((a\_{ij}+a\_{ji})\\delta\_{kl}J\_i^k J\_j^l-\\frac{m}{2}(J\_i^k J\_j^l\\delta\_{ik}a\_{lj}+J\_i^k J\_j^l\\delta\_{il}a\_{kj})\\&-\\frac{m}{2}(J\_i^k J\_j^l\\delta\_{kj}a\_{li}+J\_i^k J\_j^l\\delta\_{lj}a\_{ki})\\Big)+\\frac{-tr(a)\\delta\_{kl}\\delta\_{ij}J\_i^k J\_j^l}{m}+J\_i^k J\_j^l\\delta\_{ij}\\frac{(a\_{lk}+a\_{kl})}{2}\\&=\\frac{1}{2}\\Big(2tr(a)+mtr(a)\\Big)-tr(a)+tr(a)=\\frac{m+2}{2}tr(a).\\end{align\*}\
$$\
\
(8.54)\
\
Finally, the last identity follows from the fact that _K_ is traceless on the first and last\
two pairs of indices.\
\
Lemma 31. _We have the following identities:_\
\
$$\
B\_{e u c}(r^{2}d r\\otimes d r)=(-2n)r d r,\
$$\
\
(8.55)\
\
$$\
B\_{e u c}(r^{4}\\theta\\otimes\\theta)=2r d r,\
$$\
\
(8.56)\
\
$$\
B\_{e u c}(r^{2}g\_{e u c})=2(n-1)r d r.\
$$\
\
(8.57)\
\
Proof. Recall that if H = Hijklxixjdxk ⊗ dxl then\
\
$$\
H=H\_{ijkl}x^{i}x^{j}dx^{k}\\otimes dx^{l}\
$$\
\
$$\
B\_{e u c}(H)=(-2H\_{k j k l}+H\_{j l k k})x^{j}d x^{l}.\
$$\
\
(8.58)\
\
It follows that\
\
$$\
\\begin{align\*}B\_{euc}(r^2dr\\otimes dr)&=(-2\\frac{\\delta\_{kk}\\delta\_{jl}+\\delta\_{kl}\\delta\_{jk}}{2}+\\frac{\\delta\_{jk}\\delta\_{lk}+\\delta\_{kj}\\delta\_{lk}}{2})x^jdx^l\\&=(-2n)\\sum\_{i}x^idx^i.\\end{align\*}\
$$\
\
(8.59)\
\
* * *\
\
Next,\
\
$$\
B\_{{e u c}}(r^{2}\\theta\\otimes\\theta)=\\Big(-2\\frac{J\_{k}^{k}J\_{j}^{l}+J\_{k}^{l}J\_{j}^{k}}{2}+\\frac{J\_{j}^{k}J\_{l}^{k}+J\_{j}^{k}J\_{l}^{k}}{2}\\Big)x^{j}d x^{l}=2\\sum\_{i}x^{i}d x^{i}.\
$$\
\
(8.60)\
\
The formula (8.57) follows easily.\
\
We next construct a special symmetric 2-tensor _k1_ on the Calabi manifold.\
\
$$\
k\_{1}\
$$\
\
Proposition 8.1. _Let σ2 denote the quadratic_ 2- _tensor_\
\
$$\
\\sigma\_{2}\
$$\
\
$$\
\\begin{align\*}\\sigma\_{2}=&r^{2}(-dr\\otimes dr-(2n-1)r^{2}\\theta\\otimes\\theta+g\_{euc})\\=&S\_{ijkl}x^{i}x^{j}dx^{k}dx^{l}.\\end{align\*}\
$$\
\
(8.61)\
\
_Then_\
\
$$\
tr\_{euc}(\\sigma\_{2})=0,\
$$\
\
(8.62)\
\
$$\
\\hat{B} _{e u c}(\\sigma_{2})=0,\
$$\
\
(8.63)\
\
$$\
\\Delta\_{e u c}(\\sigma\_{2})=0,\
$$\
\
(8.64)\
\
_and_\
\
$$\
\\langle\\langle S,K\\rangle\\rangle=0,\
$$\
\
(8.65)\
\
for all Kijkl of the form in (8.43). Furthermore, there exist a constant c 6= 0 and a\
_tensor k1 defined on the Calabi manifold with the following properties_\
\
$$\
K\_{ijkl}\
$$\
\
$$\
c\\neq0\
$$\
\
$$\
k\_{1}\
$$\
\
$$\
\\begin{aligned}&k\_{1}=c\\cdot\\sigma\_{2}+O(r^{-2n+2+\\epsilon}),\\quad\ &\\begin{aligned}\ &P\_{g\_{cal}}(k\_{1})=o\\&B\_{g\_{cal}}(k\_{1})=0,\ &\\end{aligned}\ \\end{aligned}\
$$\
\
(8.66)\
\
$$\
as;r\\to\\infty.\
$$\
\
* * *\
\
_Proof._ For equation (8.62), we have\
\
$$\
tr\_{euc}(\\sigma\_{2})=r^{2}\\big(-1-(2n-1)+2n\\big)=0.\
$$\
\
(8.67)\
\
For equation (8.63), using Lemma 31, we have\
\
$$\
B\_{e u c}(\\sigma\_{2})=\\left(2n-2(2n-1)+2(n-1)\\right)r d r=0.\
$$\
\
(8.68)\
\
Next, it follows from Lemma 29 that Sijkl = Sklij, so (8.62) implies (8.64). To see (8.65),\
Lemma (30) implies that\
\
$$\
S\_{ijkl}=S\_{klij}\
$$\
\
$$\
\\langle\\langle S,K\\rangle\\rangle=\\big((n+1)(1-2n)-(1-2n^{2}-n)\\big)t r(a)=0.\
$$\
\
(8.69)\
\
Next, let ( _H,_ Λ) = _(σ2,0)_ in Proposition 3.1 to find a solution of\
\
$$\
(H,\\Lambda)=(\\sigma\_2,0)\
$$\
\
$$\
\\begin{align\*}P\_{g\_{cal}}(k\_1)&=\\tilde{\\lambda}o\\k\_1&=c\\cdot\\sigma\_2+O(r^{-2n+2+\\epsilon}),\\B\_{g\_{cal}}(h)&=0,\\end{align\*}\
$$\
\
(8.70)\
\
˜ is given by\
where _λ_\
\
$$\
\\tilde{\\lambda}\
$$\
\
$$\
\\tilde{\\lambda}=-\\frac{c}{\|o\| _{L^{2}}^{2}}\\lim_{r\\rightarrow\\infty}\\int\_{S\_{r}/\\Gamma\_{n}}\\frac{n+1}{r}\\langle\\sigma\_{2},o\\rangle d S\_{S\_{r}/\\Gamma\_{n}}.\
$$\
\
(8.71)\
\
The leading term in the integrand is given by\
\
$$\
\\frac{n+1}{r}\\langle\\sigma\_{2},o\_{e u c}\\rangle=c\\cdot2n(1-n^{2})r^{1-m},\
$$\
\
(8.72)\
\
˜ = 1 finishes the proof.\
so choosing the scaling constant _c_ to make _λ_\
\
$$\
\\tilde{\\lambda}=1\
$$\
\
The following result is the key ingredient to our existence theorem in the AHE case,\
which will be proved in Section 9.\
\
* * *\
\
Proposition 8.2. Let σ = c · σ2 = c · Sijklzizjdzkdzl be as Proposition 8.1. Then there\
˜ ˜) = 0\
exist a solution k of Pg0(k defined on M0 such that\
\
$$\
\\sigma=c\\cdot\\sigma\_{2}=c\\cdot S\_{ijkl}z^{i}z^{j}dz^{k}dz^{l}\
$$\
\
$$\
\\tilde{k}\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
P\_{g\_0}(\\tilde{k})=0\
$$\
\
$$\
\\tilde{k}=\\sigma+O(\|z\|)\\mathrm{ ~~as~~}\|z\|\\rightarrow0\
$$\
\
(8.73)\
\
$$\
\\tilde{k}=k\_{\\infty}+o(1)\\mathrm{ ~~\\it{a s}~~}x\\to0,\
$$\
\
(8.74)\
\
_where x2k_ ∞ _∈ V0._\
\
$$\
x^{2}k\_{\\infty}\\in\\overline{V\_{0}}\
$$\
\
_Proof._ The proof is immediate from Lemma 27 if we let _σ_ be the leading term of the\
tensor _k1_ found in Proposition 8.1.\
\
$$\
k\_{1}\
$$\
\
* * *\
\
## Completion of proofs\
\
In this chapter, we complete the proofs of Theorems 1.2 and 1.3. First, for _u ∈_ R, we\
define\
\
$$\
u\\in\\mathbb{R}\
$$\
\
$$\
h\_{t,u}=g\_{c a l}+t h+u t k\_{1},\
$$\
\
(9.1)\
\
where _h_ was defined in (4.4), and _k1_ was defined in Proposition 8.1.\
\
$$\
k\_{1}\
$$\
\
Lemma 32. For t and u sufficiently small, ht,u is a Riemannian metric on Xt. Moreover, for each integer ‘ ≥ 0, there exists a constant c‘so that ht,u satisfies the following\
estimate on Xt\
\
$$\
h\_{t,u}\
$$\
\
$$\
X^{t}\
$$\
\
$$\
\\ell\\geq0\
$$\
\
$$\
c\_{\\ell}\
$$\
\
$$\
h\_{t,u}\
$$\
\
$$\
X^{t}\
$$\
\
$$\
\|\\nabla^{\\ell}\\big(R i c\_{h\_{t,u}}-t\\Lambda h\_{t,u}-t\\big(\\lambda+u\\big)\\chi\_{t}(\\rho)o\\big)\| _{g_{c a l}}\\leq c\_{\\ell}t^{2}\\big(1+u^{2}+t^{2}\\big)\\rho^{2-\\ell}.\
$$\
\
(9.2)\
\
Proof. Since h and k1 both have quadratic leading terms, and gcal is ALE, there exist\
constants _c_ and _c1_ so that\
\
$$\
k\_{1}\
$$\
\
$$\
g\_{cal}\
$$\
\
$$\
c\_{1}\
$$\
\
$$\
\|h\| _{g_{c a l}}(p)\\leq c\\rho^{2}(p)\
$$\
\
(9.3)\
\
$$\
\|k\_{1}\| _{g_{c a l}}(p)\\leq c\_{1}\\rho^{2}(p),\
$$\
\
(9.4)\
\
for any p ∈ Xt. Similarly, there exists a constant c2 so that\
\
$$\
p\\in X^{t}\
$$\
\
$$\
c\_{2}\
$$\
\
$$\
\|o\| _{g_{{c a l}}}(p)\\leq c\_{2}\\rho^{-2n}(p),\
$$\
\
(9.5)\
\
* * *\
\
$$\
p\\in X^{t}\
$$\
\
for any p ∈ Xt. It follows that\
\
$$\
\|t h\| _{g_{c a l}}(p)\\leq c\\rho^{2}(p)\\leq\\frac{1}{2}c t^{\\frac{1}{2}}\
$$\
\
(9.6)\
\
$$\
\|t u k\_{1}\| _{g_{c a l}}(p)\\leq c\_{1}u\\rho^{2}(p)\\leq\\frac{1}{2}c\_{1}u t^{\\frac{1}{2}}\
$$\
\
(9.7)\
\
$$\
\|t u o\| _{g_{c a l}}(p)\\leq c\_{2}u\\rho^{2}(p)\\leq\\frac{1}{2}c\_{2}u t^{\\frac{1}{2}}\
$$\
\
(9.8)\
\
The right hand side is independent of p so ht,u is a Riemannian metric for sufficiently\
small _t_ and _u._ Recall that\
\
$$\
h\_{t,u}\
$$\
\
$$\
d\_{g\_{cal}}Ric(h)=\\Lambda g\_{cal}+\\lambda o\
$$\
\
(9.9)\
\
$$\
d\_{g\_{cal}}Ric(o)=0\
$$\
\
(9.10)\
\
$$\
d\_{g\_{cal}}Ric(k\_1)=o,\
$$\
\
(9.11)\
\
so we have\
\
$$\
Ric(g\_{cal}+th+tuk\_1)=Ric(g\_{cal})+d\_{g\_{cal}}Ric(th+tuk\_1)+Q(th+tuk\_1),\
$$\
\
(9.12)\
\
where, using (4.14), _Q_ is a nonlinear term satisfying\
\
$$\
\\begin{aligned}{\|Q(t h+t u k\_{1})\|\\leq b\\Big(\|R m\_{g\_{c a l}}\|t h+t u k\_{1}\|^{2}}&{{}+\|t h+t u k\_{1}\|\\nabla^{2}(t h+t u k\_{1})\|}\ {}&{{}+\|\\nabla(t h+t u k\_{1})\|^{2}\\Big),}\ \\end{aligned}\
$$\
\
(9.13)\
\
for some constant _b_ and for _t_ and _u_ sufficiently small, and where the norms and covariant\
derivatives are measured with respect to the Calabi metric. Note that\
\
$$\
\\left\|\\nabla^{\\ell}h\\right\|\\leq c\_{\\ell}\\rho^{2-\\ell}\
$$\
\
(9.14)\
\
$$\
\|\\nabla^{\\ell}o\|\\leq c\_{\\ell}\\rho^{-2n-\\ell}\
$$\
\
(9.15)\
\
$$\
\|\\nabla^{\\ell}k\_{1}\|\\leq c\_{\\ell}\\rho^{2-\\ell},\
$$\
\
(9.16)\
\
* * *\
\
so it follows that\
\
$$\
\\left\|Q\\left(t h+t u k\_{1}\\right)\\right\|\\leq b\_{1}t^{2}\\left(1+t^{2}+u^{2}\\right)\\rho^{2}\
$$\
\
(9.17)\
\
and consequently\
\
$$\
\\begin{align\*}\|Ric\_{h\_{t,u}}-t\\Lambda h\_{t,u}-t\\lambda o-t u o\|\\leq c\_0t^2(1+t^2+u^2)\\rho^2,\\end{align\*}\
$$\
\
(9.18)\
\
for some constant _c0,_ so the lemma for _‘_ = 0 follows. The proof for _‘_ \> 0 is similar and\
is omitted.\
\
$$\
c\_{0},\
$$\
\
$$\
\\ell>0\
$$\
\
$$\
\\ell=0\
$$\
\
We next define\
8\
\
$$\
\\begin{aligned}&k=\\left{\\begin{aligned}\ &\\tilde{k}&&M\_{0}\\setminus B(p\_{0},2t^{1/4})\\&&\\&(1-\\chi\_{t}(r))\\phi\_{t}^{\*}\\tilde{k}+\\chi\_{t}(r)t^{2}k\_{1}&&(1/2)t^{-1/4}<r<2t^{-1/4}\\&&\\&t^{2}k\_{1}&&r<(1/2)t^{-1/4}\ &\\end{aligned}\\right.,\ \\end{aligned}\
$$\
\
(9.19)\
\
˜ was defined in Proposition 8.2.\
where χt is the cutoff function we defined in (1.10), and k\
For u ∈ R, consider the metric on Mt defined by gt,u = gt \+ uk, where gt is the refined\
metric defined in (4.20). Note that gt,u has the following expression\
8\
\
$$\
\\tilde{k}\
$$\
\
$$\
\\chi\_{t}\
$$\
\
$$\
u\\in\\mathbb{R}\
$$\
\
$$\
M^{t}\
$$\
\
$$\
g\_{t,u}=g\_t+uk\
$$\
\
$$\
g\_{t}\
$$\
\
$$\
g\_{t,u}\
$$\
\
$$\
g\_{t,u}=\\left{\\begin{aligned}{}&{{}g\_{0}+u\\tilde{k}}&{}&{{}M\_{0}\\setminus B(p\_{0},2t^{1/4})}\ {}&{{}(1-\\chi\_{t}(r))\\phi\_{t}^{\*}(g\_{0}+u\\tilde{k})+\\chi\_{t}(r)t h\_{t,u}}&{}&{{}(1/2)t^{-1/4}<r<2t^{-1/4}}\ {}&{{}t h\_{t,u}}&{}&{{}r<(1/2)t^{-1/4}}\ \\end{aligned}\\right..\
$$\
\
(9.20)\
\
This metric satisfies the following modification of Lemma 14.\
\
Lemma 33. For t and u sufficiently small, gt,u _over, for each integer ‘ ≥ 0, there exist a constant c_\
estimate on Xt\
\
is a Riemannian metric on Mt. More-\
‘so that gt,u satisfies the following\
\
$$\
g\_{t,u}\
$$\
\
$$\
M^{t}\
$$\
\
$$\
\\ell\\geq0\
$$\
\
$$\
c\_{\\ell}\
$$\
\
$$\
g\_{t,u}\
$$\
\
$$\
X^{t}\
$$\
\
$$\
\|\\nabla^{\\ell}(R i c\_{g\_{t,u}}-\\Lambda g\_{t,u}-t(\\lambda+u)\\chi\_{t}(\\rho)o)\| _{g_{c a l}}\\leq c\_{\\ell}t^{2}(1+t^{2}+u^{2})\\rho^{2-\\ell}.\
$$\
\
(9.21)\
\
* * *\
\
Proof. If r < (1/2)t−1/4, then the proof follows from the Lemma 32 by scaling. If\
\
$$\
r<(1/2)t^{-1/4}\
$$\
\
$$\
(1/2)t^{-1/4}<r<2t^{-1/4},\
$$\
\
(9.22)\
\
then\
\
$$\
g\_{t,u}=\\left(1-\\chi\_{t}(r)\\right)\\left(\\phi\_{t}^{\*}(u\\tilde{k}+g\_{0})\\right)+\\chi\_{t}(r)\\left(t h\_{t}+t^{2}u k\_{1}\\right).\
$$\
\
(9.23)\
\
We have that\
\
(9.24)\
\
$$\
\\phi\_{t}^{\*}g\_{0}=t g\_{e u c}+t^{2}H+O\\left(t^{\\frac{3}{2}}\\rho^{3}\\right)\
$$\
\
$$\
t h\_{t}=t g\_{e u c}+t^{2}H+t O\\big(r^{-2n}\\big)+t O\\big(r^{2-2n+\\epsilon}\\big),\
$$\
\
(9.25)\
\
and\
\
$$\
\\phi\_{t}^{\*}(u\\tilde{k})=t^{2}(u\\sigma)+u t^{2}O(r^{-2n+2+\\epsilon})\
$$\
\
(9.26)\
\
$$\
t^{2}u k\_{1}=t^{2}u(\\sigma)+t^{2}O(r^{-2n+2+\\epsilon}),\
$$\
\
(9.27)\
\
as _t →_ 0\. Since the quadratic terms agree in each of these, we have the estimate\
\
$$\
t\\to0\
$$\
\
$$\
g\_{t,u}=t g\_{e u c}+t^{2}H+t^{2}u\\sigma+t O\\left(t^{\\frac{3}{2}}\\rho^{3}\\right),\
$$\
\
(9.28)\
\
as _t →_ 0\. Writing\
\
$$\
t\\to0.\
$$\
\
$$\
\\theta=g\_{t}-t g\_{e u c},\
$$\
\
(9.29)\
\
expanding the Ricci tensor near t · geuc we have\
\
$$\
t\\cdot g\_{euc}\
$$\
\
(9.30)\
\
$$\
R i c\_{g\_{t,u}}=d\_{t\\cdot e u c}R i c(\\theta)+Q(\\theta),\
$$\
\
where _Q(θ_) satisfies the estimate\
\
$$\
Q(\\theta)\
$$\
\
$$\
t^{2}\|Q(\\theta)\|\\leq c(\|\\theta\|\\nabla^{2}\\theta\|+\|\\nabla\\theta\|^{2}),\
$$\
\
(9.31)\
\
* * *\
\
for some constant c, where the norms are with respect to geuc. More precisely,\
\
$$\
g\_{euc}\
$$\
\
$$\
\\theta=t^{2}H+t^{2}u\\sigma+tO\\left(t^{\\frac{3}{2}}\\rho^{3}\\right)\
$$\
\
(9.32)\
\
implies that\
\
$$\
\|\\nabla^{2}\\theta\|\\theta\|=O\\big(t^{4}(1+u^{2}+t^{2})\\rho^{2}\\big),\
$$\
\
(9.33)\
\
$$\
\|\\nabla\\theta\|^{2}=O\\left(t^{4}(1+u^{2}+t^{2})\\rho^{2}\\right).\
$$\
\
(9.34)\
\
From (4.4) it follows that\
\
$$\
d\_{t\\cdot e u c}R i c(\\theta)=t\\Lambda g\_{e u c}+O\\left(t^{2}(1+u^{2}+t^{2})\\rho^{2}\\right),\
$$\
\
(9.35)\
\
where _O_ is with respect to the Euclidean metric. Note that (9.22) implies that\
\
$$\
t\\lambda\\chi\_{t}(\\rho)o=O(t^{2}\\rho^{2}).\
$$\
\
(9.36)\
\
Finally we obtain\
\
$$\
R i c\_{g\_{t,u}}-\\Lambda g\_{t,u}-t(\\lambda+u)\\chi\_{t}(\\rho)o=O\\left(t^{2}(1+t^{2}+u^{2})\\rho^{2}\\right),\
$$\
\
(9.37)\
\
so the lemma for _‘_ = 0 follows. For _‘_ \> 0, the proof is similar and is omitted.\
\
$$\
\\ell=0\
$$\
\
$$\
\\ell>0\
$$\
\
_Proof of Theorem 1.2._ We apply Proposition 5.1, keeping track of the dependence on\
the variable _u._ From Proposition 5.1, we obtain a solution of\
\
$$\
\\Phi\\left(\\hat{g} _{t,u,v}\\right)=\\lambda(t,u)\\left(\\chi_{t}o\\right).\
$$\
\
(9.38)\
\
Lemma 33 implies that _λ(t,u_) is differentiable in the _u_ variable, and if _λ_ = 0 then\
\
$$\
\\lambda(t,u)\
$$\
\
$$\
\\lambda=0\
$$\
\
$$\
\\lambda(t,u)=t u+O(t^{2-\\frac{\\delta\_{0}}{2}}).\
$$\
\
(9.39)\
\
By the classical implicit function theorem, for each _t_ sufficiently small, there exists _u(t_)\
such that λ(t,u(t)) = 0. For t sufficiently small, Ricgt,u,vis strictly negative, and a\
standard argument (see \[8\]) then implies that ˆgt,u,v is Einstein.\
\
$$\
u(t)\
$$\
\
$$\
\\lambda(t,u(t))=0\
$$\
\
$$\
R i c\_{g\_{t,u,v}}\
$$\
\
$$\
\\hat{g}\_{t,u,v}\
$$\
\
* * *\
\
_Proof of Theorem 1.3._ First assume that _g0_ is non-degenerate. Observe that the refined\
approximate metric is close to the näıve approximate metric in the Cδ2,α weighted\
0,δ _∞;t_\
norm, for _t_ sufficiently small. As above, from the results in \[10, Section 8\], for any\
metric gE satisfying (1.15), then there exists a diffeomorphism ϕ : Mt → Mt so that\
Bgt(gt − ϕ∗gE) = 0, and ϕ∗gE remains close to gt in the Cδ2,α weighted norm. The\
0,δ _∞;t_\
metric ϕ∗gE would then give a zero of the mapping Φt, but then (5.20) would then imply\
that _λ_ = 0, a contradiction.\
\
$$\
g\_{0}\
$$\
\
$$\
C\_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}\
$$\
\
$$\
g\_{E}\
$$\
\
$$\
\\varphi:M^{t}\\rightarrow M^{t}\
$$\
\
$$\
B\_{g\_{t}}(g\_{t}-\\varphi^{\*}g\_{E})=0\
$$\
\
$$\
\\varphi^{\*}g\_{E}\
$$\
\
$$\
g\_{t}\
$$\
\
$$\
C\_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}\
$$\
\
$$\
\\varphi^{\*}g\_{E}\
$$\
\
$$\
\\Phi\_{t}\
$$\
\
$$\
\\lambda=0\
$$\
\
If _g0_ is not non-degenerate, then if _δ_ ∞is chosen sufficiently small, the linearized\
operator is Fredholm (see \[20\]), so there is a finite-dimensional space of _L2_ infinitesimal\
Einstein deformations on ( _M0,g0)._ The remainder of the proof is almost identical to the\
proof of Theorem 1.1 given above.\
\
$$\
g\_{0}\
$$\
\
$$\
\\delta\_{\\infty}\
$$\
\
$$\
\\left(M\_{0},g\_{0}\\right)\
$$\
\
$$\
L^{2}\
$$\
\
* * *\
\
# Remarks on the four dimensional\
\
case\
\
In this chapter we give some remarks on the proof of existence result for the case _n_ = 2\
which was done by Biquard in \[10\].\
\
$$\
n=2\
$$\
\
In \[10, Lemma 11.1 (2)\], it is claimed that any quadratic germ at _p0_ can be extended\
to a kernel element on all of _M0_ (the AHE orbifold) which is bounded at infinity. This\
does not agree with the Lemma 27, which finds that there is an orthogonality condition\
on the germ which must be satisfied in order to be extendable. The proof of \[10, Theorem 1.1\] requires that the quadratic germs corresponding to the leading terms of _k1,_\
_k2,_ and _k3_ be extended in such a fashion. It turns out that the germ corresponding to\
_k1_ can indeed be extended, as is shown in Proposition 8.2 (it _does_ satisfy the required\
orthogonality condition). However, we show in this chapter that, in fact, the germs corresponding to _k2_ and _k3_ do not satisfy the required orthogonality condition, and therefore\
_cannot_ be extended to kernel elements which are bounded at infinity. However, we also\
show that the argument in \[10\] can be repaired by modifying the germs corresponding\
to _k2_ and _k3_ by adding Lie derivative terms, and then using the germ extension result\
in Lemma 27.\
\
$$\
p\_{0}\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
k\_{2},\
$$\
\
$$\
k\_{1}\
$$\
\
$$\
k\_{3}\
$$\
\
$$\
k\_{1}\
$$\
\
$$\
k\_{2}\
$$\
\
$$\
k\_{3}\
$$\
\
$$\
k\_{2}\
$$\
\
$$\
k\_{3}\
$$\
\
* * *\
\
#### 10.1 The tensors _k1, k2_ and _k3_\
\
10.1 The tensors k1 , k2 and k3\
\
$$\
k\_{1},;k\_{2}\
$$\
\
$$\
k\_{3}\
$$\
\
To recall some notation, define\
\
$$\
(\\alpha\_{1}) _{i}=r^{-2}I_{i p}^{1}x^{p}\
$$\
\
(10.1)\
\
$$\
(\\alpha\_{2}) _{i}=r^{-2}I_{i p}^{2}x^{p}\
$$\
\
(10.2)\
\
(10.3)\
\
$$\
(\\alpha\_{3}) _{i}=r^{-2}I_{i p}^{3}x^{p}.\
$$\
\
The quaternion identities are\
\
$$\
I^{1}I^{2}=I^{3}, ~~I^{2}I^{3}=I^{1},~~ I^{3}I^{1}=I^{2}\
$$\
\
(10.4)\
\
$$\
(I^{1})^{2}=(I^{2})^{2}=(I^{3})^{2}=-I d.\
$$\
\
(10.5)\
\
In our index notation, this is\
\
$$\
I\_{ip}^{1}I\_{pj}^{2}=I\_{ij}^{3},\ I\_{ip}^{2}I\_{pj}^{3}=I\_{ij}^{1},\ I\_{ip}^{3}I\_{pj}^{1}=I\_{ij}^{2}\
$$\
\
(10.6)\
\
$$\
I\_{i p}^{1}I\_{p j}^{1}=I\_{i p}^{2}I\_{p j}^{2}=I\_{i p}^{3}I\_{p j}^{3}=-\\delta\_{i j}.\
$$\
\
(10.7)\
\
Note also that the matrices corresponding to _I_\
\
1, I2, and I3 are skew-symmetric.\
\
$$\
I^{1},I^{2},\
$$\
\
$$\
I^{3}\
$$\
\
In \[10, Proposition 2.1 (5)\], the tensor _k1_ is defined as\
\
$$\
k\_{1}\
$$\
\
$$\
k\_{1,B}=\\frac{3}{2}\\hat{k} _{1}-\\frac{1}{8}\\sqrt{1+r^{4}}g_{E H}+\\frac{1}{12}\\delta^{\*}\\Big(\\frac{(1+r^{4})^{\\frac{3}{2}}-1}{r^{3}}\\partial\_{r}\\Big),\
$$\
\
(10.8)\
\
where\
\
(10.9)\
\
$$\
\\hat{k} _{1,B}=-\\frac{1}{12}(1+r^{4})^{\\frac{3}{2}}o_{1},\
$$\
\
and\
\
$$\
o\_{1}\\sim\\frac{1}{r^{2}}\\Big(r^{-2}d r^{2}+\\alpha\_{1}^{2}-\\alpha\_{2}^{2}-\\alpha\_{3}^{2}\\Big).\
$$\
\
(10.10)\
\
* * *\
\
A computation shows that\
\
$$\
k\_{1,B}\\sim\\frac{1}{12}(-2r^{2}\\alpha\_{1}^{2}+r^{4}\\alpha\_{2}^{2}+r^{4}\\alpha\_{3}^{2}).\
$$\
\
(10.11)\
\
On the other hand, in Proposition 8.1, the tensor _k1_ is defined as\
\
$$\
k\_{1}\
$$\
\
$$\
k\_{1,M V}\\sim r^{2}(-d r^{2}-(2n-1)r^{2}\\alpha\_{1}^{2}+g\_{E u c}),\
$$\
\
(10.12)\
\
where the complex dimension is _n._ For _n_ = 2, this is\
\
$$\
k\_{1,M V}\\sim c r^{2}(-2r^{2}\\alpha\_{1}^{2}+r^{4}\\alpha\_{2}^{2}+r^{4}\\alpha\_{3}^{2}).\
$$\
\
(10.13)\
\
Consequently, up to a constant, we have\
\
$$\
k\_{1,B}\\sim k\_{1,M V}.\
$$\
\
(10.14)\
\
It is easy to see that this germ is traceless, harmonic, and divergence-free. Furthermore,\
as shown in Proposition 8.1, it is orthogonal to the space of tensors _S_ arising from a\
germ of a 1-form with linear coefficients defined in Equation 8.30. Consequently, this\
quadratic germ can indeed be extended to a kernel element of _P_ on the AHE orbifold\
which is bounded at infinity. So there is no problem with extending the quadratic germ\
corresponding to _k1._\
\
$$\
k\_{1}\
$$\
\
In dimension 4, Eguchi-Hanson manifold has three infinitesimal Einstein deformations. This leads to two more tensors, _k2_ and _k3_ for the existence part. From \[10,\
Proposition 2.1 (5)\], the leading terms of _k2_ and _k3_ are (up to a multiple)\
\
$$\
k\_{2}\
$$\
\
$$\
k\_{3}\
$$\
\
$$\
k\_{2}\
$$\
\
$$\
k\_{3}\
$$\
\
$$\
k\_{2}\\sim r^{2}(dr\\odot r\\alpha\_{3}+r\\alpha\_{1}\\odot r\\alpha\_{2})\
$$\
\
(10.15)\
\
$$\
k\_{3}\\sim r^{2}(-d r\\odot r\\alpha\_{2}+r\\alpha\_{1}\\odot r\\alpha\_{3}).\
$$\
\
(10.16)\
\
* * *\
\
Consider first the term _r2(dr rα3)._ As a 2-tensor, this is written as\
\
$$\
r^{2}(d r\\odot r\\alpha\_{3})\
$$\
\
$$\
r^{2}(d r\\odot r\\alpha\_{3})=A\_{i j k l}x^{i}x^{j}d x^{k}d x^{l},\
$$\
\
(10.17)\
\
where\
\
$$\
A\_{i j k l}=\\frac{1}{4}\\big(\\delta\_{i k}I\_{j l}^{3}+\\delta\_{j k}I\_{i l}^{3}+\\delta\_{i l}I\_{j k}^{3}+\\delta\_{j l}I\_{i k}^{3}\\big).\
$$\
\
(10.18)\
\
Note that\
\
$$\
A\_{ijkl}=A\_{jikl}=A\_{ijlk},\
$$\
\
(10.19)\
\
$$\
\\sum\_{i}A\_{i i k l}=0,\
$$\
\
(10.20)\
\
$$\
\\sum\_{k}A\_{ijkk}=0.\
$$\
\
(10.21)\
\
Recall from Equation 8.43, the 2-germ _K_ defined by\
(\
\
$$\
\\begin{align\*}K\_{ijkl}&=\\frac{1}{2}\\Big(\\big(a\_{ij}+a\_{ji}\\big)\\delta\_{kl}-\\frac{m}{2}\\big(\\delta\_{ik}a\_{lj}+\\delta\_{il}a\_{kj}\\big)-\\frac{m}{2}\\big(\\delta\_{kj}a\_{li}+\\delta\_{lj}a\_{ki}\\big)\\Big)\\&+\\frac{-tr(a)\\delta\_{kl}\\delta\_{ij}}{m}+\\frac{\\delta\_{ij}}{2}\\big(a\_{lk}+a\_{kl}\\big),\\end{align\*}\
$$\
\
(10.22)\
\
where _m_ is the real dimension of _M0,_ which is equal to 4 in this case. So when we take\
the inner product of Aijkl and Kijkl, the terms in K with either δkl or δij will give zero.\
Consequently,\
\
$$\
M\_{0}\
$$\
\
$$\
A\_{ijkl}\
$$\
\
$$\
K\_{ijkl}\
$$\
\
$$\
\\delta\_{kl}\
$$\
\
$$\
\\delta\_{ij}\
$$\
\
$$\
\\begin{aligned}\\sum\_{i,j,k,l}A\_{ijkl}K\_{ijkl}&=-\\frac{m}{16}\\sum\_{i,j,k,l}\\left(\\delta\_{ik}I\_{jl}^3+\\delta\_{jk}I\_{il}^3+\\delta\_{il}I\_{jk}^3+\\delta\_{jl}I\_{ik}^3\\right)\\&\\quad\\cdot\\left(\\delta\_{ik}a\_{lj}+\\delta\_{il}a\_{kj}+\\delta\_{kj}a\_{li}+\\delta\_{lj}a\_{ki}\\right)\\&=-\\frac{m}{4}\\sum\_{i,j,k,l}\\left(\\delta\_{ik}I\_{jl}^3+\\delta\_{jk}I\_{il}^3+\\delta\_{il}I\_{jk}^3+\\delta\_{jl}I\_{ik}^3\\right)\\cdot\\left(\\delta\_{ik}a\_{lj}\\right)\\&=-\\frac{m}{4}\\big(mI\_{jl}^3a\_{lj}+I\_{jl}^3a\_{lj}+I\_{jk}^3a\_{kj}\\big)\\&=-\\frac{m(m+2)}{4}tr(I^3\\circ a).\ \\end{aligned}\
$$\
\
(10.23)\
\
* * *\
\
Next, consider the term _r2(rα1 rα2)._ As a 2-tensor, this is written as\
\
$$\
r^{2}(r\\alpha\_{1}\\odot r\\alpha\_{2})\
$$\
\
$$\
r^{2}(r\\alpha\_{1}\\odot r\\alpha\_{2})=B\_{i j k l}x^{i}x^{j}d x^{k}d x^{l},\
$$\
\
(10.24)\
\
where\
\
$$\
B\_{i j k l}=\\frac{1}{4}\\big(I\_{i k}^{1}I\_{j l}^{2}+I\_{j k}^{1}I\_{i l}^{2}+I\_{i l}^{1}I\_{j k}^{2}+I\_{j l}^{1}I\_{i k}^{2}\\big).\
$$\
\
(10.25)\
\
Note that\
\
$$\
B\_{ijkl}=B\_{jikl}=B\_{ijlk},\
$$\
\
(10.26)\
\
$$\
\\sum\_{i}B\_{i i k l}=0,\
$$\
\
(10.27)\
\
$$\
\\sum\_{k}B\_{ijkk}=0.\
$$\
\
(10.28)\
\
Again, when we take the inner product of Bijkl and Kijkl\
or δij will give zero. Consequently,\
\
, the terms in K with either δkl\
\
$$\
B\_{ijkl}\
$$\
\
$$\
K\_{ijkl}\
$$\
\
$$\
\\delta\_{kl}\
$$\
\
$$\
\\delta\_{ij}\
$$\
\
$$\
\\begin{aligned}\\sum\_{i,j,k,l}B\_{ijkl}K\_{ijkl}&=-\\frac{m}{16}\\sum\_{i,j,k,l}\\left(I\_{ik}^1I\_{jl}^2+I\_{jk}^1I\_{il}^2+I\_{il}^1I\_{jk}^2+I\_{jl}^1I\_{ik}^2\\right)\\&\\quad\\cdot\\left(\\delta\_{ik}a\_{lj}+\\delta\_{il}a\_{kj}+\\delta\_{kj}a\_{li}+\\delta\_{lj}a\_{ki}\\right)\\&=-\\frac{m}{4}\\sum\_{i,j,k,l}\\left(I\_{ik}^1I\_{jl}^2+I\_{jk}^1I\_{il}^2+I\_{il}^1I\_{jk}^2+I\_{jl}^1I\_{ik}^2\\right)\\cdot\\left(\\delta\_{ik}a\_{lj}\\right)\\&=-\\frac{m}{4}\\big(I\_{jk}^1I\_{kl}^2a\_{lj}+I\_{kl}^1I\_{jk}^2a\_{lj}\\big)\\&=-\\frac{m}{4}\\big(I\_{jl}^3a\_{lj}-I\_{jl}^3a\_{lj}\\big)\\&=0.\ \\end{aligned}\
$$\
\
(10.29)\
\
We conclude that\
\
$$\
\\langle\\langle K,r^{2}(d r\\odot r\\alpha\_{3}+r\\alpha\_{1}\\odot r\\alpha\_{2})\\rangle\\rangle=-\\frac{m(m+2)}{4}t r(I^{3}\\circ a).\
$$\
\
(10.30)\
\
* * *\
\
Choosing a = I3, for example, this will be non-zero. Therefore, by Lemma 27 the\
quadratic germ _k2 cannot_ be extended to a kernel element _M0_ which is bounded at the\
conformal infinity of _M0._ A similar argument shows that the quadratic germ corresponding to _k3_ cannot be extended.\
\
$$\
a;=;I^{3}\
$$\
\
$$\
k\_{2}\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
M\_{0}\
$$\
\
$$\
k\_{3}\
$$\
\
However, this problem can be fixed as follows. Normalizing so that\
\
$$\
k\_{2}\\sim r^{2}(d r\\odot r\\alpha\_{3}+r\\alpha\_{1}\\odot r\\alpha\_{2}),\
$$\
\
(10.31)\
\
define\
\
$$\
\\tilde{k} _{2}=k_{2}-\\delta^{\*}\\left(r^{4}\\alpha\_{3}\\right).\
$$\
\
(10.32)\
\
The leading term is given by\
\
$$\
\\tilde{k} _{2}\\sim r^{2}(r\\alpha_{1}\\odot r\\alpha\_{2}).\
$$\
\
(10.33)\
\
It is easy to see that this germ is traceless, harmonic, divergence-free. It was just shown\
above that it is orthogonal to the space of tensors _S_ arising from a germ of a 1-form\
with linear coefficients defined in Equation 8.30. Consequently, from Lemma 27, this\
quadratic germ can indeed be extended to a kernel element of _P_ on the AHE orbifold\
which is bounded at infinity.\
\
Similarly for _k3,_ normalize so that\
\
$$\
k\_{3}\
$$\
\
$$\
k\_{3}=r^{2}\\bigl(-d r\\odot r\\alpha\_{2}+r\\alpha\_{1}\\odot r\\alpha\_{3}\\bigr),\
$$\
\
(10.34)\
\
and define\
\
$$\
\\tilde{k} _{3}=k_{2}+\\delta^{\*}\\left(r^{4}\\alpha\_{2}\\right).\
$$\
\
(10.35)\
\
* * *\
\
The leading term is given by\
\
$$\
\\tilde{k} _{3}\\sim r^{2}(r\\alpha_{1}\\odot r\\alpha\_{3}).\
$$\
\
(10.36)\
\
Again, it is easy to see that this germ is traceless, harmonic, and divergence-free. With\
a calculation similar to the above, it follows that it is orthogonal to the space of tensors\
_S_ arising from a germ of a 1-form with linear coefficients defined in Equation 8.30.\
Consequently, from Lemma 27, this quadratic germ can indeed be extended to a kernel\
element of _P_ on the AHE orbifold which is bounded at infinity.\
\
˜ ˜\
We conclude that, provided that _k2_ and _k3_ are replaced by _k2_ and _k3,_ respectively,\
then the desingularization argument in \[10, Section 12\] can be fixed using Lemma 27.\
\
$$\
k\_{2}\
$$\
\
$$\
\\tilde{k}\_{3}\
$$\
\
$$\
k\_{3}\
$$\
\
Of course, in the higher-dimensional case _m_ \> 4, this problem does not arise, since\
there is no rotational freedom, and it is only necessary to extend the germ corresponding\
to _k1._\
\
$$\
m>4.\
$$\
\
$$\
k\_{1}\
$$\
\
* * *\
\
## Bibliography\
\
\[1\] A. G. Ache and J. A. Viaclovsky, _Obstruction-flat asymptotically locally Euclidean metrics,_ Geom. Funct. Anal., 22 (2012), pp. 832–877.\
\
\[2\] M. T. Anderson, _On boundary value problems for Einstein metrics,_ Geom. Topol.,\
12 (2008), pp. 2009–2045.\
\
\[3\] L. Andersson and M. Dahl, _Scalar curvature rigidity for asymptotically locally_\
_hyperbolic manifolds,_ Ann. Global Anal. Geom., 16 (1998), pp. 1–27.\
\
\[4\] E. Aubry and C. Guillarmou, _Conformal harmonic forms, Branson-Gover_\
_operators and Dirichlet problem at infinity,_ J. Eur. Math. Soc. (JEMS), 13 (2011),\
pp. 911–957.\
\
\[5\] R. Bartnik, _The mass of an asymptotically flat manifold,_ Comm. Pure Appl.\
Math., 39 (1986), pp. 661–693.\
\
\[6\] L. Bérard-Bergery, _Sur de nouvelles varíet´es riemanniennes d’Einstein,_ in Institut Élie Cartan, 6, vol. 6 of Inst. Élie Cartan, Univ. Nancy, Nancy, 1982, pp. 1–60.\
\
\[7\] A. L. Besse, _Einstein manifolds,_ Classics in Mathematics, Springer-Verlag, Berlin,\
2008\. Reprint of the 1987 edition.\
\
\[8\] O. Biquard, _Asymptotically symmetric Einstein metrics,_ vol. 13 of SMF/AMS\
Texts and Monographs, American Mathematical Society, Providence, RI; Socíet´e\
Math´ematique de France, Paris, 2006. Translated from the 2000 French original by\
Stephen S. Wilson.\
\
* * *\
\
\[9\], _Continuation unique \`a partir de l’infini conforme pour les ḿetriques_\
_d’Einstein,_ Math. Res. Lett., 15 (2008), pp. 1091–1099.\
\
\[10\], _D´esingularisation de ḿetriques d’Einstein. I,_ Invent. Math., 192 (2013),\
pp. 197–252.\
\
\[11\] S. Brendle, _Blow-up phenomena for the Yamabe equation,_ J. Amer. Math. Soc.,\
21 (2008), pp. 951–979.\
\
\[12\] E. Calabi, _Ḿetriques k¨ahĺeriennes et fibŕes holomorphes,_ Ann. Sci. École Norm.\
Sup. (4), 12 (1979), pp. 269–294.\
\
\[13\] P. T. Chruściel, E. Delay, J. M. Lee, and D. N. Skinner, _Boundary_\
_regularity of conformally compact Einstein metrics,_ J. Differential Geom., 69 (2005),\
pp. 111–136.\
\
\[14\] C. R. Graham and J. M. Lee, _Einstein metrics with prescribed conformal infinity_\
_on the ball,_ Adv. Math., 87 (1991), pp. 186–225.\
\
\[15\] M. J. Gursky and J. A. Viaclovsky, _Critical metrics on connected sums of_\
_Einstein four-manifolds,_ Adv. Math., 292 (2016), pp. 210–315.\
\
\[16\] J. Han and J. A. Viaclovsky, _Deformation theory of scalar-flat K¨ahler ALE_\
_surfaces,_ arXiv.org:1605.05267, 2016.\
\
\[17\] D. D. Joyce, _Compact manifolds with special holonomy,_ Oxford Mathematical\
Monographs, Oxford University Press, Oxford, 2000.\
\
\[18\] S. Kobayashi and K. Nomizu, _Foundations of differential geometry. Vol. II,_\
\
* * *\
\
Wiley Classics Library, John Wiley & Sons, Inc., New York, 1996. Reprint of the\
1969 original, A Wiley-Interscience Publication.\
\
\[19\] W. Kühnel and H.-B. Rademacher, _Conformal completion of_ U(n)- _invariant_\
_Ricci-flat K¨ahler metrics at infinity,_ Z. Anal. Anwendungen, 16 (1997), pp. 113–117.\
Dedicated to the memory of Paul G¨unther.\
\
\[20\] J. M. Lee, _Fredholm operators and Einstein metrics on conformally compact manifolds,_ Mem. Amer. Math. Soc., 183 (2006), pp. vi+83.\
\
\[21\] R. Mazzeo, _The Hodge cohomology of a conformally compact metric,_ J. Differential\
Geom., 28 (1988), pp. 309–339.\
\
\[22\], _Elliptic theory of differential edge operators. I,_ Comm. Partial Differential\
Equations, 16 (1991), pp. 1615–1664.\
\
\[23\], _Unique continuation at infinity and embedded eigenvalues for asymptotically_\
_hyperbolic manifolds,_ Amer. J. Math., 113 (1991), pp. 25–45.\
\
\[24\] R. Mazzeo and M. Singer, _Some remarks on conic degeneration and bending of_\
_Poincaŕe-Einstein metrics,_ arXiv.org:0709.1498, 2007.\
\
\[25\] J. Morrow and K. Kodaira, _Complex manifolds,_ AMS Chelsea Publishing,\
Providence, RI, 2006. Reprint of the 1971 edition with errata.\
\
\[26\] P. Morteza and J. A. Viaclovsky, _The Calabi metric and desingularization of_\
_Einsten orbifolds,_ to appear in the Journal of the European Mathematical Society.\
\
\[27\] D. N. Page and C. N. Pope, _Inhomogeneous Einstein metrics on complex line_\
_bundles,_ Classical Quantum Gravity, 4 (1987), pp. 213–225.