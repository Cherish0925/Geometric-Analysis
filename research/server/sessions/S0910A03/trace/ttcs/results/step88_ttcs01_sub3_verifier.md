# TTCS Independent Branch Record

```json
{
  "step_id": 88,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/scripts/step88_minimal_separator_verify.py",
    "Sessions/S0910A03/workspace/data/step88_minimal_separator_verify.json"
  ]
}
```

## Task

Independently verify and strengthen the proposed removal of reflection from the Step 87 forced OT obstruction. Work in a complete 4-manifold with a free orthogonally transitive T^2 action, quotient base B diffeomorphic to a cylinder, exact outward expanding cusp ends, and E=Ric+3g with ||E||op<=delta. (i) For any invariant minimal hypersurface Sigma=pi^{-1}(C) over an essential closed base curve C, derive with explicit normal and induced-measure conventions the contracted Gauss formula and the periodic intrinsic T^3 scalar identity for q=ds^2+G(s), G=e^sigma M. Check whether <e_s>=12-2<D>+2<|II|^2>+<h^2> and hence >=12-8delta is exactly correct, where D=tr E-2E(nu,nu), h=sigma_s, e_s=|U_s|^2, averages use rho ds, and full base e dominates e_s. (ii) Prove or find the precise missing hypotheses in obtaining an interior smooth essential-loop minimizer for length in the auxiliary metric rho^2 gamma_B, using the two expanding ends. Check equivalence between geodesicity of C for rho^2 gamma_B and minimality of pi^{-1}(C) in g, and analyze boundary barriers/properness rather than assuming reflection or a global Gaussian foliation. (iii) Check that Step 87's complete-base massive-resolvent ceiling applies unchanged, and state the strongest mathematically justified theorem. Identify any subtle failure involving completeness, end orientation, homotopy-class minimization, self-intersection, weighted averages, or attachment regularity.

## Output

# Scientific memo: reflection-free forced OT obstruction

## 1. Minimal invariant separator and its scalar identity

Let
\[
g=\gamma_B+G_{ab}\,d\xi^a d\xi^b,\qquad
G=e^\sigma M,\qquad \det M=1,
\]
on a complete free orthogonally transitive \(T^2\)-manifold. Put
\[
\rho=\sqrt{\det G}=e^\sigma .
\]
Let \(C\subset B\) be a smooth embedded essential closed curve, parametrized by \(\gamma_B\)-arclength \(s\). Write \(T=C_s\), choose either \(\gamma_B\)-unit normal \(\nu\), and let
\[
\Sigma=\pi^{-1}(C),\qquad q=g|_\Sigma=ds^2+G_{ab}(s)d\xi^a d\xi^b.
\]
With a fixed Haar-coordinate fundamental volume \(\mathcal V_{T^2}\),
\[
d\operatorname{vol}_q=\rho\,ds\,d\xi^1d\xi^2,
\qquad
\langle f\rangle_C
=\frac{\int_C f\rho\,ds}{\int_C\rho\,ds}.
\]

Use
\[
\mathrm{II}(X,Y)=g(\nabla_X\nu,Y),\qquad H=\operatorname{tr}_q\mathrm{II}.
\]
Reversing \(\nu\) reverses \(\mathrm{II}\) and \(H\), while all equations below remain invariant.

### Contracted Gauss equation

For any hypersurface,
\[
R_q=R_g-2\operatorname{Ric}_g(\nu,\nu)+H^2-|\mathrm{II}|^2.
\]
Since \(E=\operatorname{Ric}_g+3g\) in dimension four,
\[
R_g=-12+\operatorname{tr}_gE,\qquad
\operatorname{Ric}_g(\nu,\nu)=-3+E(\nu,\nu).
\]
If \(\Sigma\) is minimal, \(H=0\), and therefore
\[
\boxed{
R_q=-6+D-|\mathrm{II}|^2,
\qquad
D:=\operatorname{tr}_gE-2E(\nu,\nu).}
\tag{1.1}
\]

In a \(g\)-orthonormal frame \((T,V_1,V_2,\nu)\),
\[
D=E(T,T)+E(V_1,V_1)+E(V_2,V_2)-E(\nu,\nu).
\]
Thus
\[
\|E\|_{\mathrm{op}}\le\delta
\quad\Longrightarrow\quad
|D|\le4\delta.
\tag{1.2}
\]
The coefficient \(4\) is the exact algebraic estimate available from the operator norm alone.

### Intrinsic scalar curvature of \(q\)

Let
\[
A=\frac12G^{-1}G_s,\qquad h=\sigma_s=\frac{\rho_s}{\rho}.
\]
For the \(T^2\)-foliation of \((\Sigma,q)\),
\[
R_q=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2).
\tag{1.3}
\]
Writing \(P=M^{-1}M_s\), one has
\[
\operatorname{tr}P=0,\qquad
A=\frac12(hI+P).
\]
In the \(H^2=SL(2)/SO(2)\) normalization used in Steps 85–87,
\[
e_s:=|U_s|_{\mathbb H^2}^2=\frac12\operatorname{tr}(P^2).
\]
Consequently
\[
\operatorname{tr}(A^2)=\frac12h^2+\frac12e_s,
\]
and hence
\[
\boxed{
R_q=-2h_s-\frac32h^2-\frac12e_s.}
\tag{1.4}
\]

Because \(C\) is closed and \(\rho_s=h\rho\),
\[
\int_C\rho h_s\,ds
=-\int_C\rho h^2\,ds.
\]
Averaging (1.4) therefore gives
\[
\boxed{
\langle R_q\rangle_C
=\frac12\bigl(\langle h^2\rangle_C-\langle e_s\rangle_C\bigr).}
\tag{1.5}
\]

Equating (1.1) and (1.5) yields the exact separator identity
\[
\boxed{
\langle e_s\rangle_C
=
12-2\langle D\rangle_C
+2\langle|\mathrm{II}|^2\rangle_C
+\langle h^2\rangle_C.}
\tag{1.6}
\]
Thus the proposed formula is exactly correct, including every coefficient and sign. In particular,
\[
\boxed{\langle e_s\rangle_C\ge12-8\delta.}
\tag{1.7}
\]

Finally, along \(C\), \((T,\nu)\) is a \(\gamma_B\)-orthonormal base frame, so
\[
e=|dU|_{\gamma_B}^2
=|dU(T)|^2+|dU(\nu)|^2
=e_s+|dU(\nu)|^2\ge e_s.
\tag{1.8}
\]
Therefore
\[
\sup_B e\ge\langle e_s\rangle_C\ge12-8\delta.
\tag{1.9}
\]

The symbolic equalities in `step88_minimal_separator_verify.py` and its JSON output agree with (1.5), (1.6), and (1.2).

---

## 2. Weighted-loop geodesics are precisely invariant minimal hypersurfaces

Set
\[
\widehat\gamma:=\rho^2\gamma_B.
\]
The \(g\)-area of an invariant hypersurface over \(C\) is
\[
\operatorname{Area}_g(\pi^{-1}(C))
=\mathcal V_{T^2}\int_C\rho\,ds_{\gamma_B}
=\mathcal V_{T^2}\operatorname{Length}_{\widehat\gamma}(C).
\tag{2.1}
\]

For a pointwise verification, define the \(\gamma_B\)-geodesic curvature
\[
k_\gamma=\langle\nabla_TT,\nu\rangle.
\]
Then
\[
\mathrm{II}(T,T)
=\langle\nabla_T\nu,T\rangle=-k_\gamma.
\]
For a vertical orthonormal frame, the Koszul formula gives
\[
2g(\nabla_{V_a}\nu,V_b)=\nu(G_{ab}),
\]
and hence
\[
\sum_{a=1}^2\mathrm{II}(V_a,V_a)
=\frac12\operatorname{tr}(G^{-1}\nu G)
=\nu(\log\rho).
\]
Thus
\[
\boxed{H=-k_\gamma+\nu(\log\rho).}
\tag{2.2}
\]

Under the conformal change \(\widehat\gamma=\rho^2\gamma_B\),
\[
k_{\widehat\gamma}
=\rho^{-1}\bigl(k_\gamma-\nu(\log\rho)\bigr)
=-\rho^{-1}H.
\tag{2.3}
\]
Therefore
\[
\boxed{
C\text{ is a }\widehat\gamma\text{-geodesic}
\iff
\pi^{-1}(C)\text{ is minimal in }g.}
\tag{2.4}
\]
This is pointwise, so stationarity under invariant variations already gives full minimality; no global Gaussian foliation is involved.

---

## 3. Existence of a smooth embedded essential minimizer

The end hypothesis needs the following precise interpretation. Outside a compact subset, \(B\) has two components
\[
E_\pm\simeq [T_0,\infty)_{t_\pm}\times S^1_{z_\pm},
\]
where \(t_\pm\to+\infty\) points outward on both ends and
\[
\gamma_B=dt_\pm^2+e^{2t_\pm}dz_\pm^2,\qquad
\rho=c_\pm e^{2t_\pm},\qquad c_\pm>0.
\tag{3.1}
\]
The circle coordinate has a fixed period \(\ell_\pm\), and its class is the primitive generator of the cylindrical end.

Then
\[
\widehat\gamma
=c_\pm^2e^{4t_\pm}dt_\pm^2
+c_\pm^2e^{6t_\pm}dz_\pm^2.
\tag{3.2}
\]
Both the radial distance
\[
\int^{\infty}c_\pm e^{2t}\,dt
\]
and the length of a degree-one level loop
\[
c_\pm e^{3t}\ell_\pm
\]
diverge. Since \(\rho\) has a positive minimum on the compact middle region, \((B,\widehat\gamma)\) is complete and proper.

Let \(L_0\) be the \(\widehat\gamma\)-length of one fixed primitive essential loop. Choose \(T\) so large that
\[
c_\pm e^{3T}\ell_\pm>L_0+1
\]
on both ends. Any primitive loop lying entirely in \(t_\pm\ge T\) satisfies
\[
L_{\widehat\gamma}(C)
\ge
c_\pm e^{3T}\left|\int_C dz_\pm\right|
=c_\pm e^{3T}\ell_\pm>L_0+1.
\tag{3.3}
\]
Hence every minimizing sequence of length at most \(L_0+1\) meets a fixed compact subset. Each such loop then lies in a fixed metric neighborhood of that subset, which is compact by properness. The direct method gives a length minimizer in the primitive class.

Smoothness and embeddedness can be obtained cleanly by minimizing mass among integral \(1\)-cycles representing the generator of \(H_1(B;\mathbb Z)\). Compactness follows from the same end estimate. A minimizing \(1\)-cycle on a smooth surface is a smooth union of embedded closed geodesics with integer multiplicities. Contractible components can be removed. Since every embedded essential component of a cylinder represents \(\pm1\), total homology \(+1\) forces the minimizer to be one embedded essential geodesic with multiplicity one.

There is also a direct geometric end barrier. With
\[
R=\frac{c_\pm}{2}e^{2t_\pm},
\]
equation (3.2) becomes
\[
\widehat\gamma=dR^2+F(R)^2dz_\pm^2,
\qquad F(R)=2^{3/2}c_\pm^{-1/2}R^{3/2}.
\]
Along an affinely parametrized geodesic,
\[
R''=F(R)F'(R)\,(z_\pm')^2.
\tag{3.4}
\]
A closed geodesic cannot have a maximum of \(R\) in an exact end: at such a point (3.4) contradicts \(R''\le0\), while \(R'=z'=0\) would give zero velocity. Thus the resulting geodesic lies on the compact side of the exact end regions.

### Why outward orientation matters

Completeness of \(g\) alone does not imply completeness of \(\widehat\gamma\). For example,
\[
g=dt^2+e^{2t}g_{T^3}\qquad\text{on }\mathbb R\times T^3
\]
is complete and satisfies \(E=0\). Its \(t\to+\infty\) end expands, but its \(t\to-\infty\) end shrinks. There
\[
\rho\asymp e^{2t},\qquad
\int_{-\infty}^{t_0}\rho\,dt<\infty,
\qquad
L_{\widehat\gamma}(\{t\}\times S^1)\asymp e^{3t}\to0.
\]
The primitive length infimum escapes through that end and is not attained. Thus “two cusp ends” is insufficient unless both end coordinates increase outward with the expanding form (3.1).

---

## 4. Massive-resolvent ceiling

Reflection is not used anywhere in the complete-base argument of Step 87. Under the global free-OT reduction,
\[
\operatorname{Ric}^4_f
=
\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
=
-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B
\ge-(3+\delta)\gamma_B.
\tag{4.1}
\]
Thus \(CD(-(3+\delta),4)\) holds.

Let
\[
K_0=3+\delta,\qquad \kappa=2K_0.
\]
The forced Bochner inequality gives
\[
(-L+\kappa)e
\le\kappa^2+8\delta^2-2\operatorname{div}_\sigma V,
\qquad |V|\le2\delta\sqrt e.
\tag{4.2}
\]

The Fisher-information calculation yields
\[
C_\kappa
:=\sup_x\int_B|\nabla_yG_\kappa(x,y)|\,d\mu(y)
\le\frac{2}{\sqrt{3+\delta}}.
\tag{4.3}
\]
Step 87’s boxed equality in its equation (5.1) should be read as an upper estimate: saturation of the heat-kernel inequalities has not been shown. All subsequent algebra uses only (4.3), so its ceiling is unchanged.

On exact ends, \(U\) is constant and the defect vanishes. Hence \(e,F,V\) vanish outside a compact subset. In particular, \(e\) is bounded and integration by parts against \(G_\kappa\) has no end flux. If
\[
\mathscr E=\sup_B e,
\]
Duhamel comparison gives
\[
\mathscr E
\le
2(3+\delta)+\frac{4\delta^2}{3+\delta}
+\frac{8\delta}{\sqrt{3+\delta}}\sqrt{\mathscr E}.
\]
Solving this quadratic inequality yields
\[
\boxed{
\mathscr E\le\mathcal B(\delta):=
\left[
\frac{4\delta}{\sqrt{3+\delta}}
+
\sqrt{2(3+\delta)+\frac{20\delta^2}{3+\delta}}
\right]^2.}
\tag{4.4}
\]

---

## 5. Resulting theorem

**Theorem.**  
Let \((M^4,g)\) be complete and smooth, with a free orthogonally transitive isometric \(T^2\)-action. Suppose:

1. \(B=M/T^2\) is diffeomorphic to \(S^1\times\mathbb R\);
2. outside a compact set, both components have the exact outward model (3.1), with constant orbit map \(U\);
3. \(E=\operatorname{Ric}_g+3g\) satisfies \(\|E\|_{\mathrm{op}}\le\delta\).

Then there is a smooth embedded essential \(\widehat\gamma\)-geodesic \(C\), and \(\Sigma=\pi^{-1}(C)\) is a smooth invariant minimal \(T^3\). Moreover,
\[
12-2\langle D\rangle_C
+2\langle|\mathrm{II}|^2\rangle_C
+\langle h^2\rangle_C
\le \mathcal B(\delta),
\tag{5.1}
\]
and consequently
\[
12-8\delta\le\mathcal B(\delta).
\tag{5.2}
\]

The function \(\mathcal B(\delta)\) is strictly increasing for \(\delta\ge0\), while \(12-8\delta\) is strictly decreasing. Their unique intersection is
\[
\boxed{\delta_*=0.246249763690668\ldots}
\]
defined by
\[
\mathcal B(\delta_*)=12-8\delta_*.
\]
Therefore no such complete two-ended free-OT metric exists for
\[
\boxed{0\le\delta<\delta_*.}
\]

This removes reflection from the Step 87 obstruction under the stated exact two-ended outward-expansion assumptions. The minimal separator replaces the reflected center, and its extra terms \(2\langle|\mathrm{II}|^2\rangle+\langle h^2\rangle\) only strengthen the energy floor.

For merely asymptotic ends, additional decay data are required: bounded \(e\), the global \(CD\) estimate, and sufficient control of \(V\) to justify the resolvent integration by parts. Smooth exact attachment on open end neighborhoods supplies all of these automatically. The Step 88 script verifies the coefficient algebra and end growth; the variational compactness and embedded regularity are supplied by the argument above rather than by that computation.