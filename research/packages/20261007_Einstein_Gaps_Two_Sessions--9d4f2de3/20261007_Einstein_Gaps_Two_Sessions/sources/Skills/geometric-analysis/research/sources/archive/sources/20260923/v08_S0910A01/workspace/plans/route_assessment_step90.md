# Route assessment: Step 90

## Step 91 correction notice

Use `workspace/plans/route_assessment_step91.md` and `workspace/notes/step91_receiver_and_adjacent_green.md` for the current status.  The Step-90 K-reflection theorem remains useful for the K-equivariant linear pairwise background problem, but language about full-construction/all-order completion was too strong.  The Step-90 spectral script also had a flawed mode enumeration; Step 91 corrected quotient descent to azimuthal m-parity, moved the factor trace-free minimum from P=4 to P=2, kept independent degrees, and retained only the lower-bound conclusion P>=1.
## Advance this step

The K-symmetry $K(z,w)=(\bar z,w)$ gives three structural results for the product orbifold:

1. **Cross-parity elimination.**  All even–odd and odd–even interactions vanish for every node pair (including diagonal) by K-parity of the background operator.  This removes the problematic mixed-sector self-singularities that Step 89 identified as needing "separate symmetry or matched subtraction."

2. **Geometric mode annihilation.**  The negative shape mode $q=g_A-g_B$ and all four scalar zero modes are K-even, hence geometrically orthogonal to the K-odd chirality source at the full construction level.  This upgrades the Step 89 flat $V_2$ principal calculation to a complete statement about the operator.

3. **K-odd spectral positivity.**  $P|_{\text{K-odd quotient TT}}\ge1$, achieved by the axial mode.  No negative or zero modes exist in this sector.  The Green pseudo-inverse is well-defined and positive in the bilinear-form sense.

Combined with A (scalar mode elimination), J (transverse projection elimination), and L (orbit exchange), the full symmetry group $\{I,\sigma,A,J,K,L,KJ,LK,\ldots\}$ reduces the relative mixed-minus-all-same interaction to:
$$
\Delta_\varepsilon(\tau)=\sum_{i\ne j}t_it_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11}(\tau),
$$
a finite sum over smooth off-diagonal Green kernel values.

## What is NOT resolved

- The **sign** of the off-diagonal odd–odd Green kernel $K_{ij}^{11}$ at distinct nodes is not determined by spectral positivity.  An off-diagonal matrix with zero diagonal is not positive-semidefinite.
- The **numerical value** of $K_{ij}^{11}$ requires either explicit spectral decomposition/summation or a direct PDE solve on the orbifold.
- The inter-node interaction at $O(t^3)$ is below Ozuch Proposition 2.19's $O(t^{5/2})$ resolution; a matched projected expansion at this order is still needed.
- **Full K-equivariance of the Ozuch/Biquard construction** (chart, Bianchi normalization, gauge) is natural for standard choices but needs explicit verification.
- **Nonlinear higher-order terms** may have different chirality structure.
- This is a positive-branch local desingularization calculation, not a Yau–26 solution.

## Current route status

### Positive mixed-row desingularization
After Step 90, the calculation is in its cleanest form:
- All unwanted spectral sectors eliminated by symmetry
- All self-singularities removed
- The surviving object is a finite, well-defined, smooth Green function evaluation
- Next concrete step: compute $K_{ij}^{11}$ via spectral decomposition or heat kernel

### Restricted IL negative branch
Still the strongest scope-relevant Yau–26 asset.  Separate from the product-orbifold work.

### Graph and higher-dimensional routes
A03's graph work continues independently.  No current branch covers all dimensions.
