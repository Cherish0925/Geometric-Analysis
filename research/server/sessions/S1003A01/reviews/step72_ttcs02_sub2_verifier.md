# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step72_H2_curvature_factorization.md",
    "Sessions/S1003A01/workspace/notes/step71_flat_exactness_and_fibre_structure.md",
    "Sessions/S1003A01/workspace/scripts/step72_vary_H2_free.py",
    "Sessions/S1003A01/workspace/scripts/step72_lift_quotient.py",
    "Sessions/S1003A01/workspace/scripts/step72_curvature_identification.py",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K6.json",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K8.json",
    "Sessions/S1003A01/workspace/data/step72/lift_quotient_K6.json",
    "Sessions/S1003A01/workspace/data/step72/lift_quotient_K8.json",
    "Sessions/S1003A01/workspace/data/step72/curvature_identification.json"
  ]
}
```

## Task

Verify the final Step-72 local conclusion after the correction-independent lift quotient was computed. Read the note, all three central scripts, and outputs. Check: (1) the identification of ker(dE0,dN1)/quartic-Hamiltonian gauge with the five-dimensional W^-(0) block; (2) the linear-algebra statement that a chosen W^- lift changes P_K(E_K), but its class modulo J_h ker A_h vanishes at K=6 and K=8 because B has full target rank; (3) whether the explicit radial conclusions and cancellation norms are interpreted correctly; (4) why the attempted fixing of coordinate N3,N5,N7 does not yet define covariant fixed torsion, and what its nonzero residual actually establishes; and (5) whether the revised note withdraws all stronger unsupported Step-71 inferences. Give a concise theorem-quality formulation, name any remaining computational flaw or normalization issue, and distinguish exact structural facts from floating evidence.

## Output

# Verification memo: Step 72 lift quotient, $W^-(0)$ identification, and the coordinate-torsion test

## 0. Summary

- **Lift-quotient conclusion.** The central Step-72 conclusion is correct, but the note phrases it in a way that is weaker and less transparent than what the data show.
- **$W^-(0)$ identification.** This is an exact, base-point-independent, $U(2)$-equivariant fact. The polished witness plays no role in it.
- **The "factorization".** It is not specifically about $W^-$. It is a surjectivity theorem for the fixed-$H_2$ subtower, and the vanishing of the $W^-$ class follows automatically from it.
- **Torsion-fixed branch.** Its reported `rank_B = 35/84` and `incremental_rank = 0` are numerical artifacts of a self-relative tolerance. Only the inconsistency residual carries information, and that information is coordinate- and gauge-dependent.
- **K=6 numbers.** Several K=6 values in the note do not match the stored JSON.

## 1. $\ker(dE_0,dN_1)/\mathcal G_2 \cong W^-(0)$

### Why this is exact

$H$ has no constant or linear part. Hence $g(0)=I$ and $\partial g(0)=0$, so $\Gamma(0)=0$.

- For $g=\exp H$, the quartic term $H^2/2$ does not contribute to $\partial^2 g(0)$. So $\mathrm{Rm}(0)$, and hence $E_0=\mathrm{Ric}(0)-\lambda I$, is **exactly linear** in $H_2$. It is not merely linearized.
- The same holds for the degree-1 Nijenhuis coefficients. In $N\sim J\partial J$ with $J=J_0\exp H$, the degree-1 part is $J_0\cdot\partial(\text{deg-2})$, which is linear in $H_2$.

Consequently $A_2$ is a fixed rational matrix, independent of the base jet and of $\lambda$. It is also equivariant under $U(2)$, which preserves $(g_0,J_0,\omega)$. The phrase "at the polished gen5, $\lambda=-5$ jet" in §2 of the note is therefore misleading: the statement is a flat, exact fact.

### Exact argument

1. Quartic-Hamiltonian gauge gives $L_Xg_0$, whose linearized curvature vanishes identically. So both chiral blocks vanish on $\mathcal G_2$ exactly. The $10^{-15}$ values are roundoff.
2. On $\ker A_2$ we have $\delta\mathrm{Ric}(0)=0$ (with $\lambda$ fixed), so $\delta\mathrm{Rm}(0)=\delta W^+ +\delta W^-$.
3. With $\omega\in\Lambda^+$, $U(2)=U(1)_+\times SU(2)_-$ acts on $W^-\cong \mathrm{Sym}^4$ of the $SU(2)_-$ spinor irreducibly. On $W^+$ it acts with $U(1)_+$-weights $0,\pm2,\pm4$, i.e. $1+2+2$.
4. The quotient $\ker A_2/\mathcal G_2$ is a 5-dimensional $U(2)$-representation. Its map to $W^-(0)$ is equivariant and nonzero. By irreducibility, a nonzero equivariant map from a 5-dimensional space onto the irreducible 5-dimensional $W^-$ is surjective, hence an isomorphism.
5. The vanishing of $\delta W^+$ is the statement that $(E_0,N_1)$ fix $W^+(0)$. This is consistent with almost-Kähler theory: at a point where $\nabla\omega=0$, the $W^+$ components are fixed by $s$ and by the first jet of $N$.

### What still needs to be pinned down

- **Orientation.** `curvature_maps` labels $\Lambda^\pm$ by $e_{01}\pm e_{23}$, etc. Nothing in the script verifies that $\omega_0=g_0(J_0\cdot,\cdot)$ lies in the span of `Sp`. The name "$W^-$" requires this one-line check.
- **Exact certification.** Because $A_2$ is rational and base-independent, the counts (rank 20, kernel 40, gauge 35) can be computed in exact arithmetic in seconds. This would remove floating evidence from this item entirely.
- **Unequal singular values (1.94, 1.94, 1.90, 1.67, 1.63).** These reflect the non-orthonormal monomial and `anti_basis` normalization. Only injectivity matters.

A dimension count consistent with the data, but not yet verified, would make the picture complete:
$$
60-35=25=20\ (\mathrm{Rm}(0))+5\ (\text{curvature-invisible torsion jet}),
$$
with $E_0$ removing 10 directions and $N_1$ removing $W^+$ plus the 5 torsion directions.

## 2. The lift quotient: what is exact, and what it actually says

### Exact linear algebra

If $\operatorname{rank}(J_h|_{\ker A_h})=\dim P_K$, then $\operatorname{im}B=P_K$. Every class $[Y]\in P_K/\operatorname{im}B$ vanishes for every $X$, not only for the $W^-$ directions.

So the incremental-rank-zero result carries no information about $W^-$ beyond surjectivity of $B$. The accurate statement is:

> At the base jet, the linearized order-$K$ scalar compatibility $P_K\circ dE_K$, restricted to the fixed-$H_2$ tangent of the lower equations $\{dE_0=\dots=dE_{K-2}=0,\ \delta H_2=0\}$, is surjective ($K=6$: rank 35; $K=8$: rank 84).

The $W^-$ conclusion is a corollary. The note's sentence "stronger and more precise than…" is accurate, but it should say that the $W^-$ part is automatic.

### Nonlinear consequence (worth stating)

The compatibility map is a submersion along the lower solution set. Two facts are needed:

- the lower solution set is a manifold near the base, i.e. $A$ has locally constant rank;
- the base nearly solves the compatibility.

Given both, the implicit function theorem produces nearby jets satisfying $P_K(E_K)=0$ exactly, with $H_2$ held fixed. Surjectivity is an open polynomial condition, so it persists on an open set. If it holds at one exact point of an irreducible component, it holds on a Zariski-dense subset of that component. That is the rigorous content behind "locally viable through tested orders."

### Floating evidence and conditioning at K=8

| Item | K=6 | K=8 |
|---|---|---|
| `sv_B_tail` (two smallest $\sigma$ of $B$) | 0.517, 0.252 | 0.0073, 0.0050 |
| $\sigma_{\max}(B)$ recorded? | no | no |
| Rank tolerance | $10^{-8}\sigma_{\max}$ | $10^{-8}\sigma_{\max}$ |

- At K=8, $J$-scale responses are $\sim 2\times10^5$ (from `vary_H2_free_K8`). If $\sigma_{\max}(B)$ is of that order, the tolerance is $\sim 2\times10^{-3}$. The smallest singular value would then sit only about 2.5× above threshold. $\sigma_{\max}(B)$ must be recorded.
- A certificate needs two ingredients:
  - a lower bound $\sigma_{\min}(B)\ge 5\times10^{-3}$ at a certified exact solution near the witness, which exists by Newton–Kantorovich on the lower tower;
  - a Lipschitz bound on $B$ over that distance.

  The witness residual ($E_8\sim10^{-6}$) makes such a certificate plausible but not automatic.
- **Dimension mismatch.** `dim_ker_Ah = 735` at K=8, while Step 71 reported `dim Tan = 736` for the same fixed-$H_2$ lower system. $E_0$ does not involve $h$, so the two should agree. The off-by-one signals a singular value of $A_h$ near the $10^{-10}$ relative threshold.
  - This does not affect $\operatorname{rank}B=84$.
  - It does mean the lower solution set's local manifold structure at K=8 is not numerically clean. That structure is exactly what the submersion argument above needs.
  - The singular-value gap of $A_h$ around index 969 should be printed.

## 3. Radial row and cancellation norms

### Interpretation (correct)

| Quantity | Meaning |
|---|---|
| $\ell^TY$ (165.6; 522.6) | Property of the minimum-norm section only |
| $\|\ell^TB\|$ (7.25; 0.926) | Nonzero, so the radial row is reachable by fixed-$H_2$ corrections. Agrees with Step 71 "all of Tan" (7.25; 0.926). |
| $\ell^T(I-\Pi_B)Y\sim10^{-12}$–$10^{-11}$ | Forced by full rank of $B$ |
| Cancelled $Y$: $5.3\times10^{-9}$ against $\|Y\|\sim2\times10^5$ | Relative $\sim10^{-14}$, i.e. roundoff |

The correction norm grows from 262 (K=6) to 81428 (K=8). This growth tracks $1/\sigma_{\min}(B)$ and is consistent with the conditioning discussed in §2.

### Number mismatch at K=6

The note's K=6 values do not match `lift_quotient_K6.json`:

| Quantity | Note | JSON |
|---|---|---|
| Quotient norm | $8.55\times10^{-11}$ | $8.045\times10^{-11}$ |
| Largest quotient singular value | $5.93\times10^{-11}$ | $5.31\times10^{-11}$ |
| Radial quotient | $1.81\times10^{-12}$ | $1.59\times10^{-12}$ |
| Cancelled $Y$ | $1.52\times10^{-11}$ | $1.83\times10^{-11}$ |

The K=8 values match. The K=6 values evidently come from a different run, likely with different tolerances. Either the note or the data file should be regenerated so that they agree.

### Normalization of the radial row

$\ell$ implements $\Delta^m x^{2\beta}\big|_0=\dfrac{m!}{\prod\beta_i!}\prod(2\beta_i)!$, which is correct. However:

- This pairing is valid only if `P_matrix(K)` outputs **monomial coefficients** of degree $K-2$. The dimensions (35, 84) are consistent with that.
- The factor $1/2$ in `P_matrix(K)/2` rescales all rows uniformly. It is irrelevant to ranks and quotients, but it should be noted wherever absolute radial values are compared with Step 69/71.

## 4. The coordinate $N_3,N_5,N_7$-fixed branch

### Computational artifact in `analyse()`

The rank of $B$ uses `tol = 1e-8 * sb[0]`, relative to $B$'s own largest singular value. In the torsion-fixed branch:

| Quantity | K=6 | K=8 |
|---|---|---|
| `dim ker` | 210 | 363 |
| `radial_B_norm` | $9.4\times10^{-12}$ | $4.8\times10^{-11}$ |
| `sv_B_tail` | $\sim4\times10^{-12}$ | $\sim6\times10^{-12}$ |

The kernel dimensions are exactly Step 71's top-degree torsion-free flat kernel $F$, on which $dR|_F=0$ was found to roundoff. So $B\approx0$ in its entirety. It is counted as rank 35/84 only because the threshold scales with its own roundoff-sized $\sigma_{\max}$. This is the same pitfall the curvature script explicitly guards against with an absolute threshold.

Hence `rank_B`, `incremental_rank = 0`, `quotient_Y_norm`, and `radial_quotient` in this branch are meaningless. They come from projecting $Y$ onto a noise subspace, which is also why the correction norms are $4\times10^{14}$ and $4\times10^{16}$.

The note dismisses the correction norms but leaves the rank fields standing in the JSON. The fix is to threshold $B$ relative to $\|J_h\|$, or to use an absolute threshold. The correct reading is:

> With coordinate $N_{\ge3}$ fixed, no higher freedom acts on $P_K$ at all.

### What the residual establishes

The least-squares problem
$$
[A_h;TN_h]\,H=-[A_p;TN_p]\,X
$$
was solved with `rcond = 1e-12`. Including near-null directions can only lower the residual. So the K=6 relative residual $3.7\times10^{-3}$ is a genuine linear inconsistency. Precisely:

> There is no first-order deformation with $\delta H_2\in X$ (the Euclidean complement of gauge), $\delta H_2$ gauge component zero, that preserves $E_0,\dots,E_{K-2}$ and all coordinate $N_q$ coefficients, $3\le q\le K-1$.

This is not yet a statement about covariant torsion, for three reasons:

1. **$H_2$-gauge frozen.** $X$ is a Euclidean slice. The test does not let $\delta H_2$ acquire a $\mathcal G_2$ component together with its prolonged higher corrections. A degree-3 Hamiltonian vector field $V$ shifts coordinate $N_3$ by $\mathcal L_VN_1$, which is nonzero because $N_1\neq0$ at a nondegenerate zero. Part or all of the residual may be pure gauge. The cheapest decisive test is to append the 35 columns of $G_2$, with their full one-parameter-pullback higher corrections, to the free variables and recompute the residual.
2. **Coordinate versus covariant.** Even after the gauge quotient, coordinate Taylor coefficients of $N$ differ from $(\nabla^jN)(0)$ by Christoffel terms. At $j\ge1$, those terms contain $\partial^2g(0)$, i.e. they depend linearly on $\delta H_2$ through $\delta\Gamma$. Coupling to $W^-$ therefore appears partly by construction in coordinates. The intrinsic question uses symmetrized covariant derivatives of $N$, or the torsion section, modulo pullback.
3. **Aggregated residual.** The residual is aggregated over 5 columns. The informative quantity is the dimension of the subspace of $W^-$ directions that cannot be lifted, i.e. the rank of the projected residual. At K=8 the relative residual is not even computed, because `rhs_norm` is missing from the JSON.

## 5. Withdrawal of Step-71 inferences

**Withdrawn adequately:**
- the §7.4 statement that the radial hierarchy is the unique carrier;
- the §6 dichotomy;
- the §7 header correction;
- §7.3 recast as restricted.

**Still too strong:**
- **§7.1 title**, "Full Nijenhuis Taylor data are complete coordinates on the tangent." The body denies the intrinsic reading, but the title still asserts it. It should describe a fixed-$H_2$, coordinate, Euclidean-slice fact.
- **§7.4 first bullet**, "early generic local obstruction … unlikely." The data come from one base point at K=8 and two at K=6. "Generic" requires the semicontinuity argument of §2 together with a certified exact base point.
- **Step 72 §6.** "Vindicates Spirit #80's global warning" is interpretation, not something computed here. The Weitzenböck remark is correct as background, but no global quantity was evaluated.

## 6. Theorem-quality formulation

**Proposition A (exact, flat, base-independent).**

- *Hypotheses.* Darboux coordinates; $g=g_0\exp H$, $J=J_0\exp H$ with $H=O(|x|^2)$ anti-$J$; $\lambda$ fixed; $\omega_0\in\Lambda^+$.
- *Conclusion.* The map $H_2\mapsto(\mathrm{Ric}(0)-\lambda g_0,\ N_1)$ is linear, of rank 20 on the 60-dimensional space. Its kernel contains the 35-dimensional quartic-Hamiltonian gauge. The quotient is $U(2)$-isomorphic to $W^-(0)$, while $W^+(0)$ is determined by $(E_0,N_1)$.
- *Status.* Rank values are to be certified rationally; equivariance and irreducibility are exact.

**Proposition B (numerical, at the gen5, $\lambda=-5$ witness, $K\in\{6,8\}$).**

- *Statement.* $P_K\circ dE_K$ restricted to $\ker(dE_0,\dots,dE_{K-2})\cap\{\delta H_2=0\}$ is onto $P_K$, with $\sigma_{\min}=0.25$ at K=6 and $5.0\times10^{-3}$ at K=8.
- *Corollary.* No class in $P_K$ depends on the $W^-(0)$ direction, or on any $H_2$ variation, modulo admissible higher corrections. The radial row in particular is not an obstruction.
- *Nonlinear consequence.* Given a nearby exact solution with constant-rank lower system, order-$K$ compatibility is solvable with $H_2$ fixed.

**Observation C (coordinate, gauge-frozen).** With the gauge component of $\delta H_2$ frozen and coordinate $N_3,\dots,N_{K-1}$ fixed, the $W^-$ directions admit no first-order Einstein lift (K=6 relative residual $3.7\times10^{-3}$). The fixed-torsion higher freedom acts trivially on $P_K$. Neither statement is yet gauge-invariant.

## 7. Exact versus floating

| Exact | Floating, certifiable |
|---|---|
| Linearity and base-independence of $A_2$ | Ranks 20/40/35 (rationally certifiable) |
| Vanishing of curvature on gauge | $\operatorname{rank}B=35,84$; the K=8 margin needs $\sigma_{\max}(B)$ |
| $U(2)$ irreducibility, giving $\cong W^-$ | $\dim\ker A_h=735$ vs 736 |
| "$B$ onto $\Rightarrow$ all classes vanish" | Cancellation norms; inconsistency residual of the torsion-fixed system |
| | All torsion-fixed `rank_B` fields: artifacts, to be discarded |