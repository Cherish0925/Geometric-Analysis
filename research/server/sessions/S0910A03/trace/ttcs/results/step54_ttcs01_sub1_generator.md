# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md",
    "Sessions/S0910A03/workspace/notes/step53_coupled_transported_coefficient_start.md",
    "Sessions/S0910A03/staging/processing/xu_local_ricci_flow.txt",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Develop or falsify the synchronized-output construction in Step 54 for short-time existence of the exact fixed-cutoff normalized local Ricci flow. The goal is a rigorous mixed parabolic–transport iteration for the transported square coefficient, not a generic literature discussion. Starting from the proposed inner system with frozen metric U but output coefficient beta^2 and transport velocity beta^2 W(V), derive the exact joint high-order and difference energies. Determine whether every top derivative of V appearing in beta's transport equation can be absorbed by the beta-weighted parabolic dissipation of the same output, including when comparing two solutions with different beta weights. If a direct contraction fails, seek a good unknown, relative-flow/Lagrangian reformulation, symmetrizer, or graph norm that fixes the mismatch. State the exact remaining term if no closure works. Do not assume interpolation turns Hölder-1/2 into Lipschitz.

## Output

The synchronized-output construction closes. The essential device is to compare two metric equations through the arithmetic mean of their two principal operators. This produces dissipation weighted by
\[
\beta _1^2+\beta _2^2+2\varepsilon,
\]
which absorbs every top derivative of \(V_1-V_2\) produced by either transport equation. The one-sided comparison from Step 54 misses this symmetric coercivity.

## 1. Exact frozen-\(U\), output-\(\beta\) system

Fix a smooth reference metric \(\bar g\), write \(D=\bar\nabla\), and define
\[
W_j(G)=\frac12G^{pq}
 \bigl(D_pG_{qj}+D_qG_{pj}-D_jG_{pq}\bigr),
\qquad
W(G)^k=G^{kj}W_j(G).
\]

For metrics \(U,G\), set
\[
\begin{aligned}
\mathcal R_{ij}(U,G)
={}&-U^{ab}\bar g^{pq}
 \bigl(\bar R_{jaqb}G_{ip}+\bar R_{iaqb}G_{jp}\bigr),\\
\mathcal Q_{ij}(U,DU)
={}&\frac12U^{ab}U^{pq}\bigl(
D_iU_{pa}D_jU_{qb}
+2D_aU_{jp}D_qU_{ib}\\
&\hspace{27mm}
-2D_aU_{jp}D_bU_{iq}
-2D_jU_{pa}D_bU_{iq}
-2D_iU_{pa}D_bU_{jq}\bigr),\\
\mathcal C_{ij}(U,\beta)
={}&2\beta\bigl((D_i\beta)W_j(U)+(D_j\beta)W_i(U)\bigr).
\end{aligned}
\]

These tensors satisfy
\[
G^{ab}D_aD_bG+\mathcal R(G,G)+\mathcal Q(G,DG)
=-2\operatorname{Ric}_G+\mathcal L_{W(G)}G.
\]

For a prescribed metric path \(U(t)\), consider
\[
\boxed{
\begin{aligned}
\partial_tG_{ij}
={}&(\beta^2+\varepsilon)U^{ab}D_aD_bG_{ij}
+\beta^2\mathcal R_{ij}(U,G)
+\beta^2\mathcal Q_{ij}(U,DU)\\
&+\mathcal C_{ij}(U,\beta)-2\beta^2G_{ij},\\
\partial_t\beta
={}&\beta^2W(G)^kD_k\beta,\\
G(0)&=g_0,\qquad \beta(0)=\chi .
\end{aligned}}
\tag{1}
\]

At a fixed point \(U=G\),
\[
\partial_tG
=-2\beta^2(\operatorname{Ric}_G+G)
+\mathcal L_{\beta^2W(G)}G
+\varepsilon G^{ab}D_aD_bG.
\tag{2}
\]
Thus the \(\varepsilon\to0\) equation is exactly the transported-cutoff DeTurck system.

The choice to freeze all Xu terms in \(U\), rather than only the principal inverse metric, is compatible with the argument below. Terms containing \(D^{m+1}U\) are handled by integration by parts and the same \(\beta\)-weighted metric dissipation.

---

## 2. Joint high-order energy

Choose
\[
m>\frac n2+4.
\]
Assume throughout a ball in which \(U,G\) are uniformly equivalent to \(\bar g\), with
\[
\|U\|_{H^m}+\|G\|_{H^m}+\|\beta\|_{H^m}\le R.
\]
Set
\[
E_m(t)=\frac12\bigl(\|G\|_{H^m}^2+\|\beta\|_{H^m}^2\bigr),
\]
and
\[
\mathscr D_m(t)
=\sum_{k=0}^{m}\int_M(\beta^2+\varepsilon)|D^{k+1}G|^2\,d\mu_{\bar g}.
\]

### 2.1 Principal metric term

For \(|I|=m\),
\[
\begin{aligned}
&\int_M\left\langle D^IG,
D^I\bigl((\beta^2+\varepsilon)U^{ab}D_aD_bG\bigr)\right\rangle\\
={}&-\int_M(\beta^2+\varepsilon)U^{ab}
  \langle D_aD^IG,D_bD^IG\rangle+\mathcal P_I .
\end{aligned}
\tag{3}
\]

The only first-coefficient derivative involving \(\beta\) is
\[
D(\beta^2)=2\beta\,D\beta.
\]
Consequently,
\[
|\mathcal P_I|
\le \eta \mathscr D_m+C_{\eta,R}(1+\|G\|_{H^m}^2+\|\beta\|_{H^m}^2).
\tag{4}
\]
No quotient by \(\beta\) occurs. Derivatives of the \(\varepsilon U^{-1}\) coefficient carry \(\varepsilon\) and are absorbed by the \(\varepsilon|D^{m+1}G|^2\) portion.

### 2.2 Frozen quadratic Xu term

The top \(U\)-derivative in \(D^m(\beta^2\mathcal Q(U,DU))\) has the form
\[
\beta^2 A(U,DU)\,D^{m+1}U.
\]
Its contribution is
\[
\int_M D^mG*\beta^2A(U,DU)D^{m+1}U.
\]
Moving one derivative from \(U\) gives
\[
-\int_M D^{m+1}G*\beta^2A(U,DU)D^mU+\text{lower-order terms}.
\tag{5}
\]
Since
\[
\beta^2|D^{m+1}G|
\le \|\beta\|_{L^\infty}\,|\beta D^{m+1}G|,
\]
(5) is bounded by
\[
\eta\mathscr D_m+C_{\eta,R}.
\tag{6}
\]

### 2.3 Lie cross term

Using
\[
\mathcal C(U,\beta)=2\beta\,\operatorname{sym}(D\beta\otimes W(U)^\flat),
\]
the two top structures in \(D^m\mathcal C\) are
\[
2\beta W(U)*D^{m+1}\beta,
\qquad
2\beta D\beta*\mathsf L_U(D^{m+1}U),
\tag{7}
\]
where \(\mathsf L_U\) denotes the principal linearization of \(W(U)\).

For the first term,
\[
\begin{aligned}
\int_M D^mG*\beta W(U)*D^{m+1}\beta
={}&-\int_M D^{m+1}G*\beta W(U)*D^m\beta\\
&+\text{terms containing at most \(m\) derivatives}.
\end{aligned}
\tag{8}
\]
Hence
\[
|(8)|\le
\eta\|\beta D^{m+1}G\|_2^2+C_{\eta,R}\|\beta\|_{H^m}^2.
\tag{9}
\]

For the second term in (7), moving one derivative from \(U\) gives
\[
\int_M D^mG*\beta D\beta*D^{m+1}U
=
-\int_M D^{m+1}G*\beta D\beta*D^mU+\text{lower terms},
\tag{10}
\]
and again
\[
|(10)|\le \eta\mathscr D_m+C_{\eta,R}.
\tag{11}
\]

Thus neither \(D^{m+1}\beta\) nor \(D^{m+1}U\) survives in the final metric estimate.

### 2.4 Transport energy

Let \(v=\beta^2W(G)\). Then
\[
\frac12\frac d{dt}\|D^m\beta\|_2^2
=
-\frac12\int_M\operatorname{div}_{\bar g}v\,|D^m\beta|^2
+\int_M D^m\beta\,[D^m,v^kD_k]\beta.
\tag{12}
\]

The only term containing \(D^{m+1}G\) is
\[
\mathcal T_m
=
\int_M D^m\beta\,
  \beta^2\mathsf L_G(D^{m+1}G)*D\beta.
\tag{13}
\]
Therefore
\[
|\mathcal T_m|
\le
C_R\|\beta D^{m+1}G\|_2\|D^m\beta\|_2
\le
\eta\mathscr D_m+C_{\eta,R}\|\beta\|_{H^m}^2.
\tag{14}
\]
All derivatives of \(\beta^2\) contain at most \(m\) derivatives of \(\beta\).

Combining (3)–(14) gives, with constants independent of \(0<\varepsilon\le1\),
\[
\boxed{
\frac d{dt}E_m+c\,\mathscr D_m
\le C_R(1+E_m).
}
\tag{15}
\]

In particular, on a time depending only on the chosen high Sobolev ball,
\[
\sup_{t\le T}E_m(t)+c\int_0^T\mathscr D_m(t)\,dt\le C_R.
\tag{16}
\]

The transport equation also preserves \(0\le\beta\le1\), since \(\beta\) is constant along the characteristics of \(-\beta^2W(G)\).

---

## 3. Symmetric difference equation

Let \((G_i,\beta_i)\) solve (1) with frozen inputs \(U_i\), \(i=1,2\). Write
\[
Z=G_1-G_2,\qquad
\omega=\beta_1-\beta_2,\qquad
dU=U_1-U_2.
\]
Define
\[
P_i=(\beta_i^2+\varepsilon)U_i^{-1},
\qquad
\bar P=\frac12(P_1+P_2),
\qquad
\delta P=P_1-P_2,
\]
and
\[
G_*=\frac12(G_1+G_2).
\]

The principal difference has the exact identity
\[
P_1D^2G_1-P_2D^2G_2
=
\bar P\,D^2Z+\delta P\,D^2G_*.
\tag{17}
\]
Similarly, with
\[
v_i=\beta_i^2W(G_i),\qquad
\bar v=\frac12(v_1+v_2),\qquad
\delta v=v_1-v_2,\qquad
\beta_*=\frac12(\beta_1+\beta_2),
\]
the transport difference is exactly
\[
\partial_t\omega
=
\bar v\cdot D\omega+\delta v\cdot D\beta_*.
\tag{18}
\]

The averaged metric coefficient satisfies
\[
\bar P^{ab}\xi_a\xi_b
\ge c_R\bigl(\beta_1^2+\beta_2^2+2\varepsilon\bigr)|\xi|_{\bar g}^2.
\tag{19}
\]

This is the missing structural feature in a one-sided comparison.

Set
\[
S=\beta_1^2+\beta_2^2+2\varepsilon.
\]
For the affine path
\[
\beta_\theta=(1-\theta)\beta_2+\theta\beta_1,
\]
one has
\[
|\beta_\theta|^2\le 2(\beta_1^2+\beta_2^2)\le2S.
\tag{20}
\]

Choose
\[
r>\frac n2+2,\qquad m=r+2.
\]
Define
\[
E_r^\Delta
=\frac12\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\bigr),
\]
and
\[
\mathscr D_r^\Delta
=\sum_{k=0}^r\int_M
S\,|D^{k+1}Z|^2\,d\mu_{\bar g}.
\]

### 3.1 The coefficient-difference source

The exact decomposition
\[
\delta P
=(\beta_1^2-\beta_2^2)\frac{U_1^{-1}+U_2^{-1}}2
+\frac{\beta_1^2+\beta_2^2+2\varepsilon}{2}
 (U_1^{-1}-U_2^{-1})
\tag{21}
\]
gives
\[
\|\delta P\|_{H^r}
\le C_R\bigl(\|\omega\|_{H^r}+\|dU\|_{H^r}\bigr).
\tag{22}
\]
Because \(G_*\) is bounded in \(H^{r+2}\),
\[
\|\delta P\,D^2G_*\|_{H^r}
\le
C_R\bigl(\|\omega\|_{H^r}+\|dU\|_{H^r}\bigr).
\tag{23}
\]
This uses the two-derivative high ball directly:
\[
\|fg\|_{H^r}
\lesssim
\|f\|_{H^r}\|g\|_{L^\infty}
+\|f\|_{L^\infty}\|g\|_{H^r}.
\]
No interpolation between the low difference norm and the high ball is involved.

### 3.2 Top term from the transport equation

Along the path \((G_\theta,\beta_\theta)\),
\[
\delta v
=
\int_0^1
\left(2\beta_\theta\omega\,W(G_\theta)
+\beta_\theta^2\,DW_{G_\theta}[Z]\right)d\theta.
\tag{24}
\]
The principal part of \(D^rDW_{G_\theta}[Z]\) is
\[
\mathsf L_{G_\theta}(D^{r+1}Z).
\]
Thus the only new top term from (18) is
\[
\mathcal I_r
=
\int_0^1\!\!\int_M
D^r\omega\,
\beta_\theta^2\mathsf L_{G_\theta}(D^{r+1}Z)
*D\beta_*\,d\mu_{\bar g}\,d\theta.
\tag{25}
\]
Using (20),
\[
|\mathcal I_r|
\le
C_R\|\sqrt S\,D^{r+1}Z\|_2\|\omega\|_{H^r}
\le
\eta\mathscr D_r^\Delta+C_{\eta,R}\|\omega\|_{H^r}^2.
\tag{26}
\]

### 3.3 Top cutoff derivative in the metric equation

The differential of the cross term is
\[
\begin{aligned}
D\mathcal C_{(U,\beta)}[dU,\omega]
={}&2\omega\,\operatorname{sym}(D\beta\otimes W(U)^\flat)\\
&+2\beta\,\operatorname{sym}(D\omega\otimes W(U)^\flat)\\
&+2\beta\,\operatorname{sym}
 \bigl(D\beta\otimes DW_U[dU]^\flat\bigr).
\end{aligned}
\tag{27}
\]

After applying \(D^r\), the first top expression involving \(\omega\) is
\[
\int_M D^rZ*\beta_\theta W(U_\theta)*D^{r+1}\omega.
\tag{28}
\]
Moving one derivative gives
\[
(28)
=
-\int_M D^{r+1}Z*\beta_\theta W(U_\theta)*D^r\omega
+\text{lower terms},
\]
so that
\[
|(28)|
\le
\eta\mathscr D_r^\Delta+C_{\eta,R}E_r^\Delta.
\tag{29}
\]

The top \(dU\)-term is
\[
\int_M D^rZ*
  \beta_\theta D\beta_\theta*A(U_\theta)D^{r+1}dU.
\tag{30}
\]
Moving one derivative from \(dU\) yields
\[
|(30)|
\le
\eta\mathscr D_r^\Delta
+C_{\eta,R}\bigl(E_r^\Delta+\|dU\|_{H^r}^2\bigr).
\tag{31}
\]

The frozen quadratic Xu term produces
\[
\int_M D^rZ*
  \beta_\theta^2A(U_\theta,DU_\theta)D^{r+1}dU,
\tag{32}
\]
which is treated identically:
\[
|(32)|
\le
\eta\mathscr D_r^\Delta
+C_{\eta,R}\bigl(E_r^\Delta+\|dU\|_{H^r}^2\bigr).
\tag{33}
\]

All other terms contain at most \(r\) derivatives of \(Z,\omega,dU\).

### 3.4 Closed difference estimate

The principal commutators from \(\bar P D^2Z\), (23), and (26)–(33) give
\[
\boxed{
\frac d{dt}E_r^\Delta
+c\,\mathscr D_r^\Delta
\le
C_R E_r^\Delta+C_R\|U_1-U_2\|_{H^r}^2.
}
\tag{34}
\]
The constants are independent of \(\varepsilon\).

Since both inner solutions start from \((g_0,\chi)\),
\[
E_r^\Delta(0)=0,
\]
and hence
\[
\boxed{
\sup_{t\le T}E_r^\Delta(t)
\le
C_RT e^{C_RT}
\sup_{t\le T}\|U_1-U_2\|_{H^r}^2.
}
\tag{35}
\]

---

## 4. Why the one-sided comparison does not close

If the metric equation is written only with the first principal operator, its dissipation is
\[
\int_M(\beta_1^2+\varepsilon)|D^{r+1}Z|^2.
\]
The second transport equation contributes the exact term
\[
\int_M
D^r\omega\,
\beta_2^2\mathsf L(D^{r+1}Z)
*D\beta_2.
\tag{36}
\]
Where \(\beta_1=0\) and \(\beta_2\ne0\), (36) cannot be absorbed uniformly as \(\varepsilon\to0\).

Identity (17) replaces the one-sided principal coefficient by \(\bar P\), whose dissipation contains both \(\beta_1^2\) and \(\beta_2^2\). The new source \(\delta P D^2G_*\) is Lipschitz in the \(H^r\) differences because \(G_*\) lies in a fixed \(H^{r+2}\) ball. Thus the mismatch is removed without a good unknown or a graph norm.

---

## 5. Fixed point and the degenerate limit

For fixed \(\varepsilon>0\) and prescribed \(U\), system (1) is a strictly parabolic–transport system. A smooth spectral regularization gives finite-dimensional equations; (15) supplies a common existence interval, and passage through the spectral parameter gives a smooth inner solution. The estimate is independent of \(\varepsilon\).

Define
\[
\Phi_\varepsilon(U)=G[U].
\]
The high-order estimate preserves a bounded \(H^m\) ball, while (35) shows
\[
\|\Phi_\varepsilon(U_1)-\Phi_\varepsilon(U_2)\|_{C_TH^r}
\le
\bigl(C_RT e^{C_RT}\bigr)^{1/2}
\|U_1-U_2\|_{C_TH^r}.
\tag{37}
\]
For \(T\) sufficiently small, independently of \(\varepsilon\), this is a contraction. Its fixed point \(U=G_\varepsilon\), together with the associated \(\beta_\varepsilon\), solves (2).

The uniform estimates are
\[
\sup_{t\le T}
\bigl(\|G_\varepsilon\|_{H^m}^2+\|\beta_\varepsilon\|_{H^m}^2\bigr)
+
\int_0^T\!\!\int_M
(\beta_\varepsilon^2+\varepsilon)
|D^{m+1}G_\varepsilon|^2
\le C_m.
\tag{38}
\]
Moreover,
\[
\partial_tG_\varepsilon
\quad\text{is bounded in }H^{m-2},
\qquad
\partial_t\beta_\varepsilon
\quad\text{is bounded in }H^{m-1}.
\tag{39}
\]
Compactness therefore gives a subsequence converging strongly below order \(m\). The regularizing term satisfies
\[
\varepsilon G_\varepsilon^{ab}D_aD_bG_\varepsilon
\longrightarrow0
\quad\text{in }H^{m-2},
\]
and the limit solves
\[
\begin{aligned}
\partial_t\widehat g
&=-2\beta^2(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\beta^2W(\widehat g)}\widehat g,\\
\partial_t\beta
&=\beta^2W(\widehat g)\cdot D\beta.
\end{aligned}
\tag{40}
\]

Finally let
\[
X=-\beta^2W(\widehat g),\qquad
\partial_t\varphi=X\circ\varphi,\qquad \varphi_0=\operatorname{id}.
\]
Then
\[
\frac d{dt}(\beta\circ\varphi)
=(\partial_t\beta+X\beta)\circ\varphi=0,
\]
so
\[
\beta\circ\varphi=\chi.
\]
For \(h=\varphi^*\widehat g\),
\[
\partial_th
=\varphi^*(\partial_t\widehat g+\mathcal L_X\widehat g)
=-2\chi^2(\operatorname{Ric}_h+h).
\]

Hence every smooth closed initial metric and smooth cutoff \(0\le\chi\le1\) admit a smooth short-time solution of the exact fixed-cutoff normalized local Ricci flow
\[
\boxed{
\partial_th=-2\chi^2(\operatorname{Ric}_h+h),\qquad h(0)=g_0.
}
\]

The decisive comparison is the averaged principal identity (17); it converts the two transported squares into a single symmetrizer and removes the differing-weight term identified in Step 54.