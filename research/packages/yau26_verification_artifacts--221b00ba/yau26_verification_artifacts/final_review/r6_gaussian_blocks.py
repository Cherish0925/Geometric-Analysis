# Referee check of the three blocks of E=Ric+3g for g=dt^2+e^{2t} qtilde(t,.)  (thm:W, sec6)
# numeric assembly of Ricci from exact symbolic derivatives of the metric components
import sympy as sp, numpy as np, random
t,z,x,y=sp.symbols('t z x y',real=True)
co=[t,z,x,y]
qt=sp.Matrix([[2+sp.sin(z)*sp.exp(-2*t)+sp.cos(x)/5, sp.cos(z)*sp.exp(-t)/3, sp.sin(x+z)/7],
              [sp.cos(z)*sp.exp(-t)/3, 1+sp.cos(z+y)/(2*(1+t**2)), sp.sin(z)/4],
              [sp.sin(x+z)/7, sp.sin(z)/4, 2+sp.sin(z)*sp.tanh(t)+sp.cos(y)/9]])
def arrays(gm,co):
    n=gm.shape[0]; m=len(co)
    G=sp.lambdify(co,gm,'numpy')
    dG=sp.lambdify(co,[sp.diff(gm,c) for c in co],'numpy')
    ddG=sp.lambdify(co,[[sp.diff(gm,c,d) for d in co] for c in co],'numpy')
    return G,dG,ddG
def ricci_num(g,dg,ddg):
    # g[n,n], dg[e][n,n], ddg[e][f][n,n]; coordinates indexed same as metric indices
    n=g.shape[0]; gi=np.linalg.inv(g)
    dg=np.array(dg,dtype=float); ddg=np.array(ddg,dtype=float)   # dg[e,a,b]
    Gam=np.zeros((n,n,n)); 
    low=np.zeros((n,n,n))      # low[d,b,c]=1/2(d_b g_dc + d_c g_db - d_d g_bc)
    for d in range(n):
        for b in range(n):
            for c in range(n):
                low[d,b,c]=0.5*(dg[b,d,c]+dg[c,d,b]-dg[d,b,c])
    Gam=np.einsum('ad,dbc->abc',gi,low)
    dgi=np.array([-gi@dg[e]@gi for e in range(n)])   # dgi[e,a,d]
    dlow=np.zeros((n,n,n,n))   # dlow[e,d,b,c]
    for e in range(n):
        for d in range(n):
            for b in range(n):
                for c in range(n):
                    dlow[e,d,b,c]=0.5*(ddg[e,b,d,c]+ddg[e,c,d,b]-ddg[e,d,b,c])
    dGam=np.einsum('ead,dbc->eabc',dgi,low)+np.einsum('ad,edbc->eabc',gi,dlow)  # dGam[e,a,b,c]
    Ric=np.einsum('aabc->bc',dGam)-np.einsum('caba->bc',dGam)+np.einsum('aad,dbc->bc',Gam,Gam)-np.einsum('acd,dba->bc',Gam,Gam)
    return Ric,Gam
g4=sp.zeros(4); g4[0,0]=1; g4[1:,1:]=sp.exp(2*t)*qt
G4,dG4,ddG4=arrays(g4,co)
Q,dQ,ddQ=arrays(qt,co)
random.seed(11)
for trial in range(4):
    p=[random.uniform(0.2,1.5),random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]
    g=np.array(G4(*p),dtype=float); Ric4,_=ricci_num(g,dG4(*p),ddG4(*p))
    E=Ric4+3*g
    q=np.array(Q(*p),dtype=float); dq=np.array(dQ(*p),dtype=float); ddq=np.array(ddQ(*p),dtype=float)
    qi=np.linalg.inv(q)
    Ric3,Gam3=ricci_num(q,dq[1:],ddq[1:,1:])
    J=qi@dq[0]
    dJ=[-qi@dq[e]@qi@dq[0]+qi@ddq[e,0] for e in range(4)]      # derivative of J wrt coordinate e
    trJ=np.trace(J); trJ2=np.trace(J@J)
    Ett=-trJ-0.5*np.trace(dJ[0])-0.25*trJ2
    ET=np.exp(-2*p[0])*qi@Ric3-0.5*dJ[0]-1.5*J-0.5*trJ*np.eye(3)-0.25*trJ*J
    divJ=np.array([sum(dJ[j+1][j,i] for j in range(3))+sum(Gam3[j,j,k]*J[k,i] for j in range(3) for k in range(3))-sum(Gam3[k,j,i]*J[j,k] for j in range(3) for k in range(3)) for i in range(3)])
    dtr=np.array([np.trace(dJ[i+1]) for i in range(3)])
    Emix=0.5*(divJ-dtr)
    ETtrue=np.linalg.inv(g[1:,1:])@E[1:,1:]
    print("pt",np.round(p,3),"| E_tt resid %.2e"%abs(E[0,0]-Ett),"| E_T resid %.2e"%np.abs(ETtrue-ET).max(),"| E_mix resid %.2e"%np.abs(E[0,1:]-Emix).max(),"| sizes",round(abs(E[0,0]),3),round(np.abs(ETtrue).max(),3),round(np.abs(E[0,1:]).max(),4))
