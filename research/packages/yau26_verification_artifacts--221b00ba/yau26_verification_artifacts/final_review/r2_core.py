# Referee check of Lemma lem:core: D Ric_k(htilde) = k on Eguchi-Hanson, smoothness at the bolt, decay of htilde-H_*
import sympy as sp
rho,th,ph,ps,eps=sp.symbols('rho theta phi psi epsilon',real=True)
co=[rho,th,ph,ps]
def metric(X,Y,Z):
    g=sp.zeros(4)
    g[0,0]=X; g[1,1]=Y
    g[2,2]=Y*sp.sin(th)**2+Z*sp.cos(th)**2; g[2,3]=g[3,2]=Z*sp.cos(th); g[3,3]=Z
    return g
def ricci(g):
    gi=g.inv()
    Gam=[[[sum(gi[a,d]*(sp.diff(g[d,b],co[c])+sp.diff(g[d,c],co[b])-sp.diff(g[b,c],co[d])) for d in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric=sp.zeros(4)
    for b in range(4):
        for c in range(4):
            Ric[b,c]=sum(sp.diff(Gam[a][b][c],co[a]) for a in range(4))-sum(sp.diff(Gam[a][b][a],co[c]) for a in range(4))\
              +sum(Gam[a][a][d]*Gam[d][b][c] for a in range(4) for d in range(4))-sum(Gam[a][c][d]*Gam[d][b][a] for a in range(4) for d in range(4))
    return Ric
W=1-rho**-4
kX,kY,kZ=1/W,rho**2/4,rho**2*W/4
hX=-rho**2*(7*rho**2-5)/(36*(rho**2-1)*(rho**2+1)**2)
hY=-5*(rho**4-1)/144
hZ=-rho**4/72+sp.Rational(1,16)-1/(12*rho**2)+5/(144*rho**4)
g=metric(kX+eps*hX,kY+eps*hY,kZ+eps*hZ)
Ric=ricci(g)
R0=sp.simplify(Ric.subs(eps,0))
print("Ric(k)=0:",R0==sp.zeros(4))
D=sp.simplify(sp.diff(Ric,eps).subs(eps,0))
k=metric(kX,kY,kZ)
print("DRic_k(htilde)-k =",sp.simplify(D-k).tolist())
# smoothness at the bolt: s = geodesic distance, need h_ss and h_psipsi/(k_psipsi) to agree at rho=1 and all coefficient functions smooth in tau=rho-1
hss=sp.simplify(hX/kX)          # component along unit radial vector
h33=sp.simplify(hZ/kZ)          # component along unit sigma_3 vector
print("h(e_rho,e_rho) =",sp.factor(hss)," -> at bolt:",sp.limit(hss,rho,1))
print("h(e_3,e_3)   =",sp.factor(h33)," -> at bolt:",sp.limit(h33,rho,1))
# decay of htilde - H_* in the k-orthonormal frame
HsY=-5*rho**4/144; HsZ=-rho**4/72
print("frame comps of htilde-H_*:",sp.factor(sp.simplify(hX/kX)),",",sp.factor(sp.simplify((hY-HsY)/kY)),",",sp.factor(sp.simplify((hZ-HsZ)/kZ)))
# H_* from its Cartesian definition: -(5/36)(rho^2 e-(x.dx)^2)+(1/12)<Jx,dx>^2 with <Jx,dx>=rho^2 sigma_3/2
print("H_* sigma-components check:", sp.simplify(-sp.Rational(5,36)*rho**2*rho**2/4-HsY)==0, sp.simplify(-sp.Rational(5,36)*rho**4/4+sp.Rational(1,12)*rho**4/4-HsZ)==0)
