"""
T^2-symmetric Einstein evolution in Gaussian gauge from a (twisted) reflection throat.
g = dr^2 + q_ij(r,z) dy^i dy^j,  y=(z, xi1, xi2), z periodic.  Ric = -3 g.
   dq/dr = 2 q S ,   dS/dr = q^{-1} Ric(q) + 3 I - (tr S) S
Constraints:  R_q = -6 + H^2 - |S|^2 ,  div K - dH = 0.
Exploratory shooting experiment (ill-posed Cauchy problem, low Fourier truncation + filter).
"""
import numpy as np
from scipy.integrate import solve_ivp

class T2Evolver:
    def __init__(self, N=48, period=2*np.pi, filt=36.0, kfrac=2/3, kcut=None):
        self.N=N; self.P=period
        self.z=np.arange(N)*period/N
        k=np.fft.fftfreq(N, d=period/N)*2*np.pi
        self.k=k
        kmax=np.max(np.abs(k))
        # exponential filter to tame the elliptic-Cauchy instability
        self.filter=np.exp(-filt*(np.abs(k)/kmax)**16)
        self.filter[np.abs(k)>kfrac*kmax]=0.0
        if kcut is not None:
            kk=np.abs(k)*period/(2*np.pi)
            self.filter=np.exp(-36.0*(kk/kcut)**12)
            self.filter[kk>kcut]=0.0
    def dz(self,f):
        return np.real(np.fft.ifft(1j*self.k*np.fft.fft(f,axis=-1),axis=-1))
    def smooth(self,f):
        return np.real(np.fft.ifft(self.filter*np.fft.fft(f,axis=-1),axis=-1))
    def ricci(self,q):
        """q: array (3,3,N) symmetric. returns Ric_ij (3,3,N) and qinv."""
        N=self.N
        qinv=np.linalg.inv(q.transpose(2,0,1)).transpose(1,2,0)
        dq=self.dz(q)                      # derivative w.r.t. z (index 0)
        # Christoffel Gamma^i_{jk} = 1/2 q^{il}( d_j q_{lk} + d_k q_{lj} - d_l q_{jk} ), only d_0 nonzero
        Dq=np.zeros((3,3,3,N))             # Dq[m,l,k] = d_m q_{lk}
        Dq[0]=dq
        T=Dq.transpose(1,0,2,3)+Dq.transpose(1,2,0,3)-Dq.transpose(0,1,2,3)   # T[l,j,k]= d_j q_lk + d_k q_lj - d_l q_jk
        T=np.zeros((3,3,3,N))
        for l in range(3):
            for j in range(3):
                for kk in range(3):
                    T[l,j,kk]=Dq[j,l,kk]+Dq[kk,l,j]-Dq[l,j,kk]
        Gam=0.5*np.einsum('iln,ljkn->ijkn',qinv,T)
        dGam0=self.dz(Gam)                 # d_0 Gamma^i_{jk}
        Ric=np.zeros((3,3,N))
        tr=np.einsum('iikn->kn',Gam)       # Gamma^i_{ik}
        dtr0=self.dz(tr)
        for j in range(3):
            for kk in range(3):
                val=dGam0[0,j,kk].copy()                       # d_i Gamma^i_jk  (only i=0)
                if j==0: val-=dtr0[kk]                         # - d_j Gamma^i_ik
                val+=np.einsum('ln,ln->n',tr,Gam[:,j,kk])      # Gamma^i_il Gamma^l_jk
                val-=np.einsum('iln,lin->n',Gam[:,j,:],Gam[:,:,kk]) # Gamma^i_jl Gamma^l_ik
                Ric[j,kk]=val
        Ric=0.5*(Ric+Ric.transpose(1,0,2))
        return Ric,qinv
    def rhs(self,r,y):
        N=self.N
        q=y[:9*N].reshape(3,3,N); S=y[9*N:].reshape(3,3,N)
        q=0.5*(q+q.transpose(1,0,2))
        q=self.smooth(q); S=self.smooth(S)
        Ric,qinv=self.ricci(q)
        Rs=np.einsum('iln,ljn->ijn',qinv,Ric)
        H=np.einsum('iin->n',S)
        dq=2*np.einsum('iln,ljn->ijn',q,S)
        dq=0.5*(dq+dq.transpose(1,0,2))
        dS=Rs+3*np.eye(3)[:,:,None]-H[None,None,:]*S
        dq=self.smooth(dq); dS=self.smooth(dS)
        return np.concatenate([dq.ravel(),dS.ravel()])
    def constraints(self,q,S):
        Ric,qinv=self.ricci(q)
        R=np.einsum('ijn,ijn->n',qinv,Ric)
        H=np.einsum('iin->n',S)
        S2=np.einsum('ijn,jin->n',S,S)
        ham=R+6-H**2+S2
        return ham,H,S2,R

def unit_test():
    ev=T2Evolver(N=64)
    z=ev.z
    a=0.3*np.sin(z); b=0.2*np.cos(2*z)+0.1*np.sin(z); c=-0.25*np.cos(z)
    q=np.zeros((3,3,ev.N)); q[0,0]=np.exp(2*a); q[1,1]=np.exp(2*b); q[2,2]=np.exp(2*c)
    Ric,qinv=ev.ricci(q)
    d=ev.dz
    az,bz,cz=d(a),d(b),d(c); bzz,czz=d(bz),d(cz)
    rz=-np.exp(-2*a)*(bzz+czz+bz**2+cz**2-az*(bz+cz))
    rx=-np.exp(-2*a)*(bzz+bz**2+bz*cz-az*bz)
    ry=-np.exp(-2*a)*(czz+cz**2+bz*cz-az*cz)
    print('diag test:',np.max(np.abs(Ric[0,0]*np.exp(-2*a)-rz)),np.max(np.abs(Ric[1,1]*np.exp(-2*b)-rx)),np.max(np.abs(Ric[2,2]*np.exp(-2*c)-ry)), 'offdiag',np.max(np.abs(Ric[0,1])),np.max(np.abs(Ric[1,2])))
    # shear test: xi1 -> xi1 + theta(z): scalar curvature invariant
    th=0.4*np.sin(z)+0.1*np.cos(3*z); thz=d(th)
    J=np.zeros((3,3,ev.N)); J[0,0]=1; J[1,1]=1; J[2,2]=1; J[1,0]=thz   # d(xi1+theta)= dxi1 + theta' dz
    q2=np.einsum('ain,abn,bjn->ijn',J,q,J)
    Ric2,qinv2=ev.ricci(q2)
    R1=np.einsum('ijn,ijn->n',qinv,Ric); R2=np.einsum('ijn,ijn->n',qinv2,Ric2)
    print('shear test (scalar curvature invariance):',np.max(np.abs(R1-R2)))

if __name__=='__main__':
    unit_test()
