# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Verify the H-WU resolution for the weighted cutoff flow U_m = nabla^m(chi^2(Rm+G)) under dt g = -2 chi^2 (Ric+g). The central claim (Proposition §5) is: in the evolution equation for U_m, the UNIQUE source of the single cutoff jet C_{m+2} = nabla^{m+2}chi is from the Hessian-a contraction in the Lichnerowicz variation, giving the form 2*chi*C_{m+2} * (aE) plus products of lower jets. All other terms (commutator, G-variation, normalization, reaction, outer Leibniz j>=1) produce single jets of order <= m+1. Verify: (1) The product-rule identity nabla^k(chi^2) = sum_{s=0}^k C(k,s) C_s C_{k-s} and its top jet 2*chi*C_k. (2) The factorization a*(nabla^2 a)*E = (nabla^2 a)*(aE) and why this preserves chi weight after m derivatives. (3) The commutator bound max single jet = C_m from [dt, nabla^m]U. (4) That the chi factor in 2*chi*C_{m+2} is essential for pairing with weighted dissipation int chi^2|nabla U_m|^2|U_m|^{p-2} via Cauchy-Schwarz, and that bare C_{m+2} would fail. (5) Whether any curvature-commutator correction from reordering covariant derivatives in the Leibniz expansion could introduce an unaccounted C_{m+2} term.

## Output

## Scientific verification memo

### Main finding

The weight property required by the staggered energy estimate is valid:

\[
\text{every explicit }C_{m+2}\text{ term has the form }
\chi\, C_{m+2}*\mathcal A(U),
\]

where \(\mathcal A(U)\) is an algebraic contraction of \(U\), including
\(aE=\operatorname{Ric}(U)\). No bare \(C_{m+2}*\mathcal A(U)\) is generated.

The uniqueness statement in Step 43 §5 needs one amendment. It is valid for the raw expression

\[
\partial_tU_m=\nabla^m(a\,\partial_tT)+[\partial_t,\nabla^m]U,
\]

before the principal term is rewritten as \(a\Delta U_m\). In the parabolic form used to obtain the weighted dissipation, converting \(a^2\Delta T\) into \(a\Delta U\) creates an additional top-jet source \(-(\Delta a)U\). This source also has the required \(\chi C_{m+2}\) weight.

---

### 1. Derivatives of \(a=\chi^2\)

For an ordered multi-index \(I=(i_1,\dots,i_k)\), the exact covariant Leibniz formula is a sum over subsets:

\[
\nabla_I(\chi^2)
=
\sum_{S\subseteq\{1,\dots,k\}}
(\nabla_{I_S}\chi)\,\widetilde\otimes_S\,
(\nabla_{I_{S^c}}\chi),
\]

with derivative order inherited from \(I\) and tensor slots placed according to \(S\). If derivatives are symmetrized, this becomes the binomial notation

\[
\nabla^k(\chi^2)
=
\sum_{s=0}^k \binom{k}{s}
\operatorname{Sym}\!\left(C_s\otimes C_{k-s}\right).
\]

Thus Step 43 (1.2) is exact with symmetrization or shuffle placement understood; as an equality of ordered tensors with one fixed \(\otimes\), it is only schematic.

For \(k\ge1\), the two endpoint allocations are

\[
\chi C_k+C_k\chi=2\chi C_k.
\]

Every proper allocation has the form \(C_s*C_{k-s}\) with

\[
1\le s\le k-1,
\]

so neither factor has order \(k\). Therefore

\[
\boxed{\nabla^k a=2\chi C_k+
\sum_{1\le s\le k-1}C_s*C_{k-s}}
\]

at the top-jet level. This verifies the factor \(2\chi\).

---

### 2. Hessian-\(a\) source and preservation of the \(\chi\) factor

Let \(\mathcal H(A,E)\) denote the Hessian contraction displayed in Step 35 (2.7). It is bilinear in \(A=\nabla^2a\) and \(E\). Since \(a\) is a scalar,

\[
a\,\mathcal H(\nabla^2a,E)
=
\mathcal H(\nabla^2a,aE).
\]

Moreover,

\[
aE
=
a\,\operatorname{Ric}(T)
=
\operatorname{Ric}(aT)
=
\operatorname{Ric}(U),
\]

so

\[
|aE|\le c_n|U|.
\]

In

\[
a\nabla^m\mathcal H(\nabla^2a,E),
\]

the only allocation containing \(m+2\) derivatives of \(a\) is the one putting all \(m\) derivatives on \(\nabla^2a\):

\[
a\,\mathcal H(\nabla^{m+2}a,E)
=
\mathcal H(\nabla^{m+2}a,aE).
\]

Consequently,

\[
\mathcal H(\nabla^{m+2}a,aE)
=
2\chi\,\mathcal H(C_{m+2},aE)
+
\sum_{1\le s\le m+1}
C_s*C_{m+2-s}*(aE).
\]

Every other outer Leibniz allocation has an individual cutoff jet of order at most

\[
\max\{j,m-j+2\}\le m+1,\qquad j\ge1.
\]

Thus the Hessian-variation contribution has exactly the desired top weight.

---

### 3. Additional \(C_{m+2}\) source in parabolic form

From Step 43 (2.4), write schematically

\[
(\partial_t-a\Delta)T
=
\mathcal H(\nabla^2a,E)
+\mathcal G(\nabla a,\nabla E)
+\text{lower-order terms}.
\]

Because \(U=aT\),

\[
\begin{aligned}
(\partial_t-a\Delta)U
&=a(\partial_t-a\Delta)T
-a(\Delta a)T-2a\nabla a*\nabla T\\
&=\mathcal H(\nabla^2a,aE)
-(\Delta a)U
-2\nabla a*\nabla U
+2\frac{|\nabla a|^2}{a}U
+\cdots .
\end{aligned}
\]

Here

\[
\frac{|\nabla a|^2}{a}=4|d\chi|^2
\]

extends smoothly across \(\chi=0\).

After applying \(\nabla^m\), the term

\[
-\nabla^m((\Delta a)U)
\]

has the additional top allocation

\[
-(\nabla^m\Delta a)*U
=
-2\chi\,\operatorname{tr}(C_{m+2})*U
+\text{lower cutoff jets}.
\]

Therefore the parabolic \(U_m\) equation has at least two tensorial sources of order \(C_{m+2}\):

\[
2\chi\,\mathcal H(C_{m+2},aE),
\qquad
-2\chi\,\operatorname{tr}(C_{m+2})*U.
\]

Both are of the common form \(\chi C_{m+2}*U\), since \(aE=\operatorname{Ric}(U)\). This is precisely the form needed in A03 Step 40 (2.4), but the provenance is not solely the original Hessian contraction once \(a\Delta U_m\) is isolated.

---

### 4. Time–connection commutator

For a covariant tensor \(U\),

\[
[\partial_t,\nabla^m]U
=
\sum_{q=0}^{m-1}
\nabla^q(\partial_t\Gamma)*
\nabla^{m-1-q}U,
\]

with contractions over the tensor and derivative slots. Under
\(h=-2aE\),

\[
\partial_t\Gamma
=
g^{-1}*\nabla(aE).
\]

Hence

\[
\nabla^q(\partial_t\Gamma)
=
g^{-1}*\nabla^{q+1}(aE)+\text{curvature-reordering terms}.
\]

Expanding the explicit cutoff factors gives a largest individual jet \(C_{q+1}\). Also,

\[
\nabla^{m-1-q}U
=
\nabla^{m-1-q}(aT)
\]

contains cutoff jets of order at most \(C_{m-1-q}\). Therefore

\[
\max\{q+1,m-1-q\}\le m,
\qquad 0\le q\le m-1.
\]

Thus

\[
\boxed{[\partial_t,\nabla^m]U
\text{ contains no explicit }C_{m+1}\text{ or }C_{m+2}.}
\]

Writing \(\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)\) makes this even clearer: the commutator can be organized directly in derivatives of \(U\), with no explicit cutoff jet arising from \(\partial_t\Gamma\).

---

### 5. Pairing with weighted dissipation

Let \(V=U_m\) and \(P(V)=|V|^{p-2}V\). A top source has the form

\[
I=\int \chi C_{m+2}*\mathcal A(U)*P(V),
\qquad |\mathcal A(U)|\le C|U|\le CK.
\]

After integrating one derivative from \(C_{m+2}\),

\[
I
=
-\int C_{m+1}*
\nabla\!\left[\chi\mathcal A(U)P(V)\right].
\]

The term in which the derivative hits \(P(V)\) satisfies

\[
|\nabla P(V)|
\le (p-1)|V|^{p-2}|\nabla V|.
\]

The equality asserted in Step 43 §6 should be replaced by this tensor norm inequality. It is sufficient:

\[
\begin{aligned}
&\int \chi |C_{m+1}|\,|\mathcal A(U)|
|V|^{p-2}|\nabla V|\\
&\qquad\le
\varepsilon
\int\chi^2|\nabla V|^2|V|^{p-2}
+
C_{p,\varepsilon}K^2
\int |C_{m+1}|^2|V|^{p-2}.
\end{aligned}
\]

The final integral uses the current coupled \(L^p\) norms:

\[
\int |C_{m+1}|^2|V|^{p-2}
\le
\|C_{m+1}\|_p^2\|V\|_p^{p-2}
\le
C\bigl(\|C_{m+1}\|_p^p+\|V\|_p^p\bigr).
\]

Thus Step 43’s reference to a previously established \(L^{2p}\) norm for \(C_{m+1}\) is unnecessary and has the wrong staggered indexing; \(C_{m+1}\) is part of the current pair.

For a bare source \(C_{m+2}*\mathcal A(U)\), integration by parts would instead require

\[
\int |C_{m+1}|\,|\mathcal A(U)|
|V|^{p-2}|\nabla V|.
\]

Pairing with \(\chi^2|\nabla V|^2|V|^{p-2}\) introduces

\[
\frac{|\mathcal A(U)|^2}{\chi^2}.
\]

The hypothesis \(|U|\le K\) gives no control of \(U/\chi=\chi T\) or
\((aE)/\chi=\chi E\) near \(\chi=0\). Hence the weighted Young estimate does not close without the explicit \(\chi\).

---

### 6. Curvature reordering

The Leibniz formula itself needs no curvature correction if derivative order is retained. Curvature terms appear only when derivatives are permuted into a chosen canonical ordering.

For a tensor \(\nabla^r a\),

\[
[\nabla_i,\nabla_j](\nabla^r a)
=
\operatorname{Rm}*\nabla^r a.
\]

An adjacent interchange replaces two covariant derivatives by a curvature factor. Thus reordering an order-\((m+2)\) derivative of \(a\) produces terms schematically of the form

\[
\nabla^q\operatorname{Rm}*\nabla^{m-q}a,
\]

whose largest cutoff derivative is at most \(C_m\). Expanding
\(\nabla^{m-q}a\) into derivatives of \(\chi\) cannot restore a
\(C_{m+2}\) factor.

Likewise, commuting \(\nabla^m\) with \(\Delta\) produces curvature derivatives times lower derivatives of \(U\), not an additional \(C_{m+2}\).

---

### Corrected top-jet statement

The tensor structure supported by the supplied equations is:

\[
\boxed{
(\partial_t-a\Delta)U_m
\text{ has all of its }C_{m+2}\text{ contributions in }
2\chi C_{m+2}*\mathcal A(U),
}
\]

where \(\mathcal A(U)\) consists of algebraic contractions of \(U\), including \(\operatorname{Ric}(U)=aE\). All remaining explicit cutoff jets have order at most \(m+1\), while the time–connection commutator has order at most \(m\).

This corrected formulation supplies exactly the weight required by the staggered energy mechanism.