# Route assessment after Step 24

## Main correction

Step 23's dissipation-locality finding remains valuable, but its maximal-net
repair is not an established input for the actual selected maximal-function
support construction.  A maximal `r`-net on all of `M` includes bad centers, and
the global curvature budget does not make

\[
A_\alpha^2\|F\|_{L^2(U_\alpha)}
\]

small at every such center.  The Step 23 graph theorem is therefore conditional
on all-center smallness; it does not replace Li's all-center hypothesis for the
LeBrun sequence.

## New selected-support formulation

Step 24 developed the buffered selected-support alternative.  On a support
chosen from one maximal-function good center `p`, use a physical cutoff `chi`
with `a=chi^2` and an auxiliary energy cutoff `eta` satisfying

\[
\operatorname{supp}\chi\Subset\{\eta=1\}\Subset\Omega_\eta,
\qquad \operatorname{supp}\nabla\eta\subset\{\chi=0\}^{\circ}.
\]

Thus

\[
a|\nabla\eta|^2=0,
\qquad \nabla a\cdot\nabla\eta=0,
\qquad \operatorname{supp}a\subset\{\eta=1\},
\]

and the collar where `grad eta` lives is exactly stationary because `a=0` there.
This is a coefficient-support fact, not finite propagation.  The entire active
transition of `chi` is included in the energy domain.

The good-center hypothesis gives

\[
H_2(0)=\int\eta^2F^2\le(1+K_0)\operatorname{Vol}(\Omega_\eta),
\qquad
\beta_0=A_\Omega^2H_2(0)^{1/2}\le C(L_\eta)r^2\sqrt{1+K_0},
\]

so collapsed volume cancels on the selected support itself.  The scale `r` must
be chosen after fixed support ratios and tensor constants.

## Verified algebra and repairs

Scripts:

- `workspace/scripts/step24_buffered_support_algebra.py` ran successfully.  With
  sample constants it shows the inherited `r=0.003` is too large for absorption
  (`C beta/c=1.53`) and computes a smaller sample radius `r=1.713e-3` with
  `beta=0.025`.  It confirms support cancellations, `A^4 int int aF^3 ~ beta^3`,
  time-average propagation scale `A^4H_3(t) ~ beta^3/t`, and triangular `Q`
  amplification.
- `workspace/scripts/step24_support_tensor_monomials.py` ran successfully and
  verifies the correct Sobolev variables: `chi F` for q=2, `a F^{3/2}` for q=3,
  and `chi E` for the defect potential.  It also shows the wrong variable
  `chi F^{3/2}` factors `aF^4`, not the actual `a^2F^4`, and its cutoff term
  lacks an `a` factor.
- `workspace/scripts/step24_packing_coloring.py` ran successfully and gives a
  crude collapse-free packing/coloring constant: selected disjoint supports can
  retain a fixed, though tiny, volume fraction if the good set has fixed volume
  proportion.

TTCS verification (`trace/ttcs/results/step24_ttcs01_verifier1_integration.md`)
supported the buffered-support repair and supplied two corrections now included
in the note: use the active parameter
`beta_a=A^2||F||_{L^2(supp chi)}`, and replace the first q=3 Riccati estimate by
linear critical absorption with `u=aF^{3/2}`.

## Current conditional energy chain

Subject to exact tensor inequalities and evolving Sobolev control on one
selected support:

1. q=2:
   \[
   H_2'+cD_2\le C\int aF^3+Cr^{-2}H_2,
   \quad \int aF^3\le C\beta_a(D_2+r^{-2}H_2),
   \]
   hence `H_2` persists and `int D_2` is controlled.
2. Weighted cubic:
   \[
   A_\Omega^4\int_0^T\int aF^3\le C\beta_*^3.
   \]
3. q=3:
   \[
   Y'+cD_3\le Cr^{-2}Y+C\int a^2F^4,
   \quad \int a^2F^4\le C\beta_a(D_3+r^{-2}Y),
   \]
   giving `A^4Y(t) <= C beta^3/t` by time averaging and forward propagation.
4. Defect:
   \[
   Q'+cX\le Cr^{-2}Q+C\int aF|E|^2,
   \quad \int aF|E|^2\le C\beta_a(X+r^{-2}Q),
   \]
   so `Q` propagates triangularly with no curvature-only source.

## What remains load-bearing

- Exact tensor proof of the q=2 inequality under `partial_t g=-2a(Ric+g)`, with
  metric-norm, volume-form, algebraic curvature, `nabla a`, and `nabla^2a`
  terms.
- Exact tensor proof of the q=3 weighted inequality with dissipation weight
  `a^2F|nabla Rm|^2` and reaction `a^2F^4`.
- Exact homogeneous defect energy inequality for `E=Ric+g`; confirm there is no
  independent `(nabla^2a)*g` source after combining Ricci and normalization.
- Evolving Sobolev constants, cutoff-gradient bounds, and uniform smooth
  existence/metric comparability on `[0, theta r^2]`. Critical energy persistence
  alone does not give these.
- The density bridge: selected disjoint plateaux have fixed volume proportion,
  but final topological recalibration needs enough smoothed plateau mass with
  small Step 8 tensor-defect densities and normalized `Q/A -> 0` in the region
  used for exponential-pullback/Derdziński.

## Parallel work started

A bounded Codex worker was initialized and started in exec mode to independently
derive the index-level tensor energy inequalities.  Proposal:
`workspace/codex_loop/Research_Project_Proposal.md`.  Later agent should check
status once; if succeeded, read `workspace/codex_loop/Research_Report.md` and
`workspace/codex_loop/work/tensor_energy_derivation.md` before relying on it.

## Scope

Even a successful support-local smoothing theorem would still address only the
critical four-dimensional negative LeBrun/Ishida-LeBrun laboratory.  It does not
settle the positive branch, arbitrary four-dimensional manifolds, dimensions
`n>=5`, the full Yau 26 proposition, or Lean formalization.
