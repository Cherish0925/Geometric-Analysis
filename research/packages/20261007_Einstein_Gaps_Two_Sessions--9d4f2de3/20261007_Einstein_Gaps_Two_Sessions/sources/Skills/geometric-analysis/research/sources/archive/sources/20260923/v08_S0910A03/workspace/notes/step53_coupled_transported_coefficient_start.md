# Step 53: [SUPERSEDED by Step 55 direct nonlinear construction]

# Step 53: Coupled transported-coefficient start theorem

> **Step 54 supersession.** The pullback identity and weighted structural observations in this note remain useful, but Theorem 5.1 and the Banach contraction in §4.4 are not proved. The frozen transport velocity depends on the input metric, whereas the weighted parabolic dissipation controls the output metric; interpolation supplies only one-half-Hölder dependence in the lower contraction norm. Section 6's claimed \(A^{-1/2}\) obstruction is also withdrawn: volume-weighted eligible cores normalize both \(\int\mathfrak D\) and their retained volume by \(A\), and the support radius can be fixed. See `step54_route_reassessment_and_joint_weighted_iteration.md`.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Mathematical outcome

The fixed-cutoff normalized flow $\partial_t g = -2\chi^2(\operatorname{Ric}_g+g)$ requires
a coupled metric–transport system in the DeTurck gauge (Step 52 §5).  This note
proves that the coupling closes through a staggered parabolic–ODE grading, and
states the resulting per-datum existence theorem as a source-supported extension
of Xu's Section 2 construction.

## 1. The exact coupled system

### 1.1 Variables and equations

Fix a closed Riemannian manifold $(M,g_0)$, a reference metric $\widetilde g=g_0$,
and a smooth function $\chi:M\to[0,1]$.  Set $a=\chi^2$.

**Geometric flow** (target):
$$
  \partial_t g = -2a(\operatorname{Ric}_g + g), \qquad g(0)=g_0.  \tag{1.1}
$$

**DeTurck gauge.**  Let $W(\widehat g,\widetilde g)$ denote the DeTurck vector
field, $W^k=\widehat g^{ab}(\widehat\Gamma^k_{ab}-\widetilde\Gamma^k_{ab})$.
The diffeomorphism $\varphi_t$ satisfies
$$
  \partial_t\varphi = -\widehat a\,W\circ\varphi, \qquad \varphi_0=\operatorname{id}.
  \tag{1.2}
$$
The transported cutoff is
$$
  \widehat\chi = \chi\circ\varphi^{-1}, \qquad \widehat a=\widehat\chi^2.
  \tag{1.3}
$$
The coupled DeTurck system is
$$
\boxed{
\begin{cases}
  \partial_t\widehat g
    = -2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
      +\mathcal L_{\widehat aW}\widehat g, \\[2pt]
  \partial_t\widehat\chi
    = \widehat a\,W^k\partial_k\widehat\chi
    = \widehat\chi^2\,W^k\partial_k\widehat\chi, \\[2pt]
  \widehat g(0)=g_0,\quad \widehat\chi(0)=\chi.
\end{cases}
}  \tag{1.4}
$$
The first equation is parabolic (degenerate where $\widehat\chi=0$); the second
is first-order transport by the field $\widehat aW$.

**Pullback identity.** Since $\chi$ is time-independent in geometric coordinates
and $\widehat\chi=\chi\circ\varphi^{-1}$, we have
$\widehat\chi\circ\varphi=\chi$ for all $t$.  Setting $g=\varphi^*\widehat g$,
the standard DeTurck computation and naturality of $\operatorname{Ric}$ give
$$
  \partial_t g
  = \varphi^*\bigl(-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)\bigr)
  = -2(\widehat a\circ\varphi)(\operatorname{Ric}_g+g)
  = -2\chi^2(\operatorname{Ric}_g+g),
$$
which is exactly (1.1).  $\square$

### 1.2 Key algebraic identities for $\widehat\chi$

Working with $\widehat\chi$ rather than $\widehat a$ preserves two structural
identities at the zero set:

**(I1)** $|\nabla\widehat a|^2/\widehat a = 4|\nabla\widehat\chi|^2$
wherever $\widehat\chi>0$, and $=0$ where $\widehat\chi=0$ by smoothness.

**(I2)** $\widehat a_1-\widehat a_2
         = (\widehat\chi_1+\widehat\chi_2)(\widehat\chi_1-\widehat\chi_2)$.

Identity (I2) is the factorization that makes contraction estimates for the
coefficient difference proportional to the $\widehat\chi$ difference, with a
bounded multiplier $\|\widehat\chi_1+\widehat\chi_2\|_\infty\le2$.

## 2. Principal structure analysis

### 2.1 Derivative orders in the coupling

Write $V=\widehat g-\widetilde g$ and $\psi=\widehat\chi$.  In Xu's
fixed-background framework relative to $\widetilde\nabla$:

**Metric equation:**
$$
  \partial_tV = \psi^2\widetilde g^{-1}*\widetilde\nabla^2V
    + D(\widetilde g+V,V) + B(\widetilde g+V,\widetilde\nabla V)
    - 2\psi^2(\widetilde g+V),
  \tag{2.1}
$$
where $D$ is algebraic in its second argument and $B$ is first-order.  The
coefficient $\psi^2$ involves **zero derivatives of $\psi$** in the principal part.

**Scalar transport:**
$$
  \partial_t\psi = \psi^2 W^k\partial_k\psi.
  \tag{2.2}
$$
The DeTurck vector $W$ involves **first derivatives of $V$** (through Christoffel
symbols).  The transport involves **first derivatives of $\psi$**.

**Coupling matrix (derivative orders):**

| | affects $V$ at order $k$ | affects $\psi$ at order $k$ |
|---|---|---|
| **$V$ derivatives needed** | $k+2$ (principal part) | $k+1$ (through $\nabla W$) |
| **$\psi$ derivatives needed** | $k$ (through coefficient $\psi^2$) | $k+1$ (through $\nabla\psi$) |

The coupling is **lower-triangular in derivative count**:
- The metric equation at order $k$ needs $\psi$ at order $k$ (same level, no loss).
- The transport at order $k$ needs $V$ at order $k+1$ (one above).

### 2.2 The parabolic–ODE grading


### 2.2 The weighted parabolic–ODE grading

The decisive mechanism is the **weighted parabolic dissipation**.  For the
$\varepsilon$-regularized equation with coefficient $b=\psi^2+\varepsilon$,
the energy estimate produces
$$
  \frac d{dt}\|V\|_{H^s}^2
  + c\int_M(\psi^2+\varepsilon)|\widetilde\nabla^{s+1}V|^2
  \le C\|V\|_{H^s}^2 + \text{lower},
  \tag{2.3}
$$
yielding $V\in C([0,T];H^s)$ and the **weighted** gain
$$
  \int_0^T\!\!\int_M(\psi^2+\varepsilon)|\widetilde\nabla^{s+1}V|^2\le C.
  \tag{2.4}
$$
The gain is weighted, not the unweighted $V\in L^2_TH^{s+1}$; the unweighted
norm may degenerate as $\varepsilon\to0$.

**The weight cancellation (central mechanism).**  The ODE velocity has
$\psi^2 W$, and at the top order,
$$
  \|\psi^2\widetilde\nabla^{s+1}V\|_2
  \le\|\psi\|_\infty\cdot\|\psi\widetilde\nabla^{s+1}V\|_2.
$$
The remaining terms in $\widetilde\nabla^s(\psi^2 W)$ involve at most $s$
derivatives of $V$ (by Leibniz), controlled by $\|V\|_{C_TH^s}$.  Hence
$$
  \int_0^T\|\psi^2 W\|_{H^s}dt
  \le C\|\psi\|_\infty\sqrt T\,
    \bigl(\int_0^T\|\psi\widetilde\nabla^{s+1}V\|_2^2\,dt\bigr)^{1/2}
  + C\sqrt T\,P(\|V\|_{C_TH^s},\|\psi\|_{C_TH^s}),
  \tag{2.5}
$$
which is finite by (2.4) and Cauchy–Schwarz.  The weight $\psi^2$ in the ODE
velocity is compensated by the weight $\psi^2$ in the parabolic dissipation.

**The Lie cross-term absorption.**  The term
$2\operatorname{sym}(d(\psi^2)\otimes W^\flat)$ in (2.1) produces
$\psi\nabla^{k+1}\psi*W$ at derivative order $k$.  In the energy estimate,
integrating by parts moves the derivative from $\psi$ to $V$:
$$
  \int\partial^kV\cdot\psi\nabla\psi\cdot W\cdot\partial^{k+1}\psi
  \leadsto
  \int\psi\partial^{k+1}V\cdot(\psi\nabla\psi\cdot W\cdot\partial^kV+\cdots)
$$
The factor $\psi\partial^{k+1}V$ is absorbed by the weighted dissipation
$\int\psi^2|\nabla^{k+1}V|^2$ via Cauchy–Schwarz.

**The diffeomorphism $\varphi$** solves the ODE (1.2).  Since
$\psi^2W\in L^1_tH^s$ by (2.5), the flow $\varphi$ preserves $H^s$ regularity
with Jacobian lower bound controlled by
$\int_0^T\|\nabla(\psi^2 W)\|_\infty dt$.

**The transported cutoff** $\psi=\chi\circ\varphi^{-1}$ then has
$\|\psi\|_{H^s}\le C(\|\chi\|_{C^s},\|\varphi\|_{H^s},
\inf_M\det D\varphi)$, which is controlled by the diffeomorphism.

**Staggered grading summary** (with $s=\widetilde p+2$ from Xu):

| Variable | $C_T$ regularity | Weighted $L^2_T$ | Source |
|---|---|---|---|
| $V$ (metric) | $H^{\widetilde p+2}$ | $\int\psi^2|\nabla^{\widetilde p+3}V|^2$ | parabolic eq (2.4) |
| $\varphi$ (diffeo) | $H^{\widetilde p+2}$ | — | ODE + (2.5) |
| $\psi=\chi\circ\varphi^{-1}$ | $H^{\widetilde p+2}$ | — | composition |
| $\psi^2W$ (ODE vel.) | — | in $L^1_tH^{\widetilde p+2}$ | (2.5) |

**Closure:**
- Metric energy at $H^{\widetilde p+2}$: coefficient $\psi$ available at
  $H^{\widetilde p+2}$; Lie cross-term absorbed by weighted dissipation.
- ODE at $H^{\widetilde p+2}$: $\psi^2W\in L^1_tH^{\widetilde p+2}$ by (2.5).
- Composition: $\varphi\in C_TH^{\widetilde p+2}$ with positive Jacobian.

**The grading closes.**  The weighted parabolic dissipation compensates both
the ODE velocity requirement and the Lie cross-term in the metric energy.

## 3. Transport energy estimate via integration by parts

The transport equation (2.2) preserves Sobolev norms through a standard energy
identity.

**Proposition 3.1** (Transport $H^k$ energy).
*Let $\psi$ solve $\partial_t\psi=\psi^2 W^k\partial_k\psi$ with smooth
bounded $(\psi,W)$.  Then*
$$
  \frac d{dt}\|\psi\|_{H^k}^2
  \le C\bigl(\|\psi\|_{H^k}^2\cdot\|\nabla\psi\|_{L^\infty}
       + \|\psi\|_{H^k}^2\cdot\|\operatorname{div}(\psi^2W)\|_{H^{k-1}}
       + \text{lower}\bigr)\|\psi\|_{H^k}^2.
$$

*Proof sketch.*  At the highest order $|\alpha|=k$:
$$
  \int\partial^\alpha\psi\cdot\psi^2W^j\partial_j\partial^\alpha\psi\,dV
  = -\tfrac12\int(\partial^\alpha\psi)^2\partial_j(\psi^2W^j)\,dV.
  \tag{3.1}
$$
The RHS involves only $\partial(\psi^2W)$, not $\partial^{k+1}\psi$.  The
commutator $[\partial^\alpha,\psi^2W^j\partial_j]\psi$ has terms of the form
$(\partial^{j_1}\psi^2)(\partial^{j_2}W)(\partial^{j_3+1}\psi)$ with
$j_1+j_2+j_3=k$ and $j_3<k$.  By Sobolev multiplication ($\widetilde p>n/2$),
these are bounded by $C(\|\psi\|_{H^k},\|W\|_{H^k})\cdot\|\psi\|_{H^k}$.

**Key point:** The top-order product $\psi^2W\cdot\nabla\partial^\alpha\psi$ is
absorbed by integration by parts (3.1) without needing $\psi$ at order $k+1$.
This is why the transport equation does not create derivative loss.

## 4. The coupled fixed-point map

### 4.1 Setup in Xu's framework

For $\varepsilon>0$, define the coupled frozen map
$\Phi_\varepsilon^N:(U,\alpha)\mapsto(V,\beta)$ on the product Banach ball
$$
  \mathcal B = \bigl\{(U,\alpha)\in
    C([0,T];H^{\widetilde p+2}\times H^{\widetilde p+2}):
    U\in A_T\cap B_{\widetilde p+2}(G),\;
    \|\alpha-\chi\|_{C_TH^{\widetilde p+2}}\le\rho
  \bigr\}
$$
by solving:

**Step 1 (metric):**
$$
  \partial_tV = (\alpha^2+\varepsilon)U^{-1}*\widetilde\nabla^2V
    + D(U,V) + B(U,\widetilde\nabla U)
    - 2\alpha^2 V - 2\alpha^2\widetilde g,
  \quad V(0)=0.
  \tag{4.1}
$$
This is Xu's frozen equation with coefficient $\alpha^2+\varepsilon$ replacing
$\chi^2+\varepsilon$, plus the algebraic normalization $-2\alpha^2V-2\alpha^2\widetilde g$.

**Step 2 (transport):**
$$
  \partial_t\beta = \alpha^2\,W(U)^k\partial_k\beta,
  \quad \beta(0)=\chi.
  \tag{4.2}
$$
This is a linear transport equation for $\beta$, with velocity $\alpha^2 W(U)$
determined by the frozen data $(\alpha,U)$.  Note: we freeze the velocity from
the INPUT $(U,\alpha)$, making the map fully explicit.

### 4.2 Invariant ball for the metric (Step 1)

The metric equation (4.1) differs from Xu's equation (2.5) in two ways:
1. The coefficient is $\alpha^2+\varepsilon$ instead of $\chi^2+\varepsilon$.
2. The algebraic reaction $-2\alpha^2V-2\alpha^2\widetilde g$ is added.

**Effect of (1):** Since $\alpha\in\mathcal B$ with $\|\alpha\|_\infty\le1$ and
$\|\alpha\|_{H^{\widetilde p+2}}\le\|\chi\|_{H^{\widetilde p+2}}+\rho$, the
coefficient $\alpha^2+\varepsilon$ has the same $\varepsilon$-uniform bounds as
Xu's $\chi^2+\varepsilon$.  All of Xu's estimates (Propositions 2.5, 2.7) carry
through with constants depending on $\|\alpha\|_{H^{\widetilde p+2}}$ instead of
$\|\chi\|_{H^{\widetilde p+2}}$; the ball membership controls this.

**Effect of (2):** As shown in Step 52 §3, the reaction $-2\alpha^2V$ adds
bounded Grönwall terms to the power traces $\phi_m,\psi_m$ (eigenvalue bounds)
and to the Sobolev energies $\|V\|_m^2$.  The source $-2\alpha^2\widetilde g$
is prescribed and bounded.  Xu's invariant ball holds after reducing $T$.

### 4.3 Invariant ball for the transport (Step 2)

The linear transport (4.2) has velocity $\alpha^2 W(U)$.  Since $\alpha$ and $U$
are in the invariant ball, $\|\alpha^2 W\|_{H^k}$ is bounded for all
$k\le\widetilde p+2$ (using $\|W(U)\|_{H^k}\le C\|U\|_{H^{k+1}}$ and Sobolev
multiplication).

By the energy estimate (Proposition 3.1) and the IBP mechanism (§3),
$\|\beta\|_{H^{\widetilde p+2}}$ satisfies a Grönwall inequality with bounded
coefficients.  For small $T$:
$$
  \|\beta(t)-\chi\|_{H^{\widetilde p+2}}
  \le C\,T\,\|\alpha^2 W(U)\|_{C_TH^{\widetilde p+2}}\|\chi\|_{H^{\widetilde p+3}}
  \le \rho/2
$$
after choosing $T$ small (depending on $g_0,\chi$).

### 4.4 Contraction estimate

Let $(V_i,\beta_i)=\Phi_\varepsilon^N(U_i,\alpha_i)$ for $i=1,2$.

**Metric contraction.**  Set $\mathcal W=V_1-V_2$.  The difference equation is
$$
  \partial_t\mathcal W
  = (\alpha_1^2+\varepsilon)U_1^{-1}*\widetilde\nabla^2\mathcal W
  + P(U_1)\mathcal W + \mathcal H,
$$
where the inhomogeneity $\mathcal H$ contains:

(a) $(\alpha_1^2-\alpha_2^2)(U_2^{-1}\widetilde\nabla^2V_2+\cdots)$:
    By (I2), $\alpha_1^2-\alpha_2^2=(\alpha_1+\alpha_2)(\alpha_1-\alpha_2)$,
    and by Sobolev multiplication in the $H^{\widetilde p+2}$ ball,
    $\|\alpha_1^2-\alpha_2^2\|_{H^{\widetilde p}}\le
    C(\|\alpha_1\|_{H^{\widetilde p}}+\|\alpha_2\|_{H^{\widetilde p}})
    \|\alpha_1-\alpha_2\|_{H^{\widetilde p}}$.  The factor
    $\|U_2^{-1}\widetilde\nabla^2V_2\|_{H^{\widetilde p}}$ is bounded from the
    invariant ball.

(b) $(U_1^{-1}-U_2^{-1})\widetilde\nabla^2V_2+\cdots$: standard Xu terms,
    estimated exactly as in Xu's Proposition 2.8, eqs. (2.31)--(2.46).

(c) $-2(\alpha_1^2-\alpha_2^2)(V_2+\widetilde g)$:
    algebraic, bounded by $C\|\alpha_1-\alpha_2\|_{H^{\widetilde p}}$.

(d) $2\operatorname{sym}(d(\alpha_1^2)\otimes W_1^\flat
    -d(\alpha_2^2)\otimes W_2^\flat)$: the Lie cross-term.
    Split as $d(\alpha_1^2-\alpha_2^2)\otimes W_1^\flat
    +d(\alpha_2^2)\otimes(W_1-W_2)^\flat$.

For the cross-term (d), $\|d(\alpha_1^2-\alpha_2^2)\|_{H^{\widetilde p-1}}\le
C\|\alpha_1-\alpha_2\|_{H^{\widetilde p}}$ (using the invariant ball), and
$\|W_1-W_2\|_{H^{\widetilde p}}$ involves $\|U_1-U_2\|_{H^{\widetilde p+1}}$.
This last term is one order higher than the contraction norm.  It is absorbed by
the **weighted parabolic dissipation** of $\mathcal W$, exactly as Xu absorbs
the analogous $J_{12.2}$ term (lines 916–953 of Xu's proof): the energy
estimate produces
$$
  \frac d{dt}\|\mathcal W\|_{\widetilde p}^2
  + c\int(\alpha_1^2+\varepsilon)|\widetilde\nabla^{\widetilde p+1}\mathcal W|^2
  \le \text{RHS},
$$
and the dangerous $\|\widetilde\nabla^{\widetilde p+1}\mathcal W\|$ terms from
(d) carry a factor $\|d(\alpha_2^2)\|_\infty\le C$ (from the invariant ball),
so they are absorbed with a $1/1000$ coefficient against the dissipation.

After absorption, the contraction estimate is:
$$
  \|\mathcal W\|_{T,\widetilde p}^2
  \le C_2 T e^{C_1T}\bigl(\|U_1-U_2\|_{T,\widetilde p}^2
       + \|\alpha_1-\alpha_2\|_{T,\widetilde p}^2\bigr).
  \tag{4.3}
$$

**Transport contraction.**  Set $\omega=\beta_1-\beta_2$.  The difference
satisfies
$$
  \partial_t\omega = \alpha_1^2 W(U_1)\cdot\nabla\omega
    + [\alpha_1^2 W(U_1)-\alpha_2^2 W(U_2)]\cdot\nabla\beta_2.
$$
The coefficient difference splits as
$\alpha_1^2 W_1-\alpha_2^2 W_2
= (\alpha_1^2-\alpha_2^2)W_1 + \alpha_2^2(W_1-W_2)$.

The $W_1-W_2$ term involves one extra derivative of $U_1-U_2$.  In the
$H^{\widetilde p}$ energy for $\omega$, this produces terms with
$\|\widetilde\nabla^{\widetilde p+1}(U_1-U_2)\|$ acting on $\nabla\beta_2$
(bounded from the invariant ball).  These terms carry a factor $\alpha_2^2$
and are bounded by the $U_1,U_2$ invariant-ball membership:
$$
  \|\alpha_2^2(W_1-W_2)\cdot\nabla\beta_2\|_{H^{\widetilde p}}
  \le C\|U_1-U_2\|_{H^{\widetilde p}}
$$
(using Sobolev multiplication and the higher-order bound on $U_1-U_2$ from
interpolation: $\|h\|_{H^{r+1}}\le C\|h\|_{H^r}^{1/2}\|h\|_{H^{r+2}}^{1/2}$,
with $\|h\|_{H^{r+2}}$ bounded by the ball radius).

By Grönwall on the $H^{\widetilde p}$ energy of $\omega$:
$$
  \|\omega\|_{T,\widetilde p}^2
  \le C_4 T e^{C_3T}\bigl(\|U_1-U_2\|_{T,\widetilde p}^2
       + \|\alpha_1-\alpha_2\|_{T,\widetilde p}^2\bigr).
  \tag{4.4}
$$

**Combined contraction.**  In the product norm
$\|(V,\beta)\|=\|V\|_{T,\widetilde p}+\|\beta\|_{T,\widetilde p}$:
$$
  \|(V_1-V_2,\beta_1-\beta_2)\|
  \le C\sqrt{T}e^{CT}\|(U_1-U_2,\alpha_1-\alpha_2)\|.
$$
For $T$ small enough, this is $<\delta<1$.  $\square$

**TTCS corrections incorporated:** The parabolic dissipation is weighted, not
unweighted; the $\|U_1-U_2\|_{H^{\widetilde p+1}}$ terms in the Lie cross-term
and transport are absorbed by Xu's $J_{12.2}$-type mechanism (metric) and
interpolation (transport), not by the false inequality
$\|h\|_{H^{r+1}}\le C\|h\|_{H^r}$.

### 4.5 The $\varepsilon\to0$ limit and smooth geometric solution

The $\varepsilon$-independent high-Sobolev bounds (from §4.2 and §4.3, uniform
in $\varepsilon$) give precompactness of the family
$\{(\widehat g_\varepsilon,\psi_\varepsilon)\}$ in
$C([0,T];H^{\widetilde p+1}\times H^{\widetilde p+1})$.  A subsequence converges
to $(\widehat g,\psi)$ solving the degenerate system (1.4).

Smoothness in $\{\psi>0\}$ follows from parabolic regularity (the equation is
strictly parabolic there).  On the interior of $\{\psi=0\}$, all terms vanish and
$\widehat g$ is stationary.  Smoothness across $\partial\{\psi>0\}$ follows from
the global fixed-background Sobolev bounds at arbitrary order (Proposition 2.7
applied to the coupled ball, as in Xu's Theorem 2.9).

The geometric solution $g=\varphi^*\widehat g$ with $\varphi$ from (1.2) then
satisfies (1.1) on $[0,T]$.

## 5. Per-datum existence theorem

**Theorem 5.1** (Normalized Xu–Yang start with transported coefficient).
*Let $(M,g_0)$ be a closed Riemannian manifold and $\chi:M\to[0,1]$ a smooth
function.  There exists $T=T(g_0,\chi)>0$ and a smooth family of metrics $g(t)$,
$t\in[0,T]$, solving*
$$
  \partial_tg = -2\chi^2(\operatorname{Ric}_g+g), \qquad g(0)=g_0.
$$
*The same construction provides restart from any smooth positive-definite datum.
The time $T$ depends on the full smooth geometry of $(g_0,\chi)$ and is not
asserted to be uniform across a family.*

**Proof outline.**
1. Regularize $\psi^2\mapsto\psi^2+\varepsilon$ in (4.1) and solve the coupled
   fixed-point $\Phi_\varepsilon^N$ on $\mathcal B$ (§4.1–4.4).  Xu's argument
   (Proposition 2.5, 2.7, 2.8, Theorem 2.9) extends to the product ball with the
   modifications in §4.2–4.4.
2. Pass $\varepsilon\to0$ using $\varepsilon$-independent bounds (§4.5).
3. Recover the geometric flow via the pullback (§1.1).

**What is imported from Xu:**
- The scalar parabolic existence (Theorem 8.3 in [Li–Tam] cited by Xu).
- The bilipschitz ball and Sobolev energy estimates (Propositions 2.5, 2.7).
- The contraction structure (Proposition 2.8).
- The Arzelà–Ascoli compactness for $\varepsilon\to0$ (Theorem 2.9).

**What is new in this note:**
- The coupled product ball $\mathcal B$ with the transport variable $\psi$.
- The IBP transport energy estimate (§3) that prevents derivative loss.
- The parabolic–ODE grading (§2.2) that closes the regularity chain.
- The coefficient-difference factorization (I2) in the contraction (§4.4).
- The algebraic normalization $-2\psi^2V-2\psi^2\widetilde g$ treated as in
  Step 52 §3.

## 6. A02 critical-product scaling and structural limitation

A02 message #382 (independently confirmed) identifies a structural limitation:
the terminal spectral density $\int_M\mathfrak D\le119Q$ involves the
**global** Seiberg–Witten monopole inequality, so
$Q=\int_M|E|^2\le C\delta^2\operatorname{Vol}(M)\le C'\delta^2 A$.  Localizing
to a unit core ball gives average $\mathfrak D\le C'\delta^2 A/\operatorname{Vol}(B_1)$.

For the spectral contradiction to work, $\delta^2 A\to0$, hence
$\delta_0\le c/\sqrt A$.  As $A\to\infty$ (more complex topology),
$\delta_0\to0$.

**Consequence:** The restricted negative IL theorem gives a per-topology gap
$\delta_0(A)>0$ for each fixed $A$, but $\inf_A\delta_0(A)=0$.  It cannot
produce dimension-only constants $c_4,C_4$ for Yau Problem 26.

This is structural: the Seiberg–Witten lower bound is global, and localizing it
to a core ball introduces the global volume, which scales with $A$.  No
improvement within the current localized-flow framework can remove this
$A$-dependence without replacing the global topological input.

**What the restricted theorem would establish (if completed):**
For each closed 4-manifold $M$ in the critical IL family with parameter $A$,
no smooth metric $g$ with $\|\operatorname{Ric}_g+g\|_\infty<c/\sqrt A$
can exist.  Equivalently, $M$ does not admit Einstein metrics with
$\operatorname{Ric}=-\lambda g$ for $\lambda$ near 1 with tolerance
$c/\sqrt A$.  This is a meaningful obstruction-theory result but not a
resolution of the all-dimensional Yau 26 question.

## 7. Supersession and file status

- Step 52's §3 "Proposition 3.1" (metric-only Xu extension): **superseded** by
  the coupled system here (the metric-only version has the wrong pullback).
- Step 51's L^p energy closure: **remains falsified** by the flat-torus test.
- Step 50's Yang lower-order perturbation analysis: **compatible** with this
  note; the transported-coefficient system is equivalent to Yang's Approach 1
  with the normalization perturbation.
- Step 50's staggered Wang continuation: **separate and preserved** for
  positive-time extension after the flow exists.

## 8. What remains for the restricted negative IL result

1. **Theorem 5.1 needs verification**: The contraction estimates (4.3)–(4.4)
   use Xu's structure but with the coupled product.  An independent TTCS or
   source-level check should confirm the cross-term absorption.

2. **Sequence-uniform first-exit**: Even with the start theorem, the critical
   product $\bar\beta\sim O(A^{1/2})$ (A02 §3) means the flow observation time
   and terminal estimates are A-dependent.  The first-exit chain
   $K_2\to Y\to J_6\to\text{all-}p$ must be checked with explicit A-dependence.

3. **Terminal spectral argument**: Requires the global $\int\mathfrak D$ bound,
   which introduces the $A^{1/2}$ factor.

4. **The broader Yau 26**: Positive branch, arbitrary 4-manifold topology,
   $n\ge5$, dimension-only constants, and Lean formalization remain untouched.
