---
retention_scope: session
part: 5
total_parts: 7
---

[Part 5/7 of: Eguchi–Hanson Singularities in U(2)-Invariant Ricci Flow]

Note that by the strong maximum principle applied to the evolution equation ( [5.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ36)) of _Q_

\\begin{aligned} Q < 1 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\], \\end{aligned}

as otherwise Q=1 everywhere, which is not true. As Z\_{\\theta } = \\frac{x}{Q^2} + f\_{\\theta }(Q) and by Proposition [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar123) for every 0 \\le Q < 1 we have f\_{\\theta }(Q) \\rightarrow 0 as \\theta \\rightarrow 0 it follows that

\\begin{aligned} x \\ge 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\]. \\end{aligned}

However, as

\\begin{aligned} T\_2 = Qy - x \\ge 0 \\,\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\] \\end{aligned}

and y \\le 0 by the assumption that g(t) \\in {\\mathcal {I}} it follows that

\\begin{aligned} x = y = 0\\quad \\text { on } \\, M\_2 \\times (-\\infty , 0\]. \\end{aligned}

By Lemma [4.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar27) we conclude that (M\_2, g(t)), t\\in (-\\infty , 0\], is stationary and homothetic to the Eguchi–Hanson space. \\square

Now we prove Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115).

### Proof of Corollary 11.2

By Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67) and the fact that b\_s \\le 0 for metrics in {\\mathcal {I}} there exists a C\_1 > 0 such that

\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)}(p) \\le \\frac{C\_1}{b^2(p,t)} \\le \\frac{C\_1}{b^2(o,t)}. \\end{aligned}

This shows that

\\begin{aligned} b(o,t) \\rightarrow 0\\quad \\text { as } t \\rightarrow T\_\\textrm{sing}. \\end{aligned}

As by assumption

\\begin{aligned} C :=\\sup \\frac{b(p\_i, t\_i)}{b(o,t\_i)} < \\infty \\end{aligned}

and y \\le 0 by the fact that g(t) \\in {\\mathcal {I}} it follows that

\\begin{aligned} \\partial \_t b(o,t) \\le 0, \\quad t \\in \[0,T\_\\textrm{sing}), \\end{aligned}\
\
by ( [10.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ75)). We deduce\
\
\\begin{aligned} b(p\_i,t\_i) \\rightarrow 0\\quad \\text { as } i \\rightarrow \\infty . \\end{aligned}\
\
Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i, t\_i)t \\big ), \\quad t\\in \\big \[- b^{-2}(p\_i,t\_i)t\_i, 0\\big \]. \\end{aligned}\
\
These satisfy the curvature bound\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_i(t)}\|\_{g\_i(t)} \\le C^2 C\_1 \\,\\quad \\text { on } \\, M\_2 \\times \\big \[- b^{-2}(p\_i,t\_i)t\_i, 0\\big \]. \\end{aligned}\
\
By Theorem [7.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar64) the rescaled metrics g\_i(t) are \\kappa -non-collapsed at larger and larger scales. Hence by Corollary [8.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar83) the Ricci flows (M\_2, g\_i(t), p\_i) subsequentially converge to a pointed ancient Ricci flow (M\_2, g\_{\\infty }(t), p\_\\infty ),  \- \\infty< t < 0, with g\_\\infty (t) \\in {\\mathcal {I}}. By Theorem [11.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar114) it follows that g\_\\infty (t) is stationary and homothetic to the Eguchi–Hanson metric. \\square\
\
### 11.6 Proof of Technical Lemmas\
\
In this subsection we collect the proofs of the technical lemmas we relied on above.\
\
### Proof of Lemma 11.6\
\
We apply \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)"), Theorem 9.2\] to prove this lemma. Define\
\
\\begin{aligned} r = Q^2. \\end{aligned}\
\
Then\
\
\\begin{aligned}&f' = 2 Q f\_r, \\\&f'' = 2 f\_r + 4 r f\_{rr}, \\end{aligned}\
\
where ' denotes the derivative with respect to _Q_ and subscript _r_ denotes the derivative with respect to _r_. Rewriting the differential Eq. ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) with respect to the independent variable _r_, we obtain\
\
\\begin{aligned} r f\_{rr} = \\frac{1}{2(1-r)} \\left( 6r - 4 - r f\\right) f\_r + \\frac{f}{8 \\;\\left( 1- r\\right) ^2 }\\big (f^2 r + 3 fr - 6f - 6r + 8 \\big ).\\nonumber \\\ \\end{aligned}\
\
(11.11)\
\
\
At r=0 the right hand side must equal zero, which can be ensured by requiring\
\
\\begin{aligned} f\_r (0) = \\frac{1}{2} f\_0 - \\frac{3}{8} f\_0^2. \\end{aligned}\
\
Now define\
\
\\begin{aligned} u\_1&= f - f\_0, \\\ u\_2&= f\_r - f\_r(0). \\end{aligned}\
\
Then ( [11.11](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ94)) can be written as a system of equations of the form\
\
\\begin{aligned} r (u\_i)\_r = P\_i(\\vec {u},r,f\_0), \\quad i = 1, 2, \\end{aligned}\
\
where\
\
\\begin{aligned} P: {\\mathbb {R}}^2 \\times (-1,1) \\times {\\mathbb {R}}&\\longrightarrow {\\mathbb {R}}^2, \\\ (\\vec {u}, r, f\_0)&\\longmapsto P(\\vec {u}, r, f\_0) \\end{aligned}\
\
is an analytic vector-valued function of several variables satisfying\
\
\\begin{aligned} P(\\vec {0}, 0, f\_0) = 0 \\end{aligned}\
\
for all f\_0 \\in (-1, 1). A computation shows that\
\
\\begin{aligned} \\frac{\\partial P}{\\partial u} \\Big \|\_{(\\vec {0},0, f\_0)} = \\begin{pmatrix} 0 &{}\\quad 0 \\\ 1- \\frac{3}{2} f\_0 &{}\\quad -2 \\end{pmatrix}. \\end{aligned}\
\
This matrix has no positive integer eigenvalues and furthermore\
\
\\begin{aligned} B = \\sup \_{\\begin{array}{c} m\\in {\\mathbb {N}}\\\ f\_0 \\in {\\mathbb {R}} \\end{array}} \\left\\Vert \\left( m I\_2 - \\frac{\\partial P}{\\partial u} \\Big \|\_{(\\vec {0},0, f\_0)}\\right) ^{-1}\\right\\Vert < \\infty , \\end{aligned}\
\
where I\_2 is the 2\\times 2 identity matrix. By \[ [1](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR1 "Appleton, A.: A family of non-collapsed steady Ricci solitons in even dimensions greater or equal to four,                    arXiv:1708.00161                                     (2017)"),  Theorem 9.2\] the desired result follows. \\square\
\
### Proof of Lemma 11.7\
\
At Q=0, we have by L’Hôpital’s Rule that\
\
\\begin{aligned} f'' = \\frac{1}{4} f \\left( 4 - 3 f \\right) > 0 \\,\\quad \\text { for }\\, 0< f(0) < \\frac{4}{3}. \\end{aligned}\
\
(11.12)\
\
\
Furthermore, at an extremum of _f_ we have\
\
\\begin{aligned} f'' = \\frac{2 f}{4\\left( 1-Q^2\\right) ^2}\\big ( f^2 Q^2+3 f Q^2-6 f-6 Q^2+8 \\big ). \\end{aligned}\
\
(11.13)\
\
\
Defining the polynomial\
\
\\begin{aligned} p\_1(f,Q^2) = f^2 Q^2+3 f Q^2-6 f-6 Q^2+8, \\end{aligned}\
\
we see that\
\
\\begin{aligned} \\partial \_{Q^2} p\_1 = f^2 + 3f - 6< 0\\,\\quad \\text { for } 0 < f \\le 1. \\end{aligned}\
\
Therefore\
\
\\begin{aligned} p\_1(f, Q) > p\_1(f, 1) = f^2 - 3f + 2 \\ge 0 \\quad \\, \\text { for } 0< f \\le 1 \\text { and } 0 \\le Q < 1. \\end{aligned}\
\
From ( [11.13](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ96)) it then follows that f'>0 for as long as 0 < f \\le 1. \\square\
\
### Proof of Lemma 11.8\
\
We argue by contradiction. Assume there does not exist such a Q\_{\\theta } < 1. Then by Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121) we have f' >0 on Q \\in (0,1) and hence\
\
\\begin{aligned} \\lim \_{Q \\rightarrow 1^-} f(Q) = l \\le 1 \\end{aligned}\
\
exists. By ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) we have\
\
\\begin{aligned} 4 \\big (1-Q^2\\big )^2 f'' =&- 4 \\big (1-Q^2\\big ) \\big (Q^2 f-5 Q^2+3\\big ) \\frac{f'}{Q} \\\&\\quad + 2f\\Big ( Q^2\\big (f^2+3 f-6\\big )+8-6 f \\Big ). \\end{aligned}\
\
For Q^2 > 1 - \\frac{\\theta }{4} and 0< f < 1 we have\
\
\\begin{aligned} Q^2 f-5 Q^2+3< 3 - 4 Q^2 < -1 + \\theta \\end{aligned}\
\
and\
\
\\begin{aligned} Q^2\\big (f^2+3 f-6\\big )+8-6 f > (2-f)(1-f), \\end{aligned}\
\
as for 0<f<1\
\
\\begin{aligned} f^2+3 f-6 < 0. \\end{aligned}\
\
Hence for  Q^2 > 1 - \\frac{\\theta }{4} and 0< f< 1 we obtain the following inequality\
\
\\begin{aligned} f''&\\ge \\alpha \\frac{f'}{1-Q} + \\beta \\frac{1-f}{(1-Q)^2}, \\end{aligned}\
\
(11.14)\
\
\
where\
\
\\begin{aligned} \\alpha&= \\frac{1-\\theta }{Q(1+Q)},\\\ \\beta&= \\frac{f\\left( 2 - f\\right) }{2 \\left( 1+Q\\right) ^2}. \\end{aligned}\
\
Furthermore we observe that\
\
\\begin{aligned} \\alpha&\\rightarrow \\frac{1}{2} \\, \\,\\,\\text { as } f,Q \\rightarrow 1, \\\ \\beta&\\rightarrow \\frac{1}{8} \\, \\,\\,\\text { as } f,Q \\rightarrow 1. \\end{aligned}\
\
If l < 1, then there would exist a Q\_\*<1 such that for Q \\ge Q\_\* we have\
\
\\begin{aligned} f'' \\ge \\frac{1}{10} \\frac{l(1-l)(2-l)}{(1-Q)^2}. \\end{aligned}\
\
Here \\frac{1}{10} can be replaced by any positive number less that \\frac{1}{8}. However, integrating this differential inequality shows that in this case _f_ would reach 1 before Q = 1, leading to a contradiction of our assumption. Therefore we may assume that l =1.\
\
Defining\
\
\\begin{aligned} g(Q) = 1 - f(Q), \\end{aligned}\
\
we obtain the differential inequality\
\
\\begin{aligned} g''(Q) \\le \\alpha \\frac{g'(Q)}{1-Q} - \\beta \\frac{g(Q)}{(1-Q)^2}. \\end{aligned}\
\
(11.15)\
\
\
By Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121) we know that g(Q) > 0 and g'(Q) < 0 on Q \\in (0,1).\
\
### Claim 1\
\
The function _g_( _Q_) reaches zero before Q = 1.\
\
### Proof of Claim 1\
\
By our assumption that l=1 we know that there exists a Q\_\*< 1 such that for Q > Q\_\*\
\
\\begin{aligned} g(Q) < \\theta . \\end{aligned}\
\
Furthermore, by choosing Q\_\*< 1 sufficiently close to 1, we may assume that for Q \\ge Q\_\*\
\
\\begin{aligned} g''(Q) \\le \\frac{3}{7} \\frac{g'(Q)}{1-Q} - \\frac{5}{49} \\frac{g(Q)}{(1-Q)^2}, \\end{aligned}\
\
(11.16)\
\
\
as  \\frac{3}{7} < \\frac{1}{2} and \\frac{5}{49} < \\frac{1}{8}. Now take the substitution\
\
\\begin{aligned} g(Q) = u\\left( r \\right) \\end{aligned}\
\
for\
\
\\begin{aligned} r = -\\ln (1- Q). \\end{aligned}\
\
Then ( [11.16](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ99)) becomes\
\
\\begin{aligned} \\frac{d^2u}{dr^2} + \\frac{4}{7} \\frac{du}{dr} + \\frac{5}{49} u \\le 0. \\end{aligned}\
\
The corresponding ordinary differential equation is of oscillatory type, which motivates the substitution\
\
\\begin{aligned} u(r) = e^{-\\frac{2}{7} r} v(r) \\end{aligned}\
\
yielding the inequality\
\
\\begin{aligned} \\frac{d^2v}{dr^2} \\le - \\frac{1}{49} v. \\end{aligned}\
\
Hence _v_ reaches 0 in finite _r_, which tracing back the substitutions, shows that _g_ must reach zero before Q = 1. \\square\
\
Now it remains to prove the assertions (1), (2) and (3). We prove (1). First fix a \\theta \\in (0,1). By Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121) we know that f'\_\\theta (Q\_{\\theta }) > 0. Now extend the solution f\_\\theta  of ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) to the interval \[0, Q\_{\\theta } + c\], c>0, such that f'\_{\\theta }(Q) > 0 on (0, Q\_{\\theta } + c\]. By the continuous dependence of f\_{\\theta }(Q) on \\theta  it follows that for every \\epsilon > 0 there exists a \\delta > 0 such that \|\\theta - \\theta '\| \\le \\delta  implies \|Q\_\\theta - Q\_{\\theta '}\| < \\epsilon . To prove the continuity of Q\_\\theta  at \\theta = 1, note that Q\_1 = 0, f\_1(0) = 1 and f'\_1=0. Then recall from the proof of Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121) that f''(0) > 0 when 0< f(0) < \\frac{4}{3}. Now applying the same argument as above yields continuity of Q\_\\theta  at \\theta = 1 and therefore proves (1).

Assertion (2) follows from the fact that for the initial condition f(0) = 0 the corresponding solution to the ODE ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) is f(Q) = 0. By the continuous dependence of _f_ on f(0) = 0 we deduce that

\\begin{aligned} Q\_{\\theta } \\rightarrow 1 \\quad \\text { as } \\theta \\rightarrow 0. \\end{aligned}

Finally, Assertion (3) follows by definition. \\square

### Proof of Lemma 11.11

First note that by Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121) we know that f,f' \\ge 0 on \[0, Q\_{\\theta }\]. Solving the ODE ( [11.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ89)) for f'', we obtain

\\begin{aligned} f''&= \\frac{1}{2 Q \\left( 1-Q^2\\right) ^2} \\big ( 2 Q^4 f f'-10 Q^4 f'-2 Q^2 f f'+16 Q^2 f'\\nonumber \\\&\\quad -6 f' + Q^3 f^3+3 Q^3 f^2-6 Q^3 f-6 Q f^2+8 Q f \\big ). \\end{aligned}

(11.17)


Substituting expression ( [11.17](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ100)) into ( [11.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ92)) yields

\\begin{aligned} A\_2&= - \\frac{1}{2 \\left( 1-Q^2\\right) ^2} \\Big ( 2 Q^3 \\big (1-Q^2\\big ) \\big ( 2 - Q^2 f \\big ) f' \\\&\\quad + f^3 Q^6+3 f^2 Q^6-6 f^2 Q^4-2 f Q^6+4 f Q^2+4 Q^6-12 Q^2+8 \\Big ). \\end{aligned}

Defining

\\begin{aligned} p\_2 (f, Q^2) = f^3 Q^6+3 f^2 Q^6-6 f^2 Q^4-2 f Q^6+4 f Q^2+4 Q^6-12 Q^2+8, \\end{aligned}

we then only need to check that

\\begin{aligned} p\_2 \\ge 0 \\,\\quad \\text { for } \\, 0 \\le f, Q \\le 1. \\end{aligned}

Defining

\\begin{aligned} {\\tilde{p}}\_2 (F, Q^2) = p\_2(f, Q^2), \\end{aligned}

for

\\begin{aligned} F = f Q^2, \\end{aligned}

we see that

\\begin{aligned} \\partial \_{Q^2} {\\tilde{p}}\_2 \\Big \|\_F = 3 F^2 - 4FQ^2 + 12 \\big ( Q^4 -1 \\big ) \\le 0 \\quad \\, \\text { for } \\, 0\\le F, Q \\le 1 \\end{aligned}

with equality only at F= 0, Q = 1. Therefore the minimum of p\_2 is attained when Q = 1, in which case we have we have

\\begin{aligned} {\\tilde{p}}\_2(F, 1) = \\left( F-2\\right) \\left( F-1\\right) F \\ge 0 \\quad \\text { for } \\, 0\\le F \\le 1. \\end{aligned}

As  0 \\le Q \\le Q\_{\\theta } < 1, we actually have p\_2(f, Q^2) > 0 on (f,Q) \\in \[0,1\] \\times \[0, Q\_\\theta \] and the result follows. \\square

### Proof of Lemma 11.13

A computation shows that

\\begin{aligned} \\beta&= -\\big (Q^2f+2 Q^2-2\\big )^2 f'' \\nonumber \\\&\\quad \\,\\, + \\big (-3 Q^4 f^2-14 Q^4 f+12 Q^2 f-20 Q^4+32 Q^2-12\\big ) \\frac{f'}{Q} \\nonumber \\\&\\quad \\,\\, -4 Q^2 f^2-12 Q^2 f+16 f \\end{aligned}

(11.18)


and

\\begin{aligned} \\gamma&= -\\big (1-Q^2\\big )^2 f'' + \\big (1- Q^2\\big )\\big (2 Q^2 f+11 Q^2-9\\big )\\frac{f'}{Q} \\nonumber \\\&\\quad \\,\\, + 2 Q^2 f^3+6 Q^2 f^2-12 f^2-6 Q^2 f+\\frac{30 f}{Q^2}-20 f-18 Q^2+\\frac{54}{Q^2}-\\frac{36}{Q^4}, \\end{aligned}

(11.19)


where we omitted the dependence of _f_ on \\theta  and _Q_ for brevity. We first show that \\beta > 0 in the region

\\begin{aligned} R\_1 = \\left\\{ (f,Q) \\, \\Big \| \\, 0 \\le Q \\le Q\_{\\theta }, 0 < f \\le \\min \\left( 1, 3 \\frac{1-Q^2}{Q^2}\\right) \\right\\} \\end{aligned}

of the _f_- _Q_-plane. Plugging the expression ( [11.17](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ100)) of f'' into the expression ( [11.18](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ101)) for \\beta , we obtain

\\begin{aligned} 2 \\big (1-Q^2 \\big )^2 \\beta&= 2 ff' Q(1 - Q^2)\\big ( Q^4 f^2+2 Q^4 f-4 Q^2 f-2 Q^4-2 Q^2+4 \\big ) \\\&\\quad + f^2 \\big ( -Q^6f^3-7 Q^6 f^2+10 Q^4 f^2-10 Q^6 f+36 Q^4 f \\\&\\quad -28 Q^2 f+4 Q^6+8 Q^4-36 Q^2+24 \\big ). \\end{aligned}

An application of L’Hôpital’s Rule shows that \\beta = 12 f^2 > 0 at Q=0 and therefore we may assume that Q>0. Recall that f,f' > 0 on (0,Q\_{\\theta }) by Lemma [11.7](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar121). Hence it suffices to show that the polynomials

\\begin{aligned} p\_3(f,Q^2) = Q^4 f^2+2 Q^4 f-4 Q^2 f-2 Q^4-2 Q^2+4 \\end{aligned}

and

\\begin{aligned} p\_4(f,Q^2)&= -Q^6f^3-7 Q^6 f^2+10 Q^4 f^2-10 Q^6 f+36 Q^4 f \\\&\\quad -28 Q^2 f+4 Q^6+8 Q^4-36 Q^2+24 \\end{aligned}

are positive on R\_1 \\cap \\{ Q > 0 \\}. A computation shows

\\begin{aligned} \\partial \_{Q^2} p\_3 = 2\\big (f^2 Q^2 - 1 \\big ) + 4f \\big (Q^2 -1 \\big ) - 4 Q^2 \\le 0 \\end{aligned}

and hence for every (f,Q) \\in R\_1 we have

\\begin{aligned} p\_3(f, Q^2) \\ge p\_3\\left( f, \\frac{3}{3 +f}\\right) = \\left( \\frac{f}{3+f}\\right) ^2 > 0. \\end{aligned}

To show that p\_4 > 0 on R\_1 is more complicated. For this we introduce the variable

\\begin{aligned} F= fQ^2 \\end{aligned}

and polynomial

\\begin{aligned} {\\tilde{p}}\_4 (F, Q^2) = p\_4( f, Q^2). \\end{aligned}

Then

\\begin{aligned} {\\tilde{p}}\_4(F, Q^2)&= 24 -28 F+10 F^2 -F^3+\\big (-7 F^2+36 F-36\\big ) Q^2 \\\&\\quad +(8-10 F) Q^4+4 Q^6, \\end{aligned}

which gives

\\begin{aligned} \\partial \_{Q^2} {\\tilde{p}}\_4 = -7 F^2 - 4 F \\big (-9 + 5 Q^2\\big ) + 4 \\big (-9 + 4 Q^2 + 3 Q^4\\big ). \\end{aligned}

As this expression is concave in _F_ one can easily check that in the region

\\begin{aligned} 0 < F \\le \\min \\left( Q^2, 3\\big (1-Q^2\\big ) \\right) ,\\quad 0 \\le Q \\le 1 \\end{aligned}

of the Q^2- _F_-plane we have

\\begin{aligned} \\partial \_{Q^2} {\\tilde{p}}\_4 \\le 0 \\end{aligned}

and thus

\\begin{aligned} {\\tilde{p}}\_4(F, Q^2) \\ge {\\tilde{p}}\_4\\left( F, \\frac{3-F}{3}\\right) = \\frac{1}{27} F \\big (2 F^2-3 F+18\\big ) > 0. \\end{aligned}

From this we conclude that p\_4 > 0 on R\_1\\cap \\{Q > 0 \\} and hence \\beta > 0 on R\_1.

We adopt the same procedure to show that \\gamma > 0 in the region

\\begin{aligned} R\_2 = \\left\\{ (f,Q) \\, \\Big \| \\, 0 \\le Q \\le Q\_{\\theta }, 3 \\frac{1-Q^2}{Q^2} \\le f \\le 1 \\right\\} . \\end{aligned}

Substituting the expression ( [11.17](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ100)) for f'' into the expression ( [11.19](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ102)) for \\gamma  we obtain

\\begin{aligned} \\gamma&= 3 \\big (1-Q^2\\big ) \\big (Q^2 f+2 Q^2-2\\big ) \\frac{f'}{Q} +\\frac{1}{Q^4} \\Bigg ( \\frac{3 f^3 Q^6}{2}+\\frac{9 f^2 Q^6}{2}-9 f^2 Q^4 \\\&\\quad -3 f Q^6-24 f Q^4+30 f Q^2-18 Q^6+54 Q^2-36\\Bigg ). \\end{aligned}

First notice that for any point (f,Q) \\in R\_2

\\begin{aligned} 3\\frac{1- Q^2}{Q^2} \\le 1 \\end{aligned}

and hence

\\begin{aligned} \\sqrt{\\frac{3}{4}} \\le Q \\le Q\_{\\theta } < 1. \\end{aligned}

Then from

\\begin{aligned} f \\ge 3 \\frac{1-Q^2}{Q^2} \\end{aligned}

it follows that

\\begin{aligned} Q^2 f + 2 Q^2 - 2 \\ge 1- Q^2 > 0\\quad \\, \\text { on } \\, R\_2. \\end{aligned}

Therefore the first term in the expression for \\gamma  is positive and we only need to prove non-negativity of the second term. For this define the polynomials

\\begin{aligned} p\_5(f, Q^2)&= \\frac{3 f^3 Q^6}{2}+\\frac{9 f^2 Q^6}{2}-9 f^2 Q^4-3 f Q^6-24 f Q^4 \\\&\\quad \\quad +30 f Q^2-18 Q^6+54 Q^2-36 \\end{aligned}

and

\\begin{aligned} \\tilde{p\_5}(F,Q^2)&= \\frac{3 F^3}{2}+\\frac{9 F^2 Q^2}{2}-9 F^2-3 F Q^4-24 F Q^2 \\\&\\quad \\quad +30 F-18 Q^6+54 Q^2-36, \\end{aligned}

where we again took F = f Q^2. Computing the partial derivatives

\\begin{aligned}&\\partial \_{Q^2} {\\tilde{p}}\_5 = \\frac{9 F^2}{2}-6 F Q^2-24 F-54 Q^4+54, \\\&\\partial \_{F} {\\tilde{p}}\_5 = \\frac{9 F^2}{2}+9 F Q^2-18 F-3 Q^4-24 Q^2+30, \\end{aligned}

we deduce that at an local extrema \\partial \_{Q^2} {\\tilde{p}}\_3 = \\partial \_{F} {\\tilde{p}}\_4=0,

\\begin{aligned} F = \\frac{-17 Q^4+8 Q^2+8}{5 Q^2+2} \\end{aligned}

and

\\begin{aligned} 80 + 144 Q^2 - 188 Q^4 - 200 Q^6 + 307 Q^8 = 0. \\end{aligned}

In Lemma [11.15](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar142) below we show that the equation for Q^2 has no zeros in the interval Q^2 \\in \[\\frac{3}{4}, 1\]. Therefore p\_5(F,Q^2) has no local extrema in the region R\_3 of the (F,Q^2)-plane enclosed by the curves

\\begin{aligned} L\_1&: Q^2 = 1, 0\\le F\\le 1, \\\ L\_2&: \\frac{2}{3} \\le Q^2 \\le 1, 0\\le F\\le 1, \\\ L\_3&: \\frac{2}{3} \\le Q^2 \\le 1, F = 3 \\big (1-Q^2\\big ). \\end{aligned}

As the set of the (F,Q^2)-plane corresponding to R\_2 is a subset of R\_3 it suffices to check non-negativity of {\\tilde{p}}\_5 on the boundary of the region R\_3. There we have

\\begin{aligned} {\\tilde{p}}\_5(F, 1) = \\frac{3}{2} F\\left( 1 - F\\right) \\left( 2-F\\right) \\ge 0 \\quad \\text { on}\\, L\_1 \\end{aligned}

and

\\begin{aligned} {\\tilde{p}}\_5\\big (1, Q^2\\big ) = \\frac{3}{2} (1-Q^2) \\big (12 Q^4+14 Q^2-9\\big ) \\ge 0 \\quad \\text { on}\\, L\_2 \\end{aligned}

and

\\begin{aligned} {\\tilde{p}}\_5\\big (3(1-Q^2), Q^2\\big ) = \\frac{9}{2} \\big (1-Q^2\\big ) \\big (2 Q^4-3 Q^2+3\\big ) \\ge 0 \\quad \\text { on}\\, L\_3. \\end{aligned}

This concludes the proof. \\square

### Lemma 11.15

The equation

\\begin{aligned} 80 + 144 r - 188 r^2 - 200 r^3 + 307 r^4 = 0 \\end{aligned}

has no roots in the interval \[0, 1\].

### Proof

For r \\in \[0,1\] we have

\\begin{aligned} 80&+ 144 r - 188 r^2 - 200 r^3 + 307 r^4\\\&\\ge (80 - 6r) + 150r - 200r^2 - 200 r^3 + 300 r^4\\\ {}&\\ge 24 + 50\\big (1 + 3r - 4r^2 - 4r^3 + 6r^4 \\big ). \\end{aligned}

Then we see that

\\begin{aligned} 1 + 3r - 4r^2 - 4r^3 + 6r^4&= \\big (1 - 2r^2\\big )^2 +r \\big ( 2r^3 - 4r^2 + 3 \\big ) \\\&\\ge \\big (1 - 2r^2\\big )^2 +r \\big ( 2r^4 - 4r^2 + 3\\big ) \\\&\\ge \\big (1 - 2r^2\\big )^2 +r \\big ( 2(r^2 -1)^2 + 1\\big ) \\\&\\ge 0. \\end{aligned}

This concludes the proof. \\square

## 12 Discussion of Blow-up Limits in k = 2 Case

In this section we investigate the possible blow-up limits of a Ricci flow (M\_2, g(t)), t\\in \[0, T\_\\textrm{sing}), starting from an initial metric g(0) \\in {\\mathcal {I}} with \\sup \_{p \\in M\_2} b(p,0) < \\infty . By Lemma [10.5](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar109) and Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) we know that such flows develop a Type II singularity modeled on the Eguchi–Hanson space as the area of the non-principal orbit S^2\_o shrinks to zero. One expects, however, that at larger distance scales from S^2\_o one could also see other blow-up limits. The goal of this section is to show that these are in fact limited to the following four possibilities: (i) the Eguchi–Hanson space, (ii) the flat {\\mathbb {R}}^4 / {\\mathbb {Z}}\_2 orbifold, (iii) the 4d Bryant soliton quotiented by {\\mathbb {Z}}\_2 and (iv) the shrinking cylinder {\\mathbb {R}}\\times {\\mathbb {R}}P^3.\
\
Next, we state the main theorem of this section:\
\
### Theorem 12.1\
\
(Blow-up limits)   Let (M\_2, g(t)), t \\in \[0, T\_\\textrm{sing}), be a Ricci flow starting from an initial metric g(0) \\in {\\mathcal {I}} (see Definition [7.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar63)) with \\sup \_{p \\in M\_2} b(p,0) < \\infty . Let (p\_i,t\_i) be a sequence of points in spacetime with b(p\_i, t\_i) \\rightarrow 0. Passing to a subsequence, we may assume that we are in one of the four cases listed below.\
\
1. (i)\
\\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} < \\infty .\
\
2. (ii)\
\\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} = \\infty  and \\lim \_{i \\rightarrow \\infty } b\_s(p\_i, t\_i) = 1.\
\
3. (iii)\
\\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} = \\infty  and \\lim \_{i \\rightarrow \\infty } b\_s(p\_i, t\_i) \\in (0,1).\
\
4. (iv)\
\\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} = \\infty  and \\lim \_{i \\rightarrow \\infty } b\_s(p\_i, t\_i) = 0.\
\
\
Consider the dilated Ricci flows\
\
\\begin{aligned} g\_i (t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big (t\_i + b^2(p\_i, t\_i) t \\big ), \\quad t \\in \\big \[- b^{-2}(p\_i,t\_i) t\_i , 0\\big \]. \\end{aligned}\
\
Then (M\_2, g\_i(t), p\_i), t \\in \[- b(p\_i,t\_i)^{-2} t\_i , 0\], subsequentially converges, in the Cheeger–Gromov sense, to an ancient Ricci flow (M\_\\infty , g\_\\infty (t), p\_\\infty ), t \\in (-\\infty , 0\]. Depending on the limiting property of the sequence (p\_i, t\_i) we have:\
\
1. (i)\
M\_\\infty \\cong M\_2 and g\_\\infty (t) is stationary and homothetic to the Eguchi–Hanson metric.\
\
2. (ii)\
M\_\\infty \\cong ({\\mathbb {R}}^4\\setminus \\{0\\}) / {\\mathbb {Z}}\_2 and g\_\\infty (t) can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 that is stationary and isometric to the flat orbifold {\\mathbb {R}}^4/{\\mathbb {Z}}\_2.\
\
3. (iii)\
M\_\\infty \\cong ({\\mathbb {R}}^4\\setminus \\{0\\}) / {\\mathbb {Z}}\_2 and g\_\\infty (t) can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2 that is homothetic to the 4d Bryant soliton quotiented by {\\mathbb {Z}}\_2.\
\
4. (iv)\
M\_\\infty \\cong {\\mathbb {R}}\\times {\\mathbb {R}}P^3 and g\_\\infty (t) is homothetic to a shrinking cylinder.\
\
\
### Remark 12.2\
\
Notice that in Theorem [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar144) we do not claim that all blow-up limits (i)–(iv) actually occur. If the Eguchi–Hanson singularity is isolated one would only see (i) and (ii).\
\
### 12.1 Outline of Proof\
\
Assume we are given a sequence of points (p\_i, t\_i) in spacetime with b(p\_i, t\_i) \\rightarrow 0. Consider the rescaled metrics\
\
\\begin{aligned} g\_i(t) = \\frac{1}{b^2(p\_i,t\_i)} g\\big ( t\_i + b^2(p\_i, t\_i) t\\big ), \\quad t \\in \\big \[- b^{-2}(p\_i, t\_i) t\_i, 0\\big \], \\end{aligned}\
\
normalized such that b(p\_i, 0) = 1. By passing to a subsequence we may assume that either\
\
\\begin{aligned}{} & {} \\text { (I) } \\sup \_i \\frac{b(p\_i,t\_i)}{b(o,t\_i)} < \\infty \\quad \\text {or}\\\{} & {} \\text { (II) } \\lim \_{i \\rightarrow \\infty } \\frac{b(p\_i,t\_i)}{b(o,t\_i)} = \\infty . \\end{aligned}\
\
In Case (I) we know by Corollary [11.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar115) that (M\_2, g\_i(t), p\_i) subsequentially converges to the Eguchi–Hanson space, which is the blow-up limit (i) from above. Therefore we only need to investigate the behavior in Case (II), i.e., at scales larger than the forming Eguchi–Hanson singularity. At these scales Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) yields very important geometric information. In particular, we show that for every \\epsilon > 0 there exist constants C,\\delta > 0 such that the following holds: For all points ( _p_, _t_) in spacetime at which C b(o,t) \\le b(p,t) \\le \\delta  we have\
\
- Q \\ge 1 - \\epsilon ;\
\
- T\_{F\_1} :=b b\_{ss} + 1- b\_s^2 \\ge -\\epsilon ;\
\
- T\_{F\_2} :=b b\_{ss} + 1- b\_s^2 - \\left( 1-b\_s^2\\right) ^2 \\le \\epsilon ;\
\
- \\partial \_t b^2 \\le \\epsilon .\
\
\
Hence a blow-up limit (M\_\\infty , g\_\\infty (t), p\_\\infty ) in Case (II) satisfies Q = 1, T\_{F\_1} \\ge 0 and T\_{F\_2} \\le 0. Therefore M\_\\infty  is rotationally symmetric and satisfies\
\
\\begin{aligned} \\frac{1 - b^2\_s}{b^2} - \\frac{(1-b\_s^2)^2}{b^2} \\le -\\frac{b\_{ss}}{b} \\le \\frac{1 - b\_s^2}{b^2}. \\end{aligned}\
\
As -\\frac{b\_{ss}}{b} and \\frac{1-b\_s^2}{b^2} are the only non-zero components of the curvature tensor of a rotationally symmetric metric, we see that blow-up limits of Case (II) satisfy the curvature bound\
\
\\begin{aligned} \|\\textrm{Rm}\_{g\_\\infty (t)}\|\_{g\_\\infty (t)} \\le c \\frac{1-b\_s^2}{b^2} \\end{aligned}\
\
for some universal constant c>0.\
\
We now briefly explain some of the geometric intuition behind the quantities T\_{F\_1} and T\_{F\_2} for rotationally symmetric metrics. When T\_{F\_1} = 0 the underlying space is of constant curvature and therefore isometric to a sphere, the flat plane or hyperbolic space, depending on the sign of the scalar curvature. On the other hand solving the ODE T\_{F\_2} = 0 one can show that b\_s \\rightarrow 0 as s \\rightarrow \\infty  and the underlying space is asymptotically cylindrical. Thus blow-up limits in Case (II) are rotationally symmetric spaces that are ‘sandwiched’ between a sphere and an asymptotically cylindrical space.\
\
We need to divide Case (II) into three subcases in order to investigate the possible blow-up limits: By passing to a subsequence we may assume that\
\
\\begin{aligned}{} & {} \\text {(II.a) } b\_s(p\_i, t\_i) \\rightarrow 1 \\, \\text { or }\\\{} & {} \\text {(II.b) } b\_s(p\_i,t\_i) \\rightarrow \\eta \\in (0,1) \\, \\text { or } \\,\\\{} & {} \\text {(II.c) } b\_s(p\_i,t\_i) \\rightarrow 0. \\end{aligned}\
\
For (II.a) and (II.c) we show in Lemmas [12.9](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar167) and [12.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar157) that (M\_2, g\_i(t), p\_i) subsequentially converges to the flat orbifold {\\mathbb {R}}^4 / {\\mathbb {Z}}\_2 and the shrinking cylinder {\\mathbb {R}}\\times {\\mathbb {R}}P^3, respectively. The main idea is that by the strong maximum principle applied to the evolution equation ( [A.4](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ112)) of b\_s when Q=1 a minimum b\_s = 0 or a maximum b\_s = 1 can only be attained if b\_s is constant everywhere.\
\
Proving that the blow-up limit in Case (II.b) is an ancient orbifold Ricci flow, which is homothetic to the 4d Bryant soliton quotiented by {\\mathbb {Z}}\_2, is trickier. The construction is carried out in Lemma [12.8](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar161), the proof of which we sketch here: Fix a T > 0 and define\
\
\\begin{aligned} E\_{p,t,n} :=\\left\\{ p' \\in M\_2 \\, \\Big \| \\, b(p',t) > \\frac{b(p,t)}{n} \\right\\} \\subseteq M\_2. \\end{aligned}\
\
Then consider the rescaled metrics g\_i(t), defined as above, on the parabolic neighborhoods\
\
\\begin{aligned} \\Omega \_{i,n} :=E\_{p\_i, t\_i, n} \\times \[-T - 1, 0\] \\end{aligned}\
\
in spacetime. By Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146) we know that \\partial \_t b^2 \\rightarrow 0 uniformly as b \\rightarrow 0. Hence from the curvature bound\
\
\\begin{aligned} \|\\textrm{Rm}\_{g(t)}\|\_{g(t)} \\le \\frac{C\_1}{b^{2}} \\end{aligned}\
\
(12.1)\
\
\
of Theorem [7.6](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar67), we see that the curvature of g\_i(t) is bounded by Cn^2 on \\Omega \_{i,n} for _i_ sufficiently large and C>0 some constant. The difficulty in constructing the limiting orbifold flow arises from the fact that the curvature bound ( [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#Equ103)) degenerates as n \\rightarrow \\infty . We get around this by exploiting the inequalities on T\_{F\_1} and T\_{F\_2} derived in Lemma [12.3](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar146), to find a uniform curvature bound independent of _n_. From here it is then easy to construct the orbifold Ricci flow g\_\\infty (t), t \\in \[-T, 0\], on ({\\mathbb {R}}^4 \\setminus \\{0\\}) /{\\mathbb {Z}}\_2 by taking the limit n\\rightarrow \\infty . Via Lemma [B.2](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar176), and Theorem [B.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar175) in Appendix B, we show that g\_\\infty (t) can be extended to a smooth orbifold Ricci flow on {\\mathbb {R}}^4/{\\mathbb {Z}}\_2. A priori the curvature bound of g\_\\infty (t) on {\\mathbb {R}}^4 / {\\mathbb {Z}}\_2 \\times \[0,T\] may deteriorate as T \\rightarrow \\infty . Nevertheless we can use a diagonal argument to construct an ancient orbifold Ricci flow on {\\mathbb {R}}^4 /{\\mathbb {Z}}\_2. Hamilton’s trace Harnack inequality then implies that g\_\\infty (t) has bounded curvature on {\\mathbb {R}}^4/{\\mathbb {Z}}^2 \\times (-\\infty ,0\]. Finally, we apply the result \[ [27](https://link.springer.com/article/10.1007/s42543-022-00048-y#ref-CR27 "Li, X.L., Zhang, Y.J.: Ancient solutions to the Ricci flow in higher dimensions,                    arXiv:1812.04156                                     (2018)")\] by Xiaolong Li and Yongjia Zhang to deduce that g\_\\infty (t) is homothetic to the 4d Bryant soliton quotiented by {\\mathbb {Z}}\_2.

### 12.2 Proof of Main Theorem

We begin by proving the central lemma of this section, which yields important geometric information on the high curvature regions of a Ricci flow (M\_2, g(t)) as in the Theorem [12.1](https://link.springer.com/article/10.1007/s42543-022-00048-y#FPar144).

### Lemma 12.3