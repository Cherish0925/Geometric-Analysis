# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/scripts/verify_step24_exact_curvature_variation.py",
    "Sessions/S0910A03/workspace/scripts/verify_step24_downstream_chain.py",
    "Sessions/S0910A03/workspace/notes/step22_inverse_square_correction_and_two_stage_architecture.md"
  ]
}
```

## Task

Verify the following two claims for the 4D normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed Riemannian 4-manifold.

CLAIM 1 (Normalization reaction): Under h = -2a·g with a = χ², the linearized Riemann curvature variation has ZERO lower-order R·h contribution. The conformal piece contributes only the Kulkarni-Nomizu Hessian source -(∇²a ∧ g) to ∂_t R_{ijkl}. Consequently, the full flow h = -2a(Ric+g) has curvature evolution ∂_t Rm = a·ΔRm + a·(Rm*Rm) + (∇a)*(∇Ric) + (∇²a ∧ E), where the quadratic reaction is EXACTLY the same as Wang's unnormalized local Ricci flow, and the normalization produces no linear Rm reaction.

CLAIM 2 (Subcritical downstream chain): Conditional on the q=2,3 integrated energy inequalities holding for the normalized cutoff flow, the complete chain from H₃(t) ≤ Cγ³/t to the gap theorem on critical Ishida-LeBrun 4-manifolds is logically sound:
(a) The subcritical Moser iteration from L³ to L^∞ converges because 3 > n/2 = 2 in 4D. The exponent sequence q_k = 3·(3/2)^k and the per-step constant product converge.
(b) The defect iteration from J₆ to |aE| ≤ Cδ(r²/t)^{1/3} uses the same subcritical potential.
(c) The metric drift ∫₀^{θr²} |aE| dt is integrable (proportional to δ), hence self-improving.
(d) All five first-exit conditions (Sobolev, energy, curvature, defect, metric) are self-improving.

Please verify these using the general linearized curvature variation formula (Chow-Lu-Ni Lemma 2.27) and the standard subcritical Moser theory. Identify any errors, missing hypotheses, or gaps in the chain.

## Output

# Scientific verification memo

## 1. Curvature variation under the conformal normalization term

For an all-lowered Riemann tensor, the first statement is incorrect. Specializing the general curvature linearization to

\[
h=\varphi g
\]

gives, with the Kulkarni–Nomizu convention

\[
(A\owedge B)_{ijkl}
=A_{ik}B_{jl}+A_{jl}B_{ik}-A_{il}B_{jk}-A_{jk}B_{il},
\]

the formula

\[
(D\operatorname{Rm})_g(\varphi g)_{ijkl}
=
\varphi R_{ijkl}
+\frac12(\nabla^2\varphi\owedge g)_{ijkl}.
\tag{1}
\]

Thus, for \(\varphi=-2a\),

\[
\boxed{
(D\operatorname{Rm})_g(-2ag)_{ijkl}
=
-2aR_{ijkl}-(\nabla^2a\owedge g)_{ijkl}.}
\tag{2}
\]

The Hessian sign changes if the opposite Riemann-sign convention is used, but the algebraic term \(-2aR_{ijkl}\) cannot disappear.

### Constant-scaling test

Set \(a\equiv1\) and evolve only by \(\partial_tg=-2g\). Then

\[
g(t)=e^{-2t}g(0).
\]

The Levi-Civita connection and \(R^l{}_{ijk}\) remain fixed, while lowering the last index gives

\[
R_{ijkl}(t)=e^{-2t}R_{ijkl}(0).
\]

Consequently,

\[
\partial_tR_{ijkl}=-2R_{ijkl},
\]

which directly rules out zero algebraic variation for \(R_{ijkl}\).

The source of the confusion is tensor valence. For the mixed tensor \(R^l{}_{ijk}\), a conformal variation has only Hessian terms:

\[
(DR)^l{}_{ijk}(\varphi g)
=
\frac12\left(
\delta^l_j\nabla_i\nabla_k\varphi
-\delta^l_i\nabla_j\nabla_k\varphi
-g_{jk}\nabla_i\nabla^l\varphi
+g_{ik}\nabla_j\nabla^l\varphi
\right).
\]

Lowering \(l\) contributes the missing term

\[
h_{lm}R^m{}_{ijk}=\varphi R_{ijkl}.
\]

The cancellation in `verify_step24_downstream_chain.py` therefore corresponds to the mixed tensor calculation while its prose refers to \(R_{ijkl}\).

### Correct full tensor structure

For the local Ricci part one has schematically, with the same convention,

\[
(D\operatorname{Rm})_g(-2a\operatorname{Ric})
=
a\Delta\operatorname{Rm}
+aQ(\operatorname{Rm})
+\mathcal C(\nabla a,\nabla\operatorname{Ric})
-(\nabla^2a\owedge\operatorname{Ric}),
\]

where \(Q\) is Wang’s quadratic curvature expression and \(\mathcal C\) is the standard first-derivative contraction. Adding (2), and writing \(E=\operatorname{Ric}+g\), gives

\[
\boxed{
\partial_t\operatorname{Rm}
=
a\Delta\operatorname{Rm}
+aQ(\operatorname{Rm})
-2a\operatorname{Rm}
+\mathcal C(\nabla a,\nabla E)
-(\nabla^2a\owedge E).}
\tag{3}
\]

Hence:

* The quadratic expression \(Q(\operatorname{Rm})\) is the same one as in the unnormalized local Ricci flow.
* The normalization adds the linear reaction \(-2a\operatorname{Rm}\).
* The Hessian terms do combine into an expression linear in \(E\), which is the important homogeneous structure used in Step 23.
* At \(E=0\), the full right-hand side vanishes. For \(\operatorname{Ric}=-g\), the Einstein curvature identity gives
  \[
  \Delta\operatorname{Rm}+Q(\operatorname{Rm})=2\operatorname{Rm},
  \]
  so the local-Ricci reaction cancels the normalization term in (3).

The linear term is harmless for the weighted energy estimate:

\[
\left|
\int \eta^2a^{q-2}F^{q-2}
\langle \operatorname{Rm},-2a\operatorname{Rm}\rangle
\right|
\le C\int\eta^2a^{q-1}F^q
\le CH_q.
\]

For \(r\le1\), this is included in \(Cr^{-2}H_q\). Thus the main Step 23 energy architecture can survive this correction.

The two supplied scripts are internally inconsistent here. `verify_step24_exact_curvature_variation.py` retains a schematic \(a\operatorname{Rm}\) term, while `verify_step24_downstream_chain.py` asserts that it vanishes. Neither SymPy calculation implements the complete indexed Chow–Lu–Ni formula; the constant-scaling calculation fixes the issue immediately.

---

## 2. Correct normalization of the \(H_3\) estimate

With the Sobolev coefficient used in Step 23,

\[
\|u\|_4^2\le \mathsf S
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\]

the estimate supplied by (4.4) is

\[
\boxed{\mathsf S^2H_3(t)\le \frac{C\gamma^3}{t},}
\tag{4}
\]

not merely \(H_3(t)\le C\gamma^3/t\).

This factor is essential when the local volume collapses, because

\[
\mathsf S\lesssim r^2\operatorname{Vol}(U)^{-1/2}
\]

need not remain uniformly bounded. The starting statement in the question is sufficient only if \(\mathsf S\) is already absorbed into the notation.

The reason (4) is exactly the right normalization is the potential estimate. On a plateau, or in the corresponding weighted formulation with \(\mathcal K=aF\) and \(d\nu=a^{-2}d\mu\),

\[
\begin{aligned}
\int Fv^2
&\le \|F\|_3\|v\|_3^2 \\
&\le H_3^{1/3}\|v\|_2^{2/3}\|v\|_4^{4/3}\\
&\le H_3^{1/3}\mathsf S^{2/3}
      \|v\|_2^{2/3}\mathcal E[v]^{2/3}\\
&\le \varepsilon\mathcal E[v]
 +C\varepsilon^{-2}\mathsf S^2H_3\,\|v\|_2^2.
\end{aligned}
\tag{5}
\]

On a time slab \([t/2,t]\), (4) makes the integrated zero-order coefficient dimensionless:

\[
\int_{t/2}^t \mathsf S^2H_3(s)\,ds
\le C\gamma^3\log2.
\tag{6}
\]

This is the quantitative input needed by subcritical parabolic Moser theory.

---

## 3. Convergence of the exponent product

For

\[
q_k=3\left(\frac32\right)^k,
\]

one has

\[
\sum_{k=0}^\infty\frac1{q_k}=1,
\qquad
\sum_{k=0}^\infty\frac{\log q_k}{q_k}
=
\log3+2\log\frac32<\infty.
\]

Therefore, if the \(k\)-th energy step has a constant bounded by \(Cq_k^A\), then

\[
\prod_{k=0}^\infty(Cq_k^A)^{1/q_k}<\infty.
\tag{7}
\]

This algebraic part is correct. On a slab separated from \(t=0\), the potential belongs to \(L^\infty_tL^3_x\), and

\[
\frac{n}{2p}=\frac{4}{2\cdot3}=\frac23<1,
\]

which is the usual parabolic subcritical relation.

Under a valid scalar or all-exponent weighted energy inequality, the expected smoothing scale is

\[
\begin{aligned}
\|aF(t)\|_\infty
&\le C(\gamma)\mathsf S^{2/3}t^{-2/3}
      H_3(t/2)^{1/3}\\
&\le \frac{C(\gamma)\gamma}{t},
\end{aligned}
\tag{8}
\]

where (4) supplies the cancellation of \(\mathsf S\). This explains the desired \(t^{-1}\) behavior without any local-volume factor.

However, convergence of (7) by itself is not an iteration proof. The \(q=2,3\) inequalities alone do not provide:

1. energy inequalities for every \(q\ge3\), with controlled \(q\)-dependence; or
2. a scalar weak inequality for \(aF\) to which a standard theorem applies.

Because \(a\) vanishes in the transition annulus, the operator is degenerate there. Ordinary uniformly parabolic Moser theory applies directly only on an inner plateau where \(a=1\). A global estimate for \(aF\) requires the weighted formulation or a direct all-\(q\) argument. The supplied material has not derived that argument.

---

## 4. Defect iteration and metric drift

Assuming the homogeneous \(J_m\) inequalities hold for every \(m\ge6\), together with

\[
J_6(t/2)\le C\delta^6V,
\qquad
\mathsf S\lesssim r^2V^{-1/2},
\tag{9}
\]

the standard \(L^6\)-to-\(L^\infty\) scaling gives

\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C(\gamma)\mathsf S^{1/3}t^{-1/3}
          J_6(t/2)^{1/6}\\
&\le C(\gamma)\delta
   \left(\frac{r^2}{t}\right)^{1/3}.
\end{aligned}
\tag{10}
\]

The volume factors cancel:

\[
\mathsf S^{1/3}V^{1/6}
\lesssim
(r^2V^{-1/2})^{1/3}V^{1/6}
=r^{2/3}.
\]

Starting the subcritical iteration at \(t/2\), rather than integrating the \(H_3(s)\sim s^{-1}\) coefficient from zero, is essential. Persistence of \(J_6\) from time zero must come from the separate critical \(L^2\)-curvature absorption in (5.4)–(5.6); it does not follow from the curvature \(q=2,3\) inequalities.

Conditional on (10), the drift computation is correct:

\[
\begin{aligned}
\int_0^{\theta r^2}|aE(t)|\,dt
&\le C\delta r^{2/3}
       \int_0^{\theta r^2}t^{-1/3}\,dt\\
&=\frac32C\delta\theta^{2/3}r^2.
\end{aligned}
\tag{11}
\]

For a fixed tangent vector,

\[
\left|\frac{d}{dt}\log g_t(v,v)\right|
\le2|aE|_{g(t)},
\]

so (11) gives a bilipschitz factor bounded by the exponential of a quantity proportional to \(\delta\).

---

## 5. Remaining mathematical gaps in the asserted complete chain

The following ingredients are not consequences of the \(q=2,3\) curvature inequalities alone:

1. **All-exponent curvature evolution.**  
   A scalar Kato inequality or weighted \(H_q\) inequalities for every \(q\ge3\) are needed. The transition terms involving \(da\) and \(\nabla^2a\) must retain constants with acceptable growth in \(q\).

2. **Weighted treatment of the transition annulus.**  
   The estimate \(H_3=\int aF^3\,d\mu\) controls \(F\) unweighted only where \(a=1\). Global control of \(aF\), and especially global control of \(aE\) needed for metric comparability, requires a direct weighted Moser theorem for
   \[
   d\nu=a^{-2}d\mu
   \]
   or an equivalent componentwise energy construction.

3. **Independent \(J_6\) evolution.**  
   Step 23 states the homogeneous defect inequality schematically, but its indexed derivation and all-\(m\) continuation are not supplied. This is an additional PDE input beyond the curvature \(q=2,3\) formulas.

4. **Quantitative first-exit margins.**  
   Sobolev persistence follows from bilipschitz comparability, and energy persistence follows from (3.5). Curvature and defect improvement depend on the missing weighted iterations. Strict improvement also requires explicit choices of \(\theta\), the initial \(\gamma\), the bilipschitz margin, and \(\delta\).

5. **Smooth continuation of the degenerate flow.**  
   The coefficient \(a=\chi^2\) vanishes outside the active region. A DeTurck or Yang–Wang continuation result adapted to the normalization term is still needed. Step 23 itself lists this as unresolved.

6. **Passage from smoothing to the Ishida–LeBrun contradiction.**  
   The supplied files only enumerate the exponential-pullback, calibrated-density, \(W^+\)-spectrum, and projector steps. Their equations and compactness argument are not present, so the final geometric implication cannot be verified from these artifacts.

The downstream script itself records unresolved dimensional calculations— including “this needs more care” and “accept the standard result”—before printing that the chain is complete. Its exit code verifies only the displayed symbolic arithmetic.

## Overall assessment

* For \(R_{ijkl}\), the conformal normalization contributes both
  \[
  -2aR_{ijkl}
  \quad\text{and}\quad
  -(\nabla^2a\owedge g)_{ijkl}.
  \]
  Zero algebraic contribution is correct only for the mixed tensor \(R^l{}_{ijk}\).

* The useful homogeneous identity
  \[
  \text{Hessian terms}=-(\nabla^2a\owedge E)
  \]
  is correct and preserves stationarity when \(E=0\).

* The subcritical exponent product, defect smoothing exponent \(1/3\), and metric-drift integral are mathematically consistent after restoring the factor \(\mathsf S^2\) in the \(H_3\) estimate.

* The complete downstream theorem does not yet follow from the stated \(q=2,3\) hypotheses. The all-exponent weighted estimates, the independent defect hierarchy, degenerate-flow continuation, quantitative first-exit closure, and final calibrated compactness argument remain mathematically substantive.