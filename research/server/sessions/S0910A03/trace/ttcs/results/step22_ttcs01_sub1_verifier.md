# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step22_inverse_square_correction_and_two_stage_architecture.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step21_corrections_from_ttcs_and_peers.md",
    "Sessions/S0910A03/workspace/scripts/verify_step22_inverse_square_and_subcritical.py"
  ]
}
```

## Task

Verify the following claims about the normalized cutoff flow in 4 dimensions:

1. INVERSE-SQUARE COUNTEREXAMPLE: The Hardy potential V = κ/|x|² on R⁴ with 0 < κ < 1 satisfies the form bound ∫Vφ² ≤ κ∫|∇φ|² (small form perturbation), but the heat semigroup e^{t(Δ+V)} does NOT have a uniform L²→L∞ bound. Verify that σ = 1-√(1-κ) > 0 gives the singular ground state r^{-σ} ∈ L² \ L∞.

2. SUBCRITICAL UPGRADE: In 4D, n/2 = 2 is the critical Sobolev exponent. A potential in L² gives only a form bound (critical, possibly non-ultracontractive). A potential in L³ gives form-relative bound zero (subcritical), allowing standard Moser iteration with convergent constants. Verify that the Wang hierarchy H₃(t) ≤ Cγ³/t provides exactly this subcritical upgrade at positive time.

3. SOBOLEV VARIABLE: For v = ηχF with a=χ², check that |∇v|² = η²a|∇F|² + |∇χ|²F² + a F²|∇η|² + cross terms, and that |∇a|²/a = 4|∇χ|² is bounded. Verify that this means the gradient of the Sobolev variable is controlled by the dissipation D₂ = ∫η²a|∇F|² plus lower-order terms.

4. CAUCHY-SCHWARZ FACTORING: H₃ = ∫η²aF³ ≤ H₂^{1/2} · (∫η²a²F⁴)^{1/2}. The second factor requires an OUTER cutoff. Verify that the finite-neighbor graph system handles this, and that the critical Sobolev product β = A₀²||F||₂ = C√ε_Li controls the absorption.

5. TRANSCRIPTION: The correct quadratic form is ε_t[φ] = ∫|∇(a^{-1/2}φ)|²dμ, NOT ∫|∇(a⁻¹φ)|²dμ. The former has leading weight a⁻¹ near the gradient, the latter a⁻². Verify that the a⁻¹/² version matches the conformal Sobolev substitution u = a^{-1/2}φ.

## Output

# Scientific verification memo

## 1. Inverse-square counterexample

Let
\[
H=-\Delta-\frac{\kappa}{r^2},\qquad 0<\kappa<1,
\]
on \(\mathbb R^4\), with the Friedrichs realization. The four-dimensional Hardy inequality is
\[
\int_{\mathbb R^4}\frac{|\phi|^2}{r^2}\,dx
\le \int_{\mathbb R^4}|\nabla\phi|^2\,dx,
\]
so
\[
\langle H\phi,\phi\rangle
\ge (1-\kappa)\int|\nabla\phi|^2.
\]
Thus \(V=\kappa r^{-2}\) has relative form coefficient \(\kappa<1\).

For \(h=r^{-\alpha}\),
\[
(\Delta+\kappa r^{-2})h
=\bigl[\kappa-\alpha(2-\alpha)\bigr]r^{-\alpha-2}.
\]
Hence the radial exponents satisfy
\[
\alpha^2-2\alpha+\kappa=0,
\qquad
\alpha_\pm=1\pm\sqrt{1-\kappa}.
\]
The Friedrichs branch is
\[
\sigma=\alpha_-=1-\sqrt{1-\kappa}\in(0,1).
\]
Near \(r=0\),
\[
\int_{B_1}r^{-2\sigma}\,dx
=|\mathbb S^3|\int_0^1r^{3-2\sigma}\,dr<\infty,
\]
whereas \(r^{-\sigma}\) is unbounded on every neighborhood of the origin. Moreover,
\[
\int_{B_1}|\nabla r^{-\sigma}|^2dx
\asymp\int_0^1r^{1-2\sigma}dr<\infty,
\]
which selects this branch in the Friedrichs form domain.

A direct ground-state transform makes the semigroup conclusion precise. For radial \(w\),
\[
(\Delta+\kappa r^{-2})(r^{-\sigma}w)
=r^{-\sigma}\left(w_{rr}+\frac{3-2\sigma}{r}w_r\right).
\]
The transformed operator is the radial heat operator in effective dimension \(4-2\sigma\). If \(f\ge0\) is a nonzero smooth radial function supported in an annulus, then the transformed heat solution has a strictly positive finite value at \(r=0\). Consequently,
\[
e^{t(\Delta+V)}f(r)\sim c_t r^{-\sigma},
\qquad c_t>0,
\]
as \(r\downarrow0\). Therefore \(e^{t(\Delta+V)}f\notin L^\infty\), although it remains in \(L^2\). There is no bounded \(L^2\to L^\infty\) operator at any \(t>0\).

Three precision corrections are needed in the Step 22 note:

1. The bare function \(r^{-\sigma}\) is in \(L^2_{\mathrm{loc}}\), not in global \(L^2(\mathbb R^4)\), since it does not decay sufficiently at infinity. The semigroup output constructed above is a genuine global \(L^2\setminus L^\infty\) function.
2. The assertion about “any” \(L^2\) datum is too broad because signed data can cancel the leading radial coefficient. A nonzero nonnegative radial datum already proves the operator statement.
3. Scaling gives the kernel form
   \[
   p_t(x,y)\sim t^{-2}
   \left(\frac{|x|}{\sqrt t}\right)^{-\sigma}
   \left(\frac{|y|}{\sqrt t}\right)^{-\sigma}\Phi,
   \]
   equivalently \(t^{-2+\sigma}|x|^{-\sigma}|y|^{-\sigma}\Phi\) when both variables approach zero. The displayed \(t^{-2}|x|^{-\sigma}|y|^{-\sigma}\Phi\) in Step 22 is not scaling-compatible unless the omitted \(t\)-powers are absorbed into \(\Phi\).

Also,
\[
\int_{B_1}V^2dx\asymp\int_0^1\frac{dr}{r}=\infty.
\]
Thus the Hardy potential lies in weak \(L^2\), not strong \(L^2\). It decisively refutes an abstract theorem based only on the relative form coefficient. Smooth truncations \(V_\varepsilon\le\kappa r^{-2}\) retain that coefficient while their ultracontractive constants diverge as \(\varepsilon\downarrow0\).

## 2. Critical versus subcritical potential estimates

In dimension four, \(n/2=2\) is the critical integrability exponent for a zeroth-order potential; the corresponding function Sobolev exponent is \(4\).

With
\[
X[\phi]=\int|\nabla\phi|^2+r^{-2}\int\phi^2,
\qquad
\|\phi\|_4^2\le A_0^2X[\phi],
\]
a strong \(L^2\) potential gives
\[
\int |V|\phi^2
\le \|V\|_2\|\phi\|_4^2
\le A_0^2\|V\|_2X[\phi].
\]
This is a fixed relative coefficient. In a power test for \(u^q\), the potential coefficient acquires powers of \(q\), so one fixed small coefficient is suited to finitely many prescribed exponents, not automatically to the entire \(q\to\infty\) sequence.

For \(V\in L^3\), Hölder and interpolation instead give
\[
\int |V|\phi^2
\le \|V\|_3\|\phi\|_3^2
\le \|V\|_3\|\phi\|_2^{2/3}\|\phi\|_4^{4/3}.
\]
Therefore, for every \(\varepsilon>0\),
\[
\int |V|\phi^2
\le
\varepsilon X[\phi]
+C\varepsilon^{-2}A_0^4\|V\|_3^3\|\phi\|_2^2.
\tag{2.1}
\]
This is the quantitative form-relative-zero estimate needed in Moser iteration. Choosing \(\varepsilon\) as a reciprocal polynomial in \(q\) produces only polynomial \(q\)-dependence, whose product converges along a geometric exponent sequence.

For completeness, a fixed strong-\(L^2\) potential is also infinitesimally form bounded after truncating its high-value part. At the critical exponent, however, the resulting lower-order constant depends on the detailed \(L^2\) tail and is not controlled by the single number \(\|V\|_2\) in the explicit manner of (2.1).

### Application to \(H_3\)

Set
\[
\mathcal K=aF,\qquad d\nu=a^{-2}d\mu.
\]
Then
\[
\|\mathcal K\|_{L^3(\nu)}^3
=\int aF^3\,d\mu=H_3.
\]
Thus any estimate of the form
\[
A_0^4H_3(s)\le \frac{C\gamma^3}{s}
\tag{2.2}
\]
gives, uniformly for \(s\in[t/2,t]\),
\[
A_0^4\|\mathcal K(s)\|_{L^3(\nu_s)}^3
\le \frac{C\gamma^3}{t}.
\]
Substitution into (2.1) yields
\[
\int\mathcal K\phi^2\,d\nu_s
\le \varepsilon\mathfrak e_s[\phi]
+C\varepsilon^{-2}\frac{\gamma^3}{t}
\|\phi\|_{L^2(\nu_s)}^2.
\]
This is exactly the subcritical potential estimate used in the positive-time iteration.

There is a normalization inconsistency in Step 22: Step 20 equation (2.3) establishes formally
\[
\boxed{A_0^4H_3(t)\le C\gamma^3/t},
\]
not \(H_3(t)\le C\gamma^3/t\) unless \(A_0=1\) or \(A_0^4H_3\) has been renamed \(H_3\). The combination naturally entering the Moser estimate is \(A_0^4H_3\), so the analytic mechanism remains correct after restoring this factor.

The supplied files establish the implication from (2.2) to subcritical Moser estimates. They do not contain a complete derivation of (2.2) for the normalized cutoff flow: Step 20 equation (11.1) is assumed, while Step 22 lists the tensor evolution, finite-neighbor bookkeeping, evolving measure, and zero-set regularization as unresolved.

The final exponent discussion in `verify_step22_inverse_square_and_subcritical.py` also contains two errors. For
\[
\frac1{r_k}=\frac12-\frac1{q_k},
\]
one has \(r_k\to2\) from above, not below; with \(q_0=2\), the first values are \(r_0=\infty\), \(r_1=4\), \(r_2=8/3\), so they are not all below \(3\). On the possibly infinite measure space \((\Omega,\nu)\), \(L^3\) also need not embed in lower \(L^r\) spaces. The fixed-\(L^3\) interpolation argument (2.1), rather than that \(r_k\)-sequence, is the correct justification.

## 3. Sobolev variable and weighted dissipation

For nonnegative \(\chi\), \(a=\chi^2\), and
\[
v=\eta\chi F,
\]
one has exactly
\[
\nabla v
=\eta\chi\nabla F+\eta F\nabla\chi+\chi F\nabla\eta.
\]
Hence
\[
\begin{aligned}
|\nabla v|^2={}&
\eta^2a|\nabla F|^2
+\eta^2F^2|\nabla\chi|^2
+aF^2|\nabla\eta|^2\\
&+2\eta^2\chi F\langle\nabla F,\nabla\chi\rangle
+2\eta aF\langle\nabla F,\nabla\eta\rangle
+2\eta\chi F^2\langle\nabla\chi,\nabla\eta\rangle.
\end{aligned}
\]
The task’s second square term omits \(\eta^2\); it is valid only as an upper estimate when \(0\le\eta\le1\).

Applying Young’s inequality to the cross terms gives
\[
|\nabla v|^2
\le C\left(
\eta^2a|\nabla F|^2
+\eta^2F^2|\nabla\chi|^2
+aF^2|\nabla\eta|^2
\right).
\]
Consequently,
\[
\int|\nabla v|^2
\le C D_2
+C r^{-2}\int_{\operatorname{supp}\eta_{\rm out}}F^2,
\]
provided \(|\nabla\chi|+|\nabla\eta|\le Cr^{-1}\). This verifies the control by
\[
D_2=\int\eta^2a|\nabla F|^2
\]
plus outer lower-order energy.

On \(\{a>0\}\),
\[
\frac{|\nabla a|^2}{a}
=\frac{|2\chi\nabla\chi|^2}{\chi^2}
=4|\nabla\chi|^2.
\]
For a smooth nonnegative cutoff, this has the bounded zero-set extension used in the weak energy calculation.

## 4. Cauchy–Schwarz factoring and outer cutoffs

The factoring is exact:
\[
\begin{aligned}
H_{3,\eta}
&=\int\eta^2aF^3\\
&\le
\left(\int\eta^2F^2\right)^{1/2}
\left(\int\eta^2a^2F^4\right)^{1/2}.
\end{aligned}
\tag{4.1}
\]
An outer cutoff \(\widetilde\eta\equiv1\) on \(\operatorname{supp}\eta\) is needed because Sobolev controls
\[
\int\widetilde\eta^4a^2F^4
=\|\widetilde\eta\chi F\|_4^4,
\]
whereas using \(\eta\) itself only produces \(\eta^4\), which does not dominate \(\eta^2\) where \(\eta\) is small. With the outer cutoff,
\[
\left(\int\eta^2a^2F^4\right)^{1/2}
\le
\|\widetilde\eta\chi F\|_4^2
\le
CA_0^2\left(D_{2,\widetilde\eta}
+r^{-2}H_{2,\widetilde\eta}\right).
\]
Thus
\[
H_{3,\eta}
\le
C\beta_{\rm out}
\left(D_{2,\widetilde\eta}
+r^{-2}H_{2,\widetilde\eta}\right),
\qquad
\beta_{\rm out}=A_0^2\|F\|_{L^2(U_{\rm out})}.
\tag{4.2}
\]

For a graph of outer neighborhoods with degree at most \(N\), an energy system schematically of the form
\[
E_\alpha'+cD_\alpha
\le C\beta_*\sum_{\rho\sim\alpha}D_\rho+\text{lower-order terms}
\]
sums to
\[
\sum_\alpha E_\alpha'
+\bigl(c-CN\beta_*\bigr)\sum_\alpha D_\alpha
\le\text{lower-order terms}.
\]
Thus bounded degree and \(CN\beta_*<c/2\) algebraically absorb the outer dissipations. If Sobolev constants vary, the same calculation uses weighted energies with adjacent weights uniformly comparable.

The local Li-radius estimate is
\[
A_0^2\|F\|_2
\lesssim
r^2\operatorname{Vol}(U)^{-1/2}
\bigl(K_F\operatorname{Vol}(U)\bigr)^{1/2}
=r^2\sqrt{K_F}.
\]
Hence \(r^4K_F\lesssim\varepsilon_{\rm Li}\) gives
\[
\beta_{\rm out}\lesssim\sqrt{\varepsilon_{\rm Li}}.
\]
For \(F=(1+|\operatorname{Rm}|^2)^{1/2}\), this either requires defining the Li scale using \(K_F\), or retaining the extra \(Cr^2\) term recorded in Step 20. At the initial near-\(\operatorname{Ric}=-g\) slice, \(F\lesssim|\operatorname{Rm}|\), so the two parameters are comparable.

The graph absorption mechanism is therefore mathematically sound under a bounded-degree outer family and per-neighborhood Li energy. The supplied notes do not yet present the full cutoff family, weighted graph sum, and exact normalized-flow tensor inequality together; Step 22 explicitly records these pieces as unresolved.

## 5. Conformal Sobolev substitution

Because \(d\nu=a^{-2}d\mu\),
\[
\|\phi\|_{L^4(\nu)}^2
=\left(\int a^{-2}\phi^4\,d\mu\right)^{1/2}
=\|a^{-1/2}\phi\|_{L^4(\mu)}^2.
\]
Therefore the Sobolev substitution is exactly
\[
u=a^{-1/2}\phi,
\]
and its gradient form is
\[
\int\left|\nabla(a^{-1/2}\phi)\right|^2d\mu.
\]
For \(\phi=\eta\mathcal K=\eta aF\), this gives
\[
a^{-1/2}\phi=\eta a^{1/2}F=\eta\chi F=v,
\]
directly matching the Sobolev variable in Section 3.

The exact expansions are
\[
\begin{aligned}
\left|\nabla(a^{-1/2}\phi)\right|^2
={}&a^{-1}|\nabla\phi|^2
-a^{-2}\phi\langle\nabla a,\nabla\phi\rangle
+\frac14a^{-3}|\nabla a|^2\phi^2,\\
\left|\nabla(a^{-1}\phi)\right|^2
={}&a^{-2}|\nabla\phi|^2
-2a^{-3}\phi\langle\nabla a,\nabla\phi\rangle
+a^{-4}|\nabla a|^2\phi^2.
\end{aligned}
\]
Thus the leading gradient weights are respectively \(a^{-1}\) and \(a^{-2}\). The \(O(\cdot)\) expansion in Step 22 understates the first zero-order power: it should contain \(a^{-3}|\nabla a|^2\phi^2\), not \(a^{-2}|\nabla a|^2\phi^2\). After inserting \(\phi=\eta aF\), this term reduces to a regular cutoff contribution controlled by \(|\nabla a|^2/a=4|\nabla\chi|^2\).

Finally, the exact lower-order Sobolev term after substitution is
\[
r^{-2}\int a^{-1}\phi^2d\mu
=r^{-2}\int a\phi^2d\nu.
\]
Since \(0\le a\le1\), it is bounded above by
\[
r^{-2}\|\phi\|_{L^2(\nu)}^2.
\]
Thus the larger \(L^2(\nu)\) mass term used in Step 22 is valid, but it is an enlargement rather than an exact identity.

Overall, items 1, 3, and 5 are mathematically established after the stated corrections. Item 2 correctly identifies the \(H_3\) mechanism once \(A_0^4H_3\le C\gamma^3/t\) is used. Item 4 verifies the local factoring and bounded-degree graph algebra, while the complete normalized-flow derivation of the \(H_2\to H_3\) estimate is not contained in the supplied material.