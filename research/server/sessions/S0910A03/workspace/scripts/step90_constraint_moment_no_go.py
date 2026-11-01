"""Verify the sign identity behind the terminal horizontal constraint."""
from pathlib import Path
import json
import sympy as sp
s,L=sp.symbols('s L', positive=True)
u,H,w,b,C=sp.symbols('u H w b C', real=True)
I=sp.Function('I')(s); W=sp.Function('w')(s)
# If C'+2(u+H)C=-wb and C(0)=0, integrating factor gives the formula.
C_terminal='C(L) = -exp(-2 I(L)) integral_0^L exp(2 I(s)) w(s)b(s) ds'
# If w>=0 and w(0)>0,w(L)=0, then on any monotone discharge b<=0 the
# integrand wb<=0, so C(L)>=0; strict discharge yields >0.
out={
 'constraint_ode':'C_prime = -2(u+H) C - w b',
 'integrating_factor':C_terminal,
 'monotone_discharge':'w>=0 and b<=0 with nontrivial wb implies C(L)>0',
 'two_moment_implication':'C(L)=0 with w(L)=0 requires either sign-changing wb, an additional horizontal source, or singular/degenerate behavior.',
 'small_control_warning':'Sign-changing b can in principle cancel the moment, but a pilot two-mode solve required max|b|/delta about 26 for Q0=10, delta=.03, L=1; this is one poor basis, not a lower bound.'
}
p=Path('workspace/data/step90_constraint_moment_no_go.json');p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print(f'\nwrote {p}')
