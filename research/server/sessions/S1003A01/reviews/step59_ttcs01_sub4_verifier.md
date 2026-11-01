# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step58_chiral_bolt_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Sessions/S1003A01/workspace/notes/step56_soldered_instanton_and_SU2_AKE.md",
    "Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Analyze the zero of the torsion/Nijenhuis section in the closed four-dimensional negative-Einstein almost-Kähler problem. Starting from alpha=∇Ω as a section of E=Λ^{0,1}⊗Λ^{0,2}, the soldered equations (d_b alpha)^-=0, d_b^*alpha=2eta, and the AAD Bianchi/Weitzenböck equations recorded in the supplied notes, derive the strongest trustworthy leading-order constraints at a zero alpha(p)=0. Determine what can and cannot be concluded about vanishing order, isolated local index, sign of that index, and localized top Chern charge. Explore a consequential new route: whether Einstein curvature identities force the leading homogeneous coefficient map into a proper algebraic class incompatible with positive total c2, or instead allow the principal f=z model. Clearly distinguish a proved derivation from a plausible conjecture and point to the next decisive calculation.

## Output

# Verification Memo: Zero-Locus Analysis of the Torsion Section in Closed Negative-Einstein Almost-Kähler Four-Manifolds

## 1. Topological forcing: the localized Euler class

The bundle $E = [[\Lambda^{0,1}\otimes\Lambda^{0,2}]]$ is a real rank-4 bundle (underlying a complex rank-2 bundle) over $M^4$. Its top Chern class is computed by the splitting principle:

$$c_2(E) = c_2(\Lambda^{0,1}) + c_1(\Lambda^{0,2})\cdot c_1(\Lambda^{0,1}) + c_1(\Lambda^{0,2})^2$$

Using $c_1(\Lambda^{0,1}) = -c_1$, $c_2(\Lambda^{0,1}) = c_2(TM) = \chi$, $c_1(\Lambda^{0,2}) = -c_1$:

$$c_2(E) = \chi + c_1^2 + c_1^2 = \chi + 2(2\chi+3\tau) = 5\chi + 6\tau$$

**This derivation is clean.** For a closed Einstein four-manifold with $s < 0$: Hitchin–Thorpe gives $2\chi+3\tau \geq 0$, and $\chi > 0$ follows from $8\pi^2\chi = \int(|W|^2 + s^2/6) > 0$. Therefore $5\chi + 6\tau \geq \chi > 0$. Armstrong's theorem (AAD Lemma 2) states that nowhere-vanishing Nijenhuis tensor forces $5\chi+6\tau = 0$, which contradicts the Einstein inequality. **Every closed negative-Einstein AK four-manifold has a zero of $\nabla\Omega$.** This is a proved statement combining Armstrong, Hitchin–Thorpe, and Chern–Gauss–Bonnet.

The section $\alpha = \nabla\Omega$ of $E$ has localized Euler class $c_2(E) = 5\chi+6\tau > 0$. If zeros are isolated and transverse, the signed index sum equals $5\chi+6\tau$. If the zero set is higher-dimensional (a real-analytic subvariety, by analyticity of Einstein metrics via DeTurck–Kazdan), the localization requires the Euler class of the normal data, not just a point-index count. The spirit note's warning against assuming isolatedness or positivity of individual indices is correct.

## 2. Leading-order analysis at a zero: what the principal symbol determines

At $p$ where $\alpha(p) = 0$, choose $J$-standard coordinates with orthonormal basis $\{e_i\}$, $Je_1 = e_2$, $Je_3 = e_4$, and the AAD gauge $\phi = e^{13} - e^{24}$. The section is $\alpha = a\otimes\phi - Ja\otimes J\phi$ with $a(p) = 0$.

The ASD instanton equation $(d_b\alpha)^- = 0$ at the symbol level constrains the $\mathbb{C}$-linear part of the leading coefficient: writing $f_i(z) = cz_i + (Bz)_i$ in complex coordinates $z_1, z_2$:

$$\partial_{z_1}f_2 = 0, \quad \partial_{z_2}f_1 = 0, \quad \partial_{z_1}f_1 = \partial_{z_2}f_2$$

This forces the holomorphic part to be $cI$ (scalar times identity), leaving the antiholomorphic part $B \in M_{2\times 2}(\mathbb{C})$ unconstrained. **This derivation is verified.**

**At the zero itself, $(d_b\alpha)^- = 0$ is automatic** and imposes no constraint on the leading jet. This follows from the Ricci identity (AAD equation (23)) at $p$:

$$da(p) = -R(J\phi)(p), \qquad d(Ja)(p) = -R(\phi)(p)$$

For Einstein, $R(\phi) \in \Lambda^+$ (since $\widetilde{\text{Ric}_0} = 0$ and $W^\pm$ preserves self-duality type). So $da(p)$ and $d(Ja)(p)$ are purely self-dual, giving $(da)^-(p) = 0$ identically. **This is a proved statement** from the Einstein condition and the structure of the curvature operator.

## 3. The local index: both signs are symbol-compatible

The $\mathbb{R}$-linear map $T: v \mapsto cv + B\bar{v}$ on $\mathbb{C}^2 \cong \mathbb{R}^4$ has real determinant

$$\det_{\mathbb{R}}(T) = \det(|c|^2 I - \bar{B}B)$$

(computed via the $(z,\bar{z})$ block matrix $\begin{pmatrix}cI & B \\ \bar{B} & \bar{c}I\end{pmatrix}$).

**Positive index example**: $f = z$ (i.e., $c = 1$, $B = 0$): $\det = 1 > 0$, index $= +1$.

**Negative index example**: $f(z_1,z_2) = (z_1 + 2\bar{z}_1, z_2)$ (i.e., $c=1$, $B = \text{diag}(2,0)$): $\det(I - \bar{B}B) = \det\begin{pmatrix}-3 & 0\\0 & 1\end{pmatrix} = -3 < 0$, index $= -1$.

Both satisfy the principal-symbol constraint $a_{12} = a_{21} = 0$, $a_{11} = a_{22} = 1$. **The principal symbol of the ASD equation does not constrain the sign of the local index.** This is a concrete algebraic verification.

## 4. What the Einstein AK equations determine at a zero

At $p$ with $\nabla\Omega(p) = 0$: $q(p) = 0$, $\kappa(p) = s$, and the curvature at $p$ decomposes as:

**Self-dual Weyl**: $W_1^+(p)$: acts as $s/6$ on $\Omega$ and $-s/12$ on $[[\Lambda^{0,2}]]$ (net $R$ eigenvalue on $[[\Lambda^{0,2}]]$ is zero since $s/12 - s/12 = 0$).

$W_2^+(p)$: determined by $\eta(p) = \rho_*''(p)$. Since $\nabla^*\nabla\Omega(p) = 2\eta(p)$ (from $q = 0$), and $\nabla^*\nabla\Omega = -\sum_i \nabla^2_{e_i,e_i}\Omega$, we have $\eta(p) \neq 0$ generically. **This is the central structural point**: the metric is not "instantaneously Kähler–Einstein" at $p$ even though $\nabla J(p) = 0$, because the curvature retains $W_2^+ \neq 0$.

$W_3^+(p)$: parametrized by $(\lambda, \mu) \in \mathbb{R}^2$, free at this order.

**Antisymmetric part of $\nabla a$**: From the Ricci identity at $p$:
$$da(p) = -\eta_2\Omega - \mu\phi + \lambda J\phi, \qquad d(Ja)(p) = -\eta_1\Omega - \lambda\phi - \mu J\phi$$

where $\eta = \eta_1\phi + \eta_2 J\phi$. This fixes the 6 real parameters of the antisymmetric part $A$ of $\nabla a$, in terms of $(\eta_1, \eta_2, \lambda, \mu)$.

**Symmetric part of $\nabla a$**: The divergence equation $\nabla^*\nabla\Omega = 2\eta$ gives:
$$\text{tr}(S) = \sum_i \nabla_i a_i = -2\eta_1$$

This is ONE real constraint on the 10-parameter symmetric part $S$, leaving 9 free parameters (the traceless symmetric part of $\nabla a$).

**Consistency check**: The $J\phi$-component of the divergence equation gives $-\langle da, \Omega\rangle = 2\eta_2$. Substituting $da(p) = -\eta_2\Omega - \mu\phi + \lambda J\phi$: $\langle da, \Omega\rangle = -2\eta_2$, so $-(-2\eta_2) = 2\eta_2$. ✓ This is a tautology, not an independent constraint.

**No further constraint from the ASD equation**: As shown in §2, $(d_b\alpha)^-(p) = 0$ is automatic.

**Summary of free parameters in the leading coefficient $L = S + A$**:
- $A$: determined by $(\eta_1, \eta_2, \lambda, \mu)$ — 4 parameters from curvature at $p$
- $S$: 9 free parameters (traceless symmetric part) + $\eta_1$ (trace, determined by curvature)
- Additional free: $W^-(p)$ has 5 parameters, $W_3^+(p)$ contributes $(\lambda, \mu)$ to $A$

The determinant $\det(L) = \det(S+A)$ depends on all these parameters. With 9 free parameters in $S$ alone, the sign of $\det(L)$ is not determined. **There is no proved algebraic restriction on the local index from the 2-jet analysis at a zero.**

## 5. The $f = z$ model: status

The model $f_1 = z_1$, $f_2 = z_2$ (holomorphic part $c = 1$, antiholomorphic part $B = 0$) satisfies:
- Principal symbol: ✓ ($a_{12} = a_{21} = 0$, $a_{11} = a_{22} = 1$)
- ASD at zero: ✓ (automatic)
- Divergence: $\text{div}(a) = 2$ (nonzero), sources $\eta_1 = -1 \neq 0$

This model has local index $+1$. Its nonzero divergence is consistent with $\eta(p) \neq 0$. **It satisfies all necessary conditions at the leading order.** Whether it extends to a solution of the full prolonged Einstein AK system at the zero remains unresolved. The spirit note correctly identifies this gap: "It is NOT a constructed Einstein AK germ or a solution of all prolonged AAD equations."

To determine whether the $f = z$ model actually occurs, one must solve the prolongation system for the 3-jet of $\Omega$ at $p$, using the Weitzenböck formula (Step 55, eq. 3.8) evaluated at $p$:

$$(∇^*∇\alpha)_X(p) = \left[\tfrac{1}{2}dq_X - 2\langle(\delta W_3^+)_{JX}, \Omega\rangle\right]\Omega + 2(\nabla_X\eta)'' + 2\nabla_{J\eta(X)}\Omega \Big|_p$$

The LHS involves the 3-jet of $\Omega$; the RHS involves $(\nabla\eta)(p)$ and $(\delta W_3^+)(p)$, which are themselves 3-jet quantities. The equation is an identity among 3-jets, not an additional constraint on the 2-jet. **No obstruction to the $f = z$ model arises at this order.**

## 6. What cannot be concluded

**Vanishing order**: The Einstein metric is real-analytic (DeTurck–Kazdan), and $\Omega$ is analytic (harmonic form on an analytic Riemannian manifold). So $\nabla\Omega$ is analytic, and its zero set is a proper analytic subvariety with finite vanishing order at every point. **Proved, but the vanishing order is not determined a priori.**

**Isolated zeros**: Not established. The zero set could be a surface (codimension 2 in $M^4$). The AAD Theorem 1 local model (for the third Gray condition) has zeros forming a codimension-2 set in $M^4$ (corresponding to zeros of $dw$ on the base surface $\Sigma$). For the negative-Einstein case without the third Gray condition, the dimension of the zero set is unknown.

**Sign of index**: Not determined by the present analysis. Both signs are compatible with all established constraints.

**Localized top Chern charge**: $c_2(E) = 5\chi + 6\tau > 0$ is proved. Its localization to the zero set is well-defined but requires knowledge of the zero-set geometry for non-isolated zeros.

## 7. The proposed route: algebraic incompatibility with positive $c_2$

The route asks whether Einstein identities force the leading coefficient $L$ into an algebraic subset where $\det(L) \leq 0$, contradicting $c_2 > 0$. **This route is not established.** The analysis shows:

- The holomorphic part of $L$ is constrained to $cI$ (2 real parameters)
- The antiholomorphic part $B$ and the curvature parameters give enough freedom for both signs of $\det(L)$
- No prolongation constraint at the 2-jet or 3-jet level restricts the index sign

**For this route to succeed**, one would need:

(a) A constraint from higher prolongation orders that restricts the traceless symmetric part of $\nabla a$, OR

(b) A global argument showing that the analytic continuation of the strict-region structure forces specific behavior at the zero.

Option (b) connects to the explicit Bianchi VIII branch: there, $q > 0$ everywhere on the open manifold and $q \to 0$ only at infinity, so no finite zero exists. A closed manifold forces the zero into the interior, but the local structure at that zero must be compatible with the strict AKE geometry on both sides. This compatibility might impose the missing constraint.

## 8. The genuine next computation

The decisive calculation is a **jet-determination analysis at a zero of $\nabla\Omega$**, using:

1. The full Weitzenböck formula (3.8) and its first covariant derivative at $p$, expressing compatibility conditions among 3-jets
2. The relation $\eta = (\nabla^*\nabla\Omega)''/2$ and its derivative, which couples the 3-jet of $\Omega$ to $\nabla\eta$ and $\delta W_3^+$
3. The differential Bianchi identity (Step 55, eq. 3.6) evaluated at $p$, which constrains $dq$, $\nabla\eta$, $\delta W_3^+$ jointly

The specific test: at degree $N$ in the Taylor expansion, count:
- The number of unknowns: the free components of $\nabla^N\Omega$ at $p$, modulo the type constraint
- The number of equations: from the Einstein AK prolongation system at order $N$
- The compatibility conditions at order $N-1$

If at some finite $N$ the compatibility conditions at order $N-1$ impose a new algebraic relation on the $(N-1)$-jet that cannot be absorbed into the universal identities (equation (1.1) of Step 55, contracted Bianchi, etc.), then an obstruction is obtained.

The Step-55 analysis found that the previously computed apparent obstruction at degree 15 was the universal Ricci-symbol identity (equation 1.1), not a genuine new relation. The computation was done in Darboux gauge at a generic point, not at a zero. **The jet-determination analysis specifically at a zero of $\nabla\Omega$** is a distinct computation, because:

- At the zero, the system has additional degeneracy (the ASD condition is vacuous)
- The curvature parameters $(\eta, W_3^+)$ enter through the Ricci identity rather than through the equation
- The symmetric part of the leading jet has different free count than at a generic point

This computation has not been performed. It is the highest-value next step for the zero-locus approach to Goldberg.

## 9. Connection to the AAD unique-continuation and third-Gray results

The AAD paper proves (Proposition 1) that under the third Gray condition $(\text{Ric}'' = 0, W_2^+ = 0)$, the Weitzenböck equation simplifies to

$$\nabla^*\nabla(\nabla\Omega) + \frac{3s}{4}\nabla\Omega + \nabla_{\text{Ric}_0(\cdot)}\Omega = 0$$

This is a second-order linear elliptic equation on $\nabla\Omega$, and Aronszajn's theorem gives strong unique continuation. For general Einstein AK (not third Gray), the equation (47) has additional nonlinear source terms involving $\eta$ and $W_3^+$. The spirit note's Proposition 3 observation that AAD's zero-analysis uses the third-Gray branch structure (specifically the opposite Kähler structure $(g,I)$) is accurate: AAD's Proposition 3 extends $(g,I)$ across zeros using the formula

$$\Omega_I = -\Omega - \frac{2}{\Delta(|\nabla^{k-1}\Omega|^2)} dd^J(|\nabla^{k-1}\Omega|^2)$$

which requires the Kähler structure of $(g,I)$, not available in the general Einstein case. The general Einstein AK zero analysis genuinely lacks this tool.

## 10. Summary assessment

| Statement | Status |
|-----------|--------|
| $c_2(E) = 5\chi+6\tau > 0$ for closed Einstein $s<0$ | **Proved** |
| Zeros of $\nabla\Omega$ must exist | **Proved** |
| Zeros have finite vanishing order | **Proved** (analyticity) |
| $(d_b\alpha)^- = 0$ is automatic at zeros | **Proved** |
| $\eta(p) \neq 0$ generically at a zero | **Proved** (structure) |
| $f = z$ model satisfies principal conditions | **Proved** |
| Full prolongation admits $f = z$ | **Unresolved** |
| Local index sign is determined | **Not established** |
| Zero-locus route proves Goldberg | **Not established** |

The zero-locus approach has produced the correct topological framework ($c_2 > 0$, zeros forced) and identified the precise gap: the algebraic system on the leading jet at a zero of $\nabla\Omega$, beyond the principal symbol, has not been fully resolved. The computation that would close or definitively assess this route is the jet-determination analysis at a zero, checking whether higher prolongation compatibility forces the index sign or leaves it free.