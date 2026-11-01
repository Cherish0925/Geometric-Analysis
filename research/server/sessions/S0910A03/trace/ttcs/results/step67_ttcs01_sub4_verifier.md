# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step67_corrections_and_analytic_neck_reopening.md",
    "Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md",
    "Sessions/S0910A03/workspace/notes/step63_graph_manifold_counterexample_analysis.md"
  ]
}
```

## Task

Verify the new Step 67 local curved-neck result in full mathematical detail. Check sign conventions, Koiso/Theorem 2.1 hypotheses, existence of an analytic constant-scalar-curvature -6 metric on T^3, the W=0 constraint for a four-dimensional Ric=-3g extension, the formula for g''(0), time-reflection symmetry, and H'(0)=3 under the opposite S convention. Identify any hidden issue that would invalidate the conclusion that an exact local negative-Einstein germ reverses mean curvature through a curved totally geodesic T^3. Also distinguish exactly what this refutes and what remains global. Ground every conclusion in the supplied source and note; do not assume a global extension.

## Output

## Verifier memo — Step 67 local curved-neck Einstein germ

**Overall finding.** The central Step 67 statement is correct and is properly grounded in the supplied source (Ammann–Moroianu–Moroianu, Theorem 2.1 / Koiso, and Corollaries 2.2–2.3). Every arithmetic and sign step I could reconstruct checks out, and the mean-curvature reversal at $H(0)=0$, $H'(0)=3$ is confirmed by two independent computations. The note's careful separation of the local exact result from the unresolved global continuation is accurate. Details below, with the cross-checks that make the conclusion reliable and the substance that remains open.

### 1. Constraint reduction ($n=3$, $\lambda=-3$, $W_0=0$)

Using AMM (2.9)–(2.10) exactly as reproduced in the source:
- $d\operatorname{tr}W+\delta^gW=0$ is $0=0$ for $W=0$. ✓
- $\operatorname{Scal}^g+\operatorname{tr}(W^2)-\operatorname{tr}^2(W)=(n-1)\lambda$ becomes $\operatorname{Scal}^g=2\lambda=-6$. ✓

The single value $\lambda=-3$ is forced by (2.10) once $\operatorname{Scal}=-6$ and $W=0$, and (2.9) holds for that same $\lambda$. This is exactly the $\alpha=0$ (totally geodesic) instance of Corollary 2.2, whose stated formula $\alpha=\sqrt{\operatorname{Scal}/(n(n-1))-\lambda/n}$ gives $\alpha=0\Leftrightarrow\operatorname{Scal}=(n-1)\lambda=-6$. The reduction is correct.

### 2. Existence of an analytic constant-scalar-curvature $-6$ metric on $T^3$

This holds, and for $n=3$ the argument is clean. $T^3$ admits conformal classes whose Yamabe constant is below zero: take any analytic metric $g_1$ on $T^3$ with $\int\operatorname{Scal}_{g_1}\,dV<0$ (an analytic, e.g. trigonometric, perturbation of the flat metric achieves this). The constant test function in the conformal-Laplacian Rayleigh quotient then gives lowest eigenvalue $<0$, i.e. $Y(T^3,[g_1])<0$. The Yamabe minimizer $g=u^{4/(n-2)}g_1=u^{4}g_1$ solves $L_{g_1}u=Y\,u^{5}$ — a semilinear elliptic equation with **analytic coefficients and polynomial ($u^5$) nonlinearity** (the exponent $4/(n-2)=4$ is an even integer precisely at $n=3$), so Morrey analytic regularity makes $u>0$ analytic; hence $g$ is analytic with constant $\operatorname{Scal}=Y<0$. A constant rescaling $\tilde g=\mu g$, $\mu=|Y|/6$, gives $\operatorname{Scal}_{\tilde g}=\mu^{-1}Y=-6$ and preserves analyticity. This is exactly the mechanism of Corollaries 2.2–2.3 in the source, so the note's appeal to those corollaries is justified. Note the resulting metric is generically inhomogeneous, which correctly places it in the "curved, tangentially inhomogeneous slice" class of Section 1.3 (i.e. genuinely outside the flat-slice theorem, and with $\operatorname{Ric}^{g_t}$ actively contributing to (E)).

### 3. Koiso Theorem 2.1 hypotheses and the full torus slice

The hypotheses (analytic $(M,g)$, analytic symmetric $W$ satisfying (2.9)–(2.10)) are met: $g_0$ analytic (Section 2), $W_0=0$ trivially analytic. Theorem 2.1 yields a unique analytic Einstein germ $g^Z=dt^2+g_t$, $g_0=g$, $\operatorname{Ric}^Z=\lambda g^Z=-3g^Z$, with $t=0$-Weingarten $=W_0=0$, hence $T^3\times\{0\}$ totally geodesic. Because $T^3$ is compact, the pointwise radii $\varepsilon_x$ from the Cauchy–Kowalevskaya step can be taken uniform, so the germ lives on a genuine $(-\varepsilon,\varepsilon)\times T^3$ — the reversal really occurs across the whole torus, not merely one coordinate patch. $g_t$ stays positive-definite for small $|t|$ by continuity. All correct.

### 4. Second normal derivative $\ddot g_0$ and non-degeneracy

Setting $\dot g_0=-2W_0=0$ in the tangential equation (E) at $t=0$ collapses the two $\dot g$-quadratic terms:
$$\ddot g_0=2\operatorname{Ric}_{g_0}-2\lambda g_0=2\operatorname{Ric}_{g_0}+6g_0,$$
matching (E0). This is nonzero: $\operatorname{tr}_{g_0}\ddot g_0=2\operatorname{Scal}_{g_0}+6\cdot3=2(-6)+18=6\neq0$. So $\ddot g_0\not\equiv0$ independent of anisotropy — the germ is genuinely $t$-dependent and is not the static product $dt^2+g_0$ (which cannot be Einstein since it has $\operatorname{Ric}(\nu,\nu)=0\neq-3$). The note's phrasing "nonzero unless $g_0$ were three-dimensional Einstein (impossible on $T^3$)" is right; the trace already settles it.

Cross-check with AMM (2.3): $\operatorname{Ric}^Z(\nu,\nu)=\operatorname{tr}(W_0^2)-\tfrac12\operatorname{tr}_{g_0}\ddot g_0=0-\tfrac12(6)=-3=\lambda$. ✓

### 5. Time-reflection symmetry

Equation (E) is second order in $t$ with right-hand side depending on $g_t$ (even under $t\mapsto-t$) and on $\dot g_t$ only through the two quadratic terms (even in $\dot g_t$). The Cauchy data $g_0$, $\dot g_0=0$ are preserved under $t\mapsto-t$. Hence $g_{-t}$ solves (E) with identical data, and analytic uniqueness (Cauchy–Kowalevskaya) gives $g_t=g_{-t}$. Correct. Consequently $\dot g_t$ is odd and $H(t)=\tfrac12\operatorname{tr}_{g_t}\dot g_t$ is odd in $t$, which by itself already shows a sign change through $t=0$.

### 6. Mean-curvature reversal $H(0)=0$, $H'(0)=3$ — verified twice

With the note's convention $S=-W=\nabla\nu$ (positive $H$ = expanding volume), the Raychaudhuri/Riccati trace identity is $H'=-\operatorname{Ric}^Z(\nu,\nu)-|S|^2$. Since $\operatorname{Ric}^Z=-3g^Z$ and $g^Z(\nu,\nu)=1$, $\operatorname{Ric}^Z(\nu,\nu)=-3$, giving $H'=3-|S|^2$. At $t=0$, $S_0=0$, so $H(0)=0$ and $H'(0)=3>0$.

Independent volume-element computation: $H=\tfrac12\operatorname{tr}_{g_t}\dot g_t$, so
$$H'(0)=\tfrac12\big[\dot g^{ij}\dot g_{ij}+g^{ij}\ddot g_{ij}\big]_{t=0}=\tfrac12\operatorname{tr}_{g_0}\ddot g_0=\tfrac12(6)=3,$$
using $\dot g_0=0$ and $\operatorname{tr}_{g_0}\ddot g_0=6$ from Section 4. Both routes agree. The convention bookkeeping is internally consistent: $\tfrac12\operatorname{tr}_g\dot g=-\operatorname{tr}W=\operatorname{tr}S=H$, so the volume computation is measuring the same $H$ as the Riccati identity. The reversal (sign change of $H$ through a totally geodesic curved $T^3$) is a genuine geometric fact, invariant under $\nu\mapsto-\nu$ (which only relabels which side is contracting).

### 7. Consistency cross-checks that raise confidence

- Contracted Gauss at $t=0$: $\operatorname{Scal}^Z-2\operatorname{Ric}^Z(\nu,\nu)=-12-2(-3)=-6$ equals $\operatorname{Scal}^{T^3}-H^2+|S|^2=-6-0+0=-6$. ✓ The single ingredient distinguishing this from the Step 63 flat-slice computation is $\operatorname{Scal}^{T^3}=-6\neq0$.
- Exact hyperbolic cusp $dr^2+e^{-2r}g_{\rm flat}$: $H=-3$ constant, $|S|^2=3$, $\operatorname{Ric}(\nu,\nu)=-3$ — satisfies $H'=-\operatorname{Ric}(\nu,\nu)-|S|^2=0$ and $H^2=9\ge9-6\delta$. So the cusp meets the flat-slice inequality with no reversal, consistent with Section 1.3.

### 8. What is genuinely established vs. what is not contradicted

The germ does **not** contradict the Step 63 flat-slice theorem. That theorem assumes intrinsically flat slices ($R_M=0$) and derives $H^2\ge9-6\delta$; the germ has $R_M=\operatorname{Scal}_{g_0}=-6$, so the Cauchy–Schwarz step ($2H^2/3\ge6-4\delta$, which used $R_M=0$) simply does not apply. What Step 67 correctly refutes is any *local* no-reversal statement resting only on: $T^3$ topology, self-adjointness of the shape operator, the sign of scalar curvature, or a small ambient Einstein defect. Here the defect is exactly zero, the slice is a torus, the shape operator is self-adjoint, and reversal still occurs — because the slice is intrinsically curved. This pinpoints the flat-slice hypothesis as the load-bearing ingredient in earlier no-neck reasoning, exactly as Section 1.3 states.

### 9. The global substance that remains open (and a sharpening)

The germ is local: it exists on $(-\varepsilon,\varepsilon)\times T^3$ with $\varepsilon$ possibly small, and analytic uniqueness makes it rigid. The Riemannian Einstein evolution (E) is elliptic-type, so smooth/generic continuation is not available (consistent with AMM Prop. 2.5 and Example 2.7). The note correctly identifies the open problem as global: continue the germ far enough to match two flat-cusp ends of opposite induced mean-curvature sign, exactly or with uniformly small $\|\operatorname{Ric}+3g\|_{L^\infty}$, controlling both the mixed constraint $dH+\delta W$ and the Hamiltonian constraint, not only the tangential equation.

One structural point worth stating explicitly, because it constrains any global program: an **exact** global match is impossible. If the exact germ ($\operatorname{Ric}=-3g$) and exact cusps ($\operatorname{Ric}=-3g$) could be smoothly assembled into a closed graph 4-manifold, that manifold would carry an exact Einstein metric — excluded by Di Cerbo (Step 63, Theorem 12). Therefore any global construction must carry nonzero defect somewhere, and the entire question is whether that defect can be driven to zero (a would-be counterexample) or is bounded below uniformly (a pinching-gap theorem). The germ gives zero *local* defect at the reversal point but says nothing about the two matching layers; as the note observes, shrinking those layers controls integral norms but not the sup norm the target requires. The next tests it lists (linearize (E) about the germ and about the cusp; use $g_t=g_{-t}$ to ask whether analytic $g_0$ can generate asymptotically flat-cusp ends; test integrated monotonicities against both the exact germ and exact cusps) are the right objects, and any candidate monotone quantity that would forbid the germ is thereby known to be wrong.

### 10. Mapping to Yau 26 — a point to keep precise

The germ addresses only the branch with Ricci near $-3g$. Disproving Yau 26 in a fixed dimension requires defeating **every** admissible pinching window $[c_n,C_n]$, including windows centered above zero and across zero, since $c_n,C_n$ are chosen by the proposer. A completed graph-manifold construction with $\|\operatorname{Ric}+3g\|\to0$ would defeat only windows overlapping the sub-zero range near $-3$; it leaves windows in the positive range untouched. The note's requirement of "both normalized signs in the same dimension on all-Einstein-excluding manifolds" captures this, and Step 63 Section 5.3 correctly records that the positive branch has no candidate yet. So the germ, even fully globalized, would be necessary but not sufficient for a dimension-4 disproof.

### 11. Auxiliary corrections in Section 1 — all valid

For completeness I checked the retractions: the 3D identity $K_{ij}=\tfrac12(\rho_i+\rho_j-\rho_k)$ with $(-2,-2,-10)\Rightarrow K_{12}=3>0$ is correct (Preissmann needs sectional curvature below zero, not Ricci below zero); the unit-volume flat $T^4$ has $\int|\operatorname{Ric}|^2=0<1/3$, refuting the earlier Chern–Weil inequality; and $\Sigma_g\times\Sigma_h$ ($g,h\ge2$) has $\chi=4(g-1)(h-1)>0$, $\tau=0$, meets Hitchin–Thorpe, and is Einstein as a product of equally normalized hyperbolic factors, so it is not in the class $2\chi\le3|\tau|$. These corrections are sound.

**Net.** No error invalidates the Step 67 local germ. The one item I would not leave implicit is that exact global assembly is barred by Di Cerbo, so the germ's value is precisely to show the reversal obstruction is not local and to redirect any resolution toward the two-ended matching problem with controlled sup-norm defect and controlled constraints.