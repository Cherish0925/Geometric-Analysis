"""Frozen-symbol check for the reduced five-field Einstein--DeTurck boundary data.

Unknown amplitudes are (p,q,r,s,u)=(h_nn,h_nθ,h_θθ,h_xx,h_yy).
For a decaying interior mode exp(-k n+i xi θ), k=|xi|>0, impose at the
outer face: two tangential conformal-class conditions, mean curvature, and
the two nontrivial Bianchi components.  The determinant must be nonzero.
"""
import sympy as sp
from pathlib import Path
import json

k,xi=sp.symbols('k xi', positive=True, real=True)
p,q,r,s,u=sp.symbols('p q r s u')
vars=sp.Matrix([p,q,r,s,u])
I=sp.I
conds=sp.Matrix([
    r-s,
    r-u,
    -k*(r+s+u)/2-I*xi*q,
    k*p/2-k*(r+s+u)/2-I*xi*q,
    k*q+I*xi*(p-r+s+u)/2,
])
M=conds.jacobian(vars)
det=sp.factor(M.det())
det_char=sp.factor(det.subs(xi,k))
det_char_neg=sp.factor(det.subs(xi,-k))
print('boundary matrix =')
sp.print_latex(M)
print('det(k,xi) =',det)
print('det xi=+k =',det_char)
print('det xi=-k =',det_char_neg)

# Center parity is one scalar condition for each Laplace-type field:
# Neumann p,r,s,u and Dirichlet q.  Its frozen principal boundary matrix is diagonal.
center=sp.diag(-k,1,-k,-k,-k)
center_det=sp.factor(center.det())
print('center parity determinant =',center_det)

out={
 'outer_matrix':[[str(M[i,j]) for j in range(5)] for i in range(5)],
 'outer_det_general':str(det),
 'outer_det_xi_plus_k':str(det_char),
 'outer_det_xi_minus_k':str(det_char_neg),
 'center_parity_det':str(center_det),
 'interpretation':'Nonzero for k>0; this is a frozen principal-symbol calculation only, not nonlinear existence or invertibility.'
}
path=Path(__file__).resolve().parents[1]/'data'/'step71_reflection_boundary_symbol.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print('wrote',path)
