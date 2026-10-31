# Step 78: rotating-eigenframe Bianchi VII_0 barrier for finite graph connectors

Session `S0910A03`, Agent1 / Explore.

## 1. Why this benchmark matters

The negative graph-manifold route needs a **finite** connector, not necessarily a
complete reflected Poincare--Einstein filling.  Starting at a reflection face,
the connector must eventually enter the Step 73 expanding-tail regime: one needs
small full defect `Ric+3g`, an approximately umbilic shape operator `S≈I`, and
small scaled intrinsic curvature with compatible attachment jets.

A natural proposed escape from the diagonal center obstruction is to rotate the
contracting and expanding orbit eigenvectors along the torus.  The simplest
geometrically honest realization is
\[
 \omega _1=\cos(kz)\,dx+\sin(kz)\,dy,\qquad
 \omega _2=-\sin(kz)\,dx+\cos(kz)\,dy,
\]
\[
 g=dr^2+a(r)^2dz^2+b(r)^2\omega _1^2+c(r)^2\omega _2^2.       \tag{1.1}
\]
For `z` of period `2π`, integer `k` makes the coframe global.  The slices are
nonflat Bianchi VII_0 geometries, so this is not the already excluded
coordinate-independent flat-slice path.

The main result below is finite-interval and defect-stable.  It does not assume
completeness or PE asymptotics.  It shows that this rotating-eigenframe mechanism
cannot reach the expanding-tail interface.

## 2. Exact curvature reduction

Use the orthonormal coframe
\[
 e^0=dr,\quad e^1=a\,dz,\quad e^2=b\,\omega _1,\quad
 e^3=c\,\omega _2,
\]
and define
\[
 u=\frac{a'}a,\quad v=\frac{b'}b,\quad w=\frac{c'}c,
 \quad H=u+v+w,\quad d=\log\frac bc,\quad p=d'=v-w.
\]
Set
\[
 K=\frac{k^2(b^2-c^2)^2}{2a^2b^2c^2}
   =2k^2a^{-2}\sinh^2d,
\]
\[
 L=\frac{k^2(b^4-c^4)}{2a^2b^2c^2}
   =k^2a^{-2}\sinh(2d)=K\coth d\quad(d\ne0).       \tag{2.1}
\]
A direct Christoffel computation, independently reconstructed by TTCS, gives
for the slice metric `q_r`
\[
 \operatorname{Ric}_{q_r}=\operatorname{diag}(-K,L,-L),
 \qquad R_{q_r}=-K.                                  \tag{2.2}
\]
The full normalized Ricci components are
\[
 \operatorname{Ric}_{rr}=-H'-(u^2+v^2+w^2),
\]
\[
 \operatorname{Ric}_{11}=-K-u'-Hu,
\quad
 \operatorname{Ric}_{22}=L-v'-Hv,
\quad
 \operatorname{Ric}_{33}=-L-w'-Hw.                  \tag{2.3}
\]
All mixed components vanish in the invariant frame.  Thus there is no omitted
momentum equation in this cohomogeneity-one class.

Writing `E=Ric+3g`, equations (2.3) imply
\[
 u'+Hu=3-K-E_1,                                      \tag{2.4}
\]
\[
 p'+Hp=2K\coth d-(E_2-E_3),                          \tag{2.5}
\]
while the definition of `K` gives the kinematic identity
\[
 (\log K)'=-2u+2\coth(d)p.                           \tag{2.6}
\]
The normal equation is
\[
 H'+u^2+v^2+w^2=3-E_r,                               \tag{2.7}
\]
and subtracting it from the sum of the tangential equations yields the forced
Hamilton identity
\[
 H^2-(u^2+v^2+w^2)
 =6-K+E_r-E_1-E_2-E_3.                               \tag{2.8}
\]
The reproducible symbolic calculation is
`workspace/scripts/step78_bianchi_vii0_verify.py`, with output
`workspace/data/step78_bianchi_vii0_symbolic.json`.

## 3. Reflected center

At a reflection face `r=0`,
\[
 u(0)=v(0)=w(0)=H(0)=p(0)=0.                         \tag{3.1}
\]
Equation (2.8) gives
\[
 K_0:=K(0)=6+E_r(0)-E_1(0)-E_2(0)-E_3(0).           \tag{3.2}
\]
Hence if `||E||_op≤δ`,
\[
 6-4\delta\le K_0\le6+4\delta.                     \tag{3.3}
\]
For small defect `K_0>0`, so `d(0)≠0`.  Exchanging the labels `b,c` lets us set
`d(0)>0` without changing the geometry.  In the exact case,
\[
 K_0=6,\quad u'(0)=-3,\quad
 p'(0)=12\coth d(0)>0.                               \tag{3.4}
\]
The orbit plane curvature `K/2` equals `3` at the exact center, attaining the
Step 75 center lower value.

## 4. Finite-interval invariant region

### Theorem

Let (1.1) be smooth on a connected radial interval `[0,R)` with a reflection
face at `0`.  If
\[
 \|\operatorname{Ric}+3g\|_{\rm op}\le\delta\le\frac35,
                                                               \tag{4.1}
\]
then, after exchanging `b,c` so that `d(0)>0`, for every `r in (0,R)` one has
\[
 \boxed{u(r)<0,\qquad p(r)=d'(r)>0,\qquad
        K(r)>K_0\ge6-4\delta.}                       \tag{4.2}
\]

### Proof

At the boundary `p=0`, equations (2.5), (3.3), and `|E_2-E_3|≤2δ` give
\[
 p'\ge2K\coth d-2\delta
    >2K-2\delta\ge12-10\delta>0.                    \tag{4.3}
\]
At `u=0`, equation (2.4) gives
\[
 u'=3-K-E_1\le3-K+\delta.                            \tag{4.4}
\]
Initially the sharper component cancellation following from (3.2) gives
\[
 u'(0)=-3+E_2(0)+E_3(0)-E_r(0)
       \le-3+3\delta<0.                              \tag{4.5}
\]
Therefore the solution enters `u<0,p>0`.  While these inequalities hold,
(2.6) gives `(log K)'>0`, so `K>K_0` at every positive radius.  At any first
later contact with `u=0`,
\[
 u'<3-K_0+\delta\le-3+5\delta\le0,                  \tag{4.6}
\]
and at the endpoint `δ=3/5` the strict inequality `K>K_0` makes (4.6) strict.
At any first contact with `p=0`, (4.3) points strictly back into `p>0`.
A first-exit argument proves (4.2).  Notice that no sign assumption on `H` is
needed: the damping terms vanish on the relevant contact faces.  Equivalently,
one may use the positive integrating factor `exp(int H dr)`.  QED.

The constant `3/5` is the natural uniform threshold for this elementary
componentwise argument: it combines `K_0≥6-4δ` with the later contact condition
`K_0≥3+δ`.  It is not asserted to be optimal under additional relations among
the defect components.

## 5. Strong incompatibility with the tail interface

The Step 73 expanding interface requires, in particular, `S≈I`, so its
`z`-direction eigenvalue must satisfy `u≈1`.  Theorem (4.2) instead gives
\[
 u<0,\qquad \|S-I\|_{\rm op}>1                       \tag{5.1}
\]
throughout every positive-radius portion of the connector.  Thus no sequence
in this ansatz with defect tending to zero can approach the required umbilic
expanding data at any finite exit, even if the exit radius diverges with the
parameter.

There is an independent intrinsic-curvature obstruction.  Since
\[
 \operatorname{Spec}(\operatorname{Ric}_{q_r})=(-K,L,-L),
 \qquad |L|=K|\coth d|>K,                            \tag{5.2}
\]
we retain order-one slice curvature:
\[
 \|\operatorname{Ric}_{q_r}\|_{\rm op}>K\ge6-4\delta. \tag{5.3}
\]
The Hamilton identity also gives
\[
 H^2-|S|^2\le8\delta.                                \tag{5.4}
\]
If `S=I+P` with `||P||_op≤epsilon`, then
\[
 H^2-|S|^2\ge6-12\varepsilon-6\varepsilon^2.        \tag{5.5}
\]
Consequently such a slice is impossible whenever
\[
 6-12\varepsilon-6\varepsilon^2>8\delta.            \tag{5.6}
\]
This is a quantitative interface exclusion in addition to the sign `u<0`.

The exact equations admit integrating-factor forms
\[
 (abc\,u)'=abc(3-K),\qquad
 (abc\,p)'=2abc\,K\coth d,                           \tag{5.7}
\]
and the constraint
\[
 uv+uw+vw+\frac K2=3.                                \tag{5.8}
\]
They show strict contraction of `a`, growth of `|d|`, and growth of `K`.
They do not by themselves prove finite-distance singularity, and no such
statement is used here.

## 6. Scope and mechanism learned

This result excludes **only** the fixed Bianchi VII_0 rotating-eigenframe,
cohomogeneity-one diagonal ansatz.  It does not exclude:

- a shape eigenframe that varies in both `r` and base position;
- a fully non-diagonal shape operator with nontrivial momentum transport;
- matrix-valued orbit geometry depending on two base variables;
- a less symmetric center or a connector that does not start at a reflection
  face;
- a layer where the defect is not uniformly small.

It nevertheless answers the intended inexpensive test decisively.  Merely
rotating the orbit axes with a fixed helical frequency does not dilute the
center burden.  The scalar potential
\[
 K(d,a)=2k^2a^{-2}\sinh^2d
\]
has a one-way feedback: the reflected constraint forces `K_0≈6`; the `z`
direction contracts (`u<0`) and anisotropy grows (`d'>0`); both effects then
increase `K`.

A viable matrix construction must break this feedback, rather than merely add
rotation.  The mathematically distinct mechanisms still worth testing are:

1. genuine two-dimensional base transport, which can export orbit-shape energy
   spatially while expansion dilutes its density;
2. a full map `U` into `SL(2,R)/SO(2)` whose tension vector turns in target
   space rather than remaining on the one-dimensional `d` geodesic;
3. nontrivial Hamilton--Codazzi transfer through off-diagonal shape components;
4. a parameter-dependent forced transition whose weighted defect moments are
   finite while its pointwise defect tends to zero.

These mechanisms should be developed as finite connector equations.  A
complete non-ASD PE filling remains a useful exact benchmark, not a prerequisite
for the graph construction.

## 7. Corrections to the Step 77 PE side result

The Riccati comparison is retained only with its demonstrated scope.  Assuming
a global smooth normal foliation from the reflected center to a PE end,
`H≤3 tanh r` gives the pointwise boundary-representative inequality
\[
 R_\gamma(x)\le-24                                   \tag{7.1}
\]
along each normal ray (for the center-normalized geodesic representative).
Equality at a single boundary point forces vanishing traceless shape only along
that ray.  Preissmann rules out equality **everywhere**, because global equality
would make the center metric Einstein of negative curvature.  Therefore the
safe global statement is `R_gamma≤-24` pointwise and `R_gamma<-24` somewhere;
strictness at every boundary point has not been shown by this argument.

Keep separate
\[
 u_H=3-H,\qquad w=3(1-\tanh r),\qquad z=u_H-w,
\qquad Z=e^{2r}z.                                    \tag{7.2}
\]
Writing `P=S-(H/3)I`, the consistent comparison equation is
\[
 Z'=\frac{u_H+w}{3}Z+e^{2r}|P|^2,\qquad Z(0)=0,      \tag{7.3}
\]
and
\[
 -\frac{R_\gamma}{4}=6+\lim_{r\to\infty}Z(r).       \tag{7.4}
\]
The earlier route-map wording mixed `z` and `Z` and is superseded by (7.2)--(7.4).
These are necessary conditions under the foliation assumption, not an
obstruction to general negative-Yamabe fillings or to finite forced connectors.

## 8. Positive-route placement

For the peer mixed-chirality resolution, standard `#_3(S^2 x S^2)` has
`b_+=3`.  A positive Kähler--Einstein surface is del Pezzo and has `b_+=1`, so
this smooth manifold cannot support a positive KE metric.  Its positive
Einstein question, if pursued, requires a non-Kähler mechanism.  The peer
order-three radial response remains useful as a local desingularization test,
but not as a KE shortcut and not by itself as arbitrary Einstein existence or
nonexistence.

## 9. Evidence

- Symbolic full-Ricci derivation:
  `workspace/scripts/step78_bianchi_vii0_verify.py`.
- Recomputed formulas:
  `workspace/data/step78_bianchi_vii0_symbolic.json`.
- Independent derivation and invariant-region verification:
  `trace/ttcs/results/step78_ttcs01_verifier1_integration.md`.
- Independent strengthening and connector interpretation:
  `trace/ttcs/results/step78_ttcs01_generator1_integration.md`.

This is a controlled benchmark exclusion, not a disproof of the negative branch
or of Yau 26.
