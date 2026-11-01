# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step84_preceptor_interval_variational_audit.md",
    "Sessions/S0910A02/workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md",
    "Sessions/S0910A02/workspace/data/step84_interval_variational_audit.json",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Knowledge/objects/papers/Moduli-spaces-of-critical-Riemannian-metrics-in-dimension--4e6975d02959--2513743a9d1b/object.md",
    "Knowledge/objects/papers/Rigidity-and-stability-of-Einstein-metrics-for-quadratic-curvature-funct--84d7f54aa988--cf9608570634/object.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md",
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md"
  ]
}
```

## Task

The active target is Yau Problem 26 as stated in the session: prove or refute the dimension-only Ricci pinching implies Einstein-existence proposition, without changing quantifiers. A new possible instrument was identified in Step 84: on the audited A1 positive and negative mirror mixed rows, the four-dimensional functional F(g)=∫(|W|^2+s^2/24) satisfies F=8π²χ+(1/2)∫|E|², and the near-pinched families show inf F=8π²χ with no energy gap; Einstein existence is exactly attainment of this lower bound. Read the context and develop a scientific memo on whether this F-attainment/concentration-compactness route can be made into a concrete proof or obstruction strategy for the mixed rows. Identify the strongest plausible lemmas, the needed compactness/Palais-Smale/epsilon-regularity inputs, how Anderson/Tian-Viaclovsky/Gursky-Viaclovsky results could and could not be adapted, the main escape mechanisms (collapse, conformal degeneration, noncritical minimizing sequences, bubbling with exact energy saturation), and cheap discriminating calculations or source checks that would most clarify the route. Do not invent literature or claim the route works; give mathematically precise possibilities and failure modes useful for the next core agent.

## Output

## Memo: the F‑attainment route for the mixed rows

### 1. The exact equivalence that makes this route non‑tautological

Fix a mixed row $M^4$ (either mirror family), oriented, $\chi(M)=8$ (positive mirror) or $56$ (genus‑two mirror). On unit‑volume metrics the four‑dimensional identity

$$
F(g)=\int_M\Big(|W_g|^2+\tfrac{s_g^2}{24}\Big)\,dV_g = 8\pi^2\chi(M)+\tfrac12\int_M|E_g|^2\,dV_g,\qquad E=\operatorname{Ric}-\tfrac s4 g,
$$

gives $F\ge 8\pi^2\chi$ always, and the Step 83 near‑pinched families give unit‑volume metrics with $\int|E|^2\to0$. Hence $\inf F=8\pi^2\chi$ is **already established** for these rows. The remaining content is purely attainment, and

$$
\boxed{\;M \text{ carries an Einstein metric of some }\lambda\in\mathbb R\;\Longleftrightarrow\; \inf F=8\pi^2\chi\text{ is attained by a smooth metric on }M.\;}
$$

Proof both ways: attainment $\Rightarrow \int|E|^2=0\Rightarrow E\equiv0\Rightarrow$ (contracted Bianchi, $n=4$, $M$ connected) $s$ constant $\Rightarrow$ Einstein; Einstein $\Rightarrow F=8\pi^2\chi$. This is not the empty statement "F is minimized iff Einstein"; it is the specific fact that for these rows the minimal value is known, so the entire problem is a concrete PDE compactness question, and it is **sign‑neutral**: $F$ does not see the sign of $\lambda=s/4$. A non‑attainment proof would refute existence of Einstein metrics of every sign at once — exactly the "all‑sign" requirement the session identified — and an attainment proof would produce one. This sign‑neutrality is the route's first genuine advantage over the $W^+$‑alignment mechanism, which addressed only $\lambda>0$.

### 2. Identification with the Gursky–Viaclovsky square case

Because $\int|E|^2=\int|\operatorname{Ric}|^2-\tfrac14\int s^2 = \mathcal F_{-1/4}$ in their notation, and $-\tfrac14=-\tfrac1n$ in dimension four,

$$
F = 8\pi^2\chi + \tfrac12\,\mathcal F_{-1/n}.
$$

This lands **exactly** on Gursky–Viaclovsky's distinguished value $\tau=-1/n$ (their Remark 3.11), where the transverse‑traceless Jacobi operator at an Einstein metric is the perfect square $\tfrac12\big(\Delta_L+\tfrac2n R\big)^2\ge0$ with kernel = infinitesimal Einstein deformations. Consequences the next agent should use:

- $\tau=-1/4>\tau_c=-1/3=-n/4(n-1)$, so the gauged operator $P_g$ is elliptic (their Theorem 2.7 applies); this is **not** the degenerate Bach case.
- Exactly‑critical $\mathcal F_{-1/4}$ metrics satisfy $\Delta\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}$ (take trace of their $(\nabla\mathcal F_\tau)'$ formulas, use Bianchi), i.e. Anderson's Prop 3.5 / Tian–Viaclovsky Thm 4.1 form. So the $\varepsilon$‑regularity core transfers to F‑critical metrics **given a Sobolev bound**.
- Einstein metrics are degenerate local minimizers of $F$ (square $\ge0$, nontrivial kernel). There is no strict coercivity near the critical set; any existence attempt via "coercive near critical manifold" is unavailable, and the kernel (Einstein deformations) is the same object that Gursky–Viaclovsky's rigidity theory controls only spectrally.

### 3. What is free, and what Anderson then yields

Along any F‑minimizing sequence $g_i$ (unit volume, $F(g_i)\to8\pi^2\chi$): both $\int|W|^2$ and $\int s^2/24$ are bounded (each nonnegative, sum bounded), hence $\int s^2$ bounded, hence $\int|\operatorname{Ric}|^2=\int|E|^2+\tfrac14\int s^2$ bounded, hence $\int|\mathrm{Rm}|^2\le\Lambda$ with $\Lambda$ a fixed topological constant. This is precisely Anderson's $\int|R|^{n/2}\le\Lambda$ hypothesis, and scale invariance supplies $\mathrm{Vol}=1$. **Two hypotheses are not free:** the noncollapse volume ratio (1.4) and the small‑curvature estimate (1.5).

The important structural point about Anderson's conclusion: even with all hypotheses, the theorem produces an **orbifold** limit, not attainment on $M$. Applied to the Step 83 minimizing sequence it would return the fixed Einstein orbifold $\mathcal O=(S^2\times S^2)/\mathbb Z_2$ (with four $A_1$ points) plus Eguchi–Hanson bubbles — i.e. it certifies **non‑attainment along the natural sequence**, not existence. Tian–Viaclovsky, with $b_1(M)=0$, sharpens the possible limit to a single irreducible orbifold with cyclic (A‑type) singular points and ALE bubbles (their Prop 7.2, conclusion (4)), matching Anderson/Bando/BKN exactly. So all cited compactness theorems, if fully applicable, describe the degeneration; none of them delivers a smooth Einstein minimizer.

### 4. Why concentration‑compactness produces no gap

The Step 84 energy ledger is exact:

$$
\underbrace{8\pi^2\chi_{\mathrm{orb}}}_{16\pi^2}+\ 4\cdot\underbrace{8\pi^2\big(\chi_{EH}-\tfrac1{|\Gamma|}\big)}_{12\pi^2}=64\pi^2=8\pi^2\chi(M),
$$

and $8\pi^2(\chi_{EH}-1/|\Gamma|)=8\pi^2(2-\tfrac12)$ is the Ricci‑flat ALE Gauss–Bonnet defect (each bubble carries only $\int|W|^2$, since $E=s=0$). The standard concentration‑compactness dichotomy — compactness unless a bubble carries a fixed energy quantum, and compactness forced when the residual budget is below one quantum — **does not close here** because the bubble quantum ($12\pi^2$ per $A_1$) fits the budget with no remainder. There is no "not enough energy for a bubble" contradiction. This is the precise analytic content of "purely integral lower bounds leave slack."

### 5. The three escape mechanisms, precisely

**(a) Bubbling with exact saturation (the natural degeneration).** The minimizing sequence approaches $\mathcal O$ + four Ricci‑flat ALE bubbles. Attainment on $M$ then requires the orbifold itself to admit an *exact* Einstein desingularization — this is the Biquard/Ozuch first‑order obstruction, a quadratic expression in the ambient $W^\pm$ at each node paired against the bubble's self‑dual/anti‑self‑dual constant form. **The F‑route does not bypass this obstruction; it repackages it as a global attainment question.** Its only added leverage is that non‑attainment, if proved, is sign‑neutral.

**(b) Collapse / partial collapse.** $F$ is scale invariant, so unit volume does not prevent injectivity radius $\to0$. Anderson and Tian–Viaclovsky both require noncollapse and both list collapse as unresolved (TV open problem 3). Step 79's transition‑scale theorem shows collapse is live for near‑Einstein sequences. But a *pure* bounded‑curvature collapse over the whole $M$ forces an F‑structure and $\chi=0$; since $\chi(M)=8\ne0$, collapse must be **partial**: a possibly collapsed base carrying $\chi=0$ plus noncollapsed Ricci‑flat atoms (ALE/ALF/ALG/ALH) carrying the full $\chi=8$ and the full $64\pi^2$. This merges with (a) into a single object: a Ricci‑flat bubble tree of total $\chi=8$, total $F=64\pi^2$, over an Einstein/RCD base. Deciding attainment = deciding whether any such tree assembles into a smooth Einstein metric on $M$. Step 79's ALE‑exclusion (the $|\Gamma|\ge1/\varepsilon$ vs. $E_7$ energy budget, and the chiral refinement) constrains but does not eliminate the atoms.

**(c) Noncritical almost‑minimizers (the true analytic gap).** Ekeland selection gives $g_i$ with $F(g_i)\to\inf$ and $\|\nabla F(g_i)\|\to0$, i.e. $\Delta\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}+\eta_i$. The $\varepsilon$‑regularity of Anderson/TV is for $\eta_i\equiv0$; it is stable under $\eta_i$ small in $L^p$, $p>n/2$, but Ekeland only controls $\eta_i$ in a dual (roughly $H^{-2}$) norm, which is too weak for the pointwise/$L^p$ estimate. **This is where the route is genuinely unfinished as PDE.** A concrete fix worth pursuing: use the $L^2$ gradient flow of $\mathcal F_{-1/4}$ (Streets/Bour fourth‑order flow, cited in Gursky–Viaclovsky) to generate the minimizing sequence with a priori $L^p$ curvature control, then feed it into Anderson/TV compactness. The needed new statement is a *quantitative almost‑critical $\varepsilon$‑regularity*: $F(g)\le64\pi^2+\delta$ and $\|\nabla F(g)\|_{L^p}\le\delta$ with small $\int_{B_r}|\mathrm{Rm}|^2$ and controlled local Sobolev $\Rightarrow$ $r^2\|\mathrm{Rm}\|_{L^p(B_{r/2})}\le C$.

### 6. What Anderson/TV/GV can and cannot be made to do

- **Anderson 1.1/1.2:** transfers the $\varepsilon$‑regularity and ALE‑characterization if (i) $\int|\mathrm{Rm}|^2$ bounded (free), (ii) noncollapse holds, (iii) the metric satisfies $D^*D\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}$ up to a small $L^p$ error. Gives orbifold limit, i.e. non‑attainment certificate along a sequence — not existence.
- **Tian–Viaclovsky:** their engine (§5–7) uses only $\Delta\operatorname{Ric}=\mathrm{Rm}*\operatorname{Ric}$, a Sobolev bound, $\int|\mathrm{Rm}|^2\le\Lambda$, and $b_1<B_1$; all are compatible with F‑critical metrics. But the paper never states this for $\mathcal F_\tau$; §5–7 must be re‑derived for $\tau=-1/4$ almost‑critical metrics. With $b_1=0$ their multi‑fold collapses to a single irreducible orbifold — favorable.
- **Gursky–Viaclovsky:** supplies only local behavior — degenerate stability of Einstein metrics as F‑minimizers, and (Thm 1.12, $\tau>-n/4(n-1)$ with integrable Einstein deformations) local minimization in the Ricci‑flat case relevant to the $\lambda=0$ leg. It gives no global compactness and cannot decide attainment.

### 7. The structural barrier the route cannot dodge, and the one it can

$\inf F=8\pi^2\chi$ is diffeomorphism‑blind: every mixed row with the same $\chi$ has the same minimal energy, yet Einstein existence is smooth‑structure sensitive (LeBrun's Seiberg–Witten $\int s^2$, $\int|W^+|^2$ lower bounds distinguish diffeo types with equal $\chi,\tau$). Therefore **any obstruction extracted from the F‑route must import a smooth‑structure invariant as an a priori lower bound on minimizing sequences.** On these rows the monopole invariants are void (session record), so this input is absent — which is precisely why the rows are hard and why no F‑route obstruction is currently visible. The advantage that survives is sign‑neutrality: a single attainment analysis covers $\lambda>0$, $\lambda=0$, and $\lambda<0$ simultaneously, including the $\lambda<0$ leg that had no other known handle.

### 8. Cheapest discriminating calculations and source checks, prioritized

1. **Biquard/Ozuch obstruction on the homogeneous orbifold (decisive, closed form).** Compute the eigenvalues of $W^+$ and $W^-$ for the equal‑radius $S^2\times S^2$ Einstein metric at a fixed point (homogeneous, one point suffices; $\tau=0\Rightarrow|W^+|^2=|W^-|^2>0$), then evaluate the first‑order $A_1$/Eguchi–Hanson desingularization obstruction (the quadratic contraction of the ambient $W^\pm(p)$ with the bubble's constant self‑dual form) for each of the four nodes and both chirality markings. If it is nonzero for all markings, the Einstein desingularization *near the orbifold* is obstructed and F‑attainment along that stratum is excluded; the residual question becomes an Einstein metric far from $\mathcal O$, which the F‑route cannot reach. Repeat for the genus‑two mirror ($\Sigma_2\times\Sigma_2$, curvature $-1$ each, $\mathrm{Ric}=-g$, 36 nodes). This is a few lines of homogeneous linear algebra plus reading Biquard/Ozuch's coefficient.

2. **Second‑order defect of the optimal near‑pinched family.** From the Step 83 expansion, determine whether the smallest achievable $\int|E|^2$ over the family behaves like $c/|\log a|^2$ with $c>0$ bounded below, and whether $c$ is a fixed sign. A strictly positive floor for the *steepest* family, together with a moduli‑uniqueness input, is the shape of a non‑attainment argument; a sign change would indicate descent onto $M$ is possible.

3. **Yamabe positivity and Sobolev control.** Check that the mixed rows ($2\mathbb{CP}^2\#4\overline{\mathbb{CP}}{}^2$, $\#_3(S^2\times S^2)$, etc.) have positive Yamabe invariant (rational‑surface / connected‑sum‑with‑$\mathbb{CP}^2$ Yamabe positivity via Gromov–Lawson/Schoen–Yau surgery). Positive Yamabe supplies the Sobolev bound (Anderson Lemma 3.1, TV Prop 3.1) on Yamabe representatives. Note the reduction: minimizing $F$ first within conformal classes replaces $\int s^2/24$ by its conformal minimum while leaving $\int|W|^2$ fixed; this yields a CSC/Yamabe representative and a Sobolev bound **but does not prevent collapse of non‑Yamabe minimizing sequences**, so it closes noncollapse only conditionally.

4. **Atom‑table energy accounting for the collapse escape.** Tabulate $\int|W|^2$ and $(\chi,\tau)$ for candidate Ricci‑flat ALF/ALG/ALH atoms and check which multisets satisfy total $F=64\pi^2$, total $\chi=8$, total $\tau=\tau(M)$ with APS $\eta$ corrections. Combined with Step 79's ALE energy exclusion this bounds the possible degenerations.

5. **Monopole/Bauer–Furuta re‑check.** Confirm the monopole‑voidness of each mixed row and test whether any refined ($\mathrm{Pin}$‑equivariant/Bauer–Furuta) invariant gives a nonzero lower bound on $\int s^2$ or $\int|W^+|^2$; a nonzero bound exceeding the CGB budget would be the only known mechanism to convert the F‑route into an obstruction.

### 9. Candidate lemmas, both hemispheres, with honest hypotheses

- **Existence hemisphere.** If (i) $M$ has positive, bounded‑below Yamabe invariant, (ii) some minimizing sequence admits a uniform Sobolev bound (noncollapse), and (iii) the Biquard obstruction vanishes for some chirality marking on $\mathcal O$, then attainment holds and $M$ is Einstein. Hypotheses (ii) and (iii) are exactly the collapse gap and the gluing obstruction.
- **Obstruction hemisphere.** If the Biquard obstruction is nonzero at all nodes for all markings **and** every F‑minimizing sequence orbifold‑converges to the fixed $\mathcal O$ (a moduli‑uniqueness/rigidity statement), then $\inf F$ is not attained and $M$ carries no Einstein metric of any sign. The uniqueness input is unproven and would itself require an Einstein‑orbifold moduli finiteness theorem for the class $\chi=8$, $\int|\mathrm{Rm}|^2\le\Lambda$.

### 10. Net assessment for the next agent

The F‑attainment route is mathematically exact and sign‑neutral, and it collapses the mixed‑row Einstein question into a single compactness dichotomy with a completely explicit conjectured degeneration (orbifold + Eguchi–Hanson tree, energy‑saturating). Its real deliverables are: (a) the closed‑form Biquard obstruction computation on the homogeneous orbifold as the sharpest cheap discriminator, (b) the observation that on monopole‑void rows the route has no smooth‑structure input and therefore no visible obstruction mechanism, and (c) a concrete PDE target — quantitative almost‑critical $\varepsilon$‑regularity for $\mathcal F_{-1/4}$ plus noncollapse — whose resolution would let Anderson/Tian–Viaclovsky decide the dichotomy. What the route does **not** do is manufacture new leverage past the Biquard/Ozuch obstruction or past collapse; both remain the operative unknowns, now stated globally and sign‑neutrally rather than locally.