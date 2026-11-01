(* Verify the LeBrun negative Einstein exclusion mechanism *)
(* For M = X # k CPbar^2, c1^2(X) = A *)
(* 2chi + 3tau = A - k *)
(* SW basic class kappa^2 = A - k *)

Print["=== LeBrun Negative Einstein Exclusion ==="];

(* For a hypothetical negative Einstein metric h on M: *)
(* Ric_h = lambda*h, lambda < 0, s = 4*lambda *)
(* CGB: 8*Pi^2*(A-k) = 4*Integral[|W+|^2] + 16*lambda^2*Vol/3 *)
(* SW: 16*lambda^2*Vol >= 32*Pi^2*(A-k) *)

(* From SW: lambda^2*Vol >= 2*Pi^2*(A-k) *)
(* Substituting into CGB: *)
(* 4*Integral[|W+|^2] = 8*Pi^2*(A-k) - 16*lambda^2*Vol/3 *)
(*                      <= 8*Pi^2*(A-k) - 16*(2*Pi^2*(A-k))/3 *)
(*                      = 8*Pi^2*(A-k) - 32*Pi^2*(A-k)/3 *)
(*                      = 8*Pi^2*(A-k)*(1 - 4/3) *)
(*                      = -8*Pi^2*(A-k)/3 *)

Print["CGB + SW for Einstein:"];
Print["4*int|W+|^2 <= 8*Pi^2*(A-k)*(1 - 4/3) = -8*Pi^2*(A-k)/3"];
Print["Since int|W+|^2 >= 0 and A > k, this is a CONTRADICTION."];
Print["Therefore: no negative Einstein metric on M when k < A."];
Print[];

(* Now for the INPUT metric g with delta_-(g) = delta: *)
(* s = -4 + e_s, |e_s| <= 4*delta *)
(* |E|^2 <= 4*delta^2 *)
(* CGB: 4*Pi^2*(A-k) = 2*int|W+|^2 + int[s^2/24] - int[|E|^2/2] *)
(* Need |W+|^2 >= 0, so: int[s^2/24] - int[|E|^2/2] <= 4*Pi^2*(A-k) *)
(* From SW: int[s^2] >= 32*Pi^2*(A-k), so int[s^2/24] >= 4*Pi^2*(A-k)/3 *)

Print["=== Input metric with delta_- = delta ==="];
Print["From |W+|^2 >= 0: int|E|^2/2 >= int s^2/24 - 4*Pi^2*(A-k)"];
Print["From SW: int s^2/24 >= 4*Pi^2*(A-k)/3"];
Print["So: int|E|^2/2 >= 4*Pi^2*(A-k)/3 - 4*Pi^2*(A-k) = -8*Pi^2*(A-k)/3"];
Print["This is trivially satisfied (non-positive)."];
Print[];

(* Try: using the CGB for 2chi-3tau as well *)
(* B = 2chi - 3tau = 4*chi(X) - A + 5*k *)
(* From 2chi-3tau CGB: 4*Pi^2*B = 2*int|W-|^2 + int s^2/24 - int|E|^2/2 *)
(* And from 2chi+3tau: 4*Pi^2*C = 2*int|W+|^2 + int s^2/24 - int|E|^2/2 *)
(* where C = A-k *)

(* Adding: 4*Pi^2*(B+C) = 2*int|W|^2 + int s^2/12 - int|E|^2 *)
(* = 2*int|W|^2 + int s^2/12 - int|E|^2 *)

(* For BMY bound surfaces: A = 3*chiX, tau(X) = (A-2chiX)/3 = chiX/3 *)
(* B = 4chiX - 3chiX + 5k = chiX + 5k *)
(* C = 3chiX - k *)

Print["=== For BMY-saturating surfaces (A = 3*chi_X) ==="];
chiX = Symbol["chiX"];
A = 3*chiX;
k = Symbol["k"];
B = 4*chiX - A + 5*k;
C2 = A - k;
Print["C = 2chi+3tau = ", C2];
Print["B = 2chi-3tau = ", B];
Print["B = ", Simplify[B]];

(* Check: B = chiX + 5k *)
(* Strict HT requires B > 0 and C > 0 *)
(* C > 0: k < 3chiX *)
(* B > 0: always (chiX >= 1 and k >= 1) *)
Print[];

(* S0910A01 formula: delta^2 >= (k - 2A/3)/(3*(A-k)) *)
(* = (k - 2chiX)/(3*(3chiX - k)) *)
(* This is > 0 only when k > 2chiX *)

Print["S0910A01 bound (for A = 3chiX):"];
deltaSquared = (k - 2*A/3)/(3*(A - k));
Print["delta^2 >= ", Simplify[deltaSquared]];
Print["= (k - 2*chiX) / (3*(3*chiX - k))"];
Print["Positive only when k > 2*chiX"];
Print[];

(* For k = 2*chiX + m where m >= 1: *)
(* delta^2 >= m / (3*(chiX - m)) *)
(* For m = 1: delta^2 >= 1/(3*(chiX-1)) ~ 1/(3*chiX) *)
(* As chiX -> infty: delta -> 0 like 1/sqrt(chiX) ~ 1/sqrt(A) *)
Print["For k = 2*chiX + m, m >= 1:"];
Print["delta^2 >= m/(3*(chiX - m))"];
Print["For m = 1: delta^2 >= 1/(3*(chiX-1)) ~ 1/(3*chiX) ~ 1/A"];
Print["So delta >= 1/sqrt(A) -> 0 as A -> infinity."];
Print[];
Print["This confirms the necessary condition allows delta -> 0 for varying manifolds."];
Print["But the CONSTRUCTION of such metrics remains OPEN."];
