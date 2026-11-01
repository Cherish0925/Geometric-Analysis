"""
Step 12: characteristic-class bookkeeping for the LeBrun near-critical family.
Distinguishes p1(TM) from p1(Lambda^2_+).
"""
import json, os

def formulas(A='A', chiX='chiX', k='k'):
    return {
        "chi_M": f"{chiX}+{k}",
        "tau_X_from_A_chi": f"({A}-2*{chiX})/3",
        "tau_M": f"({A}-2*{chiX})/3 - {k}",
        "p1_TM_integral": f"3*tau_M = {A}-2*{chiX}-3*{k}",
        "p1_Lambda_plus_integral": f"2*chi_M+3*tau_M = {A}-{k}",
        "p1_Lambda_minus_integral": f"2*chi_M-3*tau_M = 4*{chiX}+5*{k}-{A}",
        "near_k_A_over_3": {
            "p1_TM_per_A": "1 - 2 chiX/A - 1 = -2 chiX/A (typically negative for general type)",
            "p1_Lambda_plus_per_A": "1 - 1/3 = 2/3 (positive in the orientation where LeBrun uses W+)",
            "warning": "If one says simply p1 without naming the bundle, the sign can be wrong. The calibrated density rho_+ used in LeBrun/Derdzinski arguments is for Lambda^2_+, not TM."
        }
    }

samples=[]
for chiX_over_A in [1/3, 1, 2, 5]:
    A=300.0; chi=chiX_over_A*A; k=A/3
    tauX=(A-2*chi)/3; tauM=tauX-k
    samples.append({
        "chiX_over_A": chiX_over_A,
        "A": A,
        "k": k,
        "tauM_over_A": tauM/A,
        "int_p1_TM_over_A": 3*tauM/A,
        "int_p1_Lambda_plus_over_A": (2*(chi+k)+3*tauM)/A,
        "int_p1_Lambda_minus_over_A": (2*(chi+k)-3*tauM)/A,
    })

out={"formulas":formulas(),"samples":samples}
OUTDIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data")); os.makedirs(OUTDIR,exist_ok=True)
OUT=os.path.join(OUTDIR,"step12_characteristic_class_bookkeeping.json")
with open(OUT,"w") as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
print("Saved",OUT)
