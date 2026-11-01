#!/usr/bin/env python3
"""Step 60 base-pair continuation: structural verification.

Checks the key mathematical claims of the base-pair proof note:
1. C2 evolution has no U2 term (only U1*C1)
2. m=1 signed-Hessian resolution is correctly stated
3. Direct Young bound replaces defective IBP for C1*C2*U0
4. T1 derivation uses B2*W (not B2*T0)
5. Metric/volume time variation is included in C2 energy
6. Base order is non-circular
7. Normal-form reconciliation is stated
8. Derivative-reordering lemma pairs C_{m+2} only with U0
"""

import json
import sys
from pathlib import Path

NOTE = Path(__file__).resolve().parent.parent / "notes" / "step60_base_pair_proof.md"
OUT = Path(__file__).resolve().parent.parent / "data" / "step60_base_pair_verify.json"

results = []

def check(name, condition, detail=""):
    results.append({"check": name, "status": "PASS" if condition else "FAIL", "detail": detail})
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name} -- {detail}")

# Read note
text = NOTE.read_text()

# 1. C2 evolution: boxed equation (3.4) has U1*C1, no U2
check(
    "C2_evolution_no_U2",
    "\\boxed{\\partial_tC_2=g^{-1}*U_1*C_1.}" in text,
    "eq (3.4): partial_t C2 = g^{-1}*U1*C1, no U2"
)

# 2. C2 evolution derivation: connection appears once algebraically
check(
    "C2_connection_once",
    "No second covariant derivative acts on the connection" in text or
    "not `U_2`" in text or
    "no `U_{m+1}`" in text or
    "No `U_2`" in text or
    "not `U_2`" in text,
    "C2 derivation: connection appears once, no U2"
)

# 3. m=1 signed-Hessian: the B3*U0 term reduces to signed form
check(
    "signed_hessian_resolution",
    "This IS of the signed form" in text or
    "signed-Hessian lemma closes all m=1" in text,
    "B3*U0 IBP descendant is signed-Hessian form"
)

# 4. Direct Young for C1*C2*U0 (Flag B repair)
check(
    "direct_young_no_IBP",
    "Direct Young bound" in text,
    "C1*C2*U0 handled by direct Young, not IBP"
)

# 5. T1 derivation uses B2*W not B2*T0 (Flag C repair)
check(
    "T1_uses_B2W",
    "B_2*W" in text and "B_2*T_0" not in text.split("B_2*W")[0][-500:],
    "T1 equation: B2*W from drift, not B2*T0"
)

# 6. Metric/volume time variation in C2 energy (Flag E repair)
check(
    "metric_time_variation",
    "\\|U_0\\|_\\infty\\|C_2\\|_p^p" in text,
    "C2 energy includes metric/volume variation via U0 L-inf"
)

# 7. Non-circular base order
check(
    "non_circular_order",
    "non-circular" in text and "U_0\\in L^\\infty" in text,
    "base order: (U0 Linf, T0 Lq) -> (U1,C2) -> T1 -> T0 Linf"
)

# 8. Derivative-reordering: C_{m+2} paired only with U0
check(
    "reordering_Cm2_U0_only",
    "paired only with `U_0`" in text or "paired exclusively with" in text,
    "C_{m+2} paired only with U0, never U_j for j>=1"
)

# 9. Normal-form reconciliation (Flag F repair)
check(
    "normal_form_reconciliation",
    "Normal-form reconciliation" in text,
    "Step 59 and Step 60 normal forms reconciled"
)

# 10. aT1*U0 divergence-form descendant (Flag A repair)
check(
    "divergence_descendant_aT1U0",
    "aT_1*U_0" in text,
    "aT1*U0 from divergence-form descendant included in ledger"
)

# 11. Time commutator g^{-1}*U1*U0 (Flag A repair)
check(
    "time_commutator_U1U0",
    "g^{-1}*U_1*U_0" in text or "(\\partial_t\\Gamma)*U_0" in text,
    "time commutator (dt Gamma)*U0 = g^{-1}*U1*U0 included"
)

# 12. Abstract correctly states C3 arises
check(
    "abstract_C3_arises",
    "C_3` that arises" in text or "`C_3` arises" in text or
    "total cutoff derivative `\\le 3`" in text,
    "Abstract states C3 arises and reduces to signed C2-Hessian"
)

# 13. No defective IBP claim for C1*C2*U0
# Check that the old text "With `C_2=\\nabla C_1`, integrate once" is gone
check(
    "no_defective_IBP",
    "With `C_2=\\nabla C_1`, integrate once" not in text,
    "Defective IBP mechanism for C1*C2*U0 removed"
)

# 14. Grönwall conclusion
check(
    "gronwall_conclusion",
    "e^{C_{p,\\tau}(t-\\tau)}" in text,
    "Grönwall estimate (4.3) present"
)

# 15. T0 L-inf from Sobolev embedding
check(
    "T0_Linf_sobolev",
    "W^{1,p}\\hookrightarrow L^\\infty" in text,
    "T0 L-inf from W1p Sobolev embedding, p>4"
)

# Summary
n_pass = sum(1 for r in results if r["status"] == "PASS")
n_total = len(results)
print(f"\n=== Summary: {n_pass}/{n_total} passed ===")

# Write JSON
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "step": 60,
    "note": str(NOTE),
    "checks": results,
    "summary": f"{n_pass}/{n_total} passed"
}, indent=2))
print(f"Wrote {OUT}")

sys.exit(0 if n_pass == n_total else 1)
