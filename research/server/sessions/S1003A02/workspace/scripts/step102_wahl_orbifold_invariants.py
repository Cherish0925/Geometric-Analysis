#!/usr/bin/env python3
"""Step 102: verify the Dedekind-sum identity for Wahl singularities 1/n^2(1,n-1)
and confirm K^2-invariance of the orbifold characteristic numbers.

Key identity to verify:
  s(n-1, n^2) = (n^2-1)/(6n^2)

Consequence:
  signature defect = 4s(n-1,n^2) = (2/3)(1-1/n^2)
  chi_orb = chi(M) - t(1-1/n^2)
  tau_orb = sigma(M) + t*(2/3)(1-1/n^2)
  => 2*chi_orb + 3*tau_orb = 2*chi(M) + 3*sigma(M) = A - k.
"""

from fractions import Fraction
import json, os, math


def dedekind_sum_exact(a, b):
    """Exact Dedekind sum s(a,b) = sum_{k=1}^{b-1} ((k/b))((ka/b))
    where ((x)) = x - floor(x) - 1/2 for x not integer, 0 for x integer."""
    s = Fraction(0)
    for k in range(1, b):
        x = Fraction(k, b)
        y = Fraction(k * a, b)
        # ((x)) for x not integer
        frac_x = x - int(x) if x == int(x) else x - math.floor(float(x))
        frac_y = y - int(y) if y == int(y) else y - math.floor(float(y))
        # Use exact floor
        frac_x = x - (x.__floor__() if hasattr(x, '__floor__') else Fraction(math.floor(float(x))))
        frac_y = y - (y.__floor__() if hasattr(y, '__floor__') else Fraction(math.floor(float(y))))
        
        # ((x)) = frac(x) - 1/2 if frac(x) != 0, else 0
        if frac_x == 0:
            bx = Fraction(0)
        else:
            bx = frac_x - Fraction(1, 2)
        if frac_y == 0:
            by = Fraction(0)
        else:
            by = frac_y - Fraction(1, 2)
        s += bx * by
    return s


def floor_frac(q):
    """Floor of a Fraction."""
    return q.numerator // q.denominator if q >= 0 else -((-q.numerator + q.denominator - 1) // q.denominator)


def dedekind_sum_exact_v2(a, b):
    """Exact Dedekind sum using Fraction arithmetic only."""
    s = Fraction(0)
    for k in range(1, b):
        x = Fraction(k, b)
        y = Fraction(k * a, b)
        fx = x - floor_frac(x)
        fy = y - floor_frac(y)
        bx = (fx - Fraction(1, 2)) if fx != 0 else Fraction(0)
        by = (fy - Fraction(1, 2)) if fy != 0 else Fraction(0)
        s += bx * by
    return s


def predicted_dedekind(n):
    """s(n-1, n^2) = (n^2 - 1)/(6n^2)."""
    return Fraction(n * n - 1, 6 * n * n)


def run():
    results = []
    all_ok = True
    
    for n in range(2, 25):
        p = n * n
        q = n - 1
        if math.gcd(q, p) != 1:
            continue
        
        s_exact = dedekind_sum_exact_v2(q, p)
        s_pred = predicted_dedekind(n)
        
        match = (s_exact == s_pred)
        if not match:
            all_ok = False
        
        # Signature defect = 4s
        sig_defect = 4 * s_exact
        # Euler correction per point: 1 - 1/n^2
        euler_corr = Fraction(n * n - 1, n * n)
        
        # K^2 check: -2*euler_corr + 3*sig_defect should be 0
        k2_check = -2 * euler_corr + 3 * sig_defect
        k2_ok = (k2_check == 0)
        if not k2_ok:
            all_ok = False
        
        row = {
            "n": n,
            "p": p,
            "q": q,
            "s_exact": str(s_exact),
            "s_predicted": str(s_pred),
            "match": match,
            "sig_defect": str(sig_defect),
            "euler_corr": str(euler_corr),
            "K2_check": str(k2_check),
            "K2_invariant": k2_ok,
        }
        results.append(row)
        
        if n <= 10:
            print(f"n={n:2d}: s({q},{p}) = {s_exact} = {s_pred} {'✓' if match else '✗'}  "
                  f"K²-inv: {'✓' if k2_ok else '✗'}")
    
    # Also verify the reciprocity law for selected n
    recip_checks = []
    for n in [3, 5, 7, 11, 13]:
        a, b = n - 1, n * n
        sa = dedekind_sum_exact_v2(a, b)
        sb = dedekind_sum_exact_v2(b % a, a) if a > 1 else Fraction(0)
        rhs = Fraction(a*a + b*b + 1, 12*a*b) - Fraction(1, 4)
        check = (sa + sb == rhs)
        recip_checks.append({"n": n, "reciprocity_ok": check})
        if not check:
            all_ok = False
    
    print(f"\n{len(results)} cases; all_ok = {all_ok}")
    print(f"Reciprocity checks: {recip_checks}")
    
    outdir = "data/step102"
    os.makedirs(outdir, exist_ok=True)
    out = {
        "description": "Wahl orbifold invariants: Dedekind sum s(n-1,n^2) = (n^2-1)/(6n^2) "
                       "and K^2-invariance 2*chi_orb + 3*tau_orb = 2*chi(M) + 3*tau(M)",
        "cases": len(results),
        "all_ok": all_ok,
        "reciprocity_checks": recip_checks,
        "rows": results,
    }
    with open(os.path.join(outdir, "wahl_orbifold_invariants.json"), "w") as f:
        json.dump(out, f, indent=1)
    
    assert all_ok, "Some checks failed!"


if __name__ == "__main__":
    run()
