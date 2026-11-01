# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step60_base_pair_proof.md",
    "Sessions/S0910A01/workspace/notes/step59_induction_ledger_repair.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md"
  ]
}
```

## Task

Verify the base-pair continuation proof in step60_base_pair_proof.md. The critical mathematical claims to check:

1. **C₂ evolution (§3):** The note claims ∂ₜC₂ = g^{-1}*U₁*C₁ with no U₂ term. The derivation: ∂ₜΓ = g^{-1}*∇(aE), and ∇(aE) = ∇(Ric(U)) = g^{-1}*U₁. Then [∂ₜ,∇²]χ = (∂ₜΓ)*∇χ = g^{-1}*U₁*C₁. Is this correct? In particular: (a) Is ∇(aE) really g^{-1}*U₁ without any U₀ or B₁ terms? The Ricci contraction of ∇U involves only U₁? (b) When computing [∂ₜ,∇²]χ, does ∂ₜΓ acting on ∇χ really give only U₁*C₁, not U₂? Note that ∇²χ involves Γ acting on ∇χ, and ∂ₜΓ = g^{-1}*U₁, so the commutator should be g^{-1}*U₁*C₁. But could there be a ∇(∂ₜΓ) term? Since ∇²χ = ∇(∇χ), and ∂ₜ∇ = ∂ₜΓ, the commutator [∂ₜ,∇] acting on ∇χ gives (∂ₜΓ)*∇χ. No derivative of ∂ₜΓ appears because ∇²χ = ∇(∇χ) and ∂ₜ only hits the connection once.

2. **m=1 signed-Hessian resolution (§2.3–2.6):** The note claims that the B₃*U₀ term, after integration by parts of C₃=∇C₂, produces a signed contraction ∫χ∇ᵢ∇ⱼχ B^{ij}(V) that the A03 lemma handles. Check: (a) After ∫χ|V|^{p-2}V*C₃*U₀ and IBP, the third term is -2∫χ|V|^{p-2}V*V*C₂. Is this really of the signed form ∫χ∇ᵢ∇ⱼχ B^{ij}(V) where B^{ij}(V) is a contraction of |V|^{p-2}V⊗V? (b) The note says 'This IS of the signed form (1.1)' — verify that the tensor indices work out: C₂ = ∇²χ = ∇ᵢ∇ⱼχ, and |V|^p*C₂ means a specific contraction. Can every such contraction be written as B^{ij}(V) with the required bounds |B|≤C|V|^p, |∇B|≤Cp|V|^{p-1}|∇V|?

3. **m=1 Hessian terms (§2.6):** The B₂*V terms from the principal operator and drift give ∫χ C₂*V*|V|^{p-2}V. The note claims this is also of the signed-Hessian form. Verify.

4. **Base order non-circularity:** The proof uses U₁ (from the base pair) in the C₂ evolution and in the T₁ derivation. But the U₁ estimate itself is coupled to C₂. Is the coupled Grönwall argument (4.1)–(4.3) free of circularity?

5. **Derivative-reordering lemma (§7):** The note claims C_{m+2} is paired only with U₀. Verify from the Leibniz expansion ∇^m(B₂*U) = Σ C(m,k) B_{k+2}*U_{m-k}. For k=m: B_{m+2}*U₀. For k=m-1: B_{m+1}*U₁. Could any term B_{m+2}*U_j with j≥1 arise from a different source (e.g., differentiating the principal operator div(a∇U) m times)?

Be specific: identify any mathematical error, any missing term, or any unjustified step. If the proof is correct, confirm it explicitly.

## Output

## Verification memo: Step 60 base-pair continuation

The base-pair argument in `step60_base_pair_proof.md` is structurally sound at the schematic tensor level, assuming the imported zero-order inputs and the Step 58 normal form for the weighted curvature equation. The central mechanisms are valid:

\[
(U_0\in L^\infty,\;T_0\in L^q_{\rm fin})
\longrightarrow (U_1,C_2)\in L^p
\longrightarrow T_1\in L^p
\longrightarrow T_0\in L^\infty
\]

can be closed by a coupled Grönwall argument, and the apparent \(m=1\) circular Hessian terms can be treated by the signed-Hessian integration lemma if the tensor contractions are kept signed before absolute values are taken.

There are, however, several places where the written estimates are too compressed or slightly inaccurate. These do not appear to destroy the mechanism, but they must be corrected for a standalone proof.

---

## 1. The \(C_2\) evolution: \(\partial_tC_2=g^{-1}*U_1*C_1\)

### 1.1 Verification

Let

\[
C_1=\nabla\chi=d\chi,\qquad C_2=\nabla^2\chi.
\]

Since \(\chi\) is a fixed spatial scalar, \(C_1=d\chi\) is connection-independent as a one-form. In components,

\[
(C_2)_{ij}=\nabla_i\nabla_j\chi
=\partial_i\partial_j\chi-\Gamma^k_{ij}\partial_k\chi.
\]

Therefore

\[
\partial_t(C_2)_{ij}=-(\partial_t\Gamma^k_{ij})\nabla_k\chi.
\]

No derivative of \(\partial_t\Gamma\) appears at this level, because only one connection coefficient occurs in \(\nabla^2\chi\). Thus there is no \(U_2\) term in \(\partial_tC_2\).

The connection variation under

\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g,\qquad a=\chi^2,
\]

is schematically

\[
\partial_t\Gamma=g^{-1}*\nabla(aE),
\]

up to the usual symmetrization and sign. By the algebraic identity used throughout the notes,

\[
U=aT,\qquad \operatorname{Ric}(U)=aE,
\]

and since \(\nabla g=0\),

\[
\nabla(aE)=\nabla\operatorname{Ric}(U)=g^{-1}*\nabla U=g^{-1}*U_1.
\]

Hence

\[
\boxed{\partial_tC_2=g^{-1}*U_1*C_1.}
\]

This part of Step 60 is correct.

### 1.2 Expansion of \(U_1\)

If one expands \(U_1=\nabla(aT)\), then

\[
U_1=B_1*T_0+aT_1,\qquad B_1=\nabla a=2\chi C_1.
\]

Thus \(\partial_tC_2\) does contain a \(B_1*T_0*C_1\) piece, but that piece is already inside \(U_1\). There is no additional standalone \(U_0\) term and no \(U_2\) term.

### 1.3 Metric variation in the \(L^p\) norm

The energy estimate for \(\|C_2\|_p^p\) also contains terms from the time variation of the metric, the pointwise tensor norm, and the volume form. Since

\[
\partial_tg=-2aE=-2\operatorname{Ric}(U),
\]

and \(U_0\in L^\infty\) is imported, these extra terms are bounded by

\[
C\|C_2\|_p^p.
\]

They are lower-order and belong in the coupled inequality. Step 60 does not display them explicitly, but they do not alter the structure.

---

## 2. The \(B_3*U_0\) term and the signed-Hessian resolution

This is the most delicate part of the note. The conclusion is essentially correct, but the written estimate in §2.5 and the table in §2.8 need refinement.

Let

\[
V=U_1,\qquad \Phi=|V|^{p-2}V,
\]

with the usual regularization if \(p\) is not an even integer.

The problematic contribution from differentiating \(B_2*U\) is

\[
B_3*U_0,\qquad B_3=\nabla^3a.
\]

Since \(a=\chi^2\),

\[
B_3=2\chi C_3+6C_1*C_2.
\]

The top part is

\[
2\chi C_3*U_0.
\]

Tested against \(\Phi\), this gives schematically

\[
2\int \chi\,\Phi*C_3*U_0.
\]

Using \(C_3=\nabla C_2\) and integrating one derivative,

\[
2\int \chi\,\Phi*C_3*U_0
=
-2\int \chi\,\nabla\Phi*C_2*U_0
-2\int \Phi*C_1*C_2*U_0
-2\int \chi\,\Phi*C_2*\nabla U_0.
\]

Since \(\nabla U_0=U_1=V\), the last term is

\[
-2\int \chi\,\Phi*C_2*V.
\]

This is the term that Step 60 identifies as signed-Hessian.

### 2.1 The last term is of signed-Hessian form

Because \(C_2=\nabla^2\chi\) is symmetric, any universal contraction of \(C_2\) with \(\Phi\otimes V\) can be written as

\[
\int \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
\]

where \(B^{ij}(V)\) is the coefficient of \(\nabla_i\nabla_j\chi\) in the contraction. Since the original contraction is quadratic in \(V\) after including \(\Phi=|V|^{p-2}V\),

\[
|B(V)|\le C|V|^p.
\]

Also,

\[
|\nabla B(V)|
\le C_p |V|^{p-1}|\nabla V|,
\]

after the standard regularization of \(|V|^{p-2}V\) near \(V=0\). Therefore the Step 38 signed-Hessian lemma applies:

\[
\left|\int \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\right|
\le
\varepsilon D^U_{1,p}
+
C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p,
\]

where

\[
D^U_{1,p}=\int a|\nabla V|^2|V|^{p-2}.
\]

Thus the genuinely dangerous part of the \(B_3*U_0\) term is controlled without any \(L^\infty\) bound on \(C_2\).

### 2.2 The first two IBP remainders need a little more care

Step 60 says that the first term is “absorbed by diffusion” and that the second is bounded by Young using bounded \(C_1,U_0\). Read literally, that is too compressed.

The first remainder is

\[
-2\int \chi\,\nabla\Phi*C_2*U_0.
\]

Using \(U_0\in L^\infty\),

\[
\left|\int \chi\,\nabla\Phi*C_2*U_0\right|
\lesssim
\int \chi |C_2|\,|V|^{p-2}|\nabla V|.
\]

Weighted Young gives

\[
\int \chi |C_2|\,|V|^{p-2}|\nabla V|
\le
\varepsilon D^U_{1,p}
+
C_\varepsilon\int |C_2|^2|V|^{p-2}.
\]

For \(p>2\),

\[
\int |C_2|^2|V|^{p-2}
\le
\|C_2\|_p^2\|V\|_p^{p-2}
\le
\varepsilon\|C_2\|_p^p+C_\varepsilon\|V\|_p^p.
\]

So this term is controlled, but it contributes a \(\|C_2\|_p^p\) term. It is not absorbed by diffusion alone.

The second remainder is

\[
-2\int \Phi*C_1*C_2*U_0.
\]

Using \(C_1,U_0\in L^\infty\),

\[
\left|\int \Phi*C_1*C_2*U_0\right|
\lesssim
\int |C_2|\,|V|^{p-1}.
\]

Hölder and Young give

\[
\int |C_2|\,|V|^{p-1}
\le
\|C_2\|_p\|V\|_p^{p-1}
\le
\varepsilon\|C_2\|_p^p+C_\varepsilon\|V\|_p^p.
\]

Again, this is controlled, but it should be recorded as a coupled \(C_2\)-norm contribution, not as something bounded using only \(\|C_1\|_\infty\) and \(\|U_0\|_\infty\).

### 2.3 Correction to the table in §2.8

The table entry for

\[
C_1*C_2*U_0
\]

should therefore be amended. The term is not bounded solely by \(\|C_1\|_\infty\) and \(\|U_0\|_\infty\), because \(C_2\) is an evolving unknown. It is controlled either by the coupled \(L^p\) norm of \(C_2\), or in some index configurations by an additional signed integration using the special structure \(C_1*C_2\). The coupled estimate already has room for this contribution.

This is a presentational gap, not a structural break.

---

## 3. The \(B_2*V\) terms

The \(B_2*V\) terms from the differentiated principal operator and drift are of the form

\[
\int \Phi*(B_2*V).
\]

Since

\[
B_2=2\chi C_2+2C_1*C_1,
\]

we get two types:

\[
2\int \chi\,\Phi*C_2*V
\]

and

\[
2\int \Phi*C_1*C_1*V.
\]

The second is bounded by

\[
C\|C_1\|_\infty^2\|V\|_p^p.
\]

The first is again of signed-Hessian form:

\[
2\int \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
\]

with \(B^{ij}(V)\) a contraction of \(|V|^{p-2}V\otimes V\). The same bounds hold:

\[
|B(V)|\le C|V|^p,
\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]

Therefore the signed-Hessian lemma gives

\[
\left|2\int \chi\,\Phi*C_2*V\right|
\le
\varepsilon D^U_{1,p}
+
C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\]

So Step 60’s treatment of the \(B_2*V\) terms is correct.

---

## 4. Non-circularity of the coupled base-pair estimate

The coupled system written in Step 60 is

\[
\begin{aligned}
\frac{d}{dt}\|U_1\|_p^p+cD^U_{1,p}
&\le C_{p,\tau}(1+\|U_1\|_p^p)+C_{p,\tau}\|C_2\|_p^p,\\
\frac{d}{dt}\|C_2\|_p^p
&\le C(\|U_1\|_p^p+\|C_2\|_p^p).
\end{aligned}
\]

Adding gives

\[
\frac{d}{dt}
\left(\|U_1\|_p^p+\|C_2\|_p^p\right)
+cD^U_{1,p}
\le
C_{p,\tau}
\left(1+\|U_1\|_p^p+\|C_2\|_p^p\right).
\]

This is a standard coupled differential inequality. It does not assume prior \(L^p\) bounds for \(U_1\) or \(C_2\). The initial values at \(t=\tau\) are finite because the solution is smooth there. Grönwall then gives finite bounds on \([\tau,T_*)\), with constants depending on the imported data at \(\tau\), the cutoff geometry, and the metric-comparison/Sobolev inputs.

Thus the base-pair estimate is not circular.

One should include the lower-order terms coming from time variation of the metric, norms, and volume form. As noted above, these are controlled by \(U_0\in L^\infty\) and metric equivalence, and they only add terms of the form

\[
C_{p,\tau}(\|U_1\|_p^p+\|C_2\|_p^p).
\]

They preserve the coupled Grönwall structure.

---

## 5. The derivative-reordering lemma and the placement of \(C_{m+2}\)

Step 60 states that in the level-\(m\) differentiated \(U\)-equation, the highest cutoff jet \(C_{m+2}\) appears only paired with \(U_0\). This is correct by derivative counting, assuming the Step 58 normal form.

The source that produces \(C_{m+2}\) is

\[
\nabla^m(B_2*U).
\]

Leibniz gives

\[
\nabla^m(B_2*U)
=
\sum_{k=0}^m \binom{m}{k} B_{k+2}*U_{m-k}.
\]

The largest cutoff derivative occurs at \(k=m\):

\[
B_{m+2}*U_0.
\]

The next one is \(k=m-1\):

\[
B_{m+1}*U_1.
\]

Thus inside this source, \(C_{m+2}\) appears only with \(U_0\).

The principal operator and drift terms do not produce \(C_{m+2}\) paired with \(U_j\), \(j\ge1\). Indeed, differentiating

\[
\operatorname{div}(a\nabla U)
\]

\(m\) times produces at most \(B_{m+1}*U_1\) and lower terms, because the operator contains one derivative on \(U\) and one derivative falling through the divergence. Differentiating

\[
B_1*\nabla U
\]

produces at most \(B_{m+1}*U_1\). The algebraic reaction terms contain no high cutoff derivatives. The time commutator uses

\[
\partial_t\Gamma=g^{-1}*U_1,
\]

so

\[
[\partial_t,\nabla^m]U
\]

involves derivatives of \(U_1\) up to order \(m-1\), hence at most \(U_m\), and no \(C_{m+2}\). Curvature commutators lower the derivative count and produce only lower curvature/cutoff factors.

Therefore the structural statement is correct:

\[
C_{m+2}\text{ appears only with }U_0,
\]

and \(C_{m+1}\) appears with \(U_1\) or \(U_0\), as in the Step 59 ledger.

However, the proof sketch still needs an exact index-level treatment of covariant non-commutation and symmetrization. The derivative count gives the right structural extraction, but a formal proof must write the universal contractions and verify that every commutator produced by reordering derivatives indeed belongs to lower levels.

---

## 6. Additional points needing correction or completion

### 6.1 The opening statement about \(C_3\)

The opening paragraph of Step 60 says that every coefficient-derivative term at \(m=1\) has total cutoff derivative \(\le2\), so no \(C_3\) arises. This does not match §2.3, where

\[
\nabla(B_2*U)=B_3*U_0+B_2*V
\]

explicitly produces \(B_3\), hence \(\chi C_3*U_0\). The proof actually uses an integration by parts of this \(C_3\) term. The corrected statement is:

> At \(m=1\), a \(C_3\) term does arise from \(B_3*U_0\), but after one signed integration by parts it reduces to signed \(C_2\)-Hessian terms plus remainders controlled by the coupled \((U_1,C_2)\) estimate.

This is a textual inconsistency, not a fatal mathematical obstruction.

### 6.2 Time commutator in the \(m=1\) equation

When deriving the equation for \(V=U_1\), one must include

\[
[\partial_t,\nabla]U=(\partial_t\Gamma)*U.
\]

Using \(\partial_t\Gamma=g^{-1}*U_1\), this gives a term of the form

\[
g^{-1}*U_1*U_0,
\]

which is a bounded-coefficient multiple of \(U_1\). Step 60 does not display this time commutator separately in §2, but it is harmless and fits the existing bounded-coefficient terms.

### 6.3 \(B_2\) is not fixed under the evolving connection

In §5.2, Step 60 says that \(B_2\) is a fixed spatial function and hence \(\|B_2\|_{2p}\) is a per-datum constant. This is too loose. The cutoff function \(\chi\) is fixed, but \(B_2=\nabla^2(\chi^2)\) depends on the evolving connection. Its \(C_2\)-part evolves. The correct statement is that the base-pair estimate has already supplied \(L^r\) bounds for \(C_2\) for every finite \(r\), so \(\|B_2\|_{2p}\) is controlled by the base-pair output, not by fixedness.

This correction does not introduce circularity, because the \(T_1\) estimate is run after the \((U_1,C_2)\) base pair.

### 6.4 Exact tensor-index formulas remain necessary

The schematic \(*\)-notation hides several important details:

1. the precise index placements in the signed-Hessian contractions;
2. symmetrization of \(B^{ij}(V)\), since \(\nabla_i\nabla_j\chi\) is symmetric;
3. the regularization of \(|V|^{p-2}V\) when \(V=0\);
4. the exact curvature commutators produced by reordering covariant derivatives;
5. the time variation of tensor norms and volume forms.

These are not conceptual obstructions, but they are required for a rigorous standalone proof and eventually for Lean formalization.

### 6.5 Dimensional coverage

The Sobolev embedding step

\[
W^{1,p}\hookrightarrow L^\infty
\]

is used in dimension four with \(p>4\). Thus this base-pair continuation belongs to the four-dimensional restricted analytic bridge. It does not by itself treat all dimensions \(n\ge2\), dimension-only constants, or the full Yau Problem 26 proposition.

---

## Final assessment

The requested critical points check out as follows:

1. **\(C_2\) evolution:** Correct.  
   \[
   \partial_tC_2=g^{-1}*U_1*C_1
   \]
   with no \(U_2\) term. The identity \(\nabla(aE)=g^{-1}*U_1\) is valid because \(aE=\operatorname{Ric}(U)\) and \(\nabla g=0\). If expanded, \(U_1\) contains \(B_1*T_0+aT_1\).

2. **\(B_3*U_0\) signed-Hessian resolution:** Structurally correct.  
   The top \(\chi C_3*U_0\) term integrates by parts to a signed term
   \[
   \int \chi\,\nabla_i\nabla_j\chi\,B^{ij}(U_1),
   \]
   with the required bounds. However, the IBP remainders involving \(C_2\) must be estimated through the coupled \(C_2\)-norm, not merely by \(\|C_1\|_\infty\) and \(\|U_0\|_\infty\).

3. **\(B_2*V\) terms:** Correct.  
   They are signed-Hessian terms of the same form and are controlled by the Step 38 lemma.

4. **Non-circularity:** Correct.  
   The coupled \((U_1,C_2)\) Grönwall system is not circular. It uses only imported zero-order inputs and finite smooth initial data at \(t=\tau\).

5. **Derivative-reordering lemma:** Structurally correct by derivative counting.  
   \(C_{m+2}\) appears only with \(U_0\). A full index-level proof of the commutator and reordering statement is still needed.

With these corrections and completions, the base-pair continuation proof is mathematically coherent and supports the stated base layer:

\[
(U_0\in L^\infty,\;T_0\in L^q_{\rm fin})
\to (U_1,C_2)\in L^p_{\rm fin}
\to T_1\in L^p_{\rm fin}
\to T_0\in L^\infty.
\]