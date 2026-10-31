#!/bin/sh
# smooth-bolt, exact-collar log-neck sweep with explicit plateau seed: P and J targets
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=2
OUT=../data/o11logneck
for T in P J; do
for x in 1e-3 1e-4 1e-5 1e-6 1e-7 1e-8 1e-9 1e-10 1e-11 1e-12; do
  echo "$x $T"
done; done | xargs -P 4 -n 2 sh -c 'python o11_perp_logneck.py $0 --deg 32 --nq 2400 --maxiter 600 --shi -0.15 --smooth --ncore 10 --nout 16 --target $1 --plateau 1 --out '$OUT'/V$1_x$0.json > '$OUT'/V$1_x$0.log 2>&1'
for T in P J; do
for x in 1e-3 1e-4 1e-5; do
  echo "$x $T"
done; done | xargs -P 4 -n 2 sh -c 'python o11_perp_logneck.py $0 --deg 32 --nq 2400 --maxiter 600 --shi -0.15 --smooth --ncore 10 --nout 16 --target $1 --out '$OUT'/W$1_x$0.json > '$OUT'/W$1_x$0.log 2>&1'
echo done
