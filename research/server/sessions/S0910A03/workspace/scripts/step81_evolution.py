#!/usr/bin/env python3
"""
Reflected Einstein germ evolution from rotating-loop centers.

Starting from S(0)=0 on a reflected T³ with q₀ at scalar curvature -6,
the exact Einstein Riccati system is:

  S' = -S² + Ric(q_r) + 3I   (shape operator evolution)
  g_r' = 2S g_r              (metric evolution)
  H' = -|S|² + R(q_r) + 9    (mean curvature)

For the rotating-loop center (d=d*, θ=kz, constant area):
  S'(0) = Ric(q₀)+3I has eigenvalues:
    λ_z = -3  (z-direction)
    λ₊, λ₋  (orbit directions, trace = 6)

This script:
1. Computes S'(0) eigenvalues analytically for all k.
2. Sets up and solves the z-independent (VII₀ limit) evolution ODE.
3. Tracks H(r), S eigenvalues, orbit-map d(r), and the tail-interface distance.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigvalsh
import json
from pathlib import Path

def periodic_deriv(f, h):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2*h)

def compute_S_prime_0(k):
    """Compute S'(0) eigenvalues for rotating loop with winding k."""
    sd2 = 12.0 / k**2
    sd = np.sqrt(sd2)
    d_star = np.arcsinh(sd)
    cd = np.cosh(d_star)
    
    Nz = 1024
    z = np.linspace(0, 2*np.pi, Nz, endpoint=False)
    dz = z[1] - z[0]
    
    theta = k * z
    ct, st = np.cos(theta), np.sin(theta)
    
    G11 = cd + sd*ct
    G12 = sd*st
    G22 = cd - sd*ct
    
    dG11 = periodic_deriv(G11, dz)
    dG12 = periodic_deriv(G12, dz)
    dG22 = periodic_deriv(G22, dz)
    ddG11 = periodic_deriv(dG11, dz)
    ddG12 = periodic_deriv(dG12, dz)
    ddG22 = periodic_deriv(dG22, dz)
    
    detG = G11*G22 - G12**2
    Gi11, Gi12, Gi22 = G22/detG, -G12/detG, G11/detG
    
    A11 = 0.5*(Gi11*dG11 + Gi12*dG12)
    A12 = 0.5*(Gi11*dG12 + Gi12*dG22)
    A21 = 0.5*(Gi12*dG11 + Gi22*dG12)
    A22 = 0.5*(Gi12*dG12 + Gi22*dG22)
    
    h_tr = A11 + A22
    trA2 = A11**2 + A12*A21 + A21*A12 + A22**2
    
    # Ric_zz = -|A|² (for h=0)
    Ric_zz = -trA2.mean()
    
    # Full Christoffel orbit Ricci
    Ric_11 = -0.5*ddG11 + 0.5*(dG11*A11+dG12*A21 + dG11*A11+dG12*A21)
    Ric_12 = -0.5*ddG12 + 0.5*(dG11*A12+dG12*A22 + dG12*A11+dG22*A21)
    Ric_22 = -0.5*ddG22 + 0.5*(dG12*A12+dG22*A22 + dG12*A12+dG22*A22)
    
    Rm11 = Gi11*Ric_11 + Gi12*Ric_12
    Rm12 = Gi11*Ric_12 + Gi12*Ric_22
    Rm21 = Gi12*Ric_11 + Gi22*Ric_12
    Rm22 = Gi12*Ric_12 + Gi22*Ric_22
    
    S11 = Rm11 + 3.0; S22 = Rm22 + 3.0
    S12 = Rm12; S21 = Rm21
    
    Str = S11 + S22
    Sdet = S11*S22 - S12*S21
    Sdisc = np.maximum(Str**2 - 4*Sdet, 0)
    eig_plus = (Str + np.sqrt(Sdisc))/2
    eig_minus = (Str - np.sqrt(Sdisc))/2
    
    return {
        'k': k,
        'd_star': d_star,
        'sinh_d': sd,
        'cosh_d': cd,
        'Ric_zz': float(Ric_zz),
        'S_z': float(Ric_zz + 3),
        'S_orbit_plus': float(eig_plus.mean()),
        'S_orbit_minus': float(eig_minus.mean()),
        'S_orbit_plus_var': float(eig_plus.std()),
        'S_orbit_minus_var': float(eig_minus.std()),
        'S_min': float(min(Ric_zz+3, eig_minus.mean())),
        'S_trace': float(Ric_zz+3+eig_plus.mean()+eig_minus.mean()),
    }

def evolve_vii0(k, r_max=10.0, dr=0.001):
    """
    Evolve the z-independent (Bianchi VII₀) reflected Einstein system.
    
    For the VII₀ metric g=dr²+a²dz²+b²ω₁²+c²ω₂² with coframe freq k₇₈=k/2:
    Variables: (a, a', b, b', c, c')
    
    The reflected center has:
    a(0)=a₀, a'(0)=0, b(0)=b₀=e^{d*/2}, c(0)=c₀=e^{-d*/2}, b'(0)=c'(0)=0.
    
    where k²sinh²d*=12, and we set a₀=1 (z-circle normalization).
    
    The slice curvature K=2k₇₈²a⁻²sinh²d, d=log(b/c).
    """
    sd2 = 12.0 / k**2
    sd = np.sqrt(sd2)
    d_star = np.arcsinh(sd)
    cd = np.cosh(d_star)
    
    # For Bianchi VII₀ with coframe frequency k78:
    # The orbit-matrix eigenframe rotates at k78 = k/2 in z.
    # The intrinsic slice curvature K = 2*k78^2 * a^{-2} * sinh^2(d)
    # where d = log(b/c).
    k78 = k / 2.0
    
    b0 = np.exp(d_star/2)
    c0 = np.exp(-d_star/2)
    a0 = 1.0
    
    # State: y = [a, a', b, b', c, c']
    y0 = [a0, 0.0, b0, 0.0, c0, 0.0]
    
    # Einstein equations Ric = -3g for VII₀:
    # u=a'/a, v=b'/b, w=c'/c, H=u+v+w
    # d=log(b/c), K=2k78^2*a^{-2}*sinh^2(d)
    # L = K*coth(d) (for sinh d > 0)
    #
    # u' = 3-K-u*H        (Ric_zz = -3)
    # v' = 3+L-v*H         (Ric_11 = -3) [orbit eigenvalue aligned with b]
    # w' = 3-L-w*H          (Ric_22 = -3) [orbit eigenvalue aligned with c]
    # H' = |S|^2 - 3  where |S|^2 = u^2+v^2+w^2 ... wait
    
    # Actually the standard ODE for Einstein manifolds with cohomogeneity one:
    # For g=dr²+a²dz²+b²ω₁²+c²ω₂²:
    # Ric_{rr} = -(a''/a + b''/b + c''/c) = -3
    # Ric_{zz} = -(a''/a + a'(b'/b+c'/c) + a²-K) * a² ... no.
    
    # Let me use the Einstein equations from Step 78 directly.
    # From the Step 78 note: with u=a'/a, v=b'/b, w=c'/c, H=u+v+w:
    # Ric_rr = -(u'+u²) - (v'+v²) - (w'+w²) = -3
    # Ric_zz/a² = -(u'+Hu) + 3 - K = -3 ... so u'+Hu = 6-K
    # Ric_11/b² = -(v'+Hv) + 3 + L = -3 ... so v'+Hv = 6+L
    # Ric_22/c² = -(w'+Hw) + 3 - L = -3 ... so w'+Hw = 6-L
    
    # Hmm, but these should give Ric_{ii} = -3g_{ii}, so:
    # Ric_zz = -3a², Ric_11 = -3b², Ric_22 = -3c²
    
    # From Step 78 equations (2.4-2.6):
    # u' + Hu = 3 - K (eq 2.4, Ric_zz component)
    # d'' + Hd' = 2K coth d (eq 2.5)
    # (log K)' = -2u + 2 coth(d) d' (eq 2.6)
    
    # where H = u+v+w, d = log(b/c), v=(d'+h)/2, w=(-d'+h)/2 with h=v+w=(log(bc))'/(bc).
    # Actually v=b'/b, w=c'/c, so d'=v-w, h_orb=v+w.
    # H = u + h_orb.
    
    # The constraint (Ric_rr = -3):
    # u'+u² + v'+v² + w'+w² = 3
    
    # Let me use the state vector [a, da, σ, dσ, d, dd] where:
    # σ = log(bc) = orbit area log, u=da/a, h_orb=dσ, H=u+h_orb
    # v = (dσ+dd)/2, w = (dσ-dd)/2
    
    def rhs(r, y):
        a, da, sig, dsig, d, dd = y
        if a < 1e-10 or np.cosh(d) > 1e10:
            return [0]*6
        
        u = da / a
        h_orb = dsig  # d(log(bc))/dr
        H = u + h_orb
        
        # Slice curvature
        shd = np.sinh(d) if abs(d) > 1e-12 else d
        chd = np.cosh(d)
        K = 2 * k78**2 * a**(-2) * shd**2
        if abs(d) > 1e-12:
            L = K * chd / shd
        else:
            L = 2 * k78**2 * a**(-2) * d * chd  # limit
        
        # From u'+Hu = 3-K:
        du = (3 - K) - H*u
        dda = du * a + da * u  # a'' = a(u'+u²) = a(du + u²)
        # Actually: da = a*u, so d(da)/dr = da*u + a*du. And a' = da.
        # du = da'/a - (da/a)² = (a*a''-a'^2)/a² = a''/a - u²
        # So a'' = a(du+u²).
        
        # From d''+Hd'=2K coth d:
        if abs(d) > 1e-12:
            ddd = 2*K*chd/shd - H*dd
        else:
            ddd = 2*K*chd/d - H*dd if abs(d) > 1e-15 else 12*k78**2*a**(-2) - H*dd
        
        # From the constraint and the area equation:
        # v'+v² + w'+w² = 3 - (u'+u²)
        # where v=(dsig+dd)/2, w=(dsig-dd)/2
        # Also: H'+H² = 3 (from Ric_rr=-3 and the identity)
        # No: -(u'+u²)-(v'+v²)-(w'+w²)=-3, so u'+u²+v'+v²+w'+w²=3.
        # H' = -|S|²+something... Let me use:
        # v'+Hv = 3+L (from Step 78 pattern)  => no, let me re-derive.
        
        # Actually from the full Einstein:
        # The orbit Ricci for the VII₀ metric:
        # Ric_{ω₁ω₁}/b² = -(v'+Hv) + (3+L) where L depends on d and slice curvature
        # Wait, I should use the exact formulas from Step 78.
        
        # From Step 78 note equation (2.3-2.6):
        # Ric_rr = -H' - (u²+v²+w²) = -3
        # Ric_zz/a² = -(u'+Hu) + 3-K = -3  => u'+Hu = 6-K
        # d'' + Hd' = 2K coth d
        # And the orbit equations:
        
        # v = (h_orb+dd)/2, w = (h_orb-dd)/2
        # We need h_orb' (or equivalently dsig'):
        # h_orb = v+w, h_orb' = v'+w'
        # From Ric_rr: u'+u²+v'+v²+w'+w²=3
        # u'+u² = du+u² (we know du already)
        # v'+v² = ?
        # We have: v² + w² = (h_orb²+dd²)/2
        # v'+w' = h_orb'
        # From u'+u²+v'+v²+w'+w²=3:
        # du+u² + h_orb' + (h_orb²+dd²)/2 = 3
        # So h_orb' = 3-du-u²-(h_orb²+dd²)/2
        
        v = (h_orb + dd)/2
        w = (h_orb - dd)/2
        
        ddsig = 3 - du - u**2 - (h_orb**2 + dd**2)/2
        # Check: this should equal v'+w'. 
        # And v²+w² = (h_orb²+dd²)/2. OK.
        
        # Verify: H' = du + ddsig. And H'+|S|² = 3 where |S|²=u²+v²+w².
        # H' = du+ddsig = du + 3-du-u²-(h_orb²+dd²)/2 = 3-u²-(h_orb²+dd²)/2
        # |S|² = u²+(h_orb²+dd²)/2
        # H'+|S|² = 3. Good.
        
        return [da, a*(du+u**2), dsig, ddsig, dd, ddd]
    
    # Initial conditions
    y0_ode = [a0, 0.0, np.log(b0*c0), 0.0, d_star, 0.0]
    
    # Solve
    def event_singular(r, y):
        return y[0] - 1e-8  # a -> 0
    event_singular.terminal = True
    
    def event_expand(r, y):
        return y[1]/y[0] + y[3] - 3.0  # H = u+h_orb = 3 (tail value)
    event_expand.terminal = False
    
    sol = solve_ivp(rhs, [0, r_max], y0_ode, method='RK45', 
                    max_step=dr, dense_output=True, events=[event_singular, event_expand],
                    rtol=1e-10, atol=1e-12)
    
    r = sol.t
    a, da, sig, dsig, d, dd = sol.y
    u = da/a
    H = u + dsig
    v = (dsig + dd)/2
    w = (dsig - dd)/2
    S_sq = u**2 + v**2 + w**2
    K = 2*k78**2*a**(-2)*np.sinh(d)**2
    
    # Shape operator eigenvalues (in the eigenframe):
    # The three eigenvalues of S are: u (z-direction), v (ω₁), w (ω₂)
    
    # Check: S-I for the tail interface
    S_minus_I_max = np.maximum(np.abs(u-1), np.maximum(np.abs(v-1), np.abs(w-1)))
    
    return {
        'k': k,
        'd_star': float(d_star),
        'r_max_reached': float(r[-1]),
        'r': r.tolist(),
        'H': H.tolist(),
        'u': u.tolist(),
        'v_orb': v.tolist(),
        'w_orb': w.tolist(),
        'd': d.tolist(),
        'K': K.tolist(),
        'a': a.tolist(),
        'S_minus_I_max': S_minus_I_max.tolist(),
    }

def main():
    results = {}
    
    # Part 1: S'(0) eigenvalues
    print("=== S'(0) eigenvalues for rotating loop centers ===")
    sp0_list = []
    for k in [1, 2, 3, 4, 6, 8, 12]:
        sp0 = compute_S_prime_0(k)
        sp0_list.append(sp0)
        print(f"k={k:2d}: d*={sp0['d_star']:.4f}, S'_z={sp0['S_z']:.3f}, "
              f"orbit=({sp0['S_orbit_plus']:.3f}, {sp0['S_orbit_minus']:.3f}), "
              f"min={sp0['S_min']:.3f}")
    results['S_prime_0'] = sp0_list
    
    # Analytical check: for large k, orbit eigenvalues -> 3
    # For general k: orbit trace = 6, orbit product = ?
    # From the formula: Ric_orbit = -(1/2)ddG + (1/2)(dGA + dGA^T)
    # For the rotating loop: all quantities are equivariant, so eigenvalues are constant.
    # The orbit S' eigenvalues should be 3 ± f(d*) where f is some function.
    
    # Part 2: VII₀ evolution
    print("\n=== VII₀ reflected Einstein evolution ===")
    evo_list = []
    for k in [2, 3, 4, 6, 8]:
        evo = evolve_vii0(k, r_max=5.0, dr=0.0005)
        r = np.array(evo['r'])
        H = np.array(evo['H'])
        d = np.array(evo['d'])
        a = np.array(evo['a'])
        K = np.array(evo['K'])
        
        # Find key radii
        # r where H reaches minimum
        iH_min = np.argmin(H)
        # r where a reaches minimum (or collapses)
        ia_min = np.argmin(a)
        
        # Sample at r=0.5, 1.0, 2.0
        r_samples = [0.0, 0.5, 1.0, 2.0, 3.0]
        samples = {}
        for rs in r_samples:
            idx = np.argmin(np.abs(r - rs))
            if idx < len(r):
                samples[f"r={rs:.1f}"] = {
                    'H': float(H[idx]), 
                    'a': float(a[idx]),
                    'd': float(d[idx]),
                    'K': float(K[idx]),
                    'u': float(evo['u'][idx]),
                    'v': float(evo['v_orb'][idx]),
                    'w': float(evo['w_orb'][idx]),
                }
        
        summary = {
            'k': k,
            'd_star': evo['d_star'],
            'r_max': float(r[-1]),
            'H_min': float(H.min()),
            'H_min_r': float(r[iH_min]),
            'a_min': float(a.min()),
            'a_min_r': float(r[ia_min]),
            'd_final': float(d[-1]),
            'K_final': float(K[-1]),
            'samples': samples,
        }
        evo_list.append(summary)
        
        print(f"k={k}: r_max={r[-1]:.3f}, H_min={H.min():.3f} at r={r[iH_min]:.3f}, "
              f"a_min={a.min():.4f}, d_final={d[-1]:.3f}, K_final={K[-1]:.1f}")
    
    results['evolution'] = evo_list
    
    # Part 3: Detailed k=2 evolution (the most studied case)
    evo2 = evolve_vii0(2, r_max=5.0, dr=0.0001)
    r2 = np.array(evo2['r'])
    H2 = np.array(evo2['H'])
    d2 = np.array(evo2['d'])
    a2 = np.array(evo2['a'])
    u2 = np.array(evo2['u'])
    v2 = np.array(evo2['v_orb'])
    w2 = np.array(evo2['w_orb'])
    K2 = np.array(evo2['K'])
    
    # Check the Step 78 barrier: u < 0, d' > 0, K > K(0)
    print(f"\n--- k=2 detailed ---")
    print(f"max u: {u2.max():.6f} (should be < 0)")
    dd2 = np.array(evo2['d']); # d' > 0?
    dd2_deriv = np.gradient(d2, r2)
    print(f"min d': {dd2_deriv[1:].min():.6f} (should be > 0)")
    print(f"min K-K(0): {(K2-K2[0]).min():.6f} (should be > 0)")
    
    # The tail interface requires: H ≈ 3, S ≈ I (u≈1, v≈1, w≈1)
    # and scaled intrinsic Ric close to 0.
    # How far is the solution from this?
    SI_max = np.maximum(np.abs(u2-1), np.maximum(np.abs(v2-1), np.abs(w2-1)))
    print(f"||S-I||_max at r=2: {SI_max[np.argmin(np.abs(r2-2))]:.3f}")
    print(f"||S-I||_max at r=5: {SI_max[-1]:.3f}")
    
    results['k2_detailed'] = {
        'r': r2[::10].tolist(),
        'H': H2[::10].tolist(),
        'u': u2[::10].tolist(),
        'v': v2[::10].tolist(),
        'w': w2[::10].tolist(),
        'd': d2[::10].tolist(),
        'K': K2[::10].tolist(),
        'a': a2[::10].tolist(),
    }
    
    # Part 4: Background d''(0) for each k
    print(f"\n=== Initial accelerations ===")
    for k in [1, 2, 3, 4, 8]:
        sd = np.sqrt(12.0/k**2)
        d_star = np.arcsinh(sd)
        cd = np.cosh(d_star)
        K0 = 6.0  # by construction
        L0 = K0 * cd / sd
        k78 = k/2
        # d''(0) = 2K coth d = 2K0 * cd/sd
        d_pp = 2*K0*cd/sd
        # Background H'(0) = -3
        # u'(0) = 3-K0 - 0 = -3
        # For angular slip at mode k̃ < k:
        print(f"k={k}: d*={d_star:.3f}, d''(0)={d_pp:.3f}, "
              f"coth(d*)={cd/sd:.3f}")
        # The angular slip A''(0) = (k̃²-k²)A(0)
        for kt in range(1, min(k, 5)):
            Ap = (kt**2 - k**2)
            print(f"  k̃={kt}: A''(0)/A(0)={Ap}, ratio to d''(0): {abs(Ap)/d_pp:.3f}")
    
    out = Path(__file__).resolve().parents[1] / 'data' / 'step81_evolution.json'
    out.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"\nwrote {out}")

if __name__ == '__main__':
    main()
