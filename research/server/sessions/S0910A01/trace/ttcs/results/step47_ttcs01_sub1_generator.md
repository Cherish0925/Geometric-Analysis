# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md",
    "Knowledge/objects/papers/Farrell-Jones-spheres-and-inertia-groups-of-complex-projective-spaces--acfe469446a9--8fe24450b510/object.md",
    "Sessions/S0910A01/staging/acquired/Volume_entropy_and_rigidity_for_𝖱𝖢𝖣-spaces_97042f61708bf34d/part_001.md",
    "Sessions/S0910A01/staging/acquired/Extended_graph_4-manifolds__and_Einstein_metrics_36ca3f274012faba/content.md"
  ]
}
```

## Task

Using the Step 47 note and the actual sources, develop the strongest scientifically useful next formulations for the entropy/global-volume and exotic-smooth-structure directions toward the full Yau 26 proposition. In particular: (i) determine what normalized topology/entropy margin would be required for a uniform varying-target negative pinching theorem beyond fixed X; (ii) analyze whether Farrell--Jones real-hyperbolic exotic smoothings could become a strict counterexample route, separating what topology rules out for positive/zero/negative Einstein constants and what remains unknown; (iii) propose a few load-bearing theorem statements or calculations that would materially decide these routes. Do not invent literature or assert a no-Einstein theorem absent from the files.

## Output

The most useful global quantity is not the additive Euler defect, but its ratio to the hyperbolic volume represented by the map.

### 1. The normalized margin required when the target varies

Let \(f:Y^4\to X^4\) have degree \(k\ne 0\), where \(X\) is real hyperbolic with sectional curvature \(-1\). Put

\[
q_\chi(f):=\frac{\chi(Y)}{|k|\chi(X)},\qquad
R_{\mathrm{Ric}}(f):=
\frac{\operatorname{Vol}_{\mathrm{Ric}}(Y)}
{|k|\operatorname{Vol}(X)} .
\]

BCG gives \(R_{\mathrm{Ric}}(f)\ge 1\). For a metric satisfying

\[
\bigl\|g^{-1}(\operatorname{Ric}_g+g)\bigr\|_{\infty,\mathrm{op}}\le \delta,
\]

the Step 47 calculation, after setting \(g'=(1+\delta)g/3\), gives

\[
R_{\mathrm{Ric}}(f)
\le
\frac{\operatorname{Vol}_{g'}(Y)}
{|k|\operatorname{Vol}(X)}
\le
q_\chi(f)F(\delta),
\qquad
F(\delta)=
\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\tag{1}
\]

Thus the exact normalized quantity controlling a varying-target family
\(\mathcal C\) is

\[
\Gamma(\mathcal C):=
\inf_{f\in\mathcal C}
\frac{R_{\mathrm{Ric}}(f)}{q_\chi(f)}.
\tag{2}
\]

If \(\Gamma(\mathcal C)>1\), then no member of \(\mathcal C\) carries such a metric whenever

\[
F(\delta)<\Gamma(\mathcal C).
\]

The corresponding explicit threshold is

\[
\delta<
\delta_*(\Gamma):=
\frac{\sqrt{\Gamma(1+3\Gamma)}-(1+\Gamma)}
{1+2\Gamma}.
\tag{3}
\]

This isolates precisely what a dimension-only varying-target theorem would require: a fixed multiplicative separation of \(R_{\mathrm{Ric}}(f)\) from \(q_\chi(f)\). An additive Euler discrepancy or additive volume excess is insufficient because the error in (1) is proportional to \(\operatorname{Vol}(X)\).

A purely topological version follows immediately. If

\[
q_\chi(f)\le 1-\alpha
\qquad\text{for one fixed }\alpha>0,
\]

then \(R_{\mathrm{Ric}}\ge1\) yields \(\Gamma\ge(1-\alpha)^{-1}\), and pinching is impossible for

\[
\delta<
\delta_\alpha:=
\frac{-2+\alpha+\sqrt{4-\alpha}}{3-\alpha}
=\frac{\alpha}{4}+O(\alpha^2).
\tag{4}
\]

This is a target-independent theorem already contained in CGB+BCG: the necessary topological input is a relative Euler shortfall, not a fixed integer shortfall.

There is an entropy analogue. Define the scale-invariant quantity

\[
R_{\mathrm{ent}}(f):=
\inf_g
\frac{h(g)^4\operatorname{Vol}_g(Y)}
{3^4|k|\operatorname{Vol}(X)}.
\]

BCG gives \(R_{\mathrm{ent}}\ge1\). For \(g'\) in (1), Bishop comparison gives \(h(g')\le3\), hence

\[
R_{\mathrm{ent}}(f)\le q_\chi(f)F(\delta).
\]

Consequently a uniform entropy formulation is

\[
\inf_{f\in\mathcal C}
\frac{R_{\mathrm{ent}}(f)}{q_\chi(f)}>1.
\tag{5}
\]

Either (2) or (5) supplies the required normalized margin. BBCG supplies a positive excess for each fixed target, but its own Farrell–Jones discussion shows that no such excess can be uniform over all noncovering maps and all hyperbolic targets. The recent RCD stability theorem likewise retains a diameter parameter; covers of increasing volume necessarily leave every fixed-diameter family.

For \(Y=X\# X\), with the degree-two map to \(X\),

\[
q_\chi=1-\frac1{\chi(X)}.
\]

BBCG Corollary 1.7 gives

\[
R_{\mathrm{Ric}}\ge1+\varepsilon(X).
\]

Thus the exact varying-\(X\) margin needed here is

\[
\inf_X
\frac{1+\varepsilon(X)}
{1-1/\chi(X)}>1.
\tag{6}
\]

The known information only says \(\varepsilon(X)>0\) separately for each \(X\). Since \(1/\chi(X)\to0\) along large covers, neither term currently supplies a fixed separation.

---

## 2. Farrell–Jones exotic smoothings and the three Einstein signs

The real-hyperbolic Farrell–Jones construction recalled by BBCG supplies finite covers \(X_i\) and exotic smoothings

\[
Y_i=X_i\#\Sigma
\]

that are homeomorphic but not diffeomorphic to \(X_i\), together with metrics whose sectional curvatures approach \(-1\). If

\[
-1-\epsilon_i\le K_{g_i}\le -1+\epsilon_i,
\]

then for every unit vector \(v\),

\[
\operatorname{Ric}_{g_i}(v,v)
=\sum_{j=2}^{n}K(v,e_j),
\]

so

\[
\left\|
g_i^{-1}\bigl(\operatorname{Ric}_{g_i}+(n-1)g_i\bigr)
\right\|_{\mathrm{op}}
\le (n-1)\epsilon_i.
\tag{7}
\]

Thus these are genuine tight Ricci-pinching examples, not merely sectional-curvature examples.

The topology of \(Y_i\) settles two Einstein signs:

* If \(\lambda>0\), Bonnet–Myers would make \(\pi_1(Y_i)\) finite, while \(\pi_1(Y_i)\cong\pi_1(X_i)\) is an infinite hyperbolic lattice.
* If \(\lambda=0\), Bishop–Gromov applied to the universal cover gives polynomial volume growth, hence polynomial deck-group growth. Hyperbolic lattices have exponential growth.

The unresolved sign is \(\lambda<0\). An exotic smoothing cannot carry a locally symmetric real-hyperbolic metric, but it could in principle carry a different Einstein metric with Weyl curvature. Mostow rigidity does not turn an arbitrary Einstein metric into a real-hyperbolic one.

After normalizing any such metric \(h\) by

\[
\operatorname{Ric}_h=-(n-1)h,
\]

BCG gives only

\[
\operatorname{Vol}_h(Y_i)\ge \operatorname{Vol}(X_i),
\tag{8}
\]

with equality forcing the hyperbolic metric and hence the standard smoothing. A strict excess in (8) is fully compatible with all presently supplied sources. The auxiliary almost-hyperbolic metric \(g_i\) controls an infimum over all metrics with a Ricci lower bound; it does not control the volume of a potentially remote Einstein metric \(h\).

This missing \(\lambda<0\) statement is therefore exact and substantial:

> **Einstein smooth rigidity for hyperbolic homotopy types.**  
> If a closed smooth \(n\)-manifold \(M\) is homotopy equivalent to a closed real-hyperbolic \(n\)-manifold \(X\), and \(M\) carries \(h\) with
> \(\operatorname{Ric}_h=-(n-1)h\), then \(h\) has sectional curvature \(-1\).

This theorem would make every Farrell–Jones exotic member Einstein-free, since the other two signs are already excluded topologically.

There is a complete four-dimensional model for this statement. If \(M^4\) is homeomorphic to a real-hyperbolic \(X^4\) and \(h\) satisfies \(\operatorname{Ric}_h=-3h\), then \(\chi(M)=\chi(X)\) and \(\tau(M)=0\). The Einstein CGB/signature estimate used by LeBrun gives

\[
2\chi(M)\ge \frac{3}{2\pi^2}\operatorname{Vol}_h(M),
\]

hence

\[
\operatorname{Vol}_h(M)
\le \frac{4\pi^2}{3}\chi(X)
=\operatorname{Vol}(X).
\]

BCG gives the reverse inequality, so equality holds and \(h\) is real hyperbolic. The higher-dimensional Farrell–Jones examples lie outside this four-dimensional CGB mechanism; Di Cerbo’s discussion explicitly emphasizes how little is known about Einstein nonexistence in dimensions at least five.

### Quantifier effect on Yau 26

Suppose the missing \(\lambda<0\) theorem were established for the real Farrell–Jones sequence. Then the metrics in (7), after constant rescaling, fit every interval

\[
c<C,\qquad c<0.
\]

Indeed choose any \(\mu\in(c,\min\{C,0\})\), rescale so that the central Ricci eigenvalue is \(\mu\), and require

\[
\epsilon_i<
\min\left\{
\frac{\mu-c}{-\mu},
\frac{C-\mu}{-\mu}
\right\}.
\]

When \(c<C<0\), the optimal relative width is

\[
\frac{C-c}{-c-C}.
\]

Thus Einstein-free Farrell–Jones examples would exclude every proposed Yau interval whose lower endpoint is below zero. They do not provide metrics satisfying \(0\le\operatorname{Ric}\le Cg\) or \(0<c\,g\le\operatorname{Ric}\), since their fundamental groups already prevent such metrics. The \(c_n\ge0\) branch therefore requires a separate family.

The complex-hyperbolic source in dimensions \(14\) and \(16\) does not by itself give tight Ricci pinching. The stated sectional interval

\[
[-4-\epsilon,-1+\epsilon]
\]

only implies the broad estimate

\[
-(n-1)(4+\epsilon)g
\le \operatorname{Ric}
\le -(n-1)(1-\epsilon)g,
\]

whose relative width does not tend to zero. The primary Farrell–Jones complex-hyperbolic construction would need the stronger tensor estimate

\[
\left\|
g_\epsilon^{-1}
\bigl(\operatorname{Ric}_{g_\epsilon}+\kappa_n g_\epsilon\bigr)
\right\|_{\infty,\mathrm{op}}\longrightarrow0
\tag{9}
\]

for the appropriate complex-hyperbolic Einstein constant \(\kappa_n\). The supplied Kasilingam theorem does not state (9).

---

## 3. Especially decisive theorem shapes and calculations

### A. Sparse connected sums in dimension four

Define the scale-invariant lower-sign Ricci defect

\[
\mathfrak p(M):=
\inf_{a>0,\;g}
\left\|
a^{-1}g^{-1}(\operatorname{Ric}_g+a g)
\right\|_{\infty,\mathrm{op}}.
\]

For \(M=X\#X\), CGB+BCG gives

\[
\mathfrak p(X\#X)\ge
\frac{-2+\chi(X)^{-1}+\sqrt{4-\chi(X)^{-1}}}
{3-\chi(X)^{-1}}
\sim \frac1{4\chi(X)}.
\tag{10}
\]

Every \(X\#X\) here carries no Einstein metric:

* \(\lambda>0\) is excluded by its infinite fundamental group.
* \(\lambda=0\) is excluded by exponential group growth.
* For \(\lambda<0\), scale to \(\operatorname{Ric}=-3g\). The degree-two map to \(X\) and BCG give
  \(\operatorname{Vol}_g(X\#X)\ge2\operatorname{Vol}(X)\). But
  \[
  2\chi(X\#X)=4\chi(X)-4,
  \]
  whereas LeBrun’s Einstein estimate would require
  \[
  4\chi(X)-4
  \ge
  \frac{3}{2\pi^2}\,2\operatorname{Vol}(X)
  =4\chi(X),
  \]
  an impossibility.

Therefore either of the following results would be highly consequential:

\[
\inf_X\mathfrak p(X\#X)>0,
\tag{11}
\]

or a construction of covers \(X_i\) and metrics \(g_i\) on \(X_i\#X_i\) with

\[
\mathfrak p(X_i\#X_i)\longrightarrow0.
\tag{12}
\]

Statement (12) would give a four-dimensional Einstein-free sequence with arbitrarily tight Ricci pinching, avoiding the unresolved high-dimensional Einstein question attached to exotic spheres. Estimate (10) shows that the known global formulas permit exactly this asymptotic possibility.

A simple neck computation explains why (12) is nontrivial. For a rotational metric

\[
dr^2+f(r)^2g_{S^3},
\]

at a throat with \(f'=0\), set \(x=f''/f\) and \(y=2/f^2\ge0\). The Ricci eigenvalues are

\[
\lambda_r=-3x,\qquad \lambda_t=y-x.
\]

Relative to the target \(-3g\),

\[
\inf_{x\ge0,\;y\ge0}
\frac1{3}
\max\{\,|-3x+3|,\ |y-x+3|\,\}
=\frac12.
\tag{13}
\]

Thus an ordinary rotational connected-sum neck cannot yield tight Ricci pinching. Any realization of (12) would need an anisotropic or globally distributed transition rather than a standard warped throat.

### B. Higher-dimensional Einstein volume rigidity

A sharp sufficient theorem for the Farrell–Jones route is

\[
M\simeq X,\quad
\operatorname{Ric}_h=-(n-1)h
\quad\Longrightarrow\quad
\operatorname{Vol}_h(M)\le\operatorname{Vol}(X).
\tag{14}
\]

Together with BCG, (14) forces equality and a hyperbolic metric. In four dimensions, (14) is exactly what CGB and the signature formula provide. In higher dimensions it would require a new Einstein curvature integral, a sharp simplicial-volume inequality specialized to Einstein metrics, or another mechanism controlling the Weyl contribution.

Another sufficient formulation is maximal entropy:

\[
M\simeq X,\quad
\operatorname{Ric}_h=-(n-1)h
\quad\Longrightarrow\quad
h(h)=n-1.
\tag{15}
\]

Known maximal-entropy rigidity would then force the universal cover of \(h\) to be real hyperbolic. Neither (14) nor (15) follows from the supplied sources.

### C. Exact asymptotics of Farrell–Jones metrics

For the real-hyperbolic sequence, the most informative quantitative package is

\[
\epsilon_i\to0,\qquad
\frac{\operatorname{Vol}(Y_i,g_i)}
{\operatorname{Vol}(X_i)}\to1,\qquad
\frac{\operatorname{diam}(X_i)}
{\text{hyperbolic scale}}\to\infty,
\tag{16}
\]

together with the Ricci estimate (7). BBCG qualitatively uses precisely this phenomenon to explain the diameter dependence of its rigidity constant. Explicit rates relating pinching, cover degree, diameter, and volume excess would determine how rapidly every normalized global margin degenerates.

For the complex-hyperbolic examples, the decisive calculation is (9), which requires the primary construction rather than the sectional interval quoted by Kasilingam.

In summary, global volume methods reduce the varying-target issue to the multiplicative ratio \(R/q_\chi\), while the Farrell–Jones route reduces to Einstein smooth rigidity for the \(\lambda<0\) sign. The four-dimensional family \(X\#X\) offers a second route where Einstein nonexistence is already complete and the sole hard quantity is the asymptotic Ricci defect in (12).