# Step 21: Conditional finite-exponent smoothing lemma

> **STEP 22 ENERGY CORRECTION.** The finite-exponent conclusion in this note is
> stronger than its hypotheses support.  The available input on a support
> component is `int_U F^2 <= M Vol(U)`.  For a Whitney ball
> `W=B_ell(y)`, Bishop--Gromov gives only
> `ell^4 fint_W F^2 <= C M r^4`; it does **not** give
> `int_W F^2 <= C M Vol(W)`.  Critical Sobolev absorption still survives
> through `A_W^2 ||F||_{L^2(W)} <= C r^2 sqrt(M)`, but the unweighted
> moment bounds and the time-uniform `H_3` input must be derived from a
> current per-component first-exit energy, not from a Whitney-volume-normal
> bound.  See `workspace/notes/step22_current_energy_formulation.md`, which
> supersedes Sections 5--13 of this note wherever they use (5.2) or treat
> current `gamma(t)` as already controlled.

> **CORRECTION (TTCS Step 21).** Sections 6 and 8 of the original version
> contained a scaling error: curvature has dimension length⁻², so under
> metric rescaling `g̃ = ℓ⁻²g` the rescaled curvature is `|Rm(g̃)| = ℓ²|Rm(g)|`,
> and `F` is NOT invariant.  The raw Stampacchia output on the rescaled ball
> is `ℓ²F ≤ C`, not `F ≤ C`.  The correct pointwise output is from A03's
> `q → 3q/2` weighted-moment iteration (Section 8 below, replacing the
> original Stampacchia step): `|aRm| ≤ Cγ/t`, giving `|aRm| = O(1)` at
> the smoothing time.  The parabolic Sobolev exponent, BG transfer, and
> a₀-cancellation in the critical absorption remain valid.  The volume
> power in (6.2) is corrected to `Vol^{3/2}`.

## 1. Purpose

This note derives the conditional finite-exponent smoothing lemma for the
normalized cutoff flow

\[
  \partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad a=\chi^2,\quad 0\le a\le1,
\]

on a four-dimensional closed Riemannian manifold.  It does not prove a
Ricci-pinching gap and does not settle Yau Problem 26.  All statements below
hold on a provisional first-exit interval on which the evolving metric satisfies
the hypotheses stated in the lemma.

The key advance over Steps 19–20 is an actual PDE output: under the stated
provisional conditions, the four-step chain

\[
  q{=}2\text{ energy}\;\longrightarrow\;
  \text{4D parabolic Sobolev}\;\longrightarrow\;
  q{=}3\text{ + time cutoff}\;\longrightarrow\;
  \text{local boundedness}
\]

produces a uniform curvature bound on each Whitney ball at positive time,
independent of the cutoff level `chi_0` and of collapsed volume.  Critical
absorption is used at the two fixed exponents `q=2` and `q=3` only; the final
step uses the established time-uniform spatial `L^3` as a supercritical
potential (`3 > n/2 = 2` for `n = 4`).

## 2. Hypotheses (provisional first-exit)

Let `B_{5r}(p)` be one support component.  Assume:

**(H1)** Per-component maximal-function control at scale `6r`:
\[
  \mathcal M_{6r}(|\operatorname{Rm}_0|^2)(p)\le K_0.
\]

**(H2)** Metric comparability on `B_{5r}(p)\times[0,T]`, `T=\theta r^2`:
\[
  \Lambda^{-1}g_0\le g(t)\le\Lambda g_0.
\]

**(H3)** Relative Sobolev persistence on `B_{5r}(p)` with constant `A^2`.

**(H4)** Small critical product:
\[
  \gamma:=A^2\|F_0\|_{L^2(B_{5r}(p))}\le\varepsilon_0,
\]
where `F=(1+|\operatorname{Rm}|^2)^{1/2}` and
`\varepsilon_0=\varepsilon_0(c,L,\Lambda)` is a numerical constant depending
only on the cutoff parameter `c`, the Lipschitz constant `L` of `\chi`, and
the comparability `\Lambda`.

## 3. Bishop–Gromov energy transfer to Whitney balls

Fix `y\in B_{4r}(p)` with `\chi_0=\chi(y)>0`.  Set `\ell=cr\chi_0`,
`a_0=\chi_0^2`, `W=B_\ell(y)`.

Since `B_\ell(y)\subset B_{5r}(p)` (ensured by `c<1` and `d(y,p)<4r`), the
integral comparison gives

\[
  \int_W|\operatorname{Rm}_0|^2\,d\mu_0
  \le\int_{B_{5r}}|\operatorname{Rm}_0|^2\,d\mu_0
  \le K_0\operatorname{Vol}_0(B_{5r}).
\]

Bishop–Gromov on `(M^4,g_0)` with `\operatorname{Ric}\ge-3g_0` gives

\[
  \operatorname{Vol}_0(B_\ell(y))
  \ge c_{\mathrm{BG}}\left(\frac\ell{5r}\right)^4
     \operatorname{Vol}_0(B_{5r}(p))
  =c_{\mathrm{BG}}\left(\frac{c\chi_0}{5}\right)^4
     \operatorname{Vol}_0(B_{5r}).
\]

Therefore

\[
  \ell^4\fint_W|\operatorname{Rm}_0|^2
  \le(cr\chi_0)^4\cdot
    \frac{K_0\operatorname{Vol}_0(B_{5r})}
         {c_{\mathrm{BG}}(c\chi_0/5)^4\operatorname{Vol}_0(B_{5r})}
  =\frac{5^4}{c_{\mathrm{BG}}}\,K_0\,r^4.
\]

The `\chi_0` cancels exactly.  Hence

\[
\boxed{
  \ell^4\fint_W F_0^2\,d\mu_0
  \le C(c)\,K_0\,r^4,
  \qquad
  \gamma_W:=A_W^2\|F_0\|_{L^2(W)}
  \le C\,r^2\sqrt{1+K_0}.
}
\tag{3.1}
\]

By (H2)–(H3), the same bound holds at time `t` with constant
`C(\Lambda)\gamma_W`.

## 4. Whitney-ball setup

On `W=B_\ell(y)`:

\[
  (1-Lc)^2a_0\le a\le(1+Lc)^2a_0,
  \qquad
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le\frac{4L^2}{r^2}.
\]

Nested balls: `W=B_\ell(y)\supset W_1=B_{3\ell/4}\supset W_2=B_{\ell/2}
\supset W_3=B_{\ell/4}\supset W_4=B_{\ell/8}\supset W_5=B_{\ell/16}`.

Whitney rescaling: `\tilde x=(x{-}y)/\ell`, `\tilde t=a_0t/\ell^2`.  On the
rescaled unit ball `\tilde B_1`:

- Operator `\partial_{\tilde t}-\tilde a\,\tilde\Delta` with
  `\tilde a=a/a_0\in[\lambda,\Lambda_W]`, uniformly parabolic.
- Rescaled time: `\tilde T=a_0T/\ell^2=\theta/c^2`, independent of `\chi_0`.
- Rescaled Ricci: `\ell^2\operatorname{Ric}=O(c^2r^2)`, negligibly small.
- Rescaled Sobolev and BG constants: uniformly bounded, dimension-dependent.

Under the metric rescaling `g̃ = ℓ⁻²g`, the curvature transforms as
`|Rm(g̃)|_{g̃} = ℓ² |Rm(g)|_g`.  The natural rescaled regularization is
`F̃ = (1 + |Rm(g̃)|²)^{1/2} ≈ ℓ²F` when `ℓ²|Rm| ≫ 1`.  For the
near-Einstein initial data with `|Rm| ~ O(1)`, the rescaled curvature
`ℓ²|Rm| ~ c²r²χ₀² ≪ 1` is SMALL on the rescaled ball.
The energy estimates below work with the ORIGINAL `F` and the
degenerate operator `∂_t - aΔ` made uniformly parabolic by the Whitney
reduction.  The pointwise bound is obtained by A03's `q → 3q/2` Moser
iteration on the weighted moments `H_q = ∫η² a^{q-2} F^q`, which
avoids metric rescaling entirely.

## 5. Step A — `q=2` energy estimate

Use the power inequality from Step 20, Section 3, at `q=2` with spatial cutoff
`\eta` supported on `W_1` and `|\nabla\eta|\le C/\ell`.  After integrating the
`\nabla^2a` terms by parts (using `|E|\le CF` and `|\nabla E|\le C|\nabla\operatorname{Rm}|`):

\[
\begin{aligned}
  \frac d{dt}\int\eta^2F^2\,d\mu+c_2\int\eta^2a|\nabla\operatorname{Rm}|^2\,d\mu
  &\le C_2\int\eta^2aF^3\,d\mu \\
  &\quad+C_2\int\left(\frac{|\nabla a|^2}{a}+a+a|\nabla\eta|^2\right)F^2\,d\mu.
\end{aligned}
\tag{5.1}
\]

The reaction is absorbed by Hölder/Sobolev:

\[
  \int\eta^2aF^3=\int aF\cdot(\eta F)^2
  \le C\,a_0\,\|\eta F\|_4^2\,\|F\|_2
  \le C\,\gamma_W
    \left(\int a|\nabla(\eta F)|^2+\ell^{-2}\int a(\eta F)^2\right).
\]

Since `\gamma_W\le Cr^2\sqrt{1+K_0}\le\varepsilon_0`, the gradient part is
absorbed into the LHS dissipation (the factor `a_0` cancels on both sides).

After absorbing and integrating over `[0,T]`:

\[
\boxed{
  \sup_{t\in[0,T]}\int_{W_2}F^2\,d\mu
  +\int_0^T\!\!\int_{W_2}a|\nabla\operatorname{Rm}|^2\,d\mu\,dt
  \le C_A\,(1+K_0)\operatorname{Vol}_0(W),
}
\tag{5.2}
\]

with `C_A` independent of `\chi_0` and collapsed volume.

## 6. Step B — parabolic Sobolev embedding

In four spatial dimensions, the standard parabolic interpolation inequality
(Ladyzhenskaya/Gagliardo–Nirenberg) gives, for `u\in L^\infty([0,T];L^2)\cap
L^2([0,T];H^1)` on a Riemannian ball of uniform geometry:

\[
  \int_0^T\!\!\int|u|^3\,d\mu\,dt
  \le C_{\mathrm{PS}}
    \left(\sup_t\int u^2\right)^{1/2}
    \int_0^T\!\!\int|\nabla u|^2\,d\mu\,dt.
\tag{6.1}
\]

The exponent `3=2(n{+}2)/n` is specific to `n=4`.

In the rescaled Whitney picture, the diffusivity is `a\approx a_0` and the
effective gradient dissipation is `a_0\int|\nabla F|^2`.  Applying (6.1) to the
Step A outputs on the inner ball `W_3`:

\[
\boxed{
  \int_0^T\!\!\int_{W_3}F^3\,d\mu\,dt
  \le C_B\,(1+K_0)^{3/2}\frac{\operatorname{Vol}_0(W)^{3/2}}{a_0^{1/2}}.
}
\tag{6.2}
\]

A03's weighted formulation uses `H_2 = ∫η²F²` (no `a`-weight at `q=2`)
and `H_3 = ∫η²aF³` (weight `a` at `q=3`).  The spacetime integral of
`H_3` is bounded by the absorption:

\[
  \int_0^TH_3(s)\,ds\le C\gamma\,H_2(0).
\tag{6.3}
\]

This is Equation (2.2) of A03's Step 20 note.  All factors are
independent of `χ_0` and collapsed volume because `γ` and `H_2(0)`
have the BG cancellation from Section 3.

## 7. Step C — `q=3` with time cutoff

On the rescaled cylinder `\tilde B_{1/4}\times[0,\tilde T]`, introduce:

- Time cutoff: `\varphi(\tilde t)=0` for `\tilde t<\tilde\delta`,
  `\varphi=1` for `\tilde t\ge2\tilde\delta`,
  `|\varphi'|\le C/\tilde\delta`.
- Spatial cutoff: `\tilde\eta` on `\tilde B_{1/8}\subset\tilde B_{1/4}`.

The `q=3` power inequality with these cutoffs:

\[
\begin{aligned}
  \frac d{d\tilde t}\int\varphi^2\tilde\eta^2F^3\,d\tilde\mu
  +c_3\int\varphi^2\tilde\eta^2F|\tilde\nabla F|^2\,d\tilde\mu
  &\le C_3\int\varphi^2\tilde\eta^2F^4\,d\tilde\mu \\
  &\quad+2\varphi\varphi'\int\tilde\eta^2F^3\,d\tilde\mu
        +\text{(cutoff spatial terms)}.
\end{aligned}
\tag{7.1}
\]

The reaction `\int\varphi^2\tilde\eta^2F^4` is absorbed by the same
Hölder/Sobolev mechanism at `q=3`:

\[
  \int(\varphi\tilde\eta F^{3/2})^2\cdot F
  \le\gamma_W\bigl(\|\nabla(\varphi\tilde\eta F^{3/2})\|_2^2+\cdots\bigr),
\]

absorbing the gradient part against the LHS dissipation (factor `9/4`
from `\nabla(F^{3/2})=(3/2)F^{1/2}\nabla F`).  The coefficient for `q=3`
is `9\gamma_W/4$`, still small.  Since `\varphi(0)=0`, the initial term
vanishes, and the time-derivative source is bounded by Step B:

\[
  \int_0^{\tilde T}|\varphi'|\int\tilde\eta^2F^3\,d\tilde\mu\,d\tilde t
  \le\frac C{\tilde\delta}\int_0^{\tilde T}\!\!\int_{\tilde B_{1/4}}F^3
  \le\frac{\tilde C_B}{\tilde\delta}.
\]

After absorption, since `\varphi=1` on `[\,2\tilde\delta,\tilde T\,]`:

\[
\boxed{
  \sup_{\tilde t\in[2\tilde\delta,\,\tilde T]}
  \int_{\tilde B_{1/8}}F^3\,d\tilde\mu
  \le\frac{C_C}{\tilde\delta},
}
\tag{7.2}
\]

with `C_C` depending only on the rescaled Sobolev constant and the bound
`\tilde C_B`.  All independent of `\chi_0` and collapsed volume.

Converting to original variables (`\tilde\delta=a_0\delta/\ell^2=\delta/(c^2r^2)`):

\[
  \sup_{t\in[2\delta,\,T]}\int_{B_{\ell/8}(y)}F^3\,d\mu
  \le\frac{C\,c^2r^2}{\delta}\,\ell^4.
\]

The L³ average `\fint_{B_{\ell/8}}F^3` is bounded by a constant depending
only on `\delta/(c^2r^2)`, the Sobolev data, and `K_0`.

## 8. Step D — weighted Moser iteration `q → 3q/2` (from A03)

> The original version used Stampacchia on the rescaled ball, but this
> requires the rescaled curvature `\tilde F = (1+\ell^4|Rm|^2)^{1/2}`,
> not the original `F`.  The raw Stampacchia output is `\ell^2F \le C`,
> i.e., `|aRm| \le Cr^{-2}`, which is weaker than needed.
> The correct mechanism is A03's weighted-moment iteration,
> which works entirely in the original metric.

From Steps A–C, the weighted cubic potential satisfies (A03 equation 2.3):

\[
  A^4H_3(t)\le\frac{C\gamma^3}{t},
  \qquad t\in(0,T].
\tag{8.1}
\]

This makes the curvature reaction in the `q`-th power inequality a time-dependent
potential of strength `C(r^{-2}+\gamma^3/t)` on `[t/2,t]`.  The recurrence
`q_{j+1}=3q_j/2` with base `q_0=2`, applied on nested cylinders
`Q_{j+1}\Subset Q_j\subset B_{\ell/2}\times[t/2,t]`, gives (A03 equation 11.3):

\[
  M_{q_{j+1}}(Q_{j+1})^{1/q_{j+1}}
  \le (CA^2)^{2/(3q_j)}
  \left[Cq_j^\sigma4^j(t^{-1}+r^{-2})\right]^{1/q_j}
  M_{q_j}(Q_j)^{1/q_j}.
\tag{8.2}
\]

The exponent sums `\sum1/q_j=3/q_0=3/2` and
`\sum(j+\log q_j)/q_j<\infty` guarantee convergence of the product.
The endpoint is:

\[
\boxed{
  \|aF(t)\|_\infty\le C\gamma/t
  \qquad\Longleftrightarrow\qquad
  |a\operatorname{Rm}(t)|\le C\gamma/t.
}
\tag{8.3}
\]

At the smoothing time `t=\theta r^2`:

\[
  |a\operatorname{Rm}|\le\frac{C\gamma}{\theta r^2}
  =\frac{C\sqrt{1+K_0}}{\theta}=O(1).
\]

For the defect, the same iteration starting from `q_0=6` and `J_6(0)\le\delta^6V`
gives (A03 equation 11.4):

\[
\boxed{
  |aE(t)|\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
}
\tag{8.4}
\]

All constants are independent of `\chi_0` and collapsed volume because the
weighted moments `H_q`, `J_m`, the BG energy transfer, and the Sobolev product
all have the cancellation from Section 3.

**What (8.3)–(8.4) give on the transition and plateau.**

- Plateau (`\chi_0=1`): `a=1`, so `|\operatorname{Rm}|\le C\gamma/t=O(1)`.
  The curvature is bounded.
- Transition (`\chi_0\to0`): `a=\chi_0^2`, so
  `|\operatorname{Rm}|\le C\gamma/(t\chi_0^2)` may be large.  The velocity
  estimate controls only bilipschitz metric displacement,
  `\int_0^T|aE|\,dt\le C\delta\,T\cdot(r^2/T)^{1/3}=O(\delta r^2)`,
  independent of `\chi_0`; it does not control curvature closeness because
  curvature contains second spatial derivatives.  No pointwise transition
  curvature bound should be inferred here.

The weighted bound `|aRm|=O(1)` is the correct output for the continuation
argument.  It does NOT give `|Rm|\le C` with constant independent of `\chi_0`,
but it does give uniform control on the metric speed `|aE|` and on all weighted
curvature expressions entering the energy and defect inequalities.

**Conditional status.**  The iteration (8.2) requires the weak nested
time-space estimate (A03 equation 11.1) on every nested cylinder,
uniformly with finite-neighbor outer terms.  This is the remaining
mathematical task for the zero-order curvature layer.

## 9. Conditional Finite-Exponent Smoothing Lemma

**Lemma.** Under hypotheses (H1)–(H4) with `T=\theta r^2`, `\theta<c^2/4`:
for every `y\in B_{4r}(p)` with `\chi(y)=\chi_0>0`, setting `\ell=cr\chi_0`,
and for every `\delta>0`:

1. *Time-uniform L²*:
   `\sup_{t}\int_{B_{\ell/2}}F^2\le C(1+K_0)\operatorname{Vol}(W)`.

2. *Spacetime L³*:
   `\int_0^T\int_{B_{\ell/4}}F^3\,d\mu\,dt` is bounded.

3. *Time-uniform spatial L³*:
   `\sup_{t\ge2\delta}\int_{B_{\ell/8}}F^3` is bounded.

4. *Weighted pointwise bound* (from A03 `q\to3q/2` Moser iteration):
   `|a\operatorname{Rm}(t)|\le C\gamma/t`, hence `|a\operatorname{Rm}|=O(1)`
   at `t=\theta r^2`.  Also `|aE(t)|\le C\delta(r^2/t)^{1/3}`.

All bounds are independent of `\chi_0` and collapsed volume.

**Proof.** Steps A–C above provide time-uniform weighted cubic potential
`H_3(t)\le C\gamma H_2(0)/t`.  Step D uses A03's `q\to3q/2` Moser
iteration on nested cylinders with convergent exponent products to produce
the pointwise weighted bounds (8.3)–(8.4).

## 10. Consequences for the continuation argument

The lemma gives weighted curvature and defect control on every Whitney ball.

**Metric drift.** `\int_0^T|aE|\,dt\le C\delta\,T^{2/3}\,r^{2/3}
=O(\delta r^2)$, independent of `\chi_0`.  Metric comparability (H2) is
maintained for sufficiently small `\delta` and `r`.

**Weighted curvature.** `|a\operatorname{Rm}|=O(1)` at the smoothing time.
This does NOT give `|\operatorname{Rm}|\le C$ with constant independent of
`\chi_0$; in the transition, `|\operatorname{Rm}|$ may be `O(1/\chi_0^2)`.
The metric displacement estimate gives bilipschitz comparison there, but not
curvature closeness to the initial metric.  The corrected Step 22 formulation
does not use pointwise transition curvature control.

**Defect energy.** From the triangular `Q$ estimate (Step 20, Section 7):
`Q_{\mathrm{support}}(T)\le e^{CT/r^2}Q_{\mathrm{support}}(0)`.  The weighted
curvature bound provides the potential `a|\operatorname{Rm}|\le C\gamma/t$ for
the local defect inequality.  With `\gamma/t=O(1/r^2)$ at `t=\theta r^2$, the
finite-neighbor coupling has bounded coefficients.

**Controlled charts.** On the plateau (`\chi_0=1`), `|a\operatorname{Rm}|=O(1)`
gives `|\operatorname{Rm}|=O(1)$, so the harmonic-coordinate equation produces a
controlled chart.  Through Step 8 tensor-deficit densities and Derdziński's
Proposition 5, the forbidden calibrated Einstein germ is obtained.  In the
transition, no chart is needed because the metric is essentially unchanged.

## 11. Relation to A03 weighted-moment hierarchy

A03's formulation uses the weighted moments `H_q=\int\eta^2a^{q-2}F^q` with
Sobolev variable `v_q=\eta a^{(q-1)/2}F^{q/2}`.  Their result (2.3):

\[
  A^4H_3(t)\le\frac{C\gamma^3}{t}
\]

is the time-decay version of Step C.  The backwards averaging that produces
this `1/t$ decay is equivalent to the time-cutoff mechanism: from
`\int_0^tH_3\le C\gamma H_2(0)` and `H_3'\le Cr^{-2}H_3$`, a good
intermediate time exists with `H_3(t_1)\le C\gamma H_2(0)/t_1$`, and forward
propagation from `t_1$ gives the uniform bound.

The two approaches are complementary: the direct weighted moments are cleaner
for the zero-order curvature hierarchy, while the Whitney rescaling makes the
operator uniformly parabolic for the subsequent derivative/Bernstein estimates.

## 12. Per-component versus total-support energy

A03 (message #292) correctly noted that total-support energy does not
automatically imply per-Whitney-ball smallness.  The resolution is in
Section 3: the maximal-function selection in (H1) gives per-component control
`\fint_{B_{5r}(p)}|\operatorname{Rm}|^2\le K_0$, and Bishop–Gromov comparison
from the component center to any interior Whitney ball cancels the `\chi_0^4$
factor in `\ell^4$ against the `(c\chi_0/5)^4$ volume ratio.

The centered per-component budget IS sufficient.  No additional per-Whitney-ball
hypothesis is needed beyond (H1).

## 13. What remains for the first-exit closure

The finite-exponent lemma and the `q\to3q/2` iteration are conditional on
(H1)–(H4) and on the weak nested time-space estimate (A03 eq. 11.1).

**Self-improving structure.** Per A03 message #294, the zero-order first-exit
does NOT require quantitative pointwise control of `\chi\nabla(aE)` or of
the connection.  All Hessian-`a` terms integrate by parts; fixed cutoff
gradients, relative Sobolev constants, and volume comparison transfer under
bilipschitz metric comparability.  The provisional first-exit quantities are:

1. **Metric comparability (H2)**: improved by the integrable defect velocity
   `|aE|\le C\delta(r^2/t)^{1/3}`.

2. **Sobolev persistence (H3)**: follows from metric comparability on fixed
   domains.  Self-improving.

3. **Current-time critical energy**: must be maintained small by a first-exit
   argument.  The `q=2` energy inequality gives `\sup_t\int F^2\le C(1+K_0)Vol`,
   so `\gamma(t)=A^2\|F(t)\|_2\le C\gamma(0)`.  This needs explicit
   writing but uses the same absorption mechanism.

4. **Triangular defect `Q/A\to0`**: from the multiplicative coupling
   `Q'_\alpha\le Cr^{-2}\sum Q_\beta`.

5. **Weak nested time-space estimate** (A03 eq. 11.1): the load-bearing
   remaining derivation.  All algebraic and exponent structure has been
   verified; the task is to prove it uniformly with the finite-neighbor
   outer terms from the exact evolving tensor equations.

6. **Adaptation of Wang's smooth-extension theorem**: terminal `|aRm|\le C\gamma/t`
   is expected to generate derivative bounds internally, but this adaptation
   from `-2aRic` to `-2a(Ric+g)` must be written.

## 14. Broader research position

This lemma addresses only the critical four-dimensional negative
LeBrun/Ishida–LeBrun laboratory.  Even if the full first-exit closure is
established, it would prove only the negative-branch Ricci-pinching theorem
for this specific family.  The positive branch, higher dimensions `n\ge5`,
the full interval statement, and the Lean 4 formalization remain open.

## Files

- Verification: `workspace/scripts/step21_finite_exponent_smoothing.py`
- This note: `workspace/notes/step21_finite_exponent_smoothing_lemma.md`
- Predecessor: `workspace/notes/step20_closed_tensor_estimate.md`
- A03 companion: `Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md`
- TTCS verification: see below
