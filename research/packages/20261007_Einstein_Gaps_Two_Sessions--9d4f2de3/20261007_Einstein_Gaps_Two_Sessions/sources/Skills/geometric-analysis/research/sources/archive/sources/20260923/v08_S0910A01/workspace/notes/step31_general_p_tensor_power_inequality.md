# Step 31: General-$p$ tensor power inequality for the normalized cutoff flow


**Step 32 superseding audit.**  The weight identities in this note remain useful,
but its claimed completed general-\(p\) theorem and its Sections 5--8 endpoint
interpretation are superseded by `workspace/notes/step32_nested_moser_and_tensor_audit.md`.
Use the single convention
\(\|z\|_4^2\le C_S(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2)\),
\(\beta=C_SH_2(0)^{1/2}\), with positive-time coefficient \(C_S^2Y\).
The direct spacetime recurrence has no division by \(L_k^{1/2}\) and yields the
conditional endpoints \(\|aF(t)\|_\infty\lesssim\beta/t\) and
\(\|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}\) only after the same-support
\(H_3\), fixed \(J_6\), and \(Q\) estimates are proved from time zero.
A collapse-independent unnormalized Dirichlet Sobolev constant is false.  The
tensor-power derivation below is only schematic until the Hessian-\(a\) terms
with derivatives hitting \(a^{p-2}F^{p-2}\) are absorbed while retaining both
\(D_p^{\operatorname{Rm}}\) and \(D_p^F\), and until the regularized defect
power calculation is written.
Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

This note derives the explicit all-$p$ weighted curvature power inequality
for the flow $\partial_tg=-2aE$, $a=\chi^2$, $E=\operatorname{Ric}+g$, on one
macro-disjoint buffered selected support.  The derivation tracks $p$-dependent
coefficients to show polynomial growth in $p$, compatible with Moser convergence.
It extends Step 25's $p=2$ and $p=3$ cases to general $p\ge2$ and connects
through the three-factor absorption and Cauchy--Schwarz interpolation (A03 Step
31) to the complete Moser recurrence from $K_3$ to $\|aF\|_\infty$.

## 1. Setup and notation

Let $(M^n,g(t))$ satisfy the normalized cutoff flow on a closed manifold:
$$
\partial_tg = -2a(\operatorname{Ric}+g) = -2aE, \qquad a = \chi^2 \in [0,1],
\tag{1.1}
$$
with fixed smooth cutoff $\chi\in C^\infty(M,[0,1])$, $|\nabla\chi|\le C_\chi/r$
on $\operatorname{supp}\chi$, and the buffered support geometry (Step 24):
$$
a|\nabla\eta|^2 = 0, \quad \nabla a\cdot\nabla\eta = 0, \quad
\operatorname{supp}(a)\subset\{\eta=1\}.
\tag{1.2}
$$
All integrals below are over $\operatorname{supp}\chi$ (where $\eta=1$); the
auxiliary $\eta$ appears only in the IBP boundary terms, which vanish.

Standing cutoff identities:
$$
\nabla a = 2\chi\nabla\chi, \quad
\frac{|\nabla a|^2}{a} = 4|\nabla\chi|^2 \le \frac{4C_\chi^2}{r^2}, \quad
\nabla^2 a = 2\,d\chi\otimes d\chi + 2\chi\nabla^2\chi.
\tag{1.3}
$$

Define $F=(1+|\operatorname{Rm}|^2)^{1/2}\ge1$, so that
$$
|\nabla F| \le |\nabla\operatorname{Rm}| \quad\text{(Kato)}, \qquad
|E| \le C_nF, \qquad |\nabla E| \le C_n|\nabla\operatorname{Rm}|.
\tag{1.4}
$$

The weighted moment and dissipation:
$$
K_p(t) = \int a^{p-2}F^p\,d\mu_t, \qquad
D_p^F(t) = \int a^{p-1}F^{p-2}|\nabla F|^2\,d\mu_t,
$$
$$
D_p^{\operatorname{Rm}}(t) = \int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2\,d\mu_t
\ge D_p^F.
\tag{1.5}
$$
The Moser test function is $Z_p = a^{(p-1)/2}F^{p/2}$, whose gradient satisfies
(A03 Step 31, eq. (4)):
$$
\|\nabla Z_p\|_2^2 \le Cp^2(D_p^F + r^{-2}K_p).
\tag{1.6}
$$

## 2. Time derivative of $K_p$

$$
\frac{d}{dt}K_p = \underbrace{\int a^{p-2}\frac{p}{2}F^{p-2}\partial_t(|\operatorname{Rm}|^2_g)\,d\mu}_{\text{curvature evolution}} + \underbrace{\int a^{p-2}F^p\partial_t(d\mu)}_{\text{volume}}.
\tag{2.1}
$$

**Volume form.** From $\partial_t(d\mu) = -a(s+n)\,d\mu$ and $|s+n|\le C_nF$:
$$
\left|\text{volume term}\right| \le C_np\int a^{p-1}F^{p+1}\,d\mu =: C_npR_p.
\tag{2.2}
$$
(The factor $p$ is absent because the weight $a^{p-2}$ does not evolve; the
$a^{p-1}$ in $R_p$ comes from the product $a^{p-2}\cdot a$.)

**Curvature evolution.** From Step 25 eq. (2.7), the curvature variation
decomposes into types A--D.  In the general-$p$ setting, each is tested against
$\frac{p}{2}a^{p-2}F^{p-2}\cdot 2\operatorname{Rm}$, producing the following.

### 2a. Type A: Bochner principal and normalization

The Bochner identity gives, after testing:
$$
\int a^{p-2}\frac{p}{2}F^{p-2}\cdot\bigl[a\Delta(|\operatorname{Rm}|^2) - 2a|\nabla\operatorname{Rm}|^2 + a\operatorname{Rm}^3 + O(a|\operatorname{Rm}|^2)\bigr].
$$

**Dissipation.** The Bochner pair contributes two dissipation terms:

(i) from $-2a|\nabla\operatorname{Rm}|^2$:
$$
-p\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2 = -pD_p^{\operatorname{Rm}}.
\tag{2.3a}
$$

(ii) from IBP of $a\Delta(|\operatorname{Rm}|^2)$: using $\nabla(|\operatorname{Rm}|^2) = 2F\nabla F$ and the product rule on $\nabla[a^{p-1}\frac{p}{2}F^{p-2}]$:
$$
-\frac{p(p-2)}{2}\int a^{p-1}\cdot 2F^{p-2}|\nabla F|^2 = -p(p-2)D_p^F.
\tag{2.3b}
$$

Combined: $-pD_p^{\operatorname{Rm}} - p(p-2)D_p^F \le -p(p-1)D_p^F$ (using
$D_p^{\operatorname{Rm}}\ge D_p^F$).

**IBP cutoff remainder.** The IBP also produces:
$$
-p(p-1)\int a^{p-2}F^{p-1}(\nabla a)\cdot\nabla F.
$$
By Young ($\varepsilon=1/(2(p-1))$) and (1.3):
$$
\left|\cdots\right| \le \frac{p(p-1)}{2}D_p^F + \frac{Cp(p-1)}{r^2}K_p.
\tag{2.4}
$$

After absorbing (2.4) into the dissipation, the remaining principal dissipation
from Type A is:
$$
\ge -\frac{p(p-1)}{2}D_p^F.
\tag{2.5}
$$

**Cubic reaction.** $|a\operatorname{Rm}^3| \le CaF^3$, so the testing gives
$\le Cp\int a^{p-1}F^{p+1} = CpR_p$.

**Normalization.** As in Step 25, the conformal contribution to
$\partial_t(|\operatorname{Rm}|^2\,d\mu)$ is exactly zero, and for
$F^2=1+|\operatorname{Rm}|^2$, the net conformal source is $-4a\,d\mu$ per unit
volume (a bounded term, not a curvature damping).  Tested against
$a^{p-2}F^{p-2}$, this contributes $\le Cp\int a^{p-2}F^{p-2}\le CpK_p$ (since
$F\ge1$).

### 2b. Type B: first-derivative cutoff

$$
|(\nabla a)(\nabla E)\operatorname{Rm}| \le C|\nabla a||\nabla\operatorname{Rm}|F.
$$
Tested and Young'ed exactly as (2.4):
$$
\le \varepsilon p D_p^{\operatorname{Rm}} + \frac{Cp}{\varepsilon r^2}K_p.
\tag{2.6}
$$

### 2c. Type C: Hessian-of-$a$

After IBP (Step 25 eqs. 2.15--2.17 generalized to weight $a^{p-2}F^{p-2}$),
the boundary term $\nabla a\cdot\nabla\eta$ vanishes by (1.2).  The surviving
term has the same structure as Type B with $\nabla a$ from the IBP:
$$
\le \varepsilon p D_p^{\operatorname{Rm}} + \frac{Cp}{\varepsilon r^2}K_p.
\tag{2.7}
$$

### 2d. Type D: algebraic coupling

$$
|a\operatorname{Rm}*E*\operatorname{Rm}| \le CaF^3.
$$
Tested: $\le Cp R_p$, same as the cubic reaction.

### 2e. Metric variation of the norm

Each inverse-metric factor $g^{ij}$ varies as $\partial_tg^{ij}=2aE^{ij}$;
with four factors:
$$
\left|(\text{metric variation of }|\operatorname{Rm}|^2)\right| \le Ca|E||\operatorname{Rm}|^2 \le CaF^3.
$$
Tested: $\le CpR_p$.

## 3. Collected general-$p$ power inequality

Choosing $\varepsilon = 1/8$ in (2.6)--(2.7) and absorbing into the principal
dissipation (2.5):

$$
\boxed{
K_p' + \frac{p(p-1)}{4}D_p^F
\le C_1 p R_p + C_2 p^2 r^{-2}K_p + C_3 pK_p,}
\tag{3.1}
$$

where:
- $R_p = \int a^{p-1}F^{p+1}\,d\mu$ is the **curvature reaction**;
- $C_1, C_2, C_3$ depend only on $n$ and the cutoff constants $C_\chi, L_\chi$;
- the $C_3pK_p$ term absorbs the normalization source (bounded since $F\ge1$).

For $p\ge3$: $(p-1)/4 \ge p/8$, so the dissipation coefficient is $\ge p^2/8$.
For $p=2$: $(p-1)/4 = 1/4$, giving $D_2^F/2$ after the chosen $\varepsilon$.
Both match the Step 25 $p=2$ and $p=3$ cases.

## 4. Three-factor absorption of the curvature reaction

**Exact factorization (Step 27).** For $Z_p = a^{(p-1)/2}F^{p/2}$:
$$
a^{p-1}F^{p+1} = (aF^3)^{1/3}(a^{p-2}F^p)^{1/3}Z_p^{4/3}.
\tag{4.1}
$$
*Proof:* $a$-exponent: $1/3+(p-2)/3+2(p-1)/3 = (3p-3)/3 = p-1$; $F$-exponent:
$1+p/3+2p/3 = p+1$.  $\square$

By Hölder $(3,3,3)$:
$$
R_p = \int a^{p-1}F^{p+1}
\le Y^{1/3}K_p^{1/3}\|Z_p\|_4^{4/3},
\qquad Y = K_3 = \int aF^3.
\tag{4.2}
$$

By the Sobolev bound (1.6):
$$
\|Z_p\|_4^2 \le S^2\cdot Cp^2(D_p^F + r^{-2}K_p).
\tag{4.3}
$$

Hence:
$$
R_p \le Cp^{4/3}S^{4/3}Y^{1/3}K_p^{1/3}(D_p^F + r^{-2}K_p)^{2/3}.
\tag{4.4}
$$

**Young absorption.** Apply $a^{1/3}b^{2/3}\le\frac{1}{3\lambda}a+\frac{2\lambda^{1/2}}{3}b$
to $a=K_p$, $b=D_p^F+r^{-2}K_p$, choosing $\lambda^{1/2}$ so that the
$D_p^F$-coefficient becomes $\frac{p(p-1)}{16C_1p} = \frac{p-1}{16C_1}$:

$$
\frac{2\lambda^{1/2}}{3}\cdot C_1 p \cdot Cp^{4/3}S^{4/3}Y^{1/3}
= \frac{p(p-1)}{16}.
$$

Solving: $\lambda^{1/2} = \frac{3(p-1)}{32C_1Cp^{4/3}S^{4/3}Y^{1/3}}$.
Hence $\frac{1}{\lambda} = \frac{(32C_1C)^2 p^{8/3}S^{8/3}Y^{2/3}}{9(p-1)^2}$.

The $K_p$-coefficient from absorption:
$$
C_1 p\cdot Cp^{4/3}S^{4/3}Y^{1/3}\cdot\frac{1}{3\lambda}
= \frac{C_1 Cp^{7/3}S^{4/3}Y^{1/3}}{3}\cdot\frac{(32C_1 C)^2 p^{8/3}S^{8/3}Y^{2/3}}{9(p-1)^2}.
$$

For $p\ge2$: $(p-1)^2\ge p^2/4$, so this is $\le C_*p^3 S^4Y$ where $C_*$
depends only on $n$ and cutoff constants.

**Absorbed form.** Substituting into (3.1):

$$
\boxed{
K_p' + \frac{p^2}{16}D_p^F
\le C_*(p^3 S^4Y + p^2 r^{-2} + p)K_p + C_3 pK_p.}
\tag{4.5}
$$

For the Moser iteration, write the coefficient as $L_p(t)$:
$$
L_p(t) = C_*(p^3 S^4Y(t) + p^2 r^{-2} + p).
\tag{4.6}
$$

The polynomial growth in $p$ is $O(p^3)$ from the three-factor absorption.

## 5. Cauchy--Schwarz interpolation and the Moser recurrence

**Lemma (A03 Step 31).** For $\kappa = 3/2$:
$$
K_{\kappa p} = K_{3p/2} \le K_p^{1/2}\,K_{2p}^{1/2},
\qquad K_{2p} = \|Z_p\|_4^4.
\tag{5.1}
$$
*Proof:* Cauchy--Schwarz with factors $a^{(p-2)/2}F^{p/2}$ and
$a^{(2p-2)/2}F^p$; exponents sum to $(3p-4)/2 = 3p/2-2$ and $3p/2$.

**Sobolev bound on $K_{2p}$.**
$$
K_{2p}^{1/2} = \|Z_p\|_4^2 \le Cp^2 S^2(D_p^F + r^{-2}K_p).
\tag{5.2}
$$

**Spacetime estimate.** Integrate (4.5) over a time slab $I_k = [t_k,T]$ with
time cutoff $\zeta_k$ satisfying $|\zeta_k'|\le 4^k/T$:
$$
\sup_{I_{k+1}}K_{p_k} + \int_{I_{k+1}}D_{p_k}^F
\le L_{k}\int_{I_k}K_{p_k},
\tag{5.3}
$$
where $L_k = Cp_k^3(4^k T^{-1} + S^4\|Y\|_{L^\infty(I_k)} + r^{-2} + 1)$.

**Recurrence.** Integrating (5.2) over $I_{k+1}$:
$$
\int_{I_{k+1}}K_{2p_k}^{1/2}
\le Cp_k^2 S^2\int_{I_{k+1}}(D_{p_k}^F + r^{-2}K_{p_k}).
$$
And by (5.1):
$$
\int_{I_{k+1}}K_{p_{k+1}}
\le (\sup K_{p_k})^{1/2}\int_{I_{k+1}}K_{2p_k}^{1/2}.
$$
Combining:
$$
\int_{I_{k+1}}K_{p_{k+1}}
\le Cp_k^2 S^2\bigl[L_k\int_{I_k}K_{p_k}\bigr]^{3/2}/(L_k^{1/2}).
$$

More precisely, define
$$
m_k = \left(\frac{1}{|I_k|}\int_{I_k}K_{p_k}\right)^{1/p_k}, \qquad p_k = (3/2)^k p_0.
$$

Then the Moser recurrence has the form
$$
m_{k+1}^{p_{k+1}}|I_{k+1}|
\le (Cp_k^2 S^2)^{p_{k+1}/p_k}\cdot(L_k|I_k|)^{3p_{k+1}/(2p_k)}\cdot m_k^{3p_{k+1}/2}|I_k|^{-p_{k+1}/2}.
$$

Taking $p_{k+1}$-th roots:
$$
m_{k+1} \le C_k m_k,
\qquad C_k = (C p_k^5 S^2 L_k)^{1/p_k}\cdot|I_k|^{-3/(2p_k)}\cdot|I_{k+1}|^{1/p_{k+1}}.
\tag{5.4}
$$

**Moser product convergence.**
$$
\prod_{k=0}^\infty C_k
= \exp\left(\sum_{k=0}^\infty\frac{\log C_k'}{p_k}\right)
$$
where $C_k'$ grows polynomially in $p_k$ and $4^k$.  Since
$p_k = (3/2)^k p_0$ grows geometrically:
$$
\sum_k\frac{\log p_k}{p_k} < \infty, \qquad
\sum_k\frac{k}{p_k} < \infty.
\tag{5.5}
$$
Therefore $\prod C_k < \infty$, and the Moser iteration converges to:
$$
\|aF(T)\|_\infty \le C_{\operatorname{Mos}}\cdot m_0
= C_{\operatorname{Mos}}\left(\frac{1}{|I_0|}\int_{I_0}K_{p_0}\right)^{1/p_0}.
\tag{5.6}
$$

**Exponent sums** (in dimension $n=4$ with $\kappa=3/2$, $p_0=3$):
$$
\sum_{k=0}^\infty\frac{1}{p_k} = \frac{1}{p_0}\cdot\frac{\kappa}{\kappa-1} = \frac{n+2}{2p_0} = 1.
\tag{5.7}
$$
$$
\sum_{k=0}^\infty\frac{1}{\kappa p_k} = \frac{n}{2p_0} = \frac{2}{3}.
$$

The temporal localization power from nested time cutoffs is $T^{-\sum 1/p_k}=T^{-1}$,
producing the **time singularity**:
$$
\boxed{
\|aF(t)\|_\infty \le C_{\operatorname{Mos}}\left(\frac{1}{t}\int_0^t K_3\right)^{1/3},
\qquad 0 < t \le T.}
\tag{5.8}
$$

## 6. The q=3 cubic potential and terminal curvature bound

**q=3 energy persistence** (from Step 25 eq. 5.1--5.3, with $K_3 = Y$):
$$
Y' + cD_3^F \le Cr^{-2}Y + C\int a^2 F^4.
\tag{6.1}
$$
The reaction $\int a^2F^4$ is absorbed by $\beta_a = S^2 H_2^{1/2}$
(Step 24 eq. 5.2), giving for small $\beta_a$:
$$
Y(t) \le e^{Cr^{-2}t}Y(0), \qquad 0 \le t \le T.
\tag{6.2}
$$

**Initial $K_3$ bound.** At $t=0$, the initial Ricci pinching $|E|\le\delta$
gives $|\operatorname{Rm}| \le C(1+\delta)$ only if we have sectional curvature
control.  In general, only $H_2(0) \le C\operatorname{Vol}(1+K_0)$ is available.
But:
$$
K_3(0) = \int aF^3(0) \le K_2(0)^{1/2}K_4(0)^{1/2}
$$
by (5.1) at $p=2$. And $K_4(0) = \|Z_2(0)\|_4^4 \le S^4\cdot C(D_2^F(0)+r^{-2}K_2(0))^2$...
but $D_2^F(0)$ requires initial gradient control that we do not have.

The correct approach is through spacetime averaging.  From the q=2 energy (Step 25):
$$
\int_0^T D_2^F \le CH_2(0)(1+r^{-2}T).
\tag{6.3}
$$

**Spacetime $K_3$ bound.** By (5.1) and (5.2) at $p=2$:
$$
K_3(t) \le K_2(t)^{1/2}K_4(t)^{1/2} \le K_2(t)^{1/2}\cdot CS^2(D_2^F(t)+r^{-2}K_2(t))^{1/2} \cdot K_2(t)^{1/4}.
$$

Actually, more directly: $K_3 \le K_2^{1/2}K_4^{1/2}$ and
$K_4^{1/2} = \|Z_2\|_4^2 \le CS^2(D_2^F+r^{-2}K_2)$.  So
$$
K_3(t) \le CS^2K_2(t)^{1/2}(D_2^F(t)+r^{-2}K_2(t)).
$$

Integrating: $\int_0^T K_3 \le CS^2(\sup K_2)^{1/2}\int_0^T(D_2^F+r^{-2}K_2)$.

Using $H_2$ persistence ($\sup K_2 \le 2H_2(0)$) and (6.3):
$$
\int_0^T K_3 \le C S^2 H_2(0)^{1/2}\cdot H_2(0)(1+r^{-2}T)
= C\gamma H_2(0)(1+\theta),
\tag{6.4}
$$
where $\gamma = S^2 H_2(0)^{1/2}$ is the critical absorption parameter and
$T = \theta r^2$.

**Good slice and forward propagation.**  For any $t \in (0,T]$, there exists
$t_* \in [t/2,t]$ with
$$
K_3(t_*) \le \frac{2}{t}\int_0^t K_3.
$$
Forward from $t_*$ using (6.2):
$$
K_3(t) \le e^{Cr^{-2}t/2}K_3(t_*) \le \frac{Ce^{C\theta}}{t}\int_0^T K_3.
\tag{6.5}
$$

Combining with (6.4):
$$
K_3(t) \le \frac{C\gamma H_2(0)(1+\theta)e^{C\theta}}{t}, \qquad 0<t\le T.
\tag{6.6}
$$

**Terminal curvature bound.** Substituting (6.6) into (5.8):
$$
\|aF(t)\|_\infty \le C_{\operatorname{Mos}}\left(\frac{1}{t}\int_0^t\frac{C\gamma H_2(0)}{s}\,ds\right)^{1/3}
$$
...but the integral $\int_0^t s^{-1}\,ds$ diverges.  The correct procedure is to
use (6.6) only as a **coefficient** in the Moser iteration, not as an input.

More precisely: the energy inequality (4.5) has the time-dependent coefficient
$S^4 Y(t) \le CS^4\gamma H_2(0)/t$.  On the time slab $[t/2,t]$:
$$
\int_{t/2}^t S^4 Y(s)\,ds \le CS^4\gamma H_2(0)\log 2 = C\gamma^3\log 2
$$
(using $S^4 H_2(0) = \gamma^2$).  This integrated coefficient is **bounded
uniformly in $t$** for small $\gamma$.

The nested Moser iteration on $[t/2,t]$ therefore gives:
$$
\boxed{
\|aF(t)\|_\infty
\le C_{\operatorname{Mos}}\left(\frac{K_3(t)}{1}\right)^{1/3}
\le C\left(\frac{\gamma H_2(0)}{t}\right)^{1/3}
= C\frac{\gamma^{1/3}H_2(0)^{1/3}}{t^{1/3}}.}
\tag{6.7}
$$

Using $\gamma = S^2H_2(0)^{1/2}$ and $\beta = S\sqrt{H_2(0)}$:
$\gamma^{1/3}H_2(0)^{1/3} = S^{2/3}H_2(0)^{1/2} = S^{-1/3}\beta$.

In fact, the cleanest form uses $Y(t) \le CY(0)e^{C\theta}$ and runs Moser
on $[t/2,t]$ starting from the instantaneous $K_3(t)$:
$$
\|aF(t)\|_\infty \le CK_3(t)^{1/3}\cdot(t/2)^{-1/3}\cdot(t/2)^{1/3}
= CK_3(t)^{1/3}.
\tag{6.8}
$$

But $K_3(t)$ need not be small—it is bounded by $O(H_2(0))$.  The $\beta/t$ form
appears when we combine the temporal localization of the Moser product with the
spacetime integral of $K_3$:

$$
\|aF(t)\|_\infty^3 \le \frac{C}{t}\int_0^t K_3(s)\,ds \le \frac{C\gamma H_2(0)(1+\theta)}{1} \le C\gamma H_2(0),
$$
so $\|aF(t)\|_\infty \le C(\gamma H_2(0))^{1/3}$ for $t\in(0,T]$, independent of $t$.

This is a **bounded** estimate, not $C/t$.  The $\beta/t$ time-decay in earlier notes
(Steps 27, 29) conflated the coefficient in the Moser equation with the output.
The correct statement is:

> For the curvature seed $p_0=3$ in dimension $n=4$, the Moser output from
> $K_3$ on $[0,\theta r^2]$ is a **uniform bound**:
> $$\|aF(t)\|_\infty \le C(\gamma,\theta)$$
> for $0 < t \le \theta r^2$, where $C(\gamma,\theta)$ depends on the
> critical parameter $\gamma = S^2H_2(0)^{1/2}$ and the time ratio $\theta$.

The $1/t$ singularity in earlier notes should be understood as the behavior of
the **coefficient** $S^4Y(t) \le C\gamma^2/t$ in the Moser equation, not of
the output $\|aF\|_\infty$.

**Corrected curvature estimate (TTCS-verified):**
$$
\boxed{\|aF\|_{L^\infty([T/4,T])}
\le C_{\rm Mos}\left(\frac{1}{VT}\int_0^TK_3\right)^{1/3}
\lesssim S^{1/3}\theta^{-1/3}(1+K_0)^{1/2},}
\tag{6.9}
$$
where $V=\operatorname{Vol}(\operatorname{supp}\chi)$ and $S^2=Cr^4/V$.
The explicit $V$ cancels after using $S^2=Cr^4/V$ and $H_2\le CV(1+K_0)$,
but the bound depends on $S$.  If the Dirichlet Sobolev inequality applies
($Z_p$ vanishes at $\partial\operatorname{supp}\chi$), then $S$ is replaced
by a volume-independent constant $C_{\rm Dir}(n,\kappa r^2)$.

## 7. Defect seed: $J_6$ persistence and weighted velocity

For $\Phi = |E|_\varepsilon = (|E|^2+\varepsilon)^{1/2}$, the defect power
inequality follows the same scheme but with key differences:

1. **Homogeneity in $E$:** the evolution $\partial_t E = \ldots$ vanishes at
   $E=0$, so every term contains at least one factor of $|E|$.
2. **Curvature potential:** the reaction is $\int a^{p-1}F|E|^p$ (not
   $\int a^{p-1}|E|^{p+1}$), because the coupling $\operatorname{Rm}*E$ brings
   one power of $F$.

The defect power inequality is:
$$
J_p' + \frac{p^2}{16}\hat D_p
\le C_*\bigl(p^3 S^4Y + p^2r^{-2}\bigr)J_p + Cp\int a^{p-1}F|E|^p,
\tag{7.1}
$$
where $J_p = \int a^{p-2}|E|^p$ and $\hat D_p = \int a^{p-1}|E|^{p-2}|\nabla E|^2$.

**Critical absorption at $p_0=6$.** The curvature potential
$\int a^{p-1}F|E|^p$ with $p=6$:
$$
\int a^5 F|E|^6 \le \|aF\|_\infty J_6.
$$
After Step 6 gives $\|aF\|_\infty \le C_*$, this is absorbed for initial
$J_6(0) \le \delta^6\operatorname{Vol}$ (from $|E(0)|\le\delta$).

**Defect Moser.** Starting from $p_0=6$ with seed $J_6$, the Moser iteration
with coefficient $\|aF\|_\infty$ gives:
$$
\|a^{1-2/p}|E|\|_\infty \to \|a|E|\|_\infty \le C\delta,
\tag{7.2}
$$
a uniform bound on the weighted defect.

**Metric comparison.** The velocity $|aE|(t) \le C\delta$ for $0<t\le T$ gives:
$$
V(T) = \int_0^T\|aE\|_\infty\,dt \le C\delta T,
$$
and $e^{-2V}g_0 \le g(T) \le e^{2V}g_0$ on $\operatorname{supp}\chi$.
For $\delta T$ small, the metric is bilipschitz.

## 8. Correction of prior time-decay claims

Steps 27 and 29 stated $\|aF(t)\|_\infty \le C\beta/t$ and
$\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$.  These were predicated on the
coefficient $S^4Y(t)\sim C/t$ propagating into the Moser output as a $1/t$ factor.

**Correction:** The Moser output from an $L^{p_0}$ seed is $\|u\|_\infty \le C\|u\|_{p_0}$ (with
a constant depending on the time interval and the coefficient's $L^1_t$ norm).
A coefficient that is integrable on $[0,T]$ does not create $1/t$ decay in the output;
it only appears as a bounded multiplicative constant.  The $1/t$ decay of
$S^4Y(t)$ is consumed by the integration, not transmitted to the pointwise curvature.

The corrected estimates are:
- **Curvature:** $\|aF(t)\|_\infty \le C(\gamma, \theta)$ (uniform on $(0,T]$).
- **Defect:** $\|aE(t)\|_\infty \le C\delta$ (uniform on $(0,T]$).
- **Velocity:** $V(T) = O(\delta T) = O(\delta\theta r^2)$ (integrable, small for small $\delta\theta$).

These are weaker than the prior claims but still sufficient for the metric comparison
and the terminal recalibration, because the critical requirement is $V(T) = o(1)$
as $\delta\to0$, which holds for any fixed $\theta$.

## 9. Summary: complete Moser chain

| Step | Input | Output | $p$-growth |
|------|-------|--------|------------|
| q=2 energy | $H_2(0)$ | $\sup H_2\le CH_2(0)$, $\int D_2 \le CH_2(0)$ | $p^2$ |
| q=3 energy | $H_2$ persistence | $Y(t)\le CY(0)$, $Y(t)\le C\gamma H_2/t$ | $p^2$ |
| general-$p$ | $K_3$ control | power inequality (4.5) | $p^3$ (reaction) |
| Moser ($p_0=3$) | $K_3$ | $\|aF\|_\infty \le C$ | $\sum\log p_k/p_k<\infty$ |
| $J_6$ persistence | $\|aF\|_\infty$ | $J_6(t)\le CJ_6(0)$ | $p^2$ |
| Moser ($p_0=6$) | $J_6$ | $\|aE\|_\infty \le C\delta$ | $\sum\log p_k/p_k<\infty$ |
| Velocity | $\|aE\|_\infty$ | $V(T)\le C\delta T$ | — |
| Metric comparison | $V(T)$ | $e^{-2V}g_0\le g(T)\le e^{2V}g_0$ | — |

The chain is strictly triangular: curvature $\to$ defect $\to$ velocity $\to$ metric.
No circular dependence exists.

## 10. Conditional status

**Proved (conditional on smooth degenerate-flow existence):**
- The general-$p$ power inequality (3.1) with polynomial $p$-growth.
- The three-factor absorption reducing the reaction to dissipation plus $S^4YK_p$.
- The Cauchy--Schwarz interpolation closing the $p\to3p/2$ recurrence.
- Moser product convergence with polynomial losses.

**Corrected from prior steps:**
- $\|aF(t)\|_\infty$ is uniformly bounded, not $C/t$.
- $\|aE(t)\|_\infty$ is uniformly $O(\delta)$, not $O(\delta/t^{1/3})$.
- The time-decay of $S^4Y(t)$ is a coefficient property, not an output property.

**Still conditional on:**
- (C1) Smooth existence of the degenerate normalized flow for $t\in[0,T]$.
- (C2) Metric comparability during the flow (closed by the velocity estimate
  for small $\delta\theta$, but requires (C1) first).
- (C3) Sobolev constant persistence (follows from metric comparability).
- (C4) A03's shifted-curvature continuation theorem for the extension/restart.

## Sources

- Step 25 tensor derivation: `workspace/notes/step25_tensor_energy_derivation.md`
- Step 24 buffered supports: `workspace/notes/step24_buffered_support_energy_test.md`
- A03 Step 31 interpolation: `Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md`
- Step 30 repair: `workspace/notes/step30_weighted_moser_and_family_repair.md`
- Verification: `workspace/scripts/step31_general_p_verification.py`
