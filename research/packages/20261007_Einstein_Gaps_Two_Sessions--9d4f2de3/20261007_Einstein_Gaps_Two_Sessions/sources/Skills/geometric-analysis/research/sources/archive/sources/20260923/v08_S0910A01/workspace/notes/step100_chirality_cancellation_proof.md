# Step 100: Structural proof of same-chirality vanishing B_{++} = B_{--} = 0

Session `S0910A01`. Agent2 / Constructor. Phase Execute.

## Main theorem

**Theorem** (AA/BB chirality cancellation identity). In the implemented AA/BB tensor-scalar spectral model on $(S^2\times S^2)/\mathbb Z_2$ with receiver NN, the same-chirality inter-node blocks $B_{++} = B_{--} = 0$ at every fixed degree pair $(\ell_t, \ell_s)$ for every distinct source node (NS, SN, SS) and both tensor sectors (AA, BB).

The proof is a finite-dimensional algebraic identity of the exact bilinear receiver/source maps on the product background. It does not require spectral convergence, tail estimates, or heat-kernel regularization.

**Scope note**: The AB one-form sector vanishing is supported by numerical evidence (Step 98 convergence ladder) but requires a separate algebraic argument. The self-interaction NN←NN is excluded.

## Algebraic setup

The bilinear maps $R_\pm: \mathrm{Sym}^2(\mathbb R^2) \times \mathrm{Sym}^2(\mathbb R^2) \to M_{2\times 2}$ (kernel-plane matrices) are built from the self-dual/anti-self-dual form algebra of the product background. Using the trace-free basis $D=\mathrm{diag}(1,-1)$, $O=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, and $I=\mathrm{diag}(1,1)$:

**Receiver maps** (exact, from Step 99 coefficient algebra):
$$R_+(D,D)=-\tfrac12 D, \quad R_+(O,O)=\tfrac12 D, \quad R_+(D,O)=R_+(O,D)=-\tfrac12 O$$
$$R_+(I,I)=-\tfrac12 I, \quad R_+(T,I)=R_+(I,T)=0 \text{ for } T\in\{D,O\}$$

**Source maps** (exact):
$$S_+(D,D)=-\tfrac14 D, \quad S_+(O,O)=\tfrac14 D, \quad S_+(D,O)=S_+(O,D)=-\tfrac14 O$$
$$S_+(I,I)=0, \quad S_+(T,I)=S_+(I,T)=0 \text{ for } T\in\{D,O\}$$

**Minus-chirality maps** (complete table, verified by explicit computation):
$$R_-(D,D)=-\tfrac12 D,\quad R_-(D,O)=-\tfrac12 O,\quad R_-(O,D)=+\tfrac12 O,\quad R_-(O,O)=-\tfrac12 D$$
$$S_-(D,D)=-\tfrac14 D,\quad S_-(D,O)=-\tfrac14 O,\quad S_-(O,D)=+\tfrac14 O,\quad S_-(O,O)=-\tfrac14 D$$
$$R_-(I,I)=-\tfrac12 I,\quad R_-(T,I)=R_-(I,T)=0,\quad S_-(I,I)=S_-(T,I)=0$$
Entries with tensor argument $O$ have sign changes: $R_-(O,D)=+\tfrac12 O$ vs $R_+(O,D)=-\tfrac12 O$, and $R_-(O,O)=-\tfrac12 D$ vs $R_+(O,O)=+\tfrac12 D$. In the Block products, these sign changes cancel pairwise.

The four tensor polarization types at a node are: $(E,c_2)\to D$, $(E,s_2)\to O$, $(M,c_2)\to O$, $(M,s_2)\to -D$.

## Proof: three independent mechanisms

The orbifold has four $A_1$ nodes labeled by pairs of sphere poles: NN, NS, SN, SS. The receiver is always NN. For each source node and spectral sector (AA or BB), the tensor and scalar factors sit on specific sphere poles.

### Case 1: tensor at different poles (SN, SS for AA; NS, SS for BB)

The tensor receiver at pole N and source at pole S have node signs:
$$T_{\rm src}(E,c_2)=\sigma D,\; T_{\rm src}(E,s_2)=-\sigma O,\; T_{\rm src}(M,c_2)=\sigma O,\; T_{\rm src}(M,s_2)=\sigma D$$
where $\sigma = (-1)^{\ell_t+1}$, while all receiver signs are $+1$.

**Pairing $\{(E,c_2),(M,s_2)\}$**: receiver $D+(-D)=0$, so $R_+(\cdot)\otimes S_+(\cdot)=0$.

**Pairing $\{(E,s_2),(M,c_2)\}$**: source $-\sigma O+\sigma O=0$, so $R_+(\cdot)\otimes S_+(\cdot)=0$.

Result: $B_{++}=0$ for **each scalar mode individually**, before any scalar sum.

### Case 2: tensor at the same pole (NS for AA; SN for BB)

All four tensor types evaluate at the same pole (both N), so $T_{\rm recv}=T_{\rm src}=T_k$ for each $k$. The tensor-type sum for a fixed scalar mode $S$ is:
$$\sum_{k=1}^4 R_+(T_k,S)\otimes S_+(T_k,S) = 2\bigl[R_+(D,S)\otimes S_+(D,S)+R_+(O,S)\otimes S_+(O,S)\bigr]$$

**Identity (a)**: For the $m_0$ scalar mode ($S=I$):
$$R_+(D,I)=S_+(D,I)=R_+(O,I)=S_+(O,I)=0$$
so the $m_0$ contribution vanishes trivially.

**Identity (b)**: For $c_2$ scalar ($S=D$):
$$\mathrm{Block}_D = 2\bigl[(-\tfrac12 D)\otimes(-\tfrac14 D)+(-\tfrac12 O)\otimes(-\tfrac14 O)\bigr]=\tfrac14(D\otimes D+O\otimes O)$$

For $s_2$ scalar ($S=O$):
$$\mathrm{Block}_O = 2\bigl[(-\tfrac12 O)\otimes(-\tfrac14 O)+(\tfrac12 D)\otimes(\tfrac14 D)\bigr]=\tfrac14(O\otimes O+D\otimes D)=\mathrm{Block}_D$$

**The $c_2$ and $s_2$ tensor-sum blocks are identical.** With the $s_2$ node sign at the opposite scalar pole:
$$w_{c_2}\cdot\sigma\cdot\mathrm{Block}_D + w_{s_2}\cdot(-\sigma)\cdot\mathrm{Block}_O = \sigma(\mathrm{Block}_D-\mathrm{Block}_O)=0 \qquad\square$$

## Why cross-chirality $B_{+-}\neq 0$

For $B_{+-}$, the receiver uses $R_+$ and the source uses $S_-$. The minus-chirality source map has:
$$S_-(O,D)=+\tfrac14 O \quad(\text{vs } S_+(O,D)=-\tfrac14 O)$$

This sign flip makes:
$$\mathrm{Block}_D^{+-}=\tfrac14(D\otimes D-O\otimes O), \qquad \mathrm{Block}_O^{+-}=-\tfrac14(D\otimes D-O\otimes O)=-\mathrm{Block}_D^{+-}$$

Now $\mathrm{Block}_D^{+-}=-\mathrm{Block}_O^{+-}$, so the $c_2+s_2$ sum **reinforces** instead of cancelling:
$$\sigma\cdot\mathrm{Block}_D^{+-}+(-\sigma)\cdot\mathrm{Block}_O^{+-}=2\sigma\cdot\mathrm{Block}_D^{+-}\neq 0$$

## Geometric interpretation

The Eguchi–Hanson metric is anti-self-dual (Ozuch §1.2.1, line 307): $R^+(\mathbf{eh})=0$. Its leading asymptotic correction $H^4(\zeta^+)=-\rho(\zeta)^-\circ\zeta^+/(2r^4)$ produces **Ricci-flat anti-self-dual** linearized curvature at the flat metric (line 332):
$$d_{\mathbf e}R^+(H^4(\zeta^+))=0$$

In the product spectral decomposition, this structural fact manifests as the three algebraic identities above. The self-dual receiver $R_+$ cannot detect the anti-self-dual curvature produced by a same-chirality EH source. The cross-chirality source has the opposite anti-self-duality, which breaks the key equality $\mathrm{Block}_D=\mathrm{Block}_O$ into $\mathrm{Block}_D=-\mathrm{Block}_O$ through the sign of the K-odd $(O,D)$ cross term.

## Scope

This theorem applies to the implemented AA/BB tensor-scalar spectral model on the product background. The AB one-form sector vanishing is supported by numerical evidence (Step 98 convergence ladder, machine-precision zeros across all tested node pairs and heat rungs) but requires its own structural argument because the AB representation algebra (one-form × one-form) differs from the tensor × scalar structure.

**Node-sign convention**: The opposite $c_2/s_2$ signs at the south pole follow from the standard antipodal action on real $m=2$ spherical harmonics: $\cos(2\varphi)$ is even and $\sin(2\varphi)$ is odd under the orientation-preserving identification of tangent planes at antipodal poles via parallel transport along a meridian. This is a geometric property of the sphere, not an assumed frame convention. For $\ell_s=0$ or $1$, no $m=2$ scalar Hessian modes exist; the $I$-type contribution vanishes via $R_\pm(T,I)=0$ for traceless $T$.

The Step 99 bridge checks verify that the omitted same-factor partial tensor jets vanish for the actual electric/full-Lie magnetic families, so the result extends to the complete tensor-scalar product eigenmodes in the AA/BB sectors.

The structural proof covers all degrees and all node pairs for AA/BB. It does **not** by itself establish the full Ozuch distributional source identity, complete the self/deformation/complement/projector-motion terms, or control the remainder. The all-same KE consistency and mixed-diagonal positive-definiteness remain consequences of the verified spectral structure rather than proved complete obstruction theorems.

## Verification

- `workspace/scripts/step100_chirality_cancellation_proof.py`: exhaustive exact-rational test of B_{++}=0 for 72 AA/BB sector/pair/degree combinations
- `workspace/data/step100_chirality_cancellation_proof.json`: numerical results
- B_{--} verified by explicit minus-map calculation (this step, inline)
- Bilinear maps extracted from exact form-algebraic coefficients (Step 99 audit)
- Cross-verification with Steps 98/99 floating computations
- TTCS verification: `trace/ttcs/results/step100_ttcs01_verifier1_integration.md`
