#!/bin/sh
# Step 8: fixed-frame theta=pi/2 cells vs fixed-frame aligned control.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=6
D=../data/o11perp
mkdir -p $D
for x in 0.1 0.03 0.01 0.003 0.001; do
  for mode in perp aligned; do
    for sm in rough smooth; do
      A=""; [ $mode = aligned ] && A="--aligned"
      S=""; [ $sm = smooth ] && S="--smooth"
      python o11_perp_cell.py $x 6 6 300 $A $S > $D/${mode}_${sm}_x$x.json 2>/dev/null &
    done
  done
done
wait
echo done
