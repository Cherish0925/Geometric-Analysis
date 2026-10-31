"""Exact algebra for fixed_ratio.md; not a metric-realization certificate."""
import sympy as s

d, S, F, w, p, z, P, Q = s.symbols("d S F w p z P Q", positive=True)
quotient = (S+s.sqrt(6)*w)**2/(F+2*w*w)
w_star = s.sqrt(6)*F/(2*S)
assert s.simplify(quotient.subs(w, w_star)-(3+S*S/F)) == 0
assert s.simplify(s.diff(quotient, w).subs(w, w_star)) == 0
coordinate = (z*z+Q)/(z+P)**2
assert s.simplify(s.diff(coordinate,z)-2*(P*z-Q)/(z+P)**3) == 0
R1 = 3*d*d/(4*(2-d)**2)
R2 = d*d/4
R3 = 3*d*d/(4*(2+d)**2)
assert s.factor(R1-R3) == 6*d**3/((d-2)**2*(d+2)**2)
d0 = 2-s.sqrt(3)
assert s.simplify((R1-R2).subs(d,d0)) == 0
C_small = 9*(3-d*d)/(1-3*d*d)
C_large = 27*(1-d)/((1-2*d)*(1+d))
assert s.simplify(3+24/(1-12*R2)-C_small) == 0
assert s.simplify(3+24/(1-12*R1)-C_large) == 0
P_small = (1+5*d*d)/(3-d*d)
P_large = s.Rational(1,3)+4*d*d/(3*(1-d))
assert s.simplify(1-18/C_small-P_small) == 0
assert s.simplify(1-18/C_large-P_large) == 0
assert s.simplify(P_small.subs(d,d0)-(2*s.sqrt(3)-3)) == 0
assert s.simplify(P_small.subs(d,d0)-P_large.subs(d,d0)) == 0
inverse_small = s.sqrt((3*p-1)/(p+5))
inverse_large = (s.sqrt((3*p-1)*(3*p+15))-(3*p-1))/8
assert s.simplify(P_small.subs(d,inverse_small)-p) == 0
# Check the unsquared inverse equation to avoid hiding an extraneous root.
assert s.expand(4*inverse_large**2+(3*p-1)*inverse_large-(3*p-1)) == 0
old = s.Rational(1,3)+2*d*d/(1-d)**2
diff_small = 2*d*d*(1+16*d-11*d*d)/(3*(3-d*d)*(1-d)**2)
diff_large = 2*d*d*(1+2*d)/(3*(1-d)**2)
assert s.simplify(old-P_small-diff_small) == 0
assert s.simplify(old-P_large-diff_large) == 0
q=s.symbols("q",positive=True)
assert s.limit(inverse_small.subs(p,q+s.Rational(1,3))/s.sqrt(q),q,0) == s.Rational(3,4)
print("Exact fixed-ratio algebra checks passed.")
print("Defect-branch crossing:", s.N(d0,14))
print("Ratio-branch crossing:", s.N(2*s.sqrt(3)-3,14))
for ratio in [s.Rational(2,5), s.Rational(1,2), s.Rational(3,4), s.Rational(9,10)]:
    use_small = bool(ratio <= 2*s.sqrt(3)-3)
    new_gap = (inverse_small if use_small else inverse_large).subs(p,ratio)
    old_root = s.sqrt((ratio-s.Rational(1,3))/2)
    old_gap = old_root/(1+old_root)
    assert float(new_gap) > float(old_gap)
    print("p=",ratio,"new bound=",s.N(new_gap,10),"old bound=",s.N(old_gap,10))
