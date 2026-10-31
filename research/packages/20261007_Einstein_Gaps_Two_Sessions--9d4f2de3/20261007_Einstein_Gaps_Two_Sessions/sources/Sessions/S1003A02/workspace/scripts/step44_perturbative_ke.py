"""Step 44: pointwise (cover-independent) coercivity constants at a complex-hyperbolic
Kähler-Einstein surface, and the s*-pocket refinement of AKGamma.

Output: workspace/data/step44_perturbative_ke.json

Part 1. CH^2 with holomorphic sectional curvature c=-4 (Ric=-6g, s=-24).
   Rm(X,Y,Z,W)=(c/4)[g(X,Z)g(Y,W)-g(X,W)g(Y,Z)+g(X,JZ)g(Y,JW)-g(X,JW)g(Y,JZ)+2g(X,JY)g(Z,JW)]
   convention Rm(a,b,a,b)=K(a,b).  (Rh)_{ij}=Rm_{ikjl}h_{kl}  (sphere: Rh=-h on trace-free).
   Einstein operator on TT: L_E=nabla*nabla-2R.  Koiso Bochner (TT, Ric=lam g):
       <L_E h,h> = ||d^nabla h||^2 + <(-lam-R)h,h>  >= (-lam-a)||h||^2,  a=max spec(R|S^2_0).
   Sanity: real hyperbolic K=-1, n=4: a=1, -lam=3 -> gap 2 (rigid for n>=3).
Part 2. Clifford model of the linearized SW operator at a parallel spinor Phi0 with |Phi0|^2=-s,
   c(F+)=(Phi0 Phi0^*)_0.  Checks (i) the first-order cross terms of ||L(a,psi)||^2 cancel
   (symbol level, so exact when nabla Phi0=0) for the correct gauge coefficient, (ii) the
   zeroth-order potential on (alpha, psi_par, psi_perp).
Part 3. Two-region Jensen minimisation for the AKGamma density with a pocket {s*>=0}.
"""
import json, itertools, os
import numpy as np
import sympy as sp

out = {}
# ---------------- Part 1 ----------------
n = 4
g = np.eye(n)
J = np.zeros((n, n)); J[1, 0] = 1; J[0, 1] = -1; J[3, 2] = 1; J[2, 3] = -1  # J e0=e1, J e2=e3
def gJ(X, Y):  # g(X,JY)
    return X @ (J @ Y)
E = np.eye(n)
def Rm_space(c, kind):
    R = np.zeros((n, n, n, n))
    for a, b, cc, d in itertools.product(range(n), repeat=4):
        X, Y, Z, W = E[a], E[b], E[cc], E[d]
        val = X @ Z * (Y @ W) - X @ W * (Y @ Z)
        if kind == 'complex':
            val += gJ(X, Z) * gJ(Y, W) - gJ(X, W) * gJ(Y, Z) + 2 * gJ(X, Y) * gJ(Z, W)
            val *= c / 4
        else:
            val *= c
        R[a, b, cc, d] = val
    return R
def analyse(R):
    Ric = np.einsum('kikj->ij', R)  # Ric(Y,W)=sum_k Rm(e_k,Y,e_k,W)
    # basis of S^2_0
    basis = []
    for i in range(n):
        for j in range(i, n):
            h = np.zeros((n, n)); h[i, j] = h[j, i] = 1; basis.append(h)
    B = np.array([h.flatten() for h in basis]).T
    # orthonormal basis of trace-free symmetric
    P = np.eye(n * n) - np.outer(g.flatten(), g.flatten()) / n
    Q, _ = np.linalg.qr(P @ B)
    # keep 9 independent
    U, S, Vt = np.linalg.svd(P @ B); TF = U[:, :9]
    def Rcirc(hv):
        h = hv.reshape(n, n)
        return np.einsum('ikjl,kl->ij', R, h).flatten()
    M = np.array([[TF[:, a] @ Rcirc(TF[:, b]) for b in range(9)] for a in range(9)])
    return Ric, TF, M
for kind, c in [('real', -1.0), ('complex', -4.0)]:
    R = Rm_space(c, kind)
    Ric, TF, M = analyse(R)
    lam = Ric[0, 0]
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    rec = dict(lambda_einstein=float(lam), ricci_is_einstein=bool(np.allclose(Ric, lam * g)),
               Rcirc_spectrum_tracefree=[round(float(x), 10) for x in sorted(ev)],
               a_max=float(max(ev)), koiso_pointwise_gap=float(-lam - max(ev)))
    if kind == 'complex':
        # sectional curvature range and J-split
        secs = []
        rng = np.random.default_rng(0)
        for _ in range(4000):
            X, Y = rng.normal(size=4), rng.normal(size=4)
            area = (X @ X) * (Y @ Y) - (X @ Y) ** 2
            secs.append(np.einsum('abcd,a,b,c,d', R, X, Y, X, Y) / area)
        rec['sectional_range_sampled'] = [float(min(secs)), float(max(secs))]
        # J-invariant (h(J.,J.)=h) vs anti-invariant
        def Jact(hv):
            h = hv.reshape(n, n); return (J.T @ h @ J).flatten()
        JM = np.array([[TF[:, a] @ Jact(TF[:, b]) for b in range(9)] for a in range(9)])
        w, V = np.linalg.eigh((JM + JM.T) / 2)
        for sign, name in [(1, 'J_invariant'), (-1, 'J_anti')]:
            idx = [i for i in range(9) if abs(w[i] - sign) < 1e-8]
            Vs = V[:, idx]
            sub = Vs.T @ ((M + M.T) / 2) @ Vs
            rec[name] = dict(dim=len(idx), Rcirc_spec=[round(float(x), 10) for x in np.linalg.eigvalsh(sub)])
        # Hodge-type gap on J-invariant TT: L_E = Delta_L - 2 lam, Delta_L<->Delta_d>=0 => >= -2 lam
        rec['J_invariant_gap_from_Hodge'] = float(-2 * lam)
        rec['J_invariant_gap_from_Koiso'] = float(-lam - max(rec['J_invariant']['Rcirc_spec']))
        rec['J_anti_gap_from_Koiso'] = float(-lam - max(rec['J_anti']['Rcirc_spec']))
    out['part1_' + kind + '_hyperbolic'] = rec

# ---------------- Part 2: Clifford model ----------------
I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2))
gam = [np.block([[Z2, -I2], [I2, Z2]]).astype(complex)] + [np.block([[Z2, 1j * s], [1j * s, Z2]]) for s in (sx, sy, sz)]
for i in range(4):
    for j in range(4):
        assert np.allclose(gam[i] @ gam[j] + gam[j] @ gam[i], -2 * (i == j) * np.eye(4))
def cform(F):  # F antisymmetric 4x4 real (or complex), c(F)=sum_{i<j} F_ij g_i g_j
    return sum(F[i, j] * gam[i] @ gam[j] for i in range(4) for j in range(i + 1, 4))
# self-dual basis (orientation e0123): e01+e23, e02+e31, e03+e12, normalised |eta|=1
def two(i, j):
    F = np.zeros((4, 4)); F[i, j] = 1; F[j, i] = -1; return F
SD = [(two(0, 1) + two(2, 3)) / np.sqrt(2), (two(0, 2) + two(3, 1)) / np.sqrt(2), (two(0, 3) + two(1, 2)) / np.sqrt(2)]
ASD = [(two(0, 1) - two(2, 3)) / np.sqrt(2), (two(0, 2) - two(3, 1)) / np.sqrt(2), (two(0, 3) - two(1, 2)) / np.sqrt(2)]
# find the block on which SD acts
blk_SD = [np.linalg.norm(cform(F)[:2, :2]) for F in SD]
plus = slice(0, 2) if min(blk_SD) > 1e-9 else slice(2, 4)
minus = slice(2, 4) if plus == slice(0, 2) else slice(0, 2)
cSD = [cform(F)[plus, plus] for F in SD]
hs_norm = [float(np.real(np.trace(C.conj().T @ C))) for C in cSD]
out['part2_clifford'] = dict(SD_acts_on_block='first' if plus == slice(0, 2) else 'second',
                             HS_norm_sq_of_c_unit_SD=hs_norm,
                             ASD_on_plus_norm=float(max(np.linalg.norm(cform(F)[plus, plus]) for F in ASD)))
def sd_from_herm(Hm):
    """Imag SD 2-form sigma with c(sigma)=Hm (traceless Hermitian on S+): sigma=i*tau, c(tau)=-i Hm."""
    coeff = []
    for C in cSD:  # C skew-Hermitian, <eta,tau>=-(1/4)tr(c eta c tau)
        coeff.append(float(np.real(-0.25 * np.trace(C @ (-1j * Hm)))))
    return np.array(coeff)  # components of tau in SD orthonormal basis
s_val = -4.0; lam = s_val / 4
Phi0 = np.array([np.sqrt(-s_val), 0], complex)
# check reconstruction
Hm0 = np.outer(Phi0, Phi0.conj()) - 0.5 * np.vdot(Phi0, Phi0).real * I2
t0 = sd_from_herm(Hm0)
rec_c = sum(t * C for t, C in zip(t0, cSD)) * 1j
out['part2_clifford']['sigma_reconstruct_err'] = float(np.linalg.norm(rec_c - Hm0))
out['part2_clifford']['|sigma(Phi0)|^2_vs_|Phi|^4/8'] = [float(t0 @ t0), float(abs(Phi0 @ Phi0.conj()) ** 2 / 8)]
# real coordinates: alpha in R^4 (a=i alpha), psi in C^2 ~ R^4
def psi_from(v): return np.array([v[0] + 1j * v[1], v[2] + 1j * v[3]])
# components of L as real vectors; derivative d_j applied to a field f is represented by symbol "index j"
# Build cross-term coefficient tensors: first-order part of L_a paired with zeroth-order of L_psi (M^j),
# zeroth-order of L_a paired with first-order of L_psi (N^j).  Need M^j == N^j for all j (then
# int dj(alpha) M psi - int alpha N dj psi = int dj(alpha)(M-N)psi = 0).
def L_a_first(alpha_deriv_j, j):
    """first-order part of L_a when only d_j alpha = alpha_deriv_j is nonzero: returns (gauge, SD-form(tau), spinor)"""
    A = np.zeros((4, 4)); A[j, :] = alpha_deriv_j  # A[j,mu]=d_j alpha_mu
    dstar = -np.trace(A)  # d^*alpha=-sum_j d_j alpha_j  (real), gauge comp = i*dstar
    dal = A - A.T  # (d alpha)_{j mu}=d_j alpha_mu - d_mu alpha_j
    tau = np.array([0.5 * np.sum(dal * F) for F in SD])  # <d alpha, F> with form inner product sum_{i<j}
    return dstar, tau
def L_psi_zero(psi, cg):
    gauge = cg * np.imag(np.vdot(Phi0, psi))
    Hm = np.outer(Phi0, psi.conj()) + np.outer(psi, Phi0.conj())
    Hm = Hm - 0.5 * np.real(np.trace(Hm)) * I2
    tau = sd_from_herm(Hm)  # sigma'(psi)=i tau
    return gauge, tau
def L_a_zero(alpha):
    cvec = sum(alpha[j] * gam[j] for j in range(4))
    return (0.5j * cvec @ np.concatenate([Phi0, [0, 0]]) if plus == slice(0, 2) else 0.5j * cvec @ np.concatenate([[0, 0], Phi0]))[minus]
def L_psi_first(psi, j):  # D psi with only d_j psi nonzero: c(e_j) psi
    full = np.zeros(4, complex); full[plus] = psi
    return (gam[j] @ full)[minus]
def cross_mismatch(cg, sign_sigma):
    worst = 0.0
    for j in range(4):
        Mj = np.zeros((4, 4)); Nj = np.zeros((4, 4))
        for mu in range(4):
            e = np.zeros(4); e[mu] = 1
            dst, tau_a = L_a_first(e, j)
            zero_a = L_a_zero(e)
            for nu in range(4):
                v = np.zeros(4); v[nu] = 1; psi = psi_from(v)
                gz, tau_p = L_psi_zero(psi, cg)
                # components: gauge (both imaginary -> product of real parts), form (d^+a - s*sigma'), spinor
                Mj[mu, nu] = dst * gz + tau_a @ (-sign_sigma * tau_p)
                Nj[mu, nu] = np.real(np.vdot(zero_a, L_psi_first(psi, j)))
        worst = max(worst, np.max(np.abs(Mj - Nj)))
    return worst
scan = {}
for sgn in (1, -1):
    for cg in (-2, -1, -0.5, 0.5, 1, 2):
        scan[f'sign_sigma={sgn},c_g={cg}'] = float(cross_mismatch(cg, sgn))
out['part2_clifford']['cross_term_mismatch_scan'] = scan
best = min(scan, key=scan.get)
out['part2_clifford']['cross_terms_cancel_for'] = best
# zeroth-order potential (pointwise), using best parameters
sgn = int(best.split(',')[0].split('=')[1]); cg = float(best.split(',')[1].split('=')[1])
def potential(alpha, v):
    psi = psi_from(v)
    # 1-form part: ||d*a||^2+||d+a||^2 >= (1/2)(||nabla a||^2 + lam ||a||^2): potential lam/2
    V = 0.5 * lam * alpha @ alpha
    V += np.linalg.norm(L_a_zero(alpha)) ** 2
    # Dirac^2 potential on S+: s/4 |psi|^2 + (1/2)<c(F+)psi,psi>, c(F+)=Hm0
    V += s_val / 4 * np.vdot(psi, psi).real + 0.5 * np.vdot(psi, Hm0 @ psi).real
    gz, tau_p = L_psi_zero(psi, cg)
    V += gz ** 2 + tau_p @ tau_p
    return V
Q = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        ei = np.zeros(8); ei[i] = 1; ej = np.zeros(8); ej[j] = 1
        Q[i, j] = 0.25 * (potential(*np.split(ei + ej, 2)) - potential(*np.split(ei - ej, 2)))
w = np.linalg.eigvalsh(Q)
out['part2_clifford']['potential_eigs_alpha4_psi4'] = [round(float(x), 10) for x in w]
out['part2_clifford']['normalisation'] = 's=-4, lam=-1, |Phi0|^2=4; psi_perp potential 0 is lifted by the Landau/Kodaira bound ||nabla psi_perp||^2>=|i Lambda F_perp| ||psi_perp||^2=2|lam| ||psi_perp||^2 on Lambda^{0,2}=K^{-1}'
out['part2_clifford']['uniform_SW_gap_lower_bound'] = 'min(|lam|/2, potentials on psi_par, 2|lam|) — see eigenvalues'

# ---------------- Part 3: pocket refinement ----------------
sig, de, phi, th = sp.symbols('sigma delta phi theta', positive=True)
G = (2 * sig ** 2 + (3 * de - 2 * sig) ** 2) / (192 * sp.pi ** 2)
x, y, d = sp.symbols('x y d', real=True)
Gq = (2 * x ** 2 + (3 * y - 2 * x) ** 2)
# min Gq s.t. y-x=D
D = sp.symbols('D', positive=True)
xs = sp.solve(sp.diff(Gq.subs(y, x + D), x), x)[0]
minval = sp.simplify(Gq.subs(y, x + D).subs(x, xs))
psi_ = phi / (1 - phi)
Gam_phi = 3 * th ** 2 - 2 * th + 1 + psi_ * (1 - th) ** 2
thopt = sp.solve(sp.diff(Gam_phi, th), th)[0]
out['part3_pocket'] = dict(
    min_quadratic_on_line_y_minus_x_eq_D=str(minval),
    pocket_excess_formula='C+ >= (l^2/128pi^2 V)[Gamma(theta)+ (phi/(1-phi))(1-theta)_+^2],  phi=Vol{s*>=0}/V',
    theta_opt=str(sp.simplify(thopt)),
    min_over_theta=str(sp.simplify(Gam_phi.subs(th, thopt))),
    check_phi0=str(sp.simplify(Gam_phi.subs(th, thopt).subs(phi, 0))),
)
# numerical brute-force check of two-region optimum
rng = np.random.default_rng(1)
def two_region_min(phiv, sbar, dbar):
    best = 1e9
    for _ in range(20000):
        s1 = rng.uniform(0, 4 * sbar); d1 = s1 + rng.uniform(0, 3 * sbar)  # pocket: delta>=sigma
        s2 = (sbar - phiv * s1) / (1 - phiv); d2 = (dbar - phiv * d1) / (1 - phiv)
        val = phiv * (2 * s1 ** 2 + (3 * d1 - 2 * s1) ** 2) + (1 - phiv) * (2 * s2 ** 2 + (3 * d2 - 2 * s2) ** 2)
        best = min(best, val)
    return best
chk = []
for phiv, sbar, dbar in [(0.1, 4, 2), (0.3, 4, 1), (0.05, 4, 3)]:
    num = two_region_min(phiv, sbar, dbar)
    pred = (2 * sbar ** 2 + (3 * dbar - 2 * sbar) ** 2) + phiv / (1 - phiv) * 6 * max(sbar - dbar, 0) ** 2
    chk.append(dict(phi=phiv, sigma_bar=sbar, delta_bar=dbar, sampled_min=num, formula=pred))
out['part3_pocket']['bruteforce_two_region_check_(units_192pi^2)'] = chk

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step44_perturbative_ke.json')
json.dump(out, open(path, 'w'), indent=1)
print(json.dumps(out, indent=1))
