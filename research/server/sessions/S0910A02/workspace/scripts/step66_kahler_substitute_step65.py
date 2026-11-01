#!/usr/bin/env python3
"""Step 66: Substitute Kaehler-potential variations into Step-65 linearized Ricci formulas.

This is the decisive inexpensive check of the Strategist's scalar-reduction idea.
It uses Step-65's full-4D symbolic dRic formulas (trusted because the full angular
Christoffels were included) and substitutes the Kaehler variation

    h_phi = A_phi (e0^2 + e3^2) + B_phi (e1^2+e2^2)

so f1=f3=A_phi, f2=B_phi in the Step-65 ansatz.

For radial phi with q=phi'(r), in our dd^c normalization:
    A_phi = (2/r) d/dr [ q r W / 2 ]
    B_phi = 2 q W / r,
where W=1-r^{-4}.  The real Ricci-form identity should imply dRic[h_phi]
is a Kaehler tensor determined by a radial scalar S = c*(A_phi+B_phi) or its
sign/factor variant.  We solve for the exact factor by comparing dRic with
A_S/B_S computed from S.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
INP = ROOT / "data" / "step65_full4d_lichnerowicz.json"
OUT = ROOT / "data" / "step66_kahler_substitute_step65.json"

r = sp.symbols('r', positive=True)
W = 1 - r**(-4)
q = sp.Function('q')(r)  # q = phi'
f1 = sp.Function('f1')
f2 = sp.Function('f2')
f3 = sp.Function('f3')

# Kaehler coefficients in the same orthonormal coframe as f1,f2,f3.
A = sp.simplify((2/r) * sp.diff(q*r*W/2, r))
B = sp.simplify(2*q*W/r)
Delta = sp.simplify(A + B)

def Acoef(fp):
    return sp.simplify((2/r)*sp.diff(fp*r*W/2, r))

def Bcoef(fp):
    return sp.simplify(2*fp*W/r)

# A_S/B_S for S = Delta (where fp = S' if S is a scalar potential).
# But Ricci variation is -ddc(log det)' = -ddc(Delta_complex phi); if Delta_complex is
# proportional to A+B, then use fp = d/dr(A+B).  We compare generically.
AS = sp.simplify(Acoef(sp.diff(Delta, r)))
BS = sp.simplify(Bcoef(sp.diff(Delta, r)))

# load Step65 dRic coordinate components.
import json
D = json.loads(INP.read_text())
loc = {'r': r, 'Derivative': sp.Derivative, 'f1': f1, 'f2': f2, 'f3': f3}
exprs = {k: sp.sympify(v, locals=loc) for k,v in D['dRic_at_point'].items()}
# Substitute f's and derivatives.
subs = {
    f1(r): A, f2(r): B, f3(r): A,
    sp.Derivative(f1(r), r): sp.diff(A, r),
    sp.Derivative(f2(r), r): sp.diff(B, r),
    sp.Derivative(f3(r), r): sp.diff(A, r),
    sp.Derivative(f1(r), (r,2)): sp.diff(A, (r,2)),
    sp.Derivative(f2(r), (r,2)): sp.diff(B, (r,2)),
    sp.Derivative(f3(r), (r,2)): sp.diff(A, (r,2)),
}
dR = {k: sp.simplify(e.subs(subs)) for k,e in exprs.items()}

# Convert predicted frame components to coordinate components at the evaluation point:
# coord rr = C/W, theta theta = (r^2/4) D, psi psi = (r^2 W/4) C.
# Compare dR00 with +/- AS/W, dR11 with +/- (r^2/4)BS, dR33 with +/- (r^2 W/4)AS.
comparisons = {}
for factor in [sp.Rational(1,1), sp.Rational(-1,1), sp.Rational(1,2), sp.Rational(-1,2), sp.Rational(2,1), sp.Rational(-2,1)]:
    diff00 = sp.simplify(dR['00'] - factor*AS/W)
    diff11 = sp.simplify(dR['11'] - factor*(r**2/4)*BS)
    diff33 = sp.simplify(dR['33'] - factor*(r**2*W/4)*AS)
    ok = bool(diff00==0 and diff11==0 and diff33==0)
    comparisons[str(factor)] = {"diff00": str(diff00), "diff11": str(diff11), "diff33": str(diff33), "holds": ok}
    print(f"factor {factor}: holds={ok}")
    if ok:
        print("  exact master identity factor:", factor)

# Also test specific potentials q=2r (phi=r^2) and q=2r^5/(r^4-1) (EH potential, A=B=4).
# This supplies numerical/closed-form sanity checks and catches factor errors.
test_qs = {
    "phi_r2": 2*r,
    "EH_potential_q": 2*r**5/(r**4-1),
}
tests = {}
for name, qval in test_qs.items():
    vals = {sp.Derivative(q, (r,3)): sp.diff(qval,(r,3)), sp.Derivative(q,(r,2)): sp.diff(qval,(r,2)),
            sp.Derivative(q,r): sp.diff(qval,r), q: qval}
    dr_vals = {k: sp.simplify(v.subs(vals)) for k,v in dR.items()}
    # frame components from coordinate components:
    frame00 = sp.simplify(dr_vals['00']*W)
    frame11 = sp.simplify(dr_vals['11']*4/r**2)
    frame33 = sp.simplify(dr_vals['33']*4/(r**2*W))
    tests[name] = {"frame00": str(frame00), "frame11": str(frame11), "frame33": str(frame33)}
    print(f"\n{name}: frame dRic =")
    print("  00:", frame00)
    print("  11:", frame11)
    print("  33:", frame33)

# If master identity factor known, then scalar equation for dRic=Lambda*g is factor*A_{Delta}' = Lambda.
# Store the exact formulas for A,B,Delta and dR frame components.
frame = {
    "00": sp.simplify(dR['00']*W),
    "11": sp.simplify(dR['11']*4/r**2),
    "33": sp.simplify(dR['33']*4/(r**2*W)),
}

OUT.write_text(json.dumps({
    "status":"ok",
    "A_phi": str(A),
    "B_phi": str(B),
    "Delta_A_plus_B": str(Delta),
    "AS_from_Delta": str(AS),
    "BS_from_Delta": str(BS),
    "frame_dRic_kaehler_variation": {k: str(v) for k,v in frame.items()},
    "comparisons_factor_times_ddc_Delta": comparisons,
    "test_potentials": tests,
}, indent=2))
print("\nOutput:", OUT)
