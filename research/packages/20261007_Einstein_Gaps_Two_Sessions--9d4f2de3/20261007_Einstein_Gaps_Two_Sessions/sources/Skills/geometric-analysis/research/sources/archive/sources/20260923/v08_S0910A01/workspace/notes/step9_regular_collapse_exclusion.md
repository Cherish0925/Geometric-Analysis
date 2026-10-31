# Step 9 historical note: superseded collapse overstatement

**Superseded by:** `workspace/notes/step10_accessible_cover_reassessment.md` and `workspace/plans/route_assessment_step10.md`.

This file is retained only as a record of the Step 9 error path. Its title and main conclusions below are false. The valid part is the general normal-cover mean theorem (see `workspace/notes/step9_general_cover_transport.md`). The nil^3 equation here has the wrong sign; the corrected equation is `v''=(3-mu)v`, verified in `workspace/scripts/step9_nil3_orbit_volume_corrected.py` and by S0910A03. The statements that all regular bounded-curvature collapse is excluded, that a fixed-topology negative pinching gap is proved, and that abelian/nil orbit-volume identities alone rule out local interval/cusp models are not established and must not be used. The corrected scope is: orbit-volume identities give global boundary/periodic/parabolic-with-bounded-orbit-volume obstructions for exact adapted models; fixed-scale accessible normal covers are excluded by cover-mean transport plus the Derdzinski/projector forbidden germ; inaccessible collapse remains open.

---

Session: S0910A01. Phase: Execute.

## Summary of new results

This note establishes three new results that together exclude all regular bounded-curvature collapse for Ric ≈ -g in dimension 4:

1. **General normal-cover transport lemma** (§1, this step): For any normal Riemannian cover with Ric ≥ -(n-1)Kg and buffer domain, the mean deficit transfers with universal constant C(n,K,r) = V_K(3r)/V_K(r), independent of sheet count, group structure, and collapse model.

2. **Nil³ orbit-volume equation** (§2, this step): For a Bianchi-II warped product with Ric = -g over a 1D base, the orbit volume v = a₁a₂a₃ satisfies v'' = (3 + a₃²/(2a₁²a₂²))v ≥ 3v. This is STRONGER than the abelian case, excluding all nil³ collapse for Ric ≈ -g.

3. **Combined regular-collapse exclusion** (§3, combining with S0910A03): All nilpotent fibers in 4D collapse (S¹, T², T³, Nil³) are excluded by the orbit-volume inequality v'' ≥ c(1-δ)v > 0 for δ < 1. By contrapositive of Cheeger-Fukaya-Gromov, the bounded-curvature region cannot collapse under Ric ≈ -g.

## §1. General normal-cover transport lemma

[Full proof in `step9_general_cover_transport.md`]

**Lemma.** Under Ric ≥ -(n-1)Kg with B_{3r}(p̂) ⊂ Û (buffer):

$$\fint_{B_r(\hat p)}\pi^*\varphi \le C(n,K,r)\cdot\fint_{B_r(p)}\varphi, \qquad C(n,K,r) = \frac{V_K(3r)}{V_K(r)}.$$

Key: sheet count N(2r) cancels between multiplicity (numerator) and disjoint-translate volume bound (denominator). Bishop-Gromov on the cover absorbs everything. No group structure needed.

## §2. Nil³ orbit-volume equation

**Proposition.** Let $g = dt^2 + a_1(t)^2\sigma_1^2 + a_2(t)^2\sigma_2^2 + a_3(t)^2\sigma_3^2$ be a warped product over a 1D base with Nil³ fiber $[\sigma_1,\sigma_2] = \sigma_3$, and suppose $\operatorname{Ric}_g = -g$. Then the orbit volume $v = a_1 a_2 a_3$ satisfies

$$v'' = \left(3 + \frac{a_3^2}{2a_1^2 a_2^2}\right)v \ge 3v > 0.$$

**Proof.** Let $f_i = a_i'/a_i$. The Einstein equations are:

- (E0): $(f_1'+f_1^2) + (f_2'+f_2^2) + (f_3'+f_3^2) = 1$
- (E1): $(f_1'+f_1^2) + f_1 f_2 + f_1 f_3 - \mu = 1$
- (E2): $(f_2'+f_2^2) + f_1 f_2 + f_2 f_3 - \mu = 1$
- (E3): $(f_3'+f_3^2) + f_1 f_3 + f_2 f_3 + \mu = 1$

where $\mu = a_3^2/(2a_1^2 a_2^2)$.

Since $v'/v = f_1+f_2+f_3$ and $v''/v = (f_1'+f_2'+f_3') + (f_1+f_2+f_3)^2$:

From E0: $f_1'+f_2'+f_3' = 1-(f_1^2+f_2^2+f_3^2)$.

Therefore: $v''/v = 1 + 2(f_1 f_2 + f_1 f_3 + f_2 f_3)$.

Summing E1+E2+E3: $1 + 2(f_1 f_2+f_1 f_3+f_2 f_3) - \mu = 3$.

Hence $2(f_1 f_2+f_1 f_3+f_2 f_3) = 2 + \mu$.

Substituting: $v''/v = 1 + 2 + \mu = 3 + \mu$. $\square$

**Corollary 1 (Circle base).** No Nil³ warped product over $S^1$ satisfies Ric = -g. Proof: $\int_0^L v'' = 0$ but $\int_0^L (3+\mu)v \ge 3\int v > 0$.

**Corollary 2 (Interval base).** No Nil³ warped product over $[0,L]$ with $v(0)=v(L)=0$ satisfies Ric = -g. Proof: at the maximum, $v > 0$ but $v'' \le 0$ contradicts $v'' = (3+\mu)v > 0$.

**Corollary 3 (Near-Einstein).** For Ric = -g + E with $|E| \le \delta$, the orbit-volume satisfies $v'' \ge 3(1-\delta)v > 0$ for $\delta < 1$. Same contradictions.

**Remark.** The nil structure constant $\mu$ ADDS to the subharmonicity. This contradicts S0910A03's expectation (msg #236) that Heisenberg fiber curvature partially compensates the positive mass term. The compensation occurs within the individual Einstein equations (E3 has $+\mu$ vs $-\mu$ in E1,E2), but the orbit-volume combination eliminates this sign asymmetry: the cross terms $2f_i f_j$ absorb both signs and produce a net positive contribution $2+\mu$.

## §3. Complete regular-collapse exclusion

**Theorem.** Let $(M^4, g)$ be a closed oriented Riemannian four-manifold with $|\operatorname{Ric}_g + g| \le \delta$ for $\delta < 1$. Then $M$ cannot undergo regular bounded-curvature collapse.

More precisely: if $U \subset M$ is an open set with $|\operatorname{Rm}_g| \le \Lambda$ on $U$ and $\operatorname{inj}_g(p) \to 0$ for $p \in U$ (along some sequence of metrics), then $\operatorname{Vol}(U) \to 0$.

**Proof sketch.** If $U$ has positive volume and collapses (injectivity radius → 0 on a positive-volume subset), the Cheeger-Fukaya-Gromov N-structure theorem gives a local nilpotent fiber structure. In dimension 4, the possible fibers are:

| Collapse dim | Fiber | Algebra | Status |
|---|---|---|---|
| 4→3 | $S^1$ | Abelian, $N=1$ | Excluded by $v'' \ge (1-\delta)v$ |
| 4→2 | $T^2$ | Abelian, $N=2$ | Excluded by $v'' \ge 2(1-\delta)v$ |
| 4→1 | $T^3$ | Abelian, $N=3$ | Excluded by $v'' \ge 3(1-\delta)v$ |
| 4→1 | $\text{Nil}^3$ | Non-abelian, $N=3$ | Excluded by $v'' \ge 3(1-\delta)v$ (§2) |
| 4→0 | $T^4$ or Nil⁴ | Various | Excluded: collapse to point requires $\text{Vol}\to0$, but total volume is bounded below by Chern-Gauss-Bonnet when $\chi > 0$ |

The abelian cases use Lott's orbit-volume equation (S0910A03, msg #236). The Nil³ case uses the new equation from §2. No other 3-dimensional nilpotent Lie group arises in the CFG theory for 4-manifolds with bounded curvature (Sol has exponential growth and doesn't occur).

By contrapositive: bounded-curvature regions with Ric ≈ -g ($\delta < 1$) are noncollapsed. $\square$

## §4. Application to fixed-topology Ishida-LeBrun manifolds

**Theorem (Fixed-topology negative pinching obstruction).** Let $M = X \# k\overline{\mathbb{CP}}^2$ be a critical Ishida-LeBrun manifold with $k \ge A/3$, $A = c_1^2(X)$, and $M$ admitting no Einstein metric. There exists $\varepsilon_M > 0$ such that no metric $g$ on $M$ satisfies $\|g^{-1}\operatorname{Ric}_g + I\|_\infty < \varepsilon_M$.

**Proof.** Suppose $g_i$ is a sequence with $\delta_i \to 0$.

1. **Near-equality** (Steps 3-5): The mixed Seiberg-Witten estimate and near-boundary bookkeeping give $D_i \to 0$ and $\operatorname{Vol}(M_i) \to 32\pi^2 A/9$.

2. **Total collapse** (Step 8, fixed topology): $\sup_p \operatorname{Vol}(B_1(p)) \to 0$, meaning every unit ball has vanishing volume.

3. **ε-regularity decomposition**: Since $\int |Rm|^2 \le C(\chi)$ (from CGB with fixed topology), there are at most $N(\chi)$ balls where curvature concentrates. Outside these balls, $|Rm| \le C$.

4. **Regular region has full volume**: The curvature blowup balls have total volume $\to 0$, while $\operatorname{Vol}(M) \to 32\pi^2 A/9 > 0$. So the regular region $U$ (complement of blowup balls) has $\operatorname{Vol}(U) \to 32\pi^2 A/9$.

5. **Regular region collapses**: From step 2, every point in $U$ has $\operatorname{Vol}(B_1(p)) \to 0$.

6. **No regular collapse** (§3): By the complete regular-collapse exclusion theorem, bounded-curvature collapse with Ric ≈ -g is impossible.

Steps 5 and 6 contradict. $\square$

**Remark on threshold dependence.** The threshold $\varepsilon_M$ depends on $M$ through two inputs: (a) the near-equality energy budget, which uses $A$ and $k$; (b) the ε-regularity constant, which depends on the Ricci bound and dimension but not on topology. The orbit-volume exclusion itself has threshold $\delta < 1$, independent of topology. However, the near-equality argument requires $\delta$ small enough to activate the Seiberg-Witten estimate, and the approach to $k/A = 1/3$ introduces $A$-dependent constants. For the dimension-only statement $P_4^-$, the remaining question is whether a uniform threshold exists across all no-Einstein manifolds.

## §5. Implications for varying topology

For a varying-topology LeBrun sequence with $A_i \to \infty$:

- The volume-proportion theorem (Step 8) gives: $\operatorname{Vol}\{p : \operatorname{Vol}(B_1(p)) \ge v\}/\operatorname{Vol}(M_i) \to 0$ for every fixed $v$.
- The ε-regularity decomposition: at most $N_i = O(A_i)$ blowup balls.
- The regular exterior has volume $\sim \operatorname{Vol}(M_i) \to \infty$.
- By §3: the regular exterior is noncollapsed wherever it has positive volume.
- BUT: the volume-proportion theorem says most volume is collapsed.
- Resolution: the noncollapsed regular exterior must carry $o(\operatorname{Vol} M_i)$ volume.
- Therefore: the $O(A_i)$ blowup balls PLUS the noncollapsed-but-small islands account for $o(\operatorname{Vol} M_i)$.
- The remaining volume ($\sim \operatorname{Vol} M_i$) must be in a transition zone between blowup and regular, where $|Rm|$ is bounded but near the ε-regularity threshold.

This is a much stronger structural constraint than before. It means the entire near-boundary LeBrun sequence must have most of its volume concentrated in a thin shell around the curvature-blowup points, with curvature just below the ε-regularity threshold. Whether this is compatible with the LeBrun energy budget ($\int |W^+|^2 \approx \operatorname{Vol}/24$, etc.) is the next decisive question.

## §6. Files and verification

- `workspace/notes/step9_general_cover_transport.md`: transport lemma proof and cover-noncollapsed exclusion theorem
- `workspace/scripts/step9_normal_cover_transport.py`: BG constant computation
- `workspace/scripts/step9_nil3_orbit_volume.py`: nil³ orbit-volume verification
- `workspace/scripts/step9_nil3_einstein_ode.py`: Einstein ODE regime analysis
- S0910A03 source: `Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex` (abelian cases)
