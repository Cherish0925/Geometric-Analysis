# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md",
    "Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260926_boundary_compatibility.md",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A01/workspace/data/perp_collar/verify_x0.01_X8_J_d8.json"
  ]
}
```

## Task

Read the Step-9 construction note as a differential geometer and verify the logical chain for the proposed finite-scale perpendicular complex-hyperbolic blow-up cell: normalization/rescaling from J6 to the Ric=-g cell cost, smooth bolt conditions, C2-to-smooth exact-collar perturbation, residual-finiteness supply of a fixed large embedded ball, and the I54 single-blowup transfer to a balanced-family coefficient below four. Identify any mathematical flaw that would invalidate the route, and separate it from the single remaining computational enclosure. Use the actual inherited I54 source and the Step-7/8 derivations. Do not treat floating-point evidence as proof.

## Output

# Verification memo: finite-scale perpendicular CH blow-up cell and the I54 transfer

## Summary

I checked each link against I54 §§1–2 and 6–8, Step 7 (§§1, 5), Step 8, and the two scripts. The logical chain from the frozen profile to

$$\limsup_j \alpha(M_j)/h_j\le 4-\tfrac{8\varepsilon_0}{9}$$

is mathematically sound. No step invalidates the route.

Several points that the Step-9 note treats as partly open are in fact exact consequences of how the profile is constructed:

- metric positivity,
- the bolt jets,
- the C² collar match,
- the topological charge "1".

The only quantity that still needs a validated enclosure is one integral over the frozen C² profile. Its floating-point value is

$$\frac{J_6}{8\pi^2}-1\approx-8.84\times10^{-4}.$$

There are also two code hazards and one existential qualification, recorded below.

## 1. Normalization: J₆ equals the I54 cell cost J₁/(8π²)

Set $\tilde g=6g$. Then:

- $\operatorname{Ric}_{\tilde g}=\operatorname{Ric}_g$, so the background $\operatorname{Ric}_g=-6g$ becomes $\operatorname{Ric}_{\tilde g}=-\tilde g$.
- $\operatorname{Ric}_{\tilde g}+\tilde g=\operatorname{Ric}_g+6g$.
- For a (0,2)-tensor, $|T|^2_{\tilde g}=6^{-2}|T|^2_g$, while $dV_{\tilde g}=36\,dV_g$.

The factors cancel, so the I54 cost $\int|\operatorname{Ric}+G|^2$ with $G=\tilde g$ equals $J_6(g)$.

The split $|\operatorname{Ric}+6g|^2=|\operatorname{Ric}^\circ|^2+\tfrac14(s+24)^2$ follows from $|(s/4+6)g|^2=4(s/4+6)^2$.

The collar data in `verify_x0.01_X8_J_d8.json` are $G=72=X+X^2$ and $h=(8,8,72)$ at $X=8$. These are the $K=x+x^2$ complex-hyperbolic profile with $\lambda=-6$, as in Step 8. The volume density $\pi^2\sqrt{\det h/G}\,dx$ matches $2\pi^2\sqrt{\det g}$ with $\int\sigma_{123}=2\pi^2$.

## 2. Topology and orientation: the cell is D # CP̄², with q = k = 1

I54 (1.1)–(1.2) requires $\Delta\chi=1$ and $\Delta\tau=-1$ relative to the complex orientation of $D$. This should be stated explicitly, because the bolt sits in the σ₁ slot rather than the CH fibre slot σ₃.

- The forms $r\,dr\wedge\sigma_i+r^2\sigma_j\wedge\sigma_k$, for i = 1, 2, 3, all lie in the same chirality Λ⁺. The CH Kähler form is asymptotic to the i = 3 member, so "perpendicular" means a rotation inside Λ⁺, not a change of orientation.
- Right multiplication by a unit quaternion rotates (σ₁, σ₂, σ₃). It lies in the identity component of SO(4) and maps the σ₁-bolt cell to a σ₃-bolt (Burns-type) cell. The σ₃-bolt cell is the complex blow-up.
- Hence the exceptional sphere has self-intersection −1 in the CH orientation, and q = k = 1.

A numerical check of orientation and topology is already coded. `PerpCell.report` returns `resid_A`, `resid_B`, defined as

$$(P-1)-\Big(4\Delta W^\pm+\tfrac{1}{12}\Delta S\Big),$$

with the CH ball values $12\pi^2X^2$ and $288\pi^2X^2$. These ball values are correct for any X: $\mathrm{Vol}=\pi^2X^2/2$, $s=-24$, $|W^+|^2=24$.

For the X = 8 witness, one of the two residuals should vanish to quadrature accuracy. This uses Weyl curvature, which none of the three Ricci reconstructions exercise. That makes it an independent test that the bolt is a (−1)-curve and not a (+1)-curve; the latter would give Δ(2χ+3τ) = +5.

## 3. Bolt smoothness is exact, given the frozen coefficients

Treat the stored doubles in `x0.01_X8_J_d8.json` as exact dyadic rationals. Put $y=x-x_0$.

**Radial coordinate.**
- $G=y\hat G(y)$ with $\hat G$ analytic and positive.
- Then $t=\int_0^y ds/(2\sqrt{G})=\sqrt y\,m(y)$, so $t^2$ is an analytic invertible function of y.
- Every profile function, being analytic in y, is therefore even and smooth in t.

**Collapsing direction.**
- $F=yF'(x_0)+O(y^2)$, so $F=f_1g_1t^2+O(t^4)$.
- The coefficient shift makes $q_F(x_0)+q_G(x_0)=0$ identically, so $F'G'=e^{0}=1$ exactly.
- With σ₁-period 2π this is the O(−1) no-cone condition. It is not the Eguchi–Hanson condition, which has period π.

**Tangential directions.**
- The isotropy acts on $\sigma_2+i\sigma_3$ with weight 2, because $\mathrm{Ad}_{e^{i\varphi}}$ rotates the (j, k)-plane by 2φ.
- The Verdiani–Ziller conditions therefore require h₂ + h₃ even, and h₃ − h₂ = O(t⁴) = O(y²).
- Here $w=\log(1+x)\,\mathrm{smooth}(u)+u^{\mathrm{wpow}}(1-u)^3\Sigma$ with $u=O(y)$ and $\mathrm{smooth}(u)=O(u^3)$. So w = O(y²) holds exactly if and only if wpow = 2.

**Artifact gap.** The bolt block of `verify_x0.01_X8_J_d8.json` lists F, G, F′G′ and w, but not w′(x₀). The only record of w′(x₀) = 0 is peer message 756. The verifier output should record w′(x₀) and wpow directly.

**Consequence for the topological "1".** The endpoint value Φ(bolt) = 1 in Step-7 (1.5) depends on F′G′ = 1:

$$u_3(x_0)=\sqrt{G/F}\,F'-\gamma_3\;\longrightarrow\;\sqrt{f_1g_1}-2=-1.$$

A cone angle would shift the charge. Because F′G′ = 1 holds exactly, the "1" is exact.

## 4. Positivity is automatic, not a grid fact

For x ∈ (x₀, X] we have u ∈ (0, 1]. The quintic smoothstep $\mathrm{smooth}(u)=10u^3-15u^4+6u^5$ is monotone from 0 to 1 on [0, 1]. Therefore:

- $G=\big(x-x_0+(x^2+x_0)\,\mathrm{smooth}(u)\big)e^{q_G}\ge (x-x_0)e^{q_G}>0$,
- $F=(x-x_0)e^{q_F}+x_0\,\mathrm{smooth}(u)>0$,
- $h_2=x>0$ and $h_3=xe^w>0$.

The Step-7 cutoff replaces F, G by convex combinations $\psi f+(1-\psi)f_{CH}$ of positive functions, so positivity also survives smoothing.

The phrase in Step 9 §6, "positivity on the whole interval" as a missing ingredient, can be removed. The 20,001-point minima (0.966, 1.032) are illustrations, not inputs.

## 5. C² collar and smoothing

At u = 1:
- smooth − 1 = O((1−u)³), and the factors (1−u)³ multiply q_F, q_G and the w-remainder.
- Hence $F-x$, $G-x-x^2$ and $w-\log(1+x)$ all vanish to third order.
- So the metric is C², with continuous curvature and a third-derivative jump.

Step-7 (5.2) applies. On the cutoff layer $\partial^j(\psi q)=O(A\varepsilon^{3-j})$, so both the new and the removed defect densities are O(Aε) on a layer of x-length O(ε) near x ≈ X = 8, where the geometry is uniformly nondegenerate. This gives

$$|\Delta J_6|\le CA^2\varepsilon^3.$$

The cutoff metric equals CH on [X−ε, X], so it is C^∞ with an exact open collar.

For the existence statement no explicit C is needed. The strict inequality for the C² profile passes to small ε by continuity. The explicit constant matters only if a numerical margin for a named smooth metric is wanted.

## 6. Large-ball supply via residual finiteness

The argument is correct:

1. Γ is a torsion-free cocompact lattice, so $\{\gamma\ne1: d(p,\gamma p)\le 2r\}$ is finite.
2. Malcev's theorem (finitely generated linear groups are residually finite) gives a finite-index Γ′ avoiding this set.
3. The closed r-ball, with r taken slightly larger than needed as a buffer, embeds in $X_*=\Gamma'\backslash\mathbb{CH}^2$.
4. In every finite cover of X_* the ball has deg-many disjoint simply connected lifts.

Numerically, $r_{-6}=\operatorname{arsinh}\sqrt8=1.7627$ and $r_{-1}=\sqrt6\,r_{-6}=4.318$. The collar sits inside x ≤ X, so D can be exactly this ball.

I54 Theorem 5 needs only connected finite covers of some fixed compact CH surface with $A_j\ge j^4$, and $\chi=3\tau$ holds for every CH surface. So X_* is a legitimate base. The balls needed are:
- k_j ≈ (2/9)Q_j = o(A_j) large balls for the cells,
- small balls for the handle and leftover surgeries.

**Existential qualification.** This proves the bound for some balanced sequence, built over X_*. It does not prove it for an arbitrary pre-fixed tower. Normal covers can keep a nontrivial γ with $d(p,\gamma p)\le 2r$ for every p. As a negative answer to "is the first coefficient 4 for balanced families of this type," the existential family is sufficient. I54 (2.3)'s phrase "on the original M_j" requires that the original base already contain the large ball, which can be arranged by choosing the base to be X_*.

## 7. The transfer formula

Let the cells and surgeries change (V, I, R) by δV, δI, δR, all o(A), around $V_0=2\pi^2A$, $I=-4V_0$, $R=4V_0$. Then

$$4VR-I^2=4V_0\,\delta J+O(\delta^2),\qquad \delta J=\delta R+2\delta I+4\delta V,$$

so

$$\mathcal E=\frac{\delta J}{V_0}\,\big(1+O(h)\big).$$

This reproduces I54 (2.1)–(2.2). The second-order term $n^2t^2/v$ is relatively O(h) → 0.

The contributions are:
- Each handle costs 32π² (LeBrun's $R_\varepsilon\to8\pi^2A(1+h)$ with δI, δV → 0).
- The k_j cells contribute $k_jJ_1$.

Therefore

$$\frac{\mathcal E}{h_j}\to\frac{(2/9)J_1+(7/36)\,32\pi^2}{2\pi^2}=\frac{J_1}{9\pi^2}+\frac{28}{9}.$$

With $J_1=8\pi^2(1-\varepsilon_0)$ this is $4-8\varepsilon_0/9$. The scale-invariant $\mathcal E=4-I^2/(VR)$ is the functional defining α.

Arithmetic:
- X = 8: $\varepsilon_0=8.83757\times10^{-4}$, coefficient 3.99921444.
- X = 16: $\varepsilon_0=1.09706\times10^{-3}$, coefficient 3.99902484.

## 8. Consistency with the proved lower theorems in I54

None of the I54 lower bounds applies to the witness.

- **Theorem 1 and §5** cover conformally Kähler and biaxial cells. The witness is triaxial with distinct self-dual Weyl eigenvalues in the interior.
- **§6.1** covers diagonal triaxial cells with the bolt in the CH-fibre slot σ₃. The perpendicular bolt is in σ₁, and the σ₁-slot complex structure is not integrable on the CH collar, since b ≠ c there.
- **§7**, i.e. (7.2) and the collar-strengthened (7.3), only forces 4d/9 < v < 4d when J < 8π². The cell volume is d minus an O(x₀²) amount, so it lies inside this range.
- **Proposition 2** (no smooth stationary cell) is irrelevant, because the witness is not stationary.

The deficit is about 8.8x₀². This matches Step 8's second-order picture: the perpendicular direction lies in the kernel of $R^+=\{s/4,0,0\}$, so there is no linear term, and the background response is of order x₀δ − δ².

A further cheap consistency test comes from LeBrun's signed estimate (I54 §7): $H_C=\int_C(-s+\sqrt6|W^+|)_+^2\ge36d$. This is a theorem, so any violation computed on the witness would expose a code error.

## 9. Code and artifact hazards

1. **Hard-coded X in evaluation.** `perp_dual_cost.py` `make_cell` builds `DualCell(x0, 1.0, …)`. So `eval` on any X ≠ 1 record silently evaluates a different metric, with collar at X = 1 and a different ell = log(X/x₀). The Step-9 numbers come from `perp_collar_verify.py`, and its collar block shows G = 72, so they are not affected. Any re-evaluation through `perp_dual_cost.py eval` would be wrong.
2. **Default wpow.** `eval` sets `smooth_mode = (rec.get('wpow',1)==2)`. A record without a `wpow` key is therefore evaluated as the non-smooth wpow = 1 profile.
3. **Stale comment.** `o11_perp_cell.py` says "G → x+x² (C¹)", but the code gives C².
4. **Filename typo.** The second witness is cited as `x00.01_X16_J_d8.json`, while its output is `verify_x0.01_X16_J_d8.json`.

## 10. The single remaining enclosure

**Statement to certify.** For the frozen C² profile at X = 8:

$$\Delta:=S_1+S_2+S_3+C_3+\frac{1}{32\pi^2}\int(s+24)^2\,dV<0.$$

By Step-7 (1.5), with its exact endpoint values Φ(bolt) = 1 (§3 above) and Φ(collar) = 0 (from C¹ matching to $u_{CH}=(0,3x,0)$), this is equivalent to $J_6/(8\pi^2)<1$.

**Why the relative form helps.**
- The total magnitude of the terms is $\sum|\cdot|\approx7.3\times10^{-3}$, against a margin of $8.84\times10^{-4}$. An enclosure with about 10% relative accuracy on the pieces is enough. The direct J integral would need about $10^{-4}$ relative accuracy.
- By Step-7 (4.5) and its analogues, each relative density is O(t) at the bolt. The Burns charge peak, of height ≈ 2·ell in u near u = 0, has already been moved into the exact "1".

**Removing the interval blow-up seen in Step 9.** The inflation comes from half-integer powers of y and from removable 0/0 quotients. A cancellation-free form exists:

1. Write $F=y\hat F$, $G=y\hat G$, $w=y^2\hat w$, with
   - $\hat F=e^{q_F}+x_0\,\mathrm{smooth}(u)/y$,
   - $\mathrm{smooth}(u)/y=u^2\,(u/y)\,(10-15u+6u^2)$,
   - $u/y=\log(1+y/x_0)/(\ell y)$, evaluated as $\log(1+z)/z$ by series or Arb.
2. The spin variables have definite parity:
   - $u_3$ is analytic, since $\dot a_3=\sqrt{\hat G/\hat F}\,F'$.
   - $u_1$ and $u_2$ are √y times analytic functions. The anisotropy enters through $\big(x\,\mathrm{expm1}(w)+F\big)/\sqrt{xe^wF}$, with $\mathrm{expm1}(w)=y^2\hat w\cdot\frac{\mathrm{expm1}(w)}{w}$.
   - $\lambda_1,\lambda_2\propto\sqrt y$, $\lambda_3\propto1/\sqrt y$, and $dt\propto dy/\sqrt y$.
3. Extract all √y factors symbolically. Each of S₁, S₂, S₃, C₃ and the scalar square then becomes an integrand in dy that is analytic in y. Its denominators are only $\hat F$, $\hat G$, x and $e^w$, all bounded away from zero.
4. Integrate in u ∈ [0, 1], using $dy=x_0\ell e^{\ell u}du$, with rigorous complex-analytic Gauss–Legendre on subintervals (e.g. `acb_calc_integrate`). Every function involved is holomorphic on a thin complex neighbourhood of [0, 1].

**Precision status.** The present floating-point evidence consists of:
- agreement of three independent Ricci reconstructions to 6×10⁻¹⁴,
- coordinate-code drift of 1.3×10⁻⁷ at 2400 nodes.

Both are far smaller than the margin, but neither is a proof. The X = 16 witness gives a margin of 1.10×10⁻³, at the cost of a ball of radius $\sqrt6\operatorname{arsinh}4=5.10$.

## 11. What the completed certificate would establish

Once the enclosure is done, the result is: there exist balanced sequences $M_j=X_j\#k_j\overline{\mathbb{CP}}^2\#\ell_j(S^1\times S^3)$, with X_j covers of a fixed compact CH surface, such that

$$\limsup_j\frac{\alpha(M_j)}{h_j}\le3.99921444\;(<4).$$

The coefficient 4 from the shrinking construction is therefore not optimal.

It would leave open:
- the true value of the first coefficient,
- its relation to the lower bound $c_1h^2$,
- the x₀ → 0 behaviour. The x₀ = 0.001 restart stayed slightly above 1, which may reflect either the optimizer or an O(x₀²) deficit with an x₀-dependent constant.
- whether the second-order kernel-direction interaction (Step 8 §7.4) can be computed as a closed formula in X.