"""
Gauge comparison for mixed Ricci formula in the T^2 reduction.
Uses gauge A_x=0, A_y^I=f_I x to first order with variable f.
"""
import sympy as sp, json, os
n=4
h11x,h11y,h12x,h12y,h22x,h22y=sp.symbols('h11x h11y h12x h12y h22x h22y')
f1,f2,f1x,f1y,f2x,f2y=sp.symbols('f1 f2 f1x f1y f2x f2y')
dg=[[[sp.Integer(0) for j in range(n)] for i in range(n)] for a in range(n)]
ddg=[[[[sp.Integer(0) for j in range(n)] for i in range(n)] for b in range(n)] for a in range(n)]
# h first only enough for mixed Ric; second zero
for (a,i,j),v in {(0,2,2):h11x,(1,2,2):h11y,(0,2,3):h12x,(1,2,3):h12y,(0,3,3):h22x,(1,3,3):h22y}.items():
    dg[a][i][j]=v; dg[a][j][i]=v
# A_x=0; A_y^I=f_I x => at origin d_x A_y=f, d_xx A_y=f_x, d_xy A_y=f_y; others zero
dA1={(0,1,2):f1,(0,1,3):f2}
dA2={(0,0,1,2):f1x,(0,1,1,2):f1y,(1,0,1,2):f1y,
     (0,0,1,3):f2x,(0,1,1,3):f2y,(1,0,1,3):f2y}
for a in [0,1]:
    for b in [0,1]:
        for I in [2,3]:
            v=dA1.get((a,b,I),0); dg[a][b][I]=v; dg[a][I][b]=v
# A*A second base
for a in [0,1]:
 for d in [0,1]:
  for b in [0,1]:
   for c in [0,1]:
    val=0
    for I in [2,3]: val += dA1.get((a,b,I),0)*dA1.get((d,c,I),0)+dA1.get((d,b,I),0)*dA1.get((a,c,I),0)
    ddg[a][d][b][c]+=sp.simplify(val); ddg[a][d][c][b]=ddg[a][d][b][c]

def dh(a,I,J):
    if I>J: I,J=J,I
    return dg[a][I][J]
for a in [0,1]:
 for d in [0,1]:
  for b in [0,1]:
   for I in [2,3]:
    val=dA2.get((a,d,b,I),0)
    for J in [2,3]:
     val += dh(a,I,J)*dA1.get((d,b,J),0)+dh(d,I,J)*dA1.get((a,b,J),0)
    ddg[a][d][b][I]+=sp.simplify(val); ddg[a][d][I][b]=ddg[a][d][b][I]
# christoffels
Gamma=[[[0 for j in range(n)] for i in range(n)] for k in range(n)]
for k in range(n):
 for i in range(n):
  for j in range(n): Gamma[k][i][j]=sp.simplify(sp.Rational(1,2)*(dg[i][j][k]+dg[j][i][k]-dg[k][i][j]))
dGamma=[[[[0 for j in range(n)] for i in range(n)] for k in range(n)] for m in range(n)]
for m in range(n):
 for k in range(n):
  for i in range(n):
   for j in range(n):
    inv=0
    for l in range(n): inv += -dg[m][k][l]*(dg[i][j][l]+dg[j][i][l]-dg[l][i][j])
    der=ddg[m][i][j][k]+ddg[m][j][i][k]-ddg[m][k][i][j]
    dGamma[m][k][i][j]=sp.simplify(sp.Rational(1,2)*(inv+der))
Ric=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
 for j in range(n):
  term=0
  for k in range(n): term += dGamma[k][k][i][j]-dGamma[j][k][i][k]
  for k in range(n):
   for l in range(n): term += Gamma[k][i][j]*Gamma[l][k][l]-Gamma[l][i][k]*Gamma[k][j][l]
  Ric[i][j]=sp.factor(sp.simplify(term))
# C derivative as before
wx=sp.Rational(1,2)*(h11x+h22x); wy=sp.Rational(1,2)*(h11y+h22y)
C1x=sp.simplify(wx*f1+h11x*f1+f1x+h12x*f2); C1y=sp.simplify(wy*f1+h11y*f1+f1y+h12y*f2)
C2x=sp.simplify(wx*f2+h12x*f1+h22x*f2+f2x); C2y=sp.simplify(wy*f2+h12y*f1+h22y*f2+f2y)
exprs={
"Ric_x_theta":sp.factor(Ric[0][2]),"Ric_y_theta":sp.factor(Ric[1][2]),
"Ric_x_phi":sp.factor(Ric[0][3]),"Ric_y_phi":sp.factor(Ric[1][3]),
"half_C1y":sp.factor(sp.Rational(1,2)*C1y),"minus_half_C1x":sp.factor(-sp.Rational(1,2)*C1x),
"half_C2y":sp.factor(sp.Rational(1,2)*C2y),"minus_half_C2x":sp.factor(-sp.Rational(1,2)*C2x),
"diff_x_theta":sp.factor(Ric[0][2]-sp.Rational(1,2)*C1y),
"diff_y_theta":sp.factor(Ric[1][2]+sp.Rational(1,2)*C1x),
"diff_x_phi":sp.factor(Ric[0][3]-sp.Rational(1,2)*C2y),
"diff_y_phi":sp.factor(Ric[1][3]+sp.Rational(1,2)*C2x)}
for k,v in exprs.items(): print(k,"=",v)
OUTDIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data")); os.makedirs(OUTDIR,exist_ok=True)
with open(os.path.join(OUTDIR,"step12_toric_mixed_gauge_compare.json"),"w") as f: json.dump({k:str(v) for k,v in exprs.items()},f,indent=2)
