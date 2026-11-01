# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step87_missed_mode_green_correction.md",
    "Sessions/S0910A01/workspace/scripts/step87_missed_killing_mode_boundary.py",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/scripts/step87_missed_killing_mode_receiver.py",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_receiver.json",
    "Sessions/S0910A01/workspace/notes/step86_kernel_projection_vanishing_and_green_formula.md",
    "Sessions/S0910A01/trace/ttcs/results/step86_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the Step 87 correction to the Step 86 product-orbifold Green-response claim. Read the Step 87 note, scripts/data, and the Step 86 note/TTCS memo. Check whether the missed mode h=(*du_A)⊗(*du_B)+(*du_B)⊗(*du_A) is a legitimate mixed one-form product eigentensor (P eigenvalue 1 in the stated product-sector convention), whether its quadratic jet near NN contains the fully mixed channels h_{03}=-x_1x_2 and h_{12}=-x_0x_3, whether the boundary source projection B_+-B_- is genuinely nonzero in the C_ab convention, and whether the receiver linearized curvature calculation supports a nonzero local radial response. Also identify any normalization/gauge/receiver caveats that prevent promoting this single-mode calculation to the full Ozuch coefficient c_opp-c_same.

## Output

# Verifier Memo — Step 87 correction to the Step 86 product-orbifold response

## Headline

The Step 87 correction is sound. Every checkable positive statement in the note reproduces under independent recomputation, and the Step 86 §8.2 "physical eigenmodes lie in ker(D)" argument is genuinely mistaken in the way Step 87 states. I confirmed the two decisive numbers by hand and from the explicit $C_{ab}$ matrices: the $S^3/\mathbb{Z}_2$ source projection difference is exactly $\pi^2$, and the receiver curvature contrast is exactly $(\delta R^+)_{11}=+1$, $(\delta R^-)_{11}=-1$. What Step 87 establishes is that the same/opposite chirality difference is not annihilated term-by-term; it does not yet produce a single correct inter-node summand, and the note's §4 is accurate about that.

## 1. The mode is a legitimate descended object, and the geometric setup is coherent

The orbifold $(S^2\times S^2)/\mathbb{Z}_2$ with four $A_1$ nodes uses the involution $\sigma\times\sigma$, where $\sigma$ is the $\pi$-rotation about each factor's polar axis. This fixes $\{N,S\}\times\{N,S\}$ (four points), and the tangent action at each fixed point is $-I$ on $\mathbb{R}^4$, giving $\mathbb{R}^4/\mathbb{Z}_2$. The script's `transform_matrix_A = -I` is exactly this generator's differential, so the reported "zero pullback error" under $A$ is the true orbifold invariance at the node. The height function $u_A=\cos\theta_A$ and its Hodge dual $*du_A$ (the axial Killing one-form) are both $\sigma$-invariant, so $*du_A\otimes*du_B$ descends. This is internally consistent and correct. (Note that any degree-2 jet is automatically $-I$-even, so the $A$-invariance check is weak; the $J=\mathrm{diag}(1,-1,1,-1)$ invariance is the informative discrete symmetry.)

Near NN, $u_A=1-\tfrac12|x_A|^2+O(r^4)$ and $*du_A = x_1dx_0-x_0dx_1+O(r^3)$ are the correct local expansions, matching Step 86's convention.

**One item resting only on the Step 85 ledger.** The claim $Ph=h$ (eigenvalue 1, via $\tfrac12(2+2-2)$) is consistent with the ledger but I did not re-derive it from $P=\tfrac12\nabla^*\nabla-\mathring R$. The plausible mechanism: on a product the mixed 2-planes are flat, so $\mathring R$ annihilates the $\alpha\otimes\beta$ AB block, leaving $\tfrac12\nabla^*\nabla$, and each axial one-form on $S^2(1)$ contributes Hodge-Laplacian eigenvalue $\ell(\ell+1)=2$ with a Weitzenböck/Ricci offset $-1$ per factor. The arithmetic $\tfrac12(2+2-2)=1$ is coherent with this. Confirming that $\mathring R$ indeed vanishes on the mixed AB block is the one first-principles step still worth pinning down, because the "low-eigenvalue channel through which chirality propagates" language depends on $\lambda_P=1$ specifically.

## 2. Quadratic jet channels — verified

With $\alpha=(x_1,-x_0,0,0)$, $\beta=(0,0,x_3,-x_2)$ and $h_{ij}=\alpha_i\beta_j+\beta_i\alpha_j$:
$$h_{03}=\alpha_0\beta_3=x_1(-x_2)=-x_1x_2,\qquad h_{12}=\alpha_1\beta_2=(-x_0)(x_3)=-x_0x_3.$$
Both indices of $h_{03}=(0,3)$ span both factors, and its derivative indices $(1,2)$ also span both factors — a fully mixed tensor/derivative quartet. The script's `oneform_linear`/`sym_product_quadratic` reproduce this, and the JSON entries `h_03_x1_x2_coeff=-1`, `h_12_x0_x3_coeff=-1` are correct. This is precisely the channel Step 86's diagonal $D_{ij,ij}$ restriction cannot see.

## 3. Source projection difference — verified analytically as exactly $\pi^2$

I reduced the $S^3/\mathbb{Z}_2$ pairing to the defect contraction without trusting the numerics. Using the quartic moment and the $-\tfrac12$ (multipole), $\tfrac12$ (quotient), $3$ (Ozuch) assembly, and the symmetry of $D_{ab,ij}=\sum_k(C_{2k,ab}C_{2k,ij}-C_{k2,ab}C_{k2,ij})$ under pair swap and within each pair, plus $\mathrm{tr}\,C_{ab}=0$ (which kills the $\delta_{ab}\delta_{pq}$ term), one gets the exact identity
$$B_+-B_- = -\tfrac{3}{4}\cdot\tfrac{1}{12}\,(2)\sum_{ijpq}D_{ijpq}M_{ijpq} = -\tfrac18\,(\text{defect contraction}).$$

I then recomputed the defect contraction from explicit $C$ matrices. Building all six wedge matrices and forming $C[1,k]=\mathrm{sym}(w^+_1 w^-_k)$ and $C[k,1]=\mathrm{sym}(w^+_k w^-_1)$, I found:
- Every $C[1,k]$ and every $C[k,1]$ vanishes at entries $(0,2)$ and $(1,3)$, so $D[0,2,1,3]=0$; the four positive-$M$ terms ($M[0,2,1,3]$, etc.) contribute nothing.
- $D[0,3,1,2]$: the $C[1,k]$ family gives $C[1,0]_{03}C[1,0]_{12}=(-1)(-1)=1$; the $C[k,1]$ family gives $C[0,1]_{03}C[0,1]_{12}=(1)(-1)=-1$; so $D[0,3,1,2]=1-(-1)=2$, matching the JSON. The four negative-$M$ terms each give $2\times(-1)=-2$.

Total defect contraction $=-8$, hence $B_+-B_-=-\tfrac18(-8)=+1$, i.e. exactly $\pi^2$. This confirms `source_projection_difference_plus_minus_over_pi2 = 1/1` rigorously. The difference is genuinely nonzero, so the Step 86 §8.2 conclusion that all physical AB modes lie in $\ker(D)$ is false.

**Where Step 86 erred, precisely.** §8.2 asserted that for AB one-form modes "tensor at $(iA,jB)$ pairs with angular at $(iA,jB)$," forcing $\mathrm{tr}(h_{AB}\cdot D_{:,:,iA,jB})=D_{iA,jB,iA,jB}=0$ by repeated indices. This holds for the *gradient* one-forms $du$ (whose tensor and derivative indices coincide), but not for the *coclosed/axial* one-forms $*du$, whose derivative index is the rotated one. The data show this cleanly: `gradA_gradB`, `gradA_killB`, `killA_gradB` all have defect contraction $0$, and only `killA_killB` has $-8$. The missed sector is exactly the Killing (rotational) half of the AB one-form spectrum.

## 4. Receiver curvature contrast — verified by hand

From $\delta R_{ijkl}=\tfrac12(h_{il,jk}+h_{jk,il}-h_{ik,jl}-h_{jl,ik})$ and the nonzero Hessians ($h_{03,12}=-1$, $h_{12,03}=-1$, $h_{02,13}=1$, $h_{13,02}=1$), I computed the SD block entry in the $\omega_2^\pm$ direction directly:
$$\delta R_{0202}=0,\quad \delta R_{1313}=0,\quad \delta R_{0213}=\tfrac12(h_{03,21}+h_{12,03})=\tfrac12(-1-1)=-1.$$
Then $(\delta R^+)_{11}=\tfrac12(\delta R_{0202}-2\delta R_{0213}+\delta R_{1313})=\tfrac12(2)=+1$, and for the ASD direction $(\delta R^-)_{11}=\tfrac12(\delta R_{0202}+2\delta R_{0213}+\delta R_{1313})=-1$. These match the JSON exactly. The chirality-opposite receiver response is real. The chirality-symmetric behavior of `gradA_gradB` ($\delta R^+=\delta R^-=\mathrm{diag}(0,1,1)$, linearized Ricci $2I$, scalar $8$) is a good consistency contrast: the sign contrast is tied specifically to the axial/rotational character, not to the AB sector generically.

## 5. What is not yet established — the substance separating this from $c_{\rm opp}-c_{\rm same}$

The note's §4 lists these and I concur; the ones that most change the interpretation:

1. **Same-node vs distinct-node evaluation.** Both the source projection and the receiver curvature are computed at the *single* NN node in the *same* frame. The physical coefficient is $L_iG_P^\perp S_j$ with $i\neq j$: the same global $L^2$-normalized eigenmode $\psi_\alpha$ must be evaluated at node $i$ (receiver jet) and at node $j$ (source jet), with the correct relative transport between the two node frames. Step 87 supplies neither the transport nor the receiver's own jet $(V_0,V_1,V_2)^{(i)}$ at a second node. So this refutes a term-by-term vanishing assertion but does not deliver even one correct inter-node summand. This is the same distinction the Step 86 integration memo drew between the kernel-projection $\nu_l$ and the true resolvent response $G_P^\perp$.

2. **$L^2$ normalization.** $B_\pm$ and the $\pm1$ curvature entry are in an unnormalized frame ($V=\alpha\otimes\beta+\beta\otimes\alpha$ with no $1/2$, and no division by $\|\psi_\alpha\|^2$). The single-mode summand $\sim (\text{source})(\text{receiver})/\lambda_P$ cannot be assembled from these raw numbers without the operator-norm normalization.

3. **The chosen EH kernel direction.** The script hard-codes $\zeta^+=\omega_2^+$ (only the $C[1,k]$ row) and $\zeta^-=\omega_2^-$. The $\omega_3^\pm$ direction, or a generic vector in $\ker R^\pm=\mathrm{span}\{\omega_2^\pm,\omega_3^\pm\}$, would give a different number. So $B_+-B_-=\pi^2$ is direction-specific, not canonical; the physical value depends on which EH direction is glued at each node.

4. **Receiver functional identity.** Reading $(\delta R^+)_{11}$ off a local curvature block is not literally Ozuch's receiver pairing $3\int_{\Sigma_i}\langle O_1^4(\zeta_i^+),(\psi_\alpha)_2^{(i)}\rangle$. The receiver should be a link-sphere pairing over $\Sigma_i$ against the mode's *node-$i$* jet, plus the constant-jet/frame correction for modes with $V_0\neq0$ (here $V_0=0$, which is favorable). The identification of the block entry with the true receiver functional is still to be made.

5. **Eigenvalue $-1$ shape mode and kernel modes.** The full resolvent sum runs over the entire kernel-orthogonal complement, including the $g_A-g_B$ mode of eigenvalue $P=-1$ (with its sign) and excluding only the kernel. Step 87's mode is one $\lambda_P=+1$ channel; the sum over all channels and all four nodes could still reinforce or cancel. Overall sign (which chirality yields the larger coefficient) is convention-dependent through the $H^4$ sign and the receiver sign, neither pinned to Ozuch's normalization here.

## 6. Net assessment

Step 87 correctly overturns the Step 86 boxed "$c_{\rm opp}-c_{\rm same}=0$ structural" conclusion: the annihilation argument rested on a false index-matching assumption for the axial one-forms, and the corrected calculation shows a genuine, exactly-computed $\pi^2$ source difference and a $\pm1$ chirality-split receiver response in one live $\lambda_P=1$ channel. The proposed continuation — a full product-eigenspace jet engine with per-node $(V_0,V_1,V_2)$, normalized modes, node-to-node transport, and a regularized sum that includes the $P=-1$ mode — is the right object, and using this axial Killing–Killing mode as its unit test (any implementation returning zero here is repeating the earlier error) is a well-chosen internal check. The quantity that would answer the mixed-chirality question, $c_{\rm opp}-c_{\rm same}$, remains uncomputed, and the note says so accurately.