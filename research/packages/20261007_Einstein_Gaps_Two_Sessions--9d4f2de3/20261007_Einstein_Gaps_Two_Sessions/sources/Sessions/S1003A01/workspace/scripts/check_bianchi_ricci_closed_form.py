"""Symbolic check that the closed Bianchi-IX Ricci formula used in
perp_rigorous_enclosure.py equals the Cartan-derived Ricci of perp_cartan_verify.py.

R00 = -(a''/a+b''/b+c''/c),
Rii = -ai''/ai - (ai'/ai)(aj'/aj+ak'/ak) + 2(ai^4-(aj^2-ak^2)^2)/(ai^2 aj^2 ak^2).
Also checks the desingularized D1 and A2,A3 rewritings used near the bolt.
"""
import contextlib, io, runpy
import sympy as sp

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path('perp_cartan_verify.py')
Ric = ns['Ric']; A = ns['A']; A1 = ns['A1']; A2 = ns['A2']
a, b, c = A
closed = [-(A2[0]/a + A2[1]/b + A2[2]/c)]
for i in range(3):
    j, k = (i+1) % 3, (i+2) % 3
    closed.append(-A2[i]/A[i] - (A1[i]/A[i])*(A1[j]/A[j] + A1[k]/A[k])
                  + 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/(A[i]**2*A[j]**2*A[k]**2))
print('closed-form Ricci minus Cartan Ricci:', [sp.cancel(sp.together(closed[n] - Ric[n])) for n in range(4)], flush=True)

# Desingularized pieces in the x variable (d/dt = 2 sqrt(G) d/dx, h = a^2, h1 = y FH, G = y GH).
y = sp.symbols('y', positive=True)
FH, GH = sp.Function('FH')(y), sp.Function('GH')(y)
h1 = y*FH; G = y*GH
a1t = 2*sp.sqrt(G)*sp.diff(sp.sqrt(h1), y)
a1tt = 2*sp.sqrt(G)*sp.diff(a1t, y)
D1_raw = a1tt/sp.sqrt(h1)
rho = GH/FH
D1_new = 2*rho*sp.diff(h1, y, 2) + sp.diff(h1, y)*(sp.diff(GH, y)*FH - GH*sp.diff(FH, y))/FH**2
f0, f1, f2, g0, g1 = sp.symbols('f0 f1 f2 g0 g1', positive=True)
rep = {sp.Derivative(FH, (y, 2)): f2, sp.Derivative(FH, y): f1, sp.Derivative(GH, y): g1}
d1 = (D1_raw - D1_new).subs(rep).subs({FH: f0, GH: g0})
print('D1 rewrite residual:', sp.cancel(sp.together(sp.expand(d1))), flush=True)
w, x, h1s = sp.symbols('w x h1', positive=True)
h2, h3 = x, x*sp.exp(w)
A2raw = 2*(h2**2 - (h3 - h1s)**2)/(h1s*h2*h3)
A2new = -4*sp.sinh(w)/h1s + 4/x - 2*h1s/(x**2*sp.exp(w))
E = sp.symbols('E', positive=True)
sub = lambda e: sp.cancel(sp.together(e.rewrite(sp.exp).subs(sp.exp(w), E)))
print('A2 rewrite residual:', sub(A2raw - A2new))
A3raw = 2*(h3**2 - (h1s - h2)**2)/(h1s*h2*h3)
A3new = 4*sp.sinh(w)/h1s + 4/(x*sp.exp(w)) - 2*h1s/(x**2*sp.exp(w))
print('A3 rewrite residual:', sub(A3raw - A3new))
A1raw = 2*(h1s**2 - (h2 - h3)**2)/(h1s*h2*h3)
A1new = 2*h1s/(x*h3) - 2*x**2*(sp.exp(w) - 1)**2/(h1s*x*h3)
print('A1 rewrite residual:', sub(A1raw - A1new))
