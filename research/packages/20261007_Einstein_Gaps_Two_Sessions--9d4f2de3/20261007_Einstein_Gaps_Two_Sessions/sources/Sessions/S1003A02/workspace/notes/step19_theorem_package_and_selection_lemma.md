# Step 19 — theorem package, independent reading of Theorem E, and the supercritical selection lemma

## 1. Consolidated mathematical package

The dependence-ordered research package is now

`workspace/notes/theorem_package_v1.md`.

It separates the direct defect, trace-free Ricci energy, and alignment functionals; records the actual-field bulk theorems; separates zero infimum from attainment; states the signed marked-cell response at its proved scope; retains the general Burns transgression and the full logarithmic remainder as open; records both certified cells and the improved balanced upper coefficient; distinguishes construction-level cell subadditivity from the unrestricted closed-manifold infimum; and includes Theorem E with its exact bolt geometry. The package is a research map, not a manuscript or a completion statement.

The common mechanism that survives this separation is:

1. an actual metric-wise field and its differential identities control the regular bulk;
2. a topology change is realized by a complete marked cell whose cost responds to the ambient self-dual curvature;
3. first-order-free directions can use a negative quadratic interaction, while handles retain a different exact cost;
4. exact Einstein filling may require changing the boundary CR structure;
5. the unrestricted \(\alpha\)-problem still needs a passage from global near-minimizers to regular bulk plus marked cells or collapse.

The first-order law for arbitrary bulk, the error-controlled \(-9\) kernel law, \(p_{1,0}>0\), equality of global and cell asymptotics, and standard-CR diagonal nonexistence remain open in the same package.

## 2. Independent mathematical reading of Theorem E

The proof in `workspace/notes/step15_ach_projected_theory.md` and its source artifacts were read as one argument rather than as unrelated computations.

### 2.1 Regular bolt

With \(s=t^2\), \(a_1=A(s)\), \(a_2=B(s)\), and \(a_3=tC(s)\), `workspace/scripts/ach_bolt_fuchs.py` verifies algebraically that its three Fuchsian equations are equivalent to the diagonal Einstein equations. For
\[
(\sigma,\delta,\gamma)=((A+B)/2-b,A-B,C-1),
\]
the linear part is
\[
(4D^2,\ 4D^2-16,\ 4D^2+2D),\qquad D=s\partial_s.
\]
The only positive-integer resonance is the \(s^2\) coefficient of \(\delta\), which is the free bolt parameter \(d\). The remainder starts at order \(s^7\), so it does not change this coefficient. The radial inverses on functions vanishing to order seven have the displayed factors \(1/(4m^2)\), \(1/[4(m-2)(m+2)]\), and \(1/[2m(2m+1)]\), together with their \(D\)-bounds.

The complex-disc enclosure covers \(|s|\le10^{-4}\) and gives a self-map with Lipschitz factor \(0.03251\). Hence the fixed point is holomorphic in \(s\), not merely a solution on the positive real axis. The parity conditions \(A,B,C\) analytic in \(s\), \(C(0)=1\), and \(A-B=O(s^2)=O(t^4)\) are exactly the regular \(\mathcal O(-1)\) bolt conditions in this normalization. Constraint propagation has \(\mathcal C'=-2S\mathcal C\); since \(S\sim t^{-1}\) and the regular series has \(t^2\mathcal C\to0\), the constraint vanishes identically.

There is one minor interval-implementation point to repair for a completely literal rerun: the residual and Jacobian suprema at lines 204 and 227 are converted from Arb upper endpoints to ordinary binary64 without applying `nextafter` toward \(+\infty\). The recorded self-map has roughly a factor-two margin and the contraction factor is only \(0.03251\), so multiplying all such stored suprema by \(1+10^{-12}\) is far inside the proved inequalities and absorbs binary64 rounding. The argument is unchanged, but the script should use directed outward conversion and be rerun before this computation is exported as a standalone certificate.

### 2.2 Validated passage and staying orbit

`workspace/scripts/ach_capd_field_check.py` parses the vector field directly from `ach_bolt_capd.cpp`; its symbolic difference from the exact anisotropy-resolving Einstein field is zero in all seven components. The corrected mean-potential cancellation is therefore present in the code actually transported. The Fuchsian boxes are converted to outward binary64 endpoints, and CAPD transports a tiled parameter interval to \(T=2.75\).

The block computation verifies that the stable faces are inward, both unstable faces are outward, \(\zeta\) decreases, and a staying orbit cannot reach a \(q\)-face because the total future drift is smaller than its recorded distance from those faces. The first and last parameter boxes lie in opposite unstable slabs. Continuity of the bolt family and the exit map therefore gives a parameter whose orbit stays in the block for all future time. This is the required Ważewski argument; the construction does not infer existence from a floating root.

Inside the block, \(\zeta'\le-1.99846\zeta\), all nonneutral coordinates are \(O(\zeta)\), and
\[
\widetilde\Phi=q+(y_g-y_h)/4-\zeta\sinh q,
\qquad |\widetilde\Phi'|\le19.5826\zeta^2.
\]
Thus the radial time extends to infinity, the metric is complete, its curvature approaches the ACH equilibrium, and the integrated drift gives
\[
\rho_\infty\in[2.1901328141,2.1924133695].
\]
[Corrected in Step 20 after peer message 771.] The repaired exact bolt Weyl blocks are diag(−41/16,−41/16,41/8) and diag(−91/16,−91/16,91/8), with squared norms 5043/128 and 24843/128; the earlier three-distinct-eigenvalue values came from a symbol collision. Both blocks are nonzero, so the metric is neither half-conformally-flat. Non-Kählerness follows because a Kähler metric with s=−24 must have Kähler-side Weyl spectrum exactly (−4,2,2), with norm 24, and neither block has this spectrum in either orientation. See theorem_package_v1.md §6.2.

The Biquard--Herzlich curvature integral was not computed in this Step. It is an optional independent branch validation and should first return the CR \(\nu\)-invariant from the convergent combined density; conversion to the Burns--Epstein invariant needs its additive contact normalization.

## 3. Supercritical selection: the valid lemma

Work on one closed negative-Yamabe four-manifold in the scalar-normalized class
\[
\mathcal S_{-4}=\{g\in C^\infty:\ s_g=-4\}.
\]
Set
\[
p=\inf_{\mathcal S_{-4}}P,
\qquad R_1(g)=\int|\nabla\operatorname{Rm}_g|^2\,d\mu_g.
\]
Let \(\delta>0\), choose smooth \(g_0\in\mathcal S_{-4}\) with \(P(g_0)\le p+\delta\), and suppose \(0<R_1(g_0)<\infty\). Put \(\varepsilon=\delta/R_1(g_0)\). If a smooth \(g\in\mathcal S_{-4}\) satisfies
\[
P(g)+\varepsilon R_1(g)
\le \inf_{\mathcal S_{-4}}(P+\varepsilon R_1)+\delta,
\]
then
\[
P(g)+\varepsilon R_1(g)
\le P(g_0)+\varepsilon R_1(g_0)+\delta
\le p+3\delta.
\]
Consequently
\[
0\le P(g)-p\le3\delta,
\qquad R_1(g)\le3R_1(g_0).
\]
No attained minimum, gauge choice, or Euler equation is needed: a smooth approximate minimizer exists by the definition of the infimum. The scalar normalization is essential because \(P\) is scale invariant while \(R_1(c^2g)=c^{-2}R_1(g)\). If \(R_1(g_0)=0\), the comparison metric has parallel curvature and should be treated separately rather than defining \(\varepsilon\) by division.

A smooth exact-collar cell has finite \(R_1\). The certified profiles are initially matched through the second jet; multiplying their third-order collar deviation by a flat cutoff produces a smooth exact-collar metric with finite \(R_1\) and arbitrarily small change of the quadratic curvature cost. A smooth closed gluing and its smooth scalar-minus-four Yamabe representative also have finite \(R_1\).

## 4. Why the lemma does not yet remove concentration

The energy comparison is correct, but the stronger compactness conclusion proposed for it does not follow.

### 4.1 The comparison depends on \(\delta\)

For each \(\delta\), define the regularity profile
\[
\mathcal R_*(\delta)=
\inf\{R_1(g):g\in\mathcal S_{-4},\ P(g)\le p+\delta\}.
\]
The lemma gives a selected metric with \(R_1\le3R_1(g_0)\), and optimizing the comparison gives essentially \(R_1\lesssim\mathcal R_*(\delta)\). It gives a uniform derivative bound as \(\delta\downarrow0\) only if
\[
\sup_{0<\delta<\delta_0}\mathcal R_*(\delta)<\infty.
\]
That is new geometric information, not a consequence of the comparison. A certified construction cannot be substituted for \(g_0\) at arbitrarily small \(\delta\) unless it is already known to lie within \(\delta\) of the unknown infimum. Choosing an arbitrary smooth \(\delta\)-near-minimizer supplies finite \(R_1(g_0)\), but that number may diverge arbitrarily fast as \(\delta\to0\).

This dependence is particularly important for the balanced family. Fixed-size smooth blow-up cells have finite derivative energy per cell before scalar normalization, but the sharp handle value is approached by shrinking cores, and neither the handle scales nor the derivatives introduced by the global Yamabe replacement have yet been bounded uniformly. Even a total estimate \(R_1=O(A_j)\) would allow one concentration scale as small as \(A_j^{-1/2}\), because a fixed-profile bubble at scale \(r\) has derivative-curvature cost of order \(r^{-2}\). An extensive total bound does not give local equiintegrability.

### 4.2 Intrinsic derivative energy is not a uniform Sobolev estimate

For a fixed metric with Sobolev constant \(C_S(g)\),
\[
\|\operatorname{Rm}\|_4^2
\le C_S(g)\bigl(\|\nabla\operatorname{Rm}\|_2^2+	ext{lower-order term}\bigr).
\]
A uniform conclusion therefore needs a uniform local Sobolev or harmonic-radius input. The intrinsic bound on \(\int|\nabla\operatorname{Rm}|^2\) does not itself provide that input. Global volume noncollapse alone, with only \(s=-4\) and an \(L^2\) trace-free Ricci bound, does not give uniform volume ratios, Ricci bounds, or harmonic coordinates.

The retrieved regularity literature reinforces this distinction. Anderson--Bando--Kasue--Nakajima compactness applies to Einstein metrics with diameter, volume, and \(L^2\)-curvature control; the Ricci-flow regularity results require a flow equation and scalar/Ricci hypotheses. These equations are precisely what the selected metrics do not yet possess uniformly. Thus the statement “curvature is bounded in \(W^{1,2}\), hence in \(L^4\), hence harmonic-coordinate compactness” is valid only after a uniform Sobolev/harmonic-radius structure has been supplied.

### 4.3 Correct mathematical consequence

The elementary lemma converts any *already uniformly regular* family of comparisons approaching \(p\) into a uniformly regular selected near-minimizing family. It does not create such comparisons. Conditional on

- \(\sup_jR_1(g_{0,j})<\infty\) (or a suitable locally equiintegrable analogue),
- uniform local Sobolev/volume-radius control on the noncollapsed region,
- the corresponding harmonic-coordinate theorem,

the supercritical bound can exclude fixed-energy bubbles whose scales tend to zero in that region. Collapse and topology accounting would still require separate arguments.

## 5. Revised compactness front

The useful next object is the regularity profile \(\mathcal R_*(\delta)\), not merely the penalized functional. There are three possible advances:

1. prove a uniform or quantitatively controlled upper bound for \(\mathcal R_*(\delta)\) from a new construction that approaches the true infimum, rather than only the known upper construction;
2. derive from an approximate Euler equation for \(P+\varepsilon R_1\) a local Sobolev/harmonic-radius estimate whose constants depend on the controlled combination \(\varepsilon R_1\) in a way that survives \(\varepsilon\to0\);
3. formulate a local regularizer or concentration function whose comparison bound is equiintegrable, not merely extensive.

Any of these would connect the lemma to the desired bulk/cell decomposition. Without one of them, Anderson's existing ideal-minimizer theorem remains stronger on fixed topology, while the family-uniform, marked-cell and actual-field passage stays open. The matrix-valued Burns transgression remains the complementary local theorem of broad reach.
