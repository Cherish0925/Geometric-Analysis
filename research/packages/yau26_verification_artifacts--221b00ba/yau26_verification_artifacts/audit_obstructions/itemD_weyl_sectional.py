"""ITEM D: which norm of W makes  K(Pi) <= -1/3 + delta + |W|/sqrt3  true?
Build random algebraic curvature tensors in dimension 4 with Ric = -g + eta, ||eta||_op <= delta,
random Weyl part, and compare max sectional curvature with the three candidate norms:
  |W|_HS  (Hilbert-Schmidt norm of W acting on Lambda^2; |W|^2 = (1/4) W_ijkl W^ijkl  -- the CGB norm),
  |W|_full = 2 |W|_HS,   ||W||_spec = spectral norm of W on Lambda^2.
"""
import itertools
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(5)
n = 4
I4 = np.eye(n)


def KN(h, k):
    return (np.einsum('ik,jl->ijkl', h, k) + np.einsum('jl,ik->ijkl', h, k)
            - np.einsum('il,jk->ijkl', h, k) - np.einsum('jk,il->ijkl', h, k))


def weyl_part(R):
    Ric = np.einsum('ijkj->ik', R)          # with K(e1,e2)=R_1212 convention, Ric_ik = R_ijkj
    s = np.trace(Ric)
    E = Ric - s / 4 * I4
    return R - 0.5 * KN(E, I4) - s / 24 * KN(I4, I4), Ric


pairs = list(itertools.combinations(range(n), 2))


def op_on_2forms(W):
    return np.array([[W[a, b, c, d] for (c, d) in pairs] for (a, b) in pairs])


def sec(R, u, v):
    return np.einsum('ijkl,i,j,k,l->', R, u, v, u, v)


def max_sec(R, tries=40):
    best = -1e9

    def f(p):
        A = p.reshape(2, 4)
        q, _ = np.linalg.qr(A.T)
        return -sec(R, q[:, 0], q[:, 1])
    for _ in range(tries):
        res = minimize(f, rng.normal(size=8), method='BFGS')
        best = max(best, -res.fun)
    return best


viol = {'HS': 0, 'spec': 0}
ratios = []
for trial in range(60):
    # random Weyl tensor
    R0 = sum(KN(*(lambda a, b: (a + a.T, b + b.T))(rng.normal(size=(4, 4)), rng.normal(size=(4, 4)))) for _ in range(4))
    W, _ = weyl_part(R0)
    W *= rng.uniform(0.1, 3.0) / np.sqrt(np.sum(W**2))
    assert np.abs(np.einsum('ijkj->ik', W)).max() < 1e-12
    delta = rng.uniform(0, 0.33)
    Q, _ = np.linalg.qr(rng.normal(size=(4, 4)))
    eta = Q @ np.diag(rng.uniform(-delta, delta, 4)) @ Q.T
    if trial % 2 == 0:                       # extremal eta: two +delta, two -delta
        eta = Q @ np.diag([delta, delta, -delta, -delta]) @ Q.T
    Ric = -I4 + eta; s = np.trace(Ric); E = Ric - s / 4 * I4
    R = W + 0.5 * KN(E, I4) + s / 24 * KN(I4, I4)
    assert np.abs(np.einsum('ijkj->ik', R) - Ric).max() < 1e-12
    Kmax = max_sec(R)
    Wop = op_on_2forms(W)
    HS = np.sqrt(np.sum(Wop**2)); full = np.sqrt(np.sum(W**2)); spec = np.abs(np.linalg.eigvalsh(Wop)).max()
    assert abs(full - 2 * HS) < 1e-10
    if Kmax > -1 / 3 + delta + HS / np.sqrt(3) + 1e-9:
        viol['HS'] += 1
    if Kmax > -1 / 3 + delta + spec / np.sqrt(3) + 1e-9:
        viol['spec'] += 1
    ratios.append((Kmax + 1 / 3 - delta) / (HS / np.sqrt(3)))
print("violations with |W| = HS norm on Lambda^2 :", viol['HS'], "/ 60")
print("violations with |W| = spectral norm       :", viol['spec'], "/ 60   (inequality FALSE for the spectral norm)")
print("max of (Kmax+1/3-delta)/(|W|_HS/sqrt3) over random samples:", max(ratios))

# sharpness of the constant 1/sqrt3 for the HS norm: Weyl tensor of S^2 x S^2 type, W^+ = W^- = diag(2a,-a,-a), a>0
P1 = np.diag([1.0, 1, 0, 0]); P2 = np.diag([0.0, 0, 1, 1])
Rprod = 0.5 * KN(P1, P1) + 0.5 * KN(P2, P2)             # S^2(1) x S^2(1)
Wp, Ricp = weyl_part(Rprod)
Wop = op_on_2forms(Wp)
HS = np.sqrt(np.sum(Wop**2))
print("S^2xS^2-type Weyl tensor: |W|_HS =", HS, "; max Weyl sectional value =",
      max(sec(Wp, I4[i], I4[j]) for i, j in pairs), " ; |W|_HS/sqrt3 =", HS / np.sqrt(3), " (equality => constant sharp)")
# H^2 x H^2 with Ric = -g (not an equality case: top Weyl eigenvalue is +1/3, |W|_HS = 2/sqrt3)
Rh = -0.5 * KN(P1, P1) - 0.5 * KN(P2, P2)
Wh, _ = weyl_part(Rh)
print("H^2xH^2 (Ric=-g): max K =", max(sec(Rh, I4[i], I4[j]) for i, j in pairs),
      "<= -1/3 + |W|_HS/sqrt3 =", -1 / 3 + np.sqrt(np.sum(op_on_2forms(Wh)**2)) / np.sqrt(3))
