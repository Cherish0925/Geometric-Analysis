#!/bin/bash
# Grid of optimized rotated cells: (x0, theta).  Output: workspace/data/o11rot/grid_x0{x0}_th{theta}.json
cd "$(dirname "$0")"
OUT=../data/o11rot
mkdir -p $OUT
export XLA_FLAGS=--xla_cpu_multi_thread_eigen=false
export OMP_NUM_THREADS=1
jobs=()
for x0 in 0.003 0.01 0.03; do
  for th in 0 0.3926991 0.7853982 1.1780972 1.5707963; do
    jobs+=("$x0 $th")
  done
done
printf '%s\n' "${jobs[@]}" | xargs -P 15 -L 1 bash -c 'python o11_rotated_cell.py $0 1.0 $1 6 4 6 0.05 300 --wB --opt 2>/dev/null > '"$OUT"'/grid_x0$0_th$1.json'
echo done
