#!/usr/bin/env python3
"""Verify the center angular-slip cancellation and radial sign in H^2 polar variables."""
import json
from pathlib import Path
import sympy as sp
d,m,k,A,B=sp.symbols('d m k A B', positive=True, nonzero=True)
s,c=sp.sinh(d),sp.cosh(d)
# Background U=(d,mz); perturb delta d=A cos(kz), delta psi=B sin(kz).
# First variation of tangential H2 energy |U_z|^2=sinh^2(d) psi_z^2.
delta_energy=sp.expand(2*s*c*m**2*A+2*s**2*m*k*B)
B_slip=-m*c*A/(k*s)
energy_after=sp.simplify(delta_energy.subs(B,B_slip))
# Linearized d equation at reflected center, sigma_r=0:
# A''-k^2 A = m^2 cosh(2d) A + 2mk sinh(d)cosh(d) B.
Add=sp.simplify(k**2*A+m**2*sp.cosh(2*d)*A+2*m*k*s*c*B_slip)
# Uniform scalar-minus-six center requires m^2 sinh^2 d=12.
sigma_rr=6
lambda_rr=sp.simplify(-(m**2*s**2)/4)
d0_rr=sp.simplify(m**2*s*c)
out={
 'first_variation_tangential_energy':str(delta_energy),
 'angular_slip_relation':str(B_slip),
 'energy_variation_after_slip':str(energy_after),
 'perturbation_radial_acceleration_after_slip':str(Add),
 'expected_Arr':'A*(k**2-m**2)',
 'A_sign_residual':str(sp.simplify(Add-A*(k**2-m**2))),
 'scalar_minus6_condition':'m**2*sinh(d)**2=12',
 'center_jets_under_condition':{
   'sigma_rr':str(sigma_rr),
   'lambda_rr':str(lambda_rr.subs(m**2,12/s**2)),
   'background_d_rr':str(d0_rr.subs(m**2,12/s**2)),
 },
 'periodicity_note':'m and k must obey the polar-angle/global orbit-matrix periodicity convention; choosing m>=2 permits an integer k<m.',
 'scope':'linearized center sign only; zero and 2k backreaction and full constraints remain unsolved',
}
p=Path(__file__).resolve().parents[1]/'data'/'step80_angular_slip.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));print('wrote',p)
