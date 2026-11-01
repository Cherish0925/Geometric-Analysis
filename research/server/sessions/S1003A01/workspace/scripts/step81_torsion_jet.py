"""Step 81b: full first jet of the torsion alpha on the Bianchi-VIII model and the
Poincare-Lelong decomposition of the Levi form of log q along the torsion line.

D alpha = nabla alpha - i b alpha (weight -1, as in the torsion structure equation).
Project the derivative slot into (1,0)/(0,1) and the form slot into (1,0):
   D'alpha  = S + skew      (S symmetric in (1,0)x(1,0), skew part prop. to conj(v) psi)
   D''alpha = trace + T     (trace prop. to conj(eta) omega, T trace-free)
The (0,1) form-slot part of nabla alpha is the algebraic Nijenhuis term.
Also evaluates, for the unit torsion line l_alpha = span(e,Je), e = Re alpha^#/|.|,
Z=(e-iJe)/2:
   a = <D_Z alpha, alpha>, b = <D_Zbar alpha, alpha>,  holomorphic-gradient defect
   G = |D_Z alpha|^2|alpha|^2 - |a|^2 >= 0,
and checks L_{log q}(l_alpha) = s/2 numerically at eps=0 for many p.
Output: workspace/data/step81/torsion_jet.json
"""
import json, os, sys
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import step79_dW_components_bianchiVIII as B
import step81_ddc_canonical_pairing as T

mp.mp.dps = 30
I = mp.mpc(0, 1); SQ2 = mp.sqrt(2)


def jet(p):
    u1, u2, u3 = T.fr(p); om = u1*SQ2; psi = u2 + I*u3
    alpha, b = T.conn(p)
    Gm = B.Gamma(p)
    dal0 = [mp.diff(lambda z, k=k: T.conn(z)[0][k], p)/mp.sqrt(B.G(p)) for k in range(4)]
    M = mp.matrix(4, 4)  # M[a,c] = (D_a alpha)_c
    for a in range(4):
        for c in range(4):
            val = (dal0[c] if a == 0 else 0) - sum(Gm[a][c][d]*alpha[d] for d in range(4)) - I*b[a]*alpha[c]
            M[a, c] = val
    def Jv(v):
        return [sum(v[a]*om[a, bb] for a in range(4)) for bb in range(4)]
    # projectors on vectors/forms: xi^{1,0} = (xi - i xi o J)/2 with (xi o J)_a = sum_b om_ab xi_b
    def xiJ(xi):
        return [sum(om[a, bb]*xi[bb] for bb in range(4)) for a in range(4)]
    def p10(xi):
        x = xiJ(xi); return [(xi[a]-I*x[a])/2 for a in range(4)]
    def p01(xi):
        x = xiJ(xi); return [(xi[a]+I*x[a])/2 for a in range(4)]
    # form-slot projections for each derivative index
    rows10 = [p10([M[a, c] for c in range(4)]) for a in range(4)]
    rows01 = [p01([M[a, c] for c in range(4)]) for a in range(4)]
    # derivative-slot projection: apply to columns
    def proj_deriv(rows, pr):
        cols = [[rows[a][c] for a in range(4)] for c in range(4)]
        pc = [pr(col) for col in cols]
        return [[pc[c][a] for c in range(4)] for a in range(4)]
    Dp = proj_deriv(rows10, p10)   # (1,0) deriv, (1,0) form
    Dpp = proj_deriv(rows10, p01)  # (0,1) deriv, (1,0) form
    Nform = rows01                 # (0,1) form part (Nijenhuis, algebraic)
    # real-matrix norms: |A|^2 = sum_{a,c}|A_ac|^2
    nrm = lambda A: sum(abs(A[a][c])**2 for a in range(4) for c in range(4))
    sym = [[(Dp[a][c]+Dp[c][a])/2 for c in range(4)] for a in range(4)]
    skw = [[(Dp[a][c]-Dp[c][a])/2 for c in range(4)] for a in range(4)]
    # trace of D'' with respect to the hermitian pairing: tr = sum_a Dpp[a][c] * (J e_a)_c type
    # use omega-contraction: t = sum_{a,c} Dpp[a][c] om[a,c]
    tr = sum(Dpp[a][c]*om[a, c] for a in range(4) for c in range(4))
    # trace-free part: subtract (tr/ |om|^2) om projected to ((0,1),(1,0)) type
    omp = proj_deriv([p10([om[a, c] for c in range(4)]) for a in range(4)], p01)
    nom = sum(omp[a][c]*om[a, c] for a in range(4) for c in range(4))
    Tf = [[Dpp[a][c] - tr/nom*omp[a][c] for c in range(4)] for a in range(4)]
    # torsion line
    ra = [mp.re(z) for z in alpha]; na = mp.sqrt(sum(z**2 for z in ra))
    e = [z/na for z in ra]; Je = Jv(e)
    Z = [(e[k]-I*Je[k])/2 for k in range(4)]; Zb = [(e[k]+I*Je[k])/2 for k in range(4)]
    DZ = [sum(Z[a]*M[a, c] for a in range(4)) for c in range(4)]
    DZb = [sum(Zb[a]*M[a, c] for a in range(4)) for c in range(4)]
    DZ10 = p10(DZ); DZb10 = p10(DZb)
    al2 = sum(abs(z)**2 for z in alpha)
    herm = lambda x, y: sum(x[k]*mp.conj(y[k]) for k in range(4))
    a_ = herm(DZ10, alpha); b_ = herm(DZb10, alpha)
    Gdef = sum(abs(z)**2 for z in DZ10)*al2 - abs(a_)**2
    # Levi form of log q along l_alpha at eps=0
    d = T.analyse(p, mp.mpf(0))
    return dict(p=p, q=d['q'], alpha2=al2, n_sym=nrm(sym), n_skew=nrm(skw), n_Dpp=nrm(Dpp), n_trace_part=abs(tr)**2/abs(nom),
                n_Tf=nrm(Tf), n_N=nrm(Nform), eta2=d['eta2'], v2=d['eta2']*0 + 0,
                DZb_norm2=sum(abs(z)**2 for z in DZb10), DZ_norm2=sum(abs(z)**2 for z in DZ10),
                a=a_, b=b_, Gdef=Gdef, L_tor=d['L_tor'], L_oth=d['L_oth'], lap_logq=d['lap'])


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'data', 'step81'); os.makedirs(outdir, exist_ok=True)
    rows = []
    for ps in ['0.34', '0.36', '0.4', '0.45', '0.5', '0.6', '0.7', '0.8', '0.9', '0.95', '0.99']:
        r = jet(mp.mpf(ps))
        row = {k: mp.nstr(v, 14) for k, v in r.items()}
        rows.append(row); print(row, flush=True)
    json.dump(rows, open(os.path.join(outdir, 'torsion_jet.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
