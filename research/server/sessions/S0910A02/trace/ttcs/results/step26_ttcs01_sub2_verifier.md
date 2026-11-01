# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step26_nilpotent_abelian_forcing_audit.md",
    "Sessions/S0910A02/workspace/data/step26_nilpotent_submersion_balance.json",
    "Sessions/S0910A02/workspace/data/step26_heisenberg_moving_frame_ricci.json",
    "Sessions/S0910A02/workspace/notes/step25_structural_resolution_landscape.md",
    "Sessions/S0910A02/workspace/notes/step24_all_dim_positive_collapse_architecture.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/2211.09998-Collapsed-Manifolds-with-local-Ricci-bounded-Covering-Geometr--4e46d62a6fcb--f76980c4eb0a/object.md",
    "Knowledge/objects/papers/Ricci-positive-metrics-on-connected-sums-of-projective-spaces--17bdbf22f9bb--cb9ce73e65bd/object.md"
  ]
}
```

## Task

Verify the Step-26 nilpotent abelian-forcing audit for the Yau-26 positive branch. Focus on mathematical correctness and theorem-shaping consequences: (i) the Heisenberg intrinsic Ricci/anistropy pattern; (ii) the twist-only rank/center bound and whether it is narrow; (iii) the cohomogeneity-one diagonal H3 moving-frame Ricci formulas and the claim that T-active local exact Ric=+1 data with large bracket are algebraically possible; (iv) whether this really defeats a pointwise Milnor-only abelian-forcing theorem and supports a graded/relative-rate theorem instead; (v) source-scope claims about Kapovitch--Wilking/Naber--Zhang/Rong. Do not invent external facts; if exact O'Neill formulas are needed but not in the files, state the missing source need precisely. Please give a direct scientific memo: corrections, confirmed parts, and what theorem statement remains viable.

## Output

# Verifier Memo — Step-26 Nilpotent Abelian-Forcing Work (Yau-26 positive branch)

## Bottom line

The mathematical content of the Step-26 note is correct on every point I could recompute independently. The Heisenberg Ricci pattern, the totally-geodesic twist rank estimate, the cohomogeneity-one moving-frame Ricci formulas, the Hamiltonian constraint, and the scalar identity all check out. The central conclusion — that a Milnor-only pointwise forcing argument is defeated once the fiber second fundamental form is admitted, and that any true statement must be graded/relative-rate — is sound. The source attributions to Kapovitch–Wilking, Naber–Zhang, and Rong are accurate in substance. Two things should be sharpened: the note is over-cautious about the O'Neill input (a usable totally-geodesic vertical Ricci formula is present in-file, Burdick Lemma 2.5), and the connection between the local germ and genuine collapse deserves a more explicit statement, because it is precisely where the two-sided $C^0$ pinching hypothesis stops delivering what the target theorem needs.

## 1. Confirmed computations

**Heisenberg intrinsic Ricci.** For a left-invariant metric with orthonormal bracket $[e_1,e_2]=b e_3$, the known unit-$b$ sectional curvatures ($K_{12}=-3/4$, $K_{13}=K_{23}=+1/4$) give $\operatorname{Ric}=(-1/2,-1/2,+1/2)$; scaling the single structure constant makes curvature scale as $b^2$, hence $\operatorname{Ric}=(-b^2/2,-b^2/2,+b^2/2)$, $\operatorname{scal}=-b^2/2$, center-minus-generator anisotropy $=b^2$. Confirmed.

**Twist-only rank estimate.** With totally geodesic fibers the O'Neill vertical Ricci is $\operatorname{Ric}^V_M(U,U)=\operatorname{Ric}^F(U,U)+\sum_i|A_{X_i}U|^2$. Using $\langle A_{X_i}U,X_j\rangle=-\langle A_{X_i}X_j,U\rangle$ one gets $Q(U,U)=\sum_{i<j}2\langle\omega_{ij},U\rangle^2$ with $\omega_{ij}=A_{X_i}X_j$, so $Q\ge0$ and $\operatorname{rank}Q\le\binom{d}{2}$. For $H_3$ Einstein-normalized to $\operatorname{Ric}=g$, $Q=\operatorname{diag}(1+b^2/2,\,1+b^2/2,\,1-b^2/2)$; positive-definiteness for $b<\sqrt2$ forces rank 3 hence $\binom d2\ge3$, i.e. $d\ge3$; at $b=\sqrt2$ the center entry vanishes (rank 2, still $d\ge3$ since $\binom22=1$); for $b^2/2>1+\delta$ the center entry drops below $-\delta$, incompatible with $Q\ge0$. The immediate upper-pinching statement $b^2/2\le 1+\delta$ follows because $Q_{33}\ge0$ forces the total center Ricci $\ge b^2/2$. All entries of the JSON table are internally consistent. The "clean but narrow" reading is right: this is a genuine $T=0$ obstruction, not the general collapse statement.

**Cohomogeneity-one moving-frame Ricci.** With $e_0=\partial_t$, $e_1=a^{-1}E_1$, $e_2=a^{-1}E_2$, $e_3=c^{-1}E_3$, the anholonomy $[e_0,e_i]=-k_ie_i$ ($k_1=a'/a$, $k_3=c'/c$), $[e_1,e_2]=be_3$ with $b=c/a^2$ is correct. The three reported components follow from the standard $dt^2+g_t$ decomposition: $\operatorname{Ric}_{00}=-(\operatorname{tr}S'+\operatorname{tr}S^2)=-2(k_1'+k_1^2)-(k_3'+k_3^2)$; the tangential components equal the intrinsic fiber Ricci (Milnor $\mp b^2/2$) minus $k_i'+Hk_i$ with $H=2k_1+k_3$. Expanding matches the symbolic matrix in `step26_heisenberg_moving_frame_ricci.json` exactly, and both Ricci sign conventions there agree. The diagonal form (no off-diagonal Ricci) is consistent with the $E_1\!\leftrightarrow\!E_2$ symmetry of the ansatz, and the symbolic output confirms it.

**Constraint and scalar identity.** Substituting the vertical $\operatorname{Ric}_{ii}=1$ equations into $\operatorname{Ric}_{00}$ gives $\operatorname{Ric}_{00}=\tfrac{b^2}{2}+2k_1^2+4k_1k_3+3$, hence $\operatorname{Ric}_{00}-1=\tfrac12(4k_1^2+8k_1k_3+b^2+4)$; the Hamiltonian constraint $4k_1^2+8k_1k_3+b^2+4=0$ is therefore exactly $\operatorname{Ric}_{00}=1$. The sample data $b_0=20,k_1=10,k_3=-10.05$ satisfy it ($400-804+400+4=0$), and $b'=b(k_3-2k_1)=20(-30.05)=-601$ as reported. I also verified $\operatorname{scal}_M=\sum_\mu\operatorname{Ric}_{\mu\mu}=-\tfrac{b^2}{2}-4k_1'-2k_3'-6k_1^2-4k_1k_3-2k_3^2$ term by term. All confirmed.

## 2. The T-active model and its effect on pointwise forcing

The sample is a genuine local exact $\operatorname{Ric}=+g$ germ on a short $t$-interval, with all four diagonal components equal to $1$ and off-diagonals vanishing. It demonstrates cleanly that large orthonormal bracket $b$ is locally compatible with exact positive Einstein data — at the price of large anisotropic shape operator ($2k_1^2+k_3^2\approx301$ at $t=0$) and rapid relative evolution ($b'\approx-601$). This is exactly the content needed to defeat the Step-25 pointwise argument, which used only the intrinsic fiber term $-cb^2/\varepsilon^2$ and omitted the $T$ contribution to the total vertical Ricci. The inference "total Ricci bounded $\Rightarrow$ bracket bounded" is not valid pointwise; the note's correction is right.

One point to make explicit for theorem-shaping. The germ has no collapse parameter; it is at unit scale with $b$ and $|T|$ both $O(20)$. The link to collapse is carried entirely by the separate scaling analysis (§5), and that analysis is the substantive part: homothetic collapse ($\gamma=\alpha$) forces $b=\varepsilon^{-\alpha}\to\infty$, so to hold $\operatorname{Ric}=+1$ one needs $|T|\sim b\to\infty$; graded ($\gamma=2\alpha$) keeps $b=O(1)$; super-graded ($\gamma>2\alpha$) sends $b\to0$. The scale-invariant product $b\cdot\text{diam}$ stays $O(1)$ in the homothetic column, which is the almost-flat (Gromov) signature. So the operative dichotomy is: bounded-curvature collapse keeps $|T|$ bounded and then the Milnor term genuinely dominates (forcing abelian at the bracket scale), whereas an unbounded-$|T|$ collapse is the only way nonabelian brackets persist against positive pinching. Under two-sided $C^0$ Ricci alone $|T|$ is not bounded — this is exactly the CZ-spike phenomenon recorded in the earlier steps — so the abelian-forcing statement cannot be a consequence of pinching by itself. The note states this ("collapse-to-fibration regularity bridge under $C^0$ Ricci only") but it is the crux and should be foregrounded rather than left in the closing paragraph.

## 3. Source grounding (KW / Naber–Zhang / Rong)

The attributions match the supplied excerpts in substance:

- **Naber–Zhang / Kapovitch–Wilking.** Theorem 2.26 (KW): for $\operatorname{Ric}\ge-(n-1)$, $\Gamma_{\epsilon_1}(p)$ is $(w(n),n)$-nilpotent — present and correctly quoted. Theorem 2.27: near a $k$-dimensional Ricci-limit space, the fibered group is $(w_0,n-k)$-nilpotent with rank $\le n-k$ — present. The maximal-rank $\Rightarrow$ noncollapsed-cover statement is carried by Theorem 5.1 (noncollapse $\operatorname{Vol}(B_{1/2}(\tilde q))\ge v_0$ plus splitting); "Proposition 5.9" is referenced in the text as the detailed vehicle, so the pointer is legitimate even though the excerpt shows the packaged statement as Theorem 5.1.

- **Rong.** Local $(\rho,v)$-bound Ricci covering geometry, the HKRX maximally-collapsed infra-nil statement (Theorem 0.3), the nilpotent fiber-bundle theorem under GH-closeness to a noncollapsed lower-dimensional manifold plus local rewinding volume lower bound (Theorem B), and the rank estimate/noncollapse under maximal rank (Theorem C, C1) are all present and correctly summarized.

The synthesis — lower Ricci alone gives almost-nilpotent short-loop groups, but the controlled submersion with usable $A,T,N$ needs the extra local rewinding volume lower bound and GH base regularity — is the correct reading of these sources. Line-number precision cannot be checked from the excerpts, but no attributed statement is misdescribed.

A refinement worth adding, because it sharpens the target theorem's structure. NZ Theorem 1.1 requires $|\operatorname{Ric}|\le n-1$ (which pinching supplies), GH-closeness to $\mathbb R^{k-\ell}\times Z^\ell$ with $\dim Z^\ell\le 3$, and **maximal** fibered rank; under these it yields a uniform curvature bound on the regular region, hence bounded $T$ there. On that maximal-rank region the intrinsic Milnor term therefore dominates and an abelian-forcing-type conclusion is within reach. The genuine difficulty is concentrated on the non-maximal-rank strata (the K3 $I_1$-type singular fibers, Eguchi–Hanson at $\ell=4$), where curvature is unbounded. The $\dim Z^\ell\le 3$ restriction is sharp (Remark 1.3, Example 3.3) and is itself a real structural obstacle for higher-dimensional collapse, not just a technical hypothesis. Stating the target theorem region-by-region (regular maximal-rank vs. singular strata) would make it more defensible.

## 4. Precise missing analytic input

The note reports that a direct O'Neill/Besse formula was not ingested and treats the twist term cautiously. In fact the totally-geodesic vertical Ricci is available in the supplied Burdick paper, Lemma 2.5: for $T=0$,
$$\operatorname{Ric}_{\tilde g}(U_j,U_j)=\frac{\operatorname{Ric}_{\hat g}(V_j,V_j)-(n-1)f'^2}{f^2}-\frac{f''}{f}-m\frac{f'h'}{fh}+\big(\operatorname{Ric}_g(V_j,V_j)-\operatorname{Ric}_{\hat g}(V_j,V_j)\big)\frac{f^2}{h^4},$$
where the last term is exactly $\sum_i|A_{X_i}V_j|^2=Q(V_j,V_j)\ge0$. This corroborates the sign and structure of $Q$ used in §3 and the rank identity. So the twist-only analysis does not depend on an un-ingested source.

What is genuinely absent from the files, and needed only for the general submersion theorem (not for the cohomogeneity-one germ, which was derived directly by Koszul), is:

1. the full O'Neill/Besse Ricci submersion system with **nonzero** fiber second fundamental form $T$ and mean curvature $N$ (Besse 9.36 in generality) — needed to state the mixed and horizontal equations and to make the $|T|\sim b$ balance quantitative;
2. the coefficient convention for the integrated O'Neill scalar identity on a closed fibration, including the divergence/flux terms at the degeneration locus — the note honestly says this was not certified.

These two are the concrete external inputs to request; both are standard (Besse, O'Neill 1966) and would let the general theorem be written with explicit constants.

Items not independently verifiable from the supplied material: the toric individual-warping equation $-\Delta_B p=(1-K_B)p$ and its endpoint-layer cancellation (§2) come from earlier steps not in the file set, and the peer-message tensor derivations (§7, A01/A03) are outside the provided sources; the note appropriately marks the latter as not personally verified. The endpoint-layer cancellation argument ($\pi^2/L^2\sim2A$ offsetting $K_B=-A$) is dimensional/heuristic and is presented as such.

## 5. Which theorem statement remains viable

The pointwise Milnor-only statement is not viable, and the note is right to retire it. What remains supportable, as a conjecture with named hypotheses, is a graded/relative-rate statement of roughly this form:

> Let a sequence of closed $n$-manifolds with $\operatorname{Ric}\in[1-\delta,1+\delta]$ collapse. On the regular (maximal fibered rank, $\dim Z^\ell\le3$) region, NZ/Rong give a nilpotent fibration with uniformly bounded curvature, hence bounded $T,N$; there the intrinsic Milnor term dominates and the first collapse stage is virtually abelian (torus/circle), producing the determinant-trace / Kaluza–Klein equations. Any surviving nonabelian bracket direction must be graded, relegated to a smaller scale, and treated by iterated abelian stages. Nonabelian bracket persistence at the first collapse scale requires $|T|$ comparable to $b$, which is excluded on the bounded-curvature regular region.

The essential open pieces, in decreasing tractability:
- the regularity bridge from two-sided $C^0$ pinching to a controlled nilpotent fibration is **not** a consequence of pinching alone; it currently needs the local rewinding volume lower bound / GH-noncollapse-to-lower-dim hypothesis (Rong Theorem B) as an added assumption, or equivalently the maximal-rank condition (NZ Theorem 5.1). Establishing this from pinching is the load-bearing unknown;
- control of $|T|$/mean curvature at the collapse scale on non-maximal-rank strata, where curvature is unbounded under $C^0$ Ricci;
- the singular/fixed strata (including the four-dimensional toric fixed-locus adversary and the $\dim Z^\ell=4$ Eguchi–Hanson threshold), where none of the regular-region control applies.

So the graded statement is the correct replacement target, and the Step-26 work has legitimately converted an overstated pointwise assertion into a structurally accurate program. The honest position is that even the first-stage fibration is not yet derivable from pinching without one of the added noncollapse hypotheses; the abelian character of that first stage, once the fibration and bounded $T$ are granted, is the part the computations here genuinely support.