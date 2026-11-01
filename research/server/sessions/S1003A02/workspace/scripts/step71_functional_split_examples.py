"""Step 71: exact checks of the all-metric identity
    E(g) = (4P + L_s)/R = 1 + (12 W_+ + L_s - 24 pi^2 T_+)/R ,   T_+ = 2chi + 3tau,
on explicit metrics (R = int|Ric|^2 > 0), plus the Yamabe-normalised ASD family formula.
Conventions (LeBrun): 8pi^2 chi = int(|W|^2 + s^2/24 - |Ric0|^2/2), 12 pi^2 tau = int(|W+|^2-|W-|^2).
Output: workspace/data/step71_functional_split_examples.json
"""
import json, os
import sympy as sp

pi = sp.pi
out = {}

def record(name, ric_eigs, vol, chi, tau, Wp, Wm):
    """ric_eigs: constant Ricci eigenvalues (homogeneous metric), vol: volume,
    Wp, Wm: integrated |W+|^2, |W-|^2."""
    e = [sp.nsimplify(x) for x in ric_eigs]
    s = sum(e)
    ric0 = [x - s/4 for x in e]
    P = sum(x**2 for x in ric0)*vol
    R = sum(x**2 for x in e)*vol
    Ls = 0
    gb = sp.simplify(Wp + Wm + s**2/24*vol - P/2 - 8*pi**2*chi)
    sig = sp.simplify(Wp - Wm - 12*pi**2*tau)
    Tp = 2*chi + 3*tau
    if R == 0:
        E1 = E2 = sp.Integer(4)
    else:
        E1 = sp.simplify((4*P + Ls)/R)
        E2 = sp.simplify(1 + (12*Wp + Ls - 24*pi**2*Tp)/R)
    # direct definition: 4 - T^2/(R V)
    T = s*vol
    E0 = sp.Integer(4) if R == 0 else sp.simplify(4 - T**2/(R*vol))
    out[name] = dict(chi=str(chi), tau=str(tau), T_plus=str(Tp), T_minus=str(2*chi-3*tau),
                     P=str(sp.simplify(P)), R=str(sp.simplify(R)), E_def=str(E0),
                     E_formula=str(E1), E_identity=str(E2),
                     gauss_bonnet_residual=str(gb), signature_residual=str(sig),
                     consistent=bool(sp.simplify(E0-E1) == 0 and sp.simplify(E1-E2) == 0 and gb == 0 and sig == 0))

L, g = sp.symbols('L g', positive=True)
V_S4 = 8*pi**2/3
record('round S4', [3, 3, 3, 3], V_S4, 2, 0, 0, 0)
record('CP2 Fubini-Study (Ric=6g)', [6, 6, 6, 6], pi**2/2, 3, 1, 12*pi**2, 0)
record('S1(L) x S3(1)', [0, 2, 2, 2], 2*pi**2*L, 0, 0, 0, 0)
vH = sp.symbols('v_H', positive=True)   # volume of hyperbolic 3-manifold
record('S1(L) x H3/Gamma', [0, -2, -2, -2], L*vH, 0, 0, 0, 0)
record('Sigma_g(-1) x S2(+1), g>=2', [-1, -1, 1, 1], 4*pi*(g-1)*4*pi, 4-4*g, 0, 0, 0)
vX = sp.symbols('V_X', positive=True)
record('compact hyperbolic 4-manifold', [-3, -3, -3, -3], vX, 3*vX/(4*pi**2), 0, 0, 0)
record('K3 Ricci-flat', [0, 0, 0, 0], 1, 24, -16, 0, 192*pi**2)

# Yamabe-normalised ASD (W+=0) constant-s metric on k CPbar^2 # l (S1xS3):
k, l, Y2 = sp.symbols('k l Y2', real=True)
chi = 2 + k - 2*l; tau = -k
Wm = 12*pi**2*k; Wp = 0
# constant s, int s^2 = Y^2 ; GB gives P
P = 2*(Wm + Y2/24 - 8*pi**2*chi)
R = P + Y2/4
E = sp.simplify((4*P)/R)
m, y = sp.symbols('m y')
E_my = sp.simplify(E.subs(Y2, 32*pi**2*y).subs(k, m + 4 - 4*l))
out['ASD constant-s family on kCPbar2 # l(S1xS3)'] = dict(
    P=str(sp.simplify(P)), R=str(sp.simplify(R)), E=str(E),
    E_in_m_y=str(sp.simplify(E_my)), note='m=k+4l-4, y=Y^2/(32 pi^2); expect 1+9m/(3m+4y)',
    check=bool(sp.simplify(E_my - (1 + 9*m/(3*m + 4*y))) == 0),
    S4=str(sp.simplify(E_my.subs({m: -4, y: 12}))), CPbar2_FS=str(sp.simplify(E_my.subs({m: -3, y: 9}))),
    four_CPbar2_any_y=str(sp.simplify(E_my.subs(m, 0))), S1xS3_any_y=str(sp.simplify(E_my.subs(m, 0))))

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step71_functional_split_examples.json')
with open(path, 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
