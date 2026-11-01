#!/usr/bin/env python3
"""Step 80: explicit REAL reconstruction of a formal AKE jet through order 6 (H2..H8) when Phi6 <= 0,
and evaluation of the UNREDUCED residuals E0..E6.  Positive-Phi6 control: same construction with the
scalar minimiser z* (phi(z*) = Phi6 > 0), which must leave a residual of size ~Phi6 in E6.

Construction.  y = P z + K w   (P: joint range of the quadratic forms, K: its complement).
   Psi(y) = c + J P z + J K w + (1/2) z^T (P^T H P) z         (H depends only on the P-part)
   scalar row pi (pi^T J K = 0):  phi(z) = pi.c + (pi.J P) z + (1/2) z^T H_pi z = 0
       z = z* + t v,  z* = -H_pi^{-1} j,  v = unit eigenvector (eigenvalue h>0),  t = sqrt(-2 Phi6 / h)
   remaining rows: solve (J K) w = -(c + J P z + (1/2) z^T H z)   (least squares; consistent by rank 34)
Then u = u0 + N y gives H4..H7, and H8 = argmin |L6 H8 + E6(u, H8=0)|.
Conventions: H = sum_d sum_{a<6} sum_{m in mon_d[d]} v_d[a*n_d + m] * B_a x^m, with B_a = anti_basis()
(6 symmetric anti-J0 matrices), J0 = [[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]], g = exp(H),
E = Ric(g) - lam g, monomials T.R.mons (exponent 4-tuples) restricted to degree d in the order T.mon_d[d].
Output: workspace/data/step80/recon_<tag>.json and recon_<tag>.npz
"""
import json, sys, os, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step80')
import step79_general_order6 as G
from step77_gn_germ import jet_coords

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step80'


def full_pieces(T, H2, H3, tol=1e-10):
    U = [4, 5, 6, 7]; orders = [1, 2, 3, 4, 5]
    sizes = [T.size[d] for d in U]; n = sum(sizes)
    base = G.zeros(T, skip=tuple(U) + (2, 3))
    def jets(u, h8=None):
        out = {2: H2, 3: H3, **base}; o = 0
        for d, s in zip(U, sizes):
            out[d] = u[o:o + s]; o += s
        if h8 is not None:
            out[8] = h8
        return out
    F = lambda u: T.Evec(jets(u), orders)[0]
    z = torch.zeros(n, dtype=G.dt, device=G.dev)
    b = F(z); A = G.batched_cols(F, n, b)
    u0 = -torch.linalg.pinv(A, rtol=tol) @ b
    N = G.null_right(A, tol); ny = N.shape[1]
    E6 = lambda u: T.Evec(jets(u), [6])[0]
    if 'Qc' not in G._CACHE:
        G.reduce_general(T, H2, H3)
    C6 = G._CACHE['C6']; Qc = G._CACHE['Qc']
    c = C6.T @ E6(u0)
    vj = torch.func.vmap(lambda v: torch.func.jvp(E6, (u0,), (v,))[1])
    Jy = C6.T @ torch.cat([vj(N[:, s:s + 64].T).T for s in range(0, ny, 64)], dim=1)
    N4 = N[:sizes[0]]
    Hy = 2 * torch.einsum('ia,rij,jb->rab', N4, Qc, N4)
    Gm = torch.outer(c, c) + Jy @ Jy.T + torch.einsum('rab,sab->rs', Hy, Hy)
    ev, V = torch.linalg.eigh(Gm)
    rr = int((ev > 1e-10 * ev[-1]).sum()); Ur = V[:, -rr:]
    c = Ur.T @ c; Jy = Ur.T @ Jy; Hy = torch.einsum('rs,rab->sab', Ur, Hy); C6 = C6 @ Ur
    return dict(c=c, J=Jy, H=Hy, C6=C6, u0=u0, N=N, jets=jets, sizes=sizes, U=U)


def construct(pc, tol=1e-9):
    c = pc['c'].cpu().numpy(); J = pc['J'].cpu().numpy(); H = pc['H'].cpu().numpy()
    m, n = J.shape
    Hs = np.concatenate([H[i] for i in range(m)], axis=1)
    Uq, s, _ = np.linalg.svd(Hs, full_matrices=False)
    r = int((s > tol * s[0]).sum()); P, K = Uq[:, :r], Uq[:, r:]
    JK = J @ K
    Ul, sl, _ = np.linalg.svd(JK, full_matrices=True)
    rw = int((sl > tol * sl[0]).sum())
    Pi = Ul[:, rw:]
    # nontrivial surviving functionals
    M = np.concatenate([Pi.T @ c[:, None], Pi.T @ J, np.einsum('ri,rab->iab', Pi, H).reshape(Pi.shape[1], -1)], axis=1)
    Um, sm, _ = np.linalg.svd(M, full_matrices=False)
    keep = sm > 1e-9 * sm[0]
    Pin = Pi @ Um[:, keep]
    info = {'quad_rank': r, 'rank_JK': rw, 'n_surv': int(Pin.shape[1])}
    if Pin.shape[1] != 1:
        return None, info
    pi = Pin[:, 0]
    Hpi = P.T @ np.einsum('i,iab->ab', pi, H) @ P; jv = (pi @ J) @ P; cp = float(pi @ c)
    ev, V = np.linalg.eigh(Hpi)
    if ev[-1] < 0:
        pi, Hpi, jv, cp = -pi, -Hpi, -jv, -cp; ev, V = np.linalg.eigh(Hpi)
    info['Hpi_eig'] = [float(ev[0]), float(ev[-1])]; info['definite'] = bool(ev[0] > 0)
    if not info['definite']:
        return None, info
    zs = -np.linalg.solve(Hpi, jv)
    Phi6 = cp + jv @ zs + 0.5 * zs @ Hpi @ zs
    info['Phi6'] = float(Phi6)
    if Phi6 <= 0:
        t = np.sqrt(-2 * Phi6 / ev[0]); z = zs + t * V[:, 0]
    else:
        z = zs
    info['phi_at_z'] = float(cp + jv @ z + 0.5 * z @ Hpi @ z)
    yP = P @ z
    rhs = -(c + J @ yP + 0.5 * np.einsum('rab,a,b->r', H, yP, yP))
    w, *_ = np.linalg.lstsq(JK, rhs, rcond=None)
    y = yP + K @ w
    Psi = c + J @ y + 0.5 * np.einsum('rab,a,b->r', H, y, y)
    info['Psi_norm'] = float(np.linalg.norm(Psi)); info['Psi_dot_pi'] = float(pi @ Psi)
    info['y_norm'] = float(np.linalg.norm(y))
    return dict(y=y, pi=pi, P=P, Hpi=Hpi, jv=jv, cpi=cp, z=z), info


def evaluate(T, H2, H3, pc, y):
    dev, dt = G.dev, G.dt
    u = pc['u0'] + pc['N'] @ torch.tensor(y, dtype=dt, device=dev)
    n8 = T.size[8]; z8 = torch.zeros(n8, dtype=dt, device=dev)
    jets0 = pc['jets'](u, z8)
    e6_0 = T.Evec(jets0, [6])[0]
    f8 = lambda h: T.Evec({**G.zeros(T), 8: h}, [6])[0]
    L6 = G.batched_cols(f8, n8, f8(z8))
    H8 = torch.linalg.lstsq(L6, -e6_0.unsqueeze(1)).solution[:, 0]
    jets = pc['jets'](u, H8)
    res = {}
    for k in range(0, 7):
        res[f'E{k}'] = float(T.Evec(jets, [k])[0].norm())
    res['E6_before_H8'] = float(e6_0.norm())
    jout = {d: v.cpu().numpy() for d, v in jets.items()}
    return res, jout


def run(tag, jet, lam):
    t0 = time.time()
    T = G.TowerAll(6, lam)
    H2 = G.make_H2(T, 'jet', lam, np.random.default_rng(0), jet, 1.0, 0.0)
    H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
    jc = jet_coords(T.torsion({2: H2, **G.zeros(T, skip=(2,))}))
    pc = full_pieces(T, H2, H3)
    sol, info = construct(pc)
    rec = {'tag': tag, 'lam': lam, 'jet_coords': jc, 'jet_input': {'c': [jet[0].real, jet[0].imag],
           'S': [[[complex(x).real, complex(x).imag] for x in row] for row in jet[1]],
           'A': [[[complex(x).real, complex(x).imag] for x in row] for row in jet[2]]}, **info}
    if sol is not None:
        res, jout = evaluate(T, H2, H3, pc, sol['y'])
        rec['unreduced_residuals'] = res
        ell = (pc['C6'].cpu().numpy() @ sol['pi'])
        np.savez(OUT / f'recon_{tag}.npz', **{f'H{d}': v for d, v in jout.items()},
                 u0=pc['u0'].cpu().numpy(), N=pc['N'].cpu().numpy(), C6=pc['C6'].cpu().numpy(),
                 ell=ell, pi=sol['pi'], P=sol['P'], Hpi=sol['Hpi'], jv=sol['jv'], cpi=sol['cpi'], z=sol['z'], y=sol['y'],
                 mons=np.array(T.R.mons), **{f'mon_d{d}': np.array(T.mon_d[d]) for d in T.degs})
    rec['time'] = time.time() - t0
    print(json.dumps({k: v for k, v in rec.items() if k not in ('jet_input',)}, default=float), flush=True)
    (OUT / f'recon_{tag}.json').write_text(json.dumps(rec, indent=1, default=float) + '\n')
    return rec


def as_jet(c, S, A):
    S = np.asarray(S, dtype=complex); A = np.asarray(A, dtype=complex)
    return (complex(c), [[complex(S[i, j]) for j in range(2)] for i in range(2)], [[complex(A[i, j]) for j in range(2)] for i in range(2)])


def main():
    from step80_lambda_scan import unit_jet
    from step80_F012_scan import random_cone_jet
    r21 = np.random.default_rng(21); j0 = unit_jet(r21)
    r42 = np.random.default_rng(42); gens = [random_cone_jet(r42, 'generic') for _ in range(8)]
    cases = [('lsA_jet0_lam-40', as_jet(*j0), -40.0), ('lsA_jet0_lam-1', as_jet(*j0), -1.0),
             ('F012_gen2_lam0', as_jet(*gens[2]), 0.0), ('F012_gen2_lam-5', as_jet(*gens[2]), -5.0),
             ('F012_gen5_lam-5', as_jet(*gens[5]), -5.0)]
    sel = sys.argv[1:] or [c[0] for c in cases]
    for tag, jet, lam in cases:
        if tag in sel:
            run(tag, jet, lam)


if __name__ == '__main__':
    main()
