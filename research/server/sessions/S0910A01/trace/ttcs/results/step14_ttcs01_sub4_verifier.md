# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step14_smoothing_vs_reduction_route.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md"
  ]
}
```

## Task

Evaluate the source-grounded smoothing route for the four-dimensional negative branch of Yau Problem 26. Read the Step 14 route note and the Ye Li 0911.3104 smoothing source carefully. Check the scale calculation: bounded local mean |Rm|^2 on a maximal-function good ball implies Ye Li's r^4-average smallness after choosing a fixed small physical radius. Determine exactly what is and is not supplied by Li's theorem as stated (complete/all-centers vs buffered local), and whether the route note faithfully identifies the missing bridges. Then assess how this could interact with the existing Derdziński chart-accessibility theorem: what additional statement would be sufficient to turn smoothing into a fixed-scale normal-cover/harmonic-chart contradiction, and what assumptions would be unsupported? Do not decide the session; give a rigorous mathematical memo with source-specific hypotheses and possible proof repairs.

## Output

## Verifier memo: the Li-smoothing route for the $\lambda<0$ four-dimensional branch of Yau 26

### 1. The §3 scale computation is correct, and its true content is a maximal-function statement

The algebra in Step 14 §3 is sound. The one identity that carries everything is
$$
\frac{r^4}{\operatorname{Vol}B_r(q)}\int_{B_r(q)}|\operatorname{Rm}|^2 \;=\; r^4\,\fint_{B_r(q)}|\operatorname{Rm}|^2,
$$
so Li's dimensionless quantity is exactly $r^4$ times a local mean. The transfer step is also correct: for $q\in B_r(p)$ one has $B_r(q)\subset B_{2r}(p)\subset B_{3r}(q)$, and Bishop–Gromov relative comparison under $\operatorname{Ric}\ge -3g$ (in dimension four this is $\operatorname{Ric}\ge -(n-1)Kg$ with $K=1$, model $H^4(-1)$) gives
$$
\frac{\operatorname{Vol}B_{2r}(p)}{\operatorname{Vol}B_r(q)}\le\frac{\operatorname{Vol}B_{3r}(q)}{\operatorname{Vol}B_r(q)}\le\frac{V_{-1}(3r)}{V_{-1}(r)}=:C_{BG}(r),
$$
which is bounded by a dimensional constant for $r\le1$ (the ratio tends to $3^4=81$ as $r\to0$ and stays finite up to $r=1$). Hence $r^4\fint_{B_r(q)}|\operatorname{Rm}|^2\le r^4 C_{BG}(r)K_0$, and $r_*(K_0)=(\varepsilon_{Li}/2C_{BG}K_0)^{1/4}$ makes the Li input hold. This is arithmetically right and the "fixed physical radius" observation is genuine: the near-Einstein scale is fixed before $i\to\infty$.

One sharpening the note states loosely and should be stated cleanly. §3 writes the input as a mean bound "$\fint_{B_{2r}(p)}|\operatorname{Rm}|^2\le K_0$," but a mean over a big ball does **not** control means over concentric sub-balls; that is why the last paragraph of §3 and Step 11's Hardy–Littlewood passage are actually load-bearing. The correct hypothesis is the centered maximal control
$$
\mathcal M_R(|\operatorname{Rm}|^2)(p):=\sup_{s\le R}\fint_{B_s(p)}|\operatorname{Rm}|^2\le K_0 .
$$
From a single such good center $p$ at macroscopic radius $R$, the same Bishop–Gromov estimate gives the dimensionless smallness at radius $r_*$ for **every** center $q$ in a fixed-multiple buffer $B_{\beta r_*}(p)$ with $(\beta+2)r_*\le R$: for $d=d(q,p)\le\beta r_*$,
$$
\fint_{B_{r_*}(q)}|\operatorname{Rm}|^2\le\frac{V_{-1}((\beta+2)r_*)}{V_{-1}(r_*)}\,K_0 .
$$
So the object §3 really produces is not "one good ball" but "smallness for all centers in a buffer around a maximal-good center." That distinction is exactly what Li's theorem consumes, and it is the correct target.

Consistency point worth recording: on the collapsed part the **absolute** integral $\int_{B_{r_*}}|\operatorname{Rm}|^2\le K_0\operatorname{Vol}B_{r_*}$ is automatically small because volume is small, so the dimensionless (mean$\times r^4$) form is the right invariant. This matches the Cheeger–Tian shrinking sentence in Li (paragraph before the References): an absolute small $L^2$ bound forces the dimensionless smallness on a comparable concentric ball. The route targets the correct quantity.

### 2. What Li's Theorem 3.6 supplies, and the actual barrier

Li's Theorem 1.1/3.1/3.6 is a **complete, all-centers** statement. Three features of the source make this structural, not cosmetic:

- Theorem 1.1 and eq. (3.2) impose the smallness "for any $x\in M$." Theorem 3.6 restates the dimensionless form with the same universality.
- The existence proof (Theorem 3.4 and the proof of 3.1) runs a covering argument $B_{2r}(x)\subset\bigcup_{i=1}^N B_r(y_i)$, $y_i\in B_{3r/2}(x)$, coupling each ball to neighbors. Li explicitly notes "the equation discussed here is not local."
- The continuation argument defines $[0,T_{\max})$ by the **global** conditions (3.7)–(3.9), in particular $\sup_{x\in M}\|\operatorname{Rm}(g(t))\|_{2;B_r(x)}\le 2[C_1A_0]^{-1}$. The uniform definite existence time $T\ge C_1\min(r^2,K^{-1})$ and the uniform $\|\operatorname{Rm}\|_\infty\le C_2/t$ depend on this global sup being controlled at $t=0$.

The note's assessment that this is "an all-centers smoothing theorem, not yet a theorem that one selected good center gives a local flow on a buffered ball" is faithful and correct.

The memo should, however, name the real barrier precisely, because the note leaves it implicit. Yau 26 lives on **closed** four-manifolds, which are already complete, so noncompactness is not the obstruction. On a closed manifold Hamilton's classical short-time existence gives a flow with no smallness at all — but only for a time controlled by $\max|\operatorname{Rm}(g_0)|$, which degenerates along the near-critical LeBrun sequence, so the fixed-$t$ bound $|\operatorname{Rm}(t)|\le C/t$ uniform in $i$ is lost. Li's theorem is valuable precisely because its existence time and curvature bound depend only on $\varepsilon,K,r$, not on $\max|\operatorname{Rm}|$. The obstruction to using it here is therefore:

> the Noether/maximal-function selection supplies the dimensionless smallness only on a positive-fraction good set; on the complementary high-energy set (fraction $\le C\cdot12/\Lambda$ by the Prop 1 bound $\overline{|\mathcal R|^2}\le12+o(1)$ and Chebyshev/Hardy–Littlewood) the smallness genuinely fails at any fixed $r_*$.

Hence a **global** application of Li on closed $M$ is impossible, and the missing object is an *interior* version tolerating a high-energy exterior. This is a pseudolocality-type statement: given the dimensionless smallness on a buffer $B_{\beta r_*}(p_i)$ and $|\operatorname{Ric}|\le K$, one wants a uniform-in-$i$ interior bound $|\operatorname{Rm}(g_i(t))|\le C/t$ on $B_{\beta r_*/2}(p_i)$ for $t\le\theta r_*^2$, with the exterior bad set confined to a collar of width $\sim\sqrt t$. Li's global maximum-principle continuation does not give this; the collar-confinement (heat-type quasi-locality of the curvature estimate) must be proved. The note's §5.1 menu (localized/conformal-completion Li; Yang/Xu with a collapsed replacement for the Sobolev constant; Huang–Wang under model+rank hypotheses) is the right menu, and it correctly records that no cited source delivers the collapse-compatible interior existence: Yang/Xu need a local Sobolev/volume-doubling input, Wang pseudolocality needs a small-volume lower bound at scale $\tau r$, and Huang–Wang needs a GH-model plus maximal fibered nilpotency rank. All three re-import a noncollapse or rank hypothesis of the kind the program is trying to produce rather than assume.

### 3. Faithfulness of the "two missing bridges," with two sharpenings

The note's §5.1 (localize Li) and §5.2 (preserve/recover near-Einstein and calibrated data) are the two correct bridges. Two places need more force.

**(a) The parabolic transfer of the Einstein defect (route "use the smoothed metrics").** The note says $|\operatorname{Rm}|\le C/t$ "may amplify $\delta_i$ only polynomially in $t$," which is too optimistic as stated. The scale-invariant defect is $\mathring{\operatorname{Ric}}=E$, and under Ricci flow $\partial_t|E|^2\le\Delta|E|^2+c|\operatorname{Rm}||E|^2$. A maximum-principle Grönwall with $|\operatorname{Rm}|\le C/t$ gives $\sup|E|^2(t)\le\sup|E|^2(\epsilon)\,(t/\epsilon)^{cC}$, and $\int_0^\theta C/s\,ds$ **diverges**, so this does not propagate the small initial defect $\sup|E(0)|=O(\delta_i)$ to a positive time. Equivalently $|E(t)|\le|\operatorname{Rm}(t)|\le C/t$ is the only free bound, and it is not small. Preserving the pointwise near-Einstein condition under the flow is therefore an open analytic point, not a polynomial estimate. The calibrated $W^+$ data is at least as fragile. This makes the "use the original metric" branch the mathematically cleaner one.

**(b) The "use the original metric" branch (route A) is stronger than the note frames it, once one identifies what smoothing must actually deliver.** Li's bilipschitz control $\tfrac12 g_0\le g(t)\le2g_0$ (his (3.8), via Hamilton's trick) is uniform, so volumes distort by at most $2^4$ and radii by at most $2$. Consequently the only thing smoothing needs to hand back to $g_i(0)$ is **noncollapse on a normal cover**, not preserved curvature or defect:

> **Sufficient statement (S).** For a positive volume proportion of centers $p$ in the near-critical LeBrun sequence there is a buffered normal cover $\pi:(\widehat U,\hat g_i(0))\to(B_{4h}(p),g_i(0))$ with $\operatorname{Vol}_{\hat g_i(0)}B_h(\hat p)\ge v h^4$, for fixed $h,v>0$.

If (S) holds, Cheeger–Naber (bounded Ricci $|\operatorname{Ric}|\le3/2$ plus noncollapse) gives harmonic charts of definite radius for the **original** metric $\hat g_i(0)$ off a set of $r^4$-small measure, i.e. $(h',v')$-chart-accessibility on positive volume, contradicting Step 11 Theorem 1 through the original defect $F_i$ (whose local mean is $\to0$ on the good set by the established $\int F_i=o(A)$ estimate). Route A therefore never needs the flow to preserve $E$ or $W^+$; it needs the flow only to establish noncollapse of a normal cover.

### 4. Where smoothing genuinely helps, and where it does not — the interaction with the Derdziński theorem

The clean way to see the interaction: **smoothing converts "bounded Ricci" into "bounded sectional curvature" on the buffered good region** ($|\operatorname{Rm}(g_i(\theta r_*^2))|\le C/(\theta r_*^2)$, a fixed bound uniform in $i$). This is a real gain, because it replaces the fragile bounded-Ricci collapse theory (Naber–Zhang, with residual-dimension and maximal-rank hypotheses) by the classical bounded-curvature collapse theory of Cheeger–Fukaya–Gromov. On the **regular** stratum of the resulting N-structure, CFG gives a normal cover on which the metric is noncollapsed with injectivity radius bounded below by a constant depending only on the curvature bound; via the bilipschitz transfer this yields (S) for $g_i(0)$ there. So the chain

$$
\text{localized Li}\;\Rightarrow\;|\operatorname{Rm}|\le C/t\;\Rightarrow\;\text{CFG regular N-structure}\;\Rightarrow\;(S)\;\Rightarrow\;\text{chart-accessible}\;\Rightarrow\;\text{Derdziński contradiction}
$$

is coherent, and it is a stronger footing for the accessibility half than the earlier Naber–Zhang framing.

What smoothing does **not** remove is the rank-zero / singular-stratum evasion, and this deserves emphasis because the note treats the Taub–NUT–AdS object mainly as an original-metric energy issue. Even with genuinely bounded sectional curvature, CFG noncollapse of covers holds only on the regular stratum. Near a fixed orbit of a local circle N-structure (the Taub–NUT–AdS geometry with $\nu\to0$ is exactly this) the small fiber is contractible, the fibered rank is $0$ instead of the needed $4-3=1$, the local fundamental group is trivial, unwrapping produces no new volume, and yet the region is collapsed with a bounded-curvature metric. Such a region is neither chart-accessible directly (its harmonic radius is comparable to the collapse scale) nor via unwrapping. Crucially, after smoothing the curvature there is **bounded** ($C/t$), so the maximal-function energy exclusion that removes NUT cores at the level of the original metric (Step 12: divergent mean energy on core-containing balls) no longer applies to the smoothed geometry. Thus the fibered-rank information is still needed on a positive volume, and smoothing has not supplied it — it has only upgraded the ambient regularity in which the rank question is posed. The note's §5.1/§7 lines ("collapsed bounded-curvature structure after smoothing still requires cover/noncollapse/fiber-rank information") acknowledge this, but the specific point that the A03 rank-0 model **survives the smoothing** and is no longer excluded by energy should be stated, because it is the single mechanism that keeps route A from closing.

### 5. What is supported, what is an assumption to avoid

Supported and correctly used:
- The §3 dimensionless-smallness computation (with the maximal-function reading of §2 above).
- Li Theorem 3.6 as an all-centers complete-manifold statement; the note does not assume a one-good-ball version.
- The bilipschitz control (3.8) and the fixed-time curvature bound $C/t$ as the CFG input; Remark 3.2 (the $n\ge3$ version with $L^{n/2}$) shows the mechanism is not dimension-four-special, though the removal of the Sobolev/volume input via Cheeger–Tian is.

Assumptions that would be unsupported if inserted silently:
- Applying Li globally on the closed LeBrun manifold (smallness fails on a positive-fraction high-energy set; §2 above).
- Treating the interior/collar-confined existence as a corollary of Li's global maximality argument (it is a pseudolocality statement still to be proved).
- Propagating the pointwise near-Einstein/calibrated data through the flow using $|\operatorname{Rm}|\le C/t$ (the Grönwall integral diverges at $t\to0$; §3(a)).
- Reading CFG/collapse as giving noncollapsed covers everywhere rather than on the regular stratum (the bounded-curvature rank-0 Taub–NUT evasion; §4).
- Using Wang pseudolocality or Huang–Wang as drop-in collapse-compatible local existence (both re-import a volume/isoperimetric or model+rank hypothesis).

Two concrete repairs that would materially advance the route:
1. **An interior Li estimate.** Prove: dimensionless smallness on $B_{\beta r_*}(p)$ plus $|\operatorname{Ric}|\le K$ implies $|\operatorname{Rm}(g(t))|\le C/t$ on $B_{\beta r_*/2}(p)$ for $t\le\theta r_*^2$, with constants independent of the exterior, by confining the exterior high-energy influence to a $\sqrt t$-collar. This is the analytic heart and is stated by no cited source in the collapse setting.
2. **A regular-stratum positive-volume statement after smoothing.** Prove that on a positive volume proportion of the smoothed good region the CFG N-structure has fibered rank $\ge1$ (equivalently, that the rank-0 stratum, now of bounded curvature, has vanishing volume proportion or carries a lower bound on the defect $F$). This is precisely the input that turns (S) into a positive-volume fact and thereby closes the Derdziński contradiction.

Reduced to one line: smoothing legitimately trades the bounded-Ricci collapse difficulty for the classical bounded-curvature collapse theory and needs the flow only to deliver noncollapse of a normal cover for the original metric; the two things it does not by itself deliver are the collapse-compatible interior existence and the exclusion of bounded-curvature rank-zero collapse on positive volume, and the note faithfully identifies the first while understating that the second persists after smoothing.