# Actual monopole deficits are moduli energy in the nonlinear slow family

24 September 2026. This companion to the
[nonlinear slow-moduli theorem](20260924_nonlinear_slow_moduli.md)
identifies its actual gauge classes and computes their deficits exactly.
It connects a complete nonlinear metric family to the first-line
curvature-functional theory; the Chern--Weil identity used in the
connection is classical. This is part of the same slow-family result,
not an independent claim of a new general curvature inequality.

## 1. Geometric setting and actual classes

Let \((B,\gamma)\) and \(F\) be closed oriented surfaces of genera at
least two. The base has curvature \(-1\). Let \(h_v\), for \(v\) in a
compact interval, be a smooth path of curvature \(-1\) metrics on the
fixed marked surface \(F\), with horizontal tangent
\[
 k_v=\partial_vh_v,\qquad
 \operatorname{tr}_{h_v}k_v=0,\quad\delta_{h_v}k_v=0,
 \quad\int_F|k_v|_{h_v}^2\,dA_{h_v}=1.                 \tag{1}
\]
This is the positive-speed, fiber \(L^2\)-arclength convention of the
companion, not a claim about a particular convention for a constant
multiple of the Weil--Petersson metric. For a smooth function
\(v:B\to I\), put
\[
 M=B\times F,\qquad G=\gamma+h_{v(x)},\quad
 A_F=\operatorname{Area}(F,h_v),\quad V=\operatorname{Vol}(M,G).
                                                               \tag{2}
\]
The trace condition in (1) gives a **pointwise fixed** area form
\(dA_F\), so \(V=A_F\operatorname{Area}(B,\gamma)\).

**Proposition 1 (exact actual supply).** In the two orientations of
\(M\), there are fixed actual determinant classes \(a_\pm\) whose
harmonic representatives are
\[
 \omega_\pm=dA_B\pm dA_F,\qquad
 H_\pm=-\frac{\omega_\pm}{2\pi},\qquad
 p_\pm=(a_\pm^+)^2=a_\pm^2=A:=2\chi(M),\quad V=2\pi^2A.
                                                               \tag{3}
\]
Here \(+\) on \(a_-^+\) refers to self-duality in the **opposite**
orientation. The forms \(\omega_\pm\) are closed, nondegenerate,
harmonic, and have norm squared two. They need not be parallel.

**Proof.** In the product orientation \(*_GdA_B=dA_F\), so
\(\omega_+\) is self-dual and \(\omega_-\) is anti-self-dual.
Both are closed because the fiber area form is independent of \(v\).
They are therefore harmonic, and \(\omega_-\) is self-dual after
orientation reversal. The compatible almost-complex structures are
\(J_B\oplus J_{h_v}\) and \(J_B\oplus(-J_{h_v})\). Their first
Chern classes are
\[
 a_+=c_1(TB)+c_1(TF),\qquad
 a_-=c_1(TB)-c_1(TF)=-[\omega_-]/(2\pi),
\]
and \(a_+=-[\omega_+]/(2\pi)\), by the curvature \(-1\)
normalizations. The varying complex structures are homotopic to the
constant ones along the parameter interval. In particular these are
integral determinant classes, not arbitrarily chosen real classes.

In either orientation \(b_+=1+2g(B)g(F)>1\). Taubes's symplectic
nonvanishing theorem supplies the actual Spin\(^c\) structures.
Metric-independent nonvanishing and the conformal rescaling argument
give the same structure for every auxiliary positive weight, as in the
[polarized closure proof](../mathematics/current/lebrun_stability_closure.md).
Since \(H_\pm\) already represents the entire class and is self-dual
in its corresponding orientation, there is no unaccounted-for
anti-self-dual projection. Finally \(\tau(M)=0\), and Gauss--Bonnet
on the factors gives (3). \(\square\)

## 2. Exact functional and Ricci-energy identities

Use tensor norms for Ricci and endomorphism norms on two-forms for
Weyl. Set
\[
 E=\operatorname{Ric}_G+G,\quad r=\fint_M|E|^2,\quad
 D(v)=\int_B|dv|^2\,dA_B,\quad \alpha=\frac{D(v)}{4V},
\]
\[
 \mathfrak D_\pm=\frac32\int_M(s^2+12|W^\pm|^2)-72\pi^2p_\pm,
 \qquad q_\pm=\mathfrak D_\pm/V.                       \tag{4}
\]

**Theorem 2 (gauge deficit equals slow energy plus full residual).**
For every metric (2), without a small-amplitude hypothesis,
\[
 \boxed{q_+=q_-=9\alpha+\frac92r
      =\frac9{4V}D(v)+\frac92\fint_M|\operatorname{Ric}_G+G|^2.}
                                                               \tag{5}
\]
The relative Einstein defect is exactly
\[
 \boxed{\mathcal E(G)=\frac{4r-\alpha^2}{4+2\alpha+r},
            \qquad r\ge\alpha^2.}                    \tag{6}
\]
Thus both \(q_\pm=0\) and \(\mathcal E(G)=0\) force \(v\) constant;
the resulting metric is a hyperbolic product. The assertion concerns
this full block family, not all metrics on \(B\times F\).
The derivative budget of the actual harmonic forms is also exact:
\[
 \int_M|\nabla\omega_\pm|^2=\tfrac12D(v),\qquad
 q_\pm=\tfrac92\left(\fint_M|\nabla\omega_\pm|^2+r\right).
                                                               \tag{5a}
\]

**Proof.** The exact Ricci calculation of the companion gives
\[
 s_G+4=-\frac14|k_v|^2|dv|^2,\qquad
 E_{HH}=-\frac14|k_v|^2dv\otimes dv.                    \tag{7}
\]
Unit fiber speed implies
\(\fint s=-4-\alpha\), and direct expansion gives
\[
 R:=\int_M|\operatorname{Ric}|^2=V(4+2\alpha+r).
                                                               \tag{8}
\]
LeBrun's Chern--Weil identity, separately in either orientation, is
\[
 \mathfrak D_\pm=\frac92\bigl[R-8\pi^2(2p_\pm-T_\pm)\bigr].
                                                               \tag{9}
\]
Here \(T_\pm=2\chi\pm3\tau=A=p_\pm\) and
\(8\pi^2A=4V\). Equations (8)--(9) prove (5).

Pointwise \(E_{HH}\) has rank at most one and its trace equals the
entire trace of \(E\); the vertical residual is trace-free. Hence
\(r\ge\fint(\operatorname{tr}E)^2\ge\alpha^2\).
Direct minimization over nonzero Einstein constants gives
\(\mathcal E=4-(\int s)^2/(RV)\). Inserting (8) proves (6).
Its numerator is at least \(3r\). Thus zero relative defect forces
\(r=\alpha=0\), and (1) forces \(dv=0\). This also rules out a
different nonzero Einstein normalization inside this family; its scalar
curvature is negative, so Ricci-flatness is not an omitted case.

For (5a), use orthonormal base vectors \(X_i\), fiber vectors \(e_a\),
and \(S_i=\tfrac12h^{-1}k_v\,\partial_iv\). The covariant derivatives
of \(\omega_\pm\) in horizontal directions vanish. In a vertical
direction their only nonzero components are mixed base--fiber ones.
Squaring these gives \(2\sum_i|S_i|^2\): the cross contraction
vanishes since the \(S_i\) are proportional to one symmetric
trace-free matrix, which is orthogonal to its product with the fiber
complex structure. Hence
\(|\nabla\omega_\pm|^2=\tfrac12|k_v|^2|dv|^2\).
Integrating the unit-speed condition proves (5a).
\(\square\)

## 3. The precise missing global quantity is a scalar spectral scale

Let \(\lambda_1=\lambda_1(B,\gamma)>0\) and
\(\operatorname{Var}_B(v)=\fint_B(v-\bar v)^2\).
The companion's full nonlinear energy identity implies
\[
 r\ge\frac1{4V}\int_B(\Delta_\gamma v)^2,
 \qquad \Delta_\gamma=-\operatorname{div}\nabla.        \tag{10}
\]
Consequently
\[
 \boxed{q_\pm\ge\frac{9\lambda_1}{4A_F}
                       \operatorname{Var}_B(v),\qquad
 r\ge\frac{\lambda_1^2}{4A_F}\operatorname{Var}_B(v).} \tag{11}
\]
Both powers of \(\lambda_1\) are attained in order by the actual
cyclic family below. These bounds do not replace \(\lambda_1\) by a
genus-independent constant.

There is also an input-to-saturation implication in this family:
\[
 \boxed{q_\pm\le\left(\frac92+\frac9{\lambda_1}\right)r.} 
                                                               \tag{12}
\]
Indeed \(\int(\Delta v)^2\ge\lambda_1D(v)\), so (10) gives
\(\alpha\le r/\lambda_1\); now use (5). If only the scale-free
relative defect is supplied, then
\[
 \mathcal E<\frac37
 \quad\Longrightarrow\quad
 r\le\frac73\mathcal E,
\]
\[
 q_\pm\le\left(\frac{21}2+\frac{21}{\lambda_1}\right)\mathcal E,
 \qquad
 \operatorname{Var}_B(v)\le
          \frac{28A_F}{3\lambda_1^2}\mathcal E.         \tag{13}
\]
To check the implication, (6) and \(\alpha\le\sqrt r\) give
\(\mathcal E\ge3r/(4+2\sqrt r+r)\). This increasing function
equals \(3/7\) at \(r=1\); for \(r<1\), it is at least \(3r/7\).

Equations (11)--(13) distinguish curvature-functional saturation from
constancy of the actual global moduli parameter. They eliminate the
auxiliary-form supply assumption and the separate near-saturation
assumption here, using the genuine geometric family and its scalar
spectrum. They make no analogous claim for unrestricted near-Einstein
metrics without a surface fibration or without (1).

## 4. Variable base curvature and the complete cscK equality family

The same construction also allows an arbitrary base metric \(\gamma\)
on the fixed surface of genus at least two. Define
\[
 \lambda_B=-\fint_B K_\gamma
      =\frac{4\pi(g(B)-1)}{\operatorname{Area}(B,\gamma)}>0.
\]
The actual classes remain \(c_1(TB)\pm c_1(TF)\), but their entire
harmonic representatives are now
\(- (\lambda_BdA_B\pm dA_F)/(2\pi)\). Only their self-dual parts
in the corresponding orientations enter the functional:
\[
 H_\pm^+=-\frac{\lambda_B+1}{4\pi}\omega_\pm,\quad
 p_\pm=\frac{(\lambda_B+1)^2V}{8\pi^2},\quad
 T_\pm=A=\frac{\lambda_B V}{2\pi^2}.
                                                               \tag{17}
\]
In particular a nonzero negative projection is retained when the two
factor scales differ; it is not dropped as though every actual class
were self-dual.

Put \(X=|dv|^2\), and let \(\Xi(v)\ge1/(16A_F)\) be the full
normal-acceleration coefficient in the companion. Direct expansion of
all its Ricci blocks and (9) give
\[
 \boxed{\begin{aligned}
 q_+=q_-=\frac9{2V}\bigg[&2A_F\int_B(K_\gamma+\lambda_B)^2
       -\frac12\int_B K_\gamma X\\
       &+\frac14\int_B(\Delta v)^2+\int_B\Xi(v)X^2\bigg].
 \end{aligned}}                                               \tag{18}
\]
For verification before completing the square, the Ricci energy is
\[
 R=2V+2A_F\int_BK_\gamma^2-\tfrac12\int_BK_\gamma X
                 +\tfrac14\int_B(\Delta v)^2+\int_B\Xi(v)X^2,
\]
and \(8\pi^2(2p_\pm-T_\pm)=2(1+\lambda_B^2)V\).
These prove (18) without invoking an unproved geometric limit.

If \(K_\gamma\le-\kappa_0<0\), every displayed term in (18) is
nonnegative and
\[
 q_\pm\ge\frac{9A_F}{V}\int_B(K_\gamma+\lambda_B)^2
                       +\frac{9\kappa_0}{4V}\int_B|dv|^2.
                                                               \tag{19}
\]
Equality \(q_\pm=0\) is equivalent to constant \(v\) and constant
base curvature. The resulting product is cscK, and is Einstein only if
\(\lambda_B=1\). Thus the complete classical equality family is
preserved, rather than incorrectly replacing it by the KE family.

For the actual pointwise Yau26 input \(\delta_-(G)<1\), the horizontal
Ricci eigenvalue perpendicular to \(dv\) is exactly \(K_\gamma\).
Consequently \(|K_\gamma+1|\le\delta_-\), so (19) applies with
\(\kappa_0=1-\delta_-\). This also makes
\(1-\delta_-\le\lambda_B\le1+\delta_-\). Equations (9),(17) and
\(R/V\le4(1+\delta_-)^2\) yield the concrete upper bound
\[
                       q_\pm\le54\delta_-+9\delta_-^2.         \tag{20}
\]
Thus functional saturation is automatic from pointwise Ricci pinching
on this actual block family, even with variable base curvature. What is
not automatic is global constancy of its moduli parameter: the scalar
spectral scale in (11)--(13) still matters.

## 5. Fixed moduli oscillation with exact periods and vanishing defects

Fix a hyperbolic base \(B_0\) and a nonzero primitive integral harmonic
one-form \(\eta\). Let \(B_m\) be its connected degree-\(m\) cyclic
cover. On the infinite cyclic cover, choose \(z\) with
\(dz=\eta\), \(z(\tau x)=z(x)+1\). Take a fixed
\(a>0\) inside the interval (1), after translating its center, and set
\[
             v_m=a\cos(2\pi z/m).                      \tag{21}
\]
For \(m\ge3\), summing over the deck translates gives exactly
\[
 \bar v_m=0,\qquad\operatorname{Var}_{B_m}(v_m)=a^2/2,
\]
\[
 D(v_m)=\frac{2\pi^2a^2}{m}\int_{B_0}|\eta|^2,
\quad
 \int_{B_m}(\Delta v_m)^2
       =\frac{8\pi^4a^2}{m^3}\int_{B_0}|\eta|^4.       \tag{22}
\]
Write \(V_0=A_F\operatorname{Area}(B_0)\). The complete block
formula, with the fixed smooth path on a compact interval, gives
\[
 \delta_-(G_m)=O(m^{-2}),\quad r_m=\Theta(m^{-4}),\quad
 \mathcal E(G_m)=\Theta(m^{-4}),
\]
\[
 \boxed{q_{+,m}=q_{-,m}
  =\frac{9\pi^2a^2}{2V_0m^2}\int_{B_0}|\eta|^2+O(m^{-4}).}
                                                               \tag{23}
\]
The lower bound for \(r_m\) is (10) and (22); its upper bound follows
from \(|dv_m|+|\nabla^2v_m|=O(m^{-1})\) together with the sharper
\(\Delta v_m=O(m^{-2})\) and the exact absence of a mixed block.
Equivalently the full nonlinear identity has only
\((\Delta v_m)^2\) and bounded multiples of \(|dv_m|^4\).
The two-sided estimate for \(\mathcal E\) follows from (6).
The cyclic-cell estimate in
[I33](20260924_integrable_kernel_cyclic_repair.md) and the Rayleigh quotient
in (22) give \(\lambda_1(B_m)=\Theta(m^{-2})\), confirming the orders
in (11). There is no claim that \(v_m\) itself is an eigenfunction:
\(|\eta|^2\) need not be constant.

In particular all of the following hold simultaneously:

- the two gauge classes are actual and have no negative-square cost;
- their harmonic representatives are the **exact** nonvanishing
  constant-length forms (3), with no period error;
- pointwise Ricci defect and both normalized functional deficits vanish;
- even the unnormalized Ricci-error energy is \(O(m^{-3})\);
- the marked moduli oscillation in (22) stays fixed and nonzero.

This is a concrete sharpness statement for upgrading average gauge
structure to global constancy of the supplied fibration. It is not a
counterexample to Yau26: every \(B_m\times F\) already carries exact
hyperbolic product metrics. The companion proves separation from
fiber-preserving product outputs; neither note asserts separation from
**all** Einstein metrics and arbitrary diffeomorphisms. Exact periods,
absence of zeros, and small local derivative energy do not alone remove
the long scalar slow modes.

## 6. Sources and what is additional

- C. H. Taubes, *The Seiberg--Witten invariants and symplectic forms*,
  Mathematical Research Letters 1 (1994), 809--822,
  [main theorem](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf),
  supplies actual classes in (3). The new argument does not claim to
  invent canonical-class nonvanishing.
- C. LeBrun, *Ricci curvature, minimal volumes, and Seiberg--Witten
  theory*, [Propositions 4.1--4.2 and equation (17)](https://arxiv.org/html/math/0003068),
  supply the classical identity (9) and its gauge interpretation.
- The [new nonlinear slow-family calculation](20260924_nonlinear_slow_moduli.md)
  supplies the full Ricci blocks and (10), retaining the normal
  acceleration terms rather than dropping them after projection.
- The [previous cyclic inverse theorem](20260924_integrable_kernel_cyclic_repair.md)
  supplies the order of the scalar spectral scale. Here the amplitude
  is fixed, so the new family is not confined to its shrinking
  \(O(m^{-2})\) repair neighbourhood.

The additional connection is the exact formula (5), with actual classes
and a real, fully nonlinear metric family, and its sharp spectral
consequences (11)--(23). No priority or optimality beyond the stated
orders on this family is claimed.
