"""Exact finite checks for the standalone integral-rigidity manuscript.

These checks detect algebraic transcription errors. They do not establish
monopole existence, chamber compatibility, or the analytic inequalities.
Run with Python and SymPy; the script has no file or network side effects.
"""

import sympy as sp

Q = sp.Rational
checks = 0


def zero(expression):
    global checks
    assert sp.expand(expression) == 0
    checks += 1


# The two completed squares and the exact distance to the forbidden orbit.
s, alpha, w, z = sp.symbols("s alpha w z", real=True)
q = -s + 3 * alpha
t = s + 24 * alpha
energy = s**2 / 24 + 3 * alpha**2
zero(27 * energy - q**2 - t**2 / 8)
bminus2 = sp.symbols("bminus2")
G = (2 * s / 3 - 2 * alpha) ** 2 - bminus2
zero(t**2 + 18 * G - 216 * energy + 18 * bminus2)
zero(
    Q(3, 2) * alpha**2 + Q(1, 24) + (-alpha + z) / 2
    - (Q(3, 2) * (alpha - Q(1, 6)) ** 2 + z / 2)
)
zero(
    ((2 * s / 3 - 2 * alpha) ** 2
     - (2 * s / 3 - 2 * alpha + 2 * z) ** 2)
    - z * (-8 * s / 3 + 8 * alpha - 4 * z)
)

# Retained Hölder moment algebra.
theta, EQ, Cstar = sp.symbols("theta EQ Cstar", nonzero=True)
Hstar = EQ * theta**2 - Cstar
Pstar = Cstar - EQ * theta**3
zero(EQ - Cstar - Hstar - (1 + theta) * (Pstar + Hstar) / theta**2)
assert Q(1, 2) * Q(8, 27) == Q(4, 27)
assert 36 * Q(9, 16) + 9 == Q(117, 4)
assert Q(245, 2) < 1215
assert 972 * Q(5, 4) == 1215
checks += 4

# A pointwise four-dimensional jet, with the manuscript's full tensor norm.
omega = []
for pairs in (
    ((0, 1), (2, 3)),
    ((0, 2), (3, 1)),
    ((0, 3), (1, 2)),
):
    form = sp.zeros(4)
    for i, j in pairs:
        form[i, j], form[j, i] = 1, -1
    omega.append(form)

rho = sp.symbols("rho", positive=True)
cjet = sp.symbols("c0:4", real=True)
ajet = sp.symbols("a0:4", real=True)
bjet = sp.symbols("b0:4", real=True)
pjet = sp.Matrix([rho, 0, 0])
vjet = [sp.Matrix([cjet[i], ajet[i], bjet[i]]) for i in range(4)]
dmodel = [
    pjet.dot(v) * sp.eye(3) / 12 - (pjet * v.T + v * pjet.T) / 8
    for v in vjet
]
grad_model2 = sum(sp.trace(dm.T * dm) for dm in dmodel)
div_model2 = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            entry = sum(
                dmodel[i][a, b] * omega[a][i, j] * omega[b][k, l] / 2
                for i in range(4) for a in range(3) for b in range(3)
            )
            div_model2 += entry**2

grad_form = [
    sum((vjet[i][a] * omega[a] for a in range(3)), sp.zeros(4)) / sp.sqrt(2)
    for i in range(4)
]
exterior = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for i in range(4):
    for j in range(4):
        for k in range(4):
            exterior[i, j, k] = (
                grad_form[i][j, k] + grad_form[j][k, i] + grad_form[k][i, j]
            )
exterior2 = sum(
    exterior[i, j, k] ** 2
    for i in range(4) for j in range(4) for k in range(4)
) / 6
star_exterior = [
    sum(
        sp.LeviCivita(i, j, k, l) * exterior[i, j, k]
        for i in range(4) for j in range(4) for k in range(4)
    ) / 6
    for l in range(4)
]
star_displayed = [
    (-ajet[2] - bjet[3] - cjet[1]) / sp.sqrt(2),
    (ajet[3] - bjet[2] + cjet[0]) / sp.sqrt(2),
    (ajet[0] + bjet[1] - cjet[3]) / sp.sqrt(2),
    (-ajet[1] + bjet[0] + cjet[2]) / sp.sqrt(2),
]
for actual, displayed in zip(star_exterior, star_displayed):
    zero(actual - displayed)
contract_amp = rho * sp.Matrix([-cjet[1], cjet[0], -cjet[3], cjet[2]]) / sp.sqrt(2)
cross_amp = sum(contract_amp[j] * star_exterior[j] for j in range(4))
grad_form2 = sum(v.dot(v) for v in vjet)
amp2 = sum(c**2 for c in cjet)
zero(grad_model2 - rho**2 * grad_form2 / 32 - rho**2 * amp2 / 96)
zero(
    grad_model2 - div_model2
    - rho**2 * (grad_form2 - 2 * exterior2) / 64
    - rho**2 * amp2 / 32 + rho * cross_amp / 16
)

# Elimination of the integrated weighted Hodge expression, equation (6.8).
U, H, D, Aamp, Ccross = sp.symbols("U H D Aamp Ccross")
Jidentity = U / 64 + D / 32 - Aamp / 48 + Ccross / 16
U_from_hodge = -H + 2 * D + 4 * Ccross - 2 * Aamp
zero(
    Jidentity.subs(U, U_from_hodge)
    - (-H / 64 + D / 16 - 5 * Aamp / 96 + Ccross / 8)
)
assert (-s * rho**4 / 192 - rho**6 / 384).subs({s: -4, rho: sp.sqrt(2)}) == Q(1, 16)
checks += 1

# All-sign energy identity and nonpositive-topology supplement.
P, S2, Ls, W2, T, pi2 = sp.symbols("P S2 Ls W2 T pi2")
R2 = P + S2 / 4
zero((4 * P + Ls) - (R2 + 12 * W2 - 24 * pi2 * T + Ls)
     .subs(T, (S2 / 24 + 2 * W2 - P / 2) / (4 * pi2)))
assert Q(1, 2) * Q(1, 4) * (Q(2, 3) + Q(1, 4)) == Q(11, 96) < Q(1, 4)
checks += 1

print(f"PASS: {checks} exact finite algebra/component checks.")
