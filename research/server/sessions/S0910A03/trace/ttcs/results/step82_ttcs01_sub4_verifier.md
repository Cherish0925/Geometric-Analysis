# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step82_slice_balance_verify.py",
    "Sessions/S0910A03/workspace/data/step82_slice_balance.json",
    "Sessions/S0910A03/workspace/scripts/step82_geometric_balance_check.py",
    "Sessions/S0910A03/workspace/data/step82_geometric_balance.json",
    "Sessions/S0910A03/workspace/scripts/step82_turning_covariance_model.py",
    "Sessions/S0910A03/workspace/data/step82_turning_covariance_model.json",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md"
  ]
}
```

## Task

Independently verify the physical Gaussian-slice balance derivation for the orthogonally transitive T^2-invariant metric and sharpen what it says about reversal of mean horizontal contraction. Use E=Ric_g+3g, q_r=e^{2a}dz^2+G_ab dx^a dx^b, rho=sqrt(det G), u=a_r, B=(1/2)G^{-1}G_r, v=tr B, B0=B-(v/2)I, dmu=e^a rho dz, V=int dmu, I=int u dmu, J=int v dmu. Check (i) J'=6V-int tr_orbit(E)dmu, (ii) I'=3V+int R(q_r)dmu-int E_zz dmu, including why the intrinsic orbit-Ricci trace integrates to zero, and (iii) after the Hamilton constraint, whether the defect term is 2E_rr-E_zz or tr_orbit(E)-E_rr. Derive the necessary inequality at the first return I=0 after I<0 under ||E||op<=delta, carefully treating covariance, differentiability, and signs. Then investigate whether the orbit-map energy identity, matrix equation, base constraints, or J/V evolution yields a nontrivial bound on 2Cov(u,v)+<v^2>/2-<|B0|^2> strong enough to prevent reversal, or whether the balances alone admit algebraically favorable slices. Give direct mathematics, state exact hypotheses, and distinguish slice compatibility from dynamic reachability. Check the session scripts/data rather than trusting their summaries.

## Output

# Verification Memo: Physical Gaussian-slice balances for the OT T²-invariant metric

Session S0910A03, Step 82 material. I recomputed the geometry from the definitions rather than trusting the script summaries, and I ran the algebra of the contracted Gauss equation independently. The headline result: **items (i) and (ii) are correct, but the exact defect term in (iii) is the opposite of what the two step82 scripts state in prose — and the scripts' own numbers prove it.** The first-return inequality survives this correction. Details below.

## 1. Definitions and evolution scaffolding — all consistent

For $g=dr^2+e^{2a}dz^2+e^{\sigma+w}dx^2+e^{\sigma-w}dy^2$ (dimension 4, target $\mathrm{Ric}=-3g$, $E=\mathrm{Ric}_g+3g$):

- $\rho=\sqrt{\det G}=e^\sigma$; $G^{-1}G_r=\mathrm{diag}(\sigma_r+w_r,\sigma_r-w_r)$, so $B=\tfrac12\,\mathrm{diag}(\sigma_r{+}w_r,\sigma_r{-}w_r)$, $v=\mathrm{tr}\,B=\sigma_r$, $B_0=\tfrac12\mathrm{diag}(w_r,-w_r)$, $|B_0|^2=\tfrac12 w_r^2$. ✓
- $u=a_r$, $H=\mathrm{tr}\,S=u+v$, $|S|^2=u^2+\tfrac12 v^2+|B_0|^2$ (using $\mathrm{tr}(B^2)=|B_0|^2+\tfrac{v^2}{2}$). ✓
- $d\mu=e^{a+\sigma}dz=\mathrm{dvol}_{q_r}/\!\int_{T^2}dx\,dy$; $V'=\int H\,d\mu=I+J$. ✓

All match the scripts.

## 2. (i) $J'=6V-\int \mathrm{tr}_{orbit}(E)\,d\mu$ — correct

$J'=\int(\sigma_{rr}+H\sigma_r)\,d\mu$. Using the tangential evolution $\mathrm{Ric}_g|_{TN}=\mathrm{Ric}_q-(S'+HS)$ and tracing over the orbit block,
$$\sigma_{rr}+H\sigma_r=\mathrm{tr}_{orbit}(S'+HS)=\mathrm{tr}_{orbit}\mathrm{Ric}_q-\mathrm{tr}_{orbit}\mathrm{Ric}_g=6-E_{orb}+\mathrm{tr}_{orbit}\mathrm{Ric}_q,$$
since $\mathrm{tr}_{orbit}\mathrm{Ric}_g=(E_x-3)+(E_y-3)=E_{orb}-6$.

I recomputed the intrinsic orbit trace from the diagonal frame (independent of the script):
$$\mathrm{tr}_{orbit}\mathrm{Ric}_q=e^{-2a}\bigl(a_z\sigma_z-\sigma_z^2-\sigma_{zz}\bigr)=-e^{-a-\sigma}\partial_z\!\bigl(e^{\sigma-a}\sigma_z\bigr),$$
matching the script's `J_point_residual` and `J_divergence_expected` exactly. Weighted by $d\mu=e^{a+\sigma}dz$ this is $-\partial_z(e^{\sigma-a}\sigma_z)\,dz$, a pure $z$-derivative, so $\int\mathrm{tr}_{orbit}\mathrm{Ric}_q\,d\mu=0$ by periodicity. Hence (i). ✓

Worth recording: **the orbit-Ricci trace depends only on the orbit area $\sigma$, not on the shear $w$** (the $w$-terms cancel in the trace). So the "$\int\mathrm{tr}_{orbit}\mathrm{Ric}_q\,d\mu=0$" statement is genuinely area-only and should extend to a rotating (non-diagonal $M$) orbit frame, though the scripts verify only the diagonal/eigenframe-aligned case. This is the one place the general OT case (with $M$ off-diagonal) is not yet checked symbolically.

## 3. (ii) $I'=3V+\int R(q_r)\,d\mu-\int E_{zz}\,d\mu$ — correct

$I'=\int(a_{rr}+Ha_r)\,d\mu$, and the $z$-block evolution gives $a_{rr}+Ha_r=\mathrm{Ric}_q(e_z,e_z)-(E_{zz}-3)=R(q)-\mathrm{tr}_{orbit}\mathrm{Ric}_q+3-E_{zz}$. The extra $-\mathrm{tr}_{orbit}\mathrm{Ric}_q$ is the same $z$-divergence and integrates to zero, leaving (ii). I re-derived $R(q)=e^{-2a}(-2\sigma_{zz}+2a_z\sigma_z-\tfrac32\sigma_z^2-\tfrac12 w_z^2)$ from the diagonal sectional curvatures; matches the script's `Rq`. ✓

The script's finite-difference test is a genuinely independent confirmation: `I_prime_fd` differentiates $I=\int a_r e^{a+\sigma}dz$ numerically (no identity assumed) and matches `I_rhs_direct` built from the direct 4-D Ricci components to $1.4\times10^{-12}$ on a non-Einstein field; same for $J$ at $6\times10^{-12}$. This validates the entire evolution-equation chain, including the sign conventions.

## 4. (iii) The defect term is $\mathrm{tr}_{orbit}(E)-E_{rr}$, NOT $2E_{rr}-E_{zz}$ — the scripts' prose is inverted

This is the substantive correction. The contracted Gauss equation for the slice with unit normal $\partial_r$ is, with no approximation,
$$R(q)=R_g-2\,\mathrm{Ric}_g(\partial_r,\partial_r)+H^2-|S|^2.$$
Writing $R_g=\mathrm{tr}_g E-12$ and $\mathrm{Ric}_g(\partial_r,\partial_r)=E_{rr}-3$:
$$\boxed{\,R(q)=-6+H^2-|S|^2+\bigl(\mathrm{tr}_g E-2E_{rr}\bigr).\,}$$
The step82 scripts instead hard-code `Rq_ham = -6 + H^2 - |S|^2 + 2*Err`, i.e. they replaced $\mathrm{tr}_g E-2E_{rr}$ by $2E_{rr}$. That replacement is valid only on-shell ($E=0$); off-shell it is wrong by $\mathrm{tr}_g E-4E_{rr}$, which is exactly the nonzero `hamilton_residual` the script itself prints and the $0.3644$ integral residual it reports.

Substituting the correct Gauss identity into (ii):
$$I'\!/V=-3+2\,\mathrm{Cov}(u,v)+\tfrac12\langle v^2\rangle-\langle|B_0|^2\rangle+\langle E_{orb}-E_{rr}\rangle,$$
using $\mathrm{tr}_g E-2E_{rr}-E_{zz}=E_{orb}-E_{rr}$ and $H^2-|S|^2=2uv+\tfrac{v^2}{2}-|B_0|^2$. So the exact per-slice defect is $E_{orb}-E_{rr}=\mathrm{tr}_{orbit}(E)-E_{rr}$, the combination the scripts label "strategist-proposed" and reject.

**The script's own numerics confirm this and contradict its text.** In `step82_slice_balance.json`:
- `I_rhs_proposed_if_constraint = 0.06513607870995765` (uses $E_{orb}-E_{rr}$) matches `I_prime_fd = 0.06513607870850535` and `I_rhs_direct = 0.06513607870995486`;
- `I_rhs_turn_correct_if_constraint = -0.2993…` (uses $2E_{rr}-E_{zz}$) does **not** match $I'$.

Because the test field is arbitrary (polynomial in $r$, no field equation), the identity that holds for it is the geometric one, and it selects $E_{orb}-E_{rr}$. The JSON keys `correct_defect_from_hamilton = 2E_rr-E_zz` and `proposed_defect = E_orb-E_rr`, and the sentence "The Hamilton substitution gives 2E_rr-E_zz, not tr_orbit(E)-E_rr," are therefore reversed. `step82_geometric_balance_check.py` propagates the same wrong constraint but has no independent numerical test, so it merely re-derives the incorrect labeling. Any downstream note quoting "$2E_{rr}-E_{zz}$" as the turning defect (e.g. the strategist-formula-check verdict) should be re-signed to $\mathrm{tr}_{orbit}(E)-E_{rr}$.

## 5. First-return necessary inequality — correct, and robust to the §4 correction

At a reflected center $S(0)=0$ gives $I(0)=0$; with contraction $I$ dips below zero. If $I$ is $C^1$ and first returns to $0$ at $r_*$ from $I<0$, then $I(r_*)=0$ and $I'(r_*)\ge0$. At $I=0$, $\langle u\rangle_\mu=0$, so $\langle uv\rangle=\mathrm{Cov}(u,v)$ exactly. From $I'/V\ge0$ and $\langle E_{orb}-E_{rr}\rangle\le 3\delta$ (each orthonormal component of $E$ is a Rayleigh quotient bounded by $\|E\|_{op}\le\delta$; $|E_{orb}-E_{rr}|\le|E_x|+|E_y|+|E_{rr}|\le3\delta$):
$$2\,\mathrm{Cov}(u,v)+\tfrac12\langle v^2\rangle-\langle|B_0|^2\rangle\ \ge\ 3-3\delta.$$
Signs, differentiability, and the covariance reduction all check out. Crucially, the defect-form error of §4 does **not** touch this inequality: both $E_{orb}-E_{rr}$ and $2E_{rr}-E_{zz}$ carry the same operator-norm bound $3\delta$, so the threshold $3-3\delta$ is identical either way. The one place the correction would matter is any finer argument that uses the *directional structure* of the defect (e.g. one-sided control of $E_{rr}$ alone): there the two forms differ, and the correct $E_{orb}-E_{rr}$ must be used.

## 6. Do the balances bound $T=2\,\mathrm{Cov}(u,v)+\tfrac12\langle v^2\rangle-\langle|B_0|^2\rangle$ enough to prevent reversal? No.

- **Mean evolution only controls the mean.** With $y=J/V=\langle v\rangle$, $x=I/V$: $J'/V=6-\langle E_{orb}\rangle$, hence $y'=6-\langle E_{orb}\rangle-y(x+y)$, and at $x=0$, $y'\in[6-2\delta-y^2,\,6+2\delta-y^2]$. This bounds $\langle v\rangle$ but $\langle v^2\rangle=y^2+\mathrm{Var}(v)$ and $\mathrm{Cov}(u,v)$ are unconstrained by the linear balances; $\langle u^2\rangle$ never appears, so a moment closure does not exist at this order. The favorable term escapes through inhomogeneity.
- **Explicit favorable slices exist.** Taking $v=2\cos z$ (mean 0), $u=2\cos z$, $w_r=0$: $\mathrm{Cov}(u,v)=2$, $\tfrac12\langle v^2\rangle=1$, shear $0$, so $T=5\ge3$. This reproduces the covariance-model entry `turn_term=5.0` and confirms the 140-profile count: the integrated balances by themselves permit $T\ge3$, i.e. they do not obstruct reversal.
- **Slice compatibility ≠ dynamic reachability.** An algebraically favorable slice need not be reachable from a reflected $R(q_0)=-6$ center under the actual (near-)Einstein flow. The VII₀ collapse (Step 81) is precisely the demonstration that favorable algebraic states are available yet unreachable: the frozen angular momentum forces the orbit shear $|B_0|^2$ to grow, pushing $T$ down and driving finite-radius collapse. The reversal-preventing content, if any, lives in the shear budget, not in the balances.

**What an actual reversal-preventing bound would require** (none supplied by (i)–(iii)): control of $\mathrm{Cov}(u,v)$ and $\mathrm{Var}(v)$ by the orbit-map energy $\tfrac12|dU|^2_{H^2}$, the matrix Noether constraint $\mathcal Q(r)=\int\rho\,M^{-1}M_r\,dz\equiv0$ (which vanishes at reflection), and the base conformal/constraint equations (Step 79, (4.8)/(4.10)). The physical reading of the inequality is exact and useful: reversal of mean horizontal contraction demands that orbit-area expansion variance and its correlation with the $z$-direction shape ($2\,\mathrm{Cov}(u,v)+\tfrac12\langle v^2\rangle$) overcome the orbit shear $\langle|B_0|^2\rangle$ by at least $3-3\delta$. Whether the coupled system forces the shear to win (as in VII₀) or permits the Step 79 redistribution to make $T\ge3$ reachable remains the open dynamical question — the balances select this question but decide neither side.

## 7. Summary of what to fix and what stands

- Stands: definitions; $V'=I+J$; identity (i); identity (ii); the divergence-vanishing of $\int\mathrm{tr}_{orbit}\mathrm{Ric}_q\,d\mu$ (diagonal case, area-only); the necessary inequality $T\ge3-3\delta$ and its threshold; the compatibility-vs-reachability distinction; the $T\ge3$ profile existence.
- Needs correction in `step82_slice_balance_verify.py`, `step82_geometric_balance_check.py`, their JSON, and any downstream note: the Hamilton/Gauss constraint should read $R(q)=-6+H^2-|S|^2+(\mathrm{tr}_g E-2E_{rr})$, and the exact turning defect is $\mathrm{tr}_{orbit}(E)-E_{rr}$, not $2E_{rr}-E_{zz}$. The scripts' numerics already agree with this; only the labels/prose are inverted.
- Not yet checked: the orbit-trace divergence identity for a genuinely rotating (non-diagonal $M$) orbit frame — expected to hold because the trace is area-only, but the symbolic verification is diagonal.