# Step 76 — Route assessment: four problems after the orbifold closure

Agent1, Explore. This note evaluates the four priority problems against the accumulated evidence from both sessions and identifies the highest-value mathematical direction.

## 1. What the orbifold closure establishes and what it does not

The paired-$A_1$ orbifold branch is mathematically complete:
- $\inf_{\rm orb}P(V_m)=8\pi^2k$, $\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}$ (exact)
- $P$-infimum nonattained; $\alpha_{\rm orb}$ nonattained except possibly at the wall $k=A/3$
- No Einstein orbifold on $V_m$ for any $m\ge1$
- Root subsystem theorem: only $A$- and $D$-components embed in the aspherical host
- $E_6,E_7,E_8$ Kronheimer plumbings excluded; single $A_r$ ($r\ge4$) excluded at full rank

Combined with the mixed transfer inequality, most singular concentration patterns are arithmetically excluded. The remaining candidates (D-type Kronheimer at $a\ge6$, rational-ball/Wahl fillers, and collapse) survive the necessary charge and lattice screens but lack actual geometric realizations. A02's message #874 confirms the lattice filter independently and sharpens the full-absorption budget.

**What this does NOT give:**
- Any unrestricted all-metric lower bound on $P$ or $\alpha$
- Smooth $P$-attainment on any fixed manifold
- A closed Goldberg theorem or counterexample
- The exact value of $P_*(M)$ for any single $M$

The orbifold work clarifies *which degenerations must be controlled* but does not supply the analytical control.

## 2. Problem-by-problem assessment

### Problem 1 (Einstein existence, $0<k<A/3$)

**Current state:** Settled negatively for $k\ge A/3$ (LeBrun) and in the window $(1/3-\varepsilon)A<k<A/3$ by N1's actual-field supply. Open for $k\le(1/3-\varepsilon)A$.

**Missing mechanism:** An inequality that sees individual exceptional classes on an Einstein metric. The certified sub-$8\pi^2$ cells show that $P\ge8\pi^2k$ is false for unrestricted metrics; the paired-class averaging in N1 stops at $k/A=1/3$. No new route to positivity was opened in the present loop.

**Assessment:** This is the hardest problem. Any progress requires a fundamentally new mechanism (e.g., a multiclass interaction, a spectral or entropy argument, or a constructive Einstein metric). Neither session has identified such a mechanism. Continued work here without a new idea risks repeating known limitations.

### Problem 2 (Optimal full curvature)

**Current state:**
- $8\pi^2\max\{0,k-A/3\}\le P_*(M)\le 8\pi^2k(1-Cs^2\varepsilon^2\log(1/\varepsilon))$
- The certified CH cell gives $P<8\pi^2\cdot0.99567$ per blow-up
- The balanced family coefficient is $<3.9961512$, not $4$
- The Kähler infimum is exactly $8\pi^2k$ (Theorem $K_\infty$)

**Missing mechanism:** A matching lower bound below $8\pi^2k$ on any fixed manifold. The classical LeBrun bound $P\ge8\pi^2(k-A/3)$ vanishes at $k=A/3$. No quadratic or sublinear lower bound is established.

**Assessment:** The upper and lower bounds are far apart. Improving either side by a definite amount would be valuable but requires either better constructions (hard: the cell optimization seems saturated) or better lower bounds (hard: same difficulty as Problem 1). The most promising specific advance would be deciding $P_*>0$ at $k=A/3$, where Einstein is excluded but the classical lower bound vanishes.

### Problem 3 (Non-Bach-flat smooth global minimizer)

**Current state:** Reduces to smooth $P$-attainment on a manifold admitting neither Einstein nor scalar-flat metrics. A02's Theorem 54.A gives the $k=1$ dichotomy under Anderson's hypotheses: Einstein or non-Bach-flat minimizer.

**Missing mechanism:** Unconditional smooth compactness of $P$-minimizing sequences. The Anderson framework requires strong bubble-scale convergence, derivative-controlled ALE decay, energy equality, and removability—all open analytic inputs.

**Assessment:** The conditional framework is already comprehensive. New progress requires either (a) proving the analytic hypotheses unconditionally, which is deep PDE analysis, or (b) finding a non-variational route to a non-Bach-flat critical metric. Neither seems immediately tractable.

### Problem 4 (Closed negative Goldberg)

**Current state:**
- Complete noncompact strict AKE model (Steps 57–59): existence proof, not a closed example
- Torsion zeros forced by $5\chi+6\tau>0$ (Armstrong); every nondegenerate zero has index $+1$
- Local prolongation through order 8: no obstruction (Steps 62–72)
- Global AAD-LeBrun inequality: $2\int(|W^+|-a)^2+12\pi^2\|c_1(J)^-\|^2\le3T_{\rm AK}$
- Scalar compatibility operator and half-twistor structure (Steps 68–71)
- The flat-exactness fibre theorem: nonlinear compatibility cannot be reduced to torsion alone (Step 71)

**Missing mechanism:** A global argument coupling the torsion zero charge to enough retained harmonic ASD canonical flux to contradict the AAD budget. Specifically:
- The torsion charge $5\chi+6\tau$ forces positive total index
- At each zero, $|W^+|^2\ge s^2/24$ with curvature excess $|\eta|^2+|W_3^+|^2$
- The canonical class $c_1(J)$ has an ASD harmonic projection controlled by a Weitzenböck equation containing $W^-$
- No current argument forces enough of the AAD budget into the $\|c_1(J)^-\|^2$ or Weyl-fluctuation terms

**Assessment:** This problem has the most developed infrastructure and the clearest identified global mechanism. The key question is precise and mathematical: can the topology of the zero set force the canonical ASD harmonic flux to be large enough to exhaust the torsion budget? This requires combining the degree/index structure of torsion zeros with the Bochner/Weitzenböck analysis of ASD 2-forms—a genuine mathematical problem with well-defined inputs. A resolution (either integrability proof or counterexample identification) would be a major result.

## 3. Comparative leverage and recommendation

| Problem | Infrastructure | Identified mechanism | Tractability | Value |
|---------|---------------|---------------------|-------------|-------|
| 1 | Low | None identified | Very hard | High |
| 2 | Medium | Cell optimization saturated; need lower bound | Hard | High |
| 3 | High (conditional) | Need unconditional PDE | Hard (different skills) | High |
| 4 | High | Global torsion-canonical transport | Moderate-to-hard | Very high |

**Recommendation:** Problem 4 has the highest expected research value per unit of effort. The local infrastructure is complete (no finite-order obstruction, complete strict model, torsion zero classification, half-twistor structure), and the global question is precisely formulated. The AAD-LeBrun inequality provides the budget framework; what remains is a single decisive transport argument.

The specific mathematical target is:

**Theorem (target).** On a closed Einstein almost-Kähler four-manifold $(M,g,J,\omega)$ with $s<0$, the torsion vanishes identically.

**Proof strategy.** Use the Weitzenböck equation on the canonical connection, the ASD harmonic projection of $c_1(J)$, the zero-set topology from Armstrong's charge, and the AAD budget to force $T_{\rm AK}=0$.

The alternative outcome—a closed counterexample—would require constructing a compact quotient of the Bianchi VIII model or a fundamentally new compact AKE geometry. This is also a legitimate resolution.

## 4. Secondary directions to preserve

- The orbifold exclusion results should be documented as a complete restricted theorem.
- A02's Theorem 54.A dichotomy and its conditional implications for Problem 3 should be inherited without further conditional extension.
- The $P_*>0$ question at $k=A/3$ (where Einstein is excluded but the classical bound vanishes) is a concrete intermediate target for Problem 2 that may be more tractable than the full open range.
- The Wahl/rational-ball k≥2 parity question (A02 #874) should be answered as it constrains the degeneration picture.

## 5. A02 coordination

A02's latest message #874 contains:
1. Extended screen for general hosts (BMY defect): correct and useful
2. Lattice filter confirmation: agrees with our root subsystem theorem
3. Full-absorption budget: D_{≥6} is the only surviving full-absorption Kronheimer mechanism
4. Questions: Šuvaina d≥2 lattice and k≥2 parity

Responses:
- The $d\ge2$ Şuvaina fibre $N_{d,n}$ is the free $\mathbb Z_n$ quotient of the $A_{dn-1}$ Milnor fibre and has $\pi_1=\mathbb Z_n$, $\chi=d$, and $b_2=d-1$. Its negative intersection lattice is $A_{d-1}(-1)$, of determinant $d$ (not $-I_{d-1}$). One derivation is as follows. Upstairs, $H_2$ is the negative $A_{dn-1}$ root lattice. The $\mathbb Z_n$-invariant sublattice consists of vectors constant on each of the $d$ orbits of $n$ coordinates and has form $nA_{d-1}(-1)$. Pullback under the degree-$n$ cover multiplies intersections by $n$. Downstairs, $|H_1(\partial N)|=dn^2$, $H_1(N)=\mathbb Z_n$, and the boundary map is onto, so $|\det Q_N|=dn^2/n^2=d$; comparing determinants shows that pullback is the full invariant sublattice and $Q_N=A_{d-1}(-1)$. This matches Şuvaina's construction of $N_{d,n}$ as the quotient of the $A_{dn-1}$ fibre \cite{suvaina2011ale}.
- The n=2 parity law IS largely $k=1$-specific. At $k\ge3$, the vector $v=e_1+e_2+e_3+e_4\in-I_{k+1}$ has $v^2=-4$, is primitive (gcd of coordinates is 1), and its perpendicular complement has rank $k$ and contains $D_3=A_3$ as a root subsystem. So the $n=2$ EH/$\mathbb Z_2$ Wahl ball embeds for $k\ge3$. At $k=2$, one needs a primitive vector of square $-4$ in $-I_3$: $v=(1,1,1,1)$ doesn't fit in rank 3, but $v=(2,0,0)$ is not primitive. However $v=(1,1,1,\cdot)$ would need rank $\ge3$ coordinates with $\sum a_i^2=4$ and $\gcd=1$: $(1,1,1,1)$ needs rank $4$ so $k+1\ge4$, i.e., $k\ge3$. For $k=2$, $-I_3$ has no primitive vector of square $-4$ (need $a^2+b^2+c^2=4$ with $\gcd(a,b,c)=1$: $(2,0,0)$ fails primitivity; $(1,1,1,1)$ needs 4 coords). So $k=2$ also excludes $n=2$.

Summary (as first written): the $n=2$ Wahl ball is lattice-obstructed for $k=1,2$ and lattice-allowed for $k\ge3$.

**Correction (Step 79, after A02 #876/#878).** The $k\ge3$ statement used only primitivity of a square-$(-4)$ vector and is withdrawn. The correct integral-gluing condition (A02 Question 96.W, resolved as Prop. 98.W/Cor. 98.V in `Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md` §3) requires an index-$n$ sublattice of the complement with determinant $n^2$ whose discriminant *bilinear* form is anti-isometric to the linking form of $L(n^2,na-1)$, together with null-homotopy of $B\to X$; for torsion-free $\pi_1(X)$ the Wahl boundary map into the complement vanishes and the discriminant form is the lens linking form. A02 finds this realizable for $k\ge5$ per point (primitive $v$ on five coordinates with $v^2=-N$, $N\equiv-\sigma(na-1)u^2 \bmod n^2$; 54 cases, `Sessions/S1003A02/workspace/scripts/step98_wahl_gluing_lattice.py`). The $e_1+\dots+e_4$ reading for $k=3,4$ is not a valid embedding certificate. The general-$k$ second-filling chain condition and the $w_2$/spin$^c$ refinement remain unexamined. What survives from this paragraph is only that Theorem 55.5's parity law is specific to $k=1$.
