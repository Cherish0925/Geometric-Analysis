# Step 54 supplement: [SUPERSEDED by Step 55 direct nonlinear construction]

# Step 54 supplement: exact synchronized-output fixed-background ledger

## 0. Purpose

This note fixes the precise inner map whose two-order-lower difference estimate should replace the invalid Step 53 product contraction. It distinguishes three levels:

1. the exact nonlinear transported-cutoff DeTurck equation at a fixed point;
2. a frozen-
metric inner mixed system whose fixed points solve that equation;
3. the derivative families that must be checked to obtain an \(H^s\) invariant ball and an \(H^r\), \(r=s-2\), contraction.

No existence theorem is asserted until every family below is allocated.

## 1. Exact fixed-background formula

Fix a smooth background metric \(\bar g\), let \(D=\bar\nabla\), and define the standard DeTurck vector
\[
W^k(G)=G^{ab}\bigl(\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}\bigr).
\tag{1.1}
\]
There are smooth universal tensors \(R_{ij}(G,V)\), linear in \(V\), and \(Q_{ij}(G,DG)\), quadratic in \(DG\), such that
\[
-2\operatorname{Ric}(G)+\mathcal L_{W(G)}G
=G^{ab}D_aD_bG+R(G,G)+Q(G,DG).
\tag{1.2}
\]
For a scalar \(\beta\),
\[
\mathcal L_{\beta^2W(G)}G
=\beta^2\mathcal L_{W(G)}G
+2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr).
\tag{1.3}
\]
Therefore the exact transported-cutoff normalized DeTurck system is
\[
\begin{cases}
\partial_tG
=\beta^2\bigl[G^{-1}D^2G+R(G,G)+Q(G,DG)-2G\bigr]
+2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr),\\
\partial_t\beta=\beta^2W(G)\cdot D\beta.
\end{cases}
\tag{1.4}
\]
The pullback by \(\partial_t\varphi=-\beta^2W(G)\circ\varphi\) has \(\beta\circ\varphi=\chi\) and solves the fixed-cutoff geometric equation.

## 2. Frozen-metric synchronized-output inner system

For a prescribed positive metric path \(U\), use
\[
\begin{cases}
\partial_tV
=(\beta^2+\varepsilon)U^{-1}D^2V
+\beta^2R(U,V)+\beta^2Q(U,DU)-2\beta^2V
+2\operatorname{sym}\bigl(d(\beta^2)\otimes W(U)^\flat_U\bigr),\\
\partial_t\beta=\beta^2W(V)\cdot D\beta,\\
(V,\beta)|_{t=0}=(g_0,\chi).
\end{cases}
\tag{2.1}
\]
At a fixed point \(U=V=G\), (2.1) is (1.4) plus \(\varepsilon G^{-1}D^2G\), which vanishes in the regularized limit.

The asymmetry is deliberate. The metric equation follows Xu's frozen coefficients, while the transport uses the metric output. This places the lost derivative of the transport difference on \(Z=V_1-V_2\), which has parabolic dissipation.

## 3. Single-solution top-order ledger

Let \(s>n/2+4\). At derivative order \(s\), the only factors beyond the controlled \(H^s\) ball are:

| source | top structure | allocation |
|---|---|---|
| principal metric | \((\beta^2+\varepsilon)D^{s+2}V\) after testing | integrate once; gives \(-(\beta^2+\varepsilon)|D^{s+1}V|^2\) |
| derivative of principal coefficient | \(\beta D\beta\,D^{s+1}V\) | absorb by \(\beta^2|D^{s+1}V|^2\) |
| frozen \(Q(U,DU)\) | \(\beta^2D^{s+1}U\) | integrate one derivative onto \(V\); absorb \(\beta D^{s+1}V\), leave \(D^sU\) |
| Lie cross, cutoff top | \(\beta W(U)D^{s+1}\beta\) | integrate derivative onto \(V\); absorb \(\beta D^{s+1}V\) |
| Lie cross, input top | \(\beta D\beta\,D^{s+1}U\) | integrate derivative off \(U\); absorb \(\beta D^{s+1}V\) after testing |
| transport | \(D^s\beta\,\beta^2D^{s+1}V\,D\beta\) | absorb \(\beta D^{s+1}V\) |

This gives the candidate joint estimate
\[
\frac d{dt}\mathcal E_s+c\mathcal D_s\le C_R(1+\mathcal E_s),
\quad
\mathcal E_s=\|V\|_{H^s}^2+A\|\beta\|_{H^s}^2,
\quad
\mathcal D_s=\sum_{k\le s}\int(\beta^2+\varepsilon)|D^{k+1}V|^2.
\tag{3.1}
\]
A large fixed \(A\) is allowed, as in Yang's linear symmetrizer.

## 4. Two-order-lower difference ledger

Let \((V_i,\beta_i)\) correspond to frozen inputs \(U_i\), and set
\[
Z=V_1-V_2,\quad \omega=\beta_1-\beta_2,\quad H=U_1-U_2.
\tag{4.1}
\]
Choose
\[
r=s-2>n/2+2.
\tag{4.2}
\]
Orient every top-order difference relative to branch 2.

### 4.1 Principal metric family

\[
(\beta_1^2+\varepsilon)U_1^{-1}D^2V_1
-(\beta_2^2+\varepsilon)U_2^{-1}D^2V_2
\]
\[
=(\beta_2^2+\varepsilon)U_2^{-1}D^2Z
+(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1
+(\beta_2^2+\varepsilon)(U_1^{-1}-U_2^{-1})D^2V_1.
\tag{4.3}
\]
The first term supplies branch-2 dissipation. Because \(r+2=s\), the second and third are product estimates using the individual \(H^s\) bound:
\[
\|D^r[(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1]\|_2\le C_R\|\omega\|_{H^r},
\tag{4.4}
\]
\[
\|D^r[(\beta_2^2+\varepsilon)(U_1^{-1}-U_2^{-1})D^2V_1]\|_2\le C_R\|H\|_{H^r}.
\tag{4.5}
\]
No difference interpolation is used.

### 4.2 Frozen algebraic and quadratic families

For \(\beta^2R(U,V)\), the difference splits into coefficient, input, and output pieces:
\[
(\beta_1^2-\beta_2^2)R(U_1,V_1)
+\beta_2^2[R(U_1,V_1)-R(U_2,V_1)]
+\beta_2^2R(U_2,Z),
\tag{4.6}
\]
all controlled in \(H^r\) by \(\omega,H,Z\).

For \(\beta^2Q(U,DU)\), the top input difference is schematically
\[
\beta_2^2 A(U_1,U_2,DU_1,DU_2)D^{r+1}H.
\tag{4.7}
\]
After testing against \(D^rZ\), integrate one derivative off \(H\):
\[
\int D^rZ\,\beta_2^2 A D^{r+1}H
=-\int \beta_2^2D^{r+1}Z\,A D^rH
-\int D^rZ\,D(\beta_2^2A)D^rH.
\tag{4.8}
\]
The first term has \(\beta_2^2D^{r+1}Z\) and is absorbed; the second is lower order. Thus no unweighted \(D^{r+1}H\) survives.

### 4.3 Lie cross family

Use the branch-oriented identities
\[
\beta_1^2-\beta_2^2=(\beta_1+\beta_2)\omega,
\tag{4.9}
\]
\[
d(\beta_1^2)-d(\beta_2^2)=2\beta_2d\omega+2\omega d\beta_1.
\tag{4.10}
\]
The top output-cutoff difference is
\[
\int D^rZ\,\beta_2W(U_2)D^{r+1}\omega.
\tag{4.11}
\]
Integrating once gives
\[
-\int \beta_2D^{r+1}Z\,W(U_2)D^r\omega+\text{lower},
\tag{4.12}
\]
absorbed by branch-2 dissipation.

The top input metric difference is
\[
\int D^rZ\,\beta_2D\beta_2\,A(U_1,U_2)D^{r+1}H,
\tag{4.13}
\]
and is treated exactly as (4.8). Any coefficient-difference terms without \(D^{r+1}\omega\) are ordinary \(H^r\) products.

### 4.4 Transport family

\[
\partial_t\omega
=\beta_1^2W(V_1)\cdot D\omega
+[\beta_1^2W(V_1)-\beta_2^2W(V_2)]\cdot D\beta_2,
\tag{4.14}
\]
with
\[
\beta_1^2W(V_1)-\beta_2^2W(V_2)
=(\beta_1^2-\beta_2^2)W(V_1)+\beta_2^2[W(V_1)-W(V_2)].
\tag{4.15}
\]
Transport integration by parts removes \(D^{r+1}\omega\) from the advective term. The top metric-output difference is
\[
\int D^r\omega\,\beta_2^2A(V_1,V_2)D^{r+1}Z\,D\beta_2,
\tag{4.16}
\]
which is absorbed by the same branch-2 dissipation. All other pieces use at most \(r\) derivatives of \(Z,\omega\).

### 4.5 Candidate result

The ledger yields, provided the fixed-background identities (1.2)--(1.3) introduce no omitted family,
\[
\frac d{dt}\bigl(\|Z\|_{H^r}^2+A\|\omega\|_{H^r}^2\bigr)
+c\sum_{k\le r}\int(\beta_2^2+\varepsilon)|D^{k+1}Z|^2
\]
\[
\le C_R\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2+\|H\|_{H^r}^2\bigr).
\tag{4.17}
\]
Zero initial difference then gives an outer contraction for small \(T\).

## 5. Checks still required before promotion

1. Derive (1.2) in exactly the same fixed-background convention used by Xu, including whether \(R(U,V)\) is the correct frozen linear term and whether every \(Q\)-family is covered.
2. Check all commutators when \(D^r\) hits \(U^{-1}\), \(W(U)^\flat_U\), and the background volume pairing.
3. Verify that integrating the top \(D^{r+1}H\) terms in (4.8), (4.13) never differentiates a factor lacking \(\beta_2\).
4. Construct the fixed-\(\varepsilon\) inner mixed solution (Galerkin or standard parabolic--symmetric-hyperbolic theory) and show (3.1) before invoking the outer contraction.
5. Obtain arbitrary-order estimates and compactness sufficient to pass \(\varepsilon\to0\) smoothly across the zero set.

Until these are done, (4.17) is a precise candidate tensor ledger, not a theorem.

## 6. TTCS tensor verification and correction

Two independent verifier branches reconstructed the fixed-background identities and supported the finite-order ledger after one precise correction.

### 6.1 Correct Lie difference orientation

For the branch-2 organization, write
\[
d(\beta_1^2)\odot\mathcal W(U_1)-d(\beta_2^2)\odot\mathcal W(U_2)
=[d(\beta_1^2)-d(\beta_2^2)]\odot\mathcal W(U_1)
+d(\beta_2^2)\odot[\mathcal W(U_1)-\mathcal W(U_2)].
\tag{6.1}
\]
Together with
\[
d(\beta_1^2)-d(\beta_2^2)=2\beta_2d\omega+2\omega d\beta_1,
\tag{6.2}
\]
the top cutoff term is
\[
\int D^rZ\,\beta_2\mathcal W(U_1)D^{r+1}\omega,
\tag{6.3}
\]
not the \(\mathcal W(U_2)\) version written in (4.11). Equation (6.3) integrates to branch-2 weighted dissipation. An alternative decomposition using \(\mathcal W(U_2)\) is possible only if its additional cross term is kept explicitly.

A vital bookkeeping rule is: a high derivative on one complete branch, such as
\(\omega\mathcal W(U_2)D^{r+1}\beta_1\) or \(\omega D^{r+1}U_1\), is bounded directly by the individual \(H^s\) ball. Do not split it into branch 2 plus a difference; that would manufacture an unweighted high derivative of \(\omega\) or \(H\).

### 6.2 Verified finite-order conclusion

With \(r=s-2\), the exact Xu fixed-background tensors \(R_{\bar g}(U,V)\), \(Q(U,DU)\), and
\[
d(\beta^2)\odot\mathcal W(U)
\tag{6.4}
\]
exhaust the nonlinear DeTurck families. The verifier found:

- the single-solution \(H^s\) joint estimate is \(\varepsilon\)-uniform;
- the corrected branch-2 \(H^{s-2}\) difference estimate is \(\varepsilon\)-uniform;
- all top \(D^{r+1}H\) terms from \(Q\) or the Lie-input difference carry \(\beta_2^2\) or \(\beta_2D\beta_2\) and are integrated onto \(Z\);
- all top \(D^{r+1}\omega\) terms arise through \(d(\beta^2)\), gain \(\beta_2\), and are integrated onto \(Z\);
- the transport top term carries \(\beta_2^2D^{r+1}Z\);
- no inverse power of \(\varepsilon\) is introduced.

Thus (4.17), with (6.1)--(6.3), is supported as a finite-order a priori estimate.

### 6.3 Exact remaining theorem work

The start theorem still requires two constructions beyond the finite-order ledger:

1. For fixed \(\varepsilon>0\), construct the coupled strictly-parabolic/transport inner solution (e.g. Friedrichs--Galerkin) using the joint energy, and then run the outer Xu contraction.
2. Establish on the same common time interval the all-order \(\varepsilon\)-uniform tame hierarchy
   \[
   E_m'+cD_m\le C(E_s)E_m+C_m(E_{m-1}),
   \tag{6.5}
   \]
   plus uniform time-derivative bounds, so a diagonal limit is smooth across the moving zero set of \(\beta\).

Finite \(H^s\) compactness alone yields only finite regularity and does not justify smooth matching across \(\{\beta=0\}\). The transported equation preserves the zero set along characteristics and contains no division by \(\beta\), which makes (6.5) plausible, but this all-order hierarchy has not yet been written. The exact TTCS record is `trace/ttcs/results/step54_ttcs02_verifier1_integration.md`.
