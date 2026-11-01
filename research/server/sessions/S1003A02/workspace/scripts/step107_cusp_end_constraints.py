"""Step 107: exact symbolic checks behind the Einstein-end constraints of
`notes/step107_einstein_end_constraints_D4_object_and_specification.md`.

Checks (all symbolic, SymPy):
 (1) Left-invariant metric x1 s1^2 + x2 s2^2 + x3 s3^2 on SU(2), with
     d s_i = 2 s_j ^ s_k: principal Ricci r_i = 2[x_i^2-(x_j-x_k)^2]/(x1 x2 x3),
     r1 + r2 = 4(x1+x2-x3)/(x1 x2), Berger scalar 8/a^2 - 2c^2/a^4, round S^3: 6.
 (2) Diagonal Bianchi IX 4-metric dt^2 + sum a_i(t)^2 s_i^2:
     K(dt,e_i) = -a_i''/a_i and the Hamiltonian (Gauss) constraint
         sigma_2(lambda) = s_Sigma/2 + G(nu,nu),  lambda_i = a_i'/a_i,
     with G = Ric - s g/2.  Flat check a_i = t.
 (3) Fibred-cusp leading model g = dr^2 + e^{2phi}(dx^2+dy^2)
       + e^{-2r} f^2 (dth + A1 dx + A2 dy)^2  (coordinates r,x,y,th):
     Ric(d_r,d_r) = -1 exactly, Ric(d_r,d_x) = f_x/f + O(e^{-2r}),
     and with f const, A=0: Ric = -1 on fibre and Ric_base = K_B g_B,
     so Einstein forces f const and K_B = -1 (= lambda).
 (4) Genus-g disc-bundle caps: c = 4 - 4g + e; adjunction comparison.
Output: workspace/data/step107/cusp_end_constraints.json
"""
import json, os
import sympy as sp


def ricci_from_metric(g, X):
    n = len(X)
    ginv = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                         - sp.diff(g[b, c], X[d])) for d in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(b, n):
            expr = 0
            for a in range(n):
                expr += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    expr += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            Ric[b, c] = Ric[c, b] = sp.simplify(expr)
    return Ric, ginv


def frame_curvature(n, C, deriv):
    """Orthonormal frame with [e_i,e_j]=sum_k C[i][j][k] e_k; deriv[i](f) = e_i(f).
    Returns Riemann R[i][j][k][l] = <R(e_i,e_j)e_k, e_l>, R(X,Y)=[nabla_X,nabla_Y]-nabla_[X,Y]."""
    c = lambda i, j, k: C[i][j][k]
    # Koszul: <nabla_{e_i} e_j, e_k> = 1/2 (c_ijk - c_jki + c_kij)
    G = [[[sp.Rational(1, 2)*(c(i, j, k) - c(j, k, i) + c(k, i, j)) for k in range(n)]
          for j in range(n)] for i in range(n)]

    def nabla(i, V):  # V: list of component functions in frame
        return [deriv[i](V[k]) + sum(V[j]*G[i][j][k] for j in range(n)) for k in range(n)]
    E = [[1 if a == b else 0 for a in range(n)] for b in range(n)]
    R = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                t1 = nabla(i, [G[j][k][m] for m in range(n)])
                t2 = nabla(j, [G[i][k][m] for m in range(n)])
                br = [sum(C[i][j][m]*G[m][k][l] for m in range(n)) for l in range(n)]
                for l in range(n):
                    R[(i, j, k, l)] = sp.simplify(t1[l] - t2[l] - br[l])
    return R


out = {}
# ---------- (1) left-invariant SU(2) ----------
x1, x2, x3 = sp.symbols('x1 x2 x3', positive=True)
a = [sp.sqrt(x1), sp.sqrt(x2), sp.sqrt(x3)]
# frame e_i = X_i / a_i, [X_j,X_k] = -2 X_i (cyclic)
C3 = [[[0]*3 for _ in range(3)] for _ in range(3)]
for (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    C3[j][k][i] = -2*a[i]/(a[j]*a[k])
    C3[k][j][i] = 2*a[i]/(a[j]*a[k])
zero = lambda f: 0
R3 = frame_curvature(3, C3, [zero]*3)
ric3 = [sp.simplify(sum(R3[(m, i, i, m)] for m in range(3))) for i in range(3)]
target = [2*(x1**2-(x2-x3)**2)/(x1*x2*x3), 2*(x2**2-(x1-x3)**2)/(x1*x2*x3),
          2*(x3**2-(x1-x2)**2)/(x1*x2*x3)]
ok1 = all(sp.simplify(ric3[i]-target[i]) == 0 for i in range(3))
ok1b = sp.simplify(ric3[0]+ric3[1]-4*(x1+x2-x3)/(x1*x2)) == 0
A_, c_ = sp.symbols('A c', positive=True)
sB = sp.simplify(sum(ric3).subs({x1: A_**2, x2: A_**2, x3: c_**2}))
ok1c = sp.simplify(sB-(8/A_**2-2*c_**2/A_**4)) == 0
ok1d = sp.simplify(sum(ric3).subs({x1: 1, x2: 1, x3: 1})) == 6
out['su2_left_invariant'] = dict(ricci_formula=ok1, r1_plus_r2=ok1b, berger_scalar=ok1c,
                                 round_scalar_6=ok1d)

# ---------- (2) diagonal Bianchi IX ----------
t = sp.symbols('t', positive=True)
af = [sp.Function('a%d' % i)(t) for i in range(1, 4)]
n = 4
C4 = [[[0]*4 for _ in range(4)] for _ in range(4)]
for i in range(3):
    lam = sp.diff(af[i], t)/af[i]
    C4[0][i+1][i+1] = -lam      # [d_t, e_i] = -lambda_i e_i
    C4[i+1][0][i+1] = lam
for (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    C4[j+1][k+1][i+1] = -2*af[i]/(af[j]*af[k])
    C4[k+1][j+1][i+1] = 2*af[i]/(af[j]*af[k])
deriv = [lambda f: sp.diff(f, t)] + [zero]*3
R4 = frame_curvature(4, C4, deriv)
Ric4 = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        Ric4[i, j] = sp.simplify(sum(R4[(m, i, j, m)] for m in range(4)))
s4 = sp.simplify(sum(Ric4[i, i] for i in range(4)))
G00 = sp.simplify(Ric4[0, 0]-s4/2)
lams = [sp.diff(af[i], t)/af[i] for i in range(3)]
sig2 = lams[0]*lams[1]+lams[1]*lams[2]+lams[2]*lams[0]
X = [af[i]**2 for i in range(3)]
sSig = sum([2*(X[0]**2-(X[1]-X[2])**2), 2*(X[1]**2-(X[0]-X[2])**2),
            2*(X[2]**2-(X[0]-X[1])**2)])/(X[0]*X[1]*X[2])
ok2 = sp.simplify(sig2-(sSig/2+G00)) == 0
mixed = [sp.simplify(R4[(0, i+1, i+1, 0)]) for i in range(3)]  # <R(e0,ei)ei,e0>
ok2b = all(sp.simplify(mixed[i] + sp.diff(af[i], t, 2)/af[i]) == 0 for i in range(3))
flat = all(sp.simplify(R4[key].subs({af[0]: t, af[1]: t, af[2]: t}).doit()) == 0
           for key in R4)
offdiag = all(sp.simplify(Ric4[i, j]) == 0 for i in range(4) for j in range(4) if i != j)
out['bianchi_IX'] = dict(gauss_constraint=ok2, mixed_sectional=ok2b, flat_check=flat,
                         ricci_diagonal=offdiag)

# ---------- (3) fibred-cusp leading model ----------
r, x, y, th = sp.symbols('r x y th', real=True)
phi = sp.Function('phi')(x, y)
f = sp.Function('f')(x, y)
A1 = sp.Function('A1')(x, y)
A2 = sp.Function('A2')(x, y)
w = sp.exp(-2*r)*f**2
eta = sp.Matrix([0, A1, A2, 1])  # coefficients of dth + A1 dx + A2 dy in (r,x,y,th)
g = sp.diag(1, sp.exp(2*phi), sp.exp(2*phi), 0) + w*eta*eta.T
Ric, ginv = ricci_from_metric(g, [r, x, y, th])
ok3a = sp.simplify(Ric[0, 0] + 1) == 0
lead_rx = sp.simplify(sp.limit(sp.simplify(Ric[0, 1] - A1*Ric[0, 3]), r, sp.oo)) if False else None
# Ric(d_r, horizontal lift of d_x) = Ric[0,1] - A1 Ric[0,3]
hor = sp.simplify(Ric[0, 1] - A1*Ric[0, 3])
ok3b = sp.simplify(sp.expand(hor - sp.diff(f, x)/f).subs(sp.exp(-2*r), 0)) == 0
# special case f const, A = 0
Ric0, _ = ricci_from_metric(sp.diag(1, sp.exp(2*phi), sp.exp(2*phi), sp.exp(-2*r)), [r, x, y, th])
KB = sp.simplify(-(sp.diff(phi, x, 2)+sp.diff(phi, y, 2))*sp.exp(-2*phi))
ok3c = (sp.simplify(Ric0[3, 3]/sp.exp(-2*r) + 1) == 0 and
        sp.simplify(Ric0[1, 1]/sp.exp(2*phi) - KB) == 0 and sp.simplify(Ric0[1, 2]) == 0)
out['fibred_cusp_model'] = dict(Ric_rr_equals_minus1=ok3a,
                                Ric_r_horizontal_leading_equals_grad_log_f=ok3b,
                                fconst_fibre_minus1_base_KB=ok3c,
                                Ric_r_horizontal=str(sp.simplify(hor)))

# ---------- (4) genus caps ----------
rows = []
for gg in range(0, 5):
    for e in range(-6, 13):
        cplus = 4 - 4*gg + e
        rows.append(dict(g=gg, e=e, c_plus=cplus, admissible_charge=cplus >= 0,
                         adjunction_allows=(e <= 2*gg-2) if (gg >= 1 and e >= 0) else None))
surv = [rw for rw in rows if rw['g'] >= 2 and rw['admissible_charge'] and
        (rw['adjunction_allows'] in (True, None))]
out['genus_disc_bundle_caps'] = dict(formula='c_+ = T_+(D_e(Sigma_g)) - (-e+3 sign e) = 4-4g+e',
                                     survivors_g_ge_2=surv, rows=rows)

out['all_ok'] = bool(ok1 and ok1b and ok1c and ok1d and ok2 and ok2b and flat and offdiag
                     and ok3a and ok3b and ok3c and len(surv) == 0)
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step107')
os.makedirs(od, exist_ok=True)
with open(os.path.join(od, 'cusp_end_constraints.json'), 'w') as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({k: v for k, v in out.items() if k != 'genus_disc_bundle_caps'}, indent=1, default=str))
print('genus survivors (g>=2):', surv)
