# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A01/workspace/scripts/step29_ak_exterior_bridge.py",
    "Sessions/S1003A01/workspace/scripts/step29_local_AK_flux.py",
    "Sessions/S1003A01/workspace/scripts/step29_capacity_contact.py",
    "Sessions/S1003A01/workspace/scripts/exterior_null_line.py",
    "Sessions/S1003A01/workspace/data/step29/ak_exterior_bridge_x0038_X128_rho10.json",
    "Sessions/S1003A01/workspace/data/step29/local_AK_flux_x0038_X128.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x0015_X256.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x0038_X128.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x007_X256.json"
  ]
}
```

## Task

Independently verify the Step-29 mathematical bridge between the canonical almost-Kähler action and the already solved antisymmetric complex-hyperbolic exterior response. Read the theory note and all three scripts/data. Check: (i) the nonlinear local formula Phat[t0,t1]=int L_AK+B(t1)-B(t0), including B=b_+-3F-9P^2-6Wuu', endpoint values and normalization; (ii) the exact linear formulas q=theta, v_-=f_-w, nu=-v_-/(2sqrt x), lambda, and L_AK=mu w'^2+(Aw^2)' with every coefficient/sign; (iii) that the Einstein mass mode has zero raw action and nonzero AK tail canceled by the interface, so the Step-19 mass null line is preserved and no tail action may be counted twice; (iv) that the numerical profile evaluations actually test those equations and that the reported raw/AK/flux numbers follow from the supplied artifacts; (v) the contact identity/capacity computation, especially whether the linear two-constraint minimizer and its interpretation (26-39% of observed QA/2, frozen-profile only) are correct. Identify any mathematical or code error and state the strongest corrected result and implications for the all-metric Einstein-gap programme. Do not propose a separate tail cost unless the bridge is false.

## Output

# Verification Memo — Step-29 AK–Exterior Bridge

## 1. Typographical error in the displayed $\lambda$ formula

The note presents
$$\lambda = -\frac{x^2(1+x)w' + (2-3x)w}{2(1+x)^3}$$
but the SymPy output in `ak_exterior_bridge_x0038_X128_rho10.json` is
```
"-(x**2*Derivative(w(x), x) - 3*x*w(x) + x*Derivative(w(x), x) + 2*w(x))/(2*(x + 1)**3)"
```
which expands to $-\bigl[(x^2+x)w' + (2-3x)w\bigr]/\bigl[2(1+x)^3\bigr]$. The numerator coefficient of $w'$ is $x^2+x = x(1+x)$, **not** $x^2(1+x) = x^3+x^2$.

**Independent derivation confirms the script.** Starting from $\nu=-\sqrt{x}\,w/\bigl[2(1+x)^{5/2}\bigr]$, $\beta=(3-2x)/\bigl[2\sqrt{x(1+x)}\bigr]$, and $\lambda=\tfrac12\nu_T+\beta\nu$ with $dT=dx/\bigl[2\sqrt{x(1+x)}\bigr]$:

$$\nu_T = 2\sqrt{x(1+x)}\,\frac{d\nu}{dx} = -\frac{2x(1+x)w'+w(1-4x)}{2(1+x)^3},$$

$$\beta\nu = -\frac{(3-2x)w}{4(1+x)^3},$$

$$\lambda = -\frac{2x(1+x)w'+w(1-4x)+(3-2x)w}{4(1+x)^3} = -\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.\quad\checkmark$$

The polynomials differ: $x(1+x) = x^2+x$ versus $x^2(1+x) = x^3+x^2$; the discrepancy is $x(1+x)(x-1)$. **All scripts and JSON artifacts use the correct SymPy expression. No downstream computation is affected; this is a display-only error in the note.**

## 2. Nonlinear local identity: $B = b_+ - 3\mathcal{F} - 9\mathcal{P}^2 - 6Wuu'$

### Algebraic check on exact CH

On the exact CH collar ($u=1$, $u'=0$, $q=0$, $A_g=A_h=\sqrt{x}$, $A_f=\sqrt{x(1+x)}$):

| Quantity | Value |
|---|---|
| $v_f = a_f'-\gamma_f$ | $(2x+1)-(1-x)=3x$ |
| $v_g = a_g'-\gamma_g$ | $\sqrt{1+x}-\sqrt{1+x}=0$ |
| $b_+ = 2-|v|^2-v_fv_gv_h$ | $2-9x^2$ |
| $\mathcal{P}=A_gA_h$ | $x$ |
| $\mathcal{P}_T=2uA_f$ | $2\sqrt{x(1+x)}$ |
| $\mathcal{P}_{TT}$ | $2(2x+1)$ |
| $\mathcal{F}=4x\cdot1-x\cdot2(2x+1)-2x(1+x)$ | $-6x^2$ |
| $B=(2-9x^2)-3(-6x^2)-9x^2-0$ | $\mathbf{2}$ |

Exact cancellation confirmed. $\checkmark$

### Numerical endpoint

At $x=128$ (CH end): `B_minus_2 = -5.82e-11`. This $10^{-11}$ residual arises from the floating-point profile representation, not from any formula defect. $\checkmark$

### Identity residual across nine test sections

All nine rows in `local_AK_flux_x0038_X128.json` have `local_identity_residual` in the range $5.4\times10^{-11}$–$6.3\times10^{-11}$, confirming $\widehat{P}_{tail} = \int L_{AK} + B_{\rm end} - B_{\rm entry}$ to that precision. Cross-checking at $x=0.5$:

$$0.01636263 = 0.01195842 + (2.000000 - 1.995596) = 0.01195842 + 0.00440421.\quad\checkmark$$

The note's Table (Section 2) entries match the JSON values to the reported significant figures. $\checkmark$

## 3. Linear bridge identity: $L_{AK} = \mu(w')^2 + (Aw^2)'$

### Symbolic verification

SymPy reports `identity_residual: "0"`. $\checkmark$

### Independent pointwise spot-check at $x=2$, $w=1$, $w'=0$

Using the correct $\lambda = 2/27$ and $\nu^2 = 1/486$:

$$L_{AK}=\tfrac{x}{2}(2\lambda^2-6\nu^2)=1\cdot\bigl(\tfrac{8}{729}-\tfrac{9}{729}\bigr)=-\tfrac{1}{729}.$$

Meanwhile $A'(2) = -x(-6x^2+15x-4)/\bigl[4(1+x)^6\bigr]\big|_{x=2} = -2\cdot2/(4\cdot729) = -1/729$, and $\mu\cdot0^2+A'(2)=-1/729$. $\checkmark$

### Coefficients $\mu$ and $A$

$\mu = x(1+x)f_-^2/4 = x^3/\bigl[4(1+x)^4\bigr]$ from Step-19 definitions. $\checkmark$

$A(x)=-x^2(3x-2)/\bigl[4(1+x)^5\bigr]$: vanishes at $x=0$ and $x=2/3$; negative for $x>2/3$, positive for $0<x<2/3$. At $x=10$: $A(10) = -100\cdot28/(4\cdot161051)=-0.004346449...$, matching the JSON `entry_interface_Aw2` for the mass mode with $w=1$. $\checkmark$

### Numerical profile test beyond $\rho=10$

`bridge_residual_profile = 1.49e-10`, i.e., $|\int L_{AK}-\int\mu(w')^2 - [Aw^2]_\rho^X|<2\times10^{-10}$. $\checkmark$

## 4. Einstein mass mode: no double-counting

For the exact decaying Einstein mass mode $w\equiv\text{const}$ (Step-19 null line $\delta=0$):

| Quantity | Value |
|---|---|
| Raw Ricci action $\int\mu(w')^2$ | $0$ |
| AK tail $\int L_{AK}=0-A(\rho)w^2$ | $-A(10)=+0.004346$ |
| Entry interface $A(\rho)w^2$ | $-0.004346$ |
| Sum (AK tail + interface) | $0.0$ |

The JSON confirms: `AK_plus_entry_interface: 0.0`. $\checkmark$

**Consequence**: the AK tail integral on a terminal CH interval is the raw Ricci action plus the interface flux $A(\rho)w_0^2$. The Step-19 exterior response $\delta^2/I(\rho)$ remains the correct terminal cost, and the mass null direction $\delta=0$ is preserved. Adding the AK tail to the raw exterior response would count $-A(\rho)w_0^2$ twice.

For the actual profile at $\rho=10$: the finite-$X$ predicted AK tail (from the Step-19 minimizer cost plus the flux) is $4.5650\times10^{-3}$, versus the actual AK tail $4.5689\times10^{-3}$, mismatch $3.93\times10^{-6}$. This small discrepancy measures nonlinear deviation of the optimized cell from the frozen-trace linear CH minimizer—it is not missing action. $\checkmark$

## 5. "96% is interface" interpretation

At $\rho=10$: raw tail $=1.53\times10^{-4}$, $B(\text{entry})-2=4.36\times10^{-3}$, AK tail $=4.51\times10^{-3}$. The interface conversion constitutes $4.36/4.51=96.6\%$ of the AK tail. This arithmetic is correct and the physical interpretation—that beyond $x\approx10$ the AK formulation's "positive" contribution is almost entirely a reclassification of quantities already captured by the raw exterior—is sound. $\checkmark$

## 6. Contact equation and capacity computation

### Contact identity

The identity $y_T + 4y/A_f = -\nu(1-y^2)$ with $y=\tanh(q/2)$ is verified on all three profiles ($x_0=0.015, 0.038, 0.07$) with maximum bulk residual $0.6$–$1.3\times10^{-6}$. The sign change of $\nu$ is confirmed in all three cases. $\checkmark$

The note correctly observes that on the linear CH tail this reduces to the Step-19 torsion equation $(k\theta)'=f_-v_-/2$—so it is not an independent new constraint but the same relation in AK variables.

### Capacity computation

The frozen-profile capacity minimization is a standard constrained quadratic problem:

**One constraint (endpoints):** $\operatorname{cap}_1 = h_0^2/(2R)$ with $R=\int\rho^{-1}dT$. For $x_0=0.038$: $h_0=-0.01748$, $\operatorname{cap}_1=0.00585$, $\operatorname{cap}_1/E_{\rm obs}=0.178$. $\checkmark$

**Two constraints (endpoints + contact moment):** The additional moment $M_{\rm res}$ is imposed on the harmonic residual via a Green representer $z$ solving $-(\rho z')'=c$, $z|_{\rm endpoints}=0$. The additional capacity is $M_{\rm res}^2/(2\langle c,z\rangle)$. For $x_0=0.038$: $M_{\rm res}=0.00591$, $\text{gram}=0.00364$, additional $=0.00591^2/(2\times0.00364)=0.00480$, total $\operatorname{cap}_2=0.01066$, $\operatorname{cap}_2/E_{\rm obs}=0.324$. $\checkmark$ — verified by reproducing the arithmetic from JSON values.

All three profiles show fractions 26–39%, which is genuinely far from saturation. The interpretation that the transport energy cannot be reduced to two scalar moments is correct: the remaining 61–74% requires the full nonlinear profile structure.

**Scope of this calculation:** As the note and script both state, the weights, integrating factors, and moments are produced by a single actual metric. No uniformity over the diagonal competitor class (let alone the full metric class) is asserted. This is a probe of one mechanism, not a lower bound.

## 7. Code-level observations

1. **`step29_ak_exterior_bridge.py`**: The `symbolic_bridge()` function is clean and self-contained. The `numerical_tail()` function reconstructs $w$ from the torsion relation through nested JAX autodiff, which is intricate but validated by the $1.5\times10^{-10}$ residual. The reconstruction chain ($q\to q_x\to w\to w_x\to\nu\to\lambda$) is numerically well-conditioned on the tested profile because $x\geq10$ is deep in the CH regime where $u\approx1$.

2. **`step29_local_AK_flux.py`**: The computation of $\mathcal{P}_{TT}$ uses `pTT = 2*((up0/u0)*af0 + At0[0])`, correctly implementing $d(2uA_f)/dT = 2(u'A_f/u + A_f')$ at $dT=u\,dt$. The 16-point Gauss quadrature per panel with 1200+ panels gives stable integrals. $\checkmark$

3. **`step29_capacity_contact.py`**: The Green representer computation removes the affine harmonic correction from $z_{\rm rep}$ to clean endpoint residuals from cumulative quadrature noise—a correct numerical technique. The `mask` for finite positive $\rho$ avoids the collar endpoint where $\nu=0$ and the weight $\rho=\hat{W}/\mu^2$ degenerates. $\checkmark$

## 8. Summary of the bridge's scientific content

The bridge is mathematically correct throughout the computational chain: the single displayed typo ($x^2(1+x)\to x(1+x)$ in the $\lambda$ formula) does not enter any script or data artifact.

**What is established:**

- The AK tail integral on a terminal CH interval and the raw Ricci tail integral differ by an explicit, computable interface flux. The AK formulation produces no independent positive exterior response.
- The Step-19 exterior response $\delta^2/I(\rho)$ with its Einstein mass null direction is the complete terminal cost for the antisymmetric sector. The AK decomposition is an exact reparametrization, not an additional source of positive action.
- The frozen-profile contact-moment capacity explains under 40% of the observed $W_3^+$ transport energy; the lower-bound problem requires retaining the full nonlinear ODE evolution, not just boundary traces.

**What remains open for the global programme:**

The bridge resolves the representation ambiguity between AK and raw formulations on the exterior, but the interior near-zone structure—where the Nijenhuis field $\nu$ generates the subthreshold saving—is not bounded from below by the quantities computed here. A global lower bound needs either a near-zone inequality coupling $\nu$ to $(u, \lambda)$ through the full evolution, or an entirely different mechanism for the compact core $x\lesssim6$.