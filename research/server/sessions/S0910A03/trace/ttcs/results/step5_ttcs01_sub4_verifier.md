# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A03/workspace/notes/step4_compactness_synthesis.tex",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Sessions/S0910A03/staging/acquired/2609_01464__Removability_of_non-isolated_singularities_for_Eins_32e2d5864ee030ed/part_001.md"
  ]
}
```

## Task

Check the compactness extraction argument under only |Ric+g|_{L∞}->0 on noncollapsed four-dimensional balls. Using Cheeger–Naber harmonic-radius measure estimates, determine what positive-measure regular patches can be selected, what local convergence follows, whether uniform convergence of the Ricci defect is enough to bootstrap a C^{1,alpha}/W^{2,p} harmonic-chart limit to a smooth Einstein metric, and how an integral deficit O(delta^2) passes to that patch. Explicitly separate noncollapse at one ball, typical-point selection, curvature concentration, collapsing regions, and topology recovery. State exact missing assumptions if the argument fails.

## Output

# Verifier Memo: Compactness Extraction under $\|\mathrm{Ric}_{g_i}+g_i\|_{L^\infty}\to 0$ on Noncollapsed 4-Balls

Setting fixed for this memo: $(M^4,g_i)$ closed, $\|\mathrm{Ric}_{g_i}+g_i\|_{L^\infty}\le\delta_i\to0$ (the $\lambda=-1$ regime). Then for large $i$, $|\mathrm{Ric}_{g_i}|\le 1+\delta_i\le 3=n-1$, so the Cheeger–Naber hypothesis $|\mathrm{Ric}|\le n-1$ holds; scalar curvature $s_i=\mathrm{tr}\,\mathrm{Ric}_{g_i}=-4+\mathrm{tr}\,E_i$ with $E_i:=\mathrm{Ric}_{g_i}+g_i$, so $s_\infty=-4$ in any limit. I trace the extraction piece by piece and separate what the supplied tools actually deliver from what must be assumed.

---

## 1. Noncollapse at one ball

This is a genuine input, not a consequence. The two counterexamples in the notes are correct and each is decisive:

- $\Sigma_g\times\Sigma_{g'}$ with a degenerating hyperbolic factor: exact $\mathrm{Ric}=-g$, fixed volume $16\pi^2(g-1)(g'-1)$, but $\mathrm{Vol}(B(p_i,r))\le C(r)\ell_i\to0$ near the short geodesic. Exact Einstein with fixed topology does not prevent local collapse.
- Anderson's $M_j^4\to T^3$ (Cheeger–Naber Example 2.16): $|\mathrm{Ric}|\to0$, $\mathrm{diam}\le1$, $\mathrm{Vol}\to0$, $b_2\to\infty$. Total collapse under two-sided Ricci control.

So the assertion "$\mathrm{Vol}(B_1(p_i))\ge v>0$ at some $p_i$" cannot be derived from $\|\mathrm{Ric}+g\|_{L^\infty}\to0$ together with fixed topology and volume normalization. It must be posited. The Weyl-profile filter is a real observation but does not repair this: it excludes the *macroscopic bulk* of the known collapse models ($\Sigma_g\times\Sigma_{g'}$ is Kähler with $|W^+|=2/\sqrt6$; hyperbolic cusps are conformally flat with $W^+=0$), yet says nothing about thin necks/cusps of vanishing volume that carry negligible integral deficit.

---

## 2. Typical-point selection and passage of the integral deficit

Given noncollapse $\mathrm{Vol}(B_1(p_i))>v$, the correct selection tool is **Cheeger–Naber Theorem 1.13 / Remark 1.11**, which under $|\mathrm{Ric}|\le3$ + noncollapse gives the sharp weak-$L^2$ estimate on the *harmonic radius*:
$$
\mathrm{Vol}\big(T_r(\{x\in B_1(p_i): r_h(x)\le r\})\big)\le C(v)\,r^4 .
$$
Fixing $r_0$ with $C(v)r_0^4<\tfrac12 v$, the set $\{r_h\ge r_0\}$ has definite measure in $B_1(p_i)$. This estimate uses only bounded Ricci; it does **not** require the Einstein equation or a bound on $|\nabla\mathrm{Ric}|$. I emphasize that it controls the harmonic radius, giving $C^{1,\alpha}\cap W^{2,q}$ charts, **not** the regularity scale $r_x$ (curvature bound $|\mathrm{Rm}|\le r^{-2}$). The regularity-scale upgrade in Cheeger–Naber Theorem 1.13/Remark 1.16 is exactly the step that needs Einstein or $|\nabla\mathrm{Ric}|\le\Lambda$, and the $g_i$ are only approximately Einstein. This distinction is where the step7 note's "Step D" needs care (Section 3).

The volume-random averaging in step7 §4 is valid: with $\mathrm{Ric}_{g_i}\ge-(3+\delta_i)$, Bishop–Gromov gives $\mathrm{Vol}(B_R(x))\le V_{-3}(R)=C(R)$, hence
$$
\mathbb E\Big[\textstyle\int_{B_R(p)}F_i\Big]=\frac{1}{\mathrm{Vol}(M_i)}\int_{M_i}F_i(x)\,\mathrm{Vol}(B_R(x))\,d\mu\le \frac{C(R)}{\mathrm{Vol}(M_i)}\int_{M_i}F_i ,
$$
and Markov gives small $\int_{B_R(p)}F_i$ off a vanishing volume-fraction of basepoints. Two structural points must be separated here, because the note's single functional $F_i=(s_i+4)^2+(|W^+_i|-\tfrac1{2\sqrt6})^2+|E_i|^2$ conflates two different smallness sources:

- **The Ricci/scalar part is genuinely $O(\delta^2)$ and genuinely normalized-small.** Pointwise $|E_i|^2\le\delta_i^2$ and $(s_i+4)^2=(\mathrm{tr}\,E_i)^2\le 4|E_i|^2$, so $\frac1{\mathrm{Vol}(M_i)}\int(|E_i|^2+(s_i+4)^2)\le 5\delta_i^2\to0$ with no further input.
- **The Weyl part is not controlled by $\delta$.** $|W^+_i|-\tfrac1{2\sqrt6}$ is not a pointwise function of $E_i$; the Weyl tensor is not determined by the Ricci defect. Its integral smallness must come from near-saturation of the LeBrun/Chern–Gauss–Bonnet curvature identity (the Cauchy–Schwarz remainder $\int(s+8\sqrt6|W^+|)^2$). Whether this remainder tends to zero **as a total integral** (which, with $\mathrm{Vol}(M_i)$ bounded above and below, then yields normalized smallness and lets the averaging pass it) versus only saturating a positive topological constant is the one item I could not settle from the supplied fragments. This should be read off the LeBrun 2001/2006 quantity ($K_i\to A$, $\mathrm{Vol}\to 32\pi^2A/9$ in step4) before treating $\int F_i/\mathrm{Vol}\to0$ as established. If the remainder is a total-integral quantity tending to $0$, the passage is clean; if it merely saturates, the averaging as written does not yet deliver local Weyl smallness.

Intersecting the noncollapsed fraction (Section 6) with the small-deficit fraction is valid **only when the noncollapsed fraction is definite** — see Section 7(A).

---

## 3. Does uniform Ricci-defect convergence bootstrap to a smooth Einstein limit?

Yes, but the mechanism in step7 "Step C" must be repaired; the corrected route is favorable and needs weaker input than stated.

In harmonic coordinates on a chart with $r_h\ge r_0$, write the standard identity
$$
\mathrm{Ric}_{ij}(g_i)=-\tfrac12 g_i^{kl}\partial_k\partial_l g_{i,ij}+Q(g_i,\partial g_i),
$$
$Q$ algebraically quadratic in $\partial g_i$. Using $\mathrm{Ric}(g_i)=-g_i+E_i$,
$$
-\tfrac12 g_i^{kl}\partial_k\partial_l g_{i,ij}=-g_{i,ij}-Q(g_i,\partial g_i)+E_{i,ij}.
$$

**The step7 claim "RHS converges in $C^\alpha$, so Schauder gives $C^{2,\alpha}$ convergence of $g_i$" is not supported.** The defect $E_i\to0$ only in $L^\infty=C^0$; the near-Einstein hypothesis gives no Hölder decay of $E_i$. Schauder needs the RHS bounded in $C^{0,\alpha}$, which the $E_i$ term does not satisfy. Sequence-level $C^{2,\alpha}$ bounds on the $g_i$ are therefore not available, and consequently one may **not** assert uniform/pointwise $C^\alpha$ convergence of $W^+_i$ along the sequence (Weyl involves $\partial^2 g$).

The correct chain, which reaches the same conclusion with only $C^0$ decay of $E_i$:

1. **Uniform $W^{2,p}$ (all $p<\infty$) bounds** via $L^p$ (Calderón–Zygmund) elliptic theory: $g_i^{kl}\in C^{0,\alpha}$ uniformly (uniformly elliptic), RHS bounded in $L^\infty\subset L^p$. Gives the same $C^{1,\alpha}$ that harmonic-radius control already provided, and weak $W^{2,p}$ compactness.
2. Extract $g_i\to g_\infty$ in $C^{1,\alpha'}$, weakly in $W^{2,p}$.
3. **Pass the equation to the limit.** Coefficients $g_i^{kl}\to g_\infty^{kl}$ in $C^{0,\alpha'}$; $Q(g_i,\partial g_i)\to Q(g_\infty,\partial g_\infty)$ in $C^{0,\alpha'}$; $E_i\to0$ in $C^0$. The limit satisfies, weakly in $W^{2,p}$ harmonic coordinates, $\mathrm{Ric}(g_\infty)=-g_\infty$.
4. **Bootstrap on the limit** (DeTurck–Kazdan): for the fixed metric $g_\infty$ the RHS $-g_\infty-Q(g_\infty,\partial g_\infty)$ is genuinely $C^{0,\alpha}$ (there is no defect term), so Schauder gives $g_\infty\in C^{2,\alpha}$, then $C^\infty$ (real-analytic). Smooth Einstein on the regular part.
5. **Strong $W^{2,p}$ convergence on interior patches.** For $w_i:=g_i-g_\infty$, $L_i w_{i,ij}=(f_i-f_\infty)+(f_\infty-L_i g_{\infty,ij})\to0$ in $L^p$ (first term from $E_i\to0$ in $C^0$; second from $g_\infty$ fixed and coefficients converging), and $w_i\to0$ in $C^{1,\alpha}\subset L^p$. The interior $W^{2,p}$ estimate with uniform constants gives $\|w_i\|_{W^{2,p}(B_{R'})}\to0$. Hence $\mathrm{Rm}(g_i)\to\mathrm{Rm}(g_\infty)$ **strongly in $L^p_{loc}$**.

Consequences for the deficit passage: strong $L^p$ curvature convergence gives $s_i\to s_\infty$, $|W^+_i|\to|W^+_\infty|$ in $L^p_{loc}$, so $\int_{B_{R'}}(s_\infty+8\sqrt6|W^+_\infty|)^2=\lim\int(s_i+8\sqrt6|W^+_i|)^2=0$, i.e. pointwise $s_\infty=-8\sqrt6|W^+_\infty|$; with $s_\infty=-4$, $|W^+_\infty|=1/(2\sqrt6)$ on the regular part. So step7 "Step C/D" reaches a correct target, but the passage is $L^p$/a.e. on the regular part via strong $W^{2,p}$, **not** uniform pointwise convergence of $W^+_i$ along the sequence; the latter is exactly what breaks near concentration points (Section 4). This corrected mechanism is scientifically stronger for the research: it shows the Ricci-defect need only decay in $C^0$, matching what $\|\mathrm{Ric}+g\|_{L^\infty}\to0$ actually supplies.

This convergence level ($C^{1,\alpha}$, strong $W^{2,p}$ off a singular set) is precisely consistent with Anderson orbifold compactness and with Antonelli–Székelyhidi Theorem 1.4 ($C^{1,\alpha}$ structure on the regular set).

---

## 4. Curvature concentration

Even on a noncollapsed patch with $\int_{B_1(p_i)}F_i\to0$, the harmonic-radius estimate permits a residual set $\{r_h=0\}$ of codimension 4. In dimension 4 this is a finite set of points. The supplied results pin the structure of the limit:

- Cheeger–Naber Theorem 1.4: the limit is smooth away from a set of Hausdorff codimension $\ge4$ (isolated points here).
- Cheeger–Naber Theorem 1.13 gives $\fint_{B_1}|\mathrm{Rm}|^2\le C(v)$ (via Chern–Gauss–Bonnet + bubble tree), so Anderson's $L^{n/2}=L^2$ orbifold compactness applies to the (Einstein) limit: **the patch limit is a smooth Einstein orbifold with at most $c(v)$ isolated singular points** (Cheeger–Naber Corollary 8.85; Anderson Theorem 1.1). Blow-ups at concentration points are complete Ricci-flat ALE spaces (Eguchi–Hanson type, Example 2.15).

The Weyl-profile identity $|W^+_\infty|=1/(2\sqrt6)$ holds on the *smooth* part; the note's remark that the profile "restricts bubbles to hyperkähler models" concerns the ALE blow-ups, not the presence/absence of the orbifold points themselves.

On the removability tool (Antonelli–Székelyhidi): Theorem 1.2 removes 4-dimensional $L^\infty$ Einstein singularities of Assouad codimension $>3-\tfrac13=\tfrac83$, and codimension 4 exceeds $\tfrac83$. **But its structural hypothesis is that $g$ is an $L^\infty$ metric on a fixed smooth manifold** ($\Lambda^{-1}h\le g\le\Lambda h$). A genuine orbifold cone point $\mathbb R^4/\Gamma$ ($\Gamma\ne1$) is topologically singular and is not $L^\infty$-equivalent to a smooth metric on a manifold; Theorem 1.4 explicitly gives only $C^{1,\alpha}$ structure on the regular set and not across such a point (indeed [25] constructs $X=X^{\mathrm{reg}}$ with no $C^{1,\alpha}$ structure). So Antonelli–Székelyhidi removes singularities that already sit inside a fixed smooth $M$ with $g\in L^\infty(M)$; it does not by itself eliminate the orbifold cone points produced by bubbling. To reach a smooth-manifold limit one needs an additional energy-gap/$\epsilon$-regularity input precluding concentration, or one accepts an orbifold limit. The codimension threshold is met dimensionally; the $L^\infty$-on-a-manifold hypothesis is the binding one.

---

## 5. Collapsing regions

The volume-random argument controls $\int_{B_R(p)}F_i$ with respect to the volume measure of $M_i$, i.e. it identifies balls that are *typical for volume*. It says nothing about whether those balls are noncollapsed. If the noncollapsed fraction tends to zero (as in the $T^3$ example and the degenerating product), then every typical ball can have small deficit while no ball is noncollapsed, and the harmonic-radius machinery of Sections 2–3 has no entry point. The tools supplied (Cheeger–Naber harmonic-radius estimate, Anderson orbifold compactness, Antonelli–Székelyhidi RCD extension) all take noncollapse as input; none produces it. The Weyl filter removes specific known collapse models as macroscopic bulk but leaves open unknown collapse with $|W^+|\approx1/(2\sqrt6)$, $s\approx-4$, and (from the Bochner computation in step7 §1) $|\nabla W^+|^2\approx1/24$ concentrating in vanishing-volume regions.

---

## 6. Topology recovery

Cheeger–Naber Theorem 1.12 (finite diffeomorphism type) and the bubble-tree decomposition Theorem 8.64 reconstruct 4-dimensional topology, but they require a **diameter bound** $\mathrm{diam}\le D$. The $\lambda=-1$ regime has $\mathrm{Ric}\approx-g$, so there is no Myers control and diameter can be unbounded; the global finite-type/bubble-tree reconstruction is not available as stated. On a fixed $M$ the diffeomorphism type is of course fixed, so "finiteness" is trivial; the substantive issue is whether the limit is diffeomorphic to $M$. Under collapse it need not be (the $T^3$ limit has different topology, $b_2\to\infty$). Under noncollapsed bubbling, Anderson's Mayer–Vietoris reconstruction (Anderson Remark 2.10: $H_*(M_i)$ determined by the orbifold $V$ and the ALE bubbles) recovers the topology, again contingent on the noncollapsed + $L^2$-curvature regime. On a single patch one recovers only that the regular part embeds in $M_i$ for large $i$ (Anderson Theorem 1.1), not a global topological statement.

---

## 7. Exact conditions the extraction requires

The chain "select $p_i$ → harmonic radius → $C^{1,\alpha}\cap W^{2,q}$ → smooth Einstein limit → Weyl profile" is sound **on a noncollapsed patch**, with the Section 3 correction. The conditions it needs, none derivable from $\|\mathrm{Ric}+g\|_{L^\infty}\to0$ + fixed topology + volume normalization, are:

**(A) Definite noncollapsed volume-fraction.** $\exists\,v,\tau>0$ with $\mathrm{Vol}(\{p:\mathrm{Vol}(B_1(p))\ge v\})\ge\tau\,\mathrm{Vol}(M_i)$ for large $i$. This is the load-bearing hypothesis. Without it the intersection of "noncollapsed" with "small deficit" can be empty. Anderson $T^3$-collapse and the degenerating product show it can be violated.

**(B) Normalized Weyl deficit tending to zero.** The $O(\delta^2)$ estimate covers only $\int(|E_i|^2+(s_i+4)^2)/\mathrm{Vol}$. Local smallness of $(|W^+_i|-\tfrac1{2\sqrt6})^2$ requires that the LeBrun Cauchy–Schwarz remainder $\int(s+8\sqrt6|W^+|)^2$ be a total-integral quantity tending to $0$ (not merely a saturating topological constant). This should be verified against the LeBrun 2001/2006 identity before $\int F_i/\mathrm{Vol}\to0$ is used.

**(C) No-concentration / removal of orbifold points.** An energy-gap or $\epsilon$-regularity input (of Einstein type) precluding codimension-4 curvature concentration, or acceptance of an Einstein orbifold limit. Antonelli–Székelyhidi Theorem 1.2 removes codim-$>\tfrac83$ singularities only under the $L^\infty$-on-a-fixed-manifold hypothesis, which orbifold cone points $\mathbb R^4/\Gamma$ do not meet.

**(D) Compactness for any Derdziński/Stokes contradiction.** The patch limit is pointed noncompact/complete, not closed. The conformal factor equation $\Delta f=-f/2$ admits nonconstant solutions on noncompact Einstein manifolds (step7 §2 is correct), so the Kähler-forcing via Stokes — the step that turns $|W^+|=1/(2\sqrt6)$ into a contradiction with $|W^+|^2=s^2/24=2/3$ — is unavailable on a local limit. This is not a defect of the extraction but a structural feature: the $\lambda=-1$ contradiction is inherently global on the compact $M_i$, and no patch limit can close it. The natural continuation is the global Taubes/SW route with integer-invariant stability (step7 §5), which remains open.

**(E) Diameter control for global topology.** Needed for Cheeger–Naber Theorem 1.12 / Theorem 8.64; unavailable from $\mathrm{Ric}\approx-g$.

Net reading: with (A) and (B), the local extraction yields a smooth Einstein orbifold patch limit with $|W^+_\infty|=1/(2\sqrt6)$, the Section-3 corrected mechanism holding under only $C^0$ Ricci-defect decay. The strategy then meets the noncompact wall (D), so the four-dimensional argument does not terminate at the level of local limits and must route through a global mechanism on $M_i$.