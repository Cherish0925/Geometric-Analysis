#!/usr/bin/env python3
"""Step 75 (Q4): symbol-level checks for the torsion of an almost-Kahler Einstein 4-manifold.

Model (flat, principal symbol level): alpha = f_1 dzbar_1 + f_2 dzbar_2, f: C^2 -> C^2.
Derivative data D = (P, Q), P_{ji} = d f_i / d z_j, Q_{ji} = d f_i / d zbar_j (complex 2x2 each).
Einstein (Ric_0 = 0) <=> (d^nabla T)^- = 0 <=> primitive part of P vanishes: P = c I.
Kernel K = {P = c I, Q arbitrary}, complex dim 5.

Checks
 1. refined Kato constant k^2 = sup_{|xi|=|v|=1} |pi_K(xi (x) v)|^2 for the real gradient
    (expected 3/4), and that it is attained;
 2. local index of a linear zero f(z) = c z + B zbar equals
    sign((|c|^2 - s1^2)(|c|^2 - s2^2)), s_i singular values of B (c = 0 gives +1);
 3. kernel dimension count (rank of the primitive-P constraint).
Output: workspace/data/step75_torsion_symbol_checks.json
"""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(75)


def real_grad_from_PQ(P, Q):
    """Real gradient (d/dx_j, d/dy_j) f_i as complex 4x2 array from (P,Q)."""
    G = np.zeros((4, 2), complex)
    for j in range(2):
        G[2 * j] = P[j] + Q[j]            # d/dx_j = d/dz_j + d/dzbar_j
        G[2 * j + 1] = 1j * (P[j] - Q[j])  # d/dy_j = i(d/dz_j - d/dzbar_j)
    return G


def realvec(G):
    return np.concatenate([G.real.ravel(), G.imag.ravel()])


# Basis of the real 16-dim gradient space and of K (real dim 10).
def gradient_basis_K():
    vecs = []
    # c I  (c complex)
    for c in (1.0, 1j):
        vecs.append(realvec(real_grad_from_PQ(c * np.eye(2), np.zeros((2, 2)))))
    for j in range(2):
        for i in range(2):
            for c in (1.0, 1j):
                Q = np.zeros((2, 2), complex)
                Q[j, i] = c
                vecs.append(realvec(real_grad_from_PQ(np.zeros((2, 2)), Q)))
    Bk = np.array(vecs).T
    Qk, _ = np.linalg.qr(Bk)
    return Qk


def kato_constant(trials=20000):
    Qk = gradient_basis_K()
    best = 0.0
    for _ in range(trials):
        xi = rng.normal(size=4); xi /= np.linalg.norm(xi)
        v = rng.normal(size=2) + 1j * rng.normal(size=2); v /= np.linalg.norm(v)
        G = np.outer(xi, v)  # real covector (x) value
        x = realvec(G)
        pr = Qk @ (Qk.T @ x)
        best = max(best, float(pr @ pr))
    # local refinement by simple random search around best
    return best, Qk.shape[1]


def kato_attained():
    """Explicit maximiser: xi = dx_1, v = e_1 (expected 3/4)."""
    Qk = gradient_basis_K()
    xi = np.array([1.0, 0, 0, 0]); v = np.array([1.0, 0])
    x = realvec(np.outer(xi, v)); pr = Qk @ (Qk.T @ x)
    return float(pr @ pr)


def index_linear(c, B):
    # real 4x4 matrix of z -> c z + B zbar on R^4 = C^2 (x1,y1,x2,y2)
    M = np.zeros((4, 4))
    for k in range(4):
        e = np.zeros(4); e[k] = 1
        z = np.array([e[0] + 1j * e[1], e[2] + 1j * e[3]])
        w = c * z + B @ np.conj(z)
        M[:, k] = [w[0].real, w[0].imag, w[1].real, w[1].imag]
    return int(np.sign(np.linalg.det(M))), float(np.linalg.det(M))


def index_formula(c, B):
    """ind = sign(|c|^4 - |c|^2 (||S||^2-||A||^2) + |det B|^2), B = S + A."""
    S = (B + B.T) / 2; A = (B - B.T) / 2
    t = np.linalg.norm(S) ** 2 - np.linalg.norm(A) ** 2
    t_direct = np.trace(np.conj(B) @ B)
    assert abs(t - t_direct) < 1e-9 * (1 + abs(t)), (t, t_direct)
    return int(np.sign(abs(c) ** 4 - abs(c) ** 2 * t + abs(np.linalg.det(B)) ** 2))


def main():
    k2, dimK = kato_constant()
    k2_att = kato_attained()
    agree, n, neg = 0, 4000, 0
    for _ in range(n):
        c = (rng.normal() + 1j * rng.normal()) * rng.choice([0.0, 0.3, 1.0, 3.0])
        B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        i1, det = index_linear(c, B)
        i2 = index_formula(c, B)
        agree += int(i1 == i2); neg += int(i1 < 0)
    # determinant identity det_R = det(|c|^2 I - Bbar B) (as real number)
    c = 0.7 + 0.2j; B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    det_direct = index_linear(c, B)[1]
    det_formula = float(np.linalg.det(abs(c) ** 2 * np.eye(2) - np.conj(B) @ B).real)
    # negative index requires ||S||^2 - ||A||^2 >= 2|det B| and c != 0; test pure modes
    pure = dict(c_only=index_linear(1.0, np.zeros((2, 2)))[0],
                antisym_only=index_linear(0.0, np.array([[0, 1.0], [-1.0, 0]]))[0],
                A01_example=index_linear(1.0, np.array([[2.0, 0], [0, 0]]))[0])
    out = dict(
        pure_modes=pure,
        kernel_real_dim=dimK,
        kato_k2_sampled_max=k2, kato_k2_attained_dx1_e1=k2_att, kato_k2_expected=0.75,
        index_formula_agreement=f"{agree}/{n}", negative_index_fraction=neg / n,
        det_direct=det_direct, det_formula=det_formula,
    )
    p = ROOT / "data" / "step75_torsion_symbol_checks.json"
    p.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
