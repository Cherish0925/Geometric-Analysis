import os, json
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "data", "step52a")
d = json.load(open(os.path.join(D, "exact_su2minus_Q.json")))
Q = sp.Matrix([[sp.Rational(z) for z in row] for row in d["Q"]])
Hc = Q[5:, 5:]
print("Hc eigen", Hc.eigenvals())
ns = Hc.nullspace()
print("null vectors", [list(n) for n in ns])
Bj = Q[5:, :5]   # coupling corrector <- jet (s,w11,w22,w12,w13)
for n in ns:
    print("null . B (coeffs of s,w11,w22,w12,w13):", list(n.T*Bj))
print("Q jet block", Q[:5, :5])
print("B", Bj)
