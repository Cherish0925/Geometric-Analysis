# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/originals/0911_3104__Smoothing_Riemannian_Metrics_with_Bounded_Ricci_Curvatures_in_Dimens.pdf",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/workspace/scripts/verify_einstein_defect_evolution.py"
  ]
}
```

## Task

Investigate a normalized cutoff Ricci flow on a closed 4-manifold, ∂_t g=-2 χ^2 (Ric+g), as a localization device for a metric with globally small Einstein defect |E|<=delta but curvature-energy control only on a buffered ball. Derive the principal evolution of E=Ric+g, keeping every term from spatially varying χ, and determine whether all added terms are homogeneous in E and its derivatives (so vanish when E=0) or whether gauge/parabolicity issues introduce other terms. Seek an energy bootstrap compatible with Ye Li's Corollary 3.5 and quantify interior boundary influence. Compare this route with local Ricci-DeTurck/Yang flows if needed, but do not cite unstated theorems. Produce explicit formulas and a scientifically useful conditional route or obstruction.

## Output

## Scientific memo: the cutoff normalized flow as an Einstein‑defect localizer

### 1. Setup and the exact defect evolution (all χ‑terms retained)

Write $a=\chi^2$ (values of $\chi$ fixed on $M^4$, gradients taken in $g(t)$), and let $E=\operatorname{Ric}+g$, so the flow is $\partial_t g = -2aE$. Using the linearization of Ricci, $D\operatorname{Ric}(h)=-\tfrac12\Delta_L h-\tfrac12\nabla\nabla(\operatorname{tr}h)+\tfrac12(\nabla_i(\operatorname{div}h)_j+\nabla_j(\operatorname{div}h)_i)$ with $h=-2aE$, the contracted Bianchi identity $\operatorname{div}E=\tfrac12\nabla(\operatorname{tr}E)$, and $\partial_tE=D\operatorname{Ric}(h)+h$, every term can be collected exactly:

$$
\boxed{
\begin{aligned}
\partial_t E_{ij}
={}& a\,\Delta_L E_{ij}\;-\;2a\,E_{ij}\\
&+\;2\,\nabla^k a\,\nabla_k E_{ij}\;-\;\nabla^k a\,(\nabla_i E_{kj}+\nabla_j E_{ki})
&&\text{(transport / gauge, first order in }\nabla E)\\
&+\;(\Delta a)\,E_{ij}\;-\;(\nabla_i\nabla^k a)\,E_{kj}-(\nabla_j\nabla^k a)\,E_{ki}
&&\text{(zeroth order, }\nabla^2a\ \text{coefficients)}\\
&+\;\tfrac12\big(\nabla_i a\,\nabla_j\!\operatorname{tr}E+\nabla_j a\,\nabla_i\!\operatorname{tr}E\big)\;+\;(\nabla_i\nabla_j a)\,\operatorname{tr}E .
&&\text{(trace channel)}
\end{aligned}}
$$

The two Bianchi cancellations that keep the pure flow well‑posed survive verbatim with the weight: the $a\,\nabla_i\nabla_j\!\operatorname{tr}E$ pieces from the Hessian‑of‑trace term and the divergence term cancel, and the algebraic $\operatorname{Ric}\!*\!E\!*\!E$ contributions recombine (with the overall factor $a$) exactly as in the $\chi\equiv1$ computation your `verify_einstein_defect_evolution.py` already confirmed.

**Decisive structural fact.** *Every term carries a factor of $E$, $\nabla E$, $\operatorname{tr}E$, or $\nabla\operatorname{tr}E$.* There is **no inhomogeneous term**. Consequently $E\equiv0$ is an exact stationary solution of the cutoff flow everywhere, including throughout the transition annulus $\{0<\chi<1\}$. This is geometrically obvious a posteriori ($g$ Einstein $\Rightarrow \partial_t g=-2\chi^2\cdot0=0$), but the term‑by‑term collection is what guarantees that the $|E|^2$ energy inequality has **no source**, which is the property the localization argument lives or dies by. The spatial variation of $\chi$ produces only a first‑order transport/gauge perturbation and $\nabla^2\chi$‑weighted zeroth‑order multipliers — never a driving force.

**DeTurck compatibility.** If a DeTurck field is added for parabolicity, $\partial_t g=-2a E+a\,\mathcal L_{W(g,\bar g)}g$, the extra piece acts on $E$ as $a\,\mathcal L_W E$, again homogeneous in $E$. Better: the cutoff DeTurck flow is $\varphi_t$‑equivalent to the cutoff flow, and the pointwise norm $|\operatorname{Ric}+g|$ is diffeomorphism‑invariant, so $\sup|E|$ is unchanged. Existence can therefore be taken from the strictly‑parabolic (where $\chi>0$) DeTurck version while all defect estimates are read off the geometric flow. The generated diffeomorphism has displacement $\lesssim\!\int|W|\,dt\lesssim t_0\sim r_0^2$, small against the buffer width, so it does not transport interior points across the transition annulus.

### 2. The scalar $|E|^2$ inequality and its divergence form

Taking $2\langle E,\partial_t E\rangle+ (\partial_t g^{-1})*E*E$ (the inverse‑metric variation gives $+4a\,\operatorname{tr}(E^3)$, which recombines with the curvature reaction as in the pure case):

$$
(\partial_t - a\,\Delta)\,|E|^2
= -2a\,|\nabla E|^2 \;+\;4a\,R_{ikjl}E^{ij}E^{kl}
\;+\;\underbrace{2\nabla a\!\cdot\!\nabla|E|^2}_{\text{transport}}\;+\;\mathcal A[\chi],
$$

where $\mathcal A[\chi]$ collects all annulus multipliers — schematically $\nabla a * E*\nabla E$ (gauge and trace first order) and $(\nabla^2a)*E*E$ — each supported on $\{\nabla\chi\neq0\}$ and each **quadratic in $(E,\nabla E)$**.

The transport term merges with the principal part into a clean weighted diffusion, since
$$
a\,\Delta u+2\nabla a\!\cdot\!\nabla u=\chi^{-2}\,\operatorname{div}\!\big(\chi^{4}\nabla u\big),\qquad u=|E|^2 .
$$
Thus $|E|^2$ is a subsolution of a **$\chi^4$‑weighted heat operator** with reaction $4|\operatorname{Rm}|$ and annulus forcing $\mathcal A[\chi]$. This is precisely the shape of your Corollary 3.5: that corollary already runs Moser iteration for $\partial_t u\le \varphi^2(\Delta u+c_0 f u)$ with a *compactly supported* weight $\varphi^2$. The cutoff flow makes $\varphi^2=\chi^2$ (equivalently the weight $\chi^4$) the intrinsic weight of the equation rather than an artificial test cutoff, so Li's machinery applies to the flow it generated instead of to an externally imposed localization of a global theorem.

### 3. Energy bootstrap; where the two hypotheses enter

Take $G(t)=\int_M \chi^{4}|E|^2\,dV_{g(t)}$. Using the divergence form, integrating against the weight, and $\partial_t\,dV_g=-\chi^2(\operatorname{tr}E)\,dV$ (again homogeneous, cubic contribution $\lesssim\delta\,G$):

$$
\frac{dG}{dt}\;\le\; -c\!\int \chi^{4}|\nabla E|^2
\;+\;4\!\int \chi^{4}|\operatorname{Rm}|\,|E|^2
\;+\;C\!\int_{\{\nabla\chi\neq0\}}\!\big(|\nabla\chi|^2+\chi|\nabla^2\chi|\big)|E|^2
\;+\;C\delta\,G .
$$

- **Reaction term (needs local energy).** By Hölder plus the relative Sobolev inequality (valid under $\operatorname{Ric}\ge-3g$), exactly as in your step‑13 §4,
$$
\int\chi^4|\operatorname{Rm}||E|^2\le \|\operatorname{Rm}\|_{L^2(\operatorname{supp}\chi)}\,\|\chi^2E\|_{L^4}^2
\le C_S\Big(\fint|\operatorname{Rm}|^2\Big)^{1/2}\!\big(\|\nabla(\chi^2E)\|_2^2+r_0^{-2}\|\chi^2E\|_2^2\big),
$$
and $\big(\fint|\operatorname{Rm}|^2\big)^{1/2}=\varepsilon_{r_0}^{1/2}/r_0^{2}$ with $\varepsilon_{r_0}=r_0^4\fint|\operatorname{Rm}|^2\le K_0r_0^4$. For $r_0$ chosen so $C_S\varepsilon_{r_0}^{1/2}<c$, the gradient part is **absorbed** by $-c\int\chi^4|\nabla E|^2$, and the volume factor cancels (the mechanism that defeats the pointwise $C/t$ Grönwall divergence recorded in your step‑13 §3). This step uses $\|\operatorname{Rm}\|_{L^2}$ only on $\operatorname{supp}\chi$, i.e. the buffered ball — the **local** hypothesis.

- **Transition‑annulus term (needs global smallness).** Since $|\nabla\chi|^2/\chi^2=4|\nabla\chi|^2$ is finite, all of $\mathcal A[\chi]$ is bounded after Cauchy–Schwarz by $\varepsilon\!\int\chi^4|\nabla E|^2+C_\varepsilon\!\int_{\{\nabla\chi\neq0\}}(|\nabla\chi|^2+\chi|\nabla^2\chi|)|E|^2$. On the annulus we do **not** control curvature; we control $|E|\le\delta$ *globally*. Hence this contribution is $\le C(\chi)\,\delta^2\,\mathrm{Vol}(\text{annulus})$, a bounded feed. This is the exact quantification of the influence of the cutoff transition zone on the interior: it is $O(\delta^2)$, weighted by $\sup(|\nabla\chi|^2+\chi|\nabla^2\chi|)$ times the annulus volume (Bishop–Gromov bounded).

Grönwall then gives $G(t)\le e^{Ct}\big(G(0)+C\delta^2\,\mathrm{Vol}(\text{annulus})\,t\big)\le C'\delta^2$, since $G(0)\le\delta^2\!\int\chi^4$. On the interior region $\{\chi=1\}$ this reads $\int_{\{\chi=1\}}|E(t)|^2\le C'\delta^2$.

**The clean division of labor is the scientific payoff:** the two hypotheses of the problem map onto the two term families with no overlap — local $\|\operatorname{Rm}\|_{L^2}$ feeds the reaction on $\operatorname{supp}\chi$; global $|E|\le\delta$ feeds the annulus forcing. The cutoff is what makes "curvature energy controlled only on a buffered ball" *sufficient*, because the flow deforms only where $\chi>0$.

### 4. Interior insulation and the pointwise upgrade

Use a two‑scale profile: $\chi\equiv1$ on $B_2$, transition on $B_2\!\setminus\!B_3$, support in $B_3$; the target region is $B_1$. On $\{\chi=1\}\supset B_2$ the cutoff flow **is** the normalized Ricci flow, so Li's smoothing (Theorem 3.6) applies there verbatim: $|\operatorname{Rm}(g(t_0))|\le C/t_0$ on $B_1$ at $t_0\sim r_0^2$, and Li's energy persistence ($\|\operatorname{Rm}\|_{L^2}$ stays $\le 2\times$ initial) holds on $\{\chi=1\}$. Interior parabolic estimates on $B_1$ depend only on data in $B_2\subset\{\chi=1\}$, so they are insulated from the transition annulus by a fixed parabolic distance; annulus curvature growth is further suppressed in the reaction integral by the $\chi^4$ weight. With $|\operatorname{Rm}|\le C/t_0$ and $\int_{B_1}|E(t_0)|^2\le C'\delta^2$ in hand, the parabolic mean‑value inequality (Corollary 3.5 with genuine $\varphi^2=1$ locally, $f=|\operatorname{Rm}|$) upgrades to $\sup_{B_{1/2}}|E(t_0)|\le C\delta$. At $t_0$, on $B_{1/2}$: bounded sectional curvature **and** defect $\le C\delta$ simultaneously, with Shi derivative bounds — the localized "nearly‑Einstein, bounded‑curvature" region your forbidden‑germ argument requires.

### 5. Relation to Yang / Ricci–DeTurck localizations

Yang's local Ricci flow (freeze the metric outside a ball, run a Ricci‑type deformation inside, existence under integral curvature + noncollapsing, with Li removing noncollapsing in 4D) is the sharp‑cutoff sibling of the present flow. The smooth $\chi$ replaces Yang's characteristic‑function ball, which trades a data prescription along $\{ \chi=0\}$ for the smooth annulus terms $\mathcal A[\chi]$ — and §1 shows those terms are homogeneous in $E$ and, by §3, $O(\delta^2)$. On a **closed** $M$ this is an advantage: the metric simply and smoothly ceases to evolve where $\chi=0$, so no data need be prescribed at the frontier of the support and existence follows from the degenerate‑parabolic (strictly parabolic where $\chi>0$) DeTurck flow with $g(0)$ frozen outside $\operatorname{supp}\chi$ as an initial condition on the non‑evolving set. The Ricci–DeTurck gauge is needed only for existence/parabolicity of the $g$‑flow; by the diffeomorphism‑invariance of $|E|$ (§1) it contributes nothing to the defect estimate.

### 6. The one input that must be verified, and dimensional reach

The route is conditional on a single non‑automatic point: **persistence of the local $L^2$ curvature energy on $\{\chi=1\}$ under the cutoff flow.** On $\{\chi=1\}$ the flow is genuinely the normalized Ricci flow, so Li's own persistence argument applies, but one should check that interior estimates on $B_1$ never require energy data from inside the annulus (guaranteed by insulating $B_1\Subset B_2\subset\{\chi=1\}$ and by the $\chi^4$ suppression of the reaction on the annulus). If that check holds, the cutoff flow supplies a self‑contained realization of the $L^2$‑propagation mechanism that your step‑13 note had to leave conditional on a "localized Li theorem": here Li's theorem is used only on the honest normalized‑flow region $\{\chi=1\}$, and the cutoff — not a localization of Li's statement — carries the confinement.

Two features are dimension‑independent and two are not. The defect evolution of §1 (homogeneity, no source, DeTurck‑invariance) and the $\chi^4$‑weighted energy structure of §2–§3 hold for all $n$. The curvature smoothing input (Li 3.6) rests on Cheeger–Tian's Gauss–Bonnet‑based collapsed removal of noncollapsing, which is 4D‑specific; in $n\ge5$ the buffered‑ball energy‑shrinking that supplies the small $\varepsilon_{r_0}$ must be obtained by other means, and the reaction absorption uses the $L^{n/2}$ curvature norm (Li's Remark 3.2) rather than $L^2$. Thus the cutoff flow gives a clean, dimension‑free **defect‑propagation** engine; the remaining dimensional dependence lives entirely in the curvature‑smoothing supply feeding the reaction term.

### 7. Concrete objects to compute next (to make the route decisive)

- The explicit constant in $C_S\varepsilon_{r_0}^{1/2}<c$ as a function of $(n,K_0)$, i.e. the largest $r_0$ (Einstein scale) for which absorption holds — this fixes the size of the guaranteed nearly‑Einstein region.
- The annulus multiplier $\sup(|\nabla\chi|^2+\chi|\nabla^2\chi|)$ for an optimized radial $\chi$ on $B_2\!\setminus\!B_3$, giving the sharp $\delta^2$ prefactor in the interior influence.
- The curvature evolution under the cutoff flow written with all $\nabla\chi$ terms (the non‑source analogue of §1 for $\operatorname{Rm}$), to confirm quantitatively that the annulus curvature terms enter the interior estimate only through $\chi^4$‑suppressed integrals.
- A short verification that the DeTurck displacement $\int_0^{t_0}|W|\,dt$ stays below the buffer width $r_0$ under $|\operatorname{Rm}|\le C/t$, so that $B_1$ maps into $\{\chi=1\}$ throughout.