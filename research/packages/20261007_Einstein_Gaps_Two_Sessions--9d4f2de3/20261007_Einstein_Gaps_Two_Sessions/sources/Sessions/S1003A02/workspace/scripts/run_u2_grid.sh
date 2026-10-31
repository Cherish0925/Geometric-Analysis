#!/bin/bash
# grid of U(2) cell minimisations (log-radial basis); at most 6 concurrent jobs, 8 threads each
cd "$(dirname "$0")"
export JAX_PLATFORMS=cpu
export XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=8"
export OMP_NUM_THREADS=8
mkdir -p ../data/u2grid
out=../data/u2grid/u2_cell_grid2.jsonl
: > $out
jobs_list=""
for X in 2.0 10.0 50.0; do
  for x0 in 0.0003 0.003 0.03 0.1 0.3 1.0 3.0 10.0; do
    awk "BEGIN{exit !($x0 < $X/2)}" || continue
    jobs_list="$jobs_list $x0:$X"
  done
done
echo $jobs_list | tr ' ' '\n' | xargs -P 6 -I{} bash -c 'p={}; x0=${p%%:*}; X=${p##*:}; timeout 1500 python u2_cell_jax_log.py $x0 $X 12 1600 2>>../data/u2grid/err.log >> '"$out"
cat $out
