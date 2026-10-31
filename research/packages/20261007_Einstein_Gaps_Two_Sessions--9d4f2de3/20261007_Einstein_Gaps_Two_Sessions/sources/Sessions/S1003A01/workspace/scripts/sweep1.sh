#!/bin/bash
# Parallel sweep of the conformal triaxial one-bolt cell cost.
# Output: workspace/data/cell_sweep1/*.jsonl ; summary via summarize_sweep.py
cd "$(dirname "$0")"
OUT=../data/cell_sweep1
mkdir -p $OUT
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
jobs=()
for Rc in 0.8 1.2 2.0 3.0; do
 for mu in 0.001 0.003 0.01 0.03 0.1 0.3 0.6; do
  for mode in phionly full; do
   for init in 0.0 0.05; do
    echo "$Rc $mu $mode $init"
   done
  done
 done
done | xargs -P 100 -L 1 bash -c 'python cell_opt.py --Rc $0 --mu $1 --modes $2 --init $3 --seeds 2 --deg 18 --iters 6000 --coord log --out '"$OUT"'/run_$0_$1_$2_$3.jsonl > /dev/null 2>&1'
echo done
