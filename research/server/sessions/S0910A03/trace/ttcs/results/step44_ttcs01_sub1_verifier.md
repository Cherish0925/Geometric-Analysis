# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step43_general_order_unweighted_T_estimate.md",
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A03/workspace/scripts/verify_step44_weight_and_schedule.py"
  ]
}
```

## Task

Independently verify the repaired continuation seed and higher-order allocation. Read the Step 44 zero-order T note together with the Step 40 staggered induction and the corrected Step 43 note. Check the exact zero-order shifted-curvature energy structure under |U|=|aT|<=K: quadratic reaction, inverse-metric and volume variation, signed Hessian-a contraction, gradient terms, and whether the resulting unweighted L^p bound truly supplies T_0 uniformly up to a finite maximal endpoint. Then check that higher connection-variation terms should be kept as derivatives of Ric(U), and whether the m=1 signed Hessian treatment plus the arbitrary-order schedule closes without any hidden pointwise T assumption or current-exponent escalation. Identify any tensor term or logical dependence that remains unproved; give corrections rather than accepting schematic equations.

## Output

# Scientific verification memo

## 1. Zero-order shifted-curvature estimate

Let
\[
S=\operatorname{Ric}(U)=aE,\qquad \partial_tg=-2S,\qquad
T=\operatorname{Rm}+G,\qquad U=aT,\qquad a=\chi^2.
\]
Because \(\operatorname{Ric}(T)=E\),
\[
|S|=|\operatorname{Ric}(U)|\le C_n|U|\le C_nK. \tag{1}
\]

### Curvature evolution

For a metric variation \(\partial_tg=-2S\), the covariant curvature tensor satisfies
\[
\partial_t\operatorname{Rm}=\mathscr D^2S+\operatorname{Rm}*S,
\]
where \(\mathscr D^2S\) is the usual four-term second-derivative expression. Substitution of \(S=aE\) gives
\[
\mathscr D^2(aE)
=a\,\mathscr D^2E+\nabla a*\nabla E+(\nabla^2a)*E.
\]
The contracted Bianchi identity converts \(a\mathscr D^2\operatorname{Ric}\) into
\[
a\Delta\operatorname{Rm}+a\,\operatorname{Rm}*\operatorname{Rm}.
\]
Since
\[
\nabla E=\operatorname{Ric}(\nabla T),\qquad
\operatorname{Rm}=T-G,\qquad \nabla G=0,
\]
this has precisely the structural form used in Step 44:
\[
\partial_tT
=a\Delta T+a\,\mathcal P_2(T,G)
+\nabla a*\nabla T
+\mathscr H(\nabla^2a,E)
+a\,\mathcal P_1(T,G), \tag{2}
\]
where \(\mathcal P_2\) has degree at most two in \(T,G\), and every algebraic reaction carries \(a\).

With the stated normalization of the Kulkarni product,
\[
\partial_tG=-\frac{2a}{n-1}(E\owedge g), \tag{3}
\]
so
\[
|\partial_tG|\le C_na|E|\le C_n|U|.
\]
Thus equations (1.1)–(1.3) of Step 44 have the correct tensor structure. Exact numerical coefficients are immaterial for the energy inequality, but the factor \(a\) in every algebraic reaction is essential.

### Quadratic reaction

Testing the quadratic part against \(p|T|^{p-2}T\) produces
\[
C_{n,p}\int a|T|^{p+1}.
\]
Since \(a\ge0\),
\[
a|T|^{p+1}=|aT|\,|T|^p=|U|\,|T|^p
\le K|T|^p. \tag{4}
\]
This is the decisive reduction. No division by \(a\) occurs.

The lower powers satisfy, assuming the standard cutoff normalization \(0\le\chi\le1\),
\[
a|T|^p+a|T|^{p-1}
\le C_p(1+|T|^p). \tag{5}
\]
If \(\chi\) is not normalized this way, the constants in Step 44 must also depend on \(\|a\|_\infty\).

### Inverse-metric and volume variations

For the covariant rank-four tensor \(T\),
\[
\partial_t|T|^p
=p|T|^{p-2}\langle\partial_tT,T\rangle
+\mathcal M_p(S,T),
\]
where
\[
|\mathcal M_p(S,T)|\le C_{n,p}|S||T|^p
\le C_{n,p}K|T|^p. \tag{6}
\]
Also,
\[
\partial_t d\mu=-\operatorname{tr}(S)\,d\mu,
\qquad
|\operatorname{tr}S|\le C_nK. \tag{7}
\]
Therefore both terms in Step 44 §2 are controlled solely by \(K\), without an unweighted pointwise estimate for \(T\).

### Diffusion and first derivatives of \(a\)

Integration by parts gives
\[
\begin{aligned}
p\int a|T|^{p-2}\langle\Delta T,T\rangle
={}&-p\int a|T|^{p-2}|\nabla T|^2\\
&-p(p-2)\int a|T|^{p-4}|\langle\nabla T,T\rangle|^2
+J_a ,
\end{aligned}
\]
with
\[
|J_a|\le C_{n,p}\int|\nabla a|\,|T|^{p-1}|\nabla T|. \tag{8}
\]
The explicit \(\nabla a*\nabla T\) terms have the same form. Since
\[
\nabla a=2\chi\,d\chi,\qquad
\frac{|\nabla a|^2}{a}=4|d\chi|^2 \tag{9}
\]
where \(\chi\ne0\), Young’s inequality yields
\[
|J_a|
\le\varepsilon\int a|T|^{p-2}|\nabla T|^2
+C_{n,p,\varepsilon}\|d\chi\|_\infty^2\int|T|^p. \tag{10}
\]
For a smooth cutoff \(\chi\ge0\), \(d\chi=0\) wherever \(\chi=0\), so (9) extends harmlessly over that set.

### Signed Hessian-\(a\) contraction

The Hessian part has the form
\[
I_H=p\int(\nabla_i\nabla_ja)\,
B^{ij}(T,E)|T|^{p-2}\,d\mu, \tag{11}
\]
with
\[
|B(T,E)|\le C_n|T||E|\le C_n|T|^2.
\]
Because covariant differentiation commutes with metric trace,
\[
\nabla E=\operatorname{Ric}(\nabla T),
\]
and hence
\[
|\nabla B(T,E)|\le C_n|T||\nabla T|. \tag{12}
\]
One integration by parts gives
\[
I_H=-p\int(\nabla_ja)\,
\nabla_i\!\left(B^{ij}(T,E)|T|^{p-2}\right)d\mu,
\]
and therefore
\[
|I_H|
\le C_{n,p}\int|\nabla a|\,|T|^{p-1}|\nabla T|
\le\varepsilon\mathcal D_p
+C_{n,p,\varepsilon}\|d\chi\|_\infty^2\mathcal T_p. \tag{13}
\]
Thus no pointwise estimate for \(\nabla^2\chi\) enters. This part of the repair is valid.

For arbitrary real \(p\ge2\), a fully rigorous presentation can test with
\[
(|T|^2+\eta)^{(p-2)/2}T
\]
and pass to \(\eta\downarrow0\); this regularization is not written in the notes but is standard.

## 2. Uniformity up to a finite endpoint

Combining the preceding estimates gives
\[
\frac d{dt}\mathcal T_p+c_{n,p}\mathcal D_p
\le A_{n,p}\mathcal T_p+B_{n,p}\operatorname{Vol}(g(t)), \tag{14}
\]
where
\[
A_{n,p}=C_{n,p}\bigl(K+1+\sup_{[\tau,T_*)}\|d\chi\|_\infty^2\bigr).
\]

Equation (1) implies
\[
|\partial_tg|_g\le C_nK,
\]
so on the finite slab \([\tau,T_*)\),
\[
e^{-C_nK(T_*-\tau)}g(\tau)
\le g(t)\le
e^{C_nK(T_*-\tau)}g(\tau). \tag{15}
\]
Consequently, both \(\|d\chi\|_{g(t),\infty}\) and \(\operatorname{Vol}(g(t))\) are uniformly finite. Since \(M\) is compact and the solution is smooth at \(\tau\),
\[
\mathcal T_p(\tau)<\infty.
\]
Gronwall gives the explicit endpoint-uniform estimate
\[
\sup_{\tau\le t<T_*}\mathcal T_p(t)
\le e^{A_{n,p}(T_*-\tau)}
\left[
\mathcal T_p(\tau)
+B_{n,p}V_*(T_*-\tau)
\right]<\infty, \tag{16}
\]
where \(V_*=\sup_{[\tau,T_*)}\operatorname{Vol}(g(t))\).

Thus Step 44 genuinely supplies \(T_0\in L^p\) for every finite \(p\ge2\), uniformly up to \(T_*\). It is a per-datum estimate: its constants depend on \(\tau\), \(K\), the initial \(L^p\) norm, and the cutoff. No finite-total-curvature argument is involved.

## 3. Higher connection variation

The clean formula is obtained by retaining \(U\). With \(S=\operatorname{Ric}(U)\),
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}
\bigl(\nabla_iS_{j\ell}+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\bigr). \tag{17}
\]
Because \(\nabla g^{-1}=0\), ordered covariant derivatives satisfy
\[
\nabla^\ell(\partial_t\Gamma)
=g^{-1}*\nabla^{\ell+1}\operatorname{Ric}(U). \tag{18}
\]
Since metric trace commutes with \(\nabla\), the top factor is \(U_{\ell+1}\).

Accordingly,
\[
[\partial_t,\nabla^m]T
=\sum_{\ell=0}^{m-1}
U_{\ell+1}*T_{m-1-\ell}, \tag{19}
\]
up to the finite tensor-slot multiplicities. At \(\ell=m-1\), the top product is
\[
U_m*T_0, \tag{20}
\]
not an unweighted \(T_m*T_0\) coefficient. At the \(T_m\) stage, \(U_m\) is already known in every finite \(L^q\), while \(T_0\) is supplied by (16). Thus
\[
\int |U_m||T_0||T_m|^{p-1}
\le \|U_m\|_{2p}\|T_0\|_{2p}\|T_m\|_p^{p-1}. \tag{21}
\]
No pointwise \(T_0\) estimate is needed.

Step 43 equation (4.2), with schematic quadratic \(T*T\) terms inside \(\nabla^j(\partial_t\Gamma)\), is not the exact geometric identity. Formula (18) is the correct replacement. Curvature products appear only if derivative orders are subsequently commuted.

## 4. The \(m=1\) signed Hessian correction

Step 43 §3 contains a sentence asserting that, for \(m=1\),
\[
\chi C_2\,T_1\,P(T_1)
\]
is controlled because \(C_2\) is bounded. Uniform \(L^\infty\) control of \(C_2\) is not available at that stage; obtaining it from later derivatives would be circular.

Writing \(X=T_1\), the required treatment is instead
\[
J=\int\chi\,\nabla_i\nabla_j\chi\,
B^{ij}(X)|X|^{p-2}.
\]
With
\[
|B(X)|\le C|X|^2,\qquad
|\nabla B(X)|\le C|X||\nabla X|,
\]
integration by parts gives
\[
|J|
\le C_p\|d\chi\|_\infty^2\|X\|_p^p
+\varepsilon\int\chi^2|\nabla X|^2|X|^{p-2}. \tag{22}
\]
This is exactly the signed mechanism described later in Step 43 §9 and in Step 40. Equation (22), rather than an \(L^\infty\) estimate for \(C_2\), is required in the \(m=1\) argument.

## 5. Arbitrary-order allocation

The Step 40 ordering
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
\]
has the correct exponent structure.

For \(V=U_m\) and \(Z=C_{m+1}\):

1. \(\chi C_1U_{m+1}\) is absorbed by the weighted dissipation.
2. \(\chi C_2V\) is treated by the signed estimate analogous to (22).
3. The sole \(C_{m+2}\) term is \(\chi C_{m+2}U\). One integration by parts leaves \(Z\), not \(C_{m+2}\).
4. The resulting term \(\chi ZU_1P(V)\) is integrated once more for \(m\ge2\). Its factors \(C_m\) and \(U_1\) are from earlier levels. For \(m=1\), it is again of the form (22).
5. The only simultaneous current-pair products are
   \[
   |Z|^2|V|^{p-2},
   \qquad |Z||V|^{p-1},
   \]
   both controlled with \(Z,V\in L^p\).

The raw cutoff-jet evolution has the structure
\[
\partial_tC_{m+1}
=\sum_{\ell=0}^{m-1}
\nabla^\ell(\partial_t\Gamma)*C_{m-\ell}. \tag{23}
\]
Its top term is \(U_m*C_1\); inverse-metric and volume variations add the bounded coefficient \(U_0*C_{m+1}\). Hence the coupled \(L^p\) system for \((U_m,C_{m+1})\) closes at the same exponent.

At the subsequent \(T_m\) stage, the term
\[
\chi C_{m+2}T\,P(T_m)
\]
is integrated once. The last resulting term is bounded through
\[
\int |C_{m+1}|^2|T|^2|T_m|^{p-2}
\le
\|C_{m+1}\|_{2p}^2\|T\|_{2p}^2\|T_m\|_p^{p-2}. \tag{24}
\]
Here \(C_{m+1}\) and \(T\) belong to completed levels and are already available at exponent \(2p\). The current variable \(T_m\) remains at exponent \(p\).

Laplacian commutators also do not introduce pointwise \(T\): their current-order algebraic part is
\[
a\,\operatorname{Rm}*T_m=(U-aG)*T_m,
\]
whose coefficient is bounded by \(K+C_n\). Lower derivative products are handled with finite Hölder exponents from earlier levels.

If covariant derivatives of \(C_{m+1}\) must be reordered before integration by parts, iterated commutators have the form
\[
\nabla^q\operatorname{Rm}*C_s,\qquad q+s\le m-1,
\]
so only \(T_q\) with \(q<m\) occurs. This is compatible with the staggered ordering.

## 6. Material still absent from the supplied derivation

- Step 40 equations (1.4) and (1.5) are schematic. The energy allocation is internally consistent, but the notes contain no indexed all-order derivation proving that every contraction belongs to the displayed tensor classes. The most relevant missing ledger concerns the reordering terms in the second integration by parts and the full Laplacian commutator.
- The sentence in Step 43 §3 using an \(L^\infty\) estimate for \(C_2\) must be replaced by (22).
- The derivative estimates yield a smooth terminal metric: all \(U_m\) become pointwise bounded by Sobolev embedding, so every spatial derivative of \(\partial_tg=-2\operatorname{Ric}(U)\) is integrable in time. Extension beyond \(T_*\), however, also uses the separate transported-coefficient DeTurck short-time theorem, whose tame estimates and restart construction are not supplied.
- `verify_step44_weight_and_schedule.py` correctly checks scalar weights and Hölder arithmetic, but, as its final output states, it does not verify tensor provenance, the signed contractions, or PDE existence.

In summary, the Step 44 seed is valid and gives the required endpoint-uniform, per-datum \(T_0\) norms. The higher-order exponent ordering contains no hidden pointwise \(T\) input once connection variation is retained as \(\nabla^{j+1}\operatorname{Ric}(U)\), and the \(m=1\) terms are handled by signed integration by parts. The remaining mathematical substance is an indexed derivation of the all-order schematic evolution families and the independent transported DeTurck start/restart theorem.