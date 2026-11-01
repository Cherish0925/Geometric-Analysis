#!/bin/bash
# Step 65: run the exceptional-flux ledger on the perpendicular CH cell family.
cd "$(dirname "$0")/.." || exit 1
P=../../S1003A01/workspace/data/perp_area
mkdir -p data/step65_family
pids=()
python scripts/step65_cell_twist_flux.py $P/x00.03_X128_d20.json data/step65_cell_twist_flux.json > /dev/null 2> data/step65_family/main.err & pids+=($!)
for r in x00.003_X64_d16 x00.01_X64_d20 x00.02_X128_d20 x00.05_X128_d20 x00.07_X128_d20 x00.1_X128_d20 x00.15_X128_d20 x00.03_X64_d16 x00.03_X256_d24; do
  OMP_NUM_THREADS=1 python scripts/step65_cell_twist_flux.py $P/$r.json data/step65_family/$r.json --quick > /dev/null 2> data/step65_family/$r.err & pids+=($!)
done
rc=0; for p in "${pids[@]}"; do wait $p || rc=1; done
python - <<'EOF' | tee data/step65_family/summary.txt
import json,glob
for f in sorted(glob.glob('data/step65_family/*.json'))+['data/step65_cell_twist_flux.json']:
    d=json.load(open(f));L=d['ledger_theta0_on_cell'];c=d['checks']
    print(f.split('/')[-1][:18], 'x0=%.3f X=%g p=%.7f(rec %.7f) delta=%.6f Fsup/2pi=%.6f hodge=%.6f loss=%.6f sav/2delta=%.4f eff=%.3f tauq50=%.2f closed=%.1e |h|2=%.5f taupos=%.5f tauneg=%.5f'%(d['x0'],d['X'],L['p'],c['P_record'],L['flux_deficit_delta'],L['F_E_sup_over_J_over_2pi_(int 2|m1 phi|)'],L['hodge_lower_bound_(F_E/2pi)^2/|h|^2'],L['loss_nonharmonic_over_4pi2'],L['saving_over_2delta'],L['J1_twist_harmonic_efficiency_on_cell'],L['tau_J1_quantiles_x_over_x0']['0.5'],c['closedness_residual_sigma_plus'],c['h_norm2_cell'],L['tau_J1_positive_part_over_2pi'],L['tau_J1_negative_part_over_2pi']))
EOF
exit $rc
