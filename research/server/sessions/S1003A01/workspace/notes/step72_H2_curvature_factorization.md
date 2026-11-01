# Step 72 — Degree-two curvature directions, lift dependence, and the corrected local factorization

Agent3, Execute. Inputs: Step 71, Spirit #80, and the Step-72 computations.

## 1. Why the Step-71 radial reading was too strong

Step 71 fixed the first metric jet `H2` and varied `(H4,H6,H8)` in an even Darboux germ. Its subspaces therefore did not test the five physical torsion-preserving curvature directions in the degree-two anti-$J$ metric jet. Moreover, fixing separate coordinate coefficients $N_3,N_5$ is not the same as fixing covariant torsion data modulo a genuine Hamiltonian pullback: a degree-four Hamiltonian vector field acts on `H2`, induces higher metric corrections, and changes higher coordinate Nijenhuis coefficients through Lie derivatives of $N_1$.

Consequently, the Step-71 observations remain restricted facts about the chosen fixed-`H2` tangent spaces. They do not show that the radial hierarchy is independent of $W^-$ or of all curvature data. The final two sentences of Step-71 §7.4, which privileged the radial hierarchy as the only possible local-global carrier, are withdrawn.

## 2. The degree-two quotient is exactly five-dimensional

At the polished gen5, $\lambda=-5$ even Darboux jet, the degree-two anti-$J$ coefficient space has dimension
$$
6\binom{5}{3}=60.
$$
Let
$$
A_2=(dE_0,dN_1)|_{H_2}.
$$
The computation in `scripts/step72_vary_H2_free.py` gives
$$
\operatorname{rank}A_2=20,\qquad \dim\ker A_2=40.
$$
The degree-two metric variations induced by quartic Hamiltonians have rank $35$, lie in $\ker A_2$ to Frobenius norm $8.0\times10^{-15}$, and are returned as an orthonormal basis by `gauge_basis`. Thus
$$
\dim\bigl(\ker A_2/\mathcal G_2\bigr)=40-35=5.
$$
The projected kernel matrix has five singular values equal to $1$ to $2\times10^{-14}$ and all remaining singular values below $2.2\times10^{-15}$. This verifies the five-dimensional physical quotient algebraically in the chosen coordinates. `scripts/step72_curvature_identification.py` then extracts the flat linearized curvature operator at the origin. On the physical basis the trace-free $\Lambda^-$ block has rank five, singular values $1.63$--$1.94$, while the $\Lambda^+$ block has norm $1.6\times10^{-15}$. Both chiral blocks vanish on the Hamiltonian gauge basis to $1.5\times10^{-15}$. Thus, with the script's coordinate orientation, the quotient is numerically the trace-free $\Lambda^-$ curvature block. For the imported $J_0$, the fundamental form is $e^{01}+e^{23}$ under $\Omega(X,Y)=g(JX,Y)$, which lies in the script's $\Lambda^+$ span, so this is also $W^-$ in the complex orientation. The overall Riemann-sign convention can reverse values but not rank.

An instructive correction arose in `step72_vary_H2_tangent.py`: on the full tangent of the lower equations, imposing $dN_1=0$ while allowing all blocks produced no visible `H2` motion in the particular SVD null basis. This is not evidence that the five-dimensional quotient disappears. It reflects how the tangent basis and higher corrections were constrained; direct quotienting at degree two is the appropriate calculation.

## 3. A selected lift produces a large $W^-$ response, but that response is not intrinsic

Write the linearized lower equations and next scalar map as
$$
A=[A_p\ A_h],\qquad J=[J_p\ J_h],
$$
where $p=H_2$ and $h=(H_4,\ldots,H_K)$. For a five-column physical basis $X\subset H_2$, the minimum-coefficient-norm lift used by `step72_vary_H2_free.py` is
$$
H_0=-A_h^+A_pX,
$$
and its next scalar response is
$$
Y=J_pX+J_hH_0.
$$
The lower equations are solved accurately:

- $K=6$: relative lower residual $3.04\times10^{-15}$;
- $K=8$: relative lower residual $4.14\times10^{-14}$.

For this selected section, $Y$ has rank five. Its singular values are
$$
K=6:\quad 5792,5059,3316,3205,2304,
$$
$$
K=8:\quad 2.061\times10^5,1.130\times10^5,8.070\times10^4,5.570\times10^4,4.209\times10^4.
$$
The radial norms are respectively $165.6$ and $522.6$. These values are genuine features of that minimum-norm section, not roundoff leakage.

They do **not** define a curvature-to-compatibility map. Any other lift has the form
$$
H_0+N_hC,\qquad N_h=\ker A_h,
$$
and changes $Y$ by
$$
B C,\qquad B=J_hN_h.
$$
Only the class $[Y]\in P_K/\operatorname{im}B$ is independent of the lift.

## 4. Exact numerical factorization modulo all admissible lower corrections

`scripts/step72_lift_quotient.py` computes this quotient directly.

### At $K=6$

$$
\dim\ker A_h=361,\qquad \operatorname{rank}B=35=\dim P_6.
$$
Thus the fixed-`H2` higher freedom already surjects onto every scalar compatibility coefficient. The joint rank of $[B,Y]$ is still $35$, so the physical `H2` quotient adds no new row. Quantitatively,
$$
\|(I-\Pi_{\operatorname{im}B})Y\|=8.55\times10^{-11},
$$
with singular values at most $5.93\times10^{-11}$. The radial row is also fully movable:
$$
\|\ell_6^TB\|=7.2487,
\quad
\|\ell_6^TY\|=165.58,
\quad
\|\ell_6^T(I-\Pi_B)Y\|=1.81\times10^{-12}.
$$
An explicit numerical correction in the computed $\ker A_h$ reduces the full $Y$ norm to $1.68\times10^{-11}$. Its kernel residual is $1.15\times10^{-11}$ and the corrected lower-equation residual is $3.00\times10^{-11}$ (relative to a right-hand-side norm $1.02\times10^4$), supporting admissibility at the attained precision.

### At $K=8$

$$
\dim\ker A_h=735,\qquad \operatorname{rank}B=84=\dim P_8.
$$
Again the joint rank is $84$ and the incremental rank is zero. The quotient norm is $4.18\times10^{-10}$, while
$$
\|\ell_8^TB\|=0.92593,
\quad
\|\ell_8^TY\|=522.64,
\quad
\|\ell_8^T(I-\Pi_B)Y\|=2.01\times10^{-11}.
$$
An explicit fixed-`H2` correction reduces $Y$ to $5.31\times10^{-9}$, at the numerical conditioning scale. Its coefficient norm is $8.14\times10^4$; the kernel residual is $3.36\times10^{-8}$ and the corrected lower-equation residual is $3.60\times10^{-8}$ (relative to a right-hand-side norm $2.68\times10^5$). Thus the cancellation is admissible to relative scale about $10^{-13}$ in this floating system.

Therefore the correct first-order statement in the unrestricted even Darboux tower is:

> **Computed factorization through $K=8.** The five-dimensional physical degree-two quotient changes a chosen lifted scalar source, including its radial component, but its entire change factors through the scalar image of admissible higher-jet corrections. It contributes no correction-independent compatibility class at $K=6$ or $K=8$.

This is stronger and more precise than either “the radial row is torsion-only” or “the radial row depends intrinsically on $W^-$.” Both earlier readings confused a selected section with the quotient by higher lift freedom.

## 5. What happens if higher coordinate torsion is fixed

The script also appended the equations
$$
dN_3=dN_5=\cdots=dN_{K-1}=0
$$
with their `H2` contributions included. Those systems are not solvable for the five physical `H2` directions:

- $K=6$: augmented lower residual $47.8$, relative residual $3.71\times10^{-3}$;
- $K=8$: augmented lower residual $9302$, relative residual $3.05\times10^{-2}$.

The enormous formal cancellation coefficients ($4.1\times10^{14}$ and $4.3\times10^{16}$) arise from treating numerical null directions as available despite this incompatibility and have no mathematical meaning. The useful conclusion is narrower: the full five-column physical slice has no simultaneous coordinate-torsion-fixed Einstein lift at the achieved precision in this gauge, so at least one physical combination forces a higher coordinate-Nijenhuis change. The residual matrix rank was not yet recorded, so this does not show that every nonzero physical direction is incompatible.

These coordinate constraints are not yet covariant torsion constraints modulo genuine Hamiltonian pullback. Moreover, the augmented branch's reported ranks of its almost-zero $B$ matrices used a self-relative threshold and are spurious; its quotient/cancellation numbers must be discarded. A geometric factorization theorem should use covariant derivatives of the Nijenhuis/torsion section and include the induced higher corrections of one actual Hamiltonian diffeomorphism.

## 6. Revised local picture and global relevance

The flat exactness and newest-channel theorems remain intact. The nonlinear extension space is coupled:

1. the physical $W^-$-type degree-two data alter the particular higher torsion and curvature jets required by the Einstein equations;
2. at the tested orders, no scalar compatibility class survives after quotienting by all higher lifts;
3. trying to hold all displayed coordinate torsion coefficients fixed is incompatible with these physical directions;
4. hence neither the radial row nor the complementary scalar rows can currently be promoted to a curvature-independent local obstruction.

This supplies finite-order evidence, at the tested witness, that no scalar compatibility class remains through $K=8$ after higher lifts; it does not prove general local viability, all-orders formal extension, or convergence. It also vindicates Spirit #80's global warning: compact Goldberg transport must retain the full coupled geometry. The harmonic projection of $q\widehat\omega$ depends on the metric, and an ASD harmonic form obeys a Weitzenböck equation containing $W^-$. The absence of an explicit $W^-$ term in a pointwise $\Delta q$ identity does not remove $W^-$ from covariant derivatives, harmonic projection, or global transport.

## 7. Files

- `scripts/step72_vary_H2_tangent.py`, `data/step72/vary_H2_tangent_K6.json`: exposes the limitation of imposing selected fixed-coordinate constraints.
- `scripts/step72_vary_H2_free.py`, `data/step72/vary_H2_free_K{6,8}.json`: constructs the five-dimensional degree-two quotient and minimum-norm lifts.
- `scripts/step72_lift_quotient.py`, `data/step72/lift_quotient_K{6,8}.json`: computes the correction-independent quotient and explicit cancellation.
- `scripts/step72_curvature_identification.py`, `data/step72/curvature_identification.json`: identifies the five-dimensional quotient with the $W^-$ curvature block and verifies gauge curvature vanishes.
- TTCS integration `trace/ttcs/results/step72_ttcs01_verifier2_integration.md`: independently identified the lift ambiguity and predicted the $K=8$ cancellation before the final quotient run.
