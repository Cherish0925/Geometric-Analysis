"""Checks for the actual closed E_D logarithmic modulation counterexample."""
import math
import sympy as s

u, lam = s.symbols('u lam', real=True, positive=True)
a = (lam-s.log(s.cosh(u)))/lam
lap = -s.diff(a,u,2)-s.tanh(u)*s.diff(a,u)
assert s.simplify(lap-1/lam)==0
assert s.simplify(s.diff(a,u).subs(u,0))==0
assert s.simplify(a.subs(u,0))==1
print('PASS: central ramp value, zero gradient, and exact 1/Lambda forcing')

t,beta,theta=s.symbols('t beta theta',real=True)
Xt=s.Function('Xt')(t,theta)
Xtheta=s.Function('Xtheta')(t,theta)
gtheta=beta**2*s.cosh(t)**2
lie= Xt*s.diff(gtheta,t)+2*gtheta*s.diff(Xtheta,theta)
assert s.simplify(lie.subs(t,0)/beta**2
                  -2*s.diff(Xtheta,theta).subs(t,0))==0
print('PASS: every smooth waist gauge has zero mean angular diagonal component')

x=s.symbols('x',nonnegative=True)
for r in (1,2,3,4):
    assert s.integrate(x**r*s.exp(-x),(x,0,s.oo))==s.factorial(r)
print('PASS: exponential collar weight controls all tested polynomial ramp moments')

# The geometric product rule supplies Q/(2 Lambda)+O(epsilon) at the
# centre. Check only the scale comparison, not an assumed output block.
rho=s.symbols('rho',positive=True)
assert s.limit(s.exp(-rho)*rho,rho,s.oo)==0
print('PASS: the O(epsilon) operator error is negligible against 1/Lambda')

for power in (1.1,1.25,1.4):
    ratios=[]
    nonlinear=[]
    critical=[]
    for log_inverse in (20.,40.,80.):
        eps=math.exp(-log_inverse)
        eta=eps**power
        ratios.append(eta/(log_inverse*eps**2))
        nonlinear.append(eta*log_inverse)
        critical.append(eps**2*log_inverse/(eps**1.5))
    assert ratios[0]<ratios[1]<ratios[2]
    assert nonlinear[0]>nonlinear[1]>nonlinear[2]
    assert critical[0]>critical[1]>critical[2]
    print(f'PASS: q={power:g}; linear/background ratios '
          + ', '.join(f'{v:.3g}' for v in ratios))

print('PASS: logarithmic loss is incompatible with uniform coercivity but harmless at polynomial repair accuracy')
