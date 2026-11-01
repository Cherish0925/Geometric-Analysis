---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Contents]

We restricted the above discussion to dimension 4 for simplicity, since quadratic
functionals are scale-invariant in that dimension. In dimensions other than four, if
_F_ denotes a quadratic curvature functional, then the volume-normalized functional
˜\[\
\
(7.31)\
\
$$\
\\tilde{\\mathcal{F}}\[g\]=V o l(g)^{\\frac{4}{n}-1}\\mathcal{F}\[g\].\
$$\
\
is scale-invariant. Many of the results stated above also have analogues in other\
dimensions. For example, Corollary 7.5 has an analogue in higher dimensions:\
\
Theorem 7.13 (\[GV15\]). _Let (M,g) be a sphere, space form, or complex pro-_\
jective space, normalized so that Ric(g)=(n − 1)g. Then there exists a C2,α-\
_neighborhood U of g such that if g˜ ∈ U with Ric(˜g_) _≤ (n−1)˜g, then Vol(˜g) ≥ Vol(g_)\
with equality if and only if g˜ = φ∗g for some diffeomorphism φ : M → M.\
\
$$\
Ric(g)=(n-1)g\
$$\
\
$$\
C^{2,\\alpha}\
$$\
\
$$\
f\\tilde{g}\\in U\
$$\
\
$$\
Ric(\\tilde{g})\\leq(n-1)\\tilde{g}\
$$\
\
$$\
\\mathrm{Vol}(\\tilde{g})\\geq\\mathrm{Vol}(g)\
$$\
\
$$\
\\tilde{\\mathbf{\\nabla}g}=\\phi^{\*}g\
$$\
\
For the proof, and for other examples of rigidity and stability of Einstein metrics\
for quadratic curvature functionals, we refer the reader to \[GV15\].\
\
We mention that quadratic functionals in dimension 3 were considered by Anderson in \[And97, And01\]. Also, critical points of the functional F˜σ2 (defined\
above in (2.21)) were studied in dimension 3 in \[GV01\]. For rigidity results involving other types of functionals see \[MØ13\].\
\
$$\
\\tilde{\\mathcal{F}} _{\\sigma_{2}}\
$$\
\
* * *\
\
# ALE metrics and orbifold limits\
\
### 1\. Ricci-flat ALE metrics\
\
In order to understand limits of Einstein metrics, one one first have some understanding of a class of complete non-compact metrics, which are defined as follows.\
\
Definition 8.1. A complete Riemannian manifold (X4,g) is called asymptotically\
_locally Euclidean_ or _ALE_ of order _τ_ if there exists a finite subgroup Γ _⊂_ SO(4)\
acting freely on _S3_ and a diffeomorphism _ψ_ : _X \ K →_ (R4 \\*\\* B(0,R))/Γ where _K_\
is a compact subset of _X,_ and such that under this identification,\
\
$$\
(X^{4},g)\
$$\
\
$$\
\\Gamma\\subset SO(4)\
$$\
\
$$\
S^{3}\
$$\
\
$$\
\\psi:X\\setminus K\\to(\\mathbb{R}^{4}\\setminus B(0,R))/\\Gamma\
$$\
\
$$\
X,\
$$\
\
(8.1)\
\
$$\
(\\psi\_{\*}g) _{i j}=\\delta_{i j}+O(\\rho^{-\\tau}),\
$$\
\
(8.2)\
\
$$\
\\partial^{\|k\|}(\\psi\_{\*}g)\_{i j}=O(\\rho^{-\\tau-k}),\
$$\
\
for any partial derivative of order _k,_ as _r →∞,_ where _ρ_ is the distance to some\
fixed basepoint.\
\
$$\
k,\
$$\
\
$$\
r\\to\\infty\
$$\
\
$$\
\\rho\
$$\
\
Note that this definition is really just the same as Definition 2.7, with the\
addition of a group at infinity:\
\
#### 1.1. Eguchi-Hanson metric\
\
We next recall the Eguchi-Hanson metric, which was the first example of a nontrivial Ricci-flat ALE space \[EH79\]. It is given by\
\[\]\
\
(8.3)\
\
$$\
g\_{\\operatorname{EH}}=\\frac{d r^{2}}{1-r^{-4}}+r^{2}\\Big\[\\sigma\_{1}^{2}+\\sigma\_{2}^{2}+(1-r^{-4})\\sigma\_{3}^{2}\\Big\],\
$$\
\
# where _r_ is a radial coordinate, and _{σ1,σ2,σ3}_ is a left-invariant coframe on _S3_ (viewed as the Lie group SU(2)). This has an apparent singularity at _r_ = 1, so redefine the radial coordinate to be ˆ2r = _r2 −_ 1, and attach a CP1 at _ˆr_ = 0\. After taking a quotient by Z2, the metric then extends smoothly over the added CP1, is Ricci-flat, ALE at infinity of order 4, and is diffeomorphic to O(−2) ∼ T ∗S2.\
\
This space is hyperk¨ahler, that is, there are three independent complex structures\
denoted by _I,J,_ and _K_ satisfying the quaternion relations\
\
$$\
S^{3}\
$$\
\
$$\
\\left{\\sigma\_{1},\\sigma\_{2},\\sigma\_{3}\\right}\
$$\
\
$$\
r=1\
$$\
\
$$\
\\hat{r}^{2}=r^{2}-1\
$$\
\
$$\
\\mathbb{C}\\mathbb{P}^1\
$$\
\
$$\
\\hat{r}=0\
$$\
\
$$\
\\mathbb{Z}\_2\
$$\
\
$$\
\\mathbb{C}\\mathbb{P}^1\
$$\
\
$$\
\\mathcal{O}(-2)\\cong T^\*S^2\
$$\
\
$$\
I,J,\
$$\
\
$$\
I^{2}=J^{2}=K^{2}=I J K=-1.\
$$\
\
(8.4)\
\
Denote the corresponding K¨ahler forms by ωI,ωJ,ωK, which are 3 linearly independent harmonic self-dual 2-forms.\
\
$$\
\\omega\_{I},\\omega\_{J},\\omega\_{K}\
$$\
\
1\
Since this space is non-compact, let us look at HE,−(X,g), which we define\
to be decaying infinitesimal Einstein deformations, that is, those h ∈ S2(T ∗X)\
satisfying all the conditions in (4.3), and also which satisfy h = O(r−) for some\
\
> 0. Using the isomorphism S02(T ∗M) = Λ2+ ⊗Λ2−, it follows from the discussions\
>    1\
>    in Lecture 6 that HE,−(X,g) has a basis\
\
$$\
H\_{E,-}^{1}(X,g)\
$$\
\
$$\
h\\in S^{2}(T^{\*}X)\
$$\
\
$$\
\\epsilon>0\
$$\
\
$$\
h=O(r^{-\\epsilon})\
$$\
\
$$\
S\_{0}^{2}(T^{\*}M)=\\Lambda\_{+}^{2}\\otimes\\Lambda\_{-}^{2}\
$$\
\
$$\
H\_{E,-}^{1}(X,g)\
$$\
\
(8.5)\
\
$$\
{\\omega\_{I}\\otimes\\omega^{-},\\omega\_{J}\\otimes\\omega^{-},\\omega\_{K}\\otimes\\omega^{-}},\
$$\
\
* * *\
\
$$\
\\omega^{-}\
$$\
\
where ω− is a non-trivial L2 harmonic 2-form, see \[Pag78b\]. Consequently,\
\
$$\
L^{2}\
$$\
\
(8.6)\
\
$$\
\\dim(H\_{E,-}^{1}(X,g))=3.\
$$\
\
However, the Eguchi-Hanson metric is known to be rigid (up to scaling) as an\
Einstein ALE metric. This means that these infinitesimal deformations do not\
integrate to non-trivial Einstein deformations. It turns out that these elements can\
in fact be written as Lie derivatives, and can be understood as gluing parameters\
for a certain gluing problem which we will discuss in more detail below.\
\
#### 1.2. Hyperk¨ahler ALE metrics\
\
After the Eguchi-Hanson metric was found, Gibbons-Hawking wrote down a metric\
ansatz depending on the choice of _n_ monopole points in R3, giving an anti-selfdual ALE hyperk¨ahler metric with group _Z/nZ_ at infinity, which are called multi-\
Eguchi-Hanson metrics \[GH78, Hit79\]. In 1989, Kronheimer then classified all\
hyperk¨ahler ALE spaces in dimension 4, \[Kro89a, Kro89b\]. To describe these,\
we consider the following subgroups of SU(2):\
\
$$\
\\mathbb{Z}/n\\mathbb{Z}\
$$\
\
$$\
\\mathbb{R}^{\\bar{3}}\
$$\
\
• Type An,n ≥ 1: Γ the cyclic group Zn+1,\
\
(8.7)\
\
$$\
A\_{n},n\\geq1;\
$$\
\
$$\
\\mathbb{Z}\_{n+1}\
$$\
\
$$\
(z\_{1},z\_{2})\\mapsto(e^{2\\pi i p/(n+1)}z\_{1},e^{-2\\pi i p/(n+1)}z\_{2}),0\\leq p\\leq n.\
$$\
\
acting on R4, which is identified with C2 via the map\
\
$$\
\\mathbb{C}^2\
$$\
\
$$\
\\mathbb{R}^4\
$$\
\
$$\
(x\_{1},y\_{1},x\_{2},y\_{2})\\mapsto(x\_{1}+i y\_{1},x\_{2}+i y\_{2})=(z\_{1},z\_{2}).\
$$\
\
(8.8)\
\
Writing a quaternion _q ∈_ H as _α_ \+ _jβ_ for _α,β ∈_ C, we can also describe\
the action as generated by e2πi/(n+1), acting on the left.\
\
$$\
q\\in\
$$\
\
$$\
\\alpha+j\\beta\
$$\
\
$$\
\\alpha,\\beta\\in\\mathbb{C}\
$$\
\
$$\
e^{2\\pi i/(n+\\stackrel{\\circ}{1)}}\
$$\
\
• Type Dn,n ≥ 3: Γ the binary dihedral group D∗n−2 of order 4(n −2). This\
is generated by eπi/(n−2) and j, both acting on the left.\
\
$$\
D\_{n},n\\geq3;\
$$\
\
$$\
\\mathbb{D}\_{n-2}^{\*}\
$$\
\
$$\
4(n-2)\
$$\
\
$$\
e^{\\pi i/(n-2)}\
$$\
\
$$\
j,\
$$\
\
• Type E6 : Γ = T∗\
of A(4).\
\
, the binary tetrahedral group of order 24, double cover\
\
$$\
E\_{6}:\\Gamma=\\mathbb{T}^{\*}\
$$\
\
$$\
A(4)\
$$\
\
_•_ Type _E7_ : Γ = O\
of S(4).\
\
∗, the binary octohedral group of order 48, double cover\
\
$$\
E\_{7}:\\Gamma=\\mathbb{O}^{\*}\
$$\
\
$$\
S(4)\
$$\
\
• Type E8 : Γ = I∗, the binary icosahedral group of order 120, double cover\
of A(5).\
\
$$\
E\_{8}:\\Gamma=\\mathbb{I}^{\*}\
$$\
\
$$\
A(5)\
$$\
\
We will not go into details about Kronheimer’s construction, but just briefly\
discuss the identification of the space of decaying infinitesimal Einstein deformations, given by the argument in \[Biq13a, Proposition 1.1\]. The operator ∆L acting\
on transverse-traceless tensors can be identified with the operator d−d∗− where\
∼\
\
$$\
\\Delta\_{L}\
$$\
\
))(8.9)\
\
$$\
\\tilde{d} _{-}:\\hat{\\Omega}^{1}\\otimes\\hat{\\Omega}_{+}^{2}\\to\\hat{\\Omega} _{-}^{2}\\otimes\\hat{\\Omega}_{+}^{2}\\cong\\Gamma(\\tilde{S}\_{0}^{2}(T^{\*}X))\
$$\
\
$$\
d\_{-}d\_{-}^{\*}\
$$\
\
is the exterior derivative. Since Ω2+ has a basis of parallel sections {ωI,ωJ,ωK},\
the proposition follows since the L2-cohomology H2(2)(X) is isomorphic to the usual\
cohomology H2(X) \[Car98\]. Consequently, the formal dimension of the moduli\
space of any such metric is 3b2−. Note by the Weitzenb¨ock formulas given in Lecture 6, these deformations are equivalent to decaying infinitesimal anti-self-dual\
deformations, see \[Via13b\]. Kronheimer has shown that the actual dimension of\
the moduli space of hyperk¨ahler metrics on these spaces is 3b2− − 3, which implies\
that there are infinitesimal deformations which are not integrable. As in the case\
\
$$\
\\Omega\_{+}^{2}\
$$\
\
$$\
{\\omega\_{I},\\omega\_{J},\\omega\_{K}}\
$$\
\
$$\
H\_{(2)}^{2}(X)\
$$\
\
$$\
H^{2}(X)\
$$\
\
$$\
3b\_{2}^{-}\
$$\
\
$$\
3b\_{2}^{-}-3\
$$ of the Eguchi-Hanson metric, these can also be understood as gluing parameters.\
The properties of these spaces are summarized in Table 8.1.\
\
Table 8.1. Invariants of hyperk¨ahler ALE spaces.\
\
| Type | (\\Gamma) | (\|\\Gamma\|) | b2- | χ |\
| --- | --- | --- | --- | --- |\
| An, n ≥ 1 | (\\mathbb{Z}\_{n+1}) | n+1 | n | n+1 |\
| Dm, m ≥ 3 | (\\mathbb{D}\_{m-2}^\*) | 4(m-2) | m | m+1 |\
| E6 | (\\mathbb{T}^\*) | 24 | 6 | 7 |\
| E7 | (\\mathbb{O}^\*) | 48 | 7 | 8 |\
| E8 | (\\mathbb{I}^\*) | 120 | 8 | 9 |\
\
$$\
b\_{2}^{-}\
$$\
\
$$\
A\_{n},n\\geq1\
$$\
\
$$\
\\chi\
$$\
\
$$\
\\overline{\\mathbb{Z}\_{n+1}}\
$$\
\
$$\
n+1\
$$\
\
$$\
D\_{m},m\\geq3\
$$\
\
$$\
n\
$$\
\
$$\
E\_{6}\
$$\
\
$$\
\\mathbb{D}\_{m-2}^{\*}\
$$\
\
$$\
\\mathbb{T}^\*\
$$\
\
$$\
n+1\
$$\
\
$$\
4(m-2)\
$$\
\
$$\
E\_{7}\
$$\
\
$$\
m+1\
$$\
\
$$\
\\textcircled{O}^{\*}\
$$\
\
$$\
E\_{8}\
$$\
\
$$\
\\mathbb{I}^\*\
$$\
\
To close this brief discussion of hyperk¨ahler metrics, we note here the following\
interesting conjecture due to Bando, Kasue, and Nakajima \[BKN89\]:\
\
Conjecture 8.2. _If (M,g) is a simply-connected Ricci-flat ALE space in dimension_\
_four, then g is hyperk¨ahler._\
\
$$\
\\textit{If}\\left(M,g\\right)\
$$\
\
The following result, which is joint work of the author and Michael Lock, shows\
that the conjecture is true, provided one restricts to the diffeomorphism types of\
minimal resolutions of C2/Γ, or any iterated blow-up thereof.\
\
$$\
\\mathbb{C}^2/\\Gamma,\
$$\
\
Theorem 8.3 (\[LV15b\]). _Let_ Γ _⊂_ U(2) _be a finite subgroup which acts freely on_\
S3, and let X be diffeomorphic to the minimal resolution of C2/Γ, or any iterated\
_blow-up thereof. If g is a Ricci-flat ALE metric on X, then_ Γ _⊂_ SU(2) _and g is_\
_hyperk¨ahler._\
\
$$\
\\Gamma\\subset\\mathrm{U}(2)\
$$\
\
$$\
S^{3}\
$$\
\
$$\
\\mathbb{C}^2/\\Gamma\
$$\
\
$$\
g\
$$\
\
$$\
\\Gamma\\subset SU(2)\
$$\
\
Remark 8.4. There are other interesting complete Einstein metrics with different asymptotics at infinity, known as “ALF”, “ALG”, and “ALH” gravitational\
instantons. We will not have time to discuss these, and refer the reader to \[BM11,\
Min10\] for a nice discussion of these types of metrics. There are also many interesting examples of gravitational instantons which have non-integral volume growth\
exponent \[Hei12\].\
\
$$\
\`\`\\mathrm{ALF}''\
$$\
\
$$\
\\text{"}ALG\\text{"}\
$$\
\
### 2\. Non-collapsed limits of Einstein metrics\
\
The results in Lecture 4 give a local description of the moduli space near a fixed\
Einstein metric. One would also like to understand global properties of the moduli\
space of Einstein metrics, for example, what are the possible limits of sequences of\
Einstein metrics?\
\
Definition 8.5. A Riemannian orbifold (M4,g) is a topological space which is\
a smooth manifold of dimension 4 with a smooth Riemannian metric away from\
finitely many singular points. At a singular point _p, M_ is locally diffeomorphic\
to a cone C on S3/Γ, where Γ ⊂ SO(4) is a finite subgroup acting freely on S3.\
Furthermore, at such a singular point, the metric is locally the quotient of a smooth\
Γ-invariant metric on _B4_ under the orbifold group Γ.\
\
$$\
(M^{4},g)\
$$\
\
$$\
S^{3}/\\Gamma,\
$$\
\
$$\
\\Gamma\\subset SO(4)\
$$\
\
$$\
p,\
$$\
\
$$\
\\mathcal{C}\
$$\
\
$$\
S^{3}\
$$\
\
$$\
B^{4}\
$$\
\
In the non-collapsing case, the following is known, due to Anderson, Bando-\
Kasue-Nakajima, and Tian.\
\
* * *\
\
Theorem 8.6 (\[And89\], \[BKN89\], \[Tia90\]). Let (Mi,gi) sequence of Einstein\
_manifolds of dimension_ 4 _satisfying_\
∫\
\
$$\
(M\_{i},g\_{i})\
$$\
\
(8.10)\
\
$$\
\\int\_{M\_{i}}\|R m\_{g\_{i}}\|^{2}d V\_{g\_{i}}<\\Lambda,\\operatorname{diam}(g\_{i})<D,V o l(g\_{i})>V>0.\
$$\
\
_Then for a subsequence {j}⊂{i},_\
\
$$\
{j}\\subset{i}\
$$\
\
(8.11)\
\
$$\
(M\_{j},g\_{j})\\xrightarrow{\\operatorname{C h e e g e r-G r o m o v}}(M\_{\\infty},g\_{\\infty}),\
$$\
\
_where_ ( _M_ ∞ _,g_ ∞) _is an orbifold with finitely many singular points._\
\
$$\
\\left(M\_{\\infty},g\_{\\infty}\\right)\
$$\
\
The above convergence is in the Cheeger-Gromov sense which means that the\
metrics converge in the Gromov-Hausdorff sense to the limit space as a metric\
space, but away from the singular points, the convergence is moreover smooth (after\
pulling back by diffeomorphisms). Rescaling such a sequence to have bounded\
curvature near a singular point and taking a pointed limit yields Ricci-flat ALE\
spaces, also called “bubbles”. This bubbling description can be refined; what we just\
described produces a “deepest bubble”. Choosing different scalings can yield a tree\
of ALE Ricci-flat orbifolds at a singular point, see \[Nak88\] for a nice description\
of this process.\
\
#### 2.1. K3 example\
\
Eguchi-Hanson metrics arise as bubbles for certain sequences of Calabi-Yau metrics\
on K3, and was suggested by \[KT87\]:\
\
Example 8.7. There exists a sequence of Ricci-flat metrics gi on K3 satisfying\
4\
\
$$\
g\_{i}\
$$\
\
(8.12)\
\
$$\
(K3,g\_{i})\\longrightarrow(T^{4}/{\\pm1},g\_{\\mathrm{flat}}).\
$$\
\
At each of the 16 singular points, an Eguchi-Hanson metric on T ∗S2 “bubbles off ”.\
\
$$\
T^{\*}S^{2}\
$$\
\
$$\
o\\textit{ff}\
$$\
\
Note that since each Eguchi-Hanson metric has 3 infinitesimal Einstein deformations, and the torus has 10 flat deformations, modulo scaling the parameter\
count is 57, which is in nice agreement with the count made in Section 3 of Lecture 6. See \[Pag78b\] for a nice heuristic description of this. Also see \[LS94\] for a\
rigorous construction of a Calabi-Yau metric by anti-self-dual gluing methods, and\
the note of Donaldson \[Don10\] for a rigorous construction using K¨ahler-Einstein\
techniques.\
\
Remark 8.8. There is another very interesting limit of Calabi-Yau metrics on K3,\
known as the “large complex structure limit” \[GW00\]. A sequence of these metrics\
collapses to a limiting 2-sphere, so the limit is not described by Theorem 8.6. Away\
from 24 points, the sequence collapses with bounded curvature, and gives a nice\
illustration of the-regularity theorem of Cheeger-Tian \[CT06\].\
\
#### 2.2. Desingularization\
\
We next ask the follow question:\
\
_•_ Can you reverse this process? That is, can you start with an Einstein\
orbifold, “glue on” hyperk¨ahler bubbles at the singular points, and resolve\
to a smooth Einstein metric?\
\
The “answer” is:\
\
_•_ In general, the answer is “no”, since this gluing problem is obstructed;\
there are always decaying infinitesimal Einstein deformations of non-trivial\
Ricci-flat ALE spaces.\
\
* * *\
\
In the ASD case, the relevant operator maps between different bundles, and\
the index is not necessarily zero. However, the index is always zero in the Einstein\
case, so this makes the problem much more difficult. We remark that sometimes,\
Einstein metrics _can_ be found by gluing techniques, but only when using some extra\
structure. As mentioned above, Calabi-Yau metrics on K3 can be produced using\
ASD gluing techniques \[LS94\], or K¨ahler-Einstein techniques \[Don10\]. For the _G2_\
and _Spin(7_) cases, see \[Joy96, Joy99\].\
\
#### 2.3. Biquard’s Theorem\
\
$$\
G\_{2}\
$$\
\
We next discuss a beautiful result which says that the answer to the above question\
is “yes” in a certain case. The setting is a class of complete non-compact Einstein\
metrics with negative Einstein constant. If _M4_ is a compact manifold with boundary _∂M,_ then a metric _g_ on _M4_ is said to be _conformally compact_ if _˜g_ = _ρ2g_ has\
some regularity (e.g., Ḧolder) up to the boundary, where _ρ_ is a defining function for\
the boundary which satisfies ρ−1(0) = ∂M and dρ 6= 0 on ∂M. If \|dp\|g˜= 1, then\
_g_ limits to a hyperbolic metric as _ρ →_ 0, such a metric is called _asymptotically hyperbolic._ If it is in addition Einstein (necessarily with negative Einstein constant),\
then _(M,g)_ is called _asymptotically hyperbolic Einstein,_ or AHE for short. We note\
that there is an induced conformal class on the boundary manifold at infinity. This\
definition should be thought of as a generalization of the hyperbolic ball, with the\
conformal class of the round sphere at infinity. Biquard’s result is the following.\
\
$$\
M^{4}\
$$\
\
$$\
M^{4}\
$$\
\
$$\
\\tilde{g}=\\rho^{2}g\
$$\
\
$$\
\\rho\
$$\
\
$$\
\\rho^{-1}(0)=\\partial M\
$$\
\
$$\
d\\rho\\ne0\
$$\
\
$$\
\|dp\|\_{\\tilde{g}}=1\
$$\
\
$$\
\\rho\\to0\
$$\
\
Theorem 8.9 (Biquard \[Biq13a\]). Let (M4,g) be an AHE metric with a Z/2Z\
orbifold singularity at p ∈ M. If (M4,g) is rigid (i.e., g admits no nontrivial\
_infinitesimal Einstein deformations), then the singularity can be resolved to a AHE_ _metric by gluing on an Eguchi-Hanson metric if and only if_\
\
$$\
(M^{4},g)\
$$\
\
$$\
a\ \\mathbb{Z}/2\\mathbb{Z}\
$$\
\
$$\
p\\in M\
$$\
\
$$\
:(M^{4},g)\
$$\
\
$$\
\\textit{if}\
$$\
\
(8.13)\
\
$$\
\\det\\left(\\mathcal{R}^{+}\\right)(p)=0,\
$$\
\
where R+ is the upper-left 3 × 3 block in (5.14).\
\
$$\
\\mathcal{R}^{+}\
$$\
\
$$\
3\\times3\
$$\
\
As we discussed above, the Eguchi-Hanson metric admits a 3-dimensional space\
of infinitesimal Einstein deformations, so this gluing problem is obstructed. One\
of these deformations corresponds to a scaling parameter, and the other two correspond to rotations in SO(4)/U(2). Biquard is able to overcome these obstructions\
using the freedom to perturb the boundary conformal class of the AH Einstein\
metric.\
\
$$\
SO(4)/U(2)\
$$\
\
Recently, Biqard has given a generalization of Theorem 8.9 to allow orbifolds\
with more general ADE-type singularities, see \[Biq13b\] for the precise statement\
of this extension.\
\
### 3\. Bt-flat metrics\
\
We next return to critical metrics of quadratic curvature functionals. We will be\
interested in the functional\
∫ ∫\
\
$$\
\\mathcal{B} _{t}\[g\]=\\int_{M}\|W\_{g}\|^{2}d V\_{g}+t\\int\_{M}R\_{g}^{2}d V\_{g}.\
$$\
\
Remark 8.10. From the Chern-Gauss-Bonnet Theorem 5.4, this is really the most\
general quadratic functional in dimension 4, up to scaling. We have chosen to\
normalize this way to take advantage of the conformal invariance of _W._\
\
* * *\
\
The Euler-Lagrange equations of\
\
Bt are given by\
\
(8.14)\
\
$$\
\\mathcal{B}\_{t}\
$$\
\
$$\
B^{t}\\equiv B+t C=0,\
$$\
\
where _B_ is the _Bach tensor_ defined by (5.6)\
(\
\
(8.15)\
\
$$\
B\_{i j}\\equiv-4\\Big(\\nabla^{k}\\nabla^{l}W\_{i k j l}+\\frac{1}{2}R^{k l}W\_{i k j l}\\Big),\
$$\
\
and _C_ is the tensor defined by (5.8)\
\
(8.16)\
\
$$\
C\_{i j}=2\\nabla\_{i}\\nabla\_{j}R-2(\\Delta R)g\_{i j}-2R R\_{i j}+\\frac{1}{2}R^{2}g\_{i j}.\
$$\
\
From conformal invariance of the functional _W,_ it follows that the Bach-tensor is\
conformally invariant. We will refer to such a critical metric as a Bt-flat metric.\
Note that any Einstein metric is critical for Bt, but there are in fact non-Einstein\
Bt-flat metrics, as we shall see.\
\
$$\
\\mathcal{W},\
$$\
\
$$\
B^{t}\
$$\
\
$$\
\\mathcal{B}\_{t}\
$$\
\
$$\
B^{t\_{1}}\
$$\
\
For _t 6=_ 0, by taking a trace of the E-L equations, it follows that\
\
$$\
t\\neq0\
$$\
\
(8.17)\
\
$$\
\\Delta R=0.\
$$\
\
If _M_ is compact, this implies _R_ =\
equivalent to\
\
constant. Consequently, the Bt-flat condition is\
\
$$\
B^{t}-flat\
$$\
\
(8.18)\
\
$$\
\\boldsymbol{B}=2t\\boldsymbol{R}\\cdot\\boldsymbol{E},\
$$\
\
where _E_ denotes the traceless Ricci tensor. That is, the Bach tensor is a constant\
multiple of the traceless Ricci tensor, which is indeed a natural generalization of\
the Einstein condition.\
\
$$\
E\
$$\
\
$$\
B^{t}-flat\
$$\
\
#### 3.1. Bt-flat ALE metrics\
\
Of course, all of the hyperk¨ahler ALE spaces described above are also Bt-flat, but\
there are many more non-Einstein examples.\
\
$$\
B^{t}-flat\
$$\
\
A large source of examples is the following. If _(M,g)_ is Bach-flat and has\
positive scalar curvature, then we can convert _(M,g)_ into an asymptotically flat\
(AF) metric\
\
$$\
(M,g)\
$$\
\
$$\
(M,g)\
$$\
\
$$\
(N,g\_N)=(M\\setminus{p},G^2g)\
$$\
\
using the Green’s function for the conformal Laplacian _G_ based at _p._ Since _(M,g)_ is\
Bach-flat, then (N,gN) is also Bach-flat (from conformal invariance) and scalar-flat\
(since we used the Green’s function). Consequently, gN is Bt-flat for all t ∈ R. This\
gives a large family of examples of non-trivial asymptotically flat Bt-flat metrics,\
in contrast to the Ricci-flat case.\
\
$$\
p.\
$$\
\
$$\
(M,g)\
$$\
\
$$\
(N,g\_N)\
$$\
\
$$\
g\_{N}\
$$\
\
$$\
B^{t}\
$$\
\
$$\
t\\in\\mathbb{R}\
$$\
\
$$\
B^{t}.\
$$\
\
By taking the sum of Green’s functions based at several points, one can also\
obtain many examples with several ends. In the special case of the sphere, with\
two points, one obtains the Euclidean Schwarzschild metric\
()2\
\
$$\
g=\\left(1+\\frac{m}{r^2}\\right)^2g\_0,\
$$\
\
(8.19)\
\
where _g0_ is the Euclidean metric. This metric plays a very important rˆole in the\
Riemannian Penrose Inequality, see for example \[Bra01, BL09\].\
\
$$\
g\_{0}\
$$\
\
Another family of non-trivial examples is the following. In \[LeB88\], LeBrun\
presented the first known examples of scalar-flat ALE spaces of negative mass, which gave counterexamples to extending the positive mass theorem to ALE spaces. We\
briefly describe these as follows. Define\
\[\]\
\
(8.20)\
\
$$\
g\_{\\mathrm{LB}}=\\frac{d r^{2}}{1+A r^{-2}+B r^{-4}}+r^{2}\\Big\[\\sigma\_{1}^{2}+\\sigma\_{2}^{2}+\\big(1+A r^{-2}+B r^{-4}\\big)\\sigma\_{3}^{2}\\Big\],\
$$\
\
where r is a radial coordinate, {σ1,σ2,σ3} is a left-invariant coframe on S3, and\
_A_ = _n −_ 2, _B_ = 1 _− n._ There is an apparent singularity at _r_ = 1, so redefine the\
radial coordinate to be rˆ2 = _r2 −_ 1, and attach a CP1 at _rˆ_ = 0\. After taking a\
quotient by Zn, with action given by the diagonal action\
\
$$\
\\left{\\sigma\_{1},\\sigma\_{2},\\sigma\_{3}\\right}\
$$\
\
$$\
S^{3}\
$$\
\
$$\
A=n-2,B=1-n\
$$\
\
$$\
r=1\
$$\
\
$$\
\\hat{r}^{2}=r^{2}-1\
$$\
\
$$\
\\mathbb{C}\\mathbb{P}^1\
$$\
\
$$\
\\hat{r}=0\
$$\
\
$$\
\\mathbb{Z}\_{n}\
$$\
\
(8.21)\
\
$$\
(z\_{1},z\_{2})\\mapsto e^{2\\pi i p/n}(z\_{1},z\_{2}),\\quad0\\leq p\\leq n-1,\
$$\
\
the metric then extends smoothly over the added CP1, is ALE at infinity, and\
is diffeomorphic to _O(−n)._ The mass (as defined in (2.15)) is computed to be\
_−2(n −_ 2), which is negative when _n_ \> 2\. These metrics are scalar-flat K¨ahler (so\
are anti-self-dual, and thus Bach-flat), and satisfy b2− = 1,τ = −1, and χ = 2.\
\
$$\
\\mathbb{C}\\mathbb{P}^1\
$$\
\
$$\
\\mathcal{O}(-n)\
$$\
\
$$\
-2(n-2)\
$$\
\
$$\
n>2\
$$\
\
$$\
b\_{-}^{2}=1,\\tau=-1\
$$\
\
$$\
\\chi=2\
$$\
\
In 2004, Calderbank and Singer produced many examples of toric ALE antiself-dual metrics, which are moreover scalar-flat K¨ahler, and have cyclic groups at\
infinity contained in U(2) \[CS04\]. In 2014, the author, jointly with Michael Lock,\
produced new examples of ALE scalar-flat K¨ahler metrics with group at infinity\
_any_ finite subgroup of U(2) acting freely on _S3_ \[LV14\].\
\
$$\
S^{3}\[LV14\]\
$$\
\
### 4\. Non-collapsed limits of Bt-flat metrics\
\
$$\
B^{t}-flat\
$$\
\
For t 6= 0, the Bt-flat equation can be rewritten as\
\
$$\
t\\neq0\
$$\
\
$$\
B^{t}\
$$\
\
(8.22)\
\
$$\
\\Delta R i c=R m\*R i c.\
$$\
\
If _t_ = 0, equation (8.22) is satisfied provided one assumes in addition that _g_ has\
constant scalar curvature. With slightly different geometric assumptions, a similar\
orbifold-compactness theorem as in the Einstein case holds for sequences of metrics\
satisfying (8.22):\
\
$$\
g\
$$\
\
$$\
t=0\
$$\
\
Theorem 8.11 (Tian-Viaclovsky \[TV05a, TV05b, TV08\]). Let (Mi,gi) be a\
_sequence of_ 4- _dimensional manifolds satisfying_ (8.22) _and_\
∫\
\
$$\
(M\_{i},g\_{i})\
$$\
\
(8.23)\
\
$$\
\\int\_{M\_{i}}\|R m\_{g\_{i}}\|^{2}d V\_{g\_{i}}<\\Lambda,{V o l}(B(q,s))>V s^{4}>0,b\_{1}(M\_{i})<B,\
$$\
\
_for all s ≤ diam(M)/2. Then for a subsequence {j}⊂{i},_\
\
$$\
s\\leq{d i a m}(M)/2\
$$\
\
$$\
{j}\\subset{i}\
$$\
\
(8.24)\
\
$$\
(M\_{j},g\_{j})\\xrightarrow{\\operatorname{C h e e g e r-G r o m o v}}(M\_{\\infty},g\_{\\infty}),\
$$\
\
$$\
\\left(M\_{\\infty},g\_{\\infty}\\right)\
$$\
\
_where_ ( _M_ ∞ _,g_ ∞) _is a multi-fold satisfying_ (8.22), _with finitely many singular points._\
\
Similar to the Einstein case, rescaling such a sequence to have bounded curvature near a singular point yields ALE metrics satisfying (8.22). An important\
difference with the Einstein case is that the ALE spaces can have multiple ends\
(this is ruled out in the Einstein case by the Cheeger-Gromoll splitting theorem).\
Thus singular points are more general in that multiple orbifold cones can touch at\
a singular point, thus the terminology “multi-fold”. Another difference is that a\
smooth point of the limit can in fact be a singular point of convergence, this cannot\
happen in the Einstein case (by Bishop’s volume comparison theorem).\
\
The key point in this theorem is the following related volume growth theorem:\
\
* * *\
\
Theorem 8.12 (Tian-Viaclovsky \[TV08\]). _Let (M,g) be a metric satisfying_ (8.22)\
_on a smooth, complete four-dimensional manifold M with_\
∫\
\
(8.25)\
\
$$\
\\int\_{M}\|{\\operatorname{Rm}} _{g}\|^{2}d V_{g}\\leq\\Lambda,\
$$\
\
_for some constant Λ._\
\
_Assume that_\
\
(8.26)\
\
$$\
\\begin{aligned}{\\operatorname{Vol}(B(q,s))}&{{}\\geq V\_{0}s^{4},\\quad\\mathit{f o r~a l l}\\quad q\\in M,\\quad\\mathit{and}\\quad s\\leq{d i a m}(M)/2,}\ {b\_{1}(M)}&{{}<B\_{1},}\ \\end{aligned}\
$$\
\
(8.27)\
\
_where V0,B1 are constants. Then there exists a constant V1, depending only upon_ _V0, Λ,B1, such that_ Vol(B(p,r)) _≤ V1 · r4, for all p ∈ M and r_ \> _0._\
\
$$\
V\_{0},B\_{1}\
$$\
\
$$\
V\_{1}\
$$\
\
$$\
\\mathrm{Vol}(B(p,r))\\leq V\_1\\cdot r^4\
$$\
\
$$\
V\_{0},\\Lambda,B\_{1}\
$$\
\
$$\
p\\in M\
$$\
\
$$\
r>0\
$$\
\
Once one has this volume growth estimate, the proof of Theorem 8.11 is fairly\
similar to the Einstein case, see \[TV05b\]. The key part of the proof of Theorem 8.12\
is the volume growth theorem in \[TV05a\], which depends on a Sobolev constant\
bound. Subsequently, using a point-picking argument, it was shown in \[TV08\] that\
the Sobolev constant bound can be replaced with a lower volume growth bound,\
which is the version we stated here. But we note that if a Sobolev constant bound\
is assumed, then the assumption on _b1_ is not necessary \[TV08\].\
\
$$\
b\_{1}\
$$\
\
#### 4.1. Desingularization questions\
\
It is natural to ask the same question that we asked in the Einstein case:\
\
_•_ Can you reverse this process? That is, start with an critical orbifold, “glue\
on” critical ALE metrics at the singular points, and resolve to a smooth\
critical metric?\
\
The “answer” is still:\
\
_•_ In general, the answer is “no”, because this gluing problem is obstructed;\
there are always decaying infinitesimal deformations of non-trivial Bt-flat\
ALE metrics.\
\
$$\
B^{t}.\
$$\
\
However, in Lecture 10 we will discuss a recent theorem which says that the answer\
is “yes” in certain cases.\
\
* * *\
\
# Regularity and volume growth\
\
In this Lecture, we will discuss some of the main ideas involved in the proofs of\
Theorems 8.11 and 8.12. Also, we will give an outline of the proof of the existence\
of an Einstein metric on CP2#2CP2 due to Chen-LeBrun-Weber \[CLW08\].\
\
$$\
\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2\
$$\
\
### 1\. Local regularity\
\
We consider any system of the type\
\
(9.1)\
\
$$\
\\Delta R i c=R m\*R i c.\
$$\
\
Any Riemannian metric satisfies\
\
(9.2)\
\
$$\
\\Delta R m=L(\\nabla^{2}R i c)+R m\*R m,\
$$\
\
$$\
L(\\nabla^{2}Ric)\
$$\
\
where L(∇2Ric) denotes a linear expression in second derivatives of the Ricci tensor, and _Rm ∗ Rm_ denotes a term which is quadratic in the curvature tensor (see\
\[Ham82, Lemma 7.2\]).\
\
$$\
Rm\*Rm\
$$\
\
For a compact 4-manifold ( _M,g),_ we define the Sobolev constant _CS_ as the\
best constant CS so that for all f ∈ C0,1(M) (Lipschitz) we have\
\
$$\
(M,g)\
$$\
\
$$\
C\_{S}\
$$\
\
$$\
C\_{S}\
$$\
\
$$\
f\\in C^{0,1}(M)\
$$\
\
(9.3)\
\
$$\
\|f\| _{L^{4}}\\leq C_{S}\|\\nabla f\| _{L^{2}}+\\overline{{V o l^{-1/4}}}\|f\|_{L^{2}}.\
$$\
\
If _(X,g)_ is a complete, noncompact 4-manifold, the Sobolev constant _CS_ is\
defined as the best constant CS so that for all f ∈ Cc0,1(X) (Lipschitz with compact\
support), we have\
\
$$\
(X,g)\
$$\
\
$$\
C\_{S}\
$$\
\
$$\
C\_{S}\
$$\
\
$$\
f\\in C\_{c}^{0,1}(X)\
$$\
\
(9.4)\
\
$$\
\|f\| _{L^{4}}\\leq C_{S}\|\\nabla f\|\_{L^{2}}.\
$$\
\
The following local regularity theorem is known as an “ -regularity” theorem:\
\
Theorem 9.1 (Tian-Viaclovsky \[TV05a\]). _Assume that (9.1) is satisfied, let r <_\
_diam(X)/2, and B(p,r_) _be a geodesic ball around the point p, and k ≥ 0. Then_\
there exist constants 0,Ck (depending upon CS) so that if\
{∫}\
\
$$\
r<\
$$\
\
$$\
d i a m(X)/2\_{\\cdot}\
$$\
\
$$\
B(p,r)\
$$\
\
$$\
p,\
$$\
\
$$\
k\\geq0\
$$\
\
$$\
\\epsilon\_{0},C\_{k}\
$$\
\
$$\
C\_{S})\
$$\
\
$$\
\|R m\| _{L^{2}(B(p,r))}=\\left{\\int_{B(p,r)}\|R m\|^{2}d V\_{g}\\right}^{1/2}\\leq\\epsilon\_{0},\
$$\
\
_then_\
\
$$\
\\mathop{{s u p}} _{B(p,r/2)}\\lvert\\nabla^{k}R m\\rvert\\leq\\frac{C_{k}}{r^{2+k}}\\left{\\int\_{B(p,r)}\\vert R m\\vert^{2}d V\_{g}\\right}^{1/2}\\leq\\frac{C\_{k}\\epsilon\_{0}}{r^{2+k}}.\
$$\
\
In the case of harmonic curvature, _δRm_ = 0, one has an equation on the full\
curvature tensor\
\
$$\
\\delta R m=0\
$$\
\
$$\
\\Delta R m=R m\*R m.\
$$\
\
(9.5)\
\
* * *\
\
In this case, the result follow by a Moser iteration procedure, for details we refer\
to \[Aku94, And89, Nak88, Tia90\]. This is a generalization of an-regularity\
theorem of Uhlenbeck \[Uhl82a, Uhl82b\]. We also note that this theorem was\
extended to extremal K¨ahler metrics by Chen-Weber \[CW11\]. Also, for Einstein\
metrics, dependence on the Sobolev constant was removed in \[CT06\].\
\
Even though second derivatives of the Ricci tensor occur in (9.2), overall the\
principal symbol of the system (9.1) and (9.2) is in triangular form. The equations\
(9.1) and (9.2), when viewed as an elliptic system, together with the bound on the\
Sobolev constant, are the key to the proof of theorem 9.1, which is an involved\
iteration procedure, and we will refer the reader to \[TV05a\] for details.\
\
In relation to Theorem 8.11, this-regularity result is the key to proving that\
there are only finitely many points at which the curvature can blow-up. This is\
because each such point must account for at least0of the _L2_-norm of curvature, which is assumed to be bounded for the sequence. Consequently, at strictly\
positive distance away from the singular points, the curvature is bounded, and a\
subsequential limiting space with finitely many singular points can be obtained using fundamental ideas of Cheeger \[Che70\] and Gromov \[Gro07\]. The subsequence\
will converge to the limit in the Gromov-Hausdorff sense, but the convergence away\
from the singular points is much stronger in the following sense. Define Ωδ,j ⊂ Mj\
to be the set of points with distance to the singular set bounded below by _δ_ \> 0.\
For _j_ large, these subsets all be diffeomorphic, and after pulling-back by diffeomorphisms to a fixed manifold, the metrics converge in any Ck,α-norm in coordinate\
charts as _j →∞._ To say more about the structure of the singularities, we need an\
upper volume growth estimate, which we discuss next.\
\
$$\
\\epsilon\_{0}\
$$\
\
$$\
L^{2}-norm\
$$\
\
$$\
\\Omega\_{\\delta,j}\\subset M\_{j}\
$$\
\
$$\
\\delta>0.\
$$\
\
$$\
C^{k,\\alpha}\
$$\
\
$$\
j\\to\\infty\
$$\
\
### 2\. Volume growth estimate\
\
We emphasize that, in the Einstein case, an upper volume growth estimate on balls\
follows from Bishop’s volume comparison theorem \[BC64\]. For metrics satisfying\
a system of the form (9.1), it is much more difficult to obtain an upper volume\
growth estimate since we are not assuming any pointwise Ricci curvature bound.\
The following is the key result:\
\
Theorem 9.2 (Tian-Viaclovsky \[TV05a\]). _Let (X,g) be a complete, noncompact,_\
_n-dimensional Riemannian manifold with base point p. Assume that there exists a_\
_constant C1_ \> 0 _so that_\
\
$$\
(X,g)\
$$\
\
$$\
C\_{1}>0\
$$\
\
(9.6)\
\
$$\
\\mathrm{Vol}(B(q,s))\\geq C\_1s^n,\
$$\
\
_for any q ∈ X, and all s ≥ 0. Assume furthermore that as r →∞,_\
\
$$\
q\\in X\
$$\
\
$$\
s\\geq0\
$$\
\
$$\
r\\to\\infty\
$$\
\
(9.7)\
\
$$\
\\sup\_{S(r)}\|R m\_g\|=o(r^{-2}),\
$$\
\
_where S(r_) _denotes the sphere of radius r centered at p. If b1(X_) < _∞, then (X,g)_\
_has finitely many ends, and there exists a constant C2 (depending on g) so that_\
\
$$\
S(r)\
$$\
\
$$\
\\mathit{If}:b\_{1}(X)<\\infty\
$$\
\
$$\
(X,g)\
$$\
\
(9.8)\
\
$$\
C\_{2}\
$$\
\
$$\
{V o l}(B(p,r))\\leq C\_{2}r^{n}.\
$$\
\
_Furthermore, each end is ALE of order 0._\
\
Outline of proof. The entire proof of this theorem is over 20 pages long;\
we only give an extremely rough outline containing the main ideas. For _s_ \> 1,\
\
$$\
s>1\
$$\
\
* * *\
\
$$\
A(s^{i},s^{i+1})\
$$\
\
consider a sequence of dyadic annuli\
subsequence _{j}⊂{i}_ so that\
\
A(si,si+1). We can assume that there is a\
\
$$\
{j}\\subset{i}\
$$\
\
(9.9)\
\
$$\
\\mathcal{H}^{n-1}(S(s^{j+1}))\\geq(1-\\eta\_{j})\\mathcal{H}^{n-1}(S(s^{j}))s^{n-1}\
$$\
\
for some sequence ηj → 0 as j →∞.\
volume growth assumption. Letting _A_\
∫\
1\
\
Otherwise, this would contradict the lower\
j = A(sj,sj+1), we show that as j →∞,\
\
$$\
\\eta\_{j}\\rightarrow0\
$$\
\
$$\
j\\to\\infty\
$$\
\
$$\
j\\to\\infty\
$$\
\
$$\
A\_{j}=A(s^{j},s^{j+1})\
$$\
\
(9.10)\
\
$$\
\\frac{1}{V o l(A\_{j})}\\int\_{A\_{j}}\|\\Delta r^{2}-2n\|d V\_{g}\\to0.\
$$\
\
The proof of this is a long computation and uses the coarea formula, we will omit\
the details.\
\
If we rescale the annuli to unit size, that is, let\
\
(9.11)\
\
$$\
\\big(\\tilde{A} _{j},\\tilde{g}_{j}\\big)=\\big(A\_{j},s^{-2j}g\\big),\
$$\
\
the curvature decay estimate (9.7) implies that\
\
0(9.12)\
\
$$\
\|Rm(\\tilde{g}\_{j})\|\\rightarrow0\
$$\
\
as j →∞, so the metric ˜gj is limiting to a flat metric.\
\
$$\
j\\to\\infty\
$$\
\
$$\
\\tilde{g}\_{j}\
$$\
\
$$\
\\Delta\\tilde{r}^{2}\\rightarrow2n;as;j\\rightarrow\\infty\
$$\
\
Note that if Vol(Ãj) < C for some constant C, then (9.10) would imply that\
∆˜r2 → 2n as j →∞, which implies that the rescaled distance function is limiting to\
the Euclidean distance function, so the sequence of rescaled annuli would converge\
to a Euclidean annulus. However, we do not yet know that the volumes of the\
rescaled annuli are bounded. To deal with this, we use a contradiction argument.\
If the rescaled volumes are not bounded, then we show it is possible to divide the\
annuli into finitely many regions with large but bounded volume, and prove that\
there is always at least one “nice” connected, non-collapsed region. This chopping\
procedure is one of the most delicate parts of the proof. We then apply the above\
rescaling argument to the sequence of “nice” regions, and show that these regions\
converge to portions of Euclidean annuli. Since Euclidean annuli “close up”, it\
follows that the entire annular regions are in fact converging to Euclidean annuli.\
This contradiction proves that the rescaled annuli have bounded volume. Since this\
can be done for any _s_ \> 1, the upper volume estimate (9.8) follows. It then follows\
that all tangent cones at infinity are Euclidean cones, from which we conclude that\
the metric is ALE of order 0.\
\
$$\
{V o l}(\\tilde{A}\_{j})<C\
$$\
\
$$\
up''\
$$\
\
$$\
s>1\
$$\
\
A important technical point arises with the above argument. In general, annuli\
might have many connected boundary components, and a sequence of connected\
components of annuli with the inner boundaries having more than 1 connected\
component would cause a problem. However, the assumption on the first Betti\
number ensures that this situation cannot arise.\
\
Note that Theorem 9.2 is a result for noncompact spaces, but this result does\
in fact imply the volume growth result stated in Theorem 8.12. This is done by a\
contradiction argument, see \[TV05b, TV08\] for the details.\
\
### 3\. ALE order and removable singularity theorems\
\
The upper volume growth estimate implies that all tangent cones of the limit space\
are ALE of order 0 which implies that the limit space has C0-orbifold singularities.\
That is, after passing to a local cover as in Definition 8.5, the metric only has\
an extension to a C0-metric in a neighborhood of the origin. Another important\
ingredient in the proof of Theorem 8.11 is therefore to prove that the singularities\
\
$$\
C^{0}\
$$\
\
$$\
C^{0}\]
$$ of the limit are _smooth_ orbifold points, that is, after passing to a local cover, the
metric can be extended to a _C_ ∞-metric over the origin. A closely related problem
is to obtain the optimal ALE order of the spaces which bubble out, which we will
discuss next.

$$
C^{\\infty}
$$

A crucial result in the Ricci-flat case was obtained by Cheeger-Tian: if (Mn,g)
is Ricci-flat ALE of order 0, there exists a change of coordinates at infinity so that
(Mn,g) is ALE of order n, where n is the dimension \[CT94\]. This generalized and
extended the work of Bando-Kasue-Nakajima \[BKN89\], who employed improved
Kato inequalities together with a Moser iteration argument. The Cheeger-Tian
method has the advantage of finding the _optimal_ order of curvature decay, without
relying on Kato inequalities.

$$
\\left(M^{n},g\\right)
$$

$$
\\left(M^{n},g\\right)
$$

In the case of anti-self-dual scalar-flat metrics, or scalar-flat metrics with harmonic curvature, it was proved in \[TV05a\] that such spaces are ALE of order _τ_ for
any _τ_ < 2, using the technique of Kato inequalities. Subsequently, this was generalized to Bach-flat metrics and metrics with harmonic curvature in dimension 4
in \[Str10\], using the Cheeger-Tian technique. This technique was generalized to
obstruction-flat metrics in any dimension in \[AV12\], which is a generalization of
the Bach-flat condition in dimension four, see \[Gra09\].

$$
\\tau<2
$$

The method in \[AV12\] applies to much more general systems than just the
obstruction tensors, and works in any dimension _n ≥_ 3\. Given two tensor fields
_A,B,_ the notation _A∗B_ will mean a linear combination of contractions of _A⊗B_
yielding a symmetric 2-tensor. The main result is:

$$
n\\geq3
$$

$$
A,B,
$$

$$
A\\otimes B
$$

n
Theorem 9.3 (Ache-Viaclovsky \[AV12\]). _Let k_ = 1 _if n_ = _3, or_ 1 _≤ k ≤_ − 1 if
2
_n ≥ 4. Assume that (M,g) is scalar-flat, ALE of order 0, and satisfies_

$$
1\\leq k\\leq\\frac{n}{2}-1ij
$$

$$
n\\geq4
$$

(9.13)

$$
\\Delta\_{g}^{k}{R i c}=\\sum\_{j=2}^{k+1}\\sum\_{\\alpha\_{1}+\\ldots+\\alpha\_{j}=2(k+1)-2j}\\nabla\_{g}^{\\alpha\_{1}}{R m} _\\ldots_\\nabla\_{g}^{\\alpha\_{j}}{R m}.
$$

_Then (M,g) is ALE of order n − 2k._

$$
(M,g)
$$

$$
n-2k
$$

For _k_ = 1, this is simply

$$
k=1
$$

(9.14)

$$
\\Delta R i c=R m\*R m.
$$

We emphasize that this is more general than (9.1), since the right hand side is allowed to be quadratic in the full curvature tensor. This is satisfied in particular by
scalar-flat K¨ahler metrics and metrics with harmonic curvature in any dimension,
and also anti-self-dual metrics in dimension 4. These special cases were previously
considered in \[Che09\] using improved Kato inequalities and a Moser iteration technique. The optimal decay for scalar-flat anti-self-dual ALE metrics was previously
considered in \[CLW08, Proposition 13\]. The case of extremal K¨ahler ALE metrics
was considered in \[CW11\]. As mentioned above, the cases of Bach-flat metrics and
metrics with harmonic curvature in dimension 4 were considered in \[Str10\].

The main idea of the proof of Theorem 9.3 is based on the method of Cheeger-
Tian from \[CT94\], and is roughly to show that the optimal ALE decay rate is
determined by the rates of decaying solutions of the gauged, linearized equation on
a Euclidean cone. This step uses a fundamental technique of Leon Simon called
the _Three Annulus Lemma_ \[Sim85\]. An analysis of the decay rates of solutions of
the gauged linearized equation, together with an estimate on the nonlinear terms
in the equation, then yields Theorem 9.3.

* * *

The same technique also yields a removable singularity theorem for higher-order
systems:

n
Theorem 9.4 (Ache-Viaclovsky \[AV12\]). _Let k_ = 1 _if n_ = _3, or_ 1 _≤ k ≤ −_ 1 _if_
2
n ≥ 4. Assume that (Bρ(0) {0},g) has constant scalar curvature and satisfies

$$
k=1if n=3
$$

$$
1\\leq k\\leq\\frac{n}{2}-1
$$

$$
(B\_{\\rho}(0)\\setminus\\dot{{0},g})
$$

$$
n\\geq4
$$

(9.15)

$$
\\Delta\_{g}^{k}{R i c}=\\sum\_{j=2}^{k+1}\\sum\_{\\alpha\_{1}+\\ldots+\\alpha\_{j}=2(k+1)-2j}\\nabla\_{g}^{\\alpha\_{1}}{R m} _\\ldots_\\nabla\_{g}^{\\alpha\_{j}}{R m}.
$$

If the origin is a C0-orbifold point for g, then the metric extends to a smooth orbifold
metric in Bρ(0).

$$
C^{0}-or of old
$$

$$
B\_{\\rho}(0)
$$

In particular, this says that the limit space in Theorem 8.11 is a smooth multifold.

### 4\. Chen-LeBrun-Weber metric

The volume growth theorem was used in a fundamental way in \[CLW08\] in order
to obtain an Einstein metric on CP2#2CP , in this section we will give a brief2
overview of the proof.

$$
\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

Theorem 9.5 (Chen-LeBrun-Weber \[CLW08\]). _There exists a positive Einstein_ _metric on M_ = CP2#2CP2.

$$
M=\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

Outline of Proof. The first step is to consider K¨ahler classes which are
invariant under a torus action, and bilaterally symmetric. That is, only K¨ahler
classes from which the (−1) curves in the blow-up have the same area are considered.
The space of such K¨ahler classes is 1-dimensional, and one can parametrize these
classes by the area of the (−1) curves; call this parameter _x._ Chen-Lebrun-Weber
then consider the functional
(c1 · \[ω\])2 1

(9.16)

$$
\\mathcal{A}(\[\\omega\])=\\frac{(c\_{1}\\cdot\[\\omega\])^{2}}{\[\\omega\]^{2}}-\\frac{1}{32\\pi^{2}}\\mathcal{F}(\\xi,\[\\omega\]),
$$

where _F_ (ξ,\[ω\]) is the Futaki invariant, with _ξ_ the extremal vector field of the
class \[ω\], see \[Fut83, Fut88, FM93\]. It is next observed that the graph of _A_ as
a function of _x_ has a strict local minimum at a certain positive value of _x,_ call
this value x0. If one can prove that an extremal K¨ahler metric gx0 exists in this
class corresponding to x0, then S would have a critical point at gx0 when restricted
to the set of toric, bilaterally symmetric K¨ahler classes on _M._ From (6.26), the
functional _W_ would also have such a critical point.

$$
\\mathcal{F}(\\xi,\[\\omega\])
$$

$$
\\xi
$$

$$
\\left\[\\omega\\right\]
$$

$$
x
$$

$$
x,
$$

$$
x\_{0}
$$

$$
g\_{x\_0}
$$

$$
x\_{0}
$$

$$
\\mathcal{S}
$$

$$
g\_{x\_0}
$$

To proceed further, we need to understand the structure of the Bach tensor
for a K¨ahler metric. The Bach tensor is a symmetric tensor, and since we have a
complex structure, we can consider the tensors B+ and B−, the J-invariant and J
anti-invariant parts of _B,_ respectively. A computation shows that
2 ()

$$
B^{+}
$$

$$
B^{-}
$$

(9.17)

$$
B^{+}=-\\frac{2}{3}\\left(R E+2(\\nabla^{2}R)\_{0}^{+}\\right),
$$

(9.18)

$$
B^{-}=\\frac{2}{3}(\\nabla^{2}R)\_{0}^{-},
$$

where (∇2R)0+ and (∇2R)0− denote the J-invariant and J anti-invariant parts of
the traceless Hessian of the scalar curvature, respectively, see \[Der83, ACG03\].
This implies the following:

$$
(\\nabla^{2}R)\_{0}^{+}
$$

$$
(\\nabla^{2}R)\_{0}^{-}
$$

* * *

Proposition 9.6 (Derdzinski \[Der83\]). _If (M,g,J) is K¨ahler and Bach-flat, then_
(M,g,J) is extremal and the metric g˜ = Rg−2g is Einstein near any point with
Rg 6= 0.

$$
\\mathit{If}\\left(M,g,J\\right)
$$

$$
\\left(M,g,J\\right)
$$

$$
\\tilde{g}=R\_{g}^{-2}g
$$

$$
R\_{g}\\neq0.
$$

Proof. This follows from equations (9.17) and (9.18) by noting that the condition (∇2R)0− = 0 is exactly the condition for g to be extremal K¨ahler \[Cal82\],
and the second claim follows from the conformal transformation formula (2.7).

$$
(\\nabla^{2}R)\_{0}^{-}=0
$$

If the extremal metric gx0 exists, since this metric is critical for W restricted to
the space of invariant K¨ahler classes, (9.17) and (9.18) show that the Bach tensor
can be viewed is a harmonic (1,1)-form and can therefore be used as a K¨ahler
variation. Consequently, gx0 would be Bach-flat. It turns out that this metric
must have strictly positive scalar curvature, so Proposition 9.6 yields the desired
conformally Einstein metric.

$$
g\_{x\_0}
$$

$$
g\_{x\_0}
$$

The main part of the proof is therefore to show that the extremal K¨ahler metric
gx0 exists. To show this, a continuity argument is used. For x small, extremal
K¨ahler metrics are known to exist in these K¨ahler classes by work of Arezzo-Pacard-
Singer \[APS11\]; this was an extension of the gluing result of Arezzo-Pacard for
constant scalar curvature K¨ahler metrics \[AP06, AP09\]. The set of K¨ahler classes
admitting extremal K¨ahler metrics is known to be open by LeBrun-Simanca \[LS93\].
A compactness theorem is used to show that the set of _x_ for which there exists an
extremal K¨ahler metric is also closed for _x ≤ x0._ Consequently, from connectedness
of the interval (0,x0\], an extremal K¨ahler metric exists at _x0._

$$
g\_{x\_0}
$$

$$
x\\leq x\_{0}
$$

$$
(0,x\_0\]
$$

$$
x\_{0}
$$

To show the compactness, an extension of Theorem 8.11 to extremal K¨ahler
metrics is used \[CW11\]. We note that the main part of \[CW11\] is to extend theregularity result in Theorem 9.1 to the class of extremal K¨ahler metrics; the volume
growth result in Theorem 9.2 is still crucial in order to obtain the compactness
theorem. Given a sequence of extremal K¨ahler metrics gxi for xi → x ≤ x0 as
_i → ∞,_ an orbifold limit can be obtained provided that the Sobolev constant
can be controlled, which is proved in \[CLW08, Section 5\]. If the curvatures of
this sequence were not bounded, then a nontrivial K¨ahler scalar-flat ALE space
must bubble off at some point. However, a detailed analysis of possible bubbles,
employing the toric and bilateral symmetries, shows that non-trivial bubbles can
be ruled out, thereby proving compactness.

$$
g\_{x\_i}
$$

$$
x\_{i}\\rightarrow x\\leq x\_{0}
$$

$$
i\\to\\infty,
$$

* * *

# A gluing theorem for Bt-flat metrics

$$
B^{t}-
$$

### 1\. Existence of critical metrics

Let us begin by stating the main result:

Theorem 10.1 (Gursky-Viaclovsky \[GV13\]). A Bt-flat metric exists on the man-
_ifolds in the table for some t near the indicated value of t0._

$$
B^{t}
$$

Table 10.1. Simply-connected examples with one bubble

| Topology of connected sum | Value(s) of t0 |
| --- | --- |
| (\\mathbb{CP}^2 #\\overline{\\mathbb{CP}}^2) | -1/3 |
| (S^2 × S^2 #\\overline{\\mathbb{CP}}^2 = \\mathbb{CP}^2 #2\\overline{\\mathbb{CP}}^2) | -1/3, -(9m1)-1 |
| S2 × S2 #S2 × S2 | -2(9m1)-1 |

$$
t\_{0}
$$

$$
\\overline{\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2}
$$

$$
-1/3
$$

$$
S^{2}\\times S^{2}#\\overline{\\mathbb{C}}\\mathbb{P}^{2}=\\mathbb{C}\\mathbb{P}^{2}#2\\overline{\\mathbb{C}}\\mathbb{P}^{2}
$$

$$
-1/3,-(9m\_1)^{-1}
$$

$$
S^{2}\\times S^{2}#S^{2}\\times S^{2}
$$

$$
-2(9m\_{1})^{-1}
$$

The constant _m1_ is the mass of the Green’s function metric of the product
metric S2 × S2, defined in (2.15).

$$
m\_{1}
$$

$$
S^{2}\\times S^{2}
$$

We make some remarks:

_• M_ = CP2#CP2 admits an U(2)-invariant Einstein metric called the “Page
metric” \[Pag78a\]. _M_ does not admit any K¨ahler-Einstein metric, but the
Page metric is conformal to an extremal K¨ahler metric.

$$
M=\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

$$
U(2)
$$

_• M_ = CP2#2CP2 admits a toric invariant Einstein metric called “Chen-
LeBrun-Weber metric” described in the previous lecture \[CLW08\]. Again,
_M_ does not admit any K¨ahler-Einstein metric, but the Chen-LeBrun-
Weber metric is conformal to an extremal K¨ahler metric.

$$
M=\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

• M = S2 × S2#S2 × S2 does not admit any K¨ahler metric, it does not
even admit an almost complex structure. Our metric is the first known
example of a “canonical” metric on this manifold.

$$
M=S^{2}\\times S^{2}#S^{2}\\times S^{2}
$$

#### 1.1. The approximate metric

The critical metrics in Theorem 10.1 are found by perturbing from an “approximate” critical metric. We describe this construction next.

• Let (Z,gZ) and (Y,gY) be Einstein manifolds, and assume that gY has
positive scalar curvature.

$$
(Z,g\_Z)
$$

$$
\\left(Y,g\_{Y}\\right)
$$

$$
z\_{0}\\in Z
$$

_•_ Choose basepoints _z0 ∈ Z_ and _y0 ∈ Y._

$$
y\_{0}\\in Y.
$$

• Convert (Y,gY) into an asymptotically flat (AF) metric

$$
\\left(Y,g\_{Y}\\right)
$$

$$
\\left(N,g\_{N}\\right)=\\left(Y\\setminus\\left{y\_{0}\\right},G^{2}g\_{Y}\\right)
$$ using the Green’s function for the conformal Laplacian based at _y0._ Since
(M,g) is Bach-flat, then (N,gN) is also Bach-flat (from conformal invariance) and scalar-flat (since we used the Green’s function). Consequently,
gN is Bt-flat for all t ∈ R.

$$
y\_{0}.
$$

$$
(M,g)
$$

$$
\\left(N,g\_{N}\\right)
$$

$$
B^{t}-flat
$$

$$
t\\in\\mathbb{R}.
$$

_•_ Let _a_ \> 0 be small, and consider _Z\\B(z0,a)._ Scale the compact metric
to (Z, g˜ = a−4gZ). Attach this metric to the metric (N\\B(a−1),gN)
using cutoff functions near the boundary, to obtain a smooth metric on
the connected sum _Z#Y._

$$
a>0
$$

$$
Z\\setminus B(z\_{0},a)
$$

$$
(Z,\\tilde{g}=a^{-4}g\_{Z})
$$

$$
(N\\setminus B(a^{-1}),g\_{N})
$$

$$
Z#\\overline{Y}
$$

Compact Einstein Damage zone
metric
AF metric

Figure 10.1. The approximate metric.

Since both gZ and gN are Bt-flat, this metric is an “approximate” Bt-flat metric, with vanishing Bt tensor away from the “damage zone”, where cutoff functions
were used.

$$
g\_{N}
$$

$$
g\_{Z}
$$

$$
B^{t}
$$

$$
B^{t}
$$

$$
B^{t}
$$

### 2\. Lyapunov-Schmidt reduction

In general, there are several degrees of freedom in this approximate metric.

_•_ The scaling parameter _a_ (1-dimensional).

_•_ Rotational freedom when attaching (6-dimensional).

_•_ Freedom to move the base points of either factor (8-dimensional).

There are a total of 15 gluing parameters, which yield a 15-dimensional space
of “approximate” kernel of the linearized operator. Using a Lyapunov-Schmidt
reduction argument, one can reduce the problem to that of finding a zero of the
_Kuranishi map_

$$
\\Psi:U\\subset\\mathbb{R}^{15}\\to\\mathbb{R}^{15}.
$$

(10.1)

_•_ It is crucial to use certain weighted norms to find a bounded right inverse
for the linearized operator.

_•_ This 15-dimensional problem is too difficult in general. We will take advantage of various symmetries in order to reduce to only 1 free parameter:
the scaling parameter _a._

* * *

#### 2.1. Technical theorem

The leading term of the Kuranishi map corresponding to the scaling parameter is
given by:

Theorem 10.2 (\[GV13\]).
(

_As a → 0, then for any_ \> _0,_
)

$$
a\\to0\]
$$

(10.2)

$$
\\epsilon>0
$$

$$
\\Psi\_{1}=\\Big(\\frac{2}{3}W(z\_{0})\\circledast W(y\_{0})+4t R(z\_{0}){\\operatorname{mass}}(g\_{N})\\Big)\\omega\_{3}a^{4}+O(a^{6-\\epsilon}),
$$

where ω3 = Vol(S3)

_, and the product of the Weyl tensors is given by_
∑

$$
\\omega\_{3}=Vol(S^{3})
$$

(10.3)

$$
W(z\_{0})\\circledast W(y\_{0})=\\sum\_{i j k l}W\_{i j k l}(z\_{0})(W\_{i j k l}(y\_{0})+W\_{i l k j}(y\_{0})),
$$

where Wijkl(·) denotes the components of the Weyl tensor in a normal coordinate
_system at the corresponding point._

$$
W\_{i j k l}(\\cdot)
$$

We note that the product ~ depends upon the coordinate systems chosen, and
therefore in general depends upon a rotation parameter, and obviously on the base
points of the gluing.

### 3\. The building blocks

We next discuss the “building blocks” of the gluing construction.

#### 3.1. The Fubini-Study metric

We let (CP2,gFS) denote the Fubini-Study metric, scaled so that Ric = 6g. We
consider the following group actions.

$$
(\\mathbb{C P}^{2},g\_{\\mathrm{FS}})
$$

$$
Ric=6g
$$

Torus action:

(10.4)

$$
\[z\_{0},z\_{1},z\_{2}\]\\mapsto\[z\_{0},e^{i\\theta\_{1}}z\_{1},e^{i\\theta\_{2}}z\_{2}\].
$$

Flip symmetry:

(10.5)

$$
\[z\_{0},z\_{1},z\_{2}\]\\mapsto\[z\_{0},z\_{2},z\_{1}\].
$$

The Green’s function metric of the Fubini-Study metric ˆgFS is also known as the
Burns metric, and is completely explicit (in fact, it is the case _n_ = 1 of (8.20)) with
mass given by

$$
\\hat{g}\_{FS}
$$

$$
\\mathrm{mass}(\\hat{g}\_{FS})=2.
$$

(10.6)

#### 3.2. The product metric

The next building block is (S2 × S2,gS2×S2), the product of 2-dimensional spheres
of Gaussian curvature 1, with _Ric_ = _g._ We consider the following group actions.

$$
\\left(S^{2}\\times S^{2},g\_{S^{2}\\times S^{2}}\\right)
$$

$$
Ric=g
$$

Torus action:

(10.7)

Product of rotations fixing north and south poles.

Flip symmetry:

$$
(p\_{1},p\_{2})\\mapsto(p\_{2},p\_{1}).
$$

(10.8)

The Green’s function metric ĝS2×S2of the product metric does not seem to
have a known explicit description. We will denote

$$
\\hat{g}\_{S^{2}\\times S^{2}}
$$

(10.9)

$$
m\_{1}=\\operatorname{mass}(\\hat{g}\_{S^{2}\\times S^{2}}).
$$

* * *

By the positive mass theorem of Schoen-Yau, _m1_ \> 0\. Note that since _S2 × S2_ is
spin, this also follows from Witten’s proof of the positive mass theorem. The value
of _m1_ has recently been determined:

$$
S^{2}\\times S^{2}
$$

$$
m\_{1}>0
$$

$$
m\_{1}
$$

Theorem 10.3 (\[Via15\]). _The mass m1 ∼_ .5872 _and may be written as an explicit_
_infinite sum._

$$
m\_{1}\\sim.5872
$$

The explicit formula for the mass is lengthy, and will not be written here. We
just note that this implies that (−9m1)−1 ∼= −.1892 so as a corollary we see that
2
the manifold S2 × S2#CP admits a Bt-flat metrics for at least two different values
of _t._ Note that it is shown in \[GV13\] that the metrics obtained in Theorem 10.1
are not Einstein, so these metrics are distinct from the Chen-LeBrun-Weber metric.

$$
(-9m\_{1})^{-1}\\sim=-.1892
$$

$$
S^{2}\\times S^{2}#\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}
$$

$$
B^{t}.
$$

### 4\. Remarks on the proof

We first remark that:

_•_ We impose the toric symmetry and “flip” symmetry in order to reduce
the number of free parameters to 1 (only the scaling parameter). That is,
we perform an equivariant gluing.

$$
\\text{"}flip\\text{"}
$$

_•_ The special value of _t0_ is computed by
2

$$
t\_{0}
$$

$$
\\frac{2}{3}W(z\_{0})\\circledast W(y\_{0})+4t\_{0}R(z\_{0}){\\operatorname{mass}}(g\_{N})=0.
$$

This choice of _t0_ makes the leading term of the Kuranishi map vanish,
and is furthermore a nondegenerate zero (if R(z0) \> 0; mass(gN) \> 0 by
the positive mass theorem).

$$
t\_{0}
$$

$$
(\\mathrm{if}R(z\_{0})>0;\\mathrm{mass}(g\_{N})>0
$$

We next outline the spaces used in the construction of the näıve approximate
metric:

_•_ (i) CP2#CP ; the Fubini-Study metric with a Burns metric attached at2
one fixed point. This case admits a U(2)-action.

$$
\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

2 2
• (ii) S2 × S2#CP = CP2#2CP ; the product metric on S2 × S2 with a
Burns metric attached at one fixed point. Alternatively, we can view this
as the Fubini-Study metric on CP2, with a Green’s function _S2×S2_ metric
attached at one fixed point. For this topology, we will therefore construct
two different critical metrics. Both of these will have toric symmetry plus
invariance under the flip symmetry.

$$
S^{2}\\times S^{2}#\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}=\\mathbb{C}\\mathbb{P}^{2}#2\\overline{\\mathbb{C}}\\overline{\\mathbb{P}}^{2}
$$

$$
S^{2}\\times S^{2}
$$

$$
\\mathbb{C}\\mathbb{P}^2
$$

$$
S^{2}\\times S^{2}
$$

• (iii) S2 × S2#S2 × S2; the product metric on S2 × S2 with a Green’s
function _S2 × S2_ metric attached at one fixed point. This metric is toric
and flip-symmetric.

$$
S^{2}\\times S^{2}#S^{2}\\times S^{2};
$$

$$
S^{2}\\times S^{2}
$$

$$
S^{2}\\times S^{2}
$$

We note that an equivariant gluing is carried out – the metrics obtained in
Theorem 10.1 retain the indicated symmetries.

By imposing other discrete symmetries, we can perform the gluing operation
with more than one bubble. For example, we can find critical metrics on CP2#3CP2
2
3#S2×S2, CP2#3(S2×S2), S2×S2#4CP , and 5#S2×S2 (see \[GV13, Table 1.2\]).

$$
\\mathbb{C}\\mathbb{P}^2#3\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

$$
3#S^{2}\\times S^{2},\\mathbb{C}\\mathbb{P}^{2}#3(S^{2}\\times S^{2}),S^{2}\\times S^{2}#4\\overline{\\mathbb{C}\\mathbb{P}}^{2}
$$

$$
5#S^{2}\\times S^{2}
$$

The product metric on S2 × S2 admits the quotient S2 × S2/Z2 where Z2
acts by the antipodal map on both factors. It is well-known that this quotient
is diffeomorphic to G(2,4), the Grassmannian of 2-planes in R4, see for example
\[ST69\]. Another quotient is RP2 _×_ RP2. The product metric descends to an

$$
S^{2}\\times S^{2}
$$

$$
S^{2}\\times S^{2}/\\mathbb{Z}\_{2}
$$

$$
\\mathbb{Z}\_2
$$

$$
G(2,4)
$$

$$
\\mathbb{R}^4
$$

$$
\\mathbb{R}\\mathbb{P}^{2}\\times\\mathbb{R}\\mathbb{P}^{2}
$$

* * *

Einstein metric on both of these quotients. We can also use these quotient spaces
as building blocks to obtain non-simply connected examples. We do not list all of
the examples here, but just note that we find a critical metric on G(2,4)#G(2,4),
which has infinite fundamental group, and therefore does not admit any positive
Einstein metric by Myers’ Theorem. For the complete list of non-simply-connected
examples, see \[GV13, Table 1.3, Table B.1\].

$$
G(2,4)#G(2,4)
$$

#### 4.1. Ellipticity and gauging

The Bt-flat equations are not elliptic due to diffeomorphism invariance. A gauging
procedure analogous to the Bianchi gauge is used. This was already discussed above
in Lecture 7, with the following note. From (5.4), we can write

$$
B^{t}
$$

(10.10)

$$
\\mathcal{F} _{\\tau}=16\\pi^{2}\\chi(M)+\\frac{1}{2}\\mathcal{B}_{2(\\tau+\\frac{1}{3})}.
$$

Taking gradients, we obtain the relation

(10.11)

$$
\\nabla\\mathcal{B} _{t}=2\\nabla\\mathcal{F}_{\\frac{t}{2}-\\frac{1}{3}}.
$$

It follows from the formula for _P_

that the linearized operator is given by

(10.12)

$$
S^{t}h=(B^{\\prime}+t C^{\\prime})h+\\mathcal{K} _{g}\\delta_{g}\\mathcal{K} _{g}\\delta_{g}\\stackrel{\\circ}{h},
$$

where B′ and C′ are the linearizations of B and C respectively. Therefore the
t
discussion in Lecture 7 applies, with τ replaced by − 1/3.
2

$$
B'
$$

$$
C'
$$

$$
\\frac{t}{2}-\\frac{1}{3}
$$

#### 4.2. Rigidity

The rigidity results we need were discussed above.
ing linearized operator as we change _τ → t._
linearized operator at an Einstein metric is given by
()(

We mention here the result-
For _h_ transverse-traceless (TT), the
())

$$
\\tau\\to t.
$$

(10.13)

$$
S^{t}h=\\Big(\\Delta\_{L}+\\frac{1}{2}R\\Big)\\Big(\\Delta\_{L}+\\Big(\\frac{1}{3}+t\\Big)R\\Big)h.
$$

Next, for _h_ = _fg,_ we have

$$
h=f g
$$

(10.14)

$$
t r\_{g}(S^{t}h)=6t(3\\Delta+R)(\\Delta f).
$$

The above rigidity results, Theorems 7.11 and 7.12, are then as follows (stated in
terms of _t_ instead of τ).

Theorem 10.4 (\[GV15\]). On (CP2,gFS), H1t = {0} provided that t < 1.

$$
(\\mathbb{C P}^{2},g\_{\\mathrm{FS}}),H\_{t}^{1}={0}
$$

$$
t<1
$$

For the case of the product metric:

Theorem 10.5 (\[GV15\]). On (S2 × S2,gS2×S2), H1t = {0} provided that t < 2/3
and t 6= −1/3. If t = −1/3, then H1t is one-dimensional and spanned by the element
_g1 − g2._

$$
\\left(S^{2}\\times S^{2},g\_{S^{2}\\times S^{2}}\\right),H\_{t}^{1}=\\left{0\\right}
$$

$$
t<2/3
$$

$$
t\\neq-1/3.\ \\textit{If}t=-1/3
$$

$$
H\_{t}^{1}
$$

$$
g\_{1}-g\_{2}
$$

In relation to Theorem 10.1, the positive mass theorem says that _t0_ < 0, so
luckily we are in the rigidity range of the factors. Consequently, there is no cokernel
arising from deformations of the building blocks.

$$
t\_{0}<0
$$

* * *

#### 4.3. Refined approximate metric

The approximate metric described above is not good enough. It must be improved
by matching up leading terms of the metrics by solving certain auxiliary linear
equations, so that the cutoff function disappears from the leading term. This step
is inspired by the work of Biquard mentioned above. Let (Z,gZ) be the compact
metric. In Riemannian normal coordinates,

$$
\\left(Z,g\_{Z}\\right)
$$

(10.15)

$$
(g\_{Z}) _{i j}(z)=\\delta_{i j}-\\frac{1}{3}R\_{i k j l}(z\_{0})z^{k}z^{l}+O^{(4)}(\|z\|^{4})\_{i j}
$$

as _z → z0._

$$
z\\rightarrow z\_{0}
$$

Let (N,gN

) be the Green’s function metric of ( _Y,g_

Y), then we have

$$
(N,g\_N)
$$

$$
\\left(Y,g\_{Y}\\right)
$$

(10.16)

$$
(g\_{N}) _{i j}(x)=\\delta_{i j}-\\frac{1}{3}R\_{i k j l}(y\_{0})\\frac{x^{k}x^{l}}{\|x\|^{4}}+2A\\frac{1}{\|x\|^{2}}\\delta\_{i j}+O^{(4)}(\|x\|^{-4+\\epsilon})
$$

as _\|x\|→∞,_ for any > 0. Note that the constant _A_ is given by

$$
\|x\|\\to\\infty
$$

$$
\\epsilon>0
$$

(10.17)

$$
\\mathrm{mass}(g\_N)=12A-R(y\_0)/12.
$$

We consider a−4gZ and let z = a2x, then we have

$$
a^{-4}g\_{Z}
$$

$$
z=a^{2}x
$$

(10.18)

$$
a^{-4}(g\_{Z}) _{i j}(x)=\\delta_{i j}-a^{4}\\frac{1}{3}R\_{i k j l}(z\_{0})x^{k}x^{l}+\\cdots.
$$

Note that the second order terms do not agree. One needs to construct new metrics
on the factors so that these terms agree. This is done by solving the linearized
equation on each factor with prescribed leading term the second order term of the
_other_ metric. We will describe this procedure next.

#### 4.4. The obstruction

On (N,gN), one would like to solve

$$
(N,g\_N)
$$

(10.19)

$$
\\begin{align\*}S^{t}\\tilde{h}&=0\\\tilde{h}&=-a^{4}\\frac{1}{3}R\_{ikjl}(z\_{0})x^{k}x^{l}+O(\|x\|^{\\epsilon}),\\end{align\*}
$$

as _x → ∞._ However, it turns out this equation is obstructed, so there is not
necessarily a solution. However, using some Fredholm theory in weighted spaces,
it turns out that one _can_ solve the modified equation
˜ =

$$
x\\to\\infty
$$

$$
S^{t}\\tilde{h}=\\lambda\\cdot k\_{1},
$$

where k1 pairs nontrivially with the decaying cokernel o1 on the AF space (N,gN).
(There is also a considerable amount of work involved in order to prove that the
space of decaying cokernel is 1-dimensional; the symmetries are crucial for this.)

$$
k\_{1}
$$

$$
o\_{1}
$$

$$
\\left(N,g\_{N}\\right)
$$

_•_ A similar procedure is carried out on the compact factor, except this is unobstructed (since the compact factor is rigid), so this does not contribute
to the leading term of the Kuranishi map.

The leading term is the computed by the following. Pairing with the cokernel
element _o1,_
∫

$$
o\_{1}
$$

$$
\\begin{aligned}\\lambda&=\\lim\_{r\\to\\infty}\\int\_{B(r)}\\langle S\\tilde{h},o\_1\\rangle\\&=\\lim\_{r\\to\\infty}(spherical boundary integrals).\\end{aligned}
$$

* * *

)(10.20)

This limit can be computed explicitly using the expansion of the cokernel element

$$
(o\_{1}) _{ij}=\\frac{2}{3}W_{ikjl}(y\_{0})\\frac{x^{k}x^{l}}{\|x\|^{4}}+f g\_{ij}+O(\|x\|^{-4+\\epsilon})
$$

as _x →∞,_ where _f_ satisfies

$$
x\\to\\infty
$$

(10.21)

$$
\\Delta f=-\\frac{1}{3}\\langle{R i c},o\_{1}\\rangle,
$$

together with the expansion

(10.22)

$$
\\tilde{h}=-a^{4}\\frac{1}{3}R\_{i k j l}(z\_{0})x^{k}x^{l}+O(\|x\|^{\\epsilon}),
$$

as _x →∞._

$$
x\\to\\infty.
$$

The complete computation is very lengthy, and we refer to \[GV13\] for the
details.

#### 4.5. Final remarks

The proof shows that there is a dichotomy. Either

_•_ (i) there is a critical metric at exactly the critical _t0,_ in which case there
would necessarily be a 1-dimensional moduli space of solutions for this
fixed _t0,_ or

$$
t\_{0},
$$

$$
t\_{0},
$$

_•_ (ii) for each value of the gluing parameter _a_ sufficiently small, there will be
a critical metric for a corresponding value of _t0_ = _t0(a)._ The dependence
of _t0_ on _a_ will depend on the next term in the expansion of the Kuranishi
map.

$$
t\_{0}=t\_{0}(a)
$$

$$
t\_{0}
$$

### Bibliography

\[AB03\] Kazuo Akutagawa and Boris Botvinnik, _Yamabe metrics on cylindrical manifolds,_
Geom. Funct. Anal. 13 (2003), no. 2, 259–333. MR 1982146 (2004e:53051)

\[AB04\], _The Yamabe invariants of orbifolds and cylindrical manifolds, and L_ 2-
_harmonic spinors,_ J. Reine Angew. Math. 574 (2004), 121–146. MR 2099112
(2005g:53055)

$$
L^{2}
$$

\[ACG03\] V. Apostolov, D. M. J. Calderbank, and P. Gauduchon, _The geometry of weakly selfdual K¨ahler surfaces,_ Compositio Math. 135 (2003), no. 3, 279–322. MR 1956815
(2004f:53045)

\[ADH13\] Bernd Ammann, Mattias Dahl, and Emmanuel Humbert, _Smooth Yamabe invariant_
_and surgery,_ J. Differential Geom. 94 (2013), no. 1, 1–58. MR 3031859

\[AHS78\] M. F. Atiyah, N. J. Hitchin, and I. M. Singer, _Self-duality in four-dimensional Riemannian geometry,_ Proc. Roy. Soc. London Ser. A 362 (1978), no. 1711, 425–461.
MR 506229 (80d:53023)

\[AIL07\] Kazuo Akutagawa, Masashi Ishida, and Claude LeBrun, _Perelman’s invariant, Ricci_
_flow, and the Yamabe invariants of smooth manifolds,_ Arch. Math. (Basel) 88 (2007),
no. 1, 71–76. MR 2289603 (2007j:53070)

\[Aku94\] Kazuo Akutagawa, _Yamabe metrics of positive scalar curvature and conformally flat_
_manifolds,_ Differential Geom. Appl. 4 (1994), no. 3, 239–258. MR 95i:58046

\[Aku12\], _Computations of the orbifold Yamabe invariant,_ Math. Z. 271 (2012), no. 3-4,
611–625. MR 2945574

\[And89\] Michael T. Anderson, _Ricci curvature bounds and Einstein metrics on compact manifolds,_ J. Amer. Math. Soc. 2 (1989), no. 3, 455–490. MR 90g:53052

\[And97\], _Extrema of curvature functionals on the space of metrics on_ 3- _manifolds,_ Calc.
Var. Partial Differential Equations 5 (1997), no. 3, 199–269. MR 1438146 (98a:58041)

\[And01\], _Extrema of curvature functionals on the space of metrics on 3-manifolds._ _II,_ Calc. Var. Partial Differential Equations 12 (2001), no. 1, 1–58. MR 1808106
(2002a:58012)

* * *

\[And10\], _A survey of Einstein metrics on 4-manifolds,_ Handbook of geometric analysis,
No. 3, Adv. Lect. Math. (ALM), vol. 14, Int. Press, Somerville, MA, 2010, pp. 1–39.
MR 2743446 (2012a:53071)

\[AP06\] Claudio Arezzo and Frank Pacard, _Blowing up and desingularizing constant scalar_
_curvature K¨ahler manifolds,_ Acta Math. 196 (2006), no. 2, 179–228. MR 2275832
(2007i:32018)

\[AP09\], _Blowing up K¨ahler manifolds with constant scalar curvature. II,_ Ann. of Math.
(2) 170 (2009), no. 2, 685–738. MR 2552105 (2010m:32025)

\[APS11\] Claudio Arezzo, Frank Pacard, and Michael Singer, _Extremal metrics on blowups,_ Duke
Math. J. 157 (2011), no. 1, 1–51. MR 2783927 (2012k:32024)

\[Aub76\] Thierry Aubin, _Équations diff´erentielles non lińeaires et probl\`eme de Yamabe concernant la courbure scalaire,_ J. Math. Pures Appl. (9) 55 (1976), no. 3, 269–296.

\[Aub78\], _Équations du type Monge-Amp\`ere sur les varíet´es k¨ahĺeriennes compactes,_
Bull. Sci. Math. (2) 102 (1978), no. 1, 63–95. MR 494932 (81d:53047)

\[Aub98\], _Some nonlinear problems in Riemannian geometry,_ Springer-Verlag, Berlin,
1998.

\[AV12\] Antonio G. Ache and Jeff A. Viaclovsky, _Obstruction-flat asymptotically locally Euclidean metrics,_ Geom. Funct. Anal. 22 (2012), no. 4, 832–877.

\[AV15\], _Asymptotics of the self-dual deformation complex,_ J. Geom. Anal. 25 (2015),
no. 2, 951–1000. MR 3319957

\[Bac21\] R. Bach, _Zur weylschen relativitatstheorie und der weylschen erweiterung des krummungstensorbegriffs,_ Math. Zeit. 9 (1921), 112–135.

\[Bar86\] Robert Bartnik, _The mass of an asymptotically flat manifold,_ Comm. Pure Appl. Math.
39 (1986), no. 5, 661–693. MR 849427 (88b:58144)

\[BC64\] Richard L. Bishop and Richard J. Crittenden, _Geometry of manifolds,_ Academic Press,
New York, 1964. MR 29 #6401

\[BCG95\] G. Besson, G. Courtois, and S. Gallot, _Entropies et rigidit´es des espaces localement_
_syḿetriques de courbure strictement ńegative,_ Geom. Funct. Anal. 5 (1995), no. 5,
731–799. MR 1354289 (96i:58136)

\[BE69\] M. Berger and D. Ebin, _Some decompositions of the space of symmetric tensors on a_
_Riemannian manifold,_ J. Differential Geometry 3 (1969), 379–392. MR 0266084 (42
#993)

\[Ber70\] Marcel Berger, _Quelques formules de variation pour une structure riemannienne,_ Ann.
Sci. École Norm. Sup. (4) 3 (1970), 285–294. MR 0278238 (43 #3969)

\[Bes08\] Arthur L. Besse, _Einstein manifolds,_ Classics in Mathematics, Springer-Verlag, Berlin,
2008, Reprint of the 1987 edition. MR 2371700 (2008k:53084)

\[BG08\] Thomas P. Branson and A. Rod Gover, _Origins, applications and generalisations_
_of the Q-curvature,_ Acta Appl. Math. 102 (2008), no. 2-3, 131–146. MR 2407527
(2010a:53025)

\[Biq13a\] Olivier Biquard, _D´esingularisation de ḿetriques d’Einstein. I,_ Invent. Math. 192
(2013), no. 1, 197–252. MR 3032330

\[Biq13b\], _D´esingularisation de ḿetriques d’Einstein. II,_ arXiv.org:1311.0956, 2013.

\[BKN89\] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima, _On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth,_
Invent. Math. 97 (1989), no. 2, 313–349. MR 90c:53098

\[BL09\] Hubert L. Bray and Dan A. Lee, _On the Riemannian Penrose inequality in dimensions_
_less than eight,_ Duke Math. J. 148 (2009), no. 1, 81–106. MR 2515101 (2010f:53051)

\[Bla00\] David E. Blair, _Spaces of metrics and curvature functionals,_ Handbook of differential
geometry, Vol. I, North-Holland, Amsterdam, 2000, pp. 153–185.

\[BM09\] Simon Brendle and Fernando C. Marques, _Blow-up phenomena for the Yamabe equation. II,_ J. Differential Geom. 81 (2009), no. 2, 225–250. MR 2472174 (2010k:53050)

\[BM11\] Olivier Biquard and Vincent Minerbe, _A Kummer construction for gravitational instantons,_ Comm. Math. Phys. 308 (2011), no. 3, 773–794. MR 2855540 (2012m:53101)

\[BN04\] Hubert L. Bray and Andŕe Neves, _Classification of prime 3-manifolds with Yamabe_ _invariant greater than_ RP3, Ann. of Math. (2) 159 (2004), no. 1, 407–424. MR 2052359
(2005f:53048a)

\[Bog78\] F. A. Bogomolov, _Hamiltonian K¨ahlerian manifolds,_ Dokl. Akad. Nauk SSSR 243
(1978), no. 5, 1101–1104.

* * *

\[Bra01\] Hubert L. Bray, _Proof of the Riemannian Penrose inequality using the positive mass_
_theorem,_ J. Differential Geom. 59 (2001), no. 2, 177–267. MR 1908823 (2004j:53046)

\[Bre05\] Simon Brendle, _Convergence of the Yamabe flow for arbitrary initial energy,_ J. Differential Geom. 69 (2005), no. 2, 217–278. MR 2168505 (2006e:53119)

\[Bre07\], _Convergence of the Yamabe flow in dimension 6 and higher,_ Invent. Math.
170 (2007), no. 3, 541–576. MR 2357502 (2008k:53136)

\[Bre08\], _Blow-up phenomena for the Yamabe equation,_ J. Amer. Math. Soc. 21 (2008),
no. 4, 951–979. MR 2425176 (2009m:53084)

\[BWZ04\] C. B¨ohm, M. Wang, and W. Ziller, _A variational approach for compact homogeneous_
_Einstein manifolds,_ Geom. Funct. Anal. 14 (2004), no. 4, 681–733. MR 2084976
(2005g:53074)

\[Cal82\] Eugenio Calabi, _Extremal K¨ahler metrics,_ Seminar on Differential Geometry, Ann.
of Math. Stud., vol. 102, Princeton Univ. Press, Princeton, N.J., 1982, pp. 259–290.
MR 645743 (83i:53088)

\[Cal85\], _Extremal K¨ahler metrics. II,_ Differential geometry and complex analysis,
Springer, Berlin, 1985, pp. 95–114. MR 780039 (86h:53067)

\[Car98\] Gilles Carron, _Une suite exacte en L_ 2- _cohomologie,_ Duke Math. J. 95 (1998), no. 2,
343–372.

\[CG72\] Jeff Cheeger and Detlef Gromoll, _The splitting theorem for manifolds of nonnegative_
_Ricci curvature,_ J. Differential Geometry 6 (1971/72), 119–128. MR 0303460 (46
#2597)

\[CGY02a\] Sun-Yung A. Chang, Matthew J. Gursky, and Paul Yang, _An a priori estimate for a_
_fully nonlinear equation on four-manifolds,_ J. Anal. Math. 87 (2002), 151–186, Dedicated to the memory of Thomas H. Wolff. MR 1945280 (2003k:53036)

\[CGY02b\] Sun-Yung A. Chang, Matthew J. Gursky, and Paul C. Yang, _An equation of Monge-_
_Amp\`ere type in conformal geometry, and four-manifolds of positive Ricci curvature,_
Ann. of Math. (2) 155 (2002), no. 3, 709–787. MR 1923964 (2003j:53048)

\[Che70\] Jeff Cheeger, _Finiteness theorems for Riemannian manifolds,_ Amer. J. Math. 92
(1970), 61–74. MR 0263092 (41 #7697)

\[Che09\] Szu-Yu Sophie Chen, _Optimal curvature decays on asymptotically locally euclidean_
_manifolds,_ arXiv.org:0911.5538, 2009.

\[CLW08\] Xiuxiong Chen, Claude Lebrun, and Brian Weber, _On conformally K¨ahler, Einstein_
_manifolds,_ J. Amer. Math. Soc. 21 (2008), no. 4, 1137–1168.

\[CS04\] David M. J. Calderbank and Michael A. Singer, _Einstein metrics and complex singularities,_ Invent. Math. 156 (2004), no. 2, 405–443.

\[CS06\], _Toric self-dual Einstein metrics on compact orbifolds,_ Duke Math. J. 133
(2006), no. 2, 237–258. MR 2225692 (2007g:53041)