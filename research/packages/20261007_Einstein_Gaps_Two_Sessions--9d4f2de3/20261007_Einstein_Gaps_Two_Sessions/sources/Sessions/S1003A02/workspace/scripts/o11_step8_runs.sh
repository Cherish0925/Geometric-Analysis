#!/bin/sh
# Step 8: aligned cells at smaller x0, then rotation-density minimisation for all x0.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=8
D=../data/o11rot
for x in 0.0003 0.0001; do
  python o11_rotated_cell.py $x 1.0 0 6 4 6 0.05 300 --wB --opt > $D/grid_x0${x}_th0.json 2>/dev/null &
done
for x in 0.03 0.003 0.001; do
  python o11_rotation_density.py $x > $D/rd_log_$x.txt 2>/dev/null &
done
wait
for x in 0.0003 0.0001; do
  python o11_rotation_density.py $x > $D/rd_log_$x.txt 2>/dev/null
done
echo done
