# Step 70: Noncollapsed A₁ bubbling flux dichotomy

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

Depends on: Steps 59–63 (rate-limited H4/jet-drift), Step 69 (flux constants
and clean annulus identity), manuscript `20260912.tex` §FND:flux/nonlinearflux/
energyflux (lines 890–1003), Steps 67–68 (operator conventions, reflection,
kernel audit).

## 0. Purpose and scope

This note formulates a precise **dichotomy theorem** for noncollapsed
four-dimensional near-Einstein sequences with A₁ bubbles. It combines the
manuscript's proved clean-annulus flux identities with the Step-63 jet-drift
reachability result. The theorem is:

> For each bubble with a nonzero Weyl mismatch $K$, either the projected
> first Biquard obstruction vanishes (when $\delta_j\log(1/t_j)\to0$),
> or the bubble scale is exponentially small
> $t_j\le\exp(-c/\delta_j)$.

**What is proved** (by the manuscript identities and session computations):
the clean-annulus algebra, sharp flux constants, the log-Weyl operator
identity, the two-jet reachability of the exponential branch, and the
algebraic properties of the spherical model.

**What requires additional bubbling-specific hypotheses** (not yet proved):
harmonic/Bianchi neck coordinates, ambient Einstein tower subtraction,
weighted neck energy control, endpoint matching, TT quadrupole identification,
and finite-node uniform estimates.

The note states both parts explicitly and marks the boundary.

---

## 1. Setting and definitions

Let $(M_j,g_j)$ be a sequence of closed, connected, smooth, oriented
four-manifolds with
$$
\|\operatorname{Ric}_{g_j}-\Lambda g_j\|_{\mathrm{op},\infty}
=\delta_j\to0,
\qquad \Lambda\in\mathbb R\setminus\{0\}.
$$
Assume *noncollapse*: $\operatorname{Vol}(M_j)\ge v>0$.  By Cheeger–Naber
regularity (and the Cheeger–Gromov compactness adapted to bounded Ricci),
a subsequence converges in pointed Gromov–Hausdorff sense to a smooth
Einstein orbifold $(\mathcal O,g_0)$ with $\operatorname{Ric}(g_0)=\Lambda g_0$,
having finitely many isolated ADE singularities $p_1,\dots,p_N$.

At each $p_k$ an ALE Ricci-flat bubble $(B_k,b_k)$ emerges with scale $t_k\to0$.
We restrict to $A_1=\mathbb Z/2$ singularities; the bubble is Eguchi–Hanson.

### Neck region

For each $k$, define the annular neck in orbifold normal coordinates as
$$
A_k=\{b_k<r<R_k\}/\mathbb Z_2,\qquad
L_k=\log(R_k/b_k).
$$
In the standard ALE picture, $b_k\sim t_k^{1/2}$, $R_k\sim t_k^{-1/2+\epsilon}$
for small $\epsilon>0$, so $L_k\sim|\log t_k|$.

### Quadratic normal-coordinate tensors

At $p_k$, the orbifold metric in normal coordinates is
$$
g_0=e+H_0^{(k)}+O(r^4),\qquad
D\operatorname{Ric}_eH_0^{(k)}=\Lambda e.
$$
The inner EH correction (Step 68, verified from the manuscript) supplies
$$
H_1^{(k)}=\sigma H_*,\qquad
D\operatorname{Ric}_eH_1^{(k)}=\Lambda e,
$$
where $H_*$ is the specific quadratic tensor \eqref{FND:Hstar} with
$\mathcal R_+(H_*)=\operatorname{diag}(1/2,1/2,0)$ in the Weyl decomposition.

The **Weyl mismatch** is
$$
K^{(k)}=H_0^{(k)}-H_1^{(k)},
$$
which satisfies $\operatorname{tr}K=\operatorname{div}K=\Delta K=0$,
$K(x,\cdot)=0$; it is a pure Weyl normal-coordinate tensor of the form
$K_{ij}=-\frac13C_{ikjl}x^kx^l$.

$K^{(k)}=0$ if and only if $H_0^{(k)}=H_1^{(k)}$, which means the
orbifold's Weyl curvature at $p_k$ is exactly compatible with the chosen
EH direction. The first Biquard obstruction condition
$R_\pm(p_k)\zeta_k=0$ is equivalent to $K^{(k)}$ lying in a specific
linear subspace.

---

## 2. Clean-annulus flux identity (PROVED)

This is a direct consequence of the manuscript Proposition FND:flux, verified
in Step 69.

**Theorem (Linear flux bound).** Let $A=\{b<r<R\}/\mathbb Z_2$ with
$L=\log(R/b)$. Let $K$ be a nonzero $\mathbb Z_2$-invariant quadratic tensor
with $\operatorname{tr}K=\operatorname{div}K=\Delta K=0$, $K(x,\cdot)=0$.
Set
$$
o=r^{-6}K,\qquad
I_K=\int_{S^3/\mathbb Z_2}|K|_{\mathrm{HS}}^2,\qquad
J_K=\int_{S^3/\mathbb Z_2}\|K\|_*.
$$
If $u$ is smooth on $A$ with $u=0$ near $r=b$ and $u=K$ near $r=R$, then
$$
\int_A\langle D\operatorname{Ric}_eu,o\rangle=-3I_K,
\qquad
\|D\operatorname{Ric}_eu\|_{\mathrm{op},\infty}
\ge\frac{3I_K}{LJ_K}.
$$

**Proof.** The test tensor $o$ is trace-free, divergence-free, harmonic, and
$o(\nu,\cdot)=0$. Integration by parts annihilates all gauge terms in the
true linearized Ricci operator. The boundary pairing uses
$\partial_rK=2K/r$ and $\partial_ro=-4o/r$; only the outer boundary
contributes. Operator/nuclear norm duality gives the lower bound.  ∎

The **spherical model** constant (Step 69, Lean-audited):
$I_K=v_\Gamma/216$, $J_K=v_\Gamma/9$, giving $3I_K/(J_K)=1/8$. Hence
$$
\|D\operatorname{Ric}_eu\|_{\mathrm{op},\infty}\ge\frac{1}{8L}.
$$

---

## 3. Nonlinear and energy extensions (PROVED in manuscript)

**Theorem (Nonlinear flux bound, FND:nonlinearflux).** If $g=e+q$ with
$|q|\le Br^2$, $|Dq|\le Br$, $BR^2\le1/2$, endpoints $e+H_1$ and $e+H_0$,
$K=H_0-H_1$, $D\operatorname{Ric}_eH_i=\Lambda e$, then
$$
\delta_\Lambda(g)\ge
\frac{3I_K-C_K(B^2+B)R^2}{J_K(L+CBR^2)}.
$$

**Theorem (Energy flux bound, FND:energyflux).** With weighted neck energy
$\mathcal E(q)=\int_A r^{-4}|Dq|^2$ and $C^0$ bound $|q|\le\epsilon r^2$:
$$
\delta_\Lambda(g)\ge
\frac{3I_K-C(\epsilon+\mathcal E+R\sqrt{\mathcal E}+R^2)}
{J_KL+CR(\sqrt{\mathcal E}+R)}.
$$

Both are proved in the manuscript by expanding the nonlinear Ricci
operator, integrating against the decaying test tensor $o$, and using
a single integration by parts.

---

## 4. Transfer hypotheses (OPEN)

To apply the flux bounds to an actual bubbling sequence, the following
conditions must be verified on the $j$-th neck $A_k^{(j)}$:

**(T1) Harmonic/Bianchi coordinates.** On $A_k^{(j)}$, the metric $g_j$
is written as $g_j=e+q_j$ in coordinates that are harmonic (or satisfy
a controlled Bianchi gauge) for the background orbifold metric.

**(T2) Ambient tower subtraction.** The orbifold quadratic terms $H_0^{(k)}$
and the leading EH correction are subtracted from $q_j$; the residual $q_j$
in the flux bounds is then the actual mismatch from the model.

**(T3) TT quadrupole identification.** The leading angular component of
$q_j$ on the neck is identified as a nonzero multiple of $K^{(k)}$ plus
controlled higher-order terms; the multipole structure and TT projection
are verified.

**(T4) Weighted energy control.** The weighted Dirichlet energy
$\mathcal E(q_j)=\int_{A_k^{(j)}}r^{-4}|Dq_j|^2$ is uniformly bounded
and converges to zero as $j\to\infty$ (or is bounded by $C\delta_j^\alpha$
for some $\alpha>0$).

**(T5) Endpoint matching.** The inner model (EH scale $t_k$ metric plus
$q_\Lambda$ correction from FND:exactcore) and the outer model (orbifold
metric $g_0+H_0^{(k)}$) agree with $q_j$ at the inner and outer boundaries
to errors $\epsilon_\pm\to0$.

**(T6) Nonlinear error.** The nonlinear Ricci remainder beyond the
quadratic terms in $q$ is controlled by the weighted energy and $C^0$ bounds.

**(T7) Finite-node uniformity.** Constants $C_K$, $C$ in the flux bounds
are uniform over the finitely many bubbles $k=1,\dots,N$.

**(T8) Inner/outer flux identification.** The flux integral computed
from the inner EH model (via $H_*$ and the biaxial core) matches the
flux from the outer orbifold model through the neck, with error controlled
by (T4)–(T6).

**Status of each hypothesis:**

| Hyp. | Status | Source |
|------|--------|--------|
| T1 | Standard: harmonic coordinates exist on noncollapsed Ricci-bounded manifolds (Cheeger–Naber). Detail: quantitative control vs. Bianchi gauge may need Anderson-type estimates. | Literature |
| T2 | The orbifold normal-coordinate expansion is standard. Subtraction is algebraic once T1 is established. | Standard |
| T3 | Requires the bubble's leading far-field to be the quadrupole; this follows from the ALE decay rate $O(\rho^{-4})$ of the EH metric. Detail: TT projection onto the Γ-invariant sector. | EH asymptotics + representation theory |
| T4 | The weighted energy converges if the necks become metrically long and the mismatch is controlled; establishing this from $C^0$ Ricci bounds alone (without full curvature) is the hard part. The CZ spike (Step 11) shows it cannot hold unconditionally without coordinate/gauge conditions. | Open: requires gauge-normalized control |
| T5 | Inner endpoint: the $q_\Lambda$ family (Step 68, verified) gives a smooth inner model matching to $O(a^2+b^2)$. Outer: orbifold convergence gives $O(R^2)$ matching. | Partially proved (inner); standard (outer) |
| T6 | Follows from T4 + T5 via the manuscript's nonlinear expansion. | Conditional on T4, T5 |
| T7 | Finite number of bubbles is automatic from noncollapse + Euler characteristic bound. Uniform constants follow from uniform geometry of the orbifold away from singular points. | Standard |
| T8 | This is the deepest open item. It requires that the physical transition from EH core to orbifold background produces the same leading flux as the algebraic model. The reflection symmetry (Step 68) constrains but does not determine this. | Open |

---

## 5. The dichotomy theorem (conditional on T1–T8)

**Theorem (Noncollapsed A₁ flux dichotomy).**
Assume the setting of §1 with all bubbles of type $A_1$. Assume hypotheses
T1–T8 hold uniformly. Let $K^{(k)}$ be the Weyl mismatch at bubble $p_k$.

Then for each $k$ with $K^{(k)}\ne0$:

**(a)** If $\delta_j\log(1/t_k^{(j)})\to0$, then the projected first
Biquard obstruction vanishes: $R_\pm(p_k)\zeta_k=0$ for the EH direction
$\zeta_k$ chosen to match $H_1^{(k)}$.

**(b)** If the projected first obstruction does NOT vanish (i.e.,
$K^{(k)}\ne0$ is structurally forced by the bubble/orbifold geometry), then
$$
t_k^{(j)}\le\exp\!\left(-\frac{c(K^{(k)})}{\delta_j}\right)
$$
for a constant $c(K^{(k)})>0$ depending only on $K^{(k)}$ and the geometry.

**Proof sketch.**
From §3 (energy flux bound) applied to the $j$-th neck at $p_k$:
$$
\delta_j\ge\frac{3I_{K^{(k)}}-o_j(1)}{J_{K^{(k)}}L_k^{(j)}+o_j(1)},
$$
where $o_j(1)$ collects the T4–T8 error terms which vanish as $j\to\infty$.
Since $L_k^{(j)}\sim|\log t_k^{(j)}|$, rearranging gives
$$
\delta_j\cdot|\log t_k^{(j)}|\ge\frac{3I_{K^{(k)}}}{J_{K^{(k)}}}-o_j(1)
=\frac{1}{8}-o_j(1)>0
$$
for large $j$. In particular $\delta_j|\log t_k^{(j)}|\ge c>0$, i.e.,
$t_k^{(j)}\le\exp(-c/\delta_j)$.

Therefore: either $K^{(k)}=0$ (first obstruction can be killed, and the
flux bound is vacuous), or $t_k^{(j)}$ is exponentially small in $1/\delta_j$.  ∎

**Remark (Branch (b) is realizable).** The Step-63 jet-drift computation
shows that a continuous path of Einstein-compatible two-jets connects any
outer Weyl block to the degenerate set $\{R_\pm\zeta=0\}$, with Ricci defect
$O(\delta)$ at the outer edge and vanishing at the center. The degenerate set
has codimension 1 in $\operatorname{Sym}^2_0(\mathbb R^3)^+\oplus
\operatorname{Sym}^2_0(\mathbb R^3)^-$, so every starting point can reach it.
Therefore the exponential channel is not merely a logical possibility left
open by the proof technique: it is a genuine geometric feature of the
$C^0$-Ricci-pinching problem.

---

## 6. Behavior on the mixed product-quotient rows

On the product orbifold $(S^2(\Lambda)\times S^2(\Lambda))/\mathbb Z_2$,
the curvature at each $A_1$ node satisfies
$$
R_+=R_-=\operatorname{diag}(\Lambda,0,0).
$$
Both $R_+$ and $R_-$ have a two-dimensional kernel. Therefore, for BOTH
compatible and reversed EH directions, a direction $\zeta$ satisfying
$R_\pm(p_k)\zeta_k=0$ always exists. Hence:

**On the mixed rows, $K^{(k)}=0$ is always achievable and the dichotomy
is trivially satisfied.** The flux bound provides no constraint and says
nothing about Einstein existence.

This is consistent with the known facts:
- The $r=0$ row (all compatible) desingularizes to the del Pezzo dP4 KE metric.
- The $r=4$ row (all reversed) also desingularizes (by reflection symmetry,
  Step 68).
- The mixed rows $r=1,2,3$ have first obstruction automatically killed but
  higher obstruction status unknown.

The dichotomy's real content constrains topologies where $R_\pm$ is
generically nondegenerate at some bubble—for instance, $E$-type ADE
singularities where the nontrivial chiral Weyl block has no invariant
component (Steps 46–47), or generic orbifolds away from the special
product structure.

---

## 7. Relation to the full Yau-26 target

This dichotomy is a structural/formalizable result about noncollapsed
bubbling geometry. It does NOT resolve any branch of the Yau-26 proposition:

1. **Not a proof of $P_4^+$**: even if all first obstructions vanish (as
   they do on the mixed rows), this does not produce an Einstein metric.
   Higher obstructions and transversality would be needed.

2. **Not a refutation of $P_4^+$**: the exponential branch provides a
   mechanism for near-pinched sequences to exist without Einstein metrics,
   but constructing an actual closed counterexample requires both a
   near-pinched input (which the log-Weyl construction provides) AND
   an Einstein nonexistence theorem on the underlying manifold (which
   no existing technique delivers for the SW-void mixed rows).

3. **Complements the construction side**: the log-Weyl near-pinched
   construction (FND:A1construction) provides $\delta_\sigma(g_a)=
   O(|\log a|^{-1})$ on fixed resolutions. The dichotomy theorem
   describes the *response* of any such sequence in the noncollapsed
   regime. Together they constrain the problem but leave the Einstein
   existence question open.

## 8. Files

- This note: `workspace/notes/step70_necessity_flux_dichotomy.md`
- Flux constants: `workspace/data/step69_flux_identity_constants.json`
- Step 69 Lean kernel: `workspace/proofs/Step69FluxKernelAlgebra.lean`
- Step 68 q_Λ verification: `workspace/data/step68_qLambda_core_verify.json`
- Step 68 log-Weyl check: `workspace/data/step68_log_weyl_operator_check.json`
- Step 63 jet-drift data: `workspace/data/step63_jet_drift_full.json`
