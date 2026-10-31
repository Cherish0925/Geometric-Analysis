"""Exact presentation and Euler-volume checks for round8_construction.md.

Run: qiushi-yau26 env numeric python round8_construction_check.py
No general Einstein existence/nonexistence is tested by this script.
"""

import sympy as s
from sympy.combinatorics.free_groups import free_group


def check(value, label):
    assert value, label
    print(f"PASS {label}")


F, a, b, c, d = free_group("a b c d")
comm = lambda x, y: x*y*x**-1*y**-1
check(comm(a, b*a) == comm(a, b), "based twist preserves handle relator")
check(comm(a, b*a**-1) == comm(a, b), "inverse twist preserves relator")
for k in [-3, -1, 1, 2, 5]:
    check(comm(a, b*a**k) == comm(a, b), f"power-twist relator k={k}")

p, q = s.symbols("p q", integer=True, positive=True)
chi = 4*(p-1)*(q-1)
euler_cap = (2*p-4)*(2*q-2)
V0 = 16*s.pi**2*(p-1)*(q-1)
check(s.expand(chi-euler_cap) == 4*(q-1), "exact Euler-product deficit")
check(s.simplify(4*s.pi**2*euler_cap/V0-(p-2)/(p-1)) == 0,
      "sharp representation-volume normalization")
check(euler_cap.subs(p, 2) == 0, "genus-two representation volume vanishes")

for gp in range(2, 7):
    for gq in range(2, 7):
        classes = {(k, 0) for k in range(-2*gp+4, 2*gp-3)}
        classes |= {(0, l) for l in range(-2*gq+2, 2*gq-1)}
        # Pairing (a,b).(c,d)=a*d+b*c; alpha^2=beta^2=0.
        maximum = max(abs(x[0]*y[1]+x[1]*y[0])
                      for x in classes for y in classes)
        check(maximum == (2*gp-4)*(2*gq-2),
              f"Euler-line cup bound p={gp}, q={gq}")

# An order-two element in PSL(2,R) illustrates why D^k cannot be
# replaced by D in the curve-killing conclusion for torsion targets.
I = s.eye(2)
J = s.Matrix([[0, -1], [1, 0]])
check(J != I and J != -I and J**2 == -I,
      "power-twist PSL2R counterexample has nontrivial A with A^2=1 in PSL")

# Real matrices anticommuting with J have negative determinant;
# hence the elliptic order-two PSL2R centralizer has no extra component.
u, v = s.symbols("u v", real=True)
C = s.Matrix([[u, v], [v, -u]])
check(C*J == -J*C and s.expand(C.det()) == -u**2-v**2,
      "real order-two centralizer exception excluded")

# In PSL(2,C), by contrast, a nontrivial order-two A can survive.
# This is a scope test, not a PSL2R representation.
i = s.I
A = s.diag(i, -i)
B = J
z = (1-i)/s.sqrt(2)
T = s.diag(z, 1/z)
def zero_matrix(M):
    return all(s.simplify(entry) == 0 for entry in M)
check(zero_matrix(T*A*T.inv()-A), "complex example T centralizes A")
check(zero_matrix(A*B*A.inv()*B.inv()+I),
      "complex example surface commutator is identity only in PSL")
check(zero_matrix(T*B*T.inv()-B*A), "complex example satisfies single-twist relation")
check(A != I and A != -I, "complex example A is not identity in PSL")

print("All checks passed. The general group and geometric arguments are in the note.")
