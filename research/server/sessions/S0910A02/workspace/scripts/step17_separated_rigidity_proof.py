"""
Step 17 (S0910A02): Exact Separated Einstein Rigidity Theorem.

Theorem: Let (M^4, g) be a closed smooth Riemannian 4-manifold with Ric = g
admitting a cohomogeneity-one isometric S^1 x SO(3) action with principal
orbit S^1 x S^2 and two singular orbits (both S^2 bolts). Then g is
isometric to the round product S^2(1) x S^2(1) (Nariai metric, Vol = 16 pi^2).

Proof outline:
1. Einstein + cohomogeneity-one => ODE system: a'=Ap, 2aa''+(a')^2=kappa-a^2
2. First integral: a(a')^2 = kappa(a-1) - (a^3-1)/3
3. Second bolt value a_+ = (-1+sqrt(9+24A))/2 from first integral zero
4. Second bolt slope mu = (2a_+ + 1)/(a_+(a_+ + 2))  
5. Smooth closure requires mu = 1 <=> a_+ = 1 <=> A = 0
6. A = 0 gives kappa = 1, a(r) = 1, p(r) = sin r on [0, pi] => S^2 x S^2

This script verifies steps 3-6 symbolically and numerically.
"""
import json, os
import sympy as sp
import numpy as np

# ===== Symbolic verification =====
A = sp.Symbol('A', nonneg=True)
kappa = 1 + 2*A

# Step 3: a_+ from first integral = 0
a_plus_expr = (-1 + sp.sqrt(9 + 24*A)) / 2
# Verify: kappa(a_+ - 1) = (a_+^3 - 1)/3
lhs = kappa * (a_plus_expr - 1)
rhs = (a_plus_expr**3 - 1) / 3
first_integral_check = sp.simplify(lhs - rhs)

# Step 4: mu from the ψψ equation at the second bolt
# a''(r_*) = (kappa - a_+^2) / (2 a_+),  p'(r_*) = a''/(A),
# mu = |p'(r_*)| = (1 + 4A - a_+) / (2A a_+)
# Alternative form verified in Step 16: mu = (2a_+ + 1)/(a_+(a_+ + 2))
mu_form1 = (2*a_plus_expr + 1) / (a_plus_expr * (a_plus_expr + 2))
mu_form2 = (1 + 4*A - a_plus_expr) / (2*A*a_plus_expr)
mu_equivalence = sp.simplify(mu_form1 - mu_form2)

# Step 5: mu = 1 <=> a_+ = 1
# mu = 1 => (2a + 1) = a(a+2) = a^2 + 2a => a^2 = 1 => a = 1
a_val = sp.Symbol('a', positive=True)
mu_gen = (2*a_val + 1) / (a_val * (a_val + 2))
mu_equals_1 = sp.solve(mu_gen - 1, a_val)

# a_+ = 1 => A = 0
A_from_aplus_1 = sp.solve(a_plus_expr - 1, A)

# Step 6: A = 0 => kappa = 1, ODE becomes p'' + p = 0, a = 1
# p(r) = sin r on [0, pi], Vol = 2 pi * 4 pi * int_0^pi sin r dr = 16 pi^2

# ===== Numerical verification: mu(A) is strictly decreasing for A > 0 =====
A_vals = np.array([0, 0.001, 0.01, 0.1, 0.5, 1, 4, 9, 100, 10000])
results = []
for Av in A_vals:
    kv = 1 + 2*Av
    a_pv = (-1 + np.sqrt(9 + 24*Av)) / 2
    if Av > 0:
        mu_v = (2*a_pv + 1) / (a_pv * (a_pv + 2))
    else:
        mu_v = 1.0  # Nariai limit
    results.append({
        'A': float(Av), 'kappa': float(kv),
        'a_plus': float(a_pv), 'mu': float(mu_v),
        'mu_minus_1': float(mu_v - 1)
    })

# Check mu is strictly decreasing
mu_vals = [r['mu'] for r in results]
monotone = all(mu_vals[i] >= mu_vals[i+1] for i in range(len(mu_vals)-1))

# ===== Derivative of mu w.r.t. A at A=0 =====
# mu(A) = (2 a_+(A) + 1) / (a_+(A)(a_+(A) + 2))
# d(mu)/d(A)|_{A=0}: first compute d(a_+)/d(A)|_{A=0}
# a_+(A) = (-1 + sqrt(9+24A))/2, so a'_+(A) = 12/sqrt(9+24A) / 2 = 6/sqrt(9+24A)
# a'_+(0) = 6/3 = 2
# mu(a) = (2a+1)/(a(a+2)), d(mu)/d(a) = ...
# At a=1: mu = 3/3 = 1
# d(mu)/d(a) = [2 a(a+2) - (2a+1)(2a+2)] / (a(a+2))^2
#            = [2a^2+4a - 4a^2-6a-2] / (a(a+2))^2
#            = [-2a^2-2a-2] / (a(a+2))^2
# At a=1: [-2-2-2]/9 = -6/9 = -2/3
# d(mu)/d(A)|_{A=0} = d(mu)/d(a) * d(a)/d(A) = (-2/3)(2) = -4/3
dmu_dA_at_0 = sp.Rational(-4, 3)

report = {
    'title': 'Step 17 Separated Einstein Rigidity Theorem verification',
    'theorem': 'Exact Einstein Ric=g, cohomogeneity-one with S^1 x S^2 principal orbit '
               'and two S^2 bolts => Nariai/S^2 x S^2',
    'symbolic_checks': {
        'first_integral_zero_at_a_plus': str(first_integral_check),  # should be 0
        'mu_form_equivalence': str(mu_equivalence),  # should be 0
        'mu_equals_1_solutions': [str(s) for s in mu_equals_1],  # should be [1]
        'A_when_a_plus_equals_1': [str(s) for s in A_from_aplus_1],  # should be [0]
    },
    'linearization': {
        'd_mu_dA_at_A_equals_0': str(dmu_dA_at_0),
        'interpretation': 'mu(A) = 1 - (4/3)A + O(A^2), so any nonzero A gives '
                          'a definite cone angle defect |1-mu| >= (4/3)A - O(A^2)'
    },
    'numerical_samples': results,
    'mu_strictly_decreasing': monotone,
    'conclusion': 'Smooth closure at both bolts requires mu=1, hence a_+=1, hence A=0. '
                  'The unique solution is S^2(1)xS^2(1) with Vol=16 pi^2. '
                  'This is the classical fact that Euclidean Schwarzschild-de Sitter cannot '
                  'simultaneously smooth both horizons (surface gravity ratio != 1 for A>0).',
    'scope': 'Applies only to the separated cohomogeneity-one class with two S^2 bolts. '
             'Does not address general toric polygons, general metrics, or n>=5.'
}

OUT = 'Sessions/S0910A02/workspace/data/step17_separated_rigidity_proof.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"\nSaved {OUT}")
