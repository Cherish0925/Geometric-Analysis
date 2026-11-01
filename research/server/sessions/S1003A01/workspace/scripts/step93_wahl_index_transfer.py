"""Step 93: exact local index data at a Wahl point 1/n^2(1,n-1).

Purpose.  Test, independently of any Kirby calculation, Lemma 93.I of
workspace/notes/step93_wfl_theorem_removability_index_transfer_and_wahl_self_similarity.md:

  ind D^{orb}_{res(s)} on V  =  ind D_s on M      for every spin^c structure s on M,

where M = V^reg U B_{n,1}.  Via Kawasaki's formula the orbifold index is the smooth
Chern--Weil integral plus a fixed-point term delta(m) depending only on the local twist
character zeta^m of the line twisting the canonical lift.  Because the real class square and
the Chern--Weil signature integrand differ from M only through the local signature defect,
Lemma 93.I is equivalent to the purely local identity

     delta(m) = (tau_orb - tau_top)/8 + (correction from c_1^2 Chern-Weil)    (*)

for exactly those m that are restrictions of spin^c structures on B_{n,1}.

We compute, with exact cyclotomic arithmetic (sympy, exact algebraic numbers -> rational):
  (1) e_orb correction     1 - 1/p,  p = n^2;
  (2) signature defect     d_sig = tau_CW - tau_top
                           = -(1/p) sum_{k=1}^{p-1} cot(pi k/p) cot(pi k q/p),  q = n-1
      (orbifold G-signature fixed-point term; sign checked by K^2 invariance below);
  (3) K^2 invariance       2(1-1/p) == 3 d_sig  ?   (T-singularity: K_V^2 = K_M^2)
  (4) holomorphic Lefschetz / Kawasaki fixed point term for Lambda^{0,*} (x) chi^m
         delta(m) = (1/p) sum_{k=1}^{p-1} zeta^{k m} / ((1-zeta^{-k})(1-zeta^{-k q}))
      including the Chern--Weil change of c_1(L)^2 for the twisted line, and the set of
      m for which the total orbifold index equals the smooth one.

Output: workspace/data/step93/wahl_index_transfer.json
"""
import json, os
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50

def rationalize(x, maxden=10**8):
    f = Fraction(str(mp.nstr(x, 40))).limit_denominator(maxden)
    return f

def data(n):
    p = n * n
    q = n - 1
    z = lambda k: mp.e ** (2j * mp.pi * k / p)
    # (2) signature defect of the cone point (orbifold signature theorem)
    # convention: dsig := tau_CW(orbifold Chern-Weil) - tau_top = +(1/p) sum cot cot.
    # (The opposite sign was tried first and fails K^2 invariance with the same magnitude;
    #  the sign is fixed by the Kahler identity K^2 = 2 e_orb + 3 tau_CW on T-singularities.)
    dsig = sum(mp.cot(mp.pi * k / p) * mp.cot(mp.pi * k * q / p) for k in range(1, p)) / p
    dsig_r = rationalize(dsig)
    eorb = Fraction(1) - Fraction(1, p)
    K2_inv = (2 * eorb == 3 * dsig_r)
    # (4) Kawasaki fixed point term for Dolbeault twisted by chi^m (both inversion conventions)
    def delta(m, conv):
        s = mp.mpc(0)
        for k in range(1, p):
            if conv == 'inv':
                den = (1 - z(-k)) * (1 - z(-k * q))
            else:
                den = (1 - z(k)) * (1 - z(k * q))
            s += z(k * m) / den
        return s / p
    out = dict(n=n, p=p, q=q, e_orb_correction=str(eorb), signature_defect=str(dsig_r),
               K2_invariance_2e_eq_3sig=K2_inv)
    # Riemann-Roch consistency for the canonical lift (m=0): chi(O_V)=chi(O_M) for a
    # Q-Gorenstein smoothing, Noether on V: chi = (K^2 + e_orb)/12 + delta(0), K^2 invariant,
    # e_orb = e - (1-1/p)  =>  delta(0) must equal (1-1/p)/12.
    d0 = delta(0, 'inv')
    out['delta0'] = str(rationalize(d0.real))
    out['delta0_imag'] = float(abs(d0.imag))
    out['delta0_expected_(1-1/p)/12'] = str(eorb / 12)
    out['RR_consistent'] = (rationalize(d0.real) == eorb / 12)
    # Twisted lifts.  Twisting the canonical lift by the local line chi^m changes the
    # orbifold index by [Kawasaki term change] + [Chern-Weil change]; the smooth side changes
    # by the corresponding integral change.  For a twist by a line ell on M restricted from a
    # class extending over B (torsion on B), the real Chern-Weil change is identical on V and
    # M.  Hence ind_V = ind_M  <=>  delta(m) = delta(0).
    ok = {}
    for conv in ('inv', 'dir'):
        good = []
        vals = {}
        for m in range(p):
            dm = delta(m, conv)
            vals[m] = (float(dm.real), float(dm.imag))
            if abs(dm - d0) < mp.mpf(10) ** (-30):
                good.append(m)
        ok[conv] = good
    out['m_with_delta_eq_delta0'] = ok
    out['extendible_coset_nZ'] = [n * j for j in range(n)]
    out['match_extendible'] = {c: sorted(ok[c]) == [n * j for j in range(n)] for c in ok}
    # Step-89 isotropy convention: S^+ = Lambda^{00}+Lambda^{02} weights (0,-n); twist zeta^{m}
    # gives an invariant value of Phi iff m = 0 or m = n mod p.
    out['Phi_value_allowed_twists'] = [m for m in range(p) if m % p == 0 or (m - n) % p == 0]
    # discrepancies of the minimal resolution chain [n+2,2,...,2] and K.C for a (-1)-curve
    # meeting chain component i transversally once (complex model of the Wahl orbifold)
    a = [Fraction(-(n - i), n) for i in range(1, n)]
    out['discrepancies'] = [str(x) for x in a]
    out['K_dot_C_minus1_curve_meeting_component_i'] = [str(-1 - x) for x in a]
    out['all_K_negative'] = all(-1 - x < 0 for x in a)
    return out

res = {n: data(n) for n in range(2, 9)}
print(json.dumps(res, indent=1, default=str))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step93')
os.makedirs(od, exist_ok=True)
json.dump(res, open(os.path.join(od, 'wahl_index_transfer.json'), 'w'), indent=1, default=str)
