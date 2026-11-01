#!/bin/bash
# Step 79 batch on GPU 1: Kahler control, A01 shared cone point (c=1, S=I, a=1+2i), lambda grid.
cd "$(dirname "$0")"
export CUDA_VISIBLE_DEVICES=1
export STEP79_OUT=step79b; L=../data/step79b
python -u step79_general_order6.py --h2 kahler --lam -3 --h3scales 0,1 --nh3 1 --seed 1 --nlm 20 --tag kahler_lam-3 > $L/log_kahler_lam-3.txt 2>&1
JET='[[1,0],[[1,0],[0,0],[1,0]],[1,2]]'
python -u step79_general_order6.py --h2 jet --jet "$JET" --lam -1 --h3scales 0,0.3,1 --nh3 2 --seed 2 --nlm 20 --tag a01pt_lam-1 > $L/log_a01pt_lam-1.txt 2>&1
for l in -10 0 1 -0.1; do
python -u step79_general_order6.py --h2 jet --jet "$JET" --lam $l --h3scales 0 --nh3 1 --seed 3 --nlm 10 --tag a01pt_lam$l > $L/log_a01pt_lam$l.txt 2>&1
done
python -u step79_general_order6.py --h2 kahler --lam 3 --h3scales 0 --nh3 1 --seed 4 --nlm 20 --tag kahler_lam3 > $L/log_kahler_lam3.txt 2>&1
echo done
