"""Step 45: exact curvature of the biaxial Taub-NUT and Taub-NUT-AdS cells.

Frame (Euler-angle sigma_i with d sigma_i = -sigma_j ^ sigma_k, psi period 4 pi):
    e0 = A dR, e1 = B sigma1, e2 = B sigma2, e3 = C sigma3.
GH / Taub-NUT (Ric=0):         A^2=H,    B^2=H R^2, C^2=ell^2/H,      H=1+ell/R.
TNAdS (claimed Ric=-g):        A^2=H/F,  B^2=H R^2, C^2=ell^2 F/H,    F=1+R(R+2 ell)/3.

The script solves the first Cartan equation symbolically, builds the curvature
operator, and outputs: Ricci, the chirality of the vanishing Weyl half, |W|^2,
the scalar Laplacian, the exact volume density, and the evaluation of these
quantities on the flux-balance radius R(R+ell)^2 = 3 ell/4.
Output: workspace/data/step45/tnads_cartan.json
"""
import json, os, itertools
import sympy as sp

R, ell = sp.symbols('R ell', positive=True)
H = 1 + ell / R


def frame_structure(A, B, C):
    """de^a = sum_{b<c} D[a][(b,c)] e^b^e^c."""
    D = [dict() for _ in range(4)]
    D[1][(0, 1)] = sp.diff(B, R) / (A * B); D[1][(2, 3)] = -B / (B * C)
    D[2][(0, 2)] = sp.diff(B, R) / (A * B); D[2][(1, 3)] = +B / (C * B)   # -(1/C) e31 = +(1/C) e13
    D[3][(0, 3)] = sp.diff(C, R) / (A * C); D[3][(1, 2)] = -C / (B * B)
    return D


def two_form_from_dict(dct):
    M = sp.zeros(4)
    for (b, c), v in dct.items():
        M[b, c] += v; M[c, b] -= v
    return M


def wedge11(a, b):
    """a,b: 1-form coefficient lists -> antisymmetric matrix of a^b (coefficient of e^i^e^j is M[i,j], i<j)."""
    M = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            M[i, j] = a[i] * b[j] - a[j] * b[i]
    return M


def curvature(A, B, C):
    D = frame_structure(A, B, C)
    dE = [two_form_from_dict(D[a]) for a in range(4)]
    # unknown connection omega_{ab} = sum_c w[a,b,c] e^c, antisymmetric in a,b
    w = {}
    syms = []
    for a in range(4):
        for b in range(a + 1, 4):
            for c in range(4):
                s = sp.Symbol(f'w_{a}{b}{c}'); syms.append(s)
                w[(a, b, c)] = s; w[(b, a, c)] = -s
    for a in range(4):
        for c in range(4):
            w[(a, a, c)] = 0
    eqs = []
    for a in range(4):
        tot = dE[a]
        for b in range(4):
            tot = tot + wedge11([w[(a, b, c)] for c in range(4)], [1 if k == b else 0 for k in range(4)])
        for i in range(4):
            for j in range(i + 1, 4):
                eqs.append(sp.expand(tot[i, j]))
    sol = sp.solve(eqs, syms, dict=True)[0]
    om = {(a, b): [sp.simplify(sp.sympify(w[(a, b, c)]).subs(sol)) for c in range(4)] for a in range(4) for b in range(4)}

    def d1(alpha):
        M = sp.zeros(4)
        for a in range(4):
            if alpha[a] == 0:
                continue
            da = sp.diff(alpha[a], R) / A
            M += wedge11([da, 0, 0, 0], [1 if k == a else 0 for k in range(4)])
            M += alpha[a] * dE[a]
        return M

    Om = {}
    for a in range(4):
        for b in range(4):
            M = d1(om[(a, b)])
            for c in range(4):
                M += wedge11(om[(a, c)], om[(c, b)])
            Om[(a, b)] = M.applyfunc(sp.simplify)
    Riem = {}
    for a, b, c, d in itertools.product(range(4), repeat=4):
        Riem[(a, b, c, d)] = Om[(a, b)][c, d]
    return Riem


def invariants(Riem):
    Ric = sp.zeros(4)
    for b in range(4):
        for d in range(4):
            Ric[b, d] = sp.simplify(sum(Riem[(a, b, a, d)] for a in range(4)))
    s = sp.simplify(sum(Ric[i, i] for i in range(4)))
    # curvature operator on 2-forms in basis e01,e02,e03,e23,e31,e12
    pairs = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
    Rop = sp.Matrix(6, 6, lambda i, j: Riem[pairs[i] + pairs[j]])
    Pp = sp.Matrix([[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]) / sp.sqrt(2)
    Pm = sp.Matrix([[1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, -1]]) / sp.sqrt(2)
    Wp = (Pp * Rop * Pp.T).applyfunc(sp.simplify)
    Wm = (Pm * Rop * Pm.T).applyfunc(sp.simplify)
    Wp0 = (Wp - sp.eye(3) * Wp.trace() / 3).applyfunc(sp.simplify)
    Wm0 = (Wm - sp.eye(3) * Wm.trace() / 3).applyfunc(sp.simplify)
    # operator norm convention: |W|^2 = sum of squares of the 3x3 matrix entries
    return Ric, s, Wp0, Wm0


def main():
    F = 1 + R * (R + 2 * ell) / 3
    cases = {
        'TN': (sp.sqrt(H), R * sp.sqrt(H), ell / sp.sqrt(H)),
        'TNAdS': (sp.sqrt(H / F), R * sp.sqrt(H), ell * sp.sqrt(F / H)),
    }
    out = {}
    W2 = {}
    for name, (A, B, C) in cases.items():
        Riem = curvature(A, B, C)
        Ric, s, Wp0, Wm0 = invariants(Riem)
        Wp2 = sp.simplify(sum(x**2 for x in Wp0))
        Wm2 = sp.simplify(sum(x**2 for x in Wm0))
        W2[name] = (sp.factor(Wp2), sp.factor(Wm2))
        vol = sp.simplify(A * B**2 * C)
        out[name] = dict(
            Ricci_diag=[str(sp.factor(Ric[i, i])) for i in range(4)],
            Ricci_offdiag_zero=bool(all(sp.simplify(Ric[i, j]) == 0 for i in range(4) for j in range(4) if i != j)),
            scalar=str(sp.simplify(s)),
            Wplus_sq_e0123=str(sp.factor(Wp2)),
            Wminus_sq_e0123=str(sp.factor(Wm2)),
            Wplus_eigs=[str(sp.factor(Wp0[i, i])) for i in range(3)],
            Wminus_eigs=[str(sp.factor(Wm0[i, i])) for i in range(3)],
            volume_density_per_sigma123=str(vol),
            radial_laplacian="(1/(A B^2 C)) d/dR( B^2 C/A d/dR )",
            laplacian_weight_B2C_over_A=str(sp.simplify(B**2 * C / A)),
        )
    # flux-balance radius and evaluations
    rows = []
    for lv in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        Rs = sp.nsolve(R * (R + lv)**2 - sp.Rational(3, 4) * lv, R, (0.75 * lv)**(1 / 3))
        sub = {R: Rs, ell: lv}
        vals = {}
        for name in cases:
            Wp2, Wm2 = W2[name]
            vals[name] = (float(Wp2.subs(sub)), float(Wm2.subs(sub)))
        Fm1 = float((F - 1).subs(sub))
        rows.append(dict(ell=lv, R_star=float(Rs), R_star_over_l13=float(Rs / lv**(1 / 3)),
                         TN_Wsq=vals['TN'], TNAdS_Wsq=vals['TNAdS'], F_minus_1=Fm1,
                         TN_tidal_ell_over_R3=float(lv / Rs**3)))
    out['flux_balance_rows'] = rows
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step45')
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'tnads_cartan.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
