# Full-collar pure shear, exact scalar calibration, and the conformal boundary of Einstein repair

## 1. The fixed closed manifold and the result

This note uses the nonzero integer-shear self-gluing of Round 11 with
identity fiber mapping class. Fix \(h\geq1\), \(g\geq2\), a surface
\(B=F_{h,2}\), a closed surface \(F=\Sigma_g\), and a circle-valued map
\(u:F\to\mathbb R/2\pi\mathbb Z\) representing a nonzero integral class.
Glue the two boundary components of \(B\times F\) by
\[
 (\phi,x)\longmapsto(-\phi+u(x),x).
\]
The resulting closed smooth four-manifold \(M\) is fixed throughout.
It has \(\tau(M)=0\), \(\chi(M)=4h(g-1)>0\). The Round-11 construction,
topological argument and variational computation apply to this pure-shear
case. In particular,
\[
 V_*=\frac{4\pi^2\chi(M)}9,\qquad
 \sigma(M)=-12\sqrt{V_*}=-8\pi\sqrt{\chi(M)}.
 \tag{1}
\]
The new construction below uses almost the full hyperbolic collar.
Its conclusions are
\[
 \begin{split}
 \operatorname{Vol}(g_\ell)&=V_*,
 &\|\operatorname{Ric}_{g_\ell}+3g_\ell\|_{C^j(g_\ell)}
     &\leq C_j\ell^2,\\
 s_{\widehat g_\ell}&=-12,
 &\|\operatorname{Ric}_{\widehat g_\ell}+3\widehat g_\ell
                   \|_{C^j(\widehat g_\ell)}&\leq C_j\ell^2,\\
 \operatorname{Vol}(\widehat g_\ell)
   &=V_*+\frac{\sqrt3\,\|\beta\|_2^2}{24\pi^3}\ell^3
       +O(\ell^5),&
 \int_M|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2
       &\leq C\ell^5.
 \end{split}                                                     \tag{2}
\]
Here \(\beta=-du\) is chosen harmonic for the fixed curvature-\(-3\)
fiber metric. All tensor norms are relative to the displayed metric,
and \(j\) is any fixed nonnegative integer. Every conformal class
\([g_\ell]=[\widehat g_\ell]\) contains no Einstein metric of any sign.
This is a statement about these conformal classes, not about all metrics
on \(M\).

The smooth topology and the underlying near-Einstein existence result
are inherited from Round 11. The additions are the full-collar profile,
its improved pointwise and integral scales, exact scalar calibration,
and the explicit cubic volume and Yamabe deficits.

## 2. The full-collar connection profile

Set \(k=\sqrt3\), \(c=\ell/(2\pi)\), and take a curvature-\(-3\)
metric on \(B\) with both boundary lengths \(\ell\). After gluing its
two half collars, the circle radius on the resulting neck is
\[
 a(t)=c\cosh(kt),\qquad
 |t|<w_\ell,\qquad
 w_\ell=k^{-1}\operatorname{arsinh}
                      \frac1{\sinh(k\ell/2)}.
 \tag{3}
\]
In particular \(w_\ell=k^{-1}|\log\ell|+O(1)\).
Choose a sufficiently large fixed \(C_0>4\), put
\(R_\ell=w_\ell-C_0\), and choose even smooth \(\eta_\ell\) with
\[
 \eta_\ell=1\quad(|t|\leq R_\ell-1),\qquad
 \eta_\ell=0\quad(|t|\geq R_\ell),\qquad
 0\leq\eta_\ell\leq1.
\]
All derivatives of each fixed order are bounded independently of \(\ell\);
one may translate a single fixed cutoff on each end. Define
\[
 I_\ell=\int_{\mathbb R}\eta_\ell(t)\operatorname{sech}^3(kt)\,dt,
 \qquad
 z_\ell'(t)=I_\ell^{-1}\eta_\ell(t)\operatorname{sech}^3(kt),
 \qquad z_\ell(-\infty)=0.
 \tag{4}
\]
Then \(z_\ell=0\) at the left end and \(z_\ell=1\) at the right end,
with all derivatives zero near the gluing interfaces. Moreover
\[
 I_\ell=\frac{\pi}{2k}+O(\ell^3),\qquad
 e^{-kR_\ell}\asymp\ell.
 \tag{5}
\]
On the collar take
\[
 g_\ell=dt^2+a(t)^2(d\phi+z_\ell(t)\beta)^2+h_F,
 \tag{6}
\]
and use the exact product metric elsewhere. Since both end connections
are flat with the prescribed integral difference, (6) has precisely
the original marked gluing. Replacing the original \(du\) by its harmonic
representative changes \(u\) by a globally defined real-valued function
and hence by an isotopy of the boundary shear. It changes no smooth type.

For the orthonormal splitting \(T=\partial_t\),
\(U=a^{-1}\partial_\phi\), \(TF\), set \(E=\operatorname{Ric}+3g_\ell\).
The full Ricci formulas are
\[
 \begin{split}
 E_{TT}&=-Q,& E_{UU}&=Q,&
 E_{XY}&=-\frac12a^2(z_\ell')^2\beta(X)\beta(Y),\\
 E_{XU}&=-\frac a2\{z_\ell''+3(a'/a)z_\ell'\}\beta(X),&
 E_{TU}&=E_{TX}=0,&
 Q&=\frac12a^2(z_\ell')^2|\beta|^2.
 \end{split}                                                     \tag{7}
\]
The last vanishing uses that \(\beta\) is closed and coclosed. Thus
\[
 s_{g_\ell}=-12-Q.                                               \tag{8}
\]
In the core, \((a^3z_\ell')'=0\): the mixed Ricci equation is solved
exactly. On the two cutoff strips \(a\asymp1\), while \(z_\ell'\)
and each of its derivatives are \(O(\ell^3)\). Consequently the mixed
error there is \(O(\ell^3)\), and the diagonal error is \(O(\ell^6)\).
In the core,
\[
 Q=\frac{c^2}{2I_\ell^2}\operatorname{sech}^4(kt)|\beta|^2,
 \tag{9}
\]
so the full error is \(O(\ell^2)\), with the same estimate for all
fixed covariant derivatives. Curvature and its fixed derivatives
remain uniformly bounded. The local coefficient verification is
described in §5.

The full-collar choice is available because the mapping class is the
identity. No region is reserved for changing the fiber metric. This
does not improve a general mapping-class construction without checking
the separate transition region.

The profile is also the fixed-background connection-energy minimizer:
\[
 \left(\int z'\,dt\right)^2
 \leq\left(\int a^3z'^2\,dt\right)
        \left(\int a^{-3}\,dt\right),
 \tag{10}
\]
with equality when \(z'\) is proportional to \(a^{-3}\).
The cutoff incurs only the stated end errors. The more general
connection-capacity and fiber-shape calculations are in
[round14_shear.md](round14_shear.md).

## 3. Scalar loss and the fifth-order tracefree energy

The volume form \(a\,dt\,d\phi\,d\mu_F\) does not depend on \(z_\ell\).
Gauss--Bonnet for the two curvature-\(-3\) surface factors therefore gives
the exact first identity in (2). Write
\(B_\beta=\int_F|\beta|^2\,d\mu_F>0\). The total scalar loss is
\[
 \begin{split}
 \mathcal R_\ell:=\int_MQ\,d\mu
 &=\pi c^3B_\beta I_\ell^{-2}
       \int_{\mathbb R}\eta_\ell^2\operatorname{sech}^3(kt)\,dt\\
 &=2kc^3B_\beta+O(\ell^6)
  =\frac{kB_\beta}{4\pi^3}\ell^3+O(\ell^6).
 \end{split}                                                     \tag{11}
\]
The error follows because each omitted tail has size \(O(\ell^3)\);
the prefactor is \(O(\ell^3)\). Also
\[
 \|Q\|_\infty=O(\ell^2),\qquad \|Q\|_2=O(\ell^{5/2}).
 \tag{12}
\]

Away from zeros of \(\beta\), diagonalize in the \(\beta\)-direction.
On the core the eigenvalues of \(E\) are \((-Q,Q,-Q,0)\).
Those of \(E^\circ\) are
\((-3Q/4,5Q/4,-3Q/4,Q/4)\), whence
\[
 |E^\circ|^2=\frac{11}{4}Q^2.
 \tag{13}
\]
The formula extends over the zeros. Since
\(\int_{\mathbb R}\operatorname{sech}^7(kt)\,dt=5\pi/(16k)\),
and the cutoff mixed error has squared integral \(O(\ell^6)\),
\[
 \boxed{
 \int_M|\operatorname{Ric}_{g_\ell}^{\circ}|^2\,d\mu
 =\frac{55k^3}{256\pi^7}
      \left(\int_F|\beta|^4\,d\mu_F\right)\ell^5+O(\ell^6).}
 \tag{14}
\]
This coefficient concerns the original shear metric. Conformal scalar
repair changes the tracefree Ricci tensor at the same \(L^2\) order,
so (14) is not asserted with the same coefficient for the repaired metric.

## 4. Exact scalar calibration

There is a unique positive smooth \(v_\ell\) such that
\(\widehat g_\ell=v_\ell^2g_\ell\) has scalar curvature \(-12\).
With \(\Delta=\operatorname{div}\nabla\), the equation is
\[
 -6\Delta v-(12+Q)v=-12v^3.                                    \tag{15}
\]
For existence, \(1\) is a subsolution and
\[
 U=\sqrt{1+\|Q\|_\infty/12}
\]
is a supersolution. Monotone iteration for a shifted operator
\(-6\Delta+C\), with fixed \(C\) large enough on \(1\leq v\leq U\leq2\),
gives a solution between them on each closed \(M\).
For uniqueness, if \(v_1,v_2\) solve (15), the ratio \(v_1/v_2\)
satisfies the same constant-negative-scalar conformal equation relative
to \(v_2^2g_\ell\). Its maximum is at most one and its minimum at least one.

Set \(w=v-1\). Then
\[
 0<w\leq C\ell^2,\qquad
 -6\Delta w+24w=Q(1+w)-36w^2-12w^3.                           \tag{16}
\]
The strict inequality follows from the strong maximum principle and
\(Q\not\equiv0\). The uniform higher derivative estimate is justified
in §5; it does not require an injectivity-radius lower bound.

Integrating (16) gives
\[
 24\int w=\int Q+\int Qw-36\int w^2-12\int w^3.              \tag{17}
\]
Combine this with the exact volume expansion
\(\int\{(1+w)^4-1\}=4\int w+6\int w^2+4\int w^3+\int w^4\).
The quadratic term cancels:
\[
 \boxed{
 \operatorname{Vol}(\widehat g_\ell)-V_*
 =\frac16\int Q+\frac16\int Qw+2\int w^3+\int w^4.}
 \tag{18}
\]
Every term on the right is nonnegative. From (17),
\(\int w\leq C\int Q=O(\ell^3)\), so
\(\int Qw=O(\ell^5)\), \(\int w^3=O(\ell^7)\) and
\(\int w^4=O(\ell^9)\). Equations (11) and (18) prove
\[
 \boxed{
 \operatorname{Vol}(\widehat g_\ell)
 =V_*+\frac{kB_\beta}{24\pi^3}\ell^3+O(\ell^5)>V_*.}
 \tag{19}
\]

For a constant-negative-scalar metric, the conformal Yamabe quotient
is bounded below by its value at constants, directly by Hölder's
inequality and nonnegativity of the Dirichlet integral. Thus
\[
 Y([g_\ell])=-12\sqrt{\operatorname{Vol}(\widehat g_\ell)}
 \quad\text{and}\quad
 \boxed{
 \sigma(M)-Y([g_\ell])
 =\frac{kB_\beta}{4\pi^3\sqrt{V_*}}\ell^3+O(\ell^5).}
 \tag{20}
\]
This identifies the leading strict deficit in these conformal classes;
it does not establish any positive uniform Yamabe deficit over all classes.

## 5. Uniform estimates through the collapsing collar

Here the use of local covers can be verified in the explicit coordinates,
without a general compactness theorem. Outside the neck, use local
hyperbolic product covers of fixed radius. In the neck unwrap the circle,
and at a point \(t_0\) rescale its local coordinate by \(a(t_0)\).
On a fixed-radius \(t\)-interval, \(a(t)/a(t_0)\) and all its fixed
derivatives are uniformly bounded above and below. On a fiber chart
write \(\beta=db\) and replace the unwrapped circle coordinate by
\(\phi+z(t)b\). The connection then becomes
\[
 d\phi+z\beta=d(\phi+zb)-z'b\,dt.
\]
The remaining normalized off-diagonal coefficients are bounded by
\(a(t_0)z'\), with uniformly bounded derivatives. In the central region
this is \(O(\ell)\); near the cutoff it is \(O(\ell^3)\). These
coordinates give uniformly elliptic metrics on fixed balls with
uniform bounds of every fixed order. They cover every point, whether
or not the quotient circle is short.

Lift the actual global scalar solution to these charts; no circle
invariance of the solution is assumed. The \(C^0\) estimate (16),
local \(W^{2,p}\) estimates with any fixed \(p>4\), and then Schauder
estimates and differentiation of (16) give
\[
 \|w\|_{C^j(g_\ell)}\leq C_j\ell^2
 \quad\text{for every fixed }j.
 \tag{21}
\]
The bootstrap starts from a bounded \(O(\ell^2)\) right-hand side;
the metric and \(Q\) have the fixed-order coefficient bounds just
described. Shrinking a chart by a fixed factor is harmless because
the construction provides the same-size larger chart at every point.

There is also a global estimate at the sharper integral scale.
Multiply (16) by \(w\geq0\), integrate, and discard the favorable
cubic and quartic terms. For sufficiently small \(\ell\),
\[
 \|w\|_2+\|\nabla w\|_2\leq C\|Q\|_2,\qquad
 \|\Delta w\|_2\leq C\|Q\|_2.
 \tag{22}
\]
Integrated Bochner and the uniform Ricci bound imply
\[
 \|\nabla^2w\|_2\leq C\|Q\|_2=O(\ell^{5/2}).                 \tag{23}
\]
No Sobolev constant appears. In dimension four the conformal formula is
\[
 \operatorname{Ric}^{\circ}_{v^2g}
 =\operatorname{Ric}^{\circ}_g
  -2v^{-1}(\nabla^2v)^\circ
  +4v^{-2}(dv\otimes dv)^\circ.                              \tag{24}
\]
The \(L^2\) norm of a fixed covariant two-tensor is conformally invariant
in dimension four. Equations (12)--(14), (21)--(24) prove the last
estimate in (2), and the conformal Ricci formula proves its pointwise
and fixed-derivative counterparts. Since \(s_{\widehat g_\ell}=-12\),
\[
 \operatorname{Ric}_{\widehat g_\ell}+3\widehat g_\ell
 \quad\text{is tracefree and divergence-free}.               \tag{25}
\]
For the complete four-index curvature norm, Chern--Gauss--Bonnet gives
\[
 \int_M|\operatorname{Rm}_{\widehat g_\ell}|^2
 =32\pi^2\chi(M)+4\int_M|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2
 =32\pi^2\chi(M)+O(\ell^5).
 \tag{26}
\]
Thus scalar normalization removes neither the genuine tracefree source
nor the original full Einstein question.

There is also an exact expression for the scale-invariant integral
Einstein defect used in the first research line. Put
\(J_\ell=\int|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2\) and
\(\widehat V_\ell=\operatorname{Vol}(\widehat g_\ell)\). Since
the scalar curvature is identically \(-12\),
\[
 \begin{split}
 \mathcal E(\widehat g_\ell)
 &=\inf_{\lambda\ne0}
       \frac{J_\ell+4(\lambda+3)^2\widehat V_\ell}
                       {\lambda^2\widehat V_\ell}\\
 &=\frac{4J_\ell}{36\widehat V_\ell+J_\ell}=O(\ell^5),
 \qquad
 \lambda_{\mathrm{opt}}=-3-\frac{J_\ell}{12\widehat V_\ell}.
 \end{split}                                                    \tag{26a}
\]
The minimum follows by completing the square in \(1/\lambda\).
Thus these fixed-topology examples have integral defect at most fifth
order while retaining the all-mode exclusion radius proved below.

## 6. No Einstein metric in the entire conformal class

This conclusion can be proved directly for the constructed classes,
without imposing any symmetry on a proposed conformal factor.
Their negative Yamabe constant excludes Einstein constants zero or
positive. Normalize a hypothetical conformal Einstein metric to
\(\operatorname{Ric}=-3g\). By uniqueness in §4 it must be
\(\widehat g_\ell=v_\ell^2g_\ell\).

There is a nonempty open region away from the shear where \(g_\ell\)
is a product of two curvature-\(-3\) surfaces. Both \(g_\ell\) and the
putative \(\widehat g_\ell\) are Einstein there. Put \(p=v_\ell^{-1}\).
The tracefree conformal Ricci formula gives
\[
 \nabla^2p=\varphi g_\ell.                                    \tag{27}
\]
For vectors \(X,Y\) tangent to different product factors, the mixed
curvature is zero. Commuting derivatives in (27) gives
\((X\varphi)Y-(Y\varphi)X=0\), so \(d\varphi=0\).
Commuting again within either curvature-\(-3\) factor then forces
the corresponding projection of \(\nabla p\) to vanish. Hence \(p\)
and \(v_\ell\) are constant on this open set. The common normalization
\(\operatorname{Ric}=-3g\) forces that constant to be \(v_\ell=1\).
This contradicts the strict inequality \(v_\ell>1\) in (16).

Therefore
\[
 \boxed{[g_\ell]\ \text{contains no Einstein metric of any sign}.}
 \tag{28}
\]
It follows that exact Einstein repair, if possible at all, must include
a genuinely nonconformal tensor deformation. This is stronger than
testing circle-invariant conformal corrections, but it still leaves
all nonconformal metrics on the same \(M\) available.

## 7. What this changes in the global problem

The scalar-calibrated metrics form an explicit bounded-curvature family
with three linked scales:
\[
 \|\operatorname{Ric}+3g\|_\infty=O(\ell^2),\qquad
 \operatorname{Vol}-V_*
   =\frac{kB_\beta}{24\pi^3}\ell^3+O(\ell^5),\qquad
 \|\operatorname{Ric}^{\circ}\|_2^2=O(\ell^5).
 \tag{29}
\]
The leading scalar and Yamabe deficits are the fixed shear class's
Hodge energy. The mixed connection equation has already been solved
in the long core. The surviving source is tracefree, transverse, and
has nonzero waist and fiber-shape projections described in
[round14_shear.md](round14_shear.md).

These facts supply a sharper input for a full tensor correction problem.
The quantitative all-mode exclusion in §8 strengthens the conformal
conclusion for this very family. Neither result prohibits an Einstein sequence crossing
infinitely many normalized moduli components. The Round-13 volume
argument still prohibits a continuous vanishing all-mode repair branch
and forces such a sequence to have distinct Einstein volumes tending
to \(V_*\). Nothing here establishes an analytic compactification at
the collapsed limit or rules out those infinitely many components.

The topological ratio remains
\((2\chi+3\tau)/\alpha^2=1\); the integral-rigidity forbidden band near
\(2/3\) is not entered. No Yau26 counterexample is claimed.

## 8. A simultaneous all-mode exclusion neighborhood

The independent receiver argument in
[round14_repair_radius.md](round14_repair_radius.md) applies to the
precise profile (4). In its notation \(c=\ell/(2\pi)\). It constructs
a compactly supported tracefree tensor on one nonzero-shear neck,
\[
 H=\chi(t)\operatorname{sech}^2(kt)
                   \{dt^2-a^2(d\phi+z_\ell\beta)^2\},
\]
where \(\chi=1\) throughout the shear and is cut off in the next
fixed-width exact-product bands. For the actual ungauged Einstein
operator, the self-adjoint gauged operator and the full gauge term give
\[
 \begin{split}
 \int\langle\operatorname{Ric}_{g_\ell}+3g_\ell,H\rangle
    &=-3kB_\beta c^3+O(c^6),\\
 \|H\|_1&=O(c),\\
 \|P_{g_\ell}H\|_1+\|\delta_{g_\ell}H\|_1&=O(c^2).
 \end{split}                                                    \tag{30}
\]
The linear response of an arbitrary global tensor perturbation of
\(C^2\) size \(\eta\) is therefore \(O(c^2\eta)\); its nonlinear
response is \(O(c\eta^2)\). The signed leading term cannot be removed
when \(\eta\leq\varepsilon c\), for sufficiently small fixed
\(\varepsilon>0\). The same tracefree receiver controls the possible
change in Einstein constant. No symmetry, support or gauge condition
is imposed on the perturbation.

The scalar repair satisfies
\(\|\widehat g_\ell-g_\ell\|_{C^2(g_\ell)}=O(\ell^2)\).
Its \(C^2\) norms and those of \(g_\ell\) are uniformly equivalent,
by (21). Thus there are \(r_0,b_0>0\) such that
\[
 \boxed{
 \|q-\widehat g_\ell\|_{C^2(\widehat g_\ell)}\leq r_0\ell
 \quad\Longrightarrow\quad
 \|q^{-1}\operatorname{Ric}_q+3I\|_\infty\geq b_0\ell^2,
 \quad q\text{ is not Einstein of any sign}.}
 \tag{31}
\]
Any diffeomorphism pullback lying in this ball is excluded as well.
In particular the calibrated family's defect is \(\Theta(\ell^2)\),
and it has an all-tensor no-Einstein neighborhood of radius proportional
to \(\ell\), together with the cubic volume excess (19). This provides
a quantitative separation between residual size and possible correction
size on a fixed closed manifold. The radius tends to zero, so it is
not a uniform global distance from all Einstein metrics and does not
settle their existence elsewhere.

The receiver also supplies the matching lower bound for the integral
defect. With \(A_F=\operatorname{Area}(F,h_F)\), its exact norm is
\[
 \|H\|_{L^2(g_\ell)}^2
 =4\pi A_F c\int\chi^2\operatorname{sech}^3(kt)\,dt
 =\frac{2\pi^2A_F}{k}c+O(c^4).
 \tag{31a}
\]
For the scalar correction \(h=\widehat g_\ell-g_\ell=O(c^2)\),
the linear and nonlinear response estimates used in (30) give
\[
 \int\langle\operatorname{Ric}_{\widehat g_\ell}
                       +3\widehat g_\ell,H\rangle_{g_\ell}\,d\mu_{g_\ell}
 =-3kB_\beta c^3+O(c^4).
 \tag{31b}
\]
The tensor in this pairing is \(\operatorname{Ric}^{\circ}_{\widehat g_\ell}\).
Its squared \(L^2\) norm is exactly conformally invariant in dimension
four. Cauchy--Schwarz and (31a)--(31b) therefore yield
\[
 \liminf_{\ell\to0}\frac{J_\ell}{c^5}
 \geq\frac{9k^3B_\beta^2}{2\pi^2A_F}>0.
 \quad\text{Consequently}\quad
 \boxed{J_\ell=\Theta(\ell^5),\qquad
        \mathcal E(\widehat g_\ell)=\Theta(\ell^5).}
 \tag{31c}
\]
This is a two-sided order statement. It does not identify the full
leading coefficient of the scalar-repaired tracefree energy.

More quantitatively, define the marked geometric distance
\[
 d_2(g,\mathrm{Ein})=\inf_{q\ {\rm Einstein}}
                  \|q-g\|_{C^2(g)},
 \tag{32}
\]
where all pullbacks and Einstein constants are allowed, and the infimum
of the empty set is \(+\infty\). Equation (31) gives
\(d_2(\widehat g_\ell,\mathrm{Ein})\geq r_0\ell\).
Write \(\delta_{-3}(g)=\|g^{-1}\operatorname{Ric}_g+3I\|_\infty\).
Consequently there is no uniform repair estimate on this family of either
form
\[
 d_2(g,\mathrm{Ein})\leq C\delta_{-3}(g)^p\quad(p>1/2),
 \qquad
 d_2(g,\mathrm{Ein})\leq C\mathcal E(g)^p\quad(p>1/5).
 \tag{33}
\]
Indeed their right sides are \(O(\ell^{2p})\) and \(O(\ell^{5p})\),
respectively, contradicting the lower bound when the exponent exceeds
one. The endpoint powers are not ruled out. This is an obstruction
to strong uniform quantitative correction, not to the unrestricted
existence implication asked by Yau26.

## 9. Proof inputs and checks

- [round11_closed_gluing.md](round11_closed_gluing.md): the fixed marked
  smooth gluing, hyperbolic collar, complete Ricci blocks, exact volume.
- [round11_variational.md](round11_variational.md): Yamabe invariant,
  both orientations, and curvature-energy identity on this family.
- [round11_kahler.md](round11_kahler.md): nonvirtual Kähler property
  of the nonzero-shear gluing, including identity fiber mapping class.
- [round12_global.md](round12_global.md): monopole numbers and global
  restrictions on the same manifolds.
- [round13_global.md](round13_global.md): normalized Einstein volume
  and the continuous-branch obstruction.
- [round14_shear.md](round14_shear.md): independent capacity, waist,
  and fiber-shape calculations.
- [round14_repair_radius.md](round14_repair_radius.md): the full-tensor
  adjoint receiver, linear and nonlinear response estimates, and the
  any-Einstein-constant exclusion used in (31).

[round14_global_check.py](round14_global_check.py) checks the exact profile
identity, tensor trace and norm, integral constants, conformal polynomial,
and volume cancellation. These finite checks do not replace the global
elliptic argument or the existing topological proofs.
