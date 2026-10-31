# The nonabelian uniformization route and its unresolved convention bridge

This note investigates a different route from the integral calibration gap.
The established result is a conditional global reduction using Leung's
uniformization theorem. An explicit rank-one calculation is also preserved,
but its identification with the published nonabelian equation remains
unverified: the matrix identity alone does not fix the dual Clifford sign.
It is not a proved exclusion of that research route and does not prove
that the Dehn-twist bundle has no Einstein metric.

## 1. The global theorem one would actually need to apply

The relevant primary source is N. C. Leung,
[Non-Abelian Seiberg--Witten equations on Einstein manifolds](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf),
J. reine angew. Math. 519 (2000), 17--29, Theorem 1.1 and Section 2.
The published paper, rather than just its abstract or the earlier preprint,
is used here. It fixes a spin-c structure with determinant line L and a
Hermitian connection D_L with harmonic curvature. Set W=S_L^+ and E=W.
The additional data are a Hermitian connection A on E and

\[
 \phi\in\Gamma\operatorname{Hom}(W,E)
       =\Gamma(S^+_{L^{-1}}\otimes E),
 \qquad F_A^+=\tau(\phi),\qquad \mathcal D_A\phi=0.       \tag{1}
\]

Here the Dirac operator uses the fixed background D_L and the variable
connection A. The quadratic map projects on the trace-free part of the
**W factor**; its definition must not be replaced by a different U(2)
monopole equation with a prescribed determinant perturbation.

The cited theorem says that an Einstein metric admitting (1) has
signature at most zero. At signature zero its universal cover is one of
the symmetric spaces R^4, H^4, or H^2 x H^2.

Consequently the following conditional reduction is global, not a
scalar--Weyl numerical test.

**Proposition 1.** Let X be a closed oriented four-manifold with
signature zero which admits no metric of nonpositive sectional
curvature. If every Einstein metric on X supplies the data (1) for
some spin-c structure and harmonic background determinant connection,
then X admits no Einstein metric.

Indeed all three universal covers in Leung's conclusion have
nonpositive sectional curvature. There is no sign assumption on the
putative Einstein constant in this argument.

For the actual Dehn-twist surface bundle E_D, the needed topology is
already established in the supplied construction: its signature is zero,
and its Dehn-twist mapping-torus subgroup obstructs a nonpositively curved
metric. Thus Proposition 1 applies **if the solution hypothesis can be
established**. Equivalently, any Einstein metric on E_D would have to have
empty moduli space for (1), for every allowed L and D_L. This is a
restriction on actual differential solutions, but remains a direct
conditional consequence of the cited theorem, not a new existence result
for a gauge-theoretic invariant.

## 2. The rank-one temptation

Let L now be the determinant of the canonical spin-c structure of an
almost-complex four-manifold. Its positive spinor bundle has a smooth
unitary splitting

\[
                        W\simeq\mathbb C\oplus L.        \tag{2}
\]

More generally c2(W)=(c1(L)^2-2 chi-3 tau)/4, so the canonical square
c1(L)^2=2 chi+3 tau supplies the same topological splitting. This
splitting need not be parallel for the Levi--Civita spin connection.

An ordinary Seiberg--Witten solution is a determinant connection B on L
and a spinor psi in W. Normalize the ordinary quadratic map q so that

\[
          \mathcal D_B\psi=0,\qquad F_B^+=q(\psi).       \tag{3}
\]

A positive conventional factor in q can be absorbed into the spinor
normalization. The determinant curvature in (3) is not the curvature
of an auxiliary twisting line with half the determinant charge.

There is a canonical complex-linear identification

\[
 j:W\longrightarrow\operatorname{Hom}(W,L),\qquad
                  j(v)(w)=v\wedge w.                    \tag{4}
\]

Using (2) on the target E, put the homomorphism j(psi) in its L summand
and put zero in its trivial summand. Equip the latter with a flat
connection. This is the direct rank-one proposal for (1).

There are two independent pieces to check: the charge in the Dirac
operator and the sign of the quadratic map. Both matter.

## 3. Exact algebra for an explicitly defined projection model

Work in a unitary frame of W and its determinant frame. For
v=(a,b)^T, (4) is the row (-b,a). Its Hermitian adjoint satisfies

\[
 (jv)^*(jv)=|v|^2 I-vv^*,\qquad
 \big((jv)^*(jv)\big)_0=-(vv^*)_0.                       \tag{5}
\]

The same identity is valid in every unitary frame, including the U(1)
determinant action. For a purely Hermitian tensor identification, a row
alpha=sum alpha_i e^i gives
alpha tensor bar(alpha) in W* tensor bar(W*). The Hermitian metric
identifies bar(W*) with W; exchanging the two factors to form End(W)
gives the matrix with row j, column i equal to bar(alpha_j) alpha_i,
which is precisely alpha* alpha, not alpha alpha*.

Now **define a model map** Q_lit by converting this trace-free Hermitian
matrix with exactly the same fixed map that converts (psi psi*)_0 to
q(psi) in (3). On the active target line this definition gives

\[
                         Q_{\rm lit}(j\psi)=-q(\psi).   \tag{6}
\]

Equation (6) is a definition-level consequence of (5). It is **not** an
established identification Q_lit=tau for the published system (1).
In particular, passing between the dual spinor Clifford action and the
original spinor action can introduce a further sign; Section 4 explains
why this is an actual unresolved step, not an optional convention choice.

Let A_1 be the connection on the active L summand. On
S^+_{L^{-1}} tensor L its determinant connection is

\[
                              B'=2A_1-D_L.               \tag{7}
\]

Indeed its central spin connection is -D_L/2+A_1=B'/2.
The natural choice matching the induced spin-c connection to that in (3)
is therefore

\[
                         A_1=(B+D_L)/2.                 \tag{8}
\]

The average of these two connections on the same line is a globally
defined connection on that line. For the explicitly defined equation
F_A^+=Q_lit(phi), (6) and (8) give

\[
       \frac12(F_B^++F_{D_L}^+)=-q(\psi)=-F_B^+.         \tag{9}
\]

Let h be the harmonic self-dual representative of 2 pi i c1(L).
Both curvatures on the left have harmonic self-dual projection h.
Projecting (9) onto harmonic forms gives h=-h. Hence h=0.

**Proposition 2 (the literal-projection model only).** If
(c1(L)^+)^2>0, an ordinary solution (3) cannot, by (4), (8), and a flat
complementary line, solve F_A^+=Q_lit(phi). The same holds after any
nonzero constant rescaling of the spinor. This proposition does not
assert the same statement for Leung's system (1).

For the rescaled spinor the projected equation is h=-c h with c>0,
which is equally impossible. This obstruction does not assume that
the metric is Einstein. In particular it applies to the canonical
monopole on E_D for every metric: its square is T=2 chi(E_D)>0,
and its positive projection has square at least T.

The same calculation also obstructs an approximate solution of this
model equation. In the normalization of (6), set phi=t j(psi), t real,
and keep (8). Its model Dirac residual vanishes, but its curvature residual
R=F_A^+-Q_lit(phi) has harmonic projection (1+t^2)h on the active line.
Consequently, with the usual Hermitian Hilbert--Schmidt norm,

\[
 \boxed{\quad
  \int|R|^2\ \ge\ 4\pi^2(1+t^2)^2(c_1(L)^+)^2.
 \quad}                                                   \tag{10}
\]

For the actual Ric approximately -g family on E_D, whose volume is
V_*=2 pi^2 T, this gives the normalized average lower bound
V_*^{-1} integral |R|^2 >= 2(1+t^2)^2. Thus this rank-one ansatz
does not become a small-error seed for the explicitly defined model as
the Ricci defect tends to zero. This is not yet a bound for the
published nonabelian equation.

This proposition addresses the direct construction, not every possible
rank-one solution of a perturbed or differently normalized system.
An arbitrary alteration of A_1 need not preserve the given harmonic
spinor, and would itself require solving a new coupled Dirac equation.
Nor does the calculation assert that every nonabelian solution splits.

## 4. Why the published sign cannot be inferred from (5)

On a dual representation, the infinitesimal action of a matrix K is
-K^T, not K^T. Accordingly the even Clifford action on the dual spinor
must be matched with that sign. The matrix identity (5) establishes a
relative sign between two Hermitian endomorphisms; it does not by itself
identify which Hermitian-to-two-form maps the author uses on the two
spinor representations.

There is a concrete primary-source warning. In Leung,
[Seiberg Witten invariants and uniformizations](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/591-1996_Leung_SW_inv__Uniformization_Math_Annalen.pdf),
Math. Ann. 306 (1996), 31--46, printed page 40, the connection A is on
the canonical line K, the spinor lies in S_+ tensor K^(-1/2), and the
displayed equation uses F_A^+=phi bar(phi). The spinor determinant is
K^(-1), not K. Thus that notation already requires a sign comparison
before it can be identified with (3). The 2000 paper invokes this
earlier construction. Its sentence about projection on the original
W factor is not enough, on its own, to settle the comparison.

For clarity the two possible comparisons have different consequences.
If the actual active-line map is -q, the induced equation is

\[
        \mathcal D_B\psi=0,\qquad
             F_B^+=-2q(\psi)-F_{D_L}^+.                 \tag{11}
\]

This changes the quadratic sign and usual perturbation persistence does
not apply. If instead the actual map is +q, it gives

\[
             F_B^+=2q(\psi)-F_{D_L}^+.                  \tag{12}
\]

The latter has the usual quadratic sign and a prescribed perturbation.
For an ordinary unperturbed solution and unit spinor scaling, the direct
curvature residual in this alternative model is
(F_{D_L}^+-F_B^+)/2, whose harmonic projection is zero. It is therefore
incorrect to use (5) alone to claim the positive residual bound (10)
for every natural nonabelian convention.

There is also a useful consistency test. An automatic transfer of all
canonical monopole solutions into the precise hypotheses of Leung's
theorem would force every canonical-monopole Einstein four-manifold
to have nonpositive signature. Compact complex-ball quotients have
negative Kahler--Einstein metrics, canonical solutions, and positive
signature. Hence some sign, determinant-connection, or other equation
compatibility in such a universal transfer must fail. This test does
not prove which compatibility fails and does not resolve the comparison
for E_D.

There is also no general operation that combines the two ordinary
monopoles of opposite orientations into a solution of (1): their Dirac
bundles have different chirality, while (1) requires a single connection
and a coupled quadratic equation in one fixed chirality. A proposed
construction of this sort must verify those equations, not just their
Chern classes.

The missing input in Proposition 1 remains an actual
rank-two solution of the precise system (1), for every putative Einstein
metric on the actual bundle. A topologically nonzero invariant known to
force these particular solutions would suffice. Neither the ordinary
SW/Bauer--Furuta classes already used in the integral gap nor the
convex-hull/polarization invariant supplies this implication here.
Leung's published Remark 1.2 itself separates a hoped-for invariant
from the analytic solution hypothesis.

## 5. Scope and verification

The established calculation is the cohomological obstruction in the
explicit model Q_lit, and the useful global reduction is Proposition 1.
Identification of that model with Leung's equations is pending. Thus no
failure of the genuine nonabelian route has been proved here, and no
integral threshold has been improved from 2/3 to 1 or to 3/4.
The genuine near-Einstein sequences on E_D already prevent a universal
positive Ricci-energy gap on that fixed topology, as explained in
[round5_rigidity.md](round5_rigidity.md), Section 5. No replacement of
those actual sequences by numerical witnesses is made here.

[round7_rigidity_check.py](round7_rigidity_check.py) verifies (5), its
unitary-frame covariance, the determinant-charge identity (7), the
model harmonic projection obstruction, and the sign-reversed alternative.
These are algebra checks only. They do not verify the cited global
uniformization theorem, identify its absolute Clifford convention, or
establish existence of a nonabelian solution.
