"""Exact algebra behind the rank obstruction and its NPC sharpness family."""
import sympy as s

n = s.symbols("n", integer=True, positive=True)
k2 = 2*n/(n+1)
gap = n*(n-1)/(n+1)
assert s.simplify(n*(k2-1)-gap) == 0
assert s.simplify(n-k2-gap) == 0
assert s.simplify((2*n-(n+1))*n/(n+1)-gap) == 0
assert gap.subs(n,3) == s.Rational(3,2)
assert k2.subs(n,3) == s.Rational(3,2)

# All algebraic curvature entries in an orthonormal d-frame.
# Flat tangent planes have zero curvature; the trace difference sees
# exactly twice the normal-normal sectional curvatures, without cross terms.
for dim in range(3,9):
    for rank in range(1,dim):
        sectional = {}
        for i in range(dim):
            for j in range(i+1,dim):
                sectional[i,j] = (s.Integer(0) if j < rank else
                                   s.Symbol(f"K_{i}_{j}"))
        ric = [sum(sectional[min(i,j),max(i,j)]
                   for j in range(dim) if j != i) for i in range(dim)]
        difference = sum(ric[rank:])-sum(ric[:rank])
        normal = 2*sum(sectional[i,j] for i in range(rank,dim)
                       for j in range(i+1,dim))
        assert s.expand(difference-normal) == 0

# Ricci contribution to a four-dimensional plane with Ric=-3I+E.
e = s.symbols("e0:4", real=True)
correction = (e[0]+e[1])/2-sum(e)/6
assert [s.diff(correction,v) for v in e] == [
    s.Rational(1,3),s.Rational(1,3),-s.Rational(1,6),-s.Rational(1,6)]
assert sum(abs(s.diff(correction,v)) for v in e) == 1

print("PASS: flat-rank Ricci trace identity, all-dimensional sharp balancing, four-dimensional Weyl correction")
print("Scope: exact algebra; the flat torus theorem, minimizing loops, and mollifier estimates are analytic arguments in the accompanying note.")
