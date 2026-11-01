# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md",
    "Sessions/S0910A01/workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md"
  ]
}
```

## Task

Independently verify the mathematical correctness of the consolidated restricted negative Ishida-LeBrun gap theorem proof. Focus on three load-bearing points:

1. **Proposition 3.2 (quantitative local Φ lower bound from compactness).** The proof argues: on Riemannian 4-balls with |Rm| ≤ K and Vol(B_{ρ/2}) ≥ v₀, the density Φ = |E|² + (s+4)² + (s+8√6|W⁺|)² + G has fint Φ ≥ η(K,ρ,v₀) > 0. Otherwise a minimizing sequence converges smoothly (Cheeger-Gromov) to a germ with Φ ≡ 0, which is Einstein with the calibrated W⁺ spectrum, contradicting Derdziński. Is this compactness argument valid? Are the hypotheses sufficient for smooth subsequential convergence on B_{ρ/2}? Does Φ = 0 really force all four calibrated conditions, or could a density vanishing in the mean have a nontrivial limit? Does the passage from mean-zero Φ to pointwise Φ=0 on the limit require strong L¹ convergence (which Cheeger-Gromov does supply) or something else?

2. **Terminal averaging and support-count independence.** The Liouville average integral over P_i^in is claimed to be bounded by C(K,ρ)∫_M Φ without a factor depending on the number of supports. Check whether the Liouville-Rauch double integral over P_i^in can indeed be controlled by a single global integral of Φ over M, given bounded curvature and the fact that different centers' pullback images may overlap in M.

3. **Coefficient regularization order of operations.** The proof constructs regularized flows b_ε = χ² + ε² for each ε > 0, obtains ε-uniform bounds from the geometric energies (NOT from the ε-dependent PDE constants), passes to a smooth limit solving the exact a = χ² equation, and only THEN applies stationary-complement and disjoint-support identities. Check whether the ε-uniform geometric bounds (§5.2 properties) are indeed sufficient for a common existence time and smooth compactness, or whether additional information is needed.

## Output

# Scientific verification memo

## Overall assessment

The local Derdziński mechanism is mathematically viable, but Proposition 3.2 uses a stronger compactness conclusion than its stated hypotheses provide. Its conclusion can be recovered by harmonic-coordinate elliptic compactness using the \(|E|^2\) term in \(\Phi\).

The Liouville–Rauch averaging estimate is valid and carries no factor from the number of supports, provided \(\rho\) is chosen below the curvature comparison scale and every relevant geodesic remains in the bounded-curvature plateau.

The coefficient-regularization order is correct. Smooth compactness follows if the asserted fixed-coordinate, all-order, \(\varepsilon\)-uniform estimates and metric equivalence are actually available. The supplied excerpts establish important tensor structure but do not contain enough of the regularized continuation argument to verify that analytic package independently.

---

## 1. Proposition 3.2

### 1.1 Bounded curvature and noncollapse do not directly give smooth convergence

The sentence

> “By Cheeger–Gromov compactness … a subsequence converges smoothly”

is not justified from only
\[
|\operatorname{Rm}_{g_k}|\le K,\qquad
\operatorname{Vol}_{g_k}(B_{\rho/2})\ge v_0.
\]

These assumptions give, after shrinking to an interior ball and choosing harmonic coordinates,

\[
g_k\to g_\infty \quad\text{in }C^{1,\alpha},
\qquad
g_k\rightharpoonup g_\infty\quad\text{in }W^{2,p},
\]
for finite \(p\), with uniform \(W^{2,p}\) bounds. Smooth Cheeger–Gromov convergence normally requires uniform bounds for all covariant derivatives of curvature.

This distinction matters because weak \(W^{2,p}\) convergence alone does not ensure strong convergence of \(W^+\) or of nonlinear spectral expressions such as \(\mathcal G\). Curvature oscillation could survive weak convergence.

### 1.2 The \(|E|^2\) term supplies the missing elliptic compactness

The proposition can nevertheless be proved. Suppose
\[
\fint_{B_{\rho/2}(p_k)}\Phi_{g_k}\,d\mu_{g_k}\longrightarrow0.
\]
A sectional-curvature bound gives a uniform upper volume bound at fixed radius, so
\[
\int_{B_{\rho/2}(p_k)}\Phi_{g_k}\,d\mu_{g_k}\longrightarrow0.
\]
In particular,
\[
\|E_k\|_{L^2(B_{\rho/2})}\longrightarrow0.
\]
Since \(|\operatorname{Rm}_{g_k}|\le K\), the tensors \(E_k\) are uniformly bounded pointwise. Interpolation then gives
\[
\|E_k\|_{L^p(B_{\rho/2})}\longrightarrow0
\qquad\text{for every finite }p.
\]

The curvature and volume assumptions give a uniform harmonic radius at the center, after replacing \(\rho/2\) by a smaller radius \(r_h=r_h(K,\rho,v_0)>0\). In harmonic coordinates,
\[
g_k^{ab}\partial_a\partial_b(g_k)_{ij}
=
-2\operatorname{Ric}_{ij}(g_k)
+Q_{ij}(g_k^{-1},\partial g_k).
\]
Because
\[
\operatorname{Ric}(g_k)=-g_k+E_k,
\]
the right side converges strongly in \(L^p\), while the coefficients converge in \(C^\alpha\). Interior elliptic estimates therefore give
\[
g_k\longrightarrow g_\infty
\quad\text{strongly in }W^{2,p}_{\mathrm{loc}}
\]
for every finite \(p\). Consequently,
\[
\operatorname{Rm}_{g_k}\longrightarrow\operatorname{Rm}_{g_\infty}
\quad\text{strongly in }L^p_{\mathrm{loc}}.
\]

The limit satisfies
\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\]
weakly and hence smoothly by elliptic regularity in harmonic coordinates. Strong curvature convergence is sufficient to pass the other algebraic components of \(\Phi\) to the limit. Thus every term vanishes almost everywhere, and smoothness promotes the resulting identities to pointwise identities.

So the conclusion of Proposition 3.2 is supportable, but the proof should use this elliptic argument rather than smooth compactness from curvature and volume alone.

### 1.3 Algebraic consequences of \(\Phi=0\)

From \(E=0\),
\[
\operatorname{Ric}=-g,\qquad s=-4.
\]
The third square gives
\[
-4+8\sqrt6\,|W^+|=0,
\]
hence
\[
|W^+|=\frac1{2\sqrt6},
\qquad |W^+|^2=\frac1{24}.
\]

For the definitions in the note,
\[
f=\frac23s-2\sqrt{\frac23}|W^+|=-3,
\qquad
a_*=\frac23s+2w=-\frac83+2w,
\]
where \(w\) is the smallest eigenvalue of \(W^+\). Since \(w\le0\), one has \(a_*<0\). The relation
\[
\mathcal G=f^2-(a_{*,-})^2=0
\]
therefore yields \(a_*=-3\), so
\[
w=-\frac16.
\]
If the other eigenvalues are \(x,y\), trace-freeness and the norm give
\[
x+y=\frac16,\qquad
x^2+y^2=\frac1{72}.
\]
Thus
\[
x=y=\frac1{12}.
\]
Therefore
\[
\operatorname{spec}(W^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

There is no residual branch in this algebra. The convention for \(a_{*,-}\) should nevertheless be stated explicitly in the consolidated proof.

### 1.4 Derdziński contradiction

For an Einstein metric, \(\delta W^+=0\). The spectrum above has two eigenvalues and \(W^+\neq0\), so the quoted Derdziński proposition makes
\[
(24|W^+|^2)^{1/3}g=g
\]
locally Kähler. A Kähler surface with \(s=-4\) has
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
incompatible with \(1/24\). This local contradiction is correct under the quoted Derdziński theorem and the stated curvature conventions.

---

## 2. Terminal Liouville averaging

Let
\[
D_p=\int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi.
\]
Choose \(\rho\) below a fixed comparison scale depending on \(K\), and assume every geodesic segment involved remains in the terminal plateau. Rauch–Günther comparison gives
\[
c(K,\rho)\rho^4\le D_p\le C(K,\rho)\rho^4,
\qquad
0<J_p(t,\xi)\le C(K,\rho)t^3.
\]
Consequently,
\[
A_\rho\Phi(p)
\le
\frac{C}{\rho^4}
\int_{S_pM}\int_0^\rho
t^3\Phi(\gamma_{p,\xi}(t))\,dt\,d\xi.
\]

Integrating over \(P=P_i^{\rm in}\),
\[
\begin{aligned}
\int_P A_\rho\Phi(p)\,d\mu(p)
&\le
\frac{C}{\rho^4}\int_0^\rho t^3
\int_{SM|_P}\Phi(\pi G_t v)\,dL(v)\,dt\\
&\le
\frac{C}{\rho^4}\int_0^\rho t^3
\int_{SM}\Phi(\pi G_t v)\,dL(v)\,dt.
\end{aligned}
\]
Here \(G_t\) is geodesic flow and \(dL\) is Liouville measure. Its invariance gives
\[
\int_{SM}\Phi(\pi G_t v)\,dL(v)
=
|S^3|\int_M\Phi\,d\mu.
\]
Therefore
\[
\int_P A_\rho\Phi\,d\mu
\le C(K,\rho)\int_M\Phi\,d\mu.
\]

No support-count factor appears. Different starting points and directions may reach the same point of \(M\), but they are integrated as elements of \(SM\), and Liouville invariance controls the full aggregate. This remains true even when the exponential map has overlapping images in the base manifold. Positivity of the pullback metric is ensured by choosing \(\rho\) below the conjugate-radius comparison scale.

There is a minor radius normalization to record. Proposition 3.2 gives a lower mean on the pullback \(B_{\rho/2}\), whereas \(A_\rho\) uses radius \(\rho\). Since \(\Phi\ge0\),
\[
\int_{B_\rho}\Phi\ge\int_{B_{\rho/2}}\Phi,
\]
and comparison bounds the two relevant volumes. Hence Proposition 3.2 implies
\[
A_\rho\Phi(p)\ge c(K,\rho,v_0)\eta,
\]
possibly after renaming \(\eta\). The proof should not silently use exactly the same numerical constant.

---

## 3. Coefficient regularization

### 3.1 The order of operations is correct

For
\[
b_\varepsilon=\chi^2+\varepsilon^2,
\qquad
\partial_tg_\varepsilon
=-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon),
\]
the exterior region evolves whenever \(\varepsilon>0\). Thus stationary-complement identities and exact supportwise summation are unavailable at the regularized level.

If a smooth subsequence converges to \(g\), then
\[
b_\varepsilon\to\chi^2
\]
smoothly in fixed coordinates, and passing to the equation gives
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]
Only for this exact equation does \(\partial_tg=0\) where \(\chi=0\). The ordering used in the consolidated note is therefore mathematically appropriate.

Restarting without uniqueness is also viable: for an autonomous smooth equation, all one-sided time derivatives at a joining slice are recursively determined by the terminal metric and \(\chi\). Two smooth pieces with the same terminal datum consequently have matching time jets.

### 3.2 What is sufficient for smooth compactness

For a fixed initial datum, the following \(\varepsilon\)-uniform package on a common interval \([0,\tau]\) is sufficient:

\[
\Lambda^{-1}g_0\le g_\varepsilon(t)\le\Lambda g_0,
\]
together with, in a fixed finite atlas,
\[
\sup_{\varepsilon,t\le\tau}
\|\nabla_0^m g_\varepsilon(t)\|_{L^\infty}<\infty
\quad\text{for every }m,
\]
and corresponding time-derivative bounds. A diagonal Arzelà–Ascoli argument then gives smooth convergence on \(M\times[0,\tau]\).

Finite-\(L^p\) tensor estimates can produce these bounds if they include:

- every derivative order with some \(p>4\);
- uniform Sobolev constants for the evolving metrics;
- uniform control of the connection difference \(\nabla^{g_\varepsilon}-\nabla^{g_0}\);
- conversion of geometric covariant derivatives to fixed-coordinate derivatives;
- bounds for \(\partial_tg_\varepsilon=-2b_\varepsilon E_\varepsilon\) and its differentiated equations.

The metric-equivalence estimate follows from a weighted curvature bound because contraction of
\[
U_\varepsilon=b_\varepsilon
\left(\operatorname{Rm}+\frac{g\owedge g}{2(n-1)}\right)
\]
controls \(b_\varepsilon E_\varepsilon\). Thus
\[
|\partial_tg_\varepsilon|
\le C\bigl(|U_\varepsilon|+b_\varepsilon\bigr).
\]

### 3.3 Weighted curvature alone is insufficient near \(\chi=0\)

Where \(\chi=0\),
\[
b_\varepsilon=\varepsilon^2,
\]
so a bound on \(U_\varepsilon=b_\varepsilon T_\varepsilon\) alone permits
\[
|T_\varepsilon|\sim\varepsilon^{-2}.
\]
Smooth compactness therefore requires the unweighted \(T\)-estimates and their higher-order analogues, not only the weighted \(U_m\) estimates. The notes identify a zero-order unweighted seed and a staggered \(U_m,T_m,C_{m+1}\) scheme, which is the correct structure.

The tensor ledger in Step 43 verifies one essential part: every highest cutoff jet \(C_{m+2}\) carries a factor \(\chi\), allowing absorption against
\[
\int b_\varepsilon|\nabla U_m|^2|U_m|^{p-2}.
\]
It does not by itself establish all fixed-coordinate estimates needed above.

### 3.4 Common existence time is not independently established in the excerpts

Section 5.2 states that the staggered energies, first-exit improvement, and connection-difference estimates yield a common time and all-order fixed-coordinate bounds. The displayed material does not contain the complete continuation derivation linking those ingredients.

In particular, the regularized construction needs estimates valid before the exact stationary-complement identities are available. A logically clean decomposition is:

1. A per-input, \(\varepsilon\)-uniform short-time argument using only the regularized equation, retaining every \(\varepsilon^2\) exterior term.
2. Smooth extraction of an exact \(\chi^2\)-flow on that short interval.
3. First-exit and global \(Q\) estimates on the exact flow.
4. All-order continuation or smooth restart while the weighted curvature remains bounded.

If first-exit estimates that use a frozen exterior are invoked before Step 2, the reasoning becomes circular. The supplied notes say the frozen-exterior identities begin only after the limit, which is correct, but the separate regularized short-time estimate is not displayed in enough detail to reproduce.

---

## Final scientific status

- **Local \(\Phi\) lower bound:** its conclusion is supportable, but the printed smooth-compactness proof must be replaced by the harmonic-coordinate \(E_k\to0\) elliptic argument above.
- **Terminal averaging:** mathematically sound, independent of support count, with a small-radius assumption and a harmless renaming of the local constant.
- **Coefficient regularization:** the order of operations is correct. Smooth extraction is valid if the asserted all-order fixed-coordinate estimates hold. Those estimates and the common-time continuation are not fully demonstrated in the supplied files.

Thus the Derdziński and averaging parts can be made rigorous, while the regularized-flow existence and continuation module remains the principal unresolved analytic component for an independently reproducible proof of the family-uniform Ricci-\((-g)\) gap.