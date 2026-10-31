# Step 60 TTCS assimilation and repaired local neck-drift model

Session `S0910A02`.  This note supersedes the overstatements in `step60_resonant_h4_neck_drift_and_alf_flux.md` where it is more precise.  It assimilates the TTCS verifier result and the additional exact Ricci computation made after TTCS.

Files added after the first Step-60 note:

- TTCS integration: `trace/ttcs/results/step60_ttcs01_verifier1_integration.md`
- Branches: `trace/ttcs/results/step60_ttcs01_sub1_verifier.md`, `trace/ttcs/results/step60_ttcs01_sub2_verifier.md`
- Exact local Ricci script: `workspace/scripts/step60_verify_warped_ricci_symbolic.py`
- Exact local Ricci data: `workspace/data/step60_verify_warped_ricci_symbolic.json`
- Corrected long-neck exact-Ricci schedule: `workspace/scripts/step60_full_warped_neck_ricci.py`
- Corrected schedule data: `workspace/data/step60_full_warped_neck_ricci.json`

## 1. What TTCS verified

The independent verifier supports the core Step-60 correction:

1. With metric bubble scale `t`, the ALE pullback metric may be written
   \[
   \widetilde g_i=t_i^{-1}F_i^*g_i,\qquad F_i(y)=\sqrt{t_i}\,y,
   \]
   and the Ricci defect obeys
   \[
   |F_i^*(\operatorname{Ric}_{g_i}-\Lambda g_i)|_{\widetilde g_i}\le t_i\delta_i.
   \]
2. The l=2 radial operator
   \[
   Lf=f''+\frac3r f'-\frac8{r^2}f
   \]
   has roots `2,-4` and Wronskian `r^3W=-6`.
3. A constant projected source produces the exact resonant particular solution
   \[
   f_p(r)=\frac S6 r^2\log\frac r{r_0}
          -\frac S{36}(r^2-r_0^6r^{-4}),
   \]
   hence relative l=2 flux drift `O(delta log(1/t))` from `r=O(1)` to `R~t^{-1/2}`.
4. Step 59's fixed noncritical weighted lemma with `beta<2` cannot reach the `O(t)` matching target; `beta=2` is the resonant endpoint and must be handled by flux/log or an equivalent critical weighted method.
5. The fixed-annulus iterated-limit argument in Steps 35--36/42 did not remove the resonance; it implicitly assumed the cross-neck matching rate it needed to prove.
6. The scalar ALF mass calculation is arithmetically correct as a first model: on the `R^3` base the roots are `(ell,-ell-1)`, so the mass pair is `(0,-1)`, not the ALE `(2,-4)` pair.

## 2. Corrections to my first Step-60 note

The first Step-60 note should be read with the following corrections.

### 2.1 The H4 statement is still a conditional flux framework, not a theorem

The one-dimensional Wronskian computation gives the correct error scale.  A geometric necessity theorem still requires a complete tensor flux identity of the form
\[
\Phi_k(R_i)-\Phi_k(r_0)
=\int_{r_0}^{R_i}\langle
\operatorname{Ric}_{\widetilde g_i}-\Lambda t_i\widetilde g_i, o_k\rangle
 +\mathcal N_i+\mathcal G_i+\mathcal T_i,
\]
with
\[
|\text{Ricci term}|\le C t_i\delta_i\log R_i,
\qquad
\mathcal N_i+\mathcal G_i+\mathcal T_i=o(t_i),
\]
plus inner EH-parameter orthogonalization and outer curvature identification.  Only after proving, for instance,
\[
\frac{\Phi_{k,\mathrm{in}}}{t_i}\to0
\]
or an equivalent vanishing of the inner normalized coefficient, does
\(\delta_i\log(1/t_i)\to0\) force
\(R_\pm(p)\zeta=0\).

Thus the correct status is: **rate-limited necessity is proved in the scalar l=2 model and becomes a geometric theorem only after the annular gauge/projection, nonlinear, gauge, tower-subtraction, inner-flux, and outer-identification pieces are supplied.**

### 2.2 The exponential channel should be stated two-sided when claiming constant drift

If
\[
t_i=e^{-a/\delta_i},
\]
then the scalar relative drift is constant, \(a/12\) in the normalization used by `step60_neck_drift_schedules.py`.  But the phrase
\[
t_i\lesssim e^{-c/\delta_i}
\]
only gives a lower bound on \(\\delta_i\log(1/t_i)\), not an upper bound.  For a true `O(1)` drift schedule use
\[
e^{-C/\delta_i}\lesssim t_i\lesssim e^{-c/\delta_i},
\]
or specify the exact schedule, e.g. `t=exp(-a/delta)` or, in the repaired local metric below,
\[
t_i=\delta_i e^{-2a/\delta_i}.
\]

### 2.3 Bianchi does not make the Ricci defect divergence-free

For
\[
E=\operatorname{Ric}-\Lambda g
\]
one has
\[
\nabla^iE_{ij}=\frac12\nabla_j\operatorname{tr}E,
\]
not generally `div E=0`.  This does not eliminate the free Cotton/trace-free Hessian channel because `C^0` pinching gives no control of \(\nabla E\), but future notes must not call a general Ricci defect TT without imposing trace/divergence conditions separately.

### 2.4 The original local warping schedule controlled only the Laplacian

The first local model with fixed outer orbifold radius `eta=1` controlled
\(\Delta u\) but not the full exact Ricci tensor.  In the exact opposite-warped metric
\[
g=dr^2+r^2d\theta^2+e^{2u}d\phi^2+e^{-2u}d\psi^2,
\]
the base Ricci block contains \(-2du\otimes du\).  If `R=t^{-1/2}` and
\(u=t r^2A(\log r)\cos2\theta\), then at the outer end
\(|\nabla u|^2\asymp t\), which exceeds the desired ALE Ricci allowance
\(t\delta\) by a factor `1/delta`.  The script `step60_warp_neck_drift_model.py` therefore proves only the linear Laplacian channel, not a full local Ricci-pinched segment.

### 2.5 ALF remains scalar-model only

The ALF calculation in the first note is a scalar Gibbons--Hawking/Taub--NUT mass proxy.  It does not prove that collapse bubbles must be ALF, does not treat Euclidean Schwarzschild, and does not compute the tensor Lichnerowicz adjoint kernel or boundary Wronskian.  Also the rod-energy bookkeeping needs endpoint/rod-count clarification before citing per-rod `8pi^2` saturation; the Chern--Weil total-energy pinning itself is unaffected.

## 3. Repaired exact local long-neck model

TTCS pointed out a possible repair: shrink the outer orbifold radius with the pinching defect.  I tested it explicitly.

Use the exact local metric
\[
g=dr^2+r^2d\theta^2+e^{2u}d\phi^2+e^{-2u}d\psi^2,
\]
with
\[
u=t r^2 A(\log r)\cos2\theta.
\]
The script `step60_verify_warped_ricci_symbolic.py` symbolically computed all Christoffel and Ricci components and verified exactly:
\[
\operatorname{Ric}_{rr}=-2u_r^2,
\quad
\operatorname{Ric}_{r\theta}=-2u_ru_\theta,
\quad
\operatorname{Ric}_{\theta\theta}=-2u_\theta^2,
\]
\[
\operatorname{Ric}_{\phi\phi}/g_{\phi\phi}=-\Delta_Bu,
\qquad
\operatorname{Ric}_{\psi\psi}/g_{\psi\psi}=+\Delta_Bu,
\]
where
\[
\Delta_Bu=u_{rr}+r^{-1}u_r+r^{-2}u_{\theta\theta}.
\]
The data file `step60_verify_warped_ricci_symbolic.json` has `all_components_match=true`.

Now set
\[
\eta_i^2=\delta_i,
\qquad
R_i=\frac{\eta_i}{\sqrt{t_i}}=e^{L_i},
\qquad
L_i=\frac a{\delta_i},
\]
so
\[
t_i=\delta_i e^{-2a/\delta_i}.
\]
Let `A(s)` change by `DeltaA=O(1)` across `s in [0,L_i]` using a smooth long-shoulder profile.  `step60_full_warped_neck_ricci.py` used the `C^2` smootherstep profile `q(z)=6z^5-15z^4+10z^3` as a numerical proxy; a genuine `C^infty` profile with comparable derivative bounds should be substituted for final geometry.  The scale estimates are:
\[
|\Delta_Bu|\le Ct_i/L_i\le C_a t_i\delta_i,
\]
while at the outer end
\[
|\nabla u|^2\le C t_i^2R_i^2 = C t_i\eta_i^2=Ct_i\delta_i.
\]
Thus the full exact local Ricci tensor, including quadratic gradient terms, is `O(t_i delta_i)` in the ALE frame, while the l=2 coefficient changes by `t_i DeltaA=O(t_i)`.

The script data records this uniformly.  For example, at `delta=0.1`, `a=4`,
\[
\log_{10}(1/t)\approx35.74,
\]
`max |Delta u|/(t delta) <= 1.876`, and the exact Ricci operator bound divided by `t delta` is about `17.88`.  At `delta=0.02`, `a=4`,
\[
\log_{10}(1/t)\approx175.42,
\]
with the same bounded constants.  The old fixed-eta schedule fails exactly as TTCS predicted: at `delta=0.05`, the gradient-square term divided by `t delta` is about `160`.

## 4. Meaning of the repaired model

This repaired local model is stronger than the first Step-60 Laplacian check.  It shows that the exponential long-neck channel survives the full exact Ricci tensor **in a local flat doubly-warped model** after the correct shrinking-outer-radius scaling is used.

It still does **not** produce a Yau--26 counterexample or even a closed near-pinched metric.  The remaining hard tasks are:

1. replace the local `T^2`-warped flat annulus by a neck compatible with the `S^3/\mathbb Z_2`/EH obstruction tensor, or compute a nonzero projection from this model into the relevant EH l=2 sector;
2. put the local model on top of a positive Einstein/orbifold background without losing the `O(t delta)` Ricci defect;
3. build smooth end caps with a `C^infty` profile and no endpoint Ricci spike;
4. control the ambient `H2/H4` subtraction and gauge terms through the shrinking outer radius `eta=sqrt(delta)`;
5. choose or build a closed smooth topology and decide whether it admits some far-away Einstein metric.

The important research consequence is narrower but real: the H4 `delta log(1/t)` failure channel is not just a scalar ODE artefact.  There is an exact local Riemannian metric mechanism, descended from the Step-11 opposite-warping Hessian freedom, that realizes order-one l=2 drift over an exponentially long neck while keeping the full local Ricci defect at the allowed scale.

## 5. Updated next decisive actions

Two lines now deserve priority:

1. **Tensor EH/neck projection of the repaired local model.**  Compute whether the repaired doubly-warped l=2 mode has nonzero Wronskian pairing with the actual EH obstruction tensor after embedding a torus-warped annulus into an `A_1` neck model or after rewriting it in appropriate spherical/tensor harmonics.  If the projection is nonzero and caps can be controlled, the exponent-scale failure channel becomes a serious counterexample construction path.  If the projection is forced to vanish or capping necessarily creates a larger Ricci defect, that becomes proof-side information.
2. **True ALF tensor flux.**  Replace the scalar `R^3` mass proxy by a gauge-fixed Lichnerowicz/Einstein-operator calculation on Taub--NUT and Euclidean Schwarzschild, including `S^1`-invariant tensor modes, adjoint kernel, mass/bolt parameter, and boundary flux under positive-Einstein normalization.

The A03/A01 restricted Ishida--LeBrun flow route has advanced according to peer messages #416--#420, but I did not audit it in this step.  It remains logically separate from the positive noncollapsed/collapse mechanisms developed here and still does not cover the full sign-free, all-dimensional Yau--26 proposition.
