# Step 100: relative Chern–Gauss–Bonnet budget for an explicit graph gluing

Session `S0910A03`, Agent1 / Explore.

## 1. Why the Step 99 route change is invalid

For the normalized negative branch in dimension four, disproving the universal implication requires a sequence

\[
\|g_j^{-1}(\operatorname{Ric}_{g_j}+3g_j)\|_{L^\infty}\longrightarrow0
\]

on closed manifolds carrying no Einstein metric (the manifolds may vary with `j`). A single example with defect near `1.098` cannot do this: the existential interval in Yau 26 may be much narrower and need not meet that topology at all.

The number

\[
\frac{3(\sqrt3-1)}2\approx1.098
\]

is the old Step 2/64 Chern–Gauss–Bonnet lower bound for a **closed** four-manifold with `chi <= 0`, specialized to `Ric ≈ -3g`. It is not a new graph-connector phenomenon. A connector `T^3 x I` has boundary. Local free-`T^2` symmetry does not extend to a global free action on a completed graph manifold and does not force its Euler characteristic to vanish. Pure finite-volume real-hyperbolic pieces instead have

\[
\operatorname{Vol}_{-1}(P)=\frac{4\pi^2}{3}\chi(P)>0,
\]

and gluing their truncations along flat three-manifolds preserves the sum of Euler characteristics because every gluing hypersurface has Euler characteristic zero.

Step 99's proposed connector inequality therefore deleted the hyperbolic topological term. The associated assertion of sharpness was also unjustified: making `|W|` formally zero does not show that the separate extremal estimates for scalar curvature and trace-free Ricci are simultaneously realized by a metric.

The incorrect target and connector conclusion have been withdrawn in:

- `workspace/notes/step99_raychaudhuri_cgb_and_cost_structure.md`;
- `workspace/plans/step99_route_map.md`.

The Raychaudhuri finite-length floor and the complete Ricci-block cost decomposition remain useful.

## 2. Exact relative identity

Let `M` be a closed oriented four-manifold obtained by gluing truncations of finite-volume real-hyperbolic four-pieces. Let `N subset M` be the union of replacement regions. Assume first that the complement `M \ N` is exactly sectional-curvature `-1`. Let `C_removed` be the union of complete hyperbolic cusp tails replaced by `N`, and write

\[
V_N=\operatorname{Vol}_g(N),\qquad
V_{\rm rem}=\operatorname{Vol}_{-1}(C_{\rm removed}),\qquad
E=\operatorname{Ric}_g+3g,
\]

with `e=tr_g E` and `E^o=E-(e/4)g`.

Chern–Gauss–Bonnet gives

\[
8\pi^2\chi(M)
 =\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|E^\circ|^2}{2}\right)d\mu,
\qquad s=-12+e.
\]

For the disjoint union of complete hyperbolic pieces, `W=0`, `E=0`, and

\[
8\pi^2\chi(M)=6(P_{\rm kept}+V_{\rm rem}),
\]

where `P_kept` is the hyperbolic volume retained outside `N`. On `M\N`, the actual metric contributes exactly `6P_kept`. Subtracting these terms and expanding

\[
\frac{(-12+e)^2}{24}=6-e+\frac{e^2}{24}
\]

yields the exact relative balance

\[
\boxed{
2\int_N|W|^2+12(V_N-V_{\rm rem})
=\int_N\left(|E^\circ|^2+2e-\frac{e^2}{12}\right)d\mu .
}
\tag{RCGB}
\]

This formula contains the term that Step 99 omitted. It compares the replacement to the particular cusp volume it displaces; it does not impose the closed-`chi=0` formula on `N`.

If the exterior is only approximate, its difference from the corresponding complete hyperbolic piece must remain in the equation. Writing

\[
\Phi(g)=|W_g|^2+\frac{s_g^2}{24}-\frac{|
\operatorname{Ric}_g^\circ|^2}{2},
\]

the right correction is the signed exterior contribution

\[
-2\int_{M\setminus N}(\Phi(g)-6)\,d\mu_g
\]

together with any volume-domain mismatch needed to compare the actual exterior with the reference hyperbolic region. Thus `e^{2t}q_t` is an exact hyperbolic exterior only when `q_t` is flat; for nonflat `q_t`, its explicit residual and curvature contribution cannot be discarded.

## 3. Coarse consequence and what it can—or cannot—show

If `||E||_op <= delta`, then in dimension four

\[
|e|\le4\delta,
\qquad |E^\circ|^2\le4\delta^2.
\]

Therefore

\[
\left|
2\int_N|W|^2+12(V_N-V_{\rm rem})
\right|
\le (8\delta+4\delta^2)V_N.
\tag{B}
\]

The sharper eigenvalue optimization of the polynomial integrand could improve constants, but it cannot change the essential requirement. If `delta_j -> 0`, then

\[
\frac{2\int_{N_j}|W|^2}{V_{N_j}}
+12\left(1-rac{V_{{\rm rem},j}}{V_{N_j}}
ight)
\longrightarrow0.
\tag{NB}
\]

A global obstruction would require showing that the left side stays separated from zero for every faithful connector in the intended family. Positivity of the Weyl term alone is insufficient, because `V_N` may be smaller than `V_rem` and cancel it. Conversely, satisfying `(NB)` is only necessary; it does not solve the horizontal, shape, Maxwell, or matching equations.

A particularly transparent rearrangement is

\[
V_{\rm rem}-V_N
=\frac16\int_N|W|^2+O(\delta V_N).
\tag{V}
\]

Thus a near-Einstein replacement must remove *more* hyperbolic cusp volume than it inserts unless its Weyl energy is negligible; the volume deficit pays exactly one sixth of the connector Weyl energy to leading order. This is the correct geometric budget.

## 4. Explicit hyperbolic-piece laboratory

Use one of Ratcliffe–Tschantz's orientable double covers `24cdc1.*` of a one-cusped hyperbolic 24-cell manifold. The directly read source records:

- the nonorientable base has `chi=1`, hyperbolic volume `4 pi^2/3`, and maximum-cusp volume `8`;
- its orientable double cover has one cusp with link `T^3`, hence `chi=2`, total hyperbolic volume `8 pi^2/3`, and maximum-cusp volume `16`;
- for `24cdc1.1`, `H_1 = Z + Z_3 + Z_13` and `H_3=0`, so `b1=1>b3=0`.

The last fact closes the old Step 70 peripheral-rank question for this explicit piece: the image of `H_1(T^3;Q) -> H_1(\bar P;Q)` has positive rank. Hence there exists a primitive character nonzero on the cusp group. For every degree `N` coprime to its peripheral multiplicity, the corresponding cyclic cover has one cusp with a peripheral sublattice of type `(N,1,1)`.

This gives an explicitly specified sequence of pure hyperbolic pieces for the matching laboratory. It does **not** yet verify which affine self-gluing yields the precise extended graph topology intended for the charged center, but pairing two copies (or appropriate boundary components) by an affine map lies in the pure-piece graph class once all boundary components are paired.

## 5. Same-parameter scaling

Normalize a torus cusp as

\[
g_{\rm cusp}=dt^2+e^{-2t}q_*,
\qquad A_*=\operatorname{Vol}(T^3,q_*).
\]

At depth `T`,

\[
A(T)=A_*e^{-3T},
\qquad V_{\rm tail}(T)=\int_T^\infty A_*e^{-3t}dt=\frac{A(T)}3.
\tag{Cusp}
\]

A degree-`N` one-cusp cover multiplies the cusp cross-sectional covolume by `N`. Taking

\[
T_N=\log N+T_0
\]

gives

\[
A_N(T_N)=A_*e^{-3T_0}N^{-2},
\qquad V_{{\rm rem},N}=\frac{A_*e^{-3T_0}}{3}N^{-2}.
\tag{S1}
\]

The charged Koiso/free-`T^2` center uses a rank-two lattice quotient. It is locally isometric before quotienting and therefore preserves all local normalized curvature quantities while multiplying every four-volume and every integral of a local scalar density such as `|W|^2` or `|E|^p` by `N^{-2}`. If a fixed dimensionless full-matrix connector field `g_conn` is inserted at the matched boundary scale, then

\[
V_{N}=N^{-2}\widehat V,
\quad \int_{N_N}|W|^2=N^{-2}\widehat{\mathcal W},
\quad \int_{N_N}F(E)=N^{-2}\int_{\widehat N}F(E).
\tag{S2}
\]

Consequently `(RCGB)` divides by `N^{-2}` to a fixed dimensionless equation:

\[
2\widehat{\mathcal W}+12(\widehat V-\widehat V_{\rm rem})
=\widehat{\mathcal R}_E.
\tag{S3}
\]

**Main conclusion of the scaling calculation:** the anisotropic lattice parameter that matches the core to the hyperbolic cusp does not by itself make the relative CGB balance easier or harder. Connector volume, removed-cusp volume, Weyl energy, and defect integrals all carry the same leading `N^{-2}` factor. An obstruction must therefore be a dimensionless mismatch in `(S3)` that persists for all increasingly long/flexible connector profiles; no contradiction follows from collapse alone.

The executable bookkeeping file

- `workspace/scripts/step100_relative_cgb_scaling.py`

writes

- `workspace/data/step100_relative_cgb_scaling.json`.

For degrees `1,...,128`, it verifies the `N^{-2}` scaling to relative spread below `2.3e-15`, the cusp-tail relation `V_removed=A/3` exactly in floating arithmetic, and the hyperbolic Gauss–Bonnet relation exactly for the chosen constants. The connector and Weyl densities in that JSON are explicitly labeled placeholders: they demonstrate scaling only and are not measured geometry.

## 6. Connection to the faithful full-matrix family

For a computed slice field `q(r,s)` in Gaussian form, the local volume is

\[
V_N=(2\pi)^2\int\!\int \sqrt{\det q(r,s)}\,ds\,dr
\]

for unit-period orbit coordinates after including the corresponding coordinate-period convention. The Step 98 evaluator already computes `q`, all blocks of `E`, and the invariant operator norm. To evaluate `(RCGB)` faithfully it must additionally compute the full four-dimensional Riemann tensor or Weyl norm, use a correct radial/tangential quadrature, retain the actual orbit periods, and avoid endpoint derivative overwrites. The coarse direct-nodal pilot is unsuitable because it neither saved a continuous optimized field nor differentiated its endpoint jets faithfully.

The one-quintic baseline also cannot decide the budget: its residual is huge and its attachment `q=e^{2r}q0` remains only asymptotically Einstein when `q0` is nonflat. Its volume and CGB terms could be computed as a control, but they would measure that poor interpolant and approximate exterior, not the intended sequence.

A meaningful next calculation should use a jet-preserving piecewise spectral/full-matrix family and, for each common parameter tuple `(N,T_N,R,center data)`, record:

\[
\begin{gathered}
V_N,\quad V_{\rm rem},\quad \int_N|W|^2,\quad
\int_N\left(|E^\circ|^2+2e-e^2/12\right),\\
\sup_N\|E\|_{op},\quad
\text{each Ricci block},\quad
\text{positivity and endpoint errors},\quad
\text{and the exterior correction if nonhyperbolic.}
\end{gathered}
\]

The exact residual of `(RCGB)` should converge to zero under independent grid refinement. The scientifically decisive quantity is the normalized mismatch

\[
\mathcal M=
\frac{2\int_N|W|^2+12(V_N-V_{\rm rem})}{V_N},
\]

compared with the bound `|M| <= 8 delta+4 delta^2`. If `delta -> 0` while `M` stays away from zero after all center, truncation, and affine data vary, the result points toward a scoped obstruction theorem. If `M -> 0`, CGB remains compatible and work returns to the full joint inner transition.

## 7. Research judgment

The Step 99 finite-target reinterpretation was a quantifier error and a topology error, not a promising route. The corrected relative budget is valuable because it finally connects the highly developed local charged connector to an explicit no-Einstein pure-piece graph family in one normalization.

The calculation does not currently yield a mismatch. In fact, the common `N^{-2}` scaling shows that the lattice-collapse mechanism is compatible with all terms at leading order. CGB therefore does not presently replace the inner matching problem. It supplies an exact global consistency relation that every future construction must satisfy and a dimensionless observable capable of distinguishing a real global obstruction from mere local interpolation failure.

The unrestricted Yau 26 problem remains open: no negative-branch vanishing-defect graph sequence, positive-branch failure, universal existence theorem, or Lean formalization has been obtained.
