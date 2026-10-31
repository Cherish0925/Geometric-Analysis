#!/bin/bash
# Sweep of the overlapping-tail two-cell trial (pair_overlap_trial.py) over depth w and phase theta.
# Usage: bash run_pair_sweep.sh RECORD OUTDIR NLOG2 "W LIST" [MAXPAR]
# (At most MAXPAR concurrent processes; many concurrent XLA processes exhaust the thread limit.)
REC=$1; OUT=$2; N=${3:-15}; WS=${4:-"0.1 0.2 0.4 0.6 0.8 1.0 1.2 1.5"}; MAXPAR=${5:-4}
cd "$(dirname "$0")"   # REC and OUT are relative to the scripts directory
mkdir -p "$OUT"
export JAX_PLATFORMS=cpu PYTHONDONTWRITEBYTECODE=1
export XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
TH="0,0.39269908169872414,0.7853981633974483"
for W in $WS; do
  while [ "$(jobs -rp | wc -l)" -ge "$MAXPAR" ]; do sleep 2; done
  python pair_overlap_trial.py "$REC" --w $W --theta $TH --n $N --seed 0 --out "$OUT/w${W}_s0.json" > "$OUT/w${W}_s0.log" 2>&1 &
done
wait
echo done
