#!/usr/bin/env python3
"""
Step 91: heat-regularized adjacent off-diagonal Green response in the mixed
AB one-form tensor sector.

This is not the complete Ozuch coefficient.  It is the corrected spectral
instrument for the sector in which the Step-87 axial mode lives, using:
  * quotient generator r_pi parity by azimuthal m, not by ell;
  * independent degrees ell_A, ell_B;
  * receiver/source weights from the Step-89/91 sparse odd functional;
  * heat regularization for the off-diagonal Green value.

The computed object is
    K_AB(τ; i,j) = (π²/2) Σ exp(-τ λ_P) R_i(ψ) R_j(ψ) /(λ_P ||ψ||²_quot)
over mixed one-form products ψ=α_A ⊙ β_B built from normalized scalar spherical
harmonics with |m|=0 or 2, since other m have zero Hessian at a pole and do not
enter the sparse receiver.  Exact and coexact one-form types are both included.
The source adjoint normalization S^1=(π²/2)R^1 is the principal normalization
established in Step 89/91; the singular source matching to Ozuch's full chart is
still separate.
"""
from __future__ import annotations

import json
import math
import pathlib
from dataclasses import dataclass
from typing import Literal

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

Node = Literal["N", "S"]
Kind = Literal["exact", "coexact"]

# Oriented tangent frame convention.  At S use global (X,-Y), so the frame is
# positively oriented with the outward normal at S.  Matrix J represents Hodge
# star on 1-forms: *(a dx + b dy)= -b dx + a dy.
J = np.array([[0.0, -1.0], [1.0, 0.0]])


@dataclass(frozen=True)
class OneFormJet:
    ell: int
    mode: str      # m0, c2, s2
    kind: Kind
    node: Node
    deriv: np.ndarray  # 2x2 matrix ∂_b alpha_a in local oriented frame
    scalar_lap: float  # ell(ell+1)


def scalar_hessian_coefficients(ell: int, node: Node):
    """Return normalized scalar harmonic Hessian matrices at a pole.

    Modes returned: m0 always; c2/s2 for ell>=2.  Real harmonics are L2-normalized
    on S^2.  At S, the local frame is (X,-Y), causing the sin(2φ) Hessian to gain
    an extra minus sign relative to the cos mode.
    """
    lam = ell * (ell + 1)
    out: list[tuple[str, np.ndarray]] = []

    # m=0: Y_l0 = sqrt((2l+1)/4π) P_l(cos θ), Hess_N = -C*λ/2 I.
    C0 = math.sqrt((2 * ell + 1) / (4 * math.pi))
    H0_N = -(C0 * lam / 2.0) * np.eye(2)
    sign0 = 1.0 if node == "N" else ((-1.0) ** ell)
    out.append(("m0", sign0 * H0_N))

    if ell >= 2:
        # Leading coefficient for real m=2 harmonics:
        # sqrt(2) * N_l2 * (l+2)!/[8(l-2)!] times (x^2-y^2) or 2xy.
        # Use logs to avoid overflow for larger ell.
        log_ratio = math.lgamma(ell + 3) - math.lgamma(ell - 1)  # log((l+2)!/(l-2)!)
        A2 = math.exp(log_ratio) / 8.0
        Nl2 = math.sqrt((2 * ell + 1) / (4 * math.pi) * math.exp(math.lgamma(ell - 1) - math.lgamma(ell + 3)))
        b = math.sqrt(2.0) * Nl2 * A2
        Hc_N = np.array([[2 * b, 0.0], [0.0, -2 * b]])
        Hs_N = np.array([[0.0, 2 * b], [2 * b, 0.0]])
        sign_c = 1.0 if node == "N" else ((-1.0) ** ell)
        sign_s = 1.0 if node == "N" else (-((-1.0) ** ell))  # local Y coordinate flips at S
        out.append(("c2", sign_c * Hc_N))
        out.append(("s2", sign_s * Hs_N))
    return out


def oneform_jets(ell: int, node: Node) -> list[OneFormJet]:
    lam = ell * (ell + 1)
    jets: list[OneFormJet] = []
    for mode, H in scalar_hessian_coefficients(ell, node):
        jets.append(OneFormJet(ell, mode, "exact", node, H.copy(), lam))
        jets.append(OneFormJet(ell, mode, "coexact", node, J @ H, lam))
    return jets


def receiver_from_deriv(A: np.ndarray, B: np.ndarray) -> float:
    """Sparse odd receiver for h=alpha_A⊙beta_B.

    A[a,b]=∂_b alpha_a, B[mu,nu]=∂_nu beta_mu in local oriented frames.
    R_odd=-1/2(A_01 B_10 + A_10 B_01).
    """
    return -0.5 * (A[0, 1] * B[1, 0] + A[1, 0] * B[0, 1])


def sector_sum(Lmax: int, tau: float, pair: str = "adjacent_NS") -> dict:
    # pair choices are receiver NN and source node: NN(self formal), NS(adjacent B), SN(adjacent A), SS(opposite corner).
    # Only separated pairs should be interpreted as finite Green values; self is listed only for heat behavior.
    recA, recB = "N", "N"
    if pair == "NN":
        srcA, srcB = "N", "N"
    elif pair == "NS":
        srcA, srcB = "N", "S"
    elif pair == "SN":
        srcA, srcB = "S", "N"
    elif pair == "SS":
        srcA, srcB = "S", "S"
    else:
        raise ValueError(pair)

    # Precompute local one-form jets.
    jets = {(ell, node): oneform_jets(ell, node) for ell in range(1, Lmax + 1) for node in ["N", "S"]}

    total = 0.0
    axial_l1 = 0.0
    by_type: dict[str, float] = {}
    by_mode_pair: dict[str, float] = {}
    shell_tail_abs_last10 = 0.0
    shell_contribs = []

    for ellA in range(1, Lmax + 1):
        shell = 0.0
        lamA_scalar = ellA * (ellA + 1)
        for ellB in range(1, Lmax + 1):
            lamB_scalar = ellB * (ellB + 1)
            lamP = 0.5 * (lamA_scalar + lamB_scalar) - 1.0
            heat = math.exp(-tau * lamP)
            norm_quot = lamA_scalar * lamB_scalar  # for normalized scalar harmonics; quotient halves 2*norms
            pref = (math.pi ** 2 / 2.0) * heat / (lamP * norm_quot)
            pair_sum = 0.0
            for ja_r in jets[(ellA, recA)]:
                for jb_r in jets[(ellB, recB)]:
                    Rr = receiver_from_deriv(ja_r.deriv, jb_r.deriv)
                    if abs(Rr) < 1e-15:
                        continue
                    # Same global harmonic label at source; only node changes.
                    for ja_s in jets[(ellA, srcA)]:
                        if ja_s.mode != ja_r.mode or ja_s.kind != ja_r.kind:
                            continue
                        for jb_s in jets[(ellB, srcB)]:
                            if jb_s.mode != jb_r.mode or jb_s.kind != jb_r.kind:
                                continue
                            Rs = receiver_from_deriv(ja_s.deriv, jb_s.deriv)
                            if abs(Rs) < 1e-15:
                                continue
                            val = pref * Rr * Rs
                            pair_sum += val
                            key = f"{ja_r.kind}-{jb_r.kind}"
                            by_type[key] = by_type.get(key, 0.0) + val
                            mkey = f"{ja_r.mode}-{jb_r.mode}:{key}"
                            by_mode_pair[mkey] = by_mode_pair.get(mkey, 0.0) + val
                            if ellA == 1 and ellB == 1 and ja_r.mode == "m0" and jb_r.mode == "m0" and ja_r.kind == "coexact" and jb_r.kind == "coexact":
                                axial_l1 += val
            total += pair_sum
            shell += pair_sum
        shell_contribs.append(shell)

    if Lmax >= 10:
        shell_tail_abs_last10 = float(sum(abs(x) for x in shell_contribs[-10:]))

    return {
        "pair": f"receiver_NN_source_{pair}",
        "Lmax": Lmax,
        "tau": tau,
        "K_AB_heat": total,
        "axial_l1_contribution": axial_l1,
        "by_oneform_type": dict(sorted(by_type.items())),
        "largest_mode_pair_contributions": dict(sorted(by_mode_pair.items(), key=lambda kv: -abs(kv[1]))[:12]),
        "last_10_ellA_shell_abs_sum": shell_tail_abs_last10,
        "note": "AB mixed one-form sector only; heat regularized; uses principal S=(pi^2/2)R normalization. Self pair is singular as tau->0 and not a finite off-diagonal value.",
    }


def main():
    # A ladder showing heat convergence for the adjacent and symmetry-related separated pairs.
    L_for_tau = {0.2: 80, 0.1: 100, 0.05: 140, 0.02: 220, 0.01: 320, 0.005: 480, 0.003: 650}
    adjacent_ladder = []
    for tau, L in L_for_tau.items():
        adjacent_ladder.append(sector_sum(L, tau, "NS"))

    # Pair class comparison at a fixed conservative heat cutoff.
    class_tau = 0.01
    class_L = 360
    pair_classes = [sector_sum(class_L, class_tau, p) for p in ["NS", "SN", "SS"]]

    # Formal self heat behavior at larger tau only, to document non-finite nature without driving divergence.
    self_heat = [sector_sum(80, tau, "NN") for tau in [0.2, 0.1, 0.05]]

    results = {
        "step": 91,
        "scope": "corrected heat-regularized adjacent Green response in AB one-form sector",
        "normalization": {
            "receiver": "R_odd=-1/2(A_01 B_10 + A_10 B_01) for h=alpha_A sym beta_B",
            "source_receiver_adjoint_principal": "S_odd=(pi^2/2) R_odd, from Step89/91 sparse identity",
            "norm_on_quotient": "||alpha_A sym beta_B||^2_{quot}=ell_A(ell_A+1) ell_B(ell_B+1) for L2-normalized scalar harmonics",
            "P_eigenvalue": "lambda_P=(ell_A(ell_A+1)+ell_B(ell_B+1))/2 - 1 for mixed one-form products",
            "quotient_descent": "only azimuthal m parity matters under r_pi; the Hessian-supported modes m=0,2 automatically have even m_A+m_B",
            "degrees": "ell_A and ell_B are independent; no ell_A=ell_B restriction is imposed",
        },
        "adjacent_NS_heat_ladder": adjacent_ladder,
        "pair_class_comparison_tau_0p01": pair_classes,
        "formal_self_heat_samples": self_heat,
        "interpretation": [
            "For receiver NN and source NS, the AB one-form sector stabilizes near a negative value about -3.14e-2 as tau decreases in this normalization.",
            "The axial ell=1 m=0 coexact-coexact term alone contributes -9/128 to the adjacent coefficient; higher one-form modes partly cancel it but do not cancel it completely in this sector.",
            "This is still not the full Ozuch adjacent coefficient: AA/BB trace-free tensor sectors, gauge/Bianchi source matching, and sharp heat-kernel error control remain to be derived.",
            "The computation obeys the corrected spectral rules: m-parity for quotient descent, independent degrees, factor trace-free eigenvalue correction kept out of this AB-only sector, and heat regularization rather than ordinary cutoff convergence.",
        ],
    }

    outpath = DATA_DIR / "step91_adjacent_ab_heat_spectral.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    main()
