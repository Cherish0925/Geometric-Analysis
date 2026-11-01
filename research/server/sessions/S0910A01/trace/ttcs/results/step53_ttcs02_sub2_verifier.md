# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/scripts/verify_step55_direct_construction.py",
    "Sessions/S0910A03/workspace/data/step55_direct_construction_checks.json",
    "Sessions/S0910A01/trace/ttcs/results/step53_ttcs01_verifier1_integration.md",
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md"
  ]
}
```

## Task

Verify A03 Step56's repaired direct transported-cutoff flow construction after the Step55 critique. Read the Step56 note, the Step55 note/checks for context, the TTCS Step53 critique, and the patched A01 Step45 consolidated IL proof. Focus on whether the tame product lemma and arbitrary-order hierarchy really repair the false derivative split; whether the doubly regularized parabolic-scalar-viscosity system can be used without epsilon/nu losses; whether the smooth epsilon,nu->0 passage and pullback give a per-datum exact flow; and whether the corrected first-exit interface (unweighted H2/K2, stationary Q remainder, per-datum start plus positive-time continuation) is coherent. Also check the patched Liouville-invariance averaging in A01 Step45 lines around 560--580: does it remove the exponential-map multiplicity concern under collapse? Identify remaining mathematical work before the restricted Ishida--LeBrun theorem is complete, without treating Step56 as a global Yau-26 solution.

## Output

# Scientific Verification Memo — A03 Step 56 (tame repair) and the A01 Step 45 Liouville patch

## Summary judgment

Step 56 makes a genuine and largely correct repair of the derivative-split error that invalidated Step 55 §5. The tame product lemma (§2) is essentially sound; I checked the underlying Gagliardo–Nirenberg counting below and it delivers the linear-in-$H^m$ structure it needs. The doubly regularized system (1.2), with scalar viscosity $\nu\bar\Delta\beta$, is a real structural improvement: it converts the earlier parabolic-plus-transport coupling into a genuinely parabolic system with diagonal principal blocks, and it makes $0\le\beta\le1$ (1.3) a direct maximum-principle statement. No inverse power of $\varepsilon$ or $\nu$ enters any of the energy estimates. The smooth $(\varepsilon,\nu)\to(0,0)$ passage and pullback give existence (not uniqueness, correctly) of a per-datum exact flow of $\partial_t g=-2\chi^2(\operatorname{Ric}_g+g)$. The reorganized first-exit interface (§6) is logically coherent and addresses the sequence-uniform-time concern from the Step 53 memo by the correct move: it concedes that the local existence time is per-datum and replaces it with a positive-time continuation argument whose constants use only sequence-uniform inputs.

The A01 Step 45 §7.2 Liouville-invariance rewrite of the terminal averaging does remove the exponential-map multiplicity concern under collapse. I verified the change of variables to the unit tangent bundle in detail.

What still stands between this and a complete restricted Ishida–LeBrun theorem is analytic content that is stated in Step 56 §6 but derived elsewhere (A01 Steps 34–36) or not in the supplied material at all: the sequence-uniform first-exit evolution inequalities (in particular the treatment of the $\chi\nabla^2\chi$ part of $\nabla^2 a$), and the continuation/regularity bootstrap that upgrades the weighted curvature bound at a terminal slab to a smooth restart, including collar behavior.

---

## 1. Tame product lemma §2 — verified

This is the load-bearing repair. Step 55 §5 asserted that for $j\le m-s$ the coefficient derivative $D^j[(\beta^2+\varepsilon)G^{-1}]$ is controlled by the fixed low energy $E_s$; that is false (take $m=3s$, $j=2s$). Step 56 replaces it by retaining the high derivative linearly in the current $H^m$ norm.

I checked (2.5)–(2.6) by the Gagliardo–Nirenberg exponent count. With $s_0>n/2+4$ we have $H^{s_0}\hookrightarrow W^{4,\infty}$, so factors of order $\le 4$ sit in $L^\infty$. For a factor of order $q_i>4$, interpolating $D^{q_i}$ between $D^{m}$ (in $L^2$) and $D^{4}$ (in $L^\infty$) gives $\theta_i=(q_i-4)/(m-4)$ and $1/p_i=\theta_i/2$. For an $L^2$ product one needs $\sum_{\text{high}}\theta_i\le 1$, i.e.
$$
\sum_{\text{high}}(q_i-4)\le m-4 .
$$
With one high factor ($h=1$): the requirement is $q_1\le m$, satisfied by the hypothesis $q_i\le m$. With $h=2$: $\sum\theta_i=(q_1+q_2-8)/(m-4)\le (m+2-8)/(m-4)=(m-6)/(m-4)<1$, using $\sum q_i\le m+2$. For $h\ge2$ the requirement $\sum_{\text{high}}q_i\le m+4(h-1)$ is weaker than $\sum q_i\le m+2$. So the total $H^m$ power never exceeds $1$, and on the neighborhood (2.2) the product is bounded by $C_{m,R}(1+\|G\|_{H^m}+\|\beta\|_{H^m})$. The exponent condition (2.1), $s_0>n/2+4$, is exactly what makes $W^{4,\infty}$ available, and the "$+2$" derivative surplus in (2.5) is absorbable precisely because the base regularity is $W^{4,\infty}$ rather than $L^\infty$.

Consequences (2.7)–(2.8) follow directly. I checked (2.8): $D^{m+1}(\beta^2)-2\beta D^{m+1}\beta=\sum_{k=1}^m\binom{m+1}{k}D^k\beta\,D^{m+1-k}\beta$, a genuine product of two $\beta$-derivatives (orders $\le m$, total $m+1\le m+2$), so tame estimation gives $\le C_R\|\beta\|_{H^m}$ — linear, as stated.

This lemma is the correct object and it genuinely differs from the false Step 55 split: the high derivative is kept linearly in $\mathcal E_m$, not asserted to be a fixed constant.

## 2. Arbitrary-order hierarchy §3 — the substituted estimates close

Proposition 3.1's individual terms check out with the tame lemma:

- §3.1 principal term: the $k=1$ coefficient derivative splits as (3.4); the $2\beta D\beta\,G^{-1}$ piece uses $\beta^2/(\beta^2+\varepsilon)\le1$ under weighted Young, giving (3.5) with no $\varepsilon^{-1}$. The $k\ge2$ terms $D^kA\,D^{m-k+2}G$ have both factors of order $\le m$ and total order $m+2$; the tame bound (2.7) then pairs against $D^mG$ to give (3.6). This is exactly the location of the former error, now correctly handled.
- §3.2 quadratic term: top factor absorbed by weighted Young, rest tame.
- §3.3 Lie cross term: the two top allocations (3.8) and the (3.9)–(3.10) integration of the ordered $D^{m+1}\beta$ produce one weighted-absorbable term and tame remainders. I checked the first term of (3.10) absorbs via $\beta^2/(\beta^2+\varepsilon)\le1$.
- §3.4 transport and viscosity: (3.12)–(3.13) use $\beta^4/(\beta^2+\varepsilon)\le1$; the $\nu\bar\Delta\beta$ term contributes a favorable dissipation and a $\nu\|\beta\|_{H^m}^2\le\|\beta\|_{H^m}^2$ term.

Every $\varepsilon,\nu$ appears with a favorable sign or through a ratio bounded by $1$. The inequality (3.2) with $(\varepsilon,\nu)$-independent constants is credible.

## 3. Common interval and higher orders §4 — the tame feature holds

The essential tame property is that the coefficient $C_{m,R}$ in (3.2) depends only on the low-order neighborhood (2.2), not on $\mathcal E_m$. Consequently, once the $m=s_0$ bootstrap fixes $[0,T_0]$ and maintains (2.2) there, Grönwall for each $m>s_0$ closes on the same $[0,T_0]$ with (4.4). The interval genuinely does not shrink with $m$. This is the correct, Nash–Moser-free structure, and it is what a tame construction should produce.

The doubly regularized system is now legitimately quasilinear strongly parabolic in both blocks, so "standard strongly parabolic theory" for fixed positive $(\varepsilon,\nu)$ is a much cleaner invocation than in Step 55, where $\beta$ obeyed a first-order transport equation and the coupled system was parabolic–hyperbolic. The scalar-viscosity version also gives (1.3) before removing either regularization, which the earlier route obtained only through transport level-set preservation.

Two points a full writeup still needs: the fixed-$(\varepsilon,\nu)$ local existence and continuation for the coupled system must be produced by an approximation (the note offers Galerkin/spectral truncation) that preserves both metric positivity and the transport integration-by-parts / commutator structure used in §3; and the truncation's compatibility with the maximum principle (1.3) should be stated, since (1.3) is used structurally.

## 4. Limit and pullback §5 — existence, correctly not uniqueness

(5.1)–(5.2): repeated time differentiation uses only higher spatial bounds and $0<\varepsilon,\nu\le1$, never divides by them, so a diagonal subsequence converges in every space-time $C^k$ to a smooth $(G,\beta)$ solving (1.1). The pullback (5.3)–(5.4) is the same computation verified in Step 55 §7 (with $\beta$ evaluated at $\varphi(t,x)$), and I re-confirm $\frac{d}{dt}\beta(t,\varphi(t,x))=0$ and the Lie-term cancellation give $\partial_t g=-2\chi^2(\operatorname{Ric}_g+g)$.

Step 56 explicitly asserts only existence of at least one smooth per-datum flow and defers canonical uniqueness. This is the right posture: the Ishida–LeBrun application uses existence and restart, and the earlier difference-ledger uniqueness for arbitrary smooth solutions is not reconstructed here.

## 5. First-exit interface §6 — coherent architecture; several inequalities asserted, not derived here

The three §6 moves are individually correct in structure:

- §6.1: at $q=2$ the hierarchy weight $a^{q-2}=a^0=1$, so $H_2^\alpha=\int\eta_\alpha^2 F_T^2$ is genuinely unweighted and controls curvature across the matched $\eta_\alpha$ support, including small-$a$ collars. Since $T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)}$ differs from $\operatorname{Rm}$ by a fixed multiple of the constant-curvature tensor, $|T|^2$ and $1+|\operatorname{Rm}|^2$ are comparable up to an additive volume term, so the maximal-function seed (6.3) is legitimate. This addresses the Step 53 concern that an $a$-weighted energy is too weak for Sobolev absorption.
- §6.2: I verified $\{1-\rho>0\}\subseteq\{a=0\}$. With disjoint $B_{7r}$ buffers at most one $\eta_\alpha$ is nonzero at a point, so $\rho\le1$; and $\chi_\alpha>0\Rightarrow\eta_\alpha=1\Rightarrow\rho=1$, whose contrapositive is $\rho<1\Rightarrow a=0$. On $\{a=0\}$ the exact flow is stationary, so $Q_{\rm rest}(t)=Q_{\rm rest}(0)$ and the split (6.6)–(6.7) is exact. This is a correct refinement of the A01 §6.3 global-$Q$ statement.
- §6.3: the note concedes that the local time $T_i$ depends on high Sobolev norms and higher cutoff jets and that curvature-to-volume budgets do not supply these — exactly the Step 53 point. It then substitutes a per-datum start plus positive-time continuation: run the first-exit estimates, whose constants use only unweighted $H_2$, the local Sobolev coefficient, $|d\chi|\lesssim r^{-1}$, initial Ricci defect, and fixed buffers, on $(0,\min\{T_i^*,\theta r^2\})$; if $T_i^*<\theta r^2$, the weighted curvature is finite on $[T_i^*/2,T_i^*)$, the continuation hierarchy gives a smooth endpoint, and the local theorem restarts, contradicting maximality. The logic is not circular: the a priori estimates hold on any existence subinterval with sequence-uniform constants, while the restart uses per-datum (non-uniform) higher bounds; the observation at $t=\theta r^2$ then reads off uniform terminal data. The separation of "per-datum continuation" from "uniform observation" is the correct resolution.

Two derivations are asserted here rather than carried out in the supplied files:

1. **Sequence-uniform first-exit evolution inequalities.** The propagation bounds $(K_2^\eta)'\le C(1+r^{-2})K_2^\eta$, $J_6'+cX_6\le C(1+r^{-2})J_6$, the Moser endpoints (6.8), and the drift bound live in A01 Steps 34–36 and are stated, not reproduced. The single most delicate object is $\nabla^2 a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi$: the uniform-input list in §6.3 contains only $|d\chi|\lesssim r^{-1}$, so every occurrence of $\chi\nabla^2\chi$ must be integrated by parts down to first-order cutoff data for the constants to be independent of the (uncontrolled) second cutoff jet $\nabla^2\chi_i$. Citing a "signed Hessian contraction" does not by itself establish this; the term-by-term integration is the piece to complete.
2. **Continuation/regularity bootstrap for the restart.** The weighted bound $\|aF_T(t)\|_\infty\le C\gamma/t$ is a bound on $a\cdot$curvature, not on curvature itself. On the plateau $\{a=1\}$ this is a genuine curvature bound and Shi-type smoothing gives smooth high derivatives; on $\{a=0\}$ the metric is stationary and smooth; but on the collar $\{0<a<1\}$, where $a$ is small, the passage from the weighted bound and the unweighted $H_2$ energy to bounded high Sobolev norms — needed to reinvoke the local theorem — is not derived. This collar regularity, together with the derivative-smoothing estimates for the specific flow $\partial_t g=-2a(\operatorname{Ric}+g)$, is what makes the "continuation hierarchy (6.9) gives a smooth endpoint" step rigorous.

## 6. The A01 Step 45 §7.2 Liouville patch — the multiplicity concern is removed

I checked the requested passage. The concern in the Step 53 memo was that pulling $\Phi$ back to $T_pM$ by $\exp_p$ and integrating over $T_pM$ overcounts when $\exp_p$ is many-to-one, and that under collapse short geodesic loops could make this overcount diverge.

The patched upper bound never integrates over $T_pM$. Writing $\Phi(\exp_p(t\xi))=\Phi(\pi(\varphi_t(p,\xi)))$ with $\varphi_t$ the geodesic flow on $SM$ and $d\Lambda=d\mu(p)\,d\xi$ the local product form of Liouville measure, the average (7.2) integrated over $P_i^{\rm in}$ becomes, using $c_0t^3\le J_p\le C_0t^3$ for the denominator bound,
$$
\int_{P_i^{\rm in}}A_\rho\Phi_i\,d\mu
\le C(K,\rho)\rho^{-4}\int_0^\rho t^3\!\int_{SM|_{P_i^{\rm in}}}\Phi_i(\pi\circ\varphi_t(v))\,d\Lambda(v)\,dt .
$$
For each fixed $t$, $\varphi_t:SM\to SM$ is a measure-preserving diffeomorphism (Liouville's theorem), so $\varphi_t(SM|_{P_i^{\rm in}})\subseteq SM$ and, by $\Phi\ge0$,
$$
\int_{SM|_{P_i^{\rm in}}}\Phi_i(\pi\circ\varphi_t(v))\,d\Lambda(v)
\le\int_{SM}\Phi_i(\pi(v))\,d\Lambda(v)=\omega_3\int_{M_i}\Phi_i\,d\mu ,
$$
giving (7.3). Because the transport is a measure-preserving bijection of $SM$, there is no overcounting: injectivity of $\exp_p$ is never used. This is a correct fix.

The lower-bound direction (7.4a) does use the pullback ball $B_\rho(0)\subset T_{p_i}M$ with $\exp_{p_i}^*g$, but that is legitimate: for $\rho$ below the conjugate radius (guaranteed by $|\operatorname{Rm}|\le K$ and small $\rho\le r/2$), $\exp_{p_i}$ is a local diffeomorphism, so $\exp_{p_i}^*g$ is a smooth metric with pulled-back curvature $\le K$, and $J_p\ge c_0t^3$ gives $\operatorname{Vol}(B_{\rho/2}(0),\exp_{p_i}^*g)\ge v_0>0$ — noncollapse on the tangent-space pullback, which "unwraps" any base collapse. Proposition 3.2 then applies to the pullback ball. Upper bound (Liouville, no multiplicity) and lower bound (pullback ball, unwrapped noncollapse) are mutually consistent, and the final combination $\eta'\operatorname{Vol}(P_i^{\rm in})\le 119\,C(K,\rho)Q_i(T)$ with $\operatorname{Vol}(P_i^{\rm in})\ge c'\alpha_0A_i$ and $Q_i(T)/A_i\to0$ closes the contradiction. The multiplicity concern is genuinely resolved.

One dependency worth stating: the Rauch two-sided Jacobian bound $c_0t^3\le J_p\le C_0t^3$ requires the geodesics $\exp_p(t\xi)$, $t\le\rho$, to stay inside the bounded-curvature plateau and to reach no conjugate point; both are supplied by the geodesic-buffer condition of §6.4 and $\rho\le r/2$. That geodesic buffer in turn depends on the terminal chart properties, which depend on the first-exit estimates of item 1 above.

## 7. Mathematical work remaining before the restricted theorem is end-to-end

1. Term-by-term sequence-uniform first-exit evolution inequalities (A01 Steps 34–36), with explicit integration by parts of $\chi\nabla^2\chi$ so that constants depend only on $|d\chi|\lesssim r^{-1}$ and sequence-uniform curvature-to-volume data.
2. The continuation/regularity bootstrap that turns the weighted curvature bound at a terminal slab into a smooth restart, resolving collar regularity for $\partial_t g=-2a(\operatorname{Ric}+g)$; this is the analytic content behind (6.9).
3. Fixed-$(\varepsilon,\nu)$ existence and continuation for the coupled parabolic system, via an approximation preserving metric positivity, the transport commutator structure, and the maximum principle (1.3).
4. Term-by-term verification of the DeTurck tensors $R(G,G),\,Q(G,DG)$ and identity (1.3) at every order (standard, asserted).
5. Independent checking of the topological/local core: the mixed Seiberg–Witten averaged estimate (2.1)–(2.5), the calibrated profiles and algebra (2.9)–(2.12) including the numerical constants $4Q,108Q,6Q,119Q$, Derdziński Proposition 3.1, and the elliptic upgrade in Proposition 3.2 (the strong $W^{2,p}$ convergence driven by the $|E|^2$ component of $\Phi$). The elliptic upgrade in 3.2 reads correctly; the calibration constants deserve a separate recomputation.

Two evidential notes. The `verify_step55_direct_construction.py` script carries no weight for any of the PDE substance above: 18 of its 22 checks are hard-coded `True`, and the four computed ones are arithmetic ($r>n/2$, $2p-n=0$). Its check #12, "Q-type antisymmetric IBP identity" $\int h\,A\,Dh=-\tfrac12\int|h|^2DA$, is not valid for tensor/matrix coefficients $A$; the Step 55 and Step 56 texts correctly replaced that identity by weighted Young/Cauchy–Schwarz, so the script line is stale relative to the notes it purports to verify. Step 56 adds no numerical artifact of its own.

## 8. Extent of coverage

Even with items 1–5 completed, the resulting statement is the family-uniform $\operatorname{Ric}\approx-g$ Ishida–LeBrun no-Einstein geography in dimension four: it does not touch the $\operatorname{Ric}\approx+g$ branch (where the Ozuch chirality obstruction has the bi-Kähler loophole noted in the A01 record), arbitrary four-manifold topology, dimensions $n\ge5$, the dimension-only pinching constants $c_n<C_n$ demanded by Problem 26, or the Lean 4 formalization. Step 56 states this coverage plainly in its §7 and should continue to be read as a per-datum smoothing module feeding one branch of a four-dimensional argument, not as a resolution of the full problem.