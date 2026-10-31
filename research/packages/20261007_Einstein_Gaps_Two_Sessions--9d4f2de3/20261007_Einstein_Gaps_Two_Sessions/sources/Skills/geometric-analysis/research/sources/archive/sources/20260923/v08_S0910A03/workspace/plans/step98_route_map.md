# Step 98 route map: resolution-continuable full-matrix matching

## What changed

The Step 97 cosh trial is retained only as an exterior warped-product benchmark.
It does not retain the charged Koiso Weingarten tensor and does not lower the
whole-cylinder defect. The claimed orbit roots `0,-2`, diagonal center trial,
coordinate-norm residual ranking, conjugate-point interpretation, and
coordinate-repair conclusion are withdrawn; see
`workspace/notes/step98_full_matrix_matching_pressure_test.md`.

The active object is now a full `3 x 3` SPD logarithmic-matrix field on both
sides of one charged Koiso center. The implementation evaluates all ten Ricci
blocks and the generalized-eigenvalue operator norm. Exact center jets are
known analytically. A coarse direct nodal trial shows large discrete
compensability, but it does not preserve the true endpoint jets after
optimization and has not survived refinement.

## Immediate construction work

1. Replace the direct nodal parametrization by a nested, analytically
   jet-preserving form `X=H_R+w_R Y` on one signed cylinder. Use spectral
   elements of fixed physical width, with `w_R` vanishing through order two at
   the center and both endpoints. Do not overwrite derivative arrays.
2. Freeze analytic Step 94 `q0,K0` once and sample it at every Fourier
   resolution. Start with `Ns=48,64,96,128`; increase radial resolution so
   physical grid spacing is fixed.
3. Store every accepted coefficient vector and evaluate it on independent
   shifted/padded grids at `3x` resolution. Record `E_nn`, `E_ni`, `E_T`,
   operator sup, `L^2,L^4,L^8,L^16`, Fourier/Chebyshev tails, and minimum SPD
   eigenvalue. A coarse decrease without fine-grid decrease is discarded.
4. Give the outer attachment a genuinely exact flat-torus expanding region,
   or retain and subtract the explicit inherited term
   `e^{-2R} ||q0^{-1/2} Ric(q0) q0^{-1/2}||`.
5. Once one fixed `R` sequence converges, continue in `R` with warm starts and
   fixed physical resolution. Track whether the residual stays centered,
   escapes to the ends with a known indicial rate, or develops cutoff-scale
   oscillations.

## Linearized interpretation

At each resolved trial, use quadrature/volume mass matrices and the physical
metric on variations. For singular fields compute their residual pairing,
required correction `|<u,F>|/s`, and physical inverse scale. Decompose left
fields by Ricci block and target Fourier mode. A meaningful obstruction would
be a low-frequency centered adjoint field that persists under resolution and
`R`, pairs nontrivially with the residual, and is inaccessible to all shared
center/end parameters. A small raw nodal singular value alone means nothing.

## Scope

No continuous connector or negative-branch counterexample has been obtained.
The positive branch, no-Einstein topology on a fixed closed manifold, higher
dimensions, and Lean formalization remain separate unresolved parts of Yau 26.
