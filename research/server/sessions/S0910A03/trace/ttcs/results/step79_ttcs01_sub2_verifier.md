# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/data/step79_ot_reduction.json",
    "Sessions/S0910A03/workspace/data/step79_verifications.json",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Verify the following structural reduction for orthogonally transitive T²-invariant 4D Einstein metrics with Ric = -3g.

Metric: g = e^{2λ}(dr²+dz²) + G_{ab}(r,z)dξ^a dξ^b with G = e^σ M, det M = 1.

1. AREA EQUATION: σ_rr + σ_zz + σ_r² + σ_z² = 6 e^{2λ}. Check the coefficient 6.

2. ORBIT MAP EQUATION: div(e^σ M^{-1}dM) = 0 (weighted harmonic map to H² = SL(2)/SO(2)).
  In H² polar coords: d-eq: (e^σ d_r)_r + (e^σ d_z)_z = e^σ sinh(d)cosh(d)|∇ψ|²
  Conservation: div(e^σ sinh²(d) ∇ψ) = 0

3. BASE CONFORMAL: Δλ = (|∇σ|² - e_{H²})/4 where e_{H²} = H²-energy of orbit map.

4. TWIST VANISHING: For commuting Killing fields on Ric=-3g, twist scalars are constant. Reflection reverses orientation ⟹ twist = 0 on exact reflected cores.

5. VII_0 SPECIALIZATION: Setting ψ=kz, d=d(r), the d-equation becomes (e^σ d')' = e^σ sinh(d)cosh(d)k², whose RHS is always positive. This is the VII_0 barrier mechanism.

6. STEP 73 RECOVERY: On the cusp background with diagonal orbit (α=v, β=0), the orbit equation gives v_rr + 3v_r + e^{-2r}v_zz = 0, recovering Step 73.

Verify each component. Check whether the coefficient in the area equation is 6 (not 3). Check whether the orbit equation is exactly a weighted harmonic map. Check the conservation law. Does the mechanism analysis correctly identify that general 2-variable H² maps can break the VII_0 barrier through angular momentum absorption by the growing weight e^σ? Are there additional conservation laws or monotonicity constraints in the coupled system that could prevent this?

## Output

## Verifier memo — Step 79 orthogonally transitive reduction

I recomputed the reduction independently from the block metric $g=e^{2\lambda}(dr^2+dz^2)+G_{ab}d\xi^ad\xi^b$, $G=e^\sigma M$, $\det M=1$, treating $(r,z)$ as a 2D base with $b_{ij}=e^{2\lambda}\delta_{ij}$ and $(\xi^1,\xi^2)$ as flat-torus orbit coordinates. The core of the reduction is correct, and I can now certify most of it by direct computation rather than by analogy. There is one genuine sign error in an auxiliary equation, and one presentational gap in the Step 73 recovery. Details below.

### 1. Area equation — coefficient 6 is correct

Tracing the orbit–orbit Einstein equation gives $G^{ab}\mathrm{Ric}_{ab}=G^{ab}\Lambda G_{ab}=2\Lambda$. From the Christoffel structure of the block metric, the full-matrix orbit shear $\operatorname{tr}(A_iA_j)$ with $A_i=G^{-1}\partial_iG$ cancels in the trace, leaving
$$G^{ab}\mathrm{Ric}_{ab}=-e^{-2\lambda}\bigl(\Delta_\delta\sigma+|\nabla\sigma|^2\bigr).$$
Setting this equal to $2\Lambda=-6$ yields exactly $\sigma_{rr}+\sigma_{zz}+\sigma_r^2+\sigma_z^2=6e^{2\lambda}$, equivalently $\Delta e^\sigma=6e^{2\lambda+\sigma}$. The coefficient is $|2\Lambda|=6$, **not 3**: the factor 2 comes from tracing over the two orbit directions, and using 3 would be the mistake of forgetting that trace dimension. The concrete cusp/tail checks confirm it: for $\sigma=-2\log(-t)$ one gets $\sigma_{tt}+\sigma_t^2=6/t^2=6e^{2\lambda}$. Confirmed.

### 2. Orbit map equation — genuinely a weighted harmonic map to the curvature $-1$ plane

The trace-free part of the orbit Einstein equation is $\operatorname{tracefree}(\mathrm{Ric}_{ab})=0$, and this is $\operatorname{div}(e^\sigma M^{-1}\nabla M)=0$. The decomposition is self-consistent: $G^{-1}\partial_iG=\partial_i\sigma\,I+M^{-1}\partial_iM$, the trace of $\partial_i(e^\sigma G^{-1}\partial_iG)$ reproduces $\Delta e^\sigma=6e^{2\lambda+\sigma}$, and the trace-free residue is precisely the $M$-equation. Since $\operatorname{div}(M^{-1}\nabla M)=0$ (with weight) is the tension-field equation for a map into the symmetric space $SL(2,\mathbb R)/SO(2)$, "weighted harmonic map to the plane of curvature $-1$" is the correct description. The energy normalization is right: with $M=\mathrm{diag}(e^\alpha,e^{-\alpha})$, $\tfrac12\operatorname{tr}((M^{-1}dM)^2)=d\alpha^2$, matching $ds^2_H=d\alpha^2+e^{-2\alpha}d\beta^2$ and $e_{H^2}=|\nabla\alpha|^2+e^{-2\alpha}|\nabla\beta|^2$.

The polar-coordinate forms are the standard target Christoffels, and I confirm both:
- $d$-equation: $\Gamma^d_{\psi\psi}=-\sinh d\cosh d$, so $\operatorname{div}(e^\sigma\nabla d)=e^\sigma\sinh d\cosh d\,|\nabla\psi|^2$ (positive right side). Matches (4.4).
- $\psi$-equation: Euler–Lagrange in $\psi$ gives $\operatorname{div}(e^\sigma\sinh^2d\,\nabla\psi)=0$. Matches (4.5).

The conservation law (4.5) is the Noether current of the rotational symmetry $\psi\mapsto\psi+\text{const}$ of the target. Confirmed, including that $J_i=e^\sigma\sinh^2d\,\psi_i$ is divergence-free.

### 3. Base conformal equation (4.8) — coefficient $1/4$ verified rigorously

This one I could close by direct computation, not just on the cusp. The base–base Ricci is
$$\mathrm{Ric}_{ij}=R^b_{ij}-\nabla^b_i\nabla^b_j\sigma-\tfrac12\sigma_i\sigma_j-\tfrac12 e_{H^2,ij},$$
using $\operatorname{tr}(A_iA_j)=2\sigma_i\sigma_j+2e_{H^2,ij}$. Tracing with $b^{ij}=e^{-2\lambda}\delta^{ij}$, using $R^b_{ij}=-\Delta_\delta\lambda\,\delta_{ij}$ in 2D, and substituting the area equation $\Delta_\delta\sigma=6e^{2\lambda}-|\nabla\sigma|^2$, everything collapses to
$$\Delta_\delta\lambda=\tfrac14\bigl(|\nabla\sigma|^2-e_{H^2}\bigr).$$
Exactly (4.8), coefficient $1/4$ and both signs correct. The off-diagonal component $\mathrm{Ric}_{rz}=0$ of the same tensor gives
$$\sigma_{rz}=\lambda_z\sigma_r+\lambda_r\sigma_z-\tfrac12\sigma_r\sigma_z-\tfrac12 e_{H^2,rz},$$
exactly (4.10). So the two base equations are not just cusp-checked; they follow from the general block-Ricci formula. This is strong internal support for the whole §4 system.

### 4. Sign error in the Iwasawa $\alpha$-equation (4.6)

The one defect I found. The target metric $d\alpha^2+e^{-2\alpha}d\beta^2$ has $\Gamma^\alpha_{\beta\beta}=+e^{-2\alpha}$, so the tension field $\tau^\alpha=\tfrac1{e^\sigma}\operatorname{div}(e^\sigma\nabla\alpha)+e^{-2\alpha}|\nabla\beta|^2=0$ gives
$$\operatorname{div}(e^\sigma\nabla\alpha)=-\,e^{\sigma-2\alpha}\,|\nabla\beta|^2,$$
with a **minus** on the right. Equation (4.6) as written has a plus. Cross-check: a geodesic in this plane obeys $\alpha''=-e^{-2\alpha}\beta'^2$ (semicircles in the upper-half-plane model $y=e^\alpha$ have $\alpha$ concave), confirming the minus. The polar $d$-equation (4.4) with its plus sign is the correct one and is internally consistent; (4.6) contradicts it under the $\beta=0\Leftrightarrow\psi=0$ correspondence. Because every worked example here has $\beta=0$, nothing downstream is affected numerically — but this is precisely the term that switches on in any true two-parameter ($\beta\neq0$) orbit map, which is the regime the mechanism discussion wants to explore. The corrected (4.6) should carry the minus sign; (4.7) for $\beta$ is fine.

### 5. Step 73 recovery — correct result, but the conformal coordinate change is elided

Substituting $\sigma=2r-2\log N$, $\alpha=v$, $\beta=0$ directly into the reduction *in the coordinates $(r,z)$* gives $v_{rr}+2v_r+v_{zz}=0$, which is **not** Step 73's $v_{rr}+3v_r+e^{-2r}v_{zz}=0$. The two agree only after recognizing that Step 73's base $dr^2+e^{2r}dz^2$ is not in conformal gauge. The conformal coordinate is $\tau=-e^{-r}$, giving base $e^{2r}(d\tau^2+dz^2)$, $e^{2\lambda}=e^{2r}$. Running $\operatorname{div}_{(\tau,z)}(e^\sigma\nabla v)=0$ with $\partial_\tau=e^r\partial_r$ produces
$$e^{2r}(v_{rr}+3v_r)+v_{zz}=0\;\Longleftrightarrow\;v_{rr}+3v_r+e^{-2r}v_{zz}=0,$$
which does match Step 73. So the recovery is correct, but §5.2 as written conflates Step 73's non-conformal radial variable with the conformal base coordinate. I verified the area equation in the same conformal frame: $\sigma=-2\log(-\tau)$ gives $\sigma_{\tau\tau}+\sigma_\tau^2=6/\tau^2=6e^{2r}$. The $\beta=0$ source is zero regardless of the (4.6) sign, so the recovery is untouched by item 4. Worth a one-line correction so a reader does not substitute into the wrong frame.

### 6. Twist vanishing (§2) — sound, and the distinction from off-diagonal $G$ is correct

For a Killing field on an Einstein manifold, $\mathrm{Ric}(X)\propto X^\flat$, so $X^\flat\wedge\mathrm{Ric}(X)^\flat=0$ and the twist form is closed; the rank-two scalars $c_X,c_Y$ are constant. A reflection fixing the central hypersurface reverses orientation, flips the Hodge star, sends $c_X\to-c_X$; constancy then forces $c_X=c_Y=0$. Valid, given the reflection isometry is present. The clarification that the off-diagonal orbit entry (the Li–Liu $A(r,z)$ in $dy+A\,dx$) is $\beta$ in the Iwasawa chart — the orbit-map angular degree of freedom, not twist — is correct and conceptually useful: $\beta\neq0$ is fully compatible with orthogonal transitivity. The $O(\|E\|)$ statement for approximate cores is the right order and is correctly noted as needing a separate uniform estimate over a long connector.

### 7. VII$_0$ mechanism (§6) and the open question about additional structure

The VII$_0$ metric does sit inside this T²-invariant orthogonally transitive class: $\partial_x,\partial_y$ commute and are Killing (metric independent of $x,y$), there are no base–orbit cross terms, and the rotating eigenframe is the helicoidal map $d=d(r)$, $\psi=kz$ with $\psi_z=k$ frozen. Then (4.4) reads $(e^\sigma d')'=e^\sigma\sinh d\cosh d\,k^2>0$, which is the same one-way feedback that Step 78 found by direct curvature computation ($K=2k^2a^{-2}\sinh^2 d$ monotone). The two derivations agreeing on the "always positive source" is a good independent cross-check, and both give orbit-plane curvature $3$ at the exact center.

On the central question — can a genuine two-variable $(d(r,z),\psi(r,z))$ map dissipate the center anisotropy through the growing weight $e^\sigma$? — the note's reasoning is a plausible heuristic supported by a correct principle (maps into a target of curvature $-1$ have a favorable Bochner term and no concentration, unlike maps to $S^2$), and the note is clear that existence is not established. Two points of precision, and three structures that would actually decide the matter:

**Precision.** The $\psi$-conservation law controls $\operatorname{div}J$, not the pointwise size of $\psi_z$. The radial-flux statement $\Phi(r)=\int_{S^1}e^\sigma\sinh^2d\,\psi_r\,dz=\text{const}$, with $\Phi\equiv0$ from $\psi_r(0,z)=0$ at the reflection center, is correct and rigorous. But §6.3(1) "if $e^\sigma$ grows and $d$ stays $O(1)$ then $\psi_z$ must decay" is not implied by conservation alone — the current can circulate on the $z$-circle. §6.2 states this more carefully; §6.3(1) slightly overstates it. The honest content is: the angular degree of freedom is not frozen (unlike VII$_0$), so the positive source *can* vanish; it is not forced to.

**Structures that would discriminate feasibility, not yet computed:**

1. **A Pohozaev/virial identity.** Multiply the area and orbit equations by radial/dilation vector fields and integrate over $[0,R]\times S^1$ with reflection data at $r=0$ and the tail-interface data at $r=R$ ($d\to0$, $\psi_z\to0$, $S\approx I$). This should produce an integral relation linking the order-one center anisotropy energy $\langle d_s^2\rangle_\rho\ge12-8\delta$ (Step 76, (7.1)) to the outgoing fluxes. It is exactly this kind of identity that could either show the expanding weight has enough room to carry the center energy out, or reveal an incompatibility at small full defect. This is the single most decisive inexpensive computation.

2. **The Hopf/stress structure of the weighted map.** For an unweighted harmonic map from a Riemann surface the Hopf differential is holomorphic; here the weight $e^\sigma$ and the coupling to (4.1),(4.8) modify it. Working out the failure-to-be-holomorphic term $\partial_{\bar w}(\text{Hopf})$ in terms of $\nabla\sigma$ would give a transport law for the trace-free orbit stress along $r$, which is what actually governs whether $d$ can relax.

3. **Single-valuedness of $\lambda$ around the $z$-circle.** Equation (4.8) plus the first-order pair from $\mathrm{Ric}_{rr}-\mathrm{Ric}_{zz}=0$ and (4.10) determine $\lambda$; on a $z$-periodic cylinder, $\oint\partial_z\lambda\,dz=0$ must hold at each $r$. With $\Lambda\neq0$ this closure links the orbit-map fluxes to the area profile and may impose a global relation not visible pointwise. Checking whether this period condition is automatically satisfied or imposes an extra equation would clarify whether the coupled system is genuinely free to choose the desired exit data.

None of these is settled by the material here, and the note's §8 "not established" list already names existence and the possibility of an additional monotonicity obstruction. My assessment is that the §4 reduction is fully correct (area coefficient 6, orbit map = weighted harmonic map, conservation law, conformal equation with $1/4$, and constraint (4.10) all verified by direct computation), the (4.6) sign needs the minus, the Step 73 recovery needs the conformal-coordinate note, and the mechanism is a well-motivated but unproven proposal whose decisive test is the integral identity in point 1 above.

### Summary of items to correct or add
- (4.6): change the source sign to $\;-e^{\sigma-2\alpha}(\beta_r^2+\beta_z^2)$; the polar (4.4) is the correct benchmark it must match.
- §5.2: state the conformal change $\tau=-e^{-r}$ explicitly; direct substitution in $(r,z)$ gives $v_{rr}+2v_r+v_{zz}$, and only the conformal frame gives Step 73's $v_{rr}+3v_r+e^{-2r}v_{zz}=0$.
- §6.3(1): soften to the divergence-form statement; pointwise $\psi_z$ decay is not forced by conservation.
- Everything else in §2–§5 checks, including the two base equations which I re-derived from the block-Ricci formula.