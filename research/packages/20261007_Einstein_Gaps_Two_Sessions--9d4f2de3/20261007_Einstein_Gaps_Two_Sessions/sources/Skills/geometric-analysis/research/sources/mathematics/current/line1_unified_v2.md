---
title: "Integral Einstein obstruction and curvature-functional stability"
subtitle: "First-line synthesis after polarized closure"
date: "23 September 2026"
fontsize: 11pt
geometry: margin=1in
header-includes:
  - \usepackage{mathrsfs}
  - \usepackage{esint}
  - \setmathfont{Asana Math}
  - \setlength{\emergencystretch}{3em}
---

# Mathematical center

The first research line now contains two distinct questions:

1. Which topology prevents the Einstein residual from tending to zero,
   even when the geometry degenerates?
2. What geometric information survives when a sharp curvature functional
   approaches its minimum?

The existing integral calibration proof answers the first in an actual
monopole category. The second must retain the full equality set of the
functional being studied. For LeBrun's Proposition 4.1 this is the
compatible constant-scalar-curvature Kähler set, not merely the Einstein
set. The two questions meet through the primitive part of the Chern class
and the topology of the manifold; they are not interchangeable.

This synthesis replaces the *current-status guidance* in the uploaded
September 22 literature note. It preserves that note, its 37 references,
and the correction as original sources. It does not replace the original
analytic proofs. The present increment consists of a scalar-band
remainder argument, its Kähler controls, and a corrected connection to
the original problem.

# The working Yau26 statement

The project uses the following working formulation: in each dimension,
does an appropriate dimension-only pointwise Ricci pinching condition
force the underlying closed smooth manifold to admit some Einstein
metric? The output need not resemble the input, preserve a complex
structure, or have the same Einstein sign.

For the sign-normalized formulation, let
\[
e_\sigma(M)=\inf_g\|g^{-1}\operatorname{Ric}_g-\sigma I\|_\infty,
\qquad
\Delta_n^\sigma=\inf_{M\in\mathcal N_n}e_\sigma(M),
\]
where \(\mathcal N_n\) is the class of closed smooth \(n\)-manifolds with
no Einstein metric of any sign. The project asks whether, for each \(n\),
at least one of \(\Delta_n^+,\Delta_n^-\) is positive. A negative answer
needs both to vanish in the same dimension; the witnesses may have
different smooth types and may vary along sequences.

This is the project's fixed formulation, not a new verification of the
historical problem's wording. Integral error cannot replace its
pointwise input: [Round 18](round18_integral_limits.md) constructs
varying no-Einstein manifolds with bounded local geometry and vanishing
averaged error, while their maximum error stays positive.

# Inherited results and their proof ownership

## Polarized closure is written, not a fresh task

Let
\[
T_X=2\chi(X)+3\tau(X)>0,\quad
M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),\quad
D_{\rm top}=k+4\ell.
\]
Under the nonzero Seiberg--Witten invariant and chamber hypotheses of
[the closure manuscript](lebrun_stability_closure.md), the proof chooses
an actual Spin\(^c\) structure at each polarization:
\[
\forall g\ \exists a_g\ \forall f>0.
\]
The same chosen structure supports every smooth positive auxiliary
weight. Exceptional generators are signed at that polarization, not
fixed once for all metrics. Their projection and square satisfy
\[
(a_g^+)^2\ge A=c^2\ge T_X,\qquad a_g^2=A-k\ge T_M.
\]
The conformal invariance of the self-dual splitting and the weighted
equation are proved explicitly there, including the applicable
\(b_+=1\) case.

Conditional on the precisely stated integral calibration lemma of
[Round 4](round4_rigidity.md), the closure obtains
\[
\mathcal E(g)+
\left(\frac13-\frac{D_{\rm top}}{T_X}\right)_+
\ge\varepsilon,\qquad
\varepsilon=\min\left\{\frac14,\frac{c_{\rm cal}}{1215}\right\}>0.
\tag{1}
\]
Here
\[
\mathcal E(g)=
\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}.
\]
The dependence on the core analytic lemma is not removed by writing the
application proof. That lemma remains supported by its original
Hessian, weighted-monopole, and weak-Bianchi arguments.

For non-Ricci-flat Einstein metrics, \(\mathcal E=0\). For Ricci-flat
metrics, \(\mathcal E=4\), so their exclusion instead uses
\[
\int s_-^2\ge32\pi^2(a_g^+)^2\ge32\pi^2A>0.
\]
Taking a smaller closed threshold, such as \(\gamma=\varepsilon/2\),
handles the endpoint. The minimal general-type blow-up application
includes \(b_+=1\). The positive-budget version of the classical
connected-sum obstruction is included too; \(T_X=0\) is not included
by division, and the Ricci-flat K3 corner must survive.

## The independent spectral criterion

For a bounded self-dual form \(\psi\), write
\[
A_{\psi,t}=t\left(\frac{|\psi|^2}{3}I-\psi\otimes\psi\right),\quad
B=\fint|\Delta_H\psi|^2,
\]
\[
d=\fint\left(
|\operatorname{Ric}-\sigma g|^2+
|W^+-A_{\psi,t}|^2+(|\psi|^2-2)^2\right).
\]
[Round 21](round21_analytic.md) supplies the constant-parameter
compatibility estimate
\[
\operatorname{dist}\bigl(t,\{0,-\sigma/2\}\bigr)^2
\le C(K,T_0)(1+B)d,\qquad |\psi|\le K,\quad |t|\le T_0,\quad d\le1.
\tag{2}
\]
The zero root controls only \(W^+\); the nonzero root is the
Kähler--Einstein model. The relevant smallness is the joint quantity
\((1+B)d\), not \(d\) alone. A supplied form with
\(B=o(d^{-1})\) is sufficient for spectral selection. A topology label
or a formal cohomology class does not supply this form.

The two older mechanisms remain separate. Round 4 treats an impossible
calibration near the monopole topological boundary. Round 17 treats a
realizable Kähler calibration using scalar-energy slack, Ricci error,
and a topological remainder. Neither is newly discovered here.

# Correct defects and equality models

Set
\[
p=(a_g^+)^2,\quad T=2\chi+3\tau,\quad
R_2=\int|\operatorname{Ric}|^2,\quad
P=\int|\operatorname{Ric}^{\circ}|^2,\quad
L=\int(s-\bar s)^2.
\]
Use the Hilbert--Schmidt norm of \(W^+:\Lambda^+\to\Lambda^+\), and put
\[
\mathscr D=
\frac1{4\pi^2}\int\left(\frac{s^2}{24}+\frac{|W^+|^2}{2}\right)-\frac p2.
\tag{3}
\]
In the actual polarized monopole category \(\mathscr D\ge0\).
LeBrun's equality statement at \(p>0\) is compatible negative cscK,
not Einstein. At \(p=0\), the direct numerical equality condition is
\(s=W^+=0\); no nonzero-spinor normalization is available there.

For two surface factors of curvatures \(-\alpha,-\beta\),
\[
s=-2(\alpha+\beta),\qquad
|\operatorname{Ric}^{\circ}|^2=(\alpha-\beta)^2,\qquad
\mathscr D=0
\]
for the compatible canonical Spin\(^c\) structure. Thus no positive
multiple of \(P\) can be bounded by \(\mathscr D\) alone.

Chern--Weil gives the exact classical identities
\[
R_2-8\pi^2(2p-T)=32\pi^2\mathscr D,
\tag{4}
\]
and, whenever \(p\ge A\),
\[
R_2-8\pi^2(2A-T)
=32\pi^2\mathscr D+16\pi^2(p-A).
\tag{5}
\]
In the minimal general-type blow-up/handle setting,
\(T=A-D_{\rm top}\). Formula (5) then measures excess above
LeBrun's absolute Ricci-energy infimum. It is a decomposition into
two nonnegative losses, not by itself an Einstein coercivity theorem.

# A proved remainder in the negative scalar band

The new proof is in [Scalar-band remainder](line1_scalar_band_remainder.md).
It uses the actual conformally solvable structure, with \(p>0\), and
\[
-S\le s\le-s_0<0.
\tag{6}
\]
It does not assume Kähler geometry, Einstein geometry, a Ricci bound,
noncollapse, a Sobolev constant, or a lower bound for \(a_g^2\).

Write \(w=\sqrt6|W^+|\), \(q=-s+w\), and \(t=s+2w\). The exact split is
\[
144\pi^2\mathscr D
=\left(\int q_+^2-72\pi^2p\right)
  \int q_-^2+\frac12\int t^2 .
\tag{7}
\]
Every term on the right is nonnegative. Under (6), \(q_-=0\).
The weighted monopole equation with smooth approximations to
\(f=\sqrt q\) produces actual smooth global self-dual forms \(\psi\).
For every prescribed approximation tolerance, they satisfy
\[
|\psi|\le S/\sqrt{s_0},\qquad
\int\bigl(|d\psi|^2+|d|\psi||^2\bigr)
\le C\mathscr D+\text{tolerance},
\tag{8}
\]
\[
\int\left|W^+-
\left(\frac{|\psi|^2}{8}I-\frac38\psi\otimes\psi\right)\right|^2
\le C(S,s_0)\mathscr D+\text{tolerance}.
\tag{9}
\]
Here \(d\psi\) is the exterior derivative, not the full covariant
derivative. The latter has the weaker estimate
\[
\int|\nabla\psi|^2
\le C(S,s_0)\left(\mathscr D+\sqrt{V\mathscr D}\right)
+\text{tolerance}.
\tag{10}
\]
The proof retains the differential, spectral, and Hölder losses
instead of replacing them by an equality-case slogan. It uses no
derivatives of the smoothing weights.

This is an extension of the retained-defect calculation of Round 3 to
the correct Proposition 4.1 functional, not a new gauge-existence
theorem. Unlike Round 17, its smallness assumption is
\(\mathscr D\), not scalar energy above \(32\pi^2a^2\) plus Ricci
error. Consequently it allows the non-Einstein cscK equality examples.
The cost is the explicit scalar-band hypothesis.

If additionally \(\lambda_1(g)\ge\lambda_0>0\), Poincaré controls the
scalar variance by \(C(S,s_0,\lambda_0)\mathscr D\).
No such uniform spectral hypothesis is needed in (8)--(10).
Neither these estimates nor vanishing averaged derivatives assert
smooth convergence across degenerating manifolds.

# The primitive-period term that distinguishes Einstein geometry

For an actual Kähler surface, use \(a=c_1(M,J)\) (or its negative),
so \(a^2=T\). Hodge theory and the Ricci-form identity give
\[
\mathscr D=\frac{L}{64\pi^2},\qquad
P=8\pi^2(p-T)+16\pi^2\mathscr D.
\tag{11}
\]
The quantity \(p-T=\|a^-\|_2^2\) is the harmonic primitive canonical
energy. It is independent of the scalar-variance loss.
For \(R_2>0\),
\[
\mathcal E=
\frac{4P+L}{R_2}
=4\,\frac{p-T+4\mathscr D}{2p-T+4\mathscr D}.
\tag{12}
\]
These classical Kähler identities, derived in
[the companion proof](line1_kahler_energy.md), give a precise
criterion, not an unconditional extension to almost-Kähler metrics.
At fixed nonzero normalization, both losses must vanish to obtain
Einstein geometry.

There is a sharper test than unequal products. Start with an equal
negative-curvature product of two high-genus surfaces and blow up
\(k>0\) points. Classical Arezzo--Pacard cscK blow-up metrics give
an actual fixed-topology sequence satisfying
\[
\mathscr D=0,\qquad p\longrightarrow A,\qquad
R_2\longrightarrow8\pi^2(A+k),\qquad
\mathcal E\longrightarrow\frac{4k}{A+k}>0.
\tag{13}
\]
Thus even *both* losses in (5) tending to zero do not make the
sequence Einstein: \(p-T=(p-A)+k\) retains the blow-up contribution.
The existence theorem and these deductions are attributed separately;
this is not a new cscK construction. It is not a counterexample to
pointwise Yau26.

# Where the new remainder meets pointwise Yau26

If \(\delta_-=\|g^{-1}\operatorname{Ric}+I\|_\infty<1\), then
\[
-4(1+\delta_-)\le s\le-4(1-\delta_-).
\]
Hence a fixed small pinching range supplies the scalar band in (6).
**It does not supply small \(\mathscr D/V\).** That requires a
separate near-minimum or topological argument.

When both inputs hold, (8)--(10) supply an actual bounded global form,
not merely a pointwise chosen Weyl eigenvector. After constant
rescaling, the form approaches the allowed negative-KE normalization.
This is useful geometric information about the original metric.
It does not exclude the allowed branch.

The next missing estimate is specific: can the induced determinant
connection, or another actual closed representative, be used to
control the primitive-period part and the errors in passing from a
bounded nearly closed form to genuine global geometry? The exact
Kähler identity (11) identifies the term that has to be kept.
A proposed extension must agree with both (13) and the existing
shear examples; it cannot suppress the topological contribution.

## Closing the second-order form budget

The first-order estimates alone do not give
\(B=\fint|\Delta_H\psi|^2\). The companion proof now supplies this
additional step using the inherited bounded-section Hessian lemma.
If, in addition to (6),
\[
\fint|\operatorname{Ric}|^2\le R_0,\qquad
\frac{(-a_g^2)_+}{V}\le A_0,\qquad
\frac{\mathscr D}{V}\le D_0,
\]
then its actual forms can be chosen with
\[
\fint|\Delta_H\psi|^2\le C(S,s_0,R_0,A_0,D_0).
\tag{14}
\]
The determinant-curvature identity controls the full line curvature
by its self-dual part and the class square. The positive-spinor
connection involves \(W^+\), scalar curvature, trace-free Ricci,
and that line curvature, but not \(W^-\). The spinor rough-Laplacian
equation contains the weight, not its derivatives. These facts make
the inherited Hessian estimate applicable without a hidden weight
derivative or Sobolev bound.

There is a useful category where the square budget is automatic.
If \(a_g^2\ge T\), Chern--Weil gives
\[
\frac{(-a_g^2)_+}{V}
\le\frac{(-T)_+}{V}
\le\frac1{8\pi^2}\fint|\operatorname{Ric}^{\circ}|^2.
\tag{15}
\]
Consequently, for \(\delta_-\le1/2\), \(\mathscr D/V\le1\), and
an actual class with \(a_g^2\ge T\), there are actual smooth forms
\(\omega=\sqrt3\,\psi/2\) with uniform bound and
\[
B_\omega\le C,\qquad
d_{-1,1/2}(\omega)\le
C\left(\delta_-^2+\frac{\mathscr D}{V}\right)
+\text{arbitrarily small tolerance}.
\tag{16}
\]
Indeed the polynomial model in (9) is exactly \(A_{\omega,1/2}\).
Writing \(a_0=q-9|\psi|^2/4\), its amplitude error is exactly
\[
|\omega|^2-2=\frac t6-\frac{s+4}{2}-\frac{a_0}{3}.
\]
This proves a specific actual-form supply statement with a controlled
joint budget. It uses the inherited Hessian lemma, but not the
forbidden-spectrum calibration theorem as a black box.

Equation (16) reaches the **allowed** negative-KE root. It is a
geometric-structure input, not a new contradiction and not a proof
of global Kähler or Einstein existence. In particular, the separate
assumption \(\mathscr D/V\to0\) cannot be deleted: the scalar band
alone does not give it.

# Literature connections with their actual hypotheses

The uploaded 37-reference map is retained, with its original verification
levels. Four especially direct comparisons have been checked against
primary texts in this increment:

| Input | Available conclusion | Additional bridge needed here |
| --- | --- | --- |
| LeBrun's actual weighted monopoles | Curvature lower bounds and cscK equality | Quantitative retained losses, as above |
| Catino--Dameno: exact \(\delta W^+=0\), everywhere simple largest eigenvalue | Conformal Kähler structure on at most a double cover | Control the nonzero divergence source and eigenline degeneracy |
| Fine--Krasnov--Singer: compact exact Einstein, fixed Einstein constant, \(\mathcal R^+<0\) | Infinitesimal and local rigidity modulo diffeomorphisms | Pointwise definiteness and an appropriate neighborhood for approximate data |
| LeBrun--Ozuch: positive exact Einstein sequence, singular Hermitian orbifold limit, ASD ALE bubble tree | Eventually Kähler--Einstein | Verify that a proposed sequence belongs to this degeneration class |

In negative normalization the Round 21 roots give
\[
t=0:\quad\mathcal R^+=-I/3,\qquad
t=1/2:\quad\operatorname{spec}\mathcal R^+=(-1,0,0).
\]
Only the first lies in the strictly definite connection regime.
The negative-KE root also has a double largest Weyl eigenvalue, so it
does not satisfy Catino--Dameno's simple-largest-eigenvalue hypothesis.

Other retained connections remain available without being presumed to
solve the new problem:

- Derdziński, LeBrun, and Sekigawa distinguish harmonic Weyl,
  harmonic-form, and almost-Kähler rigidity.
- Cheeger--Tian treats precise Einstein small-energy regularity.
  Cheeger--Naber and Jiang--Naber use their stated noncollapse/Ricci
  hypotheses. Naber--Zhang's maximal-rank information is not an
  unconditional full-curvature bound for arbitrary Ricci-pinched data.
- Uhlenbeck provides local critical-energy gauges; uniform constants
  on collapsing covers require proof.
- Biquard and Ozuch describe exact orbifold degeneration and, in
  specified categories, coverage by gluing procedures. Their scope
  is not every non-Einstein input or every distant output.
- Ricci-flow, entropy, and spinor methods require an actual flow and
  an evolution budget. Failure of a given flow is not smooth-type
  nonexistence.
- Effective negatively curved stability allows some geometric
  degeneration but retains thin-part and sectional-curvature
  hypotheses. Product thin parts retain Teichmüller slow modes.
- Non-locally-symmetric negative Einstein and non-ball-quotient KE
  examples are positive tests of any proposed general obstruction.

# Research choices following this increment

The immediate extension with mathematical content is not a more
ambitious slogan about the same forbidden spectrum. There are three
distinct tests:

1. **Quantitative realization of the allowed branch.** Extend (11)
   from an actual Kähler metric to controlled monopole-generated
   approximate structures, with an explicit error for nonclosure,
   zero sets, and determinant curvature. Success would connect the
   functional remainder to a real Einstein residual, or identify an
   unavoidable global incompatibility.
2. **New actual-form supply.** Apply (2) in a category not already
   covered by the monopole theorem. Harmonic forms, line-bundle-valued
   eigenforms, and coupled gauge equations require different
   existence proofs and joint budgets. They are alternatives, not
   interchangeable names for an assumed form.
3. **Variable spectral amplitude.** For \(t=t(x)\), retain the
   \(dt\) and \(\nabla^2t\) terms in the self-test. The conformal
   divergence identity from modern Weyl theory offers a concrete
   comparison. The constant-\(t\) theorem cannot silently be reused.

The first is the closest continuation of the present proof; the
other two preserve the broader scope of the first line. A result on
a fixed neighborhood or near-minimum sequence should be completed
at that scope. An all-output Einstein judgment still requires a
separate global argument.

# Sources and mathematical attribution

- Original analytic input: [Round 3 retained defects](round3_monopole_input.md),
  [Round 4 integral calibration](round4_rigidity.md),
  [Round 5 abstract classes](round5_rigidity.md),
  [Round 13 polarization](round13_chamber.md),
  [Round 17 scalar calibration](round17_integral.md),
  [Round 21 spectrum](round21_analytic.md).
- Current classical-application closure:
  [polarized closure](lebrun_stability_closure.md).
- This increment's derivations:
  [scalar-band remainder](line1_scalar_band_remainder.md) and
  [Kähler energy comparison](line1_kahler_energy.md).
- All seven uploaded files, including the duplicate discussion texts:
  [source inventory](line1_sources_20260923/manifest.json).
  The original section-to-use correspondence is in
  [coverage](line1_source_coverage.tsv).
- Primary texts:
  [LeBrun's curvature functionals, Props. 4.1--4.2 and Thm. 4.3](https://arxiv.org/html/math/0003068);
  [weighted solvability, Lemma 3.7](https://arxiv.org/html/math/0611450);
  [Catino--Dameno](https://arxiv.org/html/2607.21538v1);
  [Fine--Krasnov--Singer](https://arxiv.org/abs/1910.09790);
  [LeBrun--Ozuch](https://arxiv.org/html/2601.19215v2).

The algebraic decompositions and Kähler comparison are classical
deductions. The scalar-band retained-remainder proof is a new
derivation in this research record, built from the earlier weighted
identities; worldwide priority has not been established. No original
upload, active Session, service, or installed Skill is replaced by this
research increment.
