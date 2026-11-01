# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step30_weighted_moser_and_family_repair.md",
    "Sessions/S0910A01/workspace/scripts/step30_weighted_moser_family_repair.py",
    "Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md"
  ]
}
```

## Task

Verify the Step 30 repair of the four-dimensional negative Ishida--LeBrun selected-support route. Focus on four concrete issues, not the old dependency diagram: (1) whether the mixed Hölder--Sobolev estimate H_{3p/2} <= H_p^{1/2} ||z_p||_4^2 correctly repairs the half-power gap in the weighted Moser hierarchy with z_p=a^{(p-1)/2} f^{p/2}, including time cutoffs and polynomial p-losses; (2) whether ordinary unweighted Moser on U=a(Rm+G) is indeed unjustified as a first bound because the operator remains a Delta and the quadratic term becomes U*U, while U remains useful for continuation; (3) whether the Ishida--LeBrun family bookkeeping should use an O(A) Euler bound plus Vol/A lower bound rather than chi(M)=A+O(1) or K0->9, and whether sigma_i/A_i->0 (not exact sigma=0) is the full analytic regime; (4) whether the macro-disjoint support/plateau/eigenline zero-extension refinements are the right hypotheses for the terminal pullback chain. Please identify any remaining hidden mathematical gaps precisely.

## Output

# Scientific verification memo

## Overall assessment

The Step 30 corrections are mathematically sound at the algebraic and structural level:

1. The mixed estimate
   \[
   H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2
   \]
   does repair the half-power mismatch, provided the energy cutoffs are arranged exactly as stated.
2. Replacing the first weighted estimate by ordinary Moser iteration on \(U=a(\operatorname{Rm}+G)\) is not supported: the diffusion remains \(a\Delta\), and the quadratic reaction is \(U*U\).
3. The family argument needs only \(\chi(M)=O(A)\), two-sided control of \(\operatorname{Vol}/A\), and \(\sigma/A\to0\). Neither \(\chi(M)=A+O(1)\) nor \(K_0\to9\) follows from the displayed formulas.
4. Macro-disjoint buffers, an inner center set with a uniform terminal geodesic margin, and zero extension of locally estimated densities are the correct geometric inputs for pullback averaging.

These repairs do not yet yield the selected-support flow theorem. The unresolved content is concentrated in the tensor power inequalities, the \(q=3\) positive-time estimate, \(J_6\) and global \(Q\) propagation, the weighted endpoint extraction, the support-selection theorem, and the terminal gauge-density estimates.

---

## 1. Mixed Hölder–Sobolev repair

Let \(\kappa=3/2\), and suppose \(\eta\equiv1\) wherever \(a\ne0\). Then, omitting factors equal to one on this active region,

\[
H_{\kappa p}
 =\int a^{3p/2-2}f^{3p/2}.
\]

With
\[
z_p=\eta a^{(p-1)/2}f^{p/2},
\]
one has
\[
(a^{p-2}f^p)^{1/2}z_p^2
 =a^{(p-2)/2+p-1}f^{3p/2}
 =a^{3p/2-2}f^{3p/2}.
\]
Therefore Cauchy–Schwarz gives
\[
H_{3p/2}
\le
\left(\int a^{p-2}f^p\right)^{1/2}
\left(\int z_p^4\right)^{1/2}
=H_p^{1/2}\|z_p\|_4^2.
\]

This is the exact exponent identity recorded by the verification script. It genuinely removes the previous mismatch. By contrast,
\[
z_p^3=a^{3(p-1)/2}f^{3p/2}
      =a^{1/2}\,a^{3p/2-2}f^{3p/2}.
\]
Since \(0\le a\le1\), this only gives \(\int z_p^3\le H_{3p/2}\), which is the unusable direction.

### Cutoff precision

The displayed Cauchy–Schwarz estimate uses \(H_p\), rather than an unweighted integral \(\int a^{p-2}f^p\), only because \(\eta=1\) throughout the region where \(a\ne0\). If that separation is weakened, the formula is no longer immediate: the first Cauchy factor lacks \(\eta\). An equivalent nested formulation is possible, with the next energy supported where the preceding cutoff equals one, but the nesting must be explicit.

The gradient estimate is also consistent:
\[
\begin{aligned}
|\nabla z_p|^2
&\le Cp^2 a^{p-1}f^{p-2}|\nabla f|^2
 +Cp^2a^{p-3}f^p|\nabla a|^2\\
&\le Cp^2D_p+Cp^2r^{-2}H_p,
\end{aligned}
\]
because
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2}.
\]
The \(\nabla\eta\) contribution vanishes under the stationary-collar arrangement.

For the real exponents \(p_k=p_0(3/2)^k\), powers of \(a\) need a weak-chain-rule justification at \(a=0\). Since \(p_k\ge3\) and \(a=\chi^2\), the displayed gradients are locally integrable and the quotient \(|\nabla a|^2/a\) extends continuously. A regularization \(a+\varepsilon\), followed by \(\varepsilon\downarrow0\), would make this part fully explicit.

### Time recurrence

Write
\[
M_{p,k}=\int_{\tau_k}^tH_p(s)\,ds.
\]
The time-cutoff energy estimate must have the form
\[
\sup_{[\tau_{k+1},t]}H_p+
\int_{\tau_{k+1}}^t(D_p+r^{-2}H_p)
\le L_kM_{p,k},
\]
where, on \(t/2\le s\le t\),
\[
L_k\le Cp_k^N4^k
\left(t^{-1}+r^{-2}+\frac{\beta^3}{t}\right).
\]
Under the small fixed bound on \(\beta\), its final term is absorbed into the constant multiplying \(t^{-1}\).

Integrating the repaired bridge then gives
\[
M_{\kappa p,k+1}
\le Cp^NS
\left(L_kM_{p,k}\right)^{3/2}.
\]
Since \(\kappa=3/2\),
\[
M_{\kappa p,k+1}^{1/(\kappa p)}
\le (Cp^NS)^{1/(\kappa p)}
L_k^{1/p}M_{p,k}^{1/p}.
\]
Thus
\[
\sum_k\frac{\log p_k}{p_k}<\infty,
\qquad
\sum_k\frac{k}{p_k}<\infty
\]
is exactly what is needed. The powers are
\[
\sum_k\frac1{p_k}=\frac3{p_0},
\qquad
\sum_k\frac1{\kappa p_k}=\frac2{p_0}.
\]

Consequently the formal endpoint is
\[
\|af(t)\|_\infty
\le
CS^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(s)\,ds\right)^{1/p_0},
\]
for \(t\le cr^2\). This gives:

- \(p_0=3\), \(\int_{t/2}^tY\le C\beta^3/S^2\):
  \[
  \|aF(t)\|_\infty\le C\beta/t;
  \]
- \(p_0=6\), \(\int_{t/2}^tJ_6\le C\delta^6Vt\):
  \[
  \|aE(t)\|_\infty
  \le C\delta r^{2/3}t^{-1/3}.
  \]

One endpoint detail is absent from Step 30: after bounding the spacetime quantities \(M_{p_k,k}\), the final time-slice estimate should use
\[
H_{p_k}(t)\le L_kM_{p_k,k}.
\]
Taking \(p_k\to\infty\) then yields the spatial essential supremum at the fixed time \(t\). Relying only on shrinking spacetime intervals whose intersection is the single time \(t\) would not by itself provide that conclusion.

The Python script verifies the exponent identities and convergence of the model product. It does not verify the tensor evolution inequality, cutoff integration by parts, moving measure, or treatment of source terms.

---

## 2. Shifted curvature \(U\)

Let
\[
T=\operatorname{Rm}+G,\qquad U=aT.
\]
From the supplied continuation calculation,
\[
(\partial_t-a\Delta)T
=a(T*T+G*T)+(\nabla a)*\nabla T+(\nabla^2a)*T.
\]
Multiplying by \(a\) gives
\[
a^2T*T=(aT)*(aT)=U*U,
\]
while
\[
a^2G*T=aG*U.
\]
Rewriting \(a\Delta(aT)\) introduces first- and zeroth-order cutoff terms, but it does not change the principal operator from \(a\Delta\).

Hence testing the \(U\)-equation against \(|U|^{p-2}U\) yields dissipation of the form
\[
\int a\,\bigl|\nabla |U|^{p/2}\bigr|^2,
\]
not
\[
\int\bigl|\nabla |U|^{p/2}\bigr|^2.
\]
The ordinary Sobolev inequality used in an unweighted parabolic Moser iteration therefore cannot be applied from this estimate alone. Moreover, \(U*U\) has no additional factor of \(a\) to soften the reaction near the zero set of the cutoff.

The same observation applies to Step 29’s ordinary Moser paragraph for \(aE\): its equation also has principal part \(a\Delta\). Step 30’s common weighted hierarchy for curvature and defect is the consistent replacement.

The continuation use of \(U\) remains valid and scientifically important:
\[
\operatorname{Ric}(U)=aE,\qquad
\partial_tg=-2\operatorname{Ric}(U),\qquad
\partial_t\Gamma=\nabla U
\]
schematically. Once \(\sup|a\operatorname{Rm}|\) has been obtained, \(\sup|U|\) follows, and the shifted-curvature derivative induction can organize all connection and cutoff derivatives. The continuation document correctly uses an unweighted \(L^p\) estimate for \(T\) only after \(\sup|U|\) is known; it does not use ordinary Moser to create that first pointwise estimate.

One textual correction remains necessary in Step 29: its displayed \(U\)-equation contains \(a(U*U+G*U)\). The quadratic term should be \(U*U\), while the linear normalized term has the form \(aG*U\), modulo universal contractions and cutoff commutators.

---

## 3. Family and volume bookkeeping

The connected-sum identity is correct:
\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}-\sigma.
\]

Under the actual inputs \(m=2,3\), minimal general-type \(X_j\), and \(b_+(N)=0\), Noether gives
\[
c_2(X_j)\le5c_1^2(X_j)+36.
\]
Also,
\[
\chi(N)=\frac A3+\sigma+6-4m-6b_1(N)
\le\frac A3+\sigma+6-4m.
\]
Thus
\[
\chi(M)
\le5A+36m+\frac A3+\sigma+6-4m-2m
=\frac{16}{3}A+\sigma+30m+6.
\]
At \(\sigma=0\), the numerical ratios \(65/6\) and \(28/3\) in Step 30 follow from \(A\ge12(m-1)\).

This is an \(O(A)\) estimate when \(\sigma/A\to0\). It does not imply \(\chi(M)=A+O(1)\).

### Two-sided volume control

The lower estimate for \(\operatorname{Vol}/A\) uses the scalar monopole inequality together with \(|s|\le4(1+\delta)\):
\[
32\pi^2A\le\int s^2
\le16(1+\delta)^2\operatorname{Vol},
\]
hence
\[
\frac{\operatorname{Vol}}A
\ge\frac{2\pi^2}{(1+\delta)^2}.
\]

For the upper estimate, Chern–Weil gives
\[
\int\left(2|W^+|^2+\frac{s^2}{24}\right)
=
4\pi^2\left(\frac{2A}{3}-\sigma\right)
+\frac12\int|\operatorname{Ric}^{\circ}|^2.
\]
Since
\[
|s|\ge4(1-\delta),\qquad
|\operatorname{Ric}^{\circ}|^2\le4\delta^2,
\]
one obtains
\[
\bigl(1-2\delta-2\delta^2\bigr)\operatorname{Vol}
\le4\pi^2A.
\]
This reproduces the denominator used by the script and supplies a uniform upper estimate for small \(\delta\).

The Chern–Gauss–Bonnet decomposition then yields, for any fixed tensor-norm convention,
\[
\int|\operatorname{Rm}|^2
\le C_1\chi(M)+C_2\operatorname{Vol}
     +C_3\delta^2\operatorname{Vol}.
\]
Combining the Euler estimate with the lower volume estimate gives
\[
K_0=\operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2\le C.
\]
No displayed identity determines a limit \(K_0\to9\); the Weyl contribution and the possible variation of \(\chi(M)/A\) prevent such a numerical conclusion.

### The parameter \(\sigma\)

The mixed monopole/Chern–Weil relation gives
\[
R=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2\ge\sigma.
\]
Therefore
\[
\sigma
\le\frac{\delta^2}{2\pi^2}\operatorname{Vol},
\qquad
\frac{\sigma}{A}\le C\delta^2.
\]
Every sequence with \(\delta_i\to0\) consequently satisfies
\[
\sigma_i/A_i\to0,
\]
even when every \(\sigma_i\) is strictly positive. Exact equality \(\sigma=0\) is only one subfamily. This correction is essential because a fixed positive \(\sigma\) with \(A\to\infty\) already has \(\sigma/A\to0\).

---

## 4. Macro-disjoint supports and terminal pullback

The support geometry proposed in Step 30 matches what the terminal argument actually uses. A precise arrangement is

\[
P_j\Subset\{a_j=1\}
\Subset \text{curvature plateau}_j
\Subset \text{stationary buffer}_j,
\]
with the outer buffers pairwise disjoint.

The graph edge rule \(d(x_i,x_j)\le12r\) ensures that a retained color class has disjoint \(6r\)-buffers. Bounded degree follows from the initial Ricci lower estimate and relative Bishop–Gromov packing at fixed radius ratios, even in collapsed regions.

To obtain a fixed volume fraction, coloring must be weighted by disjointly assigned center cells, such as Voronoi pieces contained in \(B_r(x_j)\). Merely selecting the color with the largest number of centers does not control retained volume when ball volumes vary. With weighted cells, one gets
\[
\operatorname{Vol}(P)\ge\theta\operatorname{Vol}(M)
\ge\theta v_-A.
\]

The terminal geodesic condition also needs a quantitative margin. If \(p\in P_j\subset B_r(x_j)\), the active plateau contains \(B_{4r}(x_j)\), and
\[
e^{-\zeta}g_0\le g(T)\le e^\zeta g_0,
\]
then choosing \(\rho\) with
\[
r+e^{\zeta/2}\rho<4r
\]
ensures every terminal \(g(T)\)-geodesic of length at most \(\rho\) from \(p\) remains in the bounded-curvature plateau. A further restriction
\[
K\rho^2<\pi^2/4
\]
gives the conjugate-radius and Rauch estimates needed on the tangent-space ball.

Zero extension is appropriate for the eigenform density. If
\[
2\langle\mathscr AH,H\rangle
\]
has been estimated only on the bounded-curvature buffers, it can be set to zero elsewhere before the global pullback averaging formula is applied. This does not affect any selected tangent ball because those balls lie entirely inside the buffers. The extended object is only required to be measurable and pointwise \(\ge0\).

Here \(\mathscr A=W^++\sqrt{2/3}|W^+|I\) is more accurately described as a positive-semidefinite shifted Weyl endomorphism, not as a projector. At equality its kernel is the lowest Weyl eigenspace; that is the property used later.

There is also a normalization inconsistency in the supplied terminal density lemma. Its derivation gives
\[
A_\rho\mathfrak D(p)\le C\,\frac QA,
\]
because \(\operatorname{Vol}(P)\ge\alpha A\). Its statement instead introduces \(Q/(8\pi^2)\le\varepsilon\). The familywise vanishing quantity is \(Q/A\), and the terminal result should be stated directly in those terms.

Likewise, replacing the regularization parameter \(\varepsilon_Q=Q\) by a mean quantity such as \(Q/\operatorname{Vol}\) is structurally appropriate: \(Q=o(A)\) does not imply \(Q\to0\), while
\[
Q/\operatorname{Vol}\to0
\]
does follow from the lower volume estimate. The positive-weight monopole calculation still needs to display how its smoothing errors depend on this parameter; the supplied terminal note only states the resulting estimates.

---

## Remaining mathematical gaps

1. **All-\(p\) tensor inequality.**  
   The route needs an index-level derivation of
   \[
   H_p'+cp^{-m}D_p
   \le Cp^N(r^{-2}+S^2Y)H_p
   \]
   for both \(F\) and regularized \(|E|\), including moving norms, moving volume, Lichnerowicz terms, all \(\nabla^2a\) integrations, and real cutoff powers.

2. **Positive-time cubic estimate.**  
   The formula
   \[
   S^2Y(t)\le C\beta^3/t
   \]
   remains schematic. It must hold on exactly the same buffer and evolving Sobolev structure used in the higher-power iteration.

3. **Defect propagation.**  
   Uniform \(J_6\) persistence and the unweighted global estimate
   \[
   Q(T)/A\to0
   \]
   require complete transition-term calculations. A \(C/t\) curvature coefficient cannot simply be integrated from time zero.

4. **Endpoint and source handling.**  
   The time-slice extraction described above, additive source terms, Kato regularization, and passage through real exponents are not contained in the script.

5. **Flow existence and continuation.**  
   The shifted-curvature document provides the correct derivative structure, but the grouped Wang integration-by-parts step is still imported schematically. Degenerate short-time existence through strictly parabolic approximants is also referenced rather than reproduced.

6. **Weighted support selection.**  
   The bounded-degree coloring, Voronoi weighting, preservation of a fixed \(A\)-proportional center-set volume, and terminal geodesic containment have not yet been assembled into a proved geometric lemma.

7. **Terminal gauge density.**  
   The estimates for harmonic amplitude and
   \(\int\langle\mathscr AH,H\rangle\) are cited from the positive-weight monopole construction. Their uniform dependence on \(K\), the family-scaled regularization, and local elliptic compactness of \(H_i\) are not derived in the supplied Step 30 materials.

Thus Step 30 successfully repairs the identified algebraic and topological defects and gives a coherent route for the Ricci-near-\(-g\) Ishida–LeBrun family. The decisive theorem-level work remains in the tensor PDE estimates, geometric support lemma, and terminal gauge-density bridge.