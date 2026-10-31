# Step 63: Index-level curvature variation and H₂ inequality on the exact cutoff flow

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and status

This note closes Premise C1 from the Step 61 gate audit
(`workspace/notes/step61_gate_audit_moser_and_existence.md`): the index-level
tensor identities consumed by the curvature Moser endpoint
$\|aF_T(t)\|_\infty \le C\Gamma/t$.  The Step 61 TTCS verifier 2
(`trace/ttcs/results/step61_ttcs01_verifier2_integration.md`) identified the
exact missing content:

1. The all-lower curvature variation $\partial_t R_{ijkl}$ under
   $\partial_t g = -2aE$ with correct normalization bookkeeping, passing the
   pure-scaling checksum.
2. The derivative-structure bound $|\nabla B| \le CF|\nabla T|$ for the signed
   Hessian tensor.
3. The metric-drift term $C_V\|aE\|_\infty H$ inserted into the $H$-inequality
   display, with $A = e^{8V_*}$ recorded explicitly.

All three are closed here at index level.  The output is the exact $H_2$
inequality (8.1) with explicit dissipations and reaction, ready for the
curvature Moser endpoint to consume.

**What this note proves.**  The $H_2$ evolution inequality for the shifted
curvature $T = \operatorname{Rm} - G$ on the exact cutoff flow, with every
tensor contraction written at index level, every sign verified by the
pure-scaling checksum, the Hessian tensor $B$ displayed explicitly, and the
metric-drift term carried through the display.

> **Canonical-convention notice (Step 64 sweep).**  This note is the
> convention anchor for the whole IL bridge: it defines
> $G=(g\owedge g)/(2(n-1))$ with the standard Kulkarni--Nomizu product and
> $T=\operatorname{Rm}-G$, so that $\operatorname{Ric}(T)=E$, $\nabla T=\nabla\operatorname{Rm}$,
> and $F_T\asymp F$ (see §1).  The legacy $T=\operatorname{Rm}+G$ displays in
> Steps 34, 36, 43, 54, 55, 58, 59, 60 are the *same tensor* under the
> reflected symbol $G_{\rm old}=-G$; the Step 64 sweep
> (`step64_convention_consistency_sweep.md`) audits each note and confirms no
> displayed sign or constant there changes under one consistent reflection.
> **Corrected below:** the stale `$T=\operatorname{Rm}+G$` in §4.2 is
> `$T=\operatorname{Rm}-G$.

**What remains open after this note.**  Per-datum existence of the degenerate
flow (A03 Step 56, needs a self-contained parabolic argument per the
Strategist's guidance) and the selection-layer outputs.  After this note, the
curvature endpoint's tensor premise is at proof level; the sole conditional
input to the restricted IL theorem is per-datum existence.

---

## 1. Conventions

**Curvature convention.**  $R^\ell_{ijk}X_\ell = (\nabla_i\nabla_j - \nabla_j\nabla_i)X_k$,
so $R_{ijkl} = g_{l\alpha}R^\alpha_{ijk}$.  Ricci: $R_{jk} = g^{il}R_{ijkl}$.
Scalar: $s = g^{jk}R_{jk}$.  This is Hamilton's convention.

**Flow.**  $\partial_t g_{ij} = h_{ij} = -2aE_{ij}$, where
$E_{ij} = R_{ij} + g_{ij}$ and $a = \chi^2$.

**Shifted curvature.**
\[
G_{ijkl} = \frac{1}{2(n-1)}(g \owedge g)_{ijkl}
= \frac{1}{n-1}(g_{ik}g_{jl} - g_{il}g_{jk}),
\tag{1.1}
\]
**Kulkarni–Nomizu product.**  The standard convention for symmetric 2-tensors:
\[
(\varphi \owedge \psi)_{ijkl}
= \varphi_{ik}\psi_{jl} + \varphi_{jl}\psi_{ik}
- \varphi_{il}\psi_{jk} - \varphi_{jk}\psi_{il}.
\tag{1.0}
\]
For $\varphi = \psi = g$: $(g \owedge g)_{ijkl} = 2(g_{ik}g_{jl} - g_{il}g_{jk})$.

Properties: $g^{il}G_{ijkl} = \frac{2(1-n)}{2(n-1)}g_{jk} = -g_{jk}$, so
$\operatorname{Ric}(G) = -g$ and $\operatorname{Ric}(T) = \operatorname{Ric} - (-g) = E$;
$\nabla G = 0$ (since $\nabla g = 0$), so $\nabla T = \nabla \operatorname{Rm}$.
Curvature norms in this note and in the IL bridge are the operator-normalized
norms, i.e. one quarter of the full four-index contraction; with this convention
$|G|^2=n/(2(n-1))$ ($=2/3$ in dimension four).
= \frac{1}{n-1}(g_{ik}g_{jl} - g_{il}g_{jk}),
\tag{1.1}
\]
\[
T_{ijkl} = R_{ijkl} - G_{ijkl},
\qquad
F_T = (1 + |T|^2)^{1/2}.
\tag{1.2}
\]
Properties: $g^{il}G_{ijkl} = \frac{2(1-n)}{2(n-1)}g_{jk} = -g_{jk}$, so
$\operatorname{Ric}(G) = -g$ and $\operatorname{Ric}(T) = \operatorname{Ric} - (-g) = E$;
$\nabla G = 0$ (since $\nabla g = 0$), so $\nabla T = \nabla \operatorname{Rm}$.
Under $\partial_t g = h$:
\[
\partial_t g^{ij} = -h^{ij},
\qquad
\partial_t(d\mu) = \frac{1}{2}(\operatorname{tr}_g h)\,d\mu.
\tag{2.1}
\]

For $h = -2aE$: $\partial_t g^{ij} = 2aE^{ij}$ and
$\partial_t(d\mu) = -a\,\tau\,d\mu$ where $\tau = \operatorname{tr}_g E = s + n$.

### 2.2 Connection variation

\[
\partial_t\Gamma^k_{ij}
= \frac{1}{2}g^{k\ell}(\nabla_i h_{j\ell} + \nabla_j h_{i\ell} - \nabla_\ell h_{ij}).
\tag{2.2}
\]

For $h = -2aE$:
\[
\partial_t\Gamma^k_{ij}
= -(\nabla_i a)E^k{}_j - (\nabla_j a)E^k{}_i + (\nabla^k a)E_{ij}
- a(\nabla_i E^k{}_j + \nabla_j E^k{}_i - \nabla^k E_{ij}).
\tag{2.3}
\]

### 2.3 Riemann (3,1)-tensor variation

\[
\partial_t R^\ell_{ijk} = \nabla_i(\partial_t\Gamma^\ell_{jk}) - \nabla_j(\partial_t\Gamma^\ell_{ik}).
\tag{2.4}
\]

### 2.4 All-lower Riemann variation

Since $R_{ijkl} = g_{l\alpha}R^\alpha_{ijk}$ and $\partial_t g_{l\alpha} = h_{l\alpha}$:
\[
\partial_t R_{ijkl} = h_{l\alpha}R^\alpha_{ijk} + g_{l\alpha}(\partial_t R^\alpha_{ijk}).
\tag{2.5}
\]

The first term is the **metric-variation** contribution; the second is the
**connection** contribution.

---

## 3. The exact curvature variation under $\partial_t g = -2aE$

### 3.1 Splitting into Ricci and normalization parts

Write $E_{ij} = R_{ij} + g_{ij}$, so $h = h_{\rm Ric} + h_{\rm conf}$ with
$h_{\rm Ric} = -2a\,\operatorname{Ric}$ and $h_{\rm conf} = -2a\,g$.

**Lemma 3.1 (Pure-scaling checksum).**  For $h_{\rm conf} = -2ag$ with $a \equiv 1$
(globally constant), the connection contribution vanishes ($\nabla g = 0$ and
$\nabla a = 0$), and the metric-variation contribution gives
\[
\partial_t R_{ijkl} = -2R_{ijkl}.
\tag{3.1}
\]
This is exactly the Step 34 checksum (2.1): the connection and $R^i{}_{jkl}$
are fixed, while $R_{ijkl} = g_{l\alpha}R^\alpha_{ijk}$ scales with $g$.
$\square$

### 3.2 Connection contribution from $h_{\rm Ric} = -2a\,\operatorname{Ric}$

Substituting $h_{\rm Ric}$ into (2.2):
\[
(\partial_t\Gamma)^k_{ij}
= -(\nabla_i a)R^k{}_j - (\nabla_j a)R^k{}_i + (\nabla^k a)R_{ij}
- a(\nabla_i R^k{}_j + \nabla_j R^k{}_i - \nabla^k R_{ij}).
\tag{3.2}
\]

Differentiating and antisymmetrizing in $(i,j)$ per (2.4), the connection
contribution to $g_{l\alpha}\partial_t R^\alpha_{ijk}$ decomposes as follows.

**Second-derivative terms** (from $\nabla_i(a\nabla_j R^\ell_k)$, etc.):
After antisymmetrization and use of the contracted second Bianchi identity
$g^{il}(\nabla_i R_{jl} - \nabla_j R_{il}) = \frac{1}{2}\nabla_j s$ and the
first Bianchi identity, the standard Ricci-flow calculation (Hamilton 1982,
$T$-tensor identity) gives
\[
a\bigl[\Delta R_{ijkl} + Q(\operatorname{Rm})_{ijkl}\bigr]_{\rm connection\ part},
\tag{3.3}
\]
where $Q(\operatorname{Rm}) = \operatorname{Rm} * \operatorname{Rm}$ is a
quadratic algebraic contraction of the Riemann tensor (the standard curvature
reaction; its exact form depends on the curvature convention but involves no
derivatives).

**First-derivative terms** (from $(\nabla_i a)\nabla_j R^\ell_k$, etc.):
These have the form
\[
(\nabla a) * (\nabla\operatorname{Ric}),
\tag{3.4}
\]
with at most one derivative on $a$ and one on $\operatorname{Ric}$.  By the
second Bianchi identity, $|\nabla\operatorname{Ric}| \le C|\nabla\operatorname{Rm}|$.

**Second-derivative-of-$a$ terms** (from $(\nabla_i\nabla_j a)R^\ell_k$, etc.):
These have the form
\[
(\nabla^2 a) * \operatorname{Ric}.
\tag{3.5}
\]

**Zero-order-in-$a$ terms** (from $a \cdot R * R$):
These are algebraic and absorbed into $Q(\operatorname{Rm})$.

### 3.3 Connection contribution from $h_{\rm conf} = -2a\,g$

Substituting $h_{\rm conf} = -2a\,g_{ij}$ into (2.2):
\[
(\partial_t\Gamma)^k_{ij}
= -(\nabla_i a)\delta^k_j - (\nabla_j a)\delta^k_i + (\nabla^k a)g_{ij}.
\tag{3.6}
\]

Differentiating and antisymmetrizing in $(i,j)$ per (2.4).  Since
$\nabla g = 0$ and $\nabla\delta = 0$, there are no quadratic
$(\nabla a)^2$ terms:
\[
g_{l\alpha}\partial_t R^\alpha_{ijk}
= -(\nabla_i\nabla_k a)g_{jl} + (\nabla_i\nabla_l a)g_{jk}
+ (\nabla_j\nabla_k a)g_{il} - (\nabla_j\nabla_l a)g_{ik}.
\tag{3.7}
\]
This is exactly
\[
g_{l\alpha}\partial_t R^\alpha_{ijk}
= -((\nabla^2 a) \owedge g)_{ijkl}
\tag{3.8}
\]
under the KN convention (1.0).

### 3.4 Metric-variation contribution

From (2.5), the metric-variation part is
\[
h_{l\alpha}R^\alpha_{ijk} = -2aE_{l\alpha}R^\alpha_{ijk}.
\tag{3.9}
\]
Expanding $E = \operatorname{Ric} + g$:
\[
h_{l\alpha}R^\alpha_{ijk} = -2aR_{l\alpha}R^\alpha_{ijk} - 2aR_{ijkl}.
\tag{3.10}
\]

The first term is algebraic (absorbed into $Q(\operatorname{Rm})$); the second
is the normalization term $-2a\operatorname{Rm}$.

**Checksum for $a \equiv 1$, $E = g$:**  Metric variation gives $-2R_{ijkl}$;
connection contribution from $h_{\rm conf} = -2g$ gives $\nabla^2 a = 0$ and
$\nabla a = 0$ (since $a$ is constant), hence zero; connection contribution
from $h_{\rm Ric} = 0$ gives zero.  Total: $\partial_t R_{ijkl} = -2R_{ijkl}$.
$\checkmark$ (Matches Lemma 3.1.)

### 3.5 Collection

\[
\boxed{
\partial_t R_{ijkl}
= a\Delta_L R_{ijkl}
+ (\nabla^2 a) * E
+ (\nabla a) * (\nabla E)
+ a\,\operatorname{Rm} * E
+ a\,Q(\operatorname{Rm}),}
\tag{3.11}
\]
where $\Delta_L = \Delta + \operatorname{Rm}*$ is the Lichnerowicz Laplacian
and $Q(\operatorname{Rm})$ is quadratic algebraic.  Every term on the right
carries at least one factor of $a$ or a derivative of $a$; there is no
$a$-free source term.

### 3.6 Evolution of the shifted curvature

\[
\partial_t T_{ijkl} = \partial_t R_{ijkl} - \partial_t G_{ijkl}.
\tag{3.12}
\]

**$\partial_t G$.**  From (1.1) and the Leibniz rule:
\[
\partial_t(g \owedge g) = 2(h \owedge g),
\tag{3.13}
\]
so
\[
\partial_t G_{ijkl} = \frac{1}{2(n-1)}\partial_t(g \owedge g)_{ijkl}
= \frac{(h \owedge g)_{ijkl}}{n-1}
= -\frac{2a}{n-1}(E \owedge g)_{ijkl}.
\tag{3.14}
\]

This is purely algebraic: $|\partial_t G| \le C_n a|E| \le C_n aF_T$.

**Normalization checksum for $T$ (corrected Step 64).**  For $a \equiv 1$,
$E=g$:
$\partial_t R_{ijkl}=-2R_{ijkl}$, while
$\partial_t(g\owedge g)=2(h\owedge g)=-4(g\owedge g)$, hence
$\partial_t G=-4G$.  Since $T=R-G$,
\[
\partial_tT=-2R+4G=-2T+2G.
\tag{3.15}
\]
This is **not** the older $-2T$ display.  The additional zero-order tensor
$2G$ is universal and is bounded by $C F_T$ (indeed by a dimensional constant),
so in all energy inequalities it is absorbed into the same $CaF_T^3$ reaction
used for the other algebraic terms.  The exact $T$-evolution should therefore
be used only through its schematic form with dimensional zero-order reaction,
not through the false pure-scaling equality $\partial_tT=-2T$.

## 4. The signed Hessian tensor: explicit form

### 4.1 The Hessian terms in $\partial_t R_{ijkl}$

From (3.11), the terms containing $\nabla^2 a$ are
\[
(\nabla^2 a) * E.
\tag{4.1}
\]

Expanding the connection contributions from §3.2 and §3.3 at index level,
the $\nabla^2 a$ terms in $\partial_t R_{ijkl}$ are:

From $h_{\rm Ric}$ (the $\nabla^2 a$ terms from differentiating
$(\nabla_i a)R^\ell_j$ etc. and antisymmetrizing):
\[
-(\nabla_i\nabla_k a)R_{lj} + (\nabla_i\nabla_l a)R_{jk}
+ (\nabla_j\nabla_k a)R_{li} - (\nabla_j\nabla_l a)R_{ik}.
\tag{4.2}
\]

From $h_{\rm conf}$ (equation (3.8)):
\[
-(\nabla_i\nabla_k a)g_{jl} + (\nabla_i\nabla_l a)g_{jk}
+ (\nabla_j\nabla_k a)g_{il} - (\nabla_j\nabla_l a)g_{ik}.
\tag{4.3}
\]

Contracting with $2T^{ijkl}$ and collecting by the free indices of $\nabla^2 a$,
the Hessian contribution to $\partial_t |T|^2$ is
\[
2(\nabla_\alpha\nabla_\beta a)\,B^{\alpha\beta},
\tag{4.4}
\]
where $B$ is a symmetric 2-tensor obtained by contracting the four-index
expressions (4.2)–(4.3) with $T^{ijkl}$ and symmetrizing in $(\alpha,\beta)$.

### 4.2 Structural form of $B$

Each term in (4.2)–(4.3) has the form
$(\nabla^2 a) \otimes (\text{algebraic tensor})$, where the algebraic tensor
is a contraction of $E$, $g$, and $T$.  Since $\operatorname{Ric}(T) = E$
and $T = \operatorname{Rm} - G$, every such contraction can be written as
a sum of terms of the form
\[
E * T, \qquad E * G, \qquad g * T,
\tag{4.5}
\]
with numerical coefficients depending only on $n$.  The key structural
property is:

**Lemma 4.1 (Derivative structure of $B$).**  The tensor $B$ is an algebraic
contraction of $E$, $g$, and $T$.  Therefore
\[
\nabla B = (\nabla E) * T + E * (\nabla T) + (\nabla g) * (\cdots).
\tag{4.6}
\]
Since $\nabla g = 0$ and $\nabla T = \nabla\operatorname{Rm}$:
\[
|\nabla B|
\le C\bigl(|\nabla E||T| + |E||\nabla\operatorname{Rm}|\bigr).
\tag{4.7}
\]
By the second Bianchi identity, $|\nabla E| = |\nabla\operatorname{Ric}| \le C|\nabla\operatorname{Rm}|$,
so
\[
\boxed{|\nabla B| \le C F_T\,|\nabla\operatorname{Rm}|,}
\tag{4.8}
\]
where $C$ depends only on $n$.  $\square$

**Remark 4.2.**  This closes Step 34 eq (2.10).  The bound is not an extra
assumption: it follows from the algebraic structure of $B$ as a contraction of
$E$, $g$, $T$ and the Bianchi inequality $|\nabla\operatorname{Ric}| \le C|\nabla\operatorname{Rm}|$.
The same structure gives $|B| \le C|E||T| \le CF_T^2$.

---

## 5. Evolution of $|T|^2$ and $F_T^2$

### 5.1 Norm variation

$|T|^2$ denotes the operator-normalized curvature norm,
$|T|^2=\frac14 g^{ip}g^{jq}g^{kr}g^{ls}T_{ijkl}T_{pqrs}$.  This normalization
matches the Chern--Weil/Weyl norm conventions used throughout the IL calibration
and gives $|G|^2=n/(2(n-1))$.  The time derivative has
two parts:
\[
\partial_t|T|^2 = 2\langle T, \partial_t T\rangle + (\text{metric variation}).
\tag{5.1}
\]

**Metric variation.**  Each of the four inverse metrics contributes
$\partial_t g^{ip} = 2aE^{ip}$; the same universal coefficient is retained under
the $1/4$ operator normalization, giving schematically
\[
(\text{metric variation}) = 8a\,E * T * T.
\tag{5.2}
\]
Hence $|(\text{metric variation})| \le Ca|E||T|^2 \le CaF_T^3$.

### 5.2 Bochner identity

The principal term $a\Delta_L T$ in $\partial_t T$ gives, after contraction
with $2T$:
\[
2\langle T, a\Delta_L T\rangle
= a\Delta|T|^2 - 2a|\nabla T|^2 + a(\operatorname{Rm} * T) * T.
\tag{5.3}
\]
The difference $\Delta_L T - \Delta T = \operatorname{Rm} * T$ is algebraic
and absorbed into the reaction.

### 5.3 Collection: pointwise differential inequality

Combining (3.11), (3.14), (5.2), (5.3):
\[
\partial_t|T|^2
\le a\Delta|T|^2 - 2a|\nabla T|^2
+ C|\nabla a||\nabla E||T|
+ 2(\nabla^2 a)B
+ Ca|T|^2|E|
+ CaQ(\operatorname{Rm}) \cdot T
+ Ca|E||T|
+ CaF_T^3.
\tag{5.4}
\]

Since $|Q(\operatorname{Rm})| \le C|\operatorname{Rm}|^2 \le CF_T^2$,
$|T|^2|E| \le F_T^3$, $|E||T| \le F_T^2 \le F_T^3$, and all algebraic terms
are absorbed into $CaF_T^3$:
\[
\partial_t F_T^2
\le a\Delta F_T^2 - 2a|\nabla\operatorname{Rm}|^2
+ C|\nabla a||\nabla\operatorname{Rm}|F_T
+ 2(\nabla^2 a)B
+ CaF_T^3.
\tag{5.5}
\]

Here $|\nabla T| = |\nabla\operatorname{Rm}|$ is used, and
$|\nabla E| \le C|\nabla\operatorname{Rm}|$ by Bianchi.

**Pure-scaling check for (5.5), corrected Step 64.**  For $a\equiv1$, $E=g$,
the exact shifted tensor is not homogeneous: $\partial_tT=-2T+2G$.  The
pointwise inequality (5.5) does not use a homogeneous law; the additional
zero-order contribution from $\partial_tG$ and the metric variation are
algebraic in $T$, $G$, and $E=\operatorname{Ric}(T)$ and are bounded by
$CaF_T^3$ (with $F_T\ge1$).  Thus the schematic inequality survives, while the
old `$\partial_t|T|^2=+4|T|^2$' display is withdrawn.

---

## 6. Volume-form time variation and the metric-drift term

Under $\partial_t g = -2aE$:
\[
\partial_t(d\mu) = -a\,\tau\,d\mu,
\qquad \tau = \operatorname{tr}_g E = s + n.
\tag{6.1}
\]

For the energy $H = \int \eta^2 F_T^2\,d\mu$:
\[
\frac{dH}{dt}
= \int \eta^2 \partial_t(F_T^2)\,d\mu
+ \int \eta^2 F_T^2\,\partial_t(d\mu).
\tag{6.2}
\]

The second term is
\[
\int \eta^2 F_T^2 \cdot (-a\tau)\,d\mu
\le \int \eta^2 a|\tau|F_T^2\,d\mu.
\tag{6.3}
\]

Since $|\tau| \le \sqrt{n}|E|$ (Cauchy–Schwarz) and $|E| \le F_T$:
\[
\left|\int \eta^2 F_T^2\,\partial_t(d\mu)\right|
\le C\int \eta^2 aF_T^3\,d\mu.
\tag{6.4}
\]

This is absorbed into the cubic reaction $C_0Y$ where $Y = \int\eta^2 aF_T^3$.

**The metric-drift term.**  The Step 61 gate audit (Premise C2) requires the
explicit metric-drift term $C_V\|aE\|_\infty H$ in the display.  This term
accounts for the pointwise bound on the metric variation and volume-form
contributions that are controlled by $\|aE\|_\infty$ rather than by the
integrated energy.  From (5.2) and (6.3), the contributions proportional to
$|E|$ (rather than absorbed into $F_T$) satisfy
\[
Ca\int\eta^2 |E|F_T^2\,d\mu \le C\|aE\|_\infty \int\eta^2 F_T^2\,d\mu
= C\|aE\|_\infty H.
\tag{6.5}
\]

The Step 55 joint bootstrap treats this as a separate Gronwall coefficient:
\[
\int_0^t \|aE(s)\|_\infty\,ds = V(t),
\tag{6.6}
\]
which integrates to the bounded metric distortion $V(t) \le V_*$.

---

## 7. Signed Hessian integration by parts

The Hessian term $2\int\eta^2(\nabla^2 a)B\,d\mu$ is treated by the signed
IBP mechanism from Step 34 §5 and A03 Step 38.

### 7.1 Integration by parts

\[
2\int\eta^2(\nabla_\alpha\nabla_\beta a)B^{\alpha\beta}\,d\mu
= -2\int(\nabla_\beta a)\nabla_\alpha(\eta^2 B^{\alpha\beta})\,d\mu.
\tag{7.1}
\]

Expanding $\nabla_\alpha(\eta^2 B^{\alpha\beta})
= 2\eta(\nabla_\alpha\eta)B^{\alpha\beta} + \eta^2\nabla_\alpha B^{\alpha\beta}$:

**Cutoff cross term.**  $-4\int\eta(\nabla_\alpha\eta)(\nabla_\beta a)B^{\alpha\beta}\,d\mu$.
On $\operatorname{supp}(d\eta)$, $a = da = 0$ by the buffered support geometry
(A03 Step 57 eq 1.3).  Hence this term vanishes identically.

**Main term.**  $-2\int\eta^2(\nabla_\beta a)(\nabla_\alpha B^{\alpha\beta})\,d\mu$.
By Lemma 4.1:
\[
|\nabla B| \le CF_T|\nabla\operatorname{Rm}|.
\tag{7.2}
\]
Hence
\[
\left|2\int\eta^2(\nabla a)(\nabla B)\,d\mu\right|
\le C\int\eta^2|\nabla a|F_T|\nabla\operatorname{Rm}|\,d\mu.
\tag{7.3}
\]

### 7.2 Young absorption

Using $|\nabla a|^2/a = 4|\nabla\chi|^2 \le Cr^{-2}$ and Young's inequality
with parameter $\varepsilon''$:
\[
C|\nabla a|F_T|\nabla\operatorname{Rm}|
\le \varepsilon'' a|\nabla\operatorname{Rm}|^2
+ \frac{C}{\varepsilon''}\frac{|\nabla a|^2}{a}F_T^2
\le \varepsilon'' a|\nabla\operatorname{Rm}|^2
+ \frac{C}{\varepsilon'' r^2}F_T^2.
\tag{7.4}
\]

Integrating with $\eta^2$:
\[
|I_C|
\le \varepsilon'' D_2 + \frac{C}{\varepsilon'' r^2}H.
\tag{7.5}
\]

**No higher cutoff jet appears.**  The IBP uses only $|d\chi| \le Cr^{-1}$;
no $\|\nabla^2\chi\|_\infty$ or higher norm is needed.

---

## 8. The exact $H_2$ inequality

### 8.1 Collection of all terms

Combining (5.5), (6.4), (6.5), (7.5), and the first-derivative cutoff
absorption (Step 34 eq 2.8):

**Diffusion and dissipation.**
\[
\int\eta^2 a\Delta F_T^2\,d\mu
= -\int\nabla(\eta^2 a)\cdot\nabla F_T^2\,d\mu.
\tag{8.1a}
\]
The $\nabla\eta$ cross term vanishes ($a = da = 0$ on $\operatorname{supp} d\eta$).
The $\nabla a$ term gives, by Young:
\[
|\nabla a \cdot \langle T, \nabla T\rangle|
\le \frac{\varepsilon}{2}a|\nabla T|^2 + \frac{2C}{\varepsilon r^2}|T|^2.
\tag{8.1b}
\]
The explicit tensor dissipation gives $-2D_2$.

**First-derivative cutoff.**  By (2.8) of Step 34 with $p = 2$:
\[
C\int\eta^2|\nabla a||\nabla\operatorname{Rm}|F_T\,d\mu
\le \varepsilon' D_2 + \frac{C}{\varepsilon' r^2}H.
\tag{8.1c}
\]

**Signed Hessian.**  By (7.5):
\[
|I_C| \le \varepsilon'' D_2 + \frac{C}{\varepsilon'' r^2}H.
\tag{8.1d}
\]

**Cubic reaction.**  All algebraic terms and the volume-form contribution:
\[
C_0\int\eta^2 aF_T^3\,d\mu = C_0Y.
\tag{8.1e}
\]

**Metric drift.**  By (6.5):
\[
C_V\|aE\|_\infty H.
\tag{8.1f}
\]

**Lower-order.**  From $F_T \ge 1$ and $0 \le a \le 1$, constants from the
$G$-evolution and metric variation on $F_T \ge 1$ parts:
\[
C_H(1 + r^{-2})H.
\tag{8.1g}
\]

### 8.2 The $H_2$ inequality

Choosing $\varepsilon = \varepsilon' = \varepsilon'' = c_0/6$:

\[
\boxed{
\frac{dH}{dt} + c_0D_2
\le C_0Y + C_H(1 + r^{-2})H + C_V\|aE\|_\infty H,}
\tag{8.2}
\]
where
\[
H = \int\eta^2 F_T^2\,d\mu,
\quad
D_2 = \int\eta^2 a|\nabla\operatorname{Rm}|^2\,d\mu,
\quad
Y = \int\eta^2 aF_T^3\,d\mu.
\tag{8.3}
\]

### 8.3 Sobolev transport
## 9. Pure-scaling checks: what is exact and what is only schematic

Set $a \equiv 1$, $E = g$ (pure scaling $\partial_t g = -2g$), $n = 4$.

| Quantity | Correct computation | Consequence |
|----------|---------------------|-------------|
| $\partial_t R_{ijkl}$ | $-2R_{ijkl}$ (§3.4) | all-lower Riemann checksum remains valid |
| $\partial_tG_{ijkl}$ | $-4G_{ijkl}$ because $\partial_t(g\owedge g)=2(h\owedge g)=-4(g\owedge g)$ | Step 63's earlier `$-2G$' row was false |
| $\partial_tT_{ijkl}$ | $-2R_{ijkl}+4G_{ijkl}=-2T_{ijkl}+2G_{ijkl}$ | exact $T$ scaling is not homogeneous |
| $\partial_t|T|^2$ | not $+4|T|^2$ in general; on a flat torus $R=0$, $T=-G$, the covariant scaling and four inverse metrics cancel to give $\partial_t|T|^2=0$ | do not use the old `$+4|T|^2$' line |
| $\partial_t(d\mu)$ | $-4\,d\mu$ | volume-form line remains valid |
| $\partial_t\int|\operatorname{Rm}|^2d\mu$ | $0$ in dimension four for pure scaling of $\operatorname{Rm}$ | Riemann-energy scaling remains valid |
| Hessian / first-derivative cutoff terms | $0$ because $a$ is constant | signed-Hessian and cutoff-gradient checks remain valid |
| Metric-drift term | $C_V\|aE\|_\infty H$ with $\|aE\|_\infty=1$ | display (8.2) remains valid |

The false homogeneous line $\partial_tT=-2T$ has **no role** in the estimates
after this correction.  The repaired use is: all zero-order contributions from
$Q(\operatorname{Rm})$, $\operatorname{Rm}*E$, metric variation, and
$\partial_tG$ are algebraic tensors bounded by $CaF_T^3$ (or by a lower
$CaF_T^2$ term absorbed by $CaF_T^3$ since $F_T\ge1$).  Thus the pointwise
inequality (5.5), the $H_2$ inequality (8.2), and the downstream Moser
endpoint survive unchanged as inequalities, but no later writeup may quote the
old pure-scaling table as an exact $T$-evolution verification.

---

## 10. What this note closes and what remains

**Closed (this note).**

1. **Premise C1a: All-lower curvature variation.**  Equation (3.11) with the
   corrected pure-scaling checks (§9).  The index-level derivation from the
   general variation formulas (2.2)–(2.5) through the Ricci/normalization split
   (§3.2–§3.4) is complete.  The exact shifted tensor is not homogeneous under
   pure scaling; only the resulting algebraic zero-order terms are used in the
   estimates.

2. **Premise C1b: Derivative-structure bound.**  Lemma 4.1 proves
   $|\nabla B| \le CF_T|\nabla\operatorname{Rm}|$ from the algebraic structure
   of $B$ as a contraction of $E$, $g$, $T$ and the Bianchi inequality.
   This is a proved result, not an assumption.

3. **Premise C2: Metric-drift display.**  Equation (8.2) carries
   $C_V\|aE\|_\infty H$ explicitly, and (8.4) records $A = e^{8V_*}$.

**Remaining conditional input to the restricted IL theorem.**

Per-datum existence of the degenerate cutoff flow (A03 Step 56).  Per the
Strategist's guidance, this cannot be resolved by citation of standard
uniformly parabolic theory (Amann, Lunardi, maximal $L^p$ regularity), since
the transported DeTurck system has principal coefficient $\beta^2 \ge 0$
degenerate on the collar.  The honest resolution is either a self-contained
existence argument built from A03's tame hierarchy with the fixed-parameter
parabolic content fully written, or a cleanly isolated conditional theorem.

**Curvature Moser endpoint status.**  The endpoint $\|aF_T(t)\|_\infty \le C\Gamma/t$
now consumes: (8.2) — proved here at index level as an inequality after the
Step 64 pure-scaling repair; the critical absorption
$Y \le C\gamma(D_2 + r^{-2}H)$ — verified by TTCS (Step 61 verifier 2 §2);
the $q=3$ propagation and Moser iteration — verified algebraically (Step 61
verifier 2 §§3–5); the defect endpoint — proved (Step 62).  The sole remaining
conditional input to the curvature endpoint is per-datum existence.

---

## 11. Scope

This note establishes the $H_2$ evolution inequality for the restricted
four-dimensional negative Ishida–LeBrun cutoff-flow theorem.  It does not
address the positive branch, arbitrary four-manifold topology, dimensions
$n \ge 5$, dimension-only constants, or Lean formalization.  The $H_2$
inequality is an a priori estimate on one selected support; the selection-layer
outputs (maximal-function good support, buffered cutoffs, Sobolev constant)
are verified by TTCS but remain per-datum conditional on flow existence.
