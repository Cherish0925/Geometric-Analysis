#!/usr/bin/env python3
"""Joint reflected core-to-entry finite-mode experiment.

Metric (physical Gaussian radius r, z periodic):
  g = dr^2 + exp(2 a(r,z)) dz^2
      + exp(sigma(r,z)+v(r,z)) dx^2
      + exp(sigma(r,z)-v(r,z)) dy^2.

This is the diagonal orthogonally-transitive T^2 class, expressed directly in
(base, orbit-area, orbit-shape) variables.  It starts from the validated
Step-69 scalar-minus-six center with S=0, includes the exact Koiso second jet,
and optimizes a, sigma, and v jointly.  The comparison family freezes the base
and orbit area to a cosh carrier and optimizes v only; the joint family allows
the Hessian/base-curvature response needed to compensate orbit-map stress.

All five orthonormal components of E=Ric+3g are evaluated.  The experiment is
finite-dimensional numerical evidence only; it is not an existence theorem.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import jax
jax.config.update("jax_enable_x64", True)
import jax.numpy as jnp
from jax import jit, jacfwd
import numpy as np
from numpy.polynomial import Chebyshev, Polynomial
from scipy.integrate import solve_bvp
from scipy.optimize import least_squares

MODE = sys.argv[1] if len(sys.argv) > 1 else "pilot"
if MODE == "pilot":
    KZ, NZ, NR = 4, 24, 29
    R_LIST = [2.0, 4.0, 6.0]
    MAX_NFEV = 85
    LOCAL_ELL = [0.25, 0.40, 0.65, 1.0]
    NGLOBAL = 8
elif MODE == "refine":
    KZ, NZ, NR = 6, 36, 41
    R_LIST = [4.0, 6.0, 8.0]
    MAX_NFEV = 150
    LOCAL_ELL = [0.20, 0.30, 0.45, 0.68, 1.0, 1.45]
    NGLOBAL = 12
else:
    raise ValueError("mode must be pilot or refine")

TWOPI = 2.0 * np.pi
A_CENTER = 1.0
P_LP = 8.0
W_ENTRY = 0.35
W_RIC = 0.08
W_ANISO_FLUX = 0.015
W_COEF = 2.0e-7


def real_fourier_basis(z: np.ndarray, kz: int):
    nm = 1 + 2 * kz
    Z = np.zeros((z.size, nm)); Z1 = np.zeros_like(Z); Z2 = np.zeros_like(Z)
    Z[:, 0] = 1.0
    for k in range(1, kz + 1):
        ic, is_ = 2*k - 1, 2*k
        Z[:, ic] = np.cos(k*z); Z[:, is_] = np.sin(k*z)
        Z1[:, ic] = -k*np.sin(k*z); Z1[:, is_] = k*np.cos(k*z)
        Z2[:, ic] = -k*k*np.cos(k*z); Z2[:, is_] = -k*k*np.sin(k*z)
    return Z, Z1, Z2


def yamabe_center(z_eval: np.ndarray):
    def ode(z, y):
        u, up = y
        return np.vstack((up, 0.75*u**5 - 0.25*A_CENTER**2*np.cos(z)**2*u))
    def bc(ya, yb):
        return np.array([ya[0]-yb[0], ya[1]-yb[1]])
    zz = np.linspace(0.0, TWOPI, 801)
    u0 = (A_CENTER*A_CENTER/6.0)**0.25
    guess = np.vstack((u0*(1+0.02*np.cos(2*zz)), -0.04*u0*np.sin(2*zz)))
    sol = solve_bvp(ode, bc, zz, guess, tol=1e-11, max_nodes=40000)
    if not sol.success:
        raise RuntimeError(sol.message)
    u = sol.sol(z_eval)[0]
    f = A_CENTER*np.sin(z_eval)
    # a=2 log u, b=2 log u+f, c=2 log u-f; sigma=b+c, v=b-c.
    return 2*np.log(u), 4*np.log(u), 2*f


def intrinsic_ric_np(a, sig, v, az, sz, vz, azz, szz, vzz):
    b=(sig+v)/2; c=(sig-v)/2
    bz=(sz+vz)/2; cz=(sz-vz)/2
    bzz=(szz+vzz)/2; czz=(szz-vzz)/2
    em=np.exp(-2*a)
    ra=-em*((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz)
    rb=-em*((bzz-az*bz)+bz*bz+bz*cz)
    rc=-em*((czz-az*cz)+cz*cz+bz*cz)
    return np.stack((ra,rb,rc))


z_np = TWOPI*np.arange(NZ)/NZ
Z_np, Z1_np, Z2_np = real_fourier_basis(z_np, KZ)
NM = Z_np.shape[1]
center_raw = np.stack(yamabe_center(z_np))
C0 = np.stack([np.linalg.lstsq(Z_np, q, rcond=None)[0] for q in center_raw])
center = C0@Z_np.T; center_z=C0@Z1_np.T; center_zz=C0@Z2_np.T
center_ric = intrinsic_ric_np(center[0],center[1],center[2],center_z[0],center_z[1],center_z[2],center_zz[0],center_zz[1],center_zz[2])
center_scalar = center_ric.sum(0)
# Koiso L_i''=Ric_i+3. Convert (a,b,c) accelerations to (a,sigma=b+c,v=b-c).
J2_raw = np.stack((center_ric[0]+3.0,
                   center_ric[1]+center_ric[2]+6.0,
                   center_ric[1]-center_ric[2]))
J2 = np.stack([np.linalg.lstsq(Z_np,q,rcond=None)[0] for q in J2_raw])

Z=jnp.asarray(Z_np); Z1=jnp.asarray(Z1_np); Z2=jnp.asarray(Z2_np)
C0j=jnp.asarray(C0); J2j=jnp.asarray(J2)


def logcosh_np(r):
    return np.logaddexp(r,-r)-math.log(2.0)


def carrier_arrays(r: np.ndarray, ell: float):
    """C=.5 ell^2(1-exp(-(r/ell)^2)); C''(0)=1, C'(0)=0."""
    x=r/ell; e=np.exp(-x*x)
    return 0.5*ell*ell*(1-e), r*e, e*(1-2*x*x)


def free_basis(r: np.ndarray, R: float):
    vals=[]; d1=[]; d2=[]; names=[]
    # Local analytic modes vanish through second order at reflection center.
    for ell in LOCAL_ELL:
        x=r/ell; e=np.exp(-x*x)
        vals.append(x**4*e)
        d1.append(e*(4*x**3-2*x**5)/ell)
        d2.append(e*(12*x**2-18*x**4+4*x**6)/(ell*ell))
        names.append(f"local_{ell:g}")
    # Global even modes s^4 T_j(2s^2-1); all vanish through order 2 at center.
    sp=Polynomial([0,1]); arg=2*sp**2-1
    s=r/R
    for j in range(NGLOBAL):
        p=sp**4*Chebyshev.basis(j).convert(kind=Polynomial)(arg)
        vv=p(s); q1=p.deriv(1)(s)/R; q2=p.deriv(2)(s)/(R*R)
        scale=max(np.sqrt(np.mean(vv*vv)+np.mean((R*q1)**2)+np.mean((R*R*q2)**2)),1e-12)
        vals.append(vv/scale); d1.append(q1/scale); d2.append(q2/scale)
        names.append(f"global_{j}")
    return np.array(vals).T,np.array(d1).T,np.array(d2).T,names


def radial_grid(R: float):
    inner_end=min(1.5,R)
    ninner=max(15,int(round(NR*inner_end/R)))
    ninner=min(ninner,NR-5)
    inner=np.linspace(0,inner_end,ninner,endpoint=False)
    outer=np.linspace(inner_end,R,NR-ninner)
    return np.unique(np.concatenate((inner,outer)))


def make_problem(R: float, ell: float, variant: str, entry_weight: float):
    r_np=radial_grid(R)
    B_np,B1_np,B2_np,names=free_basis(r_np,R); J=B_np.shape[1]
    car_np,car1_np,car2_np=carrier_arrays(r_np,ell)
    B=jnp.asarray(B_np); B1=jnp.asarray(B1_np); B2=jnp.asarray(B2_np)
    car=jnp.asarray(car_np); car1=jnp.asarray(car1_np); car2=jnp.asarray(car2_np)
    r=jnp.asarray(r_np)
    wr=np.empty(len(r_np)); wr[0]=(r_np[1]-r_np[0])/2; wr[-1]=(r_np[-1]-r_np[-2])/2
    wr[1:-1]=(r_np[2:]-r_np[:-2])/2; wr/=R
    sqw=jnp.sqrt(jnp.asarray(wr)[:,None]/NZ)
    free_components=(0,1,2) if variant=="joint" else (2,)
    ncomp=len(free_components)

    def fields(vec):
        coef=vec.reshape(ncomp,J,NM)
        # Exact center value and Koiso second jet via bounded carrier.
        l0=jnp.einsum('im,zm->iz',C0j,Z)
        l0z=jnp.einsum('im,zm->iz',C0j,Z1); l0zz=jnp.einsum('im,zm->iz',C0j,Z2)
        j2=jnp.einsum('im,zm->iz',J2j,Z)
        j2z=jnp.einsum('im,zm->iz',J2j,Z1); j2zz=jnp.einsum('im,zm->iz',J2j,Z2)
        # Common cosh expansion gives a'',b'',c''=1 before the correction;
        # in (a,sigma,v), its second jet is (1,2,0). Carrier corrects to Koiso.
        common=jnp.stack((jnp.logaddexp(r,-r)-math.log(2.0),
                          2*(jnp.logaddexp(r,-r)-math.log(2.0)),
                          jnp.zeros_like(r)))
        common1=jnp.stack((jnp.tanh(r),2*jnp.tanh(r),jnp.zeros_like(r)))
        common2=jnp.stack((1/jnp.cosh(r)**2,2/jnp.cosh(r)**2,jnp.zeros_like(r)))
        basejet=jnp.array([1.0,2.0,0.0])[:,None,None]
        corr2=j2[:,None,:]-basejet
        corr2z=j2z[:,None,:]
        corr2zz=j2zz[:,None,:]
        L=l0[:,None,:]+common[:,:,None]+car[None,:,None]*corr2
        Lr=common1[:,:,None]+car1[None,:,None]*corr2
        Lrr=common2[:,:,None]+car2[None,:,None]*corr2
        Lz=l0z[:,None,:]+car[None,:,None]*corr2z
        Lzz=l0zz[:,None,:]+car[None,:,None]*corr2zz
        Lrz=car1[None,:,None]*corr2z
        # Free corrections.
        for p,comp in enumerate(free_components):
            F=jnp.einsum('rj,jm,zm->rz',B,coef[p],Z)
            Fr=jnp.einsum('rj,jm,zm->rz',B1,coef[p],Z)
            Frr=jnp.einsum('rj,jm,zm->rz',B2,coef[p],Z)
            Fz=jnp.einsum('rj,jm,zm->rz',B,coef[p],Z1)
            Fzz=jnp.einsum('rj,jm,zm->rz',B,coef[p],Z2)
            Frz=jnp.einsum('rj,jm,zm->rz',B1,coef[p],Z1)
            L=L.at[comp].add(F); Lr=Lr.at[comp].add(Fr); Lrr=Lrr.at[comp].add(Frr)
            Lz=Lz.at[comp].add(Fz); Lzz=Lzz.at[comp].add(Fzz); Lrz=Lrz.at[comp].add(Frz)
        return L,Lr,Lrr,Lz,Lzz,Lrz

    def components(vec):
        L,Lr,Lrr,Lz,Lzz,Lrz=fields(vec)
        a,sig,v=L; ar,sr,vr=Lr; arr,srr,vrr=Lrr
        az,sz,vz=Lz; azz,szz,vzz=Lzz; arz,srz,vrz=Lrz
        b=(sig+v)/2; c=(sig-v)/2
        br=(sr+vr)/2; cr=(sr-vr)/2; brr=(srr+vrr)/2; crr=(srr-vrr)/2
        bz=(sz+vz)/2; cz=(sz-vz)/2; bzz=(szz+vzz)/2; czz=(szz-vzz)/2
        brz=(srz+vrz)/2; crz=(srz-vrz)/2
        em=jnp.exp(-2*a)
        E0=3-ar*ar-arr-br*br-brr-cr*cr-crr
        E1=jnp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-brz-crz)
        E2=3-ar*ar-ar*br-ar*cr-arr+em*(az*bz+az*cz-bz*bz-bzz-cz*cz-czz)
        E3=3-ar*br-br*br-br*cr-brr+em*(az*bz-bz*bz-bz*cz-bzz)
        E4=3-ar*cr-br*cr-cr*cr-crr+em*(az*cz-bz*cz-cz*cz-czz)
        return jnp.stack((E0,E1,E2,E3,E4)),(L,Lr,Lrr,Lz,Lzz,Lrz)

    def intrinsic_jax(L,Lz,Lzz):
        a,sig,v=L; az,sz,vz=Lz; _,szz,vzz=Lzz
        b=(sig+v)/2; c=(sig-v)/2; bz=(sz+vz)/2; cz=(sz-vz)/2
        bzz=(szz+vzz)/2; czz=(szz-vzz)/2; em=jnp.exp(-2*a)
        return jnp.stack((-em*((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz),
                          -em*((bzz-az*bz)+bz*bz+bz*cz),
                          -em*((czz-az*cz)+cz*cz+bz*cz)))

    def residual(vec):
        E,fld=components(vec)
        # Frobenius-weighted L2 field residual for stable Gauss--Newton.  True
        # operator sup, RMS, and q95 are always computed independently below.
        core=jnp.stack((E[0],jnp.sqrt(2.)*E[1],E[2],E[3],E[4]))*sqw[None]
        out=[core.reshape(-1)]
        if entry_weight>0:
            L,Lr,Lrr,Lz,Lzz,Lrz=fld
            ric=intrinsic_jax(L[:,-1],Lz[:,-1],Lzz[:,-1])
            # S=(a_r,b_r,c_r); convert from (a,sigma,v).
            S=jnp.stack((Lr[0,-1],(Lr[1,-1]+Lr[2,-1])/2,(Lr[1,-1]-Lr[2,-1])/2))
            w=math.sqrt(entry_weight/(3*NZ))
            out.append(w*(S-1).reshape(-1))
            out.append(math.sqrt(W_RIC/(3*NZ))*ric.reshape(-1))
            # Keep anisotropy flux free, but weakly discourage a large unattachable jet.
            out.append(math.sqrt(W_ANISO_FLUX/NZ)*Lr[2,-1].reshape(-1))
        out.append(math.sqrt(W_COEF/max(vec.size,1))*vec)
        return jnp.concatenate(out)

    return {"r":r_np,"J":J,"names":names,"variant":variant,"ncomp":ncomp,
            "fields":fields,"components":components,"residual":residual,
            "intrinsic":intrinsic_jax}


def exact_op(E):
    tr=E[0]+E[2]; disc=np.sqrt((E[0]-E[2])**2+4*E[1]**2)
    return np.maximum.reduce((np.abs((tr-disc)/2),np.abs((tr+disc)/2),np.abs(E[3]),np.abs(E[4])))


def diagnostics(vec,R,ell,pr,label):
    E_j,fld_j=pr["components"](jnp.asarray(vec)); E=np.asarray(E_j)
    L,Lr,Lrr,Lz,Lzz,Lrz=[np.asarray(x) for x in fld_j]; r=pr["r"]
    op=exact_op(E); ric=np.asarray(pr["intrinsic"](fld_j[0][:,-1],fld_j[3][:,-1],fld_j[4][:,-1]))
    S=np.stack((Lr[0],(Lr[1]+Lr[2])/2,(Lr[1]-Lr[2])/2))
    H=S.sum(0); shearI2=np.sum((S-1)**2,axis=0)
    rr_idx,zz_idx=np.unravel_index(np.argmax(op),op.shape)
    # OT variables and invariant physical orbit-map energy |dv|^2 on the base.
    map_er=Lr[2]**2; map_ez=np.exp(-2*L[0])*Lz[2]**2; map_energy=map_er+map_ez
    # Invariant base tensor formula specialized to diagonal U=v. In Gaussian gauge,
    # E_rr and E_zz are already exact; compare frozen-cusp prediction -1/2 dv⊗dv.
    frozen_pred=np.stack((-0.5*map_er,-0.5*map_ez))
    # Normal identity pointwise for all z.
    normal=Lrr[0]+Lrr[1]+Lr[0]**2+0.5*(Lr[1]**2+Lr[2]**2)-3+E[0]
    # Center and exit checks.
    center_val=np.stack((L[0,0],L[1,0],L[2,0]))
    center_second=np.stack((Lrr[0,0],Lrr[1,0],Lrr[2,0]))
    center_j2_projected=J2@Z_np.T
    entry_growth=np.mean((L[0,-1]-L[0,0]+L[1,-1]-L[1,0])/3)
    # Compensation ledger: compare full base residual with positive orbit stress scale.
    stress_sup=float(np.max(0.5*map_energy))
    return {
      "label":label,"variant":pr["variant"],"R_physical":R,"carrier_ell":ell,
      "operator_sup":float(op.max()),"operator_rms":float(np.sqrt(np.mean(op**2))),
      "operator_q95":float(np.quantile(op,0.95)),"argmax_r":float(r[rr_idx]),"argmax_z":float(z_np[zz_idx]),
      "component_sup":{k:float(np.abs(E[i]).max()) for i,k in enumerate(["E_rr","E_rz","E_zz","E_x","E_y"])},
      "center":{"value_error_sup":float(np.abs(center_val-center).max()),"shape_sup":float(np.abs(S[:,0]).max()),
                "second_jet_error_sup":float(np.abs(center_second-center_j2_projected).max()),
                "scalar_minus6_sup":float(np.abs(center_scalar+6).max()),
                "component_sup":{k:float(np.abs(E[i,0]).max()) for i,k in enumerate(["E_rr","E_rz","E_zz","E_x","E_y"]) }},
      "exit":{"S_minus_I_sup":float(np.abs(S[:,-1]-1).max()),"S_minus_I_rms":float(np.sqrt(np.mean((S[:,-1]-1)**2))),
              "intrinsic_Ric_sup":float(np.abs(ric).max()),"v_oscillation":float(np.ptp(L[2,-1])),
              "v_r_sup":float(np.abs(Lr[2,-1]).max()),"a_range":[float(L[0,-1].min()),float(L[0,-1].max())],
              "sigma_range":[float(L[1,-1].min()),float(L[1,-1].max())],"mean_log_volume_growth":float(entry_growth)},
      "base_orbit_coupling":{"physical_map_energy_sup":float(map_energy.max()),"orbit_stress_half_sup":stress_sup,
              "frozen_cusp_Err_prediction_sup":float(np.abs(frozen_pred[0]).max()),
              "frozen_cusp_Ezz_prediction_sup":float(np.abs(frozen_pred[1]).max()),
              "base_response_needed":bool(stress_sup>float(op.max()))},
      "normal_identity_sup":float(np.abs(normal).max()),
      "field_range":[float(L.min()),float(L.max())],"coefficient_norm":float(np.linalg.norm(vec)),
      "residual_norm":float(np.linalg.norm(np.asarray(pr["residual"](jnp.asarray(vec)))))
    }


def solve_problem(pr,x0):
    rf=jit(pr["residual"]); jf=jit(jacfwd(pr["residual"]))
    def fun(x): return np.asarray(rf(jnp.asarray(x)),float)
    def jac(x): return np.asarray(jf(jnp.asarray(x)),float)
    return least_squares(fun,x0,jac=jac,method="trf",tr_solver="lsmr",x_scale="jac",
                         bounds=(-20,20),max_nfev=MAX_NFEV,ftol=2e-10,xtol=2e-10,gtol=2e-10,verbose=0)


def best_carrier(R,variant):
    rows=[]
    for ell in [0.20,0.28,0.40,0.58,0.82,1.15]:
        pr=make_problem(R,ell,variant,0.0); x=np.zeros(pr["ncomp"]*pr["J"]*NM)
        d=diagnostics(x,R,ell,pr,"carrier")
        rows.append((d["operator_sup"],ell,pr,d))
    rows.sort(key=lambda q:q[0])
    return rows


def main():
    print(f"Step80 joint base response {MODE}: Kz={KZ} Nz={NZ} Nr={NR}")
    print(f"center scalar error={np.abs(center_scalar+6).max():.3e}; Koiso trace={J2_raw[0]+J2_raw[1]}")
    out={"scope":"finite-mode joint (base, orbit area, orbit shape) reflected core-to-entry test; not existence/nonexistence",
         "mode":MODE,"grid":{"Kz":KZ,"Nz":NZ,"Nr":NR},
         "center":{"A":A_CENTER,"scalar_minus6_sup":float(np.abs(center_scalar+6).max()),
                   "Koiso_second_jet_component_ranges":[[float(q.min()),float(q.max())] for q in J2_raw]},
         "runs":[]}
    croot=Path(__file__).resolve().parents[1]/"data"/f"step80_joint_coefficients_{MODE}"
    croot.mkdir(parents=True,exist_ok=True)
    for R in R_LIST:
        row={"R":R,"variants":{}}
        for variant in ["shape_only","joint"]:
            scans=best_carrier(R,variant); _,ell,pr,d0=scans[0]
            x0=np.zeros(pr["ncomp"]*pr["J"]*NM)
            t0=time.time(); res0=solve_problem(pr,x0); dres=diagnostics(res0.x,R,ell,pr,"residual")
            pr1=make_problem(R,ell,variant,W_ENTRY); res1=solve_problem(pr1,res0.x); dent=diagnostics(res1.x,R,ell,pr1,"entry")
            print(f"R={R:g} {variant}: carrier {d0['operator_sup']:.4g}; residual {dres['operator_sup']:.4g}; entry {dent['operator_sup']:.4g}; exit S {dent['exit']['S_minus_I_sup']:.3g}; Ric3 {dent['exit']['intrinsic_Ric_sup']:.3g}; wall {time.time()-t0:.1f}s",flush=True)
            row["variants"][variant]={"carrier_scan":[d for _,_,_,d in scans],"selected_ell":ell,
                "residual":dres,"entry":dent,
                "solvers":[{"nfev":int(res0.nfev),"cost":float(res0.cost),"optimality":float(res0.optimality),"message":str(res0.message)},
                           {"nfev":int(res1.nfev),"cost":float(res1.cost),"optimality":float(res1.optimality),"message":str(res1.message)}]}
            np.save(croot/f"R{R:g}_{variant}_res.npy",res0.x); np.save(croot/f"R{R:g}_{variant}_entry.npy",res1.x)
        # Direct paired comparison at same R.
        so=row["variants"]["shape_only"]["entry"]; jo=row["variants"]["joint"]["entry"]
        row["paired_comparison"]={"operator_sup_ratio_joint_over_shape":jo["operator_sup"]/so["operator_sup"],
            "operator_rms_ratio_joint_over_shape":jo["operator_rms"]/so["operator_rms"],
            "joint_argmax_r":jo["argmax_r"],"shape_argmax_r":so["argmax_r"]}
        out["runs"].append(row)
    path=Path(__file__).resolve().parents[1]/"data"/f"step80_joint_base_response_{MODE}.json"
    path.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print("wrote",path)


if __name__=="__main__":
    main()
