"""Step 91: exact check of |nabla tau|^2 = (1/2) Delta_g |tau|^2 on Taub-NUT (GH form),
and the per-core integral 8 pi^2 m* ell^2, and the Wigner-Seitz cell volume 4 pi^2 ell^2.
Conventions as Step 47: V=1+ell/r, |tau|^2=m*/V, |Hess fbar|^2=2 ell^2/(r+ell)^4,
|nabla tau|^2 = 2 rho*^2 a^2 |Hess fbar|^2, rho*=4/3, a^2=2/9, m*=128/81.
"""
import sympy as sp, json, os
r, l = sp.symbols('r ell', positive=True)
rho, a2, m = sp.Rational(4,3), sp.Rational(2,9), sp.Rational(128,81)
V = 1 + l/r
tau2 = m/V
lap_R3 = sp.diff(r**2*sp.diff(tau2, r), r)/r**2
lap_g = sp.simplify(lap_R3/V)
grad2 = 2*rho**2*a2*2*l**2/(r+l)**4
res1 = sp.simplify(lap_g/2 - grad2)
core = sp.simplify(16*sp.pi**2*l*sp.integrate(grad2*V*r**2, (r, 0, sp.oo)))
res2 = sp.simplify(core - 8*sp.pi**2*m*l**2)
cell = sp.simplify(core/(2*m))  # volume per core so that mean q = 2 m*
out = {"half_lap_minus_grad2": str(res1), "core_int": str(core), "core_minus_8pi2mell2": str(res2),
       "cell_volume_for_mean_2mstar": str(cell), "rho2a2_times2": str(2*rho**2*a2), "mstar": str(m)}
print(json.dumps(out, indent=1))
od = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step91')
os.makedirs(od, exist_ok=True)
json.dump(out, open(os.path.join(od, 'tn_mean_identity.json'), 'w'), indent=1)
