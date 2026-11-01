(* Step 87 independent Wolfram exact check of missed Killing mode. *)
ClearAll[Wedge, Cmat, MomentCoeff, BoundaryCoeff];
Wedge[i_, j_] := Module[{A = ConstantArray[0, {4, 4}]}, A[[i, j]] = 1; A[[j, i]] = -1; A];
e01 = Wedge[1, 2]; e02 = Wedge[1, 3]; e03 = Wedge[1, 4];
e12 = Wedge[2, 3]; e13 = Wedge[2, 4]; e23 = Wedge[3, 4];
wp = {(e01 + e23)/Sqrt[2], (e02 - e13)/Sqrt[2], (e03 + e12)/Sqrt[2]};
wm = {(e01 - e23)/Sqrt[2], (e02 + e13)/Sqrt[2], (e03 - e12)/Sqrt[2]};
C = Table[Simplify[wp[[a]].wm[[b]] + Transpose[wp[[a]].wm[[b]]]], {a, 3}, {b, 3}];
Print["C integral entries: ", And @@ Flatten[Table[Element[C[[a, b, i, j]], Integers], {a, 3}, {b, 3}, {i, 4}, {j, 4}]]];
Print["orthogonality max offdiag: ", Max[Abs[Flatten[Table[Tr[C[[a, b]].C[[c, d]]] - If[a == c && b == d, 4, 0], {a, 3}, {b, 3}, {c, 3}, {d, 3}]]]]];
D = Table[Sum[C[[2, k, i, j]] C[[k, 2, m, n]]*0, {k, 3}], {i,4},{j,4},{m,4},{n,4}];
D = Table[Sum[C[[2, k, i, j]] C[[2, k, m, n]] - C[[k, 2, i, j]] C[[k, 2, m, n]], {k, 3}], {i, 4}, {j, 4}, {m, 4}, {n, 4}];
Print["D[1,4,2,3] (0-based D_03,12): ", D[[1, 4, 2, 3]]];
Print["D[2,3,1,4] (0-based D_12,03): ", D[[2, 3, 1, 4]]];
(* Killing one-forms: alpha = x2 dx1 - x1 dx2 on factor A, beta = x4 dx3 - x3 dx4 on factor B in 1-based indices. *)
A = ConstantArray[0, {4, 4}]; B = ConstantArray[0, {4, 4}];
A[[1, 2]] = 1; A[[2, 1]] = -1;
B[[3, 4]] = 1; B[[4, 3]] = -1;
M = Table[A[[i, p]] B[[j, q]] + B[[i, p]] A[[j, q]], {i, 4}, {j, 4}, {p, 4}, {q, 4}];
Print["M[1,4,2,3] (h03 x1x2 coeff 0-based): ", M[[1, 4, 2, 3]]];
Print["M[2,3,1,4] (h12 x0x3 coeff 0-based): ", M[[2, 3, 1, 4]]];
Dcontr = Sum[D[[i, j, p, q]] M[[i, j, p, q]], {i,4},{j,4},{p,4},{q,4}];
Print["D:M = ", Dcontr];
MomentCoeff[a_, b_, p_, q_] := (KroneckerDelta[a, b] KroneckerDelta[p, q] + KroneckerDelta[a, p] KroneckerDelta[b, q] + KroneckerDelta[a, q] KroneckerDelta[b, p])/12;
BoundaryCoeff[chir_] := Module[{total = 0, AA},
  Do[
    AA = If[chir == 1, C[[2, k]], C[[k, 2]]];
    total += Sum[AA[[a, b]] AA[[i, j]] M[[i, j, p, q]] MomentCoeff[a, b, p, q], {a,4},{b,4},{i,4},{j,4},{p,4},{q,4}],
    {k,3}];
  Simplify[-3/4 total]
];
Bp = BoundaryCoeff[1]; Bm = BoundaryCoeff[-1];
Print["Bplus/pi^2 = ", Bp];
Print["Bminus/pi^2 = ", Bm];
Print["difference/pi^2 = ", Simplify[Bp - Bm]];
(* Linearized curvature block for missed mode. *)
H = Table[M[[i,j,a,b]] + M[[i,j,b,a]], {i,4},{j,4},{a,4},{b,4}];
dR = Table[1/2 (H[[i,l,j,k]] + H[[j,k,i,l]] - H[[i,k,j,l]] - H[[j,l,i,k]]), {i,4},{j,4},{k,4},{l,4}];
BlockEntry[basis1_, basis2_] := Simplify[1/4 Sum[basis1[[i,j]] dR[[i,j,k,l]] basis2[[k,l]], {i,4},{j,4},{k,4},{l,4}]];
Rpp = Table[BlockEntry[wp[[a]], wp[[b]]], {a,3},{b,3}];
Rmm = Table[BlockEntry[wm[[a]], wm[[b]]], {a,3},{b,3}];
Print["delta R plus block: ", MatrixForm[Rpp]];
Print["delta R minus block: ", MatrixForm[Rmm]];
Print["Rpp[[2,2]]=", Rpp[[2,2]], ", Rmm[[2,2]]=", Rmm[[2,2]]];
