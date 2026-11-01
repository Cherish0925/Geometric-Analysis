# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step37_global_Q_persistence.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/workspace/scripts/verify_step37_interface_algebra.py",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/scripts/step36_platform_Q_verify.py",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Review A03 Step 37's three analytic-interface notes as possible proofs for the restricted four-dimensional negative cutoff-flow route, using A01's Step 36 platform note and verifier as comparison. Focus especially on the shifted-U base-pair continuation note. Check: (1) transported-DeTurck existence: does the note correctly adapt Yang's Theorem 8.2 to the normalized term, and is any claimed chi^2 weight for delta(hat a) too strong or harmless? (2) global Q persistence: are the weights, buffered K2 use, Gronwall coefficient, and independence from J6 correct? (3) base-pair continuation: does the written proof actually implement the second integration by parts for I_{1c}/I_3 that the script/message claim, or does it still rely on an invalid direct Holder bound such as ∫ chi |Theta| |W|^p <= ||Theta||_p ||W||_p^p? Are unweighted L^p(T), Sobolev upgrades, and G terms sufficiently justified, or still hidden hypotheses? Give a direct mathematical memo identifying what can be accepted now and what exact calculation remains.

## Output

# Scientific verification memo

## Overall mathematical reading

The three notes have different levels of support:

1. **Transported-coefficient DeTurck existence:** the normalized adaptation is mathematically sound as a citation-based extension of Yang’s Theorem 8.2. The asserted \(\chi^2\)-factor in \(\delta\widehat a\) is false, but the actual term is still zeroth order in the map variation and fits Yang’s \(E\psi\) term. Thus it does not alter the existence mechanism.
2. **Global \(Q\)-persistence:** the main energy mechanism and its independence from \(J_6\) are correct. The displayed derivation omits gradient-\(a\) terms, uses the buffered curvature energy imprecisely, and does not explicitly justify the shorter \(Cr^{-2}\) growth rate. A01’s \(C(1+r^{-2})\) formulation follows directly from the written estimates.
3. **Shifted-\(U\) base pair:** the revised §§3.1 and 3.3 do use the needed second signed integration by parts; they no longer depend on the incorrect direct Hölder estimate. The resulting finite-\(L^p\) base estimate is credible conditional on the stated \(L^p(T)\) input and on the schematic \(W\)-equation. It is not yet a continuation theorem because the exact normalized \(U\)-equation, the unweighted \(T\)-energy, and the higher staggered derivative induction are absent.

---

## 1. Normalized transported-DeTurck existence

### 1.1 Pullback mechanism

A03’s system
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
 +2\widehat\delta^*(\widehat a\,\omega),
\qquad
\widehat a=a\circ\varphi_t^{-1},
\]
with \(\omega=S^{-1}\delta G(S)\), is the direct normalized analogue of Yang’s equations (8.5)–(8.6). Since
\[
2\widehat\delta^*(\widehat a\omega)
=\mathcal L_{(\widehat a\omega)^\sharp}\widehat g,
\]
and the Eulerian velocity of \(\varphi_t\) is the opposite vector field, the Lie derivative cancels under pullback. Moreover,
\[
\varphi_t^*\widehat a=a,\qquad
\varphi_t^*\operatorname{Ric}_{\widehat g}
=\operatorname{Ric}_{\varphi_t^*\widehat g}.
\]
Therefore \(g=\varphi_t^*\widehat g\) satisfies
\[
\partial_tg=-2a(\operatorname{Ric}_g+g).
\]
This is the correct geometric equation. The earlier fixed term \(a\mathcal L_Wg\) would indeed miss
\[
da\otimes W^\flat+W^\flat\otimes da.
\]

### 1.2 Variation of the transported coefficient

The sentence
\[
\delta\widehat a
=\chi^2(\text{first-order operator in }\psi)
\]
is too strong. If \(Y=\delta\varphi\circ\varphi^{-1}\), then
\[
\boxed{\delta\widehat a=-d\widehat a(Y)
=-2\widehat\chi\,d\widehat\chi(Y).}
\]
There is generally only one factor of \(\widehat\chi\). For example, locally taking
\(\chi=x^2\) gives \(a=x^4\) and
\[
da=4x^3\,dx,
\]
which cannot be written as \(a\) times a bounded smooth coefficient near \(x=0\).

This does not damage the linearized argument. The new normalized term is
\[
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h+2\,d\widehat a(Y)\,\widehat g.
\]
It contains no derivatives of \(h\) and no spatial derivatives of \(Y\). At Sobolev level \(m\), it has the standard estimate
\[
\left\|
-2\widehat a\,h+2d\widehat a(Y)\widehat g
\right\|_{H^m}
\le C_m\bigl(\|h\|_{H^m}+\|Y\|_{H^m}\bigr),
\]
with constants depending on the fixed smooth datum and the background solution. It belongs in Yang’s \(Dh+E\psi\) sector, not in the principal part.

Thus the false \(\chi^2\)-weight is harmless after correction. No weighted absorption is needed for this term.

### 1.3 Degree of completeness

Yang’s source itself states that smooth tame estimates follow from energy integrals and interpolation. A03 invokes stability of those estimates under the displayed zeroth-order perturbation rather than reproducing them. That is a standard and mathematically appropriate use of Yang’s theorem. A fully expanded treatment would add the preceding \(H^m\) estimate at every derivative level.

The Approach 2 remark is less precise. Under the spatially varying conformal term
\[
-2(\varepsilon^2+a)g,
\]
the curvature variation contains not only an algebraic reaction but also terms involving
\(\nabla^2a\owedge g\). These coefficients are smooth and independent of \(\varepsilon\), so they are still lower-order per-datum terms, but they are not merely
\((\varepsilon^2+a)|\operatorname{Rm}|\). Since A03 relies on Approach 1, this imprecision does not affect its stated theorem.

**Usable result:** per-datum smooth short-time existence for the normalized fixed-cutoff flow is supported by Yang’s transported system, after replacing the sentence about a \(\chi^2\)-factor by the exact formula above.

---

## 2. Global unweighted defect energy

Let
\[
Q=\int_M|E|^2\,d\mu,\qquad
X=\int_Ma|\nabla E|^2\,d\mu.
\]

### 2.1 Correct evolution structure

The homogeneity in \(E\) is correct: if \(E=0\), the velocity vanishes and the defect stays zero. However, A03 equation (2.1) is incomplete as a literal schematic identity. The variation of \(aE\) also produces gradient-\(a\) terms. The appropriate structure is
\[
(\partial_t-a\Delta)|E|^2
=
-2a|\nabla E|^2
+\nabla a*E*\nabla E
+\nabla^2a*E*E
+a\,\operatorname{Rm}*E*E
+a\,E*E*E
+a\,E*E.
\]
Every term still contains \(E\) or \(\nabla E\).

The omitted gradient term satisfies
\[
\int |\nabla a||E||\nabla E|
\le
\varepsilon X
+C_\varepsilon\int\frac{|\nabla a|^2}{a}|E|^2.
\]
For \(a=\chi^2\),
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
\quad\text{on }\{\chi\ne0\},
\]
with zero extension at zeros. The Hessian term gives the same estimate after signed integration by parts, using
\[
|B_0(E)|\le C|E|^2,\qquad
|\nabla B_0(E)|\le C|E||\nabla E|.
\]
Thus both cutoff-derivative sectors contribute
\[
\varepsilon X+Cr^{-2}Q.
\]

### 2.2 Buffered curvature energy

The line
\[
\|F\|_{L^2(U_j)}
\le K_{2,j}^{1/2},
\qquad
K_{2,j}=\int_{U_j}\eta_j^2F^2,
\]
does not follow unless \(\eta_j\equiv1\) throughout \(U_j\). The correct buffered calculation, already present in A01, is
\[
\begin{aligned}
\int F(\chi_jE)^2
&=\int_{\operatorname{supp}\chi_j}F(\chi_jE)^2\\
&\le
\left(\int_{U_j}\eta_j^2F^2\right)^{1/2}
\|\chi_jE\|_4^2,
\end{aligned}
\]
where
\[
\eta_j\equiv1\quad\text{on }\operatorname{supp}\chi_j.
\]
The local Sobolev inequality then gives
\[
\|\chi_jE\|_4^2
\le C\mathcal S_j
\left(
\int_{U_j}a|\nabla E|^2
+r^{-2}\int_{U_j}|E|^2
\right).
\]
Hence
\[
\int F(\chi_jE)^2
\le C\gamma_j
\left(
X_j+r^{-2}Q_j
\right),
\qquad
\gamma_j=\mathcal S_jK_{2,j}^{1/2}.
\]
Disjoint supports allow direct summation.

### 2.3 Growth coefficient

From A03’s displayed estimate of the measure term,
\[
\int a|E|^3\le C(Q+I_1),
\]
the immediate inequality is
\[
Q'\le C(1+r^{-2})Q,
\]
after absorbing the \(X\)-term. This yields
\[
\boxed{
Q(t)\le
e^{C(1+r^{-2})t}Q(0)
\le e^{C\theta(1+r^2)}Q(0)
\quad (t\le\theta r^2).
}
\]
This is exactly A01’s formulation.

The shorter rate \(Cr^{-2}\) is also obtainable, but it requires an explicit sharpening: since
\[
|E|\le C(1+|\operatorname{Rm}|)\le CF,
\]
all active algebraic terms, including the volume-form cubic term, can be grouped into
\[
C\int aF|E|^2.
\]
That entire quantity is then treated by the buffered \(F\)-potential estimate and contributes \(C\gamma_*r^{-2}Q\). Alternatively, assuming \(r\le1\) converts \(1+r^{-2}\) to \(Cr^{-2}\). A03 does not explicitly make either step before writing (3.8)–(3.10).

For the intended fixed-radius application, both forms preserve
\[
Q(t)=O(Q(0)).
\]

### 2.4 Independence from \(J_6\)

This part is correct. Neither
\[
J_6=\int\eta^2a^4|E|^6
\]
nor \(\|aE\|_\infty\) controls the unweighted integral near small \(a\). The global calibration uses \(Q\) directly, so it requires its own evolution estimate. The dependency separation in A03 and A01 is mathematically appropriate.

**Usable result:** the \(Q\)-propagation argument is sound after inserting the gradient-\(a\) sector, restricting the \(F\)-integral to \(\operatorname{supp}\chi_j\) and using \(\eta_j\equiv1\) there, and either retaining \(C(1+r^{-2})\) or explicitly performing the sharper \(F\)-grouping.

---

## 3. Shifted-\(U\) base-pair estimate

Set
\[
U=aT,\qquad W=\nabla U,\qquad \Theta=\nabla^2\chi.
\]

### 3.1 The second integration by parts is now the right one

The revised text no longer uses
\[
\int\chi|\Theta||W|^p
\le \|\Theta\|_p\|W\|_p^p,
\]
which would require \(W\in L^{p^2/(p-1)}\), not merely \(L^p\).

For both \(I_{1c}\) and \(I_3\), the actual signed term has the form
\[
J=\int_M\chi\,\chi_{;ij}\,B^{ij}(W)\,d\mu,
\]
where
\[
|B(W)|\le C_p|W|^p,\qquad
|\nabla B(W)|\le C_p|W|^{p-1}|\nabla W|.
\]
On closed \(M\), the exact calculation is
\[
\boxed{
J
=
-\int\chi_{;i}\chi_{;j}B^{ij}(W)
-\int\chi\,\chi_{;j}\nabla_iB^{ij}(W).
}
\]
Therefore
\[
\begin{aligned}
|J|
&\le
C_p\|d\chi\|_\infty^2\int|W|^p
+C_p\int\chi|d\chi||W|^{p-1}|\nabla W|\\
&\le
\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p.
\end{aligned}
\]
This is precisely the estimate asserted in (3.9) and (3.11). It applies because:

- in \(I_{1c}\), the derivative landing on \(U\) produces \(W\), so the test tensor and this new \(W\) give a degree-\(p\) tensor \(B(W)\);
- in \(I_3\), the source already contains \(\chi\Theta*W\), producing the same degree-\(p\) structure.

Thus the base energy no longer contains the earlier Hölder error. The script comment saying “total power \(p+1\)” is textually wrong; the degree is \(p\), as the note itself now states.

### 3.2 Remaining base estimates

The other principal estimates are consistent:

- \(I_{1a}\) uses \(\chi=\sqrt a\) and gives
  \[
  \varepsilon\int a|\nabla W|^2|W|^{p-2}
  +C K^2\|\Theta\|_p^2\|W\|_p^{p-2}.
  \]
- \(I_{1b}\) and \(I_2\) use the valid Hölder pairing
  \[
  \int|\Theta||W|^{p-1}
  \le\|\Theta\|_p\|W\|_p^{p-1}.
  \]
- \(I_4\) has the matching \(\chi\)-factor and is absorbed into the weighted diffusion.
- Since
  \[
  \partial_t\nabla^2\chi
  =g^{-1}*\nabla\operatorname{Ric}(U)*d\chi,
  \]
  together with norm variation, one obtains
  \[
  \partial_t|\Theta|
  \le CK|\Theta|+C|W||d\chi|.
  \]

Conditional on the schematic \(W\)-equation and the unweighted \(T\)-input, the coupled estimate
\[
Y_1' \le C\bigl(1+Y_1+\|T\|_p^p\bigr),
\qquad
Y_1=\|W\|_p^p+\|\Theta\|_p^p,
\]
is valid.

### 3.3 Inputs that remain external to this note

Two substantial ingredients are not derived in the file.

#### Unweighted \(L^p(T)\)

Section 1 describes this as controlled by \(|U|\), while §7 correctly restates it as an independently available input. Wang’s Lemma 4.10 proves the analogous estimate for unnormalized local Ricci flow under a weighted curvature bound. For the present shifted normalized equation, the corresponding tensor estimate would have the form
\[
\frac{d}{dt}\int|T|^p
\le C_{p,K,\chi}\left(1+\int|T|^p\right),
\]
after signed treatment of the Hessian-cutoff term. That normalized shifted derivation is not contained in A03 Step 37.

#### Exact \(W\)-equation and the \(G\)-sector

The proof assumes
\[
\begin{aligned}
(\partial_t-a\Delta)W
={}&
\chi\nabla^3\chi*U
+d\chi*\Theta*U
+\chi\Theta*W
+\chi d\chi*\nabla W\\
&+U*W+G*W+\mathcal R,
\end{aligned}
\]
with
\[
|\mathcal R|\le C_K(1+|T|+|W|).
\]
This form is plausible: \(G\) is spatially parallel, \(|G|\) is dimensional, and \(\partial_tG\) is algebraic in \(\operatorname{Ric}(U)\). Also,
\[
a\nabla T=W-da*T
\]
places unweighted \(T\) only in an additive \(L^p\) term when multiplied by bounded \(U\) and \(d\chi\). Nevertheless, the file does not derive the normalized \(U\)-equation at tensor level, so the assertion that no unweighted \(T*W\) coefficient or unweighted \(\nabla T\) term survives remains unsupported within this note.

### 3.4 No pointwise continuation follows from the base pair

The revised §6 is correct: bounds for
\[
\|\nabla U\|_{L^p},\qquad \|\nabla^2\chi\|_{L^p}
\]
do not imply their \(L^\infty\) norms. Sobolev embedding requires one additional unweighted spatial derivative. The higher staggered system involving
\[
\nabla^mU,\qquad \nabla^{m+1}\chi,\qquad \nabla^{m-1}T
\]
has not been established.

The script’s hard-coded statements B8 and C4 therefore verify neither the higher induction nor smooth terminal extension. Most of the script’s PDE entries are literal `True`; it verifies exponent arithmetic and the identity \(\sqrt a=\chi\), not the tensor evolution.

---

## Final mathematical assessment

- **Short-time existence:** supported, with the exact correction
  \(\delta\widehat a=-d\widehat a(Y)\); the extra normalized term remains a smooth zeroth-order perturbation.
- **Global \(Q\):** supported after adding the omitted \(\nabla a*E*\nabla E\) terms and using the buffered energy only on \(\operatorname{supp}\chi_j\). The directly justified growth rate is \(C(1+r^{-2})\); \(Cr^{-2}\) needs explicit regrouping into the \(F\)-potential or \(r\le1\).
- **Base pair:** the second signed integration by parts is mathematically correct and removes the direct Hölder error. The finite-\(L^p\) lemma is conditional on an independently established \(L^p(T)\) estimate and an index-level normalized \(W\)-equation.
- **Continuation:** the remaining mathematical substance is the normalized shifted \(T\)-energy, the exact \(U/W\) evolution including all \(G\)-terms, and the full higher derivative induction leading to pointwise derivative bounds and a smooth terminal metric.