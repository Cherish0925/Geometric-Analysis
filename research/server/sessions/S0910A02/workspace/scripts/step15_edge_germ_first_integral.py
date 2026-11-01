"""
Step 15: exact first-integral for the separated boundary-bubble Einstein germ.

From the flexible formal series, a(r)=R(r) to high order.  Then the local model
becomes
    g = dr^2 + p(r)^2 dtheta^2 + a(r)^2 g_{S^2(kappa)},
    kappa = 1 + 2A,
where the shrinking rod/fixed sphere at r=0 has a(0)=1, a'(0)=0,
p(0)=0, p'(0)=1, and A=a''(0)>0.  The Einstein equations Ric=g imply
    a' = A p,
    2 a a'' + (a')^2 = kappa - a^2,
and hence the first integral
    a (a')^2 = kappa(a-1) - (a^3-1)/3.
The second zero of p occurs at a=a_+ satisfying a_+^2+a_+ +1 = 3kappa.
The slope there is
    |p'| = (2a_+ + 1)/(a_+(a_+ + 2)).
With the period normalized to make the first bolt smooth, smoothness at the
second parallel bolt would require |p'|=1; for A>0 it is <1, giving a cone/orbifold
angle in the separated two-bolt block.  This isolates a simple global obstruction
but does not by itself rule out polygonal boundary bubbling, where the cap can be
absorbed by nonseparated corner/gluing geometry.
"""
import json, math, os
import sympy as sp

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.abspath(os.path.join(HERE,'..','data'))
os.makedirs(DATA,exist_ok=True)

A=sp.symbols('A', positive=True)
a=sp.symbols('a', positive=True)
kappa=1+2*A
aplus=sp.simplify((-1+sp.sqrt(9+24*A))/2)
mu=sp.simplify((2*aplus+1)/(aplus*(aplus+2)))
# solve mu=1
# convert using aplus variable: mu=1 iff 2a+1=a(a+2), iff a^2=1.

samples=[]
for Aval in [0,0.01,0.1,0.5,1,4,9,16,36,100,400,10000]:
    if Aval==0:
        ap=1.0; muv=1.0
    else:
        ap=(-1+math.sqrt(9+24*Aval))/2
        muv=(2*ap+1)/(ap*(ap+2))
    samples.append({'A':Aval,'kappa':1+2*Aval,'a_plus':ap,'second_bolt_slope_abs':muv,
                    'cone_angle_if_first_bolt_period_2pi':2*math.pi*muv,
                    'orbifold_order_if_mu_inverse':(1/muv if muv>0 else None),
                    'rod_flux':2/(1+2*Aval)})

# compare formal coefficients from first integral by solving Taylor recursively for a and p=a'/A.
r=sp.symbols('r')
coeffs={k:sp.symbols(f'c{k}') for k in range(2,12,2)}
aser=1 + sum(coeffs[k]*r**k for k in coeffs)
expr=sp.series(2*aser*sp.diff(aser,r,2)+sp.diff(aser,r)**2 - (kappa-aser**2), r, 0, 10).removeO().expand()
sol={coeffs[2]:A/2}
records=[]
for powr in [2,4,6,8]:
    # coefficient r^powr solves c_{powr+2}
    var=coeffs.get(powr+2)
    eq=sp.simplify(expr.subs(sol).coeff(r,powr))
    if var is not None:
        s=sp.solve([eq],[var],dict=True)
        if s:
            sol[var]=sp.simplify(s[0][var])
            records.append({'power':powr,'solved':{str(var):str(sol[var])},'equation':str(eq)})
# p=a'/A, compare coefficients
pser=sp.series(sp.diff(aser.subs(sol),r)/A, r, 0, 10).removeO().expand()

report={
 'title':'Step 15 exact first-integral for separated edge Einstein germ',
 'equations':{
   'metric':'dr^2+p(r)^2 dtheta^2+a(r)^2 g_{S^2(kappa)}, kappa=1+2A',
   'relation':'a_prime=A p',
   'ODE':'2 a a_second + a_prime^2 = kappa - a^2',
   'first_integral':'a a_prime^2 = kappa(a-1) - (a^3-1)/3',
   'a_plus':'(-1+sqrt(9+24A))/2',
   'second_bolt_slope_abs':'(2a_plus+1)/(a_plus(a_plus+2))'
 },
 'samples':samples,
 'taylor_a_coefficients':{str(k):str(sp.factor(v)) for k,v in sol.items()},
 'taylor_p_from_a_prime_over_A':str(sp.factor(pser)),
 'finding':('The large-negative-edge-curvature germ is an exact local Einstein warped-product germ for every A>0, but the simplest separated block develops a second parallel collapsing circle with slope mu<1 once the first bolt period is made smooth. Thus the formal edge bubble is locally allowed but globally wants a cone/orbifold unless nonseparated polygon/corner geometry or a gluing construction absorbs the mismatch. This strongly supports the boundary-bubble/Biquard-obstruction framing.'),
 'caution':'This is a cohomogeneity-one separated cap, not a proof that all toric boundary bubbles are conical and not a closed pinched counterexample.'
}
OUT=os.path.join(DATA,'step15_edge_germ_first_integral.json')
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps({
 'samples':samples,
 'taylor_a_coefficients':report['taylor_a_coefficients'],
 'taylor_p':report['taylor_p_from_a_prime_over_A'],
 'finding':report['finding'],
 'saved':OUT},indent=2))
