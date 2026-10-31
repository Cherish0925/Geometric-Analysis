# Restricted Ishida–LeBrun negative-gap theorem: canonical assembly

Session: S0910A01.  Agent2 / Constructor.  Step 68, Execute.

This note assembles the restricted four-dimensional negative Ishida–LeBrun
pinching gap theorem from the established module chain, under one consistent
curvature convention.  It is a research proof note, not a final deliverable.
Step 69 repaired two load-bearing regressions in the first assembly: the
selected-support input is the collapse-cancelling product
$\mathcal S_\alpha H_{2,\alpha}^{1/2}$ from a full-curvature mean budget on
outer buffers, not a noncollapsing Sobolev constant or initial sectional
curvature bound; and the high-$p$ defect Moser coefficient
$\mathcal S^2Y\lesssim\gamma^3/t$ is used only on positive-time slabs, while
near time zero the independent integrated $q=2$ curvature-energy estimate is
the controlling input.

Each module is cited by its canonical source.  The assembly's role is to verify
that the interfaces match, the convention is uniform, and the two levels of
uniformity (sequence-uniform vs datum-dependent) are correctly separated.

---

## 0. Statement

**Theorem (family-uniform restricted negative gap).**
*There exists a constant $\varepsilon_{\rm IL}>0$ with the following
property.  Let*
$$
M=\bigl(\#_{j=1}^m X_j\bigr)\# N,
\qquad m\in\{2,3\},
$$
*where each $X_j$ is a minimal complex surface of general type, $N$ is
closed oriented with $b_+(N)=0$, and the connected sum carries the
Ishida–LeBrun monopole sign family.  Set*
$$
A=\sum_j c_1^2(X_j)>0,
\qquad
D=4m-(2\chi+3\tau)(N),
\qquad
q=D-\tfrac{A}{3}.
\tag{0.1}
$$
*If $q\ge0$, then no smooth Riemannian metric $g$ on $M$ satisfies*
$$
\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\operatorname{op}}
<\varepsilon_{\rm IL}.
\tag{0.2}
$$
*The constant $\varepsilon_{\rm IL}$ depends only on dimension four and
the universal constants in the Sobolev, curvature, and Moser estimates.
It is independent of $A$, $D$, $q$, $N$, the choices of $X_j$, and the
input metric.*

**Status after Step 69 review.**  The displayed theorem is the intended
restricted IL negative-gap result carried by this assembly.  The Step 69
Preceptor repair and TTCS review confirm the two corrected interfaces
(selected-support collapse cancellation and the time-zero/positive-time split
in defect Moser) as mathematically coherent.  They also keep the status as a
research-level assembly until the following are expanded in fully independent
proof text: the support lemma with full-curvature budget and coloring, the
index-level cutoff-flow tensor inequalities, the real-exponent/time-cutoff
defect Moser recurrence, the simultaneous first-exit closure, and the
per-datum existence/continuation interface.

**Scope.**  This is a restricted four-dimensional negative-sign result
for the Ishida–LeBrun no-Einstein geography with $q\ge0$.  It does not
settle the positive branch, arbitrary four-manifold topology, dimensions
$n\ge5$, or the Lean 4 formalization required by the full Yau Problem 26.

---

## 1. Canonical convention

Use Hamilton's curvature/Ricci contraction: $R_{jk}=g^{il}R_{ijkl}$.
Standard Kulkarni–Nomizu product:
$$
(\varphi\owedge\psi)_{ijkl}=\varphi_{ik}\psi_{jl}+\varphi_{jl}\psi_{ik}
-\varphi_{il}\psi_{jk}-\varphi_{jk}\psi_{il}.
\tag{1.1}
$$
Constant-curvature reference and shifted curvature:
$$
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}-G,\qquad
F_T=(1+|T|^2)^{1/2}.
\tag{1.2}
$$
Properties in dimension $n=4$:
$$
\operatorname{Ric}(G)=-g,\qquad
\operatorname{Ric}(T)=\operatorname{Ric}+g=:E,\qquad
\nabla T=\nabla\operatorname{Rm},\qquad
|G|^2=\tfrac23.
\tag{1.3}
$$
Curvature norms are operator-normalized (one quarter of the full
four-index contraction).  Defect: $E=\operatorname{Ric}+g$.  Scalar
defect: $\tau=\operatorname{tr}E=s+4$.

**Convention source:** `step64_convention_consistency_sweep.md`, confirmed
by `step63_curvature_variation_index_proof.md` §1.

**Legacy translation:** Steps 34, 36, 43, 54, 55, 58–60 wrote
$T_{\rm old}=\operatorname{Rm}+G_{\rm old}$ with the intended universal
shift satisfying $\operatorname{Ric}(G_{\rm old})=+g$.  This forces
$G_{\rm old}=-G$, so $T_{\rm old}=T$.  All pointwise quantities
$F_T,|T|^2,\nabla T$ and energies $H_2,K_p^\eta,Y,J_p$ are unchanged.

---

## 2. Proof architecture (by contradiction)

Suppose $(M_i,g_i)$ is a sequence in the permitted geography with
$E_i=\operatorname{Ric}_{g_i}+g_i$, $\delta_i=\|E_i\|_\infty\to0$,
$q_i\ge0$, and $A_i>0$.  The argument has four layers:

| Layer | Content | Uniformity level |
|-------|---------|-----------------|
| A. Terminal calibration (§3) | $\int\Phi\le119Q$ from topology | Sequence-uniform (metric-independent) |
| B. Selected-support construction (§4) | maximal-function supports, cutoffs | Sequence-uniform parameters |
| C. Cutoff-flow smoothing (§§5–8) | existence, bootstrap, endpoints, continuation | Per-datum existence; sequence-uniform low-order estimates |
| D. Terminal contradiction (§9) | Liouville selection, forbidden germ | Sequence-uniform |

The contradiction: Layer A gives $\int\Phi(g_i(T))=o(A_i)$.  Layer D
extracts a good pullback ball with $\fint\Phi\to0$, producing a smooth
Einstein germ with a forbidden Weyl spectrum.  The $A_i$-proportional
volume from Layer B carries the cancellation.

---

## 3. Terminal calibration lemma

**Source:** `step67_terminal_recalibration_recovery.md`.

Let $g$ be any smooth Riemannian metric on $M$ (with the fixed complex
orientation).  Define
$$
Q=\int_M|E|^2\,d\mu_g,\qquad
I=\frac1{4\pi^2}\int\!\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu_g,\qquad
J=\frac1{4\pi^2}\int\frac{|E^\circ|^2}{2}\,d\mu_g,
\tag{3.1}
$$
where $E^\circ=\operatorname{Ric}-\frac s4g$ is trace-free Ricci and
$W^+$ is the self-dual Weyl operator on $\Lambda^+$.

The orthogonal decomposition $E=E^\circ+\frac{s+4}{4}g$ gives
$$
\int(s+4)^2\le4Q,\qquad J\le\frac{Q}{8\pi^2}.
\tag{3.2}
$$
Mixed Seiberg–Witten averaging over the monopole sign family:
$$
I\ge\tfrac23\bigl[A+\sum_\ell|e_\ell^+|^2\bigr].
\tag{3.3}
$$
Chern–Weil identity: $I-J=\frac{2A}{3}-q$.  The averaged deficit is
$$
D_{\rm av}=J-q-\tfrac23\sum_\ell|e_\ell^+|^2,\qquad
0\le D_{\rm av}\le J\le\frac{Q}{8\pi^2}\quad(q\ge0).
\tag{3.4}
$$

**Calibration density (sign-free negative-part formulation).**  Put
$\nu=|W^+|$, $f=\frac23s-2\sqrt{2/3}\,\nu$,
$a_*=\frac23s+2w$ (with $w$ the lowest $W^+$ eigenvalue), and
$$
\mathcal G=f^2-a_{*,-}^2\ge0.
\tag{3.5}
$$
The nonnegativity of $\mathcal G$ does not require $s<0$ (see Step 8).
The exact square identity
$$
\frac{s^2}{24}+2\nu^2=\frac1{12}f^2+\frac1{216}(s+8\sqrt6\,\nu)^2
\tag{3.6}
$$
with the averaged inequality (3.3) and (3.4) gives
$$
\int(s+8\sqrt6|W^+|)^2\le108Q,\qquad
\int\mathcal G\le6Q.
\tag{3.7}
$$
Define the terminal calibration density
$$
\Phi=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+\mathcal G.
\tag{3.8}
$$
Then
$$
\boxed{\int_M\Phi\,d\mu_g\le(1+4+108+6)Q=119Q.}
\tag{3.9}
$$
**This holds for every smooth metric on $M$ with the fixed orientation,
with no flow, no scalar-sign assumption, and no density transport.**
The only inputs are the Seiberg–Witten monopole family and the Chern–Weil
identity for the IL geography with $q\ge0$.

---

## 4. Selected-support construction

**Source:** Steps 34, 43, 45 (§§4–5) with notation from Step 55 §1.
**Standalone proof:** `step70_selected_support_lemma.md` (824 lines,
TTCS-verified, 33/33 structural checks).

### 4.1 Full-curvature budget and maximal-function support selection

The selected-support construction begins from a **global integral** curvature
budget, not from pointwise curvature control.  Along a hypothetical
negative-pinched IL sequence, the initial metrics have
$\operatorname{Ric}_{g_i}\ge -2g_i$ for large $i$, calibrated volume
$\operatorname{Vol}(M_i,g_i)\asymp A_i$, and the full-curvature mean budget
$$
\int_{M_i}|\operatorname{Rm}_{g_i}|^2\,d\mu_{g_i}\le C_0A_i.
\tag{4.1a}
$$
Equivalently, since $T=\operatorname{Rm}-G$ and $|G|$ is dimensional,
$\int F_T^2\le C_0'A_i$ for $F_T=(1+|T|^2)^{1/2}$.  This budget is only
an $L^2$ statement; it does **not** bound sectional curvature at time zero.
The smoothing flow is needed precisely to convert this critical mean input
into positive-time pointwise curvature on the plateau.

Fix support ratios
$$
1<L_{\rm pl}<L_\chi<L_\eta,
\qquad (L_{\rm pl},L_\chi,L_\eta)=(5,6,7)
\tag{4.1b}
$$
for the displayed radii below, and choose the maximal-function scale
$R_0\ge L_\eta r$ (in practice one may take $R_0=10r$ to leave slack for
outer buffers).  Define the volume-average maximal function
$$
\mathcal M_{R_0}f(x)=\sup_{0<s\le R_0}\fint_{B_s(x)} f\,d\mu,
\qquad f=|\operatorname{Rm}_{g_i}|^2 .
\tag{4.1c}
$$
The use of $R_0\ge7r$ is load-bearing: a supremum only over radii
$s\le r$ would not control the auxiliary support $B_{7r}(x)$.

Choose a threshold
$$
\lambda={\widetilde\gamma^2\over r^4},
\tag{4.1d}
$$
where $\widetilde\gamma$ is fixed below the absorption scale and then $r$
is chosen small enough.  The Bishop--Gromov weak-type maximal inequality
under the Ricci lower bound gives
$$
\operatorname{Vol}\{x:\mathcal M_{R_0}f(x)>\lambda\}
\le {C(R_0)\over\lambda}\int_{M_i}|\operatorname{Rm}|^2
\le C{r^4\over\widetilde\gamma^2}A_i .
\tag{4.1e}
$$
Combining this with the calibrated lower volume
$\operatorname{Vol}(M_i,g_i)\ge c_VA_i$ and choosing
$C r^4/\widetilde\gamma^2<c_V/2$, the good set
$$
G_i=\{x:\mathcal M_{R_0}f(x)\le\lambda\}
\tag{4.1f}
$$
has $\operatorname{Vol}(G_i)\ge c_GA_i$.

Choose a maximal $r$-separated subset $\{x_\alpha\}\subset G_i$.  The good
set is covered by $\bigcup_\alpha B_r(x_\alpha)$, and Bishop--Gromov packing
and coloring give a subfamily whose outer buffers are disjoint and whose
inner balls retain an $A_i$-proportional total volume, as in §4.2.

### 4.2 Cutoff architecture and global weight

Apply a fixed-ratio coloring to the selected centers so that in one retained
color class the $B_{7r}(x_\alpha)$ are pairwise disjoint; the retained inner
volume is still $\ge\alpha_0A_i$ after adjusting $\alpha_0$ by a dimensional
packing factor.

For each retained center $x_\alpha$, choose smooth cutoffs:
$$
\chi_\alpha=1\text{ on }B_{5r}(x_\alpha),\qquad
\operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha),\qquad
|d\chi_\alpha|\le C/r.
\tag{4.2a}
$$
Auxiliary cutoff:
$$
\eta_\alpha=1\text{ on }B_{6r}(x_\alpha),\qquad
\operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha).
\tag{4.2b}
$$
Distance cutoffs are smoothed at a datum-dependent scale while preserving
the plateau, support inclusions, and the gradient bound.  Higher cutoff jets
are finite for each smooth datum but are not sequence-uniform inputs.

The **global cutoff** may be written
$$
\chi_i=\sum_\alpha\chi_\alpha,
\qquad
 a_i=\chi_i^2=\sum_\alpha\chi_\alpha^2\in[0,1],
\tag{4.2c}
$$
because the retained supports are disjoint.  On
$M_i\setminus\bigcup_\alpha B_{7r}(x_\alpha)$, $a_i=0$ and the metric is
stationary under the flow.

The cutoff flow (§5) uses **this single global $a_i$**, producing **one
global terminal metric** $g_i(T)$ on $M_i$.  This is essential: §§7–9 apply
the Seiberg–Witten inequality, global $Q$ propagation, and Liouville
averaging to one closed metric on the same smooth manifold.

The nested support identity for each $\alpha$:
$$
a_i|\nabla\eta_\alpha|^2
=(\nabla a_i)\cdot(\nabla\eta_\alpha)=0
\tag{4.2d}
$$
by disjoint support ($\operatorname{supp}\nabla\eta_\alpha\subset\{a_i=0\}$).
This replaces finite propagation, which does not hold for Ricci flow.

### 4.3 Initial energy seeds and collapse cancellation

On $U_\alpha=B_{7r}(x_\alpha)$ the maximal-function condition, with
$7r\le R_0$, gives
$$
\fint_{U_\alpha}|\operatorname{Rm}_{g_i}|^2\le {\widetilde\gamma^2\over r^4}.
\tag{4.3a}
$$
Thus the augmented curvature energy satisfies
$$
H_{2,\alpha}(0)=\int\eta_\alpha^2F_T^2\,d\mu_0
\le C\left(1+{\widetilde\gamma^2\over r^4}\right)
\operatorname{Vol}(U_\alpha).
\tag{4.3b}
$$
The four-dimensional relative Sobolev inequality on the same support is
$$
\|u\|_{L^4(U_\alpha)}^2
\le\mathcal S_\alpha(0)
\left(\|\nabla u\|_{L^2(U_\alpha)}^2+r^{-2}\|u\|_{L^2(U_\alpha)}^2\right),
\qquad
\mathcal S_\alpha(0)
\le C(L_\eta)r^2\operatorname{Vol}(U_\alpha)^{-1/2}.
\tag{4.4}
$$
Consequently the absorption parameter is controlled by the **product**
$$
\gamma_\alpha(0)=\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}
\le C(L_\eta)r^2\left(1+{\widetilde\gamma^2\over r^4}\right)^{1/2}
\le C(r^2+\widetilde\gamma).
\tag{4.5}
$$
This is the collapse cancellation from the actual support estimates:
$\mathcal S_\alpha$ itself may grow like
$r^2\operatorname{Vol}(U_\alpha)^{-1/2}$ under collapse, and
$H_{2,\alpha}^{1/2}$ shrinks like $\operatorname{Vol}(U_\alpha)^{1/2}$.
Only their product is sequence-uniformly small.  No pointwise sectional
curvature bound is assumed at time zero.

### 4.4 Proportional-volume plateau and volume upper bound

The calibrated Chern–Weil geography gives
$$
\operatorname{Vol}(M_i,g_i)\ge\frac{32\pi^2}{9}A_i(1-C\delta_i)
\tag{4.6}
$$
as $\delta_i\to0$.  The inner plateau set
$P_i=\bigcup_\alpha B_r(x_\alpha)$ satisfies
$$
\operatorname{Vol}_{g_i}(P_i)\ge\alpha_0 A_i
\tag{4.7}
$$
for a universal $\alpha_0>0$, independent of $i$.

**Volume upper bound.**  Since $|\operatorname{tr}E|\le4\delta_i$,
we have $s\ge-4-4\delta_i$.  The mixed SW inequality gives
$$
I\ge\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i),
$$
while $I=J+\frac{2A_i}{3}-q_i\le J+\frac{2A_i}{3}$ and
$J\le\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i)$.
For $\delta_i$ small:
$$
\operatorname{Vol}(M_i)\le CA_i.
\tag{4.8}
$$
Consequently $Q(0)=\int|E_i|^2\le4\delta_i^2\operatorname{Vol}(M_i)
\le C\delta_i^2A_i$, giving $Q(0)/A_i\to0$.

---

## 5. Per-datum cutoff-flow existence

**Source:** `step65_per_datum_existence_theorem.md`.

**Theorem (per-datum existence).**  For any closed Riemannian manifold
$(M^n,\bar g)$, smooth positive metric $g_0$, smooth cutoff
$\chi:M\to[0,1]$, and $\sigma\in\mathbb R$, there exists
$T_0=T_0(g_0,\chi,\bar g,\sigma,n)>0$ and a smooth solution of
$$
\partial_tg=-2\chi^2(\operatorname{Ric}_g-\sigma g),
\qquad g(0)=g_0,
\tag{5.1}
$$
on $M\times[0,T_0]$.

**Construction.** Doubly regularized $(\varepsilon,\nu)$
transported-DeTurck system with diagonal strongly parabolic principal
symbol (Legendre–Hadamard constant $\min(\varepsilon\lambda,\nu)$).
Standard quasilinear parabolic existence for each fixed
$(\varepsilon,\nu)>0$.  $(\varepsilon,\nu)$-independent tame hierarchy
gives uniform $C^k$ bounds on a common interval $[0,T_0]$.  All-order
$m$-level Grönwall continuation prevents finite-time blowup.
Arzelà–Ascoli diagonal convergence produces a smooth solution of the
exact degenerate system.  DeTurck pullback recovers the geometric
equation.

**Application to the IL sequence.** For each $(M_i,g_i)$ use the single
global smooth cutoff $\chi_i$ from §4.2, so that
$a_i=\chi_i^2=\sum_\alpha\chi_\alpha^2$.  The theorem gives a smooth
solution on a datum-dependent interval $[0,T_{0,i}]$ for the one global
flow producing one global terminal metric.  The local estimates in §6 are
then applied on each disjoint buffered component using its auxiliary
$\eta_\alpha$.

**Remark on uniformity.** The per-datum existence gives datum-dependent
higher-order bounds and existence times.  The sequence-uniform estimates
used in the contradiction (§§6–7 below) are the low-order curvature,
defect, and $Q$ bounds from the first-exit bootstrap, not the full
$C^k$ hierarchy.

---

## 6. Coupled first-exit bootstrap

**Source:** `step55_joint_bootstrap_background_continuation_repair.md`.

### 6.1 Bootstrap variables

On each selected support $\alpha$, define:
$$
\gamma_\alpha(t)=\mathcal S_\alpha(t)\sqrt{H_{2,\alpha}(t)},\qquad
\Gamma(t)=\max_\alpha\sup_{s\le t}\gamma_\alpha(s),
$$
$$
V(t)=\int_0^t\|aE(s)\|_{L^\infty}\,ds.
\tag{6.1}
$$
The provisional first-exit assumptions on $[0,T]$ with $T\le\theta r^2$:
$$
\Gamma(T)\le\gamma_*,\qquad V(T)\le V_*.
\tag{6.2}
$$

### 6.2 Bilipschitz and Sobolev transport from $V$

$$
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0),\qquad
\mathcal S(t)\le e^{8V(t)}\mathcal S(0).
\tag{6.3}
$$
No evolving Ricci lower bound is assumed.

### 6.3 Augmented curvature energy

Under (6.2) and the convention of §1, including the corrected
non-homogeneous shifted-curvature evolution
$\partial_tT=-2aT+2aG+\text{gradient terms}$ (Step 64):
$$
H_{2,\alpha}'(t)+c D_{2,\alpha}(t)
\le C_H(1+r^{-2})H_{2,\alpha}(t)
+C_V\|aE(t)\|_\infty H_{2,\alpha}(t).
\tag{6.4}
$$
The extra $2aG$ zero-order term from the convention correction is
bounded by $CaF_T^2\le CaF_T^3$ (since $F_T\ge1$) and absorbed
into the existing reaction structure.  Hence (using Sobolev transport from
§6.2)
$$
\gamma(t)\le\gamma(0)
\exp\bigl\{(8+\tfrac12C_V)V(t)+C_H\theta\bigr\}.
\tag{6.5}
$$
### 6.4 Curvature branch: integrated energy before positive-time pointwise bounds

**Sources:** `step34_integrated_potential_q3_and_defect.md`,
`step63_curvature_variation_index_proof.md`.

The first curvature input is the independently integrated $q=2$ energy
estimate on the same buffered support:
$$
K_{2,\alpha}^\eta(t)+\int_0^tD_{2,\alpha}^\eta(s)\,ds
\le C K_{2,\alpha}^\eta(0),
\tag{6.6a}
$$
obtained by absorbing
$Y_\alpha=\int\eta_\alpha^2a_iF_T^3$ through the small product
$\gamma_\alpha=\mathcal S_\alpha(K_{2,\alpha}^\eta)^{1/2}$.  Consequently
$$
\int_0^tY_\alpha(s)\,ds\le C\gamma_\alpha K_{2,\alpha}^\eta(0),
\qquad
\int_0^t\mathcal S_\alpha(s)^2Y_\alpha(s)\,ds\le C\gamma_\alpha^3 .
\tag{6.6b}
$$
This integrated estimate is what is used near time zero.  It does not come
from the later pointwise bound $\mathcal S^2Y\le C\gamma^3/t$.

For a fixed positive target time $t>0$, the integrated bound supplies a
good slice $\tau\in[t/4,t/2]$ with
$Y_\alpha(\tau)\le C\gamma_\alpha K_{2,\alpha}^\eta(0)/t$.  Propagating the
$q=3$ inequality from that slice gives, on positive-time slabs,
$$
Y_\alpha(t)\le {C\gamma_\alpha K_{2,\alpha}^\eta(0)\over t},
\qquad
\mathcal S_\alpha(t)^2Y_\alpha(t)
\le {C\gamma_\alpha^3\over t}.
\tag{6.6c}
$$
The $t^{-1}$ expression is therefore a positive-time Moser coefficient; it
is not integrated from $0$.  The subsequent curvature Moser iteration gives
$$
\|a_iF_T(t)\|_\infty\le {C\Gamma\over t},
\qquad 0<t\le T.
\tag{6.6d}
$$
This endpoint is a smoothing output.  It is not an initial sectional
curvature assumption.

### 6.5 Defect Moser endpoint (three-factor route)

**Source:** `step62_defect_moser_general_p_proof.md`.
**Standalone proof:** `step70_defect_moser_real_exponent.md` (real-exponent
regularization, explicit time cutoffs, endpoint identification).

The $J_6$ seed persists by two-factor absorption (Step 34 §5):
$$
J_6(t)
\le e^{C(1+r^{-2})t}J_6(0).
\tag{6.7}
$$
For the high-$p$ ladder one uses the general-$p$ three-factor inequality
(Proposition 4.1 of Step 62):
$$
J_p'+c_1'pD_p^E+c_2'p^2Q_p
\le Cp^N\bigl(r^{-2}+1+\mathcal S^2Y\bigr)J_p.
\tag{6.8}
$$
The coefficient $\mathcal S^2Y$ is controlled on each nested Moser slab by
(6.6b)--(6.6c): on $[\tau_k,t]$ with $\tau_k\ge t/2$,
$$
\int_{\tau_k}^{t}\mathcal S^2Y\,ds\le C\gamma^3,
\qquad
\sup_{s\in[\tau_k,t]}\mathcal S(s)^2Y(s)
\le {C\gamma^3\over \tau_k}.
\tag{6.8a}
$$
Thus the high-$p$ absorption condition is independent of $p$; the two-factor
route is retained only for the $p=6$ seed because its direct high-$p$
absorption would require $\gamma_t\le c/p$.  The nested time-integrated
recurrence, seeded by
$I_0=\int_{t/2}^tJ_6(s)ds\le CtJ_6(0)$ rather than by a Sobolev-weighted
point value, gives
$$
\|a_iE(t)\|_\infty
\le C_E\delta_i\left({r^2\over t}\right)^{1/3},
\qquad 0<t\le T.
\tag{6.9}
$$
Here $\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\mathrm{op}}$; the fixed Hilbert--Schmidt dimensional factor is absorbed into $C_E$.
The repaired standalone proof keeps the Step 62 weights
$J_p=\int\eta^2a^{p-2}|E|^p$ and
$z_p=\eta a^{(p-1)/2}|E|^{p/2}$, so the large-$p$ limit controls
$aE$ throughout the transition region.  Its time-integrated Moser product
retains the $L_k^{3/2}$ factor, giving
$\mathcal S^{1/3}t^{-1/2}I_0^{1/6}$ before substituting
$I_0\le CtJ_6(0)$; this is what recovers the final $t^{-1/3}$ exponent.
The zero-time input is the integrated $q=2$/seed estimate, not the
positive-time $t^{-1}$ coefficient.

### 6.6 Integrated defect velocity and $V$-improvement

$$
V(T)=\int_0^T\|a_iE(t)\|_\infty\,dt
\le\frac{3}{2}C_E\delta_i\theta^{2/3}r^2.
\tag{6.10}
$$
For $\delta_i\le V_*/(3C_E\theta^{2/3}r^2)$, this improves $V(T)\le V_*/2$.
### 6.7 Bootstrap closure

Choose $V_*,\theta>0$ (universally) so that
$$
\exp\bigl\{(8+\tfrac12C_V)V_*+C_H\theta\bigr\}\le\tfrac32.
\tag{6.11}
$$
If initially $\gamma(0)\le\gamma_*/2$, then (6.5) improves to
$\Gamma(T)\le\frac34\gamma_*$.  Combined with the $V$-improvement (6.10),
the standard first-time argument closes the coupled $(\Gamma,V)$
bootstrap on $[0,\theta r^2]$.

**All estimates in §6 are sequence-uniform:** they depend on $r$, $\theta$,
$\gamma_*$, $V_*$, the maximal-function threshold $\widetilde\gamma$, and
the full-curvature budget constant $C_0$, not on $i$, $A_i$, or
datum-dependent higher-order bounds.  They use only the initial product
smallness $\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}$, not a uniform bound
for $\mathcal S_\alpha(0)$ or for initial sectional curvature.
---

## 7. Global $Q$ propagation

On the exact flow, the selected supports have frozen (stationary)
complement.  The global unweighted defect:
$$
Q(t)=\int_M|E(t)|^2\,d\mu_{g(t)}.
\tag{7.1}
$$
On each support, the defect equation gives
$\frac{d}{dt}\int_{\rm supp}|E|^2\le C(1+r^{-2})\int_{\rm supp}|E|^2
+C\|aE\|_\infty\int_{\rm supp}|E|^2$.
On the complement, $\partial_tg=0$ so $E$ is frozen.  Summing:
$$
Q(T)\le e^{C(1+r^{-2})T+C_VV(T)}Q(0).
\tag{7.2}
$$
Since $Q(0)=\int|E_i|^2\le\delta_i^2\operatorname{Vol}(M_i)
=O(\delta_i^2 A_i)$, we get $Q(T)/A_i\to0$ for fixed parameters.

**Remark.** This global estimate uses the exact flow, not the
regularization.  It is applied after the per-datum existence theorem
gives a smooth solution and after the first-exit bootstrap gives the
common time $\theta r^2$.

---

## 8. All-order continuation and common observation time

**Sources:** `step58_all_order_continuation_proof.md`,
`step59_induction_ledger_repair.md`,
`step60_base_pair_proof.md`,
`step55_joint_bootstrap_background_continuation_repair.md` §2.

### 8.1 The continuation problem

The per-datum existence theorem (§5) gives a smooth solution for the single
global cutoff on $[0,T_{0,i}]$.  The first-exit bootstrap (§6) uses the
common parameter $\theta r^2$.  If $T_{0,i}<\theta r^2$ for some datum, we
must show that the solution can be restarted past that time.

### 8.2 Datum-dependent all-order hierarchy

On the smooth positive-time slab $[\tau,T_*)$ with $\tau>0$, define
the weighted curvature derivatives
$U_m=\nabla^m(aT)$, cutoff jets
$C_m=\nabla^m\chi$, and connection difference
$A(t)=\nabla^{g(t)}-\nabla^{g(\tau)}$.

**Base pair $(U_1,C_2)$.**  The $C_2$ evolution is exact:
$\partial_tC_2=g^{-1}*U_1*C_1$ (no $U_2$ term, because
$\nabla^2\chi$ has one algebraic Christoffel insertion).  All
$m=1$ Hessian terms have the signed-Hessian form.  Coupled
Grönwall from $U_0\in L^\infty+T_0\in L^q_{\rm fin}$ gives
finite $(U_1,C_2)$ bounds.  Then $T_1$ and $T_0\in L^\infty$
follow.  (Source: `step60_base_pair_proof.md`.)

**General induction for $m\ge2$.**  The highest cutoff jet
$C_{m+2}$ occurs paired only with $U_0$.  At each level,
coupled Hölder$(4,p,4,2p/(p-2))$ absorption and signed-Hessian
IBP yield:
$$
\frac{d}{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int a|\nabla U_m|^2|U_m|^{p-2}
\le\mathcal C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr),
\tag{8.1}
$$
where $\mathcal C_{m,p}$ depends on all previous-level bounds and
per-datum constants.  (Source: `step58_all_order_continuation_proof.md`
with the Step 59 ledger repair.)

**Fixed-background conversion.**  On the positive-time slab, the
connection difference satisfies the strictly triangular evolution
$$
\partial_tA_m=g^{-1}*U_{m+1}
+P_m(A_{\le m-1},U_{\le m},g^{-1}),
\tag{8.2}
$$
with no current $A_m$ coefficient (Step 55 §2).  This converts
current-pair bounds to fixed-background Sobolev restart data.

### 8.3 Continuation argument

Suppose the maximal smooth existence time $T_*<\theta r^2$ for
some datum.  On $[\tau,T_*)$ with $\tau>0$, the all-order hierarchy
gives finite $\bar\nabla^m g$ bounds for every $m$, uniformly on
compact subsets of $[\tau,T_*)$.  Therefore $g(t)\to g(T_*)$
converges in $C^\infty(M)$ as $t\to T_*$, giving a smooth positive
metric $g(T_*)$.  Reapplying the per-datum existence theorem with
initial data $g(T_*)$ extends the solution past $T_*$, contradicting
maximality.  Hence every datum reaches $\theta r^2$.

**Critical distinction:**  The all-order bounds at level $m\ge2$ are
datum-dependent.  They may grow with $i$.  The first-exit quantities
$\Gamma,V,Q$ that enter the terminal contradiction are sequence-uniform
(§§6–7), not these higher-order bounds.  The terminal convergence in
§9.5 uses $W^{2,p}$ elliptic regularity, not $C^\infty$
Cheeger–Gromov, so datum-dependent higher-order bounds do not leak
into the contradiction.

### 8.4 Observations on the common time

After continuation, each $(M_i,g_i)$ has a smooth solution on
$[0,\theta r^2]$.  At terminal time $T=\theta r^2$:

- **Bounded curvature on plateau:**
  $|\operatorname{Rm}(T)|\le K(\gamma_*,\theta,r)$ on $\{a=1\}$.
  This is sequence-uniform.
- **Metric distortion:** $V(\theta r^2)\le C\delta_i\theta^{2/3}r^2\to0$.
  Sequence-uniform.
- **Global $Q$:** $Q(T)/A_i\to0$.  Sequence-uniform.
- **Proportional inner volume:**
  $\operatorname{Vol}_{g_i(T)}(P_i)\ge\alpha_0 A_i/2$ for large $i$.
  Sequence-uniform (drift from (6.10) is small).

---

## 9. Terminal contradiction

### 9.1 Apply terminal calibration

At terminal time $T$, $g_i(T)$ is a smooth closed metric on the same
smooth manifold $M_i$ with the same IL geography.  Applying the terminal
calibration lemma (§3):
$$
\int_{M_i}\Phi(g_i(T))\,d\mu_{g_i(T)}\le119Q(T).
\tag{9.1}
$$

### 9.2 Local forbidden-germ lower bound

**Source:** `step8_derdzinski_measure_local_theorem.md`.

**Proposition (forbidden germ).**  There exist $K_0,\rho_0,\eta>0$
(universal) such that for any smooth Riemannian 4-ball $(B,g)$ with
$|\operatorname{Rm}|\le K_0$ and noncollapse
$\operatorname{Vol}(B)\ge v_0\rho_0^4$:
$$
\fint_{B_{\rho_0/2}(0)}\Phi\,d\mu_g\ge\eta.
\tag{9.2}
$$

**Proof mechanism.**  If (9.2) failed, a compactness argument would
produce a smooth Einstein germ with $\Phi=0$, forcing:
$$
E=0\ (s=-4),\qquad |W^+|^2=1/24,\qquad \mathcal G=0.
\tag{9.3}
$$
The gap algebra (from $\mathcal G=0$) forces
$\operatorname{spec}(W^+)=(-1/6,1/12,1/12)$:  a two-eigenvalue profile.
By Derdziński's Proposition 5, an Einstein metric with $\delta W^+=0$
and at most two distinct $W^+$ eigenvalues is locally conformal to
Kähler.  The conformal factor is $(24|W^+|^2)^{1/3}=1$ (constant),
so the metric itself is locally Kähler.  But a Kähler–Einstein
four-germ with $\operatorname{Ric}=-g$ has $|W^+|^2=s^2/24=2/3$,
contradicting $|W^+|^2=1/24$. $\square$

### 9.3 Liouville pullback-ball averaging

**Source:** `step28_terminal_recalibration_pullback.md`,
`step45_consolidated_IL_negative_gap_proof.md` §7.

For each $p\in P_i$ (inner plateau at terminal time), define the
exponential pullback ball in the tangent space:
$$
\mathcal B_\rho(p)=\{v\in T_pM:|v|_{g_i(T)}<\rho\},\qquad
\tilde g_p=(\exp_p)^*g_i(T).
\tag{9.4}
$$
By bounded curvature (§8.4) and Rauch comparison, the pullback ball
$(\mathcal B_\rho,\tilde g_p)$ is noncollapsed with uniform geometry,
even if the exponential map folds or self-overlaps on the base manifold.

The unit tangent bundle carries the Liouville measure
$d\Lambda=d\mu\wedge d\sigma$.  The geodesic flow $\varphi_t$ preserves
$\Lambda$.  For the nonnegative density $\Phi$:
$$
\int_{P_i}\mathcal A_\rho\Phi(p)\,d\mu_{g_i(T)}(p)
\le C(K,\rho)\int_{M_i}\Phi(g_i(T))\,d\mu_{g_i(T)}.
\tag{9.5}
$$
where $\mathcal A_\rho\Phi(p)=\fint_{\mathcal B_\rho(p)}
(\exp_p)^*\Phi\,d\mu_{\tilde g_p}$.

**Remark on collapse.** The Liouville measure averaging uses the
geodesic flow on the unit tangent bundle.  It does not require a
lower volume bound for base-manifold balls; the noncollapse and
geometry control are on the tangent-space pullback ball.

### 9.4 $A$-proportional cancellation

From (9.1) and (9.5):
$$
\int_{P_i}\mathcal A_\rho\Phi(p)\,d\mu(p)
\le C\cdot119\,Q(T)=o(A_i).
\tag{9.6}
$$
Since $\operatorname{Vol}_{g_i(T)}(P_i)\ge\alpha_0 A_i/2$, some
$p_i\in P_i$ satisfies
$$
\mathcal A_\rho\Phi(p_i)
\le\frac{2C\cdot119\,Q(T)}{\alpha_0 A_i}\to0.
\tag{9.7}
$$

### 9.5 Convergence and contradiction

The pullback balls $(\mathcal B_\rho(p_i),\tilde g_{p_i})$ have
uniformly bounded curvature and noncollapse.  The convergence uses
**finite regularity, not $C^\infty$ Cheeger–Gromov** (which would
require datum-dependent curvature-derivative bounds):

1. Uniformly bounded curvature gives uniform $C^{1,\alpha}$ harmonic
   coordinates on a slightly smaller ball $B_{\rho'}$.
2. In these coordinates, the Ricci equation
   $g^{ab}\partial_a\partial_b g_{jk}=-2\operatorname{Ric}_{jk}
   +Q(g^{-1},\partial g)$ has uniformly bounded $C^{1,\alpha}$
   coefficients.  Since $\mathcal A_\rho|E_i|^2\to0$, the right-hand
   side $\operatorname{Ric}=-g+E_i$ converges strongly in $L^p$.
   Interior elliptic estimates give
   $\tilde g_{p_i}\to g_\infty$ strongly in $W^{2,p}_{\rm loc}$
   for all $p<\infty$.
3. The $W^{2,p}$ convergence passes $s,W^+,\mathcal G$ in $L^1_{\rm loc}$.
   Since $\int\Phi(\tilde g_{p_i})\to0$ and $\Phi\ge0$, we get
   $\Phi_{g_\infty}\equiv0$ pointwise.
4. The limit satisfies $\operatorname{Ric}_{g_\infty}=-g_\infty$
   weakly, then smoothly by Einstein elliptic regularity.

The forbidden germ (§9.2) gives $\fint\Phi\ge\eta>0$:
contradiction. $\square$

**Remark.**  This is the mechanism already in Step 45 §3.2–3.3.
No datum-dependent higher-order bounds leak into the terminal
contradiction.

---

## 10. Module dependency chart

```
Terminal calibration (§3)
  ↑ pure topology/Chern–Weil, no flow input
  
Selected-support construction (§4)
  ↑ maximal function, initial geometry, q≥0 geography

Per-datum existence (§5)
  ↑ doubly regularized DeTurck, tame hierarchy, pullback

(Γ,V) bootstrap (§6)
  ├─ Curvature endpoint (§6.4) [Step 63]
  │   ↑ H₂ inequality, convention correction
  ├─ Defect endpoint (§6.5) [Step 62, three-factor]
  │   ↑ J₆ seed, S²Y coefficient from curvature branch
  └─ V-improvement (§6.6)
      ↑ integrated defect velocity

Global Q propagation (§7)
  ↑ exact flow + stationary complement

All-order continuation (§8)
  ↑ base pair + induction [Steps 58–60]
  ↑ fixed-background conversion [Step 55 §2]
  ⚠ datum-dependent (NOT used in terminal estimates)

Terminal contradiction (§9)
  ├─ Liouville averaging [Step 28/45]
  ├─ Forbidden germ [Step 8, Derdziński]
  └─ A-proportional cancellation
```

---

## 11. Uniformity separation record

**Sequence-uniform inputs to the contradiction:**
- $\varepsilon_{\rm IL}$: universal constant.
- $r,R_0,\theta,\gamma_*,V_*,\widetilde\gamma$: universal parameters with
  $R_0\ge7r$ so the maximal function controls the outer buffers.
- The full-curvature budget constants in
  $\operatorname{Vol}(M_i)\asymp A_i$ and $\int F_T^2\le C A_i$.
- The collapse-cancelling initial products
  $\gamma_\alpha(0)=\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}$; neither
  $\mathcal S_\alpha(0)$ nor initial sectional curvature is assumed uniformly
  bounded.
- $\alpha_0$: universal proportional-volume constant for the strict inner
  plateau.
- $K,\rho,\eta$: forbidden-germ constants after positive-time smoothing and
  pullback noncollapse.
- $C$ in (9.5): Liouville geometry constant.
- First-exit curvature/defect endpoints (6.6d), (6.9).
- Global $Q$ propagation (7.2).

**Datum-dependent (NOT entering the contradiction):**
- Per-datum existence time $T_{0,i}$ for the single global cutoff flow.
- All-order continuation bounds at level $m\ge2$.
- Fixed-background $A$-bounds (§8.2).
- Higher-order restart data.

The datum-dependent hierarchy is used only to ensure each solution reaches
$\theta r^2$.  Once there, only the sequence-uniform curvature, defect, $Q$,
and volume estimates are used.

---

## 12. Convention audit trail

| Module | Original convention | Status under canonical $T=\operatorname{Rm}-G$ |
|--------|--------------------|-------------------------------------------------|
| Step 63 curvature endpoint | $T=\operatorname{Rm}-G$ (canonical) | Anchor |
| Step 64 consistency sweep | Audits old notes | All old $T_{\rm old}=T$ |
| Step 62 defect Moser | $G$-free | Unchanged |
| Step 55 $(\Gamma,V)$ | Uses only $F_T,\nabla T,E$ | Unchanged under $G_{\rm old}=-G$ |
| Steps 58–60 continuation | Schematic $a(T+T*T)$ | Zero-order $G$ absorbed |
| Step 65 existence | Convention-independent | N/A |
| Step 67 terminal calibration | Pure topology | N/A |
| Step 28/45 Liouville | Uses $\Phi,\operatorname{Rm},W^+$ | Convention-independent |

The only module with a direct convention dependence is Step 63 (curvature
variation and $H_2$ inequality), which is already the canonical anchor.
The extra $2aG$ term in $\partial_tT=-2aT+2aG+\nabla\text{ terms}$ adds
$CaF_T^2\le CaF_T^3$ to the reaction, absorbed by the existing $Y$-term.

---

## 13. What remains for the full Yau Problem 26

This restricted IL theorem addresses only one branch of the original
problem.  The unresolved fronts are:

1. **Positive branch ($\operatorname{Ric}\approx+g$):**  no curvature
   budget analogous to the SW/Chern–Weil mechanism; no forbidden positive
   Einstein germ; Myers compactness helps but collapse is not excluded.
   
2. **Arbitrary four-manifold topology:** the IL geography with $q\ge0$
   is a proper subset of all closed oriented four-manifolds.

3. **Dimensions $n\ge5$:** no SW or self-dual Weyl machinery available.
   No known structural replacement.

4. **Lean 4 formalization:** requires a stable complete mathematical
   resolution, not yet achieved.

5. **Quantifier structure:** a full proof needs one dimension-only
   sign branch per dimension; a full refutation needs a family defeating
   all admissible intervals on the same or related manifolds.

---

## 14. Source file register

| Note | Path |
|------|------|
| Terminal calibration | `workspace/notes/step67_terminal_recalibration_recovery.md` |
| Per-datum existence | `workspace/notes/step65_per_datum_existence_theorem.md` |
| $(\Gamma,V)$ bootstrap | `workspace/notes/step55_joint_bootstrap_background_continuation_repair.md` |
| Defect Moser endpoint | `workspace/notes/step62_defect_moser_general_p_proof.md` |
| Curvature endpoint | `workspace/notes/step63_curvature_variation_index_proof.md` |
| Convention sweep | `workspace/notes/step64_convention_consistency_sweep.md` |
| Base pair proof | `workspace/notes/step60_base_pair_proof.md` |
| All-order continuation | `workspace/notes/step58_all_order_continuation_proof.md` |
| Induction ledger repair | `workspace/notes/step59_induction_ledger_repair.md` |
| Terminal pullback selection | `workspace/notes/step28_terminal_recalibration_pullback.md` |
| Forbidden germ | `workspace/notes/step8_derdzinski_measure_local_theorem.md` |
| Consolidated prior assembly | `workspace/notes/step45_consolidated_IL_negative_gap_proof.md` |
| Mixed SW bound | `workspace/notes/step3_mixed_bound_analysis.md` |
| Route assessment | `workspace/plans/route_assessment_step67.md` |
