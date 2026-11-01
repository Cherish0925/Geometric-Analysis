---
retention_scope: session
part: 2
total_parts: 13
---

[Part 2/13 of: Notes on Seiberg-Witten Theory Liviu I. Nicolaescu]

The space of Lp-sections of E (modulo equality almost everywhere) is
denoted by Lp(E). The space Lploc(E) consists of measurable sections u of
E such that u’ 2 Lp(E) for any smooth, compactly supported function on
_M._

$$
L^{p}(E)
$$

$$
\\overline{L\_{loc}^{p}(E)}
$$

$$
u\\varphi\\in L^{p}(E)
$$

**Proposition 1.2.12.**

Lp(E) is a Banach space with respect to the norm
( ¡R
¢

$$
\|\\psi\| _{p,E}=\\left{\\begin{array}{r l}{\\left(\\int_{M}\|\\psi(x)\|^{p}d v\_{g}(x)\\right)^{1/p}}&{i f;p<\\infty}\ {\\mathrm{ess}\\operatorname\*{s u p}\_{x}\|\\psi(x)\|}&{i f;p=\\infty}\\end{array}\\right..
$$

For each _m_ = _1;_ 2

_; ¢¢¢_ deflne _r_

m as the composition

$$
m=1,2,\\cdots
$$

$$
\\nabla^{m}
$$

$$
\\nabla^{m}:;C^{\\infty}(E)\\stackrel{\\nabla^{E}}{\\to}C^{\\infty}(T^{ _}M\\otimes E)\\stackrel{\\nabla^{T^{_}M\\otimes E}}{\\longrightarrow}\\cdots\\stackrel{\\nabla}{\\to}C^{\\infty}(T^{\*}M^{\\otimes m}\\otimes E)
$$

where we used the symbol _r_ to generically denote the connections in the
⁄ ›j
tensor products T M › E induced by rg and rE.

$$
T^{\*}M^{\\otimes j}\\otimes E
$$

$$
\\nabla^{g}
$$

$$
\\nabla^{E}
$$

The metrics _g_ and _h_ induce metrics in each
⁄ ›m
_T M › E,_ and in particular, we can deflne the spaces

of the tensor bundles
⁄ ›m
Lp(T M › E).

$$
T^{\*}M^{\\otimes m}\\otimes E
$$

$$
L^{p}(T^{\*}M^{\\otimes m}\\otimes E)
$$

Deflnition 1.2.13. (a) Let u 2 L1loc(E) and v 2 L1
say that rmu = v weakly if
Z Z

⁄ ›m
loc(T M › E). We

$$
u\\in L\_{loc}^{1}(E)
$$

$$
v\\in L\_{loc}^{1}(T^{\*}M^{\\otimes m}\\otimes E)
$$

$$
\\nabla^{m}u=v
$$

$$
\\int\_{M}\\langle v,\\phi\\rangle d v\_{g}=\\int\\langle u,(\\nabla^{m})^{ _}\\phi\\rangle d v\_{g},\\quad\\forall u\\in C\_{0}^{\\infty}(T^{_}M^{\\otimes m}\\otimes E).
$$

(b) Deflne Lm;p(E) as the space of sections u 2
⁄ ›j
1;:::;m there exist vj 2 Lp(T M › E) such that
deflne the Sobolev norm k ¢ km;p by

Lp(E) such that 8j =
rju = vj weakly. We

$$
L^{m,p}(E)
$$

$$
u;\\in;L^p(E)
$$

$$
\\forall j=
v\_{j}\\in L^{p}(T^{\*}M^{\\otimes j}\\otimes E)
$$

$$
1,\\ldots,m
$$

$$
\\nabla^{j}\\boldsymbol{u}=\\boldsymbol{v}\_{j}
$$

$$
\|\\cdot\|\_{m,p}
$$

$$
\|u\| _{m,p}=\|u\|_{m,p,E}=\\sum\_{j=1}^{p}\|\\nabla^{j}u\|\_{p}.
$$

Proposition 1.2.14. (Lk;p(E); k¢kk;p;E) is a Banach space which is reexive
_if_ 1 < _p<1._

$$
(L^{k,p}(E),\|\\cdot\|\_{k,p,E})
$$

$$
\\text{"}1<p<\\infty
$$

* * *

**Exercise 1.2.1. (Kato’s Inequalities)** Suppose _E!M_ is a Hermitian
vector bundle over an oriented Riemannian manifold ( _M;_ g). Fix a Hermitian
connection _r_ on _E._

(a) Show that for every u 2 L1;2loc(E) the function

$$
u\\in L\_{loc}^{1,2}(E)
$$

$$
M\\ni x\\mapsto\|u(x)\|
$$

is in Lloc1;2(M) and moreover

$$
L\_{loc}^{1,2}(M)
$$

$$
\\left\|d\|u(x)\|\\right\|\\leq\\left\|(\\nabla u)(x)\\right\|
$$

almost everywhere on _M._

⁄
(b) Set ¢E:= r r and denote by ¢M the Laplacian on M. Show that for
all u 2 Lloc2;2(E) we have

$$
\\Delta\_{E}:=\\nabla^{\*}\\nabla
$$

$$
\\Delta\_{M}
$$

$$
u\\in L\_{loc}^{2,2}(E)
$$

$$
\\Delta\_{M}\\left(\|u\|^{2}\\right)=2\\Re\\mathfrak{e}\\langle\\Delta\_{E}u,u\\rangle-2\|\\nabla u\|^{2}
$$

so that

$$
\\Delta\_{M}\|u\|^{2}\\leq2\\mathfrak{R e}\\langle\\Delta\_{E}u,u\\rangle
$$

almost everywhere on _M._

The H˜older spaces can be deflned on manifolds as well. If _(M; g)_ isa
Riemannian manifold then _g_ canonically deflnes a metric space structure
on _M_ and, in particular, we can talk about the oscillation of a function
_u_ : _M !_ K. On the other hand, deflning the oscillation of a section of some
bundle over _M_ requires a little more work.

$$
(M,g)
$$

$$
u:M\\to\\mathbb{K}
$$

Let (E; h; r) as before. We assume the injectivity radius ‰M of M is
positive. Set ‰0 = minf1; ‰M g. Ifx; y 2 M are two points such that
distg(x; y) • ‰0 then they can be joined by a unique minimal geodesicx;y
starting at x and ending at y. We denote by Tx;y: Ey! Ex the rE-parallel
transport along x;y. For each »2Ex and ·2Ey we set by deflnition

$$
\\rho\_{M}
$$

$$
\\rho\_{0};=;\\min{1,\\rho\_{M}}
$$

$$
x,y\\in M
$$

$$
\\operatorname{dist} _{g}(x,y)\\leq\\rho_{0}
$$

$$
\\gamma\_{x,y}
$$

$$
T\_{x,y}:E\_{y}\\xrightarrow{}E\_{x}
$$

$$
\\nabla^{E}
$$

$$
\\gamma\_{x,y}
$$

$$
\\xi\\in E\_{x}
$$

$$
\\eta\\in E\_{y}
$$

$$
\|\\xi-\\eta\|=\|\\xi-T\_{x,y}\\eta\| _x=\|\\eta-T_{y,x}\\xi\|\_y.
$$

If _u_ : _M!E_ is a section of _E_ and

S‰M has diameter < ‰0 we deflne

$$
u:M\\rightarrow E
$$

$$
S\\subset M
$$

$$
<\\rho\_{0}
$$

$$
\\operatorname{osc}\\left(u;S\\right)=\\operatorname\*{s u p}{\|u(x)-u(y)\|;x,y\\in S}.
$$

Finally set

$$
\[u\] _{\\alpha,E}=\\operatorname\*{s u p}{r^{-\\alpha}{\\operatorname{osc}}\\left(u;;;B_{r}(x)\\right);;;0<r<\\rho\_{0},;x\\in M}.
$$

For any _k ‚_ 0 deflne the _H˜older norm_

$$
k\\geq0
$$

$$
\|u\| _{k,\\alpha,E}=\\sum_{j=0}^{k}\|\\nabla^{j}u\| _{\\infty,E}+\[\\nabla^{m}u\]_{\\alpha,T^{\*}M^{\\otimes m}\\otimes E}.
$$

and set

$$
C^{k,\\alpha}(E)={u\\in C^{k}(E);;;\|u\|\_{k,\\alpha}<\\infty}.
$$

* * *

**Theorem 1.2.15.** _Let (M; g) be a_ **compact,** _N -dimensional, oriented Riemannian manifold and E a vector bundle over M equipped with a metric h_
_and compatible connection r. Then the following are true._

$$
(M,g)
$$

(a) The Sobolev space Lm;p(E) and the H˜older spaces Ck;fi(E) do not depend
_on the metrics g; h and on the connection r. More precisely, if g1 is a_ _difierent metric on M and r1 is another connection on E compatible with_ _some metric h1 then_

$$
L^{m,p}(E)
$$

$$
C^{k,\\alpha}(E)
$$

$$
g\_{1}
$$

$$
\\nabla^{1}
$$

$$
h\_{1}
$$

$$
L^{m,p}(E,g,h,\\nabla)=L^{m,p}(E,g\_{1},h\_{1},\\nabla^{1})\\quad{a s ~~s e t s~~ o f~s e c t i o n s}
$$

_and the identity map between these two spaces is a Banach space isomorphism. A similar statement is true for the H˜older spaces._

(b) If 1 • p<1 then C1(E) is dense in Lk;p(E).

$$
1\\leq p<\\infty
$$

$$
L^{k,p}(E)
$$

$$
C^{\\infty}(E)
$$