#!/bin/bash
# Step 79: cone scan of Phi6 on GPU 0 (even branch H3=0), output data/step79c
cd "$(dirname "$0")"
export CUDA_VISIBLE_DEVICES=0 STEP79_OUT=step79c
python -u step79_cone_scan.py --njets 4 --lams=-3,-1,0,1 --wscales 0 --seed 21 --tag generic_s21 > ../data/step79c/log_generic_s21.txt 2>&1
python -u step79_cone_scan.py --njets 2 --lams=-1,1 --wscales 0,3 --mode smallc --seed 22 --tag smallc_s22 > ../data/step79c/log_smallc_s22.txt 2>&1
python -u step79_cone_scan.py --njets 2 --lams=-1,1 --wscales 0 --mode bigc --seed 23 --tag bigc_s23 > ../data/step79c/log_bigc_s23.txt 2>&1
python -u step79_cone_scan.py --njets 2 --lams=-1 --wscales 0 --h3 1.0 --seed 24 --tag h3probe_s24 > ../data/step79c/log_h3probe_s24.txt 2>&1
echo done
