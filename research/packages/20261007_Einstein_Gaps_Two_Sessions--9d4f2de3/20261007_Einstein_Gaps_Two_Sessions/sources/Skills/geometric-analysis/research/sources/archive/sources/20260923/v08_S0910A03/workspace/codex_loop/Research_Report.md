# Research Report: weighted Moser audit and continuation repair

## Task and context

This run audited two remaining analytic claims for the normalized fixed-cutoff flow

\[
\partial_tg=-2a(\operatorname{Ric}+g),\qquad a=\chi^2:
\]

the proposal to obtain the first weighted pointwise bounds by ordinary unweighted Moser iteration on

\[
T=\operatorname{Rm}+G,\quad U=aT,\quad
E=\operatorname{Ric}+g,\quad V=aE,
\]

and the shifted-curvature smooth-extension induction at the order where \(\nabla^mU\) interacts with high cutoff derivatives.

The current proposal supersedes the previous continuation-only task. The older artifact Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md has been given a prominent correction notice.

## Main verdict

The proposed ordinary unweighted Moser iteration on \(U,V\) fails. Although the existing \(H_3\) and \(J_6\) seeds control \(\|U\|_{L^3}\) and \(\|V\|_{L^6}\), the principal operator remains \(a\Delta\). Its energy controls only \(\int a|\nabla |Z|^{p/2}|^2\), not the unweighted gradient required by standard Sobolev/Moser. Moreover, the shifted curvature reaction is \(U*U\), not \(aU*U\), so the \(U\)-energy contains an unweighted \(\int|U|^{p+1}\) term.

The strongest valid replacement is the mixed weighted recurrence for

\[
H_p(f)=\int\eta^2a^{p-2}f^p,\qquad
f=F=(1+|\operatorname{Rm}|^2)^{1/2}\ \text{or}\ |E|.
\]

The time-slice identity

\[
H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2,\qquad
z_p=\eta a^{(p-1)/2}f^{p/2},
\]

repairs the previously detected half-power mismatch. Conditional on the session's same-support positive-time \(H_3\) estimate, propagated \(J_6\), metric comparison, and Sobolev persistence, it yields the intended volume-independent endpoints

\[
\|aF(t)\|_\infty\le C\beta/t,\qquad
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
\]

The smooth-extension theorem remains valid, but its earlier derivative graph must be corrected. At order \(m\), one must first estimate the coupled pair

\[
(\nabla^mU,\nabla^{m+1}\chi),
\]

and only then estimate \(\nabla^mT\). Wang's printed Proposition 4.14 does not justify dependence on cutoff derivatives only through order \(m\).

## Tensor equations and weak energies

Using

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
\operatorname{Ric}(G)=g,\qquad
\operatorname{Ric}(U)=V,
\]

the velocity is exactly \(\partial_tg=-2V\). The shifted equation is

\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\]

Multiplication by \(a\), with all product terms rewritten polynomially, gives

\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U+U*U+aG*U.
\]

The identity \(a^2T*T=U*U\) is the important weight check.

Starting from the exact defect equation, the \((\Delta a)E\) and \(2\,da*\nabla E\) terms cancel the corresponding product-rule terms in \((\partial_t-a\Delta)(aE)\). The remaining equation is

\[
(\partial_t-a\Delta)V
=da*\nabla V+\nabla^2a*V+d\chi*d\chi*V
+U*V+V*V+aG*V.
\]

It is homogeneous in \(V\), and \(|V|\le C_n|U|\).

Hessian-cutoff terms in both equations can be integrated once without dividing by \(a\), using

\[
|da|\,|Z|^{p-1}|\nabla Z|
=2|d\chi|\,|Z|^{p/2}
 \bigl(\chi|Z|^{(p-2)/2}|\nabla Z|\bigr).
\]

Including moving tensor norms and \(\partial_td\mu=-(\operatorname{tr}V)d\mu\) gives

\[
\frac d{dt}\int|U|^p
+c_pp\int a|U|^{p-2}|\nabla U|^2
\le Cp^2(1+r^{-2})\int|U|^p+Cp\int|U|^{p+1},
\]

and

\[
\frac d{dt}\int|V|^p
+c_pp\int a|V|^{p-2}|\nabla V|^2
\le Cp^2(1+r^{-2})\int|V|^p
+Cp\int|U||V|^p.
\]

No unweighted \(T\), higher cutoff derivative, or or or division by \(a\) occurs in these weak inequalities. Their failure is specifically at coercivity and reaction absorption.

## Exact obstruction to ordinary Moser

For \(w=|U|^{p/2}\), Sobolev can be applied to \(\chi w\), producing

\[
\|\chi w\|_4^2
=\left(\int a^2|U|^{2p}\right)^{1/2},
\]

not the unweighted next norm \((\int|U|^{2p})^{1/2}\). The same problem occurs for \(V\).

This is not just formal bookkeeping. Near a regular zero of \(\chi\), take \(a=x^2\) and a triangular normal bump supported in \([\varepsilon,2\varepsilon]\). Its one-dimensional factors satisfy

\[
\int w_\varepsilon^2=\varepsilon/3,\qquad
\int w_\varepsilon^4=\varepsilon/5,\qquad
\int x^2|w_\varepsilon'|^2=28\varepsilon/3.
\]

Hence the ratio of the unweighted \(L^4\) quantity to the weighted gradient plus \(L^2\) terms grows as \(\varepsilon^{-1/2}\). Smooth approximations preserve this scaling. Therefore no uniform degenerate Sobolev inequality needed by ordinary Moser is available.

The seeds themselves are valid:

\[
\int|U|^3\le CH_3,\qquad \int|V|^6\le J_6,
\]

but a seed cannot compensate for the missing Sobolev coercivity or the unweighted \(U*U\) reaction.

## Valid weighted recurrence and endpoints

For the weighted hierarchy, set

\[
D_p=\int\eta^2a^{p-1}f^{p-2}|\nabla f|^2,\qquad
z_p=\eta a^{(p-1)/2}f^{p/2}.
\]

The tensor power calculation gives

\[
H_p'+c\|\nabla z_p\|_2^2
\le Cp^Nr^{-2}H_p+CpR_p,\qquad
R_p=\int\eta^2a^{p-1}Ff^p.
\]

The exact three-factor decomposition

\[
\eta^2a^{p-1}Ff^p
=(aF^3)^{1/3}(\eta^2a^{p-2}f^p)^{1/3}z_p^{4/3}
\]

and Sobolev–Young imply

\[
H_p'+cD_p\le Cp^N(r^{-2}+S^2Y)H_p,\qquad
Y=\int aF^3.
\]

The corrected next-exponent bridge is

\[
H_{3p/2}
=\int(a^{p-2}f^p)^{1/2}z_p^2
\le H_p^{1/2}\|z_p\|_4^2.
\]

Nested time cutoffs with \(p_{k+1}=3p_k/2\) then yield

\[
\|af(t)\|_\infty
\le CS^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(s)\,ds\right)^{1/p_0}.
\]

For \(p_0=3\), the positive-time \(H_3\) seed gives \(\|aF\|_\infty\le C\beta/t\). For \(p_0=6\), \(J_6\le C\delta^6\operatorname{Vol}\) and \(S\asymp r^2\operatorname{Vol}^{-1/2}\) give \(\|aE\|_\infty\le C\delta(r^2/t)^{1/3}\). Thus volume cancellation survives through the weighted recurrence.

These endpoint conclusions remain dependent on the existing session inputs: the same-support \(H_3\) estimate, \(J_6\) propagation, and the simultaneous metric/Sobolev first-exit bootstrap. This run proves the missing weight bridge and refutes the unweighted shortcut; it does not independently re-prove all those upstream inputs.

## Corrected smooth-extension induction

Under the terminal hypothesis \(\|U\|_\infty\le K\), metric equivalence and Sobolev constants are uniform, and the base energy gives \(\|T\|_{L^q}<\infty\) for every finite \(q\).

Let

\[
W_m=\nabla^mU,\qquad C_{m+1}=\nabla^{m+1}\chi.
\]

The high terms in the \(W_m\) equation are

\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]

\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla W_m.
\]

Writing \(P_p(W)=|W|^{p-2}W\), one integration by parts in \(\Gamma_1\) produces

\[
-\int\nabla P_p(W_m)*\chi C_{m+1}*U.
\]

Young's inequality leaves the nonremovable current-order term

\[
C K^2\int|C_{m+1}|^2|W_m|^{p-2}
\le CK^2\|C_{m+1}\|_p^2\|W_m\|_p^{p-2}.
\]

This is the precise omission in a cutoff-through-order-\(m\) argument. The remaining descendants of \(\Gamma_1\), together with \(\Gamma_2,\Gamma_3\), are expanded in the main memo. Integrating the current cutoff derivative in the \(\Gamma_3\)-type term leaves only cutoff order \(m\), lower \(U,T\) derivatives, and diffusion-absorbable terms. \(\Gamma_4\) is absorbed directly.

The cutoff evolution has the exact derivative count

\[
\partial_t\nabla^{m+1}\chi
=\sum_{q=0}^{m-1}\nabla^q(\partial_t\Gamma)*
\nabla^{m-q}\chi,\qquad
\partial_t\Gamma
=g^{-1}*\nabla V=g^{-1}*\operatorname{Ric}(\nabla U).
\]

Its unique current-order term is \(\nabla^mU*\nabla\chi\). After regularizing the norms, the two estimates are

\[
\mathcal X_{m,p}'
+c\mathscr D_{m,p}
\le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}),
\]

\[
\mathcal Z_{m+1,p}'
\le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}),
\]

where

\[
\mathcal X_{m,p}\simeq\|\nabla^mU\|_p^2,\qquad
\mathcal Z_{m+1,p}\simeq\|\nabla^{m+1}\chi\|_p^2.
\]

Joint Gronwall closes the pair.

For an explicit finite Hölder schedule at target exponent \(p\):

- current \(W_m,C_{m+1}\) factors use the same \(L^p\) exponent;
- squared products of two previous-level factors use \(L^{4p}\);
- all remaining monomials use previous-level \(L^{8p}\) norms;
- terms retaining \(\chi\) use Sobolev on \(\chi|W_m|^{p/2}\).

There is no infinite exponent cascade because previous levels are already known for every finite exponent.

After the current pair is bounded, the \(\nabla^mT\) energy is estimated. Its top cutoff term \(\chi\nabla^{m+2}\chi*T\) loses one derivative by integration by parts and uses the now-available \(\nabla^{m+1}\chi\). The current connection commutator

\[
\int|\nabla^mU|\,|T|\,|\nabla^mT|^{p-1}
\]

closes with \(\nabla^mU,T\in L^{2p}\). This yields \(\nabla^mT\in L^p\) for every finite \(p\). Repeating the pair-first, \(T\)-second order and then applying Sobolev proves all weighted curvature derivative bounds needed for smooth extension.

## Disjoint macro-supports

For a common flow with \(a=\sum_j\chi_j^2\) and pairwise disjoint active and buffered macro-supports:

- at each point only one cutoff is active, so no \(d\chi_i*d\chi_j\) cross terms occur;
- weighted energies and defect energies sum exactly componentwise;
- global pointwise endpoints are componentwise maxima and remain independent of the number of components under uniform support geometry and seeds;
- the ordinary \(U,V\) Moser obstruction persists in every transition collar;
- the corrected continuation theorem applies to the single global coefficient \(a\);
- stationary collars between the enlarged buffers are necessary for the localized integrations to remain additive.

In DeTurck gauge, the entire coefficient is transported as \(\widehat a=a\circ\phi^{-1}\), multiplying both \(\operatorname{Ric}(\widehat g)\) and \(\widehat g\). Pullback restores the original fixed union of supports.

## Artifacts

- Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md contains the complete derivation, explicit weak energies, functional obstruction, valid weighted recurrence, expanded high-order continuation terms, finite exponent schedule, and macro-support implications.
- Sessions/S0910A03/workspace/codex_loop/work/verify_weighted_moser_coupling.py verifies the product and weight identities, endpoint exponent sums, defect volume cancellation, degenerate-Sobolev scaling counterexample, and Hölder schedules.
- Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md now carries a supersession notice. Its shift identities remain useful, but its old cutoff-through-order-\(m\) dependency claim must not be used.

The derivation was checked against:

- Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md;
- Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md;
- Sessions/S0910A01/workspace/notes/step30_weighted_moser_and_family_repair.md;
- Wang Section 4 in Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md.

## Verification performed

The command

    $QIUSHI_PYTHON Sessions/S0910A03/workspace/codex_loop/work/verify_weighted_moser_coupling.py

returned

    PASS: U/V products, mixed weights, endpoint exponents, degenerate-Sobolev scaling, and coupled Holder schedule

The script also passed Python byte-compilation. Display-math and LaTeX environment delimiters in the main memo were checked and found balanced.

## Handoff and unresolved scope

Qiushi should reject ordinary unweighted Moser on \(U,V\), retain \(U\) for velocity and continuation, and use the weighted mixed recurrence for the first pointwise curvature and defect bounds. The continuation proof should be reorganized at every order as

\[
(\nabla^mU,\nabla^{m+1}\chi)\quad\longrightarrow\quad\nabla^mT.
\]

The analytic weight mismatch and Wang cutoff-order omission are repaired. The global four-dimensional negative Ricci-pinching route still depends on the upstream \(H_3\), \(J_6\), common first-exit, support-selection, and terminal topological/calibration arguments. Nothing here establishes the full Yau Problem 26 or its other branches and dimensions.