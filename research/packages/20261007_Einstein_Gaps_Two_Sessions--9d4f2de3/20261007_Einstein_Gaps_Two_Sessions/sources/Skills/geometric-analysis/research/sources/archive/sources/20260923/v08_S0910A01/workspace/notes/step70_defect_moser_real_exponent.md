# Step 70/71: Real-exponent defect Moser endpoint with the Step 62 weights

Session: S0910A01.  Agent2 construction repaired by Agent1 in Step 71.

## Purpose

This note is the corrected standalone expansion of assembly §6.5.  It
keeps the weighted hierarchy from Step 62 and only adds the real-exponent
regularization and explicit time-slab arithmetic.  The Step 70 draft used
fixed weight $a^2$ in $J_p$ while testing the equation with $a^{p-2}$;
that mixed two different hierarchies and made the large-$p$ norm see the
wrong quantity on the transition region.  The hierarchy below is the one
needed for the metric-velocity bound
\[
   V(T)=\int_0^T\|aE(t)\|_\infty\,dt .
\]

Throughout $n=4$, $a=\chi^2\in[0,1]$, $E=\operatorname{Ric}+g$,
$F=(1+|T|^2)^{1/2}$, and the flow is
\[
   \partial_tg=-2aE .
\]
We work on one buffered support $U=B_{7r}(x_\alpha)$ with auxiliary
cutoff $\eta$ satisfying $\eta=1$ on a neighbourhood of $\operatorname{supp}a$
and $\operatorname{supp}d\eta\subset\{a=0\}^{\circ}$.  Cutoffs are chosen
flat at the boundary of their zero set; equivalently one may prove the
identities first for regularized weights and pass to the limit.  Thus
$a^\beta$ is an admissible smooth test weight for all real $\beta>0$, and
its derivatives obey the usual square-cutoff estimates with constants
polynomial in $\beta$.

---

## 1. Curvature-branch inputs

The defect iteration uses two curvature-branch facts.  The first is valid
from time zero:
\[
 K_2^\eta(t)+\int_0^tD_2^\eta\le C K_2^\eta(0),
 \qquad
 \int_0^t\mathcal S^2Y\le C\gamma^3 .
\tag{1.1}
\]
The second is a positive-time consequence and is used only on inner Moser
slabs separated from $0$:
\[
 \mathcal S(s)^2Y(s)\le {C\gamma^3\over s},\qquad s>0.
\tag{1.2}
\]
Here $Y=\int\eta^2aF^3$ and
$\gamma=\mathcal S(0)K_2^\eta(0)^{1/2}$ after the bilipschitz transport
from the coupled bootstrap.  The distinction between the integrated input
in (1.1) and the positive-time bound (1.2) is part of the mechanism.

---

## 2. Real-exponent weighted objects

For $\varepsilon>0$ and real $p\ge6$, put
\[
 s_\varepsilon=|E|^2+\varepsilon,
\]
and keep the Step 62 weights
\[
 J_{p,\varepsilon}
 =\int \eta^2 a^{p-2}s_\varepsilon^{p/2}\,d\mu_t,
 \qquad
 D^E_{p,\varepsilon}
 =\int \eta^2 a^{p-1}s_\varepsilon^{p/2-1}|\nabla E|^2\,d\mu_t,
\tag{2.1}
\]
\[
 Q_{p,\varepsilon}
 =\int\eta^2a^{p-1}s_\varepsilon^{p/2-2}|\nabla s_\varepsilon|^2\,d\mu_t,
 \qquad
 z_{p,\varepsilon}=\eta\,a^{(p-1)/2}s_\varepsilon^{p/4}.
\tag{2.2}
\]
The power $a^{p-2}$ is essential.  Since
\[(a^{p-2})^{1/p}\to a,
\]
the large-$p$ norm of $J_p$ detects $a|E|$ throughout the whole transition
region $0<a<1$, not merely $|E|$ on the plateau.

The Sobolev-gradient energy is not the radial dissipation alone.  The
square-cutoff derivative bound $|\nabla a|^2\le Ca/r^2$ and the support
condition on $d\eta$ give
\[
 \|\nabla z_{p,\varepsilon}\|_2^2
 \le C p^2\bigl(Q_{p,\varepsilon}+r^{-2}J_{p,\varepsilon}\bigr)
     +C p^2D^E_{p,\varepsilon},
\tag{2.3}
\]
and Kato converts the radial term into the tensor dissipation when needed.
Thus the Sobolev step always uses
\[
 \|z_{p,\varepsilon}\|_4^2
 \le C\mathcal S p^2
       \bigl(D^E_{p,\varepsilon}+Q_{p,\varepsilon}+r^{-2}J_{p,\varepsilon}\bigr),
\tag{2.4}
\]
while the energy inequality retains both $D^E_p$ and $Q_p$.

---

## 3. General-$p$ defect inequality with the correct weight

Testing the regularized defect equation for $s_\varepsilon$ against
$\eta^2a^{p-2}s_\varepsilon^{p/2-1}$ gives, uniformly as
$\varepsilon\downarrow0$,
\[
 J'_{p,\varepsilon}
 +c_1pD^E_{p,\varepsilon}+c_2p^2Q_{p,\varepsilon}
 \le Cp^N(1+r^{-2})J_{p,\varepsilon}+Cp\,P_{p,\varepsilon}+R_\varepsilon,
\tag{3.1}
\]
with $R_\varepsilon\to0$ and
\[
 P_{p,\varepsilon}
 =\int\eta^2a^{p-1}F s_\varepsilon^{p/2}.
\tag{3.2}
\]
The cutoff-Hessian terms are the Step 34 signed integrations by parts;
terms involving $d\eta$ vanish because $a|d\eta|^2=(da)\cdot d\eta=0$.
Cross terms produced by $d(a^{p-2})$ are treated Kato-first, so their
powers match $J_p$ and do not create a different hierarchy.

The three-factor identity is exact for the Step 62 weights:
\[
 \eta^2a^{p-1}Fs_\varepsilon^{p/2}
 = (aF^3)^{1/3}
   (\eta^2a^{p-2}s_\varepsilon^{p/2})^{1/3}
   z_{p,\varepsilon}^{4/3}.
\tag{3.3}
\]
Hölder, Sobolev, and Young therefore give
\[
 CpP_{p,\varepsilon}
 \le \epsilon\bigl(c_1pD^E_{p,\varepsilon}+c_2p^2Q_{p,\varepsilon}\bigr)
   +C_\epsilon p^N\mathcal S^2Y\,J_{p,\varepsilon}
   +Cp^N r^{-2}J_{p,\varepsilon}.
\tag{3.4}
\]
The term $\epsilon pQ_p$ is absorbed into $c_2p^2Q_p$ for every
$p\ge2$ without imposing $\gamma\le c/p$.  After absorption and
letting $\varepsilon\downarrow0$,
\[
 J'_p+c_1'pD^E_p+c_2'p^2Q_p
 \le Cp^N\bigl(1+r^{-2}+\mathcal S^2Y\bigr)J_p .
\tag{3.5}
\]

---

## 4. The fixed seed $J_6$

For $p=6$ the two-factor estimate is harmless because the exponent is
fixed:
\[
 P_6\le C\gamma\,(Q_6+r^{-2}J_6).
\]
With $\gamma$ chosen below the universal seed threshold,
\[
 J_6(s)\le e^{C(1+r^{-2})s}J_6(0),
 \qquad 0\le s\le\theta r^2 .
\tag{4.1}
\]
Consequently, for a target time $0<t\le\theta r^2$,
\[
 I_0:=\int_{t/2}^{t}J_6(s)\,ds
 \le CtJ_6(0)
 \le Ct\,\delta^6\operatorname{Vol}(U).
\tag{4.2}
\]
No Sobolev factor is introduced into this seed.

---

## 5. Time-integrated Moser ladder

Fix $t\in(0,\theta r^2]$ and define nested slabs
\[
 \tau_k=t(1-2^{-(k+1)}),\qquad p_{k+1}=\frac32p_k,
 \qquad p_0=6.
\tag{5.1}
\]
Let $\zeta_k$ vanish before $\tau_{k-1}$, equal one on $[\tau_k,t]$, and
satisfy $|\zeta_k'|\le C2^k/t$.  Set
\[
 I_k=\int_{\tau_k}^{t}J_{p_k}(s)\,ds .
\tag{5.2}
\]
The standard parabolic Moser step obtained from (3.5), (2.4), and the
interpolation relation $p_{k+1}=3p_k/2$ has the form
\[
 I_{k+1}
 \le Cp_k^N\mathcal S\bigl(L_k I_k\bigr)^{3/2},
 \qquad
 L_k=Cp_k^N4^k(t^{-1}+r^{-2}).
\tag{5.3}
\]
The power $L_k^{3/2}$ is retained.  Since $t\le\theta r^2$, the term
$r^{-2}$ is absorbed into $Ct^{-1}$, and the coefficient
$\mathcal S^2Y$ is controlled on each slab by (1.1)--(1.2): its time
integral is bounded from zero by (1.1), while on positive inner slabs
its pointwise size is at most $C\gamma^3/\tau_k$ and hence contributes
to $L_k$ with the same $t^{-1}$ scale.

Iterating (5.3) gives
\[
 I_k\le I_0^{(3/2)^k}
 \prod_{j=0}^{k-1}
 \bigl(Cp_j^N\mathcal S L_j^{3/2}\bigr)^{(3/2)^{k-1-j}} .
\tag{5.4}
\]
Taking the $p_k$-th root and using
$\sum_{j\ge0}(2/3)^{j+1}=2$ and the analogous convergence of
$\sum j(2/3)^j$ yields
\[
 \limsup_{k\to\infty} I_k^{1/p_k}
 \le C\,I_0^{1/6}\,\mathcal S^{1/3}\,t^{-1/2}.
\tag{5.5}
\]
The exponent $t^{-1/2}$ comes from $L_k^{3/2}$: one power
$t^{-1}$ in $L_k$ would give $t^{-1/3}$, and the additional $3/2$ in
(5.3) changes this to $t^{-1/2}$.  This is precisely the arithmetic that
must not be dropped.

A final standard localization step converts the shrinking-slab integral
bound into the value at the terminal time; applying the estimate on
$[t,t+h]$ and letting $h\downarrow0$, or equivalently using continuity of
$J_{p_k}(s)$ in $s$, gives
\[
 \|aE(t)\|_\infty
 \le C\,I_0^{1/6}\,\mathcal S^{1/3}\,t^{-1/2}.
\tag{5.6}
\]
The large-$p$ limit is
\[
 J_p(t)^{1/p}\to\sup_{\operatorname{supp}a} a|E(t)|,
\tag{5.7}
\]
because $a^{(p-2)/p}\to a$ and $\eta=1$ near $\operatorname{supp}a$.
Thus the transition annulus $0<a<1$ is included; on $a=0$ the product
$aE$ vanishes.

---

## 6. Volume cancellation and velocity estimate

Substitute the seed (4.2) into (5.6):
\[
 \|aE(t)\|_\infty
 \le C\mathcal S^{1/3}t^{-1/2}(t\delta^6V)^{1/6}
 = C\delta\,\mathcal S^{1/3}V^{1/6}t^{-1/3},
\tag{6.1}
\]
where $V=\operatorname{Vol}(U)$.
The selected-support Sobolev estimate gives
\[
 \mathcal S\le Cr^2V^{-1/2},
 \qquad
 \mathcal S^{1/3}V^{1/6}\le Cr^{2/3}.
\tag{6.2}
\]
Therefore
\[
 \boxed{
 \|aE(t)\|_\infty\le C\delta\left({r^2\over t}\right)^{1/3},
 \qquad 0<t\le\theta r^2 .}
\tag{6.3}
\]
The local volume cancels even in collapsing supports.  Finally,
\[
 \int_0^T\|aE(t)\|_\infty\,dt
 \le C\delta r^{2/3}T^{2/3}
 \le C\delta\theta^{2/3}r^2,
 \qquad T\le\theta r^2.
\tag{6.4}
\]
This is the $V$-improvement used by the coupled first-exit bootstrap.

---

## 7. What is preserved from Step 62

The repaired expansion preserves exactly the older mechanism:

1. $J_p=\int\eta^2a^{p-2}|E|^p$ and
   $z_p=\eta a^{(p-1)/2}|E|^{p/2}$ are the active objects.
2. The high-$p$ step uses three factors and the coefficient
   $\mathcal S^2Y$; the direct two-factor route remains only the fixed
   $p=6$ seed.
3. The time-integrated seed is $I_0\le CtJ_6(0)$ and has no Sobolev
   factor.
4. The Moser product keeps $L_k^{3/2}$, giving
   $\mathcal S^{1/3}t^{-1/2}I_0^{1/6}$ before the seed is substituted.
5. The final endpoint is still
   $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$, now with the transition
   region and the time-exponent arithmetic both accounted for.
