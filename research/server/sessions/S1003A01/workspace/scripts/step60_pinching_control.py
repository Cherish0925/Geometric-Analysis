"""Step 60: Weyl-pinching control on the explicit Bianchi-VIII AKE pair.

Checks, exactly in p (1/3<p<1), with s=-12 and W+ eigenvalues w_i on omega_i
(curvature-operator normalization, |omega_i|^2=2):
  (a) Weitzenbock trace identity <W+ Omega,Omega> = s/3 + q/2, i.e.
      2(X1 w1 + X2 w2) = -4 + q/2;
  (b) lambda_min(W+) - s/6 > 0 on the open interval, tending to 0 only at p->1;
  (c) |W+|^2 - s^2/24 < 0 on the open interval (strict pinching at every finite point),
      with equality only in the limit p->1 (the infinite end, q->0).
Root counts: sympy Poly.count_roots(a,b) counts the CLOSED interval; open_count() below
removes endpoint roots, so the labels '(1/3,1)' now mean the open interval.
Output: workspace/data/step60/pinching_control.json
"""
import json, os
import sympy as sp

p = sp.symbols('p', positive=True)
D = 1 + 3*p**2
w1 = -4*(9*p**6 - 18*p**5 - 9*p**4 - 6*p**3 + 9*p**2 - 1)/D**3
w2 = -4*(9*p**6 + 18*p**5 - 9*p**4 + 6*p**3 + 9*p**2 - 1)/D**3
w3 = 8*(9*p**6 - 9*p**4 + 9*p**2 - 1)/D**3
X1 = (1 - p)**3*(3*p + 1)/(16*p**3)
X2 = (1 + p)**3*(3*p - 1)/(16*p**3)
q = 36*(1 - p**2)**3/D**3
s = -12

def open_count(num, a, b):
    P = sp.Poly(num, p)
    c = P.count_roots(a, b)
    for e in (a, b):
        if P.eval(e) == 0:
            c -= P.count_roots(e, e)
    return c

out = {}
out['trace_zero'] = str(sp.simplify(w1 + w2 + w3))
out['X1+X2-1'] = str(sp.simplify(X1 + X2 - 1))
lhs = 2*(X1*w1 + X2*w2)
out['weitzenbock_residual'] = str(sp.factor(sp.simplify(lhs - (sp.Rational(s, 3) + q/2))))

# eigenvalue gaps above s/6 = -2
gaps = {}
for name, w in (('w1', w1), ('w2', w2), ('w3', w3)):
    g = sp.factor(sp.simplify(w + 2))
    gaps[name] = str(g)
out['eigen_minus_s_over_6'] = gaps
# minimal eigenvalue: numerically identify which is smallest on a grid, plus exact
# sign analysis of numerator of w2+2 on (1/3,1)
for name, w in (('w1', w1), ('w2', w2), ('w3', w3)):
    num = sp.numer(sp.factor(w + 2))
    # exact count of real roots of the numerator in the open interval (1/3,1)
    out[name + '+2_roots_in_open_(1/3,1)'] = open_count(num, sp.Rational(1, 3), 1)
    out[name + '+2_roots_in_closed_[1/3,1]'] = sp.Poly(num, p).count_roots(sp.Rational(1, 3), 1)
    out[name + '+2_numerator'] = str(sp.factor(num))
    out[name + '+2_at_p=1/2'] = str((w + 2).subs(p, sp.Rational(1, 2)))
grid = [sp.Rational(1, 3) + sp.Rational(k, 300)*sp.Rational(2, 3) for k in range(1, 300)]
mins = []
for x in grid:
    vals = [float(w.subs(p, x)) for w in (w1, w2, w3)]
    mins.append(min(vals))
out['lambda_min_minus_s6_grid_min'] = min(m + 2 for m in mins)
out['lambda_min_at_bolt'] = [str(sp.nsimplify(w.subs(p, sp.Rational(1, 3)))) for w in (w1, w2, w3)]
out['lambda_at_infinity'] = [str(sp.limit(w, p, 1)) for w in (w1, w2, w3)]
W2norm = sp.simplify(w1**2 + w2**2 + w3**2)
pin = sp.factor(sp.simplify(W2norm - sp.Rational(s**2, 24)))
out['|W+|^2 - s^2/24'] = str(pin)
out['|W+|^2_bolt'] = str(sp.simplify(W2norm.subs(p, sp.Rational(1, 3))))
out['pinching_sign_grid'] = [float(pin.subs(p, x)) for x in grid[::30]]
out['pinching_numerator_roots_in_open_(1/3,1)'] = open_count(sp.numer(pin), sp.Rational(1, 3), 1)
out['pinching_numerator_roots_in_closed_[1/3,1]'] = sp.Poly(sp.numer(pin), p).count_roots(sp.Rational(1, 3), 1)
os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'data', 'step60'), exist_ok=True)
path = os.path.join(os.path.dirname(__file__), '..', 'data', 'step60', 'pinching_control.json')
with open(path, 'w') as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
