"""Step 105: exact consistency checks of the cap charge
    c(C) = (2chi+3tau)(C) + Q_+(L as boundary of the Einstein side),
for circle-collapsed (fibred-cusp/ALF) links, using
    E -> 0,  H = (1/2) a-lim eta = e/3 - sign(e)   (Dai--Wei, circle bundle over S^2,
                                                   e = Euler number of L oriented as boundary of the region)
    Q_+ = 2E - 3H,  Q_- = 2E + 3H.
Convention check: for a Ricci-flat cap C (P=0), Theorem G on C gives
    C_+(C) = (2chi+3tau)(C) - Q_+^{out}(C) = c(C),
since Q^{out}(C) = -Q(L as boundary of the complement).
Known models (C_+ = (1/2pi^2)int|W+|^2 since s=0):
    Taub-NUT, W^- = 0 orientation (ball):       C_+ = 4
    Taub-NUT, W^+ = 0 orientation (ball):       C_+ = 0
    Taub-bolt on O(-1), blow-up orientation:    C_+ = 3   (Step 27: (1/2pi^2)int|W+|^2 = 3)
    multi-Taub-NUT A_{m-1} ALF, hyperkahler orientation (W^+=0): C_+ = 0, boundary L(m,1)
Output: workspace/data/step105/cap_charge_check.json
"""
from fractions import Fraction as F
import json, os

def sgn(x):
    return (x > 0) - (x < 0)

def H_circle(e):          # (1/2) adiabatic eta, e w.r.t. the oriented link
    return F(e, 3) - sgn(e)

def Qplus(e):             # Euler transgression vanishes on circle collapse
    return -3 * H_circle(e)

def cap_charge(chi, tau, e_out):
    """e_out: Euler number of the link oriented as boundary of the cap.
    Seen from the Einstein side the link has e = -e_out."""
    return 2 * chi + 3 * tau + Qplus(-e_out)

checks = []
def add(name, chi, tau, e_out, expected):
    c = cap_charge(chi, tau, e_out)
    checks.append(dict(name=name, chi=chi, tau=tau, e_out=e_out, c=str(c),
                       expected=str(expected), ok=(c == expected)))

# Taub-NUT, W^- = 0 orientation: e_out = -1 (Hopf as boundary of O(-1)-type filling)
add("Taub-NUT (W^-=0), ball", 1, 0, -1, 4)
add("Taub-NUT (W^+=0), ball", 1, 0, +1, 0)
add("Taub-bolt on O(-1), blow-up orientation", 2, -1, -1, 3)
for m in range(1, 9):
    # A_{m-1} ALF hyperkahler: chi = m, tau = -(m-1), boundary L(m,1) with e_out = +m
    add(f"multi-Taub-NUT A_{m-1} ALF (W^+=0)", m, -(m - 1), +m, 0)

# r exceptional classes in one S^3-Hopf cap #r CP2bar minus ball: chi = 1+r, tau = -r
table = []
for r in range(0, 9):
    table.append(dict(r=r,
                      c_disk_chirality=str(cap_charge(1 + r, -r, -1)),
                      c_opposite_chirality=str(cap_charge(1 + r, -r, +1))))
# disk bundles D(-p), boundary L(p,1), both fibration chiralities
dtab = []
for p in range(1, 9):
    dtab.append(dict(p=p, c_disk_chirality=str(cap_charge(2, -1, -p)),
                     c_opposite_chirality=str(cap_charge(2, -1, +p))))

# LeBrun transfer: 3A >= 9k + 8 sum c ; singleton disk-chirality caps (c=3): k <= A/11
lebrun = dict(singleton_threshold=str(F(3, 9 + 8 * 3)), four_class_caps_threshold=str(F(3, 9)))

out = dict(all_ok=all(c["ok"] for c in checks), model_checks=checks,
           S3_hopf_caps=table, disk_bundle_caps=dtab, lebrun_transfer=lebrun)
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, "..", "data", "step105"); os.makedirs(od, exist_ok=True)
json.dump(out, open(os.path.join(od, "cap_charge_check.json"), "w"), indent=1)
print("all_ok", out["all_ok"]); print(table); print(dtab); print(lebrun)
assert out["all_ok"]
