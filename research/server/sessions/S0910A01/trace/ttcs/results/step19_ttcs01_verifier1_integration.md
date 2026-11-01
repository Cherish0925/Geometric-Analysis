# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 19,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step19_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step19_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical correctness of the Whitney-ball reduction for the degenerate cutoff-flow curvature estimate. The construction claims: (1) On Whitney balls B_{crχ₀}(y) in the support of a cutoff flow ∂_tg = -2χ²(Ric+g), Bishop-Gromov comparison transfers total support energy ∫_Ω|Rm|² ≤ CK₀Vol(Ω) to Whitney-ball Li smallness ℓ⁴ fint|Rm|² ≤ CK₀r⁴ with the χ₀ canceling. (2) The Sobolev product A_ℓ||Rm||₂ ≤ C√K₀ r² is independent of χ₀ and collapsed volume. (3) On each Whitney ball, a≈a₀=χ₀², so the operator is non-degenerate; time θr² provides smoothing at ALL Whitney levels simultaneously because the diffusion-to-ball ratio √θ/c is χ₀-independent. (4) The Moser iteration gives |aRm|≤C/t with C independent of χ₀. (5) For U=aE and p>2, ||U||_∞ ≤ Ca₀^{1-2/p}t^{-2/p}||E(0)||_p, so the weighted defect improves as a₀→0. Check: (a) Is the BG comparison in Section 3 correct — does ℓ⁴/Vol(B_ℓ) exactly cancel the χ₀⁴ in ℓ⁴? (b) Does the Sobolev product really cancel the cutoff level algebraically? (c) Is the time matching correct — does physical time θr² suffice for all Whitney levels? (d) Are there hidden obstacles: does the cutoff perturbation (a-a₀)E on the Whitney ball remain absorbable through the Moser iteration? (e) Does the finite-overlap Whitney cover create cumulative constants that could depend on χ₀? (f) Is the claim that ∇²a can be fully removed by integration by parts in the tensor energy correct?

## Integrated Scientific Memo

# Whitney-ball reduction verification

## Verdict

The Whitney construction correctly removes the **scale degeneracy** of \(a=\chi ^2\): the Bishop–Gromov transfer, Sobolev-volume cancellation, and diffusion-time matching are uniform as \(\chi _0\to0\). However, the supplied argument does **not** yet prove the claimed tensor estimate
\[
|a\,\mathrm{Rm}|\le C/t.
\]
The missing step is a complete, coupled curvature–defect energy and parabolic iteration. Several statements require correction:

- BG cancellation is uniform, not literally exact at finite hyperbolic radius.
- The energy budget must be local to each support component/enlargement.
- \(a-a_0=O(ca_0)\), not \(O(c^2a_0)\).
- Whitney localization produces \(c^{-2}r^{-2}\), not merely \(r^{-2}\).
- Integration by parts removes explicit \(\nabla^2a\), but leaves essential \(\nabla E\) and \(E\)-energy terms.
- Bounded overlap controls sums of unnormalized integrals, not automatically sums of normalized Whitney energies.

---

## (a) Bishop–Gromov transfer

Let
\[
W=B_{g_0}(y,\ell),\qquad \ell=cr\chi _0,\qquad \chi _0=\chi(y)>0,
\]
and suppose \(y\in\Omega_j=B_{5r}(p_j)\). Assume a **local** energy budget
\[
\int_{\Omega_j}|\mathrm{Rm}(g(t))|^2\,d\mu_t
 \le C_1\bar K_0\,\operatorname{Vol}_{g_0}(\Omega_j),
\]
where \(\bar K_0\) has units \(L^{-4}\). Metric comparability and
\(\Omega_j\subset B_{g_0}(y,10r)\) give
\[
\ell^4\fint_W^{g(t)}|\mathrm{Rm}|^2
 \le C\bar K_0\,\ell^4
 \frac{\operatorname{Vol}_{g_0}(B_{10r}(y))}
      {\operatorname{Vol}_{g_0}(B_\ell(y))}.
\]
Under \(\operatorname{Ric}_{g_0}\ge-3g_0\),
\[
\frac{\operatorname{Vol}(B_{10r}(y))}
     {\operatorname{Vol}(B_\ell(y))}
\le \frac{V_{-1}(10r)}{V_{-1}(\ell)}.
\]
In dimension four,
\[
V_{-1}(s)=2\pi^2\int_0^s\sinh^3u\,du.
\]
For \(0<\ell\le r\le r_0\),
\[
V_{-1}(\ell)\ge \frac{\pi^2}{2}\ell^4,
\qquad
V_{-1}(10r)\le C(r_0)r^4,
\]
and hence
\[
\boxed{\ell^4\fint_W|\mathrm{Rm}|^2
 \le C(r_0,\zeta)\bar K_0r^4.}
\]

Thus the \(\chi _0^4\) dependence is eliminated uniformly. It is not an exact cancellation because \(V_{-1}(\ell)\) is not exactly proportional to \(\ell^4\); the script only demonstrates the small-radius asymptotics.

### Necessary locality correction

A single estimate
\[
\int_{\Omega}|\mathrm{Rm}|^2\le
\bar K_0\operatorname{Vol}(\Omega),
\qquad \Omega=\bigcup_j\Omega_j,
\]
does not imply the displayed bound uniformly on every \(\Omega_j\): energy may concentrate in one component, introducing
\(\operatorname{Vol}(\Omega)/\operatorname{Vol}(\Omega_j)\). Each base support ball or a bounded enlargement must have its own energy budget, unless the union has additional controlled volume distribution.

There is also a normalization mismatch. If the hypothesis is instead
\[
r^4\fint_{B_{6r}}|\mathrm{Rm}|^2\le K_0^{\rm sc},
\]
then the transferred result is \(CK_0^{\rm sc}\), not
\(CK_0^{\rm sc}r^4\).

---

## (b) Sobolev product

Use the squared Sobolev form
\[
\|\varphi\|_4^2
 \le S_\ell\int_W\bigl(|\nabla\varphi|^2+\ell^{-2}\varphi^2\bigr),
\qquad
S_\ell\le C\frac{\ell^2}{\operatorname{Vol}(W)^{1/2}}.
\]
Then
\[
\begin{aligned}
S_\ell\|\mathrm{Rm}\|_{L^2(W)}
&\le C\sqrt{\bar K_0}\,\ell^2
 \left(\frac{\operatorname{Vol}(\Omega_j)}
 {\operatorname{Vol}(W)}\right)^{1/2}\\
&\le C\sqrt{\bar K_0}\,\ell^2
 \left(\frac{V_{-1}(10r)}{V_{-1}(\ell)}\right)^{1/2}\\
&\le C\sqrt{\bar K_0}\,r^2.
\end{aligned}
\]
Therefore
\[
\boxed{S_\ell\|\mathrm{Rm}\|_2
 \le C\sqrt{\bar K_0}\,r^2,}
\]
independently of \(\chi _0\) and collapsed volume.

This is the coefficient entering
\[
\int a|\mathrm{Rm}|^3
 =\int |\mathrm{Rm}|\,|\chi\eta\mathrm{Rm}|^2.
\]

The notes use inconsistent Sobolev notation. If
\[
\|\varphi\|_4\le A_\ell
(\|\nabla\varphi\|_2+\ell^{-1}\|\varphi\|_2),
\]
then \(A_\ell\asymp \ell/\operatorname{Vol}(W)^{1/4}\) and the relevant product is
\[
A_\ell^2\|\mathrm{Rm}\|_2,
\]
not \(A_\ell\|\mathrm{Rm}\|_2\).

The numerical value \(0.111\) verifies scaling only; it omits Sobolev, tensor, metric-comparison, and energy-persistence constants and therefore does not establish absorption.

---

## (c) Physical time at all Whitney levels

Lipschitz control gives
\[
|\chi-\chi _0|\le Lc\chi _0
\]
on \(W\), hence, if \(Lc<1\),
\[
(1-Lc)^2a_0\le a\le(1+Lc)^2a_0,
\qquad a_0=\chi _0^2.
\]
At physical time \(T=\theta r^2\), the diffusion radius is
\[
\sqrt{a_0T}=\chi _0r\sqrt{\theta},
\]
so
\[
\frac{\sqrt{a_0T}}{\ell}=\frac{\sqrt{\theta}}{c}.
\]
Thus \(\theta\le c^2/4\) places the relevant diffusion cylinder inside \(W\), uniformly in \(\chi _0\). Equivalently,
\[
\frac{\ell^2}{a_0}=c^2r^2.
\]

This matching is correct. Nested spatial cutoffs enlarged by a factor \(q\) require \(qLc<1\).

One must also retain the localization contribution
\[
a|\nabla\eta|^2\sim\frac{a_0}{\ell^2}
 =\frac1{c^2r^2}.
\]
Thus the local Gronwall factor over \(T=\theta r^2\) is
\[
\exp(C\theta/c^2),
\]
not merely \(\exp(C\theta)\). The same restriction \(\theta\lesssim c^2\) controls both diffusion containment and localization growth.

---

## (d) Cutoff perturbation and Moser iteration

The source’s estimate
\[
a-a_0=O(c^2a_0)
\]
is false. In fact,
\[
\frac{|a-a_0|}{a_0}
 \le Lc(2+Lc)=O(Lc).
\]
For \(L=2,c=0.1\), this permits a \(44\%\) variation, consistent with
\(a/a_0\in[0.64,1.44]\).

Accordingly, \((a-a_0)E\) should not be treated merely as a small forcing. The correct mechanism is that, after time rescaling by \(a_0\), the operator is uniformly parabolic with ellipticity ratio
\[
\frac{(1+Lc)^2}{(1-Lc)^2},
\]
independent of \(\chi _0\). Moreover,
\[
\frac{\ell|\nabla a|}{a_0}=O(cL),\qquad
\frac{\ell^2}{a_0}\frac{|\nabla a|^2}{a}=O(c^2L^2).
\]
These are uniform coefficient bounds, not a completed absorption proof.

The supplied Moser argument remains incomplete because:

1. the full curvature equation has \(E\)-dependent derivative sources;
2. energy persistence on each Whitney cylinder has not been derived from the coupled system;
3. an all-exponent tensor iteration with every coefficient tracked has not been supplied.

In particular, the Python script evaluates a schematic inequality; it does not derive the curvature evolution or prove a parabolic iteration.

The branch materials disagree about whether critical curvature absorption is automatically exponent-independent. The safe conclusion from the supplied sources is that this is unresolved until the exact tested curvature inequality is written with its \(p\)-dependence. The A03 warning definitely applies to the defect iteration; whether the curvature iteration fits a Li theorem with a fixed critical threshold must be verified from the precise curvature equation rather than asserted.

Hence
\[
|a\,\mathrm{Rm}|\le C/t
\]
is compatible with the Whitney scaling but not established here.

---

## (e) Whitney overlap

Intersecting enlarged Whitney balls have comparable radii. If
\(qW_i\cap qW_j\ne\varnothing\), then
\[
|\chi(y_i)-\chi(y_j)|
 \le qcL\bigl(\chi(y_i)+\chi(y_j)\bigr),
\]
so \(qcL<1\) gives a uniform ratio \(\ell_i/\ell_j\). Local doubling then yields overlap multiplicity
\[
N=N(n,L,c,q,r_0),
\]
independent of \(\chi _0\). Infinitely many levels accumulating at
\(\{\chi=0\}\) do not themselves create a divergent factor:
\[
\sum_\alpha\int_{W_\alpha}F
 \le N\int_{\{\chi>0\}}F.
\]

However, finite overlap directly controls **unnormalized integrals**, not sums of
\[
R_\alpha=\ell_\alpha^4\fint_{W_\alpha}|\mathrm{Rm}|^2,
\]
because these carry varying weights
\(\ell_\alpha^4/\operatorname{Vol}(W_\alpha)\). The proof should use either:

- a supremum of normalized local energies, with a finite-neighbor differential inequality; or
- a support-summed quantity built from unnormalized integrals.

The base support family \(\Omega_j\) must likewise have bounded multiplicity or separate local budgets.

---

## (f) Removal of \(\nabla^2a\)

A pointwise Hessian bound can plausibly be avoided in weak localized tensor energies, but “\(\nabla^2a\) is fully removed” is incomplete unless all resulting coupled terms are retained.

For \(H=\mathrm{Rm}\), a representative term is
\[
I=\int\eta^2\langle\nabla^2a*E,H\rangle.
\]
One integration by parts yields schematically
\[
I=
-\int\eta^2\nabla a*\nabla E*H
-\int\eta^2\nabla a*E*\nabla H
-2\int\eta\nabla\eta*\nabla a*E*H.
\]
Young’s inequality gives contributions of the form
\[
\varepsilon\int\eta^2a|\nabla H|^2
+\varepsilon\int\eta^2a|\nabla E|^2
+C_\varepsilon\int\eta^2\frac{|\nabla a|^2}{a}
 (|H|^2+|E|^2)
+\text{localization terms}.
\]
Since
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
 \le 4L^2r^{-2},
\]
no inverse power of \(\chi\) remains. But the calculation necessarily leaves:

- an \(a|\nabla E|^2\) term requiring defect dissipation;
- an \(r^{-2}|E|^2\) source;
- at higher curvature powers, mixed quantities such as
  \[
  \frac{|\nabla a|^2}{a}|E|^2|H|^{p-2}.
  \]

Therefore the honest energy estimate must be coupled, for example through
\[
H_\alpha=R_\alpha+\kappa P_\alpha,
\]
where \(P_\alpha\) is defect energy. The curvature-only inequality in Section 6 omits this essential structure. Explicit \(\nabla^2a\) can be removed, but not without replacing it by controlled first-derivative **couplings**.

---

## Weighted defect claim

For the constant-coefficient model in dimension four,
\[
U(t)=a_0e^{a_0t\Delta}E(0),
\]
and hence
\[
\|U(t)\|_\infty
 \le C a_0^{\,1-2/p}t^{-2/p}\|E(0)\|_p.
\]
For \(p>2\), this improves as \(a_0\to0\). This model calculation is correct.

For the tensor flow, the corresponding estimate still requires:

1. fixed-\(p\) spatial control of \(U=aE\);
2. a weighted curvature potential, such as
   \[
   |a\,\mathrm{Rm}|\le C/t
   \quad\text{or}\quad
   \int a|\mathrm{Rm}|^3\le C/(A_\ell^4t);
   \]
3. control of cutoff commutators and evolving geometry.

Thus the boundary improvement is valid scaling evidence, not yet a proved flow estimate.

## Final assessment

- **(a)** Valid after imposing local support energy; cancellation is uniform, not exact.
- **(b)** Valid with the squared Sobolev coefficient.
- **(c)** Correct uniformly across all Whitney levels; localization also forces \(\theta=O(c^2)\).
- **(d)** Not proved. The coefficient variation is \(O(c)\), handled by uniform ellipticity rather than \(O(c^2)\)-perturbative absorption.
- **(e)** No \(\chi _0\)-dependent overlap loss for unnormalized integrals, but normalized-energy summation must be reformulated.
- **(f)** Explicit Hessians can be integrated away, but this generates indispensable curvature–defect coupling.

The precise unresolved object is a full localized tensor derivation, followed by a finite-neighbor/infinite-Whitney-graph continuation and parabolic estimate for the coupled curvature–defect system. Until that is supplied, the Whitney reduction establishes uniform geometry and scaling but not the claimed \(|a\,\mathrm{Rm}|\le C/t\) theorem.