"""Step 51: full Chern-Gauss-Bonnet-form logarithmic corner coefficient F(Rm_p, zeta) of a perpendicular
Burns insertion, for an arbitrary algebraic curvature jet at the insertion point.

Mathematics (workspace/notes/step51_kernel_spectrum_log_coefficient.md; Step-50 note Lemma 1.1):
  f(g) = (4|W+|^2 + s^2/12) sqrt(det g)       (pointwise CGB: |Ric0|^2 = f - Chern-Weil, exact forms)
  g(a,eps) = delta + a*h2 + eps*(kB + a*K_c),  h2 = -(1/3) R_ikjl x^k x^l,  K_c = sum c_i K_i (degree 0)
  Homogeneity: f(a,eps; lam x) = lam^-4 f(a lam^2, eps lam^-2; x), so the degree -4 part of the
  order-eps^2 relative density is EXACTLY the a^2 eps^2 Taylor coefficient at |x| = 1.
  F(c) = (1/8pi^2) int_{S^3} [a^2 eps^2] f dOmega = C0 + 2 B.c + c^T A c,
  A = flat (W+,s) linearization block (as in step50), B, C0 from exact nested forward derivatives.
  Also returned: the [a eps] coefficient (diagonal order-eps corner; must vanish since Burns is ASD+scalar-flat).

Curvature jet: Einstein part with s = -24 and W+ = diag(lam1, lam2, lam3) in the (J1,J2,J3) basis of
Lambda+ (Burns zeta = J3), optional W- jet (that of H2xH2) times wm, optional Ric0 jet.
  h2 = (2/3) sum_m v_m v_m^T - (1/6) sum_m lam_m v_m v_m^T  (+ wm * hW)
Checks: CH = (2,-4,2): F(kB only) = 12, F_opt = -18 (Step 49 Ric0-form: 11.99999999999, -18.0000000000).
        H2xH2 = CH + hW: F(kB only) = 17.6, F_opt = -18.

Usage: python step51_cgb_full_coefficient.py OUT_TAG lam1 lam2 lam3 [wm ANG NS NXI]
Output: workspace/data/step51/cgb_<OUT_TAG>.json
"""
import sys, os, json, time, math, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step51")
os.makedirs(OUT, exist_ok=True)

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def conj(q): return np.array([q[0], -q[1], -q[2], -q[3]])
E4 = np.eye(4)
Jm = np.zeros((3, 4, 4))
for c in range(4):
    for b in range(4):
        prod = qmul(conj(E4[c]), E4[b])
        for m in range(3):
            Jm[m, b, c] = prod[m+1]
Jm_j = jnp.array(Jm)
def vvec(x): return jnp.einsum('mbc,c->mb', Jm_j, x)

u0 = E4[0]; u1v = Jm[1] @ u0
cand = E4[2] - (E4[2]@u0)*u0 - (E4[2]@u1v)*u1v
if np.linalg.norm(cand) < 1e-8:
    cand = E4[3] - (E4[3]@u0)*u0 - (E4[3]@u1v)*u1v
u2v = cand/np.linalg.norm(cand); u3v = Jm[1] @ u2v
O = jnp.array(np.stack([u0, u1v, u2v, u3v], axis=1))

def h2_CH(x):
    v = vvec(x)
    return (1/3)*(jnp.outer(v[0], v[0]) + jnp.outer(v[2], v[2])) + (4/3)*jnp.outer(v[1], v[1])
def h2_H2H2(x):
    y = O.T @ x
    def blk(z): return 2*((z@z)*jnp.eye(2) - jnp.outer(z, z))
    G = jnp.zeros((4, 4)).at[0:2, 0:2].set(blk(y[0:2])).at[2:4, 2:4].set(blk(y[2:4]))
    return O @ G @ O.T
def hW(x): return h2_H2H2(x) - h2_CH(x)

# fixed trace-free Ricci direction (generic, not aligned with the J-frame)
E_RIC = np.array([[1.0, 0.3, 0.0, 0.2], [0.3, -0.5, 0.4, 0.0], [0.0, 0.4, 0.7, -0.1], [0.2, 0.0, -0.1, -1.2]])
E_RIC = jnp.array(E_RIC - np.trace(E_RIC)/4*np.eye(4))

def h2_ric0(x, E):
    """h2 for R = (1/2) E (Kulkarni-Nomizu) g, E trace-free: h_ij = -(1/3) R_ikjl x^k x^l."""
    u = x@x; Ex = E@x
    return -(1/6)*(E*u + (x@Ex)*jnp.eye(4) - jnp.outer(Ex, x) - jnp.outer(x, Ex))

def make_h2(lams, wm, rc=0.0):
    lams = jnp.array(lams)
    def h2(x):
        v = vvec(x)
        base = sum(((2/3) - lams[m]/6)*jnp.outer(v[m], v[m]) for m in range(3))
        return base + wm*hW(x) + rc*h2_ric0(x, E_RIC)
    return h2

def kB(x):
    u = x@x; v = vvec(x)
    return (jnp.outer(v[0], v[0]) + jnp.outer(v[1], v[1]))/u**2

def riemann(g, dg, ddg):
    gi = jnp.linalg.inv(g)
    Gl = 0.5*(dg.transpose(0, 2, 1) + dg - jnp.einsum('bcd->dbc', dg))
    G = jnp.einsum('ad,dbc->abc', gi, Gl)
    dGl = 0.5*(ddg.transpose(0, 2, 1, 3) + ddg - jnp.einsum('bcde->dbce', ddg))
    dgi = -jnp.einsum('am,mne,nd->ade', gi, dg, gi)
    dG = jnp.einsum('ade,dbc->abce', dgi, Gl) + jnp.einsum('ad,dbce->abce', gi, dGl)
    Rup = (jnp.einsum('adbc->abcd', dG) - jnp.einsum('acbd->abcd', dG)
           + jnp.einsum('ace,edb->abcd', G, G) - jnp.einsum('ade,ecb->abcd', G, G))
    return jnp.einsum('ae,ebcd->abcd', g, Rup)

PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
Jvec = np.array([[Jm[m][a, b] for (a, b) in PAIRS] for m in range(3)])
Jvec = Jvec/np.linalg.norm(Jvec, axis=1, keepdims=True)
Jv = jnp.array(Jvec)
BIN = [1.0, -0.5, 0.375, -0.3125, 0.2734375]    # (1+H)^(-1/2) to 4th order (exact for 4th derivatives)

def curv_data(g, dg, ddg, order=4):
    R = riemann(g, dg, ddg)
    H = g - jnp.eye(4)
    e = BIN[0]*jnp.eye(4); Hp = jnp.eye(4)
    for n in range(1, order+1):
        Hp = Hp @ H; e = e + BIN[n]*Hp
    Rf = jnp.einsum('ia,jb,kc,ld,ijkl->abcd', e, e, e, e, R)
    Ric = jnp.einsum('abad->bd', Rf)
    s = jnp.trace(Ric)
    I = jnp.eye(4)
    Wf = (Rf - 0.5*(jnp.einsum('ac,bd->abcd', I, Ric) - jnp.einsum('ad,bc->abcd', I, Ric)
                    - jnp.einsum('bc,ad->abcd', I, Ric) + jnp.einsum('bd,ac->abcd', I, Ric))
          + (s/6)*(jnp.einsum('ac,bd->abcd', I, I) - jnp.einsum('ad,bc->abcd', I, I)))
    M = jnp.stack([jnp.stack([Wf[a, b, c, d] for (c, d) in PAIRS]) for (a, b) in PAIRS])
    return Jv @ M @ Jv.T, s

def jets(f, x):
    return f(x), jax.jacfwd(f)(x), jax.jacfwd(jax.jacfwd(f))(x)

def monomials(x, deg):
    u = x@x
    if deg == 0:
        return jnp.ones((1,))
    idx = list(itertools.combinations_with_replacement(range(4), deg))
    return jnp.stack([jnp.prod(x[jnp.array(i)]) for i in idx]) / u**(deg//2)

Esym = []
for a in range(4):
    for b in range(a, 4):
        E = np.zeros((4, 4)); E[a, b] = E[b, a] = 1.0
        Esym.append(E)
Esym = jnp.array(Esym)

def make_basis(angmax):
    def kstack(x):
        mons = jnp.concatenate([monomials(x, d) for d in range(0, angmax+1, 2)])
        return jnp.einsum('m,eij->meij', mons, Esym).reshape(-1, 4, 4)
    return kstack

def main():
    tag = sys.argv[1]
    lams = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    wm = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
    ANG = int(sys.argv[6]) if len(sys.argv) > 6 else 4
    NS = int(sys.argv[7]) if len(sys.argv) > 7 else 12
    NXI = int(sys.argv[8]) if len(sys.argv) > 8 else 20
    rc = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0
    assert abs(sum(lams)) < 1e-12, "W+ must be trace-free"
    h2 = make_h2(lams, wm, rc)
    kstack = make_basis(ANG)

    def per_point(x):
        Hh, dHh, ddHh = jets(h2, x)
        Kb, dKb, ddKb = jets(kB, x)
        K, dK, ddK = jets(kstack, x)
        I = jnp.eye(4)
        def fval(a, ep, c):
            Kc = jnp.einsum('i,ijk->jk', c, K); dKc = jnp.einsum('i,ijkl->jkl', c, dK)
            ddKc = jnp.einsum('i,ijklm->jklm', c, ddK)
            g = I + a*Hh + ep*Kb + a*ep*Kc
            dg = a*dHh + ep*dKb + a*ep*dKc
            ddg = a*ddHh + ep*ddKb + a*ep*ddKc
            Wp, s = curv_data(g, dg, ddg)
            return (4*jnp.sum(Wp*Wp) + s*s/12)*jnp.sqrt(jnp.linalg.det(g))
        def coef22(c):
            d = jax.grad
            f4 = d(d(d(d(fval, 0), 0), 1), 1)
            return f4(0.0, 0.0, c)/4.0
        def coef11(c):
            return jax.grad(jax.grad(fval, 0), 1)(0.0, 0.0, c)
        c0 = jnp.zeros(K.shape[0])
        C0 = coef22(c0)
        B = 0.5*jax.grad(coef22)(c0)
        C11 = coef11(c0)
        # flat linearization block (W+ and s) for each basis tensor
        def lin_flat(k, dk, ddk):
            def Fw(ep):
                Wp, s = curv_data(I + ep*k, ep*dk, ep*ddk, order=1)
                return jnp.concatenate([Wp.reshape(-1), jnp.array([s])])
            return jax.jacfwd(Fw)(0.0)
        L = jax.vmap(lin_flat)(K, dK, ddK)
        return C0, B, C11, L

    pp = jax.jit(jax.vmap(per_point))
    sn, sw = np.polynomial.legendre.leggauss(NS); sn = 0.5*(sn+1); sw = 0.5*sw
    xi = 2*np.pi*np.arange(NXI)/NXI; xw = 2*np.pi/NXI
    pts, wts = [], []
    for s_, w_ in zip(sn, sw):
        for a in xi:
            for b in xi:
                pts.append([math.sqrt(1-s_)*math.cos(a), math.sqrt(1-s_)*math.sin(a),
                            math.sqrt(s_)*math.cos(b), math.sqrt(s_)*math.sin(b)])
                wts.append(0.5*w_*xw*xw)
    pts = np.array(pts); wts = np.array(wts)
    t0 = time.time()
    C0t = 0.0; C11t = 0.0; Bt = None; At = None
    wvec = np.concatenate([4*np.ones(9), [1/12]])
    CHK = 160
    for i in range(0, len(pts), CHK):
        C0, B, C11, L = [np.array(o) for o in pp(jnp.array(pts[i:i+CHK]))]
        w = wts[i:i+CHK]
        C0t += float(w @ C0); C11t += float(w @ C11)
        Bi = w @ B
        Lw = L*np.sqrt(wvec)[None, None, :]*np.sqrt(w)[:, None, None]      # (n, nb, 10)
        Lf = Lw.transpose(0, 2, 1).reshape(-1, L.shape[1])
        Ai = Lf.T @ Lf
        Bt = Bi if Bt is None else Bt + Bi
        At = Ai if At is None else At + Ai
        if i == 0:
            print("first chunk", time.time()-t0, flush=True)
    n8 = 8*np.pi**2
    C0t /= n8; C11t /= n8; Bt = Bt/n8; At = At/n8
    ev, V = np.linalg.eigh(At)
    keep = ev > 1e-10*ev.max()
    Ainv = (V[:, keep]/ev[keep]) @ V[:, keep].T
    sol = -Ainv @ Bt
    Fopt = C0t + Bt @ sol
    rangeres = float(np.linalg.norm(Bt - At @ (Ainv @ Bt)))
    mu = [l - 2.0 for l in lams]          # R+ eigenvalues W+ + s/12, s = -24
    res = dict(tag=tag, lams=lams, wm=wm, ric0_scale=rc, ANG=ANG, NS=NS, NXI=NXI, nbasis=int(len(Bt)),
               F_kB_only=C0t, F_opt=float(Fopt), a_eps_coef=C11t, B_range_residual=rangeres,
               null=int(np.sum(~keep)), Rplus=mu, Rplus_zeta=mu[2],
               A02_Phi=float(-mu[2]*(mu[2]-mu[0]-mu[1])/2 - (mu[0]-mu[1])**2/2),
               time=time.time()-t0)
    print(json.dumps(res, indent=1), flush=True)
    json.dump(res, open(os.path.join(OUT, f"cgb_{tag}.json"), "w"), indent=1)
    np.savez(os.path.join(OUT, f"cgb_{tag}.npz"), A=At, B=Bt, sol=sol)

if __name__ == "__main__":
    main()
