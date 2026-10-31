import sympy as sp
r = sp.symbols('r', positive=True)
W = 1-r**-4
Gdot = r**2/12 + 1/(4*r**2) - 1/(3*r**4)
# check ODE for Gdot
print('Gdot ODE residual:', sp.simplify(r*sp.diff(Gdot,r)+4*Gdot-(r**2/2+1/(2*r**2))), ' Gdot(1)=',Gdot.subs(r,1))
Fdot = -sp.Rational(1,2)*r**2*W + Gdot
# qdot components: coefficient of dr^2, of (s1^2+s2^2), of s3^2
qd_rr = -Fdot/W**2
qd_12 = 0
qd_33 = r**2*Gdot/4
v = sp.Rational(5,72)*(r**3-1/r)
L_rr = v*sp.diff(1/W,r) + 2*sp.diff(v,r)/W
L_12 = v*sp.diff(r**2/4,r)
L_33 = v*sp.diff(r**2*W/4,r)
h_rr = sp.simplify(qd_rr-L_rr); h_12 = sp.simplify(qd_12-L_12); h_33=sp.simplify(qd_33-L_33)
claim_rr = -r**2*(7*r**2-5)/(36*(r**2-1)*(r**2+1)**2)
claim_12 = -5*(r**4-1)/144
claim_33 = -r**4/72+sp.Rational(1,16)-r**-2/12+5*r**-4/144
print('rr diff:', sp.simplify(h_rr-claim_rr))
print('12 diff:', sp.simplify(h_12-claim_12))
print('33 diff:', sp.simplify(h_33-claim_33))
# asymptotics vs H_*: H_* = -5/36 (r^2 e - (x.dx)^2) + 1/12 <Jx,dx>^2 ; in polar: (r^2 e-(x dx)^2) = r^2 * r^2/4 (s1^2+s2^2+s3^2); <Jx,dx> = r^2/2 s3
Hs_12 = -sp.Rational(5,36)*r**4/4
Hs_33 = -sp.Rational(5,36)*r**4/4 + sp.Rational(1,12)*r**4/4
print('h_12 - H*_12 =', sp.simplify(h_12-Hs_12), '   (metric weight r^2/4 -> relative O(r^-2))')
print('h_33 - H*_33 =', sp.simplify(h_33-Hs_33))
print('h_rr series:', sp.series(h_rr, r, sp.oo, 6))
# norms relative to EH: |h - H*|_g components in ON frame
print('ON-frame deviations: rr:', sp.simplify(h_rr*W), ' 12:', sp.simplify((h_12-Hs_12)/(r**2/4)), ' 33:', sp.simplify((h_33-Hs_33)/(r**2*W/4)))
