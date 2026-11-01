"""
Step 12 (S0910A02): symbolic local calculation for T^2-invariant 4-metrics.

Goal: verify the determinant/eigenfunction equation for the orbit-area density
w = sqrt(det h), where h is the metric on T^2 orbits, and determine what happens
when the horizontal distribution has curvature (twist/O'Neill terms).

We calculate at one point in a gauge with:
  - base coordinates x,y geodesic and orthonormal at the point,
  - fiber coordinates theta,phi with h(point)=I,
  - connection forms A^i vanish at the point but have curvature F^i_{xy}=f_i.

The full metric is
  g = g_B + h_ij (dy^i + A^i)(dy^j + A^j)
with base flat to first order for this vertical-trace calculation.  We encode the
first and second jets of h and the first jets of A, compute the Ricci tensor at the
point from the metric-jet formula, and compare h^{ij} Ric_ij with Delta_B w / w.

If Ric = lambda g, the vertical trace equals k lambda = 2 lambda.
"""
import sympy as sp
import json, os

# Coordinates: 0=x, 1=y, 2=theta, 3=phi
n = 4
x, y = 0, 1
th, ph = 2, 3

# First derivatives of h at the point h=I.
h11x,h11y,h12x,h12y,h22x,h22y = sp.symbols('h11x h11y h12x h12y h22x h22y')
# Second derivatives of h.
h11xx,h11xy,h11yy,h12xx,h12xy,h12yy,h22xx,h22xy,h22yy = sp.symbols(
    'h11xx h11xy h11yy h12xx h12xy h12yy h22xx h22xy h22yy')
# Connection curvatures F^theta_{xy}=f1, F^phi_{xy}=f2.
f1,f2 = sp.symbols('f1 f2')

# Metric value at point: identity.
g0 = sp.eye(n)

# First derivatives dg[a][i][j] = partial_a g_ij at point.
dg = [[[sp.Integer(0) for j in range(n)] for i in range(n)] for a in range(n)]
# Second derivatives ddg[a][b][i][j] = partial_a partial_b g_ij at point.
ddg = [[[[sp.Integer(0) for j in range(n)] for i in range(n)] for b in range(n)] for a in range(n)]

def set_sym(arr, *idx_val):
    *idx, val = idx_val
    a = arr
    for ii in idx[:-1]:
        a = a[ii]
    a[idx[-1]] = val

# h derivatives map for vertical components (2,2),(2,3),(3,3)
h_first = {
    (0,2,2): h11x, (1,2,2): h11y,
    (0,2,3): h12x, (1,2,3): h12y,
    (0,3,3): h22x, (1,3,3): h22y,
}
for (a,i,j), val in h_first.items():
    dg[a][i][j] = val
    dg[a][j][i] = val

h_second = {
    (0,0,2,2): h11xx, (0,1,2,2): h11xy, (1,0,2,2): h11xy, (1,1,2,2): h11yy,
    (0,0,2,3): h12xx, (0,1,2,3): h12xy, (1,0,2,3): h12xy, (1,1,2,3): h12yy,
    (0,0,3,3): h22xx, (0,1,3,3): h22xy, (1,0,3,3): h22xy, (1,1,3,3): h22yy,
}
for (a,b,i,j), val in h_second.items():
    ddg[a][b][i][j] = val
    ddg[a][b][j][i] = val

# Connection gauge: A^i_x = -1/2 f_i y, A^i_y = +1/2 f_i x.
# Since g_{a,vertical i}=h_{ij} A^j_a and h(point)=I, first derivatives are dA.
# d_a A^i_b values at origin.
dA = {}
# for vertical theta (2) curvature f1
dA[(1,0,2)] = -f1/2  # partial_y A_x^theta
dA[(0,1,2)] =  f1/2  # partial_x A_y^theta
# for vertical phi (3) curvature f2
dA[(1,0,3)] = -f2/2
dA[(0,1,3)] =  f2/2
# all other first derivatives zero
for a in [0,1]:
    for b in [0,1]:
        for I in [2,3]:
            val = dA.get((a,b,I), sp.Integer(0))
            dg[a][b][I] = val
            dg[a][I][b] = val

# Second derivatives of g_{bc} from A^i_b A^i_c terms at origin:
# partial_a partial_d sum_i A^i_b A^i_c = sum_i [(partial_a A^i_b)(partial_d A^i_c)+(partial_d A^i_b)(partial_a A^i_c)]
for a in [0,1]:
    for d in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                val = sp.Integer(0)
                for I in [2,3]:
                    val += dA.get((a,b,I), sp.Integer(0))*dA.get((d,c,I), sp.Integer(0))
                    val += dA.get((d,b,I), sp.Integer(0))*dA.get((a,c,I), sp.Integer(0))
                ddg[a][d][b][c] += sp.simplify(val)
                ddg[a][d][c][b] = ddg[a][d][b][c]

# Second derivatives of mixed g_{b,I}=h_{IJ}A^J_b from dh * dA terms at origin.
# partial_a partial_d g_{b,I} = (partial_a h_{I,J})(partial_d A^J_b)+(partial_d h_{I,J})(partial_a A^J_b)
# h at origin I,J = vertical labels 2,3.
def dh(a,I,J):
    if I>J: I,J=J,I
    return dg[a][I][J]

for a in [0,1]:
    for d in [0,1]:
        for b in [0,1]:
            for I in [2,3]:
                val = sp.Integer(0)
                for J in [2,3]:
                    val += dh(a,I,J)*dA.get((d,b,J), sp.Integer(0))
                    val += dh(d,I,J)*dA.get((a,b,J), sp.Integer(0))
                ddg[a][d][b][I] += sp.simplify(val)
                ddg[a][d][I][b] = ddg[a][d][b][I]

# Christoffel at point: Gamma[k][i][j]
Gamma = [[[sp.Integer(0) for j in range(n)] for i in range(n)] for k in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            val = sp.Rational(1,2)*(dg[i][j][k] + dg[j][i][k] - dg[k][i][j])
            Gamma[k][i][j] = sp.simplify(val)

# Derivative of Gamma: dGamma[m][k][i][j] = partial_m Gamma^k_{ij} at point.
# partial_m g^{kl} = - dg[m][k][l] since g=I.
dGamma = [[[[sp.Integer(0) for j in range(n)] for i in range(n)] for k in range(n)] for m in range(n)]
for m in range(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # derivative of inverse contribution
                inv_part = sp.Integer(0)
                for l in range(n):
                    inv_part += -dg[m][k][l] * (dg[i][j][l] + dg[j][i][l] - dg[l][i][j])
                # derivative of metric derivatives
                der_part = ddg[m][i][j][k] + ddg[m][j][i][k] - ddg[m][k][i][j]
                dGamma[m][k][i][j] = sp.simplify(sp.Rational(1,2)*(inv_part + der_part))

# Ricci tensor Ric_ij = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma^k_ij Gamma^l_kl - Gamma^l_ik Gamma^k_jl
Ric = [[sp.Integer(0) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        term = sp.Integer(0)
        for k in range(n):
            term += dGamma[k][k][i][j] - dGamma[j][k][i][k]
        for k in range(n):
            for l in range(n):
                term += Gamma[k][i][j]*Gamma[l][k][l] - Gamma[l][i][k]*Gamma[k][j][l]
        Ric[i][j] = sp.factor(sp.simplify(term))

Ric_vert_trace = sp.factor(sp.simplify(Ric[2][2] + Ric[3][3]))

# Compute Delta w/w at origin from h polynomial with same jets.
X,Y = sp.symbols('X Y')
h11 = 1 + h11x*X + h11y*Y + sp.Rational(1,2)*h11xx*X**2 + h11xy*X*Y + sp.Rational(1,2)*h11yy*Y**2
h12 =     h12x*X + h12y*Y + sp.Rational(1,2)*h12xx*X**2 + h12xy*X*Y + sp.Rational(1,2)*h12yy*Y**2
h22 = 1 + h22x*X + h22y*Y + sp.Rational(1,2)*h22xx*X**2 + h22xy*X*Y + sp.Rational(1,2)*h22yy*Y**2
w = sp.sqrt(h11*h22 - h12**2)
Delta_w = sp.diff(w,X,2).subs({X:0,Y:0}) + sp.diff(w,Y,2).subs({X:0,Y:0})
Delta_w = sp.factor(sp.simplify(Delta_w))
F_norm_sq = sp.factor(f1**2 + f2**2)  # at h=I, base ON, F_i has one component; convention to be inferred

combo_no_twist = sp.factor(sp.simplify(Ric_vert_trace + Delta_w))
combo_with_half = sp.factor(sp.simplify(Ric_vert_trace + Delta_w - sp.Rational(1,2)*F_norm_sq))
combo_with_quarter = sp.factor(sp.simplify(Ric_vert_trace + Delta_w - sp.Rational(1,4)*F_norm_sq))
combo_with_full = sp.factor(sp.simplify(Ric_vert_trace + Delta_w - F_norm_sq))

print("Vertical Ricci trace h^{ij}Ric_ij at h=I:")
print(Ric_vert_trace)
print("\nDelta_B w / w at h=I (w=1):")
print(Delta_w)
print("\nRic_vert_trace + Delta_w:")
print(combo_no_twist)
print("\nCompare twist coefficients:")
print("minus 1/2 |F|^2 ->", combo_with_half)
print("minus 1/4 |F|^2 ->", combo_with_quarter)
print("minus 1   |F|^2 ->", combo_with_full)

# Einstein implication with Ric=lambda g: vertical trace=2 lambda.
lambda_sym = sp.symbols('lambda')
# If Rv = -Delta_w + cF, then Delta_w = cF - 2 lambda.
# Determine c from combo_no_twist.

out = {
    "Ric_vert_trace": str(Ric_vert_trace),
    "Delta_w_at_point": str(Delta_w),
    "Ric_vert_trace_plus_Delta_w": str(combo_no_twist),
    "interpretation_h_equals_I": "h^{ij}Ric_ij = -Delta_B(sqrt(det h))/sqrt(det h) + (1/2)*(f1^2+f2^2) in this F-component convention" if combo_with_half==0 else "see expressions",
    "Einstein_lambda_implication": "Delta_B w = ((1/2)|F|^2_h - 2*lambda) w at a point in the gauge h=I, if the displayed half-coefficient vanishes exactly"
}
OUTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
os.makedirs(OUTDIR, exist_ok=True)
with open(os.path.join(OUTDIR, "step12_toric_vertical_trace_symbolic.json"), "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved", os.path.join(OUTDIR, "step12_toric_vertical_trace_symbolic.json"))
