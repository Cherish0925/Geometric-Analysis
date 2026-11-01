"""
Step 12: symbolic mixed Ricci calculation for T^2-invariant 4-metrics.

At a point with base geodesic ON, h=I, connection A=0, but connection curvature
F^I_{xy}=f_I has first derivatives f_{I,x}, f_{I,y}.  We compute Ric_{aI} and
compare with the standard reduced Einstein/Yang--Mills equation:

    d( w h_{IJ} *_B F^J ) = 0

where w=sqrt(det h).  In coordinates with orientation dx wedge dy and h=I,
*_B F^J = f_J, so the quantities C_I=w h_{IJ} f_J have derivatives involving
f gradients and h first derivatives.  Ric_{aI}=0 should be equivalent to the
C_I being constant (up to the Hodge rotation and a factor/sign).
"""
import sympy as sp
import json, os

n=4
# derivative symbols for h at point h=I
h11x,h11y,h12x,h12y,h22x,h22y = sp.symbols('h11x h11y h12x h12y h22x h22y')
h11xx,h11xy,h11yy,h12xx,h12xy,h12yy,h22xx,h22xy,h22yy = sp.symbols(
    'h11xx h11xy h11yy h12xx h12xy h12yy h22xx h22xy h22yy')
# curvature scalar components and gradients
f1,f2,f1x,f1y,f2x,f2y = sp.symbols('f1 f2 f1x f1y f2x f2y')

# first and second derivatives of metric at origin
dg=[[[sp.Integer(0) for j in range(n)] for i in range(n)] for a in range(n)]
ddg=[[[[sp.Integer(0) for j in range(n)] for i in range(n)] for b in range(n)] for a in range(n)]
# h derivatives
h_first={(0,2,2):h11x,(1,2,2):h11y,(0,2,3):h12x,(1,2,3):h12y,(0,3,3):h22x,(1,3,3):h22y}
for (a,i,j),v in h_first.items():
    dg[a][i][j]=v; dg[a][j][i]=v
h_second={(0,0,2,2):h11xx,(0,1,2,2):h11xy,(1,0,2,2):h11xy,(1,1,2,2):h11yy,
          (0,0,2,3):h12xx,(0,1,2,3):h12xy,(1,0,2,3):h12xy,(1,1,2,3):h12yy,
          (0,0,3,3):h22xx,(0,1,3,3):h22xy,(1,0,3,3):h22xy,(1,1,3,3):h22yy}
for (a,b,i,j),v in h_second.items():
    ddg[a][b][i][j]=v; ddg[a][b][j][i]=v

# A derivatives from gauge A_x^I=-1/2 f_I(x,y) y, A_y^I=1/2 f_I(x,y) x.
# dA1[a,b,I]=partial_a A_b^I at origin; b=0 x, b=1 y; I=2 theta, 3 phi.
dA1={}
dA2={}
for I, f, fx, fy in [(2,f1,f1x,f1y),(3,f2,f2x,f2y)]:
    dA1[(1,0,I)] = -f/2
    dA1[(0,1,I)] =  f/2
    # second derivatives partial_a partial_d A_b
    # A_x=-1/2 f y
    dA2[(0,0,0,I)] = 0
    dA2[(0,1,0,I)] = -fx/2
    dA2[(1,0,0,I)] = -fx/2
    dA2[(1,1,0,I)] = -fy
    # A_y=+1/2 f x
    dA2[(0,0,1,I)] = fx
    dA2[(0,1,1,I)] = fy/2
    dA2[(1,0,1,I)] = fy/2
    dA2[(1,1,1,I)] = 0

# First metric mixed derivatives g_{bI}=h_IJ A_b^J: at origin = dA.
for a in [0,1]:
    for b in [0,1]:
        for I in [2,3]:
            val=dA1.get((a,b,I),sp.Integer(0))
            dg[a][b][I]=val; dg[a][I][b]=val

# Second derivatives for base A*A term
for a in [0,1]:
  for d in [0,1]:
    for b in [0,1]:
      for c in [0,1]:
        val=0
        for I in [2,3]:
          val += dA1.get((a,b,I),0)*dA1.get((d,c,I),0)
          val += dA1.get((d,b,I),0)*dA1.get((a,c,I),0)
        ddg[a][d][b][c]+=sp.simplify(val)
        ddg[a][d][c][b]=ddg[a][d][b][c]

# helper dh
def dh(a,I,J):
    if I>J: I,J=J,I
    return dg[a][I][J]

# Second mixed g_{bI}=h_IJ A_b^J: h*d2A + dh*dA terms; h=I at origin.
for a in [0,1]:
  for d in [0,1]:
    for b in [0,1]:
      for I in [2,3]:
        val=dA2.get((a,d,b,I),0)  # h_IJ delta times second A^I
        for J in [2,3]:
          val += dh(a,I,J)*dA1.get((d,b,J),0)
          val += dh(d,I,J)*dA1.get((a,b,J),0)
        ddg[a][d][b][I]+=sp.simplify(val)
        ddg[a][d][I][b]=ddg[a][d][b][I]

# Christoffels and derivatives as before
Gamma=[[[sp.Integer(0) for j in range(n)] for i in range(n)] for k in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      Gamma[k][i][j]=sp.simplify(sp.Rational(1,2)*(dg[i][j][k]+dg[j][i][k]-dg[k][i][j]))

dGamma=[[[[sp.Integer(0) for j in range(n)] for i in range(n)] for k in range(n)] for m in range(n)]
for m in range(n):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        inv_part=0
        for l in range(n):
          inv_part += -dg[m][k][l]*(dg[i][j][l]+dg[j][i][l]-dg[l][i][j])
        der_part=ddg[m][i][j][k]+ddg[m][j][i][k]-ddg[m][k][i][j]
        dGamma[m][k][i][j]=sp.simplify(sp.Rational(1,2)*(inv_part+der_part))

Ric=[[sp.Integer(0) for j in range(n)] for i in range(n)]
for i in range(n):
  for j in range(n):
    term=0
    for k in range(n):
      term += dGamma[k][k][i][j]-dGamma[j][k][i][k]
    for k in range(n):
      for l in range(n):
        term += Gamma[k][i][j]*Gamma[l][k][l]-Gamma[l][i][k]*Gamma[k][j][l]
    Ric[i][j]=sp.factor(sp.simplify(term))

# C_I = w h_IJ f_J at h=I. w_x=1/2(h11x+h22x), w_y=1/2(h11y+h22y).
wx=sp.Rational(1,2)*(h11x+h22x)
wy=sp.Rational(1,2)*(h11y+h22y)
# C1 = w*(h11*f1+h12*f2); at origin h11=1,h12=0, derivatives:
C1x=sp.simplify(wx*f1 + h11x*f1 + f1x + h12x*f2)
C1y=sp.simplify(wy*f1 + h11y*f1 + f1y + h12y*f2)
# C2 = w*(h12*f1+h22*f2)
C2x=sp.simplify(wx*f2 + h12x*f1 + h22x*f2 + f2x)
C2y=sp.simplify(wy*f2 + h12y*f1 + h22y*f2 + f2y)

exprs={
  "Ric_x_theta": sp.factor(Ric[0][2]),
  "Ric_y_theta": sp.factor(Ric[1][2]),
  "Ric_x_phi": sp.factor(Ric[0][3]),
  "Ric_y_phi": sp.factor(Ric[1][3]),
  "C1x": sp.factor(C1x), "C1y": sp.factor(C1y),
  "C2x": sp.factor(C2x), "C2y": sp.factor(C2y),
  "Ric_x_theta_minus_half_C1y": sp.factor(sp.simplify(Ric[0][2]-sp.Rational(1,2)*C1y)),
  "Ric_y_theta_plus_half_C1x": sp.factor(sp.simplify(Ric[1][2]+sp.Rational(1,2)*C1x)),
  "Ric_x_phi_minus_half_C2y": sp.factor(sp.simplify(Ric[0][3]-sp.Rational(1,2)*C2y)),
  "Ric_y_phi_plus_half_C2x": sp.factor(sp.simplify(Ric[1][3]+sp.Rational(1,2)*C2x)),
}
for k,v in exprs.items():
    print(k, "=", v)

OUTDIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data"))
os.makedirs(OUTDIR,exist_ok=True)
with open(os.path.join(OUTDIR,"step12_toric_mixed_ricci_symbolic.json"),"w") as f:
    json.dump({k:str(v) for k,v in exprs.items()}, f, indent=2)
print("Saved", os.path.join(OUTDIR,"step12_toric_mixed_ricci_symbolic.json"))
