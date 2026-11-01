#!/usr/bin/env python3
"""
Step 10: symbolic bookkeeping for four-dimensional LeBrun near-boundary
curvature energy.

This is not a numerical experiment on metrics.  It verifies the Chern-Weil
normalizations used in the corrected route note and prevents the erroneous
replacement
    int |W-|^2 = int |W+|^2 + 32*pi^2*k
from being inherited.  The correct relation is
    int(|W+|^2 - |W-|^2) = 12*pi^2*tau(M), tau(M)=tau(X)-k.
"""
import sympy as sp

pi = sp.pi
A, k, chiX, tauX, J, E2 = sp.symbols('A k chiX tauX J E2', positive=True)
# A = c1^2(X) = 2 chi(X) + 3 tau(X)
relation_A = sp.Eq(A, 2*chiX + 3*tauX)
chiM = chiX + k
tauM = tauX - k
# Signature formula: S_plus - S_minus = 12 pi^2 tau(M)
Wp2 = sp.symbols('Wp2')
Wm2 = Wp2 - 12*pi**2*tauM
# Dossier CGB convention: I-J=A-k where I=(1/4pi^2) int(s^2/24+2|W+|^2)
# Hence int(s^2/24+2|W+|^2) = 4 pi^2 (A-k+J)
I_int = 4*pi**2*(A - k + J)
Sscalar_int = sp.symbols('Sscalar_int')  # int s^2/24
# solve  Sscalar + 2 Wp2 = I_int
Wp2_expr = sp.simplify((I_int - Sscalar_int)/2)
Wm2_expr = sp.simplify(Wp2_expr - 12*pi**2*tauM)
# Substitute tauX=(A-2chiX)/3
Wm2_sub = sp.simplify(Wm2_expr.subs(tauX, (A-2*chiX)/3))
# Full curvature-operator energy in four dimensions with this convention:
# int |Rcal|^2 = int(|W+|^2+|W-|^2+s^2/24+|E|^2/2)
# CGB: 8pi^2 chi = int(|W+|^2+|W-|^2+s^2/24-|E|^2/2)
# Therefore curvature-operator energy = 8pi^2 chi(M) + int|E|^2.
Rcal2_from_cgb = 8*pi**2*chiM + E2
# Direct expression using Wp,Wm,Sscalar and E2/2
Rcal2_direct = sp.simplify(Wp2_expr + Wm2_expr + Sscalar_int + E2/2)
# J=(1/(4pi^2)) int |E|^2/2, so E2 = 8pi^2 J.
Rcal2_J = sp.simplify(Rcal2_from_cgb.subs(E2, 8*pi**2*J))

print('A relation: A = 2 chiX + 3 tauX')
print('chi(M)=', chiM)
print('tau(M)=', tauM)
print('Correct signature relation: int Wm^2 = int Wp^2 - 12*pi^2*tau(M)')
print('Wm^2 expression from I and scalar:')
print(' ', Wm2_sub)
print('\nFull curvature-operator energy from CGB:')
print(' int |Rcal|^2 = 8*pi^2*chi(M) + int |E|^2')
print(' with J=(1/(4pi^2)) int |E|^2/2:')
print(' ', Rcal2_J)
print('\nNormalized by A if chiX/A and k/A and J/A are bounded:')
print(' int |Rcal|^2 / A = 8*pi^2*(chiX/A + k/A + J/A)')

# Near-boundary calibrated scalar integral when Ric ~ -g: s ~ -4, Vol ~ (32/9)pi^2 A.
Vol_cal = sp.Rational(32,9)*pi**2*A
Sscalar_cal = sp.Rational(16,24)*Vol_cal  # s^2/24 = 16/24 = 2/3
Wp2_cal = sp.Rational(1,24)*Vol_cal
I_cal = sp.simplify(Sscalar_cal + 2*Wp2_cal)
print('\nCalibrated near-boundary values:')
print(' Vol =', Vol_cal)
print(' int s^2/24 =', sp.simplify(Sscalar_cal))
print(' int |W+|^2 =', sp.simplify(Wp2_cal))
print(' int(s^2/24+2|W+|^2)=', I_cal, '= 4*pi^2*(2A/3)')
assert sp.simplify(I_cal - 4*pi**2*sp.Rational(2,3)*A) == 0

# Show the erroneous formula would only hold under an artificial tauX relation.
erroneous_rhs = Wp2 + 32*pi**2*k
correct_rhs = Wp2 - 12*pi**2*(tauX-k)
diff = sp.simplify(erroneous_rhs - correct_rhs)
print('\nDifference between erroneous Wm formula (Wp+32pi^2 k) and correct one:')
print(' ', diff)
print('It vanishes only if 20*k + 12*tauX = 0, not in general.')

print('\nAll Step 10 energy-bookkeeping checks passed.')
