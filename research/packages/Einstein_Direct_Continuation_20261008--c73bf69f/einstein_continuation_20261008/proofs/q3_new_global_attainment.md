# Q3: conformally reduced stability and the unresolved attainment step

The target remains a smooth closed global minimizer of `P(g)=integral |Ric°|²` with nonzero Bach tensor. This continuation does not construct one. It adds an exact stability test coupling an unrestricted metric change with its optimal first-order Yamabe correction. It does not add a compactness hypothesis or identify another functional's minimizer with a P-minimizer.

Read: `new_global_variation.md`, `new_q3_global.md`, `q3_variational_structure_current.md`, `q3_global_boundary_current.md`, `q3_global_compactness_current.md`, and the normalized/conformal sections of `upload/03_Subsequent_Mathematical_Developments.tex`.

## 1. An exact reduced-Hessian formula

Let g be a smooth closed P-critical four-metric with constant scalar s<0. Set E=Ric°, let L=-div grad be the nonnegative scalar Laplacian, and denote the unrestricted P-Hessian by H. All inner products below are integrated with the fixed metric g. No Bach normalization is needed.

For a transverse-traceless symmetric tensor h, set

    a=<E,h>,    a0=a-average(a).

Define the smooth mean-zero function

    f_h=(6L-2s)^(-1)a0.

The inverse exists because s<0. Then

    H(h+2 f_h g, h+2 f_h g)
       = H(h,h)-<a0, L(6L-2s)^(-1)a0>.                 (1)

In fact the right side is the minimum of `H(h+2fg,h+2fg)` over all smooth conformal corrections f, modulo constants. The same correction makes the scalar-curvature variation constant:

    s'[h+2 f_h g]=-average(a).                          (2)

Thus (1) is the actual Hessian in the negative-Yamabe slice, not a merely formal combination of unrelated variations.

### Proof

The four-dimensional identity `P=2W+S/12-16pi²chi`, with W the full operator-norm Weyl energy and S=integral s², and conformal invariance of W give

    DP_g[2fg] = integral s Lf.

At a critical metric s is constant. Differentiating this identity in h, the variations of the operator and volume cancel because `integral Lf=0` for every metric. Therefore

    H(h,2fg)=integral s'[h] Lf.

The transverse-traceless scalar variation is `s'[h]=-<E,h>=-a`, so the mixed Hessian is `-<a,Lf>`.

For `g_t=e^(2tf)g`, the exact scalar transformation gives

    H(2fg,2fg)=6||Lf||²-2s< f,Lf>.

Writing A=6L²-2sL, expansion gives

    H(h+2fg,h+2fg)=H(h,h)-2<a,Lf>+<f,Af>.

On mean-zero functions, `Af_h=L a0`; completing the square proves (1). The scalar variation of the conformal direction is `(6L-2s)f_h`; this gives (2).

Since negative unit-volume Yamabe metrics form a smooth slice through the conformal classes, this tangent vector is realized by a smooth Yamabe-normalized path. At a P-critical metric, acceleration of that path does not change its second variation. The source for this classical slice property is M. Anderson, *On uniqueness and differentiability in the space of Yamabe metrics*, arXiv:math/0210446, opening discussion: https://www.math.stonybrook.edu/~anderson/yamabe.pdf .

## 2. Consequence in the genuine traceless-Ricci direction

Contracted Bianchi makes E transverse-traceless when s is constant. Put

    q=|E|²,    q0=q-average(q).

Every smooth local P-minimum of negative scalar curvature must satisfy

    H(E,E) >= <q0,L(6L-2s)^(-1)q0>
           >= lambda1/(6lambda1-2s) * ||q0||².          (3)

Here lambda1>0 is the first nonzero scalar eigenvalue of the fixed closed connected metric. Thus nonconstant Ricci-defect density requires a strictly positive Hessian in the E direction. If an independently calculated critical candidate has

    H(E,E) < <q0,L(6L-2s)^(-1)q0>,

then the explicitly given direction `E+2(6L-2s)^(-1)q0*g` decreases P at second order and excludes that candidate from Q3.

The spectral bound is exact: on an eigenfunction of L with eigenvalue lambda, the correction term has multiplier `lambda/(6lambda-2s)`. It lies strictly between 0 and 1/6 and increases with lambda. The calculation does not establish a sign for `H(E,E)` itself. That missing sign cannot be replaced by P-criticality or scalar negativity.

This is a necessary stability inequality, not a new sharp topological lower bound and not an attainment theorem. It provides a concrete test for a future critical construction; it does not exclude all non-Einstein critical metrics.

## 3. Why this does not yet repair the global existence argument

The fixed Godeaux candidate has a real A1 degeneration with zero-P Eguchi–Hanson loss below the strict Burns upper threshold. That construction is already in `q3_global_boundary_current.md`. Consequently a scalar/Weyl bound and `P<8pi²` do not give smooth precompactness. The new Hessian identity concerns a smooth critical point and cannot be applied by assuming one exists.

Anderson's ideal-minimizer theorem can produce singular/collapsed limits rather than a smooth minimizer. The reduced Hessian neither identifies their topology nor supplies a strict comparison with them. The negative Yamabe slice is smooth locally at an existing smooth metric; its existence is not completeness of the space of conformal classes.

An aspherical base removes the embedded (-2) and (-3) sphere channels for a single blowup, as the previous topology note proves. But the available such negative-KE bases do not give a known Einstein obstruction after only one blowup. Enlarging the blowup number restores the obstruction while reopening spherical root channels. No alternative topology with both the required Einstein exclusion and a proved compactness theorem was obtained in this investigation.

## 4. Exact status

No matching unrestricted calibration with a non-Bach-flat equality metric was found. No smooth-attainment theorem was proved on the fixed candidate or an alternate manifold. The new complete calculation is (1)–(3), which optimizes the full mixed conformal/TT stability test instead of testing the E direction alone. Q3 remains open in this continuation.

The mathematical requirement for a positive resolution has not changed: produce an actual smooth global minimizer, either through an unrestricted sharp bound with an explicit equality metric or through a proved comparison excluding every relevant singular/collapsed minimizing alternative. The present note supplies neither and makes no claim to do so.

## 5. All-metric actual supply on the rational-ball contraction orbifold

The gluing estimates in `q2_exact_infimum_new.md` give a stronger transfer statement than the earlier convergence formulation. It is intrinsic to the contraction orbifold: no constant-scalar minimizing sequence, prior geometric limit, neck energy identity, or convergence of Hodge projections is required.

**Proposition.** Let `M=X#CPbar²`, with `A=c1²(X)>0`, and suppose both sign classes `a_±=K±E` have unperturbed actual SW solutions for every smooth metric on M. Let O be the orbifold obtained by replacing an embedded reversed rational ball `-B₂` with its standard cone of group Z4. Then the restrictions of both sign classes extend to actual orbifold SW classes for every smooth orbifold metric on O. Every such metric h satisfies

    P(h) >= 8pi²(4-A/3).                              (4)

Consequently if `A<=9`, the entire smooth metric space of this orbifold has `P>=8pi²`. In particular it cannot be the smooth compact orbifold bulk of a sequence with `limsup P<8pi²`, because the nonnegative P density is lower semicontinuous on its regular part.

### Smooth approximation of an arbitrary orbifold metric

Fix an arbitrary smooth orbifold metric h on O. In a uniformizing geodesic chart it has expansion `h=delta+h_0`, with

    |D^m h_0| <= C_h r^(2-m),     m=0,1,2.

The reversed Eguchi–Hanson/Z2 metric is Ricci-flat and has ALE order four. At length scale a, its end metric is `delta+h_N`, with

    |D^m h_N| <= C a^4 r^(-4-m), m=0,1,2.

Choose the matching radius `r_a=a^(1/2)`. On the annulus use

    g_a=delta+chi h_N+(1-chi)h_0,

with a radial cutoff having `|D^m chi|<=C r_a^(-m)`. The pointwise curvature estimate is

    |Rm(g_a)| <= C_h(1+a^4 r_a^(-6)) <= C_h(1+a).

Positivity follows from the corresponding zeroth-order closeness. On the inner core g_a is exactly the scaled Ricci-flat metric, so its scalar curvature is zero despite its possibly large Weyl curvature. Outside the chart it is h. Thus the resulting smooth metrics on the original M have a uniform lower scalar bound and a uniform volume bound. They converge smoothly to h on each compact subset of the orbifold regular set.

This construction works for every fixed h. Constants may depend on h; all-metric supply on O does not require a constant uniform over all orbifold metrics.

### Passing the actual fields and removing the quotient point

Choose actual unperturbed SW solutions for each a_± on g_a. The scalar lower bound gives a uniform maximum-principle bound on the spinors. The curvature equation, the volume bound, and

    integral(|F+|²-|F-|²)=4pi² a_±²

bound the full determinant curvature in L². The integrated Weitzenböck identity also bounds the covariant derivative of the spinor in L². Coulomb gauge and local elliptic regularity give subsequential convergence on every compact subset of the regular bulk. There are only two classes, so the two limits can be taken simultaneously.

On the uniformizing punctured four-ball, pull back a limiting solution. Finite curvature energy and bounded spinor permit a gauge with the connection in W^(1,2). The point has zero W^(1,2) capacity, so the equations extend distributionally. In Coulomb gauge, the elliptic operator `d*+d+` has bounded right side `q(Phi)` (plus smooth reference-connection terms). Local elliptic regularity and the Dirac equation then bootstrap both fields to smoothness. The finite group action extends with its induced spin^c lift and determinant character. No trivial isotropy assumption is made.

The real determinant classes are fixed by their restrictions to the regular bulk. One may fix compatible orbifold spin^c extensions throughout the statement; discrete local isotropy choices, if present, do not change the real classes used in the curvature estimate. In particular the same procedure applies to every metric in a given orbifold conformal class, supplying the quantifier needed in LeBrun's mixed inequality.

### Projection budget on the orbifold

Both B₂ and its cone replacement have zero real H², while their common lens boundary is a real homology sphere. Mayer–Vietoris identifies the real second cohomology and its intersection pairing on M and O. Hence

    K_O²=A,    E_O²=-1,    K_O.E_O=0.

With the Hodge decomposition of any fixed orbifold metric,

    ( |(K_O+E_O)^+|²+|(K_O-E_O)^+|² )/2
      = |K_O^+|²+|E_O^+|² >= A.

At least one actual class has projection square at least A. This is a new calculation on the bulk Hodge decomposition, so no prelimit harmonic-projection convergence is needed.

### Curvature lower bound

The reversed Ricci-flat quotient has operator-curvature integral `6pi²`, entirely in W+. Its Euler and signature curvature contributions are `3/4` and `1/2`. Thus the orbifold Chern–Weil quantities satisfy

    chi_orb=chi(M)-3/4,
    tau_curv,orb=tau(M)-1/2,
    T_curv,orb=2chi_orb+3tau_curv,orb=A-4.

Here `tau_curv,orb` is the signature curvature integral, not the signature of the real intersection pairing. The isolated-point correction remains explicit.

LeBrun's mixed estimate applies on a smooth compact orbifold through the same integrated Weitzenböck and conformal argument in invariant charts. The all-metric actual supply just proved yields

    P(h) >= 8pi²[(2/3)A-T_curv,orb]
          =8pi²(4-A/3).

This proves (4). It is an intrinsic estimate for every h, stronger than an estimate conditioned on h appearing as a minimizing limit.

For a reversed Ricci-flat cyclic rational-ball quotient of end order d², d>=2, the same conclusion holds whenever the quotient has the differentiated ALE order-four expansion used in the gluing above. The characteristic contribution is `4(1-1/d²)`, and the lower bound becomes

    P(h) >= 8pi²[5-A/3-4/d²] >=8pi²(4-A/3).

The ordinary ASD orientation contributes zero to T and is not excluded by this calculation. Partial collapse, nonsmooth orbifold limits, and general Ricci-flat ALE spaces outside the stated quotient class are also not covered.

Primary classical input checked: C. LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg-Witten Theory*, arXiv:math/0003068, Proposition 2.3 and Proposition 3.1, https://arxiv.org/pdf/math/0003068 . The actual conformal supply requirement is explicit in that proof. The present transfer derives that supply from the original smooth all-metric hypothesis and the scalar-controlled reconstruction.
