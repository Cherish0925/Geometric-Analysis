---
retention_scope: session
part: 7
total_parts: 7
---

[Part 7/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

As \\big \|\\frac{b\_{ss}}{b}\\big \| \\le K, b \\rightarrow 0 and b\_s \\rightarrow 1 as s \\rightarrow 0, we see \\Psi (s) = O(K) as s\\rightarrow 0. By similar reasoning one shows that\
\
\\begin{aligned} s \\partial \_s \\Psi (s)&= \\frac{ 2 - 4\\left( \\frac{b}{s}\\right) ^2 + 2 \\left( \\frac{b}{s}\\right) b\_s}{s^2} \\\&= -\\frac{3 b\_{ss}(s\_0)}{s}+\\frac{2 b\_{ss}(s\_1)}{s}-b\_{ss}(s\_0)^2+b\_{ss}(s\_1) b\_{ss}(s\_0) \\end{aligned}\
\
and\
\
\\begin{aligned} s^2 \\partial \_{ss} \\Psi (s)&= \\frac{2 b b\_{ss}-16 \\left( \\frac{b}{s}\\right) b\_s + 2 b\_s^2 +20 \\left( \\frac{b}{s}\\right) ^2 -6}{s^2} \\\&= b\_{ss}(s\_0) b\_{ss}(s)+\\frac{2 b\_{ss}(s)}{s}+\\frac{12 b\_{ss}(s\_0)}{s}-\\frac{12 b\_{ss}(s\_1)}{s} \\\&\\quad +5 b\_{ss}(s\_0)^2-8 b\_{ss}(s\_1) b\_{ss}(s\_0)+2 b\_{ss}(s\_1)^2 \\end{aligned}\
\
are of order _O_( _K_) as s \\rightarrow 0. \\square\
\
Next, extend _g_ to the origin by setting g = \\delta \_{ij} there. As\
\
\\begin{aligned} s^2 \\delta \_{ij} - x\_i x\_j = O(s^2) \\end{aligned}\
\
it follows by Claim 1 that this defines a continuous extension of _g_ to the origin.\
\
A computation shows\
\
\\begin{aligned} \\partial \_k g\_{ij} = \\left( 2 x\_k \\delta \_{ij} - \\delta \_{ik} x\_j - x\_i \\delta \_{jk} \\right) \\Psi (s) +\\big ( s^2 \\delta \_{ij} - x\_i x\_j \\big ) \\frac{x\_k}{s}\\partial \_s \\Psi (s). \\end{aligned}\
\
As\
\
\\begin{aligned} 2 x\_k \\delta \_{ij} - \\delta \_{ik} x\_j - x\_i \\delta \_{jk} = O(s) \\end{aligned}\
\
and\
\
\\begin{aligned} \\big ( s^2 \\delta \_{ij} - x\_i x\_j \\big ) \\frac{x\_k}{s} = O(s^2), \\end{aligned}\
\
it follows that we may continuously extend \\partial \_k g\_{ij} to the origin by setting \\partial \_k g\_{ij} = 0 there. Finally, note that\
\
\\begin{aligned} \\partial \_k \\partial \_l g\_{ij} = O(1) \\Psi + O(s)\\partial \_s \\Psi + O(s^2) \\partial \_{ss} \\Psi = O(K). \\end{aligned}\
\
Hence \\partial \_k \\partial \_l g\_{ij} is bounded in a neighborhood around, but excluding the origin. This shows that \\partial \_k g\_{ij} is Lipschitz. \\square\
\
Next, we prove the boundedness of the gradient of the curvature tensor. For this we recall some interior curvature estimates. Note the following differential inequalities for the evolution of the curvature tensor and its derivatives under Ricci flow (see for instance \[ [7](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR7 "Chow, B., Knopf, D.: The Ricci Flow: An Introduction. Mathematical Surveys and Monographs, Vol. 110. AMS, Providence, RI (2004)"),  Chapter 7\]):\
\
\\begin{aligned}&\\big (\\partial \_t - \\Delta \\big ) \|\\textrm{Rm}\|^2 \\le - 2\|\\nabla \\textrm{Rm}\|^2 + 16 \|\\textrm{Rm}\|^3, \\end{aligned}\
\
(B.1)\
\
\
\\begin{aligned}&\\big (\\partial \_t - \\Delta \\big ) \|\\nabla ^m \\textrm{Rm}\|^2 \\le - 2 \|\\nabla ^{m+1} \\textrm{Rm}\|^2 \\nonumber \\\&\\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad \\quad + \\sum \_{j=0}^m c\_{mj} \|\\nabla ^j \\textrm{Rm}\| \\cdot \|\\nabla ^{m-j} \\textrm{Rm}\| \\cdot \|\\nabla ^m \\textrm{Rm}\|. \\end{aligned}\
\
(B.2)\
\
\
Here c\_{mj} are positive constants depending on _j_, _m_ and the dimension of the manifold only. Note also that the Laplacian is with respect to the evolving metric _g_( _t_). Using these inequalities one can show the following interior derivative estimate (see for instance \[ [6](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR6 "Cao, H.D., Zhu, X.P.: A complete proof of the Poincaré and geometrization conjectures—application of the Hamilton–Perelman theory of the Ricci flow. Asian J. Math. 10(2), 165–492 (2006)"),  Theorem 1.4.2\]).\
\
### Theorem B.3\
\
(Shi’s interior estimates)   There exist positive constants \\theta , C\_m, m \\in {\\mathbb {N}}, depending on the dimension _n_ only, such that the following holds: Let _M_ be a manifold of dimension _n_ and 0 < T \\le \\frac{\\theta }{K}. Assume that _g_( _t_), t \\in \[0, T\], is a solution to the Ricci flow on an open neighborhood _U_ of _M_ and\
\
\\begin{aligned} \|\\textrm{Rm}\| < K \\quad \\text { on } \\, B\_{g(0)}\\left( p, r\\right) \\times \[0,T\]. \\end{aligned}\
\
If for p \\in U and r>0 the closed set \\overline{B\_{g(0)}(p, r)} is contained in _U_, then\
\
\\begin{aligned} \|\\nabla ^m \\textrm{Rm}\|^2<C\_m K^2 \\left( \\frac{1}{r^{2m}} + \\frac{1}{t^m} + K^m\\right) \\, \\quad \\text { on } \\, B\_{g(0)}\\bigg (p, \\frac{r}{2}\\bigg ) \\times (0,T\]. \\end{aligned}\
\
Next, we prove that for all \\tau > 0 the gradient \|\\nabla \\textrm{Rm}\| is bounded on ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \[\\tau , T\]. First note that due to Shi’s estimates of Theorem [B.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar180)\
\
\\begin{aligned} \|\\nabla \\textrm{Rm}\_{g(t)}\|\_{g(t)}(p) = O\\left( \\frac{1}{d\_{g(t)}(p, 0)}\\right) \\, \\quad \\text { on } ({\\mathbb {R}}^4 \\setminus \\{0\\})\\times \[\\tau , T\]. \\end{aligned}\
\
Furthermore, from ( [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ115)) and an application of Kato’s inequality to show that\
\
\\begin{aligned} \|\\nabla \|\\nabla \\textrm{Rm}\|\| \\le \|\\nabla ^2 \\textrm{Rm}\|, \\end{aligned}\
\
it follows that\
\
\\begin{aligned} \\big ( \\partial \_t - \\Delta \\big ) \|\\nabla \\textrm{Rm}\| \\le C\|\\textrm{Rm}\|\|\\nabla \\textrm{Rm}\|. \\end{aligned}\
\
Hence when curvature is bounded by _K_, the function u :=e^{-CKt} \|\\nabla \\textrm{Rm}\| is a subsolution to the heat equation, i.e.\
\
\\begin{aligned} \\big (\\partial \_t - \\Delta \\big ) u \\le 0. \\end{aligned}\
\
With help of a De Giorgi–Nash–Moser iteration argument, this is enough to prove that _u_ is bounded for t > \\tau . We carry this out in the lemma below:\
\
### Lemma B.4\
\
Let ({\\mathbb {R}}^4 \\setminus \\{0\\},g(t)),  t\\in \[0,T\], be a Ricci flow as in Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175). Then for any \\tau > 0 there exists a C = C(K, \\tau ) > 0 such that\
\
\\begin{aligned} \|\\nabla \\textrm{Rm}\| < C \\end{aligned}\
\
on ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \[\\tau , T\].\
\
### Proof\
\
As shown above, the function u = e^{-CKt} \|\\nabla \\textrm{Rm}\| is a subsolution to the heat equation, i.e.\
\
\\begin{aligned} \\left( \\partial \_t - \\Delta \\right) u \\le 0. \\end{aligned}\
\
By Lemma [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar176) we may choose Euclidean coordinates x^i, i = 1, 2, 3, 4, on {\\mathbb {R}}^4 for which _g_(0) is C^{1,1}. Take s^2 = \\sum \_i (x^i)^2 and write B\_R(x) for the ball centered at _x_ with radius _R_ with respect to _g_(0).\
\
Since the curvature of _g_( _t_) is bounded on ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \[0,T\], there exists a \\lambda > 0 such that\
\
\\begin{aligned} \\frac{1}{\\lambda } g(0) \\le g(t) \\le \\lambda g(0) \\,\\quad \\text { on } \\, \\big ({\\mathbb {R}}^4 \\setminus \\{0\\}\\big ) \\times \[0,T\]. \\end{aligned}\
\
Therefore, Shi’s interior estimates imply\
\
\\begin{aligned} u( \\cdot , t) = O\\left( \\frac{1}{s}\\right) \\,\\quad \\text { for } \\, t \\in \[\\tau , T\]. \\end{aligned}\
\
Hence it suffices to show that for some R>0 the function _u_ is bounded on B\_R(0) \\times \[\\tau , T\]. We achieve this via a De Giorgi–Nash–Moser iteration argument. In the claim below we derive the crucial estimate.\
\
### Claim 1\
\
Let \\delta > 0, p \\ge 2, R\_0 \\in \[1,10\] and t\_0 \\in \[\\delta , T). Then there exists a constant C = C(K, \\delta , T) >0 such that the following holds: If u \\in L^p(B\_{R\_0} \\times \[t\_0, T\]), then for R\_1 \\in \[\\frac{1}{2}, R\_0) and t\_1 \\in (t\_0, T\]\
\
\\begin{aligned} \\left\\Vert u\\right\\Vert \_{L^{2p}(B\_{R\_1}(0) \\times \[t\_1,T\])} \\le \\left\[ C\\left( \\frac{p^2}{(R\_0 - R\_1)^2} + \\frac{1}{t\_1-t\_0} \\right) \\right\] ^{\\frac{1}{p}} \\left\\Vert u\\right\\Vert \_{L^{p}(B\_{R\_0}(0) \\times \[t\_0,T\])}. \\end{aligned}\
\
### Proof of Claim 1\
\
In the following a constant _C_ is assumed to only depend on _K_, \\delta  and _T_ and might vary from line to line. Fix a number A > 1 that we later take to \\infty . Then choose a C^2 function F: {\\mathbb {R}}\_{\\ge 0} \\rightarrow {\\mathbb {R}} with the following properties:\
\
1. (1)\
F(s) = s^p for  s \\le A.\
\
2. (2)\
_F_ is linear for s \\ge A+1 with slope pA^{p-1} + 1.\
\
3. (3)\
On \[A,A+1\] take _F_( _s_) to be defined such that F''\\ge 0.\
\
\
We see that these properties imply that F'(s) \\le ps^{p-1}. Next, define the cut-off functions \\eta \_\\epsilon , \\epsilon >0, and \\phi : {\\mathbb {R}}^4 \\rightarrow {\\mathbb {R}}. For this take a smooth function h: {\\mathbb {R}}\\rightarrow {\\mathbb {R}} with h = 0 on (-\\infty ,\\frac{1}{2}\] and h = 1 on \[1,\\infty ). Then define\
\
\\begin{aligned} \\eta \_\\epsilon = h\\left( \\frac{s}{\\epsilon }\\right) \\end{aligned}\
\
and\
\
\\begin{aligned} \\phi = h\\left( \\frac{R\_0-s}{R\_0-R\_1}\\right) . \\end{aligned}\
\
That is, \\phi = 1 on B\_{R\_1}(0) and \\phi = 0 on {\\mathbb {R}}^4 \\setminus B\_{R\_0}(0). Clearly, \|\\nabla \\phi \|\_{g(t)} \\le \\frac{c}{R\_0 - R\_1} and \|\\nabla \\eta \_\\epsilon \|\_{g(t)} \\le \\frac{c}{\\epsilon } for some universal constant _c_ depending on _h_ and \\lambda  only.\
\
Since u \\in L^p(B\_{R\_0} \\times \[t\_0, T\]) is a positive function there exists a t' \\in \[t\_0, t\_1\] such that\
\
\\begin{aligned} \\int \_{B\_{R\_0}(0)} u^p(\\cdot , t') \\; {{d}}x \\le \\frac{1}{t\_0-t\_1} \\int \_{t\_0}^T \\int \_{B\_{R\_0}(0)} u^p \\; {{d}}x \\; {{d}}t. \\end{aligned}\
\
(B.3)\
\
\
Next, we compute via integration by parts\
\
\\begin{aligned} \\frac{d}{dt} \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F(u) \\phi ^2 \\; {{d}} x&= \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F'(u) \\Delta u \\phi ^2 \\; {{d}} x \\\&= -\\int \_{{\\mathbb {R}}^4} \\nabla \\eta \_\\epsilon F'(u) \\nabla u \\phi ^2 \\; {{d}} x -\\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F''(u) \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\\&\\quad \\; -\\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F'(u) \\nabla u \\nabla \\phi ^2 \\; {{d}} x. \\end{aligned}\
\
Integrating with respect to time from t' to _T_ and noting that\
\
\\begin{aligned} \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F(u(\\cdot , T)) \\phi ^2 \\; {{d}} x \\ge 0, \\end{aligned}\
\
we obtain\
\
\\begin{aligned} \\int \_{t'}^T \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F''(u) \|\\nabla u\|^2 \\phi ^2 \\; {{d}}x \\; {{d}}t&\\le \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F(u(\\cdot , t')) \\phi ^2 \\; {{d}}x \\nonumber \\\ {}&\\quad -\\int \_{t'}^T\\int \_{{\\mathbb {R}}^4} \\nabla \\eta \_\\epsilon F'(u) \\nabla u \\phi ^2 \\; {{d}}x \\; {{d}}t \\nonumber \\\&\\quad -\\int \_{t'}^T\\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F'(u) \\nabla u \\nabla \\phi ^2 \\; {{d}}x \\; {{d}}t \\nonumber \\\&:=I\_1 - I\_2 - I\_3. \\end{aligned}\
\
(B.4)\
\
\
Next we estimate each of these integrals I\_1, I\_2 and I\_3 separately, in order to analyze their behaviors as \\epsilon \\rightarrow 0. For the first integral we have\
\
\\begin{aligned} I\_1 \\le \\int \_{B\_{R\_0}} u^p(\\cdot , t') \\; {{d}}x \\le \\frac{1}{t\_1-t\_0} \\left\\Vert u\\right\\Vert ^p\_{L^p(B\_{R\_0}(0)\\times \[t\_0,T\])}. \\end{aligned}\
\
For the second integral I\_2, note that Shi’s estimates and Kato’s inequality yield\
\
\\begin{aligned} \|\\nabla u\| = \\bigg \|\\nabla \\big ( e^{-CKt}\|\\nabla \\textrm{Rm}\| \\big )\\bigg \| \\le \|\\nabla ^2 \\textrm{Rm}\| = O\\left( \\frac{1}{s^2}\\right) \\, \\quad \\text { as } \\, s \\rightarrow 0. \\end{aligned}\
\
As \|\\nabla \\eta \_\\epsilon \| \\le \\frac{c}{\\epsilon }, \|F'\| \\le pA^{p-1} +1 and \\phi ^2 =1 in a neighborhood of 0, we see that\
\
\\begin{aligned} \|\\nabla \\eta \_\\epsilon \| \\cdot \|F'(u)\|\\cdot \|\\nabla u\|\\cdot \|\\phi ^2\| \\le C \\epsilon ^{-3} \\big (pA^{p-1}+1\\big ) \\,\\quad \\text { on } \\, B\_{\\epsilon }(0). \\end{aligned}\
\
As \\text {vol}\_{g(t)}(B\_\\epsilon (0)) \\le C \\epsilon ^4 we obtain\
\
\\begin{aligned} \|I\_2\| \\le C \\epsilon \\big (pA^{p-1}+1\\big ). \\end{aligned}\
\
For the final integral I\_3, recall that by definition 0 \\le F'(u) \\le pu^{p-1}. Furthermore, \|\\nabla \\phi ^2\| has support in B\_{R\_0}(0)\\setminus B\_{R\_1}(0) and is bounded by \\frac{2c}{R\_0-R\_1}. As R\_1 \\ge \\frac{1}{2} by assumption, Shi’s estimates imply that on this set \|\\nabla u\| and _u_ are bounded by some constant _C_. Thus\
\
\\begin{aligned} \|I\_3\|&\\le \\frac{2c pC^{p}}{R\_0-R\_1} \\text {vol}\\left( B\_{R\_0}(0)\\setminus B\_{R\_1}(0)\\right) \\\&\\le pC^{p+1}, \\end{aligned}\
\
where we used that\
\
\\begin{aligned} \\text {vol}\\big (B\_{R\_0}(0)\\setminus B\_{R\_1}(0)\\big ) \\le C\\big ( R^4\_0 -R^4\_1 \\big ) \\le C \\left( R\_0 - R\_1\\right) , \\end{aligned}\
\
as \\frac{1}{2} \\le R\_0 \\le R\_1 \\le 10 by assumption. This shows that I\_3 is convergent. Now split the integral I\_3 as\
\
\\begin{aligned} I\_3 = \\int \_{t'}^T \\int \_{\\{u \\le A\\}} \\eta \_\\epsilon F'(u) \\nabla u \\nabla \\phi ^2 \\; {{d}}x \\; {{d}}t + I\_4, \\end{aligned}\
\
where\
\
\\begin{aligned} I\_4 = \\int \_{t'}^T \\int \_{\\{u \\ge A\\}} \\eta \_\\epsilon F'(u) \\nabla u \\nabla \\phi ^2 \\; {{d}}x \\; {{d}}t. \\end{aligned}\
\
As I\_3 is convergent, we see that I\_4 \\rightarrow 0 as A \\rightarrow \\infty . Observe that by Young’s inequality\
\
\\begin{aligned} p u^{p-1} \|\\nabla u\| \|\\nabla \\phi ^2\| = \\phi u^{\\frac{p-2}{2}} \|\\nabla u\| \\cdot 2p u^{\\frac{p}{2}} \|\\nabla \\phi \| \\le \\frac{1}{2} u^{p-2} \|\\nabla u\|^2 \\phi ^2 + 2p^2 \|\\nabla \\phi \|^2 u^p. \\end{aligned}\
\
Moreover,\
\
\\begin{aligned} \|\\nabla \\phi \|^2 \\le \\left( \\frac{c}{R\_0-R\_1}\\right) ^2. \\end{aligned}\
\
Hence we obtain\
\
\\begin{aligned} \|I\_3\|&\\le \\int \_{t'}^T\\int \_{\\{u \\le A\\}} \\frac{1}{2} \\eta \_\\epsilon u^{p-2} \|\\nabla u\|^2 \\phi ^2 + 2 p^2 \\eta \_\\epsilon \|\\nabla \\phi \|^2 u^p \\; {{d}} x \\; {{d}} t + I\_4 \\\&\\le \\int \_{t'}^T\\int \_{\\{u \\le A\\}} \\frac{1}{2} \\eta \_\\epsilon u^{p-2} \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\; {{d}} t + \\frac{Cp^2}{(R\_0-R\_1)^2} \\left\\Vert u\\right\\Vert ^p\_{L^p(B\_{R\_0}(0)\\times \[t\_0,T\])} + I\_4. \\end{aligned}\
\
Next, note that F''(u) = p(p-1)u^{p-2} for u \\le A and F'' \\ge 0 everywhere. Therefore\
\
\\begin{aligned} \\int \_{t'}^T \\int \_{{\\mathbb {R}}^4} \\eta \_\\epsilon F''(u) \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\; {{d}} t&\\ge \\int \_{t'}^T \\int \_{\\{u \\le A\\}} \\eta \_\\epsilon p(p-1)u^{p-2} \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\; {{d}} t. \\end{aligned}\
\
Substituting this inequality and the inequalities for \|I\_1\|, \|I\_2\| and \|I\_3\| derived above into ( [B.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ117)), we deduce\
\
\\begin{aligned} \\left( p(p-1) - \\frac{1}{2} \\right)&\\int \_{t'}^T \\int \_{\\{u \\le A\\}} \\eta \_\\epsilon u^{p-2} \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\; {{d}} t \\\&\\le C\\left( \\frac{p^2}{(R\_0-R\_1)^2} + \\frac{1}{t\_1-t\_0} \\right) \\left\\Vert u\\right\\Vert ^p\_{L^p(B\_{R\_0}(0)\\times \[t\_0,T\])} \\\ {}&\\quad + C \\epsilon (pA^{p-1}+1) + I\_4. \\end{aligned}\
\
Taking \\epsilon \\rightarrow 0 and then A \\rightarrow \\infty  yields\
\
\\begin{aligned} \\left( p(p-1) - \\frac{1}{2} \\right)&\\int \_{t'}^T \\int \_{{\\mathbb {R}}^4}u^{p-2} \|\\nabla u\|^2 \\phi ^2 \\; {{d}} x \\; {{d}} t \\\&\\le C\\left( \\frac{p^2}{(R\_0-R\_1)^2} + \\frac{1}{t\_1-t\_0} \\right) \\left\\Vert u\\right\\Vert ^p\_{L^p(B\_{R\_0}(0)\\times \[t\_0,T\])} \\end{aligned}\
\
by the monotone convergence theorem. Then note that\
\
\\begin{aligned} u^{p-2} \|\\nabla u\|^2 \\phi ^2 = \\frac{4}{p^2} \\big \|\\nabla u^{\\frac{p}{2}}\\big \|^2 \\phi ^2 \\end{aligned}\
\
and\
\
\\begin{aligned} \|\\nabla u^{\\frac{p}{2}}\|^2 \\phi ^2&= \\left\| \\nabla (\\phi u^{\\frac{p}{2}}) - u^{\\frac{p}{2}} \\nabla \\phi \\right\| ^2 \\\&\\ge \\left\| \\nabla (\\phi u^{\\frac{p}{2}})\\right\| ^2 + \\left\| u^{\\frac{p}{2}} \\nabla \\phi \\right\| ^2 - 2\\left\| \\nabla (\\phi u^{\\frac{p}{2}})\\right\| \\cdot \\left\| u^{\\frac{p}{2}} \\nabla \\phi \\right\| \\\&\\ge \\frac{1}{2}\\big \|\\nabla (\\phi u^{\\frac{p}{2}})\\big \|^2 - u^p \|\\nabla \\phi \|^2, \\end{aligned}\
\
where in the last line we applied Young’s inequality to bound the cross-term. Therefore\
\
\\begin{aligned} \\int \_{t'}^T \\int \_{{\\mathbb {R}}^4} \|\\nabla (\\phi u^{\\frac{p}{2}})\|^2 \\; {{d}} x \\; {{d}} t \\le C\\left( \\frac{p^2}{(R\_0-R\_1)^2} + \\frac{1}{t\_1-t\_0} \\right) \\left\\Vert u\\right\\Vert ^p\_{L^p(B\_{R\_0}(0)\\times \[t\_0,T\])} \\end{aligned}\
\
and applying the Sobolev inequality proves Claim 1. \\square\
\
Now we may iterate the estimate of Claim 1 to prove the desired result. First note that due to Shi’s estimates, for any R\_0> 0 and t\_0>0 we have that u \\in L^2(B\_{R\_0}(0)\\times \[t\_0, T\]). We take t\_0 = \\frac{\\tau }{2}, R\_0 = 2 + \\sqrt{\\frac{\\tau }{2}}, \\Delta t\_i = (\\Delta R\_i)^2 = \\frac{\\tau }{2^{i+1}}, p\_i = 2^{i+1} and\
\
\\begin{aligned}&R\_{i+1} = R\_{i} - \\Delta R\_i,\\\&t\_{i+1} = t\_{i} + \\Delta t\_i. \\end{aligned}\
\
Then inductively applying the estimate of Claim 1 and taking the limit as i \\rightarrow \\infty , we obtain\
\
\\begin{aligned} \\left\\Vert u\\right\\Vert \_{L^{\\infty }(B\_{2}(0)\\times \[\\tau , T\])} \\le C\_\\infty \\left\\Vert u\\right\\Vert \_{L^{2}(B\_{R\_0}(0)\\times \[\\frac{\\tau }{2}, T\])} < \\infty , \\end{aligned}\
\
where C\_\\infty > 0 is a positive constant. This proves the desired result. \\square\
\
Next, we prove that the higher derivatives of the curvature tensor are also bounded at positive times. For this we need a generalization of Shi’s estimates for the situation in which some of the derivatives of the curvature tensor are known to be bounded. In particular, we have\
\
### Theorem B.5\
\
(Shi’s interior estimates with derivative bounds) Let n \\ge 2 and m \\ge 1. Then for every choice of constant K>0 there exists constants \\theta > 0 and C>0 such that the following holds: Let _M_ be an open manifold _M_ of dimension _n_ and 0 < T \\le \\frac{\\theta }{K}. Assume that _g_( _t_), t\\in \[0,T\], is a solution to the Ricci flow on an open subset _U_ of _M_ and\
\
\\begin{aligned} \|\\nabla ^l \\textrm{Rm}\|&\\le K \\,\\quad \\textrm{on } \\, U \\times \[0, T\] \\, \\mathrm{and\\,\\, for } \\, l \\in \\{0, 1, 2, \\cdots , m\\}. \\end{aligned}\
\
If for p \\in U and r>0 the closed set \\overline{B\_{g(0)}(p, r)} is contained in _U_ then\
\
\\begin{aligned} \|\\nabla ^{m+1} \\textrm{Rm}\|^2 \\le C \\left( \\frac{1}{r^2} + \\frac{1}{t} + 1 \\right) \\,\\quad \\textrm{on } \\, B\_{g(0)}\\bigg (p, \\frac{r}{2}\\bigg ) \\times (0,T\]. \\end{aligned}\
\
### Proof\
\
We follow the proofs of \[ [6](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR6 "Cao, H.D., Zhu, X.P.: A complete proof of the Poincaré and geometrization conjectures—application of the Hamilton–Perelman theory of the Ricci flow. Asian J. Math. 10(2), 165–492 (2006)"),  Theorem 1.4.2\] and \[ [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR10 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)"),  Theorem 14.16\]. In the following the constant _C_ depends on _m_ and _n_ only and may vary from line to line. Consider the quantity\
\
\\begin{aligned} S= \\big ( BK^2 + \|\\nabla ^m \\textrm{Rm}\|^2 \\big ) \|\\nabla ^{m+1} \\textrm{Rm}\|^2, \\end{aligned}\
\
where B>0 is to be fixed later. With help of the differential inequality ( [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ115)) we obtain\
\
\\begin{aligned} \\partial \_t S&\\le \\Delta S - 2 \\nabla \|\\nabla ^m \\textrm{Rm}\|^2 \\nabla \|\\nabla ^{m+1} \\textrm{Rm}\|^2 - 2 \|\\nabla ^{m+1} \\textrm{Rm}\|^4 \\\&\\quad + \\sum \_j c\_{mj} \\cdot \|\\nabla ^j \\textrm{Rm}\| \\cdot \|\\nabla ^{m-j} \\textrm{Rm}\| \\cdot \|\\nabla ^m \\textrm{Rm}\| \\cdot \|\\nabla ^{m+1} \\textrm{Rm}\|^2 \\\&\\quad -2 \\big (BK^2 + \|\\nabla ^m \\textrm{Rm}\|^2 \\big ) \|\\nabla ^{m+2} \\textrm{Rm}\|^2\\\&\\quad + \\big ( BK^2 + \|\\nabla ^{m}\\textrm{Rm}\|^2 \\big ) \\sum \_j c\_{m+1 j} \\cdot \|\\nabla ^j \\textrm{Rm}\| \\cdot \|\\nabla ^{m+1-j} \\textrm{Rm}\| \\cdot \|\\nabla ^{m+1} \\textrm{Rm}\|. \\end{aligned}\
\
Using Cauchy’s inequality and the assumption that \|\\nabla ^l \\textrm{Rm}\| \\le K for l= 0, 1, 2, \\cdots m, we deduce\
\
\\begin{aligned} \\partial \_t S&\\le \\Delta S + 8K \|\\nabla ^{m+1} \\textrm{Rm}\|^2 \|\\nabla ^{m+2} \\textrm{Rm}\| - 2 \|\\nabla ^{m+1} \\textrm{Rm}\|^4 -2 BK^2 \|\\nabla ^{m+2} \\textrm{Rm}\|^2 \\\&\\quad + CK^3 \|\\nabla ^{m+1}\\textrm{Rm}\|^2 + CK^3(B+1) \\big (\|\\nabla ^{m+1} \\textrm{Rm}\|^2 + K \|\\nabla ^{m+1} \\textrm{Rm}\| \\big ). \\end{aligned}\
\
Noting that for all x \\in {\\mathbb {R}} we have x^2 + K x \\le 2 x^2 + \\frac{1}{4} K^2 we obtain with help of Young’s inequality that\
\
\\begin{aligned} \\partial \_t S&\\le \\Delta S - \|\\nabla ^{m+1}\\textrm{Rm}\|^4 + 2 \\left( 32 - B\\right) K^2 \|\\nabla ^{m+2} \\textrm{Rm}\|^2\\\&\\quad + CK^6 + CK^5(B+1) + CK^6(B+1)^2. \\end{aligned}\
\
Taking B = 32 and assuming without loss of generality that K>1, we obtain\
\
\\begin{aligned} \\partial \_t S \\le \\Delta S - \\frac{S^2}{C K^4} + C K^6. \\end{aligned}\
\
From here we may follow the proof of \[ [6](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR6 "Cao, H.D., Zhu, X.P.: A complete proof of the Poincaré and geometrization conjectures—application of the Hamilton–Perelman theory of the Ricci flow. Asian J. Math. 10(2), 165–492 (2006)"),  Theorem 1.4.2\] to deduce the desired result. \\square\
\
With help of Theorem [B.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar185) we inductively prove that the higher derivatives of the curvature tensor are bounded.\
\
### Lemma B.6\
\
Let ({\\mathbb {R}}^4 \\setminus \\{0\\},g(t)),  t\\in \[0,T\], be a Ricci flow as in Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175). Then for any \\tau > 0 there exist constants C\_m = C\_m(K, \\tau ) > 0, m \\in {\\mathbb {N}}, such that\
\
\\begin{aligned} \|\\nabla ^m \\textrm{Rm}\| < C\_m \\end{aligned}\
\
on ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \\left\[ \\tau , T\\right\] .\
\
### Proof\
\
We prove this lemma by induction. By Lemma [B.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar181) the result is true for m=1. Assume that the result is true for m \\le N. Then there exist constants C\_l>0, l = 1, 2, 3, \\cdots , N such that\
\
\\begin{aligned} \|\\nabla ^l \\textrm{Rm}\| \\le C\_l \\quad \\text { on } \\, ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \\left\[ \\frac{\\tau }{4}, T\\right\] \\, \\text { and for } \\, l = 1, 2, 3, \\cdots , N. \\end{aligned}\
\
As in the proof of Lemma [B.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar181), choose coordinates x^i, i = 1, 2, 3,4, such that _g_(0) can be extended to a C^{1,1} metric on {\\mathbb {R}}^4, and write s^2 = \\sum \_i (x^i)^2. As the curvature of _g_( _t_), t \\in \[0,T\], is bounded there exists a \\lambda > 0 such that\
\
\\begin{aligned} \\frac{1}{\\lambda } g(0) \\le g(t) \\le \\lambda g(0) \\, \\quad \\text { on } \\, \\big ({\\mathbb {R}}^4 \\setminus \\{0\\}\\big ) \\times \[0, T\]. \\end{aligned}\
\
By the modified Shi’s estimates of Theorem [B.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar185) we see that\
\
\\begin{aligned} \|\\nabla ^{N+1} \\textrm{Rm}\| \\le C\\left( \\frac{1}{s} + 1\\right) \\, \\text { on } \\, ({\\mathbb {R}}^4 \\setminus \\{0\\}) \\times \\left\[ \\frac{\\tau }{2}, T\\right\] , \\end{aligned}\
\
for some _C_ that depends on \\tau , K, and C\_l, l = 1, 2, \\cdots , N, only. In particular, this implies that for all R>0 the function u \\in L^2(B\_R(0))\\times \[0,T\]. By the differential inequality ( [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ115)) for the evolution of the curvature derivatives we see that\
\
\\begin{aligned} \\left( \\partial \_t - \\Delta \\right) \|\\nabla ^{N+1}\\textrm{Rm}\|^2 \\le - 2 \|\\nabla ^{N+2} \\textrm{Rm}\|^2 + CK^2\|\\nabla ^{N+1} \\textrm{Rm}\| + CK \|\\nabla ^{N+1} \\textrm{Rm}\|^2 \\end{aligned}\
\
and hence\
\
\\begin{aligned} \\left( \\partial \_t - \\Delta \\right) \|\\nabla ^{N+1}\\textrm{Rm}\| \\le CK \\big ( K + \|\\nabla ^{N+1} \\textrm{Rm}\|\\big ). \\end{aligned}\
\
Thus defining\
\
\\begin{aligned} u = e^{-CKt} \\big (\|\\nabla ^{N+1} \\textrm{Rm}\| + K\\big ) \\end{aligned}\
\
we deduce that\
\
\\begin{aligned} \\left( \\partial \_t - \\Delta \\right) u \\le 0. \\end{aligned}\
\
Now we are in the same setup as in the proof of Lemma [B.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar181). Therefore we may use the same De Giorgi–Nash–Moser iteration argument to show that _u_ and hence \|\\nabla ^{N+1} \\text {Rm}\| are bounded in {\\mathbb {R}}^4 \\times \[\\tau , T\]. This proves the desired result. \\square\
\
Now we may prove the main Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175):\
\
### Proof of Theorem B.1\
\
By Lemma [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar176) we can choose coordinates x^i, i = 1, 2, 3, 4, for {\\mathbb {R}}^4 such that _g_( _T_) can be extended to a C^{1,1} metric on all of {\\mathbb {R}}^4. Below we write g = g(T) for brevity. By \[ [13](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR13 "DeTurck, D.M., Kazdan, J.L.: Some regularity theorems in Riemannian geometry. Ann. Sci. Ecole Norm. Sup. (4) 14(3), 249–260 (1981)"), Lemma 1.2\] there exist C^{2,\\alpha } harmonic coordinates y^i: U \\rightarrow {\\mathbb {R}}, i =1 , 2, 3, 4, in an open neighborhood _U_ of {\\mathbb {R}}^4 containing the origin and satisfying\
\
1. (1)\
y^i = 0;\
\
2. (2)\
\\frac{\\partial y^i}{\\partial x^j} = \\delta ^i\_j\
\
\
at the origin. Furthermore, as _g_ is smooth on U \\setminus \\{0\\}, it follows from interior elliptic regularity that y^i are smooth on U \\setminus \\{0\\}. Write\
\
\\begin{aligned} g\_{ij} = g\\left( \\frac{\\partial }{\\partial y^i}, \\frac{\\partial }{\\partial y^j}\\right) \\quad \\text { and } \\quad \\textrm{Ric}\_{ij} = \\textrm{Ric}\_g\\left( \\frac{\\partial }{\\partial y^i}, \\frac{\\partial }{\\partial y^j}\\right) . \\end{aligned}\
\
We have that g\_{ij} \\in C^{1, \\alpha }(U) with respect to the y^i coordinates. Furthermore, g\_{ij} is smooth on U \\setminus \\{0\\}.\
\
By \[ [30](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR30 "Petersen, P.: Riemannian Geometry, 3rd Edition. Graduate Texts in Mathematics, Vol. 171. Springer, Cham (2016)"),  Chapter 10, Lemma 49\]) we have\
\
\\begin{aligned} \\frac{1}{2} \\Delta g\_{ij} + Q(g, \\partial g) = - \\textrm{Ric}\_{ij} \\quad \\text {on } U \\setminus \\{0\\}, \\end{aligned}\
\
(B.5)\
\
\
where Q(g, \\partial g) is some universal analytic expression that is polynomial in the matrix _g_, quadratic in \\frac{\\partial g}{\\partial y^i}, and has a denominator term depending on \\sqrt{\\textrm{det}\\,g\_{ij}}. Equation ( [B.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ118)) makes sense on all of _U_ if we interprete it in the weak sense.\
\
### Claim 1\
\
If g\_{ij}(y) \\in C^{k}(U) for k \\in {\\mathbb {N}}, then R\_{ij}(y) \\in C^{k-1, 1}(U).\
\
### Proof of Claim 1\
\
Writing\
\
\\begin{aligned} Y\_i = \\frac{\\partial }{\\partial y^i} \\quad \\text { for } \\, i = 1,2,3,4. \\end{aligned}\
\
on U \\setminus \\{0\\}, we have\
\
\\begin{aligned} \\frac{\\partial ^k}{\\partial y^{i\_1} \\partial y^{i\_2} \\cdots \\partial y^{i\_k}} \\textrm{Ric}\_{ij}&= Y\_{i\_1} Y\_{i\_2} \\cdots Y\_{i\_k} \\textrm{Ric}( Y\_i , Y\_j) \\\&= \\nabla \_{Y\_{i\_1}} \\nabla \_{Y\_{i\_2}} \\cdots \\nabla \_{Y\_{i\_k}} \\textrm{Ric}(Y\_i, Y\_j). \\end{aligned}\
\
Since covariant differentiation commutes with contractions, we can use the product rule to express the above derivative as a sum of terms, which only involve \\nabla ^m \\textrm{Ric}, m = 1, 2, \\cdots , k, and \\nabla ^m Y\_{i\_l}, m, l = 1, 2, \\cdots , k, contracted with Y\_i, Y\_j and Y\_{i\_l}, l = 1, 2, \\cdots , k. As by Lemma [B.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar187) all the derivatives of the curvature tensor are bounded and g\_{ij}(y) \\in C^{k}(U) we see that\
\
\\begin{aligned} \\frac{\\partial ^k}{\\partial y^{i\_1} \\partial y^{i\_2} \\cdots \\partial y^{i\_k}} \\textrm{Ric}\_{ij} \\end{aligned}\
\
is bounded as well. Hence the _k_-th spatial derivatives \\partial ^k \\textrm{Ric}\_{ij} are bounded, which implies that \\partial ^{k-1} \\textrm{Ric}\_{ij} is a Lipschitz function and can be continuously extended to a all of _U_. Similarly, the lower order derivatives \\partial ^m \\textrm{Ric}\_{ij}, m = 0, 1, 2, \\cdots , k-2, can be continuously extended to the origin. \\square\
\
First note that _g_ is a C^{1,1}(U) weak solution of the elliptic Eq. ( [B.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ118)). Furthermore Q(g, \\partial g) \\in C^{0,1}(U) and by Claim 1 we have \\textrm{Ric}\_{ij} \\in C^{0,1}(U) as well. Since such weak solutions are unique, and there exists a C^{2,\\alpha }(U) solution that agrees on the boundary \\partial U, we see that _g_ is in fact C^{2,\\alpha }(U). Bootstrapping standard Schauder estimates and the result of Claim 1, we conclude that g\_{ij} is smooth with respect to the harmonic coordinates y^i, i = 1, 2, 3, 4.\
\
It remains to be shown that _g_( _t_) can be extended to a smooth Ricci flow on {\\mathbb {R}}^4 \\times (0,T\]. Recall that by Lemma [B.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar187), for all \\tau >0 the derivatives of the curvature tensor are bounded on U \\times \[\\tau , T\]. Moreover _g_( _T_) is bi-Lipschitz to the Euclidean metric \\delta \_{ij} on _U_ and by the previous paragraph the covariant derivatives of _g_( _T_) with respect to \\delta \_{ij} are all bounded. Therefore we may follow the proof of \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"),  Lemma 3.11\] with t\_0 = T to deduce that\
\
\\begin{aligned} \\frac{\\partial ^m}{\\partial t^m} \\frac{\\partial ^n}{\\partial y^{i\_1} \\cdots \\partial y^{i\_n}} \\left( g(t)\\right) \_{ij} \\le K\_{m,n} \\,\\quad \\text { on } \\, (U\\setminus \\{0\\})\\times \[\\tau ,T\], \\end{aligned}\
\
for some constants K\_{m,n}>0. This shows that _g_( _t_) can be smoothly extended to U\\times \[\\tau , T\]. As \\tau > 0 was arbitrary the desired result follows. \\square\
\
## Rights and permissions\
\
**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).\
\
[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Eguchi%E2%80%93Hanson%20Singularities%20in%20U%282%29-Invariant%20Ricci%20Flow&author=Alexander%20Appleton&contentID=10.1007%2Fs42543-022-00048-y&copyright=The%20Author%28s%29&publication=2096-6075&publicationDate=2022-11-16&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY)\
\
## About this article\
\
[![Check for updates. Verify currency and authenticity via CrossMark](<Base64-Image-Removed>)](https://crossmark.crossref.org/dialog/?doi=10.1007/s42543-022-00048-y)\
\
### Cite this article\
\
Appleton, A. Eguchi–Hanson Singularities in **_U_**(2)-Invariant Ricci Flow.\
_Peking Math J_ **6**, 1–141 (2023). https://doi.org/10.1007/s42543-022-00048-y\
\
[Download citation](https://citation-needed.springer.com/v2/references/10.1007/s42543-022-00048-y?format=refman&flavour=citation)\
\
- Received: 01 July 2020\
\
- Revised: 21 January 2022\
\
- Accepted: 08 February 2022\
\
- Published: 16 November 2022\
\
- Version of record: 16 November 2022\
\
- Issue date: March 2023\
\
- DOI: https://doi.org/10.1007/s42543-022-00048-y\
\
\
### Share this article\
\
Anyone you share the following link with will be able to read this content:\
\
Get shareable link\
\
Sorry, a shareable link is not currently available for this article.\
\
Copy shareable link to clipboard\
\
Provided by the Springer Nature SharedIt content-sharing initiative\
\
\
### Keywords\
\
- [Ricci Flow](https://link.springer.com/search?query=Ricci%20Flow&facet-discipline=%22Mathematics%22)\
- [Eguchi–Hanson metric](https://link.springer.com/search?query=Eguchi%E2%80%93Hanson%20metric&facet-discipline=%22Mathematics%22)\
- [Singularity model](https://link.springer.com/search?query=Singularity%20model&facet-discipline=%22Mathematics%22)\
- [Four dimensional](https://link.springer.com/search?query=Four%20dimensional&facet-discipline=%22Mathematics%22)\
- [Blow-up](https://link.springer.com/search?query=Blow-up&facet-discipline=%22Mathematics%22)\
\
### Mathematics Subject Classification\
\
- [53E20](https://link.springer.com/search?query=53E20&facet-discipline=%22Mathematics%22)