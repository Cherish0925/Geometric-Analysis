"""
Step 94: exact 1D countermodel to the false maximum-principle inference.
Solve y''=-18-4 exp(y), y(0)=log Q0, y'(0)=0.
Then Q=exp(y) has a strict positive maximum Q0 at 0 and tends to zero
as |x|->infinity. The first integral is
  (y')^2 = 36(log Q0-y)+8(Q0-exp(y)).
This is a scalar sign check only, not a reduced Einstein solution.
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp

Q0_values=[0.01,0.1,1.0,10.0]
R=8.0
records=[]
for Q0 in Q0_values:
    y0=np.log(Q0)
    def rhs(x,Y):
        y,v=Y
        return [v,-18.0-4.0*np.exp(y)]
    sol=solve_ivp(rhs,[0,R],[y0,0.0],rtol=1e-11,atol=1e-13,dense_output=False,max_step=0.005)
    x=sol.t; y=sol.y[0]; v=sol.y[1]; Q=np.exp(y)
    first=v*v-(36.0*(y0-y)+8.0*(Q0-Q))
    # concatenate the even extension conceptually; derivative zero at center.
    records.append({
        'Q0':Q0,
        'Q_at_R':float(Q[-1]),
        'logQ_at_R':float(y[-1]),
        'Q_monotone_nonincreasing_on_positive_half':bool(np.all(np.diff(Q)<=1e-13)),
        'center_second_derivative_Q':float(Q0*(-18.0-4.0*Q0)),
        'max_first_integral_residual':float(np.max(np.abs(first))),
        'asymptotic_log_slope_at_R':float(v[-1]),
    })
out={
    'equation':'y_second=-18-4 exp(y)',
    'initial_data':'y(0)=log Q0, y_prime(0)=0',
    'first_integral':'y_prime^2=36(log Q0-y)+8(Q0-exp(y))',
    'mathematical_conclusion':'For every Q0>0 the even solution has Q=exp(y) with strict positive interior maximum Q0 and Q->0 at both infinities. Thus L log Q<0 is compatible with a positive interior maximum.',
    'scope':'Scalar sign countermodel only; it does not solve the coupled T2-reduced Einstein equations.',
    'runs':records,
}
path=Path('workspace/data/step94_scalar_superharmonic_countermodel.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'wrote {path}')
