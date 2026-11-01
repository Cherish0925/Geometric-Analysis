"""Step 50: W^- compatibility of the perpendicular Burns tail, in the Chern-Gauss-Bonnet (W+, s) form.

Mathematics (workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md):
  Pointwise CGB in 4D:  |Ric0|^2 = 4|W+|^2 + s^2/12 - (16 pi^2 e + 24 pi^2 p),  e,p Chern-Weil densities.
  Relative to a fixed background the Chern-Weil terms are exact, and an exact homogeneous degree -4
  density has zero S^3 average, so the eps^2 log coefficient F can be computed from 4|W+|^2+s^2/12.
  Since Burns = delta + eps*kB is exactly ASD (W+=0) and scalar-flat, only Rm_p (the quadratic
  normal-coordinate jet h_2) enters F.  The W^- -dependent part of F is
        kappa(W^-) = min_{k0} (1/8pi^2) int_{S^3} [ 4|S_W + Lw(k0)|^2 + (sigma_W + Ls(k0))^2/12 ],
  where S_W  = d_a d_eps W+(delta + a h_W + eps kB)|_0      (homogeneous degree -2),
        sigma_W = d_a d_eps s(delta + a h_W + eps kB)|_0,
        Lw(k0) = d_eps W+(delta + eps k0), Ls(k0) = d_eps s(delta + eps k0)  (k0 homogeneous degree 0).
  kappa = 0  iff  (S_W, sigma_W) lies in the range of (Lw, Ls) on degree-0 correctors.

All quantities are homogeneous, so they are evaluated at |x| = 1 with no Laurent extraction.
Norm convention: |W+|^2 = Frobenius norm of the operator on Lambda^2 with entries W_abcd (a<b, c<d),
which is the convention in 8 pi^2 chi = int(|W|^2 - |Ric0|^2/2 + s^2/24) (checked on CP^2).
Also computes the flat corrector block in Ric0 form, to compare with Step-49 quadforms (CGB check).

Usage: python step50_wminus_compatibility.py [ANGMAX NS NXI]
Output: workspace/data/step50/wminus_compat_A<ANGMAX>.json, .npz
"""
import sys, os, json, time, math, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step50")
os.makedirs(OUT, exist_ok=True)

# quaternion left-invariant coframe, identical to step49
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

# H2xH2 orthonormal adapted basis (same as step49)
u0 = E4[0]; u1v = Jm[1] @ u0
cand = E4[2] - (E4[2]@u0)*u0 - (E4[2]@u1v)*u1v
if np.linalg.norm(cand) < 1e-8:
    cand = E4[3] - (E4[3]@u0)*u0 - (E4[3]@u1v)*u1v
u2v = cand/np.linalg.norm(cand); u3v = Jm[1] @ u2v
O = jnp.array(np.stack([u0, u1v, u2v, u3v], axis=1))

# quadratic normal-coordinate jets h_2 (Ric = -6 g)
def h2_CH(x):
    v = vvec(x)
    return (1/3)*(jnp.outer(v[0], v[0]) + jnp.outer(v[2], v[2])) + (4/3)*jnp.outer(v[1], v[1])
def h2_H2H2(x):
    y = O.T @ x
    def blk(z): return 2*((z@z)*jnp.eye(2) - jnp.outer(z, z))
    G = jnp.zeros((4, 4)).at[0:2, 0:2].set(blk(y[0:2])).at[2:4, 2:4].set(blk(y[2:4]))
    return O @ G @ O.T
def hW(x): return h2_H2H2(x) - h2_CH(x)
def kB(x):
    u = x@x; v = vvec(x)
    return (jnp.outer(v[0], v[0]) + jnp.outer(v[1], v[1]))/u**2

# ----- curvature from jets
def riemann(g, dg, ddg):
    """dg[i,j,k]=d_k g_ij, ddg[i,j,k,l]=d_l d_k g_ij. Returns R_abcd (sphere: g_ac g_bd - g_ad g_bc)."""
    gi = jnp.linalg.inv(g)
    Gl = 0.5*(dg.transpose(0, 2, 1) + dg - jnp.einsum('bcd->dbc', dg))      # Gl[d,b,c]
    G = jnp.einsum('ad,dbc->abc', gi, Gl)                                    # Gamma^a_bc
    dGl = 0.5*(ddg.transpose(0, 2, 1, 3) + ddg - jnp.einsum('bcde->dbce', ddg))
    dgi = -jnp.einsum('am,mne,nd->ade', gi, dg, gi)
    dG = jnp.einsum('ade,dbc->abce', dgi, Gl) + jnp.einsum('ad,dbce->abce', gi, dGl)  # d_e Gamma^a_bc
    # R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb
    Rup = (jnp.einsum('adbc->abcd', dG) - jnp.einsum('acbd->abcd', dG)
           + jnp.einsum('ace,edb->abcd', G, G) - jnp.einsum('ade,ecb->abcd', G, G))
    return jnp.einsum('ae,ebcd->abcd', g, Rup)

PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
# Lambda_ours = span of the left-invariant complex structures J_m (Burns zeta = J_3, CH omega = J_2)
Jvec = np.array([[Jm[m][a, b] for (a, b) in PAIRS] for m in range(3)])
Jvec = Jvec/np.linalg.norm(Jvec, axis=1, keepdims=True)
assert np.allclose(Jvec @ Jvec.T, np.eye(3))
Jv = jnp.array(Jvec)

def curv_data(g, dg, ddg):
    """Return (W+ as 3x3 in the J-basis, s, Ric0 in orthonormal frame)."""
    R = riemann(g, dg, ddg)
    gi = jnp.linalg.inv(g)
    H = g - jnp.eye(4)
    e = jnp.eye(4) - 0.5*H + 0.375*H@H          # g^{-1/2} to second order (exact for 2nd derivatives at 0)
    Rf = jnp.einsum('ia,jb,kc,ld,ijkl->abcd', e, e, e, e, R)
    Ric = jnp.einsum('abad->bd', Rf)             # sphere: +3 g
    s = jnp.trace(Ric)
    I = jnp.eye(4)
    Wf = (Rf - 0.5*(jnp.einsum('ac,bd->abcd', I, Ric) - jnp.einsum('ad,bc->abcd', I, Ric)
                    - jnp.einsum('bc,ad->abcd', I, Ric) + jnp.einsum('bd,ac->abcd', I, Ric))
          + (s/6)*(jnp.einsum('ac,bd->abcd', I, I) - jnp.einsum('ad,bc->abcd', I, I)))
    M = jnp.stack([jnp.stack([Wf[a, b, c, d] for (c, d) in PAIRS]) for (a, b) in PAIRS])
    Wp = Jv @ M @ Jv.T
    Ric0 = Ric - 0.25*s*I
    return Wp, s, Ric0

def jets(f, x):
    return f(x), jax.jacfwd(f)(x), jax.jacfwd(jax.jacfwd(f))(x)

def source_point(x, hfun):
    h, dh, ddh = jets(hfun, x)
    k, dk, ddk = jets(kB, x)
    I = jnp.eye(4)
    def F(ae):
        a, ep = ae[0], ae[1]
        return curv_data(I + a*h + ep*k, a*dh + ep*dk, a*ddh + ep*ddk)
    def Fw(ae): Wp, s, R0 = F(ae); return jnp.concatenate([Wp.reshape(-1), jnp.array([s]), R0.reshape(-1)])
    Hs = jax.jacfwd(jax.jacfwd(Fw))(jnp.zeros(2))       # (26,2,2)
    lin_h = jax.jacfwd(Fw)(jnp.zeros(2))                # (26,2)
    return Hs[:, 0, 1], lin_h[:, 0], lin_h[:, 1], jax.jacfwd(jax.jacfwd(Fw))(jnp.zeros(2))[:, 1, 1]

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

def lin_flat(k, dk, ddk):
    I = jnp.eye(4)
    def Fw(ep):
        Wp, s, R0 = curv_data(I + ep*k, ep*dk, ep*ddk)
        return jnp.concatenate([Wp.reshape(-1), jnp.array([s]), R0.reshape(-1)])
    return jax.jacfwd(Fw)(0.0)

def main():
    ANG = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    NS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    NXI = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    kstack = make_basis(ANG)
    def per_point(x):
        S, linh, link, kk = source_point(x, hW)
        K = kstack(x); dK = jax.jacfwd(kstack)(x); ddK = jax.jacfwd(jax.jacfwd(kstack))(x)
        L = jax.vmap(lin_flat)(K, dK, ddK)            # (nb,26)
        return S, linh, link, kk, L
    pp = jax.jit(jax.vmap(per_point))
    sn, sw = np.polynomial.legendre.leggauss(NS); sn = 0.5*(sn+1); sw = 0.5*sw
    xi = 2*np.pi*np.arange(NXI)/NXI; xw = 2*np.pi/NXI
    pts, wts = [], []
    for s_, w in zip(sn, sw):
        for a in xi:
            for b in xi:
                pts.append([math.sqrt(1-s_)*math.cos(a), math.sqrt(1-s_)*math.sin(a),
                            math.sqrt(s_)*math.cos(b), math.sqrt(s_)*math.sin(b)])
                wts.append(0.5*w*xw*xw)
    pts = np.array(pts); wts = np.array(wts)
    print("total S^3 volume (should be 2pi^2=%.6f):" % (2*np.pi**2), wts.sum(), flush=True)
    t0 = time.time()
    outs = [pp(jnp.array(pts[i:i+256])) for i in range(0, len(pts), 256)]
    S = np.concatenate([np.array(o[0]) for o in outs]); linh = np.concatenate([np.array(o[1]) for o in outs])
    link = np.concatenate([np.array(o[2]) for o in outs]); kk = np.concatenate([np.array(o[3]) for o in outs])
    L = np.concatenate([np.array(o[4]) for o in outs])     # (npts, nb, 26)
    print("eval time", time.time()-t0, flush=True)
    nb = L.shape[1]
    # sanity: hW is pure W^-, Burns tail exactly ASD + scalar-flat
    checks = {"max_linW+_hW": float(np.abs(linh[:, :10]).max()), "max_lin_Ric0_hW": float(np.abs(linh[:, 10:]).max()),
              "max_linW+s_kB": float(np.abs(link[:, :10]).max()), "max_secondW+s_kB": float(np.abs(kk[:, :10]).max())}
    # weights for the CGB density 4|W+|^2 + s^2/12 (W+ 3x3 in orthonormal J basis: Frobenius = op norm conv)
    wvec = np.concatenate([4*np.ones(9), [1/12]])
    sq = np.sqrt(wts)[:, None]*np.sqrt(wvec)[None, :]
    A = (sq[:, None, :]*L[:, :, :10]).transpose(0, 2, 1).reshape(-1, nb)     # rows (pt,comp)
    b = (sq*S[:, :10]).reshape(-1)
    norm2 = float(b @ b)/(8*np.pi**2)
    sol, res, rk, sv = np.linalg.lstsq(A, -b, rcond=1e-10)
    resid = A@sol + b
    kappa = float(resid@resid)/(8*np.pi**2)
    # SU(2)-invariant (diagonal) leading modes v_m v_m^T/u: should not couple (spin argument)
    def diagmodes(x):
        u = x@x; v = vvec(x)
        return jnp.stack([jnp.outer(v[m], v[m])/u for m in range(3)])
    def pd(x):
        K = diagmodes(x); dK = jax.jacfwd(diagmodes)(x); ddK = jax.jacfwd(jax.jacfwd(diagmodes))(x)
        return jax.vmap(lin_flat)(K, dK, ddK)
    Ld = np.array(jax.jit(jax.vmap(pd))(jnp.array(pts)))
    Ad = (sq[:, None, :]*Ld[:, :, :10]).transpose(0, 2, 1).reshape(-1, 3)
    coup_diag = float(np.linalg.norm(Ad.T@b))
    # CGB check: flat corrector block, Ric0 form versus (W+,s) form
    QW = A.T@A
    sqR = np.sqrt(wts)[:, None]
    AR = (sqR[:, None, :]*L[:, :, 10:]).transpose(0, 2, 1).reshape(-1, nb)
    QR = AR.T@AR
    cgb_rel = float(np.linalg.norm(QW-QR)/np.linalg.norm(QR))
    # Ric0-form W^- quadratic term (no-corrector) for comparison with step49 (20.35-14.75 = 5.6)
    bR = (sqR*S[:, 10:]).reshape(-1)
    res_out = dict(ANG=ANG, NS=NS, NXI=NXI, nbasis=nb, checks=checks,
                   S_W_norm2_over_8pi2=norm2, kappa=kappa, rank=int(rk),
                   coupling_to_SU2_diag_modes=coup_diag,
                   cgb_block_rel_diff=cgb_rel,
                   Ric0form_SW_norm2_over_8pi2=float(bR@bR)/(8*np.pi**2),
                   min_sol_norm=float(np.linalg.norm(sol)))
    print(json.dumps(res_out, indent=1), flush=True)
    json.dump(res_out, open(os.path.join(OUT, f"wminus_compat_A{ANG}.json"), "w"), indent=1)
    np.savez(os.path.join(OUT, f"wminus_compat_A{ANG}.npz"), sol=sol, pts=pts, wts=wts, S=S, QW=QW, QR=QR)

if __name__ == "__main__":
    main()
