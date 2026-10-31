#!/bin/bash
# Bolt-area (b^2 = x0) dependence of the large-collar perpendicular CH cell branch.
# For each x0: obtain an X=8 degree-8 J-optimal cell (existing record or perp_collar_scan.py from
# zero), then continue the same physical metric outward (perp_collar_continue.py, which now keeps
# the seed's x0) to X=16 (deg 10), 32 (deg 12), 64 (deg 16).  Separately restarts the x0=.01 X=64
# cell at degree 20.  Outputs: data/perp_area/x0{X0}_X{X}_d{deg}.json and .log
cd "$(dirname "$0")"
OUT=../data/perp_area; mkdir -p $OUT
export JAX_PLATFORMS=cpu PYTHONDONTWRITEBYTECODE=1
export XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
chain () {
  X0=$1; SEED=$2
  if [ -z "$SEED" ]; then
    SEED=$OUT/x0${X0}_X8_d8.json
    python perp_collar_scan.py $X0 8 8 J 600 $SEED > $OUT/x0${X0}_X8_d8.log 2>&1 || return
  fi
  P=$SEED
  for XD in "16 10 800" "32 12 1000" "64 16 1200"; do
    set -- $XD
    N=$OUT/x0${X0}_X$1_d$2.json
    python perp_collar_continue.py $P $1 $2 $N --nq $3 --maxiter 9000 > ${N%.json}.log 2>&1 || return
    P=$N
  done
}
chain 0.003 ../data/perp_collar/x00.003_X8_J_d8.json &
chain 0.015 &
chain 0.02 &
chain 0.03 ../data/perp_collar/x00.03_X8_J_d8.json &
chain 0.05 &
chain 0.1 &
python perp_collar_continue.py ../data/perp_collar/continued_X32_to_X64_J_d16.json 64 20 $OUT/x00.01_X64_d20.json --nq 1400 --maxiter 12000 > $OUT/x00.01_X64_d20.log 2>&1 &
wait
echo done
