#!/usr/bin/env python3
"""Step 71: does the scalar compatibility source depend on torsion-free (curvature) fibre data?

Spirit #79 question.  At the polished order-8 witness (A02 gen5, lambda=-5, H2 fixed), let
  x = (H4, ..., H_K)            unknown even metric jets (Darboux gauge, g=exp H, Omega fixed)
  C(x) = (E2, ..., E_{K-2})      lower Einstein equations (all components)
  R(x) = P_K(E_K)               the scalar compatibility for the next lift H_{K+2}
  N(x) = coordinate Taylor coefficients of the Nijenhuis tensor of J = J0 exp(H)
         in odd degrees 3..K-1 (degree 1 is fixed by H2).
Tangent space Tan = ker dC.  Torsion-fixed fibre F = Tan cap ker dN.
If dR|_F = 0, the next scalar source depends (to first order on the solution variety) only on torsion
Taylor data: the torsion-only reduction holds at this order.  If dR|_F != 0, curvature-fibre data feed
the obstruction, and we measure how many new directions of the scalar target they reach beyond the
newest-jet channel image.

Sub-fibres: F_top = F cap {only H_K varies} (should give 0 by the newest-channel factorization).
Also records the J0 exp(H) sanity check J^2=-1 and g-compatibility.
Absolute singular values are recorded (lesson of Step 69: never use self-relative rank only).

Run: python step71_fibre_test.py K   (K=6 or 8)
Out: workspace/data/step71/fibre_test_K{K}.json
"""
from pathlib import Path
import json, sys, time
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt, J0
from step68_scalar_compatibility import P_matrix
OUT = HERE.parent / 'data' / 'step71'; OUT.mkdir(parents=True, exist_ok=True)


def expH(R, H):
    eye = torch.zeros(4, 4, R.nm, dtype=dt, device=dev)
    for i in range(4): eye[i, i, 0] = 1
    g = eye + H; Pw = H; fact = 1.0
    for n in range(2, R.N // 2 + 1):
        Pw = R.mm(Pw, H, 'ikp,kjp->ijp'); fact *= n
        g = g + Pw / fact
    return g


def nijenhuis(R, Jm):
    """N^k_ij = J^l_i d_l J^k_j - J^l_j d_l J^k_i - J^k_l (d_i J^l_j - d_j J^l_i); Jm[k,j,p]."""
    dJ = torch.stack([R.diff(Jm, l) for l in range(4)], 0)      # dJ[l,k,j,p] = d_l J^k_j
    A = R.mm(Jm, dJ, 'lip,lkjp->kijp')                           # J^l_i d_l J^k_j
    B = dJ.permute(1, 2, 0, 3)                                   # [k,j,l] = d_l J^k_j
    curl = B.permute(0, 2, 1, 3) - B                             # [k,i,j]: d_i J^k_j - d_j J^k_i ; B[k,j,i]=d_i J^k_j
    # B[k,a,b] = d_b J^k_a.  want d_i J^l_j = B[l,j,i];  curl2[l,i,j] = B[l,j,i]-B[l,i,j]
    curl2 = B.permute(0, 2, 1, 3) - B
    Cterm = R.mm(Jm, curl2, 'klp,lijp->kijp')
    return A - A.permute(0, 2, 1, 3) - Cterm


def null_basis(M, tol_abs):
    U, s, Vh = torch.linalg.svd(M, full_matrices=True)
    r = int((s > tol_abs).sum())
    return Vh[r:].T, s


def main(K=8, name='recon_F012_gen5_lam-5'):
    t0 = time.time()
    lam = float(name.split('lam')[-1])
    base = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step80'
    dd = np.load(base / f'{name}.npz')
    T = Tower(K, lam); T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
    tt = lambda a: torch.tensor(np.asarray(a), dtype=dt, device=dev)
    H2 = tt(dd['H2'])
    v8 = np.load(HERE.parent / 'data' / 'step69' / f'order8_polished_v_{name}.npy')
    s8 = [6 * 35, 6 * 84, 6 * 165]   # sizes of H4,H6,H8 in Tower(8) layout (monomial counts 35,84,165)
    unk = list(range(4, K + 1, 2))
    sizes = [T.size[d] for d in unk]
    parts = {4: v8[:s8[0]], 6: v8[s8[0]:s8[0] + s8[1]], 8: v8[s8[0] + s8[1]:]}
    x0 = torch.cat([tt(parts[d]) for d in unk])
    n = x0.numel()
    cons = list(range(2, K - 1, 2))
    nC = 10 * sum(len(T.mon_d[k]) for k in cons)
    PK = tt(P_matrix(K).astype(float) / 2.0)
    odd = list(range(3, K, 2))
    oidx = torch.tensor([i for d in odd for i in T.mon_d[d]], device=dev)
    iu = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    J0t = tt(J0)

    def jets(x):
        J = {2: H2}; o = 0
        for d, s in zip(unk, sizes): J[d] = x[o:o + s]; o += s
        return J

    def funC(x): return T.Evec(jets(x), cons)[0]
    def funR(x): return PK @ T.Evec(jets(x), [K])[0]
    def Jmat(x):
        g = expH(T.R, T.H(jets(x)))
        return torch.einsum('ab,bjp->ajp', J0t, g), g
    def funN(x):
        Jm, _ = Jmat(x); N = nijenhuis(T.R, Jm)
        return torch.stack([N[k, i, j][oidx] for k in range(4) for (i, j) in iu]).reshape(-1)

    # sanity: J^2=-1 and N degree-1 part nonzero, N degree 0 zero
    Jm, g = Jmat(x0)
    J2 = T.R.trunc(T.R.mm(Jm, Jm, 'ikp,kjp->ijp'), T.R.N)
    J2[0, 0, 0] += 1; J2[1, 1, 0] += 1; J2[2, 2, 0] += 1; J2[3, 3, 0] += 1
    Nfull = nijenhuis(T.R, Jm)
    sanity = {'J2_plus_1_norm': float(J2.norm()),
              'N_deg0': float(Nfull[..., T.mon_d[0]].norm()),
              'N_deg1': float(Nfull[..., T.mon_d[1]].norm()),
              'N_deg2(even, should be 0)': float(Nfull[..., T.mon_d[2]].norm()),
              'residual_C': float(funC(x0).norm()), 'residual_R': float(funR(x0).norm())}
    print(json.dumps(sanity), flush=True)

    eye = torch.eye(n, dtype=dt, device=dev)
    def jac(f):
        vj = torch.func.vmap(lambda e: torch.func.jvp(f, (x0,), (e,))[1])
        return torch.cat([vj(eye[s:s + 64]).T for s in range(0, n, 64)], dim=1)
    JC, JR, JN = jac(funC), jac(funR), jac(funN)
    print('jacobians', JC.shape, JR.shape, JN.shape, round(time.time() - t0, 1), flush=True)

    sC = torch.linalg.svdvals(JC); tolC = 1e-9 * float(sC[0])
    Tan, _ = null_basis(JC, tolC)
    JNT = JN @ Tan; sNT = torch.linalg.svdvals(JNT); tolN = 1e-9 * float(sNT[0])
    Fz, _ = null_basis(JNT, tolN)
    Fb = Tan @ Fz
    JRT = JR @ Tan; sRT = torch.linalg.svdvals(JRT)
    JRF = JR @ Fb; sRF = torch.linalg.svdvals(JRF) if Fb.shape[1] else torch.zeros(1, dtype=dt, device=dev)
    rel = lambda s, ref: int((s > 1e-8 * ref).sum())
    refR = float(sRT[0])
    out = {'K': K, 'name': name, 'lam': lam, 'n_unknowns': n, 'sanity': sanity,
           'rank_dC': rel(sC, float(sC[0]) * 1e-1) if False else int((sC > tolC).sum()),
           'dim_Tan': int(Tan.shape[1]), 'rank_dN_on_Tan': int((sNT > tolN).sum()),
           'dim_F': int(Fb.shape[1]),
           'rank_dR_on_Tan': rel(sRT, refR), 'sv_dR_on_Tan_top': float(sRT[0]), 'sv_dR_on_Tan_tail': [float(a) for a in sRT[-5:]],
           'rank_dR_on_F_rel_to_Tan_scale': rel(sRF, refR),
           'sv_dR_on_F': [float(a) for a in sRF[:40]]}
    # combined image: is dR(F) inside dR(top-only channel)?
    top = unk[-1]; o_top = sum(sizes[:-1])
    mask = torch.zeros(n, dtype=dt, device=dev); mask[o_top:] = 1
    # top-only tangent: variations of H_K only satisfying dC (dC does not see H_K except via E_{K-2} -> L_{K-2})
    Ptop = torch.diag(mask)
    Ttop, _ = null_basis(torch.cat([JC, torch.diag(1 - mask)[(1 - mask).bool()]]), tolC)
    JRtop = JR @ Ttop; sTop = torch.linalg.svdvals(JRtop)
    out['dim_top_tangent'] = int(Ttop.shape[1]); out['rank_newest_channel'] = rel(sTop, refR)
    out['sv_newest_top'] = float(sTop[0])
    # top-only torsion-fixed fibre
    JNtop = JN @ Ttop; sN2 = torch.linalg.svdvals(JNtop)
    Fz2, _ = null_basis(JNtop, 1e-9 * float(sN2[0])); Ftop = Ttop @ Fz2
    sRFt = torch.linalg.svdvals(JR @ Ftop) if Ftop.shape[1] else torch.zeros(1, dtype=dt, device=dev)
    out['dim_F_top'] = int(Ftop.shape[1]); out['sv_dR_on_F_top_max'] = float(sRFt[0])
    # joint image rank: [dR(top channel), dR(F)]
    if Fb.shape[1]:
        Ut, st, _ = torch.linalg.svd(JRtop, full_matrices=False); rt = rel(st, refR)
        Uf, sf, _ = torch.linalg.svd(JRF, full_matrices=False); rf = rel(sf, refR)
        joint = torch.cat([Ut[:, :rt], Uf[:, :rf]], 1)
        sj = torch.linalg.svdvals(joint)
        out['rank_image_F'] = rf; out['rank_image_top'] = rt; out['rank_joint_top_plus_F'] = int((sj > 1e-8).sum())
        # which lower jet carries the F-dependence: restrict F to directions with delta H_lower pattern
        blocks = {}
        o = 0
        for d, s in zip(unk, sizes):
            blocks[str(d)] = float(Fb[o:o + s].norm()); o += s
        out['F_basis_block_norms'] = blocks
        # radial row of P_K(E_K): the U(2) invariant Delta^{(K-2)/2} moment.  Project images on it.
    out['time'] = time.time() - t0
    (OUT / f'fibre_test_K{K}.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=1), flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
