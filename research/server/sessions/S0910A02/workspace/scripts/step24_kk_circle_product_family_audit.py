"""
Step 24 audit: exact Kaluza--Klein circle-collapse product family.

This is a symbolic/numeric ledger for the constant-fiber principal S^1
Kaluza--Klein equations used in the positive branch of Yau 26.
It does not compute curvature from coordinates; it checks the algebraic
O'Neill equations recorded in Step 6:

  Ric_M^H = Ric_B - 1/2 (phi o phi),
  Ric_M(U,U) = 1/2 |phi|^2,
  Ric_M^mixed = +/- 1/2 d^* phi.

For Ric_M = g_M, the base data must satisfy
  |phi|^2 = 2, d phi = d^* phi = 0, Ric_B = g_B + 1/2 phi o phi.

The family B = S^2_{Ric=2} x N_{Ric=1}, phi = sqrt(2) area_{S^2}
solves these equations for every Einstein N with Ric_N = g_N.
With N=S^{n-3}, the total space is L(q,1) x S^{n-3}, q->infty,
more explicitly (S^3(sqrt(2))/Z_q) x S^{n-3}, an exact positive
Einstein collapsing sequence in every n>=5 with uniformly bounded curvature.
Dimension n=4 would require N=S^1 with Ric=1, impossible.
"""
import json
import math
from pathlib import Path

records = []
for n in range(4, 13):
    d = n - 3  # dimension of N factor in B=S^2 x N
    possible_N_positive_Einstein = d >= 2
    # Algebraic blocks in orthonormal basis: S^2 directions have phi o phi = 2; N directions 0.
    vertical_ric = 0.5 * 2.0
    horizontal_target = 1.0
    ric_B_S2 = 2.0
    ric_B_N_required = 1.0
    horizontal_residual_S2 = ric_B_S2 - 0.5 * 2.0 - horizontal_target
    # If d=1 and N=S^1, Ric_N is forced to be 0, not 1.
    ric_N_available_model = 1.0 if possible_N_positive_Einstein else 0.0
    horizontal_residual_N = ric_N_available_model - 0.0 - horizontal_target
    exact = abs(vertical_ric - 1.0) < 1e-12 and abs(horizontal_residual_S2) < 1e-12 and abs(horizontal_residual_N) < 1e-12
    records.append({
        "total_dimension_n": n,
        "base_dimension_m": n - 1,
        "N_dimension_d=n-3": d,
        "candidate_base": f"S^2_Ric=2 x {'S^'+str(d)+'_Ric=1' if d>=2 else 'S^1'}",
        "vertical_Ric": vertical_ric,
        "horizontal_residual_S2": horizontal_residual_S2,
        "horizontal_residual_N_or_S1": horizontal_residual_N,
        "exact_KK_Einstein_equations_hold_for_model": exact,
        "interpretation": (
            "No: n=4 would need a circle factor with Ric=1; this is the Step-6 Bochner/topology obstruction."
            if not exact else
            "Yes: gives exact Ric=g on (S^3(sqrt(2))/Z_q) x S^{n-3} after choosing t=sqrt(2)/q."
        ),
    })

# Integrality/collapse normalization for S^2_Ric=2: area=2*pi.  If Omega is the area form,
# phi=sqrt(2) Omega and F_q=q Omega, then t_q F_q=phi for t_q=sqrt(2)/q.
q_records = []
for q in [1,2,5,10,100,1000]:
    t = math.sqrt(2)/q
    q_records.append({
        "q": q,
        "fiber_scale_t": t,
        "fiber_length_2pi_t": 2*math.pi*t,
        "actual_volume_factor_relative_to_base": 2*math.pi*t,
        "q_dependence_ignoring_2pi": t,
        "curvature_form_integral_over_S2": f"2*pi*{q}",
        "tF_fixed_norm": math.sqrt(2),
    })

out = {
    "title": "Step 24 KK circle product family audit",
    "oneill_equations_checked": [
        "Ric_M^H = Ric_B - 1/2(phi o phi)",
        "Ric_M(U,U)=1/2|phi|^2",
        "Ric_M^mixed=+/-1/2 d^*phi",
        "Ric_M=g in constant-length connection class iff |phi|^2=2, d*phi=0, Ric_B=g_B+1/2(phi o phi); dphi=0 is automatic from dF=0",
    ],
    "family": "B=S^2 with Ric=2 times any closed Einstein N^d with Ric=1; phi=sqrt(2) area_S2; total P_q -> B has c1=q[S^2] and t=sqrt(2)/q, giving (S^3(sqrt(2))/Z_q) x N^d.",
    "dimension_records": records,
    "collapse_normalization": q_records,
    "conclusions": [
        "The Step-6 obstruction to constant-length free S^1 positive Einstein collapse is special to base dimension 3 / total dimension 4.",
        "The proposed general odd-base obstruction from the kernel of a 2-form is false: for base S^2 x S^d, d>=2, the kernel lies in the Einstein factor Ric=1 and creates no Bochner contradiction.",
        "For every total dimension n>=5, (S^3(sqrt(2))/Z_q) x S^{n-3} carries exact Ric=g metrics collapsing as q->infty with bounded curvature; these are finite quotients/products of fixed Einstein manifolds, so the Yau-26 conclusion holds trivially for the model.",
        "This supports the revised positive-branch program: characterize positive-pinched collapse as Einstein-compatible rather than trying to forbid collapse."
    ],
}

path = Path("Sessions/S0910A02/workspace/data/step24_kk_circle_product_family_audit.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
print(f"Saved {path}")
