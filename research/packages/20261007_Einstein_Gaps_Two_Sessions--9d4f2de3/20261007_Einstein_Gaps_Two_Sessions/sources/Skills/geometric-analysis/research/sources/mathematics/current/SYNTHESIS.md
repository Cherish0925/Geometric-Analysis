# Yau 26: mathematical progress across research rounds 1–12

21 September 2026.

This synthesis compares the research sequence ending at local commit c98fdfb
with the installed qiushi-yau26 research manuscripts dated 10–17 September.
Round 1 is the original research README and its companion notes; rounds 2–12
have individually numbered syntheses. These are twelve research continuations,
not twelve independent discoveries and not the earlier three 100-step Sessions.

“New” below means new relative to that Skill baseline. The cited notes contain
proofs and their computational support; a comprehensive publication-priority
comparison has not been completed. This document consolidates those deductions,
rather than treating every intermediate estimate as a separate main theorem.

## 1. The change in the mathematical position

The baseline already contained the exact-Einstein uniform topology gap,
the fixed A1/log-Weyl construction, the Dehn-twist surface-bundle construction,
its variational quantities, algebraic smoothing examples, charged stable
local Einstein germs, and restricted orthogonally transitive connector
results. None is counted again here.

The strongest subsequent changes are:

| Scientific question | Baseline | Present increment |
| --- | --- | --- |
| Can the critical monopole topologies carry arbitrarily small Ricci defect? | Exact Einstein exclusion; approximate exclusion under additional geometry | A uniform integral Ricci-defect gap in specified monopole families, without pointwise curvature, noncollapse or diameter assumptions |
| Which fixed closed smooth objects admit vanishing defect? | Marked A1 resolutions and surface bundles | Closed sheared product-block assemblies, including examples that are not any oriented surface bundle and have no Kähler finite cover |
| Can a symmetric exact connector be globally completed? | OT and selected model obstructions | Boundary connectedness for the whole smoothly conformally compact Einstein free-circle class |
| Does exact exclusion force an approximate gap? | An unresolved possibility for connectors | An explicit two-ended family with an exact global error formula, and a doubling estimate for fixed nonzero circle-bundle degree |
| What can be said about all exact outputs on the new closed objects? | No such objects in the baseline | Complete ordinary basic-class sets, sharp variational quantities, and absence of all nonzero local Killing fields for any hypothetical Einstein metric |

The last four rows interact, but their manifolds and hypotheses must remain
distinct. In particular, the noncompact approximate connectors are not closed
Yau26 counterexamples, and the new closed product-block manifolds are not the
real-hyperbolic extended graph manifolds with a previously known all-Einstein
obstruction.

Throughout, \(\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_\infty\),
with the spectral operator norm. Some connector calculations use
\(\epsilon(g)=\|g^{-1}\operatorname{Ric}_g+3I\|_\infty\);
then \(\delta_-(3g)=\epsilon(g)/3\).

## 2. Line I: from exact topology exclusion to an integral near-Einstein gap

### 2.1 The principal theorem

For a closed minimal complex surface of general type \(X\), with
\(b_+(X)>1\), let \(A=c_1^2(X)>0\) and
\(M=X\#k\overline{\mathbb{CP}}^{\,2}\). Define the scale-invariant quantity
\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}
=\frac{4\int|\operatorname{Ric}^{\circ}|^2+
\int(s-\bar s)^2}{\int|\operatorname{Ric}|^2}.
\]
The monopole input excludes a zero denominator. Rounds 3–4 prove
\[
\boxed{\mathcal E(g)+\left(\frac13-\frac{k}{A}\right)_+\ge c_*>0}
\]
uniformly over \(X,k,g\). Neither total volume, diameter, injectivity radius,
Sobolev constants, full curvature nor curvature derivatives enter the
constant. The earlier pointwise consequence is
\[
\delta_-(g)^2+\left(\frac13-\frac{k}{A}\right)_+\ge c>0.
\]
The positive-sign part of the integral formulation follows from classical
scalar monopole estimates; the substantive new analytic closure is negative.

This is stronger than the baseline exact-Einstein gap on this family:
it excludes even arbitrarily small normalized integral Ricci defect near
the critical topology ratio. It does not prove Einstein existence on
arbitrary four-manifolds.

Proofs: [intrinsic closure](round3_rigidity.md),
[blow-up theorem](round3_joint_gap.md),
[integral theorem](round4_rigidity.md),
[all-sign formulation](round4_all_sign_gap.md).

### 2.2 Why the proof is different from the old compactness argument

The proof does not first construct a noncollapsed limiting chart.
A rescaled monopole supplies a bounded spinor and a smooth polynomial
Weyl model
\[
A_\psi=\frac{|\psi|^2}{24}I-\frac18\psi\otimes\psi.
\]
Near equality controls \(W^+-A_\psi\) in averaged \(L^2\).
Covariant integration by parts controls the spinor Hessian using the
rough Laplacian and the bundle-curvature \(L^2\) budget. The unused
anti-self-dual Weyl block does not act on the positive-spinor bundle.

This extra derivative permits testing weak Bianchi against
\(J_\psi=\operatorname{div}W(A_\psi)\) itself. Near equality then forces
both \(\fint|J_\psi|^2\to0\) and, by the weighted Hodge identity,
\(\fint|J_\psi|^2\to1/16\). The contradiction takes place on the original
closed metrics, even when they collapse.

Round 4 replaces a pointwise-dependent rescaling by a truncated weight
whose extra cost is charged to \(\int(s+4)^2\). This removes the remaining
pointwise scalar/Ricci hypothesis rather than assuming a smoothing theorem.

### 2.3 Generality and the actual input it requires

Let \(T=2\chi+3\tau\), and let \(\alpha_{\mathrm{sp}}^2>0\) be the
period-plane minimax over actual special monopole classes, whose squares
satisfy \(a^2\ge T\), on a closed oriented four-manifold with \(b_+\ge2\).
Round 5 gives
\[
\boxed{\mathcal E(g)+
\left(\frac{T}{\alpha_{\mathrm{sp}}^2}-\frac23\right)_+
\ge\varepsilon_0>0.}
\]
This removes the need for a particular blow-up presentation. For arbitrary
monopole classes without the square condition, the constant retains a
negative-class-square dependence; abstract \(\mathrm{MP}(A)\) alone has
not been silently upgraded to this universal version.

The connected-sum applications use actual gluing theorems for monopole
classes, not intersection-form vectors invented to fit the inequality.
See [the invariant and connected-sum theorem](round5_rigidity.md).

### 2.4 Supporting results and compatibility with constructions

The following are meaningful components, not extra copies of the main gap:

- An explicit forbidden-Weyl spectral box, and an obstruction to extending
  the proposed invariant scalar multiplier globally:
  [round 1 rigidity](rigidity.md).
- A Ricci-small, bounded-full-curvature example with divergent Cotton
  energy, showing why the derivative source cannot simply be discarded:
  [the same note](rigidity.md).
- Strong local \(L^2\) Weyl convergence under the stated controlled-chart
  assumptions, and a curvature-bounded conditional gap:
  [weak transfer](round2_weak_curvature.md) and
  [conditional gap, Section 9](round2_rigidity.md).
- An explicit improved bound above \(k/A=1/3\), e.g. approximately
  0.296535 instead of 0.224009 at \(k/A=1/2\):
  [fixed-ratio optimization](fixed_ratio.md).
- Sharp algebraic Ricci-box estimates, implying strict Hitchin–Thorpe
  for \(\delta_\sigma<1/2\):
  [curvature-box calculation](curvature_box.md).

The important cross-line result is not another coefficient. On the old
\(E_D\) and the new sheared closed examples, the monopole ratio is
\(T/\alpha^2=1\). Fixed negative locally symmetric orbifold fillings
with the stated concentration convergence satisfy \(T/\alpha^2\ge3/4\)
whenever \(\alpha^2>0\).
They cannot approach the critical value \(2/3\) just by adding bubble
energy or changing chirality. Conversely, connected-sum modifications
that move actual monopole topology into the forbidden band cannot retain
vanishing Ricci defect. This explains why the existing input construction
and the existing no-Einstein band do not automatically meet.

The filling-independent energy/topology calculation is
[round 7 concentration](round7_endpoint.md); its special A1 predecessor
and the \(E_D\) comparison are [round 5](round5_rigidity.md).
The \(E_D\) saturation itself was already in the Skill.

## 3. Line II: exact local models, limits of repair, and new closed inputs

### 3.1 A complete nonlinear Einstein model

Rounds 2–4 pass from second-order corrections to actual complete metrics on
\((\mathbb R\times S^1)^2\):
\[
G[z]=g[z]+k[z],\qquad \operatorname{Ric}_{G[z]}=-G[z],
\qquad k[z]=O(|z|^2).
\]
All eight bounded angularly invariant Jacobi directions under consideration
are integrated. This is not a claim of eight inequivalent global moduli.
The proof keeps all tensor blocks, a weighted inverse, the nonlinear
target space, and gauge removal.

The exact twist law is
\[
\frac{\pi^2}{2}(-b_1,B_1)^{\mathsf T}=M[z]q[z],\qquad M[z]>0.
\]
It includes the infinite-boundary Stokes limit. Nonzero twist exports
real boundary response; an \(L^2\) correction cannot be used to erase a
non-\(L^2\) receiver's flux. A nonzero-charge model cannot agree unchanged
on an open set with a closed Einstein manifold. Approximate insertion
with changes throughout remains possible.

Proofs: [complete model](round3_construction.md),
[nonlinear charge](round4_construction.md),
[exact-core restriction](round4_exact_core.md).

### 3.2 The old \(E_D\) construction has a much stronger repair theorem

For the balanced \(E_D\) metrics \(G_\varepsilon\), the latest estimate is
\[
\|h\|_{C^2(G_\varepsilon)}\le c_*\varepsilon
\quad\Longrightarrow\quad
\delta_-(G_\varepsilon+h)\ge c_1\varepsilon^3.
\]
There is no symmetry or support restriction on \(h\). After a fixed
reduction of radius, no Einstein metric of any constant lies in this ball.
The inherited scalar correction gives a matching cubic upper order.
For \(h=o(\varepsilon)\), the explicit lower coefficient is
\(1/[16\pi^4(p-1)]\), where \(p\) is fibre genus.

The gain over the Skill is removal of the old restricted correction
classes, not merely another cubic residual computation. A whole-fibre
TT receiver and an inverse in its actual weighted measure retain the
full kernel, angular modes and end response. Its quadratic kernel
contribution has the wrong sign to cancel the source.

The progression from base-TT directions, through the
\(O(\varepsilon^{3/2})\) ball, to this fixed linear-size ball is one
developing result, not three separate major discoveries.
Proofs: [whole-fibre receiver](round5_construction.md),
[weighted inverse](round6_weighted_inverse.md),
[final neighbourhood theorem](round6_construction.md).
Distant Einstein metrics are not excluded.

### 3.3 Explicit two-ended approximate metrics

On the fixed noncompact manifold
\(\mathbb R\times S^1\times\Sigma_g\), Round 10 gives an explicit
smooth complete family with fixed conformal infinities and
\[
\boxed{\|\operatorname{Ric}_{g_d}+3g_d\|_{\infty,\mathrm{op}}
=\frac{d(2d+3)}{(1+d)^2}\longrightarrow0.}
\]
Here the displayed norm means the metric-relative endomorphism norm.
Every fixed curvature-derivative order remains bounded. An exact-end
variant and a doubling construction on fixed nontrivial circle bundles
are also proved. The latter uses a cited external exact-cusp existence
theorem; it is not attributed anew to this project.

These are genuine geometries realizing a degenerating estimate, rather
than algebraic data satisfying only selected equations. Optical
ground-state localization and circle collapse explain how small error
coexists with exact nonexistence in the free-circle two-boundary class.
The cross-sections are \(S^1\times\Sigma_g\), or corresponding circle
bundles, not the \(T^3\) of the unresolved approximate flat-torus connector.

Proofs: [explicit Kottler modification](round10_kottler.md),
[nontrivial-bundle doubling](round10_cusp_doubling.md),
[optical mechanism](round10_optical.md),
[charge and Chern constraints](round10_connector.md).

### 3.4 The largest constructive change: fixed closed sheared assemblies

Round 11 joins blocks \(B_v\times F_v\) by fixed boundary maps
\[
(\phi,x)\longmapsto(-\phi+u_e(x),f_e(x)).
\]
The bases have negative Euler characteristic and boundary; the closed
fibres have matching genus at least two. Circle-valued integral shear
and arbitrary orientation-preserving mapping classes are both allowed.
The closed smooth assembly carries
\[
\boxed{\|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty
\le C\bigl(|\log\ell|^{-1}+\ell\bigr)\to0,\qquad
\operatorname{Vol}(G_\ell)=4\pi^2\chi(M)/9.}
\]
After rescaling by three this is precisely the normalized negative
Yau26 input. Full curvature stays bounded; positive-order curvature
derivatives tend to zero. Both orientations are symplectic.

Two different freedoms make this possible. A long collar absorbs the
mapping-class change slowly. A separate collapsed throat makes an
integral shear cost \(O(\ell)\) in the full Ricci matrix while retaining
its nonzero topological class. Circle-valued transition maps close the
construction without assuming a nonexistent global primitive.

For self-gluing \(F_{h,2}\times\Sigma_g\), with \(h\ge1,\ g\ge2\),
\(u\ne0\) and infinite-order
\([f]\) produce manifolds that are not any oriented surface bundle over
a surface. Thus this is not just the old \(E_D\) construction renamed.
A separating gluing can, however, reproduce an old surface-bundle object;
the notes explicitly distinguish that case.

Proofs: [closed construction](round11_closed_gluing.md),
[actual smooth topology](round11_graph_topology.md).

## 4. Line III: global conclusions on connectors and on the actual closed objects

### 4.1 An entire exact connector class is excluded

Round 9 proves: in dimension at least three, a smoothly conformally compact
negative Einstein manifold with a free isometric circle action extending
freely to its compactification has connected conformal boundary.
No boundary Yamabe sign, orthogonal transitivity or trivial principal
bundle is required.

In particular, all exact two-AH-end free-\(T^2\) connectors on
\(\mathbb R\times T^3\) are excluded, including nonzero charge and
rotating nondiagonal orbit shape. This is strictly broader than the
baseline OT/Morse obstruction.

The principal proof builds an auxiliary static Lorentzian metric from
the circle quotient. The original twist contributes nonnegative null
Ricci curvature; a classical boundary-noncommunication theorem then
contradicts the compact optical path between ends. A separate
four-dimensional stable-separator proof detects the conserved charge.

Proofs: [boundary connectedness](round9_connector.md),
[Riemannian separator](round9_riemannian.md).
The external causal input is
[Galloway–Schleich–Witt–Woolgar, Theorem 2](https://arxiv.org/pdf/hep-th/9912119).

Earlier charged-neck, holonomy and spectral identities remain valid,
but statements in rounds 6–8 calling this exact free-torus completion
open have been superseded. The approximate, nonsymmetric and singular-orbit
problems have not thereby been excluded.

### 4.2 Global topology and invariants of the new closed inputs

For \(M=M(h,g;u,f)\), with \(h\ge1,\ g\ge2,\ u\ne0\), the proof gives
\[
\chi(M)=4h(g-1)>0,\qquad \tau(M)=0,
\]
asphericity and absence of a Kähler finite cover. The last assertion
requires no order assumption on \(f\). The non-surface-bundle theorem
additionally uses infinite mapping-class order.

An explicit even-Betti example has
\[
\chi=4,\quad \tau=0,\quad b_1=4,\quad b_2=10,\quad b_+=b_-=5.
\]
The obstruction is therefore not merely odd first Betti number.

On these same objects the symplectic monopole lower bounds and the
constructed upper bounds agree:
\[
\begin{aligned}
\sigma(M)&=-8\pi\sqrt{\chi(M)},\\
\inf_{\operatorname{Ric}\ge-g}\operatorname{Vol}&=4\pi^2\chi(M),\\
\inf\int s^2&=64\pi^2\chi(M),\\
\inf\int|\operatorname{Ric}|^2&=16\pi^2\chi(M),\\
\inf\int|\operatorname{Rm}|^2&=32\pi^2\chi(M).
\end{aligned}
\]
The last line uses the full four-index tensor norm. The first four
extrema are not attained when \(u\ne0\). Attainment of the last is
equivalent to Einstein existence and remains undecided.
The form of this variational argument was already present for \(E_D\);
its extension to these different smooth objects is the increment.

Round 12 additionally computes the entire ordinary basic first-Chern sets:
\[
\mathcal B(M)=\{\pm a\},\qquad
\mathcal B(-M)=\{\pm b\},\qquad
a^2=2\chi,\quad a\cdot b=0,\quad b^2=-2\chi
\]
in the positive orientation, and \(\alpha^2=\beta^2=2\chi\) in each
orientation. This is stronger than listing known canonical classes.
It does not classify every possible monopole or refined gauge invariant.

Proofs: [virtual Kähler obstruction](round11_kahler.md),
[variational quantities](round11_variational.md),
[complete ordinary basic sets](round12_global.md).

### 4.3 Every hypothetical Einstein output must have no local symmetry

For every Riemannian metric on the self-glued \(M(u\ne0)\), the
universal-cover isometry group is discrete. Einstein analyticity and
Nomizu extension then imply:
\[
\boxed{\text{An Einstein metric on }M
\text{ has no nonzero local Killing field on any open set.}}
\]
This remains true on every finite cover. The proof combines the actual
Bass–Serre group, smooth irreducibility and
[Farb–Weinberger, Theorem 1.3](https://math.uchicago.edu/~farb/papers/isoms.pdf).
It is a concrete application of classical global rigidity, not a new
general isometry theorem.

Positive Einstein and Ricci-flat metrics are already excluded by the
group. Therefore any remaining Einstein output must be negative,
non-Kähler even after finite cover, and entirely without continuous
local symmetry. The conclusion concerns every possible output, not
only small perturbations of the constructed sequence.

It gives no lower bound on the size of a symmetry-breaking perturbation.
Such an output may still exist. Proof: [global symmetry](round12_symmetry.md).

A separate collar theorem quantifies a repair cost in its stated
circle-invariant normal form:
\[
\eta\ge\frac{\sqrt3}{4\Lambda^2}
d_{\mathcal T}([h_-],[h_+])^2.
\]
The radius is within a factor \(\Lambda\) of the cosh profile and
depends only on the longitudinal variable; \(\eta\) bounds the face
mean curvatures. This estimate survives circle collapse but does not
apply unchanged to an arbitrary spatially varying radius.
See [marked collar repair](round12_repair.md).

### 4.4 Other substantive global results

These results should remain visible without being confused with the
principal closed-input theorem:

| Object or mechanism | Actual additional result | Remaining distinction |
| --- | --- | --- |
| Real-hyperbolic Davis resolutions | Explicit smooth topology; ordinary entropy vanishes; neither orientation of the all-negative filling is almost complex; ordinary numerical SW and ordinary absolute \(S^1\)-equivariant BF vanish on the fixed marked fillings in both orientations | No general Einstein nonexistence, all-monopole vanishing or vanishing of other gauge refinements follows |
| Dehn-twist \(E_D\) | Complete rank-one representation-volume calculation; every map to a closed strictly negatively curved four-manifold has degree zero | Negative Einstein does not imply negative sectional curvature |
| Multiple and noncommuting twists | Actual slow-interpolation inputs with sharply reduced, or zero, product-hyperbolic representation volumes | Slow interpolation is inherited; representation computation is the added analysis |
| Intrinsic harmonic/Hodge functional | Constructed inputs have \(\Gamma=0\); each hypothetical normalized Einstein output on the specified infinite-monodromy bundle has \(\Gamma>0\) | No uniform positive separation over all source metrics |
| Exact Kodaira controls | Infinite monodromy can coexist with genuine negative KE and \(\Gamma/\operatorname{Vol}\to0\) | These controls have positive signature, not the zero signature of \(E_D\) |
| Nonabelian gauge route | Exact partial seeds, critical-energy lower bounds, rank-one mixing identity, and an explicitly specified corrected-system classification | Auxiliary solutions do not follow from ordinary SW; different curvature conventions define different systems |
| Schoen-surface control | A known negative KE, zero-signature, nonlocally symmetric surface blocks an overly broad ordinary-monopole uniformization claim | This is an established example used as a control, not a new surface |

Sources: [Davis entropy](round6_entropy.md),
[Davis gauge analysis](round7_topology.md),
[rank-one representations](round8_construction.md),
[multiple twists](round8_multitwist.md),
[harmonic functional](round9_bundle.md),
[Kodaira controls](round10_bundle.md),
[reducible energy](round8_nonabelian.md),
[partial seeds](round9_nonabelian.md),
[full-rank residual](round10_nonabelian.md),
[rank-one mixing](round11_rankone.md),
[corrected Clifford system](round12_uniformization.md),
[Schoen control](round12_control.md).

The corrected Clifford system in round 12 has solutions precisely in
the real-hyperbolic case under its closed Einstein, \(\chi>0,\tau=0\)
hypotheses. This is a statement about the equations explicitly derived
there. They have not been identified with Leung's intended published
system and its bidisk converse. The earlier unshifted-system seeds cannot
be transferred to it without checking its central curvature equation.

### 4.5 Quantitative connector and transport results retained beneath the main theorem

These estimates explain what failed, which escape was later realized,
and which hypotheses remain useful. They should not be lost merely
because the exact free-circle theorem is now stronger in another respect.

| Setting | Result and mechanism | Scope |
| --- | --- | --- |
| Two exact expanding flat ends, with \(\operatorname{Ric}\ge-(3+\epsilon)g\) | A minimizing-geodesic index form forces bridge width greater than \(\log(12/\epsilon)+O(\epsilon|\log\epsilon|)\) | No torus symmetry is assumed; a one-sided Ricci example shows width alone does not control the full Ricci defect |
| Full positive-definite orbit matrices on homogeneous Nil slices | Two expanding ends with the specified asymptotics force operator-norm Ricci defect relative to \(-\lambda g\) at least \(\lambda/3\) | Includes central-direction mixing; not arbitrary spatially varying connectors |
| \(\mathbb R\times T^3\), exact outward hyperbolic ends and nonpositive sectional curvature | The flat torus theorem forces defect at least \(3/2\); the value is sharp as an infimum | No isometric torus action is assumed; positive sectional curvature is a genuine remaining escape |
| A complete two-ended harmonic separator | \(\lambda_0+\frac23\int Q\,d\nu\le2+\frac23\epsilon\) retains physical twist in the classical spectral inequality | Neither a lower bound on \(\lambda_0\) nor on twist mass is supplied |
| Exact torus ends with marked holonomy | A finite positive matrix relates real end-holonomy lifts to conserved charge | Equal torus-valued holonomy does not imply equal real lifts |
| Approximate rather than exact connectors | Charge leakage is bounded in the actual orbit-weighted norm; a Chern-number gap contains a degenerating radius denominator | Small Ricci error does not preserve exact charge, and fixed nonzero Chern number alone does not force a uniform gap |

Proofs: [width](round3_global.md), [full-matrix Nil](round4_global.md),
[flat-torus rank obstruction](round5_rank_obstruction.md),
[harmonic spectrum](round7_spectral.md), [boundary holonomy](round8_boundary.md),
[approximate charge and Chern number](round10_connector.md).

The one-ended capped metric in [round 6](round6_global.md) realizes
actual charge removal with \(O(R^{-3})\) full Ricci error and an exact
hyperbolic outer end. Its bolt and one-ended topology prevent it from
being substituted for the two-ended cylinder. The earlier Skill already
had nonzero-charge stable Koiso germs: their rederivation is not another
existence theorem claimed by these rounds.

## 5. How the three lines now fit together

The first line establishes a stable obstruction on one class of smooth
topologies. The second creates approximations on other fixed topologies.
The third determines what exact Einstein geometry on those actual
input manifolds could look like.

The most useful connection is also the most restrictive:

1. The critical monopole theorem is genuinely stronger than the old
   exact-only gap, but the constructed examples saturate a different
   topological ratio. They are not counterexamples to it.
2. Exact free-circle connector exclusion and approximate free-circle
   construction coexist. A no-exact theorem is not automatically a
   quantitative error gap in degenerating geometry.
3. Closed sheared constructions retain integral topology while its
   pointwise Ricci cost vanishes. Yet topology forces any exact output
   to break every local symmetry of the construction.
4. Scalar/Ricci-energy nonattainment is not full-curvature-energy
   nonattainment. The latter remains exactly the missing Einstein
   question on the new closed examples.

Thus the research has moved beyond three separate lists of tools.
It now connects topology invisible to small Ricci error, global gauge
data, degeneration, and restrictions on every exact output.

The strongest candidates for substantive new methods relative to the
Skill are the intrinsic bounded-spinor closure, the two-scale closed
shear construction, the circle-quotient-to-causal-boundary argument,
and the detector-weighted repair analysis. The invariant computations
and symmetry conclusions are strong object-specific applications.
Improved constants, repeat checks and known control examples support
these results; they are not all independent breakthroughs.

### 5.1 The geometric objects cannot be interchanged

| Actual object | Small-defect input | Exact conclusion currently obtained | Unresolved question |
| --- | --- | --- | --- |
| Specified critical monopole families | A uniform integral lower bound forbids vanishing defect in the critical band | All Einstein signs are excluded there | Which other topologies admit an equally effective intrinsic calibration? |
| The closed Dehn-twist bundle \(E_D\) | The inherited construction has vanishing pointwise defect | A fixed linear-size \(C^2\) ball around the chosen family contains no exact repair; representation and harmonic constraints are known | Existence of a distant, unrestricted negative Einstein metric |
| Closed sheared \(M(h,g;u,f)\) with nonzero shear | The new fixed-topology construction has vanishing defect and bounded full curvature | Ordinary basic classes are determined; any Einstein metric lacks every nonzero local Killing germ | The full nonsymmetric negative Einstein equation on that same smooth manifold |
| The complete double-cylinder model \((\mathbb R\times S^1)^2\) | An exact analytic Einstein family is constructed | Its nonzero-charge members have no cocompact quotient and cannot be retained unchanged inside a closed Einstein metric | A global construction that genuinely changes the core |
| Smoothly conformally compact, free-circle, two-ended objects | Explicit approximate doubles exist for \(S^1\times\Sigma\) and the stated circle bundles | Exact Einstein metrics preserving that free-circle structure are excluded | Other exact fillings without that structure; small-defect connectors with the different flat \(T^3\) cross-section |
| The marked Davis orbifold resolutions | The inherited applicable log-Weyl construction supplies small defect | Specific topology and ordinary gauge-detector limitations are computed | Arbitrary Einstein existence on the actual smooth resolutions |

The complete double-cylinder Einstein family does not have the smooth
conformally compact asymptotics assumed by the two-ended exclusion theorem.
Likewise, the hyperbolic-surface cross-section of the explicit approximate
double is not a flat torus. These are different geometric settings, not
contradictory conclusions.

### 5.2 Three questions that now require genuinely different mechanisms

**Transfer of rigidity.** The intrinsic gap needs a bounded geometric field
with enough controlled derivatives to test the weak curvature equation.
On the closed sheared examples the existing monopole budget is already known
and lies outside its critical range. Reapplying the same numerical invariant
will not change that fact. A useful extension must supply a different
calibration, a new differential identity, or a new relation to the topology.

**Repair in degenerating geometry.** A residual tending to zero is an actual
construction result, but the inverse estimate and admissible correction
radius can deteriorate at the same time. The receiver estimates identify
this failure quantitatively near \(E_D\). On the new closed objects the
symmetry theorem shows that the search must allow symmetry breaking on
every open neck; it gives no positive lower bound on its amplitude. A small
but genuinely nonsymmetric correction is not ruled out by that theorem.

**Global existence versus nonattainment.** The calculated scalar and Ricci
functionals already have sharp values on the new manifolds. Their failure
to attain those values is not a proof that an Einstein metric at a different
volume cannot exist. The full-curvature minimum is the remaining attainment
problem. A new estimate or construction must distinguish that functional,
or directly address the unrestricted Einstein equation.

These are research opportunities identified by the results, not assertions
that only three methods can succeed. Positive-branch and higher-dimensional
ideas remain relevant to the original quantifiers.

## 6. The twelve rounds as one progression

| Round | Main surviving increment | Read |
| --- | --- | --- |
| 1 | Explicit spectral/fixed-ratio estimates, correction projection and optimized curvature budgets | [original synthesis](README.md) |
| 2 | Weak curvature transfer, bounded-kernel classification, quadratic correction and charged transport | [round 2](round2.md) |
| 3 | Curvature-independent pointwise monopole gap and exact complete model | [round 3](round3.md) |
| 4 | Integral all-sign gap, nonlinear charge law, exact-core restriction | [round 4](round4.md) |
| 5 | Whole-fibre repair receiver and compatibility of actual constructions with the monopole gap | [round 5](round5.md) |
| 6 | Linear-size closed repair exclusion, one-ended charge removal and actual Davis test object | [round 6](round6.md) |
| 7 | Filling-independent concentration budget, actual gauge-detector limits and harmonic separator | [round 7](round7.md) |
| 8 | Representation calculations, restricted global connector exclusions and critical gauge energy | [round 8](round8.md) |
| 9 | Full exact free-circle boundary obstruction, partial gauge seeds and harmonic-energy separation | [round 9](round9.md) |
| 10 | Explicit approximate double ends, nontrivial circle bundles and exact control families | [round 10](round10.md) |
| 11 | Fixed closed sheared assemblies, nonbundle/virtual-Kähler topology and sharp variational theory | [round 11](round11.md) |
| 12 | Complete ordinary basic sets, compulsory symmetry breaking and marked repair constraints | [round 12](round12.md) |

The numbered notes retain their historical “next question” sections.
For current work, use the strongest statements above: the round-2
curvature-bound limitation has been superseded for the monopole
application, and the round-6–8 exact free-torus continuation question
has been closed in its stated free-action class. Their valid estimates
have not been discarded.

## 7. What has and has not been achieved for Yau26

There are substantial theorem-level increments beyond the Skill:
an integral obstruction, new fixed closed input geometries, a complete
exact connector exclusion, constructive approximate escape, and global
information about the same closed inputs. These are not merely improved
numerical precision.

No constructed closed manifold has yet been proved to have both
\(e_-(M)=0\) and no Einstein metric of any sign. On the new sheared
family, the unresolved output is specifically a nonsymmetric,
non-Kähler negative Einstein metric. Its existence would be a new
positive construction; its nonexistence on one member would produce
a negative-branch counterexample.

Neither unrestricted four-dimensional sign branch has been settled,
and there is no full dimension-only affirmative theorem. The positive
branch and general higher-dimensional affirmative mechanism have
received much less decisive progress in these twelve rounds. A complete
negative answer would require defeating both signs in one fixed
dimension, not solving every dimension.

The next work should therefore compare concrete options: the full
nonsymmetric Einstein equation on a specified closed input; an invariant
or identity not exhausted by the calculated monopole data; or a
construction on an already established no-Einstein smooth type. Reducing
an already vanishing residual without changing these questions is not
the same as closing them.

The proof notes, scripts and per-round verification records remain intact.
This synthesis does not claim a new execution of every historical check
or a fresh line-by-line verification of every proof. It updates the
mathematical map from the actual manuscripts and their dependencies.
Installed Skills, live Sessions and services were not changed.
