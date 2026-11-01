#!/usr/bin/env python3
"""Step 50: summary of the Yamabe/Weyl ledger along the perpendicular CH cell family, and
exact checks for the Kahler infimum (Arezzo-Pacard classes) and the ALE bubble charge.

Inputs : workspace/data/step50_family/ledger_x00.*.json  (written by step50_family_ledger.sh,
         which runs A01's step43_yamabe_lebrun_ledger.py, N=80000, on A01 perp_area records).
Output : workspace/data/step50_family_summary.json
Units  : 8 pi^2, relative to the replaced CH ball, scalar -4 (Ric=-g) scale; floating quadrature.
Ledger identity (Y0): saving := 1 - P(hat g)/8pi^2 = 4 (D_W - DeltaV)  (tail-free DeltaV).
"""
import glob, json, math, os
import sympy as sp

here = os.path.dirname(os.path.abspath(__file__))
dd = os.path.join(here, '..', 'data')
rows = []
for f in sorted(glob.glob(os.path.join(dd, 'step50_family', 'ledger_x00.*.json'))):
    d = json.load(open(f))
    s = d['saving_hat_identity']; dv = d['DeltaV_identity']; dw = dv + s / 4
    x0 = d['x0']
    rows.append(dict(record=os.path.basename(f), x0=x0, X=d['X'], P_g=d['P_g'], saving_hat=s,
                     DeltaV=dv, D_W=dw, ratio_DW_DV=dw / dv, efficiency=s / (4 * dv),
                     DeltaV_over_x0=dv / x0, saving_over_x0sq_log=s / (x0 ** 2 * math.log(1 / x0)),
                     Psi=d['Psi_int'], dist2=d['dist2_int'], LeB=d['LeB_term'], deltaW=d['dWeyl_rel'],
                     F_Y=d.get('F_Y_identity'), Y_allowance=4 * dv - 2 * d['Psi_int']))
rows.sort(key=lambda r: (r['x0'], r['X']))

# Kahler infimum: Omega = K - e^2 sum a_i E_i + (crepant classes c, K.c=0, c^2=-q<=0), K^2=A
A, e, q, k, a = sp.symbols('A e q k a', positive=True)
KM_Omega = A + e**2 * k * a          # (K + sum E).(K - e^2 a sum E): E.E=-1, K.E=0
Omega2 = A - e**4 * (k * a**2 + q)
Phat = sp.simplify(KM_Omega**2 / Omega2 - A + k)
lim = sp.limit(Phat, e, 0)
series = sp.series(Phat, e, 0, 3).removeO()

# ALE bubble charge  Phat >= 2/|G| - 2 chi + 3|tau + eta|  (single end); blow-up bubble R^4 # kb CP2bar
kb = sp.symbols('k_b', positive=True, integer=True)
charge_blowup = 2 - 2 * (1 + kb) + 3 * kb

out = dict(status='floating quadrature (cells); exact sympy (Kahler class, charge)',
           family=rows,
           max_efficiency=max(r['efficiency'] for r in rows),
           kahler_Phat_cscK=str(Phat), kahler_limit_e_to_0=str(lim), kahler_series=str(sp.expand(series)),
           blowup_bubble_charge=str(sp.simplify(charge_blowup)))
p = os.path.join(dd, 'step50_family_summary.json')
json.dump(out, open(p, 'w'), indent=1)
for r in rows:
    print(f"x0={r['x0']:.3f} X={r['X']:.0f} P={r['P_g']:.6f} s={r['saving_hat']:.6f} DV={r['DeltaV']:.5f} "
          f"DW/DV={r['ratio_DW_DV']:.5f} eff={r['efficiency']:.4f} DV/x0={r['DeltaV_over_x0']:.3f} "
          f"s/(x0^2 log)={r['saving_over_x0sq_log']:.3f} allowance={r['Y_allowance']:.4f}")
print('Phat_cscK =', Phat, '; limit =', lim, '; series =', sp.expand(series))
print('blow-up bubble charge =', sp.simplify(charge_blowup))
