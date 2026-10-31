# Step 58: All-order current-pair continuation — proof-level note

> **Step 59 refinement.** The Hölder residual estimate, signed-Hessian integration,
> and autonomous splice mechanisms in this note remain useful, but the dependency
> summary in §10 was too strong. Step 59 shows that the differentiated tensor
> hierarchy still needs an explicit source-by-source ledger, a non-circular base
> package, exact derivative-reordering lemmas, and strict triangular
> fixed-background conversion. Do not cite this file as proving that only the
> per-datum local existence input remains.

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and scope

This note writes the proof-level continuation component for the restricted
four-dimensional negative Ishida–LeBrun cutoff-flow theorem.  It starts from
the per-datum exact-flow construction (A03 Step 56), the coupled
\((\Gamma,V)\) first-exit bootstrap (A01 Step 55), the curvature Moser endpoint
(A03 Step 58), the defect Moser endpoint (A01 Step 34), and the finite restart
threshold (A01 Step 55).  It corrects the two substantive errors identified in
A01 Step 57 and the TTCS reviews:

1. The base \(T,U\) structural equations carry no independent constant forcing.
2. The all-order induction starts from the already established base layer at
   \(m=2\), not at \(m=1\).

The conclusion is a smooth terminal metric \(g_*\) and an autonomous-equation
splice across the observation time, with no uniqueness statement used.  Terminal
compactness is in A01 Step 56 §4–§5.  The full chain remains restricted to a
four-dimensional negative IL geography and does not settle Yau Problem 26.

---

## 1. Setup and notation

On a closed four-manifold \((M^4,g_0)\) with a smooth fixed cutoff
\(\chi:M\to[0,1]\), the exact cutoff flow is
\[
 \partial_tg=-2a(\operatorname{Ric}_g+g)=-2\operatorname{Ric}(U),
 \qquad a=\chi^2.
\tag{1.1}
\]
Define the shifted curvature tensor, its weighted form, and their jets:
\[
 T=\operatorname{Rm}+G,\qquad G=\frac{g\owedge g}{6},\qquad U=aT,
\tag{1.2}
\]
\[
 T_m=\nabla^mT,\quad U_m=\nabla^mU,\quad
 C_j=\nabla^j\chi,\quad B_j=\nabla^ja=\nabla^j(\chi^2).
\tag{1.3}
\]
Here \(n=4\), so \(2(n-1)=6\).  On a positive-time slab \([\tau,T_*)\) with
\(\tau>0\), the flow produces a smooth family of metrics satisfying the
first-exit bootstrap bounds.

---

## 2. Corrected base equations and stationarity

### 2.1 Stationarity principle

If \(T\equiv0\), then \(\operatorname{Rm}=-G\) (under the legacy
\(T=\operatorname{Rm}+G_{\rm old}\); **Step 64 sweep note:** this display is
self-referential in the symbol \(G\) and hence vacuous — under the canonical
\(T=\operatorname{Rm}-G\) it reads \(\operatorname{Rm}=+G\); the substantive
point is the next clause), so \(\operatorname{Ric}=-g\), so
\(E=\operatorname{Ric}+g=0\) and the flow is stationary:
\(\partial_tg=0\). Consequently \(\partial_tT=0\) and \(\partial_tU=0\).
Every term in the structural equations must therefore vanish at \(T=U=0\).
This is the source of the correction to A03 Step 60 eqs (1.5)–(1.6).

### 2.2 The \(T\)-equation

The Riemann variation under (1.1), combined with the second Bianchi identity
and the algebraic \(\partial_tG\) expression, gives the structural equation
\[
 \partial_tT
 =a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T).
\tag{2.1}
\]
Here the star-products denote universal linear combinations of metric
contractions with coefficients depending on \(g\) and its inverse.  The
linear term \(aT\) records the universal zero-order reaction after rewriting
\(\operatorname{Rm}=T+G\) in the canonical Step 63 convention (equivalently
\(\operatorname{Rm}=T-G_{\rm old}\) in the legacy convention); it is schematic
and may absorb dimensional constant tensors into \(a(T+T*T)\) because
\(F_T\ge1\).  The quadratic \(a(T*T)\) comes from the standard Rm*Rm reaction.
At \(T=0\): every displayed term vanishes.  There is no independent
\(a\cdot1\) or \(a\cdot G\) forcing term.

### 2.3 The \(U\)-equation

Since \(a=\chi^2\) is a fixed spatial function, \(\partial_ta=0\), hence
\(\partial_tU=a\,\partial_tT\).  Using the Laplacian product rule
\[
 \Delta(aT)=a\Delta T+2\nabla a\cdot\nabla T+(\Delta a)T,
\tag{2.2}
\]
and the gradient identity \(\nabla U=a\nabla T+(\nabla a)*T\), a direct
computation converts (2.1) to
\[
 \partial_tU
 =\operatorname{div}(a\nabla U)+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU.
\tag{2.3}
\]
The principal operator is \(\operatorname{div}(a\nabla U)=a\Delta U+B_1*\nabla U\).
The term \(a^2(T*T)\) rewrites as \((aT)*(aT)=U*U\).  The linear term
\(a^2T=aU\).  The remaining drift terms come from rewriting the Laplacian
and gradient conversions.  At \(T=U=0\): every term vanishes.  There is no
independent \(a^2\) forcing.

### 2.4 The key identity removing apparent unweighted terms

The term \((B_1*B_1)*T\) appears unweighted in \(T\).  Since
\(B_1=\nabla(\chi^2)=2\chi C_1\), every concrete contraction satisfies
\[
 (B_1*B_1)*T=4\chi^2(C_1*C_1)*T=4(C_1*C_1)*U.
\tag{2.4}
\]
No division by \(a\) is performed; the identity is algebraic and holds
globally.  After this replacement, (2.3) becomes
\[
 \partial_tU
 =\operatorname{div}(a\nabla U)+B_1*\nabla U+B_2*U
 +4(C_1*C_1)*U+U*U+aU.
\tag{2.5}
\]
Every coefficient of \(U\) on the right side is bounded on a controlled slab.
No naked \(T\) appears in the \(U\)-equation after this identity is applied.

---

## 3. Imported base layer (source order refined by Step 59)

> **Step 59 correction.** This section should not be read as a self-contained
> base proof.  The correct non-circular order is
> \((U_0\in L^\infty, T_0\in L^q_{\rm fin})\to(U_1,C_2)\to T_1\to
> T_0\in L^\infty\), after which the general `m>=2` induction begins.  The
> `W^{1,p}\to L^\infty` step is an output of `T_1` control, not an input that
> proves `T_1,U_1,C_2`.

The following finite-exponent bounds are the intended imported base package on
\([\tau,T_*)\) with \(\tau>0\):

\[
\boxed{
\begin{aligned}
&\|U\|_\infty=\|aT\|_\infty\le K_\tau<\infty,\\
&T_0=T,\quad T_1=\nabla T,\quad
 U_1=\nabla U,\quad C_2=\nabla^2\chi
 \quad\in L_t^\infty L_x^q
 \quad\forall\, q<\infty.
\end{aligned}}
\tag{3.1}
\]

**Current status of the sources:**

- \(\|aT\|_\infty\): supplied by the curvature Moser endpoint
  \(\|aF_T(t)\|_\infty\le C\Gamma/t\) on positive time.
- \(T_0\in L^q\) for all finite \(q\): an unweighted finite-exponent seed is
  needed before the base pair; it must not be replaced by pointwise curvature.
- \((U_1,C_2)\in L^q\): requires the special base-pair estimate with the
  signed-Hessian treatment of the \(m=1\) contraction.
- \(T_1\in L^q\): follows only after the base pair has been controlled.
- \(T_0\in L^\infty\): follows after \(T_0,T_1\in L^p\), \(p>4\), by Kato and
  Sobolev embedding on the per-datum positive-time slab.

> **Step 60 update.** The base package is now established in
> `workspace/notes/step60_base_pair_proof.md`.  The C₂ evolution is
> `∂ₜC₂=g^{-1}*U₁*C₁` (no U₂), all m=1 Hessian terms have the A03
> signed-Hessian form, and the coupled (U₁,C₂) Grönwall closes
> non-circularly from the imported zero-order inputs.  T₁ and
> T₀∈L^∞ follow in the correct source order.  Six TTCS repairs
> incorporated; structural verification 15/15.

The base package is therefore established by the Step 60 proof, not by
the general `m>=2` mechanism in this file.
---

## 4. General current-pair induction (\(m\ge2\))

### 4.1 Derivative families at level \(m\)

Applying \(\nabla^m\) to (2.1), using the spatial commutator identity
\[
 [\nabla^m,\Delta]A
 =\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA,
\tag{4.1}
\]
and the coordinate-time commutator
\[
 \partial_t(\nabla^mA)
 =\nabla^m(\partial_tA)
 +\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA,
\tag{4.2}
\]
with \(\nabla^r(\partial_t\Gamma)=g^{-1}*U_{r+1}\) plus curvature
reorderings that introduce \(T_q*U_{r-q}\) with \(q\le r-1\le m-2\),
the \(U_m\)-equation takes the form
\[
 \partial_tU_m
 =\operatorname{div}(a\nabla U_m)
 +\mathcal T_{m}^{U}+\mathcal P_m^U.
\tag{4.3}
\]

The **current-order top terms** \(\mathcal T_m^U\) are:
\[
\begin{array}{ll}
 \chi C_{m+2}*U_0, & \text{(top cutoff)}\\
 \chi C_{m+1}*U_1, & \text{(next cutoff)}\\
 C_1*C_{m+1}*U_0, & \text{(from }(U3)\text{ extremal)}\\
 C_1*C_1*U_m, & \text{(from }(U3)\text{ extremal)}\\
 \chi C_2*U_m, & \text{(current signed Hessian)}\\
 B_1*\nabla U_m, & \text{(absorbed into principal)}
\end{array}
\tag{4.4}
\]
The term \(B_1*\nabla U_m=2\chi C_1*\nabla U_m\) is absorbed into the
divergence operator and never separated.

The **strict lower-order remainder** \(\mathcal P_m^U\) contains:
\[
\begin{array}{ll}
 B_r*U_{m+2-r},\quad 2\le r\le m+2, & \text{(drift on prior levels)}\\
 C_{r+1}*C_{s+1}*U_t,\quad r+s+t=m,\ t<m, & \text{(prior U3)}\\
 U_i*U_j,\quad i+j=m,\ i,j<m, & \text{(prior U4)}\\
 B_\ell*\nabla^r\operatorname{Rm}*U_s,\quad \ell\ge1,\ \ell+r+s=m, & \text{(spatial comm.\ with coeff.)}\\
 a\operatorname{Rm}*U_m, & \text{(spatial comm.\ }\ell=0\text{, bounded coeff.)}\\
 U_{r+1}*U_s,\quad r+s=m-1,\ r+1\le m-1, & \text{(time comm.)}\\
 T_q*U_{r-q}*U_s,\quad q\le m-2, & \text{(time reordering)}\\
 B_r*U_{m-r},\quad 0\le r\le m, & \text{(linear drift from }aU\text{)}
\end{array}
\tag{4.5}
\]
Every factor in \(\mathcal P_m^U\) involves only:
- previous \(U_j\) with \(j<m\) (known inductively in \(L^q\));
- cutoff jets \(C_\ell\) with \(\ell\le m\) (known inductively);
- bounded zero-order coefficients \(U_0,T_0,g^{-1}\);
- or the current \(U_m\) multiplied by bounded coefficients.

**Why \(aT_m\) never appears unweighted.**  The Leibniz identity
\[
 U_m=\nabla^m(aT)=aT_m+\sum_{q=1}^m\binom{m}{q}B_q*T_{m-q}
\tag{4.6}
\]
gives
\[
 aT_m=U_m-\sum_{q=1}^m\binom{m}{q}B_q*T_{m-q}.
\tag{4.7}
\]
Every unweighted \(T\)-factor on the right side has index at most \(m-1\).
When the spatial commutator at \(\ell=0\) produces
\(a\nabla^r\operatorname{Rm}*U_s\) with \(r+s=m\) and \(r=m\), we have
\(a\nabla^m\operatorname{Rm}=a(T_m-\nabla^mG)\) and \(\nabla^mG=0\) for
\(m\ge1\), so \(aT_m*U_0=U_m*U_0+\text{lower}\) after using (4.7).
No bare \(T_m\) survives outside bounded-coefficient or previous-level
products.

### 4.2 The cutoff jet equation

For the fixed scalar \(\chi\), the coordinate-time commutator gives
\[
 \partial_tC_{m+1}
 =C_1*U_m+\sum_{1\le j<m}C_{m+1-j}*U_j
 +\mathcal R_m,
\tag{4.8}
\]
where \(\mathcal R_m\) contains curvature reorderings and products of
strictly prior curvature and cutoff levels.  Critically, there is no
\(U_{m+1}\) or \(C_{m+2}\) in (4.8), because differentiation of
\(\partial_t\Gamma=g^{-1}*U_1\) raises \(U\) by one order while the
cutoff is lowered by one order.

---

## 5. Energy closure at level \(m\ge2\)

### 5.1 Weighted pair energy

Fix a finite exponent \(p\ge2\) and work on \([\tau,T_*)\).  Set
\[
 V=U_m,\qquad Z=C_{m+1},\qquad
 D_{m,p}^U=\int a|\nabla V|^2|V|^{p-2}.
\tag{5.1}
\]

**Testing the weighted equation against \(|V|^{p-2}V\):**

\(\bullet\) **Principal operator.**
\[
 \int|V|^{p-2}V*\operatorname{div}(a\nabla V)
 =-c_pD_{m,p}^U.
\tag{5.2}
\]
The term \(B_1*\nabla V\) is never separated from the divergence; its
energy contribution is the cross term in the integration by parts, absorbed
by
\[
 \frac{|B_1|^2}{a}=4|C_1|^2,
\tag{5.3}
\]
which is bounded.

\(\bullet\) **Top cutoff term \(\chi C_{m+2}*U_0\).**
Integrate by parts once, using \(C_{m+2}=\nabla C_{m+1}+\text{connection
terms}\):
\[
\begin{aligned}
 &\int|V|^{p-2}V*\chi C_{m+2}*U_0\\
 &\quad=-\int\nabla(|V|^{p-2}V)*\chi Z*U_0\\
 &\qquad-\int|V|^{p-2}V*C_1*Z*U_0\\
 &\qquad-\int|V|^{p-2}V*\chi Z*U_1\\
 &\qquad+\text{lower connection terms}.
\end{aligned}
\tag{5.4}
\]
- First line: \(|\nabla(|V|^{p-2}V)|\le(p-1)|V|^{p-2}|\nabla V|\).
  The integral is bounded by
  \(\varepsilon D_{m,p}^U+C(\|Z\|_p^p+\|V\|_p^p)\) using
  \(\|U_0\|_\infty\le K\).
- Second line: \(C_1\) and \(U_0\) are bounded, so this is
  \(\le C(\|Z\|_p^p+\|V\|_p^p+1)\) by Young.
- Third line: this is the critical residual
  \[
   I_m=\int\chi|Z|\,|U_1|\,|V|^{p-1}.
  \tag{5.5}
  \]

### 5.2 Absorption of the critical residual (\(m\ge2\))

Define \(f=\chi|V|^{p/2}\).  The local Sobolev inequality on the support
gives
\[
 \|f\|_4^2\le C_S\bigl(p^2D_{m,p}^U+C_{p,r}\|V\|_p^p\bigr).
\tag{5.6}
\]
Apply Hölder with exponents \((4,p,4,2p/(p-2))\) when \(p>2\):
\[
 I_m\le\|f\|_4\,\|Z\|_p\,\|U_1\|_4\,\|V\|_p^{p/2-1}.
\tag{5.7}
\]
(For \(p=2\), use exponents \((4,2,4)\).)  Since \(m\ge2\), the factor
\(\|U_1\|_4\) is a **base-layer quantity** (not a current unknown).  Young
gives
\[
 I_m\le\varepsilon D_{m,p}^U
 +C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{5.8}
\]
Here \(C_{m,p,\tau}\) depends on the per-datum base norms
\(\|U_1\|_{L^4}\), the Sobolev constant \(C_S\) of \(g(\tau)\), and the
cutoff scale \(r\).

**Why this fails at \(m=1\).**  When \(m=1\), the critical residual
becomes \(I_1=\int\chi|C_2|\,|U_1|^p\).  Now \(V=U_1\) is the current
unknown, not a base-layer quantity.  The factor \(\|U_1\|_4\) in (5.7) is
the very quantity being estimated, so Young cannot close linearly.  This is
why the base layer (3.1) must be established independently (by the
curvature/defect Moser endpoints and the \(W^{1,p}\) bridge), and the
induction begins at \(m=2\).

### 5.3 Signed-Hessian integration

The current term \(\chi C_2*U_m\) is not a bounded coefficient: \(C_2\)
is known only in finite \(L^q\).  Its energy contribution is a tensor
contraction
\[
 J_m=\int\chi(\nabla^2\chi)_{ij}\,\mathcal B^{ij}(V),
 \qquad |\mathcal B|\lesssim|V|^p,\
 |\nabla\mathcal B|\lesssim p|V|^{p-1}|\nabla V|.
\tag{5.9}
\]
Since \(C_2=\nabla C_1+\text{lower}\), integrate by parts:
\[
 |J_m|\le C\int|C_1|^2|V|^p
 +Cp\int\chi|C_1||V|^{p-1}|\nabla V|
 \le\varepsilon D_{m,p}^U+C\|C_1\|_\infty^2\|V\|_p^p.
\tag{5.10}
\]
Thus the Hessian term is closed using only \(\|C_1\|_\infty=\|\nabla\chi\|_\infty
\le Cr^{-1}\), never an \(L^\infty\) bound on \(C_2\).

### 5.4 Current-pair Grönwall

The \(C_1*C_1*U_m\) term from (4.4) is bounded-coefficient and gives
\(\le C\|C_1\|_\infty^2\|V\|_p^p\).  The remaining terms in
\(\mathcal P_m^U\) involve prior quantities in finite exponents against
\(|V|^{p-1}\); Hölder/Young closes them with per-datum constants.

Testing (4.8) against \(|Z|^{p-2}Z\) and using the base:
\[
 {d\over dt}\|Z\|_p^p
 \le C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{5.11}
\]
Adding (5.8), (5.10), (5.11), and the lower-order contributions:
\[
 \boxed{
 {d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
 +cD_{m,p}^U
 \le C_{m,p,\tau}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).}
\tag{5.12}
\]
Grönwall gives
\[
 \|U_m(t)\|_p^p+\|C_{m+1}(t)\|_p^p\le C_{m,p,\tau}\quad\forall\,t\in[\tau,T_*),
\tag{5.13}
\]
for every finite \(p\).

---

## 6. Unweighted curvature recovery at level \(m\)

After (5.13) is established for the pair \((U_m,C_{m+1})\), the
unweighted \(T_m\) equation is
\[
 \partial_tT_m
 =a\Delta T_m+B_1*\nabla T_m+B_2*T_m
 +2\chi C_{m+2}*T_0+\chi C_{m+1}*T_1
 +\chi C_2*T_m+\mathcal S_m,
\tag{6.1}
\]
where \(\mathcal S_m\) is lower-order in the same sense as \(\mathcal P_m^U\).

**Top cutoff term.**  Integration by parts on \(\chi C_{m+2}*T_0\) reduces
to the residual
\[
 \widetilde I_m=\int\chi|C_{m+1}|\,|T_1|\,|T_m|^{p-1}.
\tag{6.2}
\]
By the same Hölder–Sobolev argument as (5.7)–(5.8), using
\(T_1\in L^4\) (base layer) and the just-completed \(C_{m+1}\in L^p\):
\[
 \widetilde I_m\le\varepsilon D_{m,p}^T
 +C_{m,p,\tau}\bigl(1+\|C_{m+1}\|_p^p+\|T_m\|_p^p\bigr).
\tag{6.3}
\]

**Weighted-to-unweighted conversion.**  When \(a\operatorname{Rm}*T_m\)
appears via spatial commutators, use
\[
 aT_m=U_m-\sum_{q=1}^m\binom{m}{q}B_q*T_{m-q}
\tag{6.4}
\]
to replace \(aT_m\) with the known \(U_m\) plus strictly prior unweighted
terms.

**Signed Hessian** \(\chi C_2*T_m\): same integration by parts as (5.10)
with \(T_m\) in place of \(U_m\).

Combined:
\[
 \boxed{
 {d\over dt}\|T_m\|_p^p+cD_{m,p}^T
 \le C_{m,p,\tau}\bigl(1+\|T_m\|_p^p\bigr).}
\tag{6.5}
\]

### Induction summary

For every \(m\ge2\) and every finite \(p\):
\[
 T_0\xrightarrow{\text{base}}\
 (U_1,C_2)\xrightarrow{\text{base}}\
 T_1\xrightarrow{\text{base}}\
 (U_2,C_3)\xrightarrow{(5.12)}\
 T_2\xrightarrow{(6.5)}\
 (U_3,C_4)\xrightarrow{(5.12)}\
 T_3\to\cdots
\tag{6.6}
\]
The first three arrows use the independently established base layer (3.1).
Every subsequent arrow uses the general mechanism proved above, starting at
\(m=2\).  The constants \(C_{m,p,\tau}\) are per-datum; they are not used
in the sequence-uniform first-exit estimates.

---

## 7. Fixed-background connection conversion

### 7.1 Setup

Fix \(\bar g=g(\tau)\) and \(\bar\nabla=\nabla^{g(\tau)}\).  The connection
difference is
\[
 A=\nabla^{g(t)}-\bar\nabla,\qquad
 A_{ij}^k=\tfrac12g^{kl}(\bar\nabla_ig_{jl}+\bar\nabla_jg_{il}-\bar\nabla_lg_{ij}).
\tag{7.1}
\]

### 7.2 Triangular evolution

Coordinate-time differentiation gives
\[
 \partial_tA=g^{-1}*\nabla^{g(t)}(aE)
 =g^{-1}*U_1+\text{lower}(A,U_0,g^{-1}).
\tag{7.2}
\]
At level \(m\), applying \(\bar\nabla^m\) and converting between
\(\bar\nabla\) and \(\nabla^{g(t)}\):
\[
 \bar\nabla^m\partial_tA
 =g^{-1}*U_{m+1}+B_0^A*A_m
 +P_m(A_{<m},\,U_{\le m},\,g^{-1}),
\tag{7.3}
\]
where \(A_m=\bar\nabla^mA\) and \(B_0^A\) is a bounded linear coefficient
from the metric and its inverse.  The \(B_0^A*A_m\) term is linear and
poses no problem for Grönwall.  The key structural property is that
\(U_{m+1}\) is the top forcing, and no \(A_{m+1}\) appears on the right
side.

### 7.3 Conversion between derivatives

For any tensor \(\Psi\),
\[
 \nabla^{g(t)}\Psi=\bar\nabla\Psi+A*\Psi.
\tag{7.4}
\]
At higher orders,
\[
 \nabla^{g(t),m}\Psi
 =\bar\nabla^m\Psi
 +\sum_{\ell=1}^m\bar\nabla^{\ell-1}A*\bar\nabla^{m-\ell}\Psi
 +\text{multi-products with lower }A.
\tag{7.5}
\]
In particular, \(U_{m+1}=\nabla^{g(t),m+1}U\) involves
\(\bar\nabla^{m+1}U\) plus products of \(A_{\le m}\) and
\(\bar\nabla^{\le m}U\).  But \(\bar\nabla^{m+1}U\) is not directly
available.  The triangular structure means we solve for \(A_m\) from (7.3),
using the already known \(U_{m+1}\) from the evolving-derivative induction.

### 7.4 Induction for fixed-background bounds

Given the all-order evolving-derivative bounds from §6, proceed by induction
on \(m\):

- \(m=0\): (7.2) gives \(\partial_tA=g^{-1}*U_1+\text{lower}\),
  so \(\|A(t)\|_{L^p}\le C_\tau\) from \(U_1\in L_t^\infty L_x^p\).
- \(m\to m+1\): assume \(A_0,\ldots,A_m\in L_t^\infty L_x^p\).
  Equation (7.3) at level \(m+1\) gives
  \[
   \bar\nabla^{m+1}\partial_tA=g^{-1}*U_{m+2}+B_0^A*A_{m+1}+\text{known}.
  \tag{7.6}
  \]
  Thus \(\partial_tA_{m+1}\in L_t^\infty L_x^p\) from \(U_{m+2}\in L_t^\infty L_x^p\)
  (the evolving tower) and the inductive hypothesis.  Grönwall on \(\|A_{m+1}(t)\|_p^p\)
  gives the bound.

The metric itself satisfies
\[
 \bar\nabla g=A*g,\qquad
 \bar\nabla^{m+1}g=(\bar\nabla^mA)*g+\text{lower products},
\tag{7.7}
\]
so fixed-background \(H^s\) control of \(g\) follows from \(A_0,\ldots,A_{s-1}\in L^p\).

### 7.5 \(H^s\) convergence

For the time derivative,
\[
 \partial_tg=-2\operatorname{Ric}(U),
\tag{7.8}
\]
which in fixed-background coordinates gives
\[
 \|\partial_tg\|_{H^s(\bar g)}\le C_s\bigl(\|U\|_{H^{s+1}(\bar g)}+\|A\|_{H^s}*\cdots\bigr)<\infty.
\tag{7.9}
\]
Therefore \(g(t)\) is Cauchy in every \(H^s(\bar g)\) as \(t\uparrow T_*\),
and
\[
 g(t)\longrightarrow g_*\quad\text{in }H^s(\bar g)\quad\forall\,s.
\tag{7.10}
\]
Since \(H^s(M^4)\hookrightarrow C^k(M^4)\) for \(s>k+2\), the convergence
is in \(C^\infty(M)\).

---

## 8. Positive-definite terminal metric and autonomous splice

### 8.1 Positive definiteness of \(g_*\)

The metric velocity satisfies \(\|\partial_tg\|_{g,\mathrm{op}}\le
2\|aE\|_{g,\mathrm{op}}\).  From the defect Moser endpoint,
\[
 \|aE(t)\|_\infty\le C_E\delta\left(\frac{r^2}{t}\right)^{1/3},
\tag{8.1}
\]
which is integrable on \([\tau,T_*)\).  Therefore
\[
 e^{-2V_*}\,g(\tau)\le g(t)\le e^{2V_*}\,g(\tau),
 \qquad V_*=\int_\tau^{T_*}\|aE\|_\infty\,ds<\infty,
\tag{8.2}
\]
and \(g_*\) is positive definite.  The \(C^\infty\) convergence of
\(g(t)\to g_*\) makes \(g_*\) a smooth Riemannian metric.

### 8.2 Autonomous time-jet matching

The cutoff flow is autonomous: its right-hand side depends only on the
current spatial metric and the fixed \(\chi\), not explicitly on time.
Define the flow map recursively:
\[
 \mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g),
 \qquad
 \mathcal F_{\ell+1}(g)=D\mathcal F_\ell(g)[\mathcal F(g)].
\tag{8.3}
\]
Each \(\mathcal F_\ell\) depends on a finite spatial jet of \(g\) and the
fixed \(\chi\).  For the old branch \(g(t)\), \(t<T_*\):
\[
 \partial_t^\ell g(t)=\mathcal F_\ell(g(t))
 \longrightarrow\mathcal F_\ell(g_*)\quad\text{in }C^\infty,
\tag{8.4}
\]
using the \(C^\infty\) convergence of \(g(t)\) and continuity of \(\mathcal F_\ell\) in smooth topology.

Apply the per-datum local existence theorem (A03 Step 56) to the smooth
positive metric \(g_*\).  Any smooth solution \(\hat g(s)\), \(s\in[0,\epsilon)\),
with \(\hat g(0)=g_*\) satisfies
\[
 \partial_s^\ell\hat g(0)=\mathcal F_\ell(g_*)
 \quad\forall\,\ell\ge1.
\tag{8.5}
\]
Define the spliced solution:
\[
 \widetilde g(t)=
 \begin{cases}
 g(t), & t<T_*,\\
 g_*, & t=T_*,\\
 \hat g(t-T_*), & t>T_*.
 \end{cases}
\tag{8.6}
\]
By (8.4) and (8.5), the left and right time jets of every order match at
\(T_*\).  Together with the \(C^\infty\) convergence from both sides,
\(\widetilde g\) is a smooth solution across \(T_*\).  **No overlap
uniqueness or comparison of two solutions on the same interval is used.**

### 8.3 Continuation past the common time

If the first-exit bootstrap bounds remain valid at \(T_*\), the spliced
solution extends to \([0,T_*+\epsilon)\).  This contradicts the assumption
that \(T_*\) was the supremum of the existence interval satisfying the
bootstrap.  Hence \(T_*\ge\theta r^2\) for any sequence datum satisfying the
initial smallness condition.

The constants in §§4–8 are per-datum.  They ensure that every individual
datum reaches the common observation time \(\theta r^2\).  The common-time
and terminal-compactness mechanism (A01 Step 56 §§3–5) uses only the
sequence-uniform first-exit outputs and the terminal Seiberg–Witten
recalibration.

---

## 9. Interface to the terminal contradiction

The terminal chain, assembled in A01 Step 56 §§3–5, uses:

1. **Terminal recalibration:** \(g_i(T)\) lives on the same smooth manifold,
   so the monopole inequality applies to \(g_i(T)\).  The terminal defect
   \(Q_i(T)=\int|E_i|^2\) is controlled by the global \(Q\)-propagation.

2. **Terminal density:** with \(q_{\rm top}\ge0\),
   \[
    \int\Phi_i\le119Q_i(T),
    \qquad\Phi_i=|E_i|^2+(s_i+4)^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i\ge0.
   \tag{9.1}
   \]

3. **Liouville pullback selection:**
   \[
    \operatorname{Vol}(P_i)\ge c_0A_i,\qquad
    \int\Phi_i\le C\delta_i^2A_i
    \implies
    \exists\,p_i\in P_i:\
    \mathcal A_\rho\Phi_i(p_i)\le Cc_0^{-1}\delta_i^2.
   \tag{9.2}
   \]

4. **Pullback \(W^{2,q}_{\rm loc}\) compactness:** bounded curvature on
   pullback balls, Rauch noncollapse, harmonic coordinates, and
   \(\Phi_i\to0\) in \(L^1_{\rm loc}\) give a smooth Einstein limit with
   \(\Phi_\infty\equiv0\).

5. **Derdziński forbidden germ:** the calibrated spectrum
   \(\operatorname{Spec}(W^+_\infty)=(-1/6,1/12,1/12)\) with
   \(|W^+_\infty|^2=1/24\) and \(\operatorname{Ric}=-g_\infty\) makes
   \((24|W^+|^2)^{1/3}g_\infty=g_\infty\) locally Kähler by
   Derdziński Proposition 5 (the metric is Einstein hence \(\delta W^+=0\),
   and the spectrum has at most two eigenvalues).  But a four-dimensional
   Kähler–Einstein metric with \(\operatorname{Ric}=-g\) has
   \(|W^+|^2=s^2/24=2/3\neq1/24\).

This local contradiction gives \(\eta(K,\rho)>0\) such that
\(\mathcal A_\rho\Phi_i\ge\eta\) on every admissible pullback ball, which
contradicts (9.2) for \(\delta_i\) small.  The gap
\(\varepsilon_{\mathcal F}>0\) is class-uniform if the support, chart, and
flow constants are uniform over the stated IL family.

---

## 10. Summary of corrected dependencies, refined by Step 59

| Module | Status after Step 59 | Source |
|--------|--------|--------|
| A. Per-datum flow existence | Still conditional | Transported-cutoff DeTurck construction |
| B. Curvature Moser endpoint | Imported, still source-dependent | A03 Step 58 |
| C. Defect Moser endpoint | Imported, still source-dependent | A01 Step 34 |
| D. Coupled \((\Gamma,V)\) bootstrap | Imported, still source-dependent | A01 Step 55 |
| E. Base layer \(U_0\in L^\infty, T_0\in L^q\to(U_1,C_2)\to T_1\) | Not self-contained in this note | A03 Step 57/Step 37 family plus Step 59 corrections |
| F. Current-pair and unweighted continuation | Useful mechanisms here; refined ledger needed | Step 59 |
| G. Terminal compactness | Imported local mechanism | A01 Step 56 §4 |
| H. Forbidden germ | Source-grounded local obstruction | Derdziński source |

The full restricted IL chain remains promising, but this file by itself does not
make the restricted theorem unconditional. Step 59 preserves the good estimates
while making explicit the remaining exact tensor evolution, reordering, base,
and fixed-background product work.

---

## 11. Verification records

Script: `workspace/scripts/step58_all_order_continuation_verify.py`
Data: `workspace/data/step58_all_order_continuation_verify.json`
