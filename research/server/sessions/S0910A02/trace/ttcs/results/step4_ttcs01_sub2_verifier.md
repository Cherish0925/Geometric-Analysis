# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md",
    "Sessions/S0910A02/workspace/notes/step3_stable_integral_obstruction_principle.md",
    "Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md"
  ]
}
```

## Task

Check the Step-4 Preceptor note for Yau Problem 26. Focus on the four-dimensional full-Weyl Chern--Gauss--Bonnet accounting and the route judgment. Verify the constants and inequalities: 8π²χ = ∫(|W|²+s²/24-|E|²/2), b(δ)=(2/3)(1-δ)²-2δ², volume ceiling, equivalence between volume lower bound and Weyl-energy deficit up to δ-dependent constants, and the claim that tight pinching plus bounded |Rm| forbids 4D collapse. Also check the target-fidelity/refutation logic: p→1/3+ negative LeBrun boundary alone cannot refute Q_4, positive branch obstruction statements are not overclaimed, and Anderson/Ye source gaps are stated at their real scope. Identify corrections or sharper formulations that would materially affect the next research step.

## Output

## Verifier memo — Step-4 Preceptor note (4D full-Weyl CGB accounting and route logic)

Bottom line: I reworked every displayed constant, identity, and inequality in the note. They are all correct, including the ones that were repaired earlier in the session. The route logic (both sign branches needed to refute $Q_4$; positive-branch obstructions stated at their true strength; Min-Oo/Anderson/Ye conditions) is also correct. Below I confirm each computation, then give the two sharper formulations and one concrete source-object that would materially affect the next research step.

### 1. Curvature identities and pointwise bounds — correct

- **(GB)** $8\pi^2\chi=\int(|W|^2+\tfrac{s^2}{24}-\tfrac12|\mathring r|^2)$ is the standard full-Weyl 4D Gauss–Bonnet form (Besse convention). It is internally consistent with the CGB+ signature form used in the Step-3 note: adding $3\tau=\tfrac1{4\pi^2}\int(|W^+|^2-|W^-|^2)$ to $\chi$ gives exactly $2\chi+3\tau=\tfrac1{4\pi^2}\int(2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|\mathring r|^2)$. Verified by direct combination.
- **Pointwise bounds.** With Ricci-endomorphism eigenvalues $\sigma+e_i$, $|e_i|\le\delta$: $|s|\ge 4(1-\delta)$ from $s=4\sigma+\sum e_i$, so $\tfrac{s^2}{24}\ge\tfrac23(1-\delta)^2$; and $|\mathring r|^2=\sum(e_i-\bar e)^2=\sum e_i^2-4\bar e^2\le 4\delta^2$. Both correct. The upper side $|s|\le4(1+\delta)$ gives $\tfrac{s^2}{24}\le\tfrac23(1+\delta)^2=a(\delta)$, so $b(\delta)\le B\le a(\delta)$ with $B=\tfrac{s^2}{24}-\tfrac12|\mathring r|^2$ is correct.

### 2. $b(\delta)$, positivity window, volume ceiling — correct

- $b(\delta)=\tfrac23(1-\delta)^2-2\delta^2=\tfrac23-\tfrac43\delta-\tfrac43\delta^2$. Verified by expansion.
- $b(\delta)>0\iff(1-\delta)^2>3\delta^2\iff\delta<\tfrac1{1+\sqrt3}\approx0.366$. Verified.
- Inequality (1) $\int|W|^2+b(\delta)\mathrm{Vol}\le 8\pi^2\chi$ follows pointwise from $B\ge b(\delta)$ and $|W|^2\ge0$. Euler positivity $\chi>0$ (hence integer $\chi\ge1$) and the ceiling $\mathrm{Vol}\le 8\pi^2\chi/b(\delta)$ follow. At $\delta=0$: $b(0)=\tfrac23$, $\mathrm{Vol}\le12\pi^2\chi$, which is the exact Einstein volume bound for $\mathrm{Ric}=\pm g$. Verified. The expansion $8\pi^2\chi/b(\delta)=12\pi^2\chi+O(\delta)\chi$ (coefficient $24\pi^2$) is correct.

### 3. Volume ↔ Weyl-deficit equivalence and bounded-curvature no-collapse — correct

- $\mathrm{Vol}\ge v\Rightarrow\int|W|^2\le8\pi^2\chi-b(\delta)v$, and $\int|W|^2\le8\pi^2\chi-\eta\Rightarrow\mathrm{Vol}\ge\eta/a(\delta)$: both are immediate from $8\pi^2\chi=\int|W|^2+\int B$ with $b(\delta)\mathrm{Vol}\le\int B\le a(\delta)\mathrm{Vol}$. The two $\delta$-dependent constants are asymmetric ($b$ has a linear deficit, $a$ a linear excess) but that is harmless.
- Bounded-curvature statement: $|Rm|\le K\Rightarrow|W|^2\le K^2$ (orthogonality of the Weyl/Ricci/scalar decomposition gives $|W|\le|Rm|$ pointwise, same norm as in GB). Then $8\pi^2\chi\le(K^2+a(\delta))\mathrm{Vol}$, so $\mathrm{Vol}\ge 8\pi^2\chi/(K^2+a(\delta))\ge8\pi^2/(K^2+a(\delta))$ using $\chi\ge1$. Verified. The Bochner remark ($\mathrm{Ric}>0\Rightarrow b_1=0\Rightarrow\chi=2+b_2\ge2$ on oriented $M$) is correct. The trace-free energy bound $\int|\mathring r|^2\le4\delta^2\mathrm{Vol}\le\tfrac{32\pi^2\delta^2}{b(\delta)}\chi$ is correct.

The deduction is exactly what it is stated to be: with a *fixed* curvature bound $K$, tight pinching forbids collapse, so collapse compatible with tight pinching forces $|Rm|\to\infty$ with $\int|W|^2$ approaching the entire $8\pi^2\chi$ budget. This is consistent with the Anderson $T^3$-collapse example (Cheeger–Naber Example 2.16): those have $\mathrm{Ric}\to0$, not $\mathrm{Ric}\approx\pm g$, so tight pinching excludes them. No error, and the note does not assert more than the fixed-$K$ statement.

### 4. Refutation logic — correct, and I confirm it by an explicit rescaling argument

The note's assertion "refuting $Q_4$ needs defeating both sign branches; a minus-branch LeBrun construction alone does not refute $Q_4$" is right. Verification:

- $Q_4$ is true iff *some* interval $[c_4,C_4]$ forces Einstein existence. Proving one sign branch (say $\|\mathrm{Ric}-g\|_{op}\le\epsilon\Rightarrow$ Einstein) exhibits the interval $[1-\epsilon,1+\epsilon]$, hence proves $Q_4$. So each branch proving is sufficient.
- Wider intervals are weaker hypotheses: $[c,C]\subset[c',C']$ and $[c',C']$ works $\Rightarrow[c,C]$ works. So if tight intervals do not work, all wider ones do not either.
- A positive-branch example (Ricci in $[1-\delta,1+\delta]$, no Einstein) rescales by $g\mapsto\lambda g$ to Ricci in $[(1-\delta)/\lambda,(1+\delta)/\lambda]$ (Ricci is scale-invariant; the comparison scales), covering every interval with $C>0$, including small straddling ones. It cannot cover intervals with $C\le0$ (Ricci stays positive). Those require a minus-branch example. Hence both branches with $\delta\to0$ are genuinely needed. Confirmed.

The Step-3 stable-obstruction engine that Step-4 relies on also checks out: from (1) $L_+-T_+\le\tfrac{\delta^2}{2\pi^2}\mathrm{Vol}$ and (2) $\mathrm{Vol}\le\tfrac{4\pi^2T_+}{b(\delta)}$ one gets $(L_+-T_+)b(\delta)\le2T_+\delta^2$, then $(L_+-T_+)\tfrac23(1-\delta)^2\le2L_+\delta^2$, i.e. $\tfrac{\delta}{1-\delta}\ge\sqrt{\tfrac{L_+-T_+}{3L_+}}$; with $L_+=\tfrac23A$, $T_+=A-k$ this is $\sqrt{(p-1/3)/2}$. All steps verified.

### 5. Positive-branch obstruction statements are at their true strength

- LeBrun/SW general-type blow-ups: $\delta_+<1\Rightarrow\mathrm{Ric}>0\Rightarrow s>0$, incompatible with a nonzero monopole class (no PSC), so these manifolds carry no positive-pinched metric at all — they are inert for $P_4^+$, not counterexamples. Correct, not overstated.
- Hitchin–Thorpe filter: in the positivity window, $2\chi\pm3\tau\ge\tfrac{b(\delta)}{4\pi^2}\mathrm{Vol}>0$ gives strict $2\chi>3|\tau|$ (and $\chi>0$) for any tightly pinched metric of either sign. Verified. So HT-violating topologies are excluded as tight inputs — a genuine sign-blind topological filter.
- Positive-Ricci surgery existence (Sha–Yang/Wraith/Reiser/Perelman core metrics) being strictly weaker than Einstein or tight pinching: stated correctly.

### 6. Min-Oo / Anderson / Ye conditions match the sources

The Min-Oo source confirms the stated conditions exactly: $n>3$, average scalar curvature $r<0$, $d^2\max|K|<\Lambda^2$, and pinching $\max_{SM}|np/r-1|<\epsilon(n,\Lambda)$; the Sobolev/isoperimetric control comes from a Ricci lower bound plus diameter, and the output metric is near the input. This is not dimension-only Ricci pinching, and the method explicitly does not run for the non-below-zero Einstein constant. The note uses it correctly and only as a $\sigma=-1$-branch, sectional-curvature-and-diameter-controlled result. Anderson 1989 Cor. B(4) and Ye 1993 are correctly held as not-yet-retrieved and not used as theorem support; Kröncke's citation places Ye as a stability-near-existing-Einstein result, which is the right reading given the available text.

### 7. Two sharper formulations and one concrete source object for the next step

**(a) The linear-in-$\delta$ deficit is intrinsic to operator-norm pinching and controls any edge analysis.** $b(\delta)=\tfrac23-\tfrac43\delta+O(\delta^2)$; the linear term comes entirely from $|s|\ge4(1-\delta)$. It vanishes only if a scalar-centering normalization ($\sum e_i=0$, i.e. $s\equiv4\sigma$) is imposed, which the Yau-26 hypothesis $c_ng\le\mathrm{Ric}\le C_ng$ does not supply. Consequence for the $p\to1/3^+$ edge study: the volume ceiling, the trace-free energy bound, and the stable-obstruction margin all degrade linearly, not quadratically, in $\delta$. Any quantitative near-equality analysis that wants a quadratic margin must first argue a scalar-centering step; otherwise the linear rate is the governing one.

**(b) The genuinely open regime is a volume lower bound with no a priori $v$.** The accounting delivers a ceiling always, and a floor *only under a curvature bound*. Under $P_4^+$, Myers gives a diameter bound and $|\mathrm{Ric}|$ is bounded automatically, so the sole missing hypothesis to enter Cheeger–Naber (Thm 1.12/1.13) and Anderson/BKN noncollapsed regularity is $\mathrm{Vol}\ge v>0$. Two points sharpen this: (i) Yau-26 needs constants independent of any $v$, so the collapsed / Weyl-saturation case ($\int|W|^2\to8\pi^2\chi$) is the one not reached by these tools; (ii) even with noncollapse, Cheeger–Naber yields finitely many diffeomorphism types and Einstein-orbifold limits, which is finiteness, not existence on the fixed smooth $M$ — the desingularization step is where Ozuch/Biquard show a generic $\det\mathbf R=0$ obstruction. So the positive existence route, as the note states, reduces to either resolving the Weyl-saturation collapse case or producing a new positive-branch mechanism; the accounting does not itself close it.

**(c) Ozuch Example 1 is the most on-point positive-Ricci near-Einstein object in the present sources and deserves an explicit dissection.** The supplied Ozuch text (Example 1) exhibits a smooth $M^4$ and metrics $g_i$ with $\mathrm{Ric}(g_i)\ge3g_i$ and $\|\mathrm{Ric}(g_i)-3g_i\|_{L^p}\to0$, GH-converging to $\mathbb S^4/\mathbb Z_2$, with no Einstein sequence $\mathrm{Ric}=3g_i$ converging to that orbifold. Two features determine whether this bears on $P_4^+$, and both point against a direct reading as a pointwise-pinching counterexample: the closeness is $L^p$, not pointwise operator norm (the gluing produces curvature concentration in the neck, so $\|\mathrm{Ric}-3g\|_{op}$ does not tend to zero over $M$), and "no Einstein GH-close to this orbifold" is not "no Einstein metric on $M$." The productive next object is therefore the exact pointwise Ricci two-sided bound of the $g_i$ (retrievable from Ozuch II / Biquard) and whether the underlying $M^4$ admits any Einstein metric at all. If the $g_i$ turned out to be pointwise two-sided pinched with ratio $\to1$ and $M^4$ Einstein-free, that would be a positive-branch object of the exact type the route review asks for; the available text does not establish either, and the neck-curvature structure makes pointwise pinching unlikely. Stating this precisely would keep the positive-branch discussion anchored to a real source rather than to the abstract "new obstruction needed."

No arithmetic or sign errors were found in the Step-4 note; the accounting is sound and its route judgment is supported by the branch/rescaling analysis above. The three items in §7 are the ones that would change how the next positive-branch and edge-analysis work is set up.