# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/perp_rigorous_enclosure.py",
    "Sessions/S1003A01/workspace/scripts/check_bianchi_ricci_closed_form.py",
    "Sessions/S1003A02/workspace/data/o11_peer_rigorous_replication_256.json",
    "Sessions/S1003A02/workspace/data/o11_peer_rigorous_replication_160.json",
    "Sessions/S1003A02/workspace/data/o11_peer_rigorous_replication_320.json",
    "Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex",
    "Skills/geometric-analysis/research/paper/sections/field_interfaces_and_curvature_interactions.tex"
  ]
}
```

## Task

Verify the newly completed rigorous enclosure and O11 consequence after the earlier review. Read the regularized acb script, its symbolic Ricci checker, the 256-bit replication output, the session synthesis, and the inherited variational formulas. Focus on the load-bearing issues: correctness of the bolt-regular Ricci rewrite and volume normalization; compliance with acb.integral's holomorphy callback contract including piecewise phi evaluation; whether the coefficient vector defines a legitimate exact witness despite originating as binary64; passage from C2 CH matching to smooth exact-collar metrics without losing strict inequality; residual-finite replication; and the constant limsup alpha/h <= 28/9+J1/(9pi^2)=4-(8/9)epsilon. State whether this is now a proved strict upper coefficient below 4, and identify any remaining mathematical flaw that would overturn it. Do not revisit unrelated session routes.

## Output

## Scientific verification memo

### 1. Conclusion

The supplied script, symbolic comparison, Arb output, smoothing argument, and variational transfer establish a strict first-order upper coefficient below \(4\) for a suitably selected balanced sequence:
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le \frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac89\varepsilon_0
<3.999214438342511<4,
\]
where
\[
\frac{J_1}{8\pi^2}
=\frac{J_6}{8\pi^2}
<0.9991162431353244,
\qquad
\varepsilon_0>0.0008837568646756.
\]

Thus the universal coefficient-four statement is disproved. The result concerns an existential balanced cover sequence equipped with replicated finite-scale cells; it does not determine the optimal coefficient or assert the same value for every preassigned sequence.

No mathematical flaw that would overturn this strict inequality is visible in the supplied materials. The full numerical value using the unsmoothed \(C^2\) cell requires a diagonal smooth approximation, explained in §5 below; that construction is available.

---

### 2. Bolt-regular Ricci formulas and normalization

Put
\[
dt=\frac{dx}{2\sqrt G},\qquad
h_1=F,\quad h_2=x,\quad h_3=xe^w,\qquad a_i=\sqrt{h_i}.
\]
For any \(h_i\),
\[
D_i:=\frac{\ddot a_i}{a_i}
=\frac{G'h_i'}{h_i}
 +\frac{2Gh_i''}{h_i}
 -\frac{G(h_i')^2}{h_i^2},
\]
while
\[
\frac{\dot a_i}{a_i}\frac{\dot a_j}{a_j}
=\frac{G h_i'h_j'}{h_i h_j}.
\]
With \(y=x-x_0\), \(F=y\widehat F\), and \(G=y\widehat G\), direct cancellation gives
\[
D_1
=2\frac{\widehat G}{\widehat F}F''
 +F'\frac{\widehat G'\widehat F-\widehat G\widehat F'}
              {\widehat F^2},
\]
which is exactly the expression used in `perp_rigorous_enclosure.py`. Likewise,
\[
D_2=\frac{G'}x-\frac{G}{x^2},
\]
and the coded expression for \(D_3\) is the general formula above with \(h_3=xe^w\). The three mixed logarithmic-derivative products in the script are also exactly
\[
L_iL_j=\frac{G h_i'h_j'}{h_i h_j}.
\]

For \(d\sigma_1=2\sigma_2\wedge\sigma_3\) cyclically, the standard diagonal Bianchi IX formula is
\[
R_{00}=-(D_1+D_2+D_3),
\]
\[
R_{ii}
=-D_i-L_i(L_j+L_k)
 +2\frac{a_i^4-(a_j^2-a_k^2)^2}
          {a_i^2a_j^2a_k^2}.
\]
It has the correct normalization: for \(a_1=a_2=a_3=a\) constant, the orbit Ricci tensor is \(2a^{-2}g\), as for the unit round three-sphere in this convention. The symbolic script compares all four components with the independent Cartan computation and reports zero residuals.

The potentially singular algebraic terms are removed correctly. Since
\[
w=y^2\widehat w,\qquad e^w-1=w\phi(w),\qquad
\sinh w=w\,\operatorname{shc}(w),
\]
one has
\[
\frac{(e^w-1)^2}{F}
=\frac{y^3\widehat w^{\,2}\phi(w)^2}{\widehat F},
\qquad
\frac{\sinh w}{F}
=\frac{y\widehat w\,\operatorname{shc}(w)}{\widehat F}.
\]
These are precisely the factors in `A1`, `A2`, and `A3`. No division by \(y\) survives at \(u=0\). The symbolic comparison separately returns zero for the \(D_1,A_1,A_2,A_3\) rewrites.

At the bolt,
\[
\widehat F(0)=e^{q_F(0)},\qquad
\widehat G(0)=e^{q_G(0)}.
\]
The coefficient shift imposes \(q_F(0)+q_G(0)=0\), so \(F'(x_0)G'(x_0)=1\). In radial distance \(t\), this gives
\[
y=G'(x_0)t^2+O(t^4),\qquad a_1=t+O(t^3).
\]
Moreover \(w=O(y^2)=O(t^4)\), so the two tangential coefficients agree to the required order. This is the regular bolt expansion, not merely a finite-value curvature evaluation.

For the volume, the normalization
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2
\]
gives
\[
\frac{dV}{8\pi^2}
=\frac18\,x e^{w/2}\sqrt{\frac FG}\,dx
=\frac18\,x e^{w/2}
 \sqrt{\frac{\widehat F}{\widehat G}}\,
 \ell x\,du.
\]
This agrees exactly with the coded `vol`. Hence
\[
\frac{J_6}{8\pi^2}
=\int_0^1 \mathrm{vol}(u)
 \sum_{\alpha=0}^3(R_{\alpha\alpha}+6)^2\,du
\]
has no missing orbit, radial, or \(8\pi^2\) factor.

The separate outputs also satisfy
\[
0.999108702733592648
+0.000007540401731663
=0.999116243135324311,
\]
as required by
\[
|\Ric+6g|^2
=|\Ric^\circ|^2+\frac14(s+24)^2.
\]

---

### 3. `acb.integral` and holomorphic evaluation

The callback supplies a holomorphic extension of the real integrand:

* polynomial and exponential operations are entire;
* `log(1+x)` receives `analytic=analytic`;
* the final square root \(\sqrt{\widehat F/\widehat G}\) receives the same flag;
* divisions return indeterminate balls whenever a denominator cannot be separated from zero.

On the real interval, \(F,G>0\) analytically:
\[
F=y e^{q_F}+x_0S(u)>0,
\qquad
G=\bigl(y+(x^2+x_0)S(u)\bigr)e^{q_G}>0.
\]
Thus \(\widehat F/\widehat G>0\), and compactness supplies a complex neighborhood on which the required logarithm and square-root branches exist. Adaptive subdivision allows Arb to certify these branches locally.

The piecewise evaluation of
\[
\phi(z)=\frac{e^z-1}{z}
\]
is compatible with the callback contract. For \(r\le1\), the code uses
\[
\phi(z)=\sum_{k\ge0}\frac{z^k}{(k+1)!}
\]
and the analogous series for its first two derivatives. For all three series, the omitted coefficient at index \(k\) is at most \(1/k!\), so
\[
\sum_{k=N}^\infty \frac{r^k}{k!}
\le
\frac{r^N/N!}{1-r/(N+1)}
\]
is valid. Adding this disk to both real and imaginary components encloses the complex remainder.

For \(r>1\), the direct quotient formulas represent the same entire functions away from \(z=0\). If an input ball in this branch also contains \(0\), division by \(z\) returns an indeterminate result; the integrator then subdivides rather than receiving a false analyticity certificate. Near \(z=0\), sufficiently small balls enter the power-series branch. The implementation switch therefore does not introduce a piecewise mathematical integrand.

The only ordinary floating-point operation inside the enclosure core is the construction
\[
r=(\operatorname{float}(\operatorname{mid}|z|)
 +\operatorname{float}(\operatorname{rad}|z|))(1+2^{-30})+10^{-300}.
\]
For the finite values arising in this run, standard correctly rounded binary64 conversion has relative error of order \(2^{-53}\); the \(2^{-30}\) inflation exceeds this by more than seven orders of magnitude. Values below \(10^{-300}\) are covered by the additive term. Thus the radius used in the Taylor remainder is outward for these calls. Replacing this line by a purely Arb upper endpoint would make the artifact independent of this binary64 fact, but the present computation is not numerically close to violating it.

The 160-, 256-, and 320-bit runs agree. At 256 bits,
\[
\frac{J_6}{8\pi^2}
\in [0.999116243135324311\pm2.25\times10^{-19}],
\]
which lies below \(1\) by roughly \(8.84\times10^{-4}\), vastly more than the enclosure radius. The Arb ball itself, rather than the JSON Boolean obtained after conversion to a Python float, carries the proof.

---

### 4. Exact status of the coefficient vector

The JSON numbers are parsed as Python binary64 values and then passed to `arb`. Each selected binary64 value is an exact dyadic rational. At 160 bits and above, the original 53-bit values and the finite coefficient sums are represented exactly; the exponential and logarithmic evaluations are then enclosed by Arb.

The witness is therefore the metric defined by these exact dyadic coefficients, not an interval around an optimizer and not an assertion about an unknown exact minimizer. Its numerical origin is mathematically irrelevant after freezing the vector.

The bolt shift should be understood algebraically as
\[
c_{G,0}^{\rm new}
=c_{G,0}^{\rm old}
-\sum_k(-1)^k(c_{F,k}+c_{G,k}),
\]
which makes \(q_F(0)+q_G(0)=0\) identically. Recording the dyadic ratios or hexadecimal float strings in a final archival version would make this interpretation platform-independent, but it does not alter the present witness.

---

### 5. From \(C^2\) matching to smooth exact-CH cells

Let \(v=X-x\). Every deviation from the complex-hyperbolic profile is \(O(v^3)\), with first and second derivatives \(O(v^2)\) and \(O(v)\). This includes both the free \((1-u)^3\) terms and the smoothstep interpolation, since
\[
S(u)-1=O((1-u)^3).
\]

Choose a smooth cutoff \(\chi(v/\delta)\) that vanishes near \(v=0\) and equals one for \(v\ge\delta\), and replace the deviation from CH by \(\chi\) times that deviation. In the transition collar,
\[
\Delta g=O(\delta^3),\qquad
\nabla\Delta g=O(\delta^2),\qquad
\nabla^2\Delta g=O(\delta).
\]
The inverse metric remains uniformly controlled there, so
\[
\Ric(g_\delta)+6g_\delta=O(\delta).
\]
Since the collar volume is \(O(\delta)\),
\[
J_6(g_\delta)-J_6(g_0)=O(\delta^3),
\qquad
J_6(g_\delta)\longrightarrow J_6(g_0).
\]
Each \(g_\delta\) is smooth and agrees exactly with CH on an open outer collar. Therefore some fixed sufficiently small \(\delta\) already gives a smooth cell with cost below \(8\pi^2\).

To retain the full numerical coefficient based on the \(C^2\) limiting value, take \(\delta_j\to0\) along the balanced sequence. Then the smooth cell costs satisfy
\[
J_{1,j}=J_1+o(1).
\]
This diagonal choice justifies the exact limsup expression with the computed \(J_1\). If one instead fixes a single smoothed cell once and for all, one obtains the same strict conclusion with any slightly smaller value of \(\varepsilon_0\).

---

### 6. Residual-finite replication and transfer constant

Let \(r\) contain the scaled \(X=8\) cell and a fixed buffer. For a point \(p\in\mathbb{CH}^2\), proper discontinuity makes
\[
\{\gamma\ne1:d(p,\gamma p)\le2r\}
\]
finite. Residual finiteness supplies a finite-index subgroup containing none of these elements, hence a finite cover \(X_*\) containing the required embedded ball.

Every further degree-\(d_j\) cover of \(X_*\) contains \(d_j\) disjoint lifts of that ball. Since \(A_j=d_jA_*\) and
\[
\frac{k_j}{A_j}\sim\frac29 h_j\longrightarrow0,
\]
one has \(k_j/d_j\to0\). Thus there are more than enough disjoint lifts for all \(k_j\) blow-up cells. This is a genuine replication argument, not an assumption of uniformly large injectivity radius for arbitrary cover sequences.

For the resulting metrics, evaluated at the fixed Einstein constant \(\lambda=-1\),
\[
D_j
\le k_j(J_1+o(1))+32\pi^2\ell_j+o(Q_j),
\]
while
\[
V_j=2\pi^2A_j+O(Q_j).
\]
Because \(h_j=Q_j/A_j\to0\), the volume correction contributes only \(o(1)\) after dividing the defect by \(h_j\). Using
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36},
\]
gives
\[
\begin{aligned}
\limsup_j\frac{\alpha_j}{h_j}
&\le
\frac29\frac{J_1}{2\pi^2}
+\frac7{36}\frac{32\pi^2}{2\pi^2}\\
&=\frac{J_1}{9\pi^2}+\frac{28}{9}.
\end{aligned}
\]
Writing \(J_1=8\pi^2(1-\varepsilon_0)\) yields
\[
\frac{28}{9}+\frac{J_1}{9\pi^2}
=4-\frac89\varepsilon_0.
\]
The certified Arb ball gives
\[
\varepsilon_0>0.0008837568646756,
\]
and hence
\[
4-\frac89\varepsilon_0
<3.999214438342511.
\]

### Final assessment

The local curvature algebra, orbit-volume factor, holomorphic Arb callback, exact dyadic witness, smooth exact-CH approximation, replicated cover construction, and coefficient arithmetic fit together correctly. No remaining mathematical flaw in these components overturns the strict coefficient below \(4\). The unresolved mathematical quantity is the optimal cell cost, and therefore the sharp balanced coefficient, not the existence of this strict upper construction.