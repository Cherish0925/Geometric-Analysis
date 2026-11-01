"""
Step 57b: general-background quadratic form for the kernel-direction eps^2 log(1/eps) Burns coefficient.

Curvature parametrisation (orientation dx1 dy1 dx2 dy2, zeta = (e12+e34)/sqrt2 = Kahler form of the Burns J):
  curvature operator on Lambda^2 = Lambda^+ (+) Lambda^-  :  [[W+ + s/12, Bk], [Bk^T, W- + s/12]]
  R_abcd = sum R_IJ w^I_ab w^J_cd  (convention R_1212 = sectional curvature).
Background jet B_R = -(1/3) R_iajb x^a x^b (normal-coordinate quadratic part) and an independent quartic part C.
Outputs (workspace/data/step57_general_form_D{D}.json):
  M_eff (20x20 quadratic form after optimal K), the invariant fit, ell on quartic jets and its factorisation
  through nabla^2 Rm(0), N(R) = nabla^2 Rm(0) of delta+B_R, and the CH test.
usage: python step57_general_form.py D nu_pts nphi
"""
import sys, os, json, time, itertools
import numpy as np
import jax, jax.numpy as jnp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step57_kernel_log_coefficient import *

D = int(sys.argv[1]) if len(sys.argv) > 1 else 2
nu_pts = int(sys.argv[2]) if len(sys.argv) > 2 else 6
nphi = int(sys.argv[3]) if len(sys.argv) > 3 else 16
DO_ELL = (sys.argv[4] == 'ell') if len(sys.argv) > 4 else False
DENS = os.environ.get('STEP57_DENSITY', 'ric')  # 'ric' = |Ric°|^2 dmu ; 'fplus' = (4|W+|^2 + s^2/12) dmu (code check)
if DENS == 'fplus':
    import step57_kernel_log_coefficient as K57
    K57.density_from_jet = K57.density_Fplus_from_jet
    density_from_jet = K57.density_Fplus_from_jet
OUTF = os.path.join(HERE, '..', 'data', 'step57_general_form_D%d_q%d_%d%s.json' % (D, nu_pts, nphi, '' if DENS == 'ric' else '_' + DENS))
E8 = 8 * np.pi ** 2
t0 = time.time()

# ---------- Lambda^2 bases ----------
def e2(a, b):
    m = np.zeros((4, 4)); m[a, b] = 1; m[b, a] = -1; return m
s2 = 1 / np.sqrt(2)
Lp = [s2 * (e2(0, 1) + e2(2, 3)), s2 * (e2(0, 2) - e2(1, 3)), s2 * (e2(0, 3) + e2(1, 2))]
Lm = [s2 * (e2(0, 1) - e2(2, 3)), s2 * (e2(0, 2) + e2(1, 3)), s2 * (e2(0, 3) - e2(1, 2))]
L2 = Lp + Lm
assert np.allclose(Lp[0], np.array(kahler_form(Jz)) * s2) or np.allclose(Lp[0], -np.array(kahler_form(Jz)) * s2)

def tl_basis():
    b = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        m = np.zeros((3, 3)); m[i, j] = m[j, i] = s2; b.append(m)
    b.append(np.diag([1, -1, 0]) * s2)
    b.append(np.diag([1, 1, -2]) / np.sqrt(6))
    return b
TL = tl_basis()
# component labels: 0:s, 1-5:W+, 6-10:W-, 11-19:Bk (row-major, row = Lambda^+ index)
def operator_from_params(t):
    t = np.asarray(t, float)
    s = t[0]
    Wp = sum(t[1 + i] * TL[i] for i in range(5)); Wm = sum(t[6 + i] * TL[i] for i in range(5))
    Bk = t[11:20].reshape(3, 3)
    Rop = np.zeros((6, 6))
    Rop[:3, :3] = Wp + s / 12 * np.eye(3); Rop[3:, 3:] = Wm + s / 12 * np.eye(3)
    Rop[:3, 3:] = Bk; Rop[3:, :3] = Bk.T
    return Rop
def riemann_from_operator(Rop):
    W = np.array(L2)
    return np.einsum('IJ,Iab,Jcd->abcd', Rop, W, W)

def B_field(Rabcd):
    R = jnp.array(Rabcd)
    def B(x):
        return -(1. / 3.) * jnp.einsum('iajb,a,b->ij', R, x, x)
    return B

# ---------- Riemann & covariant derivatives of a metric field ----------
def christoffel_fn(gf):
    def Gam(x):
        g, dg, _ = jet(gf, x)
        gi = jnp.linalg.inv(g)
        t = jnp.einsum('jli->lij', dg) + jnp.einsum('ilj->lij', dg) - jnp.einsum('ijl->lij', dg)
        return 0.5 * jnp.einsum('kl,lij->kij', gi, t)
    return Gam
def riem_fn(gf):
    Gam = christoffel_fn(gf)
    def Rm(x):
        G = Gam(x); dG = jax.jacfwd(Gam)(x)  # dG[l,j,k,i] = d_i Gamma^l_jk
        Rup = (jnp.einsum('ljki->lijk', dG) - jnp.einsum('likj->lijk', dG)
               + jnp.einsum('lim,mjk->lijk', G, G) - jnp.einsum('ljm,mik->lijk', G, G))  # R^l_{ijk}
        g = gf(x)
        Rlow = jnp.einsum('lm,mijk->ijkl', g, Rup)  # g(R(e_i,e_j)e_k, e_l)
        return -Rlow  # convention R_1212 = +K
    return Rm
def nabla2_riem_at0(gf):
    Rm = riem_fn(gf); Gam = christoffel_fn(gf)
    def nR(x):
        R = Rm(x); dR = jax.jacfwd(Rm)(x)  # dR[i,j,k,l,n]
        G = Gam(x)
        out = jnp.einsum('ijkln->nijkl', dR)
        out = out - jnp.einsum('pni,pjkl->nijkl', G, R) - jnp.einsum('pnj,ipkl->nijkl', G, R) \
                  - jnp.einsum('pnk,ijpl->nijkl', G, R) - jnp.einsum('pnl,ijkp->nijkl', G, R)
        return out
    return jnp.einsum('nijklm->mnijkl', jax.jacfwd(nR)(jnp.zeros(4)))  # Gamma(0)=0 assumed

# ---------- checks of conventions ----------
Rid = riemann_from_operator(np.eye(6))
gS = lambda x: jnp.eye(4) + B_field(Rid)(x)
Rc = np.array(riem_fn(gS)(jnp.zeros(4)))
assert np.allclose(Rc, Rid, atol=1e-10), 'convention mismatch'
dens0, Ric0, s0 = density_from_jet(*jet(gS, jnp.zeros(4)))
print('sphere check: s =', float(s0), ' (expect 12)')

# ---------- quadrature, K jets, Q ----------
X, W = s3_quadrature(nu_pts, nphi)
basis = make_K_basis(D); Kf = [K_field(E, m, D) for E, m in basis]
def kstack(x):
    return (jnp.stack([K(x) for K in Kf]), jnp.stack([jax.jacfwd(K)(x) for K in Kf]),
            jnp.stack([jax.jacfwd(jax.jacfwd(K))(x) for K in Kf]))
KJ = jax.jit(jax.vmap(kstack))(X)
rl = jax.jit(jax.vmap(jax.vmap(lambda a, b, c: ric_lin_flat((a, b, c)))))
LK = rl(*KJ)
Q = np.array(jnp.einsum('p,pkij,plij->kl', W, LK, LK)) / E8
print('K basis', len(Kf), 'points', X.shape[0], 't', time.time() - t0)

Afun = tail_A()
AJ = jax.jit(jax.vmap(lambda x: jet(Afun, x)))(X)

def bvec(Bf):
    BJ = jax.vmap(lambda x: jet(Bf, x))(X)
    G = jax.jit(jax.vmap(grad_ABK_point))(AJ, BJ)
    bb = (jnp.einsum('pij,pkij->pk', G[0], KJ[0]) + jnp.einsum('pijm,pkijm->pk', G[1], KJ[1])
          + jnp.einsum('pijmn,pkijmn->pk', G[2], KJ[2]))
    return np.array(jnp.einsum('p,pk->k', W, bb)) / E8, BJ

def pair_point(Aj, B1, B2):
    def F(a, b1, b2):
        return density_from_jet(*add((1., DELTA), (a, Aj), (b1, B1), (b2, B2)))[0]
    return 0.25 * jax.grad(jax.grad(jax.grad(jax.grad(F, 0), 0), 1), 2)(0., 0., 0.)
pairv = jax.jit(jax.vmap(pair_point))
def AAC_point(Aj, Cj):
    def F(a, c):
        return density_from_jet(*add((1., DELTA), (a, Aj), (c, Cj)))[0]
    return 0.5 * jax.grad(jax.grad(jax.grad(F, 0), 0), 1)(0., 0.)
aacv = jax.jit(jax.vmap(AAC_point))

# ---------- curvature basis: 20 directions ----------
NB = 20
Rbas = [riemann_from_operator(operator_from_params(np.eye(NB)[a])) for a in range(NB)]
bs, BJs = [], []
for a in range(NB):
    b, BJ = bvec(B_field(Rbas[a])); bs.append(b); BJs.append(BJ)
bs = np.array(bs)  # (20, nK)
M = np.zeros((NB, NB))
for a in range(NB):
    for c in range(a, NB):
        v = float(jnp.sum(W * pairv(AJ, BJs[a], BJs[c]))) / E8
        # pair_point gives c(B1,B2) bilinear with c(B,B)=coefficient; M symmetric
        M[a, c] = M[c, a] = v
print('M built t', time.time() - t0)
wq, Vq = np.linalg.eigh(Q)
big = wq > 1e-9 * wq.max()
Qp = Vq[:, big] @ np.diag(1 / wq[big]) @ Vq[:, big].T
leak = np.linalg.norm((Vq[:, ~big].T @ bs.T))
Meff = M - 0.25 * bs @ Qp @ bs.T
Meff = 0.5 * (Meff + Meff.T)
print('kernel leak of b vectors', leak)
leak_dir = np.linalg.norm(Vq[:, ~big].T @ bs.T, axis=0)
print('leak per curvature direction', np.round(leak_dir, 6))
print('Q eigenvalues (smallest 30)', np.round(wq[:30], 10))
if not DO_ELL:
    tCHs = np.array([-24., 0, 0, 0, 4.242640687119285, -2.449489742783178] + [0.] * 14)
    print('Phi_CH (normal-coordinate B, ell=0 from D2 run)', float(tCHs @ Meff @ tCHs))
    out = dict(D=D, nu_pts=nu_pts, nphi=nphi, nK=len(Kf), leak=float(leak), leak_dir=leak_dir.tolist(),
               Meff=Meff.tolist(), M=M.tolist(), Qeig=wq.tolist(), Phi_CH=float(tCHs @ Meff @ tCHs),
               labels=['s'] + ['W+%d' % i for i in range(5)] + ['W-%d' % i for i in range(5)] +
                      ['Bk%d%d' % (i, j) for i in range(3) for j in range(3)])
    json.dump(out, open(OUTF, 'w'))
    print('saved', OUTF, 't', time.time() - t0)
    sys.exit(0)

# ---------- quartic jets: ell(C) and nabla^2Rm map ----------
monos4 = monomials(4)
Cbasis = []
for (i, j) in SYM:
    E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1
    for m in monos4:
        Cbasis.append((E, m))
def C_field(E, m):
    E = jnp.array(E); m = [int(v) for v in m]
    def C(x):
        mon = 1.0
        for i in range(4):
            if m[i] > 0:
                mon = mon * x[i] ** m[i]
        return E * mon
    return C
ell = np.zeros(len(Cbasis)); Lmap = []
for n, (E, m) in enumerate(Cbasis):
    Cf = C_field(E, m)
    CJ = jax.vmap(lambda x: jet(Cf, x))(X)
    ell[n] = float(jnp.sum(W * aacv(AJ, CJ))) / E8
    gC = lambda x, Cf=Cf: jnp.eye(4) + Cf(x)
    Lmap.append(np.array(nabla2_riem_at0(gC)).ravel())
Lmap = np.array(Lmap)  # (350, 4096)
# factorisation ell = Lmap @ lhat ?
lhat, res, rk, sv = np.linalg.lstsq(Lmap, ell, rcond=None)
fact_res = float(np.linalg.norm(Lmap @ lhat - ell) / max(np.linalg.norm(ell), 1e-300))
print('ell norm', np.linalg.norm(ell), 'factorisation residual', fact_res, 'rank L', rk, 't', time.time() - t0)

# N(R): nabla^2 Rm(0) of delta + B_R, quadratic in R -> evaluate for basis pairs via polarisation
def N_of(Rabcd):
    gB = lambda x: jnp.eye(4) + B_field(Rabcd)(x)
    return np.array(nabla2_riem_at0(gB)).ravel()
# ell-hat applied to N(R) is a quadratic form in t
Nq = np.zeros((NB, NB))
Nd = [float(N_of(Rbas[a]) @ lhat) for a in range(NB)]
for a in range(NB):
    Nq[a, a] = Nd[a]
    for c in range(a + 1, NB):
        v = float(N_of(Rbas[a] + Rbas[c]) @ lhat)
        Nq[a, c] = Nq[c, a] = 0.5 * (v - Nd[a] - Nd[c])
print('N built t', time.time() - t0)
# geometric form:  Phi(R, nabla^2Rm) = t^T (Meff - Nq) t + lhat . nabla^2Rm
Mgeo = Meff - Nq

# ---------- CH test ----------
Bf = ddbar_metric(lambda y: 0.5 * jnp.dot(y, y) ** 2, J2)
gCH = ddbar_metric(lambda y: -jnp.log(1 - jnp.dot(y, y)), J2)
RCH = np.array(riem_fn(gCH)(jnp.zeros(4)))
# params of RCH
Wm_ = np.array(L2)
Rop = np.einsum('abcd,Iab,Jcd->IJ', RCH, Wm_, Wm_) / 4.0
tCH = np.linalg.lstsq(np.array([operator_from_params(np.eye(NB)[a]).ravel() for a in range(NB)]).T,
                      Rop.ravel(), rcond=None)[0]
nab2CH = np.array(nabla2_riem_at0(gCH)).ravel()
Phi_CH = float(tCH @ Mgeo @ tCH + lhat @ nab2CH)
print('CH params', np.round(tCH, 6), '|nabla2Rm_CH|', np.linalg.norm(nab2CH), 'Phi_CH', Phi_CH)

out = dict(D=D, nu_pts=nu_pts, nphi=nphi, nK=len(Kf), leak=float(leak), Meff=Meff.tolist(), Nq=Nq.tolist(),
           Mgeo=Mgeo.tolist(), ell_fact_residual=fact_res, lhat=lhat.tolist(), Phi_CH=Phi_CH, tCH=tCH.tolist(),
           labels=['s'] + ['W+%d' % i for i in range(5)] + ['W-%d' % i for i in range(5)] +
                  ['Bk%d%d' % (i, j) for i in range(3) for j in range(3)])
json.dump(out, open(OUTF, 'w'))
np.save(OUTF.replace('.json', '_Lmap.npy'), Lmap)
np.save(OUTF.replace('.json', '_ell.npy'), ell)
print('saved', OUTF, 't', time.time() - t0)
