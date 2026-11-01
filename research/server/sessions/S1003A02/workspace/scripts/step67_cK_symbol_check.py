#!/usr/bin/env python3
"""Step 67: principal-symbol injectivity behind the Garding estimate for the
second-order misalignment l_2 at a cscK metric (Theorem 67.K, part (ii)).

At a point, with orthonormal frame, Omega = e12+e34 (SD, the Kahler form),
h = unit ASD form (arbitrary direction), xi = unit covector.  The linearised
system on the constant-scalar harmonic-gauge slice has principal symbol

  gdot -> ( P_perp(gdot0)  [6 comps: <gdot0, phi_a o n_j>, n_j ⟂ h in Lambda^- ],
            <gdot0, Omega o h>  [amplitude, 1],
            tr gdot - gdot(xi,xi)  [scalar, 1],
            gdot(xi) - xi tr(gdot)/2  [harmonic gauge, 4] )

(orders 2,2,2,1; only injectivity matters).  We check rank 10 for random
(h, xi), that without the gauge rows the kernel is exactly 2-dimensional and
consists of sigma o h with sigma in Omega^perp (the free Ricci-rotation
modes), and that (sigma o h)^2 = (1/4)|sigma|^2|h|^2 Id (form norms).
Output: workspace/data/step67_cK_symbol_check.json
"""
import json, itertools
from pathlib import Path
import numpy as np

rng = np.random.default_rng(67)

def E(i, j):
    A = np.zeros((4, 4)); A[i, j] = 1; A[j, i] = -1; return A

SD = [E(0,1)+E(2,3), E(0,2)+E(3,1), E(0,3)+E(1,2)]
ASD = [E(0,1)-E(2,3), E(0,2)-E(3,1), E(0,3)-E(1,2)]
fnorm = lambda A: 0.5*np.sum(A*A)          # form norm, |e12+e34|^2 = 2
sym_basis = []
for i in range(4):
    for j in range(i, 4):
        S = np.zeros((4, 4)); S[i, j] = 1; S[j, i] = 1
        sym_basis.append(S if i != j else S/2)

out = {"trials": []}
# commutation / symmetry / square checks
checks = []
for a, b in itertools.product(range(3), range(3)):
    T = SD[a] @ ASD[b]
    checks.append(dict(sym=float(np.abs(T - T.T).max()),
                       comm=float(np.abs(SD[a]@ASD[b] - ASD[b]@SD[a]).max()),
                       tr=float(abs(np.trace(T)))))
out["phi_o_psi_symmetric_tracefree_commuting_maxerr"] = max(max(c.values()) for c in checks)

def unit(v): return v/np.linalg.norm(v)
Om = SD[0]
for trial in range(200):
    c = unit(rng.normal(size=3)); h = sum(ci*A for ci, A in zip(c, ASD))
    h = h/np.sqrt(fnorm(h))
    # orthonormal complement of h in Lambda^-
    M = np.linalg.qr(np.column_stack([c, rng.normal(size=3), rng.normal(size=3)]))[0]
    n = [sum(M[i, k]*ASD[i] for i in range(3)) for k in (1, 2)]
    n = [x/np.sqrt(fnorm(x)) for x in n]
    xi = unit(rng.normal(size=4))
    rows_main, rows_gauge = [], []
    for S in sym_basis:
        g0 = S - np.trace(S)/4*np.eye(4)
        r = [np.sum(g0*(SD[a] @ nj)) for a in range(3) for nj in n]
        r.append(np.sum(g0*(Om @ h)))
        r.append(np.trace(S) - xi @ S @ xi)
        rows_main.append(r)
        rows_gauge.append(list(S @ xi - 0.5*xi*np.trace(S)))
    Amain = np.array(rows_main).T            # 8 x 10
    Afull = np.vstack([Amain, np.array(rows_gauge).T])  # 12 x 10
    sv_full = np.linalg.svd(Afull, compute_uv=False)
    sv_main = np.linalg.svd(Amain, compute_uv=False)
    ker = np.linalg.svd(Amain)[2][-2:]      # kernel basis (10-vectors)
    # check kernel = sigma o h, sigma in span(SD[1],SD[2])
    span = []
    for sig in (SD[1], SD[2]):
        T = sig @ h
        span.append([np.sum(T*S)/np.sum(S*S) for S in sym_basis])
    span = np.array(span)
    # compare subspaces via projection
    Q1 = np.linalg.qr(ker.T)[0]; Q2 = np.linalg.qr(np.array([[np.sum(sum(v[k]*sym_basis[k] for k in range(10))*S)
                                                              for S in sym_basis] for v in span]).T)[0]
    # rebuild kernel matrices directly and test they lie in span{sigma o h}
    def mat(v): return sum(v[k]*sym_basis[k] for k in range(10))
    targets = [SD[1] @ h, SD[2] @ h]
    G = np.array([[np.sum(a*b) for b in targets] for a in targets])
    res = 0.0
    for v in ker:
        Kmat = mat(v); Kmat = Kmat - np.trace(Kmat)/4*np.eye(4)   # tracefree part (trace is slaved to sigma by the s'-row)
        coef = np.linalg.solve(G, [np.sum(Kmat*t) for t in targets])
        res = max(res, np.abs(Kmat - coef[0]*targets[0] - coef[1]*targets[1]).max()/np.abs(Kmat).max())
    sig = rng.normal()*SD[1] + rng.normal()*SD[2]
    T = sig @ h
    sq = T @ T
    sq_err = np.abs(sq - 0.25*fnorm(sig)*fnorm(h)*np.eye(4)*4).max()  # see note below
    out["trials"].append(dict(min_sv_full=float(sv_full[-1]), rank_main=int(np.sum(sv_main > 1e-10)),
                              ker_in_sigma_o_h_relres=float(res),
                              square_ratio=float(sq[0, 0]/(fnorm(sig)*fnorm(h))),
                              square_offdiag=float(np.abs(sq - sq[0, 0]*np.eye(4)).max())))
tr = out["trials"]
out["summary"] = dict(
    min_over_trials_min_singular_value_full=min(t["min_sv_full"] for t in tr),
    rank_without_gauge=sorted(set(t["rank_main"] for t in tr)),
    max_kernel_residual=max(t["ker_in_sigma_o_h_relres"] for t in tr),
    square_ratio_range=[min(t["square_ratio"] for t in tr), max(t["square_ratio"] for t in tr)],
    max_square_offdiag=max(t["square_offdiag"] for t in tr))
p = Path(__file__).resolve().parents[1]/"data"/"step67_cK_symbol_check.json"
p.write_text(json.dumps({k: v for k, v in out.items() if k != "trials"}, indent=1))
print(json.dumps(out["summary"], indent=1), out["phi_o_psi_symmetric_tracefree_commuting_maxerr"])
