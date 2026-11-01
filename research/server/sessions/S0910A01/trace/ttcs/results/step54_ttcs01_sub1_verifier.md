# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/data/step54_first_exit_verify.json"
  ]
}
```

## Task

Verify the first-exit and continuation derivation in step54_first_exit_continuation_derivation.md. Focus on three critical mathematical points:

1. AUGMENTED ENERGY vs FLAT-TORUS TEST: The derivation claims that the flat-torus test (creating curvature from zero by nonconstant cutoff) does not invalidate augmented-energy estimates H_2 = int eta^2(1+|Rm|^2), because the normalization reaction +4a|R|^2 is absorbed by the CaF^3 reaction term already present. Check: is the reaction structure in the curvature power inequality (eq 4.4 of Step 35, eq 2.6 of this note) genuinely compatible with the normalization? Specifically, does the Hamilton quadratic + normalization + Hessian-a absorption close with the available dissipation, without introducing a bare additive constant?

2. DEFECT HOMOGENEITY: The derivation separates defect energies from curvature energies by the property B_def|_{E=0} = 0. Check whether every term in the J_6 evolution (eq 4.2) and the Q propagation (eq 7.2) genuinely has E-homogeneous coefficients. In particular, verify that the volume form variation d mu contributes an E-dependent term (not a curvature-only term) in the defect energy evolution.

3. CONTINUATION ARGUMENT: The staggered hierarchy (eq 6.2-6.3) claims that the highest cutoff jet C_{m+2} always carries a chi factor from the product rule nabla^{m+2}(chi^2) = 2 chi C_{m+2} + lower. Check: does this chi factor survive integration by parts and pairing with the weighted dissipation? Is there a term where the chi weight is consumed by a different factor, leaving a bare C_{m+2} contribution?

Provide a mathematical assessment of each point, identifying any gaps or errors.

## Output

# Scientific verification memo

## 1. Augmented curvature energy and the flat-torus calculation

### Structural compatibility

With the standard Kulkarni–Nomizu convention,
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,
\]
one has
\[
\operatorname{Ric}(G)=g,\qquad \operatorname{Ric}(T)=E,
\qquad \nabla G=0.
\]
Consequently,
\[
|E|\le C_n|T|,\qquad |\nabla E|\le C_n|\nabla T|
=C_n|\nabla\operatorname{Rm}|.
\]

Replacing \(\operatorname{Rm}\) by \(T\) in the Hessian-\(a\) contraction gives
\[
\Sigma_H^T
=8(\nabla_p\nabla_q a)B_T^{pq},
\qquad
B_T^{pq}=T^p{}_j{}^q{}_lE^{jl}.
\]
It satisfies
\[
|B_T|\le C F_T^2,\qquad
|\nabla B_T|
\le C F_T|\nabla\operatorname{Rm}|,
\quad F_T=(1+|T|^2)^{1/2}.
\]
Thus the signed integration-by-parts calculation of Step 35 extends to \(T\):
\[
|T_H^T|
\le \varepsilon p\!\left(D_p^{\rm Rm}+(p-2)D_p^{F_T}\right)
+C_\varepsilon p^3r^{-2}K_p.
\]
The additional terms from \(\partial_tG\), inverse-metric variation, and rewriting the Hamilton polynomial in \(\operatorname{Rm}=T-G\) are algebraic and obey
\[
|\text{algebraic terms in }\partial_tF_T^2|
\le CaF_T^3.
\]
The volume variation also has this form:
\[
\partial_t d\mu=-a\,\operatorname{tr}E\,d\mu,
\qquad
|\operatorname{tr}E|\le C F_T.
\]
Hence testing by \(a^{p-2}F_T^{p-2}\) produces
\[
C\int \eta^2a^{p-1}F_T^{p+1},
\]
not a standalone additive quantity. The \(p\ge3\) power inequality is therefore structurally compatible with the shifted curvature.

### The \(p=2\) step needs the small critical-energy absorption

Equation (2.7) in Step 54 does not follow merely by observing that \(H_2\) contains \(1\). Before absorption, the correct form is
\[
(H_2^\alpha)'+cD_2^\alpha
\le CY_T+C(1+r^{-2})H_2^\alpha,
\qquad
Y_T=\int\eta^2aF_T^3.
\]
The essential estimate is
\[
Y_T
=\int(\eta F_T)(\chi F_T)^2
\le (H_2^\alpha)^{1/2}\|\chi F_T\|_4^2
\le C\mathcal S(H_2^\alpha)^{1/2}
\left(D_2^\alpha+r^{-2}H_2^\alpha\right).
\]
Thus
\[
\gamma(t)=\mathcal S(t)(H_2^\alpha(t))^{1/2}
\]
must remain below a dimensional absorption threshold. Under that assumption,
\[
(H_2^\alpha)'\le C(1+r^{-2})H_2^\alpha.
\]
Step 54 implicitly uses this argument but presents (2.7) as an unconditional Grönwall estimate.

### What the flat-torus example actually tests

At \(t=0\) on a flat torus,
\[
\operatorname{Rm}=0,\qquad E=g.
\]
The term \(4a|\operatorname{Rm}|^2\) is then zero. Curvature is created instead by
\[
\partial_t\operatorname{Rm}\big|_{t=0}
=(\nabla^2a)\owedge g
\]
up to convention-dependent constants. Therefore
\[
|\operatorname{Rm}(t)|^2=O(t^2|\nabla^2a|^2).
\]
The relevant augmented-energy mechanism is the signed treatment of
\[
\operatorname{Rm}*(\nabla^2a)*E.
\]
After integration by parts, Young’s inequality produces a remainder of the form
\[
Cr^{-2}\int\eta^2(1+|\operatorname{Rm}|^2),
\]
where the constant \(1\) supplies the weighted support volume. The normalization reaction \(4a|\operatorname{Rm}|^2\) is harmless, but it is not the term responsible for curvature creation at the flat initial metric.

Thus the principal conclusion is valid: the flat-torus calculation does not contradict augmented \(H_2\) estimates. The explanation in Step 54 should distinguish the Hessian-\(a\) mechanism from the uniform-scaling reaction.

### Two concrete artifact inconsistencies

1. Since \(0\le\eta\le1\),
   \[
   \int\eta^2\,d\mu\le \operatorname{Vol}(\operatorname{supp}\eta),
   \]
   not the reverse. It is bounded below by the volume of the plateau where \(\eta=1\). Both Step 54 and the JSON entry identifying \(H_2\ge\operatorname{Vol}(\operatorname{supp}\eta)\) state the wrong relation.

2. Step 54 uses
   \[
   |G|^2=\frac{2n}{n-1},
   \]
   whereas `step54_first_exit_verify.json` uses
   \[
   |G|^2=\frac{n}{2(n-1)}.
   \]
   These differ by a factor of four. Under the convention for which
   \(\operatorname{Ric}(G)=g\), the first value is the compatible one. Norm equivalence remains true, but the numerical constants recorded in the JSON do not verify the tensor convention used in the note.

---

## 2. Homogeneity of the defect evolution

### Exact structural reason

The defect evolves by
\[
\partial_tE
=D\operatorname{Ric}_g[-2aE]-2aE.
\]
Since Ricci linearization is linear in its input, every term contains one of
\[
E,\quad \nabla E,\quad \nabla^2E.
\]
Curvature may occur as a coefficient, for example \(a\,\operatorname{Rm}*E\), but there is no term depending only on curvature and \(a\). In particular, \(E\equiv0\) is exactly stationary.

The inverse-metric part of \(\partial_t|E|^2\) is cubic in \(E\), while the Hessian contribution is
\[
2(\nabla_p\nabla_q a)B_{\rm def}^{pq},
\qquad
B_{\rm def}^{pq}
=|E|^2g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq}.
\]
Hence
\[
B_{\rm def}=O(|E|^2),
\qquad
\nabla B_{\rm def}=O(|E||\nabla E|).
\]
This verifies the required vanishing in both the \(J_6\) and \(Q\) energies.

### Volume variation

The exact formula is
\[
\partial_t d\mu
=\frac12\operatorname{tr}_g(-2aE)\,d\mu
=-a\,\operatorname{tr}E\,d\mu.
\]

For
\[
J_6=\int\eta^2a^4|E|^6\,d\mu,
\]
the volume contribution is
\[
-\int\eta^2a^5(\operatorname{tr}E)|E|^6\,d\mu.
\]
It is seventh order in \(E\) and satisfies
\[
\left|\int\eta^2a^5(\operatorname{tr}E)|E|^6\right|
\le C\int\eta^2a^5F_T|E|^6.
\]
This is precisely part of the potential \(P_6\); it is not a curvature-only source.

For
\[
Q_\alpha=\int\eta_\alpha^2|E|^2\,d\mu,
\]
the corresponding contribution is
\[
-\int\eta_\alpha^2a(\operatorname{tr}E)|E|^2\,d\mu,
\]
again vanishing whenever \(E=0\).

### \(J_6\) estimate

The derivation from Steps 34–35 gives
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6,
\qquad
P_6=\int F_T\,|\eta a^{5/2}E^3|^2.
\]
Then
\[
P_6
\le (H_2^\alpha)^{1/2}\,
\|\eta a^{5/2}|E|^3\|_4^2
\le C\gamma(t)\bigl(X_6+r^{-2}J_6\bigr).
\]
Therefore (4.2) follows under the same small-\(\gamma\) absorption used in the curvature seed. Step 54 suppresses this hypothesis, although Step 34 contains it explicitly.

### \(Q_\alpha\) propagation

The stated explanation for (7.2)—that its coefficient follows from a pointwise curvature bound—is insufficient near \(t=0\), because (3.4) only gives
\[
aF_T(t)\lesssim \frac{\gamma}{t}.
\]
A direct Grönwall argument with that coefficient would encounter \(\int_0^Tdt/t\).

The appropriate \(Q\) calculation instead uses critical \(L^2\)-Sobolev absorption. With
\[
D_E=\int\eta^2a|\nabla E|^2,
\qquad
P_2=\int\eta^2aF_T|E|^2,
\]
the tensor evolution yields
\[
Q_\alpha'+cD_E
\le CP_2+C(1+r^{-2})Q_\alpha.
\]
Moreover,
\[
P_2
\le \|F_T\|_{2,\operatorname{supp}a}\,
\|\eta\chi E\|_4^2
\le C\gamma(t)\bigl(D_E+r^{-2}Q_\alpha\bigr).
\]
The terms from \(d\chi\), \(\nabla^2a\), inverse metrics, and volume variation all fit this estimate. For small \(\gamma(t)\),
\[
Q_\alpha'\le C(1+r^{-2})Q_\alpha.
\]
Thus (7.2) is mathematically available, but its derivation in Step 54 cites the wrong controlling mechanism.

Equality (7.1) additionally requires a choice such as
\[
\rho=\sum_\alpha\eta_\alpha^2.
\]
Because \(\eta_\alpha=1\) on \(\operatorname{supp}a\), the support of \(1-\rho\) then lies where \(a=0\), and the remainder is genuinely stationary.

---

## 3. Highest cutoff jets and continuation

### The leading integration-by-parts mechanism

The product identity
\[
\nabla^{m+2}(\chi^2)
=2\chi\,C_{m+2}+\text{terms involving }C_j,\ j\le m+1
\]
is correct.

More importantly, in the \(U_m=\nabla^m(aT)\) equation, the highest Hessian-cutoff term has an additional weighted factor:
\[
a\,\nabla^m\bigl((\nabla^2a)*E\bigr)
=(\nabla^{m+2}a)*(aE)+\text{lower-order terms}.
\]
Since \(aE\) is a contraction of \(aT=U_0\), the dangerous integral has the form
\[
I_m=\int \chi\,C_{m+2}*(aE)*|U_m|^{p-2}U_m.
\]
Writing \(C_{m+2}=\nabla C_{m+1}\) schematically and integrating by parts,
\[
I_m
=-\int C_{m+1}*
\nabla\!\left(\chi(aE)|U_m|^{p-2}U_m\right).
\]
There are three types:

* derivative on \(\chi\): \(d\chi\,C_{m+1}\), so the cutoff derivative order has dropped;
* derivative on \(aE\): controlled by \(U_1\);
* derivative on \(U_m\): the factor \(\chi\) remains and
  \[
  \begin{aligned}
  &\int\chi |C_{m+1}|\,|aE|\,|U_m|^{p-2}|\nabla U_m|\\
  &\quad\le
  \varepsilon\int\chi^2|\nabla U_m|^2|U_m|^{p-2}
  +C_\varepsilon\int|C_{m+1}|^2|aE|^2|U_m|^{p-2}.
  \end{aligned}
  \]

Therefore, when the derivative consumes the \(\chi\) factor, it leaves \(C_{m+1}\), not a bare \(C_{m+2}\). When it differentiates \(U_m\), \(\chi\) remains available for the weighted dissipation. At this leading level, the proposed mechanism is correct.

The same weighted structure is compatible with the connection commutators because
\[
\partial_t\Gamma=\nabla(aE),
\]
and with curvature commutators because
\[
a\,\operatorname{Rm}=aT-aG=U_0-aG.
\]
No division by \(a\) is needed in these formulas.

### What is not yet contained in equation (6.3)

The single product identity does not by itself prove the complete coupled estimate (6.3). An indexed finite-order induction still has to account for:

* every \([\partial_t,\nabla^m]\) term;
* commutations in the degenerate diffusion operator;
* the evolution of \(C_{m+1}\), whose highest forcing is \(\nabla^m(aE)\);
* the \(L^\infty\) control of lower \(U_j,C_j\) needed in the \(L^p\) products;
* the choice of sufficiently high finite order and \(p>n\) for endpoint Sobolev regularity.

The displayed hierarchy is consistent with these structures, but Step 54 does not provide the complete induction.

### Invalid collar recovery

The sentence asserting that \(T_m\) can be recovered on \(0<a<1\) from \(U_m\) “using \(a\ge0\)” is incorrect. Already at order zero,
\[
U_0=aT
\]
does not control \(T\) as \(a\to0\). For higher derivatives,
\[
U_m=aT_m+\sum_{j=1}^m(\nabla^ja)*T_{m-j},
\]
and solving for \(T_m\) requires division by \(a\). There is no uniform lower bound for \(a\) in the transition collar.

A division-free continuation mechanism is available from the metric equation itself:
\[
\partial_tg=-2aE,
\qquad
\nabla^m(aE)=\operatorname{RicciContraction}(U_m).
\]
Time-integrable control of sufficiently many \(U_m\) controls the fixed-coordinate derivatives of \(g\) by integrating this equation. With high enough finite order and \(p>n\), this can supply the endpoint \(H^{s_0}\) regularity required for restarting the per-datum flow. That argument is materially different from recovering \(T_m\) by dividing \(U_m\) by \(a\), and it is absent from Step 54.

### Metric drift and Sobolev comparison

The line
\[
|\partial_tg|\le2\delta
\]
is only known initially. The propagated estimate is instead
\[
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3},
\]
whose time integral is finite. This still gives
\[
e^{-C\Lambda}g_0\le g(t)\le e^{C\Lambda}g_0,
\qquad
\Lambda=\int_0^t\|aE(s)\|_\infty ds.
\]
Localized Sobolev inequalities compare directly under this bilipschitz estimate. Pointwise metric drift alone does not preserve a Ricci lower bound, since Ricci depends on second derivatives. Thus the Sobolev bootstrap can be closed through bilipschitz comparison, but not by the Ricci-comparison explanation written in §5.2.

---

## Assessment

1. **Augmented energy:** The tensor structure supports the desired power inequalities without a standalone additive source. The \(T\)-shift requires the explicit \(B_T=T*E\) calculation above, and the \(H_2\) Grönwall estimate requires small critical energy. The flat-torus curvature creation comes from \(\nabla^2a\), not from \(4a|\operatorname{Rm}|^2\).

2. **Defect energies:** All terms vanish with \(E\), including the volume-form contributions. The \(J_6\) estimate is supported by Steps 34–35. The \(Q\) estimate is also obtainable, but through \(L^2\)-Sobolev absorption rather than the singular pointwise curvature estimate.

3. **Continuation:** No bare \(C_{m+2}\) remains after the leading integration by parts; consuming \(\chi\) lowers the cutoff derivative order. The full finite-order induction is not written. More seriously, recovering unweighted curvature in the transition collar by dividing by \(a\) is invalid; endpoint regularity must instead come from direct control of the weighted velocity \(aE\) and its derivatives.

A separate visible issue in §8.1 is that bounded curvature and a geodesic buffer alone do not imply a uniform lower volume for \(B_{\rho/2}(p)\). Flat tori with a very short circle have zero curvature and arbitrarily small fixed-radius balls. Rauch comparison controls conjugate behavior, not quotient identifications; the terminal compactness argument therefore needs an independent injectivity or local-volume input from the selection construction.