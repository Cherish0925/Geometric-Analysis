"""Step 62: exact check of the zero-index determinant formula and its restriction to the cone
||A||^2 = 8|c|^2 + ||S||^2  (Frobenius norms; f(z) = c z + (S+A) zbar on C^2)."""
import sympy as sp
c1, c2 = sp.symbols('c1 c2', real=True)
s = sp.symbols('s1:7', real=True); a1, a2 = sp.symbols('a1 a2', real=True)
I = sp.I
c = c1 + I*c2
S = sp.Matrix([[s[0] + I*s[1], s[2] + I*s[3]], [s[2] + I*s[3], s[4] + I*s[5]]])
a = a1 + I*a2
A = sp.Matrix([[0, a], [-a, 0]])
B = S + A
x = sp.symbols('x1:5', real=True)
z = sp.Matrix([x[0] + I*x[1], x[2] + I*x[3]])
f = c*z + B*z.conjugate()
comps = [sp.re(sp.expand(f[0])), sp.im(sp.expand(f[0])), sp.re(sp.expand(f[1])), sp.im(sp.expand(f[1]))]
Mr = sp.Matrix([[sp.diff(comp, xi) for xi in x] for comp in comps])
det = sp.expand(Mr.det())
nc2 = c1**2 + c2**2
nS2 = sum(sp.Abs(e)**2 for e in S).expand(complex=True)
nA2 = sp.expand(2*(a1**2 + a2**2))
dB = sp.expand(B.det())
dB2 = sp.expand(sp.re(dB)**2 + sp.im(dB)**2)
formula = sp.expand(nc2**2 - nc2*(nS2 - nA2) + dB2)
print("det - A02 formula =", sp.simplify(det - formula))
# Frobenius norm of the real matrix vs complex data
fro = sp.expand(sum(e**2 for e in Mr))
print("real Frobenius - (4|c|^2 + 2||S||^2 + 2||A||^2) =", sp.simplify(fro - (4*nc2 + 2*nS2 + 2*nA2)))
# On the cone ||A||^2 = 8|c|^2+||S||^2:  det = 9|c|^4 + |det B|^2 and |det B| >= |a|^2-|det S| >= 4|c|^2
print("cone: det = 9|c|^4 + |detB|^2  (by substitution nA2 -> 8nc2+nS2):",
      sp.simplify(formula.subs(nA2, 8*nc2 + nS2) - (9*nc2**2 + dB2)) if False else sp.simplify((nc2**2 - nc2*(nS2 - (8*nc2 + nS2)) + dB2) - (9*nc2**2 + dB2)))
