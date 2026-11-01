---
retention_scope: session
part: 11
total_parts: 13
---

[Part 11/13 of: Notes on Seiberg-Witten Theory Liviu I. Nicolaescu]

so that\
\
$$\
4\\ell h(\\sigma\_{n})(h(\\sigma\_{n})-1)=\\frac{4(n+1)(n+1+\\ell)}{\\ell}.\
$$\
\
To compute the integral term we use the intersection form on H2(N;Z)\
induced by the Poincar¶e duality\
\
$$\
H^{2}(N,\\mathbb{Z})\
$$\
\
$$\
H^{2}(D\_{\\ell},\\partial D\_{\\ell};\\mathbb{Z})\\times H^{2}(D\_{\\ell},\\mathbb{Z})\\to\\mathbb{Z}.\
$$\
\
Then\
\
$$\
\\int\_{\\hat{N} _{\\ell}}c_{1}(\\hat{A} _{n})\\wedge c_{1}(\\hat{A}\_{n})=\\frac{(2n+2+\\ell)^{2}}{\\ell}\
$$\
\
⁄\
since det(^n)=… L2n+2+‘. We conclude that\
\
$$\
\\left(\\hat{\\sigma} _{n}\\right)=\\pi^{\*}L_{2n+2+\\ell}.\
$$\
\
$$\
\\dim\\ker\_{ex}\\mathfrak{D}\_{\\hat{A}\_n}^\*=0.\
$$\
\
* * *\
\
## 4.2. Finite energy monopoles\
\
This very technical section ofiers a glimpse into the analytical theory of\
the Seiberg-Witten equations on 4-manifolds with cylindrical ends. To keep\
the technical details within reasonable limits we will consider only some\
special, simpler situations required by the topological applications we have\
in mind. This choice has an academic advantage as well: it ofiers the reader\
a quite extensive picture of what to expect relying on a relatively moderate\
analytical machinery. For an exhaustive presentation of this type of problem\
in the Yang-Mills context we refer to \[ **96, 133\].**\
\
We tried to keep the presentation as self-contained as possible but, to\
keep the length of this section within reasonable limits, we had to appeal\
to certain basic facts about elliptic partial difierential equations we did not\
include in this book. These can be found in \[ **47, 105\].**\
\
**4.2.1. Regularity.** Suppose _N^_ is an oriented cylindrical 4-manifold with\
N := @1N^. Fix a cylindrical spinc structure ^¿ = (^; ; ’) onN^ ( := @1^)\
^ ^ ^¡\
(see x4.1.1 for precise deflnitions). Denote by S^= S+ ' S the bundle of\
^ ^\
complex spinors associated to ^, and by S the bundle of complex spinors\
associated to. S^ can be equipped with a cylindrical structure such that\
S = @1S^+.\
^\
\
$$\
\\hat{N}\
$$\
\
$$\
N:=\\partial\_{\\infty}\\hat{N}\
$$\
\
$$\
s p i n^{c}\
$$\
\
$$\
\\hat{\\tau}=\\left(\\hat{\\sigma},\\sigma,\\varphi\\right)\
$$\
\
$$\
\\hat{N}\\left(\\sigma:=\\partial\_{\\infty}\\hat{\\sigma}\\right)\
$$\
\
$$\
\\S4.1.1\
$$\
\
$$\
\\hat{\\mathbb{S}} _{\\hat{\\sigma}}=\\hat{\\mathbb{S}}_{\\hat{\\sigma}}^{+}\\oplus\\hat{\\mathbb{S}}\_{\\hat{\\sigma}}^{-}\
$$\
\
$$\
\\hat{\\sigma}\
$$\
\
$$\
\\mathbb{S}\_{\\sigma}\
$$\
\
$$\
\\sigma.\\quad\\hat{\\mathbb{S}}\_{\\sigma}\
$$\
\
$$\
\\mathbb{S} _{\\sigma}=\\partial_{\\infty}\\hat{\\mathbb{S}}\_{\\hat{\\sigma}}^{+}\
$$\
\
We denote by C^ the conflguration space consisting of pairs C^ := ( _ˆ;^_ A^)\
^\
where ˆ^ 2 Lloc2;2(S^+) and A^ is an L2;2loc Hermitian connection of det(^). Deflne\
^\
Gb as the space of Lloc3;2-maps ^ : N^! S1. For every point p0 2 N^ we\
^\
deflne the subgroup Gb _(p0) ‰_ Gb consisting of maps ^ : _N^! S1_ such that\
^\
^(p0) = 1\. (Such gauge transformations are said to be _based at p0._)\
\
$$\
\\hat{\\mathcal{C}}\_{\\hat{\\sigma}}\
$$\
\
$$\
\\hat{\\mathsf{C}}:=\\left(\\hat{\\psi},\\hat{A}\\right)\
$$\
\
$$\
\\hat{\\psi}\\in L\_{l o c}^{2,2}(\\hat{\\mathbb{S}}\_{\\hat{\\sigma}}^{+})\
$$\
\
$$\
\\det(\\hat{\\sigma})\
$$\
\
$$\
\\hat{A}\
$$\
\
$$\
L\_{loc}^{2,2}\
$$\
\
$$\
\\widehat{\\mathcal{G}}\_{\\widehat{\\sigma}}\
$$\
\
$$\
L\_{loc}^{3,2}\
$$\
\
$$\
\\hat{\\gamma}:\\hat{N}\\rightarrow S^{1}\
$$\
\
$$\
p\_{0}\\in\\hat{N}\
$$\
\
$$\
\\widehat{\\mathcal{G}} _{\\hat{\\sigma}}(p_{0})\\subset\\widehat{\\mathcal{G}}\_{\\sigma}\
$$\
\
$$\
\\hat{\\gamma}:\\hat{N}\\rightarrow S^{1}\
$$\
\
$$\
\\hat{\\gamma}(p\_{0})=1\
$$\
\
$$\
p\_{0}.\\big)\
$$\
\
A _flnite energy monopole_ is a conflguration C\
the Seiberg-Witten equations\
(\
\
^ =(ˆ;^ A^) _2_ C^ satisfying\
\
$$\
\\hat{\\mathsf{C}}=(\\hat{\\psi},\\hat{A})\\in\\hat{\\mathcal{C}}\
$$\
\
$$\
\\left{\\begin{array}{r c l}{\\hat{\\mathfrak{D}} _{\\hat{A}}\\hat{\\psi}}&{=}&{0}\ {F_{\\hat{A}}^{+}}&{=}&{\\hat{\\mathbf{c}}^{-1}\\big(\\frac{1}{2}q(\\psi)\\big)}\ \\end{array}\\right.\
$$\
\
and the growth condition\
Z ‡\
\
$$\
E(\\hat{\\mathsf{C}}):=\\int\_{\\hat{N}}\\Bigl(\|\\hat{\\nabla}^{\\hat{A}}\\hat{\\psi}\|^{2}+\\frac{1}{8}\|q(\\hat{\\psi})\|^{2}+\|F\_{\\hat{A}}\|^{2}+\\frac{\\hat{s}}{4}\|\\hat{\\psi}\|^{2}\\Bigr)d v(\\hat{g})<\\infty.\
$$\
\
We will denote by Z^^ the set of flnite energy monopoles on N^.\
\
$$\
\\hat{\\mathcal{Z}}\_{\\hat{\\sigma}}\
$$\
\
$$\
\\hat{N}\
$$\
\
As in the closed case, we will need to use perturbation parameters. In\
this case they will take the form of closed, _compactly supported_ 2-forms\
· 2 ›2(N^) of appropriate regularity.\
\
$$\
\\eta\\in\\Omega^{2}(\\hat{N})\
$$\
\
**Proposition 4.2.1.** _Let_ C^ =(ˆ;^ A^) _2_ Z^. _Then there exists_ ^ _2_ Gb _such_\
^ ^\
that ^ ¢ C^ 2 C1.\
\
$$\
\\hat{\\mathsf{C}}=(\\hat{\\psi},\\hat{A})\\in\\hat{\\mathcal{Z}}\_{\\hat{\\sigma}}\
$$\
\
$$\
\\hat{\\gamma}\\in\\widehat{\\mathcal{G}}\_{\\hat{\\sigma}}\
$$\
\
$$\
\\hat{\\gamma}\\cdot\\hat{\\mathsf{C}}\\in C^{\\infty}\
$$\
\
* * *\
\
**Proof** The proof relies on the following technical result.\
\
**Lemma 4.2.2.** _Suppose M is a smooth, compact, oriented Riemannian_ 4-\
manifold with smooth boundary @M = N, 2 Spinc(M) and C = (ˆ; A) is\
a L2;2-monopole corresponding to the spinc-structure. Then there exists a\
Lloc3;2-map f : M ! R such that eif ¢ C is smooth in the interior of M.\
\
$$\
\\partial M=N,\\sigma\\in\\mathrm{S p i n^c}(M)\
$$\
\
$$\
\\mathsf{C}=(\\psi,A)\
$$\
\
$$\
L^{2,2}\
$$\
\
$$\
sp i n^{c}.\
$$\
\
$$\
L\_{loc}^{3,2}-map\ f:M\\to\\mathbb{R}\
$$\
\
$$\
e^{\\mathbf{i}f}\\cdot\\mathsf{C}\
$$\
\
We will present the proof of this lemma after we explain why it implies\
Proposition 4.2.1.\
\
Let C^ =(ˆ;^ A^) be a flnite energy monopole on N^. Set Cn:= (n; n+ 2)£\
N, n 2 Z+. Using Lemma 4.2.2 we can flnd L3;2loc-maps\
\
$$\
\\hat{\\mathsf{C}}=(\\hat{\\psi},\\hat{A})\
$$\
\
$$\
\\hat{N}\
$$\
\
$$\
C\_{n}:=(n,n+2)\\times\
N,n\\in\\mathbb{Z} _+_\
_L_{loc}^{3,2}\
$$\
\
$$\
f:\\hat{N} _{1}=\\hat{N}\\setminus(1,\\infty)\\times N\\to\\mathbb{R},\\quad f_{n}:C\_{n}\\to\\mathbb{R}\
$$\
\
such that\
\
$$\
e^{\\mathbf{i}f}\\cdot\\hat{\\mathsf{C}}\\mid\_{\\hat{N} _{1}}\\in C^{\\infty}(\\hat{N}_{1}),\\quad e^{\\mathbf{i}f\_{n}}\\hat{\\mathsf{C}}\\mid\_{C\_{n}}\\in C^{\\infty}(C\_{n}),\\quad\\forall n\\in\\mathbb{Z}\_{+}.\
$$\
\
Set u0 = f0 ¡ f, un:= fn\
function on ( _n; n_ \+ 1)£ _N,_\
\
¡ fn¡1, 8n ‚ 1. Observe that un is a smooth\
8n 2 Z+ because on this cylinder we have\
¡ ¢\
\
$$\
u\_{0}=f\_{0}-f,;u\_{n}:=f\_{n}-f\_{n-1},;\\forall n\\geq1\
$$\
\
$$\
u\_{n}\
$$\
\
$$\
(n,n+1)\\times N\
$$\
\
$$\
\\in\\mathbb{Z}\_{+}\
$$\
\
$$\
-2\\mathbf{i}d u\_{n}=e^{\\mathbf{i}f\_{n}}\\cdot\\hat{A}-e^{\\mathbf{i}f\_{n-1}}\\cdot\\hat{A}\\in C^{\\infty}\\big((n,n+1)\\times N\\big).\
$$\
\
¡ ¢\
Fix 0 <"¿ 1/8. For each n 2 Z+ deflne ’n 2 C1comp N^ such that ’n · un\
on (n + 1/2 ¡ "; n+ 1/2 \+ ")£ N and ’n · 0 outside (n + 1/2 ¡ 2"; n+ 1/2 \+ 2")£ N.\
Finally, set\
\
$$\
0<\\varepsilon\\ll\\frac{1}{8}\
$$\
\
$$\
n\\in\\mathbb{Z}\_{+}\
$$\
\
$$\
\\varphi\_{n}\\in C\_{c o m p}^{\\infty}\\left(\\hat{N}\\right)\
$$\
\
$$\
\\varphi\_{n}\\equiv u\_{n}\
$$\
\
$$\
\\left(n+\\frac{1}{2}-\\varepsilon,n+\\frac{1}{2}+\\varepsilon\\right)\\times N\
$$\
\
$$\
\\varphi\_{n}\\equiv0\
$$\
\
$$\
\\left(n+\\frac{1}{2}-2\\varepsilon,n+\\frac{1}{2}+2\\varepsilon\\right)\\times N\
$$\
\
$$\
h\_{n}:(n-1/2-\\varepsilon,n+1/2+\\varepsilon)\\times N\\to\\mathbb{R},\\quad h\_{n}=f\_{n-1}+\\varphi\_{n},\\quad n\\geq1,\
$$\
\
and\
\
$$\
h\_{0}\\equiv f+\\varphi\_{0};\\mathrm{ ~~o n~~};\\hat{N}\\setminus\[1/2,\\infty)\\times N.\
$$\
\
Observe that hn¡1· hn on (\
(hn) deflnes an Lloc3;2-map\
\
1 1\
_n_ \+ _¡ "; n+_ \+ _")£ N_\
2 2\
h : N^! R:\
\
so that the collection\
\
$$\
h\_{n-1}\\equiv h\_{n}on(n+\\frac{1}{2}-\\varepsilon,n+\\frac{1}{2}+\\varepsilon)\\times N\
$$\
\
$$\
\\left(h\_{n}\\right)\
$$\
\
$$\
L\_{loc}^{3,2}-map\
$$\
\
$$\
h:\\hat{N}\\rightarrow\\mathbb{R}.\
$$\
\
On the other hand, on the cylinder ( _n ¡_ 1=2 _¡ "; n_ \+ 1\
‡ ·\
\
=2+") _£ N_ we have\
\
$$\
(n-1/2-\\varepsilon,n+1/2+\\varepsilon)\\times N\
$$\
\
$$\
e^{\\mathbf{i}h}\\cdot\\hat{\\mathsf{C}}=e^{\\mathbf{i}\\varphi\_{n}}\\cdot\\left(e^{\\mathbf{i}f\_{n-1}}\\hat{\\mathsf{C}}\\right)\\in e^{\\mathbf{i}\\varphi\_{n}}\\cdot C^{\\infty}\\subset C^{\\infty}.\\quad\\blacksquare\
$$\
\
**Proof of Lemma 4.2.2** Fix a Hermitian connection _A0_ on det() which\
is smooth up to the boundary of _M_ and set **ia** := _A¡A0._ The Dirichlet\
problem\
‰\
⁄\
¢ u = 12d a in M\
\
$$\
A\_{0}\
$$\
\
$$\
:=A-A\_{0}\
$$\
\
$$\
\\left{\\begin{array}{r c l}{\\Delta\_{M}u}&{=}&{\\frac{1}{2}d^{\*}a\\quad\\mathrm{in}\\quad M}\ {u}&{=}&{0\\quad\\mathrm{on}\\quad\\partial M}\ \\end{array}\\right.\
$$\
\
has a unique solution u 2 L3;2(M) (see \[47, Chap. 8\]). Set := eiu and\
( _\`;_ B):= _¢_ ( _ˆ;_ A). If **ib** := _B¡A0_ then\
\
$$\
u\\in L^{3,2}(M)\
$$\
\
$$\
\\gamma:=e^{\\mathbf{i}u}\
$$\
\
$$\
\\left(\\phi,B\\right):=\\gamma\\cdot\\left(\\psi,A\\right)\
$$\
\
$$\
\\mathbf{i}b:=B-A\_{0}\
$$\
\
$$\
\\mathbf{i}b=\\mathbf{i}a-2\\mathbf{i}du\
$$\
\
* * *\
\
⁄ ⁄\
so that d b = i(d a ¡ 2¢M u) = 0. The Seiberg-Witten equations for (\`; B)\
can be rewritten as an _elliptic_ system\
\
$$\
d^{ _}b=\\mathbf{i}\\left(d^{_}a-2\\Delta\_{M}u\\right)=0\
$$\
\
$$\
\\left(\\phi,B\\right)\
$$\
\
(4.2.1a)\
\
$$\
\\mathfrak{D} _{A_{0}}\\phi=-\\frac{1}{2}\\mathbf{c}(\\mathbf{i}b)\\phi,\
$$\
\
(4.2.1b)\
\
$$\
(d^{+}\\oplus d^{\*})b=\\left(\\frac{1}{2}q(\\phi)-F\_{A\_{0}}^{+}\\right)\\oplus0.\
$$\
\
An elliptic bootstrap, identical to the one in the proof of Proposition 2.1.11\
of x2.1.2 concludes the proof of Lemma 4.2.2. ¥\
\
Proposition 4.2.1 shows that there is no loss of generality by working only\
with _smooth_ flnite energy monopoles. Observe also that nowhere in the proof\
have we relied on the growth condition E(C^) < _1_ to establish regularity\
modulo Gb. The growth condition afiects only the asymptotic behavior. In\
particular, the considerations in 2.4.1 show that\
\
$$\
E(\\hat{C})<\\infty\
$$\
\
$$\
\\widehat{\\mathcal{G}}.\
$$\
\
$$\
\\hat{\\mathcal{Z}}\_{\\hat{\\sigma}}\\neq\\emptyset\\implies\\mathit{t h e r e ~~e x i s t~~ t h r e e-d i m e n s i o n a l ~~\\sigma-m o n o p o l e s~~ o n ~~N~~}\
$$\
\
_=; =) there exist three-dimensional-monopoles on N_\
In the next subsection we will have a closer look at three-dimensional monopoles.\
\
c\
4.2.2. Three-dimensional monopoles. Consider a closed, compact, ori-structure 2 Spinc(N).\
ented We want to deflne a functional set-up which closely follows the relationship Riemannian manifold _(N; g)_ and a _spin_\
between the four- and three-dimensional theory.\
\
$$\
(N,g)\
$$\
\
$$\
spin^{c}\
$$\
\
$$\
\\sigma;\\in;S p i n^{c}(N)\
$$\
\
Deflne a conflguration space C consisting of pairs _(ˆ; A)_ where _ˆ 2_\
L2;2(S) and A is an L2;2-connection on det(). (Often we will need to\
consider conflgurations of difierent regularity, which will be indicated by\
Sobolev superscripts attached to C. E.g., Cr refers to conflgurations in\
Lr;2.)\
\
$$\
\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
(\\psi,A)\
$$\
\
$$\
\\psi\\in\
$$\
\
$$\
L^{2,2}(\\mathbb{S}\_{\\sigma})\
$$\
\
$$\
L^{2,2}\
$$\
\
$$\
(\\sigma)\
$$\
\
$$\
\\mathcal{C} _{\\sigma}.\ E.g.,\ \\mathcal{C}_{\\sigma}^{r}\
$$\
\
$$\
\\left(L^{r,2}.\\right)\
$$\
\
Denote by G the group of L3;2-maps : N!S1. Observe that since\
dimN = 3 the Sobolev-Morrey embedding theorem implies L3;2 embeds in\
a H˜older space and, as in x2.1.2, we can conclude that G is a Hilbert-Lie\
group with commutative Lie algebra T1G := L3;2(N;iR). For every ⁄2N\
we set\
G (⁄):=f 2 G; (⁄) = 1g:\
\
$$\
\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
L^{3,2}-maps\\gamma:N\\to S^1\
$$\
\
$$\
N=3\
$$\
\
$$\
L^{3,2}\
$$\
\
$$\
\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
T\_{1}\\mathfrak{G}\_{\\sigma}:=L^{3,2}(N,\\mathbf{i}\\mathbb{R})\
$$\
\
$$\
\*\\in N\
$$\
\
$$\
\\mathbb{G} _{\\sigma}(\*):={\\gamma\\in\\mathbb{G}_{\\sigma};\\gamma(\*)=1}.\
$$\
\
G (⁄) will be called the group of gauge transformations based at _⁄._ Observe\
that G (⁄) acts _freely_ on C. Now set B : C _=G_ and B (⁄):=C (⁄)=G (⁄).\
As in x2.2.2 we can equip B and B (⁄) with natural Sobolev metrics.\
\
$$\
\\mathcal{G}\_{\\sigma}(\*)\
$$\
\
$$\
\*\
$$\
\
$$\
\\mathcal{G}\_{\\sigma}(\*)\
$$\
\
$$\
\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
\\mathcal{B} _{\\sigma}:\\mathcal{C}_{\\sigma}/\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
\\bar{\\mathcal{B}} _{\\sigma}(\*):=\\mathcal{C}_{\\sigma}( _)/\\mathcal{G}\_{\\sigma}(_)\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}(\*)\
$$\
\
For every C _2_ C we denote by\
\
$$\
\\mathsf{C}\\in\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
\\mathfrak{L} _{\\mathsf{C}}:T_{1}\\mathfrak{G} _{\\sigma}\\to T_{\\mathsf{C}}\\mathfrak{C}\_{\\sigma}\
$$ the inflnitesimal action at C\
\
$$\
\\mathfrak{L} _{\\mathsf{C}}(\\mathbf{i}f):=\\frac{d}{d t}\\left\|_{t=0}\\right.e^{\\mathbf{i}t f}\\cdot\\mathsf{C}=(\\mathbf{i}f\\psi,A-2\\mathbf{i}d f).\
$$\
\
Its formal _(L2)_ adjoint is\
\
$$\
(L^{2})\
$$\
\
$$\
T\_{\\mathsf{C}}\\mathfrak{C} _{\\sigma}\\ni\\dot{\\mathsf{C}}\\mapsto\\mathfrak{L}_{\\mathsf{C}}^{ _}\\dot{\\mathsf{C}}=\\mathfrak{L}\_{\\mathsf{C}}^{_}(\\dot{\\psi},\\mathbf{i}\\dot{a})=-2\\mathbf{i}d^{\*}\\dot{a}-\\mathbf{i}\\mathfrak{I m}\\langle\\psi,\\dot{\\psi}\\rangle.\
$$\
\
As in the four-dimensional case, we can identify ker LC with the Lie algebra\
of the stabilizer **Stab** (C) with respect to the G action.\
\
$$\
\\mathfrak{L}\_{\\mathsf{C}}\
$$\
\
$$\
\\mathcal{G}\_{\\sigma}\
$$\
\
Since C is an a–ne space we can identify the tangent space TCC with\
C via the map\
\
$$\
\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
T\_{\\mathsf{C}}\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
\\dot{\\mathsf{C}}\\mapsto\\mathsf{C}+\\dot{\\mathsf{C}}.\
$$\
\
$$\
\\mathcal{C}\_{\\sigma}\
$$\
\
»\
Deflne the slice SC ‰ TCC = C at C by\
\
$$\
\\mathcal{S} _{\\mathsf{C}}\\subset T_{\\mathsf{C}}\\mathcal{C} _{\\sigma}\\cong\\mathcal{C}_{\\sigma}\
$$\
\
$$\
\\mathsf{C}\
$$\
\
$$\
\\mathcal{S} _{\\mathsf{C}}:=\\ker\\mathfrak{L}_{\\mathsf{C}}^{\*}\\cap L^{2,2}.\
$$\
\
⁄\
More generally, we set SCr:= ker LC \ Lr;2. The slice at C is equipped with\
a natural **Stab** (C)-action and, exactly as in the four-dimensional case (see\
x2.2.2), we have the following result.\
\
$$\
\\mathcal{S} _{\\mathsf{C}}^{r}:=\\ker\\mathfrak{L}_{\\mathsf{C}}^{\*}\\cap L^{r,2}\
$$\
\
**Proposition 4.2.3.** _There exists a small_ **Stab** (C)- _invariant neighborhood_\
UC of C 2 SC such that every orbit of G which intersects UC does so trasver-\
_sally, along a single_ **Stab** (C)- _orbit. In particular, every_ G (⁄)- _orbit inter-_\
sects UC transversely in at most one point.\
\
$$\
U\_{\\mathsf{C}}{ ~~o f~~}\\mathsf{C}\\in\\mathcal{S}\_{\\mathsf{C}}\
$$\
\
$$\
\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
U\_{\\mathsf{C}}\
$$\
\
$$\
(\\mathsf{C})\
$$\
\
$$\
\\mathfrak{G}\_{\\sigma}(\*)\\text{-}o r b i t\
$$\
\
From the above proposition we conclude that B (⁄) is a Hilbert manifold\
while B is smooth away from the reducible orbits.\
\
$$\
\\mathcal{B}\_{\\sigma}(\*)\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
A _three-dimensional monopole_ is a conflguration C = _(ˆ; A) 2_ C satisfying the Seiberg-Witten equations\
‰\
\
$$\
\\mathsf{C}=\\left(\\psi,A\\right)\\in\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
\\left{\\begin{array}{r c l}{\\mathfrak{D} _{A}\\psi}&{=}&{0}\ {\\frac{1}{2}q(\\psi)}&{=}&{\\mathbf{c}(\*F_{A})}\ \\end{array}\\right..\
$$\
\
Denote by Z _‰_ C the set of three-dimensional monopoles. Exactly as\
in the four-dimensional case we conclude that each three-monopole is Gequivalent to a smooth one and M := Z _=G_ is a compact subset of B.\
\
$$\
\\tilde{z} _{\\sigma}\\subset\\mathfrak{C}_{\\sigma}\
$$\
\
$$\
\\mathcal{G}\_{\\sigma^{-}}\
$$\
\
$$\
\\mathfrak{M} _{\\sigma}:=\\mathcal{Z}_{\\sigma}/\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
**Remark 4.2.4.** Arguing exactly as in the proof of Lemma 2.2.3 one can\
prove that if _(ˆ; A)_ is a 3-monopole then\
\
$$\
\\left(\\psi,A\\right)\
$$\
\
$$\
\\operatorname\*{s u p} _{x\\in N}\|\\psi(x)\|^{2}\\leq2\\operatorname\*{s u p}_{x\\in N}\|s(x)\|\
$$\
\
where _s_ is the scalar curvature of _N._ We have already used this fact in the\
proof of the Thom conjecture in x2.4.2.\
\
* * *\
\
To describe the local structure of M we need to linearize the Seiberg-\
Witten equations along a slice. The monopoles are zeros of the smooth\
map\
SW : C _»_\
! C1 = T C; (ˆ; A) 7! (D6 ˆ; q(ˆ) ¡ c(⁄FA)\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
S W:\\mathbb{C} _{\\sigma}\\longrightarrow\\mathbb{C}_{\\sigma}^{1}\\cong T\_{\\mathsf{C}}\\mathbb{C} _{\\sigma},(\\psi,A)\\mapsto(\\mathbb{D}_{A}\\psi,q(\\psi)-\\mathbf{c}(\*F\_{A})\
$$\
\
As explained in x2.4.1, the map _SW_ is the formal (i.e. _L2_) gradient of the\
energy functional\
_E_ : _C! R;_\
\
$$\
\\left\|L^{2}\\right)\
$$\
\
$$\
\\mathcal{E} _{\\sigma}:\\mathcal{C}_{\\underline{{\\sigma}}}\\to\\mathbb{R},\
$$\
\
$$\
\\mathcal{E} _{\\sigma}(\\psi,A)=\\frac{1}{2}\\int_{N}(A-A\_{0})\\wedge(F\_{A}+F\_{A\_{0}})+\\frac{1}{2}\\int\_{N}\\langle\\mathfrak{D} _{A}\\psi,\\psi\\rangle d v_{g}\
$$\
\
where _A0_ is a flxed, smooth reference Hermitian connection on det(). Since\
\
$$\
A\_{0}\
$$\
\
$$\
\\frac{d}{dt}\\left\| _{t=0}\\right.\\mathcal{E}_{\\sigma}(e^{t\\mathbf{i}f}\\cdot\\mathsf{C})=0.\
$$\
\
we deduce\
\
$$\
D\_{\\mathsf{C}}\\mathcal{E} _{\\sigma}(\\mathfrak{L}_{\\mathsf{C}}\\mathbf{i}f)=0\\Longleftrightarrow\\Big\\langle S W(\\mathsf{C}),\\mathfrak{L} _{\\mathsf{C}}(\\mathbf{i}f)\\Big\\rangle_{L^{2}}=0,\\quad\\forall\\mathbf{i}f\\in T\_{\\mathbf{1}}\\mathfrak{G}\_{\\sigma}\
$$\
\
so that\
\
$$\
SW(C)\\in\\mathcal{S} _{C}^{1},\\quad\\forall C\\in\\mathcal{C}_{\\sigma}.\
$$\
\
Observe also that for every _2_ G we have\
\
$$\
\\gamma\\in\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
SW(\\gamma\\cdot(\\psi,A))=(\\gamma\\mathfrak{D}\_A\\psi,q(\\psi)-\\mathbf{c}(\*F\_A))\
$$\
\
$$\
\|S W(\\gamma\\cdot\\mathsf{C})\| _{L^2}=\|S W(\\mathsf{C})\|_{L^2}.\
$$\
\
so that\
\
Hence C! kSW(C)kL2 is a well deflned continuous function on B which\
we denote by f. We can regard SW(C) as anS1-invariant tangent vector\
fleld on B (⁄) or as a genuine tangent vector fleld on B;irr. ForC\_ 2 TCC\
and **if** _2 T1G_ deflne\
2 3 2 3\
\
$$\
\\mathsf{C}\\to\|SW(\\mathsf{C})\|\_{L^2}\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
$$\
SW(C)\
$$\
\
$$\
S^{1}\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}(\*)\
$$\
\
$$\
\\mathcal{B}\_{\\sigma,irr}\
$$\
\
$$\
\\dot{\\mathsf{C}}\\in T\_{\\mathsf{C}}\\mathfrak{C}\_{\\sigma}\
$$\
\
$$\
\\mathbf{i}f\\in T\_1\\mathbb{G}\_{\\sigma}\
$$\
\
$$\
\\begin{aligned}\\mathfrak{T} _{\\mathsf{C}}\\left\[\\begin{array}{c}\\dot{\\mathsf{C}}\\\mathbf{i}f\\\end{array}\\right\]&=\\left\[\\begin{array}{cc}\\underline{SW}&-\\frac{1}{2}\\mathfrak{L}_{\\mathsf{C}}\\&\\-\\frac{1}{2}\\mathfrak{L} _{\\mathsf{C}}^\*&0\\\end{array}\\right\]\\left\[\\begin{array}{c}\\dot{\\mathsf{C}}\\\\\mathbf{i}f\\\end{array}\\right\]\\\mathsf{t}=\\left\[\\begin{array}{c}\\frac{d}{dt}\\left\|_{t=0}\\right.SW(\\mathsf{C}+t\\dot{\\mathsf{C}})-\\frac{1}{2}\\mathfrak{L} _{\\mathsf{C}}(\\mathbf{i}f)\\\-\\frac{1}{2}\\mathfrak{L}_{\\mathsf{C}}^\*\\dot{\\mathsf{C}}\\\end{array}\\right\]&\\in\\overline{T\_{\\mathsf{C}}\\mathfrak{C}\_{\\sigma}}^{L^2}\\oplus L^2(N,\\mathbf{i}\\mathbb{R}).\\end{aligned}\
$$\
\
More explicitly, if C := ( _ˆ; A_\
2 3 2\
\
) and C\_ _=(ˆ;_\_ **i**\
3 2\
\
_a_\_) then\
3\
\
$$\
\\dot{\\mathsf{C}}=\\left(\\dot{\\psi},\\dot{\\mathbf{i}}\\dot{a}\\right)\
$$\
\
$$\
\\mathsf{C}:=(\\psi,A)\
$$\
\
(4.2.2)\
\
$$\
\\begin{aligned}{\\mathcal{T} _{\\mathsf{C}}\\left\[\\begin{array}{c}{\\dot{\\psi}}\ {\\mathbf{i}\\dot{a}}\ {\\mathbf{i}f}\ \\end{array}\\right\]=\\left\[\\begin{array}{c c c}{\\mathfrak{D}_{A}}&{0}&{0}\ {0}&{- _d}&{d}\ {0}&{d^{_}}&{0}\ \\end{array}\\right\]\\cdot\\left\[\\begin{array}{c}{\\dot{\\psi}}\ {\\mathbf{i}\\dot{a}}\ {\\mathbf{i}f}\ \\end{array}\\right\]+\\left\[\\begin{array}{c}{\\frac{1}{2}\\mathbf{c}(\\mathbf{i}\\dot{a})\\psi-\\frac{\\mathbf{i}}{2}f\\psi}\ {\\frac{1}{2}\\dot{q}(\\psi,\\psi)}\ {\\frac{\\mathbf{i}}{2}\\mathfrak{I m}\\left\\langle\\psi,\\dot{\\psi}\\right\\rangle}\ \\end{array}\\right\].}\ \\end{aligned}\
$$\
\
Denote by TC0 the flrst operator on the right-hand side of (4.2.2) and set\
PC:= TC ¡TC0. Notice that PC is a zeroth order operator while TC is a flrst\
order, formally selfadjoint elliptic operator.\
\
$$\
\\mathbb{T}\_{\\mathsf{C}}^{0}\
$$\
\
$$\
\\mathcal{P} _{\\mathsf{C}}:=\\mathcal{T}_{\\mathsf{C}}-\\mathcal{T}\_{\\mathsf{C}}^{\\widetilde{0}}\
$$\
\
$$\
\\mathcal{P}\_{\\mathsf{C}}\
$$\
\
* * *\
\
**Exercise 4.2.1.** Prove directly that TC is formally selfadjoint.\
\
$$\
\\mathfrak{T}\_{\\mathsf{C}}\
$$\
\
Suppose C0 is a 3-monopole. To understand the local structure of M\
near C0 it su–ces to understand the structure of the critical set of the\
restriction of E to a small neighborhood U of C0 2 SC0. For every C 2 C\
we denote by ƒC the L2-orthogonal projection\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
\\mathcal{E}\_{\\sigma}\
$$\
\
$$\
\\Pi\_{\\mathsf{C}}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
\\mathsf{C} _{0}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\mathsf{C}\\in\\mathcal{C}\_{\\sigma}\
$$\
\
$$\
T\_{\\mathbb{C}}\\mathcal{C} _{\\sigma}^{0}\\to\\mathcal{S}_{\\mathbb{C}\_{0}}^{0}.\
$$\
\
Since TCC0\
instead of ƒC.\
\
is independent of C, _T_\
\
» ⁄\
CC0 = L2(S' iT N), we can write ƒ\
\
$$\
T\_{\\mathsf{C}}\\mathcal{C}\_{\\sigma}^{0}\
$$\
\
$$\
\\mathbb{C},T\_{\\mathbb{C}}\\mathbb{C}\_{\\sigma}^{0}\\cong L^{2}(\\mathbb{S}\\oplus\\mathbf{i}T^{\*}N)\
$$\
\
$$\
\\Pi\_{\\complement}\
$$\
\
$$\
\\Pi T\_{\\mathsf{C}}\\mathcal{C} _{\\sigma}^{r}\\subset\\mathcal{S}_{\\mathsf{C}\_{0}}^{r},\\forall r\\geq0.\
$$\
\
**Exercise 4.2.2.**\
\
Show that ƒTCCr\
\
‰SCr0, 8r ‚ 0.\
\
Lemma 4.2.5. There exist a Stab (C0)-invariant neighborhood U = UC0of\
C0 2 S0C and a constant ‚>0 such that\
\
$$\
\\left(\\mathsf{C}\_{0}\\right)\
$$\
\
$$\
U=U\_{\\mathsf{C}\_0}\
$$\
\
$$\
\\mathsf{C} _{0}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\lambda>0\
$$\
\
$$\
\\frac{1}{\\lambda}\|S W(\\mathsf{C})\| _{L^{2}}\\leq\|\\Pi S W(\\mathsf{C})\|_{L^{2}}\\leq\\lambda\|S W(\\mathsf{C})\|\_{L^{2}},\\quad\\forall\\mathsf{C}\\in U.\
$$\
\
It is worth emphasizing the main point of the above result. Roughly\
speaking, it says that, for C su–ciently close to C0, the component of SW(C)\
orthogonal to SC0is small compared to the component along SC0. In particular, if C 2 S0C is close to C0 then SW(C) vanishes if and only if its\
component along SC0vanishes.\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
SW(C)\
$$\
\
$$\
\\mathcal{S}\_{\\mathsf{C}\_0}\
$$\
\
$$\
\\mathcal{S}\_{\\mathsf{C}\_0}\
$$\
\
$$\
\\mathsf{C}\\in\\mathcal{S}\_{\\mathsf{C}\_0}\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
SW(C)\
$$\
\
$$\
\\mathcal{S}\_{\\mathsf{C}\_0}\
$$\
\
**Proof** Observe that we always have\
\
$$\
\|\\Pi S W(\\mathsf{C})\| _{L^{2}}\\leq\|S W(\\mathsf{C})\|_{L^{2}}\
$$\
\
so it su–ces to flnd a neighborhood\
\
U of C0 2 S0C and ‚>1 such that\
\
$$\
\\mathsf{C} _{0}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\lambda>1\
$$\
\
$$\
\|S W(\\mathsf{C})\| _{L^{2}}\\leq\\lambda\|\\Pi S W(\\mathsf{C})\|_{L^{2}},\\quad\\forall\\mathsf{C}\\in U.\
$$\
\
We will prove a slightly more general result.\
that there exists a neighborhood _U_\
any “ 2 SC we have the equality\
\
of C0 2 S0C\
\
More precisely, we will show\
such that for any C _2 U_ and\
\
$$\
\\mathsf{C} _{0}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\mathsf{C}\\in U\
$$\
\
$$\
\\Psi\\in\\mathcal{S}\_{\\mathsf{C}}\
$$\
\
$$\
\|\\Psi\| _{L^{2}}\\leq\\lambda\|\\Pi\\Psi\|_{L^{2}}.\
$$\
\
Lemma 4.2.5 follows by setting “ := SW(C) in the above inequality.\
\
$$\
\\Psi:=S W(\\mathsf{C})\
$$\
\
We argue by contradiction. Suppose there exist sequences Cn 2 S0C and\
“n 2 SCnsuch that\
1\
\
$$\
\\mathsf{C} _{n}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\Psi\_{n}\\in\\mathcal{S} _{\\mathsf{C}_{n}}\
$$\
\
$$\
\\mathsf{C} _{n}\\xrightarrow{L^{2,2}}\\mathsf{C}_{0},\ \|\\Psi\_{n}\| _{L^{2}}=1,\ \|\\Pi\\Psi_{m}\|\_{L^{2}}<\\frac{1}{n}.\
$$\
\
Set ¤n:= ƒ“n and ¥n:= (1 ¡ ƒ)“\
\
n. Then\
‡\
1\
\
$$\
\\Upsilon\_{n}:=\\Pi\\Psi\_{n}\
$$\
\
$$\
\\Xi\_{n}:=(1-\\Pi)\\Psi\_{n}\
$$\
\
(4.2.3)\
\
$$\
1\\geq\|\\Xi\_{n}\|>\\Big(1-\\frac{1}{n}\\Big).\
$$\
\
* * *\
\
^? »\
Now observe that ¥n? S0C so there exists a unique ifn 2 (ker LC0) =\
?\
(T1Stab(C0)) _‰ T1G_ such that\
\
$$\
\\hat{\\Xi} _{n}\\perp\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\mathbf{i}f\_n\\in(\\ker\\mathfrak{L}\_{\\mathsf{C}\_0})^{\\perp}\\cong\
$$\
\
$$\
(T\_{1}\\mathbf{Stab}(\\mathbf{C} _{0}))^{\\perp}\\subset T_{1}\\mathbb{G}\_{\\sigma}\
$$\
\
$$\
\\mathfrak{L} _{\\mathsf{C}_{0}}(\\mathbf{i}f\_{n})=\\hat{\\Xi}\_{n},\
$$\
\
$$\
\\mathfrak{L}\_{\\mathsf{C} _n}(\\mathbf{i}f)=\\mathfrak{L}_{\\mathsf{C}\_0}+\\mathfrak{R}\_n\
$$\
\
where Rn is a zeroth order p.d.o. (bundle morphism) such that kRnk2;2 =\
o(1) as _n ! 1._ The condition\
\
$$\
R\_{n}\
$$\
\
$$\
\|\\bar{R} _n\|_{2,2}=\
n\\to\\infty\
$$\
\
$$\
\\mathfrak{L}\_{\\mathsf{C}\_n}^\*\\psi\_n=0\
$$\
\
$$\
o(1)\
$$\
\
can be rewritten as\
\
$$\
0=\\big(\\mathfrak{L} _{\\mathsf{C}_{0}}^{ _}+R\_{n}^{_}\\big)\\big(\\Upsilon\_{n}+\\Xi\_{n}\\big)=\\mathfrak{L} _{\\mathsf{C}_{0}}^{ _}\\Xi\_{n}+R\_{n}^{_}\\Xi\_{n}=\\mathfrak{L} _{\\mathsf{C}_{0}}^{ _}\\mathfrak{L}{\\mathsf{C}{0}}\\big(\\mathbf{i}f\_{n}\\big)+R\_{n}^{_}\\Xi\_{n}.\
$$\
\
⁄\
Thus ifn? ker LC0LC0 and\
\
$$\
\\mathbf{i}f\_{n}\\perp\
$$\
\
$$\
\\mathfrak{L} _{\\mathsf{C}_{0}}^{\*}\\mathfrak{L} _{\\mathsf{C}_{0}}\
$$\
\
$$\
\|\\mathfrak{L} _{\\mathsf{C}_{0}}^{ _}\\mathfrak{L}{\\mathsf{C}{0}}(\\mathbf{i}f\_{n})\|{L^{p}}=\|R{n}^{_}\\Xi\_{n}\|\_{L^{p}},\\forall p\\in(1,\\infty).\
$$\
\
Using the Sobolev inequalities we deduce that there exists _C_ >0 such that\
\
$$\
\|R\_{n}\| _{L^{\\infty}}\\leq C\|R_{n}\|\_{2,2}.\
$$\
\
Hence there exists _C_ >0 such that\
\
$$\
C>0\
$$\
\
$$\
\|R\_{n}^{\*}\\Xi\_{n}\| _{L^{2}}\\leq C_{q}\|R\_{n}\| _{2,2}\|\\Xi_{n}\|\_{L^{2}},\\quad\\forall n.\
$$\
\
Using the elliptic estimate of Theorem 1.2.18 (v) for the generalized Lapla-\
⁄\
cian LC0LC0 we deduce that there exists a constant C>1 such that\
\
$$\
\\mathfrak{L} _{\\mathsf{C}_{0}}^{\*}\\mathfrak{L} _{\\mathsf{C}_{0}}\
$$\
\
$$\
C>1\
$$\
\
$$\
\|f\_{n}\| _{2,2}\\leq C\|R_{n}\\Xi\_{n}\|\_{L^{2}}=o(1)\\quad\\mathrm{as}\\quad n\\to\\infty.\
$$\
\
This implies fn! 0 inL2;2 and since LC0(ifn) = ¥n we deduce ¥n! 0 in\
_L2._ This contradicts the inequality (4.2.3). Lemma 4.2.5 is proved. ¥\
\
$$\
f\_{n}\\rightarrow0\
$$\
\
$$\
L^{2,2}\
$$\
\
$$\
\\mathfrak{L} _{\\mathsf{C}_{0}}(\\mathbf{i}f\_{n})=\\Xi\_{n}\
$$\
\
$$\
\\Xi\_{n}\\rightarrow0\
$$\
\
$$\
L^{2}\
$$\
\
Fix a neighborhood U of C0 2 S0C as in the above lemma. The critical\
points of E jU are determined from the equation\
\
$$\
\\mathsf{C} _{0}\\in\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\mathcal{E} _{\\sigma}\\left\|_{U}\\right.\
\\Pi S W(\\mathsf{C})=0,\\quad\\mathsf{C}\\in U.\
$$\
\
Equivalently, this means there exists a unique **if** _2 T1G_ such that\
\
$$\
\\mathbf{i}f\\in T\_1\\mathbb{G}\_{\\sigma}\
$$\
\
$$\
\\mathbf{i}f\\perp\\ker\\mathfrak{L} _{\\mathsf{C}_{0}},\\quad{S W}(\\mathsf{C})+\\mathfrak{L} _{\\mathsf{C}_{0}}(\\mathbf{i}f)=0.\
$$\
\
Thus, the problem of understanding the structure of M near C0 boils down\
to understanding the local structure of the equation\
\
(4.2.4)\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
SW(C\_{0}+\\dot{C})=0\
$$\
\
$$\
\\mathfrak{L}\_{\\mathsf{C}\_0}^\*\\dot{\\mathsf{C}}=0\
$$\
\
⁄\
where LC0C\_ = 0 and kC\_k2;2\
\
is very small.\
\
$$\
\|\\dot{\\mathsf{C}}\|\_{2,2}\
$$\
\
Set\
\
$$\
H\_{\\mathsf{C} _{0}}^{0}:=\\ker\\mathfrak{L}_{\\mathsf{C} _{0}},\\quad H_{\\mathsf{C} _{0}}^{1}:=\\left{\\dot{\\mathsf{C}}\\in\\mathfrak{C}_{\\mathsf{C}};\\quad\\underline{{{S W}}}(\\dot{\\mathsf{C}})=0,\\quad\\mathfrak{L} _{\\mathsf{C}_{0}}^{\*}\\dot{\\mathsf{C}}=0\\right}\
$$ and denote by ƒ1 : SC0! H1C the L2-orthogonal projection. Observe that\
0\
\
$$\
\\Pi\_{1}:\\mathcal{S} _{\\mathsf{C}_{0}}\\xrightarrow{}H\_{\\mathsf{C}\_{0}}^{1}\
$$\
\
$$\
L^{2}\
$$\
\
$$\
\\ker\\mathfrak{T} _{\\mathsf{C}_{0}}=H\_{\\mathsf{C} _{0}}^{1}\\oplus H_{\\mathsf{C}\_{0}}^{0}.\
$$\
\
For every _r_ >0 we set\
\
$$\
r>0\
$$\
\
$$\
B\_{\\mathsf{C}}(r):={\\dot{\\mathsf{C}}\\in H\_{\\mathsf{C}}^{1};\\quad\|\\dot{\\mathsf{C}}\|\_{L^{2}}<r}.\
$$\
\
The equation (4.2.4) is equivalent to the pair of equations\
‡ ·\
\
( _y_") (1\
\
$$\
(1-\\Pi\_{1})\\Big(S W(\\mathsf{C} _{0}+\\dot{\\mathsf{C}})\\Big)=0,\\quad\\dot{\\mathsf{C}}\\in\\mathcal{S}_{\\mathsf{C} _{0}},\\quad\|\\dot{\\mathsf{C}}\|_{2,2}\\leq\\varepsilon,\
$$\
\
$$\
\\Pi\_{1}\\Big(S W(\\mathsf{C} _{0}+\\dot{\\mathsf{C}})\\Big)=0,\\quad\\dot{\\mathsf{C}}\\in\\mathcal{S}_{\\mathsf{C} _{0}},\\quad\|\\dot{\\mathsf{C}}\|_{2,2}\\leq\\varepsilon.\
$$\
\
( _yy_") ƒ\
\
The local structure of ( _y_") can be easily analyzed using the implicit\
function theorem. Our next result states that the solution set of ( _y_") can be\
represented as the graph of a **Stab(C0**)-equivariant map\
\
$$\
(\\dagger\_{\\varepsilon})\
$$\
\
$$\
(\\dagger\_{\\varepsilon})\
$$\
\
$$\
\\mathbf{.S t a b}(\\mathsf{{C}}\_{0})\
$$\
\
$$\
\\Phi\_{1}:H\_{\\mathsf{C} _{0}}^{1}\\to\\ker\\Pi_{1}\
$$\
\
tangent to H1C at 0.\
0\
\
$$\
H^{1} _{\\mathsf{C}_{0}}\
$$\
\
**Proposition 4.2.6.** _Suppose_ C0 _is a smooth_ 3- _monopole. There exist r0_ =\
r0(C0) \> _0, "_ = "(C0), _”_ = ”(C0) \> 0 _and a smooth_ **Stab(C**)- _equivariant_\
_map_\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
r\_{0}=\
r\_{0}(\\mathsf{C} _{0}):>:0,;\\varepsilon:=:\\varepsilon(\\mathsf{C}_{0}),;\\nu:=:\\nu(\\mathsf{C}\_{0}):>:0\
$$\
\
$$\
\\Phi\_{1}:B\_{\\mathrm{C} _{0}}(r_{0})\\rightarrow\\ker(1-\\Pi\_{1})\\mathcal{S} _{\\mathrm{C}_{0}}\
$$\
\
_satisfying the following requirements._\
\
(i)'1(0) = _0._\
\
$$\
\\Phi\_{1}(0)=0.\
$$\
\
_(ii) Any solution_\
\
C\_ 0 of (y") decomposes as\
\
$$\
\\dot{\\mathsf{C}}'\
$$\
\
$$\
(\\dagger\_{\\varepsilon})\
$$\
\
$$\
\\dot{\\mathsf{C}}'=\\dot{\\mathsf{C}}\\oplus\\Phi\_1(\\dot{\\mathsf{C}})\
$$\
\
_where_ C\_ = ƒ1\
\
C\_ 0 2 BC0(r0). In particular,\
‡\
¡\
\
$$\
\\dot{\\mathsf{C}}=\\Pi\_{1}\\dot{\\mathsf{C}}^{\\prime}\\in B\_{\\mathsf{C} _{0}}(r_{0})\
$$\
\
$$\
(\\mathbf{1}-\\Pi\_{1})\\Big(\\mathop{{S W}}\\bigl(\\mathop{}\\mathsf{C}+\\dot{\\mathsf{C}}+\\Phi\_{1}(\\dot{\\mathsf{C}})\\mathop{})+\\mathfrak{L} _{\\mathsf{C}}\\Phi_{0}(\\dot{\\mathsf{C}})\\Big)=0,\
$$\
\
$$\
\\forall\\dot{\\mathsf{C}}\\in B\_{\\mathsf{C}}(r).\
$$\
\
(iii) k'1(C\_)k2;2 • ”kC\_ k2, kD'1(v)k2;2 • Ckvk¢kC\_ k, 8 v;C\_ 2 H1C0. (H1C\
C\_ 0\
_is a flnite-dimensional space and thus all norms on it are equivalent.)_\
\
$$\
\|\\Phi\_{1}(\\dot{\\mathsf{C}})\| _{2,2}\\leq\\nu\|\\dot{\\mathsf{C}}\|^{2},\|D_{\\dot{\\mathsf{C}}}\\Phi\_{1}(v)\| _{2,2}\\leq C\|v\|\\cdot\|\\dot{\\mathsf{C}}\|,\\forall v,\\dot{\\mathsf{C}}\\in H_{\\mathsf{C} _{0}}^{1}.\\quad(H_{\\mathsf{C}\_{0}}^{1}\
$$\
\
The proof is a consequence of the implicit function theorem applied to\
the nonlinear equation\
F(C\_)=0\
\
$$\
F(\\dot{\\complement})=0\
$$\
\
where _F_ is the **Stab(C0**)-equivariant map\
\
$$\
\\left(\\mathsf{C}\_{0}\\right)\
$$\
\
$$\
F:\\mathcal{S} _{\\mathsf{C}_{0}}\\to(1-\\Pi\_{1})\\mathcal{S} _{\\mathsf{C}_{0}}^{1},\\quad\\dot{\\mathsf{C}}\\mapsto(1-\\Pi\_{1})\\Pi{S W}(\\mathsf{C}\_{0}+\\dot{\\mathsf{C}}).\
$$\
\
* * *\
\
The linearization of this map at C\_ = 0 is (1 ¡ ƒ1)SWC0, which is onto and\
has kernel H1C0.\
\
$$\
\\dot{\\mathsf{C}}=0is(1-\\Pi\_1)\\underline{SW}\_{\\mathsf{C}\_0}\
$$\
\
$$\
H^{1} _{\\mathsf{C}_{0}}\
$$\
\
Set\
\
$$\
Q\_{\\mathsf{C} _{0}}:B_{\\mathsf{C} _{0}}(r_{0})\\to H\_{\\mathsf{C} _{0}}^{1},\\quad\\dot{\\mathsf{C}}\\mapsto\\Pi_{1}S W(\\mathsf{C} _{0}+\\dot{\\mathsf{C}}+\\Phi_{1}(\\dot{\\mathsf{C}})).\
$$\
\
QC0is called the Kuranishi map at C0\
and the above discussion shows that _Q_\
neighborhood of C0 in M.\
\
. ItisaStab(C0)-equivariant map\
¡\
C01=Stab(C0) is homeomorphic to a\
\
$$\
\\mathsf{C}\_{0}.\
$$\
\
$$\
Q\_{\\mathsf{C}\_0}\
$$\
\
$$\
\\mathrm{Stab}(\\mathrm{C}\_0)\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
Q\_{\\mathsf{C} _{0}}^{-1}/\\mathbf{Stab}(\\mathsf{C}_{0})\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
**Deflnition 4.2.7.** A 3-monopole C0\
\
is called regular if QC0· 0.\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
Q\_{C\_{0}}\\equiv0.\
$$\
\
Example 4.2.8. Suppose C0 = (“0; A0\
i.e. _ˆ0 ·_ 0\. Then\
n\
\
) _isasmooth_ reducible 3-monopole,\
o\
\
$$\
\\mathsf{C} _{0}=\\left(\\Psi_{0},A\_{0}\\right)\
$$\
\
$$\
\\psi\_{0}\\equiv0\
$$\
\
$$\
\\mathcal{S} _{\\mathsf{C}_{0}}=\\left{\\dot{\\phi}\\oplus\\mathbf{i}\\dot{b}\\in L^{2,2}(\\mathbb{S}\_{\\sigma}\\oplus\\mathbf{i}T^{ _}N);\\quad d^{_}\\dot{b}=0\\right}\
$$\
\
and\
\
$$\
\\mathrm{T}\_{\\mathrm{C} _0}=\\mathrm{T}_{\\mathrm{C} _0}^0=\\mathrm{D}_{\\mathrm{A}\_0}\\oplus\\mathrm{SIGN}.\
$$\
\
Thus\
\
$$\
H\_{\\mathsf{C} _{0}}^{1}\\cong\\ker\\mathfrak{D}_{A\_{0}}\\oplus\\mathbf{i H^{1}}(N,g),\\quad H\_{\\mathsf{C}\_{0}}^{0}\\cong\\mathbf{iH}^{0}(N,g)\\cong\\mathbf{i}\\mathbb{R}.\
$$\
\
Fix (ˆ;\_ ia\_) 2 BC0(r0). Then (\`;\_ ib\_):= '1\
tion\
\_ \_)\
\
( _ˆ;_\_ **ia**\_) is the solution of the equa-\
\
$$\
(\\dot{\\psi},\\mathbf{i}\\dot{a})\\in B\_{\\mathsf{C} _{0}}(r_{0})\
$$\
\
$$\
(\\dot{\\phi},\\mathbf{i}\\dot{b}):=\\Phi\_{1}(\\dot{\\psi},\\mathbf{i}\\dot{a})\
$$\
\
$$\
\\begin{array}{c}{(\\dot{\\phi},\\mathbf{i}\\dot{b})\\in(1-\\Pi\_{1})\\mathcal{S} _{\\mathsf{C}_{0}},}\ {(1-\\Pi\_{1})\\Big(\\mathfrak{D} _{A_{0}+\\mathbf{i}\\dot{a}+\\mathbf{i}\\dot{b}}(\\dot{\\psi}+\\dot{\\phi}),\*F\_{A\_{0}+\\mathbf{i}\\dot{a}+\\mathbf{i}\\dot{b}}-\\frac{1}{2}q(\\dot{\\psi}+\\dot{\\phi})\\Big)=0}\ \\end{array}\
$$\
\
or equivalently,\
\
(4.2.5)\
\
$$\
\\begin{align\*}(1-\\Pi\_1')\\Big(\\mathfrak{D}\_{A\_0+\\mathbf{i}\\dot{a}+\\mathbf{i}\\dot{b}}\\dot{\\phi}+\\frac{1}{2}\\mathbf{c}(\\mathbf{i}\\dot{a}+\\mathbf{i}\\dot{b})\\dot{\\psi})\\Big)=0,\\(1-\\Pi\_1'')\\Big(\\mathbf{i} _d\\dot{b}-\\frac{1}{2}q(\\dot{\\psi}+\\dot{\\phi})\\Big)=0.\\end{align_}\
$$\
\
where ƒ10 denotes the orthogonal projection onto ker DA0and ƒ100 denotes\
the orthogonal projection onto H1(N; g).\
\
$$\
\\Pi\_{1}^{\\prime}\
$$\
\
$$\
\\mathfrak{D} _{A_{0}}\
$$\
\
$$\
\\Pi\_{1}^{\\prime\\prime}\
$$\
\
$$\
\\mathbf{H}^{1}(N,g)\
$$\
\
Suppose now that ker DA0= 0. Then ƒ1\
equivalent to\
\
0 · 0, ˆ\_ · 0 and thus (4.2.5) is\
‡ ·\
\
$$\
\\Pi\_{1}^{\\prime}\\equiv0,\\dot{\\psi}\\equiv0\
$$\
\
$$\
\\mathfrak{D} _{A_{0}}=0\
$$\
\
$$\
\\mathfrak{D} _{A_{0}+\\mathbf{i}\\dot{a}+\\mathbf{i}\\dot{b}}\\dot{\\phi}=0,\\quad(1-\\Pi\_{1}^{\\prime\\prime})\\Big(\\mathbf{i}\*d\\dot{b}-q(\\dot{\\phi})\\Big)=0.\
$$\
\
(4.2.6)\
\
The map '1 of Proposition 4.2.6 is described by a pair of maps on\
\
$$\
\\Phi\_{1}\
$$\
\
$$\
\\dot{b}=\\dot{b}(\\dot{a}),\\quad\\dot{\\phi}=\\dot{\\phi}(\\dot{a}),\\quad\\dot{a}\\in\\mathbf{H}^{1}(N,g),\\quad\|\\dot{a}\| _{L^{2}}\\leq r_{0},\\quad\|b\| _{2,2}\\leq\\nu\|a\|_{2}^{2}.\
$$\
\
By making r0 even smaller we can assume DA _(is invertible, being_\
_0+ia +ib a)_\
_very close to the invertible operator DA0. This shows that \`_ · 0 and the\
second equation of (4.2.6) implies _b_\_ _·_ 0\. Thus '1 _·_ 0.\
\
$$\
\\mathfrak{D} _{A_{0}+\\mathrm{i}\\dot{a}+\\mathrm{i}\\dot{b}(\\dot{a})}\
$$\
\
$$\
r\_{0}\
$$\
\
$$\
\\mathfrak{D} _{A_{0}}\
$$\
\
$$\
\\dot{\\phi}\\equiv0\
$$\
\
$$\
\\dot{b}\\equiv0\
$$\
\
$$\
\\Phi\_{1}\\equiv0\
$$\
\
* * *\
\
To compute the Kuranishi map at C0 we need to compute\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
\\Pi\_{1}^{\\prime\\prime}(\*F\_{A\_{0}+\\mathbf{i}\\dot{a}}),\\quad\\dot{a}\\in\\mathbf{H}^{1}(N,g).\
$$\
\
Now observe that since C0 is reducible we have _FA0_ = 0\. _Thus⁄FA0_ +i _a_ _=_\
_**i⁄**da_, which clearly has trivial projection on the space of harmonic 1-forms.\
We have thus shown that if _A0_ is a at connection on det() such that\
ker DA0= 0 then (0; A0) is a regular, reducible monopole.\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
F\_{A\_{0}}=0\
$$\
\
$$\
\\mathbf{i}\*d\\dot{a}\
$$\
\
$$\
\*F\_{A\_{0}+\\mathbf{i}\\dot{a}}=\
A\_{0}\
$$\
\
$$\
\\mathfrak{D} _{A_{0}}=0\
$$\
\
$$\
(0,A\_{0})\
$$\
\
The stabilizer of C0 is S1 which acts trivially on H1C = iH1(N; g) so\
0\
that there exists an open neighborhood of C0 in M homeomorphic to an\
1(N)\
open ball in Rb and consisting only of reducible monopoles.\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
S^{1}\
$$\
\
$$\
H\_{C\_0}^1=\\mathrm{i}H^1(N,g)\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
\\mathbb{R}^{b\_{1}(N)}\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
### Deflnition 4.2.9.\
\
### A pair\
\
$$\
(\\sigma , g) = \\left(s p i n ^ {c} \\mathrm {s t r u c t u r e o n} N, \\mathrm {R i e m a n n i a n m e tric o n} N\\right)\
$$\
\
is called _good_ if all irreducible _(; g)_-monopoles are regular and for any at\
connection A on det() the operator DA is invertible.\
\
$$\
(\\sigma,g)\
$$\
\
$$\
\\mathfrak{D}\_{A}\
$$\
\
The discussion in the above example has the following consequence.\
\
**Proposition 4.2.10.** _If g is a positive scalar curvature metric on N then_\
(; g) is good for every 2 Spinc(N). Moreover, M is either empty or it\
_is a compact smooth manifold difieomorphic to a b1(N_)- _dimensional torus_\
_consisting only of regular reducible monopoles._\
\
$$\
(\\sigma,g)\
$$\
\
$$\
\\sigma\\in S p i n^{c}(N)\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
b\_{1}(N)\
$$\
\
**Remark 4.2.11.** Suppose _(; g)_ is a good pair and C0\
»\
smooth monopole. If C0 is reducible then H1C = H\
0\
of Stab (C0) onH1C is trivial. This proves that TCM\
0\
\
= _(ˆ0; A0)_ isa\
1(N;R) and the action\
»\
= HC1, 8C 2 M.\
\
$$\
\\mathsf{C} _{0};=;(\\psi_{0},A\_{0})\
$$\
\
$$\
(\\sigma,g)\
$$\
\
$$\
\\mathsf{C}\_{0}\
$$\
\
$$\
H\_{\\mathsf{C}\_{0}}^{1}\\cong H^{1}(N,\\mathbb{R})\
$$\
\
$$\
\\left(\\mathsf{C}\_{0}\\right)\
$$\
\
$$\
H^{1} _{\\mathsf{C}_{0}}\
$$\
\
$$\
T\_{\\mathsf{C}}\\mathfrak{M} _{\\sigma}\\cong H_{\\mathsf{C}}^{1},\\forall\\mathsf{C}\\in\\mathfrak{M}\_{\\sigma}\
$$\
\
For each smooth monopole C and 0 < _•¿_ 1 we deflne the _Kuranishi_\
_neighborhood_ of C\
\
$$\
0<\\kappa\\ll1\
$$\
\
$$\
U\_{\\mathsf{C}}(\\kappa):={\\dot{\\mathsf{C}}\\in\\mathcal{S} _{\\mathsf{C}};\\quad\|\\dot{\\mathsf{C}}\|_{2,2}<\\operatorname\*{m i n}(\\kappa,\\varepsilon(\\mathsf{C}))}\
$$\
\
where "(C) is determined as in Proposition 4.2.6. After we factor out the\
action of **Stab(C**) it determines an open neighborhood of C in B.\
\
$$\
\\varepsilon(\\mathsf{C})\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
**A word about notation** _When no serious confusion is possible, we will_\
continue to denote by UC0(•) the neighborhood of \[C0\] in B determined by\
UC0‰ SC0. For example, the statement C 2 UC0(•) means C ¡C0 2 S0C and\
kC ¡ C0k2;2 <•while the statement \[C\] 2 UC0provides information only\
_about the gauge equivalence class of_ C _and not_ C _itself._\
\
$$\
U\_{\\mathsf{C}\_{0}}(\\kappa)\
$$\
\
$$\
U\_{\\mathsf{C} _{0}}\\subset\\mathcal{S}_{\\mathsf{C}\_{0}}\
$$\
\
$$\
\\left\[\\mathsf{C}\_{0}\\right\]\
$$\
\
$$\
\\mathsf{C}\\in U\_{\\mathsf{C}\_0}(\\kappa)\
$$\
\
$$\
\|\\mathsf{C}-\\mathsf{C} _0\|_{2,2}<\\kappa\
$$\
\
$$\
\\mathsf{C}-\\mathsf{C} _0\\in\\mathcal{S}_{\\mathsf{C}\_0}\
$$\
\
$$\
\[\\mathsf{C}\]\\in U\_{\\mathsf{C}\_0}\
$$\
\
The family\
\
$$\
\\Big{U\_{\\mathsf{C}}(\\kappa);\[\\mathsf{C}\]\\in\\mathfrak{M}\_{\\sigma}\\Big}\
$$ is then an open cover of the compact subset M _‰_ B. We can extract a\
flnite subcover\
U (•); ¢¢¢; U (•)\
\
$$\
\\mathfrak{M} _{\\sigma}\\subset\\mathcal{B}_{\\sigma}\
$$\
\
$$\
U\_{\\mathsf{C} _{1}}(\\kappa),\\cdots,U_{\\mathsf{C}\_{m}}(\\kappa)\
$$\
\
and we set\
\
$$\
\\kappa\_{0}:=\\min{\\kappa(\\mathsf{C} _{1}),\\cdots,\\kappa(\\mathsf{C}_{m})},\
$$\
\
$$\
U\_{\\kappa}:=\\bigcup\_{i=1}^{m}U\_{\\mathsf{C} _{i}}(\\kappa),\\quad\\forall\\kappa<\\kappa_{0}.\
$$\
\
_U_•is an open neighborhood of M in B\
of M. Observe that for every C _2 U_•\
\
called a _Kuranishi neighborhood_\
\
$$\
U\_{\\kappa}\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
$$\
\\mathfrak{M}\_{\\sigma}\
$$\
\
$$\
\\mathsf{C}\\in U\_{\\kappa}\
$$\
\
$$\
\\operatorname{dist} _{2,2}(\[\\mathsf{C}\],\\mathfrak{M}_{\\sigma})\\leq\\kappa.\
$$\
\
**4.2.3. Asymptotic behavior. Part I.**\
\
Consider a semi-inflnite cylinder\
\
$$\
\\hat{N}:=\\left(\\mathbb{R}\_{+}\\times N,d t^{2}+g\\right)\
$$\
\
and a spinc structure on N. We will denote by ^ the induced cylindrical\
spinc structure on N^. For every smooth conflguration\
\
$$\
\\sigma a s p i n^{c}\
$$\
\
$$\
\\hat{\\sigma}\
$$\
\
$$\
spin^{c}\
$$\
\
$$\
\\hat{N}\
$$\
\
$$\
\\hat{\\mathsf{C}}=\\big(\\hat{\\psi},\\hat{A}\\big)\\in\\Gamma\\big(\\hat{\\mathbb{S}} _{\\sigma}^{+}\\big)\\times\\mathcal{A}_{\\sigma}\
$$\
\
we deflne the scalar quantity called the\
fl fl fl fl\
\
_energy density_ as\
fl fl fl fl\
\
$$\
\\rho\_{\\hat{\\mathsf{C}}}:=\\big\|\\hat{\\nabla}^{\\hat{A}}\\hat{\\psi}\\big\|^{2}+\\frac{1}{8}\\big\|q(\\hat{\\psi})\\big\|^{2}+\\big\|F\_{\\hat{A}}\\big\|^{2}+\\frac{\\hat{s}}{4}\\big\|\\hat{\\psi}\\big\|^{2}.\
$$\
\
Thus,\
\
$$\
E(\\hat{\\mathsf{C}})=\\int\_{\\hat{N}}\\rho\_{\\hat{\\mathsf{C}}}d v\_{\\hat{g}}.\
$$\
\
For every interval I ‰ R+ and every ">0 we set\
\
$$\
I\\subset\\mathbb{R}\_{+}\
$$\
\
$$\
\\varepsilon>0\
$$\
\
$$\
I\_{\\varepsilon}:=\\left{t\\in\\mathbb{R}\_{+};\\quad\\operatorname{dist}\\left(t,I\\right)\\leq\\varepsilon\\right}\
$$\
\
$$\
E\_{\\hat{\\mathsf{C}}}(I):=\\int\_{I\\times N}\\rho\_{\\hat{\\mathsf{C}}}d v\_{\\hat{g}}.\
$$\
\
Fix a Hermitian connection _A0_ on det()! _N_ and denote by _A0^_ its\
pullback to det(^)! N^. Any smooth Hermitian connection _A^_ on det(^)\
can be written as\
A^ = A0^ \+ i’(t)dt + ia(t)\
\
$$\
A\_{0}\
$$\
\
$$\
\\det(\\sigma)\\to N\
$$\
\
$$\
\\hat{A}\_{0}\
$$\
\
$$\
\\det(\\hat{\\sigma})\\rightarrow\\hat{N}\
$$\
\
$$\
\\hat{A}\
$$\
\
$$\
\\det(\\hat{\\sigma})\
$$\
\
$$\
\\hat{A}=\\hat{A}\_{0}+\\mathbf{i}\\varphi(t)d t+\\mathbf{i}a(t)\
$$\
\
where _’(t_) (resp. a(t)) is a smooth path of 0-forms (resp. 1-forms) on _N._\
Set\
A(t):=A0 \+ ia(t)=A^j :\
\
$$\
\\varphi(t)\
$$\
\
$$\
a(t))\
$$\
\
$$\
A(t):=A\_{0}+\\mathbf{i}a(t)=\\hat{A}\\left\|\_{{t}\\times N}\\right..\
$$\
\
If ^ := eif(t) is a gauge transformation on\
df\
\
_N^_ then\
\
$$\
\\hat{\\gamma}:=e^{\\mathbf{i}f(t)}\
$$\
\
$$\
\\hat{N}\
$$\
\
$$\
\\hat{\\gamma}\\cdot\\hat{A}=\\hat{A}\_{0}+\\mathbf{i}(\\varphi(t)-2\\frac{d f}{d t})d t+\\mathbf{i}(a(t)-2d f(t))\
$$ where we recall that _d_ denotes the _three-dimensional_ exterior derivative\
along _N._ If we regard ^ as a smooth path of gauge transformationst\
on _N_ then the above computation shows\
\
$$\
\\hat{\\gamma}\
$$\
\
$$\
\\gamma\_{t}\
$$\
\
$$\
(\\hat{\\gamma}\\cdot\\hat{A})(t)=\\gamma\_{t}\\cdot A(t).\
$$\
\
In other words, the assignment _A^ 7! A(t_) deflnes a unique class \[A(t)\] _2_\
A =G. This also implies that for any smooth conflguration C^ the assignment\
\
$$\
\\hat{A}\\mapsto A(t)\
$$\
\
$$\
\\left\[A(t)\\right\]\\in\
$$\
\
$$\
\\mathcal{A} _{\\sigma}/\\mathcal{G}_{\\sigma}\
$$\
\
$$\
\\hat{\\mathsf{C}}\
$$\
\
$$\
\\jmath\_{t}:\\hat{\\mathsf{C}}\\mapsto\\mathsf{C}(t):=\\hat{\\mathsf{C}}\\left\|\_{{t}\\times N}\\right.\
$$\
\
deflnes a unique gauge equivalence class \[C(t)\] _2_ B = C =G. Clearly, the\
path _t 7!_ \[C(t)\] in B is continuous. In particular, the quantity\
\
$$\
\[C(t)\]\\in\\mathcal{B} _{\\sigma}=\\mathcal{C}_{\\sigma}/\\mathcal{G}\_{\\sigma}\
$$\
\
$$\
t\\mapsto\[C(t)\]\
$$\
\
$$\
\\mathcal{B}\_{\\sigma}\
$$\
\
$$\
\\nu\_{\\hat{\\mathsf{C}}}(t):=\\mathfrak{f}(\\mathsf{C}(t))=\|S W(\\mathsf{C}(t))\|\_{L^{2}}\
$$\
\
is well deflned and independent of the gauge equivalence class of C^.\
\
$$\
\\hat{\\mathsf{C}}.\
$$\
\
Suppose now that C^ is a 4-monopole. Modulo a smooth gauge transformation we can assume C^ is temporal\
\
$$\
\\hat{\\mathsf{C}}\
$$\
\
$$\
\\hat{\\mathsf{C}}\
$$\
\
$$\
\\hat{\\mathsf{C}}=\\left(\\psi(t),A(t)\\right).\
$$\
\
Then, for every interval _I ‰_\
Z\
\
R+ we have\
Z Z\
\
$$\
I\\subset\\mathbb{R}\_{+}\
$$\
\
$$\
\\int\_{I}\|S W(\\mathsf{C}(t))\| _{L^{2}}^{2}d t=\\int_{t}d t\\int\_{N}\|\\dot{\\psi}(t)\|^{2}+\|\\dot{A}\|^{2}d v\_{g}=\\frac{1}{2}E\_{\\hat{\\mathsf{C}}}(I)\
$$\
\
so that\
\
(4.2.7)\
\
$$\
\|\\nu\_{\\mathsf{C}}\| _{L^{2}(I)}^{2}=\\frac{1}{2}E_{\\hat{\\mathsf{C}}}(I).\
$$\
\
A simple application of H˜older’s inequality shows that\
1\
\
(4.2.8)\
\
$$\
\\operatorname{dist} _{L^{2}}(\[\\mathsf{C}(t_{0})\],\[\\mathsf{C}(t\_{1})\])\\leq\\frac{1}{2}E\_{\\hat{\\mathsf{C}}}(\[t\_{0},t\_{1}\])^{1/2}(t\_{1}-t\_{0})^{1/2}.\
$$\
\
Consider a flnite interval _I_\
\
= \[t0; t1\] 2 R+\
\
and set\
\
$$\
I=\[t\_0,t\_1\]\\in\\mathbb{R} _+_\
_\|s\|:=\\max_{x\\in N}\|s\_g(x)\|.\
$$\
\
Observe that\
\
$$\
\\begin{align\*}&\\frac{1}{16}\|\\hat{\\psi}\| _{L^4(I\\times N)}^4=\\frac{1}{16}\\int\_I dt\\int\_N\|\\hat{\\psi}(t,x)\|^4dv\_g\\&=\\frac{1}{8}\\int\_I dt\\int\_N\|q(\\hat{\\psi})\|^2\\leq E_{\\hat{\\mathsf{C}}}(I)-\\frac{1}{4}\\int\_I dt\\int\_N s\|\\hat{\\psi}\|^2dv\_g\\&\\quad\\leq E\_{\\hat{\\mathsf{C}}}(I)+\\frac{\|s\|}{4}\\int\_I dt\\int\_N\|\\hat{\\psi}\|^2dv\_g\\&\\quad\\leq E\_{\\hat{\\mathsf{C}}}(I)+\\frac{\|s\|}{4}(t\_1-t\_0)^{1/2}\\mathrm{vol} _g(N)^{1/2}\|\\hat{\\psi}\|_{L^4(I\\times N)}^2\\&\\quad\\leq E\_{\\hat{\\mathsf{C}}}(I)+\\frac{1}{32}\|\\hat{\\psi}\|\_{L^4(I\\times N)}^4+\\frac{\|s\|^2}{2}(t\_1-t\_0)\\mathrm{vol}\_g(N).\\end{align\*}\
$$\
\
* * *\
\
We have thus obtained the following _L4_-estimate.\
\
(4.2.9)\
\
$$\
L^{4}.\
$$\
\
$$\
\|\\hat{\\psi}\| _{L^{4}(I\\times N)}^{4}\\leq32E_{\\hat{\\mathsf{C}}}(I)+16\|s\|^{2}(t\_{1}-t\_{0})\\mathrm{vol}\_{g}(N).\
$$\
\
We can build on this estimate to obtain a priori\
\
_L1_-estimates for ˆ^.\
\
$$\
L^{\\infty}\
$$\
\
$$\
\\hat{\\psi}\_{i}\
$$\
\
**Proposition 4.2.12.** _There exists a constant C>_\
_the metric g such that_\
‡\
\
0 _which depends only on_\
·\
\
$$\
C>0\
$$\
\
(4.2.10)\
\
$$\
\|\\hat{\\psi}\| _{L^{\\infty}(\[T,T+1\]\\times N)}^{4}\\leq C\\Big(E_{\\hat{\\mathsf{C}}}(\[T-1,T+2\])+1\\Big),\\quad\\forall T>1.\
$$\
\
**Proof** We have\
\
$$\
0=\\mathfrak{D} _{\\hat{A}}^{\*}\\mathfrak{D}_{\\hat{A}}\\hat{\\psi}=\\big(\\hat{\\nabla}^{\\hat{A}}\\big)^{\*}\\hat{\\nabla}^{\\hat{A}}\\hat{\\psi}+\\frac{s}{4}\\hat{\\psi}+\\frac{1}{2}\\hat{\\mathbf{c}}(F\_{\\hat{A}}^{+})\\hat{\\psi}.\
$$\
\
We can now use Kato’s inequality and the equality c^(F +)=1/2q(ˆ^) to con-\
A^\
clude that\
D¡ E\
¢ _s_1\
\
$$\
\\hat{\\mathbf{c}}(F\_{\\hat{A}}^{+})=\\frac{1}{2}q(\\hat{\\psi})\
$$\
\
$$\
\\hat{\\Delta}\_{\\hat{g}}\|\\hat{\\psi}\|^{2}\\leq2\\Big\\langle\\big(\\hat{\\nabla}^{\\hat{A}}\\big)^{\*}\\hat{\\nabla}^{\\hat{A}}\\hat{\\psi},\\hat{\\psi}\\Big\\rangle=-\\frac{s}{2}\|\\hat{\\psi}\|^{2}-\\frac{1}{4}\|\\hat{\\psi}\|^{4}.\
$$\
\
Now set _u_ := _ĵ^j2_ so that we have\
\
$$\
u:=\|\\hat{\\psi}\|^2\
$$\
\
$$\
\\hat{\\Delta}\_{\\hat{g}}u+\\frac{s}{2}u\\leq-\\frac{1}{4}u^{2}\\leq0.\
$$\
\
We can rewrite this as a difierential inequality of the type\
\
$$\
\\hat{\\Delta}\_{\\hat{g}}u+a u\\leq0\
$$\
\
s\
where _a_ = _2 L1(\[T ¡1;T_ \+ 2\]£ N). Using the DeGiorgi-Nash-Moser in-\
2\
equality (see **\[11\]** or \[ **47,** Thm. 8.17\]) we deduce that there exists a constant\
_C_ >0 which depends only on _g_ such that\
‡ ·\
\
$$\
a=\\frac{s}{2}\\in L^{\\infty}(\[T-1,T+2\]\\times N)\
$$\
\
$$\
C>0\
$$\
\
$$\
\\operatorname\*{s u p} _{\[T,T+1\]\\times N}u\\leq C\\Big(\|s\|+\|u\|_{L^{2}(\[T-1,T+2\]\\times N)}\\Big)\
$$\
\
$$\
\\stackrel{(4.2.9)}{\\leq}C^{\\prime}\\Big(E\_{\\hat{\\mathsf{C}}}(\[t-1,T+2\])+1\\Big)^{1/2}.\\blacksquare\
$$\
\
**Corollary 4.2.13.** _If_ C^ =(ˆ;^ A^) _is a flnite energy monopole on N^_ = _R£ N_\
_then there exists a constant C_ >0 _which depends only on the metric g such_\
_that_\
‡ ·\
\
$$\
\\mathit{If}\\hat{\\mathsf{C}}=(\\hat{\\psi},\\hat{A})\
$$\
\
$$\
\\hat{N}=\\mathbb{R}\\times N\
$$\
\
$$\
C>0\
$$\
\
(4.2.11)\
\
$$\
\|\\hat{\\psi}\| _{L^{\\infty}(\\hat{N})}^{4}\\leq C\\Big(E_{\\hat{\\mathsf{C}}}(\\mathbb{R}\_{+})+1\\Big).\
$$\
\
The next result, whose proof is deferred to x4.2.5, shows that if the total\
kinetic energy over a time period of length 4 is small enough, then the kinetic\
energy at each moment must be small. In other words, \\bursts" of energy\
are prohibited.\
\
* * *\
\
**Lemma 4.2.14.** _Fix a smooth connection A0 on_ det(). _There exist C0_ \> 0\
_and_ 0 < _!_ < 1 _such that for every smooth_ **temporal** _monopole_ C^ _on_\
0\
\[¡2;2\] _£ N satisfying_\
^ = (C(\
\
$$\
A \_ {0}\
$$\
\
$$\
C \_ {0} > 0\
$$\
\
$$\
0 < \\omega\_ {0} < 1\
$$\
\
$$\
\[ \- 2, 2 \] \\times N\
$$\
\
$$\
\\hat {\\mathrm {C}} = (\\mathrm {C} (t)) = \\left(\\psi (t), A \_ {0} + \\mathbf {i} a (t)\\right), a (t) \\in \\Omega^ {1} (N),\
$$\
\
$$\
E ^ {2} := \\int\_ {- 2} ^ {2} d t \\int\_ {N} \\left(\| \\dot {\\psi} (t) \| ^ {2} + \| \\dot {a} (t) \| ^ {2}\\right) d v \_ {N} \\leq \\omega\_ {0}\
$$\
\
_we have_\
\
$$\
\\left\| S W \\left(\\mathrm {C} (t)\\right) \\right\| \_ {L ^ {2} (N)} ^ {2} = \\int\_ {N} \\left(\| \\dot {\\psi} (t) \| ^ {2} + \| \\dot {a} (t) \| ^ {2}\\right) d v \_ {N} \\leq C \_ {0} E ^ {2}, \\forall t \\in \[ - 1, 1 \].\
$$\
\
**Corollary 4.2.15.** _There exist C_ >0 _and !₀ 2_ (0;1) _such that if_ C^ _is a_\
_smooth monopole on_ \[¡2;2\] _£ N satisfying_\
\
$$\
C > 0\
$$\
\
$$\
\\omega\_ {0} \\in (0, 1)\
$$\
\
$$\
i f \\hat {\\mathrm {C}}\
$$\
\
$$\
\[ \- 2, 2 \] \\times N\
$$\
\
$$\
E ^ {2} := E \_ {\\hat {\\mathrm {C}}} (\[ - 2, 2 \]) \\leq \\omega\_ {0}\
$$\
\
_then_\
\
$$\
\\left\| S W \\left(\\hat {\\mathsf {C}} \| \_ {t \\times N}\\right) \\right\| \_ {L ^ {2} (N)} \\leq C \_ {0} E, \\forall t \\in \[ - 1, 1 \].\
$$\
\
**Proof** Since the above inequality is invariant under gauge transformations\
on \[¡2;2\]£ _N_ we can assume C^ is in temporal gauge and then apply Lemma\
4.2.14. ¥\
\
$$\
\[ \- 2, 2 \] \\times N\
$$\
\
For every ~ > 0 denote by f~ the level set of f\
\
$$\
\\hbar > 0\
$$\
\
$$\
\\mathrm {f} ^ {\\hbar}\
$$\
\
$$\
\\mathrm {f} ^ {\\hbar} = \\left{C \\in \\mathcal {C} \_ {\\sigma}; \\mathrm {f} (\\mathrm {C}) < \\hbar \\right}.\
$$\
\
Observe that f~ is an open neighborhood of Z in B. The following result\
reflnes Proposition 2.4.6 of 2.4.1. We leave its proof to the reader.\
\
$$\
\\mathrm {f} ^ {\\hbar}\
$$\
\
$$\
Z \_ {\\sigma}\
$$\
\
$$\
\\mathcal {B} \_ {\\sigma}\
$$\
\
**Proposition 4.2.16.** _There exists a function_\
\
$$\
\\hbar : (0, 1) \\rightarrow (0, \\infty), \\kappa \\mapsto \\hbar (\\kappa)\
$$\
\
_such that_\
\
(i) lim•!0 ~(•) = 0.\
\
$$\
\\lim \_ {\\kappa \\rightarrow 0} \\hbar (\\kappa) = 0.\
$$\
\
_(ii)If_ C _2_ f~(•) _then there exist a smooth monopole_ C0 _2_ Z _and 2_ G _such_ _that_ _¢_ C _2 U_ ( _•):_\
\
$$\
\\mathrm {C} \_ {0} \\in \\mathcal {Z} \_ {\\sigma}\
$$\
\
$$\
(i i) I f \\mathrm {C} \\in \\mathfrak {f} ^ {\\hbar (\\kappa)}\
$$\
\
$$\
\\gamma \\in \\mathcal {G} \_ {\\sigma}\
$$\
\
$$\
\\gamma \\cdot \\mathsf {C} \\in U \_ {\\mathrm {C} \_ {0}} (\\kappa).\
$$\
\
From the above proposition we deduce the following consequence.\
\
Corollary 4.2.17. If M =; there exists ~0 \> 0 such that f(C) > ~0, 8C.\
\
$$\
I f \\mathfrak {M} \_ {\\sigma} = \\emptyset\
$$\
\
$$\
\\hbar\_ {0} > 0\
$$\
\
$$\
\\mathrm {f} (\\mathrm {C}) > \\hbar\_ {0}, \\forall \\mathrm {C}\
$$\
\
* * *\
\
The above result, coupled with Corollary 4.2.15, leads to the following\
conclusion.\
\
**Corollary 4.2.18.** _If_ C^ _is a flnite energy monopole on_\
sequence tn!1we can flnd a subsequence tn such that\
_k_ _to a point in M._\
\
R+ £ N then for any\
\[C(tnk)\] converges\
\
$$\
I f \\hat {C}\
$$\
\
$$\
\\mathbb {R} \_ {+} \\times N\
$$\
\
$$\
t \_ {n} \\rightarrow \\infty\
$$\
\
$$\
t \_ {n \_ {k}}\
$$\
\
$$\
\\left\[ \\mathrm {C} \\left(t \_ {n \_ {k}}\\right) \\right\]\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
‘)\
If M(1); ¢¢¢;M(are the connected components of M\
0 such that _U_•0consists of _disjoint_ open neighborhoods\
_1; ¢¢¢; ‘._ Set\
¡\
d0 = d0(•) := min dist U(i);U0(j)\
\
we can flnd •0 >\
U•(j)0of M(j), j =\
¢\
_:_\
\
$$\
\\mathfrak {M} \_ {\\sigma} ^ {(1)}, \\dots , \\mathfrak {M} \_ {\\sigma} ^ {(\\ell)}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\kappa\_ {0} >\
$$\
\
$$\
U \_ {\\kappa\_ {0}} ^ {(j)}\
$$\
\
$$\
U \_ {\\kappa\_ {0}}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma} ^ {(j)}, j =\
1, \\dots , \\ell\
$$\
\
$$\
d \_ {0} = d \_ {0} \\left(\\kappa\_ {0}\\right) := \\min \_ {i \\neq j} \\operatorname {d i s t} \_ {L ^ {2}} \\left(U \_ {\\kappa\_ {0}} ^ {(i)}, U \_ {\\kappa\_ {0}} ^ {(j)}\\right).\
$$\
\
**Exercise 4.2.3.** Show that\
\
$$\
\\liminf \_ {\\kappa\_ {0} \\searrow 0} d \_ {0} \\left(k \_ {0}\\right) > 0.\
$$\
\
Hint: Show that if •0 is su–ciently small there exists a constant C>0\
depending only on the geometry of _N_ and _C(E0_) such that\
\
$$\
\\kappa\_ {0}\
$$\
\
$$\
C > 0\
$$\
\
$$\
C \\left(E \_ {0}\\right)\
$$\
\
$$\
\\operatorname {d i s t} \_ {L ^ {2}} \\left(\[ \\mathsf {C} \], \\mathfrak {M} \_ {\\sigma} ^ {(i)}\\right) \\leq C \\kappa\_ {0}, \\forall i, \\forall \[ \\mathsf {C} \] \\in U \_ {\\kappa\_ {0}} ^ {(i)}.\
$$\
\
Corollary 4.2.15 shows that if C^ is a flnite energy monopole and _T_ >0\
is such that\
E (\[T; 1)) ¿ ~(•)\
\
$$\
\\hat {C}\
$$\
\
$$\
T > 0\
$$\
\
$$\
E \_ {\\hat {C}} (\[ T, \\infty)) \\ll \\hbar (\\kappa)\
$$\
\
then \[C(t)\] _2 U_•, _8t>T+_ 1\. Clearly, for large _t_ the path _t 7!_ \[C(t)\] will\
wander inside a single component U•(j) of U•. We have thus proved the\
following result.\
\
$$\
\[ \\mathrm {C} (t) \] \\in U \_ {\\kappa}, \\forall t > T + 1\
$$\
\
$$\
t \\mapsto \[ C (t) \]\
$$\
\
$$\
U \_ {\\kappa} ^ {(j)}\
$$\
\
$$\
U \_ {\\kappa}\
$$\
\
**Corollary 4.2.19.** _Suppose_ C^ _is a flnite energy smooth monopole on N^._\
Then there exist a connected component M(j) of M and, for all •>0, an\
instant of time t = t(•) > 0, such that \[C(t)\] 2 U•(j) for all t > t(•).\
\
$$\
\\hat {C}\
$$\
\
$$\
\\hat {N}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma} ^ {(j)}\
$$\
\
$$\
\\kappa > 0\
$$\
\
$$\
t = t (\\kappa) > 0\
$$\
\
$$\
\[ \\mathrm {C} (t) \] \\in U \_ {\\kappa} ^ {(j)}\
$$\
\
$$\
t > t (\\kappa)\
$$\
\
A priori, the path \[C(t)\] in the above corollary may wander around\
smaller and smaller neighborhoods U•(j) of M(j) without converging to any\
specifled 3-monopole so the limit set may consist of several points in M.\
The results we proved so far show that the manner in which \[C(t)\] travels\
around M is quite constrained. More precisely, for every triple of arbitrarily\
small constants _a; b; c_ \> 0 there exists an instant of time _T_ = _T (a; b; c)_ \> 0\
such that for all _t_ >Tthe distance between \[C(t)\] and M is < _a,_ the kinetic\
energy kˆ\_ (t)k2L \+ ka\_ (t)k2L at time t is < b, and there is not much energy\
2 2\
left, i.e.\
E (\[T; 1)) < c:\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
U \_ {\\kappa} ^ {(j)}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma} ^ {(j)}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
a, b, c > 0\
$$\
\
$$\
T = T (a, b, c) > 0\
$$\
\
$$\
t > T\
$$\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
\| \\dot {\\psi} (t) \| \_ {L ^ {2}} ^ {2} + \| \\dot {a} (t) \| \_ {L ^ {2}} ^ {2}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma} \\mathrm {i s} < a\
$$\
\
$$\
E \_ {\\hat {C}} (\[ T, \\infty)) < c.\
$$\
\
The energy functional _E_ on _N_ (whose critical points are the 3-monopoles)\
may not descend to C _=G_ so it may not induce a well deflned function on\
\
$$\
\\mathcal {E}\
$$\
\
$$\
\\mathcal {C} \_ {\\sigma} / \\mathcal {G} \_ {\\sigma}\
$$\
\
* * *\
\
M. On the other hand, it descends to function on C =G1 where G1 denotes\
the identity component of G. We denote by M~ the space of G1-orbits of 3-\
monopoles. _E_ deflnes a continuous map from the discrete set of components\
of M~ to R. M is a quotient of M~ modulo the action of the discrete group\
H1(N;Z). Since\
E(C(t1)) ¡E(C(t0)) = E (\[t0; t1\])\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\mathcal {C} \_ {\\sigma} / \\mathcal {G} \_ {\\sigma} ^ {1}\
$$\
\
$$\
\\mathcal {G} \_ {\\sigma} ^ {1}\
$$\
\
$$\
\\mathcal {G} \_ {\\sigma}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\mathcal {G} \_ {\\sigma} ^ {1}\
$$\
\
$$\
\\mathcal {E}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\mathbb {R}. \\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
\\mathfrak {M} \_ {\\sigma}\
$$\
\
$$\
H ^ {1} (N, \\mathbb {Z})\
$$\
\
$$\
\\mathcal {E} \\left(\\mathrm {C} \\left(t \_ {1}\\right)\\right) - \\mathcal {E} \\left(\\mathrm {C} \\left(t \_ {0}\\right)\\right) = E \_ {\\hat {\\mathrm {C}}} \\left(\[ t \_ {0}, t \_ {1} \]\\right)\
$$\
\
E(C(t)) has a well deflned limit _E1_ as _t !1so_ that the path C(t) \\orbits"\
closer and closer around one of the components of M~ where _E·E1._\
\
$$\
\\mathcal {E} (\\mathrm {C} (t))\
$$\
\
$$\
\\mathcal {E} \_ {\\infty}\
$$\
\
$$\
t \\rightarrow \\infty\
$$\
\
$$\
\\mathrm {C} (t) \\text {" o r b i t s"}\
$$\
\
$$\
\\mathcal {E} \\equiv \\mathcal {E} \_ {\\infty}\
$$\
\
$$\
\\tilde {\\mathfrak {M}} \_ {\\sigma}\
$$\
\
In the next subsection we will show that these restrictions, coupled with\
the ellipticity of the Seiberg-Witten equations on cylinders, will force \[C(t)\]\
to converge to a specifled monopole \[C0\] _2_ M. To minimize the volume\
of technicalities we will make the simplifying assumption below which is\
satisfled in all concrete applications we have in mind. For a presentation of\
the general situation in the similar case of Yang-Mills equations we refer to\
\[ **96, 133\].**\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
\[ \\mathrm {C} \_ {0} \] \\in \\mathfrak {M} \_ {\\sigma}\
$$\
\
(N)\
\
_In the remainder of this chapter we will work exclusively with_\
_good pairs_ ( _; g):_\
\
**4.2.4. Asymptotic behavior. Part II.** Suppose C^ is a flnite energy\
monopole on N^. In the last subsection we have shown that for every\
0 < _•¿_ 1 there exist a smooth monopole C0 and an interval _J_ = _\[t0; t1\] ‰_\
R+ such that for every t 2 J the conflguration \[C(t)\] 2 UC0(•). We deduced this conclusion by taking advantage of the nice dynamical description\
of the Seiberg-Witten equations in temporal gauge. These arguments were\
however not powerful enough to deduce, for example, that once \[C(t)\] enters\
a neighborhood UC0(•) of \[C0\] it is then forced to stay inside it. From a\
technical point of view this is due essentially to a lack of estimates of the\
length of the path \[C(t)\], that is, estimating _L1_-norms of _t_-derivatives on\
_long_ time intervals. It is desirable to control the length of a portion of this\
path in terms of its energy. To obtain such estimates we need to modify C^\
by a gauge transformation which will capture the _elliptic_ character of the\
Seiberg-Witten equations on a cylinder. Following **\[96, 133\]** we introduce\
the following notion.\
\
$$\
\\hat {C}\
$$\
\
$$\
\\hat {N}\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
0 < \\kappa \\ll 1\
$$\
\
$$\
J = \\left\[ t \_ {0}, t \_ {1} \\right\] \\subset\
$$\
\
$$\
t \\in J\
$$\
\
$$\
\\mathbb {R} \_ {+}\
$$\
\
$$\
\[ \\mathrm {C} (t) \] \\in U \_ {\\mathrm {C} \_ {0}} (\\kappa)\
$$\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
U \_ {\\mathrm {C} \_ {0}} (\\kappa)\
$$\
\
$$\
\[ \\mathrm {C} \_ {0} \]\
$$\
\
$$\
L^{1} \\mathrm{-n o r m s}\
$$\
\
$$\
\\hat {C}\
$$\
\
**Deflnition 4.2.20.** Let _• 2_ (0;1) and C0 be a smooth monopole on N.A\
conflguration C^ on a cylinder _I£N_ is said to be in _•_- _standard gauge_ with\
respect to C0 if there exist smooth paths\
\
$$\
\\kappa \\in (0, 1)\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
\\hat {C}\
$$\
\
$$\
I \\times N\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
I \\ni t \\rightarrow (\\mathbf {i} f (t), \\mathrm {V} (t)) \\in \\left(\\ker \\mathfrak {L} \_ {\\mathrm {C} \_ {0}}\\right) ^ {\\perp} \\times \\mathcal {S} \_ {\\mathrm {C} \_ {0}}, \\mathrm {V} (t) = (\\psi (t), \\mathbf {i} a (t))\
$$\
\
such that kV(t)k2;2 = kˆ(t)k2;2 \+ ka(t)k\
\
2;2 < •, 8t 2 I and\
\
$$\
\| \\mathrm {V} (t) \| \_ {2, 2} = \| \\psi (t) \| \_ {2, 2} + \| a (t) \| \_ {2, 2} < \\kappa , \\forall t \\in I \\text {a n d}\
$$\
\
$$\
\\hat {\\mathrm {C}} = \\left(\\psi\_ {0} + \\psi (t), A \_ {0} + \\mathbf {i} f (t) d t + \\mathbf {i} a (t)\\right).\
$$\
\
* * *\
\
For a proof of the following technical result we refer to \[ **96,** Lemma\
2.4.3\].\
\
**Lemma 4.2.21.** _Assume_ C^ _is a smooth conflguration on I £ N and_ C0 _is a_\
_smooth monopole on N such that_ C(t) _is gauge equivalent to a conflguration_\
in UC0(•), 8t 2 I. Then there exists a smooth gauge transformation\
\
$$\
\\hat {C}\
$$\
\
$$\
I \\times N\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
\\mathrm {C} (t)\
$$\
\
$$\
U \_ {\\mathrm {C} \_ {0}} (\\kappa), \\forall t \\in I\
$$\
\
$$\
\\hat {\\gamma}: I \\times N \\rightarrow S ^ {1}\
$$\
\
_such that_ ^ _¢_ C^ _is in •-standard gauge with respect to_\
\
C0.\
\
$$\
\\hat {\\gamma} \\cdot \\hat {C}\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
Suppose now that C^ is a smooth 4-monopole on\
gauge with respect to the smooth 3-monopole C0\
write\
C^ =(ˆ^ = ˆ0 \+ ˆ(t); A^ = A0 +\
\
_I£N_ in _•_-standard\
= ( _ˆ0; A0)._ Thus, we can\
idf (t)dt + ia(t))\
\
$$\
\\hat {C}\
$$\
\
$$\
I \\times N\
$$\
\
$$\
\\mathrm {C} \_ {0} = \\left(\\psi\_ {0}, A \_ {0}\\right)\
$$\
\
$$\
\\hat {\\mathrm {C}} = \\left(\\hat {\\psi} = \\psi\_ {0} + \\psi (t), \\hat {A} = A \_ {0} + \\mathbf {i} d f (t) d t + \\mathbf {i} a (t)\\right)\
$$\
\
where, for any _t 2 I,_\
\
$$\
t \\in I\
$$\
\
(4.2.12)\
\
$$\
\| a (t) \| \_ {\\frac {3}{2}, 2} + \| \\psi (t) \| \_ {\\frac {3}{2}, 2} \\leq \\kappa ,\
$$\
\
$$\
\\mathfrak {L} \_ {\\mathrm {C} 0} ^ {\*} \\left(\\psi (t), \\mathbf {i} a (t)\\right) = 0, \\mathbf {i} f (t) \\perp \\ker \\mathfrak {L} \_ {\\mathrm {C} 0}.\
$$\
\
Then, using the identities (2.4.1) and (2.4.2) in\
\
x2.4.1, we deduce\
\
$$\
F \_ {\\hat {A}} = F \_ {A \_ {0}} + \\mathbf {i} d t \\wedge (\\dot {a} (t) - d f (t)) + \\mathbf {i} d a (t),\
$$\
\
$$\
\\begin{array}{l} F \_ {\\hat {A}} ^ {+} = \\frac {\\mathbf {i}}{2} \\left(d t \\wedge \\left(\\dot {a} + \* F \_ {A \_ {0}} + \* d a (t) - d f (t)\\right) + \* \\left(\\dot {a} (t) + F \_ {A \_ {0}} + d a (t) - d f (t)\\right)\\right) \ (J := \\hat {\\mathbf {c}} (d t), A (t) := A \_ {0} + \\mathbf {i} a (t)), \ \\end{array}\
$$\
\
$$\
\\mathcal {D} \_ {\\hat {A}} = J \\left(\\partial\_ {t} - \\mathfrak {D} \_ {A (t)} + \\frac {\\mathbf {i}}{2} f (t)\\right).\
$$\
\
If we suppress the _t_ dependence in the above notation and we use the identity\
‡ ·\
1 1\
\
$$\
\\mathfrak {D} \_ {A} \\psi\_ {0} = \\left(\\mathfrak {D} \_ {A \_ {0}} + \\frac {1}{2} c (\\mathbf {i} a)\\right) \\psi\_ {0} = \\frac {1}{2} c (\\mathbf {i} a) \\psi\_ {0}\
$$\
\
we can rewrite the Seiberg-Witten equations for C\
‡ ·\
\
^ as follows.\
\
(4.2.13a)\
\
$$\
\\hat {C}\
$$\
\
$$\
\\frac {d}{d t} \\psi = \\left(\\mathfrak {D} \_ {A} - \\frac {\\mathbf {i}}{2} f\\right) (\\psi + \\psi\_ {0}) = \\mathfrak {D} \_ {A \_ {0}} \\psi + \\frac {1}{2} \\left(c (\\mathbf {i} a) - \\mathbf {i} f\\right) (\\psi\_ {0} + \\psi),\
$$\
\
(4.2.13b)\
\
$$\
\\mathbf {i} \\frac {d}{d t} a = \\frac {1}{2} q \\left(\\psi\_ {0} + \\psi\\right) - \* \\mathbf {i} d a + \\mathbf {i} d f - \* F \_ {A \_ {0}},\
$$\
\
(4.2.13c)\
\
$$\
d ^ {\*} a + \\frac {1}{2} \\mathfrak {I m} \\langle \\psi\_ {0}, \\psi \\rangle = 0.\
$$\
\
One unpleasant feature of these equations is the apparent lack of information on the _t_-derivatives of _f._ Still, the size of _f_ can be controlled in terms of the sizes of ( _ˆ;_ A). To achieve this we will need an elementary\
identity whose proof is left to the reader.\
\
$$\
(\\psi , A)\
$$\
\
**Exercise 4.2.4.** (\[107\]) Suppose\
smooth Hermitian connection on det(\
\
_ˆ_ is a smooth spinor on _N_ and _A_ is a\
). Then\
\
$$\
\\psi\
$$\
\
(4.2.14)\
\
$$\
d ^ {\*} q (\\psi) = - \\mathrm {i} \\Im \\mathfrak {m} \\langle \\psi , \\mathfrak {D} \_ {A} \\psi \\rangle .\
$$\
\
For simplicity, in the sequel will denote the\
we will denote by the same letter\
_on_ C0, _the total energy of_ C^\
\
_t_-derivatives by dots. Also,\
_C all positive constants which depend only_\
_and the metric g._\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
\\hat {C}\
$$\
\
$$\
g.\
$$\
\
Difierentiating (4.2.13c) with respect to\
\
_t_ we get\
\
$$\
\\mathbf {i} d ^ {\*} \\dot {a} + \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0}, \\dot {\\psi} \\rangle = 0.\
$$\
\
Now use (4.2.13c) and (4.2.14) to obtain\
\
$$\
\\begin{array}{l} 0 = \\frac {1}{2} d ^ { _} q (\\psi + \\psi\_ {0}) + \\mathbf {i} d ^ {_} d f + \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0}, \\dot {\\psi} \\rangle \ \\stackrel {(4. 2. 1 3 a)} {=} - \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0} + \\psi , \\mathfrak {D} \_ {A} (\\psi\_ {0} + \\psi) \\rangle + \\mathbf {i} d ^ { _} d f + \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0}, \\dot {\\psi} \\rangle \ = - \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0} + \\psi , \\dot {\\psi} + \\frac {\\mathbf {i}}{2} f (\\psi + \\psi\_ {0}) \\rangle + \\mathbf {i} d ^ {_} d f + \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi\_ {0}, \\dot {\\psi} \\rangle \ = \\mathbf {i} d ^ {\*} d f + \\frac {\\mathbf {i}}{4} \| \\psi\_ {0} + \\psi \| ^ {2} f - \\frac {\\mathbf {i}}{2} \\mathfrak {I m} \\langle \\psi , \\dot {\\psi} \\rangle \\stackrel {(4. 2. 1 3 a)} {=} \ \\end{array}\
$$\
\
$$\
\\begin{array}{l} \\mathbf {i} d ^ { _} d f + \\frac {\\mathbf {i}}{4} \\Re e \\langle \\psi\_ {0} + \\psi , \\psi\_ {0} + \\psi \\rangle f - \\frac {\\mathbf {i}}{2} \\Im m \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle - \\frac {\\mathbf {i}}{4} \\Re e \\langle \\psi , (\\psi\_ {0} + \\psi) \\rangle f \ = \\mathbf {i} d ^ {_} d f + \\frac {\\mathbf {i}}{4} \\Re e \\langle \\psi\_ {0}, \\psi\_ {0} + \\psi \\rangle f - \\frac {\\mathbf {i}}{2} \\Im m \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle \ = \\mathbf {i} d ^ { _} d f + \\frac {\\mathbf {i}}{4} \| \\psi\_ {0} \| ^ {2} f + \\frac {\\mathbf {i}}{4} \\Re e \\langle \\psi\_ {0}, \\psi \\rangle f - \\frac {\\mathbf {i}}{2} \\Im m \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle \ = \\frac {\\mathbf {i}}{4} \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} ^ {_} \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} (\\mathbf {i} f) + \\frac {1}{4} \\Re e \\langle \\psi\_ {0}, \\psi \\rangle \\mathbf {i} f - \\frac {\\mathbf {i}}{2} \\Im m \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle . \ \\end{array}\
$$\
\
Hence\
\
(4.2.15)\
\
$$\
\\mathfrak {L} \_ {\\mathrm {C} \_ {0}} ^ {\*} \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} \\mathbf {i} f = - \\Re \\mathfrak {e} \\langle \\psi\_ {0}, \\psi \\rangle \\mathbf {i} f + 2 \\Im \\mathfrak {m} \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle .\
$$\
\
The proof of the following result is a simple application of Theorem\
1.2.18 (v) and is left to the reader.\
\
$$\
\\psi\
$$\
\
Lemma 4.2.22. For each ˆ such that kˆk2;2 • • consider the operator\
\
$$\
\| \\psi \| \_ {2, 2} \\leq \\kappa\
$$\
\
$$\
T \_ {\\psi}: \\ker \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} ^ {\\perp} \\cap L ^ {3, 2} \\rightarrow L ^ {1, 2} (N, \\mathbf {i} \\mathbb {R}), \\mathbf {i} f \\mapsto \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} ^ {\*} \\mathfrak {L} \_ {\\mathrm {C} \_ {0}} + \\Re \\mathfrak {e} \\langle \\psi\_ {0}, \\psi \\rangle \\mathbf {i} f.\
$$\
\
Then, if • is su–ciently small the operator Tˆ is invertible. Moreover for\
_every r 2 f0; 1g and every p 2_ (1;2\] _there exists a constant C_ >0 _depending_\
_only on p, r and the geometry of N such that_\
\
$$\
T \_ {\\psi}\
$$\
\
$$\
r \\in {0, 1 }\
$$\
\
$$\
p \\in (1, 2 \]\
$$\
\
$$\
C > 0\
$$\
\
$$\
N\
$$\
\
$$\
\| f \| \_ {2 + r, p} \\leq C \| T \_ {\\psi} \\mathbf {i} f \| \_ {r, p}.\
$$\
\
* * *\
\
Using the above lemma we deduce that there exists a constant _C_ >0\
such that\
kfk • CkImĥ;D 0ˆik :\
\
$$\
C > 0\
$$\
\
$$\
\| f \| \_ {2, 2} \\leq C \| \\mathfrak {I m} \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle \| \_ {L ^ {2}}.\
$$\
\
The Sobolev embedding theorems show that we have continuous embeddings\
\
$$\
L ^ {2, 2} (N) \\hookrightarrow L ^ {\\infty} (N), L ^ {1, 2} (N) \\hookrightarrow L ^ {6} (N).\
$$\
\
Using H˜older’s inequality we deduce that there exists a constant _C_ >0 such\
that for every a 2 L2;2(N) and b 2 L1;2(N) we have\
\
$$\
C > 0\
$$\
\
$$\
a \\in L ^ {2, 2} (N)\
$$\
\
$$\
b \\in L ^ {1, 2} (N)\
$$\
\
$$\
\| a \\cdot b \| \_ {L ^ {1, 2}} \\leq C \| a \| \_ {2, 2} \\cdot \| b \| \_ {1, 2}.\
$$\
\
Hence\
\
$$\
\| \\Im \\mathfrak {m} \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle \| \_ {L ^ {1, 2}} \\leq C \| \\psi \| \_ {2, 2} \| \\mathfrak {D} \_ {A \_ {0}} \\psi \| \_ {1, 2} \\leq C \| \\psi \| \_ {2, 2} ^ {2}.\
$$\
\
We have thus established the estimate\
\
(4.2.16)\
\
$$\
\| f \| \_ {2, 2} \\leq C \| \\psi \| \_ {2, 2} ^ {2} < ^ {(4. 2. 1 2)} C \\kappa^ {2}.\
$$\
\
Since _•_ is meant to be very small we deduce that _f_ (t) is very small as long\
as C^ _jI£N_ is in _•_-standard gauge. Set\
\
$$\
\\hat {C} \| \_ {I \\times N}\
$$\
\
$$\
\\mathrm {V} (t) := \\left(\\psi (t), \\mathbf {i} a (t)\\right).\
$$\
\
The ow equations (4.2.13) can be rewritten as\
•\
\
(4.2.17)\
\
$$\
\\dot {\\mathrm {V}} = S W \\left(\\mathrm {C} \_ {0} + \\mathrm {V}\\right) + \\left\[ \\begin{array}{c} - \\frac {\\mathrm {i} f}{2} \\psi\_ {0} - \\frac {\\mathrm {i} f}{2} \\psi \ \\mathbf {i} d f \\end{array} \\right\]\
$$\
\
where\
\
(4.2.18)\
\
$$\
\\mathfrak {L} \_ {\\mathrm {C} \_ {0}} ^ {\*} \\mathrm {V} = 0\
$$\
\
and\
\
(4.2.19)\
\
$$\
\\mathbf {i} f = 2 T \_ {\\psi} ^ {- 1} \\left(\\mathbf {i} \\Im \\mathfrak {m} \\langle \\psi , \\mathfrak {D} \_ {A \_ {0}} \\psi \\rangle\\right).\
$$\
\
We will denote the second term on the right-hand side of (4.2.17) by N(V).\
Observe that\
1\
\
$$\
\\mathfrak {N} (\\mathrm {V})\
$$\
\
(4.2.20)\
\
$$\
\\mathfrak {N} (\\mathrm {V}) = - \\frac {1}{2} \\mathfrak {L} \_ {\\mathrm {C} \_ {0} + \\mathrm {V}} (\\mathbf {i} f).\
$$\
\
The estimate (4.2.16) shows that\
\
(4.2.21)\
\
$$\
\| \\mathfrak {N} (\\mathrm {V}) \| \_ {2, 2} \\leq C \| \\mathrm {V} \| \_ {2, 2} ^ {2}.\
$$\
\
**Remark 4.2.23.** One can show exactly as in \[ **96,** Chap. 2\] that there\
exists a natural L2-metric on SC0such that in a neighborhood of 0 2 S0C\
the equations (4.2.17) have the form\
~\
\
$$\
L ^ {2}\
$$\
\
$$\
0 \\in \\mathcal {S} \_ {\\mathrm {C} \_ {0}}\
$$\
\
$$\
\\mathcal {S} \_ {\\mathrm {C} \_ {0}}\
$$\
\
$$\
\\dot {V} = \\tilde {\\nabla} \\mathcal {E} \| \_ {\\mathcal {S} \_ {C \_ {0}}} \\left(C \_ {0} + V\\right)\
$$\
\
where the gradient _r_ ~ is computed with respect to this metric. ¥\
\
$$\
\\tilde {\\nabla}\
$$\
\
* * *\
\
For every 0 < _•¿_ 1 we can flnd _T0(_ _t0 ‚ T0(•_) there exists a smooth monopole C0\
8\
\
•)=T0(•;C^) 0 such that for all\
= C0(t0) _2_ M so that\
\
$$\
0 < \\kappa \\ll 1\
$$\
\
$$\
T \_ {0} (\\kappa) = T \_ {0} \\left(\\kappa , \\hat {\\mathrm {C}}\\right) \\gg 0\
$$\
\
$$\
t \_ {0} \\geq T \_ {0} (\\kappa)\
$$\
\
$$\
\\mathrm {C} \_ {0} = \\mathrm {C} \_ {0} \\left(t \_ {0}\\right) \\in \\mathfrak {M} \_ {\\sigma}\
$$\
\
(4.2.22)\
\
$$\
\\left{ \\begin{array}{l} \[ \\mathrm {C} (t \_ {0}) \] \\in U \_ {\\mathrm {C} \_ {0}} (\\kappa^ {2}) \ E \_ {\\hat {\\mathrm {C}}} (\[ T \_ {0} (\\kappa), \\infty)) \\leq \\kappa^ {6}, \\forall t \\geq T \_ {0} (\\kappa). \ \| S W (\[ \\mathrm {C} (t) \]) \| \_ {L ^ {2}} ^ {2} < \\kappa^ {6} \\end{array} \\right.\
$$\
\
**Fix** _t0 ‚ T0(•_) and deflne\
n\
\
$$\
t \_ {0} \\geq T \_ {0} (\\kappa)\
$$\
\
$$\
\\begin{array}{l} T \_ {\\kappa} \\left(t \_ {0}\\right) := \\sup \\left{\\tau > 0; \[ C \\left(t \_ {0} + t\\right)\] \\in U \_ {C \_ {0} \\left(t \_ {0}\\right)} (\\kappa), \\forall t \\in \[ 0, \\tau \] \\right} \ = \\sup \\left{T > 0; \| V \\left(t \_ {0} + t\\right) \| \_ {2, 2} \\leq \\kappa , \\forall t \\in \[ 0, T \] \\right} \ \\end{array}\
$$\
\
where V(t) is determined as above by placing C^ in _•_-standard gauge at C0\
over the time interval for which this is possible. Roughly speaking, _T_• _(t0)_ is\
the length of the time interval, beginning at _t0,_ during which the orbit \[C(t)\]\
stays _•_-close to \[C0\]:= \[C0(t0)\]. We want to get more precise information\
about the size of\
¡ ¢\
\
$$\
\\mathrm {V} (t)\
$$\
\
$$\
\\hat {C}\
$$\
\
$$\
\\mathrm {C} \_ {0}\
$$\
\
$$\
T \_ {\\kappa} \\left(t \_ {0}\\right)\
$$\
\
$$\
t \_ {0}\
$$\
\
$$\
\[ \\mathrm {C} (t) \]\
$$\
\
$$\
\[ \\mathrm {C} \_ {0} \] := \[ \\mathrm {C} \_ {0} \\left(t \_ {0}\\right) \]\
$$\
\
$$\
\\operatorname {d i s t} \_ {2, 2} \\left(\\left\[ \\mathrm {C} \\left(t \_ {0} + t\\right) \\right\], \\left\[ \\mathrm {C} \_ {0} \\right\]\\right)\
$$\
\
for 0 _• t • T_•(t0).\
\
$$\
0 \\leq t \\leq T \_ {\\kappa} \\left(t \_ {0}\\right)\
$$\
\
One of the main advantages of working in standard gauges comes from\