"""Summarize best positive-q cell searches and asymptotic payments."""
import argparse
import json
import os
import pandas as pd

ap=argparse.ArgumentParser()
ap.add_argument('inputs',nargs='+')
ap.add_argument('--out',required=True)
a=ap.parse_args()
rows=[]
for path in a.inputs:
    with open(path) as fh:
        rows += [json.loads(x) for x in fh if x.strip()]
df=pd.DataFrame(rows)
# Exclude profiles that effectively sit on the positivity penalty floor from
# the robust table; retain them in the raw records.
rob=df[df.F_min_scaled>0.05].copy()
idx=rob.groupby(['mu','qfrac_target']).j.idxmin()
best=rob.loc[idx].sort_values(['mu','qfrac_target'])
cols=['mu','qfrac_target','family','sign','wseed','q','j','K','deficit',
      'proj','rx','ry','rz','rv','Pw','Tphi','nfrac','F_min_scaled','phi_max',
      'radial_identity_error','i54_identity_error']
print(best[cols].to_string(index=False))
print('\nminimum j by mu')
print(rob.loc[rob.groupby('mu').j.idxmin(),cols].to_string(index=False))
print('\nmax abs identity errors',df.radial_identity_error.abs().max(),
      df.i54_identity_error.abs().max())
os.makedirs(os.path.dirname(a.out),exist_ok=True)
best[cols].to_csv(a.out,index=False)
