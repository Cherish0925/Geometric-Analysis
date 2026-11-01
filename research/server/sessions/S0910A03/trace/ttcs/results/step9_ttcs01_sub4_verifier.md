# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md",
    "Sessions/S0910A01/workspace/notes/step10_accessible_cover_reassessment.md"
  ]
}
```

## Task

Verify or refute the following regularity claim and identify the precise obstruction if false:

CLAIM (the regularity question): On a 4-dimensional Riemannian ball (B_1(p), g) with Ric ≥ -3g that arises as the local universal cover of a collapsed near-Einstein ball, suppose:
(a) fint_{B_r(p)} |Rm|² ≤ K for all 0 < r ≤ 1/3 (controlled maximal curvature function)
(b) Ric ≥ -(1+δ)(n-1)g with δ small

Does (a)+(b) force Vol(B_{r*}(p)) ≥ c(K)r*⁴ for some fixed r*(K) > 0?

Consider:
1. Known ε-regularity theorems (Anderson, Cheeger-Naber) and whether they apply without noncollapse as input
2. Whether the 4D conformal invariance of ∫|Rm|² adds structure
3. Whether a countermodel exists: a collapsed ball with Ric ≥ -3g, controlled normalized curvature mean at every scale, and Vol → 0
4. The distinction between 'local universal cover' and 'arbitrary ball' - the cover has no short loops
5. Whether Naber-Zhang Prop 6.4 hypotheses (GH model, maximal rank, model noncollapsing) follow from (a)+(b)

Give a precise mathematical assessment, not a survey.

## Output

## Verification memo: the fixed-scale volume lower bound from curvature-mean control

### Direct assessment

The proposed implication **(a) + (b) ⟹ Vol(B_{r*}) ≥ c(K) r*⁴** is **false as stated**. Hypotheses (a) and (b) — a bounded normalized $\int|\mathrm{Rm}|^2$ at every scale $r\le 1/3$, together with a Ricci lower bound $\mathrm{Ric}\ge -3g$ — are compatible with unbounded collapse on a *simply connected* space. A ball inside the Berger family furnishes an explicit counterexample that meets exactly the two operative hypotheses. The near-Einstein wording ("arises as the local universal cover of a collapsed near-Einstein ball") is context, not a working hypothesis; if one promotes it to a working hypothesis the situation changes and I treat that separately below.

### The counterexample

Take the Berger metric on $S^3=SU(2)$ with left-invariant coframe $\{\sigma_1,\sigma_2,\sigma_3\}$,
$$
g_\lambda=\lambda^2\sigma_1^2+\sigma_2^2+\sigma_3^2,\qquad \lambda\to 0,
$$
and form the product $ (N^4,\,\bar g_\lambda) = S^3_\lambda\times\mathbb R$. Its geometry is standard:

- Sectional curvatures $K(X_2,X_3)=4-3\lambda^2$, $K(X_1,X_2)=K(X_1,X_3)=\lambda^2$; all bounded, all $\ge 0$. Hence $|\mathrm{Rm}|\le C$ uniformly ($C\approx 4$), and $\mathrm{Ric}\ge 0$.
- On the product, $\mathrm{Ric}_{\bar g_\lambda}\ge 0 \ge -3\bar g_\lambda$, so **(b) holds** (indeed with room to spare).
- Because $|\mathrm{Rm}|\le C$ pointwise, $\fint_{B_r}|\mathrm{Rm}|^2\le C^2$ for **every** $r$, so the maximal-function condition **(a) holds** with $K=C^2$, at all scales including $r<\lambda$.
- The Hopf fiber is a closed geodesic of length $2\pi\lambda\to 0$; the $S^3_\lambda$ factor collapses to $S^2(\tfrac12)$. For any fixed $r_*\le 1/3$, $\mathrm{Vol}(B_{r_*})\sim \lambda \to 0$. So **the conclusion fails for every fixed $r_*$**.
- $N^4=S^3_\lambda\times\mathbb R$ is simply connected: it is a genuine local universal cover (take base $S^3_\lambda\times S^1_L$; unwrapping the $S^1$ gives exactly $S^3_\lambda\times\mathbb R$).

Thus a genuine local universal cover, with no noncontractible short loops, satisfies (a) and (b) with a uniform $K$ and still collapses to volume zero at every fixed scale. The proposed regularity implication does not hold.

### The precise obstruction

The mechanism is continuous local symmetry. The universal cover undoes collapse that is carried by the **discrete** group $\pi_1$ (short *noncontractible* loops become long). It does **not** undo collapse carried by a **continuous** isometric orbit. In the Berger sphere the collapsing direction is the Hopf $S^1$: the shrinking geodesics are contractible closed geodesics (orbits of a continuous isometry), not elements of $\pi_1$. Passing to the universal cover leaves them untouched, because $S^3_\lambda$ is already simply connected.

This exposes the reading of point (4) that is doing the work in the notes. "The cover has no short loops" is true only for *noncontractible* loops; the cover can and does retain arbitrarily short *contractible* closed geodesics whenever the collapse has a positive-dimensional continuous nilpotent (here abelian $S^1$) local structure. In Cheeger–Fukaya–Gromov language: the local nilpotent structure $N$ governing the collapse need not be discrete. The universal cover is noncollapsed precisely when $N$ is discrete (pure $\pi_1$). A one-parameter continuous $N$ produces collapse that survives on the cover. This is not excluded by any amount of $L^2$-curvature-mean control or by a Ricci lower bound.

### Sub-question 1 — Anderson and Cheeger–Naber

Neither generates noncollapse; both consume it.

- Anderson $\varepsilon$-regularity needs *absolute* smallness $\int_B|\mathrm{Rm}|^2<\varepsilon_0$ **and** a volume lower bound $\mathrm{Vol}(B_1)\ge v>0$ as input, and returns a harmonic radius. Removing the volume input removes the conclusion.
- Cheeger–Naber codimension-four regularity (Thm 1.4) and the 4D finiteness (Thm 1.12) both take a uniform lower volume bound as hypothesis.

So the known theorems cannot be inverted to *produce* the volume lower bound from (a)+(b). In the Berger example, $\int_{B_r}|\mathrm{Rm}|^2\le C^2\,\mathrm{Vol}(B_r)\to 0$: the *absolute* energy actually tends to zero, yet no volume lower bound appears — exactly the situation these theorems cannot address without noncollapse assumed.

### Sub-question 2 — 4D conformal invariance of $\int|\mathrm{Rm}|^2$

Scale invariance of the absolute energy is fully consistent with collapse and supplies no volume lower bound. Under blow-up of a collapsing ball the invariant energy is preserved, but the blow-up limit is a lower-dimensional space ($S^2\times\mathbb R$ in the Berger case), not a noncollapsed 4-manifold. Conformal invariance controls how energy transports across scales; it does not manufacture the 4-dimensional volume that noncollapse requires. It adds no structure toward the desired implication.

### Sub-question 5 — do Naber–Zhang Prop 6.4 hypotheses follow from (a)+(b)?

No. Prop 6.4 requires (i) GH-closeness to a model $\mathbb R^{k-\ell}\times Z^\ell$ with $\ell\le3$, (ii) a uniform model noncollapsing radius $r_c>0$, and (iii) **maximal fibered nilpotency rank $n-k$**. Condition (iii) is exactly the statement that the collapse is accounted for by the *discrete* fundamental group — i.e., that the continuous part of $N$ is trivial. This is the precise hypothesis that rules out the Berger mechanism. (a)+(b) say nothing about the rank of the fibered structure and do not imply (iii); the Berger example has $k=3$, $\ell=0$, a continuous $S^1$ collapse, and rank $0<n-k=1$ — it is a rank-drop configuration, precisely the case Prop 6.4 excludes by hypothesis rather than concludes. Also note (a)+(b) give bounded *Ricci* only from below and bounded $\mathrm{Rm}$ only in $L^2$-mean, not the pointwise $|\mathrm{Rm}|\le C$ that CFG bounded-curvature theory uses; Naber–Zhang works with bounded Ricci precisely to avoid this, but at the price of needing (i)–(iii) as input.

### What changes under the near-Einstein condition (and what remains open)

The surrounding program does not actually have only (a)+(b): the deficit $F_i\to 0$ forces $\mathrm{Ric}\to -g$ in mean on the cover, i.e. a two-sided pinching toward $\lambda=-1$, not merely a lower bound. This is a strictly stronger input, and it disarms the Berger counterexample, whose Ricci is $\ge 0$, far from $-g$. So the *literal* implication is false, but the *operationally relevant* implication — bounded curvature mean at all scales **plus $\mathrm{Ric}\to -g$ in mean** ⟹ fixed-scale noncollapse of the cover — is not settled by the Berger example and is a genuinely different question.

Here is the structure the core work should confront, stated as substance rather than as instruction:

1. All *known* homogeneous $\lambda<0$ Einstein models ($\mathbb{RH}^4$, $\mathbb{CH}^2$, solvable-group Einstein metrics) have noncollapsed universal covers: they are homogeneous, hence carry uniform injectivity radius, and their cusps ($\Gamma\backslash\mathbb{RH}^4$, complex-hyperbolic Heisenberg cusp) collapse only through the *discrete* lattice $\Gamma$, which the universal cover undoes. This is why the real- and complex-hyperbolic cusps in step8/step10 unwrap to noncollapsed symmetric spaces.

2. A $\lambda=-1$ *continuous* collapse on the cover would require a positive-dimensional isometric nilpotent action whose orbit volume shrinks while the metric stays near $\mathrm{Ric}=-g$. This is exactly the object the orbit-volume ODE governs: $\Delta_B v=(\tfrac14|F|^2-\lambda N)v$ with $\lambda=-1$, and the $\mathrm{nil}^3$ relation $v''=(3-\mu)v$. The recorded analysis excludes circle-base models but leaves interval/cusp segments alive — and those cusps are exactly the ones that unwrap to noncollapsed homogeneous spaces. Whether a *unit-scale* continuous collapse of the cover with $\mathrm{Ric}\to -g$ can exist is therefore the real content, and it is tied to the endpoint behavior of $\rho$ in the $\mathrm{nil}^3$ ODE and to whether the continuous symmetry can persist at a fixed physical scale rather than only as $r\to0$.

3. What is still absent, and what would actually decide the matter: a statement that $\mathrm{Ric}\to -g$ in mean on the cover (not just $\mathrm{Ric}\ge -3g$) forbids a positive-dimensional continuous nilpotent collapse structure at a fixed scale. Equivalently, that the near-Einstein condition forces the fibered nilpotency rank to be maximal (the CFG structure discrete) on a positive volume proportion. That is precisely Naber–Zhang condition (iii), and it must come from the Einstein equation itself — the $L^2$ curvature mean and one-sided Ricci bound provably do not deliver it, as Berger shows.

### Bottom line for the transported-mean bridge

The Step 9 architecture reduces the $\lambda<0$ fixed-topology pinching question to "controlled normalized curvature at every scale on the cover ⟹ fixed-scale noncollapse." The verification here shows this reduction cannot be closed by curvature-energy control plus a Ricci lower bound alone: the Berger product realizes every such hypothesis while collapsing. The missing ingredient is the exclusion of continuous-symmetry collapse, which is neither an $\varepsilon$-regularity output nor a consequence of conformal invariance, and which is exactly the maximal-rank input that Naber–Zhang assumes. The one avenue not refuted by Berger is the full two-sided near-Einstein condition $\mathrm{Ric}\to -g$; deciding it is the same continuous-symmetry $\lambda=-1$ collapse problem already visible in the orbit-volume ODE, and it requires using the Einstein equation, not the mean curvature control, to force discreteness of the collapse structure.

One consistency note on the Step 9 phrasing "the calibrated-germ contradiction survives at scale $r_*$ because the rescaled Einstein constant is $-r_*^2\ne 0$": this is correct *if* a fixed $r_*$ noncollapsed harmonic chart is available, but the availability is exactly the unproven point. The Berger analysis shows that a fixed $r_*$ cannot be produced from (a)+(b); the honest state is that $r_*$ may only exist at shrinking scale, where (as the notes already record) the rescaled Einstein constant $-r_*^2\to 0$ and the calibrated spectrum contradiction dissolves. The two things the notes must not conflate are: bounded normalized curvature at all scales (available) and a fixed-scale noncollapsed cover (not available from the stated hypotheses).