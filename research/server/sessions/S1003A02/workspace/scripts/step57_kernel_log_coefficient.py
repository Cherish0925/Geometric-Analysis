"""
Step 57: formal second-order (eps^2 log 1/eps) coefficient of a Burns insertion in a general background.

Setting.  Background g0 near p written as g0 = delta + nu*B + nu^2*C (+ odd/higher terms that cannot reach
the log order), Burns tail eps*A with A = ddbar(log r^2) for the constant complex structure J_zeta
(normalised so ddbar(|x|^2) = delta; then g_B = delta + eps*A is exactly the Burns metric, eps = Area(E)/pi),
and a free degree-0 correction eps*nu*K.  The neck density |Ric^o|^2 dmu has an eps^2 nu^2 r^{-4} part; its
S^3 integral divided by 8 pi^2 is the coefficient F with

      P/(8 pi^2) = ... + (F/2) eps^2 log(1/eps) + O(eps^2)     (F = F_P of the CH chapter; CH: F_min=-18).

F = c_AABB + c_AAC + c_ABK(K) + c_KK(K);  minimise over K (quadratic, Q_KK background independent).

Input/outputs: no input; writes workspace/data/step57_kernel_log_coefficient.json.
"""
import json, os, sys, itertools, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step57_kernel_log_coefficient.json')

# ---------------- complex structures ----------------
# coordinates x=(x1,y1,x2,y2), z1=x1+i y1, z2=x2+i y2 ; orientation dx1 dy1 dx2 dy2
Jz = jnp.array([[0., -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])  # J d/dx1 = d/dy1


def kahler_form(J):
    # omega(X,Y) = g(JX,Y) ; as matrix omega_ab = (J^T)_{ab}?  omega_ab = g(J e_a, e_b) = J_{ba}
    return J.T


def hodge_star_2form(w):
    eps = np.zeros((4, 4, 4, 4))
    for p in itertools.permutations(range(4)):
        sgn = np.linalg.det(np.eye(4)[list(p)])
        eps[p] = sgn
    return 0.5 * np.einsum('abcd,cd->ab', eps, w)


def sd_complex_structures():
    """three orthonormal SD complex structures (Kahler forms in Lambda^+)"""
    w1 = np.array(kahler_form(Jz))
    # candidates
    out = [w1]
    basis = []
    for (a, b) in itertools.combinations(range(4), 2):
        m = np.zeros((4, 4)); m[a, b] = 1; m[b, a] = -1; basis.append(m)
    sd = [0.5 * (m + hodge_star_2form(m)) for m in basis]
    # Gram-Schmidt in SD space
    for m in sd:
        v = m.copy()
        for u in out:
            v -= np.sum(v * u) / np.sum(u * u) * u
        if np.linalg.norm(v) > 1e-8:
            v = v / np.linalg.norm(v) * np.linalg.norm(w1)
            out.append(v)
        if len(out) == 3:
            break
    Js = [jnp.array(w.T) for w in out]  # J = omega^T
    for J in Js:
        assert np.allclose(np.array(J @ J), -np.eye(4)), 'not complex'
        assert np.allclose(np.array(J.T @ J), np.eye(4))
    return Js


J1, J2, J3 = sd_complex_structures()
assert np.allclose(np.array(J1), np.array(Jz))


def ddbar_metric(f, J):
    """Kahler metric of potential f for constant J, normalised so f=|x|^2 gives delta"""
    def g(x):
        H = jax.hessian(f)(x)
        return 0.25 * (H + J.T @ H @ J)
    return g


# ---------------- jets ----------------
def jet(T, x):
    return T(x), jax.jacfwd(T)(x), jax.jacfwd(jax.jacfwd(T))(x)


def density_from_jet(g, dg, ddg):
    gi = jnp.linalg.inv(g)
    # dg[i,j,k] = d_k g_ij ; ddg[i,j,k,l] = d_k d_l g_ij
    t = jnp.einsum('jli->lij', dg) + jnp.einsum('ilj->lij', dg) - jnp.einsum('ijl->lij', dg)
    Gam = 0.5 * jnp.einsum('kl,lij->kij', gi, t)
    dgi = -jnp.einsum('ka,abm,bl->klm', gi, dg, gi)
    dt = (jnp.einsum('jlim->lijm', ddg) + jnp.einsum('iljm->lijm', ddg) - jnp.einsum('ijlm->lijm', ddg))
    dGam = 0.5 * jnp.einsum('klm,lij->kijm', dgi, t) + 0.5 * jnp.einsum('kl,lijm->kijm', gi, dt)
    Ric = (jnp.einsum('kijk->ij', dGam) - jnp.einsum('kikj->ij', dGam)
           + jnp.einsum('kkl,lij->ij', Gam, Gam) - jnp.einsum('kjl,lik->ij', Gam, Gam))
    s = jnp.einsum('ij,ij->', gi, Ric)
    Ro = Ric - 0.25 * s * g
    n2 = jnp.einsum('ia,jb,ij,ab->', gi, gi, Ro, Ro)
    return n2 * jnp.sqrt(jnp.linalg.det(g)), Ric, s


def density_Fplus_from_jet(g, dg, ddg):
    """(4|W+|^2 + s^2/12) dmu ; differs from |Ric^o|^2 dmu by the Chern-Gauss-Bonnet/signature density
    (locally a divergence), so it must give the same eps^2 log coefficient for every K (code check)."""
    gi = jnp.linalg.inv(g)
    t = jnp.einsum('jli->lij', dg) + jnp.einsum('ilj->lij', dg) - jnp.einsum('ijl->lij', dg)
    Gam = 0.5 * jnp.einsum('kl,lij->kij', gi, t)
    dgi = -jnp.einsum('ka,abm,bl->klm', gi, dg, gi)
    dt = (jnp.einsum('jlim->lijm', ddg) + jnp.einsum('iljm->lijm', ddg) - jnp.einsum('ijlm->lijm', ddg))
    dGam = 0.5 * jnp.einsum('klm,lij->kijm', dgi, t) + 0.5 * jnp.einsum('kl,lijm->kijm', gi, dt)
    # R^l_{ijk} = d_i Gam^l_jk - d_j Gam^l_ik + Gam^l_im Gam^m_jk - Gam^l_jm Gam^m_ik ; dGam[l,j,k,i]
    Rup = (jnp.einsum('ljki->lijk', dGam) - jnp.einsum('likj->lijk', dGam)
           + jnp.einsum('lim,mjk->lijk', Gam, Gam) - jnp.einsum('ljm,mik->lijk', Gam, Gam))
    Rlow = -jnp.einsum('lm,mijk->ijkl', g, Rup)  # R_1212 = +K convention
    Ric = jnp.einsum('aiaj->ij', jnp.einsum('abcd->acbd', Rlow).transpose(0, 2, 1, 3)) if False else None
    # orthonormal coframe: g = L L^T, e_a = L^{-T} columns -> frame components R_abcd = R(e_a,..)
    L = jnp.linalg.cholesky(g)
    E = jnp.linalg.inv(L).T  # columns are orthonormal vectors
    Rf = jnp.einsum('ijkl,ia,jb,kc,ld->abcd', Rlow, E, E, E, E)
    s2_ = 1 / jnp.sqrt(2.)
    def e2(a, b):
        m = jnp.zeros((4, 4)).at[a, b].set(1.).at[b, a].set(-1.); return m
    Lp = jnp.stack([s2_ * (e2(0, 1) + e2(2, 3)), s2_ * (e2(0, 2) - e2(1, 3)), s2_ * (e2(0, 3) + e2(1, 2))])
    Rpp = 0.25 * jnp.einsum('abcd,Iab,Jcd->IJ', Rf, Lp, Lp)
    sc = jnp.einsum('abab->', Rf)
    Wp = Rpp - jnp.trace(Rpp) / 3 * jnp.eye(3)
    dens = (4 * jnp.sum(Wp * Wp) + sc ** 2 / 12) * jnp.sqrt(jnp.linalg.det(g))
    return dens, None, sc


def ricci_from_jet(g, dg, ddg):
    return density_from_jet(g, dg, ddg)[1]


DELTA = (jnp.eye(4), jnp.zeros((4, 4, 4)), jnp.zeros((4, 4, 4, 4)))


def add(*terms):
    out = [0, 0, 0]
    for c, jt in terms:
        for i in range(3):
            out[i] = out[i] + c * jt[i]
    return tuple(out)


# ---------------- quadrature on S^3 ----------------
def s3_quadrature(nu_pts=10, nphi=32):
    u, wu = np.polynomial.legendre.leggauss(nu_pts)
    u = 0.5 * (u + 1); wu = 0.5 * wu  # on [0,1]
    phi = 2 * np.pi * np.arange(nphi) / nphi; wphi = 2 * np.pi / nphi
    X, W = [], []
    for ui, wi in zip(u, wu):
        c, s = np.sqrt(1 - ui), np.sqrt(ui)
        for p1 in phi:
            for p2 in phi:
                X.append([c * np.cos(p1), c * np.sin(p1), s * np.cos(p2), s * np.sin(p2)])
                W.append(0.5 * wi * wphi * wphi)
    return jnp.array(X), jnp.array(W)


# ---------------- pointwise multilinear coefficients ----------------
def coeffs_point(Aj, Bj, Cj):
    def F(a, b, c):
        return density_from_jet(*add((1., DELTA), (a, Aj), (b, Bj), (c, Cj)))[0]
    d_a = jax.grad(F, 0)
    c_AABB = 0.25 * jax.grad(jax.grad(jax.grad(d_a, 0), 1), 1)(0., 0., 0.)
    c_AAC = 0.5 * jax.grad(jax.grad(d_a, 0), 2)(0., 0., 0.)
    return c_AABB, c_AAC


def grad_ABK_point(Aj, Bj):
    def phi(Kj):
        def F(a, b):
            return density_from_jet(*add((1., DELTA), (a, Aj), (b, Bj), (1., Kj)))[0]
        return jax.grad(jax.grad(F, 0), 1)(0., 0.)
    zero = (jnp.zeros((4, 4)), jnp.zeros((4, 4, 4)), jnp.zeros((4, 4, 4, 4)))
    return jax.grad(phi)(zero)


def ric_lin_flat(Kj):
    _, _, dd = Kj
    # dd[i,j,k,l] = d_k d_l K_ij
    R = 0.5 * (jnp.einsum('jkik->ij', dd) + jnp.einsum('ikjk->ij', dd) - jnp.einsum('kkij->ij', dd)
               - jnp.einsum('ijkk->ij', dd))
    return R - 0.25 * jnp.trace(R) * jnp.eye(4)


# ---------------- K basis ----------------
def monomials(deg):
    out = []
    for e in itertools.product(range(deg + 1), repeat=4):
        if sum(e) == deg:
            out.append(e)
    return out


SYM = [(a, b) for a in range(4) for b in range(a, 4)]


def make_K_basis(D):
    mons = monomials(D)
    basis = []
    for (a, b) in SYM:
        E = np.zeros((4, 4)); E[a, b] = 1; E[b, a] = 1
        for m in mons:
            basis.append((E, np.array(m)))
    return basis


def K_field(E, m, D):
    E = jnp.array(E); m = [int(v) for v in m]
    def K(x):
        mon = 1.0
        for i in range(4):
            if m[i] > 0:
                mon = mon * x[i] ** m[i]   # integer_pow: safe derivatives at x_i = 0
        return E * mon / jnp.dot(x, x) ** (D // 2)
    return K


def invariant_K_basis():
    """SU(2)_- invariant degree-0 symmetric tensors: Sym^2 span{dr, s1, s2, s3}"""
    def forms(x):
        x1, y1, x2, y2 = x
        r = jnp.sqrt(jnp.dot(x, x))
        dr = x / r
        s3 = jnp.array([-y1, x1, -y2, x2]) / r
        # z1 dz2 - z2 dz1 = (x1+iy1)(dx2+idy2) - (x2+iy2)(dx1+idy1)
        re = jnp.array([-x2, y2, x1, -y1]) / r
        im = jnp.array([-y2, -x2, y1, x1]) / r
        return [dr, re, im, s3]
    fields = []
    names = ['dr', 's1', 's2', 's3']
    for i in range(4):
        for j in range(i, 4):
            def K(x, i=i, j=j):
                f = forms(x)
                return 0.5 * (jnp.outer(f[i], f[j]) + jnp.outer(f[j], f[i]))
            fields.append(((names[i], names[j]), K))
    return fields


# ---------------- driver ----------------
def tail_A():
    return ddbar_metric(lambda x: jnp.log(jnp.dot(x, x)), Jz)


def run_background(Bfun, Cfun, X, W, Kbasis_fields, label, chunk=512):
    """returns c0 = int(c_AABB + c_AAC), vector b, matrix Q (for given K fields)"""
    Afun = tail_A()
    def pt(x):
        Aj = jet(Afun, x); Bj = jet(Bfun, x); Cj = jet(Cfun, x)
        c1, c2 = coeffs_point(Aj, Bj, Cj)
        G = grad_ABK_point(Aj, Bj)
        return c1, c2, G
    ptv = jax.jit(jax.vmap(pt))
    nK = len(Kbasis_fields)
    def kjets(x):
        js = [jet(K, x) for K in Kbasis_fields]
        return js
    c1t = 0.; c2t = 0.
    b = np.zeros(nK); Q = np.zeros((nK, nK))
    # vectorised K jets: stack
    def kstack(x):
        j0 = jnp.stack([K(x) for K in Kbasis_fields])
        j1 = jnp.stack([jax.jacfwd(K)(x) for K in Kbasis_fields])
        j2 = jnp.stack([jax.jacfwd(jax.jacfwd(K))(x) for K in Kbasis_fields])
        return j0, j1, j2
    ks = jax.jit(jax.vmap(kstack))
    rl = jax.jit(jax.vmap(jax.vmap(lambda j0, j1, j2: ric_lin_flat((j0, j1, j2)))))
    for s0 in range(0, X.shape[0], chunk):
        xs = X[s0:s0 + chunk]; ws = W[s0:s0 + chunk]
        c1, c2, G = ptv(xs)
        c1t += float(jnp.sum(ws * c1)); c2t += float(jnp.sum(ws * c2))
        j0, j1, j2 = ks(xs)  # (n, nK, ...)
        bb = (jnp.einsum('pij,pkij->pk', G[0], j0) + jnp.einsum('pijm,pkijm->pk', G[1], j1)
              + jnp.einsum('pijmn,pkijmn->pk', G[2], j2))
        b += np.array(jnp.einsum('p,pk->k', ws, bb))
        L = rl(j0, j1, j2)  # (n,nK,4,4)
        Q += np.array(jnp.einsum('p,pkij,plij->kl', ws, L, L))
    return c1t, c2t, b, Q


def minimise(c0, b, Q, tol=1e-9):
    w, V = np.linalg.eigh(Q)
    big = w > tol * max(w.max(), 1e-300)
    bt = V.T @ b
    ker_leak = float(np.linalg.norm(bt[~big])) if (~big).any() else 0.0
    val = c0 - 0.25 * float(np.sum(bt[big] ** 2 / w[big]))
    kappa = -0.5 * V[:, big] @ (bt[big] / w[big])
    return val, ker_leak, kappa, int((~big).sum())


if __name__ == '__main__':
    pass
