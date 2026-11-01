---
retention_scope: session
part: 2
total_parts: 7
---

[Part 2/7 of: A Continuous Cusp Closing Process for Negative Kähler–Einstein Metrics]

\\begin{aligned} &f:S^{5}\\times \[0,\\infty )\\times \\mathbb{C}\\to \\mathbb{C},\\\ &f(z,r,y)= 3y\\left ( \\sum \_{i=1}^{3}\|z\_{i}\|^{4}\\right )+3y^{2}\\left (\\sum \_{i=1}^{3}\|z\_{i}\|^{2} \\overline{z}^{3}\_{i}\\right )+ y^{3} \\left (\\sum \_{i=1}^{3} \\overline{z}\_{i}^{6}\\right )-r^{3}, \\end{aligned}\
\
(2.11)\
\
\
and fix any point _p_ =( _p_ 1, _p_ 2, _p_ 3)∈ _S_ 5. Since\
\
\\begin{aligned} f(p,0,0)=0,\\;\\, \\frac{\\partial f}{\\partial y}(p,0,0)=3\\sum \_{i=1}^{3}\|p\_{i}\|^{4} \\neq 0, \\end{aligned}\
\
(2.12)\
\
\
the implicit function theorem asserts the existence of a unique smooth function _g_ _p_, defined in some open neighborhood _U_ _p_×\[0, _ε_ _p_) of ( _p_,0), such that _g_ _p_( _p_,0)=0 and _f_( _z_, _r_, _g_ _p_( _z_, _r_))=0\. An obvious covering argument on _S_ 5 then yields a smooth function g: S^{5} \\times \[0,\\varepsilon ) \\to \\mathbb{C} satisfying\
\
\\begin{aligned} g(z,0)=0, \\quad f(z,r,g(z,r))=0. \\end{aligned}\
\
(2.13)\
\
\
We now set _R_ = _ε_ −1 and define \\nu :\\mathbb{C}^{3}\\setminus \\overline{B}\_{R}\\to \\mathbb{C} by\
\
\\begin{aligned} \\nu (z) = \\frac{1}{\|z\|}g\\left (\\frac{z}{\|z\|},\\frac{1}{\|z\|}\\right ). \\end{aligned}\
\
(2.14)\
\
\
The fact that _ν_ satisfies \\sum \_{i=1}^{3}(z\_{i}+\\nu (z)\\overline{z}\_{i}^{2})^{3}=1 for each z\\in TY\_{0} \\setminus \\overline{B}\_{R} is straightforward to verify.\
\
Now we show that _ν_( _z_)= _O_(\| _z_ \|−4). To see this, observe that _ν_( _z_)\| _z_ \|4 _P_( _z_)=1 on \\mathbb{C}^{3}\\setminus \\overline{B}\_{R}, where\
\
P(z)=3\\left (\\sum \_{i=1}^{3}\\frac{\|z\_{i}\|^{4}}{\|z\|^{4}}\\right )+3( \\nu (z)\|z\|)\\left (\\sum \_{i=1}^{3} \\frac{\|z\_{i}\|^{2}\\overline{z}^{3}\_{i}}{\|z\|^{5}}\\right )+(\\nu (z)\|z\|)^{2} \\left (\\sum \_{i=1}^{3}\\frac{\\overline{z}\_{i}^{6}}{\|z\|^{6}}\\right ).\
\
(2.15)\
\
\
It then suffices to note that \\nu (z)\|z\| = g(\\frac{z}{\|z\|},\\frac{1}{\|z\|}) \\to 0 uniformly as \| _z_ \|→∞.\
\
In order to complete the proof of the lemma, we show that _∂_ _k_ _ν_( _z_)= _O_(\| _z_ \|−4− _k_) for all _k_ ⩾1\. We only do this for _k_ =1\. To this end, note that _ν_( _z_)=1/(\| _z_ \|4 _P_( _z_)). Thus, using the expression of _P_( _z_) in ( [2.15](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ18)), it suffices to show that _∂_( _ν_( _z_)\| _z_ \|)= _O_(\| _z_ \|−1). But this follows from ( [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ17)) and from the fact that _g_ is a smooth function on _S_ 5×\[0, _ε_). The lemma is proved. □\
\
Now we define a diffeomorphism Φ from TY\_{0}\\setminus \\overline{B}\_{R} onto its image contained in _TY_ 1 as follows:\
\
\\Phi (z\_{1},z\_{2},z\_{3}):=(z\_{1}+\\nu (z)\\overline{z}\_{1}^{2},z\_{2}+ \\nu (z)\\overline{z}\_{2}^{2},z\_{3}+\\nu (z)\\overline{z}\_{3}^{2}).\
\
(2.16)\
\
\
With this, we can trivialize the family _TY_ _σ_ diffeomorphically at infinity.\
\
### Definition 2.4\
\
Let Φ be defined by ( [2.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ19)), m'\_{\\sigma}:TY\_{0}\\to TY\_{0} by sending _z_ to _σ_ −1/3 _z_ and _m_ _σ_: _TY_ _σ_→ _TY_ 1 by sending _z_ to _σ_ −1/3 _z_. Then we define a family of maps \\Phi \_{\\sigma}: TY\_{0}\\setminus B\_{\|\\sigma \|^{1/3}R}\\to TY\_{\\sigma} by\
\
\\Phi \_{\\sigma}:=m^{-1}\_{\\sigma}\\circ \\Phi \\circ m'\_{\\sigma}.\
\
(2.17)\
\
\
### Lemma 2.5\
\
Let _z_ ∈ _TY_ 0 with \| _z_ \|⩾\| _σ_ \|1/3 _R_ and also set _ν_ _σ_( _z_):= _σ_ −1/3 _ν_( _σ_ −1/3 _z_). Then\
\
\\Phi \_{\\sigma}(z\_{1},z\_{2},z\_{3})=(z\_{1}+\\nu \_{\\sigma}(z)\\overline{z}\_{1}^{2},z\_{2}+ \\nu \_{\\sigma}(z)\\overline{z}\_{2}^{2},z\_{3}+\\nu \_{\\sigma}(z) \\overline{z}\_{3}^{2})\
\
(2.18)\
\
\
with _∂_ _k_ _ν_ _σ_( _z_)= _O_(\| _σ_ \|\| _z_ \|−4− _k_) as \| _σ_ \|−1/3\| _z_ \|→∞ for all _k_ ⩾0.\
\
### Proof\
\
By ( [2.17](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ20)), for _z_ ∈ _TY_ 0,\
\
\\begin{aligned} \\begin{aligned} &\\Phi \_{\\sigma}(z\_{1},z\_{2}, z\_{3}) \\\ &\\quad= (z\_{1}+\\sigma ^{-\\frac{1}{3}} \\nu (\\sigma ^{-\\frac{1}{3}}z) \\overline{z}\_{1}^{2}, z\_{2}+\\sigma ^{- \\frac{1}{3}}\\nu (\\sigma ^{-\\frac{1}{3}}z) \\overline{z}\_{2}^{2}, z\_{3}+ \\sigma ^{-\\frac{1}{3}}\\nu (\\sigma ^{-\\frac{1}{3}}z) \\overline{z}\_{3}^{2}). \\end{aligned} \\end{aligned}\
\
(2.19)\
\
\
Recall that _∂_ _k_ _ν_( _z_)= _O_(\| _z_ \|−4− _k_) as \| _z_ \|→∞ for all _k_ ⩾0\. Thus,\
\
\\begin{aligned} \\partial ^{k} \\nu \_{\\sigma}(z) = \\sigma ^{-\\frac{1+k}{3}}(\\partial ^{k} \\nu )(\\sigma ^{-\\frac{1}{3}}z) = O(\|\\sigma \|^{-\\frac{1+k}{3}}(\| \\sigma \|^{-\\frac{1}{3}}\|z\|)^{-4-k}) = O(\|\\sigma \| \|z\|^{-4-k}) \\end{aligned}\
\
(2.20)\
\
\
as \| _σ_ \|−1/3\| _z_ \|→∞. □\
\
### Remark 2.6\
\
By Lemma [2.5](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar7), Φ_σ_ is well-defined if \| _z_ \|⩾\| _σ_ \|1/3 _R_ for some sufficiently large but fixed _R_ ≫1\. However, the gluing will later be carried out in a region where \| _z_ \| is much larger than this. More precisely, the gluing region is \|z\| = \|\\sigma \|^{1/3} e^{\\zeta \\,\\cdot \\, \|{\\log \|\\sigma \|}\|^{\\alpha}} for some fixed \\alpha < \\frac{1}{2} and for _ζ_ ∈\[1,2\].\
\
Lastly, we use the above identifications to trivialize the family \\{\\mathcal{X}\_{\\sigma}\\}\_{\\sigma \\in \\Delta} diffeomorphically away from smaller and smaller neighborhoods of the singularity (0,0,0) \\in \\mathcal{X}\_{0} \\subset \\mathbb{C}^{3}.\
\
### Lemma 2.7\
\
There exists a _C_ 5 diffeomorphism _G_ _σ_ from \\mathcal {X}\_{0}\\setminus \\{\|z\| \\leqslant 3\|\\sigma \|^{1/3}R\\} onto its image, which is contained in \\mathcal {X}\_{\\sigma}\\setminus \\{\|z\|\\leqslant 2\|\\sigma \|^{\\frac{1}{3}}R\\} and contains \\mathcal{X}\_{\\sigma }\\setminus \\{\|z\| \\leqslant 4\|\\sigma \|^{1/3}R\\}, such that the following hold:\
\
(1):\
\
_G_ _σ_ is smooth away from the hyperplane { _Z_ 0=0} and is the identity on this hyperplane.\
\
(2):\
\
Fix _R_ 0≪1 so that Ψ is defined on \| _z_ \|⩽3 _R_ 0. Then G\_{\\sigma }= \\Psi \_{\\sigma}^{-1}\\circ \\Phi \_{\\sigma}\\circ \\Psi \_{0} for \| _z_ \|⩽ _R_ 0.\
\
(3):\
\
If we denote the complex structure of \\mathcal {X}\_{\\sigma} by _J_ _σ_, then for any _r_ 0>0 and any smooth metric _ω_ 0 on \\mathcal {X}\_{0}\\setminus \\{\|z\| < r\_{0}\\} we have that\
\
\\begin{aligned} \|\\nabla ^{k}\_{\\omega \_{0}} (G^{\*}\_{\\sigma }J\_{\\sigma}-J\_{0})\|\_{ \\omega \_{0}} =O\_{r\_{0},\\omega \_{0}}(\|\\sigma \|)\\;\\,\\text{on}\\;\\, \\mathcal {X}\_{0}\\setminus \\{\|z\| < r\_{0}\\} \\end{aligned}\
\
(2.21)\
\
\
for all _σ_ sufficiently small depending on _r_ 0 and for all 0⩽ _k_ ⩽4.\
\
### Proof\
\
By construction, \\mathcal{X} = \\{(Z,\\sigma ) \\in \\mathbb{CP}^{3} \\times \\Delta : p(Z) = \\sigma Z\_{0}^{6}\\} for a certain homogeneous sextic _p_. By ( [2.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ7)), all fibers \\mathcal{X}\_{\\sigma }= \\{Z \\in \\mathbb{CP}^{3}: (Z,\\sigma ) \\in \\mathcal{X}\\} intersect the plane { _Z_ 0=0} transversely in the smooth curve \\{Z\_{0}=0, Z\_{1}^{6} + Z\_{2}^{6} + Z\_{3}^{6} = 0\\}. Write \\mathbb{A}^{3} to denote the affine chart { _Z_ 0≠0} and define\
\
q: \\mathbb{A}^{3} \\to \\mathbb{C}, \\;\\, q(Z) := p(Z)/Z\_{0}^{6}.\
\
(2.22)\
\
\
Let ∇ _q_ denote the type (1,0) gradient of _q_ with respect to the standard Euclidean Kähler metric on \\mathbb{A}^{3} and let \|∇ _q_ \| denote the Euclidean length of ∇ _q_. Then the smooth (1,0)-vector field\
\
V := \\left (\\frac{\\nabla q}{\|\\nabla q\|^{2}},1 \\right ) \\in T^{1,0}( \\mathbb{A}^{3} \\times \\Delta )\
\
(2.23)\
\
\
is defined at all points of the submanifold \\mathcal{X}' := (\\mathcal{X}\\setminus \\mathcal{X}\_{0}^{sing}) \\cap ( \\mathbb{A}^{3} \\times \\Delta ) and is tangent to \\mathcal{X}'. In fact, the time- _σ_ flow of _V_ maps the fiber \\mathcal{X}'\_{\\tau} into the fiber \\mathcal{X}'\_{\\tau +\\sigma} for every _τ_.\
\
### Claim 2.8\
\
_V_ extends from \\mathcal{X}' to \\mathcal{X} \\setminus \\mathcal{X}\_{0}^{sing} as a _C_ 5 vector field vanishing along the infinity divisor.\
\
### Proof of Claim [2.8](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar12)\
\
It suffices to check this in the chart { _Z_ 1≠0}. Define affine coordinates _w_ 1= _Z_ 0/ _Z_ 1, _w_ 2= _Z_ 2/ _Z_ 1, _w_ 3= _Z_ 3/ _Z_ 1 on this chart. Then _d_(1/ _w_ 1), _d_( _w_ 2/ _w_ 1), _d_( _w_ 3/ _w_ 1) are an orthonormal (1,0)-coframe with respect to the standard Euclidean metric on \\mathbb{A}^{3} = \\{w\_{1} \\neq 0\\}. The following (0,1)-frame (written as vectors with respect to \\partial \_{\\overline{w}\_{1}},\\partial \_{\\overline{w}\_{2}},\\partial \_{ \\overline{w}\_{3}}) is metrically dual to this coframe:\
\
V\_{1} := (-w\_{1}^{2},-w\_{1}w\_{2},-w\_{1}w\_{3}),\\;\\,V\_{2} := (0,w\_{1},0), \\;\\,V\_{3} := (0,0,w\_{1}).\
\
(2.24)\
\
\
With _ψ_( _t_):= _t_ 6+ _t_ 3 we then have that _q_ = _ψ_(1/ _w_ 1)+ _ψ_( _w_ 2/ _w_ 1)+ _ψ_( _w_ 3/ _w_ 1) and so\
\
\\overline{\\nabla q} = \\psi '\\left (\\frac{1}{w\_{1}}\\right )V\_{1} + \\psi '\\left (\\frac{w\_{2}}{w\_{1}}\\right )V\_{2} + \\psi '\\left ( \\frac{w\_{3}}{w\_{1}}\\right )V\_{3}.\
\
(2.25)\
\
\
It follows that \| _w_ 1\|10\|∇ _q_ \|2 is smooth and ⩾36 at { _w_ 1=0}. Using this fact and the transversality of \\mathcal{X} to the hyperplane { _Z_ 0=0}×Δ, we get that the T^{1,0}\\mathbb{CP}^{3} component of _V_ vanishes to order 6 at the infinity divisor in \\mathcal{X}. Thus, _V_ extends as a _C_ 5 vector field. □\
\
We may assume that C^{-1}\\leqslant \|V\|\_{\\omega \_{0}} \\leqslant C for some positive constant _C_ on the set \|z\|\\geqslant \\frac{R\_{0}}{2}. Consider the flow _H_ _t_ induced by _V_ on \\mathcal {X}'\\setminus \\{\|z\| < \\frac{R\_{0}}{2}\\}. For _σ_ sufficiently small, _H_ _σ_ induces a diffeomorphism from \\mathcal {X}'\_{0}\\setminus \\{\|z\|< \\frac{3R\_{0}}{4}\\} onto its image in \\mathcal {X}'\_{\\sigma}. Here we use the fact that \|V\|\_{\\omega \_{0}} is uniformly bounded on \\mathcal {X}'\\setminus \\{\|z\|< \\frac{R\_{0}}{2}\\}, so the incompleteness of \\mathcal {X}' does not affect that _H_ _σ_ is a diffeomorphism when _σ_ is sufficiently small and \|z\|\\geqslant \\frac{3R\_{0}}{4}. It follows that on the strip S :=\\{ {R\_{0} \\leqslant \|z\| \\leqslant 2R\_{0}}\\}\\cap \\mathcal {X}\_{0} we have two diffeomorphisms \\Psi \_{\\sigma}^{-1} \\circ \\Phi \_{\\sigma }\\circ \\Psi \_{0} and _H_ _σ_ onto some region of \\mathcal {X}\_{\\sigma}. Use the map \\Psi \_{\\sigma}^{-1}\\circ \\Phi \_{\\sigma}\\circ \\Psi \_{0} to identify _S_ with its image inside \\mathcal {X}\_{\\sigma}. Under this identification, _H_ _σ_ can be seen as a family of embeddings\
\
\\begin{aligned} \\tilde{H}\_{\\sigma}: S'\\to S \\end{aligned}\
\
(2.26)\
\
\
from S' := \\{1.1R\_{0} \\leqslant \|z\| \\leqslant 1.9R\_{0}\\} \\cap \\mathcal{X} into _S_. Since \\tilde{H}\_{\\sigma}\\to{\\mathrm{Id}}\_{S'} as _σ_ →0, \\tilde{H}\_{\\sigma} is smoothly isotopic to the identity map on _S_′ when _σ_ is sufficiently small. In particular, \\tilde{H}\_{\\sigma} is given by the flow of a time-dependent vector field \\tilde{V}\_{\\sigma} defined on \\tilde{H}\_{\\sigma}(S'). Let _τ_: _S_ →\[0,1\] be a smooth cut-off function given by _τ_( _z_)= _χ_(\| _z_ \|), where _χ_ is a smooth increasing function equal to zero for \| _z_ \|⩽1.3 _R_ 0 and equal to 1 for \| _z_ \|⩾1.7 _R_ 0. Let \\tilde{I}\_{\\sigma} be the diffeomorphisms generated by the vector field \\tau \\tilde{V}\_{\\sigma} for _σ_ sufficiently small. By construction, \\tilde{I}\_{\\sigma} is equal to the identity for \| _z_ \|⩽1.2 _R_ 0 and equal to \\tilde{H}\_{\\sigma} for \| _z_ \|⩾1.8 _R_ 0. Thus, the diffeomorphism\
\
G\_{\\sigma}:= \\textstyle\\begin{cases} \\Psi \_{\\sigma}^{-1} \\circ \\Phi \_{\\sigma }\\circ \\Psi \_{0} \\circ \\tilde{I}\_{\\sigma }& \\text{for}\\;\\, \|z\|\\leqslant 1.8R\_{0}, \\\ H\_{\\sigma }& \\text{for}\\;\\, \|z\| \\geqslant 1.8R\_{0},\\end{cases}\
\
(2.27)\
\
\
satisfies the desired properties. □ □\
\
### 2.2 Singular Kähler-Einstein metrics with hyperbolic cusps\
\
Let \\mathcal {X} = \\{\\mathcal{X}\_{\\sigma}\\}\_{\\sigma \\in \\Delta} be the family of sextic surfaces in \\mathbb{CP}^{3} discussed above. Recall that we have removed a family of hyperplane sections \\mathcal{D} = \\{\\mathcal{D}\_{\\sigma}\\}\_{\\sigma \\in \\Delta} with \[2\\mathcal{D}\_{\\sigma}\] = K\_{\\mathcal {X}\_{\\sigma}} for all _σ_ ∈Δ, thus defining a family of affine surfaces \\mathcal {Y}\_{\\sigma}=\\mathcal {X}\_{\\sigma}\\setminus \\mathcal{D}\_{\\sigma}, and that we have also fixed a family of holomorphic volume forms Ω_σ_ (unique up to scaling) on \\mathcal {Y}\_{\\sigma} that vanish to order 2 along the infinity divisors \\mathcal{D}\_{\\sigma}.\
\
It is a well-known fact that the regular part of \\mathcal{X}\_{0} admits a unique complete Kähler-Einstein metric _ω_ _KE_,0 with Ricci curvature −1. This fact can nowadays be viewed as a very special case of a general theory of complete Kähler-Einstein metrics on log-canonical models; see \[ [BG14](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR4 " 					Berman, R., Guenancia, H.: Kähler-Einstein metrics on stable varieties and log canonical pairs. Geom. Funct. Anal. 24, 1683–1730 (2014) 				"), Thm A\] and \[ [Son17](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR33 " 					Song, J.: Degeneration of Kähler-Einstein manifolds of negative scalar curvature. Preprint (2017). arXiv:                   1706.01518                                    "), Sect. 3\]. However, in the 2-dimensional case—particularly for surfaces of general type with elliptic singularities such as our \\mathcal{X}\_{0}—the required existence result actually goes back to work of R. Kobayashi \[ [Kob85](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR23 " 					Kobayashi, R.: Einstein-Kaehler metrics on open algebraic surfaces of general type. Tohoku Math. J. 37, 43–77 (1985) 				"), Thm 1\] and of Cheng-Tian-Yau \[ [CY86](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR8 " 					Cheng, S.-Y., Yau, S.-T.: Inequality between Chern numbers of singular Kähler surfaces and characterization of orbit space of discrete group of SU(2,1). In: Complex Differential Geometry and Nonlinear Differential Equations, Brunswick, ME, 1984. Contemp. Math., vol. 49, pp. 31–44. Am. Math. Soc., Providence (1986) 				"), [TY87](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR37 " 					Tian, G., Yau, S.-T.: Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry. In: Mathematical Aspects of String Theory, San Diego, CA, 1986. Adv. Ser. Math. Phys., vol. 1, pp. 574–628. World Sci. Publishing, Singapore (1987) 				")\]. We now briefly review the construction of _ω_ _KE_,0 in our example.\
\
In our example, recall that K\_{\\mathcal {X}\_{\\sigma}}\\cong \\mathcal {O}(2)\|\_{\\mathcal {X}\_{\\sigma}}. Fix the embedding \\mathbb{CP}^{3}\\to \\mathbb{CP}^{9} induced by \\mathcal {O}(2) as\
\
\\begin{aligned}{} \[Z\_{0},Z\_{1},Z\_{2},Z\_{3}\]\\longrightarrow \[Z\_{0}^{2},Z\_{0}Z\_{1},Z\_{0}Z\_{2},Z\_{0}Z\_{3},Z\_{1}^{2},Z\_{1}Z\_{2},Z\_{1}Z\_{3},Z\_{2}^{2},Z\_{2}Z\_{3},Z\_{3}^{2}\]. \\end{aligned}\
\
(2.28)\
\
\
Restricting the Fubini-Study metric on \\mathbb{CP}^{9} to the image of \\mathbb{CP}^{3}, we have\
\
\\begin{aligned} \\begin{aligned} \\omega \_{FS}&:=i\\partial \\overline {\\partial }\\log (\|Z\_{0}^{2}\|^{2}+\|Z\_{0}Z\_{1}\|^{2}+\|Z\_{0}Z\_{2}\|^{2}+\|Z\_{0}Z\_{3}\|^{2}+\|Z\_{1}^{2}\|^{2}+\|Z\_{1}Z\_{2}\|^{2}\\\ &+\|Z\_{1}Z\_{3}\|^{2} +\|Z\_{2}^{2}\|^{2}+\|Z\_{2}Z\_{3}\|^{2}+\|Z\_{3}^{2}\|^{2}). \\end{aligned} \\end{aligned}\
\
(2.29)\
\
\
On the affine piece _Z_ 0≠0, we set\
\
\\begin{aligned} \\psi \_{FS}:={}&\\log (1+\|z\_{1}\|^{2}+\|z\_{2}\|^{2}+\|z\_{3}\|^{2}+\|z\_{1}\|^{4}+\|z\_{1}z\_{2}\|^{2}+\|z\_{1}z\_{3}\|^{2}\\\ &{}+\|z\_{2}\|^{4}+\|z\_{2}z\_{3}\|^{2}+\|z\_{3}\|^{4}). \\end{aligned}\
\
(2.30)\
\
\
For better emphasis, we also introduce the notation\
\
\\begin{aligned} \\omega \_{FS,\\sigma} := \\omega \_{FS}\|\_{\\mathcal{X}\_{\\sigma}},\\;\\,\\psi \_{FS, \\sigma} := \\psi \_{FS}\|\_{\\mathcal{Y}\_{\\sigma}}\\;\\,\\text{for all}\\;\\, \\sigma \\in \\Delta . \\end{aligned}\
\
(2.31)\
\
\
Now let us fix a volume form _V_ on \\mathcal {X}\_{0}, which is induced by the Fubini-Study metric of the line bundle \\mathcal {O}(1) on \\mathbb{CP}^{9}, such that\
\
\\omega \_{FS,0} =i\\partial \\overline {\\partial }\\log V.\
\
(2.32)\
\
\
Then the complex Monge-Ampère equation of interest on \\mathcal {X}\_{0} is given by\
\
(\\omega \_{FS,0}+i\\partial \\overline {\\partial }\\psi \_{0})^{2} = e ^{\\psi \_{0}} V.\
\
(2.33)\
\
\
We have the following existence result from \[ [Kob85](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR23 " 					Kobayashi, R.: Einstein-Kaehler metrics on open algebraic surfaces of general type. Tohoku Math. J. 37, 43–77 (1985) 				"), Thm 1\], \[ [BG14](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR4 " 					Berman, R., Guenancia, H.: Kähler-Einstein metrics on stable varieties and log canonical pairs. Geom. Funct. Anal. 24, 1683–1730 (2014) 				"), Thm C\], \[ [Son17](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR33 " 					Song, J.: Degeneration of Kähler-Einstein manifolds of negative scalar curvature. Preprint (2017). arXiv:                   1706.01518                                    "), Lemma 3.6\], together with an asymptotic estimate of the solution _ψ_ 0 from \[ [NGG23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR11 " 					Di Nezza, E., Guedj, V., Guenancia, H.: Families of singular Kähler-Einstein metrics. J. Eur. Math. Soc. 25, 2697–2762 (2023) 				"), Prop D\], \[ [SSW20](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR34 " 					Song, J., Sturm, J., Wang, X.: Continuity of the Weil-Petersson potential. Preprint (2020). arXiv:                   2008.11215                                    "), Prop 3.1\], \[ [DFS23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR10 " 					Datar, V., Fu, X., Song, J.: Kähler-Einstein metric near an isolated log canonical singularity. J. Reine Angew. Math. 797, 79–116 (2023) 				"), Thm 1.1\].\
\
### Theorem 2.9\
\
_The equation_ ( [2.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ36)) _admits a solution_\\psi \_{0} \\in C^{\\infty}(\\mathcal{X}\_{0}^{reg}) _satisfying_\
\
\\begin{aligned} -(3+\\varepsilon )\\log (-{\\log \|\\sigma \_{E}\|\_{h\_{E}}})-C\_{\\varepsilon }\\leqslant \\pi ^{\*}(\\Psi \_{0}^{-1})^{\*}\\psi \_{0}\\leqslant C \\end{aligned}\
\
(2.34)\
\
\
_for every_ _ε_ >0, _where_ _π_ _is the resolution_ ( [2.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ10)), _σ_ _E_ _is a defining section of_ _E_ _inside the total space_\\hat{L} _and_ _h_ _E_ _is any Hermitian metric on_ _L_ → _E_.\
\
It will be convenient to rewrite the Monge-Ampère equation ( [2.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ36)) in the following manner.\
\
### Lemma 2.10\
\
Define _ψ_ _KE_,0:= _ψ_ 0+ _ψ_ _FS_,0, where _ψ_ 0 is the solution provided by Theorem [2.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar14). Then, after adding a constant to _ψ_ _KE_,0, the Kähler-Einstein metric \\omega \_{KE,0}:=i\\partial \\overline {\\partial }\\psi \_{KE,0} satisfies\
\
\\log \\frac{\\omega \_{KE,0}^ {2}}{\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0}}=\\psi \_{KE,0}.\
\
(2.35)\
\
\
### Proof\
\
By construction, ( [2.33](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ36)), we have that\
\
\\log \\frac{\\omega \_{KE,0}^{2}}{V} = \\psi \_{KE,0} - \\psi \_{FS,0}.\
\
(2.36)\
\
\
Recall that by definition, _V_ is the unique real volume form on the regular part of \\mathcal{X}\_{0} that, viewed as a Hermitian metric on K\_{\\mathcal{X}\_{0}}, maps to the Fubini-Study metric _h_ _FS_ under the adjunction isomorphisms K\_{\\mathcal{X}\_{0}} \\cong \\mathcal{O}\_{\\mathbb{CP}^{3}}(2)\|\_{ \\mathcal{X}\_{0}} \\cong \\mathcal{O}\_{\\mathbb{CP}^{9}}(1)\|\_{\\mathcal{X}\_{0}}. On the other hand, also by construction, Ω0 vanishes to order 2 along the hyperplane section \\mathcal{D}\_{0} = \\mathcal{X}\_{0} \\setminus \\mathcal{Y}\_{0} and vanishes nowhere else. Thus, under the above adjunctions, Ω0 maps to some nonzero multiple of the section _S_ of \\mathcal{O}\_{\\mathbb{CP}^{9}}(1)\|\_{\\mathcal{X}\_{0}} that cuts out the hyperplane \\mathcal{D}\_{0}. The square of the Hermitian norm of Ω0 with respect to _V_ is (\\Omega \_{0} \\wedge \\overline{\\Omega}\_{0})/V, and \|S\|\_{h\_{FS}}^{2} = -\\psi \_{FS,0}. Thus, we get ( [2.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ38)) from ( [2.36](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ39)) by adding _ψ_ _FS_,0+ _const_ to both sides. □\
\
We now turn to a more precise asymptotic description of _ψ_ _KE_,0 near the singularity p \\in \\mathcal{X}\_{0}. After introducing the relevant radial model potential _ψ_ _cusp_ and proving some technical lemmas, we will give the precise asymptotics of _ψ_ _KE_,0 in Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar23), which is the final result of this section.\
\
Working on the line bundle _L_ whose total space \\hat{L} resolves the singularity, let _h_ denote the Hermitian metric on _L_ (unique up to scale) whose curvature form is minus the flat Kähler form _ω_ _E_ representing 2\\pi c\_{1}(L') \\in H^{1,1}(E,\\mathbb{R}). Here _L_′ denotes the dual of _L_. We also denote the positively curved Hermitian metric dual to _h_ by _h_′. Abusing notation, we view _h_ as a function on the total space of _L_ via\
\
h: \\hat{L} \\to \\mathbb{R}, \\;\\, \\xi \\mapsto \|\\xi \|\_{h}^{2}.\
\
(2.37)\
\
\
We consider radial Kähler metrics \\omega = i\\partial \\overline{\\partial} \\psi (t) on {0< _h_ ⩽ _δ_}, where \\psi : (-\\infty , \\log \\delta \] \\rightarrow \\mathbb{R} and\
\
\\begin{aligned} t := \\log h. \\end{aligned}\
\
(2.38)\
\
\
Since the discussion of these model Kähler metrics (here as well as in all subsequent sections) works more or less the same way in all dimensions _n_ with ( _L_′, _h_′)→( _E_, _ω_ _E_) a polarized compact Calabi-Yau ( _n_ −1)-fold, we prefer to _not_ specialize our computations of these metrics to the case _n_ =2.\
\
Continuing to work in the general _n_-dimensional setting, we fix a nowhere vanishing holomorphic ( _n_ −1)-form Ω_E_ on _E_ with\
\
\\omega \_{E}^{n-1}=i^{(n-1)^{2}} \\Omega \_{E}\\wedge \\overline{\\Omega}\_{E}.\
\
(2.39)\
\
\
Note that Ω_E_ is unique up to multiplication by a unit complex number. Using this, we now construct a holomorphic volume form \\Omega \_{\\mathcal {C}} on the total space of the \\mathbb{C}^{\*}-bundle associated with _L_ or _L_′, i.e., on the complement of the zero section in the total space of either one of these two line bundles. This form \\Omega \_{\\mathcal{C}} will be unique up to sign, and will have first-order poles along both zero sections such that its residues at these poles are equal to ±Ω_E_. Precisely, let _p_ denote the bundle projection from the total space of the \\mathbb{C}^{\*}-bundle onto _E_ and let ± _Z_ denote the (1,0)-vector field on the total space that generates the natural \\mathbb{C}^{\*}-action coming from either _L_ or _L_′. Then \\Omega \_{\\mathcal {C}} is determined by the equation\
\
\\pm Z \\lrcorner \ \\Omega \_{\\mathcal {C}}=p^{\*}\\Omega \_{E}.\
\
(2.40)\
\
\
A radial (1,1)-form \\omega = i\\partial \\overline{\\partial}\\psi (t) as above is positive definite if and only if\
\
\\begin{aligned} \\psi '(t), \\psi ''(t)>0. \\end{aligned}\
\
(2.41)\
\
\
Then _ω_ is a Kähler-Einstein metric if ( [2.41](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ44)) holds and\
\
\\begin{aligned} (\\psi ')^{n-1} \\psi '' =e^{\\psi +a} \\end{aligned}\
\
(2.42)\
\
\
for some a \\in \\mathbb{R}. If _ψ_ satisfies ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)), then given any k \\in \\mathbb{R}^{+}, the function Ψ( _t_):= _ψ_( _kt_) satisfies\
\
\\begin{aligned} (\\Psi ')^{n-1} \\Psi '' =e^{\\Psi +a +(n+1)\\log k}, \\end{aligned}\
\
(2.43)\
\
\
which is the same as equation ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) except having a different _a_. The solutions related to the cuspidal model Kähler-Einstein metrics in our previous paper \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\] are\
\
\\begin{aligned} \\psi \_{cusp}(t) = -(n+1) \\log (-t),\\;\\, e^{a} = (n+1)^{n}. \\end{aligned}\
\
(2.44)\
\
\
Given an arbitrary _a_, the model solution is defined as\
\
\\begin{aligned} \\psi \_{cusp}(t) := -(n+1) \\log (-t )+n\\log (n+1) -a, \\;\\, \\omega \_{cusp} := i\\partial \\overline{\\partial}\\psi \_{cusp}. \\end{aligned}\
\
(2.45)\
\
\
### Lemma 2.11\
\
Adding a constant to _ψ_ _cusp_, i.e., choosing the constant _a_ in ( [2.45](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ48)) correctly, one has\
\
e^{-\\psi \_{cusp}}\\omega \_{cusp}^{n}=i^{n^{2}}\\Omega \_{\\mathcal {C}} \\wedge \\overline{\\Omega}\_{\\mathcal {C}}.\
\
(2.46)\
\
\
### Proof\
\
It follows from the symmetry of \\omega \_{cusp},\\Omega \_{\\mathcal {C}} and from the Kähler-Einstein condition that\
\
\\begin{aligned} g(t):= \\frac{e^{-\\psi \_{cusp}}\\omega \_{cusp}^{n}}{i^{n^{2}}\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}} \\end{aligned}\
\
(2.47)\
\
\
is a pluriharmonic function depending only on _t_. Now\
\
\\begin{aligned} i\\partial \\overline {\\partial }g(t)=g'(t)i\\partial \\overline {\\partial }t+ig''(t)\\partial t\\wedge \\overline{\\partial} t=0. \\end{aligned}\
\
(2.48)\
\
\
So _g_( _t_) must be a constant and ( [2.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ49)) can be achieved by adding a constant to _ψ_ _cusp_. □\
\
To compare _ψ_ _KE_,0 to _ψ_ _cusp_ in our main example, it is helpful to rescale the holomorphic volume forms Ω_σ_ by a constant so that Ω0 becomes asymptotic to \\Psi \_{0}^{\*}\\Omega \_{\\mathcal{C}} at the singularity p \\in \\mathcal{X}\_{0}.\
\
### Lemma 2.12\
\
For fixed Ω0 and \\Omega \_{\\mathcal {C}}, there is a nonzero complex constant _C_ such that\
\
(\\Psi \_{0}^{-1})^{\*}(\\Omega \_{0}\\wedge \\overline{\\Omega}\_{0})= \|C\|^{2} e^{-v} {\\Omega \_{\\mathcal {C}}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}},\
\
(2.49)\
\
\
where _v_ is a pluriharmonic function satisfying for all _ε_ >0 and _j_ ⩾1 and for _t_ →−∞ that\
\
\|v\|=O(e^{\\frac{t}{2}}),\\;\\,\|\\nabla \_{\\omega \_{cusp}}^{j} v\|\_{\\omega \_{cusp}}=O\_{ \\varepsilon ,j}(e^{\\frac{(1-\\varepsilon )t}{2}}).\
\
(2.50)\
\
\
### Proof\
\
The function H:=\[(\\Psi \_{0}^{-1})^{\*}\\Omega \_{0}\]/\\Omega \_{\\mathcal {C}} is a nowhere vanishing holomorphic function on _U_ ∖{0} for some small open neighborhood _U_ of the singularity 0∈ _TY_ 0. Since this is a normal isolated surface singularity in \\mathbb{C}^{3}, the Hartogs principle \[ [Rup08](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR30 " 					Ruppenthal, J.: A                                                                               $\overline{\partial}$                 -theoretical proof of Hartogs’ extension theorem on Stein spaces with isolated singularities. J. Geom. Anal. 18, 1127–1132 (2008) 				"), Thm 1.1\] says that _H_ extends to a holomorphic function on _U_. We must have that _H_(0)≠0 because otherwise lim_z_ →01/ _H_( _z_)=∞, contradicting the Hartogs principle for 1/ _H_. Let _C_:= _H_(0). Then ( [2.49](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ52)) holds with _v_( _z_):=log\| _H_(0)/ _H_( _z_)\|2, which is obviously pluriharmonic and obviously satisfies \| _v_( _z_)\|= _O_(\| _z_ \|)= _O_( _e_ _t_/2) as \| _z_ \|→0 resp. _t_ →−∞.\
\
Now we further estimate \|\\nabla \_{\\omega \_{cusp}}^{j} v\|\_{\\omega \_{cusp}} for all _j_ ⩾1\. Since _v_ is in particular harmonic with respect to _ω_ _cusp_ and since _ω_ _cusp_ is a hyperbolic metric for _n_ =2, these derivatives can be estimated using Schauder theory on the universal covers of _ω_ _cusp_-geodesic balls of some fixed radius _r_ 0∈(0,1\]. Coordinates on these local universal covers that make _ω_ _cusp_ uniformly smoothly bounded can be found e.g. in \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), proof of Lemma 3.5\]. The _ε_-loss in ( [2.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ53)) is due to the fact that the function _t_ (which coincides with −1/ _x_ in the notation of \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\]) varies by a factor of 1+ _O_( _r_ 0) over any _ω_ _cusp_-ball of radius _r_ 0≪1. □\
\
By a common rescaling of the forms Ω_σ_, which was our only freedom in choosing these forms, we can now arrange that _C_ =1 in ( [2.49](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ52)), i.e., that Ω0 is asymptotic to \\Psi \_{0}^{\*}\\Omega \_{\\mathcal{C}} near the singularity p \\in \\mathcal{X}\_{0}. According to Lemma [2.10](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar15), this leads to an additive normalization of _ψ_ _KE_,0 such that ( [2.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ38)) holds, and this equation then matches the equation ( [2.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ49)) satisfied by _ψ_ _cusp_ to leading order at the singularity.\
\
We require one additional technical lemma before stating our final result.\
\
### Lemma 2.13\
\
Let _U_ be a neighborhood of the singularity _p_ =(0,0,0) in _TY_ 0. Let _φ_ be a function on _U_ ∖{ _p_} satisfying i\\partial \\overline {\\partial }\\varphi =0 and \| _φ_ \|= _o_(−log\| _z_ \|)= _o_(− _t_) as \| _z_ \|→0 resp. _t_ →−∞. Then _φ_ extends continuously as a PSH function on _U_. Moreover, _φ_ is the real part of a holomorphic function near the origin of \\mathbb{C}^{3}, so, after subtracting a constant, \| _φ_ \|= _O_(\| _z_ \|)= _O_( _e_ _t_/2) as \| _z_ \|→0 resp. _t_ →−∞.\
\
### Proof\
\
Consider the resolution of singularities \\pi :\\hat{L} \\to TY\_{0} from ( [2.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ10)). The exceptional divisor is an elliptic curve _E_ and \\hat{L} is the total space of a negative holomorphic line bundle _L_ over _E_. For any point _q_ ∈ _E_, there is a local holomorphic trivialization of the line bundle \\hat{L}\|\_{V}\\cong V\\times \\mathbb{C} for some neighborhood _V_ ∋ _q_. Let _w_ 1 be the coordinate of _V_ and _w_ 2 be the coordinate of \\mathbb{C}. Then by assumption, _φ_ restricted to any fiber of _L_ is a smooth harmonic function on the punctured disk Δ∗ with a sub-logarithmic pole at 0. Hence for each fixed _w_ 1, _φ_ can be extended continuously across 0. So for fixed _w_ 1, _φ_ is the real part of a holomorphic function on Δ. By the mean value theorem,\
\
![](https://media.springernature.com/lw213/springer-static/image/art%3A10.1007%2Fs00039-025-00708-y/MediaObjects/39_2025_708_Equ54_HTML.png)\
\
(2.51)\
\
\
where _γ_ is a fixed circle centered at 0. Taking i\\partial \\overline {\\partial } with respect to the variable _w_ 1, we have that _φ_( _w_ 1,0) is a harmonic function of _w_ 1. Notice that _E_ is compact, so _φ_( _w_ 1,0) is a constant. Hence _φ_ can be extended continuously across \\mathcal{X}\_{0}^{sing} as a PSH function on \\mathcal{X}\_{0}.\
\
Now we show that _φ_ is the real part of a holomorphic function. Note that because the line bundle \\hat{L} is homotopy equivalent to its zero section _E_, the de Rham cohomology H^{1}(\\hat{L},\\mathbb{R}) is naturally isomorphic to H^{1}(E,\\mathbb{R}). Since i\\partial \\overline {\\partial }\\pi ^{\*}\\varphi =0, _d_ _c_ _π_ ∗ _φ_ is a closed real 1-form. So we have\
\
\\begin{aligned} d^{c}\\pi ^{\*}\\varphi =dg+a\\alpha +b\\beta , \\end{aligned}\
\
(2.52)\
\
\
where _a_, _b_ are constants, _g_ is a function on an open neighborhood of the zero section of \\hat{L} and _α_, _β_ are closed 1-forms on _E_ generating H^{1}(E,\\mathbb{R}). Let _γ_ _α_, _γ_ _β_ be loops in _E_ whose homology classes are Poincaré dual to _α_, _β_. Note that _φ_ is constant on _E_ and _dg_ is exact, so the integrals of the 1-form _d_ _c_ _π_ ∗ _φ_ − _dg_ along the loops _γ_ _α_, _γ_ _β_ are zero. So _a_, _b_ are zero. So _f_:= _π_ ∗ _φ_ − _ig_ is a holomorphic function with real part _π_ ∗ _φ_, necessarily constant along the zero section _E_. After pushing down to the singularity, we can locally extend _f_ to a holomorphic function on an open set of \\mathbb{C}^{3}. By subtracting a constant, we may assume that _f_( _p_)=0\. By Taylor expansion, we deduce that _f_ = _O_(\| _z_ \|). □\
\
We are now able to prove the following precise asymptotic comparison of _ψ_ _KE_,0 and _ψ_ _cusp_. Modulo the above lemmas this is the statement of \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), Main Theorem\], whose proof relies on an earlier partial result from \[ [DFS23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR10 " 					Datar, V., Fu, X., Song, J.: Kähler-Einstein metric near an isolated log canonical singularity. J. Reine Angew. Math. 797, 79–116 (2023) 				"), Thm 1.4\]. The results of \[ [DFS23](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR10 " 					Datar, V., Fu, X., Song, J.: Kähler-Einstein metric near an isolated log canonical singularity. J. Reine Angew. Math. 797, 79–116 (2023) 				"), [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\] can be generalized to all dimensions _n_ ⩾2 assuming that the polarized Calabi-Yau ( _n_ −1)-fold ( _L_′, _h_′)→( _E_, _ω_ _E_) in the above discussion of _ψ_ _cusp_ is flat.\
\
### Proposition 2.14\
\
Let Ψ_σ_ be the local holomorphic isomorphism defined in equation ( [2.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ12)). Then\
\
\\begin{aligned} (\\Psi ^{-1}\_{0})^{\*}\\psi \_{KE,0}-\\psi \_{cusp}=u+v, \\end{aligned}\
\
(2.53)\
\
\
where for some constants \\mathfrak{s} \\in \\mathbb{R}, \\delta \_{0} \\in \\mathbb{R}^{+}, for all _j_ ⩾0 and for _t_ →−∞,\
\
\\left \|\\nabla \_{\\omega \_{cusp}}^{j}\\left (u+3 \\log \\left (1- \\frac{\\mathfrak{s}}{t}\\right )\\right )\\right \|\_{\\omega \_{cusp}}= O\_{j}(e^{- \\delta \_{0}\\sqrt {-t}}),\
\
(2.54)\
\
\
and where _v_ is a pluriharmonic function satisfying for all _ε_ >0 and _j_ ⩾1 and for _t_ →−∞ that\
\
\|v\|=O(e^{\\frac{t}{2}}),\\;\\,\|\\nabla \_{\\omega \_{cusp}}^{j} v\|\_{\\omega \_{cusp}}=O\_{ \\varepsilon ,j}(e^{\\frac{(1-\\varepsilon )t}{2}}).\
\
(2.55)\
\
\
### Remark 2.15\
\
Composing both sides of ( [2.53](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ56)) with the automorphism _scale_ _λ_( _z_)= _λz_ of \\mathbb{C}^{3} yields a new decomposition (\\Psi \_{0}^{-1} \\circ scale\_{\\lambda})^{\*}\\psi \_{KE,0} - \\psi \_{cusp} = u\_{\\lambda }+ v\_{\\lambda}, where _u_ _λ_, _v_ _λ_ satisfy the same properties as before except that the constant \\mathfrak{s} in ( [2.54](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ57)) gets replaced by \\mathfrak{s}-\\log \\lambda . Thus, by choosing \\lambda = e^{\\mathfrak{s}} we obtain that _u_ _λ_ is purely exponentially decaying and contains no powers of 1/ _t_ in its expansion as _t_ →−∞. This was already pointed out in the introduction to our previous paper \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\].\
\
This suggests making the following modification to our setup: For \\lambda = e^{\\mathfrak{s}}, replace \\Psi \_{\\sigma}: \\mathcal{Y}\_{\\sigma }\\to TY\_{\\sigma} by {scale}\_{\\lambda ^{-1}} \\circ \\Psi \_{\\sigma}: \\mathcal{Y}\_{\\sigma } \\to TY\_{\\lambda ^{-3}\\sigma} for all _σ_ ∈Δ. (The domains of these maps are actually just small open neighborhoods of the origin in \\mathbb{C}^{3} intersected with \\mathcal{Y}\_{\\sigma}.) In this way, we can assume without loss of generality that \\mathfrak{s} = 0 in ( [2.54](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ57)), i.e., that _u_ is exponentially decaying. Note that, so far, we have never actually used the map Ψ_σ_ with _σ_ ≠0 except in Lemma [2.7](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar10). The statement and proof of that lemma remain unchanged if we also replace Φ_σ_ by \\Phi \_{\\lambda ^{-3}\\sigma}, which again takes values in TY\_{\\lambda ^{-3}\\sigma}.\
\
However, Ψ_σ_,Φ_σ_ will also be used as gluing maps in Sect. [3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec13). The replacements \\Psi \_{\\sigma }\\leadsto {scale}\_{\\lambda ^{-1}}\\circ \\Psi \_{\\sigma} and \\Phi \_{\\sigma }\\leadsto \\Phi \_{\\lambda ^{-3}\\sigma} do not worsen any of the estimates in Sect. [3](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec13) (or later), but being able to assume that \\mathfrak{s} = 0 in ( [2.54](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ57)) drastically reduces the gluing error. To exploit this improvement without having to introduce even more notation, we will from now on simply assume that \\mathfrak{s} = 0 and _λ_ =1.\
\
### Proof of Proposition [2.14](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar23)\
\
First of all, if we define\
\
\\begin{aligned} u:=\\log \\left ( \\frac{(\\Psi \_{0}^{-1})^{\*}\\omega ^{2}\_{KE,0}}{\\omega ^{2}\_{cusp}} \\right ), \\end{aligned}\
\
(2.56)\
\
\
then by the Kähler-Einstein equation, we have that\
\
\\begin{aligned} (\\Psi \_{0}^{-1})^{\*}\\omega \_{KE,0}-\\omega \_{cusp}=i\\partial \\overline {\\partial }u. \\end{aligned}\
\
(2.57)\
\
\
By \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), Main Theorem\], there exist \\mathfrak{s} \\in \\mathbb{R}, \\delta \_{0} \\in \\mathbb{R}^{+} such that for all _j_ ⩾0 and for _t_ →−∞,\
\
\\begin{aligned} \\left \|\\nabla \_{\\omega \_{cusp}}^{j}\\left (u +3 \\log \\left (1- \\frac{\\mathfrak{s}}{t}\\right )\\right )\\right \|\_{\\omega \_{cusp}} = O\_{j}(e^{- \\delta \_{0}\\sqrt {-t}}). \\end{aligned}\
\
(2.58)\
\
\
Here we remark again that the function −1/ _t_ in this paper is the same as the function _x_ used in \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\]. So at the Kähler potential level, we have that\
\
(\\Psi \_{0}^{-1})^{\*}\\psi \_{KE,0}-\\psi \_{cusp}=\\varphi +u,\
\
(2.59)\
\
\
where _φ_ is a pluriharmonic function. By the estimate ( [2.34](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ37)) of _ψ_ _KE_,0 near the singularity and by the definition of _ψ_ _cusp_, we have \| _φ_ \|= _O_(log(− _t_))= _o_(− _t_). Thus, by Lemma [2.13](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar21), _φ_ = **c** + **v**, where **c** is a constant and **v** is a pluriharmonic function satisfying \| **v** \|= _O_(\| _z_ \|)= _O_( _e_ _t_/2).\
\
It is now easy to see that the constant **c** is zero. Indeed,\
\
e^{-\\psi \_{cusp}}\\omega \_{cusp}^{2}=\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}=e^{v}(\\Psi \_{0}^{-1})^{\*}(\\Omega \_{0} \\wedge \\overline{\\Omega}\_{0})=e^{v}(\\Psi \_{0}^{-1})^{\*}(e^{-\\psi \_{KE,0}} \\omega ^{2}\_{KE,0})\
\
(2.60)\
\
\
by ( [2.46](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ49)), by ( [2.49](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ52)) with our chosen normalization _C_ =1, and by ( [2.35](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ38)). Therefore,\
\
{\\mathbf{c}+u+\\mathbf{v}}=(\\Psi \_{0}^{-1})^{\*}\\psi \_{KE,0}-\\psi \_{cusp} = \\log \\left ( \\frac{(\\Psi \_{0}^{-1})^{\*}\\omega ^{2}\_{KE,0}}{\\omega ^{2}\_{cusp}} \\right ) + v = u + O(e^{\\frac{t}{2}}).\
\
(2.61)\
\
\
Since **v** goes to zero at the singularity, we get **c** =0\. Moreover, **v** = _v_, so ( [2.50](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ53)) implies ( [2.55](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ58)). □\
\
### 2.3 Tian-Yau metrics\
\
In this subsection we review the Tian-Yau construction \[ [TY90](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR38 " 					Tian, G., Yau, S.-T.: Complete Kähler manifolds with zero Ricci curvature, I. J. Amer. Math. Soc. 3, 579–609 (1990) 				"), Thm 4.2\] of a complete Ricci-flat Kähler metric on the complement of a smooth anti-canonical divisor in a smooth Fano manifold. Expositions of this construction can be found in \[ [H+22](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR18 " 					Hein, H.-J., Sun, S., Viaclovsky, J., Zhang, R.: Nilpotent structures and collapsing Ricci-flat metrics on the K3 surface. J. Amer. Math. Soc. 35, 123–209 (2022) 				"), Sect. 3\] and \[ [H+21](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR19 " 					Hein, H.-J., Sun, S., Viaclovsky, J., Zhang, R.: Asymptotically Calabi metrics and weak Fano manifolds. Geom. Topol. (2021, in press). arXiv:                   2111.09287                                    "), Sect. 3\]. We will borrow freely from these two references and show how to match their notation to ours.\
\
As in our discussion of cusp metrics above, let _E_ be an ( _n_ −1)-dimensional compact Kähler manifold with trivial canonical bundle _K_ _E_ and let _L_′→ _E_ be an ample line bundle, the dual of a negative line bundle _L_ → _E_. We fix a nowhere vanishing holomorphic ( _n_ −1)-form Ω_E_ on _E_ with\
\
\\int \_{E} i^{(n-1)^{2}}\\Omega \_{E}\\wedge \\overline{\\Omega}\_{E}=(2\\pi c\_{1}(L'))^{n-1}.\
\
(2.62)\
\
\
By Yau’s resolution of the Calabi conjecture \[ [Yau78](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR40 " 					Yau, S.-T.: On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I. Comm. Pure Appl. Math. 31, 339–411 (1978) 				")\], there exists a unique Ricci-flat Kähler metric _ω_ _E_ on _E_ representing the Kähler class 2\\pi c\_{1}(L') \\in H^{1,1}(E,\\mathbb{R}) and satisfying the equation\
\
\\omega \_{E}^{n-1}=i^{(n-1)^{2}} \\Omega \_{E}\\wedge \\overline{\\Omega}\_{E}.\
\
(2.63)\
\
\
Up to scaling, there exists a unique Hermitian metric _h_′ on _L_′ whose curvature form is _ω_ _E_, and _h_′ is the dual of a negatively curved Hermitian metric _h_ on _L_. We now fix a choice of _h_′. Then the _Calabi model space_ is the subset \\mathcal {C} of the total space of _L_′ consisting of all elements _ξ_ with 0<\| _ξ_ \|_h_′<1, endowed with a nowhere vanishing holomorphic volume form \\Omega \_{\\mathcal {C}} and a Ricci-flat Kähler metric \\omega \_{\\mathcal {C}} which is incomplete as \| _ξ_ \|_h_′→1 and complete as \| _ξ_ \|_h_′→0\. Again as in our discussion of cusp metrics above, the holomorphic volume form \\Omega \_{\\mathcal {C}} is uniquely determined by the equation\
\
Z \\lrcorner \ \\Omega \_{\\mathcal {C}}=p^{\*}\\Omega \_{E},\
\
(2.64)\
\
\
where p : \\mathcal {C} \\to E is the bundle projection and _Z_ is the holomorphic vector field generating the natural \\mathbb{C}^{\*}-action on the fibers of _p_ (i.e., the one coming from the line bundle structure of _L_′). The metric \\omega \_{\\mathcal {C}} is given by the Calabi ansatz\
\
\\omega \_{\\mathcal {C}}:=i\\partial \\overline {\\partial }\\psi \_{\\mathcal {C}}, \\;\\, \\psi \_{ \\mathcal{C}} := \\frac{n}{n+1}(-{\\log \|\\xi \|\_{h'}^{2}})^{\\frac{n+1}{n}},\
\
(2.65)\
\
\
and satisfies the Monge-Ampère equation\
\
\\omega \_{\\mathcal {C}}^{n}=i^{n^{2}} \\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}},\
\
(2.66)\
\
\
hence is Ricci-flat. Also define the momentum coordinate\
\
\\mathbf{z} := (-{\\log \|\\xi \|^{2}\_{h'}})^{\\frac{1}{n}}.\
\
(2.67)\
\
\
Then the \\omega \_{\\mathcal {C}}-distance to a fixed point in \\mathcal{C} is uniformly comparable to **z**( _n_ +1)/2 for _z_ ≫1.\
\
We now explain the Tian-Yau construction \[ [TY90](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR38 " 					Tian, G., Yau, S.-T.: Complete Kähler manifolds with zero Ricci curvature, I. J. Amer. Math. Soc. 3, 579–609 (1990) 				")\] of complete Ricci-flat Kähler metrics asymptotic to a Calabi ansatz at infinity. Let _M_ be a smooth Fano manifold of complex dimension _n_, let E\\in \|K\_{M}^{-1}\| be a smooth divisor, and let _L_′ denote the holomorphic normal bundle to _E_ in _M_. Then _E_ has a trivial canonical bundle and _L_′ is ample, so in particular we can choose a holomorphic volume form Ω_E_ on _E_ which satisfies ( [2.62](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ65)). We fix a defining section _S_ of _E_, so that _S_ −1 can be viewed as a holomorphic _n_-form Ω_X_ on _X_ = _M_ ∖ _E_ with a simple pole along _E_. After scaling _S_ by a nonzero complex constant, we may assume that Ω_E_ is the residue of Ω_X_ along _E_. (In practice this means that Ω_X_ is asymptotic to \\Omega \_{\\mathcal{C}} with respect to a suitable diffeomorphism Φ between tubular neighborhoods of _E_ in _M_ and of the zero section in _L_′.) Lastly, we fix a Hermitian metric _h_ _M_ on K\_{M}^{-1} whose curvature form is strictly positive on _M_ and restricts to the unique Ricci-flat Kähler form _ω_ _E_∈2 _πc_ 1( _L_′) on _E_. Then\
\
\\omega \_{X}^{\\circ }:= \\frac{n}{n+1}i\\partial \\overline {\\partial }(-{\\log \|S\|\_{h\_{M}}^{2}})^{ \\frac{n+1}{n}}\
\
(2.68)\
\
\
defines a Kähler form on a neighborhood of infinity in _X_. This \\omega \_{X}^{\\circ} is then complete towards _E_ and is asymptotic to \\omega \_{\\mathcal{C}}, where the Hermitian metric _h_′ used in ( [2.65](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ68)) is the restriction of _h_ _M_ to K\_{M}^{-1}\|\_{E} = L'. In particular, \\omega \_{X}^{\\circ} is asymptotically Ricci-flat. Moreover, since _X_ is an affine variety, it is reasonably straightforward to extend \\omega \_{X}^{\\circ} as a globally defined i\\partial \\overline{\\partial}-exact Kähler form on the whole manifold _X_. Then the following is proved in \[ [TY90](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR38 " 					Tian, G., Yau, S.-T.: Complete Kähler manifolds with zero Ricci curvature, I. J. Amer. Math. Soc. 3, 579–609 (1990) 				")\] by solving a Monge-Ampère equation with reference metric \\omega \_{X}^{\\circ}. The exponential decay statement follows from \[ [Hei12](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR16 " 					Hein, H.-J.: Gravitational instantons from rational elliptic surfaces. J. Amer. Math. Soc. 25, 355–393 (2012) 				"), Prop 2.9\].\
\
### Theorem 2.16\
\
_There is a complete Ricci_- _flat Kähler metric_ _ω_ _X_ _on_ _X_ _solving the equation_\
\
\\omega \_{X}^{n}=i^{n^{2}}\\Omega \_{X}\\wedge \\overline{\\Omega}\_{X}.\
\
(2.69)\
\
\
_Moreover_, _there is a unique choice of the scaling factor of_ _h_′ _resp_. _of_ _h_ _M_ _such that_\\omega \_{X} = \\omega \_{X}^{\\circ }+ i\\partial \\overline{\\partial}\\phi , _where for some_ _δ_ 0>0 _and for all_ _k_ ⩾0, _as_ _z_ →∞,\
\
\|\\nabla \_{\\omega \_{\\mathcal{C}}}^{k} (\\phi \\circ \\Phi )\|\_{\\omega \_{ \\mathcal{C}}} = O\_{k}(e^{-\\delta \_{0} \\mathbf{z}^{n/2}}).\
\
(2.70)\
\
\
_Here we have implicitly fixed a smooth identification_ Φ _of_ _M_ _and of the total space of_ _L_′ _near_ _E_.\
\
We will now apply this construction to our space X := TY\_{1} = \\{z\_{1}^{3}+z\_{2}^{3}+z\_{3}^{3}=1\\}, a smooth cubic in \\mathbb{C}^{3}. We can compactify _X_ to _M_, a smooth cubic in \\mathbb{CP}^{3}, by adding an elliptic curve _E_ at infinity. Note that _M_ is an anticanonically embedded del Pezzo surface and L'=-K\_{M}^{-1}\|\_{E} = \\mathcal {O}\_{\\mathbb{CP}^{3}}(1)\|\_{E}. The total space of the dual bundle _L_ resolves the singularity of the cubic cone _TY_ 0 at the origin, and \\mathcal{C} is identified with a neighborhood of infinity in _TY_ 0. Then our diffeomorphism Φ=Φ1 from ( [2.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ19)), ( [2.17](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ20)) plays the role of the smooth identification Φ in Theorem [2.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar26), and **z** 2= _t_ for _t_ >0.\
\
The following lemma records some more detailed estimates from \[ [H+22](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR18 " 					Hein, H.-J., Sun, S., Viaclovsky, J., Zhang, R.: Nilpotent structures and collapsing Ricci-flat metrics on the K3 surface. J. Amer. Math. Soc. 35, 123–209 (2022) 				"), Prop 3.4\] in our setting.\
\
### Lemma 2.17\
\
For all _ε_ >0 and _k_ ⩾0 and for _t_ →+∞,\
\
\|\\nabla \_{g\_{\\mathcal {C}}}^{k}(\\Phi \_{1}^{\*}J\_{TY\_{1}}-J\_{\\mathcal {C}})\|\_{g\_{ \\mathcal {C}}} + \|\\nabla \_{g\_{\\mathcal{C}}}^{k}(\\Phi \_{1}^{\*}\\Omega \_{TY\_{1}}- \\Omega \_{\\mathcal {C}})\|\_{g\_{\\mathcal {C}}} =O\_{\\varepsilon ,k}(e^{-( \\frac{1}{2}-\\varepsilon )t}).\
\
(2.71)\
\
\
Moreover, there exists a global potential \\psi \_{TY\_{1}} of \\omega \_{TY\_{1}}, i.e., \\omega \_{TY\_{1}} = i\\partial \\overline{\\partial}\\psi \_{TY\_{1}} globally on _TY_ 1, such that there exists _δ_ 0>0 such that for all _k_ ⩾0 and for _t_ →+∞,\
\
\\begin{aligned} \|\\nabla \_{g\_{\\mathcal {C}}}^{k}(\\Phi \_{1}^{\*}\\psi \_{TY\_{1}}-\\psi \_{\\mathcal {C}})\|\_{g\_{ \\mathcal {C}}} + \|\\nabla \_{g\_{\\mathcal {C}}}^{k}(\\Phi \_{1}^{\*}\\omega \_{TY\_{1}}- \\omega \_{\\mathcal {C}})\|\_{g\_{\\mathcal {C}}} =O\_{k}(e^{-\\delta \_{0} \\sqrt{t}}). \\end{aligned}\
\
(2.72)\
\
\
In our gluing construction, we will be working with a scaled copy of \\omega \_{TY\_{1}}, pulled back from _TY_ 1 to _TY_ _σ_ via the maps of Definition [2.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar6). Let us first recall these maps for convenience:\
\
\\begin{aligned} \\Phi : TY\_{0}\\setminus \\overline{B}\_{R} \\to TY\_{1}, \\;\\, \\Phi (z) = z + O(\|z\|^{-2})\\;\\,\\text{as}\\;\\;\|z\|\\to \\infty , \\\ m\_{\\sigma}': TY\_{0} \\to TY\_{0}, \\;\\, m\_{\\sigma}'(z) = \\sigma ^{-1/3}z, \\\ m\_{\\sigma}: TY\_{\\sigma }\\to TY\_{1}, \\;\\,m\_{\\sigma}(z) = \\sigma ^{-1/3}z, \\\ \\Phi \_{\\sigma}: TY\_{0} \\setminus \\overline{B}\_{\|\\sigma \|^{1/3}R}\\to TY\_{ \\sigma}, \\;\\, \\Phi \_{\\sigma }= m^{-1}\_{\\sigma }\\circ \\Phi \\circ m'\_{ \\sigma}. \\end{aligned}\
\
(2.73)\
\
\
Next, we introduce the following pullback objects:\
\
\\begin{aligned} \\Omega \_{TY\_{\\sigma}} := m\_{\\sigma}^{\*}\\Omega \_{TY\_{1}}, \\;\\,\\omega \_{TY\_{\\sigma}} := m\_{\\sigma}^{\*}\\omega \_{TY\_{1}},\\;\\,\\psi \_{TY\_{ \\sigma}} := m\_{\\sigma}^{\*}\\psi \_{TY\_{1}} \\;\\,\\text{and}\\;\\, g\_{\\mathcal {C}, \\sigma}:=(m'\_{\\sigma})^{\*}g\_{\\mathcal {C}}. \\end{aligned}\
\
(2.74)\
\
\
Then Lemma [2.17](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar27) implies the following estimates, including an additional rescaling. The strange form of the scaling factor, \| _b_ \|1/2 with _b_ <0, is due to some conventions in Sect. [2.4](https://link.springer.com/article/10.1007/s00039-025-00708-y#Sec9).\
\
### Lemma 2.18\
\
For all _b_ <0 and _σ_ ∈Δ∗ the following estimates hold with all of the implied constants independent of _b_ and _σ_. First, for all _ε_ >0 and _k_ ⩾0 and for t - \\frac{2}{3}\\log \|\\sigma \|\\to +\\infty ,\
\
\\begin{aligned} \|\\nabla \_{\|b\|^{\\frac{1}{2}}g\_{\\mathcal {C},\\sigma}}^{k}( \\Phi ^{\*}\_{\\sigma }J\_{TY\_{\\sigma}}-J\_{\\mathcal {C}})\|\_{\|b\|^{\\frac{1}{2}}g\_{ \\mathcal {C},\\sigma}} &=O\_{\\varepsilon ,k}(\|b\|^{-\\frac{k}{4}}e^{-( \\frac{1}{2}-\\varepsilon )(t-\\frac{2}{3}\\log \|\\sigma \|)}), \\\ \|\\nabla \_{\|b\|^{\\frac{1}{2}}g\_{\\mathcal{C},\\sigma}}^{k}(\\Phi \_{\\sigma}^{\*} \\Omega \_{TY\_{\\sigma}}-\\Omega \_{\\mathcal {C}})\|\_{\|b\|^{\\frac{1}{2}}g\_{ \\mathcal {C}, \\sigma}}&=O\_{\\varepsilon ,k}(\|b\|^{-\\frac{k}{4}}e^{-( \\frac{1}{2}-\\varepsilon )(t-\\frac{2}{3}\\log \|\\sigma \|)}). \\end{aligned}\
\
(2.75)\
\
\
Moreover, there exists _δ_ 0>0 such that for all _k_ ⩾0 and for t - \\frac{2}{3}\\log \|\\sigma \|\\to +\\infty ,\
\
\\begin{aligned} \|\\nabla \_{\|b\|^{\\frac{1}{2}}g\_{\\mathcal {C},\\sigma}}^{k}(\|b\|^{ \\frac{1}{2}}\\Phi \_{\\sigma}^{\*}\\psi \_{TY\_{\\sigma}}-\|b\|^{\\frac{1}{2}} \\psi \_{\\mathcal {C},\\sigma})\|\_{{\|b\|^{\\frac{1}{2}}g\_{\\mathcal {C},\\sigma}}}&=O\_{k}(\|b\|^{ \\frac{2-k}{4}}e^{-{\\delta}\_{0} (t-\\frac{2}{3}\\log \|\\sigma \|)^{1/2}}), \\\ \|\\nabla \_{\|b\|^{\\frac{1}{2}}g\_{\\mathcal {C},\\sigma}}^{k}(\|b\|^{ \\frac{1}{2}}\\Phi \_{\\sigma}^{\*}\\omega \_{TY\_{\\sigma}}-\|b\|^{\\frac{1}{2}} \\omega \_{\\mathcal {C},\\sigma})\|\_{{\|b\|^{\\frac{1}{2}}g\_{\\mathcal {C},\\sigma}}}&=O\_{k}(\|b\|^{- \\frac{k}{4}}e^{-{\\delta}\_{0} (t-\\frac{2}{3}\\log \|\\sigma \|)^{1/2}}). \\end{aligned}\
\
(2.76)\
\
\
### Proof\
\
This is trivial except for the following two observations. First, t - \\frac{2}{3}\\log \|\\sigma \| = (m\_{\\sigma}')^{\*}t. Second, J\_{\\mathcal{C},\\sigma} := (m\_{\\sigma}')^{\*}J\_{\\mathcal{C}} and \\Omega \_{\\mathcal{C},\\sigma} := (m\_{\\sigma}')^{\*}\\Omega \_{ \\mathcal{C}} are actually equal to J\_{\\mathcal{C}} resp. \\Omega \_{\\mathcal{C}}. □\
\
Lastly, we need to compare the holomorphic volume form \\Omega \_{TY\_{\\sigma}} on _TY_ _σ_ to the holomorphic volume form Ω_σ_ on \\mathcal{Y}\_{\\sigma }\\subset \\mathcal{X}\_{\\sigma} on a uniform neighborhood of the origin in \\mathbb{C}^{3}.\
\
### Lemma 2.19\
\
Recall the local biholomorphism \\Psi \_{\\sigma}: \\mathcal{Y}\_{\\sigma }\\to TY\_{\\sigma} from ( [2.9](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ12)). Then for all _σ_ ∈Δ∗,\
\
(\\Psi \_{\\sigma}^{-1})^{\*}\\Omega \_{\\sigma }= (1 + O(\|z\|))\\Omega \_{TY\_{ \\sigma}}\
\
(2.77)\
\
\
as \| _z_ \|→0, and the implied constant is independent of _σ_.\
\
### Proof\
\
There exists an _ε_ >0 such that for every fixed _σ_ ∈Δ∗, the function H\_{\\sigma }:= \[(\\Psi \_{\\sigma}^{-1})^{\*}\\Omega \_{\\sigma}\]/\\Omega \_{TY\_{ \\sigma}} is holomorphic on _TY_ _σ_∩ _B_ _ε_(0). Since all data depend holomorphically on _σ_, it follows that\
\
H: B\_{\\varepsilon}(0)\\setminus TY\_{0} \\to \\mathbb{C}, \\;\\,z \\mapsto H\_{ \\sigma}(z)\\;\\,\\text{with}\\;\\,\\sigma = z\_{1}^{3} + z\_{2}^{3} + z\_{3}^{3} \\neq 0,\
\
(2.78)\
\
\
is holomorphic.\
\
### Claim 2.20\
\
_H_ extends holomorphically to _B_ _ε_(0).\
\
### Proof of Claim [2.20](https://link.springer.com/article/10.1007/s00039-025-00708-y\#FPar32)\
\
It is enough to show that _H_ extends holomorphically to _B_ _ε_(0)∖{0} because then the claim follows from Hartogs’ theorem. Obviously the numerator, (\\Psi \_{\\sigma}^{-1})^{\*}\\Omega \_{\\sigma}, is holomorphic even at the points of _TY_ 0∖{0}. For the denominator, \\Omega \_{TY\_{\\sigma}}, cover \\mathbb{C}^{3} \\setminus \\{0\\} by the open sets { _z_ _i_≠0} ( _i_ =1,2,3). By symmetry we only need to consider the case _i_ =1\. By adjunction, there exists \\gamma \\in \\mathbb{C}^{\*} such that \\Omega \_{TY\_{1}} is the restriction to the tangent bundle of _TY_ 1 of the 2-form \\gamma (dz\_{2} \\wedge dz\_{3})/z\_{1}^{2} on { _z_ 1≠0}. The latter is invariant under _m_ _σ_. Thus, \\Omega \_{TY\_{\\sigma}} is given by the same formula, so it extends as a holomorphic and nowhere vanishing section of the relative canonical bundle across _TY_ 0∖{0}. □\
\
It remains to show that _H_(0)=1. To see that this is true, we approach the origin along a sequence of points in _TY_ 0∖{0}. Along this sequence, \[(\\Psi \_{0}^{-1})^{\*}\\Omega \_{0}\]/\\Omega \_{\\mathcal{C}} \\to 1 by the normalization chosen after the proof of Lemma [2.12](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar19), so we need to show that \\Omega \_{TY\_{0}}/\\Omega \_{\\mathcal{C}} \\to 1 as well. In fact, \\Omega \_{TY\_{0}} = \\Omega \_{\\mathcal{C}} on _TY_ 0∖{0}. The reason is that these forms are scale-invariant on the cone _TY_ 0∖{0} and have the same residue at the infinity divisor _E_; compare the general construction of Ω_X_ before Theorem [2.16](https://link.springer.com/article/10.1007/s00039-025-00708-y#FPar26). □\
\
### 2.4 A new neck region between a Tian-Yau end and a hyperbolic cusp\
\
We now return to the radial Kähler-Einstein equation ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) on a general _n_-dimensional cusp singularity, which already gave us the asymptotic model _ψ_ _cusp_ for the unique complete Kähler-Einstein potential on the regular part of our 2-dimensional example \\mathcal{X}\_{0}. In general, ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) is equivalent to\
\
\\begin{aligned} \\frac{1}{n+1}(\\psi ')^{n+1} = e^{\\psi +a}+b \\end{aligned}\
\
(2.79)\
\
\
for some constant _b_. Then we have, for any _t_ < _t_ 0,\
\
\\begin{aligned} \\int \_{\\psi (t)}^{\\psi (t\_{0})} (e^{\\xi +a}+b )^{-\\frac{1}{n+1}}d\\xi = (n+1)^{\\frac{1}{n+1}}(t\_{0}-t). \\end{aligned}\
\
(2.80)\
\
\
The case _b_ =0 yields the cusp solution _ψ_ _cusp_. The case _b_ >0 yields solutions that are still defined on an entire negative half-line but are not metrically complete as _t_ →−∞. In \[ [BG14](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR4 " 					Berman, R., Guenancia, H.: Kähler-Einstein metrics on stable varieties and log canonical pairs. Geom. Funct. Anal. 24, 1683–1730 (2014) 				"), Sect. 2\] and \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				"), Ex 2.7\], it was shown that the completions of these metrics may be viewed as Kähler-Einstein edge metrics on the total space of _L_, with conical singularities along the zero section that get pushed off to infinity as _b_ →0 while the diameter of the zero section shrinks to zero. Since we are now considering smoothings rather than resolutions of singularities, it is natural to try to use the case _b_ <0.\
\
We showed in \[ [FHJ24](https://link.springer.com/article/10.1007/s00039-025-00708-y#ref-CR13 " 					Fu, X., Hein, H.-J., Jiang, X.: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps. Calc. Var. Partial Differ. Equ. 63, Article ID 6 (2024) 				")\] that when _b_ <0, there are solutions to ( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)) which correspond to incomplete Kähler-Einstein metrics on { _δ_ −< _h_ ⩽ _δ_ +}, where _δ_ −, _δ_ +>0 are constants that depend on _a_, _b_. In fact, ( [2.41](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ44)) and ( [2.79](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ82)) imply that _e_ _ψ_ + _a_+ _b_ >0\. When _b_ <0, the integral on the left-hand side of ( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)) is bounded and the bound is independent of _t_, _t_ 0. The purpose of this section is to study these solutions in detail. They give rise to “horn metrics” _ω_ _T_ approximating _ω_ _cusp_ as in Fig. [2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Fig2).\
\
**Figure 2**\
\
![Figure 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00039-025-00708-y/MediaObjects/39_2025_708_Fig2_HTML.png)\
\
[Full size image](https://link.springer.com/article/10.1007/s00039-025-00708-y/figures/2)\
\
Cusp metric _ω_ _cusp_, horn metric _ω_ _T_, gluing regions. (Color figure online.)\
\
### Convention 2.21\
\
We will introduce geometric parameters _T_ < _T_ +2 _T_ 0<2 _τ_ <0, and _b_, _T_, _T_ 0, _τ_ will eventually be made to depend on _σ_. The standing assumption is that as _σ_ →0 we have that\
\
\\begin{aligned} T \\to -\\infty , \\;\\, T\_{0} \\to +\\infty , \\;\\, T\_{0}/T \\to 0, \\;\\, \\tau \\to -\\infty , \\;\\, \\tau /T \\to 0, \\;\\, b \\to 0, \\;\\, b\|\\tau \|^{n+1} \\to 0. \\end{aligned}\
\
(2.81)\
\
\
We will be proving many _O_(…) type estimates for various different quantities, and the understanding will always be that the _O_(…) holds as _σ_ →0, so that ( [2.81](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ84)) is in force.\
\
We assume _ψ_ _T_( _t_) is the solution of ( [2.42](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ45)) such that\
\
\\begin{aligned} e^{\\psi \_{T}(T) +a} +b=0,\\quad \\psi \_{T}(\\tau ) = \\psi \_{cusp} (\\tau ). \\end{aligned}\
\
(2.82)\
\
\
Then\
\
\\begin{aligned} \\psi \_{T}(T) = \\log \|b\|-a, \\quad \\psi \_{T}(\\tau ) = -(n+1)\\log ( - \\tau )+n\\log (n+1) -a. \\end{aligned}\
\
(2.83)\
\
\
We note here that with \\omega \_{T} := i\\partial \\overline {\\partial }\\psi \_{T} it holds that\
\
e^{-\\psi \_{T}}\\omega \_{T}^{n}=i^{n^{2}}\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}.\
\
(2.84)\
\
\
Indeed, radial pluriharmonic functions are constant (cf. ( [2.48](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ51))), so there is a constant _C_ _T_ such that\
\
e^{-\\psi \_{T}+C\_{T}}\\omega \_{T}^{n}=i^{n^{2}}\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}.\
\
(2.85)\
\
\
Now by taking _t_ = _τ_ and noting that _ψ_ _T_( _τ_)= _ψ_ _cusp_( _τ_) (cf. ( [2.82](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ85))), one has\
\
i^{n^{2}}\\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}=e^{-\\psi \_{T}( \\tau )+C\_{T}}\\omega \_{T}^{n}=e^{-\\psi \_{cusp}(\\tau )+C\_{T}}\\omega \_{T}^{n}=e^{C\_{T}}i^{n^{2}} \\Omega \_{\\mathcal {C}}\\wedge \\overline{\\Omega}\_{\\mathcal {C}}\
\
(2.86)\
\
\
as before. So indeed _C_ _T_=0.\
\
### Remark 2.22\
\
We show the relationship between _ω_ _T_ and _ω_ _cusp_ in Fig. [2](https://link.springer.com/article/10.1007/s00039-025-00708-y#Fig2). The metric _ω_ _T_ has a horn singularity at _t_ = _T_, which evolves into the cusp singularity as _T_ →−∞. Later we will see that for a fixed _T_, the horn of _ω_ _T_ is asymptotic to a scaled copy of the Calabi model space, which allows us to carry out a gluing construction in the region _t_ ∈\[ _T_ + _T_ 0, _T_ +2 _T_ 0\] that we shaded orange in the figure ( _T_ 0→+∞ but _T_ 0/ _T_ →0). Similarly, in the green region, _t_ ∈\[2 _τ_, _τ_\] ( _τ_ →−∞ but _τ_/ _T_ →0), we can glue _ω_ _T_ with _ω_ _cusp_. We often refer to the region _T_ +2 _T_ 0< _t_ <2 _τ_ as the “new” or “middle” neck.\
\
By ( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)),\
\
\\begin{aligned} \\int \_{\\psi \_{T}(T)}^{\\psi \_{T}(\\tau )} (e^{\\xi +a}+b )^{- \\frac{1}{n+1}}d\\xi = (n+1)^{\\frac{1}{n+1}}(\\tau -T). \\end{aligned}\
\
(2.87)\
\
\
( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)) and ( [2.83](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ86)) show that, by setting _ξ_ = _s_ +log\| _b_ \|− _a_,\
\
\\begin{aligned} \\int \_{0}^{-(n+1)\\log \|\\tau \| -\\log \|b\|+n\\log (n+1) }(e^{s}-1)^{- \\frac{1}{n+1}}ds = (n+1)^{\\frac{1}{n+1}}\|b\|^{\\frac{1}{n+1}}(\\tau -T). \\end{aligned}\
\
(2.88)\
\
\
Hence we obtain the crucial relation between _T_ and _b_:\
\
\\begin{aligned} T =- (n+1)^{-\\frac{1}{n+1}} c(n) \|b\|^{-\\frac{1}{n+1}} +O(\\tau ), \\end{aligned}\
\
(2.89)\
\
\
where\
\
\\begin{aligned} c(n) := \\int \_{0}^{\\infty }(e^{s}-1)^{-\\frac{1}{n+1}} ds. \\end{aligned}\
\
(2.90)\
\
\
We conclude that\
\
\\begin{aligned} \\psi \_{cusp}(T) = \\log \|b\| -(n+1)\\log c(n) +O(\|b\|^{\\frac{1}{n+1}} \\tau ). \\end{aligned}\
\
(2.91)\
\
\
Hence,\
\
\\begin{aligned} \\psi \_{cusp}(T) - \\psi \_{T}(T)= -(n+1)\\log c(n) +a +O(\|b\|^{ \\frac{1}{n+1}}\\tau ), \\end{aligned}\
\
(2.92)\
\
\
which tends to a constant as _σ_ →0 by ( [2.81](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ84)).\
\
#### 2.4.1 Estimates asymptotically close to the cusp (green region)\
\
Similarly to ( [2.80](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ83)), one has\
\
\\begin{aligned} \\int \_{\\psi \_{T}(t)}^{\\psi \_{T}(\\tau )} (e^{\\xi +a}+b )^{- \\frac{1}{n+1}}d\\xi = (n+1)^{\\frac{1}{n+1}}(\\tau -t). \\end{aligned}\
\
(2.93)\
\
\
Substitute _ξ_ = _s_ + _ψ_ _T_( _τ_). By ( [2.83](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ86)),\
\
\\begin{aligned} \\int \_{\\psi \_{T}(t)-\\psi \_{T}(\\tau )}^{0} (e^{s}+(n+1)^{-n} b\|\\tau \|^{n+1})^{- \\frac{1}{n+1}}ds =- (n+1)(1-\\tau ^{-1}t). \\end{aligned}\
\
(2.94)\
\
\
Let _c_ 1>0 be the unique constant such that\
\
\\begin{aligned} \\int \_{-c\_{1}}^{0} (e^{s})^{-\\frac{1}{n+1}}ds = n+1. \\end{aligned}\
\
(2.95)\
\
\
When _t_ =2 _τ_, the right-hand side of ( [2.94](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ97)) equals _n_ +1\. As _b_ <0, we have\
\
\\begin{aligned} (e^{s}+e^{-a} b\|\\tau \|^{n+1})^{-\\frac{1}{n+1}} > (e^{s})^{- \\frac{1}{n+1}}>0. \\end{aligned}\
\
(2.96)\
\
\
By comparing ( [2.94](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ97)) and ( [2.95](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ98)), we derive that _ψ_ _T_(2 _τ_)− _ψ_ _T_( _τ_)>− _c_ 1. By taking _b_ →0− in ( [2.94](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ97)), we see that _ψ_ _T_( _t_)− _ψ_ _T_( _τ_) must decrease to a constant. On the other hand,\
\
\\begin{aligned} \\int \_{\\psi \_{cusp}(2\\tau )-\\psi \_{cusp}(\\tau )}^{0} (e^{s})^{- \\frac{1}{n+1}}ds =n+1. \\end{aligned}\
\
(2.97)\
\
\
By ( [2.81](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ84)) and all the discussions above, _ψ_ _T_(2 _τ_)− _ψ_ _T_( _τ_) converges to _ψ_ _cusp_(2 _τ_)− _ψ_ _cusp_( _τ_). By ( [2.82](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ85)), _ψ_ _T_(2 _τ_)→ _ψ_ _cusp_(2 _τ_). Replacing 2 _τ_ by any constant in (2 _τ_, _τ_), the same argument implies that,\
\
\\begin{aligned} \\psi \_{T}(t) - \\psi \_{cusp}(t) =o(1) \\end{aligned}\
\
(2.98)\
\
\
as _b_ →0− if we fix \\frac{t}{\\tau} as a constant in \[1,2\].\
\
When _t_ = _cτ_ for some constant _c_ ∈\[1,2\], _s_ ⩾ _ψ_ _T_( _t_)− _ψ_ _T_( _τ_)⩾− _c_ 1 in ( [2.94](https://link.springer.com/article/10.1007/s00039-025-00708-y#Equ97)). Using that\
\
\\begin{aligned} \\begin{aligned} \\int \_{\\psi \_{T}(t)-\\psi \_{T}(\\tau )}^{0} (e^{s}+(n+1)^{-n} b\|\\tau \|^{n+1})^{- \\frac{1}{n+1}}ds &= (n+1)(c-1) \\\ &= \\int \_{\\psi \_{cusp}(t)-\\psi \_{cusp}(\\tau )}^{0} (e^{s})^{- \\frac{1}{n+1}}ds, \\end{aligned} \\end{aligned}\
\
(2.99)\
\
\
we derive\
\
\\begin{aligned} \\begin{aligned} &\\int \_{\\psi \_{T}(t)-\\psi \_{T}(\\tau )}^{0}\\left ( (e^{s}+(n+1)^{-n} b\| \\tau \|^{n+1})^{-\\frac{1}{n+1}} - (e^{s})^{-\\frac{1}{n+1}} \\right ) ds \\\ &\\quad= \\int \_{\\psi \_{cusp}(t)-\\psi \_{T}(t)}^{0} (e^{s})^{-\\frac{1}{n+1}}ds, \\end{aligned} \\end{aligned}\
\
(2.100)\
\
\
which shows that, for _t_ ∈\[2 _τ_, _τ_\],\
\
\\begin{aligned} \\psi \_{T}(t) - \\psi \_{cusp}(t) =O(\|b\| \|\\tau \|^{n+1}). \\end{aligned}\
\
(2.101)\
\
\
Let \\rho :=\\sqrt{(n+1)/2} \\log (-t), which is a Busemann function of _ω_ _cusp_. For _t_ ∈\[2 _τ_, _τ_\], _ρ_ varies by an additive constant independent of _b_. Set the normalized Busemann function\
\
\\begin{aligned} \\tilde{\\rho}(t) := \\rho (t) - \\rho (\\tau ) =\\sqrt{\\frac{n+1}{2}} \\log \\left ( \\frac{t}{\\tau} \\right ), \\end{aligned}\
\
(2.102)\
\
\
whose range is I = \[0, \\sqrt{(n+1)/2}\\log 2\] . Regard t \\psi \_{T}', t^{2} \\psi \_{T}'' as functions of \\tilde{\\rho}. As _b_ →0−,\
\
\\begin{aligned} \\begin{aligned} t \\psi \_{T}' &= t (n+1)^{\\frac{1}{n+1}} (e^{\\psi \_{T}+a}+b)^{ \\frac{1}{n+1}} \\\ &= - e^{\\sqrt{\\frac{2}{n+1}}\\tilde{\\rho}} (n+1)^{\\frac{1}{n+1}} (e^{ \\psi \_{T}-\\psi \_{T}(\\tau )+a}+b \|\\tau \|^{n+1} )^{\\frac{1}{n+1}} \\\ &= -(n+1)+O(\|b\| \|\\tau \|^{n+1}), \\end{aligned} \\end{aligned}\
\
(2.103)\
\
\
uniformly for \\tilde{\\rho}\\in I, where we have applied the fact that\
\
\\begin{aligned} \\begin{aligned} \\psi \_{T}-\\psi \_{T}(\\tau )&=\\psi \_{cusp}-\\psi \_{cusp}(\\tau )+O(\|b\|\| \\tau \|^{n+1})\\\ & =-(n+1)\\log \|t/\\tau \| +O(\|b\|\|\\tau \|^{n+1}). \\end{aligned} \\end{aligned}\
\
(2.104)\
\
\
A similar computation shows that\
\
\\begin{aligned} \\begin{aligned} t^{2} \\psi \_{T}'' &= t^{2} e^{\\psi \_{T} +a}(\\psi \_{T}')^{1-n} = e^{ \\psi \_{T} -\\psi \_{cusp} +n\\log (n+1)}(-t\\psi \_{T}')^{1-n} \\\ &= n+1+O(\|b\|\| \\tau \|^{n+1}) \\end{aligned} \\end{aligned}\
\
(2.105)\
\
\
as _b_ →0−. By differentiating\
\
\\begin{aligned} t^{2} \\psi \_{T}'' = (n+1)^{n} e^{\\psi \_{T} -\\psi \_{cusp}}(-t\\psi \_{T}')^{1-n} \\end{aligned}\
\
(2.106)\
\
\
multiple times and multiplying by _t_ each time, we derive the following lemma.\
\
### Lemma 2.23\
\
For _k_ ⩾1,\
\
\\begin{aligned} t^{k}\\psi \_{T}^{(k)}=(-1)^{k}(n+1)(k-1)! + O\_{k}(\|b\|\|\\tau \|^{n+1}) \\end{aligned}\
\
(2.107)\
\
\
on \\{\\tilde{\\rho}\\in I\\} as _b_ →0−. Here (-1)^{k}(n+1)(k-1)! = t^{k}\\psi \_{cusp}^{(k)}.\
\
Introduce a local bundle chart ( _z_ 1,…, _z_ _n_) on the total space of _L_ such that _z_ _n_=0 cuts out the zero section. Write the Hermitian metric as _h_ = _e_ − _φ_\| _z_ _n_\|2, where _φ_ depends only on _z_ 1,…, _z_ _n_ −1. Then for any radial potential _ψ_ = _ψ_( _t_), _t_ =log _h_, the associated (1,1)-form can be written as\
\
\\begin{aligned} \\omega = i\\partial \\overline{\\partial} \\psi = -\\psi ' i\\partial \\overline{\\partial} \\varphi + \\psi '' i(\\partial \\varphi - \\partial \\log z\_{n}) \\wedge (\\overline{\\partial} \\varphi - \\overline{\\partial} \\log \\overline{z}\_{n}). \\end{aligned}\
\
(2.108)\
\
\
We now assume that the Calabi-Yau ( _E_, _ω_ _E_), \\omega \_{E} = -i\\partial \\overline {\\partial }\\varphi , is flat and _z_ 1,…, _z_ _n_ −1 are the standard linear coordinates on the universal cover \\mathbb{C}^{n-1} \\to E. We also write _z_ _α_= _x_ _α_+ _iy_ _α_ for 1⩽ _α_ ⩽ _n_ −1, _θ_ =arg _z_ _n_ and _x_ =−1/ _t_. Then, on the universal cover of \\{2\\tau \\leqslant t\\leqslant \\frac{1}{2}\\tau \\}, we define a new chart via\
\
\\begin{aligned} (\\check{x}\_{\\alpha}, \\check{y}\_{\\alpha}, \\check{x}, \\check{\\theta}) := (\| \\tau \|^{-\\frac{1}{2}} x\_{\\alpha}, \|\\tau \|^{-\\frac{1}{2}} y\_{\\alpha}, \| \\tau \| x, \|\\tau \|^{-1}\\theta ) \\end{aligned}\
\
(2.109)\
\
\