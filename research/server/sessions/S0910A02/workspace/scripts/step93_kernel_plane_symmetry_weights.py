"""
Step 93: preliminary kernel-plane symmetry weights for the product mirror.

This is an organizational algebra check, not a physical Ozuch coefficient.  It
fixes a natural local pole-frame convention and computes how rotations around
the two sphere axes act on the chiral kernel planes at the four A1 nodes.

Convention: local oriented tangent frames at N and S are chosen so that an axis
rotation by angle theta acts by R(theta) at N and by R(-theta) at S.  If s_N=+1,
s_S=-1, local rotation angles are a=s_A alpha and b=s_B beta.  On Lambda^+ the
kernel plane rotates by a+b, while on Lambda^- it rotates by a-b.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step93_kernel_plane_symmetry_weights.json"

nodes = {
    "NN": (+1, +1),
    "NS": (+1, -1),
    "SN": (-1, +1),
    "SS": (-1, -1),
}

patterns = {
    "diagonal_balanced_plus_NN_SS": {"NN": "+", "SS": "+", "NS": "-", "SN": "-"},
    "adjacent_balanced_plus_NN_NS": {"NN": "+", "NS": "+", "SN": "-", "SS": "-"},
    "all_plus": {"NN": "+", "NS": "+", "SN": "+", "SS": "+"},
}


def weight(sA: int, sB: int, chirality: str):
    # theta = coeff_alpha * alpha + coeff_beta * beta
    eps = +1 if chirality == "+" else -1
    return (sA, eps * sB)


def weight_str(w):
    a, b = w
    def term(c, name):
        if c == 1:
            return name
        if c == -1:
            return f"-{name}"
        return f"{c}{name}"
    if b == 1:
        return f"{term(a,'α')}+β" if a != 0 else "β"
    if b == -1:
        return f"{term(a,'α')}-β" if a != 0 else "-β"
    return term(a, "α")

results = {
    "purpose": "Pin down natural SO(2)_A x SO(2)_B characters on kernel planes for product A1 nodes.",
    "frame_convention": {
        "N": "axis rotation acts by R(θ) on the local oriented tangent frame",
        "S": "axis rotation acts by R(-θ) using the oriented frame (x,-y)",
        "Lambda_plus_kernel_angle": "a+b for local factor angles a,b",
        "Lambda_minus_kernel_angle": "a-b for local factor angles a,b",
        "formula": "θ_j = s_A α + eps(chirality) s_B β, eps(+)=+1, eps(-)=-1",
        "warning": "Changing pole-frame conventions conjugates signs; physical computations must calibrate on r=0 KE row. H^4(ξ)=H^4(-ξ), so projective signs are partly redundant.",
    },
    "node_weights": {},
    "patterns": {},
}

for node, (sA, sB) in nodes.items():
    results["node_weights"][node] = {
        "pole_signs": {"s_A": sA, "s_B": sB},
        "plus_weight": weight_str(weight(sA, sB, "+")),
        "minus_weight": weight_str(weight(sA, sB, "-")),
        "plus_coefficients_alpha_beta": weight(sA, sB, "+"),
        "minus_coefficients_alpha_beta": weight(sA, sB, "-"),
    }

for pname, patt in patterns.items():
    entries = {}
    chars = {}
    for node, chi in patt.items():
        sA, sB = nodes[node]
        w = weight(sA, sB, chi)
        entries[node] = {"chirality": chi, "weight": weight_str(w), "coefficients_alpha_beta": w}
        chars.setdefault(w, []).append(node)
    results["patterns"][pname] = {
        "entries": entries,
        "distinct_characters": {weight_str(k): v for k, v in chars.items()},
        "interpretation": "For diagonal balanced, all nodes have weights ±(α+β), so a common SO(2) character is plausible after projectivizing/sign transport; for adjacent balanced, both α+β and α-β characters occur, so a single isotropic scalar reduction is less automatic.",
    }

# Basic pair character products for diagonal pattern: whether source quadratic and receiver Sym(K) can share character.
diag = patterns["diagonal_balanced_plus_NN_SS"]
pair_data = []
for i, chi_i in diag.items():
    for j, chi_j in diag.items():
        if i == j:
            continue
        wi = weight(*nodes[i], chi_i)
        wj = weight(*nodes[j], chi_j)
        # Sym^2 of a weight w real 2D rep has trivial + character 2w;
        # Sym(K_j) has trivial + character 2wj.
        same_anisotropic_character = (2*wi[0], 2*wi[1]) == (2*wj[0], 2*wj[1]) or (2*wi[0], 2*wi[1]) == (-2*wj[0], -2*wj[1])
        pair_data.append({
            "source": i,
            "receiver": j,
            "source_chirality": chi_i,
            "receiver_chirality": chi_j,
            "source_weight": weight_str(wi),
            "receiver_weight": weight_str(wj),
            "same_chirality": chi_i == chi_j,
            "anisotropic_characters_match_up_to_sign": same_anisotropic_character,
            "warning": "Character match is necessary but not sufficient for a nonzero physical Q_ji; full Green/slice/frame computation is required.",
        })
results["diagonal_balanced_pair_character_checks"] = pair_data

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Saved {OUT}")
print("Diagonal balanced weights:")
for node, entry in results["patterns"]["diagonal_balanced_plus_NN_SS"]["entries"].items():
    print(f"  {node} {entry['chirality']}: {entry['weight']}")
print("Adjacent balanced weights:")
for node, entry in results["patterns"]["adjacent_balanced_plus_NN_NS"]["entries"].items():
    print(f"  {node} {entry['chirality']}: {entry['weight']}")
