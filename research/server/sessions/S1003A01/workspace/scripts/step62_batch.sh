#!/bin/bash
# Step 62 batch: continuation tests of first-torsion-jet sectors at a torsion zero.
# usage: step62_batch.sh D NSTEPS CPUS_PER_JOB "lam:sector:seed ..."
cd "$(dirname "$0")"
D=$1; NS=$2; C=$3; shift 3
pids=(); i=0
CPUS=(${QIUSHI_CPU_LIST//,/ })
for spec in $@; do
  IFS=: read lam sec seed <<< "$spec"
  lo=$((i*C)); cl=$(echo ${CPUS[@]:$lo:$C} | tr ' ' ',')
  OMP_NUM_THREADS=$C OPENBLAS_NUM_THREADS=$C MKL_NUM_THREADS=$C taskset -c $cl \
    python -u step62_zero_prolong.py cont $D $lam $sec $seed $NS > ../data/step62/log_D${D}_l${lam}_${sec}_s${seed}.txt 2>&1 &
  pids+=($!); i=$((i+1))
done
rc=0
for p in ${pids[@]}; do wait $p || rc=1; done
exit $rc
