# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step54_exact_synchronized_output_ledger.md",
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md",
    "Sessions/S0910A03/staging/processing/xu_local_ricci_flow.txt",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Verify the exact synchronized-output fixed-background ledger in the new Step 54 supplement as a mathematician working on degenerate quasilinear parabolic systems. Reconstruct the frozen inner system from the exact DeTurck identity and check every top-order family in the single-solution H^s estimate and the branch-2-oriented H^{s-2} difference estimate. Focus on whether any term produces an unweighted D^{r+1}(U1-U2), an unweighted D^{r+1}omega, a missing derivative of V or beta, or an epsilon-dependent constant. Check the product estimates (4.4)-(4.5), integrations (4.8),(4.12)-(4.13), and transport (4.14)-(4.16). Also assess whether standard Galerkin/parabolic-transport construction plus the stated uniform tame hierarchy can pass epsilon to zero smoothly across the zero set, or identify the exact missing estimate. Do not accept the theorem merely because the schematic ledger looks plausible; return explicit corrected formulas and status.

## Output

## Scientific memo

### 1. Exact fixed-background equation

Let \(D=\bar\nabla\), and write
\[
A(G)^k{}_{ab}:=\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}
=\frac12G^{k\ell}\bigl(D_aG_{b\ell}+D_bG_{a\ell}-D_\ell G_{ab}\bigr).
\]
Then
\[
W^k(G)=G^{ab}A(G)^k{}_{ab},
\qquad
\mathcal W_j(G):=G_{jk}W^k(G)
=\frac12G^{pq}\bigl(D_pG_{qj}+D_qG_{pj}-D_jG_{pq}\bigr).
\]

In the convention of Xu’s equation (2.3),
\[
-2\operatorname{Ric}(G)+\mathcal L_{W(G)}G
=G^{ab}D_aD_bG+\mathcal R_{\bar g}(G,G)+\mathcal Q(G,DG),
\]
where the frozen algebraic term is
\[
\mathcal R_{\bar g}(U,V)_{ij}
=
-U^{ab}\Bigl(
V_{ip}\bar g^{pq}\bar R_{jaqb}
+
V_{jp}\bar g^{pq}\bar R_{iaqb}
\Bigr),
\]
and
\[
\begin{aligned}
\mathcal Q(U,DU)_{ij}
=\frac12U^{ab}U^{pq}\bigl(&
D_iU_{pa}D_jU_{qb}
+2D_aU_{jp}D_qU_{ib}\\
&-2D_aU_{jp}D_bU_{iq}
-2D_jU_{pa}D_bU_{iq}
-2D_iU_{pa}D_bU_{jq}
\bigr).
\end{aligned}
\]
Dummy-index renaming does not affect this formula.

If \(p\odot q\) denotes \(p_iq_j+p_jq_i\), then
\[
\mathcal L_{\beta^2W(G)}G
=\beta^2\mathcal L_{W(G)}G+d(\beta^2)\odot\mathcal W(G).
\]
Thus the exact transported system is
\[
\begin{cases}
G_t=\beta^2\bigl(G^{ab}D_aD_bG+\mathcal R_{\bar g}(G,G)
+\mathcal Q(G,DG)-2G\bigr)
+d(\beta^2)\odot\mathcal W(G),\\[1mm]
\beta_t=\beta^2W(G)\cdot D\beta.
\end{cases}
\]

Accordingly, the exact Xu-type frozen inner system is
\[
\boxed{
\begin{cases}
V_t=(\beta^2+\varepsilon)U^{ab}D_aD_bV
+\beta^2\mathcal R_{\bar g}(U,V)
+\beta^2\mathcal Q(U,DU)-2\beta^2V\\
\hspace{25mm}+d(\beta^2)\odot\mathcal W(U),\\[1mm]
\beta_t=\beta^2W(V)\cdot D\beta.
\end{cases}}
\]
At \(U=V=G\), this is the exact transported equation plus
\(\varepsilon G^{ab}D_aD_bG\). This matches Xu’s freezing convention: the principal inverse metric and every quadratic \(DU\)-factor are frozen, while the curvature-background term remains linear in \(V\).

---

### 2. Single-solution \(H^s\) energy

Assume \(s>n/2+4\), \(U\) stays uniformly positive, and
\[
\|U\|_{H^s}+\|V\|_{H^s}+\|\beta\|_{H^s}\le R.
\]
All norms and integrations may be taken with the fixed background metric.

#### Principal operator

Set \(a=\beta^2+\varepsilon\). At order \(s\),
\[
\begin{aligned}
\langle D^sV,D^s(aU^{ab}D_aD_bV)\rangle
={}&-\int aU^{ab}\langle D_aD^sV,D_bD^sV\rangle\\
&+O\!\int\bigl(|\beta D\beta|+a|DU|\bigr)
|D^{s+1}V||D^sV|+\text{lower terms}.
\end{aligned}
\]
The two displayed coefficient terms satisfy
\[
|\beta D\beta|\,|D^{s+1}V|
\le C_R\,|\beta D^{s+1}V|,
\]
and
\[
a|DU|\,|D^{s+1}V||D^sV|
\le \eta a|D^{s+1}V|^2+C_{\eta,R}a|D^sV|^2.
\]
The \(\varepsilon DU^{-1}\) part is absorbed by the
\(\varepsilon|D^{s+1}V|^2\) component, without dividing by \(\varepsilon\).

When at least two derivatives hit \(aU^{-1}\), at most \(D^sV\) remains on the other factor. Since \(s>n/2+4\), standard Moser estimates control all such terms from the \(H^s\) ball. This principal-coefficient family was omitted from the short table but does not alter the proposed estimate.

#### Frozen quadratic term

The only derivative exceeding \(s\) is
\[
D^s\!\left(\beta^2\mathcal Q(U,DU)\right)
=
\beta^2\mathsf A(U,DU)D^{s+1}U+\text{terms with at most \(s\) derivatives}.
\]
After pairing with \(D^sV\),
\[
\begin{aligned}
\int D^sV\,\beta^2\mathsf A\,D^{s+1}U
={}&-\int \beta^2D^{s+1}V\,\mathsf A\,D^sU\\
&-\int D^sV\,D(\beta^2\mathsf A)\,D^sU
+\text{background-curvature commutators}.
\end{aligned}
\]
The first term contains \(\beta D^{s+1}V\); the second contains at most
\(D^sU,D^sV,D\beta\). Hence no unweighted \(D^{s+1}U\) remains.

#### Lie-cross term

The two top pieces of
\[
D^s\bigl(d(\beta^2)\odot\mathcal W(U)\bigr)
\]
are
\[
\beta\,\mathcal W(U)\,D^{s+1}\beta,
\qquad
\beta D\beta\,\mathsf A(U)D^{s+1}U.
\]
They give
\[
\begin{aligned}
\int D^sV\,\beta\mathcal W(U)D^{s+1}\beta
={}&-\int \beta\mathcal W(U)D^{s+1}V\,D^s\beta\\
&-\int D(\beta\mathcal W(U))D^sV\,D^s\beta+\cdots ,
\end{aligned}
\]
and
\[
\begin{aligned}
\int D^sV\,\beta D\beta\,\mathsf A D^{s+1}U
={}&-\int \beta D\beta\,\mathsf A D^{s+1}V\,D^sU\\
&-\int D(\beta D\beta\,\mathsf A)D^sV\,D^sU+\cdots .
\end{aligned}
\]
Both first terms match the \(\beta^2|D^{s+1}V|^2\) dissipation. The differentiated coefficients require only \(D^2U,D^2\beta\) in \(L^\infty\).

#### Transport equation

For \(b=\beta^2W(V)\),
\[
\frac12\frac d{dt}\|D^s\beta\|_2^2
=
-\frac12\int (\operatorname{div}b)|D^s\beta|^2
+\int D^s\beta\,[D^s,b\cdot D]\beta.
\]
The unique top metric term is
\[
\int D^s\beta\;\beta^2\mathsf A(V)D^{s+1}V\,D\beta,
\]
so
\[
|I_s|
\le \eta\|\beta D^{s+1}V\|_2^2
+C_{\eta,R}\|\beta\|_{H^s}^2.
\]
The advective \(D^{s+1}\beta\) term disappears by integration by parts. The divergence term uses \(D^2V\in L^\infty\).

Thus the single-solution top-order ledger is structurally correct. More precisely,
\[
\frac d{dt}\bigl(\|V\|_{H^s}^2+A\|\beta\|_{H^s}^2\bigr)
+c\sum_{k\le s}\int(\beta^2+\varepsilon)|D^{k+1}V|^2
\le C_R\bigl(1+\|V\|_{H^s}^2+\|\beta\|_{H^s}^2\bigr),
\]
with constants uniform for \(0<\varepsilon\le1\).

---

### 3. Principal difference terms at \(r=s-2\)

Let
\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2,\qquad H=U_1-U_2.
\]
The decomposition (4.3) is algebraically correct:
\[
\begin{aligned}
&a_1U_1^{-1}D^2V_1-a_2U_2^{-1}D^2V_2\\
&\quad=a_2U_2^{-1}D^2Z
+(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1
+a_2(U_1^{-1}-U_2^{-1})D^2V_1,
\end{aligned}
\]
where \(a_i=\beta_i^2+\varepsilon\).

Because \(r>n/2+2\), \(H^r\) is an algebra, and
\[
\|\beta_1^2-\beta_2^2\|_{H^r}\le C_R\|\omega\|_{H^r},
\qquad
\|U_1^{-1}-U_2^{-1}\|_{H^r}\le C_R\|H\|_{H^r}.
\]
Since \(r+2=s\),
\[
\|D^2V_1\|_{H^r}\le \|V_1\|_{H^s}\le R.
\]
Therefore
\[
\|(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1\|_{H^r}
\le C_R\|\omega\|_{H^r},
\]
and
\[
\|a_2(U_1^{-1}-U_2^{-1})D^2V_1\|_{H^r}
\le C_R\|H\|_{H^r}.
\]
These are precisely (4.4)–(4.5). Their validity uses the full two-derivative gap; with only \(r=s-1\), the same direct estimate would require one derivative not supplied by the invariant ball.

The commutators of \(D^r\) with \(a_2U_2^{-1}\) are handled as in the single-solution estimate. The \(\varepsilon DU_2^{-1}\) contribution is absorbed by the \(\varepsilon\)-part of branch-2 dissipation.

---

### 4. Quadratic and Lie differences

For the quadratic expression,
\[
\beta_1^2Q(U_1)-\beta_2^2Q(U_2)
=(\beta_1^2-\beta_2^2)Q(U_1)
+\beta_2^2\bigl(Q(U_1)-Q(U_2)\bigr).
\]
Since \(Q\) is quadratic in \(DU\),
\[
Q(U_1)-Q(U_2)
=\mathsf A^a(U_1,U_2,DU_1,DU_2)D_aH
+\mathsf B(U_1,U_2,DU_1,DU_2)H.
\]
The only top term is therefore
\[
\int D^rZ\,\beta_2^2\mathsf A\,D^{r+1}H.
\]
The integration in (4.8) becomes
\[
\begin{aligned}
\int D^rZ\,\beta_2^2\mathsf A\,D^{r+1}H
={}&-\int \beta_2^2D^{r+1}Z\,\mathsf A\,D^rH\\
&-\int D^rZ\,D(\beta_2^2\mathsf A)\,D^rH+\cdots .
\end{aligned}
\]
Hence
\[
|I_Q|
\le \eta\|\beta_2D^{r+1}Z\|_2^2
+C_{\eta,R}\bigl(\|H\|_{H^r}^2+\|Z\|_{H^r}^2\bigr).
\]
No unweighted \(D^{r+1}H\) survives.

#### Correction to (4.11)

The exact branch-2-weighted Lie decomposition is
\[
\begin{aligned}
&d(\beta_1^2)\odot\mathcal W(U_1)
-d(\beta_2^2)\odot\mathcal W(U_2)\\
&\quad=
\bigl(2\beta_2d\omega+2\omega d\beta_1\bigr)\odot\mathcal W(U_1)
+d(\beta_2^2)\odot\bigl(\mathcal W(U_1)-\mathcal W(U_2)\bigr).
\end{aligned}
\]
Thus the coefficient in the top cutoff term is \(\mathcal W(U_1)\), not
\(\mathcal W(U_2)\):
\[
I_\omega
=
\int D^rZ\,\beta_2\mathcal W(U_1)D^{r+1}\omega.
\]
The corrected integration is
\[
\begin{aligned}
I_\omega
={}&-\int \beta_2D^{r+1}Z\,\mathcal W(U_1)D^r\omega\\
&-\int D^rZ\,D\!\bigl(\beta_2\mathcal W(U_1)\bigr)D^r\omega+\cdots ,
\end{aligned}
\]
and hence
\[
|I_\omega|
\le \eta\|\beta_2D^{r+1}Z\|_2^2
+C_{\eta,R}\bigl(\|\omega\|_{H^r}^2+\|Z\|_{H^r}^2\bigr).
\]

Also,
\[
\mathcal W(U_1)-\mathcal W(U_2)
=\mathsf P^a(U_1,U_2)D_aH
+\mathsf P_0(U_1,U_2,DU_2)H.
\]
Since \(d(\beta_2^2)=2\beta_2d\beta_2\), the top metric-input term is
\[
\int D^rZ\,\beta_2D\beta_2\,\mathsf P\,D^{r+1}H.
\]
After integration,
\[
\begin{aligned}
={}&-\int \beta_2D\beta_2\,\mathsf P\,D^{r+1}Z\,D^rH\\
&-\int D^rZ\,D(\beta_2D\beta_2\,\mathsf P)D^rH+\cdots ,
\end{aligned}
\]
which again matches branch-2 dissipation. This verifies (4.13), subject to replacing the schematic coefficient by the displayed exact decomposition.

---

### 5. Transport difference

With \(b_i=\beta_i^2W(V_i)\),
\[
\omega_t=b_1\cdot D\omega+(b_1-b_2)\cdot D\beta_2,
\]
and
\[
b_1-b_2
=(\beta_1^2-\beta_2^2)W(V_1)
+\beta_2^2\bigl(W(V_1)-W(V_2)\bigr).
\]
Moreover,
\[
W(V_1)-W(V_2)
=\mathsf C^a(V_1,V_2)D_aZ
+\mathsf C_0(V_1,V_2,DV_2)Z.
\]
The only top output term is
\[
I_T=\int D^r\omega\,
\beta_2^2\mathsf C\,D^{r+1}Z\,D\beta_2.
\]
Since \(\beta_2D\beta_2\in L^\infty\),
\[
|I_T|
\le C_R\|\beta_2D^{r+1}Z\|_2\|\omega\|_{H^r}
\le \eta\|\beta_2D^{r+1}Z\|_2^2+C_{\eta,R}\|\omega\|_{H^r}^2.
\]

For the advective term \(b_1\cdot D\omega\), the apparent
\(D^{r+1}\omega\) is removed by integration by parts. Its commutator is controlled because the individual \(H^s\) bounds give
\[
b_1\in H^{r+1},\qquad Db_1\in L^\infty.
\]
Here the two spare derivatives are again being used: \(W(V_1)\) contains one derivative of \(V_1\), but \(V_1\in H^{r+2}\).

---

### 6. Result of the finite-order verification

After the correction \(\mathcal W(U_2)\mapsto\mathcal W(U_1)\) in (4.11), the branch-2 organization produces
\[
\begin{aligned}
\frac d{dt}\bigl(\|Z\|_{H^r}^2+A\|\omega\|_{H^r}^2\bigr)
&+c\sum_{k\le r}\int(\beta_2^2+\varepsilon)|D^{k+1}Z|^2\\
&\le C_R\bigl(
\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2+\|H\|_{H^r}^2
\bigr).
\end{aligned}
\]
At this derivative level:

- every \(D^{r+1}H\) comes with either \(\beta_2^2\) from \(Q\) or \(\beta_2D\beta_2\) from the Lie cross;
- every \(D^{r+1}\omega\) in the metric equation comes with \(\beta_2\);
- every \(D^{r+1}Z\) in the transport equation comes with \(\beta_2^2\);
- the principal coefficient differences are treated without differentiating \(H\) or \(\omega\) above order \(r\);
- no estimate above divides by \(\varepsilon\).

Background-curvature commutators and the fixed background volume form contribute only lower-order expressions.

---

### 7. Fixed-\(\varepsilon\) construction and the \(\varepsilon\to0\) passage

For each fixed \(\varepsilon>0\), the metric equation is strongly parabolic and the cutoff equation is a quasilinear transport equation with velocity depending on \(DV\). A Friedrichs or Galerkin construction is compatible with the joint energy above. The energy, rather than generic parabolic regularity, is what can provide an existence interval independent of \(\varepsilon\); ordinary Schauder estimates generally introduce powers of \(\varepsilon^{-1}\).

The finite \(H^s\) estimate alone does not yield a smooth limit across \(\{\beta=0\}\). The missing analytic object is a tame hierarchy on one common time interval: for every \(m\ge s\),
\[
\boxed{
\frac d{dt}E_m+cD_m
\le C(E_s)E_m+C_m(E_{m-1}),}
\]
where
\[
E_m=\|G_\varepsilon\|_{H^m}^2+\|\beta_\varepsilon\|_{H^m}^2,
\qquad
D_m=\sum_{k\le m}\int(\beta_\varepsilon^2+\varepsilon)
|D^{k+1}G_\varepsilon|^2,
\]
and every constant is independent of \(\varepsilon\). The affine dependence on the top energy is important for retaining the base \(H^s\) lifespan at all derivative orders.

One also needs the resulting temporal bounds
\[
\|\partial_tG_\varepsilon\|_{H^{m-2}}
+\|\partial_t\beta_\varepsilon\|_{H^{m-1}}
\le C_m,
\]
uniformly in \(\varepsilon\). They follow from the equations once the spatial hierarchy is available.

With these estimates, Rellich compactness and a diagonal argument give smooth convergence on the common interval. In particular,
\[
\varepsilon G_\varepsilon^{-1}D^2G_\varepsilon\to0
\]
in every fixed lower Sobolev norm, while all remaining nonlinear terms converge directly. No division by \(\beta\) occurs, so the zero set introduces no additional singular expression. Smooth convergence of
\(\beta_\varepsilon^2W(G_\varepsilon)\) also gives convergence of the DeTurck diffeomorphisms.

Therefore the synchronized-output finite-order ledger is mathematically consistent after the stated Lie-term correction. What remains unresolved in the supplied supplement is the uniform all-order tame estimate and its derivation at the approximation level; standard fixed-\(\varepsilon\) theory by itself does not supply that estimate.