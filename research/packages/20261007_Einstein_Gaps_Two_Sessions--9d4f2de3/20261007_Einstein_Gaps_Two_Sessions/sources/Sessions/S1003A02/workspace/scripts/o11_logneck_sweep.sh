#!/bin/sh
# log-neck sweep: P target (deg 32, 40) and J target (deg 32), x0 = 1e-3 .. 1e-9
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=2
OUT=../data/o11logneck
for spec in "P 32" "P 40" "J 32"; do
for x in 1e-3 3e-4 1e-4 3e-5 1e-5 1e-6 1e-7 1e-8 1e-9; do
  echo "$x $spec"
done; done | xargs -P 4 -n 3 sh -c 'python o11_perp_logneck.py $0 --deg $2 --target $1 --nq 2400 --maxiter 300 --shi -0.15 --out '$OUT'/$1_x$0_d$2.json > '$OUT'/$1_x$0_d$2.log 2>&1'
echo done
