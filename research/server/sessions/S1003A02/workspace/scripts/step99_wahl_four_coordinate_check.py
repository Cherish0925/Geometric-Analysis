#!/usr/bin/env python3
"""Step 99: exact checks for the repaired four-coordinate Wahl discriminant construction.

For each Wahl link L(n^2,na-1), orientation sign sigma, and 2<=n<=NMAX,
choose the least positive N congruent to -sigma(na-1) modulo n^2 and represent N
as four squares.  For v in -I_4 define L_v={x : x.v=0 mod n}.  The script
constructs an integral kernel basis using Smith normal form, verifies index n,
Gram determinant n^2, cyclic discriminant group Z_{n^2}, and generator v/n of
order n^2 with the desired self-pairing.  It also records low-rank obstructions:
the minimum number k<=4 of squares representing some target square class modulo
n^2.  Output: workspace/data/step99/wahl_four_coordinate_check.json.

This is finite consistency evidence.  The general k<=4 sufficiency is Lagrange's
four-square theorem; the exact complement and discriminant arguments are proved
in notes/step96_suvaina_lattice_and_kahler_filler_theorem.md, Step-99 repair.
"""
import json
import math
import os
from fractions import Fraction

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step99", "wahl_four_coordinate_check.json")
NMAX = 16


def units_mod(n):
    return [u for u in range(1, n * n) if math.gcd(u, n) == 1]


def sums_of_k_squares(k, max_sum):
    """Map representable sums <= max_sum to one nonnegative k-tuple."""
    out = {}
    lim = math.isqrt(max_sum)
    def rec(prefix, start, remaining):
        if remaining == 0:
            s = sum(x*x for x in prefix)
            if s <= max_sum and s not in out:
                out[s] = list(prefix)
            return
        for x in range(start, lim + 1):
            s0 = sum(y*y for y in prefix) + x*x
            if s0 > max_sum:
                break
            rec(prefix + [x], x, remaining - 1)
    rec([], 0, k)
    return out


def kernel_basis(v, n):
    """Column basis for {x in Z^4 : v.x=0 mod n} via Smith decomposition."""
    # Integral solutions of v.x=nz are the first four coordinates of the
    # integer kernel of A=[v_1,...,v_4,-n].  Since gcd(v_1,...,v_4,n)=1,
    # Smith normal decomposition sends A to [1,0,0,0,0]; columns 2--5 of
    # the right transformation form a saturated basis of ker A.
    A = DomainMatrix.from_list_sympy(1, 5, [list(v) + [-n]]).convert_to(ZZ)
    S, left, right = smith_normal_decomp(A)
    assert (left * A * right).to_Matrix() == S.to_Matrix()
    R = right.to_Matrix()
    B = R[:4, 1:]
    assert B.shape == (4, 4)
    return B


def min_square_rank(n, q, sigma):
    modulus = n*n
    targets = {(-sigma*q*u*u) % modulus for u in units_mod(n)}
    max_sum = 4*modulus
    for k in range(1, 5):
        reps = sums_of_k_squares(k, max_sum)
        for N, vec in reps.items():
            if N > 0 and N % modulus in targets and math.gcd(N, n) == 1:
                return k, N, vec
    raise AssertionError((n, q, sigma))


def run():
    rows = []
    all_ok = True
    rank_counts = {str(k): 0 for k in range(1, 5)}
    for n in range(2, NMAX + 1):
        modulus = n*n
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
            q = n*a - 1
            for sigma in (1, -1):
                target = (-sigma*q) % modulus
                N = target if target else modulus
                # Four-square witness, padded to four coordinates.
                reps4 = sums_of_k_squares(4, N)
                while N not in reps4:
                    N += modulus
                    reps4 = sums_of_k_squares(4, N)
                v = reps4[N]
                assert len(v) == 4 and sum(x*x for x in v) == N
                assert math.gcd(N, n) == 1
                B = kernel_basis(v, n)
                assert abs(int(B.det())) == n
                for c in range(4):
                    assert sum(v[r]*int(B[r,c]) for r in range(4)) % n == 0
                G = -B.T*B
                det = abs(int(G.det()))
                S = smith_normal_form(G, domain=sp.ZZ)
                inv = sorted(abs(int(S[i,i])) for i in range(4))
                target_forms = {Fraction(sigma*q*u*u, modulus) % 1 for u in units_mod(n)}
                self_pairing = Fraction(-N, modulus) % 1
                min_k, min_N, min_v = min_square_rank(n, q, sigma)
                rank_counts[str(min_k)] += 1
                ok = det == modulus and inv == [1,1,1,modulus] and self_pairing in target_forms
                all_ok = all_ok and ok
                rows.append({
                    "n": n, "a": a, "q": q, "sigma": sigma,
                    "N": N, "v": v, "index": abs(int(B.det())),
                    "det_abs": det, "snf": inv,
                    "self_pairing": str(self_pairing),
                    "min_square_rank": min_k, "min_N": min_N,
                    "min_v": min_v, "ok": ok,
                })
    payload = {
        "NMAX": NMAX,
        "cases": len(rows),
        "all_ok": all_ok,
        "min_rank_counts": rank_counts,
        "rows": rows,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(payload, f, indent=1)
    print(len(rows), "cases; all_ok =", all_ok, "; min-rank counts =", rank_counts)
    assert all_ok


if __name__ == "__main__":
    run()
