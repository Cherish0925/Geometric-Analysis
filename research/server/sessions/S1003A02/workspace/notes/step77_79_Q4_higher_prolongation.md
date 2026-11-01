# Steps 77–79 — Higher prolongation of almost-Kähler Einstein germs at a torsion zero

Status tags: [P] proved, [N] exact/numerical computation with stated coverage, [C] conjectural.
Conventions: Darboux gauge \(\Omega=\Omega_0\) standard, \(g=e^{H}\) with \(H\) symmetric and anti-\(J_0\)-commuting (Siegel parametrization of \(\Omega_0\)-compatible metrics), torsion zero at \(0\) \(\Leftrightarrow H=O(|x|^2)\) after cubic-Hamiltonian gauge (rank 20 of 24, Step 76). \(H=\sum_{d\ge2}H_d\), \(H_d\) homogeneous of degree \(d\); \(E=\operatorname{Ric}(e^H)-\lambda e^H\), \(E_k\) its \(x\)-degree-\(k\) part. Torsion jet \(f=cz+(S+A)\bar z\) as in 76.Z; cone \(\|A\|^2=\|S\|^2+8|c|^2\).

## 1. Degree count and parity [P]

**Lemma 77.1 (degree count).** \(E_k\) is a sum of multilinear terms in jets \(H_{d_1},\dots,H_{d_r}\) with \(\sum d_i=k+2\) (Ricci part: two derivatives) or \(\sum d_i=k\) (\(\lambda e^H\) part). Hence \(E_k=L_kH_{k+2}+\mathcal N_k(H_2,\dots,H_{k+1})\) with \(L_k\) the flat linearized Ricci operator, and a product of two jets of degree \(\ge m\) first appears at order \(2m-2\).

Consequence (correcting Spirit #94 and confirming the Step-78 comment): \(E_6\) contains \(H_4\cdot H_4\); the order-6 residual conditions are **quadratic** in \(H_4\). With \(H_2,H_3\) fixed and unknowns \(u=(H_4,H_5,H_6,H_7)\), the orders \(1,\dots,5\) are **affine** in \(u\) (no product of two unknowns has total degree \(\le7\)), and
\[
E_6=L_6H_8+\operatorname{aff}(u)+\mathcal Q(H_4,H_4),
\]
where \(\mathcal Q\) is the pure \(H_4H_4\) part of flat Ricci at degree 8: **universal**, independent of \(H_2,H_3,\lambda\). (Verified numerically: quadratic-model relative error \(\le10^{-13}\) in every run.)

**Lemma 77.2 (parity).** \(x\mapsto-x\) is a linear symplectic isometry of the flat model, so for even \(H\) all \(E_{\rm odd}\equiv0\); even germs have a torsion zero at 0. Orders 3, 5 cannot cut even jets.

## 2. Linear Hilbert data [N, exact mod two primes, two λ] (Step 77)

| k | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| rank \(L_k\) | 10 | 36 | 83 | 156 | 260 |
| coker | 0 | 4 | 17 | 44 | 90 |
| flat Bianchi | 0 | 4 | 16 | 40 | 80 |
| excess | 0 | 0 | 1 | 4 | 10 |
| ker mod gauge | 15 | 28 | 43 | 60 | 79 |

Excess \(=\binom{k+1}{3}\): one scalar nonlinear compatibility \(\Phi\) whose degree-\((k-2)\) Taylor coefficients are the order-\(k\) conditions; its order-2 coefficient is the quadric of 76.Z. Top-map ranks (newest free jet \(K\in\ker L_{k-2}\), generic cone point): 10, 20, 28 at \(k=4,6,8\) against excess 10, 35, 84; rank 0 at torsion-free \(H_2\). Over \(\mathbb C\) the 15 order-6 residual conditions of the even ansatz have full Jacobian rank w.r.t. the admissible \(H_4\) (absorbable over \(\mathbb C\)).

## 3. The exact order-6 reduction to one scalar inequality [N] (Steps 78–79)

Fix \(H_2\) (on \(E_0=0\) and the cone) and \(H_3\) (orders 1, 3 solvable). Solve orders 1–5 exactly: \(u=u_0+Ny\). With \(C_6\) a basis of \(\operatorname{coker}L_6\) (flat, 259-dimensional), \(\Psi(y)=C_6^TE_6=c+Jy+\tfrac12y^THy\) exactly. Rows of \(\Psi\) that vanish identically (Bianchi) are removed by the Gram spectrum of \((c,J,H)\) (sharp gap \(10^{-15}\to10^{-1}\)); the remaining rows are the excess (35 at a strict cone point). Let \(P\) be the joint range of the quadratic forms and \(K_c\) its complement; \(J K_c\) absorbs all but the rows annihilated by \(\pi\in\operatorname{coker}(JK_c)\). When exactly one such row remains and its reduced Hessian \(H_r\) is definite,
\[
\text{real formal solvability through order 6}\iff \Phi_6:=\pi\!\cdot\!c-\tfrac12 j^TH_r^{-1}j\le0\quad(H_r>0\text{ normalized}).
\]
\(\Phi_6\) is normalization-invariant up to the positive scale of \(\pi\) (unit vector in an orthonormal coker frame).

Two independent pipelines:
- `step78_reduced_order6.py`/`step78_quad6.py`/`step78_phi6.py` (even ansatz; \(H_6\)'s \(\ker L_4\) part eliminated first);
- `step79_general_order6.py` (all degrees 2–8; generic affine elimination of orders 1–5; universal \(\mathcal Q\) by polarization).
At the Step-77 D6 jet (\(\lambda=-3\)) both give \(\Phi_6=3.976571\times10^{-4}\) (agreement \(10^{-11}\) relative), with joint quadratic rank 12, linear absorption 34 of 35, one scalar, \(H_r>0\).

**Kähler control (passes).** Torsion-free admissible \(H_2\) at \(\lambda=-3\), \(H_3=0\): 25 nontrivial rows, all 25 absorbed linearly, no scalar condition, LM residual \(2\times10^{-12}\): real solvable, as it must be (KE germs exist). `data/step79b/gen6_kahler_lam-3.json`.

**Odd jets do not rescue the D6 jet (so far).** A nonzero admissible \(H_3=t\,h_3\) adds 4 order-5 conditions on \(H_4\) that do not disappear as \(t\to0\) (they are \(t\times\)[a condition independent of \(t\)]: \(ny\) drops 845→841, joint quadratic rank 12→8), and \(\Phi_6\) increases: \(t=0.1\): \(2.88\times10^{-3}\); \(t=0.3\): \(3.72\times10^{-3}\). (RESULTS FOR t=1,3 AND OTHER DIRECTIONS: see §4.)

## 4. Data

| jet | λ (unit torsion norm) | W⁻-shift | H₃ | rows / quad rank / absorbed / scalar | Φ₆ |
|---|---|---|---|---|---|
| D6 (|c|²=1.8e-4, tn=.354) | −3 (λ/tn −8.5) | — | 0 | 35/12/34/1, H_r>0 | 3.98e-4 |
| D6 | 0, +3 | — | 0 | same | 3.52e-3, 1.19e-2 (Step 78) |
| D6 | −3 | — | 0.1,0.3,1,3 ×h₃ | 35/8/34/1 | 2.88e-3, 3.72e-3, 3.00e-2, 1.59 |
| generic s11 #0 (|c|²=.038, S²=.058, A²=.365) | −1 | 0, 2 | 0 | 35/12/34/1 | 0.784, 0.762 |
| same | +1 | 0, 2 | 0 | 35/12/34/1 | 0.863, 0.866 |
| generic s21 #0 (|c|²=.028, S²=.108, A²=.335) | −3, −1, 0 | 0 | 0 | 35/12/34/1 | 0.865, 0.837, 0.819 |
| Kähler (torsion-free) | −3 | — | 0 | 25/22/25/0 | solvable (LM 2e-12) |
| A01 shared jet c=1, S=[[2,1],[1,1+i]], a=2+2i (tn=√52, det 110) | −1 (λ/tn −0.139) | min-norm | 0 | 35/12/34/1, H_r>0 | **1121.5** (c₀=1492.3; LM min 1179) |
| symmetric jet c=1, S=I, a=1+2i (det 29) | −1 | min-norm | 0 | 35/12/31/**4** (special: 4 scalars) | not reduced; LM min 459 (unsolved) |
| Kähler | −3 | — | 1×h₃ | orders 1–5 inconsistent (resid 0.069): random order-3-admissible H₃ is not order-4/5-admissible on the Kähler 2-jet | — |

Files: `data/step79/gen6_d6_*.json`, `data/step79b/gen6_kahler_lam-3.json`, `data/step79c/cone_test.json`; scan in progress `data/step79c/cone_*` (generic/smallc/bigc/H₃ probe) and A01 shared point `data/step79b/gen6_a01pt_*`.

Reading. The scalar order-6 obstruction is robust (order-one values at a non-degenerate generic jet), insensitive to the torsion-free part of the 2-jet, and of the same sign for λ<0, λ=0, λ>0. Along the odd direction tested the odd jet only adds conditions. The Kähler control passes. The obstruction therefore looks like an identity of Weitzenböck type at a torsion zero, \(\tfrac12|P\nabla^3\Omega|^2_{H_r}+F=0\) with \(F>0\) on the strict cone — not a sign-of-λ effect. Scope: one odd direction, a handful of cone jets; floating-point (no interval certificate yet).

## 5. What failed and why
- Step-77 LM on the full germ system: stagnation is now explained by \(\Phi_6>0\), not by conditioning.
- Unreduced fixed-\(H_2\) GN (Step 78): failed even at linear orders because the linear constraints were not eliminated.
- SDP certificate v1 (\(\max\lambda_{\min}\)): returns 0 whenever the multiplier form has a kernel; v2 (\(\varepsilon e_0e_0^T\)) failed numerically on the degenerate face. The explicit reduction supersedes both.
- Spirit #94's linear-tower argument: wrong degree count (Lemma 77.1).
