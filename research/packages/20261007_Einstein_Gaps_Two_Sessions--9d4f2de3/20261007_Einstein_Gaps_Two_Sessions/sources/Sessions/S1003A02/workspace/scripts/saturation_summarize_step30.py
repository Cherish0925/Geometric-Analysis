"""Summarize Step-30 anisotropic saturation experiments and charge relations."""
import glob,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(glob.glob(str(root/'data/saturation_control/*aniso*json'))+glob.glob(str(root/'data/saturation_control/regular_*json'))):
 try:
  r=json.loads(Path(p).read_text())
 except (json.JSONDecodeError,OSError):
  continue
 if not isinstance(r,dict) or 'entry_delta' not in r: continue
 d=r.get('entry_delta',[0]*5)
 rows.append({'file':Path(p).name,'eps':r['eps'],'success':r['success'],'dx':d[0],'dchi':d[3],'deta':d[4],
              'cost':r['cost'],'bplus0':r['bplus_initial'],'cost_minus_gap2':r['cost']-(2-r['bplus_initial']),
              't_ch':r['t_ch'],'A':r['A']})
out={'rows':rows,'interpretation':{
 'raw_entry':'Fixed O(1) x, chi, eta as eps->0 generally leaves the controlled F-structure regime; low raw costs are enlarged-entry warnings, not regular bolt competitors.',
 'regular_entry':'The finite-charge normalized-jet class uses x=X z^3, chi=C z, eta=N z. Exact limiting bplus is -2-(C+4X)^2; eta does not change it. This class is not automatically bounded-curvature geometry.',
 'best_subunit_observation':'raw eps=1/16, delta eta=-8 has collocation 0.5454 and independently reconstructed connector metric 0.5745, but eta=-8 is not uniform finite-charge scaling; its entry bplus=1.45194 already requires prefix cost at least 0.45194, and at eps=1/32 the same raw perturbation costs 2.9425.'}}
(root/'data/saturation_control/step30_anisotropic_summary.json').write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps(out,indent=1))
