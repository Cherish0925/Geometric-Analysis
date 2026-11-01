# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/originals/0911_3104__Smoothing_Riemannian_Metrics_with_Bounded_Ricci_Curvatures_in_Dimens.pdf",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Read Ye Li's actual paper and the Step 13 smoothing note in light of the Strategist correction. Reconstruct rigorously the source-based estimate for the normalized Einstein defect E=Ric+g under normalized Ricci flow, focusing on Corollary 3.5. Determine the correct scaling, Sobolev constant A and volume cancellation, the subsolution inequality for u=(|E|^2+eta)^{1/2}, normalized-vs-unnormalized flow conversion, and exactly which global/local all-centers, evolving curvature-energy, cutoff, metric-equivalence, and boundary hypotheses are needed. Explicitly identify any source typographical ambiguity such as the cutoff phi^2 in Cor. 3.5. Assess whether one can obtain |E(x,t)| <= C delta (r^2/t)^(2/3) uniformly on an interior ball and metric drift O(delta r^(4/3)t^(1/3)); do not assume the flawed Step 13 inner/outer Gronwall. Give a direct mathematical memo with derivations and a precise conditional lemma.

## Output

# Verification Memo: Source-based reconstruction of the Einstein-defect estimate via Ye Li's Corollary 3.5

## 1. Summary of what holds and what remains open

Working directly from Ye Li's paper (the attached PDF, Cor. 3.5 on p. 12 and its use on p. 14) rather than from the Step 13 Sobolev-absorption construction, the target estimate

$$|E(x,t)| \le C^\*\,\delta\,(r^2/t)^{2/3},\qquad E:=\operatorname{Ric}(g)+g,$$

and the metric drift $O(\delta\,r^{4/3}t^{1/3})$ are both **correct and reconstructible as a single clean application of Corollary 3.5** to $u=(|E|^2+\eta)^{1/2}$. The volume cancels exactly, the constant is genuinely uniform (depends only on $n=4$, the Ricci bound $K$, and Li's dimensional constants), and the derivation does **not** use the flawed inner/outer Gronwall of Step 13 §4. That entire §4 is, in effect, a hand re-derivation of what Corollary 3.5 already packages; the direct route is sharper and its scaling is transparent.

Three matters need explicit handling, listed here and detailed below:

- a source typographical artifact ($\phi^2$ in the Cor. 3.5 hypothesis, and $\phi^2\Delta|\mathrm{Rm}|^2$ on p. 13) that must be read as absent;
- the normalized-vs-unnormalized flow conversion, which is a bounded rescaling on an $O(r^2)$ interval and is harmless;
- the one genuinely external analytic input: local short-time existence of the flow with the $C/t$ interior curvature bound on a ball in the **collapsing** regime, since Li's Theorem 3.1 as written is a global (all-of-$M$) statement.

A separate structural point (§9) is that the raw band hypothesis $c_ng\le\operatorname{Ric}\le C_ng$ does **not** by itself make $\delta=|\operatorname{Ric}+g|$ small; the propagation lemma is only informative when fed a genuinely small-defect input, which must come from elsewhere.

## 2. The $\phi^2$ artifact in Corollary 3.5

Corollary 3.5 states the hypothesis as
$$\frac{\partial u}{\partial t}\le \phi^2(\Delta u + c_0 f u).$$
The $\phi^2$ prefactor cannot be part of the intended pointwise differential inequality: $\phi$ is the compactly supported cutoff used only inside the integral (Moser) estimates, and the same spurious $\phi^2$ appears on p. 13 in
$$\tfrac{\partial}{\partial t}|\mathrm{Rm}|^2=\phi^2\Delta|\mathrm{Rm}|^2-2|\nabla\mathrm{Rm}|^2+\mathrm{Rm}*\mathrm{Rm}*\mathrm{Rm},$$
where the correct Ricci-flow evolution has no $\phi^2$ in front of $\Delta$. The intended reading of the Cor. 3.5 hypothesis is the honest subsolution inequality
$$\boxed{\ \partial_t u \le \Delta u + c_0\, f\, u\ }$$
with $f$ satisfying the assumptions of Theorem 3.4 ($\partial_t f\le\Delta f+C_0f^2$, small initial $L^2$ energy, $\partial_t\,dV\le c f\,dV$). This is exactly how Li himself uses it on p. 14 to bound $|\operatorname{Ric}(g(t))|$. The reconstruction below uses this corrected hypothesis.

## 3. The subsolution for $u=(|E|^2+\eta)^{1/2}$ (Kato reduction)

Take the verified squared-norm evolution (confirmed independently in the Step 13 verifier integration):
$$(\partial_t-\Delta)|E|^2=-2|\nabla E|^2+4R_{ikjl}E_{ij}E_{kl}\le -2|\nabla E|^2+4|\mathrm{Rm}|\,|E|^2 .$$
Set $w=|E|^2$, $u=(w+\eta)^{1/2}$, $\eta>0$. Then $\partial_t u=\dfrac{\partial_t w}{2u}$, $\Delta u=\dfrac{\Delta w}{2u}-\dfrac{|\nabla w|^2}{4u^3}$, so
$$(\partial_t-\Delta)u=\frac{\partial_t w-\Delta w}{2u}+\frac{|\nabla w|^2}{4u^3}.$$
Kato: $|\nabla w|=|\nabla|E|^2|\le 2|E||\nabla E|$, hence $|\nabla w|^2\le 4w|\nabla E|^2\le 4u^2|\nabla E|^2$, giving $\dfrac{|\nabla w|^2}{4u^3}\le\dfrac{|\nabla E|^2}{u}$. Combining with $\partial_t w-\Delta w\le -2|\nabla E|^2+4|\mathrm{Rm}|w$:
$$(\partial_t-\Delta)u\le \frac{-2|\nabla E|^2+4|\mathrm{Rm}|w}{2u}+\frac{|\nabla E|^2}{u}=\frac{2|\mathrm{Rm}|w}{u}\le 2|\mathrm{Rm}|\,u,$$
since $w/u=w/(w+\eta)^{1/2}\le u$. Therefore
$$\boxed{\ (\partial_t-\Delta)u\le 2|\mathrm{Rm}|\,u\ }$$
i.e. $u$ is a Cor. 3.5 subsolution with $c_0 f=2|\mathrm{Rm}|$, so $f=|\mathrm{Rm}|$, $c_0=2$. The curvature-form condition $\partial_t\,dV=-R\,dV$, $|R|\le C|\mathrm{Rm}|$, matches $\partial_t\,dV\le cf\,dV$ with the same $f=|\mathrm{Rm}|$. Crucially the "$f$" needed for the $E$-estimate is the very same $|\mathrm{Rm}|$ that Li's smoothing controls; no new geometric quantity enters. Let $\eta\downarrow0$ at the end so $u\to|E|$, $u_0\to|E(0)|$.

## 4. Normalized $\leftrightarrow$ unnormalized conversion

Li's Theorem 3.1/3.6 is for the unnormalized flow $\partial_\tau\bar g=-2\operatorname{Ric}(\bar g)$; $E=\operatorname{Ric}+g$ has its clean fixed point $\operatorname{Ric}=-g$ under the normalized flow $\partial_t g=-2(\operatorname{Ric}+g)=-2E$. Put $g(t)=c(t)\,\bar g(\tau(t))$. Since $\operatorname{Ric}(c\bar g)=\operatorname{Ric}(\bar g)$,
$$\partial_t g=c'\bar g-2c\tau'\operatorname{Ric}(\bar g)\stackrel{!}{=}-2\operatorname{Ric}(\bar g)-2c\bar g$$
forces $c\tau'=1$ and $c'=-2c$, i.e.
$$c(t)=e^{-2t},\qquad \tau(t)=\tfrac12(e^{2t}-1).$$
On $[0,t_0]$ with $t_0=C_2r^2\le C_2$ and $r\le1$ small, $c=1+O(r^2)$ and $\tau=t\,(1+O(r^2))$. Hence Li's estimates for $\bar g$ transfer to the normalized $g$ up to bounded factors: $|\mathrm{Rm}(g(t))|_{g(t)}=c^{-1}|\mathrm{Rm}(\bar g(\tau))|_{\bar g}\le C_3/\tau\approx C_3/t$; metric equivalence $\tfrac12 g_0\le g(t)\le 2g_0$; the local Sobolev constant and volume form all change by $1+O(r^2)$. The subsolution of §3 is derived directly on the normalized flow, so the two ingredients (curvature bound via conversion, $E$-subsolution direct) are simultaneously available. No re-derivation of Li's argument for the extra $-2g$ term is required.

## 5. Volume/Sobolev cancellation — the main derivation

Corollary 3.5 (corrected) applied to $u=(|E|^2+\eta)^{1/2}$, for $0<t<\min(T,C_2r^2)$:
$$|u(x,t)|\le C_1\,A^{2/3}\,t^{-2/3}\Big(\int_{B_{3r}(x)}u_0^{3}\Big)^{1/3}.$$

**The Sobolev constant.** The relevant inequality (Li (2.1)) is $\big(\int_{B_r}f^4\big)^{1/2}\le A\int_{B_r}|\nabla f|^2$ for compactly supported $f$. Dimensional matching (LHS $\sim \mathrm{Vol}^{1/2}$, RHS $\sim A\,L^{-2}\mathrm{Vol}$) forces
$$A\;\sim\; \frac{r^2}{\mathrm{Vol}(B_r)^{1/2}},$$
which is exactly Li's stated bound $C_s(B_r)\le C\,(r^4/\mathrm{Vol}(B_r))^{1/2}=C\,r^2/\mathrm{Vol}(B_r)^{1/2}$ (his $A$ and $C_s$ coincide up to a dimensional constant; this is the Saloff-Coste ball Sobolev inequality under a Ricci lower bound). Hence
$$A^{2/3}=C\,\frac{r^{4/3}}{\mathrm{Vol}(B_r)^{1/3}}.$$

**The data term.** With $|E(g_0)|\le\delta$ on $B_{3r}(x)$ (and $\eta\downarrow0$),
$$\Big(\int_{B_{3r}(x)}u_0^3\Big)^{1/3}\le \delta\,\mathrm{Vol}(B_{3r}(x))^{1/3}\le \delta\,C_D^{1/3}\,\mathrm{Vol}(B_r(x))^{1/3},$$
using volume doubling $C_D$ from bounded Ricci.

**Cancellation.** Multiplying,
$$A^{2/3}\Big(\int u_0^3\Big)^{1/3}\le C\,\frac{r^{4/3}}{\mathrm{Vol}(B_r)^{1/3}}\cdot \delta\,C_D^{1/3}\mathrm{Vol}(B_r)^{1/3}=C\,C_D^{1/3}\,\delta\,r^{4/3}.$$
The volume disappears completely. Therefore
$$\boxed{\ |E(x,t)|\le C^\*\,\delta\,r^{4/3}\,t^{-2/3}=C^\*\,\delta\,(r^2/t)^{2/3}\ },\qquad 0<t<\min(T,C_2r^2),$$
with $C^\*=C^\*(n{=}4,K,C_D,\text{Li's constants})$, uniform in the volume and in the sequence index. At $t_0=\theta r^2$ ($\theta\le C_2$): $|E(\cdot,t_0)|\le C^\*\theta^{-2/3}\delta$ on the interior ball, while simultaneously $|\mathrm{Rm}(g(t_0))|\le C_3/t_0\sim C/r^2$.

This confirms the numeric exponent $2/3$ (not from any ad hoc Gronwall) and produces an object with bounded curvature **and** defect $O(\delta)$ on a fixed interior ball. It is the same $\delta$-order as the Step 13 §4.5 assertion, but the derivation is one line of Corollary 3.5 plus the volume cancellation, and the $(r^2/t)^{2/3}$ scaling is explicit.

## 6. Metric drift

Under the normalized flow $\partial_t g=-2E$, $|\partial_t g|_g=2|E|$. Near $t=0$ use $|E(s)|\le 2\delta$ (smooth continuity from $|E(0)|\le\delta$ on the smooth solution); for larger $s$ use §5. Then
$$\int_0^{t}|\partial_s g|\,ds\le \int_0^{t}2\min\!\big(2\delta,\;C^\*\delta (r^2/s)^{2/3}\big)\,ds\le 2C^\*\delta\,r^{4/3}\!\int_0^t s^{-2/3}\,ds=6C^\*\delta\,r^{4/3}t^{1/3}.$$
The integral converges at $s=0$ because the exponent $-2/3>-1$. So the drift is $O(\delta\,r^{4/3}t^{1/3})$, matching the claim; at $t_0\sim r^2$ it is $O(\delta r^2)$, vanishing with $\delta$.

## 7. Conditional Lemma (precise statement)

**Lemma (E-propagation through Li smoothing).** Let $(M^4,g_0)$ be smooth, $p\in M$, $r_0\in(0,1]$. Suppose:

- **(H1) energy:** $r_0^4\,\fint_{B_{r_0}(y)}|\mathrm{Rm}(g_0)|^2\le \varepsilon_{Li}$ for every center $y\in B_{3r_0}(p)$;
- **(H2) Ricci:** $|\operatorname{Ric}(g_0)|\le K$;
- **(H3) defect:** $|\operatorname{Ric}(g_0)+g_0|\le\delta$ on $B_{3r_0}(p)$;
- **(H4) local flow:** the normalized flow $\partial_t g=-2(\operatorname{Ric}+g)$ exists smoothly on $B_{3r_0}(p)\times[0,t_0]$, $t_0=C_2r_0^2$, with $\tfrac12g_0\le g(t)\le2g_0$, $|\mathrm{Rm}(g(t))|\le C_3/t$, and the uniform Sobolev inequality with $A(t)\le C_A\,r_0^2/\mathrm{Vol}(B_{r_0})^{1/2}$ for interior centers.

Then for $0<t\le t_0$ and $x\in B_{r_0}(p)$,
$$|\operatorname{Ric}(g(t))+g(t)|\le C^\*\,\delta\,(r_0^2/t)^{2/3},\qquad \int_0^t|\partial_s g|\,ds\le C^{\*\*}\delta\,r_0^{4/3}t^{1/3},$$
with $C^\*,C^{\*\*}$ depending only on $n=4$, $K$, and Li's dimensional constants. At $t_0$: $|\operatorname{Ric}(g(t_0))+g(t_0)|\le C^\*\delta$ on $B_{r_0}(p)$ while $|\mathrm{Rm}(g(t_0))|\le C_3/t_0$.

Everything in §§3–6 establishes the conclusion **given (H1)–(H4)**. The only piece not internally produced by Li's own argument is (H4)'s local existence; see §8.

## 8. Which hypotheses are internal to Li, which are external

- **(H1) at a buffered ball is supplied by a single maximal-function bound plus doubling.** If $M_1|\mathrm{Rm}|^2(p)\le K_0$, then $\fint_{B_r(p)}|\mathrm{Rm}|^2\le K_0$ for all $r\le1$; for a nearby center $y\in B_{r_0/2}(p)$, $B_{r_0}(y)\subset B_{3r_0/2}(p)$, so $\fint_{B_{r_0}(y)}|\mathrm{Rm}|^2\le K_0\,\mathrm{Vol}(B_{3r_0/2}(p))/\mathrm{Vol}(B_{r_0}(y))\le K_0 C_D$. Then $r_0^4\fint\le K_0C_D\,r_0^4\le\varepsilon_{Li}$ for $r_0$ small. So the all-centers dimensionless smallness on a buffered ball follows from a *point* bound at $p$; the maximal-function good point is enough to feed (H1) on a genuine ball. This part of the Step 13 §1 calculation is sound.

- **Metric equivalence, uniform Sobolev along the flow, doubling, the $\int|\mathrm{Rm}|^3\le\mu^3/t$ bound (needed so that $f=|\mathrm{Rm}|$ verifies Theorem 3.4), $|\mathrm{Rm}|\le C_3/t$** are all internal to Li's Theorem 3.1 argument (his (3.7)–(3.9) maximality, Hamilton's trick, Corollary 3.5), for a **complete** manifold satisfying (H1) at *every* $x$.

- **The genuinely external input is (H4) as a *local* statement.** Li's Theorem 3.1 needs the small-energy condition at every $x\in$ a *complete* manifold. The maximal-function good set on $M$ is measure-theoretically large but need not be a solid ball; the complement (where curvature concentrates) can be nonempty, so the global condition can break down, and one cannot invoke Li globally. Reducing to a ball $B_{3r_0}(p)$ is not covered by Li's theorem, because Li's construction (short-time existence + $C/t$) explicitly *avoids* the local Ricci flow and instead relies on a complete-manifold covering/maximum-principle argument. Localizing it requires either: (i) imposing Dirichlet/Neumann conditions at the edge of $B_{3r_0}(p)$ and controlling the induced error in the Moser iteration and in Hamilton's trick near the edge; or (ii) returning to the local Ricci flow of Yang [16]/Xu [15]. Both Yang and Xu, however, take a noncollapsing/volume input; the collapsing regime — precisely the case Li handled globally via Cheeger–Tian [7] and Gauss–Bonnet–Chern — is where a purely local short-time flow with an interior $C/t$ bound is not established in the supplied materials. This is the principal unresolved analytic item; it is a real construction to be carried out, not a formality. Note Li's covering only ever references balls $B_{r_0}(y_i)$ with $y_i\in B_{3r_0/2}$ of interior centers, which suggests a buffer of width $\sim 2r_0$ keeps the argument interior — but the edge treatment of the flow itself (not just the covering) is what must be proved.

- The $2/3$-exponent structure additionally requires that $f=|\mathrm{Rm}|$ actually satisfies Theorem 3.4's initial smallness $\big(\int_{B_r}|\mathrm{Rm}(g_0)|^2\big)^{1/2}\le (6C_0A)^{-1}$, i.e. the same $\varepsilon_{Li}$ threshold as (H1). This is consistent: (H1) supplies both the smoothing and the Cor. 3.5 coefficient control simultaneously.

## 9. Structural point on the source of small $\delta$

The propagation is only informative when $\delta$ is genuinely small. The problem's hypothesis $c_ng\le\operatorname{Ric}_g\le C_ng$ is a two-sided *band* with $c_n<C_n$, not pinching. It gives bounded Ricci ($|\operatorname{Ric}|\le\max(|c_n|,|C_n|)$, feeding (H2)), but $|\operatorname{Ric}+g|$ is of order $|C_n-c_n|+|1+\tfrac{c_n+C_n}{2}|$, which is $O(1)$, not small. So feeding the raw band metrics into this Lemma yields $|E(t_0)|\le C^\*\cdot O(1)$ — no Einstein limit follows. The Lemma is a brick whose input $\delta\to0$ must be produced by a separate mechanism (a minimizing/contradiction sequence in which the defect tends to zero, or an independent pinching estimate). The provided materials position it inside a "forbidden-germ" contradiction (Step 13 §5), where presumably a defect-$\to0$ sequence is generated; but that generation, and its compatibility with the collapsing local flow (H4), is exactly what still has to be assembled. It should be stated explicitly that this Lemma consumes small defect rather than producing it from the band.

## 10. Relation to Step 13 §4 (Sobolev absorption / inner–outer Gronwall)

Step 13 §4 derives $\int_{B}|E|^2$ propagation by absorbing $\int|\mathrm{Rm}||\phi E|^2\le\|\mathrm{Rm}\|_{L^2}\|\phi E\|_{L^4}^2$ into the $-2\int|\nabla E|^2$ dissipation via the ball Sobolev inequality, then runs a time-Gronwall $e^{C_3 r_0^{-2}t}$ and a parabolic mean-value inequality. This is exactly the mechanism inside Li's Moser iteration that produces Corollary 3.5. Invoking Cor. 3.5 directly is cleaner: it delivers the pointwise bound with the sharp $(r^2/t)^{2/3}$ scaling and a transparent volume cancellation, whereas the §4 route carries an $e^{C_1C_3/2}$ factor and a less explicit constant. The two reach the same $\delta$-order conclusion; the Cor. 3.5 route is the source-grounded and simpler one. The Step 13 verifier's correction — that the "$-2E$" linear term does not survive as damping in $|E|^2$ — is confirmed and is irrelevant to this route, which never relies on such damping: the smallness comes entirely from $A^{2/3}\cdot\mathrm{Vol}^{1/3}=O(r^{4/3})$ times the small data $\delta$.

## 11. Items to settle to close the brick

1. **Local flow (H4) in the collapsing regime**: a short-time existence with interior $|\mathrm{Rm}|\le C_3/t$ on $B_{3r_0}(p)\times[0,C_2r_0^2]$ under (H1)–(H2) with edge conditions controlled, without a noncollapsing input. This is the substantive missing construction.
2. **Persistence of (H1)-type dimensionless energy along the flow on the ball**, so that $f=|\mathrm{Rm}|$ continues to satisfy Theorem 3.4's smallness for $t\in(0,t_0]$; internal to Li globally, to be re-proved locally.
3. **Source of small $\delta$** (§9), and its compatibility with the local, possibly collapsed, geometry.
4. **Transfer of any calibrated/curvature-profile data** through the interval $[0,t_0]$ (the note's §7.3), if the downstream contradiction uses $W^+$ structure; this needs the $L^2$ evolution of that curvature piece across the $C/t$ layer.

Items 1 and 3 are the ones that determine whether this brick can carry weight in the larger argument; items 2 and 4 are checkable given a local flow. The $E$-propagation estimate itself (§§3–7) is solid and independent of the Step 13 §4 machinery.