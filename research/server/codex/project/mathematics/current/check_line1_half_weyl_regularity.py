#!/usr/bin/env python3
"""Exact algebraic checks for the half-Weyl equation-to-budget note.

No discretized PDE or global geometric assertions are tested here.
"""
import json
import sympy as s


checks = []


def equal(name, lhs, rhs):
    difference = lhs - rhs
    if isinstance(difference, s.MatrixBase):
        assert all(s.simplify(x) == 0 for x in difference), name
    else:
        assert s.simplify(difference) == 0, name
    checks.append(name)


def norm2(matrix):
    return s.trace(matrix.T * matrix)


def commutator(left, right):
    return left * right - right * left


l1, l2, a, b, c, h1, h2 = s.symbols("l1 l2 a b c h1 h2", real=True)
D = s.diag(l1, l2, -l1-l2)
P = s.diag(1, 0, 0)
I = s.eye(3)
K = s.Matrix([[0, a, b], [-a, 0, c], [-b, -c, 0]])
H = s.diag(h1, h2, -h1-h2)
W1 = H + commutator(K, D)
W2 = 2 * commutator(K, H) + commutator(K, commutator(K, D))
P1 = commutator(K, P)
P2 = commutator(K, commutator(K, P))
S = s.diag(0, 1/(l2-l1), 1/(-2*l1-l2))

equal("Weyl equation preserves trace", s.trace(2*D+6*D**2-2*norm2(D)*I), 0)
Wke = s.diag(-s.Rational(2,3), s.Rational(1,3), s.Rational(1,3))
equal("negative KE solves algebraic equation", 2*Wke+6*Wke**2-2*norm2(Wke)*I, s.zeros(3))
equal("projector first derivative", P1, -S*W1*P-P*W1*S)
equal("eigenvalue first derivative", s.trace(P*W1), h1)
equal("eigen equation first jet", (D-l1*I)*P1+(W1-h1*I)*P, s.zeros(3))
equal("eigen equation second jet", (D-l1*I)*P2+2*(W1-h1*I)*P1+W2*P, s.zeros(3))
equal("projector first jet", P1*P+P*P1, P1)
equal("projector second jet", P2*P+2*P1*P1+P*P2, P2)

A = l1*(3*P-I)/2
A1 = h1*(3*P-I)/2+3*l1*P1/2
A2 = 3*h1*P1+3*l1*P2/2
equal("model first jet", A1, h1*(3*P-I)/2+commutator(K,A))
equal("model second jet", A2, 2*commutator(K,h1*(3*P-I)/2)+commutator(K,commutator(K,A)))
equal("upper splitting residual", norm2(D-A), (l1+2*l2)**2/2)

t, h = s.symbols("t h", real=True)
Wt = s.diag(-4*t/3, 2*t/3-h/2, 2*t/3+h/2)
equal("KE orbit distance", norm2(Wt-Wke), 8*(t-s.Rational(1,2))**2/3+h**2/2)
equal("spectral rank-one model", A, (-3*l1/4)*(s.Rational(2,3)*I-2*P))

# Two independent trace-free eigenvalue gaps parametrize ordered matrices.
rho, gap_extra, upper_gap = s.symbols("rho gap_extra upper_gap", nonnegative=True)
lowest = -(2*(rho+gap_extra)+upper_gap)/3
middle = lowest+rho+gap_extra
highest = middle+upper_gap
equal("ordered trace constraint", lowest+middle+highest, 0)
equal("automatic amplitude lower bound", -3*lowest/4-rho/2, gap_extra/2+upper_gap/4)

# Reject sign and factor mutations that could fake a valid-looking estimate.
rejected = []
wrong_pde = -2*Wke+6*Wke**2-2*norm2(Wke)*I
assert wrong_pde != s.zeros(3)
rejected.append("scalar sign reversed in Einstein equation")
assert s.simplify(norm2(D-A)-(l1+2*l2)**2) != 0
rejected.append("missing one-half in eigenvalue-splitting norm")
assert s.simplify(norm2(Wt-Wke)-4*(t-s.Rational(1,2))**2/3-h**2/2) != 0
rejected.append("wrong amplitude factor in KE orbit distance")

print(json.dumps({"status": "passed", "exact_checks": checks,
                  "intentional_errors_rejected": rejected,
                  "scope": "finite algebra only; analytic proof is in the note"}, indent=2))
