# Einstein repair with an integrable kernel: a sharp cyclic-cover theorem

24 September 2026. The positive-coercivity hypothesis in the
[uniformly local repair theorem](20260924_uniformly_local_repair.md)
excludes products of hyperbolic surfaces. Here all their genuine
Teichmüller parameters are retained. On a specified cyclic-cover family
we prove a complete nonlinear repair theorem with the correct quadratic
loss, and actual near-Einstein metrics showing that loss cannot be
replaced by a uniform constant. The reduced equation is proved to vanish;
its solvability is not an assumption.

## 1. Objects, norms and statements

Fix closed oriented hyperbolic surfaces \((B,b)\), \((F,f)\), of curvature
\(-1\), and a primitive epimorphism \(\pi_1(B)\to\mathbb Z\).
Let \((B_m,b_m)\) be the degree-\(m\) cyclic cover. Put
\[
 M_m=B_m\times F,\qquad h_m=b_m+f,\qquad
 \operatorname{Ric}_{h_m}=-h_m.
\]
All constants below depend on these fixed surfaces, the cyclic cover and
\(0<\alpha<1\), but not on \(m\). Use the uniform lifted product atlas
to define \(X_m=C^{3,\alpha}_{\rm uloc}\) and
\(Y_m=C^{1,\alpha}_{\rm uloc}\). These are supremum norms, not sums
over charts. The choice of one extra derivative makes the global factor
projections and gauge estimates explicit.

For a metric \(g\), let
\[
 W_m(g)^k=g^{ij}\bigl(\Gamma(g)^k_{ij}-\Gamma(h_m)^k_{ij}\bigr),
 \quad
 \Phi_m(g)=\operatorname{Ric}_g+g-\tfrac12\mathcal L_{W_m(g)}g.
                                                               \tag{1}
\]
The condition \(W_m(g)=0\) says that the identity map to \((M_m,h_m)\)
is harmonic. At \(h_m\),
\[
 D\Phi_m=L_m=\tfrac12\Delta_{L,h_m}+I
            =\tfrac12\nabla^*\nabla-\mathring R.
\]
Write \(T_\Sigma\) for the transverse-traceless tensors on a hyperbolic
surface, and set
\[
 K_m=T_{B_m}\oplus T_F=\ker L_m,
 \qquad \Pi_m=\text{the }L^2(h_m)\text{-projection onto }K_m.
                                                               \tag{2}
\]
Every vector in \(K_m\) is an actual infinitesimal factor deformation;
its dimension grows with \(m\). None is discarded.

**Theorem A (quantified repair to the full Einstein moduli).** There are
\(c,C,r_0>0\) and smooth families
\[
 H_m(k)=h_m+k+R_m(k),\qquad k\in K_m,\quad \|k\|_{X_m}<r_0,
                                                               \tag{3}
\]
of exact product Einstein metrics in harmonic gauge, with
\(\Pi_mR_m(k)=0\) and
\[
 \|R_m(k)\|_{X_m}\le C\|k\|_{X_m}^2,\qquad
 \|DR_m(k)\|\le C\|k\|_{X_m}.
                                                               \tag{4}
\]
If \(W_m(g)=0\) and \(\|g-h_m\|_{X_m}<c m^{-2}\), then
\[
 \boxed{\quad
 \|g-H_m(\Pi_m(g-h_m))\|_{X_m}
       \le C m^2\|\operatorname{Ric}_g+g\|_{Y_m}.
 \quad}                                                       \tag{5}
\]
In particular every exact Einstein metric in this harmonic-gauge
neighborhood belongs to (3). The assertion permits every tensor sector
in the input metric, not only product or fiber-preserving perturbations.

**Theorem B (the loss is realized nonlinearly).** There are smooth
metrics \(g_m\), uniformly noncollapsed with uniformly bounded
curvature derivatives of every fixed order, such that
\[
 \|g_m-h_m\|_{X_m}\le C m^{-2},\qquad
 \|\operatorname{Ric}_{g_m}+g_m\|_{Y_m}\le C m^{-4},
                                                               \tag{6}
\]
but, writing \(\mathscr E(M_m)=\{h:\operatorname{Ric}_h=-h\}\),
\[
 \boxed{\quad
 \inf_{h\in\mathscr E(M_m)}\|h-g_m\|_{X_m}\ge c m^{-2}.
 \quad}                                                       \tag{7}
\]
The infimum includes all normalized Einstein metrics and their
diffeomorphic pullbacks, not just the displayed product family. Thus a
uniform residual-to-distance estimate with exponent \(\theta>1/2\)
is false on this family, even though all exact kernel directions are
integrable. No optimality of the exponent \(1/2\) is asserted.

These manifolds already admit \(h_m\). Theorem B is a limitation of
uniform perturbative repair, not an Einstein-nonexistence result or a
counterexample to Yau26.

## 2. The scalar inverse costs exactly \(m^2\)

Let \(\Delta\ge0\). We first prove
\[
 \|\Delta_{B_m}^{-1}v\|_{C^0}\le C m^2\|v\|_{C^0},
 \qquad \int_{B_m}v=0,
                                                               \tag{8}
\]
with the inverse chosen to have mean zero. Cut the fixed base along a
nonseparating curve dual to the epimorphism, and use bounded overlapping
enlargements of its lifted cells. Adjacent cells and these enlargements
have uniform Poincaré constants and bounded overlap. For a solution
\(\Delta u=v\), differences of consecutive cell means are bounded by
the local \(L^2\) gradient. Local elliptic estimates, after subtracting
a cell mean, give
\[
 \sup_{\text{cell }j}|u-u_j|
 \le C\bigl(\|\nabla u\|_{L^2(\text{enlarged cell }j)}
                  +\|v\|_\infty\bigr).
\]
To justify this estimate, cover the cell by a fixed chain of interior
balls, apply the inhomogeneous local \(L^2\)-to-\(C^0\) estimate on
each ball, and use Poincaré on the enlargement. No estimate at an
artificial cut boundary is used.

Summing along at most \(m\) cells and applying Cauchy--Schwarz yields
\[
 O:=\operatorname{osc}u\le C\sqrt m\|\nabla u\|_2+C\|v\|_\infty.
\]
Since \(\operatorname{Vol}B_m=m\operatorname{Vol}B\), integration by
parts, with any constant subtracted from \(u\), gives
\[
 \|\nabla u\|_2^2=\int uv\le C m\|v\|_\infty O.
\]
Substitution and Young's inequality prove (8). Uniform local Schauder
estimates then give its \(C^{j,\alpha}\)-to-\(C^{j+2,\alpha}\)
version, with the same \(m^2\) loss.

For sharpness choose the harmonic one-form \(\eta\) in the primitive
integral class. Its lift to the infinite cyclic cover is \(dz\), with
\(z(\tau x)=z(x)+1\) and \(\Delta z=0\). For \(m\ge2\),
\[
 v_m=\cos(2\pi z/m)
\]
is a smooth function on \(B_m\). Summing over the deck orbit proves
\(\int v_m=0\), while \(\|v_m\|_\infty=1\). The chain rule gives
\[
 \Delta v_m=\frac{4\pi^2}{m^2}|\eta|^2v_m,
 \qquad \|\Delta v_m\|_{C^{j,\alpha}_{\rm uloc}}\le C_jm^{-2}.
                                                               \tag{9}
\]
All local derivatives of \(v_m\) are uniformly bounded. Thus the
order in (8) is attained on an actual harmonic-circle construction,
not merely inferred from a discrete graph model.

## 3. Uniform projections and the full transverse inverse

The classical product decomposition gives two slow channels
\[
 T_{B_m}\widehat\otimes L^2(F),\qquad
 L^2(B_m)\widehat\otimes T_F,
\]
on which \(L_m\) is respectively \(\tfrac12\Delta_F\) and
\(\tfrac12\Delta_{B_m}\). The remaining trace, conformal-Killing and
mixed sectors have positive shifts. These are the complete sectors,
as in [Kröncke, Proposition 4.1 and Lemma 4.2](https://arxiv.org/html/1508.00721)
and [the project's surface calculation](../mathematics/current/round17_product_operator.md),
rescaled from curvature \(-3\) to \(-1\). In Kröncke's notation the
Einstein operator \(\Delta_E=\nabla^*\nabla-2\mathring R\) is
\(2L_m\), not \(L_m\). In our nonnegative Hodge convention,
\(\Delta_H=\nabla^*\nabla-1\) on surface one-forms. Thus the exact
intertwining needed below is
\[
 L_{B_m\times F}(D_Bz)
       =D_B\bigl(\tfrac12\Delta_{H,B}+1+\tfrac12\Delta_F\bigr)z
       =D_B(A_B+\tfrac12\Delta_F)z.
\]
This also follows directly from the surface identities
\(L_B=D_B\delta_B\) on trace-free tensors and
\(\delta_BD_B=A_B\). The accompanying coordinate check verifies
both identities for arbitrary one-form coefficients in the
curvature-\(-1\) half-plane metric; no Hodge sign is inferred from a
change of notation in the cited source.

We need Hölder, not just Hilbert-space, control of these projectors.
For a hyperbolic surface let
\[
 D\xi=\delta^*\xi+\tfrac12(\delta\xi)b,
 \qquad A=\delta D=\tfrac12\nabla^*\nabla+\tfrac12.
\]
For a trace-free tensor \(s\), its TT projection is
\(P_Ts=s-D A^{-1}\delta s\). This formula has uniform bounds on
the present surfaces, including as an operator from \(C^0\) to
local \(C^{j,\alpha}\) for every fixed \(j\).

Here is a proof which does not assume a bound for a large-rank projection.
Put \(w=A^{-1}\delta s\). The cyclic surfaces have
\(\operatorname{Vol}B_R(x)\le C(1+R)\), by counting translates of a
fixed cell in the infinite cyclic cover. Test \(Aw=\delta s\) with
\(\phi_x^2w\), where \(\phi_x=e^{-a\operatorname{dist}(x,\cdot)}\)
and \(a>0\) is fixed and sufficiently small. Integrate the divergence
on the right onto \(\phi_x^2w\). The positive potential \(1/2\),
Young's inequality and \(|d\phi_x|\le a\phi_x\) give
\[
 \int\phi_x^2(|\nabla w|^2+|w|^2)
       \le C\int\phi_x^2|s|^2\le C\|s\|_\infty^2.        \tag{10}
\]
The last constant follows from the linear ball-growth bound. Thus
\(P_Ts=s-Dw\) has uniformly bounded local \(L^2\) norm. It is TT;
the first-order operator \(\delta:S^2_0\to T^*\Sigma\) is elliptic
in dimension two. Local homogeneous elliptic estimates therefore
bound every derivative of \(P_Ts\) by this local \(L^2\) norm.
This proves the claim, first for smooth \(s\), and then by density for
the stated bounds. The fixed surface \(F\) has the same property.

The estimates persist with a parameter in the other factor: the
projections commute with those derivatives, and their \(C^0\)-to-local-
derivative bounds apply to parameter differences. Hence the factor
projections, their product-sector extensions and \(\Pi_m\) are bounded
on \(X_m,Y_m\), uniformly in \(m\). For \(\Pi_m\), one additionally
averages over the other factor; normalized averaging has norm at most
one. This explains why a growing kernel dimension causes no projection
constant here.

We claim that
\[
 \boxed{\quad
 \|u\|_{X_m}\le C m^2\|L_mu\|_{Y_m},\qquad \Pi_mu=0.
 \quad}                                                       \tag{11}
\]
For the two slow channels, remove their true constant coefficient
modes only, and apply (8) or the fixed scalar Green operator on \(F\).
This gives the required \(C^0\) bound. For traces, the operator is
\(1+\tfrac12(\Delta_{B_m}+\Delta_F)\), so the maximum principle
gives a uniform bound.

On a conformal-Killing sector write the source as \(D_Bw\), where
\(w=A_B^{-1}\delta_Bs\). Its \(C^{0,\alpha}\) norm on the product is
bounded by \(C\|s\|_{Y_m}\), using the positive-potential inverse
and the preceding parameter estimates. Solve
\[
 (A_B+\tfrac12\Delta_F)z=w,
 \qquad u=D_Bz.
\]
This connection operator has potential \(1/2\); the maximum principle
and local Schauder estimates bound \(u\) in \(C^0\) uniformly.
The other conformal-Killing sector is identical with the factors
interchanged. This retains its response rather than setting it to zero.

On the mixed bundle,
\[
 L_m=\tfrac12\nabla^*\nabla,
 \qquad \langle L_mu,u\rangle_{L^2}\ge\|u\|_2^2,
\]
because each factor's rough one-form Laplacian is \(\Delta_H+1\).
Multiplication by a scalar preserves this entire bundle. The weighted
identity in the preceding repair theorem thus applies with gap one
and linear volume growth, giving a uniform local \(L^2\) bound and
then a \(C^0\) bound. We do not apply weighted coercivity to the
nonlocal kernel-orthogonal subspace: multiplication need not preserve
that subspace.

Finally, the full local elliptic estimate
\[
 \|u\|_{X_m}\le C(\|L_mu\|_{Y_m}+\|u\|_\infty)
\]
proves (11) after summing the finitely many sector types. Fredholm
theory gives surjectivity onto \(K_m^\perp\cap Y_m\). Applying (9)
to \(u=v_mq\), for any fixed nonzero \(q\in T_F\), shows that the
operator norm in (11) is at least \(c m^2\). These tensors are TT
and orthogonal to the **entire** kernel (2).

## 4. Integration of the whole kernel, uniformly in the cover

We give the uniform version of the fixed-geometry argument in
[Round 18, §7](../mathematics/current/round18_twisted_operator.md).
For \(q\in T_{B_m}\) small in the uniform norm, the metric \(b_m+q\)
is positive definite and
\(K(b_m+q)+1=O(\|q\|^2)\), because the curvature variation of a TT
tensor is zero. Solve
\[
 \Delta_{b_m+q}u+e^{2u}+K(b_m+q)=0.                         \tag{12}
\]
Its derivative at zero is \(\Delta_{b_m}+2\). The maximum principle
and uniform local Schauder estimates give a uniform inverse; the
nonlinear contraction therefore gives \(u=O(\|q\|^2)\) on a
uniform ball. Thus \(e^{2u}(b_m+q)\) has curvature \(-1\) and
derivative \(q\). TT elliptic estimates control all higher local
derivatives of \(q\) by its uniform norm, so this construction and
its first two parameter derivatives have uniform bounds. The same
construction applies on \(F\).

Place each hyperbolic family in harmonic-map gauge relative to its
reference surface. The Jacobi operator at the identity is
\(\nabla^*\nabla+1\). Its pointwise positive potential, the maximum
principle and local Schauder theory give uniform inverse bounds.
The implicit-function argument for maps to the fixed reference metric
therefore has a uniform radius. Its first variation is zero along TT
directions. Pushing the family forward by this small harmonic
diffeomorphism preserves curvature and changes it only quadratically.
Taking products gives actual Einstein metrics in the gauge (1).

Their kernel projection is \(q+O(q^2)\), with uniformly bounded
derivative. The inverse function theorem on \(K_m\), using its
uniform norm rather than coordinatewise parameter bounds, reparametrizes
the family to give (3)--(4). Constants do not depend on its dimension.

Let \(Q_m=I-\Pi_m\). The usual complementary equation is
\[
 Q_m\Phi_m(h_m+k+w)=0,\qquad w\in K_m^\perp.
\]
By (11) and the uniform quadratic Hölder estimate, it has a unique
small solution in the radius \(c m^{-2}\) under consideration.
The actual family already constructed is this graph:
\(w=R_m(k)\). Its remaining equation is therefore
\[
 \boxed{\ \Pi_m\Phi_m(h_m+k+R_m(k))=0\ }
\]
identically. This proves compatibility of every reduced equation;
it is stronger than omitting them or assuming integrability of only
selected tangent vectors.

To prove (5), take \(k=\Pi_m(g-h_m)\),
\(z=g-H_m(k)\in K_m^\perp\), and expand (1). The quadratic remainder
\(N_m\) satisfies a uniform Lipschitz bound
\[
 \|N_m(a)-N_m(b)\|_{Y_m}
 \le C(\|a\|_{X_m}+\|b\|_{X_m})\|a-b\|_{X_m}.
\]
Since \(\Phi_m(H_m(k))=0\), (11) gives
\[
 \|z\|_{X_m}\le C m^2\bigl(\|Q_m\Phi_m(g)\|_{Y_m}
                                +Ccm^{-2}\|z\|_{X_m}\bigr).
\]
Choose \(c\) small enough to absorb the last term. In harmonic gauge
\(\Phi_m(g)=\operatorname{Ric}_g+g\), proving Theorem A. The same
argument classifies every nearby gauged zero, not merely the solutions
obtained by a chosen iteration.

## 5. Actual small residuals separated from all Einstein outputs

Fix a nonzero \(q\in T_F\), let \(u_m=v_mq\) from (9), and first put
\(\widetilde g_m(t)=h_m+t u_m\). The tensors \(u_m\) have uniformly
bounded local derivatives of every fixed order, are TT, and satisfy
\[
 \Pi_mu_m=0,\quad \|u_m\|_{X_m}\ge c_0>0,
 \quad \|L_mu_m\|_{Y_m}\le C m^{-2}.
\]
Consequently
\[
 \|\operatorname{Ric}_{\widetilde g_m(t)}+\widetilde g_m(t)\|_{Y_m}
                         \le C(t m^{-2}+t^2).              \tag{13}
\]
This is the Taylor expansion of the actual Ricci tensor, not just a
linearized forcing. Because \(DW_m|_{h_m}(u_m)=0\), the harmonic-map
gauge adjustment described above is \(O(t^2)\), with bounds in every
fixed derivative norm. Denote the adjusted metric by \(g_m(t)\). Then
\[
 W_m(g_m(t))=0,\qquad
 g_m(t)=h_m+t u_m+O_{X_m}(t^2),                              \tag{14}
\]
and (13) still holds. Choose once and for all a sufficiently small
\(\theta_0>0\), and set \(t=t_m=\theta_0m^{-2}\).
These metrics lie in Theorem A's neighborhood and satisfy (6).

For any family member \(H_m(k)\) at distance \(O(t_m)\) from
\(g_m(t_m)\), the bounded projection and (14) imply
\(\|k\|_{X_m}\le C t_m\). Equations (3)--(4) then give
\[
 Q_m(g_m(t_m)-H_m(k))=t_m u_m+O_{X_m}(t_m^2).
\]
Thus its norm is at least \(c t_m\); boundedness of \(Q_m\) gives
the same lower bound for the metric distance. Members farther away
already obey that bound. By Theorem A this treats every gauged
Einstein metric within its neighborhood.

For clarity, an arbitrary nearby Einstein output cannot evade this
argument by a small change of gauge. If \(h\) is close to \(g_m(t_m)\)
in \(X_m\), solve the harmonic map equation from \((M_m,h)\) to
\((M_m,h_m)\) near the identity. At \(h_m\) its Jacobi operator on
vector fields is \(\nabla^*\nabla+1\), so the inverse is uniform;
small coefficient perturbations preserve that bound. Since the
identity is already harmonic for \(g_m(t_m)\), the solution \(F\) satisfies
\[
 \|F-\operatorname{id}\|_{C^{4,\alpha}_{\rm uloc}}
                       \le C\|h-g_m(t_m)\|_{X_m}.
\]
It is a diffeomorphism. Its pushforward \(\bar h=(F^{-1})^*h\) is
Einstein and in the gauge (1). The metrics \(g_m(t_m)\) have uniformly
bounded \(C^{4,\alpha}\) norms, so writing
\[
 \bar h-g_m=(F^{-1})^*(h-g_m)
                       +\bigl((F^{-1})^*g_m-g_m\bigr)
\]
gives \(\|\bar h-g_m\|_{X_m}\le C\|h-g_m\|_{X_m}\), with no
derivative loss in this comparison. Taking \(\theta_0\) smaller if
necessary puts \(\bar h\) inside the classified neighborhood whenever
the proposed distance is less than a fixed small multiple of \(t_m\).
The gauged lower bound contradicts such a distance. Outputs outside
that small ball trivially satisfy (7). This proves Theorem B.

Combining (6)--(7), for every \(\theta>1/2\),
\[
 \frac{\operatorname{dist}_{X_m}(g_m,\mathscr E(M_m))}
      {\|\operatorname{Ric}_{g_m}+g_m\|_{Y_m}^{\theta}}
                       \longrightarrow\infty.
\]
In particular the \(m^2\) loss in the linear residual estimate (5)
has matching nonlinear examples.

## 6. Mathematical position

The product spectrum and the integration of surface Teichmüller
directions are classical; see Kröncke above and
[Rupflin--Topping on horizontal hyperbolic metrics](https://link.springer.com/article/10.1007/s00526-018-1386-y).
Round 18 already proved local completeness at each fixed finite-monodromy
geometry. The increment here is the **uniformly quantified cyclic
regime**: a sharp Hölder-space transverse inverse, an explicit nonlinear
radius, all reduced equations solved by the actual full moduli, and a
nonlinear obstruction to volume-independent strong repair estimates.

There is no contradiction with the preceding positive-coercivity theorem.
This family has exact kernels and scalar slow channels, although its
local geometry is uniformly bounded and its ball growth is only linear.
Nor does this exclude a different existence proof, a weaker repair
modulus, or a theorem retaining additional global control of the slow
coefficients. It identifies a real geometric quantity that such a theorem
must handle; it does not identify another absent gauge zero mode.

`check_integrable_kernel_cyclic_repair.py` checks the curvature-\(-1\)
surface differential identities, the harmonic-circle chain rule,
deck-orbit cancellation and the nonlinear scaling. It also checks the
negative control that localization need not preserve kernel
orthogonality. These finite calculations do not verify the cellwise
elliptic estimates, uniform moduli integration or nonlinear existence
argument.
