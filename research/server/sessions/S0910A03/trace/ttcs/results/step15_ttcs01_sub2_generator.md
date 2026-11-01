# TTCS Independent Branch Record

```json
{
  "step_id": 15,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/workspace/scripts/verify_L2_completion_square_chain.py"
  ]
}
```

## Task

On a fixed critical Ishida-LeBrun 4-manifold M with Einstein defect E = Ric+g and a normalized cutoff flow ∂_t g = -2χ²E, the evolution of the GLOBAL L² defect Q(t) = ∫_M |E(t)|² dμ(t) is the key quantity for the topological near-saturation argument.

The challenge: the integrated energy inequality involves terms with |Rm||E|², and |Rm| is not initially bounded (Weyl can be large). The flow produces bounded curvature only after a positive time, creating a bootstrap problem.

GENERATE a concrete mechanism to control Q(t) on a short time interval [0,T] with T = O(r₀²), specifically:

1. Can the L² estimate be SEPARATED from the curvature bootstrap? For example: (a) On the plateau (χ=1), Li's Cor 3.5 gives |E| ≤ Cδ(r²/t)^{2/3}, so ∫_plateau|E(t)|² is controlled. (b) The frozen exterior contributes ∫_frozen|E₀|² = O(δ²Vol). (c) For the transition region: explore whether the DEGENERATE parabolic structure (coefficient χ² between 0 and 1) provides enough suppression. The L² contribution from the transition has width D, and |E|² there might be controlled by interpolation between the plateau (small E) and frozen boundary (E = δ).

2. Alternatively: can the GLOBAL L² estimate be obtained directly from the fact that every term in the cutoff equation is homogeneous in E? Even without a pointwise |Rm| bound, the reaction ∫|Rm||E|² might be controlled by using the INITIAL L² bound on |Rm|² (which is O(A) from topology) combined with a 4D Sobolev inequality on a COVERING by balls. Does the bounded-overlap covering + relative Sobolev produce a collapse-independent global Sobolev constant?

3. Or: can we avoid the global Q(t) estimate entirely by using only the INTEGRAL identities? The completion-square chain gives ∫(|W⁺|-1/(2√6))² ≤ 0.41∫|E|² for any metric. If we can show that the INTEGRATED ∫∫₀ᵀ|E(t)|² dt dμ is controlled (even if Q(t) at specific times is not), this might suffice for a time-averaged topological argument.

Look for the simplest, most robust mechanism.

## Output

## The one genuinely dangerous term, and why the rest is harmless

Before choosing a control mechanism, decompose the reaction exactly. Under the closed-manifold cutoff flow the volume‑weighted defect obeys

$$
\frac{d}{dt}Q=\int_M\Big[-2a|\nabla E|^2+4a\,\mathrm{Rm}(E,E)+2\langle E,\mathcal C_a(E)\rangle+|E|^2\Delta a-a\tau|E|^2\Big]\,d\mu ,
\qquad a=\chi^2 .
$$

Insert the Kulkarni–Nomizu split in dimension four, $R=W+\tfrac12\,\mathrm{Ric}_0\owedge g+\tfrac{s}{24}\,g\owedge g$, into $4R_{ikjl}E_{ij}E_{kl}$. Two of the three pieces are benign:

- **Scalar piece.** $(g\owedge g)_{ikjl}E_{ij}E_{kl}=2(\tau^2-|E|^2)$, so this contributes $\tfrac{s}{3}(\tau^2-|E|^2)$. With $s\approx-4$ and $\tau^2\le4|E|^2$ this is a bounded multiple of $|E|^2$ — a pure Gronwall term.
- **Traceless‑Ricci piece.** Here the identity $\mathrm{Ric}_0=E_0$ is exact: $E=\mathrm{Ric}+g$, $\tau=s+4$, so $E-\tfrac{\tau}{4}g=\mathrm{Ric}-\tfrac{s}{4}g=\mathrm{Ric}_0$. Hence $\tfrac12(\mathrm{Ric}_0\owedge g)(E,E)$ is **cubic** in $E$, bounded by $C|E|^3\le C\|E\|_\infty|E|^2$.

Only the **Weyl piece** $4W(E_0,E_0)\le C|W|\,|E|^2$ carries an unbounded coefficient. All the $\mathcal C_a$, $\Delta a$, $\tau|E|^2$ terms are homogeneous in $E$ and, by the Young/integration‑by‑parts algebra already recorded (`verify_cutoff_defect_energy.py`), reduce to $C\!\int(a+|\nabla\chi|^2)|E|^2$ plus a gradient part absorbable by the $-2\!\int a|\nabla E|^2$ reservoir. So the entire problem is: **control $\int a|W|\,|E|^2$.** Nothing else in the identity requires a pointwise curvature bound. This is worth isolating explicitly because it shows the obstruction is one term, not the whole energy inequality.

## Primary mechanism: confine the flow to a single good ball

The simplest robust route removes the concentration difficulty at the source rather than fighting it. Do **not** smooth all of $M$. The topological near‑saturation argument is a global *integral* identity on the fixed closed manifold; bounded curvature is needed only on one plateau ball to extract a limit. So put the cutoff at a single well‑chosen point and freeze the rest.

Pick $p$ with $\displaystyle\operatorname*{avg}_{B_{3r_0}(p)}|\mathrm{Rm}|^2\le\Lambda$. Such $p$ exists off a set of measure $\le C\Lambda^{-1}\!\int|\mathrm{Rm}|^2$ (centered maximal function; $\int|\mathrm{Rm}|^2=O(\mathrm{Vol})$ from topology plus the calibrated profile), and the calibrated value $|W^+|\approx\tfrac1{2\sqrt6}$ merely fixes $\Lambda\gtrsim\tfrac1{24}$ — it does not obstruct good points, it only forces $r_0\lesssim\varepsilon_{\mathrm{Li}}^{1/4}$, which is exactly the small‑radius bridge. Take $\chi=1$ on $B_{r_0/8}(p)$, $\chi=0$ outside $B_{r_0}(p)$, transition in the collar $B_{r_0}(p)\setminus B_{r_0/8}(p)$.

Now $\operatorname{supp}(aE)\subset\subset B_{3r_0/2}(p)$, so a **single** relative Sobolev inequality on that one ball handles the Weyl term — no bounded‑overlap covering is needed at all:

$$
\int_{M}a\,|W|\,|E|^2
\le \|W\|_{L^2(B_{3r_0/2})}\,\|aE\|_{L^4}^2
\le C\,\varepsilon^{1/2}\Big(\|\nabla(aE)\|_2^2+r_0^{-2}\|aE\|_2^2\Big),
\qquad \varepsilon=(3r_0/2)^4\!\!\operatorname*{avg}_{B_{3r_0/2}}\!|\mathrm{Rm}|^2 .
$$

The relative Sobolev constant carries $r^2/\mathrm{Vol}(B_r)^{1/2}$ and $\|W\|_{L^2}$ carries $\mathrm{Vol}^{1/2}$: **the volume cancels identically**, leaving the collapse‑free coefficient $C\varepsilon^{1/2}$. Because $\varepsilon\le\Lambda(3r_0/2)^4\le\varepsilon_{\mathrm{Li}}$ is small, $\|\nabla(aE)\|_2^2\le 2\int a|\nabla E|^2+Cr_0^{-2}\!\int|\nabla\chi|^2|E|^2$ is absorbed into the dissipation. What survives is

$$
\frac{d}{dt}\,Q_{\mathrm{active}}(t)\le \frac{C}{r_0^{2}}\,Q_{\mathrm{active}}(t),
\qquad
Q_{\mathrm{active}}(\theta r_0^2)\le e^{C\theta}\,Q_{\mathrm{active}}(0)\le e^{C\theta}\delta^2\,\mathrm{Vol}(B_{r_0}) .
$$

The frozen exterior contributes the unchanged $\int_{\chi=0}|E_0|^2\le\delta^2\mathrm{Vol}(M)$. Hence

$$
\boxed{\ \frac{Q(\theta r_0^2)}{\mathrm{Vol}}\le C'\delta^2\longrightarrow 0.\ }
$$

Because the cutoff flow lives on the fixed closed $M$ and changes no topology, the completion‑square chain (`verify_L2_completion_square_chain.py`) applies verbatim to $g_i(\theta r_0^2)$:

$$
\int_M\Big(|W^+(t)|-\tfrac1{2\sqrt6}\Big)^2\le 0.41\,Q(t)\le C\delta^2\mathrm{Vol}\to 0 \ \text{(normalized)} ,
$$

while on the plateau $B_{r_0/8}(p)$ the metric now has $|\mathrm{Rm}|\le C/(\theta r_0^2)$ and, by Corollary 3.5, $|E|\le C_\theta\delta$ pointwise. This is exactly the pair — global normalized calibration plus local bounded curvature — that the limit‑extraction needs.

**What this route buys.** It converts the global $Q$-control into (i) one relative Sobolev inequality on one ball, (ii) an initial local energy smallness that holds by choice of $p$, and (iii) the trivial frozen estimate. It never invokes a global Sobolev constant (which does degenerate under collapse) and never touches the concentration set.

## Direct answers to the three suggested routes

**(1) Separation into plateau/frozen/transition.** This is essentially the primary mechanism, but the transition need not be estimated by interpolation. Once the whole cutoff sits in one good ball, the transition annulus is *inside* the region where the single Sobolev inequality already controls the Weyl reaction; its $|\nabla\chi|^2|E|^2$ contribution is a benign $Cr_0^{-2}Q$ term. No separate interpolation between plateau‑small and frozen‑$\delta$ values is required.

**(2) Global Sobolev via bounded‑overlap covering.** The covering produces a *sum of collapse‑robust local inequalities*, not a single collapse‑independent global Sobolev constant — the latter genuinely degenerates as $\mathrm{Vol}\to0$. The covering version works only if every center carries small local energy, which breaks on the concentration set. Confining to one good ball removes the need for the covering entirely, so route (2) is real but strictly heavier than route (1); it becomes necessary only if one insists on smoothing all of $M$, which the topological argument does not require.

**(3) Time‑integrated $\int_0^T\!\!\int|E|^2$.** With the pointwise‑in‑time Gronwall of route (1) this is not needed. Note also that Corollary 3.5's $|E|\le C\delta(r^2/t)^{2/3}$ makes $\int_0^T|E|\,dt$ convergent ($t^{-2/3}$) but $\int_0^T|E|^2\,dt$ divergent at $t=0$ ($t^{-4/3}$); the space‑time $L^2$ average therefore *cannot* be used naively near $t=0$. It survives only as a backup: the parabolic energy identity delivers $\int_0^T\!\int a|\nabla E|^2$ bounded by $Q(0)$ regardless, so if the pointwise coefficient were ever marginal, the dissipation integral remains a controlled reserve.

## The single remaining analytic object

Everything above is conditional on **persistence of the local curvature energy along the cutoff flow**: $\varepsilon(t)=(3r_0/2)^4\operatorname{avg}_{B_{3r_0/2}(p)}|\mathrm{Rm}(t)|^2\le\varepsilon_{\mathrm{Li}}$ for $t\in[0,\theta r_0^2]$, together with $|\mathrm{Rm}(t)|\le C/t$ on the plateau. This is exactly the load‑bearing bootstrap already isolated in `step14` §5, and it is unchanged by the present simplification. Its curvature evolution under $\partial_t g=-2\chi^2\mathrm{Ric}$ carries extra $\nabla\chi*\nabla\mathrm{Rm}$ and $\nabla^2\chi*\mathrm{Rm}$ terms living in the collar. The concrete object to establish is a maximal‑energy inequality of the form

$$
\frac{d}{dt}\!\int \chi^2|\mathrm{Rm}|^2+c\!\int|\nabla(\chi|\mathrm{Rm}|)|^2\le C|\nabla\chi|_\infty^2\!\int_{\operatorname{supp}\nabla\chi}|\mathrm{Rm}|^2 ,
$$

which is precisely Wang's sourced 4D form (`wang2009pseudolocality`, Thm 6.3) *if* its global‑Sobolev/global‑support input is replaced by the single‑ball relative Sobolev used above. Establishing this one localized inequality closes the entire $Q$-control and simultaneously supplies the $C/t$ bound Corollary 3.5 needs. The advance is that the defect side is now fully handled and only this curvature‑energy persistence remains.

## Two distinct alternatives worth cheap exploration

**A pointwise route that bypasses $Q$ entirely.** Kato gives $(\partial_t-a\Delta)|E|\le 2a|W|\,|E|+C|E|$ on the plateau. Rather than an $L^2$ Gronwall, one can attempt a direct maximum‑principle bound using the *integrable* singular factor: the $2/3$-exponent estimate makes $\int_0^t|W|\,d\tau$ finite even as the pointwise curvature blows up like $C/\tau$, because Corollary 3.5's structure controls the potential in $L^3$, not $L^\infty$. If a De Giorgi–Nash–Moser iteration for the subsolution $|E|$ can be run with the $L^3$ Weyl potential (subcritical in 4D once the local energy is small), it yields $|E(\theta r_0^2)|\le C_\theta\delta$ pointwise on the plateau *directly*, and then $Q$-control becomes a corollary rather than a prerequisite. This is the same mechanism as Corollary 3.5 but re‑derived so that the $L^2$ and $L^\infty$ statements are not separate load‑bearing steps.

**A level‑set decomposition if global smoothing is ever forced.** If some later step needs bounded curvature on more than one ball, replace the excision by a De Giorgi truncation of the Weyl coefficient: split $W=W\mathbf 1_{|W|\le\Lambda}+W\mathbf 1_{|W|>\Lambda}$. The bounded part gives $\Lambda Q$; the tail obeys $\int_{|W|>\Lambda}|W|\,|E|^2\le\|E\|_\infty^2\Lambda^{-1}\!\int|W|^2=O(\delta^2\mathrm{Vol}\cdot\Lambda^{-1})$ *provided* $\|E\|_\infty$ is propagated. This trades the geometric excision for the pointwise‑defect propagation of the first alternative; the two are dual, and whichever of $\|E\|_\infty$ or single‑ball confinement is easier to secure determines which to use.

The recommendation implicit in this material: the single‑good‑ball route is the least assumption‑laden — one Sobolev inequality, one energy persistence statement, one trivially cheap frozen term — and it exploits the fact that the calibration is a global integral on a fixed topology, so global bounded curvature is simply not part of the requirement.