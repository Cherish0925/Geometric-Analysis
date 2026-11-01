#!/bin/bash
# Step 50: Yamabe/Weyl ledger (A01 step43_yamabe_lebrun_ledger.py) along the perpendicular CH cell family.
# Output: Sessions/S1003A02/workspace/data/step50_family/ledger_<x0>_<X>.json, one per record; then summary.
cd "$(dirname "$0")/../../../S1003A01/workspace/scripts" || exit 1
OUT=../../../S1003A02/workspace/data/step50_family
pids=()
for rec in x00.003_X64_d16 x00.01_X64_d20 x00.015_X64_d16 x00.02_X256_d24 x00.03_X128_d20 x00.03_X256_d24 \
           x00.05_X256_d24 x00.07_X256_d24 x00.1_X128_d20 x00.15_X256_d24; do
  python step43_yamabe_lebrun_ledger.py ../data/perp_area/$rec.json --out $OUT/ledger_$rec.json --N 80000 > $OUT/log_$rec.txt 2>&1 &
  pids+=($!)
done
rc=0
for p in "${pids[@]}"; do wait $p || rc=1; done
exit $rc
