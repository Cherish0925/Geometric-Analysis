# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md"
  ]
}
```

## Task

Verify the normalized transported-coefficient Yang/DeTurck start-restart construction in Step 44 against Yang Theorem 8.2 itself. Focus on mathematical sufficiency: exact pullback/gauge transport; variation delta(a_hat) with the diffeomorphism variable; the coupled H^k energy estimate for Yang's linearized metric-transport system with epsilon^2 Delta h; whether integration by parts removes derivative loss in chi C nabla psi; whether constants are uniform in epsilon; whether these estimates really give the smooth tame inverse needed by Yang's fixed-point/Nash-Moser argument after adding -2 a_hat g_hat; coupled uniqueness when transported coefficients differ; and restart from a smooth endpoint. Identify any missing regularity, derivative, compatibility, or nonlinear argument. The goal is a rigorous scientific verdict, not a generic review.

## Output

# Verification Memo: Step 44 normalized transported-coefficient Yang/DeTurck start–restart

## Verdict in one line

The incremental mathematics is structurally correct: the added normalization term $-2\hat a\hat g$ is genuinely gauge-inert in the pullback and a bounded zeroth-order perturbation of Yang's linearized pair, and the coupled $H^k$ energy estimate closes because every derivative-loss coupling carries exactly the cutoff factor whose square supplies the (degenerate) metric dissipation. What is written establishes the $\varepsilon$-uniform linear solve and the $\varepsilon\downarrow0$ smooth limit. What is invoked rather than executed is the *tame* form of the estimate and its neighborhood-uniform version — the actual object Yang's fixed-point / Nash–Moser step consumes. Below I check each requested item and then state precisely what remains.

---

## 1. Exact pullback and gauge transport

The identity in §1–§2, $g=\varphi_t^*\hat g$ solving $\partial_t g=-2a(\operatorname{Ric}_g+g)$, is robust and does not depend on reconstructing Yang's full transport bookkeeping.

Writing $\frac{d}{dt}\varphi_t^*\hat g=\varphi_t^*(\partial_t\hat g+\mathcal L_{X_t}\hat g)$ with $X_t=(\partial_t\varphi_t)\circ\varphi_t^{-1}$, Yang's cancellation matches the gauge term $2\hat\delta^*(\hat a\,S^{-1}\delta G(S))=\mathcal L_{\hat a W}\hat g$ against $\mathcal L_{X_t}\hat g$. The diffeomorphism ODE (1.2) is untouched by the normalization, so whatever cancellation Yang has is preserved verbatim. The *new* term $-2\hat a\hat g$ is a pointwise-algebraic symmetric tensor; its pullback is purely natural,
$$\varphi_t^*(-2\hat a\hat g)=-2(\varphi_t^*\hat a)(\varphi_t^*\hat g)=-2a\,g,$$
using the tautology $\varphi_t^*\hat a=(\chi\circ\varphi_t^{-1}\circ\varphi_t)^2=\chi^2=a$. This is unconditional. The two consistency tests are correct: with $S=g_0$ one has $\delta G(S)=0$ (since $\hat\nabla g_0=0$), so the gauge and the ODE are inert at $t=0$, and if additionally $\operatorname{Ric}_{g_0}=-g_0$ the whole velocity vanishes — the $\operatorname{Ric}=-g$ fixed point is stationary. The observation that only the *weighted* generator $\hat a W$ enters the pullback (so the unweighted DeTurck vector need not vanish on $\{a=0\}$) is exactly what repairs the fixed-coefficient error of Step 35.

One item the note takes on citation: that Yang's own generator equals $-\hat a W$, i.e. the placement of $\chi^2$ and the meaning of $\varphi_{t*}$ in (1.2). From the excerpt $X_t(q)=-\hat a(q)(\varphi_{t*}W)(q)$; equality with $-\hat a W$ requires Yang's intended reading of the sharp/pushforward. Since the normalization does not enter here, this does not affect the incremental correctness, but a self-contained write-up should reproduce Yang's transport identity rather than cite it.

## 2. Variation $\delta\hat a$ with the diffeomorphism variable

Correct, with one bookkeeping correction to flag. With $\zeta=\delta\varphi\circ\varphi^{-1}$,
$$\delta\hat\chi=-d\hat\chi(\zeta),\qquad \delta\hat a=2\hat\chi\,\delta\hat\chi=-2\hat\chi\,d\hat\chi(\zeta),$$
using $\delta(\varphi^{-1})=-(d\varphi^{-1})(\psi\circ\varphi^{-1})$. This is zeroth order in $\psi$ (a fixed smooth bundle map $\zeta=\psi\circ\varphi^{-1}$) times the fixed smooth coefficient $d\hat\chi$. Hence (2.5): the normalization adds only $\hat\chi^2*h$ and $\hat\chi\,d\hat\chi*\psi$ to the metric equation, with no derivative of $h,\psi$ and no inverse power of $\hat\chi$. Type-checking $\delta(-2\hat a\hat g)=-2\hat\chi^2 h-2(\delta\hat a)\hat g$ against (2.5) is consistent.

Two things to make explicit. (a) Step 37 §3 wrote $\delta\hat a=+2\hat\chi\,d\hat\chi(\psi)$; Step 44 corrects the sign and the argument to $-2\hat\chi\,d\hat\chi(\zeta)$. Only the magnitude enters the energy estimate, but the earlier form was imprecise and the two notes now disagree literally. (b) The passage from $\zeta$ to $\psi$ in (2.5) uses $H^k$-equivalence of $\psi$ and $\psi\circ\varphi^{-1}$ under the fixed smooth $\varphi_t$; true per datum, worth one line.

## 3. Coupled $H^k$ estimate with $\varepsilon^2\Delta h$, and removal of derivative loss in $\hat\chi C\nabla\psi$

This is the technical center and it is done correctly.

- **Metric diffusion (3.3).** $2\langle\nabla^kh,\nabla^k(\hat\chi^2\Delta h)\rangle$: the leading integration by parts yields $-2\|\hat\chi\nabla^{k+1}h\|_2^2$ plus a term from $\nabla(\hat\chi^2)=2\hat\chi\,d\hat\chi$; the single $\hat\chi$ factor there pairs against the weighted top norm, so Young distributes the weight and no inverse power of $\hat\chi$ appears. Commutator terms with $\ge2$ derivatives on $\hat\chi^2$ carry $\le k$ derivatives of $h$. Correct.

- **The derivative-losing coupling (3.5)–(3.6).** The term $\hat\chi C\nabla^{k+1}\psi$ is one order above what $\mathcal E_k$ controls, and the transport equation gives no $\psi$-dissipation. One integration by parts,
$$\int\nabla^kh\,\hat\chi C\nabla^{k+1}\psi=-\int\hat\chi C\,\nabla^{k+1}h\,\nabla^k\psi-\int\nabla(\hat\chi C)\,\nabla^kh\,\nabla^k\psi,$$
transfers the derivative onto $h$. The first term is $C\cdot(\hat\chi\nabla^{k+1}h)$ against $\nabla^k\psi$, absorbed by Young into $\rho\|\hat\chi\nabla^{k+1}h\|^2+C_\rho\|\psi\|_{H^k}^2$; the second is order $k$ in both. No $\|\psi\|_{H^{k+1}}$ survives. This is exactly why Yang's $C$ carries a single $\hat\chi$: the loss lands in the one place ($\hat\chi\nabla^{k+1}h$) where degenerate dissipation exists. Correct and essential.

- **Transport (3.7)–(3.8).** The metric-side coupling $\hat\chi^2 Q\nabla^{k+1}h=\hat\chi Q(\hat\chi\nabla^{k+1}h)$ is again absorbed into the weighted dissipation. The top self-transport term $\int\nabla^k\psi\,\hat\chi^2P\nabla^{k+1}\psi\le C\|\psi\|_{H^k}^2$ is asserted; this is the one place the estimate *needs* a property of Yang's $P$ — that its principal part is (anti)symmetric/symmetrizable so that the top-order transport integrates by parts to lower order. Geometrically $P$ is an advection/Lie-type operator and this holds, but the note inherits it from Yang without checking the explicit $P$. For self-containment this must be shown against Yang's (8.8).

- **Degeneracy on $\{\hat\chi=0\}$.** Every derivative-loss term ($\hat\chi C\nabla^{k+1}\psi$, $\hat\chi^2 Q\nabla^{k+1}h$) carries a $\hat\chi$ factor, so it is supported where dissipation exists; on $\{\hat\chi=0\}$ the $h$-equation reduces (as $\varepsilon\to0$) to a coefficient ODE with no coupling loss. The estimate therefore closes uniformly despite the dissipation weight vanishing. The note's emphasis on the one-cutoff-factor structure is the correct crux.

- **Normalization terms (3.9).** $\hat\chi^2 h$ and $\hat\chi\,d\hat\chi*\psi$ are zeroth order with smooth coefficients, bounded by $\mathcal E_k$; no loss, no inverse $\hat\chi$. Correct.

- **Assembly and $\varepsilon$-uniformity (3.10).** Finitely many absorptions each spend $\rho$ of the fixed weighted-dissipation budget $c\|\hat\chi\nabla^{k+1}h\|^2$; small $\rho$ and large $A_k$ close the loop. Crucially, all absorptions draw on the weighted (not the $\varepsilon^2$) dissipation, and the $\varepsilon^2$ term contributes only extra nonnegative dissipation plus a harmless $C\varepsilon^2\|h\|_{H^k}^2\le C\|h\|_{H^k}^2$. Hence the constants are $\varepsilon$-independent. Gronwall gives $\varepsilon$-uniform $H^k$ bounds at every order; the equations give time-derivative bounds two orders lower ($\varepsilon^2\Delta h$ costs $\varepsilon^2\|h\|_{H^{k}}\to0$). Aubin–Lions/Arzelà–Ascoli then produce the smooth $\varepsilon\downarrow0$ limit solving (2.1)–(2.2). This chain is valid.

Existence of the regularized solution for fixed $\varepsilon$ (a parabolic-$h$/transport-$\psi$ coupled linear system with smooth coefficients) is Yang's assertion and is standard; the note relies on it.

## 4. Whether these give the smooth tame inverse Nash–Moser needs (after adding $-2\hat a\hat g$)

This is where the note reduces to Yang rather than completing the analysis, and the reduction is logically valid but not fully executed.

The Gronwall output $\mathcal E_k(t)\le e^{C_kt}\big(\mathcal E_k(0)+\int\|f\|_{H^k}^2+\|\eta\|_{H^k}^2\big)$ is an energy estimate with $C_k$ depending on finitely many derivatives of the reference pair and cutoff. Hamilton's implicit-function machinery consumes a *tame* estimate: linear in the high norm of the data with a fixed derivative loss, and constant depending polynomially on high norms of the coefficients, holding *uniformly for the linearization at every point of a neighborhood*. Two steps are asserted ("standard commutator interpolation puts the dependence in the same smooth tame form used by Yang") but not carried out:

1. The Moser/Gagliardo–Nirenberg product and commutator estimates that convert $C_k$ into the tame polynomial-in-coefficient-norm form with explicit loss $r$. The raw commutators $[\nabla^k,\hat\chi^2\Delta]h$ etc. produce $\|\nabla^k(\text{coeff})\|\,\|h\|_{H^2}$ pieces that must be interpolated; this is genuinely standard, but it is the content of "tame," and it is not written.

2. The tame invertibility as a *family* over a neighborhood of the reference pair, uniformly. The note verifies the estimate at "a solution"/reference and gestures at "a bounded set of smooth reference pairs." The Nash–Moser step needs $D\Phi(u)^{-1}$ tame-uniformly for $u$ near the reference.

On the incremental question — does adding $-2\hat a\hat g$ preserve whatever tame inverse Yang has — the answer supported by §3 is yes: $D\Phi_{\mathrm{norm}}=D\Phi_{\mathrm{Yang}}+\big(-2\hat a\,h-2(\delta\hat a)\hat g,\,0\big)$ is a bounded zeroth-order perturbation depending tamely on $u$, absorbed by Gronwall without touching the principal $2\hat\chi^2\Delta$ symbol or the transport structure. So "normalized tame inverse ⟸ Yang's tame inverse + bounded zeroth-order term" is a correct implication *given Yang's Theorem 8.2 as a black box supplying the reduction "linearized unique smooth solution + tame estimate ⟹ nonlinear existence."* Yang does assert that reduction in the excerpt. The residual work is thus not the incremental step but the underlying tame estimate itself, which Yang leaves at "standard arguments" and which Step 44 also leaves at that level. Step 41 §5.1 and its status table already record this as the outstanding analytic obligation ("full tame estimates not yet written"); Step 44 advances it by writing the $\varepsilon$-uniform energy estimate and the limit, but not the tame form or the family version.

## 5. Coupled uniqueness when transported coefficients differ

Correct in structure. For two solutions with equal initial data, $\Phi(u_1)-\Phi(u_2)=\int_0^1 D\Phi(u_s)\,ds\,(u_1-u_2)=0$ gives a homogeneous linear system of the form (2.1)–(2.2) for $(h,\psi)=(\hat g_1-\hat g_2,\varphi_1-\varphi_2)$ with segment-averaged smooth coefficients. The coefficient difference is controlled at zeroth order,
$$\hat a_1-\hat a_2=-2\hat\chi\,d\hat\chi*(\varphi_1-\varphi_2)+\text{smooth quadratic},$$
so metric and transport differences are estimated together; (3.10) with zero forcing and zero initial data yields $\mathcal E_k\equiv0$. The point that this needs no pointwise vanishing of the ordinary DeTurck vector on $\{a=0\}$ is correct, since the coupling is handled through the shared energy, not through the gauge field. Two details are invoked: the segment $u_s$ living in a genuine chart on metrics and diffeomorphisms (positivity of $\hat g_s$, a vector-field representation of $\varphi_s$), and the geometric-uniqueness lift — representing a geometric solution $g$ in Yang's gauge with fixed $S$, which itself requires solving the coupled diffeomorphism problem. Both are standard for DeTurck-Ricci flow but are stated, not constructed.

## 6. Restart from a smooth endpoint

Correct given its hypothesis. If $g(t)\to g_*$ smooth and positive-definite as $t\uparrow T_*$, the per-datum local-flow theorem applied to $(g_*,\chi)$ with new background $S=g_*$ starts a solution; geometric uniqueness glues it to the old one on the overlap; extension follows. There is no circularity: the per-datum time may depend on all smooth norms of $(g_*,\chi)$, and the existence of the smooth positive-definite limit is explicitly deferred to the separate continuation result (Step 41 §5.5, the shifted-curvature continuation). The restart is only as strong as that continuation statement, which the note correctly disclaims here.

---

## Genuine remaining analytic substance (for a self-contained proof)

1. **Tame form written out.** Execute the Moser/Gagliardo–Nirenberg commutator interpolation turning $C_k$ in (3.10) into a tame constant (polynomial in coefficient norms, fixed derivative loss). This is the object Yang's reduction consumes and is presently invoked verbatim from Yang.

2. **Neighborhood-uniform tame family.** State and prove the linearized tame estimate uniformly for the linearization at every point of a smooth neighborhood, as the implicit-function step requires, not only at a reference pair.

3. **Transport top-order (3.7).** Verify (anti)symmetry/symmetrizability of Yang's principal $P$ from (8.8) so the top transport term integrates to lower order; currently inherited.

4. **Geometric-uniqueness lift.** Construct the representation of a geometric solution $g$ in Yang's gauge with fixed $S$ (existence of $\varphi_t$ solving the coupled ODE), which the pull-back-uniqueness argument uses.

5. **Bookkeeping.** Reconcile the $\delta\hat a$ sign and $\psi$-vs-$\zeta$ statement between Step 37 §3 and Step 44 (2.4)–(2.5), and record the $H^k$-equivalence of $\psi$ and $\psi\circ\varphi^{-1}$.

6. **Yang's own transport identity.** Reproduce $X_t=-\hat a W$ from (8.5)–(8.6) rather than citing it, closing the one gauge algebra fact the pullback of the Yang part rests on (the normalization part is independent of it).

None of items 1–6 are errors in Step 44; items 1–2 and 3–4 sit at exactly the level Yang leaves them, while 5–6 are small internal-consistency and citation matters. The mathematical mechanism the note isolates — normalization as a gauge-inert, bounded zeroth-order term, and derivative-loss couplings weighted by the same cutoff that carries the dissipation — is the correct and sufficient structural reason the normalized transported-coefficient system inherits Yang's short-time existence, uniqueness, and restart. The construction is sufficient modulo importing Yang's Theorem 8.2 as a proven reduction; it is not yet sufficient as a stand-alone tame-estimate proof.