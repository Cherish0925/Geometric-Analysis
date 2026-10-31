# Step 39: self-improving first-exit theorem

> **Supersession notice (Step 40).** This is a conditional first-exit architecture,
> not a proved flow theorem.  Its Step 1 invokes Step 39 Theorem 8.1, whose
> arbitrary-order continuation induction is invalid as written.  Step 40 proves
> the m=2 coupled repair and the preceding order-one unweighted \(\nabla T\)
> estimate, but higher orders and the transported-coefficient existence theorem
> remain to be established.  Statements below asserting that Layers A--D are
> complete or that only terminal geometry remains are withdrawn.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Conditional proposed statement

**Theorem (Self-improving first-exit).** Let $(M^4,g_0)$ be a closed
four-manifold with a fixed macro-disjoint buffered support system
$(B_r(p_j),\chi_j,\eta_j)$ satisfying:

- $a=\sum_j\chi_j^2$ with $\chi_j\ge0$, $\|d\chi_j\|_\infty\le C/r$,
  $\|\nabla^2\chi_j\|_\infty\le C/r^2$;
- $\operatorname{supp}\chi_j\subset B_{5r}(p_j)$ and $\chi_j\equiv1$ on
  $B_{4r}(p_j)$;
- auxiliary $\eta_j\equiv1$ on $B_{6r}(p_j)\supset\operatorname{supp}\chi_j$,
  with $a=da=0$ on $\operatorname{supp}d\eta_j$;
- the $B_{6r}(p_j)$ are pairwise disjoint (coloured separation, Step 30).

Suppose the initial datum $g_0$ satisfies:
$$
K_{2,j}(0)=\int_{B_{6r}(p_j)}\eta_j^2F_0^2\,d\mu_0\le K_0V_j(0),
\qquad
J_{6,j}(0)=\int_{B_{6r}(p_j)}\eta_j^2a_j^4|E_0|^6\,d\mu_0\le\delta^6V_j(0),
\tag{0.1}
$$
where $V_j(0)=\operatorname{Vol}_{g_0}(B_{6r}(p_j))$ and $\gamma_0=Cr^2\sqrt{K_0}\ll1$.

Then the transported-coefficient DeTurck system (Step 37) produces a smooth
solution $g(t)$ of $\partial_tg=-2aE$ on $[0,\theta r^2]$, with $\theta>0$
depending only on $K_0,r$ and dimension, such that:

(a) **Metric comparability:** $e^{-C\delta\theta^{2/3}r^2}g_0\le g(t)\le e^{C\delta\theta^{2/3}r^2}g_0$.

(b) **Sobolev comparability:** $\mathcal S_j(t)\le 2\mathcal S_j(0)$, hence
$\gamma_j(t)\le 2\gamma_0$.

(c) **Curvature control:**
$$
\sup_{t\le\theta r^2}K_{2,j}(t)\le CK_{2,j}(0),
\qquad
Y_j(t)=\int\eta_j^2a_jF^3\le C\gamma_0K_{2,j}(0)/t,
$$
$$
\|a_jF(t)\|_\infty\le C\gamma_0/t.
$$

(d) **Defect control:**
$$
J_{6,j}(t)\le C\delta^6V_j(0),
\qquad
\|a_jE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
$$
$$
\int_0^{\theta r^2}\|a_jE(t)\|_\infty\,dt\le C\delta\theta^{2/3}r^2.
$$

(e) **Global defect:** $Q(t)=\int_M|E|^2\le e^{C\theta}Q(0)$.

(f) **Smooth extension:** the solution is smooth on $(0,\theta r^2]$, with
all derivatives bounded on each compact subinterval.

The constants $C$ depend only on dimension, $K_0r^2$, and the cutoff
parameter; they are independent of the manifold topology, the collapse
volume $V_j$, or the initial defect $\delta$.

## 1. Proof architecture

The proof is a **continuity argument in the exit time**. Define
$$
T^*=\sup\bigl\{T\in(0,\theta_0r^2]:\text{(a)--(e) hold on }[0,T]
\text{ with constants }2C_0\bigr\},
$$
starting from $\theta_0$ to be chosen. At $t=0$, (a)--(e) hold with constants
$C_0/2$, so $T^*>0$ by continuity.

**Step 1: Existence on $[0,T^*]$.** The transported-coefficient DeTurck system
(Step 37) gives short-time smooth existence. On $[0,T^*]$, $|U|\le\|aF\|_\infty
\le C\gamma_0/t$. For any $\varepsilon>0$, $|U|$ is bounded on $[\varepsilon,T^*]$.
The continuation induction (Step 39 Theorem 8.1) gives all-derivative pointwise
bounds on $[\varepsilon,T^*]$. By Arzelà-Ascoli, the solution extends past $T^*$
if $T^*<\theta_0r^2$.

**Step 2: Recovery of (a) from (d).** The metric evolves by
$\partial_tg=-2aE$, so
$$
|g(t)-g(0)|\le\int_0^t2|aE|\,ds\le C\delta\theta^{2/3}r^2
$$
by the drift estimate. For $\delta$ small enough (depending only on $\theta$),
this gives metric comparability with constant $<2C_0$.

**Step 3: Recovery of (b) from (a).** The Sobolev constant
$\mathcal S\simeq r^2/\sqrt{V}$ changes by the metric and volume variation.
By (a), $V(t)\ge e^{-C\delta}V(0)$ and the Sobolev form changes by
$e^{C\delta}$. For $\delta$ small, $\mathcal S(t)\le(1+C\delta)\mathcal S(0)$.

**Step 4: Recovery of (c) from the $q=2,3$ estimates.** Given (a)--(b), the
curvature power inequality (A01 Step 35) and $q=2$ absorption (Step 38 §4)
give $K_2$ persistence. The $q=3$ equation with good-slice propagation gives
$Y(t)\le C\gamma K_2/t$. The curvature Moser iteration gives
$\|aF(t)\|_\infty\le C\gamma/t$. All with $\gamma\le2\gamma_0$.

**Step 5: Recovery of (d) from the defect estimates.** Given (b)--(c),
$J_6$ persistence (Step 35) gives $J_6(t)\le C\delta^6V$. The general-$p$
defect power inequality (Step 39 Theorem 7.1) and the defect Moser iteration
give $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$. The drift integral is
$C\delta\theta^{2/3}r^2$.

**Step 6: Recovery of (e).** The global $Q$ persistence (Step 37) gives
$Q(t)\le e^{C\theta}Q(0)$, using the same Sobolev and $K_2$ inputs.

**Step 7: Improvement.** If $T^*<\theta_0r^2$, the recovered constants at
$T^*$ are strictly better than $2C_0$ (they are $C_0(1+C\delta)$), so the
solution can be extended past $T^*$ while maintaining (a)--(e), contradicting
the definition of $T^*$. Hence $T^*=\theta_0r^2$.

## 2. The output

At the terminal time $\theta r^2$, the controlled metric produces:

- A bounded-curvature plateau on the strict centers $B_r(p_j)$, where $a=1$
  and the Moser endpoint gives $|F(t)|\le C\gamma/t$.
- An Einstein-defect bound
  $\int|E(\theta r^2)|^2\le e^{C\theta}Q(0)$ globally, and locally the
  calibration inequality
  $$
  \int\left(|W^+|-\frac1{2\sqrt6}\right)^2\le\frac7{24}Q(\theta r^2)
  \le CQ(0).
  $$
- Controlled Weyl-modulus and monopole data on the plateau, suitable for the
  exponential-pullback chart selection of Step 29.

The subsequent terminal geometric passage (Steps 3-6, 29-30) then produces
the contradiction: the selected Einstein germ has the forbidden calibrated
$W^+$-spectrum, completing the per-manifold gap for a single critical
Ishida-LeBrun four-manifold.

## 3. Circularity check

The only quantity that could create circularity is the Sobolev constant, which
depends on the evolving metric. The chain is:

$$
\text{drift bound (d)} \Rightarrow \text{metric bound (a)}
\Rightarrow \text{Sobolev bound (b)}
\Rightarrow \text{curvature/defect bounds (c)+(d)}.
$$

The drift bound uses $\|aE\|_\infty$, which uses the Moser iteration,
which uses $\mathcal S^2Y$ and the general-$p$ inequality, which uses
$\mathcal S$ and $K_2$.

The self-improvement works because the drift is proportional to $\delta$:
making $\delta$ small enough makes the metric and Sobolev variation
arbitrarily small, while the curvature constants ($K_0$, $\gamma_0$) are
fixed initial data. This is the collapse-independent mechanism.

## 4. Status

This first-exit theorem is written as a proof structure, with each component
proved in the referenced notes. What remains to make it a fully written
theorem:

1. Collect all the conditional lemmas into one self-contained document
   (potentially a paper draft).
2. Verify the terminal geometric passage as a single connected argument.
3. Extend from a single critical manifold to the full Ishida-LeBrun family.

These include unresolved mathematical mechanisms, not merely organization.
The general-p defect inequality is retained, but arbitrary-order continuation,
transported-coefficient existence, and the terminal geometric passage remain
unfinished for the restricted four-dimensional negative route.
