"""Resolution check for exact charged-Koiso center residual using full Gaussian blocks."""
from pathlib import Path
import importlib.util,json,numpy as np
p=Path(__file__).with_name('step98_full_matrix_joint_transition.py')
spec=importlib.util.spec_from_file_location('fm',p);fm=importlib.util.module_from_spec(spec);spec.loader.exec_module(fm)
out=[]
for ns in [16,24,32,48,64,96,128]:
 g=fm.center_geometry(ns,2,1.,.5)
 q=g['q0'][None,:,:,:]
 K=g['k0'][None,:,:,:]
 qi=np.linalg.inv(q)
 target=2*(g['ric0']+3*g['q0']+2*np.einsum('sij,sjk,skl->sil',g['k0'],np.linalg.inv(g['q0']),g['k0']))
 qn=2*K;qnn=target[None,:,:,:]
 # Dummy derivative matrices are overridden.
 res=fm.full_residual(q,np.zeros((1,1)),np.zeros((1,1)),qn_override=qn,qnn_override=qnn)
 out.append({'ns':ns,'op_sup':float(res['op'].max()),'Enn':float(np.abs(res['Enn']).max()),
             'mom_orth':float(np.max(np.linalg.norm(res['Eorth'][0,:,0,1:],axis=1))),
             'ET_orth':float(max(np.max(np.abs(np.linalg.eigvalsh(res['Eorth'][0,k,1:,1:]))) for k in range(ns))),
             'scalar_constraint':float(np.max(np.abs(g['scalar0']+7)))})
path=Path(__file__).resolve().parents[1]/'data/step98_center_residual_resolution.json';path.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
