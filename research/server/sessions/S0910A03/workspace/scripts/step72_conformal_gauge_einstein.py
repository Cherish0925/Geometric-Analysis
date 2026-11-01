"""
Step 72: T^2-invariant Einstein system in CONFORMAL (t,theta) gauge.

Metric ansatz (Weyl/Papapetrou form, Riemannian signature):
  g = e^{2phi(t,z)} (dt^2 + dz^2) + e^{2b(t,z)} dx^2 + e^{2c(t,z)} dy^2

where z = theta is periodic, x,y are the flat T^2 quotient directions.

Any T^2-invariant metric with orthogonal 2-plane distribution can locally be
brought to this form (2D conformal gauge uses both (t,z) diffeomorphisms).

Goals:
 1. Compute Ric + 3g exactly.
 2. Determine the principal symbol / ellipticity of the natural 3-equation set.
 3. Identify the constraint structure via contracted Bianchi.
 4. Extract the reflection-center conditions and the Koiso scalar condition.
 5. Check the orbit-area function rho = e^{b+c} for a harmonic-type equation.
"""

import sympy as sp
import json, pathlib

t, z = sp.symbols('t z', real=True)
x, y = sp.symbols('x y', real=True)
phi = sp.Function('phi')(t, z)
b = sp.Function('b')(t, z)
c = sp.Function('c')(t, z)

coords = [t, z, x, y]
g = sp.diag(sp.exp(2*phi), sp.exp(2*phi), sp.exp(2*b), sp.exp(2*c))
ginv = sp.diag(sp.exp(-2*phi), sp.exp(-2*phi), sp.exp(-2*b), sp.exp(-2*c))

n = 4

def christoffel(g, ginv, coords):
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a_ in range(n):
        for m in range(n):
            for k in range(n):
                s = 0
                for l in range(n):
                    s += ginv[a_, l]*(sp.diff(g[l, m], coords[k])
                                      + sp.diff(g[l, k], coords[m])
                                      - sp.diff(g[m, k], coords[l]))
                G[a_][m][k] = sp.simplify(s/2)
    return G

Gam = christoffel(g, ginv, coords)

def ricci(Gam, coords):
    R = sp.zeros(n, n)
    for m in range(n):
        for k in range(n):
            expr = 0
            for a_ in range(n):
                expr += sp.diff(Gam[a_][m][k], coords[a_])
                expr -= sp.diff(Gam[a_][m][a_], coords[k])
                for l in range(n):
                    expr += Gam[a_][a_][l]*Gam[l][m][k]
                    expr -= Gam[a_][k][l]*Gam[l][m][a_]
            R[m, k] = sp.simplify(expr)
    return R

print("computing Ricci ...")
Ric = ricci(Gam, coords)

Lam = -3
E = sp.zeros(n, n)
for i in range(n):
    for j in range(n):
        E[i, j] = sp.simplify(Ric[i, j] - Lam*g[i, j])

names = ['tt', 'tz', 'zz', 'xx', 'yy']
idx = [(0, 0), (0, 1), (1, 1), (2, 2), (3, 3)]

out = {}
print("\n=== Einstein defect E = Ric + 3g ===")
for nm, (i, j) in zip(names, idx):
    # normalize tangential ones by the metric coefficient
    if nm in ('xx',):
        expr = sp.simplify(E[i, j]*sp.exp(-2*b))
    elif nm in ('yy',):
        expr = sp.simplify(E[i, j]*sp.exp(-2*c))
    elif nm in ('tt', 'zz'):
        expr = sp.simplify(E[i, j]*sp.exp(-2*phi))
    else:
        expr = sp.simplify(E[i, j])
    expr = sp.expand(expr)
    out[nm] = str(expr)
    print(f"\nE_{nm} (normalized) =")
    sp.pprint(expr)

# ---------------------------------------------------------------
# 1. Orbit-area function rho = e^{b+c}: check for a harmonic equation
# ---------------------------------------------------------------
print("\n" + "="*60)
print("ORBIT-AREA FUNCTION rho = e^{b+c}")
print("="*60)
# The combination E_xx/g_xx + E_yy/g_yy should relate to Laplacian of rho.
Exx = sp.expand(sp.simplify(E[2, 2]*sp.exp(-2*b)))
Eyy = sp.expand(sp.simplify(E[3, 3]*sp.exp(-2*c)))
comb = sp.simplify(Exx + Eyy)
print("\nE_xx/g_xx + E_yy/g_yy =")
sp.pprint(sp.expand(comb))

rho = sp.exp(b + c)
# flat 2D Laplacian
lap_flat_rho = sp.diff(rho, t, 2) + sp.diff(rho, z, 2)
print("\n(d_tt + d_zz) rho / rho =")
sp.pprint(sp.simplify(sp.expand(lap_flat_rho/rho)))
out['orbit_area_check'] = {
    'Exx_plus_Eyy': str(sp.expand(comb)),
    'lap_flat_rho_over_rho': str(sp.simplify(sp.expand(lap_flat_rho/rho))),
}

# The Einstein condition combination:  is (d_tt+d_zz) rho = -6 e^{2phi} rho ?
test = sp.simplify(sp.expand(lap_flat_rho + 6*sp.exp(2*phi)*rho))
print("\nlap_flat(rho) + 6 e^{2phi} rho  (should equal rho*(Exx+Eyy) up to factor) =")
sp.pprint(test)
ratio = sp.simplify(sp.expand(test/rho) - comb)
print("\n[lap_flat(rho)/rho + 6 e^{2phi}] - (Exx+Eyy) =")
sp.pprint(sp.simplify(ratio))
out['rho_identity_residual'] = str(sp.simplify(ratio))

# ---------------------------------------------------------------
# 2. Principal symbol of the natural 3-equation system
# ---------------------------------------------------------------
print("\n" + "="*60)
print("PRINCIPAL SYMBOL")
print("="*60)
tau, xi = sp.symbols('tau xi', real=True)
P, B_, C_ = sp.symbols('P B C')  # amplitudes of phi, b, c
subsmap = {}
# second-derivative substitution: d_tt f -> -tau^2 F, d_zz f -> -xi^2 F, d_tz f -> -tau*xi*F
def princ(expr, amp_map):
    e = sp.expand(expr)
    rep = {}
    for f, A in amp_map.items():
        rep[sp.Derivative(f, (t, 2))] = -tau**2*A
        rep[sp.Derivative(f, (z, 2))] = -xi**2*A
        rep[sp.Derivative(f, t, z)] = -tau*xi*A
        rep[sp.Derivative(f, z, t)] = -tau*xi*A
    e = e.subs(rep)
    # drop all remaining first-derivative / algebraic terms
    e = e.subs({sp.Derivative(f, t): 0 for f in amp_map})
    e = e.subs({sp.Derivative(f, z): 0 for f in amp_map})
    for f in amp_map:
        e = e.subs(f, 0)
    return sp.expand(e)

amp = {phi: P, b: B_, c: C_}
# use E_zz, E_xx, E_yy as candidate evolution triple; also try E_tt+E_zz
cands = {
    'E_tt': sp.expand(sp.simplify(E[0, 0]*sp.exp(-2*phi))),
    'E_zz': sp.expand(sp.simplify(E[1, 1]*sp.exp(-2*phi))),
    'E_xx': Exx,
    'E_yy': Eyy,
    'E_tz': sp.expand(sp.simplify(E[0, 1])),
    'E_tt_plus_E_zz': sp.expand(sp.simplify((E[0, 0] + E[1, 1])*sp.exp(-2*phi))),
}
symb = {}
for k, v in cands.items():
    s = princ(v, amp)
    symb[k] = s
    print(f"\nsymbol[{k}] = {s}")

out['principal_symbols'] = {k: str(v) for k, v in symb.items()}

# Build the 3x3 matrix for (E_tt+E_zz, E_xx, E_yy) in unknowns (P,B,C)
rows = ['E_tt_plus_E_zz', 'E_xx', 'E_yy']
M = sp.zeros(3, 3)
for i, rn in enumerate(rows):
    for j, A in enumerate([P, B_, C_]):
        M[i, j] = sp.expand(symb[rn]).coeff(A)
print("\nsymbol matrix for (E_tt+E_zz, E_xx, E_yy) in (phi,b,c):")
sp.pprint(M)
detM = sp.factor(sp.simplify(M.det()))
print("\ndet =", detM)
out['symbol_matrix_ttzz_xx_yy'] = str(M)
out['det_ttzz_xx_yy'] = str(detM)

# also try (E_zz, E_xx, E_yy)
rows2 = ['E_zz', 'E_xx', 'E_yy']
M2 = sp.zeros(3, 3)
for i, rn in enumerate(rows2):
    for j, A in enumerate([P, B_, C_]):
        M2[i, j] = sp.expand(symb[rn]).coeff(A)
print("\nsymbol matrix for (E_zz, E_xx, E_yy):")
sp.pprint(M2)
det2 = sp.factor(sp.simplify(M2.det()))
print("det =", det2)
out['symbol_matrix_zz_xx_yy'] = str(M2)
out['det_zz_xx_yy'] = str(det2)

path = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'step72_conformal_gauge_system.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(f"\nwrote {path}")
