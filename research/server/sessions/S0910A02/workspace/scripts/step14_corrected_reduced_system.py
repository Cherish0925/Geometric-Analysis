"""
Step 14 (S0910A02): CORRECTED reduced system and base-curvature formula.

This script establishes the correct complete reduced Einstein system for
twist-free toric positive Einstein 4-manifolds, checks it on S^2 x S^2,
and identifies the correct base-curvature formula.

CORRECTED DERIVATION:
For g = g_B + p^2 dtheta^2 + q^2 dphi^2 on (Omega, g_B), with w = pq, v = log(p/q):

Horizontal Einstein:  Ric_B(X,Y) - Hess(p)(X,Y)/p - Hess(q)(X,Y)/q = lambda g_B(X,Y)
Vertical Einstein (theta):  -Delta p/p - <grad p, grad q>/(pq) = lambda
Vertical Einstein (phi):   -Delta q/q - <grad p, grad q>/(pq) = lambda
Determinant (sum of vertical): -Delta(pq)/(pq) = 2 lambda
Ratio (difference of vertical):  div(w grad v) = 0

In the (w,v) parametrization (p = sqrt(w) e^{v/2}, q = sqrt(w) e^{-v/2}):

Identity: Hess(p)/p + Hess(q)/q = (log w)_{ab} + (1/2)[(log w)_a (log w)_b + v_a v_b]

NOTE: the factor 1/2 on v_a v_b is because log p = (log w + v)/2, NOT log w/2 + v.

Trace of horizontal: 2 K_B - Delta(log w) - (1/2)(|grad log w|^2 + |grad v|^2) = 2 lambda
Using Delta(log w) = -2 lambda - |grad log w|^2:
K_B = (1/4)(|grad v|^2 - |grad log w|^2)

Equivalently: K_B = -<grad log p, grad log q>.
"""
import json, math, os
import sympy as sp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# =====================================================================
# CHECK 1: S^2(1) x S^2(1) with Ric = g (lambda=1)
# g_B = dx^2 + dy^2 (flat square [0,pi]^2), p = sin x, q = sin y.
# =====================================================================
x, y = sp.symbols('x y', real=True, positive=True)
p_s2 = sp.sin(x)
q_s2 = sp.sin(y)
w_s2 = p_s2 * q_s2
v_s2 = sp.log(p_s2 / q_s2)

# Base curvature (should be 0 for flat g_B)
grad_logp = [sp.diff(sp.log(p_s2), x), sp.diff(sp.log(p_s2), y)]
grad_logq = [sp.diff(sp.log(q_s2), x), sp.diff(sp.log(q_s2), y)]
KB_direct = -sp.simplify(sum(a*b for a,b in zip(grad_logp, grad_logq)))

grad_logw = [sp.diff(sp.log(w_s2), x), sp.diff(sp.log(w_s2), y)]
grad_v = [sp.diff(v_s2, x), sp.diff(v_s2, y)]
norm2_grad_v = sp.simplify(sum(a**2 for a in grad_v))
norm2_grad_logw = sp.simplify(sum(a**2 for a in grad_logw))
KB_formula = sp.Rational(1,4) * sp.simplify(norm2_grad_v - norm2_grad_logw)

# Horizontal equation check: p_{ab}/p + q_{ab}/q should equal (K_B - 1) delta_{ab}
hess_p_over_p = [[sp.simplify(sp.diff(p_s2, a, b) / p_s2) for b in [x,y]] for a in [x,y]]
hess_q_over_q = [[sp.simplify(sp.diff(q_s2, a, b) / q_s2) for b in [x,y]] for a in [x,y]]
horiz_sum = [[sp.simplify(hess_p_over_p[i][j] + hess_q_over_q[i][j]) for j in range(2)] for i in range(2)]

# Formula via (w,v): (log w)_{ab} + (1/2)[(log w)_a (log w)_b + v_a v_b]
logw = sp.log(w_s2)
hess_logw = [[sp.simplify(sp.diff(logw, a, b)) for b in [x,y]] for a in [x,y]]
formula_check = [[sp.simplify(hess_logw[i][j] + sp.Rational(1,2)*(grad_logw[i]*grad_logw[j] + grad_v[i]*grad_v[j]))
                  for j in range(2)] for i in range(2)]

# Vertical equation check
lap_p = sp.simplify(sp.diff(p_s2, x, x) + sp.diff(p_s2, y, y))
lap_q = sp.simplify(sp.diff(q_s2, x, x) + sp.diff(q_s2, y, y))
gradp_dot_gradq = sp.simplify(sp.diff(p_s2,x)*sp.diff(q_s2,x) + sp.diff(p_s2,y)*sp.diff(q_s2,y))
vert_theta = sp.simplify(-lap_p/p_s2 - gradp_dot_gradq/(p_s2*q_s2))
vert_phi = sp.simplify(-lap_q/q_s2 - gradp_dot_gradq/(p_s2*q_s2))

# Div(w grad v) = 0 check
div_w_gradv = sp.simplify(sp.diff(w_s2*grad_v[0], x) + sp.diff(w_s2*grad_v[1], y))

# Traceless condition: (log w)_{zz} + (1/2)[(log w)_z^2 + v_z^2] = 0
# In real coordinates: the traceless part of the horizontal sum = 0.
traceless_xx_minus_yy = sp.simplify(formula_check[0][0] - formula_check[1][1])
traceless_xy = sp.simplify(formula_check[0][1])

report = {
    "title": "Step 14: corrected reduced system verification on S^2 x S^2",
    "S2xS2_data": {
        "g_B": "dx^2+dy^2 (flat)", "domain": "[0,pi]^2",
        "p": "sin x", "q": "sin y", "w": "sin x sin y", "v": "log(sin x/sin y)"
    },
    "KB_direct_minus_inner_product": str(KB_direct),
    "KB_via_gradient_formula": str(KB_formula),
    "KB_check": "PASS" if sp.simplify(KB_direct - KB_formula) == 0 else "FAIL",
    "horizontal_sum": [[str(formula_check[i][j]) for j in range(2)] for i in range(2)],
    "direct_horizontal_sum": [[str(horiz_sum[i][j]) for j in range(2)] for i in range(2)],
    "formula_matches_direct": str(all(sp.simplify(formula_check[i][j] - horiz_sum[i][j])==0 for i in range(2) for j in range(2))),
    "vertical_theta_equals_lambda": str(vert_theta),
    "vertical_phi_equals_lambda": str(vert_phi),
    "div_w_gradv": str(div_w_gradv),
    "traceless_xx_minus_yy": str(traceless_xx_minus_yy),
    "traceless_xy": str(traceless_xy),
    "CORRECTED_base_curvature_formula": {
        "formula": "K_B = (1/4)(|grad v|^2 - |grad log w|^2) = -<grad log p, grad log q>",
        "S2xS2_value": "0 (flat, correct)",
        "sign": "K_B can be positive or negative depending on relative magnitudes",
        "RETRACTED": "The earlier K_B >= 3 was from the WRONG formula Hess(log w) = (K_B-1)g_B; the correct formula has an extra quadratic gradient term."
    },
    "complete_reduced_system": {
        "eq1": "-Delta_B w = 2 w,  w=0 on dOmega  (determinant eigenvalue)",
        "eq2": "div_B(w grad v) = 0,  v -> +-infty at alternating rods  (ratio harmonic eq.)",
        "eq3": "(log w)_{zz} + (1/2)[(log w)_z^2 + v_z^2] = 0  (traceless horizontal)",
        "eq4": "K_B = (1/4)(|grad v|^2 - |grad log w|^2)",
        "eq5": "int_Omega K_B dA = 2pi - (pi/2)chi(M)  (Gauss-Bonnet corners)",
        "eq6": "Unit closure: dp/dr -> 1 (or dq/dr -> 1) at each rod, primitive"
    }
}

OUT = os.path.join(DATA, "step14_corrected_reduced_system.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"\nSaved {OUT}")
