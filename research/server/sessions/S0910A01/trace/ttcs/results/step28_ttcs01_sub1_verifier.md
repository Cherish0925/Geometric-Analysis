# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/codex_loop/Research_Report.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step16_exponential_pullback_averaging_review.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step28_terminal_pullback_constants.py",
    "Sessions/S0910A01/workspace/scripts/step28_moser_recurrence_verify.py"
  ]
}
```

## Task

Verify the Step 28 consolidation of the restricted four-dimensional negative LeBrun/Ishida-LeBrun route. Read the A01 terminal recalibration/pullback note, the patched A01 weak-Moser note, A03's general-p note, A03's shifted-curvature continuation theorem and Codex report/artifact, plus the Step 16 pullback and Step 8 Derdzinski/gap notes. Please check three scientific points: (1) whether the corrected Moser recurrence (using A03 Sections 5.2-5.3, fixed J6 from time zero, polynomial p-dependence inside the time-cutoff recurrence) avoids the exponent/Gronwall errors; (2) whether the shifted curvature U=a(Rm+G) continuation proof really removes the normalization/cutoff-jet obstacle at the schematic proof level; (3) whether terminal recalibration plus exponential-pullback selection legitimately bypasses plateau noncollapse and Euler-density localization, assuming the analytic selected-support theorem produces a positive-volume bounded-curvature plateau set and Q(T)/A -> 0. Identify any remaining logical gaps or corrections without lowering the all-dimensional Yau-26 goal.

## Output

# Scientific verification memo

## Overall assessment

The Step 28 consolidation is mathematically coherent in its three main interfaces:

1. The revised Moser argument removes the earlier exponentiation problem: polynomial \(p\)-dependence remains inside a time-cutoff recurrence, and the relevant infinite products converge.
2. The shifted tensor
   \[
   U=a(\operatorname{Rm}+G),\qquad G=\frac{g\owedge g}{2(n-1)},
   \]
   restores Wang’s triangular derivative structure for the normalized cutoff flow at the schematic/source-transfer level.
3. Terminal recalibration and exponential pullback do bypass base-manifold noncollapse and Euler-density localization, provided the plateau output has the quantitative form used in Step 28: volume comparable to \(A_i\), fixed curvature and radius constants, and a fixed-width geodesic buffer.

The resulting implication is still conditional on the selected-support flow theorem and its global energy estimates.

---

## 1. Corrected Moser recurrence

### 1.1 The weight algebra is consistent

For
\[
K_p=\int \eta^2a^{p-2}\Phi^p,\qquad
Z_p=\eta a^{(p-1)/2}\Phi^{p/2},
\]
the support condition \(\eta=1\) wherever \(a>0\) gives
\[
K_{2p}=\int Z_p^4.
\]
Indeed, both integrands equal \(a^{2p-2}\Phi^{2p}\) on the active region, while they vanish where \(a=0\).

In dimension four,
\[
K_{3p/2}
\le K_p^{1/2}K_{2p}^{1/2},
\]
because the interpolated \(a\)-exponent is
\[
\frac{p-2}{2}+\frac{2p-2}{2}
=\frac{3p}{2}-2.
\]
This exact exponent identity is essential: there is no residual power of \(a\) near its zero set.

Combining this interpolation with
\[
\|Z_p\|_4^2
\le \mathsf S\bigl(\|\nabla Z_p\|_2^2+r^{-2}\|Z_p\|_2^2\bigr)
\]
produces the A03 recurrence
\[
\mathcal M_{p_{k+1},k+1}
\le C\mathsf S\bigl(L_k\mathcal M_{p_k,k}\bigr)^{3/2},
\qquad p_{k+1}=\frac32p_k.
\]

### 1.2 Polynomial \(p\)-dependence no longer enters an exponential

On a slab \([t/2,t]\), the potential estimate
\[
\mathsf S^2Y(s)\le \frac{C\beta^3}{s}
\le \frac{2C\beta^3}{t}
\]
turns the power-energy inequality into
\[
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^N\left(r^{-2}+\frac{\beta^3}{t}\right)K_p.
\]
Multiplication by a time cutoff and direct integration gives
\[
L_k=Cp_k^N4^k\left(t^{-1}+r^{-2}\right),
\]
after using the fixed small upper bound for \(\beta\). No separate Grönwall step at exponent \(p_k\) is needed.

Writing \(m_k=\mathcal M_{p_k,k}^{1/p_k}\),
\[
m_{k+1}
\le (C\mathsf S)^{1/((3/2)p_k)}L_k^{1/p_k}m_k.
\]
The sums are
\[
\sum_{k\ge0}\frac1{p_k}=\frac3{p_0},
\qquad
\sum_{k\ge0}\frac1{(3/2)p_k}=\frac2{p_0}.
\]
Thus the total Sobolev power is \(\mathsf S^{2/p_0}\), while
\[
\sum_k\frac{\log L_k}{p_k}<\infty
\]
because \(\log L_k=O(k+\log p_k)\) and \(p_k\) grows geometrically. The two Step 28 scripts correctly verify these exponent sums; they are algebra ledgers rather than proofs of the underlying tensor inequality.

### 1.3 The two endpoint estimates follow with the stated powers

For curvature, \(p_0=3\) and
\[
\int_{t/2}^tY(s)\,ds\le C\beta^3\mathsf S^{-2}.
\]
Hence
\[
\|aF(t)\|_\infty
\le C\mathsf S^{2/3}t^{-1}
   \bigl(\beta^3\mathsf S^{-2}\bigr)^{1/3}
=\frac{C\beta}{t}.
\]

For the defect, \(p_0=6\) and
\[
\int_{t/2}^tJ_6(s)\,ds
\le C\delta^6Vt.
\]
Therefore
\[
\|aE(t)\|_\infty
\le C\mathsf S^{1/3}t^{-1/2}
   (\delta^6Vt)^{1/6}.
\]
Using \(\mathsf S=Cr^2V^{-1/2}\) gives
\[
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]
The volume factors cancel exactly.

### 1.4 Starting \(J_6\) at time zero is the correct repair

The A03 estimate
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6
+C\int a^5F|E|^6
\]
allows
\[
\int a^5F|E|^6
\le \|F\|_{L^2(\operatorname{supp}\chi)}
   \|Z_6\|_4^2
\le \bar\beta
   \bigl(\|\nabla Z_6\|_2^2+r^{-2}J_6\bigr).
\]
Since \(p=6\) is fixed, one fixed smallness threshold for \(\bar\beta\) absorbs this term and yields
\[
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
This avoids integrating a coefficient proportional to \(1/t\) from time zero.

### 1.5 Remaining analytic substance in this part

The recurrence itself is now correct. Its required input remains the fully justified inequality
\[
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^Nr^{-2}K_p
 +Cp^N\int a^{p-1}F\Phi^p
\]
with \(c\) uniform for \(p\ge3\) and one finite \(N\). A03 supplies the right derivative counting and weight identities, but several Hessian-cutoff contractions are still compressed into schematic notation, especially for regularized \(|E|\). A publication-level proof would contain the complete contraction formulas, the grouped integrations by parts, and an explicit uniform approximation for the noninteger weights \(a^{p-2}\).

The \(Y(t)\) estimate, active-region \(H_2\) preservation, and global \(Q(t)\) inequality also remain inputs rather than consequences of the recurrence.

---

## 2. Shifted-curvature continuation

### 2.1 The shift correctly incorporates normalization

With the supplied conventions,
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
\operatorname{Ric}(G)=g.
\]
Thus, for
\[
T=\operatorname{Rm}+G,\qquad U=aT,
\]
one has the exact identities
\[
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,
\qquad
\operatorname{Ric}(U)=aE,
\qquad
\partial_tg=-2\operatorname{Ric}(U).
\]
The formula
\[
\partial_tG=\frac1{n-1}(\partial_tg)\owedge g
\]
is consistent with the variation of the contraction \(g^{ik}G_{ijkl}=g_{jl}\). The accompanying script correctly verifies this convention-sensitive algebra.

The shifted evolution
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T)
\]
has the decisive vanishing property that every term contains \(T\) or a derivative of \(T\). In particular, there is no independent \(\nabla^2a*G\) source. This is also forced by the fact that \(T=0\) represents a stationary metric with \(\operatorname{Ric}=-g\).

### 2.2 Multiplication by \(a\) removes division at the zero set

For \(U=aT\), the equation has the form
\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U
 +U*U+aG*U.
\]
All uses of the cutoff quotient reduce to
\[
\frac{|da|^2}{a}=4|d\chi|^2,
\]
which extends continuously across \(\{a=0\}\). Therefore no inverse power of \(a\) is introduced.

### 2.3 The derivative triangle agrees with Wang’s mechanism

The raw differentiated equation contains
\[
\chi\nabla^{m+2}\chi*U,\quad
\nabla\chi*\nabla^{m+1}\chi*U,\quad
\chi\nabla^{m+1}\chi*\nabla U,\quad
\chi\nabla\chi*\nabla^{m+1}U.
\]
The Codex artifact identifies the same four highest-order allocations as Wang’s local Ricci-flow argument.

The grouped integration by parts used in Wang’s Proposition 4.14 has two effects:

- terms containing \(\nabla^{m+1}U\) retain a factor \(\chi\) and are absorbed by
  \[
  \int \chi^2|\nabla^{m+1}U|^2|\nabla^mU|^{p-2};
  \]
- the apparent \(\nabla^{m+2}\chi\) input reduces to cutoff derivatives of order at most \(m\), with the residual top product
  \[
  \nabla^2\chi*\nabla^m\chi*U*
  \nabla^mU|\nabla^mU|^{p-2}.
  \]

The resulting induction order is
\[
\nabla^{m-1}U
\longrightarrow \nabla^m\chi
\longrightarrow \nabla^{m-1}T
\longrightarrow \nabla^mU.
\]
The added \(G\)-terms are linear in the current \(U\)-derivative or involve previously controlled derivatives, so they add no new highest-order input.

The unweighted \(L^p\) estimate for \(T\) is also sound:
\[
\frac d{dt}\int|T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\int|T|^p.
\]
The Hessian of \(a\) is integrated once, and the resulting \(da\)-term is controlled using \(|da|^2/a=4|d\chi|^2\). Hence large curvature hidden where \(a\) is small is controlled in finite \(L^p\), while the metric is stationary outside the cutoff support.

### 2.4 Smooth extension follows from the resulting bounds

A uniform bound for \(|U|\) gives
\[
|\partial_tg|\le C,
\]
hence uniform metric equivalence. The all-order estimates for \(U\) imply all-order estimates for
\[
\partial_tg=-2\operatorname{Ric}(U).
\]
The connection-difference argument then gives convergence of \(g(t)\) in every \(C^r\) norm to a positive-definite terminal metric.

There is one textual correction. Equation (7.3) in the A03 note writes an unspecified \(\mathcal L_V\widehat g\). The formula consistent with the detailed artifact is
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}(\widehat g)+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,
\]
together with
\[
\partial_t\phi\circ\phi^{-1}=-\widehat aW,
\qquad
\phi^*\widehat a=a.
\]
Without the factor \(\widehat a\) in both the gauge vector and the transported coefficient, pullback does not recover the fixed-cutoff equation.

At the schematic/source-transfer level, the normalization and cutoff-jet obstruction is removed. A completely standalone proof would reproduce Wang’s grouped contraction identity and staggered Hölder exponents rather than referring to them as verbatim transfers.

---

## 3. Terminal recalibration and exponential pullback

### 3.1 The terminal constants are correct

In four dimensions,
\[
E=\operatorname{Ric}+g
=\operatorname{Ric}^{\circ}+\frac{s+4}{4}g,
\]
so
\[
|E|^2=|\operatorname{Ric}^{\circ}|^2+\frac{(s+4)^2}{4}.
\]
Consequently,
\[
\int(s+4)^2\le4Q(T),\qquad
J\le\frac{Q(T)}{8\pi^2}.
\]

For the terminally reselected monopole sign,
\[
0\le D_a\le J.
\]
The Step 8 square and gap estimates then give
\[
\int(s+8\sqrt6|W^+|)^2\le108Q(T),
\qquad
\int\mathcal G\le6Q(T).
\]
Adding these to \(\int|E|^2\) and \(\int(s+4)^2\) yields
\[
\int\mathfrak D\le119Q(T).
\]
The script reproduces \(108\), \(6\), and \(119\) correctly.

This recalibration is genuinely terminal: no curvature tensor is transported from time zero. The Seiberg–Witten and Chern–Gauss–Bonnet relations are reapplied to the terminal closed metric.

### 3.2 Exponential averaging does not use base injectivity radius

Under \(|\sec|\le K\) along all radial geodesics of length \(\rho\),
\[
s_K(t)^3\le J_p(t,\xi)\le s_{-K}(t)^3.
\]
Liouville invariance gives
\[
\int_{P_i}A_\rho\mathfrak D_i
\le C(4,K,\rho)\int_{M_i}\mathfrak D_i.
\]
Therefore, if
\[
\operatorname{Vol}(P_i)\ge\alpha A_i,\qquad
\int\mathfrak D_i=o(A_i),
\]
some \(p_i\in P_i\) satisfies
\[
A_\rho\mathfrak D_i(p_i)\to0.
\]

Multiple sheets of \(\exp_{p_i}\) over the base cause no problem: the argument integrates on the tangent ball with multiplicity, and every density involved is pointwise \(\ge0\).

A merely nonzero value of \(\operatorname{Vol}(P_i)\) is not sufficient. The needed quantitative statement is \(\operatorname{Vol}(P_i)\ge\alpha A_i\) with fixed \(\alpha>0\), together with fixed \(K,\rho\) and radial containment in the curvature-controlled buffer.

### 3.3 Pullback restores local noncollapse

For
\[
\widehat g_i=(\exp_{p_i})^*g_i(T)
\]
on \(B_\rho(0)\subset T_{p_i}M_i\), radial coordinates satisfy
\[
s_K(t)^3\le J_i(t,\xi).
\]
The radial coordinate has unit gradient before conjugacy, so the metric ball centered at the origin agrees with the corresponding radial tangent ball. Hence smaller balls have a uniform positive volume lower bound. Distinct tangent vectors are not identified even when their images in \(M_i\) coincide.

Bounded curvature also gives a uniform \(L^\infty\) bound for \(E_i\). Since the selected pullback integral of \(|E_i|^2\) tends to zero,
\[
E_i\to0
\quad\text{strongly in every finite }L^p
\]
by interpolation. Harmonic-coordinate elliptic estimates then give strong finite-\(W^{2,p}\) convergence on a smaller ball. This fills an important detail in Step 28: \(L^2\) defect plus bounded curvature is enough to recover the stronger finite-\(L^p\) convergence needed for the harmonic-coordinate equation.

The limit satisfies
\[
\operatorname{Ric}=-g,\qquad s=-4,\qquad
s+8\sqrt6|W^+|=0,\qquad \mathcal G=0.
\]
Thus
\[
|W^+|^2=\frac1{24},\qquad
\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Derdziński’s factor is
\[
(24|W^+|^2)^{1/3}=1,
\]
so the metric itself is locally Kähler. A Kähler–Einstein four-metric with \(s=-4\) has
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
which is incompatible with \(1/24\). The Step 8 source passage and spectrum algebra support this conclusion.

---

## 4. Mathematical content still absent

The consolidation supports the downstream implication, but the following ingredients are not yet established in the supplied notes:

- a selected-support flow construction producing
  \[
  \operatorname{Vol}(P_i)\ge\alpha A_i
  \]
  after shrinking to fixed-width inner plateaux;
- fixed \(K,\rho\) and terminal radial containment for every center in \(P_i\);
- the pointwise-in-time \(Y\)-estimate, active \(H_2\) preservation, fixed \(J_6\) estimate, and global
  \[
  Q_i(T)\le e^{C\theta}Q_i(0)
  \]
  as one simultaneous theorem for the multi-support flow;
- full index-level general-\(p\) curvature and defect inequalities with uniform dissipation and polynomial \(p\)-dependence;
- the detailed Wang contraction transfer and degenerate DeTurck restart written independently of source shorthand.

Even after those components are supplied, the resulting theorem concerns the four-dimensional \(\operatorname{Ric}\approx-g\) Ishida–LeBrun family. The all-dimensional Yau-26 problem additionally requires the universal dimension-only constants, all smooth topologies, the other Ricci-sign regimes, dimensions outside four, and the requested Lean 4 formalization.