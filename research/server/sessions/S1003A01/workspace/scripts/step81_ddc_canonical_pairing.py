"""Step 81: the exact two-form Theta_u = d d^c u paired with the closed canonical
curvature forms gamma and beta = gamma - (s/4) omega, tested on the complete
Bianchi-VIII strict AKE model (Ric=-3g, s=-12).

General predictions (derived in workspace/notes/step81_normalized_sections_and_ddc_canonical_pairing.md):
  (P1) Theta_u ^ omega = (Delta u) dV                       (any almost-Kahler 4-manifold)
  (P2) Theta_u^{(2,0)+(0,2)} = sqrt2 Re( alpha(grad u) psi )   (Nijenhuis part, first order)
  (P3) gamma^+ = (s/4+q/8) omega + sqrt2 Re(conj(eta) psi),  |gamma^-|^2 = q^2/32
  (P4) beta^{1,1} = (q/8)omega + gamma^- has rank one; its null J-line is the
       torsion line span(Re alpha^#, Im alpha^#)
  (P5) Theta_u ^ beta = (q/8) Delta u + 2<du,X> - <Theta^-,gamma^->,  X = Re(eta alpha)
  (I)  for every u:  int <Theta_u^-,gamma^-> = int <du, 2X - dq/8>
       with u = log(q+eps):  int <Theta^-,gamma^-> = int (2q|eta|^2 - 4|Y|^2)/(q+eps),
       |Y|^2 = |dq-8X|^2/32.
Usage: python step81_ddc_canonical_pairing.py [points|integrals]
Output: workspace/data/step81/ddc_points.json, ddc_integrals.json
"""
import json, os, sys
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import step79_dW_components_bianchiVIII as B

mp.mp.dps = 30
I = mp.mpc(0, 1)
S = mp.mpf(-12)
SQ2 = mp.sqrt(2)


def qf(p):
    return 36*(1-p**2)**3/(1+3*p**2)**3


def eta2_exact(p):
    return 9*(1-p*p)**3*(9*p*p-1)/(3*p*p+1)**4


p0 = mp.mpf('0.5')
_u1, _u2, _u3 = B.frame_forms(p0)
_om = _u1*SQ2
_psi = _u2 + I*_u3
S3 = 1 if mp.norm((-_om).T*_psi - I*_psi) < 1e-20 else -1


def fr(pp):
    return B.frame_forms(pp, S3)


def conn(pp):
    u1, u2, u3 = fr(pp)
    nab = [[B.cov2(lambda z, k=k: fr(z)[k], pp, a) for k in range(2)] for a in range(4)]
    alpha = [B.ip2(nab[a][0], u2) - I*B.ip2(nab[a][0], u3) for a in range(4)]
    b = [B.ip2(nab[a][1], u3) for a in range(4)]
    return alpha, b


def asd_basis():
    out = []
    for i, (j, k) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
        F = mp.matrix(4, 4); F[0, i] = 1; F[i, 0] = -1; F[j, k] = -1; F[k, j] = 1
        out.append(F/SQ2)
    return out


def wedge22(F, H):
    return (F[0, 1]*H[2, 3] - F[0, 2]*H[1, 3] + F[0, 3]*H[1, 2]
            + F[1, 2]*H[0, 3] - F[1, 3]*H[0, 2] + F[2, 3]*H[0, 1])


def analyse(p, eps):
    u1, u2, u3 = fr(p); om = u1*SQ2; psi = u2 + I*u3
    alpha, b = conn(p)
    c = B.cstruct(p)
    q = qf(p)
    # gamma = -db
    db0 = [mp.diff(lambda z, k=k: conn(z)[1][k], p)/mp.sqrt(B.G(p)) for k in range(4)]
    db = mp.matrix(4, 4)
    for a in range(4):
        for bb in range(4):
            db[a, bb] = (db0[bb] if a == 0 else 0) - (db0[a] if bb == 0 else 0) - sum(c[a][bb][e]*b[e] for e in range(4))
    gam = -db
    beta = gam - (S/4)*om
    # u = log(q+eps), radial
    uf = lambda z: mp.log(qf(z)+eps)
    du0 = B.E0(uf, p)
    du = [du0, 0, 0, 0]
    def dcu(z):
        o = fr(z)[0]*SQ2
        d0 = mp.diff(uf, z)/mp.sqrt(B.G(z))
        return [-o[a, 0]*d0 for a in range(4)]
    dc = dcu(p)
    dc0 = [mp.diff(lambda z, k=k: dcu(z)[k], p)/mp.sqrt(B.G(p)) for k in range(4)]
    Th = mp.matrix(4, 4)
    for a in range(4):
        for bb in range(4):
            Th[a, bb] = (dc0[bb] if a == 0 else 0) - (dc0[a] if bb == 0 else 0) - sum(c[a][bb][e]*dc[e] for e in range(4))
    # Laplacian of u
    volf = lambda z: mp.sqrt(B.A(z)[0]*B.A(z)[1]*B.A(z)[2])
    lap = mp.diff(lambda z: volf(z)/mp.sqrt(B.G(z))*mp.diff(uf, z), p)/(volf(p)*mp.sqrt(B.G(p)))
    # (P2)
    a_ = sum(alpha[k]*du[k] for k in range(4))
    P2 = [B.ip2(Th, u2) - SQ2*mp.re(a_), B.ip2(Th, u3) + SQ2*mp.im(a_)]
    # (P3)
    eta = (B.ip2(gam, u2) + I*B.ip2(gam, u3))/SQ2
    gtr = B.ip2(gam, om)/2
    W = asd_basis()
    gm = [B.ip2(gam, w) for w in W]; tm = [B.ip2(Th, w) for w in W]
    gm2 = sum(z**2 for z in gm)
    Thm_gm = sum(x*y for x, y in zip(tm, gm))
    # X and Y
    X = [mp.re(eta*alpha[k]) for k in range(4)]
    dq0 = mp.diff(qf, p)/mp.sqrt(B.G(p)); dq = [dq0, 0, 0, 0]
    Y2 = sum((dq[k]-8*X[k])**2 for k in range(4))/32
    duX = sum(du[k]*X[k] for k in range(4))
    # (P5)
    wedge = wedge22(Th, beta)
    P5 = wedge - ((q/8)*lap + 2*duX - Thm_gm)
    # (P4): J-invariant part of beta and its J-lines
    J = -om  # (J v)_b = sum_a v_a om_ab ; matrix acting v -> v^T om
    def Jv(v):
        return [sum(v[a]*om[a, bb] for a in range(4)) for bb in range(4)]
    def form(F, x, y):
        return sum(F[a, bb]*x[a]*y[bb] for a in range(4) for bb in range(4))
    ra = [mp.re(z) for z in alpha]; ia = [mp.im(z) for z in alpha]
    na = mp.sqrt(sum(z**2 for z in ra))
    e1 = [z/na for z in ra]; Je1 = Jv(e1)
    # orthonormal complement J-line
    basis = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    def gs(vs, w):
        w = [mp.mpf(z) for z in w]
        for v in vs:
            cpl = sum(x*y for x, y in zip(v, w)); w = [x-cpl*y for x, y in zip(w, v)]
        n = mp.sqrt(sum(z**2 for z in w)); return [z/n for z in w], n
    best = None
    for w in basis:
        e2, n = gs([e1, Je1], w)
        if best is None or n > best[1]:
            best = (e2, n)
    e2 = best[0]; Je2 = Jv(e2)
    beta_tor = form(beta, e1, Je1); beta_oth = form(beta, e2, Je2)
    L_tor = form(Th, e1, Je1); L_oth = form(Th, e2, Je2)
    # alignment of Im alpha with J Re alpha
    ia_vs_J = mp.sqrt(sum((x - y*na)**2 for x, y in zip(ia, Je1))) if na > 0 else 0
    ia_vs_mJ = mp.sqrt(sum((x + y*na)**2 for x, y in zip(ia, Je1))) if na > 0 else 0
    return dict(p=p, q=q, lap=lap, P1=B.ip2(Th, om)-lap, P2=max(abs(z) for z in P2),
                gtr=gtr, gtr_pred=S/4+q/8, eta=eta, eta2=abs(eta)**2, eta2_exact=eta2_exact(p),
                gm2=gm2, gm2_pred=q**2/32, P5=P5, wedge=wedge, Thm_gm=Thm_gm, duX=duX, Y2=Y2,
                beta_tor=beta_tor, beta_oth=beta_oth, beta_oth_pred=q/4, L_tor=L_tor, L_oth=L_oth,
                Imalpha_eq_J_Realpha=ia_vs_J, Imalpha_eq_mJ_Realpha=ia_vs_mJ,
                anis_pred=(q/8)*(L_oth-L_tor), dq0=dq0,
                vol=volf(p), sqrtG=mp.sqrt(B.G(p)))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'data', 'step81'); os.makedirs(outdir, exist_ok=True)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'points'
    if mode == 'points':
        rows = []
        for ps in ['0.4', '0.5', '0.6', '0.75', '0.9']:
            for es in ['1e-2', '0']:
                d = analyse(mp.mpf(ps), mp.mpf(es))
                row = {k: mp.nstr(v, 14) for k, v in d.items()}; row['eps'] = es
                rows.append(row)
                print({k: row[k] for k in ['p', 'eps', 'P1', 'P2', 'gtr', 'gtr_pred', 'eta2', 'eta2_exact', 'gm2', 'gm2_pred', 'P5',
                                           'beta_tor', 'beta_oth', 'beta_oth_pred', 'L_tor', 'L_oth', 'Thm_gm', 'anis_pred',
                                           'Imalpha_eq_J_Realpha', 'Imalpha_eq_mJ_Realpha']}, flush=True)
        json.dump({'s3': S3, 'rows': rows}, open(os.path.join(outdir, 'ddc_points.json'), 'w'), indent=1)
        return
    if mode == 'integrals':
        import numpy as np
        order = int(sys.argv[2]) if len(sys.argv) > 2 else 12
        umax = int(sys.argv[3]) if len(sys.argv) > 3 else 16
        epss = [mp.mpf(z) for z in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['1e-1', '1e-2', '1e-4'])]
        zz, ww = np.polynomial.legendre.leggauss(order)
        res = {}
        for eps in epss:
            tot = {k: mp.mpf(0) for k in ['Thm_gm', 'rhs_I', 'wedge', 'qLtor', 'qLoth', 'lapq8', 'duX2', 'gradq_over_h']}
            for kseg in range(umax):
                for zf, wf in zip(zz, ww):
                    u = kseg + (1+mp.mpf(float(zf)))/2; wg = mp.mpf(float(wf))/2
                    x = 1-mp.exp(-u); p = mp.mpf(1)/3+mp.mpf(2)/3*x*x; jac = mp.mpf(4)/3*x*mp.exp(-u)
                    d = analyse(p, eps)
                    meas = d['vol']*d['sqrtG']*jac*wg
                    h = d['q']+eps
                    vals = dict(Thm_gm=d['Thm_gm'], rhs_I=(2*d['q']*d['eta2']-4*d['Y2'])/h, wedge=d['wedge'],
                                qLtor=d['q']*d['L_tor']/8, qLoth=d['q']*d['L_oth']/8, lapq8=d['q']*d['lap']/8,
                                duX2=2*d['duX'], gradq_over_h=d['dq0']**2/h)
                    for k in tot:
                        tot[k] += mp.re(vals[k])*meas
            row = {k: mp.nstr(v, 14) for k, v in tot.items()}
            row['identity_I_residual'] = mp.nstr(tot['Thm_gm']-tot['rhs_I'], 8)
            row['int_wedge_beta'] = mp.nstr(tot['wedge'], 8)
            res[mp.nstr(eps, 3)] = row
            print(mp.nstr(eps, 3), row, flush=True)
        json.dump({'order': order, 'umax': umax, 'results': res}, open(os.path.join(outdir, 'ddc_integrals.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
