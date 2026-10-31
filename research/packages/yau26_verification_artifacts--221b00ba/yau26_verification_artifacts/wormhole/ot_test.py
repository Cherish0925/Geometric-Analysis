import numpy as np, sys
from scipy.optimize import brentq
from evolve import T2Evolver
from throat import evolve, diagnose

def hill(ev,beta,ell0,m):
    z=ev.z; N=ev.N
    v=beta*np.cos(m*z); vs=ev.dz(v)/ell0
    pot=9/4-3/16*vs**2
    k=ev.k/ell0
    D2=np.real(np.fft.ifft(-(k**2)[:,None]*np.fft.fft(np.eye(N),axis=0),axis=0))
    Hm=-D2+np.diag(pot); Hm=0.5*(Hm+Hm.T)
    ev_,evec=np.linalg.eigh(Hm)
    psi=evec[:,0]; psi*=np.sign(psi.sum())
    return ev_[0],psi,v

N=int(sys.argv[1]); ell0=float(sys.argv[2]); m=int(sys.argv[3]); rmax=float(sys.argv[4])
ev=T2Evolver(N=N)
bc=brentq(lambda b: hill(ev,b,ell0,m)[0],0.5,40.0,xtol=1e-13)
lam,psi,v=hill(ev,bc,ell0,m)
print('critical beta=',bc,'lambda0=',lam,'psi min/max',psi.min(),psi.max())
sig=4/3*np.log(psi/psi.max())
q=np.zeros((3,3,N)); S=np.zeros((3,3,N))
q[0,0]=ell0**2; q[1,1]=np.exp(sig+v); q[2,2]=np.exp(sig-v)
ham,H,S2,R=ev.constraints(q,S)
print('initial ham violation',np.max(np.abs(ham)))
sol=evolve(ev,q,S,rmax=rmax)
print('status',sol.status,'r_final',sol.t[-1])
for row in diagnose(ev,sol):
    print('r=%.3f  H:[%.3f,%.3f]  eigS:[%.3f,%.3f]  ham=%.2e'%row)
