# Yau 26: a parallel research round

**Latest continuation:** [Round 6: a larger repair obstruction and a charged
Einstein neck](round6.md). It excludes a fixed linear-size neighbourhood of
exact repairs on the closed bundle, constructs an actual charged Einstein
neck and complete one-ended charge-removal metrics, and tests entropy on a
specific simply connected hyperbolic-orbifold resolution.

[Round 5: global receivers, construction
compatibility, and connector geometry](round5.md). It excludes critical-scale
exact repairs on the closed surface bundle, compares actual constructions
with the monopole gap, and derives a sharp nonpositive-sectional-curvature
connector obstruction without a symmetry assumption.

[Round 4: integral rigidity, nonlinear charge,
and global matching](round4.md) removes pointwise curvature assumptions
from the monopole gap, derives a nonlinear boundary law for the exact
Einstein family, and proves precise obstructions to two forms of global
completion.

[Round 3: intrinsic near-Einstein gap and exact model completion](round3.md)
provides the preceding pointwise gap and complete Einstein family.

[Round 2: weak curvature transfer, complete model corrections, and twisted
connectors](round2.md) and the original round below are retained as their
mathematical predecessors.

19 September 2026. Mathematical notes and executable calculations for the
rigidity, construction, and global-existence questions. The existing Skill
was read as research input; its manuscripts, running Sessions, and services
were not modified.

## The problem being advanced

Write
\[
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad \sigma\in\{+1,-1\}.
\]
For each dimension, the working Yau26 statement asks for a dimension-only
Ricci interval forcing the **same smooth closed manifold** to admit some
Einstein metric. The output need not be close to the input or have the same
Einstein sign. A complete affirmative argument must cover every dimension;
a complete negative argument can defeat both normalized branches in one
fixed dimension, using different manifolds for the two branches if needed.

This round does not settle either unrestricted four-dimensional branch.
It obtains explicit restricted results and identifies exactly which extra
geometric information the attempted connections require. The claims below
are mathematical deductions in the accompanying notes; their publication
novelty has not been established by a comprehensive literature comparison.

## 1. Rigidity: a quantitative forbidden spectrum and the limit of a direct method

[The rigidity note](rigidity.md) proves that a closed oriented four-metric
with scalar curvature \(s=-4\) and \(\operatorname{div}W^+=0\) cannot have
all its ordered self-dual Weyl eigenvalues within \(10^{-4}\) of
\[
(-1/6,1/12,1/12)
\]
at every point. The argument is an explicit differential inequality, rather
than a compactness argument. Put \(x=|W^+|^2\), \(y=\det W^+\), and
\[
f=x+36y+24(x-1/24)^2.
\]
The classical harmonic-Weyl equations give \(\Delta f\ge1/32\) throughout
that spectral box. Integrating on a closed manifold is impossible. The
derivative matrix, its positive margin, and the radius estimates are given
explicitly, with an independent reconstruction from the eigenvalue equations.

The same investigation proves a limitation on a proposed extension: no
globally \(C^2\), orthogonally invariant scalar function of \(W^+\) can have
both a nonnegative derivative quadratic form on every admissible
harmonic-Weyl first jet and a positive reaction at this target spectrum.
On the negative repeated-eigenvalue ray, these demands would require
\((u^{2/3}\psi'(u))'\ge0\), smoothness at zero, and \(\psi'(u_0)<0\),
which are incompatible.

This does not exclude coupled equations or controlled-error arguments.
It explains why simply extending the local multiplier to a globally
sign-definite one cannot close the average-density gap. An actual metric
perturbation in the note also has Ricci defect tending to zero and uniformly
bounded full curvature, while its Cotton energy diverges. Small residual
alone therefore does not control the derivative source needed in the
non-Einstein Weitzenbock identity.

**Remaining mathematical connection:** force enough of a near-critical,
possibly collapsed near-Einstein metric into a region where the local
inequality applies, while controlling the complementary derivative and
concentration costs. A pointwise exclusion is not yet a mean-density bound.

### An improved explicit gap above the critical topology ratio

[A second calculation](fixed_ratio.md) jointly optimizes the Ricci and
Weyl variables in the monopole/Chern--Weil inequalities. For the specified
blow-up family, put \(p=k/c_1^2(X)\). If \(1/3<p<1\), every metric satisfies
\[
\delta_-(g)\ge
\begin{cases}
\sqrt{(3p-1)/(p+5)},&p\le2\sqrt3-3,\\
\bigl(\sqrt{(3p-1)(3p+15)}-(3p-1)\bigr)/8,&p\ge2\sqrt3-3.
\end{cases}
\]
For example, at \(p=1/2\) the bound is approximately \(0.296535\), improving
the previously used \(0.224009\). This follows from the classical monopole
input and does not depend on the unpublished exact-Einstein uniform-gap
proof. As \(p\downarrow1/3\), the bound still tends to zero like
\((3/4)\sqrt{p-1/3}\); it does not solve the critical or below-critical case.

## 2. Construction: base-moduli drift does not remove the third-order source

[The construction note](construction.md) works on the balanced \(E_D\)
surface-bundle family already in the Skill. It retains the manuscript's
global TT test-tensor and adjoint estimates as explicit inputs.

For an arbitrary base TT tensor \(k\), set \(B=\pi^*k\), keeping the fibre
metric path fixed. The horizontal Ricci identity is
\[
(\operatorname{Ric}_{b'+h}+b'+h)_{HH}=(K(b')+1)b'-T,
\]
where \(T\) does not depend on \(b'\). Since \(DK_b(k)=0\) and the fixed
test tensor is trace-free, **both the first and second projected variations
vanish for every base TT direction**, not just one symmetric trial tensor.

For a perturbation \(B+r\), with geometric \(C^2\) sizes \(a,z\), the
projected change obeys
\[
|P(B+r)-P(0)|\le C\beta(\varepsilon^2z+a^3+az+z^2),
\qquad \beta=\varepsilon^2.
\]
Consequently, if \(a=O(\varepsilon^{3/2})\) and
\(z=o(\varepsilon^{3/2})\), or if \(a=o(\varepsilon)\) and
\(z=O(\varepsilon^2)\), then
\[
\liminf_{\varepsilon\to0}
\frac{\delta_-(G_\varepsilon+B+r)}{\varepsilon^3}
\ge\frac1{16\pi^4(p-1)},
\]
where \(p\) is the fibre genus. This is an explicit lower bound, not an
assertion that equality is attainable. The Ricci Taylor estimates are
tensorial and do not introduce an inverse injectivity-radius factor.

**Remaining mathematical connection:** identify all admissible leading
directions outside base TT, solve the full complement equation, and retain
its contribution to the nonlinear obstruction. The exact reduced equation
is written in the note. A trial-mode eigenvalue or a small residual is not
a substitute for that equation. The result does not exclude distant or
otherwise unrestricted Einstein metrics on \(E_D\).

## 3. Global determination: a stronger geometric budget, and a precise feasible set

[The global note](global.md) constructs simultaneous algebraic curvature
data satisfying the presently available two-orientation monopole, volume,
energy, and signature constraints for a hypothetical Einstein metric on
\(E_D\). The example can have distinct Weyl eigenvalues and positive
sectional curvature on part of the algebraic distribution. Thus these
constraints alone do not empty the known necessary volume interval.
The data are not a metric construction; they identify the limitation of
this proposed inequality-only exclusion.

[The curvature-box calculation](curvature_box.md) optimizes the full Ricci
eigenvalue box before using Chern--Gauss--Bonnet. If
\(\delta_-(g)\le d\le1\), then
\[
\frac{s^2}{24}-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
\ge
\begin{cases}
\frac23(1-d)^2,&0\le d\le1/3,\\
\frac23(1+d)(1-2d),&1/3\le d\le1.
\end{cases}
\]
These are sharp algebraic bounds; no closed equality metric is asserted.
One consequence is the strict Hitchin--Thorpe inequality whenever
\(\delta_\sigma<1/2\), for either sign.

For a smoothly matched connector replacing cusp volume, retain an exact
hyperbolic exterior and the reference Euler budget. Let
\(w=\fint_N|W|^2\), \(r=V_{\rm rem}/V_N\), and normalize the defect by
\(\epsilon=\|g^{-1}\operatorname{Ric}+3I\|_\infty\).
If geometry supplies \(w\ge w_0\) and
\(r\le1+w_0/6-\kappa\), \(0<\kappa\le1\), then
\[
\epsilon\ge
\begin{cases}
3(1-\sqrt{1-\kappa}),&\kappa\le5/9,\\
(\sqrt{9+72\kappa}-3)/4,&\kappa\ge5/9.
\end{cases}
\]
The lower bound is independent of cover degree. Its additional geometric
hypothesis is essential: the global note exhibits compatible concentration
data when no positive \(\kappa\) is available. Preserving an unrescaled AH
core to distance \(R\) also forces an explicit Euler-characteristic cost of
order \(e^{3R}\).

**Remaining mathematical connection:** prove a positive normalized
volume/Weyl cost for actual connectors, or construct connectors that avoid
it while satisfying every Ricci block and the same end-lattice data. For
\(E_D\), a new differential or monodromy-sensitive restriction is needed;
the current scalar numerical constraints give no contradiction.

## What this changes for the next research round

The three investigations have reduced three broad suggestions to specific
mathematical tasks: control the derivative cost of leaving the forbidden
spectral neighbourhood; determine the full non-base-mode correction on
\(E_D\); and prove or evade a geometric connector cost. None of these tasks
is replaced by additional precision in the existing finite calculations.
Other constructions and methods remain available; these are the missing
connections located by this round, not a classification of all possible
approaches to Yau26.

## Reading and reproduction

- [Rigidity derivations](rigidity.md), [independent reconstruction](rigidity_review.md).
- [Optimized fixed-topology-ratio gap](fixed_ratio.md).
- [Construction derivations](construction.md), [independent review](independent_review.md).
- [Global inequalities and algebraic witnesses](global.md).
- [Exact curvature-box optimization and connector bound](curvature_box.md).
- [Execution record and reproducible commands](verification.md).

The original Skill remains at
`/data/qiushi/qiushi_engine_v09/users/user2/Skills/qiushi-yau26/`.
Its manuscript arguments are research inputs, not conclusions independently
re-proved in full by this round's algebraic tests.
