#!/usr/bin/env python3
"""Step 96: integral intersection lattice of Suvaina class-T fillers and their effect on the full-absorption screen.

Object.  N = N_{d,n,m} = M_{d,n}/Z_n, M_{d,n} = {xy = prod_{i<=d} prod_{j<n} (z - c_i rho^j)} the A_{dn-1} Milnor fibre,
rho = exp(2 pi i/n), Z_n acting by rho.(x,y,z) = (rho x, rho^{-1} y, rho^m z), (m,n)=1  (Suvaina 2012, Prop. 2.3 / Thm B).
Scope (Step-98 repair).  Suvaina's class also contains quotients of minimal resolutions of SINGULAR invariant fibres
(repeated c_i^n); these are equivariantly diffeomorphic to the smooth-fibre models above (distinct Gibbons-Hawking
centres in R^3, equivariant isotopy), so the same lattice model applies.  This script is a FINITE consistency check of
the permutation-lattice arithmetic for 1<=d<=6, 2<=n<=7; its 'index' field uses the topological determinant
prediction and is not an independent computation of transfer.  General coverage is the proof in
notes/step96_suvaina_lattice_and_kahler_filler_theorem.md, not this finite range.
Model used.  H_2(M) = sum-zero sublattice Lambda of Z^{dn} (basis e_{(i,j)} = roots c_i rho^j), form -sum x^2;
the deck group permutes roots (i,j) -> (i,j+m) with no signs (segment spheres map to segment spheres, fibre circles
are rotated, orientation kept).
Checks (exact):
 (1) invariant lattice I = Lambda^G, scaled form (1/n) Q, equals A_{d-1}(-1): det = d (up to sign), even, roots.
 (2) Cartan-Leray: coinvariants Lambda_G (rank d-1) and its torsion; H_2(N) = coker(d^3 : H_3(Z_n)=Z_n -> Lambda_G),
     so torsion(Lambda_G) must be a quotient of Z_n; the boundary argument (pi_1(dN) ->> pi_1 N) gives H_2(N) free.
 (3) determinant identity |H_1(dN)| = |det Q_N| |H_1 N|^2 / |Tors H_2 N|^2 with |H_1(dN)| = d n^2, H_1 N = Z_n.
 (4) full-absorption costs with Suvaina substitutes for the low D-blocks (D_2 = A_1+A_1, D_3 = A_3): cost - rank/6 > 0.
Output: workspace/data/step96/suvaina_lattice.json
"""
import json, os, itertools
from fractions import Fraction as F
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

out = {"lattice": [], "coinvariants": [], "costs": {}}

def perm_matrix(d, n, m):
    N = d * n
    P = sp.zeros(N, N)
    for i in range(d):
        for j in range(n):
            P[i * n + (j + m) % n, i * n + j] = 1
    return P

for d in range(1, 7):
    for n in range(2, 8):
        for m in range(1, n):
            if sp.gcd(m, n) != 1:
                continue
            N = d * n
            # basis of Lambda: f_a = e_a - e_{N-1}, a < N-1
            B = sp.zeros(N, N - 1)
            for a in range(N - 1):
                B[a, a] = 1; B[N - 1, a] = -1
            P = perm_matrix(d, n, m)
            # (1) invariant lattice: orbit sums O_i, sum-zero combos; basis O_i - O_{d-1}
            if d >= 2:
                O = [sp.Matrix([1 if (a // n) == i else 0 for a in range(N)]) for i in range(d)]
                basis = [O[i] - O[d - 1] for i in range(d - 1)]
                G = sp.Matrix(d - 1, d - 1, lambda r, c: -(basis[r].T * basis[c])[0] / n)
                detG = G.det()
                even = all(G[r, r] % 2 == 0 for r in range(d - 1))
                # check invariance and that these span Lambda^G (primitive saturation): Lambda^G = ker(P - 1) on Lambda
                ok_inv = all(((P * b) - b).is_zero_matrix for b in basis)
                # saturation: Smith form of basis matrix inside Z^N has all invariant factors 1
                Bm = sp.Matrix.hstack(*basis)
                snf = smith_normal_form(Bm, domain=sp.ZZ)
                sat = all(abs(snf[r, r]) == 1 for r in range(d - 1))
            else:
                detG, even, ok_inv, sat = 1, True, True, True
            # (2) coinvariants Lambda / (P-1)Lambda, Lambda coordinates via B
            # action on Lambda in basis f: solve B X = P B
            X = (B.T * B).inv() * B.T * P * B
            assert (B * X - P * B).is_zero_matrix
            Rel = X - sp.eye(N - 1)
            snf2 = smith_normal_form(Rel, domain=sp.ZZ)
            diag = [abs(snf2[r, r]) for r in range(min(snf2.shape))]
            rank_rel = sum(1 for x in diag if x != 0)
            tors = [int(x) for x in diag if x not in (0, 1)]
            coinv_rank = (N - 1) - rank_rel
            tors_order = 1
            for t in tors:
                tors_order *= t
            # (3) determinant identity, assuming H_2(N) free (boundary argument) and H_1 N = Z_n
            det_pred = F(d * n * n, n * n)
            rec = {"d": d, "n": n, "m": m, "b2": d - 1, "det_scaled_invariant": int(abs(detG)),
                   "even": bool(even), "invariant": bool(ok_inv), "saturated": bool(sat),
                   "det_from_boundary_identity": str(det_pred),
                   "index_of_transfer_image": 1 if abs(detG) == det_pred else None,
                   "coinvariant_rank": int(coinv_rank), "coinvariant_torsion": tors,
                   "coinv_torsion_divides_n": n % tors_order == 0}
            assert rec["coinvariant_rank"] == d - 1
            assert abs(detG) == det_pred, rec
            assert rec["coinv_torsion_divides_n"], rec
            out["lattice"].append(rec)

# (4) costs.  complex-oriented Ricci-flat Kahler filler cost = chi - 1/|Gamma| - b_2 = 1 - 1/|Gamma|.
def cost_kron_A(r):
    return 1 - F(1, r + 1)
def cost_suv(d, n):
    return 1 - F(1, d * n * n)
best = {}
# D_2 = A_1 + A_1 : components each EH (cost 1/2) or Suvaina d=2 (min over n>=2 at n=2: 1-1/8)
eh = cost_kron_A(1); s2 = cost_suv(2, 2)
best["D2"] = {"EH+EH": str(2 * eh), "EH+Suv(d=2,n=2)": str(eh + s2), "Suv+Suv": str(2 * s2), "rank/6": str(F(2, 6))}
# D_3 = A_3 : Kronheimer A_3 (|Gamma|=4) or Suvaina d=4 (min at n=2: 1 - 1/16)
best["D3"] = {"Kron A3": str(cost_kron_A(3)), "Suv(d=4,n=2)": str(cost_suv(4, 2)), "rank/6": str(F(3, 6))}
for k, v in best.items():
    r = F(int(k[1]), 1)
    vals = [F(x) for kk, x in v.items() if kk != "rank/6"]
    assert min(vals) > r / 6
out["costs"] = best
out["conclusion"] = ("H_2(N_{d,n,m}) = A_{d-1}(-1), torsion-free, transfer image = full invariant lattice; "
                     "Suvaina substitutes only raise the cost of D_2/D_3 blocks; D_{>=4} blocks are irreducible "
                     "D-type and cannot be Suvaina (A-type) lattices")
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step96')
os.makedirs(p, exist_ok=True)
with open(os.path.join(p, 'suvaina_lattice.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print(len(out["lattice"]), "cases checked")
print(json.dumps(out["costs"], indent=1))
print(sorted({tuple(r["coinvariant_torsion"]) for r in out["lattice"]}))
print([ (r["d"], r["n"], r["coinvariant_torsion"]) for r in out["lattice"] if r["m"] == 1][:20])
