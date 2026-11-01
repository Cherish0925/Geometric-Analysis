# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step23_cooperative_persistence_theorem.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A01/workspace/notes/step22_current_energy_formulation.md",
    "Sessions/S0910A01/workspace/scripts/step23_cooperative_persistence.py"
  ]
}
```

## Task

Verify the central structural claim in the Step 23 cooperative persistence theorem for the four-dimensional negative LeBrun/Ishida-LeBrun cutoff-flow route. The claim: for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) on a closed four-manifold, when the q=2 curvature energy H_{2,α} = ∫ η_α² F² is tested against η_α² H (the testing function), and the reaction ∫ η_α² aF³ is absorbed using the Sobolev variable v = η_α a^{1/2} F, the resulting gradient integral ||∇v||² decomposes into the α-component dissipation D_{2,α} plus r⁻² H-type localization terms, all supported within U_α. Specifically: (1) The gradient ∇(η_α a^{1/2} F) = η_α a^{1/2}∇F + η_α (∇a/(2a^{1/2}))F + a^{1/2}F ∇η_α has all three contributions supported in supp(η_α) ⊂ U_α. (2) The term η_α² a|∇F|² is bounded by C·D_{2,α}. (3) The term η_α²(|∇a|²/a)F² ≤ Cr⁻² H_{2,α}. (4) The term a|∇η_α|²F² ≤ Cr⁻² ∫_{U_α}F². (5) Therefore the Sobolev inequality ||v||₄² ≤ A_α²(CD_{2,α} + Cr⁻²∫_{U_α}F²) involves ONLY the α-component dissipation, no neighbor dissipation Z_β. (6) After Hölder R ≤ γ_α(D + r⁻²H) and absorption into cD, the vector inequality is S' + cZ ≤ (b/r²)BS with ε=0 (no εBZ term). Check whether any term was missed: inverse metric variation in F, measure evolution, Hessian-a integrations by parts, the lower-order aFq term from normalization, or overlap contributions to ∫_{U_α}F². Also check: does the cooperative comparison for the resulting S'≤(b/r²)BS give componentwise Gronwall with constants independent of component count?

## Output

## Scientific memo

### Main finding

The locality computation behind the Sobolev absorption is correct: when the same cutoff \(\eta_\alpha\) defines both the tested energy and the Sobolev variable, every gradient term is supported in \(U_\alpha\) and is controlled by \(D_{2,\alpha}\) plus zeroth-order localization integrals. None of the listed geometric variation terms introduces \(D_{2,\beta}\).

However, the passage from this local inequality to the displayed cooperative vector system uses

\[
\int_{U_\alpha}F^2\le \sum_{\beta\sim\alpha}H_{2,\beta},
\tag{A}
\]

and (A) does not follow from bounded overlap. With the cutoffs and ball geometry stated in Step 23, it is generally false. Thus \(\varepsilon=0\) is verified at the differential-energy level, while the vector inequality additionally requires a covering domination or nested outer energies.

### 1. Exact gradient decomposition

Assume the usual cutoff convention \(\chi\ge0\), so \(a^{1/2}=\chi\). It is cleaner to avoid division by \(a\) and write

\[
v=\eta_\alpha\chi F,\qquad
\nabla v
=\eta_\alpha\chi\nabla F
+\eta_\alpha F\nabla\chi
+\chi F\nabla\eta_\alpha.
\]

Hence

\[
\int |\nabla v|^2
\le 3\int\eta_\alpha^2a|\nabla F|^2
+3\int\eta_\alpha^2|\nabla\chi|^2F^2
+3\int a|\nabla\eta_\alpha|^2F^2.
\tag{1}
\]

The coefficient \(2\) used in Step 23 is not valid for three arbitrary summands; \(3\) works and has no structural effect.

Since

\[
|\nabla F|
=\frac{|\langle \operatorname{Rm},\nabla\operatorname{Rm}\rangle|}{F}
\le |\nabla\operatorname{Rm}|,
\]

the first term in (1) is at most \(3D_{2,\alpha}\). Moreover,

\[
|\nabla\chi|^2=\frac{|\nabla a|^2}{4a}
\]

on \(\{\chi>0\}\), with the smooth extension understood on \(\{\chi=0\}\). Under the Whitney estimate \(|\nabla\chi|\le Cr^{-1}\),

\[
\int\eta_\alpha^2|\nabla\chi|^2F^2
\le Cr^{-2}H_{2,\alpha}.
\]

Finally, using \(a\le1\) and \(|\nabla\eta_\alpha|\le Cr^{-1}\),

\[
\int a|\nabla\eta_\alpha|^2F^2
\le Cr^{-2}\int_{U_\alpha}F^2.
\]

All three integrands are supported in \(\operatorname{supp}\eta_\alpha\) or \(\operatorname{supp}\nabla\eta_\alpha\), both contained in \(U_\alpha\). Therefore

\[
\boxed{
\|v\|_4^2
\le C A_\alpha^2
\left(
D_{2,\alpha}
+r^{-2}\int_{U_\alpha}F^2
\right).}
\tag{2}
\]

No neighboring gradient energy occurs in (2).

### 2. The omitted geometric variation terms remain local

A full \(q=2\) term ledger has the schematic form

\[
\frac{d}{dt}H_{2,\alpha}+c_0D_{2,\alpha}
\le
C\int\eta_\alpha^2aF^3
+C\int\eta_\alpha^2
\left(a+\frac{|\nabla a|^2}{a}\right)F^2
+C\int a|\nabla\eta_\alpha|^2F^2.
\tag{3}
\]

Each listed source fits (3):

- **Inverse metric variation.** For a covariant curvature tensor, differentiating the inverse metrics in \(|\operatorname{Rm}|^2\) produces
  \[
  a\,E*\operatorname{Rm}*\operatorname{Rm},
  \]
  bounded by \(CaF^3\) because \(|E|\le CF\).

- **Measure evolution.**
  \[
  \partial_t d\mu=-a\,\operatorname{tr}_g(E)\,d\mu,
  \]
  so its contribution is bounded by \(CaF^3\).

- **Hessian-\(a\) terms.** A representative integral satisfies
  \[
  \int\eta_\alpha^2\operatorname{Rm}*(\nabla^2a)*E
  =
  -\int\nabla a*
  \nabla(\eta_\alpha^2\operatorname{Rm}*E).
  \]
  Using
  \[
  |E|\le CF,\qquad |\nabla E|\le C|\nabla\operatorname{Rm}|,
  \]
  and Young’s inequality gives
  \[
  \varepsilon D_{2,\alpha}
  +C_\varepsilon\int\eta_\alpha^2
  \frac{|\nabla a|^2}{a}F^2
  +C\int a|\nabla\eta_\alpha|^2F^2.
  \]
  This again uses only \(D_{2,\alpha}\).

- **Normalization term.** The linear \(a\operatorname{Rm}\) contribution gives \(CaF^2\). It is a local zeroth-order term. For \(r\le1\), it can be included in \(Cr^{-2}\int_{U_\alpha}F^2\); otherwise the rate is \(C(1+r^{-2})\).

Thus none of these terms changes the no-neighbor-dissipation structure.

### 3. Reaction absorption

In four dimensions,

\[
R_{2,\alpha}
=\int Fv^2
\le \|F\|_{L^2(U_\alpha)}\|v\|_4^2.
\]

With

\[
\gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)},
\]

equation (2) yields

\[
R_{2,\alpha}
\le C\gamma_\alpha
\left(
D_{2,\alpha}
+r^{-2}\int_{U_\alpha}F^2
\right).
\tag{4}
\]

The precise absorption condition is \(C\gamma_\alpha<c_0/2\), rather than literally \(\gamma_\alpha<c_0/2\) unless the constant \(C\) is incorporated into the definition. After absorption,

\[
H_{2,\alpha}'+\frac{c_0}{2}D_{2,\alpha}
\le Cr^{-2}\int_{U_\alpha}F^2.
\tag{5}
\]

Equation (5) is the verified local structural result and contains no \(D_{2,\beta}\).

### 4. Missing covering domination in Step 23

Bounded overlap gives an upper-multiplicity relation such as

\[
\sum_\beta \mathbf 1_{U_\beta}\le N,
\]

but it does not imply

\[
\mathbf 1_{U_\alpha}
\le C\sum_{\beta\sim\alpha}\eta_\beta^2.
\]

Indeed, Step 23 assumes centers separated by at least \(10r\), while \(U_\alpha=B_{5r}(p_\alpha)\) and \(\eta_\alpha\) vanishes outside \(B_{4r}(p_\alpha)\). The \(U_\alpha\) are essentially disjoint, and the annulus

\[
B_{5r}(p_\alpha)\setminus B_{4r}(p_\alpha)
\]

is not measured by \(H_{2,\alpha}\) or by a neighboring weighted energy. A smooth function concentrated in this annulus violates (A). No supplied curvature hypothesis excludes the analogous concentration for \(F\).

A sufficient replacement is an explicit domination

\[
\int_{U_\alpha}F^2
\le C_0\sum_{\beta\sim\alpha}
\int \xi_\beta^2F^2,
\tag{6}
\]

where the outer cutoffs satisfy

\[
\mathbf1_{U_\alpha}
\le C_0\sum_{\beta\sim\alpha}\xi_\beta^2.
\]

This is the nested inner/outer construction already present in Step 22. Under (6), only \(H\)-energies enter from neighboring components; the dissipation in (4) remains \(D_{2,\alpha}\).

### 5. Cooperative comparison

Assuming (6), fixed time-uniform Sobolev weights \(A_\alpha\), and neighboring comparability \(A_\alpha/A_\beta\le C_A\), multiplying (5) by \(A_\alpha^4\) gives

\[
S_\alpha'+cZ_\alpha
\le \frac{b}{r^2}
\sum_{\beta}B_{\alpha\beta}S_\beta,
\qquad
B_{\alpha\beta}\ge0,
\qquad
\sum_\beta B_{\alpha\beta}\le L.
\tag{7}
\]

Let \(m(t)=\max_\alpha S_\alpha(t)\). At an index attaining the maximum,

\[
D^+m(t)\le \frac{bL}{r^2}m(t),
\]

and hence

\[
\boxed{
S_\alpha(t)\le
e^{bLt/r^2}\max_\beta S_\beta(0).}
\tag{8}
\]

This constant is independent of the number of components. The same follows from the entrywise-positive matrix semigroup \(e^{(bt/r^2)B}\).

Likewise,

\[
c\int_0^tZ_\alpha(s)\,ds
\le e^{bLt/r^2}\max_\beta S_\beta(0).
\tag{9}
\]

For total-energy estimates in the \(\ell^1\) norm, row sums alone are insufficient; uniform column sums are also needed. A symmetric finite-neighbor relation together with two-sided \(A_\alpha/A_\beta\) comparability supplies them.

The \(A_\alpha\) must be fixed upper Sobolev coefficients valid throughout the time interval. If they are differentiated as evolving quantities, \(S_\alpha'\) acquires an additional \(4A_\alpha'/A_\alpha\) term.

### 6. Two related artifacts

- The Python script assumes the no-neighbor-dissipation identity in its text; it numerically illustrates only the cooperative ODE after that identity is supplied.
- The time-averaging argument in Step 23 does not justify a bound at \(T/2\), nor propagation to times earlier than the selected \(t_*\). A common-time estimate follows instead by integrating
  \[
  H_3(t)\le e^{(t-s)M}H_3(s),\qquad s<t,
  \]
  over \(s\in[t/2,t]\).
- In the script’s resolvent section,
  \[
  \rho\approx0.0292,\qquad
  1-\frac{0.1}{\rho}\approx-2.43,
  \]
  so the printed positivity requirement is not met for the chosen numbers.

### Conclusion

The central locality statement is mathematically sound: Sobolev absorption with \(v=\eta_\alpha a^{1/2}F\), together with the full curvature-variation ledger, uses only \(D_{2,\alpha}\). Thus no \(\varepsilon BZ\) term is generated by the PDE calculation. The cooperative Gronwall estimate is also correct and independent of component count once the vector inequality is available.

The present Step 23 definitions do not supply the required domination of \(\int_{U_\alpha}F^2\) by neighboring weighted energies. An explicit covering lower bound or the nested outer-cutoff energies from Step 22 is the missing geometric ingredient connecting the verified local inequality to the displayed cooperative system.