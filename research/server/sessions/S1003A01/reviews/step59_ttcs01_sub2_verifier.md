# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md",
    "Sessions/S1003A01/workspace/notes/spirit_step58_chiral_bolt_and_zero_charge.md",
    "Sessions/S1003A01/workspace/scripts/step59_chiral_exact.py",
    "Sessions/S1003A01/workspace/data/step59/chiral_exact.json",
    "Sessions/S1003A01/workspace/data/step58/global_exact.json",
    "Sessions/S1003A01/workspace/scripts/step58_exact_bianchiVIII_fast.py",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Independently verify the mathematical content of the proposed all-p Cartan/chirality and smooth-bolt completion for the explicit Bianchi-VIII negative Einstein almost-Kähler pair. Check sign and normalization conventions, whether the identities d_i'+h_i d_i=1 and 2W_i d_i-d_jd_k=-1 really imply W^-=0, whether the displayed W^+ eigenvalues and eta/W3 norms follow, and whether the polar slice formulas prove a smooth metric and 2-form across the bolt for compact-generator period 2π. Identify any hidden issue in the quotient/group lift or normal Euler degree. Also inspect the proposed c2(E)=5χ+6τ zero-charge interpretation and state exactly what is proved for nonisolated zeros versus what remains unknown about Einstein-AK zero germs. Give direct mathematical corrections, not process advice.

## Output

# Verification Memo: Chiral Curvature, Bolt Completion, and Zero-Locus Structure

## 1. Chiral connection identities and $W^- = 0$

**Convention setup.** From the diagonal Bianchi class A structure equations $de^i = h_i\,e^{0i} + 2W_i\,e^{jk}$, the spatial connection is $\omega^{jk} = C_i\,e^i$ with $C_i = W_j + W_k - W_i$. Define $d_i = h_i + C_i$ and $b_i = h_i - C_i$.

The two chiral $\mathfrak{so}(3)$ connections act on $\Lambda^+$ and $\Lambda^-$ respectively. The anti-self-dual $\mathfrak{so}(3)$ has **opposite** structure constants from the self-dual one (because $[\omega_i^-, \omega_j^-] = -2\epsilon_{ijk}\omega_k^-$ versus $+$ for self-dual). Using unnormalized connection 1-forms $d_i\,e^i$ for the $\Lambda^-$ chirality, the curvature 2-form components are:

$$F_k^{-} = (d_k' + h_k d_k)\,e^{0k} + (2W_k d_k - d_i d_j)\,e^{ij}$$

where the minus sign on $d_i d_j$ comes from the opposite-sign cross product. This matches the notes' displayed formula.

**Implication of the identities.** The verified identities $d_i' + h_i d_i = 1$ and $2W_i d_i - d_j d_k = -1$ give:

$$F_k^{-} = e^{0k} - e^{ij} = \omega_k^-$$

Since $\omega_k^- = e^{0k} - e^{ij}$, the curvature is purely anti-self-dual (consistent) and **proportional to the identity** in the $\omega_k^-$ basis. The curvature operator restricted to $\Lambda^-$ is therefore scalar: $\mathcal{R}^-|_{\Lambda^-} = c\,I$ for some constant $c$ (depending on the overall normalization mapping $F_k^-$ to the curvature operator). Since the Singer–Thorpe decomposition gives $\mathcal{R}^-|_{\Lambda^-} = W^- + \frac{s}{12}I$, a scalar block forces $W^- = 0$ exactly (the trace-free part vanishes).

**Convention cross-check at $p \to 1$.** The $W^+$ eigenvalues at $p = 1$ are $(w_1, w_2, w_3) = (1, -2, 1)$ (from the script output). At this limit, $X_2 \to 1$ so $\Omega \to \omega_2$. For $\mathbb{CH}^2$ with $\text{Ric} = -3g$, $s = -12$, and $\kappa = s = -12$, the standard AAD decomposition (equation (11) in the paper) gives:

- $W^+(\Omega) = \frac{\kappa}{6}\Omega$, eigenvalue $\frac{\kappa}{6} = -2$ on $\omega_2$ ✓
- $W^+(\phi) = -\frac{\kappa}{12}\phi$, eigenvalue $-\frac{\kappa}{12} = +1$ on $\omega_1, \omega_3$ ✓

This confirms the curvature conventions are internally consistent. The formula $w_k = 1 - (b_k' + h_k b_k)$ correctly gives the $W^+$ eigenvalues (not the full curvature operator eigenvalues, which would include $s/12 = -1$).

**Computational verification.** The script `step59_chiral_exact.py` performs all arithmetic in the quadratic extension $\mathbb{Q}(p,y)/(y^2 - D)$ and confirms all residuals vanish. This is rigorous exact arithmetic, not floating-point. ✓

## 2. $W^+$ eigenvalues and $|\eta|^2$, $|W_3^+|^2$ formulas

In the $\Lambda^+$ basis $(\omega_1, \omega_2, \omega_3)$ with $|\omega_k|^2 = 2$, the almost-Kähler form is $\Omega = \sqrt{X_1}\,\omega_1 + \sqrt{X_2}\,\omega_2$ with $X_1 + X_2 = 1$.

**Derivation of $|\eta|^2$.** From the AAD $U(2)$ decomposition, $\eta = W^+(\Omega) - \frac{\kappa}{6}\Omega$ where $\frac{\kappa}{6} = X_1 w_1 + X_2 w_2$. Direct computation:

$$\eta = (w_1 - w_2)\sqrt{X_1 X_2}\,(\sqrt{X_2}\,\omega_1 - \sqrt{X_1}\,\omega_2)$$

$$|\eta|^2 = (w_1 - w_2)^2 X_1 X_2 \cdot 2(X_1 + X_2) = 2X_1 X_2(w_1 - w_2)^2 \quad \checkmark$$

**Derivation of $|W_3^+|^2$.** The $W^+$ action on $[\Lambda^{0,2}]$ is diagonal (since $W^+$ is diagonal in $\omega_k$). In the orthonormal basis $\phi = \sqrt{X_2}\,\omega_1 - \sqrt{X_1}\,\omega_2$ and $J\phi = \omega_3$:

$$W^+|_{[\Lambda^{0,2}]} = \begin{pmatrix} X_2 w_1 + X_1 w_2 & 0 \\ 0 & w_3 \end{pmatrix}$$

Subtracting the scalar part $-\frac{\kappa}{12}I$, using $w_1 + w_2 + w_3 = 0$, the trace-free $W_3^+$ has eigenvalue:

$$\lambda = \tfrac{1}{2}(X_2 w_1 + X_1 w_2 - w_3) = \tfrac{1}{2}((1+X_2)w_1 + (1+X_1)w_2)$$

$$|W_3^+|^2 = 2\lambda^2 = \tfrac{1}{2}(X_2 w_1 + X_1 w_2 - w_3)^2 \quad \checkmark$$

Both formulas are confirmed by the computational output. ✓

## 3. Smooth bolt completion

The bolt at $p = 1/3$ ($r = 0$) has $A_1 \to 0$ while $A_2, A_3 \to 6$. The compact generator $E_1$ acts with period $2\pi$ and adjoint weight 2 on $(E_2, E_3)$.

**Metric smoothness.** Three conditions must hold for a smooth metric on the completed disk bundle:

(a) $A_1 = r^2 \cdot f_1(r^2)$ with $f_1(0) = 1$: confirmed from the series $A_1 = r^2 + \frac{2}{9}r^4 + \cdots$ ✓

(b) The horizontal mean $(A_2 + A_3)/2$ is analytic in $r^2$: confirmed, $= 6 + 7r^2 + \cdots$ ✓

(c) The anisotropy $A_2 - A_3 = \frac{10}{3}r^4 + O(r^6)$: divisible by $r^4$ as required by the weight-4 representation $e^{4i\theta}$ in $\text{Re}(z^4\eta_0^2)$ ✓

The analyticity argument is correct: since $p - 1/3$ is analytic in $r^2$, all metric coefficients are analytic in $r^2$, and divisibility at each order follows automatically from the leading behavior.

**2-form smoothness.** The notes compute $C_{dr} = \sqrt{X_2 A_2} = 4r + O(r^3)$ and $C_\theta = \sqrt{X_2 A_3 A_1} = 4r^2 + O(r^4)$. The quantities $f_+/r$ and $f_-/r^3$ are analytic in $r^2$ because:

$$f_+/r = \frac{C_{dr}/r + C_\theta/r^2}{2} = \frac{(4 + O(r^2)) + (4 + O(r^2))}{2} = 4 + O(r^2)$$

$$f_-/r^3 = \frac{C_{dr}/r - C_\theta/r^2}{2r^2}: \quad C_{dr}/r - C_\theta/r^2 = O(r^2) \implies f_-/r^3 = O(1)$$

Both are analytic in $r^2$. The $\Omega_1$ component ($\sqrt{X_1}$-weighted) also extends smoothly since $X_1 = 1 - X_2$ and $X_2 = \frac{8}{3}r^2 + O(r^4)$ is analytic in $r^2$.

The bolt completion argument is rigorous. ✓

## 4. Normal Euler degree: sign correction needed

**Direct calculation.** At the bolt, the connection 1-forms approach:

- Normal: $\omega^{01}|_\Sigma = \sigma_1|_\Sigma = A$ (the principal connection)
- Tangent: $\omega^{23}|_\Sigma = C_1 a_1|_{r=0}\,\sigma_1|_\Sigma = 2A$

Here $C_1 a_1 \to 2$ at $r = 0$ because $C_1 = W_2 + W_3 - W_1 \sim 2/r$ and $a_1 \sim r$.

The curvatures on $\Sigma$:

$$d\omega^{01}|_\Sigma = dA = d\sigma_1 = -2\sigma_2\wedge\sigma_3 = -\tfrac{1}{3}\Omega_\Sigma$$

$$d\omega^{23}|_\Sigma = 2\,dA = -\tfrac{2}{3}\Omega_\Sigma$$

This gives $K_\Sigma = -2/3$ and, by Gauss–Bonnet, $\text{Area}(\Sigma_g) = 6\pi(g-1)$.

The Chern numbers:

$$c_1(\nu) = \frac{1}{2\pi}\int_\Sigma\left(-\tfrac{1}{3}\Omega_\Sigma\right) = -\frac{6\pi(g-1)}{6\pi} = 1 - g$$

$$c_1(T\Sigma) = \frac{1}{2\pi}\int_\Sigma\left(-\tfrac{2}{3}\Omega_\Sigma\right) = 2 - 2g$$

**The ratio is $c_1(\nu) = +\tfrac{1}{2}\,c_1(T\Sigma)$, not $-\tfrac{1}{2}\,c_1(T\Sigma)$.**

The notes state "$c_1(\text{normal}) = -c_1(T\Sigma)/2$, giving degree $g-1$." The correct statement is $c_1(\nu) = +c_1(T\Sigma)/2 = 1-g$.

**Geometric meaning.** The normal bundle is topologically $T\Sigma^{1/2}$ (a spin structure on $\Sigma_g$), not $K_\Sigma^{1/2}$. For $g \geq 2$: $c_1(\nu) = 1-g < 0$, and the disk bundle is a quotient $\Gamma \backslash SL(2,\mathbb{R}) \times_{SO(2)} D^2$ where $\Gamma$ is a torsion-free cocompact lattice in $SL(2,\mathbb{R})$. The period $2\pi$ of $E_1$ in $SL(2,\mathbb{R})$ is correct (since $e^{2\pi E_1} = I$ in $SL(2,\mathbb{R})$).

**Source of the sign error in the notes.** The notes claim "the tangent connection rotation is $-2\sigma_1$." The correct value is $+2\sigma_1$ (from $\omega^{23}|_\Sigma = 2A$). The sign likely arose from confusing the adjoint action $\text{ad}_{E_1}(E_2) = [E_1, E_2] = -2E_3$ (which has a minus sign from the Lie bracket) with the connection coefficient (which involves additional metric-dependent terms from the Koszul formula).

**Impact.** This sign correction does not affect the local AKE existence theorem, the half-conformal-flatness proof, the closed Goldberg argument, or the curvature integral identities. It affects the identification of the global topology of the bolt completion.

## 5. $c_2(E) = 5\chi + 6\tau$ and existence of zeros

**Chern class calculation.** With $E = \Lambda^{0,1} \otimes \Lambda^{0,2}$ (complex rank 2), using $c_1(\Lambda^{0,1}) = c_1(J)$, $c_2(\Lambda^{0,1}) = c_2(J) = \chi$, and $c_1(\Lambda^{0,2}) = c_1(J)$:

$$c_2(E) = c_2(\Lambda^{0,1}) + c_1(\Lambda^{0,1})\,c_1(\Lambda^{0,2}) + c_1(\Lambda^{0,2})^2 = \chi + c_1^2 + c_1^2 = \chi + 2(2\chi + 3\tau) = 5\chi + 6\tau$$

This is correct. ✓

**Positivity for Einstein $s \neq 0$.** For closed Einstein 4-manifolds: $\chi > 0$ (from the Chern–Gauss–Bonnet integrand being strictly positive when $s \neq 0$) and $2\chi + 3\tau \geq 0$ (Hitchin–Thorpe). Therefore $5\chi + 6\tau = \chi + 2(2\chi + 3\tau) > 0$. The deduction via Armstrong's topological theorem that $q$ must vanish somewhere is valid. ✓

**What the positive $c_2(E)$ proves.** If the torsion section $\nabla\Omega \in \Gamma(E_{\mathbb{R}})$ (real rank 4 on a 4-manifold) were nowhere zero, the localized Euler class would be zero, contradicting $c_2(E) = 5\chi + 6\tau > 0$. So zeros exist.

**What remains unresolved about zero germs.** The following are genuinely open:

(i) **Finite-order vanishing vs. Kähler extension.** Can a negative-Einstein AK germ have $q = 0$ at a point with finite vanishing order without being Kähler in a neighborhood? The AAD unique-continuation result (Proposition 1) applies under the **third Gray condition** ($\text{Ric}'' = 0$ AND $W^+(\Omega) = \frac{\kappa}{6}\Omega$), not under Einstein alone. For a general Einstein AK metric, only $\text{Ric}'' = 0$ holds; the additional condition $\rho_*'' = 0$ (equivalently $W_2^+ = 0$, i.e., $\Omega$ is a Weyl eigenform) is not automatic. The remark in AAD (Remark 1(i)) extends unique continuation to the case where any two of $\{\text{Ric}'', \rho_*'', W_3^+\}$ vanish, but this still requires one extra vanishing beyond Einstein.

(ii) **Index structure at zeros.** Even with $c_2(E) > 0$, the local index of an individual zero can be negative (the principal-part analysis in the notes constructs a type-compatible linear section $f = z$ with positive index, but also permits $f = \bar{z}$ with negative index). No mechanism from the Einstein equations alone forces all zero indices to be positive. Therefore $c_2(E) > 0$ does not by itself bound the number or structure of zeros.

(iii) **Attachment to the strict branch.** The explicit Bianchi VIII pair has $q > 0$ on $(1/3, 1)$ with $q \to 0$ only at the ACH end ($p \to 1$). Whether a different solution branch can have $q \to 0$ at a finite point and continue as a strict AKE germ on the other side is unknown. The prolonged Einstein AK system is real-analytic in the strict region, so the zero set is real-analytic where $q > 0$; the behavior at $q = 0$ is controlled by a degenerate ODE/PDE whose local solution space has not been classified.

## 6. Minor additional observations

**Integral identities.** The balance $\int(|\eta|^2 + 2|W_3^+|^2 + \frac{3q^2}{16} - \frac{3q}{2}) = 0$ is a nontrivial identity relating curvature and torsion profiles. It was derived conditionally on the all-$p$ half-conformal identity ($W^- = 0$), which is now established by the chiral Cartan calculation. The integrals are computed per orbit volume in `step58_global_exact.py` and are exact rational numbers. This identity is now unconditional. ✓

**Novelty.** Armstrong's 2002 paper remains unavailable. The rational Bianchi VIII AKE pair may or may not be known. The geometric content (explicit half-conformally-flat negative-Einstein strictly-AK structure with computable global invariants) is valuable regardless of priority, as it provides a concrete testing ground for any proposed approach to the closed Goldberg problem.