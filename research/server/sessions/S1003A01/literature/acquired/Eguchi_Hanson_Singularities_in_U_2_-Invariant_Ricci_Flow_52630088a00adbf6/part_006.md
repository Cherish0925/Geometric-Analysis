---
retention_scope: session
part: 6
total_parts: 7
---

[Part 6/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Then for every \\epsilon \\in (0,1) there exist constants C, \\delta > 0 such that at all points ( _p_, _t_) in spacetime with C b(o,t) \\le b(p,t) \\le \\delta  the following inequalities hold:\
\
1. (i)\
Q \\ge 1 - \\epsilon ;\
\
2. (ii)\
bb\_{ss} \\le \\epsilon ;\
\
3. (iii)\
T\_{F\_1} :=b b\_{ss} + 1- b\_s^2 \\ge -\\epsilon ;\
\
4. (iv)\
T\_{F\_2} :=b b\_{ss} + 1- b\_s^2 - \\left( 1-b\_s^2\\right) ^2 \\le \\epsilon ;\
\
5. (v)\
\\partial \_t b^2 \\le \\epsilon .\
\
\
### Remark 12.4\
\
Inequality (ii) is implied by (iv) for metrics in {\\mathcal {I}}. However, we need (ii) as an intermediate result before proving (iv).\
\
### Proof\
\
Fix \\epsilon \\in (0,1). Recall the following facts of the Eguchi–Hanson space (M\_2, g^E) derived in Sect. [4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec15):\
\
1. (a)\
x = y = 0 on M\_2.\
\
2. (b)\
Q \\rightarrow 1 as s \\rightarrow \\infty .\
\
3. (c)\
g^E is normalized such that its warping function b^E satisfies b^E(0)=1.\
\
\
Using (a) a computation shows that\
\
\\begin{aligned}&bb\_{ss} = 2\\big (1-Q^2\\big ), \\\&T\_{F\_1} = 3\\big (1 - Q^2\\big ), \\\&T\_{F\_2} = 3\\big (1 - Q^2\\big ) - \\big (1-Q^2\\big )^2, \\\&\\partial \_t b^2 = 0 \\end{aligned}\
\
on (M\_2, g^E). Pick C > 10 such that on (M\_2, g^E) we have Q > 1 - \\epsilon , bb\_{ss} < \\epsilon , T\_{F\_1} > -\\epsilon  and T\_{F\_2} < \\epsilon  whenever s > C. This is possible by Property (b).\
\
Take a path \\gamma : \[0,T\_\\textrm{sing}) \\rightarrow M\_2 such that\
\
\\begin{aligned} s(\\gamma (t), t) = C b(o,t), \\end{aligned}\
\
where we recall that _s_( _p_, _t_) is the distance of a point p \\in M\_2 from the non-principal orbit S^2\_o at the tip of M\_2. By Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) we know that at distance scales comparable to _b_( _o_, _t_) away from S^2\_o we converge to the Eguchi–Hanson space as t \\rightarrow T\_\\textrm{sing}. From the scale-invariance of _Q_, bb\_{ss}, T\_{F\_1}, T\_{F\_2} and \\partial \_t b^2 it follows that at spacetime points (\\gamma (t),t) Inequalities (i)–(v) eventually hold as t \\rightarrow T\_\\textrm{sing}.\
\
Let _A_ be the set of all sequences of points \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} in spacetime satisfying the following two properties:\
\
1. (1)\
b(p\_i, t\_i) \\ge C b(o, t\_i);\
\
2. (2)\
b(p\_i, t\_i) \\rightarrow 0 as i \\rightarrow \\infty .\
\
\
Note that Property (2) implies that for such sequences t\_i \\rightarrow T\_\\textrm{sing} as i \\rightarrow \\infty .\
\
We first prove Inequality (i), arguing by contradiction. Assume that\
\
\\begin{aligned} \\iota := \\inf \\left\\{ \\liminf \_{i \\rightarrow \\infty } Q(p\_i, t\_i) \\, \\big \| \\, \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A \\right\\} < 1 - \\epsilon . \\end{aligned}\
\
Then there exists a sequence \\{ A\_n \\}\_{n \\in {\\mathbb {N}}} of sequences A\_n = \\{(p\_{n,i}, t\_{n,i}) \\}\_{i \\in {\\mathbb {N}}} of points in spacetime satisfying Properties (1) and (2) above, and\
\
\\begin{aligned} \\lim \_{n \\rightarrow \\infty } \\liminf \_{i \\rightarrow \\infty } Q(p\_{n,i}, t\_{n,i}) = \\iota . \\end{aligned}\
\
For each n \\in {\\mathbb {N}} take N(n) \\in {\\mathbb {N}} such that for m \\ge N(n) we have\
\
\\begin{aligned} \\left\| \\liminf \_{i \\rightarrow \\infty } Q(p\_{m,i}, t\_{m,i}) - \\iota \\right\| \\le \\frac{1}{n}. \\end{aligned}\
\
For each n \\in {\\mathbb {N}} take I(n) \\in {\\mathbb {N}} such that\
\
\\begin{aligned} \\left\| Q(p\_{n,I(n)}, t\_{n,I(n)}) - \\liminf \_{i \\rightarrow \\infty } Q(p\_{n,i}, t\_{n,i})\\right\| \\le \\frac{1}{n} \\end{aligned}\
\
and\
\
\\begin{aligned} b(p\_{n,I(n)}, t\_{n, I(n)}) \\le \\frac{1}{n}. \\end{aligned}\
\
Let (p\_n, t\_n) = (p\_{N(n), I(N(n))}, t\_{N(n), I(N(n))}) for n \\in {\\mathbb {N}}. Then we see that\
\
\\begin{aligned} Q(p\_i, t\_i) \\rightarrow \\iota \\quad \\text { as }\\, i \\rightarrow \\infty \\end{aligned}\
\
and both Properties (1) and (2) from above hold.\
\
Before we carry on recall that by Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) there exists a C\_1>0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2} \\quad \\text { on } \\, M\_2 \\times \[0, T\_\\textrm{sing}). \\end{aligned}\
\
Recall also Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64), from which it follows that there exist constants \\kappa , \\rho >0 such that _g_( _t_) is \\kappa -non-collapsed at scale \\rho . Next, consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g\\big ( t\_i + b^2(p\_i, t\_i)t\\big ), \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
where \\Delta t\\!>\\!0 is chosen such that Proposition  [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) holds. Then (C\_{g\_i(0)}(p\_i, \\frac{1}{2})\\!, g\_i(t), p\_i) subsequentially converges to a pointed Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\Delta t, 0\]. By construction,\
\
\\begin{aligned} b(p\_\\infty , 0) = 1 \\end{aligned}\
\
and\
\
\\begin{aligned} Q(p\_\\infty , 0) = \\iota < 1 - \\epsilon . \\end{aligned}\
\
### Claim 1\
\
\\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i, t\_i)}{b(o, t\_i)} = \\infty .\
\
### Proof of Claim 1\
\
We argue by contradiction. Assume there exists a C'>0 such that after passing to a subsequence of (p\_i, t\_i)\
\
\\begin{aligned} \\frac{b(p\_i, t\_i)}{b(o, t\_i)} < C'. \\end{aligned}\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g\\big ( t\_i + b^2(p\_i, t\_i)t\\big ), \\quad t \\in \\big \[-b^{-2}(p\_i, t\_i) t\_i, 0\\big \]. \\end{aligned}\
\
By Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) we see that (M\_2, g\_i(t), p\_i) subsequentially converges to (M\_2, g\_{\\infty }(t), p\_\\infty ), where g\_\\infty (t) is stationary and homothetic to the Eguchi–Hanson metric. By construction,\
\
\\begin{aligned} 1 = b(p\_\\infty , 0) \\ge C b(o, 0) \\end{aligned}\
\
and\
\
\\begin{aligned} Q(p\_\\infty , 0) = \\iota < 1- \\epsilon . \\end{aligned}\
\
Furthermore,\
\
\\begin{aligned} s(p\_\\infty , 0) \\ge b(p\_\\infty , 0) \\ge C b(o, 0), \\end{aligned}\
\
where the first inequality follows from the fact that 1 \\ge Q \\ge b\_s \\ge 0 for metrics in {\\mathcal {I}} and the second inequality follows from the definition of _C_. Thus\
\
\\begin{aligned} Q(p\_\\infty , 0) > 1 - \\epsilon , \\end{aligned}\
\
which is a contradiction and hence proves the claim. \\square\
\
### Claim 2\
\
For every N \\!\\in \\! {\\mathbb {N}} eventually \\frac{b(p,t)}{b(o,t)} \\!> \\!N everywhere in (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), \\!g\_i(t),\\! p\_i) \\times \[-\\Delta t, 0\].\
\
### Proof of Claim 2\
\
Fix N \\in {\\mathbb {N}}. We argue by contradiction. After passing to a subsequence of (p\_i, t\_i), we may assume that there exists a sequence of spacetime points (p'\_i, t'\_i) \\in (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i) \\times \[-\\Delta t, 0\] for which \\frac{b(p'\_i,t'\_i)}{b(o, t'\_i)} \\le N. Consider the rescaled metrics\
\
\\begin{aligned} g'\_i(t) = \\frac{1}{b^2(p'\_i, t'\_i)} g\\big (t'\_i + b^2(p'\_i, t'\_i) t\\big ), \\quad t \\in \\big \[-b^{-2}(p'\_i, t'\_i) t'\_i, 0\\big \]. \\end{aligned}\
\
By Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115), (M\_2, g'\_i(t), p'\_i), t \\in \[-b^{-2}(p'\_i, t'\_i) t'\_i, 0\], converges to an ancient Ricci flow (M\_\\infty , g'\_\\infty (t), p'\_\\infty ), t \\in (-\\infty , 0\], which is stationary and homothetic to the Eguchi–Hanson space. Note that on the non-principal orbit S^2\_o\
\
\\begin{aligned} 0 \\ge \\partial \_t b^2(o,t) = 4by\_s \\ge - 4bQ\_s = -4k, \\end{aligned}\
\
as 0 \\ge y = b\_s - Q \\ge -Q and y=Q=0 at _o_ for metrics in {\\mathcal {I}}. Hence for \\tau \\in (0, \\frac{1}{4k}) the warping function b\_i of the metric g\_i(t) satisfies\
\
\\begin{aligned} b\_i(o,t) \\ge 1 - 4k \\tau > 0 \\quad \\text { for } \\, t \\in \\big \[-b^{-2}(p'\_i, t'\_i) t'\_i, \\tau \\big \]. \\end{aligned}\
\
We deduce by Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) that g\_i(t) has bounded curvature on M\_2 \\times \[-b^{-2}(p'\_i, t'\_i) t'\_i, \\tau \]. Hence (M\_2, g'\_i(t), p'\_i), t \\in \[-b^{-2}(p'\_i, t'\_i) t'\_i, \\tau \], also converges to the stationary Eguchi–Hanson space. In fact, inductively we can then show that for any \\tau > 0 we converge to the Eguchi–Hanson space. As (p'\_i, t'\_i) converges to a point (p'\_\\infty , t'\_\\infty ) in {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\], this implies that {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\] is a subset of a spacetime corresponding to the Eguchi–Hanson space, and therefore \\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} < \\infty . This, however, contradicts Claim 1. \\square\
\
### Claim 3\
\
Q(p\_\\infty , 0) = \\inf \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} Q.\
\
### Proof of Claim 3\
\
We argue by contradiction. If Q(p',t') < \\iota  at a point (p', t') \\in {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\], one could pick a sequence of points (p'\_i, t'\_i) \\in C\_{g\_i(0)}\\big (p\_i, \\frac{1}{2}\\big ) \\times \[-\\Delta t, 0\] with (p'\_i, t'\_i) \\rightarrow (p',t') as i \\rightarrow \\infty . Then shifting back to the time of the Ricci flow (M\_2, g(t)) via T'\_i = t\_i + t'\_ib^2(p\_i,t\_i) we see that the sequence (p'\_i, T'\_i) \\in M\_2 \\times \[0, T\_\\textrm{sing}) satisfies Properties (1) and (2). The former property holds because of Claim 2. This, however, would contradict the definition of \\iota . \\square\
\
By Property (1) of the sequence (p\_i, t\_i) we see that p\_\\infty  does not lie on a non-principal orbit of {\\mathcal {C}}\_\\infty  and therefore Q(p\_\\infty , 0) = a(p\_\\infty , 0) > 0. However, the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ shows that the only attainable minima are 0 and 1, yielding a contradiction. This concludes the proof of (i).\
\
We prove (ii)–(v) by the same strategy. Below we first prove Inequality (ii) by contradiction. Assume that\
\
\\begin{aligned} \\iota := \\sup \\left\\{ \\limsup \_{i \\rightarrow \\infty } bb\_{ss}\\big \|\_{(p\_i, t\_i)} \\, \\Big \| \\, \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A \\right\\} > \\epsilon . \\end{aligned}\
\
As before we can construct a sequence points (p\_i, t\_i) in spacetime satisfying Properties (1) and (2), and such that\
\
\\begin{aligned} \\lim \_{i \\rightarrow \\infty } bb\_{ss}\\big \|\_{(p\_i, t\_i)} = \\iota . \\end{aligned}\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g\\big ( t\_i + b^2(p\_i, t\_i)t\\big ), \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
where \\Delta t \\!> \\!0 is chosen such that Proposition  [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) holds. Then (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t),\\! p\_i) subsequentially converges to a pointed Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). By construction\
\
\\begin{aligned} bb\_{ss}\\big \|\_{(p\_\\infty , 0)} = \\iota > \\epsilon . \\end{aligned}\
\
Furthermore, by the same arguments as in Claims 1–3, we have\
\
\\begin{aligned} bb\_{ss}\\big \|\_{(p\_\\infty , 0)} = \\sup \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} bb\_{ss}, \\end{aligned}\
\
and hence\
\
\\begin{aligned} \\partial \_t bb\_{ss} \\big \|\_{(p\_\\infty , 0)} \\ge 0. \\end{aligned}\
\
By Statement (i) of this lemma we know that Q = 1 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. For Q=1 the evolution equation for bb\_{ss} is\
\
\\begin{aligned} \\partial \_t (bb\_{ss}) = (bb\_{ss})\_{ss} - \\frac{b\_s}{b} (bb\_{ss})\_s -4 \\frac{b\_s^2}{b^2} \\big ( 1- b\_s^2\\big ) -2 \\frac{b\_{ss}}{b} \\big (b b\_{ss}+2 b\_s^2\\big ). \\end{aligned}\
\
The derivation is carried out in Appendix A, in the subsection on the evolution equations when Q=1. From this we see that at the point (p\_\\infty ,0) in spacetime we have\
\
\\begin{aligned} \\partial \_t (bb\_{ss}) \\big \|\_{(p\_\\infty ,0)} < 0, \\end{aligned}\
\
which is a contradiction. This proves (ii).\
\
We prove Inequality (iii) similarly. Assume that\
\
\\begin{aligned} \\iota := \\inf \\left\\{ \\liminf \_{i \\rightarrow \\infty } T\_{F\_1}(p\_i, t\_i) \\, \\big \| \\, \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A \\right\\} < - \\epsilon . \\end{aligned}\
\
Pick \\{(p\_i,t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A such that\
\
\\begin{aligned} \\lim \_{i \\rightarrow \\infty } T\_{F\_1}(p\_i, t\_i) = \\iota . \\end{aligned}\
\
As before, (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t),p\_i) subsequentially converges to a pointed Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). By construction\
\
\\begin{aligned} T\_{F\_1} (p\_\\infty , 0) = \\inf \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} T\_{F\_1} = \\iota < - \\epsilon , \\end{aligned}\
\
and hence\
\
\\begin{aligned} \\partial \_t T\_{F\_1} \\big \|\_{(p\_\\infty , 0)} \\le 0. \\end{aligned}\
\
By Inequality (i) of this lemma Q = 1 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. For Q=1 the evolution equation of T\_{F\_1} can be written as\
\
\\begin{aligned} \\partial \_t T\_{F\_1} = (T\_{F\_1})\_{ss} - \\frac{b\_s}{b} (T\_{F\_1})\_s - 8\\frac{b^2\_s}{b^2} T\_{F\_1}. \\end{aligned}\
\
The derivation is carried out in Appendix A. From this we see that at the point (p\_\\infty ,0) in spacetime we have\
\
\\begin{aligned} \\partial \_t T\_{F\_1} \\big \|\_{(p\_\\infty ,0)} \\ge 0, \\end{aligned}\
\
with equality if and only if b\_s \\big \|\_{(p\_\\infty ,0)} = 0. Therefore we conclude that b\_s = 0 at (p\_\\infty , 0). Applying the strong maximum principle to the evolution equation ( [A.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ112)) of b\_s when Q=1, it then follows that b\_s = 0, and hence b\_{ss}=0, everywhere in {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. This, however, implies T\_{F\_1} = 1 at (p\_\\infty , 0), which is a contradiction and thus proves (ii).\
\
We proceed to prove (iv) in the same fashion. Assume that\
\
\\begin{aligned} \\iota := \\sup \\left\\{ \\limsup \_{i \\rightarrow \\infty } T\_{F\_2}(p\_i, t\_i) \\, \\big \| \\, \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A \\right\\} > \\epsilon . \\end{aligned}\
\
Pick \\{(p\_i,t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A such that\
\
\\begin{aligned} \\lim \_{i \\rightarrow \\infty } T\_{F\_2}(p\_i, t\_i) = \\iota . \\end{aligned}\
\
As before, (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i) subsequentially converges to a pointed Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). By construction,\
\
\\begin{aligned} T\_{F\_2}(p\_\\infty , 0) = \\sup \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} T\_{F\_2} = \\iota > \\epsilon . \\end{aligned}\
\
Therefore\
\
\\begin{aligned} \\partial \_t T\_{F\_2} \\big \|\_{(p\_\\infty , 0)} \\ge 0. \\end{aligned}\
\
By Statements (i) and (ii) of this lemma we have Q=1 and bb\_{ss} \\le 0 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. When Q=1 the evolution equation of T\_{F\_2} can be written as\
\
\\begin{aligned} \\partial \_t T\_{F\_2} = (T\_{F\_2})\_{ss} - \\frac{b\_s}{b} (T\_{F\_2})\_s + \\frac{1}{b^2} C\_{F\_2}, \\end{aligned}\
\
where C\_{F\_2} is a polynomial expression in bb\_{ss} and 1 - b\_s^2. The derivation is carried out in Appendix A. By Lemma [A.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar171) in Appendix A, C\_{F\_2} < 0 whenever T\_{F\_2} > 0 and bb\_{ss} \\le 0. This, however, implies\
\
\\begin{aligned} \\partial \_t T\_{F\_2}\\big \|\_{(p\_\\infty , 0)} < 0, \\end{aligned}\
\
which is a contradiction and thus proves (iv).\
\
Finally we prove (v), also by contradiction. Assume that\
\
\\begin{aligned} \\iota := \\sup \\left\\{ \\limsup \_{i \\rightarrow \\infty } \\partial \_t b^2 (p\_i, t\_i) \\, \\big \| \\, \\{(p\_i, t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A \\right\\} > \\epsilon . \\end{aligned}\
\
Pick \\{(p\_i,t\_i)\\}\_{i \\in {\\mathbb {N}}} \\in A such that\
\
\\begin{aligned} \\lim \_{i \\rightarrow \\infty } \\partial \_t b^2 (p\_i, t\_i) = \\iota . \\end{aligned}\
\
As before, (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i) subsequentially converges to a pointed Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). By construction,\
\
\\begin{aligned} \\partial \_t b^2\\big \|\_{(p\_\\infty , 0)} = \\iota > \\epsilon , \\end{aligned}\
\
as \\partial \_t b^2 is a scale-invariant quantity. By (i) we have Q = 1 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\] and the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ simplifies to\
\
\\begin{aligned} \\partial \_t b^2 = 2bb\_{ss} + 4 \\big ( b\_s^2 -1\\big ). \\end{aligned}\
\
By Inequality (iii) of this lemma we have\
\
\\begin{aligned} bb\_{ss} \\le b\_s^2 -1 +\\big (1 - b\_s^2\\big ) \\le 0 \\quad \\text {~on }\\,{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\], \\end{aligned}\
\
as b\_s \\in \[0,1\] for metrics in {\\mathcal {I}}. This, however, implies that\
\
\\begin{aligned} \\partial \_t b^2 \\le 0, \\end{aligned}\
\
which is a contradiction and thus proves (v). \\square\
\
### Lemma 12.5\
\
Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Then for every \\epsilon \\in (0,1) there exists a \\delta > 0 such that at all points ( _p_, _t_) in spacetime at which b(p,t) \\le \\delta  we have\
\
\\begin{aligned} \\partial \_t b^2 \\le \\epsilon . \\end{aligned}\
\
### Proof\
\
Fix \\epsilon > 0. By Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) we only need to prove that there exists a \\delta > 0 such that the result holds when b(p,t)\\le C b(o,t) \\le \\delta , where C>0 is as in Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146). Note that\
\
\\begin{aligned} \\partial \_t b^2 = 0 \\end{aligned}\
\
on the Eguchi–Hanson space background. By Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) we know that on the scale b(p,t) \\le C b(o,t) we converge to the Eguchi–Hanson space as t \\rightarrow T\_\\textrm{sing}. As b(o,t) \\rightarrow 0 as t \\rightarrow T\_\\textrm{sing} we see that there exists a \\delta >0 such that\
\
\\begin{aligned} \\partial \_t b^2 \\le \\epsilon \\end{aligned}\
\
at all points ( _p_, _t_) in spacetime at which b(p,t) \\le C b(o,t) \\le \\delta . This completes the proof. \\square\
\
Below we prove the simplest case of Theorem [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar144).\
\
### Lemma 12.6\
\
Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Let (p\_i,t\_i) be a sequence of points in spacetime satisfying\
\
1. (1)\
b(p\_i, t\_i) \\rightarrow 0;\
\
2. (2)\
b\_s(p\_i,t\_i) \\rightarrow 0;\
\
3. (3)\
b(p\_i,t\_i) > 2 b(o, t\_i).\
\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i,t\_i) t\\big ), \\quad t \\in \\big \[-b^{-2}(p\_i, t\_i)t\_i, 0\\big \]. \\end{aligned}\
\
Then (M\_2, g\_i(t), p\_i) , t \\in \[-b^{-2}(p\_i, t\_i)t\_i, 0\], subsequentially converges, in the Cheeger–Gromov sense, to the shrinking cylinder {\\mathbb {R}}\\times {\\mathbb {R}}P^3.\
\
### Proof\
\
Fix T>0. By Lemma [12.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar155), the curvature bound of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) and the fact that b\_s \\in \[0,1\] for metrics in {\\mathcal {I}}, we see that the curvatures of g\_i(t) on the parabolic neighborhoods C\_{g\_i(0)}(p\_i, \\frac{1}{2}) \\times \[-T, 0\] are eventually uniformly bounded. By Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) the Ricci flows g\_i(t) are \\kappa -non-collapsed. Hence (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i), t \\in \[-T,0\], subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-T,0\], where by construction b\_s = 0 at the point (p\_\\infty , 0) in spacetime. Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) implies Q = 1 on {\\mathcal {C}}\_\\infty \\times \[-T, 0\]. Applying the strong maximum principle to the evolution equation ( [A.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ112)) of b\_s when Q=1 shows that\
\
\\begin{aligned} b\_s = 0 \\, \\quad \\text { on } \\, {\\mathcal {C}}\_{\\infty } \\times \[-T, 0\]. \\end{aligned}\
\
That is, the metric g\_\\infty (t) is cylindrical. From here one can inductively show that for every r > 0 the Ricci flows (C\_{g\_i(0)}(p\_i, r), g\_i(t), p\_i), t \\in \[-T,0\] subsequentially converge to a limiting cylindrical Ricci flow. Hence (M\_2, g\_i(t), p\_i), t \\in \[-T, 0\], subsequentially converges to the shrinking cylinder ({\\mathbb {R}}\\times {\\mathbb {R}}P^3, g\_\\infty (t), p\_\\infty ), t \\in \[-T,0\]. As T>0 is arbitrary the desired result follows by a diagonal argument. \\square\
\
Before we carry on constructing the blow-up limit (iii) of Theorem [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar144), we need to state two technical lemmas. Their proofs can be skipped on the first reading.\
\
### Lemma 12.7\
\
Let {\\hat{\\eta }} > 0. There exists a K= K({\\hat{\\eta }})>1 such that the following holds: Let s\_0 > 0 and b: \[s\_0, \\infty ) \\rightarrow {\\mathbb {R}} satisfy the ordinary differential inequalities\
\
\\begin{aligned} b b\_{ss} \\le b\_s^2 -1 + \\big ( 1- b\_s^2\\big )^2 \\end{aligned}\
\
(12.2)\
\
\
and\
\
\\begin{aligned} b\_s > 0. \\end{aligned}\
\
If at s\_0 we have\
\
\\begin{aligned} \\frac{1- b\_s^2}{b^2}\\Big \|\_{s\_0} = K \\end{aligned}\
\
(12.3)\
\
\
and\
\
\\begin{aligned} b\_s\\big \|\_{s\_0} \\in \[{\\hat{\\eta }}, 1), \\end{aligned}\
\
(12.4)\
\
\
then b\_s < {\\hat{\\eta }} when b \\ge 1.\
\
### Proof\
\
First note that b(s\_0) \\le \\frac{1}{\\sqrt{K}} < 1  by ( [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ105)) and ( [12.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ106)). Furthermore, as b\_s \\in \[{\\hat{\\eta }}, 1) at s\_0 we see from ( [12.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ104)) that b\_s < 1 on \[s\_0, \\infty ).\
\
Write B = b\_s. Then the ODI becomes\
\
\\begin{aligned} b B\_s \\le B^2 -1 + \\big ( 1- B^2\\big )^2 = - B^2\\big ( 1- B^2\\big ). \\end{aligned}\
\
Since b\_s > 0 we may treat _b_ as the independent variable, yielding the following ODI\
\
\\begin{aligned} \\frac{{{d}}B}{{{d}}b}\\le - \\frac{B^2 \\left( 1- B^2\\right) }{bB}. \\end{aligned}\
\
Note that as B=b\_s\\in (0,1) we may rearrange the inequality and integrate to obtain\
\
\\begin{aligned} \\int \_{B\_0}^B \\frac{B {{d}}B}{B^2\\left( 1 - B^2\\right) } \\le -\\int \_{b\_0}^b \\frac{{{d}}b}{b}, \\end{aligned}\
\
where we denote by b\_0 and B\_0 the values of _b_ and _B_ at s\_0, respectively. Evaluating the integrals and rearranging we deduce\
\
\\begin{aligned} \\frac{B^2}{1 - B^2} \\le \\frac{B\_0^2 b\_0^2}{(1-B\_0^2) b^2}. \\end{aligned}\
\
By the initial conditions ( [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ105)) and ( [12.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ106)) we have\
\
\\begin{aligned} \\frac{b\_0^2 B\_0^2}{1 - B\_0^2} = \\frac{B\_0^2}{K} = \\frac{B\_0^4}{K B\_0^2}\\le \\frac{1}{K {\\hat{\\eta }}^2} \\end{aligned}\
\
and therefore\
\
\\begin{aligned} \\frac{B^2}{1 - B^2} \\le \\frac{1}{K{\\hat{\\eta }}^2b^2}. \\end{aligned}\
\
Hence when b \\ge 1 we have\
\
\\begin{aligned} \\frac{B^2}{1 - B^2} \\le \\frac{1}{K {\\hat{\\eta }}^2}, \\end{aligned}\
\
which can be rearranged to\
\
\\begin{aligned} B^2 \\le \\frac{1}{K {\\hat{\\eta }}^2 + 1}. \\end{aligned}\
\
Choosing _K_ sufficiently large the desired result follows. \\square\
\
Now we may construct the orbifold Ricci flow blow-up:\
\
### Lemma 12.8\
\
Let \\eta \\in (0,1) and (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Assume that (p\_i,t\_i) is a sequence of points in spacetime satisfying\
\
1. (1)\
b(p\_i, t\_i) \\rightarrow 0 as i \\rightarrow \\infty ;\
\
2. (2)\
\\frac{b(p\_i,t\_i)}{b(o,t\_i)} \\rightarrow \\infty  as i \\rightarrow \\infty ;\
\
3. (3)\
b\_s(p\_i,t\_i) \\rightarrow \\eta  as i \\rightarrow \\infty .\
\
\
Consider the rescaled Ricci flows\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i,t\_i) t\\big ), \\quad t\\in \\big \[-b^{-2}(p\_i, t\_i) t\_i, 0\\big \]. \\end{aligned}\
\
Then (M\_2, g\_i(t), p\_i), t\\in \[-b^{-2}(p\_i, t\_i) t\_i, 0\], subsequentially converges, in the Cheeger–Gromov sense, to an ancient Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in (-\\infty ,0\], where M\_\\infty \\cong ({\\mathbb {R}}^4\\setminus \\{0\\})/{\\mathbb {Z}}\_2. Moreover, g\_\\infty (t) can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4 /{\\mathbb {Z}}\_2 that is homothetic to the 4d Bryant soliton quotiented by {\\mathbb {Z}}\_2.\
\
### Proof\
\
Fix T > 0. By Lemma [12.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar155) we have that for every \\epsilon > 0 there exists a \\delta > 0 such that at points ( _p_, _t_) in spacetime at which b(p,t) < \\delta  we have \\partial \_t b^2 \\le \\epsilon . This shows that for every N > 0 there exists a \\delta '= \\delta '(N) > 0 such that whenever b(p,t) < \\delta ' then\
\
\\begin{aligned} b(p,t') > \\frac{b(p,t)}{2} \\quad \\text { for } \\, t' \\in \\big \[t- N b^2(p,t), t\\big \]. \\end{aligned}\
\
(12.5)\
\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i,t\_i) t\\big ). \\end{aligned}\
\
For n \\in {\\mathbb {N}}\_{\\ge 2} and (p,t) \\in M\_2 \\times \[0, T\_\\textrm{sing}) define the open set\
\
\\begin{aligned} E\_{p,t,n} := \\left\\{ p' \\in M\_2 \\, \\Big \| \\, b(p',t) > \\frac{b(p,t)}{n} \\right\\} \\subseteq M\_2. \\end{aligned}\
\
Furthermore, define the parabolic neighborhoods\
\
\\begin{aligned} \\Omega \_{i,n} = E\_{p\_i,t\_i,n} \\times \[-T-1 , 0\]. \\end{aligned}\
\
Recall that by Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) there exists a C\_1 > 0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2} \\quad \\text { on } \\, M\_2 \\times \[0, T\_\\textrm{sing}). \\end{aligned}\
\
Hence for fixed _n_ and sufficiently large _i_ the curvatures of g\_i(t) on \\Omega \_{i,n} are uniformly bounded:\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le 4n^2C\_1 \\, \\quad \\text { on }\\Omega \_{i,n}. \\end{aligned}\
\
This follows from ( [12.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ107)), b(p\_i, t\_i) \\rightarrow 0 and the fact that b\_s \\ge 0 for metrics in {\\mathcal {I}}. By Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) the Ricci flows g\_i(t) are \\kappa -non-collapsed at larger and larger scales. By a slight adaptation of the local compactness Theorem [8.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar82) we see that for each n \\in {\\mathbb {N}} the Ricci flows (E\_{p\_i, t\_i, n}, g\_i(t), p\_i), t \\in \[-T-1,0\], subsequentially converge to a Ricci flow ({\\mathcal {E}}\_{\\infty , n}, g\_{\\infty ,n}(t), p\_{\\infty ,n}), t \\in \[-T-1, 0\]. The manifolds {\\mathcal {E}}\_{\\infty , n} are diffeomorphic to ({\\mathbb {R}}^4\\setminus \\{0\\})/{\\mathbb {Z}}\_2 and therefore incomplete. By a diagonal argument we may assume that {\\mathcal {E}}\_{\\infty , n} \\subset {\\mathcal {E}}\_{\\infty , n+1} and g\_{\\infty ,n}(t) = g\_{\\infty ,n+1}(t) on {\\mathcal {E}}\_{\\infty , n}. This allows us to drop the dependence on _n_ and write g\_\\infty (t) and p\_\\infty  for brevity. By Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) we have Q = 1, bb\_{ss} \\le 0, T\_{F\_1} \\le 0, T\_{F\_2} \\ge 0 and \\partial \_t b^2 \\le 0 on {\\mathcal {E}}\_{\\infty , n}.\
\
### Claim 1\
\
There exists an {\\hat{\\eta }} > 0, independent of _n_, such that on the word line (p\_{\\infty }, t), t \\in \[-T, 0\], in {\\mathcal {E}}\_{\\infty , n} \\times \[-T, 0\] we have b\_s > {\\hat{\\eta }} uniformly.\
\
### Proof of Claim 1\
\
We argue by contradiction. Assume that t' \\in \[-T,0\] is such that for t \\in \[t', 0\] we have b\_s(p\_\\infty , t) \\ge 0 with equality if, and only if, t = t'. Applying the strong maximum principle to the evolution equation ( [A.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ112)) of b\_s when Q=1, we obtain that b\_s = 0 on {\\mathcal {E}}\_{\\infty , n} \\times \[-T-1, t'\]. That is, the metric g\_\\infty (t) is cylindrical for times t \\in \[-T-1, t'\]. We now show that this leads to a contradiction. Take times t'\_i = t\_i - t' b^2(p\_i,t\_i). Then the spacetime points (p\_i,t'\_i) \\in M\_2 \\times \[0, T\_\\textrm{sing}) converge to the spacetime point (p\_\\infty , t') \\in {\\mathcal {E}}\_{\\infty , n} \\times \[-T-1, t'\]. Consider the rescaled metrics\
\
\\begin{aligned} g'\_i(t) = \\frac{1}{b^2(p\_i,t'\_i)} g\\big (t'\_i + b^2(p\_i, t'\_i)t \\big ), \\quad t\\in \\big \[-b^{-2}(p\_i, t'\_i)t'\_i, 0\\big \]. \\end{aligned}\
\
Because b\_s(p\_i, t'\_i) \\rightarrow 0 as i \\rightarrow \\infty , Lemma [12.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar157) implies that after passing to a subsequence (M\_2, g'\_i(t), p\_i) converges to the shrinking cylinder {\\mathbb {R}}\\times {\\mathbb {R}}P^3. For every n\\in {\\mathbb {N}} take N\_n \\in {\\mathbb {N}} such that for i \\ge N\_n the region C\_{g'\_i(0)}(p\_i, n) \\subset M\_2 is close, in the Cheeger–Gromov sense, to a cylinder {\\mathbb {R}}\\times {\\mathbb {R}}P^3 of length 2 _n_ and radius 1. By Perelman’s pseudolocality theorem there exists a K > 0 and \\tau > 0 such that g'\_i(t) has bounded curvature on C\_{g'\_i(0)}(p\_i, n-1) \\times \[0, \\tau \]. Hence (M\_2, g'\_i(t), p\_i), t \\in \[-t'\_i b(p\_i, t'\_i)^{-2}, \\tau \], subsequentially converges to a limiting Ricci flow (M\_\\infty , g'\_\\infty (t),p\_\\infty ),  t \\in (-\\infty , \\tau \], where M\_\\infty \\cong {\\mathbb {R}}\\times {\\mathbb {R}}P^3 and g'\_\\infty (0) is cylindrical. By the uniqueness of Ricci flow solutions \[ [11](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR11 "Chen, B.L., Zhu, X.P.: Uniqueness of the Ricci flow on complete noncompact manifolds. J. Differ. Geom. 74(1), 119–154 (2006)")\], we see that g'\_\\infty (t) remains cylindrical for t \\in \[0, \\tau \] and therefore b\_s= 0 on M\_\\infty \\times (-\\infty , \\tau ). Now we have arrived at a contradiction, as this implies that t' is not the earliest time at which b\_s = 0 on the wordline through the point (p\_\\infty , 0) in the spacetime {\\mathcal {E}}\_{\\infty , n} \\times \[-T-1, 0\]. This proves the claim. \\square\
\
As T\_{F\_1} \\ge 0 we have\
\
\\begin{aligned} -\\frac{b\_{ss}}{b} \\le \\frac{1-b\_s^2}{b^2} \\, \\quad \\text { on } \\, {\\mathcal {E}}\_{\\infty , n} \\times \[-T, 0\], \\end{aligned}\
\
and hence\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_{\\infty }(t)}\|\_{g\_{\\infty }(t)} \\le c \\frac{1-b\_s^2}{b^2} \\end{aligned}\
\
(12.6)\
\
\
for some universal constant c >0, as \\frac{1-b\_s^2}{b^2} and -\\frac{b\_{ss}}{b} are the only non-zero curvature components of a rotationally symmetric metric.\
\
### Claim 2\
\
There exists a K= K({\\hat{\\eta }}) > 1, independent of _n_, such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_{\\infty }(t)}\|\_{g\_{\\infty }(t)} < cK \\end{aligned}\
\
uniformly on {\\mathcal {E}}\_{\\infty , n} \\times \[-T,0\].\
\
### Proof of Claim\
\
Fix n \\ge 2. As bb\_{ss} \\le 0 and b\_s \\ge 0 it follows from Claim 1 that b\_s \\ge {\\hat{\\eta }}>0 in the region\
\
\\begin{aligned} R = \\left\\{ (p,t) \\in {\\mathcal {E}}\_{\\infty , n} \\times \[-T,0\] \\, \\Big \| \\, b(p,t) \\le b(p\_\\infty , t) \\right\\} . \\end{aligned}\
\
As \\partial \_t b^2 \\le 0 we have b(p\_\\infty , t) \\ge b(p\_\\infty , 0) = 1 for t \\in \[-T, 0\].\
\
Now choose a K = K({\\hat{\\eta }}) > 1 such that Lemma [12.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar159) holds true. If at some point (p',t') \\in {\\mathcal {E}}\_{\\infty , n} \\times \[-T,0\] we had\
\
\\begin{aligned} \\frac{1- b\_s^2}{b^2} \\ge K \\end{aligned}\
\
then on the time slice \\{t= t'\\} \\subset {\\mathcal {E}}\_{\\infty ,n} the result of Lemma [12.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar159) would imply that b\_s < {\\hat{\\eta }} when b \\ge 1. This cannot be true, as by Lemma [12.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar155) we have that \\partial \_t b^2 \\le 0 on {\\mathcal {E}}\_{\\infty ,n} \\times \[-T, 0\] and therefore b(p\_\\infty , t) \\ge 1 for t \\in \[-T,0\]. Hence we deduce by ( [12.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ108)) that the curvature is bounded by _cK_ on the region _R_. As on {\\mathcal {E}}\_{\\infty , n} \\times \[-T,0\] \\setminus R we have b > 1, it follows by ( [12.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ108)) and the fact that b\_s \\in \[0,1\] for metrics in {\\mathcal {I}} that the curvature is uniformly bounded by _c_ there. \\square\
\
Claim 2 shows that as n \\rightarrow \\infty  we may extract a limiting Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-T, 0\], with curvature bounded by _cK_. By construction M\_\\infty  is diffeomorphic to (R^4\\setminus \\{0\\})/ {\\mathbb {Z}}\_2. Define the radial coordinate \\xi : M\_{\\infty } \\rightarrow {\\mathbb {R}} by\
\
\\begin{aligned} \\xi (p) = d\_{g\_\\infty (0)}(p, \\Sigma \_{p\_\\infty }) + \\xi \_0, \\end{aligned}\
\
where \\xi \_0 \\in {\\mathbb {R}} is chosen such that \\xi \\rightarrow 0 as b \\rightarrow 0.\
\
Note that by the Ricci flow equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) for _b_ we have\
\
\\begin{aligned} \|\\partial \_t b^2\| \\le 3 b^2 \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le 3 b^2 K \\,\\quad \\text { on } \\, M\_\\infty \\times \[-T,0\]. \\end{aligned}\
\
Working in (\\xi , t) coordinates we see that\
\
\\begin{aligned} b^2(\\xi , t) \\le b^2(\\xi , 0) e^{3 K T}, \\quad t \\in \[-T,0\]. \\end{aligned}\
\
Hence for all t \\in \[-T,0\] we have b(\\xi , t) \\rightarrow 0 as \\xi \\rightarrow 0. As M\_\\infty  has bounded curvature, we see that \\frac{1-b\_s^2}{b^2} is bounded as well and hence b\_s(\\xi , t) \\rightarrow 1 as \\xi \\rightarrow 0. From Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175) in Appendix B it then follows that g\_\\infty (t), t \\in (-T,0\], can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4\\times {\\mathbb {Z}}\_2. Since _T_ was arbitrary, a diagonal argument produces an ancient orbifold Ricci flow ((R^4\\setminus \\{0\\})/ {\\mathbb {Z}}\_2, g\_\\infty (t), p\_\\infty ), t \\in (-\\infty , 0\]. Note that a priori g\_\\infty (t) might have unbounded curvature as t \\rightarrow -\\infty .\
\
As Q = 1, b\_s \\in \[0,1\] and b\_{ss} \\le 0 we see that g\_\\infty (t) is rotationally symmetric and has positive sectional curvature. Furthermore, for each t \\in (-\\infty , 0\] the metric g\_\\infty (t) is asymptotically cylindrical, as the following argument shows: Either _b_ is bounded, in which case bb\_{ss} \\le 0 and b\_s \\ge 0 show that \\lim \_{s\\rightarrow \\infty } b\_s = 0, or _b_ is unbounded, in which case the inequality T\_{F\_2} \\le 0 and the proof of Lemma [12.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar159) show that on each time slice b\_s \\rightarrow 0 as b \\rightarrow \\infty .\
\
By the Hamilton’s trace Harnack inequality (see for instance \[ [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR10 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)"),  Theorem D.26\]) and the fact that for any T > 0 the metric g\_\\infty (t) has bounded curvature on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 \\times \[-T,0\], it follows that\
\
\\begin{aligned} \\partial \_t R\_{g\_\\infty (t)} \\ge 0 \\,\\quad \\text { on } \\, {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 \\times (-\\infty ,0\]. \\end{aligned}\
\
Therefore g\_\\infty (t) has bounded curvature on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 \\times (\\infty , 0\]. By the result of Li and Zhang \[ [27](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR27 "Li, X.L., Zhang, Y.J.: Ancient solutions to the Ricci flow in higher dimensions,                    arXiv:1812.04156                                     (2018)")\] we conclude that g\_\\infty (t) is homothetic to the four dimensional Bryant soliton quotiented by {\\mathbb {Z}}\_2. \\square\
\
### Lemma 12.9\
\
Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Let (p\_i,t\_i) be a sequence of points in spacetime satisfying\
\
1. (1)\
b(p\_i,t\_i) \\rightarrow 0;\
\
2. (2)\
b\_s(p\_i,t\_i) \\rightarrow 1.\
\
\
Consider the sequence of rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i,t\_i) t\\big ), \\quad t \\in \\big \[-b^{-2}(p\_i,t\_i) t\_i, 0\\big \]. \\end{aligned}\
\
Then (M\_2, g\_i(t), p\_i), t \\in \[-b^{-2}(p\_i,t\_i) t\_i, 0\], subsequentially converges, in the Cheeger–Gromov sense, to an ancient Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t\\in (-\\infty , 0\], where M\_\\infty \\cong ({\\mathbb {R}}^4 \\setminus \\{0\\}) /{\\mathbb {Z}}\_2 and g\_\\infty (t) can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 that is stationary and isometric to the flat orbifold {\\mathbb {R}}^4/{\\mathbb {Z}}\_2.\
\
### Proof\
\
First note that\
\
### Claim 1\
\
\\begin{aligned} \\frac{b(p\_i, t\_i)}{b(o,t\_i)} \\rightarrow \\infty \\, \\quad \\text { as } \\, i \\rightarrow \\infty . \\end{aligned}\
\
### Proof of Claim 1\
\
We argue by contradiction. Assume there exists a C>0 such that after passing to a subsequence of (p\_i, t\_i) we have\
\
\\begin{aligned} \\frac{b(p\_i, t\_i)}{b(o,t\_i)} \\le C. \\end{aligned}\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g \\big (t\_i + b^2(p\_i, t\_i) t\\big ), \\quad t \\in \\big \[- b^{-2}(p\_i, t\_i)t\_i, 0\\big \]. \\end{aligned}\
\
Then by Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) the sequence (M\_2, g\_i(t), p\_i) subsequentially converges to a blow-up limit (M\_2, g\_\\infty (t), p\_\\infty ), which is homothetic to the Eguchi–Hanson space. By construction,\
\
\\begin{aligned} b(p\_\\infty , 0) = 1 \\end{aligned}\
\
and\
\
\\begin{aligned} b\_s(p\_\\infty , 0) = 1. \\end{aligned}\
\
The latter follows from the assumption that b\_s(p\_i,t\_i) \\rightarrow 1 as i \\rightarrow \\infty . However, by Lemma [4.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar29) we have b\_s < 1 everywhere on the Eguchi–Hanson space. This is a contradiction and the claim follows.\
\
Fix T>0 and consider the rescaled metrics g\_i(t) on the parabolic sets E\_{(p\_i,t\_i,n)} \\times \[-T, 0\] as in the proof of Lemma [12.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar161). By the same reasoning, we see that for all n \\in {\\mathbb {N}}\_{\\ge 2} the flows (E\_{p\_i,t\_i,n}, g\_i(t), p\_i) subsequentially converges to a Ricci flow ({\\mathcal {E}}\_{\\infty , n}, g\_{\\infty , n}(t), p\_{\\infty , n}), t \\in \[-T,0\]. As in the proof of Lemma [12.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar161), we may assume that {\\mathcal {E}}\_{\\infty , n} \\subset {\\mathcal {E}}\_{\\infty , n+1} and g\_{\\infty , n} = g\_{\\infty , n+1} on {\\mathcal {E}}\_{\\infty , n}. Therefore we drop the dependence on _n_ and write p\_\\infty  and g\_{\\infty }(t). By construction we have\
\
\\begin{aligned} b(p\_\\infty , 0) = 1 \\end{aligned}\
\
and\
\
\\begin{aligned} b\_s(p\_\\infty , 0) = 1, \\end{aligned}\
\
where the latter follows from the assumption that b\_s(p\_i, t\_i) \\rightarrow 1 as i \\rightarrow \\infty . Furthermore, by Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) and Claim 1 we have Q = 1 on {\\mathcal {E}}\_{\\infty , n} \\times \[-T, 0\]. Applying the strong maximum principle to the evolution equation ( [A.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ112)) of b\_s when Q=1 we deduce that b\_s = 1 everywhere in {\\mathcal {E}}\_{\\infty , n} \\times \[-T, 0\]. Hence g\_\\infty (t) is flat and ({\\mathcal {E}}\_{\\infty , n}, g\_\\infty (t), p\_\\infty ), t \\in \[-T, 0\], converges to the flat orbifold {\\mathbb {R}}^4 / {\\mathbb {Z}}\_2 as n \\rightarrow \\infty . As T> 0 was arbitrary the desired result follows by a diagonal argument. \\square\
\
## References\
\
01. Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four, [arXiv:1708.00161](http://arxiv.org/abs/1708.00161) (2017)\
\
02. Appleton, A., Wilkening, J.: Computation of U(2)-invariant Ricci flow singularities, In preparation\
\
03. Bryant, R.L.: Ricci flow solitons in dimension three with SO(3)-symmetries, available at [www.math.duke.edu/bryant/3DRotSymRicciSolitons.pdf](http://www.math.duke.edu/bryant/3DRotSymRicciSolitons.pdf)\
\
04. Calabi, E.: Métriques kählériennes et fibrés holomorphes. Ann. Sci. Ecole Norm. Sup. (4) **12**(2), 269–294 (1979)\
\
    [Article](https://doi.org/10.24033%2Fasens.1367) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=543218) [MATH](http://www.emis.de/MATH-item?0431.53056) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=M%C3%A9triques%20k%C3%A4hl%C3%A9riennes%20et%20fibr%C3%A9s%20holomorphes&journal=Ann.%20Sci.%20Ecole%20Norm.%20Sup.%20%284%29&doi=10.24033%2Fasens.1367&volume=12&issue=2&pages=269-294&publication_year=1979&author=Calabi%2CE)\
\
05. Cao, H.D.: Recent progress on Ricci solitons. In: Recent Advances in Geometric Analysis, Adv. Lectures Math., Vol. 11, pp. 1–38. Int. Press, Someville, MA (2010)\
\
06. Cao, H.D., Zhu, X.P.: A complete proof of the Poincaré and geometrization conjectures—application of the Hamilton–Perelman theory of the Ricci flow. Asian J. Math. **10**(2), 165–492 (2006)\
\
07. Chow, B., Knopf, D.: The Ricci Flow: An Introduction. Mathematical Surveys and Monographs, Vol. 110. AMS, Providence, RI (2004)\
\
08. Chow, B., Lu, P., Ni, L.: Hamilton’s Ricci Flow, Lectures in Contemporary Mathematics, Vol. 3, Science Press and Graduate Studies in Mathematics, Vol. 77, American Mathematical Society (co-publication) (2006)\
\
09. Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)\
\
10. Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)\
\
11. Chen, B.L., Zhu, X.P.: Uniqueness of the Ricci flow on complete noncompact manifolds. J. Differ. Geom. **74**(1), 119–154 (2006)\
\
12. Cao, H.D., Zhou, D.T.: On complete gradient shrinking Ricci solitons. J. Differ. Geom. **85**(2), 175–185 (2010)\
\
13. DeTurck, D.M., Kazdan, J.L.: Some regularity theorems in Riemannian geometry. Ann. Sci. Ecole Norm. Sup. (4) **14**(3), 249–260 (1981)\
\
14. Eguchi, T., Hanson, A.J.: Self-dual solutions to Euclidean gravity. Ann. Phys. **120**(1), 82–105 (1979)\
\
15. Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. **19**(5), 905–922 (2011)\
\
16. Feldman, M., Ilmanen, T., Knopf, D.: Rotationally symmetric shrinking and expanding gradient Kähler–Ricci solitons. J. Diff. Geom. **65**(2), 169–209 (2003)\
\
17. Friedman, A.: Partial Differential Equations of Parabolic Type. Prentice-Hall, Englewood Cliffs, NJ (1964)\
\
18. Feehan, P.M.N.: Maximum principles for boundary-degenerate linear parabolic differential operators, [arXiv:1306.5197](http://arxiv.org/abs/1306.5197) (2013)\
\
19. Gibbons, G.W., Hawking, S.W.: Gravitational multi-instantons. Phys. Lett. B **78**(4), 430–432 (1978)\
\
    [Article](https://doi.org/10.1016%2F0370-2693%2878%2990478-1) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=541508) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Gravitational%20multi-instantons&journal=Phys.%20Lett.%20B&doi=10.1016%2F0370-2693%2878%2990478-1&volume=78&issue=4&pages=430-432&publication_year=1978&author=Gibbons%2CGW&author=Hawking%2CSW)\
\
20. Gibbons, G.W., Hawking, S.W.: Classification of gravitational instanton symmetries. Comm. Math. Phys. **66**(3), 291–310 (1979)\
\
    [Article](https://link.springer.com/article/10.1007/BF01197189) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=535152) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Classification%20of%20gravitational%20instanton%20symmetries&journal=Comm.%20Math.%20Phys.&doi=10.1007%2FBF01197189&volume=66&issue=3&pages=291-310&publication_year=1979&author=Gibbons%2CGW&author=Hawking%2CSW)\
\
21. Hamilton, R.S.: Three-manifolds with positive Ricci curvature. J. Differ. Geom. **17**(2), 255–306 (1982)\
\
22. Hamilton, R.S.: The formation of singularities in the Ricci flow. In: Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), pp. 7–136. Int. Press, Cambridge, MA (1995)\
\
23. Hamilton, R.S.: Four-manifolds with positive curvature operator. J. Differ. Geom. **24**(2), 153–179 (1986)\
\
    [Article](https://doi.org/10.4310%2Fjdg%2F1214440433) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=862046) [MATH](http://www.emis.de/MATH-item?0628.53042) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Four-manifolds%20with%20positive%20curvature%20operator&journal=J.%20Differ.%20Geom.&doi=10.4310%2Fjdg%2F1214440433&volume=24&issue=2&pages=153-179&publication_year=1986&author=Hamilton%2CRS)\
\
24. Isenberg, J., Knopf, D., Sesum, N.: Non-Kähler Ricci flow singularities that converge to Kähler–Ricci solitons, [arXiv:1703.02918v2](http://arxiv.org/abs/1703.02918v2) (2017)\
\
25. Kronheimer, P.B.: The construction of ALE spaces as hyper-Kähler quotients. J. Differ. Geom. **29**(3), 665–683 (1989)\
\
26. Kronheimer, P.B.: A Torelli-type theorem for gravitational instantons. J. Differ. Geom. **29**(3), 685–697 (1989)\
\
27. Li, X.L., Zhang, Y.J.: Ancient solutions to the Ricci flow in higher dimensions, [arXiv:1812.04156](http://arxiv.org/abs/1812.04156) (2018)\
\
28. Máximo, D.: On the blow-up of four-dimensional Ricci flow singularities. J. Reine Angew. Math. **692**, 153–171 (2014)\
\
29. Naber, A.: Noncompact shrinking four solitons with nonnegative curvature. J. Reine Angew. Math. **645**, 125–153 (2010)\
\
    [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=2673425) [MATH](http://www.emis.de/MATH-item?1196.53041) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Noncompact%20shrinking%20four%20solitons%20with%20nonnegative%20curvature&journal=J.%20Reine%20Angew.%20Math.&volume=645&pages=125-153&publication_year=2010&author=Naber%2CA)\
\
30. Petersen, P.: Riemannian Geometry, 3rd Edition. Graduate Texts in Mathematics, Vol. 171. Springer, Cham (2016)\
\
31. Protter, M.H., Weinberger, H.F.: Maximum Principles in Differential Equations. Springer-Verlag, New York (1984)\
\
32. Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. **30**(1), 223–301 (1989)\
\
33. Topping, P.: Lectures on the Ricci Flow. London Mathematical Society Lecture Note Series, Vol. 325. Cambridge University Press, Cambridge (2006)\
\
34. Verdiani, L., Ziller, W.: Smoothness conditions in cohomogeneity manifolds, [arXiv:1804.04680](http://arxiv.org/abs/1804.04680) (2018)\
\
35. Whitney, H.: Differentiable even functions. Duke Math. J. **10**(1), 159–160 (1943)\
\
    [Article](https://doi.org/10.1215%2FS0012-7094-43-01015-4) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=7783) [MATH](http://www.emis.de/MATH-item?0063.08235) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Differentiable%20even%20functions&journal=Duke%20Math.%20J.&doi=10.1215%2FS0012-7094-43-01015-4&volume=10&issue=1&pages=159-160&publication_year=1943&author=Whitney%2CH)\
\
\
[Download references](https://citation-needed.springer.com/v2/references/10.1007/s42543-022-00048-y?format=refman&flavour=references)\
\
## Acknowledgements\
\
The author would like to thank his PhD advisors Richard Bamler and Jon Wilkening for their constant support and encouragement. This work was supported by a GSR fellowship, which was funded by NSF grant DMS-1344991. Finally the author would like to thank the anonymous referee for their helpful comments.\
\
## Author information\
\
### Authors and Affiliations\
\
1. Department of Mathematics, UC Berkeley, Berkeley, CA, 94720, USA\
\
Alexander Appleton\
\
\
Authors\
\
1. Alexander Appleton\
\
\
[View author publications](https://link.springer.com/search?sortBy=newestFirst&contributor=Alexander%20Appleton)\
\
\
\
\
\
Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Alexander%20Appleton) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Alexander%20Appleton%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)\
\
\
### Corresponding author\
\
Correspondence to\
[Alexander Appleton](mailto:lx.appleton@googlemail.com).\
\
## Appendices\
\
### Appendix A\
\
Here we carry out some of the computations we rely on throughout the paper. Recall\
\
\\begin{aligned} \\frac{\\partial }{\\partial s} = \\frac{1}{u(\\xi , t)} \\frac{\\partial }{\\partial \\xi } \\end{aligned}\
\
and the commutation relation\
\
\\begin{aligned}{}\[\\partial \_t, \\partial \_s\] = - \\frac{a\_{ss}}{a} - 2 \\frac{b\_{ss}}{b} \\end{aligned}\
\
from Sect. [2.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec12). For the computations it will also be helpful to keep in mind that\
\
\\begin{aligned} bQ\_s = a\_s - Q b\_s \\end{aligned}\
\
which follows from differentiating the expression Q = \\frac{a}{b}. Finally recall the definition of the Kähler quantities\
\
\\begin{aligned} x = a\_s + Q^2 -2 \\end{aligned}\
\
and\
\
\\begin{aligned} y = b\_s - Q \\end{aligned}\
\
from Sect. [4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec15).\
\
First we compute the evolution equation of _Q_:\
\
\\begin{aligned} \\partial \_t Q = \\frac{\\partial \_t a}{b} - \\frac{a \\partial \_t b}{b^2}. \\end{aligned}\
\
Inserting the expressions for \\partial \_t a and \\partial \_t b from the evolution equations ( [2.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ17)) and ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) for _a_ and _b_ we obtain\
\
\\begin{aligned} \\partial \_t Q = Q\_{ss} + 3 \\frac{b\_s}{b} Q\_s + \\frac{4}{b^2} Q\\big (1-Q^2\\big ). \\end{aligned}\
\
### 1.1 Evolution Equations of a\_s, b\_s, Qb\_s, _x_, _y_ and \\frac{y}{Q}\
\
By the commutation relations above we have\
\
\\begin{aligned} \\partial \_t a\_s&= \\partial \_s \\partial \_t a - \\left( \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b}\\right) a\_s, \\\ \\partial \_t b\_s&= \\partial \_s \\partial \_t b - \\left( \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b}\\right) b\_s. \\end{aligned}\
\
Hence plugging in the expressions for \\partial \_t a and \\partial \_t b from the evolution equations ( [2.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ17)) and ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) for _a_ and _b_ we obtain\
\
\\begin{aligned} \\partial \_t a\_s&= (a\_s)\_{ss} + \\left( 2 \\frac{b\_s}{b} - \\frac{a\_s}{a}\\right) (a\_s)\_s + \\frac{1}{b^2}\\big ( -2 a\_s b\_s^2- 6 Q^2 a\_s + 8 Q^3 b\_s \\big ), \\\ \\partial \_t b\_s&= (b\_s)\_{ss} + \\frac{a\_s}{a} (b\_s)\_s + \\frac{1}{b^2}\\left( -\\frac{a\_s^2 b\_s}{Q^2}+4 Q a\_s-6 Q^2 b\_s-b\_s^3+4 b\_s \\right) . \\end{aligned}\
\
From here we can compute the evolution equation of Q b\_s:\
\
\\begin{aligned} \\partial \_t Qb\_s&= (\\partial \_t Q )b\_s + Q \\partial \_t b\_s \\\&= (Qb\_s)\_{ss} + \\left( 2 \\frac{b\_s}{b} - \\frac{a\_s}{a}\\right) (Qb\_s)\_s +\\frac{1}{b^2}\\big ( 4 Q^2 a\_s- 10 Q^3 b\_s - 2 Q b\_s^3 + 8 Q b\_s\\big ). \\end{aligned}\
\
Now we may compute the evolution equations of the Kähler quantities _x_ and _y_:\
\
\\begin{aligned} \\partial \_t x&= \\partial \_t a\_s + 2 Q \\partial \_t Q \\\&= x\_{ss} + \\left( 2 \\frac{b\_s}{b} - \\frac{a\_s}{a}\\right) x\_s - \\frac{2}{b^2}\\big (2 Q^2 + y^2\\big ) x - \\frac{2}{b^2}\\big (Q^2 +2 \\big ) y^2, \\end{aligned}\
\
where in the last step we made the substitutions a\_s = x - Q^2 + 2, b\_s = y + Q and a = Q b. Similarly,\
\
\\begin{aligned} \\partial \_t y&= \\partial \_t b\_s - \\partial \_t Q \\nonumber \\\&= y\_{ss} + \\frac{a\_s}{a} y - \\frac{y}{a^2} \\left( \\left( x+2\\right) ^2 + Q^2 \\big (2x + y^2\\big ) \\right) . \\end{aligned}\
\
(A.1)\
\
\
Then we can compute\
\
\\begin{aligned} \\partial \_t \\left( \\frac{y}{Q}\\right)&=\\frac{\\partial \_t y}{Q} - \\frac{y \\partial \_t Q}{Q^2} \\nonumber \\\&= \\left( \\frac{y}{Q}\\right) \_{ss} + \\left( 3 \\frac{a\_s}{a} - 2 \\frac{b\_s}{b} \\right) \\left( \\frac{y}{Q}\\right) \_s + \\frac{2}{b^2}\\frac{y}{Q}\\left( 2 + \\frac{y}{Q}\\right) \\left( Q b\_s - 2 a\_s \\right) , \\end{aligned}\
\
(A.2)\
\
\
where we substituted a\_s = x - Q^2 + 2, b\_s = y + Q and a = Q b in the last step.\
\
### 1.2 Evolution Equation of H\_{\\pm }\
\
In Sect. [7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec18) we define the quantities\
\
\\begin{aligned} H\_{\\pm } :=bb\_{ss} \\mp a\_s^2 - b\_s^2 \\pm C \\end{aligned}\
\
for some constant C> 0. Below we derive its evolution equation.\
\
First note that we have\
\
\\begin{aligned} \\partial \_t b\_{ss} = \\partial \_s \\partial \_t b\_{s} - \\left( \\frac{a\_{ss}}{a} + 2 \\frac{b\_{ss}}{b}\\right) b\_s. \\end{aligned}\
\
Substituting the evolution equation for b\_s derived above we obtain\
\
\\begin{aligned} \\partial \_t b\_{ss}&= (b\_{ss})\_{ss} +\\frac{a\_s}{a}(b\_{ss})\_s + \\frac{4 a a\_{ss}}{b^3}-\\frac{2 a\_s^2 b\_{ss}}{a^2}+\\frac{2 a\_s^3 b\_s}{a^3} \\\&\\quad \\quad -\\frac{24 a a\_s b\_s}{b^4}+\\frac{4 a\_s^2}{b^3}-\\frac{2 a\_s a\_{ss} b\_s}{a^2}-\\frac{6 a^2 b\_{ss}}{b^4}+\\frac{24 a^2 b\_s^2}{b^5}\\\&\\quad \\quad -\\frac{2 b\_{ss}^2}{b}+\\frac{4 b\_{ss}}{b^2}+\\frac{2 b\_s^4}{b^3}-\\frac{8 b\_s^2}{b^3}-\\frac{3 b\_s^2 b\_{ss}}{b^2}. \\end{aligned}\
\
Hence we can compute the evolution equation of _H_ via\
\
\\begin{aligned} \\partial \_t H = (\\partial \_t b)b\_{ss} + b \\partial \_t b\_{ss} \\mp 2 a\_s \\partial \_t a\_s - 2 b\_s \\partial \_t b\_s \\end{aligned}\
\
and substituting the expressions for \\partial \_t b, \\partial \_t b\_{ss}, \\partial \_t a\_s and \\partial \_t b\_s derived above. Noting that\
\
\\begin{aligned} H\_s = \\mp 2 a\_s a\_{ss}+b (b\_{ss})\_s-b\_{s} b\_{ss} \\end{aligned}\
\
and\
\
\\begin{aligned} H\_{ss} = \\mp 2 a\_{ss}^2 \\mp 2 (a\_{ss})\_{s} a\_s+b (b\_{ss})\_{ss}-b\_{ss}^2, \\end{aligned}\
\
a longer computation shows that\
\
\\begin{aligned} \\partial \_t H\_\\pm= & {} \[H\_\\pm \]\_{ss} + \\left( \\frac{a\_s}{a} -2 \\frac{b\_s}{b}\\right) \[H\_\\pm \]\_s +H\_\\pm \\left( -\\frac{2 a\_s^2}{a^2}-\\frac{4 a^2}{b^4}-\\frac{4b\_s^2}{b^2}\\right) \\\{} & {} \\pm C \\left( \\frac{2 a\_s^2}{a^2}+\\frac{4 a^2}{b^4}+\\frac{4b\_s^2}{b^2}\\right) \\\{} & {} \\pm 2 a\_{ss}^2 + a\_{ss} \\left( -\\frac{2 b a\_s b\_s}{a^2} \\mp \\frac{8 a\_s b\_s}{b} \\pm \\frac{4 a\_s^2}{a}+\\frac{4a}{b^2}\\right) \\\{} & {} +\\frac{2 b a\_s^3 b\_s}{a^3}-\\frac{32 a a\_sb\_s}{b^3}\\mp \\frac{16 a^3 a\_s b\_s}{b^5}+\\frac{4 a\_s^2}{b^2} \\pm \\frac{8 a^2a\_s^2}{b^4} \\\{} & {} \\mp \\frac{2 a\_s^4}{a^2} +\\frac{32 a^2 b\_s^2}{b^4}-\\frac{16 b\_s^2}{b^2}. \\end{aligned}\
\
### 1.3 Evolution Equation of f\_{\\theta }(Q)\
\
\\begin{aligned} \\partial \_t f\_{\\theta }(Q)&= f' \\partial \_t Q \\\&= f' \\left( Q\_{ss} + 3 \\frac{b\_s}{b} Q\_s + \\frac{4}{b^2}Q \\big (1 - Q^2\\big ) \\right) \\end{aligned}\
\
by the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_. Note that we omitted the dependence the quantities on spacetime (\\xi , t) and the dependence of _f_ on _Q_ and \\theta . For example we wrote f' for f'\_{\\theta }(Q(\\xi ,t)). Noting that\
\
\\begin{aligned} \\left\[ f(Q)\\right\] \_{s} = f'(Q)Q\_s \\end{aligned}\
\
and\
\
\\begin{aligned} \\left\[ f(Q)\\right\] \_{ss} = f''(Q)Q^2\_s + f'(Q) Q\_{ss}, \\end{aligned}\
\
we obtain\
\
\\begin{aligned} \\partial \_t f(Q)&= \[f(Q)\]\_{ss} - f'' Q\_s^2 + 3 \\frac{b\_s}{b} \[f(Q)\]\_s + \\frac{4}{b^2} f' Q \\big (1 - Q^2 \\big ) \\\&= \[f(Q)\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2 \\frac{b\_s}{b} \\right) \[f(Q)\]\_s \\\&\\quad + \\left( 5 \\frac{b\_s}{b} - 3 \\frac{a\_s}{a} \\right) \[f(Q)\]\_s + \\frac{4}{b^2} f' Q \\big (1 - Q^2 \\big ) - f'' Q\_s^2\\\&= \[f(Q)\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2 \\frac{b\_s}{b} \\right) \[f(Q)\]\_s + \\frac{1}{b^2} C\_f, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_f&= \\left( 5 b\_s - 3 \\frac{a\_s}{Q} \\right) b\[f(Q)\]\_s + 4 f' Q \\big (1 - Q^2 \\big ) - f'' b^2 Q\_s^2 \\\&= \\left( 5 b\_s - 3 \\frac{a\_s}{Q} \\right) f' \\left( a\_s - Qb\_s\\right) + 4 f' Q \\big (1 - Q^2 \\big ) - \\left( a\_s - Q b\_s\\right) ^2f'' \\\&= \\left( 8 a\_s b\_s - 3 \\frac{a\_s^2}{Q} - 5 Q b\_s^2 + 4 Q \\big (1 - Q^2\\big ) \\right) f' - \\left( a\_s - Q b\_s \\right) ^2f''. \\end{aligned}\
\
### 1.4 Evolution Equation of Z\_{\\theta }\
\
We have\
\
\\begin{aligned} \\partial \_t Z\_{\\theta } = \\partial \_t \\left( \\frac{x}{Q^2}\\right) + \\partial \_t f\_{\\theta }(Q). \\end{aligned}\
\
We computed the evolution equation for f\_{\\theta }(Q) above. Therefore it remains to compute \\partial \_t \\frac{x}{Q^2}. For this recall the evolution equation ( [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ42)) of _x_\
\
\\begin{aligned} \\partial \_t x = x\_{ss} + \\left( 2 \\frac{b\_s}{b} - \\frac{a\_s}{a} \\right) x\_{s} + \\frac{1}{b^2}C\_x, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_x = - 2 \\big (2 Q^2 + y^2\\big ) x - 2 \\big (Q^2 +2 \\big ) y^2. \\end{aligned}\
\
Differentiation shows that\
\
\\begin{aligned} \\partial \_s \\left( \\frac{x}{Q^2}\\right) = \\frac{x\_s}{Q^2}- 2 \\frac{xQ\_s}{Q^3} \\end{aligned}\
\
and\
\
\\begin{aligned} \\partial \_{ss} \\left( \\frac{x}{Q^2}\\right) = \\frac{x\_{ss}}{Q^2}- 4 \\frac{x\_sQ\_s}{Q^3} - 2x \\frac{Q\_{ss}}{Q^3} + 6x \\frac{Q\_s^2}{Q^4} . \\end{aligned}\
\
Therefore we get\
\
\\begin{aligned} \\partial \_t \\frac{x}{Q^2}&= \\frac{1}{Q^2}\\partial \_t x - 2\\frac{x}{Q^3} \\partial \_t Q \\\&= \\left( \\frac{x}{Q^2}\\right) \_{ss}+ \\left( 3\\frac{a\_s}{a} - 2 \\frac{b\_s}{b} \\right) \\left( \\frac{x}{Q^2}\\right) \_s + \\frac{1}{b^2} C\_{\\frac{x}{Q^2}}, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_{\\frac{x}{Q^2}}&= 6 \\frac{x a\_s}{Q^4} (bQ\_s) - 10 \\frac{x b\_s}{Q^3} (bQ\_s) - 6\\frac{x}{Q^4} (bQ\_s)^2 + \\frac{C\_x}{Q^2} - \\frac{8x}{Q^2} \\big (1- Q^2\\big ) \\\&= -\\frac{4 a\_{s}^2 b\_{s}}{Q^3}+\\frac{2 a\_{s} b\_{s}^2}{Q^2}+\\frac{8 a\_{s} b\_{s}}{Q^3}-\\frac{8 a\_{s}}{Q^2}+2 a\_{s}-\\frac{8 b\_{s}^2}{Q^2}+8 Q b\_{s}+\\frac{16}{Q^2}-16. \\end{aligned}\
\
In the last step, we used the expressions for _x_, _y_ and Q\_s in terms of a\_s, b\_s and _Q_ to eliminate _x_, _y_ and Q\_s from the expression for C\_{\\frac{x}{Q^2}}. Hence we have\
\
\\begin{aligned} \\partial \_t Z\_{\\theta } = \[Z\_{\\theta }\]\_{ss} + \\left( 3\\frac{a\_s}{a} - 2 \\frac{b\_s}{b}\\right) \[Z\_{\\theta }\]\_s + \\frac{1}{b^2} C\_Z, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_Z = C\_{\\frac{x}{Q^2}} + C\_f. \\end{aligned}\
\
As\
\
\\begin{aligned} Z\_{\\theta } = \\frac{x}{Q^2} + f\_{\\theta }(Q) = \\frac{a\_s + Q^2 - 2}{Q^2} + f\_{\\theta }(Q) \\end{aligned}\
\
by definition, we can solve for a\_s to obtain\
\
\\begin{aligned} a\_s = Q^2 Z\_{\\theta } - Q^2 f\_{\\theta } + 2 - Q^2. \\end{aligned}\
\
Using this substitution to eliminate all occurring a\_s from the expression C\_Z we obtain\
\
\\begin{aligned} C\_Z = C\_{Z,0} + C\_{Z,1} Z\_{\\theta } + C\_{Z,2} Z\_{\\theta }^2, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_{Z,0}&= A\_0 + A\_1 \\left\[ \\frac{b\_s}{Q}\\right\] + A\_2 \\left\[ \\frac{b\_s}{Q}\\right\] ^2, \\\ C\_{Z,1}&= 2 Q^3 b\_s f''+8 Q^2 b\_s f'+8 f Q b\_s+8 Qb\_s-\\frac{8 b\_s}{Q} +2 b\_s^2+2 f Q^4 f''\\\&\\quad +2 Q^4 f''-4Q^2 f''+6 f Q^3 f'+6 Q^3 f'-12 Q f'+2 Q^2-8,\\\ C\_{Z,2}&= -4 Q b\_s -Q^4f''-3 Q^3 f', \\end{aligned}\
\
and\
\
\\begin{aligned} A\_0 =&- Q^4 f^2 f''-2 Q^4 f f''-Q^4 f''+4 Q^2 f f''+4 Q^2 f''-4 f''-3 Q^3 f^2 f' \\\&-6 Q^3 f f'-7 Q^3 f'+12 Q f f'+16 Q f'-\\frac{12 f'}{Q}-2 Q^2 f+8 f-2 Q^2-4, \\\ A\_1 =&-2 Q^4 f f''-2 Q^4 f''+4 Q^2 f''-8 Q^3 f f'-8 Q^3 f' \\\&+16 Q f'-4 Q^2 f^2-8 Q^2 f+8 f+4 Q^2+8, \\\ A\_2 =&- Q^4f''-5 Q^3 f'-2 Q^2 f-2 Q^2-4. \\\ \\end{aligned}\
\
### 1.5 Evolution Equation of Z\_1\
\
The evolution equation for Z\_1 = \\frac{x}{Q^2} + 1 follows quickly from the evolution equations for Z\_{\\theta } by setting f = 1. One obtains\
\
\\begin{aligned} \\partial \_t Z\_1 = \[Z\_1\]\_{ss} + \\left( 3\\frac{a\_s}{a} - 2 \\frac{b\_s}{b}\\right) \[Z\_1\]\_s + \\frac{1}{b^2}\\big ( C\_{Z\_1, 0} + C\_{Z\_1, 1} Z\_1 + C\_{Z\_1, 2} Z\_1^2\\big ),\\nonumber \\\ \\end{aligned}\
\
(A.3)\
\
\
where\
\
\\begin{aligned} C\_{Z\_1,0}&= \\frac{1}{Q^2}\\left( - 4\\big (1+Q^2\\big )y^2 + 8Q\\big (1-2Q^2 \\big )y + 16Q^2\\big (1-Q^2\\big ) \\right) , \\\ C\_{Z\_1,1}&= 16 Q b\_s-\\frac{8 b\_s}{Q}+2 b\_s^2+2 Q^2-8, \\\ C\_{Z\_1,2}&= -4 Q b\_s. \\end{aligned}\
\
Note that we wrote C\_{Z\_1,0} in terms of y = b\_s - Q instead of b\_s in order to see the similarity with the zeroth order term of the evolution equation of T\_1 presented in the proof of Lemma [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar44).\
\
### 1.6 Evolution Equations When Q=1\
\
When Q = 1 we have a = b and the Ricci flow equations simplify. In particular, we obtain\
\
\\begin{aligned} \\frac{\\partial \_t u}{u}&= 3\\frac{b\_{ss}}{b}, \\\ \\partial \_t b&= b\_{ss} + \\frac{2}{b}\\big (b\_s^2 -1 \\big ). \\end{aligned}\
\
Using the commutation relation of \\partial \_t and \\partial \_s we can also compute the evolution equation of b\_s and b\_{ss}:\
\
\\begin{aligned} \\partial \_t b\_s&= \\partial \_s \\partial \_t b - 3 b\_s \\frac{b\_{ss}}{b} \\nonumber \\\&= (b\_s)\_{ss} + \\frac{b\_s}{b}(b\_s)\_s + 2 \\frac{b\_s}{b^2}\\big ( 1- b\_s^2\\big ). \\end{aligned}\
\
(A.4)\
\
\
Similarly,\
\
\\begin{aligned} \\partial \_t b\_{ss}&= \\partial \_s \\partial \_t b\_s - 3 b\_{ss} \\frac{b\_{ss}}{b} \\nonumber \\\&= (b\_{ss})\_{ss} +\\frac{b\_{s}}{b} (b\_{ss})\_s -\\frac{2 b\_{ss}^2}{b}+\\frac{4 \\left( b\_{s}^2-1\\right) b\_{s}^2}{b^3} \\nonumber \\\&\\quad -\\frac{5 b\_{s}^2 b\_{ss}}{b^2}-\\frac{2 \\left( b\_{s}^2-1\\right) b\_{ss}}{b^2}. \\end{aligned}\
\
(A.5)\
\
\
Let us introduce the notation\
\
\\begin{aligned} X&:=1 - b\_s^2, \\\ Y&:=-b b\_{ss}. \\end{aligned}\
\
We need the evolution equations of _scale-invariant_ quantities of the form\
\
\\begin{aligned} T\_F = -Y + F(X), \\end{aligned}\
\
where F: \[0, 1\] \\rightarrow {\\mathbb {R}} is a smooth function. In particular, we see that\
\
\\begin{aligned} \\partial \_t T\_F = (\\partial \_t b) b\_{ss} + b \\partial \_t b\_{ss} -2 b\_s F'\\big (1-b\_s^2\\big ) \\partial \_t b\_s. \\end{aligned}\
\
Expanding this expression, we obtain\
\
\\begin{aligned} \\partial \_t T\_F = (T\_F)\_{ss} - \\frac{b\_s}{b}(T\_F)\_s + \\frac{1}{b^2} C\_F, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_F&= 4 X^2-4 X Y-4 X-2 Y^2+4 Y \\\&\\quad +2\\big ( 2 X^2-2 X Y-2 X+Y^2+2 Y \\big )F'(X) \\\&\\quad +4 (X-1) Y^2 F''(X). \\end{aligned}\
\
In this paper we make use of three different choices of _F_:\
\
\\begin{aligned} F\_0(X)&= 0, \\\ F\_1(X)&= X, \\\ F\_2(X)&= X - X^2. \\end{aligned}\
\
Plugging these into the expression for C\_F above we compute\
\
\\begin{aligned} C\_{F\_0}&= -4 b\_s^2 \\big ( 1- b\_s^2\\big ) -2 b b\_{ss} \\big (b b\_{ss}+2 b\_s^2\\big ) ,\\\ C\_{F\_1}&= -8 b\_s^2 T\_{F\_1}, \\\ C\_{F\_2}&= 4 \\left( (2-3 X) Y^2 +\\big (2 X^2-4 X+2\\big ) Y -2 (X-1)^2 X \\right) . \\end{aligned}\
\
We also prove the following lemma here:\
\
### Lemma A.1\
\
Let X\\in \[0,1\]. Then whenever 0 \\le Y < X - X^2 we have\
\
\\begin{aligned} P(X,Y) :=(2-3 X) Y^2 +\\big (2 X^2-4 X+2\\big ) Y -2 (X-1)^2 X < 0. \\end{aligned}\
\
In other words, C\_{F\_2} < 0 whenever T\_{F\_2} > 0 and bb\_{ss} \\le 0.\
\
### Proof\
\
Let _R_ be the region in the _X_- _Y_-plane satisfying the inequalities X\\in \[0,1\] and 0 \\le Y < X - X^2. Note that Y < X - X^2 and Y \\ge 0 implies that X \\in (0,1). A computation shows\
\
\\begin{aligned} P(X, X- X^2) = -3 (X-1)^2 X^3 < 0 \\,\\quad \\text { for } \\, X \\in (0,1). \\end{aligned}\
\
Notice that for a fixed X \\in \[0, \\frac{2}{3}\] the quadratic polynomial _P_( _X_, _Y_) in _Y_ is convex. As\
\
\\begin{aligned} P(X, 0) = -2 (X-1)^2 X < 0 \\, \\quad \\text { for } \\, X \\in (0,1), \\end{aligned}\
\
we deduce that P(X,Y) > 0 on R \\cap \\{ X \\le \\frac{2}{3} \\}. To prove that P(X, Y) > 0 in R \\cap \\{ X \\ge \\frac{2}{3} \\} is trickier. For this we prove the following claim:\
\
### Claim 1\
\
\\partial \_X P(X, Y) > 0 on R \\cap \\{ X \\ge \\frac{2}{3} \\}.\
\
### Proof of Claim 1\
\
A computation shows\
\
\\begin{aligned} \\partial \_X P(X, Y) = -6 X^2+8 X -2 +(4 X-4) Y-3 Y^2. \\end{aligned}\
\
Hence for fixed _X_ is concave in _Y_. Then note that\
\
\\begin{aligned} \\partial \_X P(X, 0) = -6 X^2+8 X -2 > 0 \\,\\quad \\text { for } X \\in \\bigg \[\\frac{2}{3},1\\bigg ) \\end{aligned}\
\
and\
\
\\begin{aligned} \\partial \_X P(X, X-X^2) = (1-X) \\big (3 X^3+X^2+2 X-2\\big ) > 0 \\quad \\text { for } \\, X \\in \\bigg \[\\frac{2}{3},1\\bigg ). \\end{aligned}\
\
The last inequality follows by the fact that the polynomial 3 X^3+X^2+2 X-2 is increasing on \[0, 1\] and evaluates to \\frac{2}{3} at X = \\frac{2}{3}. Hence the claim follows by concavity of \\partial \_X P(X, Y) in _Y_. \\square\
\
By above we know that P(X,X^2-X) < 0 for X\\in (0,1). Hence using the result of the claim, we see that P(X,Y) < 0 on R \\cap \\{ X \\ge \\frac{2}{3} \\}. \\square\
\
### Appendix B: Removable Singularity\
\
We prove the following theorem:\
\
### Theorem B.1\
\
(Removable singularity)   Let ({\\mathbb {R}}^4 \\setminus \\{0\\}, g(t)), t \\in \[0,T\], be a rotationally symmetric Ricci flow of bounded curvature, i.e., there exists a K>0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} < K \\quad \\text { on } \\, {\\mathbb {R}}^4 \\times \[0,T\]. \\end{aligned}\
\
Taking \\xi \\in (0,\\infty ) to be a radial coordinate on {\\mathbb {R}}^4 \\setminus \\{0\\} the metric _g_( _t_) may be written as\
\
\\begin{aligned} g(t) = u^2(\\xi , t) d\\xi ^2 + b^2(\\xi ,t) g\_{S^3}, \\end{aligned}\
\
where u,b : (0,\\infty ) \\rightarrow {\\mathbb {R}} are smooth warping functions, and g\_{S^3} is the round metric on S^3 with sectional curvatures equal to one. If for all t \\in \[0,T\] the warping function b(\\xi ,t) \\rightarrow 0 as \\xi \\rightarrow 0, then _g_( _t_) can be extended to a smooth Ricci flow on {\\mathbb {R}}^4 \\times (0,T\].\
\
Below we assume ({\\mathbb {R}}^4 \\setminus \\{0\\}, g(t)), t \\in \[0,T\], is a Ricci flow as in Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175). The proof strategy will be as follows: First we prove in Lemma [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar176) that for every t\_0 \\in \[0,T\] there exist coordinates x^i, i = 1,2,3,4, of {\\mathbb {R}}^4 for which the metric g(t\_0) can be extended to a C^{1,1} metric on {\\mathbb {R}}^4. Note, however, without control on the derivative of the curvature tensor the metric _g_( _t_) at times t \\ne t\_0 may not to be C^{1,1} with respect to the coordinates x^i. To get around this issue we show in Lemmas [B.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar181) and [B.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar187) that in fact all derivatives \\nabla ^m \\textrm{Rm}, m \\in {\\mathbb {N}}, of the curvature tensor are bounded on {\\mathbb {R}}^4 \\setminus \\{0\\}\\times (\\delta ,T\] for any \\delta > 0. The proof utilizes Shi’s interior derivative estimates and is based on a De Giorgi–Nash–Moser iteration argument. With these results in place, we use harmonic coordinates to prove Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175). Let us begin by proving\
\
### Lemma B.2\
\
Let g = ds^2 + b(s)^2 g\_{S^3} be a smooth, rotationally symmetric metric with bounded curvature on {\\mathbb {R}}^4\\setminus \\{0\\}. Here g\_{S^3} is the round metric of curvature one on S^3 and b: (0,\\infty ) \\rightarrow {\\mathbb {R}} is a smooth positive function. If\
\
\\begin{aligned} b \\rightarrow 0 \\, \\quad \\text { as } \\, s \\rightarrow 0, \\end{aligned}\
\
then _g_ can be extended to a C^{1,1} metric on {\\mathbb {R}}^4. Furthermore, if we take standard Euclidean coordinates x\_i, i = 1, 2, 3,4, on {\\mathbb {R}}^4 we have g\_{ij} = \\delta \_{ij} and \\partial \_k g\_{ij} = 0 at the origin, and \\partial \_k \\partial \_l g\_{ij} locally bounded on {\\mathbb {R}}^4\\setminus \\{0\\}.\
\
### Proof\
\
As _g_ has bounded curvature there exists a K>0 such that\
\
\\begin{aligned} \\Big \|\\frac{b\_{ss}}{b}\\Big \|, \\Big \|\\frac{1-b\_s^2}{b^2}\\Big \| \\le K, \\end{aligned}\
\
because these are the only non-zero curvature components of a rotationally symmetric metric. In particular, this shows that\
\
\\begin{aligned} b\_s \\rightarrow 1 \\,\\quad \\text { as } \\, s \\rightarrow 0^+ \\end{aligned}\
\
and\
\
\\begin{aligned} b\_{ss} \\rightarrow 0 \\,\\quad \\text { as } \\, s \\rightarrow 0^+. \\end{aligned}\
\
Let x\_i, i =1, 2,3,4, be Euclidean coordinates of {\\mathbb {R}}^4, normalized such that \\sum \_i (x^i)^2 = s^2. In these coordinates\
\
\\begin{aligned} g = \\left\[ \\delta \_{ij} + \\big (s^2 \\delta \_{ij} - x\_i x\_j \\big ) \\Psi (s) \\right\] {d}x^i {d}x^j, \\end{aligned}\
\
where\
\
\\begin{aligned} \\Psi (s) = \\frac{\\left( \\frac{b}{s}\\right) ^2 -1}{s^2}. \\end{aligned}\
\
Note that we used the Einstein summation convention.\
\
### Claim 1\
\
\\Psi , s \\partial \_s \\Psi , s^2 \\partial \_{ss} \\Psi = O(K) as s\\rightarrow 0.\
\
### Proof of Claim 1\
\
Fix s>0. By Taylor’s theorem there exist numbers s\_0, s\_1 \\in (0,s) such that\
\
\\begin{aligned}&b(s) = s + \\frac{1}{2} b\_{ss}(s\_0) s^2, \\\&b\_s(s) = 1 + b\_{ss}(s\_1)s. \\end{aligned}\
\
Hence\
\
\\begin{aligned} \\Psi (s)&= \\frac{b\_{ss}(s\_0)}{s} + \\left( \\frac{b\_{ss}(s\_0)}{2}\\right) ^2. \\end{aligned}\
\