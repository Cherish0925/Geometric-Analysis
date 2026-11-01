#!/usr/bin/env python3
"""
Step 61 gate audit structural verification.

Checks that the gate audit note contains all key findings from the three
TTCS verifier integrations, and that the route assessment correctly reflects
the revised module status.
"""
import json, os, sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE = os.path.join(WORKSPACE, "notes", "step61_gate_audit_moser_and_existence.md")
ROUTE = os.path.join(WORKSPACE, "plans", "route_assessment_step61.md")

results = []

def check(name, condition, detail):
    status = "PASS" if condition else "FAIL"
    results.append({"check": name, "status": status, "detail": detail})
    print(f"[{status}] {name} -- {detail}")

# Read files
with open(NOTE) as f:
    note = f.read()
with open(ROUTE) as f:
    route = f.read()

# === Defect Moser endpoint: GATE FAILED ===
check("defect_gate_failed",
      "GATE FAILED" in note,
      "defect Moser endpoint gate result is FAILED")

check("defect_J6_sound",
      "algebraically sound" in note and "independent" in note,
      "J6 persistence is algebraically sound and Y-independent")

check("defect_gap_general_p",
      "general-$p$ two-factor" in note or "general-$p$ two-factor inequality" in note,
      "general-p two-factor inequality not proved")

check("defect_gap_recurrence",
      "nested Moser recurrence" in note and "not derived" in note,
      "nested Moser recurrence cited, not derived")

check("defect_gap_seed_undefined",
      "H_{p_0}" in note and "never defined" in note,
      "seed H_{p0} undefined in recurrence")

check("defect_gap_exponent",
      "1/3" in note and "1/2" in note,
      "exponent 1/3 vs 1/2 depends on H_{p0} definition")

check("defect_no_V_leg",
      "no $V$-leg" in note or "V-leg" in note,
      "without defect endpoint, bootstrap has no V-leg")

# === Curvature Moser endpoint: GATE CONDITIONAL ===
check("curvature_gate_conditional",
      "GATE CONDITIONAL" in note,
      "curvature Moser endpoint gate result is CONDITIONAL")

check("curvature_logic_sound",
      "internally consistent" in note and "non-circular" in note,
      "curvature internal logic sound")

check("curvature_tensor_premise",
      "pure-scaling checksum" in note,
      "pure-scaling checksum needed for tensor premise")

check("curvature_metric_drift",
      "C_V\\|aE\\|_\\infty H" in note or "metric-drift" in note,
      "metric-drift term must be inserted into H-inequality")

# === Per-datum existence: GATE CONDITIONAL ===
check("existence_gate_conditional",
      note.count("GATE CONDITIONAL") >= 2,
      "existence construction gate result is CONDITIONAL")

check("existence_tame_verified",
      "tame" in note.lower() and "verified" in note,
      "tame hierarchy verified")

check("existence_cited_standard",
      "cited-standard" in note or "cited as" in note,
      "fixed-parameter parabolic existence cited-standard")

check("existence_splice_ok",
      "autonomous splice" in note and "circumvent" in note,
      "autonomous splice circumvents uniqueness")

# === Consolidated status ===
check("one_blocking_gap",
      "one blocking gap" in note or "single blocking gap" in note,
      "exactly one blocking gap identified (defect Moser)")

check("table_present",
      "| Module |" in note and "FAILED" in note and "CONDITIONAL" in note,
      "consolidated gate table present")

# === Route assessment ===
check("route_revised_status",
      "FAILED" in route and "general-$p$" in route,
      "route assessment has revised module status with FAILED gate")

check("route_next_target",
      "general-$p$ two-factor defect inequality" in route or "general-$p$" in route,
      "route assessment names the blocking gap as next target")

check("route_complementary",
      "graph-manifold" in route or "graph manifold" in route,
      "route assessment mentions complementary graph-manifold route")

# === Broader context ===
check("quantifier_noted",
      "single-sign" in route or "sign-branch" in route,
      "quantifier normalization noted")

# Summary
n_pass = sum(1 for r in results if r["status"] == "PASS")
n_total = len(results)
print(f"\n=== Summary: {n_pass}/{n_total} passed ===")

out = {
    "step": 61,
    "purpose": "gate audit structural verification",
    "checks": results,
    "summary": f"{n_pass}/{n_total} passed",
    "gate_results": {
        "defect_moser": "FAILED",
        "curvature_moser": "CONDITIONAL",
        "per_datum_existence": "CONDITIONAL",
    },
    "blocking_gap": "defect Moser general-p inequality + nested recurrence",
}
out_path = os.path.join(WORKSPACE, "data", "step61_gate_audit_verify.json")
with open(out_path, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print(f"Wrote {out_path}")

sys.exit(0 if n_pass == n_total else 1)
