# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step98_full_matrix_matching_pressure_test.md",
    "Sessions/S0910A03/workspace/data/step99_raychaudhuri_floor.json",
    "Sessions/S0910A03/workspace/data/step99_cost_structure_analysis.json"
  ]
}
```

## Task

Verify the following Raychaudhuri normal-cost analysis and assess whether a tangential cost floor exists.

For a Gaussian 4-metric g = dr² + q(r,s) with H = tr(q⁻¹q_r/2), W° = W - (H/3)I, and E = Ric + 3g:

(1) The Raychaudhuri identity H' + H²/3 + |W°|² = 3 - E_rr gives, with u = H - 3tanh r and integration against cosh²(r):
   ∫₀ᴿ cosh²(r)(-E_rr)dr = 3cosh²(R)(1-tanh R) + ∫₀ᴿ cosh²(r)[|W°|²+u²/3]dr
for any trial with H(0)=0 (minimal center), H(R)=3 (expanding). This identity was numerically verified with residual 3.4×10⁻³.

(2) The comparison ODE h'=(3+δ)-h²/3, h(0)=0, h(R)=3 forces 1≤k tanh(kR) where k=√(1+δ/3). At R=1: δ_min≈1.318. Asymptotically: δ_min~12e^{-2R}.

(3) For the conformal expansion q = cosh²(r)q₀(s) of a charged Koiso separator (scalar curvature -7, winding 2, S=1, Qmax=0.5):
   E_rr = E_ri = 0 exactly
   E_T = Ric(q₀) + 2q₀, with operator norm 9.94 at r=0, decaying as sech²(r)
   The metric has H(0)=0 and K(0)=0, so it does NOT match the charged Koiso Weingarten.

(4) For the quintic jet-preserving transition on [0,1] matching the charged center jets to expanding exterior:
   E_T dominates: peak 28.7 at r≈0.28, while Enn peaks at 10.7
   The dominant E_T term is Ric(q): the quintic creates intermediate metrics with spatial curvature up to 21.4

QUESTION: Is there a tangential-block analog of the Raychaudhuri floor? Specifically, must ‖E_T‖_op exceed some positive lower bound on [0,R] for any metric with H(0)=0 matching the charged Koiso center and H(R)=3? Or could the exact Einstein continuation (if it exists) achieve E_T=0 throughout, with the actual transition cost depending only on where the germ domain ends?

The conformal expansion suggests the tangential cost is 9.94·sech²(r_transition), which goes to zero as the transition point moves to larger r. This would mean the tangential cost has no floor — it depends on how far the exact Einstein germ extends.

## Output

## Verification memo: Raychaudhuri normal-cost identity and the tangential-block question

### Summary judgment

The two-sided normal (radial) analysis in parts (1)–(2) is correct; I rederived both the pointwise Raychaudhuri relation and the weighted integral identity from the warped-product Ricci formulas, and the comparison-ODE threshold reproduces the tabulated numbers. The warped-product and conformal computations in (3)–(4) are consistent with the JSON. However, the reasoning offered in the QUESTION — that the conformal expansion "suggests the tangential cost is 9.94·sech²(r_transition) → 0, hence no tangential floor" — does **not** follow, for a concrete structural reason: the conformal expansion is shear-free with a totally geodesic center, so it cannot begin at the charged Koiso data, and the 9.94 is the defect of that ansatz at *its own* minimal center, not a cost incurred by a charged-center transition. At the actual charged center the tangential defect is exactly zero. The existence-or-not of a tangential floor is therefore entangled with extendability of the charged Einstein germ and is not settled by the conformal comparison. Details below.

---

### (1) Raychaudhuri identity — verified, with one structural addition

With $K=\tfrac12 q_r$, $W=q^{-1}K$, $H=\operatorname{tr}W$, the warped-product radial Ricci is $\operatorname{Ric}_{rr}=-H'-\operatorname{tr}(W^2)$. Since $E_{rr}=\operatorname{Ric}_{rr}+3$,
$$3-E_{rr}=H'+\operatorname{tr}(W^2)=H'+\tfrac{H^2}{3}+|W^\circ|^2,$$
using $\operatorname{tr}(W^2)=|W^\circ|^2+H^2/3$ for the trace split on a 3-dimensional slice. This is exactly the stated pointwise identity.

For the weighted form, write $H=3\tanh r+u$. The background $H_0=3\tanh r$ solves $H_0'+H_0^2/3=3$, so
$$-E_{rr}-|W^\circ|^2=u'+2\tanh r\,u+\tfrac{u^2}{3},\qquad \cosh^2 r\,(u'+2\tanh r\,u)=\tfrac{d}{dr}\!\big(\cosh^2 r\,u\big).$$
Integrating against $\cosh^2 r$,
$$\int_0^R\!\cosh^2 r\,(-E_{rr})\,dr=\big[\cosh^2 r\,u\big]_0^R+\int_0^R\!\cosh^2 r\Big(|W^\circ|^2+\tfrac{u^2}{3}\Big)dr.$$
The edge term is $3\cosh^2R(1-\tanh R)-H(0)$ (since $u(0)=H(0)$, $u(R)=3(1-\tanh R)$). Setting $H(0)=0$ gives precisely the identity in part (1).

Two consistency points worth recording:
- The residual $3.4\times10^{-3}$ matches `normal_projection_rt1.identity_residual = 0.00342738` (the quintic trial, $H(0)=0$).
- The `hyperbolic_validation` block is not vacuous: for $q=e^{2r}I$ one has $E_{rr}=0$, $W^\circ=0$, $H(0)=3$, so the identity reads $0=3\cosh^2R(1-\tanh R)-3+\int\cosh^2 u^2/3$. The JSON confirms this: `endpoint_cost 1.5037` + `mismatch_integral 1.4964` = `3.0001` = `u_center 3` = $H(0)$. This independently validates the *general* identity including the center term to four digits, and confirms the code's $E_{rr}$, $H$, and radial differentiation. Part (1) is the $H(0)=0$ specialization of this validated relation.

### (2) Comparison threshold — verified

$h'=(3+\delta)-h^2/3$, $h(0)=0$ has closed form $h=3k\tanh(kr)$, $k=\sqrt{1+\delta/3}$, and $h(R)=3$ forces $k\tanh(kR)=1$. At $R=1$: $k\approx1.1997$, $\delta_{\min}=3(k^2-1)\approx1.318$ (matches `floor_rt1 = 1.31769`). Expanding $k=1+\varepsilon$, $\tanh(kR)\approx1-2e^{-2R}$ gives $\varepsilon\approx2e^{-2R}$, $\delta_{\min}\approx6\varepsilon=12e^{-2R}$; the `ratio_to_asymptotic` column rising toward 1 confirms this.

One point the core work should hold explicitly: this is a **pointwise** lower bound $\sup_{[0,R]}(-E_{rr})\ge\delta_{\min}\sim12e^{-2R}$, which **tends to 0** as the germ extends. The nonvanishing quantity is the *weighted integral* $\int\cosh^2(-E_{rr})\ge 3\cosh^2R(1-\tanh R)\to 3/2$. These are different objects. For a two-sided Ricci pinching statement the relevant quantity is the pointwise operator norm of $E$ relative to $g$, so the radial block by itself imposes no pointwise obstruction that survives $R\to\infty$; only its integral has a persistent floor $\ge 3/2$. This distinction directly conditions how the tangential question should be posed.

### (3)–(4) Warped and conformal computations — consistent

For $g=dr^2+\cosh^2 r\,q_0$ in dimension 4 (fiber dimension 3, $f=\cosh r$): $\operatorname{Ric}_{rr}=-3f''/f=-3\Rightarrow E_{rr}=0$; and
$$\operatorname{Ric}_T=\operatorname{Ric}(q_0)-(3\cosh^2 r-2)q_0\Rightarrow E_T=\operatorname{Ric}(q_0)+2q_0,\quad E_T^\sharp=\operatorname{sech}^2 r\,(\operatorname{Ric}(q_0)^\sharp+2I).$$
This reproduces the note's block and the 9.94·sech² decay: `conformal_R1.ET_op_sup = 9.937` at $r=0$; at $r=1$, `ET_end = 4.173 = 9.937·sech²(1)`. The center eigenvalue of $\operatorname{Ric}(q_0)^\sharp$ is $\approx 7.94$ (`Ric_q_max` at $r=0$), so with $R_{q_0}=-7$ the slice is strongly anisotropic (one direction $\sim+7.94$, the complementary two summing to $\sim-14.9$); this is internally coherent though not independently checkable here.

For the quintic (rt1): `sups.ET_total = 28.663` with the profile peaking between $r=0.28$ and $r=0.36$ (values 27.56 and 28.36 straddle the reported 28.7), and `sups.Ric_q = 21.42`. These match part (4). The important reading is that the peak is a spatial-curvature spike (`Ric_q` up to 21.4) manufactured by a poor interpolant, not an intrinsic tangential cost.

---

### The central question: is there a tangential-block floor?

**The conformal argument does not establish "no floor."** Two independent facts break the proposed chain of reasoning:

1. **The conformal expansion cannot start at the charged center.** For $q=\cosh^2 r\,q_0$, $W=\tanh r\,I$, so $W^\circ\equiv0$ and $K(0)=0$: the center is totally geodesic. The charged Koiso separator has $K_0\neq0$, i.e. $W^\circ(0)=A\neq0$ (pure shear, since $H(0)=0$). The 9.94 is the tangential defect of a shear-free metric evaluated at *its own minimal center*; sliding that ansatz's base point to larger $r$ does not connect it to the charged data. The number $9.94\,\mathrm{sech}^2(r_\text{transition})$ is not a cost paid by any charged-center transition.

2. **At the charged center the tangential defect is exactly zero.** From the identity $E_T^\sharp=\operatorname{Ric}(q)^\sharp+3I-W'-HW$ (equivalent to the note's block after substituting $q^{-1}K_r=W'+2W^2$), the charged 2-jet $X_{rr}(0)=2(\widehat R+3I)$ gives $W'(0)=\operatorname{Ric}(q_0)^\sharp+3I$ at $H(0)=0$, hence $E_T(0)=0$. So $\|E_T\|_{\mathrm{op}}$ *starts at zero* for a faithful charged transition; the quintic's 28.7 is generated in the interior by an unsuitable interpolant, precisely as the JSON's `Ric_q` spike shows.

**What actually governs the tangential cost.** Taking the trace-free part of the same identity yields the shear matrix Riccati
$$W^{\circ\prime}+H\,W^\circ=\big[\operatorname{Ric}(q)^\sharp\big]^\circ-E_T^\circ .$$
An exact tangential-Einstein continuation ($E_T^\circ=0$) requires $W^\circ$ to be driven by the slice anisotropy $[\operatorname{Ric}(q)^\sharp]^\circ$ and to steer from $A\neq0$ at the center toward $0$ at an isotropic expanding end. There is **no sign-definite structure here analogous to the scalar Raychaudhuri**: the radial floor came from a scalar Riccati with a definite-sign source $|W^\circ|^2\ge0$ and one-sided comparison; the traceless matrix equation is a driven linear-type flow with no comparable maximum-principle giving a lower bound on $\|E_T^\circ\|$. So a tangential floor cannot be inferred by analogy with (2). Note also that a nonzero center shear is *not itself* a defect — genuine Einstein metrics carry shear — so the presence of $A\neq0$ does not by itself force $E_T\neq0$.

**Consequently the tangential-floor question is essentially the germ-continuation question.** If the charged Einstein germ extends to (or approximately closes into) a complete continuation, then $E_T\equiv0$ on the germ and the residual cost is only that of truncating and closing the tail — no pointwise tangential floor. If no such continuation exists, a positive tangential floor independent of $R$ would be a rigidity statement equivalent to that nonexistence. Because the Riemannian Einstein system at a slice is elliptic and constrained (as the note correctly records — no gauge turns it into a well-posed radial evolution), the 2-jet does not freely extend; whether *this* charged separator extends and closes is the open problem itself. The present material does not resolve it in either direction.

**Weight of current numerical evidence.** The Step 98 nodal pilot reducing interior packed norm $294\to12$ leans toward interior compensability (i.e. *against* a robust pointwise tangential floor), but it is not usable as evidence: the solve stopped at four evaluations, endpoint jets were overwritten rather than carried by the optimized field, nonlinear products were not dealiased, and the "final" $1.363$ is the $N_s=16$ center Codazzi resolution floor from `step98_center_residual_resolution.json`, not a converged geometric residual. So it hints at compensability without demonstrating it.

**What would settle the question.** A genuine determination needs analysis of the coupled system — the shear Riccati above, the slice-metric evolution feeding $\operatorname{Ric}(q)$, and the Codazzi constraint $E_{ri}=q^{jk}\nabla_jK_{ki}-\partial_iH$ — under the two data conditions ($W^\circ(0)=A$ with $\operatorname{Ric}(q_0)^\sharp$ eigenvalue $\approx7.94$; isotropic expanding end). The concrete tension to resolve is whether $W^\circ$ can be driven from $A$ to $0$ while $\operatorname{Ric}(q)$ stays bounded (the quintic's 21.4 spike is where an arbitrary interpolant lets slice curvature blow up). A jet-preserving full-tensor transition optimized without the endpoint-overwrite artifact, reevaluated on an independent finer grid, would show whether $\sup\|E_T\|_{\mathrm{op}}$ can be driven below any prescribed level as $R$ grows (supporting "no pointwise floor") or plateaus at a positive value independent of resolution and $R$ (supporting a floor and, with it, nonextendability). Until such a converged sequence exists, the correct statement is that the tangential floor is undetermined, and specifically that the conformal $9.94\,\mathrm{sech}^2$ heuristic does not bear on it.

### Relation to the overall problem

Even a demonstrated absence of a tangential floor on the free-$T^2$ laboratory would give an approximately-Einstein transition of one sign on a non-compact model; it would not by itself produce a closed smooth manifold carrying a two-sided pinched metric with no Einstein metric of any sign, nor address the universal quantifiers over all such metrics. The normal-block result is solid and clarifying; the tangential-block question is the load-bearing unknown and remains open on the evidence supplied.