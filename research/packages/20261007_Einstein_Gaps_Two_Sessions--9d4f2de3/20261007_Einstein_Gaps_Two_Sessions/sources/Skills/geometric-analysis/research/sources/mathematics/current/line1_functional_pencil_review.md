# Independent proof review

23 September 2026. Reviewer: the separate `line1_direction_review`
agent. The review concerns the present functional manuscript, not all
historical results in the repository.

## Main argument

The reviewer read the original 447-line manuscript (SHA-256
`120064f7fa83903e03e816207a319db28a2e3d5af0e014bc383960df23f7c2df`)
and found no mathematical error in its new argument, conditional on the
inherited bounded-form compatibility theorem and bundle Hessian estimate.
The checks covered the signed deficit decomposition, cutoff costs,
actual versus ideal curvature moments, simultaneous amplitude and Weyl
direction fitting, second-order budget, square-cost reduction, large
defect case, and endpoint normalizations.

Eight independent SymPy identities were checked without calling the
author's checker: the functional square split, form normalization,
arbitrary-direction Weyl identity, beta-two and beta-eight identities,
KE endpoint order, classical lower-parameter bound, and the hypothetical
topological ratio. All residuals were zero. These are algebra checks,
not verification of gauge solvability.

The review requested two clarifications, now included: absorption of
the bounded beta-fourth factor in the main estimate, and compatibility
with the chosen Spin-c structure in the cscK equality statement.

## Added harmonic-alignment theorem

The reviewer separately read the subsequently added Section 7 (manuscript
SHA-256 `13f0324dab4999ffba998cd60e8a1d8c152b97aae6f40218aca599230c4201ae`) and
checked its cross-references and equations 1–29. The harmonic coefficient
`-3*pi*beta/(beta+1)`, curvature remainder `4*S/9`, canonical alignment
constant 49, derivative estimate `13*kappa + 4*sqrt(2*kappa)`, exterior
derivative bound `13*kappa/2`, and spectral-tail bound all checked out.
The intermediate weight estimate is conservative. The proof does not
assume that the harmonic representative has a maximum bound.

The bounded-form derivative estimate initially applies at small
calibration error; the remaining compact defect range is correctly
handled by the integrated Hodge identity. The second-order square cost
does not enter the stronger endpoint first-derivative estimate.

## Literature and scope

Exact Einstein saturation implying KE is already LeBrun's Corollary 2.5.
The new statement is quantitative functional non-saturation under
integral Ricci error and an explicit square budget. The classical
scalar and scalar–Weyl constraints already give the sharper elementary
bound for beta at most two. Their relaxed moment constraints do not
eliminate the formal beta-greater-than-two calibrations.

This comparison is not an exhaustive novelty audit. The formal
calibration data used to compare beta-eight with other parameters do
not assert existence of metrics realizing those data. No new
topological Einstein obstruction follows without additional application
input.
