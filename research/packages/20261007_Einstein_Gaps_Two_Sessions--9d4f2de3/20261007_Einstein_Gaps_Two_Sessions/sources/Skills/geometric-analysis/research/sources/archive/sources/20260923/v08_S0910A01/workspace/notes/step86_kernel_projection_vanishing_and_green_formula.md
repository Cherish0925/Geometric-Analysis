# Correction notice from Step 87

Step 87 found that the Step 86 conclusion in Sections 8.2--8.4 is false. Product eigentensors do not force tensor indices to equal their quadratic-jet derivative indices. The legitimate mixed one-form product mode `(*du_A)⊙(*du_B)` has `P`-eigenvalue 1, is invariant under the relevant `A` and `J` symmetries, and its quadratic jet contains fully mixed channels such as `(h_2)_{03}=-x_1x_2` and `(h_2)_{12}=-x_0x_3`. Direct exact boundary integration gives `B_+-B_- = pi^2`, and the flat receiver curvature calculation gives a nonzero radial response. Thus the only retained Step 86 result is the zero-mode/kernel-projection pairing `nu_l=0` for the scalar kernel candidates; the claimed leading-order equality `c_opp=c_same` and the assertion that all product modes lie in `ker(D)` are superseded. Use `workspace/notes/step87_missed_mode_green_correction.md` and `workspace/data/step87_missed_killing_mode_boundary.json` / `step87_missed_killing_mode_receiver.json` for the corrected status.

# Step 86: Kernel projection vanishing and exact Green spectral formula

Session `S0910A01`. Agent2 / Constructor. Phase Execute.

## 1. Theorem: ν_l = 0 for all kernel modes and both chiralities

**Setup.** The product orbifold $(S^2 \times S^2)/\mathbb{Z}_2$ with four $A_1$ nodes.
Einstein metric $g_o = g_A + g_B$ with $\operatorname{Ric}(g_o) = g_o$, $\Lambda = 1$.
Curvature: $R^+ = R^- = \operatorname{diag}(1,0,0)$.

**Ozuch's Proposition 2.10** (arXiv:2105.13193, line 616): When all first
obstructions vanish ($\lambda_k^j = 0$ for all $k,j$), the orbifold obstruction
coefficients are:
$$
\nu_l = 3\int_{\mathbb{S}^3/\mathbb{Z}_2}
\langle H^4, V_{l,2}\rangle_{\mathbf{e}}\,d\sigma,
$$
where $v_l \in \mathbf{O}(g_o) = \ker_{L^2}P_{g_o}$ has local expansion
$v_l = V_{l,0} + V_{l,2} + O(r^4)$ at the node, and $H^4(\zeta^\pm)$ is the
ALE bubble's $r^{-4}$ multipole.

**Kernel modes.** The full $L^2$-kernel of $P = \frac12\nabla^*\nabla - \mathring{R}$
on all symmetric 2-tensors of $(S^2(1)\times S^2(1))/\mathbb{Z}_2$ contains the
four modes $u_i g_j$ where $u_A, u_B$ are the first-harmonic height functions
on each factor:
$$
P(u_A g_A) = P(u_A g_B) = P(u_B g_A) = P(u_B g_B) = 0.
$$
(Eigenvalue: $\nabla^*\nabla(u_i g_j) = 2u_i g_j$, $\mathring{R}(u_i g_j) = u_i g_j$,
so $P = 1 - 1 = 0$.)

These are the ONLY zero modes (up to the gauge/Bianchi quotient).

**V_{l,2} structure at a node.** Near the NN node in geodesic coordinates
$(x_A, x_B) \in \mathbb{R}^2 \times \mathbb{R}^2$:
$$
u_A = 1 - \tfrac12|x_A|^2 + O(r^4),\quad
g_A = E_A - \tfrac12|x_A|^2 E_A + O(r^4),
$$
and similarly for $u_B, g_B$. The $r^2$-homogeneous Taylor parts are:
$$
V_2(u_A g_A) \propto |x_A|^2 E_A,\quad
V_2(u_A g_B) \propto |x_A|^2 E_B,
$$
$$
V_2(u_B g_A) \propto |x_B|^2 E_A,\quad
V_2(u_B g_B) \propto |x_B|^2 E_B.
$$

**Trace-free projection.** Since $H^4$ is trace-free, only the trace-free parts
of $V_{l,2}$ contribute to $\langle H^4, V_{l,2}\rangle$. The trace-free part of
$E_A$ or $E_B$ at the node is proportional to $C_{11} = \omega_1^+ \circ \omega_1^-$:
$$
E_A - E_B = -C_{11},\quad \operatorname{tr}(E_A) = \operatorname{tr}(E_B) = 2.
$$

**Orthogonality argument.** For $\zeta^+ \in \ker R^+ = \operatorname{span}\{\omega_2^+,\omega_3^+\}$:
$$
H^4(\zeta^+) = -\tfrac12 \sum_j p_j C_{2j}/r^4,\quad
p_j = x^T C_{2j} x/|x|^2.
$$
For $\zeta^- \in \ker R^-$:
$$
H^4(\zeta^-) = -\tfrac12 \sum_j q_j C_{j2}/r^4,\quad
q_j = x^T C_{j2} x/|x|^2.
$$
Both families involve $C_{2j}$ or $C_{j2}$ matrices. By the exact identity
$$
\operatorname{tr}(C_{ab}C_{cd}) = 4\delta_{ac}\delta_{bd},
$$
we have $\operatorname{tr}(C_{11}C_{2k}) = 4\delta_{12}\delta_{1k} = 0$ for all $k$,
and $\operatorname{tr}(C_{11}C_{k2}) = 4\delta_{1k}\delta_{12} = 0$ for all $k$.

**Conclusion.**
$$
\boxed{\nu_l^{(j,\pm)} = 3\int_{\mathbb{S}^3/\mathbb{Z}_2}
\langle H^4(\zeta^\pm), V_{l,2}\rangle_{\mathbf{e}}\,d\sigma = 0}
$$
for all four kernel modes $v_l$, both chiralities $\pm$, and every node $j$.
This is structural: it follows from the product curvature having rank-1 SD/ASD
structure with kernel in the off-diagonal $C_{ab}$ channels, while the Einstein
deformation modes live in the diagonal $C_{11}$ channel.

## 2. Consequence: the inter-node coefficient is a pure Green function

Since $\nu_l = 0$ for all $l$, the Ozuch orbifold-side tensor satisfies
$$
P_{g_o}\bar h_j^4 = 0 \quad\text{(distributionally)}
$$
with singular data $\bar h_j^4 \sim H^4(\zeta_j^{\epsilon_j})$ at node $j$.
There is NO kernel forcing term.

The spectral expansion (excluding only the zero modes) is:
$$
\bar h_j^4(x) = \sum_{\alpha:\lambda_\alpha\neq 0}
\frac{\psi_\alpha(x)}{\lambda_\alpha}\,\langle S_j,\psi_\alpha\rangle,
$$
where $\{(\psi_\alpha,\lambda_\alpha)\}$ are the non-kernel eigenmodes of $P$ on
the compact orbifold, and the **distributional source coefficient** is given
by the same Ozuch boundary pairing:
$$
\langle S_j,\psi_\alpha\rangle
= 3\int_{\mathbb{S}^3/\mathbb{Z}_2}
\langle H_j^4, (\psi_\alpha)_2^{(j)}\rangle_{\mathbf{e}}\,d\sigma,
$$
where $(\psi_\alpha)_2^{(j)}$ is the $r^2$-homogeneous part of $\psi_\alpha$ at node $j$.

The **receiver at node $i$** with obstruction mode $O_1^4(\zeta_i^{\epsilon_i})$
extracts the curvature content via the same boundary functional:
$$
\langle R_i,\psi_\alpha\rangle
= 3\int_{\mathbb{S}^3/\mathbb{Z}_2}
\langle O_1^4(\zeta_i^{\epsilon_i}), (\psi_\alpha)_2^{(i)}\rangle_{\mathbf{e}}\,d\sigma.
$$

The **exact inter-node obstruction coefficient** is then the double-boundary spectral sum:
$$
\boxed{
c_{ij}^{\epsilon_i,\epsilon_j}
= \sum_{\alpha:\lambda_\alpha\neq 0}
\frac{\langle R_i,\psi_\alpha\rangle\,\langle S_j,\psi_\alpha\rangle}{\lambda_\alpha}.
}
$$

## 3. Properties of the spectral formula

**Self-adjointness / reciprocity.** Since $P$ is self-adjoint, the Green function
satisfies $G_P(x,y) = G_P(y,x)^T$. At the coefficient level:
$$
c_{ij}^{\epsilon_i,\epsilon_j} = c_{ji}^{\epsilon_j,\epsilon_i}.
$$

**Frame invariance.** The boundary pairing is intrinsic (it depends only on the
eigenmode and the singular data, not on a coordinate choice at the node).
Therefore the spectral sum is frame-independent. This explains the frame
sensitivity of the earlier proxy computations: they were not using the correct
gauge-invariant source/receiver functionals.

**Negative modes.** The sum includes the negative eigenvalues $\lambda = -1$
(corresponding to the constant trace/shape modes with $P = -1$). These
contribute with a negative sign and must NOT be omitted.

**Convergence.** For distinct nodes $i \neq j$, the bar_h_j^4 field is smooth at $i$.
The spectral sum therefore converges: the $r^{-4} \times r^{+2}$ decay of each
source/receiver boundary pair gives numerator $\sim \lambda_\alpha^{-1}$,
and the eigenvalues grow like $\lambda_\alpha \sim \ell^2$ for large $\ell$, giving
overall $\sim \ell^{-3}$ convergence.

## 4. Chirality difference in the spectral formula

The receiver at node $i$ has fixed $+$ chirality. The chirality enters through
the source:
$$
c_{ij}^{+,+} - c_{ij}^{+,-}
= \sum_{\alpha:\lambda_\alpha\neq 0}
\frac{\langle R_i^+,\psi_\alpha\rangle}{\lambda_\alpha}
\bigl[\langle S_j^+,\psi_\alpha\rangle - \langle S_j^-,\psi_\alpha\rangle\bigr].
$$

The **chirality source difference** is:
$$
\langle S_j^+,\psi_\alpha\rangle - \langle S_j^-,\psi_\alpha\rangle
= 3\int_{\Sigma_j}
\langle H^4(\zeta^+) - H^4(\zeta^-), (\psi_\alpha)_2^{(j)}\rangle\,d\sigma.
$$

From Step 84: $H^4(\zeta^+) - H^4(\zeta^-)$ is nonzero in the $C_{21}$ and $C_{23}$
channels (the non-axial ones), with pointwise difference $4(1-p_2^2)$ and
$S^3$-mean $8/3$ in the identity pairing. The spectral propagation through
$1/\lambda_\alpha$ may modify or preserve this difference.

## 5. Product harmonic implementation

For $(S^2(1) \times S^2(1))/\mathbb{Z}_2$, the eigenmodes of $P$ decompose into
sectors from the Step 85 ledger:
- **AA/BB trace:** $P = \frac12(\ell_1(\ell_1+1)+\ell_2(\ell_2+1)) - 1$
- **AA/BB scalar TF-Hessian:** $P = \frac12(\ell_1(\ell_1+1)+\ell_2(\ell_2+1)) - 1$
  (same formula, different source/receiver projections)
- **AB one-form product:** $P = \frac12(\ell_1(\ell_1+1)+\ell_2(\ell_2+1)-2)$

The source/receiver boundary pairings at the nodes involve the second-jet
evaluations of the product harmonics, which are determined by:
- Scalar harmonic values at the poles: $Y_{\ell,0}(N) = \sqrt{(2\ell+1)/(4\pi)}$,
  $Y_{\ell,0}(S) = (-1)^\ell Y_{\ell,0}(N)$
- Second derivatives at poles involve $|m| \leq 2$ channels
- The C_{ab} projection depends on the sector type

## 6. What ν_l = 0 means for existence

The vanishing of ALL ν_l removes one of the two potential obstructions to
desingularization: the kernel-mediated coupling between nodes. The remaining
inter-node coupling comes entirely through the non-kernel Green function.

This is structurally favorable for existence: the inter-node effect is a
perturbation mediated by the spectral inverse, not a finite-dimensional
obstruction. However, whether it forces or prevents existence at the
non-Kähler mixed-chirality row depends on the sign and magnitude of the
spectral sum.

## 7. Files

- Analysis: this note
- TTCS verification: `trace/ttcs/results/step86_ttcs01_verifier1_integration.md`
- Prior angular data: `data/step84_chirality_corrected.json`
- Sector ledger: `data/step85_product_operator_sector_ledger.json`


## 8. Corrected analysis: bilinear defect and physical-mode vanishing

### 8.1 The bilinear identity fails

The SQUARED identity $\sum_k C_{ak,ij}^2 = \sum_k C_{ka,ij}^2$ holds for all
$(a,i,j)$, but the BILINEAR identity fails:
$$
D_{ij,mn} := \sum_k [C_{1k,ij}C_{1k,mn} - C_{k1,ij}C_{k1,mn}] \neq 0.
$$
The defect tensor $D$ has rank 4 (as a 16×16 matrix), eigenvalues $\pm 4$ (each
with multiplicity 2), and nonzero entries only at "fully mixed" index quartets
like $(0,1,2,3)$, $(0,3,1,2)$, etc. This structure reflects the orientation
tensor $\varepsilon_{abcd}$ through the SD/ASD completeness difference.

### 8.2 Physical eigenmodes lie in ker(D)

The spectral sum for the chirality difference is:
$$
c_{\rm opp} - c_{\rm same}
= \sum_\alpha \frac{R_\alpha \cdot K \cdot \operatorname{tr}(T_\alpha \cdot D_{:,:,m_\alpha n_\alpha})}{\lambda_\alpha},
$$
where $(m_\alpha, n_\alpha)$ are the angular indices of eigenmode $\alpha$ at the
source node, and $T_\alpha$ is its tensor.

**Key structural fact:** For every product eigenmode on $S^2 \times S^2$, the
tensor indices and angular indices are *matched* by the product structure:
- AB one-form modes: tensor $h_{AB,iA,jB}$ pairs with angular $x_{iA} x_{jB}$
- AA TF-Hessian modes: tensor has indices in $\{0,1\}^2$, angular is also in $\{0,1\}^2$
- BB TF-Hessian modes: tensor and angular both in $\{2,3\}^2$
- Trace modes: already proved zero by $C_{11}$ orthogonality

For the AB sector with tensor at $(iA, jB)$ and angular at $(iA, jB)$:
$$
\operatorname{tr}(h_{AB} \cdot D_{:,:,iA,jB})
= D_{iA,jB,iA,jB} + D_{jB,iA,iA,jB}.
$$
Since $D$ has nonzero entries only at fully mixed quartets (all four indices
different), and $(iA,jB,iA,jB)$ has repeated indices, $D_{iA,jB,iA,jB} = 0$.
Similarly $D_{jB,iA,iA,jB} = 0$ because two indices match. **Zero.**

For AA/BB sectors: all indices are within one factor ($\{0,1\}$ or $\{2,3\}$),
so $D$ has no contribution (its nonzero entries span all four directions). **Zero.**

### 8.3 Complete vanishing theorem

$$
\boxed{
c_{\rm opp} - c_{\rm same} = 0
\quad\text{at leading Ozuch order for all node pairs.}
}
$$

This vanishing is structural, not a cancellation miracle. It arises from three
independent mechanisms:
1. The kernel modes have zero boundary pairing ($\nu_l = 0$)
2. The bilinear defect $D$ has rank-4 image in the "fully mixed" orientation sector
3. Product eigenmodes have matched tensor/angular indices → they lie in $\ker(D)$

### 8.4 Implications

At leading Ozuch order (Proposition 2.10 boundary pairing through the product
Lichnerowicz resolvent):
- **Same-chirality and mixed-chirality inter-node coefficients are EQUAL**
- The all-same-chirality smoothing to $\operatorname{Bl}_5\mathbb{P}^2$ (known KE)
  constrains the radial functional
- If matching proves $F_{\rm same}(t) = 0$, then $F_{\rm mixed}(t) = 0$ also at
  this order

Any chirality difference must arise at **higher order**:
- Nonlinear terms $Q^{(3)}$ in the Ozuch expansion
- The $H_4^4$ logarithmic correction term (Remark 2.11)
- Coupling between the $v$-parameter and the $\zeta$-parameters
- Or the orbifold-deformation response $\overline{\mathbf{o}}_{j,k}^4$

### 8.5 Verification data

- Sector coupling analysis: `data/step86_sector_coupling_analysis.json`
- Spectral chirality computation: `data/step86_spectral_chirality_computation.json`
- Bilinear defect analysis: `data/step86_bilinear_defect_spectral_sum.json`
- Chirality parity identity: `data/step86_chirality_parity_identity.json`
- TTCS verification of $\nu_l = 0$: `trace/ttcs/results/step86_ttcs01_verifier1_integration.md`
