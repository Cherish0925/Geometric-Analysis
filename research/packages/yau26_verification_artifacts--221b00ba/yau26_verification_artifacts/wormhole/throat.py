import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
from evolve import T2Evolver

def throat_data(ev, beta, ell0, c, m=1, w_init=1.0, verbose=False):
    """time-symmetric twisted throat: q0 = ell0^2 dz^2 + e^{sig}(e^{v}dxi1^2+e^{-v}dxi2^2), K_{z1}=c*ell0*e^{-sig}"""
    z=ev.z; N=ev.N
    v=beta*np.cos(m*z)
    vs=ev.dz(v)/ell0                      # derivative in arclength
    pot=9/4-3/16*vs**2
    def F(w):
        wss=ev.dz(ev.dz(w))/ell0**2
        return wss-pot*w-0.75*c**2*np.exp(-v)*w**(-3)
    # lowest periodic eigenvalue of Hill operator -d^2/ds^2 + pot
    k=ev.k/ell0
    D2=np.real(np.fft.ifft(-(k**2)[:,None]*np.fft.fft(np.eye(N),axis=0),axis=0))
    Hmat=-D2+np.diag(pot)
    lam0=np.min(np.linalg.eigvalsh(0.5*(Hmat+Hmat.T)))
    if c==0:
        return None,lam0
    if lam0>=0:
        return None,lam0
    # initial guess from the ground state of the Hill operator (bifurcation asymptotics)
    evals,evecs=np.linalg.eigh(0.5*(Hmat+Hmat.T))
    psi=evecs[:,0]; psi=psi*np.sign(psi.sum()); psi=np.abs(psi)+1e-12
    A4=3*c**2*np.sum(np.exp(-v)/psi**2)/(4*abs(lam0)*np.sum(psi**2))
    guess=A4**0.25*psi
    def Fu(u):
        w=np.exp(u)
        return F(w)/w
    sol=None
    for g in [guess, guess*0.7, guess*1.5, guess*0.4, guess*2.5]:
        usol,info,ier,msg=fsolve(Fu,np.log(g),full_output=True,xtol=1e-13,maxfev=20000)
        wsol=np.exp(usol)
        if ier==1 and np.max(np.abs(F(wsol)/wsol))<1e-9:
            sol=wsol; break
    if sol is None:
        return None,lam0
    sig=4/3*np.log(sol)
    q=np.zeros((3,3,N)); S=np.zeros((3,3,N))
    q[0,0]=ell0**2; q[1,1]=np.exp(sig+v); q[2,2]=np.exp(sig-v)
    kap=c*ell0*np.exp(-sig)
    # S^i_j = q^{il}K_lj ; K_{01}=K_{10}=kap
    S[0,1]=kap/q[0,0]; S[1,0]=kap/q[1,1]
    return (q,S,sig,v),lam0

def evolve(ev,q,S,rmax=8.0,rtol=1e-9,atol=1e-11):
    N=ev.N
    y0=np.concatenate([q.ravel(),S.ravel()])
    def blow(r,y):
        Sx=y[9*N:]
        return 50.0-np.max(np.abs(Sx))
    blow.terminal=True
    def degenerate(r,y):
        qx=y[:9*N].reshape(3,3,N)
        det=np.linalg.det(qx.transpose(2,0,1))
        return np.min(det)-1e-12
    degenerate.terminal=True
    sol=solve_ivp(ev.rhs,[0,rmax],y0,method='DOP853',rtol=rtol,atol=atol,events=[blow,degenerate],dense_output=False,max_step=0.02)
    return sol

def diagnose(ev,sol):
    N=ev.N
    out=[]
    for i in range(0,len(sol.t),max(1,len(sol.t)//12)):
        y=sol.y[:,i]; q=y[:9*N].reshape(3,3,N); S=y[9*N:].reshape(3,3,N)
        ham,H,S2,R=ev.constraints(q,S)
        eig=np.array([np.linalg.eigvals(S[:,:,n]).real for n in range(N)])
        out.append((sol.t[i],H.min(),H.max(),eig.min(),eig.max(),np.max(np.abs(ham))))
    return out

if __name__=='__main__':
    import sys
    ev=T2Evolver(N=48)
    beta=float(sys.argv[1]); ell0=float(sys.argv[2]); c=float(sys.argv[3]); m=int(sys.argv[4]) if len(sys.argv)>4 else 1
    data,lam0=throat_data(ev,beta,ell0,c,m=m)
    print('lambda0(Hill)=',lam0)
    if data is None:
        print('no throat data'); sys.exit()
    q,S,sig,v=data
    ham,H,S2,R=ev.constraints(q,S)
    print('initial constraint violation',np.max(np.abs(ham)),' sigma range',sig.min(),sig.max(),' Q range',S2.min(),S2.max())
    sol=evolve(ev,q,S)
    print('status',sol.status,'r_final',sol.t[-1],sol.message)
    for row in diagnose(ev,sol):
        print('r=%.3f  H:[%.3f,%.3f]  eigS:[%.3f,%.3f]  ham=%.2e'%row)
