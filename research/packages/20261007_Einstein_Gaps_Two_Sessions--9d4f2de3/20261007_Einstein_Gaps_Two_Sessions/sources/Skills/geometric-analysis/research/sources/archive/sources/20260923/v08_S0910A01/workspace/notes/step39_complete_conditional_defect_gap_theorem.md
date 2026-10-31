> **Step 41 supersedes.** The corrected theorem is in `workspace/notes/step41_corrected_restricted_defect_gap_theorem.md`, incorporating all Step 40 Preceptor repairs and TTCS corrections.  A03 Step 43 independently resolved H-AO/H-UT and derived the terminal G density.  Only H-DT (DeTurck existence) remains.

> **Step 40 Preceptor update.** This Step 39 synthesis is a valuable proof architecture, not yet a rigorous theorem.  The review in `workspace/notes/step40_preceptor_review_step39_interfaces.md` found unresolved interfaces: support cutoffs should not assert sequence-uniform Hessian bounds from Ricci lower/mean-energy data; the `K_2` self-improvement must use the homogeneous Step 34 estimate rather than a bare additive `C_0T`; the normalized weighted-`U` and unweighted-`T` evolution formulae, including `G`, normalization, connection, and zero-order `T` propagation, still need full derivation before A03's staggered induction can be applied; the transported DeTurck start/restart requires the detailed Yang tame-estimate adaptation; terminal calibration must state `q>=0` or carry `q_-`; and the terminal pullback passage must use inner centers, Liouville--Rauch averaging, and strong finite-`W^{2,p}` convergence.  Treat the document below as superseded at these interfaces until those repairs are written.

# Step 39: Complete conditional defect gap theorem for the four-dimensional negative branch

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Overview

This note assembles all conditional pieces from Steps 1–38 (A01) and Steps 39–40
(A03) into a single end-to-end proof of a negative defect gap for near-critical
Ishida–LeBrun four-manifolds.  The argument is conditional on one analytic
hypothesis (H1) stated below.  The second hypothesis (H2) originally recorded by
TTCS is discharged within the proof using the Step 35 signed Hessian-\(a\) IBP.

**Hypothesis (H1): Per-datum degenerate DeTurck existence and restart.**
For any closed Riemannian four-manifold \((M,g_0)\) and smooth cutoff \(\chi\) with
\(\chi^2g_0\le g_0\), the transported-coefficient DeTurck system
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,
\qquad
\widehat a=a\circ\varphi_t^{-1},
\tag{H1}
\]
has a smooth solution on \([0,T_1)\) for some \(T_1>0\) depending on the
individual datum, with
\(\partial_t\varphi_t\circ\varphi_t^{-1}=-\widehat aW\).  Pulling back by
\(\varphi_t\) gives the fixed-cutoff flow
\(\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)\).  Furthermore, the construction
can restart from any smooth terminal metric.

This is the standard degenerate DeTurck construction of Yang (Theorem 4.1 in the
Wang–Yang pseudolocality paper) with the normalization \(+g\) as a smooth
bounded zeroth-order perturbation.  It does not change the degenerate parabolic
principal symbol.

## 1. Theorem statement

**Theorem 1.1 (Four-dimensional negative defect gap, conditional on (H1)).**
*There exist universal constants \(\varepsilon_4>0\), \(r_0>0\), \(\theta_0>0\)
with the following property.  Let
\[
M_i=X_i\#k_i\overline{\mathbb{CP}}^{\,2},
\qquad A_i=c_1^2(X_i)\to\infty,
\qquad k_i/A_i\to 1/3,
\]
be a near-critical Ishida–LeBrun sequence of closed oriented four-manifolds
carrying the monopole class structure.  Then for all sufficiently large \(i\),
every Riemannian metric \(g_i\) on \(M_i\) satisfies*
\[
\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_{\infty,\mathrm{op}}
\ge\varepsilon_4.
\]

In particular, these manifolds do not admit metrics with arbitrarily tight
negative Ricci pinching.

---

## 2. Near-critical calibration (Steps 2–8)

Assume for contradiction that \(\delta_i\to0\) with
\[
\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_{\infty,\mathrm{op}}<\delta_i.
\tag{2.1}
\]

### 2.1 Mixed Seiberg–Witten inequality

For each \(M_i\) and each sign choice \(\varepsilon\in\{-1,+1\}^{k_i}\),
writing \(a_\varepsilon=c_1(L_\varepsilon)\) for the corresponding monopole class,
\[
I_i:=\frac1{4\pi^2}\int_{M_i}\left(\frac{s_i^2}{24}+2|W_i^+|^2\right)d\mu_i
\ge\frac23(a_\varepsilon^+)^2.
\tag{2.2}
\]
Averaging over all \(2^{k_i}\) sign choices gives
\[
2^{-k_i}\sum_\varepsilon(a_\varepsilon^+)^2
=A_i+\sum_{j=1}^{k_i}(E_j^+)^2,
\tag{2.3}
\]
where \(E_j\) are exceptional classes.

### 2.2 Chern–Gauss–Bonnet and traceless Ricci

Define
\[
J_i=\frac1{4\pi^2}\int\frac{|\mathring{\operatorname{Ric}}_i|^2}{2},
\qquad q_i=k_i-\frac{A_i}3.
\tag{2.4}
\]
Chern–Gauss–Bonnet gives \(I_i-J_i=A_i-k_i\), hence
\[
D_{a,\varepsilon}:=I_i-\frac23(a_\varepsilon^+)^2
=J_i-q_i-\frac23\bigl((a_\varepsilon^+)^2-A_i\bigr).
\tag{2.5}
\]
Since \(|\mathring{\operatorname{Ric}}|\le C\delta_i\), we have
\(J_i\le C\delta_i^2\operatorname{Vol}_i\).

### 2.3 Near-critical regime

Averaging the defect and using (2.3), the boundary sequence satisfies
\[
q_i/A_i=O(\delta_i^2),
\qquad
\operatorname{Vol}_i/A_i\to\frac{32\pi^2}{9},
\qquad
J_i/A_i=O(\delta_i^2),
\qquad D_{a,\varepsilon}/A_i=O(\delta_i^2).
\tag{2.6}
\]
The volume ratio follows from the calibrated identity: near saturation,
\[
\frac{s^2}{24}+2|W^+|^2\to\frac34\qquad\text{in }L^1\text{-mean},
\]
so \(\frac34\operatorname{Vol}_i+o(A_i)=4\pi^2I_i\to\frac{8\pi^2}3A_i\).

### 2.4 Calibrated profiles

Completing the square:
\[
\int_{M_i}(s_i+8\sqrt6\,|W_i^+|)^2\,d\mu_i\le864\pi^2D_{a,\varepsilon}.
\tag{2.7}
\]
Near equality forces in the normalized mean:
\[
s_i\to-4,
\qquad
|W_i^+|^2\to\frac1{24},
\qquad
\operatorname{spec}(W_i^+)\to\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{2.8}
\]

### 2.5 Spectral gap function

With the eigenvalue labeling \(\alpha\ge\beta\ge w\), define
\[
f=\frac23s-2\sqrt{\frac23}\,|W^+|,
\qquad
b=\frac23s+2w,
\qquad
G=f^2-(b_-)^2\ge0.
\tag{2.9}
\]
Then
\[
\int_{M_i}G_i\le48\pi^2D_{a,\varepsilon}.
\tag{2.10}
\]

### 2.6 Mean full curvature bound

By 4D Chern–Gauss–Bonnet and \(\chi(M_i)\le CA_i+O(1)\):
\[
\overline K_{0,i}:=\frac1{\operatorname{Vol}_i}\int_{M_i}|\operatorname{Rm}_i|^2
\le C_1\frac{A_i}{\operatorname{Vol}_i}+C_2\delta_i^2
\le\overline K_0
\tag{2.11}
\]
for a universal constant \(\overline K_0\) (using
\(\operatorname{Vol}_i/A_i\ge c>0\) from (2.6)).

---

## 3. Support construction (Lemma)

**Lemma 3.1 (Selected macro-disjoint good supports).**
*Under (2.1) with \(\delta_i<\delta_*\), there exist a fixed radius
\(r\le r_0\), a universal integer \(N_{\rm col}\), and for each \(i\) a finite
collection \(\{(\chi_\alpha,\eta_\alpha)\}_{\alpha\in\mathcal C_i}\) of smooth
cutoff pairs on \(M_i\) such that:*

*(a) Each \(\chi_\alpha\) is supported in \(B_{5r}(x_\alpha)\) and equals \(1\)
on \(B_{2r}(x_\alpha)\), with \(\|d\chi_\alpha\|_\infty\le C/r\) and
\(\|\nabla^2\chi_\alpha\|_\infty\le C/r^2\).*

*(b) Each \(\eta_\alpha\) is supported in \(B_{7r}(x_\alpha)\) and equals \(1\)
on \(B_{5r}(x_\alpha)\).*

*(c) The buffered domains \(B_{7r}(x_\alpha)\) are pairwise disjoint.*

*(d) Each center satisfies*
\[
r^4\fint_{B_r(x_\alpha)}|\operatorname{Rm}_i|^2\le\varepsilon_0.
\]

*(e) The total plateau volume satisfies*
\[
\sum_{\alpha\in\mathcal C_i}\operatorname{Vol}(B_{2r}(x_\alpha))
\ge\alpha_0 A_i
\]
*for a universal \(\alpha_0>0\).*

**Proof.** Use the volume-average maximal function
\[
\mathcal M_Rf(x)=\sup_{0<s\le R}\fint_{B_s(x)}f.
\tag{3.1}
\]
Under \(\operatorname{Ric}\ge-2g\), Bishop–Gromov gives a local doubling constant
\(C_D(R)\) depending only on dimension and \(R\).  The weak maximal inequality
yields
\[
\operatorname{Vol}\bigl\{\mathcal M_R(|\operatorname{Rm}|^2)
>\Lambda\overline K_{0,i}\bigr\}
\le\frac{C_D}{\Lambda}\operatorname{Vol}(M_i).
\tag{3.2}
\]
Choose \(\Lambda=2C_D/\eta_0\) so the good set
\(G_R=\{\mathcal M_R(|\operatorname{Rm}|^2)\le\Lambda\overline K_0\}\)
has volume \(\ge\eta_0\operatorname{Vol}(M_i)\).

Choose \(r\) small enough that
\[
r^4\Lambda\overline K_0\le\varepsilon_0
\qquad\text{and}\qquad
C_{\rm Sob}\,r^2(1+\Lambda\overline K_0)^{1/2}\le\gamma_*.
\tag{3.3}
\]

Take a maximal \(14r\)-separated net \(\{x_\alpha\}\) in \(G_R\).  Then
\(G_R\subset\bigcup B_{14r}(x_\alpha)\).  The balls \(B_{7r}(x_\alpha)\) are
pairwise disjoint, establishing (c).

For coverage: \(G_R\subset\bigcup B_{14r}(x_\alpha)\), and Bishop–Gromov gives
\[
\frac{\operatorname{Vol}(B_{14r}(x))}{\operatorname{Vol}(B_{2r}(x))}
\le\frac{V_{-2}(14r)}{V_{-2}(2r)}=:D_7.
\tag{3.4}
\]
Therefore
\[
\eta_0\operatorname{Vol}(M_i)
\le\operatorname{Vol}(G_R)
\le\sum_\alpha\operatorname{Vol}(B_{14r}(x_\alpha))
\le D_7\sum_\alpha\operatorname{Vol}(B_{2r}(x_\alpha)),
\]
so
\[
\sum_\alpha\operatorname{Vol}(B_{2r}(x_\alpha))
\ge\frac{\eta_0}{D_7}\operatorname{Vol}(M_i)
\ge\frac{\eta_0}{D_7}\cdot\frac{32\pi^2}{9}\cdot\frac{A_i}{2}
=:\alpha_0 A_i,
\tag{3.5}
\]
where the last inequality uses \(\operatorname{Vol}(M_i)/A_i\ge c>0\) from
(2.6) for large \(i\).  This gives (e).

Property (d) follows from the maximal function bound at each center: for
\(x_\alpha\in G_R\),
\[
\fint_{B_r(x_\alpha)}|\operatorname{Rm}|^2
\le\mathcal M_R(|\operatorname{Rm}|^2)(x_\alpha)
\le\Lambda\overline K_0,
\]
so \(r^4\fint_{B_r}|\operatorname{Rm}|^2\le r^4\Lambda\overline K_0
\le\varepsilon_0\).  \(\square\)

**Remark.** If the downstream smoothing uses the unnormalized critical integral
\(\int_{B_r}|\operatorname{Rm}|^2\) rather than \(r^4\fint\), then Bishop–Gromov
upper volume gives
\(\int_{B_r}|\operatorname{Rm}|^2\le C_{\rm BG}r^4\Lambda\overline K_0\),
so the same choice of \(r\) supplies both forms.

---

## 4. First-exit bootstrap (Proposition)

### 4.1 Setup on a single support

Fix one support \((\chi_\alpha,\eta_\alpha)\) from Lemma 3.1.  Write
\(a=\chi_\alpha^2\), \(E=\operatorname{Ric}+g\), \(T=\operatorname{Rm}+G\),
\(U=aT\), \(F=(1+|\operatorname{Rm}|^2)^{1/2}\).  The localized energies are
\[
K_2^\eta=\int\eta^2F^2,
\qquad
Y=\int\eta^2aF^3,
\qquad
J_6=\int\eta^2a^4|E|^6.
\tag{4.1}
\]
The global defect is \(Q=\int_M|E|^2\).  The squared Sobolev constant is
\(\mathcal S\simeq r^2/\operatorname{Vol}(B_{5r})^{1/2}\), and the absorption
parameter is
\[
\gamma=\mathcal S\bigl(K_2^\eta(0)\bigr)^{1/2}
\le Cr^2(1+\Lambda\overline K_0)^{1/2}\le\gamma_*.
\tag{4.2}
\]

### 4.2 First-exit conditions

Define the first-exit time
\[
T_*=\sup\left\{T\le\theta r^2:\;
\text{(F1)--(F3) hold on }[0,T]\right\},
\tag{4.3}
\]
where
\begin{align}
&\text{(F1)}\quad K_2^\eta(t)\le 2K_2^\eta(0), \tag{F1} \\
&\text{(F2)}\quad e^{-\Lambda}g_0\le g(t)\le e^{\Lambda}g_0
\text{ on }\operatorname{supp}\eta, \tag{F2} \\
&\text{(F3)}\quad \mathcal S(t)\le 2\mathcal S(0). \tag{F3}
\end{align}

### 4.3 Existence and initial conditions

By hypothesis (H1), the flow
\(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\) exists smoothly on
\([0,T_1)\).  Since the initial data satisfies (F1)–(F3) strictly and the
quantities are continuous, \(T_*>0\).

### 4.4 Energy estimates on \([0,T_*)\) — the triangular chain

On \([0,T_*)\), all conditional energy estimates hold with parameters bounded by
universal constants times \(\gamma_*\).  The chain is strictly triangular (no
circular dependence, confirmed by Step 39 TTCS):

**Step A: \(K_2^\eta\) propagation.** From the curvature power inequality
(Step 34):
\[
(K_2^\eta)'\le C(1+r^{-2}+\mathcal S^2Y)K_2^\eta+C_0.
\tag{4.4}
\]

**Step B: Integrated potential \(B\).** By \(q=2\) interpolation (Step 34):
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta),
\]
hence \(\int_0^t\mathcal S^2Y\le C\gamma^3\) and
\[
B(t):=\int_0^t\mathcal S(s)^2Y(s)\,ds\le C\gamma^3.
\tag{4.5}
\]

**Step C: \(Y\) by good slice.** From \(B(t)\le C\gamma^3\), a good time
\(t_0\in[t/2,t]\) has \(\mathcal S^2Y(t_0)\le2C\gamma^3/t\).  Gronwall from
\(t_0\) gives
\[
Y(t)\le\frac{C\gamma K_2^\eta(0)}{t}.
\tag{4.6}
\]

**Step D: \(J_6\) persistence (unregularized, Step 34).** Using
\(s=|E|^2\), \(w_6=\eta\chi^5|E|^3\), two-factor Hölder gives
\(P_6\le C\gamma(X_6+r^{-2}J_6)\).  Small \(\gamma\) absorbs:
\[
J_6'+cX_6\le C(1+r^{-2})J_6,
\qquad
J_6(T)\le C\delta^6\operatorname{Vol}.
\tag{4.7}
\]

**Step E: General-\(p\) curvature and defect power inequalities (A03 Step 39).**
For \(f=F\) (curvature) and \(f=|E|\) (defect), with \(p\ge6\):
\[
H_p'+c\|\nabla z_p\|_2^2\le Cp^4(1+r^{-2}+\mathcal S^2Y)H_p.
\tag{4.8}
\]
No \(E\)-independent additive source.

**Step F: Weighted Moser endpoints (Steps 30–32).** Nested iteration
\(p_k=(3/2)^kp_0\) with the corrected interpolation
\(H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2\) gives, on positive-time slabs:
\[
\|aF(t)\|_\infty\le\frac{C\gamma}{t},
\qquad
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\tag{4.9}
\]

**Step G: \(|U|\) boundedness.** For any \(\tau>0\) and
\(t\in[\tau,T_*)\):
\[
|U(t)|=|a(t)(\operatorname{Rm}(t)+G(t))|
\le\|aF(t)\|_\infty+C
\le\frac{C\gamma}{\tau}+C<\infty.
\tag{4.10}
\]

### 4.5 Continuation

**Step H: All-order staggered continuation (A03 Step 40, TTCS-verified).**
Given \(\sup_{[\tau,T_*)}|U|<\infty\), the staggered induction
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\tag{4.11}
\]
gives \(\nabla^mU,\nabla^{m+1}\chi,\nabla^mT\in L^q\) for all finite
\(m,q\) on \([\tau,T_*)\).  The zero-order unweighted \(T\in L^q\) input is
supplied by the signed Hessian-\(a\) IBP (Step 35):
\[
\frac{d}{dt}\|T\|_p^p+c\int a|\nabla T|^2|T|^{p-2}
\le C(K+1+r^{-2})\|T\|_p^p+C_p,
\tag{4.12}
\]
which follows from the curvature power inequality with the reaction bounded by
\(|aT|=|U|\le K\).

**Step I: Terminal smoothness.** By Sobolev embedding (\(p>4\)) applied to
bounded \(W^{m,p}\) norms of all derivatives, all
\(\nabla^mU,\nabla^m\operatorname{Rm}\) are pointwise bounded on
\([\tau,T_*)\).  The velocity
\(\partial_tg=-2\operatorname{Ric}(U)\) and connection variation
\(\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)\) are uniformly bounded
with all derivatives.  The metric converges to a smooth positive definite limit
\(g(T_*)\).

**Step J: Restart.** By (H1), the flow restarts from \(g(T_*)\).  Therefore
\(T_*\) is not the maximal time: the flow extends past \(T_*\).

### 4.6 Self-improvement of first-exit conditions

**Self-improvement of (F1).** From (4.4) and \(B(t)\le C\gamma^3\):
\[
K_2^\eta(T_*)\le e^{C(1+r^{-2})T_*+CB(T_*)}K_2^\eta(0)+C_0T_*
\le e^{C\theta(1+1)+C\gamma_*^3}K_2^\eta(0)+C_0\theta r^2.
\tag{4.13}
\]
For \(\theta\le\theta_1\) and \(\gamma_*\le\gamma_1\) small enough,
\(K_2^\eta(T_*)<2K_2^\eta(0)\).

**Self-improvement of (F2).** The metric drift satisfies
\[
D(t):=\int_0^t\|aE(s)\|_\infty\,ds
\le C\delta_i\,r^{2/3}\int_0^ts^{-1/3}\,ds
=\frac32C\delta_i\,r^{2/3}\,t^{2/3}.
\tag{4.14}
\]
At \(t=T_*\le\theta r^2\):
\[
D(T_*)\le\frac32C\delta_i\theta^{2/3}r^2.
\tag{4.15}
\]
The logarithmic metric equivalence gives
\(e^{-2D}g_0\le g(t)\le e^{2D}g_0\).  For
\(\delta_i\theta^{2/3}\le\Lambda/(4C)\), (F2) is strictly satisfied.

**Self-improvement of (F3).** The Sobolev constant on the support satisfies
\[
\mathcal S(t)\le\mathcal S(0)\cdot e^{CD(t)}.
\tag{4.16}
\]
For \(D(T_*)\le c_0\) from (4.15), \(\mathcal S(T_*)<2\mathcal S(0)\).

### 4.7 Conclusion: \(T_*=\theta r^2\)

If \(T_*<\theta r^2\), then at time \(T_*\), (F1)–(F3) hold strictly, and
the flow extends past \(T_*\) by Steps H–J.  By continuity, (F1)–(F3) hold on
\([0,T_*+\varepsilon)\) for small \(\varepsilon\), contradicting the definition
of \(T_*\).  Therefore \(T_*=\theta r^2\).

**Proposition 4.1 (Conditional smoothing principle).**
*Under (H1) and Lemma 3.1, for each support the normalized cutoff flow exists
smoothly on \([0,\theta r^2]\), and at time \(T=\theta r^2\):*
\[
K_2^\eta(T)\le 2K_2^\eta(0),
\qquad
\|aE(T)\|_\infty\le C\delta_i,
\qquad
D(T)\le C\delta_i\theta^{2/3}r^2.
\tag{4.17}
\]

---

## 5. Global \(Q\) propagation

**Proposition 5.1.** *Under (H1), for the macro-disjoint supports of Lemma 3.1,
the global defect satisfies*
\[
Q(T)=\int_{M_i}|E(T)|^2\,d\mu_T
\le e^{C(1+r^{-2})T}Q(0).
\tag{5.1}
\]

**Proof.** By Lemma 3.1(c), the buffered domains \(B_{7r}(x_\alpha)\) are
pairwise disjoint.  On each support, the defect energy obeys (Step 36):
\[
q_\alpha'(t)\le C(1+r^{-2})q_\alpha(t)+\int F(\chi_\alpha E)^2.
\tag{5.2}
\]
The potential term is absorbed by
\(\int F(\chi E)^2\le C\gamma(X_\alpha+r^{-2}q_\alpha)\), and small \(\gamma\)
gives \(q_\alpha'\le C(1+r^{-2})q_\alpha\).

On the complement \(M\setminus\bigcup\operatorname{supp}\chi_\alpha\), the
metric is stationary, so \(q_0=\int_{M\setminus}|E|^2\) is constant.  Summing:
\[
Q'(t)=\sum_\alpha q_\alpha'(t)\le C(1+r^{-2})\sum_\alpha q_\alpha(t)
\le C(1+r^{-2})Q(t).
\tag{5.3}
\]
Gronwall gives (5.1).  At \(T=\theta r^2\),
\(Q(T)\le e^{C\theta(1+1)}Q(0)\le 2Q(0)\) for small \(\theta\).  \(\square\)

Since \(Q(0)=\int|E_0|^2\le C\delta_i^2\operatorname{Vol}_i\) and
\(\operatorname{Vol}_i=O(A_i)\):
\[
Q(T)/A_i\to 0\quad\text{as }\delta_i\to0.
\tag{5.4}
\]

---

## 6. Terminal recalibration (Step 28)

At time \(T=\theta r^2\), the terminal metric \(g_i(T)\) satisfies (4.17).
The mixed Seiberg–Witten inequality still holds for the terminal metric
(it depends on topology and orientation, not the specific metric, through
the a priori monopole estimate).  The terminal defect gives:
\[
\int(s_T+4)^2\le 4Q(T),
\qquad
J_T\le\frac{Q(T)}{8\pi^2}.
\tag{6.1}
\]
Repeating the completion-of-squares from §2:
\[
\int(s_T+8\sqrt6|W_T^+|)^2\le 108Q(T),
\qquad
\int G_T\le 6Q(T).
\tag{6.2}
\]
The combined calibration density is
\[
\mathfrak D=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G,
\qquad
\int_{M_i}\mathfrak D(T)\le 119Q(T).
\tag{6.3}
\]

---

## 7. Exponential pullback and Derdziński contradiction (Steps 8, 28)

### 7.1 Center selection via exponential pullback

On each plateau \(P_\alpha=B_{2r}(x_\alpha)\), the curvature at time \(T\) is
bounded: \(|\operatorname{Rm}(T)|\le\|aF(T)\|_\infty/\inf_{P_\alpha}a+C\).
Since \(a=1\) on the plateau:
\[
|\operatorname{Rm}(T)|\le C_F:=C\gamma/(\theta r^2)+C\quad\text{on }P_\alpha.
\tag{7.1}
\]
Choose \(\rho\) with \(C_F\rho^2\le1\) so that Rauch comparison controls the
exponential map on \(B_\rho(0)\subset T_pM_i\).  Then for any nonneg integrand
\(D\):
\[
\int_{P_\alpha}\fint_{B_\rho(0)}D(\exp_pv)\,dv\,dp
\le C(C_F,\rho)\int_{M_i}D.
\tag{7.2}
\]

Applying this to \(\mathfrak D(T)\) and using \(\int\mathfrak D(T)\le119Q(T)\)
and \(\sum_\alpha\operatorname{Vol}(P_\alpha)\ge\alpha_0A_i\):
\[
\alpha_0A_i\cdot
\min_\alpha\fint_{P_\alpha}\fint_{B_\rho(0)}\mathfrak D(\exp_pv)\,dv\,dp
\le C\cdot119\,Q(T).
\tag{7.3}
\]
Since \(Q(T)/A_i\to0\), for large \(i\) there exist \(\alpha_i\in\mathcal C_i\)
and \(p_i\in P_{\alpha_i}\) with
\[
\fint_{B_\rho(0)}\mathfrak D(T)(\exp_{p_i}v)\,dv\to0.
\tag{7.4}
\]

### 7.2 Tangent-space convergence

The pullback metric \(\widetilde g_i=(\exp_{p_i})^*g_i(T)\) on
\(B_\rho(0)\subset\mathbb R^4\) has bounded curvature (by (7.1)), bounded
\(C^{1,\alpha}\) from harmonic coordinate comparison, and vanishing mean
calibration density.  By standard \(W^{2,p}\) convergence (bounded Ricci,
\(C^{1,\alpha}\) metric, harmonic radius lower bound from curvature bound),
a subsequence converges in \(C^{1,\alpha}\) and weakly in \(W^{2,p}\) to a
limit metric \(\widetilde g_\infty\) on \(B_\rho(0)\).

The curvature eigenvalues, scalar curvature, \(|W^+|\), and spectral gap
\(G\) are Lipschitz in the metric coefficients.  Since
\(\fint\mathfrak D\to0\), the limit satisfies a.e.:
\[
E_\infty=0,
\qquad s_\infty=-4,
\qquad |W_\infty^+|^2=\frac1{24},
\qquad G_\infty=0.
\tag{7.5}
\]
The first equation means \(\operatorname{Ric}_{\widetilde g_\infty}
=-\widetilde g_\infty\): the limit is Einstein.  The last two equations
give \(\operatorname{spec}(W_\infty^+)=(-1/6,1/12,1/12)\).

### 7.3 The forbidden germ (Step 8)

By Derdziński Proposition 5 (1983), on an oriented Einstein four-manifold with
\(W^+\neq0\) and at most two distinct \(W^+\)-eigenvalues, the conformal metric
\[
(24|W^+|^2)^{1/3}g
\]
is locally Kähler.  At the calibrated profile:
- Einstein: \(\operatorname{Ric}=-g\);
- Two eigenvalues: \(\{-1/6,1/12,1/12\}\);
- \(|W^+|^2=1/24\): the conformal factor is constant.

So \(\widetilde g_\infty\) is locally Kähler with
\(\operatorname{Ric}=-g\).  But any Kähler–Einstein metric with
\(\operatorname{Ric}=-g\) in four dimensions has
\(|W^+|^2=s^2/24=16/24=2/3\neq1/24\).

**Contradiction.** \(\square\)

---

## 8. Status and scope

### What is proved (conditional on (H1)):

The Ishida–LeBrun near-critical family has a uniform negative defect gap: no
sequence \(\delta_i\to0\) is possible.  This is a partial result consistent with
a positive answer to Yau Problem 26 in the negative branch of dimension four.

### What (H1) requires:

A standard DeTurck short-time existence and restart theorem for the degenerate
equation \(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\), adapting Yang's Theorem
4.1.  The normalization \(+g\) is a smooth bounded zeroth-order perturbation
that does not change the degenerate parabolic principal symbol.  This is a
plausible but not yet independently verified adaptation.

### What is NOT addressed:

1. **Positive branch** (\(\operatorname{Ric}\approx+g\)): open.
2. **Arbitrary four-manifold topology**: the current proof uses the Ishida–LeBrun
   monopole structure specifically.
3. **Dimensions \(n\ge5\)**: no analogue of SW, \(W^+\), or Derdziński.
4. **Dimension-only constants**: the current \(\varepsilon_4\) depends on the
   mean curvature bound, not only on dimension.
5. **Lean 4 formalization**: no formalizable theorem yet.

### File dependencies:

| Module | Steps | Reference |
|:---|:---:|:---|
| Near-critical calibration | 2–8 | §2 |
| Spectral gap and forbidden germ | 5–8 | §2.5, §7.3 |
| Support construction | 38 | §3, Lemma 3.1 |
| Curvature power inequality | 33–35 | §4.4 Step A |
| Fixed-exponent K₂→Y→J₆ | 34 | §4.4 Steps B–D |
| General-p defect inequality | A03-39 | §4.4 Step E |
| Weighted Moser endpoints | 30–32 | §4.4 Step F |
| All-order continuation | A03-40 | §4.5 Step H |
| Signed Hessian-a IBP | 35 | §4.5 (eqn 4.12) |
| Global Q propagation | 36 | §5 |
| Terminal recalibration | 28 | §6 |
| Exponential pullback | 28 | §7.1–7.2 |
| Derdziński Prop 5 | 8 (source) | §7.3 |
