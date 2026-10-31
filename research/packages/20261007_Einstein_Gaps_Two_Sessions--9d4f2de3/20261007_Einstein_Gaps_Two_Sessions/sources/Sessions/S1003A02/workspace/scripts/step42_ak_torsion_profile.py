"""Step 42: exact algebra of the almost-Kahler torsion-profile gap inequality.

Input : none.  Output: workspace/data/step42_ak_torsion_profile.json
Conventions (LeBrun, Four-manifolds curvature bounds and convex geometry, eq. for s*):
  almost-Kahler (g, omega), |omega|^2 = 2, u = omega/sqrt2 unit;
  s* = s + |grad omega|^2 = 2 W+(omega,omega) + s/3      (so W+(u,u) = s/6 + delta/4, delta = s*-s >= 0)
  Blair: int (s + s*) dmu = 8 pi c1(omega).[omega] = -8 pi K_omega.[omega]   (exact)
  [omega]^2 = 2V.
  C+ := (1/2pi^2) int |W+|^2 + (1/96 pi^2) int s^2 = (A - k) + P/(8 pi^2)  on X # k CPbar^2.
Checks:
  (1) pointwise lower bound G(sigma,delta) for the C+ density, using |W+|^2 >= (3/2) W+(u,u)^2;
  (2) Jensen with sigma_bar fixed by Blair gives C+ >= (l^2/(128 pi^2 V)) Gamma(theta),
      Gamma = 3 theta^2 - 2 theta + 1,  theta = int delta / l,  l = 8 pi K_omega.[omega];
  (3) min Gamma = 2/3 at theta = 1/3 (LeBrun), Gamma(0) = 1 (Kahler tariff);
  (4) the Step-40 formal common mode (r = 2-h) saturates (2) with theta = h/(2-h) and
      beta(r) = 2 theta - 3 theta^2 exactly;
  (5) LeBrun's Cauchy-Schwarz constant 48 and its extremal delta = sigma/2 (s* = s/2);
  (6) tariff reduction: if P >= 8 pi^2 kappa A theta then P/(8 pi^2) >= k kappa/(kappa+2).
"""
import json
from pathlib import Path
import sympy as sp

out = {}
sig, dl, th, h, r, kap, A, k, V, l = sp.symbols('sigma delta theta h r kappa A k V ell', real=True)
pi = sp.pi

# (1) density
Wuu = -sig/6 + dl/4                       # s = -sigma
G = (sp.Rational(3, 2)*Wuu**2)/(2*pi**2) + sig**2/(96*pi**2)
out['G_density'] = str(sp.simplify(G))
H = sp.hessian(G, (sig, dl))
out['G_convex_hessian_eigs'] = [str(sp.simplify(e)) for e in H.eigenvals()]

# (2) Blair fixes sigma_bar: int(2 sigma - delta) = l  -> sigma_bar = (l + Delta)/(2V), delta_bar = theta l / V
sb = (1 + th)*l/(2*V); db = th*l/V
CVG = sp.simplify(V*G.subs({sig: sb, dl: db}))
Gamma = sp.simplify(CVG/(l**2/(128*pi**2*V)))
out['Gamma'] = str(sp.factor(Gamma))
assert sp.simplify(Gamma - (3*th**2 - 2*th + 1)) == 0

# (3)
thmin = sp.solve(sp.diff(Gamma, th), th)[0]
out['theta_min'] = str(thmin); out['Gamma_min'] = str(sp.simplify(Gamma.subs(th, thmin)))
out['Gamma_0'] = str(Gamma.subs(th, 0))

# with l = 8 pi sqrt(2 A V): prefactor equals A
pref = sp.simplify(((8*pi*sp.sqrt(2*A*V))**2/(128*pi**2*V)))
out['prefactor_at_area_zero'] = str(pref)

# (4) common mode: s=-4, W+(u,u) = 4/3 - r, r^2 V = 8 pi^2 A, r = 2-h
Vcm = 8*pi**2*A/(2 - h)**2
dcm = sp.solve(sp.Eq(-sp.Rational(4, 6) + dl/4, sp.Rational(4, 3) - (2 - h)), dl)[0]   # delta = 4h
lcm = 8*pi*(4*pi*A/(2 - h))           # = 8 pi sqrt(2 A Vcm) for 0 <= h < 2, A > 0
assert sp.simplify((lcm**2 - 64*pi**2*2*A*Vcm)) == 0
thcm = sp.simplify(dcm*Vcm/lcm)
sigbar_check = sp.simplify((lcm + dcm*Vcm)/(2*Vcm))
beta = 16/r - 5 - 12/r**2
out['common_mode'] = dict(delta=str(dcm), theta=str(sp.simplify(thcm)), sigma_bar=str(sp.simplify(sigbar_check)),
                          beta_minus_2th_plus_3th2=str(sp.simplify(beta.subs(r, 2 - h) - (2*thcm - 3*thcm**2))))

# (5) LeBrun constant: max L^2/(4 pi^2 F) with L = 2 sigma - delta
F4 = 3*Wuu**2 + sig**2/24
ratio = sp.simplify(((2*sig - dl)**2/F4).subs(sig, 1))
crit = sp.solve(sp.diff(ratio, dl), dl)
out['CS_constant'] = [dict(delta_over_sigma=str(c), value=str(sp.simplify(ratio.subs(dl, c)))) for c in crit]

# (6) tariff reduction
Pk = sp.symbols('p')                     # p = P/(8 pi^2)
sol = sp.solve(sp.Eq(Pk, k - 2*A*(Pk/(kap*A))), Pk)[0]
out['tariff_from_linear_goldberg'] = str(sp.simplify(sol))

p = Path(__file__).resolve().parents[1]/'data'/'step42_ak_torsion_profile.json'
p.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
