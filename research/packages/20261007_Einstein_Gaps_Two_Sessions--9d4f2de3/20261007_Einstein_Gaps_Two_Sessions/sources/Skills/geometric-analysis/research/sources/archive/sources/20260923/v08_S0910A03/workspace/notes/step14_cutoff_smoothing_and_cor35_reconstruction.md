# Step 14: Corollary 3.5 reconstruction and normalized local-flow interface

## 1. Correction to the Step 13 propagation argument

The inner/outer estimate written in Step 13,

\[
\frac d{dt}Y_{\rm inner}(t)\le C r^{-2}Y_{\rm outer}(t),
\]

does not imply a Gronwall estimate for \(Y_{\rm inner}\).  The right side is a different, uncontrolled quantity.  Moreover, the initial normalized curvature energy was used as though it remained small throughout the flow.  That persistence is itself part of Ye Li's maximal energy bootstrap.  The numerical absorption example in `verify_L2_sobolev_absorption.py` checked only the coefficient algebra and supplied neither of these missing steps.  Sections 4.2--4.5 and the asserted local proposition in `step13_smoothing_bridge_and_L2_propagation.md` are therefore superseded by this note.

There is, however, a stronger source-based propagation statement.  Ye Li's Corollary 3.5 packages the nested-cutoff, covering, evolving-energy and Moser arguments that were missing from the ad hoc estimate.  It gives the desired defect bound whenever its dynamic hypotheses are available.

## 2. Exact source scope of Ye Li's theorem

The actual all-centres statement is explicit in Theorem 3.1: for **all** \(x\in M\),

\[
\|\mathrm{Rm}(g_0)\|_{L^2(B_r(x))}
 \le [C_1 C_s(B_r(x))]^{-1},
\qquad |\mathrm{Ric}(g_0)|\le K .
\]

Theorem 3.6 rewrites this in dimension four through

\[
\varepsilon_x(r)=
\frac{r^4}{\operatorname{Vol} B_r(x)}
\int_{B_r(x)}|\mathrm{Rm}|^2\le\varepsilon_{\rm Li},
\]

again with the all-centres quantifier inherited from Theorem 3.1; its isolated displayed statement omits those words, but it begins “the previous theorem can be restated.”  Li's proof propagates

\[
\sup_x C_s(B_r(x))\,\|\mathrm{Rm}(t)\|_{L^2(B_r(x))}<\theta
\]

by a supremum over centres and a bounded-overlap covering.  It also preserves metric equivalence and the ball Sobolev inequalities, proves an \(L^3\) curvature-potential estimate, and obtains \(|\mathrm{Rm}|\le C/t\).  A single maximal-function good point supplies the initial condition only on a buffered region, not on the entire closed manifold.  Li's published global theorem therefore cannot yet be directly invoked.

The small-radius observation remains valid and important.  If

\[
\mathcal M_1(|\mathrm{Rm}|^2)(p)\le K_0,
\]

then Bishop--Gromov comparison gives, for all relevant nearby centres \(y\) and radii \(\rho\) inside a fixed buffer,

\[
\frac{\rho^4}{\operatorname{Vol}B_\rho(y)}
\int_{B_\rho(y)}|\mathrm{Rm}|^2
\le C K_0 R^4.
\]

Choosing one fixed \(R=R(K_0,\varepsilon_{\rm Li})>0\) makes this initially small.  No background-curvature subtraction is needed.

## 3. Direct Einstein-defect estimate from Corollary 3.5

### 3.1 Kato subsolution

Under normalized Ricci flow

\[
\partial_tg=-2E,\qquad E=\mathrm{Ric}+g,
\]

the already verified exact identities are

\[
\partial_tE=\Delta_LE-2E,
\]

and

\[
(\partial_t-\Delta)|E|^2
=-2|\nabla E|^2+4R_{ikjl}E_{ij}E_{kl}.
\]

For \(u_\eta=(|E|^2+\eta)^{1/2}\), Kato's inequality gives

\[
(\partial_t-\Delta)u_\eta\le2|\mathrm{Rm}|u_\eta.
\]

Thus \(u=|E|\) is precisely a curvature-potential subsolution after sending \(\eta\downarrow0\).

### 3.2 A textual issue in Corollary 3.5

The paper prints

\[
\partial_tu\le\phi^2(\Delta u+c_0fu),
\]

although \(\phi\) is undefined in the statement.  Theorem 2.5 requires the ordinary inequality without \(\phi^2\), and Li immediately applies Corollary 3.5 to the ordinary Ricci flow.  The next proof also prints a spurious \(\phi^2\) in the standard curvature evolution.  The only reading compatible with the proof and use is

\[
\partial_tu\le\Delta u+c_0fu.
\]

This source ambiguity must be recorded rather than silently ignored.

### 3.3 Normalized-to-unnormalized conversion

Let \(\bar g(s)\) solve \(\partial_s\bar g=-2\operatorname{Ric}_{\bar g}\), set

\[
s=\frac{e^{2t}-1}{2},\qquad g(t)=e^{-2t}\bar g(s),\qquad
q(s)=\frac1{1+2s},
\]

and define

\[
H(s)=\operatorname{Ric}_{\bar g(s)}+q(s)\bar g(s).
\]

Then, as covariant tensors, \(H(s)=E(t)\), while

\[
|E(t)|_{g(t)}=(1+2s)|H(s)|_{\bar g(s)}.
\]

Since \(q'=-2q^2\),

\[
\partial_sH=\Delta_LH-2qH,
\]

and the extra scalar term is favourable in the norm inequality:

\[
(\partial_s-\Delta_{\bar g})(|H|^2+\eta)^{1/2}
\le2|\mathrm{Rm}(\bar g)|(|H|^2+\eta)^{1/2}.
\]

This is the clean interface to Li's unnormalized-flow result.  Four-dimensional Sobolev coefficients and \(L^2\) curvature energy are invariant under constant rescaling.

### 3.4 Two volume cancellations and the sharp scaling

Li uses

\[
\|v\|_{L^4(B_r)}^2\le A_x\|\nabla v\|_{L^2(B_r)}^2,
\qquad
A_x\le C\frac{r^2}{\operatorname{Vol}(B_r(x))^{1/2}}.
\]

First,

\[
A_x\|\mathrm{Rm}\|_{L^2(B_r(x))}
\le C\varepsilon_x(r)^{1/2};
\]

collapse cancels from the curvature-energy absorption.  Corollary 3.5 then yields

\[
|H(x,s)|\le
C A_x^{2/3}s^{-2/3}
\left(\int_{B_{3r}(x)}|H(0)|^3\right)^{1/3}.
\]

If \(|E(0)|\le\delta\), Bishop--Gromov controls the comparable-radius volume ratio and gives the second cancellation:

\[
A_x^{2/3}
\left(\int_{B_{3r}(x)}|E(0)|^3\right)^{1/3}
\le C\delta r^{4/3}.
\]

After converting back to normalized time, for \(0<t\le a r^2\),

\[
\boxed{
|E(x,t)|\le C\delta r^{4/3}t^{-2/3}
=C\delta\left(\frac{r^2}{t}\right)^{2/3}.}
\]

The singular factor is integrable.  Hence for a fixed tangent vector,

\[
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
\le2\int_0^t|E(x,\tau)|\,d\tau
\le C\delta r^{4/3}t^{1/3}.
\]

At \(t=\theta r^2\), this gives \(|E|\le C_\theta\delta\) and metric drift \(O(\delta r^2)\), uniformly in collapsed volume.  This proves defect stability **conditionally on the full dynamic local-flow package**; it does not prove curvature convergence or calibration transfer by itself.

## 4. Normalized cutoff flow and exact homogeneity

Let \(a=\chi^2\) be fixed on the original closed manifold and consider

\[
\partial_tg=-2aE.
\]

For \(\tau=\operatorname{tr}E\), direct variation of Ricci and contracted Bianchi give

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]

where

\[
\begin{aligned}
\mathcal C_a(E)_{ij}={}&(\Delta a)E_{ij}
+2\nabla^ka\,\nabla_kE_{ij}
+\tau\nabla_i\nabla_ja\\
&+\frac12(\nabla_i a\nabla_j\tau+\nabla_j a\nabla_i\tau)
-(\nabla_i\nabla^ka)E_{kj}-(\nabla_j\nabla^ka)E_{ki}\\
&-\nabla^ka(\nabla_iE_{kj}+\nabla_jE_{ki}).
\end{aligned}
\]

Every term contains \(E\), \(\tau\), \(\nabla E\), or \(\nabla\tau\), so \(\mathcal C_a(0)=0\).  Thus an exact \(\operatorname{Ric}=-g\) metric is stationary through the transition annulus; there is no collar source independent of the Einstein defect.

The squared-norm identity is

\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4a\operatorname{Rm}(E,E)
+2\langle E,\mathcal C_a(E)\rangle.
\]

With an independent test cutoff \(q=\eta^2\), integration by parts and \(\operatorname{div}E=\tfrac12d\tau\) remove all Hessians of \(a\):

\[
\begin{aligned}
\int q\,2\langle E,\mathcal C_a(E)\rangle
={}&\int[-2|E|^2\langle da,dq\rangle
-2\tau E(dq,da)+4E^2(dq,da)]\\
&+\int q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)].
\end{aligned}
\]

Using \(|\tau|\le2|E|\) in four dimensions and

\[
\frac{|da|^2}{a}=4|d\chi|^2
\]

where \(a>0\), Young's inequality absorbs the derivative terms without a \(1/\chi\) loss.  Schematically,

\[
\begin{aligned}
\frac d{dt}\int\eta^2|E|^2
+c\int\eta^2a|\nabla E|^2
\le{}&C\int(a|d\eta|^2+\eta^2|d\chi|^2+\eta^2a)|E|^2\\
&+C\int\eta^2a|\mathrm{Rm}|\,|E|^2.
\end{aligned}
\]

This has the right multiplicative structure for a critical Sobolev absorption.  The calculation is independently recorded and checked in `workspace/scripts/verify_cutoff_defect_energy.py` (exit code 0).

A DeTurck field weighted once by \(a\) preserves the same homogeneity, adding only \(\mathcal L_WE\).  But the equation is degenerate where \(a=0\), and pullback changes a fixed cutoff unless the DeTurck-side coefficient is transported.  These are existence-theory issues, not algebraic defect sources.

## 5. Existing local Ricci-flow literature: what is inherited and what is not

Local Ricci flow

\[
\partial_tg=-2\chi^2\operatorname{Ric}
\]

is an established equation (Yang; later Wang and He).  Wang's sourced Theorem 6.3 gives existence and pointwise \(\chi^2\mathrm{Rm}\), \(\chi^2\mathrm{Ric}\) estimates from a **global** Sobolev inequality on the support, globally small \(L^{n/2}\) curvature relative to that Sobolev coefficient, and an \(L^p\) Ricci bound with \(p>n/2\).  In dimension four its curvature-energy inequality has exactly the needed critical absorption form:

\[
\frac d{dt}\int|\mathrm{Rm}|^2
+c\int|\nabla(\chi|\mathrm{Rm}|)|^2
\le C|d\chi|_\infty^2\int|\mathrm{Rm}|^2.
\]

This strongly supports the cutoff route, but its noncollapse-dependent global Sobolev coefficient and global support energy do not yet match the present collapsed buffered-ball data automatically.  A relative ball Sobolev inequality has a volume-dependent coefficient; the volume cancels only when paired with **local normalized** energy.  The theorem as stated does not perform the required bounded-overlap localisation.

Fei He's later local-flow framework explicitly notes that parallel normalized results should use \(\operatorname{Ric}-\lambda g\), but its lifespan theorem assumes pointwise full-curvature scales and initial first/second derivatives of the Ricci defect.  Those inputs are unavailable for the near-Einstein sequence before smoothing.  It is therefore useful structural support, not the missing theorem.

The most promising construction is to combine three existing mechanisms rather than an arbitrary completion:

1. Yang's compactly supported local-flow existence framework on the original closed manifold;
2. Li's all-centres/bounded-overlap local normalized-energy bootstrap, restricted to a nested buffer;
3. the homogeneous normalized-defect evolution above, followed by Corollary 3.5 on the plateau \(\chi=1\).

The curvature evolution for the normalized cutoff flow has extra \(da*\nabla E\) and \(\nabla^2a*E\) terms.  Since \(E=\operatorname{Ric}+g\), they are homogeneous in the small defect rather than in the potentially order-one background Ricci.  In an integrated curvature-energy estimate they should contribute \(D^{-2}\int(|\mathrm{Rm}|^2+|E|^2)\) on a transition width \(D\), while the cubic curvature term is absorbed by the local normalized energy.  This exact localized bootstrap remains to be written and checked.

## 6. Calibration and topology

The cutoff flow lives on the original closed smooth manifold and changes no topology.  If the local-flow estimates propagate the **global** pointwise defect bound (the initial bound \(|E_i|\le\delta_i\) holds everywhere), then at every time where the flow exists,

\[
\|\operatorname{Ric}_{g_i(t)}+g_i(t)\|_\infty\le C\delta_i.
\]

The critical Ishida--LeBrun Chern--Weil/monopole near-saturation argument can then be re-run directly on the closed metric \(g_i(t)\); no local curvature comparison with \(g_i(0)\) is required.  This is why a homogeneous cutoff flow is substantially better than completing or doubling a ball: it preserves the original topology and cannot inject an additive defect independent of \(\delta_i\).

However, a local estimate only on one plateau is insufficient for the global near-saturation argument.  The construction must either yield a uniform global \(O(\delta_i)\) defect estimate for the cutoff-flow metric or prove a separate local transport of calibrated data.  The first route is cleaner because the flow is already defined on the closed manifold and the initial defect is globally small.

Even after bounded curvature and global small defect are obtained, bounded sectional curvature on a collapsed ball does not itself give a noncollapsed harmonic chart.  One must use genuine bounded-curvature covering/fibration theory.  The Step 13 claim that bounded \(B\) controls all quotient coefficients is invalid: at jet level, \(B=0\) can coexist with large \(H,z,\nabla z\) by cancellation.  Reconstruction remains a separate geometric layer.

## 7. Current conditional theorem and exact remaining analytic object

A valid conditional statement is now:

> Let \((M^4,g_i)\) be the hypothetical critical sequence with \(\|\operatorname{Ric}_{g_i}+g_i\|_\infty=\delta_i\to0\).  Suppose that at a maximal-function good point and one fixed radius \(r>0\), a normalized cutoff flow on the original closed manifold exists for \(0\le t\le\theta r^2\), equals normalized Ricci flow on a buffered plateau, remains uniformly metric-equivalent, preserves the needed all-centres local normalized \(L^2\) curvature smallness/Sobolev/covering estimates, and propagates the global defect with no additive term.  Then Corollary 3.5 gives
> \[
> |\operatorname{Ric}_{g_i(t)}+g_i(t)|\le C_\theta\delta_i
> \]
> on the plateau, with \(|\mathrm{Rm}(g_i(t))|\le Cr^{-2}\); if the same defect control is global, the closed smoothed metric has the same calibrated near-saturation profile by the original topological argument.

The remaining analytic object is precise: prove a collapse-uniform, bounded-overlap local normalized-curvature-energy bootstrap for \(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\), with a global homogeneous defect estimate and an interior \(C/t\) curvature estimate.  The defect part is now structurally favorable and Corollary 3.5 supplies its sharp propagation once the curvature bootstrap exists.  The curvature bootstrap, not the \(2/3\)-exponent estimate, is the load-bearing unresolved work.

## 8. Source and evidence paths

- Ye Li source: `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md`, especially lines 199--335; citation `\\cite{lismoothing}`.
- TTCS integrations: `trace/ttcs/results/step14_ttcs01_verifier1_integration.md`, `step14_ttcs01_generator1_integration.md`.
- Local-flow source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`; citation `\\cite{wang2009pseudolocality}`.
- Normalized local-flow structural source: `staging/acquired/Existence__Lifespan_and_Transfer_Rate_of_Ricci_Flows_on_Manifold_4f0e84ed47779027/part_001.md`, `part_002.md`; citation `\\cite{he2016existence}`.
- Algebraic check: `workspace/scripts/verify_cutoff_defect_energy.py`.
