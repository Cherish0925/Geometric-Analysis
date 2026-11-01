(* Principal symbol of DRic at flat metric, verify kernel is pure gauge *)
(* Dimension n, covector xi = e_1 *)

Print["=== Principal symbol of linearized Ricci at flat metric ==="];
Print["Convention: sigma_xi(DRic)(h)_ij = 1/2(|xi|^2 h_ij - xi_j (xi.h)_i - xi_i (xi.h)_j + xi_i xi_j tr(h))"];

n = 4; (* work in dimension 4 for concreteness *)
Print["Dimension n = ", n];

(* Symbol matrix: acts on symmetric 2-tensors *)
(* For xi = e_1, |xi|^2 = 1 *)
(* (xi.h)_i = h_{1i} *)

(* Represent symmetric 2-tensor by upper-triangular components *)
(* Index pairs: (1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4) *)
pairs = Flatten[Table[{i,j}, {i,1,n}, {j,i,n}], 1];
dim = Length[pairs];
Print["Number of independent components: ", dim];

(* Build symbol matrix *)
sigma = Table[0, {dim}, {dim}];
Do[
  {i,j} = pairs[[alpha]];
  {k,l} = pairs[[beta]];
  (* sigma(h)_ij = 1/2(h_ij - delta_{j1} h_{1i} - delta_{i1} h_{1j} + delta_{i1} delta_{j1} tr(h)) *)
  (* Need coefficient of h_kl in sigma(h)_ij *)
  (* h_ij contribution: delta_{(i,j),(k,l)} or delta_{(i,j),(l,k)} with symmetry factor *)
  symFactor = If[k == l, 1, 2]; (* h_kl = h_lk, so component appears once or twice *)
  
  coeff = 0;
  (* Term 1: h_ij *)
  If[(i==k && j==l) || (i==l && j==k), coeff += 1/symFactor];
  (* Term 2: -delta_{j1} h_{1i} *)
  If[j == 1, If[(1==k && i==l) || (1==l && i==k), coeff -= 1/symFactor]];
  (* Term 3: -delta_{i1} h_{1j} *)
  If[i == 1, If[(1==k && j==l) || (1==l && j==k), coeff -= 1/symFactor]];
  (* Term 4: delta_{i1} delta_{j1} tr(h) *)
  If[i == 1 && j == 1, If[k == l, coeff += 1]];
  
  sigma[[alpha, beta]] = coeff/2;
, {alpha, dim}, {beta, dim}];

Print["\nSymbol matrix (rows=output (i,j), cols=input (k,l)):"];
Print["Index pairs: ", pairs];
Print[MatrixForm[sigma]];

Print["\nRank of symbol: ", MatrixRank[sigma]];
Print["Kernel dimension: ", dim - MatrixRank[sigma]];

ker = NullSpace[sigma];
Print["\nKernel basis vectors:"];
Do[
  Print["  v", i, " = ", ker[[i]]];
  Print["    Components: ", Table[{pairs[[j]], ker[[i,j]]}, {j, dim}]];
, {i, Length[ker]}];

(* Check: gauge directions xi tensor V + V tensor xi for V = e_a *)
Print["\n=== Gauge directions (xi=e_1) tensor V + V tensor (xi=e_1) ==="];
Do[
  gauge = Table[0, {dim}];
  Do[
    {i,j} = pairs[[alpha]];
    (* (e_1 tensor e_a + e_a tensor e_1)_ij = delta_{i1} delta_{ja} + delta_{ia} delta_{j1} *)
    val = 0;
    If[i==1 && j==a, val += 1];
    If[i==a && j==1, val += 1];
    If[i==1 && j==1 && a==1, val = 2]; (* special case *)
    gauge[[alpha]] = val;
  , {alpha, dim}];
  Print["  V=e_", a, ": ", gauge];
, {a, 1, n}];

Print["\n=== Verify gauge directions span the kernel ==="];
gaugeVecs = Table[
  Table[
    Module[{i,j,val},
      {i,j} = pairs[[alpha]];
      val = 0;
      If[i==1 && j==a, val += 1];
      If[i==a && j==1, val += 1];
      If[i==1 && j==1 && a==1, val = 2];
      val
    ]
  , {alpha, dim}]
, {a, 1, n}];

Print["Rank of gauge space: ", MatrixRank[gaugeVecs]];
Print["Rank of kernel: ", MatrixRank[ker]];

(* Check gauge space = kernel *)
combined = Join[ker, gaugeVecs];
Print["Rank of (kernel union gauge): ", MatrixRank[combined]];
Print["If rank = n, then kernel = gauge space."];

Print["\nDone. Kernel of sigma_xi(DRic) is exactly the gauge (diffeomorphism) directions."];
