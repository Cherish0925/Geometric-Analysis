#!/usr/bin/env python3
"""Step 80: Phi6 as a function of lambda (and of the torsion-free W^- part of H2) at fixed unit-torsion cone jets.

Uses the universal surviving functional ell found in step80_universal_pi (cos = 1 across jets):
   Phi6(H2) = min { ell . E6(H) : H = H2 + H4 + ... + H7, E1..E5 = 0 }      (even branch, H3 = 0)
which is the reduced scalar c - j H^-1 j / 2 when the reduced Hessian is definite.
Tests: (i) exact polynomial degree of Phi6 in lambda (weight count allows degree <= 4);
       (ii) sign of Phi6 for |lambda| >> torsion (near-Kahler regime);
       (iii) universal quadratic form q_ell(H4) = ell . Q(H4,H4) on ALL of H4: spectrum.
Output: workspace/data/step80/lambda_scan_<tag>.json
"""
import json, sys, time, os
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step80')
import step79_general_order6 as G
from step77_gn_germ import jet_coords
from step80_universal_pi import reduce_full, surviving_functional, phi6_of

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step80'


def unit_jet(rng):
    cz = lambda: complex(*rng.standard_normal(2))
    c = cz(); S = np.array([[cz(), cz()], [0, cz()]]); S[1, 0] = S[0, 1]
    s2 = np.sum(abs(S) ** 2); amod = np.sqrt((s2 + 8 * abs(c) ** 2) / 2); a = amod * np.exp(1j * rng.uniform(0, 6.3))
    A = np.array([[0, a], [-a, 0]]); tn = np.sqrt(4 * abs(c) ** 2 + 2 * s2 + 4 * abs(a) ** 2)
    return c / tn, S / tn, A / tn


def run(T, jet, wdir, w, ell_ref=None):
    rs = np.random.default_rng(wdir)
    H2 = G.make_H2(T, 'jet', T.lam, rs, jet, 1.0, w)
    H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
    cF, JF, HF, C6, info = reduce_full(T, H2, H3)
    Pin, P, rec, (cn, Jn, Hn) = surviving_functional(cF, JF, HF)
    rec.update(info)
    if Pin.shape[1] == 1:
        pi = Pin[:, 0]; ell = C6.cpu().numpy() @ pi; nrm = np.linalg.norm(ell); pi = pi / nrm
        ph, pi = phi6_of(pi, P, cn, Jn, Hn); rec.update(ph)
        ell = C6.cpu().numpy() @ pi
        if ell_ref is not None:
            rec['cos_ref'] = float(ell @ ell_ref)
            if rec['cos_ref'] < 0:     # fix sign convention to the reference functional
                rec['Phi6_signed_ref'] = None
        rec['ell'] = ell
    return rec


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=21)
    ap.add_argument('--njets', type=int, default=2)
    ap.add_argument('--lams', default='-40,-20,-10,-5,-1,0,1,5,10,20,40')
    ap.add_argument('--ws', default='0')
    ap.add_argument('--tag', default='a')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    lams = [float(x) for x in a.lams.split(',')]; ws = [float(x) for x in a.ws.split(',')]
    jets = [unit_jet(rng) for _ in range(a.njets)]
    out = {'args': vars(a), 'records': []}
    ell_ref = None
    for lam in lams:
        T = G.TowerAll(6, lam)
        for ij, jet in enumerate(jets):
            for w in ws:
                t0 = time.time()
                rec = run(T, jet, 1000 + ij, w, ell_ref)
                ell = rec.pop('ell', None)
                if ell_ref is None and ell is not None:
                    ell_ref = ell
                    np.save(OUT / f'ell_ref_{a.tag}.npy', ell_ref)
                jc = jet_coords(T.torsion({2: G.make_H2(T, 'jet', lam, np.random.default_rng(1000 + ij), jet, 1.0, w), **G.zeros(T, skip=(2,))}))
                r = {'jet_index': ij, 'lam': lam, 'w': w, 'jet': jc, **{k: v for k, v in rec.items()}, 'time': time.time() - t0}
                out['records'].append(r)
                print('jet', ij, 'lam', lam, 'w', w, {k: r.get(k) for k in ('quad_rank', 'rank_JK', 'n_surv', 'definite', 'c', 'Phi6', 'cos_ref')}, round(r['time'], 1), flush=True)
                (OUT / f'lambda_scan_{a.tag}.json').write_text(json.dumps(out, indent=1, default=float) + '\n')
    # universal q_ell spectrum on all of H4
    Qc = G._CACHE['Qc']; C6 = G._CACHE['C6']
    pi_full = torch.tensor(C6.cpu().numpy().T @ ell_ref, dtype=G.dt, device=G.dev)
    q = torch.einsum('r,rij->ij', pi_full, Qc); q = (q + q.T) / 2
    ev = torch.linalg.eigvalsh(q).cpu().numpy()
    out['q_ell_spectrum'] = {'n_pos': int((ev > 1e-9 * abs(ev).max()).sum()), 'n_neg': int((ev < -1e-9 * abs(ev).max()).sum()),
                             'min': float(ev[0]), 'max': float(ev[-1]), 'all': [float(x) for x in ev]}
    print('q_ell on all H4:', {k: v for k, v in out['q_ell_spectrum'].items() if k != 'all'})
    # polynomial fit in lambda per jet / w
    fits = []
    for ij in range(a.njets):
        for w in ws:
            rr = [r for r in out['records'] if r['jet_index'] == ij and r['w'] == w and r.get('Phi6') is not None]
            L = np.array([r['lam'] for r in rr]); Y = np.array([r['Phi6'] * np.sign(r.get('cos_ref', 1.0)) for r in rr])
            for deg in (2, 3, 4):
                if len(L) > deg + 1:
                    cf = np.polyfit(L, Y, deg); resid = float(np.abs(np.polyval(cf, L) - Y).max())
                    fits.append({'jet': ij, 'w': w, 'deg': deg, 'coef_high_to_low': [float(x) for x in cf], 'max_resid': resid})
                    print('fit jet', ij, 'w', w, 'deg', deg, cf, 'resid %.2e' % resid)
    out['fits'] = fits
    (OUT / f'lambda_scan_{a.tag}.json').write_text(json.dumps(out, indent=1, default=float) + '\n')


if __name__ == '__main__':
    main()
