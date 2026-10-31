#!/bin/bash
# Second stage of the bolt-area branch: continue X=64 cells of several areas to X=128 (deg 20)
# and X=256 (deg 24); add fresh x0 = .07, .15 chains.  Outputs in data/perp_area/.
cd "$(dirname "$0")"
OUT=../data/perp_area
export JAX_PLATFORMS=cpu PYTHONDONTWRITEBYTECODE=1
export XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
cont () {   # X0 SEED then list of "X deg nq"
  X0=$1; P=$2; shift 2
  for XD in "$@"; do
    set -- $XD
    N=$OUT/x0${X0}_X$1_d$2.json
    python perp_collar_continue.py $P $1 $2 $N --nq $3 --maxiter 9000 > ${N%.json}.log 2>&1 || return
    P=$N
  done
}
fresh () {
  X0=$1; S=$OUT/x0${X0}_X8_d8.json
  python perp_collar_scan.py $X0 8 8 J 600 $S > ${S%.json}.log 2>&1 || return
  cont $X0 $S "16 10 800" "32 12 1000" "64 16 1200" "128 20 1400" "256 24 1600"
}
for X0 in 0.02 0.03 0.05 0.1; do
  cont $X0 $OUT/x0${X0}_X64_d16.json "128 20 1400" "256 24 1600" &
done
fresh 0.07 &
fresh 0.15 &
wait
echo done
