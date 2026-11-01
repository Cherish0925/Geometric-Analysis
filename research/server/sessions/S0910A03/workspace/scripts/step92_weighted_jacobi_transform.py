"""Step 92 symbolic conjugation of the weighted separator Jacobi operator."""
from pathlib import Path
import json
import sympy as sp

s = sp.symbols('s', real=True)
sigma = sp.Function('sigma')(s)
y = sp.Function('y')(s)
a = sp.Function('a')(s)
V = sp.Function('V')(s)
phi = sp.exp(-sigma/2) * y
Lphi = -sp.exp(-sigma) * sp.diff(sp.exp(sigma) * sp.diff(phi, s), s) + (a - V) * phi
conjugated = sp.simplify(sp.expand(sp.exp(sigma/2) * Lphi))
target = -sp.diff(y, s, 2) + (a - V + sp.diff(sigma, s, 2)/2 + sp.diff(sigma, s)**2/4) * y
residual = sp.simplify(conjugated - target)

# Express sigma''/2+sigma'^2/4 using R=-2sigma''-(3/2)sigma'^2-e_s/2.
R, es, h = sp.symbols('R e_s h', real=True)
sigma2_from_R = -R/2 - sp.Rational(3,4)*h**2 - sp.Rational(1,4)*es
weight_potential = sp.simplify(sigma2_from_R/2 + h**2/4)
# At a minimal separator R=-6+D-V (because V=|II|^2), with a=3-E_nunu.
D, Enu = sp.symbols('D E_nunu', real=True)
minsep_weight = sp.expand(weight_potential.subs(R, -6 + D - V))
full_potential = sp.expand((3-Enu) - V + minsep_weight)

out = {
    'conjugated_operator': str(conjugated),
    'target': str(target),
    'residual': str(residual),
    'weight_potential_via_intrinsic_R': str(weight_potential),
    'minimal_separator_weight_potential': str(minsep_weight),
    'full_schrodinger_potential_at_separator': str(full_potential),
    'interpretation': 'After using Gauss and intrinsic scalar curvature, the |II|^2 coefficient is -3/4 rather than -1; tangential e_s and h^2 also enter negatively. No cancellation yields a nonnegative pointwise potential.'
}
path = Path('workspace/data/step92_weighted_jacobi_transform.json')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f'wrote {path}')
