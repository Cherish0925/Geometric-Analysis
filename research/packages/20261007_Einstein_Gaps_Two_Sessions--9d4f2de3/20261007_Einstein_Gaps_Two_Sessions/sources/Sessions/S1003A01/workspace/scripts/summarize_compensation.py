"""Summarize constrained compensation runs by target n/m."""
import argparse, json, math
import pandas as pd

ap=argparse.ArgumentParser()
ap.add_argument('input')
ap.add_argument('--csv',required=True)
a=ap.parse_args()
rows=[json.loads(x) for x in open(a.input) if x.strip()]
df=pd.DataFrame(rows)
best=df.loc[df.groupby('nfrac_target')['deficit'].idxmin()].copy()
cols=['nfrac_target','nfrac','j','K','deficit','gain_n','q','A_pay','B_pay',
      'scalar_pay','rx','ry','rz','rv','radial_identity_error','i54_identity_error']
best[cols].sort_values('nfrac_target').to_csv(a.csv,index=False)
print(best[cols].sort_values('nfrac_target').to_string(index=False))
print('max identity errors',df.radial_identity_error.abs().max(),df.i54_identity_error.abs().max())
