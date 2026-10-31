#!/bin/bash
set -u
mkdir -p ../data/joint_dual
recs=(
 ../data/perp_area/x00.003_X64_d16.json
 ../data/perp_collar/continued_X32_to_X64_J_d16.json
 ../data/perp_area/x00.015_X64_d16.json
 ../data/perp_area/x00.02_X64_d16.json
 ../data/perp_area/x00.03_X64_d16.json
 ../data/perp_area/x00.05_X64_d16.json
 ../data/perp_area/x00.1_X64_d16.json
)
for r in "${recs[@]}"; do
  tag=$(basename "$r" .json)
  PYTHONDONTWRITEBYTECODE=1 python joint_dual_calibration.py "$r" --n 8001 --out "../data/joint_dual/${tag}.json" > "../data/joint_dual/${tag}.log" 2>&1
  echo "$tag done"
done
