# Step 69: anisotropic cusp compensation after correcting the two route baselines

Session: S0910A03. Agent1 / Explore.

## 1. Corrections now propagated

The Step 68 graph-volume conclusion was based on two incompatible geometries.
The estimate
\[
\delta>\operatorname{csch}^2(R/\sqrt3)
\]
uses boundaries of deleted real-hyperbolic balls in the normalization
\(\operatorname{Ric}=-g\); their areas grow with \(R\).  Flat cusp truncations
have depth-independent normalized mean curvature.  In
\(\operatorname{Ric}=-3g\), a bridge with outward mean curvatures three only
gives
\[
L\ge {2\over k}\operatorname{artanh}(1/k),\qquad
k=\sqrt{1+\delta/3}.
\]
This is a logarithmic length requirement, not a small-volume construction.
For \(G=dr^2+f(r)^2\gamma_r\), intrinsic curvature enters the tangential
Ricci endomorphism as \(f^{-2}\operatorname{Ric}_{\gamma_r}^{\sharp}\), while
volume is \(\int f^3\operatorname{Vol}(\gamma_r)dr\).  Slow interpolation and
small isotropic scale therefore compete.

For the surface-bundle candidate \(E_D\), a hypothetical normalized Einstein
metric does not have volume \(V_0\).  Chern--Gauss--Bonnet gives
\[
8\pi^2\chi(E_D)=\int |W|^2+{2\over3}\operatorname{Vol}
\quad(\operatorname{Ric}=-g),
\]
so the manuscript's inequalities leave \(V_0<\operatorname{Vol}<3V_0\).
The full curvature energy is topologically fixed at \(8V_0\), which is why its
attainment, rather than normalized volume, is equivalent to Einstein
existence.  Also, \(E_D\) has positive simplicial volume; the available entropy
and simplicial-volume constants have slack rather than vanishing.

These corrections were inserted into the Step 68 notes and sent to the group
(message #487).

## 2. Exact harmonic-map baseline closes the generic shortcut

Chapter 9 of `20260912.tex`, lines 6035--6433, already contains the exact
baseline suggested by the strategist.  Let
\[
(M,G)=(\Sigma_q,g_0)\times(\Sigma_p,k),\qquad \operatorname{Ric}_G=-G,
\]
and choose a different marked hyperbolic target \((\Sigma_q,h)\).  The unique
harmonic diffeomorphism \(u:(\Sigma_q,g_0)\to(\Sigma_q,h)\) gives the harmonic
submersion \(f=u\circ\operatorname{pr}_1\).  It is generally not horizontally
conformal, and its pulled-back target area form is neither coclosed nor
constant length.  Thus Einstein geometry plus a surface-group extension and
submersion do not imply a harmonic morphism.

Allowing the target to vary does not repair this.  The unique minimizing
marked target exists, but its Euler--Lagrange equation is only
\[
{1\over2}\int_M\operatorname{tr}_G f_h^*q\,dV_G=0
\quad\text{for all target TT }q.
\]
For a submersion this is TT orthogonality of a *fiber-averaged* push-forward
tensor, not a pointwise pure-trace equation.  Lines 6378--6427 construct a
closed near-Einstein family in which the target is the unique global optimum,
the map is a genuine rank-two harmonic submersion, all target TT stationarity
conditions hold, yet horizontal conformality fails.  More sharply, exact
Einstein product families with a fixed mismatched target make every finite
harmonic-one-form test positive while its smallest eigenvalue tends to zero.

Consequently the generic harmonic-map route has no missing routine lemma.  A
successful attack on \(E_D\) must use its infinite Dehn-twist outer monodromy
or a new Einstein identity giving an upper estimate on one of the defects
\(S_f\), \(\delta f^*\omega_h\), or \(\nabla df\).  Target optimization alone
adds only averaged stress balance.  This route is retained as a deep
monodromy-specific problem, not the immediate construction route.

## 3. Transferable content of Chapter 6

The surface-bundle construction does not homothetically shrink its curved
fiber.  It keeps every fiber metric \(h_z\) exactly hyperbolic and of fixed
area; only a base geodesic length \(\ell\) collapses.  The monodromy path has
trace-free shape operator
\[
S={1\over2}\begin{pmatrix}0&v\\v&0\end{pmatrix},\qquad v=Qz',
\]
and the entire residual is
\[
\Phi_{m ON}=
\begin{pmatrix}
-v^2/2&0&0&(v_u+2jv)/2\\
0&0&0&0\\
0&0&-v^2/2&-(v_t+kv)/2\\
(v_u+2jv)/2&0&-(v_t+kv)/2&v^2/2
\end{pmatrix}.
\]
Slow variation makes \(v=O(L^{-1})\), but the intrinsic negative-curvature
blocks remain exactly at the target Einstein scale.  The collapsing circle is
a locally flat quotient direction whose size never occurs inversely in this
matrix.  This is the mechanism worth transferring.

For a torus collar written in normalized expanding variables
\[
G=dt^2+e^{2t}\gamma_t,
\]
the exact residual is
\[
\begin{aligned}
E_{00}&=-2b-|B|^2-b',\\
E_T^\sharp&=e^{-2t}\operatorname{Ric}_{\gamma_t}^\sharp-bI-3B-bB-B',\\
E_{0\cdot}&=\operatorname{div}_{\gamma_t}B-db,
\end{aligned}
\]
where \(B=\tfrac12\gamma^{-1}\gamma'\), \(b=\operatorname{tr}B\).
A long path works only after entering an expanding regime where
\(e^{-2t}\operatorname{Ric}_{\gamma_t}\) is small and the path has uniformly
controlled geometry.  It cannot start from a uniformly homothetically shrunken
nonflat Koiso center.

## 4. Rank-two collapsed scalar-minus-six Koiso centers

There is, however, an exact analogue of Chapter 6's quotient mechanism.  Start
on \(T^3\) with
\[
h=d\theta^2+e^{2f(\theta)}dX^2+e^{-2f(\theta)}dY^2,
\qquad f(\theta)=A\sin\theta,
\]
so \(R_h=-2(f')^2\).  Solve the periodic Yamabe equation
\[
-8u''-2(f')^2u=-6u^5
\]
and set \(q=u^4h\).  Then \(R_q=-6\), hence \((q,W=0)\) is valid analytic
Koiso data for \(\operatorname{Ric}_G=-3G\).

For every integer \(N\ge1\), quotient the two translational symmetries by
periods \(1/N\):
\[
q_N=u^4\left[d\theta^2+e^{2f}{dx^2\over N^2}
                 +e^{-2f}{dy^2\over N^2}\right]
\quad\text{on unit-period }(\theta,x,y).
\]
The coordinate change \(X=x/N,Y=y/N\) makes every \(q_N\) locally isometric
to \(q_1\).  Therefore all local curvature and Koiso Taylor coefficients are
independent of \(N\), while
\[
\operatorname{Vol}(q_N)=N^{-2}\operatorname{Vol}(q_1).
\]
This is anisotropic lattice collapse, not homothety; it preserves the
normalized Einstein scale exactly.

`workspace/scripts/step69_collapsed_koiso_center.py` solves the Yamabe ODE and
writes `workspace/data/step69_collapsed_koiso_center.json`.  For \(A=1\),
\[
0.6228147\le u\le0.6583453,
\quad \|R_q+6\|_\infty<4.5\cdot10^{-15},
\quad \operatorname{Vol}(q_1)=0.4364388.
\]
The computed Ricci endomorphism ranges by component from approximately
\((-8.323,-8.146,-8.146)\) to \((-3,5.146,5.146)\); the center is strongly
anisotropic, as it must be.  The initial Koiso acceleration is
\(S'(0)=\operatorname{Ric}_q^\sharp+3I\).

The same flat lattice can appear at a hyperbolic cusp after two operations.
Take a degree-\(N\) cover in the \(\theta\) cusp direction, changing its flat
lattice from \((1,1,1)\) to \((N,1,1)\); truncate at depth \(\log N\), whose
uniform hyperbolic scale is \(1/N\).  The induced length type is
\((1,N^{-1},N^{-1})\), exactly the quotient type of \(q_N\), up to the
bounded nonflat deformation carried by the core.  This removes the previous
scale mismatch without rescaling local curvature.

Two scope qualifications are essential.  First, a chosen peripheral
sublattice need not automatically extend to a finite cover of a fixed
hyperbolic four-piece; current source retrieval found explicit one-cusped
hyperbolic 4-manifolds with torus-link orientable double covers, but not a
theorem granting arbitrary one-direction peripheral covers.  Second, the
construction still needs a fixed-scale transition from \(S=0\) at the Koiso
center to \(S\simeq I\) on an expanding end.  The quotient parameter \(N\)
does not reduce that local problem; it only makes the eventual core and cusp
lattices compatible at vanishing volume.

## 5. What the exact Li--Liu mixed-end family establishes

Li--Liu Theorem 1.3 constructs on \((0,\infty)\times T^3\) a complete
\(\operatorname{Ric}=-3h\) metric with one PE end and one AH cusp for each
prescribed quotient metric on \(T^2\).  Their Type-I form is
\[
h=\xi^{-2}\left(Wd\xi^2+W^{-1}\eta^2+We^v g_{T^2}\right),
\quad W=1-\tfrac12\xi v_\xi,
\]
with Toda equation \((e^v)_{\xi\xi}+\Delta_{T^2}v=0\), and the AH cusp has
\(W\to1\), \(v\to c_0(x,y)\).  Thus an exact Einstein solution can carry
inhomogeneous fixed-scale tangential geometry into a rank-three collapsing
flat cusp.  This is direct evidence that the required compensation is real,
not merely formal.  Because the family is ASD, it cannot contain a totally
geodesic \(T^3\); it cannot be doubled directly.  It is better viewed as a
background for a non-ASD mixed-boundary deformation or as a source of the
correct asymptotic variables.

## 6. Exploratory Cauchy evolution of the explicit center

`workspace/scripts/step69_koiso_galerkin.py` integrates the exact
\(T^2\)-invariant Gaussian Einstein evolution for diagonal metrics
\[
G=dt^2+e^{2a(t,\theta)}d\theta^2+e^{2b(t,\theta)}dx^2
      +e^{2c(t,\theta)}dy^2
\]
from the \(A=1\) center, using 6, 8, 10, and 12 Fourier modes.  Hamilton and
momentum constraints converge rapidly with resolution through about
\(t=0.4\).  The solutions agree there: at \(t=0.4\),
\[
H_{\min}\approx-3.848,\qquad H_{\max}\approx-0.873,
\]
while the 12-mode constraint residuals are about \(4.2\times10^{-3}\) and
\(2.8\times10^{-3}\).  The evolution then becomes singular/stiff near
\(t\approx0.45\), with truncation-dependent blow-up.  Since this is an elliptic
Cauchy problem, the late blow-up alone is not reliable; the resolution-stable
sign reversal well before it is useful: this explicit center evolves away
from the desired cusp slow manifold rather than toward \(H\to3\).

A 16-mode sweep (`step69_koiso_amplitude_dynamics.py`) over
\(A=0.5,\ldots,4\) showed the same pattern.  The largest positive value of
\(H_{\min}\) before it returns through zero increases only from about 0.19 to
0.59; every tested seed then contracts and the Cauchy solver fails at finite
time.  This is evidence about this one conformal seed family, not an exclusion
of all scalar-minus-six centers or all Einstein half-cores.

The amplitude sweep of the center itself
(`step69_center_amplitude_sweep.py`) exposes why: for every tested
\(A=0.03,\ldots,3\), \(P=\operatorname{Ric}_q^\sharp+3I=S'(0)\) has a negative
eigenvalue.  In dimension three with \(R_q=-6\),
\[
P_k=\operatorname{Ric}_k+3=-K_{ij}
\]
for the complementary sectional plane.  Hence the center contains positive
sectional curvature and initially contracts in some principal direction.  A
center with \(P>0\), equivalently \(K_q<0\), would enter the expanding cone in
all directions—but Preissmann forbids such a metric on \(T^3\).  This gives a
clean structural explanation: every scalar-minus-six torus center has some
initial contraction, and a successful half-core must use nonlinear spatial
redistribution to overcome it.  The Li--Liu mixed-end solution shows such
redistribution is possible without reflection symmetry; the reflection-core
problem must accomplish it while starting at \(S=0\).

## 7. Revised route judgment

The generic harmonic-map program is currently weaker: Chapter 9 already
constructs exact and near-exact countermodels to every implication short of a
new monodromy-specific Einstein estimate.  The graph route now has a sharper
constructive decomposition:

1. **local core dynamics:** find a scalar-minus-six analytic torus metric whose
   Koiso germ survives its necessarily mixed initial expansion/contraction and
   reaches an expanding end, or deform a Li--Liu PE--cusp solution to acquire a
   totally geodesic reflection surface;
2. **scale matching:** use rank-two lattice quotients of the core and a
   one-direction cusp cover plus depth \(\log N\), preserving local Einstein
   scale while total interface volume tends to zero;
3. **peripheral realization and gluing:** prove the required cusp sublattices
   occur in hyperbolic four-pieces and match affine boundary data; then control
   finite transitions and assemble a closed extended graph manifold.

Item 2 is the concrete new advance of this step.  Item 1 remains the decisive
analytic difficulty.  Item 3 is a genuine arithmetic/topological dependency,
not yet established by the retrieved sources.  Even completion of this
negative branch would not settle the sign-unrestricted Yau statement without
a same-dimensional positive-branch failure; A02's mixed-orbifold work remains
complementary.
