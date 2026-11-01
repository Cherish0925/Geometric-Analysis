#!/usr/bin/env python3
"""Step 80: map F0, F1, F2 (quadratic Phi6(lam) = F0 + F1*lam + F2*lam^2) across many cone jets.

Since Phi6 is exactly quadratic in lam, 3 lam-values suffice per jet.
Weighted homogeneity: F0 has weight 8, F1 weight 6, F2 weight 4 in the torsion jet.
With unit torsion norm, the angular part of the jet parametrizes a real algebraic variety.
Goal: determine whether F2 < 0 universally, F0 > 0 universally, and how the obstructed band width depends
on the cone angle.  Also: at the D6 (near-degenerate) jet, check the band explicitly.
Output: workspace/data/step80/F012_scan.json
"""
import json, sys, os, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step80')
import step79_general_order6 as G
from step77_gn_germ import jet_coords
from step80_universal_pi import reduce_full, surviving_functional, phi6_of, cone_jet

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step80'
OUT.mkdir(exist_ok=True)


def phi6_at(T, c, S, A, lam, wdir):
    rs = np.random.default_rng(wdir)
    S2 = np.asarray(S, dtype=complex); A2 = np.asarray(A, dtype=complex)
    jet = (complex(c), [[complex(S2[i,j]) for j in range(2)] for i in range(2)],
           [[complex(A2[i,j]) for j in range(2)] for i in range(2)])
    H2 = G.make_H2(T, 'jet', lam, rs, jet, 1.0, 0.0)
    H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
    cF, JF, HF, C6, info = reduce_full(T, H2, H3)
    Pin, P, rec, (cn, Jn, Hn) = surviving_functional(cF, JF, HF)
    if rec['n_surv'] == 1:
        pi = Pin[:, 0]; nrm = np.linalg.norm(C6.cpu().numpy() @ pi); pi = pi / nrm
        ph, _ = phi6_of(pi, P, cn, Jn, Hn); rec.update(ph)
    return rec


def fit_quadratic(lams, phis):
    """exact quadratic fit from 3 points"""
    if len(lams) == 3:
        A = np.array([[l**2, l, 1] for l in lams])
        return np.linalg.solve(A, phis)   # [a, b, c] = [F2, F1, F0]
    return np.polyfit(lams, phis, 2)


def random_cone_jet(rng, mode='generic'):
    cz = lambda: complex(*rng.standard_normal(2))
    c = cz(); S = np.array([[cz(), cz()], [0, cz()]]); S[1, 0] = S[0, 1]
    if mode == 'smallc':
        c *= 0.05
    if mode == 'bigc':
        c *= 3.0
    if mode == 'purec':
        S = np.zeros((2, 2), dtype=complex)
    s2 = np.sum(abs(S) ** 2)
    amod = np.sqrt((s2 + 8 * abs(c) ** 2) / 2)
    a = amod * np.exp(1j * rng.uniform(0, 2 * np.pi))
    A = np.array([[0, a], [-a, 0]])
    tn = np.sqrt(4 * abs(c) ** 2 + 2 * s2 + 4 * abs(a) ** 2)
    return c / tn, S / tn, A / tn


def main():
    rng = np.random.default_rng(42)
    lams3 = [-5.0, 0.0, 5.0]    # three points for exact quadratic
    out = {'lams': lams3, 'jets': []}
    Ts = {l: G.TowerAll(6, l) for l in lams3}
    
    cases = []
    for i in range(8):
        c, S, A = random_cone_jet(rng, 'generic')
        cases.append((f'gen{i}', (c, S, A)))
    for i in range(4):
        c, S, A = random_cone_jet(rng, 'smallc')
        cases.append((f'smallc{i}', (c, S, A)))
    for i in range(4):
        c, S, A = random_cone_jet(rng, 'bigc')
        cases.append((f'bigc{i}', (c, S, A)))
    # a01 shared jet
    c = 1.0+0j; S = np.array([[2, 1], [1, 1+1j]]); a = 2+2j; A = np.array([[0, a], [-a, 0]])
    tn = np.sqrt(4*abs(c)**2 + 2*np.sum(abs(S)**2) + 4*abs(a)**2)
    cases.append(('a01pt', (c/tn, S/tn, A/tn)))
    # D6 jet (near-degenerate c)
    cases.append(('d6jet', None))   # will load from file
    
    for tag, jet in cases:
        t0 = time.time()
        phis = []
        jc0 = None
        for lam in lams3:
            T = Ts[lam]
            if tag == 'd6jet':
                H2 = G.make_H2(T, 'd6', lam, rng)
                H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
                cF, JF, HF, C6, info = reduce_full(T, H2, H3)
                Pin, P, rec, (cn, Jn, Hn) = surviving_functional(cF, JF, HF)
                if rec['n_surv'] == 1:
                    pi = Pin[:, 0]; nrm = np.linalg.norm(C6.cpu().numpy() @ pi); pi = pi / nrm
                    ph, _ = phi6_of(pi, P, cn, Jn, Hn); rec.update(ph)
                if jc0 is None:
                    jc0 = jet_coords(T.torsion({2: H2, **G.zeros(T, skip=(2,))}))
            else:
                c_j, S_j, A_j = jet
                rec = phi6_at(T, c_j, S_j, A_j, lam, 2000 + abs(hash(tag)) % 1000)
                if jc0 is None:
                    rs2 = np.random.default_rng(2000 + abs(hash(tag)) % 1000)
                    c_j, S_j, A_j = jet
                    S2j = np.asarray(S_j, dtype=complex); A2j = np.asarray(A_j, dtype=complex)
                    jt = (complex(c_j), [[complex(S2j[i,j]) for j in range(2)] for i in range(2)],
                          [[complex(A2j[i,j]) for j in range(2)] for i in range(2)])
                    H2t = G.make_H2(T, 'jet', lam, rs2, jt, 1.0, 0.0)
                    jc0 = jet_coords(T.torsion({2: H2t, **G.zeros(T, skip=(2,))}))
            phis.append(rec.get('Phi6'))
        
        if all(p is not None for p in phis):
            F2, F1, F0 = fit_quadratic(lams3, phis)
            disc = F1**2 - 4*F2*F0
            r = {}
            r['F0'] = float(F0); r['F1'] = float(F1); r['F2'] = float(F2); r['disc'] = float(disc)
            if disc > 0:
                r1 = (-F1 - np.sqrt(disc)) / (2*F2)
                r2 = (-F1 + np.sqrt(disc)) / (2*F2)
                r['lam_minus'] = float(min(r1, r2)); r['lam_plus'] = float(max(r1, r2))
                r['band_width'] = float(max(r1, r2) - min(r1, r2))
            tn = np.sqrt(4*jc0['c2'] + 2*jc0['S2'] + 2*jc0['A2'])
            r['jet'] = jc0; r['tag'] = tag; r['tn'] = float(tn); r['time'] = time.time() - t0
            r['c2_frac'] = float(jc0['c2'] / (jc0['c2'] + jc0['S2'] + jc0['A2']))
            out['jets'].append(r)
            bw = r.get('band_width', np.inf)
            lm_ = r.get('lam_minus', float('nan')); lp_ = r.get('lam_plus', float('nan'))
            print(f'{tag:12s}  F0={F0:10.5f}  F1={F1:10.5f}  F2={F2:12.8f}  band=({lm_:8.2f},{lp_:8.2f})  width={bw:8.2f}  c2frac={r["c2_frac"]:.4f}  phis={[round(p,5) for p in phis]}', flush=True)
        else:
            out['jets'].append({'tag': tag, 'jet': jc0, 'phi6_values': phis, 'error': 'not all reduced'})
            print(f'{tag:12s}  Phi6 = {phis}  (SPECIAL / not all reduced)', flush=True)
    
    (OUT / 'F012_scan.json').write_text(json.dumps(out, indent=1, default=float) + '\n')
    
    # summary statistics
    fj = [j for j in out['jets'] if 'F0' in j]
    print('\n=== Summary ===')
    print(f'n_jets = {len(fj)}')
    print(f'F0 range: [{min(j["F0"] for j in fj):.6f}, {max(j["F0"] for j in fj):.6f}]  ALL POSITIVE: {all(j["F0"]>0 for j in fj)}')
    print(f'F2 range: [{min(j["F2"] for j in fj):.8f}, {max(j["F2"] for j in fj):.8f}]  ALL NEGATIVE: {all(j["F2"]<0 for j in fj)}')
    widths = [j.get('band_width', np.inf) for j in fj]
    print(f'Band widths: [{min(widths):.2f}, {max(widths):.2f}]')
    print(f'lam_minus range: [{min(j.get("lam_minus",-999) for j in fj):.2f}, {max(j.get("lam_minus",-999) for j in fj):.2f}]')
    print(f'lam_plus range: [{min(j.get("lam_plus",999) for j in fj):.2f}, {max(j.get("lam_plus",999) for j in fj):.2f}]')


if __name__ == '__main__':
    main()
