# Step 10: corrected collapse range and the fixed-scale accessible-cover program

## 1. Research position after the Step 9 repair

The four-dimensional negative-branch work remains centered on a hypothetical Ishida--LeBrun near-critical sequence

\[
\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{L^\infty,\mathrm{op}}\to0
\]

on manifolds where the mixed Seiberg--Witten estimate applies. The valid accumulated chain is:

1. The mixed LeBrun estimate and Chern--Gauss--Bonnet bookkeeping force a nonnegative calibrated defect density
   \[
   F_i=|\operatorname{Ric}_{g_i}+g_i|^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i
   \]
   whose global mean tends to zero in the near-critical regime. The pointwise gap is
   \[
   \mathcal G_i=f_i^2-(a_i^-)^2,
   \quad f_i={2\over3}s_i-2\sqrt{2/3}|W_i^+|,
   \quad a_i={2\over3}s_i+2w_i,
   \]
   where \(w_i\) is the least eigenvalue of \(W_i^+\).
2. If a fixed-scale harmonic chart on a cover sees small mean of \(F_i\), the harmonic-coordinate compactness gives a smooth local limit with \(\operatorname{Ric}=-g\).
3. Vanishing of the three terms in \(F_i\) at the limit gives
   \[
   s=-4,\qquad |W^+|={1\over2\sqrt6},\qquad
   \operatorname{Spec}(W^+)=(-1/6,1/12,1/12).
   \]
4. This local Einstein germ is impossible. Derdzinski's local theorem makes the constant two-eigenvalue harmonic \(W^+\) metric locally conformal to Kähler by the factor \((24|W^+|^2)^{1/3}g\); at the calibrated spectrum the factor is constant, so the metric is locally Kähler, contradicting \(|W^+|^2=s^2/24=2/3\) for \(\operatorname{Ric}=-g\). The independent projector calculation gives the same contradiction: constant two-eigenvalue harmonic \(W^+\) makes the simple eigenform parallel, while the Einstein--Weyl identity at the calibrated spectrum gives \(|\nabla W^+|^2=1/16\).
5. The Step 9 normal-cover mean theorem is valid and now becomes the main bridge: for a buffered normal Riemannian cover with \(\operatorname{Ric}\ge -(n-1)Kg\),
   \[
   \fint_{B_r(\hat p)}\pi^*\phi
   \le {V_{-K}^{(n)}(3r)\over V_{-K}^{(n)}(r)}
   \fint_{B_r(p)}\phi
   \]
   for every nonnegative measurable \(\phi\). The sheet number cancels; no torus or nilpotent lattice counting is needed.

The false Step 9 conclusion was not in this chain. The statement "all regular collapse is excluded" is unsupported and has been withdrawn.

## 2. Corrected range of the orbit-volume evidence

The abelian orbit-volume identity is a theorem about exact adapted metrics with a free isometric \(\mathbb R^N\)-action and a globally defined orbit-volume function \(v=\sqrt{\det G}\). I fetched Lott's primary source directly from arXiv and saved it as

- `workspace/data/sources/lott_1708_06780_collapsing_almost_ricci_flat_4_manifolds.pdf`
- `workspace/notes/sources/lott_1708_06780_collapsing_almost_ricci_flat_4_manifolds.txt`

Lines 279--345 of the extracted text give the setup and equation (2.9). In Lott's notation, for \(\operatorname{Ric}(M,g)=\lambda g\),

\[
\Delta_B \sqrt{\det G}=\left({|F|^2\over4}-\lambda N\right)\sqrt{\det G}.
\]

Proposition 2.10 then uses three additional ingredients: the base is parabolic, \(\lambda\le0\), and \(\sqrt{\det G}\) is bounded above. Under those hypotheses the orbit volume is constant, \(F=0\), and \(\lambda=0\). For the negative normalized sign \(\lambda=-1\), the right-hand side is positive wherever \(v>0\), but this only yields a contradiction when a global boundary, periodic, or Liouville argument is available.

Thus the supported abelian conclusions are:

- A circle base is excluded by integrating \(v''\) over the period.
- A parabolic base is excluded only with the bounded-above orbit-volume hypothesis used by Lott.
- A local interval model is not excluded. The real-hyperbolic torus cusp
  \[
  dt^2+e^{2t/\sqrt3}g_{T^3}
  \]
  satisfies \(\operatorname{Ric}=-g\) and has regular abelian torus fibers on an interval. It calibrates the fact that the orbit-volume equation detects global flux or endpoint behavior, not local nilpotent symmetry itself.

The non-abelian \(\mathrm{Nil}^3\) calculation is also corrected. With \(\mu=a_3^2/(2a_1^2a_2^2)\), the equation is

\[
 v''=(3-\mu)v,
\]

not \((3+\mu)v\). Circle-base exclusion can still survive, but only using additional periodic identities such as the trace-subsystem maximum principle or a monotonicity identity of the form \((vq)'=(1-3\mu)v\); it does not follow from \(v''=(3-\mu)v\) alone. Interval cusp models remain possible; the complex-hyperbolic cusp is the calibration, though any future use should include an explicit coframe normalization check.

These orbit-volume identities remain useful model theorems. They should not be used as a classification of all Ricci-bounded collapse, nor as a proof that a fixed-topology negative pinching gap has been obtained.

## 3. What the cusp calibrations do and do not mean

The existence of a real-hyperbolic torus cusp or a complex-hyperbolic nil cusp does not by itself provide an escape for a near-saturating LeBrun sequence. If such a cusp region has a fixed physical scale on which a normal cover unwraps to a noncollapsed harmonic chart, then the cover-mean theorem transports the small mean of \(F_i\) to the cover and the forbidden-spectrum argument applies. Therefore a cusp-like local Einstein model can occupy positive volume proportion only by failing fixed-scale accessibility: for example, the available unwrapping scale may shrink to zero, the lower-dimensional model may degenerate, maximal rank may fail, or the curvature/topology may concentrate outside the typical mean-defect regime.

This is the sharp research target now: not to classify every possible local torus or nil model, and not to prove a pointwise curvature bound on the original collapsed metrics, but to understand whether a positive volume proportion of the collapsed sequence admits controlled harmonic charts on normal covers at a fixed physical scale.

## 4. Source-grounded accessible-cover theorem

A precise version should be stated for arbitrary measurable subsets rather than relying on the measurability of a geometrically defined set. Let `E_i subset M_i` be measurable in a near-critical LeBrun sequence. Suppose that for every `p in E_i`, at a fixed unit scale, the following Naber--Zhang package holds with constants depending only on a chosen lower model scale `r_*>0`:

1. `B_2(p)` has the local completeness required by Naber--Zhang, for instance `closure B_2(p) subset B_4(p)` in the relevant local domain, and `|Ric|<=3` after normalization.
2. For some `0<=ell<=k<=4`, `ell<=3`, the ball `B_2(p)` is Gromov--Hausdorff close, at the Naber--Zhang smallness scale `delta_*(4,r_*)`, to `B_2(0^{k-ell},z^ell) subset R^{k-ell} x Z^ell`.
3. The Ricci-limit factor `Z^ell` has model noncollapsing radius at least `r_*` on `B_1(z^ell)`, so the constants in Proposition 6.4 are uniform.
4. The fibered fundamental group at the same scale satisfies `rank Gamma_{delta_*}(p)=4-k`.

Naber--Zhang Proposition 6.4 (source lines 1437--1454) then gives a positive `C^1` harmonic radius `h_*=h_*(4,r_*)` for every lifted point in the local universal cover. Theorem 5.1 (source lines 914--925 and 1366--1370) supplies the noncollapse and splitting input behind this statement. The curvature bound in Proposition 6.5 requires either Einstein or a bound on `|nabla Ric|`; it is not available for our approximating metrics. We only use harmonic radius and the finite `W^{2,p}` bounds that bounded Ricci gives in harmonic coordinates.

Choose a radius

\[
0<a<\min\{1/4,h_*/4\}
\]

so the cover ball and its `3a` comparison core remain inside the local universal cover domain. If `Vol(E_i)>=eta Vol(M_i)` for some `eta>0`, fixed-radius averaging for nonnegative functions under the Ricci lower bound gives points `p_i in E_i` with

\[
\fint_{B_a(p_i)}F_i\to0.
\]

The normal-cover mean theorem, in its precompact-buffer form `closure(B_{3a}(\tilde p_i)) compactly contained in the cover domain`, transports this to

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i\to0.
\]

On a smaller harmonic chart choose finite `p>4`. Bounded Ricci gives uniform `C^{1,alpha}` and `W^{2,p}` control, and the harmonic-coordinate equation with `Ric_{g_i}=-g_i+e_i`, `||e_i||_{L^infty}->0`, gives strong `W^{2,p}` convergence after shrinking. The limit is smooth and satisfies `Ric=-g`. Curvature quantities and the eigenvalues of `W^+` pass in `L^1` because eigenvalues of symmetric matrices are Lipschitz functions of their entries. The vanishing mean of `F_i` therefore gives

\[
s=-4,\qquad |W^+|^2={1\over24},\qquad
\operatorname{Spec}(W^+)=(-1/6,1/12,1/12).
\]

This is the forbidden local Einstein germ from Section 1. Consequently every such measurable `E_i` satisfies

\[
 {\operatorname{Vol}E_i\over\operatorname{Vol}M_i}\longrightarrow0 .
\]

This theorem is independent of exact torus/nil orbit-volume classification. The remaining collapsed mass must lie in points failing the fixed-scale Naber--Zhang package: rank drop, model-scale degeneration, residual four-dimensional cores, singular fibers, or only shrinking-scale unwrapping. At a shrinking scale the Einstein constant rescales away, so the calibrated `Ric=-g` spectral contradiction does not persist automatically.

## 5. Energy bookkeeping needed for the next bridge

The full-curvature energy must be handled with the correct four-dimensional formulas. The signature identity is

\[
12\pi^2\tau(M)=\int_M(|W^+|^2-|W^-|^2)d\mu,
\qquad \tau(M)=\tau(X)-k
\]

for \(M=X\# k\overline{\mathbb {CP}}^{2}\). Hence

\[
\int |W^-|^2=\int |W^+|^2-12\pi^2(\tau(X)-k),
\]

not \(\int|W^+|^2+32\pi^2k\). The latter drops the contribution of \(X\) and has the wrong coefficient.

With the curvature-operator Hilbert--Schmidt convention

\[
|\mathcal R|^2=|W^+|^2+|W^-|^2+{1\over2}|E|^2+{s^2\over24},
\]

the Chern--Gauss--Bonnet decomposition gives

\[
\int |\mathcal R|^2
=8\pi^2\chi(M)+\int |E|^2
=8\pi^2(\chi(X)+k+J)
\]

with \(J=(4\pi^2)^{-1}\int |E|^2/2\). If one instead uses the usual \((0,4)\)-curvature tensor norm, the corresponding coefficients are multiplied by the standard factor relating the two conventions; the route only needs a fixed convention and an \(O(A)\) bound. Therefore a normalized \(O(A)\) full-curvature-energy budget follows when \(\chi(X)/A\), \(k/A\), and \(J/A\) are bounded. Under \(\operatorname{Ric}+g=o_{L^\infty}(1)\) and \(\operatorname{Vol}/A=O(1)\), one has \(J/A\to0\); the nontrivial extra topology input is the chosen algebraic-surface family bound for \(\chi(X)/A\). This is not a pure consequence of Ricci pinching alone.

The script `workspace/scripts/step10_energy_budget_lebrun.py` verifies these identities and the calibrated values

\[
\operatorname{Vol}\sim {32\over9}\pi^2A,
\quad \int {s^2\over24}\sim {64\over27}\pi^2A,
\quad \int |W^+|^2\sim {4\over27}\pi^2A.
\]

For local selection the meaningful scale-invariant quantity is

\[
r^4\fint_{B_r(p)}|\mathcal R|^2,
\]

not the absolute energy of a collapsed ball. If the normalized global full-curvature mean is bounded, the same fixed-radius averaging method selects many neighborhoods with controlled mean energy. The normal-cover mean theorem preserves such control upstairs. What is still missing is a theorem turning this transported mean energy plus near-Einstein equation into the fixed-scale harmonic-chart accessibility needed above, or a proof that Naber--Zhang's model/rank hypotheses hold on most of the collapsed volume.

Small Ricci defect alone should not be treated as a pointwise curvature estimate. The Weyl divergence contains derivatives of the Schouten tensor; with only \(L^\infty\) Ricci defect it gives weak integrated identities after moving derivatives onto smooth test tensors, not the pointwise forcing used in Einstein curvature estimates. Harmonic coordinates provide finite \(W^{2,p}\) control from bounded Ricci, not \(W^{2,\infty}\) control or a curvature supremum bound for the approximating metrics.

## 6. Positive branch and Cheeger--Naber range

S0910A02's positive-branch use of Cheeger--Naber has a valid four-dimensional core and an unsupported all-dimensional extension.

Valid four-dimensional statement. Cheeger--Naber Theorem 1.12 (source lines 101--103) says that in dimension four, \(|\operatorname{Ric}|\le3\), a lower bound on every unit-ball volume, and a diameter bound imply only finitely many diffeomorphism types. Positive pinching \(|\operatorname{Ric}-g|\le\delta<1\) supplies Myers diameter control, and a lower total-volume bound supplies the unit-ball lower volume bound by Bishop--Gromov. Therefore for the Sha--Yang family \(\#_k(S^2\times S^2)\), either the normalized positive pinching defects stay away from zero along the large-\(k\) tail, or any near-positive-Einstein sequence collapses in total volume.

What this does not prove. Finitely many diffeomorphism types do not produce an Einstein metric on any one of them. The bridge from near-positive-Einstein metrics to an actual Einstein metric on the same smooth manifold still requires additional mathematics. In the noncollapsed smooth-convergence case it is standard; in the noncollapsed orbifold case it requires an approximate-to-exact obstruction projection or desingularization analysis; in the collapsed case it remains the hard part.

All-dimensional distinction. Cheeger--Naber Theorem 1.4 is all-dimensional codimension-four regularity for noncollapsed bounded-Ricci limits. Theorem 1.12 is explicitly a four-dimensional finiteness theorem. Thus the statement "noncollapsed two-sided Ricci bounds give finitely many diffeomorphism types in all dimensions" is not supplied by this source. The all-dimensional positive branch still lacks both a general finiteness theorem of that strength and, more importantly, an existence bridge from near-Einstein geometry to an Einstein metric on the original smooth manifold.

## 7. Current best research direction

The negative-branch LeBrun route has not proved or disproved Yau's Problem 26, but it has created a precise obstruction architecture. The best next construction/verification work is to attack the fixed-scale accessibility question:

- Use Naber--Zhang to identify geometric conditions under which collapsed neighborhoods unwrap to noncollapsed harmonic charts at a fixed physical scale.
- Determine whether near-critical LeBrun sequences force those conditions on a positive volume proportion, perhaps using the normalized full-curvature energy, topology distribution, or the calibrated defect density.
- If the conditions fail on most volume, characterize the failure: rank drop, degenerating model scale, residual four-dimensional cores, singular fibers, shrinking-scale unwrapping, or curvature/topology concentration.
- In parallel, keep the positive-branch Cheeger--Naber dichotomy precise: noncollapsed four-dimensional positive pinching gives finite diffeomorphism types, not Einstein existence; total collapse remains a substantive phenomenon rather than a small technical input.

This is still Explore work because the central mathematical bridge is not established. The next agent should not write final exposition or formalization; it should build or refute the accessibility bridge with source-level precision and, where possible, concrete model calculations.