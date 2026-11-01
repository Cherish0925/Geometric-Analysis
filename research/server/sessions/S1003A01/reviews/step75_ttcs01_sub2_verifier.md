# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step74_attainment_and_root_lattice.md",
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/A-COLOURFUL-CLASSIFICATION-OF-QUASI-ROOT-SYSTEMS-AND-HYPERPLANE-ARRANGEM--7dfcf71bb519--b40929d5dfa6/object.md"
  ]
}
```

## Task

Verify the two proposed consequences in spirit_step74_attainment_and_root_lattice.md against the full Step-74 theorem. First, check the variational argument that an attained orbifold P floor forces an attained scalar-energy floor, then constant scalar curvature and Einsteinity; compute the first-variation formulas and normalized-defect equality cases for k<A/3, k=A/3, and k>A/3. Second, check the topology/root-lattice argument for X a compact ball quotient: every embedded (-2)-sphere in X#k CPbar^2 lies in the exceptional -I_k lattice, and any embedded Kronheimer ADE plumbing determines a root subsystem of D_k. Scrutinize whether the signed-support-graph conclusion 'only A and D components' is valid for arbitrary root subsystems (not merely reflection-closed sets), whether E6/E7/E8 are excluded without primitivity, and whether a full-rank A_r plumbing with k=r is impossible. Identify and repair any hidden assumptions. Give a direct mathematical memo, not procedural advice.

## Output

# Verification memo: Step-74 attainment consequence and the aspherical root restriction

Both consequences proposed in `spirit_step74_attainment_and_root_lattice.md` are correct as mathematics. Four inputs are used without being stated, and they are made explicit below. The checks also produce three refinements that the note does not contain:

- At the wall $k=A/3$, attainment is equivalent to the existence of a self-dual orbifold conformal class on $V_m$.
- Complete absorption of the exceptional lattice by Kronheimer plumbings has a forced block structure.
- That block structure turns Corollary 74.D into an explicit additive budget, and the budget reproduces the Step-74 screening numbers exactly.

---

## 1. Nonattainment of $\inf_{\rm orb}P(V_m)=8\pi^2k$

**From an attained $P$ floor to a global minimizer of $S$.** Theorem 74.A gives, for every orbifold metric,
$$P=8\pi^2k+\sigma/12+2w,\qquad \sigma=S-32\pi^2A\ge0,\qquad w=W-\tfrac{4\pi^2A}{3}=2I_-\ge0 .$$
So $P(g)=8\pi^2k$ forces $\sigma=0$, that is $S(g)=32\pi^2A$. The bound $S\ge32\pi^2A$ holds for every metric in $\mathscr G_{\rm orb}(V_m)$, so $g$ is a global minimizer of $S$. Since $S$ is scale-invariant in dimension 4, every orbifold-smooth variation $g+th$ stays in the admissible class and $g$ is critical for $S$.

The input used here is that the transfer bound is valid for all orbifold metrics, not only for limits of smooth ones. Lemma 86.S resolves an arbitrary orbifold metric written in uniformizing normal coordinates, so the input is supplied.

**Conformal variation.** Take $g_t=e^{2t\varphi}g$ in dimension 4, with $\Delta=\operatorname{div}\operatorname{grad}$. Then
$$s_t=e^{-2t\varphi}\big(s-6t\Delta\varphi-6t^2|d\varphi|^2\big),\qquad d\mu_t=e^{4t\varphi}d\mu,$$
so
$$s_t^2\,d\mu_t=(s-6t\Delta\varphi)^2\,d\mu+O(t^2),\qquad \frac{d}{dt}\Big|_0 S=-12\int s\,\Delta\varphi=-12\int\varphi\,\Delta s .$$
Hence $\Delta s=0$. Integrating by parts, $\int|\nabla s|^2=0$, so $s$ is constant. Integration by parts is legitimate on an orbifold with isolated singularities: the singular set has codimension 4, or one can work in $\Gamma$-invariant uniformizing charts with a partition of unity. Because $S>0$, the constant is nonzero, and the equality chain gives $s<0$.

**Trace-free variation.** With $s'=-\Delta\operatorname{tr}h+\delta\delta h-\langle\operatorname{Ric},h\rangle$ and $\operatorname{tr}h=0$,
$$DS[h]=\int 2s\big(\delta\delta h-\langle\operatorname{Ric}^\circ,h\rangle\big)=-2s\int\langle\operatorname{Ric}^\circ,h\rangle ,$$
because $s$ is constant and the divergence term integrates to zero. Equivalently, the full Euler–Lagrange tensor is
$$2\nabla^2s-2(\Delta s)g-2s\operatorname{Ric}+\tfrac{s^2}{2}g ,$$
which reduces to $-2s\operatorname{Ric}^\circ$ when $s$ is constant.

The test tensor $h=\operatorname{Ric}^\circ$ is $\Gamma$-invariant in each chart, so it is an admissible orbifold variation. It gives $-2sP=0$, contradicting $P=8\pi^2k>0$.

**Conclusion.** $\inf_{\rm orb}P(V_m)$ is not attained for any $m\ge1$. The only inputs are (SW), (R) and the transfer bound. The Bach-flat route quoted in the note is equivalent: $W^-=0$ makes $W$ critical through Gauss–Bonnet, so $P$-critical implies $S$-critical. The route through the $S$-minimizer is shorter. The Step-74 remark that a $P$-minimizer need not have constant $s$ is superseded.

## 2. Equality cases for the normalized defect $\mathscr D=E$

The weighted-mean identity checks:
$$\frac{4P}{R}=\frac{8\pi^2(A+k)\cdot\frac{4k}{A+k}+\frac{\sigma}{3}\cdot1+2w\cdot4}{8\pi^2(A+k)+\frac{\sigma}{3}+2w},\qquad E=\frac{4P}{R}+\frac{L_s}{R}.$$
Moreover $4k/(A+k)<1$ if and only if $k<A/3$.

**Case $k<A/3$.** The minimal value $4k/(A+k)$ is strictly below the other two values, 1 and 4. Attainment of $\alpha_{\rm orb}$ therefore forces $\sigma=w=0$ and $L_s=0$. Then $P=8\pi^2k$ is attained, which §1 excludes. So $\alpha_{\rm orb}$ is not attained.

**Case $k>A/3$.** Every value in the mean is at least 1, and the weight $8\pi^2(A+k)>0$ sits on the value $4k/(A+k)>1$. Hence $E>1$ for every metric, and the infimum 1 is not attained.

**Case $k=A/3$ (the wall).** The values are $1,1,4$. $E=1$ holds if and only if $w=0$ and $L_s=0$, with $\sigma$ free. Three facts sharpen the note's description of this case.

1. **The wall exists only when $18\mid A$.** One needs $k=2m=A/3$ together with $9\mid A$. So $A=18j$, $m=3j$, $k=6j$. In particular the wall never occurs for fake projective planes ($A=9$).

2. **An attaining metric has $\sigma>0$ strictly.** If $\sigma=0$, then $P=8\pi^2k$ would be attained, which §1 excludes. So any wall extremal has $S>32\pi^2A$ and $P=8\pi^2k+\sigma/12>8\pi^2k$. It is not Einstein, by Theorem 74.A(1).

3. **Reduction to conformal geometry.** The condition $W^-=0$ is conformally invariant. If an orbifold conformal class $[g]$ with $W^-=0$ has negative Yamabe constant, the orbifold Yamabe problem is solvable by the direct or subcritical method: the threshold $Y(S^4)/|\Gamma|^{1/2}$ is positive, so no bubbling occurs. The solution has constant $s<0$, so $E=1$.
   - Yamabe constant zero is impossible, since it would give constant $s=0$, contradicting $S\ge32\pi^2A$.
   - Positive Yamabe constant must be excluded on $V_m$. This is the "negative-Yamabe exclusion of 86.S" cited in Theorem 74.C. It is a genuine dependency: the sign of $s$ at the wall is not supplied by the $L^2$ inequalities.

   **Conclusion for the wall.** Granting 86.S, wall attainment holds if and only if $V_m=X\#m(S^4/\mathbb Z_2)$ carries an orbifold conformal structure with $W^-=0$ in the complex orientation of $X$.

   The natural constructive candidate is a Donaldson–Friedman-type gluing of the ball-quotient conformal class (which has $W^-=0$) with $m$ conformally flat copies of $S^4/\mathbb Z_2$. Its decisive input is the $H^2$ of the self-dual deformation complex. This input is not settled by the supplied material.

   The available inequalities give no obstruction at the wall. With $W^-=0$ and constant $s<0$:
   - LeBrun Prop. 3.8 (mixed estimate) and Cauchy–Schwarz give $\sqrt S\ge\sqrt{72\pi^2A}-\sqrt{8\pi^2A}$, that is $S\ge32\pi^2A$.
   - LeBrun Prop. 4.1, with $I_+=4\pi^2A/3$, gives $S/24\ge2\pi^2A-2\pi^2A/3$, again $S\ge32\pi^2A$.

   Neither adds information beyond $\sigma\ge0$.

## 3. Sphere classes in $M=X\#k\overline{\mathbb{CP}}^2$, $X$ a compact ball quotient

The argument is correct. Integrally, $H_2(M)=H_2(X)\oplus\bigoplus\mathbb ZE_i$, including torsion, by Mayer–Vietoris across $S^3$. The collapse map $b$ is the projection onto the first summand. $X$ is a $K(\pi,1)$, so every map $S^2\to X$ is null-homotopic. Hence the class of any map $f:S^2\to M$ lies exactly in $\bigoplus\mathbb ZE_i$.

One phrase needs repair: the class has no $H_2(X)$ or torsion component at all, so "free integral class" should simply read "class".

Three consequences follow, two of them beyond the note:

- **Every sphere class has square $\le0$,** with equality only for the zero class.
- **Square $-2$:** $\sum a_i^2=2$ forces $a=\pm E_i\pm E_j$ with $i\ne j$.
- **Square $+2$ is impossible.** No embedded $(+2)$-sphere exists. Hence any ADE filler glued with its complex orientation opposite to $M$'s cannot occur on this $M$. Step 74 uses orientation-matched fillers; this shows orientation matching is forced, not chosen.

## 4. From an embedded plumbing to a root subsystem of $D_k$

Let $R$ be the irreducible ADE root system of the plumbing, with simple sphere classes $s_1,\dots,s_r$.

- **Injectivity.** The Gram matrix of the $s_i$ is $-\mathrm{Cartan}(R)$, which is nonsingular. So $Q(R)\to H_2(M)$ is injective, and it is isometric onto its image in $-I_k$. No primitivity is used. Primitivity of the image only affects the topology of the complement, for instance $H_1$ of the bulk, not the root type.
- **The image is the full root system $\varphi(R)$, not just the simple classes.** For a simply-laced root lattice, the roots are exactly the norm-2 vectors. So $\varphi$ sends all of $R$ into the norm-2 vectors of $\mathbb Z^k$, which form $D_k$. Being an isometry, $\varphi$ intertwines reflections, so $\varphi(R)$ is reflection-closed.

  This is the hidden step. The signed-graph argument must be applied to $\varphi(R)$. The $r$ simple sphere classes alone form a set that is not reflection-closed; for example $\{e_1-e_2,\,e_2-e_3\}$. Applied to such a set, the argument only certifies a spanning tree, not the component type.

## 5. The signed support graph argument

Fix a reflection-closed symmetric set $\Phi\subset D_k$. Put an edge $\{i,j\}$ in the support graph whenever $\pm e_i\pm e_j\in\Phi$.

1. **Sign normalization.** Flip the signs of coordinates along a spanning tree of each support component, so that every tree root is a difference $e_i-e_j$. A tree has no cycles, so the flips are consistent. These flips lie in $\{\pm1\}^k\subset O(\mathbb Z^k)$. They need not lie in $W(D_k)$, but they preserve $D_k$ and the lattice, which is all that is needed.
2. **All differences are generated.** Reflections in the tree roots are transpositions, and they generate $S_v$ on the $v$ vertices of the component. Since $\Phi$ is reflection-closed, $\Phi$ contains all $e_c-e_d$ on the component.
3. **Plus edges.** If some $e_a+e_b\in\Phi$ remains, then $S_v$ produces all $e_c+e_d$, and the component carries $D_v$. Otherwise it carries $A_{v-1}$.
4. **Orthogonal decomposition.** Roots in different support components have disjoint supports, hence are orthogonal, so $\Phi$ is the orthogonal sum of its components. Components with $v=1$ carry nothing, because $D_k$ contains no $\pm e_i$.

The ranks are $v-1$ for an $A_{v-1}$ component and $v$ for a $D_v$ component.

**What the argument requires.** It uses only reflection-closure: it needs neither additive closure nor the Levi condition. It is therefore valid for every root subsystem in the reflection sense. This agrees with the source in Knowledge:

- Rembado, Thm 3.1.3 and Thm 4.1.1, specialized to loop-free crystallographs. The red components are type A, the bichromatic components are type D, and the bipartite components $\mathcal G^{d_1,d_2}$ are equivalent to $A_{d_1+d_2-1}$ by Lemma 4.2.1.
- The sign flips in step 1 are exactly Rembado's $\sigma_{e_i}$ recolouring.

Citing Rembado Thm 4.1.1 is an acceptable alternative to writing out the argument above.

## 6. Consequences for single plumbings

Since $R$ is irreducible, $\varphi(R)$ is a single component: either $A_{v-1}$ on $v=r+1$ coordinates, or $D_v$ on $v=r$ coordinates with $D_v\cong R$.

- **$E_6,E_7,E_8$** are not isomorphic to any $A_n$ or $D_n$. They are excluded for every $k$, without primitivity. In particular $Q(E_8)$ admits no isometric embedding into any $\mathbb Z^k$.
- **$A_r$ in exactly $k=r$ coordinates** requires $D_r\cong A_r$. Among irreducible types this happens only for $r=3$:
  - $A_1$ needs 2 coordinates.
  - $A_2$ needs 3 coordinates.
  - $A_3$ fits in 3 coordinates as $D_3$. An explicit chain is $e_2-e_3$, $e_1-e_2$, $e_2+e_3$, with pairings $-1,-1,0$.
  - $A_r$ with $r\ge4$ needs $r+1$ coordinates.

  So full-rank $A_r$ with $k=r$ is impossible for every $r\ne3$, including $r=1,2$, which the note did not state.
- **$D_r$ on $r$ coordinates** is lattice-feasible. The index of $D_r$ in $\mathbb Z^r$ is 2, since $\det=4$. The order $|H_1(\partial P)|=4$ of the prism-manifold boundary is a square, so the elementary rational-ball parity test raises no obstruction.

## 7. Complete absorption and the resulting budget

Let several disjoint Kronheimer plumbings span the exceptional $\mathbb Q^k$. Their images are mutually orthogonal, so their union is reflection-closed and §5 applies to it. Spanning forces every coordinate into a $D_v$ component with $v\ge2$. An $A_{v-1}$ component leaves the vector $\sum\pm e_i$ orthogonal to everything, and an isolated coordinate is unabsorbed.

Decomposition into irreducibles is unique, and each $\varphi_j(R_j)$ is irreducible. This makes the block structure precise:

- A $D_2$ block is exactly two $A_1$ plumbings, with classes $E_i\pm E_j$. This is the paired-EH configuration of $V_m$.
- A $D_3$ block is one $A_3$ plumbing.
- A $D_v$ block with $v\ge4$ is one $D_v$ plumbing.

**Budget.** Insert this structure into Corollary 74.D, the exact $C_+=0$ test $T_-\ge x_{\min}$. Expanding $x_{\min}=\tfrac A3+\tfrac k3+\tfrac{k^2}{3A}+O(k^3/A^2)$, the test reads
$$\sum_{\text{blocks}}\varepsilon_j\le-\frac{k^2}{12A}+O(k^3/A^2),\qquad \varepsilon_j=\chi_j-\frac1{|\Gamma_j|}-\frac{7v_j}{6}.$$
The block excesses are:

| Block | $\varepsilon_j$ |
|---|---|
| $D_2$ (two EH) | $3-\tfrac73=+\tfrac23$ |
| $D_v$, $v\ge3$ | $1-\tfrac v6-\tfrac1{4(v-2)}$, using $|\Gamma|=4(v-2)$ |

For the $D_v$ formula:

| $v$ | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| $\varepsilon$ | $\tfrac14$ | $\tfrac5{24}$ | $\tfrac1{12}$ | $-\tfrac1{16}$ | $-\tfrac{13}{60}$ |

**Cross-check with Step 74.** For $C_+=0$, the mixed linear form in (3.2) equals $-36\sum\varepsilon_j$. This gives:

- $D_4\mapsto-7.5$ and $D_5\mapsto-3$, matching the JSON screening values.
- $A_5$ at $k=5$: $\varepsilon=6-\tfrac16-\tfrac{35}{6}=0$, which is the reported marginal value.

**Sample mixtures**, computed here from this formula at leading order:

| Mixture | $\sum\varepsilon_j$ | Leading-order outcome |
|---|---|---|
| $D_7+D_5$ | $\approx-0.133$ | passes |
| $D_7+D_4$ | $\approx-0.008$ | passes, only for very large $A$ (roughly $A\gtrsim1.2\times10^3$ at $k=11$) |
| $D_6+D_4$ | $>0$ | excluded |
| $D_6+D_5$ | $>0$ | excluded |
| $D_v+D_2$ | $>0$ for every $v$ | excluded |

So the full-absorption Kronheimer problem reduces to a finite integer partition problem over $D$-blocks. Pure $V_m$ ($D_2$ blocks only) and all-$D_3$, $D_4$, $D_5$ configurations are excluded. Survival requires enough blocks with $v\ge6$.

## 8. What remains unresolved

**Realizability of surviving $D_v$ blocks ($v\ge6$).** One needs a disjoint embedded configuration of $(-2)$-spheres in the classes of $D_v$ with prescribed plumbing intersections. Two sufficient routes are available:

- *Local route.* The plumbing embeds in $\#v\overline{\mathbb{CP}}^2$ minus a ball, with rational-ball complement bounded by the reversed prism manifold.
- *Global route.* The plumbing embeds in $M$ with nontrivial interaction with $X$; the local route is not necessary.

Two remarks bear on this:

- **No holomorphic realization.** Classes $E_i+E_j$ have $K\cdot C=-2\ne0$, so $D$-type plus-classes are never holomorphic $(-2)$-curves. Any realization is necessarily non-complex.
- **Individual classes are not the difficulty.** Each single root class is trivially realized by a tube sum of exceptional spheres. The difficulty lies entirely in realizing the whole configuration disjointly.

**Other open inputs.**

- Rational-ball fillers and hypothetical $b_2=1$ fillers with ADE ends carry no sphere basis, so §§3–7 say nothing about them.
- At the wall, the decisive input is the $H^2$ of the self-dual deformation complex for the gluing of $X$ with $m$ copies of $S^4/\mathbb Z_2$.