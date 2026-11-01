"""
Step 92: verify the constants in the separator Jacobi + Maxwell sup(Q) estimate.

Input inequalities on a circle C:
  Wcal=(3/4)V+(1/8)(h^2+e_s),
  int Wcal y^2 <= int(y'^2+a_delta y^2), a_delta=9/2+3delta/2,
  Q <= (4/3)Wcal,
  |w'| <= c w+B, w=sqrt(2Q), c=(3/2)|h|+(1/2)sqrt(e_s),
  c^2 <= (5/2)(h^2+e_s) <= 20 Wcal,
  B=2sqrt(2)delta.

For L>=2/sqrt(a), use a tent centered at a Q maximum with support radius r=1/sqrt(a)
and inner radius r/2. It yields int_inner Wcal <= M=8/r+(8/3)ar,
then a point Q0 <= (4/3)M/r and integral c <= sqrt(20 M r).
Gronwall bounds w_max <= exp(Cint)*(sqrt(2Q0)+B*r/2).
For short circles use y=1 globally and the shorter arc.
"""
from pathlib import Path
import json
import math


def bounds(delta: float):
    a = 4.5 + 1.5 * delta
    r = 1 / math.sqrt(a)
    M = 8/r + (8/3)*a*r  # 32/3 sqrt(a)
    Q0_long = (4/3)*M/r  # 128/9 a
    Cint_long = math.sqrt(20*M*(r/2))  # distance/path is at most r/2
    B = 2*math.sqrt(2)*delta
    w_long = math.exp(Cint_long)*(math.sqrt(2*Q0_long)+B*r/2)
    Q_long = w_long*w_long/2

    # L<2/sqrt(a): int W <= aL, hence some Q0 <= 4a/3.
    # Shorter arc d<=L/2<1/sqrt(a).  int_path c <= sqrt(20*a*L*d)
    # <= sqrt(40), and source length <=1/sqrt(a).
    Q0_short = 4*a/3
    Cint_short = math.sqrt(40)
    w_short = math.exp(Cint_short)*(math.sqrt(2*Q0_short)+B/math.sqrt(a))
    Q_short = w_short*w_short/2
    return {
        'delta': delta,
        'a_delta': a,
        'long_case': {
            'r': r,
            'tent_mass_M': M,
            'Q0_bound': Q0_long,
            'transport_exponent_bound': Cint_long,
            'sup_Q_bound': Q_long,
        },
        'short_case': {
            'Q0_bound': Q0_short,
            'transport_exponent_bound': Cint_short,
            'sup_Q_bound': Q_short,
        },
        'uniform_sup_Q_bound': max(Q_long, Q_short),
    }

rows = [bounds(d) for d in (0.0, 0.01, 0.1, 0.25, 1.0)]
out = {
    'algebraic_checks': {
        'c_squared_bound': '(3|h|/2+sqrt(e_s)/2)^2 <= (5/2)(h^2+e_s) <= 20 Wcal',
        'long_tent': 'M=8/r+(8/3)a r, r=a^(-1/2), Q0<=(4/3)M/r=(128/9)a',
        'long_transport': 'int c <= sqrt(20*M*r/2)=sqrt(320/3)',
        'short_transport': 'L<2/sqrt(a), d<=L/2 gives int c <= sqrt(20*a*L*d)<sqrt(40)',
        'status': 'constants checked from stated inequalities; deliberately coarse',
    },
    'rows': rows,
    'meaning': 'finite separator sup(Q) depending only on delta; no smallness as delta->0 and no interior Q_+ bound',
}
path = Path('workspace/data/step92_jacobi_maxwell_bound.json')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f'wrote {path}')
