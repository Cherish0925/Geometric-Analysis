# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 31,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step31_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step31_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify two critical mathematical claims from the Step 31 derivation of the general-p tensor power inequality for the normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed 4-manifold.

**Claim 1 (Time-decay correction):** The standard parabolic Moser iteration starting from the L^{p₀} seed K_{p₀} = ∫a^{p₀-2}F^{p₀} dμ gives a UNIFORM pointwise bound ‖aF(t)‖_∞ ≤ C(S, K₀, θ) on [T/4, T], NOT the time-decaying bound ‖aF(t)‖_∞ ≤ Cβ/t claimed in earlier steps. The mechanism: the Moser output from L^{p₀} on [0,T] is ‖u‖_∞ ≤ C(VT)^{-1/p₀}(∫₀^T K_{p₀})^{1/p₀}, where V is the spatial volume. The spacetime integral ∫K₃ ≤ Cγ H₂(1+θ), and the four-dimensional critical cancellation S² = Cr⁴/V, H₂ ≤ CV(1+K₀) makes the bound independent of collapse volume V. Similarly, the defect Moser from J₆ gives ‖aE‖_∞ ≤ Cδ (uniform). The velocity V(T) = O(δθr²) → 0 as δ→0.

**Claim 2 (m=2 continuation):** In the Wang-type shifted-curvature continuation for U=a(Rm+G), the single-χ Hessian term ∫χ|∇²χ||∇²U|^p at the m=2 induction level does NOT need to be absorbed by the dissipation D_{2,p} = ∫χ²|∇³U|²|∇²U|^{p-2}. Instead, using χ≤1 and |∇²χ|≤C/r², it is bounded by Cr⁻²A₂(p)^p where A₂(p)^p = ‖∇²U‖_{L^p}^p is the UNWEIGHTED L^p norm. This enters the Gronwall RHS: A₂' + cD_{2,p} ≤ C(1+A₂^p), giving A₂(t) ≤ Ce^{Ct}(A₂(0)+Ct). No exact tensor cancellation or dissipation absorption is needed.

Check: (a) Is the Moser output truly uniform (not 1/t) given a bounded integrated coefficient? (b) Does the 4D volume cancellation work correctly? (c) Is the Gronwall treatment of the single-χ term mathematically valid? (d) Are there subtle issues with the unweighted norm A₂ including transition-region curvature?

## Integrated Scientific Memo

## Verification memo for Step 31 claims

### Executive conclusion

**Claim 1 is essentially correct only after two clarifications/corrections.**

1. The earlier bound  
\[
\|aF(t)\|_\infty\le C\beta/t
\]
is **not produced** by the stated Moser iteration. The singular coefficient \(S^4K_3(t)\sim 1/t\), when used as a time-dependent potential in the iteration, contributes through an **integrated Gronwall/Moser constant**, not as a pointwise \(1/t\) decay factor.

2. However the Moser output is not “uniform” in an absolute scale-free sense. On a fixed terminal slab \([T/4,T]\), it is uniform in \(t\), with dependence on \(T=\theta r^2\), the Sobolev constant, and the initial energy scale. The correct seed normalization carries the parabolic averaging factor, schematically
\[
\|aF\|_{L^\infty([T/4,T])}^{p_0}
\lesssim
\frac{1}{VT}\int_0^T K_{p_0}(s)\,ds
\]
up to the Moser constants. Thus for \(p_0=3\),
\[
\|aF\|_\infty^3
\lesssim
\frac{1}{VT}\int_0^T K_3(s)\,ds.
\]
The note’s formula in places without the spatial factor \(V^{-1}\), and especially the step
\[
\frac1t\int_0^t K_3 \lesssim \gamma H_2,
\]
is not justified from the supplied spacetime bound.

3. The advertised four-dimensional cancellation works only in the corrected \((VT)^{-1}\) form and leaves explicit Sobolev dependence. With
\[
\int_0^T K_3\le C\gamma H_2(1+\theta),\qquad
\gamma=S^2H_2^{1/2},\qquad
H_2\le C V(1+K_0),\qquad
S^2\simeq r^4/V,\qquad
T=\theta r^2,
\]
one gets
\[
\|aF\|_\infty^3
\lesssim
\frac{S^2H_2^{3/2}}{VT}
\lesssim
\frac{S(1+K_0)^{3/2}}{\theta},
\]
hence
\[
\boxed{
\|aF\|_\infty
\lesssim
S^{1/3}\theta^{-1/3}(1+K_0)^{1/2}
}
\]
on the fixed terminal slab. The explicit collapse volume \(V\) cancels after using the four-dimensional Sobolev relation, but the estimate still depends on \(S\). If \(S\to\infty\) under collapse, this bound deteriorates.

4. The analogous defect conclusion is consistent: if \(J_6\) persists at size \(\lesssim \delta^6V\) on a fixed terminal slab, then
\[
\|aE\|_\infty^6
\lesssim
\frac1{VT}\int_{T/4}^T J_6
\lesssim
\delta^6,
\]
so
\[
\boxed{\|aE\|_\infty\lesssim \delta}
\]
on \([T/4,T]\), with constants depending on the fixed slab parameters and curvature-potential bound. Consequently
\[
\int_0^T\|aE\|_\infty\,dt
\lesssim
\delta T
=
\delta\theta r^2
\to0
\]
for fixed \(\theta,r\), once the bound is available on the needed subintervals or by restarting/covering.

**Claim 2 is correct for the specific single-\(\chi\) Hessian term, with one important induction qualification.** The term
\[
\int \chi|\nabla^2\chi|\,|\nabla^2U|^p
\]
does not need to be absorbed into
\[
D_{2,p}=\int \chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}.
\]
Instead, provided \(|\nabla^2\chi|_{g(t)}\) is already controlled at that induction level,
\[
\int \chi|\nabla^2\chi|\,|\nabla^2U|^p
\le
\|\nabla^2\chi\|_\infty A_2(p)^p
\lesssim
r^{-2}A_2(p)^p.
\]
It is a lower-order Gronwall contribution:
\[
\frac d{dt}A_2(p)^p+cD_{2,p}
\le
C\bigl(1+A_2(p)^p\bigr),
\]
so
\[
A_2(p)^p(t)
\le
e^{Ct}\bigl(A_2(p)^p(0)+Ct\bigr).
\]
No exact tensor cancellation is needed. But this verifies only the diagonal \((0,2,2)\) term; the more delicate \(\Gamma_1=\chi\nabla^{m+2}\chi*U\) family still relies on the Wang/Proposition-4.14 integration-by-parts grouping and current-order cutoff/curvature coupling.

---

## Details for the four requested checks

### (a) Is the Moser output truly uniform, not \(1/t\), given a bounded integrated coefficient?

Yes in the precise fixed-slab sense.

The general-\(p\) inequality in the Step 31 note has the form
\[
K_p' + c p^2D_p
\le
C\bigl(p^3S^4Y(t)+p^2r^{-2}+p\bigr)K_p,
\qquad
Y=K_3.
\]
The potentially singular term is the coefficient \(S^4Y(t)\). If one only knows
\[
Y(t)\lesssim \frac{\gamma H_2}{t},
\]
then on a dyadic slab \([t/2,t]\),
\[
\int_{t/2}^t S^4Y(s)\,ds
\lesssim
S^4\gamma H_2\log 2.
\]
Using \(\gamma=S^2H_2^{1/2}\), this is
\[
S^4\gamma H_2
=
S^6H_2^{3/2}
=
\gamma^3,
\]
so for small critical parameter \(\gamma\) it is a bounded multiplicative contribution to the Moser product. This singular coefficient does **not** become a \(1/t\) pointwise curvature bound.

But the Moser output still contains the ordinary parabolic mean-value normalization. For seed \(p_0=3\), on a cylinder of spatial measure \(V\) and time length \(T\),
\[
\|aF\|_\infty
\lesssim
(VT)^{-1/3}
\left(\int_0^T K_3\right)^{1/3},
\]
with constants also depending on the Sobolev/cutoff/potential data. Therefore the bound is uniform on \([T/4,T]\) for fixed \(T\), but if one re-runs the estimate on \([0,t]\), a \(t^{-1/3}\)-type averaging scale appears. This is not the earlier \(C\beta/t\) decay.

So the correct correction is:

\[
\boxed{
\text{The singular potential does not transmit a }1/t\text{ output; the fixed-slab Moser bound is uniform in }t.
}
\]

Not:

\[
\text{There is no time-scale dependence whatsoever.}
\]

---

### (b) Does the four-dimensional volume cancellation work correctly?

It works in the corrected parabolic normalization, but not in the note’s boxed formula (6.9).

Use
\[
\|aF\|_\infty^3
\lesssim
\frac1{VT}\int_0^T K_3.
\]
The supplied spacetime bound gives
\[
\int_0^T K_3
\lesssim
\gamma H_2(1+\theta),
\qquad
\gamma=S^2H_2^{1/2}.
\]
Thus
\[
\|aF\|_\infty^3
\lesssim
\frac{S^2H_2^{3/2}}{VT}.
\]
Now insert the four-dimensional relations
\[
H_2\le C V(1+K_0),
\qquad
S^2\simeq \frac{r^4}{V},
\qquad
T=\theta r^2.
\]
Then
\[
\frac{S^2H_2^{3/2}}{VT}
\lesssim
\frac{(r^4/V)\,V^{3/2}(1+K_0)^{3/2}}{V\,\theta r^2}
=
\frac{r^2}{\theta V^{1/2}}(1+K_0)^{3/2}.
\]
Since
\[
S\simeq \frac{r^2}{V^{1/2}},
\]
this becomes
\[
\|aF\|_\infty^3
\lesssim
\frac{S}{\theta}(1+K_0)^{3/2},
\]
hence
\[
\boxed{
\|aF\|_\infty
\lesssim
S^{1/3}\theta^{-1/3}(1+K_0)^{1/2}.
}
\]

This is the correct volume bookkeeping from the supplied assumptions.

Two corrections follow.

1. The Step 31 note’s boxed estimate
\[
\|aF\|_\infty
\lesssim
S^{2/3}H_2^{1/2}
\]
does not match the parabolic mean-value normalization and should not be used as the final volume-cancellation statement.

2. The phrase “independent of collapse volume \(V\)” is only true after expressing \(V\) through \(S\). If collapse causes \(S\) to blow up, the estimate still blows up. Thus the argument requires either bounded \(S\) or an additional mechanism controlling the Sobolev constant in collapsing regimes.

For the defect estimate, the analogous fixed-slab calculation is cleaner. If persistence gives
\[
J_6(t)\lesssim \delta^6V
\]
or
\[
\int_{T/4}^T J_6(s)\,ds\lesssim T\delta^6V,
\]
then
\[
\|aE\|_\infty^6
\lesssim
\frac{1}{VT}\int_{T/4}^T J_6(s)\,ds
\lesssim
\delta^6,
\]
so
\[
\boxed{\|aE\|_\infty\lesssim\delta.}
\]

---

### (c) Is the Gronwall treatment of the single-\(\chi\) \(m=2\) term valid?

Yes, for that exact term.

At \(m=2\), the relevant raw term in the \(U=a(\operatorname{Rm}+G)\) evolution is described as
\[
\chi\nabla^2\chi*\nabla^2U.
\]
Testing against
\[
|\nabla^2U|^{p-2}\nabla^2U
\]
gives
\[
I
=
\int_M \chi|\nabla^2\chi|\,|\nabla^2U|^p\,d\mu.
\]
Since \(0\le\chi\le1\),
\[
I
\le
\|\nabla^2\chi\|_{L^\infty(g(t))}
\int_M|\nabla^2U|^p\,d\mu
=
\|\nabla^2\chi\|_\infty A_2(p)^p.
\]
If
\[
\|\nabla^2\chi\|_\infty\lesssim r^{-2}
\]
has been established, then
\[
I\lesssim r^{-2}A_2(p)^p.
\]

This is a legitimate lower-order term in
\[
\frac d{dt}A_2(p)^p+cD_{2,p}
\le
C(1+A_2(p)^p).
\]
Then Gronwall yields
\[
A_2(p)^p(t)
\le
e^{Ct}\left(A_2(p)^p(0)+Ct\right).
\]

Trying to absorb \(I\) into
\[
D_{2,p}
=
\int\chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}
\]
would be the wrong mechanism: a Young inequality matching the single \(\chi\) term to the \(\chi^2\)-weighted dissipation would introduce negative powers of \(\chi\) in the complementary term near the transition set. The unweighted \(A_2(p)\) route avoids this.

The necessary qualification is that \(\nabla^2\chi\) is taken with respect to \(g(t)\). Since \(\chi\) is fixed as a function but the connection evolves,
\[
\nabla^2_{g(t)}\chi
=
\nabla^2_{g_0}\chi
-
(\Gamma(g(t))-\Gamma(g_0))*\nabla\chi.
\]
Thus \(|\nabla^2\chi|_{g(t)}\lesssim r^{-2}\) is not obtained merely from bilipschitz metric comparison. In the supplied shifted-curvature continuation scheme, it comes from the coupled Wang triangle, specifically the lower-order implication
\[
A_{\le1}\Longrightarrow C_2,
\]
where \(C_2\) controls \(\nabla^2\chi\). Once this is in place, the Gronwall estimate is valid.

---

### (d) Are there subtle issues with unweighted \(A_2\) including transition-region curvature?

Yes, but they are not fatal in the shifted-curvature scheme.

The unweighted norm is
\[
A_2(p)^p
=
\int_M|\nabla^2U|^p\,d\mu,
\qquad
U=\chi^2(\operatorname{Rm}+G).
\]
Near the transition region, \(\nabla^2U\) contains terms such as
\[
(\nabla^2\chi)\chi\,(\operatorname{Rm}+G),
\qquad
|\nabla\chi|^2(\operatorname{Rm}+G),
\qquad
\nabla\chi*\nabla\operatorname{Rm},
\qquad
\chi^2\nabla^2\operatorname{Rm}.
\]
Therefore \(A_2\) genuinely sees transition-region curvature not fully protected by a \(\chi^2\) pointwise weight. This is why one cannot argue from \(\sup|\chi^2\operatorname{Rm}|\) alone that \(A_2\) is pointwise controlled in the transition.

But the continuation argument does not require such a pointwise transition estimate. It estimates \(U\) directly and propagates the unweighted \(L^p\) norm from smooth initial data:
\[
A_2(p)(0)<\infty
\]
on the closed manifold. The degenerate diffusion supplies weighted control of top derivatives, while the lower-order transition terms enter the unweighted Gronwall energy. Thus transition curvature is **tracked by the energy**, not assumed absent.

The remaining delicate continuation issue is not this diagonal term. The harder family is the high-cutoff term
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U
\]
and its companions \(\Gamma_2,\Gamma_3,\Gamma_4\). According to the supplied shifted-curvature continuation file, these must be integrated by parts as a group in Wang’s Proposition 4.14 style. At general \(m\), the residual current-order product
\[
\nabla^2\chi*\nabla^m\chi*U*V|V|^{p-2},
\qquad
V=\nabla^mU,
\]
is handled by the simultaneous cutoff/curvature induction. The present verification of
\[
\int\chi|\nabla^2\chi||\nabla^2U|^p
\]
does not by itself prove that full grouped mechanism, but it is consistent with it.

---

## Corrected usable statements

A safe replacement for Claim 1 is:

\[
\boxed{
\|aF\|_{L^\infty([T/4,T])}
\le
C_{\rm Mos}
\left(
\frac1{VT}\int_0^T K_3(s)\,ds
\right)^{1/3},
}
\]
where \(C_{\rm Mos}\) depends on the Sobolev/cutoff constants and on the integrated potential \(\int S^4K_3\), but not on a pointwise \(1/t\) decay output. Using the supplied four-dimensional estimates,
\[
\boxed{
\|aF\|_{L^\infty([T/4,T])}
\lesssim
S^{1/3}\theta^{-1/3}(1+K_0)^{1/2}.
}
\]

A safe replacement for the defect statement is:

\[
\boxed{
\|aE\|_{L^\infty([T/4,T])}
\lesssim
\delta,
}
\]
assuming \(J_6\)-persistence at scale \(\delta^6V\) and the curvature potential bound above.

A safe replacement for Claim 2 is:

\[
\boxed{
\int\chi|\nabla^2\chi||\nabla^2U|^p
\le
Cr^{-2}A_2(p)^p
}
\]
once \(|\nabla^2\chi|_{g(t)}\le Cr^{-2}\) is supplied by the lower-order continuation induction. This term is a Gronwall term, not a dissipation-absorption term, and it requires no tensor cancellation.