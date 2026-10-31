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

# Verification memo: rigorous enclosure of the perpendicular cell and the O11 coefficient

## Summary

I found no mathematical error that overturns the result. The enclosure, the cell's geometry, the smoothing step and the transfer combine into a proof of

\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}\le 4-\tfrac89\varepsilon_0<3.999214438342511
\]

for a balanced surgery family built from covers of a fixed complex-hyperbolic quotient \(X_*\) with an embedded ball of radius above \(\sqrt6\,\operatorname{arsinh}\sqrt8\approx4.32\).

The certified \(P\)-ball also gives a slightly stronger proved constant through the traceless reduction theorem (§7).

Two points need precise wording in the synthesis:

- The witness's exact definition includes the bolt shift of \(c_{G,0}\) (§3).
- The statement is existential over balanced families. It does not cover every cover sequence (§6).

## 1. Bolt-regular Ricci rewrite and volume normalization

**\(D\)-terms.** With \(d/dt=2\sqrt G\,d/dx\) and \(a=\sqrt h\), one has \(\dot a/a=\sqrt G\,h_x/h\). For a general slot,

\[
\frac{\ddot a}{a}=\frac{2Gh_{xx}}{h}+h_x\Big(\frac Gh\Big)_x .
\]

- For \(h_1\), this gives \(D_1=2\rho h_{1,xx}+h_{1,x}\rho_x\) with \(\rho=G/h_1=\widehat G/\widehat F\). This is the code's expression.
- For \(h_2=x\), it gives \(D_2=G_x/x-G/x^2\).
- For \(h_3\), it gives \(D_3=G_xh_{3x}/h_3+2Gh_{3xx}/h_3-Gh_{3x}^2/h_3^2\).

**Mixed products.** \(L_1L_j=\rho h_{1x}h_{jx}/h_j\) and \(L_2L_3=Gh_{3x}/(xh_3)\). These match the code.

**Algebraic terms.**

- \(A_1\): uses \((e^w-1)^2=w^2\phi(w)^2\) with \(w=y^2\widehat w\). The code's \(\widehat w\) is \(u^2(\dots)\) divided by \((x_0\ell\phi)^2u^2\), so \(w=y^2\widehat w\) exactly. This gives the \(y^3\widehat w^2\phi^2/\widehat F\) term.
- \(A_2,A_3\): use \(\operatorname{shc}(w)=(\phi(w)+\phi(-w))/2=\sinh w/w\).

No factor \(1/y\) survives anywhere. The \(u\to x\) jet map \(f_{xx}=(f_{uu}-\ell f_u)/(\ell^2x^2)\) is correct.

**Normalization constant.** The closed formula vanishes on flat \(dt^2+t^2\sum\sigma_i^2\) only when \(d\sigma_1=2\sigma_2\wedge\sigma_3\): \(-2/t^2+2/t^2=0\). This fixes the constant.

**Diagonal Ricci.** The integrand \(\sum_a(R_{aa}+6)^2\) requires a diagonal Ricci tensor. This follows from the Klein four-group of conjugations by \(i,j,k\), which flip pairs of \(\sigma\)'s and are isometries of every diagonal profile. Each off-diagonal component changes sign under one of them, so it vanishes.

**Three independent numerical checks of the formula and its normalization.**

1. At \(u=1\) the profile is \(h_1=h_2=x\), \(h_3=G=X(1+X)\), and all four components equal \(-6\) to \(3\times10^{-14}\).
2. At \(u=0\) the output has \(R_{00}=R_{11}\) and \(R_{22}=R_{33}\), which is the symmetry forced by bolt smoothness.
3. The Arb values of \(P\) and of \(S=\frac14\int(s+24)^2\) agree with the separately coded Cartan/spin evaluator to \(10^{-15}\). That evaluator uses \(u_i,H_i,\lambda_i\) and the relative calibration.

**Volume.** With \(\int_{SU(2)}\sigma_1\sigma_2\sigma_3=2\pi^2\) (unit round \(S^3\) in this convention),

\[
dV/(8\pi^2)=\tfrac18\,xe^{w/2}\sqrt{F/G}\,dx,\qquad dx=\ell x\,du .
\]

At \(u=1\) this equals \(X^2\ell/8=64\log 800/8=53.4769\), matching the pointwise output \(53.47689\).

## 2. The `acb.integral` holomorphy contract

The callback signature `f(u, analytic)` matches python-flint. The non-entire operations are handled as follows:

- **Logarithm and square root.** The only logarithm, \(\log(1+x)\), and the only square root, \(\sqrt{\widehat F/\widehat G}\), receive `analytic=analytic`. They return indeterminate output if the ball meets a branch cut.
- **Divisions.** All divisions are by \(\widehat F,\widehat G,x,h_3,\phi\). Ball division by a set containing zero is non-finite, as the contract requires.
- **Everything else** (exp, Chebyshev polynomials, products) is entire.

**Piecewise \(\phi\).** Branch selection by a ball-dependent test is legitimate, because both branches enclose the same entire function.

- *Quotient branch.* The derivative formulas \(\phi'=(ze^z-e^z+1)/z^2\) and \(\phi''=(z^2e^z-2ze^z+2e^z-2)/z^3\) are correct.
- *Series branch.* The coefficients of \(\phi,\phi',\phi''\) are \(1/(k+1)!\), \((k+1)/(k+2)!\) and \(1/(k!(k+3))\), all at most \(1/k!\). Hence the tail bound \(r^N/N!/(1-r/(N+1))\) is valid. Adding it to both real and imaginary parts covers the error disc.
- *Radius \(r\).* The float \(r\) is an upper bound for \(|z|\), with a \(1+2^{-30}\) margin over the binary64 rounding.

**Integrand and result.** After desingularization the integrand is analytic near \([0,1]\), including slightly past \(u=0\), where \(\widehat F,\widehat G\approx e^{\pm q(0)}>0\). Its restriction to the real axis is real, so the real part of the output ball contains the integral. Arb's integrator returns an enlarged ball rather than a wrong one when convergence stalls. The tight radii at 160, 256 and 320 bits are mutually nested.

The remaining trust rests on the python-flint/Arb implementation itself. The 256/320-bit reruns use the same script, so they replicate the computation but do not independently re-derive it. The 1e-15 agreement with the spin code supplies that independence at the level of the formula.

## 3. The coefficient vector as an exact witness

- `arb(float(v))` makes each JSON coefficient an exact dyadic rational, and \(X=8\) is exact.
- \(x_0\) = `arb(1)/100` is a ball that contains \(1/100\). The enclosure therefore holds for \(x_0=1/100\) exactly.
- \(c_{G,0}\) is replaced by \(c_{G,0}-\sum_k(-1)^k(c_{F,k}+c_{G,k})\). This shift is a dyadic rational computed in a containing ball.

The witness is therefore the explicit real-analytic metric with these dyadic coefficients and this shifted \(c_{G,0}\). It enforces \(q_F(0)+q_G(0)=0\), so \(F'G'=1\) holds exactly. The synthesis should name the shifted constant term. The float record value \(0.99911624282\) is not the certified quantity and is not needed.

## 4. Bolt regularity and topology

**Bolt jets.** Near the bolt, \(t^2=y\cdot(\text{analytic in }y)\). Then \(a_1/t\to\sqrt{f_1g_1}=1\), and

\[
h_3-h_2=x(e^w-1)=O(y^2)=O(t^4).
\]

This is the weight-four condition for \(\sigma_2^2-\sigma_3^2\) when the \(\sigma_1\) circle closes with period \(2\pi\). The bolt is therefore smooth.

**Topology.** The \(\sigma_1\)-collapse disc bundle differs from the \(\sigma_3\) (complex Hopf) collapse by right multiplication by a unit quaternion. That map lies in \(SO(4)\) and is orientation-preserving. Hence the cell realizes exactly \(\#\overline{\mathbb{CP}}^2\), matching the topology of \(M_j\).

## 5. From \(C^2\) matching to a smooth exact-collar cell

The deviations \(\delta\in\{F-x,\ G-x-x^2,\ w-\log(1+x)\}\) all equal \((1-u)^3\) times functions analytic near \(u=1\). This uses \(S-1=O((1-u)^3)\), since \(S'(1)=S''(1)=0\).

Replace \(\delta\) by \(\beta\delta\), where \(\beta=1\) on \(x\le X-2c\), \(\beta=0\) on \(x\ge X-c\), and \(|\beta^{(m)}|\lesssim c^{-m}\). Then:

- the profile is unchanged on \(x\le X-2c\) and exactly CH beyond \(X-c\), so the metric is \(C^\infty\);
- on the transition, \((\beta\delta)^{(m)}=O(c^{3-m})\) for \(m\le2\);
- the curvature, which involves \(h''\) and \(G'\), differs from CH by \(O(c)\) on a volume \(O(c)\).

Consequently

\[
J_6^{\rm new}\le J_6^{\rm old}+O(c^3),
\]

and the same bound holds for \(P\). Because the deficit \(8\pi^2\varepsilon_0\) is fixed, a small \(c\) preserves the strict inequality. The smoothing takes place inside \(x\le X\), so it needs no extra radius. No quantitative cutoff constant is required for the strict statement.

## 6. Residual-finite replication

Residual finiteness gives a finite cover \(X_*\) in which \(B(p,r)\) is embedded. Every finite cover \(X_j\to X_*\) then contains \(\deg(X_j\to X_*)=A_j/A_*\) disjoint isometric lifts of that ball. A further subgroup is not needed: any cover works, since an embedded ball is evenly covered.

Since \(k_j\sim\frac29h_jA_j=o(A_j)\), all blow-ups fit, with room left for the handle sites.

Theorem `thm:vg-balanced-family` applies verbatim with base \(X_*\). Its rounding, its lower bound \(c_*h_j\), and the choice \(A_j\ge j^4\) are all unchanged.

**Existential nature.** For an arbitrary cover sequence of the original \(X_0\) the embedding is not automatic. If \(b_1(X_0)>0\), abelian covers whose kernel contains a fixed loop \(\gamma_0\) have injectivity radius at most \((\ell(\gamma_0)+2\operatorname{diam}X_0)/2\) everywhere. So the theorem is existential over balanced families, which suffices to refute universal coefficient four.

The method needs much less than \(X_*\): any sequence with at least \(k_j=O(h_jA_j)\) disjoint thick \(r\)-balls works. This includes any sequence of covers Benjamini–Schramm converging to \(\mathbb{CH}^2\).

## 7. The constant

A direct derivation avoids reliance on I54. Use \(\lambda=-1\) in

\[
\mathcal E(g)=\inf_\lambda\int|\operatorname{Ric}-\lambda g|^2/(\lambda^2V).
\]

The global metric consists of CH (where \(\operatorname{Ric}+g=0\)), \(k_j\) cells of cost \(J_1=J_6\) (scale invariance under \(\tilde g=6g\)), and \(\ell_j\) shrinking handle insertions. On each handle insertion \(s=0\) on volume \(O(\varepsilon^4)\), so its cost tends to \(32\pi^2\). This per-type value follows from the recovery limit \(P_\varepsilon\to8\pi^2(k+4\ell)\) for all \(k,\ell\), together with locality.

Letting \(\varepsilon\to0\) at fixed \(j\), with \(V_j=2\pi^2A_j+k_j\Delta V=2\pi^2A_j(1+O(h_j))\),

\[
\frac{\alpha_j}{h_j}\le\frac{k_jJ_1/(2\pi^2)+16\ell_j}{Q_j}(1+O(h_j))
\;\longrightarrow\;\frac{J_1}{9\pi^2}+\frac{28}{9}=4-\frac89\varepsilon_0 .
\]

Numerically, \(\varepsilon_0>0.000883756864675689-2.3\times10^{-19}\), which gives the stated bound \(<3.999214438342511\).

**Sharper proved constant.** Theorem `thm:vg-first-order-reduction` gives \(\alpha_j=4\rho_j+O(h_j^2)\) on this family. Combined with \(P\)-additivity (the CH background has \(\operatorname{Ric}^\circ=0\)), this yields

\[
\limsup\frac{\alpha_j}{h_j}\le4-\frac89\delta_P,\qquad
\delta_P=1-\frac{P}{8\pi^2}=0.000891297266407\ (\pm5\times10^{-19}),
\]

that is, \(\limsup\alpha_j/h_j\le3.9992077357632\).

The scalar part \((J_6-P)/8\pi^2=7.54\times10^{-6}\) is absorbed at order \(h^2\) by the conformal comparison. This is the better certified constant from the same witness.

**Notation.** The paper's \(\mathcal J(g)=4P/R\) and the cell energy \(J_6\) are different objects. The synthesis should keep their symbols distinct.

## 8. Open questions in the O11 problem

Nothing identified above overturns the result. The open mathematics concerns the exact value of the coefficient, not the strict inequality:

- the cell infimum within and beyond diagonal \(SU(2)\) symmetry;
- a matching lower bound;
- the near-extremal geometry.