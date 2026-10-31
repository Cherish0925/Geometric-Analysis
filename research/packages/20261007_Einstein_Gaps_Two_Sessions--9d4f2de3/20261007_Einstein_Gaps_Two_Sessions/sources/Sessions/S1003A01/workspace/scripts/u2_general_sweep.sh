#!/bin/bash
# Sweep of general U(2) cells: signed complex and real space-form bulks.
cd "$(dirname "$0")"
OUT=../data/u2_general
jobs=()
for bulk in CSF RSF; do for k in 1 -1; do for x0 in 0.0003 0.001 0.003 0.01; do for t in P J; do for d in 8 12; do
  echo "$bulk $k $x0 0.25 $d $t 800 $OUT/${bulk}_k${k}_x${x0}_X0.25_${t}_d${d}.json"
done; done; done; done; done | xargs -P 16 -L 1 bash -c 'PYTHONDONTWRITEBYTECODE=1 python u2_general_cell.py "$0" "$1" "$2" "$3" "$4" "$5" "$6" "$7" 2>/dev/null'
