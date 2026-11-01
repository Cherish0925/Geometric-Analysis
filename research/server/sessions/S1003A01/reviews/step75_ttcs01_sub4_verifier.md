# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/notes/spirit_step74_attainment_and_root_lattice.md",
    "Knowledge/objects/papers/Torus-Actions-on-Alexandrov-4-Spaces--16a56ecf5468--b4037224a666/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Skills/geometric-analysis/research/sources/mathematics/current/round13_chamber.md"
  ]
}
```

## Task

Critically review the load-bearing topology and supply hypotheses of Theorem 74.A. Check whether the T^2/Orlik-Raymond reasoning as written really yields a diffeomorphism (not merely homeomorphism) between the oriented two-Eguchi-Hanson resolution of S^4/Z2 and CPbar^2#CPbar^2; if the argument needs explicit orbit weights or a smooth-classification statement, say exactly what remains and whether a Kirby/lattice shortcut is valid. Also check the metricwise scalar bound S>=32pi^2 A on X#k CPbar^2 for b+=1 from LeBrun's polarized argument, and whether any fake-projective-plane exception remains. Conclude the precise theorem scope that is presently supported.

## Output

# Verification memo: the topology and Seiberg–Witten inputs of Theorem 74.A

## Summary

- **(R), the resolution topology.** The Step-74 argument as written proves only that $N$ is *homeomorphic* to $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$. With the explicit orbit weights computed below, the needed *orientation-preserving diffeomorphism* follows from one smooth classification input. Two routes work:
  - Orlik–Raymond's smooth equivariant classification, cited from Orlik–Raymond I itself;
  - a Kirby shortcut that rests on $\pi_0\mathrm{Diff}^+(\mathbb{RP}^3)=1$.
  
  The lattice argument alone gives homeomorphism only.
- **(SW), the supply hypothesis.** It holds metric by metric for every compact ball quotient, including $b^+=1$. The mechanism is LeBrun's polarized selection, not the convexity argument written in Step 74. No exception for fake projective planes remains.

## 1. The resolution $N$ of $O=S^4/\mathbb Z_2$

### 1a. What the written argument establishes

These steps are correct as written:
- $\pi_1(N)=1$ by van Kampen.
- $\chi(N)=4$: $\chi(|O|)=(2+2)/2=2$; remove two cone points and add two copies of $\mathcal O(-2)$, each with $\chi=2$.
- $H_2(N)$ is free of rank 2.
- The two disjoint $(-2)$-spheres span an index-2 sublattice of a definite unimodular rank-2 form. Hence the form is $-I_2$, since there is no other definite unimodular lattice of rank below 8.

From here Freedman gives homeomorphism to $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$, and nothing more.

The Orlik–Raymond step as cited does not close the gap. The registered Knowledge object (Corro–Núñez-Zimbrón–Zarei, Thm. 2.10(1)) states only that a simply connected closed 4-manifold with a $T^2$-action is *equivariantly homeomorphic* to a connected sum of $S^4,\pm\mathbb{CP}^2,S^2\times S^2$. Its sentence that "the smooth classification is equivalent to the topological classification" is a paraphrase, not a usable smooth statement. So the written proof yields homeomorphism.

This matters downstream. The Seiberg–Witten supply (SW) is a statement about the smooth manifold $X\#k\overline{\mathbb{CP}}^2$. If $N$ were only homeomorphic to $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$, the transfer in Lemma 86.S would land on $X\#mN$, whose monopole classes would need a separate gluing theorem.

### 1b. Explicit orbit weights (this closes the identification modulo one smooth classification theorem)

**Setup.** Let $T=T^2$ rotate $w_1,w_2$, and let $T'=T/\langle(\pi,\pi)\rangle$. The cocharacter lattice of $T'$ is $\mathbb Z^2+\mathbb Z(\tfrac12,\tfrac12)$. Take as basis $u=(1,0)$ and $v=(\tfrac12,\tfrac12)$.

The orbit space of $S^4$ is a bigon with vertices at the poles $t=\pm1$ and two edges:
- $\Sigma_1=\{w_1=0\}$, with isotropy circle $u$;
- $\Sigma_2=\{w_2=0\}$, with isotropy circle $(0,1)=2v-u$.

At each pole, $\det(u,2v-u)=2$, which is the $A_1$ vertex.

**Orientation at the two poles.** At the north pole the complex chart $(w_1,w_2)$ is $M$-oriented. At the south pole the $t$-direction reverses, so the $M$-oriented complex chart is $(w_1,\bar w_2)$.

**Inserted circles.** The toric minimal resolution inserts half the sum of the oriented edge generators:
- at the north pole: $\tfrac12\big((1,0)+(0,1)\big)=v$;
- at the south pole, after reorienting the $w_2$-circle: $\tfrac12\big((1,0)+(0,-1)\big)=u-v$.

In $(u,v)$-coordinates the cyclic weight sequence of $N$ is therefore
$$
(\Sigma_1,C_N,\Sigma_2,C_S)=\big((1,0),(0,1),(-1,2),(1,-1)\big),
$$
with consecutive determinants $+1,+1,-1,+1$. All vertices are smooth, and the mixed sign is consistent with $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$ carrying no almost-complex structure.

**Matching an equivariant sum.** Apply $P(x,y)=(x+y,x)$, which lies in $GL(2,\mathbb Z)$ with $\det P=-1$. It sends the sequence to
$$
\big((1,1),(1,0),(1,-1),(0,1)\big).
$$
This is exactly the weighted square of the equivariant sum $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$ formed at fixed points with lateral circles $a=(1,0)$ and $b=(0,1)$:
- the first summand has third circle $(1,1)$;
- the second summand is twisted by $(x,y)\mapsto(x,-y)$, so its third circle is $(1,-1)$.

Under this match, the merged opposite edges $a,b$ are the disjoint $(-2)$-spheres $E_1\pm E_2$.

**Independent check.** $\tilde\Sigma_1$ meets each of $C_N=E_1-E_2$ and $C_S=E_1+E_2$ once. Solving gives $\tilde\Sigma_1=-E_1$, a $(-1)$-sphere, as the matched picture predicts.

**Orientation-matching check.** If $v$ is inserted at both poles, i.e. the south cap is orientation-mismatched, the sequence becomes $(u,v,2v-u,v)$. That is a Hirzebruch-type square with even form, namely $S^2\times S^2$, the double of $D_{-2}$. So orientation matching is precisely what selects $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$.

**What remains.** Orlik–Raymond's equivariant classification determines a smooth $T^2$-manifold with fixed points up to equivariant diffeomorphism, given its weighted orbit space with orientation $\varepsilon$. The circle data above therefore give $N\cong\pm(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2)$, and the form $-I_2$ fixes the sign. Two smooth inputs are needed:
- **Smoothness of the action on $N$.** This is fine: the orientation-matched Eguchi–Hanson at the south pole is $U(2)$-invariant in the coordinates $(w_1,\bar w_2)$, which still contain $T$, and radial cutoffs keep the gluing equivariant.
- **The smooth equivariant classification.** This must be cited from Orlik–Raymond I (Trans. AMS 152, 1970) directly, not from the Corro et al. object. Alternatively it can be proved directly. Locally standard models exist at vertices and edges, and the gluings over the free part are maps into $T'$ over contractible pieces of the polygon. The relevant $H^1$ and $H^2$ obstructions vanish, which is the content of the cross-section Lemmas 5.5–5.8 in the registered object, carried out smoothly.

### 1c. Kirby and lattice shortcuts

- **Lattice only.** Not sufficient. It gives homeomorphism, nothing more.
- **Gluing-uniqueness shortcut.** Valid, with one input. By construction $N=D_{-2}\cup_\varphi D_{-2}$ (two Eguchi–Hanson caps joined across $\mathbb{RP}^3\times I$), with $\varphi$ orientation-reversing. If $\pi_0\mathrm{Diff}^+(\mathbb{RP}^3)$ is trivial (Bonahon's lens-space mapping class groups; Isom$^+(\mathbb{RP}^3)=SO(3)\times SO(3)$ is connected), then every such gluing gives the same manifold. The toric square of $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$ exhibits the same decomposition: the complement of a collar of edge $a$ retracts onto opposite edge $b$, so it is a tubular neighbourhood of a $(-2)$-sphere. This route needs Bonahon registered in place of Orlik–Raymond.

Either route, once its source is registered, gives (R) as an orientation-preserving diffeomorphism. Connected sum at regular points then gives $V_m$ resolving to $M_{2m}$.

## 2. The supply hypothesis (SW) when $b^+=1$

**Which ball quotients have $b^+=1$.** For a ball quotient, $b^+=1$ forces $p_g=0$. Noether's formula together with $c_1^2=3c_2$ gives $c_1^2=9\chi(\mathcal O)>0$, hence $q=0$ and $A=9$. These surfaces are exactly the fake projective planes, as Step 74 states.

**The base invariant is chamber-free.** In LeBrun's Proposition 3.2 (registered 2001 paper), the hypothesis $(2\chi+3\tau)(X)=c_1^2=9>0$ makes the canonical-class invariant of $X$ independent of polarization even when $b^+=1$. The reason is that $c^2>0$ prevents $c^+_H$ from ever vanishing.

**Selection on $M_k$.** For each metric with polarization $H$, orient the $E_j$ so that $c_H^+\cdot E_j\le 0$. Then $a_H=c_1(X)-\sum E_j$ has nonzero small-perturbation invariant at $H$. The chamber compatibility is (G5) of `round13_chamber.md`.

**The bound.** Since $(c^-)^2\le0$ and the cross terms are $\ge0$,
$$
(a_H^+)^2\ \ge\ (c_H^+)^2\ \ge\ c^2=A.
$$
Hence, metric by metric:
- $S\ge32\pi^2A$;
- from Thm. 2.3 multiplied by $9/4$: $\int(s-\sqrt6|W^+|)^2\ge72\pi^2A$, since $\tfrac32\big(\tfrac23s-2\sqrt{2/3}\,|W^+|\big)=s-\sqrt6|W^+|$ and $32\cdot\tfrac94=72$.

Both are exactly what Lemma 86.S and Theorem 74.B consume, since each $g_\varepsilon$ may use its own class.

**Correction to the written (SW).** The text attributes the bound to convexity over all basic classes $c_1\pm E_1\pm\dots$. That mechanism is a $b^+\ge2$ statement. For $b^+=1$ with $k>A$, the signed classes are not simultaneous all-metric monopoles. The polarized selection should replace the convexity sentence; it works uniformly for all $b^+$. Fake projective planes therefore need no separate treatment, and the phrase "the chamber issue is confined to fake projective planes" can be replaced by a citation of LeBrun Prop. 3.2.

## 3. Consistency of the numerical inputs

These identities check out:
- $\chi_{\rm orb}(V_m)=A/3+m-2m=A/3-m$, using $\chi_{\rm orb}(O)=1$.
- $\eta(\mathbb{RP}^3)=0$, because $\mathbb{RP}^3$ has an orientation-reversing isometry. Hence $\tau_{\rm orb}=A/9$.
- $T_-=A/3-k$, which agrees with (0.1) at $C_-=-6k$.

## 4. The statement presently supported

**Theorem 74.A (supported form).** Let $X$ be any compact complex-hyperbolic surface, including $A=9$ fake projective planes, and let $m\ge1$. Then:
- every orbifold metric on $V_m=X\#m(S^4/\mathbb Z_2)$ satisfies $S\ge32\pi^2A$, $P\ge8\pi^2k$, and $\mathscr D\ge\min\{1,4k/(A+k)\}$;
- $V_m$ carries no Einstein orbifold metric;
- $\inf P=8\pi^2k$ and $\alpha_{\rm orb}=\min\{1,4k/(A+k)\}$;
- Theorem 74.B holds with the same supply.

**Dependencies:**
1. Lemma 86.S from A02.
2. LeBrun 2001, Prop. 3.2 and Thm. 2.3 (registered).
3. The weight computation of §1b, together with **one** smooth classification source to be registered: Orlik–Raymond I's equivariant-diffeomorphism classification, or Bonahon's $\pi_0\mathrm{Diff}^+(\mathbb{RP}^3)=1$.

Until item 3 is registered, the identification in (R) is supported as a homeomorphism plus an explicit equivariant match of weighted squares. The diffeomorphism rests on that one theorem. No condition on $b^+$ beyond $b^+\ge1$ enters.