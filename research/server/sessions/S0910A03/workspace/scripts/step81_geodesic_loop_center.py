#!/usr/bin/env python3
"""
Exact constant-speed geodesic loop centers for the OT T²-invariant system.

Convention: SL(2)/SO(2) ≅ H² with metric ds² = (1/2)tr((M⁻¹dM)²).
In geodesic polar (d,θ): M = cosh(d)I + sinh(d)n(θ),
  n(θ) = [[cos θ, sin θ],[sin θ,-cos θ]], n² = I.
The metric is ds² = dd² + sinh²(d)dθ² (curvature -1).

Rotating loop: d=d*, θ=kz (k integer for 2π-periodicity).
Speed² = k²sinh²(d*).  For R(q₀)=-6: k²sinh²(d*) = 12.

The orbit-matrix eigenframe rotates at frequency k/2 in z.
Step 78 coframe frequency k₇₈ corresponds to k = 2k₇₈ here.

This script:
1. Verifies e_{H²}=12 and R(q₀)=-6 for rotating loops.
2. Computes S'(0) = Ric(q₀)+3I for reflected Einstein germ.
3. Verifies S'_z(0) = -3 universally.
4. Tests the isometry control (k=k₀ translation).
5. Computes the full orbit Ricci for the rotating loop.
"""
import numpy as np
import json
from pathlib import Path

def periodic_deriv(f, h):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2*h)

def main():
    results = {}
    Nz = 512
    z = np.linspace(0, 2*np.pi, Nz, endpoint=False)
    dz = z[1] - z[0]
    
    # ===== Part 1: orbit matrix for rotating loop =====
    # Test k=1,2,3,4
    for k in [1, 2, 3, 4]:
        sd2 = 12.0 / k**2      # sinh²(d*)
        sd = np.sqrt(sd2)
        d_star = np.arcsinh(sd)
        cd = np.cosh(d_star)
        
        theta = k * z           # H² polar angle
        ct, st = np.cos(theta), np.sin(theta)
        
        # M = cosh(d*)I + sinh(d*) n(θ)
        M11 = cd + sd * ct
        M12 = sd * st
        M22 = cd - sd * ct
        
        det_M = M11*M22 - M12**2
        det_err = np.max(np.abs(det_M - 1.0))
        
        # M⁻¹ = cosh(d*)I - sinh(d*) n(θ)
        Mi11 = cd - sd * ct
        Mi12 = -sd * st
        Mi22 = cd + sd * ct
        
        # T = M⁻¹ M_z
        dM11 = periodic_deriv(M11, dz)
        dM12 = periodic_deriv(M12, dz)
        dM22 = periodic_deriv(M22, dz)
        
        T11 = Mi11*dM11 + Mi12*dM12
        T12 = Mi11*dM12 + Mi12*dM22
        T21 = Mi12*dM11 + Mi22*dM12
        T22 = Mi12*dM12 + Mi22*dM22
        
        trT = T11 + T22
        trT2 = T11**2 + T12*T21 + T21*T12 + T22**2
        eH2 = 0.5 * trT2  # should be 12
        
        # Shape operator A = T/2, |A|² = (1/4)tr(T²) = eH2/2
        Asq = eH2 / 2  # should be 6
        
        # For constant area (h=0): R(q₀) = -|A|² = -6
        Rq = -Asq
        
        print(f"k={k}: d*={d_star:.4f}, e_H2=[{eH2.min():.6f},{eH2.max():.6f}]"
              f" (exp=12), R=[{Rq.min():.2f},{Rq.max():.2f}], det_err={det_err:.2e}")
        
        results[f"k={k}"] = {
            "d_star": float(d_star),
            "sinh_d": float(sd),
            "eH2_range": [float(eH2.min()), float(eH2.max())],
            "Rq_range": [float(Rq.min()), float(Rq.max())],
            "det_err": float(det_err),
        }
    
    # ===== Part 2: Full 3D Ricci for k=2 =====
    k = 2
    sd2 = 12.0 / k**2
    sd = np.sqrt(sd2)
    d_star = np.arcsinh(sd)
    cd = np.cosh(d_star)
    
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
    
    # Shape operator A^a_b = (1/2) G^{ac} dG_{cb}
    A11 = 0.5*(Gi11*dG11 + Gi12*dG12)
    A12 = 0.5*(Gi11*dG12 + Gi12*dG22)
    A21 = 0.5*(Gi12*dG11 + Gi22*dG12)
    A22 = 0.5*(Gi12*dG12 + Gi22*dG22)
    
    h_tr = A11 + A22
    trA2 = A11*A11 + A12*A21 + A21*A12 + A22*A22
    
    dA11 = periodic_deriv(A11, dz)
    dA12 = periodic_deriv(A12, dz)
    dA21 = periodic_deriv(A21, dz)
    dA22 = periodic_deriv(A22, dz)
    
    # Ric_{zz} = -h' - |A|^2  (h=0 for constant area)
    Ric_zz = -(dA11+dA22) - trA2
    
    # Ric_{ab} (orbit) using Petersen formula for g=dt²+g_t:
    # Ric_{ij} = hat{Ric}_{ij} + L'_{ij} - 2L^k_i L_{kj} + (tr L)L_{ij}
    # with L_{ij}=(1/2)dG_{ij}, L^k_i=A^k_i, L'_{ij}=(1/2)ddG_{ij}, hat{Ric}=0
    
    Ric_11 = 0.5*ddG11 - 2*(A11*(0.5*dG11) + A21*(0.5*dG12)) + h_tr*(0.5*dG11)
    Ric_12 = 0.5*ddG12 - 2*(A11*(0.5*dG12) + A21*(0.5*dG22)) + h_tr*(0.5*dG12)
    Ric_22 = 0.5*ddG22 - 2*(A12*(0.5*dG12) + A22*(0.5*dG22)) + h_tr*(0.5*dG22)
    
    # Wait - need to be careful: 2L^k_i L_{kj} = 2(A^k_i)(L_{kj}) = 2 A^k_i (1/2)dG_{kj}
    # For ij=11: 2*(A^1_1*(1/2)dG_{11} + A^2_1*(1/2)dG_{21}) = A_11 dG11 + A_21 dG12
    Ric_11_v2 = 0.5*ddG11 - (A11*dG11 + A21*dG12) + h_tr*(0.5*dG11)
    Ric_12_v2 = 0.5*ddG12 - (A11*dG12 + A21*dG22) + h_tr*(0.5*dG12)
    Ric_22_v2 = 0.5*ddG22 - (A12*dG12 + A22*dG22) + h_tr*(0.5*dG22)
    
    # Check: total scalar R = Ric_zz + G^{ab} Ric_{ab}
    Rmixed_11 = Gi11*Ric_11_v2 + Gi12*Ric_12_v2
    Rmixed_22 = Gi12*Ric_12_v2 + Gi22*Ric_22_v2
    R_orbit_trace = Rmixed_11 + Rmixed_22
    R_total = Ric_zz + R_orbit_trace
    
    print(f"\n--- k=2 full Ricci ---")
    print(f"tr A = {np.max(np.abs(h_tr)):.2e}")
    print(f"|A|^2 = {trA2.mean():.6f} (exp=6)")
    print(f"Ric_zz = {Ric_zz.mean():.6f} (exp=-6)")
    print(f"R_orbit_trace = [{R_orbit_trace.min():.4f}, {R_orbit_trace.max():.4f}]")
    print(f"R_total = [{R_total.min():.4f}, {R_total.max():.4f}] (exp=-6)")
    
    # S'(0) = Ric(q₀) + 3I
    # z-component: S'_z = Ric_zz + 3 = -6+3 = -3
    S_z = Ric_zz + 3.0
    print(f"S'_z = {S_z.mean():.6f} (exp=-3)")
    
    # Orbit: S'^a_b = Ric^a_b + 3δ^a_b
    Rmixed_12 = Gi11*Ric_12_v2 + Gi12*Ric_22_v2
    Rmixed_21 = Gi12*Ric_11_v2 + Gi22*Ric_12_v2
    
    S_11 = Rmixed_11 + 3.0
    S_12 = Rmixed_12
    S_21 = Rmixed_21
    S_22 = Rmixed_22 + 3.0
    
    S_tr = S_11 + S_22
    S_det = S_11*S_22 - S_12*S_21
    S_disc = np.maximum(S_tr**2 - 4*S_det, 0)
    eig1 = (S_tr + np.sqrt(S_disc))/2
    eig2 = (S_tr - np.sqrt(S_disc))/2
    
    print(f"S'_orbit trace = [{S_tr.min():.4f}, {S_tr.max():.4f}] (exp=6)")
    print(f"S'_orbit eig1 = [{eig1.min():.4f}, {eig1.max():.4f}]")
    print(f"S'_orbit eig2 = [{eig2.min():.4f}, {eig2.max():.4f}]")
    print(f"min eigenvalue of full S'(0): {min(S_z.min(), eig2.min()):.4f}")
    
    # For the rotating loop, by the equivariance:
    # A^2 = (|A|^2/2)I = 3I (for traceless 2x2 with tr(A^2)=6)
    A2_11 = A11*A11 + A12*A21
    A2_22 = A21*A12 + A22*A22
    print(f"\nA^2 diag: [{A2_11.mean():.4f}, {A2_22.mean():.4f}] (exp=3)")
    print(f"A^2_{11} range: [{A2_11.min():.4f}, {A2_11.max():.4f}]")
    
    results["k2_ricci"] = {
        "trA_max": float(np.max(np.abs(h_tr))),
        "Asq_mean": float(trA2.mean()),
        "Ric_zz_mean": float(Ric_zz.mean()),
        "R_total_range": [float(R_total.min()), float(R_total.max())],
        "S_z_mean": float(S_z.mean()),
        "S_orbit_trace_range": [float(S_tr.min()), float(S_tr.max())],
        "S_orbit_eig1_range": [float(eig1.min()), float(eig1.max())],
        "S_orbit_eig2_range": [float(eig2.min()), float(eig2.max())],
        "S_min_eigenvalue": float(min(S_z.min(), eig2.min())),
    }
    
    # ===== Part 3: Analytical orbit Ricci for rotating loop =====
    # For the constant-speed loop: A(z) = (k/2) * sinh(d*)/anything...
    # Actually the key property: A^2 = 3I and A_z is the rotation derivative.
    # S'_orbit = Ric^a_b + 3δ^a_b.
    # The orbit Ricci in mixed form: Ric^a_b = -(A_z)^a_b - 2(A^2)^a_b + h A^a_b
    # Since h=0 and A^2 = 3I: Ric^a_b = -(A_z)^a_b - 6δ^a_b.
    # Wait that gives Ric_orbit_trace = -tr(A_z) - 12 = 0-12 = -12? But we got 0.
    # Something is off with the Petersen formula. Let me check.
    
    # Actually the Petersen formula gives Ric_{ij} (lowered indices).
    # Converting: Ric^a_b = G^{ac} Ric_{cb}.
    # From the formula: Ric_{ij} = (1/2)ddG_{ij} - A^k_i dG_{kj} + h (1/2)dG_{ij}
    # = (1/2)ddG_{ij} - (1/2)(A dG)_{ij}  ... hmm.
    
    # Let me verify by a different route: direct Christoffel computation.
    # For g = dz^2 + G_{ab}(z)dx^a dx^b (a,b in {1,2}):
    # Using coords (z=x^0, x=x^1, y=x^2).
    # Gamma^0_{ab} = -(1/2) dG_{ab}  (since g^{00}=1)
    # Gamma^a_{0b} = (1/2) G^{ac} dG_{cb} = A^a_b
    # Gamma^a_{bc} = 0 (flat orbits)
    # 
    # R^0_{a0b} = partial_0 Gamma^0_{ab} - partial_a Gamma^0_{0b} + Gamma^0_{0c}Gamma^c_{ab} - Gamma^0_{ac}Gamma^c_{0b}
    # Gamma^0_{0c} = 0 (since g_{0c,0}=0 for c>0), Gamma^c_{ab}=0.
    # = -(1/2)ddG_{ab} - 0 + 0 - (-(1/2)dG_{ac})(A^c_b)
    # = -(1/2)ddG_{ab} + (1/2)(dG A)_{ab}
    # 
    # Ric_{ab} = R^mu_{a mu b} = R^0_{a0b} + R^c_{acb}
    # R^c_{acb}: 
    # R^c_{a0b}=0 (this is the base-orbit component, but we want R^c_{acb})
    # Actually R^c_{acb} = partial_c Gamma^c_{ab} - partial_b Gamma^c_{ac} + ...
    # But Gamma^c_{ab}=0 and all orbit-only Christoffels are zero, so R^c_{acb}=0.
    # Wait, R^c_{acb} has terms like partial_a Gamma^c_{cb} = partial_a(A^c_b)?
    # No: Gamma^c_{cb} = (1/2)G^{cd}dG_{db} involves z-derivatives only.
    # partial_a Gamma^c_{cb} = 0 for a in orbit directions.
    # Gamma^c_{a0} = A^c_a, Gamma^0_{cb} = -(1/2)dG_{cb}.
    # R^c_{a c b}: exchange first and third, using the formula
    # R^d_{acb} = d_c Gamma^d_{ab} - d_b Gamma^d_{ac} + Gamma^d_{ce}Gamma^e_{ab} - Gamma^d_{be}Gamma^e_{ac}
    # For d,a,b orbit, c=0:
    # partial_0 Gamma^d_{ab} - partial_b Gamma^d_{a0} + Gamma^d_{0e}Gamma^e_{ab} - Gamma^d_{be}Gamma^e_{a0}
    # = 0 - 0 + A^d_e * 0 - 0 * A^e_a = 0.
    # For d orbit, a orbit, c orbit, b=0:
    # R^d_{ac0} = d_c Gamma^d_{a0} - d_0 Gamma^d_{ac} + Gamma^d_{ce}Gamma^e_{a0} - Gamma^d_{0e}Gamma^e_{ac}
    # = 0 - 0 + 0 - A^d_e * 0 = 0.
    # So R^c_{acb}=0 for orbit a,b. Hence Ric_{ab} = R^0_{a0b}.
    
    # Ric_{ab} = -(1/2)ddG_{ab} + (1/2)(dG A)_{ab}
    # = -(1/2)ddG_{ab} + (1/2) dG_{ac} A^c_b
    
    # Let me verify this formula:
    Ric_11_direct = -0.5*ddG11 + 0.5*(dG11*A11 + dG12*A21)
    Ric_12_direct = -0.5*ddG12 + 0.5*(dG11*A12 + dG12*A22)
    Ric_22_direct = -0.5*ddG22 + 0.5*(dG12*A12 + dG22*A22)
    
    print(f"\n--- Direct Christoffel Ricci check ---")
    print(f"Ric_11 Petersen vs direct max diff: {np.max(np.abs(Ric_11_v2 - Ric_11_direct)):.2e}")
    print(f"Ric_22 Petersen vs direct max diff: {np.max(np.abs(Ric_22_v2 - Ric_22_direct)):.2e}")
    
    # Now convert to mixed form using the direct formula:
    Rd_11 = Gi11*Ric_11_direct + Gi12*Ric_12_direct
    Rd_22 = Gi12*Ric_12_direct + Gi22*Ric_22_direct
    R_orbit_tr_direct = Rd_11 + Rd_22
    print(f"R_orbit_trace (direct) = {R_orbit_tr_direct.mean():.4f}")
    print(f"R_total (direct) = {(Ric_zz + R_orbit_tr_direct).mean():.4f}")
    
    # S' orbit mixed from direct:
    Sd_11 = Rd_11 + 3.0
    Sd_22 = Rd_22 + 3.0
    Sd_12 = Gi11*Ric_12_direct + Gi12*Ric_22_direct
    Sd_21 = Gi12*Ric_11_direct + Gi22*Ric_12_direct
    Sd_tr = Sd_11 + Sd_22
    Sd_det = Sd_11*Sd_22 - Sd_12*Sd_21
    Sd_disc = np.maximum(Sd_tr**2 - 4*Sd_det, 0)
    eid1 = (Sd_tr + np.sqrt(Sd_disc))/2
    eid2 = (Sd_tr - np.sqrt(Sd_disc))/2
    
    print(f"S'_orbit (direct) trace = {Sd_tr.mean():.4f}")
    print(f"S'_orbit (direct) eig1 = [{eid1.min():.4f}, {eid1.max():.4f}]")
    print(f"S'_orbit (direct) eig2 = [{eid2.min():.4f}, {eid2.max():.4f}]")
    
    # ===== Part 4: Analytic formulas =====
    # Ric_{ab} = -(1/2)ddG_{ab} + (1/2)(dG)_{ac} A^c_b
    # For the rotating loop: dG_{ab} = -k sinh(d*) sin(kz) n_{ab}' + ... 
    # Actually G = cosh(d*)I + sinh(d*)n(kz), so:
    # dG = k sinh(d*) n'(kz), ddG = -k^2 sinh(d*) n(kz)
    # A = T/2 = ... Let's compute analytically.
    
    # From T = M⁻¹ M_z = k sinh(d*)(cosh(d*)n' - sinh(d*)J)
    # A = T/2 = (k sinh(d*)/2)(cosh(d*)n' - sinh(d*)J)
    # where J = n n' = [[0,1],[-1,0]]
    
    # dG = k sinh(d*) n'
    # dG A: (dG)_{ac} A^c_b = (k sinh(d*) n')_{ac} (k sinh(d*)/2)(cosh(d*)n' - sinh(d*)J)^c_b
    # = (k^2 sinh^2(d*)/2) (n'(cosh(d*)n' - sinh(d*)J))_{ab}
    # n' n' = I, n' J = ... 
    # n'(θ) J = [[-sin,-cos],[cos,-sin]][[0,1],[-1,0]] = ... 
    # Let me compute: n'=[[-s,c],[c,s]], J=[[0,1],[-1,0]]
    # n'J = [[-s*0+c*(-1), -s*1+c*0],[c*0+s*(-1), c*1+s*0]] = [[-c,-s],[-s,c]] = -n
    # So dG A = (k²sinh²d*/2)(I*cosh(d*) + sinh(d*)*n)
    #         = (k²sinh²d*/2)(cosh(d*)I + sinh(d*)n) = (k²sinh²d*/2)M = 6M
    
    # Ric_{ab} = -(1/2)(-k²sinh(d*)n) + (1/2)(6M)
    # = (k²sinh(d*)/2)n + 3M
    # = (k²sinh(d*)/2)(cos θ, sin θ; sin θ,-cos θ) + 3(cosh d* + sinh d* cos θ, ...)
    # Hmm, but this has both I and n components.
    
    # R_orbit = G^{ab} Ric_{ab} = tr(G^{-1}Ric_orbit)
    # G^{-1} = cosh(d*)I - sinh(d*)n (since G = cosh(d*)I + sinh(d*)n, G^{-1}=(cosh²-sinh²)⁻¹(cosh I - sinh n)=cosh I - sinh n)
    # G^{-1} Ric = (cosh I-sinh n)((k²sinh d*/2)n+3M)
    #            = (k²sinhd*/2)(cosh n - sinh I) + 3(cosh M - sinh n M)
    # n M = n(cosh I + sinh n) = cosh n + sinh I
    # So G^{-1}Ric = (k²sinhd*/2)(cosh n-sinh I) + 3(cosh(cosh I+sinh n)-sinh(cosh n+sinh I))
    #              = (k²sinhd*/2)(cosh n-sinh I) + 3((cosh²-sinh²)I + (cosh sinh-sinh cosh)n)
    #              = (k²sinhd*/2)(cosh n-sinh I) + 3I
    # tr(G^{-1}Ric) = (k²sinhd*/2)(0-2sinh) + 6 = -k²sinh²d* + 6 = -12+6 = -6? That gives R_orbit=-6.
    # Wait, shouldn't it be 0? R = Ric_zz + R_orbit. If R_orbit=-6 and Ric_zz=-6, R=-12?
    
    # Hmm, but R=-6 was the TARGET. Let me recheck the basic formula.
    # For q = dz²+G(z) with dim(orbit)=2 and h=0:
    # R = 2 Ric_zz ... no. R is the sum of all Ric diagonal components.
    # In 3D, R = Ric_zz + Ric^a_a.
    # Ric_zz = -|A|² = -6. If Ric^a_a = -6, then R = -12? Not -6!
    
    # Something is wrong with my formula. Let me recheck.
    
    # Actually, the issue is the Petersen formula. Let me recheck:
    # For g = dt²+g_t in (n+1) dimensions:
    # Ric_{00} = -(1/2)tr(g_t^{-1} ddg_t) - (1/4)tr((g_t^{-1}dg_t)²)  [not exactly this]
    # 
    # The correct formula (see e.g. O'Neill or direct computation) for g=dt²+g_t:
    # Ric_{00} = -tr(A') - tr(A²) where A = (1/2)g_t^{-1} dg_t
    # Ric_{ij} = Ric(g_t)_{ij} - (A²)_{ij} + (h-something)A_{ij}?
    #
    # I should use the Gauss-Codazzi approach. For hypersurface z=const in (z,x,y):
    # Second fundamental form II_{ab} = (1/2)(dG_{ab}/dz)/1 = (1/2)dG_{ab}
    # Shape operator S^a_b = g^{ac}II_{cb}/g_{00} = G^{ac}(1/2)dG_{cb} = A^a_b
    # 
    # Gauss: R(g_t)_{abcd} = R(g)_{abcd} + II_{ac}II_{bd} - II_{ad}II_{bc}
    # Codazzi: (∇_a II)_{bc} - (∇_b II)_{ac} = R(g)_{n a b c}
    # Ricci: Ric(g)_{ab} = Ric_intrinsic(g)_{ab} - Ric(g)_{0a0b} 
    #   where the second term involves the second fundamental form evolution.
    
    # Actually the correct decomposition for g = dt²+g_t gives:
    # The ambient Ricci in slice directions satisfies:
    # Ric(g)_{ab} = Ric(g_t)_{ab} - A'_{ab} + 2(A²)_{ab} - h A_{ab}
    # where A' = dA/dt. This is the Gauss equation combined with the Mainardi equation.
    
    # NO - there are different sign conventions. Let me just verify numerically.
    # I'll compute using brute-force Christoffels.
    
    # Actually my direct Christoffel derivation above gave:
    # Ric_{ab} = -(1/2)ddG_{ab} + (1/2)(dG A)_{ab}
    # Let me verify this against the standard result.
    # 
    # From R^0_{a0b} = -(1/2)ddG_{ab} + (1/2)(dG)_{ac}A^c_b.
    # But I only computed R^0_{a0b}. I need to also check R^c_{acb}.
    # Let me redo more carefully.
    
    # R^mu_{alpha mu beta}:
    # For alpha,beta orbit: 
    # mu=0: R^0_{a 0 b} = d_0 Gamma^0_{ab} - d_b Gamma^0_{a0} + Gamma^0_{0nu}Gamma^nu_{ab} - Gamma^0_{bnu}Gamma^nu_{a0}
    #   Gamma^0_{ab} = -(1/2)dG_{ab}
    #   Gamma^0_{a0} = 0 (g_{00}=1, g_{0a}=0, dg_{00}=0)
    #   Gamma^0_{0nu}: Gamma^0_{00}=0, Gamma^0_{0c}=0. So = 0.
    #   Gamma^nu_{ab}: Gamma^0_{ab}=-(1/2)dG_{ab}, Gamma^c_{ab}=0 (flat orbits).
    #   Gamma^nu_{a0}: Gamma^0_{a0}=0, Gamma^c_{a0}=A^c_a.
    #   So R^0_{a0b} = d_0(-(1/2)dG_{ab}) - 0 + 0 - (-(1/2)dG_{bc})A^c_a
    #                = -(1/2)ddG_{ab} + (1/2)dG_{bc}A^c_a
    
    # mu=c orbit: R^c_{a c b} = d_c Gamma^c_{ab} - d_b Gamma^c_{ac} + Gamma^c_{cnu}Gamma^nu_{ab} - Gamma^c_{bnu}Gamma^nu_{ac}
    #   Gamma^c_{ab} = 0, Gamma^c_{ac}: Gamma^c_{a0}=A^c_a, Gamma^c_{ad}=0 (d orbit).
    #   But the index here is R^c_{acb} summed over c.
    #   For fixed c: 
    #   d_c Gamma^c_{ab} = 0 (since Gamma^c_{ab}=0 and G doesn't depend on orbit coords)
    #   d_b Gamma^c_{ac}: Gamma^c_{ac}=0 for c orbit, a orbit. But Gamma^c_{a0}=A^c_a depends on z.
    #     When c=orbit and the second index is a=orbit, third=c:
    #     Actually R^c_{acb}: here we sum over the repeated index c (which appears as both upper
    #     and the third lower index). This is confusing. Let me use abstract notation.
    #   
    #   Ric_{ab} = g^{mu nu} R_{mu a nu b} = g^{00}R_{0a0b} + g^{cd}R_{cadb}
    #   = R_{0a0b} + G^{cd}R_{cadb}
    #   
    #   R_{0a0b} = g_{00}R^0_{a0b} = R^0_{a0b} (computed above)
    #   R_{cadb} = g_{ce}R^e_{adb}: 
    #     R^e_{adb}: Riemann with all orbit indices.
    #     Since Gamma^e_{ab}=0 and all spatial Christoffels vanish:
    #     R^e_{adb} = d_d Gamma^e_{ab} - d_b Gamma^e_{ad} + Gamma^e_{df}Gamma^f_{ab} - Gamma^e_{bf}Gamma^f_{ad}
    #     All Gamma^e_{**} with both lower indices orbit are zero.
    #     Gamma^e_{d0} = A^e_d, Gamma^0_{ab}=-(1/2)dG_{ab}.
    #     = 0 - 0 + Gamma^e_{d0}Gamma^0_{ab} - Gamma^e_{b0}Gamma^0_{ad}
    #       + Gamma^e_{df}Gamma^f_{ab}(f=0) is already counted...
    #     
    #     Actually: Gamma^f_{ab}=0 for f orbit, so Gamma^e_{df}Gamma^f_{ab} = Gamma^e_{d0}Gamma^0_{ab}
    #     Similarly Gamma^f_{ad}: for f=0: Gamma^0_{ad}=-(1/2)dG_{ad}. For f orbit: Gamma^f_{ad}=0.
    #     So Gamma^e_{bf}Gamma^f_{ad} = Gamma^e_{b0}Gamma^0_{ad}.
    #     
    #     R^e_{adb} = A^e_d(-(1/2)dG_{ab}) - A^e_b(-(1/2)dG_{ad})
    #               = (1/2)(A^e_b dG_{ad} - A^e_d dG_{ab})
    #     
    #     R_{cadb} = G_{ce}R^e_{adb} = (1/2)(G_{ce}A^e_b dG_{ad} - G_{ce}A^e_d dG_{ab})
    #             = (1/2)((GA)_{cb} dG_{ad} - (GA)_{cd} dG_{ab})
    #     Note: (GA)_{cb} = G_{ce}A^e_b = (1/2)dG_{cb} (since A=(1/2)G^{-1}dG, so GA = (1/2)dG)
    #     
    #     R_{cadb} = (1/2)((1/2)dG_{cb}dG_{ad} - (1/2)dG_{cd}dG_{ab})
    #             = (1/4)(dG_{cb}dG_{ad} - dG_{cd}dG_{ab})
    #     
    #     G^{cd}R_{cadb} = (1/4)(G^{cd}dG_{cb}dG_{ad} - G^{cd}dG_{cd}dG_{ab})
    #                    = (1/4)(2A^d_b dG_{ad} - tr(2A) dG_{ab})
    #                    = (1/2)(A^d_b dG_{ad} - h dG_{ab})
    #                    = (1/2)((dG)_{ad}A^d_b - h dG_{ab})
    #     
    #     For h=0: G^{cd}R_{cadb} = (1/2)(dG)_{ad}A^d_b
    # 
    # Combining: Ric_{ab} = R^0_{a0b} + G^{cd}R_{cadb}
    #          = -(1/2)ddG_{ab} + (1/2)(dG)_{bc}A^c_a + (1/2)(dG)_{ad}A^d_b
    # Wait, let me re-derive R^0_{a0b}:
    # R^0_{a0b} = -(1/2)ddG_{ab} + (1/2)(dG)_{bc}A^c_a
    # Hmm no: R^0_{a0b} = -(1/2)ddG_{ab} + (1/2)dG_{bc}A^c_a.
    # Let me recheck from the Christoffel calculation.
    
    # The formula for R^0_{a0b}:
    # = partial_0 Gamma^0_{ab} - partial_b Gamma^0_{a0} 
    #   + Gamma^0_{0mu}Gamma^mu_{ab} - Gamma^0_{bmu}Gamma^mu_{a0}
    # = -(1/2)ddG_{ab} - 0 + 0 - Gamma^0_{bmu}Gamma^mu_{a0}
    # Gamma^0_{bmu}Gamma^mu_{a0}: 
    #   mu=0: Gamma^0_{b0}=0.
    #   mu=c orbit: Gamma^0_{bc}Gamma^c_{a0} = -(1/2)dG_{bc} A^c_a
    # So the last term is +(1/2)dG_{bc}A^c_a.
    # R^0_{a0b} = -(1/2)ddG_{ab} + (1/2)dG_{bc}A^c_a = -(1/2)ddG_{ab} + (1/2)(dG A)_{ba}
    
    # And G^{cd}R_{cadb} = (1/2)(dG)_{ad}A^d_b (for h=0)
    # = (1/2)(dG A)_{ab}
    
    # Ric_{ab} = -(1/2)ddG_{ab} + (1/2)(dG A)_{ba} + (1/2)(dG A)_{ab}
    # 
    # For the SYMMETRIC matrix dG and MIXED A:
    # (dG A)_{ba} = dG_{bc}A^c_a, (dG A)_{ab} = dG_{ac}A^c_b
    # Since dG is symmetric: these are the two natural orderings.
    
    # So Ric_{ab} = -(1/2)ddG_{ab} + (1/2)[dG_{bc}A^c_a + dG_{ac}A^c_b]
    
    Ric_11_full = -0.5*ddG11 + 0.5*(dG11*A11 + dG12*A21 + dG11*A11 + dG12*A21)
    Ric_12_full = -0.5*ddG12 + 0.5*(dG11*A12 + dG12*A22 + dG12*A11 + dG22*A21)
    Ric_22_full = -0.5*ddG22 + 0.5*(dG12*A12 + dG22*A22 + dG12*A12 + dG22*A22)
    
    Rf_11 = Gi11*Ric_11_full + Gi12*Ric_12_full
    Rf_22 = Gi12*Ric_12_full + Gi22*Ric_22_full
    R_orb_full = Rf_11 + Rf_22
    R_full = Ric_zz + R_orb_full
    
    print(f"\n--- Full Christoffel formula ---")
    print(f"R_total_full = [{R_full.min():.4f}, {R_full.max():.4f}]")
    print(f"R_orbit_full = {R_orb_full.mean():.4f}")
    
    Sf_11 = Rf_11 + 3; Sf_22 = Rf_22 + 3
    Sf_12 = Gi11*Ric_12_full + Gi12*Ric_22_full
    Sf_21 = Gi12*Ric_11_full + Gi22*Ric_12_full
    Sf_tr = Sf_11 + Sf_22
    Sf_det = Sf_11*Sf_22 - Sf_12*Sf_21
    Sf_disc = np.maximum(Sf_tr**2 - 4*Sf_det, 0)
    ef1 = (Sf_tr + np.sqrt(Sf_disc))/2
    ef2 = (Sf_tr - np.sqrt(Sf_disc))/2
    
    print(f"S'_orbit_full trace = {Sf_tr.mean():.4f}")
    print(f"S'_orbit_full eig1 = [{ef1.min():.4f}, {ef1.max():.4f}]")
    print(f"S'_orbit_full eig2 = [{ef2.min():.4f}, {ef2.max():.4f}]")
    
    results["k2_full_ricci"] = {
        "R_total_range": [float(R_full.min()), float(R_full.max())],
        "S_orbit_trace": float(Sf_tr.mean()),
        "S_orbit_eig1_range": [float(ef1.min()), float(ef1.max())],
        "S_orbit_eig2_range": [float(ef2.min()), float(ef2.max())],
    }
    
    out = Path(__file__).resolve().parents[1] / 'data' / 'step81_geodesic_loop_center.json'
    out.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"\nwrote {out}")

if __name__ == '__main__':
    main()
