#!/usr/bin/env python3
"""Step 74: (a) exact P of the conformally flat scalar-flat neck and its Z2 quotient (the football Green cap);
(b) gluing error scaling check for the Green-cap insertion profile (warped model);
(c) Einstein-orbifold-bulk screening with scalar transfer and the transferred LeBrun mixed inequality.

Conventions (session ledger): P=int|Ric0|^2, S=int s^2, I+-=int|W+-|^2,
16 pi^2 chi = S/12 + 2W - P,  12 pi^2 tau = I+ - I-.
Bubble charges (A02 Step 55, eq. 1.1): c_pm = 2/|Gamma| - 2chi -+ 3tau -+ 3eta, so P(N)=4I_pm+S/12+8pi^2 c_pm.
CH host X (A=c1^2), resolution M=X#k CPbar^2:  T_+^orb(V)=A-k+C_+,  T_-^orb(V)=A/3+5k+C_-.
Output: workspace/data/step74/neck_and_screen.json
"""
import json, pathlib, math
import sympy as sp
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / 'data' / 'step74'
OUT.mkdir(parents=True, exist_ok=True)
A02 = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step55_orbifold_bubble_charges.json'

res = {}

# ---------------- (a) neck  g = u(r)^2 (dr^2 + r^2 g_S3), u = 1 + c/r^2 ----------------
r, c = sp.symbols('r c', positive=True)
u = 1 + c / r**2
a = r * u                      # warping function in arclength t, dt = u dr
d_dt = lambda F: sp.diff(F, r) / u
ap = sp.simplify(d_dt(a)); app = sp.simplify(d_dt(ap))
Rtt = sp.simplify(-3 * app / a)                       # Ric(e_t,e_t)
Rss = sp.simplify(-app / a + 2 * (1 - ap**2) / a**2)  # Ric(e_i,e_i) on S3 unit frame
s = sp.simplify(Rtt + 3 * Rss)
ric0sq = sp.simplify((Rtt - s / 4)**2 + 3 * (Rss - s / 4)**2)
vol_density = a**3 * u * 2 * sp.pi**2                 # d vol = a^3 dt dvol_S3, dt=u dr
Pneck = sp.simplify(sp.integrate(sp.simplify(ric0sq * vol_density), (r, 0, sp.oo)))
# decay of Ric along the end
ric_decay = sp.limit(sp.sqrt(ric0sq) * r**4, r, sp.oo)
res['neck'] = {
    'scalar_curvature': str(s),
    'P_neck': str(Pneck), 'P_neck_over_pi2': str(sp.simplify(Pneck / sp.pi**2)),
    'P_quotient_cap_over_pi2': str(sp.simplify(Pneck / (2 * sp.pi**2))),
    'lim r^4|Ric0|': str(sp.simplify(ric_decay)),
    'note': 'conformally flat => W=0; involution x -> sigma(x) c/|x|^2, sigma=diag(-1,-1,-1,1), is an isometry '
            'with two fixed points on |x|^2=c, linearization -I (A1), exchanging ends; quotient P = P_neck/2.'
}
print(res['neck'], flush=True)

# ---------------- (b) gluing tail estimate: P(h) - P(h on B_R) ~ R^{-4} ----------------
Rr = sp.symbols('R', positive=True)
tail = sp.simplify(sp.integrate(sp.simplify((ric0sq * vol_density).subs(c, 1)), (r, Rr, sp.oo)))
res['neck']['tail_P_outside_R(c=1)'] = str(tail)
res['neck']['tail_leading'] = str(sp.series(tail, Rr, sp.oo, 6).removeO())

# ---------------- (c) screening ----------------
mp.mp.dps = 40

def nc_margin(A, k, Cp, Cm):
    """Return (scalar_ok, interval_nonempty, best f^2 - (6A+C+)) for an Einstein orbifold bulk
    whose Ricci-flat fillers have total charges (C+,C-), CH host with c1^2=A, resolution X#k CPbar^2."""
    A, k, Cp, Cm = map(mp.mpf, (A, k, Cp, Cm))
    Tp = A - k + Cp; Tm = A / 3 + 5 * k + Cm
    lo = A / 3; hi = min(Tp, Tm)
    scalar_ok = bool(hi >= lo)
    if not scalar_ok:
        return scalar_ok, False, None
    x = min(max(8 * Tp / 9, lo), hi)
    f2 = (mp.sqrt(8 * x) + mp.sqrt(Tp - x))**2
    return scalar_ok, True, float(f2 - (6 * A + Cp))

def asym(k, Cp, Cm):
    # large-A leading order of the mixed test: 9 C_- + 2 C_+ + 42 k >= 0 ; scalar test: C_- >= -5k
    return {'mixed_linear': float(9 * Cm + 2 * Cp + 42 * k), 'scalar_linear': float(Cm + 5 * k)}

Alist = [9, 18, 27, 36, 45, 90, 180, 900, 9000, 90000]

def screen(k, Cp, Cm):
    rows = {}
    for A in Alist:
        s_ok, nonempty, m = nc_margin(A, k, Cp, Cm)
        rows[A] = {'scalar_ok': s_ok, 'mixed_ok': bool(nonempty and m >= -1e-25), 'margin': m}
    return {'byA': rows, 'asym': asym(k, Cp, Cm)}

F = sp.Rational
out = {}

# (c1) paired A1: k=2m EH, C+=0, C-=-6k
out['paired_A1_k2'] = screen(2, 0, -12)

# (c2) Kronheimer ADE fillers (Ricci-flat Kaehler, complex orientation matched): c+=0, c-=-4(chi-1/|Gamma|)
ade = {**{f'A{n}': (n, n + 1) for n in range(1, 11)}, 'D4': (4, 8), 'D5': (5, 12), 'D6': (6, 16), 'D7': (7, 20), 'E6': (6, 24), 'E7': (7, 48), 'E8': (8, 120)}
kron = {}
for name, (rk, G) in ade.items():
    cm = -4 * (rk + 1 - F(1, G))
    # carrying k = rank classes (the minimal-rank assignment) and also k=rank+1, k=2 rank
    kron[name] = {'c-': str(cm)}
    for k in sorted({rk, rk + 1, 2 * rk}):
        kron[name][f'k={k}'] = screen(k, 0, cm)
out['kronheimer_single_filler'] = kron

# (c3) universal budget for Ricci-flat Kaehler fillers in matched complex orientation:
#   sum_j (chi_j - 1/|Gamma_j|) <= 7k/6  (large A),  exact: A/3+5k+C_- >= (A/27)(4-sqrt(1-3k/A))^2
out['kaehler_RF_budget_statement'] = 'sum_j(chi(N_j)-1/|Gamma_j|) <= 7k/6 - k^2/(12A) - O(k^3/A^2)'
def kahler_budget_exact(A, k):
    A = mp.mpf(A); k = mp.mpf(k)
    t = mp.sqrt(1 - 3 * k / A)
    xmin = A / 27 * (4 - t)**2
    # C_- >= xmin - A/3 - 5k ;  C_- = -4 sum(chi-1/G)
    return float(-(xmin - A / 3 - 5 * k) / 4)
out['kaehler_RF_budget_exact'] = {str(A): {str(k): kahler_budget_exact(A, k) for k in (1, 2, 3, 4, 6) if 3 * k <= A}
                                  for A in Alist}

# (c4) A02 Step-55 rows at k=1 (single b2<=1 filler). Ricci-flat compatibility requires c+<=0 and c-<=0.
d = json.loads(A02.read_text())
cat = {}
for key in ['b2_one_cyclic_simply_connected', 'rational_ball_lens']:
    lst = []
    for row in d[key]:
        cp = F(row['c+']); cm = F(row['c-'])
        rf_ok = bool(cp <= 0 and cm <= 0)
        entry = {'n': row['n'], 'q': row['q'], 'c+': str(cp), 'c-': str(cm), 'RF_charge_compatible': rf_ok}
        if 'T_type_(q=mk-1 or inverse)' in row:
            entry['T_type'] = row['T_type_(q=mk-1 or inverse)']
        if rf_ok:
            sc = screen(1, cp, cm)
            entry['scalar_ok_all_A'] = all(v['scalar_ok'] for v in sc['byA'].values())
            entry['mixed_ok_all_A'] = all(v['mixed_ok'] for v in sc['byA'].values())
            entry['mixed_ok_A'] = [A for A, v in sc['byA'].items() if v['mixed_ok']]
            entry['scalar_ok_A'] = [A for A, v in sc['byA'].items() if v['scalar_ok']]
            entry['asym'] = sc['asym']
            entry['survives_large_A'] = bool(sc['byA'][Alist[-1]]['mixed_ok'])
            entry['scalar_only_large_A'] = bool(sc['byA'][Alist[-1]]['scalar_ok'])
        lst.append(entry)
    cat[key] = lst
ade_rows = []
for name, row in d['b2_one_ADE_end_in_M_orientation'].items():
    cp = F(row['c+']); cm = F(row['c-'])
    rf_ok = bool(cp <= 0 and cm <= 0)
    entry = {'end': name, 'c+': str(cp), 'c-': str(cm), 'RF_charge_compatible': rf_ok}
    if rf_ok:
        sc = screen(1, cp, cm)
        entry['scalar_ok_all_A'] = all(v['scalar_ok'] for v in sc['byA'].values())
        entry['mixed_ok_all_A'] = all(v['mixed_ok'] for v in sc['byA'].values())
        entry['mixed_ok_A'] = [A for A, v in sc['byA'].items() if v['mixed_ok']]
        entry['scalar_ok_A'] = [A for A, v in sc['byA'].items() if v['scalar_ok']]
        entry['asym'] = sc['asym']
        entry['survives_large_A'] = bool(sc['byA'][Alist[-1]]['mixed_ok'])
        entry['scalar_only_large_A'] = bool(sc['byA'][Alist[-1]]['scalar_ok'])
    ade_rows.append(entry)
cat['b2_one_ADE_end_in_M_orientation'] = ade_rows

summ = {}
for key, lst in cat.items():
    rf = [e for e in lst if e['RF_charge_compatible']]
    summ[key] = {
        'rows': len(lst), 'RF_charge_compatible': len(rf),
        'large_A_pass_scalar': sum(e['scalar_only_large_A'] for e in rf),
        'large_A_pass_mixed': sum(e['survives_large_A'] for e in rf),
        'large_A_scalar_pass_mixed_fail': [(e.get('n', e.get('end')), e.get('q'), e['c+'], e['c-']) for e in rf
                                           if e['scalar_only_large_A'] and not e['survives_large_A']],
        'large_A_mixed_survivors': [(e.get('n', e.get('end')), e.get('q'), e['c+'], e['c-'], e.get('T_type'),
                                     min(e['mixed_ok_A']) if e['mixed_ok_A'] else None) for e in rf if e['survives_large_A']],
    }
out['A02_step55_k1'] = cat
out['A02_step55_k1_summary'] = summ
res['screen'] = out
(OUT / 'neck_and_screen.json').write_text(json.dumps(res, indent=1, default=str) + '\n')
print(json.dumps({'paired': out['paired_A1_k2']['asym'],
                  'kron': {n: {kk: (v['asym'], all(x['mixed_ok'] for x in v['byA'].values()))
                               for kk, v in kr.items() if kk.startswith('k=')} for n, kr in kron.items()},
                  'budget': out['kaehler_RF_budget_exact'], 'summary': summ}, indent=1, default=str))
