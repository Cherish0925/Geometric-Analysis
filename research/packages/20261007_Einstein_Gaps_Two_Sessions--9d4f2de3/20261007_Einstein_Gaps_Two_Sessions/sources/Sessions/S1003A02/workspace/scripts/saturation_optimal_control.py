"""Direct optimal-control test for the b-independent collapsed saturation problem.

State variables are the scale-free regularized diagonal Bianchi-IX variables
    x = beta-q/2 = log(F/G), z = exp(-q/3) = (C/G)^(1/3),
    p = r h', chi = r(beta'-q'/2), eta = r q',
with d tau = dt/r.  Controls are the scale-free traceless-Ricci combinations
(Hbar,Ebar,Dbar)=r^2(H,E,D).  The exact normalized action is
    int (3 Hbar^2/16 + Ebar^2/6 + Dbar^2/8) d tau.

The initial state is the finite-epsilon Lambda-Taub-NUT entry ray at area
coordinate A.  The terminal state is an exact complex-hyperbolic orbit at a
free CH radius t_ch.  This terminal condition is stronger than merely reaching
the standard-CR Einstein stable set, so the optimized value is a construction
upper bound for the collapsed-saturation value.

Usage:
  python saturation_optimal_control.py EPS N [warm_start.json] [ch|stable]
The ``ch`` terminal is an exact finite CH orbit.  The ``stable`` terminal uses
at zeta=10^-2 the Einstein constraint, zero linear unstable coordinate, and
zero corrected Rossi variable; it is a finite-section approximation to the
standard-CR Einstein stable set and is restricted to the verified q~0 block.
Output:
  workspace/data/saturation_control/eps<EPS>_N<N>_<mode>.json
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np
import casadi as ca

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "saturation_control"
OUT.mkdir(parents=True, exist_ok=True)


def potentials_symbolic(x, z):
    """Cancellation-controlled exact shape potentials (VD,Vx,VH)."""
    em4 = ca.exp(-4*x/3)
    ep2 = ca.exp(2*x/3)
    ep8 = ca.exp(8*x/3)
    zm4, z2, z8 = z**-4, z**2, z**8
    VD = 4*zm4*(em4-ep2) + 4*(ep2*z2-em4*z8)
    Vx = 4*zm4*(ep8-em4) + 4*z2*(em4-ep2)
    VH = (ca.Rational(2,3) if hasattr(ca, 'Rational') else 2/3)*zm4*(ep8-2*ep2+em4) \
         - (4/3)*z2*(ep2+em4) + (2/3)*em4*z8
    return VD, Vx, VH


def f_rhs(X, U):
    x, z, p, chi, eta = [X[i] for i in range(5)]
    Hb, Eb, Db = [U[i] for i in range(3)]
    VD, Vx, VH = potentials_symbolic(x, z)
    xi = chi + eta/2
    return ca.vertcat(
        chi,
        -eta*z/3,
        p*p - xi*xi/3 - eta*eta/4 + VH/2 - Hb/2,
        -2*p*chi + Vx - Eb + Db/2,
        -2*p*eta + VD - Db,
    )


def running_cost(U):
    return 3*U[0]**2/16 + U[1]**2/6 + U[2]**2/8


def entry_np(eps, A):
    z = eps**(1/3)
    U = math.sqrt(1+2*A*A)
    V = 2*A*A/U
    return np.array([0.0, z, z*(2*U+V)/3, 0.0, z*(U-V)], dtype=float)


def ch_np(t):
    s, c = math.sinh(t), math.cosh(t)
    r = s*c**(1/3)
    beta = math.log(c)
    p = r*(c/s + math.tanh(t)/3)
    xi = r*math.tanh(t)
    return np.array([beta, 1.0, p, xi, 0.0], dtype=float)


def entry_ca(eps, A):
    z = eps**(1/3)
    uu = ca.sqrt(1+2*A*A)
    vv = 2*A*A/uu
    return ca.vertcat(0, z, z*(2*uu+vv)/3, 0, z*(uu-vv))


def ch_ca(t):
    s, c = ca.sinh(t), ca.cosh(t)
    r = s*c**(1/3)
    return ca.vertcat(ca.log(c), 1, r*(c/s+ca.tanh(t)/3), r*ca.tanh(t), 0)


def bplus_np(X):
    """Normalized + chiral flux b_+=2-(sum u_i^2+u1u2u3)."""
    x, z, p, chi, eta = X
    q = -3*math.log(z)
    beta = x + q/2
    xi = chi + eta/2
    af = math.exp(2*beta/3)
    ag = math.exp(-beta/3+q/2)
    ah = math.exp(-beta/3-q/2)
    pf = af*(p+2*xi/3)
    pg = ag*(p-xi/3+eta/2)
    ph = ah*(p-xi/3-eta/2)
    gf = (ag*ag+ah*ah-af*af)/(ag*ah)
    gg = (ah*ah+af*af-ag*ag)/(ah*af)
    gh = (af*af+ag*ag-ah*ah)/(af*ag)
    u = np.array([pf-gf, pg-gg, ph-gh])
    return float(2-np.dot(u,u)-np.prod(u))


def bplus_ca(X):
    """CasADi transcription of bplus_np (normalized + chiral flux)."""
    x, z, p, chi, eta = [X[i] for i in range(5)]
    q = -3*ca.log(z)
    beta = x + q/2
    xi = chi + eta/2
    af = ca.exp(2*beta/3)
    ag = ca.exp(-beta/3+q/2)
    ah = ca.exp(-beta/3-q/2)
    pf = af*(p+2*xi/3)
    pg = ag*(p-xi/3+eta/2)
    ph = ah*(p-xi/3-eta/2)
    gf = (ag*ag+ah*ah-af*af)/(ag*ah)
    gg = (ah*ah+af*af-ag*ag)/(ah*af)
    gh = (af*af+ag*ag-ah*ah)/(af*ag)
    u1, u2, u3 = pf-gf, pg-gg, ph-gh
    return 2-(u1*u1+u2*u2+u3*u3)-u1*u2*u3


def hermite_guess(eps, N, A, tch, T):
    x0, x1 = entry_np(eps, A), ch_np(tch)
    # Cubic Hermite for x,z,p. Endpoint tau derivatives for x,z are chi and -eta*z/3.
    d0 = np.array([x0[3], -x0[4]*x0[1]/3, 0.0])
    d1 = np.array([x1[3], -x1[4]*x1[1]/3, 0.0])
    y0 = x0[[0,1,2]]; y1 = x1[[0,1,2]]
    X = np.zeros((5,N+1)); Uc = np.zeros((3,N+1))
    for k in range(N+1):
        s = k/N
        h00=2*s**3-3*s**2+1; h10=s**3-2*s**2+s
        h01=-2*s**3+3*s**2; h11=s**3-s**2
        hp00=6*s**2-6*s; hp10=3*s**2-4*s+1
        hp01=-6*s**2+6*s; hp11=3*s**2-2*s
        hpp00=12*s-6; hpp10=6*s-4
        hpp01=-12*s+6; hpp11=6*s-2
        y = h00*y0+h10*T*d0+h01*y1+h11*T*d1
        ys = hp00*y0+hp10*T*d0+hp01*y1+hp11*T*d1
        yss = hpp00*y0+hpp10*T*d0+hpp01*y1+hpp11*T*d1
        yt=ys/T; ytt=yss/T**2
        xx,zz,pp=y; xd,zd,pd=yt; xdd,zdd,pdd=ytt
        eta=-3*zd/zz
        etad=-3*(zdd/zz-(zd/zz)**2)
        chi=xd; chid=xdd
        xi=chi+eta/2
        # numeric potentials via the same algebra
        em4=math.exp(-4*xx/3); ep2=math.exp(2*xx/3); ep8=math.exp(8*xx/3)
        VD=4*zz**-4*(em4-ep2)+4*(ep2*zz**2-em4*zz**8)
        Vx=4*zz**-4*(ep8-em4)+4*zz**2*(em4-ep2)
        VH=(2/3)*zz**-4*(ep8-2*ep2+em4)-(4/3)*zz**2*(ep2+em4)+(2/3)*em4*zz**8
        Db=-2*pp*eta+VD-etad
        Eb=-2*pp*chi+Vx+Db/2-chid
        Hb=2*(pp*pp-xi*xi/3-eta*eta/4+VH/2-pd)
        X[:,k]=[xx,zz,pp,chi,eta]
        Uc[:,k]=[Hb,Eb,Db]
    return X,Uc


def solve(eps, N, warm=None, mode='ch'):
    opti=ca.Opti()
    X=opti.variable(5,N+1)
    U=opti.variable(3,N+1)
    A=opti.variable(); tch=opti.variable(); T=opti.variable()
    dt=T/N
    opti.subject_to(X[:,0]==entry_ca(eps,A))
    if mode == 'ch':
        opti.subject_to(X[:,-1]==ch_ca(tch))
    elif mode == 'stable':
        # Map the scale-free state to compact ACH variables at zeta*=10^-2.
        zeta=1e-2
        be=X[0,-1]-1.5*ca.log(X[1,-1])
        q=-3*ca.log(X[1,-1]); xi=X[3,-1]+X[4,-1]/2
        fac=math.sqrt(zeta)*ca.exp(-be/3)
        yf=fac*(X[2,-1]+2*xi/3)
        yg=fac*(X[2,-1]-xi/3+X[4,-1]/2)
        yh=fac*(X[2,-1]-xi/3-X[4,-1]/2)
        kap=math.sqrt(zeta)*ca.exp(be)
        Pf=2*kap**2-8*zeta**2*ca.sinh(q)**2/kap**2
        Pg=-2*kap**2+4*zeta*ca.exp(-q)+4*zeta**2*ca.sinh(2*q)/kap**2
        Ph=-2*kap**2+4*zeta*ca.exp(q)-4*zeta**2*ca.sinh(2*q)/kap**2
        con=yf*yg+yg*yh+yh*yf-6-(Pf+Pg+Ph)/2
        # Nonlinear stable-set residual by backward integration.  Starting near
        # E(0) at zeta=zeta_end, use the physical -4 and -6 stable amplitudes,
        # integrate the exact Einstein compact ODE backward until zeta=.01,
        # and match the controlled terminal state.  Backward growth of these
        # modes is bounded because the zeta range is finite.  This parameterizes
        # the nonlinear constrained standard-CR stable set, unlike ub=0 alone.
        a4=opti.variable(); a6=opti.variable()
        zend=1e-4; zend_s=math.sqrt(1+zend)
        wc=ca.vertcat(zend_s+1/zend_s,zend_s,zend_s,zend_s,0,zend)
        wc=wc+a4*zend**2*ca.vertcat(0,1,-1,0,-0.5,0)
        wc=wc+a6*zend**3*ca.vertcat(-4,1,1,1,0,0)
        def cf(w):
            yyf,yyg,yyh,kk,qq,zz=[w[i] for i in range(6)]; ss=yyf+yyg+yyh
            ppf=2*kk**2-8*zz**2*ca.sinh(qq)**2/kk**2
            ppg=-2*kk**2+4*zz*ca.exp(-qq)+4*zz**2*ca.sinh(2*qq)/kk**2
            pph=-2*kk**2+4*zz*ca.exp(qq)-4*zz**2*ca.sinh(2*qq)/kk**2
            return ca.vertcat(6-yyf*ss+ppf,6-yyg*ss+ppg,6-yyh*ss+pph,
                              kk*(yyf-yyg-yyh),yyg-yyh,-zz*(yyg+yyh))
        Ltail=opti.variable()
        opti.subject_to(opti.bounded(1.5,Ltail,3.5))
        dtail=-Ltail/140
        for _ in range(140):
            k1=cf(wc); k2=cf(wc+dtail*k1/2); k3=cf(wc+dtail*k2/2); k4=cf(wc+dtail*k3)
            wc=wc+dtail*(k1+2*k2+2*k3+k4)/6
        opti.subject_to(ca.vertcat(yf,yg,yh,kap,q,zeta)==wc)
        opti.subject_to(opti.bounded(-500,a4,500))
        opti.subject_to(opti.bounded(-500,a6,500))
        opti.subject_to(opti.bounded(-0.3,q,0.3))
        opti.subject_to(opti.bounded(0.7,kap,1.3))
    else:
        raise ValueError(mode)
    # Hermite-Simpson constraints with node controls.
    J=0
    for k in range(N):
        xk,xn=X[:,k],X[:,k+1]; uk,un=U[:,k],U[:,k+1]
        fk,fn=f_rhs(xk,uk),f_rhs(xn,un)
        xm=(xk+xn)/2 + dt*(fk-fn)/8
        um=(uk+un)/2
        fm=f_rhs(xm,um)
        opti.subject_to(xn-xk==dt*(fk+4*fm+fn)/6)
        J += dt*(running_cost(uk)+4*running_cost(um)+running_cost(un))/6
    opti.minimize(J)
    opti.subject_to(opti.bounded(0.15,A,5.0))
    if mode == 'ch':
        import os
        opti.subject_to(opti.bounded(float(os.environ.get('SAT_TCH_LO',0.701)),tch,
                                     float(os.environ.get('SAT_TCH_HI',4.0))))
    else:
        opti.subject_to(tch==1.2)
    opti.subject_to(opti.bounded(0.2,T,30.0))
    opti.subject_to(opti.bounded(-2.0,X[0,:],5.0))
    opti.subject_to(opti.bounded(max(0.03,0.7*eps**(1/3)),X[1,:],1.5))
    import os
    _xb=float(os.environ.get('SAT_XB',30))
    opti.subject_to(opti.bounded(-_xb,X[2:5,:],_xb))
    opti.subject_to(opti.bounded(-300,U,-0+300))
    # Optional state constraint sup b_+ <= SAT_BPMAX (non-round paths).  Applied at
    # nodes and Hermite-Simpson midpoints is unnecessary for the reduced question;
    # nodes suffice at the resolutions used, and the output records the node maximum.
    _bpmax = os.environ.get('SAT_BPMAX')
    if _bpmax is not None:
        for k in range(N+1):
            opti.subject_to(bplus_ca(X[:,k]) <= float(_bpmax))

    import os
    A0=float(os.environ.get('SAT_A0',1.0)); t0=float(os.environ.get('SAT_T0CH',1.2))
    T0=float(os.environ.get('SAT_TAU0',5.0))
    X0,U0=hermite_guess(eps,N,A0,t0,T0)
    opti.set_initial(A,A0); opti.set_initial(tch,t0); opti.set_initial(T,T0)
    opti.set_initial(X,X0); opti.set_initial(U,U0)
    if warm:
        rec=json.loads(Path(warm).read_text())
        A0=float(rec['A']); t0=float(rec['t_ch']); T0=float(rec['T'])
        oldX=np.array(rec['X'],float).T; oldU=np.array(rec['U'],float).T
        so=np.linspace(0,1,oldX.shape[1]); sn=np.linspace(0,1,N+1)
        Xi=np.vstack([np.interp(sn,so,row) for row in oldX])
        Ui=np.vstack([np.interp(sn,so,row) for row in oldU])
        # Enforce the new finite-epsilon entry through a smooth correction in the initial guess.
        corr=entry_np(eps,A0)-Xi[:,0]
        Xi += corr[:,None]*(1-sn)[None,:]**3
        opti.set_initial(A,A0); opti.set_initial(tch,t0); opti.set_initial(T,T0)
        opti.set_initial(X,Xi); opti.set_initial(U,Ui)
    if mode == 'stable':
        opti.set_initial(Ltail, math.log(100)/2)
        opti.set_initial(a4, 0); opti.set_initial(a6, 0)
    opts={'expand':True,'print_time':False,
          'ipopt':{'print_level':5,'max_iter':5000,'tol':2e-8,'acceptable_tol':2e-6,
                   'linear_solver':'mumps','mu_strategy':'adaptive'}}
    opti.solver('ipopt',opts)
    try:
        sol=opti.solve(); success=True; stats=sol.stats()
        val=lambda v: np.array(sol.value(v),dtype=float)
    except RuntimeError as exc:
        success=False; stats=opti.stats(); print('solve failed:',exc)
        val=lambda v: np.array(opti.debug.value(v),dtype=float)
    xv=val(X); uv=val(U); Av=float(val(A)); tv=float(val(tch)); Tv=float(val(T)); Jv=float(val(J))
    # Dynamics residual at the collocation equations, plus charge lower-bound checks.
    cres=[]
    for k in range(N):
        h=Tv/N; xk=xv[:,k]; xn=xv[:,k+1]; uk=uv[:,k]; un=uv[:,k+1]
        Ffun=ca.Function('fr',[ca.MX.sym('xx',5),ca.MX.sym('uu',3)],
                         [f_rhs(ca.MX.sym('xx',5),ca.MX.sym('uu',3))]) if False else None
        # evaluate through a small numpy transcription
        def fn_np(xx,uu):
            x,z,p,chi,eta=xx; Hb,Eb,Db=uu; xi=chi+eta/2
            em4=np.exp(-4*x/3); ep2=np.exp(2*x/3); ep8=np.exp(8*x/3)
            VD=4*z**-4*(em4-ep2)+4*(ep2*z*z-em4*z**8)
            Vx=4*z**-4*(ep8-em4)+4*z*z*(em4-ep2)
            VH=(2/3)*z**-4*(ep8-2*ep2+em4)-(4/3)*z*z*(ep2+em4)+(2/3)*em4*z**8
            return np.array([chi,-eta*z/3,p*p-xi*xi/3-eta*eta/4+VH/2-Hb/2,
                             -2*p*chi+Vx-Eb+Db/2,-2*p*eta+VD-Db])
        fk=fn_np(xk,uk); fn=fn_np(xn,un); xm=(xk+xn)/2+h*(fk-fn)/8; um=(uk+un)/2
        cres.append(np.max(np.abs(xn-xk-h*(fk+4*fn_np(xm,um)+fn)/6)))
    bp=np.array([bplus_np(xv[:,k]) for k in range(N+1)])
    cumulative=np.zeros(N+1)
    for k in range(N):
        h=Tv/N; um=.5*(uv[:,k]+uv[:,k+1])
        cumulative[k+1]=cumulative[k]+h*(
            (3*uv[0,k]**2/16+uv[1,k]**2/6+uv[2,k]**2/8)
            +4*(3*um[0]**2/16+um[1]**2/6+um[2]**2/8)
            +(3*uv[0,k+1]**2/16+uv[1,k+1]**2/6+uv[2,k+1]**2/8))/6
    rec={'eps':eps,'N':N,'mode':mode,'success':success,'return_status':stats.get('return_status'),
         'iterations':stats.get('iter_count'),'cost':Jv,'A':Av,'t_ch':tv,'T':Tv,
         'max_collocation_residual':float(max(cres)),'initial_state':xv[:,0].tolist(),
         'terminal_state':xv[:,-1].tolist(),'bplus_initial':float(bp[0]),
         'bplus_terminal':float(bp[-1]),'min_bplus':float(bp.min()),'max_bplus':float(bp.max()),
         'max_charge_rise_minus_cost':float(np.max(bp-bp[0]-cumulative)),
         'X':xv.T.tolist(),'U':uv.T.tolist(),'bplus':bp.tolist(),'cumulative_cost':cumulative.tolist()}
    import os
    tag=(f"eps{eps:.6g}_N{N}_{mode}").replace('.','p')+os.environ.get('SAT_TAG','')
    path=OUT/f'{tag}.json'; path.write_text(json.dumps(rec,indent=1))
    print(json.dumps({k:rec[k] for k in rec if k not in ('X','U','bplus','cumulative_cost')},indent=1))
    print('output',path)
    return 0 if success else 1


if __name__=='__main__':
    eps=float(sys.argv[1]); N=int(sys.argv[2]); warm=sys.argv[3] if len(sys.argv)>3 and sys.argv[3] != '-' else None
    mode=sys.argv[4] if len(sys.argv)>4 else 'ch'
    raise SystemExit(solve(eps,N,warm,mode))
