#!/usr/bin/env python3
"""Step 86: algebra for the combined orbit/area gradient energy W=e+cX.

Here e=|dU|^2, X=|grad sigma|^2, T=tr_orbit(E), q=6-T,
and L sigma=q.  Combining the forced orbit-map Bochner identity with the
weighted scalar Bochner identity for sigma removes derivatives of T into
one divergence field J=V-c*T*grad(sigma).

The script verifies the optimal quadratic lower bound and records explicit
forcing/root constants, especially for c=1/2.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

e, X, c, W, delta = sp.symbols('e X c W delta', nonnegative=True)

# Quadratic minimization: 1/2 e^2 + c/2 X^2 >= W^2/[2(1+c)]
quad = sp.Rational(1,2)*e**2 + sp.Rational(1,2)*c*X**2
constraint_sub = sp.expand(quad.subs(e, W-c*X))
Xcrit = sp.simplify(sp.solve(sp.diff(constraint_sub, X), X)[0])
quad_min = sp.simplify(constraint_sub.subs(X, Xcrit))
quad_target = W**2/(2*(1+c))

# Error bounds under ||E||op<=delta:
# |F|<=2delta, |T|<=2delta, q=6-T so |T q|<=2delta(6+2delta).
D = sp.expand(4*delta**2 + c*2*delta*(6+2*delta))
a = 3+delta
root = sp.simplify((1+c)*(a+sp.sqrt(a**2+2*D/(1+c))))

# c=1/2 explicit root and expansion
root_half = sp.simplify(root.subs(c, sp.Rational(1,2)))
root_half_series = sp.series(root_half, delta, 0, 3).removeO()
center_floor = 12-8*delta
center_gap_series = sp.expand(center_floor-root_half_series)

# Combined divergence field norm:
# |V|<=2delta sqrt(e); |c T grad sigma|<=2c delta sqrt(X).
# By e<=W and cX<=W, |J|<=2(1+sqrt(c)) delta sqrt(W).
Jcoeff = 2*(1+sp.sqrt(c))*delta

out = {
    'definitions': {
        'e':'|dU|^2', 'X':'|grad sigma|^2', 'W':'e+cX',
        'T':'tr_orbit E', 'q':'6-T=L sigma',
        'J':'V-c*T*grad sigma'
    },
    'sigma_bochner_derivative_rewrite': (
        '-<grad sigma,grad T> = -div_sigma(T grad sigma)+T(6-T)'
    ),
    'combined_inequality': (
        '1/2 L W >= positive Hessian/stress terms + div_sigma J '
        '+ W^2/[2(1+c)] -(3+delta)W - D(c,delta)'
    ),
    'quadratic_constraint_expression': str(constraint_sub),
    'quadratic_minimizer_X': str(Xcrit),
    'quadratic_minimum': str(quad_min),
    'quadratic_residual': str(sp.simplify(quad_min-quad_target)),
    'forcing_constant_D': str(D),
    'positive_reaction_root_kc': str(root),
    'J_norm_bound_coarse': f'|J| <= ({sp.sstr(Jcoeff)})*sqrt(W)',
    'J_norm_bound_sharp_vertical': '|T|+|F|<=2 delta implies |J|<=2 delta max(1,sqrt(c))*sqrt(W)',
    'gradient_coercivity': '|DdU|^2+c|Hess sigma|^2 >= |grad W|^2/(4W)',
    'c_half': {
        'root_exact': str(root_half),
        'root_series': str(root_half_series),
        'center_floor': str(center_floor),
        'center_floor_minus_root_series': str(center_gap_series),
        'zero_defect_threshold': 9,
        'zero_defect_center_gap': 3,
        'J_coefficient': str(sp.simplify(Jcoeff.subs(c,sp.Rational(1,2))))
    },
    'conditional_cheeger': (
        'If W<=B on a domain and delta<3, then |grad sigma|<=sqrt(B/c). Since L sigma>=6-2delta, '
        'the Dirichlet/compact-support weighted Cheeger constant is at least (6-2delta)*sqrt(c/B), hence '
        'lambda_1^Dir(-L)>=c*(6-2delta)^2/(4B). This is not a Neumann gap.'
    ),
    'superlevel_cheeger': 'For a regular relatively compact component Omega_t of {W>t}: P_mu(Omega_t)>= (6-2delta)*sqrt(c/t)*mu(Omega_t).',
    'all_symbolic_zero_checks': bool(sp.simplify(quad_min-quad_target)==0)
}

path=Path(__file__).resolve().parents[1]/'data'/'step86_combined_orbit_area_energy.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print(f'wrote {path}')
