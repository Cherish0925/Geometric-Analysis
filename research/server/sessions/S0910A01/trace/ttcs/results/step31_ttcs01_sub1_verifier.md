# TTCS Independent Branch Record

```json
{
  "step_id": 31,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step31_general_p_tensor_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step31_m2_continuation_analysis.md",
    "Sessions/S0910A01/workspace/scripts/step31_general_p_verification.py",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md"
  ]
}
```

## Task

Verify two critical mathematical claims from the Step 31 derivation of the general-p tensor power inequality for the normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed 4-manifold.

**Claim 1 (Time-decay correction):** The standard parabolic Moser iteration starting from the L^{p₀} seed K_{p₀} = ∫a^{p₀-2}F^{p₀} dμ gives a UNIFORM pointwise bound ‖aF(t)‖_∞ ≤ C(S, K₀, θ) on [T/4, T], NOT the time-decaying bound ‖aF(t)‖_∞ ≤ Cβ/t claimed in earlier steps. The mechanism: the Moser output from L^{p₀} on [0,T] is ‖u‖_∞ ≤ C(VT)^{-1/p₀}(∫₀^T K_{p₀})^{1/p₀}, where V is the spatial volume. The spacetime integral ∫K₃ ≤ Cγ H₂(1+θ), and the four-dimensional critical cancellation S² = Cr⁴/V, H₂ ≤ CV(1+K₀) makes the bound independent of collapse volume V. Similarly, the defect Moser from J₆ gives ‖aE‖_∞ ≤ Cδ (uniform). The velocity V(T) = O(δθr²) → 0 as δ→0.

**Claim 2 (m=2 continuation):** In the Wang-type shifted-curvature continuation for U=a(Rm+G), the single-χ Hessian term ∫χ|∇²χ||∇²U|^p at the m=2 induction level does NOT need to be absorbed by the dissipation D_{2,p} = ∫χ²|∇³U|²|∇²U|^{p-2}. Instead, using χ≤1 and |∇²χ|≤C/r², it is bounded by Cr⁻²A₂(p)^p where A₂(p)^p = ‖∇²U‖_{L^p}^p is the UNWEIGHTED L^p norm. This enters the Gronwall RHS: A₂' + cD_{2,p} ≤ C(1+A₂^p), giving A₂(t) ≤ Ce^{Ct}(A₂(0)+Ct). No exact tensor cancellation or dissipation absorption is needed.

Check: (a) Is the Moser output truly uniform (not 1/t) given a bounded integrated coefficient? (b) Does the 4D volume cancellation work correctly? (c) Is the Gronwall treatment of the single-χ term mathematically valid? (d) Are there subtle issues with the unweighted norm A₂ including transition-region curvature?

## Output

Scientific verification memo

## (a) Parabolic Moser output: uniform on a fixed terminal slab, not \(C\beta/t\)

The time-decay correction is mathematically sound in the following precise sense.

For the curvature iteration with seed  
\[
K_{p_0}(t)=\int a^{p_0-2}F^{p_0}\,d\mu_t,\qquad p_0=3,
\]
the parabolic Moser output on a fixed cylinder of spatial volume \(V\) and time length \(T\) has the form
\[
\|aF\|_{L^\infty([T/4,T])}
\le C_{\rm Mos}\,(VT)^{-1/3}
\left(\int_0^T K_3(s)\,ds\right)^{1/3},
\]
up to the Sobolev/cutoff/potential constants produced in the iteration. The coefficient term \(S^4Y(t)\), \(Y=K_3\), enters the Moser product through its dyadic-slab control; a bounded time integral of this coefficient changes the multiplicative constant, not the seed exponent. It does not by itself generate a pointwise factor \(1/t\).

Two qualifications matter:

1. The estimate is uniform on a fixed later slab such as \([T/4,T]\). If one re-runs the estimate with \(T=t\) for every small \(t\), the usual parabolic cylinder normalization produces \(t\)-dependence. That is different from the earlier asserted \(C\beta/t\) curvature decay.

2. The Step 31 note should keep the spatial averaging factor visible. The formula
\[
\|aF(t)\|_\infty \lesssim \left(\frac1t\int_0^tK_3\right)^{1/3}
\]
omits the spatial-volume/Sobolev normalization. The script’s form
\[
\|aF\|_\infty^3\lesssim \frac1{VT}\int_0^T K_3
\]
is the cleaner version for the volume calculation.

Thus the earlier \(C\beta/t\) estimate is not supported by the Moser mechanism described here. The supported conclusion is a fixed-slab bound depending on \(S,K_0,\theta\), with \(T=\theta r^2\).

## (b) Four-dimensional volume cancellation

Using the supplied inputs
\[
\int_0^T K_3 \le C\gamma H_2(1+\theta),
\qquad
\gamma=S^2H_2^{1/2},
\]
and
\[
H_2\le C V(1+K_0),
\qquad
S^2\simeq \frac{r^4}{V},
\qquad
T=\theta r^2,
\]
one obtains
\[
\|aF\|_\infty^3
\le
C\frac{\gamma H_2}{VT}
=
C\frac{S^2H_2^{3/2}}{VT}.
\]
Then
\[
\frac{S^2H_2^{3/2}}{VT}
\le
C\frac{S^2V^{3/2}(1+K_0)^{3/2}}{VT}
=
C\frac{S^2V^{1/2}}{T}(1+K_0)^{3/2}.
\]
Since \(S^2=r^4/V\), equivalently \(S=r^2/V^{1/2}\), this becomes
\[
\frac{S^2V^{1/2}}{T}
=
\frac{Sr^2}{T}
=
\frac{S}{\theta}.
\]
Therefore
\[
\boxed{
\|aF\|_\infty
\le
C\,S^{1/3}\theta^{-1/3}(1+K_0)^{1/2}.
}
\]

So the explicit volume \(V\) cancels correctly after rewriting it through the four-dimensional Sobolev factor. The result is volume-free only in the sense that \(V\) no longer appears separately; the bound still depends on \(S\). If \(S\) is allowed to grow as \(V\) shrinks, the estimate records that through the factor \(S^{1/3}\).

For the defect iteration, the same averaging mechanism is consistent. If
\[
J_6(0)\le \delta^6 V
\]
and persistence gives \(J_6(t)\le C\delta^6V\) on the terminal slab, then
\[
\|aE\|_\infty^6
\le
C(VT)^{-1}\int_{T/4}^T J_6(s)\,ds
\le
C\delta^6.
\]
Hence
\[
\boxed{\|aE\|_\infty\le C\delta}
\]
on the fixed terminal slab. Consequently
\[
\int_0^T\|aE\|_\infty\,dt
\le
C\delta T
=
C\delta\theta r^2
\to0
\qquad(\delta\to0)
\]
for fixed \(\theta,r\).

## (c) The \(m=2\) single-\(\chi\) Hessian term

Let
\[
V_2=\nabla^2U,
\qquad
A_2(p)^p=\int_M |\nabla^2U|^p\,d\mu.
\]
The term in question is
\[
I=\int_M \chi |\nabla^2\chi|\,|\nabla^2U|^p\,d\mu.
\]
If one has a uniform bound
\[
|\nabla^2\chi|_{g(t)}\le C r^{-2}
\]
on the time interval under consideration, then
\[
|I|
\le
\|\nabla^2\chi\|_\infty
\int_M |\nabla^2U|^p\,d\mu
\le
Cr^{-2}A_2(p)^p.
\]
This is a lower-order Gronwall term. It does not have to be absorbed into
\[
D_{2,p}
=
\int_M\chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}\,d\mu.
\]
Trying to pay for \(I\) using \(D_{2,p}\) would introduce inverse powers of \(\chi\), because \(D_{2,p}\) carries \(\chi^2\) while \(I\) has only one \(\chi\). The unweighted \(L^p\) treatment avoids that problem.

The resulting energy inequality should be written for the \(p\)-th power:
\[
\frac{d}{dt}A_2(p)^p+cD_{2,p}
\le
C\bigl(1+A_2(p)^p\bigr),
\]
and Gronwall gives
\[
A_2(p)^p(t)
\le
e^{Ct}\bigl(A_2(p)^p(0)+Ct\bigr).
\]
No tensor cancellation is needed for this particular term.

One important technical point: the bound \(|\nabla^2\chi|_{g(t)}\le Cr^{-2}\) is not automatic merely from bilipschitz metric comparison, because the Hessian uses the evolving connection. In the Wang-type continuation framework, this coefficient must either be an established cutoff estimate at that stage or be supplied by the coupled \((\nabla U,\nabla^2\chi)\) part of the induction. Once that coefficient is available, the displayed Gronwall treatment is valid.

## (d) Unweighted \(A_2\) and the transition region

Using the unweighted norm
\[
A_2(p)^p=\int_M|\nabla^2U|^p
\]
is mathematically consistent with the shifted-curvature continuation scheme, because the evolved quantity is
\[
U=a(\operatorname{Rm}+G)=\chi^2(\operatorname{Rm}+G),
\]
not \(\operatorname{Rm}\) itself. On the transition region, \(\nabla^2U\) contains cutoff-derivative terms coupled to curvature, but the induction estimates \(U\) directly. It does not require separate unweighted control of \(\nabla^2\operatorname{Rm}\) there.

The necessary input is finite initial \(A_2(p)\), which holds for a smooth initial metric on a closed manifold. The continuation argument then propagates \(A_2(p)\) by Gronwall. This is compatible with the degenerate diffusion, since the dissipation is weighted while the lower-order energy quantity is unweighted.

So the single-\(\chi\) term is harmless as a Gronwall contribution, provided the evolving Hessian of \(\chi\) has already been controlled in the induction.