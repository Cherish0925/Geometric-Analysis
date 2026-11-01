# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Knowledge/objects/papers/Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--e569e9d1f954--5258e72d2de1/object.md"
  ]
}
```

## Task

Read the Step-50 note, Anderson orbifold compactness source, GV critical-metric source, and the existing link-charge note. Verify Theorems 50.B–C under a legitimate scale-compatible residual hypothesis and uniform noncollapse/Sobolev input. Check: point-picking and passage to exact P-critical limits; scalar-flatness of ALE bubbles; lower semicontinuity/energy identity; exact APS charge formula and Burns/Eguchi-Hanson/Kronheimer tests; topology of multiple-end/reducible bubbles; Seiberg-Witten connected-sum split; b1 sign in the pure Γ=1 negative-definite charge; claims of sharp equality/attainment of the bulk infimum; and the certified-cell alternatives. Produce a corrected conditional structure theorem that uses Theorem G/link charges without asserting more topology or equality than follows.

## Output

# Verification memo: Theorems 50.B–C, the bubble tariff, and the certified-cell alternatives

## 0. Summary

Theorems 50.B–C rest on a sound architecture. A scale-adapted residual makes every rescaled limit exactly $P$-critical. Anderson's orbifold theory then applies to those limits, and Theorem G prices what concentrates. Seven specific points in the note need correction or completion:

1. **Missing linear ε-regularity.** The ε-regularity step proves only that the curvature scale cannot collapse. It does not prove the linear-in-energy form of Anderson's (1.5).
2. **Sobolev constant, not volume ratio.** Anderson's critical-metric ε-regularity (Lemma 3.3, Prop. 3.5) depends on the Sobolev constant $c_S$, not on $\nu_0$.
3. **Per-bubble charge.** The per-bubble charge omits the inner orbifold-link terms. It is correct only for smooth single-ended bubbles.
4. **$b_1$ sign.** The $b_1$ correction has the wrong sign: the charge is $k_b+4b_1$, not $k_b-2b_1$.
5. **Topology of the resolution.** The decomposition $M\cong V\#\hat N_1\#\cdots$ holds only for separating single-cone $\Gamma=1$ points, with $\hat D$ (the capped region) in place of $\hat N$.
6. **Equality and attainment.** These follow only under additional standardness and insertion inputs.
7. **Certified-cell alternatives.** Two of the listed escape channels ($b_1>0$, multi-cone necks) are priced at $\ge4$ and are therefore excluded. The $\Gamma\ne1$ channel is genuinely cheap.

A corrected statement is given in §9.

## 1. The two hypotheses that make 50.B–C a theorem

**(H1) Scale-adapted Palais–Smale.**

- $\mathrm{Vol}(g_i)=1$ and $P(g_i)\to\alpha(M)$.
- With $\rho_i$ the capped curvature scale, $\varepsilon_i:=\int\rho_i^4|\nabla P(g_i)|^2d\mu\to0$.
- Derivative bounds hold: $|\nabla^j\mathrm{Rm}(g_i)|\le C_j\rho_i^{-2-j}$.

Scaling check: $|\nabla P(\lambda^2g)|_{\lambda^2g}=\lambda^{-4}|\nabla P(g)|_g$, so $r^4\int_{B_r}|\nabla P|^2$ is scale invariant, as the note states. On a point-picked ball one has $\rho_{g_0}\ge c\,r_{g'}\ge\tfrac c2 r(y_i)$. Hence the rescaled residual is at most $C\varepsilon_i$, and it tends to zero exactly because $P(g_i)\to\alpha$.

Theorem 50.A produces (H1) from any minimizing sequence, but only through Lemma W, which is a sketch. The real content of Lemma W is a local curvature-scale preservation statement for a fourth-order flow:

> If $r_{g_0}\ge\rho$ on $B(x,A\rho)$, then $|\mathrm{Rm}_{g_t}|\le2\rho^{-2}$ on $B(x,\rho)$ for $t\le c_0$.

No maximum principle is available here. This requires cut-off energy estimates of Streets/Kuwert–Schätzle type, adapted to the 1-Lipschitz weight. That is the analytic object to be written. The corrected theorem below takes (H1) as hypothesis, so it is independent of how Lemma W is finished.

The bi-Lipschitz bound $C^{-1}g_0\le g\le Cg_0$ correctly gives volume ratios $\ge\nu_0C^{-4}$. It also preserves a Sobolev constant up to a factor $C^{O(1)}$.

**(H2) Uniform Sobolev constant** (Anderson (3.1), $c_S\ge c>0$). This is the right second input, for three reasons:

- Anderson's Lemma 3.3 and Prop. 3.5 are stated with $\delta_0,C_0$ depending on $c_S$. Remark 3.10 says (1.4) "must be assumed" but gives no $\nu_0$-only constants. Step 50.B writes "constants depending on $\nu_0$", which the source does not supply. The proof of Lemma 3.3 plausibly needs only the local Sobolev inequality in an $L^{2,p}$-harmonic chart, which noncollapse provides. That variant is unwritten.
- Sobolev implies the volume lower bound (Anderson §3.1), so (H2) contains (NC).
- (H2) passes to all rescaled limits, and through Prop. 3.6 it forces single cones at every point whose link separates.

Without (H2), Anderson's Remark 2.9 shows wedge-type reducible limits even for separating links.

## 2. ε-regularity and passage to exact critical limits

The Step-50.B contradiction argument is correct for what it actually proves.

**Claim A (no scale collapse).** There exist $\delta_0,K$ such that $\int_{B(x,r)}|\mathrm{Rm}|^2\le\delta_0$ implies $r^2\sup_{B(r/2)}|\mathrm{Rm}|\le K$.

The argument runs as follows:

- Point-picking yields $y_i$ with $r_{g'}\ge\tfrac12r(y_i)$ on $B(y_i,A_ir(y_i))$.
- The derivative bounds give $C^\infty$ Cheeger–Gromov convergence; noncollapse supplies the injectivity radius.
- The limit is complete, has infinite volume, satisfies $\nabla P=0$, and has energy $\le\delta_0$.
- Its scalar curvature is $L^2$-harmonic, hence $0$.
- Prop. 3.5 (given (H2)) applied on balls of radius $r\to\infty$ forces flatness, contradicting $|\mathrm{Rm}(y_\infty)|\sim1$.

**What the note does not prove.** It does not prove the *linear* estimate (1.5): $\sup_{B(r/2)}|\mathrm{Rm}|\le(C_0\,\mathrm{vol}^{-1}\int|\mathrm{Rm}|^2)^{1/2}$. Consider a sequence with bounded scale-curvature in which the energy and the curvature both tend to zero, with the ratio of curvature to $\sqrt{\text{energy}}$ unbounded. Its rescaled limit is flat, so there is no contradiction. For approximate solutions, the residual enters $D^*D\,\mathrm{Ric}+\mathrm{Rm}*\mathrm{Ric}=(\text{residual})$ as an inhomogeneous term, and linear control by energy alone is not expected.

**Repair.** Replace (1.5) by a modulus.

> **Claim B.** For every $\eta>0$ there are $\delta(\eta)$ and $i_0(\eta)$ such that energy $\le\delta(\eta)$ on $B(x,r)$ implies $r^2\sup_{B(r/2)}|\mathrm{Rm}|\le\eta$ for $i\ge i_0$.

Proof: Claim A plus smooth subconvergence. A limit with zero energy on $B(1)$ is flat on $B(1)$. No residual is needed.

Anderson's proof of Theorem 1.1 uses (1.5) in three places:

- the curvature bound (2.7) on the good set, for which Claim A suffices;
- the decay (2.12) on annuli at singular points, for which Claim B suffices, or the exact criticality of $g_\infty$;
- Theorem 1.2 applied to complete rescaled limits.

Those limits are exactly critical on their regular parts. The weighted residual makes $\nabla P\to0$ in $L^2_{loc}$ on the regular part of every rescaled limit at every scale simultaneously. They therefore satisfy the linear (1.5) by Prop. 3.5 under (H2).

So Theorem 1.1 holds for the tail sequence after re-running Anderson's argument with (A)+(B). The note's sentence "no approximate-critical ε-regularity needs to be invented" should read "only the modulus form, which needs no residual, enters".

## 3. Scalar curvature of limits

$P=\mathcal F_{-1/4}$, which corresponds to $t=\tfrac16$ in the Gursky–Viaclovsky (GV) parametrization. I checked this from GV (1.5) and (3.8)–(3.10): $\int|\mathrm{Ric}^\circ|^2=\tfrac12\mathcal B_{1/6}-16\pi^2\chi$. The trace of $B^t=0$ gives $-6t\Delta R=-\Delta R=0$.

On the regular part of $V$ and of each bubble, $R$ is harmonic and lies in $L^2$. Near an orbifold point, $r^2|R|=o(1)$. Take the logarithmic cut-off $\eta$ on $\{\epsilon^2<r<\epsilon\}$. Then
$$\int\eta^2|\nabla R|^2\le4\int R^2|\nabla\eta|^2\le o(1)\cdot\frac{\log(1/\epsilon)}{\log^2(1/\epsilon)}\to0 .$$
Hence:

- $R$ is constant on each component of $V_0$. The constants may differ across components joined at a reducible point.
- On bubbles (infinite volume), $R\equiv0$. Then $C=0$, so $B=0$: the bubbles are Bach-flat and scalar-flat.

This settles the note's scalar-flatness assertion, with the cut-off argument replacing an orbifold removable-singularity theorem.

## 4. Lower semicontinuity and energy identity

$\alpha\ge P(g_\infty)+\sum P(\text{limits})$ is valid as a Fatou statement. The density $|\mathrm{Ric}^\circ|^2\ge0$ is integrated over disjoint compact regions: the bulk compact sets $K\subset V_0$ and the rescaled compact sets in each bubble's regular part. These regions are scale-separated for large $i$, and convergence is smooth on each.

No neck-energy identity is proved, and none is needed for the lower bound. The identity becomes a consequence in the equality branch (§7).

## 5. Charges: the region form of Theorem G

**Correct mechanism.** Do not price limiting bubbles. Price compact regions $D_{q,i}\subset M$ whose link components are taken at a fixed small radius $r$ around each cone of $q$.

For fixed $r$ and large $i$, $g_i$ on $A_q(r/2,2r)$ is $C^k$-close to $g_\infty$. As $r\to0$, the metric $g_\infty$ is $C^k$-close to the flat cone $C(S^3/\Gamma)$: Anderson gives $C^{1,\alpha}$ tangent-cone convergence, together with $r^2|\mathrm{Rm}|\to0$ and $|\nabla^j\mathrm{Rm}|\le C_jr^{-2-j}$, and interpolation. This is the $C^2$ collar regularity that Step 33 §2 identifies as sufficient. For a noncollapsed neck there is no Dai adiabatic term. The odd signature operator's kernel is topological, so $\mathcal H=\eta+\int T_{p_1}$ varies continuously.

Theorem G on $D$, keeping the terms $\int|W^\pm|^2$ and $\int s^2$ (both $\ge0$), gives
$$\widehat P(g_i;D)=\tfrac1{2\pi^2}\!\int_D|W^\pm|^2+\tfrac1{96\pi^2}\!\int_Ds^2+\sum_{c}\Bigl(\tfrac2{|\Gamma_c|}\mp3\eta_{\Gamma_c}\Bigr)-(2\chi\pm3\tau)(D)+o(1).$$

Three consequences:

- Scalar-flatness of bubbles is not needed for the lower bound.
- The region $D$ contains every deeper level, including $\Gamma'\neq1$ bubbles inside a $\Gamma=1$ tree, and has honest topological $\chi$ and $\tau$.
- The note's per-bubble formula is correct only for smooth single-ended bubbles. An orbifold bubble with an interior point of group $\Gamma'$ needs the inner-link term $-(2/|\Gamma'|\mp3\eta_{\Gamma'})$. With those terms included, the per-level bounds telescope, and $\sum_b\max_\pm\ge\max_\pm\sum_b$. The per-level version is therefore at least as strong as the region version, but only once the inner terms are present.

**Topological charges.** Let $\Gamma=1$ on all $m$ links of $D$. Let $D_{\rm cap}$ be $D$ with balls glued to every link, with invariants $b_1$, $b^+=p$, $b^-$. Then

$$\mathfrak c(D)=\Bigl[\,4(m-1)+4b_1+\max(b^--5p,\;p-5b^-)\Bigr]_+ .$$

- For $m=1$ and $p=0$ (Donaldson diagonal, any $\pi_1$): $\mathfrak c=b_2+4b_1$.
- Pure neck $S^3\times I$: $\mathfrak c=4$.
- $S^1\times S^3$ handle: $4$, matching (G1).

**The $b_1$ sign.** The note's $k_b-2b_1$ is wrong. Since $\chi(D)=1-2b_1+b_2$, one gets $2-2\chi+3|\tau|=b_2+4b_1$. The check $D=(S^1\times S^3)\setminus B$ gives $4$, consistent with Step 33. Topology in $b_1$ raises the price.

**Saturation tests** (all in the complex orientation, $W^+=0$, $s=0$, so Theorem G is an identity):

| Space | Data | Prediction |
|---|---|---|
| Burns | $\chi=2$, $\tau=-1$, $\Gamma=1$ | $\widehat P=2-1=1$ |
| Eguchi–Hanson | $\Gamma=\mathbb Z_2$, $\chi=2$, $\tau=-1$ | $\widehat P=0$ iff $\eta_{\mathbb Z_2}=0$, which is correct for $\mathbb{RP}^3$ |
| Kronheimer, $\Gamma\subset SU(2)$, rank $r$ | $\chi=1+r$, $\tau=-r$ | $\widehat P=0$ iff $\eta_\Gamma=(r-2+2/|\Gamma|)/3$ |

For $A_{p-1}$ the last condition reads $\eta=(p-1)(p-2)/3p$. This is the APS cotangent sum $\tfrac1p\sum\cot^2(\pi k/p)$ for $L(p,-1)$. The charge convention is therefore consistent, with $\mathfrak c=\widehat P=0$ for every Kronheimer space.

**An additional test for $U(2)$ groups.** Orientation reversal gives $\eta(S^3/\mathbb Z_n(1,1))=-(n-1)(n-2)/3n$. Theorem G then predicts, for LeBrun's scalar-flat Kähler metric on $\mathcal O(-n)$,
$$\widehat P=\frac{(n-2)^2}{n}:\qquad 1,\ 0,\ \tfrac13,\ 1\quad\text{for } n=1,2,3,4,$$
which reproduces Burns at $n=1$ and Eguchi–Hanson at $n=2$. A one-variable integration of LeBrun's explicit $U(2)$-invariant metric would independently fix the $\eta$ sign for non-$SU(2)$ links. These are exactly the links relevant to the $\Gamma\ne1$ alternatives.

## 6. Topology of the resolution

The decomposition is $M=M^{\rm bulk}\cup\bigcup_qD_q$, glued along the links. Four points:

- **Separation and single cones.** If a link is nonseparating, then $b_1(M)\ge1$, since intersection with the link defines a nonzero homomorphism $H_1\to\mathbb Z$. If $b_1(M)=0$, all links separate, and (H2) with Prop. 3.6 (rescaled to every level) forces single cones and one-ended bubbles. Multi-cone points and multi-end bubbles produce handles. They are priced at $\ge4$ per extra $\Gamma=1$ end.
- **Connected sums.** For a separating single-cone point with $\Gamma=1$, $M\cong\hat V\#\hat D_q$. The correct summand is $\hat D$, not $\hat N_b$: a $\Gamma=1$ tree may contain $\Gamma'\ne1$ levels, so the one-point compactifications of individual bubbles need not be manifolds.
- **Lattice cancellation.** $Q_{\hat V}\oplus(-I_K)\cong Q_X\oplus(-I_k)$ yields $Q_{\hat V}\cong Q_X\oplus(-I_{k-K})$ only when indefinite odd cancellation applies, that is $k-K\ge1$ or matching parity. In general it yields only rank, $b^\pm$, and parity data. "$\hat V$ has the intersection form of $X\#k'\overline{\mathbb{CP}}^2$" should be restated accordingly.
- **Fundamental group.** $\pi_1(M)=\pi_1(\hat V)*\ast_q\pi_1(\hat D_q)$.

## 7. Seiberg–Witten split, attainment, and equality

**SW split.** The setting is $b^+(M)\ge2$ with $SW\ne0$, as for $X$ minimal of general type plus the blow-up formula. For separating spherical-space-form links, one piece carries all of $b^+$, and every other piece has $b^+=0$. The neck-stretching vanishing argument covers any link admitting positive scalar curvature, so this extends beyond $S^3$ to $S^3/\Gamma$. By additivity, $b^+(\hat V)$ or one $b^+(\hat D_q)$ equals $b^+(M)$.

The note's alternative "$b^+(V)=0$" should read: $b^+(\hat V)=0$, exactly one $\hat D$ carries $b^+$, and the others are definite with $b^+=0$. Donaldson diagonalization applies to the closed $b^+=0$ pieces for arbitrary $\pi_1$ (Donaldson 1987). Nothing analogous is available for pieces with a lens link.

**Attainment without concentration.** This holds as stated in Theorem 50.C(1): smooth convergence on $M$ and continuity of $P$.

**Zero gap.** $\alpha=0$ forces $P(g_\infty)=0$, so $g_\infty$ is Einstein on each component of $V_0$, and the bubbles are Ricci-flat ALE. A Ricci-flat bubble with $\Gamma=1$ at infinity has volume ratio $1$ at both ends of Bishop–Gromov from a regular point, so it is flat. Hence concentration occurs only at $\Gamma\ne1$ points, which sharpens 50.C(2). If $V$ has no singular points, $M$ carries an Einstein metric.

**Equality branch.** Assume every concentration point has $\Gamma=1$, a single separating link, $b^+(\hat D_q)=0$, $b_1(\hat D_q)=0$, $\hat D_q\cong\#k_q\overline{\mathbb{CP}}^2$, and Theorem F's Burns insertion bound $\alpha(\hat V\#K\overline{\mathbb{CP}}^2)\le\alpha(\hat V)+8\pi^2K$ for arbitrary backgrounds. Smoothing $g_\infty$ at its $\Gamma=1$ points costs $o(1)$ in $P$, since $|g-\delta|+r|\partial g|+r^2|\partial^2g|\to0$. This gives $P(g_\infty)\ge\alpha(\hat V)$. Then
$$\alpha(\hat V)+8\pi^2K\ge\alpha(M)\ge P(g_\infty)+8\pi^2K\ge\alpha(\hat V)+8\pi^2K .$$
So equality holds throughout, $g_\infty$ attains $\alpha(\hat V)$ (as a metric smooth off finitely many points, $C^0$ there), and $\int_{D_i}(|W^+|^2+s^2)\to0$. Neck energy outside $K\cup D$ tends to $0$: the energy identity is a consequence in this branch.

Without $\hat D_q$ being standard, only the inequality survives, and "attained on $V$" is unproved. Smoothness of the attaining metric needs a removable-singularity theorem for $P$-critical metrics at $\Gamma=1$ points.

**Theorem 50.C(4).** "Scalar-flat bubbles never save" is false as stated. Kronheimer bubbles carry $(-2)$-classes at cost $0$, and the LeBrun $\mathcal O(-3)$ bubble costs $1/3$. The correct statement is: $\Gamma=1$ single-link regions with $b^+=0$ cost $\ge b_2+4b_1$, saturated only by $W^+=0$, $s=0$.

## 8. The certified cell on $X\#\overline{\mathbb{CP}}^2$

**Numerical inconsistency.** Step 50 uses $\widehat P\le0.995662732771115$ (the $x_0=.03$, $X=128$ row). Step 33 uses $p_*=0.995848$. Both are below $1$, so the logic is unaffected, but the interval-certified value should be the one quoted.

**Fundamental group.** A cocompact lattice in $PU(2,1)$ is one-ended (its Gromov boundary is $S^3$), so by Stallings it is freely indecomposable. Therefore either every $\hat D_q$ is simply connected, or $\pi_1(\hat V)=1$ and a single $\hat D$ carries $\pi_1(X)$. The hypothesis $b^+(X)\ge2$ holds on covers.

**Corrected alternatives** under (H1)+(H2), with $\sum_q\mathfrak c(D_q)\le\widehat P(M)-\widehat P(g_\infty)<1$:

- **Excluded:**
  - any $\Gamma=1$ region with $b^+=0$ and $b_2\ge1$ (cost $\ge1$);
  - any $\Gamma=1$ region with $b_1\ge1$ (cost $\ge4$);
  - any multi-cone or multi-end $\Gamma=1$ configuration (cost $\ge4$).

  The note's "bubble with $b_1>0$" escape is closed. This reproduces Step 33 Cor. G3, now with links supplied by the bubble-tree necks.
- **(A) No concentration.** $\alpha$ is attained by a smooth $B^{1/6}$-flat, constant-scalar metric on $M$.
- **(B) Rational-homology-ball concentration only.** Every $\Gamma=1$ region has $b_2=b_1=0$ (charge $0$). If $\pi_1$ sits in $\hat V$, the $\hat D_q$ are homotopy 4-spheres, so $\hat V$ is homeomorphic to $M$ (Freedman) and $Q_{\hat V}\cong Q_M$. The exceptional class lives in a critical bulk with $P(g_\infty)<8\pi^2$. The note's "homotopy-sphere summands" is correct here, but only through Stallings plus Freedman. Diffeomorphism is not obtained.
- **(C) Transfer of $b^+$.** One $\Gamma=1$ region carries all of $b^+(M)$, and $\hat V$ is definite with $b^+=0$. The topological charge is useless here: the $+$ side is $4-(2\chi+3\tau)(\hat D)$, and $(2\chi+3\tau)(\hat D)$ is large for ball quotients.

  What could price (C) is a localized LeBrun estimate. $\int|\omega^+|^2$ is conformally invariant, so the self-dual projection of the basic class concentrates at bubble scale, while the bubbles are scalar-flat. The lower bound $\int s^2\ge32\pi^2(c_1^+)^2$ must then be paid by the neck or by the bulk constant $R_\infty$. Noncollapsed necks supply link regularity (a) and (c) of Step 33 for free. Only the SW flux and Chern–Simons terms on the near-flat neck remain.
- **(D) $\Gamma\ne1$ concentration.** Some point has a lens link. This branch is genuinely open and cheap:
  - a rational ball with link $L(4,1)$ has $\mathfrak c=\tfrac12-2+\tfrac32=0$;
  - the $\mathcal O(-3)$ topology has $\mathfrak c=\tfrac13$.

  For a ball quotient, an $\mathcal O(-3)$-type region needs a class of square $-3$ with spherical or link-compatible representative. This is not supplied by $\pi_2(M)=\langle E\rangle$-type spheres, and its realizability is unsettled.
- **(E)** The uniform Sobolev constant degenerates. This includes collapse and is broader than "collapses somewhere".

## 9. Corrected conditional structure theorem

Let $M$ be a closed oriented 4-manifold and $g_i$ a minimizing sequence satisfying (H1) and (H2). After passing to a subsequence:

**(i) Convergence.**

- The modulus ε-regularity (A)+(B) holds.
- $g_i$ converges, $C^\infty$ on compact subsets of $V_0$, to a compact orbifold $(V,g_\infty)$. The number of points and the local groups are bounded by $\chi$, $\alpha$, $c_S$.
- $g_\infty$ is $B^{1/6}$-flat on $V_0$, with $R$ constant on each component.
- Rescalings at each point give finitely many levels of complete ALE orbifolds. These are exactly $P$-critical, scalar-flat and Bach-flat.

**(ii) Decomposition.** $M=M^{\rm bulk}_i\cup\bigcup_qD_{q,i}$, where $M^{\rm bulk}_i\cong V\setminus\bigcup B_r(q)$ and the links $S^3/\Gamma_{q,c}$ (one per cone) converge after rescaling in $C^k$ to flat-cone collars.

- If $b_1(M)=0$, every $q$ has one cone.
- For a separating single-cone point with $\Gamma=1$, $M\cong\hat V\#\hat D_q$.

**(iii) Tariff.**
$$\alpha(M)\ge P(g_\infty)+8\pi^2\sum_q\mathfrak c(D_q),\qquad \mathfrak c(D)=\Bigl[\max_\pm\Bigl(\sum_c\bigl(\tfrac2{|\Gamma_c|}\mp3\eta_{\Gamma_c}\bigr)-(2\chi\pm3\tau)(D)\Bigr)\Bigr]_+ .$$
For $\Gamma=1$ links this takes the explicit form of §5. For Burns, Eguchi–Hanson, Kronheimer (and, predictively, LeBrun $\mathcal O(-n)$) the tariff is saturated with $W^+=0$, $s=0$.

**(iv) SW split.** If $b^+(M)\ge2$, $SW(M)\ne0$, and all links separate, then exactly one piece carries $b^+(M)$. Closed pieces with $b^+=0$ have diagonal forms.

**(v) Attainment and zero gap.**

- With no concentration, $\alpha(M)$ is attained by a smooth critical metric on $M$.
- If $\alpha=0$, concentration occurs only at $\Gamma\ne1$ points, with Ricci-flat ALE bubbles and an Einstein orbifold bulk.
- The equality branch of §7 holds under its stated standardness and insertion inputs.

**(vi) Application.** For $X\#\overline{\mathbb{CP}}^2$ with $X$ a ball quotient admitting the certified cell, the outcomes are exactly (A)–(E) of §8.

## 10. Items not resolved by the supplied material

1. Lemma W as a localized fourth-order curvature-scale estimate; this is the only route from arbitrary minimizing sequences to (H1).
2. A $\nu_0$-only version of Anderson's Lemma 3.3, which would replace (H2) by (NC) wherever irreducibility is not used.
3. A removable-singularity theorem for $P$-critical metrics at orbifold points, needed for smoothness of attaining metrics.
4. The $\eta$ sign for $U(2)$ links, checkable via the LeBrun $\mathcal O(-n)$ integral.
5. The localized LeBrun estimate pricing branch (C).
6. Realizability and pricing of branch (D) inside ball-quotient blow-ups.
7. The collapsed/Sobolev-degenerate regime (E): the ALF/Taub–NUT link charges $(-2,2)$ of Step 33 enter there, and none of §§2–9 applies.