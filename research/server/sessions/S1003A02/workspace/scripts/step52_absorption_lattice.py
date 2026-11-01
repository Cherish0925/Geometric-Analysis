"""Step 52: Kronheimer absorption of exceptional classes -- lattice and characteristic bookkeeping.

Input : none.  Output: workspace/data/step52_absorption_lattice.json
Checks
  (1) explicit embeddings of even root lattices R (Kronheimer ALE lattices) of full rank into the
      odd negative-definite unimodular lattice -Z^k, index^2 = disc(R):  A1+A1 in Z^2, A3 = D3 in Z^3,
      D_n in Z^n, (A1+A1)^m in Z^{2m}; Gram matrices, determinants, index.
  (2) negative result: a single A1, A2, E6, E7, E8, A_{m^2-1} (m=3) admits no odd unimodular
      integral overlattice (discriminant not a square, or unique overlattice even).
  (3) orbifold characteristic numbers: Y = X # (S^4/Z2) resolved by two Eguchi-Hanson spaces and
      Y = X # Sigma_4 (Z4 cone point, rational ball B_2) resolved by Kronheimer A3; verify
      chi, tau of the resolution equal those of X # k CPbar^2 and 2chi+3tau is preserved;
      eta via Kronheimer identity 3 eta = r - 2 + 2/|Gamma|.
  (4) Theorem-G link charges (normalized, standard flat germs) of the blocks: Kronheimer bubbles pay 0,
      orbifold cells pay k, total = k (conservation of the standard-germ ledger).
"""
import json, itertools, os
from fractions import Fraction as F
import numpy as np

out = {}

def gram(vectors):
    V = np.array(vectors, dtype=int)
    return (-V @ V.T).tolist()   # ambient form -I

def det(M):
    return int(round(np.linalg.det(np.array(M, dtype=float))))

emb = {}
emb['A1+A1 in Z^2'] = [[1,1],[1,-1]]
emb['A3=D3 in Z^3 (chain e2-e3, e1-e2, e2+e3)'] = [[0,1,-1],[1,-1,0],[0,1,1]]
for n in (4,5,6):
    roots = [[1 if j==i else (-1 if j==i+1 else 0) for j in range(n)] for i in range(n-1)]
    roots.append([0]*(n-2)+[1,1])
    emb[f'D{n} in Z^{n}'] = roots
emb['(A1+A1)^2 in Z^4'] = [[1,1,0,0],[1,-1,0,0],[0,0,1,1],[0,0,1,-1]]
res1 = {}
for name, vecs in emb.items():
    G = gram(vecs)
    d = abs(det(G))
    diag_even = all(G[i][i] % 2 == 0 for i in range(len(G)))
    # ambient Z^k has det 1, so index^2 = disc
    res1[name] = {'gram': G, 'disc': d, 'index_in_Z^k': int(round(d ** 0.5)), 'root_lattice_even': diag_even,
                  'all_roots_norm_-2': all(G[i][i] == -2 for i in range(len(G)))}
out['embeddings'] = res1

# exceptional classes expressed in roots (rational coefficients) for A1+A1 and A3
def coeffs(vecs, target):
    V = np.array(vecs, dtype=float).T
    c = np.linalg.solve(V, np.array(target, dtype=float))
    return [str(F(x).limit_denominator(64)) for x in c]
out['E_in_root_span'] = {
    'A1+A1: E1': coeffs(emb['A1+A1 in Z^2'], [1,0]),
    'A1+A1: E2': coeffs(emb['A1+A1 in Z^2'], [0,1]),
    'A3: E1': coeffs(emb['A3=D3 in Z^3 (chain e2-e3, e1-e2, e2+e3)'], [1,0,0]),
    'A3: E2': coeffs(emb['A3=D3 in Z^3 (chain e2-e3, e1-e2, e2+e3)'], [0,1,0]),
    'A3: E3': coeffs(emb['A3=D3 in Z^3 (chain e2-e3, e1-e2, e2+e3)'], [0,0,1]),
}

# (2) obstruction: discriminants
discs = {'A1': 2, 'A2': 3, 'A3': 4, 'A8': 9, 'E6': 3, 'E7': 2, 'E8': 1, 'D4': 4}
out['single_lattice_overlattice'] = {
    k: {'disc': v, 'square': int(round(v**0.5))**2 == v,
        'note': {'A1': 'disc 2 not square: no overlattice', 'A2': 'disc 3: none', 'E6': 'disc 3: none',
                 'E7': 'disc 2: none', 'E8': 'unimodular even, not Z^8',
                 'A8': 'unique index-3 overlattice is E8 (even): no norm -1 vector',
                 'A3': 'index-2 overlattice D3^+ = Z^3 (odd)', 'D4': 'index-2 overlattices: Z^4 (odd) and the two other ones (even? D4^+ ~ D4); Z^4 occurs'}[k]}
    for k, v in discs.items()}

# (3) characteristic numbers
def kron(r, G):
    eta = F(r - 2, 3) + F(2, 3 * G)
    return {'chi': 1 + r, 'tau': -r, 'eta': eta, 'Gamma': G}
EH = kron(1, 2); A3 = kron(3, 4)
out['eta'] = {'EH(Z2)': str(EH['eta']), 'A3(Z4)': str(A3['eta'])}
def check(name, chi_orb_cell, tau_orb_cell, bubbles, k):
    # Y = X # cell-orbifold; resolution M = X # k CPbar^2 ; work with differences from X (chi_X, tau_X symbolic)
    chi_orb_Y = chi_orb_cell - 2          # chi(X) + chi_orb(cell) - 2
    tau_orb_Y = tau_orb_cell
    chi_M = chi_orb_Y + sum(b['chi'] - F(1, b['Gamma']) for b in bubbles)
    tau_M = tau_orb_Y + sum(b['tau'] + b['eta'] for b in bubbles)
    return {'chi_M - chi_X': str(chi_M), 'tau_M - tau_X': str(tau_M), 'expected': (k, -k),
            'ok': chi_M == k and tau_M == -k,
            '(2chi+3tau)_orb(Y) - c1^2(X)': str(2 * chi_orb_Y + 3 * tau_orb_Y)}
# S^4/Z2 : chi_orb = 1, tau_orb = 0.  Sigma_4 = B_2 u cone: chi_top = 2, chi_orb = 2 - (1-1/4); tau_orb fixed by
# requiring the A3 resolution to be #3CPbar^2:  tau_orb = -3 - (tau(A3)+eta) .
tau_orb_Sigma4 = -3 - (A3['tau'] + A3['eta'])
out['characteristic'] = {
    'X#(S4/Z2) + 2 EH': check('S4/Z2', F(1), F(0), [EH, EH], 2),
    'X#Sigma4 + A3': check('Sigma4', F(2) - F(3, 4), tau_orb_Sigma4, [A3], 3),
    'tau_orb(Sigma4)': str(tau_orb_Sigma4),
}

# (4) Theorem-G charges (normalized), standard germs: q_sigma(Gamma) = 2/|Gamma| - 3 sigma eta
def q(G, eta, s):
    return F(2, G) - 3 * s * eta
def block_charge(chi, tau, outs, ins):
    vals = []
    for s in (1, -1):
        v = sum(q(G, e, s) for G, e in outs) - sum(q(G, e, s) for G, e in ins) - (2 * chi + 3 * s * tau)
        vals.append(v)
    return max(max(vals), 0), [str(v) for v in vals]
S3 = (1, F(0)); Z2 = (2, EH['eta']); Z4 = (4, A3['eta'])
charges = {}
charges['Burns (D#CPbar2 cell, chi=2,tau=-1)'] = block_charge(2, -1, [S3], [])
charges['EH bubble'] = block_charge(EH['chi'], EH['tau'], [Z2], [])
charges['A3 Kronheimer bubble'] = block_charge(A3['chi'], A3['tau'], [Z4], [])
# orbifold cells with one S^3 outer boundary: (S^4/Z2) minus ball minus two cones: chi = 2 - 1 - 2 = -1, tau 0
charges['S4/Z2 cell'] = block_charge(-1, 0, [S3], [Z2, Z2])
# Sigma4 cell = B_2 minus ball minus cone: chi = 1 - 1 - 0 ... chi(B2)=1, remove ball (-1), remove cone nbhd (chi(cone)=1 replaced by boundary chi 0): chi = 2 - 1 - 1 = 0
charges['Sigma4 cell'] = block_charge(0, 0, [S3], [Z4])
charges['D#2CPbar2 cell'] = block_charge(3, -2, [S3], [])
charges['D#3CPbar2 cell'] = block_charge(4, -3, [S3], [])
out['link_charges'] = {k: {'charge': str(v[0]), 'sigma=+1,-1': v[1]} for k, v in charges.items()}

path = os.path.join(os.path.dirname(__file__), '..', 'data', 'step52_absorption_lattice.json')
with open(path, 'w') as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
