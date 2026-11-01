---
retention_scope: session
part: 3
total_parts: 7
---

[Part 3/7 of: A Continuous Cusp Closing Process for Negative Kähler–Einstein Metrics]

which takes the value _p_ =(0,…,0,1,0) at a point _q_ such that _t_( _q_)= _τ_. Under this chart, the metric _ω_ _cusp_ is equivalent to _δ_ _ij_ and in addition, for all _k_, _α_,\
\
\\begin{aligned} \\psi '\_{cusp} i\\partial \\overline{\\partial} \\varphi , \\quad \\psi ''\_{cusp} i(\\partial \\varphi - \\partial \\log z\_{n} ) \\wedge ( \\overline{\\partial} \\varphi - \\overline{\\partial} \\log \\overline{z}\_{n}) \\end{aligned}\
\
(2.110)\
\
\
have bounded _C_ _k_ norms on a fixed size ball centered at _p_, with bounds that are independent of _τ_. Also, _ψ_ _T_, _ψ_ _cusp_ are independent of _x_ _α_, _y_ _α_, _θ_. Applying this chart, Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36) implies that, for _t_ ∈\[2 _τ_, _τ_\],\
\
\\begin{aligned} \|\\nabla \_{\\omega \_{cusp}}^{k} (\\psi \_{T} -\\psi \_{cusp})\|\_{\\omega \_{cusp}}=O\_{k}(\|b\|\| \\tau \|^{n+1}). \\end{aligned}\
\
(2.111)\
\
\
Meanwhile, to prove higher order derivative estimates of _ω_ _T_ under the coordinates ( [2.109](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ112)), we only have to check that\
\
\\begin{aligned} \\frac{\\psi '\_{T}}{\\psi '\_{cusp}}, \\;\\, \\frac{\\psi ''\_{T}}{\\psi ''\_{cusp}} \\end{aligned}\
\
(2.112)\
\
\
have uniformly bounded _C_ _k_ norm with respect to ( [2.109](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ112)). For example,\
\
\\begin{aligned} \\frac{\\partial}{\\partial \\check{x}} \\frac{\\psi ''\_{T}}{\\psi ''\_{cusp}} = -\|\\tau \|^{-1} \\frac{\\partial t}{\\partial x}\\cdot \\frac{\\psi '''\_{T} \\psi \_{cusp}'' - \\psi ''\_{T} \\psi \_{cusp}'''}{(\\psi \_{cusp}'')^{2}}, \\end{aligned}\
\
(2.113)\
\
\
where\
\
\\begin{aligned} \\begin{aligned} t^{5}(\\psi '''\_{T} \\psi \_{cusp}'' - \\psi ''\_{T} \\psi \_{cusp}''')= (t^{3} \\psi '''\_{T} -t^{3} \\psi \_{cusp}''')t^{2}\\psi \_{cusp}'' - (t^{2}\\psi ''\_{T} -t^{2} \\psi \_{cusp}'')t^{3}\\psi \_{cusp}''' , \\end{aligned} \\end{aligned}\
\
(2.114)\
\
\
which is _O_(\| _b_ \|\| _τ_ \|_n_ +1) by Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36). This shows that\
\
\\begin{aligned} \\frac{\\partial}{\\partial \\check{x}} \\frac{\\psi ''\_{T}}{\\psi ''\_{cusp}} = O(\|b\|\|\\tau \|^{n+1}). \\end{aligned}\
\
(2.115)\
\
\
We can estimate the _C_ _k_ norm of ( [2.112](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ115)) with _k_ ⩾1 by induction, using the formula\
\
\\begin{aligned} \\left (\\frac{f}{g}\\right )^{(k)} = \\frac{1}{g}\\left (f^{(k)} -k! \\sum \_{j=1}^{k} \\frac{g^{(k+1-j)}}{(k+1-j)!} \\frac{\\left (\\frac{f}{g}\\right )^{(j-1)}}{(j-1)!}\\right ) \\end{aligned}\
\
(2.116)\
\
\
with\
\
\\begin{aligned} f=\\psi '\_{T} - \\psi '\_{cusp},\\;\\, g = \\psi '\_{cusp} \\end{aligned}\
\
(2.117)\
\
\
or with\
\
\\begin{aligned} f=\\psi ''\_{T} - \\psi ''\_{cusp},\\;\\, g = \\psi ''\_{cusp}. \\end{aligned}\
\
(2.118)\
\
\
By Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36) and ( [2.44](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ47)), we have for any _k_ ⩾1 that _f_( _k_)= _O_(\| _b_ \|\| _τ_ \|_n_ +1).\
\
Thus, in conclusion, we have proved the following lemma.\
\
### Lemma 2.24\
\
Let _ψ_ _T_ be the solution of ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) satisfying ( [2.88](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ91)) and assume that ( [2.81](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ84)) is in force. Then for any k\\in \\mathbb{N} and for all _t_ ∈\[2 _τ_, _τ_\],\
\
\\begin{aligned} \|\\nabla \_{\\omega \_{cusp}}^{k} (\\omega \_{T} - \\omega \_{cusp})\|\_{ \\omega \_{cusp}}= O(\|b\|\|\\tau \|^{n+1}). \\end{aligned}\
\
(2.119)\
\
\
#### 2.4.2 Estimates on the middle neck\
\
### Proposition 2.25\
\
Assume that b\\in (-\\frac{1}{2}, 0). Let _ψ_ _T_ be the solution of ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) satisfying ( [2.88](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ91)). Then:\
\
(1):\
\
For _t_ ∈\[ _T_, _τ_\],\
\
\\begin{aligned} 0\\leqslant \\psi \_{T}(t) - \\psi \_{cusp}(t) < C, \\end{aligned}\
\
(2.120)\
\
\
where _C_ does not depend on _b_.\
\
(2):\
\
_ψ_ _T_( _t_)− _ψ_ _cusp_( _t_) is a decreasing function on \[ _T_, _τ_\].\
\
(3):\
\
\\psi \_{T}'(t) < \\psi \_{cusp}'(t) for _t_ ∈\[ _T_, _τ_\].\
\
### Proof\
\
By ( [2.82](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ85)), ( [2.92](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ95)), when _t_ = _τ_ or _T_, 0⩽ _ψ_ _T_− _ψ_ _cusp_< _C_, where _C_ is independent of _b_. Now assume that _ψ_ _T_− _ψ_ _cusp_ has a positive local maximum at _p_ ∈( _T_, _τ_). Then\
\
\\begin{aligned} &\\psi \_{T}(p) > \\psi \_{cusp}(p), \\end{aligned}\
\
(2.121)\
\
\
\\begin{aligned} &0< \\psi \_{T}'(p) = \\psi \_{cusp}'(p), \\end{aligned}\
\
(2.122)\
\
\
\\begin{aligned} &0< \\psi \_{T}''(p) \\leqslant \\psi \_{cusp}''(p), \\end{aligned}\
\
(2.123)\
\
\
which contradicts the fact that _ψ_ _T_ and _ψ_ _cusp_ both satisfy equation ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)). Similarly, _ψ_ _T_− _ψ_ _cusp_ does not have a negative local minimum in ( _T_,log\| _b_ \|). Part (1) of the lemma is proved.\
\
Notice that _ψ_ _T_− _ψ_ _cusp_=0 at _τ_. If _ψ_ _T_− _ψ_ _cusp_ is not monotone, then it has either a positive local maximum or a negative local minimum in ( _T_, _τ_), which contradicts the above discussion. At _τ_, \\psi \_{T}' < \\psi \_{cusp}' by ( [2.79](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ82)). So _ψ_ _T_− _ψ_ _cusp_ is a decreasing function.\
\
For part (3), we assume that it is not true and set\
\
\\begin{aligned} t\_{0} := \\sup \\{ t \\in \[T, \\tau \]: \\psi \_{T}'(t) \\geqslant \\psi '\_{cusp}(t) \\}. \\end{aligned}\
\
(2.124)\
\
\
Then _t_ 0< _τ_. At _t_ 0, we have\
\
\\begin{aligned} &0< \\psi \_{T}'(t\_{0}) = \\psi \_{cusp}'(t\_{0}), \\end{aligned}\
\
(2.125)\
\
\
\\begin{aligned} &0< \\psi \_{T}''(t\_{0}) \\leqslant \\psi \_{cusp}''(t\_{0}), \\end{aligned}\
\
(2.126)\
\
\
By part (2), _ψ_ _T_( _t_ 0)> _ψ_ _cusp_( _t_ 0). This contradicts equation ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)). □\
\
### Proposition 2.26\
\
Fix _δ_ ∈(0,1). Then for all _η_ ∈(0, _δ_\] we have that\
\
\\begin{aligned} \\psi \_{T} (\\eta T) = \\psi \_{cusp} (\\eta T) + O(\|b\|^{\\frac{1}{n+1}} \\tau ) +O\_{\\delta}(\\eta ^{n+1}). \\end{aligned}\
\
(2.127)\
\
\
In addition,\
\
\\begin{aligned} \\psi '\_{T}(\\eta T) &= \\psi \_{cusp}' (\\eta T)e^{O\_{\\delta}(\\eta ^{n+1}) } (1+O(\|b\|^{\\frac{1}{n+1}}\\tau )), \\end{aligned}\
\
(2.128)\
\
\
\\begin{aligned} \\psi ''\_{T}(\\eta T) &=\\psi \_{cusp}''(\\eta T)e^{O\_{\\delta}(\\eta ^{n+1}) } (1+O(\|b\|^{\\frac{1}{n+1}}\\tau ) ). \\end{aligned}\
\
(2.129)\
\
\
### Proof\
\
Taking _t_ 0= _ηT_ and _t_ = _T_ and substituting _ξ_ = _s_ + _ψ_ _T_( _T_) in ( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)), we get\
\
\\begin{aligned} \\int \_{0}^{\\psi \_{T}(\\eta T)-\\psi \_{T}(T)} (e^{s}-1 )^{-\\frac{1}{n+1}}ds = (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(\\eta T-T). \\end{aligned}\
\
(2.130)\
\
\
By part (2) of Proposition [2.25](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar38), as _η_ →0+,\
\
\\begin{aligned} \\psi \_{T} (\\eta T) - \\psi \_{T} (T) > \\psi \_{cusp} (\\eta T) -\\psi \_{cusp} (T) -C \\rightarrow \\infty . \\end{aligned}\
\
(2.131)\
\
\
Taking _η_ →0+ in ( [2.130](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ133)),\
\
\\begin{aligned} \\int \_{0}^{\\infty} (e^{s}-1 )^{-\\frac{1}{n+1}}ds = (n+1)^{ \\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}\|T\|. \\end{aligned}\
\
(2.132)\
\
\
Subtracting it from ( [2.130](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ133)),\
\
\\begin{aligned} \\begin{aligned} \\int \_{\\psi \_{T} (\\eta T) - \\psi \_{T} (T)}^{\\infty} (e^{s}-1 )^{- \\frac{1}{n+1}}ds &= (n+1)^{\\frac{1}{n+1}}\\eta \|b\|^{\\frac{1}{n+1}}\|T\| \\\ &=\\eta \\left (\\int \_{0}^{\\infty }(e^{s}-1 )^{-\\frac{1}{n+1}}ds +O( \|b\|^{ \\frac{1}{n+1}}\\tau )\\right ), \\end{aligned} \\end{aligned}\
\
(2.133)\
\
\
where we applied ( [2.89](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ92)) for the last step. When _s_ >0 is bounded away from 0,\
\
\\begin{aligned} (e^{s}-1 )^{-\\frac{1}{n+1}} = e^{-\\frac{s}{n+1}} (1 - e^{-s})^{- \\frac{1}{n+1}} = e^{-\\frac{s}{n+1}} + O(e^{-\\frac{(n+2)s}{n+1}}). \\end{aligned}\
\
(2.134)\
\
\
Thus,\
\
\\begin{aligned} \\begin{aligned} &\\psi \_{T} (\\eta T) - \\psi \_{T} (T) \\\ &\\quad=(n+1)\\log (n+1) -(n+1)\\log \\eta \\\ &\\qquad{}-(n+1)\\log \\left (\\int \_{0}^{\\infty }(e^{s}-1 )^{-\\frac{1}{n+1}}ds \\right )+O(\|b\|^{\\frac{1}{n+1}}\\tau ) +O(\\eta ^{n+1}). \\end{aligned} \\end{aligned}\
\
(2.135)\
\
\
Comparing this to\
\
\\begin{aligned} \\begin{aligned} \\psi \_{cusp} (\\eta T) - \\psi \_{T} (T) &= -(n+1)\\log (-\\eta T) - \\log \|b\| +n\\log (n+1) \\\ &=-(n+1) \\log \\eta +(n+1)\\log (n+1) \\\ &-(n+1)\\log \\left (\\int \_{0}^{\\infty }(e^{s}-1 )^{-\\frac{1}{n+1}}ds \\right )+O(\|b\|^{\\frac{1}{n+1}}\\tau ), \\end{aligned} \\end{aligned}\
\
(2.136)\
\
\
we obtain that\
\
\\begin{aligned} \\psi \_{T} (\\eta T) - \\psi \_{cusp} (\\eta T) = O(\|b\|^{\\frac{1}{n+1}} \\tau ) +O(\\eta ^{n+1}). \\end{aligned}\
\
(2.137)\
\
\
The rest of the proposition follows by analyzing ( [2.79](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ82)) and ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)). □\
\
### Definition 2.27\
\
Perturbation of differential operators\
\
Given a function _ε_( **x**)>0 on a local chart **x**, we say that _f_( **x**)= _O_( _ε_( **x**)) if \| _f_( **x**)\|⩽ _Cε_( **x**) for some _C_ >0 independent of **x** and of _b_, _T_. Let\
\
\\begin{aligned} L &= \\sum \_{i,j=1}^{m} a\_{ij}(\\mathbf{x}) \\partial ^{2}\_{ij} + \\sum \_{i=1}^{m} b\_{i}(\\mathbf{x}) \\partial \_{i}, \\end{aligned}\
\
(2.138)\
\
\
\\begin{aligned} \\tilde{L} &= \\sum \_{i,j=1}^{m} \\tilde{a}\_{ij}(\\mathbf{x}) \\partial ^{2}\_{ij} + \\sum \_{i=1}^{m}\\tilde{b}\_{i}(\\mathbf{x}) \\partial \_{i}, \\end{aligned}\
\
(2.139)\
\
\
be two differential operators. We say that \\tilde{L} = L + O(\\varepsilon (\\mathbf{x})) if\
\
\\begin{aligned} \\tilde{a}\_{ij} = (1+O(\\varepsilon (\\mathbf{x}))) a\_{ij}, \\quad \\tilde{b}\_{i} =(1+O(\\varepsilon (\\mathbf{x}))) b\_{i}, \\end{aligned}\
\
(2.140)\
\
\
for all 1⩽ _i_, _j_ ⩽ _m_. Similarly, we say that \\tilde{L} = L \\cdot e^{O(\\varepsilon (\\mathbf{x}))} if\
\
\\begin{aligned} \\tilde{a}\_{ij} = e^{O(\\varepsilon (\\mathbf{x}))} a\_{ij}, \\quad \\tilde{b}\_{i} =e^{O(\\varepsilon (\\mathbf{x}))} b\_{i}. \\end{aligned}\
\
(2.141)\
\
\
### Lemma 2.28\
\
Recall the local holomorphic chart ( _z_ 1,…, _z_ _n_) introduced after Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36). Assume that in this chart a Kähler metric _g_ is given by\
\
\\begin{aligned} g\_{i \\bar{j}} = -F\\varphi \_{i \\bar{j}} + G\\left (\\varphi \_{i} - \\frac{\\delta \_{i n }}{z\_{n}}\\right )\\left (\\varphi \_{\\bar{j}} - \\frac{\\delta \_{j n }}{\\overline{z}\_{n}}\\right ), \\end{aligned}\
\
(2.142)\
\
\
where _F_, _G_ are positive functions and _φ_ is a function of _z_ 1,…, _z_ _n_ −1. Then its inverse g^{\\bar{j} k} is given by\
\
\\begin{aligned} \\begin{aligned} &g^{\\bar{\\beta}\\alpha} = -\\frac{\\varphi ^{\\bar{\\beta}\\alpha}}{F}\\;\\,(1 \\leqslant \\alpha ,\\beta \\leqslant n-1), \\;\\, g^{\\bar{\\alpha}n} = - \\frac{\\varphi ^{\\bar{\\alpha}\\gamma}\\varphi \_{ \\gamma}z\_{n}}{F}, \\\ & g^{ \\bar{n} n} = \\frac{\|z\_{n}\|^{2} (F- G \\varphi ^{\\bar{\\beta}\\alpha} \\varphi \_{\\alpha }\\varphi \_{\\bar{\\beta}})}{F G}. \\end{aligned} \\end{aligned}\
\
(2.143)\
\
\
The next corollary follows from Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40).\
\
### Corollary 2.29\
\
Fix _δ_ ∈(0,1) and let _η_ ∈(0, _δ_\]. Then at _t_ = _ηT_,

\\begin{aligned} \\Delta \_{\\omega \_{T}} = (L\_{h} +O(\|b\|^{\\frac{1}{n+1}}\\tau )) \\cdot e^{O\_{ \\delta}(\\eta ^{n+1})}, \\end{aligned}

(2.144)


where the cuspidal Laplacian _L_ _h_ was introduced in \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), Lemma 2.5\]. Using the notation _x_ =−1/ _t_ and _θ_ =arg _z_ _n_ from \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\], an explicit formula for _L_ _h_ is

\\begin{aligned} \\begin{aligned} &L\_{h}u = \\frac{1}{n+1}(x^{2} u\_{xx}+(n+1) xu\_{x} - (n+1)u -x^{-1} \\varphi ^{\\bar{\\beta}\\alpha}u\_{\\alpha \\bar{\\beta}}\\\ &\\phantom{L\_{h}u =}{} +(2x)^{-1}u\_{ \\theta \\theta})+F, \\\ &F = F(x\_{\\alpha},y\_{\\alpha}, x^{-1}u\_{\\theta \\alpha}, x^{-1}u\_{ \\theta \\bar{\\alpha}}, x^{-1}u\_{\\theta \\theta}), \\end{aligned} \\end{aligned}

(2.145)


with _F_ smooth in _x_ _α_, _y_ _α_ and linear homogeneous in the other arguments. In addition, for all _k_ ⩾0,

\\begin{aligned} \|\\nabla \_{\\omega \_{cusp}}^{k} (\\omega \_{T} - \\omega \_{cusp})\|\_{ \\omega \_{cusp}} = O\_{\\delta ,k}(\|b\|^{\\frac{1}{n+1}}\|\\tau \| + \\eta ^{n+1}). \\end{aligned}

(2.146)


### Proof

( [2.144](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ147)) follows from Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40), Lemma [2.28](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar43), and the proof of Lemma 2.5 in \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\].

To prove ( [2.146](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ149)), we first rewrite ( [2.106](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ109)) as

\\begin{aligned} \\psi \_{T}'' = (n+1)^{n} e^{\\psi \_{T} -\\psi \_{cusp}} (-t)^{-n-1}(\\psi \_{T}')^{1-n} \\end{aligned}

(2.147)


and differentiate it multiple times to inductively show that

\\begin{aligned} \\psi ^{(k)}\_{T}(\\eta T) &=\\psi \_{cusp}^{(k)}(\\eta T) (1+O(\|b\|^{ \\frac{1}{n+1}}\\tau )+O(\\eta ^{n+1})). \\end{aligned}

(2.148)


In fact, cases _k_ =1,2 follow directly from Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40). For _k_ ⩾3, when we differentiate ( [2.147](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ150)) _k_ −2 times using the product rule, every term on the right-hand side is of the form

\\begin{aligned} (-t)^{-k} (C+O(\|b\|^{\\frac{1}{n+1}}\\tau )+O(\\eta ^{n+1})). \\end{aligned}

(2.149)


By formally writing 1 = e^{\\psi \_{cusp} - \\psi \_{cusp}} and differentiating

\\begin{aligned} \\psi \_{cusp}'' = (n+1)^{n} e^{\\psi \_{cusp} -\\psi \_{cusp}} (-t)^{-n-1}( \\psi \_{cusp}')^{1-n} \\end{aligned}

(2.150)


_k_ −2 times, we know that the constants _C_ add up to ( _n_ +1)( _k_ −1)! as

\\begin{aligned} \\psi \_{cusp}^{(k)}(t) =(n+1)(k-1)!(-t)^{-k}. \\end{aligned}

(2.151)


Here we use the fact that the ( _k_ −2)-th derivatives of ( [2.147](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ150)) and ( _k_ −2)-th derivatives of ( [2.150](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ153)) are in similar forms. With this, we derive ( [2.148](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ151)). Near a point _q_ with _t_ ∗:= _t_( _q_)∈\[ _δT_, _τ_\], we then consider quasi-coordinates for _ω_ _cusp_ as in ( [2.109](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ112)):

\\begin{aligned} (\\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{x}, \\check{\\theta}) := ((-t\_{\*})^{- \\frac{1}{2}} x\_{\\alpha}, (-t\_{\*})^{-\\frac{1}{2}} y\_{\\alpha}, -t\_{\*} x, (-t\_{\*})^{-1}\\theta ). \\end{aligned}

(2.152)


Similarly as in the proof of Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36), we need to show that the _C_ _k_ norm of

\\begin{aligned} \\frac{\\psi '\_{T} - \\psi '\_{cusp}}{\\psi '\_{cusp}}, \\;\\, \\frac{\\psi ''\_{T} - \\psi ''\_{cusp}}{\\psi ''\_{cusp}} \\end{aligned}

(2.153)


with respect to ( [2.152](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ155)) on \\{2t\_{\*}< t<\\frac{1}{2}t\_{\*}\\} is bounded by C\_{k} (\|b\|^{\\frac{1}{n+1}}\|\\tau \|+\\eta ^{n+1}). For _k_ =0, this follows directly from ( [2.148](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ151)). For _k_ ⩾1, we prove it by induction by applying ( [2.116](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ119))–( [2.118](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ121)). □

### Proposition 2.30

Let _δ_ ∈(0,1) be a small dimensional constant. Define the coordinate _s_:=1− _t_/ _T_ and restrict it to _s_ ∈\[2\| _T_ \|_α_ −1, _δ_\] for some _α_ ∈(0,1). Then \\Delta \_{\\omega \_{T}} is of the form

\\begin{aligned} \\Delta \_{\\omega \_{T}} = L +O(\|b\|^{-\\frac{1}{n+1}} s^{-\\frac{1}{n}}) \\cdot \\partial ^{2}\_{\\theta \\theta}+O(\|b\|^{\\frac{1}{n+1}}\\tau )+O(s^{ \\frac{n+1}{n}}). \\end{aligned}

(2.154)


Here the _O_ notation is understood in the sense of Definition [2.27](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar42) with respect to the local chart _s_, _θ_, _z_ _α_ and the model operator _L_ takes the following form:

\\begin{aligned} \\begin{aligned} L u &= \\left (\\frac{n+1}{n}\\right )^{\\frac{1}{n}} c(n)^{- \\frac{n+1}{n}}(n s^{\\frac{n-1}{n}}u\_{ss} + (n-1)s^{-\\frac{1}{n}}u\_{s}) + \|b\|^{-\\frac{1}{n+1}}s^{-\\frac{1}{n}} \\mathcal{T} u \\\ &+ C\|b\|^{-\\frac{2}{n+1}} s^{\\frac{n-1}{n}} u\_{\\theta \\theta}+s^{- \\frac{1}{n}}\\mathcal{H}u, \\end{aligned} \\end{aligned}

(2.155)


where _C_ >0 is a constant, \\mathcal{T} is an elliptic operator on _E_ and \\mathcal{H} is linear homogeneous in

\\begin{aligned} u\_{s \\alpha}, u\_{s \\bar{\\beta}}, u\_{s\\theta}, \|b\|^{-\\frac{1}{n+1}} u\_{ \\alpha \\theta}, \|b\|^{-\\frac{1}{n+1}} u\_{\\bar{\\beta}\\theta} \\end{aligned}

(2.156)


with coefficients that are smooth in _x_ _α_, _y_ _α_ and independent of _b_, _T_.

The term O(s^{\\frac{n+1}{n}}) in ( [2.154](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ157)) stands for a comparison of differential operators as in ( [2.140](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ143)), so for applications it is important to know that this term is >−1. This is ensured by our assumption _s_ ⩽ _δ_. Similarly, given the condition _s_ ⩾2\| _T_ \|_α_ −1, we can observe that the term with \\partial ^{2}\_{\\theta \\theta} in ( [2.154](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ157)) is

\\begin{aligned} O(\|b\|^{-\\frac{1}{n+1}} s^{-\\frac{1}{n}})\\cdot \\partial ^{2}\_{\\theta \\theta} = O(\|b\|^{\\frac{\\alpha}{n+1}}) \\cdot \|b\|^{-\\frac{2}{n+1}} s^{ \\frac{n-1}{n}} u\_{\\theta \\theta}. \\end{aligned}

(2.157)


Hence, this term represents a higher-order contribution compared to the operator _L_.

### Proof of Proposition [2.30](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar46)

By ( [2.130](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ133)) and ( [2.89](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ92)),

\\begin{aligned} \\begin{aligned} \\int \_{0}^{\\psi \_{T}(\\eta T)-\\psi \_{T}(T)} (e^{\\xi}-1 )^{- \\frac{1}{n+1}} d\\xi &= (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(1- \\eta )\|T\| \\\ &=(c(n) +O(\|b\|^{\\frac{1}{n+1}}\\tau ))(1-\\eta ), \\end{aligned} \\end{aligned}

(2.158)


where 1− _η_ = _s_ and the O(\|b\|^{\\frac{1}{n+1}}\\tau ) term is independent of _s_. When _ξ_ >0 is bounded,

\\begin{aligned} (e^{\\xi}-1)^{-\\frac{1}{n+1}} = \\xi ^{-\\frac{1}{n+1}}(1+O(\\xi )) = \\xi ^{-\\frac{1}{n+1}} + O(\\xi ^{\\frac{n}{n+1}}). \\end{aligned}

(2.159)


Thus, we have that

\\begin{aligned} \\begin{aligned} &\\int \_{0}^{\\psi \_{T}(\\eta T)-\\psi \_{T}(T)} (e^{\\xi}-1 )^{- \\frac{1}{n+1}} d\\xi \\\ &\\quad= \\frac{n+1}{n}({\\psi \_{T}(\\eta T)-\\psi \_{T}(T)})^{ \\frac{n}{n+1}}(1+O({\\psi \_{T}(\\eta T)-\\psi \_{T}(T)})). \\end{aligned} \\end{aligned}

(2.160)


By ( [2.158](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ161)),

\\begin{aligned} \\begin{aligned} &\\psi \_{T}(\\eta T)-\\psi \_{T}(T)\\\ &\\quad =\\left (\\frac{n}{n+1}\\right )^{ \\frac{n+1}{n}} \\left (c(n) +O(\|b\|^{\\frac{1}{n+1}}\\tau )\\right )^{ \\frac{n+1}{n}}s^{\\frac{n+1}{n}} (1+ O(\\psi \_{T}(\\eta T)-\\psi \_{T}(T))), \\end{aligned} \\end{aligned}

(2.161)


which further implies that

\\begin{aligned} \\begin{aligned} &\\psi \_{T}(\\eta T)-\\psi \_{T}(T)\\\ &\\quad = \\left (\\frac{n}{n+1}\\right )^{ \\frac{n+1}{n}} \\left (c(n)+O(\|b\|^{\\frac{1}{n+1}}\\tau ) \\right )^{ \\frac{n+1}{n}} s^{\\frac{n+1}{n}}(1+O(s^{\\frac{n+1}{n}})). \\end{aligned} \\end{aligned}

(2.162)


The metric _ω_ _T_ is given by

\\begin{aligned} \\omega \_{T} = -\\psi \_{T}'i\\partial \\overline{\\partial} \\varphi +\\psi \_{T}''i(- \\partial \\varphi +\\partial \\log z\_{n}) \\wedge (-\\overline{\\partial} \\varphi +\\overline{\\partial} \\log z\_{n}). \\end{aligned}

(2.163)


Thanks to ( [2.162](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ165)), we can evaluate the coefficients as follows:

\\begin{aligned} \\begin{aligned} &\\psi \_{T}'(\\eta T)\\\ &\\quad = (n+1)^{\\frac{1}{n+1}}(e^{\\psi \_{T}(\\eta T) +a}+b)^{ \\frac{1}{n+1}} \\\ &\\quad= (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(e^{\\psi \_{T}(\\eta T) - \\psi \_{T}(T)}-1)^{\\frac{1}{n+1}} \\\ &\\quad= (n+1)^{\\frac{1}{n+1}}\\left (\\frac{n}{n+1}\\right )^{\\frac{1}{n}}\|b\|^{ \\frac{1}{n+1}}s^{\\frac{1}{n}}\\left (c(n)^{\\frac{1}{n}} +O(\|b\|^{ \\frac{1}{n+1}}\\tau ) +O(s^{\\frac{n+1}{n}})\\right ), \\end{aligned} \\end{aligned}

(2.164)


\\begin{aligned} \\begin{aligned} &\\psi \_{T}''(\\eta T) \\\ &\\quad= \\frac{e^{\\psi \_{T}(\\eta T)+a}}{(\\psi \_{T}'(\\eta T))^{n-1}} = \\frac{\|b\|e^{\\psi \_{T}(\\eta T)- \\psi \_{T}(T)}}{(\\psi \_{T}'(\\eta T))^{n-1}} \\\ &\\quad= (n+1)^{\\frac{1-n}{n+1}} \\left (\\frac{n}{n+1}\\right )^{ \\frac{1-n}{n}}\|b\|^{\\frac{2}{n+1}}s^{\\frac{1-n}{n}}\\\ &\\qquad{}\\times \\left (c(n)^{ \\frac{1-n}{n}} +O(\|b\|^{\\frac{1}{n+1}}\\tau ) +O(s^{\\frac{n+1}{n}}) \\right ). \\end{aligned} \\end{aligned}

(2.165)


Setting _x_ =−1/ _t_, we have _x_ =(1− _s_)−1\| _T_ \|−1 and

\\begin{aligned} \\partial \_{x} &= \|T\|(1-s)^{2} \\partial \_{s}, \\quad \\partial \_{xx}^{2} = \|T\|^{2}(1-s)^{4}\\partial \_{s}^{2} - 2\|T\|^{2}(1-s)^{3} \\partial \_{s}. \\end{aligned}

(2.166)


Given this conversion formula, it will be enough to express \\Delta \_{\\omega \_{T}} in terms of \\partial \_{x}, \\partial ^{2}\_{xx}. This can be done by a computation similar to the proof of \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), Lemma 2.5\]. Set

\\begin{aligned} Q := \\varphi ^{\\bar{\\beta}\\alpha}\\varphi \_{\\alpha }\\varphi \_{ \\bar{\\beta}}, \\end{aligned}

(2.167)


which is uniformly bounded. Applying Lemma [2.28](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar43) with _F_ = _ψ_′( _ηT_), _G_ = _ψ_″( _ηT_), we have that

\\begin{aligned} \\begin{aligned} &g^{\\bar{n} n} \\partial \_{n} \\partial \_{\\bar{n}} \\\ &\\quad= \\frac{r^{2}(F - GQ)}{FG} \\left (\\frac{x^{2}}{z\_{n}}\\partial \_{x} - \\frac{i}{2z\_{n}}\\partial \_{\\theta}\\right ) \\left ( \\frac{x^{2}}{\\overline{z}\_{n}}\\partial \_{x} + \\frac{i}{2\\overline{z}\_{n}}\\partial \_{\\theta}\\right ) \\\ &\\quad= \\left (\\frac{1}{G} -\\frac{Q}{F}\\right ) \\left (x^{4} \\partial ^{2}\_{xx} + 2 x^{3} \\partial \_{x} + \\frac{1}{4} \\partial ^{2}\_{\\theta \\theta} \\right ) \\\ &\\quad= (n+1)^{\\frac{n-1}{n+1}} \\left (\\frac{n}{n+1}\\right )^{ \\frac{n-1}{n}}c(n)^{\\frac{n-1}{n}}\|b\|^{-\\frac{2}{n+1}} s^{ \\frac{n-1}{n}} \\left (x^{4} \\partial ^{2}\_{xx} + 2 x^{3} \\partial \_{x} + \\frac{1}{4} \\partial ^{2}\_{\\theta \\theta} \\right ) \\\ &\\qquad{} -\\frac{Q}{F}(x^{4} \\partial ^{2}\_{xx} + 2 x^{3} \\partial \_{x})+O(\|b\|^{- \\frac{1}{n+1}} s^{-\\frac{1}{n}}) \\partial ^{2}\_{\\theta \\theta} +O(\|b\|^{ \\frac{1}{n+1}}\\tau ) +O(s^{\\frac{n+1}{n}}) \\\ &\\quad= (n+1) \\left (\\frac{n}{n+1}\\right )^{\\frac{n-1}{n}} c(n)^{- \\frac{n+1}{n}} s^{\\frac{n-1}{n}} \\partial ^{2}\_{ss} + C\|b\|^{- \\frac{2}{n+1}} s^{\\frac{n-1}{n}} \\partial ^{2}\_{\\theta \\theta} \\\ &\\qquad{} -\\frac{Q}{F}(x^{4} \\partial ^{2}\_{xx} + 2 x^{3} \\partial \_{x})+O(\|b\|^{- \\frac{1}{n+1}} s^{-\\frac{1}{n}}) \\partial ^{2}\_{\\theta \\theta} +O(\|b\|^{ \\frac{1}{n+1}}\\tau ) +O(s^{\\frac{n+1}{n}}), \\end{aligned} \\end{aligned}

(2.168)


\\begin{aligned} \\begin{aligned} &g^{\\bar{\\alpha}n}\\partial \_{n}\\partial \_{\\bar{\\alpha}} \\\ &\\quad=- \\frac{\\varphi ^{\\bar{\\alpha}\\gamma}\\varphi \_{ \\gamma}z\_{n}}{F} \\left ( \\frac{x^{2}}{z\_{n}}\\partial \_{x} -\\frac{i}{2z\_{n}}\\partial \_{\\theta} \\right )(\\partial \_{\\bar{\\alpha}} - x^{2}\\varphi \_{\\bar{\\alpha}} \\partial \_{x}) \\\ &\\quad= -\\frac{x^{2}}{F}\\varphi ^{\\bar{\\alpha}\\gamma}\\varphi \_{ \\gamma} \\partial ^{2}\_{x\\bar{\\alpha}}+\\frac{Q}{F}(x^{4}\\partial ^{2}\_{xx} +2x^{3} \\partial \_{x})-\\frac{ix^{2}Q\\partial ^{2}\_{x\\theta} }{2F}+ \\frac{i\\varphi ^{\\bar{\\alpha}\\gamma} \\varphi \_{\\gamma }\\partial ^{2}\_{ \\bar{\\alpha}\\theta}}{F} \\\ &\\quad= s^{-\\frac{1}{n}} H\_{1}(x\_{\\alpha}, y\_{\\alpha}, \\partial ^{2}\_{s \\bar{\\alpha}}, \|b\|^{\\frac{1}{n+1}} \\partial ^{2}\_{ss},\|b\|^{ \\frac{1}{n+1}} \\partial \_{s}, \\partial ^{2}\_{s\\theta}, \|b\|^{- \\frac{1}{n+1}} \\partial ^{2}\_{\\bar{\\alpha}\\theta})\\\ &\\qquad{}+O(b^{n+1}\\tau )+O(s^{ \\frac{n+1}{n}}), \\end{aligned} \\end{aligned}

(2.169)


\\begin{aligned} \\begin{aligned} &g^{\\bar{\\beta}\\alpha}\\partial \_{\\alpha }\\partial \_{\\bar{\\beta}} \\\ &\\quad= - \\frac{\\varphi ^{\\bar{\\beta}\\alpha}}{F}(\\partial \_{z\_{\\alpha}} - x^{2} \\varphi \_{\\alpha }\\partial \_{x})(\\partial ^{2}\_{\\bar{\\beta}} - x^{2} \\varphi \_{\\bar{\\beta}} \\partial \_{x}) \\\ &\\quad=-\\frac{\\varphi ^{\\bar{\\beta}\\alpha}}{F}\\partial ^{2}\_{\\alpha \\bar{\\beta}} +(n-1)\\frac{x^{2}\\partial \_{x}}{F} + \\frac{x^{2}\\varphi ^{\\bar{\\beta}\\alpha}(\\varphi \_{\\alpha }\\partial ^{2}\_{x\\bar{\\beta}} + \\varphi \_{\\bar{\\beta}} \\partial ^{2}\_{x\\alpha})}{F} \\\ &\\qquad{}-\\frac{Q (x^{4}\\partial ^{2}\_{xx} +2x^{3} \\partial \_{x})}{F} \\\ &\\quad= \|b\|^{-\\frac{1}{n+1}}s^{-\\frac{1}{n}}T + (n-1)\\left (\\frac{n}{n+1} \\right )^{-\\frac{1}{n}} c(n)^{-\\frac{n+1}{n}} s^{-\\frac{1}{n}} \\partial \_{s} \\\ &\\qquad{}+ s^{-\\frac{1}{n}} H\_{2}(x\_{\\alpha}, y\_{\\alpha}, \\partial ^{2}\_{s \\alpha}, \\partial ^{2}\_{s \\bar{\\beta}}, \|b\|^{\\frac{1}{n+1}} \\partial ^{2}\_{ss}, \|b\|^{\\frac{1}{n+1}} \\partial \_{s}) +O(b^{n+1}\\tau )+O(s^{ \\frac{n+1}{n}}), \\end{aligned} \\end{aligned}

(2.170)


where _H_ 1, _H_ 2 are smooth in _x_ _α_, _y_ _α_ and linear homogeneous with respect to their differential operator arguments. As \\Delta \_{\\omega \_{T}} is a real operator, all terms with an _i_ must cancel out. In addition, the terms

\\begin{aligned} \\frac{Q}{F}(x^{4} \\partial ^{2}\_{xx} + 2 x^{3} \\partial \_{x}) \\end{aligned}

(2.171)


in ( [2.168](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ171))–( [2.170](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ173)) cancel out. So the terms \|b\|^{\\frac{1}{n+1}} \\partial ^{2}\_{ss}, \|b\|^{\\frac{1}{n+1}} \\partial \_{s} in _H_ 1, _H_ 2 cancel out as well. □

Let us also note the following formulas for later use. By repeatedly differentiating ( [2.164](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ167))–( [2.165](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ168)), we may prove inductively that, when _k_ >2, there are some constants _C_ _j_, _l_ such that

\\begin{aligned} \\begin{aligned} &\\psi ^{(k)}\_{T}(\\eta T)\\\ &\\quad=\\sum \_{j=-(k-2)}^{n(k-2)}\\sum \_{l=1}^{k-1} \\frac{C\_{j,l}e^{l(\\psi \_{T}(\\eta T)+a)}}{(\\psi '\_{T}(\\eta T))^{n-1+j}} \\\ &\\quad=\\sum \_{j=-(k-2)}^{n(k-2)}\\sum \_{l=1}^{k-1} \\frac{C\_{j,l}\|b\|^{l}e^{l(\\psi \_{T}(\\eta T)-\\psi \_{T}(T))}}{(\\psi '\_{T}(\\eta T))^{n-1+j}} \\\ &\\quad=\\sum \_{j=-(k-2)}^{n(k-2)}\\sum \_{l=1}^{k-1}C\_{n,j,l}\|b\|^{l- \\frac{n-1+j}{n+1}}s^{\\frac{1-n-j}{n}}\\left (c(n)^{\\frac{1-n}{n}} +O(\|b\|^{ \\frac{1}{n+1}}\\tau ) +O(s^{\\frac{n+1}{n}})\\right ). \\end{aligned} \\end{aligned}

(2.172)


The following lemma about the shape of the volume form of _ω_ _T_ is also an easy consequence of the computations in this section.

### Lemma 2.31

Write s = 1- \\frac{t}{T} as before. Then for every _η_ ∈(0,1) we have that

\\begin{aligned} \\omega \_{T}^{n}\|\_{t=\\eta T} = \|T\|^{-n} \\mu \_{T}(1-\\eta )\\, ds \\wedge d \\theta \\wedge d{\\mathrm{Vol}}\_{E}, \\end{aligned}

(2.173)


where the radial volume density \\mu \_{T}: (0,1) \\to \\mathbb{R}^{+} satisfies the following properties:

(1):

There are constants _e_( _n_), _e_′( _n_)>0 with _e_( _n_)⩽ _μ_ _T_(1− _η_)⩽ _e_′( _n_) _η_ −( _n_ +1) for all _η_, _T_.

(2):

_μ_ ∞:=lim_T_ →−∞ _μ_ _T_ exists pointwise and is smooth.

(3):

_μ_ ∞( _s_)→ _const_ >0 as _s_ →0+ and _η_ _n_ +1 _μ_ ∞(1− _η_)→ _const_ >0 as _η_ →0+.

### Proof

From the Kähler-Einstein equation, it is straightforward to see that

\\begin{aligned} \\omega \_{T}^{n}\|\_{t=\\eta T} = e''(n) \|T\|^{-n} e^{\\psi \_{T}(\\eta T) - \\psi \_{T}(T)} ds \\wedge d\\theta \\wedge d{\\mathrm{Vol}}\_{E} \\end{aligned}

(2.174)


for some constant _e_″( _n_)>0\. For item (1), we use ( [2.120](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ123)) to estimate

\\begin{aligned} \\begin{aligned} 0 \\leqslant \\psi \_{T}(\\eta T) - \\psi \_{T}(T) &\\leqslant \\psi \_{cusp}(\\eta T) + C - \\psi \_{T}(T) \\\ &\\leqslant -(n+1)\\log \\eta - (n+1)\\log (-T) + C - \\psi \_{T}(T) \\\ &\\leqslant -(n+1)\\log \\eta + C. \\end{aligned} \\end{aligned}

(2.175)


For items (2) and (3), we use the more precise formula ( [2.127](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ130)), which is valid for all _η_ ∈(0,1). This tells us that _ψ_ _T_( _ηT_)− _ψ_ _T_( _T_) has a pointwise limit as _T_ →−∞, which is a smooth function of _η_ and which moreover differs from −( _n_ +1)log _η_ + _C_ by _O_( _η_ _n_ +1) as _η_ →0+. This also establishes the limit as _η_ →0+ in item (3). For the limit as _s_ →0+ in item (3), we can instead look at ( [2.162](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ165)). □

#### 2.4.3 Estimates asymptotically close to the Tian-Yau end (orange region)

Recall from Remark [2.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar35) that the orange gluing region takes the form _t_ ∈\[ _T_ + _T_ 0, _T_ +2 _T_ 0\] for some positive _T_ 0 depending on _σ_ such that _T_ 0→+∞ but _T_ 0/ _T_ →0− as _b_ →0−. From now on we fix an _α_ ∈(0,1) and set

\\begin{aligned} T\_{0} := \|T\|^{\\alpha}. \\end{aligned}

(2.176)


In this section we will prove decay estimates for the difference of the Tian-Yau metric and the neck metric _ω_ _T_ in the orange region. We slightly abuse notation by writing

\\begin{aligned} \\psi \_{\\mathcal{C}}(t) = \\frac{n}{n+1}(t-T)^{\\frac{n+1}{n}} \\end{aligned}

(2.177)


for the Calabi model potential shifted by _T_. We also set

\\begin{aligned} \\mathfrak{c} := n^{\\frac{1}{n}}. \\end{aligned}

(2.178)


We wish to glue _ω_ _T_ with \\mathfrak{c} \|b\|^{\\frac{1}{n}} \\omega \_{\\mathcal{C}}. To this end, we introduce the error term

\\begin{aligned} E(t):= \\psi \_{T}(t) - \\psi \_{T}(T) - \\mathfrak{c} \|b\|^{\\frac{1}{n}} \\psi \_{\\mathcal{C}}. \\end{aligned}

(2.179)


Notice that

\\begin{aligned} \\int \_{\\psi \_{T}(T)}^{\\psi \_{T}(t)} (e^{\\xi +a}+b )^{-\\frac{1}{n+1}}d \\xi = (n+1)^{\\frac{1}{n+1}}(t-T). \\end{aligned}

(2.180)


Taking _s_ = _ξ_ − _ψ_ _T_( _T_), we have that for _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\],

\\begin{aligned} \\int \_{0}^{\\psi \_{T}(t)-\\psi \_{T}(T)} (e^{s}-1 )^{-\\frac{1}{n+1}}ds = (n+1)^{ \\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(t-T) = O(T\_{0}\|T\|^{-1}). \\end{aligned}

(2.181)


Then _ψ_ _T_( _t_)− _ψ_ _T_( _T_)= _o_(1) as _T_ →−∞. When _s_ is small,

\\begin{aligned} (e^{s} -1)^{-\\frac{1}{n+1}} = s^{-\\frac{1}{n+1}} +O(s^{\\frac{n}{n+1}}). \\end{aligned}

(2.182)


We have that

\\frac{n+1}{n}(\\psi \_{T}(t)-\\psi \_{T}(T))^{\\frac{n}{n+1}}(1 +O(\\psi \_{T}(t)- \\psi \_{T}(T))) = (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(t-T).

(2.183)


In sum, for _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\],

\\begin{aligned} \\psi \_{T}(t)-\\psi \_{T}(T) = \\mathfrak{c}\|b\|^{\\frac{1}{n}}\\psi \_{ \\mathcal{C}} + O(\|b\|^{\\frac{2}{n}}T\_{0}^{\\frac{2(n+1)}{n}}), \\end{aligned}

(2.184)


which shows that

\\begin{aligned} E(t) = O(\|b\|^{\\frac{2}{n}}T\_{0}^{\\frac{2(n+1)}{n}}). \\end{aligned}

(2.185)


We can actually expand _E_( _t_) in terms of powers of \|b\|^{\\frac{1}{n}}\\psi \_{\\mathcal{C}} up to any finite order. For example,

\\begin{aligned} E(t) = \\frac{\\mathfrak{c}^{2}}{4n+2} \|b\|^{\\frac{2}{n}} \\psi \_{ \\mathcal{C}}^{2} + O(\|b\|^{\\frac{3}{n}}\\psi \_{\\mathcal{C}}^{3})\\;\\, \\text{as}\\;\\,\|b\|^{\\frac{1}{n}}\\psi \_{\\mathcal{C}} \\to 0. \\end{aligned}

(2.186)


More precisely, we have the following statement.

### Lemma 2.32

_E_( _t_) is an analytic function of \|b\|^{\\frac{1}{n}} (t-T)^{\\frac{n+1}{n}} at \|b\|^{\\frac{1}{n}} (t-T)^{\\frac{n+1}{n}}=0.

### Proof

Applying the Maclaurin series of _e_ _s_,

\\begin{aligned} (e^{s} -1)^{-\\frac{1}{n+1}}= s^{-\\frac{1}{n+1}} \\left (\\sum \_{i=0}^{ \\infty }\\frac{s^{i}}{(i+1)!}\\right )^{-\\frac{1}{n+1}}= s^{- \\frac{1}{n+1}} \\sum \_{i=0}^{\\infty }a\_{i} s^{i}, \\end{aligned}

(2.187)


where _a_ 0=1 and _C_ _i_ _a_ _i_→0 for some _C_ >0\. Indeed, \\left (\\frac{e^{s}-1}{s}\\right )^{-\\frac{1}{n+1}} is analytic at _s_ =0\. By ( [2.181](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ184)),

\\begin{aligned} \\sum \_{i=0}^{\\infty }\\tilde{a}\_{i} (\\psi \_{T}(t)-\\psi \_{T}(T))^{i+ \\frac{n}{n+1}} = (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(t-T), \\end{aligned}

(2.188)


where again \\tilde{a}\_{0}>0 and C^{i} \\tilde{a}\_{i} \\rightarrow 0 for some _C_ >0\. Taking the \\frac{n+1}{n}-th power of both sides, we get

\\begin{aligned} (\\psi \_{T}(t) - \\psi \_{T}(T))\\left (\\sum \_{i=0}^{\\infty }\\tilde{a}\_{i} (\\psi \_{T}(t)-\\psi \_{T}(T))^{i}\\right )^{\\frac{n+1}{n}} = (n+1)^{ \\frac{1}{n}}\|b\|^{\\frac{1}{n}}(t-T)^{\\frac{n+1}{n}}. \\end{aligned}

(2.189)


The left-hand side is obviously analytic in _ψ_ _T_( _t_)− _ψ_ _T_( _T_) around _ψ_ _T_( _t_)− _ψ_ _T_( _T_)=0\. Then the lemma follows from the Lagrange inversion theorem. □

Lastly, we estimate the derivatives of i\\partial \\overline {\\partial }E under the scaled Calabi metric \|b\|^{\\frac{1}{n}}\\omega \_{\\mathcal{C}}. For this we need one more lemma establishing quasi-coordinates for this metric. Following our work after Lemma [2.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar36), we define real coordinates on the universal cover of the annulus { _y_:= _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\]} via

\\begin{aligned} (\\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{y}, \\check{\\theta}) := (T\_{0}^{ \\frac{1}{2n}}x\_{\\alpha}, T\_{0}^{\\frac{1}{2n}} y\_{\\alpha}, T\_{0}^{ \\frac{1-n}{2n}} y, T\_{0}^{\\frac{1-n}{2n}} \\theta ). \\end{aligned}

(2.190)


We also introduce the corresponding holomorphic coordinates, with _w_ =log _z_ _n_:

\\begin{aligned} (\\check{z}\_{\\alpha}, \\check{w}) := (T\_{0}^{\\frac{1}{2n}} z\_{\\alpha}, T\_{0}^{ \\frac{1-n}{2n}} w). \\end{aligned}

(2.191)


### Lemma 2.33

The un-scaled Calabi metric \\omega \_{\\mathcal{C}} is uniformly equivalent to ( _δ_ _jk_) under ( [2.190](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ193))–( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)). For all _k_ ⩾1 its entries under ( [2.190](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ193))–( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)) satisfy a uniform _C_ _k_ bound independent of _T_, _T_ 0.

### Proof

Because _w_ =log _z_ _n_, we locally have that

\\begin{aligned} t =\\log h = -\\varphi + w + \\overline{w}. \\end{aligned}

(2.192)


This implies that

\\begin{aligned} \\begin{aligned} \\omega \_{\\mathcal{C}}& = \\frac{n}{n+1} i\\partial \\overline{\\partial} (t- T)^{\\frac{n+1}{n}} = \\frac{1}{n} (t-T)^{\\frac{1-n}{n}} i\\partial t \\wedge \\overline{\\partial} t +(t-T)^{\\frac{1}{n}}i\\partial \\overline{\\partial} t \\\ &= \\frac{1}{n} (t-T)^{\\frac{1-n}{n}} i\\partial (-\\varphi +w) \\wedge \\overline{\\partial} (-\\varphi +\\overline{w}) -(t-T)^{\\frac{1}{n}}i \\partial \\overline{\\partial} \\varphi , \\end{aligned} \\end{aligned}

(2.193)


where _φ_ is a quadratic polynomial in z\_{\\alpha}, \\overline{z}\_{\\alpha} for _α_ =1,…, _n_ −1\. Under the coordinates (\\check{z}\_{\\alpha}, \\check{w}) given in ( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)), it follows that

\\begin{aligned} \\begin{aligned} \\omega \_{\\mathcal{C}} &= \\frac{1}{n} ((t-T)T\_{0}^{-1})^{\\frac{1-n}{n}} i(-T\_{0}^{-\\frac{1}{2}}\\varphi \_{z\_{\\alpha}} d\\check{z}\_{\\alpha }+d \\check{w}) \\wedge (-T\_{0}^{-\\frac{1}{2}}\\varphi \_{\\overline{z}\_{\\alpha}}d \\overline{{\\check{z}}}\_{\\alpha}+d \\overline {\\check{w}}) \\\ & -((t-T)T\_{0}^{-1})^{\\frac{1}{n}}\\varphi \_{z\_{\\alpha}\\overline{z}\_{ \\beta}}id\\check{z}\_{\\alpha }\\wedge d\\overline{\\check{z}}\_{\\beta}. \\end{aligned} \\end{aligned}

(2.194)


This is uniformly equivalent to the Euclidean metric in the chart ( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)) for _y_ = _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\]. To check the desired _C_ _k_ bound for _k_ =1, note that \\varphi \_{z\_{\\alpha}\\overline{z}\_{\\beta}} is a constant, that \\varphi \_{\\overline{z}\_{\\alpha}} satisfies

\\begin{aligned} \\frac{\\partial \\varphi \_{\\overline{z}\_{\\alpha}}}{\\partial \\check{z}\_{\\beta}} = T\_{0}^{-\\frac{1}{2n}} \\frac{\\partial \\varphi \_{\\overline{z}\_{\\alpha}}}{\\partial z\_{\\beta}} =T\_{0}^{- \\frac{1}{2n}}\\varphi \_{z\_{\\beta}\\overline{z}\_{\\alpha}}, \\end{aligned}

(2.195)


and that, by ( [2.192](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ195)),

\\begin{aligned} \\frac{\\partial ((t-T)T\_{0}^{-1})}{\\partial \\check{w}} = T\_{0}^{ \\frac{n-1}{2n}} \\frac{\\partial ( (t-T)T\_{0}^{-1})}{\\partial w} =T\_{0} ^{- \\frac{n+1}{2n}}. \\end{aligned}

(2.196)


Thus, the first coordinate derivatives of \\omega \_{\\mathcal{C}} are uniformly decaying. This pattern persists for all _k_. □

### Proposition 2.34

For _t_ ∈\[ _T_ + _T_ 0, _T_ +2 _T_ 0\] and _j_ =1,2,

\\left \| \\nabla ^{j}\_{\|b\|^{\\frac{1}{n}}\\omega \_{\\mathcal {C}}} (i\\partial \\overline{\\partial} E)\\right \|^{2}\_{\|b\|^{\\frac{1}{n}}\\omega \_{\\mathcal {C}}} \\leqslant C\|b\|^{\\frac{2-j}{n}}T\_{0}^{\\frac{(2-j)(n+1)}{n}}.

(2.197)


### Proof

Define _y_:= _t_ − _T_. By deriving the Taylor expansion of _ψ_ _T_( _t_)− _ψ_ _T_( _T_) with respect to \|b\|^{\\frac{1}{n}}y^{\\frac{n+1}{n}} using ( [2.183](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ186)), we obtain that for _y_ ∈\[ _T_ 0,2 _T_ 0\] and _j_ ⩾0,

\\begin{aligned} \|(y\\partial \_{t})^{j} E(t)\|\\leqslant C\_{j} \|b\|^{\\frac{2}{n}}T\_{0}^{ \\frac{2(n+1)}{n}}, \\end{aligned}

(2.198)


where the constants _C_ _j_ are independent of _b_.

Recall the real chart (\\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{y}, \\check{\\theta}) and the holomorphic chart (\\check{z}\_{\\alpha}, \\check{w}) on the universal cover of the annulus { _y_ ∈\[ _T_ 0,2 _T_ 0\]} defined in ( [2.190](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ193))–( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)) above. By Lemma [2.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar52), these are quasi-coordinates for \\omega \_{\\mathcal{C}}, i.e., the pullback of \\omega \_{\\mathcal{C}} to the universal cover is uniformly smoothly comparable to the Euclidean metric in these coordinates and its _C_ _k_ norms are bounded independently of _T_ 0.

Now we are ready to estimate the derivatives of i\\partial \\overline{\\partial} E. In fact,

\\begin{aligned} \\begin{aligned} i\\partial \\overline{\\partial} E = E' i\\partial \\overline{\\partial} t +E'' i\\partial t \\wedge \\overline{\\partial} t =-E' i\\partial \\overline{\\partial} \\varphi + E''i (\\partial \\varphi - \\partial w) \\wedge (\\overline{\\partial}\\varphi - \\overline{\\partial} \\overline{w}), \\end{aligned} \\end{aligned}

(2.199)


where

\\begin{aligned} T\_{0}^{\\frac{1}{n}}i\\partial \\overline{\\partial} \\varphi , \\quad T\_{0}^{ \\frac{1-n}{n}}i(\\partial \\varphi - \\partial w)\\wedge ( \\overline{\\partial}\\varphi - \\overline{\\partial} \\overline{w}) \\end{aligned}

(2.200)


are uniformly smoothly bounded under ( [2.191](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ194)). So we need to check the regularity of

\\begin{aligned} E'/T\_{0}^{\\frac{1}{n}}, \\quad E''/T\_{0}^{\\frac{1-n}{n}}. \\end{aligned}

(2.201)


Because these are radial functions, we just need to check the derivatives of ( [2.201](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ204)) with respect to \\check{y}. Applying ( [2.198](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ201)), we obtain that

\\begin{aligned} \\left \|\\frac{\\partial (E'/T\_{0}^{\\frac{1}{n}})}{\\partial \\check{y}} \\right \|+\\left \| \\frac{\\partial (E''/T\_{0}^{\\frac{1-n}{n}})}{\\partial \\check{y}}\\right \| \\leqslant C\|b\|^{\\frac{2}{n}}T\_{0}^{\\frac{n+1}{2n}}, \\end{aligned}

(2.202)


\\begin{aligned} \\left \| \\frac{\\partial ^{2} (E'/T\_{0}^{\\frac{1}{n}})}{\\partial \\check{y}^{2}} \\right \| + \\left \| \\frac{\\partial ^{2} (E''/T\_{0}^{\\frac{1-n}{n}})}{\\partial \\check{y}^{2}} \\right \| \\leqslant C\|b\|^{\\frac{2}{n}}. \\end{aligned}

(2.203)


We conclude that the 2-form i\\partial \\overline{\\partial} E satisfies for _j_ =1,2 that

\\begin{aligned} \\left \| \\nabla ^{j}\_{\\omega \_{\\mathcal {C}}} (i\\partial \\overline{\\partial} E) \\right \|\_{\\omega \_{\\mathcal {C}}} \\leqslant C\|b\|^{\\frac{2}{n}}T\_{0}^{\\frac{n+1}{2n}(2-j)}. \\end{aligned}

(2.204)


Now the metric \|b\|^{\\frac{1}{n}}\\omega \_{\\mathcal {C}} in the statement of the proposition is simply a rescaling of \\omega \_{\\mathcal {C}}. If \\tilde{\\omega}= A \\omega  for some constant _A_ >0, then for any 2-form **T**,

\\begin{aligned} \|\\nabla ^{j}\_{\\tilde{\\omega}} \\mathbf{T} \|^{2}\_{\\tilde{\\omega}} = A^{-2-j} \|\\nabla ^{j}\_{ \\omega} \\mathbf{T} \|^{2}\_{\\omega}. \\end{aligned}

(2.205)


The proposition follows from ( [2.204](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ207))–( [2.205](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ208)). □

## 3 The glued approximate Kähler-Einstein metric

### 3.1 Setting up the glued metric and the Monge-Ampère equation

Before defining the glued metric, we briefly review some material from previous sections and fix some parameters.

First, we have a family of Tian-Yau spaces _TY_ _σ_ as our singularity models, see ( [2.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ9)). We have smooth embeddings \\Phi \_{\\sigma}: TY\_{0}\\setminus \\overline{B}\_{\|\\sigma \|^{1/3}R} \\to TY\_{ \\sigma} onto a neighborhood of infinity in _TY_ _σ_ for _σ_ ≠0, see ( [2.73](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ76)). In Sect. [2.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec8) we review the Tian-Yau construction (\\psi \_{TY\_{1}},\\omega \_{TY\_{1}},\\Omega \_{TY\_{1}}) on _TY_ 1 and its decay towards the Calabi model data (\\psi \_{\\mathcal{C}},\\omega \_{\\mathcal {C}},\\Omega \_{\\mathcal {C}}) on _TY_ 0 via Φ1. This gives rise to a family (\\psi \_{TY\_{\\sigma}},\\omega \_{TY\_{\\sigma}},\\Omega \_{TY\_{\\sigma}}) via the biholomorphism _m_ _σ_: _TY_ _σ_→ _TY_ 1 of ( [2.73](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ76)). A tricky point here is that, in the Tian-Yau construction, there is a unique choice of a Hermitian metric _h_ on the line bundle such that the Calabi model potential \\psi \_{\\mathcal{C}} defined using _h_ (see ( [2.65](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ68))) differs from \\psi \_{TY\_{1}} by an exponentially decaying term. We shall fix this choice of _h_, i.e., no rescalings of _h_ are allowed. Another point that we hope will aid clarity is that we are not allowing any rescalings of \\Omega \_{\\mathcal{C}}. This also fixes the scale of \\omega \_{\\mathcal{C}} because \\omega ^{2}\_{\\mathcal {C}}=\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}.

Secondly, we have a family of canonically polarized surfaces \\mathcal {X}\_{\\sigma }\\subset \\mathbb{CP}^{3} and hyperplane sections \\mathcal{D}\_{\\sigma} with \[2\\mathcal{D}\_{\\sigma}\] = K\_{\\mathcal {X}\_{\\sigma}}, see ( [2.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ4)) and ( [2.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ8)). We have a family of algebraic holomorphic volume forms Ω_σ_ on the affine surfaces \\mathcal {Y}\_{\\sigma}=\\mathcal {X}\_{\\sigma}\\setminus \\mathcal{D}\_{\\sigma}, which are unique up to scaling (Remark [2.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar2)). On the regular part of \\mathcal {Y}\_{0}, i.e., on the complement of the origin, we have a Kähler-Einstein metric \\omega \_{KE,0}=i\\partial \\overline {\\partial }\\psi \_{KE,0} with e^{-\\psi \_{KE,0}}\\omega ^{2}\_{KE,0}=\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0} (Lemma [2.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar15)). We remark that the additive normalization of _ψ_ _KE_,0 depends on the choice of a scale of Ω0, which we will fix in a moment.

Third, we fix a local holomorphic identification Ψ_σ_ of _TY_ _σ_ and \\mathcal {X}\_{\\sigma}, see ( [2.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ12)). By Lemma [2.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar19), by a suitable (unique) rescaling of Ω0 we can achieve that (\\Psi \_{0}^{-1})^{\*}(\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0})=(1+O(e^{ \\frac{t}{2}}))({\\Omega \_{\\mathcal {C}}}\\wedge \\overline{\\Omega}\_{ \\mathcal {C}}) as _t_ =log _h_ →−∞. We remark that there is no scaling ambiguity for Ω_σ_ any more since Ω0 is fixed. To get rid of the term -3 \\log (1-\\mathfrak{s}/t) in the expansion of (\\Psi \_{0}^{-1})^{\*}\\psi \_{KE,0}-\\psi \_{cusp}, we have to compose Ψ_σ_ with scale\_{e^{-{\\mathfrak{s}}}}, but it is harmless for our purposes to assume directly that \\mathfrak{s} = 0 (see Remark [2.15](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar24)). Thus we achieve that (\\Psi \_{0}^{-1})^{\*}\\psi \_{KE,0} - \\psi \_{cusp} = O(e^{-\\delta \_{0} \\sqrt{-t}}) as _t_ →−∞ for some _δ_ 0>0\. Here, _ψ_ _cusp_ has already been normalized by adding a constant such that e^{-\\psi \_{cusp}}\\omega \_{cusp}^{2}=\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}. The same relation holds for the horn metrics ( _ψ_ _T_, _ω_ _T_) of Sect. [2.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec9) instead of ( _ψ_ _cusp_, _ω_ _cusp_).

We review the relations between different parameters. The position of the horn is fixed via

\\begin{aligned} T := \\frac{2}{3}\\log \|\\sigma \|. \\end{aligned}

(3.1)


This is motivated by the discussion in Sect. [1.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec4). By ( [2.132](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ135)), the parameter _b_ <0 satisfies that \| _b_ \| is uniformly comparable to \| _T_ \|−3. Our preferred radius coordinate _t_ =log _h_ differs from log\| _z_ \|2 by a uniformly bounded function, see again the discussion before ( [1.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ3)). Here, \| _z_ \| is the standard radius in \\mathbb{C}^{3}, where _TY_ _σ_ and \\mathcal{Y}\_{\\sigma} are embedded by definition. Thus, \| _σ_ \|\| _z_ \|−3 is comparable to _e_ −(3/2)( _t_ − _T_).

The orange gluing region, where the end of the Tian-Yau space is attached to the left end of the new neck, is parametrized by _t_ ∈\[ _T_ + _T_ 0, _T_ +2 _T_ 0\] (see Fig. [2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Fig2) and Remark [2.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar35)). Here, as in ( [2.176](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ179)),

\\begin{aligned} T\_{0} := \|T\|^{\\alpha}\\;\\,\\text{for some fixed}\\;\\,\\alpha \\in (0,1). \\end{aligned}

(3.2)


The limit _α_ →1 corresponds to the naive gluing of the cusp metric and the Tian-Yau metric described after ( [1.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ3)), whereas in this paper we will always fix _α_ to be arbitrarily close to zero. It is also worth noting that we do not glue with the Tian-Yau metric normalized exactly as above but, rather, with a scaled copy of it, where the scaling factor \\mathfrak{c} equals \\sqrt{2} for _n_ =2; see ( [2.178](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ181)). We could have hidden this factor in our normalization of \\Omega \_{\\mathcal{C}}, but we chose not to do so because \\mathfrak{c} appears much later in the paper than \\Omega \_{\\mathcal{C}}, and a lot of other choices depend on the initial choice of \\Omega \_{\\mathcal{C}}.

Lastly, the green gluing region between the neck and the cusp is parametrized by _t_ ∈\[2 _τ_, _τ_\] (see Remark [2.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar35)). The only requirement so far was that _τ_/ _T_ →0 as _σ_ →0\. We now fix _τ_ such that

\\begin{aligned} \|b\|\|\\tau \|^{3} = e^{-\\delta \_{0}\\sqrt{-\\tau}}, \\end{aligned}

(3.3)


hence in particular _τ_ ∼−((3/ _δ_ 0)log\| _T_ \|)2. This is the classical choice of making the two gluing errors on the left side and on the right side of the gluing region comparable to each other (( [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ219)), line 3).

### Definition 3.1

We now define our glued approximate Kähler-Einstein metric _ω_ _glue_, _σ_ on \\mathcal{X}\_{\\sigma}. On the affine surface \\mathcal{Y}\_{\\sigma }= \\mathcal{X}\_{\\sigma }\\setminus \\mathcal{D}\_{ \\sigma} we set \\omega \_{glue,\\sigma} := i\\partial \_{\\sigma}\\overline {\\partial }\_{\\sigma}\\psi \_{glue,\\sigma}, where _ψ_ _glue_, _σ_ is defined as follows. We need to distinguish 7 different regions \\mathfrak{R}\_{1}, \\ldots , \\mathfrak{R}\_{7}; see Table [1](https://link.springer.com/article/10.1007/s00039-025-00708-y#Tab1) and Fig. [3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Fig3). We begin by setting

\\psi \_{glue,\\sigma}:=\\psi \_{FS,\\sigma}+(G\_{\\sigma}^{-1})^{\*}\\psi \_{0} \\;\\,\\text{on}\\;\\,\\mathfrak{R}\_{1} := \\Psi \_{\\sigma}^{-1}(\\Phi \_{\\sigma}( \\{t>-N\\})) \\cup (\\mathcal{Y}\_{\\sigma }\\setminus {\\mathrm{dom}}\\,\\Psi \_{ \\sigma}).

(3.4)


Here _ψ_ _FS_, _σ_ was defined in ( [2.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ34)), _ψ_ 0= _ψ_ _KE_,0− _ψ_ _FS_,0 (Lemma [2.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar14)), and _G_ _σ_ is the _C_ 5 diffeomorphism from Lemma [2.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar10), while _N_ is an arbitrary but fixed large positive constant such that Φ_σ_({ _t_ <− _N_/2}) is contained in {\\mathrm{dom}}\\,\\Psi \_{\\sigma}^{-1}. Clearly _ω_ _glue_, _σ_ is then at least _C_ 3 at the divisor \\mathcal{D}\_{\\sigma}.

**Figure 3**

![Figure 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00039-025-00708-y/MediaObjects/39_2025_708_Fig3_HTML.png)

[Full size image](https://link.springer.com/article/10.1007/s00039-025-00708-y/figures/3)

The seven regions of \\mathcal{X}\_{\\sigma}. For the middle neck \\mathfrak{R}\_{4} see also Fig. [2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Fig2). (Color figure online.)

**Table 1 Properties of _ω_ _glue_, _σ_. The estimates are sharp up to constant factors.**

[Full size table](https://link.springer.com/article/10.1007/s00039-025-00708-y/tables/1)

For the remaining 6 regions we prefer to write down formulas for (\\Psi ^{-1}\_{\\sigma})^{\*}\\psi \_{glue,\\sigma} on _TY_ _σ_ rather than for _ψ_ _glue_, _σ_ on \\mathcal{X}\_{\\sigma}. To this end, let _χ_ 1( _t_) be smooth and increasing with _χ_ 1( _t_)=0 for _t_ ⩽ _T_ + _T_ 0 and _χ_ 1( _t_)=1 for _t_ ⩾ _T_ +2 _T_ 0, and with \|\\partial \_{t}^{j}\\chi \_{1}\| = O\_{j}(T\_{0}^{-j}) for all _j_ ⩾0\. Similarly, let _χ_ 2( _t_) be smooth and increasing with _χ_ 2( _t_)=0 for _t_ ⩽2 _τ_ and _χ_ 2( _t_)=1 for _t_ ⩾ _τ_, and with \|\\partial \_{t}^{j}\\chi \_{2}\| = O\_{j}(\|\\tau \|^{-j}) for all _j_ ⩾0\. Then the desired formulas for (\\Psi ^{-1}\_{\\sigma})^{\*}\\psi \_{glue,\\sigma} are as follows:

\\begin{aligned} \\begin{aligned} &(\\Psi ^{-1}\_{\\sigma})^{\*}\\psi \_{FS,\\sigma}+((\\Psi \_{\\sigma}\\circ G\_{ \\sigma})^{-1})^{\*}\\psi \_{0} \\\ &\\quad\\text{on}\\;\\,\\Psi \_{\\sigma}( \\mathfrak{R}\_{2}) := \\Phi \_{\\sigma}(\\{\\tau < t< -N\\}), \\\ &(\\Phi \_{\\sigma}^{-1})^{\*}\\Big(\\chi \_{2}(\\Psi ^{-1}\_{0})^{\*}(G\_{\\sigma}^{\*} \\psi \_{FS,\\sigma}+\\psi \_{0})+(1-\\chi \_{2})\\psi \_{T}\\Big)\\\ &\\quad\\text{on}\\;\\,\\Psi \_{\\sigma}(\\mathfrak{R}\_{3}) := \\Phi \_{\\sigma}(\\{2 \\tau < t< \\tau \\}), \\\ &(\\Phi ^{-1}\_{\\sigma})^{\*}\\psi \_{T} \\;\\,\\text{on}\\;\\,\\Psi \_{\\sigma}( \\mathfrak{R}\_{4}) := \\Phi \_{\\sigma}(\\{T+2T\_{0}< t< 2\\tau \\}), \\\ &(\\Phi \_{\\sigma}^{-1})^{\*}\\Big(\\chi \_{1}\\psi \_{T}+(1-\\chi \_{1})\\Phi \_{ \\sigma}^{\*}(\\mathfrak{c}\|b\|^{\\frac{1}{2}}\\psi \_{TY\_{\\sigma}}+\\psi \_{T}(T)) \\Big)\\\ &\\quad\\text{on}\\;\\,\\Psi \_{\\sigma}(\\mathfrak{R}\_{5}) := \\Phi \_{ \\sigma}(\\{T\_{0}< t-T< 2T\_{0}\\}), \\\ &\\mathfrak{c}\|b\|^{\\frac{1}{2}}\\psi \_{TY\_{\\sigma}}+\\psi \_{T}(T)\\;\\, \\text{on}\\;\\,\\Psi \_{\\sigma}(\\mathfrak{R}\_{6}) := \\Phi \_{\\sigma}(\\{t < T+ T\_{0}\\}), \\\ &\\mathfrak{c}\|b\|^{\\frac{1}{2}}\\psi \_{TY\_{\\sigma}}+\\psi \_{T}(T)\\;\\, \\text{on}\\;\\,\\Psi \_{\\sigma}(\\mathfrak{R}\_{7}) := ({\\mathrm{dom}}\\,\\Psi \_{ \\sigma}^{-1})\\setminus ({\\mathrm{im}}\\,\\Phi \_{\\sigma}). \\end{aligned} \\end{aligned}

(3.5)


This concludes our definition of the glued approximate Kähler-Einstein manifold (\\mathcal{X}\_{\\sigma},\\omega \_{glue,\\sigma}).

The Monge-Ampère equation that we want to solve is

(\\omega \_{glue,\\sigma}+i\\partial \\overline {\\partial }u\_{\\sigma})^{2}=e^{u\_{\\sigma}-f\_{\\sigma}} \\omega \_{glue,\\sigma}^{2},

(3.6)


where _f_ _σ_ is the Ricci potential, defined up to a constant by the condition that

\\begin{aligned} {\\mathrm{Ric}}(\\omega \_{glue, \\sigma})+\\omega \_{glue,\\sigma}+i\\partial \\overline {\\partial }f\_{ \\sigma}=0. \\end{aligned}

(3.7)


### Lemma 3.2

Up to an arbitrary constant,

f\_{\\sigma}\|\_{\\mathcal{Y}\_{\\sigma}} = \\log \\left ( \\frac{\\omega \_{glue,\\sigma}^{2}}{\\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma}} \\right )-\\psi \_{glue,\\sigma}.

(3.8)


### Proof

Denote the right-hand side of ( [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ216)) by _g_ _σ_.

### Claim 3.3

_g_ _σ_ extends at least _C_ 3 to \\mathcal{X}\_{\\sigma}.

### Proof of Claim [3.3](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar59)

We know that \\omega \_{glue,\\sigma}^{2} is at least _C_ 3 on \\mathcal{X}\_{\\sigma} and \\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma }= \|H\_{\\mathcal{D}\_{ \\sigma}}\|^{4} \\cdot (\\textit{smooth on $\\mathcal{X}\_{\\sigma}$}), where H\_{\\mathcal{D}\_{\\sigma}} is a defining section of the line bundle \[\\mathcal{D}\_{\\sigma}\] and \|⋅\| is any smooth Hermitian metric on this line bundle. Thus, the log volume ratio in ( [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ216)) is of the form \\log \|H\_{\\mathcal{D}\_{\\sigma}}\|^{-4} + ( \\textit{at least $C^{3}$ on $\\mathcal{X}\_{\\sigma}$}). Finally, since the reference Kähler form _ω_ _FS_, _σ_ represents the Poincaré dual of the divisor class \[2\\mathcal{D}\_{\\sigma}\], we have that \\psi \_{glue,\\sigma}= \\psi \_{FS,\\sigma} + ( \\textit{at least $C^{5}$ on $\\mathcal{X}\_{\\sigma}$}) = \\log \|H\_{ \\mathcal{D}\_{\\sigma}}\|^{-4} + ( \\textit{at least $C^{5}$ on $\\mathcal{X}\_{\\sigma}$}). Thus, the two log terms in the definition of _g_ _σ_ cancel each other out and the remainder is at least _C_ 3. □

From its definition, ( [3.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ215)), and by elliptic regularity, _f_ _σ_ is at least _C_ 2, _α_ on \\mathcal{X}\_{\\sigma}. Hence, by Claim [3.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar59), so is _f_ _σ_− _g_ _σ_. From the definition of _g_ _σ_ and from the standard formula for the Ricci curvature of a Kähler metric, _g_ _σ_ satisfies {\\mathrm{Ric}}(\\omega \_{glue,\\sigma})+\\omega \_{glue,\\sigma}+i\\partial \\overline {\\partial }g\_{ \\sigma}=0 (on \\mathcal{Y}\_{\\sigma} and thus, by Claim [3.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar59), on \\mathcal{X}\_{\\sigma}). Thus, _f_ _σ_− _g_ _σ_ is pluriharmonic on \\mathcal{X}\_{\\sigma} and hence constant. □

Of course, we already know that, given _f_ _σ_, the Monge-Ampère equation ( [3.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ214)) has a unique solution _u_ _σ_ by the Aubin-Yau theorem \[ [Aub78](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR2 " 					Aubin, T.: Équations du type Monge-Ampère sur les variétés Kählériennes compactes. Bull. Sci. Math. 102, 63–95 (1978) 				"), [Yau78](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR40 " 					Yau, S.-T.: On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I. Comm. Pure Appl. Math. 31, 339–411 (1978) 				")\], and if we change _f_ _σ_ by a constant then _u_ _σ_ changes by the same constant. Our main goal in this paper is to prove that _u_ _σ_ is actually small modulo constants, meaning at the very least that \\sup \_{\\mathcal{X}\_{\\sigma}} \|i\\partial \\overline {\\partial }u\_{\\sigma}\|\_{\\omega \_{glue, \\sigma}} \\to 0 as _σ_ →0\. Clearly, the first step here is to prove that _f_ _σ_ is sufficiently small modulo constants, using the expression in ( [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ216)). This estimate is the main result of Sect. [3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec13) and we record it in Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62). To state the theorem, we need one other definition.

### Definition 3.4

The regularity scale function \\mathbf{r}\_{\\sigma}: \\mathcal{X}\_{\\sigma }\\to \\mathbb{R}^{+} of _ω_ _glue_, _σ_ is defined as follows:

\\begin{aligned} \\mathbf{r}\_{\\sigma }:= \\textstyle\\begin{cases} 1 &\\text{on}\\;\\,\\Psi \_{\\sigma}^{-1}(\\Phi \_{\\sigma}(\\{t > T/2\\})) \\cup ( \\mathcal{X}\_{\\sigma }\\setminus {\\mathrm{dom}}\\,\\Psi \_{\\sigma}), \\\ \\Psi \_{\\sigma}^{\*}(\\Phi \_{\\sigma}^{-1})^{\*}\\left (\|b\|^{\\frac{1}{4}}(t-T)^{ \\frac{3}{4}}\\right )&\\text{on}\\;\\,\\Psi \_{\\sigma}^{-1}(\\Phi \_{\\sigma}( \\{t < T/2\\})), \\\ \|b\|^{\\frac{1}{4}} &\\text{on}\\;\\,\\mathfrak{R}\_{7}. \\end{cases}\\displaystyle \\end{aligned}

(3.9)


Up to bounded factors that we suppress, **r** _σ_( _p_) is the maximal radius of an _ω_ _glue_, _σ_-ball _B_ _r_( _p_) such that _r_ −2 _ω_ _glue_, _σ_ is _C_ ∞ bounded in coordinates on the universal cover of _B_ _r_( _p_). In particular, the curvature of _ω_ _glue_, _σ_ is uniformly O(\\mathbf{r}\_{\\sigma}^{-2}). This is the curvature estimate recorded in Table [1](https://link.springer.com/article/10.1007/s00039-025-00708-y#Tab1) and it is sharp.

We are now able to state our main result in this section. The proof is deferred to Sect. [3.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec15).

### Theorem 3.5

_Let_ _f_ _σ_ _be the Ricci potential defined in_ ( [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ216)). _Then for all_ _ε_ >0 _the function_

\|f\_{\\sigma}\|+\\mathbf{r}\_{\\sigma }\|\\nabla \_{\\omega \_{glue,\\sigma}} f\_{ \\sigma}\|\_{\\omega \_{glue,\\sigma}}

(3.10)


_satisfies the following pointwise estimates as_ _σ_ →0:

\\begin{aligned} \\textstyle\\begin{cases} O(\|\\sigma \|) &\\mbox{on }\\mathfrak{R}\_{1}, \\\ O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}) & \\mbox{on }\\mathfrak{R}\_{2}, \\\ O(\|b\|\|\\tau \|^{3}) + O(e^{-\\delta \_{0}\\sqrt{-t}})& \\mbox{on }\\mathfrak{R}\_{3}, \\\ O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})+O(e^{(\\frac{1}{2}-\\varepsilon )t}) & \\mbox{on }\\mathfrak{R}\_{4}, \\\ O((T\_{0}/\|T\|)^{\\frac{3}{2}})& \\mbox{on }\\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6} \\cup \\mathfrak{R}\_{7}. \\end{cases}\\displaystyle \\end{aligned}

(3.11)


_Here we abuse notation by writing_ _t_ _instead of the correct_\\Psi \_{\\sigma}^{\*}(\\Phi \_{\\sigma}^{-1})^{\*}t.

### Remark 3.6

The shape of ( [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ219)) makes sense intuitively: _f_ _σ_ decays faster than any polynomial in \| _T_ \| on \\mathfrak{R}\_{1} \\cup \\mathfrak{R}\_{2} \\cup \\mathfrak{R}\_{4} because _ω_ _glue_, _σ_ is almost an exact solution of the negative Kähler-Einstein equation in these regions. On the other hand, on \\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6} \\cup \\mathfrak{R}\_{7} we are gluing with the scaled Tian-Yau metric, which is Ricci-flat, so up to some additive constant _f_ _σ_ then equals minus the Kähler potential of this metric, whose oscillation is ∼ ( _T_ 0/\| _T_ \|)3/2. The error in the gluing region \\mathfrak{R}\_{3} is also polynomial in \| _T_ \| but it is _O_(\| _T_ \|−3\|log\| _T_ \|\|6), i.e., almost quadratic compared to the error in the Tian-Yau region.

### Remark 3.7

Using only ( [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ219)) and standard facts from the theory of the complex Monge-Ampère equation, one can already deduce quite a bit of information about the solution _u_ _σ_. For example, the maximum principle applied to ( [3.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ214)) immediately yields that

\\begin{aligned} \\sup \\nolimits \_{\\mathcal{X}\_{\\sigma}} \|u\_{\\sigma}\| \\leqslant \\sup \\nolimits \_{\\mathcal{X}\_{\\sigma}} \|f\_{\\sigma}\| = O(\|b\|^{ \\frac{1-\\alpha}{2}}). \\end{aligned}

(3.12)


On \\mathfrak{R}\_{1} \\cup \\mathfrak{R}\_{2} \\cup \\mathfrak{R}\_{3} and on a large portion of the middle neck \\mathfrak{R}\_{4}, the regularity scale **r** _σ_ is uniformly bounded below, i.e., we have uniform _C_ ∞ bounds for _ω_ _glue_, _σ_ on the universal cover of a geodesic ball of definite size centered at any point. Thus, on all of these regions, \|i\\partial \\overline {\\partial }u\_{\\sigma}\|\_{\\omega \_{glue,\\sigma}} = O(\|b\|^{(1-\\alpha )/2}) by combining ( [3.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ220)) and Savin’s small perturbation theorem \[ [Sav07](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR32 " 					Savin, O.: Small perturbation solutions for elliptic equations. Comm. Partial Differential Equations 32, 557–578 (2007) 				"), Thm 1.3\]. This estimate already implies C^{\\infty}\_{loc} convergence of _ω_ _KE_, _σ_ to _ω_ _KE_,0 away from any fixed neighborhood of the origin in \\mathbb{C}^{3}.

On the other hand, moving towards the left boundary of the middle neck \\mathfrak{R}\_{4} and into \\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6} \\cup \\mathfrak{R}\_{7}, the regularity scale **r** _σ_ decays until it reaches its minimum of \| _b_ \|1/4 on the Tian-Yau cap \\mathfrak{R}\_{7}. To be able to apply Savin’s theorem in this situation we would need that \|u\_{\\sigma}\| \\ll \\mathbf{r}\_{\\sigma}^{2}, i.e., \| _u_ _σ_\|≪\| _b_ \|1/2 on \\mathfrak{R}\_{7}. This is obviously out of reach of ( [3.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ220)) no matter how small we make _α_.

The point of the weighted Hölder space theory developed in the rest of the paper (after the proof of Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62)) is precisely to improve the naive _C_ 0 estimate ( [3.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ220)) in the Tian-Yau region. We will for instance be able to prove that \\sup \_{\\mathfrak{R}\_{7}} \|u\_{\\sigma}\| = O\_{\\varepsilon}(\|b\|^{(5/6)- \\varepsilon}) for all _ε_ >0\. This is enough to obtain _C_ 1, _β_ closeness of _ω_ _KE_, _σ_ to the scaled Tian-Yau metric on \\mathfrak{R}\_{7} for all \\beta < \\frac{1}{3}, which in particular proves the Main Theorem. In fact, we conjecture that a more systematic approach to the obstruction theory in Sect. [5.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec40) would even yield \\sup \_{\\mathfrak{R}\_{7}} \|u\_{\\sigma}\| = O\_{\\varepsilon}(\|b\|^{1- \\varepsilon}) and thus _C_ 1, _β_ closeness for all _β_ <1\. This would then be optimal because a Ricci-flat metric cannot be _C_ 1,1 close to a metric with Ricci = −1.

### 3.2 Proof of the Ricci potential estimate

This section is dedicated to the proof of Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62). This will be done at the end of this section, as a consequence of a long sequence of lemmas.

We shall pull back everything back to _TY_ 0 and then estimate.

### Lemma 3.8

On _TY_ 0, the following hold.

(1):

If _t_ ∈\[ _T_ + _T_ 0, _τ_\], one has

\|\\nabla \_{\\omega \_{T}}^{k}(\\Phi ^{\*}\_{\\sigma }J\_{TY\_{\\sigma}}-J\_{\\mathcal {C}})\|\_{ \\omega \_{T}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})\\;\\, \\text{for all} \\;\\, k \\geqslant 0, \\varepsilon > 0.

(3.13)


(2):

If _t_ ∈\[2 _τ_,− _N_\], one has

\|\\nabla \_{\\omega \_{cusp}}^{k}(\\Phi ^{\*}\_{\\sigma }J\_{TY\_{\\sigma}}-J\_{ \\mathcal {C}})\|\_{\\omega \_{cusp}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})\\;\\, \\text{for all} \\;\\, k \\geqslant 0, \\varepsilon > 0.

(3.14)


### Proof

In Lemma [2.18](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar28) we have proved that this holds for the reference metric \|b\|^{1/2}\\omega \_{\\mathcal {C},\\sigma} instead of _ω_ _T_ or _ω_ _cusp_, assuming only that _t_ − _T_ →∞. To compare these reference metrics, we now estimate

\\left \|\\nabla ^{k}\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal{C},\\sigma}} \\omega \_{T}\\right \|\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C},\\sigma}} \\,\\,\\, \\mbox{and}\\,\\,\\,\\left \|\\nabla ^{k}\_{\|b\|^{\\frac{1}{2}}\\omega \_{ \\mathcal{C},\\sigma}}\\omega \_{cusp}\\right \|\_{\|b\|^{\\frac{1}{2}}\\omega \_{ \\mathcal {C},\\sigma}}\\,\\,\\,\\mbox{for all}\\,\\,\\, k \\geqslant 0.

(3.15)


For _δ_ >0 fixed and _t_/ _T_ ⩾1− _δ_, ( [2.164](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ167))–( [2.165](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ168)) say that _ω_ _T_ is uniformly comparable to \|b\|^{1/2}\\omega \_{\\mathcal {C},\\sigma}. For _k_ >0, first notice that by ( [2.172](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ175)), the _t_-derivatives of _ψ_ _T_ blow up at worst polynomially in \| _T_ \|. Using the quasi-coordinates ( [2.190](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ193)) for \\omega \_{\\mathcal {C},\\sigma} and \| _b_ \|∼\| _T_ \|−3, we deduce that the _k_-th derivative of _ω_ _T_ with respect to \|b\|^{1/2}\\omega \_{\\mathcal {C},\\sigma} is bounded by \|T\|^{N\_{k}} for some N\_{k} \\in \\mathbb{N}. The exponential term _e_ −(1/2− _ε_)( _t_ − _T_) absorbs these polynomial factors because _t_ − _T_ ⩾ _T_ 0=\| _T_ \|_α_. This proves (1) for _t_/ _T_ ⩾1− _δ_.

Now assume _t_/ _T_ ⩽1− _δ_ and _t_ ⩽− _N_. We first compare _ω_ _T_ to _ω_ _cusp_ in a similar fashion, using Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40). Then we compare _ω_ _cusp_ to \|b\|^{1/2}\\omega \_{\\mathcal {C},\\sigma} using the fact that these metrics are explicit. This yields the remaining case of (1) ( _t_/ _T_ ⩽1− _δ_, _t_ ⩽ _τ_) and all cases of (2) (2 _τ_ ⩽ _t_ ⩽− _N_). □

Similar arguments yield:

### Lemma 3.9

On _TY_ 0, the following hold.

(1):

If _t_ ∈\[ _T_ + _T_ 0, _τ_\], then for all _k_ ⩾0 there exists a positive integer _N_ _k_ such that

\|\\nabla \_{\\omega \_{T}}^{k}\\psi \_{T}\|\_{\\omega \_{T}}=O(\|T\|^{N\_{k}}).

(3.16)


(2):

If _t_ ∈\[2 _τ_,− _N_\], then for all _k_ ⩾0 there exists a positive integer _N_ _k_ such that

\|\\nabla \_{\\omega \_{cusp}}^{k}\\psi \_{cusp}\|\_{\\omega \_{cusp}}=O(\|T\|^{N\_{k}}).

(3.17)


Now we combine Lemma [3.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar67) and Lemma [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65) to get the following lemma, which essentially measures the non-holomorphicity of Φ_σ_.

### Lemma 3.10

On _TY_ 0, the following hold for all _k_ ⩾0, _ε_ >0\.

(1):

If _t_ ∈\[ _T_ + _T_ 0, _τ_\], we have that

\|\\nabla ^{k}\_{\\omega \_{T}}(\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{\\sigma}^{-1})^{\*} \\psi \_{T}-\\omega \_{T})\|\_{\\omega \_{T}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}).

(3.18)


(2):

If _t_ ∈\[2 _τ_,− _N_\], we have that

\|\\nabla ^{k}\_{\\omega \_{cusp}}(\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{cusp}-\\omega \_{cusp})\|\_{\\omega \_{cusp}}=O(e^{-( \\frac{1}{2}-\\varepsilon )(t-T)}).

(3.19)


### Proof

Let A\_{\\sigma}:=\\Phi \_{\\sigma}^{\*} J\_{\\sigma}-J\_{0}. Then for all functions _f_ on _TY_ _σ_ and Kähler metrics _ω_ on _TY_ 0,

\\begin{aligned} \\begin{aligned} \\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma f-i\\partial \_{0}\\overline{\\partial}\_{0}\\Phi \_{ \\sigma}^{\*}f&=\\Phi \_{\\sigma}^{\*}dd^{c}\_{\\sigma }f-dd^{c}\_{0}\\Phi \_{ \\sigma}^{\*} f \\\ &=d\\Phi \_{\\sigma}^{\*} J\_{\\sigma }d f-dJ\_{0} d \\Phi \_{\\sigma}^{\*} f \\\ &=d\\Big((A\_{\\sigma}+J\_{0})\\Phi \_{\\sigma}^{\*}(df)\\Big) -dJ\_{0} d \\Phi \_{ \\sigma}^{\*} f \\\ &=(\\nabla \_{\\omega} A\_{\\sigma}) \\circledast (\\nabla \_{\\omega}(\\Phi \_{ \\sigma}^{\*}f)) + A\_{\\sigma }\\circledast (\\nabla ^{2}\_{\\omega}(\\Phi \_{ \\sigma}^{\*}f)). \\end{aligned} \\end{aligned}

(3.20)


Here ⊛ denotes a tensorial contraction involving also the reference metric _ω_. Now we apply this with _ω_ = _ω_ _T_, _ω_ _cusp_ and with f = (\\Phi \_{\\sigma}^{-1})^{\*} \\psi \_{T}, (\\Phi \_{\\sigma}^{-1})^{\*} \\psi \_{cusp}, respectively. By Lemma [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65), _A_ _σ_ and its covariant derivatives are bounded by _e_ −(1/2− _ε_)( _t_ − _T_). On the other hand, _ψ_ _cusp_, _ψ_ _T_ and their covariant derivatives blow up at worst polynomially in \| _T_ \| by Lemma [3.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar67). Since _t_ − _T_ ⩾ _T_ 0=\| _T_ \|_α_, these polynomial factors are again absorbed by the exponential decay as in the proof of Lemma [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65). □

The following auxiliary lemma will be used in Lemma [3.13](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar74).

### Lemma 3.11