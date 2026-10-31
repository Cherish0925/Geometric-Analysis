#!/bin/bash
# Stage-2 sweep: Hessian in triaxial direction + kicked restarts.
cd "$(dirname "$0")"
OUT=../data/cell_stage2
mkdir -p $OUT
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
for Rc in 1.0 2.0 4.0; do
 for mu in 0.003 0.01 0.03 0.1 0.3; do
  echo "$Rc $mu"
 done
done | xargs -P 30 -L 1 bash -c 'python cell_stage2.py --Rc $0 --mu $1 --out '"$OUT"'/s2_$0_$1.json > '"$OUT"'/s2_$0_$1.log 2>&1'
cat $OUT/*.log | grep '^{'
