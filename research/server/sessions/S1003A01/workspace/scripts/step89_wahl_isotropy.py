"""Step 89b: isotropy constraints at a Wahl cone point 1/n^2(1,n-1) (T-singularity).

Generator zeta = exp(2 pi i/n^2) acts on C^2 with weights (1, n-1) (holomorphic coordinates
transform with these weights).  Canonical spin^c structure of the complex orbifold:
S^+ = Lambda^{0,0} + Lambda^{0,2}, S^- = Lambda^{0,1}; Lambda^+ = R omega_0 + Re Lambda^{2,0}.
We list, for each n, the dimension of the invariant subspace of
  S^+ (value of Phi), T*_C (x) S^+ (first jet of Phi), Lambda^+_C (value of an SD 2-form),
  T*_C (x) Lambda^{2,0}  (the part of nabla omega that can be nonzero for an AK form),
  T*_C (x) E,  E = Lambda^{0,1} (x) Lambda^{0,2}  (first jet of the AK torsion section).
Weights are integers mod n^2 (character exponents).  A component can be nonzero at the
cone point only if its total weight is 0 mod n^2.
Twisted spin^c structures S^+ (x) chi^j are included for chi = zeta^{n} (the Z_n cosets).
Output: workspace/data/step89/wahl_isotropy.json
"""
import json, os

def inv_dim(weights, N):
    return sum(1 for w in weights if w % N == 0)

res = {}
for n in range(2, 16):
    N = n*n
    w1, w2 = 1, n-1
    Tstar = [w1, w2, -w1, -w2]                 # complexified cotangent (dz, dzbar)
    L02 = -(w1+w2)                             # Lambda^{0,2}
    L01 = [-w1, -w2]
    L20 = w1+w2
    row = {}
    for j in range(n):
        chi = n*j
        Splus = [0+chi, L02+chi]
        row_j = dict(
            Phi_value=inv_dim(Splus, N),
            Phi_first_jet=inv_dim([a+b for a in Tstar for b in Splus], N))
        row[f'twist_{j}'] = row_j
    E = [a+L02 for a in L01]
    row['SD_form_value_(omega0,Re L20)'] = [1, inv_dim([L20, -L20], N)]
    row['nabla_omega_Lambda20_part'] = inv_dim([a+b for a in Tstar for b in [L20, -L20]], N)
    row['torsion_value_E'] = inv_dim(E, N)
    row['torsion_first_jet_TstarE'] = inv_dim([a+b for a in Tstar for b in E], N)
    res[n] = row
print(json.dumps(res, indent=1))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step89'); os.makedirs(od, exist_ok=True)
json.dump(res, open(os.path.join(od, 'wahl_isotropy.json'), 'w'), indent=1)
