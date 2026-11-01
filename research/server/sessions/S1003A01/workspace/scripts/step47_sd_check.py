"""Step 47 auxiliary: (anti)self-duality of the two GH 2-form types, checked in the
orthonormal coframe E1=sqrt(V)dr, E2=sqrt(V) r dth, E3=sqrt(V) r sin th dph, E4=eta/sqrt(V),
orientation E1234 (= dr dth dph dpsi up to the positive factor V r^2 sin th)."""
import sympy as sp
r, th, ph, ps, ell = sp.symbols('r theta phi psi ell', positive=True)
V = 1 + ell/r
X = [r, th, ph, ps]
# coframe matrix: E^a = C[a,i] dx^i
C = sp.Matrix([[sp.sqrt(V), 0, 0, 0],
               [0, sp.sqrt(V)*r, 0, 0],
               [0, 0, sp.sqrt(V)*r*sp.sin(th), 0],
               [0, 0, ell*sp.cos(th)/sp.sqrt(V), 1/sp.sqrt(V)]])
Ci = sp.simplify(C.inv())
eta = [0, 0, ell*sp.cos(th), 1]
def wedge11(a, b):
    return sp.Matrix(4, 4, lambda i, j: a[i]*b[j] - a[j]*b[i])
def star3_base(a):
    ar, ath, aph = a
    M = sp.zeros(4, 4)
    M[1, 2] += ar*r**2*sp.sin(th); M[2, 1] -= ar*r**2*sp.sin(th)
    M[2, 0] += ath*sp.sin(th);     M[0, 2] -= ath*sp.sin(th)
    M[0, 1] += aph/sp.sin(th);     M[1, 0] -= aph/sp.sin(th)
    return M
def beta(h, sign):
    dh = [sp.diff(h, r), sp.diff(h, th), sp.diff(h, ph), 0]
    return wedge11(eta, dh) + sign*V*star3_base(dh[:3])
def frame(B):  # B_ab in frame: B = sum_{i<j} B_ij dx^i dx^j ; frame comps Ci^T B Ci
    return sp.simplify(Ci.T*B*Ci)
def frame_star(F):
    S = sp.zeros(4, 4)
    for k in range(4):
        for l in range(4):
            S[k, l] = sum(sp.LeviCivita(i, j, k, l)*F[i, j] for i in range(4) for j in range(4))/2
    return S
x3 = r*sp.cos(th); x1 = r*sp.sin(th)*sp.cos(ph)
import json, os
rec = {}
for name, h in [('x3', x3), ('x3/V', x3/V), ('x1', x1)]:
    for sgn, lab in [(1, 'minus_type (eta^dh + V*dh)'), (-1, 'plus_type (eta^dh - V*dh)')]:
        F = frame(beta(h, sgn))
        S = frame_star(F)
        sd = sp.simplify(S - F) == sp.zeros(4, 4); asd = sp.simplify(S + F) == sp.zeros(4, 4)
        rec[f'{lab} h={name}'] = dict(self_dual=bool(sd), anti_self_dual=bool(asd))
        print(lab, name, 'SD:', sd, 'ASD:', asd)
od = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step47'); os.makedirs(od, exist_ok=True)
with open(os.path.join(od, 'gh_two_form_types_frame_check.json'), 'w') as fh:
    json.dump(dict(note='orthonormal-frame Hodge check; supersedes the self_dual/anti_self_dual booleans in tn_core_exact.json, which failed to simplify |sin theta|', results=rec), fh, indent=1)
# endpoint forms in frame: Omega_+- = E12 +- E34 relative to the base x3 axis are E^{x1 x2} +- E^{x3,4};
F = frame(beta(x3, 1)); print('minus_type x3 frame comps (should be +-Omega_- pattern at large r):')
sp.pprint(sp.simplify(F.subs(th, sp.pi/2)))
