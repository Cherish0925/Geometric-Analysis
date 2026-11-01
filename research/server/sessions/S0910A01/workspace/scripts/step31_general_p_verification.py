#!/usr/bin/env python3
"""
Step 31 general-p verification -- superseded by Step 32.

The original Step 31 script printed a uniform endpoint interpretation that is no
longer the active calculation.  Step 32 rebuilt the nested-time recurrence in a
single convention and restored the conditional positive-time endpoint forms:
  ||aF(t)||_inf <= C beta/t,
  ||aE(t)||_inf <= C delta (r^2/t)^(1/3),
provided the same-support H3, fixed J6, Q, and tensor-energy estimates are proved.

This wrapper prevents future runs from reproducing the obsolete Step 31 output.
Run workspace/scripts/step32_nested_moser_repair.py for the active algebraic and
scaling check.
"""
from pathlib import Path
import runpy

print("=" * 78)
print("STEP 31 SCRIPT SUPERSEDED")
print("=" * 78)
print("Use workspace/notes/step32_nested_moser_and_tensor_audit.md as the active note.")
print("Running the Step 32 replacement check now.\n")

script = Path(__file__).with_name("step32_nested_moser_repair.py")
runpy.run_path(str(script), run_name="__main__")
