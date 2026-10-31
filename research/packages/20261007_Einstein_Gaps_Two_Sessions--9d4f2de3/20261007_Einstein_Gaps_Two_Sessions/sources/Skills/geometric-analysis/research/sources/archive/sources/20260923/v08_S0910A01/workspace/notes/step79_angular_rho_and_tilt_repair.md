# Step 79: angular `rho_x` repair and tilt-linearized reduced equation

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## Purpose

This note repairs the Step 78 equivariant diagonal reduction before any attempt to compute the transverse Ozuch coefficients.  The antipodal construction remains valuable, but the local EH tensor must use Ozuch's actual angular map
\[
\rho_x(\zeta)_j={x^T(\zeta^+\circ\omega_j^-)x\over |x|^2},
\]
not a frozen vector in a fixed product `\Lambda^-` frame.  The step also records the correct second-order reduced-equation meaning of a scale-dependent tilt
\(\phi(t)=\phi_0+t\psi+o(t)\): a nonzero transverse coefficient can be absorbed if it lies in the image of `D\lambda`, so the real local obstruction is the component of `\mu` in the cokernel of this derivative.

The work is a local positive-branch test around `(S²×S²)/Z₂`; it does not prove or refute the full Yau--26 proposition.

## 1. Source pinning

The correction comes directly from Ozuch's definitions:

- Definition 1.14, lines 301--302 of the local Knowledge object:
  \[
  \rho_x(\zeta)_j=x^T(\zeta^+\circ\omega_j^-)x/|x|^2.
  \]
- Remark 1.15, lines 304--305: `rho_x` is quaternionic conjugation on the pure-quaternion part.  Therefore for fixed nonzero `\zeta`, varying `x\in S^3` rotates `\rho_x(\zeta)` through a sphere.
- Proposition 1.16 and the following curvature statement, lines 320--342:
  \[
  H^4(\zeta^+)=-{\rho_x(\zeta)^-\circ\zeta^+\over 2r^4},\qquad
  d_eR^-(H^4)=12\pi_{\rm tr}(\rho_x(\zeta)^-\otimes \rho_x(\zeta)^-)/r^6.
  \]
- Ozuch necessary equations, lines 791--795:
  \[
  t_j\lambda_k^j(\phi_j,v)+t_j^2\mu_k^j(\phi_j,v)=O(t_{\max}^{5/2}),
  \qquad \nu_l(t\phi,v)=O(t_{\max}^{5/2}).
  \]
- Ozuch's proof lines 818--826 explicitly use variations of `\lambda_2,\lambda_3` under motion of `\phi_n` to absorb/estimate transverse terms before concluding anything about `\mu_1`.  This is the source-level reason why `\mu_2,\mu_3` are not automatically separate obstructions.

## 2. Executed angular reconstruction

Script: `workspace/scripts/step79_angular_rho_verify.py`  
Data: `workspace/data/step79_angular_rho_verify.json`

For `\zeta=\omega_2`, the exact formulas produced by the script are
\[
\begin{aligned}
\rho_1&=-{2(x_1x_4+x_2x_3)\over r^2},\\
\rho_2&=-{x_1^2-x_2^2+x_3^2-x_4^2\over r^2},\\
\rho_3&={2(x_1x_2-x_3x_4)\over r^2}.
\end{aligned}
\]
For `\zeta=\omega_3`,
\[
\begin{aligned}
\rho_1&={2(x_1x_3-x_2x_4)\over r^2},\\
\rho_2&=-{2(x_1x_2+x_3x_4)\over r^2},\\
\rho_3&=-{x_1^2-x_2^2-x_3^2+x_4^2\over r^2}.
\end{aligned}
\]

The numerical sample of 20,000 random `S^3` points gives:

| quantity | value |
|---|---:|
| range of `rho_1` for `zeta=omega2` | `[-0.9999766, 0.9999646]` |
| fraction with `|rho_1|>0.1` | `0.90185` |
| max `||R^- rho_x||` for `R^-=diag(1,0,0)` | `0.9999766` |
| mean `||R^- rho_x||` | `0.498493` |
| max absolute off-block entry `(dR)_{12},(dR)_{13}` | `5.999925` |
| second moment of `rho` | approximately `I/3` |

A concrete point `x=(0.4,0.8,-0.4,0.2)` gives
\[
\rho_x(\omega_2)=(0.48,0.36,0.8),
\]
so
\(R^-\rho_x=(0.48,0,0)\neq0\) and
\((dR)_{12}=2.0736, (dR)_{13}=4.608\) in the script normalization.

### Consequence

The following Step 78 statements are withdrawn:

1. `rho(zeta)^-=(0,\cos\alpha,\sin\alpha)` in a fixed product frame for boundary pairings;
2. pointwise `R^- rho(zeta)^-=0` for in-kernel `\zeta`;
3. fixed block-diagonal `dR^-` with `(1,2)=(1,3)=0`;
4. any inference that the full second obstruction vanishes from that frozen-rho block structure.

The 37-angle Step 78 check varied the insertion angle `\alpha`; it did not vary the missing boundary angular variable `x\in S^3/Z_2`.

## 3. What survives: bare scalar factor-tracelessness

A useful structural fact remains true and is now stronger than the frozen-rho version:

**Surviving theorem.** If `\zeta^+\in span{\omega_2^+,\omega_3^+}`, then for arbitrary `\eta^-`, the product `\eta^-\circ\zeta^+` has zero trace on each `S²` factor separately.

The script checked the six basis products with max factor trace exactly zero.  Since `\rho_x(\zeta)^-` is an arbitrary anti-self-dual vector as `x` varies, this proves pointwise that the bare angular tensor
\[
H^4(\zeta^+)=-{\rho_x(\zeta)^-\circ\zeta^+\over2r^4}
\]
has zero direct pairing with every scalar tensor `f g_1` and `f g_2`.  The random-sample maximum factor trace of `H^4` was exactly zero in floating arithmetic.

This does **not** yet prove that the complete Bianchi-corrected source, the global Green response, or nonlinear residual has no scalar component.  The simultaneous antipodal symmetry still removes the four odd scalar zero modes `u_i g_j`, but even scalar modes, including the negative shape mode `g_1-g_2`, must remain in the inverse problem unless their actual source projections are separately shown to vanish.  Their presence is manageable; it is not a reason to abandon the construction.

## 4. Tilt linearization of the first obstruction

Script: `workspace/scripts/step79_tilt_linearization.py`  
Data: `workspace/data/step79_tilt_linearization.json`

Let
\[
R=\operatorname{diag}(\Lambda,0,0)
\]
in the original basis `(\omega_1,\omega_2,\omega_3)`, and take the base in-kernel direction `\phi_0=\omega_2`.  The adapted obstruction frame at `\phi_0` is
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})=(\omega_2,\omega_1,\omega_3).
\]
For a small unit-sphere tilt
\[
\phi(\varepsilon)=\operatorname{normalize}(\omega_2+\n\varepsilon(a\omega_1+b\omega_3)),
\]
Ozuch's first obstruction has the expansion, up to the common nonzero normalization constant `c`,
\[
\lambda(\phi(\varepsilon))=
\bigl(\Lambda a^2\varepsilon^2,
\Lambda a\varepsilon-\Lambda a^3\varepsilon^3-	frac12\Lambda ab^2\varepsilon^3,
0\bigr)c+O(\varepsilon^4).
\]
Thus
\[
D_\phi\lambda_{\phi_0}(a,b)=(0,c\Lambda a,0).
\]

If
\[
\phi(t)=\phi_0+t(a\omega_1+b\omega_3)+o(t),
\]
then
\[
t\lambda(\phi(t))+t^2\mu(\phi_0)
=t^2\bigl(D_\phi\lambda_{\phi_0}(a,b)+\mu(\phi_0)\bigr)+o(t^2).
\]
Therefore:

- `\mu_1` is not cancelled by first-order tilting; in the product rank-one block it is already zero by Ozuch Lemma 2.14's determinant formula.
- `\mu_2` is cancellable by the out-of-kernel tilt
  \[
  a=-{\mu_2\over c\Lambda}.
  \]
- `\mu_3` is the local surviving component in `coker(D_\phi\lambda)` unless another admissible variable changes it.  The in-kernel rotation `b` is first-order invisible to `\lambda`.

This is the finite-dimensional meaning of the Strategist correction: computing `\mu_2,\mu_3` should determine a required tilt and a surviving compatibility condition, not a two-number verdict demanding `\mu_2=\mu_3=0` separately.

## 5. Response to A02 message #532

A02's scalar-decoupling statement is consistent with the corrected calculation at the level of the bare `H^4` tensor.  The stronger assertion that all local `\mu_k` vanish by the `r=0` Kähler--Einstein control is not justified as stated.

The reason is visible in Ozuch's own proof at lines 818--826: transverse components of `\mu` can be compensated by `O(t)` motion of the EH direction because `t\lambda(\phi_0+t\psi)` is order `t^2`.  Thus exact Kähler--Einstein desingularizations imply vanishing only of the reduced component after quotienting by the image of `D\lambda`, unless one proves that the Ozuch coordinates for that family keep `\phi_n` fixed to `o(t)` and the orbifold deformation variables `v_n` contribute only lower order.  No such source-level statement is currently recorded.

For the product rank-one block, `D\lambda` has rank one at an in-kernel direction, so the expected local second-order condition is:
\[
\Pi_{\operatorname{coker}D\lambda}\mu=0,
\]
with the `\mu_2` component absorbed by a paired out-of-kernel tilt and the `\mu_3` component requiring either genuine vanishing or cancellation by another allowed parameter.  This keeps the construction open and more flexible than a strict `\mu_2=\mu_3=0` requirement, but it also prevents declaring the local tower automatically clear.

## 6. Corrected reduced problem for the antipodal diagonal row

Retain the simultaneous antipodal reduction from Step 78:

- it preserves the diagonal chirality row;
- it exchanges node pairs `(N,N)\leftrightarrow(S,S)` and `(N,S)\leftrightarrow(S,N)`;
- it makes the four scalar kernel modes `A`-odd, so their `\nu_l` equations vanish in the invariant problem.

But replace the Step 78 leading local statement by the following.

For each node orbit choose paired directions transported by `A`, allowing scale-dependent tilts:
\[
\phi_{j}(t)=\phi_{0,j}+t_j\psi_{j}^{(1)}+t_j^2\psi_{j}^{(2)}+
\sum_{i\ne j}t_i^2\psi_{ji}^{\rm int}+\cdots,
\qquad \phi_{0,j}\in\ker R^{\epsilon_j}.
\]
The reduced equations have the form
\[
F_{j,k}=t_j\lambda_{j,k}(\phi_j,v)
+t_j^2\mu_{j,k}(\phi_{0,j},v)
+\sum_{i\ne j}t_jt_i^2\,\mathcal I_{ji,k}
+\text{higher self-response}=0.
\]
At order `t_j^2`, solve the image component by choosing the out-of-kernel part of `\psi_j^{(1)}` and impose only the cokernel condition.  At the next order, the inter-node term of order `t_jt_i^2` reappears once lower-order terms have been cancelled; it should be treated together with the quadratic effects of the first tilt and any local self-response.  It has not disappeared merely because it lies below Ozuch's current `O(t^{5/2})` estimate.

The next decisive computation is therefore not just `\mu_2,\mu_3`, and not just `M_{adj},M_{diag}`.  It is the **sliced, angular, paired reduced map**:

1. reconstruct `H^4` and its connection/curvature variations with full `x`-dependent `rho_x`;
2. evaluate the local `\mu` component in `coker(D\lambda)` and the required `O(t)` out-of-kernel tilt;
3. then compute the order-`t^3` paired inter-node response using the projected product `P` pseudo-inverse, including even scalar and negative modes where the actual source projects onto them;
4. check whether scale ratios, paired tilts, and remaining angles solve the resulting finite-dimensional equations.

## 7. Current value for the Yau--26 program

This correction strengthens the positive mixed-row route by preventing a false simplification.  The product quotient remains a serious constructive laboratory: antipodal symmetry genuinely removes the odd scalar full-kernel modes, and the bare in-kernel EH tensor has no direct scalar trace.  But the branch has not proved an Einstein metric on `#3(S²×S²)` or any other mixed row.  The full Yau--26 problem remains sign-unrestricted and all-dimensional; this local positive construction is one stress test among the restricted IL negative-gap theorem and the graph-neck negative laboratory.

## Files

- Script: `Sessions/S0910A01/workspace/scripts/step79_angular_rho_verify.py`
- Data: `Sessions/S0910A01/workspace/data/step79_angular_rho_verify.json`
- Script: `Sessions/S0910A01/workspace/scripts/step79_tilt_linearization.py`
- Data: `Sessions/S0910A01/workspace/data/step79_tilt_linearization.json`
- Corrected Step 78 note should now be read through this Step 79 repair before using its rank-one or second-obstruction statements.

## 8. Pilot local image of scalar full-kernel modes

Script: `workspace/scripts/step79_scalar_kernel_Dv_lambda.py`  
Data: `workspace/data/step79_scalar_kernel_Dv_lambda.json`

After TTCS emphasized that the true quotient should use the full image of all `O(t)` movable parameters, I ran a normal-coordinate pilot for scalar full-kernel variations `v=u_i g_j`.  The calculation uses the quadratic expansion of the product metric on `S²(1)×S²(1)`, normalizes away the constant metric perturbation by the linear coordinate change `L=I-εh_0/2`, and recalculates the curvature operator block at the node.  The base calibration gives
\[
R^+=R^-=
\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},
\]
as required.

At the north--north pole and with `\phi_0=\omega_2`, the local curvature-block contributions of the four scalar modes to `D_v\lambda` in the adapted frame `(\omega_2,\omega_1,\omega_3)` are the columns
\[
\begin{pmatrix}
0 & 1/2 & 1/2 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0
\end{pmatrix}
\]
for `(u_1g_1,u_1g_2,u_2g_1,u_2g_2)`, up to Ozuch's common nonzero normalization.  Thus, in this local block model, scalar full-kernel variables can change only the `k=1` component, not the transverse `k=2,k=3` components.  Since the product rank-one determinant already gives `\mu_1=0`, this pilot supports the simpler local picture: out-of-kernel EH tilt absorbs `\mu_2`, and `\mu_3` remains the first truly local compatibility component.

Caveat: this is not yet a proof for Ozuch's global integrable deformation variables or a full gauge-sliced computation.  It checks only the curvature-block part of `D_v\lambda` for the explicit scalar tensors in local normal coordinates.  It should be used as evidence and a guide for the next exact slice calculation, not as a replacement for deriving the full `D_{(\phi,v,...) }\lambda` map.
