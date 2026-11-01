#!/bin/bash
# Step 62 batch (cone tests): usage step62_batch2.sh OUTDIR D NSTEPS CPUS_PER_JOB "lam:sector:seed ..."
cd "$(dirname "$0")"
OUTD=$1; D=$2; NS=$3; C=$4; shift 4
export STEP62_OUT=$OUTD
mkdir -p $OUTD
pids=(); i=0
CPUS=(${QIUSHI_CPU_LIST//,/ })
for spec in $@; do
  IFS=: read lam sec seed <<< "$spec"
  lo=$((i*C)); cl=$(echo ${CPUS[@]:$lo:$C} | tr ' ' ',')
  OMP_NUM_THREADS=$C OPENBLAS_NUM_THREADS=$C taskset -c $cl \
    python -u step62_zero_prolong.py cont $D $lam $sec $seed $NS > $OUTD/log_D${D}_l${lam}_${sec}_s${seed}.txt 2>&1 &
  pids+=($!); i=$((i+1))
done
rc=0
for p in ${pids[@]}; do wait $p || rc=1; done
exit $rc
