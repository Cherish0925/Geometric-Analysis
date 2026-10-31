# Independent verification V1: biaxial Bianchi-IX Ricci tensor, Einstein family q_Lambda on O(-2),
# first-order core correction h~ on Eguchi-Hanson, its asymptotics H_*.
import sympy as sp

r,th,ph,ps,Lam = sp.symbols('r theta phi psi Lambda', real=True)
X = [r,th,ph,ps]

def ricci_of(gmat):
    n=4
    ginv = gmat.inv()
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Gam[a][b][c] = sp.simplify(sum(ginv[a,d]*(sp.diff(gmat[d,b],X[c])+sp.diff(gmat[d,c],X[b])-sp.diff(gmat[b,c],X[d])) for d in range(n))/2)
    Ric = sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            val = 0
            for a in range(n):
                val += sp.diff(Gam[a][b][c],X[a]) - sp.diff(Gam[a][b][a],X[c])
                for d in range(n):
                    val += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            Ric[b,c] = sp.simplify(val)
    return Ric

def biaxial_metric(Xf, Yf, Zf):
    # g = Xf dr^2 + Yf (dtheta^2 + sin^2 dphi^2) + Zf (dpsi + cos(theta) dphi)^2
    g = sp.zeros(4,4)
    g[0,0]=Xf
    g[1,1]=Yf
    g[2,2]=Yf*sp.sin(th)**2 + Zf*sp.cos(th)**2
    g[2,3]=g[3,2]=Zf*sp.cos(th)
    g[3,3]=Zf
    return g

# general functions
Xf = sp.Function('X')(r); Yf = sp.Function('Y')(r); Zf = sp.Function('Z')(r)
g = biaxial_metric(Xf,Yf,Zf)
Ric = ricci_of(g)
# orthonormal-frame eigenvalues: R0 = Ric_rr/X ; R1 = Ric_thth / Y ; R3 = Ric(e3,e3) with e3 = d/dpsi / sqrt(Z)
R0 = sp.simplify(Ric[0,0]/Xf)
R1 = sp.simplify(Ric[1,1]/Yf)
R3 = sp.simplify(Ric[3,3]/Zf)
# check that Ric is diagonal in the frame (dr, dtheta, sin dphi-part, sigma3): Ric - (R0 X dr^2 + R1 Y (..) + R3 Z sigma3^2) = 0
target = biaxial_metric(R0*Xf, R1*Yf, R3*Zf)
print('frame-diagonality residual:', sp.simplify(Ric-target))
import pickle
pickle.dump({'R0':R0,'R1':R1,'R3':R3}, open('biaxial_ricci.pkl','wb'))
print('R0=',R0); print('R1=',R1); print('R3=',R3)
