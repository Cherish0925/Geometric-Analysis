#!/usr/bin/env python3
"""Full-residual search for a reflection core with nonflat expanded exit.

We work in physical Gaussian distance r on [0,R] with the diagonal,
orthogonally-transitive T^2-invariant ansatz

  g = dr^2 + exp(2a(r,z)) dz^2 + exp(2b(r,z)) dx^2
             + exp(2c(r,z)) dy^2,

z periodic.  The center values are the validated Step-69 scalar-minus-six
Yamabe metric and a_r=b_r=c_r=0 is enforced exactly.  No flat outer metric is
prescribed.  The objective contains *all five* orthonormal components of
E=Ric+3g, plus optional weak costs for reaching an expanded entry slice.

This is a finite-dimensional numerical experiment in a restricted symmetry
class.  It is not an Einstein-DeTurck existence theorem and it does not infer
constraint propagation from a three-equation subsystem.

Usage:
  python step75_full_residual_core_search.py pilot
  python step75_full_residual_core_search.py refine
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import minimize

import jax
jax.config.update("jax_enable_x64", True)
import jax.numpy as jnp
from jax import jit, value_and_grad

MODE = sys.argv[1] if len(sys.argv) > 1 else "pilot"
if MODE == "pilot":
    KZ, JR, NR, NZ = 5, 11, 23, 32
    ADAM_STEPS, LBFGS_ITERS = 350, 220
    R_LIST = [2.0, 4.0, 6.0]
elif MODE == "refine":
    KZ, JR, NR, NZ = 8, 17, 35, 48
    ADAM_STEPS, LBFGS_ITERS = 900, 550
    R_LIST = [4.0, 6.0, 8.0]
else:
    raise ValueError("mode must be pilot or refine")

P_NORM = 8.0
W_ENTRY_S = 0.20
W_ENTRY_RIC = 0.04
W_HIGH = 2.0e-8
TWOPI = 2.0 * np.pi


def yamabe_center(z_eval: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Validated Step-69 center; note the sign u''=.75u^5-.25cos^2(z)u."""
    def ode(z, y):
        u, up = y
        return np.vstack((up, 0.75 * u**5 - 0.25 * np.cos(z)**2 * u))

    def bc(ya, yb):
        return np.array([ya[0] - yb[0], ya[1] - yb[1]])

    zz = np.linspace(0.0, TWOPI, 801)
    u0 = (np.mean(np.cos(zz)**2) / 3.0) ** 0.25
    guess = np.vstack((u0 * (1.0 + 0.02 * np.cos(2.0 * zz)),
                       -0.04 * u0 * np.sin(2.0 * zz)))
    sol = solve_bvp(ode, bc, zz, guess, tol=1.0e-11, max_nodes=40000)
    if not sol.success:
        raise RuntimeError(sol.message)
    u = sol.sol(z_eval)[0]
    f = np.sin(z_eval)
    return 2.0 * np.log(u), 2.0 * np.log(u) + f, 2.0 * np.log(u) - f


def real_fourier_basis(z: np.ndarray, kz: int):
    nm = 1 + 2 * kz
    Z = np.zeros((z.size, nm))
    Z1 = np.zeros_like(Z)
    Z2 = np.zeros_like(Z)
    Z[:, 0] = 1.0
    for k in range(1, kz + 1):
        ic, is_ = 2*k - 1, 2*k
        Z[:, ic] = np.cos(k*z)
        Z[:, is_] = np.sin(k*z)
        Z1[:, ic] = -k*np.sin(k*z)
        Z1[:, is_] = k*np.cos(k*z)
        Z2[:, ic] = -k*k*np.cos(k*z)
        Z2[:, is_] = -k*k*np.sin(k*z)
    return Z, Z1, Z2


def radial_basis(s: np.ndarray, jr: int):
    """B_j=s^2 T_j(2s-1), so correction and its r derivative vanish at r=0."""
    from numpy.polynomial import Polynomial, Chebyshev
    B = np.zeros((s.size, jr))
    Bs = np.zeros_like(B)
    Bss = np.zeros_like(B)
    xpoly = Polynomial([-1.0, 2.0])
    spoly = Polynomial([0.0, 1.0])
    for j in range(jr):
        tj = Chebyshev.basis(j).convert(kind=Polynomial)(xpoly)
        p = spoly**2 * tj
        B[:, j] = p(s)
        Bs[:, j] = p.deriv(1)(s)
        Bss[:, j] = p.deriv(2)(s)
    return B, Bs, Bss


# Chebyshev-clustered physical grid, ordered from center to exit.
s_np = 0.5 * (1.0 - np.cos(np.pi * np.arange(NR) / (NR - 1)))
z_np = TWOPI * np.arange(NZ) / NZ
Z_np, Z1_np, Z2_np = real_fourier_basis(z_np, KZ)
B_np, Bs_np, Bss_np = radial_basis(s_np, JR)
NM = Z_np.shape[1]

# Project the exact center to the working Fourier space.
center_raw = np.stack(yamabe_center(z_np))
center_coef = np.stack([np.linalg.lstsq(Z_np, v, rcond=None)[0] for v in center_raw])
center = center_coef @ Z_np.T
center_z = center_coef @ Z1_np.T
center_zz = center_coef @ Z2_np.T

# Intrinsic Ricci of a diagonal T^3 metric depending on z.
def intrinsic_ric_np(L, Lz, Lzz):
    a, b, c = L
    az, bz, cz = Lz
    _, bzz, czz = Lzz
    em2a = np.exp(-2.0*a)
    ra = -em2a * ((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz)
    rb = -em2a * ((bzz-az*bz)+bz*bz+bz*cz)
    rc = -em2a * ((czz-az*cz)+cz*cz+bz*cz)
    return np.stack((ra, rb, rc))

center_ric = intrinsic_ric_np(center, center_z, center_zz)
center_scalar = np.sum(center_ric, axis=0)
center_accel_correction = center_ric + 2.0  # base log(cosh r) contributes +1 to L_rr

# JAX constants.
s = jnp.asarray(s_np)
z = jnp.asarray(z_np)
B = jnp.asarray(B_np); Bs = jnp.asarray(Bs_np); Bss = jnp.asarray(Bss_np)
Z = jnp.asarray(Z_np); Z1 = jnp.asarray(Z1_np); Z2 = jnp.asarray(Z2_np)
C0 = jnp.asarray(center_coef)


def logcosh(x):
    return jnp.logaddexp(x, -x) - math.log(2.0)


def fields_from_vec(vec, R):
    coef = vec.reshape(3, JR, NM)
    r = R * s
    A = logcosh(r)
    Ar = jnp.tanh(r)
    Arr = 1.0 / jnp.cosh(r)**2

    l0 = jnp.einsum('im,zm->iz', C0, Z)
    l0z = jnp.einsum('im,zm->iz', C0, Z1)
    l0zz = jnp.einsum('im,zm->iz', C0, Z2)

    corr = jnp.einsum('rj,ijm,zm->irz', B, coef, Z)
    corrr = jnp.einsum('rj,ijm,zm->irz', Bs/R, coef, Z)
    corrrr = jnp.einsum('rj,ijm,zm->irz', Bss/(R*R), coef, Z)
    corrz = jnp.einsum('rj,ijm,zm->irz', B, coef, Z1)
    corrzz = jnp.einsum('rj,ijm,zm->irz', B, coef, Z2)
    corrrz = jnp.einsum('rj,ijm,zm->irz', Bs/R, coef, Z1)

    L = l0[:, None, :] + A[None, :, None] + corr
    Lr = Ar[None, :, None] + corrr
    Lrr = Arr[None, :, None] + corrrr
    Lz = l0z[:, None, :] + corrz
    Lzz = l0zz[:, None, :] + corrzz
    Lrz = corrrz
    return L, Lr, Lrr, Lz, Lzz, Lrz


def residual_components(vec, R):
    L, Lr, Lrr, Lz, Lzz, Lrz = fields_from_vec(vec, R)
    a, b, c = L
    ar, br, cr = Lr
    arr, brr, crr = Lrr
    az, bz, cz = Lz
    _, bzz, czz = Lzz
    _, brz, crz = Lrz
    em2a = jnp.exp(-2.0*a)

    E00 = 3.0-ar*ar-arr-br*br-brr-cr*cr-crr
    E0z = jnp.exp(-a) * (ar*bz+ar*cz-br*bz-cr*cz-brz-crz)
    Ezz = (3.0-ar*ar-ar*br-ar*cr-arr
           + em2a*(az*bz+az*cz-bz*bz-bzz-cz*cz-czz))
    Ex = (3.0-ar*br-br*br-br*cr-brr
          + em2a*(az*bz-bz*bz-bz*cz-bzz))
    Ey = (3.0-ar*cr-br*cr-cr*cr-crr
          + em2a*(az*cz-bz*cz-cz*cz-czz))
    return jnp.stack((E00, E0z, Ezz, Ex, Ey)), (L, Lr, Lrr, Lz, Lzz, Lrz)


def intrinsic_ric_jax(L, Lz, Lzz):
    a, b, c = L
    az, bz, cz = Lz
    _, bzz, czz = Lzz
    em2a = jnp.exp(-2.0*a)
    ra = -em2a*((bzz-az*bz)+bz*bz+(czz-az*cz)+cz*cz)
    rb = -em2a*((bzz-az*bz)+bz*bz+bz*cz)
    rc = -em2a*((czz-az*cz)+cz*cz+bz*cz)
    return jnp.stack((ra, rb, rc))


def loss(vec, R):
    E, fld = residual_components(vec, R)
    L, Lr, _, Lz, Lzz, _ = fld
    # Frobenius norm of the 2x2 base block plus the two orbit eigenvalues.
    p2 = E[0]**2 + 2.0*E[1]**2 + E[2]**2 + E[3]**2 + E[4]**2
    full_lp = jnp.mean((p2 + 1.0e-24)**(P_NORM/2.0))**(1.0/P_NORM)

    exit_s = jnp.sqrt(jnp.mean(jnp.sum((Lr[:, -1, :]-1.0)**2, axis=0))+1e-24)
    ric3 = intrinsic_ric_jax(L[:, -1, :], Lz[:, -1, :], Lzz[:, -1, :])
    exit_ric = jnp.sqrt(jnp.mean(jnp.sum(ric3**2, axis=0))+1e-24)

    coef = vec.reshape(3, JR, NM)
    jr_weight = (jnp.arange(JR)/(max(JR-1,1)))**6
    kz_weight = jnp.zeros(NM)
    # Last two Fourier shells and last three radial modes receive a tiny stabilizer.
    kz_weight = kz_weight.at[max(0,NM-4):].set(1.0)
    high = jnp.sum(coef**2 * (jr_weight[None,:,None] + kz_weight[None,None,:]))
    return full_lp + W_ENTRY_S*exit_s + W_ENTRY_RIC*exit_ric + W_HIGH*high


loss_vg = jit(value_and_grad(loss, argnums=0), static_argnums=(1,))


def initial_vector(R, local_scale=0.55):
    """Second-order Koiso-compatible seed, smoothly localized near r=0."""
    r = R*s_np
    rho = 0.5*r*r*np.exp(-(r/local_scale)**4)
    # Fit rho in B_j while strongly enforcing rho_rr(0)=1.
    Afit = np.vstack((B_np, 50.0*Bss_np[[0],:]/(R*R)))
    yfit = np.concatenate((rho, [50.0]))
    rad = np.linalg.lstsq(Afit, yfit, rcond=None)[0]
    gcoef = np.stack([np.linalg.lstsq(Z_np, center_accel_correction[i], rcond=None)[0]
                      for i in range(3)])
    coef = np.einsum('j,im->ijm', rad, gcoef)
    return coef.reshape(-1)


def optimize_R(R, warm=None):
    v = initial_vector(R) if warm is None else warm.copy()
    # Reinitialize if a warm vector belongs to a substantially different physical scale.
    if not np.all(np.isfinite(v)):
        v = initial_vector(R)

    def fg(x):
        val, gr = loss_vg(jnp.asarray(x), float(R))
        return float(val), np.asarray(gr, dtype=float)

    # Adam preconditioner.
    m = np.zeros_like(v); q = np.zeros_like(v)
    b1, b2 = 0.9, 0.999
    best = (np.inf, v.copy())
    t0 = time.time()
    for it in range(1, ADAM_STEPS+1):
        val, gr = fg(v)
        if val < best[0]: best = (val, v.copy())
        m = b1*m + (1-b1)*gr
        q = b2*q + (1-b2)*gr*gr
        mh = m/(1-b1**it); qh = q/(1-b2**it)
        lr = 1.5e-3*(0.5+0.5*math.cos(math.pi*it/ADAM_STEPS)) + 8e-5
        v -= lr*mh/(np.sqrt(qh)+1e-8)
        if it % max(1,ADAM_STEPS//7) == 0:
            print(f"  R={R:g} Adam {it:4d}: loss={val:.6g} best={best[0]:.6g}",flush=True)
    v = best[1]
    res = minimize(fg, v, jac=True, method='L-BFGS-B',
                   options={'maxiter':LBFGS_ITERS,'maxls':35,'ftol':1e-13,'gtol':1e-9})
    print(f"  R={R:g} LBFGS: {res.message}; loss={res.fun:.6g}; nit={res.nit}; wall={time.time()-t0:.1f}s",flush=True)
    return np.asarray(res.x), float(res.fun), str(res.message)


def report(vec, R):
    E_j, fld_j = residual_components(jnp.asarray(vec), float(R))
    E = np.asarray(E_j)
    L, Lr, Lrr, Lz, Lzz, Lrz = [np.asarray(x) for x in fld_j]
    # Exact operator norm: eigs of base 2x2 block plus Ex,Ey.
    tr = E[0]+E[2]
    rad = np.sqrt((E[0]-E[2])**2 + 4*E[1]**2)
    lam_p = 0.5*(tr+rad); lam_m = 0.5*(tr-rad)
    op = np.maximum.reduce((np.abs(lam_p),np.abs(lam_m),np.abs(E[3]),np.abs(E[4])))
    ric3_exit = intrinsic_ric_np(L[:,-1,:],Lz[:,-1,:],Lzz[:,-1,:])
    S_exit = Lr[:,-1,:]
    H = np.sum(Lr,axis=0)
    shearI2 = np.sum((Lr-1.0)**2,axis=0)

    # Pointwise weighted normal identity, integrated with trapezoidal quadrature.
    rr = R*s_np
    integrand_shear = np.exp(2*rr)[:,None]*shearI2
    integrand_E = np.exp(2*rr)[:,None]*E[0]
    shear_int = np.trapezoid(integrand_shear,rr,axis=0)
    E_int = np.trapezoid(integrand_E,rr,axis=0)
    balance = np.exp(2*R)*(H[-1]-3.0)+3.0+shear_int+E_int

    center_S = Lr[:,0,:]
    center_vals_err = L[:,0,:]-center
    entry_volume_growth = float(np.mean(np.sum(L[:,-1,:],axis=0)-np.sum(L[:,0,:],axis=0))/3.0)
    out = {
        'R_physical':float(R),
        'loss':float(loss(jnp.asarray(vec),float(R))),
        'full_residual':{
            'operator_sup':float(np.max(op)),
            'operator_rms':float(np.sqrt(np.mean(op**2))),
            'component_sup':{k:float(np.max(np.abs(E[i]))) for i,k in enumerate(['E_rr','E_rz_orth','E_zz','E_x','E_y'])},
            'argmax':list(map(int,np.unravel_index(np.argmax(op),op.shape))),
            'argmax_r':float(rr[np.unravel_index(np.argmax(op),op.shape)[0]]),
        },
        'center':{
            'value_error_sup':float(np.max(np.abs(center_vals_err))),
            'shape_sup':float(np.max(np.abs(center_S))),
            'projected_scalar_minus6_sup':float(np.max(np.abs(center_scalar+6.0))),
            'projected_scalar_range':[float(np.min(center_scalar)),float(np.max(center_scalar))],
        },
        'exit':{
            'S_minus_I_sup':float(np.max(np.abs(S_exit-1.0))),
            'S_minus_I_rms':float(np.sqrt(np.mean((S_exit-1.0)**2))),
            'H_range':[float(np.min(np.sum(S_exit,axis=0))),float(np.max(np.sum(S_exit,axis=0)))],
            'intrinsic_Ric_operator_sup':float(np.max(np.abs(ric3_exit))),
            'intrinsic_scalar_range':[float(np.min(np.sum(ric3_exit,axis=0))),float(np.max(np.sum(ric3_exit,axis=0)))],
            'anisotropy_oscillation':float(np.ptp(L[1,-1,:]-L[2,-1,:])),
            'orbit_area_log_oscillation':float(np.ptp(L[1,-1,:]+L[2,-1,:])),
            'mean_log_volume_growth':entry_volume_growth,
        },
        'normal_balance':{
            'quadrature_identity_sup':float(np.max(np.abs(balance))),
            'shear_integral_range':[float(np.min(shear_int)),float(np.max(shear_int))],
            'weighted_Err_integral_range':[float(np.min(E_int)),float(np.max(E_int))],
            'eta_range':[float(np.min(3.0-H[-1])),float(np.max(3.0-H[-1]))],
        },
        'field_ranges':{
            'a':[float(np.min(L[0])),float(np.max(L[0]))],
            'b':[float(np.min(L[1])),float(np.max(L[1]))],
            'c':[float(np.min(L[2])),float(np.max(L[2]))],
        }
    }
    return out


def baseline_report(R):
    return report(np.zeros(3*JR*NM),R)


def main():
    print(f"Step75 full-residual core search mode={MODE}; Kz={KZ}, Jr={JR}, grid={NR}x{NZ}")
    print(f"Projected center scalar error sup={np.max(np.abs(center_scalar+6)):.3e}")
    results = {
        'scope':'finite-dimensional full-Ricci test in diagonal orthogonally-transitive T2 class; not an existence theorem',
        'mode':MODE,
        'grid':{'Kz':KZ,'Jr':JR,'Nr':NR,'Nz':NZ},
        'yamabe_sign':'u_rr = +(3/4)u^5 -(1/4)cos(z)^2 u (validated Step69 sign)',
        'center_projected_scalar_error_sup':float(np.max(np.abs(center_scalar+6))),
        'objective_weights':{'p':P_NORM,'entry_S':W_ENTRY_S,'entry_intrinsic_Ric':W_ENTRY_RIC,'high_mode':W_HIGH},
        'runs':[]
    }
    warm = None
    coef_dir = Path(__file__).resolve().parents[1]/'data'/f'step75_core_coefficients_{MODE}'
    coef_dir.mkdir(parents=True,exist_ok=True)
    for R in R_LIST:
        base = baseline_report(R)
        print(f"R={R:g} baseline: op_sup={base['full_residual']['operator_sup']:.5g}, exit S-I={base['exit']['S_minus_I_sup']:.3g}")
        # Use a fresh Koiso-compatible seed for each R; cross-R warm starts distort physical scales.
        vec, obj, msg = optimize_R(R,warm=None)
        rep = report(vec,R)
        rep['baseline']=base
        rep['optimizer_message']=msg
        results['runs'].append(rep)
        np.save(coef_dir/f'R{R:g}.npy',vec)
        print(f"R={R:g} RESULT op_sup={rep['full_residual']['operator_sup']:.6g}; components={rep['full_residual']['component_sup']}; exit={rep['exit']}",flush=True)

    out = Path(__file__).resolve().parents[1]/'data'/f'step75_full_residual_core_{MODE}.json'
    out.write_text(json.dumps(results,indent=2),encoding='utf-8')
    print('wrote',out)


if __name__ == '__main__':
    main()
