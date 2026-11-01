"""Step 93: explicit local twist characters of the supplied Seiberg-Witten classes at the
Wahl point of the complex-model realization (Prop. 93.C of the Step-93 note).

Setting (n odd >= 3).  M = X # k CPbar^2, B_{n,1} subset V_{-4} = nbhd of the holomorphic
(-4)-curve S = E1 - E2 - E3 - E4 (PPS Prop. 4.4 / Khodorovskiy, complex model).
Identifications used (proved in the note):
  x|_{V_{-4}} = (x.S) u,  u generator of H^2(V_{-4}) = Z;
  E_i.S = -eps_i,  eps = (1,-1,-1,-1);  K_M.S = 2;
  K_M|_B has order n in H^2(B) = Z_n (Cartier index n of a T-singularity), so u_B := u|_B is
  a generator and K|_B = 2 u_B; write everything in units of K|_B: u_B = h K|_B, h = 2^{-1} mod n.
Basic classes  c_1 = -K_M + 2 sum_{i in F} E_i  (F subset of {1..k}); local twist
  j_F = sum_{i in F, i<=4} e_i  mod n,  e_i = -eps_i h  (units of K|_B), local character
  m = n j_F in Z_{n^2}.  Step-89/93 isotropy: Phi(p) can be nonzero iff j in {0,1}.
Output: workspace/data/step93/wahl_supplied_characters.json
"""
import json, os, itertools

res = {}
for n in range(3, 16, 2):
    h = pow(2, -1, n)
    eps = (1, -1, -1, -1)
    e = [(-x * h) % n for x in eps]
    counts = {}
    forced = 0
    for F in itertools.product((0, 1), repeat=4):
        j = sum(f * ei for f, ei in zip(F, e)) % n
        counts[j] = counts.get(j, 0) + 1
        if j not in (0, 1):
            forced += 1
    res[n] = dict(h=h, e_units_of_K=e, twist_multiset=dict(sorted(counts.items())),
                  forced_zero_fraction=f"{forced}/16",
                  canonical_j=0, anticanonical_side_note="c_1=+K_M-... gives j -> 1-j, same counts")
print(json.dumps(res, indent=1))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step93')
os.makedirs(od, exist_ok=True)
json.dump(res, open(os.path.join(od, 'wahl_supplied_characters.json'), 'w'), indent=1)
