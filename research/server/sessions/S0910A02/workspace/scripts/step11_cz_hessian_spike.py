"""
Step 11 (S0910A02): Calderon-Zygmund Hessian spike for C^0-Ricci-pinched
four-manifolds.

GOAL
----
Decide whether a Cheeger--Tian-type POINTWISE epsilon-regularity theorem can
hold under the Yau-26 hypothesis  ||Ric_g - g||_{L^oo,op} <= delta  alone.

MECHANISM
---------
Doubly warped metric over a flat 2-dimensional base with TWO circle fibers
whose warpings move in OPPOSITE directions:

    g = dx^2 + dy^2 + e^{2 f1} dth^2 + e^{2 f2} dph^2 ,
    f1 = F1(x) + u(x,y),   f2 = F2(y) - u(x,y).

For such metrics the Ricci tensor sees only  Delta u  and  grad u , because the
Hessian of u cancels between the two fibers, while the Riemann tensor sees the
FULL Hessian  nabla^2 u  in the mixed base-fiber planes.  Hence a bounded
Laplacian with unbounded Hessian (the classical Calderon-Zygmund endpoint in
dimension two) yields tight Ricci pinching with pointwise curvature blow-up.

Background:  F1 = log sin x, F2 = log sin y  makes  g  the product of two unit
round 2-spheres, so  Ric = g  exactly (closed manifold S^2 x S^2, positive
Einstein, normalized exactly as in Yau 26).

SPIKE FUNCTION
--------------
    u = a * chi(r/rho) * X*Y * L_sigma(r),
    L_sigma(r) = -1/2 log(r^2 + sigma^2),
    X = x - pi/2, Y = y - pi/2, r = sqrt(X^2+Y^2).

Key exact facts (verified below):
    Delta(XY L_sigma) = XY [ -2 sigma^2/(r^2+sigma^2)^2 - 4/(r^2+sigma^2) ],
      so  |Delta(XY L_sigma)| <= 9/4  uniformly in sigma;
    (XY L_sigma)_{XY}(0) = L_sigma(0) = log(1/sigma)  ->  infinity.

OUTPUTS
-------
    Sessions/S0910A02/workspace/data/step11_cz_hessian_spike.json
"""

import json
import math
import os

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)
OUT = os.path.join(DATA, "step11_cz_hessian_spike.json")

report = {}

# ----------------------------------------------------------------------
# PART A. Symbolic curvature of the doubly warped metric, generic f1, f2
# ----------------------------------------------------------------------

x, y, th, ph = sp.symbols("x y th ph", real=True)
coords = [x, y, th, ph]
f1 = sp.Function("f1")(x, y)
f2 = sp.Function("f2")(x, y)

g = sp.diag(1, 1, sp.exp(2 * f1), sp.exp(2 * f2))
ginv = g.inv()


def christoffel(g, ginv, coords):
    n = len(coords)
    Gam = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = sp.S(0)
                for d in range(n):
                    s += ginv[a, d] * (
                        sp.diff(g[d, b], coords[c])
                        + sp.diff(g[d, c], coords[b])
                        - sp.diff(g[b, c], coords[d])
                    )
                Gam[a][b][c] = sp.simplify(s / 2)
    return Gam


def riemann_down(g, Gam, coords):
    """R_{abcd} with R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + ..."""
    n = len(coords)
    Rup = [[[[sp.S(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    expr = sp.diff(Gam[a][d][b], coords[c]) - sp.diff(
                        Gam[a][c][b], coords[d]
                    )
                    for e in range(n):
                        expr += Gam[a][c][e] * Gam[e][d][b]
                        expr -= Gam[a][d][e] * Gam[e][c][b]
                    Rup[a][b][c][d] = sp.simplify(expr)
    Rd = [[[[sp.S(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    s = sp.S(0)
                    for e in range(n):
                        s += g[a, e] * Rup[e][b][c][d]
                    Rd[a][b][c][d] = sp.simplify(s)
    return Rup, Rd


Gam = christoffel(g, ginv, coords)
Rup, Rdown = riemann_down(g, Gam, coords)

n = 4
Ric = sp.zeros(n, n)
for b in range(n):
    for d in range(n):
        s = sp.S(0)
        for a in range(n):
            s += Rup[a][b][a][d]
        Ric[b, d] = sp.simplify(s)

# orthonormal frame: e_x, e_y, e_th = e^{-f1} d_th, e_ph = e^{-f2} d_ph
scale = [sp.S(1), sp.S(1), sp.exp(-f1), sp.exp(-f2)]
Ric_fr = sp.zeros(n, n)
for i in range(n):
    for j in range(n):
        Ric_fr[i, j] = sp.simplify(Ric[i, j] * scale[i] * scale[j])

u1x, u1y = sp.diff(f1, x), sp.diff(f1, y)
u2x, u2y = sp.diff(f2, x), sp.diff(f2, y)
lap1 = sp.diff(f1, x, 2) + sp.diff(f1, y, 2)
lap2 = sp.diff(f2, x, 2) + sp.diff(f2, y, 2)

claims_A = {}
# base block:  Ric_ab = -[Hess f1 + df1 df1 + Hess f2 + df2 df2]_ab
for (i, ci) in ((0, x), (1, y)):
    for (j, cj) in ((0, x), (1, y)):
        claim = -(
            sp.diff(f1, ci, cj)
            + sp.diff(f1, ci) * sp.diff(f1, cj)
            + sp.diff(f2, ci, cj)
            + sp.diff(f2, ci) * sp.diff(f2, cj)
        )
        claims_A[f"Ric_base_{i}{j}"] = bool(
            sp.simplify(Ric_fr[i, j] - claim) == 0
        )
# fiber blocks
claim_th = -(lap1 + (u1x**2 + u1y**2) + (u1x * u2x + u1y * u2y))
claim_ph = -(lap2 + (u2x**2 + u2y**2) + (u1x * u2x + u1y * u2y))
claims_A["Ric_fiber_th"] = bool(sp.simplify(Ric_fr[2, 2] - claim_th) == 0)
claims_A["Ric_fiber_ph"] = bool(sp.simplify(Ric_fr[3, 3] - claim_ph) == 0)
claims_A["Ric_mixed_vanish"] = bool(
    all(
        sp.simplify(Ric_fr[i, j]) == 0
        for (i, j) in ((0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    )
)

# mixed base-fiber Riemann in frame: R(e_a, e_th, e_b, e_th)
Rm_fr_claims = {}
for (i, ci) in ((0, x), (1, y)):
    for (j, cj) in ((0, x), (1, y)):
        val = sp.simplify(Rdown[i][2][j][2] * sp.exp(-2 * f1))
        claim = -(sp.diff(f1, ci, cj) + sp.diff(f1, ci) * sp.diff(f1, cj))
        Rm_fr_claims[f"R_a{i}th_b{j}th"] = bool(sp.simplify(val - claim) == 0)
        val2 = sp.simplify(Rdown[i][3][j][3] * sp.exp(-2 * f2))
        claim2 = -(sp.diff(f2, ci, cj) + sp.diff(f2, ci) * sp.diff(f2, cj))
        Rm_fr_claims[f"R_a{i}ph_b{j}ph"] = bool(sp.simplify(val2 - claim2) == 0)

report["partA_generic_doubly_warped"] = {
    "ricci_formulas_verified": claims_A,
    "mixed_riemann_formulas_verified": Rm_fr_claims,
    "meaning": (
        "Ricci depends on f1,f2 through Hess f1 + Hess f2 (base block) and "
        "Delta f_i (fiber blocks); the mixed base-fiber Riemann components see "
        "Hess f1 and Hess f2 SEPARATELY."
    ),
}

# ----------------------------------------------------------------------
# PART B. Opposite warpings on the S^2 x S^2 background
# ----------------------------------------------------------------------

u = sp.Function("u")(x, y)
F1 = sp.log(sp.sin(x))
F2 = sp.log(sp.sin(y))
sub = {f1: F1 + u, f2: F2 - u}


def subst(expr):
    e = expr
    # replace derivatives first (sympy handles via .subs on Function)
    e = e.subs({sp.Derivative: sp.Derivative})
    return sp.simplify(e.subs({f1: F1 + u, f2: F2 - u}).doit())


# Build Ricci in frame directly from the verified formulas, with f1=F1+u, f2=F2-u
G1 = F1 + u
G2 = F2 - u


def hess(F, ci, cj):
    return sp.diff(F, ci, cj)


base_coords = [(0, x), (1, y)]
Ric_pert = sp.zeros(4, 4)
for (i, ci) in base_coords:
    for (j, cj) in base_coords:
        Ric_pert[i, j] = sp.simplify(
            -(
                hess(G1, ci, cj)
                + sp.diff(G1, ci) * sp.diff(G1, cj)
                + hess(G2, ci, cj)
                + sp.diff(G2, ci) * sp.diff(G2, cj)
            )
        )
lapG1 = sp.diff(G1, x, 2) + sp.diff(G1, y, 2)
lapG2 = sp.diff(G2, x, 2) + sp.diff(G2, y, 2)
dG1dG2 = sp.diff(G1, x) * sp.diff(G2, x) + sp.diff(G1, y) * sp.diff(G2, y)
n1 = sp.diff(G1, x) ** 2 + sp.diff(G1, y) ** 2
n2 = sp.diff(G2, x) ** 2 + sp.diff(G2, y) ** 2
Ric_pert[2, 2] = sp.simplify(-(lapG1 + n1 + dG1dG2))
Ric_pert[3, 3] = sp.simplify(-(lapG2 + n2 + dG1dG2))

E = sp.simplify(Ric_pert - sp.eye(4))  # defect Ric - g in the orthonormal frame

ux, uy = sp.diff(u, x), sp.diff(u, y)
uxx, uyy, uxy = sp.diff(u, x, 2), sp.diff(u, y, 2), sp.diff(u, x, y)
lapu = uxx + uyy

# Claim: base block of E has NO second derivatives of u at all.
base_second_free = all(
    sp.simplify(sp.diff(E[i, j], d)) == 0
    for (i, _) in base_coords
    for (j, _) in base_coords
    for d in (uxx, uyy, uxy)
)
# Claim: fiber blocks depend on second derivatives only through lap u.
fiber_only_lap = (
    bool(sp.simplify(sp.diff(E[2, 2], uxx) - sp.diff(E[2, 2], uyy)) == 0)
    and bool(sp.simplify(sp.diff(E[2, 2], uxy)) == 0)
    and bool(sp.simplify(sp.diff(E[3, 3], uxx) - sp.diff(E[3, 3], uyy)) == 0)
    and bool(sp.simplify(sp.diff(E[3, 3], uxy)) == 0)
)
# exact expressions
E22 = sp.simplify(sp.expand(E[2, 2]))
E33 = sp.simplify(sp.expand(E[3, 3]))
Exx = sp.simplify(sp.expand(E[0, 0]))
Eyy = sp.simplify(sp.expand(E[1, 1]))
Exy = sp.simplify(sp.expand(E[0, 1]))

# Riemann mixed components contain full Hessian of u
Rxthxth = sp.simplify(-(hess(G1, x, x) + sp.diff(G1, x) ** 2))
Rxphxph = sp.simplify(-(hess(G2, x, x) + sp.diff(G2, x) ** 2))
Rxythy = sp.simplify(-(hess(G1, x, y) + sp.diff(G1, x) * sp.diff(G1, y)))

report["partB_perturbed_S2xS2"] = {
    "background": "f1=log sin x, f2=log sin y gives Ric=g exactly (S^2(1) x S^2(1))",
    "perturbation": "f1=log sin x + u, f2=log sin y - u",
    "defect_base_block_free_of_second_derivatives_of_u": bool(base_second_free),
    "defect_fiber_blocks_depend_on_second_derivatives_only_via_Laplacian": bool(
        fiber_only_lap
    ),
    "E_xx": sp.sstr(Exx),
    "E_yy": sp.sstr(Eyy),
    "E_xy": sp.sstr(Exy),
    "E_thth": sp.sstr(E22),
    "E_phph": sp.sstr(E33),
    "R_x_th_x_th": sp.sstr(Rxthxth),
    "R_x_ph_x_ph": sp.sstr(Rxphxph),
    "R_x_th_y_th": sp.sstr(Rxythy),
    "conclusion": (
        "||Ric-g||_op <= C(|grad u| + |Delta u| + |grad u|^2) with C depending "
        "only on cot x, cot y on the support; but the mixed Riemann components "
        "equal -u_ab + O(1) and -(-u_ab) + O(1), so |Rm| >= |Hess u| - C."
    ),
}

# ----------------------------------------------------------------------
# PART C. The spike function: exact identities
# ----------------------------------------------------------------------

X, Y, sig, r = sp.symbols("X Y sigma r", positive=True)
Xs, Ys = sp.symbols("X Y", real=True)
rr = sp.sqrt(Xs**2 + Ys**2)
Lsig = -sp.Rational(1, 2) * sp.log(Xs**2 + Ys**2 + sig**2)
w = Xs * Ys * Lsig

lap_w = sp.simplify(sp.diff(w, Xs, 2) + sp.diff(w, Ys, 2))
lap_w_claim = Xs * Ys * (
    -2 * sig**2 / (Xs**2 + Ys**2 + sig**2) ** 2 - 4 / (Xs**2 + Ys**2 + sig**2)
)
lap_ok = bool(sp.simplify(lap_w - lap_w_claim) == 0)

# sup |Delta w| bound: |XY| <= (X^2+Y^2)/2 = R/2, and with S=R+sig^2,
#   |Delta w| <= (R/2)(2 sig^2/S^2 + 4/S) <= 1/4 + 2 = 9/4
Rv, Sv = sp.symbols("Rv Sv", positive=True)
bound_expr = (Rv / 2) * (2 * (Sv - Rv) / Sv**2 + 4 / Sv)
# maximize over 0<=Rv<=Sv
crit = sp.simplify(sp.solve(sp.diff(bound_expr.subs(Sv, 1), Rv), Rv))
max_bound = sp.simplify(sp.Max(*[bound_expr.subs({Sv: 1, Rv: c}) for c in crit]))

wxy0 = sp.simplify(sp.diff(w, Xs, Ys).subs({Xs: 0, Ys: 0}))

report["partC_spike_identities"] = {
    "laplacian_identity_verified": lap_ok,
    "laplacian_identity": sp.sstr(lap_w_claim),
    "sup_abs_laplacian_bound_scale_invariant": float(max_bound),
    "sup_bound_analytic": "9/4 (crude); exact optimum printed above",
    "mixed_hessian_at_origin": sp.sstr(wxy0),
    "meaning": (
        "w = X*Y*L_sigma has |Delta w| bounded by a universal constant "
        "independent of sigma, while w_{XY}(0) = log(1/sigma) diverges."
    ),
}

# ----------------------------------------------------------------------
# PART D. Numerical verification of the full family on S^2 x S^2
# ----------------------------------------------------------------------

# smooth cutoff chi: 1 on r<=rho/2, 0 on r>=rho
t = sp.symbols("t", real=True)
psi = sp.Piecewise((sp.exp(-1 / t), t > 0), (0, True))
chi_expr = psi.subs(t, 1 - 2 * sp.sqrt(Xs**2 + Ys**2) / sp.Symbol("rho", positive=True))
rho = sp.Symbol("rho", positive=True)
rr_s = sp.sqrt(Xs**2 + Ys**2)
s_var = (rr_s / rho - sp.Rational(1, 2)) * 2  # 0 at rho/2, 1 at rho
psi_a = sp.Piecewise((sp.exp(-1 / (1 - s_var)), s_var < 1), (0, True))
psi_b = sp.Piecewise((sp.exp(-1 / s_var), s_var > 0), (0, True))
chi = sp.Piecewise(
    (sp.S(1), rr_s <= rho / 2),
    (psi_a / (psi_a + psi_b), rr_s < rho),
    (sp.S(0), True),
)

a_sym = sp.Symbol("a", positive=True)
U = a_sym * chi * Xs * Ys * Lsig

# derivatives of U
dU = {
    "u": U,
    "ux": sp.diff(U, Xs),
    "uy": sp.diff(U, Ys),
    "uxx": sp.diff(U, Xs, 2),
    "uyy": sp.diff(U, Ys, 2),
    "uxy": sp.diff(U, Xs, Ys),
}
args = (Xs, Ys, a_sym, sig, rho)
fU = {k: sp.lambdify(args, v, "numpy") for k, v in dU.items()}

# exact frame components of Ric-g and of Rm for the perturbed metric,
# as functions of (x, y, u, ux, uy, uxx, uyy, uxy)
u_s, ux_s, uy_s, uxx_s, uyy_s, uxy_s = sp.symbols(
    "u_s ux_s uy_s uxx_s uyy_s uxy_s", real=True
)
repl = {
    u: u_s,
    sp.Derivative(u, x): ux_s,
    sp.Derivative(u, y): uy_s,
    sp.Derivative(u, (x, 2)): uxx_s,
    sp.Derivative(u, (y, 2)): uyy_s,
    sp.Derivative(u, x, y): uxy_s,
}


def to_num(expr):
    e = expr.subs(sp.Derivative(u, x, y), uxy_s)
    e = e.subs(sp.Derivative(u, (x, 2)), uxx_s)
    e = e.subs(sp.Derivative(u, (y, 2)), uyy_s)
    e = e.subs(sp.Derivative(u, x), ux_s)
    e = e.subs(sp.Derivative(u, y), uy_s)
    e = e.subs(u, u_s)
    return e


num_args = (x, y, u_s, ux_s, uy_s, uxx_s, uyy_s, uxy_s)
E_num = [[sp.lambdify(num_args, to_num(E[i, j]), "numpy") for j in range(4)] for i in range(4)]

# full Riemann in the frame for the perturbed metric.
# nonzero independent frame components:
#   R(e_a,e_th,e_b,e_th) = -(Hess G1 + dG1 dG1)_{ab}
#   R(e_a,e_ph,e_b,e_ph) = -(Hess G2 + dG2 dG2)_{ab}
#   R(e_th,e_ph,e_th,e_ph) = -dG1 . dG2
#   base 2-plane curvature = 0 (flat 2d base)
A1 = sp.Matrix(
    2,
    2,
    lambda i, j: -(
        hess(G1, base_coords[i][1], base_coords[j][1])
        + sp.diff(G1, base_coords[i][1]) * sp.diff(G1, base_coords[j][1])
    ),
)
A2 = sp.Matrix(
    2,
    2,
    lambda i, j: -(
        hess(G2, base_coords[i][1], base_coords[j][1])
        + sp.diff(G2, base_coords[i][1]) * sp.diff(G2, base_coords[j][1])
    ),
)
B12 = -dG1dG2

A1_num = [[sp.lambdify(num_args, to_num(A1[i, j]), "numpy") for j in range(2)] for i in range(2)]
A2_num = [[sp.lambdify(num_args, to_num(A2[i, j]), "numpy") for j in range(2)] for i in range(2)]
B12_num = sp.lambdify(num_args, to_num(B12), "numpy")


def eval_family(a_val, Lam, rho_val, n_r=4000, n_t=180):
    """Return sup norms and L^2 norms on the spike disc."""
    sig_val = math.exp(-Lam)
    # log-spaced radii from sig/100 to rho
    rmin = max(sig_val / 100.0, 1e-300)
    rs = np.concatenate(
        [
            np.array([0.0]),
            np.exp(np.linspace(math.log(rmin), math.log(rho_val * 0.999), n_r)),
        ]
    )
    ts = np.linspace(0.0, 2 * math.pi, n_t, endpoint=False)
    R_, T_ = np.meshgrid(rs, ts, indexing="ij")
    Xg = R_ * np.cos(T_)
    Yg = R_ * np.sin(T_)

    vals = {}
    for k, f in fU.items():
        with np.errstate(all="ignore"):
            vals[k] = np.nan_to_num(
                np.asarray(f(Xg, Yg, a_val, sig_val, rho_val), dtype=float),
                nan=0.0,
                posinf=0.0,
                neginf=0.0,
            )

    lap = vals["uxx"] + vals["uyy"]
    grad = np.sqrt(vals["ux"] ** 2 + vals["uy"] ** 2)
    # Hessian Frobenius norm
    hessn = np.sqrt(vals["uxx"] ** 2 + vals["uyy"] ** 2 + 2 * vals["uxy"] ** 2)

    # base point (pi/2, pi/2) -> coordinates x=pi/2+X, y=pi/2+Y
    xg = math.pi / 2 + Xg
    yg = math.pi / 2 + Yg

    Ework = np.zeros(Xg.shape + (4, 4))
    for i in range(4):
        for j in range(4):
            with np.errstate(all="ignore"):
                out = E_num[i][j](
                    xg, yg, vals["u"], vals["ux"], vals["uy"],
                    vals["uxx"], vals["uyy"], vals["uxy"],
                )
            Ework[..., i, j] = np.nan_to_num(np.broadcast_to(np.asarray(out, dtype=float), Xg.shape))
    Esym = 0.5 * (Ework + np.swapaxes(Ework, -1, -2))
    eigs = np.linalg.eigvalsh(Esym)
    delta_field = np.max(np.abs(eigs), axis=-1)

    # |Rm|^2 in the frame (sum over all index positions)
    A1v = np.zeros(Xg.shape + (2, 2))
    A2v = np.zeros(Xg.shape + (2, 2))
    for i in range(2):
        for j in range(2):
            A1v[..., i, j] = np.nan_to_num(
                np.broadcast_to(
                    np.asarray(
                        A1_num[i][j](xg, yg, vals["u"], vals["ux"], vals["uy"],
                                     vals["uxx"], vals["uyy"], vals["uxy"]),
                        dtype=float,
                    ),
                    Xg.shape,
                )
            )
            A2v[..., i, j] = np.nan_to_num(
                np.broadcast_to(
                    np.asarray(
                        A2_num[i][j](xg, yg, vals["u"], vals["ux"], vals["uy"],
                                     vals["uxx"], vals["uyy"], vals["uxy"]),
                        dtype=float,
                    ),
                    Xg.shape,
                )
            )
    B12v = np.nan_to_num(
        np.broadcast_to(
            np.asarray(
                B12_num(xg, yg, vals["u"], vals["ux"], vals["uy"],
                        vals["uxx"], vals["uyy"], vals["uxy"]),
                dtype=float,
            ),
            Xg.shape,
        )
    )
    # |Rm|^2 = 4 * sum_{a<=b}(mult) ... count: for each sectional-type pair
    # R_{abab} appears with multiplicity 4, R_{abab'} etc.  Use the standard
    # count for a diagonal "curvature operator" of this warped type:
    #   |Rm|^2 = 4 * [ sum_{i,j} (A1_{ij}^2 + A2_{ij}^2) + B12^2 ]
    Rm2 = 4.0 * (np.sum(A1v**2, axis=(-1, -2)) + np.sum(A2v**2, axis=(-1, -2)) + B12v**2)
    Rmn = np.sqrt(Rm2)

    # L^2 integrals over the base disc with the fiber volume factor
    # vol element = sin(x) e^{u} * sin(y) e^{-u} dx dy dth dph = sin x sin y dx dy dth dph
    wgt = np.sin(xg) * np.sin(yg)
    # radial trapezoid in r with measure r dr dtheta, times (2 pi)^2 fiber area
    dth = ts[1] - ts[0]
    fiber = (2 * math.pi) ** 2

    def l2(field):
        f = field**2 * wgt * R_
        # integrate in r (trapezoid over nonuniform grid) then sum in theta
        inner = np.trapz(f, rs, axis=0)
        return math.sqrt(float(np.sum(inner) * dth * fiber))

    return {
        "a": a_val,
        "Lambda_log_inv_sigma": Lam,
        "sigma": sig_val,
        "rho": rho_val,
        "sup_grad_u": float(np.max(grad)),
        "sup_abs_lap_u": float(np.max(np.abs(lap))),
        "sup_hess_u": float(np.max(hessn)),
        "L2_hess_u_base": float(
            math.sqrt(
                float(np.sum(np.trapz(hessn**2 * R_, rs, axis=0)) * dth)
            )
        ),
        "sup_delta_Ric_minus_g_op": float(np.max(delta_field)),
        "sup_Rm_norm": float(np.max(Rmn)),
        "background_sup_Rm_norm": float(np.min(Rmn)),
        "L2_Rm_on_spike_disc": l2(Rmn),
        "scale_invariant_rho2_sup_Rm": float(rho_val**2 * np.max(Rmn)),
    }


rho_val = 0.30
cases = []
for Lam in (10.0, 30.0, 100.0, 300.0):
    a_val = Lam ** (-2.0 / 3.0)
    cases.append(eval_family(a_val, Lam, rho_val))

report["partD_numerical_family"] = {
    "parametrization": "a = Lambda^{-2/3}, sigma = exp(-Lambda), rho = 0.30 fixed",
    "design": (
        "a -> 0 kills the Ricci defect (order a); a*Lambda = Lambda^{1/3} -> oo "
        "drives the pointwise Hessian, hence |Rm|, to infinity."
    ),
    "cases": cases,
}

# ----------------------------------------------------------------------
# PART E. What the family refutes and what survives
# ----------------------------------------------------------------------

report["partE_conclusions"] = {
    "refuted_statement": (
        "There exist eps, C, delta_0 > 0 such that any closed Riemannian "
        "4-manifold with ||Ric_g - g||_{L^oo,op} <= delta_0 and "
        "int_{B_r(p)}|Rm|^2 <= eps satisfies sup_{B_{r/2}(p)}|Rm| <= C r^{-2}."
    ),
    "refutation_mode": (
        "On the fixed closed manifold S^2 x S^2 the family g_j has "
        "delta_j -> 0, fixed r = rho, int_{B_rho}|Rm|^2 as small as desired "
        "(shrink rho, then a), and rho^2 sup_{B_{rho/2}}|Rm| -> oo."
    ),
    "survives_1_harmonic_radius": (
        "grad u is log-Lipschitz, so |grad u|_{C^alpha} <= C_alpha * a for every "
        "alpha < 1: the C^{1,alpha} harmonic radius stays uniformly bounded "
        "below.  Cheeger-Naber / Naber-Zhang harmonic-radius theory is untouched."
    ),
    "survives_2_Lp_and_BMO": (
        "Calderon-Zygmund gives ||Hess u||_{L^p} <= C_p ||Delta u||_{L^p} and "
        "||Hess u||_{BMO} <= C ||Delta u||_{L^oo}; both are O(a) -> 0 here.  So "
        "an L^p / BMO epsilon-regularity statement is consistent with the family."
    ),
    "consequence_for_the_program": (
        "Any Yau-26 route that needs a POINTWISE curvature bound from C^0 Ricci "
        "pinching plus small local L^2 energy is dead as stated.  The keystone "
        "must be restated in L^p or BMO, or the pointwise step must be reached "
        "through Li smoothing / Naber-Zhang covers, where the conclusion is "
        "about a smoothed metric or a cover chart rather than about g itself."
    ),
    "scope_limits": (
        "This is NOT a counterexample to Yau 26: S^2 x S^2 carries the product "
        "Einstein metric.  It is a counterexample to a regularity lemma. It also "
        "does not contradict Cheeger-Tian, whose hypothesis is exactly Einstein."
    ),
}

with open(OUT, "w") as fh:
    json.dump(report, fh, indent=2, default=str)

print("=" * 72)
print("PART A: generic doubly warped curvature formulas")
print("=" * 72)
for k, v in report["partA_generic_doubly_warped"]["ricci_formulas_verified"].items():
    print(f"  {k:22s} verified = {v}")
for k, v in report["partA_generic_doubly_warped"]["mixed_riemann_formulas_verified"].items():
    print(f"  {k:22s} verified = {v}")

print()
print("=" * 72)
print("PART B: opposite warpings on S^2(1) x S^2(1)")
print("=" * 72)
pb = report["partB_perturbed_S2xS2"]
print("  base block free of Hess u :", pb["defect_base_block_free_of_second_derivatives_of_u"])
print("  fiber blocks only via Lap :", pb["defect_fiber_blocks_depend_on_second_derivatives_only_via_Laplacian"])
print("  E_xx   =", pb["E_xx"])
print("  E_yy   =", pb["E_yy"])
print("  E_xy   =", pb["E_xy"])
print("  E_thth =", pb["E_thth"])
print("  E_phph =", pb["E_phph"])
print("  R_x_th_x_th =", pb["R_x_th_x_th"])
print("  R_x_ph_x_ph =", pb["R_x_ph_x_ph"])

print()
print("=" * 72)
print("PART C: spike identities")
print("=" * 72)
pc = report["partC_spike_identities"]
print("  Laplacian identity verified:", pc["laplacian_identity_verified"])
print("  Delta(XY L_sigma) =", pc["laplacian_identity"])
print("  scale-invariant sup bound   =", pc["sup_abs_laplacian_bound_scale_invariant"])
print("  w_XY(0) =", pc["mixed_hessian_at_origin"])

print()
print("=" * 72)
print("PART D: numerical family on S^2 x S^2  (rho = %.2f)" % rho_val)
print("=" * 72)
hdr = (
    f"{'Lambda':>8} {'a':>9} {'sup|du|':>10} {'sup|Lap u|':>11} "
    f"{'sup|Hess u|':>12} {'delta':>10} {'sup|Rm|':>10} {'rho^2 sup|Rm|':>14} {'L2 Rm':>10}"
)
print(hdr)
for c in cases:
    print(
        f"{c['Lambda_log_inv_sigma']:>8.0f} {c['a']:>9.4f} {c['sup_grad_u']:>10.4f} "
        f"{c['sup_abs_lap_u']:>11.4f} {c['sup_hess_u']:>12.4f} "
        f"{c['sup_delta_Ric_minus_g_op']:>10.4f} {c['sup_Rm_norm']:>10.3f} "
        f"{c['scale_invariant_rho2_sup_Rm']:>14.3f} {c['L2_Rm_on_spike_disc']:>10.4f}"
    )

print()
print("Saved:", OUT)
