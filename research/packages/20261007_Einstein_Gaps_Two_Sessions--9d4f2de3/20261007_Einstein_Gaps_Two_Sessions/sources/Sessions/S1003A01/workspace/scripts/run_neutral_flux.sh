#!/bin/bash
# Evaluate the bolt-carried neutral transport (neutral_flux_bolt.py) on stored cells in parallel.
cd "$(dirname "$0")"
OUT=../data/neutral_flux; mkdir -p $OUT
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1
for r in "$@"; do
  b=$(basename $r .json)
  python neutral_flux_bolt.py $r --n 4001 --out $OUT/nf_$b.json > $OUT/nf_$b.log 2>&1 &
done
wait
echo done
