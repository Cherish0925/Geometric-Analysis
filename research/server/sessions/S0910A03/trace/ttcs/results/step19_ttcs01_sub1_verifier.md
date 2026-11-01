# TTCS Independent Branch Record

```json
{
  "step_id": 19,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/scripts/verify_step19_volume_independent_beta.py",
    "Sessions/S0910A03/workspace/scripts/verify_step19_p4_threshold_and_bernstein.py",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md"
  ]
}
```

## Task

Verify the proposed first-exit closure for the 4D normalized cutoff flow. The claim is that Wang's Theorem 6.3 can be localized to a finite-neighbor system of balls on a closed 4-manifold under the normalized cutoff flow ∂_tg = -2χ²(Ric+g), yielding the volume-independent curvature decay |χ²Rm| ≤ C√ε/t.

Specific points to check:

1. VOLUME-INDEPENDENT BETA: On a ball B_r with Ric ≥ -3g, the relative Sobolev constant is A ~ C·r·V^{-1/4}. The maximal-function selection gives ∫_{B_r}|Rm|² ≤ K₀·V. Therefore β = A²·||Rm||_{L²} = C²r²V^{-1/2}·√(K₀V) = C²r²√K₀. With the Li radius r_* = (ε/K₀)^{1/4}, this gives β = C²√ε. Does this volume cancellation hold exactly in 4D? Does it fail in other dimensions?

2. LOCALIZATION OF WANG/YANG: Wang's proof (Theorem 6.3, see context_files) uses a global Sobolev inequality and global L^{n/2} curvature energy. The localized version replaces these with relative Sobolev on each ball and local energies R_α per ball. The Moser iteration (Li Theorem 2.5) runs on each individual ball B_r(x) with nested sub-balls. The energy persistence comes from the coupled L² system dH_α/dt ≤ Cr^{-2}Σ_{β~α}H_β. Does this localization introduce any new terms or require additional hypotheses beyond the coupled energy control?

3. NORMALIZED FLOW CORRECTION: Under ∂_tg = -2χ²(Ric+g) = -2χ²Ric - 2χ²g, the curvature evolution gains additional terms from h₂ = -2χ²g. These are ∂_tRm|_{h₂} ~ Hess(χ²)·g + χ²·Rm (from the metric variation formula). In the L^{n/2} energy equation, these contribute O(r^{-2})∫|Rm|^{n/2} (lower order) and ∫χ²|Rm|^{n/2} (absorbed). Is this correct? Are there any higher-order terms from the normalization that could affect the Moser absorption?

4. FIRST-EXIT CLOSURE LOGIC: Given β small → |χ²Rm|≤Cβ/t → curvature potential for Li → |χ²E|≤C_pδ(r²/t)^{2/p} → weighted Bernstein |χ∇(χ²E)|≤C_pδt^{-1/2}(r²/t)^{2/p} → for p>4: metric drift O(δθ^{1-2/p}r²), connection drift O(δθ^{1/2-2/p}), Hessian drift O(δθ^{1/2-2/p}/r) → all provisional first-exit bounds improved for small δ. Is there any circular dependency? Does the Bernstein estimate actually follow from the weighted parabolic structure?

## Output

# Scientific verification memo

## Overall assessment

The four-dimensional volume cancellation is correct, up to the fixed Sobolev and neighboring-volume constants. It is not intrinsically unique to dimension four; dimension four is special because the available \(L^{2}\) curvature energy is exactly the critical \(L^{n/2}\) energy.

A finite-neighbor Wang/Yang curvature argument is mathematically plausible, but it is not obtained merely by restricting Wang’s Theorem 6.3 to individual balls. The local Sobolev zeroth-order term, spatial localization functions, evolving measure, neighboring energies, and the added normalized-flow terms must all appear in a fresh local energy/Moser derivation.

The normalization introduces no derivatives above \(\nabla^{2}(\chi^{2})\) in the curvature equation. However, the stated treatment of the \(\nabla^{2}(\chi^{2})\owedge g\) term as simply
\[
O(r^{-2})\int |\mathrm{Rm}|^{n/2}
\]
is not literally correct without replacing \(|\mathrm{Rm}|\) by \(F=(1+|\mathrm{Rm}|^{2})^{1/2}\), or combining the Ricci and metric pieces through \(E=\mathrm{Ric}+g\).

The decisive unresolved analytic object is the weighted gradient estimate
\[
\chi |\nabla(\chi^{2}E)|
 \lesssim \delta\,t^{-1/2}(r^{2}/t)^{2/p}.
\]
Neither Wang’s Theorem 6.3 nor Li’s Theorem 2.5 supplies this estimate. Moreover, this weighted derivative controls the evolution of \(\nabla^{2}(\chi^{2})\), but it does not directly control the full connection difference.

---

## 1. Volume-independent \(\beta\)

Write the local Sobolev inequality in norm form as
\[
\|v\|_{4}
 \le A_{\alpha}\bigl(\|\nabla v\|_{2}+r^{-1}\|v\|_{2}\bigr),
 \qquad
 A_{\alpha}\le C_{S}rV_{\alpha}^{-1/4}.
\]
For an enlarged ball \(\widetilde U_{\alpha}\), suppose
\[
\int_{\widetilde U_{\alpha}}|\mathrm{Rm}|^{2}
 \le K_{0}\operatorname{Vol}(\widetilde U_{\alpha}).
\]
Initial Bishop–Gromov comparison and finite-neighbor geometry give
\[
\operatorname{Vol}(\widetilde U_{\alpha})
 \le C_{V}V_{\alpha}.
\]
Therefore
\[
\begin{aligned}
\beta_{\alpha}
&:=A_{\alpha}^{2}
 \|\mathrm{Rm}\|_{L^{2}(\widetilde U_{\alpha})}\\
&\le C_{S}^{2}r^{2}V_{\alpha}^{-1/2}
  \sqrt{K_{0}C_{V}V_{\alpha}}\\
&\le C_{S}^{2}C_{V}^{1/2}r^{2}\sqrt{K_{0}}.
\end{aligned}
\]
Thus the exponent of \(V_{\alpha}\) cancels exactly. With
\[
r_{*}^{4}K_{0}=\varepsilon,
\]
this becomes
\[
\beta_{\alpha}\le C_{S}^{2}C_{V}^{1/2}\sqrt{\varepsilon}.
\]
Consequently Wang’s threshold \(\beta\le 1/(2n^{2})\) can be met by choosing
\[
\varepsilon
 \le c\,C_{S}^{-4}C_{V}^{-1}
\]
with a dimensional \(c\).

Two qualifications matter:

1. The relation is an inequality with fixed constants, not a literal equality.
2. The energy and Sobolev volumes must refer to comparable balls. For a finite-neighbor cover, the relevant parameter is more precisely
   \[
   A_{\alpha}^{2}\|\mathrm{Rm}\|_{L^{2}(\widetilde U_{\alpha})}
   \lesssim
   \left(\sum_{\beta\sim\alpha}R_{\beta}\right)^{1/2}.
   \]
   Smallness of every \(R_{\beta}\) therefore has to include the finite neighboring degree.

### Other dimensions

For critical curvature data in dimension \(n\),
\[
A^{2}\sim r^{2}V^{-2/n}.
\]
If
\[
\fint_{B_r}|\mathrm{Rm}|^{n/2}\le K_{n/2},
\]
then
\[
\|\mathrm{Rm}\|_{L^{n/2}}
 \le K_{n/2}^{2/n}V^{2/n},
\]
and hence
\[
A^{2}\|\mathrm{Rm}\|_{L^{n/2}}
 \lesssim r^{2}K_{n/2}^{2/n}.
\]
The volume cancellation is therefore generic when the curvature exponent is \(n/2\).

What is special in four dimensions is
\[
n/2=2.
\]
For \(n>4\), an averaged \(L^{2}\) estimate alone gives no \(L^{n/2}\) estimate. For \(n=3\), Hölder converts averaged \(L^{2}\) control into the critical \(L^{3/2}\) control, with the same volume cancellation. Dimension two uses a different Sobolev formulation.

---

## 2. What localization of Wang/Yang actually entails

Wang’s Theorem 6.3 assumes the global homogeneous inequality
\[
\|f\|_{2n/(n-2)}\le A_{0}\|\nabla f\|_{2}
\]
and a global critical curvature norm. On a closed manifold this homogeneous inequality cannot hold for arbitrary functions because constants have zero gradient. A ballwise argument instead uses functions supported inside a larger ball and the relative inequality with the \(r^{-1}\|f\|_{2}\) term.

Restricting Wang’s theorem to a ball is therefore not a direct theorem invocation. A local derivation introduces the following concrete terms.

### Spatial localization

With an additional cutoff \(\eta\), integration by parts produces
\[
a|d\eta|^{2}F^{q},
\qquad
\frac{|da|^{2}}a\,\eta^{2}F^{q},
\qquad
|da||d\eta|F^{q},
\]
where \(a=\chi^{2}\) and \(F\) is the curvature quantity used in the iteration. Since
\[
\frac{|da|^{2}}a=4|d\chi|^{2},
\]
these are regular and bounded by \(Cr^{-2}\) times neighboring energies. No second derivative of \(\eta\) is needed after the standard integrations by parts.

### Relative Sobolev term

The \(r^{-1}\|f\|_{2}\) contribution creates additional
\[
Cr^{-2}\int \eta^{2}F^{q}
\]
terms at every Moser exponent. They are lower order on \(t\le\theta r^{2}\), but they must be retained.

### Neighboring balls

The support of \(\eta\) lies in an enlarged ball, so the reaction absorption uses
\[
A_{\alpha}^{2}
\|\mathrm{Rm}\|_{L^{2}(\widetilde U_{\alpha})}
\lesssim
\left(\sum_{\beta\sim\alpha}R_{\beta}\right)^{1/2}.
\]
The differential inequality
\[
\dot H_{\alpha}
 \le Cr^{-2}\sum_{\beta\sim\alpha}H_{\beta}
\]
supplies the base critical energy persistence, but the Moser argument also uses:

- provisional metric equivalence;
- uniform local Sobolev inequalities;
- comparable volumes for neighboring fixed domains;
- bounded cover degree;
- bounds for \(d\chi\) and \(d\eta\);
- control of the evolving measure;
- compact containment of all nested supports in the buffered good region.

Thus coupled \(L^{2}\) control is central, but it is not the sole input.

### Evolving measure

For the normalized cutoff flow,
\[
\partial_t d\mu=-\sigma\,d\mu,
\qquad
\sigma=\operatorname{tr}(aE).
\]
At the curvature-Moser stage this contributes
\[
\int |\sigma|\,\eta^{2}F^{q}.
\]
The fixed-supercritical \(L^{p}\) estimate for \(U=aE\), with \(p>2\), can treat this as a supercritical zeroth-order potential by interpolation and Young’s inequality. This term is absent from a literal use of Wang’s unnormalized curvature estimate and must appear in the localized normalized derivation.

Accordingly, Wang’s global theorem is strong structural evidence for the desired curvature estimate, but the finite-neighbor version is a separate lemma whose proof is not contained in the supplied notes.

---

## 3. Normalized-flow curvature correction

For a metric variation \(h\),
\[
D\mathrm{Rm}_{g}(h)
 =\tfrac12(\nabla^{2}h\text{ in curvature symmetries})
   +\mathrm{Rm}*h.
\]
For
\[
h_{2}=-2ag,
\]
using \(\nabla g=0\) gives
\[
D\mathrm{Rm}_{g}(h_{2})
 =-(\nabla^{2}a)\owedge g+a\,\mathcal R(\mathrm{Rm}),
\]
up to convention-dependent algebraic constants. Therefore:

- no derivative above \(\nabla^{2}a\) occurs in the curvature equation;
- the \(a\,\mathrm{Rm}\) contribution is multiplicative and gives a Gronwall-type lower-order term;
- the Hessian contribution is not itself proportional to \(\mathrm{Rm}\).

At exponent \(q=n/2\), the latter appears as
\[
\int \eta^{2}|\mathrm{Rm}|^{q-2}
 \left\langle \mathrm{Rm},(\nabla^{2}a)\owedge g\right\rangle,
\]
whose pointwise size is
\[
\int \eta^{2}|\nabla^{2}a|\,|\mathrm{Rm}|^{q-1},
\]
not \(r^{-2}\int|\mathrm{Rm}|^{q}\) directly. Integrating once by parts produces terms such as
\[
|da|\,|\mathrm{Rm}|^{q-2}|\nabla\mathrm{Rm}|,
\]
and Young’s inequality leaves
\[
\frac{|da|^{2}}a|\mathrm{Rm}|^{q-2}.
\]

Two mathematically coherent treatments are available.

### Treatment through \(F=(1+|\mathrm{Rm}|^{2})^{1/2}\)

Since \(F\ge1\), all lower curvature powers become bounded by \(F^{q}\). The local initial parameter then becomes
\[
A^{2}\|F\|_{2}
 \le A^{2}\|\mathrm{Rm}\|_{2}+A^{2}\sqrt V
 \lesssim \beta+r^{2}.
\]
In the near-\((-1)\)-Einstein setting, \(|E|\ll1\) implies a pointwise lower bound on \(|\mathrm{Ric}|\), hence on \(|\mathrm{Rm}|\), and therefore \(K_{0}\ge c>0\). Thus
\[
r^{2}\lesssim r^{2}\sqrt{K_{0}}\simeq\beta.
\]
This makes \(\beta+r^{2}\lesssim\beta\), so a corrected Wang-style estimate can still have the desired order
\[
|a\mathrm{Rm}|
 \lesssim \frac{\beta}{t}
 \left(1+\frac{t}{r^{2}}\right)^{C}.
\]

### Treatment through the full velocity \(aE\)

Combining the \(-2a\mathrm{Ric}\) and \(-2ag\) variations before estimating rewrites the cutoff-Hessian contribution in terms of
\[
\nabla^{2}a*E,\qquad da*\nabla E,
\]
rather than treating the \(g\)-term alone. This preserves the fact that the entire flow is stationary when \(E=0\), but it couples the curvature estimate to defect energies.

The supplied statement that normalization merely contributes
\[
O(r^{-2})\int|\mathrm{Rm}|^{n/2}
\]
therefore skips a real algebraic step. No higher-order normalization term exists, but the lower curvature powers must be handled explicitly.

---

## 4. Curvature potential and defect pointwise estimate

If the localized curvature estimate is established as
\[
\|a\mathrm{Rm}(t)\|_{\infty}\le C\beta/t
\]
and
\[
\|\mathrm{Rm}\|_{2}\le \beta/A^{2},
\]
then the weighted \(L^{3}\) potential obeys
\[
\begin{aligned}
K_{3}(t)
&=\int a|\mathrm{Rm}|^{3}\\
&\le \|a\mathrm{Rm}\|_{\infty}
     \int|\mathrm{Rm}|^{2}\\
&\le \frac{C\beta}{t}\frac{\beta^{2}}{A^{4}}
 =\frac{C\beta^{3}}{A^{4}t}.
\end{aligned}
\]
Thus Step 18’s desired estimate
\[
K_{3}(t)\le \frac{C}{A^{4}t}
\]
does follow, with room to spare when \(\beta\) is small.

A finite-neighbor Li iteration from the fixed \(L^{p}\) estimate for \(U=aE\) is then consistent with the exponent
\[
\|U(t)\|_{\infty}
 \lesssim C_{p}\delta(r^{2}/t)^{2/p}.
\]
Li’s Theorem 2.5 itself is a value estimate for a scalar heat inequality; it does not state the corresponding tensorial, degenerate, finite-neighbor theorem. Step 18’s tensor energy identity and the weighted \(K_{3}\) calculation supply the correct ingredients, but the local iteration still needs its own derivation.

---

## 5. Drift exponents and the weighted Bernstein issue

Assume
\[
\|U(t)\|_{\infty}
 \le C_{p}\delta(r^{2}/t)^{2/p}.
\]
Then
\[
\int_{0}^{\theta r^{2}}\|U(t)\|_{\infty}\,dt
 \le C_{p}\frac{p}{p-2}
 \delta\,\theta^{1-2/p}r^{2},
\]
so \(p>2\) is exactly the metric-integrability threshold.

If one also had
\[
\|\chi\nabla U(t)\|_{\infty}
 \le C_{p}\delta\,t^{-1/2}(r^{2}/t)^{2/p},
\]
then
\[
\int_{0}^{\theta r^{2}}\|\chi\nabla U(t)\|_{\infty}\,dt
 \le C_{p}\frac{2p}{p-4}
 \delta\,\theta^{1/2-2/p}r,
\]
and \(p>4\) is exactly the corresponding threshold.

The Hessian evolution is
\[
\partial_t(\nabla^{2}a)_{ij}
 =-(\partial_t\Gamma^{k}_{ij})a_{k},
\]
with
\[
\partial_t\Gamma^{k}_{ij}
 =-g^{k\ell}
 \bigl(\nabla_iU_{j\ell}+\nabla_jU_{i\ell}
       -\nabla_\ell U_{ij}\bigr).
\]
Since \(da=2\chi\,d\chi\),
\[
|\partial_t\nabla^{2}a|
 \le C|d\chi|\,|\chi\nabla U|.
\]
For \(|d\chi|\le C/r\), integration gives
\[
\|\nabla^{2}a(t)-\nabla^{2}a(0)\|_{\infty}
 \le C_{p}\frac{2p}{p-4}
 \delta\,\theta^{1/2-2/p}.
\]
Thus the \(r\)-factor cancels. Relative to an initial Hessian scale \(r^{-2}\), the dimensionless relative change is \(O(\delta r^{2})\). The \(O(\delta/r)\) expression in the proposed chain and in parts of `verify_step19_p4_threshold_and_bernstein.py` is not the result of the displayed Bernstein estimate.

### Full connection versus weighted connection

The exact connection variation involves \(\nabla U\), not \(\chi\nabla U\):
\[
|\nabla^{t}-\nabla^{0}|
 \le C\int_{0}^{t}|\nabla U|\,ds.
\]
A bound for \(\chi\nabla U\) does not control this uniformly where \(\chi\) is small. It does control the contraction
\[
(\nabla^{t}-\nabla^{0})*da,
\]
which is precisely what enters \(\nabla^{2}a\). Therefore “connection drift” must be replaced by either:

- a weighted connection quantity such as \(\chi(\nabla^{t}-\nabla^{0})\), or
- a separate unweighted estimate for \(\nabla U\).

### Why the Bernstein estimate is not yet supplied

The scalar model
\[
u_t=x^{2}u_{xx}
\]
supports the proposed weight: after \(y=\log x\), \(x u_x=u_y\), and ordinary heat-gradient scaling gives \(x|u_x|\sim t^{-1/2}\|u\|_{\infty}\). Thus the factor \(\chi\) is geometrically natural.

For the tensor equation, however, differentiating
\[
\partial_tU=a\Delta_LU+\mathcal B_a(U)
\]
produces terms of the forms
\[
\nabla a*\nabla^{2}U,\qquad
a\,\nabla\mathrm{Rm}*U,\qquad
a\,\mathrm{Rm}*\nabla U,\qquad
\nabla^{3}a*U,\qquad
\nabla^{2}a*\nabla U.
\]
A pointwise estimate for \(a\mathrm{Rm}\) alone does not control
\(a\nabla\mathrm{Rm}\). Li’s Theorem 2.5 gives no derivative estimate. Wang’s Section 4 proves qualitative smooth extension from bounded \(\chi^{2}\mathrm{Rm}\), but its derivative estimates use additional \(L^{q}\) curvature and higher-cutoff-derivative quantities, and the displayed results do not give a sequence-uniform, \(\delta\)-linear estimate with the precise \(t^{-1/2-2/p}\) rate.

A complete analytic object at this point would be a local weighted \(L^{p}\to W^{1,\infty}\) estimate for the degenerate tensor operator, with constants depending only on the provisional Sobolev geometry, finite-neighbor degree, \(K_{3}\), and first-derivative cutoff data. No such result appears in the supplied sources.

---

## Conclusion

1. **The four-dimensional \(\beta\) cancellation is valid**, including collapsed balls, after accounting for enlarged-ball volume comparison. It is a critical-exponent phenomenon rather than an exclusively four-dimensional one.

2. **Finite-neighbor localization is not a direct corollary of Wang’s Theorem 6.3.** The additional localization and relative-Sobolev terms are lower order and appear manageable, but evolving measure and normalized-flow contributions must be included explicitly.

3. **Normalization adds no derivatives above \(\nabla^{2}a\)**, but its Hessian term has one fewer curvature factor than stated. Using \(F=(1+|\mathrm{Rm}|^{2})^{1/2}\) gives a clean repair and changes the local parameter from \(\beta\) to \(\beta+Cr^{2}\), which is still \(O(\beta)\) in the near-\((-1)\)-Einstein setting.

4. **The exponent \(p>4\) is correct once the weighted gradient estimate is assumed.** The metric and weighted-Hessian drift calculations then work, with the corrected \(r\)-dependence above. The weighted Bernstein estimate and the distinction between full and weighted connection control remain the central missing derivations.

5. Weighted estimates for \(aE\) also do not by themselves propagate the global unweighted quantity
\[
Q(t)=\int|E|^{2},
\]
since \(a\) vanishes outside the active region. If \(Q(t)\) is among the first-exit quantities, it still needs a separate global energy argument.