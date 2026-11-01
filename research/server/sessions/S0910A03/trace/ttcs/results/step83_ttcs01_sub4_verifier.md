# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/trace/ttcs/results/step82_ttcs02_verifier1_integration.md",
    "Sessions/S0910A03/workspace/data/step83_integrating_factor.json"
  ]
}
```

## Task

Verify the following claim for the OT reflected-center K-production. The quantities are: g=dr²+q_r Gaussian, dμ=e^a ρ dz, x=⟨u⟩_μ, y=⟨v⟩_μ, K=⟨e-h²⟩_μ, μ(r)=exp(2∫₀ʳ x ds). The K-production equation is K'+2xK = Φ where Φ = -2⟨τ,b⟩ + 2⟨vc⟩ + Cov(v-u,k). Eliminating τ via the orbit equation ∇_r b + Hb + τ = -ε (traceless orbit defect |ε|≤Cδ) and expanding vc via Codazzi gives: Φ = [d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩ + Cov(H,|b|²)] + [⟨h²(v-2u)⟩] + [⟨h⟨A,b⟩_H²⟩] + [Cov(v-u,k)] + [2⟨ε,b⟩ + 2⟨hE_rs⟩]. CLAIM 1: The μ-weighted integral satisfies ∫₀ᴿ μ[d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩] dr = μ(R)⟨|b|²⟩(R) + ∫₀ᴿ 2yμ⟨|b|²⟩ dr, which is non-negative when y≥0 throughout [0,R]. The proof: μ'=2xμ, so d/dr(μf)=μ(f'+2xf); integrating gives ∫μ(f'+2xf)dr = [μf]₀ᴿ; the remaining 2yf term adds the second integral. CLAIM 2: The circle-geometry term ⟨h²(v-2u)⟩≥0 whenever v≥0 and u≤0 pointwise. CLAIM 3: Only Cov(v-u,k) and ⟨h⟨A,b⟩⟩ can be negative. For a connector that lowers K from 12 to ≤6+2δ, the integrating-factor equation K(R)=μ(R)⁻¹[12+∫₀ᴿ μΦ dr] requires ∫₀ᴿ μΦ dr ≤-6+2δ. Given the non-negative contributions, the covariance/tension terms must supply at least -18 units of μ-weighted production. Check every step: signs, the IBP identity, hypothesis validity (is y≥0 and u≤0 guaranteed before return?), whether Cov(H,|b|²) belongs with the positive or indefinite group, and whether the ≥-18 budget is correctly computed.

## Output

## Verification memo: Step-82/83 K-production endpoint identity and the "−18" budget

I recomputed the algebra of the three statements and the integrating-factor accounting from the equations given in `step82_..._verifier1_integration.md` and the numbers in `step83_integrating_factor.json`. The exact identities check out; the sign accounting and the "−18" figure rest on several unproven sign hypotheses, one term is mis-filed, and the stored numerical figures do not follow cleanly from the exact endpoint identity. Details below.

---

### 1. Statement 1 (the IBP identity) — algebra correct, but one term is mis-filed

With $f=\langle|b|^2\rangle$ and $\mu'=2x\mu$,
$$\mu\big(f'+2(x+y)f\big)=(\mu f)'+2y\mu f,\qquad \int_0^R(\mu f)'\,dr=\mu(R)f(R)-\mu(0)f(0).$$
At the reflected center $b(0)=0\Rightarrow f(0)=0$, $\mu(0)=1$, so
$$\int_0^R\mu\big[\tfrac{d}{dr}\langle|b|^2\rangle+2(x+y)\langle|b|^2\rangle\big]\,dr=\mu(R)\langle|b|^2\rangle(R)+\int_0^R 2y\,\mu\langle|b|^2\rangle\,dr.$$
The identity is exact and its two terms are $\ge0$ **when $y\ge0$ throughout $[0,R]$**. Two things must be separated out.

**(a) The residual $\operatorname{Cov}(H,|b|^2)$ is indefinite and does not belong in this group.** Eliminating $\tau$ from $\nabla_r b+Hb+\tau=-\varepsilon$ gives, pointwise,
$$-2\langle\tau,b\rangle=\langle\partial_r|b|^2\rangle+2\langle H|b|^2\rangle+2\langle\varepsilon,b\rangle.$$
Converting the pointwise radial derivative to the moving average via $\langle\partial_r|b|^2\rangle=\tfrac{d}{dr}\langle|b|^2\rangle-\operatorname{Cov}(H,|b|^2)$ and $2\langle H|b|^2\rangle=2(x+y)\langle|b|^2\rangle+2\operatorname{Cov}(H,|b|^2)$ yields a **net $+\operatorname{Cov}(H,|b|^2)$**:
$$-2\langle\tau,b\rangle=\tfrac{d}{dr}\langle|b|^2\rangle+2(x+y)\langle|b|^2\rangle+\operatorname{Cov}(H,|b|^2)+2\langle\varepsilon,b\rangle.$$
The IBP of Statement 1 covers only the first two terms. $\operatorname{Cov}(H,|b|^2)$ is genuinely sign-indefinite and cannot be absorbed into the non-negative pile. The task's first bracket and the `sign_structure` entry `"Phi_orbit": "NON-NEGATIVE after mu-weighting (proven by IBP)"` therefore overstate what the IBP proves: $\operatorname{Cov}(H,|b|^2)$ must be moved to the indefinite group. Its size is $\lesssim (\text{fluctuation of }H)\cdot(\text{fluctuation of }|b|^2)$, which grows with geometric amplitude, so it is not a small correction in the regime the budget forces.

**(b) $y\ge0$ throughout is not established.** Near the center $y=6r+O(r^3)>0$, and $y'(0)=6$, but nothing forces $y\ge0$ over a full connector; $y'=6-\langle E_{\rm orb}\rangle-y(x+y)$ permits $y$ to dip. If $y<0$ on part of $[0,R]$, the term $\int 2y\mu\langle|b|^2\rangle\,dr$ contributes **negatively** — i.e. mean orbit contraction would itself lower $K$. This is exactly the regime that would assist reversal, so treating the orbit term as an obstacle to reversal presumes away the configuration most favorable to reversal.

---

### 2. Statement 2 (circle term) — pointwise sign correct, hypothesis generically unmet

The Codazzi expansion is reproduced exactly:
$$2\langle vc\rangle=\langle h^2(v-2u)\rangle+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle+2\langle hE_{rs}\rangle,$$
using $D_sv=h(u-\tfrac v2)-\tfrac12\langle A,b\rangle-E_{rs}$ and $\langle hD_sv\rangle=-\langle vc\rangle$. Pointwise $v-2u\ge0$ whenever $v\ge0$ and $u\le0$, and $h^2\ge0$, so $\langle h^2(v-2u)\rangle\ge0$ under those hypotheses — algebraically correct.

The hypothesis is the weak point. $u\le0$ **and** $v\ge0$ are required **pointwise in $z$**, not on the averages $x=\langle u\rangle$, $y=\langle v\rangle$. A connector with $x<0,\ y>0$ generically has $u$ and $v$ of both signs across the slice; the fiber-area log-derivative $v=\sigma_r$ and $u=a_r$ are not sign-definite functions. So $\langle h^2(v-2u)\rangle$ is generically indefinite as well, and the `"Phi_circle": "NON-NEGATIVE when u<=0,v>=0 pointwise"` label, while literally true, describes a configuration that is not shown to occur and is not implied by the mean signs.

---

### 3. The endpoint identity and the "−6 / −12 / −18" accounting

The integrating factor gives the exact, model-independent relation
$$K(R)=\mu(R)^{-1}\Big[12+\int_0^R\mu\Phi\,dr\Big],\qquad \int_0^R\mu\Phi\,dr=\mu(R)K(R)-12.$$
For $K(R)\le6+2\delta$,
$$\int_0^R\mu\Phi\,dr\le \mu(R)(6+2\delta)-12.$$
If $x\le0$ on $[0,R]$ then $\mu(R)\le1$, so the right side is $\le -6+2\delta$: **the task's "$\int\mu\Phi\le-6+2\delta$" is a valid necessary condition, but it is the weakest form.** The sharp form is $\mu(R)(6+2\delta)-12$. For an expanding tail, $x\approx-3r$ makes $\mu(R)=e^{-3R^2+\dots}\to0$, so the necessary condition tightens to
$$\int_0^\infty\mu\Phi\,dr\le -12.$$
The "−18" then arises as $-12-6.33$: the late-window indefinite production must be $\le-18.33$ **provided** the early window contributes $+6.33$ and the late orbit + circle terms are $\ge0$. Both provisos are the conditional non-negativities of §1–§2 (plus the mis-filed $\operatorname{Cov}(H,|b|^2)$). Hence the "−18" is arithmetically consistent with the model's assumptions but is **not a proven lower bound on the indefinite terms** — if $y<0$ anywhere, or if $u,v$ change sign pointwise, or once $\operatorname{Cov}(H,|b|^2)$ is counted honestly, the orbit/circle contributions can themselves be negative and reduce the burden on $\operatorname{Cov}(v-u,k)$ and the tension term. As stated it does not close as an obstruction to reversal.

Two further points on the quantitative figures:

- **Amplitude figure is self-referential.** $C_{\min}=162.4$ uses $\mu\approx e^{-3r^2}$ for the *entire* late window (tail $\int_{0.5}^\infty e^{-3r^2}dr=0.1129$, which I confirm: $\tfrac12\sqrt{\pi/3}\,\mathrm{erfc}(\sqrt3/2)\approx0.112$). But $\mu\approx e^{-3r^2}$ is precisely the center-model contraction that a reversing connector must leave; if the connector reverses, $x\to0$, $\mu$ decays far more slowly, the late weight is much larger, and the required negative rate drops well below 162. So the "162" is computed inside the regime whose escape is the whole question; it is a model extrapolation, not an amplitude that a connector is forced to reach.

- **Force term is not uniformly small in this regime.** $2\langle\varepsilon,b\rangle+2\langle hE_{rs}\rangle$ is $O(\delta\cdot\text{amplitude})$. If the budget forces geometric amplitude of order $10^2$, the force term is $O(10^2\delta)$, i.e. $O(1)$ for moderate $\delta$. The json's own `weyl_consequence`/`forcing amplification scales as delta*(geometric amplitude)` captures this; it means the accounting does not separate cleanly into "small forcing + large geometry" at fixed $\delta$.

---

### 4. A numerical inconsistency to reconcile

The exact identity forces $\int_0^R\mu\Phi=\mu(R)K(R)-12$. With the stored center-model parameters (`K2`=$K''(0)=104$, `tau2`=16, `Var_k`=0, and $x=-3r-5.667r^3$ giving $\mu=\exp(-3r^2-2.83r^4)$):

- Near the center $\Phi=K'+2xK\approx 32r-312r^3$, which **changes sign at $r\approx0.32$**, inside $[0,0.5]$. So $\int_0^{0.5}\mu\Phi$ is not a clean positive quantity.
- The endpoint evaluation gives $\mu(0.5)K(0.5)-12\approx 0.40\cdot(12+13)-12\approx -2$, i.e. slightly negative, **not $+6.33$**.

The stored `early_positive_production = 6.331` therefore does not equal the exact endpoint value with these parameters. This is consistent with the reported `max_error_dmuK_vs_muPhi = 0.697` (r<0.5): the model's $\Phi$ and $K$ do not satisfy $(\mu K)'=\mu\Phi$ to better than $\sim0.7$ pointwise, so integrating the model $\Phi$ separately drifts from the exact endpoint value. The clean way to fix the budget is to compute the early contribution as the **exact** $\mu(R)K(R)-12$ from the universal jet ($K(r)=12+\tfrac12 K''(0)r^2+\dots$, $K''(0)\ge72$) rather than by numerically integrating a model $\Phi$ that violates the identity at the $0.7$ level. Doing so will change the "+6.33" input and hence the "−18" figure. I recommend recomputing both from the endpoint identity and reporting the residual of the identity check as a genuine accuracy figure rather than treating $+6.33$ as established.

---

### 5. What would turn this into an obstruction

The robust, hypothesis-free content that survives:

1. $K(0)=12$, $K'(0)=0$, $K''(0)\ge72$ (verified in the companion memo) — $K$ **rises** initially, $K(r)\ge12+36r^2+O(r^4)$; and $x(r)\le-3r-3r^3$.
2. The exact ledger $\Phi=\underbrace{\big[\tfrac{d}{dr}\langle|b|^2\rangle+2(x+y)\langle|b|^2\rangle\big]}_{\text{IBP-signed under }y\ge0}+\underbrace{\operatorname{Cov}(H,|b|^2)}_{\text{indefinite}}+\underbrace{\langle h^2(v-2u)\rangle}_{\text{signed only under pointwise }u\le0,v\ge0}+\underbrace{\langle h\langle A,b\rangle\rangle+\operatorname{Cov}(v-u,k)}_{\text{indefinite}}+\underbrace{2\langle\varepsilon,b\rangle+2\langle hE_{rs}\rangle}_{O(\delta\cdot\text{amplitude})}.$

To make the "the indefinite terms must supply $\le-18$" step into an obstruction, one needs either (i) an unconditional lower bound $\int_0^R\mu\,\operatorname{Cov}(H,|b|^2)\,dr\ge -(\text{small})$ and $\int_0^R\mu\langle h^2(v-2u)\rangle\,dr\ge0$ that does **not** assume pointwise $u\le0,v\ge0$ or global $y\ge0$; or (ii) a coercive bound relating the negative parts of $\operatorname{Cov}(v-u,k)$ and $\langle h\langle A,b\rangle\rangle$ to $\langle|b|^2\rangle$ and $\langle h^2\rangle$ that is *tighter* than what the $O(\delta\cdot\text{amplitude})$ force term permits at fixed $\delta$. Absent one of these, the endpoint identity organizes the production but does not yet forbid the drop from $12$ to $6$. This matches the note's own §8 statement that the outcome is an open theorem/construction fork.

**Net:** IBP identity (Statement 1) exact; circle pointwise inequality (Statement 2) exact; endpoint accounting reproduces "$\le-6+2\delta$" as a weak necessary condition and "$\le-12$" as the sharp expanding-tail version. The "$-18$" and "$162$" figures are internally consistent with the model but rest on (a) mis-filing $\operatorname{Cov}(H,|b|^2)$ as non-negative, (b) unestablished $y\ge0$ throughout, (c) unestablished pointwise $u\le0,v\ge0$, (d) an extrapolated center-model $\mu$, and (e) a model $\Phi$ that satisfies the exact identity only to $\sim0.7$. Recompute the early contribution from the exact jet-based endpoint value, count $\operatorname{Cov}(H,|b|^2)$ among the indefinite terms, and state the two conditional non-negativities explicitly before using the budget.