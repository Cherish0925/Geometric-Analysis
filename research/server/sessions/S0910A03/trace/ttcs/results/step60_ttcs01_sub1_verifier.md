# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Audit the continuation mechanism for the exact degenerate geometric flow ∂_t g=-2χ²(Ric_g+g), focusing on the two disputed points. First, determine whether the coordinate-time derivative-family enumeration (T1–T6 and U1–U7) in step45, combined with the signed integrations and Step59/A01 Step55 residual estimate, genuinely exhausts every commutator and gives the arbitrary finite-order L^p induction for the exact case b=χ². Identify any missing current-level or unweighted coefficient, with an explicit derivative allocation if one exists. Second, assess uniqueness: is A01 Step56's proposed direct estimate d/dt∫|g1-g2|²≤C∫|g1-g2|² valid for the geometric Ricci-type equation without fixing diffeomorphism gauge? Account for diffeomorphism invariance and the actual principal symbol. If invalid, decide whether the all-order energy route can instead yield a smooth terminal metric and a direct smooth splice/restart without overlap uniqueness, and state the precise time-regularity/matching needed. Give a mathematical memo, not process advice.

## Output

# Mathematical memo: exact \(\chi^2\)-cutoff continuation and uniqueness

## 1. Derivative-family enumeration for the exact flow

For the exact equation
\[
\partial_t g=-2\chi^2(\operatorname{Ric}_g+g),
\qquad b=a=\chi^2,
\qquad T=\operatorname{Rm}+G,\qquad U=bT,
\]
the Step45 coordinate-time convention is the right one:
\[
\partial_t(\nabla^m A)
=\nabla^m(\partial_t A)
+\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^s A,
\qquad
\nabla^r(\partial_t\Gamma)=U_{r+1}*g^{-1}.
\]
Together with
\[
[\nabla^m,\Delta]A
=\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA,
\]
this accounts for the two commutator sources: spatial Laplacian commutators and coordinate-time connection variation.

Assuming the structural equations
\[
\partial_tT=b\Delta T+B_1*\nabla T+B_2*T+b(T*T+T+1),
\tag{1.1}
\]
\[
\partial_tU=b\Delta U+B_1*\nabla U+B_2*U+(B_1*B_1)*T+U*U+bU+b^2,
\tag{1.2}
\]
the Step45 families T1–T6 and U1–U7 exhaust the derivative types at the star-contraction level.

### \(T_m=\nabla^mT\)

The listed families arise as follows.

- \(\nabla^m(b\Delta T)\) gives \(b\Delta T_m\), \(B_r*T_{m+2-r}\), and the spatial commutator
  \[
  b*\nabla^r\operatorname{Rm}*T_s,\qquad r+s=m.
  \]
- \(\nabla^m(B_1*\nabla T+B_2*T)\) gives exactly
  \[
  B_r*T_{m+2-r},\qquad 1\le r\le m+2.
  \]
- \(\nabla^m(bT*T)\) gives
  \[
  B_r*T_i*T_j,\qquad r+i+j=m.
  \]
- Coordinate-time commutation gives
  \[
  U_{r+1}*T_s,\qquad r+s=m-1.
  \]
- The lower \(bT\), \(bG\), \(b\) terms give \(B_r*T_{m-r}\) and \(B_m\).

The only current \(T_m\) coefficient coming from \(bT*T\) or the spatial commutator is weighted:
\[
bT_0*T_m=U_0*T_m,
\qquad
b\,\operatorname{Rm}*T_m=(U_0-bG)*T_m.
\]
Thus no bare \(T_0*T_m\) coefficient appears.

The time-commutator top allocation
\[
r=m-1,\ s=0:
\qquad U_m*T_0
\]
is unweighted in \(T_0\), but it is a forcing term in the \(T_m\) estimate after the \((U_m,C_{m+1})\) stage has already been completed. Since the zero-order seed gives \(T_0\in L^q\) for every finite \(q\), this product is controlled by Hölder/Young, not by pointwise curvature.

### \(U_m=\nabla^mU\)

The U1–U7 list similarly follows from (1.2).

- \(\nabla^m(b\Delta U)\) gives \(b\Delta U_m\), \(B_r*U_{m+2-r}\), and
  \[
  b*\nabla^r\operatorname{Rm}*U_s,\qquad r+s=m.
  \]
- \(\nabla^m(B_1*\nabla U+B_2*U)\) gives
  \[
  B_r*U_{m+2-r},\qquad 1\le r\le m+2.
  \]
- \(\nabla^m((B_1*B_1)*T)\) gives
  \[
  B_{r+1}*B_{s+1}*T_t,\qquad r+s+t=m.
  \]
- \(\nabla^m(U*U)\) gives \(U_i*U_j\), \(i+j=m\).
- Coordinate-time commutation gives \(U_{r+1}*U_s\), \(r+s=m-1\).
- Lower \(bU,b^2\) terms give \(B_r*U_{m-r}\) and \(\nabla^m(b^2)\).

For the exact case \(b=\chi^2\), the most useful identity is
\[
(B_1*B_1)*T
=4\chi^2(C_1*C_1)*T
=4(C_1*C_1)*U.
\tag{1.3}
\]
Differentiating (1.3) directly gives
\[
\nabla^m\bigl((B_1*B_1)*T\bigr)
=
\sum_{r+s+t=m} C_{r+1}*C_{s+1}*U_t.
\tag{1.4}
\]
Hence its current contributions are only
\[
C_1*C_1*U_m,
\qquad
C_{m+1}*C_1*U_0,
\]
with \(C_1,U_0\) bounded. There is no bare \(C_{m+1}*T_0\) coefficient.

Equivalently, if one keeps the Step45 \(B\)-notation first, the current \(T_m\) allocation is
\[
B_1*B_1*T_m
=4C_1*C_1\,(bT_m)
=4C_1*C_1\left(U_m-\sum_{q=1}^mB_q*T_{m-q}\right),
\tag{1.5}
\]
which again contains current \(U_m\) plus prior \(T\)-levels only.

The other delicate current \(T_m\) occurrence in the \(U_m\) equation is the spatial-commutator allocation
\[
r=m,\ s=0:
\qquad
b*T_m*U_0.
\]
Using the same Leibniz identity,
\[
bT_m=U_m-\sum_{q=1}^mB_q*T_{m-q},
\tag{1.6}
\]
this becomes \(U_m*U_0\) plus prior-level forcing. Thus no unweighted \(T_m\) coefficient is produced.

### Cutoff-jet evolution

For \(C_{m+1}=\nabla^{m+1}\chi\),
\[
\partial_t C_{m+1}
=
U_m*C_1+\sum_{1\le j<m}U_j*C_{m+1-j}
+\text{curvature commutators involving prior levels}.
\tag{1.7}
\]
The current term is \(U_m*C_1\). There is no \(U_{m+1}\) term and no \(C_{m+2}\) term in the raw cutoff-jet evolution. Norm and volume variation add only \(U_0*|C_{m+1}|^p\).

## 2. Energy closure for exact \(b=\chi^2\)

On a positive-time slab with
\[
\|U_0\|_\infty\le K,
\]
bilipschitz metric control, and the zero-order seed
\[
T_0\in L_t^\infty L_x^q\quad\forall q<\infty,
\]
the finite-order induction closes.

### Weighted pair \((U_m,C_{m+1})\)

Let
\[
V=U_m,\qquad Z=C_{m+1},\qquad
D_{m,p}^U=\int \chi^2|\nabla V|^2|V|^{p-2}.
\]

The current derivative term
\[
B_1*U_{m+1}=2\chi C_1*\nabla V
\]
is absorbed using
\[
|2\chi C_1|^2\le 4|C_1|^2\chi^2.
\]

The current Hessian term
\[
B_2*V=(2\chi C_2+2C_1*C_1)*V
\]
must be treated by signed integration:
\[
\int (\nabla_i\nabla_j b)\,\mathcal B^{ij}(V)
=
-\int (\nabla_j b)\,\nabla_i\mathcal B^{ij}(V),
\]
with
\[
|\mathcal B(V)|\lesssim |V|^p,\qquad
|\nabla\mathcal B(V)|\lesssim |V|^{p-1}|\nabla V|.
\]
Since \(db=2\chi d\chi\),
\[
\left|\int B_2*V*|V|^{p-2}V\right|
\le
\varepsilon D_{m,p}^U
+C_{\varepsilon,p}\|d\chi\|_\infty^2\|V\|_p^p.
\]

The top cutoff term has the form
\[
\chi C_{m+2}*U_0.
\]
After one integration by parts,
\[
\int |V|^{p-2}V*\chi C_{m+2}*U_0
\]
produces
\[
\nabla P(V)*\chi Z*U_0,
\qquad
P(V)*C_1*Z*U_0,
\qquad
P(V)*\chi Z*U_1.
\]
The first two are controlled by \(D_{m,p}^U\), \(\|Z\|_p\), and \(\|V\|_p\). The residual
\[
I_{\rm res}=\int \chi |Z|\,|U_1|\,|V|^{p-1}
\tag{2.1}
\]
is exactly the Step59/A01 Step55 term.

In dimension four,
\[
f=\chi |V|^{p/2}
\]
gives
\[
I_{\rm res}
\le
\|f\|_4\,\|Z\|_p\,\|U_1\|_4\,\|V\|_p^{p/2-1},
\]
and
\[
\|f\|_4^2
\le
C\left(p^2D_{m,p}^U+C_{p,\chi}\|V\|_p^p\right).
\]
Therefore
\[
I_{\rm res}
\le
\varepsilon D_{m,p}^U
+C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{2.2}
\]
For general dimension \(n>2\), the same estimate uses
\[
H^1\hookrightarrow L^{2n/(n-2)}
\]
and \(U_1\in L^n\), which is available from the base block. For \(n=2\), choose any finite Sobolev exponent.

Combining all current terms gives
\[
\frac d{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+cD_{m,p}^U
\le
C_{m,p,\tau}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\tag{2.3}
\]

### Subsequent \(T_m\) estimate

After \((U_m,C_{m+1})\) is known in all finite \(L^q\) spaces, the \(T_m\) equation is tested.

The terms \(B_1*T_{m+1}\) and \(B_2*T_m\) are treated exactly as above: weighted Young for \(B_1\), signed Hessian integration for \(B_2\).

The top cutoff term is
\[
2\chi C_{m+2}*T_0.
\]
One integration by parts gives
\[
C_1*C_{m+1}*T_0*P(T_m),
\qquad
\chi C_{m+1}*T_1*P(T_m),
\qquad
\chi C_{m+1}*T_0*\nabla P(T_m).
\]
For \(m=1\), the middle term is another signed-Hessian term. For \(m\ge2\), \(T_1\) is already a prior-level object. The last term is controlled by weighted dissipation and finite higher exponents of \(C_{m+1}\) and \(T_0\); in Step59 this is simplified further by the positive-time \(T_0\in L^\infty\) bridge.

Thus
\[
\frac d{dt}\|T_m\|_p^p
+cD_{m,p}^T
\le
C_{m,p,\tau}\bigl(1+\|T_m\|_p^p\bigr).
\tag{2.4}
\]

### Result of the enumeration check

At the star-contraction level supplied by Step45, I find no derivative allocation producing a new current object beyond the listed families. In particular:

- no bare \(T_m\) coefficient occurs in the \(U_m\) equation;
- no bare \(T_0*T_m\) coefficient occurs in the \(T_m\) equation;
- no \(C_{m+1}*U_j\) term with \(j\ge2\) occurs in the weighted pair;
- the only top cutoff jet is \(\chi C_{m+2}\), and after one integration its residual is exactly the Step59/A01 Sobolev term;
- the cutoff evolution has current term \(C_1*U_m\), not \(U_{m+1}\).

Unweighted \(T_0\) does appear as prior-level forcing, for example in the \(T_m\) time commutator \(U_m*T_0\) and in lower pieces of \(B_{m+2}*T_0\). These are controlled by the zero-order unweighted \(T_0\in\bigcap_{q<\infty}L^q\) seed and do not act as pointwise coefficients of a current unknown.

## 3. The proposed direct uniqueness estimate

A01 Step56’s proposed estimate
\[
\frac d{dt}\int |g_1-g_2|^2
\le
C\int |g_1-g_2|^2
\tag{3.1}
\]
for the geometric equation without gauge fixing is not valid as written.

The reason is the principal symbol of the Ricci operator. Linearizing
\[
\partial_t g=-2a(\operatorname{Ric}_g+g),
\qquad a=\chi^2,
\]
at a background metric gives, in the second-order part,
\[
DF_g(h)
=
a\bigl(
\Delta h+\nabla^2\operatorname{tr}h
-2\,\operatorname{sym}\nabla(\operatorname{div}h)
\bigr)
+\text{lower order}.
\tag{3.2}
\]
At a covector \(\xi\),
\[
\sigma_\xi(DF)(h)_{ij}
=
a\left(
-|\xi|^2h_{ij}
-\xi_i\xi_j\operatorname{tr}h
+\xi_i\xi^k h_{kj}
+\xi_j\xi^k h_{ki}
\right).
\tag{3.3}
\]
This is the Ricci weakly parabolic symbol. It has gauge kernel
\[
h=\xi\odot v
\quad\Longrightarrow\quad
\sigma_\xi(DF)(h)=0.
\]
More importantly for (3.1), its \(L^2\) quadratic form is not controlled by \(-a|\xi|^2|h|^2+C|h|^2\).

For example, on a flat region with \(a=1\), take \(\xi=e_1\) and
\[
h=\operatorname{diag}(1,-\varepsilon,0,\ldots,0)e^{ikx^1}.
\]
Then the principal contribution to
\[
\frac d{dt}\|h\|_2^2
\]
is proportional to
\[
2k^2(\varepsilon-\varepsilon^2)+O(1)\|h\|_2^2,
\]
which is positive and grows like \(k^2\) for \(0<\varepsilon<1\). No constant \(C\) independent of frequency can give (3.1).

The fixed scalar \(a=\chi^2\) does not add the DeTurck correction. It only multiplies the Ricci symbol. On the plateau where \(\chi=1\), the principal part is exactly that of normalized Ricci flow. The omitted term in the informal line
\[
\delta\operatorname{Ric}(h)=-\tfrac12\Delta_Lh+\text{lower}
\]
is the Lie-derivative gauge term, containing first derivatives of \(h\) inside another derivative. It is a principal term, not lower order.

Thus the displayed direct overlap-uniqueness argument cannot be used to splice a restart from some earlier \(t_j<T^*\).

## 4. Splicing without overlap uniqueness

The all-order energy route can bypass overlap uniqueness if it gives an actual smooth terminal metric.

The required terminal output is:

1. For some fixed background \(\bar\nabla\),
   \[
   g(t)\to g_*
   \quad\text{in }C^\infty(M,\bar g)
   \quad\text{as }t\uparrow T^*.
   \tag{4.1}
   \]
2. The limit \(g_*\) is positive definite.
3. For every \(k\),
   \[
   \sup_{t<T^*}\|\partial_t g(t)\|_{C^k}<\infty,
   \tag{4.2}
   \]
   so the convergence in (4.1) is obtained by Cauchy convergence in each \(C^k\).

The Step45 all-order induction plus fixed-background connection conversion is designed to give exactly this: all \(U_j,T_j\) bounds, then all fixed-coordinate derivatives of \(g\), and
\[
\partial_tg=-2\operatorname{Ric}(U)
\]
bounded in every \(C^k\).

Let
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g).
\]
If \(g(t)\to g_*\) in \(C^\infty\), then
\[
\partial_t g(t)=\mathcal F(g(t))\to \mathcal F(g_*)
\quad\text{in }C^\infty.
\]
Higher time derivatives are recursively determined:
\[
\mathcal F^{[1]}(g)=\mathcal F(g),
\qquad
\mathcal F^{[\ell+1]}(g)
=
D\mathcal F^{[\ell]}_g[\mathcal F(g)].
\tag{4.3}
\]
Each \(\mathcal F^{[\ell]}(g)\) is a differential expression involving finitely many spatial derivatives of \(g\) and \(\chi\). Hence
\[
\lim_{t\uparrow T^*}\partial_t^\ell g(t)
=
\mathcal F^{[\ell]}(g_*)
\quad\text{in }C^\infty
\tag{4.4}
\]
for every \(\ell\).

Now start any smooth local solution \(\hat g(s)\) of the same exact equation with
\[
\hat g(0)=g_*.
\]
Because \(\hat g\) is smooth and solves \(\partial_s\hat g=\mathcal F(\hat g)\),
\[
\partial_s^\ell \hat g(0)=\mathcal F^{[\ell]}(g_*)
\tag{4.5}
\]
for every \(\ell\). Therefore all left and right time jets agree at \(T^*\).

Define
\[
\tilde g(t)=
\begin{cases}
g(t),&t<T^*,\\
\hat g(t-T^*),&t\ge T^*.
\end{cases}
\]
Equations (4.4)–(4.5) imply \(\tilde g\in C^\infty\) in space-time across \(T^*\), and it solves
\[
\partial_t\tilde g=-2\chi^2(\operatorname{Ric}_{\tilde g}+\tilde g)
\]
on both sides and at \(T^*\) by continuity.

Thus a smooth terminal metric plus matching PDE-generated time jets gives a direct smooth splice. No overlap uniqueness is needed. By contrast, a restart from \(g(t_j)\) with \(t_j<T^*\) needs equality with the old branch on \([t_j,T^*)\), and that equality is not supplied by the direct \(L^2\) estimate above.