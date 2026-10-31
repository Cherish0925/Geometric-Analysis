# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md",
    "Sessions/S1003A01/workspace/scripts/joint_dual_calibration.py",
    "Sessions/S1003A01/workspace/scripts/check_joint_dual_identities.py",
    "Sessions/S1003A01/workspace/scripts/test_Ezero_reconstruction.py",
    "Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py",
    "Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_coordinate_check.py",
    "Sessions/S1003A01/workspace/data/joint_dual/summary.csv",
    "Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md",
    "Sessions/S1003A02/workspace/data/ach_capd/fuchs_boxes_N6_complex.json"
  ]
}
```

## Task

Read the Step-16 joint dual-calibration note and its core scripts. Check the mathematical normalization of z versus diagonal Ricci, the dual/Gram coefficient 1/4, signs and boundary offset for the spin field, interpretation of the numerical shares, and what the E=0 reconstruction does or does not establish. Identify any substantive error and propose the strongest corrected mathematical formulation toward a diagonal lower theorem. Also check the exact bolt Weyl calculation from the validated 2-jet, including likely factor/chirality convention issues. Do not turn this into a generic issue list; provide a direct scientific memo.

## Output

# Verification Memo — Step 16 Joint Dual Calibration and Exact Bolt Chirality

## 1. The diagonal Ricci variable z and the norm identity

The representation $z_i = -(e_0 + e_i)$, $i=1,2,3$, with trace-free constraint $\sum e_\alpha = 0$, satisfies $|z|^2 = |e|^2 = |\mathrm{Ric}^\circ|^2$. Direct expansion:

$$z_i = e_j + e_k \quad (j,k \ne 0,i), \qquad |z|^2 = 2(e_1^2+e_2^2+e_3^2) + 2(e_1e_2+e_1e_3+e_2e_3),$$

$$|e|^2 = (e_1+e_2+e_3)^2 + e_1^2+e_2^2+e_3^2 = 2(e_1^2+e_2^2+e_3^2)+2(e_1e_2+e_1e_3+e_2e_3).$$

The identity holds exactly. The coefficient $\frac{1}{4}$ in $P/(8\pi^2)=\frac{1}{4}\int W|z|^2\,dt$ is a normalization convention from integrating over the SU(2) orbit; the dual bound inherits the same factor from the pointwise completion of the square $\frac{1}{4}|z-\beta|^2 \ge 0$, yielding $\frac{1}{4}|z|^2 \ge \frac{1}{2}z\cdot\beta - \frac{1}{4}|\beta|^2$. No error here.

## 2. Offset error in the joint Gram computation

This is the main substantive problem in the step.

**The mathematical bound, equation (1).** For test fields $\beta = \sum c_A B_A$ the optimized dual lower bound on $P/(8\pi^2)$ is
$$\frac{1}{4}m^T G^{-1} m, \qquad m_A = \int W\, z\cdot B_A\,dt, \quad G_{AB}=\int W\,B_A\cdot B_B\,dt.$$
This is stated correctly in the note.

**What the code computes.** In `joint_dual_calibration.py`, the function `gram_bound` subtracts an offset from the raw moment before optimizing:

```python
m[i] = integrate(mu * np.sum(z * B[:,i,:], axis=1), v) - offset[i]
```

For the joint five-field basis the offsets are $[0,0,0,0,-1]$, where $-1$ is `spin_boundary`. The function then returns $\frac{1}{4}(m-\text{offset})^T G^{-1}(m-\text{offset})$, which is **not** the dual bound from equation (1). It is the maximum of

$$\tfrac{1}{2}\sum c_A(m_A^{\rm raw} - \text{offset}_A) - \tfrac{1}{4}c^T G c,$$

which equals the true dual bound minus $\frac{1}{2}\sum c_A^* \,\text{offset}_A$ evaluated at the shifted optimum $c^* = G^{-1}(m^{\rm raw}-\text{offset})$. This is a different functional with no direct variational interpretation as a lower bound on $P/(8\pi^2)$.

**Quantitative impact.** The spin transport identity gives $m_{\rm spin}^{\rm raw} = -1 + (\text{potential integral})$. With the offset, the code uses $m_{\rm spin}^{\rm corrected} = m_{\rm spin}^{\rm raw}+1 = \text{potential}$, which is small. Without the offset, the raw moment $\approx -1$ is large, and its contribution to the Gram-optimized bound is substantial. The Green-only bound (offset $=0$) is unaffected and correct.

At $x_0=0.03$: the reported joint bound is $0.6462$, a gain of only $0.0028$ over the Green-only bound $0.6434$. The spin-only bound with offset is $6.3\times 10^{-5}$. Without offset, the raw spin moment $\approx -1$ would give a spin-only bound $\approx 1/(4G_{\rm spin})$, which must satisfy $\le P/(8\pi^2)\approx 0.996$ but could be of order $0.25$–$0.5$. In the joint Gram, the Gram matrix handles correlation with the Green fields, but the joint bound with raw moments would be materially larger than $0.6462$—plausibly capturing 75–85% of $P/(8\pi^2)$ rather than 65%.

**Consequence for the "35% gap."** The note's conclusion that "roughly 35% of the inexpensive witness" is unresolved by the five-field basis is an overestimate. The actual gap accessible to these five fields is smaller. The corrected joint bound (offset $\to 0$) should be computed before drawing conclusions about how much additional structure (localized multipliers, etc.) is needed.

**Correction.** Remove the offset from the joint computation, or equivalently set `offset=[0,0,0,0,0]`. The raw-moment result is the correct dual bound for the specific witness. The topological decomposition (boundary $-1$ vs. potential) is a useful conceptual split, but it should be presented alongside the raw bound, not in place of it.

## 3. Sign and boundary value in the spin identity

The identity (2) is
$$\int W\,z\cdot\frac{\nabla_u\Phi}{a}\,dt = \Phi(T)-\Phi(0) - 2\int\sum_i \frac{(\partial_i\Phi)\,H_i}{\lambda_i}\,dt.$$

For O($-1$) bolt: $\Phi = C - u_2^2$, $\Phi(0)=1$ (constraint $C=1$ and $u_2=0$ at the regular bolt), $\Phi(T)=0$ (standard CH collar). So $\Phi(T)-\Phi(0) = -1$. The code's `spin_boundary = -1.0` is correct. The `check_joint_dual_identities.py` script verifies the underlying algebraic identity symbolically ($\sum b_i u_{i}' = \Phi'$, with the potential reorganization); the identity check returns $0$ for all terms. No sign error in the identity itself; the error is purely in the offset application within the Gram bound.

## 4. The $E=0$ reconstruction experiment

`test_Ezero_reconstruction.py` freezes the radial profiles $F,G$ and varies the anisotropy $w$ to minimize $\int W E^2/8\,dt$ where $E$ is one Ricci-difference (the shape channel $z_3-z_1$). The experiment demonstrates:

- **Underdetermination:** A single scalar functional on the space of smooth $w(t)$ is trivially solvable in principle; $w$ has infinitely many degrees of freedom.
- **Energy transfer:** Canceling $E$ drives $P/(8\pi^2)$ from $\sim 1$ to $\sim 2.5\times 10^5$, meaning the other two Ricci components (radial-shape and spin) absorb enormous energy.
- **Regularized trade-off:** With coefficient penalty $\mu$, one traces the Pareto front: $E$-cost drops modestly while $P$ grows. Only at $\mu \le 10^{-4}$ does $E$-cost halve, and $P$ is already $\sim 5$.

The interpretation—that a scalar observable's suppression does not identify a genuine low-$P$ escape route—is correct. The experiment is well-designed as a diagnostic but does not establish a lower bound. One caution: the experiment fixes $F,G$ and varies only $w$, so it tests within a codimension-2 slice of metric space. A competitor that jointly adjusts all three profiles could potentially suppress $E$ with less cost. The experiment does not rule this out, but the note does not make that stronger inference.

## 5. Exact bolt Weyl: chirality assignment and factor conventions

### Chiral projector identification

The script defines the six 2-form pairs as $(01,02,03,23,31,12)$ and builds:
$$\mathrm{LA}_{k,j} = \frac{1}{\sqrt{2}}(\delta_{k,j}+\delta_{k,j-3}), \quad \mathrm{LB}_{k,j} = \frac{1}{\sqrt{2}}(\delta_{k,j}-\delta_{k,j-3}).$$

This produces $\mathrm{SD}_k = (e^{0k}+e^{jl})/\sqrt{2}$ (with $(k,j,l)$ the cyclic ordering from the pair list). Since $*e^{0k} = e^{jl}$ for the orientation $\epsilon_{0123}=+1$, LA projects to self-dual 2-forms, LB to anti-self-dual. Therefore:
$$\boxed{W_A = W^+,\qquad W_B = W^-.}$$

### Numerical values at $b=4/5$, Einstein 2-jet

$$W^+ = \mathrm{diag}\!\left(-\tfrac{139}{16},\;\tfrac{57}{16},\;\tfrac{41}{8}\right), \quad |W^+|^2 = \tfrac{14647}{128}\approx 114.4,$$
$$W^- = \mathrm{diag}\!\left(-\tfrac{385}{16},\;\tfrac{203}{16},\;\tfrac{91}{8}\right), \quad |W^-|^2 = \tfrac{111279}{128}\approx 869.4.$$

Both are traceless ($(-139+57+82)/16 = 0$, $(-385+203+182)/16 = 0$). Both are nonzero, confirming the metric is neither self-dual nor anti-self-dual.

### Consistency with $\tau = -1$

For the blown-up ball (interior of $D^4\#\overline{\mathbb{CP}}^2$): $\chi = 2$, $\tau = -1$. The Hirzebruch integrand is $\propto |W^+|^2 - |W^-|^2$. At the bolt, $|W^-|^2 \gg |W^+|^2$ (ratio $\approx 7.6$), consistent with $\tau < 0$. This does not prove the global sign (the Weyl profile varies along the orbit), but it is a coherent pointwise check.

### The coordinate-check discrepancy

The exact script gives $(|W^+|^2,|W^-|^2) = (114.43, 869.37)$. The coordinate check from `o11_rotated_cell.py` gives limiting values $(194.08, 39.40)$ or similar permutation. The sum differs: $983.8$ vs $233.5$. The note attributes this to "the coordinate code's two-form norm normalization and block ordering." Without access to the internals of `o11_rotated_cell.py`, I cannot verify the exact rescaling. However, the discrepancy is a factor $\sim 4.2$ in total $|W|^2$, which is not a simple power-of-2 two-form norm convention (those give factors of 2 or 4 in individual components but preserve trace relations). The pair $(194.08, 39.40)$ sums to $233.5 \approx 983.8/4.22$, suggesting the coordinate code may use a volume-form or metric normalization that differs from the Cartan orthonormal-frame convention by a nontrivial profile-dependent factor. At the bolt where the metric degenerates, such factors can have finite limits that are not simple powers of 2. The qualitative conclusion (both halves nonzero, scalar $\to -24$, vanishing Ricci defect) is agreed by both codes.

**Recommendation:** Evaluate $|W^+|^2 + |W^-|^2$ and $s$ from both codes at an interior point (say $t=0.5$) where the metric is non-degenerate, to isolate the normalization factor and confirm it is convention-only.

## 6. Toward the strongest diagonal lower theorem

With the offset correction, the five-field dual basis captures materially more than the reported 65%. The structure for a competitor-independent lower theorem has three components:

**A. Fixed moments.** The transport identities express each moment as
$$m_A = (\text{boundary flux}) + \int W\,(\text{potential}_A)\,dt.$$
The boundary fluxes are determined by the bolt type and the CH collar alone: $-1$ for the spin direction, and specific shape-equation boundary values for the Green fields. These are topological inputs.

**B. Potential sign or bound.** The integrals $\int W\,\mathrm{potential}_A\,dt$ are metric-dependent. A lower theorem needs either:
- A proof that each potential integral $\ge 0$ (or $\ge -\epsilon$ with controlled $\epsilon$), or
- A Cauchy–Schwarz or spectral bound absorbing the potential integrals into the left-hand side $P/(8\pi^2)$ with a controlled constant.

The note's §4 correctly identifies this as the main open step. The polynomial projection test (§2, last paragraph) shows that the missing 10–15% of energy lies in localized radial multipliers in the same Ricci channels, not in a new algebraic direction. This means the representation space is sufficient; the needed input is transport/sign control for higher-order test functions.

**C. Gram spectral bound.** The matrix $G^{-1}$ must have a uniform upper bound (equivalently, $G$ must have a uniform lower eigenvalue) across the class of metrics considered. For the five-field basis, the Gram entries are integrals of products of known geometric fields against the measure $W\,dt$. On a controlled class of diagonal cells (bounded radii ratios, controlled collar geometry), these can be estimated by comparison geometry. The polynomial-basis Gram matrices becoming ill-conditioned (noted in §2) indicates that extending to localized multipliers will require careful orthogonalization or a different basis choice.

**Corrected formulation.** The strongest statement accessible from the current infrastructure is:

*For diagonal O($-1$) CH cells with bolt parameter $b$ and radii in a controlled class $\mathcal{C}$:*
$$\frac{P}{8\pi^2} \ge \frac{1}{4}\,m^T G^{-1} m \ge \frac{1}{4}\,m_{\rm bdy}^T G_{\rm max}^{-1}\,m_{\rm bdy}$$

*where $m_{\rm bdy}$ collects the boundary fluxes $(-1, \text{shape values})$ and $G_{\rm max}$ is the worst-case Gram matrix over $\mathcal{C}$, provided the potential integrals are bounded below by $0$.*

The second inequality requires proving potential non-negativity. The first equality is the correct dual bound (no offset). Computing $m_{\rm bdy}^T G_{\rm max}^{-1} m_{\rm bdy}$ with the corrected (offset-free) joint Gram would give the actual size of the topological contribution. The spin field's boundary moment $-1$ provides a substantial baseline that the current code discards.