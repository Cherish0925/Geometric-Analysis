---
retention_scope: session
part: 4
total_parts: 7
---

[Part 4/7 of: A Continuous Cusp Closing Process for Negative Kähler–Einstein Metrics]

Abuse notation by denoting (\\Psi \_{\\sigma}^{-1})^{\*}\\psi \_{FS,\\sigma} by _ψ_ _FS_, _σ_ for all sufficiently small values of _σ_, including for _σ_ =0\. This is a Kähler potential on the intersection of _TY_ _σ_ with some fixed neighborhood of the origin in \\mathbb{C}^{3}. Let _z_ ∈ _TY_ 0 with

\\begin{aligned} \|\\sigma \|^{\\frac{1}{3}}R \\leqslant \|z\|\\leqslant \\varepsilon , \\end{aligned}

(3.21)


where _ε_ is a sufficiently small constant independent of _σ_ and _R_ is a large constant as in Lemma [2.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar7). Let \\omega \_{flat}:=i\\partial \\overline {\\partial }\|z\|^{2} be the flat metric on \\mathbb{C}^{3}. Then for _k_ =0,1 and for \| _σ_ \|−1/3\| _z_ \|→∞,

\\begin{aligned} \\left \|\\nabla ^{k}\_{\\omega \_{flat}\|\_{TY\_{0}}}\\left (\\Phi ^{\*}\_{\\sigma} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{FS,\\sigma}-i\\partial \\overline {\\partial }\\psi \_{FS,0}\\right )\\right \|\_{ \\omega \_{flat}\|\_{TY\_{0}}}=O(\|\\sigma \|\|z\|^{-3-k}), \\end{aligned}

(3.22)


\\begin{aligned} \\left \|\\nabla ^{k}\_{\\omega \_{flat}\|\_{TY\_{0}}}i\\partial \\overline {\\partial }\\left (\\Phi ^{\*}\_{ \\sigma }\\psi \_{FS,\\sigma}-\\psi \_{FS,0}\\right )\\right \|\_{\\omega \_{flat}\|\_{TY\_{0}}}=O(\| \\sigma \|\|z\|^{-3-k}). \\end{aligned}

(3.23)


### Proof

We only prove ( [3.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ230)) as the proof of ( [3.23](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ231)) is similar. To prove ( [3.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ230)), we start with

### Claim 3.12

One has

\\begin{aligned} \\begin{aligned} \\Phi ^{\*}\_{\\sigma} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{FS,\\sigma}-i\\partial \\overline {\\partial }\\psi \_{FS,0}= \\biggl(\\sum \\nolimits \_{\|I\|+\|J\|=2}\\tilde{O}(\|\\sigma \|\|z\|^{-3}) dz\_{I} \\wedge d\\overline{z}\_{J}\\biggr)\\biggr\|\_{TY\_{0}}, \\end{aligned} \\end{aligned}

(3.24)


where \\tilde{O}(\|\\sigma \|\|z\|^{-3}) is a function on B\_{\\varepsilon}(0)\\subset \\mathbb{C}^{3} such that for all _k_ ⩾0 and \| _σ_ \|−1/3\| _z_ \|→∞,

\\left \|\\partial ^{k}\\tilde{O}(\|\\sigma \|\|z\|^{-3})\\right \|=O(\|\\sigma \|\|z\|^{-3-k}).

(3.25)


### Proof of Claim [3.12](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar72)

The key is the following expression of Φ_σ_ from Lemma [2.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar7):

\\Phi \_{\\sigma}^{\*}z\_{i}=z\_{i}+\\nu \_{\\sigma}(z)\\overline{z}\_{i}^{2}\\; \\,(i = 1,2,3).

(3.26)


Hence, dropping the restriction symbols for simplicity,

\\Phi \_{\\sigma}^{\*} (dz\_{i})=dz\_{i}+2\\nu \_{\\sigma}(z)\\overline{z}\_{i}dz\_{i}+ \\sum \_{j=1}^{3}\\frac{\\partial \\nu \_{\\sigma}(z)}{\\partial z\_{j}} \\overline{z}\_{i}^{2}dz\_{j}+\\sum \_{j=1}^{3} \\frac{\\partial \\nu \_{\\sigma}(z)}{\\partial \\overline{z}\_{j}} \\overline{z}\_{i}^{2}d\\overline{z}\_{j}.

(3.27)


From Lemma [2.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar7) we have for all _ℓ_ ⩾0 and for \| _σ_ \|−1/3\| _z_ \|→∞ that

\\left \|\\partial ^{\\ell}\\nu \_{\\sigma}(z)\\right \|=O(\|\\sigma \|\|z\|^{-4- \\ell}).

(3.28)


Therefore

\\Phi \_{\\sigma}^{\*}(dz\_{i})=dz\_{i}+\\sum \_{j=1}^{3}\\tilde{O}(\|\\sigma \|\|z\|^{-3})dz\_{j}+ \\sum \_{j=1}^{3}\\tilde{O}(\|\\sigma \|\|z\|^{-3})d\\overline{z}\_{j}.

(3.29)


On \\mathbb{C}^{3}, when \| _z_ \|⩽ _ε_ for some sufficiently small constant _ε_, we have that

\\begin{aligned} i\\partial \\overline {\\partial }\\psi \_{FS}=\\sum \_{i,j=1}^{3} a\_{i \\bar{\\jmath}}(z)dz\_{i}\\wedge d \\overline{z}\_{j},\\;\\,a\_{i\\bar{\\jmath}} = \\delta \_{i\\bar{\\jmath}} + O(\|z\|^{2}) \\;\\,\\text{as}\\;\\,\|z\| \\to 0, \\end{aligned}

(3.30)


and a\_{i \\bar{\\jmath}}(z) is actually real-analytic in _z_. Then, from ( [3.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ234)) and ( [3.28](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ236)),

\\Phi \_{\\sigma}^{\*} a\_{i\\bar{\\jmath}}(z)-a\_{i\\bar{\\jmath}}(z)=\\tilde{O}(\| \\sigma \|\|z\|^{-1})\\;\\, \\text{as}\\;\\,\|\\sigma \|^{-\\frac{1}{3}}\|z\|\\to \\infty .

(3.31)


For example, if z\_{1}^{2} appears in a\_{i \\bar{\\jmath}}(z), then the relevant difference is

\\begin{aligned} \\begin{aligned} (z\_{1}+\\nu \_{\\sigma}(z)\\overline{z}\_{1}^{2})^{2} -z\_{1}^{2} &= 2\\nu \_{ \\sigma}(z) z\_{1} \\overline{z}\_{1}^{2}+\\nu \_{\\sigma}(z)^{2} \\overline{z}\_{1}^{4} \\\ &=O(\|\\sigma \|\|z\|^{-1}) +O(\|\\sigma \|^{2}\|z\|^{-4})\\;\\,\\text{as}\\;\\,\| \\sigma \|^{-\\frac{1}{3}}\|z\| \\to \\infty , \\end{aligned} \\end{aligned}

(3.32)


which is _O_(\| _σ_ \|\| _z_ \|−1) because \| _σ_ \|\| _z_ \|−3= _o_(1).

Then Claim [3.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar72) follows from ( [3.29](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ237)) and ( [3.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ239)) because \| _z_ \|−1⩽ _ε_ 2\| _z_ \|−3. □

Next, we estimate the 2-form ( [3.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ232)) with respect to the metric \\omega \_{flat}\|\_{TY\_{0}}. To do so, without loss of generality (using the symmetry of _z_ 1, _z_ 2, _z_ 3) we may assume that \| _z_ 3\|⩾max{\| _z_ 1\|,\| _z_ 2\|}. In particular, we are working on the affine piece _z_ 3≠0\. From the defining equation of _TY_ 0,

dz\_{3}=-\\frac{z\_{1}^{2}}{z\_{3}^{2}}dz\_{1}-\\frac{z\_{2}^{2}}{z\_{3}^{2}}dz\_{2},

(3.33)


where we are again dropping the restriction symbols. Thus,

\\begin{aligned} \\begin{aligned} \\omega \_{flat}\|\_{TY\_{0}}=&\\left (1+\\left \|\\frac{z\_{1}}{z\_{3}}\\right \|^{4} \\right )dz\_{1}\\wedge d\\overline{z}\_{1}+\\left (1+\\left \| \\frac{z\_{2}}{z\_{3}}\\right \|^{4}\\right )dz\_{2}\\wedge d\\overline{z}\_{2} \\\ &+\\left (\\frac{z\_{1}^{2}}{z\_{3}^{2}} \\frac{\\overline{z}\_{2}^{2}}{\\overline{z}\_{3}^{2}}\\right )dz\_{1} \\wedge d\\overline{z}\_{2}+\\left (\\frac{z\_{2}^{2}}{z\_{3}^{2}} \\frac{\\overline{z}\_{1}^{2}}{\\overline{z}\_{3}^{2}}\\right )dz\_{2} \\wedge d\\overline{z}\_{1}. \\end{aligned} \\end{aligned}

(3.34)


Viewing _z_ 1, _z_ 2 as local coordinates and denoting the coefficients of the Kähler form in ( [3.34](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ242)) by g\_{i\\bar{\\jmath}}, it is easy to see that \\det (g\_{i\\bar{\\jmath}})\\geqslant 1, so every component of the inverse matrix g^{\\bar{\\imath}j} is bounded by 2 because \| _z_ 3\|⩾max{\| _z_ 1\|,\| _z_ 2\|}. This fact and ( [3.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ232)) imply the desired estimate ( [3.22](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ230)) for _k_ =0.

To finish the proof, we also need to estimate the first covariant derivative of ( [3.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ232)) with respect to \\omega \_{flat}\|\_{TY\_{0}}. Applying -z\_{3}^{3}=z\_{1}^{3}+z\_{2}^{3} and \| _z_ 3\|⩾max{\| _z_ 1\|,\| _z_ 2\|}, we have that

\\begin{aligned} \\begin{aligned} \\frac{\\partial z\_{3}}{\\partial z\_{1}}=-\\frac{z\_{1}^{2}}{z\_{3}^{2}} = O(1), \\;\\, \\frac{\\partial z\_{3}}{\\partial z\_{2}}=- \\frac{z\_{2}^{2}}{z\_{3}^{2}} = O(1). \\end{aligned} \\end{aligned}

(3.35)


Combining the claimed estimates ( [3.25](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ233)) and ( [3.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ243)), it follows from the chain rule that

\\begin{aligned} \\begin{aligned} \\left \\vert \\frac{\\partial \\tilde{O}(\|\\sigma \|\|z\|^{-3})}{\\partial z\_{i}} \\right \\vert + \\left \\vert \\frac{\\partial \\tilde{O}(\|\\sigma \|\|z\|^{-3})}{\\partial \\overline{z}\_{i}} \\right \\vert =O(\|\\sigma \|\|z\|^{-4})\\;\\,(i=1,2). \\end{aligned} \\end{aligned}

(3.36)


The remaining task is to bound the first covariant derivative of _dz_ 1, _dz_ 2, _dz_ 3 with respect to \\omega \_{flat}\|\_{TY\_{0}}. Since g^{\\bar{\\imath}j} is bounded, it is enough to bound the second partials of _z_ 1, _z_ 2, _z_ 3 and the first partials of g\_{i\\bar{\\jmath}}. This can be done by differentiating ( [3.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ243)) and ( [3.34](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ242)), respectively. Because of homogeneity reasons it is clear that all of these derivatives are bounded by a constant times \| _z_ \|−1. □

### Lemma 3.13

We work on _TY_ 0 and abuse notation by replacing

\\begin{aligned} \\begin{aligned} (\\Psi \_{0}^{-1})^{\*}\\omega \_{KE,0} \\leadsto \\omega \_{KE,0},\\;\\; ( \\Psi \_{0}^{-1})^{\*}\\psi \_{0} \\leadsto \\psi \_{0}, \\;\\; (\\Psi \_{\\sigma}^{-1})^{\*} \\psi \_{FS,\\sigma} \\leadsto \\psi \_{FS,\\sigma}. \\end{aligned} \\end{aligned}

(3.37)


Let _N_ >0 be a fixed large constant. Then for _k_ =0,1 and _t_ ∈\[2 _τ_,− _N_\] we have that

\\left \|\\nabla ^{k}\_{\\omega \_{KE,0}} \\frac{(\\Phi ^{\*}\_{\\sigma} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma ((\\Phi ^{-1}\_{\\sigma})^{\*}\\psi \_{0}+\\psi \_{FS,\\sigma}))^{2}-\\omega ^{2}\_{KE,0}}{\\omega ^{2}\_{KE,0}} \\right \|\_{\\omega \_{KE,0}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}).

(3.38)


### Proof

Inserting one more term, we have

\\begin{aligned} \\begin{aligned} \\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma ((\\Phi ^{-1}\_{\\sigma})^{\*}\\psi \_{0}+\\psi \_{FS, \\sigma}))^{2}-\\omega ^{2}\_{KE,0}=(i\\partial \\overline {\\partial }(\\psi \_{0}+\\Phi ^{\*}\_{\\sigma} \\psi \_{FS,\\sigma}))^{2}-\\omega ^{2}\_{KE,0} \\\ +\\;\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma ((\\Phi ^{-1}\_{\\sigma})^{\*}\\psi \_{0}+ \\psi \_{FS,\\sigma}))^{2}-(i\\partial \\overline {\\partial }(\\psi \_{0}+\\Phi \_{\\sigma}^{\*}\\psi \_{FS, \\sigma}))^{2}. \\end{aligned} \\end{aligned}

(3.39)


We begin by estimating the first line of ( [3.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ247)). Canceling i\\partial \\overline {\\partial }\\psi \_{0}, one has

\\begin{aligned} i\\partial \\overline {\\partial }(\\psi \_{0}+\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma})-\\omega \_{KE,0}= i\\partial \\overline {\\partial }(\\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma}-\\psi \_{FS,0}). \\end{aligned}

(3.40)


For 2-forms _ω_ 1, _ω_ 2, one has

\\begin{aligned} \\omega \_{1}^{2} - \\omega \_{2}^{2} &=2(\\omega \_{1} -\\omega \_{2}) \\wedge \\omega \_{2} +(\\omega \_{1}-\\omega \_{2})^{2}, \\end{aligned}

(3.41)


which implies that

\\begin{aligned} &\\frac{(i\\partial \\overline {\\partial }(\\psi \_{0}+\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma}))^{2}-\\omega ^{2}\_{KE,0}}{\\omega ^{2}\_{KE,0}}\\\ &\\quad=2 \\Delta \_{\\omega \_{KE,0}}(\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma}-\\psi \_{FS,0})+ \\frac{(i\\partial \\overline {\\partial }(\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma}-\\psi \_{FS,0}))^{2}}{\\omega ^{2}\_{KE,0}}. \\end{aligned}

(3.42)


To estimate these terms, we replace the reference metric _ω_ _KE_,0 by \\omega \_{flat}\|\_{TY\_{0}}.

### Claim 3.14

For any _j_ ⩾0 there is a positive integer _K_ _j_ such that as \| _z_ \|→0,

\|\\nabla ^{j}\_{\\omega \_{KE,0}}(\\omega \_{flat}\|\_{TY\_{0}})\|\_{\\omega \_{KE,0}} = O(\|z\|^{2}\|t\|^{K\_{j}}).

(3.43)


Moreover, for _j_ =0 the left-hand side is actually uniformly equivalent to \|z\|^{2} \|t\|^{K\_{0}}.

### Proof of Claim [3.14](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar76)

Thanks to \[ [DFS23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR10 " 					Datar, V., Fu, X., Song, J.: Kähler-Einstein metric near an isolated log canonical singularity. J. Reine Angew. Math. 797, 79–116 (2023) 				"), Thm 1.4\], _ω_ _cusp_ and _ω_ _KE_,0 are uniformly equivalent to any order for _t_ ⩽− _N_, so it suffices to prove the estimate using _ω_ _cusp_ as the reference metric.

On _TY_ 0∖{0} we clearly have that \| _z_ \|2= _e_ _t_ + _ψ_ for some smooth function _ψ_ on the elliptic curve _E_, viewed as a 0-homogeneous function on _TY_ 0∖{0}. Thus,

\\begin{aligned} \\omega \_{flat}\|\_{TY\_{0}}=i\\partial \\overline {\\partial }e^{t+\\psi}&=e^{t+\\psi} i\\partial \\overline {\\partial }(t+\\psi )+e^{t+ \\psi}i\\partial (t+\\psi )\\wedge \\overline{\\partial}(t+\\psi ). \\end{aligned}

(3.44)


For any fixed _t_ ∗⩽− _N_, quasi-coordinates for _ω_ _cusp_ on a neighborhood of the hypersurface { _t_ = _t_ ∗} are given by (\\rho ,\\check{x},\\check{y},\\check{\\theta}), where _ρ_ =log\| _t_ \|, (\\check{x},\\check{y}) = \|t\_{\*}\|^{-1/2}(x,y) for a fixed pair ( _x_, _y_) of linear coordinates on _E_ and \\check{\\theta}= \|t\_{\*}\|^{-1}\\theta  for a fixed angular coordinate _θ_ along the Hopf circles in \\mathbb{C}^{3}. Moreover,

\\begin{aligned} \\begin{aligned} &i\\partial \\overline {\\partial }t = \|t\_{\*}\| \\cdot ( \\textit{a fixed $2$-form in }\\check{x},\\check{y}),\\\ &\\partial t = - \\frac{1}{2}e^{\\rho }d\\rho + \|t\_{\*}\| \\cdot ( \\textit{a fixed $1$-form in }\\check{x},\\check{y},\\check{\\theta}). \\end{aligned} \\end{aligned}

(3.45)


Because covariant derivatives with respect to _ω_ _cusp_ are equivalent to ordinary partial derivatives with respect to (\\rho ,\\check{x},\\check{y},\\check{\\theta}), the claim follows from ( [3.44](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ252)) and ( [3.45](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ253)). □

We now estimate the terms on the right-hand side of ( [3.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ250)). By Lemma [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar70) and Claim [3.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar76),

\\begin{aligned} \\begin{aligned} &\|\\Delta \_{\\omega \_{KE,0}}(\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma}-\\psi \_{FS,0})\| \\\ &\\leqslant \|i\\partial \\overline{\\partial} (\\Phi ^{\*}\_{\\sigma}\\psi \_{FS, \\sigma}-\\psi \_{FS,0})\|\_{\\omega \_{flat}\|\_{TY\_{0}}} \\cdot {\\mathrm{{tr}}}\_{ \\omega \_{KE,0}}(\\omega \_{flat}\|\_{TY\_{0}}) \\\ &=O(\|\\sigma \|\|z\|^{-3} \|z\|^{2}\|t\|^{K\_{0}}) \\end{aligned} \\end{aligned}

(3.46)


as \| _σ_ \|−1/3\| _z_ \|∼ _e_(1/2)( _t_ − _T_)→∞. Because the latter condition is satisfied for _t_ ∈\[2 _τ_,− _N_\], the claimed estimate ( [3.38](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ246)) follows for the Laplacian term for _k_ =0 (with a good factor of \| _σ_ \|2/3 to spare). The first derivative of this term can be estimated in a similar fashion:

\\begin{aligned} \\begin{aligned} &\|\\nabla \_{\\omega \_{KE,0}}(\\Delta \_{\\omega \_{KE,0}}(\\Phi ^{\*}\_{\\sigma} \\psi \_{FS,\\sigma}-\\psi \_{FS,0}))\|\_{\\omega \_{KE,0}} \\\ &\\quad \\leqslant \|\\nabla \_{\\omega \_{KE,0}}(i\\partial \\overline {\\partial }(\\Phi ^{\*}\_{\\sigma}\\psi \_{FS, \\sigma}-\\psi \_{FS,0}))\|\_{\\omega \_{KE,0}} \\\ &\\quad \\leqslant \|\\nabla \_{\\omega \_{flat}\|\_{TY\_{0}}}(i\\partial \\overline {\\partial }(\\Phi ^{\*}\_{\\sigma} \\psi \_{FS,\\sigma}-\\psi \_{FS,0}))\|\_{\\omega \_{flat}\|\_{TY\_{0}}} \\cdot ({ \\mathrm{{tr}}}\_{\\omega \_{KE,0}}(\\omega \_{flat}\|\_{TY\_{0}}))^{\\frac{3}{2}} \\\ &\\qquad{}+ \|(i\\partial \\overline {\\partial }(\\Phi ^{\*}\_{\\sigma}\\psi \_{FS,\\sigma}-\\psi \_{FS,0}))\|\_{ \\omega \_{KE,0}} \\\ &\\qquad{}\\times {\\mathrm{{tr}}}\_{\\omega \_{flat}\|\_{TY\_{0}}}(\\omega \_{KE,0}) \\cdot \|\\nabla \_{\\omega \_{KE,0}}(\\omega \_{flat}\|\_{TY\_{0}})\|\_{\\omega \_{KE,0}} \\\ &\\quad= O(\|\\sigma \|\|z\|^{-4}(\|z\|^{2}\|t\|^{K\_{0}})^{\\frac{3}{2}}+\|\\sigma \|\|z\|^{-3} \|z\|^{-2}\|t\|^{-K\_{0}}\|z\|^{2}\|t\|^{K\_{1}}) \\end{aligned} \\end{aligned}

(3.47)


as \| _σ_ \|−1/3\| _z_ \|→∞. This is again of the desired order with a factor of \| _σ_ \|2/3 to spare. The estimate of the quadratic term and its first derivative is very similar and we omit it.

It remains to estimate the second line of ( [3.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ247)). Using ( [3.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ228)) with f = (\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{0} + \\psi \_{FS,\\sigma} and with reference metric _ω_ = _ω_ _KE_,0, and using Lemma [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65) and \[ [DFS23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR10 " 					Datar, V., Fu, X., Song, J.: Kähler-Einstein metric near an isolated log canonical singularity. J. Reine Angew. Math. 797, 79–116 (2023) 				"), Thm 1.4\] (to compare _ω_ _cusp_ to _ω_ _KE_,0),

\\begin{aligned} \\begin{aligned} &\\sum \_{k=0}^{1} \|\\nabla ^{k}\_{\\omega \_{KE,0}}(\\Phi ^{\*}\_{\\sigma} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma f-i\\partial \\overline {\\partial }\\Phi \_{\\sigma}^{\*}f)\|\_{\\omega \_{KE,0}}\\\ &\\quad \\leqslant O(e^{-( \\frac{1}{2}-\\varepsilon )(t-T)})\\sum \_{k=1}^{3} \|\\nabla ^{k}\_{\\omega \_{cusp}} \\Phi \_{\\sigma}^{\*}f\|\_{\\omega \_{cusp}}. \\end{aligned} \\end{aligned}

(3.48)


We will first show that the three derivatives of \\Phi \_{\\sigma}^{\*}f that appear on the right-hand side are _O_(1).

To this end, observe that

\\begin{aligned} \\Phi \_{\\sigma}^{\*}f = (\\psi \_{FS,0} + \\psi \_{0}) + (\\Phi \_{\\sigma}^{\*} \\psi \_{FS,\\sigma} - \\psi \_{FS,0}). \\end{aligned}

(3.49)


The first term is equal to the potential _ψ_ _KE_,0 of _ω_ _KE_,0. Using Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23) and quasi-coordinates for _ω_ _cusp_, one checks that the _ω_ _cusp_-gradient and all higher covariant derivatives of this potential are _O_(1). For the second term in ( [3.49](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ257)), we first show as in the proof of ( [3.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ239)) that

\\begin{aligned} \\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma} - \\psi \_{FS,0} = \\tilde{O}(\| \\sigma \|\|z\|^{-1})\|\_{TY\_{0}} \\end{aligned}

(3.50)


as \| _σ_ \|−1/3\| _z_ \|→∞, using the fact that _ψ_ _FS_( _z_) is real-analytic and _O_(\| _z_ \|2) as \| _z_ \|→0\. Second, as in ( [3.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ241))–( [3.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ244)), we use ( [3.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ258)) to further estimate the covariant derivatives of this function with respect to \\omega \_{flat}\|\_{TY\_{0}}. Here we also need the second covariant derivative of dz\_{i}\|\_{TY\_{0}} ( _i_ =1,2,3), but this is seen to be bounded by a constant times \| _z_ \|−2 by the same argument as after ( [3.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ244)). Thus,

\\begin{aligned} \|\\nabla ^{k}\_{\\omega \_{flat}\|\_{TY\_{0}}}(\\Phi \_{\\sigma}^{\*}\\psi \_{FS, \\sigma} - \\psi \_{FS,0})\|\_{\\omega \_{flat}\|\_{TY\_{0}}} = O(\|\\sigma \|\|z\|^{-1-k}) \\end{aligned}

(3.51)


for _k_ =1,2,3 and \| _σ_ \|−1/3\| _z_ \|→∞. Lastly, by using ( [3.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ251)) and following the pattern of ( [3.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ254))–( [3.47](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ255)) (i.e., expanding \\nabla ^{k}\_{\\omega \_{flat}\|\_{TY\_{0}}}u in _ω_ _cusp_-normal coordinates and solving for \\partial ^{k} u= \\nabla \_{\\omega \_{cusp}}^{k} u), we get

\\begin{aligned} \|\\nabla ^{k}\_{\\omega \_{cusp}}(\\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma} - \\psi \_{FS,0})\|\_{\\omega \_{cusp}} = O(\|\\sigma \|\|z\|^{-1}\|t\|^{K}) = o(1) \\end{aligned}

(3.52)


for _k_ =1,2,3 and \| _σ_ \|−1/3\| _z_ \|→∞, where _K_ >0\. To summarize, the three derivatives of \\Phi \_{\\sigma}^{\*}f on the right-hand side of ( [3.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ256)) are _O_(1), and this is sharp due to the contribution of \\nabla \_{\\omega \_{cusp}}\\psi \_{KE,0}.

To finish the proof of the lemma, we estimate the second line of ( [3.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ247)) using ( [3.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ256)). To do so, let us write the second line of ( [3.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ247)) as \\omega \_{1}^{2} - \\omega \_{2}^{2}. Then, taking norms with respect to _ω_ _KE_,0,

\\begin{aligned} \\begin{aligned} &\\left \|\\frac{\\omega \_{1}^{2}-\\omega \_{2}^{2}}{\\omega \_{KE,0}^{2}} \\right \| = \|\\omega \_{1}^{2} - \\omega \_{2}^{2}\| \\leqslant \|\\omega \_{1}- \\omega \_{2}\| \\cdot (2\|\\omega \_{2}\| + \|\\omega \_{1} - \\omega \_{2}\|). \\end{aligned} \\end{aligned}

(3.53)


We estimated \| _ω_ 1− _ω_ 2\| in ( [3.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ256)), and \| _ω_ 2\|= _O_(1) because \\omega \_{2} = \\omega \_{KE,0} + i\\partial \\overline {\\partial }(\\Phi \_{\\sigma}^{\*}\\psi \_{FS, \\sigma} - \\psi \_{FS,0}) and the _ω_ _KE_,0-norm of the second term was proved to be _o_(1) in ( [3.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ254)). The first derivative of the second line of ( [3.39](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ247)) can be bounded in a similar fashion, using also ( [3.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ256)) with _k_ =1 and ( [3.47](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ255)). □

### Lemma 3.15

Abuse notation by replacing (\\Psi \_{0}^{-1})^{\*}\\psi \_{0} \\leadsto \\psi \_{0} and (\\Psi \_{\\sigma}^{-1})^{\*}\\psi \_{FS,\\sigma} \\leadsto \\psi \_{FS,\\sigma}. Then:

(1):

For all _k_ ⩾0 and _t_ ∈\[2 _τ_, _τ_\], one has

\\begin{aligned} \\begin{aligned} &\|\\nabla ^{k}\_{\\omega \_{cusp}}(\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{cusp}-\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{T})\|\_{\\omega \_{cusp}} \\\ &=O(\|b\|\|\\tau \|^{3})+O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}). \\end{aligned} \\end{aligned}

(3.54)


(2):

For _k_ =0,1 and _t_ ∈\[2 _τ_, _τ_\], one has

\\begin{aligned} \\begin{aligned} &\|\\nabla ^{k}\_{\\omega \_{cusp}}(\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{cusp}-\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma ((\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{0}+\\psi \_{FS,\\sigma}))\|\_{\\omega \_{cusp}} \\\ &= O(e^{-\\delta \_{0}\\sqrt{-t}}). \\end{aligned} \\end{aligned}

(3.55)


(3):

For _k_ =0,1 and _t_ ∈\[ _T_ + _T_ 0, _T_ +2 _T_ 0\], one has

\\begin{aligned} \\begin{aligned} &\|\\nabla ^{k}\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C},\\sigma}}(\\Phi \_{\\sigma}^{\*} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{T}-\|b\|^{\\frac{1}{2}}\\Phi ^{\*}\_{ \\sigma}\\omega \_{TY,\\sigma})\|\_{\\omega \_{cusp}} \\\ &=O(e^{-\\delta \_{0} (t-T)^{1/2}})+ O(\|b\|^{\\frac{2-k}{4}}T\_{0}^{ \\frac{3(2-k)}{4}}). \\end{aligned} \\end{aligned}

(3.56)


### Proof

For item (1): By Lemma [2.24](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar37), one has for any _k_ ⩾0 and for _t_ ∈\[2 _τ_, _τ_\] that

\\begin{aligned} \|\\nabla \_{\\omega \_{cusp}}^{k} (\\omega \_{T} - \\omega \_{cusp})\|\_{ \\omega \_{cusp}} \\leqslant C\_{k} \|b\|\|\\tau \|^{3}. \\end{aligned}

(3.57)


Here _C_ _k_ does not depend on _b_, _τ_. Then by the triangle inequality and Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68),

\\begin{aligned} &\|\\nabla ^{k}\_{\\omega \_{cusp}}(\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{cusp}-\\Phi \_{\\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{ \\sigma}^{-1})^{\*}\\psi \_{T})\|\_{\\omega \_{cusp}}\\\ &\\quad \\leqslant C\_{k}( \|b\|\|\\tau \|^{3}+e^{-( \\frac{1}{2}-\\varepsilon )(t-T)}). \\end{aligned}

(3.58)


For item (2): By Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68), we can replace \\Phi \_{\\sigma}^{\*}i\\partial \_{\\sigma}\\overline {\\partial }\_{\\sigma}(\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{cusp} on the left-hand side of the claim by _ω_ _cusp_ up to an error of _O_( _e_ −(1/2− _ε_)( _t_ − _T_)), which is negligible because ( _t_ − _T_)/\| _t_ \|→∞ for _t_ ∈\[2 _τ_, _τ_\]. Similarly, by Lemma [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar70) and ( [3.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ251)) we can replace \\Phi \_{\\sigma}^{\*}i\\partial \_{\\sigma}\\overline {\\partial }\_{\\sigma}\\psi \_{FS,\\sigma} by _ω_ _FS_,0 (note that a closely related implication was already proved in ( [3.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ254))–( [3.47](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ255))). Next,

\\begin{aligned} \\omega \_{cusp} - \\omega \_{FS,0} = (\\omega \_{cusp}-\\omega \_{KE,0}) + i\\partial \\overline {\\partial }\\psi \_{0}, \\end{aligned}

(3.59)


and the first term here was estimated in Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23). Thus, it remains to estimate

\\begin{aligned} \|\\nabla \_{\\omega \_{cusp}}^{k} (i\\partial \\overline {\\partial }\\psi \_{0} - \\Phi \_{\\sigma}^{\*} i\\partial \_\\sigma \\overline {\\partial }\_\\sigma ((\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{0}))\|\_{\\omega \_{cusp}} \\end{aligned}

(3.60)


for _k_ =0,1. To do so, we use ( [3.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ228)) with _ω_ = _ω_ _cusp_ and f = (\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{0}. For this we require a bound on the first three _ω_ _cusp_-derivatives of \\Phi \_{\\sigma}^{\*}f = \\psi \_{0} = \\psi \_{KE,0} - \\psi \_{FS,0}. For _ψ_ _KE_,0, such a bound, which is actually _O_(1), follows from Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23) using quasi-coordinates for _ω_ _cusp_. For _ψ_ _FS_,0, we need to go through the same steps as after ( [3.58](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ266)): for _k_ =1,2,3 and \| _z_ \|→0 we clearly have that

\\begin{aligned} \|\\nabla \_{\\omega \_{flat}\|\_{TY\_{0}}}^{k} \\psi \_{FS,0}\|\_{\\omega \_{flat}\|\_{TY\_{0}}} = O(\|z\|^{2-k}), \\end{aligned}

(3.61)


and hence, by ( [3.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ251)) and by computations in _ω_ _cusp_-normal coordinates, for some _K_ >0,

\\begin{aligned} \|\\nabla ^{k}\_{\\omega \_{cusp}}\\psi \_{FS,0}\|\_{\\omega \_{cusp}} = O(\|z\|^{2} \|t\|^{K}) = o(1). \\end{aligned}

(3.62)


In sum, all errors are negligible compared to the one from _ω_ _cusp_− _ω_ _KE_,0, which is O(e^{-\\delta \_{0}\\sqrt{-t}}).

For item (3): Using ( [2.76](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ79)), ( [2.197](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ200)) and Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68), one has for _k_ =0,1,

\\begin{aligned} \\begin{aligned} &\\left \|\\nabla ^{k}\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C},\\sigma}}(\\Phi \_{ \\sigma}^{\*}i\\partial \_\\sigma \\overline {\\partial }\_\\sigma (\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{T}-\|b\|^{ \\frac{1}{2}}\\Phi ^{\*}\_{\\sigma}\\omega \_{TY\_{\\sigma}})\\right \|\_{\|b\|^{ \\frac{1}{2}}\\omega \_{\\mathcal {C},\\sigma}} \\\ &=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})+ O(\|b\|^{\\frac{2-k}{4}}T\_{0}^{ \\frac{3(2-k)}{4}})+O(e^{-\\delta \_{0} (t-T)^{1/2}}). \\end{aligned} \\end{aligned}

(3.63)


When applying ( [2.76](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ79)), we absorb the factor \| _b_ \|(2− _k_)/4 into e^{-\\delta \_{0}(t-T)^{1/2}} by slightly changing _δ_ 0. □

### Lemma 3.16

Abuse notation by replacing (\\Psi \_{\\sigma}^{-1})^{\*}\\Omega \_{\\sigma }\\leadsto \\Omega \_{\\sigma}. Then for some _K_ >0 and for all _ε_ >0, for _T_ + _T_ 0⩽ _t_ ⩽− _N_, for _j_ =0,1 and for _ω_ equal to either _ω_ _cusp_ or _ω_ _T_, it holds on _TY_ 0 that

\\left \|\\nabla ^{j}\_{\\omega}\\log \\frac{\\Phi \_{\\sigma}^{\*}\\Omega \_{\\sigma}\\wedge \\Phi \_{\\sigma}^{\*}\\overline{\\Omega}\_{\\sigma}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\right \|\_{\\omega}=O(\|\\sigma \|\|z\|^{-3}\|t\|^{K})=O(e^{-(\\frac{3}{2}- \\varepsilon )(t-T)}).

(3.64)


### Proof

In the following, _z_ 1, _z_ 2, _z_ 3 and _dz_ 1, _dz_ 2, _dz_ 3 are automatically understood to be restricted from \\mathbb{C}^{3} to _TY_ _σ_ or _TY_ 0. Similarly, \\tilde{O}(\\ldots ) as in ( [3.25](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ233)) denotes a function on a neighborhood of the origin in \\mathbb{C}^{3}, and we will restrict this function to _TY_ _σ_ or _TY_ 0 without writing the restriction symbol.

By the proof of Lemma [2.19](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar30) we have for all _σ_ (including _σ_ =0) that

\\Omega \_{\\sigma}=(1+f(z))\\Omega \_{TY\_{\\sigma}},

(3.65)


where _f_( _z_) is holomorphic on some neighborhood of the origin in \\mathbb{C}^{3} with _f_(0)=0. We may assume without loss of generality that \| _z_ 3\|⩾max{\| _z_ 1\|,\| _z_ 2\|} at the point of _TY_ 0 at which we are working. Then _z_ 3≠0 because _t_ >−∞. Also, \\Phi \_{\\sigma}(z)\_{3} = z\_{3} + \\nu \_{\\sigma}(z)\\overline{z}\_{3}^{2} \\neq 0 because otherwise \| _z_ 3\|= _O_(\| _σ_ \|\| _z_ \|−4)\| _z_ 3\|2, so 1= _O_(\| _σ_ \|\| _z_ \|−4)\| _z_ 3\|= _O_(\| _σ_ \|\| _z_ \|−3)= _o_(1) because _t_ − _T_ →∞, and this is a contradiction. This means that we can use the same Poincaré residue to represent \\Omega \_{TY\_{0}}\|\_{z} and \\Omega \_{TY\_{\\sigma}}\|\_{\\Phi \_{\\sigma}(z)}, i.e.,

\\begin{aligned} \\Omega \_{TY\_{0}}\|\_{z} = \\frac{dz\_{1} \\wedge dz\_{2}}{z\_{3}^{2}},\\;\\, \\Omega \_{TY\_{\\sigma}}\|\_{\\Phi \_{\\sigma}(z)} = \\frac{dz\_{1} \\wedge dz\_{2}}{\\Phi \_{\\sigma}(z)\_{3}^{2}}. \\end{aligned}

(3.66)


Then from ( [3.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ234)) and ( [3.29](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ237)) we have that

\\begin{aligned} \\begin{aligned} \\Phi \_{\\sigma}^{\*}(z\_{i})&=z\_{i}+\\tilde{O}(\|\\sigma \|\|z\|^{-2}), \\\ \\Phi \_{\\sigma}^{\*}(dz\_{1})\\wedge \\Phi \_{\\sigma}^{\*}(dz\_{2})&=dz\_{1} \\wedge dz\_{2}+\\sum \\nolimits \_{\|I\|+\|J\|=2} \\tilde{O}(\|\\sigma \|\|z\|^{-3}) \\, dz\_{I}\\wedge d\\overline{z}\_{J}, \\end{aligned} \\end{aligned}

(3.67)


where _I_, _J_ are multi-indices with values in {1,2,3}. Combining ( [3.65](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ273)), ( [3.66](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ274)) and ( [3.67](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ275)) with

\\begin{aligned} dz\_{3}=-\\frac{z\_{1}^{2}}{z\_{3}^{2}}dz\_{1}-\\frac{z\_{2}^{2}}{z\_{3}^{2}}dz\_{2}, \\end{aligned}

(3.68)


which holds identically on _TY_ 0∩{ _z_ 3≠0}, we obtain that

\\begin{aligned} \\begin{aligned} &\\frac{\\Phi \_{\\sigma}^{\*}\\Omega \_{\\sigma}\\wedge \\Phi \_{\\sigma}^{\*}\\overline{\\Omega}\_{\\sigma}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\\ &\\quad=\\left \|\\frac{1+f(\\Phi \_{\\sigma}(z))}{1+f(z)} \\right \|^{2} \\cdot \\frac{\\Phi \_{\\sigma}^{\*}(dz\_{1}) \\wedge \\Phi \_{\\sigma}^{\*}(dz\_{2}) \\wedge \\Phi \_{\\sigma}^{\*}(d\\overline{z}\_{1}) \\wedge \\Phi \_{\\sigma}^{\*}(d\\overline{z}\_{2})}{dz\_{1} \\wedge dz\_{2} \\wedge d\\overline{z}\_{1} \\wedge d\\overline{z}\_{2}} \\cdot \\left \|\\frac{z\_{3}}{\\Phi \_{\\sigma}^{\*}(z\_{3})}\\right \|^{4} \\\ &\\quad= \\left \|\\frac{1+f(\\Phi \_{\\sigma}(z))}{1+f(z)} \\right \|^{2} \\cdot \\left (1 + {\\mathrm{Re}}\\left (\\tilde{O}(\|\\sigma \|\|z\|^{-3}) \\hspace{-0.5mm} \\left \[\\frac{z\_{1}}{z\_{3}},\\frac{z\_{2}}{z\_{3}}\\right \]\\right )\\right ) \\\ &\\qquad{}\\times \\left \|1 + z\_{3}^{-1} \\tilde{O}(\|\\sigma \| \|z\|^{-2}) \\right \|^{-4}. \\end{aligned} \\end{aligned}

(3.69)


The square bracket notation stands for a polynomial in _z_ 1/ _z_ 3, _z_ 2/ _z_ 3 with \\tilde{O}(\|\\sigma \|\|z\|^{-3}) coefficients.

We can analyze \|\\nabla ^{j}\_{\\omega }\\log \\text{(3.69)} \|\_{\\omega} using the same technique as in the proofs of Lemmas [3.11](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar70) and [3.13](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar74): First, view _z_ 1, _z_ 2 as local coordinates on _TY_ 0∩{ _z_ 3≠0}, represent \\omega \_{flat}\|\_{TY\_{0}} by a matrix and estimate the \\omega \_{flat}\|\_{TY\_{0}}-covariant derivatives of log( [3.69](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ277)) in terms of its partial derivatives with respect to _z_ 1, _z_ 2. Here, the properties -z\_{3}^{3} = z\_{1}^{3} + z\_{2}^{3} and \| _z_ 3\|⩾max{\| _z_ 1\|,\| _z_ 2\|} need to be used to eliminate or estimate terms that explicitly depend on _z_ 3. The upshot is that for _j_ =0,1 and \| _σ_ \|−1/3\| _z_ \|→∞,

\\begin{aligned} \\left \|\\nabla ^{j}\_{\\omega \_{flat}\|\_{TY\_{0}}} \\log \\frac{\\Phi \_{\\sigma}^{\*}\\Omega \_{\\sigma}\\wedge \\Phi \_{\\sigma}^{\*}\\overline{\\Omega}\_{\\sigma}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\right \|\_{\\omega \_{flat}\|\_{TY\_{0}}} = O(\|\\sigma \|\|z\|^{-3-j}). \\end{aligned}

(3.70)


Secondly, we can rewrite ( [3.70](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ278)) in terms of _ω_ _cusp_ instead of \\omega \_{flat}\|\_{TY\_{0}} by using ( [3.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ251)). This implies the statement of the lemma for _ω_ = _ω_ _cusp_. For _ω_ = _ω_ _T_ we use a reduction as in the proof of Lemma [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65). Fix a small _δ_ >0\. If _t_/ _T_ ⩽1− _δ_, then _ω_ _T_ and _ω_ _cusp_ are uniformly comparable by Proposition [2.26](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar40). Thus, the version of the lemma for _ω_ _T_ follows from the one for _ω_ _cusp_ in this case. If _t_/ _T_ ⩾1− _δ_, then _ω_ _T_ is comparable to \|b\|^{1/2}\\omega \_{\\mathcal {C},\\sigma} by ( [2.164](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ167))–( [2.165](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ168)). Redoing the proof of ( [3.43](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ251)) for \\omega \_{\\mathcal {C},\\sigma} instead of _ω_ _cusp_ as the reference metric, it is clear that \|\\omega \_{flat}\|\_{TY\_{0}}\|\_{\\omega \_{\\mathcal {C},\\sigma}} = O(\|z\|^{2} \|b\|^{-L} (t - T)^{L}) for some _L_ >0 if \| _z_ \|→0 with _t_ − _T_ ⩾1\. Thus, the statement of the lemma again follows from ( [3.70](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ278)). □

We now finally come to the proof of our main result, Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62).

### Proof of Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar62)

Firstly, let us recall from ( [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ216)) the expression of the Ricci potential:

f\_{\\sigma}\|\_{\\mathcal{Y}\_{\\sigma}} = \\log \\left ( \\frac{\\omega \_{glue,\\sigma}^{2}}{\\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma}} \\right )-\\psi \_{glue,\\sigma}.

(3.71)


We will do the proof case by case by analyzing this formula.

_Region_\\mathfrak{R}\_{1} _:_ In this region, we have that _t_ >− _N_. It follows from the smoothness of Ω_σ_ and _ψ_ _FS_, _σ_ with respect to _σ_ and from the Kähler-Einstein equation

\\log \\frac{\\omega \_{KE,0}^{2}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}= \\psi \_{KE,0}

(3.72)


that \|\\nabla ^{k}\_{\\omega \_{glue,\\sigma}}f\_{\\sigma}\|\_{\\omega \_{glue, \\sigma}}=O(\|\\sigma \|) for _k_ =0,1.

_Region_\\mathfrak{R}\_{2} _:_ For region \\mathfrak{R}\_{2}, as in Lemma [3.13](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar74), we omit the pull-back map \\Psi \_{\\sigma}^{-1} for simplicity. In this region, _τ_ < _t_ <− _N_. Using ( [3.72](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ280)), we have that

\\begin{aligned} \\begin{aligned} \\Phi ^{\*}\_{\\sigma }f\_{\\sigma}&= \\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\Phi ^{\*}\_{\\sigma}\\Omega \_{\\sigma}\\wedge \\Phi ^{\*}\_{\\sigma}\\overline{\\Omega}\_{\\sigma}}+ \\log \\frac{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}{\\omega ^{2}\_{KE,0}}- \\psi \_{0}-\\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma}+\\psi \_{KE,0} \\\ &=\\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\omega \_{KE,0}^{2}}+ \\log \\frac{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}{\\Phi ^{\*}\_{\\sigma}\\Omega \_{\\sigma}\\wedge \\Phi ^{\*}\_{\\sigma}\\overline{\\Omega}\_{\\sigma}}- \\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma}+\\psi \_{FS,0}. \\end{aligned} \\end{aligned}

(3.73)


We estimate the three terms separately. By Lemma [3.13](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar74), for _k_ =0,1, we have that

\\begin{aligned} \\left \|\\nabla ^{k}\_{\\omega \_{KE,0}}\\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\omega \_{KE,0}^{2}} \\right \|\_{\\omega \_{KE,0}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}). \\end{aligned}

(3.74)


By Lemma [3.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar80), for _k_ =0,1, the second term can be estimated as

\\left \|\\nabla ^{k}\_{\\omega \_{KE,0}}\\log \\frac{\\Phi \_{\\sigma}^{\*}\\Omega \_{\\sigma}\\wedge \\Phi \_{\\sigma}^{\*}\\overline{\\Omega}\_{\\sigma}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\right \|\_{\\omega \_{KE,0}}=O(e^{-(\\frac{3}{2}-\\varepsilon )(t-T)}).

(3.75)


For the third term, for _k_ =0,1, by ( [3.58](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ266)) and Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23),

\|\\nabla ^{k}\_{\\omega \_{KE,0}}(\\Phi \_{\\sigma}^{\*}\\psi \_{FS,\\sigma}- \\psi \_{FS,0})\|\_{\\omega \_{KE,0}} =O(\|\\sigma \|\|z\|^{-1}\|t\|^{K}) = O(\|z\|^{2} e^{-(\\frac{3}{2}-\\varepsilon )(t-T)}).

(3.76)


Dropping the smaller terms, we get

\\begin{aligned} \|\\nabla \_{\\omega \_{KE,0}}^{k}\\Phi \_{\\sigma}^{\*} f\_{\\sigma}\|\_{\\omega \_{KE,0}}=O(e^{-( \\frac{1}{2}-\\varepsilon )(t-T)}) \\;\\,(k=0,1). \\end{aligned}

(3.77)


Using the metric equivalence of \\Phi ^{\*}\_{\\sigma }g\_{glue,\\sigma} and _g_ _KE_,0 in this region, which follows from Lemmas [3.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar65) and [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68) (using also ( [3.52](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ260)) to compare the term _ψ_ _FS_, _σ_ in _ψ_ _glue_, _σ_ to _ψ_ _FS_,0), we conclude that

\\begin{aligned} \|\\nabla ^{k}\_{\\omega \_{glue,\\sigma}} f\_{\\sigma}\|\_{\\omega \_{glue, \\sigma}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})\\;\\,(k=0,1). \\end{aligned}

(3.78)


_Region_\\mathfrak{R}\_{4} _:_ In this case \\psi \_{glue,\\sigma}=(\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{T} and \\omega \_{glue,\\sigma}=i\\partial \_{\\sigma}\\overline {\\partial }\_{\\sigma}(\\Phi \_{\\sigma}^{-1})^{\*}\\psi \_{T}. So we have

f\_{\\sigma}=\\log \\frac{(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma}}-( \\Phi ^{-1}\_{\\sigma})^{\*}\\psi \_{T}.

(3.79)


Hence

\\begin{aligned} \\begin{aligned} \\Phi ^{\*}\_{\\sigma }f\_{\\sigma}={}& \\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\Phi ^{\*}\_{\\sigma}\\Omega \_{\\sigma}\\wedge \\Phi ^{\*}\_{\\sigma}\\overline{\\Omega}\_{\\sigma}}- \\psi \_{T} \\\ ={}&\\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\omega \_{T}^{2}}+ \\log \\frac{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}{\\Phi ^{\*}\_{\\sigma}\\Omega \_{\\sigma}\\wedge \\Phi ^{\*}\_{\\sigma}\\overline{\\Omega}\_{\\sigma}}+ \\log \\frac{\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}\\\ &{}+ \\log \\frac{\\omega ^{2}\_{T}}{\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}}- \\psi \_{T}. \\end{aligned} \\end{aligned}

(3.80)


By equation ( [2.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ49)), the last two terms combine to zero.

Now we estimate the first three terms one by one. Using Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68), for _j_ =0,1 one has

\\left \|\\nabla ^{j}\_{\\omega \_{T}}\\left (\\log \\frac{\\Phi ^{\*}\_{\\sigma}(i\\partial \_\\sigma \\overline {\\partial }\_\\sigma \\psi \_{glue,\\sigma})^{2}}{\\omega \_{T}^{2}} \\right )\\right \|\_{\\omega \_{T}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)}).

(3.81)


By Lemma [3.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar80), for _j_ =0,1, we estimate the second term by

\\left \|\\nabla ^{j}\_{\\omega \_{T}}\\left (\\log \\frac{\\Phi \_{\\sigma}^{\*}\\Omega \_{\\sigma}\\wedge \\Phi \_{\\sigma}^{\*}\\overline{\\Omega}\_{\\sigma}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\right )\\right \|\_{\\omega \_{T}}=O(e^{-(\\frac{3}{2}-\\varepsilon )(t-T)}).

(3.82)


By ( [2.49](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ52)) and ( [2.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ53)) with _C_ =1, for _j_ =0,1 we estimate the third term by

\\left \|\\nabla ^{j}\_{\\omega \_{T}}\\left (\\log \\frac{\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}} \\right )\\right \|\_{\\omega \_{T}}=O(e^{\\frac{(1-\\varepsilon )t}{2}}).

(3.83)


Dropping the smaller term, one has

\|\\nabla \_{\\omega \_{T}}^{j}\\Phi ^{\*}\_{\\sigma }f\_{\\sigma}\|\_{\\omega \_{T}}=O(e^{-( \\frac{1}{2}-\\varepsilon )(t-T)})+O(e^{(\\frac{1}{2}-\\varepsilon )t})\\;\\,(j = 0,1).

(3.84)


Using the metric equivalence of \\Phi ^{\*}\_{\\sigma }g\_{glue,\\sigma} and _g_ _T_ in this region, we conclude that

\\begin{aligned} \|\\nabla \_{\\omega \_{glue,\\sigma}}^{j} f\_{\\sigma}\|\_{\\omega \_{glue, \\sigma}}=O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})+O(e^{(\\frac{1}{2}- \\varepsilon )t})\\;\\,(j = 0,1). \\end{aligned}

(3.85)


_Regions_\\mathfrak{R}\_{6}, \\mathfrak{R}\_{7} _:_ For regions \\mathfrak{R}\_{6},\\mathfrak{R}\_{7} we estimate _f_ _σ_ directly on _TY_ _σ_. In these two cases, one has

f\_{\\sigma}=\\log \\frac{(\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}i\\partial \\overline {\\partial }\\psi \_{TY\_{1}})^{2}}{\\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma}}- \\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}i\\partial \\overline {\\partial }\\psi \_{TY\_{1}}- \\psi \_{T}(T).

(3.86)


It follows from

{(m\_{\\sigma}^{\*}i\\partial \\overline {\\partial }\\psi \_{TY\_{1}})^{2}}={m\_{\\sigma}^{\*}\\Omega \_{TY\_{1}} \\wedge m\_{\\sigma}^{\*}\\overline{\\Omega}\_{TY\_{1}}}

(3.87)


that

\\log \\frac{(\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}i\\partial \\overline {\\partial }\\psi \_{TY\_{1}})^{2}}{\\Omega \_{\\sigma}\\wedge \\overline{\\Omega}\_{\\sigma}}- \\psi \_{T}(T)=\\log \\Big(\\mathfrak{c}^{2}\|b\|\|F\_{\\sigma}\|^{2}e^{-\\psi \_{T}(T)} \\Big),

(3.88)


where

\\begin{aligned} F\_{\\sigma}:=\\frac{m\_{\\sigma}^{\*}\\Omega \_{TY\_{1}}}{\\Omega \_{\\sigma}}. \\end{aligned}

(3.89)


Now we claim that

\\mathfrak{c}^{2}\|b\|=e^{\\psi \_{T}(T)}.

(3.90)


This can easily be checked as follows: Using the fact that \\mathfrak{c} = \\sqrt{2} in dimension _n_ =2 and that

e^{\\psi \_{T}(T)+a}+b=0,

(3.91)


we see that ( [3.90](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ298)) is equivalent to _a_ =−log2, which follows from the equation

e^{-\\psi \_{cusp}}\\omega \_{cusp}^{2} =\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}} = \\omega \_{\\mathcal {C}}^{2}

(3.92)


and from the explicit form of \\psi \_{cusp}, \\psi \_{\\mathcal {C}} in ( [2.45](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ48)), ( [2.177](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ180)) respectively.

Hence

\\log \\Big(\\mathfrak{c}^{2}\|b\|\|F\_{\\sigma}\|^{2}e^{-\\psi \_{T}(T)}\\Big)= \\log \|F\_{\\sigma}\|^{2}.

(3.93)


On _TY_ 1, if \| _z_ \|≫1, then \| _z_ \|2 is uniformly comparable to _h_ = _e_ _t_. Recall that _m_ _σ_( _z_)= _σ_ −1/3 _z_. So on _TY_ _σ_, points in regions \\mathfrak{R}\_{6} and \\mathfrak{R}\_{7} satisfy, for some constant _C_ independent of _σ_,

\\begin{aligned} \|z\|^{2} \\leqslant C \|\\sigma \|^{\\frac{2}{3}}e^{T\_{0}} = Ce^{T + T\_{0}}. \\end{aligned}

(3.94)


Using Lemma [2.19](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar30), one has

\\log \|F\_{\\sigma}\|=\\log \\left \| \\frac{m\_{\\sigma}^{\*}\\Omega \_{TY\_{1}}}{\\Omega \_{\\sigma}}\\right \|= \\tilde{O}(\|z\|)= O(e^{\\frac{T+T\_{0}}{2}}).

(3.95)


Noticing that \\mathfrak{c}\|b\|^{1/2}m\_{\\sigma}^{\*}i\\partial \\overline {\\partial }\\psi \_{TY\_{1}} is Ricci-flat, we can deduce from the Cheng-Yau gradient estimate for harmonic functions \[ [CY75](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR7 " 					Cheng, S.-Y., Yau, S.-T.: Differential equations on Riemannian manifolds and their geometric applications. Comm. Pure Appl. Math. 28, 333–354 (1975) 				"), p.350, Thm 6\] and from ( [3.95](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ303)) that

\\left \|\\nabla \_{\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}\\omega \_{TY\_{1}}} (\\log \|F\_{\\sigma}\|^{2})\\right \|\_{\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{ \\sigma}^{\*}\\omega \_{TY\_{1}}}=O(\|b\|^{-\\frac{1}{4}}e^{\\frac{T+T\_{0}}{2}}).

(3.96)


Using that \| _b_ \| is comparable to \| _T_ \|−3, we have

\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}\\psi \_{TY\_{1}}=O((T\_{0}/\|T\|)^{ \\frac{3}{2}}).

(3.97)


Also, for log _h_ ⩽ _T_ 0,

\\left \|\\nabla \_{\\omega \_{TY\_{1}}}\\psi \_{TY\_{1}}\\right \|\_{\\omega \_{TY\_{1}}}=O(T\_{0}^{ \\frac{3}{4}}),

(3.98)


and hence

\\left \|\\nabla \_{\\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}\\psi \_{TY\_{1}}} \\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}\\psi \_{TY\_{1}}\\right \|\_{ \\mathfrak{c}\|b\|^{\\frac{1}{2}}m\_{\\sigma}^{\*}\\psi \_{TY\_{1}}}=O(\|b\|^{ \\frac{1}{4}}T\_{0}^{\\frac{3}{4}}).

(3.99)


Thus, combining the _C_ 0 norm and the _C_ 1 seminorm (weighted by **r** _σ_) and dropping the smaller terms ( [3.95](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ303))–( [3.96](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ304)), we finish the proof of the case of regions \\mathfrak{R}\_{6} and \\mathfrak{R}\_{7}.

_Region_\\mathfrak{R}\_{3} _:_ In this region, we glue the two Kähler-Einstein metrics _ω_ _KE_,0 and _ω_ _T_. Set _ψ_ 1, _ψ_ 2 to be the expression of \\Phi \_{\\sigma}^{\*} \\psi \_{glue, \\sigma} in regions \\mathfrak{R}\_{2},\\mathfrak{R}\_{4} respectively. By ( [3.73](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ281)) and ( [3.75](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ283)),

\\begin{aligned} \\begin{aligned} \\Phi \_{\\sigma}^{\*} f\_{\\sigma }={}& \\log \\frac{\\Phi \_{\\sigma}^{\*} (i\\partial \_{\\sigma}\\overline{\\partial}\_{\\sigma }( (\\Phi \_{\\sigma}^{-1})^{\*}(\\psi \_{2} + \\chi \_{2} (\\psi \_{1}-\\psi \_{2}) )))^{2}}{\\omega \_{KE, 0}^{2}} \\\ &{}- (\\psi \_{2} + \\chi \_{2} (\\psi \_{1}-\\psi \_{2}))+O(e^{-(\\frac{3}{2}- \\varepsilon )(t-T)}). \\end{aligned} \\end{aligned}

(3.100)


If the error term _χ_ 2( _ψ_ 1− _ψ_ 2) vanishes, this is exactly the case of region \\mathfrak{R}\_{4}, see ( [3.85](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ293)). In general, we first apply ( [3.20](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ228)) to change \\Phi \_{\\sigma}^{\*}i\\partial \_{\\sigma}\\overline {\\partial }\_{\\sigma}f to i\\partial \\overline{\\partial}\\Phi \_{\\sigma}^{\*}f for f=(\\Phi \_{\\sigma}^{-1})^{\*}(\\psi \_{2} + \\chi \_{2} (\\psi \_{1}-\\psi \_{2}) ). Then we only need to estimate the following additional terms:

\\begin{aligned} \\frac{2i\\partial \\overline{\\partial} \\psi \_{2} \\wedge i\\partial \\overline{\\partial} (\\chi \_{2} (\\psi \_{1}-\\psi \_{2}) ) + (i\\partial \\overline{\\partial}(\\chi \_{2} (\\psi \_{1}-\\psi \_{2})))^{2}}{\\omega \_{KE, 0}^{2}} -\\chi \_{2}(\\psi \_{1}-\\psi \_{2}). \\end{aligned}

(3.101)


As _t_ ∈\[2 _τ_, _τ_\], we have, for all _j_ ⩾0,

\\begin{aligned} \|\\chi \_{2}^{(j)}(t)\| \\leqslant C\_{j}\|\\tau \|^{-j}. \\end{aligned}

(3.102)


Applying the quasi-coordinates ( [2.109](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ112)), we obtain that

\\begin{aligned} \|\\nabla ^{j}\_{\\omega \_{KE,0}}\\chi \_{2}\| \\leqslant C\_{j}. \\end{aligned}

(3.103)


Combining ( [3.103](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ311)) with the estimate of _ψ_ 1− _ψ_ 2 from Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23) and ( [2.111](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ114)), we deduce that

\\begin{aligned} \|\\nabla ^{j}\_{\\omega \_{KE,0}} (\\chi \_{2} (\\psi \_{1}-\\psi \_{2}))\|\\leqslant C\_{j}(\|b\|\| \\tau \|^{3} + e^{-\\delta \_{0}\\sqrt{-t}})\\;\\, (j = 0,1). \\end{aligned}

(3.104)


Thus, since _g_ _KE_,0 and \\Phi \_{\\sigma}^{\*}g\_{glue, \\sigma} are uniformly equivalent for _t_ ∈\[2 _τ_, _τ_\],

\\begin{aligned} \|\\nabla ^{j}\_{\\Phi \_{\\sigma}^{\*}g\_{glue,\\sigma}} (\\chi \_{2} (\\psi \_{1}- \\psi \_{2}))\|\\leqslant C\_{j}(\|b\|\|\\tau \|^{3} + e^{-\\delta \_{0}\\sqrt{-t}}) \\; \\, (j = 0,1). \\end{aligned}

(3.105)


This provides the required estimate of the cutoff errors ( [3.101](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ309)).

_Region_\\mathfrak{R}\_{5}: The situation is similar to \\mathfrak{R}\_{3}. Here we glue \\mathfrak{c}\|b\|^{1/2}m\_{\\sigma}^{\*}\\omega \_{TY\_{1}} and _ω_ _T_. From the estimate ( [3.97](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ305)) in region \\mathfrak{R}\_{6} and elementary inequalities, we deduce that

\\begin{aligned} \|f\_{\\sigma}\|+\\mathbf{r}\_{\\sigma}\|\\nabla \_{\\omega \_{glue,\\sigma}}f\_{ \\sigma}\|\_{\\omega \_{glue,\\sigma}} \\leqslant {}& C(T\_{0}/\|T\|)^{\\frac{3}{2}} + \| i\\partial \\overline {\\partial }(\\chi \_{1}E)\|\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C}}}\\\ &{}+\\mathbf{r}\_{ \\sigma}\\left \|\\nabla \_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C}}}i\\partial \\overline {\\partial }(\\chi \_{1}E) \\right \|\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C}}}, \\end{aligned}

(3.106)


where E(t):= \\psi \_{T}(t) - \\psi \_{T}(T) - \\mathfrak{c} \|b\|^{\\frac{1}{2}} \\psi \_{\\mathcal{C}}(t) is the difference of Kähler potentials defined in ( [2.179](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ182)). We estimate _χ_ 1 _E_ as follows, using the same idea as in Proposition [2.34](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar54). Firstly, for _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\],

\\begin{aligned} \|\\chi \_{1}^{(j)}(t)\| \\leqslant C\_{j} T\_{0}^{-j}\\;\\,(j \\geqslant 0). \\end{aligned}

(3.107)


Using the estimate of _E_ from ( [2.198](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ201)), we further deduce that there exists a _C_ such that, for _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\] and _j_ =0,1,2,3,

\\begin{aligned} \|((t-T)\\partial \_{t})^{j} (\\chi \_{1}E)\|\\leqslant C \|b\|T\_{0}^{3}. \\end{aligned}

(3.108)


Using quasi-coordinates, we have, for _t_ − _T_ ∈\[ _T_ 0,2 _T_ 0\] and _j_ =0,1,

\\left \| \\nabla ^{j}\_{\|b\|^{\\frac{1}{2}}\\omega \_{\\mathcal {C}}} (i\\partial \\overline{\\partial} (\\chi \_{1} E))\\right \|\_{\|b\|^{\\frac{1}{2}}\\omega \_{ \\mathcal {C}}} \\leqslant C\|b\|^{\\frac{1}{4}(2-j)}T\_{0}^{\\frac{3}{4}(2-j)}.

(3.109)


The claimed estimate in region \\mathfrak{R}\_{5} now follows from ( [3.106](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ314)) and ( [3.109](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ317)).

This completes the proof of Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62). □

### 3.3 Definition of the weight functions and weighted Hölder norms

We have set up the pre-glued manifold (\\mathcal{X}\_{\\sigma}, \\omega \_{glue,\\sigma}) and the relevant Monge-Ampère equation in ( [3.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ212))–( [3.6](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ214)) and estimated its right-hand side, i.e., the Ricci potential _f_ _σ_ of _ω_ _glue_, _σ_, in Theorem [3.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar62). In Remark [3.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar64) we discussed what can be said about the solution _u_ _σ_ using off-the-shelf arguments. This was insufficient (only) on the Tian-Yau region, motivating the development of a weighted Hölder space theory.

### Definition 3.17

Fix a parameter _δ_ >0\. In the rest of the paper _δ_ will always be chosen arbitrarily close to zero. With this in mind we define two weight functions {w}\_{\\sigma}, \\tilde{w}\_{\\sigma}: \\mathcal{X}\_{\\sigma }\\to \\mathbb{R}^{+} as follows:

\\begin{aligned} w\_{\\sigma }&:= \\textstyle\\begin{cases} \|T\|^{-\\delta} &\\text{on}\\;\\,\\Psi \_{\\sigma}^{-1}(\\Phi \_{\\sigma}(\\{t > -N \\})) \\cup (\\mathcal{X}\_{\\sigma }\\setminus {\\mathrm{dom}}\\,\\Psi \_{\\sigma}), \\\ \\Psi \_{\\sigma}^{\*}(\\Phi \_{\\sigma}^{-1})^{\*}\\left ((t-T)^{-\\delta} \\right )&\\text{on}\\;\\,\\Psi \_{\\sigma}^{-1}(\\Phi \_{\\sigma}(\\{t < -N\\})), \\\ 1 &\\text{on}\\;\\,\\mathfrak{R}\_{7}, \\end{cases}\\displaystyle \\end{aligned}

(3.110)


\\begin{aligned} \\tilde{w}\_{\\sigma }&:= \\mathbf{r}\_{\\sigma}^{-2} w\_{\\sigma}. \\end{aligned}

(3.111)


### Definition 3.18

With the weight _w_ _σ_ from ( [3.110](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ318)) and the regularity scale **r** _σ_ from ( [3.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ217)) we define for all 0⩽ _k_ ⩽4 and for all locally _C_ _k_ functions _ϕ_ on \\mathcal{X}\_{\\sigma}:

\\begin{aligned} \\\|\\phi \\\|\_{C^{k}\_{w}} : =\\sum \_{j=0}^{k} \\left \\\|w\_{\\sigma}^{-1} \\mathbf{r}\_{\\sigma}^{j}\\left \|\\nabla ^{j}\_{\\omega \_{glue,\\sigma}} \\phi \\right \|\_{\\omega \_{glue,\\sigma}}\\right \\\|\_{L^{\\infty}( \\mathcal{X}\_{\\sigma})}. \\end{aligned}

(3.112)


Moreover, for all 0⩽ _k_ ⩽3 and \\bar{\\alpha}\\in (0,1) and for all locally C^{k,\\bar{\\alpha}} functions _ϕ_ on \\mathcal{X}\_{\\sigma},

\\begin{aligned} \\begin{aligned}{} \[\\phi \]\_{C^{k,\\bar{\\alpha}}\_{w}}:={}&\\sup \\biggl\\{ \\frac{\\mathbf{r}\_{\\sigma}(p)^{k+\\bar{\\alpha}}}{w\_{\\sigma}(p)} \\frac{\|(\\nabla ^{k}\_{\\omega \_{glue,\\sigma}}\\phi )(p)-(\\nabla ^{k}\_{\\omega \_{glue,\\sigma}}\\phi )(q)\|\_{\\omega \_{glue,\\sigma}}}{d\_{\\omega \_{glue,\\sigma}}(p,q)^{\\bar{\\alpha}}}:\\\ &0 < d\_{\\omega \_{glue,\\sigma}}(p,q) < \\mathbf{r}\_{\\sigma}(p) \\biggr\\} . \\end{aligned} \\end{aligned}

(3.113)


Here the numerator of the difference quotient is to be understood using the trivialization of the tangent bundle in quasi-coordinates. Given this, we define

\\begin{aligned} \\\|\\phi \\\|\_{C^{k,\\bar{\\alpha}}\_{{w}}}:=\\\|\\phi \\\|\_{C^{k}\_{w}}+\[\\phi \]\_{C^{k, \\bar{\\alpha}}\_{w}}. \\end{aligned}

(3.114)


Replacing _w_ _σ_ by \\tilde{w}\_{\\sigma}, we may similarly define a weighted C^{k}\_{\\tilde{w}} and C^{k,\\bar{\\alpha}}\_{\\tilde{w}} norm. For us, \\bar{\\alpha} will always be an arbitrary number in (0,1) whose choice affects neither the arguments nor the results.

Table [2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Tab2) summarizes the behavior of the scale and weight functions and of the Ricci potential in a simplified manner (ignoring constant factors and allowing slightly suboptimal exponents). The only remaining geometric parameters are \| _T_ \|∼\|log\| _σ_ \|\| and \| _τ_ \|∼(log\| _T_ \|)2. This information is sufficient to understand almost all of the numerology in Sects. [4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec17)– [5](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec38).

**Table 2 Regularity scale r_σ_, weights w\_{\\sigma}, \\tilde{w}\_{\\sigma}, Ricci potential _f_ _σ_.**

[Full size table](https://link.springer.com/article/10.1007/s00039-025-00708-y/tables/2)

It is clear from standard Schauder theory on a ball of radius **r** _σ_ in \\mathbb{C}^{2} that for every \\bar{\\alpha}\\in (0,1) there exists a constant C(\\bar{\\alpha}) independent of _σ_ such that the linearization

\\begin{aligned} L\_{\\sigma }:= \\Delta \_{\\omega \_{glue,\\sigma}} - {\\mathrm{Id}} \\end{aligned}

(3.115)


of the complex Monge-Ampère operator satisfies the estimate

\\begin{aligned} \\\|\\phi \\\|\_{C^{2,\\bar{\\alpha}}\_{w}} \\leqslant C(\\bar{\\alpha})(\\\|L\_{\\sigma} \\phi \\\|\_{C^{0,\\bar{\\alpha}}\_{\\tilde{w}}} + \\\|\\phi \\\|\_{C^{0}\_{w}}) \\end{aligned}

(3.116)


for all functions _ϕ_. It is also clear that _L_ _σ_ is invertible and that we have a uniform _L_ 2 bound for L\_{\\sigma}^{-1}, i.e., \\\|\\phi \\\|\_{L^{2}} \\leqslant \\\|L\_{\\sigma}\\phi \\\|\_{L^{2}} for all _ϕ_ with respect to the L^{2}(\\mathcal{X}\_{\\sigma},\\omega \_{glue,\\sigma}) norm on both sides. However, we will see in Sect. [4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec17) that the obvious desirable strengthening, \\\|\\phi \\\|\_{C^{0}\_{w}} \\leqslant C\\\|L\_{\\sigma}\\phi \\\|\_{C^{0}\_{\\tilde{w}}}, does not hold for all _ϕ_ for any _C_ independent of _σ_. This requires us to introduce an obstruction space.

## 4 Uniform estimate of the inverse of the linearization modulo obstructions

In Sect. [4.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec18) we construct a 1-dimensional function space \\mathbb{R}\\cdot \\hat{u}\_{\\sigma }\\subset C^{\\infty}(\\mathcal{X}\_{ \\sigma}) such that there is a chance of proving uniform weighted Hölder estimates for the inverse of the restriction of _L_ _σ_ to the L^{2}(\\mathcal{X}\_{\\sigma},\\omega \_{glue,\\sigma})-orthogonal complement of \\mathbb{R} \\cdot \\hat{u}\_{\\sigma}. In the rest of this section, starting in Sect. [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec25), we then prove via a standard blowup-and-contradiction scheme that these uniform estimates are actually true. The lack of uniformity on the obstruction space \\mathbb{R}\\cdot \\hat{u}\_{\\sigma} will be dealt with in Sect. [5](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec38).

### 4.1 Definition of the obstruction space

We first sketch the idea: \\hat{u}\_{\\sigma} is constant to the left and zero to the right of the middle neck \\mathfrak{R}\_{4}, and converges in a sufficiently strong sense to \\hat{u}, a solution to an ODE L\_{\\infty }\\hat{u} = 0 on the half-line \\mathbb{R}^{+} = {\\mathrm{GH}}\\lim \_{\\sigma \\to 0}\\mathfrak{R}\_{4} with boundary values 1 on the left and 0 on the right. The solution \\hat{u} is uniquely determined by these conditions and is precisely the obstruction that breaks the obvious attempt at proving uniform estimates for L\_{\\sigma}^{-1} via blowup and contradiction. However, going from \\hat{u} to \\hat{u}\_{\\sigma} turns out to be quite complicated because \\hat{u}\_{\\sigma} is _not_ uniquely defined by the properties we need it to satisfy, so there is no canonical choice of \\hat{u}\_{\\sigma} and we need to come up with some construction that works. We now describe our solution to this problem.

The first step is to construct good coordinates on the neck \\mathfrak{R}\_{4}, which will be used throughout this subsection and which will allow us to state the crucial Proposition [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar86).

As in Corollary [2.29](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar44) and Proposition [2.30](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar46), we parametrize the model neck by

\\begin{aligned} s = 1-\\frac{t}{T} \\in (0,1)\\;\\,\\text{and}\\;\\,\\eta = 1-s = \\frac{t}{T} \\in (0,1). \\end{aligned}

(4.1)


For any _s_ 1< _s_ 2 in (0,1) we introduce coordinates on the universal cover of { _s_ 1< _s_ < _s_ 2} via

\\begin{aligned} \\begin{aligned} (\\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{x}, \\check{\\theta}) := ((-t\_{\*})^{- \\frac{1}{2}} x\_{\\alpha}, (-t\_{\*})^{-\\frac{1}{2}} y\_{\\alpha}, -t\_{\*} x, (-t\_{\*})^{-1}\\theta ), \\\ t\_{\*} := \\left (1-\\frac{s\_{1}+s\_{2}}{2}\\right )T, \\;\\, x := - \\frac{1}{t}. \\end{aligned} \\end{aligned}

(4.2)


Note that, as a function on the universal cover,

\\begin{aligned} s = s(\\check{x}) = 1 - \\frac{1-\\frac{s\_{1}+s\_{2}}{2}}{\\check{x}} \\end{aligned}

(4.3)


is increasing in \\check{x}, and is uniformly smoothly bounded in the chart ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)) if _s_ 1, _s_ 2 are fixed.

### Convention 4.1

From now on we identify the middle neck \\mathfrak{R}\_{4} \\subset \\mathcal{X}\_{\\sigma} with { _T_ +2 _T_ 0< _t_ <2 _τ_}⊂ _TY_ 0 via the diffeomorphism \\Phi \_{\\sigma}^{-1} \\circ \\Psi \_{\\sigma}. Then _s_, _η_ naturally become functions on \\mathfrak{R}\_{4} and \\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{x}, \\check{\\theta} become functions on the universal cover of \\mathfrak{R}\_{4}. The range of _s_ on \\mathfrak{R}\_{4} is an open interval which exhausts all of (0,1) as _σ_ →0\. Also, the _J_ _σ_-Kähler metric _ω_ _glue_, _σ_ on \\mathfrak{R}\_{4} then has the same Kähler potential, _ψ_ _T_, as the _J_ 0-Kähler metric _ω_ _T_. By Lemma [3.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar68), the difference of the associated metric tensors _g_ _glue_, _σ_ and _g_ _T_ measured with respect to either of them is _O_( _e_ −(1/2− _ε_)( _t_ − _T_)) including all covariant derivatives.

In addition to defining the obstruction function \\hat{u}\_{\\sigma} (which will be done in Definition [4.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar98)), our final goal in this subsection is to prove the following property of \\hat{u}\_{\\sigma}, a key result of this paper. The main cause of complication in our definition of \\hat{u}\_{\\sigma} is the need to ensure that this is true. Recall the radial volume density _μ_ ∞( _s_) from Lemma [2.31](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar48) and the weight _w_ _σ_ from Definition [3.17](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar83).

### Proposition 4.2

For _σ_ _i_→0 let x\_{i} \\in \\mathfrak{R}\_{4} \\subset \\mathcal{X}\_{\\sigma \_{i}} satisfy _s_( _x_ _i_)→ _c_ ∈(0,1) and let \\psi \_{i} \\in C^{0}(\\mathcal{X}\_{\\sigma \_{i}}) satisfy w\_{\\sigma \_{i}}(x\_{i}) \|\\psi \_{i}\| \\leqslant w\_{\\sigma \_{i}} on \\mathcal{X}\_{\\sigma \_{i}}. Assume that there exists \\psi \_{\\infty}: (0,1) \\to \\mathbb{R} such that for all _s_ 1< _s_ 2 in (0,1), _ψ_ _i_→ _ψ_ ∞∘ _s_ uniformly in the coordinates ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)) on the universal cover of { _s_ 1< _s_ < _s_ 2}. Then

\\begin{aligned} \\lim \_{i\\to \\infty}\|T\_{i}\|^{2} \\int \_{\\mathcal{X}\_{\\sigma \_{i}}} \\psi \_{i}\\hat{u}\_{\\sigma \_{i}} \\, \\omega \_{glue,\\sigma \_{i}}^{2} = 2 \\pi {\\mathrm{Vol}}(E) \\int \_{0}^{1} \\psi \_{\\infty}(s) \\hat{u}(s)\\,\\mu \_{ \\infty}(s)\\, ds. \\end{aligned}

(4.4)


The remaining steps are now roughly as follows:

- In Lemma [4.3](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar87) we prove that as _σ_ →0 the operators L\_{\\sigma}\|\_{\\mathfrak{R}\_{4}} collapse to a second-order ordinary differential operator _L_ ∞ on the interval _s_ ∈(0,1). Moreover, _L_ ∞ is asymptotic to an explicit model operator L\_{\\infty}^{\\pm} near each of the two endpoints.

- Fundamental solutions for L\_{\\infty}^{\\pm} can be calculated explicitly (Lemma [4.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar89)).

- These endpoint asymptotics imply a Liouville theorem (Lemma [4.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar91)) of independent interest: up to scalar multiples there exists a unique entire solution \\hat{u} to L\_{\\infty }\\hat{u} = 0 compatible with our weights _w_ _σ_, and we have that \\hat{u}(s) \\to 1 as _s_ →0+ and \\hat{u}(s) \\to 0 as _s_ →1−.

- The inhomogeneous ODE L\_{\\infty }\\hat{v} = \\hat{u} has a unique solution \\hat{v} satisfying \\hat{v}(s) \\to 0 as _s_ →1− and satisfying a Neumann type boundary condition as _s_ →0+ (Lemma [4.8](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar96)).

- We transplant \\hat{v} to a function \\hat{v}\_{\\sigma} on \\mathcal{X}\_{\\sigma} using radial cutoff functions and define \\hat{u}\_{\\sigma }:= L\_{\\sigma }\\hat{v}\_{\\sigma} (Definition [4.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar98)). These functions \\hat{u}\_{\\sigma} converge back to \\hat{u} as _σ_ →0 (Lemma [4.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar99)).

- Using the Neumann property of \\hat{v}, we prove that \\hat{u}\_{\\sigma} also satisfies Proposition [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar86).


We will carry out these steps in the following sub-subsections.

#### 4.1.1 Collapse to an ODE on an interval

The study of the limit ODE operator _L_ ∞ requires careful attention to various fractional exponents. We work in the general _n_-dimensional setting because the values of these exponents might look like random numbers for _n_ =2.

### Lemma 4.3

There exists a smooth second-order linear differential operator _L_ ∞ on (0,1) such that:

(1):

Let _σ_ _i_→0 as _i_ →∞. Let \\psi \_{i} \\in C^{2}(\\mathcal{X}\_{\\sigma \_{i}}) be such that for any fixed _s_ 1< _s_ 2 in (0,1),

\\sup \_{\\{s\_{1} < s < s\_{2}\\}} \|\\psi \_{i}\| = O\_{s\_{1},s\_{2}}(1)\\;\\, \\text{and}\\;\\,\\sup \_{\\{s\_{1} < s < s\_{2}\\}} \|L\_{\\sigma \_{i}}\\psi \_{i}\| = o\_{s\_{1},s\_{2}}(1)\\;\\,\\text{as}\\;\\,i\\to \\infty .

(4.5)


Then there is a smooth function \\psi \_{\\infty}: (0,1) \\to \\mathbb{R} such that _L_ ∞ _ψ_ ∞=0 and, after passing to a subsequence and pulling back to the universal cover, we have for all _s_ 1< _s_ 2 that _ψ_ _i_→ _ψ_ ∞∘ _s_ weakly in W^{2,p}\_{loc} and strongly in C^{1,\\beta}\_{loc} with respect to the coordinates ( [4.2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ326)) for all _p_ and _β_.

(2):

While there is no simple formula for _L_ ∞ globally on (0,1), at the endpoints we have that

\\begin{aligned} L\_{\\infty }&= \\frac{1}{n+1} L\_{\\infty}^{+} + O(\\eta ^{n+1})\\;\\, \\text{as}\\;\\,\\eta = 1-s \\to 0^{+}, \\end{aligned}

(4.6)


\\begin{aligned} L\_{\\infty }&= \\frac{1}{d(n)} L\_{\\infty}^{-} + O(s^{\\frac{n+1}{n}})\\; \\,\\text{as}\\;\\,s \\to 0^{+},\\;\\, d(n) := \\left (\\frac{n}{n+1}\\right )^{ \\frac{1}{n}}c(n)^{\\frac{n+1}{n}}. \\end{aligned}

(4.7)


Here the _O_ notation is to be understood in the sense of Definition [2.27](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar42), _c_( _n_) is as in ( [2.90](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ93)), and the two model operators L\_{\\infty}^{\\pm} are given by

\\begin{aligned} L\_{\\infty}^{+} &:= \\eta ^{2}\\partial \_{\\eta \\eta}^{2} - (n-1)\\eta \\partial \_{\\eta }- (n+1)\\cdot{\\mathrm{Id}}, \\end{aligned}

(4.8)


\\begin{aligned} L\_{\\infty}^{-} &:= n s^{\\frac{n-1}{n}}\\partial ^{2}\_{ss} + (n-1)s^{- \\frac{1}{n}}\\partial \_{s} - d(n) \\cdot {\\mathrm{Id}}. \\end{aligned}

(4.9)


### Proof

The chart (\\check{x},\\check{\\theta},\\check{x}\_{\\alpha},\\check{y}\_{\\alpha}) identifies the universal cover of { _s_ 1< _s_ < _s_ 2} with

\\left (\\frac{1-\\frac{s\_{1}+s\_{2}}{2}}{1-s\_{1}}, \\frac{1-\\frac{s\_{1}+s\_{2}}{2}}{1-s\_{2}}\\right ) \\times \\mathbb{R}^{2n-1},

(4.10)


where the interval is compactly contained in (0,1). As recalled in Convention [4.1](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar85), _g_ _glue_, _σ_ and _g_ _T_ are uniformly smoothly bounded on this coordinate slab and differ from each other by

\\begin{aligned} O(e^{-(\\frac{1}{2}-\\varepsilon )(t-T)})\\;\\,\\text{with}\\;\\, t-T \\geqslant 2\|T\|^{ \\alpha }\\;\\,\\text{as}\\;\\,\\sigma \\to 0, \\end{aligned}

(4.11)


including all derivatives. Also, by construction, g\_{glue,\\sigma \_{i}}, g\_{T\_{i}} and _ψ_ _i_ are invariant under the deck group Γ_i_ of the universal cover, which preserves \\check{x} and acts as a discrete Heisenberg group with fundamental domain diameter ∼(− _t_ ∗, _i_)−1/2∼\| _T_ _i_\|−1/2∼\|log\| _σ_ _i_\|\|−1/2 on the coordinates (\\check{\\theta},\\check{x}\_{\\alpha},\\check{y}\_{\\alpha}) \\in \\mathbb{R}^{2n-1}.

By assumption, the Γ_i_-invariant functions \| _ψ_ _i_\| are uniformly bounded and the Γ_i_-invariant functions \|L\_{\\sigma \_{i}}\\psi \_{i}\| uniformly converge to zero as _i_ →∞. Here, L\_{\\sigma \_{i}} = \\Delta \_{\\omega \_{glue,\\sigma \_{i}}} - {\\mathrm{Id}} is a uniformly elliptic sequence of differential operators whose coefficients are uniformly smoothly bounded with respect to _i_. Thus, by standard _L_ _p_ elliptic regularity theory on balls, _ψ_ _i_ is locally uniformly bounded in _W_ 2, _p_ for every _p_ ∈(1,∞) and hence, by Morrey embedding, in _C_ 1, _β_ for every _β_ ∈(0,1). By applying the Alaoglu and Arzelà-Ascoli compactness theorems and passing to a diagonal subsequence, we have that _ψ_ _i_→ _ψ_ ∞ locally weakly in _W_ 2, _p_ for all _p_ ∈(1,∞) and strongly in _C_ 1, _β_ for all _β_ ∈(0,1). The subsequence can be taken to be independent of _s_ 1, _s_ 2 by letting _s_ 1→0, _s_ 2→1 and diagonalizing. Moreover, for any points _p_, _q_ in our chart with _s_( _p_)= _s_( _q_), we can estimate \| _ψ_ _i_( _p_)− _ψ_ _i_( _q_)\| as follows: Without loss of generality, _p_, _q_ lie in a fundamental domain of Γ_i_ (because _ψ_ _i_ is invariant under Γ_i_) and are joined by a curve _γ_ with _s_ ∘ _γ_ = _const_ whose \\omega \_{glue,\\sigma \_{i}}-length is _O_((− _t_ ∗, _i_)−1/2)= _O_(\|log\| _σ_ _i_\|\|−1/2)→0\. Since the gradient of _ψ_ _i_ with respect to \\omega \_{glue,\\sigma \_{i}} is uniformly bounded, this implies that \| _ψ_ _i_( _p_)− _ψ_ _i_( _q_)\|= _O_(\|log\| _σ_ _i_\|\|−1/2) and hence _ψ_ ∞( _p_)= _ψ_ ∞( _q_). Thus, _ψ_ ∞ depends only on the radial coordinate _s_. This means that the first-order classical derivatives \\psi \_{\\infty , \\check{x}\_{\\alpha}}, \\psi \_{\\infty ,\\check{y}\_{ \\alpha}}, \\psi \_{\\infty ,\\check{\\theta}} are identically zero, so their weak gradients, which exist locally in _L_ _p_, are zero a.e. Thus, the corresponding first-order derivatives of _ψ_ _i_ go to zero strongly in C^{0,\\beta}\_{loc} for every _β_ and their gradients go to zero weakly in L^{p}\_{loc} for every _p_.

We now argue that _ψ_ ∞ is a weak, hence classical, solution of an ODE _L_ ∞ _ψ_ ∞=0, where _L_ ∞ is a smooth second-order linear differential operator in _s_ ∈(0,1) which is independent of the sequence _ψ_ _i_ and is asymptotically modeled by L\_{\\infty}^{\\pm} at the two endpoints. The key to this are Corollary [2.29](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar44) and Proposition [2.30](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar46). Written in terms of (\\eta , \\check{x}\_{\\alpha},\\check{y}\_{\\alpha},\\check{\\theta}), the former says that for _η_ ⩽ _δ_ <1,