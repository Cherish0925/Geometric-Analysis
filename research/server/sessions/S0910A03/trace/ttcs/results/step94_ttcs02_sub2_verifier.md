# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step94_two_ended_redshift_taper.py",
    "Sessions/S0910A03/workspace/data/step94_two_ended_redshift_taper.json",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/workspace/notes/step93_signed_transport_and_koiso_ot.md"
  ]
}
```

## Task

Read the new Step 94 two-ended redshift-taper benchmark and its exact output. Check the ODE normalization rho''=(6+Q)rho, Q=q^2/(2rho^3), the identity b=rho^-3/2 q' and w'+(3/2)sigma'w=b, the two-end q=0 construction, weighted integrals, and fitted exponential rates. Determine rigorously what this benchmark rules out: does it establish that Maxwell conservation/source control plus both OT end values, the exact area equation, and a finite separator Q bound cannot by themselves imply Q small or a length-independent matrix-weighted Poincare estimate? Confirm that it is not a full reduced Einstein connector because orbit-shape and horizontal equations are omitted. Identify the sharp remaining coupled equation or energy mechanism that any obstruction/construction must now confront. Give a concise mathematical memo.

## Output

## Verification Memo — Step 94 two-ended redshift-taper benchmark

Session S0910A03. Independent check of the scalar reduced model, its identities, its numerics, and the precise mathematical content of what it excludes.

### 1. The normalization and the two exact identities are correct

**Area equation.** With $\sigma=\log\rho$ and the weighted operator $L=\Delta+\nabla\sigma\cdot\nabla$, in one variable
$$L\sigma=\sigma''+(\sigma')^2=\frac{\rho''}{\rho}.$$
So the reduced relation $L\sigma=6+Q$ is exactly $\rho''=(6+Q)\rho$. This matches the reduced area equation (Step 90 eq. 2.5). With $q=0$ on the collars, $Q=0$ and $\rho''=6\rho$, giving the cusp growth $\rho\sim e^{\sqrt6\,r}$, $\sigma'\to\sqrt6$. (Note this is a different normalization from the round cusp $\sigma'=2$ used in Step 90 §5; here $\sqrt6\approx2.449$ is the correct rate for the $6+Q$ area equation, and it is the rate that drives every asymptotic below.)

**Transport identity.** With $w=\rho^{-3/2}q$,
$$w'=\rho^{-3/2}q'-\tfrac32\rho^{-5/2}\rho' q,\qquad \tfrac32\sigma' w=\tfrac32\rho'\rho^{-5/2}q,$$
so $w'+\tfrac32\sigma'w=\rho^{-3/2}q'=b$ identically. Also $w^2=\rho^{-3}q^2=2Q$, consistent with $w=\sqrt{2Q}$ used throughout Steps 90–93. The definitions $Q=\tfrac12\rho^{-3}q^2$ and $b=\rho^{-3/2}q'$ are internally consistent.

One point on the two recorded residuals. `transport_res` and `area_res` are algebraic consequences of the definitions (the code substitutes the analytic $w'$ and the ODE formula $\rho''=(6+Q)\rho$), so their vanishing at machine precision confirms code correctness of the identities, not independent accuracy of the integration. The genuine independent numerical content is the exponential-rate match in §2, which does validate the `solve_ivp` solution.

### 2. Numerics reproduce the analytic cusp exponents

- **Source decay.** $b=\rho^{-3/2}q'$ is supported on the taper $R<|r|<R+K$, where $q'=O(1)$ and $\rho\sim e^{\sqrt6 R}$, so $\|b\|_\infty\sim e^{-\frac32\sqrt6\,R}$. The fitted slope $-3.674232$ matches $-\tfrac32\sqrt6=-3.674235$ to five digits.
- **Weighted ratio.** $w^2\rho=q^2\rho^{-2}$ is concentrated near the center ($O(1)$, hence `weighted_charge_L2`$\to0.7934$, essentially $R$-independent), while $b^2\rho=q'^2\rho^{-2}\sim e^{-2\sqrt6 R}$. The ratio grows as $e^{2\sqrt6 R}$; the fitted exponent $4.898980$ matches $2\sqrt6=4.898979$. At $R=6$ the ratio is $3.93\times10^{12}$.
- **Geometric cross-checks.** $\rho(R+K)/\rho(R)$ at $R=1$ is $70.21/6.097=11.52\approx e^{\sqrt6}=11.58$, and `rho_at_taper_start`$(R{=}2)=70.214$ equals `rho_at_outer`$(R{=}1)=70.21$, since the pre-taper solution is the same $q=q_0$ orbit. The coordinate-charge change $\int_0^{R_{\rm end}}q'=q(R_{\rm end})-q(0)=-1$ is exact, and the odd-symmetric total is zero.

All numerics are internally consistent and pinned to the $\sqrt6$ cusp rate.

### 3. What the benchmark rigorously excludes

Fix $q_0=1$, so $Q(0)=q_0^2/2=\tfrac12$ is held at order one **independent of $R$**. As $R\to\infty$, $\|b\|_\infty\to0$ exponentially. Identifying the physical source with the mixed Ricci defect through $\|b\|_\infty\le2\sqrt2\,\delta$ (Step 90 eq. 1.5), this is a family in which
$$\delta\downarrow0\quad\text{while}\quad Q(0)=\tfrac12\ \text{fixed},$$
satisfying simultaneously: exact Maxwell transport, $q=0$ on both end collars, the exact one-dimensional area equation, and a finite central $Q$ (consistent with the enormous finite separator bound $C_Q(\delta)\sim6\times10^{10}$ of Step 92). Therefore:

**The implication "small physical source $\Rightarrow$ small $Q$" does not follow from {Maxwell transport, both end values $q=0$, exact area equation, finite separator $Q$}.** These four ingredients, treated as constraints on $(\rho,q)$, admit order-one $Q$ with $\delta\to0$.

Equivalently, the prototype matrix-weighted Poincaré/Hardy estimate (4.9), in its scalar instance $\int w^2\rho\le C\int b^2\rho+(\text{separator term})$, cannot hold with $C$ independent of connector length: the two integrals are related by the diverging ratio $e^{2\sqrt6 R}$, so any admissible $C$ must grow at least like $e^{2\sqrt6 R}$. The mechanism is transparent — the required coordinate-charge change $\Delta q=\int q'=\int b\,\rho^{3/2}$ is $O(1)$ even though $\|b\|_\infty\to0$, because the weight $\rho^{3/2}\sim e^{\frac32\sqrt6 R}$ exactly cancels the source decay. The exact area equation makes this **worse**, not better: it forces the very $\rho$-growth that amplifies a vanishing source into an order-one charge.

This is a correct and sharp refutation of the derivative-free program that would try to close the twist obstruction from transport + two-end data + area + separator finiteness alone.

### 4. It is not a full reduced Einstein connector — and the omission is active, not passive

The note states that the orbit-shape and horizontal equations are not imposed. This is verifiable at the level of the equation the scalar $Q$ actually obeys. In the plateau $q\equiv q_0$, the model has $\log Q=-3\sigma+\text{const}$, so
$$L\log Q=-3L\sigma=-3(6+Q)=-18-3Q.$$
The exact free-$T^2$ diagonal charge, by contrast, satisfies (Step 93 eq. 6.2 / Step 94 eq. 1.1)
$$L\log Q=-18-4Q,$$
where the extra $-Q$ comes from the orbit equation $L\alpha=Q$. The scalar model has effectively set $\alpha\equiv0$ ($M=I$, orbit map frozen), which violates $L\alpha=Q$ whenever $Q\neq0$. So the orbit equation is not merely dropped — the scalar profile is inconsistent with it. This is the concrete sense in which the benchmark is a relaxation, and it confirms the coverage statement in §5 of the note precisely.

Two of the three reduced equations are absent: the orbit equation (1.2) $\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z$ and the horizontal base equation (1.3).

### 5. The sharp coupled object any obstruction or construction must now confront

The benchmark isolates that Maxwell + area + two-end + separator-finiteness are not enough. The question is which remaining equation supplies a cost. Two facts locate it sharply:

1. **The orbit equation does not by itself block the redshift.** Step 90 §6 solves area **and** orbit exactly (the radial core with $L\alpha=Q$), and still exhibits redshift for every finite $Q_0$ up to $100$: coordinate $q_0$ stays fixed while physical $Q\to0$ as $\rho,\alpha$ grow. Imposing the orbit equation replaces the scalar $-18-3Q$ by the exact $-18-4Q$ but leaves the escape intact. So the operative missing equation is not the orbit equation.

2. **The horizontal base equation (1.3) is the residual object, coupled to two-end topology and separator stability.** In the Step 90 §7 forced discharge, area, orbit, and the $\theta\theta$ horizontal component are imposed exactly; only the $rr$ horizontal constraint $C=E_{rr}$ remains, obeying the exact law $C'=-2(u+H)C-wb$ and scaling as $O(\delta^2)$. Removing $C(L)$ with an exact exterior splice while keeping the source $O(\delta)$ is the open matching problem (a sign-changing control needed $\approx26\delta$ in the one tested basis), and the polar core has disk topology, not the free cylindrical two-end topology.

Combining these, the sharp remaining requirement is a **two-dimensional coupling of the horizontal Einstein equation (1.3) across the charged transition to (a) the separator stability form (4.6)/(3.3), $\int_C\mathcal W y^2\le\int_C(y_s^2+a_\delta y^2)$ with $\mathcal W\ge\tfrac34Q$, and (b) both exact OT end conditions on the free $T^2$ cylinder.** The one-dimensional transport cannot see this because it is one-dimensional and drops (1.3); the separator form controls only the single slice $n=0$ in tangential capacity (Step 92 §5–6). What is genuinely undetermined is whether sustaining an order-one $Q$ across a redshift of length $\gtrsim R$ forces the horizontal curvature / base Einstein equation to accumulate a cost over the two-dimensional region that the two-end area budget and separator stability forbid — or, conversely, whether one can solve (1.3) with $O(\delta)$ mixed source while preserving the free action, which would be a construction. This is exactly the "weighted, geometry-coupled source-to-charge" object the note names, now with the extra information that the coupling must live in the horizontal equation, since area and orbit alone permit the escape.

A complementary orbit-map remark worth recording: because $\beta\circ U=\log Q+3\sigma$ with $|\nabla_{\mathbb H^2}\beta|=1$ (Step 94 eq. 2.3), any region where $Q$ is prevented from redshifting while $\sigma$ still grows would force $|dU|\ge|d(\log Q+3\sigma)|$, i.e. large orbit energy $e$ — this is the transverse-energy term $e_\perp$ in eq. (2.7). The benchmark evades this only because its plateau lets $Q$ redshift with $U$ frozen. Any construction that instead pins $Q$ up must pay orbit energy, which the Bochner subsolution $\tfrac12Le\ge\tfrac12 e(e-6)$ (exact-OT ceiling $e\le6$, Step 85) and the resolvent ceiling (Step 87) are the natural instruments to test. This gives a second, independent handle on the same 2D coupling.

### Summary

The ODE normalization, the identities $b=\rho^{-3/2}q'$ and $w'+\tfrac32\sigma'w=b$, the two-end construction, the weighted integrals, and the fitted rates $-\tfrac32\sqrt6$ and $2\sqrt6$ are all correct and mutually consistent. The benchmark rigorously establishes, within the relaxed subsystem, that Maxwell transport, both OT end values, the exact area equation, and a finite separator $Q$ cannot by themselves force $Q$ small, and that no length-independent matrix-weighted Poincaré estimate of type (4.9) exists — the required constant grows at least like $e^{2\sqrt6 R}$. It is not a reduced Einstein connector: its scalar $Q$ obeys $L\log Q=-18-3Q$ rather than the exact $-18-4Q$, i.e. it actively violates the orbit equation, and the horizontal equation (1.3) is absent. Given that area+orbit exact already permit the redshift (Step 90 §6), the operative remaining object is the horizontal base Einstein equation coupled two-dimensionally to separator stability and both end conditions on the free $T^2$ cylinder, with the orbit-energy/resolvent equation as an independent lever on the same coupling.