(* Step 7: Curvature operator det R computation for obstruction-amplitude *)
(* Verify det R at orbifold singularities for the positive branch *)

(* --- Setup: 4D curvature operator on Lambda^2 --- *)
(* Lambda^2 basis: {e12, e34, e13, e14, e23, e24} *)
(* Self-dual: phi1 = (e12+e34)/sqrt2, phi2 = (e13-e24)/sqrt2, phi3 = (e14+e23)/sqrt2 *)
(* Anti-self-dual: psi1 = (e12-e34)/sqrt2, psi2 = (e13+e24)/sqrt2, psi3 = (e14-e23)/sqrt2 *)

(* Function: build curvature operator matrix from nonzero R_{ijkl} *)
(* Convention: R_{1212} = K for curvature of 12-plane etc *)

Print["========== CURVATURE OPERATOR det R COMPUTATION =========="];
Print[""];

(* Example 1: Round S^4 with constant curvature K *)
(* R_{ijkl} = K (delta_ik delta_jl - delta_il delta_jk) *)
(* On Lambda^2: R acts as K * Id *)
Print["--- Example 1: Round S^4, constant curvature K ---"];
K = 1/3; (* Ric = 3K g = g *)
detRS4 = K^6; (* 6 = dim Lambda^2 *)
Print["K = ", K, " (Ric = g normalization)"];
Print["s = ", 12*K];
Print["R on Lambda^2 = K * Id, eigenvalues all = ", K];
Print["det R (full Lambda^2) = K^6 = ", detRS4];
Print["det R (on Lambda^2_+) = K^3 = ", K^3];
Print["det R != 0, so S^4/Z_2 CANNOT be Einstein-desingularized"];
Print[""];

(* Example 2: S^2(K1) x S^2(K2) with K1=K2=1, Ric = g *)
Print["--- Example 2: S^2 x S^2, product metric with K1=K2=1 ---"];
(* Nonzero components: R_{1212} = 1, R_{3434} = 1 *)
(* R matrix on Lambda^2 in basis {e12,e34,e13,e14,e23,e24} *)
RmatProd = DiagonalMatrix[{1, 1, 0, 0, 0, 0}];
Print["R matrix on Lambda^2:"];
Print[MatrixForm[RmatProd]];
Print["Eigenvalues: ", Eigenvalues[RmatProd]];
Print["det R (full Lambda^2) = ", Det[RmatProd]];
Print["det R = 0, so (S^2 x S^2)/Z_2 MAY be Einstein-desingularizable"];
Print[""];

(* Now compute on the self-dual subspace *)
(* Change of basis: SD = {{1/Sqrt[2],1/Sqrt[2],0,0,0,0},
                          {0,0,1/Sqrt[2],0,0,-1/Sqrt[2]},
                          {0,0,0,1/Sqrt[2],1/Sqrt[2],0}} *)
SD = {{1/Sqrt[2], 1/Sqrt[2], 0, 0, 0, 0},
      {0, 0, 1/Sqrt[2], 0, 0, -1/Sqrt[2]},
      {0, 0, 0, 1/Sqrt[2], 1/Sqrt[2], 0}};
RmatSD = SD . RmatProd . Transpose[SD];
Print["R on Lambda^2_+ for S^2 x S^2:"];
Print[MatrixForm[Simplify[RmatSD]]];
Print["Eigenvalues: ", Eigenvalues[RmatSD]];
Print["det R|_{Lambda^2_+} = ", Det[RmatSD]];
Print[""];

(* W+ = R|_{Lambda^2_+} - (s/12) Id *)
s = 4; (* s = 2*1 + 2*1 = 4 *)
WplusProd = RmatSD - (s/12)*IdentityMatrix[3];
Print["W+ for S^2 x S^2:"];
Print[MatrixForm[Simplify[WplusProd]]];
Print["W+ eigenvalues: ", Eigenvalues[WplusProd]];
Print["det W+ = ", Det[WplusProd]];
Print[""];

(* Example 3: CP^2 Fubini-Study with Ric = g *)
(* For CP^2, W+ eigenvalues are (s/6, -s/12, -s/12) in a standard basis *)
(* With s = 4: W+ eigenvalues = (2/3, -1/3, -1/3) *)
Print["--- Example 3: CP^2, Fubini-Study with Ric = g ---"];
WplusCP2 = DiagonalMatrix[{2/3, -1/3, -1/3}];
RmatCP2SD = WplusCP2 + (s/12)*IdentityMatrix[3];
Print["W+ eigenvalues for CP^2: ", Eigenvalues[WplusCP2]];
Print["R|_{Lambda^2_+} = W+ + (s/12)Id = ", MatrixForm[Simplify[RmatCP2SD]]];
Print["R|_{Lambda^2_+} eigenvalues: ", Eigenvalues[RmatCP2SD]];
Print["det R|_{Lambda^2_+} = ", Det[RmatCP2SD]];
Print[""];
Print["BOTH S^2xS^2 and CP^2 have det R|_{Lambda^2_+} = 0"];
Print["This is generic for Kahler-Einstein 4-manifolds:"];
Print["the anti-holomorphic self-dual 2-forms are in the kernel"];
Print[""];

(* Example 4: General positive Einstein, W+ eigenvalues (w1, w2, w3) *)
(* with w1+w2+w3 = 0 (trace-free) *)
Print["--- General positive Einstein with Ric = g ---"];
Print["R|_{Lambda^2_+} eigenvalues: (w_i + s/12) = (w_i + 1/3)"];
Print["det R|_{Lambda^2_+} = Product (w_i + 1/3)"];
Print["This vanishes iff some w_i = -1/3"];
Print[""];
w1var = w1; w3var = -w1 - w2;
detGeneral = Expand[(w1 + 1/3)*(w2 + 1/3)*(-w1 - w2 + 1/3)];
Print["det R|_{Lambda^2_+} = ", Simplify[detGeneral]];
Print["Setting det = 0:"];
solns = Solve[detGeneral == 0, w2];
Print["w2 solutions: ", solns];
Print[""];

(* Verify: for S^4 (w1=w2=w3=0): det = (1/3)^3 = 1/27 *)
Print["S^4 check: w1=w2=0 -> det = ", Simplify[detGeneral /. {w1 -> 0, w2 -> 0}]];
(* For S^2xS^2 (w1=2/3, w2=-1/3, w3=-1/3): det = 0 *)
Print["S^2xS^2 check: w1=2/3, w2=-1/3 -> det = ", 
  Simplify[detGeneral /. {w1 -> 2/3, w2 -> -1/3}]];
(* For CP^2 (w1=2/3, w2=-1/3, w3=-1/3): same *)
Print["CP^2 check: w1=2/3, w2=-1/3 -> det = ", 
  Simplify[detGeneral /. {w1 -> 2/3, w2 -> -1/3}]];
Print[""];

(* The key result: det R = 0 iff one of the W+ eigenvalues = -s/12 *)
(* For Ric = g (s=4): iff one W+ eigenvalue = -1/3 *)
(* This is exactly the Kahler condition on one of the self-dual 2-forms! *)
Print["========== KEY RESULT =========="];
Print["det R|_{Lambda^2_+}(p) = 0 at an Einstein orbifold singularity"];
Print["iff one W+ eigenvalue equals -s/12 = -1/3 at that point."];
Print[""];
Print["For constant curvature (S^4): W+=0, all eigenvalues = 1/3 > 0"];
Print["  -> det R > 0 -> NO desingularization (Ozuch Thm 0.3)"];
Print["  -> Obstruction amplitude: C^0 Ricci excess stays order 1"];
Print[""];
Print["For Kahler-Einstein (CP^2, S^2xS^2): W+ has eigenvalue -1/3"];
Print["  -> det R = 0 -> Desingularization POSSIBLE (Biquard)"];
Print["  -> Obstruction amplitude: C^0 Ricci excess CAN tend to 0"];
Print[""];
Print["POSITIVE-BRANCH IMPLICATION: delta_i -> 0 noncollapsed orbifold"];
Print["limits MUST have det R = 0 (by obstruction-amplitude principle)."];
Print["Combined with LeBrun-Ozuch rigidity for positive Einstein,"];
Print["this constrains limits to Kahler-Einstein orbifolds."];
