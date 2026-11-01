# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/scripts/compute_taub_nut_ads_curvature.py",
    "Sessions/S0910A03/workspace/scripts/analyze_taub_nut_ads_multiscale.py",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/Ricci-flow-smoothing-for-locally-collapsing-manifolds-arXiv--fd31dbed4f1f--11306ef80968/object.md"
  ]
}
```

## Task

Develop a rigorous multiscale route for the following specific problem. On a fixed critical Ishida–LeBrun four-manifold suppose Ric(g_i)+g_i tends to zero in operator L-infinity norm, the calibrated nonnegative deficit has total integral tending to zero, and a positive-volume maximal-function set has uniformly bounded averages of |Rm|^2 and vanishing averages of the deficit for every radius up to 1. We may choose, for each point, the buffered downstairs domain before taking its normal/universal cover, at a radius r0 depending only on the curvature-mean bound K. Generate the strongest plausible theorem or countermodel about existence of a fixed r0 and a cover with a noncollapsed harmonic chart. Explicitly analyze persistent rank failure across all radii, the distinction between covers of B_R(p) for different R, and how the calibrated Weyl profile can exclude real-hyperbolic or Taub–NUT-type escape. Give concrete lemmas and proof ideas, not a survey, and identify exactly which statement would advance the fixed-topology negative branch.

## Output

## Reframing: the calibrated Weyl profile changes the question that Taub–NUT–AdS answers

The Taub–NUT–AdS construction refutes a *generic* proposition ("bounded curvature‑mean at all scales on the local universal cover forces noncollapse"). It does not touch the proposition that is actually at stake for a critical Ishida–LeBrun sequence, because at every good basepoint the calibrated deficit pins the Weyl profile away from the Taub–NUT band. The self‑dual annular band of Taub–NUT–AdS has, at fixed distance from the bolt,
$$
|W^+|^2\xrightarrow[\nu\to0]{}0,\qquad s\to -4 ,
$$
so its completed‑square density $(s+8\sqrt6|W^+|)^2\to 16$, i.e. it carries deficit $\gtrsim 16$ on a full‑measure set. A sequence with $\fint F_i\to0$ on a positive‑volume good set therefore *cannot* have Taub–NUT–AdS band geometry at its good points. The correct target is the calibrated regularity statement, and the countermodel is not an obstruction to it. This is the single most important correction: the direct route was abandoned against a proposition strictly weaker than the one the calibrated sequence enjoys.

Below, normalize the target to $\mathrm{Ric}=-g$, $s=-4$. Good set $G_i$: $\mathcal M_{r_0}|\mathrm{Rm}_i|^2\le K_0$ and $\mathcal M_{r_0}F_i\le\varepsilon_i\to0$, with $\mathrm{Vol}(G_i)\ge V_\infty/2$.

## Lemma A (Weyl pinning: exclusion of every $|W^+|\to0$ escape)

Since $F_i\ge (s_i+8\sqrt6|W_i^+|)^2$ and $s_i=-4+\mathrm{tr}_{g_i}h_i$ with $|\mathrm{tr}\,h_i|\le4\delta_i\to0$ uniformly,
$$
\fint_{B_r(p)}\bigl(-4+8\sqrt6\,|W_i^+|\bigr)^2\,d\mu_i\le \varepsilon_i,\qquad \forall\,r\le r_0,\ p\in G_i .
$$
The integrand is a fixed convex function of $|W^+|\ge0$ vanishing only at $|W^+|=1/(2\sqrt6)$. By Chebyshev,
$$
\frac{\mathrm{Vol}\bigl(\{\,|W_i^+|^2\le 1/96\,\}\cap B_r(p)\bigr)}{\mathrm{Vol}(B_r(p))}\le \frac{\varepsilon_i}{4}\to0 .
$$
Thus on almost all of every good ball, at every scale $\le r_0$, $|W_i^+|^2\approx1/24$. Any local model with $|W^+|\to0$ — real‑hyperbolic $\mathbb H^4$ ($W^+\equiv0$), a flat/nilpotent collapse core, a Ricci‑flat ALE/ALF bubble (there $s=0$, so $F\ge16$ as well), or a Taub–NUT–AdS band — is excluded as a positive‑volume good‑point limit. **The calibrated Weyl value $1/24$ is exactly the datum the generic regularity question lacked.**

## Base‑domain monotonicity and the role of $R$

For a fixed loop family, $\mathrm{rank}\,\mathrm{Image}[\pi_1(B_\delta(p))\to\pi_1(B_R(p))]$ is non‑increasing in $R$: enlarging $R$ can only fill more loops. Hence the universal cover of the **small** ball $B_{r_0}(p)$ unwraps *more* collapse loops than that of $B_1(p)$. In Taub–NUT–AdS the $\psi$‑circle at $p$ (distance $\tfrac12$ from the bolt) is nullhomotopic in $B_1(p)$ — it caps at the bolt — but is **not** nullhomotopic in $B_{1/3}(p)$, since the bolt lies outside. So the rank shortfall exhibited at $R=1$ is created solely by admitting the bolt into the base domain; it disappears once the base domain radius is matched to the curvature‑control radius $r_0<\tfrac12$. This is precisely the freedom the task grants: **choose the buffered downstairs domain $B_{r_0}(p)$, with $r_0$ fixed, before covering.** The mean‑transport lemma (Step 8, (T)) is compatible with this: it is stated for a normal cover of a buffered base domain with the radius‑$3s$ cover ball interior, so one works at $q\in B_{r_0/2}(p)$, $s\le r_0/6$.

## Lemma C→D (concentration expulsion at good points)

The mechanism that produced the bolt‑capping is a curvature concentration; the maximal function removes it at all scales $\le r_0$.

**Lemma D.** If $p$ collapses ($\mathrm{Vol}(B_1(p))\to0$) and $\mathcal M_{r_0}|\mathrm{Rm}_i|^2(p)\le K_0$, then for every fixed $r\le r_0$,
$$
\int_{B_r(p)}|\mathrm{Rm}_i|^2\,d\mu_i\;\le\;K_0\,\mathrm{Vol}(B_r(p))\;\le\;K_0\,\mathrm{Vol}(B_1(p))\;\xrightarrow[i\to\infty]{}0 .
$$
The middle step is $\mathrm{Vol}(B_r)\le \mathrm{Vol}(B_1)$ for $r\le1$. So the **absolute** curvature energy in every fixed‑radius ball about a collapsing good point tends to $0$. The same holds for $\int_{B_r}|\mathrm{Ric}_i+g_i|^2\le\varepsilon_i\mathrm{Vol}(B_1(p))\to0$.

Consequences. (i) No bubble can sit inside $B_{r_0}(p)$: a curvature concentration at scale $\rho_i\to0$ inside the ball carries a definite absolute energy $\ge\epsilon_0$ (minimal gravitational‑instanton/ALE energy), which would force $\fint_{B_{d+\rho_i}(p)}|\mathrm{Rm}|^2\ge\epsilon_0/\mathrm{Vol}(B_{d+\rho_i}(p))\to\infty$, contradicting $\mathcal M_{r_0}\le K_0$. (ii) A bolt at distance $>r_0$ survives but lies *outside* the base domain and cannot cap any loop inside $\pi_1(B_{r_0}(p))$. Thus **the very object needed to drop the rank inside $B_{r_0}(p)$ is expelled**, at every scale, uniformly in $i$. This is the structural resolution of "persistent rank shortfall across all radii": at a good collapsing point the count of scales carrying $\ge\epsilon_0$ absolute energy is not merely finite (the $E_0$‑budget backstop) — it is *zero* for large $i$.

## Statement E (the decisive analytic input) and Lemma B′

What remains is to convert small absolute $L^2$ energy into a pointwise curvature bound, without assuming noncollapse. In the exactly‑Einstein case this is Cheeger–Tian's collapsed 4D $\epsilon$‑regularity:
$$
\text{(Einstein, 4D):}\quad \int_{B_{2s}(x)}|\mathrm{Rm}|^2<\epsilon_{CT}\ \Longrightarrow\ \sup_{B_s(x)}|\mathrm{Rm}|\le C s^{-2},
$$
with **no** volume lower bound. The pinching metrics are near‑Einstein, so one needs:

**Statement E (near‑Einstein collapsed 4D $\epsilon$‑regularity).** There exist $\epsilon_0,C$ so that if $\mathrm{Ric}=-g+h$ on $B_{2s}(x)$ with $\int_{B_{2s}}|\mathrm{Rm}|^2<\epsilon_0$ and $\int_{B_{2s}}(|h|^2+|\nabla h|^2)<\epsilon_0$ (scale‑invariantly), then $\sup_{B_s}|\mathrm{Rm}|\le C s^{-2}$.

**Lemma B′ (contrapositive).** A sub‑maximal‑rank (singular) collapse in the annulus carries $\int_A|\mathrm{Rm}|^2\ge\epsilon_0$; equivalently, small annular energy $\Rightarrow$ regular (bounded‑curvature) collapse $\Rightarrow$ maximal rank. Given Statement E and Lemma D, at a good collapsing point the annular energy is $o(1)<\epsilon_0$, hence $\sup_{B_{r_0/2}(p)}|\mathrm{Rm}_i|\le C r_0^{-2}$: **bounded pointwise curvature on a definite ball.**

Two concrete attack ideas for Statement E (this is where the core work belongs):

1. **Integrated Bochner absorbing $\nabla^2h$.** Second Bianchi gives $\delta W^\pm=\mathrm{(const)}\,\nabla h$ and $\Delta\mathrm{Rm}=\mathrm{Rm}*\mathrm{Rm}+\nabla^2 h*g$. Moser iteration for $|\mathrm{Rm}|$ then produces the extra term $\int|\mathrm{Rm}|\,|\nabla^2h|$. Integrate by parts once to trade $\nabla^2h$ against $\nabla\mathrm{Rm}$ and $\nabla h$; the resulting $\int|\nabla h|^2$ is not directly in $G_i$. But the deficit yields it: the completed‑square identities relate $|\nabla W^+|$ to $F$ and to the second Bianchi source, and a Weitzenböck for the near‑harmonic self‑dual forms (Step 9) gives an integral identity for $\int|\nabla h|^2$ in terms of $\int F$ and $\int|\mathrm{Rm}|^2$, both $o(1)$ absolutely at good collapsing points. The claim to establish is that this closes a Moser iteration with the collapsed Sobolev inequality of Cheeger–Tian.
2. **Ricci‑flow smoothing bootstrap (Huang–Wang).** With bounded pointwise curvature already in hand from route 1 on a definite ball, or as an alternative extraction, run the local flow of Theorem 1.1/1.2. Its curvature control $|\mathrm{Rm}_{g(t)}|\le\alpha/t+\varepsilon^{-2}$ and the distance‑distortion estimate (their Appendix A, valid to $t=0$ under a Ricci lower bound) transport the calibrated limit to $t=0$. The obstacle is that their existence time uses maximal rank / almost‑Euclidean isoperimetric on the cover as input; route 1 or Lemma B′ is what would supply that input, after which HW upgrades regularity to all orders and stabilizes the germ.

## Theorem T (assembled)

**Theorem T.** Assume Statement E. There is a fixed $r_0\le\tfrac13$ (any fixed radius works; the constant $\epsilon_0=\epsilon_0(K_0)$ only sets when "large $i$" begins) and $c=c(K_0)>0$ such that for all large $i$ and every $p$ in a definite‑volume subset of $G_i$:

- If $p$ is noncollapsed ($\mathrm{Vol}(B_{r_0}(p))\ge v_0$): at scale $s(K_0)=(\epsilon_{\mathrm{And}}/K_0\omega_4)^{1/4}$ the absolute energy $\int_{B_s(p)}|\mathrm{Rm}|^2\le K_0\omega_4 s^4<\epsilon_{\mathrm{And}}$, and Anderson $\epsilon$‑regularity (bounded Ricci + noncollapse) gives a harmonic chart of size $\ge c\,s$.
- If $p$ collapses: Lemma D + Statement E give $\sup_{B_{r_0/2}(p)}|\mathrm{Rm}_i|\le Cr_0^{-2}$; bounded‑curvature collapse forces the local universal cover of $B_{r_0}(p)$ to have injectivity radius $\ge i_0(C,r_0)>0$ (Cheeger–Fukaya–Gromov / Margulis), hence a noncollapsed harmonic chart of definite size on the cover.

On that chart, $\mathrm{Ric}=-g+o_{L^\infty}(1)$ and $\fint F_i\to0$ transports with a bounded factor (T), so the limit is a smooth Einstein germ with $\mathrm{Ric}=-g$, $s=-4$, and $F_\infty\equiv0$, i.e. $|W^+_\infty|^2=1/24$ with calibrated spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$. The constant‑spectrum projector identity together with the Einstein–Weyl relation ($|\nabla W^+|^2=\tfrac1{16}\ne0$ against $\nabla W^+=0$) forbids this germ. Hence no such good collapsing point exists; since $\mathrm{Vol}(G_i)\ge V_\infty/2>0$, no sequence with $\delta_i\to0$ exists. **This closes the fixed‑topology $\lambda<0$ pinching problem on critical Ishida–LeBrun four‑manifolds.**

Note that $E_0$ enters only as a global backstop: the maximal function already expels concentration at good points, so the finite bubble count $\le E_0/\epsilon_0$ is needed only to bound the volume of the complementary bad set, not the good‑point argument.

## Multiscale count (unconditional hedge)

Independently of Statement E, define scale $r=2^{-a}$ **bad** if $\int_{A(p;r/2,2r)}|\mathrm{Rm}_i|^2\ge\epsilon_0$. Overlapping annuli have bounded multiplicity, so
$$
\#\{\text{bad scales in }[r_0,1]\}\le \frac{C}{\epsilon_0}\int_{B_2(p)}|\mathrm{Rm}_i|^2 .
$$
At a collapsing good point the right side is $\le C\epsilon_0^{-1}K_0\mathrm{Vol}(B_2(p))\to0$: **no bad scales at all** for large $i$. This is the sharpest form of "persistent rank shortfall across all radii is impossible," and it is what makes the fixed $r_0$ legitimate — one does not need to locate a single good scale, every scale $\le r_0$ is regular.

## Exactly what would advance the $\lambda<0$ fixed‑topology program

The entire chain is reduced to one statement: **the near‑Einstein collapsed 4D $L^2$ $\epsilon$‑regularity (Statement E)**, i.e. small absolute $\int|\mathrm{Rm}|^2$ plus $\mathrm{Ric}=-g+o(1)$ (with the deficit control) forcing a pointwise curvature bound without any volume lower bound. Its Einstein specialization is Cheeger–Tian. Proving Statement E — most plausibly by the integrated Bochner of route 1, using the deficit to supply $\int|\nabla h|^2$ via the self‑dual Weitzenböck identity, closed with the Cheeger–Tian collapsed Sobolev inequality — is the decisive step; everything else (Lemmas A, D, the base‑domain monotonicity, the projector germ obstruction, the good‑set volume) is already in hand or elementary. The distinguishing computations that would confirm the picture: (i) verify on the exact hyperbolic cusp $\mathbb R\times T^3$ that $|W^+|\equiv0$, so Lemma A excludes it while its maximal rank confirms that *regular* collapse is not the obstruction; (ii) verify that the Taub–NUT–AdS bolt carries $\int_{\mathrm{bolt}}|\mathrm{Rm}|^2=O(1)$ independent of $\nu$ (the scripts indicate this), which is the $\epsilon_0$ quantum underlying Lemma B′ and the expulsion in Lemma D.