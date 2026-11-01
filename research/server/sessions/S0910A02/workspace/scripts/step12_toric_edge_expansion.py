"""
Step 12: symbolic edge expansion for the twist-free toric Einstein equations.
Base metric near an edge: g_B=dr^2+a(r,s)^2 ds^2, a=1+a2(s) r^2/2+O(r^3).
Collapsing length p=r+p3(s)r^3+O(r^4); transverse length q=Q(s)+q2(s)r^2+O(r^3).
Einstein normalization lambda=1.
Verifies leading equations:
  p3=(-2 a2-1)/6, 2 q2=a2 Q, Q''+(1+2a2)Q=0.
"""
import sympy as sp, json, os
r=sp.symbols('r')
s=sp.symbols('s')
a2=sp.Function('a2')(s); p3=sp.Function('p3')(s); q2=sp.Function('q2')(s); Q=sp.Function('Q')(s)
a=1+sp.Rational(1,2)*a2*r**2
p=r+p3*r**3
q=Q+q2*r**2
# Keep terms through leading needed orders. K=-a_rr/a in geodesic edge coords.
K=sp.series(-sp.diff(a,r,2)/a, r, 0, 2).removeO()

def Lap(u):
    return sp.diff(u,r,2)+(sp.diff(a,r)/a)*sp.diff(u,r)+(1/a**2)*sp.diff(u,s,2)

def grad_dot(u,v):
    return sp.diff(u,r)*sp.diff(v,r)+(1/a**2)*sp.diff(u,s)*sp.diff(v,s)

# Equations: Delta p=(K-1)p, Delta q=(K-1)q, <grad p,grad q>=-Kpq
eq_p=sp.series(Lap(p)-(K-1)*p,r,0,2).removeO().expand()
eq_q=sp.series(Lap(q)-(K-1)*q,r,0,1).removeO().expand()
eq_g=sp.series(grad_dot(p,q)+K*p*q,r,0,2).removeO().expand()
# coeffs
coeff_p_r=sp.factor(eq_p.coeff(r,1))
coeff_q_0=sp.factor(eq_q.coeff(r,0))
coeff_g_r=sp.factor(eq_g.coeff(r,1))
# solve sequentially
sol_p3=sp.solve(sp.Eq(coeff_p_r,0),p3)[0]
sol_q2=sp.solve(sp.Eq(coeff_g_r,0),q2)[0]
remaining_q=sp.factor(coeff_q_0.subs(q2,sol_q2))
print("K at edge =", sp.series(K,r,0,1).removeO())
print("Coeff r in Delta p-(K-1)p:", coeff_p_r, "=> p3=", sol_p3)
print("Coeff r in <grad p,grad q>+Kpq:", coeff_g_r, "=> q2=", sol_q2)
print("Coeff 0 in Delta q-(K-1)q after q2 substitution:", remaining_q)
out={
    "K_edge":"-a2(s)",
    "coeff_p_r":str(coeff_p_r),
    "p3_solution":str(sol_p3),
    "coeff_grad_r":str(coeff_g_r),
    "q2_solution":str(sol_q2),
    "remaining_q_equation":str(remaining_q),
    "interpretation":"remaining_q_equation=0 is Q''+(1+2*a2)Q=0"
}
OUTDIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data")); os.makedirs(OUTDIR,exist_ok=True)
OUT=os.path.join(OUTDIR,"step12_toric_edge_expansion.json")
with open(OUT,"w") as f: json.dump(out,f,indent=2)
print("Saved",OUT)
