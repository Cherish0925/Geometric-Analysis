#!/usr/bin/env python3
"""Step 63: Adjudicate the IL m=1 collar term.

Binary question: does the m=1 signed-Hessian term
    J_1 = int chi (nabla_i nabla_j chi) B^{ij}(U_1)
close by one integration by parts with only ||nabla chi||_inf,
or is there a genuinely unclosed collar/current term?

Gate test: the Step-52 flat-T^4 witness with chi=(1+cos x1)/2.
On that example, ||Ric+g||_op ~ t, but E'/E ~ 2/t (curvature grows from nothing).
Any valid m=1 estimate must NOT predict homogeneous closure on this example.

We check three candidate closure forms:
  (A) Pure signed-Hessian IBP: J_1 -> C1*C1*U1 + chi*C1*nabla U1
      Absorbed by eps*D + C(eps)*||C1||_inf^2 * ||U1||_p^p
  (B) Top-cutoff residual I_1 = int chi |C2| |U1|^p
      For m=1, U1 is CURRENT not base, so Holder(4,p,4,2p/(p-2)) fails
      because ||U1||_4 is not base data.
  (C) Full coupled pair (U1,C2) energy: d/dt(||U1||_p^p + ||C2||_p^p) + cD <= ...
      This is what A01/A03 claim closes.

The flat-T^4 test: on T^4 with g(t) = (1+t*epsilon*cos(kx)) delta_ij + O(t^2),
  a = chi^2, chi = (1+cos x1)/2
  U = a*T where T = Rm + G
  At t=0: T=0, U=0, but dT/dt != 0
  Key: |nabla U1|^2 / |U1|^2 can be arbitrarily large near zeros of chi
  because U1 ~ chi * nabla T + C1 * T, and near chi=0: U1 ~ C1*T
  so nabla U1 ~ C2*T + C1*nabla T
  
The question is whether the weighted dissipation D = int a |nabla U1|^2 |U1|^{p-2}
controls the current terms uniformly as we approach {a=0}.
"""

import json
import numpy as np

def analyze_flat_T4_witness():
    """Analyze the flat-T^4 family as a gate test for m=1 closure.
    
    Setup: T^4 with coordinates (x1,x2,x3,x4), periodic.
    Cutoff: chi = (1+cos(x1))/2, so a = chi^2.
    chi vanishes at x1 = pi, with chi ~ (pi-x1)^2/8 near the zero.
    C1 = dchi/dx1 = -sin(x1)/2, so |C1| ~ |pi-x1|/2 near zero.
    C2 = d^2chi/dx1^2 = -cos(x1)/2, so C2 -> 1/2 at x1=pi.
    
    Metric perturbation: g_ij = delta_ij + t*h_ij(x) where h is chosen so that
    Ric(g) + g has operator norm ~ t but Rm grows.
    
    From Step 52: E'/E ~ 2/t, meaning curvature energy doubles on timescale t.
    This means any estimate predicting dE/dt <= C*E is WRONG for this family.
    """
    
    # Near x1 = pi, let s = pi - x1 (small positive)
    # chi ~ s^2/8, a ~ s^4/64
    # C1 ~ s/2, |C1|^2 ~ s^2/4
    # C2 ~ 1/2
    
    # U = a*T, so near chi=0: U ~ s^4 * T
    # U1 = nabla U ~ s^3 * T + s^4 * nabla T  (from product rule on a*T)
    # More precisely: U1 = (da)*T + a*(nabla T) ~ s^3*T + s^4*nabla T
    
    # Weighted dissipation: D = int a |nabla U1|^2 |U1|^{p-2}
    # nabla U1 ~ s^2*T + s^3*nabla T + s^4*nabla^2 T
    # |nabla U1|^2 ~ s^4|T|^2 + s^6|T||nabla T| + s^8|nabla T|^2
    # a|nabla U1|^2 ~ s^8|T|^2 + s^10|T||nabla T| + s^12|nabla T|^2
    # |U1|^{p-2} ~ (s^3|T|)^{p-2} = s^{3(p-2)}|T|^{p-2}  (dominant term)
    # So integrand of D ~ s^{8+3(p-2)} |T|^p = s^{3p+2} |T|^p
    
    # Now the SIGNED-HESSIAN term: J_1 = int chi C2 B(U1)
    # chi ~ s^2/8, C2 ~ 1/2, B(U1) ~ |U1|^p ~ s^{3p}|T|^p
    # Integrand ~ s^{2+3p} |T|^p
    
    # After IBP: J_1 -> int C1*C1*|U1|^p + int chi*C1*nabla(|U1|^p-like)
    # C1*C1 ~ s^2/4, |U1|^p ~ s^{3p}|T|^p
    # First IBP term integrand ~ s^{2+3p}|T|^p  -- SAME order as original!
    
    # The CRITICAL question: does D control J_1?
    # D integrand ~ s^{3p+2}|T|^p
    # J_1 integrand ~ s^{3p+2}|T|^p
    # They are THE SAME ORDER near s=0.
    
    # But D has |nabla U1|^2 which includes s^4|T|^2 + ... 
    # while J_1 after IBP has |C1|^2|U1|^p ~ s^2 * s^{3p}|T|^p = s^{3p+2}|T|^p
    # And D ~ s^{3p+2}|T|^p * (|nabla U1|^2 / |U1|^2)
    #         ~ s^{3p+2}|T|^p * (s^4|T|^2)/(s^6|T|^2) = s^{3p+2}|T|^p * s^{-2}
    # Wait, that's not right. Let me redo carefully.
    
    # Actually: D = int a |nabla U1|^2 |U1|^{p-2}
    # Near s=0: a ~ s^4, |U1| ~ s^3|T|, |nabla U1| ~ s^2|T| + s^3|nabla T|
    # Dominant: |nabla U1| ~ s^2|T| (from differentiating a factor in U=aT)
    # So a|nabla U1|^2 ~ s^4 * s^4|T|^2 = s^8|T|^2
    # |U1|^{p-2} ~ s^{3(p-2)}|T|^{p-2}
    # D integrand ~ s^{8+3p-6}|T|^p = s^{3p+2}|T|^p
    
    # J_1 after IBP: int |C1|^2 |U1|^p ~ int s^2 * s^{3p}|T|^p = int s^{3p+2}|T|^p
    # SAME ORDER. So D and J_1_after_IBP scale identically near s=0.
    
    # This means: D >= c * J_1_after_IBP is POSSIBLE (same scaling)
    # BUT: the constant depends on the ratio |nabla U1|^2/(|C1|^2 |U1|^2)
    #       = (s^2|T|)^2 / ((s/2)^2 * (s^3|T|)^2) * s^4  ... 
    
    # Let me compute the ratio more carefully:
    # |nabla U1|^2 / (|C1|^2 |U1|^2) 
    #   = (s^2|T|)^2 / ((s/2)^2 * (s^3|T|)^2)
    #   = s^4|T|^2 / (s^2/4 * s^6|T|^2)
    #   = s^4 / (s^8/4) = 4/s^4  --> INFINITY as s->0
    
    # Wait, that means D >> J_1_after_IBP near s=0. Good for absorption!
    # But this assumed nabla U1 ~ s^2|T|. What if nabla T dominates?
    # nabla U1 = (da)*T + a*nabla T ~ s^3*T + s^4*nabla T
    # If |nabla T| >> |T|/s, then nabla U1 ~ s^4*nabla T
    # Then |nabla U1|^2 ~ s^8|nabla T|^2
    # D integrand ~ s^4 * s^8|nabla T|^2 * s^{3(p-2)}|T|^{p-2} = s^{3p+6}|nabla T|^2|T|^{p-2}
    # J_1_after_IBP ~ s^{3p+2}|T|^p (unchanged)
    # Ratio D/J_1 ~ s^4 |nabla T|^2/(|T|^2) which can be large OR small
    # depending on |nabla T| vs |T|/s^2.
    
    # KEY INSIGHT: On the flat-T^4 witness, T starts at 0 and grows.
    # Near t=0, |nabla T|/|T| can be ARBITRARY (T is just appearing).
    # So there exist configurations where D does NOT dominate J_1_after_IBP.
    
    # Specifically: if T ~ exp(-1/s^2) type behavior near s=0,
    # then |nabla T|/|T| ~ 1/s^3, and D/J_1 ~ s^4 * 1/s^6 = 1/s^2 -> inf. OK.
    # But if T ~ s^alpha for some alpha, then |nabla T|/|T| ~ 1/s,
    # and D/J_1 ~ s^4 * 1/s^2 = s^2 -> 0. BAD!
    
    # On the actual flat-T^4 witness: T ~ t*f(x) for small t,
    # so |nabla T|/|T| ~ |f'|/|f| which is O(1) away from zeros of f.
    # Near zeros of f, the ratio blows up, helping D.
    # So for THIS specific family, D likely controls J_1.
    
    # BUT: the m=1 estimate must work for ALL families, not just flat-T^4.
    # The real question is whether there exists ANY family where
    # the m=1 signed-Hessian IBP fails to close.
    
    return {
        "flat_T4_scaling": {
            "D_integrand_near_chi_zero": "s^(3p+2)|T|^p",
            "J1_after_IBP_integrand": "s^(3p+2)|T|^p", 
            "scaling_match": True,
            "ratio_D_over_J1_generic": "|nabla U1|^2 / (|C1|^2 |U1|^2)",
            "ratio_for_nablaT_dominant": "s^4 |nabla T|^2 / |T|^2",
            "can_be_small": True,
            "note": "When |nabla T|/|T| ~ 1/s (power-law T near chi=0), ratio -> 0"
        },
        "verdict_candidates": {}
    }


def check_m1_closure_forms():
    """Check each candidate m=1 closure form against structural requirements."""
    
    results = {}
    
    # Form A: Pure signed-Hessian IBP
    # J_1 = int chi C2_{ij} B^{ij}(U1)
    # IBP: = -int C1_j C2_{ij} ... - int chi (nabla_j C2_{ij}) ...
    # Wait, C2 = nabla^2 chi, so nabla C2 = C3.
    # IBP on one derivative of C2:
    #   int chi C2_{ij} B^{ij} = -int C1_i C2_{ij} B^{ij} ... NO
    # Correct IBP: integrate nabla_i acting on C1 (= C2_{i.}):
    #   int chi (nabla_i nabla_j chi) B^{ij}
    #   = -int (nabla_i chi)(nabla_j chi) B^{ij} - int chi (nabla_j chi)(nabla_i B^{ij})
    #   = -int C1_i C1_j B^{ij} - int chi C1_j (nabla_i B^{ij})
    # First term: bounded by ||C1||_inf^2 ||U1||_p^p. GOOD.
    # Second term: nabla_i B^{ij}(U1) involves nabla U1.
    #   |nabla_i B^{ij}| <= C|U1|^{p-1}|nabla U1|
    #   So second term <= C int chi |C1| |U1|^{p-1} |nabla U1|
    #   <= eps int a|nabla U1|^2|U1|^{p-2} + C(eps)||C1||_inf^2 ||U1||_p^p
    #   using chi^2/a = 1 and Young.
    # This CLOSES with only ||C1||_inf. No ||C2|| needed.
    
    results["form_A_signed_hessian_IBP"] = {
        "status": "CLOSES_structurally",
        "uses_only_C1_inf": True,
        "mechanism": "IBP moves one derivative off C2 onto B(U1); "
                     "produces C1*C1*B and chi*C1*nabla B; "
                     "both absorbed by eps*D + C(eps)||C1||_inf^2||U1||_p^p",
        "caveat": "This handles ONLY the signed-Hessian term chi*C2*U1. "
                  "The TOP-CUTOFF term chi*C3*U0 produces residual I_1."
    }
    
    # Form B: Top-cutoff residual I_1 = int chi |C2| |U1| |V|^{p-1} where V=U1
    # For m>=2: U1 is base data in L^4, so Holder(4,p,4,2p/(p-2)) works.
    # For m=1: U1 IS the current variable V. So I_1 = int chi |C2| |V|^p.
    # This is EXACTLY the signed-Hessian term again (up to tensor structure).
    # So Form B reduces to Form A for m=1.
    # BUT: there's also the direct chi*C2*V term in the equation.
    # Both are handled by Form A.
    
    results["form_B_top_cutoff_residual_m1"] = {
        "status": "REDUCES_to_form_A",
        "explanation": "For m=1, V=U1 is current. The residual I_1 = int chi|C2||V|^p "
                       "is the same structure as the signed-Hessian term. "
                       "Form A IBP handles it.",
        "m_ge_2_difference": "For m>=2, U1 is base data in L^4, enabling Holder split."
    }
    
    # Form C: The REAL issue - is there an UNCLOSABLE term at m=1?
    # From A01 Step 59 eq (2.13) specialized to m=1:
    #   d_t U1 = div(a nabla U1) + chi C3 U0 + chi C2 U1 + C1*C2*U0 + C1*C1*U1 + B1*U1 + P1
    # Current terms: chi*C3*U0, chi*C2*U1, C1*C2*U0, C1*C1*U1
    # 
    # chi*C3*U0: IBP gives -int nabla(V^{p-1}V)*chi*C2*U0 - int V^p*C1*C2*U0 - int V^p*chi*C2*V
    #   = -(grad term) - (C1*C2*U0 term) - (chi*C2*V term)
    #   The grad term: |nabla(V^{p-1}V)| ~ p|V|^{p-1}|nabla V|, absorbed by D since U0 bounded.
    #   The C1*C2*U0 term: bounded by ||C1||_inf ||C2||_? ||U0||_inf ||V||_p^{p-1}...
    #     WAIT: this needs ||C2|| in some norm. Not just ||C1||_inf.
    #   The chi*C2*V term: this IS the signed-Hessian term, handled by Form A.
    #
    # So the QUESTION is: does the C1*C2*U0 term from the IBP of chi*C3*U0 close?
    #   int |V|^{p-1} * |C1| * |C2| * |U0|
    #   <= ||U0||_inf ||C1||_inf int |V|^{p-1} |C2|
    #   Need: int |V|^{p-1} |C2| <= eps*D + C(eps)||V||_p^p ??
    #   This requires controlling C2 by the dissipation D.
    #   But C2 is part of the COUPLED PAIR (U1,C2) energy.
    #   The C2 equation: d_t C2 = C1*U1 + ... (from A01 eq 3.13 with m=1)
    #   So C2 is controlled by its own energy, not by D alone.
    #
    # VERDICT: The m=1 closure requires the COUPLED PAIR (U1,C2) energy.
    #   The signed-Hessian term alone closes (Form A).
    #   But the top-cutoff IBP produces a C1*C2*U0 cross-term that
    #   requires the C2 energy equation to bound.
    #   This is exactly what A01/A03 claim: the coupled pair closes.
    #
    # FLAT-T^4 GATE: Does the coupled pair estimate fail on flat-T^4?
    #   On flat-T^4: E'/E ~ 2/t. The coupled estimate gives dE/dt <= CE.
    #   If C is uniform, this contradicts E'/E ~ 2/t as t->0.
    #   BUT: the constant C depends on ||C1||_inf, Vol, etc.
    #   On flat-T^4, ||C1||_inf = 1/2 (fixed), Vol = const.
    #   So C IS uniform, and the estimate DOES predict dE/dt <= CE.
    #   This CONTRADICTS E'/E ~ 2/t.
    #   
    #   THEREFORE: either (i) the coupled pair estimate is wrong, or
    #   (ii) E'/E ~ 2/t is not actually achieved by the flat-T^4 flow.
    #
    # Resolution: E'/E ~ 2/t was computed for the UNWEIGHTED energy int|Rm|^2.
    #   The coupled pair estimates WEIGHTED energies int|U1|^p + int|C2|^p.
    #   U = aT, so near a=0, U is much smaller than T.
    #   The weighted energy may well satisfy dE_w/dt <= C*E_w even when
    #   the unweighted energy does not.
    #   The bridge from weighted to unweighted happens at T0 in L^infty step,
    #   which comes AFTER the pair estimate.
    #
    # So the flat-T^4 gate does NOT directly kill the m=1 weighted estimate.
    # It kills any claim that the weighted estimate implies unweighted control
    # WITHOUT the intermediate T0-in-L^infty step.
    
    results["form_C_coupled_pair_verdict"] = {
        "status": "CONDITIONALLY_CLOSES",
        "signed_hessian_alone": "closes with ||C1||_inf only (Form A)",
        "top_cutoff_IBP_cross_term": "C1*C2*U0 requires coupled C2 energy",
        "coupled_pair_needed": True,
        "flat_T4_gate_weighted": "Weighted energy estimate MAY hold on flat-T^4; "
                                  "E'/E~2/t is for UNWEIGHTED energy. "
                                  "No direct contradiction at weighted level.",
        "flat_T4_gate_unweighted": "Unweighted control requires T0-in-L^infty step "
                                    "AFTER pair estimate. Gate does not kill m=1 pair.",
        "remaining_gap": "The m=1 pair estimate itself appears structurally sound. "
                         "The ACTUAL gap is the BASE ORDER: "
                         "(U0 in Linf, T0 in finite Lq) -> (U1,C2) -> T1 -> T0 in Linf. "
                         "The step T0 in finite Lq -> (U1,C2) is the m=1 base, "
                         "and it uses the signed-Hessian estimate of A03 Step 56 Sec 1. "
                         "That estimate is the load-bearing piece."
    }
    
    return results


def check_base_order_seed():
    """Check the seed estimate: T0 in finite Lq from signed-Hessian.
    
    This is A03 Step 56 Section 1, eq (1.1):
      d/dt ||T||_q^q + c int a|nabla T|^2|T|^{q-2} <= C(||T||_q^q + Vol)
    
    This uses signed integration of nabla^2 a contractions.
    The key identity: a|T|^{q+1} = |U||T|^q (since U=aT).
    And |da|^2 <= 4a|dchi|^2.
    
    On flat-T^4: T starts at 0, so ||T||_q = 0 initially.
    The RHS is C*Vol > 0, so ||T||_q grows at most exponentially.
    This is CONSISTENT with E'/E ~ 2/t for unweighted energy,
    because the unweighted energy is int|Rm|^2, not int|T|^q.
    T = Rm + G, and G is fixed, so int|T|^q ~ int|Rm|^q + const.
    For q=2: int|T|^2 ~ int|Rm|^2 + const, and the estimate gives
    d/dt int|T|^2 <= C int|T|^2, consistent with exponential growth.
    
    The E'/E ~ 2/t was for int|Rm|^2 specifically, where the O(t^2) 
    leading term gives E' ~ t, E ~ t^2, so E'/E ~ 1/t (not 2/t).
    Let me recheck: Step 52 says int|Rm|^2 = 48pi^4 t^2 + O(t^3).
    So E' = 96pi^4 t + O(t^2), E'/E = 2/t + O(1). Yes, 2/t.
    
    But the signed-Hessian estimate gives dE/dt <= CE, i.e., E <= E0*exp(Ct).
    With E0 = 0, this gives E = 0 for all t. CONTRADICTION with E ~ t^2.
    
    UNLESS: the constant C depends on something that blows up as t->0.
    Looking at (1.1): C depends on n, q, K=||U||_inf, ||dchi||_inf.
    On flat-T^4: ||U||_inf = ||aT||_inf. At t=0, T=0 so K=0.
    For t>0 small: K ~ t. So C is bounded as t->0.
    
    This IS a contradiction. The signed-Hessian estimate (1.1) cannot hold
    as stated for the flat-T^4 family.
    
    RESOLUTION: The estimate (1.1) was derived for the EXACT FLOW
    partial_t g = -2aE = -2chi^2(Ric+g).
    On flat-T^4 at t=0: Ric=0, so E=g, and partial_t g = -2chi^2 g.
    This is NOT the Ricci flow; it's a conformal deformation.
    Under this flow, Rm evolves by a reaction-diffusion equation.
    The question is whether the specific derivation of (1.1) accounts
    for all terms correctly.
    
    The derivation uses: d/dt int|T|^q = q int |T|^{q-2} <T, d_t T>
    and d_t T = a Delta T + (da terms) + (reaction terms).
    The signed-Hessian integration handles the da terms.
    But the REACTION terms include T*T and G*T contributions.
    On flat-T^4 at t=0: T=G (since Rm=0), so reaction ~ G*G ~ const.
    This gives d/dt int|T|^q ~ int|G|^q ~ Vol > 0 at t=0.
    So E'(0) > 0, E(0) = int|G|^q > 0 (not zero!).
    
    WAIT: T = Rm + G. At t=0 on flat T^4: Rm=0, G = g∧g/(2(n-1)) ≠ 0.
    So T(0) = G ≠ 0, and ||T(0)||_q > 0.
    The Step-52 computation int|Rm|^2 = 48pi^4 t^2 is for Rm, not T.
    ||T||^2 = ||Rm||^2 + ||G||^2 + 2<Rm,G> ~ ||G||^2 + O(t^2).
    So ||T||^2 is bounded away from zero, and E'/E for ||T||^2 is O(t),
    perfectly consistent with dE/dt <= CE.
    
    CONCLUSION: The flat-T^4 gate does NOT contradict the m=1 seed estimate.
    The apparent contradiction arose from confusing ||Rm||^2 with ||T||^2.
    """
    return {
        "seed_estimate_status": "NOT_KILLED_by_flat_T4",
        "resolution": "T = Rm + G, and G != 0 on flat T^4. "
                      "||T||^2 ~ ||G||^2 + O(t^2) is bounded away from 0. "
                      "E'/E for ||T||^q is O(t), consistent with dE/dt <= CE. "
                      "The E'/E ~ 2/t was for ||Rm||^2 only.",
        "m1_base_verdict": "The signed-Hessian seed estimate survives the flat-T^4 gate. "
                           "The m=1 coupled pair (U1,C2) estimate is structurally sound "
                           "at the weighted level. The remaining gaps are: "
                           "(1) exact tensor-index equations/reordering (A01 #433), "
                           "(2) the step from weighted pair to T1 and T0-in-L^infty, "
                           "(3) imported Moser/local-existence audits."
    }


def main():
    analysis = analyze_flat_T4_witness()
    closure = check_m1_closure_forms()
    seed = check_base_order_seed()
    
    result = {
        "adjudication_question": "Does the m=1 collar term have signed form closing "
                                  "by one IBP with ||nabla chi||_inf?",
        "binary_verdict": "YES_CONDITIONAL",
        "detail": (
            "The signed-Hessian term chi*C2*U1 closes by one IBP using only ||C1||_inf. "
            "The top-cutoff term chi*C3*U0 produces a C1*C2*U0 cross-term after IBP "
            "that requires the coupled C2 energy equation. "
            "The full coupled pair (U1,C2) energy closes structurally. "
            "The flat-T^4 gate does NOT kill the weighted m=1 estimate "
            "(apparent contradiction resolved: T=Rm+G, G!=0, ||T|| bounded away from 0). "
            "Remaining gaps are tensor-index precision, weighted-to-unweighted bridge, "
            "and imported analytic modules — not the m=1 signed structure itself."
        ),
        "flat_T4_gate": analysis,
        "closure_forms": closure,
        "seed_check": seed,
        "implication_for_IL_chain": (
            "The m=1 collar is NOT the failure point. The IL chain's scope remains "
            "a restricted family-level gap near p=1/3. The next investment should be "
            "either (a) tensor-index precision for the higher-order induction, or "
            "(b) the sharpness test: explicit near-pinched constructions on IL manifolds "
            "just above p=1/3 against the stable gap sqrt((p-1/3)/2)."
        )
    }
    
    out = "Sessions/S0910A02/workspace/data/step63_m1_collar_adjudication.json"
    with open(out, 'w') as f:
        json.dump(result, f, indent=2)
    print(json.dumps({"status": "ok", "output": out, "verdict": result["binary_verdict"]}, indent=2))


if __name__ == '__main__':
    main()
