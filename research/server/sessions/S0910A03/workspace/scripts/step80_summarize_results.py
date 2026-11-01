#!/usr/bin/env python3
"""Compact and independently recompute summary statistics for Step 80 runs."""
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'step80_joint_base_response_pilot.json'
d=json.loads(p.read_text())
out={'source':str(p),'runs':[]}
for row in d['runs']:
    q={'R':row['R'],'variants':{},'comparison':row['paired_comparison']}
    for name,v in row['variants'].items():
        e=v['entry']; r=v['residual']
        q['variants'][name]={
          'entry_operator_sup':e['operator_sup'],'entry_operator_rms':e['operator_rms'],
          'entry_q95':e['operator_q95'],'entry_argmax_r':e['argmax_r'],
          'exit_S_minus_I_sup':e['exit']['S_minus_I_sup'],
          'exit_intrinsic_Ric_sup':e['exit']['intrinsic_Ric_sup'],
          'exit_v_r_sup':e['exit']['v_r_sup'],
          'exit_mean_log_volume_growth':e['exit']['mean_log_volume_growth'],
          'map_energy_sup':e['base_orbit_coupling']['physical_map_energy_sup'],
          'orbit_stress_half_sup':e['base_orbit_coupling']['orbit_stress_half_sup'],
          'residual_stage_operator_sup':r['operator_sup'],
          'solver_nfev':[x['nfev'] for x in v['solvers']],
          'solver_optimality':[x['optimality'] for x in v['solvers']],
          'solver_messages':[x['message'] for x in v['solvers']],
        }
    out['runs'].append(q)
path=p.with_name('step80_joint_base_response_summary.json')
path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2));print('wrote',path)
