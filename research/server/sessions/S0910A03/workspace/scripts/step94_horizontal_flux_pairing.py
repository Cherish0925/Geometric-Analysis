"""
Step 94: symbolic integration-by-parts audit for the horizontal Noether pairing.

Starting from
  2 div_sigma H - d trH = -dT - T d sigma - <Z,dU> - m_q,
and dmu_sigma=exp(sigma)dmu, test against a compactly supported vector X.
The exact weak identity is
  int m_q(X) dmu_sigma = int [2 H:symgrad X - trH div_sigma X
                               + T div X - <Z,dU(X)>] dmu_sigma.
The T-term is ordinary div X (not div_sigma X) because dT+T dsigma is
integrated together against exp(sigma)dmu.
"""
from pathlib import Path
import json
import sympy as sp

# Pure coefficient check after weighted integration by parts.
Hsym, trH, divsX, TXdiv, Zterm = sp.symbols('Hsym trH divsigmaX TdivX Zterm')
# int 2 div_sigma H . X = -2 int H:symgrad X
# int -dtrH . X = + int trH div_sigma X
# RHS = int[-dT.X-T dsigma.X-Zterm-mqX]
# first two T terms combine to int T div X.
mq_from_equation = sp.expand(2*Hsym-trH*divsX+TXdiv-Zterm)
expected=2*Hsym-trH*divsX+TXdiv-Zterm

# Radial moment coefficient.
r=sp.symbols('r')
mu=sp.Function('mu')(r)
C=sp.Function('C')(r)
w=sp.Function('w')(r)
b=sp.Function('b')(r)
# C'+2(u+h)C=-wb and mu'/mu=2(u+h), so (mu C)'=-mu wb.
up_h=sp.diff(mu,r)/(2*mu)
radial_res=sp.simplify(sp.diff(mu*C,r)-mu*(sp.diff(C,r)+2*up_h*C))

out={
  'strong_identity':'2 div_sigma H-d trH=-dT-T dsigma-<Z,dU>-m_q',
  'weak_identity':'int m_q(X)dmu_sigma=int[2H:symgradX-trH div_sigmaX+T divX-<Z,dU(X)>]dmu_sigma',
  'coefficient_residual':str(sp.expand(mq_from_equation-expected)),
  'radial_integrating_factor_identity':'(mu C) prime = mu(C prime+2(u+h)C), mu=e^(2sigma)psi^2',
  'radial_symbolic_residual':str(radial_res),
  'radial_two_end_moment':'If C=0 at both ends and T=Z=0, integral mu*w*b dr=0.',
  'scope':'The pairing removes derivatives from C0 Ricci-defect blocks but gives no coercive estimate until a geometrically controlled adjoint field X is found.',
}
assert out['coefficient_residual']=='0'
assert out['radial_symbolic_residual']=='0'
path=Path('workspace/data/step94_horizontal_flux_pairing.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'wrote {path}')
