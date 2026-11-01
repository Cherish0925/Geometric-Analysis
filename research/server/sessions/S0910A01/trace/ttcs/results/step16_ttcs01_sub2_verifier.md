# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md",
    "Sessions/S0910A01/workspace/notes/step15_cutoff_smoothing_architecture.md",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Read the corrected smoothing-route files and assess the transition-inclusive cutoff-flow stability problem as mathematics. The goal is not final approval; determine whether the proposed weighted energy route can plausibly yield, on a support of radius comparable to the Li scale, (i) persistence of local normalized L2 curvature energy and interior |Rm|<=C/t, and (ii) global or support-summed Einstein-defect control Q(t0)/A->0 for the near-Einstein LeBrun critical sequence. Explicitly account for Ricci flow having no finite propagation speed, for Li's supremum/covering quantifiers, for cutoff transition terms in the E equation, for the difference between pointwise E control and the weaker normalized L2 target, and for what existing Li/Yang/Wang statements actually supply. Give a direct scientific memo: viable proof skeleton, obstruction terms, exact hypotheses still needed, and whether any part of Step 15's completed-chain wording survives after Step 16.

## Output

## Verifier memo: transition-inclusive cutoff-flow stability for the λ<0 laboratory

### 1. What the whole architecture actually rests on

After reading Steps 14–16 and the Li and Wang sources, the entire chain reduces to **one** analytic object, and both downstream targets (i) and (ii) hinge on it in the same way. That object is:

> a collapse-uniform, transition-inclusive, edge-damped **weighted local-normalized curvature-energy persistence** estimate for the cutoff flow $\partial_t g=-2\chi^2(\operatorname{Ric}+g)$ on the closed manifold, keeping $\big(\fint_{B_{r_*}(y)}|\operatorname{Rm}|^2\big)^{1/2}$ below the Sobolev-absorption threshold for every center $y$ in the support, throughout $0\le t\le\theta r_*^2$.

I verified that this single estimate delivers **both** halves. Here is the logical spine, with the terms checked.

The defect energy identity (A03 §4, algebra confirmed by inspection of $\mathcal C_a(E)$ — every summand carries $E,\tau,\nabla E,\nabla\tau$, so $\mathcal C_a(0)=0$) is
$$
\frac{d}{dt}\int\eta^2|E|^2+c\int\eta^2 a|\nabla E|^2
\le C\!\int(a|d\eta|^2+\eta^2|d\chi|^2+\eta^2a)|E|^2+C\!\int\eta^2a|\operatorname{Rm}|\,|E|^2 .
$$
Taking $\eta\equiv1$ on the closed manifold (legitimate, because outside $\mathrm{supp}\,\chi$ the metric is static, so $\tfrac{d}{dt}\int_M|E|^2=\tfrac{d}{dt}\int_{\mathrm{supp}\,\chi}|E|^2$), the only obstruction term is $\int a|\operatorname{Rm}|\,|E|^2$. Per ball, using the **relative** Sobolev inequality and the volume cancellation that is the genuine engine of this route,
$$
\int_{B_{r_*}(y)}|\operatorname{Rm}|\,|E|^2\le\|\operatorname{Rm}\|_{L^2(B_{r_*})}\,\|E\|_{L^4(B_{r_*})}^2
\le \underbrace{r_*^2\Big(\fint_{B_{r_*}}|\operatorname{Rm}|^2\Big)^{1/2}}_{=\,C_s\|\operatorname{Rm}\|_{L^2},\ \text{volume-free}}\big(\|\nabla E\|_{L^2}^2+r_*^{-2}\|E\|_{L^2}^2\big).
$$
If the normalized curvature energy per ball stays $\le C_{BG}K_0$, the prefactor is $\le r_*^2(C_{BG}K_0)^{1/2}$, small for the fixed small $r_*$; a bounded-overlap sum then absorbs the gradient and leaves $\tfrac{d}{dt}\int_M|E|^2\le C r_*^{-2}\int_M|E|^2$. Gronwall over $t\le\theta r_*^2$ gives
$$
Q(t_0)=\int_M|E(t_0)|^2\le e^{C\theta}\int_M|E(0)|^2=O(\delta_i^2 A_i),\qquad Q(t_0)/A_i=O(\delta_i^2)\to0 .
$$
This is clean and, importantly, needs **only** the local-normalized-energy persistence — not the pointwise $|\operatorname{Rm}|\le C/t$ upgrade.

I also checked that $Q(t_0)/A_i\to0$ is enough for the topological recalibration. Pointwise in dimension four, $E=\operatorname{Ric}+g$ decomposes as trace-free part $E^\circ=\mathring{\operatorname{Ric}}$ and trace $\operatorname{tr}E=s+4$, so
$$
|\mathring{\operatorname{Ric}}|^2=|E^\circ|^2\le|E|^2\quad\Longrightarrow\quad
J_i(t_0)=\frac1{4\pi^2}\!\int\frac{|\mathring{\operatorname{Ric}}|^2}{2}\le\frac{Q(t_0)}{8\pi^2}\to0\cdot A_i .
$$
Hence $J_i(t_0)/A_i\to0$, which is exactly the input Step 16 §2.4 wants, on the same smooth manifold, feeding LeBrun/Chern–Weil and the Step 8 tensor-deficit density $\mathcal G=f^2-(a_-)^2$, $0\le\int\mathcal G\le48\pi^2 D$. This part is sound and does not transport $W^+$ through the flow.

So the redirection to the normalized $L^2$ target rather than pointwise $|E|=O(\delta_i)$ is mathematically the better object: it closes with the favorable homogeneous defect identity and avoids the pointwise subtleties in §4 below.

### 2. Why the supremum-maximality localization cannot close — the precise form of infinite propagation

The Step 15 §9.1 assertion that "Li's proof structure supports localization" and "there is no uncontrolled region nearby" does not hold as stated, and the reason is exactly parabolic infinite propagation made concrete.

Li's Theorem 3.4 closes because $e_0(t)=\sup_{x\in M}\big(\int_{B_r(x)}f^2\big)^{1/2}$ is a genuine supremum over **all** centers of the complete manifold; the single-center evolution $\tfrac{d}{dt}\int_{B_r(x)}f^2\le 2N\|\nabla\phi\|_\infty^2 e_0^2$ is self-referential and closes by maximality of $T'$. The covering $B_{2r}(x)\subset\cup B_r(y_i)$, $y_i\in B_{3r/2}(x)$, pulls neighbor energy into the estimate for center $x$.

On a **bounded** plateau this telescopes outward and never terminates inside the plateau. If the tracked set is centers in $B_{(K-2)r_*}$ (inside $\{\chi=1\}=B_{Kr_*}$), each center's covering reaches $B_{(K-1/2)r_*}$, whose centers are not in the tracked set; controlling them enlarges the set by $\sim2r_*$; after $\sim K$ layers one reaches the transition rim where $\chi<1$ and the clean inequality no longer holds. There is no bounded self-contained set on which the unweighted supremum closes. This telescoping **is** the statement that Ricci flow has no finite propagation speed: the value at an interior point at time $t$ depends on data everywhere with weight $\sim e^{-d^2/4t}$, and the covering makes that dependence visible as an outward chain. The Preceptor's two objections in Step 16 §1 are therefore correct, and the "sqrt(t) prevents boundary influence" phrasing in Step 15 §4.2 is not a theorem.

Consequence: a mere "local version of Li's Theorem 3.4" is not a gap in an otherwise-finished argument; it is the wrong object. The correct object must carry the cutoff weight inside the tracked quantity.

### 3. The weighted route: what plausibly closes, and the one place it is genuinely unproven

Two candidate closures avoid the telescoping, with different residual risks.

**(a) Weighted integral bootstrap (Wang §5, localized).** Wang's local-Ricci-flow curvature-energy inequality in four dimensions,
$$
\frac{d}{dt}\int|\operatorname{Rm}|^2+c\int|\nabla(\chi|\operatorname{Rm}|)|^2\le C\|\nabla\chi\|_\infty^2\int|\operatorname{Rm}|^2 ,
$$
is Gronwall-able: with $\|\nabla\chi\|_\infty^2\sim r_*^{-2}$ and $t\sim r_*^2$ the exponent is $O(1)$, so the **total** support energy stays comparable to its initial value. This is exactly the cutoff apparatus, and it does not telescope. The cubic $\int\chi^2|\operatorname{Rm}|^3$ absorbs collapse-uniformly by the same relative-Sobolev × local-normalized-energy product ($r_*^2(\fint|\operatorname{Rm}|^2)^{1/2}$, volume cancels), summed over a bounded-overlap cover.

The residual difficulty is real and must be stated: a bound on the **total** support energy does not prevent **local concentration** into a single ball, and the cubic absorption needs the **per-ball** normalized energy below threshold at every time. Total-energy control alone does not give that.

**(b) Weighted (edge-damped) local energy quantity.** The resolution I find plausible is to track an **intrinsically weighted** local energy, e.g. $e_\varphi(t)=\sup_y \varphi(y)^2\int_{B_{r_*}(y)}|\operatorname{Rm}|^2$ with $\varphi$ slowly varying and vanishing toward the support rim ($\varphi=0$ on the frozen exterior, $|\nabla\varphi|\lesssim (\text{support width})^{-1}$). The neighbor comparison $\varphi(x)\approx\varphi(y_i)$ for $y_i\in B_{3r_*/2}(x)$ then closes the covering **without** enlarging the tracked region, because the outermost balls carry small weight and the frozen exterior carries weight zero. The transition terms enter as $\|\nabla\chi\|^2$-type contributions, which are controllable when $\varphi$ and $\chi$ are coordinated (e.g. $\varphi=\chi^k$). This is precisely the "transition-inclusive weighted stability estimate on the whole support" the Preceptor §3 asks for.

My assessment: route (b) is the correct target and looks structurally viable, but its closure is **genuinely unproven** and is the crux. What must be shown, and has not been:
- the weighted energy evolution retains a good sign after the slow-$\varphi$ neighbor comparison and the retained transition terms;
- local concentration is excluded by the weight rather than merely bounded in total;
- the collapse-canceling cubic absorption survives at the weighted level.
None of the three is an exposition detail. A03 §7 already identifies "the curvature bootstrap, not the $2/3$-exponent estimate" as load-bearing; the sharpened form is exactly (b).

### 4. Pointwise defect via Corollary 3.5: the $\phi^2$ is not a discardable typo for this use

Step 15 Proposition B and A03 §3 route the pointwise $|E(t)|\le C_\theta\delta_i$ through Li's Corollary 3.5, $|u|\le CA^{2/3}t^{-2/3}(\int_{B_{3r}}u_0^3)^{1/3}$ with $u=|E|$. Two points require attention.

First, Corollary 3.5 as printed reads $\partial_t u\le \phi^2(\Delta u+c_0 fu)$ with $\phi$ undefined. A03 §3.2 reads this as $\partial_t u\le\Delta u+c_0 fu$ (correct for Li's own $\chi\equiv1$ application, since Theorem 2.5 carries no $\phi^2$). But for the **cutoff** application the natural subsolution is $\partial_t u\le\chi^2(\Delta u+c_0 fu)+[\nabla\chi,\nabla^2\chi\ \text{terms}]$, i.e. the $\phi^2$ is not spurious in the cutoff context — yet Corollary 3.5's proof uses the **unweighted** Moser Theorem 2.5, which does not supply a $\chi^2$-weighted $L^3$ estimate and does not carry the transition terms. So citing Corollary 3.5 for the cutoff-flow defect is not licensed; one must re-derive a transition-inclusive weighted $L^3$-Moser estimate. This is additional unproven work, and it reinforces preferring the normalized-$L^2$ route of §1, which needs none of it.

Second, even granting a weighted Corollary 3.5, the pointwise route inherits the same load-bearing requirement (the curvature persistence, since $f=|\operatorname{Rm}|$ must satisfy the Theorem 3.4 hypotheses along the flow). It buys nothing over the $L^2$ route and costs the extra weighted-Moser derivation.

### 5. What Li / Yang / Wang actually supply — and what they do not

- **Li 0911.3104 (Thm 3.1/3.4/3.6).** Supplies the collapse-uniform pairing (relative ball Sobolev $C_s\le C(r^4/\mathrm{Vol})^{1/2}$ against local normalized energy, so volume cancels) and the bounded-overlap covering. Does **not** supply: any cutoff weight; a frozen exterior; a closure over anything but the global all-centers supremum. The all-centers hypothesis holds only at $t=0$ and only on the maximal-function good region; on the full manifold it fails on the concentration set, which is the reason a cutoff is used at all.

- **Yang / Wang Thm 6.3 (LRF).** Supplies the cutoff apparatus $\partial_t g=-2\chi^2\operatorname{Ric}$, short-time existence, the $\chi^2\operatorname{Rm}$/$\chi^2\operatorname{Ric}$ pointwise bounds, and the weighted curvature-energy inequality with the correct critical-absorption shape. Does **not** supply collapse uniformity: its hypotheses are a **global** Sobolev constant $A_0$ on the support and global $\|\operatorname{Rm}\|_{n/2}\le\beta/A_0^2$. On a collapsed support $A_0$ is large and the required smallness is not automatic; the volume cancellation only occurs when the **relative** ball coefficient is paired with **local** normalized energy, which Theorem 6.3 as written does not localize. A03 §5 states this correctly.

- **He (normalized LRF).** Notes the $\operatorname{Ric}-\lambda g$ normalization but its lifespan input needs pointwise full-curvature scales and initial Ricci-defect derivatives that the pre-smoothing near-Einstein sequence does not have. Structural support only.

So neither source is a plug-in. The needed theorem is the **merger**: Li's relative-Sobolev + local-normalized-energy + bounded-overlap covering, carried inside Wang/Yang's cutoff-weighted energy, with an intrinsic edge-damping weight to defeat both the telescoping and the local-concentration risk. The normalization $-2\chi^2(\operatorname{Ric}+g)$ versus $-2\chi^2\operatorname{Ric}$ is a manageable modification; A03 §3.3's time-reparametrization $s=(e^{2t}-1)/2$, $g=e^{-2t}\bar g$, $|E|_g=(1+2s)|H|_{\bar g}$ is a valid interface, and the extra $-2\chi^2 g$ term is lower order on the fixed time window.

Short-time existence deserves one note: with $\chi=0$ on an open set the system is degenerate parabolic; existence is plausible (decoupled: parabolic on $\{\chi>0\}$, static on $\{\chi=0\}$), but the regularization $\chi_\varepsilon=\max(\chi,\varepsilon)$ shifts the difficulty to sequence-uniform estimates as $\varepsilon\to0$, which is again the same bootstrap. Existence with useful uniform estimates is not yet in hand independently of §3.

### 6. The exact hypotheses still required, and a separate geometric layer

To make (i)-persistence and hence (ii) rigorous, the following must be proved, not assumed:

1. A weighted (edge-damped) local-normalized curvature-energy persistence for the cutoff flow, with the intrinsic weight excluding local concentration, the transition terms retained, and the cubic absorbed collapse-uniformly (§3(b)). Constants depending only on dimension, the Ricci lower bound $\operatorname{Ric}\ge-3g$, and the fixed ratios $\ell_{\rm in}<\ell_{\rm work}<\ell_{\rm supp}$ of Step 16 §7.
2. From 1, the absorption of $\int a|\operatorname{Rm}|\,|E|^2$ in the defect identity, giving $Q(t_0)/A_i\to0$ (the computation in §1 above is complete once 1 holds).
3. Sequence-uniform short-time existence of the degenerate cutoff flow on $[0,\theta r_*^2]$ with metric equivalence on the support.

The static quantifier issue is already repaired: Step 16 §7's scale-consistent support (inner $2r_*$, working $8r_*$, support $16r_*$, good set via maximal function + Vitali + Bishop–Gromov) gives every support center the initial normalized smallness with volume-free constants. I checked the comparable-ball arithmetic: $C_{BG}^{\rm local}\approx(13/2)^4\approx1785$ in the small-$r_*$ limit is the right Euclidean ratio, and choosing $r_*^4 C_{BG}^{\rm local}K_0\le\varepsilon_{\rm Li}/2$ is legitimate since $K_0\sim K_{\max}$ is sequence-uniform. This static repair is real and survives.

**A separate, still-open geometric layer.** Even with 1–3 giving bounded $|\operatorname{Rm}|$ on the plateaux and $Q/A\to0$, the Derdziński local contradiction (Step 8) needs the Step 9–11 chart/normal-cover access. Bounded sectional curvature on **collapsed** plateaux does not itself produce the buffered normal Riemannian covers with uniform lifted noncollapse, uniform harmonic radius, deck-averaging buffer, and controlled rank-drop/singular-strata handling. Wang's Prop 3.10–3.12 give Euclidean approximation under bounded $|\operatorname{Rm}|$ **plus** isoperimetric noncollapse — the noncollapse being exactly what is absent; passing to the local universal cover restores noncollapse but transporting the explicit tensor-deficit densities through the nilpotent fibration and deck-averaging is nontrivial. Naming Naber–Zhang or CFG does not close this unless the residual-dimension/rank/local-fibration hypotheses are verified. This layer is independent of 1–3 and is not addressed by the weighted-energy program.

### 7. What survives of Step 15 after Step 16

Surviving as sound mathematics:
- the volume cancellation $C_s\|\operatorname{Rm}\|_{L^2(B_{r_*})}=r_*^2(\fint|\operatorname{Rm}|^2)^{1/2}$ (§4.1) — the engine of collapse uniformity;
- the comparable-ball initial normalized smallness, in the scale-consistent form of Step 16 §7 (not the $B_{\rho/4}$ form of §2.4, which had the $r_*\ll\rho$ mismatch);
- the homogeneity $\mathcal C_a(0)=0$ of the cutoff defect equation (§3.1), verified algebraically;
- topological recalibration in the $J_i(t_0)/A_i\to0$ form (§5.1), now supported by the identity $|\mathring{\operatorname{Ric}}|^2\le|E|^2$ and the $Q/A\to0$ computation;
- the Step 8 Derdziński tensor-deficit contradiction as the final local mechanism.

Not surviving:
- the completed-chain wording and the §10 "Follows from all above" verdict;
- "Plateau energy bootstrap (Prop A)" as a "local version of Li's Thm 3.4" — the object itself is wrong (telescoping); it must be replaced by the weighted estimate of §3(b);
- §9.1 "Li's proof structure supports localization / no uncontrolled region nearby";
- "CFG accessibility from bounded curvature — Established (standard Cheeger–Gromov)" — the cover reconstruction with tensor-deficit transport is unresolved (§6);
- the pointwise Proposition B as a direct application of Corollary 3.5 — the $\phi^2$ form must be re-derived with transition terms for the cutoff flow (§4).

### 8. Extent of the prospective result

Even a complete 1–3 plus the cover-reconstruction layer would exclude only the LeBrun/Ishida–LeBrun critical family of near-Einstein sequences near $k/A\to1/3$ in the $\lambda<0$ case. It uses the specific four-dimensional Seiberg–Witten/Chern–Weil calibration and would not settle arbitrary no-Einstein four-manifolds in that sign case, nor anything in dimensions $n\ge5$ (the Cheeger–Tian input behind the collapse-uniform smoothing is intrinsically four-dimensional, as Li's introduction states). The route's lasting value, if closed, is the transferable tool in item 1: a collapse-uniform, defect-preserving local smoothing with retained cutoff transition terms.

**Overall reading.** The weighted route is coherent and, for the defect target (ii) and the persistence half of (i), reduces cleanly to a single load-bearing lemma whose two ingredient technologies exist. The plausibility is real but not established: the edge-damped weighted curvature-energy bootstrap that simultaneously defeats the outward telescoping (infinite propagation) and local concentration, with retained transition terms and collapse-uniform cubic absorption, is the unproven crux. Two further items remain genuinely open and independent: sequence-uniform degenerate-flow existence with useful estimates, and the normal-cover reconstruction that carries the tensor-deficit densities into the Derdziński contradiction.