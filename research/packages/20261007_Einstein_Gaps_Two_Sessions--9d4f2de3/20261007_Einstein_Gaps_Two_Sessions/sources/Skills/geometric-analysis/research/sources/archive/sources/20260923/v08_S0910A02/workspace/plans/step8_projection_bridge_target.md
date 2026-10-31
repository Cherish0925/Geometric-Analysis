# Step 8 bridge target: C0 Ricci pinching to first-obstruction projection

Session: S0910A02. Agent4/Preceptor. Phase: Explore handoff material.

## Purpose

The Step-7 obstruction-amplitude argument is rigorous only inside the Biquard--Ozuch/Eguchi--Hanson gluing normal form.  To use it for Yau 26, we need a replacement that starts from the actual hypothesis

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty(g_i),op}\le \delta_i\to0
\]

and does not assume the metrics are exact Einstein or already produced by gluing.  The target is a local projection/Pohozaev/Komar identity in which the Ricci defect appears only under an integral against smooth test data.  Then no derivative bound on the defect is required.

## Model theorem template

Work first in the four-dimensional positive normalized branch near one suspected `R^4/Z_2` concentration point.  Assume a sequence admits a two-scale description sufficient to make the following objects meaningful:

1. an outer orbifold scale converging in `C^{1,alpha} cap W^{2,p}` (and smoothly away from the point if available) to an Einstein orbifold metric `g_0` with `Ric(g_0)=g_0`;
2. an inner scale `t_i` such that `(M_i,t_i^{-1}g_i,p_i)` converges on compact subsets to Eguchi--Hanson `(Y,h_EH)`;
3. a neck annulus where approximate Bianchi/ALE coordinates identify both expansions with controlled errors;
4. a cutoff approximate cokernel tensor `phi_i`, transported from the decaying Eguchi--Hanson infinitesimal Einstein deformation/obstruction mode and supported on the core+neck.

Desired identity:

\[
\int_{\Omega_i}\langle \operatorname{Ric}(g_i)-g_i,\phi_i\rangle_{g_i}\,d\mu_{g_i}
= t_i\,\mathcal O\big(R_+(p),\text{orientation},\text{EH rotation}\big)+o(t_i). \tag{1}
\]

The obstruction term should vanish for every allowed rotation exactly when `R_+(p)` has the required kernel (equivalently, in the first-order `R^4/Z_2` case, when the Biquard--Ozuch determinant/projection obstruction vanishes in the gluing orientation).  The target is not yet Kähler-Einstein selection; `det R_+=0` is only first-order degeneracy.

## Why C0 Ricci control is enough if (1) is proved

The scaling in the Eguchi--Hanson core is `g_i ~ t_i h_EH`.  For a `(0,2)` tensor `phi_i` corresponding to a fixed model tensor `phi` on EH,

\[
|\phi_i|_{g_i}\sim t_i^{-1}|\phi|_{h_{EH}},
\qquad d\mu_{g_i}\sim t_i^2 d\mu_{h_{EH}}.
\]

Thus, on a fixed EH core,

\[
\|\phi_i\|_{L^1(g_i)}=O(t_i).
\]

The same scale should remain true after adding a controlled cutoff on the neck; this must be verified with the actual decay of the obstruction/cokernel mode.  Consequently the Yau-26 hypothesis gives

\[
\left|\int\langle \operatorname{Ric}(g_i)-g_i,\phi_i\rangle\right|
\le \delta_i\|\phi_i\|_{L^1(g_i)}=O(\delta_i t_i).
\]

Dividing (1) by `t_i` would force

\[
\mathcal O\big(R_+(p),\text{orientation},\text{rotation}\big)=O(\delta_i)+o(1),
\]

hence the first obstruction vanishes in the limit.  This is exactly the C0 version of the obstruction-amplitude principle.

## Analytic mechanism to derive (1)

Two equivalent formulations should be explored.

### A. Self-adjoint linearized Einstein projection

Let

\[
\Phi_g(h)=\operatorname{Ric}(g+h)-g-h+\text{Bianchi gauge correction}
\]

or the corresponding fixed-Einstein-constant operator.  Its linearization in Bianchi gauge is formally self-adjoint.  If `phi` is a decaying element of the ALE kernel/cokernel, integrate the equation against a cutoff of `phi`.  The interior term should be the obstruction coefficient; all derivatives of the metric error should be moved onto smooth model fields and boundary terms.

What must be computed:

* the exact normalization of the EH obstruction mode;
* the boundary terms on the inner and outer annular hypersurfaces;
* the scale at which the orbifold curvature term `R_+(p)` enters;
* the cutoff errors and their dependence on the annular ratio;
* the effect of changing EH rotation/orientation.

### B. Komar/rotation-field flux

Let `X` be a rotation field of the cone `R^4/Z_2`, transported as an approximate Killing field on the neck.  For an exact Killing field one has, up to sign convention,

\[
d(*dX^\flat)=2*\operatorname{Ric}(X,\cdot).
\]

For an Einstein metric `Ric=\lambda g`, the right-hand side is explicit and can be subtracted or included as a known volume term.  For `Ric=g+E`, the defect contribution is

\[
2*E(X,\cdot),
\]

which is bounded by `delta_i` times annular geometric data.  Comparing inner and outer flux asymptotics should reproduce the same first obstruction as Biquard/Ozuch.  This formulation may avoid constructing the full weighted gluing normal form but still requires enough `C^{1,alpha}` control to evaluate the flux and approximate Killing error.

## Failure modes to keep explicit

1. The sequence may not have a clean two-scale EH bubble; there may be bubble trees or different ALE spaces.
2. A collapsed region may not unwrap to a noncollapsed annulus with controlled deck-averaged defect.
3. The test tensor may have larger neck `L^1` norm than `O(t_i)` if the decay/cutoff is mishandled.
4. `det R_+=0` is weaker than Hermitian/Kähler-Einstein geometry; extra rigidity requires source hypotheses such as LeBrun--Ozuch admissibility and exact Einstein metrics.
5. First-obstruction vanishing does not imply existence of an Einstein metric on the smooth topology; higher-order and global obstructions remain.
6. General dimensions require a different obstruction functional (Yao-type contraction of orbifold Weyl with ALE asymptotic Weyl plus renormalized volume) and currently apply only to negative exact Einstein resolution sequences.

## Next work for Agent2

Derive (1) in the simplest controlled setting: one `R^4/Z_2` singularity, one Eguchi--Hanson bubble, no deeper trees, positive normalization `Ric≈g`, and a fixed annulus whose metric is assumed close to the glued model.  It is acceptable to state the required annular closeness as an explicit hypothesis first.  The goal is to verify the scale `LHS=O(delta t)` and identify the leading obstruction coefficient algebraically; this would turn the Step-7 amplitude heuristic into a theorem template that later can be connected to Cheeger--Naber/Naber--Zhang compactness and collapse-unwrapping.
