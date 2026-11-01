# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/notes/spirit_step72_orbifold_scalar_transfer.md",
    "Sessions/S1003A01/workspace/notes/spirit_step73_mixed_curvature_transfer.md"
  ]
}
```

## Task

Verify, as a mathematician, the theorems in step74_orbifold_transfer_theorem.md. Focus on load-bearing points: (1) Theorem 74.A lower bound: is the use of A02's Lemma 86.S to transfer S>=32pi^2 A from smooth resolution metrics on X#kCPbar^2 to every orbifold metric on V_m=X#m(S^4/Z2) valid (orientation matching of Eguchi-Hanson so the resolution really is X#2m CPbar^2; chi_orb=A/3-m; tau_orb=A/9 with zero A1 eta; Gauss-Bonnet normalization 16pi^2 chi = S/12+2W-P)? Is the convex-combination argument for D_orb>=min{1,4k/(A+k)} correct? (2) Upper construction: is h=(1+r^-2)^2 delta with involution x->diag(-1,-1,-1,1)x/|x|^2 really the Green blow-up of S^4/Z2 at a regular point, with A1 points of the correct orientation type for the resolution topology, and are the gluing estimates with rho=eps^{1/2} correct (decay order 2 end, CH background normal coordinates)? Does the glued orbifold have the topology V_m? (3) Theorem 74.B mixed transfer: is the limit argument correct, in particular the treatment of the monopole class depending on the metric and the cross term int s|W+|? Is B_+=-2pi^2 c_+ for Ricci-flat fillers consistent with the charge convention c_pm=2/|Gamma|-2chi-+3tau-+3eta and P(N)=4I_pm+S/12+8pi^2 c_pm? (4) Theorem 74.C: Einstein Chern-Weil I_pm=2pi^2(T_pm - x), x=S/96pi^2; the Cauchy-Schwarz bound for constant s<0; the formulas T_+=A-k+C_+, T_-=A/3+5k+C_-; the large-A linear form 9C_-+2C_++42k>=0; exact x_min=(A/27)[4-sqrt(1-3k/A)]^2; and Corollary 74.D for Ricci-flat Kahler fillers (c_+=0, c_-=-4(chi-1/|Gamma|)). (5) The equality-structure paragraph for possible minimizers. Report any error with a corrected statement, and say which statements are fully proved vs. need extra hypotheses (e.g. b^+(X)=1 chamber issues, regularity of orbifold metrics).

## Output

# Verification memo on Step 74: orbifold curvature transfer, the paired‑A1 law, and the Einstein‑bulk budget

## Summary

The load‑bearing mathematics of Theorems 74.A–74.C and Corollary 74.D is correct. I re‑derived every identity, expansion and listed number below. Four statements need correction or sharper wording:

- **Equality structure of a P‑minimizer.** It does not force constant $s$. Constancy of $s$ comes only from minimizing $\mathscr D$ below one.
- **Theorem 74.C does not use $\lambda<0$.** Test (3.1) needs only $P=0$. The Minkowski bound holds for every sign of $s$.
- **Wording in Corollary 74.D.** The phrase "only large‑group fillers" is reversed. The correct condition is on rank versus group order.
- **Section 5 does not need energy equality.** Lower semicontinuity of $P$ is enough. Orbifold regularity of the limit is the hypothesis that carries the weight.

Two strengthenings follow from the same computations. They are given in §6.

---

## 1. Theorem 74.A, lower bound

**Normalizations.**
- The operator‑norm Gauss–Bonnet formula $16\pi^2\chi=S/12+2W-P$ is twice $8\pi^2\chi=\int(|W|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)$. This is correct.
- Check on the complex‑hyperbolic host. In the complex orientation $W^-=0$ and $|W^+|^2=s^2/24$. This gives $I_+=12\pi^2\tau=4\pi^2A/3$ and $S=24I_+=32\pi^2A$. Gauss–Bonnet then reads $16\pi^2A/3=8\pi^2A/3+8\pi^2A/3$. ✓

**Topology of the resolution.**
- Euler characteristic: $\chi_{\rm orb}(S^4/\mathbb Z_2)=1$, so $\chi_{\rm orb}(V_m)=A/3+m-2m=A/3-m$. ✓
- Signature: $\tau_{\rm orb}(V_m)=A/9$. Two facts give this. First, $H^2(S^4/\mathbb Z_2;\mathbb Q)=0$. Second, $\eta(\mathbb{RP}^3)=0$, because $\mathbb{RP}^3=L(2,1)$ has an orientation‑reversing isometry ($1\equiv-1 \bmod 2$). ✓
- Orientation matching is automatic for $A_1$. $\mathbb R^4/\{\pm1\}$ has an orientation‑reversing isometry, so every $A_1$ point can be resolved by an Eguchi–Hanson space that is anti‑self‑dual in $M$'s orientation.
- Resolving both points of $S^4/\mathbb Z_2$ this way gives a simply connected manifold with $b_2=2$ and $\tau=0+2(-1)=-2$. That is $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$. Explicitly, the classes $E_1\pm E_2$ are disjoint $(-2)$‑spheres.
- Hence the resolution of $V_m$ is $X\#2m\overline{\mathbb{CP}}^2$, with $\chi=A/3+k$ and $\tau=A/9-k$. ✓
- Formula (0.1) follows from additivity using the definition of $c_\pm$. The Eguchi–Hanson charges are $c_+=1-4+3=0$ and $c_-=-6$. ✓
- $T_-(V_m)=A/3-k$, which agrees with $2\chi_{\rm orb}-3\tau_{\rm orb}$. ✓

**Transfer of the scalar bound.**
- In a $\mathbb Z_2$‑equivariant normal chart the orbifold metric is $\delta+O(r^2)$. The Eguchi–Hanson metric is $\delta+O(r^{-4})$.
- With any gluing radius $\rho\to0$ and $\varepsilon/\rho\to0$, curvature stays bounded on annuli of volume $O(\rho^4)$.
- Therefore $S(g_\varepsilon)\to S(g)$ and $P(g_\varepsilon)\to P(g)$, with no sign condition on the curvature. The transfer $S\ge32\pi^2A$ is valid.
- **Hypothesis to state explicitly:** the orbifold metric is $C^2$ in the uniformizing charts.

**Convex combination.** Insert $S=32\pi^2A+\sigma$ and $W=4\pi^2A/3+w$, with $w\ge0$ from $W\ge|I_+-I_-|$:
- $P=8\pi^2k+\sigma/12+2w$ and $R=8\pi^2(A+k)+\sigma/3+2w$. ✓
- $4P=\tfrac{4k}{A+k}\cdot 8\pi^2(A+k)+1\cdot\tfrac{\sigma}{3}+4\cdot 2w$. ✓
- Since $4k/(A+k)<4$, the minimum of the three weights' values is $\min\{1,4k/(A+k)\}$. Also $\mathscr D\ge 4P/R$. The bound is correct.
- The Einstein exclusion holds for every sign of $s$. ✓

**The (SW) hypothesis, made precise.**
- The barycentre step is correct. $(\mathbf a^+)^2$ is convex, the barycentre of the basic classes is $c_1(X)$, and $(c_1^+)^2\ge c_1^2=A$.
- For a Kähler surface $b^+=2p_g+1$. So $b^+=1$ forces $p_g=0$, hence $\chi(\mathcal O)=1-q\le1$, hence $q=0$ and $A=9$. The case $b^+=1$ therefore occurs **only for fake projective planes ($A=9$)**. Every ball quotient with $A\ge18$ has $b^+\ge3$.
- For $A=9$ there is a chamber argument. Each class $c_1(X)\pm E_1\pm\dots\pm E_k$ has square $9-k$. If $k\le8$, then $\mathbf a^2>0$ gives $(\mathbf a^+)^2\ge \mathbf a^2>0$, so $\mathbf a^+\neq0$ for every metric. The unperturbed equations then never meet a wall, so the Kähler‑chamber invariants hold for all metrics.
- For $A=9$ and $k\ge9$, (SW) remains open.
- The screening rows at $A=9$ have $k\le6$, so they are covered by this argument.

---

## 2. Upper construction (Green football cap)

**The cap metric.**
- $u=1+r^{-2}$ is harmonic, so $s_h=-6u^{-3}\Delta u=0$, and $h$ is conformally flat.
- Write $h=G^2 g_{S^4}$. Then $G=u(1+r^2)/2=\tfrac12(1+r^2)(1+r^{-2})$. This is exactly the sum of the round conformal‑Laplacian Green functions at the two poles.
- The map $\iota$ is the restriction of $\mathrm{diag}(-1,-1,-1,1,-1)\in SO(5)$ to $S^4$.
  - It fixes exactly $\pm e_4$, which are $(0,0,0,\pm1)$ in the plane.
  - Its linearization there is $-I$.
  - It exchanges the poles and preserves $G$.
- So $(\mathbb R^4\setminus0,h)/\iota$ is the Green blow‑up of $O=S^4/\mathbb Z_2$ at the image of the poles, which is a regular point. ✓

**Topology of the glued orbifold.**
- $O$ admits an orientation‑reversing diffeomorphism: $x_5\mapsto -x_5$ commutes with the $\mathbb Z_2$ action. So the orientation of the inserted copy does not matter.
- The glued orbifold is $X\#mO=V_m$.
- The $A_1$ points of every orientation are resolvable as in §1.

**Curvature integrals.**
- Large‑$r$ asymptotics: $\mathrm{Ric}^\circ\approx-16(\hat x\hat x-\delta/4)r^{-4}$, whose norm is $8\sqrt3\,r^{-4}$. ✓
- Tail: $\int_\varrho^\infty192r^{-8}\,2\pi^2r^3\,dr=96\pi^2\varrho^{-4}$. ✓
- Noncompact Gauss–Bonnet uses an end term of $+1$ per asymptotically Euclidean end, as calibrated by flat $\mathbb R^4$. The transgression error vanishes when the metric decays like $O(r^{-2})$.
- This gives $P(h)=32\pi^2$ for the two‑ended neck ($\chi=0$) and $P(G)=16\pi^2$ for the one‑ended quotient. ✓

**Gluing estimates.** These are correct with $\rho=\varepsilon^{1/2}$:
- $|\partial^j(\varepsilon^2h-\delta)|\lesssim\varepsilon^2\rho^{-2-j}$; for $j=2$ this is $O(1)$.
- $|\partial^j(g_X-\delta)|\lesssim\rho^{2-j}$.
- Cutoff derivatives contribute the same orders.
- Curvature is $O(1)$ on volume $O(\varepsilon^2)$.
- The cap tail per insertion is $96\pi^2(\varepsilon/\rho)^4=O(\varepsilon^2)$.
- $L_s=O(\rho^4)\to0$.

Hence $P\to8\pi^2k$ and $\mathscr D\to4k/(A+k)$. The ceiling value $1$ is inherited from the A02 dumbbell–cylinder construction (A02 package §1.2), which I did not re‑verify. Its local mechanism is consistent: on a long round $S^3\times\mathbb R$ cylinder, $4P/R=12/12=1$.

The statement $\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}$ is proved, given (SW) and that inherited ceiling.

---

## 3. Theorem 74.B (mixed transfer)

**The limit argument is correct.**
- Prop. 3.8 gives $\ge72\pi^2(\mathbf a_\varepsilon^+)^2\ge72\pi^2A$ uniformly in $\varepsilon$. No convergence of the monopole classes is needed.
- In the decomposition bulk + annuli + fillers, the integrand on the fillers is exactly $6|W^+|^2$, because $s\equiv0$ there.
- On the annuli the integrand is bounded, on volume $O(\rho^4)$.
- On the bulk the integral converges to $\int_V(s-\sqrt6|W^+|)^2$.
- The cross term $\int s|W^+|$ therefore has no filler contribution at all.

**Hypothesis on fillers.** Fillers that are not Ricci‑flat must decay at rate at least $O(r^{-2})$ with derivatives, so that the $\rho=\varepsilon^{1/2}$ estimates of §2 apply. Scalar‑flat Kähler ALE spaces satisfy this.

**Charge convention.** Combine ALE Gauss–Bonnet, $16\pi^2(\chi-1/|\Gamma|)=S/12+2W-P$, with $12\pi^2(\tau+\eta)=I_+-I_-$. Eliminating $I_-$ gives
$$P=4I_++S/12+8\pi^2\big(2/|\Gamma|-2\chi-3\tau-3\eta\big),$$
which is the stated $c_+$ (and symmetrically $c_-$).
- Consequently $B_+=-2\pi^2C_+$ for Ricci‑flat fillers.
- For scalar‑flat fillers that are not Ricci‑flat, $B_+=P(N)/4-2\pi^2c_+$.
- Eguchi–Hanson check: $I_-=12\pi^2$, $c_-=-6$. ✓

**Formula (0.2).** Ricci‑flat Kähler implies $W^+=0$. Then Gauss–Bonnet gives $I_-=8\pi^2(\chi-1/|\Gamma|)$, so $c_-=-4(\chi-1/|\Gamma|)$.
- Checks: $A_3$ gives $-15$; $A_6$ gives $-192/7$. ✓
- In the T‑type entry, $n$ must mean $|\Gamma|$. For a rational‑ball Milnor fibre $|\Gamma|$ is a square.

---

## 4. Theorem 74.C and Corollary 74.D

**Chern–Weil.** $4\pi^2T_\pm=S/24+2I_\pm-P/2$. For Einstein metrics this gives $I_\pm=2\pi^2(T_\pm-x)$. ✓

**Correction: (3.1) does not need constant $s$ or $\lambda<0$.** Minkowski's inequality gives, for every metric,
$$\int(s-\sqrt6|W^+|)^2\le\int(|s|+\sqrt6|W^+|)^2\le(\sqrt S+\sqrt{6I_+})^2 .$$
- The right side equals $12\pi^2[\sqrt{8x}+\sqrt{T_+-x}]^2$. ✓
- So the reference to Yamabe sign and to constancy of $s$ should be removed. Einstein enters only through $P=0$.

**Maximization over $x$.** Cauchy–Schwarz gives $(\sqrt8\sqrt x+\sqrt{T_+-x})^2\le9T_+$, with equality at $x=8T_+/9$. The function is $7x+T_++4\sqrt2\sqrt{x(T_+-x)}$, which is concave. ✓

**Large‑$A$ form.** Put $x=T_-=A/3+\delta$ with $\delta=5k+C_-$. Expanding,
$$f=6A+9\delta-3k+3C_++O(k^2/A).$$
The condition $f\ge6A+C_+$ becomes $42k+9C_-+2C_+\ge0$. ✓

**Exact root.** Write $t=\sqrt{1-3k/A}$ and $x=\tfrac{A}{27}(4-t)^2$. Then
- $T_+-x=\tfrac{2A}{27}(2t+1)^2$;
- the bracket sums to $\sqrt{6A}$, so $f=6A$ exactly;
- $x_{\min}-\tfrac{A+k}{3}=\tfrac{4A}{27}(1-t)^2$;
- the requirement $k\le A/3$ and the bound $C_->-14k/3$ follow.

**Corollary 74.D numerics.** Reproduced: $1.15544$, $2.27379$, $3.44281$. The expansion $7k/6-k^2/(12A)$ is correct.

**Correction to the interpretation in 74.D.** Take a single filler of rank $r$ carrying $k=r$ classes. The leading‑order condition is
$$r\ \ge\ 6\,(1-1/|\Gamma|).$$
- A larger group makes the condition harder, not easier.
- Since $1-1/|\Gamma|\ge 1/2$, every filler must carry at least 3 classes on average. For large $|\Gamma|$ it must carry about 6.
- This reproduces every listed linear form: $A_1\!:-12$, $A_2\!:-12$, $A_3\!:-9$, $A_4\!:-4.8$, $A_5\!:0$, $D_4\!:-7.5$, $D_5\!:-3$.
- It also reproduces the survivor thresholds: $A_{n\ge6}$ and $D_{n\ge6}$ survive.
- $L(9,4)$: $-45-46/9+42=-8.1$. ✓

**Additional content in the cyclic survivors.** All 8 cyclic survivors have $c_+c_-\neq0$. A Ricci‑flat filler of that type would be non‑Kähler in both orientations. Known Ricci‑flat Kähler ALE spaces in the T‑type family have $|\Gamma|=dn^2$ and $b_2=d-1$. So $b_2=1$ requires $|\Gamma|=2n^2$. The survivor orders are $49$, $81$ and $121$, which are odd squares and not of this form. If every Ricci‑flat ALE 4‑manifold were Kähler (an open expectation, not a theorem), all eight would be eliminated. This should be recorded as the precise open input.

**Script.** The screen is coded correctly. The interval is nonempty with lower end $A/3>0$, so $T_+-x\ge0$ under the square root. The warped‑product Ricci formulas in part (a) are correct.

---

## 5. Equality structure and Section 5

**Correction to the equality structure.**

*For a $P$‑minimizer*, $P=8\pi^2k$ forces $\sigma=w=0$. This gives $S=32\pi^2A$, $I_+=4\pi^2A/3$ and $W^-\equiv0$. Equality in the Minkowski chain then forces two things:
- $|W^+|=|s|/\sqrt{24}$ almost everywhere (equality case of Cauchy–Schwarz);
- $s|W^+|\le0$, hence $s\le0$ everywhere.

It does **not** force constant $s$.

*For a $\mathscr D$‑minimizer with $k<A/3$*, the condition $L_s=0$ adds constancy, so $s\equiv$ const $<0$. Note that the sign follows from the equality chain itself, without any Yamabe input.

LeBrun's smooth rigidity case of Prop. 3.8 does not pass through the limit. The equality analysis on the orbifold is a separate local problem. Existence of such a minimizer is open, as the note states.

**Section 5.** Hypothesis (i), energy equality, is unnecessary.
- Away from the singular points, $g_i$ converges smoothly to the limit, and the integrand of $P$ is nonnegative.
- Fatou's lemma then gives $\liminf P(g_i)\ge P(V)\ge8\pi^2k$, whatever the bubbles and necks are.

What remains essential:
- (ii): the limit is a $C^2$ orbifold metric on $V_m$. A $P$‑minimizing sequence has no Euler–Lagrange equation, so removable‑singularity theorems for critical metrics do not apply automatically.
- (iii): the (SW) hypothesis.
- The inherited smooth bound $P_*<8\pi^2k$, which I did not re‑verify.

---

## 6. Strengthening: a $P$‑floor for any resolved bulk

For any metric, $I_\pm=2\pi^2(T_\pm-x)+P/4$. Set $y=P/(8\pi^2)$. The transfers then give, for every orbifold metric on a bulk $V$ resolved as in §2:
$$x\ge A/3,\qquad x\le\min(T_+,T_-)+y,\qquad \max_x\big[\sqrt{8x}+\sqrt{T_++y-x}\big]^2\ge 6A+C_+ .$$

Applied to $V_m$:
- The scalar part gives exactly $y\ge k$, recovering Theorem 74.A.
- The mixed part at $y=k$ is attained with equality, $(\sqrt{8A/3}+\sqrt{2A/3})^2=6A$. This is consistent with the sharpness of the Green‑cap family.

This gives one formula for an explicit $8\pi^2y_{\min}(V)$ lower bound on every candidate bulk. For non‑Einstein bulks in degenerations it replaces the binary "Einstein or not" screen.

---

## Status

| Statement | Status |
|---|---|
| 74.A lower bounds and Einstein exclusion | Proved given (SW) and $C^2$ orbifold regularity. (SW) holds for $A\ge18$, and for $A=9$ with $k\le8$ by the chamber argument in §1. $A=9$, $k\ge9$ is open. |
| 74.A $\inf P=8\pi^2k$; $\alpha_{\rm orb}=\min\{1,4k/(A+k)\}$ | Proved, given the inherited ceiling construction. |
| 74.B | Proved for fillers decaying at rate $\ge2$ with derivatives. |
| 74.C, 74.D | Proved. The Yamabe sign and constant‑$s$ assumptions are not needed. |
| Survivors | Necessary tests only. Realizability of the fillers and existence of an Einstein bulk are open. |
| Equality structure | Corrected as in §5. Attainment is open. |
| Section 5 | Holds without energy equality. It requires orbifold regularity of the limit. |