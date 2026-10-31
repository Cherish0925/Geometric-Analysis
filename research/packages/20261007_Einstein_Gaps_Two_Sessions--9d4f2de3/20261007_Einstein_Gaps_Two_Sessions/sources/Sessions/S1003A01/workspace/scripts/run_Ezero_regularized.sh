#!/bin/bash
set -u
mkdir -p ../data/joint_dual
for mu in 1e-1 1e-2 1e-3 1e-4; do
 tag=${mu//-/m}; tag=${tag//./p}
 PYTHONDONTWRITEBYTECODE=1 python test_Ezero_reconstruction.py ../data/perp_area/x00.03_X64_d16.json --maxiter 500 --mu "$mu" --out "../data/joint_dual/Ezero_mu${tag}.json" > "../data/joint_dual/Ezero_mu${tag}.log" 2>&1
 echo $mu done
done
