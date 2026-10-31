# Verify the explicit tail formula: g = dr^2 + e^{2r}(dz^2 + e^{v}dx^2 + e^{-v}dy^2), v=v(r,z)
import sympy as sp
r,z,x,y = sp.symbols('r z x y', real=True)
v = sp.Function('v')(r,z)
X=[r,z,x,y]
g = sp.diag(1, sp.exp(2*r), sp.exp(2*r+v), sp.exp(2*r-v))
ginv = g.inv()
n=4
Gam=[[[sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
Ric=sp.zeros(n,n)
for b in range(n):
    for c in range(n):
        val=0
        for a in range(n):
            val+=sp.diff(Gam[a][b][c],X[a])-sp.diff(Gam[a][b][a],X[c])
            for d in range(n):
                val+=Gam[a][a][d]*Gam[d][b][c]-Gam[a][c][d]*Gam[d][b][a]
        Ric[b,c]=sp.simplify(val)
E = sp.simplify(Ric+3*g)
# orthonormal components
e = [1, sp.exp(-r), sp.exp(-r-v/2), sp.exp(-r+v/2)]
EON = sp.Matrix(4,4, lambda i,j: sp.simplify(E[i,j]*e[i]*e[j]))
print(EON)
Dv = sp.diff(v,r,2)+3*sp.diff(v,r)+sp.exp(-2*r)*sp.diff(v,z,2)
print('E_x + Dv/2 =', sp.simplify(EON[2,2]+Dv/2), '  E_y - Dv/2 =', sp.simplify(EON[3,3]-Dv/2))
print('E_rr + v_r^2/2 =', sp.simplify(EON[0,0]+sp.diff(v,r)**2/2), ' E_zz + e^{-2r} v_z^2/2 =', sp.simplify(EON[1,1]+sp.exp(-2*r)*sp.diff(v,z)**2/2), ' E_rz + e^{-r} v_r v_z/2 =', sp.simplify(EON[0,1]+sp.exp(-r)*sp.diff(v,r)*sp.diff(v,z)/2))
