(* Verify the quantitative Chern-Weil-SW bound for LeBrun manifolds *)
(* under Ricci pinching ||Ric + g||_op <= delta *)

Print["=== Pointwise Ricci eigenvalue analysis ==="];
(* Eigenvalues lambda_i in [-(1+d), -(1-d)], write lambda_i = -1 + eps_i, |eps_i| <= d *)
(* s = sum lambda_i = -4 + sum eps_i, mean = s/4 = -1 + ebar *)
(* Ric0 eigenvalues: eps_i - ebar *)
(* |Ric0|^2 = sum (eps_i - ebar)^2 <= sum eps_i^2 <= 4 d^2 *)
(* s^2 = 16(1-ebar)^2 >= 16(1-d)^2 when |ebar| <= d *)

(* Key pointwise ratio: |Ric0|^2 / s^2 <= 4d^2 / (16(1-d)^2) = d^2/(4(1-d)^2) *)
ratio = Simplify[4 d^2 / (16 (1-d)^2)];
Print["Pointwise |Ric0|^2/s^2 <= ", ratio];

Print["\n=== Main derivation ==="];
(* From CGB + Signature: 4 pi^2 k <= 4 pi^2 A - E_s + E_R *)
(* where E_s = int s^2/24 dmu, E_R = int |Ric0|^2/2 dmu *)
(* From SW: E_s >= 4 pi^2 A / 3 *)
(* From pointwise ratio: E_R <= 3 d^2/(1-d)^2 * E_s *)

(* Substituting: 4 pi^2 k <= 4 pi^2 A - E_s + 3 d^2/(1-d)^2 * E_s *)
(* = 4 pi^2 A - E_s (1 - 3d^2/(1-d)^2) *)
(* >= 4 pi^2 A - (4pi^2 A/3)((1-d)^2 - 3d^2)/(1-d)^2 when minimizing E_s effect *)
(* Wait: we want UPPER bound on k, so we want to MINIMIZE the subtracted term *)
(* The subtracted term is E_s * ((1-d)^2 - 3d^2)/(1-d)^2 *)
(* For small d, this factor is positive, so we minimize by taking E_s at its minimum = 4pi^2 A/3 *)

factor = Simplify[((1-d)^2 - 3 d^2)/(1-d)^2];
Print["Factor in E_s coefficient: ", factor];
Print["Expanded: ", Expand[factor]];

(* k <= A - (A/3)*((1-d)^2 - 3d^2)/(1-d)^2 *)
bound = Simplify[1 - (1/3)*((1-d)^2 - 3 d^2)/(1-d)^2];
Print["\nk/A <= ", bound];
Print["Simplified: ", FullSimplify[bound]];

(* Check if this equals 2/3 + d^2/(1-d)^2 *)
target = 2/3 + d^2/(1-d)^2;
diff = Simplify[bound - target];
Print["Difference from 2/3 + d^2/(1-d)^2: ", diff];

Print["\n=== Expansion for small delta ==="];
series = Series[2/3 + d^2/(1-d)^2, {d, 0, 4}];
Print["k/A <= ", series];

Print["\n=== Critical delta for given k/A = 2/3 + epsilon ==="];
(* Solve d^2/(1-d)^2 = eps for d *)
sol = Solve[d^2/(1-d)^2 == eps && d > 0 && d < 1, d, Reals];
Print["delta_min = ", sol];
(* Should give d = Sqrt[eps]/(1+Sqrt[eps]) *)
candidate = Sqrt[eps]/(1+Sqrt[eps]);
check = Simplify[candidate^2/(1-candidate)^2 - eps];
Print["Check: candidate^2/(1-candidate)^2 - eps = ", check];

Print["\n=== Strengthened Hitchin-Thorpe from pinching ==="];
(* 2chi - 3|tau| >= (Vol/4pi^2)(2(1-d)^2/3 - 2d^2) *)
htFactor = Simplify[2(1-d)^2/3 - 2 d^2];
Print["HT positivity factor: ", htFactor];
Print["Factor > 0 iff d < ", Solve[htFactor == 0 && d > 0, d]];
(* This is (2-4d-4d^2)/3 *)
Print["Expanded: ", Expand[htFactor]];
(* Critical: d < 1/(1+Sqrt[3]) *)
Print["1/(1+Sqrt[3]) = ", N[1/(1+Sqrt[3])]];

Print["\n=== LeBrun 1998 improved bound analysis ==="];
(* LeBrun 1998 uses Weyl estimate: for any metric on M with SW basic class, *)
(* int (2|W+|^2 + s^2/24) dmu >= (4pi^2/3)(2chi+3tau) *)
(* For M = X#kCPbar2: 2chi+3tau = A-k *)
(* Combined with CGB: 2chi+3tau = (1/4pi^2) int(2|W+|^2 + s^2/24 - |Ric0|^2/2) *)
(* This gives: (1/4pi^2) int(2|W+|^2 + s^2/24) = (A-k) + (1/4pi^2) int |Ric0|^2/2 *)
(* Weyl bound: 4pi^2(A-k) + int |Ric0|^2/2 >= (4pi^2/3)(A-k) *)
(* => int |Ric0|^2/2 >= -(8pi^2/3)(A-k) -- trivially true *)
Print["The 1998 Weyl bound does not directly improve the pinching-k/A analysis"];
Print["The improvement in LeBrun 1998 comes from a DIFFERENT mechanism:"];
Print["a sharper monopole estimate applied to the Einstein condition specifically"];

Print["\n=== Compatibility window for negative branch ==="];
(* LeBrun 1996: k >= (2/3)A => no Einstein *)
(* LeBrun 1998: k >= (25/57)A => no Einstein (improved) *)
(* Our bound: tight pinching => k/A <= 2/3 + d^2/(1-d)^2 *)
(* So: manifolds with k/A in [25/57, 2/3] have no Einstein (1998) *)
(* but our bound does not exclude tight pinching *)
Print["Compatibility window: k/A in [25/57, 2/3]"];
Print["25/57 = ", N[25/57]];
Print["2/3 = ", N[2/3]];
Print["Window width: ", N[2/3 - 25/57]];

Print["\n=== Volume bounds ==="];
(* Under pinching: Vol >= 2 pi^2 A / (1+d)^2 (from SW lower bound on int s^2) *)
(* Upper bound: from CGB, 8pi^2(chi_X+k) >= 2(1-d)^2 Vol/3 - 2d^2 Vol *)
(* so Vol <= 8pi^2(chi_X+k) / (2(1-d)^2/3 - 2d^2) = 12pi^2(chi_X+k)/((1-d)^2-3d^2) *)
Print["Vol >= 2 pi^2 A / (1+d)^2"];
Print["Vol <= 12 pi^2 (chi_X + k) / ((1-d)^2 - 3d^2)"];

Print["\nDone."];
