# Step 41: Corrected restricted negative defect gap theorem

> **Step 45 consolidation.** This note is superseded by `workspace/notes/step45_consolidated_IL_negative_gap_proof.md`, which presents the proof around the quantitative local Φ lower bound mechanism (Proposition 3.2), with all TTCS corrections incorporated: elliptic upgrade via |E|² → 0 in harmonic coordinates, Liouville constant tracking, and coefficient-regularization completeness caveat.  Use the consolidated note as the reference proof.
>

> **Step 42 repair.** The statement and two analytic interfaces below are superseded by `workspace/notes/step42_uniform_gap_weight_terminal_repairs.md`.  The intended result is a family-uniform gap over the permitted Ishida--LeBrun geography, not a topology-dependent number.  The correct Chern--Weil identity is `I-J=2A/3-q`, with averaged deficit `D_av=J-q-(2/3)Σ(E_j^+)²`.
>
> **Step 43--44 update.** The coefficient-weight structure and per-datum flow platform are now usable only in the corrected Step 44 sense.  H-WU is supplied by A01 Step 43 together with A03 Step 45's coordinate-time ledger: all `C_{m+2}` sources carry `χ`, and `C_{m+1}` is the current partner of `U_m`, closing by a same-exponent coupled energy rather than by a previous layer.  H-DT is supplied by coefficient regularization: first construct a common-time smooth limit of `b_ε=χ²+ε²` flows solving the exact `a=χ²` equation, and only then use stationary collars, frozen complement, disjoint support summation, and global `Q`.  See `workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md`.

Session: S0910A01.  Agent2 / Constructor.  Phase: Execute.

This note addresses every interface repair identified in
`step40_preceptor_review_step39_interfaces.md`.  The theorem statement,
support construction, K₂ propagation, structural equations, zero-order
unweighted T lemma, topology/sign assumptions, and terminal passage are
all corrected.  New derivations appear in §3, §5, and §6.

---

## 0. Theorem statement

**Theorem 1.1 (intended family-uniform restricted negative gap).**
*Let*
\[
M=(\#_{j=1}^mX_j)\#N,\qquad m\in\{2,3\},
\]
*where each \(X_j\) is a minimal complex surface of general type, \(N\) is
closed oriented with \(b_+(N)=0\), and the connected sum carries the
Ishida--LeBrun monopole family.  Set*
\[
A=\sum_jc_1^2(X_j)>0,
\qquad
D=4m-(2\chi+3\tau)(N),
\qquad
q=D-{A\over3}.
\]
*In the above-critical no-Einstein range \(q\ge0\), the intended conclusion is
that there is a constant \(\varepsilon_{\rm IL}>0\), independent of
\(A,D,q,N\) and of the input metric, such that no such manifold carries a
smooth metric satisfying*
\[
  \|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}
  <\varepsilon_{\rm IL}.
\tag{0.1}
\]

**Current status of this theorem statement.**  The proof below has to be read
with the Step 42--44 repairs.  The weighted all-order equation now uses A03
Step 45's current-pair estimate for \((U_m,C_{m+1})\), not the older previous-
layer wording.  The flow is obtained by coefficient regularization and smooth
limit before exact-flow localization is used.  The terminal density is \(\Phi\)
from §7.2 below, which includes \(|E|^2\).  A topology-dependent
\(\varepsilon_4(A,k)\) is not the mathematical target of this route.

**Scope.**  This is a restricted four-dimensional negative-sign result for the
Ishida--LeBrun geography.  It does not settle the positive branch, arbitrary
four-manifold topology, dimensions \(n\ge5\), or the Lean formalization required
by the full Yau Problem 26.

---

## 1. Near-critical calibration (preserved)

By contradiction for the family-uniform statement.  Suppose there is a
sequence \((M_i,g_i)\) in the permitted Ishida--LeBrun geography with
\(\|E_i\|_\infty=\delta_i\to0\), \(q_i\ge0\), and no Einstein metric on any
\(M_i\).  Do **not** assume \(A_i\to\infty\) at the outset; after the mixed
estimate forces \(q_i/A_i\to0\), split into the unbounded-\(A_i\) case and the
bounded-\(A_i\) case.  If \(A_i\) is bounded, integrality gives \(q_i=0\)
eventually, and the same terminal averaging argument applies with
\(A_i=A_0>0\).

**Monopole classes.** Each manifold in the Ishida–LeBrun family carries the
full sign family of monopole classes
\(\kappa_\varepsilon=\sum_j c_1(X_{j,i})+\sum_\ell\varepsilon_\ell E_\ell\),
\(\varepsilon_\ell=\pm1\), in the notation of the chosen connected-sum
presentation.
The mixed Seiberg–Witten inequality (LeBrun) for each class gives
\[
  I_i:=\frac1{4\pi^2}\int\!\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
  \ge\frac23(\kappa_\varepsilon^+)^2.
\tag{1.1}
\]
Averaging over all \(2^{k_i}\) sign choices:
\[
  I_i\ge\frac23\!\left[A_i+\sum_j(E_j^+)^2\right].
\tag{1.2}
\]
**Chern–Gauss–Bonnet and \(q\ge0\).** With
\(J_i=\frac1{4\pi^2}\int\frac{|\mathring{\operatorname{Ric}}|^2}{2}\),
the topology gives
\[
  I_i-J_i=(2\chi+3\tau)(M_i)={2A_i\over3}-q_i.
\tag{1.3a}
\]
Hence the averaged deficit is
\[
  D_i:=I_i-{2\over3}A_i-{2\over3}\sum_\ell(e_\ell^+)^2\ge0,
  \qquad D_i=J_i-q_i-{2\over3}\sum_\ell(e_\ell^+)^2.
\tag{1.3}
\]
There is no additional \(A_i\)-term in this formula.  Because
\(J_i/A_i\to0\) under \(\delta_i\to0\) and calibrated volume, we obtain
\(q_i/A_i\to0\), \(\sum_\ell(e_\ell^+)^2/A_i\to0\), and \(D_i/A_i\to0\).

**Calibrated profile.** The completion-of-squares identity
(Steps 5–8) gives
\[
  \int(s+8\sqrt6\,|W^+|)^2\le864\pi^2D_i,
\tag{1.4}
\]
and the substitution gap
\[
  \int G_i\le48\pi^2D_i,
  \qquad G_i=f^2-(a_{*-})^2\ge0,
\tag{1.5}
\]
with \(f=\frac23s-2\sqrt{\frac23}|W^+|\),
\(a_*=\frac23s+2w\), \(w\) being the smallest \(W^+\)-eigenvalue.

Hence in normalized mean (\(\cdot/A\)):
\[
  s\to-4,\quad|W^+|^2\to\frac1{24},\quad
  \operatorname{spec}(W^+)\to\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{1.6}
\]
**Volume ratio.** The calibrated density gives
\[
  \frac{\operatorname{Vol}(g_i)}{A_i}\to\frac{32\pi^2}{9}.
\tag{1.7}
\]

---

## 2. Support construction (corrected)

**Lemma 2.1 (collapse-sensitive support selection).**
*There exist universal constants \(\alpha_0>0\), \(r_0>0\), \(K_0>0\),
\(N_0\in\mathbb N\), and for each \(i\) sufficiently large a finite
family of smooth cutoffs
\(\{\chi_{\alpha,i}\}_{\alpha\in\mathcal A_i}\),
\(\chi_\alpha:M_i\to[0,1]\), such that:*

*(a) \(|d\chi_\alpha|\le C/r\) everywhere, where \(r\in(0,r_0]\) is a
fixed radius independent of \(i\).*

*(b) Each \(\chi_\alpha\) equals \(1\) on \(B_{5r}(x_\alpha)\) and is
supported in \(B_{6r}(x_\alpha)\).  An auxiliary cutoff \(\eta_\alpha\)
equals \(1\) on \(B_{6r}(x_\alpha)\) and is supported in \(B_{7r}(x_\alpha)\),
so \(a=0\) on \(\operatorname{supp}d\eta_\alpha\).  The centers \(x_\alpha\)
form an \(r\)-separated net in the good set.*

*(c) The outer buffered domains \(B_{7r}(x_\alpha)\) are pairwise
disjoint.  Hence the global cutoff
\(a_i=\sum_\alpha\chi_\alpha^2\) satisfies \(0\le a_i\le1\).*

*(d) The inner plateaux \(\bigcup_\alpha B_{5r}(x_\alpha)\) carry
total volume \(\ge\alpha_0A_i\) (using (1.7)).*

*(e) On each support, the initial energy satisfies
\(r^4\fint_{B_{7r}(x_\alpha)}|\operatorname{Rm}_{g_i}|^2\le\widetilde\gamma^2\),
where \(\widetilde\gamma\) is chosen below the absorption threshold by a fixed
dimensional factor.*

*(f) Higher cutoff jets \(\nabla^m\chi_\alpha\) are finite for each
smooth datum, with no sequence-uniform bound on \(m\ge2\) asserted.*

**Proof.**

**Step 1 (volume-average maximal function).**
Set \(R_0\) with \(7r\le R_0\).  Define
\[
  \mathcal M_{R_0}f(x)=\sup_{0<s\le R_0}\fint_{B_s(x)}f.
\tag{2.1}
\]
Under \(\operatorname{Ric}\ge-2g\), the weak-type maximal inequality
(Bishop–Gromov comparison) gives: for any \(\lambda>0\),
\[
  \operatorname{Vol}\{x:\mathcal M_{R_0}(|\operatorname{Rm}|^2)(x)
  >\lambda\}
  \le\frac{C(R_0)}{\lambda}\int_M|\operatorname{Rm}|^2\,d\mu.
\tag{2.2}
\]
Choose \(\lambda=\widetilde\gamma^2/r^4\), with
\(\widetilde\gamma\) fixed below the absorption scale by a dimensional factor,
and use \(\int|\operatorname{Rm}|^2\le C_0A_i\) (Chern--Weil bound):
\[
  \operatorname{Vol}(\text{bad set})
  \le\frac{C r^4}{\widetilde\gamma^2}A_i.
\tag{2.3}
\]
After fixing \(\widetilde\gamma\), choose \(r\) so
\(Cr^4/\widetilde\gamma^2<16\pi^2/9\).  Then, for \(i\) large,
\[
  \operatorname{Vol}(\text{good set})
  \ge\operatorname{Vol}(M_i)-\frac{C r^4}{\widetilde\gamma^2}A_i
  \ge\left(\frac{32\pi^2}{9}-\frac{C r^4}{\widetilde\gamma^2}\right)A_i
  \ge\alpha_0A_i,
\tag{2.4}
\]
using the calibrated volume (1.7).

**Step 2 (center separation and coloring).**
Choose a maximal \(r\)-separated subset \(\{x_\alpha\}\) of the good set.
By maximality, the good set is covered by \(\bigcup_\alpha B_r(x_\alpha)\).
A standard Vitali-type argument with Bishop–Gromov packing gives
\(|\mathcal A_i|\le C(r)A_i\), but the number can be large.

To make the \(B_{7r}\) domains disjoint, we apply \(14r\)-separated
coloring: partition \(\{x_\alpha\}\) into \(N_0\le C(n,r)\) color
classes, each \(14r\)-separated.  At least one color class carries
volume \(\ge\alpha_0A_i/N_0\), and the \(B_{7r}\) balls for that class
are pairwise disjoint.  Relabel this class as \(\mathcal A_i\); then (c)
and (d) hold after adjusting \(\alpha_0\).

**Step 3 (smooth gradient-controlled cutoffs).**
For each \(x_\alpha\), choose distance cutoffs with strict buffers:
\(\chi_\alpha=1\) on \(B_{5r}\), \(\operatorname{supp}\chi_\alpha\subset B_{6r}\),
\(\eta_\alpha=1\) on \(B_{6r}\), and \(\operatorname{supp}\eta_\alpha\subset B_{7r}\),
with \(|d\chi_\alpha|+|d\eta_\alpha|\le C/r\).

Because \(d_{g_i}\) is only Lipschitz, \(\chi_\alpha\) is Lipschitz with
the stated gradient bound.  For full smoothness, mollify at a scale
\(\ll r\) while preserving (a), (b), and the plateau and support
inclusions.  The higher jets \(\nabla^m\chi_\alpha\) depend on the
individual smooth metric \(g_i\); no sequence-uniform bound on
\(\|\nabla^2\chi_\alpha\|\) is asserted.

**Step 4 (global cutoff and single flow).**
The global weight \(a_i=\sum_\alpha\chi_\alpha^2\) satisfies
\(0\le a_i\le1\) by disjointness.  On the buffer
\(\operatorname{supp}(\nabla\chi_\alpha)\subset B_{7r}\setminus
B_{5r}\), the function \(a_i\) and all its derivatives equal those of
\(\chi_\alpha^2\).  On the complement \(M_i\setminus
\bigcup_\alpha B_{7r}(x_\alpha)\), \(a_i=0\) and the metric is
stationary under the flow \(\partial_tg=-2a_i(\operatorname{Ric}+g)\).

**Step 5 (initial energy on each support).**
Because \(x_\alpha\) lies in the good set and \(7r\le R_0\), the
maximal-function threshold directly gives
\[
  r^4\fint_{B_{7r}(x_\alpha)}|\operatorname{Rm}|^2
  \le \widetilde\gamma^2 .
\tag{2.5}
\]
If the downstream smoothing input requires an unnormalized bound
\(\int_{B_{7r}}|\operatorname{Rm}|^2\le\gamma_{\rm abs}^2\), choose
\(\widetilde\gamma\) smaller than \(\gamma_{\rm abs}\) by a fixed dimensional
factor using the Bishop–Gromov upper volume ratio
\(\operatorname{Vol}B_{7r}/r^4\le C(4,r_0)\).  Shrinking \(r\) alone would not
supply this in dimension four because this ratio has a positive Euclidean
limit.  No local noncollapse is assumed.  \(\square\)

---

## 3. Zero-order unweighted \(T\in L^p\) lemma (new)

Set \(T=\operatorname{Rm}+G\), \(U=aT\), \(E=\operatorname{Ric}(T)\),
\(G=g\owedge g/(2(n-1))\).  Recall \(\nabla G=0\) and \(\Delta G=0\).

**Lemma 3.1 (unweighted \(T\in L^p\) propagation).**
*Under a smooth solution of \(\partial_tg=-2aE\) on \([0,T_*)\),
if \(|U(t)|\le K\) on \([\tau,T_*)\) for some \(\tau>0\) and
\(K<\infty\), then for every \(p\ge2\):*
\[
  \frac{d}{dt}\int|T|^p\,d\mu
  +c_p\int a|\nabla|T|^{p/2}|^2\,d\mu
  \le C_p(K+1+r^{-2})\int|T|^p\,d\mu+C'_p(K),
\tag{3.1}
\]
*where \(C'_p(K)\) depends on \(K\), \(p\), \(\operatorname{Vol}\),
and bounded metric data.  In particular,*
\[
  \|T(t)\|_p^p
  \le e^{C_p(K+1+r^{-2})(t-\tau)}
  \bigl[\|T(\tau)\|_p^p+C'_p(K)(t-\tau)\bigr]
  <\infty
\tag{3.2}
\]
*for all \(t\in[\tau,T_*)\).*

**Proof.**

**Step A: volume form.**
\(\partial_t(d\mu)=-a\tau\,d\mu\), where \(\tau=\operatorname{tr}E=s+4\).
Since \(|a\tau|\le n|aE|\le n|U|+na|G|\le nK+Cna\), the volume density
is bounded.  Contribution to \(\frac{d}{dt}\int|T|^p\):
\[
  -\int a\tau|T|^p\,d\mu
  \le (nK+Cn)\int|T|^p.
\tag{3.3}
\]

**Step B: evolution of \(T\).**
From the standard formulas:
\[
  \partial_tT
  =a\Delta T+a\,\mathcal Q(T,G)
  +\nabla a\star\nabla T
  +(\nabla^2a)\star E
  +\mathcal N(a,T,G),
\tag{3.4}
\]
where:

- \(\mathcal Q(T,G)\) collects the Hamilton quadratic
  \(Q(\operatorname{Rm})=Q(T-G)\) and is bounded
  \(|Q(T-G)|\le C|T-G|^2\le C(|T|^2+1)\);

- \(\nabla a\star\nabla T\) is the gradient-cutoff
  (8 terms from §2.2 of Step 35), with
  \(|\nabla a\star\nabla T|\le C|\nabla a||\nabla T|\);

- \((\nabla^2a)\star E\) is the Hessian-cutoff (equation (2.7)
  of Step 35), with the signed IBP mechanism;

- \(\mathcal N(a,T,G)\) collects the normalization
  \(-2a\operatorname{Rm}=-2a(T-G)\) and the G-evolution
  \(\partial_tG=-2a(E\owedge g)/(n-1)\):
  \[
    \mathcal N=-2a(T-G)-\frac{2a}{n-1}(E\owedge g).
  \tag{3.5}
  \]
  Since \(|E|=|\operatorname{Ric}(T)|\le C|T|\) and \(|G|\le C\),
  each term in \(\mathcal N\) satisfies
  \(|\mathcal N|\le Ca|T|+Ca\).

**Stationarity at \(E=0\).**  When \(E=0\)
(i.e.\ \(\operatorname{Ric}=-g\)), the flow velocity is zero, so
\(\partial_tg=0\), \(\partial_t\Gamma=0\), \(\partial_tT=0\).
The point relevant to the
lemma is not algebraic homogeneity at \(E=0\) but the bound: under
\(|U|=|aT|\le K\),
each term in (3.4) is bounded by a polynomial in \(|T|\) with
coefficients controlled by \(K\), \(a\), \(|\nabla a|\), and \(r^{-2}\).

**Step C: testing with \(|T|^{p-2}T\).**
Compute \(\partial_t|T|^p=p|T|^{p-2}\langle\partial_tT,T\rangle
+O(pa|E||T|^p)\), where the second term arises from the inverse-metric
variation \(\partial_tg^{-1}=+2aE\text{ (contracted)}\).  Since
\(a|E|\le C|U|\le CK\), this contributes \(\le CpK\int|T|^p\) and is
absorbed into the RHS.  Now pair \(\partial_tT\) from (3.4) with
\(p|T|^{p-2}T\) and integrate.

*Diffusion:* integration by parts of \(\int p|T|^{p-2}T\!:\!(a\Delta T)\)
gives:
\[
  -p\int a|T|^{p-2}|\nabla T|^2\,d\mu
  -p(p-2)\int a|T|^{p-4}|T\!:\!\nabla T|^2\,d\mu
  -p\int|T|^{p-2}(T\!:\!\nabla T)(\nabla a)\,d\mu.
\tag{3.6}
\]
The first two terms are nonpositive.  The third is a gradient-cutoff
boundary term.

*Reaction:* \(|\int p|T|^{p-2}T\!:\!a\mathcal Q|\le
Cp\int a|T|^{p+1}+Cp\int a|T|^{p-1}\).
Using \(a|T|^{p+1}=|aT||T|^p\le K|T|^p\) and
\(a|T|^{p-1}\le K|T|^{p-2}\):
\[
  \le CpK\int|T|^p+CpK\int|T|^{p-2}\,d\mu.
\tag{3.7}
\]
By Young, \(\int|T|^{p-2}\le\int|T|^p+C_p\operatorname{Vol}\).

*Normalization/G-evolution:*
\(|\int p|T|^{p-2}T\!:\!\mathcal N|
\le Cp\int a|T|^p+Cp\int a|T|^{p-1}\le CpK\int|T|^{p-1}+Cp\int a|T|^{p-1}\).
Using \(a\le1\) and \(|T|^{p-1}\le|T|^p+C\): absorbed into
\(C(K+1)\int|T|^p+C_p(K)\operatorname{Vol}\).

*Gradient-cutoff:*
From (3.6) and the explicit gradient terms:
\[
  |\text{gradient terms}|\le Cp\int|\nabla a||T|^{p-1}|\nabla T|\,d\mu.
\]
Young against the diffusion \(\int a|T|^{p-2}|\nabla T|^2\):
\[
  \le\frac{cp}{4}\int a|T|^{p-2}|\nabla T|^2
  +C_pp^2\int\frac{|\nabla a|^2}{a}|T|^p\,d\mu.
\tag{3.8}
\]
Since \(|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}\):
\(\le\frac{cp}{4}\cdot\text{dissipation}+C_pp^2r^{-2}\int|T|^p\).

*Hessian-cutoff:* the contribution
\(\int p|T|^{p-2}T\!:\!(\nabla^2a\star E)\) has the structure
\(I_H=p\int(\nabla_i\nabla_ja)\mathcal B^{ij}(T,E)|T|^{p-2}\,d\mu\),
where the contraction tensor satisfies \(|\mathcal B|\le C|T||E|\le C|T|^2\)
and \(|\nabla\mathcal B|\le C|T||\nabla T|\) (using \(\nabla G=0\),
so \(\nabla E\) is a trace of \(\nabla T\)).
Integrate by parts on the closed manifold \(M\):
\[
  I_H=-p\int(\nabla_ja)\nabla_i\bigl(\mathcal B^{ij}|T|^{p-2}\bigr)d\mu.
\]
The derivative hits \(\mathcal B\) (bounded by \(C|T||\nabla T|\)) and
\(|T|^{p-2}\) (bounded by \((p-2)|T|^{p-3}|\nabla T|\)).  Young against
the diffusion gives:
\[
  |I_H|
  \le\varepsilon p\int a|T|^{p-2}|\nabla T|^2
  +C_\varepsilon p^3\int\frac{|\nabla a|^2}{a}|T|^p
  \le\varepsilon p\cdot\text{dissipation}+C_\varepsilon p^3r^{-2}\int|T|^p.
\tag{3.9}
\]
Since \(|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}\) (zero-extended
where \(a=0\)).
The key point is that \(\nabla^2\chi\) itself does **not** appear
after integration by parts; only \(\nabla\chi\) and the \(T,E\)
derivative structures appear.

**Assembling.** Choose \(\varepsilon\) small, absorb into dissipation:
\[
  \frac{d}{dt}\int|T|^p+\frac{cp}{2}\int a|T|^{p-2}|\nabla T|^2
  \le C_p(K+1+r^{-2})\int|T|^p+C'_p(K,\operatorname{Vol}).
\tag{3.10}
\]
The dissipation controls \(\int a|\nabla(|T|^{p/2})|^2\) after the
chain rule.  The lower-order additive term \(C'_p\) comes from the
\(\int|T|^{p-2}\le\int|T|^p+C_p\operatorname{Vol}\) Young step
and from \(\int a|T|^{p-1}\) terms.  It depends on \(K\), \(p\),
\(\operatorname{Vol}(g(t))\), and is **finite** under the bilipschitz
comparison from the drift bound.

Gronwall gives (3.2).  \(\square\)

**Remark.**  The additive term \(C'_p\) prevents a purely multiplicative
Gronwall, but for the continuation application we only need finiteness
of \(\|T(t)\|_p\) on \([\tau,T_*)\), which (3.2) supplies.  The
sequence-uniform estimates use the **weighted** energies
\(K_p,J_6\) instead.

---

## 4. Structural equations for the staggered induction (new)

### 4.1 Zero-order identities

\[
  G=\frac{g\owedge g}{2(n-1)},\quad \nabla G=0,\quad\Delta G=0.
\tag{4.1}
\]
\[
  T=\operatorname{Rm}+G,\quad U=aT,\quad
  \operatorname{Ric}(T)=E,\quad \operatorname{Ric}(U)=aE.
\tag{4.2}
\]
  \partial_tg=-2\operatorname{Ric}(U),\qquad
  (\partial_t\Gamma)^k{}_{ij}
  =-g^{k\ell}\bigl(
  \nabla_i\operatorname{Ric}(U)_{j\ell}
  +\nabla_j\operatorname{Ric}(U)_{i\ell}
  -\nabla_\ell\operatorname{Ric}(U)_{ij}\bigr).
\tag{4.3}
\]
(Standard formula for \(\partial_tg=-2S\) with \(S=\operatorname{Ric}(U)\).)
The connection variation (4.3) contains only \(\nabla\operatorname{Ric}(U)
=\nabla(aE)\), which involves \(\nabla a\cdot E+a\nabla E\) —
at most one derivative of \(U\) and one of \(a\).

### 4.2 Higher covariant derivatives: notation

Write \(U_m=\nabla^mU\), \(T_m=\nabla^mT\), \(C_j=\nabla^j\chi\)
(cutoff jets).  Since \(a=\chi^2\):
\[
  \nabla^ra
  =\sum_{s+t=r}\binom{r}{s}C_s\cdot C_t,
\tag{4.4}
\]
and in particular:
\begin{align}
  \nabla a&=2\chi\,C_1, \tag{4.5a}\\
  \nabla^2a&=2\chi\,C_2+2C_1\otimes C_1, \tag{4.5b}\\
  \nabla^3a&=2\chi\,C_3+6C_1\cdot C_2\quad
  \text{(schematic)}, \tag{4.5c}\\
  \nabla^{r+1}a&=2\chi\,C_{r+1}+\sum_{\substack{s+t=r+1\\s,t\ge1}}
  \binom{r+1}{s}C_s\cdot C_t. \tag{4.5d}
\end{align}
**Key observation (A03 Step 40):** In (4.5d), the term \(2\chi\,C_{r+1}\)
is the **only** factor containing \(C_{r+1}\); every other summand
has \(C_s,C_t\) with \(s,t\le r\).

### 4.3 Evolution of cutoff jets

Because \(\chi\) is a time-independent scalar function on \(M\):
\(\partial_t(\nabla_i\chi)=\partial_t(\partial_i\chi)=0\)
(gradient of a scalar does not involve \(\Gamma\)).  So \(C_1\) is
time-independent.

For \(m\ge2\), the commutator formula gives:
\[
  \partial_tC_m=\partial_t(\nabla^m\chi)
  =-\sum_{j=1}^{m-1}\nabla^{j-1}(\partial_t\Gamma)\star C_{m-j}.
\tag{4.6}
\]
Since \(\partial_t\Gamma=g^{-1}\star\nabla\operatorname{Ric}(U)\), the
highest-derivative term in (4.6) is:
\[
  -\nabla^{m-2}(g^{-1}\star\nabla\operatorname{Ric}(U))\star C_1.
\]
This involves \(\nabla^{m-1}\operatorname{Ric}(U)\), which after expanding
\(U=aT\) and using \(\operatorname{Ric}\) as a trace contraction gives
terms with at most \(U_{m-1}\) or \(C_{m-1}\star T_0\).
No factor \(U_m\) or \(C_m\) appears in the RHS of (4.6).

**Consequence:** The cutoff-jet equation at order \(m\) depends on
\(U_0,\ldots,U_{m-1}\) and \(C_1,\ldots,C_{m-1}\), never on \(U_m\) or
\(C_m\) or higher.  This confirms that the staggered ordering
\(T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to\cdots\) has no upward
dependencies in the cutoff-jet equation.

### 4.4 Evolution of \(\nabla^mU\)

Since \(U=aT\), the Leibniz rule gives:
\[
  \nabla^mU=\sum_{s=0}^m\binom{m}{s}(\nabla^sa)(\nabla^{m-s}T).
\tag{4.7}
\]
Using (4.4), each \(\nabla^sa\) is a polynomial in
\(C_0=\chi,C_1,\ldots,C_s\).  The time derivative is:
\[
  \partial_t(\nabla^mU)
  =[\partial_t,\nabla^m]U+\nabla^m(\partial_tU).
\tag{4.8}
\]

**Commutator term.** The commutator
\([\partial_t,\nabla^m]\) involves \(\partial_t\Gamma\) contracted with
lower derivatives.  The highest-order term in \([\partial_t,\nabla^m]U\) is
\[
  -\nabla^{m-1}(\partial_t\Gamma)\star U
  =-\nabla^{m-1}(g^{-1}\star\nabla\operatorname{Ric}(U))\star U,
\]
which involves \(\nabla^m\operatorname{Ric}(U)\).  Since
\(\operatorname{Ric}(U)\) involves \(U\) and a trace contraction (no
additional derivatives), \(\nabla^m\operatorname{Ric}(U)\) involves
\(U_m\).  This is the **current** variable — it is the expected principal
contribution.

**\(\nabla^m(\partial_tU)\) term.**  Since \(a\) is time-independent:
\(\partial_tU=a(\partial_tT)\).  Therefore:
\[
  \nabla^m(a\partial_tT)
  =\sum_{s=0}^m\binom{m}{s}(\nabla^sa)(\nabla^{m-s}\partial_tT).
\tag{4.9}
\]
Using (3.4) for \(\partial_tT\), the highest second-spatial-derivative
term is \(a\Delta T\).  After \(\nabla^{m-s}\), this gives
\(\nabla^{m-s+2}T\) paired with \(\nabla^sa\).  When \(s=0\):
\(a^2\nabla^{m+2}T\) (note the \(a^2\) since \(\partial_tU\supset a\cdot(a\Delta T)\)).
Expanding \(U_m=\sum(\nabla^sa)(\nabla^{m-s}T)\), the principal
part becomes \(a\Delta U_m+\text{lower}\) — the **degenerate diffusion**
for \(U_m\), after absorbing the additional \(\nabla a\star\nabla T\)
terms from the Leibniz rearrangement.

When \(s\ge1\), the factor \(\nabla^sa\) introduces cutoff jets.
By (4.5d), the dangerous term is \(s=m+2-j\) with
\(\nabla^{m+2-j}a=2\chi C_{m+2-j}+\text{lower}\),
paired with \(\nabla^jT\).

**The combinatorial structure.** After the full expansion, every monomial
in the RHS of (4.8) has the schematic form
\[
  \chi^{\alpha_0}C_1^{\alpha_1}\cdots C_{m+2}^{\alpha_{m+2}}
  \cdot T^{\beta_0}\cdot T_1^{\beta_1}\cdots T_{m+1}^{\beta_{m+1}}
  \cdot g^{-1\,\text{contractions}},
\tag{4.10}
\]
subject to the derivative accounting
\[
  \sum_{j=1}^{m+2}j\alpha_j+\sum_{j=1}^{m+1}j\beta_j
  \le m+2\qquad\text{(total derivative count)}.
\tag{4.11}
\]
The Step 42 weight comparison shows that the **top cutoff term in the
weighted \(U_m\) equation must be derived in the form used by A03's energy
argument**:
\[
  \chi C_{m+2}\cdot U_0,
\tag{4.12a}
\]
not merely \(C_{m+2}U_0\).  The source of the extra factor is the term
\(a(\nabla^2a)*T=(\nabla^2a)*U\) in \(\partial_tU=a\partial_tT\):
\[
  \nabla^{m+2}a*U_0
  =(2\chi C_{m+2}+\text{lower})*U_0.
\tag{4.12b}
\]
This \(\chi\) is essential, because after integrating once off
\(C_{m+2}=\nabla C_{m+1}\) it gives
\(\chi C_{m+1}U_0\nabla P(U_m)\), which is absorbed by the weighted
dissipation \(\int\chi^2|\nabla U_m|^2|U_m|^{p-2}\).  Without that factor one
would need unweighted control of \(\nabla U_m\) in the transition region.

The other current cutoff-jet structures are
\[
  C_1\cdot C_{m+1}\cdot U_0,
  \qquad
  \chi C_{m+1}\cdot U_1.
\tag{4.12c}
\]
The second term is the residual that A03 handles by a further integration by
parts for \(m\ge2\), writing \(C_{m+1}=\nabla C_m\).  At \(m=1\) it merges
with the signed Hessian-\(a\) mechanism.

**Unresolved source-level comparison.**  The derivative ordering strongly
supports the A03 staggered scheme, but the proof still needs the complete
normalized weighted \(U_m\) equation to verify that every surviving top
\(C_{m+2}\) term has the weight in (4.12a), and that no commutator,
normalization, or \(G\)-variation term produces a bare \(C_{m+2}U_0\).  This is
recorded as H-WU in the Step 42 repair note.

**For \(C_{m+1}\) itself:** the cutoff-jet evolution (4.6) at order \(m+1\)
only involves \(U_0,\ldots,U_m\) and \(C_1,\ldots,C_m\), as shown
in §4.3.

**G-term structure at higher orders.**  Since \(\nabla G=0\),
\(\nabla^jT=\nabla^j\operatorname{Rm}\) for all \(j\ge1\).
Similarly, \(\nabla^jU=\sum_{s+t=j}(\nabla^sa)(\nabla^t\operatorname{Rm})
+(\nabla^ja)\cdot G\), so the G contribution at order \(j\ge1\) is only the
zero-order \((\nabla^ja)\cdot G\) term — a cutoff jet times a bounded
constant.  **No new derivative branch from \(G\) enters at any order.**

**Normalization-term structure.**  The \(-2a\operatorname{Rm}=-2a(T-G)\)
and \(\partial_tG=-2a(E\owedge g)/(n-1)\) terms are algebraic in \(T\)
and \(a\).  Their \(m\)-th covariant derivative introduces
\(\nabla^s a\cdot\nabla^{m-s}T\) (from Leibniz), hence only cutoff jets
and already-established T-derivatives.  **No new structural branch.**

**Current conclusion.** The A03 staggered ordering
\[
  T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\tag{4.13}
\]
has the right derivative ordering for the normalized shifted equation, and the
Step 42 comparison identifies the necessary top weight.  It is not yet a
self-contained all-order tensor proof until H-WU verifies the exact weighted
\(U_m\) equation and its surviving top cutoff terms.

### 4.5 Unweighted \(T_m\) evolution

The evolution of \(T_m=\nabla^m T=\nabla^m\operatorname{Rm}\) (for \(m\ge1\))
follows the same structure as \(U_m\) but without the cutoff weight.
By (4.4)–(4.5d), \(\nabla^{m+2}a\) enters through the identity
\[
  \nabla^{m+2}a=2\chi C_{m+2}+\sum_{\substack{s+t=m+2\\s,t\ge1}}
  C_s\cdot C_t.
\tag{4.14}
\]
The term \(2\chi C_{m+2}\cdot T_0\) in the unweighted equation must be
handled by a **single integration by parts off \(C_{m+2}\)**, using
\[
  \nabla(C_{m+2})=C_{m+3}\quad\text{(not needed!)}\quad
  \text{— instead, IBP moves one }\nabla\text{ from }C_{m+2}
  \text{ to the test function and }\chi T_0.
\]
This produces \(C_{m+1}\) and lower terms, plus a boundary contribution
from \(\nabla\chi\) that is bounded by \(C/r\).  A03 Step 40's
mechanism (Proposition 3.1) handles this for all \(m\).

---

## 5. Analytic platform (corrected references)

### 5.1 Transported DeTurck existence (A03 Step 37)

The normalized transported-coefficient DeTurck system
\[
  \partial_t\widehat g
  =-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
  +\mathcal L_{\widehat aW}\widehat g,
  \qquad
  \widehat a=a\circ\varphi_t^{-1},
\tag{5.1}
\]
is a lower-order perturbation of Yang's system (Yang, Theorem 8.2 in the
arXiv version; `Convergence-of-riemannian-manifolds-with-integral-bounds`
Knowledge object, lines 787–823).  The normalization adds
\(\delta(-2\widehat a\widehat g)=-2\widehat ah-2(\delta\widehat a)\widehat g\)
to the linearized pair, preserving the principal and first-order triangular
structure.

**What is still needed** for a self-contained proof: the explicit
\(\varepsilon\)-independent tame energy estimates with the additional
lower-order terms (including the transported
\(\delta\widehat a=-d\widehat a(\psi)\) coupling), the smooth limit
as the linearization regularization is removed, and smooth dependence or
local uniqueness sufficient for a single maximal solution.  Once this
per-datum theorem is proved, restart from any smooth terminal metric is
immediate.

**Quantifier separation.** Per-datum existence time may depend on all
geometry of the single smooth input.  Sequence-uniform estimates enter
only after a smooth solution exists.

### 5.2 Homogeneous \(K_2\) propagation (Step 34)

The correct propagation is the multiplicative estimate:
\[
  (K_2^\eta)'+cD_2^\eta\le CY+Cr^{-2}K_2^\eta,
\tag{5.2}
\]
with \(Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta)\).  After absorption:
\[
  (K_2^\eta)'\le C(1+r^{-2})K_2^\eta,
  \qquad K_2^\eta(t)\le e^{C(1+r^{-2})t}K_2^\eta(0).
\tag{5.3}
\]
No bare additive \(C_0T\) term.  This survives collapse.

### 5.3 Fixed-exponent chain (Steps 34–35)

The chain
\[
  K_2^\eta\to B(t)\le C\gamma^3\to Y(t)\le C\gamma K_2^\eta(0)/t
  \to J_6(t)\le C\delta^6V
\tag{5.4}
\]
and the curvature power inequality
\[
  K_p'+c[pD_p^{\rm Rm}+p(p-2)D_p^F]
  \le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p
\tag{5.5}
\]
are established in Steps 34–35 with complete tensor-level proofs,
including signed Hessian-\(a\) IBP (no evolving pointwise Hessian bound).

### 5.4 Weighted Moser endpoints

On positive dyadic slabs, the nested recurrence gives:
\[
  \|aF(t)\|_\infty\le\frac{C\gamma}{t},
  \qquad
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
\tag{5.6}
\]
The defect endpoint is integrable:
\[
  \int_0^T\|aE\|_\infty\,dt
  \le\frac32C\delta\theta^{2/3}r^2.
\tag{5.7}
\]

### 5.5 Smooth extension statement (A03 Step 45, current form)

**Theorem 5.1 (smooth extension).**
*If \(|U|\le K\) on \([\tau,T_{\max})\) with finite bilipschitz metric
comparison, then: (i) the unweighted \(T\in L^p\) bound (Lemma 3.1)
supplies finiteness of \(\|T\|_p\); (ii) the staggered derivative-energy
induction (§4, A03 Step 40) together with the Sobolev and connection-
difference induction supplies finiteness of all higher spatial
derivatives of the curvature on \([\tau,T_{\max})\);
(iii) per-datum existence (§5.1) restarts the flow beyond
\(T_{\max}\).*

This is A03 Step 41, Theorem 3.1, now grounded in the structural
equations of §4 and the unweighted \(T\) lemma of §3.

### 5.6 First-exit closure

On the first-exit interval \([0,T_*]\) with \(T_*=\theta r^2\):

1. The Moser endpoint gives \(|U(t)|\le C\gamma/t+C\) for \(t>0\);
   the smooth initial layer covers \([0,\tau]\).
2. Finite maximal time below the selected interval is excluded by the smooth extension statement (Theorem 5.1).
3. Self-improvement: if \(K_2^\eta\) stays below \(2K_2^\eta(0)\),
   the Moser coefficient satisfies \(\gamma\le\gamma_0\), and the
   drift integral stays below \(\alpha_0/2\).  The first-exit
   conclusions extend to \(\theta r^2\).

---

## 6. Global \(Q\) propagation (Step 36)

The unweighted global defect \(Q(t)=\int_M|E|^2\,d\mu_t\) satisfies
\[
  Q(t)\le e^{C(1+r^{-2})t}Q(0).
\tag{6.1}
\]
On the stationary complement \(a=0\), both \(E\) and \(d\mu\) are
frozen.  On each support, the Step 36 derivation gives
\(Q_U'+cX_U\le C(1+r^{-2})Q_U+C\gamma(X_U+r^{-2}Q_U)\); after
absorption and disjoint summation, (6.1) follows.

Since \(Q(0)/A_i\to0\) (from \(\delta_i\to0\) and calibrated volume),
\(Q(T)/A_i\to0\) for fixed \(\theta\).

---

## 7. Terminal recalibration (corrected topology and sign)

### 7.1 Monopole class selection at the terminal metric

The terminal metric \(g_i(T)\) determines a Hodge decomposition.
For each sign choice \(\varepsilon\), the class
\[
  \kappa_\varepsilon=\sum_{j=1}^m c_1(X_{j,i})+\sum_\ell\varepsilon_\ell e_\ell
\]
is a monopole class of the original Ishida--LeBrun family.  The Seiberg--Witten
invariants are topological, so the mixed SW inequality (1.1) holds for the
terminal metric \(g_i(T)\) as well.

Averaging over all exceptional signs gives:
\[
  I_i(T)\ge\frac23\!\left[A_i+\sum_\ell(e_\ell^+(T))^2\right]
  \ge\frac23A_i.
\tag{7.1}
\]
Indeed \(\left(\sum_j c_1(X_{j,i})\right)^+\!{}^2\ge
\left(\sum_j c_1(X_{j,i})\right)^2=A_i\), and the sign average removes the
cross terms involving the \(e_\ell^+\).

### 7.2 Terminal defect density

Use \(e_\ell\) for the exceptional cohomology classes, to avoid confusing them
with the Einstein defect \(E=\operatorname{Ric}+g\).  With
\(q_i=D_i^{\rm top}-A_i/3\ge0\), where
\(D_i^{\rm top}=4m-(2\chi+3\tau)(N_i)\),
\[
  D_{{\rm av},i}(T)
  =I_i(T)-\frac23A_i-\frac23\sum_\ell(e_\ell^+(T))^2\ge0,
\tag{7.2}
\]
and the corrected Chern--Weil identity gives
\[
  D_{{\rm av},i}(T)
  =J_i(T)-q_i-\frac23\sum_\ell(e_\ell^+(T))^2.
\tag{7.3}
\]
Thus, for \(q_i\ge0\),
\[
  0\le D_{{\rm av},i}(T)\le J_i(T)\le {Q_i(T)\over 8\pi^2},
  \qquad D_{{\rm av},i}(T)/A_i\to0.
\tag{7.4}
\]

The nonnegative terminal density used for pullback must contain the full
Einstein defect:
\[
  \Phi_i
  =|E_i|^2+(s_i+4)^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i,
\tag{7.5}
\]
where
\(\mathcal G_i=f_i^2-(a_{*,i,-})^2\) is the self-dual spectral gap density
from Steps 5--8.  The terminal estimates give
\[
  \int (s_i+4)^2\le4Q_i(T),\qquad
  \int (s_i+8\sqrt6|W_i^+|)^2\le108Q_i(T),\qquad
  \int\mathcal G_i\le6Q_i(T),
\]
under \(q_i\ge0\).  Hence
\[
  \int_{M_i}\Phi_i\,d\mu(T)
  \le119\,Q_i(T).
\tag{7.6}
\]
The inclusion of \(|E_i|^2\) is essential for the terminal harmonic-coordinate
Einstein limit; scalar and Weyl calibration alone would not force
\(\operatorname{Ric}+g\to0\).

---

## 8. Terminal pullback and Derdziński contradiction (Step 28, corrected)

### 8.1 Inner center sets

**Definition.** The inner plateau is
\(P_i^{\rm in}=\bigcup_\alpha B_{r}(x_\alpha)\subset
\bigcup_\alpha B_{5r}(x_\alpha)\).
By Bishop–Gromov,
\[
  \operatorname{Vol}(B_r(x_\alpha))
  \ge\frac{V_{-2}(r)}{V_{-2}(5r)}
  \operatorname{Vol}(B_{5r}(x_\alpha)),
\tag{8.1}
\]
so \(\operatorname{Vol}(P_i^{\rm in})\ge c\,\alpha_0A_i\) for universal \(c\).

Terminal metric comparison:
\(\|g_i(T)-g_i(0)\|_{C^0}\le C\delta_i\theta^{2/3}r^2\to0\),
so the terminal volume of \(P_i^{\rm in}\) remains \(\ge c'\alpha_0A_i\).

### 8.2 Geodesic buffers

For \(p\in B_r(x_\alpha)\) (inner center) and \(\rho\le r\), every
geodesic of length \(\le\rho\) from \(p\) under the terminal metric stays
in \(B_{2r}(x_\alpha)\subset B_{5r}(x_\alpha)\), which is the plateau
region where \(a=1\) and \(|\operatorname{Rm}(T)|\le K\) (bounded
curvature from Moser).  Hence the exponential-map pullback
\(\widehat g_i=(\exp_p^{g_i(T)})^*g_i(T)\) on \(B_\rho(0)\subset T_pM\)
has uniformly bounded curvature and Rauch-comparison noncollapse.

### 8.3 Liouville–Rauch averaging

For any nonneg measurable \(D\) on \(M_i\), define the Liouville average
\[
  A_\rho D(p)
  =\frac{\int_{S_pM}\int_0^\rho D(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi}
  {\int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi},
\tag{8.2}
\]
where \(J_p(t,\xi)\) is the Jacobian determinant.  Then:
\[
  \int_{P_i^{\rm in}}A_\rho D(p)\,d\mu_{T}(p)
  \le C(K,\rho)\int_{M_i}D\,d\mu_T.
\tag{8.3}
\]
(The constant is independent of the number of supports, because the
integration over \(P_i^{\rm in}\) is one global integral.)

Apply (8.3) to \(D=\Phi_i\) from (7.5):
\[
  \frac{1}{\operatorname{Vol}(P_i^{\rm in})}
  \int_{P_i^{\rm in}}A_\rho\Phi_i(p)\,d\mu_T
  \le\frac{C(K,\rho)}{c'\alpha_0A_i}\int\Phi_i
  \le\frac{119C(K,\rho)}{c'\alpha_0}\cdot\frac{Q_i(T)}{A_i}
  \to0.
\tag{8.4}
\]
Hence there exists \(p_i\in P_i^{\rm in}\) with
\(A_\rho\Phi_i(p_i)\to0\).

### 8.4 Strong convergence on the tangent domain

The pullback metrics
\(\widehat g_i=(\exp_{p_i}^{g_i(T)})^*g_i(T)\) on \(B_\rho(0)\)
have:
- uniformly bounded sectional curvature \(\le K\);
- Rauch lower volume bound
  \(\operatorname{Vol}(\widehat B_{\rho/2})\ge c(K)>0\);
- therefore a harmonic-radius lower bound on \(B_{\rho/2}(0)\).

In harmonic coordinates on a smaller ball \(B_{\rho'}(0)\) (\(\rho'<\rho/2\)):
\[
  g_i^{ab}\partial_a\partial_b(\widehat g_i)_{jk}
  =-2(\operatorname{Ric}_{\widehat g_i})_{jk}
  +Q_{jk}(\widehat g_i^{-1},\partial\widehat g_i).
\tag{8.5}
\]
The terminal compactness passage uses only the regularity needed for the
Derdziński limit.  Uniform sectional curvature and the Rauch volume lower
bound give harmonic coordinates on a smaller ball with uniform
\(C^{1,\alpha}\cap W^{2,p}\) bounds.  In those coordinates,
\[
  \operatorname{Ric}_{\widehat g_i}=-\widehat g_i+E_i,
  \qquad \|E_i\|_{L^p_{\rm loc}}\to0
\]
for every finite \(p\), using the \(|E_i|^2\) component of the terminal density
selected by (8.4) and the available uniform bounds.  Elliptic stability for (8.5) then yields, after
passing to a subsequence,
\[
  \widehat g_i\to g_\infty\quad\text{strongly in }W^{2,p}_{\rm loc}
  \quad(p<\infty),
  \qquad \operatorname{Ric}_{g_\infty}=-g_\infty
\tag{8.6}
\]
in the weak harmonic-coordinate sense.  The curvature tensors therefore
converge strongly in \(L^p_{\rm loc}\), which is enough to pass the Weyl modulus
and spectral deficits.  Elliptic bootstrapping of the limiting Einstein equation
makes \(g_\infty\) smooth.  This replaces the unsupported \(W^{4,p}\) inference
from a \(C^0\)-small defect.

### 8.5 Derdziński contradiction

From the vanishing pullback average (8.4) applied to \(\Phi_i\), the limit satisfies:
\[
  E_\infty=0,\quad
  s_\infty=-4,\quad
  s_\infty+8\sqrt6\,|W^+_\infty|=0,\quad
  \mathcal G_\infty=0,
\tag{8.7}
\]
which forces
\[
  |W^+_\infty|^2=\frac1{24},\qquad
  \operatorname{spec}(W^+_\infty)
  =\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{8.8}
\]
The Einstein equation gives \(\delta W^+_\infty=0\) (Bianchi).
Since \(W^+\ne0\) and has at most two eigenvalues, Derdziński
Proposition 5 states: the metric \((24|W^+|^2)^{1/3}g_\infty\) is locally
Kähler.  In (8.8) the conformal factor is constant (\(=1\)), so
\(g_\infty\) itself is locally Kähler.

But a Kähler–Einstein metric with \(\operatorname{Ric}=-g\) in dimension 4
satisfies
\[
  |W^+|^2=\frac{s^2}{24}=\frac{16}{24}=\frac23\ne\frac1{24}.
\tag{8.9}
\]
Contradiction.  \(\square\)

---
## 9. Current proof ledger after Step 44

The restricted family-uniform negative result is now supported by the following
modules, read with the Step 42--44 repairs.

| Component | Evidence |
|---|---|
| Near-critical Ishida--LeBrun calibration | Steps 2--8, corrected algebra in Step 42 and §1 |
| Calibrated Weyl spectrum and spectral gap density | Steps 5--8, terminal reuse in §7 |
| Calibrated volume ratio \(\operatorname{Vol}/A\to32\pi^2/9\) | Step 5 and Step 42 |
| Support construction | §2 with strict \(\chi,\eta\) buffers and maximal-function threshold |
| Exact flow construction | Step 43 H-DT note corrected by Step 44 and A03 Step 45 coefficient regularization |
| Weighted extension | Step 43 H-WU note corrected by Step 44 and A03 Step 45 current-pair estimate |
| Zero-order unweighted \(T\) seed | §3 and A03 Step 44 |
| Curvature and defect signed-Hessian tensor variations | Step 35 and Step 34/36 defect uses |
| \(K_2^\eta\), \(Y\), \(J_6\), Moser endpoints | Step 34 with first-exit use on the exact flow |
| Global \(Q\) propagation | Step 36, applied only after the exact \(a=\chi^2\) flow exists |
| Terminal recalibration | §7 using \(D_{\rm av}=J-q-(2/3)\sum(e_\ell^+)^2\) and \(\Phi\supset |E|^2\) |
| Exponential pullback and strong finite-\(W^{2,p}\) limit | Step 28 and §8 |
| Derdziński forbidden germ | Step 8 and §8.5 |

A consolidated proof should now be written from these corrected modules rather
than by quoting this older note verbatim.  The proof must keep the order of
operations explicit: coefficient regularization constructs a smooth exact flow;
the stationary complement and disjoint support summation are then applied to
that exact flow; terminal selection uses the density \(\Phi\), not the older
\(\mathfrak D\) density.

The theorem remains restricted to the negative sign in the Ishida--LeBrun
four-dimensional geography with \(q\ge0\).  It does not address the positive
branch, arbitrary four-manifold topology, dimensions \(n\ge5\), dimension-only
constants for the full Yau 26 proposition, or Lean 4 formalization.

---

## 10. Evidence and companion files

- Step 44 Preceptor reading: `step44_preceptor_reading_first_exit_terminal_chain.md`
- Tensor identities: `step35_tensor_variation_and_hessian_a.md`
- Fixed-exponent chain: `step34_integrated_potential_q3_and_defect.md`
- Global \(Q\): `step36_analytic_platform_and_global_Q.md`
- Terminal recalibration/pullback: `step28_terminal_recalibration_pullback.md`
- H-WU correction: `step43_H_WU_resolution_weighted_evolution.md`
- H-DT correction: `step43_H_DT_assessment.md`
- A03 coordinate ledger: `Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md`
- A03 zero-order \(T\) seed: `Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md`
- TTCS Step 44 integration: `trace/ttcs/results/step44_ttcs01_verifier1_integration.md`
