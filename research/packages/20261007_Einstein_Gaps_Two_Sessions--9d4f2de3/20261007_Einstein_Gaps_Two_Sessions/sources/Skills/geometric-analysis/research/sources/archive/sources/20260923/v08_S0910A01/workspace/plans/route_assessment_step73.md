# Route assessment: Step 73

Session: S0910A01.  Agent2 / Constructor.  Step 73, Execute.

## What Step 73 produced

Three structural results for the graph-neck construction, all verified by
TTCS and corrected in response to five TTCS-identified errors.

### Established results

1. **Preissmann obstruction (Proposition 2.1):** Every metric $h$ on $T^3$
   has $\max |\operatorname{Ric}_h + 2h|_{\rm op} > 2/3$.  The isotropic
   tanh collar therefore has center defect $> 2/3$, independently of fiber
   metric and collar length.  (Corrected: flat torus theorem replaces the
   invalid fixed-triple argument at $c = 2/3$.)

2. **Koiso center formulas (3.3):** At a totally geodesic center, $S'(0) =
   \operatorname{Ric}_h^\sharp + 3I$ with $R_h = -6$. Isotropic
   impossible on $T^3$.  Formulas $a_{tt} = uv$, $b_{tt} = v^2 + v'$,
   $c_{tt} = u^2 + u'$ verified algebraically.

3. **Forced anisotropy decay:** The correct equation for the anisotropy
   difference is $\delta_{ij}' + H\delta_{ij} = r_i(h_t) - r_j(h_t)$,
   NOT the unforced $\delta_{ij}' + H\delta_{ij} = 0$.  The fiber Ricci
   forcing gives decay rate $\sim e^{-2t}$ (confirmed: fitted rate 2.002),
   slower than the unforced $e^{-3t}$ but still exponential.

### Corrections from TTCS

- **Rate:** Unforced ODE gives $\operatorname{sech}(3t)$, not
  $\operatorname{sech}(\sqrt{3}t)$.  The $\sqrt{3}$ was from the
  two-direction $a=0$ gauge.
- **Forcing:** The simplified ODE cannot produce Koiso anisotropy because
  $\delta_{ij}(0) = 0$.  The fiber Ricci creates the anisotropy.
- **$a = 0$ gauge:** Full PDE gives $b_tc_t + b_\theta c_\theta = 0$,
  NOT $b_tc_t = 0$.  The Koiso solution immediately leaves $a \equiv 0$.
- **Higher modes:** Not justified by principal part alone.
- **Preissmann boundary:** Fixed triple $(-4/3,-4/3,-8/3)$ does not
  follow from the bound; the flat torus theorem is the correct tool.

### Fiber periodicity gap

The $T^2$-invariant diagonal ansatz with $v = B\sin\theta$ produces
periodic solutions of the Riccati constraint with $R = -6$ pointwise,
but these have **nonzero mean** ($\int u \neq 0$), so $b_0(\theta)$ is
not periodic on $S^1$.  The solution branch terminates at $B \approx 2.25$
with mean $\approx 0.88 > 0$.  Zero-mean periodic fibers on $T^3$ are
not found in this form.

The Kazdan–Warner theorem guarantees metrics with $R = -6$ on $T^3$ exist,
but not in the restricted diagonal $T^2$-invariant form.

## A02 development

A02 (#503) has reallocated toward proving the positive branch $P_n^+$
all-dimensionally, using the manuscript's dimension-general annular flux
proposition with coefficient $-(d+2)/2$.  The key observation: positive-branch
counterexamples would need PSC-compatible no-Einstein manifolds, but known
no-Einstein examples in dimension 4 are monopole/BF-driven (non-PSC), and
no concrete closed no-Einstein manifold is known in $n \geq 5$.  This is a
complementary route that could resolve the full Yau 26 alongside the negative
IL theorem.

## Status of the graph route

**Positive signals:**
- Preissmann establishes a sharp threshold
- Koiso center eliminates the center defect
- Forced anisotropy still decays (rate $e^{-2t}$)

**Obstacles:**
- Zero-mean periodic fibers not found in the $T^2$-invariant form
- Gauge and BVP structure need a more general ansatz
- The construction remains far from a concrete near-Einstein metric

**Assessment:** The graph route needs either (a) a proof that zero-mean
periodic $R = -6$ fibers exist in a computationally tractable form, or
(b) a different symmetry reduction (Sol-type instead of $T^3$), or
(c) abandonment in favor of the positive branch route opened by A02.

## Next work

The highest-value next actions, in order:

1. **Absorb A02's positive-branch structure** — this is a potentially
   dimension-general proof route, more aligned with the full Yau 26 goal
   than the restricted graph-neck or IL construction.

2. **For the graph route:** attempt a Fourier/Galerkin approach to the
   zero-mean constraint, or compute on a Sol-geometry manifold where the
   nonzero mean is compatible with the monodromy.

3. **For the negative IL route:** the restricted theorem assembly is
   stable after Step 71 repairs; further work should target publication-level
   expansion of specific interfaces rather than repeated reconstruction.

## Files

- `workspace/notes/step73_preissmann_koiso_anisotropy.md` (corrected note)
- `workspace/data/step73_preissmann_koiso_verify.json` (22/22)
- `workspace/data/step73_koiso_center_analysis.json` (fiber + ODE data)
- `workspace/data/step73_ttcs_corrections.json` (forced decay, rate fix)
- `workspace/data/step73_mean_u_track.json` (mean(u) vs B tracking)
- `trace/ttcs/results/step73_ttcs01_verifier1_integration.md` (TTCS)
