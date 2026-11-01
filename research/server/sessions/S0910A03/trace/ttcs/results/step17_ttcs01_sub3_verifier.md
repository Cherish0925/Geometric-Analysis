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

## Scientific verification memo

### 1. Lichnerowicz signs and the moving-norm term

Use the convention
\[
\Delta f=g^{ij}\nabla_i\nabla_j f,
\qquad
(\Delta_LH)_{ij}
=
\Delta H_{ij}
+2R_{ikjl}H_{kl}
-\Ric_i{}^kH_{kj}
-\Ric_j{}^kH_{ki}.
\]
Then \(\Delta f\le0\) at a spatial maximum, and
\[
2\langle E,\Delta_LE\rangle
=
\Delta |E|^2-2|\nabla E|^2
+4\Rm(E,E)-4\Ric(E,E).
\]
Thus the signs used in Step 17 are consistent with this convention. An opposite convention for \(\Delta_L\) requires changing the tensor evolution simultaneously.

The algebra
\[
\Ric(E,E)=\tr(E^3)-|E|^2
\]
is correct. Consequently, inside \(2\langle E,\partial_tE\rangle\),
\[
-4a\Ric(E,E)-4a|E|^2=-4a\tr(E^3).
\]

There is, however, an additional term because \(|E|^2\) is computed using the evolving metric. Since
\[
\partial_tg=-2aE,
\qquad
\partial_tg^{ij}=2aE^{ij},
\]
differentiating both inverse metrics in
\[
|E|^2=g^{ik}g^{jl}E_{ij}E_{kl}
\]
gives
\[
\left.\partial_t|E|^2\right|_{\text{inverse metrics}}
=4a\tr(E^3).
\]
This cancels the residual \(-4a\tr(E^3)\). Therefore the full identity is
\[
\boxed{
(\partial_t-a\Delta)|E|^2
=
-2a|\nabla E|^2
+4a\Rm(E,E)
+2\langle E,\mathcal C_a(E)\rangle .
}
\]
This agrees with the exact identity already recorded in Step 14. The Python script verifies the partial algebraic identity but omits differentiation of the inverse metrics; its reported residual cubic is therefore not present in the complete scalar evolution.

The eigenvalue estimate itself is correct:
\[
|\tr(E^3)|
\le \sum_i|\lambda_i|^3
\le\left(\sum_i\lambda_i^2\right)^{3/2}
=|E|^3.
\]
Hence, under \(|E|\le2\delta_0\),
\[
4a|\tr(E^3)|\le8a\delta_0|E|^2.
\]
If \(\delta=\|E(t)\|_\infty\) denotes the current norm, the sharper coefficient is \(4a\delta\). Neither estimate is needed after the moving-norm term is included.

### 2. Pointwise treatment of the cutoff terms

From the displayed formula for \(\mathcal C_a(E)\), using in dimension four
\[
|\tau|\le2|E|,
\qquad
|\nabla\tau|\le2|\nabla E|,
\]
one obtains, for every \(\varepsilon>0\),
\[
|2\langle E,\mathcal C_a(E)\rangle|
\le
\varepsilon a|\nabla E|^2
+C_\varepsilon
\left(
|\nabla^2a|+\frac{|\nabla a|^2}{a}
\right)|E|^2
\]
where \(a>0\). For \(a=\chi^2\),
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,
\qquad
\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi.
\]
After absorbing the gradient term,
\[
\boxed{
(\partial_t-a\Delta)|E|^2
\le
C\left(
a|\Rm|
+|\nabla^2a|
+\frac{|\nabla a|^2}{a}
\right)|E|^2 .
}
\]
If the evolved cutoff derivatives satisfy
\[
|\nabla\chi|_{g(t)}\le Cr^{-1},
\qquad
|\nabla^2\chi|_{g(t)}\le Cr^{-2},
\]
this reduces to
\[
(\partial_t-a\Delta)|E|^2
\le C\bigl(a|\Rm|+r^{-2}\bigr)|E|^2.
\]
Thus there is no \(\delta\)-dependent cubic term at all. There remains a full-curvature potential \(a|\Rm|\), whose Weyl part is not controlled by the Ricci defect.

A further analytic point is that the cutoff Hessian here is \(\nabla^2_{g(t)}a\). The initial estimate \(|\nabla^2_{g_0}\chi|\le Cr^{-2}\) is not preserved merely by bilinear metric equivalence, since
\[
\nabla^2_ga=\partial^2a-\Gamma(g)*\partial a
\]
depends on first spatial derivatives of \(g\).

### 3. Degenerate maximum principle

Assume a smooth solution exists on the time interval and define
\[
U(t)=\max_M |E(\cdot,t)|^2.
\]
Uniform parabolicity is unnecessary for the elementary maximum argument. At a maximizer,
\[
\Delta|E|^2\le0,
\]
and \(a\ge0\), so the upper Dini derivative satisfies
\[
D^+U(t)
\le
C\left[
\|a\Rm(t)\|_\infty
+\left\||\nabla^2a|+\frac{|\nabla a|^2}{a}\right\|_\infty
\right]U(t).
\]
The quotient has the bounded extension \(4|\nabla\chi|^2\) away from and up to \(\chi=0\).

The statement that \(E\) is frozen wherever \(a=0\) needs the cutoff structure. For a standard smooth cutoff \(0\le\chi\le1\), every zero of \(\chi\) has \(d\chi=0\), hence
\[
a=da=\nabla^2a=0
\]
there, and the displayed tensor evolution gives \(\partial_tE=0\). For an arbitrary signed \(\chi\), \(\nabla^2(\chi^2)=2\,d\chi\otimes d\chi\) may survive at a zero, so pointwise stationarity of \(E\) need not hold. The scalar maximum argument remains valid in either case.

### 4. What Gronwall actually yields

Let
\[
B(t)=C\left[
\|a\Rm(t)\|_\infty
+\left\||\nabla^2a|+\frac{|\nabla a|^2}{a}\right\|_\infty
\right].
\]
Then
\[
\|E(t)\|_\infty^2
\le
\|E(0)\|_\infty^2
\exp\!\left(\int_0^tB(s)\,ds\right).
\]
Therefore, if one has the spacetime estimates
\[
\|a\Rm(t)\|_\infty\le K,
\qquad
|\nabla^2a|+\frac{|\nabla a|^2}{a}\le Cr^{-2},
\]
then
\[
t\le
\frac{r^2\log2}{C(Kr^2+1)}
\]
indeed implies
\[
\|E(t)\|_\infty\le\sqrt2\,\|E(0)\|_\infty.
\]

The replacement \(K=K_0=\|\Rm(g_0)\|_{\infty,\operatorname{supp}\chi}\) is not supplied by the defect maximum principle. Small bilinear drift of \(g(t)\) does not preserve curvature:
\[
\Rm(g)\sim g^{-1}\partial^2g+g^{-2}(\partial g)^2.
\]
It also does not preserve \(\nabla^2_{g(t)}a\). A spacetime curvature estimate and control of the evolved cutoff Hessian are therefore required to obtain the stated quantitative time solely from \(K_0\).

This matters directly for the good set in Section 4: maximal-function control of normalized \(L^2\) curvature on every ball does not give a uniform pointwise value of \(K_0\) on the cutoff support.

### 5. Metric equivalence

Once the pointwise defect estimate is available, the metric comparison is correct. For fixed \(v\in T_xM\),
\[
\left|\frac{d}{dt}\log g_t(v,v)\right|
=
2a\frac{|E(v,v)|}{g_t(v,v)}
\le2\|E(t)\|_\infty.
\]
Hence \(\|E(t)\|_\infty\le\sqrt2\,\delta_0\) gives
\[
e^{-2\sqrt2\delta_0t}g_0
\le g(t)\le
e^{2\sqrt2\delta_0t}g_0.
\]

Thus the algebraic normalization term is better than Step 17 states: its cubic contribution cancels completely. The metric-equivalence implication is also valid. The proposed curvature-independent closure does not follow from the scalar equation, because its Gronwall coefficient still contains the spacetime quantities \(a|\Rm|\) and \(|\nabla^2_{g(t)}a|\).