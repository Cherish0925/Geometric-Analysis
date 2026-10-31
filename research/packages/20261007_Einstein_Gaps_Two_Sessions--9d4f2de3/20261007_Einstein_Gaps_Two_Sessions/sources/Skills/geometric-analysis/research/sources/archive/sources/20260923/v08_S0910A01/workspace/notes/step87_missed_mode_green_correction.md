# Step 87: missed Killing mode and correction of the Step 86 Green-response vanishing

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## 1. Correction of the Step 86 inference

The Step 86 conclusion that the leading product-orbifold chirality response vanishes mode-by-mode is **not supported**. The structural reason is precise: the script `step86_bilinear_defect_spectral_sum.py` implicitly restricted a product eigentensor's tensor indices to equal its quadratic-jet derivative indices and then tested only diagonal contractions of the defect tensor such as
\[
D_{i_A j_B,i_A j_B}.
\]
The real boundary/source projection depends on the full second jet
\[
(\nabla_m\nabla_n\psi)_{ij},
\]
so terms with four distinct indices can contribute. Product factorization does not impose `tensor indices = derivative indices`.

This matters because Step 86 already found the bilinear chirality defect tensor
\[
D_{ij,mn}=\sum_k\left(C_{2k,ij}C_{2k,mn}-C_{k2,ij}C_{k2,mn}\right)
\]
has rank 4 and nonzero entries exactly in the fully mixed orientation channels. The next calculation should use these entries, not declare them inaccessible.

The corrected status is:

- The boundary pairing for the **kernel projection** `nu_l` from Ozuch Proposition 2.10 is valid, and the product scalar-kernel candidates still have zero pairing with `H^4` by the `C_{11}` orthogonality.
- `nu_l=0` is a Fredholm compatibility statement for the zero-mode projection. It does **not** mean the singular field is globally distributionally `P`-harmonic. The singular multipole retains a distributional source; the field is homogeneous only away from the source. A global distributionally homogeneous solution would be smooth by elliptic regularity.
- Ozuch Proposition 2.10 does not by itself identify every nonzero eigentensor source coefficient or the receiving radial curvature functional. The real node-to-node response remains an object of the form
  \[
  L_iG_P^\perp S_j^\varepsilon,
  \]
  with source, receiver, node transport, normalization, zero/negative mode handling, and regularization still to be derived.

## 2. Exact missed-mode source projection

I implemented the Strategist's missing mode in

- `workspace/scripts/step87_missed_killing_mode_boundary.py`
- output `workspace/data/step87_missed_killing_mode_boundary.json`

On each unit sphere let `u` be the height function and set
\[
\alpha=*du_A,
\qquad
\beta=*du_B,
\qquad
h=\alpha\otimes\beta+\beta\otimes\alpha .
\]
Near the NN node, in the Step 84--86 coordinate convention,
\[
\alpha=x_1dx_0-x_0dx_1+O(r_A^3),
\qquad
\beta=x_3dx_2-x_2dx_3+O(r_B^3).
\]
Thus the homogeneous quadratic tensor jet contains, among its terms,
\[
(h_2)_{03}=-x_1x_2,
\qquad
(h_2)_{12}=-x_0x_3,
\]
which are precisely fully mixed tensor/derivative-index channels. The executable check records
\[
D_{03,12}=2,
\qquad
D_{12,03}=2,
\]
in the same `C_{ab}` convention as Steps 84--86.

Using
\[
H^4_+=-\frac12\sum_k (x^TC_{2k}x)C_{2k},
\qquad
H^4_-=-\frac12\sum_k (x^TC_{k2}x)C_{k2}
\]
on `S^3`, and the exact quartic moment
\[
\int_{S^3}x_ax_bx_px_q\,d\sigma
=\frac{\pi^2}{12}(\delta_{ab}\delta_{pq}+\delta_{ap}\delta_{bq}+\delta_{aq}\delta_{bp}),
\]
with the quotient factor `1/2` for `S^3/Z_2`, the script computes the Ozuch-style boundary source projection
\[
B_\varepsilon(V_2)=3\int_{S^3/Z_2}\langle H^4_\varepsilon,V_2\rangle\,d\sigma.
\]
For the missed Killing--Killing mode:
\[
B_+(V_2)=\frac{\pi^2}{2},
\qquad
B_-(V_2)=-\frac{\pi^2}{2},
\qquad
B_+(V_2)-B_-(V_2)=\pi^2 .
\]
The same output records `D_contraction_sum_Dijpq_Mijpq = -8`; the sign relation with `B_+-B_-` depends on the common normalization and the convention that `V=alpha⊗beta+beta⊗alpha` is not divided by two.

The four axial linear-linear AB modes checked at NN were:

| mode | `B_+ / pi^2` | `B_- / pi^2` | difference |
|---|---:|---:|---:|
| `gradA_gradB` | `-1/2` | `-1/2` | `0` |
| `gradA_killB` | `0` | `0` | `0` |
| `killA_gradB` | `0` | `0` | `0` |
| `killA_killB` | `1/2` | `-1/2` | `1` |

The missed mode is invariant under simultaneous antipodal `A` and simultaneous conjugation `J`: the script reports zero pullback error for both symmetries. It also descends through the quotient because it is a product of two odd one-form factors.

## 3. Receiver-side local curvature for the missed mode

I also implemented the receiver linearized curvature calculation in

- `workspace/scripts/step87_missed_killing_mode_receiver.py`
- output `workspace/data/step87_missed_killing_mode_receiver.json`

For a quadratic tensor jet `h_ij=M_ijpq x_p x_q` with `h(0)=dh(0)=0`, the script uses the flat first-variation formula
\[
\delta R_{ijkl}
=\frac12(h_{il,jk}+h_{jk,il}-h_{ik,jl}-h_{jl,ik})
\]
and projects to the self-dual/anti-self-dual blocks using the same bases as the `C_{ab}` calculation.

For the missed Killing--Killing mode the local curvature blocks are
\[
\delta R^+=\operatorname{diag}(-2,1,1),
\qquad
\delta R^-=\operatorname{diag}(2,-1,-1),
\]
up to the script's Riemann sign convention. In particular, for receiver insertion direction `zeta=omega_2` (0-based index `1`),
\[
(\delta R^+)_{22}=1,
\qquad
(\delta R^-)_{22}=-1.
\]
Therefore a plus-chirality receiver has a nonzero local radial curvature response to this eigentensor. Combining this local receiver with the source projection and the mixed one-form sector eigenvalue
\[
\lambda_P=\frac12(2+2-2)=1
\]
gives a nonzero single-mode contribution in this unnormalized, same-frame, same-node test. This is enough to falsify the Step 86 mode-by-mode annihilation argument.

The same receiver script also reports:

- `gradA_gradB`: `delta R^+ = delta R^- = diag(0,1,1)` and radial response `+1`, chirality-independent;
- `gradA_killB` and `killA_gradB`: zero local curvature in this axial model;
- `killA_killB`: chirality-opposite curvature blocks as above.

## 4. What this does and does not establish

This step establishes an exact, reproducible local source-and-receiver calculation for one genuine product eigentensor channel that Step 86 missed. It changes the positive mixed-row route in a specific way:

- The algebraic orientation defect is not inert. It is seen by physical product eigentensors.
- The leading Green interaction cannot be declared equal for same and opposite chiralities from product factorization alone.
- There are concrete low eigenvalue channels (`P h=h`) through which chirality can propagate.

It does **not** compute the geometric coefficient `c_opp-c_same`. Missing ingredients remain:

1. `L^2` normalization of the global product eigenmodes in Ozuch's operator convention.
2. Consistent node-to-node transport for the four orbifold nodes, including orientation and chirality conventions under `A`, `J`, `L`, and the selected gluing frames.
3. The full receiver functional, including constant-jet/frame correction terms for eigentensors with nonzero `V_0`.
4. The complete product eigenspaces beyond the axial `l_1=l_2=1` one-form modes; even factor-parallel modes can carry B-factor derivative indices through scalar factors.
5. Regularized spectral summation and treatment of zero and negative modes.
6. Identification with the radial obstruction variables in the matched Ozuch/Biquard chart.

## 5. Immediate continuation

The best continuation is a complete product-eigenspace boundary-jet engine: represent each product eigentensor by its full local Taylor data `(V_0,V_1,V_2)` at each of the four nodes, compute `B_\varepsilon(V_2)` for the source, compute the receiver curvature functional including constant-frame corrections, and only then perform a regularized spectral sum over each eigenspace. The missed axial Killing--Killing mode is the first test case and should remain the unit test for the engine: any implementation that gives zero for this mode is repeating the Step 86 error.

## 6. TTCS verification and the first eigenspace extension

TTCS verification saved at `trace/ttcs/results/step87_ttcs01_verifier1_integration.md` independently confirmed the essential correction:

- `h=(*du_A)⊙(*du_B)` is a legitimate mixed one-form product eigentensor with `P h=h` in the Step 85--87 convention. On each unit `S^2`, a Killing one-form satisfies `∇*∇ α=α`; the product rough Laplacian gives `∇*∇h=2h`, and the product curvature has no mixed `AB` action, so `P=1`.
- The mode is trace-free, divergence-free, and not a pure diffeomorphism artifact.
- Its NN quadratic jet contains the fully mixed terms `M_{03,12}=M_{12,03}=-1` and pairs with `D_{03,12}=D_{12,03}=2`.
- The exact source difference is `B_+-B_-=pi^2`; the local receiver response for `zeta=omega_2` is nonzero, with blocks `δR^+=diag(-2,1,1)` and `δR^-=diag(2,-1,-1)` in the script convention.
- The current calculation is local, unnormalized relative to the full Ozuch variables, and same-frame. It does not decide the full node-to-node coefficient.

The TTCS note also corrected a wording issue: the quotient generator near a node is a simultaneous `π` rotation on both sphere factors, not the ordinary antipodal map on each `S^2`; the local linear action is `-I` on the four-dimensional tangent space. The phrase that the one-form factors are “odd” should be read as a local coefficient parity shorthand; as one-forms under the local rotation, the full pullback behavior must include the sign of `dx`.

I then extended the first source-side calculation in two scripts:

- `workspace/scripts/step87_l1_coexact_source_jets.py`, output `workspace/data/step87_l1_coexact_source_jets.json`, computes the source projection for all coexact `l=1` one-form products `(*dX_a)_A ⊙ (*dX_b)_B` at NN.
- `workspace/scripts/step87_l1_oneform_source_matrix.py`, output `workspace/data/step87_l1_oneform_source_matrix.json`, computes all exact and coexact `l=1` one-form product source projections before gauge reduction.

The complete NN source matrix before gauge reduction shows that among quotient-descending `l=1` mixed one-form products, the only nonzero source projections in this axial node frame are
\[
dZ_A\odot dZ_B:
B_+=B_-=-\frac{\pi^2}{2},
\qquad
(*dZ_A)\odot(*dZ_B):
B_+=\frac{\pi^2}{2},\quad B_-=-\frac{\pi^2}{2}.
\]
The exact `dZ_A⊙dZ_B` mode is not TT and has no chirality difference. The coexact axial mode is TT and is the clean low-eigenvalue chirality-sensitive test case. Other `X/Y` coexact modes are quotient-descending but have nonzero constant jet at NN and zero source difference in the source-only projection; they still require receiver constant-frame/background-curvature handling before a final eigenspace sum.

A provisional one-dimensional node-transport ledger, `workspace/data/step87_axial_killing_lambda1_partial.json`, uses the axial mode alone, its quotient `L^2` norm `64π^2/9`, eigenvalue `1`, and orientation-preserving local frames with `*dZ` sign `+` at `N` and `-` at `S`. It gives a rank-one partial matrix with magnitude `9/64`: same node-sign pairs (`NN/SS` with `NN/SS`, or `NS/SN` with `NS/SN`) have `+9/64` for the source `+ minus -` difference, while cross node-sign pairs have `-9/64`. This is not an Ozuch coefficient; it is a controlled low-mode contribution and a unit test for the complete product-eigenspace engine.
