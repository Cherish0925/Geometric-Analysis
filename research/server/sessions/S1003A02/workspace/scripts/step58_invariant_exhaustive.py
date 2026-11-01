"""
Step 58: exhaustive angular minimisation in the (s, W+) sector.

For curvature with only s and W+ components, the normal-coordinate quadratic jet B_R is invariant under SU(2)_-
(which acts trivially on Lambda^+), and so is the Burns tail A.  Averaging a corrector K over SU(2)_- keeps the
linear term b(K) and does not increase Q(K) = |Ric_lin K|^2 (convexity).  SU(2)_- acts simply transitively on S^3,
so SU(2)_- invariant degree-0 symmetric 2-tensors form the 10-dim space Sym^2 span{dr, s1, s2, s3}.
Minimising over that space is therefore the exact optimum over ALL degree-0 correctors (all angular modes),
with no polynomial truncation D.

Output: workspace/data/step58_invariant_exhaustive.json : 6x6 form M_eff on (s, W+_0..W+_4) and the invariant fit.
"""
import sys, os, json, time
import numpy as np
import jax, jax.numpy as jnp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step57_kernel_log_coefficient import *

nu_pts = int(sys.argv[1]) if len(sys.argv) > 1 else 8
nphi = int(sys.argv[2]) if len(sys.argv) > 2 else 24
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step58_invariant_exhaustive.json')
E8 = 8 * np.pi ** 2
t0 = time.time()

def e2(a, b):
    m = np.zeros((4, 4)); m[a, b] = 1; m[b, a] = -1; return m
s2 = 1 / np.sqrt(2)
Lp = [s2 * (e2(0, 1) + e2(2, 3)), s2 * (e2(0, 2) - e2(1, 3)), s2 * (e2(0, 3) + e2(1, 2))]
Lm = [s2 * (e2(0, 1) - e2(2, 3)), s2 * (e2(0, 2) + e2(1, 3)), s2 * (e2(0, 3) - e2(1, 2))]
L2 = Lp + Lm
TL = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    m = np.zeros((3, 3)); m[i, j] = m[j, i] = s2; TL.append(m)
TL.append(np.diag([1, -1, 0]) * s2); TL.append(np.diag([1, 1, -2]) / np.sqrt(6))
def riem(t):
    s = t[0]; Wp = sum(t[1 + i] * TL[i] for i in range(5))
    Rop = np.zeros((6, 6)); Rop[:3, :3] = Wp + s / 12 * np.eye(3); Rop[3:, 3:] = s / 12 * np.eye(3)
    W = np.array(L2)
    return np.einsum('IJ,Iab,Jcd->abcd', Rop, W, W)
def B_field(R):
    R = jnp.array(R)
    return lambda x: -(1. / 3.) * jnp.einsum('iajb,a,b->ij', R, x, x)

X, W = s3_quadrature(nu_pts, nphi)
inv = invariant_K_basis(); fields = [K for _, K in inv]
NB = 6
zeroC = lambda x: jnp.zeros((4, 4))
# quadratic form via polarisation: c(B1+B2) etc.  run_background returns c_AABB(B,B)+c_AAC, b(B), Q
vals = {}
def run(t):
    c1, c2, b, Q = run_background(B_field(riem(t)), zeroC, X, W, fields, 'inv')
    return c1 / E8, b / E8, Q / E8
basis = np.eye(NB)
diag = [run(basis[a]) for a in range(NB)]
Q = diag[0][2]
M = np.zeros((NB, NB)); bs = np.array([d[1] for d in diag])
for a in range(NB):
    M[a, a] = diag[a][0]
    for c in range(a + 1, NB):
        v = run(basis[a] + basis[c])[0]
        M[a, c] = M[c, a] = 0.5 * (v - diag[a][0] - diag[c][0])
wq, Vq = np.linalg.eigh(Q)
big = wq > 1e-9 * wq.max()
Qp = Vq[:, big] @ np.diag(1 / wq[big]) @ Vq[:, big].T
leak_dir = np.linalg.norm(Vq[:, ~big].T @ bs.T, axis=0) if (~big).any() else np.zeros(NB)
Meff = M - 0.25 * bs @ Qp @ bs.T
Meff = 0.5 * (Meff + Meff.T)
print('Q rank', int(big.sum()), 'of', len(fields), 'leak per direction', np.round(leak_dir, 8))
# invariant fit: Phi = a s^2 + b s w + c w^2 + d |W_perpperp|^2 + e |W_zperp|^2, w = W+(zeta,zeta)
# W+ params: 0:(01) 1:(02) 2:(12) 3:diag(1,-1,0)/sqrt2 4:diag(1,1,-2)/sqrt6 ; zeta = index 0 of Lambda^+
rng = np.random.default_rng(0)
rows, ys = [], []
for _ in range(60):
    t = rng.normal(size=NB)
    Wp = sum(t[1 + i] * TL[i] for i in range(5))
    w = Wp[0, 0]; Wzp2 = 2 * (Wp[0, 1] ** 2 + Wp[0, 2] ** 2)
    blk = Wp[1:, 1:] - 0.5 * np.trace(Wp[1:, 1:]) * np.eye(2); Wpp2 = np.sum(blk * blk)
    rows.append([t[0] ** 2, t[0] * w, w ** 2, Wpp2, Wzp2]); ys.append(t @ Meff @ t)
co, res, _, _ = np.linalg.lstsq(np.array(rows), np.array(ys), rcond=None)
rel = float(np.linalg.norm(np.array(rows) @ co - ys) / np.linalg.norm(ys))
fit = dict(zip(['s2', 'sw', 'w2', 'Wpp', 'Wzp'], co.tolist()))
pred = dict(s2=1 / 288, sw=-1 / 24, w2=-1.0, Wpp=-1.0)
print('fit', {k: round(v, 12) for k, v in fit.items()}, 'rel res', rel)
print('prediction', pred)
# CH check
tCH = np.array([-24., 0, 0, 0, 0, 0]); tCH[1 + 4] = 0
# CH perp: W+ = diag(s/6,-s/12,-s/12) with Kahler form = Lambda^+ index 1 (perp to zeta): diag in (zeta, 1, 2) = (-s/12, s/6, -s/12)
Wd = np.diag([2.0, -4.0, 2.0])   # = diag(-s/12, s/6, -s/12) at s=-24
tch = np.zeros(NB); tch[0] = -24
A = np.array([TL[i].ravel() for i in range(5)]).T
tch[1:] = np.linalg.lstsq(A, Wd.ravel(), rcond=None)[0]
print('Phi_CH perp (exhaustive)', float(tch @ Meff @ tch))
json.dump(dict(nu=nu_pts, nphi=nphi, Meff=Meff.tolist(), M=M.tolist(), b=bs.tolist(), Qrank=int(big.sum()),
               leak_dir=leak_dir.tolist(), fit=fit, rel_res=rel, Phi_CH_perp=float(tch @ Meff @ tch),
               time=time.time() - t0), open(OUT, 'w'), indent=1)
print('saved', OUT, time.time() - t0)
