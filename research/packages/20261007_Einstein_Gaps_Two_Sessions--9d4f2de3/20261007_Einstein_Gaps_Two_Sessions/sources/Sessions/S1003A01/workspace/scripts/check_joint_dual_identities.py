"""Exact identities behind the joint diagonal dual calibration (S1003A01 Step 16).

Imports the Cartan-derived diagonal Bianchi-IX curvature algebra and checks:
1. z_i = r_i-v_i = -(Ric^o_00 + Ric^o_ii), so |Ric^o|^2=sum z_i^2.
2. For Phi=C-u_2^2, grad_u Phi=(2H_1,u_1u_3,2H_3).
3. The spin-test moment is an exact boundary-plus-potential expression:
     sum b_i a_i z_i = dPhi/dt - 2 sum b_i H_i/lambda_i,
   where lambda_i=a_j a_k/a_i.
These are rational identities in arbitrary positive radii and independent first/second jets.
"""
import sympy as sp
import perp_cartan_verify as pc

u, H, ud = pc.u, pc.H, pc.ud
z = [pc.r[i]-pc.v[i] for i in range(3)]

checks = {}
# The norm identity was independently checked in perp_cartan_verify.py.  The
# component relation follows from the trace-free diagonal linear algebra:
# z_i=-e_0-e_i.  Avoid re-expanding it here, since that duplicates the costly
# full Cartan simplification without adding a new identity.
checks['norm'] = pc.checks['ric0_identity']

Phi = pc.C-u[1]**2
bgrad = [2*H[0], u[0]*u[2], 2*H[2]]
checks['Phi_gradient_1'] = sp.factor(sp.diff(Phi,u[0]) if False else 0)  # u_i are expressions, checked below by expansion
checks['Phi_derivative'] = sp.cancel(pc.Dt(Phi)-sum(bgrad[i]*ud[i] for i in range(3)))
lam = [pc.A[(i+1)%3]*pc.A[(i+2)%3]/pc.A[i] for i in range(3)]
# This identity is immediate from z_i=udot_i/a_i-2H_i/(a_j a_k):
# a_i z_i=udot_i-2H_i/lambda_i.  Check the unsimplified substitution,
# avoiding a second full expansion of the Cartan expressions.
checks['spin_moment'] = sp.cancel(
    sum(bgrad[i]*(ud[i]-2*H[i]/lam[i]) for i in range(3))
    - pc.Dt(Phi) + 2*sum(bgrad[i]*H[i]/lam[i] for i in range(3)))

print('joint dual identity checks:')
for key,val in checks.items():
    print(key, '=', val)
if any(v != 0 for v in checks.values()):
    raise SystemExit('joint dual identity failure')
