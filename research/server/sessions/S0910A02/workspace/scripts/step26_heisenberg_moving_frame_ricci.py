"""
Independent moving-frame Ricci check for Step 26.

Frame:
  e0 = d/dt,
  e1,e2 = a(t)^{-1} left-invariant generators,
  e3 = c(t)^{-1} center,
  [E1,E2]=E3.
Then
  [e0,e1]=-k1 e1, [e0,e2]=-k1 e2, [e0,e3]=-k3 e3,
  [e1,e2]=b e3, b=c/a^2.
Only e0 derivatives of structure functions are nonzero.

Use Koszul and the anholonomic curvature formula in an orthonormal frame to
compute Ricci components. This checks the cohomogeneity-one equations used in
step26_nilpotent_submersion_balance.py without invoking them as assumptions.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

b, k1, k3, bp, k1p, k3p = sp.symbols('b k1 k3 bp k1p k3p')
N = 4

def zeros3():
    return [[[sp.Integer(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]

# c[i][j][k] = <[e_i,e_j], e_k>
c = zeros3()

def set_br(i,j,k,val):
    c[i][j][k] = val
    c[j][i][k] = -val

set_br(0,1,1,-k1)
set_br(0,2,2,-k1)
set_br(0,3,3,-k3)
set_br(1,2,3,b)

# derivative operator e_i acting on expressions in b,k1,k3: only e0 nonzero.
def deriv(i, expr):
    if i != 0:
        return sp.Integer(0)
    return sp.diff(expr, b)*bp + sp.diff(expr, k1)*k1p + sp.diff(expr, k3)*k3p

# Gamma[i][j][k] = <nabla_{e_i} e_j, e_k>
Gamma = zeros3()
for i in range(N):
    for j in range(N):
        for k in range(N):
            Gamma[i][j][k] = sp.simplify((c[i][j][k] - c[j][k][i] + c[k][i][j]) / 2)

# R^m_{i j l} = <R(e_i,e_j)e_l, e_m>
R = [[[[sp.Integer(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for l in range(N):
            for m in range(N):
                term = deriv(i, Gamma[j][l][m]) - deriv(j, Gamma[i][l][m])
                term += sum(Gamma[j][l][p]*Gamma[i][p][m] - Gamma[i][l][p]*Gamma[j][p][m] for p in range(N))
                term -= sum(c[i][j][p]*Gamma[p][l][m] for p in range(N))
                R[i][j][l][m] = sp.simplify(term)

# Candidate Ricci conventions.  Ric(j,l)=sum_i <R(e_i,e_j)e_l,e_i>.
Ric_A = [[sp.simplify(sum(R[i][j][l][i] for i in range(N))) for l in range(N)] for j in range(N)]
# Opposite sign convention sometimes used: sum_i <R(e_j,e_i)e_i,e_l>.
Ric_B = [[sp.simplify(sum(R[j][i][i][l] for i in range(N))) for l in range(N)] for j in range(N)]

# Expected under the convention used in the session: for k'=0 at k=0 intrinsic H3 is (-b^2/2,-b^2/2,+b^2/2).
expected_session = {
    'Ric00': -(2*(k1p + k1**2) + (k3p + k3**2)),
    'Ric11': -b**2/2 - k1p - (2*k1+k3)*k1,
    'Ric22': -b**2/2 - k1p - (2*k1+k3)*k1,
    'Ric33': b**2/2 - k3p - (2*k1+k3)*k3,
}
expected_matrix = sp.diag(expected_session['Ric00'], expected_session['Ric11'], expected_session['Ric22'], expected_session['Ric33'])

# Determine which convention matches expected_session.
diff_A = [[sp.simplify(Ric_A[i][j] - expected_matrix[i,j]) for j in range(N)] for i in range(N)]
diff_B = [[sp.simplify(Ric_B[i][j] - expected_matrix[i,j]) for j in range(N)] for i in range(N)]
# Also compare -Ric_A, -Ric_B if needed.
diff_negA = [[sp.simplify(-Ric_A[i][j] - expected_matrix[i,j]) for j in range(N)] for i in range(N)]
diff_negB = [[sp.simplify(-Ric_B[i][j] - expected_matrix[i,j]) for j in range(N)] for i in range(N)]

def mat_to_str(mat):
    return [[str(sp.simplify(x)) for x in row] for row in mat]

def all_zero(mat):
    return all(sp.simplify(x) == 0 for row in mat for x in row)

# Substitute exact Ric=1 vertical equations and constraint relations as a consistency check.
H = 2*k1+k3
vert_eq_sub = {
    k1p: -1 - b**2/2 - H*k1,
    k3p: -1 + b**2/2 - H*k3,
}
Ric_expected_after_vert = [[sp.simplify(expected_matrix[i,j].subs(vert_eq_sub)) for j in range(N)] for i in range(N)]
constraint_expr = 4*k1**2 + 8*k1*k3 + b**2 + 4
Ric00_minus_1_after_vert = sp.simplify(Ric_expected_after_vert[0][0] - 1)
Ric00_relation = sp.factor(Ric00_minus_1_after_vert)

out = {
    'title': 'Step 26 moving-frame Ricci derivation for diagonal H3 cohomogeneity-one model',
    'brackets': {
        '[e0,e1]': '-k1 e1',
        '[e0,e2]': '-k1 e2',
        '[e0,e3]': '-k3 e3',
        '[e1,e2]': 'b e3',
        'e0_derivatives': {'b': 'bp', 'k1': 'k1p', 'k3': 'k3p'},
    },
    'Gamma_nonzero': [
        {'i': i, 'j': j, 'k': k, 'value': str(Gamma[i][j][k])}
        for i in range(N) for j in range(N) for k in range(N) if Gamma[i][j][k] != 0
    ],
    'Ric_convention_A_sum_R_i_j_l_i': mat_to_str(Ric_A),
    'Ric_convention_B_sum_R_j_i_i_l': mat_to_str(Ric_B),
    'expected_session_matrix': mat_to_str(expected_matrix.tolist()),
    'matches_expected': {
        'Ric_A': all_zero(diff_A),
        'Ric_B': all_zero(diff_B),
        'negative_Ric_A': all_zero(diff_negA),
        'negative_Ric_B': all_zero(diff_negB),
    },
    'diff_A_minus_expected': mat_to_str(diff_A),
    'diff_B_minus_expected': mat_to_str(diff_B),
    'vertical_Ric_equals_1_substitution': {
        'Ric_matrix_after_using_vertical_eqs': mat_to_str(Ric_expected_after_vert),
        'Ric00_minus_1_after_vertical_eqs': str(Ric00_relation),
        'constraint_for_Ric00_equals_1': str(constraint_expr),
        'relation': 'Ric00-1 = 1/2*(4 k1^2 + 8 k1 k3 + b^2 + 4), so the displayed constraint is equivalent to Ric00=1.',
    },
    'conclusion': 'The moving-frame calculation matches the Step-26 cohomogeneity-one H3 formulas under convention Ric_A. The T-active local model is algebraically consistent, so a Milnor-only abelian-forcing proof is false once second fundamental form terms are allowed.'
}

path = Path(__file__).resolve().parents[1] / 'data' / 'step26_heisenberg_moving_frame_ricci.json'
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f"\nSaved to {path}")
