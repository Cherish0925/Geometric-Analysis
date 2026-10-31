# Step 35: unregularized $J_6$ persistence lemma

## 0. Purpose and advance over the Step 34 draft

This note completes the defect persistence estimate
$J_6(t) \le e^{C(1+r^{-2})t} J_6(0)$
without norm regularization and without invoking the curvature Moser
iteration or its seed $Y = K_3$. The mechanism has two key improvements
over Step 34 and A01 Step 33:

1. **No $\varepsilon$-regularization.** Setting $s = |E|^2$, the functional
   $J_6 = \int \eta^2 a^4 s^3\,d\mu$ is smooth, and every term in
   its time derivative is smooth (including at $E = 0$). The test
   function $q = 3\eta^2 a^4 s^2$ in the integrated Hessian-$a$ identity
   is smooth. No Kato approximant $\Phi_\varepsilon$ is needed, eliminating
   the unresolved $\varepsilon$-remainder from Step 34 §4.6.

2. **Two-factor Hölder absorption replaces three-factor.** The defect
   potential $P_6 = \int \eta^2 a^5 F s^3 = \int F w^2$ is absorbed by
   $$P_6 \le \|F\|_{2,U}\|w\|_4^2 \le \gamma(X_6 + Cr^{-2}J_6),
   \tag{0.1}$$
   with $\gamma = \mathcal S K_2^{1/2}$, using only $\|F\|_2$, not
   $Y = \int aF^3$. This is possible because the defect reaction is
   *linear* in $F$ (the integrand is $aF|E|^2$, not $aF^3$), so
   the three-factor identity that A01 uses for the curvature energy
   is unnecessary here. The $J_6$ estimate is therefore self-contained:
   it needs only the $K_2$ persistence (already established at $q = 2$),
   not the separate $q = 3$ curvature seed. This simplification was
   identified by the Research Strategist.

## 1. Setting and definitions

Throughout, a smooth solution of the flow
$$
\partial_t g = -2aE, \qquad
E = \operatorname{Ric} + g, \qquad
a = \chi^2
\tag{1.1}
$$
exists on a provisional first-exit interval $[0,T]$ (within the moving
Sobolev/metric/support comparability regime of Step 34 §5). Dimension
$n = 4$.

Let $\eta$ be the auxiliary cutoff with $\eta = 1$ near $\operatorname{supp}\chi$,
$a = da = 0$ on $\operatorname{supp}d\eta$. (The $d\eta$ terms all vanish;
see §3 below.)

Set
$$
s = |E|^2 = g^{ik}g^{jl}E_{ij}E_{kl}, \qquad
F = (1 + |\operatorname{Rm}|^2)^{1/2}.
\tag{1.2}
$$
Define
\begin{align}
J_m &= \int \eta^2 a^{m-2} s^{m/2}\,d\mu, \tag{1.3}\\
X_m &= \int \eta^2 a^{m-1} s^{(m-2)/2}|\nabla E|^2\,d\mu, \tag{1.4}\\
P_m &= \int \eta^2 a^{m-1} F s^{m/2}\,d\mu, \tag{1.5}\\
w_m &= \eta a^{(m-1)/2} s^{m/4}. \tag{1.6}
\end{align}
The Sobolev inequality on the auxiliary ball $B_{6r}$ is
$$
\|u\|_4^2 \le \mathcal S(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2),
\qquad
\mathcal S = C(4,Kr^2) \frac{r^2}{\sqrt{V}},
\tag{1.7}
$$
and the absorption parameter is
$\gamma = \mathcal S K_2^{1/2}$, with $K_2 = \int \eta^2 F^2\,d\mu$.

For $m = 6$: $J_6 = \int \eta^2 a^4 s^3$,
$X_6 = \int \eta^2 a^5 s^2 |\nabla E|^2$,
$P_6 = \int \eta^2 a^5 F s^3 = \int F w_6^2$,
$w_6 = \eta \chi^5 |E|^3$.

**Regularity.** Since $s = |E|^2$ and $s^3 = |E|^6$ are smooth on the
bundle of symmetric 2-tensors, every quantity above is smooth, including
at $E = 0$. No division by $|E|$ ever occurs. The Sobolev variable
$w_6 = \eta \chi^5 s^{3/2}$: because $t \mapsto t^{3/2}$ is $C^1$
on $[0,\infty)$ with bounded derivative on bounded sets, $w_6$ is
$C^1$ (indeed, $\nabla w_6$ is continuous and bounded) wherever
$\eta, \chi, s$ are smooth.

## 2. Exact evolution of $s$ and the chain rule

The defect evolves as
$$
\partial_t E_{ij} = a(\Delta_L E_{ij} - 2E_{ij})
+ \mathcal C_a(E)_{ij},
\tag{2.1}
$$
where $\mathcal C_a(E)$ collects all cutoff-derivative terms (stated
explicitly in Step 34 eq.\ 2.2). Combined with the metric variation of
the squared norm, the scalar $s = |E|^2$ satisfies
$$
(\partial_t - a\Delta)s
= -2a|\nabla E|^2 + \Sigma_s,
\tag{2.2}
$$
where the source $\Sigma_s$ is the sum of:
- *Lichnerowicz reaction*: $4a R_{ikjl}E^{ij}E^{kl}$, bounded by $CaFs$;
- *normalization reaction*: $(-4a + 8a)|E|^2 + \ldots$, bounded by $Cas$;
- *metric variation*: $4aE^{ip}R_{ijkl}E^{jkl}{}^p$, bounded by $CaFs$;
- *cutoff terms*: $2\langle E, \mathcal C_a(E)\rangle$;
- and $|\Sigma_s| \le CaFs + C(|\nabla a||\nabla E| + |\nabla^2 a|)s$,
  with the cutoff pieces handled by IBP in §3.

The chain rule for $s^k$ is exact:
$$
\boxed{
(\partial_t - a\Delta) s^k
= k s^{k-1}(\partial_t - a\Delta)s
  - a k(k-1) s^{k-2} |\nabla s|^2.}
\tag{2.3}
$$
For $k = 3$, the extra term is $-6as|\nabla s|^2 \le 0$, and the
dissipation from (2.2) gives
$$
3s^2 \cdot (-2a|\nabla E|^2) = -6as^2|\nabla E|^2.
\tag{2.4}
$$
This is the tensor-gradient coercivity, stronger than the scalar Kato
dissipation $|\nabla s|^2 \le 4s|\nabla E|^2$.

## 3. Integrated energy identity for $J_6$

Compute
$$
J_6' = \int \eta^2 a^4 (\partial_t s^3)\,d\mu
     + \int \eta^2 a^4 s^3 (\partial_t d\mu).
\tag{3.0}
$$
The cutoff $a^4 = \chi^8$ and the auxiliary cutoff $\eta$ are
time-independent.

### 3.1 Measure term

$\partial_t d\mu = -a\tau\,d\mu$ where $\tau = \operatorname{tr}E$
(from $\partial_t g_{ij} = -2aE_{ij}$, so $\operatorname{tr}(\partial_tg) = -2a\tau$).
Since $|\tau| \le C|E| = Cs^{1/2} \le CF$:
$$
\left|\int \eta^2 a^5 \tau s^3\right|
\le C \int \eta^2 a^5 |E| s^3
\le C \int \eta^2 a^5 F s^3 = C P_6.
\tag{3.1}
$$

### 3.2 Dissipation

Using (2.3) with $k = 3$ and integrating $a\Delta s^3$ by parts
against $\eta^2 a^4$:
$$
\int \eta^2 a^4 \cdot a\Delta s^3\,d\mu
= -\int \langle d(\eta^2 a^5), d(s^3)\rangle.
\tag{3.2a}
$$
Since $ds^3 = 3s^2 ds = 6s^2 \langle E, \nabla E\rangle$, this gives
$$
-\int \langle d(\eta^2 a^5), 6s^2 E^{ij}\nabla E_{ij}\rangle.
\tag{3.2b}
$$
Expanding $d(\eta^2 a^5) = 2\eta\,d\eta\cdot a^5 + 5\eta^2 a^4 da$:
- The $d\eta$ term **vanishes** because $a = 0$ on $\operatorname{supp}d\eta$.
- The $da$ term gives a cross term estimated in §3.4 below.

Combined with the principal term from (2.4):
$$
\text{principal dissipation from } s^3 =
-6\int \eta^2 a^5 s^2|\nabla E|^2 = -6X_6.
\tag{3.2c}
$$

The extra chain-rule term $-6as|\nabla s|^2$ integrates to
$-6\int \eta^2 a^5 s|\nabla s|^2 \le 0$, which we simply discard.

### 3.3 Reaction terms (no cutoff derivatives)

From the Lichnerowicz reaction, metric variation, and normalization
in $\Sigma_s$, testing with $3\eta^2 a^4 s^2$:
\begin{align}
\left|3\int \eta^2 a^4 s^2 \cdot (CaFs)\right|
&\le C \int \eta^2 a^5 F s^3 = CP_6, \tag{3.3a}\\
\left|3\int \eta^2 a^4 s^2 \cdot (Cas)\right|
&\le C \int \eta^2 a^5 s^3 \le CJ_6. \tag{3.3b}
\end{align}

### 3.4 Cutoff first-derivative cross terms

From §3.2, the surviving cross term is
$$
I_1 = 30 \int \eta^2 a^4 s^2 |da| \cdot |E| \cdot |\nabla E|.
\tag{3.4a}
$$
Since $|E| = s^{1/2}$, this is $30\int \eta^2 a^4 s^{5/2}|da||\nabla E|$.
Young's inequality with exponents $(2,2)$:
$$
I_1 \le \varepsilon \int \eta^2 a^5 s^2 |\nabla E|^2
     + C_\varepsilon \int \eta^2 a^3 |da|^2 s^3
= \varepsilon X_6 + 4C_\varepsilon r^{-2} J_6,
\tag{3.4b}
$$
using $a^3|da|^2 = 4a^4|d\chi|^2 \le 4r^{-2} a^4$.

### 3.5 Hessian-of-$a$ terms: exact tensor IBP

The cutoff operator $\mathcal C_a(E)$ contains terms with $\nabla^2 a$.
Using the integrated Hessian-$a$ identity (Step 34 eq.\ 2.4), tested
with $q = 3\eta^2 a^4 s^2$, the Hessian terms become
$$
T_H = \int (\nabla^2 a)_{ij} B^{ij}(q),
\tag{3.5a}
$$
where $B^{ij}$ is a tensor *quadratic in $E$* (verified computationally in
check A1--A3 of the companion script):
$$
B^{ij}(q) = q(2g^{ij}|E|^2 + 2\tau E^{ij} - 4E^{ik}E_k^j).
\tag{3.5b}
$$
The key property $B^{ij} = O(s)$ (vanishing at $E = 0$) means this is not
a bare curvature source.

Integrating by parts the actual tensor $\nabla_i\nabla_j a$ (not its
absolute value; this corrects the error identified by A01):
$$
T_H = -\int \nabla_k a \cdot \nabla_k[q B^{ij} g_{ij}]
\text{ (schematic; divergence of a vector contracted with $da$)}.
\tag{3.5c}
$$
More precisely, integrating the $ij$-th component:
$$
\int a_{ij} f = -\int a_j \nabla_i f + \text{div terms},
$$
then the derivative hits three factors of $q B$:

**(i) Derivative on $a^4$ in $q$.**
Produces $a^3|da|^2 \cdot s^2 \cdot |B| \le C a^3|da|^2 s^3 = 4C a^4|d\chi|^2 s^3$,
bounded by $Cr^{-2}a^4 s^3$. Integrated: $\le Cr^{-2}J_6$.

**(ii) Derivative on $s^2$ in $q$.**
Produces $a^4|da| \cdot 2s \cdot |ds| \cdot s = a^4|da| s^{3/2} \cdot 2|E||\nabla E| \cdot s$.
This is bounded by $\eta^2 a^4 s^{5/2}|da||\nabla E|$,
which is exactly $I_1$ from (3.4a). By (3.4b):
$\le \varepsilon X_6 + C_\varepsilon r^{-2} J_6$.

**(iii) Derivative on $B^{ij}$.**
Since $|B| \le C s$ and $|\nabla B| \le C s^{1/2}|\nabla E|$
(because $B$ is quadratic in $E$), this produces
$a^4 |da| \cdot s^2 \cdot s^{1/2}|\nabla E|$
$= a^4|da| s^{5/2}|\nabla E|$,
the same structure as $I_1$, absorbed by Young:
$\le \varepsilon X_6 + C_\varepsilon r^{-2} J_6$.

Combining all three branches:
$$
|T_H| \le \varepsilon X_6 + C_\varepsilon r^{-2} J_6.
\tag{3.5d}
$$

### 3.6 First-derivative-of-$a$ terms from $\mathcal C_a(E)$

The terms $(\nabla a)\cdot\nabla E \cdot E$ in $\langle E, \mathcal C_a(E)\rangle$,
after testing with $3\eta^2 a^4 s^2$, contribute
$$
I_2 \le C \int \eta^2 a^4 |da| s^{3/2}|\nabla E|,
\tag{3.6a}
$$
which has the same structure as $I_1$ in (3.4a). By (3.4b):
$$
I_2 \le \varepsilon X_6 + C_\varepsilon r^{-2} J_6.
\tag{3.6b}
$$

## 4. Assembled differential inequality

Collecting §3.1--§3.6 and choosing $\varepsilon$ small enough to absorb
into $-6X_6$:
$$
\boxed{
J_6' + c X_6 \le C(1 + r^{-2}) J_6 + C P_6,
}\tag{4.1}
$$
with universal constants $c, C > 0$. The potential $P_6$ must now
be absorbed.

## 5. Sobolev absorption of the potential (two-factor Hölder)

This is the decisive step.
$$
P_6 = \int F w_6^2\,d\mu, \qquad w_6 = \eta \chi^5 |E|^3 = \eta a^{5/2} s^{3/2}.
\tag{5.1}
$$
By Hölder with exponents $(2, 4, 4)$ applied to $F^{1/2} \cdot F^{1/2} w_6 \cdot w_6$:
$$
P_6 \le \|F\|_{2,U} \|w_6\|_4^2.
\tag{5.2}
$$
(Here $\|F\|_{2,U}^2 \le K_2$ since $a \le 1$ and $\eta \le 1$.)

Apply the local Sobolev inequality (1.7) with $u = w_6$:
$$
\|w_6\|_4^2 \le \mathcal S(\|\nabla w_6\|_2^2 + r^{-2}\|w_6\|_2^2).
\tag{5.3}
$$
The gradient decomposes as
\begin{align}
\nabla w_6
&= (d\eta) a^{5/2} s^{3/2}
 + \eta \cdot \tfrac{5}{2} a^{3/2}(da) \cdot s^{3/2}
 + \eta \cdot a^{5/2} \cdot \tfrac{3}{2} s^{1/2} \nabla s.
\tag{5.4}
\end{align}

- *First term*: vanishes because $a = 0$ on $\operatorname{supp}d\eta$.
- *Second term*: $|\eta \cdot 5\chi^4 d\chi \cdot s^{3/2}|^2 = 25\eta^2 a^4|d\chi|^2 s^3 \le C r^{-2} J_6$.
- *Third term*: $|\eta a^{5/2} \cdot (3/2) s^{1/2} \nabla s|^2
  \le (9/4) \eta^2 a^5 s |\nabla s|^2
  \le 9 \eta^2 a^5 s^2 |\nabla E|^2 = 9 X_6$,
  using $|\nabla s|^2 = |2\langle E, \nabla E\rangle|^2 \le 4|E|^2|\nabla E|^2 = 4s|\nabla E|^2$.
- Cross terms are absorbed by Young into the same quadratics.

Also, $\|w_6\|_2^2 = \int \eta^2 a^5 s^3 \le J_6$ (since $a \le 1$).

Therefore:
$$
\|\nabla w_6\|_2^2 \le C(X_6 + r^{-2} J_6).
\tag{5.5}
$$
Substituting into (5.3):
$$
\|w_6\|_4^2 \le C \mathcal S (X_6 + r^{-2} J_6).
\tag{5.6}
$$
Combining with (5.2):
$$
\boxed{
P_6 \le C \gamma (X_6 + r^{-2} J_6),
\qquad \gamma = \mathcal S K_2^{1/2}.
}\tag{5.7}
$$

**Volume cancellation.** On a good-center support with
$K_2 \le K_0 V$:
$$
\gamma = \frac{Cr^2}{\sqrt{V}} \sqrt{K_0 V} = Cr^2 \sqrt{K_0},
\tag{5.8}
$$
which is collapse-independent, as established in Step 34.

## 6. Closed Gronwall inequality and $J_6$ persistence

Substituting (5.7) into (4.1) and choosing $\gamma_0$ so that
$C\gamma_0 < c/2$:

$$
J_6' + \tfrac{c}{2} X_6
\le C_0(1 + r^{-2}) J_6,
\tag{6.1}
$$
where $C_0$ depends only on dimension, the cutoff, and $K_0 r^2$
(all bounded for a good center). By Gronwall:
$$
\boxed{
J_6(t) \le e^{C_0(1+r^{-2})t} J_6(0),
\qquad t \in [0,T].
}\tag{6.2}
$$

For $T = \theta r^2$ with $\theta$ fixed:
$$
J_6(T) \le e^{C_0(\theta r^2 + \theta)} J_6(0).
\tag{6.3}
$$
Since $J_6(0) \le |E(0)|_\infty^6 \operatorname{Vol} \le \delta^6 V$
(from the initial $\delta$-pinching), this gives
$$
J_6(T) \le C \delta^6 V,
\tag{6.4}
$$
with $C$ depending only on $K_0, r, \theta$ and dimension. For a
maximal-function good center, $K_0$ is bounded by a sequence-uniform
constant, so $C$ is sequence-uniform.

**Comparison with A01 Step 33 §4.1.** A01's route to $J_6$ persistence
uses the integrated Gronwall coefficient $\int_0^T \mathcal S^2 Y \le C\gamma^3$,
requiring the $q = 3$ curvature seed. Our route bypasses this: the
two-factor absorption (5.7) produces a *constant* Gronwall coefficient
$C_0(1 + r^{-2})$ with no time-dependent curvature factor at all.
The two conclusions are compatible; ours is strictly simpler.

**No norm regularization.** The entire argument uses only $s = |E|^2$
and its smooth powers. The Kato regularization $\Phi_\varepsilon = (|E|^2 + \varepsilon^2)^{1/2}$
from Step 34 is not needed. No $\varepsilon$-remainder was generated,
and no limit passage is required.

## 7. Downstream consequences

### 7.1 Defect Moser iteration

With $J_6(t) \le C\delta^6 V$ and the general defect power inequality
(A01 eq.\ 4.4 or the $s$-based version), the nested spacetime Moser
recurrence starting at $p_0 = 6$ gives (Step 34 eq.\ 4.5 with
$f = |E|$):
$$
\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3},
\qquad t \in (0, T].
\tag{7.1}
$$
The time integral is finite:
$$
\int_0^T \|aE(t)\|_\infty\,dt
\le C\delta r^{2/3} T^{2/3}
= C\delta \theta^{2/3} r^2 \to 0
\quad \text{as } \delta \to 0.
\tag{7.2}
$$
This is the sequence-uniform, collapse-independent integrable metric
drift required by the first-exit argument.

### 7.2 What remains

1. **General $J_p$ Moser recurrence**: the nested-time iteration with
   the $\mathcal S^2 Y$ coefficient on dyadic slabs, producing (7.1).
   This uses the curvature Moser chain, not the $J_6$ lemma itself.
2. **$K_2$ and $Y = K_3$ persistence**: from the $q = 2,3$ curvature
   energy inequalities (Step 34 eqs.\ 3.1--3.3).
3. **First-exit bootstrap**: the simultaneous self-improving argument
   carrying $\mathcal S(t), K_2(t), J_6(t)$, metric comparison, and
   support geometry.
4. **Continuation**: the coupled $(W_m, C_{m+1})$ estimate for
   higher derivatives, needed for smooth terminal metrics and
   plateau regularity.
5. **Terminal geometric passage**: from controlled terminal
   metrics to the calibrated Einstein-germ contradiction.

Items 2--3 depend on the curvature energy inequality and its Moser
iteration, not on the $J_6$ lemma. Item 1 depends on the curvature
Moser endpoint. Item 4 is datum-dependent (per-metric constants
are acceptable). Item 5 uses the topology-uniform calibration
inequality and the local projector obstruction.

### 7.3 What this lemma does NOT establish

- Any Ricci-pinching gap or Einstein-existence theorem.
- Existence or smoothness of the degenerate cutoff flow.
- The first-exit closure (which requires the curvature chain simultaneously).
- Any statement about the full Yau Problem 26.

## 8. Verification

`workspace/scripts/verify_step35_defect_algebra.py` — 28 checks, all pass.

Verified: Hessian-$a$ contraction identity with $B$ quadratic in $E$;
$B = 0$ at $E = 0$; exact chain rule for $s^k$ with the favourable
extra term; matched weight exponents for every Young/Hölder step;
$C^1$ regularity of $w_6 = \eta\chi^5|E|^3$; two-factor Hölder
exponents; and the collapse-independent absorption parameter
$\gamma = r^2\sqrt{K_0}$.
