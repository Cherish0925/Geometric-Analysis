# Step 37: global unweighted defect energy Q(t) persistence

## 0. Purpose

Prove, as a standalone first-exit component, that the unweighted global defect
$$
Q(t) = \int_M |E(t)|^2\,d\mu_{g(t)},
\qquad E=\operatorname{Ric}_g+g,
\tag{0.1}
$$
persists from time zero on the first-exit interval for the normalized cutoff flow
$\partial_t g=-2a E$, $a=\chi^2$, on a closed 4-manifold $M$.

This note addresses the Step 36 Preceptor correction (§4): neither $J_6$ nor
$\|aE\|_\infty$ replaces $Q$, because near $\{a=0\}$ the weighted quantities can
be small while $|E|^2$ is large. The terminal calibration requires the
unweighted inequality
$$
\int\!\Big(|W^+|-\tfrac1{2\sqrt6}\Big)^2\,d\mu
\le\tfrac7{24}\!\int\!|E|^2\,d\mu = \tfrac7{24}\,Q,
$$
so $Q$ must be controlled independently.

The template is from the Step 23 homogeneous $Q$ derivation
(`step23_single_support_wang_bridge.md` §5.1, eqs. 5.1--5.3) and A01's Step 20
triangular defect energy.

## 1. Setting and hypotheses

Throughout, the same first-exit provisional geometry holds on $[0,\theta r^2]$:

- **Smooth solution** of $\partial_t g=-2a E$ from the transported-DeTurck
  existence theorem (`step37_transported_deturck_existence.md`).
- **Disjoint support collection** $\{U_j\}$ with cutoffs $\chi_j$,
  $a=\sum\chi_j^2$, active regions $B_{5r}(p_j)$, Sobolev domains
  $B_{6r}(p_j)$ disjoint, $|d\chi_j|\le Cr^{-1}$.
- **Metric comparability**: all metrics within bilipschitz ratio $e^{C_0\theta}$
  of the initial metric on $[0,\theta r^2]$ (controlled by metric drift, itself
  depending on $\|aE\|_\infty$ integrability — a separate first-exit component).
- **Small local curvature product**: $\gamma_j(t)=\mathcal S_j(t)K_{2,j}(t)^{1/2}
  \le \gamma_0\ll1$ on each support throughout the interval. Here
  $K_{2,j}=\int_{U_j}\eta_j^2 F^2$ and $\mathcal S_j$ is the local Sobolev
  constant for $L^2\hookrightarrow L^4$ on $B_{6r}(p_j)$ with respect to
  $g(t)$.

## 2. Defect equation structure

The squared-norm identity for $E$ is homogeneous:
$$
(\partial_t-a\Delta)|E|^2
= -2a|\nabla E|^2 + a\,\operatorname{Rm}*E*E
  + \nabla^2 a*B_0(E),
\tag{2.1}
$$
where $B_0^{ij}=2g^{ij}|E|^2+2(\operatorname{tr}E)E^{ij}-4E^{ik}E_k{}^j$ is the
quadratic Hessian-$a$ contraction (same as in the $J_6$ lemma). The metric
measure evolution gives $\partial_t(d\mu)=-\operatorname{tr}_g(aE)\,d\mu$,
contributing $-a(\operatorname{tr}E)|E|^2$, which is absorbed into the bounded
reaction.

The key property: **no curvature-only source appears**. Every term contains at
least one power of $E$, so $E=0$ (i.e. exact negative Einstein) is preserved
exactly.

## 3. Integrated global estimate

Integrate (2.1) against $d\mu_t$ over $M$:
$$
Q'(t) + 2\!\int_M\! a|\nabla E|^2\,d\mu
= \underbrace{\int_M a\,\operatorname{Rm}*E*E\,d\mu}_{I_1}
  + \underbrace{\int_M \nabla^2 a\cdot B_0(E)\,d\mu}_{I_2}
  + \text{measure term}.
\tag{3.1}
$$
The measure term is $-\int a(\operatorname{tr}E)|E|^2\le C\int a|E|^3\le C(Q+I_1)$
(by interpolation and Hölder); we absorb it into the treatment of $I_1$ and $I_2$.

### Term $I_2$: cutoff Hessian

Integrate by parts once:
$$
I_2 = -\int_M \nabla_k a\cdot \nabla_k\big(B_0(E)\big)\,d\mu
      + \text{boundary (none, }M\text{ closed)}.
$$
Since $|B_0|\le C|E|^2$ and $|\nabla B_0|\le C|E||\nabla E|$:
$$
|I_2|\le C\int_M |da||E||\nabla E|\,d\mu
\le \varepsilon\int_M a|\nabla E|^2 + C_\varepsilon\int_M\frac{|da|^2}{a}|E|^2.
\tag{3.2}
$$
Now $|da|^2/a = 4\chi^2|d\chi|^2/\chi^2 = 4|d\chi|^2$, and
$|d\chi_j|\le Cr^{-1}$ on each support, so
$$
|I_2|\le \varepsilon\int_M a|\nabla E|^2 + Cr^{-2}Q.
\tag{3.3}
$$

### Term $I_1$: curvature potential, support-by-support

Decompose over the disjoint supports:
$$
I_1 = \sum_j\int_{U_j}\chi_j^2|\operatorname{Rm}|\,|E|^2\,d\mu
      + \int_{\{a=0\}}0 = \sum_j I_{1,j}.
$$
On each support $U_j$, use $F=(1+|\operatorname{Rm}|^2)^{1/2}$ and write
$\chi_j^2F|E|^2 = F\cdot(\chi_jE)^2$:
$$
I_{1,j}\le \int_{U_j}F(\chi_jE)^2\,d\mu
\le \|F\|_{L^2(U_j)}\|\chi_jE\|_{L^4(U_j)}^2.
\tag{3.4}
$$
Apply the local Sobolev inequality on $B_{6r}(p_j)$:
$$
\|\chi_jE\|_4^2
\le C\mathcal S_j\Big(\int_{U_j}\chi_j^2|\nabla E|^2+|\nabla\chi_j|^2|E|^2\,d\mu\Big)
\le C\mathcal S_j\Big(\int_{U_j}a|\nabla E|^2+r^{-2}\int_{U_j}|E|^2\Big).
\tag{3.5}
$$
Hence
$$
I_{1,j}\le C\gamma_j\Big(\int_{U_j}a|\nabla E|^2+r^{-2}\int_{U_j}|E|^2\Big),
\qquad \gamma_j=\mathcal S_j K_{2,j}^{1/2}.
\tag{3.6}
$$
Summing over $j$ (supports disjoint, hence integrals additive):
$$
I_1\le C\gamma_*\Big(\int_Ma|\nabla E|^2+r^{-2}Q\Big),
\qquad \gamma_*=\max_j\gamma_j.
\tag{3.7}
$$

### Absorption and Grönwall

Combining (3.1), (3.3), (3.7), choosing $\varepsilon$ small:
$$
Q' + (2-\varepsilon-C\gamma_*)\int_Ma|\nabla E|^2
\le C(1+\gamma_*)r^{-2}Q.
\tag{3.8}
$$
Under the first-exit hypothesis $\gamma_*\le\gamma_0\ll1$:
$$
Q'(t)\le Cr^{-2}Q(t),
\tag{3.9}
$$
and therefore
$$
\boxed{Q(t)\le e^{Cr^{-2}t}\,Q(0)
\le e^{C\theta}\,Q(0)
\qquad\text{for }t\le\theta r^2.}
\tag{3.10}
$$

## 4. Initial data

Pointwise Ricci pinching $\|g^{-1}E\|_\infty\le\delta$ gives
$|E|^2\le C\delta^2$ everywhere, hence
$$
Q(0)\le C\delta^2\operatorname{Vol}(M,g_0).
$$
Combined with (3.10):
$$
Q(T)\le C\delta^2\operatorname{Vol}(M,g_0)\cdot e^{C\theta}.
\tag{4.1}
$$
For fixed first-exit parameters, $Q(T)=O(\delta^2)$, which is what the
$7/24$ calibration inequality needs.

## 5. Role in the first-exit bootstrap

The roles of the three defect controls are:

| Control | Definition | Feeds |
|---------|-----------|-------|
| $Q(t)$ | $\int_M\|E\|^2\,d\mu$ | terminal Chern–Weil/monopole calibration |
| $J_6(t)$ | $\int\eta^2a^4\|E\|^6\,d\mu$ | defect Moser iteration to $\|aE\|_\infty$ |
| $\|aE(t)\|_\infty$ | pointwise weighted defect | metric drift and moving Sobolev |

These are logically independent first-exit components. $Q$ is the only one that
uses global unweighted integration and hence the only one capable of feeding the
global calibration inequality.

## 6. Remarks on the outside region

On $\{a=0\}$ the flow velocity $\partial_tg=-2aE=0$, so $g(t)=g_0$ there.
The contribution from $\{a=0\}$ to $Q$ is fixed:
$$
\int_{\{a=0\}}|E_0|^2\,d\mu_0 = \text{const}.
$$
The evolution of $Q$ is driven entirely by the active supports $\{a>0\}$. Thus
the estimate (3.8) decomposes as
$$
Q'_{\operatorname{active}}+\cdots\le Cr^{-2}Q_{\operatorname{active}},
\qquad Q_{\operatorname{frozen}}=\text{const}.
$$
Both parts contribute to the terminal calibration, but the exterior is fixed and
harmless.

## 7. What this estimate does NOT do

- It does not give $J_6$ persistence (that is the fixed-exponent lemma, which
  uses different weights and the two-factor Hölder on each support).
- It does not give $\|aE\|_\infty$ (that requires the defect Moser iteration).
- It does not give metric drift control (that requires integrating $\|aE\|_\infty$
  in time).
- It does not prove flow existence (that is the transported-DeTurck theorem).
- It does not prove continuation (that is the shifted-curvature extension theorem).

It *only* says: given the first-exit hypotheses, the unweighted global defect
grows at most exponentially with a rate set by $r^{-2}$, which is $O(1)$ on the
first-exit time scale $\theta r^2$.
