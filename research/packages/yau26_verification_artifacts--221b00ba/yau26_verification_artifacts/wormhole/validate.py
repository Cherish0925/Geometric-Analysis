# Validation: Gaussian-normal evolution from a wavy torus t=f(z) inside the exact hyperbolic cusp
# g = dt^2 + e^{2t}(dz^2+dx^2+dy^2).  Exact Einstein, so constraints must stay ~0 and the evolved
# metric must have H -> 3 etc.
import numpy as np, sys
from evolve import T2Evolver
from throat import evolve, diagnose
N=int(sys.argv[1]); amp=float(sys.argv[2]); rmax=float(sys.argv[3])
kcut=float(sys.argv[4]) if len(sys.argv)>4 else None
ev=T2Evolver(N=N,kcut=kcut)
z=ev.z
f=amp*np.cos(z); fz=ev.dz(f); fzz=ev.dz(fz)
E=np.exp(2*f)
W=np.sqrt(1+fz**2/E)            # |grad(t-f)| = sqrt(1+e^{-2f} f'^2)
# induced metric on graph (coords z,x,y)
q=np.zeros((3,3,N)); q[0,0]=E+fz**2; q[1,1]=E; q[2,2]=E
# second fundamental form w.r.t. upward unit normal nu = grad(t-f)/W :  K = Hess(t-f)|_T / W
# Hessian of u=t-f(z) in metric dt^2+e^{2t}(dz^2+...): Gamma^t_{zz}=-e^{2t}, Gamma^z_{tz}=1
# Hess u(d_a,d_b)= d_a d_b u - Gamma^c_ab d_c u ; u_t=1,u_z=-f'
# tangent vectors: e_z = d_z + f' d_t , e_x=d_x, e_y=d_y
# Hess(tt)=0 ; Hess(tz)= -Gamma^z_{tz} u_z = f' ; Hess(zz)= -f'' - Gamma^t_zz*1 = -f''+e^{2t}; Hess(xx)=e^{2t}
Htt=0*z; Htz=fz; Hzz=-fzz+E; Hxx=E
K=np.zeros((3,3,N))
K[0,0]=(Hzz+2*fz*Htz+fz**2*Htt)/W
K[1,1]=Hxx/W; K[2,2]=Hxx/W
qinv=np.linalg.inv(q.transpose(2,0,1)).transpose(1,2,0)
S=np.einsum('iln,ljn->ijn',qinv,K)
ham,H,S2,R=ev.constraints(q,S)
print('initial ham',np.max(np.abs(ham)),'H range',H.min(),H.max())
sol=evolve(ev,q,S,rmax=rmax)
print('status',sol.status,'r_final',sol.t[-1])
for row in diagnose(ev,sol):
    print('r=%.3f  H:[%.4f,%.4f]  eigS:[%.4f,%.4f]  ham=%.2e'%row)
