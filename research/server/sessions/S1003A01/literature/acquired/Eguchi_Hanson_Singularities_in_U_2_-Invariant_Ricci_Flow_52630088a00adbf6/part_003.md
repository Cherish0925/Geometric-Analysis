---
retention_scope: session
part: 3
total_parts: 7
---

[Part 3/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

\\begin{aligned} T\_1 = a\_s - 2 + 2Q^2 \\ge 0 \\end{aligned}\
\
is preserved. Thus we only need to show that T\_4\\ge 0 is preserved whenever the Ricci flow satisfies T\_1 \\ge 0. The evolution equation of T\_4 is\
\
\\begin{aligned} \\partial \_t T\_4 = L\[T\_4\] + \\frac{1}{b^2}\\Big (b\_s\\big (5Q^3-2b\_s\\big ) -2 T\_4\\big (4Q^2 - 2Q b\_s +b\_s^2\\big ) \\Big ). \\end{aligned}\
\
A computation shows\
\
\\begin{aligned} \\frac{1}{2}Qb\_s = T\_1 - T\_4 + 1 - Q^2. \\end{aligned}\
\
By the assumption y \\le 0 we have\
\
\\begin{aligned} \\frac{Q^2}{2} \\ge \\frac{1}{2}Qb\_s, \\end{aligned}\
\
and hence it follows that\
\
\\begin{aligned} Q^2 \\ge \\frac{2}{3}\\left( 1-T\_4\\right) . \\end{aligned}\
\
Therefore\
\
\\begin{aligned} 5Q^3 - 2 b\_s \\ge 5 Q^3 - 2Q \\ge Q\\left( \\frac{4}{3} - \\frac{10}{3} T\_4 \\right) , \\end{aligned}\
\
which implies that\
\
\\begin{aligned} \\partial \_t T\_4 \\ge L\[T\_4\] - \\frac{2 T\_4}{b^2}\\left( 4 Q^2 - \\frac{1}{3}Qb\_s + b\_s^2 \\right) \\end{aligned}\
\
since b\_s \\ge 0. Note that the zeroth order coefficient of T\_4 is bounded by Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18). Furthermore \|T\_4\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) yields the desired result. \\square\
\
## 6 Exclusion of Shrinking Solitons\
\
In this section we rule out _U_(2)-invariant shrinking solitons on M\_k, k\\ge 2, within a large class of metrics. In particular, we show\
\
### Theorem 6.1\
\
(No shrinker) On M\_k, k \\ge 2, there does not exist a complete _U_(2)-invariant shrinking Ricci soliton of bounded curvature satisfying the conditions\
\
1. (1)\
\\sup \_{p \\in M\_k} \|b\_s\| < \\infty ;\
\
2. (2)\
T\_1 = a\_s + 2 Q^2 - 2 > 0 for s > 0;\
\
3. (3)\
Q = \\frac{a}{b} \\le 1.\
\
\
This theorem is the key ingredient in Sect. [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec21), where we show that certain Ricci flows on M\_k, k \\ge 3, develop Type II singularities in finite time.\
\
**Soliton equations:** Recall that a shrinking Ricci soliton ( _M_, _g_( _t_)) is a solution to the Ricci flow equation that up to diffeomorphism homothetically shrinks. Such a soliton solution may be written as\
\
\\begin{aligned} g(t) = \\sigma ^2(t) \\Phi ^\*\_t g(0), \\end{aligned}\
\
where\
\
\\begin{aligned} \\sigma (t) = \\sqrt{1 - 2 \\rho t} \\end{aligned}\
\
for some \\rho > 0 and \\Phi \_t is a family of diffeomorphisms. The reader may consult \[ [33](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR33 "Topping, P.: Lectures on the Ricci Flow. London Mathematical Society Lecture Note Series, Vol. 325. Cambridge University Press, Cambridge (2006)")\] for more details. Hence for a _U_(2)-invariant shrinking Ricci soliton (M\_k, g(t)), k \\ge 1, the corresponding warping functions can be written as\
\
\\begin{aligned} a(s,t)&= \\sigma (t)a\\left( \\frac{s}{\\sigma (t)},0\\right) , \\end{aligned}\
\
(6.1)\
\
\
\\begin{aligned} b(s,t)&= \\sigma (t)b\\left( \\frac{s}{\\sigma (t)},0\\right) . \\end{aligned}\
\
(6.2)\
\
\
The above formulae are with respect to the radial coordinate _s_, which is equivalent to fixing a gauge. For this reason the family of diffeomorphisms \\Phi \_t does not appear explicitly. Differentiating with respect to _t_ at time 0 yields\
\
\\begin{aligned} \\partial \_t\|\_{t=0} a(s,t)&= a\_s(s,0)\\left( \\frac{\\partial s}{\\partial t} + \\rho s \\right) - \\rho a(s,0) \\\&= a\_s(s,0) f\_s - \\rho a(s,0), \\end{aligned}\
\
where f: M\_k \\rightarrow {\\mathbb {R}} is the potential function satisfying\
\
\\begin{aligned} f\_{ss} = \\rho + \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b} \\end{aligned}\
\
and we used the expression ( [2.15](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ21)) for \\frac{\\partial s}{\\partial t} derived in Sect. [2.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec12). Similarly we obtain\
\
\\begin{aligned} \\partial \_t\\big \|\_{t=0} b(s,t) = b\_s(s,0) f\_s(s) - \\rho b(s,0). \\end{aligned}\
\
Substituting the expressions \\partial \_t a and \\partial \_t b from the Ricci flow equations ( [2.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ17)) and ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)), respectively, we see that the soliton equations for the warping functions _a_ and _b_ at time t=0 read (c.f. \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)")\])\
\
\\begin{aligned}{} & {} f\_{ss} = \\frac{a\_{ss}}{a}+ 2 \\frac{b\_{ss}}{b} + \\rho , \\end{aligned}\
\
(6.3)\
\
\
\\begin{aligned}{} & {} \\displaystyle a\_{ss} = 2 \\frac{a^3}{b^4} - 2 \\frac{a\_sb\_s}{b} + a\_s f\_s - \\rho a, \\end{aligned}\
\
(6.4)\
\
\
\\begin{aligned}{} & {} \\displaystyle b\_{ss} = \\frac{4}{b} - 2\\frac{a^2}{b^3} - \\frac{a\_sb\_s}{a} - \\frac{b^2\_s}{b} + b\_s f\_s - \\rho b. \\end{aligned}\
\
(6.5)\
\
\
In a slight abuse of notation we will denote _a_ and _b_ as functions of _s_ only when we are considering Ricci solitons. In that case _a_ and _b_ should be interpreted as the initial data _a_( _s_, 0) and _b_( _s_, 0) at time zero that leads to a Ricci soliton solution, via the correspondence ( [6.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ50)) and ( [6.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ51)).\
\
### Remark 6.2\
\
The above shows that all _U_(2)-invariant Ricci solitons on M\_k are automatically gradient Ricci solitons with potential function _f_.\
\
**Evolution of**{\\varvec{x}}, {\\varvec{y}} **and**{\\varvec{Q}} **on soliton background:** Since _x_, _y_ and _Q_ are _scale-invariant_ quantities, their evolution on a Ricci soliton background can be expressed as follows:\
\
\\begin{aligned} x(s, t)&= x\\left( \\frac{s}{\\sigma (t)},0\\right) , \\\ y(s, t)&= y\\left( \\frac{s}{\\sigma (t)},0\\right) ,\\\ Q(s, t)&= Q\\left( \\frac{s}{\\sigma (t)},0\\right) , \\end{aligned}\
\
Differentiating, we therefore obtain\
\
\\begin{aligned} \\partial \_t\\big \|\_{t=0} x(s,t)&= x\_s(s,0) f\_s(s), \\\ \\partial \_t\\big \|\_{t=0} y(s,t)&= y\_s(s,0) f\_s(s), \\\ \\partial \_t\\big \|\_{t=0} Q(s,t)&= Q\_s(s,0) f\_s(s). \\end{aligned}\
\
With help of the evolution equations ( [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ42)), ( [A.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ109)) and ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) for _x_, _y_ and _Q_, this yields the following ordinary differential equations for _x_, _y_ and _Q_ at time zero on a soliton background\
\
\\begin{aligned} 0&= x\_{ss} + \\left( 2\\frac{b\_s}{b}-\\frac{a\_s}{a}- f\_s\\right) x\_s - \\frac{1}{b^2}\\left( 2 Q^2 \\big (2x + y^2\\big ) + 2 y^2\\left( 2 + x\\right) \\right) ,\\end{aligned}\
\
(6.6)\
\
\
\\begin{aligned} 0&= y\_{ss} + \\left( \\frac{a\_s}{a} - f\_s\\right) y\_s -\\frac{y}{a^2} \\left( \\left( x+2\\right) ^2 + Q^2 \\big (2x + y^2 \\big )\\right) , \\end{aligned}\
\
(6.7)\
\
\
\\begin{aligned} 0&= Q\_{ss} + \\left( 3\\frac{b\_s}{b} - f\_s\\right) Q\_s + \\frac{4}{b^2}Q\\big (1-Q^2\\big ). \\end{aligned}\
\
(6.8)\
\
\
Alternatively these equations can be derived from the soliton equations ( [6.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ52))–( [6.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ54)). In a slight abuse of notation we will often denote _x_, _y_ and _Q_ as functions of _s_ only when we are considering Ricci solitons.\
\
**Exclusion of shrinking solitons:** By \[ [12](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR12 "Cao, H.D., Zhou, D.T.: On complete gradient shrinking Ricci solitons. J. Differ. Geom. 85(2), 175–185 (2010)")\] we know that the potential function of a non-compact complete shrinking Ricci soliton grows quadratically with the distance to some fixed point. In our setting this translates into the following lemma:\
\
### Lemma 6.3\
\
Let (M\_k, g), k \\ge 1, be a complete non-compact shrinking Ricci soliton of bounded curvature. Then\
\
\\begin{aligned} f&\\sim \\frac{\\rho }{2} s^2,\\quad f\_s\\sim \\rho s \\end{aligned}\
\
as s\\rightarrow \\infty .\
\
### Proof\
\
See Theorem 1.1, Eqs. (2.3) and (2.8) of \[ [12](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR12 "Cao, H.D., Zhou, D.T.: On complete gradient shrinking Ricci solitons. J. Differ. Geom. 85(2), 175–185 (2010)")\]. \\square\
\
This allows us to prove the following lemma:\
\
### Lemma 6.4\
\
Let (M\_k, g), k \\ge 1, be a complete non-compact shrinking Ricci soliton of bounded curvature with Q \\le 1 on M\_k. Then Q\_s \\ge 0 on M\_k.\
\
### Proof\
\
First notice that for a complete shrinking Ricci soliton with Q \\le 1, the strong maximum principle applied to the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ forces\
\
\\begin{aligned} Q < 1 \\quad \\text {for } \\, s \\ge 0, \\end{aligned}\
\
as otherwise we would have Q=1 everywhere, which cannot be the case. Similarly,\
\
\\begin{aligned} Q > 0, \\end{aligned}\
\
unless we are at the origin s=0. By Eq. ( [6.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ57)) we have\
\
\\begin{aligned} Q\_{ss} = \\left( f\_s - 3 \\frac{b\_s}{b}\\right) Q\_s - \\frac{4}{b^2}Q\\big (1-Q^2\\big ). \\end{aligned}\
\
(6.9)\
\
\
We now argue by contradiction. Assume there exists an s\_{\*} > 0 such that Q\_s(s\_{\*}) < 0. Then Q\_s(s) < 0 for all s> s\_{\*}, because at any extremum of _Q_ we have Q\_s = 0 and\
\
\\begin{aligned} Q\_{ss} = - \\frac{4}{b^2} Q \\big (1 - Q^2 \\big ) < 0. \\end{aligned}\
\
Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) shows that \\frac{b\_s}{b} is bounded and from Lemma [6.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar54) it follows that\
\
\\begin{aligned} f\_s \\rightarrow \\infty \\quad \\text {as } \\, s \\rightarrow \\infty . \\end{aligned}\
\
Therefore eventually\
\
\\begin{aligned} f\_s - 3 \\frac{b\_s}{b} > 0, \\end{aligned}\
\
from which it follows by Eq. ( [6.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ58)) that\
\
\\begin{aligned} Q\_{ss} <0 \\end{aligned}\
\
for sufficiently large _s_. This, however, contradicts that Q > 0 unless s=0. \\square\
\
In the lemma below we bound the term\
\
\\begin{aligned} G := (x+2)^2 + Q^2(2x+y^2), \\end{aligned}\
\
which appears in the evolution equation ( [6.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ56)) of _y_, away from zero.\
\
### Lemma 6.5\
\
Whenever Q\_s \\ge 0 and Q, T\_1 > 0 we have G > 0.\
\
### Proof\
\
We have\
\
\\begin{aligned} \\frac{Q\_s}{Q} = \\frac{a\_s}{a}-\\frac{b\_s}{b} = \\frac{x}{a} - \\frac{y}{b} + \\frac{2}{a} - \\frac{2a}{b^2}. \\end{aligned}\
\
For Q\_s \\ge 0  it follows that\
\
\\begin{aligned} x - Q y \\ge 2\\big (Q^2 - 1\\big ). \\end{aligned}\
\
Recall the quantity\
\
\\begin{aligned} T\_1 = a\_s + 2 Q^2 - 2 \\end{aligned}\
\
defined in Sect. [5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec16). Then\
\
\\begin{aligned} G&\\ge \\left( x+2\\right) ^2 + Q^2 \\left( 2\\left( Qy + 2\\big (Q^2 - 1\\big ) \\right) + y^2\\right) \\\&= x^2 + 4x + 4 + 2 Q^3 y + 4Q^4 - 4Q^2 + Q^2 y^2 \\\&=\\big ( a\_s + Q^2 -2 \\big )^2 + 4\\big ( a\_s + Q^2 -2 \\big ) + 4 + 3 Q^4 - 4 Q^2 + Q^2\\big (y + Q\\big )^2 \\\&=a\_s^2 + 2 Q^2 a\_s + 4\\big (Q^4 - Q^2\\big ) + Q^2 \\left( y + Q\\right) ^2 \\\&=a\_s^2 + 2Q^2 T\_1 + Q^2 \\left( y + Q \\right) ^2 \\\&=a\_s^2 + Q^2 b\_s^2 + 2 Q^2 T\_1 > 0. \\end{aligned}\
\
\\square\
\
Now we prove the non-existence of shrinking solitons.\
\
### Proof of Theorem 6.1\
\
We argue by contradiction. Assume such a shrinking Ricci soliton exists. Applying L’Hôpital’s Rule to the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ shows that at s=0\
\
\\begin{aligned} \\partial \_t b \\big \| \_{s=0}&= 2 b\_{ss} - \\frac{4}{b}\\\&= 2 \\left( y\_s + \\frac{k-2}{b}\\right) . \\end{aligned}\
\
Clearly, every shrinking soliton satisfies\
\
\\begin{aligned} \\partial \_t b \\big \|\_{s=0} < 0. \\end{aligned}\
\
The boundary conditions ( [1.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ3)) of _a_ and _b_ at s=0 imply that\
\
\\begin{aligned} y(0) = 0, \\end{aligned}\
\
and thus we deduce from the above that\
\
\\begin{aligned} y\_s(0) < 0, \\end{aligned}\
\
as k \\ge 2 by assumption. The ordinary differential equation ( [6.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ56)) for _y_ can be written as\
\
\\begin{aligned} y\_{ss} = \\bigg (f\_s - \\frac{a\_s}{a} \\bigg )y\_s + \\frac{y}{a^2} G. \\end{aligned}\
\
(6.10)\
\
\
Lemmas [6.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar56) and [6.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar58) imply that\
\
\\begin{aligned} G> 0\\quad \\text { for }\\, s > 0, \\end{aligned}\
\
which in turn shows that y\_s \\le 0 everywhere, as at a negative local minimum of _y_ we would have\
\
\\begin{aligned} y\_{ss} = \\frac{y}{a^2} G < 0. \\end{aligned}\
\
The asymptotic properties of _f_ listed in Lemma [6.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar54) and the bounds on \\frac{a\_s}{a} proven in Lemma [3.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar20) show that eventually\
\
\\begin{aligned} f\_s - \\frac{a\_s}{a} > 0, \\end{aligned}\
\
and hence from Eq. ( [6.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ59)) it follows that\
\
\\begin{aligned} y\_{ss} < 0 \\end{aligned}\
\
for _s_ sufficiently large. From this it follows that\
\
\\begin{aligned} \\lim \_{s \\rightarrow \\infty } y = \\lim \_{s \\rightarrow \\infty } \\left( b\_s - Q \\right) = - \\infty , \\end{aligned}\
\
which contradicts our assumptions on b\_s and _Q_. \\square\
\
## 7 Curvature Bound\
\
The aim of this section is to prove that a Ricci flow (M\_k, g(t)), k \\in {\\mathbb {N}}, t\\in \[0,T), starting from an initial metric g(0) \\in {\\mathcal {I}}—where {\\mathcal {I}} is a class of metrics to be discussed below—with \\sup \_{p \\in M\_k} b(p,0) < \\infty  satisfies the curvature bound\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le C\_1 b^{-2} \\quad \\text { for } \\, t \\in (0,T), \\end{aligned}\
\
where C\_1>0 is some constant. This allows us to control the geometry via the warping function _b_, which will be crucial for constructing blow-up limits in the following parts of the paper. Note that this bound was already derived in the compact case in \[ [24](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR24 "Isenberg, J., Knopf, D., Sesum, N.: Non-Kähler Ricci flow singularities that converge to Kähler–Ricci solitons,                    arXiv:1703.02918v2                                     (2017)")\] and we will follow their strategy to prove it in our non-compact setting.\
\
Recall the following two definitions (see also \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Definition 8.23\]):\
\
### Definition 7.1\
\
(\\kappa -collapsing) A Ricci flow ( _M_, _g_( _t_)), t \\in \[0,T), is \\kappa -collapsed at a point (p\_0, t\_0) in spacetime at scale r > 0 if\
\
- (bounded normalized curvature) \|\\textrm{Rm}(p,t)\| \\le r^{-2} for every p \\in B\_{g(t\_0)}(p\_0,r) and t \\in \[ \\max \\{t\_0 - r^2, 0 \\}, t\_0\];\
\
- (non collapsed volume)\
\
\
\
\\begin{aligned} \\text {vol}\_{g(t\_0)} B\_{g(t\_0)}(p\_0, r) < \\kappa r^4. \\end{aligned}\
\
\
### Definition 7.2\
\
(\\kappa -non-collapsing) A Ricci flow ( _M_, _g_( _t_)), t \\in \[0,T), is \\kappa -non-collapsed at scale r > 0 if for any p\_0 \\in M and t\_0 \\in \[r^2, T) the solution is not \\kappa -collapsed at point (p\_0, t\_0) at scale r > 0.\
\
We now define the class of metrics {\\mathcal {I}}.\
\
### Definition 7.3\
\
For K>0 let {\\mathcal {I}}\_K be the set of all complete _bounded curvature_ metrics of the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)) on M\_k, k \\ge 1, with _positive injectivity radius_ that satisfy the following scale-invariant inequalities:\
\
\\begin{aligned}&Q \\le 1, \\end{aligned}\
\
(7.1)\
\
\
\\begin{aligned}&a\_s, b\_s \\ge 0, \\end{aligned}\
\
(7.2)\
\
\
\\begin{aligned}&y \\le 0, \\end{aligned}\
\
(7.3)\
\
\
\\begin{aligned}&\\sup a\_s < K, \\end{aligned}\
\
(7.4)\
\
\
\\begin{aligned}&\\sup \|b b\_{ss}\| < K. \\end{aligned}\
\
(7.5)\
\
\
Denote by {\\mathcal {I}} the set of metrics _g_ such that for sufficiently large K>0 we have g\\in {\\mathcal {I}}\_K.\
\
Note that for any k \\in {\\mathbb {N}} the set {\\mathcal {I}} of metrics on M\_k is non-empty, as for example the metric on M\_k defined by\
\
\\begin{aligned} a(s)&= Q = \\tanh (k s), \\quad k \\in {\\mathbb {N}}, \\\ b(s)&= 1 \\end{aligned}\
\
is contained in {\\mathcal {I}}. In Lemma [7.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar72) below we show that if g(0) \\in {\\mathcal {I}}\_{K\_0} for some K\_0>0 then there exists a K> K\_0 such that g(t)\\in {\\mathcal {I}}\_K for t \\in \[0, T). Note that conditions ( [7.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ60))–( [7.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ64)) are scale-invariant, and therefore pass to blow-up limits.\
\
An adaptation of \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Theorem 8.26\] to our setting yields the following result:\
\
### Theorem 7.4\
\
(No local collapsing)  Let _g_( _t_), t \\in \[0,T), T< \\infty , be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}}. Then there exists a \\kappa >0 depending on _T_, {\\textrm{inj}}(g(0)) and \\sup \_{M \\times \[0, T/2\]} \\textrm{Ric}\_{g(t)} such that _g_( _t_) is \\kappa -non-collapsed at every (p,t) \\in M\\times (\\frac{T}{2}, T) at every scale \\rho < \\sqrt{T/2}.\
\
### Proof\
\
Note that by \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Lemma 6.54 (ii)\], the positive injectivity radius and bounded curvature of _g_(0) implies the lower volume bound (2) of \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Theorem 8.26\]. Since _g_(0) has bounded curvature, Condition (1) is also met by Shi’s theorem \[ [32](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR32 "Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. 30(1), 223–301 (1989)")\]. \\square\
\
### Remark 7.5\
\
Recall that if a Ricci flow _g_( _t_) is \\kappa -non-collapsed at scale \\rho , then the parabolically dilated Ricci flow \\alpha ^2 g( \\alpha ^{-2} t) is \\kappa -non-collapsed at scale \\alpha \\rho . As the \\kappa -non-collapsedness property is preserved under Cheeger–Gromov limits, a blow-up limit of a Ricci flow (M\_k, g(t)), \[0, T\_\\textrm{sing}) is \\kappa -non-collapsed at all scales.\
\
Having set up the necessary terminology, we may now state the main theorem of this section:\
\
### Theorem 7.6\
\
(Curvature bound)  Let (M\_{k}, g(t)), t \\in \[0, T), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) with\
\
\\begin{aligned} \\sup \_{p \\in M\_k} b(p,0) < \\infty . \\end{aligned}\
\
Then there exists a constant C\_1 > 0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}(p) \\le C\_1 b^{-2}(p,t) \\end{aligned}\
\
for (p,t) \\in M\_k \\times (0,T).\
\
A useful variant of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) is:\
\
### Corollary 7.7\
\
Let (M\_{k}, g(t)) with g(t) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) for t \\in (-\\infty , 0\] be an ancient Ricci flow solution which is \\kappa -non-collapsed at all scales. Then there exists a constant C\_1 > 0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}(p) \\le C\_1 b^{-2}(p,t) \\end{aligned}\
\
for (p,t) \\in M\_k \\times (-\\infty , 0\].\
\
### Remark 7.8\
\
Corollary [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar68) follows immediately from Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) for ancient \\kappa -non-collapsed Ricci flows that arise as blow up limits of Ricci flows (M\_k, g(t)), t \\in \[0, T\_\\textrm{sing}), g(0) \\in {\\mathcal {I}}, as the curvature bound is scale-invariant. Nevertheless, we give a proof of the general case.\
\
Let us now prove the assertions made above. We begin with the following lemma:\
\
### Lemma 7.9\
\
Let K\_0 > 0 and assume that (M\_k,g(t)), k \\ge 1, t\\in \[0,T), is a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}}\_{K\_0}. Then there exists a constant K \\ge 0, depending only on the initial metric _g_(0), such that\
\
\\begin{aligned} \|bb\_{ss}\| \\le K \\end{aligned}\
\
(7.6)\
\
\
on M\_k \\times \[0,T).\
\
### Proof\
\
We follow the proof strategy of \[ [24](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR24 "Isenberg, J., Knopf, D., Sesum, N.: Non-Kähler Ricci flow singularities that converge to Kähler–Ricci solitons,                    arXiv:1703.02918v2                                     (2017)"),  Lemma 7\]. Consider the quantities\
\
\\begin{aligned} H\_-&= b b\_{ss} + a\_s^2 - b\_s^2 - C, \\\ H\_+&= b b\_{ss} - a\_s^2 - b\_s^2 + C, \\end{aligned}\
\
where C > 0 is a constant to be determined later. The goal is to show that the inequalities H\_+ \\ge 0 and H\_- \\le 0 are preserved by the Ricci flow for sufficiently large C> 0. The quantities H\_\\pm  satisfy the evolution equations\
\
\\begin{aligned} \\partial \_t H\_\\pm&= \[H\_\\pm \]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_\\pm \]\_s +H\_\\pm \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad \\pm C \\left( \\frac{2 a\_s^2}{a^2}+\\frac{4 a^2}{b^4}+\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad \\pm 2 a\_{ss}^2 + a\_{ss} \\left( -\\frac{2 b a\_s b\_s}{a^2} \\mp \\frac{8 a\_s b\_s}{b} \\pm \\frac{4 a\_s^2}{a}+\\frac{4a}{b^2}\\right) \\\&\\quad +\\frac{2 b a\_s^3 b\_s}{a^3}-\\frac{32 a a\_sb\_s}{b^3}\\mp \\frac{16 a^3 a\_s b\_s}{b^5}+\\frac{4 a\_s^2}{b^2} \\pm \\frac{8 a^2a\_s^2}{b^4} \\\&\\quad \\mp \\frac{2 a\_s^4}{a^2} +\\frac{32 a^2 b\_s^2}{b^4}-\\frac{16 b\_s^2}{b^2}. \\end{aligned}\
\
In Appendix A we carry out the derivation of the evolution equation. We now show that H\_- \\le 0 is preserved. Using Young’s inequality to bound the terms involving a\_{ss} and then disregarding non-positive terms not involving _C_, we obtain\
\
\\begin{aligned} \\partial \_t H\_-&\\le \[H\_-\]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_-\]\_s +H\_- \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad -C \\left( \\frac{2 a\_s^2}{a^2}+\\frac{4 a^2}{b^4}+\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad +\\frac{1}{2}\\left( \\left( \\frac{2 b a\_s b\_s}{a^2}\\right) ^2+ \\left( \\frac{8 a\_s b\_s}{b}\\right) ^2 +\\left( \\frac{4 a\_s^2}{a}\\right) ^2+\\left( \\frac{4a}{b^2}\\right) ^2\\right) \\\&\\quad +\\frac{2 b a\_s^3 b\_s}{a^3}+\\frac{16 a^3 a\_s b\_s}{b^5}+\\frac{4 a\_s^2}{b^2}+\\frac{2 a\_s^4}{a^2} +\\frac{32 a^2 b\_s^2}{b^4}. \\end{aligned}\
\
Recall that on M\_k \\times \[0,T) we have y = b\_s - Q \\le 0 , Q \\le 1, a\_s,b\_s \\ge 0 and a\_s \\le C' for some C'>0 by Lemma [5.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar38), Lemma [5.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar33), Lemma [5.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar40) and Lemma [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar42), respectively. Therefore we obtain the following bounds away from the non-principal orbit S^2\_o:\
\
\\begin{aligned}{} & {} \\left( \\frac{2b a\_s b\_s}{a^2}\\right) ^2 = \\left( \\frac{2 a\_s b\_s}{a Q} \\right) ^2 \\le \\frac{4 a\_s^2}{a^2}, \\\{} & {} \\left( \\frac{8 a\_s b\_s}{b} \\right) ^2 = \\left( 8\\frac{a\_s}{a} Qb\_s\\right) ^2 \\le 64 \\frac{a\_s^2}{a^2}, \\\{} & {} \\left( \\frac{4 a\_s^2}{a}\\right) ^2 = 16 C'^2 \\frac{a\_s^2}{a^2}, \\\{} & {} \\frac{2 b a\_s^3 b\_s}{a^3} = \\frac{ 2a\_s^3}{a^2} \\frac{b\_s}{Q} \\le 2 C' \\frac{a\_s^2}{a^2}, \\\{} & {} \\frac{16 a^3 a\_s b\_s}{b^5} = 16 Q^3 \\frac{a\_sb\_s}{b^2} \\le 8Q^3 \\left( \\frac{a\_s^2}{b^2} + \\frac{b\_s^2}{b^2} \\right) \\le 8\\left( \\frac{a\_s^2}{a^2} + \\frac{b\_s^2}{b^2} \\right) , \\\{} & {} \\frac{4 a\_s^2}{b^2} \\le 4 \\frac{a\_s^2}{a^2}, \\\{} & {} \\frac{2 a\_s^4}{a^2} \\le 2 C'^2 \\frac{a\_s^2}{a^2}, \\\{} & {} \\frac{32 a^2 b\_s^2}{b^4} = 32 Q^2 \\frac{b\_s^2}{b^2} \\le 32 \\frac{b\_s^2}{b^2}. \\end{aligned}\
\
Hence for a sufficiently large C>0 it follows that\
\
\\begin{aligned} \\partial \_t H\_-&\\le \[H\_-\]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_-\]\_s + H\_- \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\end{aligned}\
\
away from the non-principal orbit S^2\_o. Switching to coordinates ( _s_, _t_) we see that for s > 0\
\
\\begin{aligned} \\partial \_t\|\_{s} H\_-&\\le \[H\_-\]\_{ss} + \\bigg (\\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\bigg ) \[H\_-\]\_s + H\_- \\bigg (-\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2} - \\frac{\\partial s}{\\partial t} \\bigg ). \\end{aligned}\
\
(7.7)\
\
\
On the non-principal orbit S^2\_o, or equivalently when s=0, we have\
\
\\begin{aligned} H\_- = bb\_{ss} + k^2 - C \\le bQ\_s +k^2 - C \\le k + k^2 -C, \\end{aligned}\
\
where we used that y = b\_s - Q \\le 0 with equality at s = 0. Choosing C>k^2 + k we have H\_- < 0 on \\{s = 0\\} \\times \[0,T). Hence for every T' \\in \[0, T) there exists a s\_0 > 0 such that\
\
\\begin{aligned} H\_-(s,t) \\le 0 \\quad \\text { on } \\, \[0,s\_0\] \\times \[0, T'\], \\end{aligned}\
\
as H\_-(s,t) is a smooth function on {\\mathbb {R}}\_{\\ge 0} \\times \[0, T'\]. Furthermore note that\
\
\\begin{aligned} \|H\_-\|\\le \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} b^2 + C'^2 + 1 + C, \\end{aligned}\
\
where we used the expression for the curvature component R\_{0202} derived in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11). This shows that for each time t < T' the function H\_-(s,t) grows subexponentially. Note that by Lemmas [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) and [3.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar20) the coefficient\
\
\\begin{aligned} \\frac{a\_s}{a} -2 \\frac{b\_s}{b} \\end{aligned}\
\
is bounded on \[s\_0, \\infty ) \\times \[0, T'\]. Similarly, we see from the bound ( [3.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ28)) on \|\\frac{\\partial s}{\\partial t}\| presented in the proof of the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17), Case 1, that the coefficient\
\
\\begin{aligned} -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2} - \\frac{\\partial s}{\\partial t} \\end{aligned}\
\
grows at most linearly on every times slice of \[s\_0, \\infty ) \\times \[0, T'\]. Therefore, applying the weak maximum principle to the evolution equation ( [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ66)) of H\_- on the parabolic neighborhood \[s\_0, \\infty ) \\times \[0,T'\], we deduce that\
\
\\begin{aligned} H\_- \\le 0 \\quad \\text { on } \\, M\_k \\times \[0, T'\]. \\end{aligned}\
\
As T' \\in \[0, T) was arbitrary it follows that H\_-\\le 0 is preserved by the Ricci flow.\
\
We repeat the same process to prove that H\_+ \\ge 0 is preserved. Applying Young’s inequality to bound terms involving a\_{ss} and then disregarding non-negative terms not involving _C_, we see that\
\
\\begin{aligned} \\partial \_t H\_+&\\ge \[H\_+\]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_+\]\_s +H\_+ \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad + C \\left( \\frac{2 a\_s^2}{a^2}+\\frac{4 a^2}{b^4}+\\frac{4b\_s^2}{b^2}\\right) \\\&\\quad -\\frac{1}{2}\\left( \\left( \\frac{2 b a\_s b\_s}{a^2}\\right) ^2+ \\left( \\frac{8 a\_s b\_s}{b}\\right) ^2 +\\left( \\frac{4 a\_s^2}{a}\\right) ^2+\\left( \\frac{4a}{b^2}\\right) ^2\\right) \\\&\\quad -\\frac{32 a a\_sb\_s}{b^3}-\\frac{16 a^3 a\_s b\_s}{b^5}- \\frac{2 a\_s^4}{a^2} -\\frac{16 b\_s^2}{b^2}. \\end{aligned}\
\
Bounding the zeroth order terms via Young’s inequality as above, we see that for C>0 sufficiently large\
\
\\begin{aligned} \\partial \_t H\_+&\\ge \[H\_+\]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_+\]\_s +H\_+ \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\end{aligned}\
\
away from the non-principal orbit S^2\_o. On the non-principal orbit S^2\_o we have\
\
\\begin{aligned} H\_+ = bb\_{ss} - k^2 + C \\ge - k^2 + C, \\end{aligned}\
\
where we used that b\_s \\ge 0 with equality at s =0 to deduce that b\_{ss} \\ge 0 at s = 0. From here the above proof that H\_- \\le 0 is preserved carries over and we may conclude that H\_+ \\ge 0 is preserved as well. Recalling the bounds on a\_s and b\_s, the desired result now follows. \\square\
\
Now we can prove that {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) is preserved by Ricci flow:\
\
### Lemma 7.10\
\
Let K\_0 > 0. Then there exists a K \\ge K\_0 such that the following holds: Let (M\_k,g(t)), k \\ge 1, t \\in \[0,T), be a Ricci flow solution starting from an initial metric g(0) \\in {\\mathcal {I}}\_{K\_0}. Then g(t) \\in {\\mathcal {I}}\_K for every t \\in \[0,T).\
\
### Proof\
\
By Lemmas [5.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar33), [5.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar40), [5.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar38), [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar42) we see that for K > 2 the conditions ( [7.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ60))–( [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ63)) are preserved. By Lemma [7.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar70) we see that there exists a K \\ge K\_0 such that inequality ( [7.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ64)) holds for t \\in \[0,T).\
\
Now we only need to prove that for every time t \\in \[0, T) the metric _g_( _t_) has bounded curvature and positive injectivity radius. Note that by Shi’s Theorem \[ [32](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR32 "Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. 30(1), 223–301 (1989)")\] for every time T' \\in \[0,T) the Ricci flow _g_( _t_) has bounded curvature on the time interval \[0,T'\], since g(0) \\in {\\mathcal {I}}\_K has bounded curvature. As {\\textrm{inj}}\_{g(0)} > 0 and \|\\textrm{Rm}\_{g(0)}\| < \\infty , the metric _g_(0) is non-collapsed by \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Lemma 6.54 (ii)\]. Standard volume distortion estimates under Ricci flow then show that for each t \\in \[0, T/2\] the metric _g_( _t_) is non-collapsed. By Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) there exists a \\kappa >0 and \\rho >0 such that for each t \\in \[0,T) the metric _g_( _t_) is \\kappa -non-collapsed at scale \\rho < \\sqrt{T/2}. Hence it follows from \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Lemma 6.54 (i)\] that {\\textrm{inj}}\_{g(t)} > 0 for all t \\in \[0, T). \\square\
\
Before proving Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67), we need to prove the following two lemmas in preparation:\
\
### Lemma 7.11\
\
Let (M\_k,g(t)), k \\ge 1, t\\in \[0,T), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}}. Then there exists a constant C\_0 \\ge 0, depending only on the initial metric _g_(0), such that\
\
\\begin{aligned} \|\\partial \_t b^2\| \\le C\_0. \\end{aligned}\
\
(7.8)\
\
\
### Proof\
\
By Lemma [7.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar72) there exists a K> 0 such that g(t) \\in {\\mathcal {I}}\_K for t \\in \[0, T). From the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ and Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63) of {\\mathcal {I}}\_K it follows that\
\
\\begin{aligned} \|\\partial \_t b^2\|&= \\left\| 2 b b\_{ss} - 8 + 4 Q^2 + 2 \\frac{a\_sb\_s}{Q} + 2 b\_s^2\\right\| \\\&\\le 2 K + 8 + 4 + 2 K + 2 \\\&= 4K + 14. \\end{aligned}\
\
This concludes the proof. \\square\
\
### Lemma 7.12\
\
Let (M\_k, g(t)), k \\ge 1, t \\in \[0,T), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}}. Then\
\
\\begin{aligned} \\sup \_{p \\in M\_k} b(p,t) \\le \\sup \_{p \\in M\_k} b(p,0) \\end{aligned}\
\
for all t \\in \[0,T).\
\
### Proof\
\
From the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ and expression ( [2.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ10)) for the Laplacian with respect to the background metric _g_( _t_) it follows\
\
\\begin{aligned} \\partial \_t b^2 = \\Delta \_{g(t)} b^2 - 8 + 4 Q^2 - 4 b\_s^2 \\le \\Delta \_{g(t)} b^2 - 4. \\end{aligned}\
\
Applying the maximum principle \[ [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR10 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)"),  Theorem 12.14\] yields the desired result. \\square\
\
We now proceed to proving Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67).\
\
### Proof of Theorem 7.6\
\
We argue by contradiction. Assume there exists a sequence of points (p\_i, t\_i) in spacetime and constants D\_i \\rightarrow \\infty  as i \\rightarrow \\infty  such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t\_i)}\|\_{g(t\_i)}(p\_i) = D\_i b(p\_i,t\_i)^{-2} := K\_i \\end{aligned}\
\
and\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le D\_i b^{-2} \\quad \\text { on } \\, M\_k \\times \[0, t\_i\]. \\end{aligned}\
\
By the assumption that g(0) \\in {\\mathcal {I}} the initial metric _g_(0) has bounded curvature. Hence by Shi’s theorem \[ [32](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR32 "Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. 30(1), 223–301 (1989)")\] we have that for every T' \\in \[0,T) the metric _g_( _t_) has bounded curvature on M\_k \\times \[0,T'\]. As by Lemma [7.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar76) the warping function _b_ is uniformly bounded on M\_k \\times \[0,T), we thus see that D\_i \\rightarrow \\infty  forces K\_i \\rightarrow \\infty  and therefore t\_i \\rightarrow T.\
\
Consider the rescaled Ricci flows\
\
\\begin{aligned} g\_i(t) = K\_i g \\big ( t\_i + K\_i^{-1} t \\big ), \\quad t \\in \[- K\_i \\Delta t\_i, 0\], \\end{aligned}\
\
where \\Delta t\_i > 0 is to be determined below. As K\_i \\rightarrow \\infty  we see that g\_i(t) are blow-ups rather than blow-downs, which is important for the following reason: By Theorem  [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) there exists a \\kappa >0 such that _g_( _t_) is \\kappa -non-collapsed at every scale p \\le \\sqrt{T/2} at every spacetime point (p,t) \\in M\_k \\times \[T/2, T). As K\_i \\rightarrow \\infty  we see that g\_i(t) are \\kappa -non-collapsed at scales tending to infinity as i \\rightarrow \\infty .\
\
By Lemma [7.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar72) there exists a K>0 such that g(t) \\in {\\mathcal {I}}\_K for all t \\in \[0,T). Furthermore, by Lemma [7.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar74) there exists a C\_0 such that \|\\partial \_t b^2\| \\le C\_0 on M\_k \\times \[0, T). Recall the Definition [2.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar13) of C\_g(p,r). Set\
\
\\begin{aligned} \\Delta t\_i = \\min \\left( \\frac{t\_i}{2}, \\frac{b^2(p\_i, t\_i)}{8 C\_0} \\right) \\end{aligned}\
\
and consider the parabolic neighborhoods\
\
\\begin{aligned} \\Omega \_i = C\_{g(t\_i)}\\left( p\_i, \\frac{b(p\_i,t\_i)}{2}\\right) \\times \[t\_i - \\Delta t\_i, t\_i\]. \\end{aligned}\
\
As g(t) \\in {\\mathcal {I}}\_K for t \\in \[0,T) we have that y = b\_s - Q \\le 0, Q \\le 1 and b\_s \\ge 0 everywhere on M\_k \\times \[0,T). Therefore\
\
\\begin{aligned} b(p, t\_i) \\ge \\frac{b(p\_i, t\_i)}{2} \\quad \\text { on } \\Omega \_i\\cap \\left\\{ t = t\_i\\right\\} . \\end{aligned}\
\
By Lemma [7.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar74)\
\
\\begin{aligned} b^2(p,t\_i) - b^2(p,t) \\le C\_0 (t\_i - t) \\end{aligned}\
\
for all (p,t) \\in \\Omega \_i from which it follows that\
\
\\begin{aligned} \\frac{1}{4} b^2(p\_i, t\_i) - b^2(p,t) \\le b^2(p,t\_i) - b^2(p,t) \\le C\_0 (t\_i - t) \\le C\_0 \\Delta t \\le \\frac{1}{8} b^2(p\_i, t\_i). \\end{aligned}\
\
Thus we deduce that\
\
\\begin{aligned} b^2(p,t) \\ge \\frac{1}{8} b^2(p\_i,t\_i)\\quad \\text { on }\\Omega \_i. \\end{aligned}\
\
(7.9)\
\
\
It follows that for (p,t) \\in \\Omega \_i\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}(p)&\\le D\_i b(p,t)^{-2} \\\&\\le 8 D\_i b(p\_i,t\_i)^{-2} \\\&= 8 K\_i, \\end{aligned}\
\
and hence the curvatures of the rescaled metrics g\_i(t) satisfy\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le 8 \\end{aligned}\
\
on the parabolic neighborhoods \\Omega '\_i\
\
\\begin{aligned} \\Omega '\_i :=C\_{g\_i(0)}\\left( p\_i, \\sqrt{K\_i} \\frac{b(p\_i,t\_i)}{2} \\right) \\times \[-K\_i \\Delta t\_i, 0\]. \\end{aligned}\
\
Note that\
\
\\begin{aligned} K\_i \\Delta t\_i \\rightarrow \\infty \\quad \\,\\text { as }\\, i \\rightarrow \\infty \\end{aligned}\
\
and\
\
\\begin{aligned} \\sqrt{K\_i} \\frac{b(p\_i,t\_i)}{2} \\ge \\frac{\\sqrt{D\_i}}{2} \\rightarrow \\infty \\,\\quad \\text { as } \\, i \\rightarrow \\infty . \\end{aligned}\
\
Hence \\left( C\_{g\_i(t)}(p\_i, \\sqrt{D\_i}/2), g\_i(t), p\_i\\right) , t \\in \[-K\_i \\Delta t\_i, 0\], subsequentially converges, in the Cheeger–Gromov sense, to an ancient pointed Ricci flow (M\_{\\infty }, g\_{\\infty }(t), p\_\\infty ), t \\in (-\\infty , 0\].\
\
### Claim 1\
\
The Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in (-\\infty , 0\], splits as ({\\mathbb {R}}^2 \\times N, g\_\\textrm{Eucl} + g\_N(t)), t \\in (-\\infty , 0\], where g\_\\textrm{Eucl} is the flat Euclidean metric, and (N, g\_N(t)) is a non-compact ancient Ricci flow.\
\
### Proof of Claim 1\
\
Denote by a\_i and b\_i the warping functions of the rescaled metrics g\_i(t). Then by ( [7.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ68)) we see that\
\
\\begin{aligned} b\_i(p, t) \\ge \\sqrt{\\frac{D\_i}{8}}\\quad \\, \\text { on } \\Omega '\_i. \\end{aligned}\
\
(7.10)\
\
\
As D\_i \\rightarrow \\infty , the warping functions b\_i tend to infinity uniformly. As b\_i describes the size of the base S^2 in the Hopf fibration, intuitively one can see that this claim is true. Nevertheless, we provide a formal proof below:\
\
As g(t)\\in {\\mathcal {I}}\_K for t\\in \[0,T) we have\
\
\\begin{aligned} \\left\| -\\frac{b\_{ss}}{b}\\right\| \\le \\frac{K}{b^2}\\quad \\, \\text { on } \\, M\_k \\times \[0, T). \\end{aligned}\
\
Inspecting the curvature components listed in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11), we see that all the curvature components of g\_i(t), apart from R\_{0101}, tend to zero on \\Omega '\_i. Hence the curvature operator of g\_\\infty (t) is of rank 1. Furthermore, as _g_(0) has bounded curvature by the assumption that g(0) \\in {\\mathcal {I}} we see that the scalar curvature R\_{g(t)} is pointwise bounded below by \\inf \_{p \\in M\_k} R\_{g(0)}(p) > - \\infty . Hence the blow-up limit g\_\\infty (t) has non-negative scalar curvature, which in turn implies that the curvature operator is non-negative. By \[ [23](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR23 "Hamilton, R.S.: Four-manifolds with positive curvature operator. J. Differ. Geom. 24(2), 153–179 (1986)"),  8.3. Theorem & p. 178\] we conclude that (M\_\\infty , g\_\\infty (t)) splits as a product ({\\mathbb {R}}^2 \\times N, g\_\\textrm{Eucl} + g\_N(t)). Note also that _N_ is diffeomorphic to the leafs of the distribution spanned by e\_0 and e\_1, as these are the only planes with non-flat sectional curvature. Recalling that e\_0=\\frac{\\partial }{\\partial s} we see that the integral curves of e\_0 are non-compact and therefore _N_ is non-compact as well. \\square\
\
As (M\_\\infty , g\_{\\infty }(t)) is \\kappa -non-collapsed at all scales, the above claim implies that (N, g\_N(t)) is a 2d \\kappa -solution. However, by Hamilton’s work a two dimensional \\kappa -solution is either the shrinking round sphere S^2 or its {\\mathbb {Z}}\_2 quotient \[ [8](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR8 "Chow, B., Lu, P., Ni, L.: Hamilton’s Ricci Flow, Lectures in Contemporary Mathematics, Vol. 3, Science Press and Graduate Studies in Mathematics, Vol. 77, American Mathematical Society (co-publication) (2006)"),  §1 of Chapter 9\]. Since _N_ is non-compact we have arrived at a contradiction. Therefore the desired result follows. \\square\
\
### Proof of Corollary 7.7\
\
The proof is the same as for Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67). Since the Ricci flow is assumed to be \\kappa -non-collapsed at all scales, we may also take blow-down limits and do not need to assume that _b_ is uniformly bounded. Furthermore, since ancient Ricci flows have non-negative scalar curvature, Claim 1 of the proof of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) also carries over. \\square\
\
## 8 Compactness Properties\
\
In this section we prove some compactness properties of _U_(2)-invariant cohomogeneity one Ricci flows. For general Ricci flows the compactness properties are well-known \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"), Chapter 3\]. Therefore the main technical difficulty is to show that the _U_(2)-symmetry passes to the limit.\
\
The main theorem of this section is Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) which roughly states the following compactness property: Let (U\_i, g\_i(t), p\_i), \[-\\Delta t, 0\], be a sequence of _U_(2)-invariant cohomogeneity one manifolds in the class {\\mathcal {I}} of metrics. Here the U\_i are open manifolds and assumed to compactly contain the sets C\_{g\_i(0)}(p\_i, r) (see Definition [2.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar13)) for some fixed r> 0. This condition can be understood as requiring U\_i to have ‘radial diameter’ of at least _r_. Furthermore the metrics g\_i(t) are normalized such that b = 1 at the points (p\_i, 0) in spacetime. We show that if the flows g\_i(t) are \\kappa -non-collapsed and of uniformly bounded curvature, then (U\_i, g\_i(t), p\_i), \[-\\Delta t, 0\], subsequentially converges to a limiting _U_(2)-invariant Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). Moreover, if we correctly pick/normalize the coordinate \\xi , the warping functions u\_i(\\xi , t), a\_i(\\xi ,t) and b\_i(\\xi ,t) of the metrics g\_i(t) converge on compact parabolic sets in C^\\infty  to the warping functions u\_\\infty (\\xi ,t), u\_\\infty (\\xi , t) and b\_\\infty (\\xi ,t) of g\_\\infty (t). This in essence shows that when taking limits of _U_(2)-invariant Ricci flows, we may work with the warping functions only, without having to concern ourselves with the underlying manifold.\
\
Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) has two important applications: Firstly, it implies the corresponding compactness result for complete Ricci flows. In particular, a sequence of uniformly bounded and non-collapsed _U_(2)-invariant cohomogeneity one Ricci flows (M\_k, g\_i(t), p\_i), t \\in \[-t\_i, 0\], t\_i\\rightarrow \\infty , normalized such that b(p\_i, 0) = 1, subsequentially converges, in the Cheeger–Gromov sense, to a limiting Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\infty , 0\], that is also _U_(2)-invariant and cohomogeneity one. Secondly, we prove a variant of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) in Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85), where we specialize to the case in which the ‘radial diameter’ of the U\_i is equal to \\frac{1}{2}. This will allow us to alter one assumption of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) and yield a very useful tool for proving certain scale-invariant inequalities via a contradiction/compactness argument, as introduced in the outline of Sect. [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec20) in Sect. [1.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec6) of this paper.\
\
Below we state the main results of this section. For this recall Definition [2.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar13) of C\_g(p,r), C\_g^+(p,r) and \\Sigma \_p.\
\
### Theorem 8.1\
\
(Local compactness)  Let k \\in {\\mathbb {N}} and \\kappa , \\rho , K, r, \\Delta t > 0. Assume that\
\
\\begin{aligned} (U\_i, g\_i(t), p\_i), \\quad t \\in \\left\[ -\\Delta t, 0\\right\] , \\end{aligned}\
\
is a sequence of pointed cohomogeneity one _U_(2)-invariant Ricci flows satisfying the following properties:\
\
1. (1)\
U\_i is an open _U_(2)-invariant manifold with principal orbit S^3/{\\mathbb {Z}}\_k.\
\
2. (2)\
For t \\in \[-\\Delta t, 0\] we have g\_i(t) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)). Denote by u\_i, a\_i and b\_i the warping functions of g\_i(t).\
\
3. (3)\
The closed sets \\overline{C\_{g\_i(0)}\\left( p\_i, r\\right) } \\subset U\_i are compact.\
\
4. (4)\
b\_i(p\_i,0) = 1.\
\
5. (5)\
The Ricci flow (U\_i, g\_i(t)) is \\kappa -non-collapsed at (p\_i, 0) at scale \\min (\\rho , r, \\sqrt{\\Delta t}).\
\
6. (6)\
\|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le K in U\_i \\times \\left\[ - \\Delta t, 0\\right\] .\
\
\
Then (C\_{g\_i(0)}\\left( p\_i, r \\right) , g\_i(t), p\_i), t \\in \[-\\Delta t, 0\], subsequentially converges, in the Cheeger–Gromov sense, to a pointed Ricci flow\
\
\\begin{aligned} ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), \\quad t \\in \\left\[ - \\Delta t, 0\\right\] , \\end{aligned}\
\
satisfying the following properties:\
\
1. (a)\
{\\mathcal {C}}\_\\infty  is a cohomogeneity one _U_(2)-invariant manifold such that either\
1. (i)\
      All orbits are principal: In this case {\\mathcal {C}}\_\\infty  is diffeomorphic to the cylinder {\\mathbb {R}}\\times S^3/{\\mathbb {Z}}\_k and we equip {\\mathcal {C}}\_\\infty  with a radial coordinate \\xi : {\\mathcal {C}}\_\\infty \\rightarrow {\\mathbb {R}} defined by \\xi (p) = d\_{g\_\\infty (0)}(p, \\Sigma \_{p\_\\infty } ); or\
\
2. (ii)\
      There is exactly one non-principal orbit: In this case {\\mathcal {C}}\_\\infty  is diffeomorphic to M\_k and we equip {\\mathcal {C}}\_\\infty  with the radial coordinate \\xi : {\\mathcal {C}}\_\\infty \\rightarrow {\\mathbb {R}} defined by \\xi (p) = d\_{g\_\\infty (0)}(p, S^2\_o).\
2. (b)\
There exist warping functions\
\
\
\
\\begin{aligned} u\_\\infty , a\_\\infty , b\_\\infty : C\_{g\_\\infty (0)}\\left( p\_\\infty , r \\right) \\times \[-\\Delta t, 0\] \\rightarrow {\\mathbb {R}}\_{\\ge 0} \\end{aligned}\
\
\
\
    such that the metric g\_\\infty (t), t\\in \\left\[ -\\Delta t,0 \\right\] , is of the form ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) and in the class {\\mathcal {I}}.\
\
3. (c)\
Choosing the coordinate \\xi  on (U\_i, g\_i(t), p\_i) corresponding to whether we are in Case (i) or (ii) above, the warping functions u\_i(\\xi ,t), a\_i(\\xi , t) and b\_i(\\xi ,t) converge on compact sets to u\_\\infty (\\xi ,t), a\_\\infty (\\xi ,t) and b\_\\infty (\\xi , t).\
\
4. (d)\
For every r' < r the closed set \\overline{C\_{g\_\\infty (0)}(p\_\\infty , r')} \\subset {\\mathcal {C}}\_\\infty  is compact.\
\
\
From Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) the following corollary follows immediately:\
\
### Corollary 8.2\
\
(Compactness of complete Ricci flows)  Let k \\in {\\mathbb {N}},\\kappa , K >0 and r\_i, t\_i, \\rho \_i \\rightarrow \\infty  as i \\rightarrow \\infty . Assume that ({\\mathcal {M}}\_i, g\_i(t), p\_i), t \\in \[-t\_i, 0\], is a sequence of pointed _U_(2)-invariant cohomogeneity one Ricci flows satisfying:\
\
1. (1)\
For t \\in \[-t\_i, 0\] we have g\_i(t) \\in {\\mathcal {I}}. Denote by u\_i, a\_i and b\_i the warping functions of g\_i(t).\
\
2. (2)\
\\overline{C\_{g\_i(0)}(p\_i, r\_i) } \\subset {\\mathcal {M}}\_i is compact.\
\
3. (3)\
b(p\_i,0) = 1.\
\
4. (4)\
g\_i(t) is \\kappa -non-collapsed at scale \\rho \_i.\
\
5. (5)\
\|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le K on {\\mathcal {M}}\_i \\times \[-t\_i, 0\].\
\
\
Then ({\\mathcal {M}}\_i, g\_i(t), p\_i), t\\in \[-t\_i, 0\], subsequentially converges, in the Cheeger–Gromov sense, to a pointed complete ancient Ricci flow ({\\mathcal {M}}\_\\infty , g\_\\infty (t), p\_\\infty ),  t \\in (-\\infty , 0\], with bounded curvature satisfying properties (a)–(d) of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82), when taking {\\mathcal {C}}\_\\infty = {\\mathcal {M}}\_\\infty  and r = \\infty .\
\
### Proof\
\
This follows from Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) by a diagonal argument. \\square\
\
The following proposition is a variant of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) in the case we take r=\\frac{1}{2}.\
\
### Proposition 8.3\
\
Let k \\in {\\mathbb {N}}, \\kappa , \\rho , C\_1 > 0, r = \\frac{1}{2} and \\Delta t \\in (0, \\frac{1}{48C\_1}\]. Assume\
\
\\begin{aligned} (U\_i, g\_i(t), p\_i), \\quad t \\in \\left\[ -\\Delta t, 0\\right\] , \\end{aligned}\
\
is a sequence of pointed _U_(2)-invariant cohomogeneity one Ricci flows satisfying Conditions (1)–(5) of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82). If, instead of Condition (6) of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82), we require\
\
1. (6’)\
\|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le \\frac{C\_1}{b^2} on U\_i \\times \[-\\Delta t, 0\],\
\
\
then\
\
\\begin{aligned} \\left( C\_{g\_i(0)}\\left( p\_i, \\frac{1}{2}\\right) , g\_i(t), p\_i\\right) , \\quad t \\in \[-\\Delta t, 0\] \\end{aligned}\
\
subsequentially converges, in the Cheeger–Gromov sense, to a pointed Ricci flow\
\
\\begin{aligned} ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), \\quad t \\in \\left\[ - \\Delta t, 0\\right\] , \\end{aligned}\
\
satisfying the same properties (a)–(d) listed in Theorem [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85).\
\
### Proof of Proposition 8.3\
\
For brevity we write \\Omega \_ i = C\_{g\_i(0)}\\big ( p\_i,\\frac{1}{2}\\big ) \\times \[-\\Delta t,0\]. Let a\_i and b\_i denote the warping functions of g\_i(t). As g\_i(t) \\in {\\mathcal {I}} we have\
\
\\begin{aligned} 0 \\le (b\_i)\_s \\le Q\_i \\le 1\\quad \\, \\text { in }\\, \\Omega \_i, \\end{aligned}\
\
where Q\_i = \\frac{a\_i}{b\_i} and thus\
\
\\begin{aligned} b\_i(p, 0) \\ge \\frac{1}{2} \\,\\quad \\text { for } p \\in C\_{g\_i(0)}\\left( p\_i, \\frac{1}{2}\\right) \\end{aligned}\
\
as b\_i(p\_i, 0) = 1 by assumption. By the Ricci flow equation we have\
\
\\begin{aligned} \\partial \_t b\_i^2&= - 2b^2 \\left( R\_{0202}+ R\_{1212} + R\_{2323}\\right) \\\&\\le 6 C\_1 \\quad \\, \\text { on }\\, \\Omega \_i. \\end{aligned}\
\
This implies\
\
\\begin{aligned} b\_i(p,t) \\ge \\frac{1}{\\sqrt{8}} \\quad \\text { for } (p,t)\\in \\Omega \_i, \\end{aligned}\
\
as \\Delta t \\le \\frac{1}{48C\_1} by assumption. This yields the uniform curvature bound\
\
\\begin{aligned} \|\\textrm{Rm}(g\_i)\|\_{g\_i} \\le 8C\_1 \\quad \\text { on }\\, \\Omega \_i. \\end{aligned}\
\
The result now follows from Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82). \\square\
\
The main proof idea of Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) is to construct a set of four Killing vector fields {\\overline{X}}\_j, j = 1, 2, 3, 4, generated by the _U_(2)-action on each (U\_i, g\_i(t)), and show that these Killing vector fields pass to the limit ({\\mathcal {C}}\_\\infty , g\_\\infty (t)). This allows us to reconstruct the _U_(2)-action on {\\mathcal {C}}\_\\infty , proving the desired result. The main difficulty, however, is to show that the orbits corresponding to the flows of the Killing vector fields do not degenerate in the limit and thereby ensure that the full _U_(2) symmetry group is preserved. For this we will rely on Lemma [8.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar87) below, where we prove that \\kappa -non-collapsedness implies a lower positive bound on _Q_ away from a non-principal orbit.\
\
### Lemma 8.4\
\
Let k \\in {\\mathbb {N}}, r\_0 \\in (0, 1\] and \\kappa , C\_1, c > 0. Assume that ( _M_, _g_) is a _U_(2)-invariant cohomogeneity one manifold with principal orbit S^3 /{\\mathbb {Z}}\_k equipped with a metric g \\in {\\mathcal {I}}. Take p \\in M. If\
\
1. (1)\
the set \\overline{C^+\_g(p,b(p)r\_0)} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) is compactly contained in _M_;\
\
2. (2)\
\|\\textrm{Rm}\_{g}\|\_{g} \\le \\frac{C\_1}{b^2} on \\overline{C^+\_g(p,b(p)r\_0)};\
\
3. (3)\
_g_ is \\kappa -non-collapsed at scale _cb_( _p_): If for r \\le c b(p) the ball B\_g(p,r) is compactly contained in _M_ and \|\\textrm{Rm}\_g\|\_g < r^{-2} on B\_g(p,r) then \\textrm{vol}(B\_g(p,r)) \\ge \\kappa r^4,\
\
\
then there exists an \\epsilon > 0 depending on k, \\kappa , C\_1 , c and r\_0 for which the following holds: If for q \\in C^+\_g(p,b(p)r\_0) the set C\_g(q, b(p) \\frac{r\_0}{4}) is compactly contained in C^+\_g(p,b(p)r\_0) then Q(q) \\ge \\epsilon .\
\
### Proof\
\
By rescaling we may assume without loss of generality b(p) =1 and that the metric _g_ is \\kappa -non-collapsed at scale c>0. The latter follows from the fact that if _g_ is \\kappa -non-collapsed at scale \\rho  then \\alpha ^2 g is \\kappa -non-collapsed at scale \\alpha \\rho . Fix a q \\in C^+\_g(p,b(p)r\_0) such that the assumptions of the lemma hold. Take U :=C\_g(q, b(p) \\frac{r\_0}{4}). Note that _U_ is a union of orbits of the _U_(2)-action. Recall that non-principal orbits are non-generic and characterized by a = 0. As a\_s \\ge 0 we see that all the orbits of _U_ are principal and therefore diffeomorphic to S^3/{\\mathbb {Z}}\_k. Because 0 \\le b\_s \\le Q \\le 1  for metrics in {\\mathcal {I}} we see that\
\
\\begin{aligned} 1 \\le b \\le 2 \\quad \\text { in } C^+\_g(p,r\_0), \\end{aligned}\
\
and hence\
\
\\begin{aligned} \|\\textrm{Rm}\_g\|\_g \\le C\_1 \\quad \\text { in } C^+\_g(p,r\_0) \\end{aligned}\
\
by assumption (2). From the expression\
\
\\begin{aligned} M\_2 = \\frac{1}{b^2}\\left( a\_s - Q b\_s \\right) \\end{aligned}\
\
for the curvature component R\_{0231} derived in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11) and the fact that\
\
\\begin{aligned} Q\_s = \\frac{1}{b} \\left( a\_s - Q b\_s\\right) , \\end{aligned}\
\
we deduce that\
\
\\begin{aligned} \|Q\_s\| \\le C\_1\\quad \\text { in } C^+\_g(p,r\_0). \\end{aligned}\
\
Thus for r \\le r\_1 :=\\min \\big (\\frac{r\_0}{4}, \\frac{Q(q)}{C\_1}\\big ) we have\
\
\\begin{aligned} Q \\le 2Q(q)\\quad \\, \\text { on } C\_g(q, r\_1). \\end{aligned}\
\
### Claim 1\
\
For r \\le r\_2 :=\\min \\big (\\frac{1}{100}, r\_1\\big ) we have\
\
\\begin{aligned} \\textrm{vol}(B\_g(q,r)) \\le C r^3 Q(q) \\end{aligned}\
\
for some constant C> 0 depending on _k_ only.\
\
### Proof of Claim\
\
Let q' \\in C\_g(q, r), r < r\_2. Then \\Sigma \_{q'} is isometric to S^3/{\\mathbb {Z}}\_k equipped with a squashed Berger metric. In particular, if we denote by \\iota : \\Sigma \_{q'} \\rightarrow M the inclusion, then\
\
\\begin{aligned} \\iota ^\*g = a(q')^2 \\omega \\otimes \\omega + b(q')^2\\pi ^\*(g\_\\textrm{FS}), \\end{aligned}\
\
where g\_\\textrm{FS} is the Fubini–Study metric on S^2 normalized to have curvature equal to \\frac{1}{4} and \\pi : S^3 / {\\mathbb {Z}}\_k \\rightarrow S^2 is the Hopf fibration. Note that\
\
\\begin{aligned} \\Sigma \_{q'} \\cap B\_g(q,r) \\subseteq \\Sigma \_{q'} \\cap B\_g(q',r) \\subseteq \\pi ^{-1}(B\_{{g}\_\\textrm{FS}}(\\pi (q'), r)) \\subseteq \\Sigma \_{q'}. \\end{aligned}\
\
Furthermore, as the Hopf fibers of \\Sigma \_{q'} \\cong S^3/{\\mathbb {Z}}\_k have length \\frac{2\\pi }{k} a(q'), we see that\
\
\\begin{aligned} \\textrm{vol}(\\pi ^{-1}(B\_{{g}\_\\textrm{FS}}(\\pi (q'), r))) = \\frac{2\\pi }{k} a(q') \\textrm{vol}(B\_{{g}\_{\\textrm{FS}}}(\\pi (q'), r)) \\le C a(q') r^2, \\end{aligned}\
\
for some constant C>0 depending on _k_ only. Since Q = \\frac{a}{b}, Q \\le 2 Q(q) and b \\in \[1, 2\] in C\_g(q, r\_1) it follows that\
\
\\begin{aligned} \\textrm{vol}(\\Sigma \_{q'} \\cap B\_g(q,r)) \\le 4 C Q(q) r^2. \\end{aligned}\
\
Integrating this inequality proves the claim. \\square\
\
As \|\\textrm{Rm}\_g\|\_g \\le C\_1 on C^+\_g(p,r\_0), the ball B\_g(q,\\frac{r\_0}{4}) is compactly contained in _M_, and _g_ is \\kappa -non-collapsed at scale _c_, we see that for r \\le r\_3 :=\\min \\big (\\frac{1}{\\sqrt{C\_2}}, c, \\frac{r\_0}{4}\\big )\
\
\\begin{aligned} \\textrm{vol}(B\_g(q,r)) \\ge \\kappa r^4. \\end{aligned}\
\
Setting r\_4 :=\\min \\left( r\_2, r\_3\\right)  we therefore obtain\
\
\\begin{aligned} C r\_4^3 Q(q) \\ge \\textrm{vol}(B\_g(q,r\_4)) \\ge \\kappa r\_4^4. \\end{aligned}\
\
Rearranging this inequality proves the lemma. \\square\
\
Before proving the compactness theorems listed above, we construct a set of four Killing vector fields on a general _U_(2)-invariant cohomogeneity one manifold _M_ with principal orbit S^3/{\\mathbb {Z}}\_k. By passing to the universal cover we may assume without loss of generality that k = 1. Pick the basis\
\
\\begin{aligned} X\_0 = \\begin{pmatrix} \\textrm{i} &{} 0 \\\ 0 &{} \\textrm{i} \\end{pmatrix}, \\quad X\_1 = \\begin{pmatrix} \\textrm{i} &{} 0 \\\ 0 &{} -\\textrm{i} \\end{pmatrix}, \\quad X\_2 = \\begin{pmatrix} 0 &{} \\textrm{i} \\\ \\textrm{i} &{} 0 \\end{pmatrix}, \\quad X\_3 = \\begin{pmatrix} 0 &{} -1 \\\ 1 &{} 0 \\end{pmatrix} \\end{aligned}\
\
for the Lie algebra of _U_(2). Then X\_i, i = 1, 2, 3, 4, satisfy the commutation relations\
\
\\begin{aligned}{}\[X\_1,X\_2\] = 2 X\_3, \\quad \[X\_2,X\_3\] = 2 X\_1, \\quad \[X\_3,X\_1\] = 2 X\_2 \\end{aligned}\
\
and\
\
\\begin{aligned}{}\[X\_0, X\_i\] = 0 \\quad \\, \\text { for } \\, i = 1, 2, 3. \\end{aligned}\
\
Extend X\_i, i = 1, 2, 3, 4, to left-invariant vector fields on _U_(2). Note that the integral curves generated by X\_i, i = 1, 2, 3, 4, have period 2\\pi . The _U_(2)-action generates four corresponding Killing vector fields {\\overline{X}}\_i, i = 1, 2, 3, 4, on M\_k by taking\
\
\\begin{aligned} {\\overline{X}}\_i\\big (p\\big ) = \\frac{d}{dt} \\Big \|\_{t=0} \\exp (t X\_i) \\cdot p, \\quad p \\in M\_k,\\,i = 1,2,3,4. \\end{aligned}\
\
We now prove the following:\
\
### Lemma 8.5\
\
For i = 1, 2, 3, 4 we have\
\
\\begin{aligned} \|{\\overline{X}}\_i\|\_{g} \\le \\max (a,b). \\end{aligned}\
\
### Proof\
\
By the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)) of the metric we see that \|{\\overline{X}}\_0\|\_g = a. Hence we only need to prove the result for i = 1, 2, 3. First note that the vector fields {\\overline{X}}\_i, i = 1, 2, 3, are orthogonal to \\frac{\\partial }{\\partial s} and therefore parallel to the orbits of the _U_(2) action on M\_k. Hence it suffices to study the metric _g_ restricted to these directions. Here we see that\
\
\\begin{aligned} a^2 \\omega \\otimes \\omega + b^2 \\pi ^\*(g\_{\\textrm{FS}}) \\le \\max (a,b)^2 g\_{S^3}, \\end{aligned}\
\
where g\_{S^3} is the round metric on S^3 with sectional curvatures equal to 1. Thus it suffices to show that\
\
\\begin{aligned} \|{\\overline{X}}\_i\|\_{g\_{S^3}} \\le 1. \\end{aligned}\
\
If we identify S^3 with _SU_(2), the vectors {\\overline{X}}\_i correspond to right-invariant vector fields on _SU_(2). Moreover, one can check that these vector fields are orthonormal with respect to the metric g\_{S^3}. Hence the desired result follows. \\square\
\
### Remark 8.6\
\
In fact one can show that \\min (a,b) \\le \|{\\overline{X}}\_i\|\_{g} \\le \\max (a,b). Recalling that the isometry generated by the Killing vector field {\\overline{X}}\_i descends to a rotation of the base S^2 in the Hopf fibration \\pi : S^3 \\rightarrow S^2, one can see that the upper bound is attained on \\pi ^{-1}(\\{\\text {Equator of }S^2\\}) and the lower bound is attained on \\pi ^{-1}(\\{N,S\\}), where _N_, _S_ denote the north and south pole with respect to the rotation induced by {\\overline{X}}\_i.\
\
Now we proceed to proving the main theorem of this section:\
\
### Proof of Theorem 8.1\
\
As g\_i(t) is \\kappa -non-collapsed at (p\_i,0) at scale \\min (\\rho , r, \\sqrt{\\Delta t}) it follows from \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"), Lemma 6.54\] that there exists a uniform \\delta >0 such that\
\
\\begin{aligned} {\\textrm{inj}}\_{g\_i(0)}(p\_i) > \\delta . \\end{aligned}\
\
By assumption g\_i(t) has bounded curvature on the parabolic neighborhood\
\
\\begin{aligned} \\Omega \_i :=C\_{g\_i(0)}\\left( p\_i, r\\right) \\times \[-\\Delta t, 0\]. \\end{aligned}\
\
By an adaptation of \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Theorem 3.16\] we therefore deduce that after passing to a subsequence\
\
\\begin{aligned} \\left( C\_{g\_i(0)}\\left( p\_i, r\\right) , g\_i(t), p\_i\\right) , \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
converges, in the Cheeger–Gromov sense, to a pointed Ricci flow\
\
\\begin{aligned} \\left( {\\mathcal {C}}\_{\\infty }, g\_{\\infty }(t), p\_{\\infty }\\right) , \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
where {\\mathcal {C}}\_\\infty  is an open manifold. \\square\
\
### Claim 1\
\
({\\mathcal {C}}\_{\\infty }, g\_{\\infty }(t)),  t \\in \[-\\Delta t, 0\], is _U_(2)-invariant.\
\
### Proof of Claim 1\
\
Recall the construction of the Killing vector fields {\\overline{X}}\_j, j = 1, 2, 3, 4 for a general _U_(2)-invariant manifold _M_ explained above. Let {\\overline{X}}\_{ij}, i \\in {\\mathbb {N}}, j = 1, 2, 3, 4, denote the corresponding Killing vector fields on the manifolds C\_{g\_i(0)}\\left( p\_i, r\\right) . Recall that g\_i(t) \\in {\\mathcal {I}} implies that 0 \\le b\_s \\le Q \\le 1. Therefore b \\le r+1 on C\_{g\_i(0)}\\left( p\_i, r\\right) . Note that from the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ it follows that\
\
\\begin{aligned} \\left\| \\frac{\\partial \_t b}{b}\\right\| \\le c \|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)}, \\end{aligned}\
\
where c > 0 is some universal constant. As \|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le C\_1 on \\Omega \_i by assumption, we see that there exists a C>0, depending on _r_ and C\_1 only, such that b \\le C on \\Omega \_i. From Lemma [8.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar91) it hence follows that for i \\in {\\mathbb {N}}, j = 1, 2, 3, 4,\
\
\\begin{aligned} \|{\\overline{X}}\_{ij}\|\_{g\_i(t)} \\le C\\quad \\, \\text { on }\\, \\Omega \_i. \\end{aligned}\
\
Recall that in general a Killing vector field X^a on a manifold satisfies the relation\
\
\\begin{aligned} \\nabla \_a\\nabla \_b X^c = -R^c\_{\\,abd} X^d. \\end{aligned}\
\
Therefore we see that the Killing vector fields {\\overline{X}}\_{ij} are uniformly bounded in C^2(\\Omega \_i), and converge to C^1 Killing vector fields {\\overline{X}}\_{\\infty , j}, j = 1, 2, 3,4, on \\left( {\\mathcal {C}}\_{\\infty }, g\_{\\infty }(t)\\right)  after passing to a subsequence. However, since the group of isometries of a smooth manifold is a smooth Lie group, the vector fields {\\overline{X}}\_{\\infty , j}, j = 1, 2, 3,4 are in fact smooth. As the Killing vector fields {\\overline{X}}\_{ij}, i \\in {\\mathbb {N}}, j = 1,2, 3,4, are complete, so are {\\overline{X}}\_{\\infty , j}, j = 1, 2, 3,4. Integrating the Killing vector fields {\\overline{X}}\_{\\infty , j}, j = 1,2,3,4, then yield the desired _U_(2)-action on ({\\mathcal {C}}\_\\infty , g\_\\infty (t)). \\square\
\
It remains to be shown that this action is faithful by proving that the Killing vector fields are non-zero at times t \\in \[-\\Delta t, 0\].\
\
### Claim 2\
\
The _U_(2)-action on ({\\mathcal {C}}\_{\\infty }, g\_{\\infty }(t)),  t \\in \[-\\Delta t, 0\] is faithful.\
\
### Proof of Claim 2\
\
Take r\_1 > 0 such that C\_{g\_\\infty (t)}(p\_\\infty , r\_1) is compactly contained in {\\mathcal {C}}\_\\infty  for all t \\in \[-\\Delta t, 0\]. This is possible by standard distance distortion estimates and the fact that {\\mathcal {C}}\_{\\infty } \\times \[-\\Delta t, 0\] has bounded curvature. Furthermore, since C\_{g\_\\infty (t)}(p\_\\infty , r\_1) \\times \[-\\Delta t, 0\] is compactly contained in {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\], there exist constants \\rho ', \\kappa ' > 0 such that for each t \\in \[-\\Delta t, 0\] the manifold (C\_{g\_\\infty (t)}(p\_\\infty , r\_1), g\_\\infty (t)) is \\kappa '-non-collapsed at scale less or equal to \\rho '. Since (C\_{g\_i(t)}(p\_i, r), g\_i(t), p\_i) converges in the Cheeger–Gromov sense to ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ) we see that eventually (C\_{g\_i(t)}(p\_i, r\_1), g\_i(t)) is \\kappa '/2-non-collapsed at scales less or equal to \\rho '/2.\
\
Fix t' \\in \[-\\Delta t, 0\] and choose points q\_i \\in \\Sigma ^+\_{p\_i} (see Definition [2.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar13)) and q\_\\infty \\in {\\mathcal {C}}\_\\infty  with d\_{g\_i(t')}(q\_i, \\Sigma ^+\_{p\_i}) = \\frac{1}{2}r\_1 and q\_i \\rightarrow q\_\\infty . Checking the conditions of Lemma [8.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar87), we see that there exists an \\epsilon > 0, independent of _i_, such that\
\
\\begin{aligned} Q(q\_i,t') \\ge \\epsilon . \\end{aligned}\
\
As g \\in {\\mathcal {I}} and therefore 0 \\le b\_s \\le Q \\le 1, we see that\
\
\\begin{aligned} 1 \\le b(q\_i, t') \\le \\frac{3}{2}. \\end{aligned}\
\
Therefore the geometry of the orbit \\Sigma \_{q\_i} \\cong S^3 /{\\mathbb {Z}}\_k is controlled—the curvature and diameter are uniformly bounded from above, and its volume and Hopf fiber lengths are uniformly bounded away from zero. Hence the norms of the Killing vector fields {\\overline{X}}\_{ij}, j = 1, 2, 3, 4, at the points (q\_i, t') in spacetime are uniformly bounded away from zero, proving that on the limiting space ({\\mathcal {C}}\_\\infty , g\_\\infty (t')) the Killing vector fields {\\overline{X}}\_{\\infty , j}, j = 1, 2,3,4, are non-zero. As t' \\in \[\\Delta t, 0\] was arbitrary, the desired result follows. \\square\
\
By the slice theorem we see that either (i) all orbits of {\\mathcal {C}}\_\\infty  are principal and diffeomorphic to S^3/{\\mathbb {Z}}\_k or (ii) there exists exactly one non-principal orbit, which is diffeomorphic to S^2 and as usual we denote by S^2\_o. Below it will become clear why {\\mathcal {C}}\_\\infty  cannot possess two non-principal orbits. In Case (i) {\\mathcal {C}}\_\\infty  is diffeomorphic to the manifold {\\mathbb {R}}\\times S^3/{\\mathbb {Z}}\_k and in Case (ii) it is diffeomorphic to M\_k. In both cases there is a dense open set of the form {\\mathbb {R}}\\times S^3/{\\mathbb {Z}}\_k \\subset {\\mathcal {C}}\_\\infty .\
\
We now show that the metrics g\_\\infty (t) can be expressed in the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)). Denote the warping functions of the metrics g\_i(t) by a\_i and b\_i. In Case (i) we define the radial coordinates\
\
\\begin{aligned} \\xi \_i(p) = \\pm d\_{g\_i(0)}(p, \\Sigma \_{p\_i}), \\end{aligned}\
\
and\
\
\\begin{aligned} \\xi \_\\infty (p) = \\pm d\_{g\_\\infty (0)}(p, \\Sigma \_{p\_\\infty }) \\end{aligned}\
\
on C\_{g\_i(0)}\\left( p\_i, r\\right)  and {\\mathcal {C}}\_\\infty , respectively. We choose the sign of \\xi \_i(p) depending on which side of the hypersurface \\Sigma \_{p\_i} the point _p_ lies, and in such a way that \\partial \_{\\xi \_i} a\_i , \\partial \_{\\xi \_i} b\_i \\ge 0. The sign of \\xi \_\\infty (p) is chosen such that \\xi \_i \\rightarrow \\xi \_\\infty  as i \\rightarrow \\infty . In Case (ii) we may assume without loss of generality that for all i \\in {\\mathbb {N}} the open manifolds C\_{g\_i(0)}\\left( p\_i, r\\right)  contain a point o\_i such that the orbit \\Sigma \_{o\_i} is non-principal and o\_i \\rightarrow o\_\\infty \\in {\\mathcal {C}}\_\\infty  as i \\rightarrow \\infty . Then define radial coordinates\
\