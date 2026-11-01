# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step40_preceptor_review_step39_interfaces.md"
  ]
}
```

## Task

Read the corrected restricted negative defect gap theorem note (step41_corrected_restricted_defect_gap_theorem.md), focusing on §3 (zero-order unweighted T∈L^p lemma) and §4 (structural equations for the staggered induction). Verify:

1. §3 ZERO-ORDER T LEMMA: Under |U|=|aT|≤K, does the reaction bound a|T|^{p+1} ≤ K|T|^p actually follow? Is the G-evolution term |∂_tG| ≤ Ca|T| correct given ∂_tG = -2a(E⊛g)/(n-1) and E=Ric(T)? Does the Hessian-cutoff signed IBP actually remove the ∇²χ dependence? Is the additive C'_p term genuinely harmless for the continuation application (which only needs finiteness, not multiplicative Gronwall)? Are there missing terms?

2. §4 STRUCTURAL EQUATIONS: Is it true that ∇G=0 because ∇g=0? Does ∇^jT = ∇^jRm for j≥1 follow? In the expansion of ∇^{r+1}a = Σ C_s·C_t (s+t=r+1), is it correct that only the s=0 and t=0 terms use C_{r+1}? Does the cutoff-jet evolution ∂_t C_m (equation 4.6) genuinely avoid C_m and U_m in its RHS? Does ∂_tΓ = g^{-1}*∇Ric(U) introduce at most one derivative of U? Are the dangerous terms (4.12) correctly identified?

3. INTERACTION WITH A03 INDUCTION: Does the structural analysis genuinely show that A03's staggered ordering T_0→(U_1,C_2)→T_1→... has no upward dependencies? Are there additional terms from the Kulkarni-Nomizu product, commutators, or normalization that could defeat the induction?

Provide a direct scientific memo identifying any errors, missing terms, or gaps.

## Output

# Scientific verification memo

## 1. Zero-order unweighted \(T\in L^p\) estimate

### Parts that are correct

Because \(a=\chi^2\ge 0\),
\[
a|T|^{p+1}=|aT|\,|T|^p=|U|\,|T|^p\le K|T|^p.
\]
Thus the quadratic curvature reaction becomes linear in the unweighted \(L^p\) energy under \(\|U\|_\infty\le K\). Likewise,
\[
a|T|^{p-1}=|U|\,|T|^{p-2}\le K|T|^{p-2}.
\]

The \(G\)-evolution is also correct. Symmetry of the Kulkarni–Nomizu product gives
\[
\partial_tG
=\frac{\partial_tg\owedge g+g\owedge\partial_tg}{2(n-1)}
=-\frac{2a}{n-1}(E\owedge g).
\]
Since \(E=\operatorname{Ric}(T)\),
\[
|\partial_tG|\le C_n a|E|\le C_n a|T|=C_n|U|\le C_nK.
\]
When paired against \(|T|^{p-2}T\), this contributes at most
\(C K\int |T|^{p-1}\), hence a linear \(L^p\) term plus a volume term.

### Hessian-cutoff integration by parts

The Step 35 tensors are not literally the tensor arising in the \(T\)-energy, but the same mechanism works. The Hessian contribution has the form
\[
I_H=p\int (\nabla_i\nabla_j a)\,
 |T|^{p-2}\,\mathcal B^{ij}(T,E)\,d\mu,
\]
where
\[
|\mathcal B(T,E)|\le C|T||E|\le C|T|^2,
\]
and, because \(\nabla E\) is a trace of \(\nabla T\),
\[
|\nabla \mathcal B|
 \le C\bigl(|E||\nabla T|+|T||\nabla E|\bigr)
 \le C|T||\nabla T|.
\]
After one integration by parts,
\[
|I_H|
\le \varepsilon\int a|T|^{p-2}|\nabla T|^2
 +C_{p,\varepsilon}\int\frac{|\nabla a|^2}{a}|T|^p.
\]
For \(a=\chi^2\),
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2}
\]
where \(a>0\), with the quotient extended by zero where \(a=0\). For the global sum of disjoint squared cutoffs, the same estimate holds support by support. Thus no pointwise \(\nabla^2\chi\) estimate is needed.

The current text should display this \(T*E\) contraction explicitly rather than citing \(B_{\rm curv}\) and \(B_{\rm def}\), which arise from different tested quantities.

### A term omitted from the written energy computation

Differentiating the tensor norm introduces inverse-metric variation:
\[
\partial_t|T|^p
=p|T|^{p-2}\langle \partial_tT,T\rangle
 +O\!\left(p\,a|E|\,|T|^p\right).
\]
Under \(|U|\le K\),
\[
a|E|\le C|aT|=C|U|\le CK,
\]
so this missing term is bounded by \(C_pK\int|T|^p\). It does not alter the estimate, but it must appear in a complete derivation.

The volume term is similarly controlled directly by
\[
|a\,\operatorname{tr}E|\le C|aE|\le CK.
\]
The extra \(Ca\) used in §3 is unnecessary because \(aE=\operatorname{Ric}(U)\) exactly.

### Additive term

The additive term is harmless for the stated continuation use, provided it is uniform on the finite slab. One may write it concretely as
\[
C_{n,p}(1+K^{\alpha_p})\sup_{t\in[\tau,T_*)}\operatorname{Vol}(g(t)).
\]
Since \(|\partial_tg|\le C K\), finite \(T_*-\tau\) gives bilipschitz and volume comparison. Smoothness at time \(\tau>0\) gives \(\|T(\tau)\|_p<\infty\). Gronwall then supplies a uniform finite bound up to \(T_*\); a purely multiplicative inequality is not required.

The phrase “bounded metric data” is too imprecise here: the constant must not depend on curvature derivatives that the continuation argument is trying to obtain. Volume, the finite time length, \(K\), and the transported gradient bound for \(a\) suffice.

Two smaller corrections are needed:

- If Lemma 3.1 is presented for general \(n\), then \(\operatorname{tr}E=s+n\), not \(s+4\).
- The space-form discussion does not verify stationarity for every Einstein metric with \(\operatorname{Ric}=-g\). For a general such metric, \(T\) need not be parallel. The full elliptic curvature identity makes the diffusion, quadratic, and normalization pieces cancel. This does not affect the energy estimate.

## 2. Structural identities

### Parallelism of \(G\)

At each fixed time,
\[
\nabla g=0\quad\Longrightarrow\quad \nabla G=0,\qquad \Delta G=0.
\]
Consequently,
\[
\nabla^jT=\nabla^j\operatorname{Rm},\qquad j\ge1.
\]
This is a spatial identity at one time. It does not mean
\(\nabla^j(\partial_tG)=0\). Rather,
\[
0=\partial_t(\nabla^jG)
=[\partial_t,\nabla^j]G+\nabla^j(\partial_tG).
\]
An exact temporal derivation must retain this cancellation. Since
\(\partial_tG\) is algebraic in \(\operatorname{Ric}(U)\), it introduces at most the current \(U_j\), never \(U_{j+1}\).

### Derivatives of \(a=\chi^2\)

The Leibniz expansion is correct:
\[
\nabla^{r+1}a
=\sum_{s+t=r+1}\binom{r+1}{s}C_s*C_t.
\]
Only the allocations \(s=0\) and \(t=0\) contain \(C_{r+1}\); together they give
\[
2\chi C_{r+1}.
\]
Every other allocation uses cutoff jets of order at most \(r\).

### Connection variation

Equation (4.3) has the wrong sign and normalization. If
\(S=\operatorname{Ric}(U)\) and \(\partial_tg=-2S\), then
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}
 \left(\nabla_iS_{j\ell}+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\right).
\]
The derivative-order conclusion survives: the raw connection variation contains exactly one derivative of \(U\), because \(S\) is an algebraic trace of \(U\).

### Cutoff-jet evolution

For an ordered covariant derivative \(C_m=\nabla^m\chi\),
\[
\partial_t C_m
=\sum_{\ell=0}^{m-2}\nabla^\ell(\partial_t\Gamma)
   *C_{m-1-\ell}.
\]
The top term is
\[
\nabla^{m-2}(\partial_t\Gamma)*C_1
=U_{m-1}*C_1+\text{lower-order commutators}.
\]
Thus the raw evolution of \(C_m\) contains neither \(U_m\) nor \(C_m\). In the \(L^p\) energy of \(C_m\), inverse-metric and volume variation do produce an algebraic \(U_0*C_m\) term, exactly as A03 §2.4 records.

### Lost factor in §4.4

From
\[
\partial_tU=a\,\partial_tT,\qquad
\partial_tT\supset a\Delta T,
\]
the leading term is
\[
\partial_tU\supset a^2\Delta T,
\]
not \(a\Delta T\). After rewriting through \(U=aT\), its principal part is indeed
\[
a\Delta U.
\]
The sentence following (4.9) drops one factor of \(a\) before this conversion. The final degenerate principal operator is plausible, but the displayed derivation is algebraically incomplete.

### The high-cutoff-jet list (4.12) is incomplete

Derivative accounting gives three relevant top allocations:
\[
\boxed{
\chi C_{m+2}*U_0,\qquad
C_1*C_{m+1}*U_0,\qquad
\chi C_{m+1}*U_1.}
\]
The third term is absent from (4.12). It occurs directly from
\(\nabla^{m+1}a*U_1\), and it is also produced when
\(\chi C_{m+2}*U_0\) is integrated by parts.

This omitted term is precisely the term treated in A03 equation (2.6). For \(m\ge2\), it requires the additional integration by parts
\(C_{m+1}=\nabla C_m\); for \(m=1\), it joins the signed Hessian term. Therefore the statement that one integration by parts on the \(C_{m+2}\) term completes the treatment is insufficient.

No cutoff jet above \(C_{m+2}\) can occur, and no term
\(C_{m+2}*U_j\) with \(j\ge1\) is compatible with the total derivative count.

## 3. Interaction with the A03 ordering

After inserting the missing \(\chi C_{m+1}U_1\) term, the derivative ordering remains mathematically coherent:

- \(\chi C_1U_{m+1}\) is absorbed by the weighted diffusion.
- \(\chi C_2U_m\) is treated by Hessian integration by parts.
- \(\chi C_{m+2}U_0\) and \(\chi C_{m+1}U_1\) are handled by the two integrations in A03 §2.2.
- The \(C_{m+1}\)-equation uses \(U_m\) but not \(U_{m+1}\).
- The subsequent \(T_m\)-equation may use \(U_m\) and \(C_{m+1}\), already obtained at that stage.

Kulkarni–Nomizu terms, normalization, and commutators do not visibly introduce an upward derivative:

- \(\nabla^m(\partial_tG)\) is algebraic in \(U_m\).
- Normalization contributes derivatives no higher than the current order.
- Time-connection commutators have top form \(U_m*U_0\).
- Laplacian commutators have current terms multiplied by \(aT_0=U_0\), while the remaining factors occur at earlier spatial levels.
- Reordering cutoff derivatives produces curvature times lower cutoff jets, covered by previously obtained \(T_j\) norms.

Thus the ordering
\[
T_0\longrightarrow (U_1,C_2)\longrightarrow T_1
\longrightarrow (U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
\]
has a viable triangular structure. However, §4 by itself does not establish the all-order energy inequalities: equation (4.10) records derivative counts but does not track the indispensable placement of the factor \(a\), especially where a current unweighted curvature factor must appear as \(aT_0=U_0\). The A03 formulas contain that finer bookkeeping, while Step 41 only summarizes it.

Finally, §5.1 explicitly leaves the transported DeTurck start/restart estimates and regularization limit unwritten. The continuation statement, and hence Theorem 1.1 as displayed, does not follow from the present file alone. There is also a quantifier mismatch: Theorem 1.1 fixes \(X,A,k\), whereas §1 begins with varying \(X_i,A_i,k_i\) and \(A_i\to\infty\). Those are different mathematical statements.