"""ITEM E (general case): the Gaussian-coordinate Ricci formulas are algebraic identities in the
2-jet of q at a point.  Test them on RANDOM 2-jets (fully non-diagonal q depending on r and on all
three slice coordinates) using exact jet arithmetic in numpy (no finite differences).
"""
import numpy as np

rng = np.random.default_rng(12345)


def ricci_from_jets(g, dg, ddg):
    """g[a,b], dg[c,a,b]=d_c g_ab, ddg[c,d,a,b]=d_c d_d g_ab  ->  Ricci, Christoffel."""
    n = g.shape[0]
    gi = np.linalg.inv(g)
    dgi = -np.einsum('ab,cbd,de->cae', gi, dg, gi)            # d_c g^{ae}
    # B[l? no]  lower-index Christoffel: C[m,i,j] = 1/2 (d_j g_mi + d_i g_mj - d_m g_ij)
    C = 0.5 * (np.einsum('jmi->mij', dg) + np.einsum('imj->mij', dg) - dg)
    dC = 0.5 * (np.einsum('kjmi->kmij', ddg) + np.einsum('kimj->kmij', ddg) - ddg)   # d_k C[m,i,j]
    Gam = np.einsum('lm,mij->lij', gi, C)
    dGam = np.einsum('klm,mij->klij', dgi, C) + np.einsum('lm,kmij->klij', gi, dC)    # d_k Gam^l_ij
    Ric = (np.einsum('llik->ik', dGam) - np.einsum('klil->ik', dGam)
           + np.einsum('llm,mik->ik', Gam, Gam) - np.einsum('lkm,mil->ik', Gam, Gam))
    return Ric, Gam


def random_jets(n_slice=3):
    n = n_slice + 1
    A = rng.normal(size=(n_slice, n_slice))
    q = A @ A.T + n_slice * np.eye(n_slice)
    g = np.zeros((n, n)); g[0, 0] = 1; g[1:, 1:] = q
    dg = np.zeros((n, n, n)); ddg = np.zeros((n, n, n, n))
    for c in range(n):
        M = rng.normal(size=(n_slice, n_slice)); dg[c, 1:, 1:] = M + M.T
        for d in range(c, n):
            M = rng.normal(size=(n_slice, n_slice)); M = M + M.T
            ddg[c, d, 1:, 1:] = M; ddg[d, c, 1:, 1:] = M
    return g, dg, ddg


worst = 0.0
for trial in range(200):
    g, dg, ddg = random_jets()
    Ric4, _ = ricci_from_jets(g, dg, ddg)
    q = g[1:, 1:]; qi = np.linalg.inv(q)
    # slice Ricci from tangential jets only
    Ricq, Gq = ricci_from_jets(q, dg[1:, 1:, 1:], ddg[1:, 1:, 1:, 1:])
    K = 0.5 * dg[0, 1:, 1:]
    Kr = 0.5 * ddg[0, 0, 1:, 1:]
    dK = 0.5 * ddg[1:, 0, 1:, 1:]                               # d_j K_ki
    S = qi @ K; H = np.trace(S)
    dqi = -np.einsum('ab,cbd,de->cae', qi, dg[1:, 1:, 1:], qi)   # tangential derivative of q^{-1}
    dH = np.einsum('iab,ab->i', dqi, K) + np.einsum('ab,iab->i', qi, dK)
    nabK = dK - np.einsum('mjk,mi->jki', Gq, K) - np.einsum('mji,km->jki', Gq, K)
    divK = np.einsum('jk,jki->i', qi, nabK)
    Rrr = -np.trace(qi @ Kr) + np.trace(S @ S)
    Rri = divK - dH
    Rij = Ricq - Kr - H * K + 2 * K @ qi @ K
    err = max(abs(Ric4[0, 0] - Rrr), np.abs(Ric4[0, 1:] - Rri).max(), np.abs(Ric4[1:, 1:] - Rij).max())
    # constraint
    E = Ric4 + 3 * g
    Rq = np.trace(qi @ Ricq)
    cons = -6 + H**2 - np.trace(S @ S) + np.trace(qi @ E[1:, 1:]) - E[0, 0] - Rq
    # S_r evolution  S_r = q^{-1}K_r - 2 S^2
    Sr = qi @ Kr - 2 * S @ S
    evo = qi @ Ricq + 3 * np.eye(3) - H * S - qi @ E[1:, 1:] - Sr
    err = max(err, abs(cons), np.abs(evo).max())
    worst = max(worst, err / (1 + np.abs(Ric4).max()))
print("random 2-jets, 200 trials: worst relative discrepancy of")
print("  Ric_rr, Ric_ri, Ric_ij (eq:fullRic), S_r evolution, Hamiltonian constraint =", worst)

# sanity check of the jet-Ricci routine itself: hyperbolic metric dr^2 + e^{2r} delta  =>  Ric = -3 g at r=0
n = 4
g = np.eye(n); dg = np.zeros((n, n, n)); ddg = np.zeros((n, n, n, n))
dg[0, 1:, 1:] = 2 * np.eye(3); ddg[0, 0, 1:, 1:] = 4 * np.eye(3)
print("sanity (hyperbolic cusp): Ric =", np.round(np.diag(ricci_from_jets(g, dg, ddg)[0]), 12))
