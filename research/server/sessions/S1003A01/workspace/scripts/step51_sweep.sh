#!/bin/bash
# Step 51 sweep: CGB-form log coefficient on the Einstein kernel locus and controls.
# Each case: TAG lam1 lam2 lam3 wm   (W+ eigenvalues in (J1,J2,J3); zeta = J3; s = -24)
cd "$(dirname "$0")"
CASES=(
"CH 2 -4 2 0"
"H2H2 2 -4 2 1"
"k_wm4 -4 2 2 0"
"k_wm3 -3 1 2 0"
"k_wm2 -2 0 2 0"
"k_wm1 -1 -1 2 0"
"k_w0 0 -2 2 0"
"k_w1 1 -3 2 0"
"k_w0_Wminus 0 -2 2 1"
"off_aligned 2 2 -4 0"
"off_W0 0 0 0 0"
"off_generic 1 0.5 -1.5 0"
)
IFS=',' read -ra CPUS <<< "$(echo $QIUSHI_CPU_LIST)"
# expand cpu list ranges like 0-15
LIST=()
for tok in "${CPUS[@]}"; do
  if [[ $tok == *-* ]]; then for ((c=${tok%-*}; c<=${tok#*-}; c++)); do LIST+=($c); done; else LIST+=($tok); fi
done
N=${#CASES[@]}; P=$(( ${#LIST[@]} / N )); [ $P -lt 1 ] && P=1
echo "cpus ${#LIST[@]} per-worker $P"
pids=()
for i in "${!CASES[@]}"; do
  set -- ${CASES[$i]}
  sub=$(IFS=,; echo "${LIST[*]:$((i*P)):$P}")
  taskset -c "$sub" python step51_cgb_full_coefficient.py "$1" "$2" "$3" "$4" "$5" 4 12 20 > ../data/step51/log_$1.txt 2>&1 &
  pids+=($!)
done
rc=0
for p in "${pids[@]}"; do wait $p || rc=1; done
grep -h '"tag"\|F_kB_only\|F_opt\|a_eps\|A02_Phi\|range_res' ../data/step51/cgb_*.json
exit $rc
