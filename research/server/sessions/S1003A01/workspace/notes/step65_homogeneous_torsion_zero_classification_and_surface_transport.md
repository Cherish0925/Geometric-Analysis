# Step 65 — Q4: homogeneous torsion-zero classification and the unresolved surface transport

Agent3, Execute. Inputs: Steps 62–64, Spirit #76, AAD equations recorded in `step55_darboux_ricci_compatibility.md`, and independent TTCS verification. Scripts/data: `scripts/spirit_step64_homogeneous_quadric_check.py`; `scripts/step65_homogeneous_identity_exact.py`; `scripts/step65_rank2_surface_linearization.py`; `data/spirit_step64/homogeneous_quadric_comparison.json`; `data/step65/homogeneous_identity_m2_exact.json`; `data/step65/rank2_surface_linearization.json`; the new lambda-zero run `data/step64/level6_lam0.0_s1.{json,npz}` and `intrinsic_lam0.0_s1.json`.

Labels: [P] proved from the displayed geometric equations; [E] exact/algebraic computation; [N] floating numerical comparison; [O] unresolved.

## 1. Exact scalar equation for the torsion energy [P]

Use

\[
\Delta=\operatorname{tr}\nabla^2=-\nabla^*\nabla,
\qquad u=\Omega/\sqrt2,
\qquad q=|\nabla\Omega|^2,
\]

and split

\[
W^+=\begin{pmatrix}r&\eta^T\\ \eta&-\frac r2I+V\end{pmatrix},
\qquad r=\frac s6+\frac q4,
\qquad \operatorname{tr}V=0.
\]

The harmonic-form and Einstein Weyl equations are

\[
\Delta u=-2W^+u+\frac s3u,
\qquad
\Delta W^+=\frac s2W^+-6(W^+)^2+2\operatorname{tr}((W^+)^2)I.
\]

The AAD gauge gives

\[
\sum_i(\nabla_i u)\otimes(\nabla_i u)=\frac q4 I_{u^\perp}.
\]

Applying the full product rule to \(r=\langle W^+u,u\rangle\), including the derivative source, gives

\[
\boxed{
\Delta q=8\operatorname{tr}V^2-24|\eta|^2-\frac{3s}{2}q-\frac94q^2
+16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle .}
\tag{65.1}
\]

The intermediate algebraic contribution is

\[
\frac{7s}{6}r-7r^2-\frac q2r-6|\eta|^2+2\operatorname{tr}V^2.
\]

At a torsion zero, the source and \(q\) vanish and \(\Delta q=2|\nabla^2\Omega|^2\). Thus (65.1) recovers the Step-62 identity

\[
|\nabla^2\Omega|^2=4\operatorname{tr}V^2-12|\eta|^2,
\]

which fixes the signs and constants.

## 2. The leading polynomial identity at a finite-order zero [P]

Suppose the AAD torsion one-form \(a\) has first nonzero homogeneous Taylor term \(f_m\), of degree \(m\). The principal half-twistor equation gives

\[
 f_m(z,\bar z)=z h(\bar z)+g(\bar z),
\]

where \(h\) is scalar homogeneous of degree \(m-1\) and \(g\) is \(\mathbb C^2\)-valued homogeneous of degree \(m\). Put \(w=\bar z\),

\[
B=z\otimes D_wh+D_wg,
\qquad A=\frac{B-B^T}{2},
\qquad S=\frac{B+B^T}{2}.
\]

The all-order principal curvature dictionary is

\[
|\eta|^2=4|h|^2+O(|x|^{2m-1}),
\qquad
\operatorname{tr}V^2=4\|A\|^2+O(|x|^{2m-1}),
\]

and

\[
\|Df_m\|_{\mathbb R}^2=4|h|^2+2\|A\|^2+2\|S\|^2.
\]

This follows from the exact AAD Ricci identities at their principal degree: frame terms multiply \(a\), torsion-quadratic terms begin later, and the scalar curvature action on \(\Omega^\perp\) cancels at the zero. A fully standalone presentation should still spell out these remainder estimates, but no realization assumption enters this leading calculation.

The derivative source in (65.1) has leading part

\[
\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle
=-4\operatorname{Re}\sum_j\overline{f_{m,j}}\,\partial_{w_j}h.
\]

Comparing the homogeneous degree \(2m-2\) terms in (65.1) yields

\[
\boxed{
\|A\|^2-\|S\|^2-8|h|^2
-6\operatorname{Re}\sum_j\overline{f_{m,j}}\,\partial_{w_j}h=0.}
\tag{65.2}
\]

For \(m=1\), the last term is absent and (65.2) is exactly the Step-62 cone \(\|A\|^2=8|h|^2+\|S\|^2\).

## 3. Complete algebraic classification of the leading homogeneous term [P]

Assume \(m\ge2\). Euler homogeneity rewrites (65.2) as

\[
\operatorname{tr}(\overline{Dg}Dg)+(m+1)(m+3)|h|^2
+2(m+3)\operatorname{Re}\sum_i\overline{g_i}\,\partial_{w_i}h=0.
\tag{65.3}
\]

The first two terms have bidegree \((m-1,m-1)\), while the last term and its conjugate have bidegrees \((m-2,m)\) and \((m,m-2)\). Complexifying the real source coordinates makes \(w,\bar w\) independent, so

\[
\sum_i\overline{g_i}\,\partial_{w_i}h=0,
\qquad
\operatorname{tr}(\overline{Dg}Dg)+(m+1)(m+3)|h|^2=0.
\tag{65.4}
\]

If \(g_1,g_2\) are polynomially independent, the first equation forces \(Dh=0\). If \(g=vG\) takes values in one fixed complex line, then

\[
\operatorname{tr}(\overline{Dg}Dg)
=\left|\sum_i\bar v_i\,\partial_{w_i}G\right|^2\ge0,
\]

so the second equation again forces \(h=0\). This avoids an invalid independent target rotation, which would not preserve the transpose split.

With \(h=0\), define the Hermitian form on \(2\times2\) complex matrices

\[
\mathcal H(M,N)=\operatorname{tr}(\bar M N).
\]

It has signature \((3,1)\). Expanding \(Dg=\sum M_\alpha w^\alpha\), (65.4) implies all pairings \(\mathcal H(M_\alpha,M_\beta)\) vanish. Hence the coefficient matrices span at most one totally isotropic complex line:

\[
Dg=M p(w).
\]

Mixed-partial equality excludes rank two for \(M\), and gives \(M=v\otimes\ell\), \(p=c(\ell\cdot w)^{m-1}\). Isotropy is \(|\ell\cdot\bar v|^2=0\). Integration and a compatible simultaneous unitary frame change therefore give

\[
\boxed{f_m(z)=\kappa(\bar z_2)^m e_1,\qquad m\ge2.}
\tag{65.5}
\]

This is a necessary classification of the first nonzero torsion polynomial. It is not a formal-jet or analytic-germ existence theorem and does not determine the actual zero set once higher Taylor terms are included.

## 4. What the Step-64 ten quadrics are [E+N]

For \(m=2\), write \(h=\delta\cdot\bar z\), \(g=Q(\bar z,\bar z)\), and \(P_a=Q^1_{a2}-Q^2_{a1}\). The ten real coefficients of the quadratic polynomial (65.2) are exactly the ten level-6 conditions seen numerically in Step 64. Their spatial trace is

\[
-8\left(\|Q\|^2-|P|^2+\frac{15}{4}|\delta|^2\right),
\]

so the Step-64 trace relation is correct:

\[
\boxed{\|Q\|^2-|P|^2=-\frac{15}{4}|\delta|^2.}
\tag{65.6}
\]

`step65_homogeneous_identity_exact.py` reconstructs the ten coefficient forms over the rationals, proves their matrix rank is exactly ten, proves the surface-restricted rank is exactly three, and verifies symbolically that the spatial trace is exactly \(-8(\|Q\|^2-|P|^2+15|\delta|^2/4)\). Under the surface conditions it becomes the negative sum

\[
-8\bigl(|Q^1_{12}|^2+|Q^2_{22}|^2+15|\delta_2|^2/4\bigr),
\]

which forces those three complex coefficients to vanish and leaves only \(Q^1_{22}\), giving \(f_2=\kappa\bar z_2^2e_1\). The exact output is `data/step65/homogeneous_identity_m2_exact.json`.

The independent floating script `spirit_step64_homogeneous_quadric_check.py` compares those predicted coefficient forms against the rounded lambda=-1 jet matrices: all ten principal-angle cosines equal one to displayed precision and the largest relative projection error is \(6.24\times10^{-9}\). This explains the ten equations as directional coefficients of one scalar PDE, rather than ten unrelated mechanisms.

A new independent lambda-zero run (`level6_lam0.0_s1.json`) found the same dimensions and singular values: 168 admissible degree-three directions, rank-16 intrinsic second torsion map, 629-dimensional level-6 cokernel, ten independent quadrics and three after the surface restriction. Its intrinsic quadric span has all ten principal-angle cosines equal to one against both the predicted forms and the lambda=-1 span; the maximum predicted-to-numerical projection error is \(4.87\times10^{-9}\). Its invariant trace fit is

\[
|\delta|^2+\frac4{15}\|Q\|^2-\frac4{15}|P|^2
\]

with relative residual \(3.57\times10^{-12}\). This confirms numerically that the leading conditions are lambda-independent, as (65.1)–(65.2) predict.

## 5. Correction to the exceptional-surface interpretation [P]

On a smooth \(J\)-complex surface \(C\subset\{T=0\}\) with dense rank-two locus, Step 63 identifies

\[
b=W_3^+|_C\in\Gamma(K_J^{-2}|_C),
\qquad
\deg(K_J^{-2}|_C)=\frac{s\operatorname{Area}(C)}{4\pi}.
\]

For \(s<0\), isolated exceptional zeros of \(b\) must have total negative winding.

At a point where \(T=DT=0\), (65.5) says the lowest total-degree torsion term is purely normal. In particular the tangential linear term of \(b\) vanishes. The statement in Step 64 that this excludes winding \(\pm1\) was false and is withdrawn: \(z|z|^2\) and \(\bar z|z|^2\) have zero linear part and windings \(+1\) and \(-1\), respectively. Degeneracy, multiplicity, and winding must be kept separate.

The lowest torsion polynomial (65.5) also does not determine the later mixed normal-tangential coefficient that produces \(b|_C\). Higher terms of the schematic form \(\bar z_2 P(z_1,\bar z_1)e_1\) can carry either tangential complex type unless the full equations impose a further transport law.

## 6. Exact surface transport presently available [P]

At a rank-two point of \(C\), choose an adapted unitary frame with \(TC=\operatorname{span}(e_1,Je_1)\) and \(NC=\operatorname{span}(e_3,Je_3)\). The normal first derivative of torsion is a complex-antilinear rank-one map

\[
(\nabla_{\zeta e_3}a)^\sharp=\bar\zeta\,\beta e_1,
\]

and the AAD Ricci identities identify \(\beta\) pointwise and complex-linearly with \(b=W_3^+|_C\). Covariant differentiation must use the induced connection on

\[
K_J^{-2}|_C\cong(T^{1,0}C\otimes N^{1,0}C)^{\otimes2};
\]

normal connection and Gauss–Weingarten terms cannot be dropped.

Specializing the exact Einstein AAD Bianchi equation (Step 55, equation (3.6)) along \(C\), where \(q=dq=a=\eta=\nabla\Omega=0\), gives in the transverse component

\[
2(\delta W_3^+)_Z^{\prime\prime}+(\nabla_{JZ}\eta)^{\prime\prime}=0.
\tag{65.7}
\]

For normal \(Z\), this has the intrinsic Cauchy–Riemann-type form

\[
\boxed{(D^L_{e_1}-iD^L_{Je_1})b=\Xi,}
\tag{65.8}
\]

up to the chosen complex-orientation sign, where \(\Xi\) is the corresponding normal derivative of \(\eta\). Equation (65.8) is not yet a similarity-principle equation: no supplied identity shows \(\Xi=A b+B\bar b\) with coefficients bounded through \(b=0\). Dividing by \(b\) only on the rank-two locus gives no control of exceptional windings. The second fundamental form enters when ambient higher derivatives are restricted to \(C\), even though its off-diagonal connection terms cancel from the determinant-line connection itself.

A direct flat-frame polarization of (65.2) around the rank-two model \(f_1=\kappa\bar z_2e_1\) was performed in `step65_rank2_surface_linearization.py`. For the most general degree-two half-twistor term vanishing on \(\{z_2=0\}\), the degree-one coefficient equations reduce to two real equations killing only the component \(Q^2_{12}\). Once the already known cone-along-\(C\) condition \(Q^2_{12}=0\) is imposed, the polarization has rank zero. In particular, both the \(z_1\bar z_2e_1\) coefficient \(\delta_2\) and the \(\bar z_1\bar z_2e_1\) coefficient \(Q^1_{12}\)—the two complex types of tangential variation of the rank-two normal coefficient—remain unconstrained. Thus the scalar identity itself permits either tangential complex type and cannot supply the desired similarity principle, even at principal flat order. Curved connection and second-fundamental-form terms remain for the full AAD system, but another iteration of the scalar equation will not close (65.8).

Thus negative winding is not excluded. The precise missing object is a coupled normal transport system for \((b,\nabla_N\eta,\ldots)\), or a divisibility relation controlling \(\Xi\) at zeros of \(b\). That is the compact-assembly problem created by the negative canonical degree.

## 7. Mathematical consequences and next direction

1. Every finite-order torsion zero of order \(m\ge2\) has the GH-type first nonzero polynomial (65.5), independently of the sign of scalar curvature. This replaces further blind increases of total jet degree for the leading-term question.
2. The ten Step-64 quadrics contain no new lambda-sensitive obstruction; they are the ten coefficients of (65.2), confirmed at lambda=-1 and lambda=0.
3. The compact negative-scalar issue is not the existence of a normal leading term but the tangential transport of its coefficient along a putative zero surface. The global degree forces negative total winding, while the exact local equation still contains the independent source \(\nabla_N\eta\).
4. No conclusion about a closed Goldberg counterexample or integrability follows. Isolated nondegenerate positive-index zeros also remain a separate viable local geometry; (65.5) concerns only zeros of order at least two.
5. The next useful derivation should differentiate the coupled AAD Ricci/Bianchi system in an adapted tubular frame along \(C\), retain the normal connection and second fundamental form, and seek a closed first-order system for \((b,\nabla_N\eta)\). If the source is divisible by \(b\) with bounded coefficients, a similarity principle becomes available; after fixing the induced complex orientation, its local sign must be compared with the negative degree. If the allowed principal operator instead produces the required negative winding, it identifies the necessary local geometry of any closed counterexample.
