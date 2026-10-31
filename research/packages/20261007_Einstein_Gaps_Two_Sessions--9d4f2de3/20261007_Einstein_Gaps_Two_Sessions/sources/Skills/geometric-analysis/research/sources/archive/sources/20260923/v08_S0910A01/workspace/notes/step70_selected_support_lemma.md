# Step 70: Selected-support lemma for the IL negative-gap theorem

Session: S0910A01.  Agent2 / Constructor.  Step 70, Execute.

## Purpose

This note expands the selected-support construction (assembly §4) into a
self-contained proof module.  The lemma converts the global integral
curvature budget into local energy seeds with collapse-cancelling
smallness and constructs the single global cutoff for the terminal
argument.  No initial sectional curvature bound is assumed anywhere.

**Convention.** Throughout, $n=4$, $G=\frac{g\owedge g}{6}$,
$T=\operatorname{Rm}-G$, $F_T=(1+|T|^2)^{1/2}$,
$E=\operatorname{Ric}+g$, and operator-normalized curvature norms
are used ($|G|^2=2/3$).

---

## 1. Hypotheses (from the IL contradiction sequence)

We work with a hypothetical sequence $(M_i,g_i)$ in the permitted
Ishida–LeBrun geography:

$$
M_i=\left(\#_{j=1}^{m_i}X_{j,i}\right)\#N_i,
\qquad m_i\in\{2,3\},\quad b_+(N_i)=0,
$$

$$
A_i=\sum_j c_1^2(X_{j,i})>0,\qquad
q_i=D_i-A_i/3\ge0,\qquad
D_i=4m_i-(2\chi+3\tau)(N_i).
$$

Assume

$$
\delta_i:=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_\infty\to0
\qquad\text{as }i\to\infty.
\tag{1.1}
$$

The limit $\delta_i\to0$ will be assumed small enough at each stage below;
the precise thresholds depend only on $n=4$ and fixed dimensional constants.

---

## 2. Full-curvature budget

**Proposition 2.1 (full-curvature budget).**
*Under the hypotheses of §1, there is a dimensional constant $C_0$ such
that for all $i$ sufficiently large,*

$$
\int_{M_i}|\operatorname{Rm}_{g_i}|^2\,d\mu_{g_i}\le C_0A_i.
\tag{2.1}
$$

**Proof.**

**Step 1: Chern–Gauss–Bonnet.**  In dimension four, with our operator-normalized
convention,

$$
8\pi^2\chi(M_i)
=\int_{M_i}\left(|W|^2-\frac12|\mathring{\operatorname{Ric}}|^2
+\frac{s^2}{24}\right)d\mu,
\tag{2.2}
$$

where $\mathring{\operatorname{Ric}}=\operatorname{Ric}-\frac s4 g$ is the
trace-free Ricci tensor and $|W|^2=|W^+|^2+|W^-|^2$.  Equivalently, with

$$
|\operatorname{Rm}|^2=|W|^2+\frac12|\mathring{\operatorname{Ric}}|^2+\frac{s^2}{24},
\tag{2.3}
$$

the Chern–Gauss–Bonnet identity becomes

$$
\int|\operatorname{Rm}|^2
=8\pi^2\chi+\int|\mathring{\operatorname{Ric}}|^2.
\tag{2.4}
$$

(Note: the $1/2$ in (2.3) and the coefficient $1$ in (2.4) are correct
for operator-normalized norms.  The standard Hilbert–Schmidt norm gives
coefficient $2$ instead of $1$.)

**Step 2: Euler contribution of the complex blocks.**  The connected-sum
formula gives

$$
\chi(M_i)=\sum_j c_2(X_{j,i})+\chi(N_i)-2m_i.
\tag{2.5a}
$$

For the $X_j$ contribution this proof uses the stated IL-class hypothesis
that every $X_j$ is a **minimal complex surface of general type**.  It is
not an assertion for arbitrary symplectic building blocks.  Write
$K_j^2=c_1^2(X_j)$ and $\chi_h(X_j)=1-q(X_j)+p_g(X_j)$.  Noether's
inequality gives
$$
K_j^2\ge 2p_g(X_j)-4,
$$
hence $p_g(X_j)\le (K_j^2+4)/2$.  Since
$$
c_2(X_j)=12\chi_h(X_j)-K_j^2=12(1-q(X_j)+p_g(X_j))-K_j^2
$$
and $q(X_j)\ge0$,
$$
c_2(X_j)\le12(1+p_g(X_j))-K_j^2
\le5K_j^2+36.
\tag{2.5b}
$$
Because $K_j^2\ge1$ and $m_i\in\{2,3\}$, this yields
$\sum_jc_2(X_{j,i})\le C A_i$.

**Step 3: Trace-free Ricci bound.**  Since $\operatorname{Ric}=-g+E$ and
$\delta_i=\|g_i^{-1}E_i\|_{\infty,\mathrm{op}}$, the trace-free part
satisfies

$$
|\mathring{\operatorname{Ric}}|_{\rm HS}
=|E^\circ|_{\rm HS}
\le|E|_{\rm HS}
\le2\delta_i.
\tag{2.6}
$$

(Here the factor $2$ is the dimension-four conversion from operator norm
to Hilbert--Schmidt norm.)  Hence

$$
J_i=\frac1{8\pi^2}\int|E^\circ|_{\rm HS}^2
\le\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i).
\tag{2.6a}
$$

**Step 4: Volume upper bound without using the Euler bound.**  The scalar
satisfies $s=-4+\operatorname{tr}_gE$, so $|s|\ge4(1-\delta_i)$ once
$\delta_i<1$.  Therefore

$$
I_i=\frac1{4\pi^2}\int\!\left(\frac{s^2}{24}+2|W^+|^2\right)
\ge\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i).
\tag{2.7}
$$

The geography identity gives $I_i=J_i+\frac{2A_i}{3}-q_i\le
J_i+\frac{2A_i}{3}$ because $q_i\ge0$.  Combining with (2.6a),

$$
\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i)
\le\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i)+\frac{2A_i}{3}.
$$

For $\delta_i<1/4$ this rearranges to

$$
\operatorname{Vol}(M_i)
\le\frac{4\pi^2A_i}{(1-\delta_i)^2-3\delta_i^2}
\le C A_i.
\tag{2.8}
$$

**Step 5: The $N_i$ and total Euler bounds.**  Now (and only now) the
trace-free Ricci estimate gives

$$
0\le q_i\le J_i\le C\delta_i^2A_i\le CA_i.
\tag{2.8a}
$$

Hence $D_i=A_i/3+q_i=O(A_i)$.  Since $b_+(N_i)=0$,
$(2\chi+3\tau)(N_i)=4-4b_1(N_i)-b_-(N_i)$, so
$D_i=4m_i-4+4b_1(N_i)+b_-(N_i)$ controls both $b_1(N_i)$ and
$b_-(N_i)$ up to a universal additive constant.  Consequently
$|\chi(N_i)|=|2-2b_1(N_i)+b_-(N_i)|=O(A_i)$, and (2.5a) gives
$\chi(M_i)=O(A_i)$.

**Step 6: Concluding the curvature budget.**  From (2.4), the total Euler
bound, and (2.6)--(2.8):

$$
\int|\operatorname{Rm}|^2
=8\pi^2\chi+
\int|\mathring{\operatorname{Ric}}|^2
\le C A_i+4\delta_i^2\operatorname{Vol}(M_i)
\le C_0A_i.
\tag{2.9}
$$

Since $|T|^2=|\operatorname{Rm}-G|^2\le2|\operatorname{Rm}|^2+2|G|^2$
and $|G|^2=2/3$,

$$
\int F_T^2=\int(1+|T|^2)\le1\cdot\operatorname{Vol}+2\int|\operatorname{Rm}|^2
+\frac43\operatorname{Vol}\le C_0'A_i.
\tag{2.10}
$$

$\square$

---

## 3. Volume lower bound

**Proposition 3.1 (volume lower bound).**
*For all $i$ sufficiently large,*

$$
\operatorname{Vol}(M_i,g_i)\ge\frac{32\pi^2}{9}A_i(1-C\delta_i).
\tag{3.1}
$$

**Proof.**  The calibrated Chern–Weil geography gives (assembly §3):

$$
\int(s+8\sqrt6|W^+|)^2\le108Q_i,\qquad
\int\mathcal G\le6Q_i,
$$

where $Q_i=\int|E_i|^2\le4\delta_i^2\operatorname{Vol}$.  The
completion-of-squares and monopole identities force

$$
\frac{s^2}{24}+2|W^+|^2\to\frac{3}{4}\qquad
\text{in }L^1\text{-normalized mean}.
$$

(At the calibrated values $s\to-4$, $|W^+|^2\to1/24$, one computes
$16/24+2/24=18/24=3/4$.)  Since
$\int(\frac{s^2}{24}+2|W^+|^2)=4\pi^2I_i\ge\frac{8\pi^2}{3}A_i$
and the mean approaches $3/4$, the volume satisfies

$$
\operatorname{Vol}=\frac{4\pi^2I_i}{\langle s^2/24+2|W^+|^2\rangle}
\ge\frac{8\pi^2A_i/3}{3/4+O(\delta_i)}
=\frac{32\pi^2}{9}A_i(1-O(\delta_i)).
$$

Combining with (2.8): $c_VA_i\le\operatorname{Vol}\le C_VA_i$ for a
universal $0<c_V<C_V$.  $\square$

---

## 4. Maximal-function selection

### 4.1 Weak-type maximal inequality under Ricci lower bound

**Lemma 4.1 (weak-type maximal inequality).**
*Let $(M^n,g)$ be a closed Riemannian manifold with
$\operatorname{Ric}\ge-(n-1)g$, and let $f\ge0$ be integrable.
For $R_0>0$ and*

$$
\mathcal M_{R_0}f(x)=\sup_{0<s\le R_0}\fint_{B_s(x)}f\,d\mu,
$$

*there is $C=C(n,R_0)$ such that for all $\lambda>0$,*

$$
\operatorname{Vol}\{x:\mathcal M_{R_0}f(x)>\lambda\}
\le\frac{C}{\lambda}\int_M f\,d\mu.
\tag{4.1}
$$

**Proof.**  This is the standard Vitali covering argument adapted to
manifolds with Ricci lower bound.  For each $x$ in the superlevel set,
choose a ball $B_{s_x}(x)$ with $s_x\le R_0$ and
$\fint_{B_{s_x}(x)}f>\lambda$.  By Vitali's covering lemma, select
a countable disjoint subfamily $\{B_{s_j}(x_j)\}$ such that the
triples $\{B_{5s_j}(x_j)\}$ cover the original set.  Then

$$
\operatorname{Vol}\{x:\mathcal M_{R_0}f>\lambda\}
\le\sum_j\operatorname{Vol}(B_{5s_j}(x_j))
\le\sum_j\frac{\operatorname{Vol}(B_{5s_j}(x_j))}
{\operatorname{Vol}(B_{s_j}(x_j))}
\cdot\frac{1}{\lambda}\int_{B_{s_j}}f.
$$

Bishop–Gromov comparison under $\operatorname{Ric}\ge-(n-1)g$ gives
the volume ratio

$$
\frac{\operatorname{Vol}(B_{5s}(x))}{\operatorname{Vol}(B_s(x))}
\le\frac{V_{-1}(5s)}{V_{-1}(s)}
\le C(n,R_0),
$$

where $V_{-1}(r)$ is the volume of a ball of radius $r$ in the simply
connected space of constant sectional curvature $-1$.  Since $s_j\le R_0$,
the ratio is uniformly bounded.  Summing by disjointness of the $B_{s_j}$:

$$
\operatorname{Vol}\{x:\mathcal M_{R_0}f>\lambda\}
\le\frac{C(n,R_0)}{\lambda}\sum_j\int_{B_{s_j}}f
\le\frac{C(n,R_0)}{\lambda}\int_M f.
$$

$\square$

**Remark 4.2.** The constant $C(n,R_0)$ involves the supremum of
$V_{-1}(5s)/V_{-1}(s)$ over $0<s\le R_0$, bounded when $R_0$ is fixed.
For $R_0=10r$ with $r\to0$, the constant approaches $5^n=625$ for $n=4$.

### 4.2 Threshold selection

With $f=|\operatorname{Rm}_{g_i}|^2$ and $R_0=10r$ (so $R_0\ge7r=L_\eta r$
for $(L_{\rm pl},L_\chi,L_\eta)=(5,6,7)$), set the threshold

$$
\lambda=\frac{\widetilde\gamma^2}{r^4},
\tag{4.2}
$$

where $\widetilde\gamma>0$ is chosen below.  By Proposition 2.1 and
Lemma 4.1:

$$
\operatorname{Vol}(\text{bad set}):=
\operatorname{Vol}\{x:\mathcal M_{R_0}(|\operatorname{Rm}|^2)>\lambda\}
\le\frac{C(4,10r)\,r^4}{\widetilde\gamma^2}\cdot C_0A_i
=\frac{C_1r^4}{\widetilde\gamma^2}A_i.
\tag{4.3}
$$

The **good set** is

$$
G_i=\{x\in M_i:\mathcal M_{R_0}(|\operatorname{Rm}|^2)(x)
\le\widetilde\gamma^2/r^4\}.
\tag{4.4}
$$

### 4.3 Retained good-set volume

By Proposition 3.1, $\operatorname{Vol}(M_i)\ge c_VA_i$ for $i$ large.
Hence

$$
\operatorname{Vol}(G_i)\ge c_VA_i-\frac{C_1r^4}{\widetilde\gamma^2}A_i.
\tag{4.5}
$$

**Parameter ordering:** fix $\widetilde\gamma$ first (below the absorption
threshold, see §6), then choose $r$ small enough that
$C_1r^4/\widetilde\gamma^2<c_V/2$.  This gives

$$
\operatorname{Vol}(G_i)\ge\frac{c_V}{2}A_i=:\alpha_1A_i>0
\tag{4.6}
$$

for all $i$ sufficiently large.  Note: $\widetilde\gamma$ and $r$ depend
only on $n=4$ and the dimensional constants in the curvature and
volume estimates; they are independent of $i$ and of the individual
topology within the IL geography.

---

## 5. Packing, coloring, and disjoint supports

### 5.1 $r$-separated net

Choose a **maximal $r$-separated** subset $\{x_\alpha\}\subset G_i$.
Maximality means that $G_i\subset\bigcup_\alpha B_r(x_\alpha)$.  In
particular,

$$
\operatorname{Vol}\!\left(\bigcup_\alpha B_r(x_\alpha)\right)
\ge\operatorname{Vol}(G_i)\ge\alpha_1A_i.
\tag{5.1}
$$

### 5.2 Relative packing bound

The balls $\{B_{r/2}(x_\alpha)\}$ are pairwise disjoint (by the
$r$-separation).  **Finiteness** of $|\mathcal A_i|$ follows from
compactness of $M_i$.  No absolute volume lower bound for individual
balls is assumed (collapse is permitted).

### 5.3 Intersection graph and degree bound (relative comparison)

For $L_\eta=7$, the $B_{7r}(x_\alpha)$ supports will carry the
auxiliary cutoffs.  To make them disjoint, we color the centers.
Consider the intersection graph where $x_\alpha\sim x_\beta$ whenever
$B_{7r}(x_\alpha)\cap B_{7r}(x_\beta)\ne\emptyset$, i.e., when
$d(x_\alpha,x_\beta)<14r$.

For a fixed center $x_\alpha$, each neighbor $x_\beta$ satisfies
$d(x_\alpha,x_\beta)<14r$, so $B_{r/2}(x_\beta)\subset B_{15r}(x_\alpha)$.
Since $B_{15r}(x_\alpha)\subset B_{29r}(x_\beta)$, Bishop–Gromov
comparison at $x_\beta$ under $\operatorname{Ric}\ge-3g$ gives

$$
\operatorname{Vol}(B_{r/2}(x_\beta))
\ge\frac{V_{-1}(r/2)}{V_{-1}(29r)}
\operatorname{Vol}(B_{29r}(x_\beta))
\ge\frac{V_{-1}(r/2)}{V_{-1}(29r)}
\operatorname{Vol}(B_{15r}(x_\alpha)).
\tag{5.3a}
$$

Summing the pairwise-disjoint balls $B_{r/2}(x_\beta)$ inside
$B_{15r}(x_\alpha)$:

$$
D\cdot\frac{V_{-1}(r/2)}{V_{-1}(29r)}
\operatorname{Vol}(B_{15r}(x_\alpha))
\le\sum_{\beta:\beta\sim\alpha}\operatorname{Vol}(B_{r/2}(x_\beta))
\le\operatorname{Vol}(B_{15r}(x_\alpha)).
$$

Hence the degree is bounded by the **volume ratio**:

$$
D\le\frac{V_{-1}(29r)}{V_{-1}(r/2)}
=:D_0(n,r).
\tag{5.3}
$$

For $n=4$ and small $r$, $D_0\approx(58)^4$, but the exact value does
not matter; only its $i$-independence is used.  Crucially, this bound
uses only relative Bishop–Gromov comparison, not an absolute volume
lower bound, so it remains valid under collapse.

### 5.4 Greedy coloring

The graph has maximum degree $D_0$, so a greedy coloring uses at most
$D_0+1$ colors.  At least one color class has total $B_r$-volume at least

$$
\frac{\alpha_1A_i}{D_0+1}=:\alpha_0A_i>0.
\tag{5.4}
$$

Relabel this class as $\{x_\alpha\}_{\alpha\in\mathcal A_i}$.
By construction, the $B_{7r}(x_\alpha)$ for $\alpha\in\mathcal A_i$
are **pairwise disjoint**, and the inner balls still carry
$A_i$-proportional volume:

$$
\operatorname{Vol}\!\left(\bigcup_\alpha B_r(x_\alpha)\right)
\ge\alpha_0A_i.
\tag{5.5}
$$

**The constant $\alpha_0=c_V/(2(D_0+1))$ is independent of $i$,
the individual manifold, and the topology within the IL geography.
It depends only on $n=4$, the ratio $L_\eta=7$, the separation $r$,
and the calibrated-volume constants.**

---

## 6. Cutoff architecture and global weight

### 6.1 Smooth cutoffs

For each $\alpha\in\mathcal A_i$, construct smooth cutoffs on $(M_i,g_i)$:

**Physical cutoff** $\chi_\alpha:M_i\to[0,1]$:

$$
\chi_\alpha\equiv1\text{ on }B_{5r}(x_\alpha),\qquad
\operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha),\qquad
|\nabla\chi_\alpha|\le C_\nabla/r.
\tag{6.1}
$$

**Auxiliary cutoff** $\eta_\alpha:M_i\to[0,1]$:

$$
\eta_\alpha\equiv1\text{ on }B_{6r}(x_\alpha),\qquad
\operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha),\qquad
|\nabla\eta_\alpha|\le C_\nabla/r.
\tag{6.2}
$$

**Construction.** The distance function $d_\alpha(x)=d(x,x_\alpha)$ is
Lipschitz with $|dd_\alpha|\le1$ a.e.  To ensure the strict support
nesting required for Proposition 6.1, we pre-reserve $\varepsilon$-buffers
($0<\varepsilon\ll r$ fixed).

*Physical cutoff $\chi_\alpha$:*  Start with raw
$\psi_\alpha=\varphi\circ d_\alpha$ where $\varphi=1$ on $[0,5r+\varepsilon]$,
$\varphi=0$ on $[6r-\varepsilon,\infty)$, $|\varphi'|\le2/(r-2\varepsilon)$.
Mollify at scale $\varepsilon'\ll\varepsilon$ to get a smooth
$\chi_\alpha$ with $\chi_\alpha=1$ on $B_{5r}$,
$\operatorname{supp}\chi_\alpha\subset B_{6r}$, $|\nabla\chi_\alpha|\le C/r$.

*Auxiliary cutoff $\eta_\alpha$:*  Similarly, raw $\eta=1$ on
$[0,6r+\varepsilon]$, $\eta=0$ on $[7r-\varepsilon,\infty)$, mollified at
scale $\varepsilon'$.  This gives $\eta_\alpha=1$ on $B_{6r}$,
$\operatorname{supp}\eta_\alpha\subset B_{7r}$, $|\nabla\eta_\alpha|\le C/r$.

The pre-reserved $\varepsilon$-gaps guarantee the strict inclusions
$$
\operatorname{supp}\chi_\alpha\subset B_{6r}\subset\{\eta_\alpha=1\},
\qquad
\operatorname{supp}\nabla\eta_\alpha\subset B_{7r}\setminus B_{6r}
\subset\{\chi_\alpha=0\},
$$
which are needed for the support identities in Proposition 6.1.

**Higher jets.**  The mollification produces smooth cutoffs whose higher
jets $\nabla^m\chi_\alpha$ depend on the local geometry of $(M_i,g_i)$.
These are **finite for each smooth datum** but are **not
sequence-uniformly bounded** for $m\ge2$.  This is important:
the per-datum existence theorem (assembly §5) uses all higher jets,
but only through datum-dependent estimates.  The sequence-uniform
estimates in §§7–8 below use only $|\nabla\chi|\le C/r$ and
$\chi\in[0,1]$.

### 6.2 Global cutoff

Define the **global cutoff**:

$$
\chi_i=\sum_{\alpha\in\mathcal A_i}\chi_\alpha,
\qquad
a_i=\chi_i^2.
\tag{6.3}
$$

Since the $B_{7r}(x_\alpha)$ are pairwise disjoint and
$\operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha)\subset
B_{7r}(x_\alpha)$, at each point at most one $\chi_\alpha$ is nonzero.
Hence

$$
\chi_i^2=\sum_\alpha\chi_\alpha^2,\qquad
0\le a_i=\chi_i^2\le1.
\tag{6.4}
$$

**On the complement** $M_i\setminus\bigcup_\alpha B_{6r}(x_\alpha)$,
all $\chi_\alpha=0$, so $a_i=0$ and the metric is **stationary** under
the cutoff flow $\partial_tg=-2a_i(\operatorname{Ric}+g)$.

### 6.3 Nested-support identities

**Proposition 6.1 (support identities).**
*For each $\alpha\in\mathcal A_i$:*

$$
a_i|\nabla\eta_\alpha|^2=0,\qquad
(\nabla a_i)\cdot(\nabla\eta_\alpha)=0
\tag{6.5}
$$

*pointwise on $M_i$.*

**Proof.**  The key is the support nesting:

$$
\operatorname{supp}\nabla\eta_\alpha
\subset B_{7r}(x_\alpha)\setminus B_{6r}(x_\alpha).
\tag{6.6}
$$

On this annulus, $\chi_\alpha=0$ (since
$\operatorname{supp}\chi_\alpha\subset B_{6r}$).  Also, for every
$\beta\ne\alpha$, the disjointness
$B_{7r}(x_\alpha)\cap B_{7r}(x_\beta)=\emptyset$ gives
$\chi_\beta=0$ on $B_{7r}(x_\alpha)$.  Hence $a_i=\chi_i^2=0$ on
$\operatorname{supp}\nabla\eta_\alpha$, and also $\nabla a_i=0$ there.
Both identities follow.  $\square$

**Corollary 6.2.** On
$\operatorname{supp}\nabla\eta_\alpha$, the metric is stationary
under the cutoff flow.  This replaces finite propagation (which does
not hold for Ricci flow) by a coefficient-support fact.

**Corollary 6.3.** In any energy estimate tested against $\eta_\alpha^2$,
every term involving $\nabla\eta_\alpha$ paired with $a_i$ or
$\nabla a_i$ vanishes identically.

### 6.4 One global flow

The cutoff flow uses this single global $\chi_i$, producing **one
terminal metric** $g_i(T)$ on $M_i$.  This is essential:

- The per-datum existence theorem (Step 65) applies to $(M_i,g_i,\chi_i)$
  as one system, giving a datum-dependent existence time $T_{0,i}$.
- The Seiberg–Witten inequality, global $Q$ propagation, and Liouville
  averaging in the contradiction (assembly §§7–9) are all applied to
  this single closed terminal metric on the same smooth manifold.
- The local estimates (curvature, defect, continuation) are applied
  to each disjoint buffered component using its auxiliary $\eta_\alpha$.

---

## 7. Initial energy seeds and collapse cancellation

This is the load-bearing interface for the cutoff-flow bootstrap.

### 7.1 Mean curvature on each support

Because $x_\alpha\in G_i$ and $7r\le R_0$, the maximal-function
threshold gives:

$$
\fint_{B_{7r}(x_\alpha)}|\operatorname{Rm}_{g_i}|^2
\le\frac{\widetilde\gamma^2}{r^4}.
\tag{7.1}
$$

This is a mean-value bound, not a pointwise bound.  In particular, the
sectional curvature on $B_{7r}(x_\alpha)$ is **not** bounded at time
zero.  Denote $U_\alpha=B_{7r}(x_\alpha)$.

The augmented curvature energy on the auxiliary support:

$$
H_{2,\alpha}(0):=\int_{U_\alpha}\eta_\alpha^2F_T^2\,d\mu_0.
\tag{7.2}
$$

Since $F_T^2=1+|T|^2\le1+2|\operatorname{Rm}|^2+2|G|^2
\le C(1+|\operatorname{Rm}|^2)$ and $\eta_\alpha\le1$:

$$
H_{2,\alpha}(0)\le C\int_{U_\alpha}(1+|\operatorname{Rm}|^2)
\le C\!\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha).
\tag{7.3}
$$

### 7.2 Relative Sobolev inequality and its collapse behavior

The relative Sobolev inequality on $U_\alpha=B_{7r}(x_\alpha)$ reads:
for $u\in W^{1,2}_0(U_\alpha)$ (or supported in $U_\alpha$),

$$
\|u\|_{L^4(U_\alpha)}^2
\le\mathcal S_\alpha(0)\!\left(\|\nabla u\|_{L^2(U_\alpha)}^2
+r^{-2}\|u\|_{L^2(U_\alpha)}^2\right),
\tag{7.4}
$$

where the Sobolev constant scales as

$$
\mathcal S_\alpha(0)\le C(L_\eta)\,
r^2\operatorname{Vol}(U_\alpha)^{-1/2}.
\tag{7.5}
$$

**Derivation of the scaling (7.5).**  Under $\operatorname{Ric}\ge-3g$,
the standard $L^{4/2}$-Sobolev inequality on a ball $B_R$ with
$R\le R_{\max}$ (Hebey, theorem 4.4; Saloff-Coste) gives a constant
depending on $n$, $R$, $\operatorname{Ric}\ge-(n-1)\kappa^2$, and
$\operatorname{Vol}(B_R)$.  In dimension $n=4$, the critical Sobolev
exponent is $2^*=4$, and the standard form is

$$
\left(\int_{B_R}|u|^4\right)^{1/2}
\le C_S(R,\kappa)
\left(\int_{B_R}|\nabla u|^2+R^{-2}\int_{B_R}|u|^2\right)
$$

with $C_S(R,\kappa)=C(4)\cdot R^2\operatorname{Vol}(B_R)^{-1/2}
\cdot e^{C\kappa R}$.  For $\kappa=\sqrt3$ and $R=7r\le7r_0$ with
$r_0$ small and fixed, $e^{C\kappa R}\le C'$ is bounded.  Hence

$$
\mathcal S_\alpha(0)=C(4,L_\eta)\,r^2\operatorname{Vol}(U_\alpha)^{-1/2}.
$$

**Key observation: this may diverge under collapse.**  If
$\operatorname{Vol}(U_\alpha)\to0$ along the sequence, then
$\mathcal S_\alpha(0)\to\infty$.  The flow smoothing cannot start from
a bounded Sobolev constant assumption.

### 7.3 Collapse-cancelling product

Define the critical absorption parameter:

$$
\gamma_\alpha(0):=\mathcal S_\alpha(0)\,H_{2,\alpha}(0)^{1/2}.
\tag{7.6}
$$

**Proposition 7.1 (collapse cancellation).**

$$
\gamma_\alpha(0)\le C(L_\eta)(r^2+\widetilde\gamma).
\tag{7.7}
$$

*In particular, $\gamma_\alpha(0)$ is sequence-uniformly small when $r$
and $\widetilde\gamma$ are chosen small.*

**Proof.**  From (7.5) and (7.3):

$$
\gamma_\alpha(0)
=\mathcal S_\alpha(0)\cdot H_{2,\alpha}(0)^{1/2}
\le C r^2\operatorname{Vol}(U_\alpha)^{-1/2}
\cdot\left[C\!\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha)\right]^{1/2}.
\tag{7.8}
$$

The volume cancels:

$$
\gamma_\alpha(0)
\le C r^2\left(1+\frac{\widetilde\gamma^2}{r^4}\right)^{1/2}
= C r^2\cdot\frac{(r^4+\widetilde\gamma^2)^{1/2}}{r^2}
= C(r^4+\widetilde\gamma^2)^{1/2}
\le C(r^2+\widetilde\gamma).
$$

The final inequality uses $\sqrt{a^2+b^2}\le a+b$ for $a,b\ge0$.
$\square$

**Remark 7.2 (mechanism).** The cancellation has a clear geometric
meaning:

- $\mathcal S_\alpha(0)\sim r^2/\operatorname{Vol}(U_\alpha)^{1/2}$
  **grows** under collapse;
- $H_{2,\alpha}(0)^{1/2}\sim\operatorname{Vol}(U_\alpha)^{1/2}
  \cdot(1+\widetilde\gamma/r^2)$ **shrinks** under collapse.

Their product eliminates the volume dependence entirely.  This is the
reason the critical product controls the flow: both the Sobolev
geometry and the available curvature energy respond to collapse in
opposite directions.

**Remark 7.3 (parameter order).**  The construction requires:
1. Fix the support ratios $(L_{\rm pl},L_\chi,L_\eta)=(5,6,7)$.
2. Fix $R_0=10r$ (any fixed multiple $>L_\eta$ works).
3. Choose $\widetilde\gamma$ small enough that the downstream absorption
   inequalities close: the first-exit bootstrap (assembly §6) requires
   $C\gamma_*<c_{\rm abs}$, so $\widetilde\gamma<c_{\rm abs}/(2C)$.
4. Then choose $r$ small enough that
   $C(r^2+\widetilde\gamma)<\gamma_*$, which requires $r^2<\gamma_*/(2C)$,
   and simultaneously $C_1r^4/\widetilde\gamma^2<c_V/2$ (for the good-set
   volume from §4.3), and $\theta r^2$ gives the correct observation-time
   scale.

After these choices, $\gamma_\alpha(0)\le\gamma_*/2$ for every
$\alpha$ and every $i$, uniformly.  Note that **no noncollapsing
assumption** and **no initial sectional curvature bound** enters
this smallness statement.

---

## 8. Summary of the support module outputs

The selected-support module delivers the following sequence-uniform
data for $i$ sufficiently large:

| Output | Symbol | Bound | Source |
|--------|--------|-------|--------|
| Full-curvature budget | $\int|\operatorname{Rm}|^2$ | $\le C_0A_i$ | Prop 2.1 |
| Full shifted budget | $\int F_T^2$ | $\le C_0'A_i$ | (2.10) |
| Volume lower | $\operatorname{Vol}$ | $\ge c_VA_i$ | Prop 3.1 |
| Volume upper | $\operatorname{Vol}$ | $\le C_VA_i$ | (2.8) |
| Good-set volume | $\operatorname{Vol}(G_i)$ | $\ge\alpha_1A_i$ | (4.6) |
| Retained colored volume | $\sum_\alpha\operatorname{Vol}(B_r(x_\alpha))$ | $\ge\alpha_0A_i$ | (5.5) |
| Disjoint supports | $B_{7r}(x_\alpha)\cap B_{7r}(x_\beta)=\emptyset$ | — | §5 |
| Global cutoff | $a_i=\chi_i^2\in[0,1]$ | smooth | §6 |
| Support identity | $a_i\|\nabla\eta_\alpha\|^2=0$ | pointwise | Prop 6.1 |
| Cutoff gradient | $\|\nabla\chi_\alpha\|$ | $\le C/r$ | (6.1) |
| Initial absorption | $\gamma_\alpha(0)$ | $\le C(r^2+\widetilde\gamma)$ | Prop 7.1 |
| Global defect | $Q_i(0)=\int|E_i|^2$ | $\le C\delta_i^2A_i$ | (2.8) |

**Not outputs of this module (datum-dependent only):**
- Higher cutoff jets $\nabla^m\chi_\alpha$, $m\ge2$
- Per-datum existence time $T_{0,i}$
- Sobolev constant $\mathcal S_\alpha(0)$ (may diverge under collapse)
- Initial curvature energy $H_{2,\alpha}(0)$ (depends on local volume)
- Initial sectional curvature $\sup|\operatorname{sec}|$ (uncontrolled)

The cutoff flow (assembly §§5–8) takes these sequence-uniform outputs
as inputs.  The first-exit bootstrap variable
$\Gamma(t)=\max_\alpha\sup_{s\le t}\gamma_\alpha(s)$ starts at
$\Gamma(0)\le\gamma_*/2$ by Proposition 7.1, with room for the
bootstrap improvement.

---

## 9. Comparison with the assembly

This note provides the detailed proofs behind assembly §§2–4:

| Assembly section | This note | Status |
|-----------------|-----------|--------|
| §2 contradiction setup | §1 | Matching |
| §3 terminal calibration | Not reproved here; uses Step 67 | — |
| §4.1 full-curvature budget | §2, Prop 2.1 | **Proved** |
| §4.1 maximal function | §4, Lemma 4.1 | **Proved** |
| §4.2 coloring | §5 | **Proved** |
| §4.2 cutoff architecture | §6 | **Proved** |
| §4.3 collapse cancellation | §7, Prop 7.1 | **Proved** |
| §4.4 volume bounds | §§2–3 | **Proved** |

---

## 10. Interface to the downstream modules

The cutoff-flow bootstrap (assembly §6) requires:

1. **Initial $\gamma_\alpha(0)\le\gamma_*/2$** — Proposition 7.1.
2. **$Q(0)/A_i\to0$** — from $Q(0)\le C\delta_i^2A_i$.
3. **Single global flow** — one $\chi_i$ and one terminal metric.
4. **Support identities** — Proposition 6.1 and Corollary 6.3.
5. **Disjoint supports** — coloring guarantees.
6. **$A_i$-proportional plateau volume** — (5.5).
7. **Full-curvature budget** — for the $q=2$ integrated curvature seed.
8. **No initial sectional curvature** — the curvature branch must
   produce bounded positive-time curvature as a **smoothing output**.
