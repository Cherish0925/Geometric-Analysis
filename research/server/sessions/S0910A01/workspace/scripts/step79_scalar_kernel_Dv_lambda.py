"""
Step 79: pilot computation of D_v lambda for scalar-sector P-kernel modes.

We compute the first variation of the product curvature block R^+ at a node of
S^2 x S^2 under local symmetric-tensor variations v = u_i g_j, where u_i is the
axial first harmonic on factor i.  The purpose is to test whether scalar-kernel
orbifold variables can alter the transverse lambda components at order t^2.

This is a local normal-coordinate calculation, not a complete Ozuch slice theorem.
It uses metric expansions to quadratic order at a product pole and normalizes the
constant metric perturbation by a linear coordinate change L=I-eps*h0/2.
"""

import json
import sympy as sp

# Coordinates and parameter.
y0, y1, y2, y3, eps = sp.symbols('y0 y1 y2 y3 eps')
y = [y0, y1, y2, y3]
K = sp.Integer(1)


def truncate_eps(expr):
    return sp.expand(expr).series(eps, 0, 2).removeO()


def sphere_block_metric(coords, indices):
    """Quadratic normal-coordinate expansion of unit-curvature S^2 block."""
    r2 = sum(coords[i]**2 for i in indices)
    G = sp.zeros(4, 4)
    for a in indices:
        for b in indices:
            delta = 1 if a == b else 0
            G[a, b] = delta - sp.Rational(1, 3) * (r2 * delta - coords[a] * coords[b])
    return G


def product_base_metric(coords):
    return sphere_block_metric(coords, [0, 1]) + sphere_block_metric(coords, [2, 3])


def harmonic(factor, sign, coords):
    if factor == 1:
        r2 = coords[0]**2 + coords[1]**2
    else:
        r2 = coords[2]**2 + coords[3]**2
    return sp.Integer(sign) * (1 - sp.Rational(1, 2) * r2)


def target_metric(target, coords):
    if target == 1:
        return sphere_block_metric(coords, [0, 1])
    else:
        return sphere_block_metric(coords, [2, 3])


def substitute_linear_metric(G, L):
    """Pull back metric G(x) under x=L*y: L^T G(Ly) L, to O(eps)."""
    x_expr = [sum(L[i, j] * y[j] for j in range(4)) for i in range(4)]
    subs = {y[i]: x_expr[i] for i in range(4)}
    G_sub = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            G_sub[a, b] = truncate_eps(G[a, b].subs(subs))
    out = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            s = 0
            for a in range(4):
                for b in range(4):
                    s += L[a, i] * G_sub[a, b] * L[b, j]
            out[i, j] = truncate_eps(s)
    return out


def metric_for_mode(source_factor, target_factor, pole_sign_source):
    G0 = product_base_metric(y)
    h = harmonic(source_factor, pole_sign_source, y) * target_metric(target_factor, y)
    G = G0 + eps * h
    # Constant h0 at the origin.
    h0 = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            h0[a, b] = sp.simplify(h[a, b].subs({yy: 0 for yy in y}))
    # Linear coordinate normalization x=(I-eps*h0/2)y gives pullback constant metric I+O(eps^2).
    L = sp.eye(4) - eps * h0 / 2
    Gnorm = substitute_linear_metric(G, L)
    return Gnorm, h0


def curvature_tensor_at_origin(G):
    zero = {yy: 0 for yy in y}
    R = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    # R_{a b c d} = 1/2(g_{a d,bc}+g_{bc,ad}-g_{ac,bd}-g_{bd,ac})
                    expr = sp.Rational(1, 2) * (
                        sp.diff(G[a, d], y[b], y[c])
                        + sp.diff(G[b, c], y[a], y[d])
                        - sp.diff(G[a, c], y[b], y[d])
                        - sp.diff(G[b, d], y[a], y[c])
                    )
                    R[(a, b, c, d)] = truncate_eps(expr.subs(zero))
    return R


def make_2form(entries):
    A = sp.zeros(4, 4)
    for i, j, v in entries:
        A[i, j] = v
        A[j, i] = -v
    return A

sqrt2 = sp.sqrt(2)
omega_p = [
    make_2form([(0, 1, 1/sqrt2), (2, 3, 1/sqrt2)]),
    make_2form([(0, 2, 1/sqrt2), (1, 3, -1/sqrt2)]),
    make_2form([(0, 3, 1/sqrt2), (1, 2, 1/sqrt2)]),
]
omega_m = [
    make_2form([(0, 1, 1/sqrt2), (2, 3, -1/sqrt2)]),
    make_2form([(0, 2, 1/sqrt2), (1, 3, 1/sqrt2)]),
    make_2form([(0, 3, 1/sqrt2), (1, 2, -1/sqrt2)]),
]


def curvature_operator_matrix(R, basis):
    # Matrix M_{ij}=<R basis_j, basis_i> with 2-form inner product 1/2 sum A_ab B_ab.
    M = sp.zeros(3, 3)
    for i, beta in enumerate(basis):
        for j, alpha in enumerate(basis):
            val = 0
            for a in range(4):
                for b in range(4):
                    for c in range(4):
                        for d in range(4):
                            # <R alpha, beta> = 1/4 beta_ab R_abcd alpha_cd
                            val += sp.Rational(1, 4) * beta[a, b] * R[(a, b, c, d)] * alpha[c, d]
            M[i, j] = sp.simplify(truncate_eps(val))
    return M

# Calibrate base.
Rbase = curvature_tensor_at_origin(product_base_metric(y))
Rplus_base = curvature_operator_matrix(Rbase, omega_p)
Rminus_base = curvature_operator_matrix(Rbase, omega_m)

modes = []
for source_factor in [1, 2]:
    for target_factor in [1, 2]:
        for sign in [+1, -1]:
            Gnorm, h0 = metric_for_mode(source_factor, target_factor, sign)
            R = curvature_tensor_at_origin(Gnorm)
            Rplus = curvature_operator_matrix(R, omega_p)
            dRplus = sp.simplify((Rplus - Rplus_base) / eps)
            dRplus = dRplus.applyfunc(lambda z: sp.simplify(z.subs(eps, 0)))
            # In adapted basis at phi0=omega2: (omega2, omega1, omega3).
            # D_v lambda_k = c < dR^+ phi0, phi_(k)>.
            # Original Rplus matrix indices (omega1,omega2,omega3).
            dR_col_phi0 = dRplus[:, 1]
            adapted = [dR_col_phi0[1], dR_col_phi0[0], dR_col_phi0[2]]
            modes.append({
                "mode": f"u{source_factor}_g{target_factor}",
                "pole_sign_source": sign,
                "h0_diag": [str(h0[i, i]) for i in range(4)],
                "dRplus_original_basis": [[str(sp.simplify(dRplus[i, j])) for j in range(3)] for i in range(3)],
                "D_v_lambda_adapted_phi0_omega2_up_to_c": [str(sp.simplify(x)) for x in adapted],
            })

# Also compute image rank over these modes at a fixed sign pair NN (both source signs +).
# At a given node, u1 sign and u2 sign are independent pole signs; for NN both +.
cols_NN = []
labels_NN = []
for m in modes:
    if m["pole_sign_source"] == 1:
        labels_NN.append(m["mode"])
        cols_NN.append(sp.Matrix([sp.sympify(s) for s in m["D_v_lambda_adapted_phi0_omega2_up_to_c"]]))
Mat_NN = sp.Matrix.hstack(*cols_NN)

results = {
    "step": 79,
    "purpose": "pilot local image of scalar full-kernel modes on D_v lambda",
    "method": "quadratic normal-coordinate expansion of product S^2(1)xS^2(1), plus linear normalization of constant metric perturbation",
    "calibration": {
        "Rplus_base": [[str(sp.simplify(Rplus_base[i,j])) for j in range(3)] for i in range(3)],
        "Rminus_base": [[str(sp.simplify(Rminus_base[i,j])) for j in range(3)] for i in range(3)],
        "expected": "diag(1,0,0) for both blocks in the Step 76/78 convention",
    },
    "modes": modes,
    "NN_image_matrix_columns_u1g1_u1g2_u2g1_u2g2": [[str(sp.simplify(Mat_NN[i,j])) for j in range(Mat_NN.shape[1])] for i in range(Mat_NN.shape[0])],
    "NN_rank": int(Mat_NN.rank()),
    "interpretation": "This is only the local curvature-block contribution to D_v lambda; it does not prove these modes are admissible Einstein deformation variables in the chosen slice. It tests whether D_v could add k=3 image directions.",
}

print(json.dumps(results, indent=2))
out = "Sessions/S0910A01/workspace/data/step79_scalar_kernel_Dv_lambda.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"Wrote {out}")
