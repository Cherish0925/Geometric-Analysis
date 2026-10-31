"""Summarize Step-16 joint dual and scalar-channel cancellation experiments."""
import json,glob,os,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[]
for f in sorted((root/'data/joint_dual').glob('x00*_X64_d16.json')):
 r=json.loads(f.read_text()); r=r[0] if isinstance(r,list) else r; rows.append(dict(tag=f.stem,x0=r['x0'],P=r['direct']['P_over_8pi2'],
  green=r['green_shape']['bound'],spin=r['spin']['bound'],joint=r['joint']['bound'],
  green_share=r['green_shape']['share_of_P'],joint_share=r['joint']['share_of_P'],gain=r['joint_gain_over_max']))
f=root/'data/joint_dual/continued_X32_to_X64_J_d16.json'
if f.exists():
 r=json.loads(f.read_text()); r=r[0] if isinstance(r,list) else r; rows.append(dict(tag=f.stem,x0=r['x0'],P=r['direct']['P_over_8pi2'],green=r['green_shape']['bound'],spin=r['spin']['bound'],joint=r['joint']['bound'],green_share=r['green_shape']['share_of_P'],joint_share=r['joint']['share_of_P'],gain=r['joint_gain_over_max']))
rows.sort(key=lambda q:q['x0'])
out=root/'data/joint_dual/summary.csv'
with out.open('w',newline='') as h:
 w=csv.DictWriter(h,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(json.dumps(rows,indent=1));print(out)
