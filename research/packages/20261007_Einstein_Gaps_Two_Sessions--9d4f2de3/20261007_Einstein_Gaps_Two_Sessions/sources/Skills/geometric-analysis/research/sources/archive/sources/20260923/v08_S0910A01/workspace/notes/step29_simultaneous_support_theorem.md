# Step 29: Simultaneous selected-support flow theorem

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

**STEP 30 REPAIR NOTICE.** The Step 29 theorem note is superseded where it uses ordinary unweighted Moser on \(U=a(\operatorname{Rm}+G)\) or \(|aE|\), where it assumes \(\chi(M)=A+O(1)\) or the numerical limit \(K_0\to9\), and where it treats only exact \(\sigma=0\) as the analytic regime.  The corrected route uses the mixed Hölder--Sobolev weighted recurrence
\[
H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2,
\]
keeps \(U\) for shifted-curvature continuation rather than first Moser bounds, uses only an \(O(A)\) Euler bound plus positive \(\operatorname{Vol}/A\), and treats all sequences with \(\sigma_i/A_i\to0\).  See `workspace/notes/step30_weighted_moser_and_family_repair.md`.

## 0. Purpose

This note assembles the complete bootstrap/first-exit argument on each
selected support, using every verified component from Steps 24–28 and
A03 Steps 26–27.  It shows that the chain of estimates is non-circular
and that all downstream outputs are produced at the same terminal time.

The theorem is conditional on smooth existence for the degenerate flow on
a closed manifold.  The continuation mechanism is A03's shifted-curvature
extension (Step 27 + Codex), adopted below; its Wang-Proposition-4.14
expansion and staggered Hölder exponents are still schematic.

## 1. Setting

**Flow.**  On closed \((M^4,g_0)\), fix cutoff data as in Step 24 §1:

\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

Selected support geometry: \(\Pi\Subset\Omega_\chi\Subset\Omega_\eta\), with
\(\chi\equiv1\) on \(\Pi\), \(\eta\equiv1\) on a neighborhood of
\(\operatorname{supp}\chi\), \(\operatorname{supp}\nabla\eta\subset\{\chi=0\}^\circ\).
Gradient controls: \(|\nabla\chi|\le C_\chi/r\), so \(|\nabla a|^2/a=4|\nabla\chi|^2\le4C_\chi^2/r^2\).

**Sobolev.**  Maheux–Saloff-Coste (A03 Step 26 §4): on any geodesic ball
\(B_R\) with \(\operatorname{Ric}\ge-(n-1)\kappa g\) and \(\kappa R^2\) bounded,

\[
\|u\|_{L^4(B_R)}^2\le S\bigl(\|\nabla u\|_2^2+R^{-2}\|u\|_2^2\bigr),
\qquad S=CR^2/\operatorname{Vol}(B_R)^{1/2}.
\tag{1.1}
\]

No noncollapse needed; volume enters only through explicit \(V^{-1/2}\).

**Initial data (maximal-function selection).**

\[
H_2(0)=\int_{\Omega_\eta}\eta^2F^2\le M\operatorname{Vol}(\Omega_\eta),
\qquad M=1+K_0,
\tag{1.2}
\]

\[
\beta_0=A_\Omega^2\|F(0)\|_{L^2(\Omega_\eta)}\le C(L_\eta)r^2\sqrt{M},
\qquad Q(0)=\int_{\Omega_\eta}\eta^2|E_0|^2\le4\delta^2\operatorname{Vol},
\tag{1.3}
\]

\[
J_6(0)=\int_{\Omega_\eta}\eta^2a^4|E_0|^6\le\delta^6\operatorname{Vol}.
\tag{1.4}
\]

The critical product \(\beta_0\) is independent of collapsed volume (Step 24 eq.
2.3); \(r\) is chosen so that \(C_*\beta_0\) is below the absorption threshold.

## 2. Theorem statement

**Theorem (First-exit bootstrap).** Let \(n=4\).  There exist constants
\(\theta_0,\Lambda>0\), depending only on the support ratios
\(L_{\rm pl},L_\chi,L_\eta\) and the cutoff smoothness \(C_\chi\), such that
if \(C_*\beta_0<\Lambda\) and a smooth solution exists on \([0,T_{\max})\),
then:

**(a)** The solution extends to \([0,T]\) with \(T=\theta_0 r^2\).

**(b)** On \(\operatorname{supp}\chi\times[0,T]\):

\[
e^{-1/10}g_0\le g(t)\le e^{1/10}g_0.
\tag{B1}
\]

**(c)** Sobolev persistence: \(S(t)\le2S(0)\).

**(d)** Curvature energy: \(H_2(t)\le2H_2(0)\), \(\beta(t)\le2\beta_0\).

**(e)** Cubic potential: \(S^2Y(t)\le C\beta_0^3/t\) for \(0<t\le T\).

**(f)** Curvature pointwise (weighted):

\[
\|a\operatorname{Rm}(t)\|_\infty
\le\|aF(t)\|_\infty\le\frac{C\beta_0}{t}.
\tag{B2}
\]

**(g)** Defect energy: \(J_6(t)\le e^{C\theta_0}J_6(0)\le C\delta^6\operatorname{Vol}\).

**(h)** Defect pointwise (weighted):

\[
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\tag{B3}
\]

**(i)** Velocity:

\[
V(T)=\int_0^T\|aE(s)\|_{L^\infty(\operatorname{supp}\chi)}ds
\le\tfrac32C\delta\theta_0^{2/3}r^2.
\tag{B4}
\]

**(j)** Global defect (across disjoint supports):

\[
Q_{\rm global}(T)\le e^{C\theta_0}Q_{\rm global}(0).
\tag{B5}
\]

**(k)** Inner plateau curvature: for \(0<t\le T\),

\[
|\operatorname{Rm}(x,t)|\le C\beta_0/t
\qquad\text{for all }x\in\Pi.
\tag{B6}
\]

## 3. Bootstrap architecture (proof)

Define a first-exit time

\[
T^*=\sup\{t\in(0,T_{\max}):\text{(B1)--(B4) hold with doubled constants}\}.
\]

We show that on \([0,T^*]\), the actual estimates are **strictly better** than
the bootstrap hypotheses, forcing \(T^*\ge\theta_0 r^2\) for small \(\theta_0\).

### Step A: H₂ persistence

**Input:** Bootstrap metric comparison \(\frac12g_0\le g\le2g_0\), evolved Sobolev.

**Estimate:** From Step 25 eq. (2.19):

\[
H_2'+cD_2\le C\int\eta^2aF^3+Cr^{-2}H_2+C_0,
\qquad c=2-\delta_0>0.
\]

The cubic reaction \(\int\eta^2aF^3\) is absorbed on the same support (Step 24
eq. 4.1): because \(\eta=1\) on \(\operatorname{supp}a\),

\[
\int\eta^2aF^3\le\beta_a(t)(D_2+Cr^{-2}H_2),
\qquad \beta_a(t)=A_\Omega^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}.
\]

For \(C\beta_a<c/4\) (bootstrap ensures \(\beta_a\le4\beta_0\)):

\[
H_2'+(c/2)D_2\le C_1r^{-2}H_2.
\]

Gronwall: \(H_2(t)\le e^{C_1\theta_0}H_2(0)<2H_2(0)\) for small \(\theta_0\).
Integrated dissipation: \(\int_0^TD_2\le CH_2(0)\).

**Output:** (d) with strict improvement. \(\beta(t)\le e^{C\theta_0/2}\beta_0<2\beta_0\).

### Step B: Cubic potential (q=3)

**Input:** \(H_2\) persistence, \(\beta(t)<2\beta_0\), evolved Sobolev.

**Estimate:** From Step 25 eq. (5.1)–(5.2) and Step 24 eq. (6.1)–(6.6):

\[
Y'+(c/2)D_3\le Cr^{-2}Y,
\qquad D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2,
\]

after absorbing \(I_4=\int a^2F^4\) with \(u=aF^{3/2}\) (the correct q=3
variable, Step 24 repair):

\[
I_4\le\beta_a(D_3+r^{-2}Y).
\]

Gronwall: \(Y(t)\le e^{C\theta_0}Y(0)\).

Time-averaging (Step 24 eq. 6.5–6.6): from \(A_\Omega^4\int_0^T\int aF^3\le
C\beta_0^3\) and forward propagation:

\[
S^2Y(t)\le C\beta_0^3/t,\qquad 0<t\le T.
\]

**Output:** (e).

### Step C: Curvature pointwise (weighted mixed Hölder--Sobolev Moser; Step 30 repair)

**Input:** \(S^2Y(t)\le C\beta_0^3/t\), evolved metric/Sobolev, and the tensor power inequality for \(H_p(F)=\int a^{p-2}F^p\) with polynomial \(p\)-loss.

Step 29's ordinary unweighted-\(U\) replacement is withdrawn.  Testing the \(U\)-equation still gives only \(\int a|\nabla(|U|^{p/2})|^2\), and the shifted quadratic reaction is \(U*U\), not \(aU*U\).  Thus \(U\) is retained for continuation, not for producing the first curvature bound.

The repaired iteration keeps
\[
z_p=a^{(p-1)/2}F^{p/2}.
\]
Although \(\|z_p\|_3^3\) has a half-power gap relative to \(H_{3p/2}\), the correct time-slice estimate is
\[
H_{3p/2}=\int(a^{p-2}F^p)^{1/2}z_p^2
\le H_p^{1/2}\|z_p\|_4^2.
\]
Sobolev gives
\[
\|z_p\|_4^2\le C p^N S(D_p+r^{-2}H_p),
\]
and the time-cutoff energy inequality then yields the recurrence
\[
\int_{\tau_{k+1}}^tH_{3p_k/2}
\le C p_k^N S\left(L_k\int_{\tau_k}^tH_{p_k}\right)^{3/2},
\qquad L_k=Cp_k^N4^k(t^{-1}+r^{-2}).
\]
The usual product over \(p_k=(3/2)^kp_0\) has finite polynomial loss and gives the intended endpoint
\[
\|aF(t)\|_\infty\le C\beta_0/t,
\]
provided the tensor power inequality and q=3 potential estimate are established on the same supports.  This is now a repaired route rather than a completed theorem.  See `step30_weighted_moser_and_family_repair.md`.

**Output sought:** (f) and (k) (set \(a=1\) on the inner plateau) after the missing tensor-power theorem is fully proved.

### Step D: Defect energy persistence

**Input:** \(\|aF(t)\|_\infty\le C\beta_0/t\) (curvature potential), evolved
metric/Sobolev.

**Fixed-exponent \(p=6\) estimate** (Step 26):
\[
J_6=\int\eta^2\chi^8|E|^6,\qquad Z_6=\int\eta^2\chi^{10}|E|^4|\nabla E|^2.
\]

The power-energy inequality for \(f=|E|_\varepsilon=(|E|^2+\varepsilon)^{1/2}\),
weight \(a^{p-2}=a^4=\chi^8\), has curvature potential
\(\int a^5F|E|^6=\int F\cdot z_6^2\) with \(z_6=\chi^5|E|^3\).

Absorb using \(\beta_a\) (same mechanism):
\[
\int Fz_6^2\le\beta_a(Z_6+Cr^{-2}J_6).
\]

Gronwall gives \(J_6(t)\le e^{C\theta_0}J_6(0)\le C\delta^6\operatorname{Vol}\).

**Kato regularization** (A03 Step 26 §6): regularize \(|E|_\varepsilon\),
derive the inequality for every \(\varepsilon>0\), take the limit by dominated
convergence and weak lower semicontinuity.

**Output:** (g).

### Step E: Defect pointwise (weighted mixed Hölder--Sobolev Moser; Step 30 repair)

**Input:** \(J_6(t)\le C\delta^6\operatorname{Vol}\), the same q=3 curvature potential control, evolved metric/Sobolev, and the tensor power inequality for the regularized defect \(f=|E|_\varepsilon\).

The unweighted ordinary Moser statement for \(|aE|\) is withdrawn for the same reason as the unweighted \(U\) shortcut: the principal operator remains \(a\Delta\), so the energy supplies only weighted dissipation.

Use the weighted moments
\[
K_p(E)=\int a^{p-2}|E|^p,
\qquad z_p=a^{(p-1)/2}|E|^{p/2},
\]
with seed \(p_0=6\):
\[
K_6(E)=\int a^4|E|^6=J_6\le C\delta^6V.
\]
The Step 30 interpolation
\[
K_{3p/2}(E)\le K_p(E)^{1/2}K_{2p}(E)^{1/2},
\qquad K_{2p}(E)=\|z_p\|_4^4,
\]
together with \(\|\nabla z_p\|_2^2\le Cp^N(Z_p+r^{-2}K_p)\) gives the same time-cutoff recurrence as the curvature case.  The exponent sums are \(n/(2p_0)=1/3\) for the Sobolev factor and \((1+n/2)/p_0=1/2\) for time, so
\[
\|aE(t)\|_\infty\le C\cdot S^{1/3}\cdot t^{-1/2}\cdot
(\delta^6Vt)^{1/6}
= C\delta(r^2/t)^{1/3},
\]
provided the regularized tensor defect power inequality and fixed \(J_6\) persistence are proved on the same support.  The endpoint is unchanged; the mechanism is weighted, not ordinary unweighted Moser.

**Output sought:** (h) after the defect power theorem is fully proved.

### Step F: Velocity and metric comparison

**Input:** Weighted defect pointwise (h).

\[
V(T)=\int_0^{\theta_0r^2}C\delta(r^2/s)^{1/3}ds
=\frac{3C}{2}\delta\theta_0^{2/3}r^2.
\tag{F.1}
\]

For \(\delta\) small enough (in terms of \(\theta_0\)):
\[
V(T)<1/20.
\]

Then \(e^{-2V(T)}g_0\le g(t)\le e^{2V(T)}g_0\) gives

\[
e^{-1/10}g_0\le g(t)\le e^{1/10}g_0,
\]

strictly better than the bootstrap hypothesis (B1) with doubled constant.

**Sobolev persistence:** From metric comparison, Sobolev constants change by
bounded factors, giving \(S(t)\le2S(0)\) under (B1).

**Output:** (b), (c) with strict improvement.  **Bootstrap closes.**

### Step G: Global defect

**Input:** Per-support defect Gronwall \(Q_j(t)\le e^{C\theta_0}Q_j(0)\) from
the triangular estimate (Step 25 eq. 3.6), disjoint supports with stationary
collar (Step 25 eq. 4.1):

\[
Q_{\rm global}(T)=\sum_j Q_j(T)+\sum_{\rm frozen}Q_j(0)
\le e^{C\theta_0}Q_{\rm global}(0).
\]

**Output:** (j).

## 4. Smooth existence: shifted-curvature continuation

The bootstrap assumes the flow exists on \([0,T_{\max})\).  **Short-time
existence** for the degenerate equation on closed \(M^4\) follows from Yang
§8: the DeTurck gauge transports \(\chi^2\) as \((\chi\circ\phi^{-1})^2\)
and pulls back to the fixed spatial coefficient; the zeroth-order
\(-2\widehat a\,\widehat g\) does not change the principal symbol.

**Continuation to \(T_{\max}=\theta_0r^2\)** uses A03's shifted-curvature
framework (Step 27 + Codex):

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad
U=aT.
\]

Key identities: \(\operatorname{Ric}(T)=E\),
\(\operatorname{Ric}(U)=aE\), \(\nabla G=0\).

The weighted equation for \(U\) has Wang's highest-order structure:

\[
(\partial_t-a\Delta)U=(\nabla a)*\nabla U+(\nabla^2a)*U+U*U+a\,G*U+	ext{cutoff commutators}.
\]

The important Step 30 correction is the weight of the quadratic term: if the shifted \(T\)-equation contains \(aT*T\), then multiplying by \(a\) gives \(U*U\), not \(aU*U\).  This equation is a continuation structure once \(\sup|a\operatorname{Rm}|\) is available; it is not an ordinary parabolic Moser source for that first bound.

The bootstrap curvature bound (B2) gives
\(\sup_{[0,T^*)}|U|<\infty\).  Wang's Theorem 4.1 derivative induction:
joint \((\nabla^mU,\nabla^{m+1}\chi)\) loop, with the four raw high terms
handled by grouped integration by parts.  The \(G\)-linear terms have lower
\(U\)-derivative order and create no backward edge.  All
\(\nabla^m(a\operatorname{Rm})\) are therefore uniformly bounded, giving
smooth convergence and restart at each time.

**Remaining for a full proof:** Wang Proposition 4.14 grouped IBP and
staggered Hölder at each induction level should be expanded explicitly rather
than cited from the scalar case.

## 5. Multi-support assembly and plateau fraction

**Disjoint selected supports.**  The maximal-function good set
\[
G_i=\{p\in M_i:\mathcal M_{R_0}(|\operatorname{Rm}|^2)(p)\le K_0\}
\]
satisfies \(\operatorname{Vol}(G_i)\ge\operatorname{Vol}(M_i)/2\) for
\(K_0\) chosen from the Chern–Gauss–Bonnet mean.  A maximal \(r\)-net in
\(G_i\), followed by Bishop–Gromov thinning and bounded-degree coloring
(Step 24 §1), produces a family of \(\ge N_i\) selected supports with
pairwise disjoint \(\Omega_\eta\)-regions.  Each support's plateau \(\Pi_j\)
has

\[
\operatorname{Vol}(\Pi_j)\ge c_{\rm pl}\operatorname{Vol}(\Omega_{\eta,j})
\ge c_{\rm BG}\operatorname{Vol}(B_r(p_j)),
\]

and the total plateau volume satisfies

\[
\sum_j\operatorname{Vol}(\Pi_j)
\ge\alpha\operatorname{Vol}(G_i)
\ge\frac\alpha2\operatorname{Vol}(M_i),
\]

where \(\alpha>0\) depends on the support ratios, coloring degree, and
Bishop–Gromov comparison constants.  Since
\(\operatorname{Vol}(M_i)/A_i=O(1)\) in the near-critical regime (Step 4
volume estimate),

\[
\sum_j\operatorname{Vol}_{g_i(T)}(\Pi_j)\ge\alpha'A_i
\]

for a fixed \(\alpha'>0\), where the terminal volume uses the metric comparison
\(e^{-1/10}g_0\le g(T)\le e^{1/10}g_0\).

On each \(\Pi_j\), the plateau curvature bound (B6) at \(t=T=\theta_0r^2\)
gives \(|\operatorname{Rm}|\le C/\theta_0=:K_{\rm pl}\).  Thus the
plateaux carry uniform bounded curvature with definite combined volume
fraction.

## 6. Dependency graph

The bootstrap chain is **strictly triangular** (each step uses only the
output of earlier steps plus the bootstrap hypothesis):

```
Bootstrap(B1–B4) assumed
  |
  v
(A) H₂ persistence [uses B1+Sobolev, produces β]
  |
  v
(B) S²Y ≤ Cβ³/t [uses A+Sobolev, produces cubic decay]
  |
  v
(C) ||aF||∞ ≤ Cβ/t [uses B+Sobolev (Moser), produces curvature bound]
  |
  v
(D) J₆ persistence [uses C as potential, produces defect energy]
  |
  v
(E) ||aE||∞ ≤ Cδ(r²/t)^{1/3} [uses D+Sobolev (Moser), produces velocity]
  |
  v
(F) V(T) < 1/20 [uses E, recovers B1]  ← CLOSES BOOTSTRAP
  |
  v
(G) Q_global ≤ e^{Cθ}Q_global(0) [uses per-support Q + stationarity]
```

No circular dependency.  The only external input is smooth short-time
existence (Yang §8) and smooth continuation (A03/Codex shifted curvature,
this note §4).

## 7. What this theorem produces for the LeBrun sequence

Applied to the near-critical sequence
\(M_i=X_i\#k_i\overline{\mathbb{CP}}^{\,2}\) with \(k_i/A_i\to1/3\) and
\(\delta_i\to0\):

1. Terminal global defect: \(Q_{\rm global}(T)/A_i\le Ce^{C\theta}\delta_i^2\to0\).
2. Terminal plateau family: \(\sum_j\operatorname{Vol}(\Pi_{i,j})\ge\alpha'A_i\),
   \(|\sec_{g_i(T)}|\le K_{\rm pl}\) on radius-\(\rho\) buffers.
3. Terminal recalibration (Step 28): the mixed SW/CGB/eigenvalue deficit is
   \(\int\mathfrak D_i\le119Q_i(T)=o(A_i)\).
4. Exponential pullback selection (Step 16/28): a center \(p_i\in\Pi_i\) with
   pulled-back mean \(\mathfrak D_i\to0\).
5. Harmonic-coordinate compactness on the tangent-space domain: Rauch
   noncollapse + bounded curvature + shrinking radius.
6. Smooth Einstein limit: \(\operatorname{Ric}=-g\), \(|W^+|^2=1/24\),
   \(\operatorname{spec}(W^+)=(-1/6,1/12,1/12)\).
7. Derdziński contradiction: locally conformally Kähler but Kähler–Einstein
   gives \(|W^+|^2=2/3\ne1/24\).

**Conclusion (conditional):** No sequence of LeBrun/Ishida–LeBrun manifolds
with \(k_i/A_i\to1/3\) can carry metrics with \(\delta_i\to0\).  Combined
with the mixed SW estimate (which forces \(k/A\to1/3\) for any candidate
countersequence), this gives a positive \(\delta_0>0\) such that every metric
on every such manifold has \(\|g^{-1}\operatorname{Ric}+I\|_\infty\ge\delta_0\),
conditional on the proof of §4.

## 8. What remains genuinely conditional

**Within the restricted negative route:**

| Component | Status | Reference |
|-----------|--------|-----------|
| q=2 energy (H₂) | Schematically derived + verified | Step 25 eq 2.19, Codex |
| q=3 cubic (Y) | Same mechanism, different test | Step 24 §6, Step 25 §5 |
| Weighted mixed Moser | Step 30 repair: direct \(\|z_p\|_3^3\) comparison has an \(a^{1/2}\) gap, but the actual recurrence uses \(H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2\) and weighted dissipation | Step 30 note; A03 Step 31 |
| Shifted curvature \(U\) | Useful for velocity/connection and continuation after \(\sup|a\operatorname{Rm}|\); ordinary unweighted Moser on \(|U|,|aE|\) is withdrawn | Step 30 note |
| General-p tensor ineq. | Derived with polynomial growth | A03 Step 26 §§3–6 |
| J₆ persistence | Fixed-exponent critical absorption | Step 26, script passed |
| Kato regularization | Described, not formalized | A03 Step 26 §6 |
| Shifted-curvature continuation | Codex report + scripts pass | A03 Codex, A03 Step 27 |
| Wang 4.14 grouped IBP | Schematic transfer, not expanded | This note §4 |
| Terminal recalibration | Explicit constants verified | Step 28, script passed |
| Pullback selection | Fixed-volume centers + Rauch | Step 28 §§4–5 |
| Derdziński contradiction | Read from primary source | Step 8 |

**Outside the restricted route:**

- Arbitrary four-dimensional topologies (non-LeBrun)
- Positive branch (\(\sigma=+1\))
- Dimensions \(n\ge5\)
- Full Yau 26 interval proposition
- Lean 4 formalization
- Independent kernel verification

## 9. Sources

- Step 24: `workspace/notes/step24_buffered_support_energy_test.md`
- Step 25: `workspace/notes/step25_tensor_energy_derivation.md`
- Step 26: `workspace/notes/step26_weighted_velocity_and_local_flow.md`
- Step 27: `workspace/notes/step27_unified_weak_moser_iteration.md`
- Step 28: `workspace/notes/step28_terminal_recalibration_pullback.md`
- A03 general-p: `Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md`
- A03 continuation: `Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md`
- A03 Codex report: `Sessions/S0910A03/workspace/codex_loop/Research_Report.md`
- Verification scripts: `step27_three_factor_absorption.py`, `step28_moser_recurrence_verify.py`,
  `step28_terminal_pullback_constants.py`
