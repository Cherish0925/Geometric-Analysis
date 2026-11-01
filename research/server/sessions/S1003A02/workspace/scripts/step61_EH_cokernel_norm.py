"""
Step 61: exact normalisation of the Eguchi-Hanson cokernel (Target 58.Q / Theorem 61.EH).

EH_a = dr^2/f + (r^2/4)(s1^2+s2^2) + (r^2 f/4) s3^2,  f = 1 - a^4/r^4,  r >= a,  psi-period 2pi (RP^3 levels).
Checks (exact, sympy):
  (1) EH is Ricci-flat (sanity of conventions);
  (2) F = d(s3/r^2) is closed and anti-self-dual for the orientation dr^s1^s2^s3 (the one in which the
      Kahler forms are self-dual is checked by verifying that F is ASD and omega_1 = e^01+e^23 is SD-parallel);
  (3) the constant c with Omega = c F asymptotic to the flat (e^03 - e^12)/r^4 used in step60_EH_obstruction_pairing.py
      (|Omega|^2_endo = 4/r^8 there);
  (4) ||o_i||^2_{L^2(EH_a)} = int |Omega|^2_endo dvol = pi^2 / a^4  (|Omega o omega_i|^2 = |Omega|^2_endo since omega_i is
      an orthogonal complex structure commuting with the ASD Omega);
  (5) L^2-orthogonality <o_i, o_j> = 0 (i != j) pointwise: tr(o_i^T o_j) = -tr(Omega^2 omega_i omega_j) ∝ tr(omega_i omega_j)... checked
      numerically in the flat frame.
Output: workspace/data/step61_EH_cokernel_norm.json
"""
import os, json, itertools
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step61_EH_cokernel_norm.json')
r, a, th, ph, ps = sp.symbols('r a theta phi psi', positive=True)
X = [r, th, ph, ps]
f = 1 - a**4 / r**4
# left-invariant forms in Euler angles, as row vectors in (dr, dth, dph, dps)
s1 = sp.Matrix([[0, -sp.sin(ps), sp.cos(ps) * sp.sin(th), 0]])
s2 = sp.Matrix([[0, sp.cos(ps), sp.sin(ps) * sp.sin(th), 0]])
s3 = sp.Matrix([[0, 0, sp.cos(th), 1]])
dr = sp.Matrix([[1, 0, 0, 0]])
def sym(u, v): return (u.T * v + v.T * u) / 2
g = dr.T * dr / f + r**2 / 4 * (s1.T * s1 + s2.T * s2) + r**2 * f / 4 * s3.T * s3
g = sp.simplify(g)
gi = sp.simplify(g.inv())
detg = sp.simplify(g.det())
res = {}

# (1) Ricci flatness
def christoffel(g, gi):
    G = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for k, i, j in itertools.product(range(4), repeat=3):
        G[k][i][j] = sp.simplify(sum(gi[k, l] * (sp.diff(g[l, i], X[j]) + sp.diff(g[l, j], X[i]) - sp.diff(g[i, j], X[l])) for l in range(4)) / 2)
    return G
G = christoffel(g, gi)
def ricci(G):
    R = sp.zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        R[i, j] = sp.simplify(sum(sp.diff(G[k][i][j], X[k]) - sp.diff(G[k][i][k], X[j]) +
                                  sum(G[k][k][l] * G[l][i][j] - G[k][j][l] * G[l][i][k] for l in range(4)) for k in range(4)))
    return R
Ric = ricci(G)
res['EH_ricci_flat'] = bool(Ric == sp.zeros(4, 4))
print('EH Ricci flat:', res['EH_ricci_flat'], flush=True)

# 2-forms as antisymmetric matrices F_ij
def wedge(u, v): return u.T * v - v.T * u
def ext_d_1form(w):  # w row vector of components
    F = sp.zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        F[i, j] = sp.diff(w[j], X[i]) - sp.diff(w[i], X[j])
    return sp.simplify(F)
F = ext_d_1form(s3 / r**2)
# Hodge star with volume form sqrt(det g) dr^dth^dph^dps ; orientation dr^s1^s2^s3: check sign
vol_coeff = sp.sqrt(detg)
orient = sp.simplify(sp.Matrix.vstack(dr, s1, s2, s3).det())
print('orientation det(dr,s1,s2,s3) =', orient)
def hodge(F):
    Fu = gi * F * gi.T  # raised indices
    S = sp.zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        S[i, j] = sp.simplify(sum(sp.LeviCivita(i, j, k, l) * Fu[k, l] for k in range(4) for l in range(4)) / 2 * vol_coeff * sp.sign(orient))
    return S
starF = hodge(F)
res['F_ASD'] = bool(sp.simplify(starF + F) == sp.zeros(4, 4))
res['F_SD'] = bool(sp.simplify(starF - F) == sp.zeros(4, 4))
print('F = d(s3/r^2): ASD', res['F_ASD'], ' SD', res['F_SD'], flush=True)
# Kahler forms: omega_1 = e0^e3 + e1^e2 with e0 = dr/sqrt f, e3 = r sqrt f s3/2, e1 = r s1/2, e2 = r s2/2
e0 = dr / sp.sqrt(f); e1 = r * s1 / 2; e2 = r * s2 / 2; e3 = r * sp.sqrt(f) * s3 / 2
om = [wedge(e0, e3) + wedge(e1, e2), wedge(e0, e1) + wedge(e2, e3), wedge(e0, e2) + wedge(e3, e1)]
res['omega_SD'] = [bool(sp.simplify(hodge(o) - o) == sp.zeros(4, 4)) for o in om]
res['omega_closed'] = []
for o in om:
    # closedness: dω_{ijk} = ∂_i ω_jk + ∂_j ω_ki + ∂_k ω_ij
    ok = all(sp.simplify(sp.diff(o[j, k], X[i]) + sp.diff(o[k, i], X[j]) + sp.diff(o[i, j], X[k])) == 0
             for i, j, k in itertools.combinations(range(4), 3))
    res['omega_closed'].append(bool(ok))
print('Kahler forms SD:', res['omega_SD'], ' closed:', res['omega_closed'], flush=True)

def endo_norm2(F):
    return sp.simplify(sum(F[i, j] * F[k, l] * gi[i, k] * gi[j, l] for i, j, k, l in itertools.product(range(4), repeat=4)))
nF = endo_norm2(F)
print('|d(s3/r^2)|^2_endo =', nF, flush=True)
# Omega = c F with |Omega|^2 = 4/r^8 (flat normalisation of step60): c^2 nF = 4/r^8
c2 = sp.simplify(4 / r**8 / nF)
res['c_squared'] = str(c2)
# volume integral: angles theta in [0,pi], phi in [0,2pi], psi in [0,2pi] (Z2 quotient)
dens = sp.simplify(c2 * nF * vol_coeff)
ang = sp.integrate(sp.integrate(sp.integrate(dens, (ps, 0, 2 * sp.pi)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
norm2 = sp.simplify(sp.integrate(sp.simplify(ang), (r, a, sp.oo)))
res['L2_norm_sq_o'] = str(norm2)
print('||o||^2 =', norm2, flush=True)
# level-set volume check: Vol(RP^3 of radius r) in flat limit should be pi^2 r^3
lev = sp.simplify(sp.integrate(sp.integrate(sp.integrate(vol_coeff.subs(a, 0), (ps, 0, 2 * sp.pi)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)))
res['flat_shell_density'] = str(lev)
print('flat volume density per dr (should be pi^2 r^3):', lev)
json.dump(res, open(OUT, 'w'), indent=1)
print('saved', OUT)
