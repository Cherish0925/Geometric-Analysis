# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A01/workspace/data/step89_identity_and_spectral_support.json",
    "Sessions/S0910A01/workspace/data/step89_identity_sparse_components.json",
    "Sessions/S0910A01/workspace/notes/step88_four_node_structural_theorem.md",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_receiver.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 89 correction of the product-orbifold chirality calculation. Check the corrected flat principal identity S_odd(V2)=(pi^2/2) R_odd(H) and D:H=-16 R_odd under the stated conventions; check whether the shape tensor q=g_A-g_B is indeed TT with Pq=-q and whether the principal odd source/receiver annihilation of q and scalar zero modes follows from the displayed tensor support; check the finite relative mixed-minus-all-same formulation for point-supported quadrupoles, including diagonal self-term cancellation, lack of inherited positivity, possible even/odd cross terms, and order bookkeeping t^3=o(t^(5/2)) relative to Ozuch Proposition 2.19. Please identify any remaining normalization or conceptual errors and state what is actually established versus still needing geometric/Bianchi/Ozuch matching.

## Output

## Verification memo — Step 89 correction of the product-orbifold chirality calculation

I checked the algebra, the tensor-support argument, the spectral facts, and the ordering estimate. The correction is mathematically sound; below is what I confirmed independently, one imprecision in wording, and a precise statement of what the flat principal identity does and does not settle.

### 1. The corrected normalization is internally coherent and dimensionally right

The three relations
$$S_{\rm odd}/\pi^2=-\tfrac1{32}D_{ijpq}H_{ijpq},\qquad D_{ijpq}H_{ijpq}=-16\,R_{\rm odd}(H),\qquad S_{\rm odd}(V_2)=\tfrac{\pi^2}{2}R_{\rm odd}(H)$$
are mutually consistent: substituting the middle into the first gives $S_{\rm odd}/\pi^2=-\tfrac1{32}(-16R_{\rm odd})=\tfrac12 R_{\rm odd}$, i.e. the third. The four sparse components in `step89_identity_sparse_components.json` each satisfy $D{:}H=-16\,R_{\rm odd}$ term-by-term ($-8=-16\cdot\tfrac12$, $+8=-16\cdot(-\tfrac12)$), so the identity is not just an average but holds on each independent entry.

The Step 88 factor error is correctly located: feeding the Hessian $H$ into the polynomial-coefficient source formula $-\tfrac1{16}D{:}V$ (which expects $V=\tfrac12H$) yields $-\tfrac1{16}D{:}H=R_{\rm odd}$, i.e. $S_{\rm odd}/\pi^2=R_{\rm odd}$ — exactly a factor $2$ above the true $\tfrac12 R_{\rm odd}$. The missing $\tfrac12$ is the $H\!\leftrightarrow\!V_2$ conversion, as stated.

The reported test dimension, $100$, is the correct dimension of $\operatorname{Sym}^2(\mathbb R^4)\otimes\operatorname{Sym}^2(\mathbb R^4)$ ($10\times10$), so "full basis" is the genuine space of tensors symmetric in $(ij)$ and in $(pq)$, not a sample. The axial values $S_{\rm odd}/\pi^2=\tfrac12$, $R_{\rm odd}=1$ satisfy the identity and match the Step 87 receiver data (radial$_+=1$, radial$_-=-1\Rightarrow R_{\rm odd}=1$) and source data ($B_+-B_-=\pi^2\Rightarrow S_{\rm odd}=\pi^2/2$). This chain closes.

### 2. $q=g_A-g_B$ with $Pq=-q$ — confirmed by direct computation

I verified this independently rather than trusting the assertion. On $S^2(1)\times S^2(1)$ with product metric $g=g_A\oplus g_B$:

- $\operatorname{tr}_g q=\dim A-\dim B=0$.
- $g_A,g_B$ are each parallel for the product connection, so $\nabla q=0$; hence $\delta q=0$ and $\nabla^*\nabla q=0$.
- $r_\pi$ is an isometry of each factor, preserving $g_A,g_B$ separately, so $q$ descends.
- For the curvature action $\mathring R(h)(X,Y)=\sum_i h(\mathrm{Rm}(e_i,X)Y,e_i)$: using $\mathrm{Rm}(X,Y)Z=\langle Y,Z\rangle X-\langle X,Z\rangle Y$ on each unit factor and the fact that product curvature is intra-factor, one gets $\mathring R(g_A)=g_A$ and $\mathring R(g_B)=g_B$ (the same computation that yields $\mathring R(g)=\mathrm{Ric}=g$ on the unit sphere). Therefore $\mathring R(q)=q$.

Combining, $Pq=\tfrac12\nabla^*\nabla q-\mathring R q=0-q=-q$. So $q$ is a genuine eigentensor with $P$-eigenvalue $-1$, $q\in(\ker P)^\perp$, and $G_P^\perp q=-q$. The Step 88 premise "all TT eigenvalues positive" is therefore incorrect, and the withdrawal of unconditional positivity is warranted. This is also consistent with the known linear instability of products of positive Einstein factors — the $g_A-g_B$ direction is the classical destabilizing mode of $S^2\times S^2$ — so the sign here agrees with established geometry, not just with the script.

### 3. Principal annihilation of $q$ and the four scalar modes — correct; one wording refinement

The defect tensor $D$ is supported entirely on index quadruples using all of $\{0,1,2,3\}$ with the off-diagonal $C_{2k}/C_{k2}$ structure (raw entries like $(0,1,2,3)$, $(2,3,0,1)$ with the specific antisymmetric tensor-index pairing). For $q$, the quadratic jet in normal coordinates at a node has tensor and derivative indices both inside one factor and in **diagonal** form ($h_{22},h_{33}$, etc.), so $D{:}H=0$, and since $R_{\rm odd}=-\tfrac1{16}D{:}H$ as an identity, $R_{\rm odd}(q)=0$ follows automatically — the two annihilations are one fact, not two.

One precision: the note's stated reason "tensor and derivative indices within a single $S^2$ factor" is exact for $q$ and for $u_Ag_A$, but not literally for the cross modes $u_Ag_B,u_Bg_A$. There the quadratic term $(\text{quad}_A)\cdot\delta_B$ does carry derivative indices in $A$ and tensor indices in $B$ — a genuinely mixed quadruple. It still annihilates $D$ because its tensor part is the **diagonal** $\delta_B$ ($h_{22},h_{33}$), whereas $D$ requires the **off-diagonal** $(2,3)$ tensor component. The operative reason for those modes is exactly the $C_{11}$-versus-$C_{2k}/C_{k2}$ orthogonality that the note also states. The conclusion $S_{\rm odd}=R_{\rm odd}=0$ is correct for all five modes; only the single-factor phrasing under-describes the cross cases.

### 4. Relative mixed-minus-all-same algebra — correct, with the surviving pieces named accurately

The bilinear expansion $L_i^{\epsilon_i}G S_j^{\epsilon_j}=K^{00}+\epsilon_jK^{01}+\epsilon_iK^{10}+\epsilon_i\epsilon_jK^{11}$ and the difference from $\epsilon\equiv1$ are the straightforward expansion/subtraction; correct.

- **Odd–odd diagonal cancellation:** the $i=j$ coefficient of $K^{11}$ is $\epsilon_i^2-1=0$ for $\epsilon_i\in\{\pm1\}$. So the point-supported quadrupole self-pairings $K_{ii}^{11}(\tau)$, which diverge as $\tau\downarrow0$, are multiplied by zero before the limit. This is a real algebraic removal, correctly identified.
- **Surviving diagonals:** the $K^{01},K^{10}$ diagonals carry coefficients $\epsilon_i-1$, which do not vanish. These even–odd/odd–even self-terms at a node are themselves singular and are **not** removed by the comparison. The note states this; it is the correct residual object.
- **No inherited positivity:** even if a $\tau$-regularized $K^{11}_{ij}(\tau)$ were a Gram matrix, deleting its diagonal destroys positivity — a PSD matrix with zero diagonal is identically zero, and $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ shows a PSD-minus-diagonal object is indefinite. Independently, $G_P^\perp$ is not positive (the $q$ eigenvalue $-1$ makes it indefinite), so the full unregularized pairing $\langle S_i,G_P^\perp S_j\rangle$ is not a Gram form either. Both reasons are valid and reinforce each other.

The axial isolated-channel arithmetic checks: $K^{11,\rm axial}_{ij}=\frac{(s_i)(s_j\pi^2/2)}{1\cdot(64\pi^2/9)}=\frac{9}{128}s_is_j$, and $(\epsilon_i\epsilon_j-1)K^{11}=\frac{9}{128}(1-s_is_j)$ using $s_i^2=1$, giving $0$ for equal-sign pairs and $\frac{9}{64}$ for opposite-sign pairs. The JSON's $(1-s_is_j)$ table (value $2$ on opposite pairs, $0$ on equal pairs) matches. This is a rank-one $\lambda=1$ truncation in a provisional asymmetric normalization (receiver carried as $s_i$, source as $s_j\pi^2/2$); a true self-adjoint spectral pairing would use one functional for both, so the constant $9/128$ is normalization-dependent, as the note flags.

### 5. Order bookkeeping $t^3=o(t^{5/2})$ — correct and consistent with Ozuch's own method

As $t\to0^+$, $t^3/t^{5/2}=t^{1/2}\to0$, so $t^3$ is genuinely higher order than $t^{5/2}$. The inter-node scaling $t_i t_j^2$ follows from $H^4(t_j\phi_j)=t_j^2H^4(\phi_j)$ (Ozuch Prop 1.16(1): the $r^{-4}$ term is $\propto|\zeta|^2$) propagated to node $i$ with an extra $t_i$. Ozuch Prop 2.19 gives only $t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2})$ and $\nu_l=O(t_{\max}^{5/2})$, an upper estimate whose ceiling sits **above** a $t^3$ inter-node signal; it cannot resolve that layer. This mirrors Ozuch's own §3.3 program, where he builds the higher-order approximate metrics $\mathbf{eh}^{[10]}$, $\mathbf g_\pm^{[8]}$ precisely to sharpen the estimate to $\lambda_k^j+\mu_k^j=O(|\zeta^\pm|^2|\zeta^\mp|^5+\dots)$ (Corollary 3.25) — i.e. to see effects finer than the crude $t^{5/2}$ bound. The reasoning is right; note that $\mathcal I_{ij}$ is left as a placeholder for the inter-node pairing, not derived, and whether its matched $\tau\downarrow0$ limit exists is not settled.

### 6. What is established versus what still needs geometric / Bianchi / Ozuch matching

Established (I could reconstruct or check each):
- the corrected flat principal identity $S_{\rm odd}=\tfrac{\pi^2}{2}R_{\rm odd}$, $D{:}H=-16R_{\rm odd}$, with the four-component support;
- $q$ parallel, TT, descending, with $P$-eigenvalue $-1$ (so $P$ indefinite on TT, matching the known instability of the product);
- principal $S_{\rm odd}=R_{\rm odd}=0$ on $q$ and the four scalar modes, from $D$'s off-diagonal fully-mixed support;
- the relative-comparison algebra, odd–odd diagonal removal, absence of inherited positivity, and the persistence of even–odd/odd–even diagonals;
- the ordering $t^3=o(t^{5/2})$ and why Prop 2.19 does not decide this layer.

Not yet included, and each is decisive for any sign statement:
- **The full geometric source/receiver.** The identity is only the leading flat piece. The curved-parametrix terms, the Bianchi correction, the cutoff, $H_2^4$ (nonzero once the first $\lambda_k\neq0$), the constant-jet/$V_0$ frame terms, and Ozuch's radial normalization are all absent. The equality between this note's $S_{\rm odd}$ and Ozuch's true source $3\int_{S^3/\mathbb Z_2}\langle H^4_\epsilon,V_{l,2}\rangle$ is asserted through the single Step 87 axial match, and Ozuch's formula uses the kernel-element jet $V_{l,2}$, not an arbitrary $V_2$; the general identification is not proven here.
- **Coupling of the $P=-1$ mode through the omitted terms.** Because $G_P^\perp q=-q$, any nonzero coupling of $q$ to the full (curved/Bianchi/frame) source enters the response with a sign-reversing weight. Principal-order annihilation does not decouple $q$ from the full construction; this is the single most important unresolved point for the sign question.
- **The finite inter-node kernel.** $\mathcal I_{ij}$ (the matched, regularized off-diagonal limit) is neither computed nor shown to have a finite $\tau\downarrow0$ limit under a common regularization, slice, and normalization.
- **The surviving even–odd/odd–even diagonal self-terms.** These remain singular and require an actual $A$/$J$/chart symmetry or a local construction to control; nothing here removes them.
- **Higher eigenmodes $\lambda>1$ and the regularized spectral sum**, whose $1/\lambda$ decay competes with growing jet coefficients and eigenspace dimensions.

Net reading: the correction replaces an unsupported positivity assertion with a set of exact, verifiable flat statements, one confirmed indefiniteness ($Pq=-q$), and a well-posed finite target (the matched relative kernel). No further normalization error surfaced beyond the wording point in §3. The path from this flat algebra to any statement about Einstein metrics on $\#_3(S^2\times S^2)$ runs entirely through the curved/Bianchi/Ozuch-normalized matching listed above, with the $q$-mode coupling being the pivotal missing computation.