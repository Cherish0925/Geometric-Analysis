# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 72,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step72_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step72_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the final Step-72 local conclusion after the correction-independent lift quotient was computed. Read the note, all three central scripts, and outputs. Check: (1) the identification of ker(dE0,dN1)/quartic-Hamiltonian gauge with the five-dimensional W^-(0) block; (2) the linear-algebra statement that a chosen W^- lift changes P_K(E_K), but its class modulo J_h ker A_h vanishes at K=6 and K=8 because B has full target rank; (3) whether the explicit radial conclusions and cancellation norms are interpreted correctly; (4) why the attempted fixing of coordinate N3,N5,N7 does not yet define covariant fixed torsion, and what its nonzero residual actually establishes; and (5) whether the revised note withdraws all stronger unsupported Step-71 inferences. Give a concise theorem-quality formulation, name any remaining computational flaw or normalization issue, and distinguish exact structural facts from floating evidence.

## Integrated Scientific Memo

# Verification memo — corrected Step-72 local conclusion

**The central lift-quotient conclusion is correct:** at the tested gen5, \(\lambda=-5\) witness, the computed fixed-\(H_2\) higher-jet freedom maps onto the entire next scalar target at \(K=6,8\). Consequently, the response of any chosen \(W^-(0)\) lift—including its radial component—has zero correction-independent class. This is a finite-order, first-order result supported by floating-point calculations, not yet an exact nonlinear or all-orders existence theorem.

The remaining substantive issues are the spurious ranks in the coordinate-torsion-fixed calculation, incomplete certification of numerical kernels and ranks, an orientation check, and several overstrong or stale textual statements.

## 1. Theorem-quality formulation

Let \(V_2\) be the 60-dimensional space of quadratic anti-\(J\) metric coefficients, and let
\[
A_2=(dE_0,dN_1)|_{V_2},\qquad
\mathcal G_2\subset V_2
\]
be the image of homogeneous quartic Hamiltonians acting on the constant metric.

For \(K=6,8\), write
\[
A=[A_p\ A_h]=d(E_0,E_2,\ldots,E_{K-2}),\qquad
J=[J_p\ J_h]=P_KdE_K,
\]
where \(p=H_2\) and \(h=(H_4,\ldots,H_K)\).

**Structural proposition.** If \(X\) represents degree-two physical directions and \(A_hH_0=-A_pX\) is solvable, every other lift is
\[
H_0+N_hC,\qquad \operatorname{im}N_h=\ker A_h.
\]
Its scalar response is
\[
Y+BC,\qquad
Y=J_pX+J_hH_0,\qquad B=J_hN_h.
\]
Thus the intrinsic response is only
\[
[Y]\in\mathcal P_K/\operatorname{im}(J_h\ker A_h).
\]
If \(B\) is onto, this quotient is zero **for every admissibly liftable degree-two direction**, not specifically for \(W^-\).

**Computed finite-jet statement.** At the supplied numerical witness:
\[
\dim(\ker A_2/\mathcal G_2)=40-35=5,
\]
and the linearized curvature map identifies this quotient numerically with \(S^2_0(\Lambda^-)\) in the script’s orientation. Moreover,
\[
\begin{array}{c|cc}
K&6&8\\ \hline
\dim\ker A_h&361&735\\
\operatorname{rank}B&35&84\\
\dim\mathcal P_K&35&84\\
\sigma_{\min}(B)&0.251516&0.00498409
\end{array}
\]
under the scripts’ rank thresholds. Hence the computed correction-independent scalar class vanishes at both orders.

The algebraic implication “\(B\) onto \(\Rightarrow [Y]=0\)” is exact. The stated ranks and their applicability at an exact Einstein jet remain numerical evidence requiring certification.

## 2. Degree-two quotient and curvature identification

### Exact structural content

Because \(H=O(|x|^2)\),
\[
g(0)=I,\qquad \partial g(0)=0.
\]
The quadratic part of \(g=\exp H\) is exactly \(H_2\); higher exponential terms do not contribute to curvature at the origin. Likewise, the degree-one part of the Nijenhuis tensor depends linearly on \(H_2\). Therefore **\(A_2\) is base-jet independent and independent of \(\lambda\)**. Strictly, \(H_2\mapsto E_0\) is affine because of the constant \(-\lambda I\); its derivative is linear.

Quartic Hamiltonians form a 35-dimensional space. Their cubic vector fields produce quadratic pure-coordinate metric variations. The map into metric variations is injective: a homogeneous cubic Euclidean Killing field must vanish. Tensor naturality gives
\[
\mathcal G_2\subset\ker A_2,
\qquad
\delta\mathrm{Rm}(0)|_{\mathcal G_2}=0.
\]
These are exact facts, not conclusions inferred from \(10^{-15}\) residuals.

### What the supplied calculation verifies

The scripts find \(\operatorname{rank}A_2=20\), with five unit singular values after removing gauge and all remaining singular values below \(2.2\times10^{-15}\). On the resulting five-dimensional slice:
\[
\|W^+\|=1.606\times10^{-15},
\]
whereas the five \(W^-\) singular values are
\[
1.93649,\ 1.93649,\ 1.89737,\ 1.67332,\ 1.63299.
\]
Both chiral blocks vanish on gauge to approximately \(10^{-15}\). The curvature script correctly uses an **absolute** threshold when testing these nearly zero maps.

This strongly supports the advertised identification
\[
\ker A_2/\mathcal G_2\simeq S^2_0(\Lambda^-).
\]
However, the supplied files do not contain an exact rank certificate or a complete representation-theoretic proof. Equivariance and irreducibility explain the identification **once the dimension and a nonzero equivariant curvature map are established**; they do not themselves certify the numerical dimension count. The note’s phrase “exactly … numerically and representation-theoretically” should distinguish these levels.

The script defines chirality using
\[
(e^{01}\pm e^{23}),\quad(e^{02}\pm e^{31}),\quad(e^{03}\pm e^{12}).
\]
This fixes a standard coordinate orientation. To identify its minus block with \(W^-\) in the **complex orientation**, one must also check that the imported \(J_0\) has its fundamental form in the plus span. That imported matrix is not included here. The overall Riemann-sign convention can change the map’s sign, but not these rank conclusions.

The unequal nonzero singular values are coefficient-norm artifacts, not invariant curvature constants.

## 3. Lift dependence, radial response, and explicit cancellation

The selected minimum-coefficient-norm lifts genuinely have rank-five scalar responses. Their singular values are of order \(10^3\) at \(K=6\) and \(10^5\) at \(K=8\), far above roundoff. Thus it is correct to say that **a selected lift responds strongly to the five physical curvature directions**. It is incorrect to promote this to an intrinsic curvature-to-compatibility map.

Using the current JSON rather than the note’s older \(K=6\) figures:

| Quantity | \(K=6\) | \(K=8\) |
|---|---:|---:|
| \(\|\ell_K^TY\|\) | \(165.576\) | \(522.637\) |
| \(\|\ell_K^TB\|\) | \(7.24873\) | \(0.925929\) |
| \(\|(I-\Pi_B)Y\|\) | \(8.0453\times10^{-11}\) | \(4.1787\times10^{-10}\) |
| \(\|\ell_K^T(I-\Pi_B)Y\|\) | \(1.5916\times10^{-12}\) | \(2.0060\times10^{-11}\) |
| \(\|Y+BC\|\) | \(1.8265\times10^{-11}\) | \(5.3084\times10^{-9}\) |
| \(\|N_hC\|\) | \(262.522\) | \(81428.1\) |

In particular, the radial row is **movable**, not torsion-only or intrinsically \(W^-\)-dependent. Once \(B\) has full row rank, its orthogonal complement is zero; the tiny projection residual is then a consistency check, not separate evidence of a subtle factorization.

### Radial normalization

For \(K-2=2m\), the script correctly constructs
\[
\Delta^m x^\alpha\big|_0
=
m!\prod_i\frac{\alpha_i!}{(\alpha_i/2)!}
\]
when every \(\alpha_i\) is even, and zero otherwise. It subsequently normalizes that coefficient row to unit Euclidean norm.

Thus the quoted radial values use:

- ordinary monomial coefficient pairing, assuming the imported \(P\)-matrix convention;
- a unit coefficient-Euclidean radial row;
- \(P_{\mathrm{matrix}}/2\);
- coefficient-Euclidean physical bases and minimum-norm lifts.

These choices do not affect rank or vanishing of quotient classes, but they do affect every absolute norm.

### Explicit cancellation is not fully verified as an admissible correction

The script reports \(Y+BC\), but not
\[
\|A_hN_h\|,\qquad
\|A_hN_hC\|,\qquad
\|A_h(H_0+N_hC)+A_pX\|.
\]
Since \(N_h\) is a numerically truncated kernel, these quantities are needed to verify that explicit cancellation preserves the lower equations to the claimed accuracy. This matters especially for the \(K=8\) correction of norm \(8.14\times10^4\).

The \(K=8\) kernel dimension also differs from Step 71’s \(736\), which should describe the same fixed-\(H_2\) lower system. A cutoff or conditioning explanation is plausible, but not established. The singular values around the \(A_h\) cutoff and \(\sigma_{\max}(B)\) are not recorded. Consequently, neither the harmlessness of the discrepancy nor a quantitative rank-stability margin is demonstrated.

## 4. Coordinate torsion fixing: meaning and numerical flaw

The augmented test solves
\[
\begin{bmatrix}A_h\\T_{Nh}\end{bmatrix}H
=
-\begin{bmatrix}A_p\\T_{Np}\end{bmatrix}X,
\]
where \(T_N\) fixes coordinate \(N_3,N_5,\ldots,N_{K-1}\). Including their \(H_2\) contributions is correct, but does not make these constraints covariant.

A quartic Hamiltonian generates a cubic vector field \(V_3\). Under its genuine pullback,
\[
\delta N=\mathcal L_{V_3}N,
\]
so, in particular, \(N_3\) changes through \(\mathcal L_{V_3}N_1\). The same pullback produces linked corrections in \(H_2,H_4,\ldots\). The test fixes the gauge component of \(H_2\) and does not allow this full prolonged gauge action.

Covariant derivatives of \(N\) also contain connection corrections. Here \(N(0)=0\) and \(\Gamma(0)=0\), so first derivatives at the origin agree with coordinate derivatives; the relevant discrepancy appears in higher derivatives, through terms such as \(\partial\Gamma\,\partial N\). Fixing all displayed coordinate coefficients is therefore not equivalent to fixing covariant torsion jets modulo Hamiltonian pullback.

### What the nonzero residual establishes

At \(K=6\), the augmented five-column least-squares residual is
\[
47.8135,\qquad
\frac{47.8135}{12870.463}=3.7150\times10^{-3},
\]
rather than the unrestricted residual of order \(10^{-11}\). This supports a precise conclusion:

> The five-column physical slice does not admit a simultaneous coordinate-torsion-fixed Einstein lift to numerical precision under the tested solver and gauge choice; at least one physical combination fails this test.

It does **not** establish that every nonzero \(W^-\) direction is incompatible. That requires the rank of the projected residual matrix, not merely its Frobenius norm. Nor does it establish incompatibility with covariantly fixed torsion.

At \(K=8\), the absolute residual is \(9301.93\), but the supplied JSON lacks `rhs_norm` and relative residual, despite the current script writing those fields. This is a script/output-version mismatch. Conditioning and mixed equation scales also prevent treating this absolute number as a normalized geometric obstruction.

### Remaining computational flaw

In the augmented branch, `analyse()` computes the rank of \(B\) using
\[
10^{-8}\sigma_{\max}(B)
\]
even when \(B\) is at the numerical-zero scale. It consequently reports full ranks \(35,84\) using tail singular values of order \(10^{-12}\). Step 71 identifies the corresponding kernel dimensions \(210,363\) with the top-degree torsion-free kernel, on which the newest scalar channel vanishes. This is the familiar failure of a self-relative rank test on a nearly zero matrix.

Accordingly, the augmented branch’s reported full ranks, zero incremental ranks, quotient norms, and cancellations must be discarded as geometric evidence. The \(4.26\times10^{14}\) and \(4.35\times10^{16}\) corrections exploit numerical leakage; moreover, they cannot repair an inconsistent affine lower system. An absolute or ambient-map-scaled tolerance is required here.

The revised note correctly dismisses these enormous corrections, but should explicitly identify the rank/projection failure rather than dismissing only the correction norms.

## 5. Withdrawal of Step-71 inferences

The revisions successfully withdraw the central unsupported interpretations:

- the radial hierarchy as the unique local–global carrier;
- curvature independence inferred from fixed-\(H_2\) tests;
- an intrinsic \(W^-\)-response inferred from one lift;
- coordinate Nijenhuis fixing as a complete intrinsic torsion-fibre description.

**Not all stronger wording has been eliminated:**

1. Step 71’s §7.1 heading still says “Full Nijenhuis Taylor data are complete coordinates on the tangent,” although the body correctly restricts its meaning.
2. Step 72’s claim that “the physical \(H_2\) directions force changes” should be limited to failure to lift the full tested slice, or at least one combination; the residual rank is absent.
3. “Locally viable through the tested orders” and Step 71’s “early generic local obstruction … unlikely” are interpretations of a few numerical witnesses, not proved general statements about nondegenerate index-\(+1\) zeros.
4. The `step72_vary_H2_free.py` docstring still attributes absence of \(H_2\) motion to a nonlinear first-jet cone freezing \(H_2\). That explanation is unsupported and conflicts with the base-independent linear \(A_2\) calculation and the revised note’s more cautious explanation.

The global warning about metric-dependent harmonic projection and the \(W^-\) term in the ASD Weitzenböck equation is compatible with the local conclusion. No global transport or Einstein-gap result was computed here.

Finally, the note’s \(K=6\) projection and cancellation figures differ slightly from the supplied JSON; the table above uses the actual listed output.

## Bottom line

The supported conclusion is **surjectivity of the fixed-\(H_2\) scalar correction map at two tested orders**, with vanishing of the \(W^-\) lift class as an immediate corollary. It does not establish a covariant fixed-torsion obstruction, nonlinear extendability, formal convergence, or a global Einstein gap.

The precise unresolved mathematical objects are an exact certificate for the degree-two curvature identification, certified ranks and admissible cancellation at the numerical witness, and the corresponding prolongation problem for **covariant torsion jets modulo one genuine Hamiltonian pullback**.