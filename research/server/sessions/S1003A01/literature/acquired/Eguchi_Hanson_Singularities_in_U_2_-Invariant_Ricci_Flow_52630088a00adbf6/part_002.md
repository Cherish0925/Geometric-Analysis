---
retention_scope: session
part: 2
total_parts: 7
---

[Part 2/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

Although we have not analyzed the blow-up limits of a _U_(2)-invariant Ricci flow (M\_k, g(t)), t \\in \[0,T\_\\textrm{sing}), in the k\\ne 2 case, we believe that for each k\\in {\\mathbb {N}} there exists a unique blow-up limit of the singularity arising from the collapse of the two sphere S^2\_o at the tip of M\_k. In collaboration with Jon Wilkening, the author has already conducted numerical simulations confirming this, and a paper is in preparation \[ [2](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR2 "Appleton, A., Wilkening, J.: Computation of                                                                               $$U(2)$$                                                               U                       (                       2                       )                                                         -invariant Ricci flow singularities, In preparation")\]. In particular, we conjecture that\
\
### Conjecture 2\
\
Let (M\_k, g(t)) be a _U_(2)-invariant Ricci flow encountering a singularity at the tip of M\_k, as the area of S^2\_o decreases to zero. Then the following picture holds:\
\
| _k_ | _Blow-up limit at_ o \\in S^2\_o | _Type_ | _Isolated_ |\
| --- | --- | --- | --- |\
| 1 | _FIK shrinker_ | _Type I_ | _Yes_ |\
| 2 | _Eguchi–Hanson space_ | _Type II_ | _No_ |\
| \\ge 3 | _Steady Ricci solitons of_ \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)")\] | _Type II_ | _No_ |\
\
By isolated we mean that the singularity is not accompanied by a Type I singularity in its vicinity. For instance, in the case k\\ge 2 we expect a singularity caused by the collapse of the two-sphere S^2\_o at the tip of M\_k to always be accompanied by a Type I singularity modeled on the shrinking cylinder {\\mathbb {R}}\\times S^3/{\\mathbb {Z}}\_k and therefore not to be isolated. If for each k\\ge 3 the corresponding steady Ricci soliton of \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)")\] is in fact the unique blow-up limit at the tip of M\_k, then these singularities are necessarily accompanied by a Type I singularity modeled on S^3/{\\mathbb {Z}}\_k, because these solitons are asymptotically cylindrical.\
\
Another interesting question is the following:\
\
### Question 1\
\
Can the Eguchi–Hanson singularity occur on a closed four dimensional manifold?\
\
The author conjectures that the answer is yes, however only non-generically. The simplest model on which to investigate this question is M = M\_2 \\#\_{{\\mathbb {R}}P^3} M\_2 \\cong S^2 \\times S^2 equipped with a _U_(2)-invariant metric. One could carry out a construction as follows: Vary between an initial metric that encounters an {\\mathbb {R}}\\times {\\mathbb {R}}P^3 neckpinch singularity and an initial metric that leads to the collapse of one of the S^2 factors of _M_. On the path between these two metrics, there should be a metric whose Ricci flow evolution forms an Eguchi–Hanson singularity in finite time.\
\
This paper has not touched upon the behavior of a general non- _U_(2)-invariant metric on TS^2. A first question would be:\
\
### Question 2\
\
Does the picture of Theorem [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar144) also hold for Ricci flows starting from non- _U_(2)-invariant perturbations of asymptotically cylindrical _U_(2)-invariant metrics on TS^2?\
\
And a final big question mark is the following:\
\
### Question 3\
\
Are there other four-dimensional Ricci flat ALE spaces that can occur as blow-up limits in Ricci flow?\
\
So far all known Ricci flat ALE spaces in four dimensions are hyper-Kähler and it is not known whether non-hyperkähler examples exist. Kronheimer classified all hyper-Kähler ALE spaces \[ [25](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR25 "Kronheimer, P.B.: The construction of ALE spaces as hyper-Kähler quotients. J. Differ. Geom. 29(3), 665–683 (1989)"), [26](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR26 "Kronheimer, P.B.: A Torelli-type theorem for gravitational instantons. J. Differ. Geom. 29(3), 685–697 (1989)")\]. These spaces have one end that is asymptotic to the cone {\\mathbb {R}}^4 / \\Gamma , where \\Gamma \\subset U(2) is a certain finite group—a binary dihedral, tetrahedral, octahedral or icosahedral group. In the case that \\Gamma = {\\mathbb {Z}}\_k is cyclic, Gibbons and Hawking \[ [19](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR19 "Gibbons, G.W., Hawking, S.W.: Gravitational multi-instantons. Phys. Lett. B 78(4), 430–432 (1978)"), [20](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR20 "Gibbons, G.W., Hawking, S.W.: Classification of gravitational instanton symmetries. Comm. Math. Phys. 66(3), 291–310 (1979)")\] discovered a closed form (3k - 6)-parameter family of such metrics. In the physics literature these metrics are known as multi-center Eguchi Hanson spaces. It would be interesting to see whether the results of this paper can be generalized to prove the existence of singularities modeled on these spaces.\
\
## 2 Preliminaries\
\
### 2.1 Notation\
\
Here we collect some of the notations used throughout the paper.\
\
- M\_k, k \\in {\\mathbb {N}}: a manifold diffeomorphic to the blow-up of {\\mathbb {C}}^2/ {\\mathbb {Z}}\_k, k \\ge 1, at the origin.\
\
- S^2\_o: the two-sphere added during the blow-up of {\\mathbb {C}}^2/ {\\mathbb {Z}}\_k.\
\
- \\xi : the radial coordinate on M\_k or the parametrization of the {\\mathbb {R}}\_{>0} factor in the product {\\mathbb {R}}\_{>0} \\times S^3/{\\mathbb {Z}}\_k \\subset M\_k.\
\
- _o_: a fixed point on S^2\_o.\
\
- \\Sigma \_{p}: the orbit of _p_ under the _U_(2)-action. For instance if p \\in S^2\_o \\subset M\_k we have \\Sigma \_{p} = S^2\_o and when p \\in M\_k \\setminus S^2\_o we have \\Sigma \_{p}\\cong S^3 /{\\mathbb {Z}}\_k.\
\
- _s_: the geodesic distance from S^2\_o, and often considered as a function of \\xi  and _t_.\
\
- origin: refers to the point _o_.\
\
- _g_: a metric of the form ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) or ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)) unless otherwise stated.\
\
- d\_g: the metric distance induced by _g_.\
\
- _g_( _t_): a time dependent family of metrics of the form ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) or ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)).\
\
- _u_, _a_, _b_: the warping functions of the metric ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)). Depending on context, these will be considered as functions of (\\xi ,t), ( _s_, _t_) or ( _p_, _t_), where _p_ is a point on M\_k.\
\
- Q:=\\frac{a}{b}.\
\
- B\_g(p,r): the ball centered at _p_ of radius _r_ with respect to the metric _g_.\
\
- C\_g(p, r),  r>0: the subset of a cohomogeneity one _U_(2)-invariant Riemannian manifold ( _M_, _g_) defined by\
\
\
\
\\begin{aligned} C\_g(p, r) = \\left\\{ q \\in \\,M\\, \\big \| \\, d\_g(q, \\Sigma \_{p}) < r \\right\\} . \\end{aligned}\
\
\
\
The set C\_g(p, r) is diffeomorphic to either M\_k or {\\mathbb {R}}\\times S^3/{\\mathbb {Z}}\_k.\
\
- {\\overline{C}}\_g(p, r): the closure of C\_g(p, r).\
\
- T\_\\textrm{sing}: the singular time of a Ricci flow.\
\
- C^\\infty \_{U(2)}(M\_k \\times \[0,T\]): The space of smooth _U_(2)-invariant functions u: M\_k \\times \[0,T\] \\rightarrow {\\mathbb {R}}.\
\
- _x_, _y_: Kähler quantities introduced in Sect. [4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec15).\
\
\
### 2.2 The Manifold and Metric\
\
For k \\in {\\mathbb {N}} let M\_k be diffeomorphic to the blow-up of {\\mathbb {C}}^2 /{\\mathbb {Z}}\_k at the origin. Denote by S^2\_o the embedded two-sphere in M\_k stemming from the blow-up, and fix some point _o_ for ‘origin’ on S^2\_o.\
\
We now describe the _U_(2)-invariant metrics on M\_k, k \\ge 1, studied in this paper. Let z\_1, z\_2 be the standard coordinates on {\\mathbb {C}}^2 and let _U_(2) act on {\\mathbb {C}}^2 by left multiplication. This action descends to M\_k, k \\in {\\mathbb {N}}. Note that M\_k can be seen as the total space of the complex line bundle O(-k) via\
\
\\begin{aligned} \\pi : M\_k&\\longrightarrow S^2\_o, \\\ (z\_1, z\_2)&\\longmapsto \[z\_1, z\_2\]. \\end{aligned}\
\
Then U(2) \\cong U(1) \\times SU(2) acts on M\_k in the following way: The action of _U_(1) rotates the fibres of \\pi  and _SU_(2) acts on the base S^2\_o via rotations. Now introduce the Hopf coordinates\
\
\\begin{aligned} z\_1&= \\xi \\sin \\eta \\, e^{\\textrm{i}( \\psi + \\phi )} = x\_1 +\\textrm{i} y\_1, \\\ z\_2&= \\xi \\cos \\eta \\, e^{\\textrm{i}( \\psi - \\phi )} = x\_2 +\\textrm{i} y\_2 \\end{aligned}\
\
on {\\mathbb {C}}^2\_\*, where \\xi > 0, \\eta \\in \[0, \\pi /2\] and \\psi , \\phi \\in \[0, 2 \\pi ). These coordinates descend to M\_k. In particular, this allows us to endow M\_k with the radial coordinate \\xi : M\_k \\rightarrow {\\mathbb {R}}\_{\\ge 0}, by continuously extending \\xi  to S^2\_o by taking \\xi = 0 on S^2\_o. Note that the coordinate \\xi  is only smooth on M\_k \\setminus S^2\_o.\
\
A computation shows that the standard Euclidean metric\
\
\\begin{aligned} g\_{\\textrm{Eucl}} = dx\_1^2 + dy\_1^2 + dx\_2^2 + dy\_2^2 \\end{aligned}\
\
may be written as\
\
\\begin{aligned} g\_\\textrm{Eucl} = d\\xi ^2 + \\xi ^2 \\left( d\\eta ^2 + \\sin ^2(2\\eta ) d\\phi ^2 + \\left\[ d \\psi - \\cos (2\\eta )d\\phi \\right\] ^2 \\right) \\end{aligned}\
\
in Hopf coordinates. The 1-form\
\
\\begin{aligned} \\omega :=d \\psi - \\cos (2\\eta )d\\phi \\end{aligned}\
\
is dual to the Hopf fibre directions, or equivalently dual to the vector field generated by the _U_(1) action. Furthermore\
\
\\begin{aligned} d\\eta ^2 + \\sin ^2(2\\eta ) d\\phi ^2 \\end{aligned}\
\
(2.1)\
\
\
is the pull-back of the Fubini–Study metric g\_{\\textrm{FS}} on {\\mathbb {C}}P^1, normalized to have constant sectional curvature equal to \\frac{1}{4}.\
\
From the above we see that the warped-product metric\
\
\\begin{aligned} g = u(\\xi )^2 d\\xi ^2 + a(\\xi )^2 \\omega \\otimes \\omega + b(\\xi )^2 \\pi ^\*( g\_{\\textrm{FS}}) \\end{aligned}\
\
(2.2)\
\
\
is the most general _U_(2)-invariant metric on {\\mathbb {C}}\_\*^2 and descends to a _U_(2)-invariant metric on the open dense set {\\mathbb {C}}^2\_\*/{\\mathbb {Z}}\_k \\subset M\_k. It will be useful to introduce the change of coordinates defined by\
\
\\begin{aligned} ds = u(\\xi ) d\\xi \\end{aligned}\
\
and s = 0  at \\xi = 0. Then for p \\in M\_k the quantity s(p) = d\_{g}(p, S^2\_o) describes the radial distance of _p_ from S^2\_o. In these coordinates the metric becomes\
\
\\begin{aligned} g = ds^2 + a^2(s) \\omega \\otimes \\omega + b^2(s) \\pi ^\*( g\_{\\textrm{FS}}), \\end{aligned}\
\
(2.3)\
\
\
where in a slight abuse of notation we consider _a_ and _b_ as functions of _s_. Depending on the context we will consider _a_ and _b_ either as functions of _s_ or \\xi .\
\
The metric _g_ can be extended to a metric on all of M\_k by taking a(0) = 0 and b(0) > 0. In other words we shrink the Hopf fibre directions to zero as s \\rightarrow 0 or equivalently as we approach S^2\_o. Note that for every p \\in S^2\_o\
\
\\begin{aligned} ds^2 + a^2(s) \\omega \\otimes \\omega \\end{aligned}\
\
is the pull-back of _g_ onto the fibre \\pi ^{-1}(p). As _U_(1) acts on the fibre \\pi ^{-1}(p), we see that \\pi ^{-1}(p) is a union of S^1 orbits and _p_. Furthermore, such an S^1 orbit in \\pi ^{-1}(p) \\subset M\_k is parametrized by 0\\le \\psi < \\frac{2\\pi }{k} and, by the form of the metric ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)), such an S^1 orbit at radial distance _s_ from S^2\_o has a circumference of length \\frac{2\\pi }{k}a(s). Because\
\
\\begin{aligned} \\frac{2\\pi }{k}a(s) = \\frac{2\\pi }{k} a\_s(0) s + O(s^2) \\,\\quad \\text { as } \\, s \\rightarrow 0 \\end{aligned}\
\
we must require that a\_s(0) = k in order to avoid a conical singularity at S^2\_o. This is how the topology of the manifold enters the analysis of the Ricci flow equation. Additionally requiring that _a_( _s_) and _b_( _s_) can be extended to an odd and even function, respectively, around s=0 is a sufficient condition for the metric _g_ to be smoothly extendable to all of M\_k \[ [34](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR34 "Verdiani, L., Ziller, W.: Smoothness conditions in cohomogeneity manifolds,                    arXiv:1804.04680                                     (2018)")\]. In the rest of the paper, all metrics considered will be of the form ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) or equivalently ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)). In Fig. [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Fig1) the manifold M\_k and its metric close to the two sphere S^2\_o is schematically depicted.\
\
**Fig. 1**\
\
![Fig. 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs42543-022-00048-y/MediaObjects/42543_2022_48_Fig1_HTML.png)\
\
[Full size image](https://link.springer.com/article/10.1007/s42543-022-00048-y/figures/1)\
\
Diagram of the manifold M\_k close to the tip\
\
(M\_k, g), k \\in {\\mathbb {N}}, are cohomogeneity one manifolds, meaning that the generic orbits of the _U_(2) action are of codimension 1. The generic orbit is also called the principal orbit. The non-generic orbits are called non-principal orbits. In the case of M\_k, the principal orbits are diffeomorphic to S^3/{\\mathbb {Z}}\_k and the single non-principal orbit is S^2\_o and of codimension 2. Below we introduce some notation that we frequently employ throughout the paper:\
\
### Definition 2.1\
\
Assume ( _M_, _g_) is a _U_(2)-invariant cohomogeneity one manifold with principal orbit S^3/{\\mathbb {Z}}\_k for some fixed k \\in {\\mathbb {N}} and _g_ is a metric of the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)). Let p \\in M and r >0. Then:\
\
- Let \\Sigma \_p \\subset M denote the orbit of _p_ under the _U_(2)-action.\
\
- Let \\Sigma ^+\_p be the set of all points q \\in M that can be joined via path \\tau  to _p_ with g\\left( {\\dot{\\tau }},\\frac{\\partial }{\\partial s}\\right) \\ge 0.\
\
- Let\
\
\
\
\\begin{aligned} C\_g(p,r) :=\\big \\{ q\\in M \\, \\big \| \\, d\_g(q, \\Sigma \_p) < r \\big \\}. \\end{aligned}\
\
- Let\
\
\
\
\\begin{aligned} C^+\_g(p,r) :=\\big \\{ q\\in \\Sigma ^+\_p \\, \\big \| \\, d\_g(q, \\Sigma \_p) < r \\big \\}. \\end{aligned}\
\
\
Note that we have \\Sigma \_p \\cong S^3/{\\mathbb {Z}}\_k if _p_ lies on a principal orbit and \\Sigma \_p \\cong S^2 if _p_ lies on a non-principal orbit.\
\
### 2.3 The Connection, Laplacian and Curvature Tensor\
\
We now compute the connection, Laplacian and curvature tensor for metrics of the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)). To obtain the corresponding expressions for the metric ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) use the relation\
\
\\begin{aligned} \\frac{\\partial }{\\partial s} = \\frac{1}{u}\\frac{\\partial }{\\partial \\xi }. \\end{aligned}\
\
Take the orthonormal basis\
\
\\begin{aligned} e^0 = ds, \\quad e^1 = a \\left\[ d\\psi - \\cos (2\\eta ) d \\phi \\right\] , \\quad e^2 = b d \\eta , \\quad e^3 = b \\sin (2 \\eta ) d \\phi \\end{aligned}\
\
of T^\*M. Let e\_i, i = 1 , 2, 3, 4, be the corresponding dual basis of T\_\*M. Define the connection 1-forms \\theta \_i^j by \\nabla e\_i = \\theta \_i^j e\_j and the curvature 2-forms \\Omega \_i^j by R( \\cdot , \\cdot ) e\_i = \\Omega \_i^j e\_j. With help of Cartan’s structure equations\
\
\\begin{aligned}&\\theta \_i^j = - \\theta \_j^i, \\\&de^i = - \\theta \_j^i \\wedge e^j, \\\&\\Omega \_i^j = d \\theta \_i^j + \\theta ^j\_k \\wedge \\theta ^k\_i, \\end{aligned}\
\
one can compute the connection 1-forms and curvature 2-forms. First note that\
\
\\begin{aligned} de^0&= 0, \\\ de^1&= \\frac{a\_s}{a} e^0 \\wedge e^1 + \\frac{2a}{b^2} e^2 \\wedge e^3, \\\ de^2&= \\frac{b\_s}{b} e^0 \\wedge e^2, \\\ de^3&= \\frac{b\_s}{b} e^0 \\wedge e^3 + \\frac{2}{b} \\cot (2 \\eta ) e^2 \\wedge e^3. \\end{aligned}\
\
Hence we obtain the connection 1-forms \\theta ^i\_j:\
\
\\begin{aligned} \\theta ^1\_0&= \\frac{a\_s}{a} e^1,\\quad \\theta ^1\_2 = \\frac{a}{b^2} e^3, \\\ \\theta ^2\_0&= \\frac{b\_s}{b} e^2, \\quad \\theta ^2\_3 = - \\frac{a}{b^2} e^1 - \\frac{2}{b} \\cot (2\\eta ) e^3, \\\ \\theta ^3\_0&= \\frac{b\_s}{b} e^3,\\quad \\theta ^3\_1 = \\frac{a}{b^2} e^2. \\end{aligned}\
\
Therefore\
\
\\begin{aligned}{} & {} \\nabla \_{e\_0} e\_0 = 0, \\qquad \\nabla \_{e\_1} e\_1 = - \\frac{a\_s}{a} e\_0, \\qquad \\nabla \_{e\_2} e\_2 = -\\frac{b\_s}{b} e\_0,\\\{} & {} \\nabla \_{e\_3} e\_3 = - \\frac{b\_s}{b} e\_0 - \\frac{2}{b}\\cot (2\\eta ) e\_2, \\end{aligned}\
\
from which we can derive the expression for the Laplacian of a _U_(2)-invariant function f: M\_k \\rightarrow {\\mathbb {R}}:\
\
\\begin{aligned} \\Delta f = \\sum \_{i=0}^3 \\nabla ^2\_{e\_i,e\_i} f = f\_{ss} + \\left( \\frac{a\_s}{a} + 2 \\frac{b\_s}{b} \\right) f\_s. \\end{aligned}\
\
(2.4)\
\
\
Finally, we may compute the components\
\
\\begin{aligned} R\_{ijkl} = g\\left( R(e\_k,e\_l)e\_j,e\_i\\right) \\end{aligned}\
\
of the curvature tensor. Below we list its non-zero components\
\
\\begin{aligned} R\_{0101}&= -\\frac{a\_{ss}}{a}= K\_1, \\\ R\_{0202}&= -\\frac{b\_{ss}}{b} = K\_2,\\\ R\_{0303}&= -\\frac{b\_{ss}}{b}= K\_3, \\\ R\_{0123}&= -\\frac{2}{b^2} \\left( a\_s - Q b\_s\\right) = M\_1, \\\ R\_{0231}&= \\frac{1}{b^2} \\left( a\_s - Q b\_s\\right) = M\_2, \\\ R\_{0312}&= \\frac{1}{b^2} \\left( a\_s - Q b\_s\\right) = M\_3, \\\ R\_{1212}&= \\frac{a^2}{b^4}- \\frac{a\_sb\_s}{ab} = H\_{12}, \\\ R\_{2323}&= \\frac{4}{b^2} - 3 \\frac{a^2}{b^4} - \\left( \\frac{b\_s}{b}\\right) ^2 = H\_{23}, \\\ R\_{3131}&= \\frac{a^2}{b^4}- \\frac{a\_sb\_s}{ab} = H\_{31}. \\end{aligned}\
\
All other components are either determined by the standard symmetries of the curvature tensor or are zero.\
\
### 2.4 The Ricci Flow Equation\
\
With help of the above list of curvature components, one can check that the Ricci tensor is diagonal and hence the form of the metric ( [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ8)) is preserved by Ricci flow. Allowing the warping functions _a_, _b_ and _p_ to vary in time, the Ricci flow equation ( [1.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ1)) in (\\xi , t) coordinates can be expressed as a system of coupled parabolic equations in _a_, _b_ and _u_.\
\
\\begin{aligned} \\partial \_t u&= \\frac{1}{a} \\partial \_{\\xi } \\left( \\frac{a\_{\\xi }}{u} \\right) + \\frac{2}{b} \\partial \_{\\xi } \\left( \\frac{b\_{\\xi }}{u} \\right) , \\end{aligned}\
\
(2.5)\
\
\
\\begin{aligned} \\partial \_t a&= \\frac{1}{u} \\partial \_{\\xi } \\left( \\frac{a\_{\\xi }}{u} \\right) - 2 \\frac{a^3}{b^4} + 2 \\frac{a\_{\\xi }b\_{\\xi }}{bu^2}, \\end{aligned}\
\
(2.6)\
\
\
\\begin{aligned} \\partial \_t b&= \\frac{1}{u} \\partial \_{\\xi } \\left( \\frac{b\_{\\xi }}{u} \\right) - \\frac{4}{b} + 2\\frac{a^2}{b^3} + \\frac{a\_{\\xi }b\_{\\xi }}{au^2} + \\frac{b^2\_{\\xi }}{bu^2}. \\end{aligned}\
\
(2.7)\
\
\
Define the time dependent radial distance function s = s(\\xi , t) by\
\
\\begin{aligned} ds = u(\\xi , t) d\\xi . \\end{aligned}\
\
Then\
\
\\begin{aligned} s(\\xi ,t) = \\int \_0^{\\xi } u(\\xi ,t) \\, {{d}}\\xi \\end{aligned}\
\
(2.8)\
\
\
and\
\
\\begin{aligned} \\frac{\\partial }{\\partial s} = \\frac{1}{u} \\frac{\\partial }{\\partial \\xi }. \\end{aligned}\
\
(2.9)\
\
\
Furthermore the commutation relation\
\
\\begin{aligned}{}\[\\partial \_t, \\partial \_s\] = -\\frac{\\partial \_t u}{u}\\partial \_s \\end{aligned}\
\
holds. In terms of _s_ we can use ( [2.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ15)) to rewrite the Ricci flow equation in a slightly simpler form\
\
\\begin{aligned} \\frac{\\partial \_t u}{u}&= \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b}, \\end{aligned}\
\
(2.10)\
\
\
\\begin{aligned} \\partial \_t a&= a\_{ss} - 2 \\frac{a^3}{b^4} + 2 \\frac{a\_sb\_s}{b}, \\end{aligned}\
\
(2.11)\
\
\
\\begin{aligned} \\partial \_t b&= b\_{ss} - \\frac{4}{b} + 2\\frac{a^2}{b^3} + \\frac{a\_sb\_s}{a} + \\frac{b^2\_s}{b}. \\end{aligned}\
\
(2.12)\
\
\
Note that the dependence of the right hand side of this system of equations on \\xi  is hidden in the variable s = s(\\xi , t). However we can write the equations in terms of ( _s_, _t_) by introducing the functions\
\
\\begin{aligned} {\\tilde{a}}(s,t)&= a(\\xi , t), \\\ {\\tilde{b}}(s,t)&= b(\\xi , t) \\end{aligned}\
\
and noting that\
\
\\begin{aligned} \\partial \_t a \\big \|\_{\\xi }&= \\partial \_t {\\tilde{a}} \\big \|\_{s} + \\partial \_s {\\tilde{a}} \\big \|\_{t} \\frac{\\partial s}{\\partial t}\\bigg \|\_{\\xi }, \\\ \\partial \_t b \\big \|\_{\\xi }&= \\partial \_t {\\tilde{b}} \\big \|\_{s} + \\partial \_s {\\tilde{b}} \\big \|\_{t} \\frac{\\partial s}{\\partial t}\\bigg \|\_{\\xi }. \\end{aligned}\
\
By slight abuse of notation, however, we will drop the tilde and consider the warping functions _a_, _b_ and _u_ as functions of either ( _p_, _t_), p \\in M\_k or (\\xi , t) or ( _s_, _t_), depending on context. In ( _s_, _t_) coordinates the Ricci flow equation reads\
\
\\begin{aligned} \\partial \_t a \\big \|\_{s}&= a\_{ss} - 2 \\frac{a^3}{b^4} + 2 \\frac{a\_sb\_s}{b} - a\_s \\frac{\\partial s}{\\partial t}, \\end{aligned}\
\
(2.13)\
\
\
\\begin{aligned} \\partial \_t b \\big \|\_{s}&= b\_{ss} - \\frac{4}{b} + 2\\frac{a^2}{b^3} + \\frac{a\_sb\_s}{a} + \\frac{b^2\_s}{b} - b\_s \\frac{\\partial s}{\\partial t}, \\end{aligned}\
\
(2.14)\
\
\
where\
\
\\begin{aligned} \\frac{\\partial s}{\\partial t}\\bigg \|\_{\\xi } = \\int \_0^s \\left( \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b}\\right) \\, ds. \\end{aligned}\
\
(2.15)\
\
\
Whenever we differentiate a function f: M\_k \\times \[0,T\] with respect to time, unless stated otherwise, assume that the point on the manifold M\_k is held fixed. If we differentiate with respect to time while holding _s_ fixed we will denote the partial derivative by \\partial \_t f \|\_{s} to avoid confusion. Because _s_ is a function of (\\xi ,t), in general for fixed s\_0 > 0 the set \\{ s = s\_0\\} \\subset M\_k is dependent on time. Therefore holding _s_ or \\xi  fixed during partial differentiation produces very different results.\
\
This following property of the warping functions _a_ and _b_ will be used throughout the paper.\
\
### Lemma 2.2\
\
Let (M\_k, g(t)), t \\in \[0,T), be a smooth Ricci flow solution. Then for all t \\in \[0,T\] the warping functions _a_( _s_, _t_) and _b_( _s_, _t_) can be extended to an odd and even function, respectively, on {\\mathbb {R}}.\
\
### Proof\
\
Note that a necessary condition for a metric _g_ of the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)) to be smooth is that its corresponding warping functions _a_ and _b_ are extendable to odd and even functions, respectively, on {\\mathbb {R}}. Therefore the desired result follows. Alternatively, notice that if the warping functions of the initial data _a_( _s_, 0) and _b_( _s_, 0) can be extended to an odd and even function, respectively, on {\\mathbb {R}}, we can also extend the Eqs. ( [2.13](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ19)), ( [2.14](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ20)) and ( [2.15](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ21)) to all of {\\mathbb {R}}. An inspection of these equations shows that the parity of _a_ and _b_ is preserved under the flow. \\square\
\
### 2.5 Recap of Blow-up Limits of Singularities\
\
As mentioned above, every complete Riemannian manifold ( _M_, _g_) of bounded curvature admits a short-time Ricci flow starting from _g_, however singularities may develop in finite time. Similar to the study of other nonlinear equations, it is very useful to consider blow-up limits of singularities. We briefly sketch the idea here: Assume ( _M_, _g_( _t_)), t \\in \[0,T\_{\\textrm{sing}}), is a Ricci flow encountering a curvature singularity as t \\rightarrow T\_{\\textrm{sing}}. Let (p\_i, t\_i) with p\_i \\in M and t\_i \\rightarrow T\_{\\textrm{sing}} be a sequence of points in spacetime such that\
\
\\begin{aligned} K\_i := \|\\textrm{Rm}\_{g(t\_i)}\|\_{g(t\_i)}(p\_i) = \\sup \_{t \\le t\_i} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\end{aligned}\
\
and\
\
\\begin{aligned} K\_i \\rightarrow \\infty \\quad \\text {as } \\, i \\rightarrow \\infty . \\end{aligned}\
\
Take the rescaled metrics\
\
\\begin{aligned} g\_i(t) = K\_i g\\left( t\_i + \\frac{t}{K\_i} \\right) , \\quad t \\in \[-K\_i t\_i, 0\]. \\end{aligned}\
\
Then (M\_k, g\_i(t), p\_i) subsequentially converge, in the Cheeger–Gromov sense, to a pointed ancient Ricci flow solution (M\_\\infty , g\_\\infty (t), p\_\\infty ), t\\in (-\\infty , 0\] (see \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"), Theorem 6.68\] for more details). Note that in general M\_\\infty \\ne M. A Ricci flow is called ancient if it can be extended to a time interval of the form (-\\infty , T), T \\in {\\mathbb {R}}. The blow-up limit (M\_\\infty , g\_\\infty (t), p\_\\infty ) is called the singularity model and yields important geometrical information on the shape of the singularity. Hamilton \[ [22](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR22 "Hamilton, R.S.: The formation of singularities in the Ricci flow. In: Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), pp. 7–136. Int. Press, Cambridge, MA (1995)")\] distinguished between Type I and Type II singularities, depending on the rate of curvature blow-up, i.e., for Type I\
\
\\begin{aligned} \\sup \_{M \\times \[0,T)} \\left( T\_{\\textrm{sing}}- t\\right) \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} < \\infty \\end{aligned}\
\
and for Type II\
\
\\begin{aligned} \\sup \_{M \\times \[0,T)} \\left( T\_{\\textrm{sing}}- t\\right) \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} = \\infty . \\end{aligned}\
\
By the work of Naber \[ [29](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR29 "Naber, A.: Noncompact shrinking four solitons with nonnegative curvature. J. Reine Angew. Math. 645, 125–153 (2010)")\], and Enders, Müller and Topping \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)")\] it is known that Type I singularities are modeled on shrinking Ricci solitons. One hopes—although it has not been proven—that all Type II singularities are modeled on steady solitons, as to date all known examples are.\
\
## 3 The Maximum Principle\
\
Assume we are given a Ricci flow (M\_k, g(t)), t \\in \[0,T\], k \\ge 1. We make the following definition:\
\
### Definition 3.1\
\
Let C^\\infty \_{U(2)}(M\_k \\times \[0,T\]) be the space of smooth _U_(2)-invariant functions\
\
\\begin{aligned} u: M\_k \\times \[0,T\] \\rightarrow {\\mathbb {R}}. \\end{aligned}\
\
In this section we prove a maximum principle for operators\
\
\\begin{aligned} P: C^\\infty \_{U(2)} ( M\_k \\times \[0,T\]) \\rightarrow C^\\infty \_{U(2)} ( M\_k \\times \[0,T\]) \\end{aligned}\
\
that in (\\xi ,t) coordinates and away from the non-principal orbit S^2\_o of M\_k can be written in the form\
\
\\begin{aligned} P\[u\] = \\partial \_{ss} u + \\left( m \\frac{a\_s}{a} + n \\frac{b\_s}{b}\\right) u\_s + c u - \\partial \_t u, \\quad m,n \\in {\\mathbb {R}}, \\end{aligned}\
\
(3.1)\
\
\
where c\\in C^\\infty \_{U(2)}(M\_k \\times \[0,T\]). Recall from Sect. [2.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec12) that we are interpreting the _s_ derivative as\
\
\\begin{aligned} \\frac{\\partial }{\\partial s} = \\frac{1}{u} \\frac{\\partial }{\\partial \\xi }. \\end{aligned}\
\
It is useful to work in ( _s_, _t_) coordinates, in which case the operator _P_\[ _u_\] can be expressed as\
\
\\begin{aligned} P\[u\] = \\partial \_{ss} u + \\left( m \\frac{a\_s}{a} + n \\frac{b\_s}{b} - \\frac{\\partial s}{\\partial t} \\right) u\_s + c u - \\partial \_t \\Big \|\_s u, \\end{aligned}\
\
(3.2)\
\
\
where we recall the expression ( [2.15](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ21)) for \\frac{\\partial s}{\\partial t}. Note _P_\[ _u_\] is degenerate at the origin s=0 as\
\
\\begin{aligned} m \\frac{a\_s}{a} + n \\frac{b\_s}{b} - \\frac{\\partial s}{\\partial t} \\sim \\frac{m}{s}\\quad \\text {for } 0<\|s\|\\ll 1. \\end{aligned}\
\
However, in ( _s_, _t_) coordinates the smoothness of _u_ and _c_ is equivalent to saying that _u_( _s_, _t_), _c_( _s_, _t_) can be extended to smooth even functions around s=0 by defining u(s,t) = u(-s,t) and v(s,t) = v(-s,t) for s \\le 0. Hence we see that u\_s = c\_s = 0 at s=0 and via L’Hôpital’s Rule we obtain the following representation of _P_\[ _u_\] on the principal orbit S^2\_o:\
\
\\begin{aligned} P\[u\] = (m+1)\\partial \_{ss} u + c u - \\partial \_t u. \\end{aligned}\
\
The maximum principle derived for _P_ below depends on the sign of (m+1):\
\
### Theorem 3.2\
\
Let (M\_k, g(t)), k \\in {\\mathbb {N}}, t\\in \[0,T\] be a Ricci flow with bounded curvature. Let _P_ be an operator of the form ( [3.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ22)) and u \\in C^\\infty \_{U(2)}(M\_k \\times \[0,T\]). If\
\
\\begin{aligned} P\[u\] \\le 0 \\quad \\text {in } \\, M\_k \\times \[0,T\] \\end{aligned}\
\
and there exist constants M, \\sigma > 0 such that the growth conditions\
\
\\begin{aligned} u(s,t)&\\ge - M\\exp (- \\sigma s^2), \\\ c(s,t)&\\le M\\big ( \|s\|^2 +1 \\big ) \\end{aligned}\
\
are satisfied, then the following holds true:\
\
**Case 1:**(1+m \\le 0) If\
\
\\begin{aligned} u(s,0)&\\ge 0 \\quad \\text {for } \\, s \\ge 0, \\\ u(0,t)&\\ge 0 \\quad \\text {for } \\, t \\in \[0,T\], \\end{aligned}\
\
then u(s,t) \\ge 0 on \[0,\\infty ) \\times \[0,T\]. Furthermore, if u = 0 somewhere on (0,\\infty )\\times (0,T\] then u=0 everywhere.\
\
**Case 2:**(1+m > 0) If\
\
\\begin{aligned} u(s,0)&\\ge 0 \\quad \\text {for } \\, s \\ge 0, \\end{aligned}\
\
then u(s,t) \\ge 0 on \[0,\\infty ) \\times \[0,T\]. Furthermore, if u = 0 somewhere on \[0,\\infty ) \\times (0,T\] then u=0 everywhere.\
\
Before proving Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) we need to derive some bounds on \\frac{a\_s}{a}, \\frac{b\_s}{b} and \\frac{1}{b^2} for metrics _g_ of bounded curvature. This will allow us to bound the coefficients appearing in the expression ( [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ23)) of the operator _P_\[ _u_\].\
\
### Lemma 3.3\
\
Let (M\_k ,g), k \\in {\\mathbb {N}}, and K > 0 such that \|\\textrm{Rm}\_g\|\_g \\le K \\text { on } M\_k. Then everywhere on M\_k we have\
\
1. (1)\
b^2 \\ge \\frac{1}{K};\
\
2. (2)\
\\big (\\frac{b\_s}{b}\\big )^2 \\le 5 K;\
\
3. (3)\
    \\frac{Q^2}{b^2} \\le \\frac{5}{3} K .\
\
\
### Proof\
\
From the curvature components derived in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11) we see that\
\
\\begin{aligned} b^2 H\_{23}&= 4 - 3Q^2 - b\_s^2, \\end{aligned}\
\
(3.3)\
\
\
\\begin{aligned} b^2 H\_{12}&= Q^2 - \\frac{a\_s b\_s}{Q}. \\end{aligned}\
\
(3.4)\
\
\
At a local minimum b\_s =0 we thus have\
\
\\begin{aligned} b^2 = \\frac{4}{3H\_{12} + H\_{23}} \\ge \\frac{1}{K}. \\end{aligned}\
\
Now we argue by contradiction. Assume that there exists an s^\*>0 and \\delta > 0 such that at s= s^\* we have b^2 < \\frac{1-\\delta }{K}. From above it follows that b\_s < 0 for s \\ge s^{\*} and hence, because b >0 everywhere, \\lim \_{s \\rightarrow \\infty } b\_s = 0. Equation ( [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ24)) then shows that\
\
\\begin{aligned} Q^2&= \\frac{1}{3} \\big ( 4 - b^2 H\_{23} - b\_s^2 \\big ) \\\&\\ge 1 + \\frac{\\delta }{3} - \\frac{b\_s^2}{3} \\\&\\ge 1 + \\frac{\\delta }{4} \\end{aligned}\
\
for _s_ sufficiently large. Then ( [3.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ25)) implies that eventually\
\
\\begin{aligned} a\_s \\frac{b\_s}{Q} \\ge \\frac{5}{4}\\delta . \\end{aligned}\
\
Dividing by \\frac{b\_s}{Q} shows that\
\
\\begin{aligned} a\_s \\rightarrow -\\infty \\quad \\text { as } \\, s\\rightarrow \\infty , \\end{aligned}\
\
contradicting a \\ge 0. This proves the first bound. To prove the second bound note that\
\
\\begin{aligned} \\left( \\frac{b\_s}{b}\\right) ^2 = \\frac{4-3Q^2}{b^2} - H\_{23} \\le \\frac{4}{b^2} + K \\le 5K, \\end{aligned}\
\
where the last inequality follows from (1). For the third bound we have\
\
\\begin{aligned} \\frac{Q^2}{b^2} = \\frac{1}{3} \\left( \\frac{4}{b^2} - \\left( \\frac{b\_s}{b}\\right) ^2 - H\_{23} \\right) \\le \\frac{5}{3}K. \\end{aligned}\
\
\\square\
\
### Lemma 3.4\
\
Let (M\_k ,g), k \\in {\\mathbb {N}}, and K > 0 such that \|\\textrm{Rm}\_g\|\_g \\le K \\, \\text {on} \\, M\_k. Then everywhere on M\_k we have\
\
\\begin{aligned} - 2 \\sqrt{K}< \\frac{a\_s}{a} < \\frac{1}{s} + \\sqrt{K}. \\end{aligned}\
\
(3.5)\
\
\
### Proof\
\
The quantity \\phi = \\frac{a\_s}{a}s satisfies the ODE\
\
\\begin{aligned} \\frac{d \\phi }{ds} = s \\frac{a\_{ss}}{a} + \\frac{\\phi (1-\\phi )}{s} \\end{aligned}\
\
and by L’Hôpital’s Rule we have \\phi (0) = 1. Note that the function \\phi  can be extended to an even function on {\\mathbb {R}}. Therefore \\frac{d \\phi }{ds} (0) = 0 and there exists a small \\epsilon > 0 such that\
\
\\begin{aligned} \\phi \\le 1 + \\sqrt{K}s \\quad \\text {for } \\, 0 \\le s \\le \\epsilon . \\end{aligned}\
\
Actually the inequality holds for all s\\ge 0, since whenever \\phi (s) = 1 + \\sqrt{K}s we have\
\
\\begin{aligned} \\frac{d \\phi }{ds} = s \\left( \\frac{a\_{ss}}{a} - K\\right) - \\sqrt{K} < 0, \\end{aligned}\
\
since \|\\frac{a\_{ss}}{a}\| = \|R\_{0101}\| \\le K. This proves the upper bound of ( [3.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ26)).\
\
To prove the lower bound assume that a\_s(s\_0) < 0. For every s\_1 > s\_0 there exists an s^\*\\in (s\_0, s\_1) such that\
\
\\begin{aligned} a\_s(s\_1) - a\_s(s\_0) = (s\_1- s\_0) a\_{ss} (s^{\*}) \\le (s\_1- s\_0) K \|a(s^{\*})\| \\end{aligned}\
\
by the mean value theorem. It follows that\
\
\\begin{aligned} a\_s(s) \\le \\frac{1}{2} a\_s(s\_0) \\quad \\text {for } \\, s\_0 \\le s \\le s\_0 + \\frac{1}{2K} \\bigg \|\\frac{a\_s(s\_0)}{a(s\_0)}\\bigg \|. \\end{aligned}\
\
Therefore\
\
\\begin{aligned} 0 \\le a\\left( s\_0 + \\frac{1}{2K} \\bigg \|\\frac{a\_s(s\_0)}{a(s\_0)}\\bigg \|\\right) \\le a(s\_0) + \\frac{1}{2K} \\bigg \|\\frac{a\_s(s\_0)}{a(s\_0)}\\bigg \| \\frac{a\_s(s\_0)}{2}, \\end{aligned}\
\
which implies\
\
\\begin{aligned} \\frac{a\_s(s\_0)}{a(s\_0)} \\ge -2 \\sqrt{K}. \\end{aligned}\
\
This concludes the proof. \\square\
\
Now we may proceed to proving the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17).\
\
### Proof of Case 1 of Theorem 3.2\
\
Let K>0 such that\
\
\\begin{aligned} \\sup \_{M\_k \\times \[0,T\]} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le K. \\end{aligned}\
\
Introduce the new variable r := r(s, t) defined by\
\
\\begin{aligned} r(r+2) = s^2 \\end{aligned}\
\
and let\
\
\\begin{aligned} {\\overline{u}}(r,t) = u(\\sqrt{r(r+2)},t). \\end{aligned}\
\
Note that  2r \\sim s^2 for s \\ll 1 and r \\sim s for s \\gg 1. We make this substitution to remove the apparent singularity at s=0 in the ( _s_, _t_) coordinate representation ( [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ23)) of the operator _P_\[ _u_\]. The function {\\overline{u}} is smooth, because _u_ is extendable to an even function around the origin (see \[ [35](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR35 "Whitney, H.: Differentiable even functions. Duke Math. J. 10(1), 159–160 (1943)")\]). Rewriting ( [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ23)) in terms of ( _r_, _t_) coordinates we see that {\\overline{u}} satisfies the inequality\
\
\\begin{aligned} \\partial \_t {\\overline{u}} \\big \|\_{r}&\\ge A(r) \\partial \_{rr} {\\overline{u}} + B(r,t) \\partial \_r {\\overline{u}} + C(r,t) {\\overline{u}}, \\end{aligned}\
\
where _A_, _B_ and _C_ are smooth functions defined by\
\
\\begin{aligned}&A(r) = \\frac{r(r+2)}{(r+1)^2}, \\\&B(r,t) = \\left( m\\frac{a\_s}{a} + n\\frac{b\_s}{b} - \\frac{\\partial s}{\\partial t} \\right) \\frac{s}{r+1} + \\frac{1}{(r+1)^3}, \\\&C(r,t) = c(s,t). \\end{aligned}\
\
Note that above we regard _s_ as a function of _r_. Recall that by Lemma [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar14) the functions _a_ and _b_ can be extended to an odd and even function, respectively, around the origin. Therefore the quantity\
\
\\begin{aligned} \\left( m\\frac{a\_s}{a} + n\\frac{b\_s}{b} - \\frac{\\partial s}{\\partial t} \\right) s, \\end{aligned}\
\
(3.6)\
\
\
considered as a function of _s_, can be extended to an even function around the origin by \[ [35](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR35 "Whitney, H.: Differentiable even functions. Duke Math. J. 10(1), 159–160 (1943)")\]. Hence this expression depends smoothly on _r_, showing that _B_( _r_, _t_) is smooth. Similarly, we see that _C_( _r_, _t_) is smooth. From the expression ( [2.15](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ21)) for \\frac{\\partial s}{\\partial t} and the curvature components listed in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11) it follows that\
\
\\begin{aligned} \\Big \|\\frac{\\partial s}{\\partial t}\\Big \| = \\Big \|\\int \_0^s (-K\_1 - 2 K\_2) \\, {{d}}s\\Big \| \\le 3 K s. \\end{aligned}\
\
(3.7)\
\
\
By Lemmas [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) and [3.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar20) we hence see that\
\
\\begin{aligned} \|B(r,t)\| \\le M (r + 1) \\end{aligned}\
\
for some positive constant _M_ depending on _K_. Finally, noting that _A_( _r_) is bounded and positive for r > 0, we can apply \[ [17](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR17 "Friedman, A.: Partial Differential Equations of Parabolic Type. Prentice-Hall, Englewood Cliffs, NJ (1964)"), Theorem 9, p. 43\] to deduce that the weak maximum principle holds. Note that for any compact U \\subset M\_k \\times \[0,T\] we may assume that c < 0 on _U_ by performing the transformation {\\overline{u}} \\leftarrow {\\overline{u}} e^{-\\gamma t}, for \\gamma = \\gamma (U) chosen sufficiently large. Therefore the strong maximum principle follows from a slight adaptation of \[ [17](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR17 "Friedman, A.: Partial Differential Equations of Parabolic Type. Prentice-Hall, Englewood Cliffs, NJ (1964)"), Theorem 1, p. 34\]. \\square\
\
### Proof of Case 2 of Theorem 3.2\
\
We first prove the weak maximum principle. Taking u' = u e^{-\\gamma t} we see that u' satisfies\
\
\\begin{aligned} \\partial \_t u' \\ge \\partial \_{ss} u' + \\left( m \\frac{a\_s}{a} + n \\frac{b\_s}{b}\\right) u'\_s + (c - \\gamma ) u'. \\end{aligned}\
\
As _c_ is a smooth function of ( _s_, _t_), we can choose \\gamma  sufficiently large such that in a neighborhood of \\{s=0\\}\\times \[0,T\] we have c - \\gamma < 0. Since m+1 >0 we see that u' cannot attain a negative minimum on \\{s=0\\} \\times (0,T\], as otherwise\
\
\\begin{aligned} 0 \\le \\partial \_t u' = (1 + m) u'\_{ss} + c u' > 0, \\end{aligned}\
\
which is a contradiction. The weak maximum principle now follows by the proof of \[ [17](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR17 "Friedman, A.: Partial Differential Equations of Parabolic Type. Prentice-Hall, Englewood Cliffs, NJ (1964)"), Theorem 9, p. 43\].\
\
In this paper we only apply the strong maximum principle for m\\in {\\mathbb {N}} and therefore only prove this case here. For the general case refer to \[ [18](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR18 "Feehan, P.M.N.: Maximum principles for boundary-degenerate linear parabolic differential operators,                    arXiv:1306.5197                                     (2013)"), Theorem 5.17\]. Given a Ricci flow (M\_k, g(t)), t\\in \[0,T\], define the corresponding family of rotationally symmetric spaces ({\\mathbb {R}}^{m+1}, h(t)), t \\in \[0,T\], by\
\
\\begin{aligned} h = ds^2 + a^2(s,t) g\_{S^m(\\frac{1}{k})}, \\end{aligned}\
\
where g\_{S^{m}(\\frac{1}{k})} is the round metric on S^m of sectional curvature k^2. A sufficient condition for _h_ to be smooth at s=0 is that _a_ is extendable to an odd function around the origin and\
\
\\begin{aligned} a\_s(0) = k. \\end{aligned}\
\
Both these conditions are satisfied and we conclude that _h_ is a smooth metric. The Laplacian of a rotationally symmetric function _f_ on ({\\mathbb {R}}^{m+1},h) is given by\
\
\\begin{aligned} \\Delta \_{h} f = f\_{ss} + m\\frac{a\_s}{a} f\_s \\end{aligned}\
\
and thus the condition P\[u\] \\le 0 may be written as\
\
\\begin{aligned} \\partial \_t u \\ge \\Delta \_{h(t)} u + n \\frac{b\_s}{b} u\_s + c u. \\end{aligned}\
\
Note that for any bounded U \\subset M\_k \\times \[0,T\] we may assume that c < 0 on _U_ by performing the transformation u \\leftarrow u e^{-\\gamma t}, for \\gamma = \\gamma (U) chosen sufficiently large. Hence the desired result follows from \[ [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR10 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)"),  Theorem 12.40\]. \\square\
\
### Remark 3.5\
\
It was crucial in our analysis that _u_ is extendable to an even function around the origin, as the following example demonstrates:\
\
Consider the degenerate parabolic equation\
\
\\begin{aligned} u\_t = u\_{xx} -2 \\frac{u\_x}{x} + 2 \\frac{u}{x^2} \\end{aligned}\
\
(3.8)\
\
\
on x, t \\ge 0 with initial data satisfying u(x,0) \\le 0. If we take\
\
\\begin{aligned} u = x v, \\end{aligned}\
\
a computation shows that the above PDE corresponds to\
\
\\begin{aligned} v\_t = v\_{xx}. \\end{aligned}\
\
(3.9)\
\
\
Now considering ( [3.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ30)) as the heat equation on all of {\\mathbb {R}} we can set up initial data _v_( _x_, 0) such that\
\
\\begin{aligned} v(x,0) \\le 0 \\quad \\text {for } \\, x \\ge 0, \\end{aligned}\
\
however the solution _v_ to the heat equation becomes positive at some later time t>0 and x >0. This shows that u \\le 0 is not necessarily preserved by ( [3.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ29)).\
\
In this paper we also rely on a maximum principle for a system of parabolic inequalities on u\_1, u\_2 \\in C^\\infty \_{U(2)}(M\_k \\times \[0,T\]) of the form\
\
\\begin{aligned} \\partial \_t u\_1&\\ge (u\_1)\_{ss} + \\left( m \\frac{a\_s}{a} + n \\frac{b\_s}{b}\\right) (u\_1)\_s + h\_{11} u\_1 + h\_{12} u\_2, \\end{aligned}\
\
(3.10)\
\
\
\\begin{aligned} \\partial \_t u\_2&\\ge (u\_2)\_{ss} + \\left( m \\frac{a\_s}{a} + n \\frac{b\_s}{b}\\right) (u\_2)\_s + h\_{21} u\_1 + h\_{22} u\_2, \\end{aligned}\
\
(3.11)\
\
\
where h\_{ij}\\in C^\\infty \_{U(2)}(M\_k \\times \[0,T\]), i,j = 1,2, are bounded and satisfy\
\
\\begin{aligned} h\_{12}, h\_{21} \\ge 0 \\quad \\text {on } \\, M\_k \\times \[0,T\]. \\end{aligned}\
\
We prove the following lemma:\
\
### Lemma 3.6\
\
Let (M\_k, g(t)), t \\in \[0,T\], be a Ricci flow with bounded curvature. Assume u\_1, u\_2 \\in C^\\infty \_{U(2)}(M\_k \\times \[0,T\]) satisfy the above system ( [3.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ31))–( [3.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ32)) of parabolic inequalities and for some constants M, \\sigma > 0\
\
\\begin{aligned} u\_1(s,t), u\_2(s,t) \\ge -M \\exp (\\sigma s^2) \\quad \\text {for } t \\in \[0,T\]. \\end{aligned}\
\
If\
\
\\begin{aligned} u\_1(s,0), u\_2(s,0)&\\ge 0 \\quad \\text {for } s \\ge 0, \\\ u\_1(0,t), u\_2(0,t)&\\ge 0 \\quad \\text {for } t \\in \[0,T\], \\end{aligned}\
\
then u\_1, u\_2 \\ge 0 on M\_k\\times \[0,T\].\
\
### Proof\
\
Writing the equation in terms of ( _r_, _t_) as in the proof of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) we obtain\
\
\\begin{aligned} \\partial \_t u\_1 \\big \|\_{r}&\\ge A(r) (u\_1)\_{rr} + B(r,t) (u\_1)\_r + H\_{11} u\_1 + H\_{12} u\_2, \\\ \\partial \_t u\_2 \\big \|\_{r}&\\ge A(r) (u\_2)\_{rr} + B(r,t) (u\_2)\_r + H\_{21} u\_1 + H\_{22} u\_2, \\end{aligned}\
\
where _A_( _r_), _B_( _r_, _t_) are as in the proof of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) and\
\
\\begin{aligned} H\_{ij} (r,t) = h\_{ij}(s(r),t), \\quad i,j = 1,2. \\end{aligned}\
\
After constructing a barrier function of the form\
\
\\begin{aligned} H(s,t) = \\exp \\left\[ \\frac{k \|s\|^2}{1 - \\mu t} + \\nu t \\right\] , \\quad 0 \\le t \\le \\frac{1}{2\\mu }, \\end{aligned}\
\
the result follows combining the arguments of \[ [17](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR17 "Friedman, A.: Partial Differential Equations of Parabolic Type. Prentice-Hall, Englewood Cliffs, NJ (1964)"),  Theorem 1, p. 34\] and \[ [31](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR31 "Protter, M.H., Weinberger, H.F.: Maximum Principles in Differential Equations. Springer-Verlag, New York (1984)"),  Theorem 13, p. 190\]. \\square\
\
## 4 Kähler Quantities and the Eguchi–Hanson Space\
\
Recall that a complex structure _J_ on a Riemannian manifold ( _M_, _g_) satisfying\
\
1. (1)\
g(V\_1,V\_2) = g(JV\_1,JV\_2) for all V\_1, V\_2 \\in TM,\
\
2. (2)\
\\nabla J = 0\
\
\
defines a Kähler structure. On the manifolds M\_k, k \\ge 1, we define two complex structures J\_1 and J\_2 by\
\
\\begin{aligned} J\_1 e\_1 = e\_0, \\quad J\_1 e\_2 = e\_3 \\end{aligned}\
\
and\
\
\\begin{aligned} J\_2 e\_0 = e\_2, \\quad J\_2 e\_1 = e\_3. \\end{aligned}\
\
A computation shows that (M\_k, g, J\_1) is Kähler if and only if\
\
\\begin{aligned} b\_s - Q = 0. \\end{aligned}\
\
Similarly, (M\_k, g, J\_2) is Kähler if and only if\
\
\\begin{aligned} a\_s + Q^2 - 2 = 0 \\quad \\text {and} \\quad b\_s - Q = 0. \\end{aligned}\
\
Note that being Kähler with respect to J\_2 automatically implies Kählerity with respect to J\_1. This motivates the definition of the following _scale-invariant_ quantities\
\
\\begin{aligned} x&:= a\_s + Q^2 - 2, \\\ y&:= b\_s - Q \\end{aligned}\
\
to measure the deviation of a metric from being Kähler with respect to the complex structures J\_1 and J\_2. For example, the FIK shrinker \[ [16](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR16 "Feldman, M., Ilmanen, T., Knopf, D.: Rotationally symmetric shrinking and expanding gradient Kähler–Ricci solitons. J. Diff. Geom. 65(2), 169–209 (2003)")\] is Kähler with respect to the complex structure J\_1 and in our notation satisfies y=0. The Eguchi–Hanson space is the unique Kähler manifold with respect to J\_2 as the following lemma shows.\
\
### Lemma 4.1\
\
Amongst all Riemannian manifolds (M\_k, g), k \\ge 1, equipped with _U_(2)-invariant metric _g_ of the form ( [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ9)), up to scaling the Eguchi–Hanson space is the unique Kähler manifold with respect to the complex structure J\_2. Furthermore being Kähler with respect to J\_2 is equivalent to x = y = 0.\
\
### Proof\
\
By the above discussion being Kähler with respect to J\_2 is equivalent to\
\
\\begin{aligned} x = y = 0. \\end{aligned}\
\
(4.1)\
\
\
Notice at s=0 we have\
\
\\begin{aligned} x = a\_s -2 = 0 \\end{aligned}\
\
forcing the underlying manifold to be diffeomorphic to M\_2 by the boundary conditions ( [1.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ3)). Then in terms of _a_ and _b_ the condition x = y = 0 is equivalent to the first order system of equations\
\
\\begin{aligned} a\_s&= 2 - Q^2, \\end{aligned}\
\
(4.2)\
\
\
\\begin{aligned} b\_s&= Q. \\end{aligned}\
\
(4.3)\
\
\
Let a^E and b^E be a solution to this system of equations satisfying the initial conditions\
\
\\begin{aligned} a^E&= 0, \\quad b^E = 1 \\end{aligned}\
\
at s=0. Then by the scale-invariance of condition ( [4.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ33)), for every \\lambda >0 the metric given by the warping functions \\lambda a^{E}(\\lambda s) and \\lambda b^{E}(\\lambda s) also satisfies ( [4.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ33)). Hence up to rescaling there is a unique Kähler manifold with respect to the complex structure J\_2. From \[ [14](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR14 "Eguchi, T., Hanson, A.J.: Self-dual solutions to Euclidean gravity. Ann. Phys. 120(1), 82–105 (1979)")\] or \[ [4](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR4 "Calabi, E.: Métriques kählériennes et fibrés holomorphes. Ann. Sci. Ecole Norm. Sup. (4) 12(2), 269–294 (1979)")\] we see that the metric given by a^E and b^E is homothetic to the Eguchi–Hanson metric. \\square\
\
In the rest of the paper we denote by g\_E the Eguchi–Hanson metric with warping functions a^E and b^E normalized such that b^E = 1 on S^2\_o. Note that the normalization condition is equivalent to saying that the area of the exceptional divisor S^2\_o is equal to 2 \\pi .\
\
### Lemma 4.2\
\
The warping functions a^{E} and b^{E} of the Eguchi–Hanson metric satisfy the following properties\
\
\\begin{aligned} a^{E} ,b^{E}&\\sim s \\quad \\text {as } \\, s \\rightarrow \\infty , \\\ a^{E}\_{ss}&< 0 \\quad \\text {for } \\, s \\ge 0, \\\ b^{E}\_{ss}&> 0 \\quad \\text {for } \\, s \\ge 0, \\\ \\frac{a^{E}}{b^{E}}&< 1 \\quad \\text {for } \\, s \\ge 0. \\\ \\end{aligned}\
\
### Proof\
\
For brevity write _a_ and _b_ for a^{E} and b^{E}, respectively. Note that on the Eguchi–Hanson background we have\
\
\\begin{aligned} Q\_s = \\frac{1}{b} \\left( a\_s - Q b\_s \\right) = \\frac{2}{b} \\big ( 1- Q^2 \\big ), \\end{aligned}\
\
where the last equality follows from ( [4.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ34)) and ( [4.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ35)). As Q = 0 at s=0 it follows that\
\
\\begin{aligned} Q < 1 \\quad \\text {for } \\, s\\ge 0, \\end{aligned}\
\
and hence\
\
\\begin{aligned} Q\_s > 0 \\quad \\text {for } \\, s \\ge 0. \\end{aligned}\
\
As\
\
\\begin{aligned} a\_s&= Q\_s b + Q b\_s = 2 - Q^2, \\end{aligned}\
\
it follows that\
\
\\begin{aligned} a\_{ss} = -2 Q Q\_s < 0. \\end{aligned}\
\
Similarly\
\
\\begin{aligned} b\_{ss} = Q\_s > 0. \\end{aligned}\
\
Therefore the limits\
\
\\begin{aligned} a\_\\infty := \\lim \_{s\\rightarrow \\infty } a\_s \\end{aligned}\
\
and\
\
\\begin{aligned} b\_\\infty := \\lim \_{s\\rightarrow \\infty } b\_s \\end{aligned}\
\
both exist. From the system of differential Eqs. ( [4.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ34)) and ( [4.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ35)) we then see that\
\
\\begin{aligned} a\_{\\infty } = b\_{\\infty } = 1. \\end{aligned}\
\
This concludes the proof. \\square\
\
## 5 Some Preserved Conditions\
\
In this section we derive various _scale-invariant_ inequalities that are preserved by a Ricci flow (M\_k, g(t)), t \\in \[0,T\], k \\in {\\mathbb {N}}. The scale-invariance is crucial, as it ensures that the inequalities pass to blow-up limits and therefore also constrain their geometry. The preserved inequalities we list in this section will play an important role in all subsequent sections.\
\
**Section outline:** A central quantity in our analysis is\
\
\\begin{aligned} Q = \\frac{a}{b}. \\end{aligned}\
\
In geometric terms, _Q_ measures the deviation of the cross-sectional S^3 / {\\mathbb {Z}}\_k in M\_k from being round. That is, when Q=1 the cross-section is round and as Q \\rightarrow 0 the cross-sectional S^3 / {\\mathbb {Z}}\_k collapses along the S^1 Hopf fibres to a two-sphere. A computation shows that the evolution equation of _Q_ is\
\
\\begin{aligned} \\partial \_t Q = Q\_{ss} + 3 \\frac{b\_s}{b} Q\_s + \\frac{4}{b^2} Q\\big (1-Q^2\\big ). \\end{aligned}\
\
(5.1)\
\
\
Therefore one expects that the inequality Q \\le 1 is preserved by Ricci flow, which in Lemma [5.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar33) we prove to be the case.\
\
Apart from _Q_, the Kähler quantities _x_ and _y_ introduced in Sect. [4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec15) are used throughout this paper and are one of the key ingredients in showing that certain Ricci flows on M\_2 develop singularities modeled on the Eguchi–Hanson space. We show in Lemmas [5.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar35) and [5.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar38) that the inequalities\
\
\\begin{aligned} x\\le 0 \\end{aligned}\
\
and\
\
\\begin{aligned} y \\le 0 \\end{aligned}\
\
are both preserved. Furthermore, using the maximum principle for systems of weakly coupled parabolic equations of Lemma [3.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar25), we show in Lemma [5.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar40) that\
\
\\begin{aligned} a\_s, b\_s \\ge 0 \\end{aligned}\
\
is preserved. In Lemma [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar42) we show that on a Ricci flow background satisfying Q \\le 1 and y \\le 0, for any C > 2 the inequality a\_s \\le C is preserved. In the following sections we will mainly consider Ricci flows satisfying a\_s, b\_s \\ge 0, y \\le 0, Q\\le 1 and a\_s \\le C. This gives us enough control on _a_ and _b_ to prove many interesting results.\
\
Finally, we show that whenever a subset of the inequalities Q \\le 1, y\\le 0 and a\_s, b\_s \\ge 0 hold, the details of which are discussed below, the following inequalities\
\
\\begin{aligned}&T\_1 = a\_s + 2Q^2 -2 \\ge 0, \\\&T\_2 = Qy - x = -a\_s + Qb\_s + 2\\big (1 - Q^2 \\big ) \\ge 0, \\\&T\_3 = a\_s - Qb\_s - Q^2 + 1 \\ge 0, \\\&\\min (T\_1, T\_4) \\ge 0, \\end{aligned}\
\
where\
\
\\begin{aligned} T\_4 = a\_s - \\frac{1}{2} Q b\_s - \\big (1 - Q^2\\big ) \\end{aligned}\
\
are preserved by the Ricci flow. The precise statements and proofs of these preserved inequalities can be found in Lemmas [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar44), [5.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar46), [5.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar48) and [5.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar50) below.\
\
The main idea in constructing the above inequalities is to study the evolution equation of the scale-invariant quantities\
\
\\begin{aligned} T\_{(\\alpha , \\beta , \\gamma )} = \\alpha a\_s + \\beta Q b\_s + \\gamma Q^2, \\quad \\alpha , \\beta , \\gamma \\in {\\mathbb {R}}. \\end{aligned}\
\
(5.2)\
\
\
For this we need to compute the evolution equations of a\_s, Qb\_s and Q^2. Recall Definition [3.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar16) of C^\\infty \_{U(2)}(M\_k\\times \[0,T\]). To simplify the formulae slightly, define the linear operator\
\
\\begin{aligned} L: C^\\infty \_{U(2)}(M\_k\\times \[0,T\]) \\rightarrow C^\\infty \_{U(2)}(M\_k\\times \[0,T\]) \\end{aligned}\
\
by\
\
\\begin{aligned} L\[u\] = u\_{ss} + \\left( 2\\frac{b\_s}{b} -\\frac{a\_s}{a} \\right) u\_s \\end{aligned}\
\
away from the non-principal orbit S^2\_o. As in Sect. [3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec14) we may use L’Hôpital’s Rule to find a representation of _L_ on the non-principal orbit S^2\_o. Then, as we show in Appendix A, the evolution equations of a\_s, Qb\_s and Q^2 can be written as\
\
\\begin{aligned}&\\partial \_t a\_s = L\[a\_s\] + \\frac{1}{b^2}\\big ( -2 a\_s b\_s^2- 6 Q^2 a\_s + 8 Q^3 b\_s \\big ), \\end{aligned}\
\
(5.3)\
\
\
\\begin{aligned}&\\partial \_t Q b\_s = L\[Qb\_s\] +\\frac{1}{b^2}\\big ( 4 Q^2 a\_s- 10 Q^3 b\_s - 2 Q b\_s^3 + 8 Q b\_s\\big ), \\end{aligned}\
\
(5.4)\
\
\
\\begin{aligned}&\\partial \_t Q^2 = L\[Q^2\] + \\frac{1}{b^2}\\big (4 Q a\_s b\_s - 4 Q^2 b\_s^2 - 8 Q^4 + 8 Q^2 \\big ). \\end{aligned}\
\
(5.5)\
\
\
Since the operator _L_ is linear, one sees that T\_{(\\alpha , \\beta ,\\gamma )} satisfies an evolution equation of the form\
\
\\begin{aligned} \\partial \_t T\_{(\\alpha , \\beta , \\gamma )} = L\[T\_{(\\alpha , \\beta , \\gamma )}\] + \\frac{1}{b^2} C\_{(\\alpha , \\beta , \\gamma )}, \\end{aligned}\
\
(5.6)\
\
\
where C\_{(\\alpha , \\beta , \\gamma )} is a function of a\_s, b\_s and _Q_. This evolution equation is very useful, as it allows us to systematically search for preserved inequalities. In particular, if we can find \\alpha , \\beta , \\gamma , \\delta \\in {\\mathbb {R}} for which we can determine the sign of C\_{(\\alpha , \\beta , \\gamma )} at a local extrema of T\_{(\\alpha , \\beta , \\gamma )} at which T\_{(\\alpha , \\beta , \\gamma )} = \\delta , it follows from the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) that, depending on the sign, either\
\
\\begin{aligned} T\_{(\\alpha , \\beta , \\gamma )} \\ge \\delta \\end{aligned}\
\
or\
\
\\begin{aligned} T\_{(\\alpha , \\beta , \\gamma )} \\le \\delta \\end{aligned}\
\
is a preserved inequality.\
\
We searched for real numbers \\alpha , \\beta , \\gamma  and \\delta  leading to preserved conditions that yield the most useful control of the geometry of the flow. This is how we found the quantities T\_1, T\_2, T\_3 and T\_4. In later sections we will make heavy use of each of their respective inequalities. For instance, we use the preserved inequalities T\_1 \\ge 0 to exclude shrinking solitons on M\_k, k \\ge 2, in the next section. Finally, in Sect. [11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec22) we generalize the above idea to find a continuously varying family of conserved inequalities.\
\
**Statement and proof of results:** In this subsection, we list the precise statements and proofs of the results stated in the section outline. Before we begin, we prove the following technical lemma, which we need for verifying the growth conditions of the maximum principle of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67).\
\
### Lemma 5.1\
\
Let (M\_k, g), k \\in {\\mathbb {N}}, satisfy \|\\textrm{Rm}\_g\|\_g \\le K. Then\
\
\\begin{aligned} \|a\_s\|, \|Qb\_s\| , \|Q^2\| = O\\big (\\exp (2\\sqrt{K} s)\\big ). \\end{aligned}\
\
### Proof\
\
By the curvature components listed in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11) we see that\
\
\\begin{aligned} \\bigg \|\\frac{a\_{ss}}{a}\\bigg \|, \\left\| \\frac{b\_{ss}}{b}\\right\| \\le K. \\end{aligned}\
\
Integrating\
\
\\begin{aligned} b\_{ss} \\le b K \\end{aligned}\
\
shows that\
\
\\begin{aligned} b = O\\big (\\exp (\\sqrt{K} s)\\big ). \\end{aligned}\
\
From Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) we have\
\
\\begin{aligned} Q^2 \\le \\frac{5}{3} K b^2, \\end{aligned}\
\
from which we conclude that\
\
\\begin{aligned} Q^2 = O\\big (\\exp (2\\sqrt{K} s)\\big ). \\end{aligned}\
\
Similarly, Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) shows\
\
\\begin{aligned} \|b\_s\| \\le \\sqrt{5K} b, \\end{aligned}\
\
from which we deduce that\
\
\\begin{aligned} \|Qb\_s\| \\le \\sqrt{\\frac{25}{3}} K b^2, \\end{aligned}\
\
and hence\
\
\\begin{aligned} \|Qb\_s\| = O\\big (\\exp (2\\sqrt{K} s)\\big ). \\end{aligned}\
\
Finally,\
\
\\begin{aligned} \|a\_{ss}\| \\le a K \\end{aligned}\
\
shows that\
\
\\begin{aligned} \|a\_s\| = O\\big (\\exp (\\sqrt{K} s)\\big ). \\end{aligned}\
\
This concludes the proof. \\square\
\
Now we begin proving the conserved inequalities listed above.\
\
### Lemma 5.2\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature. Then the inequality\
\
\\begin{aligned} Q \\le 1 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
Define the quantity {\\tilde{Q}} = 1 - Q. From the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ we see\
\
\\begin{aligned} \\partial \_t {\\tilde{Q}} = {\\tilde{Q}}\_{ss} + 3 \\frac{b\_s}{b} {\\tilde{Q}}\_s + {\\tilde{Q}} \\left( -\\frac{4}{b^2} Q(1+Q) \\right) . \\end{aligned}\
\
As Q \\ge 0 everywhere, the coefficient -\\frac{4}{b^2} Q(1+Q) is non-positive. Furthermore, by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31) we have \|{\\tilde{Q}}\| = o(\\exp (s^2)). Therefore we may apply the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) to deduce that {\\tilde{Q}} \\ge 0 on M\_k \\times \[0,T\]. The desired result thus follows. \\square\
\
### Lemma 5.3\
\
Let (M\_k, g(t)), t\\in \[0,T\], k = 1,2, be a Ricci flow with bounded curvature. Then the inequality\
\
\\begin{aligned} x \\le 0 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
The evolution equation of _x_, as derived in Appendix A, is\
\
\\begin{aligned} \\partial \_t x&= L\[x\] - \\frac{2}{b^2}\\big (2 Q^2 + y^2\\big ) x - \\frac{2}{b^2}\\big (Q^2 +2 \\big ) y^2 \\nonumber \\\&\\le L\[x\] - \\frac{2}{b^2}\\big (2 Q^2 + y^2\\big ) x. \\end{aligned}\
\
(5.7)\
\
\
Note that \|x\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Therefore applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) yields the desired result. \\square\
\
### Remark 5.4\
\
Note that x = k - 2 at s=0 by the boundary conditions ( [1.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ3)). Therefore the result can only hold for k = 1,2.\
\
### Lemma 5.5\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature. Then the inequality\
\
\\begin{aligned} y \\le 0 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
Let K >0 such that\
\
\\begin{aligned} \\sup \_{M\_k \\times \[0,T\]} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} < K. \\end{aligned}\
\
Since _y_ is an odd quantity, we consider the quantity Qy = Qb\_s - Q^2 instead. Its evolution equation is\
\
\\begin{aligned} \\partial \_t Qy = L\[Qy\] - 2 \\frac{Qy}{b^2}\\left( 2\\big (Q^2+x\\big ) + Qy + y^2 \\right) . \\end{aligned}\
\
(5.8)\
\
\
Note that\
\
\\begin{aligned} - \\frac{2}{b^2}\\left( 2\\big (Q^2+x\\big ) + Qy + y^2 \\right)&= - \\frac{2}{b^2} \\left( 4Q^2 -4 + b^2 M\_1 + Qb\_s + b\_s^2 \\right) \\\&\\le \\frac{8}{b^2} + 2K + 2 \\frac{\|Q\|\|b\_s\|}{b^2} \\\&\\le \\frac{8}{b^2} + 2K + \\frac{Q^2}{b^2}+ \\frac{b^2\_s}{b^2}, \\end{aligned}\
\
where M\_1 is one of the curvature components listed in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11). By Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) we see that for some C>0,\
\
\\begin{aligned} - \\frac{2}{b^2}\\left( 2\\big (Q^2+x\\big ) + Qy + y^2 \\right) \\le C K \\quad \\text {on } \\, M\_k \\times \[0,T\]. \\end{aligned}\
\
Furthermore \|Qy\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Now the result follows from applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17). \\square\
\
### Lemma 5.6\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature. If the initial metric _g_(0) satisfies a\_s, b\_s \\ge 0, then a\_s, b\_s \\ge 0 for all times t\\in \[0,T\].\
\
### Proof\
\
The evolution equations ( [5.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ38)) and ( [5.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ39)) of a\_s and Qb\_s can be written as a system of weakly coupled parabolic equations\
\
\\begin{aligned}&\\partial \_t a\_s = L\[a\_s\] - \\left( 2 \\left( \\frac{b\_s}{b}\\right) ^2 + 6\\frac{Q^2}{b^2} \\right) a\_s + 8 \\frac{Q^2}{b^2} (Qb\_s), \\end{aligned}\
\
(5.9)\
\
\
\\begin{aligned}&\\partial \_t Qb\_s = L\[Qb\_s\] + 4 \\frac{Q^2}{b^2} a\_s + \\left( \\frac{8-10Q^2}{b^2} - 2 \\left( \\frac{b\_s}{b}\\right) ^2 \\right) (Qb\_s). \\end{aligned}\
\
(5.10)\
\
\
By Lemmas [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) and [3.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar20) the zeroth order coefficients of a\_s and Qb\_s are bounded. Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31) shows that \|a\_s\|, \|b\_s\| = o(\\exp (s^2)). Finally, note that the off-diagonal coefficients 8\\frac{Q^3}{b^2} and 4 \\frac{Q^2}{b^2} are non-negative. Thus the desired result follows by the maximum principle for weakly coupled parabolic equations of Lemma [3.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar25). \\square\
\
### Lemma 5.7\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature satisfying y \\le 0, Q \\le 1 and a\_s, b\_s \\ge 0. Then for C\\ge 2 the inequality\
\
\\begin{aligned} a\_s \\le C \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
Define the quantity A :=a\_s - C. Then from the evolution equation ( [5.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ44)) of a\_s it follows that\
\
\\begin{aligned} \\partial \_t A&= L\[A\] - \\left( 2 \\left( \\frac{b\_s}{b}\\right) ^2 + 6\\frac{Q^2}{b^2} \\right) A + \\frac{1}{b^2}\\big (8Q^3 b\_s - 6CQ^2 - 2 Cb\_s^2 \\big ). \\end{aligned}\
\
Fix C \\ge 2. Then\
\
\\begin{aligned} 8Q^3 b\_s - 6CQ^2 - 2 Cb\_s^2 \\le 8 Q^4 - 6 C Q^2 \\le (8 - 6C)Q^2 \\le 0, \\end{aligned}\
\
where we used Q \\le 1 and y = b\_s - Q \\le 0. As \|A\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31) it follows from the maximum principle of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) that the inequality A \\le 0 is preserved by the Ricci flow. This proves the desired result. \\square\
\
### Lemma 5.8\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature satisfying y \\le 0, b\_s \\ge 0 and Q \\le 1. Then the inequality\
\
\\begin{aligned} T\_1 = a\_s + 2Q^2 - 2 \\ge 0 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
The evolution equation of T\_1 is\
\
\\begin{aligned} \\partial \_t T\_1&= L\[T\_1\] + \\frac{1}{b^2} \\left\[ - 4\\big (1+Q^2\\big )y^2 + 8Q\\big (1-2Q^2 \\big )y + 16Q^2\\big (1-Q^2\\big )\\right\] \\nonumber \\\&\\qquad + T\_1 \\frac{2 y}{b^2}\\left( 2Q- y\\right) , \\end{aligned}\
\
(5.11)\
\
\
which can be derived from the evolution equations ( [5.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ38)), ( [5.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ39)) and ( [5.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ40)) for a\_s, Qb\_s and Q^2 listed above. Inspecting the quadratic expression\
\
\\begin{aligned} - 4\\big (1+Q^2\\big )y^2 + 8Q\\big (1-2Q^2 \\big )y + 16Q^2\\big (1-Q^2\\big ), \\end{aligned}\
\
(5.12)\
\
\
we see that when y=0 it is equal to\
\
\\begin{aligned} 16Q^2\\big (1-Q^2\\big ) \\ge 0, \\end{aligned}\
\
and when y = - Q it is equal to\
\
\\begin{aligned} 4Q^2\\big (1- Q^2\\big ) \\ge 0. \\end{aligned}\
\
As y = b\_s - Q \\in \[-Q,0\] by the assumptions y \\le 0, b\_s \\ge 0 and Q \\le 1, and furthermore the quadratic expression ( [5.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ47)) is concave in _y_, we conclude that\
\
\\begin{aligned} \\partial \_t T\_1 \\ge L\[T\_1\] + \\frac{2y}{b^2}\\left( 2Q- y\\right) T\_1. \\end{aligned}\
\
Note that the zeroth order coefficient of T\_1 is bounded by Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18). Furthermore \|T\_1\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Hence the result follows from applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17). \\square\
\
Below we prove some further preserved conditions. These can be skipped on the first reading of the paper.\
\
### Lemma 5.9\
\
Let (M\_k, g(t)), t\\in \[0,T\], k = 1, 2, be a Ricci flow with bounded curvature satisfying Q \\le 1. Then the condition\
\
\\begin{aligned} T\_2 = Qy - x = - a\_s + Qb\_s + 2\\big ( 1 - Q^2 \\big ) \\ge 0 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
Note that T\_2 = 2 - k when s = 0 by the boundary conditions ( [1.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ3)). Therefore the result can only hold true for k = 1,2. The evolution equations of T\_2 is\
\
\\begin{aligned} \\partial \_t T\_2&= L\[T\_2\] + \\frac{4}{b^2}\\big (1- Q^2\\big ) y^2 -2 \\frac{T\_2}{b^2} \\big ( \\left( b\_s-2Q\\right) ^2+ Q^2\\big ). \\end{aligned}\
\
(5.13)\
\
\
The coefficients are bounded by Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18). Furthermore \|T\_2\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Therefore applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) yields the desired result. \\square\
\
### Lemma 5.10\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature satisfying Q \\le 1. Then the inequality\
\
\\begin{aligned} T\_3 = a\_s - Qb\_s - Q^2 + 1 \\ge 0 \\end{aligned}\
\
is preserved by the Ricci flow.\
\
### Proof\
\
The evolution equations of T\_3 is\
\
\\begin{aligned} \\partial \_t T\_3&= L\[T\_3\] + \\frac{2}{b^2} \\big (1 - Q^2\\big ) y^2 - 2 \\frac{T\_3}{b^2} \\big ( (b\_s + Q)^2+ 4Q^2\\big ). \\end{aligned}\
\
(5.14)\
\
\
Note that the coefficients are bounded by Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18). Furthermore \|T\_3\| = o(\\exp (s^2)) by Lemma [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar31). Applying the maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) yields the desired result. \\square\
\
### Lemma 5.11\
\
Let (M\_k, g(t)), t\\in \[0,T\], k \\ge 1, be a Ricci flow with bounded curvature satisfying y \\le 0, b\_s \\ge 0 and Q \\le 1. Then the inequality\
\
\\begin{aligned} \\min (T\_1, T\_4) \\ge 0 \\end{aligned}\
\
is preserved by the Ricci flow. Here\
\
\\begin{aligned} T\_1&= a\_s + 2Q^2 - 2,\\\ T\_4&= a\_s - \\frac{1}{2} Q b\_s - \\big (1 - Q^2\\big ). \\end{aligned}\
\
### Proof\
\
By Lemma [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar44) we already know that the inequality\
\