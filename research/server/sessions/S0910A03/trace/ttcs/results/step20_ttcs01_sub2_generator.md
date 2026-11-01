# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Develop the strongest viable local weighted parabolic iteration suggested by Wang for a=χ² under the normalized cutoff flow ∂tg=-2a(Ric+g), in dimension four. Focus on a self-contained theorem at the level actually supported by H_q=∫η²a^{q-2}F^q and J_m=∫η²a^{m-2}|E|^m. Seek an exact recurrence whose output norms feed the next stage, with nested localization cutoffs and finite-neighbor terms. Explore whether the curvature hierarchy can produce weighted cubic potential and whether the defect hierarchy can produce |aE| and χ∇(aE) estimates from initial |E|≤δ, while preserving homogeneity at E=0. Explicitly analyze where normalization, derivatives of a, evolving metric/measure, and curvature derivative terms enter. Compare the direct weighted hierarchy against Whitney-ball localization and identify a decisive calculation or counterexample that would choose between them. The result should be a technical construction memo, not a generic roadmap or a conclusion about the full Yau problem.

## Output

## Construction memo: weighted parabolic recurrence for $a=\chi^2$ under $\partial_t g=-2a(\mathrm{Ric}+g)$ in dimension four

### 1. Why the weights $a^{q-2}$ and $a^{m-2}$ are the correct ones

Write $F=|\mathrm{Rm}|_g$, $E=\mathrm{Ric}+g$, $G=|E|_g$, $a=\chi^2$, and set
$$
H_q=\int \eta^2\,a^{q-2}F^{q}\,d\mu,\qquad
J_m=\int \eta^2\,a^{m-2}G^{m}\,d\mu ,
$$
with $\eta$ an independent localization function. The single structural fact that organizes everything is that in dimension four the critical curvature exponent is $n/2=2$, and at $q=2$ the weight $a^{q-2}=a^0$ disappears:
$$
H_2=\int\eta^2 F^2=\text{the unweighted critical curvature energy},\qquad
J_2=\int\eta^2 G^2=Q .
$$
So the hierarchy is anchored at the one exponent where cutoff weighting is scale‑neutral, and the weight $a^{q-2}$ grows only as one climbs above criticality. This is exactly what makes the reaction parameter uniform: the Sobolev product that must be absorbed at every level is $\beta=A^2\|F\|_{L^2}$, and the four‑dimensional cancellation (relative Sobolev $A\lesssim rV^{-1/4}$ against $\|F\|_{L^2}\lesssim K_0^{1/2}V^{1/2}$) gives $\beta=C\sqrt{\varepsilon_{\mathrm{Li}}}$ with volume cancelling. The weight choice is not cosmetic: it is what places the anchor at the volume‑independent exponent.

The natural Sobolev variables are
$$
v_q=a^{(q-1)/2}F^{q/2},\qquad v_q^4=a^{2q-2}F^{2q}\ \Rightarrow\ H_{2q}=\int\eta^4 v_q^4 ,
$$
so the parabolic iteration doubles the exponent $q\mapsto 2q$ and tracks the weight $a^{q-2}\mapsto a^{2q-2}$. As $q\to\infty$, $(a^{q-2}F^q)^{1/q}\to a\,F$, i.e. the $L^\infty$ endpoint of the curvature hierarchy is exactly $\|a\,\mathrm{Rm}\|_\infty$. The defect hierarchy endpoint $(a^{m-2}G^m)^{1/m}\to a\,G=|aE|$ is likewise the object one wants. The exponent bookkeeping in `verify_step20_weighted_moment_hierarchy.py` is the algebraic skeleton of this doubling and is correct.

### 2. Exact curvature recurrence and the four entry points

Test the curvature evolution by $q\,\eta^2 a^{q-2}F^{q-1}$ and integrate. Four mechanisms enter, and each lands in a definite place.

**(a) Principal part and dissipation.** The $a\Delta$-part integrates by parts to
$$
D_q=\int\eta^2\,a^{q-1}F^{q-2}|\nabla F|^2=\tfrac{4}{q^2}\int\eta^2\,a^{q-1}|\nabla F^{q/2}|^2 ,
$$
weight $a^{q-1}$, matching the diffusion density in the script.

**(b) Reaction and the volume‑independent absorption.** The quadratic curvature reaction $a\,\mathrm{Rm}*\mathrm{Rm}$ produces exactly $H_{q+1}=\int\eta^2 a^{q-1}F^{q+1}$ (this is the identity $F\,v_q^2=H_{q+1}$). Setting $z=\eta v_q$ and using unweighted four‑dimensional Sobolev on $z$,
$$
H_{q+1}=\int F\,z^2\le \|F\|_{L^2}\,A^2\big(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2\big)
=\beta\big(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2\big).
$$
Here $\|\nabla z\|_2^2= D_q+\big[(q-1)a^{(q-2)/2}|\nabla\chi|\big]^2\!*F^q+\ (\nabla\eta\text{ terms})$. The first piece is the dissipation; because $\beta$ is a fixed small number **at every level** (the four‑dimensional volume cancellation, `verify_step19_volume_independent_beta.py`), the term $\beta D_q$ is absorbed into $c_qD_q$ uniformly in $q$. The cutoff‑derivative remainder carries the standard Moser factor $(q-1)^2(L/r)^2H_q$ into Grönwall; it grows with $q$ but is summable through the iteration. There is no $q\sqrt{\varepsilon_*}$ degradation in the *reaction*: the earlier worry about that was about repeatedly re‑absorbing curvature by smallness, which is avoided once curvature is treated as a potential (Section 3).

**(c) Normalization enters as a degree‑one source — a genuine cancellation.** Linearizing $R_{ijkl}$ under $\partial_t g=h$ gives a Hessian source $\tfrac12(\nabla_i\nabla_k h_{jl}+\cdots)$. With $h=-2aE$ the pure Hessian term is
$$
S=-\,(\nabla^2 a)\owedge E ,\qquad |S|\le C|\nabla^2 a|\,|E|\le \frac{C\delta}{r^2}.
$$
The decisive point is that one must **not** split $-2aE=-2a\mathrm{Ric}-2ag$ and read off a degree‑zero source $(\nabla^2 a)\owedge g$. Writing $\mathrm{Ric}=E-g$, the source from the $-2a\mathrm{Ric}$ part is $(\nabla^2a)\owedge(E-g)$ and the source from the $-2ag$ part is $(\nabla^2a)\owedge g$; the two $g$‑pieces cancel identically, leaving $(\nabla^2a)\owedge E$. Thus the normalization does not inject an $O(r^{-2})$ inhomogeneous curvature source into the transition annulus; it injects a term of size $O(\delta/r^2)$, degree‑one in the defect. In $H_q$ it contributes $\frac{C\delta}{r^2}\int\eta^2 a^{q-2}F^{q-1}\le \epsilon H_q+C\delta\,(\text{lower moment})$, an $O(\delta)$ Grönwall term over $t\le\theta r^2$. This is what lets $H_2$ stay below $2\varepsilon_*$: the injected critical energy is $O(\delta\theta)$, **not** $O(\theta)$ times the transition volume. I regard this cancellation as the single most consequential item in the memo, because it removes the tension that would otherwise force the critical energy to grow along the transition.

**(d) Evolving metric and measure.** The measure evolves by $\partial_t d\mu=a\,\mathrm{tr}(E)\,d\mu$; near the target $\mathrm{tr}E=R+n=O(\delta)$, so this contributes $\int\eta^2a^{q-1}\mathrm{tr}(E)F^q\le C\delta H_q$. Inverse‑metric variation in $\partial_t F^2$ gives $a\,E*\mathrm{Rm}*\mathrm{Rm}\sim a\delta F^2$, again $\le C\delta H_q$. Both are homogeneous $O(\delta)$ Grönwall terms. (For the defect, the same inverse‑metric variation cancels the cubic $E*E*E$ reaction, as in Step 18; this cancellation should be quoted, not re‑absorbed.)

Assembled,
$$
\boxed{\ \frac{d}{dt}H_q+\tfrac{c_q}{2}D_q\le C\big(r^{-2}(q-1)^2+\delta\big)H_q
+\text{(finite‑neighbor }\nabla\eta\text{ terms)}+C\delta\,(\text{lower moment}).\ }
$$

### 3. The weighted cubic potential is the natural endpoint at $q=3$

Running the parabolic $L^\infty$ iteration ($q=2\to4\to8\to\cdots$, unweighted Sobolev on $z=\eta v_q$, shrinking time intervals) yields
$$
\|a\,\mathrm{Rm}\|_{L^\infty}\le \frac{C\beta}{t},\qquad \beta=C\sqrt{\varepsilon_{\mathrm{Li}}},
$$
and hence the weighted cubic moment
$$
H_3=\int\eta^2\,a\,|\mathrm{Rm}|^3\le \|a\,\mathrm{Rm}\|_\infty\!\int|\mathrm{Rm}|^2\le \frac{C\beta\,\varepsilon_*}{t}.
$$
This is exactly the endpoint estimate Wang computes globally, $\int\chi^2|\mathrm{Rm}|^{n/2+1}\le C A^{-n}t^{-1}(t|\nabla\chi|^2+1)^2$, specialized to $n=4$ and localized. Note that $H_3$ is *not* homogeneous in $E$ and should not be: curvature does not vanish at the Einstein state. It is a smoothing estimate, and its role downstream is only as a fixed time‑dependent coefficient. Its $t^{-1/3}$ cube‑root, $H_3^{1/3}\lesssim t^{-1/3}$, is precisely the $L^3$ potential norm Li's Theorem 2.5 requires.

### 4. Defect recurrence: $|aE|$ from $|E|\le\delta$, with damping and preserved homogeneity

Test $\partial_t E=a(\Delta_L E-2E)+\mathcal C_a(E)$ by $m\,\eta^2a^{m-2}G^{m-2}E$. Three things differ from the curvature side and all help.

- **Damping.** The normalization $-2aE$ gives $-2\int\eta^2a^{m-1}G^m\le0$, genuine extra dissipation absent in unnormalized local Ricci flow. This shift is what turns mere boundedness into the improving factor $(r^2/t)^{2/p}$; the exponent $2/p$ is the balance between this damping and the $t^{-1/3}$ curvature potential in the Li iteration.
- **Curvature reaction through the cubic potential.** The Lichnerowicz curvature coupling produces $\int\eta^2a^{m-1}|\mathrm{Rm}|G^m$. Do not re‑absorb it by critical smallness; interpolate against $H_3$ via the exact identity
$$
F\,v_m^2=(aF^3)^{1/3}\,[a^{-1/3}v_m^2],\qquad v_m=a^{(m-1)/2}G^{m/2},
$$
whose $3/2$‑power is $J_{3m/2}$, the geometric interpolation of $J_m$ and $J_{2m}$. The reaction is therefore controlled by $H_3^{1/3}(t)\,\|v_m\|$-Sobolev terms with a **fixed** time coefficient $\lesssim t^{-1/3}$. This is Li's structure with $p_0=m$.
- **Homogeneity at $E=0$.** Every term in the $J_m$ inequality is degree‑$m$ in $E$; the curvature potential enters only as a coefficient. Hence the output
$$
|aE(x,t)|\le C_p\,\delta\,(r^2/t)^{2/p}\qquad(\text{fixed }p>2)
$$
is degree‑one in $\delta$ (using $\|E(0)\|_{L^p}\le\delta V^{1/p}$ and the volume cancellation $A^{4/p}V^{-1/p}=O(1)$), and it vanishes identically when $E\equiv0$. The stationary Einstein state is a fixed point of the entire construction, as required. The endpoint $p=2$ is logarithmically divergent in the time integral; $p>2$ is where metric comparability closes.

The measure/inverse‑metric terms here are $O(\delta)\cdot J_m$ or higher order, harmless.

### 5. The gradient estimate and exactly where the curvature derivative enters

Differentiate the weighted equation for $U=aE$:
$$
\partial_t(\nabla U)=a\,\Delta_L(\nabla U)-2a\nabla U+\underbrace{a\,\nabla\mathrm{Rm}*U}_{\text{new}}+\underbrace{a\,\mathrm{Rm}*\nabla U}_{H_3\text{ potential}}+\underbrace{\nabla a*\Delta U}_{\text{commutator}}+\nabla^2a*\nabla U+\nabla^3a*U .
$$
Two terms are the entire difficulty. The reaction $a\,\nabla\mathrm{Rm}*U$ needs a weighted curvature‑derivative coefficient, not available from $H_3$ alone; and the commutator $\nabla a*\Delta U$ needs $\Delta U$ near the cutoff zero set, where the weighted energy does not see it. If one has a Shi‑type bound $|a^{1/2}\nabla\mathrm{Rm}|\le C t^{-3/2}$ and $|\Delta U|$ controlled by interior regularity, then the gradient hierarchy closes as a linear degree‑one problem in $\nabla U$ with fixed potential, giving
$$
|\chi\nabla(aE)|\le C_p\,\delta\,t^{-1/2}(r^2/t)^{2/p},
$$
again degree‑one in $\delta$. The p‑threshold arithmetic is real: metric drift integrates for $p>2$ ($\theta^{1-2/p}$), connection and cutoff‑Hessian drift integrate only for $p>4$ ($\theta^{1/2-2/p}$), so $p=6$ controls all three simultaneously as $O(\delta)$. The favorable observation that $\|U\|_\infty\sim a_0^{1-2/p}$ near the cutoff zero set means the weighted defect is *better* controlled where $a\to0$, not worse.

### 6. Direct weighted hierarchy versus Whitney‑ball localization — the decisive calculation

The two organizations agree on the zeroth‑order estimates and diverge on derivatives. The clean way to see why is a Muckenhoupt test on the weight that would be required if one insisted on a genuinely weighted (degenerate‑divergence) treatment.

**Zeroth order — the direct hierarchy is the right tool.** The estimates of Sections 2–4 never need a weighted Sobolev inequality: the weight $a^{(q-1)/2}$ (resp. $a^{(m-1)/2}$) is carried *inside* the Sobolev variable $z=\eta v_q$, and one applies the ordinary unweighted four‑dimensional Sobolev inequality to $z$. All $\nabla\chi$ terms are strictly lower order (Grönwall), and the anchor $H_2=\int F^2$ is unweighted. The volume‑independent $\beta$ gives uniform reaction absorption at every level. This is the natural home for critical‑energy persistence, $\|a\,\mathrm{Rm}\|_\infty\le C\beta/t$, and the fixed‑$p$ defect $|aE|$.

**Derivatives — a structural incompatibility for the direct route.** If one tries to obtain the pointwise Bernstein estimate from a degenerate‑weight Harnack/Nash theory for $\partial_t-\mathrm{div}(a\nabla)$, the relevant weight is $a=\chi^2$. With a Lipschitz cutoff, $\chi$ vanishes linearly on its codimension‑one zero set, so $a\sim d^2$ with $d$ the distance to that set. The Muckenhoupt $A_2$ range for a codimension‑one distance weight $d^\gamma$ is $-1<\gamma<1$; the value $\gamma=2$ is outside it, and indeed $\int_{-\epsilon}^{\epsilon} d^{-2}=\infty$. Hence $a=\chi^2\notin A_2$ and the Fabes–Kenig–Serapioni degenerate‑parabolic theory does not apply. Worse, the requirement is genuinely incompatible with the flow: to place $a=\chi^2$ inside $A_2$ one would need $\chi\sim d^{s}$ with $s<1/2$, which forces $|\nabla\chi|\to\infty$ at the zero set and destroys the bound $|\nabla\chi|\le L/r$ that both short‑time existence and the drift control depend on. So one cannot simultaneously have an $A_2$ weight and a Lipschitz cutoff. Concretely, in the gradient equation this shows up as the commutator $\nabla a*\Delta U$: on the cutoff zero set $\nabla a\ne0$ while $\Delta U$ is invisible to the $a$‑weighted energy, and the term is not controlled.

**Whitney localization bypasses exactly this.** On a Whitney ball $B_\ell(y)$, $\ell=cr\chi_0$, the weight satisfies $a/a_0\in[(1-Lc)^2,(1+Lc)^2]$, so $a$ never vanishes inside the ball and the operator is uniformly parabolic with $\chi_0$‑independent ellipticity. The Bishop–Gromov energy transfer $\ell^4\fint_{B_\ell}|\mathrm{Rm}|^2\le CK_0r^4$ and the Sobolev cancellation $A_\ell^2\|\mathrm{Rm}\|_2\le C\sqrt{K_0}\,r^2$ are both independent of $\chi_0$ and of collapsed volume. Once $\|a\,\mathrm{Rm}\|_\infty\le C/t$ is in hand (by either method), Shi's local derivative estimates apply verbatim on each ball with effective time $a_0t$, giving $|\nabla\mathrm{Rm}|\le C(a_0t)^{-3/2}\cdot(\cdots)$ and hence $|\chi\nabla\mathrm{Rm}|\lesssim t^{-3/2}$ and the weighted Bernstein for $\chi\nabla U$ — with no $A_2$ requirement and no global cutoff‑derivative induction.

**The decisive test to run.** Attempt the weighted Bernstein for the degenerate operator directly and track the commutator $\nabla a*\Delta U$ and the reaction $a\nabla\mathrm{Rm}*U$ through one energy step; compare against the Whitney per‑ball Shi estimate with effective time $a_0t$. The direct route requires a bound on $\Delta U$ at the cutoff zero set that the $a$‑weighted energy does not supply, and (equivalently) an $A_2$ weight it cannot have with a Lipschitz cutoff; the Whitney route produces the same bound from a non‑degenerate interior estimate. A second, cleaner numerical test: verify that $\int_{-\epsilon}^{\epsilon} d^{-2}$ diverges while the analogous quantity on a single Whitney ball is finite and $\chi_0$‑independent. These two computations decide the division of labor unambiguously.

**Resolution.** The comparison is not winner‑take‑all. The direct weighted hierarchy is decisively correct for the four‑dimensional zeroth‑order package (critical energy $H_2$, cubic potential $H_3\le C\beta/t$, fixed‑$p$ defect $|aE|$), where its uniform‑in‑$q$ reaction absorption and the degree‑one normalization cancellation are genuine advantages. The Whitney‑ball localization is decisively correct for the derivative package ($\chi\nabla U$, $\chi^2\nabla\mathrm{Rm}$), which the direct route cannot close without a weight it structurally cannot have. A self‑contained theorem at the level actually supported is therefore: *the direct $H_q,J_m$ recurrence delivers $H_2$ persistence, $\|a\,\mathrm{Rm}\|_\infty\le C\beta/t$, $H_3\le C\beta\varepsilon_*/t$, and $|aE|\le C_p\delta(r^2/t)^{2/p}$ with volume‑independent constants and preserved homogeneity at $E=0$; the gradient conclusions are supplied by Whitney per‑ball Shi/Bernstein fed by the same $\|a\,\mathrm{Rm}\|_\infty$ bound.*

### 7. What each hierarchy definitely produces, and what it does not

The curvature hierarchy produces the weighted cubic potential $H_3$ (this is Wang's endpoint moment, localized). The defect hierarchy produces $|aE|$ from $|E|\le\delta$ with exact homogeneity, using $H_3^{1/3}\sim t^{-1/3}$ as a fixed coefficient. The defect hierarchy produces $\chi\nabla(aE)$ only after the curvature‑derivative coefficient $a^{1/2}\nabla\mathrm{Rm}$ is available, which within the pure moment framework arrives through the spacetime dissipation $\int_0^T D_q$ plus interpolation, and cleanly through Whitney Shi. The normalization enters as the degree‑one Hessian source $(\nabla^2a)\owedge E$ (after the $g$‑cancellation), the derivatives of $a$ enter through $|\nabla a|^2/a=4|\nabla\chi|^2$ Grönwall remainders and the Bernstein commutator, the evolving measure enters as $a\,\mathrm{tr}(E)$ at order $\delta$, and the curvature derivative enters only in the gradient stage. The unweighted defect $Q=\int|E|^2$ remains a separate degree‑two energy identity, since the weighted pointwise estimates say nothing where $a\to0$; its Grönwall $Q(t)\le e^{C\theta}Q(0)$ is independent of the weighted machinery and should be kept as its own lemma.