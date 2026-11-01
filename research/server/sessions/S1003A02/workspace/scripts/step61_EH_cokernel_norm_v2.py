#!/usr/bin/env python3
"""Independent exact moving-frame check of EH harmonic form/cokernel normalization.

Conventions:
 dsigma_1=-sigma_2^sigma_3, cyclic;
 g=dr^2/f+r^2(sigma1^2+sigma2^2+f sigma3^2)/4,
 f=1-a^4/r^4; RP^3 orbit volume is pi^2 r^3 sqrt(f).
"""
import json
from pathlib import Path
import sympy as sp

r,a=sp.symbols('r a', positive=True)
f=1-a**4/r**4
# e0=dr/sqrt(f), e1=r*s1/2, e2=r*s2/2, e3=r*sqrt(f)*s3/2.
# d(s3/r^2)= -2 dr^s3/r^3 - s1^s2/r^2
# = -4/r^4 (e0^e3+e1^e2), self-dual for orientation e0e1e2e3.
F_coeff_03=sp.simplify(-2/r**3 * (sp.sqrt(f)) * (2/(r*sp.sqrt(f))))
F_coeff_12=sp.simplify(-1/r**2 * (2/r)*(2/r))
# 2-form tensor norm has |e^i wedge e^j|^2_endo=2.
F_norm_endo=sp.simplify(2*(F_coeff_03**2+F_coeff_12**2))
# Omega=(-1/4)F -> coefficients +1/r^4, endomorphism norm 4/r^8.
Om_norm_endo=sp.simplify(F_norm_endo/16)
# radial shell density: orbit area pi^2 r^3 sqrt(f), times dr/sqrt(f).
shell=sp.pi**2*r**3
L2=sp.integrate(sp.simplify(Om_norm_endo*shell),(r,a,sp.oo))

out={
 "status":"exact moving-frame verification",
 "structure_equations":"d sigma_i = - sigma_j wedge sigma_k cyclic",
 "F_coeff_e03":str(F_coeff_03),
 "F_coeff_e12":str(F_coeff_12),
 "F_duality":"self-dual for orientation e0,e1,e2,e3; reversing orientation makes it ASD",
 "Omega_definition":"Omega=-(1/4)d(sigma3/r^2)",
 "Omega_endo_norm_sq":str(Om_norm_endo),
 "radial_shell_density":str(shell),
 "cokernel_tensor_norm_sq":str(L2),
 "expected":"pi**2/a**4"
}
assert sp.simplify(F_coeff_03-F_coeff_12)==0
assert sp.simplify(Om_norm_endo-4/r**8)==0
assert sp.simplify(L2-sp.pi**2/a**4)==0
path=Path(__file__).resolve().parents[1]/'data'/'step61_EH_cokernel_norm_v2.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
