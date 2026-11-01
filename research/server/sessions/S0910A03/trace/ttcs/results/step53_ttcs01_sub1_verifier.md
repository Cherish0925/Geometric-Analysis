# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step53_coupled_transported_coefficient_start.md",
    "Sessions/S0910A03/workspace/notes/step52_normalized_local_flow_start_repair.md",
    "Sessions/S0910A03/workspace/data/step53_coupled_grading_checks.json"
  ]
}
```

## Task

Verify the coupled transported-coefficient start theorem for the normalized cutoff flow ∂_t g = -2χ²(Ric+g). The central mathematical claim is that the coupled DeTurck system (metric equation + scalar transport for χ̂=χ∘φ⁻¹) has short-time existence through a staggered parabolic-ODE grading. Specifically verify:

1. PULLBACK IDENTITY: Does the coupled system (1.4) in the note actually pull back to give ∂_t g = -2χ²(Ric+g) with FIXED χ in geometric coordinates? Check the computation: g=φ*ĝ, â∘φ=a because χ̂=χ∘φ⁻¹.

2. PRINCIPAL STRUCTURE: The coupling matrix shows metric eq at order k needs ψ at order k (coefficient only), transport at order k needs V at order k+1 (through DeTurck vector W~∂V). Is this 'lower-triangular' description correct?

3. PARABOLIC GAIN: The note claims V∈C_t(H^s)∩L²_t(H^{s+1}) from the parabolic equation, and this extra L²_t derivative compensates the ODE for φ needing ∫||âW||_{H^s}dt, where ||W||_{H^s}≤C||V||_{H^{s+1}}. Verify this chain.

4. TRANSPORT IBP: The transport energy estimate claims ∫∂^α ψ·ψ²W·∂_k∂^α ψ = -½∫(∂^α ψ)²·∂_k(ψ²W), so the top-order ψ term is absorbed without needing ψ at order k+1. Is this correct for the SPECIFIC equation ∂_t ψ = ψ²W^k∂_kψ (note the coefficient is ψ² not just a constant)?

5. CONTRACTION: The I2 factorization â₁-â₂=(χ̂₁+χ̂₂)(χ̂₁-χ̂₂) is used to bound the coefficient difference in the contraction. Does this genuinely make the cross-terms proportional to ||χ̂₁-χ̂₂|| with bounded multipliers?

6. CRITICAL GAP: Is there any hidden derivative loss in the coupled fixed-point that the note misses? In particular, does the composition ψ=χ∘φ⁻¹ really give ψ∈H^s when φ∈H^s, for the specific Sobolev orders needed?

The flat-torus test (Step 52) permanently falsified Step 51's homogeneous energy closure. This note does NOT use energy estimates for existence; it uses Xu's fixed-point method. Confirm that these are genuinely different approaches.

## Output

# Scientific verification memo

## Overall assessment

Three components are mathematically correct:

1. the pullback produces the fixed-cutoff geometric flow;
2. the transport integration-by-parts identity removes the apparent \(H^{k+1}\) requirement on \(\widehat\chi\);
3. the square-difference factorization gives a Sobolev-Lipschitz dependence on \(\widehat\chi_1-\widehat\chi_2\).

The short-time theorem is nevertheless not established by §§2–4 as written. Two concrete derivative issues remain:

- the exact metric equation contains \(d(\widehat\chi^2)*W\), omitted from (2.1) and (4.1);
- estimate (4.4) uses the false inequality
  \[
  \|U_1-U_2\|_{H^{\widetilde p+1}}
  \le C\|U_1-U_2\|_{H^{\widetilde p}}.
  \]

There is also an \(\varepsilon\)-uniformity issue: degenerate parabolic energy supplies a weighted extra derivative, not the unweighted \(L^2_tH^{s+1}\) gain asserted in (2.3). These defects may admit a repair through a weighted parabolic–transport norm, but that estimate is absent from the note.

---

## 1. Pullback identity

This part is exact.

Let
\[
Y_t=(\partial_t\varphi_t)\circ\varphi_t^{-1}
   =-\widehat aW.
\]
For \(g=\varphi_t^*\widehat g\),
\[
\frac d{dt}\varphi_t^*\widehat g
 =\varphi_t^*\!\left(\partial_t\widehat g+\mathcal L_Y\widehat g\right).
\]
Substitution of (1.4) gives cancellation of the two Lie derivatives:
\[
\partial_tg
 =\varphi_t^*\!\left[-2\widehat a
   (\operatorname{Ric}_{\widehat g}+\widehat g)\right].
\]
Naturality then yields
\[
\partial_tg
 =-2(\widehat a\circ\varphi_t)
   (\operatorname{Ric}_g+g).
\]

The transport equation also gives the required coefficient identity directly:
\[
\begin{aligned}
\frac d{dt}(\widehat\chi\circ\varphi_t)
 &=\left(\partial_t\widehat\chi
       -\widehat aW(\widehat\chi)\right)\circ\varphi_t\\
 &=0.
\end{aligned}
\]
Hence
\[
\widehat\chi\circ\varphi_t=\chi,\qquad
\widehat a\circ\varphi_t
 =(\widehat\chi\circ\varphi_t)^2=\chi^2.
\]
Therefore
\[
\boxed{\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).}
\]

This repairs the fixed-coefficient pullback error identified in Step 52.

---

## 2. Exact principal and lower-order structure

The second-order metric principal symbol is indeed
\[
\widehat a\,\widehat g^{-1}*\widetilde\nabla^2\widehat g.
\]
Thus \(\widehat\chi\) enters the second-order coefficient without derivatives.

However, the full equation contains first derivatives of \(\widehat\chi\). The identity
\[
\mathcal L_{\widehat aW}\widehat g
 =\widehat a\,\mathcal L_W\widehat g
   +d\widehat a\otimes W^\flat
   +W^\flat\otimes d\widehat a
\]
gives
\[
-2\widehat a\,\operatorname{Ric}_{\widehat g}
 +\mathcal L_{\widehat aW}\widehat g
 =
 \widehat a\bigl(-2\operatorname{Ric}_{\widehat g}
                  +\mathcal L_W\widehat g\bigr)
 +2\,\operatorname{sym}(d\widehat a\otimes W^\flat).
\]
Since
\[
d\widehat a=2\widehat\chi\,d\widehat\chi,
\qquad
W\sim\widetilde\nabla V,
\]
the omitted term has the structure
\[
\widehat\chi\,\widetilde\nabla\widehat\chi
   *\widetilde\nabla V.
\]

Consequently, (2.1) and (4.1) are not the displayed-coordinate form of the exact coupled metric equation unless \(B\) secretly depends on \(\widetilde\nabla\alpha\), contrary to its displayed arguments.

After applying \(k\) derivatives, this term contains
\[
\widehat\chi\,W*\widetilde\nabla^{k+1}\widehat\chi.
\]
So the statement “the metric equation at order \(k\) needs \(\widehat\chi\) only at order \(k\)” is not true term by term.

There is a possible energy-level recovery. Pairing the displayed top term with \(\widetilde\nabla^kV\) and integrating one derivative away from \(\widehat\chi\) produces
\[
\widetilde\nabla^{k+1}V\,
 \widehat\chi W\,\widetilde\nabla^k\widehat\chi,
\]
where the top metric derivative carries the factor \(\widehat\chi\). This is compatible with the weighted metric dissipation
\[
\int\widehat\chi^2
   |\widetilde\nabla^{k+1}V|^2.
\]
That additional metric-energy calculation is needed before the “lower-triangular” description is justified. The transport row itself has the stated grading:
\[
W\sim\widetilde\nabla V
\quad\Longrightarrow\quad
H^k\text{ transport energy needs }V\text{ at }H^{k+1}.
\]

---

## 3. Parabolic gain and its dependence on \(\varepsilon\)

For each fixed \(\varepsilon>0\), the regularized metric equation is strictly parabolic and gives
\[
V_\varepsilon\in
C_tH^s\cap L^2_tH^{s+1}.
\]
The constant in the unweighted \(L^2_tH^{s+1}\) estimate generally grows like a power of \(\varepsilon^{-1}\).

The estimate uniform as \(\varepsilon\to0\) has the weighted form
\[
\int_0^T\!\!\int_M
  (\widehat\chi^2+\varepsilon)
  |\widetilde\nabla^{s+1}V_\varepsilon|^2
 \le C,
\]
or
\[
\left\|
 \sqrt{\widehat\chi^2+\varepsilon}\,
 \widetilde\nabla^{s+1}V_\varepsilon
\right\|_{L^2_{t,x}}
\le C.
\]
It does not directly imply
\[
\|V_\varepsilon\|_{L^2_tH^{s+1}}\le C
\]
with \(C\) independent of \(\varepsilon\).

The desired ODE control may still follow from the weighted estimate, because the velocity itself contains \(\widehat a=\widehat\chi^2\). Expanding
\[
\widetilde\nabla^s(\widehat aW)
 =\widehat a\,\widetilde\nabla^sW
  +\sum_{j=1}^s
   \widetilde\nabla^j\widehat a\,
   \widetilde\nabla^{s-j}W,
\]
only the first term contains \(\widetilde\nabla^{s+1}V\). It obeys
\[
\|\widehat\chi^2\widetilde\nabla^{s+1}V\|_2
 \le \|\widehat\chi\|_\infty
      \|\widehat\chi\widetilde\nabla^{s+1}V\|_2.
\]
All \(j\ge1\) terms use at most \(s\) metric derivatives and can be treated by high-order Sobolev products. Thus a plausible uniform estimate is
\[
\|\widehat aW\|_{L^2_tH^s}
 \le C\left(
 \sqrt T\,P(\|V\|_{C_tH^s},\|\widehat\chi\|_{C_tH^s})
 +\|\widehat\chi\widetilde\nabla^{s+1}V\|_{L^2_{t,x}}
 \right).
\]
Then
\[
\int_0^T\|\widehat aW\|_{H^s}\,dt
 \le\sqrt T\,\|\widehat aW\|_{L^2_tH^s}.
\]

This weighted chain is scientifically viable, but it is not the chain written in (2.3)–(2.4). Section 4.3 also invokes a \(C_tH^s\) velocity estimate, although §2.2 supplies only \(L^2_tH^s\); the corresponding small-time factor should be \(\sqrt T\), not \(T\).

---

## 4. Transport integration by parts

This mechanism is correct for the specific nonlinear coefficient \(\psi^2\).

Set
\[
v=\psi^2W.
\]
Using a fixed background connection, the top differentiated term is
\[
\int_M
 \widetilde\nabla^\alpha\psi\,
 v^j\widetilde\nabla_j
 \widetilde\nabla^\alpha\psi\,d\widetilde\mu
 =
-\frac12\int_M
 \operatorname{div}_{\widetilde g}v\,
 |\widetilde\nabla^\alpha\psi|^2\,d\widetilde\mu.
\]
The commutator satisfies the standard estimate
\[
\|[\widetilde\nabla^k,v\cdot\widetilde\nabla]\psi\|_2
 \lesssim
 \|\widetilde\nabla v\|_\infty\|\psi\|_{H^k}
 +\|v\|_{H^k}\|\widetilde\nabla\psi\|_\infty,
\]
up to fixed-background curvature terms of lower order.

Differentiating \(v=\psi^2W\) \(k\) times produces at most \(k\) derivatives of \(\psi\), not \(k+1\). The only apparent \(k+1\) derivative is the transported term
\[
v\cdot\widetilde\nabla\widetilde\nabla^k\psi,
\]
which is exactly the term integrated by parts.

Thus, for \(k>n/2+1\) and suitable \(W\)-regularity, the transport equation propagates \(H^k\) without requiring \(\psi\in H^{k+1}\). The displayed inequality in Proposition 3.1 should be rewritten in a standard commutator form, but its top-order mechanism is sound.

---

## 5. Coefficient factorization

The pointwise identity
\[
\widehat a_1-\widehat a_2
 =\widehat\chi_1^2-\widehat\chi_2^2
 =(\widehat\chi_1+\widehat\chi_2)
  (\widehat\chi_1-\widehat\chi_2)
\]
is correct.

For \(r>n/2\), the relevant Sobolev estimate is
\[
\|\widehat a_1-\widehat a_2\|_{H^r}
 \le C\bigl(
   \|\widehat\chi_1\|_{H^r}
  +\|\widehat\chi_2\|_{H^r}\bigr)
 \|\widehat\chi_1-\widehat\chi_2\|_{H^r}.
\]
Hence the coefficient difference is genuinely proportional to the scalar difference on a fixed high-Sobolev ball.

The \(L^\infty\) estimate
\[
|\widehat a_1-\widehat a_2|
 \le2|\widehat\chi_1-\widehat\chi_2|
\]
is sufficient only for zeroth-order products. High-order products also require the \(H^r\) bounds of \(\widehat\chi_1+\widehat\chi_2\).

This factorization handles the scalar coefficient dependence, but it does not address the derivative in
\[
W(U_1)-W(U_2)\sim
 \widetilde\nabla(U_1-U_2).
\]

---

## 6. Contraction estimate and the lost metric derivative

The crucial line in §4.4 is
\[
\|W_1-W_2\|_{H^{\widetilde p}}
 \le C\|U_1-U_2\|_{H^{\widetilde p+1}}
 \le C\|U_1-U_2\|_{H^{\widetilde p}}.
\]
The second inequality is false, even when \(U_1,U_2\) lie in a uniformly bounded \(H^{\widetilde p+2}\) ball.

A Fourier-mode test makes this explicit. On a torus, let
\[
h_N=N^{-(\widetilde p+2)}
     \sin(Nx_1)\,T,
\]
where \(T\) is a fixed symmetric tensor. Then
\[
\|h_N\|_{H^{\widetilde p+2}}\asymp1,\qquad
\|h_N\|_{H^{\widetilde p+1}}\asymp N^{-1},\qquad
\|h_N\|_{H^{\widetilde p}}\asymp N^{-2}.
\]
Thus
\[
\frac{\|h_N\|_{H^{\widetilde p+1}}}
     {\|h_N\|_{H^{\widetilde p}}}
 \asymp N.
\]
Since the linearization of \(W\) is first order,
\[
\|W(U+h_N)-W(U)\|_{H^{\widetilde p}}
 \asymp\|h_N\|_{H^{\widetilde p+1}}
\]
for small perturbations. No uniform Lipschitz estimate from
\(H^{\widetilde p}\) to \(H^{\widetilde p}\) follows from the high-norm ball.

Interpolation gives only
\[
\|h\|_{H^{\widetilde p+1}}
 \le C
 \|h\|_{H^{\widetilde p}}^{1/2}
 \|h\|_{H^{\widetilde p+2}}^{1/2},
\]
which has Hölder exponent \(1/2\) in the stated contraction distance.

A viable difference estimate would have to retain the parabolic derivative term, schematically
\[
\sup_t\|\delta U\|_{H^r}^2
 +\int_0^T
   (\alpha^2+\varepsilon)
   |\widetilde\nabla^{r+1}\delta U|^2,
\]
and use the factor \(\alpha^2\) in the transport velocity to control
\[
\alpha^2\widetilde\nabla^{r+1}\delta U.
\]
Equations (4.3)–(4.4) do not contain this combined weighted norm. The omitted
\(d(\alpha^2)W\) terms also generate additional differences
\[
d(\alpha_1^2-\alpha_2^2)W_1
 +d(\alpha_2^2)(W_1-W_2),
\]
which require their own mixed energy estimates.

---

## 7. Composition with the diffeomorphism

Composition itself does not produce a derivative loss at the stated high Sobolev order, provided the diffeomorphism hypotheses are included.

For
\[
s>\frac n2+1,
\]
if \(\varphi\) is an \(H^s\) diffeomorphism with Jacobian bounded away from zero, then
\[
\varphi^{-1}\in H^s
\]
and, for smooth fixed \(\chi\),
\[
\chi\circ\varphi^{-1}\in H^s.
\]
A quantitative estimate has the form
\[
\|\chi\circ\varphi^{-1}\|_{H^s}
 \le
 C\!\left(
 \|\varphi\|_{H^s},
 \|\varphi^{-1}\|_{H^s},
 \inf_M\det D\varphi
 \right)\|\chi\|_{C^s}.
\]
Thus the simplified dependence written in §2.2 omits inverse-Jacobian data, but the regularity conclusion is valid locally near the identity.

If
\[
\widehat aW\in L^1([0,T];H^s),
\qquad s>\frac n2+1,
\]
then its flow remains an \(H^s\) diffeomorphism for sufficiently short time, with
\(\int_0^T\|\widetilde\nabla(\widehat aW)\|_\infty dt\) controlling the Jacobian. The unresolved part is therefore the uniform \(L^1_tH^s\) velocity estimate, not composition by a known \(H^s\) diffeomorphism.

---

## 8. Relation to the flat-torus computation

The two methods are genuinely different.

Step 51 sought a homogeneous curvature-energy inequality of the form
\[
E'(t)\le CE(t).
\]
The flat-torus computation in Step 52 gives
\[
E(t)=48\pi^4t^2+O(t^3),
\qquad
\frac{E'(t)}{E(t)}=\frac2t+O(1),
\]
so spatial derivatives of the cutoff generate curvature even from flat initial data.

The present construction instead uses:

- a regularized DeTurck equation;
- high-Sobolev metric energies;
- transport commutator estimates;
- a fixed-point or compactness argument.

It does not require \(E'(t)\le CE(t)\), and the flat-torus computation does not obstruct short-time existence. The JSON artifact explicitly records only algebraic and derivative-order computations and states that it does not verify the full PDE construction.

## Final mathematical status

The coupled equations and their pullback are correct, and the transport equation has the desired no-loss energy structure. The supplied proof does not yet establish Theorem 5.1 because the exact \(d(\widehat\chi^2)W\) metric terms, the weighted nature of the parabolic gain, and the first derivative in \(U\mapsto W(U)\) are not incorporated into the fixed-point contraction. A complete derivation requires an \(\varepsilon\)-uniform combined metric–transport difference estimate carrying the weighted \(L^2_tH^{r+1}\) metric derivative.