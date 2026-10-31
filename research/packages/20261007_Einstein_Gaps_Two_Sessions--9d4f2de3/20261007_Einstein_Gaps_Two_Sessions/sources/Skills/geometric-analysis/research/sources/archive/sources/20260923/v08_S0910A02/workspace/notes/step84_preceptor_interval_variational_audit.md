# Step 84: Preceptor audit of interval quantifiers, mirror reductions, and the variational no-gap formulation

Session `S0910A02`, Agent4/Preceptor, Explore.

## 0. What I audited

I read the Step 83 construction note, the TTCS verifier integration and both verifier branches, the ten-sector Weyl audit data, the Step 82 sign-leg data, and A01's Step 87 missed-mode correction. I also ran a new arithmetic script:

- `workspace/scripts/step84_interval_variational_audit.py`
- output `workspace/data/step84_interval_variational_audit.json`

The construction side of Step 83 survives the Preceptor audit with its stated hypotheses: common radial normal gauge, `O_2` EH tail and ambient Taylor estimates, analytic radial-cutoff formula, fixed finite node set, fixed markings, and constants independent of the gluing parameter `a`. The ten-sector Weyl audit genuinely addresses the non-`U(2)` leakage worry: all of `Sym^2_0(Λ^+) ⊕ Sym^2_0(Λ^-)` satisfies the radial gauge, trace/divergence/harmonicity, and linearized-Ricci identities needed for the log annulus. A01's Step 87/88 Green-mode corrections concern exact desingularization coefficients; they do not create cross-node terms in the locally patched near-pinched construction, because the Step 83 metrics are assembled in disjoint balls and equal the Einstein orbifold metric outside.

This note records two corrections/additions to the route-level interpretation.

## 1. Dimension-four interval classification: boundary intervals are not surviving cases

For fixed dimension four, the original proposition asks whether there exists *some* interval `c<C`. The intervals are:

1. `c<0<C`;
2. `c=0<C`;
3. `c<0=C`;
4. `0<c<C`;
5. `c<C<0`.

Step 83 correctly noticed that a positive near-pinched fixed row only attacks positive intervals, but it did not close the boundary cases. They are closed as follows.

### 1.1 Intervals containing zero in their interior

If `c<0<C`, choose any smooth metric `g` on a closed no-Einstein four-manifold and replace it by `tg`. Constant rescaling leaves the Ricci `(0,2)` tensor unchanged while the interval bounds become `ct g` and `Ct g`. For large `t`, every bounded Ricci endomorphism lies in `[ct,Ct]`. Thus any no-Einstein four-manifold defeats such intervals. Use `S^1×S^3`.

### 1.2 The nonnegative boundary interval `[0,C]`

`S^1×S^3` with the product of a flat circle and the unit round `S^3` has Ricci eigenvalues `(0,2,2,2)` relative to the product metric. After multiplying the metric by a sufficiently large constant, it satisfies
\[
0\le Ric\le Cg
\]
for any prescribed `C>0`.

The same manifold has no Einstein metric. If a closed oriented Einstein four-manifold has `χ=0`, then the Einstein Chern--Gauss--Bonnet identity gives
\[
0=8\pi^2χ=\int(|W|^2+s^2/24),
\]
so `W=0` and `s=0`; with `E=0` this means the metric is flat. But a closed flat four-manifold has a Bieberbach fundamental group, equivalently a finite-index `Z^4` subgroup (Ocampo recalls the first Bieberbach theorem and the exact sequence `0→Z^n→Π→Φ→1` in lines 65--81 of `\cite{ocampo2019bieberbach}`). By contrast `π_1(S^1×S^3)=Z`, whose finite-index subgroups have rank one, so no flat metric exists.

### 1.3 The nonpositive boundary interval `[c,0]`

Lohkamp supplies a strictly negative Ricci metric on every closed manifold of dimension at least three; the cumulative Yau--26 source records the precise fixed-width statement at `Skills/qiushi-yau26/references/research/20260912.tex` lines 1214--1221, and the knowledge request returned the original announcement/source metadata `\cite{lohkamp1992negativelya}`. On `S^1×S^3`, take such a metric `g` with Ricci eigenvalues all negative. For `t` large, `tg` satisfies
\[
c\,tg\le Ric_g=Ric_{tg}\le0
\]
for any fixed `c<0`. The no-Einstein certificate is the same as above.

### 1.4 Strict one-signed intervals normalize exactly

If `0<c<C`, set
\[
\alpha=(C+c)/2,\qquad \delta=(C-c)/(C+c)\in(0,1),\qquad h=\alpha g.
\]
Then `c g≤Ric_g≤C g` is equivalent to
\[
(1-\delta)h\le Ric_h\le(1+\delta)h,
\]
that is `||Ric_h-h||_{op,h}≤δ`.

If `c<C<0`, set
\[
\alpha=-(C+c)/2>0,\qquad \delta=(C-c)/(-(C+c))\in(0,1),\qquad h=\alpha g.
\]
Then the interval is equivalent to
\[
-(1+\delta)h\le Ric_h\le-(1-\delta)h,
\]
that is `||Ric_h+h||_{op,h}≤δ`.

Hence in dimension four the original proposition holds iff at least one strict normalized branch `P_4^+(δ)` or `P_4^-(δ)` holds for some `δ<1`. A refutation in dimension four must defeat both strict branches; boundary and zero-crossing intervals are already defeated by `S^1×S^3` plus Lohkamp/rescaling.

## 2. Negative-mirror corollary of the audited construction

The Step 83 theorem is sign-neutral: it assumes a fixed closed Einstein 4-orbifold with finitely many `A_1` points and `Ric(g_0)=σg_0`, where `σ=±1`, plus fixed radial-normal markings and the EH core correction. Therefore it applies not only to the positive mirror
\[
(S^2\times S^2)/\mathbb Z_2,
\]
but also to the negative mirror
\[
(\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle.
\]
With each genus-2 surface normalized to curvature `-1`, the product has `Ric=-g`; the quotient has 36 isolated `A_1` points. Step 57 records the row arithmetic and topology: for `1≤r≤35`, the smooth fillings have
\[
χ=56,
\qquad τ=-36+2r,
\qquad b_+=9+r,
\qquad b_-=45-r,
\]
are simply connected, strict Hitchin--Thorpe, non-Kähler/nonsymplectic in both orientations, and have no known monopole or Gromov-norm obstruction.

Thus every fixed 36-node filling pattern carries metrics with
\[
\|Ric_g+g\|_{op}\le C/|\log a|\to0
\]
under the same fixed-marking hypotheses. The product-quotient positive rows attack strict positive intervals; the genus-2 negative rows attack strict negative intervals. Therefore a dimension-four refutation of the original Yau--26 proposition would need:

- one positive-mirror filling pattern with arbitrarily tight positive Ricci pinching and no Einstein metric of any sign;
- one negative-mirror filling pattern with arbitrarily tight negative Ricci pinching and no Einstein metric of any sign;
- the already available `S^1×S^3` argument for boundary/zero-crossing intervals.

This is a downward revision of the value of further all-sign nonexistence hunting on only the positive mirror: even a complete no-Einstein theorem there would refute `P_4^+`, but not the full original interval statement.

## 3. The exact no-gap variational formulation

For any closed oriented four-manifold define
\[
F(g)=\int_M\left(|W_g|^2+\frac{s_g^2}{24}\right)dV_g.
\]
The four-dimensional Chern--Gauss--Bonnet identity gives
\[
8\pi^2χ(M)=\int_M\left(|W|^2-\frac12|E|^2+\frac{s^2}{24}\right)dV,
\qquad E=Ric-\frac{s}{4}g,
\]
hence
\[
F(g)=8\pi^2χ(M)+\frac12\int_M |E_g|^2dV_g\ge8\pi^2χ(M).
\]
Equality holds iff `E=0`, and in dimension four the contracted Bianchi identity then forces `s` to be constant, so the metric is Einstein. Thus on any closed 4-manifold:
\[
\text{Einstein metric exists}\quad\Longleftrightarrow\quad F\text{ attains its lower bound }8\pi^2χ.
\]

The audited `A_1` families make this lower bound sharp on every fixed filling pattern they cover. Since `||Ric-σg||_{op}→0` and the construction has bounded volume, `∫|E|^2→0`; therefore
\[
\inf F=8\pi^2χ
\]
on each positive- and negative-mirror mixed row.

The energy ledger is exact. The orbifold part has orbifold Euler characteristic `χ_orb=2`, hence contributes `8π²χ_orb=16π²`. Each Eguchi--Hanson bubble contributes
\[
8\pi^2(2-1/2)=12\pi^2
\]
in the adopted convention. The positive mirror has four bubbles:
\[
16\pi^2+4\cdot12\pi^2=64\pi^2=8\pi^2\cdot8.
\]
The negative mirror has 36 bubbles:
\[
16\pi^2+36\cdot12\pi^2=448\pi^2=8\pi^2\cdot56.
\]
These equalities are recorded numerically in `step84_interval_variational_audit.json`.

This explains a pattern in Steps 78--82. Gursky, Gursky--LeBrun, Bishop, Chern--Weil, and crude alignment estimates all leave slack because there is no integral energy gap to find: the degeneration already saturates the exact closed-manifold lower bound. Any obstruction based only on a lower bound for `F`, `∫|W^±|^2`, scalar energy, or Bishop volume cannot separate a mixed row from its own orbifold-plus-EH degeneration.

## 4. What the variational instrument can and cannot currently do

The attainment formulation is genuinely different from local Biquard/Ozuch coefficients or monopole obstructions. It is global, sign-neutral, and PSC-compatible. It could in principle prove existence by a direct-method/concentration-compactness theorem, or prove nonexistence by showing every minimizing sequence necessarily degenerates to the fixed orbifold bubble tree and no smooth minimizer occurs.

However existing compactness sources do **not** already supply this conclusion.

- Anderson's orbifold compactness theorem `\cite{anderson2003orbifold}` assumes unit volume, global `L^{n/2}` full-curvature energy, noncollapse, and a small-curvature estimate; the theorem gives orbifold compactness, not smooth attainment for arbitrary almost-minimizers.
- Tian--Viaclovsky `\cite{tian2003moduli}` prove compactness for critical metrics in selected elliptic classes (half-conformally-flat constant-scalar, harmonic-curvature, and Kähler constant-scalar metrics) under Sobolev, `L^2(Rm)`, volume, and `b_1` hypotheses. Their theorem is not a Palais--Smale theorem for arbitrary sequences with `F(g_j)→8π²χ`.
- Gursky--Viaclovsky `\cite{gursky2015rigidity}` give local rigidity/stability/minimization near Einstein metrics for quadratic functionals such as `∫|Ric|²+τ∫R²`; this is local and spectral, not global compactness or global attainment on the mixed rows.

So the variational route is not a solved theorem. Its honest next mathematical form is a new Palais--Smale/concentration-compactness program for
\[
\int |E|^2 = 2F-16\pi^2χ,
\]
possibly after Ekeland selection of almost-critical minimizing sequences, volume normalization, gauge fixing, and proof of a suitable epsilon-regularity theory for almost-critical metrics. The decisive questions are:

1. Can every `F`-minimizing sequence on a fixed mixed row be replaced by an almost-critical one with enough Sobolev/noncollapse control to enter Anderson/Tian--Viaclovsky-style compactness?
2. If compactness holds, does it produce a smooth Einstein minimizer or only an orbifold-plus-ALE bubble tree?
3. Can the exact energy saturation and topological attachment data force one of these alternatives?
4. How do collapse and zero-volume concentration escape this framework, especially since `F` is scale-invariant?

A positive answer to (1)--(3) could decide the fixed-row Einstein problem in either direction. A negative answer would explain why the mixed rows evade not only integral estimates but also global variational compactness.

## 5. Consequence for next work

The Step 83 construction should now be treated as a theorem-grade staged result, but not as a Yau--26 solution. The corrected dimension-four reduction is:

- boundary and zero-crossing intervals are defeated by `S^1×S^3`;
- strict positive intervals reduce to `P_4^+`, with audited positive-mirror near-pinched rows as the strongest tests;
- strict negative intervals reduce to `P_4^-`, with the negative genus-2 mirror now also covered by the audited construction;
- full dimension-four refutation requires no-Einstein-of-any-sign results on both a positive-mirror and a negative-mirror row;
- full dimension-four proof requires one strict normalized branch to hold for every closed 4-manifold.

The most valuable frontier is no longer another local Green coefficient unless it demonstrably enters exact Einstein existence near the product degeneration. A more promising distinct instrument is the `F`-attainment/concentration-compactness program above, but it must be pursued as a serious PDE compactness problem, not as a tautological restatement that `F` is minimized iff Einstein. In parallel, the all-dimensional goal still requires structural work for `n≥5`; current product propagation gives examples, not a reduction or proof.
