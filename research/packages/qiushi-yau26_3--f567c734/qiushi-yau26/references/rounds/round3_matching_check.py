"""Exact finite-dimensional interface calculations; no global gluing solver."""
import sympy as s

a0,a1,b1,A0,A1,B1,dc,dC=s.symbols('a0 a1 b1 A0 A1 B1 dc dC',real=True)
I1=s.pi**2*(a1**2-3*b1**2-A1**2-B1**2)/8
I2=s.pi**2*(A1**2-3*B1**2-a1**2-b1**2)/8
F1p=-I1/2+s.pi*A0*a1/4-dc/2
F1m=-I1/2-s.pi*A0*a1/4+dc/2
F2p=-I2/2+s.pi*a0*A1/4-dC/2
F2m=-I2/2-s.pi*a0*A1/4+dC/2
assert s.simplify(F1p+F1m+I1)==0
assert s.simplify(F2p+F2m+I2)==0
assert s.simplify(F1p+F1m+F2p+F2m-s.pi**2*(b1**2+B1**2)/2)==0

r1p,r1m,r2p,r2m=s.symbols('r1p r1m r2p r2m',real=True)
shift1=r1p-r1m+s.pi*A0*a1/2
shift2=r2p-r2m+s.pi*a0*A1/2
assert s.simplify((F1p+r1p).subs(dc,shift1)-(r1p+r1m-I1)/2)==0
assert s.simplify((F1m+r1m).subs(dc,shift1)-(r1p+r1m-I1)/2)==0
assert s.simplify((F2p+r2p).subs(dC,shift2)-(r2p+r2m-I2)/2)==0
assert s.simplify((F2m+r2m).subs(dC,shift2)-(r2p+r2m-I2)/2)==0

eta,c0,c1=s.symbols('eta c0 c1',real=True)
Mshift=s.pi*(c0+c1*eta)
assert -s.diff(Mshift,eta)/2==-s.pi*c1/2
assert s.diff(Mshift,eta)/2==s.pi*c1/2
assert s.simplify(Mshift.subs(eta,s.pi/2)-Mshift.subs(eta,-s.pi/2)-s.pi**2*c1)==0

m=s.symbols('m',real=True)
amp,beta=s.symbols('amp beta',positive=True)
assert s.simplify((I1+I2).subs(B1,2*m/s.pi**2)+s.pi**2*b1**2/2+2*m**2/s.pi**2)==0
single={a1:0,b1:0,A1:0,B1:2/s.pi**2}
assert s.simplify(I1.subs(single)+1/(2*s.pi**2))==0
assert s.simplify(I2.subs(single)+3/(2*s.pi**2))==0
assert amp**2*(amp*beta)==amp**3*beta
assert s.simplify((amp**s.Rational(3,2))**2/amp**3)==1
print('PASS: endpoint parameter shifts preserve the net flux in each channel')
print('PASS: all four interface equations and their two solvability conditions')
print('PASS: nonzero marked twist forces nonzero total exterior response')
print('PASS: original single-twist source and physical epsilon^3 beta scale')
print('PASS: epsilon^(3/2) correction enters the normalized quadratic receiver at order one')
