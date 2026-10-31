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
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the fixed perpendicular complex-hyperbolic cell record and both independent verification notes/scripts. Check the mathematical chain needed for a strict same-metric cell J_6<8π²: normalization, Cartan/relative identities, bolt smoothness, positivity, CH attachment and smoothing, numerical integral, residual-finite cover supply, and inherited global transfer. Identify any substantive error that would invalidate the candidate, and distinguish what is proved from what remains numerical. In particular inspect the 160-bit Arb script: say exactly what it encloses and whether its Richardson-inflated result is or is not a rigorous quadrature certificate. Give a direct scientific memo aimed at completing O11, not generic review.

## Integrated Scientific Memo

# O11 verification memo: fixed perpendicular complex-hyperbolic cell

## Verdict

No normalization, bolt, positivity, attachment, covering, or transfer error was found that invalidates the \(x_0=0.01,\ X=8\), degree-eight candidate. The computations consistently indicate
\[
\frac{P}{8\pi^2}=0.9991087027335926,\qquad
\frac{J_6}{8\pi^2}=0.9991162431353243,
\]
where
\[
J_6=\int |\Ric+6g|^2
=P+\frac14\int(s+24)^2.
\]

However, the strict inequality
\[
J_6<8\pi^2
\]
is **not yet proved**. The 160-bit Arb script rigorously encloses finite composite-Simpson sums, but its Richardson-inflated interval is not a rigorous enclosure of the integral. It also omits \(u\in[0,10^{-12}]\) without bounding that tail.

Thus the candidate is mathematically coherent and numerically very convincing, but O11 still requires one certified integral bound.

---

## 1. Normalization and same-metric issue

In dimension four,
\[
\Ric=\Ric^\circ+\frac{s}{4}g,
\]
with orthogonal trace and traceless parts. Hence
\[
|\Ric+6g|^2
=|\Ric^\circ|^2+\frac14(s+24)^2.
\]
Therefore
\[
J_6=P+\frac14\int(s+24)^2
\]
is an exact identity, not a combination of unrelated estimates.

Both numerical terms are evaluated on the same frozen profile
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2.
\]
The JAX verifier computes `P_relative`, `P_positive`, and `scalar` from one `Metric` object at the same quadrature nodes; the Arb evaluator likewise sums the relative-\(P\) and scalar densities inside one `dens_x` call. There is no same-metric mismatch.

Under \(\widetilde g=6g\),
\[
\Ric_{\widetilde g}=\Ric_g,\qquad
|\cdot|_{\widetilde g}^2=6^{-2}|\cdot|_g^2,\qquad
dV_{\widetilde g}=6^2dV_g,
\]
so
\[
\int|\Ric_{\widetilde g}+\widetilde g|_{\widetilde g}^2\,dV_{\widetilde g}
=\int|\Ric_g+6g|_g^2\,dV_g=J_6(g).
\]
The cell cost therefore transfers correctly from the \(\Ric=-6g\) normalization to the global \(\Ric=-g\) normalization.

The CH profile
\[
G=x+x^2,\qquad F=x,\qquad w=\log(1+x)
\]
is consistent with \(\Ric=-6g\): putting \(x=\sinh^2r\) gives
\[
g=dr^2+\sinh^2r(\sigma_1^2+\sigma_2^2)
+\sinh^2r\cosh^2r\,\sigma_3^2.
\]

---

## 2. Cartan and relative identities

With the script’s cyclic ordering
\[
(a_1,a_2,a_3)=\bigl(\sqrt x,\sqrt{xe^w},\sqrt F\bigr),
\qquad \frac{dx}{dt}=2\sqrt G,
\]
define
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k,\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]
The positive-square formula used is
\[
\frac{P}{8\pi^2}
=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.
\]

The relative density in the verifier satisfies the algebraic identity
\[
\mathcal P-\mathcal R
=-\frac{d}{dt}\bigl(u_1^2+u_3^2+u_1u_2u_3\bigr).
\]
At the bolt,
\[
(u_1,u_2,u_3)\to(0,0,-1),
\]
whereas on the CH end
\[
(u_1,u_2,u_3)=(0,3x,0).
\]
Thus the boundary primitive changes from \(1\) to \(0\), giving
\[
\frac{P}{8\pi^2}=1+\int\mathcal R\,dt.
\]
This explains both the relative-calibration constant \(1\) and the \(8\pi^2\) one-cell reference value.

On the exact CH profile,
\[
u=(0,3x,0),
\]
and the positive-square terms vanish. The scalar expression also has
\[
\Sigma=12,
\]
so the script’s scalar density
\[
\frac{a_1a_2a_3}{4}(\Sigma-12)^2
\]
vanishes, as required by \(s=-24\).

One harmless code defect should be corrected: in `o11_collar_independent_verify.py`,
```python
C = jnp.sum(u*u)+jnp.prod(u)
```
is not the boundary primitive for the relative identity. The relevant primitive is
\[
u_1^2+u_3^2+u_1u_2u_3.
\]
The incorrect `C` variable is returned but never integrated or used in the reported \(P\), scalar, or \(J\), so it does not affect the numerical result.

The source files do not themselves contain a formal derivation of the Cartan formulas from the metric. Their strong checks are:

* exact vanishing on CH;
* agreement of positive-square and relative evaluations to \(<5\times10^{-15}\);
* agreement with the separately inherited coordinate-curvature computation.

For the final certificate, directly enclosing a curvature-derived \(P+\)scalar density would remove reliance on the relative calibration as an unproved implementation identity.

---

## 3. Bolt smoothness and topology

Let
\[
y=x-x_0,\qquad
u=\frac{\log(x/x_0)}{\log(X/x_0)}.
\]
Since
\[
S(u)=10u^3-15u^4+6u^5=O(y^3)
\]
at the bolt,
\[
F=f_1y+O(y^2),\qquad
G=g_1y+O(y^2),\qquad
w=O(y^2).
\]
The implemented shift in \(c_G\) imposes
\[
q_F(0)+q_G(0)=0,
\]
and therefore
\[
f_1g_1=1
\]
algebraically. Numerically,
\[
f_1=0.9688603622004124,\qquad
g_1=1.0321404807281673.
\]

Using radial distance
\[
\rho=\int_0^y\frac{dz}{2\sqrt{G(z)}}
=\sqrt{\frac{y}{g_1}}+O(y^{3/2}),
\]
one obtains
\[
\frac{dy^2}{4G}=d\rho^2+O(\rho^2)d\rho^2,\qquad
F=\rho^2+O(\rho^4).
\]
Moreover,
\[
x=x_0+O(\rho^2),\qquad xe^w-x=O(\rho^4).
\]
Thus the collapsing \(\sigma_1\)-circle has the no-cone form
\[
d\rho^2+\rho^2\sigma_1^2,
\]
while the two noncollapsing directions agree at the bolt and their anisotropy starts at order \(\rho^4\), the required weight-four behavior.

This proves smooth extension across the bolt in the inherited circle-period convention. The final written proof should state that convention explicitly; no evidence of a missing factor \(2\) or \(4\) appears in the supplied normalization.

The perpendicular choice of collapsing Hopf direction is related to the standard CH collapsing circle by an orientation-preserving \(SU(2)\) rotation. Hence it gives the same oriented Euler-\((-1)\) disc bundle, i.e. the local blow-up cell. This topological identification is compatible with the inherited global construction.

---

## 4. Positivity

Positivity is analytic, not inferred from sampling. For \(x_0<x\le X\),
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\]
and
\[
G=\bigl[(x-x_0)+(x^2+x_0)S(u)\bigr]e^{q_G}>0.
\]
Indeed,
\[
S'(u)=30u^2(1-u)^2\ge0,\qquad S(0)=0,\quad S(1)=1,
\]
so \(0\le S\le1\). Also \(x>0\) and \(xe^w>0\).

The sampled bounds
\[
\min\frac{G}{x-x_0}=1.0321404811,\qquad
\min\frac{F}{x-x_0}=0.9661766585
\]
are merely conditioning diagnostics. No separate interval positivity certificate is needed.

---

## 5. CH attachment and smoothing

At \(u=1\),
\[
1-S(u)=(1-u)^3(6u^2+3u+1),
\]
and every free perturbation also carries \((1-u)^3\). Consequently
\[
F-x,\quad G-(x+x^2),\quad w-\log(1+x)
=O((1-u)^3),
\]
so values and the first two \(x\)-derivatives agree with CH at \(X\). Direct attachment produces a global \(C^2\) metric with continuous curvature and zero CH defect outside the cell.

There are two adequate smoothing arguments.

### Existence by \(C^2\) approximation

On a compact glued manifold, the curvature energy
\[
g\longmapsto \int|\Ric_g+g|^2\,dV_g
\]
is continuous under uniformly positive \(C^2\) convergence. A positive \(C^2\) metric can be approximated by smooth positive metrics in \(C^2\). Hence a strict inequality for the \(C^2\) glued metric passes to a nearby smooth metric. This avoids the need for an explicit cutoff constant.

### Exact-CH-collar cutoff

If an explicit smooth cell that remains exactly CH outside a narrow collar is desired, write the deviation as
\[
h=O(z^3),\quad \partial h=O(z^2),\quad \partial^2h=O(z),
\qquad z=X-x.
\]
Cutting it off over width \(\delta\) changes the second derivatives, hence the Ricci defect, by \(O(\delta)\). The original defect in that collar is also \(O(\delta)\), and the collar volume is \(O(\delta)\), so
\[
J_6(g_\delta)-J_6(g)=O(\delta^3).
\]
Thus any rigorously certified strict frozen-cell deficit survives sufficiently small smoothing.

The printed coefficient \(3.9992144383\) corresponds to the limiting frozen \(C^2\) cost. A fixed but unquantified smoothing gives some strict coefficient below \(4\), while a sequence of smoothings with \(\delta\to0\) recovers the displayed value in the global \(\limsup\).

---

## 6. Numerical value and its present status

The independent split-Gauss computation gives
\[
\begin{aligned}
S_1&=0.00159729167196687,\\
S_2&=0.00052244698325698,\\
S_3&=0.00109028656646375,\\
C_3&=-0.00410132248809498.
\end{aligned}
\]
Hence
\[
\frac{P}{8\pi^2}
=1+S_1+S_2+S_3+C_3
=0.9991087027335926.
\]
The scalar contribution is
\[
\frac{J_6-P}{8\pi^2}
=7.54040173166\times10^{-6},
\]
so
\[
\frac{J_6}{8\pi^2}
=0.9991162431353243
\]
and the indicated deficit is
\[
\varepsilon_0
=1-\frac{J_6}{8\pi^2}
=8.83756864676\times10^{-4}.
\]

The 200, 400, and 800 split-Gauss results agree to the displayed digits, and the positive-square and relative formulas for \(P\) differ by less than \(5\times10^{-15}\). The older optimizer value
\[
0.9991162428177064
\]
differs by approximately \(3.2\times10^{-10}\), consistently with its lower-order quadrature.

These facts establish excellent numerical stability, not a rigorous integral enclosure.

---

## 7. Exact interpretation of the 160-bit Arb output

The Arb script evaluates the normalized defect density in logarithmic coordinate \(u\):
\[
f(u)
=\left(S_1+S_2+S_3+C_3+\text{scalar}\right)
\frac{dt}{dx}\frac{dx}{du}.
\]
It computes composite-Simpson sums over
\[
u\in[10^{-12},1]
\]
at 160-bit precision.

### What Arb rigorously encloses

For each fixed mesh \(n=500,1000,2000\), it encloses:

1. the decimal coefficient values after JSON parsing and `repr` conversion;
2. profile values and the derivatives needed by the second-order jet calculation;
3. each pointwise relative-plus-scalar density at the Simpson nodes;
4. all 160-bit rounding in those evaluations;
5. the corresponding finite weighted Simpson sum.

Thus, for example,
\[
[-0.00088375686366234348033656096\pm4.74\times10^{-30}]
\]
is a rigorous enclosure of the **finite \(n=2000\) Simpson sum**, not of the integral.

For an unambiguous exact-decimal witness, the script should parse the JSON numbers as strings, e.g. with `parse_float=str`, rather than first converting them to binary64. This distinction is far below the present margin, but should be removed in a formal certificate.

### What it does not enclose

The code sets
\[
e=\frac{|S_{2000}-S_{1000}|}{15},\qquad r=1000e,
\]
and reports
\[
1+\operatorname{mid}(S_{2000})+[-r,r].
\]
This uses the asymptotic \(h^4\) Simpson error model and an empirical safety factor. There is no proved bound on
\[
\sup|f^{(4)}|,
\]
nor another theorem converting the successive-mesh difference into an integral remainder. Multiplication by \(1000\) does not make the estimate rigorous.

Moreover, the code omits
\[
\int_0^{10^{-12}}f(u)\,du.
\]
Its comment says that this tail is enclosed separately, but no such enclosure is added in `simpson()` or `main()`.

Therefore the fields
```text
J_enclosure
J_upper
below_one
```
do **not** constitute a theorem-level quadrature certificate. In particular,
\[
J_{\rm upper}=0.999116244147447\ldots<1
\]
is a Richardson-inflated numerical estimate, not a rigorous upper bound for \(J_6/(8\pi^2)\).

The script’s docstring reference to a “rigorous global fourth-derivative remainder” is contradicted by the implementation: no fourth derivative or global bound is computed.

---

## 8. A modest rigorous error bound is enough

For composite Simpson with \(n=2000\),
\[
\left|\int_\epsilon^1 f-S_n\right|
\le
\frac{(1-\epsilon)^5}{180n^4}
\sup_{\epsilon\le u\le1}|f^{(4)}(u)|.
\]
To preserve merely the observed \(8.84\times10^{-4}\) sign margin, it is enough to prove roughly
\[
\sup|f^{(4)}|<2.5\times10^{12},
\]
together with a small explicit bound on the omitted initial interval. There is no need to certify the \(10^{-9}\)-scale Richardson radius.

The appropriate bolt regularization is
\[
y=x-x_0,\qquad
F=y\widehat F,\qquad
G=y\widehat G,\qquad
w=y^2\widehat w.
\]
Here \(\widehat F,\widehat G,\widehat w\) extend analytically to \(y=0\), with \(\widehat F,\widehat G>0\). After algebraically cancelling the removable \(\sqrt y\) and \(1/\sqrt y\) factors, the invariant density has an ordinary Taylor expansion at the bolt. One can then:

* enclose a Taylor remainder and the omitted \(u\)-tail near \(0\);
* use interval subdivision on the remaining compact interval; or
* prove the coarse fourth-derivative bound needed by Simpson.

A curvature-coordinate formula rational in \(F,G,w\) and their derivatives is preferable to the raw spin expression because it eliminates the severe interval dependency near the bolt. Enclosing the positive-square \(P\) density plus scalar density also avoids relying on the relative boundary calibration in the final numerical proof.

---

## 9. Residual-finite large-ball supply

Let \(p\in\mathbb{CH}^2\), and choose a fixed buffered radius \(r\) containing the cell and smoothing region. Only finitely many lattice elements satisfy
\[
d(p,\gamma p)\le2r.
\]
Residual finiteness supplies a finite-index subgroup avoiding all of them. The corresponding finite cover therefore contains the required embedded ball.

Every further degree-\(d\) cover has \(d\) disjoint lifts of that ball. Their number is proportional to the covering degree and hence to \(A_j\). Since in the balanced family
\[
k_j\sim\frac29Q_j,\qquad
Q_j=A_jh_j,\qquad h_j\to0,
\]
the required cells number \(o(A_j)\), while available lifted balls number \(\asymp A_j\). The supply is more than sufficient.

This proves an existential balanced family after replacing the original base by the fixed large-ball cover. It does not imply that every previously prescribed cover sequence contains such balls.

The radius conversion is correct:
\[
r_{-6}=\operatorname{arsinh}\sqrt8,\qquad
r_{-1}=\sqrt6\,\operatorname{arsinh}\sqrt8\approx4.32,
\]
plus any fixed collar buffer if exact-CH cutoff smoothing is used.

---

## 10. Global transfer

For \(k_j\) blow-up cells and \(\ell_j\) standard shrinking handle insertions,
\[
\int_{M_j}|\Ric+g|^2
\le k_jJ_1+32\pi^2\ell_j+o(Q_j),
\]
while
\[
\Vol(M_j)=2\pi^2A_j+o(A_j).
\]
Using
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36},\qquad
h_j=\frac{Q_j}{A_j},
\]
gives
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le
\frac{28}{9}+\frac{J_1}{9\pi^2}.
\]
If
\[
\frac{J_1}{8\pi^2}=1-\varepsilon_0,
\]
then
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le4-\frac{8\varepsilon_0}{9}.
\]
For the numerical frozen value,
\[
\varepsilon_0\approx0.000883756864676,
\]
so the limiting indicated coefficient is
\[
3.9992144383\ldots<4.
\]

There is also a slightly stronger route through the paper’s traceless-Ricci estimate. Since the same cell numerically has
\[
\frac{P_{\rm cell}}{8\pi^2}=0.9991087027335926<1,
\]
the inequality
\[
\alpha_j\le \frac{4P(g)}
{8\pi^2A_j+P(g)}
\]
would yield a coefficient of approximately \(3.9992077\), using only a certified \(P_{\rm cell}<8\pi^2\). This route relies on the paper’s monopole/Yamabe comparison but avoids certifying the positive scalar-square contribution. It has the slightly larger margin
\[
1-\frac{P_{\rm cell}}{8\pi^2}
=8.91297266407\times10^{-4}.
\]

---

## Completion status

### Established analytically

* normalization and scale invariance;
* use of one and the same metric for all energy terms;
* bolt no-cone relation and weight-four anisotropy;
* analytic positivity;
* second-jet agreement with CH;
* passage from the \(C^2\) glued metric to smooth metrics;
* residual-finite supply of sufficiently many fixed large balls;
* the inherited coefficient
  \[
  \frac{28}{9}+\frac{J_1}{9\pi^2}.
  \]

### Strong numerical evidence, not yet theorem

\[
\frac{P}{8\pi^2}=0.9991087027335926,\qquad
\frac{J_6}{8\pi^2}=0.9991162431353243.
\]

The Arb script certifies only the finite Simpson sums. Its Richardson-times-\(1000\) interval is not a rigorous quadrature enclosure, and it omits the interval \(u\in[0,10^{-12}]\).

### Precise remaining object

The remaining task is a rigorous upper enclosure below zero for either
\[
\frac{J_6}{8\pi^2}-1
\]
or, via the paper’s \(P\)-route, for
\[
\frac{P}{8\pi^2}-1.
\]
A bolt-regularized interval/Taylor evaluation with total error below roughly \(8\times10^{-4}\) suffices. Once that single enclosure is supplied, the smooth same-metric cell and global residual-finite transfer give a rigorous O11 upper coefficient strictly below \(4\).