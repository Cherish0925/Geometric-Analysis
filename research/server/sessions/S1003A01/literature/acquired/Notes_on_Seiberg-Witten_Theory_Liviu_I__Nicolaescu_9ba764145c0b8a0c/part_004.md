---
retention_scope: session
part: 4
total_parts: 13
---

[Part 4/13 of: Notes on Seiberg-Witten Theory Liviu I. Nicolaescu]

$$\
\\hat{\\nabla}^{M}=\\tau^{\*}\\nabla\
$$\
\
$$\
\\mathbb{S}\_{0}\
$$\
\
$$\
\\hat{\\nabla}^{M}=d-\\frac{1}{4}\\sum\_{i,j,k}e^{k}\\otimes\\Omega\_{k i j}\\mathbf{c}(e^{i})\\mathbf{c}(e^{j}).\
$$\
\
It satisfles the following compatibility relation:\
\
$$\
\\hat{\\nabla} _{X}^{M}\\mathbf{c}(\\alpha)=\\mathbf{c}(\\nabla_{X}^{M}\\alpha),\\quad\\forall X\\in\\operatorname{Vect}(M),\\alpha\\in\\Omega^{1}(M).\
$$\
\
Then (S0; c; rM; r^ M) is a Dirac structure called the Dirac structure induced\
by the connection rM. As explained in Sec. 1.3.1, this Dirac structure\
determines a Dirac operator we will call the Dirac operator induced by the\
connection rM.\
\
$$\
(\\mathbb{S}\_{0},\\mathbf{c},\\nabla^{M},\\hat{\\nabla}^{M})\
$$\
\
$$\
\\nabla^{'}M\
$$\
\
$$\
\\nabla^{M}\
$$\
\
Exercise 1.3.19. Suppose (M; g) is a Riemannian spin-manifold and rM\
is a metric connection. The trace of its torsion is the 1-form tr (T) locally\
deflned by\
X\
tr (T)(e)= g(e;T(e; e))\
\
$$\
(M,g)\
$$\
\
$$\
\\nabla^{M}\
$$\
\
$$\
\\mathrm{tr}\\left(T\\right)\\left(e\_{i}\\right)=\\sum\_{k}g\\left(e\_{k},T\\left(e\_{k},e\_{i}\\right)\\right)\
$$\
\
where (ei) is a local orthonormal frame. Show that the induced Dirac operator is formally selfadjoint if and only if the torsion of rM is traceless,\
tr (T) _·_ 0.\
\
$$\
(e\_{i})\
$$\
\
$$\
\\nabla^{M}\
$$\
\
$$\
(T)\\equiv0\
$$\
\
The above construction can be generalized as follows. Given a Hermitian\
vector bundle E! M and a Hermitian connection rE we can deflne a\
geometric Dirac structure\
\
$$\
E\\rightarrow M\
$$\
\
$$\
\\nabla^{E}\
$$\
\
$$\
(\\mathbb{S} _{M}\\otimes E,\\mathbf{c}_{E},\\nabla)\
$$\
\
on _M_ where\
\
$$\
\\mathbf{c} _{E}:\\Omega^{\*}(M)\\stackrel{\\mathbf{c}}{\\to}\\operatorname{End}\\left(\\mathbb{S}_{M}\\right)\\stackrel{\\otimes\\mathbf{I} _{E}}{\\hookrightarrow}\\operatorname{End}\\left(\\mathbb{S}_{M}\\otimes E\\right)\
$$ and r is the connection on SM › E induced by the connection r~ M on SM\
and the connection rE on E. We denote by DM;E the associated geometric\
Dirac operator. We say that DM;E is obtained from DM by twisting with\
the pair (E; rE).\
\
$$\
\\tilde{\\nabla}^{M}\
$$\
\
$$\
\\mathbb{S}\_{M}\\otimes E\
$$\
\
$$\
\\nabla\
$$\
\
$$\
\\nabla^{E}\
$$\
\
$$\
\\mathbb{S}\_{M}\
$$\
\
$$\
\\mathfrak{D}\_{M,E}\
$$\
\
$$\
\\mathfrak{D}\_{M}\
$$\
\
$$\
\\mathfrak{D}\_{M,E}\
$$\
\
$$\
\\left(E,\\nabla^{E}\\right)\
$$\
\
Exercise 1.3.20. Prove that the above triple (SM › E;cE; r) is indeed a\
geometric Dirac structure on _M._\
\
$$\
(\\mathbb{S} _{M}\\otimes E,\\mathbf{c}_{E},\\nabla)\
$$\
\
The curvature of _r_ is\
\
$$\
\\nabla\
$$\
\
$$\
F(\\nabla)=F(\\tilde{\\nabla}^{M})\\otimes\\mathbf{1} _{E}+\\mathbf{1}_{\\mathbb{S}\_{M}}\\otimes F(\\nabla^{E}).\
$$\
\
From the Weitzenb˜ock formula we deduce\
_s_\
\
(1.3.11)\
\
$$\
\\mathfrak{D}\_{M,E}^{2}=\\nabla^{\*}\\nabla+\\frac{s}{4}+\\mathbf{c}(F(\\nabla^{E})).\
$$\
\
s\
The endomorphism R = + c(F (rE)) is the Weitzenb˜ock remainder of the\
4\
generalized Laplacian D2M;E.\
\
$$\
\\mathcal{R}=\\frac{s}{4}+\\mathbf{c}(F(\\nabla^{E}))\
$$\
\
$$\
\\mathfrak{O}\_{M,E}^{2}.\
$$\
\
At this point we want to discuss some features of the above formula\
when dimM is even. In this case SM is Z2-graded\
\
$$\
\\mathbb{S}\_{M}\
$$\
\
$$\
\\mathbb{Z}\_{2^{-}}\
$$\
\
$$\
\\mathbb{S} _{M}=\\mathbb{S}_{M}^{+}\\oplus\\mathbb{S}\_{M}^{-}\
$$\
\
and in particular we obtain a splitting\
\
$$\
\\mathbb{S} _{\\mathit{M}}\\otimes\\mathit{E}=\\mathbb{S}_{\\mathit{M}}^{+}\\otimes\\mathit{E}\\oplus\\mathbb{S}\_{\\mathit{M}}^{-}\\otimes\\mathit{E}.\
$$\
\
With respect to the above grading the operator D\
position\
•\
0\
\
M;E has the block decom-\
‚\
⁄\
D6\
\
$$\
\\mathfrak{D}\_{M,E}\
$$\
\
$$\
\\mathfrak{D} _{M,E}=\\left\[\\begin{array}{c c}0&\\mathfrak{D}_{M,E}^{\*}\ \\mathfrak{D}\_{M,E}&0\\end{array}\\right\]\
$$\
\
¡\
where D6 M;E: C1(S+M › E)! C1(SM › E\
•\
\
). Then\
\
$$\
\\mathfrak{D} _{M,E}:C^{\\infty}(\\mathbb{S}_{M}^{+}\\otimes E)\\to C^{\\infty}(\\mathbb{S}\_{M}^{-}\\otimes E)\
$$\
\
$$\
\\mathfrak{D} _{M,E}^{2}=\\left\[\\begin{array}{c c}{\\mathfrak{D}_{M,E}^{ _}\\mathfrak{D}{M,E}}&{0}\ {0}&{\\mathfrak{D}{M,E}\\mathfrak{D}\_{M,E}^{_}}\ \\end{array}\\right\].\
$$\
\
We conclude that the Weitzenb˜ock remainder\
decomposition\
•\
_R_ 0\
\
R of D2M;E has the block\
‚\
\
$$\
\\mathcal{R}\
$$\
\
$$\
\\mathfrak{D}\_{M,E}^{2}\
$$\
\
$$\
\\mathcal{R}=\\left\[\\begin{array}{c c}\\mathcal{R} _{+}&0\ 0&\\mathcal{R}_{-}\\end{array}\\right\]\
$$\
\
(1.3.12)\
\
When dimM = 4 we can be more speciflc.\
Example 1.3.3 we deduce\
_s_\
\
Using the computation in the\
¡ ¢\
\
$$\
\\mathfrak{D} _{M,E}^{\*}\\mathfrak{D}_{M,E}=\\nabla^{\*}\\nabla+\\frac{s}{4}+\\mathbf{c}\\big(F^{+}(\\nabla^{E})\\big),\
$$\
\
(1.3.13)\
\
$$\
\\mathfrak{D} _{M,E}\\mathfrak{D}_{M,E}^{ _}=\\nabla^{_}\\nabla+\\frac{s}{4}+\\mathbf{c}\\big(F^{-}(\\nabla^{E})\\big)\
$$\
\
where F §(rE) denotes the self/antiself-dual part of the curvature of rE.\
\
$$\
F^{\\pm}(\\nabla^{E})\
$$\
\
$$\
\\nabla^{E}\
$$\
\
* * *\
\
Assume now that _(M; g)_ is an oriented, _n_-dimensional Riemannian manifold equipped with a spinc structure 2 Spinc(M). Denote by (gfifl) a collection of gluing data deflning the SO structure PSO(M) on M with respect\
to some good open cover (Ufi). Moreover, we assume is deflned by the\
data\
h : U! Spinc(n):\
\
$$\
(M,g)\
$$\
\
$$\
\\sigma\\in S p i n^{c}(M)\
$$\
\
$$\
s p i n^{c}\
$$\
\
$$\
\\left(g\_{\\alpha\\beta}\\right)\
$$\
\
$$\
P\_{SO(M)}\
$$\
\
$$\
\\sigma\
$$\
\
$$\
\\left(U\_{\\alpha}\\right)\
$$\
\
$$\
h\_{\\alpha\\beta}:U\_{\\alpha\\beta}\\rightarrow\\mathrm{Spin}^{c}(n).\
$$\
\
Denote by ‰c the fundamental complex spinorial representation\
\
$$\
\\rho^{c}\
$$\
\
$$\
\\rho^{c}:\\operatorname{Spin}^{c}(n)\\to\\operatorname{Aut}\\left(\\mathbb{S}\_{n}\\right).\
$$\
\
We obtain a complex bundle\
\
$$\
\\mathbb{S} _{\\sigma}(M)=P_{S p i n^{c}}\\times\_{\\rho^{c}}\\mathbb{S}\_{n}\
$$\
\
which has a natural Clifiord structure. This is called the _bundle of complex_\
_spinors_ associated to. We want to point out that if _M_ is equipped with a\
_spin_ structure then\
_»=_\
S = S0 › det()12:\
\
$$\
\\sigma.\
$$\
\
$$\
\\mathbb{S} _{\\sigma}\\cong\\mathbb{S}_{0}\\otimes\\operatorname\*{d e t}(\\sigma)^{1/2}.\
$$\
\
We will construct a family of geometric Dirac operators on S (M).\
\
$$\
\\mathbb{S}\_{\\sigma}(M)\
$$\
\
Consider for warm-up the special case when\
assume gfifl · 1 and\
\
_TM_ is trivial. Then we can\
\
$$\
g\_{\\alpha\\beta}\\equiv\\mathbf{1}\
$$\
\
$$\
h\_{\\alpha\\beta}=(\\mathbf{1},z\_{\\alpha\\beta}):U\_{\\alpha\\beta}\\to S p i n(n)\\times S^{1}\\to S p i n^{c}(n).\
$$\
\
The S1-cocycle (z2fifl) deflnes the line bundle det(\
more happens. The collection (zfifl\
^ = det(=\
plex Hermitian line bundle L)1\
\
). In this case something\
) is also an S1-cocycle deflning the com-\
2. Now observe that\
\
$$\
S^{1}\
$$\
\
$$\
(z\_{\\alpha\\beta}^{2})\
$$\
\
$$\
(z\_{\\alpha\\beta})\
$$\
\
$$\
S^{1}\
$$\
\
$$\
\\hat{L}=\\det(\\sigma)^{1/2}\
$$\
\
$$\
\\mathbb{S} _{M,\\sigma}=\\mathbb{S}_{M}\\otimes\\det(\\sigma)^{1/2}.\
$$\
\
We can now twist the Dirac operator D\
_A_ is a Hermitian connection on det()1\
SM;. Notice that if the collection\
\
=\
M with a pair (det()12; A), where\
=2\
and obtain a Dirac operator on\
\
$$\
\\mathfrak{D}\_{M}\
$$\
\
$$\
(\\det(\\sigma)^{1/2},A)\
$$\
\
$$\
(\\sigma)^{1/2}\
$$\
\
$$\
\\mathbb {S} \_ {M, \\sigma}\
$$\
\
$$\
{\\omega\_{\\alpha}\\in\\underline{{u}}(1)\\otimes\\Omega^{1}(U\_{\\alpha})}\
$$\
\
deflnes a connection on det(), i.e.\
\
$$\
\\omega\_ {\\beta} = \\frac {d z \_ {\\alpha \\beta} ^ {2}}{z \_ {\\alpha \\beta} ^ {2}} + \\omega\_ {\\alpha} \\mathrm {o v e r} U \_ {\\alpha \\beta}\
$$\
\
then the collection\
\
$$\
\\hat {\\omega} \_ {\\alpha} = \\frac {1}{2} \\omega\_ {\\alpha}\
$$\
\
deflnes a Hermitian connection on _L_\
the curvature of (!fi) then the curvature of (^\
1\
\
^ = det(=\
)12. Moreover if F denotes\
!fi) is given by\
\
$$\
\\hat {L} = \\det (\\sigma) ^ {1 / 2}\
$$\
\
$$\
\\left(\\omega\_ {\\alpha}\\right)\
$$\
\
$$\
\\left(\\hat {\\omega} \_ {\\alpha}\\right)\
$$\
\
(1.3.14)\
\
$$\
\\hat {F} = \\frac {1}{2} F.\
$$\
\
* * *\
\
Hence any connection on det() deflnes\
S (M).\
\
in a unique way connection on\
\
$$\
\\mathbb {S} \_ {\\sigma} (M)\
$$\
\
Assume now that _TM_ is not necessarily trivial. We can however cover\
M by open sets (Ufi) such that each T Ufi is trivial. If we pick from the start\
a connection on det() this induces a Clifiord connection on each SUfi;.\
These can be glued back to a Clifiord connection on SM; using partitions\
of unity. We let the reader check the connection obtained in this way is\
independent of the various choices.\
\
$$\
\\left(U \_ {\\alpha}\\right)\
$$\
\
$$\
T U \_ {\\alpha}\
$$\
\
$$\
(\\sigma)\
$$\
\
$$\
\\mathbb {S} \_ {M, \\sigma}\
$$\
\
$$\
\\mathbb {S} \_ {U \_ {\\alpha}, \\sigma}.\
$$\
\
**Exercise 1.3.21.** Suppose _(M; g)_ is an oriented Riemannian manifold\
equipped with a spinc structure and A is a Hermitian connection on\
det(). Denote by r^ A the connection on S induced by A. Given a smooth\
⁄^¡\
map : M!U(1) ‰ C we can construct a new connection rA1. Show\
that this connection is induced by the connection _A ¡_ 2(d) ¡1on det().\
In particular, the assignment\
\
$$\
(M, g)\
$$\
\
$$\
s p i n ^ {c}\
$$\
\
$$\
\\sigma\
$$\
\
$$\
(\\sigma)\
$$\
\
$$\
\\hat {\\nabla} ^ {A}\
$$\
\
$$\
\\mathbb {S} \_ {\\sigma}\
$$\
\
$$\
\\gamma : M \\rightarrow U (1) \\subset \\mathbb {C} ^ {\*}\
$$\
\
$$\
\\gamma \\hat {\\nabla} ^ {A} \\gamma^ {- 1}\
$$\
\
$$\
A - 2 (d \\gamma) \\gamma^ {- 1}\
$$\
\
$$\
(\\gamma , A) \\mapsto A - 2 (d \\gamma) \\gamma^ {- 1}\
$$\
\
deflnes a smooth left action of the gauge group GU(1)\
of Hermitian connection on det().\
\
(det()) on the space\
\
$$\
\\mathcal {G} \_ {U (1)} \\left(\\det (\\sigma)\\right)\
$$\
\
# Let A be a connection on det(). Denote by rA the Clifiord connection it induces on SM; and by DA:= DM;A the geometric Dirac operator associated to the geometric Dirac structure (SM;; c; rA). The Weitzenb˜ock remainder of D2M;A is a local object so in order to determine its form we can\
\
work on Ufi where SUfi;= SUfi› det()j1Ufi2. Using the equalities (1.3.11)\
and (1.3.14) we deduce\
\
$$\
(\\sigma)\
$$\
\
$$\
\\nabla^ {A}\
$$\
\
$$\
\\mathbb {S} \_ {M, \\sigma}\
$$\
\
$$\
\\mathfrak {D} \_ {A} := \\mathfrak {D} \_ {M, A}\
$$\
\
$$\
\\left(\\mathbb {S} \_ {M, \\sigma}, \\mathbf {c}, \\nabla^ {A}\\right)\
$$\
\
$$\
\\mathfrak {D} \_ {M, A} ^ {2}\
$$\
\
$$\
U \_ {\\alpha}\
$$\
\
$$\
\\mathbb{S} _{U_{\\alpha},\\sigma}=\\mathbb{S} _{U_{\\alpha}}\\otimes\\det(\\sigma)\\big\| _{U_{\\alpha}}^{1/2}\
$$\
\
(1.3.15)\
\
$$\
\\mathfrak{D} _{\\sigma,A}^{2}=(\\nabla^{A})^{\*}\\nabla^{A}+\\frac{1}{4}s+\\frac{1}{2}\\mathbf{c}(F_{A})\
$$\
\
where _FA_ denotes the curvature of the connection _A_ on det(). If _M_ is\
four-dimensional then we have a splitting\
\
$$\
F \_ {A}\
$$\
\
$$\
\\mathbb{S} _{M,\\sigma}=\\mathbb{S}_{M,\\sigma}^{+}\\oplus\\mathbb{S}\_{M,\\sigma}^{-}\
$$\
\
and\
\
(1.3.16)\
\
$$\
\\mathfrak{D} _{A}^{\*}\\mathfrak{D}_{A}=(\\nabla^{A})^{\*}\\nabla^{A}+\\frac{s}{4}+\\frac{1}{2}\\mathbf{c}(F\_{A}^{+}).\
$$\
\
**Exercise 1.3.22.** Suppose _M_ is a Riemannian manifold equipped with a\
spinc structure and A is a Hermitian connection on det(). Show that for\
any imaginary 1-form ia 2 i›1(M) we have\
\
$$\
\\in\\mathrm{i}\\Omega^{1}(M)\
$$\
\
$$\
\\mathfrak{D} _{A+\\mathbf{i}a}=\\mathfrak{D}_{A}+\\frac{1}{2}\\mathbf{c}(\\mathbf{i}a).\
$$\
\
* * *\
\
The space Spinc(M) ofspinc structures on M is equipped with a natural\
involution 7! „. It can be described as follows. Suppose is a spinc\
structure given by a cocycle (hfifl; zfifl). Then „ is the spinc-structure deflned\
by the cocycle (hfifl; z„fifl). We let the reader verify that the isomorphism\
class of „ depends only on the isomorphism class of. This involution\
enjoys several nice features.\
\
$$\
\\mathit{Spin}^{c}(M)\
$$\
\
$$\
spin^{c}\
$$\
\
$$\
\\sigma\\mapsto\\bar{\\sigma}\
$$\
\
$$\
\\sigma\
$$\
\
$$\
spin^{c}\
$$\
\
$$\
\\left(h\_{\\alpha\\beta},z\_{\\alpha\\beta}\\right)\
$$\
\
$$\
\\bar{\\sigma}\
$$\
\
$$\
spin^{c\_{\\mathrm{l}}}\
$$\
\
$$\
\\left(h\_{\\alpha\\beta},\\bar{z}\_{\\alpha\\beta}\\right)\
$$\
\
$$\
\\bar{\\sigma}\
$$\
\
$$\
\\sigma.\
$$\
\
Exercise 1.3.23. (a) For every 2 Spinc(M) there exists a natural isomorphism of complex line bundles.\
\
$$\
\\sigma\\in{S p i n}^c(M)\
$$\
\
$$\
\\det(\\bar{\\sigma})\\cong\\overline{\\det(\\sigma)}\
$$\
\
(b)⁄ If dimM = 4 then there exist natural isomorphisms of complex vector\
bundles\
\
$$\
(b)^{\*}If\
$$\
\
(1.3.17)\
\
$$\
\\vartheta:\\bar{\\mathbb{S}} _{\\sigma}^{+}\\to\\mathbb{S}_{\\bar{\\sigma}}^{+},\\quad\\vartheta^{\\sharp}:\\bar{\\mathbb{S}} _{\\sigma}^{-}\\to\\mathbb{S}_{\\bar{\\sigma}}^{-}\
$$\
\
such that for every 1-form _fi_ on _M_ we have the equality\
„)\
\
$$\
\\vartheta^{\\sharp}\\left(\\overline{{\\mathbf{c} _{\\sigma}(\\alpha)\\psi}}\\right)=\\mathbf{c}_{\\bar{\\sigma}}(\\alpha)\\vartheta(\\bar{\\psi})\
$$\
\
where **c** denotes the Clifiord multiplication on the bundle S. Moreover,\
for every ˆ 2 C1(S+) we have the equality\
„)) =\
\
$$\
\\mathbf{c}\_{\\sigma}\
$$\
\
$$\
\\mathbb{S}\_{\\sigma}\
$$\
\
$$\
\\psi\\in C^{\\infty}(\\mathbb{S}\_{\\sigma}^{+})\
$$\
\
(1.3.18)\
\
$$\
q\\left(\\vartheta\\left(\\bar{\\psi}\\right)\\right)=-q\\left(\\psi\\right)\
$$\
\
where q(ˆ) denotes the endomorphism ` 7! h`; ˆî ¡ 12ĵj2\`. (The Hermitian metric is assumed to be complex linear in the _flrst_ variable.)\
\
$$\
q(\\psi)\
$$\
\
$$\
\\phi\\mapsto\\langle\\phi,\\psi\\rangle\\psi-\\frac{1}{2}\|\\psi\|^{2}\\phi\
$$\
\
(c) Show that for every Hermitian connection _A_ on det() and for every\
ˆ 2 C1(S+) we have the identity\
„)\
\
$$\
\\psi\\in C^{\\infty}(\\mathbb{S}\_{\\sigma}^{+})\
$$\
\
(1.3.19)\
\
$$\
\\vartheta^{\\sharp}\\left(\\overline{{\\mathfrak{D} _{A}\\psi}}\\right)=\\mathfrak{D}_{A^{\*}}\\vartheta\\left(\\bar{\\psi}\\right)\
$$\
\
⁄\
where _A_\
\
» ⁄\
denotes the connection induced by _A_ on det „ = (det).\
\
$$\
A^{\*}\
$$\
\
$$\
\\bar{\\sigma}\\cong(\\det\\sigma)^\*\
$$\
\
Hint for (b). If ‰§: Spin(4)! SO(S4+) denotes the even/odd spinor\
representation then there exists a complex linear isomorphism C§: S4§!\
S4§ such that C§ – ‰§ =„ ‰§. More precisely, if we identify Spin(4) with\
SU(2)£ SU(2) and SU(2) with the group of unit quaternions then S4+ is the\
space of quaternions H equipped with the complex structure given by Ri, the\
right multiplication by i. For (q+; q¡) 2 Spin(4) the map ‰(q+; q¡) 2 SO(H)\
is described by Lq+, the left multiplication by q+. The morphism C§ is then\
given by Rj, the right multiplication by j. The description of C¡is obtained\
from the above by making the changes\
\
$$\
\\rho\_{\\pm}:\\mathrm{Spin}(4)\\rightarrow\\mathrm{SO}(\\mathbb{S}\_{4}^{+})\
$$\
\
$$\
C \_ {\\pm}: \\mathbb {S} \_ {4} ^ {\\pm} \\rightarrow\
$$\
\
$$\
\\overline{\\mathbb{S}}\_{4}^{\\pm}\
$$\
\
$$\
C\_{\\pm}\\circ\\rho\_{\\pm}=\\bar{\\rho}\_{\\pm}\
$$\
\
$$\
S p i n(4)\
$$\
\
$$\
SU(2)\\times SU(2)\
$$\
\
$$\
SU(2)\
$$\
\
$$\
\\mathbb{S}\_{4}^{+}\
$$\
\
$$\
(q\_{+},q\_{-})\\in\\mathrm{S p i n(4)}\
$$\
\
$$\
R\_{\\mathbf{i}},\
$$\
\
$$\
\\rho(q\_{+},q\_{-})\\in S O(\\mathbb{H})\
$$\
\
$$\
L\_{q\_{+}}\
$$\
\
$$\
q\_{+}\
$$\
\
$$\
R\_{\\mathbf{j}}\
$$\
\
$$\
C\_{\\pm}\
$$\
\
$$\
C\_{-}\
$$\
\
$$\
\\mathrm{left}\\leftrightarrow\\mathrm{right}\\quad\\mathrm{and}\\quad\\rho\_{+}\\big(q\_{+},q\_{-}\\big)=L\_{q\_{+}}\\leftrightarrow\\rho\_{-}\\big(q\_{+},q\_{-}\\big)=R\_{q\_{-}^{-1}}.\
$$\
\
Suppose now that _M_ is a closed, compact, oriented 4-manifold equipped\
with a spinc structure. Upon choosing a connection A on the associated line bundle det we obtain a Dirac operator\
\
$$\
\\sigma\
$$\
\
$$\
\\mathfrak{D} _{A}:C^{\\infty}(\\mathbb{S}_{\\sigma}^{+})\\to C^{\\infty}(\\mathbb{S}\_{\\sigma}^{-}).\
$$\
\
This is an elliptic operator which has a flnite index\
\
$$\
\\mathrm{ind} _{\\mathbb{C}}(\\mathfrak{D}_{A})=\\dim\_{\\mathbb{C}}\\ker\\mathfrak{D} _{A}-\\dim_{\\mathbb{C}}\\ker\\mathfrak{D}\_{A}^{\*}.\
$$\
\
According to the celebrated Atiyah-Singer index theorem this index can be\
expressed in purely topological terms. More precisely, we have the following\
equality:\
Z ¶\
\
(1.3.20)\
\
$$\
\\mathrm{ind} _{\\mathbb{C}}\\mathfrak{D}_{A}=\\frac{1}{8}\\left(\\int\_{M}c\_{1}(\\det\\sigma)\\wedge c\_{1}(\\det\\sigma)-\\tau(M)\\right)\
$$\
\
where _¿_ (M) denotes the signature of the manifold _M._\
\
$$\
\\tau(M)\
$$\
\
#### 1.4. Complex difierential geometry\
\
We present here a very brief survey of some basic difierential geometric facts\
about complex manifolds in general, and complex surfaces in particular.\
We will return to this subject later on, in Section 3.1. This is an immense\
research area and our selection certainly does not do it justice. For more\
details and examples we refer to **\[9, 10, 49, 54, 63\]** and the sources therein.\
\
**1.4.1. Elementary complex difierential geometry.** An _almost complex_\
_structure_ on a manifold _X_ is an endomorphism _J_ of the tangent bundle _TX_\
such that _J2_ = ¡1\. Note in particular that such a structure can exist only\
on _orientable_ even-dimensional manifolds. By duality we get a similar endomorphism of the cotangent bundle _T ⁄X_ which we continue to denote by\
_J._\
\
$$\
J^{2}=-1\
$$\
\
$$\
T^{\*}X\
$$\
\
$$\
J.\
$$\
\
The operator _J_ extends by complex linearity to an endomorphism of the\
complexifled tangent _TX ›_ C. It deflnes two eigenbundles corresponding to\
the eigenvalues _§i_ and thus it produces a splitting of complex bundles\
\
$$\
TX\\otimes\\mathbb{C}\
$$\
\
$$\
TX\\otimes\\mathbb{C}=(TX)^{1,0}\\oplus(TX)^{1,0}\
$$\
\
where the (1;0) superscript indicates the **i**-eigenbundle while the (0;1)-\
superscript indicates the _¡i_-eigenbundle. Note that _(T X;J)_ is isomorphic\
to (TX)1;0 as complex vector bundles. Denote by P 1;0 (resp. P 1;0) the projection onto (TX)1;0 (resp. (TX)0;1) corresponding to the above splitting.\
\
$$\
(0,1)-\
$$\
\
$$\
(TX,J)\
$$\
\
$$\
(TX)^{1,0}\
$$\
\
$$\
P^{1,0}(resp.P^{1,0})\
$$\
\
$$\
(TX)^{1,0}\
$$\
\
$$\
(T X)^{0,1})\
$$\
\
For any vector fleld X on M deflne Xc:= P 1;0X = 1/2(X ¡ iJX) and\
„⁄\
Xc:= P 0;1X = 1/2(X + iJX). By duality, these induce projectors of T X ›C\
and thus we get a similar splitting\
\
$$\
X\_{c}:=P^{1,0}X=\\frac{1}{2}(X-\\mathrm{i}JX)\
$$\
\
$$\
\\bar{X}\_{c}:=P^{0,1}X=\\frac{1}{2}(X+\\mathrm{i}JX)\
$$\
\
$$\
T^{\*}X\\otimes\\mathbb{C}\
$$\
\
(1.4.1)\
\
$$\
T^{ _}X\\otimes\\mathbb{C}=(T^{_}X)^{1,0}\\oplus(T^{\*}X)^{0,1}\
$$ which leads to a decomposition\
\
(1.4.2)\
\
$$\
\\Lambda^{k}T^{ _}X\\otimes\\mathbb{C}=\\bigoplus\_{p+q=k}\\Lambda^{p,q}T^{_}X.\
$$\
\
where\
\
$$\
\\Lambda^{p,q}T^{ _}X\\cong\\Lambda^{p}(T^{_}X)^{1,0}\\otimes\\Lambda^{q}(T^{\*}X)^{0,1}.\
$$\
\
⁄\
The sections of ⁄p;qT X are called (p,q)-forms\
›1(M) › C then fi extends to a C1(M;\
\
on _X._ For example, if _fi 2_\
C)-linear map\
\
$$\
\\Lambda^{p,q}T^{\*}X\
$$\
\
$$\
(p,q)-form s\
$$\
\
$$\
\\alpha\\in\
$$\
\
$$\
\\Omega^{1}(M)\\otimes\\mathbb{C}\
$$\
\
$$\
C^{\\infty}(M,\\mathbb{C})-\
$$\
\
$$\
\\mathrm{Vect}(M)\\otimes\\mathbb{C}\\rightarrow C^{\\infty}(M,\\mathbb{C})\
$$\
\
and\
\
$$\
\\alpha=\\alpha^{1,0}+\\alpha^{0,1}\
$$\
\
where fi1;0(X):=fi(P 1;0X) and fi0;1(Y):=fi\
\
(P 0;1Y).\
\
$$\
\\alpha^{1,0}(X):=\\alpha(P^{1,0}X)\
$$\
\
$$\
\\alpha^{0,1}(Y):=\\alpha(P^{0,1}Y).\
$$\
\
Example 1.4.1. Consider the manifold Cn with coordinates zj = xj \+ iyj,\
_j_ = _1; ¢¢¢; n._ It is equipped with a natural almost complex structure deflned\
by\
@ @ @\
\
$$\
\\mathbb{C}^n\
$$\
\
$$\
z\_{j}=x\_{j}+\\mathbf{i}y\_{j}\
$$\
\
$$\
j=1,\\cdots,n\
$$\
\
$$\
J:\\quad\\frac{\\partial}{\\partial x\_{j}}\\mapsto\\frac{\\partial}{\\partial y\_{j}}\\mapsto-\\frac{\\partial}{\\partial x\_{j}}.\
$$\
\
⁄\
The complex bundle (T Cn)1;0 (resp (T Cn)0;1) admits a global trivialization\
deflned by\
_@_ 1 _@ @_\
\
$$\
(T\\mathbb{C}^n)^{1,0}\\left(\\mathrm{resp};(T^\*\\mathbb{C}^n)^{0,1}\\right)\
$$\
\
$$\
\\frac{\\partial}{\\partial z\_{j}}:=\\frac{1}{2}\\big(\\frac{\\partial}{\\partial x\_{j}}-\\mathbf{i}\\frac{\\partial}{\\partial y\_{j}}\\big)\
$$\
\
and respectively\
\
$$\
d z\_{j}:=d x\_{j}+\\mathbf{i}d y\_{j}.\
$$\
\
⁄\
Similarly (T Cn)0;1 (resp. (T Cn)0;1) is globally trivialized by\
\
$$\
(T\\mathbb{C}^n)^{0,1}\
$$\
\
$$\
\\left(T^{\*}\\mathbb{C}^{n}\\right)^{0,1})\
$$\
\
$$\
\\frac{\\partial}{\\partial\\bar{z} _{j}}:=\\frac{1}{2}\\big(\\frac{\\partial}{\\partial x_{j}}+\\mathbf{i}\\frac{\\partial}{\\partial y\_{j}}\\big)\
$$\
\
and respectively\
\
$$\
d\\bar{z} _{j}=\\left(d x_{j}-\\mathbf{i}d y\_{j}\\right).\
$$\
\
$$\
(p,q)\
$$\
\
A (p; q)-form on Cn has the form\
X\
\
$$\
\\mathbb{C}^n\
$$\
\
$$\
\\alpha = \\sum\_ {I, J} \\alpha\_ {I J} d z ^ {I} \\otimes \\wedge d \\bar {z} ^ {J}\
$$\
\
where the summation is carried over all ordered multi-indices\
\
$$\
I:\\quad1\\leq i\_{1}<\\cdots<i\_{p}\\leq n,\\quad J:\\quad1\\leq j\_{1}<\\cdots<j\_{q}\\leq n\
$$\
\
and fiIJ is a complex valued function on Cn.\
\
$$\
\\alpha\_{IJ}\
$$\
\
$$\
\\mathbb {C} ^ {n}\
$$\
\
* * *\
\
The exterior derivative extends by complex linearity to an operator\
¡ ¢ ¡ ¢\
\
$$\
d:C^{\\infty}\\big(\\Lambda^{k}T^{ _}X\\otimes\\mathbb{C}\\big)\\rightarrow C^{\\infty}\\big(\\Lambda^{k+1}T^{_}X\\otimes\\mathbb{C}\\big).\
$$\
\
It is not di–cult to check that\
\
$$\
d \\left(\\Lambda^ {p, q}\\right) \\subset \\Lambda^ {p + 2, q - 1} \\oplus \\Lambda^ {p + 1, q} \\oplus \\Lambda^ {p, q + 1} \\oplus \\Lambda^ {p - 1, q + 2}.\
$$\
\
Accordingly, we get a decomposition of\
\
_d_\
\
$$\
d = d ^ {2, - 1} + d ^ {1, 0} + d ^ {0, 1} + d ^ {- 1, 2}.\
$$\
\
Traditionally one uses the notation\
\
$$\
\\partial := d ^ {1, 0}, \\quad \\bar {\\partial} := d ^ {0, 1}.\
$$\
\
The almost complex structure is said to be\
0.\
\
_integrable_\
\
;¡1 ¡1;2\
if _d2_ = 0 and _d_ =\
\
$$\
d ^ {2, - 1} = 0\
$$\
\
$$\
d ^ {- 1, 2} =\
$$\
\
**Proposition 1.4.2.** _Consider an almost complex manifold_ ( _M; J).The following conditions are equivalent._\
\
_(a) The almost complex structure is integrable._\
\
;¡ ¡\
(b) d21fi = d 1;2fi =0for all fi 2 ›1(M) › C.\
„ 1\
\
$$\
d ^ {2, - 1} \\alpha = d ^ {- 1, 2} \\alpha = 0\
$$\
\
$$\
\\alpha \\in \\Omega^ {1} (M) \\otimes \\mathbb {C}.\
$$\
\
$$\
\\bar {\\partial} ^ {2} f = 0 = \\partial^ {2} f, \\forall f \\in C ^ {\\infty} (M)\
$$\
\
(d) The Nijenhuis tensor N 2 ›2(TM) deflned by\
1\
\
$$\
N \\in \\Omega^ {2} (T M)\
$$\
\
$$\
N (X, Y) = \\frac {1}{4} \\left(\[ J X, J Y \] - \[ X, Y \] - J \[ X, J Y \] - J \[ J X, Y \]\\right),\
$$\
\
_8X; Y 2_ Vect ( _M), is identically zero._\
\
$$\
\\forall X, Y \\in \\operatorname {V e c t} (M)\
$$\
\
**Proof** Clearly (a)) (b). Using a partition of unity it is not di–cult to\
prove the converse, (b)) (a).\
\
$$\
(\\mathrm {a}) \\Rightarrow (\\mathrm {b})\
$$\
\
$$\
(\\mathrm {b}) \\Rightarrow (\\mathrm {a})\
$$\
\
Clearly (b)) (c). Using partitions of unity we can replace the condition\
\\8fi 2 ›1(M)" in (b) by the condition \\8fi = f dg, f; g 2 C1(M)". This\
weaker, equivalent version of (b) is clearly implied by (c). To establish the\
remaining equivalences we need to establish several identities of independent\
interest.\
\
$$\
(\\mathrm {b}) \\Rightarrow (\\mathrm {c})\
$$\
\
$$\
“ \\forall \\alpha \\in \\Omega^ {1} (M)”\
$$\
\
$$\
“ \\forall \\alpha = f d g, f, g \\in C ^ {\\infty} (M)”\
$$\
\
Let f 2 C1(M). Then\
\
$$\
f \\in C ^ {\\infty} (M)\
$$\
\
$$\
\\begin{array}{l} \\partial^ {2} f \\left(X \_ {c}, Y \_ {c}\\right) = d \\partial f \\left(X \_ {c}, Y \_ {c}\\right) = X \_ {c} \\partial f \\left(Y \_ {c}\\right) - Y \_ {c} \\partial f \\left(X \_ {c}\\right) - \\partial f \\left(\\left\[ X \_ {c}, Y \_ {c} \\right\]\\right) \ = X \_ {c} d f \\left(Y \_ {c}\\right) - Y \_ {c} d f \\left(X \_ {c}\\right) - d f \\left(\[ X \_ {c}, Y \_ {c} \] \_ {c}\\right). \ \\end{array}\
$$\
\
We compute each of the terms separately.\
n\
1\
\
$$\
X \_ {c} d f \\left(Y \_ {c}\\right) = \\frac {1}{4} \\left{X d f (Y) - J X d f (J Y) - \\mathbf {i} \\left(X d f (J Y) + J X d f (Y)\\right) \\right}.\
$$\
\
$$\
\\begin{array}{l} Y \_ {c} d f \\left(X \_ {c}\\right) = \\frac {1}{4} \\left{Y d f (X) - J Y d f (J Y) - \\mathbf {i} \\left(Y d f (J X) + J Y d f (X)\\right) \\right}. \ d f \\left(\\left\[ X \_ {c}, Y \_ {c} \\right\] \_ {c}\\right) = \\frac {1}{2} d f \\left(\\left\[ X \_ {c}, Y \_ {c} \\right\] - \\mathbf {i} J \\left\[ X \_ {c}, Y \_ {c} \\right\]\\right) \ \\end{array}\
$$\
\
* * *\
\
$$\
\\begin{array}{l} = \\frac {1}{8} d f (\[ X - \\mathbf {i} J X, Y - \\mathbf {i} J Y \]) - \\frac {\\mathbf {i}}{8} d f (J \[ X - \\mathbf {i} J X, Y - \\mathbf {i} J Y \]) \ = \\frac {1}{8} d f (\[ X, Y \] - \[ J X, J Y \] - \\mathbf {i} \[ J X, Y \] - \\mathbf {i} \[ X, J Y \]) \ - \\frac {\\mathbf {i}}{8} d f (J \[ X, Y \] - J \[ J X, J Y \] - \\mathbf {i} J \[ J X, Y \] - \\mathbf {i} J \[ X, J Y \]) \ = \\frac {1}{8} d f (\[ X, Y \] - \[ J X, J Y \] - J \[ J X, Y \] - J \[ X, J Y \]) \ - \\frac {\\mathbf {i}}{8} d f (J \[ X, Y \] - J \[ J X, J Y \] + \[ J X, Y \] + \[ X, J Y \]). \ \\end{array}\
$$\
\
At this point we use the equality _d2f_ = 0 which implies\
\
$$\
d ^ {2} f = 0\
$$\
\
$$\
U d f (V) - V d f (V) = d f (\[ U, V \]), \\forall U, V \\in \\operatorname {V e c t} (M).\
$$\
\
We deduce\
\
$$\
\\begin{array}{l} X \_ {c} d f \\left(Y \_ {c}\\right) - Y \_ {c} d f \\left(Y \_ {c}\\right) = \\frac {1}{4} \\left{d f (\[ X, Y \]) - d f (\[ J X, J Y \]) \\right} \ - \\frac {\\mathbf {i}}{4} \\left{d f (\[ X, J Y \] + d f (\[ J X, Y \]) \\right}. \ \\end{array}\
$$\
\
Putting together all of the above we deduce\
\
$$\
\\begin{array}{l} \\partial^ {2} f (X, Y) = \\partial^ {2} f \\left(X \_ {c}, Y \_ {c}\\right) = \\frac {1}{8} d f \\left(\[ X, Y \] - \[ J X, J Y \] + J \[ J X, Y \] + J \[ X, J Y \]\\right) \ + \\frac {\\mathbf {i}}{8} d f \\left(J \[ X, Y \] - J \[ J X, J Y \] + J \[ J X, Y \] + J \[ X, J Y \]\\right) \ = - d f \\left(\\overline {{N (X , Y)}} \_ {c}\\right) = - \\bar {\\partial} f \\left(N (X, Y)\\right). \ \\end{array}\
$$\
\
Similarly\
\
$$\
\\bar {\\partial} ^ {2} f (X, Y) = - \\partial f (N).\
$$\
\
It is now clear that (c) _()_ (d). ¥\
\
$$\
(\\mathrm {c}) \\Longleftrightarrow (\\mathrm {d})\
$$\
\
It is very easy to show that if _M_ is a complex manifold (i.e. admits local\
coordinates U ! Cn with holomorphic transition maps) then the induced\
almost complex structure is integrable. The converse is also true but it is\
highly nontrivial. It is known as the _Newlander-Nirenberg theorem._\
\
$$\
U \\rightarrow \\mathbb {C} ^ {n}\
$$\
\
Suppose now that _M_ is an _almost Hermitian_ manifold, i.e. _TM_ is\
equipped with a Riemannian metric _g_ and a compatible almost complex\
⁄\
structure J, i.e. J = ¡J. Extend J to an almost complex structure J\[on\
⁄\
_T X_ via the metric duality so that\
\
$$\
J^{\*}=-J\
$$\
\
$$\
g\
$$\
\
$$\
J ^ {\\flat}\
$$\
\
$$\
T^{\*}X\
$$\
\
$$\
(J^{\\flat}\\alpha)(X)=-\\alpha(J X).\
$$\
\
We obtain an eigenbundle decomposition\
\
$$\
T^{ _}X\\otimes\\mathbb{C}\\cong\\ker(\\mathbf{i}-J^{\\flat})\\oplus\\ker(\\mathbf{i}+J^{\\flat})\\cong(T^{_}X)^{1,0}\\oplus(T^{\*}X)^{0,1}\
$$ which coincides with the splitting in (1.4.1). Now deflne! 2 ›2(M) by\
\
$$\
\\omega\\in\\Omega^{2}(M)\
$$\
\
$$\
\\omega(X,Y)=g(J X,Y),\\quad\\forall X,Y\\in\\operatorname{Vect}{(M)}.\
$$\
\
Note that! 2 ›1;1(M). We can now deflne a Hermitian metric on the\
complex bundle _(T X;J)_ by\
\
$$\
\\omega\\in\\Omega^{1,1}(M)\
$$\
\
$$\
h(X,Y)=g(X,Y)-\\mathrm{i}\\omega(X,Y).\
$$\
\
It is often very useful to have local descriptions of the various notions. Pick\
a local orthonormal frame of _TM_\
\
$$\
\\left{e\_{1},f\_{1};\\cdots;e\_{n},f\_{n}\\right},f\_{k}=J e\_{k}.\
$$\
\
p1\
Then "j = (ej ¡ ifj) form a local, complex, unitary frame of T 1;0 while\
2\
p1\
"„j = (ei \+ ifj) form a local, complex, unitary frame of T 0;1. If we denote\
2\
by (ej;fj) the dual basis of (ej; fj) then\
\
$$\
\\varepsilon\_{j}=\\frac{1}{\\sqrt{2}}(e\_{j}-\\mathbf{i}f\_{j})\
$$\
\
$$\
T^{1,0}\
$$\
\
$$\
\\bar{\\varepsilon} _{j}=\\frac{1}{\\sqrt{2}}(e_{i}+\\mathbf{i}f\_{j})\
$$\
\
$$\
T^{0,1}\
$$\
\
$$\
(e\_{j},f\_{j})\
$$\
\
$$\
(e^{j},f^{j})\
$$\
\
$$\
\\varepsilon^{j}=\\frac{1}{\\sqrt{2}}(e^{j}+\\mathbf{i}f^{j})\
$$\
\
⁄\
is a local unitary frame of (T X)1;0 and\
\
$$\
(T^{\*}X)^{1,0}\
$$\
\
$$\
\\bar{\\varepsilon}^{k}:=\\frac{1}{\\sqrt{2}}(e^{k}-\\mathbf{i}f^{k})\
$$\
\
⁄\
is a local unitary frame of (T X)0;1. Then\
X\
\
$$\
(T^{\*}X)^{0,1}\
$$\
\
$$\
\\omega=\\mathbf{i}\\sum\_{j}\\varepsilon^{j}\\wedge\\bar{\\varepsilon}^{j}.\
$$\
\
If _D_ denotes the Levi-Civita connection then we have the following identity\
(see \[ **64,** IX, x4, vol.2\]):\
\
$$\
(D\_{X}\\omega)(Y,Z)=g((D\_{X}J)Y,Z)\
$$\
\
(1.4.3)\
\
$$\
=-\\frac{1}{2}d\\omega(X,J Y,J Z)+\\frac{1}{2}d\\omega(X,Y,Z)+2g(N(Y,Z),J X).\
$$\
\
**Exercise 1.4.1.**\
\
Prove the identity (1.4.3).\
\
to\
\
Suppose now that _d!_ = 0\. The identity (1.4.3) simplifles dramatically\
\
$$\
d\\omega=0\
$$\
\
(1.4.4)\
\
$$\
(D\_{X}\\omega)(Y,Z)=g((D\_{X}J)Y,Z)=2g(N(Y,Z),J X).\
$$\
\
**Deflnition 1.4.3.** An almost Hermitian manifold _(M; g; J)_ is said to be\
_almost K˜ahler_ if the form! is closed. An almost K˜ahler manifold _(M; g; J)_\
is said to be _K˜ahler_ if the almost complex structure _J_ is integrable.\
\
$$\
\\left(M,g,J\\right)\
$$\
\
* * *\
\
Exercise 1.4.2. Suppose (M2n;!) is a symplectic manifold , i.e! is a\
closed 2-form amd!n is a volume form on M. Show that there exist almost\
K¶ahler structures _(g; J)_ onM such that\
\
$$\
\\left(M^{2n},\\omega\\right)\
$$\
\
$$\
\\omega\
$$\
\
$$\
\\omega^{n}\
$$\
\
$$\
(g,J)\
$$\
\
$$\
\\omega(X,Y)=g(J X,Y),\\quad\\forall X,Y\\in\\operatorname{Vect}{(M)}.\
$$\
\
In this case both _g_ are said to be _adapted_ to!. Moreover, show that when\
_n_ = 2 the symplectic form! is self-dual with respect to any adapted metric.\
\
$$\
\\omega\
$$\
\
$$\
\\omega\
$$\
\
$$\
n=2\
$$\
\
Using the metric duality we can regard any tensor B 2 ›2(TM) asa\
⁄\
_T M_-valued 2-form\
\
$$\
B\\in\\Omega^{2}(TM)\
$$\
\
$$\
T^{\*}M.\
$$\
\
$$\
\\langle B(X,Y),Z\\rangle:=g(B(X,Y),Z),\\quad\\forall X,Y,Z\\in\\operatorname{Vect}\\left(M\\right)\
$$\
\
where _h¢; ¢i_ denotes the duality between _T ⁄M_ and _TM._ Now deflne the\
_Bianchi projector_\
\
$$\
\\langle\\cdot,\\cdot\\rangle\
$$\
\
$$\
T^{\*}M\
$$\
\
$$\
\\mathfrak{b}B(X,Y,Z)=\\langle B(X,Y),Z\\rangle+\\langle B(Z,X),Y\\rangle+\\langle B(Y,Z),X\\rangle.\
$$\
\
Then _bN_ is a 3-form. If _d!_ = 0 then using the elementary identity\
\
$$\
d\\omega=0\
$$\
\
$$\
N(JY,JZ)=-N(Y,Z)\
$$\
\
we deduce\
\
$$\
D\_{X}\\omega(Y,Z)=-2g(N(JY,JZ),JX)\
$$\
\
so that _8X; Y; Z 2_ Vect (M)\
\
$$\
\\forall X,Y,Z\\in\\mathrm{Vect}\\left(M\\right)\
$$\
\
(1.4.5)\
\
$$\
\\mathfrak{b}N(J X,J Y,J Z)=-\\frac{1}{2}(\\mathfrak{b}D\\omega)(X,Y,Z)=-\\frac{1}{2}d\\omega(X,Y,Z)=0\
$$\
\
where at the second step we have use the following identity (see Exercise\
1.4.4 for a more general situation)\
\
$$\
d\\eta(X,Y,Z)=\\mathfrak{b}(D\\eta)(X,Y,Z),\\quad\\forall\\eta\\in\\Omega^{2}(M),\\quad X,Y,Z\\in\\operatorname{Vect}{(M)}.\
$$\
\
Consider now an almost Hermitian manifold ( _M; g;_ J). A connection _r_ on\
_TX_ is said to be Hermitian if _rg_ = 0 and _rJ_ = 0.\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
\\nabla g=0\
$$\
\
$$\
\\nabla J=0\
$$\
\
If _r_ is such a connection then its _torsion_ is the _TM_-valued 2-form _T 2_\
›2(TM) deflned by\
\
$$\
\\Omega^{2}(TM)\
$$\
\
$$\
T\\in\
$$\
\
$$\
T(X,Y)=\\nabla\_{X}Y-\\nabla\_{Y}X-\[X,Y\],\\quad\\forall X,Y\\in\\operatorname{Vect}{(M)}.\
$$\
\
**Proposition 1.4.4.** _Suppose r is a Hermitian connection on an almost_\
_Hermitian manifold (M; g; J) and denote by T its torsion. Then 8X; Y 2_\
Vect (M)\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
\\forall X,Y\\in\
$$\
\
_(a)_\
\
$$\
4N(X,Y)=T(X,Y)+J T(J X,Y)+J T(X,J Y)-T(J X,J Y)\
$$\
\
(1.4.6)\
\
$$\
=N(X,Y)+J N(J X,Y)+J N(X,J Y)-N(J X,J Y).\
$$\
\
* * *\
\
_(b) If (M; g; J) is almost K˜ahler then there exists a_ unique Hermitian _connection r on TM such that_ _T_ = _N:_\
\
$$\
\\textit{If}\\left(M,g,J\\right)\
$$\
\
$$\
T\_{\\nabla}=N.\
$$\
\
**Proof** (a) We prove only the flrst equality in (1.4.6). It all begins with\
the identity\
\[ _X; Y\]=r Y ¡ r X¡T(X; Y):_\
\
$$\
\[X,Y\]=\\nabla\_{X}Y-\\nabla\_{Y}X-T(X,Y).\
$$\
\
Then\
\
$$\
\\begin{aligned}{}&{{}\[J X,J Y\]=\\nabla\_{J X}(J Y)-\\nabla\_{J Y}(J X)-T(J X,J Y)}\ {}&{{}\\quad=J(\\nabla\_{J X}Y-\\nabla\_{J Y}X)-T(J X,J Y).}\ \\end{aligned}\
$$\
\
$$\
\\begin{aligned}{J\[X,J Y\]}&{{}=J(\\nabla\_{X}(J Y)-\\nabla\_{J Y}X-T(X,J Y))}\ {}&{{}=-\\nabla\_{X}Y-J\\nabla\_{J Y}X-J T(X,J Y).}\ \\end{aligned}\
$$\
\
$$\
\\begin{aligned}{J\[J X,Y\]}&{{}=J\\big(\\nabla\_{J X}Y-\\nabla\_{Y}\\big(J X\\big)-T(J X,Y)\\big)}\ {}&{{}=J\\nabla\_{J X}Y+\\nabla\_{Y}X-J T(J X,Y).}\ \\end{aligned}\
$$\
\
We deduce\
\
$$\
4N(X,Y)=T(X,Y)+J T(J X,Y)+J T(X,J Y)-T(J X,J Y).\
$$\
\
(b) We flrst need to prove an auxiliary result.\
\
**Lemma 1.4.5.** _For any TM-valued 2-form T there exists a unique connection on TM compatible with the metric whose torsion is precisely T._\
\
**Proof of the lemma** Denote by _D_ the Levi-Civita connection on _M._\
Then any other metric connection has the form\
\
$$\
\\nabla=D+A,\\quad A\\in\\Omega^1(\\mathrm{End}\_-(TM))\
$$\
\
where End¡ _(TM)_ denotes the bundle of skew-symmetric endomorphisms of\
_TM._ Since _D_ has no torsion we deduce that the torsion of _r_ is\
\
$$\
TM\
$$\
\
$$\
T\_{\\nabla}(X,Y)=A\_{X}Y-A\_{Y}X,\\quad\\forall X,Y\\in\\operatorname{Vect}\\left(M\\right)\
$$\
\
where _AX_ denotes the contraction of _A_ _T ⁄M_-valued 2-form using the identiflcation\
\
with _X._ We can regard _A_ as a\
\
$$\
A\_{X}\
$$\
\
$$\
T^{\*}M\
$$\
\
$$\
\\langle A(X,Y),Z\\rangle:=g(A\_Z X,Y).\
$$\
\
Thus we deduce\
\
(1.4.7)\
\
$$\
\\langle T(X,Y),Z\\rangle=\\langle A(Y,Z),X\\rangle+\\langle A(Z,X),Y\\rangle.\
$$\
\
A cyclic summation leads to the identity\
\
$$\
\\mathfrak{b}T=2\\mathfrak{b}A.\
$$\
\
We can now rewrite (1.4.7) as follows:\
\
$$\
\\langle T(X,Y),Z\\rangle=(\\mathfrak{b}A)(X,Y,Z)-\\langle A(X,Y),Z\\rangle\
$$\
\
* * *\
\
$$\
=\\frac{1}{2}\\mathfrak{b}T(X,Y,Z)-\\langle A(X,Y),Z\\rangle.\
$$\
\
Hence\
\
$$\
A=-T+\\frac{1}{2}\\mathfrak{b}T.\
$$\
\
The lemma is proved. ¥\
\
According to Lemma 1.4.5 there exists a unique metric connection _r_ on\
_TM_ such that _T_ = _N._ It is explicitly deflned by\
\
$$\
T=N\
$$\
\
$$\
\\nabla=D-N+\\frac{1}{2}\\mathfrak{b}N.\
$$\
\
We have to show that when _(M; g; J)_ is almost K˜ahler this connection is\
also Hermitian, i.e.\
rJ = 0:\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
\\nabla J=0.\
$$\
\
Note flrst that in this case, according to (1.4.5), we have\
\
$$\
\\nabla=D-N,\
$$\
\
that is,\
\
$$\
g(\\nabla\_{X}Y,Z)=g(D\_{X}Y,Z)-g(N(Y,Z),X),\\quad\\forall X,Y,Z\\in\\operatorname{Vect}{(M)}.\
$$\
\
We have to show that\
\
$$\
g(D\_{X}J Y,Z)-g(N(J Y,Z),X)=-g(D\_{X}Y,J Z)+g(N(Y,J Z),X)\
$$\
\
or equivalently\
\
$$\
(1.4.8)\\quad g(D\_{X}J Y,Z)+g(D\_{X}Y,J Z)=g(N(J Y,Z),X)+g(N(Y,J Z),X).\
$$\
\
Note that\
\
$$\
N(JY,Z)=N(Y,JZ)=-JN(Y,Z)\
$$\
\
and\
\
$$\
g(D\_XY,Z)+g(D\_XY,JZ)=g((D\_XY)Y,Z)\
$$\
\
so that (1.4.8) is equivalent to\
\
$$\
g((D\_X J)Y,Z)=2g(N(Y,Z),JX)\
$$\
\
which is precisely (1.4.4). The proposition is proved. ¥\
\
**Remark 1.4.6.** (a) If _J_ is integrable (so that _M_ is K˜ahler) then _N_ =0\
so that the connection constructed in the above proposition is precisely the\
Levi-Civita connection.\
\
$$\
N=0\
$$\
\
(b) One can show (see \[64\]) that on any almost complex manifold there\
exist many connections compatible with the almost complex structure and\
torsion _N._ We refer to the survey **\[46\]** for additional facts on Hermitian\
connections.\
\
* * *\
\
**Deflnition 1.4.7.** The _Chern connection_ of an almost K˜ahler manifold\
_(M; g; J)_ is the unique Hermitian connection with torsion _N._\
\
$$\
\\left(M,g,J\\right)\
$$\
\
**Exercise 1.4.3.** Suppose that _(M; g; J)_ is an almost K˜ahler manifold and\
_D_ is the Levi-Civita connection of _g._ Show that the Chern connection _r_\
associated to the almost K˜ahler structure can be described as\
1\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
g.\
$$\
\
$$\
\\nabla\_{X}=D\_{X}-\\frac{1}{2}J(D\_{X}J),\\quad\\forall X\\in\\operatorname{Vect}{(M)}.\
$$\
\
**Exercise 1.4.4.** Suppose _(M; g)_ is a Riemannian manifold and _r_ is a\
connection on _TM_ compatible with the metric _g_ with torsion _T._ Deflne\
tr (T) 2 ›1(M) by\
X\
\
$$\
(M,g)\
$$\
\
$$\
(T)\\in\\Omega^1(M)\
$$\
\
$$\
\\mathrm{tr}\\left(T\\right)\\left(X\\right)=\\sum\_{i}g\\left(e\_{i},T\\left(e\_{i},X\\right)\\right),\\quad\\forall X\\in\\mathrm{Vect}\\left(X\\right)\
$$\
\
where ei denotes a local orthonormal frame on M. Show that for any · 2\
›p(M) we have\
\
$$\
e\_{i}\
$$\
\
$$\
\\eta\\in\
$$\
\
$$\
\\Omega^{p}(M)\
$$\
\
$$\
\\begin{aligned}{d\\eta}&{{}(X\_{0},\\cdots,X\_{p})=\\sum\_{j=0}^{p}(-1)^{j}(\\nabla\_{X\_{j}}\\eta)(X\_{0},\\cdots,\\hat{X} _{j},\\cdots,X_{p})}\ {}&{{}\\quad+\\sum\_{j<k}(-1)^{j+k}\\eta(T(X\_{j},X\_{k}),X\_{0},\\ldots,\\hat{X} _{j},\\ldots,\\hat{X}_{k},\\cdots,X\_{p}),}\ \\end{aligned}\
$$\
\
(1.4.9)\
\
$$\
\\begin{aligned}{d^{\*}\\eta(X\_{1},\\ldots,X\_{p-1})}&{{}=-\\sum\_{i=1}^{\\dim M}(\\nabla\_{e\_{i}}\\eta)(e\_{i},X\_{1},\\cdots,X\_{p-1})}\ {+}&{{}\\eta((\\operatorname{tr}T)^{\\flat},X\_{1},\\ldots,X\_{p-1})}\ \\end{aligned}\
$$\
\
(1.4.10)\
\
$$\
-\\sum\_{j=1}^{p-1}(-1)^{j}\\langle;g(X\_{j},T):,;\\eta(\\bullet,\\bullet,X\_{1},\\cdots,\\hat{X} _{j},\\cdots,X_{p-1});\\rangle.\
$$\
\
where (ei) is a local orthonormal frame, tr (T)\[denotes the vector fleld dual\
to tr (T), g(Xj;T) denotes the 2-form (X; Y) 7! g(Xj;T(X; Y) and the\
pairing _h†; †i_ refers to the inner product of two forms. (Observe that the\
above identities extend by complex linearity to complex valued forms and\
vectors.)\
\
$$\
(e\_{i})\
$$\
\
$$\
(T)^{\\flat}\
$$\
\
$$\
(T),g(X\_{j},T)\
$$\
\
$$\
(X,Y)\\mapsto g(X\_j,T(X,Y))\
$$\
\
$$\
\\langle\\bullet,\\bullet\\rangle\
$$\
\
**Exercise 1.4.5.** Suppose _(M; g; J)_ is an almost K˜ahler manifold and _r_ is\
the associated Chern connection.\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
\\nabla\
$$\
\
(a) Show that tr (N) = 0.\
\
$$\
(N)=0\
$$\
\
(b) Show that if X; Y 2 C1(T 0;1M) then N (X; Y) 2 C1(T 1;0M).\
\
$$\
X,Y\\in C^{\\infty}(T^{0,1}M)\
$$\
\
$$\
N(X,Y)\\in C^{\\infty}(T^{1,0}M)\
$$\
\
* * *\
\
(c) Denote by gc the extension of g by complex bilinearity to TM ›C. Show\
that for every X2C1(T 0;1M) the 2-form!X deflned by\
\
$$\
g\_{c}\
$$\
\
$$\
g\
$$\
\
$$\
TM\\otimes\\mathbb{C}\
$$\
\
$$\
X\\in C^{\\infty}(T^{0,1}M)\
$$\
\
$$\
\\omega\_{X}\
$$\
\
$$\
\\omega\_{X}(Y,Z)=g\_{c}(X,N(Y,Z))\
$$\
\
has type (0;2), i.e.\
\
$$\
\\omega\_{X}(J Y,Z)=\\omega\_{X}(Y,J Z)=-\\mathbf{i}\\omega\_{X}(Y,Z),\\quad\\forall Y,Z\\in\\operatorname{Vect}{(M)}.\
$$\
\
(d) Show that for any · 2 ›0;p(M) and any\
have the identities\
_p_\
X\
\
_Z0; ¢¢¢; Z_\
\
p 2 C1(T 0;1M) we\
\
$$\
\\eta\\in\\Omega^{0,p}(M)\
$$\
\
(1.4.11)\
\
$$\
Z\_{0},\\cdots,Z\_{p}\\in C^{\\infty}(T^{0,1}M)\
$$\
\
$$\
\\bar{\\partial}\\eta(Z\_{0},\\ldots,Z\_{p})=\\sum\_{j=1}^{p}(-1)^{j}(\\nabla\_{Z\_{j}}\\eta)(Z\_{0},\\cdots,\\hat{Z} _{j},\\cdots,Z_{p}),\
$$\
\
(1.4.12)\
\
$$\
\\bar{\\partial}^{\*}\\eta(Z\_{1},\\cdots,Z\_{p-1})=-\\sum\_{i=1}^{\\dim M}(\\nabla\_{e\_{i}}\\eta)(e\_{i},Z\_{1},\\cdots,Z\_{p-1}).\
$$\
\
where ei denotes a local, orthonormal frame of\
of these identities we refer to \[46\].)\
\
_TM._\
\
(For a generalization\
\
$$\
e\_{i}\
$$\
\
**Hint:** Use that fact that for any _Z0; ¢¢¢; Z_\
we have\
(@· „ )(Z0; ¢¢¢; Z)=d·\
\
p 2 C1(T\
(Z0; ¢¢¢; Z\
\
0;1M) and · 2 ›0;p(M)\
)\
\
$$\
Z\_{0},\\cdots,Z\_{p}\\in C^{\\infty}(T^{0,1}M)\
$$\
\
$$\
\\eta\\in\\Omega^{0,p}(M)\
$$\
\
$$\
(\\bar{\\partial}\\eta)(Z\_{0},\\cdots,Z\_{p})=d\\eta(Z\_{0},\\cdots,Z\_{p})\
$$\
\
and\
\
$$\
\\big(\\bar{\\partial}^{ _}\\eta\\big)\\big(Z\_{1},\\cdots,Z\_{p-1}\\big)=d^{_}\\eta\\big(Z\_{1},\\cdots,Z\_{p-1}\\big).\
$$\
\
In the remainder of this section we will assume _(M; g; J)_ is an almost\
K˜ahler manifold. Denote by! the associated symplectic form\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
\\omega(X,Y)=g(J X,Y),\\quad\\forall X,Y\\in\\operatorname{Vect}{(M)}.\
$$\
\
Set 2n = dimM. We orient M using the nowhere vanishing 2n-form!n.\
Note that\
1\
dv =!n:\
\
$$\
2n=\\dim M\
$$\
\
$$\
\\omega^{n}\
$$\
\
$$\
d v\_{g}=\\frac{1}{n!}\\omega^{n}.\
$$\
\
n!\
Using the metric _g_ and the above orientation we obtain a Hodge operator\
\
$$\
\*:\\Omega^{p}(M)\\rightarrow\\Omega^{2n-p}(M)\
$$\
\
which we extend by complex _anti-linearity_\
\
to an operator\
\
$$\
\*:\\Omega^{p}(M)\\otimes\\mathbb{C}\\rightarrow\\Omega^{2n-p}(M).\
$$\
\
$$\
\\varphi\\in\\Omega^{p,q}(M)\
$$\
\
Exercise 1.4.6. Let ’ 2 ›p;q(M). Prove that\
\
$$\
\*\\varphi\\in\\Omega^{n-p,n-q}(M)\
$$\
\
and\
\
$$\
\\varphi\\wedge\*\\varphi=\|\\varphi\|^{2}d v\_{g}\
$$\
\
where j†jdenotes the Hermitian metric induced by (\
\
⁄\
g; J) on⁄p;qT M.\
\
$$\
\\left\|\\bullet\\right\|\
$$\
\
$$\
\\Lambda^{p,q}T^{\*}M\
$$\
\
* * *\
\
Exterior multiplication by! deflnes a bundle morphism\
\
$$\
L:\\Omega^{p,q}(M)\\to\\Omega^{p+1,q+1}(M).\
$$\
\
⁄\
Its adjoint, L =⁄:›p+1;q+1(M)! ›p;q(M), is called the contraction by\
the symplectic form.\
\
$$\
L^{\*}=\\Lambda:\\Omega^{p+1,q+1}(M)\\to\\Omega^{p,q}(M)\
$$\
\
Exercise 1.4.7. Suppose (M; g; J) is an almost K˜ahler manifold and (ei; fi)\
is a local orthonormal frame such that fi = Jfi for all i. Its dual coframe\
will be denoted by (ei;fi) and, as usual, set\
\
$$\
\\left(M,g,J\\right)\
$$\
\
$$\
(e\_{i},f\_{i})\
$$\
\
$$\
f\_{i}=J f\_{i}\
$$\
\
$$\
(e^{i},f^{i})\
$$\
\
$$\
\\varepsilon\_{i}=2^{-1/2}(e\_{i}-\\mathbf{i}f\_{i}),\\quad\\bar{\\varepsilon} _{i}=2^{-1/2}(e_{i}+\\mathbf{i}f\_{i}),\
$$\
\
$$\
\\varepsilon^{i}=2^{-1/2}\\big(e^{i}+{\\bf i}f^{i}\\big),\\quad\\bar{\\varepsilon}^{i}=2^{-1/2}\\big(e^{i}-{\\bf i}f^{i}\\big).\
$$\
\
For _k_ = 1\
tions of ›\
\
; 2; ¢¢¢;nwe denote by {k and „\
⁄;⁄\
(M) uniquely determined by\
\
{k the (locally deflned) odd deriva-\
\
$$\
k=1,2,\\cdots,n\
$$\
\
$$\
\\imath\_{k}\
$$\
\
$$\
\\overline{\\imath}\_{k}\
$$\
\
$$\
\\Omega^{ _,_}(M)\
$$\
\
$$\
\\imath\_{k}\\varepsilon^{i}=\\delta\_{k}^{i}=\\bar{\\imath} _{k}\\bar{\\varepsilon}^{i},;\\imath_{k}\\bar{\\varepsilon}^{i}=\\bar{\\imath}\_{k}\\varepsilon^{i}=0\
$$\
\
where – denotes the Kronecker symbol. Show that locally\
X\
\
$$\
\\delta\
$$\
\
$$\
\\Lambda=-\\mathbf{i}\\sum\_{k}\\bar{\\imath} _{k}\\imath_{k}.\
$$\
\
Denote by ƒp;q the natural projection ›\
X\
\
⁄\
(M) › C! ›p;q(M) and set\
\
$$\
\\Pi^{p,q}\
$$\
\
$$\
\\Omega^{\*}(M)\\otimes\\mathbb{C}\\to\\Omega^{p,q}(M)\
$$\
\
$$\
\\Pi=\\sum\_{p,q}\\mathbf{i}^{p-q}\\Pi^{p,q}:\\Omega^{ _}(M)\\otimes\\mathbb{C}\\to\\Omega^{_}(M)\\otimes\\mathbb{C},\
$$\
\
$$\
H=\\sum\_{p,q}(n-p-q)\\Pi^{p,q}.\
$$\
\
⁄ ¡\
Observe that ƒ is bijective and ƒ =ƒ 1\
⁄ ¡ ⁄ ¡\
› (M) › C by dc =ƒ 1dƒ and dc =ƒ\
\
⁄ ⁄\
. Now deflne dc;dc:›(M) › C!\
_1dƒ._\
\
$$\
\\Pi^{\*}=\\Pi^{-1}\
$$\
\
$$\
d\_{c},d\_{c}^{ _}:\\Omega^{_}(M)\\otimes\\mathbb{C}\\to\
$$\
\
$$\
\\Omega^{\*}(M)\\otimes\\mathbb{C}\
$$\
\
$$\
d\_{c}=\\Pi^{-1}d\\Pi\
$$\
\
$$\
d \_ {c} ^ {\*} = \\Pi^ {- 1} d \\Pi\
$$\
\
**Example**\
\
z1; ¢¢¢;zn\
\
**1.4.8.** Consider the\
) equipped with the canonical K˜\
X\
\
space Cn (with coordinates\
ahler structure\
\
$$\
\\mathbb{C}^n\
$$\
\
$$\
z ^ {1}, \\dots , z ^ {n})\
$$\
\
$$\
\\omega\_ {0} = \\frac {\\mathbf {i}}{2} \\sum\_ {i} d z ^ {i} \\wedge d \\bar {z} ^ {i}.\
$$\
\
Set "i =\
\
~~p1~~ p1\
dzi and "„i = dz„i. For every pair of ordered multi-indices\
2 2\
\
$$\
\\bar {\\varepsilon} ^ {i} = \\frac {1}{\\sqrt {2}} d \\bar {z} ^ {i}\
$$\
\
$$\
\\varepsilon^ {i} = \\frac {1}{\\sqrt {2}} d z ^ {i}\
$$\
\
$$\
I = \\left(i \_ {1} < \\dots < i \_ {k}\\right), J = \\left(j \_ {1} < \\dots < j \_ {m}\\right)\
$$\
\
$$\
\\varepsilon^ {I} = \\varepsilon^ {i \_ {1}} \\wedge \\dots \\wedge \\varepsilon^ {i \_ {k}}, \\bar {\\varepsilon} ^ {J} = \\varepsilon^ {j \_ {1}} \\wedge \\dots \\wedge \\varepsilon^ {j \_ {m}}.\
$$\
\
we set\
\
Denote by Ic the ordered multi-index complementary to I, i.e. as unordered\
sets, we have the equality Ic = f1; ¢¢¢; ngnI. Also denote byIthe signature\
of the permutation obtained by writing the multi-indices I and Ic one after\
the other.\
\
$$\
I ^ {c} = {1, \\dots , n } \\backslash I\
$$\
\
$$\
\\sigma\_ {I}\
$$\
\
$$\
I ^ {c}\
$$\
\
* * *\
\
We can rewrite\
\
$$\
\\omega\_ {0} = \\mathbf {i} \\sum\_ {i} \\varepsilon^ {i} \\wedge \\bar {\\varepsilon} ^ {i}\
$$\
\
so that\
\
$$\
\\frac {1}{n !} \\omega\_ {0} ^ {n} = \\mathbf {i} ^ {n ^ {2}} \\varepsilon^ {1} \\wedge \\dots \\wedge \\varepsilon^ {n} \\wedge \\bar {\\varepsilon} ^ {1} \\wedge \\dots \\wedge \\bar {\\varepsilon} ^ {n}.\
$$\
\
Observe that\
\
$$\
\\begin{array}{l} \* \\varepsilon^ {i} = \\frac {1}{\\sqrt {2}} \\left(\* d x ^ {i} - \\mathbf {i} \* d y ^ {i}\\right) \ = \\frac {1}{\\sqrt {2}} \\left(d x ^ {1} \\wedge d y ^ {1}\\right) \\wedge \\dots \\wedge \\left(\\widehat {d x ^ {i} \\wedge d y ^ {i}}\\right) \\wedge \\dots \\wedge \\left(d x ^ {n} \\wedge d y ^ {n}\\right) \\wedge \\left(d y ^ {i} + \\mathbf {i} d x ^ {i}\\right) \ (\\mathrm {h a t} \\longleftrightarrow \\mathrm {m i s s i n g t e r m}) \ = \\mathbf {i} ^ {(n - 1) ^ {2} + 1} (- 1) ^ {n - i} \\varepsilon^ {1} \\wedge \\dots \\wedge \\widehat {\\varepsilon^ {i}} \\wedge \\dots \\wedge \\varepsilon^ {n} \\wedge \\bar {\\varepsilon} ^ {1} \\wedge \\dots \\wedge \\bar {\\varepsilon} ^ {n} \ \\end{array}\
$$\
\
Using the above exercise we deduce\
\
$$\
\
- \\omega\_ {0} = \\frac {1}{(n - 1) !} \\omega\_ {0} ^ {n - 1}\
  $$\
\
and, more generally,\
\
$$\
\
- \\left(\\varepsilon^ {I} \\wedge \\bar {\\varepsilon} ^ {J}\\right) = (- 1) ^ {\| J \| (n - \| I \|)} \\mathbf {i} ^ {n ^ {2}} \\sigma\_ {I} \\sigma\_ {J} \\varepsilon^ {I ^ {c}} \\wedge \\bar {\\varepsilon} ^ {J ^ {c}}.\
  $$\
\
The operators we have introduced above satisfy a series of important\
identities. For a proof of the following proposition we refer to \[ **146\].**\
\
**Proposition 1.4.9.** _Suppose (M; g; J) is an almost K˜ahler manifold. Then_\
X\
\
$$\
(M, g, J)\
$$\
\
$$\
\\Pi^ {2} = \* ^ {2} = \\sum\_ {p, q} (- 1) ^ {p + q} \\Pi^ {p, q},\
$$\
\
$$\
\\Lambda = \* ^ {- 1} L _, d ^ {_} = \- \\* d \*,\
$$\
\
$$\
\[ L, \\Lambda \] = H,\
$$\
\
$$\
\[ L, d \] = \[ \\Lambda , d ^ { _} \] = \[ L, d \_ {c} \] = \[ \\Lambda , d \_ {c} ^ {_} \] = 0,\
$$\
\
$$\
\[ L, d ^ { _} \] = d \_ {c}, \[ \\Lambda , d \] = - d \_ {c} ^ {_}, \[ L, d \_ {c} ^ { _} \] = \- d, \[ \\Lambda , d \_ {c} \] = d ^ {_}.\
$$\
\
When _M_ is K˜ahler the above list of identities can be considerably enriched. For a proof of the following important identities we refer to \[49\].\
\
**Proposition 1.4.10.** _Suppose_ ( _M; g; J_\
„\
\
) _is a_ K˜ahler\
„\
\
_manifold. Then_\
„\
\
$$\
(M, g, J)\
$$\
\
$$\
\\partial^ { _} = \- \\* \\partial , \\bar {\\partial} ^ {} = \- \\* \\bar {\\partial} , d ^ {} = \\partial^ {_} \+ \\bar {\\partial} ^ {\*},\
$$\
\
$$\
\\begin{array}{l} \[ L, \\partial \] = \[ L, \\bar {\\partial} \] = \[ \\Lambda , \\partial^ { _} \] = \[ \\Lambda , \\bar {\\partial} ^ {_} \] = 0, \ \[ L, \\partial^ { _} \] = \\mathbf {i} \\bar {\\partial}, \[ L, \\bar {\\partial} ^ {_} \] = \- \\mathbf {i} \\partial , \ \[ \\Lambda , \\partial \] = \\mathbf {i} \\bar {\\partial} ^ { _}, \[ \\Lambda , \\bar {\\partial} \] = - \\mathbf {i} \\partial^ {_}, \ \\partial \\bar {\\partial} ^ { _} = \- \\bar {\\partial} ^ {_} \\partial = - \\mathbf {i} \\bar {\\partial} ^ { _} L \\bar {\\partial} ^ {_} = \- \\mathbf {i} \\partial \\Lambda \\bar {\\partial} \ \\end{array}\
$$\
\
* * *\
\
$$\
\\bar {\\partial} \\partial^ { _} = \- \\partial^ {_} \\bar {\\partial} = - \\mathbf {i} \\partial^ { _} L \\partial^ {_} = \\mathbf {i} \\bar {\\partial} \\Lambda \\partial .\
$$\
\
⁄ ⁄ ⁄ ⁄\
If we set ¢d = dd + d d, ¢@= @@ + @ @ and\
\
„⁄„ \+ „„⁄\
¢@„ = _@ @ @@ then_\
\
$$\
\\Delta\_ {d} = d d ^ { _} \+ d ^ {_} d, \\Delta\_ {\\partial} = \\partial \\partial^ { _} \+ \\partial^ {_} \\partial\
$$\
\
$$\
\\Delta\_ {\\bar {\\partial}} = \\bar {\\partial} ^ { _} \\bar {\\partial} + \\bar {\\partial} \\bar {\\partial} ^ {_}\
$$\
\
$$\
\\Delta\_ {\\partial} = \\Delta\_ {\\bar {\\partial}} = \\frac {1}{2} \\Delta\_ {d}.\
$$\
\
We include here for later use some simple consequences of these identities.\
\
**Corollary 1.4.11.** _Suppose (M; g; J) is a K˜_\
_the following identities._\
\
_ahler manifold. Then we have_\
\
$$\
(M, g, J)\
$$\
\
(1.4.13)\
\
$$\
\\mathbf {i} \\Lambda (\\partial \\alpha) = - \\bar {\\partial} ^ {\*} \\alpha , \\forall \\alpha \\in \\Omega^ {0, 1} (M),\
$$\
\
(1.4.14)\
\
$$\
\\mathbf {i} \\Lambda \\bar {\\partial} \\beta = \\partial^ {\*} \\beta , \\forall \\beta \\in \\Omega^ {1, 0} (M),\
$$\
\
(1.4.15)\
\
$$\
\\mathbf {i} \\Lambda (\\partial \\bar {\\partial} f) = - \\frac {1}{2} d ^ {\*} d f \\quad \\forall f \\in \\Omega^ {0, 0} (M).\
$$\
\
**Proof** To prove (1.4.13) we use the commutator identity\
\
$$\
\\left\[\\Lambda,\\partial\\right\]=\\mathbf{i}\\bar{\\partial}^\*.\
$$\
\
We deduce\
\
$$\
\\Lambda\\partial\\alpha=\\partial\\Lambda\\alpha+\\mathrm{i}\\bar{\\partial}^ _\\alpha=\\mathrm{i}\\bar{\\partial}^_\\alpha\
$$\
\
since ⁄fi = 0 because fi 2 ›0;1(M). The flrst identity is proved. The same\
method proves the second identity as well. The third identity follows from\
the flrst and the equality ¢@„ = 1/2¢d. ¥\
\
$$\
\\Lambda\\alpha=0\
$$\
\
$$\
\\alpha\\in\\Omega^{0,1}(M)\
$$\
\
$$\
\\Delta\_{\\bar{\\partial}}=\\frac{1}{2}\\Delta\_{d}.\
$$\
\
The identities in Proposition 1.4.10 do not hold for almost K˜ahler manifolds but surprisingly the identities in Corollary 1.4.11 continue to hold on\
an arbitrary almost K˜ahler manifold. We will spend the remainder of this\
subsection proving this fact.\
\
**Proposition 1.4.12.** _The identities (1.4.13) { (1.4.15) continue to hold for_\
_arbitrary almost K˜ahler manifolds._\
\
$$\
(1.4.13)-(1.4.15)\
$$\
\
**Proof** We prove only (1.4.13) and\
\
(1.4.16)\
\
$$\
\\frac{1}{2}d^{ _}d f=\\bar{\\partial}^{_}\\bar{\\partial}f,\\quad\\forall f\\in\\Omega^{0,0}(M).\
$$\
\
The identity (1.4.14) follows from (1.4.13) by complex conjugation while\
(1.4.15) follows from (1.4.13) and (1.4.16).\
\
* * *\
\
Denote by _r_ the Chern connection of the almost K˜ahler structure and\
choose a local orthonormal frame (ei; fi) as in Exercise 1.4.7. To prove\
(1.4.13) we use the identity @fi = (dfi)1;1, that is,\
\
$$\
\\left(e\_{i},f\_{i}\\right)\
$$\
\
$$\
\\partial\\alpha=(d\\alpha)^{1,1}\
$$\
\
$$\
\\partial\\alpha(\\varepsilon\_{i},\\bar{\\varepsilon} _{j})=(d\\alpha)(\\varepsilon_{i},\\bar{\\varepsilon}\_{j}),\\forall i,j.\
$$\
\
At this point we want to use the fact that the torsion of the Chern connection\
is _N_ and the identity (1.4.9)\
\
$$\
\\begin{align\*}\\big(d\\alpha\\big)\\big(\\varepsilon\_{i},\\bar{\\varepsilon} _{j}\\big)&=\\big(\\nabla_{\\varepsilon\_{i}}\\alpha\\big)\\big(\\bar{\\varepsilon} _{j}\\big)-\\big(\\nabla_{\\bar{\\varepsilon} _{j}}\\alpha\\big)\\big(\\varepsilon_{i}\\big)+\\alpha\\big(N\\big(\\varepsilon\_{i},\\bar{\\varepsilon} _{j}\\big)\\big).\\&=\\big(\\nabla_{\\varepsilon\_{i}}\\alpha\\big)\\big(\\bar{\\varepsilon} _{j}\\big)+\\alpha\\big(N\\big(\\varepsilon_{i},\\bar{\\varepsilon}\_{j}\\big)\\big)\\end{align\*}\
$$\
\
because r"„j fi 2 ›0;1(M).\
\
$$\
\\nabla\_{\\bar{\\varepsilon}\_{j}}\\alpha\\in\\Omega^{0,\\bar{1}}(M)\
$$\
\
To compute _⁄@fi_ we use the local description of ⁄ in Exercise 1.4.7. We\
deduce\
X X‡ ¡ ¢ ·\
\
$$\
\\mathbf{i}\\Lambda\\partial\\alpha=\\sum\_{k}(\\partial\\alpha)(\\varepsilon\_{k},\\bar{\\varepsilon} _{k})=\\sum_{k}\\Big((\\nabla\_{\\varepsilon\_{k}}\\alpha)(\\bar{\\varepsilon} _{k})+\\alpha\\big(N(\\varepsilon_{k},\\bar{\\varepsilon}\_{k})\\big)\\Big).\
$$\
\
We need to analyze in greater detail the terms in the above sums. We will\
use the fact that for any fl 2 ›0;1(M) we have\
\
$$\
\\beta\\in\\Omega^{0,1}(M)\
$$\
\
$$\
\\beta(J X)=-\\mathbf{i}\\beta(X),\\quad\\forall X\\in\\operatorname{Vect}(M)\\otimes\\mathbb{C}.\
$$\
\
This implies that\
\
(1.4.17)\
\
$$\
\\beta(e\_{k})=\\mathbf{i}\\bar{\\beta}(f\_{k}),\\quad\\forall k.\
$$\
\
Then\
\
$$\
\\begin{align\*}(\\nabla\_{\\varepsilon\_k}\\alpha)(\\bar{\\varepsilon} _k)&=\\frac{1}{2}(\\nabla_{e\_k}-\\mathbf{i}\\nabla\_{f\_k})\\alpha(e\_k+\\mathbf{i}f\_k)\\&=\\frac{1}{2}\\Big(\\nabla\_{e\_k}\\alpha(e\_k)+\\nabla\_{f\_k}\\alpha(f\_k)\\Big)+\\frac{1}{2}\\Big(-\\mathbf{i}(\\nabla\_{f\_k}\\alpha)(e\_k)+\\mathbf{i}(\\nabla\_{e\_k}\\alpha)(f\_k)\\Big)\\end{align\*}\
$$\
\
(use the fact that rekfi; rfkfi 2 ›\
\
0;1(M) and (1.4.17))\
\
$$\
\\nabla\_{e\_{k}}\\alpha,\\nabla\_{f\_{k}}\\alpha\\in\\Omega^{0,1}(M)\
$$\
\
$$\
\\left(\\nabla\_{e\_{k}}\\alpha\\right)\\left(e\_{k}\\right)+\\left(\\nabla\_{f\_{k}}\\alpha\\right)\\left(f\_{k}\\right).\
$$\
\
Using the identity (1.4.12) we deduce\
X\
\
$$\
\\sum\_{k}(\\nabla\_{\\varepsilon\_{k}}\\alpha)(\\bar{\\varepsilon}\_{k})=-\\bar{\\partial}^{\*}\\alpha.\
$$\
\
To conclude the proof of (1.4.13) it su–ces to show that\
\
$$\
N\\left(\\varepsilon\_{k},\\bar{\\varepsilon}\_{k}\\right)=0,\\quad\\forall k.\
$$\
\
(1.4.18)\
\
We have\
\
$$\
\\begin{aligned}{N(\\varepsilon\_{k},\\bar{\\varepsilon} _{k})=\\frac{1}{2}N(e_{k}-\\mathbf{i}f\_{k},e\_{k}+\\mathbf{i}f\_{k})}&{{}=\\mathbf{i}N(e\_{k},f\_{k})=\\mathbf{i}N(e\_{k},J e\_{k})}\ {}&{{}=-\\mathbf{i}J N(e\_{k},e\_{k})=0.}\ \\end{aligned}\
$$\
\
The identity (1.4.13) is proved. Combining the above arguments with\
(1.4.11) one can easily obtain (1.4.17). The details are left to the reader. ¥\
\
* * *\
\
**1.4.2. Cauchy-Riemann operators.** Suppose _(M; J)_ is an almost complex manifold and _E!M_ is a complex Hermitian vector bundle over _M._\
We denote by ›p;q(E) the space of smooth sections of the complex bundle\
⁄\
⁄p;qT M › E so that we have a decomposition\
M\
\
$$\
(M,J)\
$$\
\
$$\
E\\rightarrow M\
$$\
\
$$\
\\Omega^{p,q}(E)\
$$\
\
$$\
\\Lambda^{p,q}T^{\*}M\\otimes E\
$$\
\
$$\
\\Omega^{k}(E)=\\bigoplus\_{p+q=k}\\Omega^{p,q}(E).\
$$\
\
A _Cauchy-Riemann operator_ (CR-operator for brevity) on _E_ is a flrst order\
p.d.o.\
L :›0;0(E)! ›0;1(E)\
\
$$\
L:\\Omega^{0,0}(E)\\to\\Omega^{0,1}(E)\
$$\
\
such that\
\
$$\
L(f u)=(\\bar{\\partial}f)\\otimes u+f L u,\\quad\\forall f\\in C^{\\infty}(M),\\quad u\\in\\Omega^{0,0}(E).\
$$\
\
Let us remark that the above condition is simply a statement about the\
symbol of _L._ We denote by CR(E) the space of CR-operators on _E_ and by\
Ah(E) the a–ne space of Hermitian connections on E. Denote by P 1;0 and\
P 0;1 the projectors associated to the decomposition\
\
$$\
\\mathcal{A}\_{h}(E)\
$$\
\
$$\
P^{1,0}\
$$\
\
$$\
P^{0,1}\
$$\
\
$$\
\\Omega^{1}(E)=\\Omega^{1,0}(E)\\oplus\\Omega^{0,1}(E).\
$$\
\
Given a connection A 2 Ah(E\
\
) with covariant derivative\
\
$$\
A\\in\\mathcal{A}\_{h}(E)\
$$\
\
$$\
\\nabla^{A}:\\Omega^{0}(E)\\rightarrow\\Omega^{1}(E)\
$$\
\
we obtain an operator\
\
$$\
\\bar{\\partial}\_{A}=P^{0,1}\\circ\\nabla^{A}:\\Omega^{0,0}(E)\\to\\Omega^{0,1}(E).\
$$\
\
We let the reader check that _@„_\
\
A is a CR-operator. We thus obtain a map\
\
$$\
\\bar{\\partial}\_{A}\
$$\
\
$$\
\\bar{\\partial} _{\\bullet}:\\mathcal{A}_{h}\\rightarrow\\mathrm{CR}(E),\\quad A\\mapsto\\bar{\\partial}\_{A}.\
$$\
\
**Proposition 1.4.13.** _The map @_\
\
„† is a bijection.\
\
$$\
\\bar{\\partial}\_{\\bullet}\
$$\
\
Proof We flrst show that @„†\
connections such that @„A = @„B\
\
is injective. Suppose _A; B_ are two Hermitian\
. Then\
\
$$\
\\bar{\\partial}\_{\\bullet}\
$$\
\
$$\
\\bar{\\partial} _{A}=\\bar{\\partial}_{B}\
$$\
\
$$\
\\delta=B-A\
$$\
\
is a 1-form valued in the bundle of skew-Hermitian endomorphisms of _E_\
such that\
–0;1 = 0:\
\
$$\
\\delta^{0,1}=0.\
$$\
\
Note that\
\
$$\
\\delta^{0,1}(X)=\\frac{1}{2}(\\delta(X)+\\mathbf{i}\\delta(J X)),\\quad\\forall X\\in\\operatorname{Vect}\\left(M\\right)\
$$\
\
where –(X) is a skew-Hermitian endomorphism and **i**– _(JX)_ is Hermitian.\
This implies –(X)=– _(JX)_ = 0 since any complex endomorphism decomposes uniquely as a sum of a skew-Hermitian and a Hermitian operator.\
\
$$\
\\delta(X)=\\delta(J X)=0\
$$\
\
* * *\
\
To prove the surjectivity we will construct a right inverse\
\
$$\
\\nabla^{\\bullet}:\\mathbf{CR}(E)\\rightarrow\\mathcal{A}\_{h}(E).\
$$\
\
Fix a Hermitian connection _A0_ on _E_\
operator @„A0. IfL 2 CR(E) then\
\
and denote by _L0_ the associated CR-\
\
$$\
A\_{0}\
$$\
\
$$\
L\_{0}\
$$\
\
$$\
\\bar{\\partial} _{A_{0}}\
$$\
\
$$\
L\\in\\mathbf{C}\\mathbf{R}(E)\
$$\
\
$$\
\\beta=L-L\_{0}\\in\\Omega^{0,1}\\left(\\operatorname{End}\\left(E\\right)\\right).\
$$\
\
We have to construct a 1-form – valued in the bundle of skew-Hermitian\
endomorphisms of _E_ such that\
\
$$\
\\delta\
$$\
\
$$\
\\delta^{0,1}=\\beta.\
$$\
\
In other words, – satisfles the functional equation\
\
$$\
\\delta\
$$\
\
$$\
\\delta(X)+\\mathbf{i}\\delta(J X)=2\\beta(X),\\quad\\forall X\\in\\operatorname{Vect}{(M)}.\
$$\
\
We deduce from the above equality that –(X) is the skew-Hermitian part of\
the endomorphism _2fl(X_) so that\
\
$$\
\\delta(X)\
$$\
\
$$\
\\delta(X)=\\beta(X)-\\beta(X)^\*.\
$$\
\
Now set\
\
$$\
\\nabla\_{\\cdot}^{L\_{0}+\\beta}=\\nabla\_{\\cdot}^{A\_{0}}+\\beta(\\cdot)-\\beta(\\cdot)^{\*}.\
$$\
\
The map\
\
$$\
L\_{0}+\\beta\\mapsto\\nabla^{L\_{0}+\\beta}\
$$\
\
is a right inverse for @„†. ¥\
\
$$\
\\bar{\\partial}\_{\\bullet}.\ \\blacksquare\
$$\
\
Suppose _L 2_ **CR** (E). Then _L_ induces flrst order p.d.o.’s\
\
$$\
L\\in\\mathbf{CR}\\left(E\\right)\
$$\
\
$$\
L:\\Omega^{p,q}(E)\\rightarrow\\Omega^{p,q+1}(E)\
$$\
\
uniquely determined by\
\
$$\
L(\\alpha\\otimes u)=\\bar{\\partial}\\alpha\\otimes u+(-1)^{p+q}\\alpha\\wedge L u,\\quad\\forall\\alpha\\in\\Omega^{p,q}(M),;u\\in C^{\\infty}(E).\
$$\
\
If _A_\
CR-operators\
\
is Hermitian connection on _E_\
@„ :›p;q(E\
\
we denote by the same symbol all the\
)! ›p;q+1(E):\
\
$$\
\\bar{\\partial}\_{A}:\\Omega^{p,q}(E)\\to\\Omega^{p,q+1}(E).\
$$\
\
Then for every\
\
(1.4.19)\
\
$$\
u\\in C^{\\infty}(E)\
$$\
\
u 2 C1(E) we have\
\
$$\
\\bar{\\partial} _{A}^{2}u=F_{A}^{0,2}u-\\left(\\partial\_{A}u\\right)\\circ N\
$$\
\
where _N_ denotes the Nijenhuis tensor of the almost complex structure on\
_N._\
\
**Exercise 1.4.8.** Use the arguments in the proof of Proposition 1.4.2 to\
prove the identity (1.4.19).\
\
* * *\
\
In the remaining part of this subsection we will assume the almost complex structure on _M_ is integrable. This means the manifold _M_ can be\
covered by (contractible) coordinate charts Ufi! Cn such that the transition maps are holomorphic. A _holomorphic structure_ on the rank- _r_ complex\
vector bundle _E_ is a collection of _holomorphic local trivializations,_ i.e. a\
collection of local trivializations\
\
$$\
U\_{\\alpha}\\rightarrow\\mathbb{C}^{n}\
$$\
\
$$\
\\Psi\_{\\alpha}:E\\left\| _{U_{\\alpha}}\\rightarrow\\underline{{\\mathbb{C}}} _{U_{\\alpha}}^{r}\\right.\
$$\
\
such that the transition maps\
\
$$\
g\_{\\beta\\alpha}:=\\Psi\_{\\beta}(p)\\circ\\Psi\_{\\alpha}^{-1}(p):U\_{\\alpha\\beta}\\to G L(r,\\mathbb{C})\\subset\\mathbb{C}^{r^{2}}\
$$\
\
are _holomorphic._ A holomorphic vector bundle is a pair\
\
(vector bundle, holomorphic structure).\
\
¡\
Two holomorphic structures “ = (“fi; gflfi = “fl– “fi1) and' =\
¡\
('fi; hflfi = 'fl –'fi1) are isomorphic if there exist holomorphic maps\
\
$$\
\\Psi=\\left(\\Psi\_{\\alpha},g\_{\\beta\\alpha}=\\Psi\_{\\beta}\\circ\\Psi\_{\\alpha}^{-1}\\right)\
$$\
\
$$\
\\Phi\_{ 尨 }=\
\\left(\\Phi\_{\\alpha},h\_{\\beta\\alpha}=\\Phi\_{\\beta}\\circ\\Phi\_{\\alpha}^{-1}\\right)\
$$\
\
$$\
T\_{\\alpha}:U\_{\\alpha}\\to G L(r,\\mathbb{C})\
$$\
\
such that\
\
$$\
h\_{\\beta\\alpha}=T\_{\\beta}g\_{\\beta\\alpha}T\_{\\alpha}^{-1}.\
$$\
\
We denote by **Hol** (E) the set of isomorphism classes of holomorphic structures on _E._ (To be completely rigorous, one has to include in the deflnition\
of equivalence the gluing cocycles subordinated to difierent covers.)\
\
**Exercise 1.4.9.** Prove that any holomorphic structure on _E_ induces an\
integrable complex structure on the total space of the bundle such that\
the canonical projection _E! M_ is a holomorphic map. Moreover, two\
equivalent isomorphic holomorphic structures induce biholomorphic complex\
structures on the total space.\
\
$$\
E\\rightarrow M\
$$\
\
Fix a holomorphic structure on _E_ given by the local holomorphic trivialization “fi. There is a canonically associated sheaf of holomorphic sections.\
If V is an open subset of M and Vfi = V \ Ufi then a section ˆ of E over V\
is called holomorphic if the functions\
\
$$\
\\Psi\_{\\alpha}\
$$\
\
$$\
V\_{\\alpha}=V\\cap U\_{\\alpha}\
$$\
\
$$\
\\psi\
$$\
\
$$\
\\psi\_{\\alpha}:=\\Psi\_{\\alpha}\\circ\\psi\\mid\_{V\_{\\alpha}}:V\_{\\alpha}\\to\\mathbb{C}^{r}\
$$\
\
are holomorphic. We denote by _OM(E_) the sheaf of holomorphic local sections of _E._ The manifold _M_ is equipped with a fundamental sheaf _OM,_\
the sheaf of local holomorphic functions on _M._ Then _OM(E_) is a sheaf of\
_OM_-modules. It is a locally free sheaf, i.e. it is locally isomorphic to the\
r\
sheaf _OM._\
\
$$\
\\mathcal{O}\_{M}(E)\
$$\
\
$$\
\\mathcal{O}\_{M}\
$$\
\
$$\
\\mathcal{O}\_{M}(E)\
$$\
\
$$\
\\mathcal{O}\_{M^{\\cdot}}\
$$\
\
$$\
\\mathcal{O}\_{M}^{r}\
$$\
\
**Exercise 1.4.10.** Prove that two holomorphic structures on _E_ are isomorphic ifi the associated sheaves of holomorphic sections are isomorphic as\
sheaves of _OM_-modules.\
\
$$\
\\mathcal{O}\_{M}\
$$\
\
* * *\
\
Denote by ei the canonical spanning sections of the trivial vector bundle\
CrU and deflne\
_fi_\
\
$$\
e\_{i}\
$$\
\
$$\
\\underline{{\\mathbb{C}}} _{U_{\\alpha}}^{r}\
$$\
\
$$\
\\Psi\_{\\alpha}^{-1}(e\_{1})=u\_{1}^{\\alpha},\\cdots,\\Psi\_{\\alpha}^{-1}(e\_{r})=u\_{r}^{\\alpha}\\in\\mathcal{O} _{M}(E,U_{\\alpha}).\
$$\
\
These sections span the flbers of Efi.\
uniquely written as\
X\
\
Any section u 2 C1(Efi) can be\
\
$$\
E\_{\\alpha}\
$$\
\
$$\
u\\in C^{\\infty}(E\_{\\alpha})\
$$\
\
$$\
u=\\sum\_{i}f\_{i}u\_{i}^{\\alpha},\\quad f\_{i}\\in C^{\\infty}(U\_{\\alpha})\\otimes\\mathbb{C}.\
$$\
\
Deflne @„fi 2 CR(Efi) by\
\
$$\
\\bar{\\partial} _{\\alpha}\\in\\mathbf{CR}(E_{\\alpha})\
$$\
\
$$\
\\bar{\\partial} _{\\alpha}u=\\sum(\\bar{\\partial}f_{i})\\otimes u\_{i}^{\\alpha}.\
$$\
\
»\
Since the identiflcations Efi = Efl over U\
we deduce\
@„ = @„ over\
\
fifl are given by holomorphic maps\
U :\
\
$$\
E\_{\\alpha}\\cong E\_{\\beta}\
$$\
\
$$\
U\_{\\alpha\\beta}\
$$\
\
$$\
\\bar{\\partial} _{\\alpha}=\\bar{\\partial}_{\\beta}\\quad\\mathrm{over}\\quad U\_{\\alpha\\beta}.\
$$\
\
Thus the operators @„fi glue together to form a CR-operator on E. It depends\
on the choice of the trivializations “fi. We will denote it by @„.\
“\
\
$$\
\\bar{\\partial}\_{\\alpha}\
$$\
\
$$\
\\Psi\_{\\alpha}\
$$\
\
$$\
\\bar{\\partial}\_{\\Psi}\
$$\
\
**Exercise 1.4.11.** Show that\
\
$$\
\\bar{\\partial} _{\\Psi}\\circ\\bar{\\partial}_{\\Psi}=0.\
$$\
\
**Deflnition 1.4.14.** A CR-operator _L_ on a complex vector bundle _E_ over\
a _complex_ manifold _M_ is called _integrable_ if _L2_ = 0\. We will denote by\
CRi(E) the space of complex integrable CR-operators.\
‡ · ‡ ·\
\
$$\
L^{2}=0\
$$\
\
$$\
\\mathbf{C}\\mathbf{R}\_{i}(E)\
$$\
\
Suppose “ = (“fi) and “=( ^ “^ fi) deflne two isomorphic holomorphic structures on _E._ Thus, there exist holomorphic maps\
\
$$\
\\left(\\Psi=\\left(\\Psi\_{\\alpha}\\right)\\right)\
$$\
\
$$\
\\left(\\hat{\\Psi}=\\left(\\hat{\\Psi}\_{\\alpha}\\right)\\right)\
$$\
\
$$\
\\gamma\_{\\alpha}:U\_{\\alpha}\\to G L(r,\\mathbb{C})\
$$\
\
such that\
\
$$\
\\hat{\\Psi} _{\\beta}\\circ\\hat{\\Psi}_{\\alpha}^{-1}\\gamma\_{\\alpha}=\\gamma\_{\\beta}\\Psi\_{\\beta}\\circ\\Psi\_{\\alpha}^{-1}.\
$$\
\
Deflne\
\
$$\
\\Phi\_{\\alpha}:=\\gamma\_{\\alpha}^{-1}\\hat{\\Psi}\_{\\alpha}.\
$$\
\
Observe that\
\
$$\
\\Phi\_{\\beta}\\circ\\Phi\_{\\alpha}^{-1}=\\Psi\_{\\beta}\\circ\\Psi\_{\\alpha}^{-1}.\
$$\
\
$$\
\\left(\\Psi=\\left(\\Psi\_{\\alpha}\\right)\\right)\
$$\
\
‡ · ‡\
Thus, the collections “ = (“fi) and\
morphic gluing cocycle. Moreover, since the maps\
have\
_@„_ = _@„_\
\
·\
' = ('fi) lead to the same holofiare holomorphic we\
_:_\
\
$$\
\\left(\\Phi=\\left(\\Phi\_{\\alpha}\\right)\\right)\
$$\
\
$$\
\\gamma\_{\\alpha}\
$$\
\
$$\
\\bar{\\partial} _{\\hat{\\Psi}}=\\bar{\\partial}_{\\Phi}.\
$$\
\
The collections “ and ' are cohomologous, i.e. there exist smooth maps\
\
$$\
\\Psi\
$$\
\
$$\
\\Phi\
$$\
\
$$\
T\_{\\alpha}:U\_{\\alpha}\\to G L(r,\\mathbb{C})\
$$\
\
* * *\
\
$$\
\\Psi\_{\\alpha}=T\_{\\alpha}\\circ\\Phi\_{\\alpha}.\
$$\
\
such that\
\
Clearly\
\
$$\
T\_{\\beta}=g\_{\\beta\\alpha}T\_{\\alpha}g\_{\\alpha\\beta}\
$$\
\
so that _T_ deflnes a complex automorphism of the bundle _E._ Thus, two collections of local trivializations which lead to the same (holomorphic) gluing\
cocycle difier by an automorphism of _E._\
\
$$\
T\
$$\
\
Suppose now that _T 2_ G(E) is a complex (not necessarily holomorphic)\
automorphism of E. Using the trivializations “fi it can be described as a\
collection of smooth maps Tfi: Ufi! GL(r; C) satisfying the gluing rules\
\
$$\
T\\in\\mathcal{G}(E)\
$$\
\
$$\
\\Psi\_{\\alpha}\
$$\
\
$$\
T\_{\\alpha}:U\_{\\alpha}\\to G L(r,\\mathbb{C})\
$$\
\
$$\
T\_{\\beta}=g\_{\\beta\\alpha}T\_{\\alpha}g\_{\\beta\\alpha}^{-1}\\Longleftrightarrow T\_{\\beta}^{-1}g\_{\\beta\\alpha}T\_{\\alpha}=g\_{\\beta\\alpha}.\
$$\
\
It deflnes new trivializations\
\
$$\
\\Phi\_{\\alpha}:E\_{\\alpha}\\to\\underline{{\\mathbb{C}}}^{r},\\quad\\Phi\_{\\alpha}=T\_{\\alpha}^{-1}\\circ\\Psi\_{\\alpha}.\
$$\
\
Notice that\
\
$$\
\\Phi\_{\\beta}\\circ\\Phi\_{\\alpha}^{-1}=T\_{\\beta}^{-1}\\Psi\_{\\beta}\\Psi\_{\\alpha}^{-1}T\_{\\alpha}=T\_{\\beta}^{-1}g\_{\\beta\\alpha}T\_{\\alpha}=g\_{\\beta\\alpha}\
$$\
\
so that 'fi are compatible with the gluing cocycle\
'=“– _T._ We obtain a new CR-operator\
\
gflfi. We will denote\
@„'.\
\
$$\
\\Phi\_{\\alpha}\
$$\
\
$$\
g\_{\\beta\\alpha}\
$$\
\
$$\
\\Phi=\\Psi\\circ T\
$$\
\
$$\
\\bar{\\partial}\_{\\Phi}\
$$\
\
If s is a section of Efi\
X\
\
then we can write\
\
$$\
E\_{\\alpha}\
$$\
\
$$\
s=\\sum\_{i}s\_{i}\\Psi\_{\\alpha}^{-1}(e\_{i})\\quad\\mathrm{and}\\quad T s=\\sum\_{i}s\_{i}\\Psi\_{\\alpha}^{-1}T\_{\\alpha}(e\_{i}).\
$$\
\
Note that\
\
$$\
\\bar{\\partial} _{\\Phi}T s=\\sum_{i}(\\bar{\\partial}s\_{i})\\Psi\_{\\alpha}^{-1}T\_{\\alpha}(e\_{i})=T\\sum\_{i}(\\bar{\\partial}s\_{i})\\Psi\_{\\alpha}^{-1}(e\_{i})=T\\bar{\\partial}\_{\\Psi}s.\
$$\
\
In other words\
\
$$\
\\bar{\\partial} _{\\Psi\\circ T}=T\\bar{\\partial}_{\\Psi}T^{-1}.\
$$\
\
The group G(E) of complex automorphisms of E acts on CRi(E) as\
above, by conjugation. We thus have a well deflned map\
\
$$\
\\mathbf{C}\\mathbf{R}\_{i}(E)\
$$\
\
$$\
\\mathrm{Hol}\\left(E\\right)\\rightarrow\\mathrm{CR}\_{i}\\left(E\\right)/\\mathrm{G}\\left(E\\right)\
$$\
\
which associates to each holomorphic structure “ on _E_ the G(E)-orbit in\
CRi(E) of the CR-operator @„. Observe that the sheaf OM(E;“) of local\
“\
sections of _E_ holomorphic with respect “ coincides precisely with the sheaf\
of local solutions of the partial difierential equation\
\
$$\
\\mathcal{G}(E)\
$$\
\
$$\
\\mathrm{CR}\_{i}(E)\
$$\
\
$$\
\\bar{\\partial}\_{\\Psi}\
$$\
\
$$\
\\mathcal{O}\_{M}(E,\\Psi)\
$$\
\
$$\
\\Psi\
$$\
\
$$\
\\bar{\\partial}\_{\\Psi}u=0,\\quad u\\quad \\mathrm{local\\quad smooth\\quad section\\quad of}\\quad E.\
$$\
\
If “1 and “2 are two holomorphic structures such that the associated CRoperators lie in the same orbit of G(E) then clearly the associated sheaves\
\
$$\
\\Psi\_{1}\
$$\
\
$$\
\\Psi\_{2}\
$$\
\
$$\
\\mathcal{G}(E)\
$$ of holomorphic sections are isomorphic as sheaves of _OM_-modules and, according to Exercise 1.4.10, the two holomorphic structures are isomorphic.\
This means that the map\
\
$$\
\\mathcal{O}\_{M}\
$$\
\
$$\
\\mathrm{Hol}\\left(E\\right)\\rightarrow\\mathrm{CR}\_{i}\\left(E\\right)\
$$\
\
is one-to-one. This map is also _surjective_ and we refer to \[ **29,** Chap. 2\]\
or \[ **63,** Chap. I\] for a proof of this nontrivial fact. The following results\
summarizes the above observations.\
\
Proposition 1.4.15. The map Hol (E)! CRi(E)=G(E), (E;“) 7! @„\
“\
_described above is a bijection._\
\
$$\
(E);\\longrightarrow;\\mathbf{CR} _{i}(E)/\\mathfrak{G}(E),;(E,\\Psi);\\mapsto;\\bar{\\partial}_{\\Psi}\
$$\
\
In view of this proposition, we can reconsider the manner in which we\
regard holomorphic bundles. In the sequel, by a holomorphic bundle over\
a complex manifold we will understand a pair _(E; L)_ where _E_ is a complex\
bundle and _L_ is an integrable CR-operator.\
\
$$\
(E,L)\
$$\
\
Suppose now that _E_ is equipped with a Hermitian metric _h._ As we have\
seen we have a bijection\
\
$$\
\\bar{\\partial} _{\\bullet}:\\mathcal{A}_{h}(E)\\longrightarrow\\mathbf{CR}(E),\\quad A\\mapsto\\bar{\\partial}\_{A}.\
$$\
\
Set\
\
$$\
\\mathcal{A} _{h}^{1,1}=\\bar{\\partial}_{\\bullet}^{-1}(\\mathbf{CR}\_{i}(E)).\
$$\
\
Lemma 1.4.16. The space A1;1h (E)\
such that FA2;0 = FA0;2 = 0.\
\
_consists of Hermitian connections A_\
\
$$\
\\mathcal{A}\_{h}^{1,1}(E)\
$$\
\
$$\
F\_{A}^{2,0}=F\_{A}^{0,2}=0\
$$\
\
Proof Suppose A 2 Ah1;1(E). Then using (1.4.19) we deduce FA0;2 = @„A2 =\
0\. On the other hand, since the connection _A_ is compatible with the metric\
h, the curvature FA is skew-Hermitian so that FA2;0 = ¡(F 2;0A)t = 0\. ¥\
\
$$\
A\\in\\mathcal{A}\_{h}^{1,1}(E)\
$$\
\
$$\
F\_{A}^{0,2}=\\bar{\\partial} _{A}^{2}=_\
_F_{A}\
$$\
\
$$\
F\_{A}^{2,0}=-(\\overline{F^{2,0}}\_{A})^{t}=0.\
$$\
\
$$\
\\mathcal{G}(E)\
$$\
\
»\
There is an action of G(E) onAh(E) induced by the isomorphism A1;1h (E) =\
CRi(E). More precisely, given T 2 G(E) and A 2 A1;1h (E) we deflne T ¢ A\
by the equality\
„ _„¡_ 1\
\
$$\
\\mathcal{A}\_{h}(E)\
$$\
\
$$\
\\mathcal{A}\_{h}^{1,1}(E)\\cong\
$$\
\
$$\
\\mathbf{CR}\_{i}(E)\
$$\
\
$$\
T\\in\\mathcal{G}(E)\
$$\
\
$$\
A\\in\\mathcal{A}\_{h}^{1,1}(E)\
$$\
\
$$\
T\\cdot A\
$$\
\
$$\
\\bar{\\partial} _{T\\cdot A}=T\\bar{\\partial}_{A}T^{-1}.\
$$\
\
We have thus proved the following result.\
\
**Proposition 1.4.17.** _Any Hermitian metric h on a complex vector bundle_\
_E over a complex manifold deflnes a bijection_\
\
$$\
\\mathrm{Hol}(E)\\cong\\mathcal{A}\_{h}^{1,1}(E)/\\mathcal{G}(E).\
$$\
\
_Moreover, any integrable CR-operator @„ on E induces a unique holomorphic_\
structure “ on E and a unique Hermitian connection A such @„A = @„ = @„.\
“\
\
$$\
\\bar{\\partial}\
$$\
\
$$\
\\bar{\\partial} _{A}=\\bar{\\partial}=\\bar{\\partial}_{\\Psi}\
$$\
\
* * *\
\
**Remark 1.4.18.** The above identiflcation has profound consequences. For\
example, in **\[58\]** it is shown that, modulo some topological identiflcations,\
it contains as a special case the classical Abel-Jacobi theorem.\
\
**Example 1.4.19.** Suppose _L!M_ is a complex line bundle over a complex\
manifold _M_ equipped with a Hermitian metric _h._ The group G(L) can be\
identifled with the group of smooth maps\
\
$$\
L\\rightarrow M\
$$\
\
$$\
\\mathcal{G}(L)\
$$\
\
$$\
f:M\\to\\mathbb{C}^\*.\
$$\
\
Suppose we are given an integrable CR-operator _@„_ on _L._ This induces a\
holomorphic structure on _L_ and a Hermitian connection _A_ such that\
„ „\
\
$$\
\\bar{\\partial}\
$$\
\
$$\
L.\
$$\
\
$$\
\\bar{\\partial} _{A}=\\bar{\\partial}\\quad\\mathrm{and}\\quad F_{A}\\in\\Omega^{1,1}(M).\
$$\
\
To flnd an explicit local description of _A_ we choose a local trivializing patch\
_U_ and a nowhere vanishing holomorphic section _s_ of _L_ over _U._ Set\
\
$$\
\\rho=h(s,s)=\|s\|\_{h}^{2}.\
$$\
\
The connection _A_ is locally described by a (1;0)-form determined by the\
conditions\
rAs = s;\
\
$$\
\\theta\
$$\
\
$$\
\\begin{aligned}\\nabla^{A}s&=\\theta s,\\d\\rho=\\theta h(s,s)+\\bar{\\theta}h(s,s)&=\\rho(\\theta+\\bar{\\theta}).\\end{aligned}\
$$\
\
from which we deduce\
\
$$\
\\theta=\\frac{\\partial\\rho}{\\rho}=\\partial\\log\\rho.\
$$\
\
The curvature of _A_ is given by the 2-form\
„\
\
$$\
d\\theta=\\bar{\\partial}\\partial\\log\\rho.\
$$\
\
Suppose now that f 2 G(L). We get a new CR-operator @„f on L:\
„\
\
$$\
f\\in\\mathcal{G}(L)\
$$\
\
$$\
\\bar{\\partial}\_{f}\
$$\
\
$$\
L\\mathrm{:}\
$$\
\
$$\
\\bar{\\partial}\_{f}=f\\bar{\\partial}f^{-1}=\\bar{\\partial}-\\frac{\\bar{\\partial}f}{f}\
$$\
\
deflning the same holomorphic structure on _L_ as @„. Its associated Chern\
connection, denoted by Af, can be determined as in the proof of Proposition\
1.4.13 using the equality\
„ „\
\
$$\
\\bar{\\partial}.\
$$\
\
$$\
A\_{f}\
$$\
\
$$\
A\_{f}-A=-\\frac{\\bar{\\partial}f}{f}+\\frac{\\partial\\bar{f}}{\\bar{f}}.\
$$\
\
This formula describes the action of G(L) onA\
\
1;1h (L).\
\
$$\
\\mathcal{A}\_{h}^{1,1}(L)\
$$\
\
Suppose that instead of the metric _h_ we work with the metric\
\
$$\
h\_{u}=\\exp(2u)h\
$$\
\
where u is a smooth real valued function on M. Denote by Au the Chern\
connection associated to the CR-operator @„ and the metric hu. Then\
\
$$\
A\_{u}\
$$\
\
$$\
\\bar{\\partial}\
$$\
\
$$\
h\_{u}\
$$\
\
$$\