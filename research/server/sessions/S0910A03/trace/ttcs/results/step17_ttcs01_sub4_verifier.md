# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/scripts/verify_normalized_cutoff_maximum_principle.py"
  ]
}
```

## Task

Verify the following claim about the normalized cutoff flow ∂_t g = -2χ²(Ric + g) on a closed 4-manifold. The Einstein defect E = Ric + g satisfies ∂_t E = a(Δ_L E - 2E) + C_a(E) where a = χ². The claim is that |E|² satisfies a scalar parabolic inequality where the reaction term has NO quadratic-in-|E|² loss independent of δ. Specifically: (1) In the Lichnerowicz contribution to ∂_t|E|², the -4a·Ric(E,E) - 4a|E|² terms combine to -4a·tr(E³), because Ric = E - g gives Ric(E,E) = tr(E³) - |E|², and the ±4a|E|² cancel exactly. (2) Therefore the full reaction at a maximum point is bounded by C(|Rm| + δ + r⁻²)|E|², where δ = ||E||_∞. (3) The resulting Gronwall gives ||E(t)||_∞ ≤ √2·δ for t ≤ θr² with θ = O(1/(K₀r² + 1)), which is an a priori bound requiring NO curvature-bootstrap output. (4) This breaks the continuation circle because metric equivalence follows directly from the defect bound: |∂_t log|v|²| ≤ 2|E| ≤ 2√2·δ. Check each step for mathematical correctness, paying special attention to: the sign of the Lichnerowicz Laplacian convention, whether the maximum principle applies to the degenerate equation (a = 0 boundary), and whether the cubic term 4a|tr(E³)| ≤ 4a|E|³ ≤ 8aδ|E|² is correctly bounded.

## Output

## Verifier Memo: Defect Evolution under the Normalized Cutoff Flow

I checked the algebra of the $|E|^2$ evolution, the reaction bound, the Gronwall estimate, the metric-equivalence step, and the behavior at the degenerate locus $a=0$. The four end statements you list are structurally sound and lead to a valid a priori estimate **conditional on smooth existence and a time-uniform curvature bound**. However, the derivation written in Step 17 §1 contains a genuine algebraic omission, and the Python script tests only a trivial identity, not the actual PDE. The correct computation is in fact cleaner than the note states. Details follow, grounded in the two notes and the script.

### 1. The evolution identity: Step 17 §1 drops a term; Step 14 §4 has it right

The variation of $|E|^2$ under $\partial_t g=-2aE$ has **two** sources, not one:

$$
\partial_t|E|^2 = \underbrace{2(\partial_t g^{ik})g^{jl}E_{ij}E_{kl}}_{\text{inverse-metric term}} + 2\langle E,\partial_t E\rangle,
\qquad \partial_t g^{ik}=2aE^{ik}.
$$

The inverse-metric term equals $4a\,\mathrm{tr}(E^3)$ (both $g^{-1}$ factors, by symmetry, with $E^{ik}(E^2)_{ik}=\mathrm{tr}(E^3)$). **Step 17 §1 omits this term entirely**: it writes $\partial_t|E|^2 = 2\langle E,a(\Delta_L E-2E)\rangle + 2\langle E,\mathcal C_a(E)\rangle$, i.e. only $2\langle E,\partial_t E\rangle$.

Carry the omitted term through. Using
$$
2\langle E,\Delta_L E\rangle=\Delta|E|^2-2|\nabla E|^2+4\operatorname{Rm}(E,E)-4\operatorname{Ric}(E,E),
\qquad
\operatorname{Ric}(E,E)=\mathrm{tr}(E^3)-|E|^2,
$$
one gets, for $a=1$,
$$
(\partial_t-\Delta)|E|^2 = -2|\nabla E|^2 + 4\operatorname{Rm}(E,E),
$$
because the inverse-metric $+4\,\mathrm{tr}(E^3)$ cancels the Lichnerowicz–Ricci $-4\,\mathrm{tr}(E^3)$, **and** the $\pm4|E|^2$ terms cancel. The cubic term is not merely small — it vanishes. This matches exactly the identity already stated in Step 14 §3.1, and in cutoff form the same cancellation gives
$$
(\partial_t-a\Delta)|E|^2 = -2a|\nabla E|^2 + 4a\operatorname{Rm}(E,E) + 2\langle E,\mathcal C_a(E)\rangle,
$$
which is precisely the Step 14 §4 identity.

Consequence: Step 17 §1's intermediate result "$-4a\,\mathrm{tr}(E^3)$ residual, hence an $O(\delta)|E|^2$ perturbation requiring $|E|\le2\delta$ throughout" is spurious. It arises solely from the dropped inverse-metric term. The honest reaction has **no cubic term and no $\delta$-dependent reaction**; the $|E|\le2\delta$ assumption Step 17 invokes to bound $4a|\mathrm{tr}(E^3)|\le8a\delta|E|^2$ is unnecessary. So Step 14 and Step 17 are internally inconsistent, and Step 14 is the correct one. The task's statement (1) — "the $\pm4a|E|^2$ cancel and the residual is $-4a\,\mathrm{tr}(E^3)$" — reflects the flawed Step 17 route; the residual is actually zero once the metric variation is included.

### 2. What `verify_normalized_cutoff_maximum_principle.py` actually tests

PART 1 checks only
$$
-4(\mathrm{tr}(E^3)-|E|^2)-4|E|^2 = -4\,\mathrm{tr}(E^3),
$$
a one-line SymPy tautology in diagonal $E$. It does **not** form $\partial_t|E|^2$, does not include $\partial_t g^{ik}=2aE^{ik}$, and therefore cannot see the second $\mathrm{tr}(E^3)$ contribution. In effect the script confirms the flawed intermediate of Step 17 rather than the PDE. The remaining PARTS (Gronwall exponent, drift, Bishop–Gromov ratio, $\bar K$ table, additive-energy table) are numerical plausibility evaluations with hand-inserted constants ($C=10$, $C_{\text{lemma}}=100$, etc.); they exercise arithmetic of the final inequalities, not their derivation. To actually certify the reaction, the script should assemble $\partial_t|E|^2$ symbolically with both inverse-metric factors and confirm the cubic cancellation directly.

### 3. Reaction bound and the maximum principle (statement (2))

With the corrected identity the reaction is $4a\operatorname{Rm}(E,E)\le 4a|\operatorname{Rm}|\,|E|^2$, plus the cutoff cross-terms. The cutoff term bound
$$
|2\langle E,\mathcal C_a(E)\rangle|\le \varepsilon a|\nabla E|^2 + C(\varepsilon^{-1}r^{-2}+1)|E|^2
$$
is legitimate pointwise, and its coefficients are uniform up to the degenerate locus precisely because $a=\chi^2$ makes $|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}$ and $|\nabla^2 a|\le Cr^{-2}$. Choosing $\varepsilon<2$, the good diffusion $-2a|\nabla E|^2$ absorbs the gradient piece, leaving pointwise
$$
(\partial_t-a\Delta)|E|^2 \le C(|\operatorname{Rm}|+r^{-2})|E|^2.
$$
So statement (2) holds with the $\delta$ term simply unnecessary; $C(|\operatorname{Rm}|+r^{-2})|E|^2$ is the sharp form. Note also that at an interior maximum the term $\tfrac12\nabla^k a\,\nabla_k|E|^2$ vanishes ($\nabla|E|^2=0$), so the first-order cutoff transport does not even enter the max-point estimate.

**Degenerate locus $a=0$.** The a priori maximum-principle argument survives the degeneracy: at any spatial maximum in $\{a>0\}$ one has $a\Delta|E|^2\le0$ (since $a\ge0$, $\Delta|E|^2\le0$), and on the interior of $\{a=0\}$ all derivatives of $a$ vanish so $\mathcal C_a(E)=0$ and $E$ is frozen. The upper Dini derivative of $\sup_M|E|^2$ is thus controlled by the reaction at the max point. This is a valid Hamilton-type estimate **given** a smooth solution; the degeneracy affects existence/regularity, not this bound. So statement (2) and the max-principle structure are correct, conditional on smooth existence of the flow.

### 4. The Gronwall constant needs a time-uniform curvature bound (statement (3))

The estimate $\tfrac{d}{dt}\sup|E|^2\le C(K+r^{-2})\sup|E|^2$ requires $K=\sup_{[0,\theta r^2]}\sup_M|\operatorname{Rm}(g(t))|$, not just the initial $K_0=\sup_{\mathrm{supp}\chi}|\operatorname{Rm}(g_0)|$. The note fixes $\theta=\ln2/(C(K_0r^2+1))$ using $K_0$, justified by "the metric barely drifts." But bounded metric drift within a factor 2 (from §2) controls $g$, not $\operatorname{Rm}$, which is two derivatives of $g$; equivalence of metrics does not bound the curvature of the evolved metric. Keeping $K$ near $K_0$ over the interval is exactly the transition-region curvature propagation the note itself lists as OPEN in §9 and in the Step 14 §7 "load-bearing unresolved work." Hence statement (3)'s "an a priori bound requiring NO curvature-bootstrap output" is not accurate as stated: the defect maximum principle removes the metric-equivalence link of the continuation circle, but a time-uniform $|\operatorname{Rm}(g(t))|$ bound remains a required input to freeze the Gronwall constant. The correct reading is: Prop 1 holds conditional on (i) smooth existence and (ii) a time-uniform curvature bound of order $K_0$ on $\mathrm{supp}\,\chi$.

### 5. Metric equivalence (statement (4)) — valid

$\big|\partial_t\log|v|_{g(t)}^2\big| = \big|\tfrac{-2aE(v,v)}{g(v,v)}\big| \le 2a\|E\|_{op}\le 2|E|\le 2\sqrt2\,\delta$, using $\|E\|_{op}\le\|E\|_F=|E|$ and $a\le1$. Integrating over $[0,\theta r^2]$ gives $|\log(g(t)/g_0)|\le 2\sqrt2\,\delta\theta r^2\to0$. This step is elementary and correct, and it genuinely follows from the defect bound alone — no curvature input. So (4) is sound, contingent only on (3).

### Net assessment

- The **inverse-metric term is missing in Step 17 §1**; its "$-4a\,\mathrm{tr}(E^3)$ residual / $O(\delta)$ perturbation" is an artifact. The true reaction is $4a\operatorname{Rm}(E,E)$ with full cubic cancellation, exactly as in Step 14 §4. Aligning Step 17 with Step 14 removes the internal inconsistency and the artificial $|E|\le2\delta$ bootstrap.
- The **script certifies a tautology**, not the evolution; a direct symbolic assembly of $\partial_t|E|^2$ including $\partial_tg^{ik}=2aE^{ik}$ would properly confirm the cancellation and is the check worth adding.
- **Statement (2)** is correct (sharper without $\delta$); the **degenerate-locus** maximum principle is valid as an a priori estimate for a smooth solution, uniform up to $a=0$ thanks to $a=\chi^2$.
- **Statement (3)** holds only with a time-uniform $|\operatorname{Rm}(g(t))|$ bound; the phrase "no curvature-bootstrap output needed" conflates the two links of the circle. The metric-equivalence link is genuinely broken; the curvature-input link is not, and is the open item in §9.
- **Statement (4)** is valid and does follow directly from the defect bound.

The sign conventions ($\Delta=\nabla^k\nabla_k$ with $\Delta|E|^2\le0$ at a max; $\partial_t\operatorname{Ric}=\Delta_L\operatorname{Ric}$ surviving the $-2g$ modification because $\Delta_L g=0$ and $\operatorname{div}g=0$) are consistent throughout. What remains unresolved for Prop 1 to stand unconditionally is the time-uniform curvature control on the transition annulus feeding the Gronwall constant — the same object Step 14 §7 identifies as load-bearing.