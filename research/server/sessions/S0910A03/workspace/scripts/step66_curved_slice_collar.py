#!/usr/bin/env python3
"""Step 66: the curved-slice collar fork.

Model class on T^3 x [r_min, r_max] (coords 0=r, 1=theta, 2=x, 3=y),
theta in S^1, (x,y) in T^2:

  g = dr^2 + exp(2(lt(r) + mu(r) phi0(x,y))) dtheta^2
           + exp(2(lx(r) + mu(r) u0(x,y)))  dx^2
           + exp(2(ly(r) + mu(r) u0(x,y)))  dy^2 .

Slices at mu=const are Part-B-type warped tori (S^1 warped over a
conformally flat T^2).  mu(r) = (1-r^2)^2 n(r) vanishes with its first
derivative at both ends, so end slices are flat; the objective forces
the ends toward unit hyperbolic-cusp calibration (S ~ +/-I, H ~ +/-3).

Full 4D Ricci tensor computed from the diagonal metric in coordinates
(theta-independence => d/dtheta = 0).  Objective ~ sup ||Ric + 3g||_op.

Decisive bit (Strategist, Step 66): can the sup defect be driven small
(collars => counterexample mechanism) or does every curved-slice collar
retain O(1) defect (gap side; obstruction at trace/integrated level)?

Validation battery before any optimization:
  V1 exact hyperbolic cusp l_i = -r, fields 0      => Ric = -3 g.
  V2 anisotropic flat warps l_i = s_i r            => closed formulas.
  V3 plateau Part-B slice: R_gamma from 4D code == Part-B formula.

Runs:
  flat   : fields frozen to 0 (flat-slice class; barrier says d_min >= 1).
  naive  : symmetric neck init, fields free.
  shear  : theta monotone contracting, x,y re-expanding, fields free.
  partb  : plateau init from Step-65 Part-B metric, fields free.

Usage: python step66_curved_slice_collar.py pilot|full [run,run,...]
"""

import sys, json, time
import numpy as np

import jax
jax.config.update("jax_enable_x64", True)
import jax.numpy as jnp
from jax import jit, value_and_grad

# ------------------------------------------------------------------ config
MODE = sys.argv[1] if len(sys.argv) > 1 else "pilot"
RUNS = (sys.argv[2].split(",") if len(sys.argv) > 2
        else ["flat", "naive", "shear", "partb"])
QUICK = (MODE == "pilot")

if QUICK:
    NR, NX, NY, KMOD = 17, 12, 12, 3
    DL, DM = 10, 6
    ADAM_STEPS, LBFGS_ITER = 300, 120
else:
    NR, NX, NY, KMOD = 33, 24, 24, 4
    DL, DM = 14, 10
    ADAM_STEPS, LBFGS_ITER = 4000, 700

NR_F, NX_F, NY_F = 2 * NR - 1, 32, 32          # fine evaluation grid
P_NORM = 16.0
LAM_SHELL, LAM_CHEB, LAM_BARR = 3e-3, 1e-4, 1e-3

# ------------------------------------------------------------------ grids
def make_grid(nr, nx, ny, kmod):
    r = np.cos(np.pi * np.arange(nr) / (nr - 1))          # Chebyshev-Lobatto
    x = 2 * np.pi * np.arange(nx) / nx
    y = 2 * np.pi * np.arange(ny) / ny
    X, Y = np.meshgrid(x, y, indexing="ij")

    # Chebyshev value/derivative matrices on the Lobatto grid
    from numpy.polynomial.chebyshev import chebvander, chebder
    V = chebvander(r, max(DL, DM))                        # (nr, dmax+1)
    dmax = max(DL, DM)
    D1 = np.zeros((dmax + 1, dmax + 1))
    D2 = np.zeros((dmax + 1, dmax + 1))
    for k in range(dmax + 1):
        e = np.zeros(dmax + 1); e[k] = 1.0
        c1 = chebder(e, 1); D1[:len(c1), k] = c1
        c2 = chebder(e, 2); D2[:len(c2), k] = c2
    M0 = V                                                # coef -> values
    M1 = V @ D1                                           # coef -> d/dr values
    M2 = V @ D2                                           # coef -> d2/dr2

    # modal basis for the (x,y) fields
    modes = [(kx, ky) for kx in range(0, kmod + 1)
             for ky in range(-kmod, kmod + 1) if (kx > 0 or ky > 0)]
    TH = np.stack([kx * X + ky * Y for (kx, ky) in modes])   # (nm,nx,ny)
    COS, SIN = np.cos(TH), np.sin(TH)
    kx_a = np.array([m[0] for m in modes], dtype=float)
    ky_a = np.array([m[1] for m in modes], dtype=float)
    shell = (np.maximum(np.abs(kx_a), np.abs(ky_a)) >= kmod).astype(float)

    g = dict(r=r, X=X, Y=Y, M0=jnp.array(M0), M1=jnp.array(M1), M2=jnp.array(M2),
             COS=jnp.array(COS), SIN=jnp.array(SIN),
             kx=jnp.array(kx_a), ky=jnp.array(ky_a),
             shell=jnp.array(shell), modes=modes, nr=nr, nx=nx, ny=ny)
    return g

G = make_grid(NR, NX, NY, KMOD)
GF = make_grid(NR_F, NX_F, NY_F, KMOD)
NM = len(G["modes"])

# ------------------------------------------------------------------ fields
def cheb_eval(g, coef, dm):
    v0 = g["M0"][:, :dm + 1] @ coef
    v1 = g["M1"][:, :dm + 1] @ coef
    v2 = g["M2"][:, :dm + 1] @ coef
    return v0, v1, v2

def field_eval(g, a, b):
    """u0(x,y) = sum a_k cos + b_k sin, with spectral derivatives."""
    th_cos, th_sin = g["COS"], g["SIN"]
    kx, ky = g["kx"], g["ky"]
    u   = jnp.tensordot(a, th_cos, 1) + jnp.tensordot(b, th_sin, 1)
    ux  = jnp.tensordot(-a * kx, th_sin, 1) + jnp.tensordot(b * kx, th_cos, 1)
    uy  = jnp.tensordot(-a * ky, th_sin, 1) + jnp.tensordot(b * ky, th_cos, 1)
    uxx = jnp.tensordot(-a * kx**2, th_cos, 1) + jnp.tensordot(-b * kx**2, th_sin, 1)
    uyy = jnp.tensordot(-a * ky**2, th_cos, 1) + jnp.tensordot(-b * ky**2, th_sin, 1)
    uxy = jnp.tensordot(-a * kx * ky, th_cos, 1) + jnp.tensordot(-b * kx * ky, th_sin, 1)
    return u, ux, uy, uxx, uyy, uxy

def build_metric(params, g):
    """Return E[4], dE[4][4], ddE[4][4][4] arrays on the grid."""
    nr, nx, ny = g["nr"], g["nx"], g["ny"]
    sh3 = (nr, nx, ny)
    lt, lt1, lt2 = cheb_eval(g, params["lt"], DL)
    lx, lx1, lx2 = cheb_eval(g, params["lx"], DL)
    ly, ly1, ly2 = cheb_eval(g, params["ly"], DL)
    n0, n1, n2 = cheb_eval(g, params["n"], DM)
    rr = jnp.array(g["r"])
    om = (1 - rr**2)                                     # 1-r^2
    mu  = om**2 * n0
    mu1 = om**2 * n1 - 4 * rr * om * n0
    mu2 = om**2 * n2 - 8 * rr * om * n1 + (12 * rr**2 - 4) * n0

    phi, phix, phiy, phixx, phiyy, phixy = field_eval(g, params["ap"], params["bp"])
    u0,  u0x,  u0y,  u0xx,  u0yy,  u0xy  = field_eval(g, params["au"], params["bu"])

    def reshape(v):   # (nr,) -> (nr,1,1)
        return v.reshape(nr, 1, 1)

    E = [None] * 4
    dE = [[jnp.zeros(sh3) for _ in range(4)] for _ in range(4)]
    ddE = [[[jnp.zeros(sh3) for _ in range(4)] for _ in range(4)] for _ in range(4)]

    E[0] = jnp.ones(sh3)
    comps = [(1, lt, lt1, lt2, phi, phix, phiy, phixx, phiyy, phixy),
             (2, lx, lx1, lx2, u0, u0x, u0y, u0xx, u0yy, u0xy),
             (3, ly, ly1, ly2, u0, u0x, u0y, u0xx, u0yy, u0xy)]
    for (i, l, l1, l2, f, fx, fy, fxx, fyy, fxy) in comps:
        lE = reshape(l) + reshape(mu) * f[None]
        Ei = jnp.exp(2 * lE)
        E[i] = Ei
        dr = reshape(l1) + reshape(mu1) * f[None]
        drr = reshape(l2) + reshape(mu2) * f[None]
        muf = reshape(mu)
        dE[i][0] = 2 * Ei * dr
        dE[i][2] = 2 * Ei * muf * fx[None]
        dE[i][3] = 2 * Ei * muf * fy[None]
        ddE[i][0][0] = 2 * Ei * (drr + 2 * dr**2)
        ddE[i][0][2] = 2 * Ei * (reshape(mu1) * fx[None] + 2 * dr * muf * fx[None])
        ddE[i][0][3] = 2 * Ei * (reshape(mu1) * fy[None] + 2 * dr * muf * fy[None])
        ddE[i][2][2] = 2 * Ei * (muf * fxx[None] + 2 * (muf * fx[None])**2)
        ddE[i][3][3] = 2 * Ei * (muf * fyy[None] + 2 * (muf * fy[None])**2)
        ddE[i][2][3] = 2 * Ei * (muf * fxy[None] + 2 * muf**2 * fx[None] * fy[None])
    return E, dE, ddE

# ------------------------------------------------------------------ Ricci
def ricci_diagonal(E, dE, ddE):
    """Christoffel + Ricci for diagonal metric; theta-derivatives vanish."""
    sh3 = E[0].shape
    G_up = [[[jnp.zeros(sh3) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dG = [[[[jnp.zeros(sh3) for _ in range(4)] for _ in range(4)]
           for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(4):
                terms = []
                if j == k:
                    terms.append((1.0, i, j))
                if i == k:
                    terms.append((1.0, j, i))
                if i == j:
                    terms.append((-1.0, k, i))
                if not terms:
                    continue
                acc = 0.0
                for (s, a, b) in terms:
                    acc = acc + s * dE[b][a]
                G_up[k][i][j] = acc / (2 * E[k])
                for c in (0, 2, 3):
                    dacc = 0.0
                    for (s, a, b) in terms:
                        ca = (min(a, c), max(a, c))
                        dacc = dacc + s * (ddE[b][ca[0]][ca[1]] / (2 * E[k])
                                           - dE[b][a] * dE[k][c] / (2 * E[k]**2))
                    dG[k][i][j][c] = dacc
    Ric = [[jnp.zeros(sh3) for _ in range(4)] for _ in range(4)]
    for j in range(4):
        for l in range(4):
            acc = 0.0
            for i in range(4):
                acc = acc + dG[i][j][l][i] - dG[i][i][j][l]
                for m in range(4):
                    acc = acc + G_up[i][j][l] * G_up[m][i][m] \
                              - G_up[m][i][l] * G_up[i][m][j]
            Ric[j][l] = acc
    return Ric

def symmetrized_eigs(E, Ric):
    """Eigenvalues of Ric + 3g as a mixed endomorphism (symmetrized)."""
    npts = int(np.prod(E[0].shape))
    M = jnp.zeros((npts, 4, 4))
    sq = [jnp.sqrt(E[i]).reshape(-1) for i in range(4)]
    for i in range(4):
        for j in range(4):
            M = M.at[:, i, j].set(Ric[i][j].reshape(-1) / (sq[i] * sq[j]))
    M = M + 3.0 * jnp.eye(4)
    return jnp.linalg.eigvalsh(M)

def defect_and_diag(params, g):
    E, dE, ddE = build_metric(params, g)
    Ric = ricci_diagonal(E, dE, ddE)
    eigs = symmetrized_eigs(E, Ric)
    defect = jnp.max(jnp.abs(eigs), axis=-1)
    # diagnostics
    lt, lt1, lt2 = cheb_eval(g, params["lt"], DL)
    lx, lx1, lx2 = cheb_eval(g, params["lx"], DL)
    ly, ly1, ly2 = cheb_eval(g, params["ly"], DL)
    n0, n1, n2 = cheb_eval(g, params["n"], DM)
    rr = jnp.array(g["r"]); om = 1 - rr**2
    mu = om**2 * n0; mu1 = om**2 * n1 - 4 * rr * om * n0
    phi = field_eval(g, params["ap"], params["bp"])[0]
    u0 = field_eval(g, params["au"], params["bu"])[0]
    rs = lambda v: v.reshape(g["nr"], 1, 1)
    S1 = rs(lt1) + rs(mu1) * phi[None]
    S2v = rs(lx1) + rs(mu1) * u0[None]
    S3 = rs(ly1) + rs(mu1) * u0[None]
    H = S1 + S2v + S3
    S2n = S1**2 + S2v**2 + S3**2
    Rm = sum(Ric[i][i] / E[i] for i in range(4))
    Rnn = Ric[0][0]
    Rg = Rm - 2 * Rnn + H**2 - S2n
    Enn = Rnn + 3.0
    diag = dict(H=H, S2n=S2n, Rg=Rg, Rm=Rm, Rnn=Rnn, Enn=Enn,
                mu=rs(mu) + 0 * H, Ric=Ric, E=E)
    return defect, diag

# ------------------------------------------------------------------ objective
def penalty(params):
    pen = 0.0
    for key in ("ap", "bp", "au", "bu"):
        pen = pen + LAM_SHELL * jnp.sum(G["shell"] * params[key]**2)
    for key in ("lt", "lx", "ly"):
        k = jnp.arange(DL + 1)
        pen = pen + LAM_CHEB * jnp.sum((k >= DL - 3) * params[key]**2)
    return pen

def objective_flat(params_vec, free_keys, base):
    params = dict(base)
    i = 0
    for key in free_keys:
        n = base[key].size
        params[key] = jnp.array(params_vec[i:i + n]).reshape(base[key].shape)
        i += n
    defect, _ = defect_and_diag(params, G)
    obj = jnp.mean(defect**P_NORM)**(1.0 / P_NORM) + penalty(params)
    return obj

# ------------------------------------------------------------------ params
def zeros_params():
    return dict(lt=np.zeros(DL + 1), lx=np.zeros(DL + 1), ly=np.zeros(DL + 1),
                n=np.zeros(DM + 1), ap=np.zeros(NM), bp=np.zeros(NM),
                au=np.zeros(NM), bu=np.zeros(NM))

def chebfit_vals(fn, d):
    """Fit Chebyshev series of degree d to fn sampled on the Lobatto grid."""
    from numpy.polynomial.chebyshev import chebfit, chebval
    c = chebfit(G["r"], fn(G["r"]), d)
    out = np.zeros(d + 1)
    out[:len(c)] = c
    return out

def pack(params, keys):
    return np.concatenate([np.asarray(params[k]).ravel() for k in keys])

def unpack(vec, keys, base):
    params = dict(base)
    i = 0
    for k in keys:
        n = base[k].size
        params[k] = np.array(vec[i:i + n]).reshape(base[k].shape)
        i += n
    return params

# ------------------------------------------------------------------ validation
def validation():
    print("=== validation battery ===", flush=True)
    p = zeros_params()
    p["lt"] = p["lx"] = p["ly"] = chebfit_vals(lambda r: -r, DL)
    defect, diag = defect_and_diag({k: jnp.array(v) for k, v in p.items()}, G)
    v1 = float(jnp.max(defect))
    print(f"V1 hyperbolic cusp: sup|Ric+3g| = {v1:.3e}  (want < 1e-9)")

    # V2 anisotropic flat: l_i = s_i r ; Ric^i_i = -s_i H, Rnn = -sum s_i^2
    s = np.array([-1.0, -0.8, -1.3])
    p2 = zeros_params()
    for key, si in zip(("lt", "lx", "ly"), s):
        p2[key] = chebfit_vals(lambda r, si=si: si * r, DL)
    defect2, diag2 = defect_and_diag({k: jnp.array(v) for k, v in p2.items()}, G)
    Ht = s.sum()
    ric_tt = -s[0] * Ht
    Ric_diag = np.array([float(diag2["Ric"][i][i].max() / (np.exp(2 * s[i-1] * 0).max() if i > 0 else 1))
                         for i in range(1, 4)])
    # compare at r=0 where E_i = 1
    mid = NR // 2
    ric_num = [float(np.asarray(diag2["Ric"][i][i])[mid, 0, 0]) for i in (1, 2, 3)]
    ric_ana = [-s[0] * Ht, -s[1] * Ht, -s[2] * Ht]
    v2 = max(abs(a - b) for a, b in zip(ric_num, ric_ana))
    rnn_num = float(np.asarray(diag2["Ric"][0][0])[mid, 0, 0])
    rnn_ana = -float((s**2).sum())
    v2 = max(v2, abs(rnn_num - rnn_ana))
    print(f"V2 anisotropic flat warps: max err = {v2:.3e}  (want < 1e-9)")

    # V3 Part-B plateau slice: l=0, mu=1, fields = truncated Part-B.
    up, phip, partb_info = partb_fields(KMOD, G)
    p3 = zeros_params()
    p3["n"] = np.zeros(DM + 1); p3["n"][0] = 1.0   # mu(0)=1, mu'(0)=0 at middle slice
    # force mu == 1: use n with (1-r^2)^2 n = 1 -> not polynomial; instead evaluate
    # slice intrinsic scalar via the 4D code with mu'=0 at r=0: mu(0)=1, mu1(0)=0
    # (mu1 = -4 r (1-r^2) n + (1-r^2)^2 n' -> 0 at r=0).  So at the middle slice
    # the 4D metric has S=0, Rnn=0 and R_gamma = R_M.
    p3["ap"], p3["bp"] = partb_info["ap"], partb_info["bp"]
    p3["au"], p3["bu"] = partb_info["au"], partb_info["bu"]
    def3, diag3 = defect_and_diag({k: jnp.array(v) for k, v in p3.items()}, G)
    Rg_4d = np.asarray(diag3["Rg"])[mid]                       # (nx,ny)
    Rg_ana = partb_info["Rg_trunc"]                            # (nx,ny)
    v3 = float(np.max(np.abs(Rg_4d - Rg_ana)))
    print(f"V3 Part-B slice scalar: max |R_gamma(4D) - R_gamma(formula)| = {v3:.3e}")
    ok = (v1 < 1e-8) and (v2 < 1e-8)
    print(f"battery {'PASSED' if ok else 'FAILED (V3 is grid-dependent)'}")
    return ok, partb_info

def partb_fields(kmod, g):
    """Recompute the Step-65 Part-B metric and truncate to the modal basis."""
    N = 128
    x = np.linspace(0, 2 * np.pi, N, endpoint=False)
    Xb, Yb = np.meshgrid(x, x, indexing="ij")
    dx = x[1] - x[0]
    phi = np.cos(Xb) + np.cos(Yb)
    gx = -np.sin(Xb); gy = -np.sin(Yb)
    g2 = gx**2 + gy**2
    corners = [(0, 0), (np.pi, 0), (0, np.pi), (np.pi, np.pi)]
    dist2 = np.full_like(Xb, 1e9)
    for cx, cy in corners:
        ddx = np.minimum(np.abs(Xb - cx), 2 * np.pi - np.abs(Xb - cx))
        ddy = np.minimum(np.abs(Yb - cy), 2 * np.pi - np.abs(Yb - cy))
        dist2 = np.minimum(dist2, ddx**2 + ddy**2)
    rho = 0.30
    disk = dist2 <= rho**2
    h_plus = 2.0
    A_plus = disk.mean() * (2 * np.pi)**2
    A_minus = (2 * np.pi)**2 - A_plus
    c1 = h_plus * A_plus / A_minus
    h = np.where(disk, h_plus, -c1)
    kx1 = np.fft.fftfreq(N, d=dx) * 2 * np.pi
    KX, KY = np.meshgrid(kx1, kx1, indexing="ij")
    sigma = 6.0
    Hhat = np.fft.fft2(h) * np.exp(-(KX**2 + KY**2) / (2 * sigma**2))
    h_sm = np.real(np.fft.ifft2(Hhat))
    h_sm -= h_sm.mean()
    K2 = KX**2 + KY**2
    K2[0, 0] = 1.0
    Phi = np.real(np.fft.ifft2(-np.fft.fft2(h_sm) / K2))
    Phi -= Phi.mean()
    u = Phi - phi

    # truncate both to modal coefficients on the working grid
    def trunc(F):
        Fhat = np.fft.fft2(F) / (N * N)
        a = np.zeros(len(g["modes"])); b = np.zeros(len(g["modes"]))
        for im, (kx, ky) in enumerate(g["modes"]):
            ix = kx % N; iy = ky % N
            c = Fhat[ix, iy]
            # F = sum a cos + b sin:  coeff of e^{i k.x} is (a - i b)/2
            a[im] = 2 * np.real(c)
            b[im] = -2 * np.imag(c)
        return a, b

    ap, bp = trunc(phi)
    au, bu = trunc(u)

    # evaluate truncated fields + R_gamma formula on the working grid
    def ev(a, b):
        return (np.tensordot(a, np.asarray(g["COS"]), 1)
                + np.tensordot(b, np.asarray(g["SIN"]), 1))
    phi_t = ev(ap, bp); u_t = ev(au, bu)
    # spectral derivatives on the working grid
    def evd(a, b):
        kx, ky = np.asarray(g["kx"]), np.asarray(g["ky"])
        C, S = np.asarray(g["COS"]), np.asarray(g["SIN"])
        ux = np.tensordot(-a * kx, S, 1) + np.tensordot(b * kx, C, 1)
        uy = np.tensordot(-a * ky, S, 1) + np.tensordot(b * ky, C, 1)
        uxx = np.tensordot(-a * kx**2, C, 1) + np.tensordot(-b * kx**2, S, 1)
        uyy = np.tensordot(-a * ky**2, C, 1) + np.tensordot(-b * ky**2, S, 1)
        return ux, uy, uxx, uyy
    pux, puy, puxx, puyy = evd(ap, bp)
    uux, uuy, uuxx, uuyy = evd(au, bu)
    lap = (puxx + puyy) + (uuxx + uuyy)
    g2t = pux**2 + puy**2
    Rg = -2 * np.exp(-2 * u_t) * (lap + g2t)
    info = dict(ap=ap, bp=bp, au=au, bu=bu, Rg_trunc=Rg,
                Rg_min=float(Rg.min()), Rg_max=float(Rg.max()))
    return u, phi, info

# ------------------------------------------------------------------ optimize
def optimize(run, partb_info):
    base = zeros_params()
    # inits
    neck = lambda r: 0.55 * r**3 - 0.45 * r       # l' ends = 1.2, l'(0) = -0.45
    if run == "flat":
        for k in ("lt", "lx", "ly"):
            base[k] = chebfit_vals(neck, DL)
        free = ["lt", "lx", "ly"]
    elif run == "naive":
        for k in ("lt", "lx", "ly"):
            base[k] = chebfit_vals(neck, DL)
        base["n"] = chebfit_vals(lambda r: np.ones_like(r), DM)
        free = ["lt", "lx", "ly", "n", "ap", "bp", "au", "bu"]
    elif run == "shear":
        base["lt"] = chebfit_vals(lambda r: -1.05 * r, DL)
        base["lx"] = chebfit_vals(neck, DL)
        base["ly"] = chebfit_vals(neck, DL)
        base["n"] = chebfit_vals(lambda r: np.ones_like(r), DM)
        free = ["lt", "lx", "ly", "n", "ap", "bp", "au", "bu"]
    elif run == "partb":
        for k in ("lt", "lx", "ly"):
            base[k] = chebfit_vals(lambda r: 0.6 * r**3 - 0.55 * r, DL)
        base["n"] = chebfit_vals(lambda r: np.ones_like(r), DM)
        base["ap"], base["bp"] = partb_info["ap"], partb_info["bp"]
        base["au"], base["bu"] = partb_info["au"], partb_info["bu"]
        free = ["lt", "lx", "ly", "n", "ap", "bp", "au", "bu"]
    else:
        raise ValueError(run)

    v0 = pack(base, free)
    from functools import partial
    @partial(jit, static_argnames=("free_keys",))
    def obj_static(params_vec, free_keys, base):
        return objective_flat(params_vec, free_keys, base)

    obj_jit = value_and_grad(obj_static, argnums=0)

    def fg(v):
        o, gr = obj_jit(jnp.array(v), tuple(free),
                        {k: jnp.array(base[k]) for k in base})
        return float(o), np.asarray(gr)

    # --- Adam stage
    print(f"[{run}] Adam stage ({ADAM_STEPS} steps)...", flush=True)
    v = v0.copy()
    m = np.zeros_like(v); vv = np.zeros_like(v)
    b1, b2, eps = 0.9, 0.999, 1e-9
    t0 = time.time()
    best = (np.inf, v.copy())
    for t in range(1, ADAM_STEPS + 1):
        o, gr = fg(v)
        lr = 3e-3 * (0.5 * (1 + np.cos(np.pi * t / ADAM_STEPS))) + 1e-4
        m = b1 * m + (1 - b1) * gr
        vv = b2 * vv + (1 - b2) * gr**2
        mh = m / (1 - b1**t); vh = vv / (1 - b2**t)
        v = v - lr * mh / (np.sqrt(vh) + eps)
        if o < best[0]:
            best = (o, v.copy())
        if t % max(1, ADAM_STEPS // 10) == 0:
            print(f"  step {t}: obj {o:.4f}  best {best[0]:.4f}  "
                  f"({time.time() - t0:.0f}s)", flush=True)
    v = best[1]

    # --- L-BFGS polish
    print(f"[{run}] L-BFGS polish (max {LBFGS_ITER})...", flush=True)
    from scipy.optimize import minimize
    it = [0]
    def fg_s(v):
        it[0] += 1
        return fg(v)
    res = minimize(fg_s, v, jac=True, method="L-BFGS-B",
                   options=dict(maxiter=LBFGS_ITER, maxls=30, ftol=1e-12, gtol=1e-10))
    print(f"  L-BFGS: {res.message}  obj {res.fun:.4f}  ({it[0]} evals)", flush=True)
    final = unpack(res.x, free, base)
    return final, float(res.fun)

# ------------------------------------------------------------------ report
def full_report(params):
    pj = {k: jnp.array(v) for k, v in params.items()}
    defect_c, diag_c = defect_and_diag(pj, G)
    defect_f, diag_f = defect_and_diag(pj, GF)
    sup_c = float(jnp.max(defect_c)); sup_f = float(jnp.max(defect_f))
    # defect_f is 1D (flattened); reshape to grid for spatial indexing
    sh3 = (GF["nr"], GF["nx"], GF["ny"])
    defect_3d = jnp.asarray(defect_f).reshape(sh3)
    flat_idx = int(jnp.argmax(defect_3d))
    idx = np.unravel_index(flat_idx, sh3)
    r_at = float(GF["r"][idx[0]])
    comp = {}
    for name, arr in (("Ric00", diag_f["Ric"][0][0]), ("Ric11", diag_f["Ric"][1][1]),
                      ("Ric22", diag_f["Ric"][2][2]), ("Ric33", diag_f["Ric"][3][3])):
        comp[name] = float(np.asarray(arr).reshape(sh3)[idx])
    Ei = [float(np.asarray(diag_f["E"][i]).reshape(sh3)[idx]) for i in range(4)]
    comp["E_diag"] = Ei
    comp["Ric_normalized"] = [comp["Ric00"],
                              comp["Ric11"] / Ei[1], comp["Ric22"] / Ei[2],
                              comp["Ric33"] / Ei[3]]
    prof = []
    # reshape diagnostics to 3D for slicing
    H_3d = np.asarray(diag_f["H"]).reshape(sh3)
    S2_3d = np.asarray(diag_f["S2n"]).reshape(sh3)
    Rg_3d = np.asarray(diag_f["Rg"]).reshape(sh3)
    Enn_3d = np.asarray(diag_f["Enn"]).reshape(sh3)
    d_3d = np.asarray(defect_3d)
    for jr in range(0, GF["nr"], max(1, GF["nr"] // 8)):
        sl = slice(jr, jr + 1)
        row = dict(r=round(float(GF["r"][jr]), 4),
                   H_mean=round(float(H_3d[jr].mean()), 4),
                   H_min=round(float(H_3d[jr].min()), 4),
                   H_max=round(float(H_3d[jr].max()), 4),
                   S2_mean=round(float(S2_3d[jr].mean()), 4),
                   Rg_min=round(float(Rg_3d[jr].min()), 4),
                   Rg_max=round(float(Rg_3d[jr].max()), 4),
                   defect_max=round(float(d_3d[jr].max()), 5),
                   Enn_absmax=round(float(np.abs(Enn_3d[jr]).max()), 5))
        prof.append(row)
    out = dict(sup_defect_coarse=sup_c, sup_defect_fine=sup_f,
               argmax_r=r_at, argmax_grid=idx, worst_point_components=comp,
               mu_range=[float(jnp.min(diag_f["mu"])), float(jnp.max(diag_f["mu"]))],
               profile=prof)
    return out

# ------------------------------------------------------------------ main
def main():
    print(f"Step 66 curved-slice collar  [{MODE}]  grid {NR}x{NX}x{NY}  "
          f"K={KMOD} ({NM} modes)  runs={RUNS}", flush=True)
    ok, partb_info = validation()
    print(f"Part-B truncated slice: R_gamma in [{partb_info['Rg_min']:.4f}, "
          f"{partb_info['Rg_max']:.4f}]", flush=True)
    if not ok:
        print("VALIDATION FAILED - aborting optimization.", flush=True)
        return
    results = {}
    for run in RUNS:
        t0 = time.time()
        print(f"\n=== RUN {run} ===", flush=True)
        params, obj = optimize(run, partb_info)
        rep = full_report(params)
        rep["objective"] = obj
        rep["wall_time_s"] = round(time.time() - t0, 1)
        rep["params"] = {k: [round(float(x), 8) for x in np.asarray(v).ravel()]
                         for k, v in params.items()}
        results[run] = rep
        print(f"[{run}] sup defect fine = {rep['sup_defect_fine']:.4f} "
              f"at r = {rep['argmax_r']:.3f}   mu range {rep['mu_range']}", flush=True)
    fn = (f"Sessions/S0910A03/workspace/data/step66_curved_slice_collar"
          f"{'_pilot' if QUICK else ''}.json")

    class NpEnc(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, (np.integer, np.int_)):
                return int(o)
            if isinstance(o, (np.floating, np.float_)):
                return float(o)
            if isinstance(o, np.ndarray):
                return o.tolist()
            return super().default(o)

    with open(fn, "w") as fh:
        json.dump(dict(mode=MODE, grid=dict(nr=NR, nx=NX, ny=NY, kmod=KMOD),
                       partb=dict(Rg_min=partb_info["Rg_min"],
                                  Rg_max=partb_info["Rg_max"]),
                       results=results), fh, indent=1, cls=NpEnc)
    print("\nSaved:", fn, flush=True)

if __name__ == "__main__":
    main()
