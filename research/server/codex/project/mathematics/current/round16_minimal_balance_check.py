"""Finite identities for the minimal-surface shear application.

The existence and global topology of Schwarz P are not numerical claims
made by this program. See round16_minimal_balance.md.
"""
import sympy as s

u, v, t, lam, r, p, q, V = s.symbols(
    "u v t lam r p q V", real=True
)
beta = [
    s.Matrix([1-u*u+v*v, 2*u*v]),
    s.Matrix([-2*u*v, -1-u*u+v*v]),
    s.Matrix([2*u, -2*v]),
]
checks = []


def zero(name, expression):
    if isinstance(expression, s.MatrixBase):
        assert all(s.simplify(x) == 0 for x in expression), name
    else:
        assert s.simplify(expression) == 0, name
    checks.append(name)


def stress(b):
    return b*b.T - (b.dot(b)/2)*s.eye(2)


for i, b in enumerate(beta, 1):
    zero(f"closed coordinate form {i}", s.diff(b[0], v)-s.diff(b[1], u))
    zero(f"coclosed coordinate form {i}", s.diff(b[0], u)+s.diff(b[1], v))
zero("three stresses cancel", sum((stress(b) for b in beta), s.zeros(2)))
zero("conformal induced metric",
     sum((b*b.T for b in beta), s.zeros(2))
     - (1+u*u+v*v)**2*s.eye(2))
zero("energy is twice conformal area",
     sum(b.dot(b) for b in beta)-2*(1+u*u+v*v)**2)
L = s.diag(lam, -lam)
zero("parallel-area determinant", (s.eye(2)-t*L).det()-(1-lam**2*t**2))
zero("minimal Gauss relation", -s.trace(L*L)/2+lam**2)
zero("energy second derivative coefficient",
     s.diff(4*s.pi*(2-2*p)*t*t, t, 2)+16*s.pi*(p-1))
zero("closed Euler characteristic", (2-2*r-6)*(2-6)-(8*r+16))
zero("closed functional second derivative sign",
     (-s.pi*q/s.sqrt(V))*(-16*s.pi*(p-1))
     -16*s.pi**2*q*(p-1)/s.sqrt(V))

# Dropping a form or altering a weight does not preserve this identity.
at = {u:s.Rational(1, 2), v:s.Rational(1, 3)}
for i in range(3):
    reduced = sum((stress(b) for j,b in enumerate(beta) if j != i), s.zeros(2))
    assert reduced.subs(at) != s.zeros(2)
wrong_weight = sum((stress(b) for b in beta), s.zeros(2))+stress(beta[0])
assert wrong_weight.subs(at) != s.zeros(2)
print(f"PASS {len(checks)} exact identities")
for name in checks:
    print("  "+name)
print("PASS three dropped-form and one unequal-weight negative controls")
