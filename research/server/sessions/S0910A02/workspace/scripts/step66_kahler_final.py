#!/usr/bin/env python3
"""Step 66 (Part A final, lightweight): settle the Kaehler reduction analytically.

Decisions made cheap:
  1. u_K' = 2 r^5/(r^4-a^4) (equivalently u_K = r^2 + a^2 ln(r^2-a^2)) satisfies
     i dd-bar(u_K) = 2 omega_K EXACTLY  [with correct A_f, B_f factors].
     The naive r^2 FAILS by an ASD term.  u_K = 2 * utilde_K (so utilde_K -> 1 at infinity).
  2. Master identity: phi=1 gives h=i dd-bar(1)=0 and dRic[0]=0 -- trivially TRUE.
     phi=r^2 (Kaehler away from bolt) gives h=r^2 g and dRic[r^2 g] != -i dd-bar(Delta_K r^2)
     in general (the identity holds only up to the trace/Hessian obstruction).

  3. KEY computation: dRic[r^2 g] analytically via Bianchi-IX Ricci under G3 -> e^{2 eps r^2} G3.
     Hand result: R33(e^{2 eps r^2} G3) = e^{-2 eps r^2} R33(G3), so dRic_33[r^2 g] = 0
     (since R33^EH = 0).  Verified here numerically against the frame formulas.

Then: the scalar ODE.  Since h(phi) = i dd-bar(phi) has A_phi = B_phi only when phi is
Kaehler-potential-like, and dRic[h] = -i dd-bar(Delta_K phi) holds for the (0,0),(3,3) block
automatically while the (1,1) block requires the B-matching, we SOLVE the scalar problem:
  Delta_K phi = -Lambda u_K + c   (so -i dd-bar(Delta_K phi) = Lambda (i dd-bar u_K) = Lambda omega_K ~ Lambda g)
with (r^3 W phi')' = r^3 (-Lambda u_K + c), regular at bolt, phi' ~ 2 r at infinity.
The residual dRic[h] - Lambda g is then checked numerically.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step66_kahler_final.json"

r, a = sp.symbols('r a', positive=True)
W = 1 - a**4/r**4
res = {}

# ---- 1. Correct A_f, B_f and potential checks ----
def Acoef(fp): return sp.simplify((2/r)*sp.diff(fp*r*W/2, r))
def Bcoef(fp): return sp.simplify(2*fp*W/r)

checks = {}
for name, fp in [("r2", 2*r), ("uK", 2*r**5/(r**4-a**4)), ("utildeK", r*(a**2+2*r**2)/(a**2+r**2))]:
    A_, B_ = Acoef(fp), Bcoef(fp)
    checks[name] = {"A": sp.simplify(A_), "B": sp.simplify(B_),
                    "A_minus_B": sp.simplify(A_-B_),
                    "A_over_B": sp.simplify(A_/B_)}
    print(f"{name}: A = {checks[name]['A']}")
    print(f"      B = {checks[name]['B']}   A-B = {checks[name]['A_minus_B']}")

res["potential_checks"] = checks
# u_K integral form
uK_int = sp.simplify(sp.integrate(2*r**5/(r**4-a**4), r))
res["uK_integral"] = str(uK_int)
print("u_K =", uK_int)

# ---- 2. Bianchi-IX frame Ricci, NUMERIC, and dRic_33[r^2 g] ----
# Use the closed-form frame Ricci (from step66_kahler_symbolic pass-1):
# R00, R11, R33 as functions of G1,G2,G3.  We reuse them but evaluate numerically.
G1,G2,G3 = sp.symbols('G1 G2 G3', positive=True)
g1p,g2p,g3p = sp.symbols('g1p g2p g3p')
g1pp,g2pp,g3pp = sp.symbols('g1pp g2pp g3pp')
# Symbolic formulas with G(r) and derivatives replaced by symbols
R00f = -g3pp/(2*G1*G3) + g3p**2/(4*G1*G3**2) - g2pp/(G1*G2) + g2p**2/(2*G1*G2**2) \
       + g1p*g3p/(4*G1**2*G3) + g1p*g2p/(2*G1**2*G2)
R11f = (1 - G3/(2*G2) - g2pp/(2*G1) - g2p*g3p/(4*G1*G3) + g1p*g2p/(4*G1**2))/G2
R33f = (G3**2/(2*G2**2) - g3pp/(2*G1) + g3p**2/(4*G1*G3) - g2p*g3p/(2*G1*G2) + g1p*g3p/(4*G1**2))/G3
R00n = sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp], R00f, 'numpy')
R11n = sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp], R11f, 'numpy')
R33n = sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp], R33f, 'numpy')

def ricci_frame(rv, G1v, G2v, G3v, G1pv, G2pv, G3pv, G1ppv, G2ppv, G3ppv):
    return (R00n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv),
            R11n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv),
            R33n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv))

av = 1.0
def EH(rv):
    Wv = 1 - av**4/rv**4
    G1 = 1/Wv; G2 = rv**2/4; G3 = rv**2*Wv/4
    Wp = 4*av**4/rv**5; Wpp = -20*av**4/rv**6
    G1p = -Wp/Wv**2; G1pp = -Wpp/Wv**2 + 2*Wp**2/Wv**3
    G2p = rv/2; G2pp = 0.5
    G3p = rv*Wv/2 + rv**2*Wp/4; G3pp = Wv/2 + rv*Wp + rv**2*Wpp/4
    return ricci_frame(rv, G1,G2,G3,G1p,G2p,G3p,G1pp,G2pp,G3pp)

# EH flatness numeric
mx = 0.0
for rv in np.linspace(1.01, 20, 400):
    mx = max(mx, max(abs(x) for x in EH(rv)))
print(f"\nEH flatness: max |Ric| = {mx:.3e}")
res["EH_flat_numeric"] = mx

# dRic_33[r^2 g]: perturb G3 -> e^{2 eps r^2} G3 (exact: scales 03 block)
def pert33(rv, eps):
    Wv = 1 - av**4/rv**4
    G1 = 1/Wv; G2 = rv**2/4
    G3 = np.exp(2*eps*rv**2)*rv**2*Wv/4
    Wp = 4*av**4/rv**5; Wpp = -20*av**4/rv**6
    G1p = -Wp/Wv**2; G1pp = -Wpp/Wv**2 + 2*Wp**2/Wv**3
    G2p = rv/2; G2pp = 0.5
    base3 = rv**2*Wv/4
    base3p = rv*Wv/2 + rv**2*Wp/4
    base3pp = Wv/2 + rv*Wp + rv**2*Wpp/4
    E = np.exp(2*eps*rv**2); Ep = 4*eps*rv*E; Epp = (4*eps + 16*eps**2*rv**2)*E
    G3p = E*base3p + Ep*base3; G3pp = E*base3pp + 2*Ep*base3p + Epp*base3
    return ricci_frame(rv, G1,G2,G3,G1p,G2p,G3p,G1pp,G2pp,G3pp)

eps0 = 1e-4
d33_num = []
for rv in [1.05, 1.5, 2.0, 3.0, 5.0, 10.0]:
    Rp = pert33(rv, eps0); Rm = pert33(rv, -eps0); R0 = EH(rv)
    dR33 = (Rp[2]-Rm[2])/(2*eps0)
    d33_num.append((rv, dR33, R0[2]))
    print(f"  r={rv}: dRic_33[r^2 g] ~ {dR33:.3e}  (R33_EH={R0[2]:.1e})")
res["dRic33_r2g_numeric"] = {"max_abs": max(abs(x[1]) for x in d33_num)}
print(f"max |dRic_33[r^2 g]| = {res['dRic33_r2g_numeric']['max_abs']:.3e}  (predicted 0)")

# ---- 3. Scalar ODE solve ----
# (r^3 W phi')' = r^3 (-Lambda u_K + c), u_K = r^2 + a^2 ln(r^2-a^2), regular at bolt, phi'->2r.
Lam = 1.0
from scipy.integrate import solve_bvp
def source(rv, c):
    uK = rv**2 + av**2*np.log(rv**2-av**2)
    return rv**3*(-Lam*uK + c)

# Integrate: r^3 W phi' = integral_{a}^{r} source ds  (regular at bolt kills homogeneous 1/(r^3 W))
# phi' = [int source] / (r^3 W).  Choose c to enforce phi'/r -> 2 at large r.
rr = np.linspace(av+1e-6, 60.0, 40000)
from scipy.integrate import cumulative_trapezoid
def phiprime(c):
    src = source(rr, c)
    I = cumulative_trapezoid(src, rr, initial=0.0)
    return I/(rr**3*(1-av**4/rr**4))
# target phi'/r -> 2 at r=60
c_target = None
from scipy.optimize import brentq
def tail(c):
    pp = phiprime(c)
    return pp[-1]/rr[-1] - 2.0
c_target = brentq(tail, -500.0, 500.0, xtol=1e-12)
pp = phiprime(c_target)
print(f"\nScalar ODE: c* = {c_target:.6f},  phi'/r at r=60 = {pp[-1]/rr[-1]:.6f} (target 2)")
# bolt regularity: phi'(a) finite?
print(f"phi' near bolt r={rr[5]:.4f}: {pp[5]:.6f} (finite={np.isfinite(pp[5])})")
res["scalar_ode"] = {"c_star": float(c_target), "phip_over_r_tail": float(pp[-1]/rr[-1]),
                     "phip_near_bolt": float(pp[5]), "Lam": Lam}

# ---- 4. Residual check: build h(phi), compute dRic numerically, compare Lambda*g ----
# h(phi): G1 -> (1+eps*A_phi)/W, G2 -> (1+eps*B_phi) r^2/4, G3 -> (1+eps*A_phi) r^2 W/4
# with A_phi = (2/r)(phi' r W/2)' , B_phi = 2 phi' W/r.
# dRic[h] should equal Lambda*g i.e. dRic_00 = dRic_11 = dRic_33 = Lambda (frame comps).
Aphi = (2/rr)*(np.gradient(pp*rr*(1-av**4/rr**4)/2, rr))
Bphi = 2*pp*(1-av**4/rr**4)/rr
Aphi_f = sp.lambdify(r, (2/r)*sp.diff(sp.Function('q')(r)*r*W/2, r), 'numpy')  # placeholder
# compute A_phi by interpolating pp
from scipy.interpolate import interp1d
pp_i = interp1d(rr, pp, kind='cubic', fill_value='extrapolate')
def Aphi_v(x):
    Wv = 1-av**4/x**4
    return (2/x)*np.gradient(pp_i(x)*x*Wv/2, x) if hasattr(x,'__len__') else None

# Simpler: evaluate dRic by finite-difference perturbation using analytic A_phi, B_phi.
# A_phi(r) = (2/r) d/dr[phi' r W/2].  Compute numerically on a dense grid.
def A_B(x):
    Wv = 1-av**4/x**4
    # phi' r W/2 and its derivative
    h = 1e-5
    f1 = pp_i(x+h)*(x+h)*(1-av**4/(x+h)**4)/2
    f0 = pp_i(x-h)*(x-h)*(1-av**4/(x-h)**4)/2
    d = (f1-f0)/(2*h)
    return (2/x)*d, 2*pp_i(x)*Wv/x

eps2 = 1e-5
residuals = []
for rv in [1.2, 1.5, 2.0, 3.0, 5.0, 8.0, 15.0]:
    Aph, Bph = A_B(rv)
    def met(e_):
        Wv = 1-av**4/rv**4
        G1 = (1+e_*Aph)/Wv; G2 = (1+e_*Bph)*rv**2/4; G3 = (1+e_*Aph)*rv**2*Wv/4
        # derivatives: need d/dr of perturbed G's; use the analytic forms via chain rule.
        # Approximate by finite difference in r as well.
        return G1,G2,G3
    # Build local perturbation: differentiate perturbed metric wrt r numerically
    def full(rv_, e_):
        Wv = 1-av**4/rv_**4; Wp = 4*av**4/rv_**5; Wpp = -20*av**4/rv_**6
        A_, B_ = A_B(rv_)
        # dA/dr, dB/dr by finite diff
        h = 1e-5
        A2,B2 = A_B(rv_+h); A1,B1 = A_B(rv_-h)
        Ap = (A2-A1)/(2*h); Bp = (B2-B1)/(2*h)
        App = (A2-2*A_+A1)/h**2; Bpp = (B2-2*B_+B1)/h**2
        G1 = (1+e_*A_)/Wv; G2 = (1+e_*B_)*rv_**2/4; G3 = (1+e_*A_)*rv_**2*Wv/4
        G1p = e_*Ap/Wv - (1+e_*A_)*Wp/Wv**2
        G2p = e_*Bp*rv_**2/4 + (1+e_*B_)*rv_/2
        G3p = e_*Ap*rv_**2*Wv/4 + (1+e_*A_)*(rv_*Wv/2 + rv_**2*Wp/4)
        G1pp = e_*App/Wv - 2*e_*Ap*Wp/Wv**2 - (1+e_*A_)*(Wpp/Wv**2 - 2*Wp**2/Wv**3)
        G2pp = e_*Bpp*rv_**2/4 + e_*Bp*rv_ + (1+e_*B_)/2
        G3pp = e_*App*rv_**2*Wv/4 + 2*e_*Ap*(rv_*Wv/2+rv_**2*Wp/4) + (1+e_*A_)*(Wv/2+rv_*Wp+rv_**2*Wpp/4)
        return ricci_frame(rv_, G1,G2,G3,G1p,G2p,G3p,G1pp,G2pp,G3pp)
    Rp = full(rv, eps2); Rm = full(rv, -eps2)
    dR = tuple((Rp[i]-Rm[i])/(2*eps2) for i in range(3))
    residuals.append((rv, dR[0], dR[1], dR[2]))
    print(f"  r={rv}: dRic[h] = ({dR[0]:.4f},{dR[1]:.4f},{dR[2]:.4f})  target Lambda={Lam}")
res["residual"] = {"Lam": Lam,
                   "max_dev_from_Lambda": float(max(abs(d- Lam) for _,*d in residuals for d in d))}
print(f"\nmax |dRic[h] - Lambda| = {res['residual']['max_dev_from_Lambda']:.4e}")

res["status"] = "ok"
OUT.write_text(json.dumps(res, indent=2, default=str))
print("Output:", OUT)
