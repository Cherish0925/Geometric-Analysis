"""
Step 18 (S0910A02): finite-difference residual evaluator for diagonal polar
T^2-invariant metrics

  g = e^{2 phi(x,y)}(dx^2+dy^2) + p(x,y)^2 dtheta^2 + q(x,y)^2 dpsi^2.

It computes the normalized positive-branch Ricci endomorphism eigenvalue errors
away from degeneration boundary:
  delta = sup max(|r_p-1|, |r_q-1|, |eig(Ric^H)-1|).

This is a scaffold for the Step-18 toric crux, not a proof and not a full
smooth-polygon solver.  The calibration case S^2 x S^2 with phi=0,
p=sin x, q=sin y on (0,pi)^2 should have residual near zero in the interior.
"""
import json, math, os
import numpy as np

ROOT="Sessions/S0910A02"
OUT=os.path.join(ROOT,"workspace/data/step18_diagonal_toric_residual_calibration.json")

# ---------- finite differences on a uniform rectangle ----------
def derivatives(F, hx, hy):
    Fx=(F[2:,1:-1]-F[:-2,1:-1])/(2*hx)
    Fy=(F[1:-1,2:]-F[1:-1,:-2])/(2*hy)
    Fxx=(F[2:,1:-1]-2*F[1:-1,1:-1]+F[:-2,1:-1])/(hx*hx)
    Fyy=(F[1:-1,2:]-2*F[1:-1,1:-1]+F[1:-1,:-2])/(hy*hy)
    Fxy=(F[2:,2:]-F[2:,:-2]-F[:-2,2:]+F[:-2,:-2])/(4*hx*hy)
    return Fx,Fy,Fxx,Fxy,Fyy

def eval_residual(phi,p,q,Lx=math.pi,Ly=math.pi,margin=4):
    # arrays shape (Nx,Ny), including endpoints.  Evaluate after one derivative
    # layer, then optionally ignore margin layers for boundary robustness.
    Nx,Ny=phi.shape
    hx=Lx/(Nx-1); hy=Ly/(Ny-1)
    logp=np.log(p); logq=np.log(q); logw=logp+logq; v=logp-logq
    phix,phiy,phixx,phixy,phiyy=derivatives(phi,hx,hy)
    lpx,lpy,lpxx,lpxy,lpyy=derivatives(logp,hx,hy)
    lqx,lqy,lqxx,lqxy,lqyy=derivatives(logq,hx,hy)
    Lx1,Ly1,Lxx,Lxy,Lyy=derivatives(logw,hx,hy)
    vx,vy,vxx,vxy,vyy=derivatives(v,hx,hy)
    ph=phi[1:-1,1:-1]
    e2inv=np.exp(-2*ph)
    # Scalar products and Laplacians in g_B=e^{2phi}delta. In dimension 2:
    # Delta_g f = e^{-2phi} Delta_E f.
    def inner(ax,ay,bx,by): return e2inv*(ax*bx+ay*by)
    def lap(fxx,fyy): return e2inv*(fxx+fyy)
    rp= -lap(lpxx,lpyy) - inner(lpx,lpy,lpx,lpy) - inner(lpx,lpy,lqx,lqy)
    rq= -lap(lqxx,lqyy) - inner(lqx,lqy,lqx,lqy) - inner(lpx,lpy,lqx,lqy)
    # Hessian in conformal coordinates: Hess_g f_ij = f_ij - Gamma^k_ij f_k.
    # Gamma^k_ij = delta^k_i phi_j + delta^k_j phi_i - delta_ij phi_k.
    def hess_components(fx,fy,fxx,fxy,fyy):
        Hxx=fxx - phix*fx + phiy*fy          # f_xx - phi_x f_x + phi_y f_y
        Hyy=fyy + phix*fx - phiy*fy          # f_yy + phi_x f_x - phi_y f_y
        Hxy=fxy - phiy*fx - phix*fy
        return Hxx,Hxy,Hyy
    HLxx,HLxy,HLyy=hess_components(Lx1,Ly1,Lxx,Lxy,Lyy)
    KB=-e2inv*(phixx+phiyy)
    # covariant 2-tensor bracket in Euclidean coordinate components
    Bxx=HLxx + 0.5*(Lx1*Lx1 + vx*vx)
    Byy=HLyy + 0.5*(Ly1*Ly1 + vy*vy)
    Bxy=HLxy + 0.5*(Lx1*Ly1 + vx*vy)
    # RicH_ij = K_B g_ij - B_ij; endomorphism = e^{-2phi} RicH matrix
    Axx=e2inv*(KB*np.exp(2*ph) - Bxx)
    Ayy=e2inv*(KB*np.exp(2*ph) - Byy)
    Axy=e2inv*(-Bxy)
    tr=Axx+Ayy
    disc=np.maximum(0.0,(Axx-Ayy)**2+4*Axy*Axy)
    eig1=0.5*(tr-np.sqrt(disc)); eig2=0.5*(tr+np.sqrt(disc))
    err=np.maximum.reduce([np.abs(rp-1),np.abs(rq-1),np.abs(eig1-1),np.abs(eig2-1)])
    # avoid boundary and derivative layers
    if margin>1:
        sl=(slice(margin-1,-(margin-1)), slice(margin-1,-(margin-1)))
        err_i=err[sl]; rp_i=rp[sl]; rq_i=rq[sl]; eig1_i=eig1[sl]; eig2_i=eig2[sl]
    else:
        err_i=err; rp_i=rp; rq_i=rq; eig1_i=eig1; eig2_i=eig2
    return {
        "N": [int(Nx),int(Ny)],
        "hx": hx, "hy": hy,
        "margin_grid_layers": margin,
        "delta_sup": float(np.nanmax(err_i)),
        "rp_range": [float(np.nanmin(rp_i)),float(np.nanmax(rp_i))],
        "rq_range": [float(np.nanmin(rq_i)),float(np.nanmax(rq_i))],
        "eigH_min_range": [float(np.nanmin(eig1_i)),float(np.nanmax(eig1_i))],
        "eigH_max_range": [float(np.nanmin(eig2_i)),float(np.nanmax(eig2_i))],
        "volume_proxy_4pi2_int_w": None,
    }

def product_case(N):
    xs=np.linspace(0,math.pi,N); ys=np.linspace(0,math.pi,N)
    X,Y=np.meshgrid(xs,ys,indexing='ij')
    phi=np.zeros_like(X)
    p=np.sin(X); q=np.sin(Y)
    # avoid log(0) in endpoints by setting tiny positive; boundaries are not evaluated.
    eps=1e-300
    p=np.maximum(p,eps); q=np.maximum(q,eps)
    rep=eval_residual(phi,p,q,margin=max(4,N//20))
    w=np.sin(X)*np.sin(Y)
    hx=math.pi/(N-1); hy=hx
    rep["volume_proxy_4pi2_int_w"] = float(4*math.pi**2*np.trapz(np.trapz(w,ys,axis=1),xs,axis=0))
    return rep

def product_analytic_check():
    return {
        "metric": "dx^2+dy^2+sin^2(x)dtheta^2+sin^2(y)dpsi^2",
        "rp": 1,
        "rq": 1,
        "horizontal_eigenvalues": [1,1],
        "volume": "4*pi^2*(int_0^pi sin x dx)^2 = 16*pi^2",
    }

reports={"analytic_product_check": product_analytic_check(), "fd_product_calibrations": {}}
for N in [65,129,257]:
    reports["fd_product_calibrations"][f"N{N}"]=product_case(N)

os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(reports,f,indent=2)
print(json.dumps(reports,indent=2))
print("Saved",OUT)
