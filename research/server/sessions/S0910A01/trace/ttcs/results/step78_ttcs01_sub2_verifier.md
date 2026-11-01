# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md",
    "Sessions/S0910A01/workspace/data/step78_equivariant_construction.json",
    "Sessions/S0910A01/workspace/data/step78_rank_one_orthogonality.json",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md"
  ]
}
```

## Task

Verify the three structural theorems for the A-equivariant diagonal reduction of the Einstein desingularization of (S^2 x S^2)/Z_2, and check the order analysis.

1. SCALAR KERNEL ELIMINATION: The simultaneous antipodal A(x,y)=(-x,-y) is orientation-preserving, commutes with sigma, and acts on product harmonics as (-1)^{l1+l2}. The four scalar P-kernel modes u_i*g_j have l_total=1 (odd), so are A-odd. An A-invariant residual is orthogonal to them. Check this carefully: is it really true that A is orientation-preserving in 4D? That it commutes with sigma? That l1+l2=1 for the kernel modes?

2. SCALAR DECOUPLING: For in-kernel zeta in span{omega_2,omega_3}, compute omega_k^+ circ omega_l^- for k,l in {2,3} in the standard product frame. Verify they all have zero trace on each S^2 factor. Therefore H^4(zeta) has zero scalar-sector coupling. Note the contrast: omega_1^+ circ omega_1^- = -(g1-g2), which IS scalar. So only in-kernel directions decouple from scalars.

3. ORDER ANALYSIS: The Ozuch necessary conditions give t^2*mu_k = O(t^{5/2}), so mu_k -> 0. The inter-node Green response contributes at O(t^3). Since 5/2 < 3, we have t^{5/2} >> t^3 for small t. Check: is this comparison correct? Does it really mean the inter-node term is BELOW the remainder? If so, the leading reduced equation is simply mu_k(alpha) = 0 at each orbit, with no inter-node coupling.

4. RANK-ONE ORTHOGONALITY: R^- = diag(Lambda,0,0) and rho(zeta)^- = (0,cos alpha,sin alpha) for in-kernel zeta. Verify R^- * rho(zeta)^- = 0. Verify the curvature modification dR^- is block-diagonal (entries (1,2) and (1,3) are zero). Does this suggest all mu_k vanish? What caveats apply?

Be precise about any errors in the reasoning.

## Output

# Verification Memo: A-equivariant reduction for the (S²×S²)/Z₂ Einstein desingularization

Prepared for the core research agent. I worked through each of the four structural results, recomputing the tensor algebra where the notes report numerics, and I checked the order accounting against the finite-dimensional expansion written in Step 77 §6.

## 1. Scalar kernel elimination — the symmetry facts hold

All three sub-facts are correct.

**A is orientation-preserving on the 4-manifold.** The antipodal map on a single S² is $-I$ on $\mathbb R^3$ restricted to the sphere; as a self-map of S² it has degree $(-1)^{n+1}=(-1)^3=-1$, hence reverses the 2D orientation. On the product $dA = da_1\oplus da_2$, so $\det dA = (-1)(-1)=+1$. Orientation of $S^2\times S^2$ is preserved. Correct.

**A commutes with σ.** On each factor the antipodal map is literally $-I$ on $\mathbb R^3$, which commutes with every rotation, in particular with $r_\pi$. The spherical-coordinate check in the note ($A:(\theta,\phi)\mapsto(\pi-\theta,\phi+\pi)$, $r_\pi:(\theta,\phi)\mapsto(\theta,\phi+\pi)$) is consistent, but the $-I$ observation makes commutation immediate. Correct.

**l₁+l₂=1 for the kernel modes.** The modes are $u_i\,g_j$ with $u_i=Y_{1,0}$ on factor $i$ and $g_j$ the parallel round metric on factor $j$. Since $A$ is an isometry, $A^*g_j=g_j$, so the parity of $u_i g_j$ under $A^*$ equals that of the scalar $u_i$. Under the antipodal map $Y_{l,m}\mapsto(-1)^l Y_{l,m}$; for $l=1$ this gives $A^*u_i=-u_i$. The function factor carries $(l_1,l_2)=(1,0)$ or $(0,1)$, total 1, odd. Every one of the four modes (and any linear combination) is therefore A-odd, so the entire four-dimensional kernel sits in the A-odd sector. The orthogonality identity $\langle h,\psi\rangle=\langle A^*h,A^*\psi\rangle=-\langle h,\psi\rangle=0$ for A-invariant $h$ and A-odd $\psi$ is the standard isometry-invariance argument and is valid.

**One point that must hold for the reduction to be genuine.** The elimination works only if the *entire* approximate metric is A-invariant. A acts freely on $S^2\times S^2$ (no point equals its antipode) and exchanges the node orbits $\{(N,N),(S,S)\}$ and $\{(N,S),(S,N)\}$ without fixing any node. So A-invariance forces the bubble at $(S,S)$ to be the A-transport of the bubble at $(N,N)$ (matched $t,\alpha$), and likewise for the second orbit — exactly the four-parameter family $(t_1,\alpha_1,t_2,\alpha_2)$. This is consistent and imposes no relation internal to a single node. Section 1.4's statement $A^*R^\pm=R^\pm$ (A preserves $\Lambda^+\oplus\Lambda^-$ because it preserves orientation) is what makes the A-equivariant gluing compatible with the chirality assignment. The construction is internally coherent. Worth recording explicitly: A also fixes the image of (equator × equator), a 2-torus, but this locus is disjoint from the four polar nodes, so it does not interfere.

## 2. Scalar decoupling — verified by direct matrix computation

I reconstructed the endomorphisms in the product frame $(e_1,e_2 \text{ on factor 1}, e_3,e_4 \text{ on factor 2})$ with
$$\omega_1^\pm=e^{12}\pm e^{34},\quad \omega_2^\pm=e^{13}\pm e^{42},\quad \omega_3^\pm=e^{14}\pm e^{23},$$
and computed the diagonals of the compositions.

- $\omega_2^+\circ\omega_2^-$: I get diagonal $(-1,+1,-1,+1)$. Factor-1 trace $=-1+1=0$, factor-2 trace $=-1+1=0$. Factor-traceless. Matches the note and `step78_equivariant_construction.json`.
- $\omega_1^+\circ\omega_1^-$: I get diagonal $(-1,-1,+1,+1)=-(g_1-g_2)$ with $g_1=\mathrm{diag}(1,1,0,0)$, $g_2=\mathrm{diag}(0,0,1,1)$. Factor traces $-2$ and $+2$: not factor-traceless. This confirms the contrast — the out-of-kernel $\omega_1$ direction lands in the scalar sector.

The cross terms $\omega_2^+\circ\omega_3^-$ etc. having zero diagonal is consistent with my basis. Since for in-kernel $\zeta=c\,\omega_2+s\,\omega_3$ the tensor $H^4$ is a bilinear combination only of $\omega_{k}^+\circ\omega_l^-$ with $k,l\in\{2,3\}$, and each such term is factor-traceless, $H^4$ is factor-traceless pointwise in the product frame. The coupling $\langle f\,g_k,H^4\rangle$ contracts $H^4$ against $g_1$ (which extracts $H^4_{11}+H^4_{22}$) or $g_2$ (extracts $H^4_{33}+H^4_{44}$), so factor-tracelessness kills the coupling for every scalar profile $f$. Theorem 3.1 is verified at the tensor-algebra level, and the "regardless of $f$" statement is justified because the vanishing is in the tensor indices, not the angular function.

The reported max factor-trace $5.5\times10^{-17}$ over 37 angles is the expected floating-point zero. No error here.

## 3. Order analysis — the inequality is right; the useful hierarchy is three-tiered

The numerical comparison is correct: $5/2=2.5<3$, so for small $t$, $t^{5/2}\gg t^3$, with $t^3/t^{5/2}=t^{1/2}\to0$. The inter-node response, entering as $t_i t_j^2\mathcal I_{ij,k}=O(t^3)$ at comparable scales, is smaller than the $O(t^{5/2})$ remainder.

I want to make the full hierarchy explicit, because the statement "does not appear in the leading equation" rests on it. With $\lambda^{(0)}=0$ for in-kernel directions, the finite-dimensional map from Step 77 §6 reads
$$F_{i,k}=t_i^2\mu^{(0)}_{i,k}(\alpha_i)+\sum_{j\ne i}t_i t_j^2\mathcal I_{ij,k}+O(t^{5/2}),$$
and since $\mu_k$ is a scale-independent coefficient, the self term is genuinely $O(t^2)$. The ordering at comparable scales is therefore
$$t^2\ \gg\ t^{5/2}\ \gg\ t^3.$$
The leading balance at $O(t^2)$ is $\mu_k(\alpha_i)=0$, decoupled between orbits; the inter-node term sits two tiers down. So Theorem 4.1 is consistent, and the reason it decouples is not merely that inter-node is below the remainder — it is that both the remainder and the inter-node term are strictly below the leading self-obstruction. That is a stronger and cleaner statement than the note's §4.3 phrasing, which compares only inter-node against remainder.

Two things the reader should keep in mind. First, the equal-scale hypothesis is essential: the note's own Remark shows that at $t_1\gg t_2$ the orbit-2 equation becomes $t_2^2\mu_k+t_2 t_1^2\mathcal I_{21,k}=O(t_1^{5/2})$, and $t_2 t_1^2$ can dominate $t_2^2$ once $t_2\ll t_1^2$; there the inter-node term is not subleading. Second, "leading reduced equation is $\mu_k=0$" is the leading finite-dimensional condition only; producing an actual Einstein metric still needs the inverse estimate on the non-scalar sector and the nonlinear remainder control listed in §8. The order analysis establishes the shape of the leading equation, not existence.

## 4. Rank-one orthogonality — computations correct, but "no mechanism" is stronger than what is shown, and a counting question is decisive

**The linear-algebra facts check out.** For $S^2(\rho)\times S^2(\rho)$ the curvature operator is $\Lambda$ on $\omega_1^\pm$ (the two area forms) and 0 on the mixed forms $\omega_{2,3}^\pm$, so $R^\pm=\mathrm{diag}(\Lambda,0,0)$, rank 1. The trace-free (Weyl) part is $\mathrm{diag}(\tfrac23,-\tfrac13,-\tfrac13)\Lambda$, matching the reported Weyl eigenvalues. With $\rho(\zeta)^-=(0,c,s)$,
$$R^-\rho(\zeta)^-=\mathrm{diag}(\Lambda,0,0)\,(0,c,s)^\top=0.$$
Verified.

I also recomputed the curvature modification. With $\rho(\zeta)^-\otimes\rho(\zeta)^-$ having only the lower-right $2\times2$ block $\begin{psmallmatrix}c^2&cs\\cs&s^2\end{psmallmatrix}$ (trace 1), the trace-free projection subtracts $\tfrac13 I$, and $\times12$ gives exactly
$$dR^-=\begin{pmatrix}-4&0&0\\0&12c^2-4&12cs\\0&12cs&12s^2-4\end{pmatrix}\Big/r^6.$$
The $(1,2),(1,3)$ entries vanish, and the kernel-block determinant is $(12c^2-4)(12s^2-4)-144c^2s^2=-48(c^2+s^2)+16=-32$, independent of $\alpha$. All matches `step78_rank_one_orthogonality.json`.

**Where the reasoning is stronger than what is established.** Section 5.3 states "the curvature provides no mechanism to produce a nonzero second obstruction." This phrasing is in tension with §5.4 and with the computation just above: $dR^-$ has a nonzero $(1,1)$ entry $(-4)$ and a nonzero kernel block with determinant $-32$. The vanishing that is actually proven is narrower — the *leading contraction* $R^-\rho(\zeta)^-$ is zero, and $\nabla R=0$ removes derivative-of-curvature terms. But the nonzero kernel block of $dR^-$ is itself a candidate contribution to $\mu_2,\mu_3$, since the Biquard second obstruction is a quadratic form that can feed on the modified curvature within the kernel directions, not only on the bare $R^-\rho$ product. Step 77 §2 states this correctly: the determinant identity gives $\mu_1=0$ for the bare rank-one block and *nothing more* until the Biq16 component formulas for $\mu_2,\mu_3$ are evaluated in this basis. Step 78 §5.3 does append the same reservation in its final sentence, so the two notes agree in substance; the summary sentence "no mechanism" simply reads as more settled than the mathematics supports. I would keep Step 77's formulation as the operative one.

**The counting question that decides the route.** Per orbit the free data entering the leading equation is a single angle $\alpha$ (the scale $t$ does not enter $\mu_k$). The leading conditions are $\mu_1=\mu_2=\mu_3=0$; $\mu_1\equiv0$ is settled, leaving $\mu_2(\alpha)=\mu_3(\alpha)=0$ — two functions of one variable. This is the pivotal issue:

- If $\mu_2,\mu_3$ are two *independent* functions of $\alpha$, then one angle cannot annihilate both at a common root; the leading system is solvable only if $\mu_2\equiv\mu_3\equiv0$ identically in $\alpha$. In that case rank-one orthogonality is not merely supportive but strictly necessary, and it must be upgraded to an identity via the full Biq16 evaluation.
- If instead $(\mu_2,\mu_3)$ transform covariantly under the $SO(2)$ rotation of the kernel plane $\{\omega_2,\omega_3\}$ — i.e. behave as the two components of one object whose modulus is the invariant — then the pair reduces to a single real condition. If that modulus is $\alpha$-independent it is again all-or-nothing; if it depends on $\alpha$ it could vanish at isolated angles.

Which of these holds is exactly what $R^-\rho=0$ plus block-diagonality cannot settle, and it is the difference between "the leading equation is automatically satisfied" and "the leading equation is generically unsolvable." The explicit Biquard component computation for $\mu_2,\mu_3$ in the adapted basis, including the effect of the nonzero $dR^-$ kernel block, is the object that resolves it. This is item 1 of Step 78 §8 and item 3 of Step 77 §6; the memo simply names why it is decisive rather than merely desirable.

## Connection to the overall research problem

These notes construct machinery toward a single positive Einstein metric on the smooth type $\#3(S^2\times S^2)$ (even $b_2=6$, spin, $\chi=8$, $\tau=0$ — internally consistent across Steps 77 and 78). Step 77 §5 already records that producing or excluding such a metric on one 4-manifold does not settle the sign-unrestricted, all-dimension pinching proposition of the research goal. Nothing in the present four results changes that; they are structural inputs to a 4-dimensional existence question, and the bridge from "Einstein metric exists on this specific manifold" to the pinching-implies-Einstein proposition is not drawn in these files. The core agent should treat the four verified/near-verified results as reliable local structure and keep the Biq16 evaluation of $\mu_2,\mu_3$ (with the counting resolution above) as the substance that determines whether even the 4-dimensional construction closes.

### Summary of findings
- Item 1: correct, including orientation, commutation, and parity; the freeness of A and the requirement that the whole approximate metric be A-invariant are the operative structural facts.
- Item 2: correct; I reproduced the diagonals of $\omega_k^+\circ\omega_l^-$ and confirmed factor-tracelessness for in-kernel directions and the scalar $-(g_1-g_2)$ for $\omega_1$.
- Item 3: the inequality and the decoupling are correct; the clean statement is the three-tier hierarchy $t^2\gg t^{5/2}\gg t^3$, valid at comparable scales, with the unequal-scale regime genuinely different.
- Item 4: $R^-\rho=0$ and the block-diagonal $dR^-$ (det $-32$) are correct; "no mechanism for a nonzero second obstruction" overstates what is proven, since the nonzero kernel block is itself a candidate contribution; and the two-functions-in-one-angle counting makes the identical vanishing of $\mu_2,\mu_3$ (or their $SO(2)$-covariant reduction) the deciding computation.