"""
Step 48: curvature block and topology arithmetic for product-surface A1 routes.

This script checks only finite-dimensional algebra used in the Explore note:
1. A product of two oriented constant-curvature surfaces with the same curvature Lambda
   has both chiral curvature blocks diag(Lambda,0,0) in a standard self/anti-self-dual basis.
2. For p_g=q=0 product-quotient surfaces with only rational double points and holomorphic
   Euler characteristic 1, Noether and c1^2=2e+3tau give b_+=1 and b_-=9-K^2 for K^2=2,4,6.
It does not prove gluing estimates, Seiberg-Witten information, or Einstein nonexistence.
"""
from fractions import Fraction


def curvature_operator_product(lam):
    # basis of 2-forms: 12,13,14,23,24,34. Product surface curvature gives eigenvalue lam on 12 and 34 only.
    diag = {
        "12": lam,
        "13": 0,
        "14": 0,
        "23": 0,
        "24": 0,
        "34": lam,
    }
    return diag


def inner(form1, form2):
    return sum(form1.get(k, 0) * form2.get(k, 0) for k in set(form1) | set(form2))


def apply_R(diag, form):
    return {k: diag[k] * v for k, v in form.items()}


def mat_on_basis(diag, basis):
    return [[inner(bi, apply_R(diag, bj)) for bj in basis] for bi in basis]

# Orthonormal normalization is irrelevant for zero/off-diagonal pattern; use 1/sqrt(2)-free paired forms.
self_basis = [
    {"12": Fraction(1), "34": Fraction(1)},
    {"13": Fraction(1), "24": Fraction(-1)},
    {"14": Fraction(1), "23": Fraction(1)},
]
anti_basis = [
    {"12": Fraction(1), "34": Fraction(-1)},
    {"13": Fraction(1), "24": Fraction(1)},
    {"14": Fraction(1), "23": Fraction(-1)},
]

for lam in [Fraction(1), Fraction(-1), Fraction(3, 2)]:
    diag = curvature_operator_product(lam)
    plus_raw = mat_on_basis(diag, self_basis)
    minus_raw = mat_on_basis(diag, anti_basis)
    # Each paired basis vector has squared norm 2, so divide by 2 for orthonormal matrix entries.
    plus = [[entry / 2 for entry in row] for row in plus_raw]
    minus = [[entry / 2 for entry in row] for row in minus_raw]
    expected = [[lam, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert plus == expected, (lam, plus)
    assert minus == expected, (lam, minus)

# Product-quotient p_g=q=0 rational-double-point families from Bauer-Catanese-Grunewald-Pignatelli.
# holomorphic chi_h=1, c1^2=K2, e=12 chi_h-K2, tau=(K2-2e)/3, b2=e-2, b+ = (b2+tau)/2.
rows = []
for K2 in [2, 4, 6]:
    e = 12 - K2
    tau = (K2 - 2 * e) // 3
    assert 3 * tau == K2 - 2 * e
    b2 = e - 2
    bplus = (b2 + tau) // 2
    bminus = (b2 - tau) // 2
    assert bplus == 1
    assert bminus == 9 - K2
    nodes = 8 - K2
    rows.append((K2, nodes, e, tau, bplus, bminus))

print("Product surface chiral curvature blocks: R_+=R_-=diag(Lambda,0,0) for Lambda=+1,-1,3/2.")
print("p_g=q=0 A1 product-quotient arithmetic (K^2, A1 nodes, e, tau, b+, b-):")
for row in rows:
    print("  ", row)
print("finite-dimensional product-surface checks passed")
