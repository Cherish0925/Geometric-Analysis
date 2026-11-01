"""Step 79: independent frame check of the complex delta W^+ = 0 system,
the |nabla W^+|^2 decomposition, the torsion structure equation and the
line-bundle Kodaira identities (with their end currents) on the complete
Bianchi-VIII strict almost-Kahler Einstein model (Ric=-3g, s=-12).

Conventions (Step-79 note):
  u1=Omega/sqrt2, psi=u2+i u3 chosen of type (2,0);
  nabla u1 = Re(alpha (x) psi), alpha=<nabla u1,u2>-i<nabla u1,u3> (type (1,0));
  nabla psi = -conj(alpha) u1 - i b psi,  b=<nabla u2,u3>;
  W u1 = r u1 + Re(conj(eta) psi), W psi = eta u1 - (r/2) psi + v conj(psi);
  D eta = d eta + i b eta,  D v = d v + 2 i b v.
Predicted (derived by hand in the note):
  (E1) d_D eta      = v alpha - i conj(eta) K(alpha) + i K(d r)
  (E2) conj(dbar_D eta) = -(3r/2) alpha - 2 i K(d_D v)
  |nabla W|^2 = 5|dr-eta alpha|^2+10|d_D v|^2+2|dbar_D v+eta conj(alpha)|^2
  (T)  d alpha - i b^alpha = -i sqrt2 [conj(eta) u1 - (q/8) conj(psi) + conj(v) psi]
  <db,omega> = -(2s+q)/4
  (Kv) |dbar v|^2-|d v|^2-(|s|-q/2)|v|^2 = i d(conj(v) Dv ^ omega)/dV
  (Keta) |dbar eta|^2-|d eta|^2-(|s|/2-q/4)|eta|^2 = i d(conj(eta) D eta ^ omega)/dV
Here d,dbar denote (1,0),(0,1) parts.  Output: data/step79/dW_check.json
"""
import json, os, itertools
import mpmath as mp

mp.mp.dps = 40
I = mp.mpc(0, 1)
S_SCAL = mp.mpf(-12)


def A(p):
    return [4*(3*p-1)*(3*p**2+1)/(3*(1-p)*(1+p)**2),
            4*(3*p+1)*(3*p**2+1)/(3*(1-p)**2*(1+p)),
            64*p**2/((1-p)*(1+p)*(3*p**2+1))]


def G(p):
    return 4*(3*p**2+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))


def X(p):
    return [(1-p)**3*(3*p+1)/(16*p**3), (1+p)**3*(3*p-1)/(16*p**3)]


def cstruct(p):
    """c[a][b][c] = <[E_a,E_b],E_c> for the orthonormal frame."""
    Av = A(p); g = G(p)
    c = [[[mp.mpf(0)]*4 for _ in range(4)] for _ in range(4)]
    for i in range(1, 4):
        Ai = lambda pp, i=i: A(pp)[i-1]
        dA = mp.diff(Ai, p)
        val = -dA/(2*Av[i-1]*mp.sqrt(g))
        c[0][i][i] = val; c[i][0][i] = -val
    sq = [mp.sqrt(z) for z in Av]
    # [xi2,xi3]=2xi1, [xi3,xi1]=-2xi2, [xi1,xi2]=-2xi3
    trip = [(2, 3, 1, 2), (3, 1, 2, -2), (1, 2, 3, -2)]
    for (j, k, i, cst) in trip:
        val = cst*sq[i-1]/(sq[j-1]*sq[k-1])
        c[j][k][i] = val; c[k][j][i] = -val
    return c


def Gamma(p):
    c = cstruct(p)
    return [[[ (c[a][b][e]-c[b][e][a]+c[e][a][b])/2 for e in range(4)] for b in range(4)] for a in range(4)]


def E0(f, p):
    return mp.diff(f, p)/mp.sqrt(G(p))


def riemann(p):
    Gm = Gamma(p); c = cstruct(p)
    dG = [[[ E0(lambda pp, b=b, cc=cc, d=d: Gamma(pp)[b][cc][d], p) for d in range(4)] for cc in range(4)] for b in range(4)]
    R = {}
    for a, b, cc, d in itertools.product(range(4), repeat=4):
        val = (dG[b][cc][d] if a == 0 else 0) - (dG[a][cc][d] if b == 0 else 0)
        for e in range(4):
            val += Gm[b][cc][e]*Gm[a][e][d] - Gm[a][cc][e]*Gm[b][e][d] - c[a][b][e]*Gm[e][cc][d]
        R[(a, b, cc, d)] = val
    return R


def omega_basis():
    out = []
    for i, (j, k) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
        F = mp.matrix(4, 4); F[0, i] = 1; F[i, 0] = -1; F[j, k] = 1; F[k, j] = -1
        out.append(F)
    return out


def ip2(F, H):
    return sum(F[a, b]*H[a, b] for a in range(4) for b in range(4))/2


def frame_forms(p, s3=1):
    w = omega_basis(); x = X(p); x1, x2 = mp.sqrt(x[0]), mp.sqrt(x[1])
    u1 = (x1*w[0]+x2*w[1])/mp.sqrt(2)
    u2 = (-x2*w[0]+x1*w[1])/mp.sqrt(2)
    u3 = s3*w[2]/mp.sqrt(2)
    return u1, u2, u3


def cov2(Ffun, p, a):
    """(nabla_{E_a} F)_{bc} for an invariant 2-form F(p)."""
    Gm = Gamma(p); F = Ffun(p)
    out = mp.matrix(4, 4)
    for b in range(4):
        for cc in range(4):
            val = E0(lambda pp: Ffun(pp)[b, cc], p) if a == 0 else 0
            for d in range(4):
                val -= Gm[a][b][d]*F[d, cc] + Gm[a][cc][d]*F[b, d]
            out[b, cc] = val
    return out


def wedge12(xi, F):
    """1-form ^ 2-form -> 3-form as dict over sorted triples."""
    out = {}
    for t in itertools.combinations(range(4), 3):
        a, b, cc = t
        out[t] = xi[a]*F[b, cc] - xi[b]*F[a, cc] + xi[cc]*F[a, b]
    return out


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'data', 'step79'); os.makedirs(outdir, exist_ok=True)
    # orientation choice of u3 so that psi is (2,0)
    p0 = mp.mpf('0.5')
    u1, u2, u3 = frame_forms(p0)
    om = u1*mp.sqrt(2); J = -om  # (J v)_b = sum_a v_a om_ab
    psi = u2 + I*u3
    test = J.T*psi - I*psi
    s3 = 1 if mp.norm(test) < 1e-20 else -1
    def fr(pp):
        return frame_forms(pp, s3)

    def quantities(p):
        u1, u2, u3 = fr(p); om = u1*mp.sqrt(2); J = -om
        psi = u2 + I*u3; psib = u2 - I*u3
        assert mp.norm(J.T*psi - I*psi) < mp.mpf(10)**-25
        nab = [[cov2(lambda pp, k=k: fr(pp)[k], p, a) for k in range(3)] for a in range(4)]
        alpha = [ip2(nab[a][0], u2) - I*ip2(nab[a][0], u3) for a in range(4)]
        b = [ip2(nab[a][1], u3) for a in range(4)]
        # check nabla psi = -conj(alpha) u1 - i b psi
        res_psi = max(mp.norm(nab[a][1]+I*nab[a][2] - (-mp.conj(alpha[a])*u1 - I*b[a]*psi)) for a in range(4))
        q = 4*sum(ip2(nab[a][0], nab[a][0]) for a in range(4))/2  # |nabla omega|^2 = 2|nabla u1|^2
        # curvature operator and W+
        R = riemann(p)
        Ric = [[sum(R[(a, bb, cc, a)] for a in range(4)) for cc in range(4)] for bb in range(4)]
        scal = sum(Ric[i][i] for i in range(4))
        def Rop(F, H):  # <Rcal F, H>, Rcal_{ab,cd}=-R_abcd, sectional positive
            return -sum(R[(a, bb, cc, d)]*F[a, bb]*H[cc, d] for a in range(4) for bb in range(4) for cc in range(4) for d in range(4))/4
        U = [u1, u2, u3]
        Wm = [[Rop(U[i], U[j]) - (scal/12 if i == j else 0) for j in range(3)] for i in range(3)]
        r = Wm[0][0]; eta = Wm[0][1] + I*Wm[0][2]
        v = (Wm[1][1]-Wm[2][2])/2 + I*Wm[1][2]
        Jm = J
        def p10(xi):
            xJ = [sum(xi[a]*Jm[a, bb] for a in range(4)) for bb in range(4)]
            return [(xi[bb]-I*xJ[bb])/2 for bb in range(4)]
        def p01(xi):
            xJ = [sum(xi[a]*Jm[a, bb] for a in range(4)) for bb in range(4)]
            return [(xi[bb]+I*xJ[bb])/2 for bb in range(4)]
        return dict(u1=u1, u2=u2, u3=u3, om=om, J=J, psi=psi, psib=psib, alpha=alpha, b=b, q=q,
                    scal=scal, Ric=Ric, W=Wm, r=r, eta=eta, v=v, p10=p10, p01=p01, res_psi=res_psi)

    def deriv_scalar(fun, p):
        re = E0(lambda pp: mp.re(fun(pp)), p); im = E0(lambda pp: mp.im(fun(pp)), p)
        return re + I*im

    def analyse(p):
        Qd = quantities(p)
        u1, psi, psib, alpha, b = Qd['u1'], Qd['psi'], Qd['psib'], Qd['alpha'], Qd['b']
        p10, p01 = Qd['p10'], Qd['p01']
        r, eta, v, q = Qd['r'], Qd['eta'], Qd['v'], Qd['q']
        # type check of alpha
        al10 = p10(alpha); al_type = max(abs(alpha[a]-al10[a]) for a in range(4))
        # Jhat: zeta in (0,1) -> (1,0) with zeta^psi = 2i Jhat(zeta)^u1 ; basis of (1,0)
        basis10 = []
        for a in range(4):
            e = [mp.mpf(0)]*4; e[a] = 1
            basis10.append(p10(e))
        def Jhat(zeta):
            lhs = wedge12(zeta, psi)
            keys = sorted(lhs)
            # solve least squares over coefficients c_a: sum c_a 2i basis10[a]^u1 = lhs
            cols = [wedge12([2*I*z for z in basis10[a]], u1) for a in range(4)]
            M = mp.matrix(len(keys), 4); rhs = mp.matrix(len(keys), 1)
            for i, k in enumerate(keys):
                rhs[i] = lhs[k]
                for a in range(4):
                    M[i, a] = cols[a][k]
            # least squares via normal equations with pseudo-inverse (rank 2)
            MH = M.H
            A_ = MH*M; B_ = MH*rhs
            # regularize: rank-2 problem; use SVD
            Uu, Ss, Vv = mp.svd_c(M)
            sol = mp.matrix(4, 1)
            for k in range(len(Ss)):
                if abs(Ss[k]) > mp.mpf(10)**-20:
                    coef = sum(mp.conj(Uu[i, k])*rhs[i] for i in range(len(keys)))/Ss[k]
                    for a in range(4):
                        sol[a] += mp.conj(Vv[k, a])*coef
            xi = [sum(sol[a]*basis10[a][bb] for a in range(4)) for bb in range(4)]
            resid = max(abs(sum(M[i, a]*sol[a] for a in range(4)) - rhs[i]) for i in range(len(keys)))
            return xi, resid
        def K(xi):
            return Jhat([mp.conj(z) for z in xi])
        # derivatives of r, eta, v along E0
        dr = [deriv_scalar(lambda pp: quantities(pp)['r'], p), 0, 0, 0]
        deta0 = deriv_scalar(lambda pp: quantities(pp)['eta'], p)
        dv0 = deriv_scalar(lambda pp: quantities(pp)['v'], p)
        Deta = [(deta0 if a == 0 else 0) + I*b[a]*eta for a in range(4)]
        Dv = [(dv0 if a == 0 else 0) + 2*I*b[a]*v for a in range(4)]
        dr10 = p10(dr); Deta10 = p10(Deta); Deta01 = p01(Deta); Dv10 = p10(Dv); Dv01 = p01(Dv)
        Ka, rK1 = K(alpha); Kdr, rK2 = K(dr10)
        E1 = [Deta10[a] - (v*alpha[a] - I*mp.conj(eta)*Ka[a] + I*Kdr[a]) for a in range(4)]
        KDv, rK3 = K(Dv10)
        E2 = [mp.conj(Deta01[a]) + (3*r/2)*alpha[a] + 2*I*KDv[a] for a in range(4)]
        n = lambda xi: sum(abs(z)**2 for z in xi)
        # |nabla W|^2 directly from W in omega basis
        w = omega_basis(); wh = [F/mp.sqrt(2) for F in w]
        def Wop_basis(pp):
            Qp = quantities(pp); U = [Qp['u1'], Qp['u2'], Qp['u3']]
            Wm = Qp['W']
            # W as matrix in omega-hat basis: W_hat = T W T^T with T_{ki}=<wh_i,U_k>
            T = [[ip2(wh[i], U[k]) for i in range(3)] for k in range(3)]
            return [[sum(T[k][i]*Wm[k][l]*T[l][j] for k in range(3) for l in range(3)) for j in range(3)] for i in range(3)]
        Gm = Gamma(p)
        Wh = Wop_basis(p)
        # connection of omega-hat frame: Theta[a][i][j]=<nabla_a wh_i, wh_j>
        Th = [[[ip2(cov2(lambda pp, i=i: wh[i], p, a), wh[j]) for j in range(3)] for i in range(3)] for a in range(4)]
        nW2 = 0
        for a in range(4):
            for i in range(3):
                for j in range(3):
                    val = (E0(lambda pp: Wop_basis(pp)[i][j], p) if a == 0 else 0)
                    # (nabla W)_ij = d W_ij - sum_k Th[a][i][k] W_kj - sum_k Th[a][j][k] W_ik
                    val -= sum(Th[a][i][k]*Wh[k][j] + Th[a][j][k]*Wh[i][k] for k in range(3))
                    nW2 += val**2
        decomp = 5*n([dr10[a]-eta*alpha[a] for a in range(4)]) + 10*n(Dv10) + 2*n([Dv01[a]+eta*mp.conj(alpha[a]) for a in range(4)])
        # torsion structure equation
        c = cstruct(p)
        dal0 = [deriv_scalar(lambda pp, k=k: quantities(pp)['alpha'][k], p) for k in range(4)]
        Dal = mp.matrix(4, 4)
        for a in range(4):
            for bb in range(4):
                val = (dal0[bb] if a == 0 else 0) - (dal0[a] if bb == 0 else 0) - sum(c[a][bb][e]*alpha[e] for e in range(4))
                val -= I*(b[a]*alpha[bb]-b[bb]*alpha[a])
                Dal[a, bb] = val
        Tpred = -I*mp.sqrt(2)*(mp.conj(eta)*u1 - (q/8)*psib + mp.conj(v)*psi)
        Tres = mp.norm(Dal - Tpred)
        # <db,omega>
        db = mp.matrix(4, 4)
        db0 = [E0(lambda pp, k=k: quantities(pp)['b'][k], p) for k in range(4)]
        for a in range(4):
            for bb in range(4):
                db[a, bb] = (db0[bb] if a == 0 else 0) - (db0[a] if bb == 0 else 0) - sum(c[a][bb][e]*b[e] for e in range(4))
        db_om = ip2(db, Qd['om'])
        s = Qd['scal']
        Fv = n(Dv01) - n(Dv10) - (abs(s) - q/2)*abs(v)**2
        Feta = n(Deta01) - n(Deta10) - (abs(s)/2 - q/4)*abs(eta)**2
        # currents: i*(conj(f) Df ^ omega)(E1,E2,E3)
        om = Qd['om']
        def cur(fval, Df):
            xi = [mp.conj(fval)*z for z in Df]
            t = wedge12(xi, om)
            return I*t[(1, 2, 3)]
        jv = cur(v, Dv); jeta = cur(eta, Deta)
        # Bochner RHS
        etaVeta = mp.re(mp.conj(v)*eta**2)
        bochR = (mp.mpf(9)/8)*r**2*q + (s/2+9*q/4)*abs(eta)**2 + (-2*s-9*q/4)*2*abs(v)**2 + 18*etaVeta
        Wm = Qd['W']
        W2 = sum(Wm[i][j]**2 for i in range(3) for j in range(3))
        return dict(p=p, scal=s, Ric_res=max(abs(Qd['Ric'][i][j]+(3 if i == j else 0)) for i in range(4) for j in range(4)),
                    q=q, q_exact=36*(1-p**2)**3/(1+3*p**2)**3, r=r, r_pred=s/6+q/4, eta=eta, v=v,
                    res_psi=Qd['res_psi'], alpha_type=al_type, K_res=max(rK1, rK2, rK3),
                    E1=mp.sqrt(n(E1)), E2=mp.sqrt(n(E2)), nW2=nW2, decomp=decomp, Tres=Tres,
                    db_om=db_om, db_om_pred=-(2*s+q)/4, Fv=Fv, Feta=Feta, jv=jv, jeta=jeta,
                    bochR=bochR, W2=W2,
                    n_dr=n([dr10[a]-eta*alpha[a] for a in range(4)]), n_dv=n(Dv10), n_dbv=n(Dv01),
                    n_cross=n([Dv01[a]+eta*mp.conj(alpha[a]) for a in range(4)]),
                    n_deta=n(Deta10), n_dbeta=n(Deta01), absv2=abs(v)**2, abseta2=abs(eta)**2,
                    n_E2lhs=n([mp.conj(Deta01[a]) + (3*r/2)*alpha[a] for a in range(4)]),
                    n_E1rhs=n([v*alpha[a] - I*mp.conj(eta)*Ka[a] + I*Kdr[a] for a in range(4)]),
                    X1=sum(alpha[a]*mp.conj(KDv[a]) for a in range(4)),
                    Xdirect=sum(alpha[a]*mp.conj(Deta01[a]) for a in range(4)),
                    alpha2=n(alpha), n_Ka=n(Ka), n_dr10=n(dr10), n_Kdr=n(Kdr),
                    vol=mp.sqrt(A(p)[0]*A(p)[1]*A(p)[2]), sqrtG=mp.sqrt(G(p)))

    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'regularized':
        # Step 80: common-(q+eps) regularization of the scalar and Kodaira
        # identities on the complete model.  The coordinate
        #   x=1-exp(-u), p=1/3+(2/3)x^2
        # resolves the bolt at u=0 and turns the ACH end into u=infinity.
        # For every fixed eps the three boundary currents vanish at both ends;
        # their maxima nevertheless diverge as eps -> 0.
        import numpy as np
        mp.mp.dps = 35
        order = int(sys.argv[2]) if len(sys.argv) > 2 else 18
        umax = mp.mpf(sys.argv[3]) if len(sys.argv) > 3 else mp.mpf(30)
        # Unit-width composite Gauss rule.  Geometry is evaluated once and
        # reused for all epsilons.
        zz, ww = np.polynomial.legendre.leggauss(order)
        nodes = []
        for kseg in range(int(mp.ceil(umax))):
            a = mp.mpf(kseg); bnd = min(umax, a+1)
            for zf, wf in zip(zz, ww):
                u = (a+bnd)/2 + (bnd-a)*mp.mpf(float(zf))/2
                wg = (bnd-a)*mp.mpf(float(wf))/2
                x = 1-mp.exp(-u)
                p = mp.mpf(1)/3 + mp.mpf(2)/3*x*x
                dpdu = mp.mpf(4)/3*x*mp.exp(-u)
                d = analyse(p)
                q = d['q']
                qp = mp.diff(lambda pp: 36*(1-pp**2)**3/(1+3*pp**2)**3, p)
                # Analyst Laplacian of q, hence D from
                # Delta q = -D + 18q - 9q^2/4.
                volf = lambda pp: mp.sqrt(A(pp)[0]*A(pp)[1]*A(pp)[2])
                lapq = mp.diff(lambda pp: volf(pp)/mp.sqrt(G(pp))*mp.diff(lambda rr: 36*(1-rr**2)**3/(1+3*rr**2)**3, pp), p)/(volf(p)*mp.sqrt(G(p)))
                D = -lapq + 18*q-mp.mpf(9)/4*q*q
                meas = d['sqrtG']*d['vol']*dpdu*wg
                nodes.append(dict(u=u,p=p,w=wg,dpdu=dpdu,d=d,q=q,qp=qp,D=D,meas=meas))
        eps_list = [mp.mpf(z) for z in ['1e-1','1e-2','1e-3','1e-4','1e-6','1e-8','1e-10','1e-12']]
        results = {}
        for eps in eps_list:
            sums = {k:mp.mpf(0) for k in ['gradq','D','q2','rhs','KvA','Kvdw','KetaA','Ketadw']}
            peaks = {k:(mp.mpf(0),mp.mpf(0)) for k in ['logq','v','eta']}
            for nd in nodes:
                d=nd['d']; q=nd['q']; den=q+eps; meas=nd['meas']
                dq2=nd['qp']**2/G(nd['p'])
                sums['gradq'] += dq2/den**2*meas
                sums['D'] += nd['D']/den*meas
                sums['q2'] += mp.mpf(9)/4*q*q/den*meas
                sums['rhs'] += 18*q/den*meas
                sums['KvA'] += d['Fv']/den*meas
                sums['KetaA'] += d['Feta']/den*meas
                # <dq,j> dV = q'(p) j_0 vol(p) dp.
                common = nd['qp']*d['vol']*nd['dpdu']*nd['w']/den**2
                sums['Kvdw'] += mp.re(d['jv'])*common
                sums['Ketadw'] += mp.re(d['jeta'])*common
                fluxes = {
                    'logq': abs(d['vol']/d['sqrtG']*nd['qp']/den),
                    'v': abs(d['vol']*mp.re(d['jv'])/den),
                    'eta': abs(d['vol']*mp.re(d['jeta'])/den)}
                for key,val in fluxes.items():
                    if val>peaks[key][0]: peaks[key]=(val,nd['u'])
            scalar_lhs=sums['gradq']+sums['D']+sums['q2']
            results[mp.nstr(eps,2)] = {
                **{k:mp.nstr(v,16) for k,v in sums.items()},
                'scalar_lhs':mp.nstr(scalar_lhs,16),
                'scalar_residual':mp.nstr(scalar_lhs-sums['rhs'],8),
                'Kv_residual':mp.nstr(sums['KvA']-sums['Kvdw'],8),
                'Keta_residual':mp.nstr(sums['KetaA']-sums['Ketadw'],8),
                'peak_flux':{k:{'abs':mp.nstr(v[0],12),'u':mp.nstr(v[1],10)} for k,v in peaks.items()}}
            print(mp.nstr(eps,3), results[mp.nstr(eps,2)], flush=True)
        out={'order':order,'umax':mp.nstr(umax,8),'node_count':len(nodes),'results':results}
        json.dump(out,open(os.path.join(outdir,'regularized_model.json'),'w'),indent=1)
        return
    if len(sys.argv) > 1 and sys.argv[1] == 'integrals':
        # radial integrals per unit group volume, dV = sqrt(G) vol dp, p = 1/3 + (2/3) x^2
        mp.mp.dps = 30
        nodes = int(sys.argv[2]) if len(sys.argv) > 2 else 40
        xs, ws = zip(*[(mp.mpf(1)/2*(1+t), w/2) for t, w in zip(*mp.gauss_legendre_nodes(nodes))]) if hasattr(mp, 'gauss_legendre_nodes') else (None, None)
        if xs is None:
            import numpy as np
            t, w = np.polynomial.legendre.leggauss(nodes)
            xs = [mp.mpf(float(z))/2+mp.mpf(1)/2 for z in t]; ws = [mp.mpf(float(z))/2 for z in w]
        keys = ['Fv', 'Feta', 'nW2', 'bochR', 'abseta2', 'absv2', 'q', 'q2', 'n_dv', 'n_dbv', 'n_cross', 'n_dr', 'n_deta', 'n_dbeta', 'vq', 'etaq', 'etaVeta']
        tot = {k: mp.mpf(0) for k in keys}
        for x, wgt in zip(xs, ws):
            p = mp.mpf(1)/3 + mp.mpf(2)/3*x**2
            d = analyse(p)
            meas = d['sqrtG']*d['vol']*mp.mpf(4)/3*x*wgt
            vals = dict(Fv=d['Fv'], Feta=d['Feta'], nW2=d['nW2'], bochR=d['bochR'], abseta2=d['abseta2'], absv2=d['absv2'],
                        q=d['q'], q2=d['q']**2, n_dv=d['n_dv'], n_dbv=d['n_dbv'], n_cross=d['n_cross'], n_dr=d['n_dr'],
                        n_deta=d['n_deta'], n_dbeta=d['n_dbeta'], vq=d['q']*d['absv2'], etaq=d['q']*d['abseta2'],
                        etaVeta=mp.re(mp.conj(d['v'])*d['eta']**2))
            for k in keys:
                tot[k] += meas*mp.re(vals[k])
        out = {k: mp.nstr(v, 12) for k, v in tot.items()}
        s_ = mp.mpf(12)
        T_AK = 2*tot['absv2'] + 3*tot['q2']/32
        out['T_AK'] = mp.nstr(T_AK, 12)
        out['star_lhs_|s|Q/16'] = mp.nstr(s_*tot['q']/16, 12)
        out['star_rhs'] = mp.nstr(tot['abseta2']+T_AK, 12)
        out['two_s_trV2'] = mp.nstr(2*s_*2*tot['absv2'], 12)
        out['gradV_part_10dv+2cross'] = mp.nstr(10*tot['n_dv']+2*tot['n_cross'], 12)
        print(json.dumps(out, indent=1))
        json.dump(out, open(os.path.join(outdir, f'model_integrals_n{nodes}.json'), 'w'), indent=1)
        return
    if len(sys.argv) > 1 and sys.argv[1] == 'logq':
        # test Delta q = 8trV^2-24|eta|^2-(3s/2)q-(9/4)q^2+16 X (analyst Laplacian) and the log q flux
        qf = lambda pp: 36*(1-pp**2)**3/(1+3*pp**2)**3
        volf = lambda pp: mp.sqrt(A(pp)[0]*A(pp)[1]*A(pp)[2])
        out = {}
        for p0 in ['0.4', '0.5', '0.7', '0.9']:
            p0 = mp.mpf(p0); d = analyse(p0)
            lap = mp.diff(lambda pp: volf(pp)/mp.sqrt(G(pp))*mp.diff(qf, pp), p0)/(volf(p0)*mp.sqrt(G(p0)))
            base = 8*2*d['absv2'] - 24*d['abseta2'] + 18*d['q'] - mp.mpf(9)/4*d['q']**2
            out[str(p0)] = {'lap_q': mp.nstr(lap, 15), 'base': mp.nstr(base, 15), 'resid_over16': mp.nstr((lap-base)/16, 15),
                            'X1': mp.nstr(d['X1'], 15), 'Xdirect': mp.nstr(d['Xdirect'], 15), 'r_alpha2': mp.nstr(d['r']*d['alpha2'], 15),
                            'vol_dlogq': mp.nstr(volf(p0)/mp.sqrt(G(p0))*mp.diff(qf, p0)/qf(p0), 15)}
            print(p0, out[str(p0)], flush=True)
        for p0 in ['0.99', '0.999', '0.9999']:
            p0 = mp.mpf(p0)
            out['end'+str(p0)] = {'vol_dlogq': mp.nstr(volf(p0)/mp.sqrt(G(p0))*mp.diff(qf, p0)/qf(p0), 15),
                                  'Vol_below': mp.nstr(mp.quad(lambda pp: volf(pp)*mp.sqrt(G(pp)), [mp.mpf(1)/3, mp.mpf('0.5'), p0]), 15)}
            print(out['end'+str(p0)], flush=True)
        json.dump(out, open(os.path.join(outdir, 'logq_check.json'), 'w'), indent=1)
        return
    if len(sys.argv) > 1 and sys.argv[1] == 'flux':
        # pointwise divergence check of the Kodaira identities and end-flux values
        out = {}
        h = mp.mpf('1e-10')
        for p0 in [mp.mpf('0.5'), mp.mpf('0.7')]:
            dm, d0, dp = analyse(p0-h), analyse(p0), analyse(p0+h)
            for key, F in [('jv', 'Fv'), ('jeta', 'Feta')]:
                Phi = lambda d: d['vol']*mp.re(d[key])
                div = (Phi(dp)-Phi(dm))/(2*h)/(d0['vol']*d0['sqrtG'])
                out[f'{key}_p{p0}'] = {'div_current': mp.nstr(div, 15), 'integrand': mp.nstr(d0[F], 15),
                                       'sum': mp.nstr(div+d0[F], 6), 'diff': mp.nstr(div-d0[F], 6)}
            out[f'aux_p{p0}'] = {k: mp.nstr(d0[k], 15) for k in ['n_E2lhs', 'n_dv', 'n_E1rhs', 'n_deta', 'alpha2', 'q', 'n_Ka', 'n_dr10', 'n_Kdr']}
        for p0 in ['0.9', '0.99', '0.999', '0.9999']:
            d = analyse(mp.mpf(p0))
            out[f'endflux_p{p0}'] = {'vol_jv': mp.nstr(d['vol']*mp.re(d['jv']), 15), 'vol_jeta': mp.nstr(d['vol']*mp.re(d['jeta']), 15),
                                     'vol': mp.nstr(d['vol'], 10), 'vol_v2': mp.nstr(d['vol']*d['absv2'], 10), 'vol_eta2': mp.nstr(d['vol']*d['abseta2'], 10)}
            print(p0, out[f'endflux_p{p0}'], flush=True)
        print(json.dumps(out, indent=1))
        json.dump(out, open(os.path.join(outdir, 'kodaira_flux.json'), 'w'), indent=1)
        return
    pts = [mp.mpf(x) for x in ['0.4', '0.5', '0.6', '0.75', '0.9']]
    rows = []
    for p in pts:
        d = analyse(p)
        rows.append({k: (str(mp.nstr(val, 15)) if not isinstance(val, (int,)) else val) for k, val in d.items()})
        print({k: mp.nstr(d[k], 8) for k in ['p', 'Ric_res', 'q', 'q_exact', 'r', 'r_pred', 'res_psi', 'alpha_type', 'K_res', 'E1', 'E2', 'nW2', 'decomp', 'Tres', 'db_om', 'db_om_pred', 'Fv', 'jv', 'Feta', 'jeta']}, flush=True)
    json.dump({'s3': s3, 'points': rows}, open(os.path.join(outdir, 'dW_check.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
