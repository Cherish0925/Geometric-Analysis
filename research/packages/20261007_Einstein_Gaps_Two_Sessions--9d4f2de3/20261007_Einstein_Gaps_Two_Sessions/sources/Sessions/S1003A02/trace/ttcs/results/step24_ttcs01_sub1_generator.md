# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md"
  ]
}
```

## Task

Develop mathematically serious possible routes from Theorem C to an absolute lower bound for the complete constant-scalar ACH O(-1) cell energy 4 Delta W_+ + 48 RV > -8 pi^2. Use the fact that CH has |W+|^2=24, first-order Weyl and volume channels cancel in kernel directions, and zero cost would require a definite Weyl deletion. Explore whether a two-scale localization through a half-conformally-flat region and a localized hyperbolic renormalized-volume comparison is coherent, what exact lemma would be needed, and what counter-mechanisms (oscillation, concentration, curved neck, collapse) defeat naive versions. Compare this route with the global bulk-to-cell passage and identify the most load-bearing theorem worth constructing, without treating a Lambda>1 trade-off as sufficient.

## Output

Let \(X=\mathcal O(-1)\to \mathbb {CP}^{1}\), with the standard spherical CR structure at infinity, and let \(g\) be complete ACH with \(s_g=-24\). Write
\[
P(g)=\int_X |\Ric^\circ_g|^2\,d\mu_g,\qquad
\mathcal A(g)=4\Delta W_+(g)+48\,\mathrm{RV}(g).
\]
Theorem C gives the exact identity
\[
P(g)=8\pi^2+\mathcal A(g). \tag{1}
\]
Thus two mathematically distinct statements are involved:

\[
\mathcal A(g)>-8\pi^2\quad\text{for each }g
\]
amounts to excluding an Einstein ACH filling with the standard spherical CR infinity, while
\[
\inf_g\mathcal A(g)>-8\pi^2
\quad\Longleftrightarrow\quad
\inf_g P(g)>0 \tag{2}
\]
also requires compactness for sequences with \(P(g_j)\to0\). The second is the substantive cell gap.

## 1. What zero cost would force

For the standard orientation, \(\mathbb {CH}^2\) has \(W^-_{\rm CH}=0\), \(|W^+_{\rm CH}|^2=24\). With the same asymptotic framing at infinity, the relative signature formula gives
\[
\Delta W_+-\int_X|W^-_g|^2=-12\pi^2. \tag{3}
\]
Set \(B_-(g)=\int_X|W^-_g|^2\). Combining (1) and (3),
\[
P(g)=4B_-(g)+48\,\mathrm{RV}(g)-40\pi^2, \tag{4}
\]
and hence
\[
\Delta W_+(g)
=-2\pi^2-12\,\mathrm{RV}(g)+\frac14P(g). \tag{5}
\]

Consequently, any sequence with \(P(g_j)\to0\) and
\[
\mathrm{RV}(g_j)\ge-o(1)
\]
must satisfy
\[
-\Delta W_+(g_j)
=2\pi^2+12\,\mathrm{RV}(g_j)+o(1)\ge 2\pi^2-o(1). \tag{6}
\]
Since the CH density is \(24\), the smallest deletion in (6) is the Weyl energy contained in a CH region of volume
\[
\frac{2\pi^2}{24}=\frac{\pi^2}{12}.
\]
At the same time,
\[
B_-(g_j)+12\,\mathrm{RV}(g_j)=10\pi^2+o(1). \tag{7}
\]
Thus a zero-cost sequence must perform a finite chiral rearrangement: it must remove a definite amount from the CH \(W^+\) channel and create a definite \(W^-\) charge carrying the exceptional topology.

This already explains why a linear estimate
\[
4\Delta W_+\ge -\Lambda\,48\mathrm{RV}-\eta,\qquad \Lambda>1,
\]
does not yield the desired result. It gives only
\[
P-8\pi^2\ge-(\Lambda-1)48\mathrm{RV}-\eta,
\]
which has no absolute content without an upper estimate for \(\mathrm{RV}\). More fundamentally, in a kernel-direction Burns perturbation,
\[
4\Delta W_+=-a\,x_0+o(x_0),\qquad
48\mathrm{RV}=a\,x_0+o(x_0),
\]
so the combined action begins at second order. A linear cone relating the two channels cannot detect either the \(-9x_0^2\log(1/x_0)\) interaction or a topological floor for \(P\).

## 2. The coherent two-scale picture

A plausible separated geometry has four radial regimes:

1. the outer CH region, where \(W^+\) has the CH spectrum and \(W^-=0\);
2. a first transition in which the CH \(W^+\) energy is removed;
3. a mesoscopic region close to real hyperbolic four-space \(H^4_{K=-2}\), where
   \[
   W^+\approx0,\qquad W^-\approx0,\qquad \Ric^\circ\approx0;
   \]
4. an inner region where the exceptional class and its \(W^-\) charge are created.

The curvature-operator decomposition makes the required geometry precise. Since both \(g\) and \(H^4_{K=-2}\) have scalar curvature \(-24\),
\[
\mathcal R_g-\mathcal R_{H}
=
\begin{pmatrix}
W^+ & \mathring{\Ric}^{\,\#}\\
(\mathring{\Ric}^{\,\#})^* & W^-
\end{pmatrix}. \tag{8}
\]
Therefore \(W^+\approx0\) alone does not give a real-hyperbolic region. One also needs \(W^-\approx0\) and \(\Ric^\circ\approx0\). A half-conformally-flat region can still contain an arbitrary anti-self-dual Einstein geometry.

If a genuine \(H^4\)-like annulus separates the exceptional core from the CH end, one may cut across its middle and replace the exterior by exact \(H^4\). After a small interpolation, one obtains a metric \(\widetilde g\) on \(D\#\overline{\mathbb {CP}}^2\) that is exactly \(H^4\) off a compact set and satisfies
\[
P(\widetilde g)\le P(g;\text{inner side})+o(1). \tag{9}
\]
Yamabe normalization then produces \(q=u^2\widetilde g\), \(s_q=-24\), with
\[
P(q)\le P(\widetilde g). \tag{10}
\]
The real-hyperbolic exterior is analytically favorable: for curvature \(-2\),
\(\lambda_0(H^4)=9/2\), so the conformal linearization has a strict spectral margin, unlike the spectrally critical CH end.

For this real-hyperbolic cell,
\[
P(q)=8\pi^2+4\int_X|W^+_q|^2+48\,\mathrm{RV}_{H}(q). \tag{11}
\]
Hence any comparison of the form
\[
\mathrm{RV}_{H}(q)\ge
-\omega\!\left(P(q)\right),
\qquad \omega(t)\longrightarrow0\quad(t\to0), \tag{12}
\]
already rules out \(P(q)\to0\). Indeed, (11) would give
\[
P(q)\ge8\pi^2-48\,\omega(P(q)).
\]
The stronger statement
\[
\mathrm{RV}_{H}(q)\ge0 \tag{13}
\]
would yield \(P(q)\ge8\pi^2\), but the sequential estimate (12) is all that the zero-cost contradiction requires.

### The exact localized lemma

The natural lemma has the following form.

**Hyperbolic enclosure lemma.**  
Let \(g_j\) be complete standard-ACH metrics on \(X\), \(s_{g_j}=-24\), with \(P(g_j)\to0\). Suppose there are embedded separating annuli
\[
A_j\simeq S^3\times[-L_j,L_j],
\qquad L_j\to\infty,
\]
enclosing the exceptional class, such that after diffeomorphisms
\[
g_j\longrightarrow g_H
\quad\text{in }C^{2,\alpha}_{\mathrm{loc}}(A_j),
\tag{14}
\]
where \(g_H\) is real hyperbolic of curvature \(-2\). Then one can construct exact-\(H^4\)-exterior metrics \(\widetilde g_j\), Yamabe normalize them to \(q_j\), and obtain
\[
P(q_j)\to0. \tag{15}
\]
If the localized real-hyperbolic volume estimate (12) holds, then such annuli cannot occur.

The cutting and Yamabe-normalization part is relatively accessible once (14) is available. The true mathematical weight lies in producing (14), or in proving that its absence creates another classified geometric limit.

## 3. Why a half-conformally-flat region does not follow from channel deletion

Equation (6) only gives an integrated deletion. It does not imply that \(|W^+|\) becomes small on an open set. A reduction of \(|W^+|^2\) by \(1\) over a region of volume \(2\pi^2\) produces the same total deletion as setting \(W^+=0\) on a much smaller region. The metric may also alternate between regions with \(|W^+|^2<24\) and \(|W^+|^2>24\).

Moreover, the \(W^-\) transition can occur on exactly the same geometric scale as the \(W^+\) deletion. Then there is no interval where both chiral blocks are small. This is the curved-neck mechanism already suggested by the certified CH cells: volume payment and Weyl saving are spatially coupled rather than separated by a real-hyperbolic plateau.

A useful theorem would therefore not assert automatic half-conformal flatness. It would give a chiral-transition decomposition:

> For an appropriately selected sequence with \(P(g_j)\to0\), either  
> (a) a real-hyperbolic enclosure as in (14) appears;  
> (b) after recentering, a complete Einstein \(s=-24\) connector appears, joining the standard CH infinity directly to the exceptional core;  
> (c) after rescaling, a Ricci-flat concentration tree carries the exceptional class; or  
> (d) topology is carried by a collapsed region.

The two-scale volume argument resolves only branch (a). Branches (b)–(d) contain the deeper compactness problem.

## 4. Counter-mechanisms defeating naive localization

### 4.1 Oscillation and diffuse deletion

The quantities \(\Delta W_+\) and \(\mathrm{RV}\) are signed relative integrals. They do not define positive measures. Rapid alternation can create a finite net channel change without producing a region close to \(H^4\).

There is also an escape-to-infinity version. In a CH shell at radial position \(R\), the volume is of order \(e^{4R}\). A perturbation of amplitude \(a_R\) supported in a shell of fixed width has first-order channel responses of order
\[
a_Re^{4R},
\]
while its quadratic Einstein defect is of order
\[
a_R^2e^{4R}.
\]
Taking \(a_R\sim e^{-4R}\) produces order-one changes in the individual linearized channels with a vanishing quadratic cost. For a topology-neutral shell the first-order Weyl and volume changes cancel in \(\mathcal A\), as they must by (1), but such shells can move the apparent location of the two channel contributions arbitrarily far outward. Any localization theorem therefore needs weighted tightness, a fixed asymptotic gauge, or a variational equation that suppresses these drifting modes.

### 4.2 Curvature concentration

Because \(P\) is scale invariant in dimension four, concentrating the exceptional class at scale \(r_j\to0\) does not make its cost disappear. If an almost-Euclidean neck develops, rescaling gives a scalar-flat ALE bubble. Lemma Q then yields
\[
P_{\rm bubble}\ge8\pi^2
\]
for a single \((-1)\)-class. Thus ordinary Burns concentration is incompatible with \(P(g_j)\to0\).

More complicated orbifold trees require the full signature \(\eta\)-terms and an intersection-form ledger. At each level, the compactly supported intersection forms and end groups must reconstruct the primitive class of square \(-1\). A Ricci-flat \(\Gamma=1\) bubble cannot do this: Lemma Q would force \(0=P\ge8\pi^2\). For nontrivial \(\Gamma\), the same conclusion needs additive accounting across the entire tree rather than a one-bubble argument.

### 4.3 Curved necks

A curved neck can convert the CH \(W^+\) state directly into the \(W^-\) topology carrier while keeping \(\Ric^\circ\) small. In the limit this becomes an Einstein connector. Theorem E shows that such connectors genuinely exist when the CR structure at infinity is allowed to move to a Rossi sphere. Thus the standard spherical value must enter decisively; local curvature algebra alone cannot remove this mechanism.

The needed result is a rigidity or properness theorem for complete ACH Einstein metrics on \(\mathcal O(-1)\) with standard spherical CR infinity. Analytic continuation from an exact CH collar does not apply to a merely asymptotic end.

### 4.4 Collapse

If injectivity radii vanish, there may be no controlled \(S^3\) annulus on which to perform the hyperbolic cut. Circle or torus fibrations can carry geometry through regions of small volume, while \(L^2\) curvature remains scale invariant. A complete treatment must pass to local covers and identify the resulting ALE, ALF, ALG, or lower-dimensional Einstein pieces. It must also show that the primitive \((-1)\)-class cannot disappear into the collapsing region.

### 4.5 Half-flat but not hyperbolic

Even with
\[
W^+\to0,\qquad P\to0,
\]
one may obtain an anti-self-dual Einstein limit with \(W^-\ne0\). The localized \(H^4\) volume comparison applies only after \(W^-\) is also shown to vanish on the separating annulus. Relative signature shows that \(W^-\) has order-one total energy, but does not determine where that energy lies.

## 5. The chiral connection representation

There is a useful gauge-theoretic formulation. Let \(A^+\) be the Levi-Civita connection on \(\Lambda^+\). Up to fixed convention factors,
\[
(F_{A^+})^+=W^++\frac{s}{12}I,
\qquad
(F_{A^+})^-=\mathring{\Ric}^{\,\#}. \tag{16}
\]
Thus \(P\) is the \(L^2\) energy of the anti-self-dual part of \(F_{A^+}\). A sequence with \(P\to0\) makes \(A^+\) into an approximate self-dual connection, while the diagonal self-dual curvature changes from the CH state
\[
W^+_{\rm CH}-2I=\operatorname{diag}(-6,0,0)
\]
to the real-hyperbolic state
\[
-2I.
\]

This suggests a chiral-transition theorem based on relative Chern–Simons quantities. Schematically, small off-diagonal curvature should force one of two behaviors:

* the two chiral transitions separate, producing an \(H^4\) plateau;
* they remain coupled and converge to an exact Einstein connector.

For arbitrary metrics, \(L^2\)-small \(\Ric^\circ\) does not control derivatives of curvature. The Bianchi identity gives
\[
\delta W \sim \nabla\Ric^\circ,
\]
not an estimate of \(\nabla\Ric^\circ\) by \(\Ric^\circ\). The connection approach therefore becomes effective after replacing a minimizing sequence by approximate stationary metrics for \(P\) under the constraint \(s=-24\). The constrained Euler–Lagrange system is fourth order and schematically yields
\[
\nabla^*\nabla \Ric^\circ
+\mathrm{Rm}*\Ric^\circ
+\Ric^\circ*\Ric^\circ
=\text{small residual}. \tag{17}
\]
Together with harmonic gauge and a Sobolev estimate, (17) can provide the \(\varepsilon\)-regularity needed to turn integral smallness into smooth annular convergence. In the connection language, it gives the approximate Yang–Mills control missing from the raw Bianchi identity.

The CH conformal spectral criticality means the scalar constraint must retain the mass or renormalized-volume mode rather than projecting it away. On an \(H^4\) annulus this issue disappears because the corresponding conformal operator has a strict spectral margin.

## 6. A stronger compactness theorem that would settle the gap

The most load-bearing theorem is not a channel inequality with \(\Lambda>1\), but a topological compactness theorem for almost-Einstein ACH metrics.

A useful precise form is the following.

**Standard-ACH odd-class carrier theorem.**  
Let \(g_j\) be complete metrics on \(\mathcal O(-1)\), with \(s_{g_j}=-24\), fixed standard spherical CR infinity in a uniform weighted gauge, and
\[
P(g_j)\to0.
\]
After variational replacement with the same asymptotic data and \(P\)-increase \(o(1)\), there is a finite decomposition into:

1. a thick complete ACH Einstein component;
2. finitely many rescaled Ricci-flat concentration components;
3. necks carrying no second homology;
4. collapsed components described on local covers;

and the compactly supported intersection form
\[
[-1]
\]
is the orthogonal sum of the intersection forms carried by these components. No primitive square-\(-1\) class disappears through the necks or the collapsed set.

This theorem would reduce the gap to three geometric rigidity statements:

* there is no complete Einstein \(s=-24\) filling of \(\mathcal O(-1)\) with standard spherical CR infinity;
* no Ricci-flat concentration tree with the required end groups carries a primitive square-\(-1\) class;
* no collapsed local-cover model carries that class without producing a definite amount of \(P\).

If all three hold, a sequence with \(P\to0\) cannot exist, and hence there is an \(\varepsilon_*>0\) such that
\[
P(g)\ge\varepsilon_*,
\qquad
4\Delta W_+(g)+48\,\mathrm{RV}(g)
\ge-8\pi^2+\varepsilon_*.\tag{18}
\]

The real-hyperbolic enclosure mechanism is naturally one part of this theorem: when the CH \(W^+\) deletion and the \(W^-\) topology carrier separate in scale, the intermediate thick component is \(H^4\), and the localized volume comparison rules it out. When they do not separate, one obtains an Einstein connector or a concentration/collapse model.

This theorem is more reusable than a direct estimate on \(\Delta W_+/\mathrm{RV}\). It would also supply the topology-retention input needed in the closed-manifold bulk-to-cell problem.

## 7. A field-theoretic route

The exceptional class \(E\in H^2_c(X)\), \(E^2=-1\), has an \(L^2\)-harmonic representative \(\omega_g\) under suitable ACH Hodge theory. Its chiral decomposition obeys
\[
\|\omega^-\|_2^2-\|\omega^+\|_2^2
= \text{fixed topological constant}. \tag{19}
\]
The Weitzenböck equation for \(\omega^-\) couples it directly to \(W^-\) and \(s=-24\). A relative Seiberg–Witten or monopole-Floer construction for the blow-up cobordism could provide an actual field tied to \(E\), rather than merely the formal number \(E^2\).

The desired analytic theorem would have the shape
\[
\bigl(1+B(\omega_g)\bigr)P(g)\ge c(E^2), \tag{20}
\]
where \(B(\omega_g)\) is controlled uniformly by the standard ACH geometry. This is the cell analogue of the bounded-form coercivity mechanism already present in the global theory.

Its hard substance is a uniform estimate for the field through concentration and collapse. If \(\|\omega_g\|_\infty\) or its local Sobolev constant diverges, (20) loses content. A relative monopole invariant with finite-energy asymptotics could prevent the exceptional charge from escaping through a curved neck, making this route potentially stronger than pure renormalized-volume comparison.

## 8. Comparison with the global bulk-to-cell passage

The global passage has additional layers:

* an actual field must identify the CH bulk;
* topological charge must be assigned to individual concentration regions;
* collapsed and noncollapsed parts must be separated;
* asymptotically CH pieces must be truncated to exact collars;
* cell energies must be shown additive up to vanishing interactions.

A cell gap does not by itself provide those steps. Conversely, trying to derive the isolated cell gap by planting the cell into large compact CH covers loses quantitative force. Truncating a complete cell at radius \(R\) consumes CH volume of order \(e^{4R}\), so the packing density is of order \(e^{-4R}\). Existing closed topological estimates become effective only at a definite blow-up density; they do not automatically yield a per-cell estimate as \(R\to\infty\).

The cell compactness theorem above is nevertheless a central input for the global problem. It would show that every localized \((-1)\)-class carries a fixed amount of Einstein defect unless it belongs to a classified Einstein, Ricci-flat, or collapsed component. That is exactly the topology-retention statement missing from the global decomposition.

## 9. Decisive calculations and source targets

Several computations would sharply distinguish the proposed mechanisms.

1. **Radial chiral profiles.** In diagonal cells, plot cumulative
   \[
   D_+(r)=-\Delta W_+(r),\qquad
   B_-(r)=\int_{t\le r}|W^-|^2,\qquad
   P(r),\qquad \mathrm{RV}(r).
   \]
   An \(H^4\) plateau would show \(D_+\) essentially completed before \(B_-\) begins, with both local Weyl densities small over a long interval. A curved connector would show the two transitions overlapping.

2. **Weighted Einstein spectrum at the CH end.** The kernel and resonance structure of the linearized Einstein operator with fixed spherical CR infinity determines whether oscillatory or outward-drifting almost-Einstein modes exist. The conformal mass mode must be recorded separately.

3. **Einstein shooting to standard infinity.** On the known Bianchi IX Einstein branch, the map from bolt data to the Rossi parameter \(\rho_\infty\) can be studied near \(\rho_\infty=1\). A standard-infinity orbit would realize the curved-neck mechanism inside the diagonal class; a quantitative separation from \(1\) would establish only the diagonal part of the required rigidity.

4. **Hyperbolic volume sources.** The exact hypotheses and conclusions needed from the Brendle–Chodosh asymptotically hyperbolic volume comparison, Chruściel–Delay positive mass theory, and Huang–Jang–Martin rigidity should be matched to metrics obtained by Yamabe normalizing compact perturbations of \(H^4\). The key question is whether they imply either
   \[
   \mathrm{RV}_H\ge0
   \quad\text{or at least}\quad
   \mathrm{RV}_H\ge-\omega(P),\ \omega(t)\to0.
   \]

5. **Almost-Einstein bubble trees.** Relevant source families are Anderson and Cheeger–Tian compactness for Einstein four-manifolds, Tian–Viaclovsky theory for critical curvature metrics, Uhlenbeck compactness for chiral connections, and local-cover descriptions of collapsed Ricci-flat four-geometries.

The two-scale \(H^4\) route is therefore coherent and potentially decisive for separated concentration, but it cannot by itself treat diffuse deletion or a direct curved Einstein connector. The central theorem is a standard-ACH almost-Einstein compactness result that preserves the primitive \((-1)\)-class through thick regions, bubbles, necks, and collapse. The localized hyperbolic renormalized-volume comparison then becomes a powerful component of that theorem rather than the entire argument.