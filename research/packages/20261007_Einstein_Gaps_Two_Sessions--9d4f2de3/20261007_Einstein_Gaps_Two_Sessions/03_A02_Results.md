# S1003A02: contribution index and proof boundaries

This index covers the whole Session, separating Steps 1–34 from the work
after resumption at 23:57 on 6 October 2026 (Steps 35–44). The preserved
[theorem package](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md)
has 541 lines and incorporates material through Step 43. The separate
Step-44 note and its verifier are therefore read together below. The source
texts remain unchanged.

Write \(P=\int|\operatorname{Ric}^{\circ}|^2\),
\(A=c_1^2(X)>0\), and \(Q=k+4\ell\) for
\(M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\).
The normalized direct defect \(\alpha=\inf\mathcal E\), the raw energy
\(P\), and the alignment functionals \(\kappa_\beta\) are different
objects. Raw \(J_6=\int|\operatorname{Ric}+6g|^2\) is not the normalized
\(\mathcal J\). Weyl norms below are curvature-operator norms.

“Proved” denotes an argument with its stated hypotheses in the preserved
research and verification records; “certified” denotes the recorded interval
enclosure for a specified object. Neither label certifies literature priority.
Computations were not rerun to prepare this index.

## 1. Inherited framework and the density-free alignment extension L′/K

The bounded-form interface, N1, I40/I41, the finite-density endpoint, the
settled linear scale on the specified balanced families, and the original
simultaneous-field identity are inherited inputs. In particular, the
bounded-form estimate \((1+B_\psi)d_\psi\ge c(K)\) does not itself
supply all the spinor differential information used by I40/I41.

A02's Theorem L′ is a genuine extension. Suppose one fixed Spin\(^c\)
structure supplies an actual unperturbed monopole for every metric in a
conformal class, with
\[
 p=(a^+)^2\ge A>0,\qquad a^2\ge T_+,\qquad
 T_+\le\theta A,\quad\theta<3/4.
\]
Then a single constant \(c_L(\theta)>0\), depending only on \(\theta\),
satisfies
\[
 \kappa_\beta(h)\ge c_L(\theta)
 \quad\text{for every }h\text{ in the class and every finite }\beta\ge2.
\]
There is no Euler-density hypothesis. This is uniform over finite \(\beta\),
not merely a separate bound for each fixed parameter. The quadratic
\[
 N_\theta(\beta)=(3/4-\theta)\beta^2
 +(1/2-11\theta/4)\beta+6-\theta
\]
has discriminant
\(\frac{57}{16}(\theta-2/3)(\theta+142/19)\), and
\(N_{2/3}(\beta)=(\beta-8)^2/12\). It locates the thresholds
\(2/3\), \(\beta=8\), and \(3/4\) in one calculation.

Corollary K covers blow-ups of minimal general-type Kähler surfaces with
\(p_g\ge1\): for all metrics and all \(\beta\ge2\),
\[
 \kappa_\beta\ge c_K(\beta-2)^2/\beta^2
\]
with a universal \(c_K>0\). The proof combines L′ in the large-blow-up
range with the inherited finite-density result in the complementary range.
These are alignment conclusions, not positive lower bounds for the
unrestricted direct Einstein defect. Full density-independent O10 remains
open outside the proved ranges.

Sources: [Step 6, §§1–3](sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md),
[Step-5 verification](sources/Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_verifier1_integration.md),
and the inherited [finite-density section](sources/Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex).

## 2. Zero-gap examples and charged concentration tangents

Canonical-model resolutions with shrinking Ricci-flat ALE pieces give
\(\alpha=0\) for the stated minimal general-type Kähler surfaces.
Şuvaina-type generalized rational blowdowns give further zero-gap examples,
including the specified simply connected minimal symplectic non-Kähler
manifolds. These use established LeBrun/Şuvaina constructions; their placement
in the direct-defect problem and the separation of zero infimum from
attainment should not be credited as an entirely new construction.

On the Ricci-flat cores, \(|\operatorname{Ric}+g|^2=4\); their contribution
vanishes because their volume shrinks. Attainment of the zero direct defect
requires a smooth Einstein metric with nonzero Einstein constant. Nef but
nonample canonical class excludes the canonical Kähler–Einstein metric for
that complex structure, not every possible Einstein metric on the smooth
manifold. The cited rational-blowdown source establishes non-Kählerness,
not absence of every complex structure.

The Gibbons–Hawking tangent calculation is a separate model result. One- and
multi-centre spaces carry actual solutions of the leading coupled equations,
with the recorded energies
\[
 \int|\nabla v|^2=8\pi^2m_*k\ell^2,\qquad
 \int|d|v|^2|^2=\frac{16\pi^2}{3}m_*^2k\ell^2.
\]
Here \(\ell\) is the scale parameter of that model. The \(k\)-centre
space has \(b_2=k-1\) and boundary \(L(k,1)\). These nontrivial tangents
defeat an overly strong leading-order Liouville argument. They do not provide
a closed-manifold escape sequence or resolve unrestricted O10.

Sources: [Step 6, §§4 and 7](sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md),
[theorem package, §§2.3 and 3.1–3.2](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md),
[one-centre verification](sources/Sessions/S1003A02/workspace/scripts/verify_gh_tangent.py),
and [multi-centre energy calculation](sources/Sessions/S1003A02/workspace/scripts/gh_multicentre_energy.py).

## 3. General-background Burns response F

For any smooth closed oriented four-manifold \((M,g)\), point \(p\), and
unit \(\zeta\in\Lambda_p^+\), the explicit Burns insertion with
exceptional area \(\pi x_0\) and cutoff radius \(x_0^{1/5}\) gives
\[
 P(\hat g_{x_0})=P(g)+8\pi^2
 \bigl[1-x_0\mathbf R_p^+(\zeta,\zeta)\bigr]+O(x_0^{6/5}),
 \qquad \mathbf R^+=W^++sI/12.
\]
The analogous raw Einstein-residual expansion holds when the background is
Einstein. The proof uses the pointwise linearly scalar-flat and self-dual-flat
Burns tail and the exact cut-annulus fluxes
\[
 \Phi^{++}=\pi^2\zeta\zeta^T,\qquad
 \Phi^{--}=\frac{\pi^2}{3}I,\qquad \Phi^{+-}=0.
\]
The core volume estimate was repaired in Step 20. The theorem is an analytic
upper construction, supported by the exact symbolic transgression.

The first-order payment depends on ambient curvature and insertion direction.
A positive eigenvalue of \(\mathbf R^+\) permits a strict saving relative
to the standard \(8\pi^2\) insertion cost. Negative Kähler–Einstein
backgrounds have first-order-free directions \(\omega^\perp\); real
hyperbolic backgrounds have negative definite \(\mathbf R^+\).

No matching lower expansion is proved. In a reduced kernel-direction family,
the exact neck calculation predicts
\[
 P/(8\pi^2),\ J/(8\pi^2)
 =1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The coefficient is exact in that reduction. Theorem F's general
\(O(x_0^{6/5})\) remainder is too large to justify this second-order saving
in a general or moving background; a uniform batch-gluing remainder is also
missing.

Sources: [Step 20, §1](sources/Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md),
[transgression script](sources/Sessions/S1003A02/workspace/scripts/burns_transgression_flux.py),
[exact output](sources/Sessions/S1003A02/workspace/data/burns_transgression_flux.json),
and [theorem package, §4.2](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md).

## 4. Complete Einstein filling of O(-1) with nonstandard Rossi infinity

The ACH existence theorem, also named Theorem E in the notes, constructs a
complete real-analytic diagonal Bianchi–IX metric on
\(\mathcal O(-1)\to\mathbb{CP}^1\), with
\[
 \operatorname{Ric}=-6g,\qquad b=4/5,\qquad
 \rho_\infty\in[2.19013,2.19242].
\]
It approaches its ACH end at least at rate \(O(e^{-1.99t})\). The proof
combines an analytic Fuchsian bolt, constraint propagation, source-level
equivalence of the corrected CAPD field, interval transport of a tiled
parameter family, cusp-block inequalities, and a Ważewski staying-orbit
argument. Existence is not inferred from a floating shooting root.

Step 22 adds a computer-assisted non-conformal-Kähler theorem: both chiral
Weyl blocks have simple spectrum at the certified off-bolt orbit. Their
discriminants have positive lower bounds \(66.1883\) and
\(0.0006333125\). Analyticity therefore excludes conformal Kählerness on
any nonempty open set in either orientation.

This is a concrete existence result of potentially independent interest.
The literature comparison in the source does not amount to a comprehensive
priority certificate. The infinity is nonstandard Rossi, so this metric is
not a zero-cost exact-standard-CH-collar cell and does not prove
\(p_{1,0}=0\). Standard-boundary nonexistence, branch uniqueness, and
exhaustion of all Einstein fillings remain separate questions.

Sources: [Steps 15–17 proof](sources/Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md),
[Step 22, §5](sources/Sessions/S1003A02/workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md),
[validated transport](sources/Sessions/S1003A02/workspace/data/ach_capd/wazewski_T2.75.json),
and [Weyl certificate](sources/Sessions/S1003A02/workspace/data/ach_capd/weyl_discriminant_t0.5.json).

## 5. Certified subunit cells and the shared closed-manifold sub-4 upper bound

The strict cheap-cell construction and its improvements belong jointly to
A01/A02 and must be counted once. The latest referenced exact-dyadic Arb
enclosures, for \(x_0=0.03\), \(X=128\), degree 20, give
\[
 \frac{P}{8\pi^2}\in
 [0.995662732753254329\ldots,0.995662732771114200\ldots],
\]
\[
 \frac{J_6}{8\pi^2}\in
 [0.995670030344086466\ldots,0.995670030355130639\ldots].
\]
Smooth exact-collar approximation, suitable disjoint placement in selected
covers, and pure-handle recovery give an existential balanced family with
\[
 \limsup_j\alpha(M_j)/h_j<3.9961512+\varepsilon.
\]
This strictly improves the proposed coefficient 4 when \(\varepsilon\)
is chosen small. It is not a result for every prescribed cover tower, nor the
sharp coefficient, nor a theorem describing arbitrary near-minimizers.
The separated bookkeeping is \(28/9+(8/9)p_{1,0}\), not \(4p_{1,0}\).

Pure-handle marked-cell infima are
\(\mathfrak P_{0,\ell}=\mathfrak J_{0,\ell}=32\pi^2\ell\), approached
by shrinking cores and not attained for \(\ell>0\). Disjoint placement
also proves cell subadditivity and existence of the balanced specific-energy
infimum. Neither result proves mixed-cell additivity or identifies the cell
specific energy with the unrestricted closed-manifold coefficient.

Sources: [theorem package, §§4.3–5](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md),
[early A02 strict cell](sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md),
and the authoritative A01 certificates for
[P](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json),
[J](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_J_exact.json),
and [scalar energy](sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_S_exact.json).

## 6. Real-hyperbolic blow-ups and the conditional sharp theorem H

For a closed real-hyperbolic four-manifold \(Y\), the degree-one pinch map
from \(X_k=Y\#k\overline{\mathbb{CP}}^2\) combines with the established
Kotschick/Sambusetti/BCG entropy obstruction to exclude Einstein metrics for
every \(k>0\). This is an application of classical results, not a new
unrestricted positive critical-\(L^2\) gap theorem.

The exact same-metric identity is
\[
 P=8\pi^2k+4\int|W^+|^2+rac{S-Y_{\rm hyp}^2}{12}.
\]
Theorem H becomes sharp under the still-unproved hypothesis
\[
 \mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}.
\]
Then \(P(g)>8\pi^2k\) for each metric, \(\inf P=8\pi^2k\), and the
infimum is not attained. For \(1\le k\le2\chi(Y)\),
\[
 \alpha(X_k)=\inf\mathcal E=\inf\mathcal J
 =\frac{4k}{k+6\chi(Y)}.
\]
Nonattainment of this normalized value is proved for \(k<2\chi(Y)\).
At \(k=2\chi(Y)\), the infimum 1 is unconditional, but attainment is an
ASD question, with constant scalar curvature additionally needed for
\(\mathcal E\); the argument does not exclude it. Arbitrary minimizing
sequences become globally half-conformally-flat and Yamabe-extremal under H.
Allocating \(8\pi^2\) to each exceptional class is established only for
the explicit Burns sequences.

Without H, the Yamabe identity gives a quantitative conditional lower bound
in terms of \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\), and positivity if
\(y_k>1-k/(2\chi(Y))\). For \(k>2\chi(Y)\), pointwise
\(\mathcal J>1\) does not give a uniform separation: conformal inflation
gives \(\inf\mathcal J=1\).

Further restricted consequences are the Ricci-floor estimate
\[
 P\ge8\pi^2k-12\operatorname{Vol}(Y)
 [1-(1+\varepsilon)^{-2}]
\]
when \(s=-12\) and \(\operatorname{Ric}\ge-3(1+\varepsilon)g\), and
classical positive-energy rigidity for exact-hyperbolic-exterior cells under
the scalar floor. These retain their pointwise hypotheses.

Sources: [Step 21](sources/Sessions/S1003A02/workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md),
[Step 22, §§1–3](sources/Sessions/S1003A02/workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md),
and [Step 23, §3](sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md).

## 7. Relative channels, link charges, diagonal calibration, and selection

For a marked exact-ended cell and its scalar-\(-24\) Yamabe representative
\(\hat g=u^2g\), the two-channel identity is
\[
 P(g)-8\pi^2Q=4\Delta W_++48\,\mathrm{RV}(\hat g)
 +3\int(\Delta u/u)^2+24\int|\nabla u|^2.
\]
The relative volume uses matched truncations and the whole-cell conformal
integral. A01 supplies unconditional existence and sufficient decay of the
CH conformal reduction. The closed identity is already implicit in LeBrun;
the marked relative formulation and its use as a channel decomposition are
the present contribution. Numerical channel evaluations show positive
relative-volume cost and greater negative Weyl change for the cheap CH
witness. Positivity of relative volume for every competitor is not proved.

Chiral transgressions price boundary germs, including their radial jets.
An almost-Euclidean neck enclosing one exceptional class pays
\(P\ge8\pi^2-C\varepsilon\). In the stated finite-charge normalized
collapsed-jet class,
\[
 \mathfrak b_+^{\rm end}=-2-(C+4X)^2,
 \qquad\liminf\widehat P_{\rm to\ round}\ge4+(C+4X)^2.
\]
The symmetry-free characteristic–constraint identities extend the
bookkeeping, not the missing regularity theorem. General competitors have
not been shown to enter these controlled link or jet classes.

Step 35, after resumption, proves the exact diagonal calibration
\[
 \widehat P=\Delta\mathfrak b_++\int L(c-c^*),\qquad
 L(c)=3\bar H^2/16+\bar E^2/6+\bar D^2/8.
\]
Its kernel is trivial and calibrated curves are ASD scalar-flat metrics.
Burns is calibrated; Taub-bolt and CH are not. The invariant biaxial set and
transverse matrix are exact. Claims about the fates of sampled calibrated
leaves come from numerical integration. A denominator/path-cost estimate
valid along every competitor remains missing. The CH-renormalized A01
identity gives finite endpoint charges but has an indefinite Nijenhuis term;
its cost cannot be added independently to the raw Ricci cost.

The supercritical selection lemma gives \(P-p\le3\delta\) and
\(R_1(g)\le3R_1(g_0)\) from an already chosen \(\delta\)-near-minimizer
\(g_0\). It does not bound \(R_1(g_0(\delta))\), create a Sobolev bound,
or exclude collapse. Exact-collar Einstein nonexistence excludes attaining
zero; it does not exclude an infimum of zero through degeneration.

Sources: [Step 23, §1](sources/Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md),
[Step 30](sources/Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md),
[Step 33](sources/Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md),
[Step 34](sources/Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md),
[Step 35](sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md),
and [Step 19, §§3–4](sources/Sessions/S1003A02/workspace/notes/step19_theorem_package_and_selection_lemma.md).

## 8. Actual paired fields, Walsh charges, and the Nijenhuis/Weyl identities

For a single sign flip, the relative twisting line has
\(c_1(u)=\pm E_i\), not \(\pm2E_i\). With
\(h=(f-f')/2\), the exact completion is
\[
 |h^+|^2=(\rho-\rho')^2/8+|w|^2/2,
 \qquad\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
\]
Thus the fixed negative-square charge lies in the anti-self-dual curvature,
whereas amplitude and spin-direction differences measure the self-dual part.
The pair is the original singleton Walsh sector, not another additive
positive sector. The normalized bilinear pair \((u,w)\) is locally
\(S^3\)-valued where both spinors are nonzero; a zero of \(u\) may unwind
through orthogonality in \(w\), rather than forcing a scalar amplitude
vortex. Tube scaling arguments describe a possible mechanism, not an actual
closed family of monopole solutions realizing it.

In the scalar-\(-4\) convention, \(0\le\rho\le2\), actual solutions
give the amplitude bound
\[
 P\ge8\pi^2Q-4\mathbb E\int(2-\rho).
\]
The residual polynomial is positive only on the shallow band
\(0.7758\ldots<\rho<2\). Step 40 separates Lee torsion from the free
Nijenhuis component: Clifford contraction controls the former and has the
\(W_2\) first-jet component as its kernel. The resulting exact identity is
\[
 8\pi^2Q-P=\frac12\mathbb E\int\rho^2|\nabla n|_{W_2}^2-\mathcal B,
 \qquad\mathcal B\ge0.
\]
Here \(\mathcal B\) contains the explicit nonnegative depletion,
amplitude/Lee, Weyl-alignment and Walsh terms. The equivalent Weyl form, with
\(M=W^+-W_0\) and \(x=M(n,n)\), is
\[
 8\pi^2Q-P=\mathbb E\int[\rho^2x-4|M|^2]
 +\mathbb E\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3
 -4\mathbb E\|\zeta\|^2-\mathcal W.
\]
This identifies actual nonintegrable rotation as the saving channel and
connects it with the negative Nijenhuis term in A01's diagonal geometry.

The formulas permit \(Q=k+4\ell\), provided actual all-sign solutions
exist on the same metric and \(c^2=(2\chi+3\tau)(X)\). Handles require
the appropriate higher-type/holonomy-constrained supplier. Positive class
square ensures irreducibility, not supply; \(b^+\ge2\) alone does not
create monopole classes. General negative-Yamabe metrics are treated through
the normalized representative and \(P(g)\ge P(\hat g)\).

The Hermitian tariff \(P\ge8\pi^2Q\) requires a simultaneous chosen
solution family with integrable Bloch structures. The separate Kähler
blow-up tariff \(P>8\pi^2k\) is a classical Hodge-index/scalar-curvature
corollary for the fixed blow-up complex structure. Equality of its infimum
requires Kähler recovery; Riemannian Theorem F alone does not provide that.
The failed isolated invariant-cell shooting/BVP calculations produced no
monopole profile and do not decide the closed-host problem.

Sources: [Step 38](sources/Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md),
[Step 40, §§1–3](sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md),
[supply verification](sources/Sessions/S1003A02/trace/ttcs/results/step39_ttcs01_verifier2_integration.md),
and the inherited [simultaneous-field section](sources/Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex).

## 9. Affine pointwise exhaustion at the LeBrun threshold

The affine-exhaustion theorem, separately called Theorem E in Step 40,
concerns pure blow-ups. Constant affine combinations of the displayed
amplitude, Nijenhuis/Weyl and closed Weyl–volume identities, followed by
discarding known nonnegative terms and using
\(|M|^2\ge\frac32M(n,n)^2\), recover exactly
\[
 C_+\ge2A/3,\qquad P/(8\pi^2)\ge k-A/3.
\]
The exact envelope has contact at \(\rho=3/2\):
\[
 g_{2/3,2/3}=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0,
 \qquad\max_\lambda g_{t,\lambda}(3/2)=-\frac34(3t-2).
\]
This is a rigorous limitation of the specified scheme in the open range
\(0<k<A/3\). It does not exclude nonlinear inequalities, other weighted
Weitzenböck multipliers, or joint constraints among actual fields sharing
one \(W^+\). The broader package claim that the whole SW-identity route
is closed should be narrowed to this verified statement. The contact state
does not supply a closed metric or a compatible actual solution family.

Sources: [Step 40, §4](sources/Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md)
and [verifier, §6](sources/Sessions/S1003A02/trace/ttcs/results/step40_ttcs01_verifier1_integration.md).

## 10. Taubes periods, the AK profile, and the conditional Cotton scale

Step 42 assumes pure blow-ups, \(b^+(X)\ge2\), \(A>0\), and that the
complete basic-class set of \(X\) is exactly \(\{\pm K_X\}\) modulo
torsion. That last hypothesis is not automatic for every general-type
surface. A standard Taubes argument then gives, for every symplectic form,
\[
 K_\omega\cdot\omega=|K_X\cdot\omega|+\sum_i|E_i\cdot\omega|,
 \qquad |E_i\cdot\omega|>0.
\]
Consequently the Step-40 exact common mode—one nowhere-zero closed
self-dual field, shared by all signs, with every exceptional period zero—is
topologically impossible. This is a new application of a classical argument,
not a new Taubes theorem. Tiny positive periods and thin zero sets are not
quantitatively excluded. The perpendicular cell's closed form vanishes at
the bolt; it is not a global almost-Kähler structure there.

For a genuine almost-Kähler structure, put
\(\ell=8\pi K_\omega\cdot[\omega]\),
\(\theta=\ell^{-1}\int|\nabla\omega|^2\),
\(\eta=|K_X\cdot\omega|/\sqrt{2AV}\), and
\(\alpha_E=\sum|E_i\cdot\omega|/\sqrt{2AV}\). The corrected AKΓ bound is
\[
 C_+\ge\frac{\ell^2}{128\pi^2V}(3\theta^2-2\theta+1)
 =A(\eta+\alpha_E)^2(3\theta^2-2\theta+1).
\]
The initial inference \(\eta\ge1\) was false; it needs the Lorentzian
period hypothesis \(H_L\). The equality conditions and intrinsic
\(\ell\)-form survive. Under the necessary period condition, a linear
torsion estimate would imply a tariff. In the monopole form, if
\(P\ge\kappa\mathcal N\) with
\(\mathcal N=\frac12\mathbb E\int\rho^2|\nabla n|_{W_2}^2\), then
\(P\ge8\pi^2k\kappa/(1+\kappa)\). This is a conditional reduction,
not the missing coercivity theorem.

Step 43 gives the correct tensor
\(W_0=a(I/3-n\otimes n)\), \(a=\rho^2/4\), with spectrum
\((-\rho^2/6,\rho^2/12,\rho^2/12)\). On an almost-Kähler first jet,
\[
 |\delta W_0|^2=\frac13|da|^2+\frac{a^2}{2}|\nabla n|^2.
\]
The squared torsion singular value is \(1/2\), not the singular value.
For a closed constant-scalar almost-Kähler metric, its Cotton pairing gives
\[
 \frac12\int a|\nabla n|^2
 =\int\langle\operatorname{Ric}^{\circ},\mathcal C^*U\rangle
 -\int\langle W^+-W_0,\delta^*U\rangle.
\]
No required second-jet bound, monopole zero-set/band localization, or
noncircular alignment-error control has been proved. With total
\(R=\mathbb E\int|\nabla n|_{W_2}^2\), Theorem N gives
\(P\ge8\pi^2k-2R\). Only if one independently proves
\(P\ge R^2/(\Lambda A)\) does optimization yield
\[
 P\ge\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
 =\frac{16\pi^4k^2}{\Lambda A}+O(k^3/A^2).
\]
The AAD proper three-symmetric model and the Kirchberg identities test this
route; they are classical inputs. The local model has
\(|\operatorname{Ric}^{\circ}|^2/|\nabla\Omega|^4=9/64\), but gives no
closed counterexample. These pure-blow-up reductions do not close balanced
O11.

Sources: [Step 42](sources/Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md),
[Step-42 verification](sources/Sessions/S1003A02/trace/ttcs/results/step42_ttcs01_verifier1_integration.md),
[Step 43](sources/Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md),
and [Step-43 verification](sources/Sessions/S1003A02/trace/ttcs/results/step43_ttcs01_verifier1_integration.md).

## 11. Step 44: surviving perturbative estimates and the valid pocket inequality

The Step-44 note proposes a universal nonlinear canonical-branch theorem
near every compact complex-hyperbolic quotient. Its independent verifier
separates valid integrated estimates, an unproved uniform analytic passage,
and a false reverse comparison.

The pointwise Koiso calculation is valid. In scalar-\(-4\) normalization,
\[
 \langle L_Eh,h\rangle\ge\frac13\|h\|_2^2
 \qquad(h\text{ transverse-traceless}),
\]
uniformly over compact ball quotients. The conformal Hessian identity and
orthogonality to the TT channel support
\[
 P(g)\ge\kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr)
\]
once a uniformly small controlled slice
\(g=e^{2f}(g_\Gamma+k)\) has been supplied.

The corrected gauge-fixed SW estimate is
\[
 \|\mathcal L(a,\psi)\|^2\ge
 \tfrac12\|\nabla a\|^2+\tfrac12\|\nabla\psi\|^2
 +\tfrac{|\lambda|}{2}\|(a,\psi)\|^2.
\]
The source's full coefficient 1 on \(\|\nabla\psi\|^2\) double-counted
the derivative energy used to lift the zero algebraic-potential modes.
The \(L^2\) gap survives. G4 uses canonical amplitude
\(|\Phi_0|^2=4\), whereas Theorem N uses amplitude 2 at the same
scalar normalization. The spinor, quadratic map and equation-target norm
must be reconciled before combining their constants. The direction \(n\)
is unchanged by constant spinor rescaling. The verifier also corrects the
Dirac residual of the conformal ansatz to
\(\frac12e^{-2f}df\cdot\Phi\) in the stated isometric identification;
the needed \(O(df)\) estimate survives.

These estimates justify integrated coercivity and a local canonical branch
for each fixed quotient. A one-sided perturbative estimate
\(R\le C(g_\Gamma)P\), after consistent normalization, is the surviving
conclusion. Lifting unit balls and citing an \(L^2\) gap do not prove a
uniformly local Hölder inverse over all cocompact quotients. The universal
nonlinear slice, branch radius and constant still require that resolvent
theorem. Thus Theorem A's claimed universal nonlinear completion remains
open, although its linear/integrated mechanism has real content.

The reverse comparison is false. With
\(R=\int\rho^2|\nabla n|_{W_2}^2\), Theorem N at \(Q=0\) gives
\[
 -P=R/2-\mathcal B,\qquad\mathcal B\ge0.
\]
This only implies \(-P\le R/2\), not \(2P\le R\). In addition to
this inference error, the verifier gives a geometric counterexample to a
general lower comparison: nearby non-Einstein Kähler metrics have canonical
Kähler direction with \(\nabla n=0\), hence \(R=0<P\). Nijenhuis
energy detects nonintegrable rotation, not every Einstein defect.
Do not retain \(P\asymp R\) or the corresponding “perturbative regime
settled” summary.

Proposition Π is independently valid. On a closed almost-Kähler manifold
with \(\ell=8\pi K_\omega\cdot[\omega]>0\), let
\(\theta=\ell^{-1}\int|\nabla\omega|^2\) and
\(\varphi=\operatorname{Vol}\{s^*\ge0\}/V<1\). Two-region Jensen
gives
\[
 C_+\ge\frac{\ell^2}{128\pi^2V}
 \left[\Gamma(\theta)+\frac{\varphi}{1-\varphi}(1-\theta)_+^2\right]
 \ge\frac{\ell^2}{128\pi^2V}\frac2{3-2\varphi},
 \qquad\Gamma(\theta)=3\theta^2-2\theta+1.
\]
The minimum occurs at \(\theta=1/(3-2\varphi)\). For
\(0<\varphi<1\), the verifier strengthens the correction above \(\theta=1\)
to \((1-\varphi)(\theta-1)^2/\varphi\), without changing that minimum.
Also
\[
 \mathbf R^+(\hat\omega,\hat\omega)=s^*/4,
\]
so an aligned Burns insertion saves at first order precisely where
\(s^*>0\). This is a valid refinement of the AK profile, not a
per-exceptional-class tariff. Conversion to the topological \(A\)-bound
retains the period hypothesis.

Neither result supplies a surgery-bulk estimate. Step 44 itself identifies
missing canonical-branch selection for actual monopoles on the blow-up and
an uncontrolled outer-layer term in local coercivity. Applying its canonical
monopole estimate to an arbitrary almost-Kähler pocket requires the same
structure and a valid local estimate. A small pocket volume alone does not
locate the pockets outside every KE neighborhood.

Sources: [Step-44 note](sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md),
[independent verifier](sources/Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub1_verifier.md)
(G4/normalization: lines 162–193; uniform inverses: 240–263; reverse comparison:
288–327; pocket proof: 331–433),
[script](sources/Sessions/S1003A02/workspace/scripts/step44_perturbative_ke.py),
and [stored output](sources/Sessions/S1003A02/workspace/data/step44_perturbative_ke.json).

## 12. Corrections, numerical boundaries, and the unresolved global implication

The following corrections govern the interpretation of the preserved sources.

- The Step-6 assertion that Ricci-flat cores contribute zero to
  \(\int|\operatorname{Ric}+g|^2\) is replaced by the shrinking-volume
  argument. Its “not complex” claim for Şuvaina examples is reduced to the
  sourced non-Kähler statement.
- The early relative-orientation scan supporting Kähler first-order
  optimality and coefficient 4 was superseded by the perpendicular
  construction and Theorem F. It is not another positive result to accumulate.
- The original Step-16 CAPD pilot used the wrong mean-potential field and is
  void. The repaired field and analytic bolt boxes support the later ACH
  existence proof. The first bolt Weyl spectra had a symbol-collision error;
  the corrected bolt spectra and off-bolt certificate replace them.
- The first Step-35 AK evaluation of scale-free connectors ignored scale
  factors and is invalid. A whole-cell endpoint identity cannot be applied
  to a connector with a collapsed entry by replacing its boundary term by 1.
- Diagonal branch scans, small-bolt matching, saturation values tending to
  4, and non-round optimizer costs around 5.4–6.6 are numerical structures.
  Feasible local-optimizer values are upper bounds, not general lower bounds.
  Fixed-object Arb/CAPD enclosures have a distinct, certified status.
- The paired-field “blindness” and affine-exhaustion statements do not rule
  out every possible algebraic or differential use of the full monopole
  family. AKΓ retains its period factor and \(H_L\) where needed.
- The formal common mode is not an actual closed-manifold counterexample;
  its exact realization is excluded under the Step-42 hypotheses. Approximate
  zero-set or tiny-period modes have not been excluded. No formal
  \(P=o(k)\) calculation disproves the original balanced-family linear gap.
- Step 44 has valid integrated gaps and a valid pocket inequality, an open
  universal nonlinear inverse/slice passage, and a false two-sided
  \(P\)-versus-Nijenhuis comparison. These statuses must remain separate.

The main unresolved implication is concrete: arbitrary genuine near-minimizers
must either enter a regime where an actual-field or geometric coercivity
estimate applies, or pay a quantitative cost for failing to do so. Present
work does not establish that implication. It also does not prove positivity
of the standard-CR cell infimum, equality of global and cell asymptotics, or
the optimal balanced O11 lower coefficient. The pure-blow-up Step-42/43
reductions cannot be substituted for the blow-up-plus-handle problem.

The most valuable completed outputs, counting joint work once, are the
strict closed-manifold sub-4 upper construction, the nonstandard-boundary
\(O(-1)\) Einstein filling, and the general-background Burns response.
For A02-specific contributions, the uniform density-free L′/K extension
belongs alongside the latter two. The most substantial post-resumption
advance is the actual-field Nijenhuis/Weyl mechanism and its precisely
bounded exhaustion result; it has not yet produced a new unrestricted gap.

Sources: [theorem package, §§7–9](sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md),
[Step 19](sources/Sessions/S1003A02/workspace/notes/step19_theorem_package_and_selection_lemma.md),
[Step 35, §5](sources/Sessions/S1003A02/workspace/notes/step35_calibration_theorem_and_branch_classification.md),
and [Step-44 verifier](sources/Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub1_verifier.md).
