# Step 24: j=1 angular second variation after Yamabe normalization and gauge resolution

Script: `workspace/scripts/angular_normalized_gauge.py`; check: `workspace/scripts/check_bianchi_delta.py`.
Base: `data/perp_direct/lm3_x00.038_X512_d28.json` (x0=.038, X=512). Data: `data/angular_isotype/ng*_*.json`.

## 1. Exact normalized second variation
At a base with s=-24, B=-Δ, σ=Ds[h], the Yamabe-normalized path (u→1 on the CH end) has
Qn(h)=Q_J(h)-D(h), D=(2/3)<σ,(B+6)(B+8)^{-1}σ>=(2/3)(|σ|²-2<σ,(B+8)^{-1}σ>), v=-(1/6)(B+8)^{-1}σ, tangent T=h+2vg.
Bounds: Q_J-(2/3)|σ|² ≤ Qn ≤ Q_J-(1/2)|σ|².
(B+8)^{-1} is solved per angular column by P2 finite elements on the cell plus an exact-CH extension to 100X
(G=x+x², h=diag(x,x,x(1+x)); coefficients continuous at X to 1e-9). σ is exactly in span{F_b} (residual 2e-14).

Checks: pure-trace modes φg have Qn/Q_J ≈ 1e-5 (r4, nel48 nq8) — exact zero expected; v(KX)=divX/4 for
KX=L_Xg-½divX g with median relative error 0.4–0.7% (large relative errors only on modes with divX≈0);
δ and Bianchi map verified: δ(φg)=-dφ and β(L_Xg)=-ΔX-Ric X to 1e-14.
Negative Qn on some KX modes (up to -5) are cancellation errors of 1e-5–6e-4 relative to Q_J≈D≈1e5 on
radial-vector gauge modes with large divX; they are not physical.

## 2. Correction of the angular multiplicity (affects Steps 22–23)
In the euler_E/ad_row0 convention left-invariant vector fields act on the ROW index of R=Rz(ψ)Ry(θ)Rz(φ).
A fixed row is one irreducible copy of the left j=1 representation (angular Laplacian scalar on it: all three
entries gave -0.0078277=-4(2+x)/(x(1+x)) at x=512; σ of row-built seeds has 42% outside the row span).
The genuine multiplicity space is a fixed COLUMN (Laplacian diagonal with distinct entries, e.g. at x=10:
-0.4366,-0.4387,-0.8022, matching CH values 4(2+x)/(x(1+x)) and 8/x). The Step-22/23 'fullmult' runs were
compressions to one copy; their threefold spectra are Schur multiplicity. With columns the spectra are no longer tripled.

## 3. Results (trace-free seeds, 9 tensors × 3 columns × nrad localized C^∞ bumps, u-support [0,0.9])
| nrad | raw min | normalized min | finite-gauge quotient | Bianchi-kernel Ritz |
|---|---|---|---|---|
| 2 | 0.1771 | 0.1379 | 0.380 | 92.6 |
| 4 | 0.0823 | 0.0589 | 0.147 | 192.5 |
| 6 | 0.0474 | 0.0350 | 0.095 (0.105 with nvec 9) | 305.6 |
| 8 | 0.0319 | 0.0253 | 0.076 | 453.1 |
| 10 (nvec 6) | — | 0.0204 | 0.090 | — |

All Qn eigenvalues in every tested space are positive: no descending normalized j=1 direction exists in these spaces.
The falling low values are gauge-dominated: Bianchi ratio |β(T)|²/|T|² of the lowest modes ≈10–15, the same
order as genuine gauge tangents (14–26), while the tf span contains essentially Bianchi-free tensors (ratio ~1e-3);
GT-overlap of lowest modes with the finite K X span 65–98%. The Bianchi-kernel Ritz values grow with nrad, so they are
fine-scale artifacts of the numerical kernel, not a converged physical gap. The physical slice bottom is therefore
not determined (bracketed only loosely). The strategist bounds are not decisive here: |σ|² ≫ Q_J for frame-tensor
seeds (lower bound strongly negative), while the upper bound stays positive.

## 4. Remaining
A converged physical j=1 bottom needs a slice-adapted basis (e.g. parametrize TT/Bianchi-free tensors directly by
solving the radial constraint ODE, or a gauge-fixed operator Qn+c|β|² with c chosen above the lifted gauge band and
convergence in nrad), plus higher isotypes j≥2 and the Ward term of the nearly stationary base. None of this changes
the unrestricted Einstein-gap problem: the cell branch is locally free of tested angular instabilities only.
