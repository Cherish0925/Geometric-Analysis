# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Audit the curvature Moser endpoint for the restricted four-dimensional cutoff flow ∂_t g = -2aE, a=χ², E=Ric+g. The claimed endpoint (A03 Step 58) is ‖aF_T(t)‖_∞ ≤ CΓ/t, where F_T=(1+|T|²)^{1/2}, T=Rm+G, Γ=sup(S·H^{1/2}), H=∫η²F². Read the derivation and test for gaps: (1) The H-inequality (eq 1.1): H'+c₀D ≤ C₀Y + C₁(1+r^{-2})H. This comes from 'the tensor calculation of Step 57' — is that tensor calculation actually at proof level, or is it schematic? Check A03 Step 57 (H2_evolution_and_continuation_bridge) if available. (2) The critical absorption Y ≤ Cγ(D+r^{-2}H) uses the localized H=∫η²F² and the maximal-function good support with γ=SH^{1/2}≤Cr²√K₀. Is the smallness of γ justified from the initial data alone (maximal-function threshold), or does it need a first-exit argument? If first-exit, is the bootstrap correctly coupled to the V=∫‖aE‖_∞ metric drift? (3) The q=3 propagation (§3): Y(τ) ≤ CΓH(0)/t from a good slice, then Gronwall with coefficient ∫(1+r^{-2}+S²Y) ≤ Cγ³ + Cr^{-2}t. Verify the Gronwall exponent bound. (4) The Moser iteration (§4): check the recurrence (4.3)-(4.7) and the product convergence (4.8). Does the L_j coefficient with time-cutoff 4^j/t and the S factor give the claimed exponents -3/p₀=-1 (time) and 2/p₀=2/3 (Sobolev) for p₀=3? (5) The final estimate ‖aF(t)‖_∞ ≤ CΓ/t: verify the S^{2/3}(ΓH(0))^{1/3} → Γ reduction uses SH(0)^{1/2}≤Γ correctly. (6) CRITICAL: is this endpoint derived under assumptions that were later repaired? Specifically, the Step 55 joint (Γ,V) bootstrap replaced the assumption S(t)≤2S(0) with Ŝ=e^{8V}S₀. Does the curvature endpoint still work under the repaired bootstrap, or does it assume the old S(t)≤2S(0)? Be explicit about what is proved, what is conditional, and what needs repair.

## Output

## Verification memo: curvature Moser endpoint in A03 Step 58

**Object examined.** The proposed endpoint for the restricted four-dimensional cutoff flow

\[
\partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}_g+g,
\]

namely

\[
\|aF_T(t)\|_{L^\infty}\le \frac{C\Gamma}{t},
\qquad
F_T=(1+|T|^2)^{1/2},
\qquad
T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},
\]

with

\[
H(t)=\int \eta^2F_T^2,\qquad
D(t)=\int \eta^2a|\nabla T|^2,\qquad
Y(t)=\int \eta^2aF_T^3,
\]

and

\[
\Gamma=\sup_{0\le s\le t}\mathcal S(s)H(s)^{1/2}.
\]

**Overall assessment.** The algebra of Step 58 is internally consistent once one accepts a provisional first-exit interval and the tensor differential inequalities. The Moser product exponents are correct. The final reduction

\[
\mathcal S^{2/3}(\Gamma H(0))^{1/3}\le C\Gamma
\]

is correct provided the Sobolev constant is transported by a bounded factor. Under the Step 55 repaired bootstrap, the needed bounded factor is \(e^{8V(t)}\), and on a bootstrap interval with \(V(t)\le V_*\) this is harmless if constants are written with that dependence.

However, the endpoint is not presently a standalone proof-level theorem. It rests on tensor inequalities that the supplied notes still describe as incomplete or schematic, and Step 58 itself omits the metric-drift term \(C_V\|aE\|_\infty H\) that Step 55 requires. The endpoint is therefore a conditional analytic consequence of a provisional interval, not the construction of that interval.

---

## 1. Status of the \(H\)-inequality and the Step 57 tensor calculation

Step 58 uses

\[
H'+c_0D\le C_0Y+C_1(1+r^{-2})H.
\tag{1.1}
\]

It says this is the relative form of the tensor calculation from A03 Step 57.

### 1.1 Removal of an additive volume constant

The removal of an additive support-volume term is sound, provided every zero-order source is supported where \(a\) or \(\eta\) is active and has one of the forms

\[
\int \eta^2a,\quad
\int \eta^2aF,\quad
\int \eta^2aF^2,\quad
\int \eta^2aF^3.
\]

Since \(F\ge 1\), \(0\le a\le 1\), and \(\eta=1\) on \(\operatorname{supp}a\),

\[
\int \eta^2a\le H,\qquad
\int \eta^2aF\le H,\qquad
\int \eta^2aF^2\le H,\qquad
\int \eta^2aF^3=Y.
\]

Thus no support-independent volume constant is needed in the relative inequality. The first-cutoff-derivative terms being of size \(Cr^{-2}H\) is also compatible with the support geometry, because \(|d\chi|\le C/r\), \(|d\eta|\le C/r\), and \(\eta=1\) on the active region of \(a\).

### 1.2 Is Step 57 proof-level?

From the supplied notes, the Step 57 tensor calculation is not visible as a completed index-level derivation. Step 34 explicitly lists several tensor PDE premises as still needing index-level derivation, including:

1. the all-lower curvature variation under the flow,
2. the exact normalization and moving-measure terms,
3. the derivative structure needed for signed Hessian cutoff integration, especially a bound of the form
   \[
   |\nabla B|\le CF|\nabla T|,
   \]
   where \(B\) is the Hessian-cutoff contraction,
4. the corresponding defect variation for \(E=\operatorname{Ric}+g\).

Step 55 treats the signed tensor estimates from Steps 34–35 and A03 Step 57 as available for the bootstrap, but it does not display the full index-level computation. Therefore, based on the visible record, the inequality

\[
H'+c_0D\le C_0Y+C_1(1+r^{-2})H
\]

is a conditional or schematic input unless A03 Step 57 contains the complete all-index calculation. To be proof-level, that calculation must supply:

- the exact evolution equation for \(T=\operatorname{Rm}+G\), including the variation of \(G=g\owedge g/(2(n-1))\);
- verification that \(\nabla T=\nabla\operatorname{Rm}\) for the evolving Levi-Civita connection;
- the signed Hessian-cutoff contraction and its integration by parts;
- the derivative bound on that contraction;
- control of first-cutoff-derivative terms without division by \(a\);
- the moving-measure and norm-variation terms.

### 1.3 Missing metric-drift term in Step 58

Step 55 gives the more complete form

\[
H'+cD\le C_H(1+r^{-2})H+C_0Y+C_V\|aE\|_\infty H.
\tag{1.9}
\]

Step 58 acknowledges that such a term may be retained for the joint metric/Sobolev bootstrap, but its displayed inequality (1.1) omits it. Under the repaired bootstrap this term is not decorative: it is integrated through

\[
V(t)=\int_0^t\|aE(s)\|_\infty\,ds.
\]

Thus, for compatibility with Step 55, the working inequality should be written with the \(C_V\|aE\|_\infty H\) term included. Its presence does not alter the Moser endpoint structurally, but it changes constants by factors such as \(e^{C_VV_*}\).

---

## 2. Critical absorption and the smallness of \(\gamma\)

Step 58 derives

\[
Y\le C\gamma(t)(D+r^{-2}H),
\qquad
\gamma(t)=\mathcal S(t)H(t)^{1/2}.
\tag{2.4}
\]

### 2.1 Validity of the interpolation

The derivation is correct under the stated support relations. Indeed,

\[
Y=\int \eta^2aF^3
=\int F(\chi F)^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\|\chi F\|_{L^4}^2
\le H^{1/2}\|\chi F\|_{L^4}^2.
\]

The local Sobolev inequality is

\[
\|v\|_{L^4}^2
\le \mathcal S\left(\|\nabla v\|_{L^2}^2+r^{-2}\|v\|_{L^2}^2\right).
\]

Because

\[
|dF|\le |\nabla T|,
\qquad
|d\chi|\le C/r,
\]

and \(\eta=1\) on the active support,

\[
\|\nabla(\chi F)\|_{L^2}^2
\le C\int a|\nabla T|^2+C r^{-2}\int F^2
\le C(D+r^{-2}H).
\]

Also \(\|\chi F\|_{L^2}^2\le H\). Therefore

\[
Y\le C\mathcal S H^{1/2}(D+r^{-2}H)
=C\gamma(D+r^{-2}H).
\]

This part is sound.

### 2.2 Initial smallness from maximal-function selection

Step 58 writes

\[
\gamma(0)\lesssim r^2\sqrt{K_0}
\]

when

\[
\mathcal S(0)\lesssim r^2V^{-1/2},
\qquad
H(0)\lesssim K_0V.
\]

This cancellation is correct:

\[
\gamma(0)
=\mathcal S(0)H(0)^{1/2}
\lesssim r^2V^{-1/2}(K_0V)^{1/2}
=r^2\sqrt{K_0}.
\]

Thus the volume dependence cancels. This is the intended critical cancellation.

However, this is only an initial statement. It does not by itself give

\[
\gamma(t)\le \gamma_*
\]

for positive time. The quantities \(H(t)\) and \(\mathcal S(t)\) evolve. Therefore a first-exit or continuity argument is needed to keep \(\gamma(t)\) small.

### 2.3 Coupling to the metric drift \(V(t)\)

Step 55 supplies the correct structural coupling. It sets

\[
V(t)=\int_0^t\|aE(s)\|_\infty\,ds.
\]

The metric distortion satisfies

\[
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0).
\]

In dimension four, the Sobolev constant transports as

\[
\mathcal S(t)\le e^{8V(t)}\mathcal S(0).
\]

The energy satisfies, with the metric-drift term included,

\[
H(t)\le H(0)\exp\{C_H(1+r^{-2})t+C_VV(t)\}.
\]

Therefore

\[
\gamma(t)
=\mathcal S(t)H(t)^{1/2}
\le
\gamma(0)
\exp\left\{8V(t)+\frac12C_VV(t)+C_H\theta\right\}
\]

for \(t\le \theta r^2\), \(r\le1\).

If \(V(t)\le V_*\) and \(\theta\) is chosen so that

\[
\exp\{(8+\tfrac12C_V)V_*+C_H\theta\}\le \frac32,
\]

then initial smallness

\[
\gamma(0)\le \frac{\gamma_*}{2}
\]

improves to

\[
\Gamma(T)\le \frac34\gamma_*.
\]

The defect endpoint in Step 55 gives

\[
\|aE(t)\|_\infty
\le C_E\delta\left(\frac{r^2}{t}\right)^{1/3},
\qquad
\delta=\|E(0)\|_\infty,
\]

and hence

\[
V(T)
\le C_E\delta r^{2/3}T^{2/3}
\le C_E\delta\theta^{2/3}r^2.
\]

Choosing \(\delta\) small relative to \(V_*\), \(\theta\), and \(C_E\) improves the \(V\)-bootstrap.

Thus the coupled \((\Gamma,V)\) bootstrap is structurally correct. It is still conditional on the defect hierarchy and the signed tensor estimates being available at proof level.

---

## 3. The \(q=3\) propagation and the Gronwall exponent

Step 58 obtains from the integrated \(Y\) estimate

\[
\int_0^tY(s)\,ds\le C\Gamma H(0).
\]

Then for each \(t>0\) there exists \(\tau\in[t/4,t/2]\) such that

\[
Y(\tau)\le \frac{C\Gamma H(0)}{t}.
\]

This is a standard good-slice argument and is valid.

The \(p=3\) inequality is

\[
Y'\le C(1+r^{-2}+\mathcal S^2Y)Y.
\]

Integrating from \(\tau\) to \(t\) gives

\[
Y(t)
\le
Y(\tau)
\exp\left(
C\int_\tau^t(1+r^{-2})\,ds
+
C\int_\tau^t\mathcal S(s)^2Y(s)\,ds
\right).
\]

The first term is controlled by \(t\le\theta r^2\):

\[
\int_\tau^t(1+r^{-2})\,ds
\le t(1+r^{-2})
\le \theta r^2+\theta
\le C\theta.
\]

For the second term, Step 58 uses

\[
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le C\mathcal S(0)^2\Gamma H(0)
\le C\Gamma^3,
\]

provided \(\mathcal S(s)\le A\mathcal S(0)\). More precisely, with \(A=e^{8V_*}\),

\[
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le C A^2\Gamma^3.
\]

Therefore the Gronwall exponent is bounded by

\[
C\theta+CA^2\Gamma^3.
\]

If \(\Gamma\le\Gamma_*\) and \(\theta\) is fixed small, this is a finite constant. Step 58 absorbs it into \(C\). Thus

\[
Y(t)\le \frac{C\Gamma H(0)}{t}
\]

and

\[
\mathcal S(t)^2Y(t)
\le \frac{CA^2\Gamma^3}{t}
\]

are valid under the provisional first-exit assumptions.

The \(t^{-1}\) coefficient is used only on positive dyadic slabs and is not integrated down to \(t=0\). That is the correct use.

---

## 4. Moser recurrence and product convergence

Step 58 defines

\[
p_j=3\left(\frac32\right)^j,
\qquad
I_j=[\tau_j,t],
\qquad
\tau_j=t(1-2^{-(j+1)}).
\]

The interpolation identity

\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}
\]

is algebraically correct. Indeed,

\[
K_p=\int \eta^2a^{p-2}F^p,
\qquad
K_{2p}=\int \eta^2a^{2p-2}F^{2p},
\]

and Hölder gives

\[
\int \eta^2a^{3p/2-2}F^{3p/2}
\le
\left(\int \eta^2a^{p-2}F^p\right)^{1/2}
\left(\int \eta^2a^{2p-2}F^{2p}\right)^{1/2}.
\]

Also,

\[
z_p=\eta a^{(p-1)/2}F^{p/2},
\]

so on the active support, where \(\eta=1\) whenever \(a\neq0\),

\[
K_{2p}=\|z_p\|_{L^4}^4.
\]

The energy estimate on \(I_j\) is written as

\[
\sup_{I_{j+1}}K_{p_j}
+
\int_{I_{j+1}}\|\nabla z_{p_j}\|_{L^2}^2
\le
L_j\int_{I_j}K_{p_j},
\]

with

\[
L_j
=
Cp_j^{N+2}
\left(
\frac{4^j}{t}+1+r^{-2}+\frac{A^2\Gamma^3}{t}
\right).
\]

Under \(t\le r^2\le1\) and \(\Gamma\le\Gamma_*\), this can be enlarged to

\[
L_j\le C_{A,\Gamma_*}p_j^{N+2}\frac{4^j}{t}.
\]

The recurrence in Step 58 is

\[
\mathcal M_{p_{j+1},j+1}
\le
C\mathcal S(L_j\mathcal M_{p_j,j})^{3/2},
\]

after using \(L_j\ge r^{-2}\). Writing

\[
m_j=\mathcal M_{p_j,j}^{1/p_j},
\]

one obtains

\[
m_{j+1}
\le
(C\mathcal S)^{2/(3p_j)}L_j^{1/p_j}m_j.
\]

This algebra is correct.

### 4.1 Product convergence

Because

\[
p_j=3\left(\frac32\right)^j,
\]

we have

\[
\frac1{p_j}=\frac13\left(\frac23\right)^j,
\]

so

\[
\sum_{j=0}^\infty\frac1{p_j}=1.
\]

Also,

\[
\sum_{j=0}^\infty \frac{j}{p_j}<\infty,
\qquad
\sum_{j=0}^\infty \frac{\log p_j}{p_j}<\infty.
\]

Thus the product of the polynomial factors \(p_j^{N+2}\) converges.

The time factor in \(L_j\) contributes

\[
\prod_j t^{-1/p_j}=t^{-\sum_j1/p_j}=t^{-1}.
\]

The dyadic factor contributes

\[
\prod_j 4^{j/p_j}
=
4^{\sum_j j/p_j}
<\infty.
\]

The Sobolev factor contributes

\[
\prod_j (C\mathcal S)^{2/(3p_j)}
=
(C\mathcal S)^{(2/3)\sum_j1/p_j}
=
(C\mathcal S)^{2/3}.
\]

Thus the asserted exponents are correct:

\[
\text{time exponent}=-1,
\qquad
\text{Sobolev exponent}=2/3.
\]

### 4.2 Sobolev constant normalization

The recurrence uses a parabolic Sobolev estimate normalized so that the final power is \(\mathcal S^{2/3}\). This is consistent with the endpoint formula in Step 34,

\[
\|af\|_\infty
\le
C\mathcal S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^t H_{p_0}(f,s)\,ds\right)^{1/p_0}.
\]

If one instead uses a different normalization of the local \(L^4\) Sobolev constant, the power of \(\mathcal S\) must be adjusted accordingly. The important point is that the same Sobolev constant convention must be used consistently in:

1. the critical absorption \(Y\le C\gamma(D+r^{-2}H)\);
2. the reaction coefficient \(\mathcal S^2Y\) in the \(K_p\) inequality;
3. the parabolic Moser recurrence.

With the convention used in Step 58, the exponents are coherent.

---

## 5. Final reduction to \(C\Gamma/t\)

The Moser iteration gives

\[
\|aF_T(t)\|_\infty
\le
\frac{C}{t}\mathcal S_*^{2/3}(\Gamma H(0))^{1/3},
\]

where \(\mathcal S_*\) is the Sobolev constant on the relevant positive-time slab. If \(\mathcal S(s)\le A\mathcal S(0)\), then

\[
\mathcal S_*^{2/3}(\Gamma H(0))^{1/3}
\le
A^{2/3}\mathcal S(0)^{2/3}\Gamma^{1/3}H(0)^{1/3}.
\]

But

\[
\mathcal S(0)^{2/3}H(0)^{1/3}
=
\left(\mathcal S(0)H(0)^{1/2}\right)^{2/3}
=
\gamma(0)^{2/3}.
\]

Since \(\gamma(0)\le\Gamma\),

\[
A^{2/3}\Gamma^{1/3}\gamma(0)^{2/3}
\le
A^{2/3}\Gamma.
\]

Therefore

\[
\|aF_T(t)\|_\infty
\le
\frac{CA^{2/3}\Gamma}{t}.
\]

Absorbing \(A^{2/3}\) into \(C\) gives the displayed

\[
\|aF_T(t)\|_\infty\le \frac{C\Gamma}{t}.
\]

This reduction is correct, provided the Sobolev transport factor \(A\) is bounded on the interval. Under Step 55, \(A=e^{8V_*}\), so this is bounded on the provisional bootstrap interval.

---

## 6. Compatibility with the repaired Step 55 bootstrap

This is the central point.

Step 58 often writes as though one has a simple bound

\[
\mathcal S(t)\le C\mathcal S(0).
\]

Step 34 had earlier used a provisional assumption such as

\[
\mathcal S(t)\le 2\mathcal S(0).
\]

Step 55 replaces that by the metric-drift transport estimate

\[
\mathcal S(t)\le e^{8V(t)}\mathcal S(0),
\qquad
V(t)=\int_0^t\|aE(s)\|_\infty\,ds.
\]

On a bootstrap interval with \(V(t)\le V_*\), this gives

\[
\mathcal S(t)\le A\mathcal S(0),
\qquad
A=e^{8V_*}.
\]

If \(V_*\) is chosen small, \(A\) is a fixed constant, for example \(A\le2\) or even smaller. Therefore the Step 58 Moser argument does not require the literal old assumption \(\mathcal S(t)\le2\mathcal S(0)\); it only requires a bounded multiplicative transport of \(\mathcal S\). The repaired bootstrap supplies exactly that.

However, to make Step 58 fully compatible with Step 55, several constants must be rewritten.

### 6.1 The \(H\)-inequality should include the \(V\)-term

The correct working inequality is

\[
H'+cD
\le
C_0Y+C_1(1+r^{-2})H+C_V\|aE\|_\infty H.
\]

Under \(V(t)\le V_*\), Gronwall gives

\[
H(t)\le e^{C\theta+C_VV_*}H(0),
\]

and

\[
\int_0^tD(s)\,ds
\le
C e^{C\theta+C_VV_*}H(0).
\]

Step 58’s simpler estimate

\[
H(t)\le e^{C\theta}H(0)
\]

is recovered only after suppressing the \(V\)-dependence. For a rigorous repaired version, the factor \(e^{C_VV_*}\) should be carried.

### 6.2 The integrated \(Y\) estimate acquires the same bounded factor

Using

\[
Y\le C\gamma(D+r^{-2}H),
\qquad
\gamma\le\Gamma,
\]

one obtains

\[
\int_0^tY(s)\,ds
\le
C\Gamma e^{C\theta+C_VV_*}H(0).
\]

Then, with \(\mathcal S(s)\le A\mathcal S(0)\),

\[
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le
C A^2e^{C\theta+C_VV_*}\Gamma^3.
\]

This still has the required integrable reaction structure. The constants in the \(q=3\) propagation and Moser iteration then depend on \(A\), \(V_*\), \(\theta\), and \(\Gamma_*\), but not on collapse volume or on \(Y(0)\).

### 6.3 The absorption condition must be imposed on the provisional interval

The direct absorption

\[
C_0Y\le \frac{c_0}{2}D+\text{lower terms}
\]

requires

\[
C_0C\gamma(t)\le \frac{c_0}{2}
\]

throughout the interval. This is why the first-exit assumption \(\Gamma\le\gamma_*\) is needed. The Step 55 bootstrap gives a mechanism to improve that assumption from initial smallness, but it does not remove the need for a continuity argument.

Thus the endpoint is valid on any smooth interval where:

1. the tensor inequalities hold;
2. \(\Gamma\le\gamma_*\) with \(\gamma_*\) small enough for absorption;
3. \(V\le V_*\) so that \(\mathcal S(t)\le A\mathcal S(0)\);
4. the defect estimate supplies the integrable bound on \(\|aE\|_\infty\).

---

## 7. What is proved, what is conditional, and what remains to be repaired

### 7.1 What is proved at the algebraic level

Conditional on the tensor differential inequalities and on the existence of a smooth provisional first-exit interval, Step 58 proves the weighted curvature endpoint

\[
\|aF_T(t)\|_\infty
\le
\frac{C(A,\theta,\Gamma_*)\Gamma}{t},
\qquad
0<t\le \theta r^2.
\]

The proof avoids \(Y(0)\). It uses only:

- the initial quadratic energy \(H(0)\);
- the critical parameter \(\Gamma\);
- the local Sobolev transport factor \(A\);
- the integrated spacetime control of \(Y\).

The collapse-volume cancellation is correctly implemented:

\[
\gamma(0)
\lesssim r^2\sqrt{K_0},
\]

so the smallness is volume-independent.

### 7.2 What is conditional

The endpoint is conditional on the following analytic inputs:

1. The \(H\)-inequality with signed Hessian absorption:
   \[
   H'+cD\le C_0Y+C_1(1+r^{-2})H+C_V\|aE\|_\infty H.
   \]

2. The fixed-\(p\) curvature inequalities:
   \[
   K_p'+c\{pD_p^T+p(p-2)D_p^F\}
   \le
   Cp^N(1+r^{-2}+\mathcal S^2Y)K_p.
   \]

3. The defect hierarchy giving
   \[
   \|aE(t)\|_\infty
   \le
   C_E\delta\left(\frac{r^2}{t}\right)^{1/3}.
   \]

4. The local Sobolev transport estimate
   \[
   \mathcal S(t)\le e^{8V(t)}\mathcal S(0).
   \]

5. The existence of a smooth exact cutoff-flow interval long enough to carry the first-exit argument.

The supplied notes indicate that these inputs are not all at final proof level. In particular, Step 34 explicitly identifies the index-level tensor variation and derivative-structure estimates as unfinished.

### 7.3 What needs repair or completion

To convert the Step 58 endpoint into a rigorous component of the restricted Ishida--LeBrun route, the following repairs or completions are needed.

1. **Insert the metric-drift term.**  
   The \(H\)-inequality used in Step 58 should be rewritten with
   \[
   C_V\|aE\|_\infty H
   \]
   included, and all subsequent constants should carry the resulting \(e^{C_VV_*}\) factor.

2. **Replace the provisional Sobolev bound by the repaired transport.**  
   Every occurrence of \(\mathcal S(t)\le C\mathcal S(0)\) should be justified by
   \[
   \mathcal S(t)\le e^{8V(t)}\mathcal S(0)
   \]
   and the bootstrap bound \(V(t)\le V_*\).

3. **Complete the index-level tensor calculation.**  
   The signed Hessian-cutoff integration must be derived at the index level for the shifted tensor \(T\), including:
   \[
   |\nabla B|\le CF|\nabla T|,
   \]
   the exact algebraic lower-order terms, and the moving-measure contributions.

4. **Complete the defect hierarchy.**  
   The estimate
   \[
   \|aE(t)\|_\infty
   \le
   C_E\delta(r^2/t)^{1/3}
   \]
   must be proved under the same repaired Sobolev transport and without assuming an unweighted evolving bound \(|E(t)|\le\delta\).

5. **Close the coupled \((\Gamma,V)\) first-exit argument.**  
   The curvature Moser endpoint must be embedded inside the coupled bootstrap, not used as an independent source of the interval.

6. **Complete finite-order continuation data.**  
   Pointwise curvature control does not by itself control higher cutoff jets or the fixed-background restart data. The current-pair hierarchy and the fixed-background connection-difference bridge must be completed to the finite order required for restart.

7. **Connect to terminal geometry.**  
   The endpoint gives weighted curvature control at positive time. It does not by itself produce the terminal exponential-pullback compactness statement or the forbidden-germ argument needed for the restricted laboratory.

---

## Final judgment on the endpoint

The proposed endpoint

\[
\|aF_T(t)\|_\infty\le \frac{C\Gamma}{t}
\]

is algebraically and analytically coherent as a conditional estimate on a provisional first-exit interval. The good-slice argument, the Gronwall exponent, the Moser recurrence, the product convergence, and the final reduction to \(\Gamma\) are all correct under the stated assumptions.

The essential qualifications are:

1. Step 58’s tensor inequalities are not visibly proof-level in the supplied notes; Step 34 still lists the required index-level tensor calculations as unfinished.

2. Step 58 omits the \(C_V\|aE\|_\infty H\) term required by the repaired Step 55 bootstrap. Once that term is included, the endpoint survives with constants depending on \(V_*\).

3. The old assumption \(\mathcal S(t)\le2\mathcal S(0)\) should be replaced by the repaired transport
   \[
   \mathcal S(t)\le e^{8V(t)}\mathcal S(0),
   \]
   which is bounded on the bootstrap interval by \(e^{8V_*}\).

4. The smallness of \(\gamma\) is initially justified by the maximal-function selection and the critical cancellation, but its persistence in time requires the coupled \((\Gamma,V)\) first-exit argument.

Thus the curvature Moser endpoint is a valid conditional module, but it is not yet a self-contained proof-level theorem. Its validity under the repaired bootstrap is intact provided the metric-drift and Sobolev-transport constants are carried explicitly and the underlying tensor estimates are completed.