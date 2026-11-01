"""
Step 14 (S0910A02): S^4 anchor verification of the corrected K_B formula.

On S^4(sqrt(3)) with standard T^2-rotation, the orbit space is a spherical
lune on S^2(sqrt(3)) with K_B = 1/3 constant.

Coordinates: r_1 = sqrt(3) sin psi cos phi, r_2 = sqrt(3) sin psi sin phi,
t = sqrt(3) cos psi. Orbit space: psi in [0,pi], phi in [0,pi/2].
g_B = 3(dpsi^2 + sin^2 psi dphi^2).
p = r_1 = sqrt(3) sin psi cos phi, q = r_2 = sqrt(3) sin psi sin phi.
w = pq = 3 sin^2 psi sin phi cos phi = (3/2) sin^2 psi sin(2 phi).
v = log(cos phi / sin phi) = log(cot phi) = -log(tan phi).

Rod at phi=0: q=0, rod of psi from 0 to pi.
Rod at phi=pi/2: p=0, rod of psi from 0 to pi.
Corners at (psi=0,phi=0) and (psi=pi,phi=0) ... wait, at psi=0 AND psi=pi,
BOTH r_1=r_2=0, so both are T^2-fixed points. Similarly for (psi=0,phi=pi/2)
and (psi=pi,phi=pi/2). But the orbit space is a lune with only TWO corners
(at psi=0 and psi=pi), each with angle pi/2.

CHECK: K_B = (1/4)(|grad v|^2 - |grad log w|^2).
Using g_B = 3 dpsi^2 + 3 sin^2 psi dphi^2.

grad v = (0, -1/(sin phi cos phi)) / sqrt(3) in ON frame.
|grad v|^2 = 1/(3 sin^2 psi sin^2 phi cos^2 phi).

log w = log 3 + 2 log sin psi + log sin phi + log cos phi.
grad log w = (2 cot psi / sqrt(3), (cot phi - tan phi)/(sqrt(3) sin psi)).
|grad log w|^2 = (4 cot^2 psi)/3 + cos^2(2phi)/(3 sin^2 psi sin^2 phi cos^2 phi).

|grad v|^2 - |grad log w|^2
= 1/(3 sin^2 psi sin^2 phi cos^2 phi) - 4 cot^2 psi / 3 - cos^2(2phi)/(3 sin^2 psi sin^2 phi cos^2 phi)
= (1 - cos^2(2phi))/(3 sin^2 psi sin^2 phi cos^2 phi) - 4 cot^2 psi / 3
= sin^2(2phi)/(3 sin^2 psi sin^2 phi cos^2 phi) - 4 cot^2 psi / 3
= 4/(3 sin^2 psi) - 4 cos^2 psi/(3 sin^2 psi)
= 4(1 - cos^2 psi)/(3 sin^2 psi)
= 4/3.

K_B = (1/4)(4/3) = 1/3.  ✓  (constant positive curvature of S^2(sqrt(3)))

This is a STRONG independent anchor for the corrected formula.

EDGE EQUATION CHECK:
The corrected edge equation is Q'' + (1 - 2 K_B|_edge) Q = 0.
For S^4: K_B = 1/3, so Q'' + (1/3)Q = 0, omega = 1/sqrt(3).
Rod length: L = pi/omega = sqrt(3) pi (matches arclength on S^2(sqrt(3))).
Rod flux: Phi = 2/omega^2 = 2*3 = 6.  ✓  (matches step13 anchor data).
Total flux = 2 * 6 = 12.  2 int w = 12.  int w = 6.  Vol = 24 pi^2.  ✓
"""
import json, math, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# Symbolic check on S^4 orbit space
psi, phi = sp.symbols('psi phi', positive=True)
R2 = sp.Integer(3)  # radius^2

p_s4 = sp.sqrt(R2) * sp.sin(psi) * sp.cos(phi)
q_s4 = sp.sqrt(R2) * sp.sin(psi) * sp.sin(phi)
w_s4 = p_s4 * q_s4
v_s4 = sp.log(sp.cos(phi) / sp.sin(phi))

# Base metric: g_B = R^2 (dpsi^2 + sin^2(psi) dphi^2)
# g^{psi psi} = 1/R^2, g^{phi phi} = 1/(R^2 sin^2 psi)
ginv = {(0,0): 1/R2, (1,1): 1/(R2 * sp.sin(psi)**2)}

logw = sp.log(w_s4)
dlogw = [sp.diff(logw, psi), sp.diff(logw, phi)]
dv = [sp.diff(v_s4, psi), sp.diff(v_s4, phi)]

norm2_dv = sp.simplify(ginv[(0,0)] * dv[0]**2 + ginv[(1,1)] * dv[1]**2)
norm2_dlogw = sp.simplify(ginv[(0,0)] * dlogw[0]**2 + ginv[(1,1)] * dlogw[1]**2)
KB_computed = sp.simplify(sp.Rational(1,4) * (norm2_dv - norm2_dlogw))

# Also check via -<grad log p, grad log q>
dlogp = [sp.diff(sp.log(p_s4), psi), sp.diff(sp.log(p_s4), phi)]
dlogq = [sp.diff(sp.log(q_s4), psi), sp.diff(sp.log(q_s4), phi)]
inner = sp.simplify(ginv[(0,0)]*dlogp[0]*dlogq[0] + ginv[(1,1)]*dlogp[1]*dlogq[1])
KB_inner = sp.simplify(-inner)

# Edge equation check
omega_s4 = sp.sqrt(1 - 2 * sp.Rational(1,3))  # = 1/sqrt(3)
L_s4 = sp.pi / omega_s4  # = sqrt(3) pi
Phi_s4 = 2 / omega_s4**2  # = 6

report = {
    "title": "Step 14: S^4 anchor for corrected K_B formula",
    "K_B_from_gradient_formula": str(KB_computed),
    "K_B_from_inner_product": str(KB_inner),
    "expected_K_B": "1/3 (S^2(sqrt(3)))",
    "check": str(sp.simplify(KB_computed - sp.Rational(1,3))),
    "edge_equation": {
        "K_B_at_edge": "1/3",
        "omega": str(omega_s4),
        "rod_length_L": str(L_s4),
        "rod_flux_Phi": str(Phi_s4),
        "total_flux": str(2 * Phi_s4),
        "int_w": str(Phi_s4),  # total flux / 2
        "Vol_4": str(4 * sp.pi**2 * Phi_s4),
    },
    "KEY_EDGE_EQUATION_CORRECTED": {
        "equation": "Q'' + (1 - 2 K_B|_edge) Q = 0",
        "boundary_conditions": "Q(0)=0, Q'(0)=1, Q(L)=0, Q'(L)=-1",
        "flux": "Phi = int_0^L Q ds = 2 / (1-2K_B) when K_B is constant on edge",
        "positive_K_B": "EXPANDS rod (omega < 1, L > pi, Phi > 2)",
        "negative_K_B": "SHRINKS rod (omega > 1, L < pi, Phi < 2)",
        "large_negative_K_B": "Phi -> 0, L -> 0, rod disappears"
    }
}

OUT = os.path.join(DATA, "step14_S4_KB_anchor.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"\nSaved {OUT}")
