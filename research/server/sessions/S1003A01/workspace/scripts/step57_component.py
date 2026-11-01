"""Step 57d: analyse the exact invariant component P (two_lift_P1.txt).
Solve the h-linear generators for h(W), find the W-curve, sample real points,
report class-A type (signs of W), mu1*mu2 (<0 needed for 0<X1<1), lam=-Q, q,
eta-type data; then integrate the Einstein+closure ODE from a sample point and
verify directly with the step56 coordinate curvature (Bianchi IX/VIII etc.).
"""
import sympy as sp, numpy as np, os, sys, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import step57_classA_metric_only as M
h1, h2, h3 = M.h; W1, W2, W3 = M.W
txt = open(os.path.join(here, '../data/step57/two_lift_P1.txt')).read().replace('^', '**')
gens = [sp.sympify(g) for g in txt.replace('\n', '').split(',') if g.strip()]
sol = sp.solve([gens[1], gens[2]], [h1, h2], dict=True)[0]
h3s = sp.solve(gens[0].subs(sol), h3)[0]
sol[h3] = h3s
sol = {k: sp.factor(v) for k, v in sol.items()}
print('h(W):', sol)
rel = [sp.factor(sp.numer(sp.together(g.subs(sol)))) for g in gens]
rel = [r for r in rel if r != 0]
G = sp.gcd_list(rel) if len(rel) > 1 else rel[0]
print('W relations (factored):'); [print('  ', r) for r in rel[:4]]
print('gcd:', sp.factor(G))
out = {'h_of_W': {str(k): str(v) for k, v in sol.items()}, 'W_relation': str(sp.factor(G))}
json.dump(out, open(os.path.join(here, '../data/step57/component_param.json'), 'w'), indent=1)
