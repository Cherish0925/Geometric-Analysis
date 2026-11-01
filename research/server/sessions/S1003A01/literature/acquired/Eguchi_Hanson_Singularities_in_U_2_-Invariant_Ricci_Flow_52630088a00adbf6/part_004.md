---
retention_scope: session
part: 4
total_parts: 7
---

[Part 4/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

\\begin{aligned} \\xi \_i(p) = d\_{g\_i(0)}(p, \\Sigma \_{o\_i}) \\end{aligned}\
\
and\
\
\\begin{aligned} \\xi \_\\infty (p) = d\_{g\_\\infty (0)}(p, \\Sigma \_{o\_\\infty }) \\end{aligned}\
\
on C\_{g\_i(0)}\\left( p\_i, r\\right)  and {\\mathcal {C}}\_\\infty . Note that the coordinates \\xi \_i and \\xi \_\\infty  are smooth away from a non-principal orbit and furthermore that \\xi \_i \\rightarrow \\xi \_\\infty  in C^\\infty  away from a non-principal orbit. Hence we obtain the one-forms d\\xi \_i and d\\xi \_\\infty  away from a non-principal orbit, which are orthogonal to all orbits of C\_{g\_i(0)}\\left( p\_i, r\\right)  and {\\mathcal {C}}\_\\infty , respectively. For brevity we drop the subscript and write \\xi  for the coordinates \\xi \_i or \\xi \_\\infty .\
\
Since the metric g\_\\infty (t) is _U_(2)-invariant, as shown above, there exist warping functions u\_\\infty , a\_\\infty , b\_\\infty : {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\] \\rightarrow {\\mathbb {R}}\_{\\ge 0} such that the metric can be expressed as\
\
\\begin{aligned} g\_\\infty (t) = u^2\_\\infty (\\xi , t) d\\xi ^2 + a^2\_\\infty (\\xi ,t) \\omega \\otimes \\omega + b\_\\infty ^2(\\xi , t) \\pi ^\*(g\_\\textrm{FS}), \\end{aligned}\
\
where at time 0 we have\
\
\\begin{aligned} u = 1 \\quad \\, \\text { on } \\, {\\mathcal {C}}\_\\infty . \\end{aligned}\
\
As\
\
\\begin{aligned} a\_\\infty (p,t) = \|{\\overline{X}}\_{\\infty , 0}\|\_{g\_\\infty (t)}(p) \\end{aligned}\
\
and {\\overline{X}}\_{i,o} \\rightarrow {\\overline{X}}\_{\\infty ,0} as i \\rightarrow \\infty  by above, we see that away from a non-principal orbit a\_i \\rightarrow a\_\\infty  smoothly. Similarly, one can show with help of the remaining Killing vector fields {\\overline{X}}\_{i,j}, j = 1, 2, 3, that away from a non-principal orbit b\_i \\rightarrow b\_\\infty  smoothly.\
\
Hence away from a non-principal orbit, a\_i(\\xi , t), b\_i(\\xi , t) \\rightarrow a\_\\infty (\\xi , t), b\_\\infty (\\xi , t) in C^\\infty  as i \\rightarrow \\infty . Furthermore, from the curvature bounds on \\Omega \_i and the boundary conditions on a\_i, b\_i, a\_\\infty , b\_\\infty  at a non-principal orbit (see Sect.  [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec10) for the smoothness conditions on the warping functions at the non-principal orbit), one can show that in fact a\_i(\\xi , t), b\_i(\\xi , t) \\rightarrow a\_\\infty (\\xi , t), b\_\\infty (\\xi , t) smoothly everywhere. Hence the metric g\_\\infty (t), t \\in \[-\\Delta t,0\], is in the class {\\mathcal {I}}. As a\_s \\ge 0 for metrics in {\\mathcal {I}} we see that {\\mathcal {C}}\_\\infty  can possess at most one non-principal orbit. Finally, we note that by \[ [9](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR9 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part I: Geometric Aspects. Mathematical Surveys and Monographs, Vol. 135. American Mathematical Society, Providence, RI (2007)"), Theorem 3.16\] the closed set \\overline{C\_{g\_{\\infty (0)}}(p\_\\infty , r')} \\subset {\\mathcal {C}}\_\\infty  is compact for every r' < r. \\square\
\
## 9 Ancient Ricci Flows Part I\
\
In this section we prove some properties of ancient Ricci flows g(t) \\in {\\mathcal {I}}, -\\infty < t \\le 0, that are _non-collapsed at all scales_. This yields important geometric information on the blow-up limits of singular Ricci flows, which we exploit and refine in later chapters. The main goal is to prove the following theorem:\
\
### Theorem 9.1\
\
Let \\kappa >0 and (M\_k, g(t)), k \\ge 2, t \\in (-\\infty ,0\], be an ancient Ricci flow, which satisfies the following properties:\
\
1. (i)\
\\kappa -non-collapsed at all scales;\
\
2. (ii)\
g(t) \\in {\\mathcal {I}} for t \\in (-\\infty ,0\].\
\
\
Then if k = 2 the following inequalities hold:\
\
\\begin{aligned} T\_1&= a\_s + 2Q^2 - 2 \\ge 0, \\\ T\_2&= Q y -x \\ge 0 , \\\ T\_3&= a\_s - Q b\_s - Q^2 + 1 \\ge 0. \\end{aligned}\
\
If k > 2 we only have T\_1 \\ge 0  and T\_3 \\ge 0. For all k \\ge 2 we have T\_1(p,t) = 0 if, and only if, k =2 and p \\in S\_o^2.\
\
Furthermore we show\
\
### Theorem 9.2\
\
Let \\kappa >0 and (M\_2,g(t)), t \\in (-\\infty ,0\], be an ancient Ricci flow, which satisfies the following properties:\
\
1. (i)\
\\kappa -non-collapsed at all scales;\
\
2. (ii)\
g(t) \\in {\\mathcal {I}} for t \\in (-\\infty , 0\];\
\
3. (iii)\
Kähler with respect to J\_1, or equivalently y=0 everywhere.\
\
\
Then (M\_2,g(t)) is stationary and homothetic to the Eguchi–Hanson space.\
\
**Proof strategy:** In both of these theorems we are given an ancient Ricci flow ( _M_, _g_( _t_)), t \\le 0, and want to show that a scale invariant quantity _T_ satisfies\
\
\\begin{aligned} T \\ge 0\\quad \\, \\text { on } \\, M \\times (-\\infty , 0\]. \\end{aligned}\
\
We prove such statements by a contradiction/compactness argument. First we assume that\
\
\\begin{aligned} \\iota :=\\inf \_{M\_k \\times (-\\infty ,0\]} T < 0 \\end{aligned}\
\
and take a sequence of points (p\_i, t\_i) in spacetime such that\
\
\\begin{aligned} T(p\_i, t\_i) \\rightarrow \\iota \\,\\quad \\text { as } \\, i \\rightarrow \\infty . \\end{aligned}\
\
Then we consider the rescaled Ricci flows\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big ( t\_i + b^2(p\_i, t\_i) t\\big ), \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
where \\Delta t > 0 is chosen such that the conditions of Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) are met. Then (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i) subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\Delta t, 0\]. By construction,\
\
\\begin{aligned} T(p\_\\infty , 0) = \\inf \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} T = \\iota < 0. \\end{aligned}\
\
However, if the evolution equation of _T_ precludes the possibility of a negative infimum being attained, we have arrived at a contradiction and proven the desired result.\
\
**Proof of main theorems of this section:** Before proving Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) we need to state a technical lemma in preparation:\
\
### Lemma 9.3\
\
Let (M\_k, g(t)), k \\in {\\mathbb {N}}, t \\le 0, be an ancient Ricci flow satisfying the conditions of Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99). Then for every \\epsilon > 0 there exists a \\delta > 0 such that whenever at a point ( _p_, _t_) in spacetime one of the following inequalities holds:\
\
1. (i)\
T\_1(p, t) \\le - \\epsilon  and k \\ge 2;\
\
2. (ii)\
T\_2(p, t) \\le -\\epsilon  and k \\le 2;\
\
3. (iii)\
T\_3(p, t) \\le - \\epsilon  and k \\in {\\mathbb {N}};\
\
4. (iv)\
\|x(p, t)\| \\ge \\epsilon  and k = 2,\
\
\
then s(p, t) \\ge \\delta b(p,t).\
\
### Proof\
\
Recall that by Corollary [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar68) there exists a C\_1 > 0 such that \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2} on M\_k \\times (-\\infty , 0\]. We first prove (i). We fix \\epsilon >0 and argue by contradiction. Assume there exists a sequence of points (p\_i, t\_i) in spacetime such that\
\
\\begin{aligned} T\_1(p\_i, t\_i) \\le - \\epsilon \\end{aligned}\
\
and\
\
\\begin{aligned} \\frac{s(p\_i,t\_i)}{b(p\_i, t\_i)} \\rightarrow 0. \\end{aligned}\
\
(9.1)\
\
\
Define the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g\\big (t\_i + b^{2}(p\_i, t\_i)t\\big ), \\,\\quad t \\in \[-\\Delta t, 0\]. \\end{aligned}\
\
For sufficiently small \\Delta t > 0 the conditions of Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) are satisfied and hence ( C\_{g\_i(0)}({\\small p\_i,\\frac{1}{2}}), g\_i(t), p\_i) subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ). By ( [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ70)) one sees that p\_\\infty  lies on the non-principal orbit S^2\_o of {\\mathcal {C}}\_\\infty . By construction we have T\_1(p\_\\infty , 0) \\le - \\epsilon  as T\_1 is a scale invariant quantity. This however contradicts the fact that T\_1 = a\_s + 2\\big (Q^2 -1\\big ) = k - 2 \\ge 0 on S^2\_o.\
\
Note that T\_2 = 2 - k, T\_3 = k + 1 and x = k - 2 on S^2\_o. Therefore by the same argument applied to T\_2, T\_3 and _x_ the desired result holds true. \\square\
\
Next we prove Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99).\
\
### Proof of Theorem 9.1\
\
Recall that by Corollary [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar68) there exists a C\_1 > 0 such that \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2} on M\_k \\times (-\\infty , 0\]. We first show that T\_1 \\ge 0 in M\_k \\times (-\\infty , 0\]. We argue by contradiction. Assume that\
\
\\begin{aligned} \\iota := \\inf \_{M\_k\\times (-\\infty , 0\]} T\_1 < 0. \\end{aligned}\
\
As g(t) \\in {\\mathcal {I}} we know that \\iota > - \\infty . Take a sequence of points (p\_i, t\_i) in spacetime such that\
\
\\begin{aligned} T\_1(p\_i, t\_i) \\rightarrow \\iota \\,\\quad \\text { as } \\, i \\rightarrow \\infty . \\end{aligned}\
\
From Lemma [9.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar101) it follows that for sufficiently large _i_\
\
\\begin{aligned} s(p\_i, t\_i) \\ge \\delta b(p\_i,t\_i) \\end{aligned}\
\
(9.2)\
\
\
for some \\delta > 0. Define the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i, t\_i)} g\\big (t\_i + b^2(p\_i, t\_i)t\\big ),\\quad t \\in \[-\\Delta t, 0\]. \\end{aligned}\
\
For sufficiently small \\Delta t > 0 the conditions of Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) are satisfied and hence (C\_{g\_i(0)}(p\_i,\\frac{1}{2}), g\_i(t), p\_i) subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\Delta t, 0\], on which by construction\
\
\\begin{aligned} b(p\_{\\infty },0) = 1, \\end{aligned}\
\
and\
\
\\begin{aligned} T\_1(p\_{\\infty },0) = \\inf \_{{\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]} T\_1 = \\iota < 0, \\end{aligned}\
\
(9.3)\
\
\
as T\_1 is a scale invariant quantity. Since T\_s(p\_\\infty , 0) = 0, we see from the evolution Eq. ( [5.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ46)) of T\_1 that\
\
\\begin{aligned} \\partial \_t T\_1 \\big \|\_{(p\_\\infty , 0)}&= L\[T\_1\] + \\frac{1}{b^2} \\left\[ - 4\\big (1+Q^2\\big )y^2 + 8Q\\big (1-2Q^2 \\big )y + 16Q^2\\big (1-Q^2\\big )\\right\] \\\&\\quad + \\frac{2 y T\_1}{b^2} \\big ( 2Q- y\\big ) \\\&\\ge (T\_1)\_{ss} + \\frac{4Q^2}{b^2}\\big (1- Q^2\\big ) + \\frac{2 y T\_1}{b^2} \\big ( 2Q- y\\big ), \\end{aligned}\
\
where we bounded the zeroth order term from below as in the proof of Lemma [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar44). Hence\
\
\\begin{aligned} \\partial \_t T\_1 \\big \|\_{(p\_{\\infty },0)} > 0 \\end{aligned}\
\
unless\
\
\\begin{aligned} \\text {Case a)}: \\quad Q(p\_{\\infty },0) = 1 \\text { and } y(p\_{\\infty },0) = 0, \\end{aligned}\
\
or\
\
\\begin{aligned} \\text {Case b)}: \\quad Q(p\_{\\infty },0) = 0 \\text { and } y(p\_{\\infty },0) = 0. \\end{aligned}\
\
However by ( [9.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ72)) we have\
\
\\begin{aligned} \\partial \_t T\_1 \\big \|\_{(p\_{\\infty },0)} \\le 0, \\end{aligned}\
\
showing that either Case a) or Case b) must hold. We now show that both of these cases are impossible, thereby arriving at a contradiction. First note that by ( [9.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ71)) we know that p\_\\infty  does not lie on the non-principal orbit S^2\_o. Therefore the strong maximum principle applied to the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ shows that in Case a) Q= 0 everywhere on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. This, however, contradicts the non-collapsedness of {\\mathcal {C}}\_\\infty  and therefore Case a) cannot occur. In Case b) the same argument shows that Q=1 everywhere on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. Then applying the strong maximum principle to the evolution equation ( [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ43)) of _Qy_, which simplifies when Q = 1, shows that y =0 everywhere on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. This, however, implies that T\_1 = 1 > 0 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\] contradicting our assumption that \\iota < 0.\
\
It remains to be shown that T\_1(p,t) = 0 if, and only if, k=2 and _p_ lies on the non-principal orbit S^2\_o. We argue by contradiction. Assume there exists a point ( _p_, _t_) in spacetime such that p \\notin S^2\_o and\
\
\\begin{aligned} T\_1(p, t) = 0. \\end{aligned}\
\
Then arguing as above, we see that either Case a) or Case b) must hold true, both of which lead to the same contradiction.\
\
By the same method we may prove that T\_2 \\ge 0 and T\_3 \\ge 0 on M\_k \\times (-\\infty , 0\]. Note that the evolution equations ( [5.13](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ48)) and ( [5.14](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ49)) show that T\_2 and T\_3 cannot attain a negative infimum, leading to the desired contradiction. \\square\
\
Next we prove Theorem [9.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar100).\
\
### Proof of Theorem 9.2\
\
Recall that by Corollary [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar68) there exists a C\_1 > 0 such that \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2} on M\_2 \\times (-\\infty , 0\]. Also recall Lemma [4.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar27), which states that (M\_2, g(t)), t \\in (-\\infty , 0\], is homothetic to the Eguchi–Hanson space if, and only if,\
\
\\begin{aligned} x = y = 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\]. \\end{aligned}\
\
Therefore it suffices to show that x = 0. We follow the proof strategy of Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) and argue by contradiction. Assume\
\
\\begin{aligned} \\iota :=\\inf \_{M\_2\\times (\\infty , 0\]} x < 0 \\end{aligned}\
\
and take a sequence of points (p\_i, t\_i) in spacetime such that\
\
\\begin{aligned} x(p\_i, t\_i) \\rightarrow \\iota . \\end{aligned}\
\
Note that \\iota > -\\infty  as g(t) \\in {\\mathcal {I}} for t \\in (-\\infty , 0\]. From Lemma [9.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar101) it follows that\
\
\\begin{aligned} s(p\_i, t\_i) \\ge \\delta b(o,t\_i) \\end{aligned}\
\
(9.4)\
\
\
for some \\delta > 0. Define the rescaled metrics\
\
\\begin{aligned} g\_i = \\frac{1}{b^2(p\_i, t\_i)} g\\big (t\_i + b^2(p\_i, t\_i)t \\big ), \\quad t \\in \[-\\Delta t, 0\], \\end{aligned}\
\
where \\Delta t > 0 is chosen such that the conditions of Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) are satisfied. Then (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i) subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\Delta t, 0\], on which by construction\
\
\\begin{aligned} x(p\_{\\infty },0) = \\iota < 0, \\end{aligned}\
\
since _x_ is a scale-invariant quantity. Furthermore, we see by ( [9.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ73)) that p\_\\infty  does not lie on the non-principal orbit S^2\_o. The evolution equation ( [5.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ42)) for _x_ in the Kähler case y=0 simplifies to\
\
\\begin{aligned} \\partial \_t x = L\[x\] - \\frac{4Q^2}{b^2} x, \\end{aligned}\
\
which implies that\
\
\\begin{aligned} \\partial \_t x \\big \|\_{(p\_{\\infty }, 0)} = x\_{ss} - \\frac{4Q^2}{b^2} x > 0 \\end{aligned}\
\
unless Q(p\_\\infty ,0) = 0. This, however, cannot happen, as otherwise the strong maximum principle applied to the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ would imply that Q = 0 on {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. Hence we have arrived at a contradiction and conclude\
\
\\begin{aligned} x \\ge 0 \\,\\quad \\text { on } M\_2 \\times (-\\infty , 0\]. \\end{aligned}\
\
By the same argument one shows that\
\
\\begin{aligned} x \\le 0 \\,\\quad \\text { on } M\_2 \\times (-\\infty , 0\], \\end{aligned}\
\
as well, which concludes the proof. \\square\
\
## 10 Eguchi–Hanson and a Family of Type II Singularities\
\
In this section we show that Ricci flow solutions (M\_k, g(t)), k \\ge 2, starting from a large class of initial metrics encounter a Type II singularity in finite time at the origin. In the case k=2 we show that the Eguchi–Hanson metric can occur as a blow-up limit. Below we state the precise result:\
\
### Theorem 10.1\
\
(Type II singularities)   Let (M\_k, g(t)), k \\ge 2, be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) with\
\
\\begin{aligned} \\sup \_{p \\in M\_k} b(p,0) < \\infty . \\end{aligned}\
\
(10.1)\
\
\
Then _g_( _t_) encounters a Type II curvature singularity in finite time T\_\\textrm{sing}>0 and\
\
\\begin{aligned} \\sup \_{0 \\le t < T\_\\textrm{sing}} \\left( T\_\\textrm{sing} - t\\right) b^{-2}(o,t) = \\infty . \\end{aligned}\
\
Furthermore, there exists a sequence of times t\_i \\rightarrow T\_\\textrm{sing} such that the following holds: Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(o,t\_i)} g\\big ( t\_i + b^2(o,t\_i) t \\big ), \\quad t \\in \\big \[-b^{-2}(o, t\_i) t\_i, b^{-2}(o, t\_i)\\left( T\_\\textrm{sing} - t\_i\\right) \\big ). \\end{aligned}\
\
Then (M\_k, g\_i(t), o) subsequentially converges, in the pointed Cheeger–Gromov sense, to an eternal Ricci flow (M\_k, g\_\\infty (t), o), t \\in (-\\infty , \\infty ). When k=2 the metric g\_\\infty (t) is stationary and homothetic to the Eguchi–Hanson metric.\
\
In this paper we do not study the detailed geometry of the singularity models of the Type II singularities arising in the k \\ge 3 case, however, as stated in Conjecture [2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar9) in the introduction, the author believes that these singularities are modeled on the non-collapsed steady Ricci solitons found in \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)")\]. The author, in collaboration with Jon Wilkening, has carried out numerical simulations supporting this conjecture. A paper summarizing the results is in preparation \[ [2](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR2 "Appleton, A., Wilkening, J.: Computation of                                                                               $$U(2)$$                                                               U                       (                       2                       )                                                         -invariant Ricci flow singularities, In preparation")\].\
\
**Outline of proof:** Here we sketch the proof of Theorem [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar105). First we show in Lemma [10.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar109) that the condition ( [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ74)) forces a Ricci flow solution (M\_k, g(t)), k \\ge 2, to develop a singularity in finite time T\_\\textrm{sing}>0 at the origin. Then we take a sequence of times t'\_i \\rightarrow T\_\\textrm{sing} and define the rescaled metrics\
\
\\begin{aligned} g'\_i(t) = \\frac{1}{b^2(o,t'\_i)} g\\big ( t'\_i + b^2(o,t'\_i) t \\big ). \\end{aligned}\
\
These metrics subsequentially converge to a singularity model (M\_k, g'\_\\infty (t)), -\\infty < t \\le 0 — an ancient solution of the Ricci flow. Now recall the dichotomy between Type I and Type II singularities and that every Type I singularity is modeled on a shrinking Ricci soliton \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)")\]. Therefore we can prove that the singularity is of Type II by showing that (M\_k, g'\_\\infty (t)) is not a shrinking Ricci soliton. For this we apply Theorem  [6.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar52), which excludes shrinking solitons whenever (i) \\sup \|b\_s\| < \\infty , (ii) T\_1>0 for s >0 and (iii) Q \\le 1 hold. By definition, every metric in {\\mathcal {I}} satisfies Conditions (i) and (iii). As these Conditions are scale-invariant, they pass to the blow-up limit (M\_k, g'\_\\infty (t)). From Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) it follows that Condition (iii) holds true as well, allowing us to conclude that (M\_k, g'\_\\infty (t)) is not a shrinking soliton and that the singularity is of Type II. By the work of Hamilton we can then choose a sequence of times t\_i \\rightarrow T\_\\textrm{sing}, possibly different from the sequence t'\_i, such that the corresponding blow-ups around the origin converge to an eternal Ricci flow (M\_k, g\_\\infty (t)), -\\infty< t < \\infty .\
\
In the k=2 case we show that (M\_2, g\_\\infty (t)) is stationary under Ricci flow and homothetic to the Eguchi–Hanson space. What makes k=2 special is that the second term of the right hand side of\
\
\\begin{aligned} \\partial \_t b(o,t) = 2 \\left( y\_s + \\frac{k-2}{b} \\right) \\end{aligned}\
\
is zero and therefore\
\
\\begin{aligned} \\partial \_t b(o,t) = 2y\_s(o,t) \\le 0, \\end{aligned}\
\
(10.2)\
\
\
as y\\le 0 with equality at S^2\_o for metrics in {\\mathcal {I}}. It turns out that for the specific choice of t\_i \\rightarrow T\_\\textrm{sing} from Hamilton’s trick we have that on (M\_2, g\_\\infty (t)) at S^2\_o at time 0 we have\
\
\\begin{aligned} \\partial \_t b(o,t) = 2y\_s(o,t) = 0. \\end{aligned}\
\
An application of L’Hôpital’s Rule shows that on S^2\_o we have\
\
\\begin{aligned} \\frac{y}{Q} = \\frac{y\_s}{k}. \\end{aligned}\
\
Therefore we can apply the strong maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17), Case 2, to the evolution equation ( [A.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ110)) of \\frac{y}{Q} to show that y = 0 everywhere. From Theorem [9.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar100) it then follows that (M\_2, g\_\\infty (t)) is homothetic to the Eguchi–Hanson space.\
\
### Remark 10.2\
\
A priori it may be possible that other sequences of times give rise to blow-up limits around _o_ that are not homothetic to the Eguchi–Hanson space. However in Sect. [11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec22) we show that the Eguchi–Hanson space is in fact the unique blow-up limit.\
\
**Recap of some properties of singular Ricci flow solutions:** Before proving Theorem [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar105) we summarize some properties of curvature blow-up rates of Ricci flows encountering singularities and their respective singularity models. For this let ( _M_, _g_( _t_)), t \\in \[0,T) be a Ricci flow encountering a singularity at time _T_. Let\
\
\\begin{aligned} K\_\\textrm{max}(t) := \\sup \_{M} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}. \\end{aligned}\
\
By Shi’s result \[ [32](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR32 "Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. 30(1), 223–301 (1989)")\] on the short time existence of Ricci flow we have\
\
\\begin{aligned} \\limsup \_{t \\nearrow T} K\_\\textrm{max}(t) = \\infty . \\end{aligned}\
\
In fact one can show with help of the evolution equation of \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}^2 that\
\
\\begin{aligned} \\sup \_{M} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\ge \\frac{1}{8}\\frac{1}{T-t}. \\end{aligned}\
\
(10.3)\
\
\
Hamilton \[ [22](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR22 "Hamilton, R.S.: The formation of singularities in the Ricci flow. In: Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), pp. 7–136. Int. Press, Cambridge, MA (1995)")\] introduced the notion of Type I and Type II Ricci flows, which are defined by the rate at which the curvature blows up as t \\nearrow T. In particular, (M\_2, g(t)) is of Type I if there exists a C>0 such that for t \\in \[0, T)\
\
\\begin{aligned} K\_\\textrm{max}(t) \\le \\frac{C}{T-t}. \\end{aligned}\
\
In the case that such a constant C>0 does not exist, that is\
\
\\begin{aligned} \\sup \_{t \\in \[0,T)} (T-t) K\_\\textrm{max}(t) = \\infty , \\end{aligned}\
\
we say the singularity is of Type II.\
\
By the work of Naber \[ [29](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR29 "Naber, A.: Noncompact shrinking four solitons with nonnegative curvature. J. Reine Angew. Math. 645, 125–153 (2010)")\] and Enders, Müller and Topping \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)")\] every Type I singularity model is a non-flat Ricci shrinking soliton. Hamilton showed how for Type II singularities one can extract a blow-up sequence converging to an eternal Ricci flow \[ [22](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR22 "Hamilton, R.S.: The formation of singularities in the Ricci flow. In: Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), pp. 7–136. Int. Press, Cambridge, MA (1995)"),  Theorem 16.4\]. However it remains to be understood whether or not all Type II singularity models are steady solitons. So far all known examples are.\
\
Below we recap the main result of \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)")\]: First note the following definition:\
\
### Definition 10.3\
\
(see \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)"),  Definition 1.2\]).   A spacetime sequence (p\_i, t\_i) with p\_i \\in M and t\_i \\nearrow T in a Ricci flow is called an **essential blow-up sequence** if there exists a constant c>0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t\_i)}\|\_{g(t\_i)}(p\_i) \\ge \\frac{c}{T-t}. \\end{aligned}\
\
A point p \\in M in a Type I Ricci flow is called a (general) **Type I singular point** if there exists an essential blow-up sequence with p\_i \\rightarrow p on _M_.\
\
Now we state the main result of \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)")\], asserting that Type I singularities are modeled on shrinking Ricci solitons.\
\
### Theorem 10.4\
\
(see \[ [15](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR15 "Enders, J., Müller, R., Topping, P.M.: On type-I singularities in Ricci flow. Commun. Anal. Geom. 19(5), 905–922 (2011)"),  Theorem 1.4\])   Let ( _M_, _g_( _t_)) be a Type I Ricci flow on \[0, _T_) and suppose _p_ is a Type I singular point as in Definition [10.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar107). Then for every sequence \\lambda \_j \\rightarrow \\infty , the rescaled Ricci flows (M, g\_j(t), p) defined on \[\\lambda \_j T, 0) by\
\
\\begin{aligned} g\_j (t) := \\lambda \_j g\\left( T + \\frac{t}{\\lambda \_j} \\right) \\end{aligned}\
\
subconverge to a non-flat gradient shrinking soliton.\
\
We use Theorem [10.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar108) to exclude Type I singularities for Ricci flows satisfying the assumptions of Theorem [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar105).\
\
**Proof of the main theorem:** First we show that a singularity must occur in finite time:\
\
### Lemma 10.5\
\
The maximal extension of a Ricci flow (M\_k, g(t)), k \\ge 1, starting from an initial metric g(0) \\in {\\mathcal {I}} with\
\
\\begin{aligned} \\sup \_{p \\in M\_k} b(p,0) < \\infty , \\end{aligned}\
\
encounters a singularity at the S^2\_o in finite time T\_\\textrm{sing}>0.\
\
### Proof\
\
By Shi’s short time existence of Ricci flow \[ [32](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR32 "Shi, W.-X.: Deforming the metric on complete Riemannian manifolds. J. Differ. Geom. 30(1), 223–301 (1989)")\] we have T\_\\textrm{sing} > 0. From the evolution equation ( [2.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ18)) of _b_ under Ricci flow it follows that\
\
\\begin{aligned} \\partial \_t b^2 \\le \\Delta \_{g(t)} b^2 - 4, \\end{aligned}\
\
where we used expression ( [2.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ10)) of the Laplacian. By the maximum principle (see for instance \[ [10](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR10 "Chow, B., et al.: The Ricci Flow: Techniques and Applications: Part II: Analytic Aspects. Mathematical Surveys and Monographs, Vol. 144. American Mathematical Society, Providence, RI (2008)"), Theorem 12.14\]) we see that there exists a T < \\infty  such that\
\
\\begin{aligned} \\inf \_{p\\in M\_k} b^2(p,t) \\rightarrow 0 \\quad \\text { as } t \\rightarrow T. \\end{aligned}\
\
As b\_s \\ge 0 we conclude that\
\
\\begin{aligned} \\lim \_{t\\rightarrow T} b(o,t) = 0. \\end{aligned}\
\
From Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) it follows that the curvature at S^2\_o blows up as t \\rightarrow T. Hence T = T\_\\textrm{sing}. \\square\
\
Below we prove Theorem [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar105).\
\
### Proof of Theorem 10.1\
\
By Lemma [10.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar109) the Ricci flow becomes singular in finite time T\_\\textrm{sing}> \\delta > 0 and b(o,t) \\rightarrow 0 as t \\nearrow T\_\\textrm{sing}. Recall that by Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) there exist a C\_1 > 0 such that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2}\\quad \\, \\text { on } \\, M\_k \\times \[0, T\_\\textrm{sing}). \\end{aligned}\
\
Moreover, by Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) there exist constants \\kappa , \\rho > 0 such that _g_( _t_) is \\kappa -non-collapsed at scales less or equal to \\rho .\
\
Now take a sequence of times t'\_i \\nearrow T\_\\textrm{sing} such that\
\
1. (1)\
b(o, t'\_i) \\rightarrow 0 as i \\rightarrow \\infty ;\
\
2. (2)\
b(o, t) \\ge b(o,t'\_i) for t \\le t'\_i.\
\
\
### Claim 1\
\
The sequence of points (o, t'\_i) in spacetime is an essential blow-up sequence.\
\
### Proof of Claim 1\
\
We argue by contradiction. Assume, after passing to a subsequence, that\
\
\\begin{aligned} (T\_\\textrm{sing}-t'\_i) \|\\textrm{Rm}\_{g(t'\_i)}\|\_{g(t'\_i)}(o) \\rightarrow 0\\, \\quad \\text {as~} i \\rightarrow \\infty . \\end{aligned}\
\
Then by Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) and the fact that b\_s \\ge 0 for metrics in {\\mathcal {I}} we have\
\
\\begin{aligned} b^2(p,t) \\ge b^2(o,t) = \\frac{4}{R\_{2323}} \\ge \\frac{4}{\|\\textrm{Rm}\_{g(t'\_i)}\|\_{g(t'\_i)}(o)}, \\end{aligned}\
\
where we used the expression for the curvature component R\_{2323} derived in Sect. [2.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec11). This shows that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t'\_i)}\|\_{g(t'\_i)}(p) \\le \\frac{C\_1}{b^2(p,t'\_i)} \\le \\frac{C\_1}{4} \|\\textrm{Rm}\_{g(t'\_i)}\|\_{g(t'\_i)}(o)\\quad \\text { for } \\, p \\in M\_k. \\end{aligned}\
\
Therefore\
\
\\begin{aligned} \\lim \_{i \\rightarrow \\infty } \\left( T\_\\textrm{sing} - t'\_i\\right) \\sup \_{p\\in M\_k}\|\\textrm{Rm}\_{g(t'\_i)}\|\_{g(t'\_i)}(p) = 0, \\end{aligned}\
\
which contradicts ( [10.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ76)). This proves the claim. \\square\
\
Define the rescaled metrics\
\
\\begin{aligned} g'\_i(t) = \\frac{1}{b^2(o,t'\_i)} g\\big ( t'\_i + b^2(o,t'\_i) t \\big ), \\quad t \\in \\big \[- b^{-2}(o,t'\_i)t'\_i, 0\\big \]. \\end{aligned}\
\
By Property (2) above and the fact that b\_s\\ge 0 for metrics in {\\mathcal {I}} it follows that\
\
\\begin{aligned} \|\\textrm{Rm}\_{g'\_i(t)}\|\_{g'\_i(t)} \\le C\_1 \\quad \\, \\text { on } \\, M\_k \\times \\big \[- b^{-2}(o,t'\_i)t'\_i, 0\\big \]. \\end{aligned}\
\
Note also that the rescaled metrics g'\_i(t) are \\kappa -non-collapsed at scales tending to infinity. Corollary [8.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar83) then implies that (M\_k, g'\_i(t),o) subsequentially converges, in the Cheeger–Gromov sense, to an ancient Ricci flow (M\_\\infty , g'\_{\\infty }(t),o), t \\in (-\\infty ,0\], where M\_\\infty \\cong M\_k. By Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) we have\
\
\\begin{aligned} T\_1(p,t) > 0 \\, \\quad \\text { on } \\, M\_\\infty \\setminus S^2\_o \\times (-\\infty , 0\] \\end{aligned}\
\
on the blow-up limit g'\_\\infty (t). Theorem [6.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar52) shows that g'\_\\infty (t) cannot be a shrinking soliton, which by the contrapositive of Theorem [10.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar108) proves that the singularity is of Type II. Therefore\
\
\\begin{aligned} \\sup \_{M \\times \[0,T\_\\textrm{sing})} \\left( T\_\\textrm{sing}- t\\right) \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} = \\infty \\end{aligned}\
\
from which we see that\
\
\\begin{aligned} \\sup \_{t \\in \[0, T\_\\textrm{sing})} \\left( T\_\\textrm{sing} - t\\right) b^{-2}(o,t) = \\infty . \\end{aligned}\
\
Now we mimic the proof of \[ [22](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR22 "Hamilton, R.S.: The formation of singularities in the Ricci flow. In: Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), pp. 7–136. Int. Press, Cambridge, MA (1995)"),  Theorem 16.4, Type II(a)\] to construct an eternal blow-up limit. Pick a sequence of times T\_i < T\_\\textrm{sing} satisfying\
\
\\begin{aligned} \\left( T\_\\textrm{sing} - T\_i\\right) b^{-2}(o,t) \\rightarrow \\infty \\end{aligned}\
\
as i \\rightarrow \\infty . Then we can choose t\_i < T\_i such that\
\
\\begin{aligned} \\left( T\_i - t\_i\\right) b^{-2}(o,t\_i) = \\sup \_{t \\le T\_i} \\left( T\_i - t\\right) b^{-2}(o,t) \\end{aligned}\
\
(10.4)\
\
\
as the latter goes to zero as t \\rightarrow T\_i. Consider the rescaled Ricci flow solutions\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(o,t\_i)} g\\big ( t\_i + b^2(o,t\_i) t \\big ), \\end{aligned}\
\
which exist for -A\_i \\le t \\le B\_i with\
\
\\begin{aligned} A\_i&= t\_i b^{-2}(o,t\_i) \\rightarrow \\infty ,\\\ B\_i&= \\left( T\_i- t\_i\\right) b^{-2}(o, t\_i) \\rightarrow \\infty . \\end{aligned}\
\
If we write a\_i, b\_i for the warping functions of the rescaled metric g\_i(t) we obtain from Eq. ( [10.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ77)) the following inequality\
\
\\begin{aligned} \\left( B\_i - t \\right) b\_i^{-2} (o,t) \\le B\_i. \\end{aligned}\
\
Note that here _t_ is the time variable of the rescaled Ricci flow g\_i(t). Therefore for any fixed _t_ we have\
\
\\begin{aligned} b\_i^{-2} (o,t) \\le \\frac{B\_i}{B\_i -t} \\rightarrow 1 \\quad \\text {as } i \\rightarrow \\infty \\end{aligned}\
\
(10.5)\
\
\
and\
\
\\begin{aligned} b^{-2}\_i(o,0) = 1. \\end{aligned}\
\
(10.6)\
\
\
From this, the fact that b\_s \\ge 0 and the curvature bound of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67), we see that on bounded time intervals the curvatures of g\_i(t) eventually become bounded by 2C\_1. In addition to this the metrics g\_i(t) are \\kappa -non-collapsed at larger and larger scales. Therefore Corollary [8.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar83) implies that (M\_2, g\_i(t), o) subsequentially converges to an eternal Ricci flow (M\_2, g\_\\infty (t), o). Furthermore ( [10.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ78)) and ( [10.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ79)) show that\
\
\\begin{aligned} b\_{\\infty }(o,t) \\ge 1\\quad \\, \\text { for } \\, t \\in (-\\infty , \\infty ) \\end{aligned}\
\
(10.7)\
\
\
and\
\
\\begin{aligned} b\_{\\infty } (o,0) = 1, \\end{aligned}\
\
(10.8)\
\
\
where we write a\_{\\infty } and b\_{\\infty } for the warping functions of the metric g\_{\\infty }(t). Notice that ( [10.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ80)) and ( [10.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ81)) imply that at time 0 on S^2\_o we have\
\
\\begin{aligned} \\partial \_t b\_{\\infty } = 2 \\left( (y\_{\\infty })\_s + \\frac{k-2}{b\_{\\infty }}\\right) = 0, \\end{aligned}\
\
(10.9)\
\
\
where y\_\\infty = (b\_\\infty )\_s - \\frac{a\_\\infty }{b\_\\infty } corresponds to the Kähler quantity _y_ on the g\_\\infty  background.\
\
Now it only remains to be shown that in the k=2 case g\_\\infty (t) is stationary and homothetic to the Eguchi–Hanson metric. In the following we drop the \\infty  subscript and let _a_, _b_, _Q_, _y_ be with respect to the metric g\_\\infty (t). Note that Eq. ( [10.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ82)) and an application of L’Hôpital’s Rule show that at time 0 on S^2\_o we have\
\
\\begin{aligned} y\_s = \\frac{y}{Q} = 0. \\end{aligned}\
\
The evolution equation for \\frac{y}{Q} derived in Appendix A is\
\
\\begin{aligned} \\partial \_t \\left( \\frac{y}{Q}\\right) = \\left( \\frac{y}{Q}\\right) \_{ss} + \\left( 3 \\frac{a\_s}{a} - 2 \\frac{b\_s}{b} \\right) \\left( \\frac{y}{Q}\\right) \_s + \\frac{2}{b^2}\\frac{y}{Q}\\left( 2 + \\frac{y}{Q}\\right) \\left( Q b\_s - 2 a\_s \\right) .\\nonumber \\\ \\end{aligned}\
\
(10.10)\
\
\
Because g\_\\infty (t) \\in {\\mathcal {I}} is of bounded curvature we see that\
\
\\begin{aligned} \\frac{1}{b^2} \\left( 2 + \\frac{y}{Q}\\right) \\left( Q b\_s - 2a\_s \\right) = \\frac{1}{b^2}\\left( -\\frac{2 a\_s b\_s}{Q}-2 a\_s+Q b\_s+b\_s^2 \\right) \\end{aligned}\
\
is bounded. Note that we applied Lemma [3.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar18) to show that \\frac{1}{b^2} is bounded. Therefore we may apply the strong maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17), Case 2, to deduce that\
\
\\begin{aligned} \\frac{y}{Q} = 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\], \\end{aligned}\
\
yielding that g\_\\infty (t) is Kähler in the k=2 case. By Theorem [9.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar100) we then deduce that g\_\\infty (t) is homothetic to the Eguchi–Hanson metric, which proves the desired result. \\square\
\
## 11 Ancient Ricci Flows Part II: k=2 Case\
\
In this section we prove that every non-collapsed ancient Ricci flow in the class of metrics {\\mathcal {I}} is isometric to the Eguchi–Hanson metric:\
\
### Theorem 11.1\
\
(Unique ancient flow)   Let \\kappa > 0 and \\left( M\_2,g(t)\\right) , t \\in (-\\infty ,0\], be an ancient Ricci flow that is \\kappa -non-collapsed at all scales and g(t) \\in {\\mathcal {I}}, t \\in (-\\infty ,0\] (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)). Then _g_( _t_) is stationary and homothetic to the Eguchi–Hanson metric.\
\
An immediate consequence of this theorem is that for _every_ sequence of times t\_i \\rightarrow T\_\\textrm{sing} in Theorem [10.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar105), the rescaled Ricci flows\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(o,t\_i)}g\\big (t + b^2(o,t\_i)t\_i \\big ), \\quad t \\in \\big \[- b^{-2}(o,t\_i) t\_i, 0\\big \], \\end{aligned}\
\
subsequentially converge to the Eguchi–Hanson space. In other words, the Eguchi–Hanson space is the _unique_ limit of blow-ups around the origin. With a little extra work one can show the slightly more general result, asserting that blow-up limits centered at points close to, but not necessarily on the tip of M\_2, subsequentially converge to the Eguchi–Hanson space:\
\
### Corollary 11.2\
\
Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) that develops a singularity at time T\_\\textrm{sing}. Let (p\_i, t\_i) be a sequence of points in spacetime with t\_i \\rightarrow T\_\\textrm{sing} satisfying\
\
\\begin{aligned} \\sup \_i \\frac{b(p\_i,t\_i)}{b(o,t\_i)} < \\infty \\end{aligned}\
\
and consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i,t\_i) t\\big ), \\quad t \\in \\big \[- b^{-2}(p\_i,t\_i) t\_i, 0\\big \]. \\end{aligned}\
\
Then (M\_2, g\_i(t), p\_i) subsequentially converges, in the Cheeger–Gromov sense, to a blow-up limit (M\_2, g\_\\infty (t), p\_\\infty ), t \\le 0, which is homothetic to the Eguchi–Hanson space.\
\
We defer the proof of Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) to the end of Sect. [11.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec27).\
\
### 11.1  Outline of Proof\
\
Here we outline the proof of Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114). Below we take (M\_2, g(t)), t \\in (-\\infty ,0\], to be a non-collapsed ancient Ricci flow with g(t) \\in {\\mathcal {I}}, t \\in (-\\infty ,0\]. We construct a continuously varying one-parameter family of functions\
\
\\begin{aligned} f\_{\\theta }: \[0,1\] \\rightarrow \[0,1\], \\quad \\theta \\in (0,1\], \\end{aligned}\
\
satisfying the following five requirements:\
\
1. (1)\
For every \\theta \\in (0,1\] the condition\
\
\
\
\\begin{aligned} Z\_{\\theta }(\\xi , t) := \\frac{x}{Q^2} + f\_{\\theta }(Q) = \\frac{a\_s + Q^2 - 2}{Q^2} + f\_{\\theta } (Q) \\ge 0 \\end{aligned}\
\
\
\
    is preserved on the (M\_2, g(t)) background.\
\
2. (2)\
For every 0\\le Q < 1\
\
\
\
\\begin{aligned} f\_{\\theta } (Q) \\rightarrow 0 \\quad \\, \\text { as } \\, \\theta \\rightarrow 0. \\end{aligned}\
\
3. (3)\
For every \\theta \\in (0,1\] there exists a Q\_{\\theta } \\in \[0,1) such that\
\
\
\
\\begin{aligned} f\_{\\theta }(Q)< 1\\quad \\text { for } \\, Q < Q\_{\\theta }, \\end{aligned}\
\
\
\
    and\
\
\
\
\\begin{aligned} f\_{\\theta }(Q) = 1 \\quad \\text { for } \\, Q \\ge Q\_{\\theta }. \\end{aligned}\
\
\
\
    Furthermore Q\_{\\theta } depends continuously on \\theta .\
\
4. (4)\
For \\theta = 1\
\
\
\
\\begin{aligned} f\_1(Q) = 1 \\end{aligned}\
\
\
\
    everywhere.\
\
5. (5)\
For every \\theta \\in (0,1\] the function f\_{\\theta } is extendable to a smooth even function around 0.\
\
\
### Remark 11.3\
\
We briefly remark on some of the properties of f\_{\\theta }:\
\
- In the expression for Z\_{\\theta } of Requirement (1) we take _x_, _Q_ and a\_s to be functions of spacetime. For brevity we do not express the dependence explicitly.\
\
- The term \\frac{x}{Q^2} can be extended smoothly to the non-principal orbit S^2\_o, as x = x\_s = 0 at s = 0. Therefore Z\_{\\theta } is well-defined on M\_2.\
\
- When \\theta = 1 we already know that\
\
\
\
\\begin{aligned} Z\_1 = \\frac{x + Q^2}{Q^2} \\ge 0 \\end{aligned}\
\
\
\
in M\_2 \\times (-\\infty , 0\], as from Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) it follows that T\_1 = Q^2 Z\_1\\ge 0 on M\_2 \\times (-\\infty , 0\].\
\
- At any point ( _p_, _t_) in spacetime such that Q(p,t) \\ge Q\_{\\theta } we have\
\
\
\
\\begin{aligned} Z\_{\\theta } (p, t) = Z\_1(p, t) \\ge 0. \\end{aligned}\
\
- The family f\_{\\theta }(Q), \\theta \\in (0,1\], we construct below is smooth everywhere apart from when Q = Q\_{\\theta }. It will become clear later that this does not pose a problem.\
\
\
In Sect. [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec24) we show that at points ( _p_, _t_) in spacetime at which Q(p, t) \\ne Q\_{\\theta }, or equivalently at points where _f_ is smooth, the evolution equation of the corresponding Z\_{\\theta } can locally be written as\
\
\\begin{aligned} \\partial \_t Z\_{\\theta }&= \[Z\_{\\theta }\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2\\frac{b\_s}{b}\\right) \[Z\_{\\theta }\]\_s + \\frac{1}{b^2}\\big ( W\_{\\theta } + Z\_{\\theta } {\\tilde{D}}\_{\\theta } \\big ), \\end{aligned}\
\
where W\_{\\theta } and {\\tilde{D}}\_{\\theta } are bounded and scale-invariant expressions involving b\_s, _Q_, f\_{\\theta }(Q), f'\_{\\theta }(Q) and f''\_{\\theta }(Q). Again, all quantities in the evolution equation of Z\_{\\theta } should be interpreted as functions of spacetime.\
\
In Sect. [11.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec25) we construct a family of functions f\_{\\theta }, \\theta \\in (0,1\], by solving an initial value problem for a second order non-linear ordinary differential equation. Subsequently we show that the family satisfies Requirements (1)–(5) listed above. In particular, we show in Sect. [11.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec26) that for the constructed family—on a non-collapsed ancient Ricci flow background—the following property holds true: For all points ( _p_, _t_) in spacetime such that Q(p, t) < Q\_{\\theta }, we have W\_{\\theta }(p, t) \\ge 0, \\theta \\in (0,1\]. This fact, in conjunction with the fourth bullet point of Remark [11.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar116), essentially shows that for each \\theta \\in (0,1\] the inequality Z\_{\\theta } \\ge 0 is preserved on the _g_( _t_) background.\
\
Once we have shown that our family f\_{\\theta }, \\theta \\in (0,1\], satisfies Requirements (1)–(5), we will use a blow-up argument in conjunction with the strong maximum principle to show that if for some \\theta \_0 \\in (0,1\] the inequality Z\_{\\theta } \\ge 0 holds for all \\theta \\in \[\\theta \_0 , 1\], then there must exist an \\theta \_1 \\in (0, \\theta \_0) such that the inequality also holds for all \\theta \\in \[\\theta \_1, 1\]. This shows that in fact for all \\theta \\in (0,1\]\
\
\\begin{aligned} Z\_{\\theta } \\ge 0 \\;\\quad \\text { on } M\_2 \\times (-\\infty , 0\]. \\end{aligned}\
\
By Property (2) of f\_{\\theta } we deduce that at all points ( _p_, _t_) in spacetime such that Q(p,t) < 1 we have\
\
\\begin{aligned} x(p,t) \\ge 0. \\end{aligned}\
\
Note that by the strong maximum principle applied to the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_ it follows that Q < 1 and hence x \\le 0 everywhere. Now recall Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) which states that\
\
\\begin{aligned} x \\le Qy \\le 0 \\, \\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\]. \\end{aligned}\
\
Therefore\
\
\\begin{aligned} x = y = 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\] \\end{aligned}\
\
and we conclude that the metric _g_( _t_) is homothetic to the Eguchi–Hanson metric by Lemma [4.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar27).\
\
### 11.2 Evolution Equations\
\
The main difficulty in carrying out the proof is to find a family of functions f\_{\\theta }, \\theta \\in (0,1\], for which Requirement (1) is satisfied. Our strategy is to first derive the evolution equation of Z\_{\\theta } for a general f\_{\\theta } and then reduce the problem to solving a second order ordinary differential equation in f\_\\theta . For this, first note that the evolution equation of f\_{\\theta }(Q) away from the non-principal orbit S^2\_o can be written as\
\
\\begin{aligned} \\partial \_t f\_{\\theta }(Q) = \[f\_{\\theta }(Q)\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2\\frac{b\_s}{b}\\right) \[f\_{\\theta }(Q)\]\_s + \\frac{1}{b^2} C\_{f}, \\end{aligned}\
\
where\
\
\\begin{aligned} C\_f&= \\left( 8 a\_s b\_s - 3 \\frac{a\_s^2}{Q} - 5 Q b\_s^2 + 4 Q \\big (1 - Q^2\\big ) \\right) f' - \\left( a\_s - Q b\_s \\right) ^2f''. \\end{aligned}\
\
(11.1)\
\
\
The computation is carried out in Appendix A.\
\
### Remark 11.4\
\
Some remarks on the evolution equation of f\_{\\theta }(Q):\
\
- We often omit the dependence of our quantities on spacetime, i.e., by f\_{\\theta }(Q) we mean f\_{\\theta }(Q(p,t)).\
\
- For brevity we often omit the dependence of _f_ on \\theta  and _Q_, as in the expression for C\_f above. For instance, we write f' for f'\_{\\theta }(Q) and f'' for f''\_{\\theta }(Q).\
\
- Note that by Lemma [2.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar14) the quantity Q = \\frac{a}{b} as a function of _s_ can be extended to an odd function around the origin. Therefore as long as f\_{\\theta }: \[0,1\] \\rightarrow \[0,1\] is extendable to an even function around the origin, the term \\frac{f'}{Q} and hence C\_f can be smoothly extended to all of M\_2.\
\
\
From Eq. ( [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ84)) and the evolution equations ( [5.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ38)) and ( [5.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ40)) of a\_s and Q^2, respectively, we see that the evolution equation of Z\_{\\theta } can be written as\
\
\\begin{aligned} \\partial \_t Z\_{\\theta } = \[Z\_{\\theta }\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2\\frac{b\_s}{b}\\right) \[Z\_{\\theta }\]\_s + \\frac{1}{b^2}\\big ( C\_{Z,0} + C\_{Z,1} Z\_{\\theta } + C\_{Z,2} Z^2\_{\\theta } \\big ),\\nonumber \\\ \\end{aligned}\
\
(11.2)\
\
\
after having eliminated any occurring a\_s by substituting\
\
\\begin{aligned} a\_s = Q^2 Z\_{\\theta }- f Q^2 - Q^2 + 2. \\end{aligned}\
\
A computation carried out in Appendix A shows that\
\
\\begin{aligned} C\_{Z,0}&= A\_0 +\\left\[ \\frac{b\_s}{Q}\\right\] A\_1 + \\left\[ \\frac{b\_s}{Q}\\right\] ^2 A\_2, \\end{aligned}\
\
where\
\
\\begin{aligned}&\\displaystyle A\_0 = - Q^4 f^2 f''-2 Q^4 f f''-Q^4 f''+4 Q^2 f f''+4 Q^2 f''-4 f''-3 Q^3 f^2 f' \\\&\\qquad \\!\\quad \\displaystyle -6 Q^3 f f'-7 Q^3 f'+12 Q f f'+16 Q f'-\\frac{12 f'}{Q}-2 Q^2 f+8 f-2 Q^2-4, \\\&\\displaystyle A\_1 = -2 Q^4 f f''-2 Q^4 f''+4 Q^2 f''-8 Q^3 f f'-8 Q^3 f' \\\&\\qquad \\!\\quad \\displaystyle +16 Q f'-4 Q^2 f^2-8 Q^2 f+8 f+4 Q^2+8, \\\&\\displaystyle A\_2 = - Q^4f''-5 Q^3 f'-2 Q^2 f-2 Q^2-4. \\\ \\end{aligned}\
\
Similarly, we compute the expressions for C\_{Z,1} and C\_{Z,2} in Appendix A, however their exact forms are not important for our analysis. It is only important to note that when _f_ is extendable to an even function around 0, the quantities C\_{Z,i}, A\_i, i = 0, 1, 2, are scale-invariant, bounded, and can be extended smoothly to S^2\_o.\
\
For reasons that will become clear below, we rewrite Eq. ( [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ85)) in the form\
\
\\begin{aligned} \\partial \_t Z\_{\\theta }&= \[Z\_{\\theta }\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2\\frac{b\_s}{b}\\right) \[Z\_{\\theta }\]\_s + \\frac{1}{b^2}\\left( W\_{\\theta } + Z\_{\\theta } D\_{\\theta } \\right) , \\end{aligned}\
\
(11.3)\
\
\
where\
\
\\begin{aligned} W\_{\\theta } = A\_0 +\\left\[ \\frac{b\_s}{Q} - Z\_{\\theta } \\right\] A\_1 + \\left\[ \\frac{b\_s}{Q} - Z\_{\\theta } \\right\] ^2 A\_2 \\end{aligned}\
\
(11.4)\
\
\
and\
\
\\begin{aligned} D\_{\\theta } = C\_{Z,1} + Z C\_{Z,2} + A\_1 - A\_2\\left( Z\_{\\theta } - 2 \\frac{b\_s}{Q}\\right) . \\end{aligned}\
\
Sometimes it will be useful to regard W\_{\\theta } as a quadratic polynomial. Therefore we define\
\
\\begin{aligned} w\_{\\theta }(z) =A\_0 + A\_1 z + A\_2 z^2. \\end{aligned}\
\
Then\
\
\\begin{aligned} W\_{\\theta } = w\_{\\theta }\\left( \\frac{b\_s}{Q} - Z\_{\\theta }\\right) . \\end{aligned}\
\
In the proof of Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114) we also need the evolution equation of\
\
\\begin{aligned} Z\_1 = \\frac{x}{Q^2}+1, \\end{aligned}\
\
which can be written as\
\
\\begin{aligned} \\partial \_t Z\_1 = \[Z\_1\]\_{ss} + \\left( 3 \\frac{a\_s}{a} - 2\\frac{b\_s}{b}\\right) \[Z\_1\]\_s + \\frac{1}{b^2} \\big (C\_{Z\_1,0} + C\_{Z\_1,1} Z\_1 + C\_{Z\_1,2} Z^2\_1 \\big ),\\nonumber \\\ \\end{aligned}\
\
(11.5)\
\
\
where\
\
\\begin{aligned} C\_{Z\_1,0} = \\frac{1}{Q^2}\\Big ( - 4\\big (1+Q^2\\big )y^2 + 8Q\\big (1-2Q^2 \\big )y + 16Q^2\\big (1-Q^2\\big ) \\Big ) \\end{aligned}\
\
and C\_{Z\_1,1}, C\_{Z\_1,2} are bounded scale-invariant functions of a\_s, b\_s and _Q_. The derivation of this evolution equation is carried out in Appendix A. Note the following lemma:\
\
### Lemma 11.5\
\
Let (M\_2, g(t)), t \\in (-\\infty , 0\], be an ancient Ricci flow as in Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114). Then\
\
\\begin{aligned} Z\_1 \\ge 0 \\end{aligned}\
\
and\
\
\\begin{aligned} C\_{Z\_1,0} \\ge 4\\big (1-Q^2\\big ) \\end{aligned}\
\
everywhere in M\_2 \\times (-\\infty , 0\].\
\
### Proof\
\
By Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) we know that Z\_1 = \\frac{T\_1}{Q^2} \\ge 0 in M\_2 \\times (-\\infty , 0\]. Moreover, notice the similarity of C\_{Z\_1,0} to the zeroth order term in the evolution equation ( [5.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ46)) of T\_1. Therefore we see by the proof of Lemma [5.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar44) that C\_{Z\_1,0} \\ge 4(1-Q^2) for metrics in {\\mathcal {I}}. \\square\
\
In the proof of Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114) we deform the inequality Z\_1 \\ge 0 along a path of conserved inequalities Z\_{\\theta } \\ge 0, \\theta \\in (0,1\]. Thus Z\_1 \\ge 0 is the starting point for successively constraining the ancient Ricci flow towards the Eguchi–Hanson space. Below we construct the f\_{\\theta } leading to the conserved inequalities Z\_{\\theta } \\ge 0.

### 11.3 Construction of f\_{\\theta }, \\theta \\in (0,1\]

The goal of the following discussion is to find a family of functions f\_{\\theta }: \[0,1\] \\rightarrow \[0,1\], \\theta \\in (0,1\], such that

\\begin{aligned} W\_{\\theta } \\ge 0 \\end{aligned}

is non-negative on ancient Ricci flows satisfying Z\_{\\theta } \\ge 0. For this we consider solutions to the ordinary differential equation

\\begin{aligned} 0&= -4 \\big (1-Q^2\\big )^2 f'' - 4 \\big (1-Q^2\\big ) \\big (Q^2 f-5 Q^2+3\\big ) \\frac{f'}{Q} \\nonumber \\\&\\quad \\,\\, + 2f\\big ( f^2 Q^2+3 f Q^2-6 f-6 Q^2+8 \\big ), \\end{aligned}

(11.6)


which is equivalent to

\\begin{aligned} w\_{\\theta } \\left( - f + 1\\right) = 0. \\end{aligned}

(11.7)


Note that we are now regarding _Q_ as an independent variable and not as a function of spacetime. Before we explain how we arrived at this differential equation, we list some of its properties below. For clarity of exposition we defer their proofs to Sect. [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec28).

### Lemma 11.6

For every f\_0 \\in {\\mathbb {R}} the ordinary differential Eq. ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) possesses an even analytic solution around the origin with initial condition

\\begin{aligned} f(0) = f\_0. \\end{aligned}

Furthermore, _f_ varies smoothly with f\_0.

### Lemma 11.7

Let f: \[0,Q\_\\textrm{max}) \\rightarrow {\\mathbb {R}}, Q\_\\textrm{max} \\le 1, be the maximal solution to the ordinary differential equation ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) with initial condition 0< f(0) < 1. Then on any interval (0, Q\_\*), Q\_\*\\le Q\_\\textrm{max}, on which 0 < f(Q) \\le 1 we have f'(Q) > 0.\
\
### Lemma 11.8\
\
Let \\theta \\in (0,1\] and f\_{\\theta }: 0 \\in I \\rightarrow {\\mathbb {R}} be the maximal solution to the ordinary differential Eq. ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) with f\_{\\theta }(0) = \\theta . Then there exists a Q\_{\\theta } \\in \[0,1) such that\
\
\\begin{aligned} f\_{\\theta }(Q\_{\\theta }) = 1 \\end{aligned}\
\
and\
\
\\begin{aligned} f\_{\\theta }(Q)< 1 \\quad \\, \\text {for }\\, 0 \\le Q < Q\_{\\theta }. \\end{aligned}\
\
Furthermore,\
\
1. (1)\
Q\_{\\theta } varies continuously with \\theta \\in (0,1\];

2. (2)
Q\_{\\theta } \\rightarrow 1 \\text { as } \\theta \\rightarrow 0;

3. (3)
Q\_1 = 0.


For each \\theta \\in (0,1\] let

\\begin{aligned} \\phi \_{\\theta }: \[0, Q\_{\\theta }\] \\rightarrow \[\\theta , 1\] \\end{aligned}

be the solution to the differential Eq. ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) with initial condition

\\begin{aligned} \\phi \_{\\theta }(0) = \\theta \\end{aligned}

and define f\_{\\theta }, \\theta \\in (0,1\], as follows:

\\begin{aligned} f\_{\\theta }(Q) = {\\left\\{ \\begin{array}{ll} \\phi \_{\\theta }(Q) &{}\\text {for }\\, 0 \\le Q \\le Q\_{\\theta }, \\\ 1 &{}\\text {for }\\, Q\_{\\theta } < Q \\le 1. \\end{array}\\right. } \\end{aligned}

(11.8)


Note that f\_{\\theta } is continuous but in general not smooth at Q = Q\_{\\theta }. This is not a problem, as will become clear later. In summary, we have:

### Proposition 11.9

There exists a unique continuously varying family of continuous functions f\_{\\theta }: \[0,1\] \\rightarrow \[0,1\] and numbers Q\_{\\theta } \\in \[0,1) for \\theta \\in (0,1\] satisfying the following properties:

- f\_{\\theta }(Q) solves ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) or equivalently w\_{\\theta }(-f\_{\\theta }(Q) + 1) = 0 for 0 \\le Q \\le Q\_{\\theta }.

- f\_{\\theta }(0) = \\theta .

- f\_{\\theta }(Q) < 1 for Q < Q\_{\\theta } and f\_{\\theta }(Q) = 1 for Q \\ge Q\_{\\theta }.

- f\_{\\theta }(Q) is strictly increasing in _Q_ when 0< Q < Q\_{\\theta }.

- f\_{\\theta }(Q) is extendable to an even function around the origin.

- Q\_{\\theta } varies continuously with \\theta .

- Q\_{\\theta } \\rightarrow 1 \\text { as } \\theta \\rightarrow 0 and Q\_1 = 0.

- For every Q \\in \[0,1) we have f\_{\\theta }(Q) \\rightarrow 0 as \\theta \\rightarrow 0.\
\
\
### 11.4 Non-negativity of W\_{\\theta }\
\
For the choice of f\_{\\theta }, \\theta \\in (0,1\], defined above the following proposition holds true:

### Proposition 11.10

Let \\theta \\in (0,1\] and f\_{\\theta } be as defined in ( [11.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ91)). Assume (M\_2, g(t)), t \\in (-\\infty ,0\], is a non-collapsed ancient Ricci flow with g(t) \\in {\\mathcal {I}} for t\\in (-\\infty ,0\] and Z\_{\\theta } \\ge 0 everywhere. Suppose at the point ( _p_, _t_) in spacetime Q(p, t) < Q\_{\\theta }. Then

\\begin{aligned} W\_{\\theta }(p, t) \\ge 0 \\end{aligned}

with equality if and only if

\\begin{aligned} T\_2(p,t) = 0. \\end{aligned}

We prove this proposition in multiple steps. First note

### Lemma 11.11

Let f\_{\\theta }, \\theta \\in (0,1\], be the family of functions as defined in Proposition [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar123). Then

\\begin{aligned} A\_2 = - Q^4f''-5 Q^3 f'-2 Q^2 f-2 Q^2-4 < 0 \\end{aligned}

(11.9)


for 0 \\le Q < Q\_{\\theta }. Thus w\_{\\theta }(z) = A\_2 z^2 + A\_1 z + A\_0 is concave in _z_ whenever 0 \\le Q < Q\_{\\theta }.

The proof of this technical lemma can be found in Sect. [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec28). Furthermore we have

### Lemma 11.12

Let \\theta \\in (0,1\]. Let (M\_2, g(t)), t \\in (-\\infty , 0\], be a non-collapsed ancient Ricci flow with g(t) \\in {\\mathcal {I}} for  t \\in (-\\infty , 0\] and Z\_{\\theta } \\ge 0 everywhere. Then

\\begin{aligned} - f\_{\\theta }(Q) + 1 \\le \\frac{b\_s}{Q} - Z\_{\\theta } \\le \\min \\left( 1, -f\_{\\theta }(Q) + \\frac{3}{Q^2} - 2 \\right) \\end{aligned}

and

\\begin{aligned} \\min \\left( 1 , -f\_{\\theta }(Q) + \\frac{3}{Q^2} - 2 \\right) = {\\left\\{ \\begin{array}{ll} 1 &{}{ \\textit{if} } f\_{\\theta }(Q) \\le 3 \\frac{1-Q^2}{Q^2}, \\\ -f + \\frac{3}{Q^2} - 2 &{} {\\textit{otherwise}}. \\end{array}\\right. } \\end{aligned}

(11.10)


### Proof

By Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99) and since g(t) \\in {\\mathcal {I}} we know that

\\begin{aligned}&y =b\_s - Q \\le 0, \\\&T\_2 = Qy - x = -a\_s + Q b\_s + 2\\big (1-Q^2\\big ) \\ge 0, \\\&T\_3 =a\_s - Qb\_s + 1 - Q^2 \\ge 0 \\end{aligned}

on M\_2 \\times (-\\infty , 0\]. Therefore y \\le 0 implies

\\begin{aligned} \\frac{b\_s}{Q} - Z\_{\\theta } \\le 1 - Z\_{\\theta } \\end{aligned}

and T\_2 \\ge 0 implies

\\begin{aligned} \\frac{b\_s}{Q} - Z\_{\\theta } = \\frac{Qb\_s - a\_s -Q^2 +2}{Q^2} - f\_{\\theta }(Q) \\ge 1 - f\_{\\theta }(Q) \\end{aligned}

and finally T\_3 \\ge 0 implies

\\begin{aligned} \\frac{b\_s}{Q} - Z\_{\\theta } = \\frac{Qb\_s - a\_s -Q^2 +2}{Q^2} - f\_{\\theta }(Q) \\le - f\_{\\theta }(Q) + \\frac{3}{Q^2} - 2. \\end{aligned}

Now applying the assumption Z\_{\\theta } \\ge 0  proves the desired result. \\square

Recalling that by definition

\\begin{aligned} W\_{\\theta } = w\_{\\theta }\\left( \\frac{b\_s}{Q} - Z\_{\\theta }\\right) , \\end{aligned}

the above Lemma [11.12](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar126) and concavity of w\_{\\theta }(z) show that to prove Proposition [11.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar124) it suffices to check that for \\theta \\in (0,1\] and 0 \\le Q < Q\_{\\theta } we have

\\begin{aligned} \\alpha&:= w\_{\\theta }\\left( - f\_{\\theta }(Q) + 1 \\right) \\ge 0, \\\ \\beta&:= w\_{\\theta }\\left( 1 \\right) \\ge 0 \\quad \\, \\text { whenever } \\, f\_{\\theta }(Q) \\le 3 \\frac{1-Q^2}{Q^2},\\\ \\gamma&:= w\_{\\theta }\\left( -f\_{\\theta }(Q) + \\frac{3}{Q^2} - 2\\right) \\ge 0 \\quad \\, \\text { whenever } \\, f\_{\\theta }(Q) \\ge 3 \\frac{1-Q^2}{Q^2}, \\end{aligned}

where f\_{\\theta } is as defined in Proposition [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar123). Note that \\gamma  is only defined for Q^2> 0. This however does not pose a problem as

\\begin{aligned} 1 \\ge f\_{\\theta }(Q) \\ge 3 \\frac{1-Q^2}{Q^2} \\end{aligned}

implies that Q^2 \\ge \\frac{3}{4}> 0. Recall that by the properties of f\_{\\theta }(Q) summarized in Proposition [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar123) we have

\\begin{aligned} w\_{\\theta }\\left( - f\_{\\theta }(Q) + 1 \\right) = 0 \\quad \\, \\text { for } \\, 0 \\le Q < Q\_{\\theta }, \\end{aligned}

and therefore only need to investigate the sign of \\beta  and \\gamma  in their respective regimes. This explains why we chose to define f\_{\\theta }(Q) via the ordinary differential equation ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)). In the following technical lemma, the proof of which we defer to Sect. [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Sec28), we show that for our choice of f\_{\\theta } the functions \\beta  and \\gamma  are in fact positive in their respective regimes:

### Lemma 11.13

Fix \\theta \\in (0,1\] and let f\_{\\theta }(Q) as defined in Proposition [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar123). Then for 0 \\le Q < Q\_{\\theta } we have

\\begin{aligned} \\beta > 0\\quad \\textrm{whenever } \\, f\_{\\theta }(Q) \\le 3 \\frac{1-Q^2}{Q^2}, \\end{aligned}

and

\\begin{aligned} \\gamma > 0\\quad \\textrm{whenever } \\, f\_{\\theta }(Q) \\ge 3 \\frac{1-Q^2}{Q^2}. \\end{aligned}

Now we can prove Proposition [11.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar124).

### Proof of Proposition 11.10

By Lemmas [11.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar125) and [11.13](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar128) we know that W\_{\\theta } \\ge 0 whenever 0 \\le Q < Q\_{\\theta }, with equality if and only if

\\begin{aligned} \\frac{b\_s}{Q} - Z\_{\\theta } = 1 - f\_{\\theta }(Q), \\end{aligned}

which by the definition of Z\_{\\theta } is equivalent to T\_2 = 0. \\square

### Remark 11.14

The proof of Proposition [11.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar124) essentially implies that for every \\theta \\in (0,1\] the inequality Z\_{\\theta } \\ge 0 is preserved on Ricci flow backgrounds in {\\mathcal {I}} satisfying T\_1 \\ge 0, T\_2 \\ge 0 and T\_3 \\ge 0. We do not prove this here, as our proof of Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114) does not rely on this fact.

### 11.5 Proof of Main Theorem

Next, we prove that the Eguchi–Hanson space is the unique ancient Ricci flow in the class {\\mathcal {I}}.

### Proof of Theorem 11.1

Recall that by Corollary [7.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar68) there exists a C\_1 > 0 such that

\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^2}. \\end{aligned}

Moreover, by Theorem [9.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar99)

\\begin{aligned} T\_1, T\_2, T\_3\\ge 0 \\quad \\, \\text { on } \\, M\_2\\times (\\infty , 0\] \\end{aligned}

and by Lemma [11.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar118)

\\begin{aligned} Z\_1 \\ge 0 \\quad \\text { on } \\, M\_2\\times (\\infty , 0\]. \\end{aligned}

Hence we may assume that there exists a \\theta \_0 \\in (0,1\] such that for all \\theta \\in \[\\theta \_0, 1\]

\\begin{aligned} Z\_{\\theta } = \\frac{x}{Q^2} + f\_{\\theta }(Q) \\ge 0 \\,\\quad \\text { on } \\, M\_2\\times (\\infty , 0\]. \\end{aligned}

### Claim 1

For every 0 \\le Q\_\*< 1 we have

\\begin{aligned} \\inf \\big \\{ Z\_{\\theta \_0}(p,t) \\, \\big \| \\, (p,t) \\in M\_2 \\times (\\infty , 0\] \\text { such that } Q(p,t) \\le Q\_\*\\big \\} > 0. \\end{aligned}

### Proof of Claim 1

We argue by contradiction. Assume there exists a sequence of points (p\_i, t\_i) in spacetime such that

\\begin{aligned} Q(p\_i, t\_i) \\le Q\_\*\\end{aligned}

and

\\begin{aligned} Z\_{\\theta \_0}(p\_i, t\_i) \\rightarrow 0 \\,\\quad \\text { as } \\, i \\rightarrow \\infty . \\end{aligned}

Consider the rescaled metrics

\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big ( t\_i + b^2(p\_i,t\_i) t\\big ), \\quad t\\in \[-\\Delta t, 0\]. \\end{aligned}

For sufficiently small \\Delta t > 0 the conditions of Proposition [8.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar85) are satisfied and therefore (C\_{g\_i(0)}(p\_i, \\frac{1}{2}), g\_i(t), p\_i), t\\in \[-\\Delta t, 0\] subsequentially converges to a Ricci flow ({\\mathcal {C}}\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in \[-\\Delta t, 0\]. Write

\\begin{aligned} \\Omega = {\\mathcal {C}}\_\\infty \\times \[-\\Delta t, 0\]. \\end{aligned}

By construction,

\\begin{aligned} Z\_{\\theta \_0}(p\_\\infty , 0) = \\inf \_{\\Omega } Z\_{\\theta \_0} = 0. \\end{aligned}

Now we need to distinguish two cases:

**Case 1:** Q(p\_\\infty ,0) < Q\_{\\theta \_0}.

Then there exists an r\\in (0,\\frac{1}{2}) and \\Delta t' \\in (0, \\Delta t) such that on the parabolic set

\\begin{aligned} \\Omega ' = C\_{g\_\\infty (0)}(p\_\\infty , r) \\times \[-\\Delta t', 0\] \\subset \\Omega \\end{aligned}

we have Q < Q\_{\\theta \_0}. By the strong maximum principle of Theorem [3.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar17) applied to the evolution equation ( [11.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ86)) of Z\_{\\theta \_0} we have

\\begin{aligned} Z\_{\\theta \_0} = 0 \\,\\quad \\text { on } \\, \\Omega ' \\end{aligned}

and therefore

\\begin{aligned} (Z\_{\\theta \_0})\_s = (Z\_{\\theta \_0})\_{ss} = 0 \\,\\quad \\text { on } \\, \\Omega '. \\end{aligned}

By the evolution equation ( [11.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ86)) of Z\_{\\theta \_0} we see that

\\begin{aligned} 0 = \\partial \_t Z\_{\\theta \_0} = {\\mathcal {Q}}\_{\\theta \_0} \\,\\quad \\text {in } \\, \\Omega ', \\end{aligned}

which by Proposition [11.10](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar124) implies

\\begin{aligned} T\_2 = Qy- x = 0 \\,\\quad \\text { in } \\, \\Omega '. \\end{aligned}

However, the evolution equation ( [5.13](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ48)) of T\_2 then implies

\\begin{aligned} y = 0 \\,\\quad \\text { on } \\, \\Omega ', \\end{aligned}

and thus also

\\begin{aligned} x = 0 \\,\\quad \\text { on }\\, \\Omega '. \\end{aligned}

That in turn implies

\\begin{aligned} Z\_{\\theta \_0}(p\_\\infty ,0) = f(Q(p\_\\infty ,0)) \\ge \\theta \_0 > 0, \\end{aligned}

which is a contradiction.

**Case 2:** Q(p\_\\infty ,0) \\ge Q\_{\\theta \_0}.

Recall that at points ( _p_, _t_) in spacetime satisfying Q(p,t) \\ge Q\_{\\theta \_0} we have Z\_{\\theta \_0}(p,t) = Z\_1(p,t). In this case we therefore have

\\begin{aligned} Z\_1(p\_\\infty ,0) = Z\_{\\theta \_0}(p\_\\infty , 0) = 0. \\end{aligned}

By the strong maximum principle applied to the evolution equation ( [11.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ88)) of Z\_1 and Lemma [11.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar118) we deduce

\\begin{aligned} Z\_1 = 0 \\,\\quad \\text { on } \\, \\Omega . \\end{aligned}

Furthermore, we see that this is only possible when

\\begin{aligned} Q = 1 \\,\\quad \\text { on } \\, \\Omega , \\end{aligned}

which contradicts

\\begin{aligned} Q(p\_\\infty ,0) \\le Q\_\*< 1. \\end{aligned}

This concludes the proof of the claim. \\square

Take Q\_\*= \\max \_{\\theta \\in \[\\frac{1}{2} \\theta \_0, \\theta \_0\]} Q\_{\\theta }. The above claim asserts that there exists a \\delta > 0 such that for all points ( _p_, _t_) in spacetime satisfying 0 \\le Q(p,t) \\le Q\_\*

\\begin{aligned} Z\_{\\theta \_0}(p,t) > \\delta . \\end{aligned}

By the continuous dependence of f\_{\\theta }(Q) on \\theta , there exists an \\epsilon >0 such that for \|\\theta - \\theta \_0\| < \\epsilon  we have \|f\_{\\theta }(Q) - f\_{\\theta \_0}(Q)\| < \\frac{\\delta }{2} for all Q \\in \[0,1\]. By choosing \\epsilon < \\frac{1}{2} \\theta \_0 we see that for all \\theta \\in \[\\theta \_0 - \\epsilon , \\theta \_0 \] and all points ( _p_, _t_) in spacetime satisfying 0 \\le Q(p,t) \\le Q\_\* we have

\\begin{aligned} Z\_{\\theta }(p,t) > \\frac{\\delta }{2}. \\end{aligned}

Since for spacetime points at which Q > Q\_\*

\\begin{aligned} Z\_{\\theta } = Z\_{\\theta \_0} = Z\_1 \\ge 0, \\end{aligned}

we deduce that for \\theta \\in \[\\theta \_0 - \\epsilon , 1\] the inequality

\\begin{aligned} Z\_{\\theta } \\ge 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\] \\end{aligned}

holds true. Now consider the set

\\begin{aligned} {\\mathcal {E}} = \\left\\{ \\theta \\in (0,1\] \\, \\big \| \\, Z\_{\\theta '} \\ge 0 \\text { for } \\theta \\le \\theta ' \\le 1 \\right\\} \\!. \\end{aligned}

The above argument shows that \\inf {\\mathcal {E}} = 0 and hence for all \\theta \\in (0,1\]

\\begin{aligned} Z\_{\\theta } \\ge 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\]. \\end{aligned}