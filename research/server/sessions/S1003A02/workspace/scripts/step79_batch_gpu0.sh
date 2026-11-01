#!/bin/bash
# Step 79 batch on GPU 0: does a nonzero odd jet H3 remove the even-ansatz order-6 obstruction at the D6 jet?
cd "$(dirname "$0")"
export CUDA_VISIBLE_DEVICES=0
L=../data/step79
python -u step79_general_order6.py --h2 d6 --lam -3 --h3scales 0.1,0.3,1,3 --nh3 3 --seed 5 --nlm 20 --tag d6_h3scan > $L/log_d6_h3scan.txt 2>&1
echo done
