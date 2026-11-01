# Step 57: an SL(2,R)-invariant strictly almost-Kähler Einstein metric with λ<0

Session S1003A01, Agent2. Status: the algebra is exact over Q; the metric checks are numerical at 1e-12 or better; bolt smoothness and completeness are numerical/asymptotic and still need proof; novelty has not been checked against Armstrong 2002 (only its metadata is available). Labels: [E] exact computer algebra, [N] numerical, [P] by hand.

## 1. Metric-only reformulation (Spirit #67, extended)
Diagonal class-A metric g=dt²+Σa_i²σ_i² with dσ_i=2n_iσ_j∧σ_k. Use the weight-1 variables h_i=a_i'/a_i and W_i=n_ia_i/(a_ja_k). Every class-A type is a sign pattern of W: IX +++, VIII ++- (and its permutations), VII0 ++0, VI0 +-0, II +00, I 000. Take ε=+1; ε=-1 is the substitution W→-W.
- Einstein equations: h_i'=-h_iS+2(W_i²-(W_j-W_k)²)-λ and W_i'=W_i(h_i-h_j-h_k), with constraint Q+λ=0, where Q=Σh_ih_j+ΣW_i²-2ΣW_iW_j. [E] D(Q+λ)=-2S(Q+λ). Setting λ=-Q gives a polynomial quadratic flow on R⁶ that conserves Q.
- Closure of Ω=Σx_i(e0∧e_i+e_j∧e_k): x_i'=μ_ix_i with μ_i=2W_i-h_j-h_k, which is linear. [P]
- q=|∇Ω|²=2[ΣX_iμ_i²+(X1+X2)b3²+(X1+X3)b2²+(X2+X3)b1²], where b1=h1+W1-W2-W3, etc.
- [E] At random rational points, `scripts/step57_classA_metric_only.py check` reproduces step56 (a,b,c) μ, H, q and h'.
- Two directions (X3=0). The X-free invariance tower is Φ_n=μ1f2^(n)-μ2f1^(n), with f^(0)=μ and f^(n+1)=Df^(n)+2μf^(n). On V(Φ) set X1=-μ2/(μ1-μ2) and X2=μ1/(μ1-μ2).
- Key lemma [P]: Φ1=0 holds iff X_i'=2μ_iX_i. Hence any invariant variety V of the λ=-Q flow with Φ1|_V=0 and μ1μ2(μ1-μ2)≠0 gives Einstein AK structures. Real points with μ1μ2<0 have 0<X_i<1 and q≥2X1μ1²>0, so they are strict.

## 2. Exact elimination [E] (`step57_two_singular.py`, `step57_two_lift.py`)
The ideal sat(<Φ1..ΦN>, μ1μ2(μ1-μ2)) has Krull dimensions 5,4,3,2,2,2 for N=1..6 (mod 32003; mult 3,7,15,38,6,6). It has a single prime component P of dimension 2 and degree 6. Lifting by farey and checking over Q:
- Φ1∈P;
- D(g)∈P for every generator g, so V(P) is exactly invariant;
- μ1, μ2, μ1-μ2 and Q are not in P.

The generators are in `data/step57/two_lift_P1.txt`. P is a graph over the W-cone:
- h1=(2W1³-5W1²W2-2W1²W3+4W1W2²-2W1W2W3-W2³)/((W1-W2)(W1+W2)), with h2 and h3 as in `data/step57/component_param.json`;
- F(W)=-(W1+W2)⁴W3²+(W1+W2)³(W1-W2)²W3+3W1W2(W1-W2)⁴=0.
- Rational-angle parametrization (u=W1/W2, v=W3/W2), verified to 1e-14:
  - c=cosφ, z=1/2+c, r=(c²-1/4)/3;
  - u=[(1-2r)+(2/√3)sinφ]/(2r), v=z(u-1)²/(u+1).

## 3. The strict negative branch [N]
The strict real points (μ1μ2<0) all have Bianchi VIII sign type and Q>0, i.e. λ<0 (`step57_real_points.py`). Along the arc φ∈(-2π/3,-π/3), Q̂>0 and μ1μ2<0 throughout (`step57_curve_metric.py`, `data/step57/curve_metric.json`).

Independent check (`step57_verify_candidate.py`, `data/step57/verify_p1.json`): the ODE was integrated in (h,W,x), and curvature was computed with the separate step56 Koszul engine (NB=-1,1,1).
- |Ric-λg|≤8e-12 with λ=-3 and s=-12.
- |x1²+x2²-1|≤3e-13 along the flow.
- The distance to V(P) is ≤8e-12.
- q ranges over 0.56 to 10.7, so q>0.
- |W⁻|²≤2e-22, where W⁻ is the Weyl part of chirality opposite to Ω. The metric is half-conformally-flat (self-dual) Einstein.
- W⁺ has a nondegenerate spectrum, e.g. (-1.80,0.47,1.33).
- η=|W⁺(Ω)^⊥|≈0.4–0.7, so η≠0 and Ω is not a W⁺ eigenform. This is consistent with AAD (Einstein with η=0 forces Kähler or Ricci-flat).

## 4. Ends [N]
- Bolt end (φ→-π/3, finite t): a1→0, a1'→1, a2=a3→√6 (2.449489743 at φ=-π/3+1e-12), X1→1, W⁺ spectrum→(-1/3,-1/3,2/3).
  - Direct t-integration near the bolt is unstable: the a2-a3 mode amplifies roundoff (W⁻ appears to blow up only after leaving V(P)). The exact-curve parametrization avoids this.
  - Expected interpretation: a smooth totally geodesic bolt Σ=Γ\H² for Γ⊂SL(2,R), with σ1-circle length 2π (slope 1). Parity and smoothness to all orders are NOT yet proved.
- Far end (φ→-2π/3): the t-length diverges logarithmically (5.65, 10.58, 15.47 for cutoffs 1e-3, 1e-6, 1e-9), so the end is complete.
  - h→(1/√2,√2,1/√2) and W2→const. The growth rates are 1:2, as in CH² horospheres with Ric=-3g. The end looks ACH, with Reeb direction e2, and a3/a1→√3.
  - The earlier forward t-integration that suggested AH asymptotics had drifted off V(P) and is invalid.

## 5. Consequences if confirmed
- Locally, the negative-scalar Goldberg statement fails: strictly AK Einstein metrics with s<0 exist, and their AK form has W⁻=0 and W⁺_2≠0.
- Expected complete examples are disk bundles over closed hyperbolic surfaces, with an ACH end.
- The closed Goldberg problem remains open. Any proof must use compactness essentially, as in the Ricci-flat NPT/Tod situation, and must exclude this self-dual mechanism globally (e.g. via LeBrun/Kim c1·ω or χ≥3τ type identities). Note that W⁻=0 means a compact quotient would need τ=... constraints.

## 6. To do
- Exact series at the bolt (parity and smoothness), and an exact ACH asymptotic analysis.
- Literature check: Armstrong 2002 (Crelle 542), Apostolov–Drăghici survey, Hitchin/Tod Bianchi VIII self-dual Einstein (Painlevé VI) identification. Hitchin's paper and Calderbank's Integrable Background Geometries are staged in `staging/acquired`.
- An exact proof that W⁻≡0 on V(P).
- Three-direction tower Ψ_n=det(f0,f1,fn).
- Run the same machinery for A02's aligned J-invariant-Ricci question (#841).
