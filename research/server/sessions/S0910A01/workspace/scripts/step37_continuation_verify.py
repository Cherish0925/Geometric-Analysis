#!/usr/bin/env python3
"""
Step 37 verifier is superseded by Step 38.

The original version printed a proof-like 42/42 success report for the Step 37
continuation theorem.  Step 38 found a structural error: the cutoff-degenerate
Lemma 1.2a used |U|<=K to infer an extra chi^2-small drift on {chi<delta}, but
U=a(Rm+G) only gives |aE|=|Ric(U)|<=C K, not |aE|<=C chi^2 K.  Small C0 metric
drift also cannot recover curvature derivatives, and fixed coordinate cutoff
jets do not control evolving covariant cutoff jets.

Use instead:
  - workspace/notes/step38_continuation_repair_and_support_normalization.md
  - workspace/scripts/step38_continuation_support_verify.py

This script exits nonzero intentionally so that future reruns do not treat the
withdrawn Step 37 closure as verified.
"""
print("STEP 37 CONTINUATION VERIFIER SUPERSEDED")
print("Reason: Lemma 1.2a fails in the cutoff-degenerate region; continuation and first-exit closure remain unproved.")
print("Run: python Sessions/S0910A01/workspace/scripts/step38_continuation_support_verify.py")
raise SystemExit(2)
