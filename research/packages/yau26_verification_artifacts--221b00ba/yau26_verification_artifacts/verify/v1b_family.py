import sympy as sp, pickle
r,Lam = sp.symbols('r Lambda', real=True)
d = pickle.load(open('biaxial_ricci.pkl','rb'))
Xs,Ys,Zs = sp.Function('X')(r), sp.Function('Y')(r), sp.Function('Z')(r)
G = sp.Function('G')(r)
c = (1-Lam/4)**2-1
F = (1+c*r**2)*G
# ODE: r(1+c r^2) G' + (4+3 c r^2) G = 4 - Lam r^2
Gp = (4-Lam*r**2-(4+3*c*r**2)*G)/(r*(1+c*r**2))
Gpp = sp.diff(Gp,r).subs(sp.Derivative(G,r),Gp)
def ev(expr):
    e = expr.subs({Xs:1/F, Ys:r**2/4, Zs:r**2*G/4}).doit()
    e = e.subs(sp.Derivative(G,(r,2)),Gpp).subs(sp.Derivative(G,r),Gp)
    return sp.simplify(e)
for k in ['R0','R1','R3']:
    print(k,'- Lambda =', sp.simplify(ev(d[k])-Lam))
