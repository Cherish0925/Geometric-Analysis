# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the newly completed rigorous enclosure and O11 consequence after the earlier review. Read the regularized acb script, its symbolic Ricci checker, the 256-bit replication output, the session synthesis, and the inherited variational formulas. Focus on the load-bearing issues: correctness of the bolt-regular Ricci rewrite and volume normalization; compliance with acb.integral's holomorphy callback contract including piecewise phi evaluation; whether the coefficient vector defines a legitimate exact witness despite originating as binary64; passage from C2 CH matching to smooth exact-collar metrics without losing strict inequality; residual-finite replication; and the constant limsup alpha/h <= 28/9+J1/(9pi^2)=4-(8/9)epsilon. State whether this is now a proved strict upper coefficient below 4, and identify any remaining mathematical flaw that would overturn it. Do not revisit unrelated session routes.

## Integrated Scientific Memo

## Verification verdict

Yes—subject to one implementation-level rigor issue described below, the supplied construction proves a strict upper coefficient below \(4\) for an **existentially chosen balanced family**:
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le \frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac89\varepsilon_0<4,
\]
where the certified cell enclosure is
\[
\frac{J_1}{8\pi^2}
=\frac{J_6}{8\pi^2}
=0.999116243135324311\ldots<1,
\]
so one may take
\[
\varepsilon_0>0.0008837568646756,
\qquad
4-\frac89\varepsilon_0
<3.999214438342511.
\]

Thus the coefficient-four conjecture is disproved for this balanced sequence. This does not determine the sharp coefficient and does not apply automatically to every preassigned cover sequence.

## 1. Ricci rewrite and normalization

Write
\[
dt=\frac{dx}{2\sqrt G},\qquad
h_1=F,\quad h_2=x,\quad h_3=xe^w,\quad a_i=\sqrt{h_i}.
\]
Then
\[
\frac{\ddot a_i}{a_i}
=\frac{G'h_i'}{h_i}
+\frac{2Gh_i''}{h_i}
-\frac{G(h_i')^2}{h_i^2},
\qquad
\frac{\dot a_i}{a_i}\frac{\dot a_j}{a_j}
=\frac{Gh_i'h_j'}{h_ih_j}.
\]
For \(F=y\widehat F\), \(G=y\widehat G\), \(y=x-x_0\), this gives exactly
\[
D_1
=2\frac{\widehat G}{\widehat F}F''
+F'\frac{\widehat G'\widehat F-\widehat G\widehat F'}
{\widehat F^2},
\]
as well as the coded
\[
D_2=\frac{G'}x-\frac G{x^2}
\]
and the corresponding \(D_3,L_{12},L_{13},L_{23}\).

The diagonal Bianchi-IX formula
\[
R_{00}=-(D_1+D_2+D_3),
\]
\[
R_{ii}=-D_i-L_i(L_j+L_k)
+2\frac{a_i^4-(a_j^2-a_k^2)^2}
{a_i^2a_j^2a_k^2}
\]
has the correct normalization for
\(d\sigma_1=2\sigma_2\wedge\sigma_3\) cyclically. The symbolic checker compares it with the independent Cartan computation and reports zero residuals for all four Ricci components and for the \(D_1,A_1,A_2,A_3\) regularizations.

The apparent bolt poles are genuinely removed:
\[
w=y^2\widehat w,\qquad e^w-1=w\phi(w),\qquad
\sinh w=w\,\operatorname{shc}(w),
\]
hence
\[
\frac{(e^w-1)^2}{F}
=\frac{y^3\widehat w^{\,2}\phi(w)^2}{\widehat F},
\qquad
\frac{\sinh w}{F}
=\frac{y\widehat w\,\operatorname{shc}(w)}{\widehat F}.
\]
No division by \(y\) remains.

The shift of \(c_{G,0}\) is part of the exact witness and enforces
\[
q_F(0)+q_G(0)=0,\qquad F'(x_0)G'(x_0)=1.
\]
Together with \(w=O(y^2)\), this gives the regular bolt expansion
\(a_1=t+O(t^3)\) and \(h_3-h_2=O(t^4)\).

For the orbit convention
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
one obtains
\[
\frac{dV}{8\pi^2}
=\frac18\,x e^{w/2}\sqrt{\frac FG}\,dx
=\frac18\,x e^{w/2}
\sqrt{\frac{\widehat F}{\widehat G}}\,
\ell x\,du,
\]
which is exactly the coded density. Thus there is no missing orbit, radial, or \(8\pi^2\) factor.

The independent decomposition also checks:
\[
\frac{P}{8\pi^2}
+\frac1{32\pi^2}\int(s+24)^2
=
0.999108702733592648
+0.000007540401731663
=
0.999116243135324311.
\]

## 2. `acb.integral` callback and piecewise \(\phi\)

The callback has the required signature and propagates `analytic=True` to the non-entire branch-sensitive operations:

- `log(1+x, analytic=True)`;
- \(\sqrt{\widehat F/\widehat G}\) with `analytic=True`.

All remaining basic operations are entire or ball divisions, and a denominator ball meeting zero produces a non-finite enclosure rather than a false analytic value. Real positivity of \(F,G\), together with compactness, provides a complex neighborhood of the interval on which the needed branches exist; adaptive subdivision verifies these locally.

The two implementations of
\[
\phi(z)=\frac{e^z-1}{z}
\]
represent the same entire function:

- for large balls, quotient formulas for \(\phi,\phi',\phi''\);
- near zero, Taylor series with a common rigorous remainder bound.

The derivative-series coefficients are all bounded by \(1/k!\), so
\[
\sum_{k=N}^\infty \frac{r^k}{k!}
\le
\frac{r^N/N!}{1-r/(N+1)}
\qquad (r\le1)
\]
does enclose all three tails. The implementation switch therefore does not define a discontinuous mathematical integrand.

### One rigor caveat

The Taylor-radius bound is constructed through binary64:
```python
r = (float(m.mid()) + float(m.rad()))*(1 + 2**-30) + 1e-300
```
The \(2^{-30}\) inflation overwhelmingly dominates ordinary binary64 rounding for the finite, moderate values occurring in this computation, so there is no realistic numerical threat to the reported enclosure. Nevertheless, as written, this relies on the conversion/rounding semantics of `float(...)` rather than deriving the upper bound wholly inside Arb.

For a completely implementation-independent certificate, replace this with a pure-Arb upper endpoint for \(|z|\). That is the only visible load-bearing certification issue. It does not indicate that the inequality is false; it is a small formal weakness in how the Taylor remainder radius is obtained.

The 160-, 256-, and 320-bit outputs all remain strictly below one. At 256 bits,
\[
\frac{J_6}{8\pi^2}
\in
[0.999116243135324311\pm2.25\times10^{-19}],
\]
with deficit approximately \(8.84\times10^{-4}\), so the conclusion is far from the enclosure boundary. The Arb ball, not the JSON Boolean after conversion to a Python float, is the certificate.

## 3. Exact witness despite binary64 origin

Parsing a decimal through Python `float` and then passing it to `arb` freezes a specific binary64 value. Such a value is an exact dyadic rational. Consequently, the witness is not “an approximation to an unknown optimizer”; it is the explicit metric defined by:

1. the exact binary64 dyadic coefficients;
2. the algebraically shifted \(c_{G,0}\);
3. \(x_0=1/100\);
4. \(X=8\).

At the stated precisions, each 53-bit dyadic coefficient is represented exactly. Its origin in a numerical optimization is irrelevant after freezing it.

For archival clarity, the coefficients should be recorded as hexadecimal floats or dyadic rational pairs, but that does not change the mathematical witness.

## 4. Smooth exact-CH attachment

The profile only matches CH through second \(x\)-jet at \(X\), so direct attachment gives a \(C^2\), not \(C^\infty\), metric. This is repairable without losing the strict inequality.

If \(v=X-x\), every deviation from CH satisfies
\[
\Delta g=O(v^3),\qquad
\nabla\Delta g=O(v^2),\qquad
\nabla^2\Delta g=O(v).
\]
Multiplying the deviation by a smooth cutoff over a collar of width \(\delta\) yields
\[
\Delta g_\delta=O(\delta^3),\qquad
\nabla\Delta g_\delta=O(\delta^2),\qquad
\nabla^2\Delta g_\delta=O(\delta),
\]
so
\[
\Ric(g_\delta)+6g_\delta=O(\delta)
\]
on a region of volume \(O(\delta)\). Therefore
\[
J_6(g_\delta)-J_6(g_0)=O(\delta^3),
\qquad
J_6(g_\delta)\to J_6(g_0).
\]
For sufficiently small fixed \(\delta\), the smoothed exact-collar cell still has \(J_6<8\pi^2\).

If the displayed coefficient is to use the unsmoothed limiting value exactly, choose \(\delta_j\to0\) along the global sequence. If one uses one fixed smoothed cell, the same strict result holds with an arbitrarily slightly smaller certified \(\varepsilon_0\).

## 5. Residual-finite replication

For a fixed buffered radius \(r\), only finitely many nonidentity lattice elements satisfy
\[
d(p,\gamma p)\le2r.
\]
Residual finiteness supplies a finite-index subgroup avoiding this finite set, hence a finite cover \(X_*\) containing the required embedded ball.

Every further finite cover \(X_j\to X_*\) contains
\[
\deg(X_j/X_*)=\frac{A_j}{A_*}
\]
disjoint lifts of that ball. Since
\[
k_j\sim\frac29Q_j
=\frac29h_jA_j=o(A_j),
\]
there are enough lifted balls for all blow-up cells. Thus replication is valid for a balanced sequence built from covers of \(X_*\).

This is existential. It does not imply that every arbitrary previously chosen cover sequence has enough such thick balls.

## 6. Transfer coefficient

The scale change \(\widetilde g=6g\) gives
\[
\int|\Ric_{\widetilde g}+\widetilde g|^2\,dV_{\widetilde g}
=J_6(g)=J_1.
\]
With
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36},
\]
and handle-cell cost \(32\pi^2\), the normalized defect satisfies
\[
\begin{aligned}
\limsup_j\frac{\alpha(M_j)}{h_j}
&\le
\frac29\frac{J_1}{2\pi^2}
+\frac7{36}\frac{32\pi^2}{2\pi^2}\\
&=
\frac{J_1}{9\pi^2}+\frac{28}{9}.
\end{aligned}
\]
Writing
\[
\frac{J_1}{8\pi^2}=1-\varepsilon_0
\]
gives
\[
\frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac89\varepsilon_0.
\]
The certified enclosure yields
\[
\boxed{
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
<3.999214438342511<4.
}
\]

There is also a potentially sharper route using the certified
\[
P/(8\pi^2)=0.999108702733592648\ldots
\]
and the inherited first-order relation \(\alpha_j=4\rho_j+O(h_j^2)\), giving approximately \(3.9992077358\). That refinement is not needed for the requested \(J_1\)-based conclusion and requires careful notation distinguishing the cell energy \(J_6\) from the paper’s normalized functional \(\mathcal J=4P/R\).

## Final assessment

The bolt algebra, volume normalization, exact dyadic witness, \(C^2\)-to-smooth approximation, residual-finite replication, and coefficient calculation are correct. The construction therefore establishes a strict upper coefficient below \(4\) for a suitably chosen balanced family.

The only remaining issue capable of challenging the word “fully rigorous” in the numerical certificate is the binary64 construction of the Taylor remainder radius inside `phi_derivs`; replacing it by a pure-Arb upper bound removes that concern. No supplied evidence suggests any geometric or variational flaw that would overturn the strict inequality. The unresolved mathematics is the sharp cell infimum and matching global lower coefficient, not the existence of this strict upper construction.