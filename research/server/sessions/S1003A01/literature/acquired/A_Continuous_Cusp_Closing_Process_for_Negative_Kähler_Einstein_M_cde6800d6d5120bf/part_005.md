---
retention_scope: session
part: 5
total_parts: 7
---

[Part 5/7 of: A Continuous Cusp Closing Process for Negative Kähler–Einstein Metrics]

\\begin{aligned} \\begin{aligned} \\Delta \_{\\omega \_{T\_{i}}} &= \\frac{1}{n+1}(\\eta ^{2}\\partial \_{\\eta \\eta}^{2} - (n-1)\\eta \\partial \_{\\eta}) \\cdot e^{O\_{\\delta}(\\eta ^{n+1})} \\\ &+ \\check{C} \\eta ^{2} \\partial ^{2}\_{\\check{\\theta}\\check{\\theta}} + \\eta \\check{T} +(-t\_{\*,i})^{-\\frac{1}{2}} \\eta \\check{H}\_{i}+O\_{ \\delta}(\|b\_{i}\|^{\\frac{1}{n+1}}\\tau \_{i}), \\end{aligned} \\end{aligned}

(4.12)


where \\check{C}>0 is a constant, \\check{T} is a constant coefficient Laplacian in the \\check{x}\_{\\alpha},\\check{y}\_{\\alpha} coordinates on \\mathbb{R}^{2n-2}, and \\check{H}\_{i} is a differential operator linear homogeneous in

\\begin{aligned} \\partial ^{2}\_{\\check{x}\_{\\alpha }\\check{\\theta}}, \\partial ^{2}\_{ \\check{y}\_{\\alpha }\\check{\\theta}}, (-t\_{\*,i})^{-\\frac{1}{2}} \\partial ^{2}\_{\\check{\\theta}\\check{\\theta}} \\end{aligned}

(4.13)


with coefficients that are uniformly smoothly bounded and Γ_i_-invariant functions of \\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}. Applying the identity ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)) to _ψ_ _i_ and subtracting _ψ_ _i_, we now observe the following:

- The left-hand side can be written as



\\begin{aligned} (\\Delta \_{\\omega \_{T\_{i}}}-{\\mathrm{Id}})\\psi \_{i} = L\_{\\sigma \_{i}}\\psi \_{i}+O(e^{- \\frac{1}{2}\|T\_{i}\|^{\\alpha}}) \\circledast (\\check{\\partial}\\psi \_{i}, \\check{\\partial}^{2}\\psi \_{i}), \\end{aligned}




(4.14)




with \\check{\\partial} the standard gradient operator in our fixed coordinate chart. The first term uniformly converges to zero by assumption. The second term goes to zero strongly in L^{p}\_{loc} for every _p_.

- On the right-hand side, every term with at least one tangential derivative, i.e., the second line of ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)) applied to _ψ_ _i_, goes to zero weakly in L^{p}\_{loc} for every _p_.


This shows that _L_ ∞ _ψ_ ∞=0 weakly, hence classically, with _L_ ∞+Id the smooth ordinary differential operator in the first line of ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)). The claim ( [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ330)) is also clear from this. For the behavior of _L_ ∞ as _s_ →0+ we can run a similar argument based on Proposition [2.30](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar46). □

#### 4.1.2 Fundamental solutions of the endpoint model operators

These are computed in Lemma [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar89). What makes our life difficult in this paper is precisely the fact that both fundamental solutions of L\_{\\infty}^{-} are bounded as _s_ →0+: if one of them was at least ⩾ _s_ − _δ_ for some _δ_ >0, which might be one’s first guess based on experience with other singularities, then the gluing would be unobstructed.

### Lemma 4.4

Recall that if _h_ 1, _h_ 2 are two fundamental solutions of a second order linear ODE, then their Wronskian is defined as w = h\_{1}h\_{2}' - h\_{1}'h\_{2}. Then the following hold.

(1):

Two fundamental solutions of L\_{\\infty}^{+} and their Wronskian are

h^{+}\_{1}(\\eta )=\\eta ^{n+1},\\;\\,h^{+}\_{2}(\\eta )=\\eta ^{-1},\\;\\,w^{+}( \\eta ) = -(n+2)\\eta ^{n-1}.

(4.15)


(2):

Denote \\lambda = (\\frac{4n}{(n+1)^{2}}\\cdot d(n))^{1/2} with _d_( _n_) defined in ( [4.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ331)). Recall the modified Bessel functions I\_{\\frac{1}{n+1}}, K\_{\\frac{1}{n+1}} of order \\frac{1}{n+1}. Write \\mathbb{R}\\{y\_{1},\\ldots ,y\_{k}\\} to denote the ring of convergent power series in _y_ 1,…, _y_ _k_ with real coefficients. Two fundamental solutions of L\_{\\infty}^{-} and their Wronskian are

\\begin{aligned} h\_{1}^{-}(s) = s^{\\frac{1}{2n}}I\_{\\frac{1}{n+1}}(\\lambda s^{ \\frac{n+1}{2n}}) \\in s^{\\frac{1}{n}} \\cdot \\mathbb{R}\\{s^{ \\frac{n+1}{n}}\\} \\subset \\mathbb{R}\\{s^{\\frac{1}{n}},s^{\\frac{n+1}{n}} \\}, \\end{aligned}

(4.16)


\\begin{aligned} h\_{2}^{-}(s) = s^{\\frac{1}{2n}}K\_{\\frac{1}{n+1}}(\\lambda s^{ \\frac{n+1}{2n}}) \\in \\mathbb{R}\\{s^{\\frac{n+1}{n}}\\} + s^{\\frac{1}{n}} \\cdot \\mathbb{R}\\{s^{\\frac{n+1}{n}}\\} \\subset \\mathbb{R}\\{s^{ \\frac{1}{n}},s^{\\frac{n+1}{n}}\\}, \\end{aligned}

(4.17)


\\begin{aligned} w^{-}(s) = -\\frac{n+1}{2n}s^{\\frac{1-n}{n}}. \\end{aligned}

(4.18)


### Proof

The computations for L\_{\\infty}^{+} are straightforward. For L\_{\\infty}^{-}, a lengthy computation shows that _u_( _s_) solves L\_{\\infty}^{-}u = 0 if and only u(s) = s^{\\frac{1}{2n}}v(\\lambda \\cdot s^{\\frac{n+1}{2n}}), where _v_( _y_) solves the modified Bessel equation

y^{2} v''(y) + y v'(y) - \\left (\\frac{1}{(n+1)^{2}} + y^{2}\\right )v(y) = 0.

(4.19)


This yields the fundamental solutions h\_{1}^{-}(s),h\_{2}^{-}(s) above. Their Wronskian is easily calculated using the fact that the Wronskian of the modified Bessel functions _I_( _y_), _K_( _y_) (of any order) is -\\frac{1}{y}. □

#### 4.1.3 A Liouville theorem for the limit ODE

The ODE _L_ ∞ _u_ =0 on the whole limit neck (0,1) has a 2-dimensional vector space of solutions. Our goal is to prove that the weight _s_ − _δ_ that we will impose as an upper bound in our blowup argument singles out a 1-dimensional subspace. Again, experience with other gluing problems suggests that by choosing 0< _δ_ ≪1 _all_ solutions to _L_ ∞ _u_ =0 are ruled out, but here we are left with a 1-dimensional obstruction space no matter how small we choose _δ_.

### Lemma 4.5

There is a unique solution \\hat{u}(s) to the homogeneous ODE L\_{\\infty }\\hat{u} =0 on (0,1) such that \\hat{u}(s) \\to 1 as _s_ →0+ and \\hat{u}(s) \\to 0 as _s_ →1−. This satisfies the following properties:

(1):

\\hat{u}(s) is strictly decreasing in _s_.

(2):

As _η_ →0+ we have that \\hat{u}(1-\\eta ) = O(\\eta ^{n+1}).

(3):

As _s_ →0+ we have that \\hat{u}(s) = 1 - C\_{1} s^{\\frac{1}{n}} + C\_{2} s^{\\frac{n+1}{n}} + R(s) with _C_ 1, _C_ 2>0 and

\|R(s)\| + s\|R'(s)\| + s^{2}\|R''(s)\| = O(s^{\\frac{n+2}{n}}).

(4.20)


(4):

If _L_ ∞ _u_ =0 and \| _u_( _s_)\|⩽ _Cs_ − _δ_ for some _δ_ ∈(0,1), then _u_ is a scalar multiple of \\hat{u}.

### Proof

The uniqueness of \\hat{u} is clear by the maximum principle.

If \\hat{u} exists, then (1) can be proved as follows: First note that \\hat{u} \\geqslant 0 because otherwise there is a global interior minimum with \\hat{u} < 0 and this contradicts the maximum principle. Next, we prove that \\hat{u} is weakly decreasing. Otherwise there exist _s_ 1< _s_ 2 in (0,1) with \\hat{u}(s\_{1}) < \\hat{u}(s\_{2}). Both of these values are nonnegative by what we said before. By the intermediate value theorem, there is an s\_{2}' \\in (s\_{2},1) such that \\hat{u}(s\_{1}) = \\hat{u}(s\_{2}'), but then \\hat{u} attains a strictly positive interior maximum on \[s\_{1},s\_{2}'\], contradicting the maximum principle. Thus, \\hat{u} is weakly decreasing. Next, we prove that \\hat{u} is strictly decreasing. If this is false, then \\hat{u} must be constant on some interval \[ _s_ 1, _s_ 2\]⊂(0,1) with _s_ 1< _s_ 2. From the ODE, \\hat{u} = 0 on \[ _s_ 1, _s_ 2\]. Hence \\hat{u} = 0 on (0,1) by interior analyticity, which contradicts \\hat{u}(0) = 1.

To prove the existence of \\hat{u}, we solve L\_{\\infty}\\hat{u}\_{\\varepsilon}=0 on \[ _ε_,1− _ε_\] with \\hat{u}\_{\\varepsilon}(\\varepsilon )=1 and \\hat{u}\_{\\varepsilon}(1-\\varepsilon ) = 0 for any fixed \\varepsilon \\in (0,\\frac{1}{2}). This is possible by the standard Dirichlet problem for nonsingular ODEs. The same argument as above shows that \\hat{u}\_{\\varepsilon} is strictly decreasing, hence in particular bounded by 0 and 1. Then, also by standard ODE theory, \\hat{u}\_{\\varepsilon} satisfies uniform derivative bounds to all orders on every fixed compact interval contained in (0,1). Thus, up to subsequences, \\hat{u}\_{\\varepsilon}\\to \\hat{u} locally smoothly on (0,1), where L\_{\\infty}\\hat{u} = 0. The issue is to prove that \\hat{u} is not identically zero, and, indeed, that it satisfies the correct boundary conditions as _s_ →0 and _s_ →1\. This will be done using a barrier argument.

First consider \\hat{u}\_{sub}(s) := 1 - C\_{1} s^{1/n} + C\_{2} s^{\\gamma} for _C_ 1, _C_ 2>0 and _γ_ >1/ _n_ to be determined. Fix an _s_ ∗∈(0,1) such that the _O_( _s_( _n_ +1)/ _n_) in ( [4.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ331)) is explicitly bounded by _C_ ∗ _s_( _n_ +1)/ _n_ for all _s_ ∈(0, _s_ ∗\]. Here _s_ ∗, _C_ ∗ can be chosen to depend only on _n_. By choosing _C_ 1, _C_ 2 such that _C_ 1 _s_ ∗1/ _n_=2 and _C_ 2 _s_ ∗_γ_=1, we get \\hat{u}\_{sub}(s\_{\*}) = 0. It remains to check that \\hat{u}\_{sub} is a subsolution on (0, _s_ ∗\] because then the maximum principle shows that \\hat{u}\_{\\varepsilon }\\geqslant \\hat{u}\_{sub} on \[ _ε_, _s_ ∗\], and so \\hat{u} \\geqslant \\hat{u}\_{sub}, proving that \\hat{u} is not identically zero and in fact \\lim \_{s\\to 0^{+}} \\hat{u}(s) = 1. To this end we calculate on (0, _s_ ∗\], using ( [4.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ331)) and the observation that _s_ 1/ _n_ is a homogeneous solution of the operator _L_ ∞+Id:

L\_{\\infty}\\hat{u}\_{sub} \\geqslant (-1+C\_{1} s^{\\frac{1}{n}} - C\_{2} s^{ \\gamma}) + (0 - C\_{\*}'C\_{1} s^{\\frac{1}{n}}) + (C\_{\*}''C\_{2}(n\\gamma -1)s^{ \\gamma -\\frac{n+1}{n}}- C\_{\*}'''C\_{2} s^{\\gamma}).

(4.21)


Here, C\_{\*}'>0 depends only on _n_ while C\_{\*}'',C\_{\*}'''>0 depend on _n_ and _γ_. Thus, as long as \\frac{1}{n} < \\gamma \\leqslant \\frac{n+1}{n}, we can arrange that ( [4.21](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ345)) ⩾0 on (0, _s_ ∗\] by making _s_ ∗ smaller if necessary. To be precise, we first let \\gamma = \\frac{n+1}{n} and then choose _s_ ∗ so small that C\_{2} = 1/s\_{\*}^{\\gamma} satisfies C\_{\*}'' C\_{2} (n\\gamma - 1) \\geqslant 2 + 2C\_{\*}' + C\_{\*}'''.

Next, we need to prove that \\hat{u}(s) \\to 0 as _s_ →1−. In fact, by applying another barrier argument to the approximating functions \\hat{u}\_{\\varepsilon}, we will prove that (2) holds. For this we again choose a _C_ ∗>0 and an _η_ ∗∈(0,1) depending only on _n_ such that the _O_( _η_ _n_ +1) in ( [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ330)) is bounded by _C_ ∗ _η_ _n_ +1 for all _η_ ∈(0, _η_ ∗\]. Then we consider the function \\hat{u}^{sup}(1-\\eta ) := C\_{1} \\eta ^{n+1} - C\_{2}\\eta ^{\\gamma} for _C_ 1, _C_ 2>0 and _γ_ > _n_ +1 to be determined. We set C\_{1} \\eta \_{\*}^{n+1} = 2 and C\_{2} \\eta \_{\*}^{\\gamma }=1, thus arranging that \\hat{u}^{sup}(1-\\eta \_{\*}) = 1. To apply the maximum principle on \[1− _η_ ∗,1), we need to check that \\hat{u}^{sup} is a supersolution for _η_ ∈(0, _η_ ∗\] after making _η_ ∗ smaller if necessary. For this we compute for _η_ ∈(0, _η_ ∗\] using ( [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ330)):

\\begin{aligned} L\_{\\infty }\\hat{u}^{sup} \\leqslant {}& (-C\_{1}\\eta ^{n+1} + C\_{2} \\eta ^{ \\gamma}) + (C\_{1}\\eta ^{n+1} + C\_{\*}'C\_{1}\\eta ^{2n+2}) \\\ &{}+ \\left (- \\frac{\\gamma (\\gamma -n)}{n+1}C\_{2}\\eta ^{\\gamma }+ C\_{\*}'''C\_{2} \\eta ^{\\gamma +n+1}\\right ), \\end{aligned}

(4.22)


where C\_{\*}'>0 depends only on _n_ and C\_{\*}'''>0 depends only on _n_, _γ_. Thus, as long as _γ_ ⩽2 _n_ +2 and 1− _γ_( _γ_ − _n_)/( _n_ +1)<0 (equivalently, _γ_ > _n_ +1), we can make ( [4.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ346)) ⩽0\. More precisely, it is enough to set _γ_ =2 _n_ +2 and choose _η_ ∗ so small that (2C\_{\*}' + C\_{\*}''')\\eta \_{\*}^{n+1} \\leqslant \\gamma (\\gamma -n)/(n+1)-1.

It remains to prove (3) and (4). The key point, carried out below, is to prove that if \| _u_ \|⩽ _Cs_ − _δ_, then _u_ actually has an expansion as _s_ →0 and as _s_ →1\. The expansion as _s_ →1 proves (2) for a general _u_. The expansion as _s_ →0 proves (3) for a general _u_, with some constant as the leading term (=: _u_(0)) but without the sign information on _C_ 1, _C_ 2. For u = \\hat{u} we already know that \\hat{u}(0) = 1. In this case it is then easy to see that _C_ 2>0 by plugging the expansion into the ODE L\_{\\infty}\\hat{u} = 0 (here the estimate ( [4.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ344)) up to two derivatives is crucial). Then _C_ 1>0 also follows: if _C_ 1<0, then \\hat{u} would obviously be strictly increasing for a short time, which contradicts (1); if _C_ 1=0, the same argument applies because we already know that _C_ 2>0\. Lastly, (4) follows by applying the maximum principle to u-u(0)\\hat{u} because the expansion tells us that u - u(0)\\hat{u} vanishes as _s_ →0+ and as _s_ →1−.

It remains to prove that a general solution _u_ to _L_ ∞ _u_ =0 on (0,1) with \| _u_ \|⩽ _Cs_ − _δ_ for some _δ_ ∈(0,1) satisfies the expansions (2) and (3). For this, we use the standard general formula

u(x) = c\_{1} h\_{1}(x) + c\_{2} h\_{2}(x) + h\_{1}(x) \\int \_{x}^{x\_{0}} \\frac{h\_{2}(t)f(t)}{w(t)a(t)}\\,dt - h\_{2}(x) \\int \_{x}^{x\_{0}} \\frac{h\_{1}(t)f(t)}{w(t)a(t)}\\,dt

(4.23)


for solutions to _au_″+ _bu_′+ _cu_ = _f_, where _h_ 1, _h_ 2 are two fundamental solutions to the homogeneous equation, w = h\_{1} h\_{2}' - h\_{1}' h\_{2} is their Wronskian, _x_ 0 is an arbitrary point and _c_ 1, _c_ 2 are constants.

We start with the easier case, _s_ →1−, which will give us (2) for a general _u_. By Lemmas [4.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar87)– [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar89) and ( [4.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ347)), for any _η_ 0∈(0,1) there exist constants _c_ 1, _c_ 2 such that for all _η_ ∈(0,1),

\\begin{aligned} u(1-\\eta )=c\_{1}\\eta ^{n+1} + c\_{2} \\eta ^{-1} + \\eta ^{n+1}\\int \_{ \\eta}^{\\eta \_{0}} t^{-n-2}f(t)\\,dt - \\eta ^{-1}\\int \_{\\eta}^{\\eta \_{0}} f(t)\\,dt, \\end{aligned}

(4.24)


\\begin{aligned} \|f(\\eta )\| \\leqslant c\\eta ^{n+1}(\\eta ^{2} \|u''(1-\\eta )\| + \\eta \|u'(1- \\eta )\| + \|u(1-\\eta )\|) \\end{aligned}

(4.25)


for some dimensional constant _c_. We are assuming that \| _u_(1− _η_)\|= _O_(1) as _η_ →0+.

### Claim 4.6

We actually have that

\|u(1-\\eta )\| + \\eta \|u'(1-\\eta )\| + \\eta ^{2}\|u''(1-\\eta )\| = O(1)\\; \\,\\text{as}\\;\\,\\eta \\to 0^{+}.

(4.26)


### Proof of Claim [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar93)

We will first show that there exist _ε_ ∈(0,1) and _C_ >0 independent of _η_ such that for any fixed 0< _η_ ≪1 the following sub-claim is true.

### Sub-Claim 4.7

Define _F_:\[0,1\]→\[0,∞) via _F_( _ρ_):=max\[ _η_,(1+ _ρ_) _η_\]\| _u_′(1−⋅)\|. Then\
\
\\begin{aligned} F(\\rho ) \\leqslant \\varepsilon \\cdot F(R) + \\frac{C}{\\eta}(R-\\rho )^{-1}\\; \\,\\text{for all}\\;\\,0\\leqslant \\rho < R \\leqslant 1. \\end{aligned}\
\
(4.27)\
\
\
If Sub-Claim [4.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar95) is true, then by a standard calculus iteration lemma (see \[ [HT20](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR20 " 					Hein, H.-J., Tosatti, V.: Higher-order estimates for collapsing Calabi-Yau metrics. Camb. J. Math. 8, 683–773 (2020) 				"), Lemma 3.4\] based on \[ [GM05](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR14 " 					Giaquinta, M., Martinazzi, L.: An Introduction to the Regularity Theory for Elliptic Systems, Harmonic Maps and Minimal Graphs. Edizioni della Normale, Pisa (2005) 				"), Lemma 8.18\], or many other sources) there exists a universal _C_ 0= _C_ 0( _ε_) such that\
\
\\begin{aligned} F(\\rho ) \\leqslant C\_{0}\\frac{C}{\\eta}(1-\\rho )^{-1}\\;\\text{for all}\\;\\,0 \\leqslant \\rho < 1. \\end{aligned}\
\
(4.28)\
\
\
Setting _ρ_ =0 in ( [4.28](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ352)) and using _L_ ∞ _u_ =0 to solve for _u_″ in terms of _u_, _u_′, we obtain Claim [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar93).\
\
_Proof of Sub-Claim_ [_4.7_](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar95) _._ We will prove ( [4.27](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ351)) by a simple interpolation argument. Let \\tilde{u} := u(1-\\cdot ). For any 0 < \\varepsilon \\leqslant \\frac{1}{10} and any _η_ ∗∈\[ _η_,(1+ _ρ_) _η_\], expand\
\
\\begin{aligned} \\tilde{u}(\\eta \_{\*} + \\varepsilon (R-\\rho )\\eta ) = \\tilde{u}(\\eta \_{\*}) + \\int \_{\\eta \_{\*}}^{\\eta \_{\*}+\\varepsilon (R-\\rho )\\eta} \\left \[ \\tilde{u}'(\\eta \_{\*}) + \\int \_{\\eta \_{\*}}^{\\xi }\\tilde{u}''( \\tilde{\\xi})\\,d\\tilde{\\xi}\\right \]d\\xi . \\end{aligned}\
\
(4.29)\
\
\
Then solve this equation for \\tilde{u}'(\\eta \_{\*}), express \\tilde{u}'' in terms of \\tilde{u}' and \\tilde{u} using the ODE _L_ ∞ _u_ =0, take the maximum over all _η_ ∗∈\[ _η_,(1+ _ρ_) _η_\], and fix _ε_ sufficiently small depending only on _n_. □\
\
Plugging Claim [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar93) into ( [4.25](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ349)), we get that \| _f_( _η_)\|= _O_( _η_ _n_ +1) as _η_ →0+. Inserting this into ( [4.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ348)), letting _η_ →0+ and using the boundedness of the left-hand side, we deduce that\
\
c\_{2} - \\int \_{0}^{\\eta \_{0}} f(t)\\,dt = 0.\
\
(4.30)\
\
\
As a consequence, \| _u_(1− _η_)\|= _O_( _η_ _n_ +1\|log _η_ \|) as _η_ →0+. This would already be enough for us but another iteration easily yields the expected \| _u_(1− _η_)\|= _O_( _η_ _n_ +1), i.e., (2) holds for a general _u_.\
\
To finish the proof, we now deal with the more difficult case _s_ →0+, i.e., statement (3). As above, and using also the fact that a(t) w(t) = -\\frac{n+1}{2} = const in this case, we have that\
\
\\begin{aligned} u(s) = c\_{1} h\_{1}^{-}(s) + c\_{2} h\_{2}^{-}(s) + h\_{1}^{-}(s)\\int \_{s}^{s\_{0}} h\_{2}^{-}(t) f(t) \\, dt - h\_{2}^{-}(s)\\int \_{s}^{s\_{0}} h\_{1}^{-}(t)f(t) \\,dt, \\end{aligned}\
\
(4.31)\
\
\
\\begin{aligned} h\_{1}^{-}(s) = c\_{1,1}s^{\\frac{1}{n}} + O(s^{\\frac{n+2}{n}}),\\;\\,h\_{2}^{-}(s) = c\_{2,0} + c\_{2,1}s^{\\frac{1}{n}} + c\_{2,2}s^{\\frac{n+1}{n}} + O(s^{ \\frac{n+2}{n}}), \\end{aligned}\
\
(4.32)\
\
\
\\begin{aligned} \|f(s)\| \\leqslant c s^{\\frac{n+1}{n}}\\left (s^{\\frac{n-1}{n}}\|u''(s)\| + s^{- \\frac{1}{n}}\|u'(s)\| + \|u(s)\|\\right ) \\end{aligned}\
\
(4.33)\
\
\
for some dimensional constants _c_ 1,1, _c_ 2,0, _c_ 2,1, _c_ 2,2, _c_. We are assuming that \| _u_( _s_)\|= _O_( _s_ − _δ_) as _s_ →0+ for some fixed _δ_ ∈(0,1). From this and from the ODE _L_ ∞ _u_ =0, we get\
\
\\begin{aligned} \|u(s)\| + s \|u'(s)\| + s^{2} \|u''(s)\| = O(s^{-\\delta})\\;\\,\\text{as}\\;\\,s \\to 0^{+} \\end{aligned}\
\
(4.34)\
\
\
as in the proof of Claim [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar93). This again directly fits into ( [4.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ357)), yielding an estimate \| _f_( _s_)\|= _O_( _s_ − _δ_) as _s_ →0+. Because of this, the integrals in ( [4.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ355)) converge as _s_ →0+. In particular, \| _u_( _s_)\|= _O_(1) as _s_ →0+. Again arguing as in the proof of Claim [4.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar93), this implies that\
\
\\begin{aligned} \|u(s)\| + s \|u'(s)\| + s^{2} \|u''(s)\| = O(1)\\;\\,\\text{as}\\;\\,s \\to 0^{+}, \\end{aligned}\
\
(4.35)\
\
\
so \| _f_( _s_)\|= _O_(1). Writing \\int \_{s}^{s\_{0}} = \\int \_{0}^{s\_{0}} - \\int \_{0}^{s} in ( [4.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ355)), we thus obtain with new constants \\tilde{c}\_{1},\\tilde{c}\_{2} that\
\
\\begin{aligned} u(s) = \\tilde{c}\_{1} h\_{1}^{-}(s) + \\tilde{c}\_{2} h\_{2}^{-}(s) - h\_{1}^{-}(s) \\int \_{0}^{s} h\_{2}^{-}(t) f(t)\\,dt + h\_{2}^{-}(s)\\int \_{0}^{s} h\_{1}^{-}(t)f(t) \\,dt, \\end{aligned}\
\
(4.36)\
\
\
where \| _f_( _s_)\|= _O_(1). By itself this says that _u_( _s_)= _d_ 0+ _d_ 1 _s_ 1/ _n_+ _O_( _s_( _n_ +1)/ _n_), which is good but not enough. We now use this information to prove that \| _f_( _s_)\|= _O_( _s_ 1/ _n_). (Once we have this, we can feed it back into ( [4.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ360)) to get that the two inhomogeneous terms are in fact _O_( _s_( _n_ +2)/ _n_), and this is the pointwise part of the desired estimate ( [4.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ344)).) Here we need to be a bit more careful than before.\
\
Consider again ( [4.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ357)). The third term is negligible because \| _u_( _s_)\|= _O_(1). For the first and second term, ( [4.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ359)) and its proof tell us nothing new because these arguments are based on upper bounds and the upper bound \| _u_( _s_)\|= _O_(1) cannot be improved. However, we now have enough information to use ( [4.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ360)) directly. In fact, we can simply take one derivative of ( [4.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ360)) and use \| _f_( _s_)\|= _O_(1) to bound _s_ \| _u_′( _s_)\|= _O_( _s_ 1/ _n_). Then, from the ODE _L_ ∞ _u_ =0,\
\
\\begin{aligned} s^{2} \|u''(s)\| \\leqslant O(s)\|u'(s)\| + O(s^{\\frac{n+1}{n}})\|u(s)\| + O(s^{ \\frac{n+1}{n}})\|f(s)\| = O(s^{\\frac{1}{n}}), \\end{aligned}\
\
(4.37)\
\
\
using what we already know about _u_′, _u_, _f_. Thus, from ( [4.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ357)), \| _f_( _s_)\|= _O_( _s_ 1/ _n_). By feeding this back into ( [4.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ360)), \| _R_( _s_)\|= _O_( _s_( _n_ +2)/ _n_) in ( [4.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ344)). This is the pointwise part of the desired expansion (3).\
\
We still need to prove the derivative estimates of _R_( _s_) in ( [4.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ344)) (as, without these, we would not be able to plug the expansion of \\hat{u} back into the ODE and deduce the sign of _C_ 1, _C_ 2, which is crucial). First, _s_ \| _R_′( _s_)\|= _O_( _s_( _n_ +2)/ _n_) is easily proved by differentiating the inhomogeneous terms in ( [4.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ360)) and using that \| _f_( _s_)\|= _O_( _s_ 1/ _n_). Notice that the terms obtained by letting _d_/ _ds_ act on the integral signs cancel out. Thus, when we differentiate one more time to estimate _R_″, there is no need for a bound on _f_′, and \| _f_( _s_)\|= _O_( _s_ 1/ _n_) implies _s_ 2\| _R_″( _s_)\|= _O_( _s_( _n_ +2)/ _n_). So (3) is proved for a general _u_. □\
\
#### 4.1.4 Solving L\_{\\infty }\\hat{v} = \\hat{u} with a Neumann boundary condition on the left\
\
The inhomogeneous ODE L\_{\\infty }v = \\hat{u} has a 2-dimensional affine space of solutions on (0,1). For the sake of transplanting _v_ to the approximating manifolds, we again require that _v_( _s_)→ _const_ as _s_ →0+ and _s_ →1−. As in Sect. [4.1.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec21) this singles out a 1-dimensional affine subspace of solutions, any two members of which differ by a scalar multiple of \\hat{u}. What makes things work in the end is the fact that there exists a canonical element \\hat{v} of this 1-dimensional affine subspace that satisfies a _Neumann_ boundary condition at _s_ =0\. We also need to know that \\hat{v} \\leqslant 0 and \\hat{v}(0) \\neq 0, but the precise value of \\hat{v}(0) is irrelevant.\
\
### Lemma 4.8\
\
There exists a solution \\hat{v} \\leqslant 0 to the inhomogeneous ODE L\_{\\infty}\\hat{v} = \\hat{u} on (0,1) such that\
\
\\begin{aligned} &\|\\hat{v}(1-\\eta )\| + \\eta \|\\hat{v}'(1-\\eta )\| + \\eta ^{2}\|\\hat{v}''(1- \\eta )\| = O(\\eta ^{n+1})\\;\\,\\text{as}\\;\\,\\eta \\to 0^{+}, \\end{aligned}\
\
(4.38)\
\
\
\\begin{aligned} \\begin{aligned}&\\hat{v}(s) = C\_{0} + C\_{2} s^{\\frac{n+1}{n}} + R(s), \\;\\,\|R(s)\| + s\|R'(s)\| + s^{2}\|R''(s)\| \\\ &\\phantom{\\hat{v}(s) }= O(s^{\\frac{n+2}{n}})\\;\\,\\text{as}\\;\\,s \\to 0^{+}, \\end{aligned} \\end{aligned}\
\
(4.39)\
\
\
where _C_ 0, _C_ 2 are constants and _C_ 0≠0.\
\
This satisfies a Neumann condition in the sense that the expected term _C_ 1 _s_ 1/ _n_ in ( [4.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ363)) vanishes.\
\
### Proof\
\
We begin by constructing one particular solution _v_ to the ODE, which may not be the one we seek. For this we proceed as in the proof of Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91), i.e., by solving Dirichlet rather than Neumann problems. Thus, for any fixed _ε_ ∈(0,1) let v\_{\\varepsilon}: \[\\varepsilon ,1-\\varepsilon \] \\to \\mathbb{R} be the unique solution to L\_{\\infty }v\_{\\varepsilon }= \\hat{u}\|\_{\[\\varepsilon ,1-\\varepsilon \]} with _v_( _ε_)=−1 and _v_(1− _ε_)=0\. At an interior maximum we must have that -v\_{\\varepsilon }\\geqslant L\_{\\infty }v\_{\\varepsilon }= \\hat{u}, i.e., v\_{\\varepsilon }\\leqslant -\\hat{u} \\leqslant 0, and at an interior minimum we must have that -v\_{\\varepsilon }\\leqslant L\_{\\infty }v\_{\\varepsilon }= \\hat{u}, i.e., v\_{\\varepsilon }\\geqslant -\\hat{u} \\geqslant -1. Thus, by comparison with the boundary values, −1⩽ _v_ _ε_⩽0\. Up to a subsequence, we can now pass to a limit v: (0,1) \\to \\mathbb{R} locally smoothly. Clearly L\_{\\infty }v = \\hat{u} and −1⩽ _v_ ⩽0.\
\
A barrier argument as in the proof of Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91) yields \\lim \_{s \\to 0^{+}} v(s) = -1 and \\lim \_{s \\to 1^{-}} v(s) = 0. Indeed, consider the function \\hat{u}\_{sub}(s) = 1 - C\_{1} s^{1/n} + C\_{2} s^{(n+1)/n} from the previous proof, which satisfies \\hat{u}\_{sub}(s\_{\*}) = 0 and L\_{\\infty}\\hat{u}\_{sub} \\geqslant 0 on (0, _s_ ∗\] for some small dimensional _s_ ∗∈(0,1). Then v^{sup} := -\\hat{u}\_{sub} trivially satisfies L\_{\\infty }v^{sup} \\leqslant 0 \\leqslant \\hat{u}, so we can use _v_ _sup_ as an upper barrier for _v_ _ε_ on \[ _ε_, _s_ ∗\], proving that \\lim \_{s\\to 0^{+}} v(s) = -1. For _s_ →1− almost the same trick works. From the proof of Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91) we know that \\hat{u}^{sup}(1-\\eta ) = C\_{1} \\eta ^{n+1} - C\_{2}\\eta ^{2n+2} satisfies \\hat{u}^{sup}(1-\\eta \_{\*}) = 1 and L\_{\\infty}\\hat{u}^{sup} \\leqslant 0 on \[1− _η_ ∗,1) for a small universal _η_ ∗∈(0,1). Then we would like to use v\_{sub} := -\\hat{u}^{sup} as a lower barrier for _v_ _ε_ on \[1− _η_ ∗,1− _ε_\]. This does not work immediately because we only have _L_ ∞ _v_ _sub_⩾0 but not L\_{\\infty }v\_{sub} \\geqslant \\hat{u}. However, we can improve the construction of \\hat{u}^{sup} slightly by choosing _η_ ∗ small enough so that (2C\_{\*}' + C\_{\*}''')\\eta \_{\*}^{n+1} ⩽ (1/2)( _γ_( _γ_ − _n_)/( _n_ +1)−1) in the previous proof, hence _L_ ∞ _v_ _sub_⩾(1/2)( _γ_( _γ_ − _n_)/( _n_ +1)−1)>0 on \[1− _η_ ∗,1). Since we already know that \\hat{u}(1-\\eta ) = O(\\eta ^{n+1}) with a dimensional constant, this means we can arrange that L\_{\\infty }v\_{sub} \\geqslant \\hat{u} on \[1− _η_ ∗,1) by making _η_ ∗ even smaller if necessary.\
\
To sum up, we have constructed a solution v: (0,1) \\to \\mathbb{R} to L\_{\\infty }v = \\hat{u} with −1⩽ _v_ ⩽0 as well as \\lim \_{s\\to 0^{+}}v(s) = -1 and \\lim \_{s \\to 1^{-}} v(s) = 0. In fact, _v_(1− _η_)= _O_( _η_ _n_ +1) as _η_ →0+, and by using Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91)(2) and the interpolation argument proving ( [4.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ350)) we can easily upgrade this to ( [4.38](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ362)). Also as in the proof of Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91), we can now prove that _v_( _s_)=−1+ _C_ 1 _s_ 1/ _n_+ _C_ 2 _s_( _n_ +1)/ _n_+ _R_( _s_), where _R_( _s_)= _O_( _s_( _n_ +2)/ _n_) with two derivatives as in ( [4.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ344)) or ( [4.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ363)). In fact, nothing needs to be changed in the proof except that \\hat{u}(s) = 1 + O(s^{1/n}) needs to be added to _f_.\
\
Having proved this expansion of _v_, we note that if _C_ 1=0, then we are done with \\hat{v} := v. Otherwise we can replace _v_ by \\hat{v} := v + \\lambda \\hat{u} for some _λ_ ≠0 to make the _s_ 1/ _n_ term vanish. Then we also need to make sure that \\hat{v} \\leqslant 0 and \\hat{v}(0) \\neq 0. By the maximum principle, it is enough to prove that \\hat{v}(0) < 0, which we do by contradiction. If \\hat{v}(0) \\geqslant 0, then the constant term of \\hat{v}(s) is nonnegative and the _s_ 1/ _n_ term vanishes. Thus, in order to have L\_{\\infty }\\hat{v}(s) = \\hat{u}(s) = 1 + O(s^{1/n}), we need _C_ 2>0 (again thanks to the fact that _R_( _s_) is estimated with two derivatives). Thus, \\hat{v}(s) > \\hat{v}(0) for 0< _s_ ≪1\. But this contradicts the inequality \\hat{v} \\leqslant \\hat{v}(0), which holds by the maximum principle. □\
\
#### 4.1.5 Definition of the obstruction function\
\
For all 0<\| _σ_ \|≪1 we first choose an s\_{\*,\\sigma} \\in (0,\\frac{1}{5}\] with\
\
\\begin{aligned} \\max \\left \\{3\|T\|^{\\alpha -1},3\\frac{\\tau}{T}\\right \\} \\leqslant s\_{\*, \\sigma} \\to 0\\;\\,\\text{as}\\;\\,\\sigma \\to 0. \\end{aligned}\
\
(4.40)\
\
\
Then we choose a smooth function _χ_ _σ_:(0,1)→\[0,1\] such that\
\
\\begin{aligned} \\chi \_{\\sigma}(s) = \\left . \\textstyle\\begin{cases} \\;0 &\\text{for}\\;\\,s \\in (0,s\_{\*,\\sigma}\] \\\ \\;1 &\\text{for}\\;\\,s \\in \[2s\_{\*,\\sigma},1) \\end{cases}\\displaystyle \\right \\} \\;\\text{and}\\;\\,s\_{\*,\\sigma}\|\\chi \_{\\sigma}'\| + s\_{\*, \\sigma}^{2}\|\\chi \_{\\sigma}''\| \\leqslant C \\end{aligned}\
\
(4.41)\
\
\
for some constant _C_ independent of _σ_. Now recall Convention [4.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar85): We identify \\mathfrak{R}\_{4} \\subset \\mathcal{X}\_{\\sigma} with the set { _T_ +2 _T_ 0< _t_ <2 _τ_}⊂ _TY_ 0 using the diffeomorphism \\Phi \_{\\sigma}^{-1} \\circ \\Psi \_{\\sigma}. In this way we can view (functions of) _s_, _η_ as functions on \\mathfrak{R}\_{4}. Thus, the following definition makes sense.\
\
### Definition 4.9\
\
We define the obstruction function \\hat{u}\_{\\sigma }\\in C^{\\infty}(\\mathcal{X}\_{\\sigma}) via \\hat{u}\_{\\sigma }:= L\_{\\sigma }\\hat{v}\_{\\sigma}, where\
\
\\begin{aligned} \\hat{v}\_{\\sigma }:= \[\\chi \_{\\sigma }\\hat{v} + (1 - \\chi \_{\\sigma}) \\hat{v}(0)\]\\chi \_{\\sigma}(1-\\cdot ) \\in C^{\\infty}(\\mathcal{X}\_{\\sigma}). \\end{aligned}\
\
(4.42)\
\
\
Note that \\hat{v}\_{\\sigma} actually extends smoothly from \\mathfrak{R}\_{4} to all of \\mathcal{X}\_{\\sigma} because it is constant equal to \\hat{v}(0) for _s_ < _s_ ∗, _σ_ and zero for _s_ >1− _s_ ∗, _σ_. By ( [4.40](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ364)) this cutoff happens strictly within the boundaries of \\mathfrak{R}\_{4}. Also, \\hat{u}\_{\\sigma} is then constant equal to -\\hat{v}(0) to the left of \\mathfrak{R}\_{4} and zero to the right of \\mathfrak{R}\_{4}.\
\
### Lemma 4.10\
\
The obstruction function \\hat{u}\_{\\sigma} satisfies the following properties:\
\
(1):\
\
Fix _s_ 1< _s_ 2 in (0,1). Lift \\hat{u}\_{\\sigma} and \\hat{u} \\circ s to functions on the domain of the chart ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)) on the universal cover of { _s_ 1< _s_ < _s_ 2}. Then \\hat{u}\_{\\sigma }\\to \\hat{u} \\circ s uniformly as _σ_ →0.\
\
(2):\
\
There exists a uniform constant _C_ such that \|\\hat{u}\_{\\sigma}\| \\leqslant C\\eta ^{3} as functions on \\mathfrak{R}\_{4} for all _σ_.\
\
The main content of (2) is that \\hat{u}\_{\\sigma} remains bounded independently of _σ_ at the left boundary of \\mathfrak{R}\_{4}. This is not at all obvious due to the poor regularity of \\hat{u}(s) and \\hat{v}(s) as _s_ →0\. Here we crucially use the Neumann property of \\hat{v}. (2) is also the key to the proof of our main result, Proposition [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar86).\
\
### Proof of Lemma [4.10](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar99)\
\
For item (1): From the proof of Lemma [4.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar87) we know that for \| _σ_ \|≪1,\
\
\\begin{aligned} \\begin{aligned} \\hat{u}\_{\\sigma }&= \[(\\Delta \_{\\omega \_{T}} - {\\mathrm{Id}}) + (\\Delta \_{ \\omega \_{glue,\\sigma}}-\\Delta \_{\\omega \_{T}})\]\\hat{v}\_{\\sigma } \\\ &= (\\Delta \_{\\omega \_{T}} - {\\mathrm{Id}})\\hat{v}\_{\\sigma }+ O\_{s\_{1},s\_{2}}(e^{- \\frac{1}{2}\|T\|^{\\alpha}}) \\circledast (\\check{\\partial}\\hat{v}\_{\\sigma}, \\check{\\partial}^{2}\\hat{v}\_{\\sigma}) \\\ &= L\_{\\infty }\\hat{v} + \[O\_{s\_{1},s\_{2}}(\|b\|^{\\frac{1}{3}}\|\\tau \|) + O\_{s\_{1},s\_{2}}(e^{- \\frac{1}{2}\|T\|^{\\alpha}})\] \\circledast (\\hat{v}',\\hat{v}''). \\end{aligned} \\end{aligned}\
\
(4.43)\
\
\
The point is that \\hat{v}\_{\\sigma} is radial in the chart ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)) and for \| _σ_ \|≪1 we have 2 _s_ ∗, _σ_< _s_ 1< _s_ 2<1−2 _s_ ∗, _σ_, so the cutoffs in ( [4.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ366)) are irrelevant and \\hat{v}\_{\\sigma }= \\hat{v}. Thus, according to the definition of _L_ ∞ as the first line of ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)), (\\Delta \_{\\omega \_{T}}-{\\mathrm{Id}})\\hat{v}\_{\\sigma} is equal to L\_{\\infty }\\hat{v} modulo the operator error O\_{\\delta}(\|b\|^{1/3}\|\\tau \|)\\hat{v}\_{\\sigma} from the second line of ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)). Moreover, \\check{\\partial} reduces to _d_/ _ds_. This explains ( [4.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ367)). Of course, L\_{\\infty}\\hat{v} = \\hat{u}, and the rest of the third line of ( [4.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ367)) obviously goes to zero uniformly as _σ_ →0.\
\
For item (2): In this proof we prefer to use _n_-dimensional notation for clarity. We fix a sufficiently small but universal _δ_ >0 and distinguish three subregions of \\mathfrak{R}\_{4} as follows.\
\
_Region (_ a _)_: _s_ =1− _η_ ∈\[ _δ_,1− _δ_\]. In this region, item (2) simply states that \\hat{u}\_{\\sigma} is bounded uniformly, independently of _σ_, and this statement is trivial from ( [4.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ367)) for _s_ 1= _δ_ and _s_ 2=1− _δ_.\
\
_Region (_ b _)_: _η_ ∈(0, _δ_\]. Here the goal is to prove that \|\\hat{u}\_{\\sigma}\| \\leqslant C\\eta ^{n+1} with _C_ independent of _σ_. We want to argue as in ( [4.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ367)) but _s_ 2 is not bounded away from 1, so we need to make the following changes:\
\
• Use the formula \\hat{v}\_{\\sigma }= \\chi \_{\\sigma}(1-\\cdot )\\hat{v} instead of \\hat{v}\_{\\sigma }= \\hat{v}.\
\
• Instead of using the charts ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)), which degenerate as _s_ 2→1, we estimate the difference between \\Delta \_{\\omega \_{glue,\\sigma}} and \\Delta \_{\\omega \_{T}} covariantly. Recall from Convention [4.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar85) and Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68) that _g_ _glue_, _σ_ and _g_ _T_ differ from each other by O(e^{-(1/2-\\varepsilon )(t-T)}) = O(e^{-(1/2)\|T\|^{\\alpha}}) uniformly over \\mathfrak{R}\_{4}, including derivatives. Also, from Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40), _g_ _T_ and _g_ _cusp_ are uniformly equivalent over {0< _η_ ⩽ _δ_}, including derivatives because both are Einstein. Thus, we can estimate\
\
\\begin{aligned} \\begin{aligned} \|(\\Delta \_{\\omega \_{glue,\\sigma}}-\\Delta \_{\\omega \_{T}})\\hat{v}\_{ \\sigma}\| &\\leqslant O\_{\\delta}(e^{-\\frac{1}{2}\|T\|^{\\alpha}})\\sum \_{k=1}^{2} \| \\nabla ^{k}\_{\\omega \_{cusp}}\\hat{v}\_{\\sigma}\|\_{\\omega \_{cusp}}\\\ &\\leqslant O\_{ \\delta}(e^{-\\frac{1}{2}\|T\|^{\\alpha}})(\\eta ^{2}\|\\hat{v}\_{\\sigma}''\| + \\eta \|\\hat{v}\_{\\sigma}'\|). \\end{aligned} \\end{aligned}\
\
(4.44)\
\
\
• Note that the operator error _O_ _δ_(\| _b_ \|1/( _n_ +1)\| _τ_ \|) from ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)) only depends on an upper bound for _η_. Thus, using ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)) and the fact that \\hat{v}\_{\\sigma} is radial, we have on all of {0< _η_ ⩽ _δ_} that\
\
\\begin{aligned} \\begin{aligned} \|(\\Delta \_{\\omega \_{T}} - {\\mathrm{Id}})\\hat{v}\_{\\sigma}\| = \|(L\_{\\infty }+ O\_{ \\delta}(\|b\|^{\\frac{1}{n+1}}\|\\tau \|))\\hat{v}\_{\\sigma}\|\\leqslant O\_{\\delta}(1) (\\eta ^{2}\|\\hat{v}\_{\\sigma}''\| + \\eta \|\\hat{v}\_{\\sigma}'\| + \|\\hat{v}\_{ \\sigma}\|). \\end{aligned} \\end{aligned}\
\
(4.45)\
\
\
The desired estimate of \\hat{u}\_{\\sigma} now easily follows from the estimates ( [4.38](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ362)) for \\hat{v} and ( [4.41](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ365)) for _χ_ _σ_.\
\
_Region (_ c _)_: _s_ ∈(0, _δ_\]. Here we prove that \|\\hat{u}\_{\\sigma}\| \\leqslant C with _C_ independent of _σ_. We again follow a similar pattern but now need to use ( [2.154](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ157)) instead of ( [2.144](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ147)) or ( [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ336)). Thus, we proceed as follows:

• We use the formula \\hat{v}\_{\\sigma }= \\chi \_{\\sigma}\\hat{v} + (1-\\chi \_{\\sigma})\\hat{v}(0).

• The comparison of _g_ _glue_, _σ_ and _g_ _T_ is the same as in (b). Then we compare _ω_ _T_ and \|b\|^{1/2}\\omega \_{\\mathcal{C},\\sigma} using ( [2.164](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ167))–( [2.165](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ168)). The comparison is uniform over {0< _s_ ⩽ _δ_} and each derivative costs at most a factor of \| _T_ \|_K_( _t_ − _T_)_K_ for some _K_ >0 as long as _t_ − _T_ ⩾1\. Thus,

\\begin{aligned} \\begin{aligned} \|(\\Delta \_{\\omega \_{glue,\\sigma}}-\\Delta \_{\\omega \_{T}})\\hat{v}\_{ \\sigma}\| \\leqslant O\_{\\delta}(e^{-\\frac{1}{2}\|T\|^{\\alpha}}\|T\|^{2K})(s^{ \\frac{n-1}{n}}\|\\hat{v}\_{\\sigma}''\| + s^{-\\frac{1}{n}}\|\\hat{v}\_{\\sigma}'\|). \\end{aligned} \\end{aligned}

(4.46)


• The operator error _O_ _δ_(\| _b_ \|1/( _n_ +1)\| _τ_ \|) from ( [2.154](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ157)) only depends on an upper bound for _s_. Applying ( [2.154](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ157)), we therefore get on all of {0< _s_ ⩽ _δ_} that

\\begin{aligned} \\begin{aligned} \|(\\Delta \_{\\omega \_{T}} - {\\mathrm{Id}})\\hat{v}\_{\\sigma}\| &= \|(L\_{\\infty }+ O\_{ \\delta}(\|b\|^{\\frac{1}{n+1}}\|\\tau \|))\\hat{v}\_{\\sigma}\|\\\ &\\leqslant O\_{\\delta}(1) (s^{\\frac{n-1}{n}}\|\\hat{v}\_{\\sigma}''\| + s^{-\\frac{1}{n}}\|\\hat{v}\_{ \\sigma}'\| + \|\\hat{v}\_{\\sigma}\|). \\end{aligned} \\end{aligned}

(4.47)


To estimate the right-hand sides of ( [4.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ370))–( [4.47](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ371)) we need to be a little more careful than in (b). First notice that the \|\\hat{v}\_{\\sigma}\| term in ( [4.47](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ371)) is obviously uniformly bounded. Next, \\hat{v}\_{\\sigma }= \\chi \_{\\sigma}(\\hat{v} - \\hat{v}(0)) + \\hat{v}(0), so in the remaining terms with \\hat{v}\_{\\sigma}', \\hat{v}\_{\\sigma}'' we can replace \\hat{v}\_{\\sigma} by \\chi \_{\\sigma}(\\hat{v} - \\hat{v}(0)). Using ( [4.41](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ365)) to estimate _χ_ _σ_ and ( [4.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ363)) to estimate \\hat{v} - \\hat{v}(0), we get the desired uniform bound. However, at this point it is crucially important that \\hat{v} satisfies a Neumann condition at _s_ =0, i.e., that the expansion of \\hat{v} - \\hat{v}(0) starts with _s_( _n_ +1)/ _n_ rather than _s_ 1/ _n_. (Otherwise the best bound we could get is \|\\hat{u}\_{\\sigma}\| \\leqslant Cs^{-1}, which is not L^{1}\_{loc}, destroying the dominated convergence argument in the proof of Proposition [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar86).) □

#### 4.1.6 Proof of Proposition [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar86)

As w\_{\\sigma \_{i}}(x\_{i}) \|\\psi \_{i}\| \\leqslant w\_{\\sigma \_{i}} on \\mathcal{X}\_{\\sigma \_{i}} and _x_ _i_ lies in \\mathfrak{R}\_{4} with _s_( _x_ _i_)→ _c_ ∈(0,1), we can deduce from the definition, ( [3.110](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ318)), of the weight function w\_{\\sigma \_{i}} that

\\begin{aligned} \|\\psi \_{i}\| \\leqslant \\textstyle\\begin{cases} C &\\text{on}\\;\\,\\mathfrak{R}\_{1}, \\\ C \\Psi \_{\\sigma}^{\*}(\\Phi \_{\\sigma}^{-1})^{\*} s^{-\\delta} &\\text{on}\\; \\,\\mathfrak{R}\_{2} \\cup \\mathfrak{R}\_{3} \\cup \\mathfrak{R}\_{4} \\cup \\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6}, \\\ C\|T\_{i}\|^{\\delta }&\\text{on}\\;\\,\\mathfrak{R}\_{7}. \\end{cases}\\displaystyle \\end{aligned}

(4.48)


Thus, RHS ( [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ328)) exists because ( [4.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ372)) implies \| _ψ_ ∞( _s_)\|⩽ _Cs_ − _δ_ for all _s_ ∈(0,1), and \|\\hat{u}(1-\\eta )\| \\leqslant C\\eta ^{3} from Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91) and \| _μ_ ∞(1− _η_)\|⩽ _Cη_ −3 from Lemma [2.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar48) for all _η_ ∈(0,1). We now decompose \\mathcal{X}\_{\\sigma \_{i}} into three regions and analyze their contributions to LHS ( [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ328)).

_Region_\\mathfrak{R}\_{1} \\cup \\mathfrak{R}\_{2} \\cup \\mathfrak{R}\_{3}: Here we obviously have \\hat{u}\_{\\sigma \_{i}}=0.

_Region_\\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6} \\cup \\mathfrak{R}\_{7}: Here \\hat{u}\_{\\sigma \_{i}} is constant equal to -\\hat{v}(0). In the unrescaled Tian-Yau space, volume grows like log _h_ as _h_ →∞. Thus, the volume of \\mathfrak{R}\_{5} \\cup \\mathfrak{R}\_{6} \\cup \\mathfrak{R}\_{7} with respect to \\omega \_{glue,\\sigma \_{i}} is bounded by _C_ \| _b_ _i_\|\| _T_ _i_\|_α_. Recalling that \| _b_ _i_\|∼\| _T_ _i_\|−3 and using the bound \| _ψ_ _i_\|⩽ _C_ \| _T_ _i_\|_δ_ from ( [4.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ372)), we get that the total contribution of this region to LHS ( [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ328)) goes to zero provided that _α_ + _δ_ <1\. This is consistent with our standing convention that _α_, _δ_ are always chosen arbitrarily close to zero.

_Region_\\mathfrak{R}\_{4}: By ( [2.173](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ176)), the volume form of \\omega \_{T\_{i}} satisfies for all _η_ =1− _s_ ∈(0,1) that

\\begin{aligned} \\omega \_{T\_{i}}^{2}\|\_{t=\\eta T\_{i}} = \|T\_{i}\|^{-2} \\mu \_{T\_{i}}(1- \\eta )\\, ds \\wedge d\\theta \\wedge d{\\mathrm{Vol}}\_{E}. \\end{aligned}

(4.49)


Thus, by Fubini, and using Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68) to compare the two volume forms,

\\begin{aligned} \\begin{aligned}&\|T\_{i}\|^{2}\\int \_{\\mathfrak{R}\_{4}}\\psi \_{i} \\hat{u}\_{\\sigma \_{i}}\\, \\omega \_{glue,\\sigma \_{i}}^{2}\\\ &\\quad = 2\\pi {\\mathrm{Vol}}(E)\\int \_{2\|T\_{i}\|^{ \\alpha -1}}^{1-2\\frac{\\tau \_{i}}{T\_{i}}} \\overline{\\psi \_{i} \\hat{u}\_{\\sigma \_{i}}}(s)\\,\\mu \_{T\_{i}}(s)(1 + O(e^{- \\frac{1}{2}\|T\_{i}\|^{\\alpha}}))\\,ds, \\end{aligned} \\end{aligned}

(4.50)


where the bar denotes the average over the relevant level set of _s_ with respect to the fixed volume form _dθ_ ∧ _d_ Vol_E_. By assumption and by Lemma [4.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar99), _ψ_ _i_→ _ϕ_ ∞ and \\hat{u}\_{\\sigma \_{i}} \\to \\hat{u} uniformly on every fixed level set of _s_. Thus, we obviously have that \\overline{\\psi \_{i} \\hat{u}\_{i}}(s) \\to \\phi \_{\\infty}(s)\\hat{u}(s) for every fixed _s_. Thus, the integrand on the right-hand side of ( [4.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ374)) converges pointwise to \\psi \_{\\infty}(s)\\hat{u}(s)\\,\\mu \_{\\infty}(s). It is also uniformly bounded by _Cs_ − _δ_⋅ _Cη_ 3⋅ _Cη_ −3⩽ _Cs_ − _δ_ thanks to ( [4.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ372)), Lemma [4.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar99) and Lemma [2.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar48). Since _Cs_ − _δ_ is integrable on (0,1), dominated convergence implies that ( [4.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ374)) converges to the right-hand side of ( [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ328)). □

### 4.2 Statement of the uniform estimate modulo obstructions and set-up of the proof

Here we state the uniform weighted Hölder estimate of the inverse linearized operator modulo obstructions and explain the strategy of the proof. This is the standard blowup-and-contradiction scheme common to this type of problem, and the aim is to obtain a contradiction to some Liouville theorem in each of the 7 cases. In Sects. [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec30)– [4.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec34) we carry out the details of this scheme in each case.

### Definition 4.11

Given the obstruction function \\hat{u}\_{\\sigma }= L\_{\\sigma }\\hat{v}\_{\\sigma} from Definition [4.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar98), we define

\\begin{aligned} \\langle \\hat{u}\_{\\sigma }\\rangle := \\mathbb{R} \\cdot \\hat{u}\_{\\sigma} \\;\\,\\text{and}\\;\\,\\langle \\hat{v}\_{\\sigma }\\rangle := \\mathbb{R} \\cdot \\hat{v}\_{\\sigma } \\end{aligned}

(4.51)


as 1-dimensional subspaces of C^{\\infty}(\\mathcal{X}\_{\\sigma}). We also write

\\begin{aligned} L\_{\\sigma}^{\\perp}: \\langle \\hat{u}\_{\\sigma }\\rangle ^{\\perp }\\to \\langle \\hat{v}\_{\\sigma }\\rangle ^{\\perp } \\end{aligned}

(4.52)


to denote the restriction of L\_{\\sigma }= \\Delta \_{\\omega \_{glue,\\sigma}} - {\\mathrm{Id}} to the orthogonal complements of \\langle \\hat{u}\_{\\sigma}\\rangle  resp. \\langle \\hat{v}\_{\\sigma}\\rangle  inside C^{2,\\bar{\\alpha}}(\\mathcal{X}\_{\\sigma}) resp. C^{0,\\bar{\\alpha}}(\\mathcal{X}\_{\\sigma}) with respect to the L^{2}(\\mathcal{X}\_{\\sigma}, \\omega \_{glue, \\sigma})-inner product for any \\bar{\\alpha}\\in (0,1). By basic elliptic theory, L\_{\\sigma}^{\\perp} is properly defined and is an isomorphism of Banach spaces.

### Theorem 4.12

_For all_\\bar{\\alpha}\\in (0,1) _there exists a constant_ C(\\bar{\\alpha}) _independent of_ _σ_ _such that_

\\begin{aligned} \\\|\\phi \\\|\_{C^{2,\\bar{\\alpha}}\_{w}} \\leqslant C(\\bar{\\alpha})\\\|L\_{\\sigma}^{ \\perp}\\phi \\\|\_{C\_{\\tilde{w}}^{0,\\bar{\\alpha}}} \\end{aligned}

(4.53)


_for all_ 0<\| _σ_ \|≪1 _and for all_\\phi \\in \\langle \\hat{u}\_{\\sigma }\\rangle ^{\\perp }\\subset C^{2, \\bar{\\alpha}}(\\mathcal{X}\_{\\sigma}).

Using the standard weighted Schauder estimates ( [3.116](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ324)), the theorem reduces to proving that

\\begin{aligned} \\\|\\phi \\\|\_{C\_{w}^{0}} \\leqslant C\\\|L\_{\\sigma}^{\\perp}\\phi \\\|\_{C\_{\\tilde{w}}^{0}}. \\end{aligned}

(4.54)


We prove this estimate by contradiction in the rest of Sect. [4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec17), starting now.

Assume that there is a sequence of functions \\phi \_{i} \\in \\langle \\hat{u}\_{\\sigma \_{i}} \\rangle ^{\\perp } \\subset C^{2,\\bar{\\alpha}} (\\mathcal{X}\_{\\sigma \_{i}}) such that _σ_ _i_→0 and

\\begin{aligned} 1 = \\\|\\phi \_{i}\\\|\_{C^{0}\_{w}} > i \\\|L\_{\\sigma \_{i}} \\phi \_{i}\\\|\_{C^{0}\_{ \\tilde{w}}}. \\end{aligned}

(4.55)


Let x\_{i} \\in \\mathcal{X}\_{\\sigma \_{i}} such that \|\\phi \_{i}(x\_{i})\| = w\_{\\sigma \_{i}}(x\_{i}). Set

\\begin{aligned} \\psi \_{i} := \\frac{\\phi \_{i}}{w\_{\\sigma \_{i}}(x\_{i})}. \\end{aligned}

(4.56)


Then _ψ_ _i_( _x_ _i_)=1 and

\\begin{aligned} \|\\psi \_{i}\|\\leqslant \\frac{w\_{\\sigma \_{i}}}{w\_{\\sigma \_{i}}(x\_{i})}. \\end{aligned}

(4.57)


### Assumption I

It is possible to choose scaling factors _μ_ _i_⩾1 such that if

\\begin{aligned} \\tilde{g}\_{i} := \\mu \_{i}^{2} g\_{glue,\\sigma \_{i}}, \\end{aligned}

(4.58)


then the spaces (\\mathcal{X}\_{\\sigma \_{i}}, \\tilde{g}\_{i}, x\_{i}) have a pointed Cheeger-Gromov limit (possibly collapsed) and the functions w\_{\\sigma \_{i}}/w\_{\\sigma \_{i}(x\_{i})} have a locally uniform limit _w_ ∞ under this pointed Cheeger-Gromov convergence.

Then the rescaled operators

\\begin{aligned} \\tilde{L}\_{i} := \\Delta \_{\\tilde{g}\_{i}} -\\mu \_{i}^{-2} {\\mathrm{Id}} = \\mu \_{i}^{-2} (\\Delta \_{g\_{\\sigma \_{i}}} - {\\mathrm{Id}})=\\mu \_{i}^{-2} L\_{ \\sigma \_{i}} \\end{aligned}

(4.59)


satisfy

\\begin{aligned} \|\\tilde{L}\_{i}\\psi \_{i}\| =\\mu \_{i}^{-2} \\frac{\|L\_{\\sigma \_{i}} \\phi \_{i}\|}{w\_{\\sigma \_{i}}(x\_{i})} < \\mu \_{i}^{-2} \\frac{1}{i} \\frac{\\tilde{w}\_{\\sigma \_{i}} }{w\_{\\sigma \_{i}}(x\_{i})}. \\end{aligned}

(4.60)


This will converge to 0 locally uniformly if we additionally make the following assumption:

### Assumption II

The sequence

\\begin{aligned} \\mu \_{i}^{-2}\\frac{ \\tilde{w}\_{\\sigma \_{i}}}{w\_{\\sigma \_{i}}(x\_{i})} \\end{aligned}

(4.61)


is locally uniformly bounded under the Cheeger-Gromov limit of Assumption [I](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar103).

In this situation, we can pass _ψ_ _i_ to a subsequential limit _ψ_ ∞ weakly in W^{2,p}\_{loc} and strongly in C^{1,\\beta}\_{loc} for all _p_, _β_, where _ψ_ ∞ is smooth and satisfies an elliptic equation \\tilde{L}\_{\\infty }\\psi \_{\\infty }= 0. This is clear from standard elliptic compactness and regularity if there is no collapsing in the Cheeger-Gromov limit, and in this case \\tilde{L}\_{\\infty }= \\Delta \_{\\tilde{g}\_{\\infty}} - \\mu \_{\\infty}^{-2} \\, {\\mathrm{Id}}. In the collapsing cases, we first need to pass to a local universal cover and work in quasi-coordinates. Then _ψ_ ∞ will be radial and \\tilde{L}\_{\\infty} will reduce to an ODE operator. See the proof of Lemma [4.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar87) for the details of this argument in the most complicated case (region \\mathfrak{R}\_{4}).

### Assumption III

There is a Liouville theorem: \\tilde{L}\_{\\infty} \\psi \_{\\infty }=0 and \| _ψ_ ∞\|⩽ _w_ ∞ imply _ψ_ ∞=0.

This contradicts the property _ψ_ ∞( _x_ ∞)=1, which holds due to strong C^{1,\\beta}\_{loc} convergence.

In the following sections, we will show that up to passing to subsequences, the above Assumptions [I](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar103), [II](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar104) and [III](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar105) are indeed satisfied in our situation. The resulting contradictions prove Theorem [4.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar102).

### 4.3 GH limit and Liouville on the Kähler-Einstein building block (region \\mathfrak{R}\_{1})

Assume that after passing to a subsequence we have for all _i_ that x\_{i} \\in \\mathfrak{R}\_{1}, or x\_{i} \\in \\mathfrak{R}\_{2} with _t_( _x_ _i_) uniformly bounded from below. Then we set _μ_ _i_:=1\. The pointed limit space of the sequence (\\mathcal{X}\_{\\sigma \_{i}}, \\tilde{g}\_{i}, x\_{i}) is the complete cuspidal Kähler-Einstein manifold (\\mathcal{X}\_{0}^{reg}, g\_{KE,0}). We now verify our three assumptions.

[I](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar103): For simplicity we only consider the case x,x\_{i} \\notin \\mathfrak{R}\_{1}, so that _t_( _x_), _t_( _x_ _i_) are actually defined. They are then uniformly bounded above and below, so

\\begin{aligned} \\begin{aligned} \\frac{w\_{\\sigma \_{i}}(x)}{w\_{\\sigma \_{i}}(x\_{i})} &= \\frac{(t(x)-T\_{i})^{-\\delta}}{(t(x\_{i})-T\_{i})^{-\\delta}}\\rightarrow 1 \\end{aligned} \\end{aligned}

(4.62)


locally uniformly. Hence _w_ ∞=1.

[II](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar104): Again assuming x,x\_{i} \\notin \\mathfrak{R}\_{1} we have that

\\begin{aligned} \\mu \_{i}^{-2} \\frac{\\tilde{w}\_{\\sigma \_{i}}(x)}{w\_{\\sigma \_{i}}(x\_{i})} = \|b\_{i}\|^{- \\frac{1}{2}}(t(x)-T\_{i})^{-\\frac{3}{2}} \\frac{w\_{\\sigma \_{i}}(x)}{w\_{\\sigma \_{i}}(x\_{i})} \\to 1 \\end{aligned}

(4.63)


locally uniformly because of [I](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar103) and because \| _b_ _i_\|∼\| _T_ _i_\|−3.

[III](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar105): By the generalized maximum principle on complete Riemannian manifolds with Ricci curvature bounded below \[ [Yau75](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR39 " 					Yau, S.-T.: Harmonic functions on complete Riemannian manifolds. Comm. Pure Appl. Math. 28, 201–228 (1975) 				"), p.207, Cor 1\], there is a sequence _y_ _i_ in \\mathcal {X}\_{0}^{reg} such that lim_i_ →∞ _ψ_ ∞( _y_ _i_)=sup _ψ_ ∞ and \\limsup \_{i\\rightarrow \\infty} \\Delta \_{g\_{KE,0}}\\psi \_{\\infty}(y\_{i}) \\leqslant 0. From the equation \\tilde{L}\_{\\infty} \\psi \_{\\infty }=0 one has \\psi \_{\\infty}(y\_{i})=\\Delta \_{g\_{KE,0}} \\psi \_{\\infty}(y\_{i}), hence sup _ψ_ ∞⩽0\. Similarly, we can show inf _ψ_ ∞⩾0\. Hence _ψ_ ∞=0.

### 4.4 GH limit and Liouville on the cusp (regions \\mathfrak{R}\_{2}, \\mathfrak{R}\_{3})

#### 4.4.1 Region \\mathfrak{R}\_{2}: the genuine cusp

Here we assume that x\_{i} \\in \\mathfrak{R}\_{2} for all _i_. Also, we assume that _x_ _i_ tends to have infinite distance from \\mathfrak{R}\_{1} as well as from \\mathfrak{R}\_{3}. Precisely,

\\begin{aligned} t(x\_{i}) \\rightarrow -\\infty , \\quad t(x\_{i})/\\tau \_{i} \\rightarrow 0. \\end{aligned}

(4.64)


We set _μ_ _i_:=1\. The Gromov-Hausdorff limit (better: the collapsed Cheeger-Gromov limit) in this case is a line. [I](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar103) and [II](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar104) work exactly as in the previous case because \| _t_( _x_ _i_)\|= _o_(\| _τ_ _i_\|)= _o_(\| _T_ _i_\|).

[III](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar105): Proceeding as in the proof of Lemma [4.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar87), we obtain a smooth limit function _ψ_ ∞( _t_) with

\\begin{aligned} \\tilde{L}\_{\\infty}\\psi \_{\\infty }= \\frac{1}{3}\\left ( t^{2} \\frac{d^{2}\\psi \_{\\infty}}{d t^{2}} -t\\frac{d\\psi \_{\\infty}}{d t} \\right ) - \\psi \_{\\infty }= 0. \\end{aligned}

(4.65)


Thus, _ψ_ ∞( _t_)= _a_(− _t_)3+ _b_(− _t_)−1, where _a_, _b_ are constants. _w_ ∞=1 rules out all possibilities.

#### 4.4.2 Region \\mathfrak{R}\_{3}: the green gluing region between the cusp and the new neck

In this case, we consider the region within finite distance from \\mathfrak{R}\_{3} with respect to g\_{glue,\\sigma \_{i}}. More precisely, we assume that

\\begin{aligned} t(x\_{i}) \\rightarrow -\\infty , \\quad t(x\_{i})/\\tau \_{i} \\rightarrow c \\in (0, \\infty ). \\end{aligned}

(4.66)


Set _μ_ _i_:=1 and apply Lemma [2.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar37), extended so that ( [2.119](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ122)) holds for _t_ ∈\[ _Cτ_ _i_, _C_ −1 _τ_ _i_\] given any fixed constant _C_ >1\. The remainder of the discussion is similar to that in the case of region \\mathfrak{R}\_{2}.

### 4.5 GH limit and Liouville on the Tian-Yau building block (region \\mathfrak{R}\_{7})

Consider the case that the points _x_ _i_ stay on the Tian-Yau side, i.e., for all _i_ we either have that x\_{i} \\in \\mathfrak{R}\_{7}, or x\_{i} \\in \\mathfrak{R}\_{6} and t(x\_{i}) - T\_{i} = \\log h(m\_{\\sigma \_{i}}(x\_{i})) remains uniformly bounded above. Set _μ_ _i_:=\| _b_ _i_\|−1/4. Then \\tilde{g}\_{i} =m\_{\\sigma \_{i}}^{\*} g\_{TY\_{1}} and the pointed limit space is (TY\_{1},g\_{TY\_{1}}) after applying the map m\_{\\sigma \_{i}}.

We now apply the map m\_{\\sigma \_{i}} without writing it explicitly. Thus, _x_ _i_∈ _TY_ 1 and log _h_( _x_ _i_)⩽ _N_.

For the three conditions, first, by taking a subsequence we can assume that w\_{\\sigma \_{i}}(x\_{i})\\rightarrow c \\in \[N^{-\\delta} ,1\]. Then w\_{\\sigma \_{i}}/w\_{\\sigma \_{i}}(x\_{i}) converges locally uniformly to _c_ −1 on \\mathfrak{R}\_{7} and to _c_ −1(log _h_)− _δ_ on \\mathfrak{R}\_{6}. Next,

\\begin{aligned} \\mu \_{i}^{-2}\\frac{\\tilde{w}\_{\\sigma \_{i}}}{w\_{\\sigma \_{i}}(x\_{i})} = \|b\_{i}\|^{ \\frac{1}{2}}\\cdot \\left (\|b\_{i}\|^{\\frac{1}{4}}(\\log h)^{\\frac{3}{4}} \\right )^{-2} \\cdot \\frac{w\_{\\sigma \_{i}}}{w\_{\\sigma \_{i}}(x\_{i})} \\end{aligned}

(4.67)


is locally uniformly convergent by the previous step. Lastly,

\\begin{aligned} \\tilde{L}\_{\\infty} \\psi \_{\\infty }= \\Delta \_{g\_{TY\_{1}}} \\psi \_{ \\infty }= 0,\\quad \|\\psi \_{\\infty}\| \\leqslant c^{-1} (\\log h)^{-\\delta}\\;\\, \\text{as}\\;\\,h \\to \\infty . \\end{aligned}

(4.68)


Then the maximum principle implies that _ψ_ ∞=0.

### 4.6 GH limit and Liouville on the Tian-Yau end (regions \\mathfrak{R}\_{6}, \\mathfrak{R}\_{5})

#### 4.6.1 Region \\mathfrak{R}\_{6}: the genuine Tian-Yau end

In this case, we assume that the points _x_ _i_ lie strictly in the interior of region \\mathfrak{R}\_{6} in the sense that

\\begin{aligned} t(x\_{i}) - T\_{i} \\to \\infty , \\quad \\rho (x\_{i})^{-1} \|T\_{i}\|^{ \\frac{3}{4}\\alpha} \\rightarrow \\infty , \\end{aligned}

(4.69)


where _ρ_ is a geometric distance function for the unrescaled Tian-Yau metric,

\\begin{aligned} \\rho (x) := (t(x) -T\_{i})^{\\frac{3}{4}}. \\end{aligned}

(4.70)


Then we define our scaling factors by

\\begin{aligned} \\mu \_{i} := \\rho (x\_{i})^{-1}\|b\_{i}\|^{-\\frac{1}{4}} \\gg \|T\_{i}\|^{ \\frac{3}{4}(1-\\alpha )} \\to \\infty , \\end{aligned}

(4.71)