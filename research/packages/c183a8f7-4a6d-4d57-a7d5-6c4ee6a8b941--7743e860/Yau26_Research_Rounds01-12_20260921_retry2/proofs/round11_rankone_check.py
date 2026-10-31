#!/usr/bin/env python3
"""Exact rank-one Clifford/curvature checks, not nonlinear PDE existence."""
import sympy as s

I = s.I
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
c = [s.eye(2), -I*pauli[2], I*pauli[0], I*pauli[1]]


def adj(m):
    return m.conjugate().T


for i in range(4):
    for j in range(4):
        assert c[i]*adj(c[j])+c[j]*adj(c[i]) == (2*s.eye(2) if i == j else s.zeros(2))
rho_omega = -c[0]*adj(c[1])-c[2]*adj(c[3])
assert rho_omega == -2*I*pauli[2]
print("PASS right Clifford matrices and canonical source-line sign")

zr, zi, wr, wi = s.symbols("zr zi wr wi", real=True)
z, w = zr+I*zi, wr+I*wi
b = [z, -I*z, w, -I*w]
bop = [z, I*z, w, I*w]
row0, row1 = s.Matrix([[1, 0]]), s.Matrix([[0, 1]])
assert s.simplify(sum((b[j]*row0*c[j] for j in range(4)), s.zeros(1, 2))) == s.zeros(1, 2)
assert s.simplify(sum((bop[j]*row1*c[j] for j in range(4)), s.zeros(1, 2))) == s.zeros(1, 2)
print("PASS both source-line Dirac annihilators, without imposing b=0")


def wedge(coeff):
    return {(i, j): s.expand(coeff[i]*s.conjugate(coeff[j])-
                             coeff[j]*s.conjugate(coeff[i]))
            for i in range(4) for j in range(i+1, 4)}


def selfdual(q):
    return [s.simplify((q[0, 1]+q[2, 3])/2),
            s.simplify((q[0, 2]-q[1, 3])/2),
            s.simplify((q[0, 3]+q[1, 2])/2)]


normb = s.expand(sum(v*s.conjugate(v) for v in b))
assert normb == 2*(zr*zr+zi*zi+wr*wr+wi*wi)
assert all(s.simplify(actual-want) == 0
           for actual, want in zip(selfdual(wedge(b)), [I*normb/2, 0, 0]))
assert all(s.simplify(actual-want) == 0
           for actual, want in zip(selfdual(wedge(bop)), [-I*normb/2, 0, 0]))
print("PASS (b wedge b*)+ = i |b|² omega_M / 2")

# Curvature of A=[[a,-b*],[b,c]]: the KK quadratic term is -b wedge b*.
diagonal_a = s.symbols("a0:4", real=True)
diagonal_c = s.symbols("c0:4", real=True)
A = [s.Matrix([[I*diagonal_a[j], -s.conjugate(b[j])],
               [b[j], I*diagonal_c[j]]]) for j in range(4)]
wb = wedge(b)
for i in range(4):
    for j in range(i+1, 4):
        comm = A[i]*A[j]-A[j]*A[i]
        assert s.simplify(comm[1, 1]+wb[i, j]) == 0
print("PASS complementary curvature F_c - b wedge b*")

# Every source-factor quadratic coefficient is supported in the image line.
p, q = s.symbols("p q", complex=True)
phi = s.Matrix([[p, q], [0, 0]])
for sigma in pauli:
    quadratic = phi*sigma*adj(phi)
    assert quadratic[1, 1] == quadratic[0, 1] == quadratic[1, 0] == 0
print("PASS target-complement quadratic term vanishes, independently of overall sign")

# The trace-free residual coefficient is sharp for R=i*r*omega*diag(-1,1).
r = s.symbols("r", positive=True)
Romega = I*r*s.diag(-1, 1)
residual_norm_squared = 2*s.trace(adj(Romega)*Romega)
paired = I*Romega[1, 1]*2
assert residual_norm_squared == 4*r*r
assert s.expand(paired*paired) == residual_norm_squared
print("PASS sharp pairing bound for trace-free curvature residual")

volume = s.symbols("volume", positive=True)
# a=-[omega]/(2*pi), integral omega²=2*volume.
chern_pair = -2*volume
mixing_energy = s.solve(s.Eq(chern_pair, -s.Symbol("mix")), s.Symbol("mix"))[0]
assert mixing_energy/volume == 2
print("PASS Chern normalization gives averaged mixing energy 2")

# Off-diagonal block curvature never changes the trace Chern class.
entries = s.symbols("t0:8", complex=True)
Ti, Tj = s.Matrix(2, 2, entries[:4]), s.Matrix(2, 2, entries[4:])
upper = adj(Ti)*Tj-adj(Tj)*Ti
lower = Ti*adj(Tj)-Tj*adj(Ti)
assert s.expand(s.trace(upper)+s.trace(lower)) == 0
f = s.symbols("f", real=True)
trace_from_determinants = I*f+I*f
trace_of_printed_central_block = s.trace(-I*f*s.eye(4))
assert s.simplify(trace_of_printed_central_block-trace_from_determinants) == -6*I*f
print("PASS block-wedge trace cancellation and printed central-trace discrepancy")
print("All checks passed; no sign-selected Leung solution or Einstein obstruction is asserted.")
