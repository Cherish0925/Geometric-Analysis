# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Verify the mathematical correctness of the per-datum existence theorem for the degenerate cutoff flow in the given note. Focus on these specific claims:

1. PRINCIPAL SYMBOL: Is the principal symbol truly diagonal? Specifically, verify that the DeTurck Lie derivative term 2sym(d(β²)⊗W^♭) contributes no second-order β derivatives to the G-equation, and that β²W·Dβ contributes no second-order G derivatives to the β-equation. The DeTurck vector field W^k = G^{ab}(Γ^k_{ab}(G) - Γ^k_{ab}(ḡ)) involves first derivatives of G; check that ∂_i(β²W^k) does not introduce ∂²G into the scalar equation.

2. (ε,ν)-INDEPENDENCE: Verify that the ratio β^{2k}/(β²+ε)^j ≤ 1 for k≥j truly controls all ε-appearances in the tame hierarchy. In particular, check the Lie cross term (A03 Step 56 eq 3.9): when ∫D^mG · βD^{m+1}β · W is integrated by parts to produce ∫βD^{m+1}G · D^mβ · W, the absorption into D_m^G uses β⁴/(β²+ε) ≤ 1. Is this the correct power? Count the β-powers precisely.

3. CONTINUATION CRITERION: The argument claims that if T_max(ε,ν) < T₀, then the H^{s₀} bound survives, so all continuation hypotheses are met. Is this logically correct? Does the H^{s₀} bound, together with Sobolev embedding, truly prevent the solution from leaving the admissible domain (G positive definite) and prevent C^k blow-up?

4. SIGN-GENERAL EXTENSION: For general σ, the only change is the zero-order term +2σβ²G. Verify that this contributes C|σ|(1+E_m) to the m-th energy estimate, as claimed. Check that no hidden σ-dependence appears in the principal or Lie terms.

5. SMOOTH LIMIT: The claim is that C^∞ convergence of (G^ε,β^ε) to (G_∞,β_∞) plus ε(R+Q)→0 gives a solution of the exact system. Is there any subtlety about convergence of the nonlinear terms (e.g. Q quadratic in DG)?

## Output

## Verifier memo — per-datum existence for the degenerate cutoff flow (S0910A01 Step 65, resting on S0910A03 Step 56)

I reconstructed each of the five points from the two notes. The construction is analytically sound; four points hold as written, and one point (the β-power bookkeeping) contains a labeling slip that does not affect the conclusion but should be aligned. Details below, followed by the downstream substance that remains unestablished.

---

### Point 1 — the principal symbol is genuinely diagonal (confirmed)

The decisive structural fact is that the cutoff enters the diffeomorphism generator as a *function times a vector field*, and the metric equation is assembled using the product rule for the Lie derivative:
$$
\mathcal L_{\beta^2 W}G=\beta^2\,\mathcal L_W G+2\operatorname{sym}\!\bigl(d(\beta^2)\otimes W^\flat_G\bigr).
$$
The full second-order content sits in $\beta^2\mathcal L_W G$, which combines with $-2\beta^2\operatorname{Ric}$ to give the standard Ricci–DeTurck block $\beta^2[G^{-1}D^2G+R+Q]$. The residual $2\operatorname{sym}(d(\beta^2)\otimes W^\flat)$ is a product of $d(\beta^2)=2\beta\,d\beta$ (first order in $\beta$) with $W^\flat$ (first order in $G$, since $W^k=G^{ab}(\Gamma(G)-\Gamma(\bar g))^k_{ab}$ is algebraic in $G^{-1}DG$). It carries no second derivative of either field. Hence no $\partial^2\beta$ enters the $G$-equation.

The scalar equation is written in **advective (non-divergence) form** $\partial_t\beta=\beta^2W\cdot D\beta+\nu\bar\Delta\beta$, i.e. $W^k$ is *not* differentiated. Since $W$ is first order in $G$ and $D\beta$ first order in $\beta$, the term $\beta^2W^k\partial_k\beta$ contains no $\partial^2G$. The concern raised in the task — that $\partial_i(\beta^2W^k)$ would produce $\partial^2G$ — is exactly what would happen in a *divergence-form* transport $\partial_i(\beta^2W^i)$, because $\partial_iW^i\supset G^{ab}\partial_i\partial G$. That off-diagonal $\partial^2G$ term does not arise here precisely because the equation is advective. I checked this is self-consistent with the geometric role of $\beta$: writing $b(t,x)=\beta(t,\varphi_t(x))$ and using $\partial_t\varphi_t=-\beta^2W|_{\varphi_t}$ gives $db/dt=(\partial_t\beta-\beta^2W\cdot D\beta)|_{\varphi_t}$, which vanishes iff the scalar equation is $\partial_t\beta=+\beta^2W\cdot D\beta$ (advective, with the stated sign). So the advective form is forced by the transport identity $\beta(t,\varphi_t)=\chi$, and the diagonal symbol (3.2) is correct. The metric block is a positive scalar times the identity on $\mathrm{Sym}^2$, i.e. strong ellipticity in the strongest sense, not merely rank-one Legendre–Hadamard — this is the intended DeTurck effect.

### Point 2 — $(\varepsilon,\nu)$-independence holds; the Lie-term power label is off by two

The ratio identity (4.4), $\beta^{2k}/(\beta^2+\varepsilon)^j\le1$ for $k\ge j\ge0$, $\beta\in[0,1]$, is correct: $\beta^{2k}/(\beta^2+\varepsilon)^j=[\beta^2/(\beta^2+\varepsilon)]^j\,\beta^{2(k-j)}\le1$.

I traced the two top-order absorptions separately, and they use **different** powers:

- **Lie cross term (A03 §3.3, eqs. 3.9–3.10).** The critical piece is $\int D^mG\cdot \beta D^{m+1}\beta\cdot W$; the single $\beta$ comes from $d(\beta^2)=2\beta D\beta$. After moving one derivative, the term to absorb is $\int \beta\,D^{m+1}G\cdot D^m\beta\cdot W$. Weighted Young against $\sqrt{\beta^2+\varepsilon}\,|D^{m+1}G|$ gives the weight ratio $\beta^2/(\beta^2+\varepsilon)\le1$ — a **single** metric-coefficient power $\beta$, so $k=j=1$.

- **Transport coupling (A03 §3.4, eqs. 3.12–3.13).** Here the drift is $V=\beta^2W$, so the coefficient of $D^{m+1}G$ is $\beta^2$, and the weight ratio is $\beta^4/(\beta^2+\varepsilon)\le\beta^2\le1$, i.e. $k=2,j=1$.

The A01 note §4.3, Lie-term bullet, attributes $\beta^4/(\beta^2+\varepsilon)\le\beta^2\le1$ to the Lie cross term. That power belongs to the transport coupling; the Lie cross term uses $\beta^2/(\beta^2+\varepsilon)\le1$. Both ratios are $\le1$ uniformly in $(\varepsilon,\nu)$, so the $(\varepsilon,\nu)$-independence conclusion is unaffected — this is a bookkeeping mislabel, not an analytic hole. Aligning the two bullets (Lie: $\beta^2/(\beta^2+\varepsilon)$; transport: $\beta^4/(\beta^2+\varepsilon)$) removes the discrepancy and makes (4.4) visibly cover both with $k\ge j$.

I also checked the remaining $\varepsilon$-appearances: the principal coefficient split $DA=2\beta D\beta\,G^{-1}+(\beta^2+\varepsilon)D(G^{-1})$ (A03 3.4) is exact and its weighted Young uses $\beta^2/(\beta^2+\varepsilon)\le1$; the viscosity contributes $-\nu\|D^{m+1}\beta\|^2+C_m\nu\|\beta\|_{H^m}^2$ with $\nu\le1$; and time-derivative bounds (4.6)/(4.2) multiply by $\beta^2+\varepsilon\le2$ and $\nu\le1$ rather than dividing. No inverse power of $\varepsilon$ or $\nu$ appears anywhere I could locate, including in the higher time-derivative induction (5.1): each $\partial_t$ inserts a bounded coefficient factor and two spatial derivatives, all controlled by (4.9).

### Point 3 — the continuation argument is logically correct (with one wording point)

The reasoning "if $T_{\max}(\varepsilon,\nu)<T_0$ then the $H^{s_0}$ bound and positivity persist, contradicting maximality" is valid. Two things make it work:

1. $s_0=\lfloor n/2\rfloor+5$ gives $H^{s_0}\hookrightarrow C^4$ (indeed $s_0>n/2+4$), which is well above the $s>n/2+2$ threshold that the fixed-$(\varepsilon,\nu)$ local theory needs. The uniform bound $\mathcal E_{s_0}\le R^2$ controls $\|G\|_{H^{s_0}},\|\beta\|_{H^{s_0}}$, hence the $C^2$-and-higher norms entering the coefficients.
2. Metric positivity $\lambda\bar g\le G\le\lambda^{-1}\bar g$ keeps the ellipticity constant $\min(\varepsilon\lambda,\nu)>0$ bounded below for fixed $(\varepsilon,\nu)$, i.e. the state stays in a compact subset of the admissible domain away from its edge.

The one place to read carefully is the phrase in Theorem A that a finite-time endpoint forces $\|u\|_{C^k}\to\infty$ "for some finite $k$." This must be understood as blow-up of a *specific* regularity threshold $k_0$ (for second-order quasilinear parabolic systems, $k_0\le2$, i.e. a $C^2$ or $C^{1,\alpha}$ or base-$H^s$ bound), not as "control every $C^k$." Under that standard reading — which is the one in Amann Ch. V and Taylor §16.1 as cited — the $H^{s_0}\hookrightarrow C^4$ bound plus uniform parabolicity exactly supplies the continuation input. I confirmed the low-order step (A03 §4, eqs. 4.1–4.3) is a non-circular continuity argument: on $\{t:\mathcal E_{s_0}\le R^2\ \text{and positivity}\}$ the differential inequality has $R$-dependent, $(\varepsilon,\nu)$-independent constants, and ODE comparison keeps $\mathcal E_{s_0}<R^2$ strictly on $[0,T_0]$, so the sup is $\ge T_0$; the fixed-$(\varepsilon,\nu)$ local solution exists up to that sup. The resulting $T_0$ is genuinely $(\varepsilon,\nu)$-free.

### Point 4 — sign-general $\sigma$ enters only the zero-order term (confirmed)

$\sigma$ appears solely through $+2\sigma\beta^2G$. This is algebraic (order zero in derivatives), so it does not touch the principal symbol, the DeTurck field $W$, or the Lie residual. In the $m$-th estimate, the Moser–Hamilton tame product (A03 2.3) with $\|\beta\|_{L^\infty}\le1$ gives $\|\beta^2G\|_{H^m}\le C_{m,R}(\|G\|_{H^m}+\|\beta\|_{H^m})$, hence $\int D^mG\cdot D^m(2\sigma\beta^2G)\le C_{m,R}|\sigma|(1+\mathcal E_m)$, matching (4.5). The stationary state on $\{\chi\neq0\}$ is $\operatorname{Ric}=\sigma g$, i.e. Einstein constant $\lambda=\sigma$; the $\sigma=-1$, $\sigma=0$, $\sigma=1$ cases correspond to the three Einstein signs, and only $T_0$ carries $\sigma$-dependence (through the Grönwall coefficient $C|\sigma|$). I found no hidden $\sigma$ elsewhere; the placement of the term with $\beta^2$ rather than $\beta^2+\varepsilon$ differs from the principal factor by $2\sigma\varepsilon G$, which is $O(\varepsilon)$ and vanishes in the limit exactly as the note states.

### Point 5 — the smooth limit of the nonlinear terms is valid (confirmed)

The uniform mixed space-time bounds (5.1) hold for all $k,j$ because time differentiation never divides by $\varepsilon,\nu$ (verified under Point 2). $C^\infty$ convergence of a diagonal subsequence then makes every derivative converge uniformly. The nonlinear terms converge for a concrete reason: the metrics stay in the fixed positive-definite shell $\lambda\bar g\le G\le\lambda^{-1}\bar g$, so $G^{-1}$ is a smooth function of $G$ on a compact set and $G_\ell^{-1}\to G_\infty^{-1}$ in $C^\infty$; the quadratic $Q(G,DG)$ is a smooth function of $(G,G^{-1},DG)$ and converges as a product of uniformly convergent, uniformly bounded arguments; $R(G,\bar g)$ and the Lie term (built from $G^{-1}DG$) converge likewise. The residuals $\varepsilon_\ell[G_\ell^{-1}D^2G_\ell+R+Q]$ and $\nu_\ell\bar\Delta\beta_\ell$ vanish in every $C^k$ because the brackets are $C^{k+2}$-bounded uniformly and the prefactors $\to0$. Passing to the limit yields $\partial_tG_\infty=\beta_\infty^2[G_\infty^{-1}D^2G_\infty+R+Q+2\sigma G_\infty]+$ Lie residual, i.e. exactly (2.3); the $2\sigma\beta^2G$ term keeps its coefficient since it never carried $\varepsilon$. I see no subtlety with the quadratic term: quadratic nonlinearity is continuous in $C^1$, and $C^1$ convergence is contained in $C^\infty$ convergence. The geometric untwisting is then standard: the DeTurck ODE (5.4) has a global smooth flow on compact $M$, the transport identity gives $\beta(t,\varphi_t)=\chi$ (I checked $d/dt[\beta(t,\varphi_t)]=0$ from the exact scalar equation with $\nu=0$), and $g=\varphi_t^*G$ solves $\partial_tg=-2\chi^2(\operatorname{Ric}-\sigma g)$.

---

### One correctness item to align, and supporting-computation reading

- The Lie/transport β-power label in A01 §4.3 (Point 2 above) should read $\beta^2/(\beta^2+\varepsilon)$ for the Lie cross term and $\beta^4/(\beta^2+\varepsilon)$ for the transport coupling. This is the only inaccuracy I found; it changes no bound.
- The allocation script (`step56_tame_allocation_check.py`, 14,002,305 partitions, reported with no violations for $7\le m\le40$) verifies only the integer derivative budget and interpolation exponents in (2.5)–(2.6). Both notes state this does not certify the tensor identities or the PDE steps; that division is stated correctly. The interpolation count itself is internally consistent: with $\theta_i=(q_i-4)/(m-4)$, two or more high factors give $\sum\theta_i\le(m-6)/(m-4)<1$, and a single high factor gives $\theta_1\le1$ (order $\le m$ after the top $D^{m+1}$ is extracted), so exactly one high $H^m$ norm appears linearly — the standard tame, not algebra, structure.

### What the theorem does and what remains open for the stated research target

The verified content is a correct **short-time, per-datum existence** result for the exact degenerate cutoff flow, valid for all $n\ge2$ and all $\sigma\in\mathbb R$, with $H^m$ control on $[0,T_0]$ and a smooth-endpoint restart. Both notes are explicit that $T_0$ depends on high Sobolev norms and the positivity constant of $g_0$, and they separate three tiers cleanly: (L1) one datum, all regularizations — proved here; (L2) family-uniform observation time under controlled Ricci defect — asserted to require the unweighted-$H_2$ first-exit bootstrap of A01 Steps 55–62 / A03 §6, *not* proved in these two notes; (L3) dimension-only $c_n,C_n$ for the Yau-26 statement — not addressed.

For the research target, the following downstream substance is what would turn this analytic component into progress on the actual problem, and none of it is settled by the material supplied here:

1. **The first-exit estimates (6.8) are used but not proved in A03 §6.** Their validity is stated to be conditional on the unweighted $H_2$, drift $Y$, $J_6$, and local $Q_\alpha$ inequalities having only first-cutoff-derivative constants after signed Hessian integration by parts (no $\|\nabla^2\chi\|_\infty$ or higher-jet constant). That conditional is exactly the mechanism that would give the family-uniform time in L2, and it is the natural next object to check independently.
2. **The Ishida–LeBrun obstruction step is entirely downstream** and is where four-manifold topology and the Seiberg–Witten input enter; the existence theorem is deliberately built without any of it, so it neither supports nor bears on that part.
3. **The route as described is four-dimensional and one-signed** ($\sigma=-1$). The $\sigma\in\mathbb R$ generality of the existence lemma is real, but the obstruction machinery it feeds is stated only for the four-dimensional $\sigma<0$ case; the positive branch, general four-manifold topology, $n\ge5$, and the dimension-only pinching constants are untouched.

So, to the specific verification request: Points 1, 3, 4, 5 are correct as written; Point 2's conclusion is correct with the noted power-label alignment. The theorem is a valid analytic building block. Its value toward the Yau-26 statement rests on the unproved first-exit inequalities and the untouched obstruction argument, which is where independent checking would next change the research judgment.