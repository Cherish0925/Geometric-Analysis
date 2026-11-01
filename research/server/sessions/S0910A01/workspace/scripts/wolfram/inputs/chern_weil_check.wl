(* Verify the Chern-Weil / LeBrun quantitative bounds for Yau Problem 26 *)

(* Dossier Proposition: if delta < 1/(1+Sqrt[3]) then 2chi > 3|tau| *)
Print["=== Dossier Proposition Verification ==="];
deltaThreshold = 1/(1 + Sqrt[3]);
Print["Threshold delta = 1/(1+Sqrt[3]) = ", N[deltaThreshold]];

(* Proof: bracket = 2(1-delta)^2/3 - 2 delta^2 must be > 0 *)
bracket[d_] := 2(1-d)^2/3 - 2 d^2;
bracketSimp = Simplify[bracket[d]];
Print["Bracket f(delta) = ", bracketSimp];
sol = Solve[bracketSimp == 0 && d > 0, d];
Print["f(delta) = 0 at delta = ", d /. sol];
Print["Verify 1/(1+Sqrt[3]) = (Sqrt[3]-1)/2 = ", Simplify[1/(1+Sqrt[3]) - (Sqrt[3]-1)/2]];
Print[""];

(* Bishop-Gromov volume for positive branch in 4D *)
(* Ric >= (1-delta)g on 4-manifold, comparison sphere has curvature (1-delta)/3 *)
(* Vol(S^4) with curvature kappa = 8 pi^2/3 * kappa^(-2) *)
Print["=== Bishop-Gromov Volume Bound (4D positive) ==="];
volBound[d_] := 24 Pi^2 / (1-d)^2;
Print["V <= 24 pi^2 / (1-delta)^2"];
Print["At delta=0: V <= ", N[volBound[0]]];
Print["At delta=0.3: V <= ", N[volBound[0.3]]];
Print[""];

(* LeBrun integral bound *)
Print["=== LeBrun + Chern-Weil Combined Bound ==="];
(* For M = X#k CPbar^2, A = c1^2(X), LeBrun range 2A/3 < k < A *)
(* ∫|E|^2 dV >= 8 pi^2 (k - 2A/3) *)
(* ∫|E|^2 dV <= 4 delta^2 V *)
(* V <= 4 pi^2 (A-k) / f(delta) for negative branch using CGB *)

(* For positive branch: combine Bishop-Gromov volume with integral bound *)
(* 4 delta^2 * 24 pi^2/(1-delta)^2 >= 8 pi^2 (k-2A/3) *)
(* 12 delta^2 / (1-delta)^2 >= k-2A/3 *)
Print["Positive branch: 12 delta^2/(1-delta)^2 >= k - 2A/3"];

(* For negative branch: V <= 4 pi^2 (A-k) / f(delta) *)
(* 4 delta^2 * 4 pi^2 (A-k) / f(delta) >= 8 pi^2 (k-2A/3) *)
(* 2 delta^2 (A-k) / f(delta) >= k - 2A/3 *)
negBracket = Simplify[2 d^2 (a - k) / bracket[d] - (k - 2 a/3)];
Print["Negative branch inequality (must be >= 0 at minimum delta):"];
Print["2 delta^2 (A-k) / f(delta) - (k-2A/3) = ", negBracket];
Print[""];

(* Small delta approximation for negative branch *)
Print["=== Small Delta Asymptotics ==="];
(* f(delta) ~ 2/3 for small delta *)
(* So 2 delta^2 (A-k) * 3/2 >= k-2A/3 *)
(* 3 delta^2 (A-k) >= k-2A/3 *)
(* delta^2 >= (k-2A/3) / (3(A-k)) *)
(* Note: earlier derivation had 6(A-k), let me re-derive *)
(* 8 pi^2 (k-2A/3) <= 4 delta^2 * 4 pi^2 (A-k) / (2/3) *)
(* 8 pi^2 (k-2A/3) <= 4 delta^2 * 6 pi^2 (A-k) *)
(* (k-2A/3) <= 3 delta^2 (A-k) *)
(* delta^2 >= (k-2A/3) / (3(A-k)) *)
Print["For small delta: delta^2 >= (k-2A/3) / (3(A-k))"];
Print["Correction: factor is 3, not 6"];
Print[""];

(* Test specific examples *)
Print["=== Specific LeBrun Examples ==="];
(* Smallest: A=4, k=3 *)
delta4 = Sqrt[(3 - 8/3) / (3*(4-3))];
Print["A=4, k=3: delta >= ", Simplify[delta4], " = ", N[delta4]];

(* A=9, k=7 *)
delta9 = Sqrt[(7 - 6) / (3*(9-7))];
Print["A=9, k=7: delta >= ", Simplify[delta9], " = ", N[delta9]];

(* A=100, k=67 (near 2A/3) *)
delta100 = Sqrt[(67 - 200/3) / (3*(100-67))];
Print["A=100, k=67: delta >= ", Simplify[delta100], " = ", N[delta100]];

(* A=1000, k=668 *)
delta1000 = Sqrt[(668 - 2000/3) / (3*(1000-668))];
Print["A=1000, k=668: delta >= ", Simplify[delta1000], " = ", N[delta1000]];
Print[""];

(* Check: as A->inf with k = ceil(2A/3)+1, delta -> 0? *)
Print["=== Varying Manifold Asymptotics ==="];
(* k = 2A/3 + 1 (A divisible by 3) *)
(* delta^2 >= 1/(3*(A/3-1)) = 3/(A(3-3/A)) -> 3/A *)
(* delta >= Sqrt(3/A) *)
Print["For A divisible by 3, k=2A/3+1:"];
Print["delta >= Sqrt(1/(A-3)) ~ Sqrt(1/A)"];
Table[{a, N[Sqrt[1/(3*(a/3-1))]]}, {a, {9, 30, 90, 300, 900, 3000}}] // TableForm // Print;
Print[""];

(* Verify: positive branch bound is UNIFORM because no volume freedom *)
Print["=== Positive Branch Uniform Bound ==="];
(* delta/(1-delta) >= Sqrt((k-2A/3)/12) *)
(* Minimum over valid k: k = ceil(2A/3)+1 *)
(* Minimum contribution: k-2A/3 >= 1/3 (when A≡1 mod 3) *)
(* So delta/(1-delta) >= Sqrt(1/36) = 1/6 *)
(* delta >= 1/7 *)
Print["Positive branch minimum: delta/(1-delta) >= 1/6, so delta >= 1/7 = ", N[1/7]];
Print["This uses Bishop-Gromov volume bound, only valid for sigma=+1"];
Print[""];

(* Key conclusion *)
Print["=== KEY CONCLUSION ==="];
Print["POSITIVE branch (sigma=+1, dim 4):"];
Print["  HT-violating manifolds: delta_+ >= 0.366 (universal, Chern-Weil)"];
Print["  LeBrun strict-HT: delta_+ >= 1 (no positive scalar curvature)"];
Print["  ALL known no-Einstein: delta_+ bounded away from 0"];
Print[""];
Print["NEGATIVE branch (sigma=-1, dim 4):"];
Print["  For fixed LeBrun M: delta_- >= C/Sqrt(c1^2(X))"];
Print["  For varying manifolds: bound -> 0 as c1^2 -> inf"];
Print["  Counterexample sequence NOT ruled out by current bounds"];
Print["  But construction of tight negative Ricci pinching is UNSOLVED"];
