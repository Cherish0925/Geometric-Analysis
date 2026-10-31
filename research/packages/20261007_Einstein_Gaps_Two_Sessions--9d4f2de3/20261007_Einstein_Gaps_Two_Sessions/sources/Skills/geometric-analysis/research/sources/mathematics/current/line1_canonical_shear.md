# Canonical harmonic calibrations on the inherited closed shear examples

23 September 2026. The closed smooth manifolds and their pointwise
near-Einstein metrics below are inherited from Rounds 11 and 14. Round 15
already supplies their constant-norm harmonic almost-Kähler forms. This
note verifies the additional canonical cohomology identity for a balanced
profile, transfers the construction to one fixed symplectic form, and
computes its first-line LB/period defects. No new smooth family or
literature priority is claimed.

The conclusion is a concrete limitation of global structural upgrades:
arbitrarily small pointwise Einstein and Weyl-calibration errors, even
with an exactly harmonic constant-norm canonical form and zero period
excess, do not force a Kähler structure on the smooth manifold or a finite
cover. This does not decide whether it admits a non-Kähler Einstein metric.

## 1. Fixed object and statement

Fix \(h\ge1\), \(g\ge2\), a compact oriented surface \(B=F_{h,2}\), and a
closed oriented surface \(F=\Sigma_g\). Give \(F\) a fixed curvature \(-1\)
metric \(h_F\), with area form \(\omega_F\). Choose a nonzero primitive
integral class in \(H^1(F;\mathbb Z)\), and let \(\beta\) be its harmonic
representative with periods in \(2\pi\mathbb Z\). Choose the circle-valued
map \(u:F\to\mathbb R/(2\pi\mathbb Z)\) with \(-du=\beta\).

Let \(M\) be the fixed closed oriented self-gluing of \(B\times F\) by

\[
 (\phi,x)\longmapsto(-\phi+u(x),x).
 \tag{1}
\]

Projection to \(F\) survives, giving a surface bundle
\(\pi:M\to F\) with fiber \(\Sigma_{h+1}\). The inherited topology gives

\[
 \chi(M)=4h(g-1),\qquad \tau(M)=0,\qquad
 T=2\chi(M)=8h(g-1)>0.
 \tag{2}
\]

With this projection, the object is an earlier cyclic Dehn-twist
\(E_D\)-type surface bundle, after interchanging the surface roles. It is
not a new smooth topology beyond the inherited construction.

No finite cover admits any Kähler structure. The proof is the identity-
mapping-class case of [Round 11's virtual Kähler obstruction](round11_kahler.md).
For the primitive shear chosen here the abelianization also gives
\(b_1=2h+2g+1\), so already \(M\) has odd first Betti number. The virtual
claim is stronger and uses the inherited group argument, not parity.

**Theorem.** There is a fixed symplectic form \(\omega\) on this fixed
\(M\), with compatible almost-complex first Chern class \(c\), and smooth
\(\omega\)-compatible metrics \(q_\ell\), \(\ell\downarrow0\), such that

\[
 [\omega]=-2\pi c,\quad c^2=T,\quad
 |\omega|_{q_\ell}^2=2,\quad *_{q_\ell}\omega=\omega,\quad
 d\omega=d^*_{q_\ell}\omega=\Delta_{H,q_\ell}\omega=0,
 \tag{3}
\]
\[
 \operatorname{Vol}(q_\ell)=2\pi^2 T,\qquad
 p_\ell=(c_{q_\ell}^+)^2=T\quad\text{exactly}.
 \tag{4}
\]

Put

\[
 A_{\omega,1/2}=\frac12\left(\frac{|\omega|^2}{3}I-
                                      \omega\otimes\omega\right).
\]

For every fixed nonnegative integer \(j\), with norms taken in \(q_\ell\),

\[
 \|\nabla^j(\operatorname{Ric}+q_\ell)\|_\infty\le C_j\ell,
 \qquad
 \|\nabla^j(W^+-A_{\omega,1/2})\|_\infty\le C_j\ell,
 \tag{5}
\]
\[
 \|\nabla^{j+1}\omega\|_\infty\le C_j\ell,
 \qquad \|\operatorname{Rm}\|_\infty\le C,
 \qquad \|\nabla^{j+1}\operatorname{Rm}\|_\infty\le C_j\ell.
 \tag{6}
\]

The class \(c\) is an actual ordinary SW class, and hence supplies the
conformal-class weighted solutions used in the first-line LB theorem.
With

\[
 B_s=\int s^2-32\pi^2 T,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 D=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+
                              \frac{|W^+|^2}{2}\right)-\frac{p_\ell}{2},
\]

one has

\[
 B_s=O(\ell^3),\quad P=O(\ell^3),\quad
 \boxed{D=\frac{P+B_s/4}{32\pi^2}=O(\ell^3),\qquad p_\ell-T=0.}
 \tag{7}
\]

Thus the normalized LB defect tends to zero. The Round-21 harmonic-source
budget \(\fint|\Delta_H\omega|^2\) is exactly zero, and its actual
calibration defect at \(t=1/2\) obeys

\[
 d_{1/2}=\fint\left(|\operatorname{Ric}+q_\ell|^2
       +|W^+-A_{\omega,1/2}|^2+(|\omega|^2-2)^2\right)=O(\ell^3).
 \tag{8}
\]

Do not confuse the zero Hodge-Laplacian budget with \(B_s\), which is
strictly positive for every \(\ell>0\).

## 2. The balanced inherited metric

Choose curvature \(-1\) metrics \(b_\ell\) on \(B\) with both geodesic
boundary circles of length \(\ell\). They may be chosen smoothly in
\(\ell>0\) using fixed pants coordinates. In the signed gluing collar,
use \(\phi\) of period \(2\pi\) and

\[
 a_\ell(t)=\frac{\ell}{2\pi}\cosh t.
 \tag{9}
\]

For sufficiently small \(\ell\), this collar contains the fixed interval
\([-R,R]\), with \(R>0\). Choose a fixed nonnegative smooth even bump
\(\eta\), supported in \((-R,R)\), with positive integral, and set

\[
 z'(t)=\frac{\eta(t)}{\int\eta},\qquad
 z(-R)=0.
\]

Then \(z=0\) near the left end, \(z=1\) near the right end, and

\[
 z'(-t)=z'(t),\qquad z(-t)=1-z(t).
 \tag{10}
\]

On this collar use

\[
 g_\ell=dt^2+a_\ell^2\theta^2+h_F,
 \qquad \theta=d\phi+z(t)\beta.
 \tag{11}
\]

Outside it use the product metric, with the right-side pullback determined
by the actual gluing (1). Since all jets of \(z\) are constant near the
ends, these metrics are smooth on the fixed closed manifold. No globally
defined real primitive of \(\beta\) is used. This is the pure-shear
specialization of [Round 11](round11_closed_gluing.md), with a symmetric
profile; there is no fiber-metric interpolation.

Let \(E=\ker d\pi\), and let \(F_\ell=E^{\perp_{g_\ell}}\). On the
collar, \(E\) is the \((t,\phi)\)-plane and \(F_\ell\) is the horizontal
graph over \(TF\). Define their metric area forms

\[
 \Omega_{E,\ell}=a_\ell\,dt\wedge\theta,\qquad
 \Omega_\ell=\Omega_{E,\ell}+\omega_F.
 \tag{12}
\]

On the product region take the usual sum of the two area forms. These
forms match under (1). Moreover \(d\beta=0\), and every term in
\(d\Omega_{E,\ell}\) contains either \(d\beta\) or two copies of \(dt\).
Thus \(d\Omega_\ell=0\). In the orthonormal coframe of (11),
\(\Omega_\ell=e^0\wedge e^1+e^2\wedge e^3\), so it is self-dual and has
squared norm two. It is therefore harmonic and defines a compatible
almost-complex structure \(J_\ell\).

The determinant of (11) is independent of \(z\). Gauss–Bonnet on the
two factors gives

\[
 V=\operatorname{Area}(B,b_\ell)\operatorname{Area}(F,h_F)
   =(4\pi h)(4\pi(g-1))=2\pi^2T.
 \tag{13}
\]

These almost-Kähler and volume facts are inherited. The next step fixes
the previously unspecified canonical period exactly.

## 3. Euler connection, its sign, and the compactly supported primitive

The splitting into oriented two-plane bundles gives
\(c_1(TM,J_\ell)=e(E)+e(F_\ell)\). Since \(d\pi:F_\ell\to TF\) is an
oriented bundle isomorphism,

\[
 e(F_\ell)=-[\omega_F]/(2\pi).
 \tag{14}
\]

For \(E\), construct an auxiliary metric \(SO(2)\) connection, not
necessarily the projected Levi-Civita connection. Outside the active
collar it is the surface Levi-Civita connection pulled back from \(B\).
In the oriented orthonormal frame dual to \((dt,a_\ell\theta)\), specify
its connection entry by

\[
 \gamma^0{}_1=-a_\ell'(t)\theta.
 \tag{15}
\]

At both ends this agrees with the product surface connection, including
the right-side coordinate pullback. The gluing acts on the oriented
\(E\)-frame by a constant rotation, so it introduces no extra connection
derivative. Hence this defines a global connection on \(E\).

Explicitly, in inward boundary coordinates \((r,\phi_B)\) the oriented
surface coframe is \((-dr,a\,d\phi_B)\). On the left it becomes
\((dt,a\theta)\); on the right, \(r=t\) and
\(d\phi_B=-d\phi+du=-\theta\), so it becomes
\(-(dt,a\theta)\). This is the constant rotation by \(\pi\).
The surface connection entry \(+a_r'd\phi_B\) pulls back to
\(-a_t'\theta\) on both ends.

The sign can be checked on the untwisted surface: its curvature entry is
\(-a_\ell''dt\wedge d\phi=-a_\ell dt\wedge d\phi\), representing Gaussian
curvature \(-1\). Because \(SO(2)\) is abelian and \(a_\ell''=a_\ell\),
the Euler form of (15) on the active collar is

\[
 \frac{d\gamma^0{}_1}{2\pi}
 =-\frac1{2\pi}\left(\Omega_{E,\ell}
                  +a_\ell' z'\,dt\wedge\beta\right).
 \tag{16}
\]

The correction is exact globally, not only locally. Indeed, \(a_\ell'\)
is odd and \(z'\) is even, so
\(\int_{-R}^{R}a_\ell' z'\,dt=0\). Put

\[
 H_\ell(t)=\int_{-R}^{t}a_\ell'(v)z'(v)\,dv.
\]

It vanishes near both ends. Thus \(H_\ell\beta\) extends by zero to a
smooth global one-form on \(M\), and

\[
 d(H_\ell\beta)=a_\ell' z'\,dt\wedge\beta.
 \tag{17}
\]

Here \(\beta\) is genuinely a global closed one-form on the collar and,
because the fiber mapping class in (1) is the identity, is the pullback
of the fixed form on the base \(F\). No forbidden real lift of \(u\) is
being substituted for it.

Combining (14)–(17) gives, in real cohomology,

\[
 \boxed{[\Omega_\ell]=-2\pi\bigl(e(E)+e(F_\ell)\bigr)=-2\pi c.}
 \tag{18}
\]

The integral class \(c\) is fixed: the vertical bundle is fixed and all
horizontal complements are homotopic. Also \(c^2=2\chi+3\tau=T\). Since
\(-\Omega_\ell/(2\pi)\) is its harmonic self-dual representative,

\[
 p_\ell=T,\qquad c_{g_\ell}^-=0,
 \qquad |c_{g_\ell}^+|^2=1/(2\pi^2)
 \quad\text{pointwise}.
 \tag{19}
\]

The parity in (10) is important. For a general nonsymmetric profile,
(16) leaves the possible neck cohomology class represented by
\(a_\ell'z' dt\wedge\beta\); it must not simply be discarded.

## 4. Pullback to one fixed symplectic form

Fix a reference \(\ell_0>0\), and put \(\omega=\Omega_{\ell_0}\).
The forms \(\Omega_\ell\) are a smooth cohomologous symplectic family on
the fixed closed manifold. Moser's argument on every compact parameter
interval \([\ell,\ell_0]\) gives an isotopy \(\Phi_\ell\) such that

\[
 \Phi_\ell^*\Omega_\ell=\omega.
\]

Set \(q_\ell=\Phi_\ell^*g_\ell\). Tensor norms, curvature energies,
harmonicity, and compatibility pull back exactly, proving (3)–(4).
No boundedness or convergence of these diffeomorphisms as \(\ell\to0\)
is claimed or needed.

## 5. Complete Ricci blocks and pointwise Weyl calibration

Write \(a=a_\ell\), \(k=a'/a=\tanh t\), and
\(U=a^{-1}\partial_\phi\). With \(X,Y\) horizontal fiber vectors, the
complete nonzero blocks of \(\mathcal E=\operatorname{Ric}_{g_\ell}+g_\ell\)
are

\[
 \begin{aligned}
 \mathcal E_{tt}&=-Q,& \mathcal E_{UU}&=Q,&
 \mathcal E_{XY}&=-\tfrac12a^2z'^2\beta(X)\beta(Y),\\
 \mathcal E_{XU}&=-\tfrac a2(z''+3kz')\beta(X),&
 Q&=\tfrac12a^2z'^2|\beta|^2.
 \end{aligned}
 \tag{20}
\]

All remaining blocks vanish; in particular the \(tU\) entry vanishes
because \(\beta\) is coclosed. These are the inherited full Ricci formulas,
now in curvature \(-1\) normalization. On the fixed active interval,
\(a\) and all its fixed derivatives are \(O(\ell)\). Thus the mixed blocks
are \(O(\ell)\), the diagonal blocks \(O(\ell^2)\), and

\[
 s=-4-Q.
 \tag{21}
\]

For the full curvature calculation use the orthonormal coframe
\(e^0=dt\), \(e^1=a\theta\), and a fiber coframe. Its extra structure term
relative to the hyperbolic product is exactly

\[
 de^1=k e^0\wedge e^1+a z'\,dt\wedge\beta.
 \tag{22}
\]

The last coefficient and all its fixed covariant derivatives are
\(O(\ell)\); fiber coefficients and \(k\) have uniform bounds. Cartan's
connection and curvature equations therefore give
\(\nabla^j(\operatorname{Rm}-\mathcal R_0)=O(\ell)\), where
\(\mathcal R_0\) is the algebraic product tensor for the actual orthogonal
two-plane splitting. The splitting is parallel up to \(O(\ell)\), with
the same derivative bounds. No inverse short-circle factor occurs:
all coefficients are circle independent. This proves (5)–(6), since the
self-dual Weyl part of \(\mathcal R_0\) is precisely
\(A_{\Omega_\ell,1/2}\).

For comparison, the already established exact form identity is

\[
 |\nabla\Omega_\ell|^2=2Q.
 \tag{23}
\]

It follows from the electric connection terms and is proved independently
in [Round 15, §7](round15_rigidity.md). Thus the form is harmonic, but is
not parallel when the shear is nonzero. Harmonicity must not be replaced
by parallelness.

## 6. Exact energy formulas and the LB remainder

Taking the tensor trace and norm in (20) gives

\[
 |\operatorname{Ric}^{\circ}|^2
 =\frac{11}{4}Q^2+\frac{a^2}{2}(z''+3kz')^2|\beta|^2.
 \tag{24}
\]

All defects are supported in the fixed collar, whose volume is
\(2\ell\sinh R\,\operatorname{Area}(F)=O(\ell)\). In particular

\[
 B_s=\int(8Q+Q^2)=O(\ell^3),\qquad P=O(\ell^3).
 \tag{25}
\]

Here are exact coefficients, not just orders. Put
\(A(t)=\cosh(t)/(2\pi)\), and define the fixed positive quantities

\[
 I_3=\int_{-R}^{R}A^3z'^2\,dt\int_F|\beta|^2,\qquad
 I_5=\int_{-R}^{R}A^5z'^4\,dt\int_F|\beta|^4,
\]
\[
 J_3=\int_{-R}^{R}A^3(z''+3\tanh(t)z')^2\,dt\int_F|\beta|^2.
\]

The fiber integrals use \(h_F\); the circle has period \(2\pi\). Then

\[
 \boxed{B_s=8\pi\ell^3 I_3+\frac\pi2\ell^5 I_5,\qquad
 P=\pi\ell^3 J_3+\frac{11\pi}{8}\ell^5 I_5.}
 \tag{26}
\]

The fixed symplectic class supplies the canonical SW class by
[Taubes's Main Theorem](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf).
Here \(b_+=\chi/2+b_1-1>1\); solutions exist for every metric, including
each conformal weight, and reducibles are excluded by \(p=T>0\).

The classical Ricci-energy identity is
\(R_2=8\pi^2(2p-T)+32\pi^2D\). Combining \(p=T\),
\(R_2=P+\int s^2/4\), and (26) gives

\[
 \boxed{D=\frac{\ell^3(J_3+2I_3)}{32\pi}
                +\frac{3\ell^5I_5}{64\pi}>0.}
 \tag{27}
\]

Thus \(D=\Theta(\ell^3)\), while the primitive period excess is identically
zero. The second-order Hodge source is zero exactly, not merely bounded.
The pointwise curvature and Ricci errors are \(O(\ell)\) on a region of
volume \(O(\ell)\), proving (8).

The symmetric optimized full-collar profile of
[Round 14](round14_global.md) also has \(z'\) even. The Euler-connection
argument therefore applies to that original, unrepaired family as well,
after normalization. Its improved Ricci estimates and the scalar-repaired
metrics are inherited; the present note does not claim them as new. A
nonconstant conformal scalar repair retains middle-dimensional harmonicity
and \(p=T\), but not the pointwise constant norm of \(\Omega_\ell\).

## 7. The shear information that survives

There is a fixed integer witness invisible to the vanishing energy norms.
On the circle quotient of the marked throat, the connection is
\(\alpha=z\beta\) and its curvature is
\(F_\alpha=z' dt\wedge\beta\). For a loop \(\gamma\subset F\),

\[
 \frac1{2\pi}\int_{[-R,R]\times\gamma}F_\alpha
 =\frac1{2\pi}\int_\gamma\beta\in\mathbb Z.
 \tag{28}
\]

For a suitable loop it is nonzero (indeed \(\pm1\) for the primitive
class). This is a **relative** flux with the two endpoint trivializations
fixed by the gluing, not a Chern number of an unspecified closed cycle.
The metric sees \(aF_\alpha\), whose norm is \(O(\ell)\); (28) does not
shrink with the circle radius.

Equivalently, the surface-bundle monodromy is a power of the Dehn twist
about the nonseparating gluing curve \(c_0\subset\Sigma_{h+1}\):
\(\rho(\gamma)=D_{c_0}^{\pm u(\gamma)}\). On fiber homology a generator
acts as a nontrivial transvection

\[
 v\longmapsto v\pm\langle v,[c_0]\rangle[c_0].
 \tag{29}
\]

Its nonzero nilpotent part \(N\) has \(N^2=0\); powers are \(I+nN\),
never the identity for \(n\ne0\). The shear remains nonzero on every
finite cover of the base. The stronger statement excluding every Kähler
finite cover of the total space follows from the inherited Bass–Serre
kernel argument, not just from this chosen projection.

This is the surviving global information: a fixed mapping-class/relative
flux datum, not a nonzero lower bound for the ordinary canonical period
excess. Equations (18)–(19) show that even this period excess can vanish
exactly while the shear remains.

## 8. Scope of the structural failure

There is also a fixed-symplectic variational consequence. For this one
\((M,\omega)\), the infimum of \(\int|\nabla\omega|^2\) over
\(\omega\)-compatible metrics is zero and is not attained. Indeed,
(23) and (26) give \(\int|\nabla\omega|^2=2\pi\ell^3I_3\to0\);
attainment at zero would make \(\omega\) parallel and the metric Kähler,
contrary to the topology. The same sequence has Einstein defect tending
to zero, but attainment of the Einstein-defect infimum is a different
question and is not decided by this argument.

The theorem rules out a proposed implication from the strong actual
calibration hypotheses (3)–(8) alone to the existence of any Kähler metric,
a parallel Kähler structure, or a Kähler finite cover. It also prevents
silently replacing an almost-parallel plane splitting by a global product
decomposition.

It does not contradict Round 21: \(t=1/2\) is its allowed negative-Einstein
root, so that spectral test has zero left side here. Nor does it disprove
an Einstein-existence conclusion without a Kähler requirement. A genuinely
non-Kähler negative Einstein metric elsewhere on this smooth manifold is
not excluded by the present arguments.

The smooth construction, nonvirtual Kähler obstruction, almost-Kähler
forms, and local product estimates are inherited from Rounds 11–15. The
specific additional checks here are the balanced Euler-class identity,
the resulting exact canonical harmonic representative and fixed-form
Moser transfer, and the explicit LB remainder (27). The accompanying
symbolic checker verifies the local exterior algebra, Euler correction,
and energy normalizations; it does not certify SW or global topology.
