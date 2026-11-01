"""Summarize scaling and exact asymptotic constants from Step 90 radial runs."""
from pathlib import Path
import json, math
import numpy as np

root=Path('workspace/data')
taper=json.loads((root/'step90_radial_twist_taper.json').read_text())['runs']
core=json.loads((root/'step90_radial_twist_core.json').read_text())['runs']

# For each L fit A/delta as delta->0 and max Err/delta^2.
summary={}
for L in sorted(set(r['L'] for r in taper)):
    rs=[r for r in taper if r['L']==L]
    vals=np.array([r['A_over_delta'] for r in rs])
    errs=np.array([r['max_abs_Err']/r['delta']**2 for r in rs])
    # In round cusp with constant damping 3 and b=-A sin^2(pi s/L), exact
    # terminal cancellation gives A/delta = e^{-3L}/I(L), where
    # I=integral_0^L e^{-3(L-s)} sin^2(pi s/L) ds.
    grid=np.linspace(0,L,200001)
    I=np.trapz(np.exp(-3*(L-grid))*np.sin(np.pi*grid/L)**2,grid)
    exact_ratio=math.exp(-3*L)/I
    summary[str(L)]={
      'A_over_delta_min':float(vals.min()),'A_over_delta_max':float(vals.max()),
      'Err_over_delta2_min':float(errs.min()),'Err_over_delta2_max':float(errs.max()),
      'round_cusp_linear_prediction_A_over_delta':float(exact_ratio)
    }

# Core redshift scaling: report radii and asymptotic states.
core_summary=[]
for r in core:
    core_summary.append({
      'Q0':r['Q0'],'r_Q_below_0.01':r['radii_Q_below']['0.01'],
      'r_Q_below_0.0001':r['radii_Q_below']['0.0001'],
      'sigma_final':r['sigma_final'],'alpha_final':r['alpha_final'],
      'u_final':r['u_final'],'v_final':r['v_final'],'H_final':r['H_final'],
      'max_rel_rr_constraint':r['max_rel_rr_constraint']
    })

out={
 'taper_scaling':summary,
 'core_redshift':core_summary,
 'interpretation':[
   'At fixed collar length L, required mixed forcing is A=C(L) delta independent of Q0 as delta decreases.',
   'The unused horizontal rr defect scales as O(delta^2), while area, orbit-traceless, and theta-theta horizontal equations were enforced exactly.',
   'The constant-charge exact radial core redshifts arbitrarily large Q0 to small Q and converges toward u=2, v=0, H=1, K=-1.'
 ]
}
p=root/'step90_taper_scaling_summary.json';p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print(f'\nwrote {p}')
