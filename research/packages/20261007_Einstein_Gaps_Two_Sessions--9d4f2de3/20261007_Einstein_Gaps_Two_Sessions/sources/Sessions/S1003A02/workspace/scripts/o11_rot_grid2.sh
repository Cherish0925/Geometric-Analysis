#!/bin/bash
# Re-run missing/failed grid points (and add x0=0.001) with limited parallelism.
cd "$(dirname "$0")"
OUT=../data/o11rot
export OMP_NUM_THREADS=4
jobs=()
for x0 in 0.001 0.003 0.01 0.03; do
  for th in 0 0.3926991 0.7853982 1.1780972 1.5707963; do
    f=$OUT/grid_x0${x0}_th${th}.json
    if ! python -c "import json;json.load(open('$f'))" 2>/dev/null; then jobs+=("$x0 $th"); fi
  done
done
printf '%s\n' "${jobs[@]}"
printf '%s\n' "${jobs[@]}" | xargs -P 8 -L 1 bash -c 'python o11_rotated_cell.py $0 1.0 $1 6 4 6 0.05 300 --wB --opt 2>'"$OUT"'/err_x0$0_th$1.log > '"$OUT"'/grid_x0$0_th$1.json'
echo done
