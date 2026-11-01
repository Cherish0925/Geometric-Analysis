"""Step 49: background dependence of the x^2 log(1/x) (= eps^2 log(1/eps)) coefficient
of a perpendicular Burns insertion into an Einstein background.

Mathematics (see workspace/notes/step49_kernel_log_coefficient_general_background.md):
  g_eps = g_bg + eps*k,  k = kB + sum_a e_a B_a,  kB = (sigma_1^2+sigma_2^2) (Burns tail,
  exact: Burns = flat + eps*kB in the Bianchi-IX form a=(sqrt(t^2+eps),sqrt(t^2+eps),t)).
  For Einstein g_bg, P(g_eps) = eps^2 int |Ric0'(k)|^2 dV + O(eps^3) in the overlap region.
  The log coefficient is C = int_{S^3} f_{-4}(omega) dOmega, where f_{-4} is the homogeneous
  degree -4 part (Cartesian normal coordinates) of the density |Ric0'(k)|^2_{g_bg} sqrt(det g_bg).
  Then P/8pi^2 contains (C/(16 pi^2)) eps^2 log(1/eps), i.e. F := C/(8 pi^2) is the coefficient
  in L_P = (eps^2/t) F of web_research_collected.tex Ch.5 (CH check: F(c=0)=59/4, F(c*)=-18).
  Total t-derivatives cannot change F (d/dt(z^a y^b) = (2b-2a) z^a y^b/t vanishes at a=b=2).

Laurent coefficients are extracted exactly (to rounding) by Cauchy averages over complex
lambda on a circle, x = lambda*omega, using holomorphic JAX differentiation.

Usage: python step49_kernel_log_coefficient.py BACKGROUND [NS NXI M RHO ANGDEG]
  BACKGROUND in {CH, H2H2, FLAT}
Output: workspace/data/step49/quadform_<BG>_<params>.npz and .json summary
"""
import sys, os, json, time, math, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step49")
os.makedirs(OUT, exist_ok=True)

# ---------- quaternion left-invariant coframe: (conj(q) dq)_m = v_m(x).dx, v_m = J_m x
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def conj(q): return np.array([q[0], -q[1], -q[2], -q[3]])
E4 = np.eye(4)
Jm = np.zeros((3, 4, 4))      # v_m(x)_b = sum_c Jm[m,b,c] x_c
for c in range(4):
    for b in range(4):
        prod = qmul(conj(E4[c]), E4[b])
        for m in range(3):
            Jm[m, b, c] = prod[m+1]
Jm_j = jnp.array(Jm)

def series(coeffs, u):
    out = 0.0*u
    for cf in reversed(coeffs):
        out = out*u + cf
    return out
NT = 22
fact = [math.factorial(n) for n in range(2*NT+4)]
# CH (Ric=-6g): a1^2=a3^2=sinh^2 t, a2^2 = sinh^2 t cosh^2 t;  psi=(a^2-u)/u^2
psi_S = [2**(2*n-1)/fact[2*n] for n in range(2, NT)]
psi_SC = [16**n/(8*fact[2*n]) for n in range(2, NT)]
S2_over_u = [2**(2*n-1)/fact[2*n] for n in range(1, NT)]      # sinh^2(t)/u
# H^2 of curvature -6: f^2 = sinh^2(sqrt6 rho)/6, phi = (f^2/u - 1)/u
phi_H = [24**n/(12*fact[2*n]) for n in range(2, NT)]

def vvec(x):
    return jnp.einsum('mbc,c->mb', Jm_j, x)   # (3,4)

# H2xH2 planes: P1 = span(e0, J2 e0); J2 is the CH complex structure (v_2 = J_2 x)
u0 = E4[0]; u1v = Jm[1] @ u0
# find u2 orthogonal to P1
cand = E4[2] - (E4[2]@u0)*u0 - (E4[2]@u1v)*u1v
if np.linalg.norm(cand) < 1e-8:
    cand = E4[3] - (E4[3]@u0)*u0 - (E4[3]@u1v)*u1v
u2v = cand/np.linalg.norm(cand); u3v = Jm[1] @ u2v
O = jnp.array(np.stack([u0, u1v, u2v, u3v], axis=1))

def g_H2(z):
    u = z@z
    return jnp.eye(2) + series(phi_H, u)*(u*jnp.eye(2) - jnp.outer(z, z))

def gb_factory(bg):
    if bg == "CH":
        def gb(x):
            u = x@x; v = vvec(x)
            return (jnp.eye(4) + series(psi_S, u)*jnp.outer(v[0], v[0])
                    + series(psi_SC, u)*jnp.outer(v[1], v[1]) + series(psi_S, u)*jnp.outer(v[2], v[2]))
    elif bg == "H2H2":
        def gb(x):
            y = O.T @ x
            G = jnp.zeros((4, 4), dtype=x.dtype)
            G = G.at[0:2, 0:2].set(g_H2(y[0:2])).at[2:4, 2:4].set(g_H2(y[2:4]))
            return O @ G @ O.T
    elif bg == "FLAT":
        def gb(x):
            return jnp.eye(4, dtype=x.dtype)
    return gb

# ---------- basis of tangent tensors
Esym = []
for a in range(4):
    for b in range(a, 4):
        E = np.zeros((4, 4)); E[a, b] = E[b, a] = 1.0
        Esym.append(E)
Esym = jnp.array(Esym)                       # (10,4,4)

def monomials(x, deg):
    u = x@x
    if deg == 0:
        return jnp.ones((1,), dtype=x.dtype)
    idx = list(itertools.combinations_with_replacement(range(4), deg))
    return jnp.stack([jnp.prod(x[jnp.array(i)]) for i in idx]) / u**(deg//2)

def make_kfun(angdeg, extra_k2):
    def kfun(x, e):
        u = x@x; v = vvec(x)
        S2 = u*series(S2_over_u, u); C2 = 1 + S2
        named = jnp.stack([
            (jnp.outer(v[0], v[0]) + jnp.outer(v[1], v[1]))/u**2,   # 0: Burns tail kB
            S2*jnp.outer(v[1], v[1])/u**2,                           # 1: CH ansatz (C^2-1) sigma2^2 piece
            2*S2*jnp.outer(v[0], v[0])/u**2,                         # 2: c1 mode
            2*S2*C2*jnp.outer(v[1], v[1])/u**2,                      # 3: c2 mode
            2*S2*jnp.outer(v[2], v[2])/u**2])                        # 4: c3 mode
        mons = jnp.concatenate([monomials(x, d) for d in range(0, angdeg+1, 2)])
        gen = jnp.einsum('m,eij->meij', mons, Esym).reshape(-1, 4, 4)
        parts = [named, gen]
        if extra_k2:
            m2 = monomials(x, 2)*u     # degree-2 homogeneous x_c x_d
            parts.append(jnp.einsum('m,eij->meij', m2, Esym).reshape(-1, 4, 4))
        allk = jnp.concatenate(parts)
        return jnp.einsum('a,aij->ij', e, allk), allk.shape[0]
    return kfun

def build(bg, angdeg, extra_k2):
    gb = gb_factory(bg)
    kfun = make_kfun(angdeg, extra_k2)
    nb = kfun(jnp.array([0.3, 0.2, 0.1, 0.5], dtype=jnp.complex128), jnp.zeros(1000, dtype=jnp.complex128)[:0] if False else None)[1] if False else None
    return gb, kfun

def ricci_alg(g, dg, ddg):
    """Ricci from metric jets: dg[i,j,k]=d_k g_ij, ddg[i,j,k,l]=d_l d_k g_ij."""
    gi = jnp.linalg.inv(g)
    # Gamma_low[d,b,c] = 1/2(d_b g_dc + d_c g_db - d_d g_bc)
    Gl = 0.5*(dg.transpose(0, 2, 1) + dg - jnp.einsum('bcd->dbc', dg))
    G = jnp.einsum('ad,dbc->abc', gi, Gl)
    # d_e Gamma_low[d,b,c] = 1/2(d_e d_b g_dc + d_e d_c g_db - d_e d_d g_bc)
    dGl = 0.5*(ddg.transpose(0, 2, 1, 3) + ddg - jnp.einsum('bcde->dbce', ddg))
    dgi = -jnp.einsum('am,mne,nd->ade', gi, dg, gi)
    dG = jnp.einsum('ade,dbc->abce', dgi, Gl) + jnp.einsum('ad,dbce->abce', gi, dGl)
    return (jnp.einsum('abca->bc', dG) - jnp.einsum('aabc->bc', dG)
            + jnp.einsum('aad,dbc->bc', G, G) - jnp.einsum('acd,dab->bc', G, G))

def ric0_alg(g, dg, ddg):
    R = ricci_alg(g, dg, ddg); gi = jnp.linalg.inv(g)
    s = jnp.einsum('ij,ij->', gi, R)
    return R - 0.25*s*g

def main():
    bg = sys.argv[1]
    NS = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    NXI = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    M = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    RHO = float(sys.argv[5]) if len(sys.argv) > 5 else 0.3
    ANG = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    K2 = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    gb = gb_factory(bg)
    kfun = make_kfun(ANG, K2)
    nb = 5 + 10*sum(len(list(itertools.combinations_with_replacement(range(4), d))) for d in range(0, ANG+1, 2)) + (100 if K2 else 0)
    def kall(x):
        return kfun(x, jnp.ones(nb, dtype=x.dtype))[0]  # unused
    def kstack(x):
        u = x@x
        e = jnp.eye(nb, dtype=x.dtype)
        return jax.vmap(lambda ee: kfun(x, ee)[0])(e)   # (nb,4,4)
    def per_point(x):
        g = gb(x)
        dg = jax.jacfwd(gb, holomorphic=True)(x)
        ddg = jax.jacfwd(jax.jacfwd(gb, holomorphic=True), holomorphic=True)(x)
        K = kstack(x)
        dK = jax.jacfwd(kstack, holomorphic=True)(x)                       # (nb,4,4,4)
        ddK = jax.jacfwd(jax.jacfwd(kstack, holomorphic=True), holomorphic=True)(x)
        lin = lambda k, dk, ddk: jax.jvp(ric0_alg, (g, dg, ddg), (k, dk, ddk))[1]
        Rs = jax.vmap(lin)(K, dK, ddK)                                     # (nb,4,4)
        gi = jnp.linalg.inv(g); sd = jnp.sqrt(jnp.linalg.det(g))
        Rup = jnp.einsum('ik,akl,lj->aij', gi, Rs, gi)
        Gm = (Rup*sd, Rs)   # bilinear form assembled outside by one matrix product
        Rb = ricci_alg(g, dg, ddg)
        resid = jnp.max(jnp.abs(Rb + 6.0*g)) if bg != "FLAT" else jnp.max(jnp.abs(Rb))
        return Gm, resid

    pp = jax.jit(jax.vmap(per_point))

    # quadrature on S^3 (Hopf): omega=(sqrt(1-s)cos xi1, sqrt(1-s) sin xi1, sqrt(s) cos xi2, sqrt(s) sin xi2)
    sn, sw = np.polynomial.legendre.leggauss(NS); sn = 0.5*(sn+1); sw = 0.5*sw
    xi = 2*np.pi*np.arange(NXI)/NXI; xw = 2*np.pi/NXI
    pts, wts = [], []
    for s, w in zip(sn, sw):
        for a in xi:
            for b in xi:
                pts.append([math.sqrt(1-s)*math.cos(a), math.sqrt(1-s)*math.sin(a),
                            math.sqrt(s)*math.cos(b), math.sqrt(s)*math.sin(b)])
                wts.append(0.5*w*xw*xw)
    pts = np.array(pts); wts = np.array(wts)
    lam = RHO*np.exp(2j*np.pi*(np.arange(M)+0.5)/M)
    Q = np.zeros((nb, nb), dtype=np.complex128); maxres = 0.0
    t0 = time.time(); CH = 64
    allx = (lam[None, :, None]*pts[:, None, :]).reshape(-1, 4)
    allw = (wts[:, None]*lam[None, :]**4/M).reshape(-1)
    for i in range(0, allx.shape[0], CH):
        (A, B), res = pp(jnp.array(allx[i:i+CH]))
        A = np.array(A); B = np.array(B); n = A.shape[0]
        A = (allw[i:i+CH][:, None, None, None]*A).transpose(0, 2, 3, 1).reshape(-1, nb)
        B = B.transpose(0, 2, 3, 1).reshape(-1, nb)
        Q += A.T @ B
        maxres = max(maxres, float(np.max(np.abs(np.array(res)))))
        if i == 0:
            print("first chunk", time.time()-t0, flush=True)
    print("time", time.time()-t0, "max bg Einstein residual", maxres, flush=True)
    Qr = Q.real; imag = float(np.max(np.abs(Q.imag)))
    tag = f"{bg}_NS{NS}_NXI{NXI}_M{M}_R{RHO}_A{ANG}_K{K2}"
    np.savez(os.path.join(OUT, f"quadform_{tag}.npz"), Q=Qr, Qimag=Q.imag)
    F = Qr/(8*np.pi**2)
    res = {"background": bg, "params": dict(NS=NS, NXI=NXI, M=M, RHO=RHO, ANG=ANG, K2=K2),
           "nbasis": nb, "max_imag": imag, "max_bg_residual": maxres}
    # CH-ansatz evaluation: k = kB + kCHtail + sum c_i mode_i
    def Fval(vec):
        return float(vec @ F @ vec)
    v0 = np.zeros(nb); v0[0] = 1; v0[1] = 1
    res["F_ansatz_c0"] = Fval(v0)
    cst = np.zeros(nb); cst[0] = 1; cst[1] = 1; cst[2:5] = [9/4, 3/4, 1/2]
    res["F_ansatz_cstar"] = Fval(cst)
    res["F_burns_only_kB"] = float(F[0, 0])
    # optimal over subspaces
    def optimize(idx):
        idx = np.array(idx)
        A = F[np.ix_(idx, idx)]; b = F[0, idx]
        w, V = np.linalg.eigh(A)
        keep = w > 1e-9*max(1, abs(w).max())
        Ainv = (V[:, keep]/w[keep]) @ V[:, keep].T
        sol = -Ainv @ b
        val = F[0, 0] + b @ sol
        resid_lin = float(np.linalg.norm(b - A @ (Ainv @ b)))
        return float(val), int(np.sum(~keep)), (float(w[keep].min()) if keep.any() else None), resid_lin, sol
    n_named = 5; n_gen = nb - n_named - (100 if K2 else 0)
    gen_idx = list(range(n_named, n_named + n_gen))
    k2_idx = list(range(n_named + n_gen, nb))
    v, nn, wmin, rl, _ = optimize([1, 2, 3, 4]); res["opt_CHansatz_modes"] = dict(F=v, null=nn, minpos=wmin, linresid=rl)
    v, nn, wmin, rl, _ = optimize(gen_idx); res["opt_general_deg0"] = dict(F=v, null=nn, minpos=wmin, linresid=rl)
    if K2:
        res["k2_linear_coupling_norm"] = float(np.linalg.norm(F[0, k2_idx]))
        res["k2_quadratic_block_norm"] = float(np.linalg.norm(F[np.ix_(k2_idx, k2_idx)]))
        res["k2_cross_gen_norm"] = float(np.linalg.norm(F[np.ix_(k2_idx, gen_idx)]))
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, f"summary_{tag}.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
