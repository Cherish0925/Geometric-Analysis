# Step 88: reflection-free minimal-separator obstruction and the twist frontier

Session `S0910A03`, Agent1 / Explore.

> **Strengthens Step 87.** Reflection and a totally geodesic center are not needed for
> the complete free-\(T^2\), orthogonally transitive (OT) obstruction. Two exact
> outward-expanding ends produce an invariant minimal separator by weighted-length
> minimization, and its Gauss identity gives the same \(12-8\delta\) energy floor,
> with additional nonnegative terms.
>
> The result remains a theorem about a specific symmetry class and complete end
> geometry. It does not apply to a general graph-manifold metric or to an
> \(S^3\)-neck in \(N\#N\).

## 1. Geometric setting and conventions

Let \((X^4,g)\) be complete and carry a free isometric OT \(T^2\)-action. Its
quotient \(B=X/T^2\) is a smooth surface and
\[
 g=\gamma_B+G_{ab}\,d\xi^a d\xi^b,
 \qquad G=e^\sigma M,
 \qquad \det M=1,
 \qquad \rho:=\sqrt{\det G}=e^\sigma.
\]
The map represented by \(M\) is
\(U:B\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2\), and
\[
 e=|dU|_{\gamma_B}^2.
\]
Normalize
\[
 E=\operatorname{Ric}_g+3g,
 \qquad \|E\|_{\mathrm{op}}\le\delta.
\]

Assume \(B\cong S^1\times\mathbb R\), and outside a compact set its two
components have outward coordinates \(t_\pm\to+\infty\) with the exact models
\[
 \gamma_B=dt_\pm^2+e^{2t_\pm}dz_\pm^2,
 \qquad
 \rho=c_\pm e^{2t_\pm},
 \qquad c_\pm>0,
\tag{1.1}
\]
and constant orbit map \(U\). The word *outward* is load-bearing. A cylinder with
one contracting end does not have the minimizing separator proved below.

For a hypersurface use
\[
 \mathrm{II}(X,Y)=g(\nabla_X\nu,Y),
 \qquad H=\operatorname{tr}\mathrm{II}.
\]

## 2. Minimal separator: exact scalar identity

Let \(C\subset B\) be a smooth embedded essential closed curve, parameterized by
\(\gamma_B\)-arclength \(s\), and let
\(\Sigma=\pi^{-1}(C)\). Its induced metric and reduced volume measure are
\[
 q=ds^2+G_{ab}(s)d\xi^a d\xi^b,
 \qquad d\mu=\rho\,ds.
\]
Averages below mean
\[
 \langle f\rangle_C
 :=\frac{\int_Cf\rho\,ds}{\int_C\rho\,ds}.
\]
Set
\[
 h=\sigma_s=(\log\rho)_s,
 \qquad e_s=|U_s|_{\mathbb H^2}^2.
\]

If \(\Sigma\) is minimal, the contracted Gauss equation is
\[
 R_q=R_g-2\operatorname{Ric}_g(\nu,\nu)-|\mathrm{II}|^2
     =-6+D-|\mathrm{II}|^2,
\tag{2.1}
\]
where
\[
 D=\operatorname{tr}_gE-2E(\nu,\nu).
\]
In an orthonormal frame \((T,V_1,V_2,\nu)\),
\[
 D=E(T,T)+E(V_1,V_1)+E(V_2,V_2)-E(\nu,\nu),
\]
so
\[
 |D|\le4\delta.
\tag{2.2}
\]

Intrinsic to \(q=ds^2+G(s)\), put
\(A=\tfrac12G^{-1}G_s\) and \(P=M^{-1}M_s\). Then
\(A=\tfrac12(hI+P)\), \(\operatorname{tr}P=0\), and in the normalization used
in Steps 79--87,
\[
 e_s=\frac12\operatorname{tr}(P^2).
\]
The one-dimensional Gauss formula gives
\[
 R_q=-2h_s-\frac32h^2-\frac12e_s.
\tag{2.3}
\]
Since \(C\) is closed and \(\rho_s=h\rho\),
\[
 \int_C\rho h_s\,ds=-\int_C\rho h^2\,ds,
\]
hence
\[
 \langle R_q\rangle_C
 =\frac12\bigl(\langle h^2\rangle_C-\langle e_s\rangle_C\bigr).
\tag{2.4}
\]
Equating (2.1) and (2.4) yields the exact identity
\[
 \boxed{
 \langle e_s\rangle_C
 =12-2\langle D\rangle_C
   +2\langle|\mathrm{II}|^2\rangle_C
   +\langle h^2\rangle_C.}
\tag{2.5}
\]
Consequently
\[
 \boxed{\langle e_s\rangle_C\ge12-8\delta.}
\tag{2.6}
\]
Moreover, if \(T,\nu\) are the tangent and normal frame of \(C\) in \(B\), then
\[
 e=|dU(T)|^2+|dU(\nu)|^2\ge e_s
\]
on \(C\), so
\[
 \boxed{\sup_Be\ge12-8\delta.}
\tag{2.7}
\]
The second fundamental form does not weaken the old reflected floor; it raises it.


### 2.1 The floor itself survives connection twist

Although the combined obstruction below uses OT for its Bochner ceiling, the
separator identity (2.5) does not. For a general free invariant metric write
locally
\[
 g=\gamma_B+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b).
\tag{2.8}
\]
Over a base curve \(C\), use its horizontal lift as the unit tangent in
\(\Sigma=\pi^{-1}(C)\). The induced volume is still \(\rho\,ds\) and, on the
universal cover of \(C\), the one-dimensional connection \(A_sds\) can be gauged
away. Its only global remnant is torus-translation holonomy, which does not change
local scalar curvature. Hence (2.3)--(2.6) remain valid. Likewise the first
variation of \(\int_C\rho ds\) shows that a
\(\rho^2\gamma_B\)-geodesic lifts to a minimal invariant hypersurface without OT.

Thus every free-\(T^2\)-invariant candidate with the two expanding ends has a
minimal separator satisfying
\[
 \sup_B |dU|^2\ge12-8\delta,
\tag{2.9}
\]
where \(U\) is the orbit-shape map in a fixed Lie-algebra basis. Connection twist
can escape only by changing the *upper* Bochner/resolvent comparison; it cannot
remove the separator floor. Since principal \(T^2\)-bundles over \(S^1\) are
topologically trivial, the lift is a \(T^3\), although its connection may have
nontrivial flat holonomy along \(C\).

## 3. Why the separator exists

Define the auxiliary surface metric
\[
 \widehat\gamma=\rho^2\gamma_B.
\tag{3.1}
\]
For every base curve \(C\), up to the fixed coordinate volume of the torus,
\[
 \operatorname{Vol}_3(\pi^{-1}(C))
 =\int_C\rho\,ds_{\gamma_B}
 =\operatorname{Length}_{\widehat\gamma}(C).
\tag{3.2}
\]

Let \(T\) be the unit tangent and define
\(k_\gamma=\langle\nabla_TT,\nu\rangle\). Directly,
\[
 \mathrm{II}(T,T)=-k_\gamma,
 \qquad
 \operatorname{tr}_{T^2}\mathrm{II}=\nu(\log\rho),
\]
so
\[
 H=-k_\gamma+\nu(\log\rho).
\tag{3.3}
\]
Under \(\widehat\gamma=\rho^2\gamma_B\), with the same curvature convention,
\[
 k_{\widehat\gamma}
 =\rho^{-1}\bigl(k_\gamma-\nu(\log\rho)\bigr)
 =-\rho^{-1}H.
\tag{3.4}
\]
Thus
\[
 C\text{ is a }\widehat\gamma\text{-geodesic}
 \quad\Longleftrightarrow\quad
 \pi^{-1}(C)\text{ is minimal in }(X,g).
\tag{3.5}
\]
No Gaussian foliation through the core is used.

On either exact end (1.1),
\[
 \widehat\gamma
 =c_\pm^2e^{4t_\pm}dt_\pm^2
  +c_\pm^2e^{6t_\pm}dz_\pm^2.
\tag{3.6}
\]
The outward radial distance is infinite:
\[
 \int^\infty c_\pm e^{2t}\,dt=\infty.
\]
If the \(z_\pm\)-period is \(\ell_\pm\), every degree-one loop lying in
\(t_\pm\ge T\) has
\[
 L_{\widehat\gamma}(C)
 \ge c_\pm e^{3T}\left|\int_Cdz_\pm\right|
 =c_\pm e^{3T}\ell_\pm\longrightarrow\infty.
\tag{3.7}
\]
Hence \((B,\widehat\gamma)\) is complete and proper and the primitive essential
loop class is coercive at both ends. A minimizing sequence meets a fixed compact
core and, by its bounded length, lies in a fixed compact metric neighborhood.
Minimizing integral one-cycle mass in the generator of \(H_1(B;\mathbb Z)\)
therefore gives a smooth union of embedded closed geodesics. Contractible
components can be removed. If several essential components remain, each carries
class \(\pm1\); canceling oppositely oriented nested pairs leaves a single
multiplicity-one component in class \(+1\) without increasing mass. Thus one may
choose a smooth embedded essential minimizing geodesic.

Equivalently, in
\(R=(c_\pm/2)e^{2t_\pm}\) coordinates the end is
\(dR^2+F(R)^2dz^2\) with \(F'>0\). Along an affinely parameterized geodesic,
\(R''=FF'(z')^2\), which forbids an interior maximum of \(R\) for a closed
geodesic in the end. This is the geometric end barrier.

The orientation condition cannot be dropped: on the exact hyperbolic cylinder
\(dt^2+e^{2t}g_{T^3}\), the \(t\to-\infty\) end has
\(\int e^{2t}dt<\infty\) and essential loop lengths tend to zero, so the
primitive infimum escapes and is not attained.

## 4. Reflection-free resolvent obstruction

The complete-base massive ceiling of Step 87 never used reflection. The global OT
equations give
\[
 \operatorname{Ric}^{4}_{\sigma}
 =\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
 =-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B
 \ge-(3+\delta)\gamma_B.
\tag{4.1}
\]
With \(L=\Delta+\nabla\sigma\cdot\nabla\), \(\kappa=6+2\delta\), and the orbit
forcing field of Steps 85--87, the forced Bochner inequality gives
\[
 (-L+\kappa)e
 \le\kappa^2+8\delta^2-2\operatorname{div}_\sigma V,
 \qquad |V|\le2\delta\sqrt e.
\tag{4.2}
\]
The corrected finite-dimensional Fisher-information estimate gives the resolvent
gradient upper estimate
\[
 \sup_x\int_B|\nabla_yG_\kappa(x,y)|\,d\mu(y)
 \le\frac2{\sqrt{3+\delta}}.
\tag{4.3}
\]
It is an upper estimate, not a proved equality. Exact constant-\(U\) ends make
\(e=V=0\) there, so boundedness and the integration at infinity are immediate.
The Step 87 Duhamel comparison is unchanged:
\[
 \sup_Be\le\mathcal B(\delta):=
 \left[
 \frac{4\delta}{\sqrt{3+\delta}}+
 \sqrt{2(3+\delta)+\frac{20\delta^2}{3+\delta}}
 \right]^2.
\tag{4.4}
\]
Combining (2.7) and (4.4),
\[
 12-8\delta\le\mathcal B(\delta).
\tag{4.5}
\]
The unique crossing is
\[
 \delta_*=0.246249763690668\ldots.
\]

### Theorem

There is no complete smooth four-manifold satisfying all of the following for
\(0\le\delta<\delta_*\):

1. a free isometric OT \(T^2\)-action;
2. quotient base \(S^1\times\mathbb R\);
3. two exact outward-expanding ends of the form (1.1), with constant orbit map and
   smooth attachment;
4. \(\|\operatorname{Ric}_g+3g\|_{\mathrm{op}}\le\delta\).

For merely asymptotic ends, one must separately prove completeness and properness
of \(\rho^2\gamma_B\), coercivity of the primitive loop class, boundedness of
\(e\), global \(CD(-(3+\delta),4)\), and enough decay of \(V\) for the resolvent
integration at infinity.

## 5. What changed in the construction landscape

Nonreflection is not an escape within this complete OT cylinder class. Reflection
was only a convenient way to exhibit a separator; two outward-expanding ends force
one variationally. The theorem does **not** say that small Ricci defect forces
symmetry, and metric averaging need not preserve the operator Ricci estimate.
It also does not touch the diffuse non-OT \(S^3\)-neck mechanism highlighted by
A02 message #638.

The nearest structural extension is a free \(T^2\)-invariant but non-OT metric
\[
 g=\gamma_{ij}dx^idx^j+
 G_{ab}(d\xi^a+A_i^a dx^i)(d\xi^b+A_j^b dx^j),
 \qquad F^a=dA^a.
\tag{5.1}
\]
Clean-context analysis indicates three important facts requiring a unified tensor
check before theorem use. A newly retrieved primary source gives an exact mixed
Ricci/twist formula in an invariant horizontal frame: its twist scalars are
constant for an exact Einstein metric \cite{liutoric}. That source settles the
conservation structure, while its full variable-\(G\) stress coefficients still
need translation into the present normalization:

* the mixed Ricci equation is a weighted Abelian Maxwell law; in the exact case
  the source-defined scalars
  \(\alpha_a=\rho\langle[X,Y/\mu],V_a\rangle\) are constant. In coordinates this
  is the precise invariant content behind a charge of the form
  \(q_a=\rho G_{ab}*_\gamma F^b\);
* connection-curvature stress has a favorable isotropic contribution to the base
  finite-dimensional drift curvature and contributes nonnegatively to
  \(|\mathrm{II}|^2\) on a minimal separator;
* its traceless vertical stress forces the orbit-shape equation even when
  \(E=0\), creating a \(-|\tau_\sigma(U)|^2\) term and a divergence flux in the
  Bochner identity. Without pointwise control of the Maxwell energy, the Step 87
  ceiling does not automatically close.

Thus twist is a genuine candidate escape within symmetry, not something controlled
by \(\delta\) alone. Exact cusp *open sets* with \(F=0\) may force zero exact charge
by the Maxwell law, whereas merely \(F\to0\) can coexist with nonzero charge as
\(\rho\to\infty\). This distinction should govern the next derivation.

## 6. Verification and provenance

* `workspace/scripts/step88_minimal_separator_verify.py` checks the scalar, Gauss,
  defect, end-growth, and threshold algebra.
* `workspace/data/step88_minimal_separator_verify.json` records zero symbolic
  residuals and \(\delta_*=0.24624976369066845\).
* `workspace/notes/step88_source_note_twist.md` records Liu's mixed Ricci formula,
  exact twist-scalar constancy, and the distinction between exact and merely
  asymptotic OT ends \cite{liutoric}.
* Independent derivations:
  `trace/ttcs/results/step88_ttcs01_verifier1_integration.md`, with both complete
  verifier branches under the same TTCS task.
* Twist hypothesis generation:
  `trace/ttcs/results/step88_ttcs01_generator1_integration.md`. Its precise
  Kaluza--Klein coefficients and proposed numerical twist threshold are not yet
  adopted; they need an index-level derivation for variable \(G\).
* Literature sources read in this Step confirm the Kaluza--Klein decomposition and
  Yang--Mills/base-stress structure. Liu gives the mixed Ricci/twist conservation
  formulas for variable orbit metric \cite{liutoric}; the separate bundle source
  quoted for a fixed totally geodesic fibre metric does not by itself justify all
  variable-\(G\) base and vertical stress coefficients needed here.
