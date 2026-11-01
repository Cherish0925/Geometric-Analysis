#!/bin/bash
# Step 58: run product-background tests of Theorem 57.Phi in parallel.  usage: bash step58_product_batch.sh D nu nphi
cd "$(dirname "$0")"
D=${1:-4}; NU=${2:-8}; NPHI=${3:-24}
pids=()
for c in "-1 -1 perp" "-1 -1 par" "-1 -3 perp" "-1 -3 par" "-1 1 perp" "-1 1 par" "1 2 perp" "-2 0.5 perp"; do
  set -- $c
  taskset -c "${QIUSHI_CPU_LIST:-0-7}" python step58_product_tests.py $1 $2 $3 $D $NU $NPHI > ../data/step58_products/step58_product_${3}_K$1_K$2_D${D}.log 2>&1 &
  pids+=($!)
done
rc=0
for p in "${pids[@]}"; do wait $p || rc=1; done
for f in ../data/step58_products/step58_product_*_D${D}_q${NU}_${NPHI}.json; do python -c "import json,sys; d=json.load(open('$f')); print(d['layout'],d['K1'],d['K2'],'Phi',round(d['Phi'],10),'pred',d['Phi_pred'],'err',d['err'],'leak',d['leak'])"; done
exit $rc
