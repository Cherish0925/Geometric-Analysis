"""Validated transport of the Fuchsian bolt boxes to time T and Wazewski entry check (b=4/5).

Input : fuchs_boxes_N*.json from ach_bolt_fuchs.py (rigorous boxes at t0 for d-subintervals,
        including the Fuchsian remainder).
Flow  : ach_bolt_capd (CAPD C0 Lohner, the exact rhs_md field, checked by ach_capd_field_check.py),
        chained in steps dt.
Check : at time T every box must lie in the verified cusp block B(K=1, zeta0=1e-2, Q=[0.70,0.90])
        (data/ach_block/block_K1_z0.01_q0.7_0.9.json) with q kept a drift-distance away from the
        q-faces, and the first/last d-subinterval must lie in the opposite egress slabs
        ub in [-1,-1/2] and [1/2,1].  The Wazewski argument then gives d in the d-interval whose
        orbit stays in B for all t >= T.
Output: data/ach_capd/wazewski_T*.json
"""
import json, math, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
BIN = HERE / 'ach_bolt_capd'
DATA = HERE.parent / 'data'


def run(box, dt, order):
    args = ['qiushi-yau26', 'env', 'ode', str(BIN), repr(dt), str(order)]
    for lo, hi in box: args += [repr(float(lo)), repr(float(hi))]
    cp = subprocess.run(args, text=True, capture_output=True)
    if cp.returncode:
        raise RuntimeError(cp.stderr.strip())
    return json.loads(cp.stdout)


def transport(entry, T, dt, order):
    box = entry['binary64_box']; t = entry['t0']; rec = None
    while T - t > 1e-12:
        h = min(dt, T - t)
        rec = run(box, h, order)
        box = [[float.fromhex(a), float.fromhex(b)] for a, b in rec['endpoint_hex']]
        t += h
    comp = {k: [float.fromhex(a), float.fromhex(b)] for k, (a, b) in rec['compact'].items()}
    return dict(d=entry['d'], t=t, endpoint=box, endpoint_hex=rec['endpoint_hex'], compact=comp,
                maxwidth=max(b - a for a, b in box))


if __name__ == '__main__':
    src = Path(sys.argv[1]); T = float(sys.argv[2]); dt = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
    order = int(sys.argv[4]) if len(sys.argv) > 4 else 30
    F = json.loads(src.read_text())
    blk = json.loads((DATA / 'ach_block' / 'block_K1_z0.01_q0.7_0.9.json').read_text())
    assert blk['all_ok']
    with ThreadPoolExecutor(max_workers=24) as ex:
        res = list(ex.map(lambda e: transport(e, T, dt, order), F['boxes']))
    ygh = blk['zeta_decay_factor_ygh_min']
    K = blk['K']; z0 = blk['zeta0']; Q = blk['q']
    checks = []
    for r in res:
        c = r['compact']
        zhi = c['zeta'][1]
        drift = (K + 4*math.sinh(max(abs(Q[0]), abs(Q[1]))))*zhi/ygh
        inside = (0 < c['zeta'][0] and zhi < z0 and
                  all(-K < c[k][0] and c[k][1] < K for k in ('s1b', 's2b', 'ab')) and
                  -K <= c['ub'][0] and c['ub'][1] <= K and
                  Q[0] + drift < c['q'][0] and c['q'][1] < Q[1] - drift)
        checks.append(dict(d=r['d'], inside=bool(inside), drift=drift, **{k: c[k] for k in c}))
    first, last = checks[0], checks[-1]
    slab = lambda c, sgn: (sgn*c['ub'][0] >= 0.5*K and sgn*c['ub'][1] <= K) if sgn > 0 else \
        (c['ub'][0] >= -K and c['ub'][1] <= -0.5*K)
    sgn = 1 if first['ub'][0] < 0 else -1
    endpoints_ok = slab(first, -sgn) and slab(last, sgn)
    # a priori enclosure of the asymptotic Rossi parameter q_inf: q stays within drift of q(T)
    qlo = min(c['q'][0] - c['drift'] for c in checks); qhi = max(c['q'][1] + c['drift'] for c in checks)
    out = dict(source=str(src), T=T, dt=dt, order=order, all_inside=all(c['inside'] for c in checks),
               endpoints_in_opposite_slabs=bool(endpoints_ok), q_inf_enclosure=[qlo, qhi],
               rho_inf_enclosure=[math.exp(qlo), math.exp(qhi)],
               max_endpoint_width=max(r['maxwidth'] for r in res), checks=checks, transported=res)
    print(json.dumps({k: v for k, v in out.items() if k not in ('checks', 'transported')}, indent=1))
    for c in checks:
        print(c['d'], c['inside'], 'ub', [round(x, 5) for x in c['ub']], 'zeta', c['zeta'][1],
              'q', [round(x, 6) for x in c['q']], 'phi', [round(x, 6) for x in c['phi']])
    (DATA / 'ach_capd' / f'wazewski_T{T:g}.json').write_text(json.dumps(out, indent=1))
