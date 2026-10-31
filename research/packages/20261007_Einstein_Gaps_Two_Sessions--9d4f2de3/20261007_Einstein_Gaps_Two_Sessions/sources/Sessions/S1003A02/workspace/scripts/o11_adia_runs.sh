#!/bin/sh
# Step 8: adiabatic (fixed-slot) family at intermediate angles + missing perp points.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=8
D=../data/o11perp
mkdir -p $D
{
for x in 0.01 0.003; do
  for t in 0 0.3926991 0.7853982 1.1780972; do echo "$x $t"; done
done
echo "0.003 pi2"; echo "0.03 pi2"; echo "0.001 pi2"
} | xargs -P 6 -n 2 sh -c '
  if [ "$1" = pi2 ]; then
    python o11_perp_cell.py $0 6 6 300 > '"$D"'/perp_rough_x$0.json 2>/dev/null
  else
    python o11_perp_cell.py $0 6 6 300 --theta=$1 > '"$D"'/adia_x$0_th$1.json 2>/dev/null
  fi'
echo done
