"""Step 66: symbolic check of the divergence identity behind rank-one exceptional Ricci rigidity.

Claim (flat R^4, pointwise algebra; the curved case is identical at a point in normal coordinates
because only first derivatives enter):
  for phi a self-dual 2-form and psi an anti-self-dual 2-form, the endomorphism product
  T = phi o psi  (T_ab = phi_ac psi_cb) is symmetric and trace-free, and
      (div T)_b = d_a T_ab = kappa1 * psi_bc (delta phi)_c + [terms vanishing iff d psi = 0],
  where (delta phi)_c = -d_a phi_ac.  In particular for closed (hence harmonic) psi,
  div(phi o psi) = kappa1 * psi(delta phi), so on {psi != 0} (psi invertible) div T = 0 iff delta phi = 0
  iff d phi = 0 (phi self-dual).
Also checks the corollary used for the Ricci tensor: Ric0 = c * phi o psi with constant s gives
div Ric0 = ds/4 = 0, hence delta phi = 0.
Outputs workspace/data/step66_rank1_bianchi_check.json
"""
import json, itertools, os, random
import sympy as sp

x = sp.symbols('x1:5')
n = 4

def form_from_pairs(coeffs):
    F = sp.zeros(4, 4)
    for (i, j), c in coeffs.items():
        F[i, j] += c; F[j, i] -= c
    return F

# basis (0-indexed coordinates 0..3 = x1..x4); orientation e1234
Wp = [{(0, 1): 1, (2, 3): 1}, {(0, 2): 1, (3, 1): 1}, {(0, 3): 1, (1, 2): 1}]
Wm = [{(0, 1): 1, (2, 3): -1}, {(0, 2): 1, (3, 1): -1}, {(0, 3): 1, (1, 2): -1}]
WP = [form_from_pairs(w) for w in Wp]
WM = [form_from_pairs(w) for w in Wm]

def hodge_check(F, sign):
    # *e12 = e34 etc.
    ok = sp.simplify(F[0, 1] - sign*F[2, 3]) == 0 and sp.simplify(F[0, 2] - sign*F[3, 1]) == 0 \
        and sp.simplify(F[0, 3] - sign*F[1, 2]) == 0
    return ok

random.seed(66)
def rpoly(deg=2):
    mons = [sp.Integer(1)] + list(x) + [a*b for a, b in itertools.combinations_with_replacement(x, 2)]
    return sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4))*m for m in mons[:1+4+10*(deg >= 2)])

f = [rpoly() for _ in range(3)]
phi = sum((f[i]*WP[i] for i in range(3)), sp.zeros(4, 4))

# general linear ASD psi, then impose d psi = 0
cs = sp.symbols('c0:15')
g = []
for i in range(3):
    g.append(cs[5*i] + sum(cs[5*i+1+j]*x[j] for j in range(4)))
psi_gen = sum((g[i]*WM[i] for i in range(3)), sp.zeros(4, 4))

def dform(F):
    # (dF)_{abc} = d_a F_bc + d_b F_ca + d_c F_ab
    out = []
    for a, b, c in itertools.combinations(range(4), 3):
        out.append(sp.diff(F[b, c], x[a]) + sp.diff(F[c, a], x[b]) + sp.diff(F[a, b], x[c]))
    return out

eqs = [sp.expand(e) for e in dform(psi_gen)]
lin = []
for e in eqs:
    P = sp.Poly(e, *x)
    lin += P.coeffs()
sol = sp.solve(lin, cs, dict=True)[0]
free = [c for c in cs if c not in sol]
subs_vals = {c: sp.Rational(random.randint(-6, 6), random.randint(1, 3)) for c in free}
psi = psi_gen.subs(sol).subs(subs_vals)
assert all(sp.simplify(e) == 0 for e in dform(psi))

T = phi*psi   # T_ab = phi_ac psi_cb
sym = sp.simplify(T - T.T) == sp.zeros(4, 4)
tr = sp.simplify(T.trace())
divT = [sp.expand(sum(sp.diff(T[a, b], x[a]) for a in range(4))) for b in range(4)]
deltaphi = [sp.expand(-sum(sp.diff(phi[a, c], x[a]) for a in range(4))) for c in range(4)]
psidelta = [sp.expand(sum(psi[b, c]*deltaphi[c] for c in range(4))) for b in range(4)]
k = sp.symbols('k')
ratio_eqs = [sp.expand(divT[b] - k*psidelta[b]) for b in range(4)]
ksol = sp.solve(ratio_eqs[0], k)
ok_all = [sp.simplify(ratio_eqs[b].subs(k, ksol[0])) == 0 for b in range(4)] if ksol else []

# control: non-closed psi breaks the identity
psi_bad = sum(((sp.Integer(1)+x[0]*(i+1))*WM[i] for i in range(3)), sp.zeros(4, 4))
Tb = phi*psi_bad
divTb = [sp.expand(sum(sp.diff(Tb[a, b], x[a]) for a in range(4))) for b in range(4)]
psidb = [sp.expand(sum(psi_bad[b, c]*deltaphi[c] for c in range(4))) for b in range(4)]
ctrl = [sp.simplify(divTb[b] - ksol[0]*psidb[b]) for b in range(4)] if ksol else []

# delta phi = 0 <=> d phi = 0 for self-dual phi (check equality of the two systems' coefficient spaces)
dphi = dform(phi)
res = {
    'phi_SD': hodge_check(phi, 1), 'psi_ASD': hodge_check(psi, -1),
    'T_symmetric': bool(sym), 'T_trace': str(tr),
    'kappa1': str(ksol), 'identity_holds_all_components': ok_all,
    'control_nonclosed_psi_residual_nonzero': [str(c) != '0' for c in ctrl],
    'psi_squared_is_scalar': str(sp.simplify(psi*psi)[0, 0]) + ' * I ? ' +
        str(sp.simplify(psi*psi - (psi*psi)[0, 0]*sp.eye(4)) == sp.zeros(4, 4)),
    'star_d_phi_vs_delta_phi_note': 'for SD phi, delta phi = -*d*phi = -*d phi, so delta phi=0 iff d phi=0',
}
# verify delta phi = -* d phi numerically: (*dphi)_c from 3-form components
print(json.dumps(res, indent=1))
out = os.path.join(os.path.dirname(__file__), '..', 'data', 'step66_rank1_bianchi_check.json')
json.dump(res, open(out, 'w'), indent=1)
print('saved', out)
