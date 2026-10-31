# 第三卷：完整区域成本、局域首项与真正近极小序列

Research snapshot: 0b1490791be560203b86a7d9834dcdc3cbc83b41.

I54—I55与X10完整正文。最新第三篇限定前文的研究目标：所有竞争序列的自动bulk选择已被反例否定，真正近极小序列的选择或带补偿替代仍开放。普通单bolt径向almost-Kähler整类排除不等于任意共形耦合类排除。

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using 10_source_map_and_history.md. Formula numbers restart in each source.


---

## Source 1: 20260928_relative_cell_cost.md

Original path: `continuation/20260928_relative_cell_cost.md`

SHA-256: `89230b7b655d7284b8fb67d513041b8ccf54c2c8b9e1df95ba6e86b5f8e223e7`

BEGIN COMPLETE SOURCE

# Relative surgery costs and almost-Kähler fillings

28 September 2026. Continuation of I44, I52 and I53, from local commit
`9e804ce`. The all-metric balanced first coefficient remains open.
This text makes the finite-region construction test precise and proves
that its conformally Kähler and biaxial candidates cannot improve it.
It then identifies the actual nonintegrability balance for the larger
conformal almost-Kähler class and retains its unresolved middle window.
The input metrics below are smooth metrics, not formal curvature data.

## 1. A complete cell and its exact relative identities

Fix an embedded ball D in a closed complex-hyperbolic surface, with the
complex orientation and Ric = -g. Write d = Vol(D). A cell is a compact
oriented smooth manifold

\[
 C=D\#k\overline{\mathbb {CP}}^{\,2}\#\ell(S^1\times S^3)
\]

with a specified outer collar on which its metric G agrees exactly with
the metric of D. All transition regions belong to C. Put

\[
 q=k+4\ell,\quad v=\operatorname{Vol}(C),\quad
 I=\int_Cs,\quad S=\int_Cs^2,\quad
 W=\int_C|W^+|^2,\quad B=\int_C|W^-|^2,
\]
\[
 R=\int_C|\operatorname{Ric}|^2,\quad
 P=R-S/4,\quad J=\int_C|\operatorname{Ric}+G|^2=R+2I+4v.
\]

The matching is of the whole metric germ, not only the induced boundary
metric. Thus all boundary transgression terms cancel on subtraction.
On D the corresponding values are s = -4, R = 4d, S = 16d,
W = 2d/3 and B = 0. Relative Chern--Weil and signature give

\[
 \boxed{R=8\pi^2q+S/3+4W-4d,\qquad
 B=12\pi^2k+W-2d/3.}                                      \tag{1.1}
\]

One can avoid boundary conventions by inserting C into the original
closed surface and subtracting the two closed identities. The changes
are \(\Delta(2\chi+3\tau)=-q\) and \(\Delta\tau=-k\).
Consequently

\[
 \boxed{J-8\pi^2q
 =\int_C\left(\frac{(s+3)^2}{3}+1+4|W^+|^2\right)-4d.}     \tag{1.2}
\]

This is an exact identity, not a lower bound. In particular, the
pointwise positivity of its density does not prove that its integral
is at least 4d on a different filling.

The classical closed identities and the shrinking constructions used
here are those of [LeBrun, Sections 3--4](https://arxiv.org/html/math/0003068),
also retained in [I44, Sections 5--6](20260927_covering_geometry_and_sharp_subfamilies.md).

## 2. A finite cell gives an actual same-family first-order test

Let X_j be the covers used in the existing balanced family, with
\(A_j=c_1^2(X_j)\), \(V_j^0=2\pi^2A_j\). Insert n_j copies of a fixed cell
into disjoint lifts of D, where \(n_j/A_j\to0\). There are enough lifts:
their number is a fixed positive multiple of A_j. Set

\[
 t=I+4v,\qquad v_j=2\pi^2A_j+n_j(v-d).
\]

The resulting actual smooth metric has

\[
 I_j=-4v_j+n_jt,\qquad
 R_j=4v_j+n_j(J-2t).
\]

Using \(\mathcal E=4-I_j^2/(v_jR_j)\), not a pointwise norm surrogate,
one obtains the exact formula

\[
 \boxed{\mathcal E
   =\frac{4n_jJ-n_j^2t^2/v_j}{4v_j+n_j(J-2t)}.}            \tag{2.1}
\]

For \(h_j=n_jq/A_j\), q > 0, it follows that

\[
             \frac{\mathcal E}{h_j}\longrightarrow
                         \frac{J}{2\pi^2q}.              \tag{2.2}
\]

This comparison includes the volume and total-scalar changes of the
cell. No Yamabe change or local monopole solution on the cell is needed.
The actual all-metric class supply is inherited on the closed connected
sum, as in I03.

For the original fixed balanced family, put \(Q_j=k_j+4\ell_j\).
Its construction gives

\[
 k_j/Q_j\to2/9,\qquad \ell_j/Q_j\to7/36,\qquad Q_j\to\infty.
\]

Use the cell with k = 8, ell = 7, q = 36, and choose

\[
 n_j=\min\{\lfloor k_j/8\rfloor,\lfloor\ell_j/7\rfloor\}.
\]

Then \(36n_j/Q_j\to1\). The remaining number of surgeries, counted
with weights 1 and 4, is \(o(Q_j)\); more precisely it is
\(O(A_jh_j^2)+O(1)\) for the original rounded family. Perform those
surgeries in separate lifts by the inherited shrinking construction.
For each fixed j its scale can be chosen so that its total volume and
scalar-moment errors are \(o(Q_j)\), and its Ricci-energy cost is
\(8\pi^2o(Q_j)\). This proves, on the original M_j rather than a new
topology window,

\[
 \boxed{\mathcal E(g_j)/h_j\to J/(72\pi^2).}               \tag{2.3}
\]

Thus a cell with J < 288 pi squared would answer the all-metric
coefficient question negatively. No such cell is constructed here.
As a smaller sufficient target, a single-blowup cell of cost J_1,
with all handles still treated by standard surgery, gives

\[
 \mathcal E/h_j\to\frac{28}{9}+\frac{J_1}{9\pi^2}.
\]

This would be below four if J_1 < 8 pi squared.

## 3. Kähler cells: an exact positive cost identity

Assume now that C is the complex blowup of D at k distinct interior
points, with its usual complex structure, and that K is a Kähler
metric equal to the complex-hyperbolic metric on the specified collar.
There are no handles in this statement. Let omega and rho be its
Kähler and Ricci forms, with \([\rho]=2\pi c_1\). Write

\[
 t_i=\int_{E_i}\omega>0,\qquad T_1=\sum_i t_i,\quad T_2=\sum_i t_i^2,
 \qquad v_K=d-T_2/2>0.
\]

The relative intersection matrix is minus the identity. Comparison
with the pullback of the forms on D gives

\[
 \operatorname{Vol}_K(C)=d-T_2/2,\qquad
 I_K:=\int_Cs_K=-4d-4\pi T_1.                             \tag{3.1}
\]

For completeness, omega differs from the pulled-back background class
by \(-\sum t_i\operatorname{PD}(E_i)\), while rho differs by
\(-2\pi\sum\operatorname{PD}(E_i)\). Cross terms against the pulled-back
classes vanish on each exceptional curve. The volume is half the
omega-square and the scalar integral is twice the rho--omega pairing.
These calculations are relative ones because the forms agree on the
collar; exact terms have no boundary contribution.

The closed real (1,1)-form alpha = rho + omega vanishes on the collar.
Its periods are \(2\pi+t_i\), so

\[
 \int_C\alpha\wedge\alpha=-\sum_i(2\pi+t_i)^2.
\]

Since \(|\operatorname{Ric}_K+K|^2=2|\alpha|^2\) and
\(\alpha^+=(s_K+4)\omega/4\), Hodge decomposition yields

\[
 \boxed{J(K)=2\sum_i(2\pi+t_i)^2
                    +\frac12\int_C(s_K+4)^2.}             \tag{3.2}
\]

In particular every such nontrivial smooth Kähler cell costs strictly
more than \(8\pi^2k\). Exceptional area and scalar error are separate
nonnegative contributions. This is a relative consequence of classical
Kähler identities, not a new existence or classification theorem.

## 4. The obstruction survives arbitrary conformal changes of the cell

**Theorem 1.** Let K be as in Section 3, k > 0, and let
\(K=u^2G\), where u is any smooth positive function equal to one on
the entire matching collar. Then

\[
 \boxed{J(G)\ge 8\pi^2k+8\pi T_1+2T_2
       +\frac{(2\pi T_1+T_2)^2}{d-T_2/2}
       +\frac14\int_C(s_G+4)^2>8\pi^2k.}                 \tag{4.1}
\]

No bound on u or its derivatives is assumed, and G need not be Kähler.

**Proof.** Use the positive scalar Laplacian. The conformal scalar
formula and u = 1 near the boundary give

\[
 I_K=\int_C(6|du|_G^2+s_Gu^2)\,dV_G
       \ge-\sqrt{S_Gv_K}.
\]

Here \(\int u^4dV_G=v_K\), and \(I_K<0\), whence
\(S_G\ge I_K^2/v_K\). Cauchy--Schwarz on K also gives
\(S_K\ge I_K^2/v_K\). The self-dual Weyl energy is conformally
invariant and equals S_K/24. Thus (1.1) says

\[
 R_G=S_G/3+S_K/6-4d+8\pi^2k.
\]

Write \(L_G=\int(s_G+4)^2\). The identity
\(J(G)=R_G-S_G/4+L_G/4\) now gives

\[
 J(G)=8\pi^2k-4d+S_G/12+S_K/6+L_G/4
       \ge8\pi^2k-4d+\frac{I_K^2}{4v_K}+L_G/4.
\]

Substituting (3.1) and expanding proves (4.1). QED.

For a single blowup of Kähler area t this reads

\[
 J(G)\ge \frac{2d(2\pi+t)^2}{d-t^2/2}
                         +\frac14\int_C(s_G+4)^2>8\pi^2. \tag{4.2}
\]

This excludes the whole conformally Kähler class, not just perturbations
of a shrinking model. It does not assert that all smooth fillings of
this topology are conformally Kähler.

## 5. Every smooth biaxial ordinary-blowup cell is covered

Normalize the invariant one-forms on S3 by
\(d\sigma_1=2\sigma_2\wedge\sigma_3\), cyclically, with Hopf period
2 pi and \(\int\sigma_1\sigma_2\sigma_3=2\pi^2\). Consider

\[
 G=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+b(t)^2\sigma_3^2.
\]

A smooth ordinary-blowup bolt at t = 0 has the smooth even/odd
expansions \(a=a_0+O(t^2)\), \(b=t+O(t^3)\), a_0 > 0.
Assume an exact radial complex-hyperbolic outer collar. Its Ricci
eigenvalues are

\[
\begin{aligned}
 \lambda_0&=-2a''/a-b''/b,\\
 \lambda_A&=-a''/a-(a'/a)^2-a'b'/(ab)+4/a^2-2b^2/a^4,\\
 \lambda_3&=-b''/b-2a'b'/(ab)+2b^2/a^4.
\end{aligned}                                                    \tag{5.1}
\]

The horizontal eigenvalue has multiplicity two. Thus the full cost is
\(2\pi^2\int a^2b\{(\lambda_0+1)^2+2(\lambda_A+1)^2+
(\lambda_3+1)^2\}\,dt\).

The complex structure with (1,0)-forms
\(dt+ib\sigma_3\) and \(a(\sigma_1+i\sigma_2)\) is integrable:
their exterior derivatives have no (0,2) component. Its form is
\(\omega=b\,dt\wedge\sigma_3+a^2\sigma_1\wedge\sigma_2\), with
\(d\omega=2(aa'-b)dt\wedge\sigma_1\wedge\sigma_2\). Solve

\[
                 (\log u)'=(b-aa')/a^2                         \tag{5.2}
\]

backward from u = 1 on the outer collar. Then K = u squared G is
Kähler. The coefficient in (5.2) is smooth and odd at the bolt, so u
extends smoothly, positively and evenly there. It is constant on the
matching collar because b = aa' there.

This is the usual complex blowup relative to that collar, not a new
complex filling: a complex radial coordinate satisfies
\(d\log\rho/dt=1/b\), with \(\rho=ct+O(t^3)\) at the bolt.
Normalizing it on the outer collar identifies the surface with the
standard complex blowup by a radial map equal to the identity there.
Theorem 1 therefore applies. Every such smooth biaxial cell satisfies
(4.2), for the positive Kähler area of its exceptional curve.

The conformal Kähler mechanism is classical; compare
[Naff--Weber, Lemma 2.1](https://arxiv.org/pdf/2111.11150).
The argument above includes the bolt extension and prescribed collar
needed for this relative cost application.

## 6. A finite-amplitude exclusion beyond the conformally Kähler class

Consider a triaxial distortion, keeping the radial and geometric-mean
profiles a,b fixed,

\[
 G_w=dt^2+a^2e^{2w}\sigma_1^2+a^2e^{-2w}\sigma_2^2+b^2\sigma_3^2.
\]

It has exactly the same volume form as the biaxial base. Require
smoothness at the bolt and w = 0 on the outer collar; compact support
away from the bolt is a sufficient condition, not an amplitude bound.
Let \(e_0=\lambda_0+1\), \(e_A=\lambda_A+1\),
\(e_3=\lambda_3+1\), and set

\[
\begin{aligned}
 c_w&=4a^{-2}(\cosh 2w-1),\\
 u_w&=-w''-(2a'/a+b'/b)w'+4b^{-2}\sinh4w-4a^{-2}\sinh2w,\\
 z_w&=8b^{-2}\sinh^22w.
\end{aligned}
\]

Cartan's formulas for a diagonal metric give

\[
 \operatorname{Ric}_{ii}=-a_i''/a_i
 -\frac{a_i'}{a_i}\left(\frac{a_j'}{a_j}+\frac{a_k'}{a_k}\right)
 +\frac{2\{a_i^4-(a_j^2-a_k^2)^2\}}{a_i^2a_j^2a_k^2},
 \qquad \operatorname{Ric}_{00}=-\sum_i a_i''/a_i.
\]

Substitution of \(a_1=ae^w,a_2=ae^{-w},a_3=b\) gives defect
eigenvalues \(e_0-2(w')^2,e_A+c_w+u_w,e_A+c_w-u_w,e_3-z_w\).
Consequently the exact change in the squared defect density is

\[
 \boxed{-4e_0(w')^2+4(w')^4+4e_Ac_w+2c_w^2+2u_w^2
                         -2e_3z_w+z_w^2.}                       \tag{6.1}
\]

Where \(e_0,e_3\le0\) and \(e_A\ge0\), this is nonnegative for
arbitrary w. No Taylor remainder is being discarded.

An explicit smooth bolt with this sign pattern is

\[
 F_\mu(r)=1+r^2/6-(\mu+\mu^2/2)/r^2+\mu^3/(3r^4),
 \quad K_\mu=dr^2/F_\mu+r^2(\sigma_1^2+\sigma_2^2)
                         +r^2F_\mu\sigma_3^2,\quad r\ge\sqrt\mu.
\]

Here

\[
 F_\mu=\frac{r^2-\mu}{r^2}
       +\frac{(r^2-\mu)^2(r^2+2\mu)}{6r^4}>0\quad(r>\sqrt\mu),
 \qquad \frac{\sqrt\mu}{2}F_\mu'(\sqrt\mu)=1.
\]

The exceptional area is \(\pi\mu\), s = -4, and
\(e_0=e_3=-p,e_A=p\), where \(p=\mu(\mu+2)/r^4\).
Fix \(0<r_c<r_1<r_D\). A cutoff equal to one below r_c and zero
above r_1 changes F to

\[
 \overline F_\mu=1+r^2/6+chi(r)
                  \{- (\mu+\mu^2/2)/r^2+\mu^3/(3r^4)\}.
\]

This is positive, retains the bolt, and is exactly CH on the outer
collar. It defines a complete Kähler cell. Permit arbitrary smooth
triaxial distortions of this metric, including on the transition,
but retain these a,b profiles. On the unchanged inner core, (6.1)
applies. The rest of J is nonnegative, so

\[
 \boxed{J(G_w)\ge2\pi^2(\mu+2)^2(1-\mu^2/r_c^4).}               \tag{6.2}
\]

Indeed the right side is \(2\pi^2\int_{\sqrt\mu}^{r_c}4p^2r^3dr\).
If \(0<r_c\le1\) and \(0<\mu\le r_c^4/3\), it is at least
\(8\pi^2+2\pi^2\mu\). The transition has not been assumed cheap:
its nonnegative contribution is simply retained on the correct side.

These classes contain metrics not conformally Kähler in the prescribed
orientation. Choose an interior point where w = w' = 0 and w'' = kappa,
with \(0<|\kappa|<1\). The changes in the radial sectional curvatures
are \(\delta R_{0101}=-\kappa\), \(\delta R_{0202}=\kappa\), and the
scalar curvature is unchanged. The self-dual Weyl eigenvalues become

\[
       1/3-\kappa/2,\qquad 1/3+\kappa/2,\qquad -2/3.
\]

They are distinct, whereas a conformally Kähler four-metric in that
orientation has a repeated self-dual Weyl eigenvalue. Thus (6.2) is
not merely another formulation of Theorem 1. It still does not cover
simultaneous changes of a,b and w.

### 6.1 All diagonal triaxial cells reduce to an actual almost-Kähler problem

There is a useful reduction even when all three profiles vary. For
\(G=dt^2+a^2e^{2w}\sigma_1^2+a^2e^{-2w}\sigma_2^2+b^2\sigma_3^2\),
solve (5.2) with u = 1 on the fixed collar and put r = ua. Then
\(dr/dt=ub/a>0\) away from the bolt. The conformal metric K = u squared G is

\[
 K=dr^2/F+r^2(e^{2w}\sigma_1^2+e^{-2w}\sigma_2^2)+r^2F\sigma_3^2,
 \qquad F=(b/a)^2.                                         \tag{6.3}
\]

Its compatible two-form
\(\omega=r\,dr\wedge\sigma_3+r^2\sigma_1\wedge\sigma_2\)
is closed for arbitrary F,w. Smoothness at an ordinary bolt gives
\(F(r_0)=0,F'(r_0)=2/r_0,w(r_0)=0\) with the smooth invariant
extensions; the outer collar has F = 1 + r squared/6 and w = 0.
Thus K is an actual almost-Kähler metric, not generally Kähler.
This includes every smooth diagonal triaxial cell with this bolt
and radial CH collar, up to a positive conformal factor fixed there.

Let \(t_E=\pi r_0^2\), \(v_K=d-t_E^2/2>0\), and
\(m_0=4d+4\pi t_E\). Define the nonnegative quantity

\[
 N=4\pi^2\int_{r_0}^{r_D}r^3F
       \left(w_r+\frac{2\sinh(2w)}{rF}\right)^2dr.          \tag{6.4}
\]

This quantity is finite for smooth bolt data. The scalar change
relative to the biaxial metric with the same F is, by (6.1),

\[
 -2F w_r^2+\frac8{r^2}(\cosh2w-1)
                  -\frac8{r^2F}\sinh^22w.
\]

Multiplying by \(2\pi^2r^3dr\) and integrating by parts gives

\[
                       \int_C s_K=-m_0-N.                 \tag{6.5}
\]

The cross term in (6.4) is integrated as the derivative of cosh 2w.
Its boundary term is \(8\pi^2r^2(\cosh2w-1)\), zero at both
the bolt and the full outer collar. The biaxial integral is -m_0
by (3.1); no assumption on its pointwise scalar curvature is used.

The almost-Kähler Chern identity gives
\(\int_C|\nabla\omega|^2=2N\). Equivalently one can check this
from (6.3)--(6.4): the nonintegrable part of the connection is the
square in (6.4). The relative Chern pairing is the same as for w = 0
because the compatible almost-complex structures are homotopic,
fixed at the bolt and collar. The usual identity
\(\int(s+|\nabla\omega|^2/2)=4\pi c_1\cdot[\omega]\)
then agrees with (6.5).
The classical integral identity, with \(|\nabla J|^2=2|\nabla\omega|^2\),
is recalled in [Apostolov--Armstrong--Draghici, introduction](https://faculty.fiu.edu/~draghici/research/paperfiles/Math-Ann.pdf).
Here it is applied after gluing the unchanged CH exterior, so subtraction
has no unspecified boundary contribution.

For any G conformal to K with factor one on the collar,
the scalar transfer used in Section 4 gives
\(S_G\ge(m_0+N)^2/v_K\). The self-dual Weitzenbock identity for
the closed constant-length form omega gives

\[
 \langle W^+\omega,\omega\rangle=s_K/3+|\nabla\omega|^2/2.
\]

A trace-free symmetric operator on the three-dimensional self-dual
space obeys \(|W^+|^2\ge3\langle W^+\omega,\omega\rangle^2/8\).
Integrating and using Cauchy yields
\(W_G=W_K\ge(m_0-2N)^2/(24v_K)\). Hence the actual remainders

\[
 A_0=S_G-(m_0+N)^2/v_K\ge0,\qquad
 B_0=W_G-(m_0-2N)^2/(24v_K)\ge0
\]

satisfy the exact identity

\[
 \boxed{J(G)-8\pi^2
 =-4d+\frac{m_0^2}{6v_K}
    +\frac{3}{4v_K}(N-m_0/3)^2
    +A_0/12+4B_0+\frac14\int_C(s_G+4)^2.}                \tag{6.6}
\]

The word exact refers to these defined remainders, not to equality
in the preceding scalar and Weyl estimates. Formula (6.6) exhibits
the possible competition: nonintegrability worsens the scalar budget
but can reduce the forced self-dual Weyl budget.

A subthreshold cell must satisfy \(m_0^2<24dv_K\) and

\[
 \frac{m_0-\sqrt{48dv_K-2m_0^2}}3<N<
 \frac{m_0+\sqrt{48dv_K-2m_0^2}}3.                        \tag{6.7}
\]

The lower endpoint is strictly positive because t_E > 0.
In fact N > 4 pi t_E is necessary. To see this, the first condition
implies \(\pi t_E/d<\sqrt{3/2}-1<1/2\), while
\((4d-8\pi t_E)^2-(48dv_K-2m_0^2)=(96\pi^2+24d)t_E^2>0\).
The exact sufficient inequality for excluding all such cells is
that the nonnegative remainders in (6.6) fill its possibly negative
first two terms. It has not been proved. This is a coupled functional
on actual metrics, with an explicit unresolved signed balance,
not a declaration that formal values of N,A_0,B_0 are realizable.

The same balance is not restricted to symmetry. On an ordinary
k-point blowup, let K be any almost-Kähler metric agreeing with the
CH structure on the whole collar, whose compatible almost-complex
structure has the usual relative first Chern class. Assume its
exceptional periods \(t_i>0\). Put

\[
 v_K=d-\tfrac12\sum t_i^2,\quad m_0=4d+4\pi\sum t_i,
                   \quad N=\tfrac12\int_C|\nabla\omega|^2.
\]

The relative intersection calculation and the same Chern identity
give (6.5). The scalar transfer and Weitzenbock argument are unchanged.
Thus (6.6) holds with 8 pi squared replaced by 8 pi squared k, with
the same definitions of A_0,B_0. Any subthreshold conformal metric
must have \(m_0^2<24dv_K\), satisfy (6.7), and in particular
\(N>4\pi\sum t_i\). The last square comparison now has right side
\(96\pi^2(\sum t_i)^2+24d\sum t_i^2\).
No symmetry or pointwise bound on the conformal factor is assumed.
The relative first Chern class is a genuine hypothesis; it cannot be
deduced for an arbitrary almost-complex filling solely from its Euler
number and signature.

In particular either of the explicit conditions
\(m_0^2\ge24dv_K\) or \(N\le4\pi\sum t_i\) rules out a lower
cost in this entire conformal almost-Kähler class. The second condition
is an integrated nonintegrability bound, not a Kähler assumption.
At its endpoint, writing \(T_1=\sum t_i,T_2=\sum t_i^2\), the
quadratic lower bound in (6.6) is
\((2dT_2+8\pi^2T_1^2)/v_K>0\). If \(\pi T_1<d/2\), that
quadratic is decreasing up to this endpoint; if \(\pi T_1\ge d/2\),
the first sufficient condition already holds. These observations
verify the two exclusions directly.

The remainders themselves have explicit analytic content. Put
\(H=6\int|du|_G^2\), \(q_\omega=\langle W_K^+\omega,\omega\rangle\),
and let P_omega be the orthogonal projection onto omega divided by
square root two. Then

\[
 A_0=\int_C\left(s_G+\frac{m_0+N+H}{v_K}u^2\right)^2dV_G
                  +\frac{2(m_0+N)H+H^2}{v_K},
\]
\[
 B_0=\int_C\left|W_K^+-\frac{3q_\omega}{4}
                  (P_\omega-\tfrac13I)\right|^2
             +\frac38\int_C(q_\omega-\overline q_\omega)^2.
                                                               \tag{6.7a}
\]

In every nontrivial smooth filling in this class A_0 is strictly
positive: equality would force u = 1, constant s_G, and hence s_G = -4
from the collar. But \(m_0+N>4v_K\) contradicts (6.5). This does
not supply a uniform modulus as the geometry degenerates.

If a fixed CH subcollar has volume \(0<a<v_K\), the remainder can
be quantified without differentiating it. Splitting Cauchy into that
collar and its complement gives

\[
 A_0\ge\frac{a(m_0+N-4v_K)^2}{v_K(v_K-a)},\qquad
 B_0\ge\frac{a(m_0-2N-4v_K)^2}{24v_K(v_K-a)}.             \tag{6.7b}
\]

For the first inequality u = 1 and s_G = -4 on the collar, while
\(\int s_Gu^2=-m_0-N-H\); discard H only after the complementary
square is formed. For the second, \(q_\omega=-4/3\) on the collar
and its full mean is \((-m_0+2N)/(3v_K)\); use (6.7a).
These are fixed-collar bounds, not uniform control when a tends to zero.

### 6.2 Symmetrization is not a monotone procedure

The positive comparison (6.1) has indispensable sign conditions.
There is an actual smooth fixed-collar cell where an arbitrarily small
triaxial deformation decreases J. Choose a positive smooth biaxial
profile F with a smooth ordinary bolt, a constant plateau F = 2 on
\(R e^{-L}<r<R\), and the exact CH profile on the exterior collar.
Such a profile is obtained by positive cutoff interpolation outside
the plateau, retaining the bolt and exterior germs.

On the plateau the base defects are
\(e_0=e_3=1,e_A=1-4/r^2\). Put \(s_0=\log r\) in this paragraph
(not scalar curvature), and \(w=\varepsilon f(s_0)\) supported there.
Expanding the exact (6.1) and integrating its mixed derivative yields

\[
 J(G_{\varepsilon f})-J(G_0)
 =16\pi^2\varepsilon^2\int
       \{f_{s_0s_0}^2+(4-r^2)f_{s_0}^2-16f^2\}\,ds_0
       +O(\varepsilon^4).                                \tag{6.8}
\]

For \(f(s_0)=\sin^2(\pi(s_0-s_*)/L)\) on that interval,
extended by zero, the integral after omitting the negative
\(-r^2f_{s_0}^2\) term is

\[
                   2\pi^4/L^3+2\pi^2/L-6L.
\]

At L = pi it is -2 pi. This zero extension is in the clamped H2 space;
smooth compactly supported approximations preserve the strict negative
value because the quadratic form is continuous in H2 on this fixed
annulus. For such a smooth f and sufficiently small nonzero epsilon,
the actual complete metric has smaller J. All transition regions are
unchanged, so they cancel in this comparison.

This descent is not subthreshold. The plateau itself already costs

\[
 \frac{J_{\rm plateau}(G_0)}{2\pi^2}
 =R^4(1-e^{-4L})-8R^2(1-e^{-2L})+32L
 \ge32L-16\tanh L.                                      \tag{6.9}
\]

At L = pi this is greater than 84, whereas the single-blowup target
in these units is four. A sufficiently small perturbation stays above
that target. Duplication of this model duplicates its cost; it does
not amortize it over additional topology. No multi-blowup matching
construction is supplied. Equations (6.8)--(6.9) together rule out
unconditional monotone symmetrization as a proof strategy without
misreporting a high-energy descent as a lower first coefficient.

### 6.3 The complete coupled functional retained for continuation

In (6.3), write G = exp(2 phi) K. Derivatives below are with respect
to r, and the data F,w,phi obey the smooth bolt conditions and
\(F=1+r^2/6,w=\phi=0\) on the fixed outer collar. Define

\[
 E_V=1-F''/2-5F'/(2r),\qquad
 E_H=1-F'/r+4(1-F)/r^2,
\]
\[
 c=4r^{-2}(\cosh2w-1),\quad z=8(r^2F)^{-1}\sinh^22w,
\]
\[
 U=-Fw''-(F'+3F/r)w'+4(r^2F)^{-1}\sinh4w
                                        -4r^{-2}\sinh2w,
\]
\[
\begin{aligned}
 D_0&=E_V+e^{2\phi}-1-3F\phi''-(2F'+3F/r)\phi',\\
 D_3&=E_V+e^{2\phi}-1-F\phi''-(2F'+5F/r)\phi'-2F(\phi')^2,\\
 D_H&=E_H+e^{2\phi}-1-F\phi''-(F'+5F/r)\phi'-2F(\phi')^2.
\end{aligned}
\]

The conformal Ricci formula and the unchanged triaxial volume give

\[
 \boxed{J(G)=2\pi^2\int r^3\left[
 (D_0-2F(w')^2)^2+(D_3-z)^2+2(D_H+c)^2
                    +2(U-2F\phi'w')^2\right]dr.}         \tag{6.10}
\]

This includes the conformal factor and every transition. Its difference
from the same F,phi with w = 0 contains exactly the possibly negative
cross terms \(-4D_0F(w')^2+4D_Hc-2D_3z\), in addition to squares.
Thus the remaining sufficient estimate in this class is explicitly

\[
 \frac{A_0}{12}+4B_0+\frac14\int(s_G+4)^2
 \ge4d-\frac{m_0^2}{6v_K}
                 -\frac{3(N-m_0/3)^2}{4v_K}              \tag{6.11}
\]

on the middle interval where its right side is positive. Equations
(6.4), (6.7a) and (6.10) specify the same actual variables on both
sides; choosing their moments independently is not a construction.

## 7. A general cell bound and its remaining numerical window

The actual closed supply yields an additional lower bound for every
cell of Section 1, without a Kähler or symmetry hypothesis. Put
\(w=\sqrt6|W^+|\). Insert the cell into a CH surface (or an appropriate
finite cover with b-plus greater than one) and use the blowup and
handle supplier of I03. The selected actual class has
\((a_g^+)^2\ge A\). The signed LeBrun estimate gives

\[
 \int_M(-s+w)_+^2\ge72\pi^2 A.
\]

On the unchanged exterior its integrand is 36 and the original closed
volume is \(2\pi^2A\). Subtraction gives
\(H_C:=\int_C(-s+w)_+^2\ge36d\). This is the inherited actual supply,
not an assumption that an arbitrary local spinor extends.
See [the signed estimate](../mathematics/current/line1_functional_pencil.md)
and [the supplier](../mathematics/current/lebrun_stability_closure.md).
In the original source these are the proof of LeBrun Theorem 2.3,
equation (11), and Proposition 3.2. Equation (11) is the signed estimate
using the smallest Weyl eigenvalue; its comparison with the Weyl norm
retains the positive part. The unsplit square inequality alone would
not justify discarding its negative part. The actual class is selected
for the metric polarization, not fixed for every metric on M.

Let \(F_C=J-8\pi^2q+4d\), the integral in (1.2). Pointwise,
\((-s+w)_+\le3+|s+3|+w\). Minkowski and weighted Cauchy give

\[
 \sqrt{H_C}\le3\sqrt v+
 \sqrt{\frac92(F_C-v)}.
\]

It follows that

\[
 \boxed{J\ge8\pi^2q-4d+v+2(2\sqrt d-\sqrt v)_+^2.}             \tag{7.1}
\]

Minimizing the right side over v > 0 gives

\[
 J\ge8\pi^2q-4d/3,\qquad
 J<8\pi^2q\ \Longrightarrow\ 4d/9<v<4d.                       \tag{7.2}
\]

The pointwise identity

\[
 \frac{(s+3)^2}{3}+1+\frac23w^2
 =\frac2{27}(-s+w)^2+\frac14(s+4)^2
                            +\frac{16}{27}(w+s/8)^2
\]

also retains the exact remainder

\[
\begin{aligned}
 J={}&8\pi^2q-4d/3+\frac2{27}(H_C-36d)
 +\frac2{27}\int_C(-s+w)_-^2\\
 &+\frac14\int_C(s+4)^2
 +\frac{16}{27}\int_C(w+s/8)^2.
\end{aligned}                                             \tag{7.3}
\]

These bounds do not yield the complete threshold. For example, formal
constant curvature moments s = -4, w = 1/2 on volume 16d/9 saturate
the numerical minimization in (7.3). They are not a metric filling
and do not match the prescribed collar. The missing conclusion is
differential and global, not an unperformed minimization of (7.3).
In fact the prescribed nonempty CH collar U has s = -4 and w = 2,
so (7.3) gives the stronger strict bound
\(J\ge8\pi^2q-4d/3+4\operatorname{Vol}(U)/3\).
The improvement depends on the collar volume; it is not uniform if
the permitted collar shrinks. No classification of equality metrics
is needed for this observation.

## 8. The full fixed-collar problem has no smooth interior critical point

**Proposition 2.** If q > 0, no smooth cell of Section 1 is stationary
for J under all compactly supported smooth metric variations.

**Proof.** Write \(\Delta_+=-\operatorname{div}\nabla\). The conformal
variation \(\dot g=2fg\), with f compactly supported, gives in dimension
four

\[
             \dot J=4\int_C f(\Delta_+s+s+4).             \tag{8.1}
\]

One obtains this either directly or from
\(J=\int|\operatorname{Ric}|^2+2\int s+4\operatorname{Vol}\).
At a stationary metric, test the scalar equation with s + 4, which
vanishes on the whole collar. Hence s = -4.

For the tensor variation use \(\Delta_-=-\Delta_+\) on the connection
Laplacian. The gradient of the Ricci-square integral is

\[
 -\Delta_-\operatorname{Ric}-2\operatorname{Rm}(\operatorname{Ric})
 +\nabla^2s-\tfrac12(\Delta_-s)g+\tfrac12|\operatorname{Ric}|^2g.
\]

Adding the other two gradients, substituting s = -4, and setting
E = Ric + g yields

\[
       \Delta_-E=-2\operatorname{Rm}(E)+\tfrac12|E|^2g.     \tag{8.2}
\]

For a fixed smooth cell this is a uniformly elliptic system locally
with scalar principal symbol and bounded coefficients; the last term
may be regarded as a bounded linear coefficient acting on E.
Since E vanishes on an open collar, elliptic unique continuation gives
E = 0 throughout the connected cell. This use does not require a
uniform estimate over degenerating cells.

Glue back the closed CH exterior. The result is a smooth Einstein
metric. Einstein analyticity and the open CH region imply
\(\nabla\operatorname{Rm}=0\) globally, with the CH curvature type.
The resulting closed manifold is therefore locally CH and aspherical.
If k > 0, its exceptional sphere has nonzero homology class and hence
nontrivial pi-two, a contradiction. If k = 0 and ell > 0, its
\(\chi-3\tau=-2\ell\), whereas a closed locally CH surface in this
orientation has \(\chi=3\tau\). This is again a contradiction. QED.

The exact gradient is recorded in
[Catino, Section 2](https://arxiv.org/pdf/1404.0569).
For systems with this common principal part use
[Aronszajn, Remark 3, page 248](https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf).
The analytic step is
[DeTurck--Kazdan, Theorem 5.2](https://www.numdam.org/article/ASENS_1981_4_14_3_249_0.pdf).

This is a nonattainment statement for smooth fixed-collar critical
metrics. It neither proves \(J\ge8\pi^2q\) for all competitors nor
excludes a sequence of subthreshold metrics. A variational search must
permit degeneration or nonattainment; a smooth numerical stationary
candidate with an exactly fixed open CH collar cannot be an exact
critical point of this unrestricted problem.

## 9. Continuation point

The finite-cell route is an actual geometric alternative to a universal
first-order lower bound. Equations (2.1)--(2.3) specify exactly how a
successful cell would change that bound on the retained real family.
Theorem 1 rules out the conformally Kähler route to such a cell.

I53 independently excludes competitors retaining enough low-cost
marked annuli. Its total curvature budget is O(A), whereas the sharp
error target is o(Q) with Q = Ah. Selecting one of L annuli only pays
O(A/L), so Lh tending to infinity, not merely L tending to infinity,
is needed for that argument. A direct signed estimate may bypass
annular extraction, but rewriting the signature identity cannot:

\[
 12\pi^2b+C_+-B_N-K_+
                   =12\pi^2k-\int_M|W^-|^2
\]

is independent of the choice of partial caps. Any new estimate must
control its geometric terms, with the permitted scalar compensation,
rather than name a new cap-dependent invariant.

The open construction target is therefore genuinely outside the proved
conformal filling class and the cheap-collar regime. The unrestricted
coefficient and the weak zero endpoint remain separate open questions.


END COMPLETE SOURCE


---

## Source 2: 20260928_localization_and_coupled_filling.md

Original path: `continuation/20260928_localization_and_coupled_filling.md`

SHA-256: `7820b33af8ed573f3ab6e817a21e8dab4575a33c412d4adac6faa196e8b46578`

BEGIN COMPLETE SOURCE

# Localization volume and the first-order cost of whole fillings

28 September 2026. Continuation from `105df84`, using the relative
identities of [I54](20260928_relative_cell_cost.md). The estimates below
apply to complete smooth fillings, not selected terminal bubbles.
They settle the first coefficient for a localized class with arbitrary
interior metrics. They do not extract that class from arbitrary
near-minimizers, so O11 remains open.

## 1. An exact all-metric bound with a fixed exterior

Let X be a closed complex-hyperbolic surface, with its complex orientation
and metric satisfying Ric = -g. Write A = c1 squared(X), so its volume
is 2 pi squared A. Remove finitely many disjoint smoothly bounded regions
which are balls, with total background volume D. Replace them by complete
marked smooth cells of the topological types in I54, Section 1. The metric
agrees with the original CH metric on the full outer collars and on the
entire complement. There are no hypotheses on the interior metric,
concentration, diameter, volume, derivatives, or its distance from a model.

Let k and ell be the total blowup and handle numbers and put

\[
 Q=k+4\ell>0,\qquad a=2\pi^2A-D>0,\qquad
 b=8\pi^2Q-4D,\qquad c=4a+b.
\]

In this section assume b is nonnegative. On the union C of the inserted
cells define

\[
 v=\operatorname{Vol}(C),\quad t=\int_Cs,\quad
 S=\int_Cs^2,\quad W=\int_C|W^+|^2.
\]

The relative identities sum over whole cells; no interior boundary is
introduced. The total Ricci energy R and total scalar integral I are

\[
 R=c+S/3+4W,\qquad I=-4a+t,\qquad V=a+v.                 \tag{1.1}
\]

In particular R is positive. Recall the scale-invariant residual

\[
 \mathcal E=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2 V}
          =4-\frac{I^2}{VR}.
\]

The formula remains valid when I = 0, with infimum four as
the absolute value of lambda tends to infinity. No normalization of the
unknown optimum lambda is imposed.

**Theorem 1.** Every metric with this complete exterior satisfies

\[
 \boxed{\mathcal E\ge
 \frac{4ab/c+v}{a+v}
 =\frac{4b}{c}+\left(1-\frac{4b}{c}\right)\frac{v}{a+v}
 \ge\min\{4b/c,1\}.}                                   \tag{1.2}
\]

For b at most 4a/3, the last lower bound is explicitly

\[
 \boxed{\mathcal E\ge
 \frac{4(Q-D/(2\pi^2))}{A+Q-D/\pi^2}.}                  \tag{1.3}
\]

*Proof.* Cauchy gives S at least t squared/v. Applying weighted
Cauchy a second time yields

\[
 (-4a+t)^2\le
 \left(\frac{16a^2}{c}+3v\right)
 \left(c+\frac{t^2}{3v}\right)
 \le\left(\frac{16a^2}{c}+3v\right)R.
\]

Subtract the resulting upper bound for I squared/(VR) from four.
This proves (1.2); inserting a and b proves (1.3). These uses of Cauchy
are on actual integrals. No formally optimized moments are claimed to
be realized by a smooth metric. The underlying relative curvature
identity is classical Chern--Weil, as derived in I54, Section 1. QED.

The bound does not require an actual monopole on an individual cell.
The original closed family's actual supply is preserved because the
topological surgery types and their markings have not changed. In
particular this is an application to that family, not a construction
of a new supplier.

## 2. The equality remainder and the whole-core energy distribution

To retain the equality information, set

\[
 \delta=\frac13(S-t^2/v)+4W\ge0,\qquad
 K=16a^2/c+3v,\qquad H=\frac{(3vc+4at)^2}{3vc}.
\]

Since R = c + t squared/(3v) + delta, exact expansion gives

\[
 KR-I^2=K\delta+H.
\]

Thus the proof of Theorem 1 retains the identity

\[
 \boxed{\mathcal E=
 \frac{4ab/c+v}{a+v}
       +\frac{K\delta+H}{(a+v)R}.}                       \tag{2.1}
\]

Consider the original balanced sequence with
Q_j = A_j h_j, h_j tending to zero, and assume only that
D_j = o(Q_j). The following result also applies to other surgery
proportions on CH covers; the balanced proportions are not used in
its proof.

**Theorem 2.** In this class, independently of the interior geometry,

\[
 \liminf_j\mathcal E(g_j)/h_j\ge4.                       \tag{2.2}
\]

Furthermore the following two statements are equivalent:

\[
 \mathcal E(g_j)/h_j\longrightarrow4;
 \qquad v_j+S_j+W_j=o(Q_j).                              \tag{2.3}
\]

The three summands in the second statement are nonnegative. Equivalently,
each is o(Q_j). For such a sequence,

\[
 \int_{C_j}|\operatorname{Ric}|^2=8\pi^2Q_j+o(Q_j),
 \qquad \int_{C_j}|\operatorname{Ric}^{\circ}|^2
                                  =8\pi^2Q_j+o(Q_j),    \tag{2.4}
\]
\[
 \int_{C_j}|W^-|^2=12\pi^2k_j+o(Q_j).                   \tag{2.5}
\]

These are statements about the entire inserted region, including all
intermediate necks and scales, not a classification of individual bubbles.

*Proof.* As j tends to infinity, a is asymptotic to 2 pi squared A,
c is asymptotic to 4a, and L := 4b/c = 4h + o(h). Eventually L is less
than one. Equation (1.2) first proves (2.2). If E/h tends to four,
it also gives v/(a+v) = o(h), hence v = o(Q).

One must use the remainder, not infer small scalar energy from this volume
statement alone. Since t squared is at most vS and S is at most 3R,
the exact definition of E gives

\[
 \sqrt{(4-\mathcal E)(a+v)}\sqrt R
       =|-4a+t|\le4a+\sqrt{3v}\sqrt R.
\]

Here E tends to zero and v/a tends to zero. Moving the last term to
the left proves R = O(a); also R is at least c, which is comparable
to a. The first term of (2.1) is 4h + o(h), so

\[
 K\delta+H=o(Qa).
\]

Because K is comparable to a, delta = o(Q). Also

\[
 H=\frac{16a^2}{3vc}\left(t+\frac{3vc}{4a}\right)^2,
 \qquad
 \left(t+\frac{3vc}{4a}\right)^2=o(Qv).
\]

As c/a is bounded and v = o(Q), it follows that t squared/v = o(Q).
The definition of delta now proves S + W = o(Q).

Conversely, v + S + W = o(Q) gives t = o(Q) by Cauchy. In (1.1),
R = 4a + b + o(Q), I = -4a + o(Q), V = a + o(Q). Expanding the
exact expression for E gives E = 4h + o(h). Finally the relative
Ricci and signature identities in I54 give (2.4)--(2.5). QED.

Classical shrinking surgery constructions attain (2.3) by choosing
their scales sufficiently small. In this localized class the lower
coefficient is therefore sharp. The theorem does not assume those
constructions describe all competing interiors.

## 3. A fixed improvement must modify a nonnegligible amount of background

Let theta = D/(2 pi squared Q). When 0 <= theta < 1 and h is small,
Theorem 1 gives

\[
 \frac{\mathcal E}{h}\ge
        \frac{4(1-\theta)}{1+h-2\theta h}.                \tag{3.1}
\]

If e := E/h is at most 4-epsilon, with fixed positive epsilon and
small h, rearrangement gives

\[
 \theta\ge\frac{4-e(1+h)}{4-2eh}.
\]

The branch theta >= 1 already has a stronger volume lower bound.
Consequently any such subfour sequence in the complete-exterior class
must satisfy

\[
 \boxed{\liminf_j\frac{D_j}{Q_j}
                       \ge\frac{\pi^2}{2}\varepsilon.}  \tag{3.2}
\]

It cannot obtain a fixed first-order improvement by arbitrary violent
changes confined to background regions of total volume o(Ah). This is
different from the shrinking C0-neighborhood theorem I53: the interior
here need not be close to any recovery metric, but the entire exterior
is fixed. Neither hypothesis is asserted to follow from the other.

For a fixed cell replicated sparsely, I54's stronger supplier-based
bound J >= 8 pi squared q - 4d/3 gives the sharper necessary cost
condition d/q >= (3 pi squared/2) epsilon for a coefficient at most
4-epsilon. The all-metric bound above does not presuppose fixed cells,
uniform cell volume, or convergence of their individual energies.

The unresolved alternative is now specific: a lower coefficient must
change a Q-scale amount of background, or must not admit this marked
complete-exterior description. No extraction theorem has been proved.

### 3.1 Individual cores and their topology need not be identified

The preceding proof extends further than its cell formulation. Suppose
the closed manifold M is already the prescribed member of the actual
family, hence \(2\chi(M)+3\tau(M)=A-Q\) and
\(\tau(M)=\tau(X)-k\). Assume only that an open subset U of the CH base
X is orientation-preservingly isometric to an open subset U' of M.
Put D = Vol(X without U) and let C be M without U'.

Subtract the two *closed* Chern--Weil identities and then split their
integrals into the common open set and its complement. The same equations
(1.1) and the relative signature identity follow. No Stokes theorem on
the complement and no boundary transgression are needed. Theorems 1--2
and (3.2) are unchanged. The complements may be clustered, connected,
multiply bounded, or lack a smooth boundary; none has to be identified
as a ball or an individual surgery core. All integrals over them are
ordinary measurable-set integrals of the smooth closed metric.

Thus the statement does not require a bubble-tree decomposition.
It only requires the common metric region and the known topology of
the closed member of the family. The common-region hypothesis itself
has not been derived from small Einstein defect.

In fact no identification with a region in a specified base is needed.
It is enough that M, of the same known closed topology, has a complex-
oriented locally CH open region of volume at least
2 pi squared A - o(Q), normalized by Ric = -g. Select a measurable
subregion with volume at most 2 pi squared A and discrepancy o(Q).
Its scalar, Ricci and Weyl densities are exactly those used in (1.1).
Splitting the closed identities gives (2.2) directly, without an
external marking or any asserted topology of its complement.

## 4. The exterior need not be Einstein

There is an exact interface for a varying exterior. Start with any smooth
reference metric on the closed base, remove the reference cells D, and
replace them by the same marked surgeries, preserving the full metric
germs. On the unchanged exterior let

\[
 a=\operatorname{Vol}(M\setminus C),\quad
 i=\int_{M\setminus C}s,\quad
 r=\int_{M\setminus C}|\operatorname{Ric}|^2>0,
 \quad e_{\mathrm{out}}=4-i^2/(ar)\ge0.
\]

All reference cap integrals below concern the reference metric, not
the inserted geometry. Relative Chern--Weil gives

\[
 b=8\pi^2Q+R_D-S_D/3-4W_D^+,\quad c=r+b,\quad
 R=c+S/3+4W,\quad I=i+t.                                 \tag{4.1}
\]

Assume b is nonnegative. Set

\[
 L=4-\frac{i^2}{ac}
  =e_{\mathrm{out}}+(4-e_{\mathrm{out}})\frac b{r+b},
 \quad K=i^2/c+3v,\quad H=\frac{(3vc-it)^2}{3vc}.
\]

Exactly as before, with delta = (S-t squared/v)/3 + 4W,

\[
 \boxed{\mathcal E=\frac{aL+v}{a+v}
                 +\frac{K\delta+H}{(a+v)R}.}             \tag{4.2}
\]

This formula is valid even when i vanishes. It explicitly retains
the cost of a non-Einstein exterior; replacing the cap correction by
the CH value -4D without its hypotheses would be incorrect.

**Theorem 3.** Suppose h = Q/A tends to zero,

\[
 r=8\pi^2A+o(A),\qquad b=8\pi^2Q+o(Q),
                    \qquad\mathcal E=O(h).              \tag{4.3}
\]

Then e_out = O(h), v/a = O(h), and

\[
 \boxed{\mathcal E\ge e_{\mathrm{out}}+4h+\frac{v}{a+v}+o(h).}
                                                               \tag{4.4}
\]

Moreover E/h tends to four if and only if

\[
 e_{\mathrm{out}}=o(h),\qquad v/a=o(h),\qquad S+W=o(Q).
                                                               \tag{4.5}
\]

The condition E = O(h) in (4.3) is dispensable in the reverse implication
of (4.5), since the other assumptions then give it.

*Proof.* Since E tends to zero and (4.2) implies E >= min(L,1),
eventually L <= E. Also L >= e_out, so e_out = O(h). The first term
of (4.2) is L + (1-L)v/(a+v); hence v/a = O(h). Assumptions (4.3)
then give L = e_out + 4h + o(h), proving (4.4).

If E/h tends to four, (4.4) forces e_out = o(h) and v/a = o(h).
As in Section 2,

\[
 \sqrt{(4-\mathcal E)(a+v)}\sqrt R
                 \le |i|+\sqrt{3v}\sqrt R
                 \le2\sqrt{ar}+\sqrt{3v}\sqrt R.
\]

Thus R = O(r). Now K is comparable to a, c is comparable to r,
and the remainder in (4.2) is o(h). It follows that delta = o(Q),
H = o(aQ), and

\[
 \left(t-\frac{3vc}{i}\right)^2=o(vQ).
\]

Here i is nonzero for large j since e_out tends to zero. Also
\(v c^2/i^2=O(vr/a)=o(Q)\). Consequently t squared/v = o(Q),
and S+W = o(Q). Conversely these conditions give
R = r + 8 pi squared Q + o(Q). The scalar cross term obeys

\[
 \frac{|it|}{ar}\le
             2\sqrt{\frac{v}{a}\frac{S}{r}}=o(h).
\]

The same exact formula for E proves the reverse implication. QED.

For example, (4.3)'s cap condition holds if
R_D + S_D + W_D^+ = o(Q); this is a property of actual reference caps,
not an assumed bubble decomposition. The exterior energy condition
must likewise be supplied. Theorem 3 gives additive first-order
costs of bulk defect and topology in this precise interface. It is
not a Gamma-convergence theorem and gives neither compactness nor
an automatic choice of reference metric for every near-minimizer.

Here is a natural way to supply the reference energy in (4.3).
Suppose the reference metrics on the CH bases themselves obey
\(\mathcal E(g_j^{\mathrm{ref}})=O(h_j)\), and the removed reference caps
have \(R_D+W_D^+=o(Q_j)\). The classical Ricci-energy lower bound on a
complex-hyperbolic surface is \(R_{\mathrm{ref}}\ge8\pi^2A\);
see [LeBrun, Theorem 4.3](https://arxiv.org/html/math/0003068).
The opposite inequality needed here follows directly from the signature:

\[
 W_{\mathrm{ref}}^+\ge12\pi^2\tau(X)=4\pi^2A/3,\qquad
 R_{\mathrm{ref}}=4P_{\mathrm{ref}}-12W_{\mathrm{ref}}^+
                                                    +24\pi^2A,
\]
\[
 4P_{\mathrm{ref}}\le
       \mathcal E(g^{\mathrm{ref}})R_{\mathrm{ref}},
 \qquad
 R_{\mathrm{ref}}\le
       \frac{8\pi^2A}{1-\mathcal E(g^{\mathrm{ref}})}.    \tag{4.6}
\]

For the last estimate take j large enough that the denominator is
positive. Since S_D <= 4R_D, these hypotheses give exactly
b = 8 pi squared Q + o(Q) and r = 8 pi squared A + O(Q).
Thus Theorem 3 applies to arbitrary replacement interiors on these
non-Einstein reference backgrounds. No smallness of their C0 distance
from the CH metric is required. The cap smallness remains an actual
assumption, not a consequence of a scalar or Ricci bound alone.

### 4.1 An intrinsic bulk criterion without a reference metric

The complete region-matching assumption can be replaced by precisely
the integral information used in the proof. On any closed member M
with \(T_+=A-Q\), choose any measurable subset U of positive volume,
with complement C of positive volume. Define its curvature budget

\[
 T_U=\frac1{8\pi^2}\left\{\frac13\int_U s^2
                   +4\int_U|W^+|^2-\int_U|\operatorname{Ric}|^2\right\}.
                                                               \tag{4.7}
\]

This is a real-valued curvature integral, not an integer or a relative
characteristic number. The closed Chern--Weil identity gives (4.1)
with
\[
                  b=8\pi^2(T_U-T_+).
\]
Consequently, if actual sets U_j can be chosen with
\[
 T_{U_j}=A_j+o(Q_j),\qquad
 \int_{U_j}|\operatorname{Ric}|^2=8\pi^2A_j+o(A_j),        \tag{4.8}
\]
Theorem 3 applies verbatim. Neither a metric model on U_j, a smooth
interface, a relative gauge marking, nor an identification of the
complement's topology is required.

Its fine additive and equality statements still concern competitive
sequences with E = O(h). Conditions (4.8) alone imply the liminf lower
coefficient four, not the upper bound E = O(h).

This is a sufficient integral selection criterion, not a completed
selection theorem. In particular, the global identity only gives
\(T_M=A-Q\); it does not supply a subset carrying \(A+o(Q)\).
Equation (4.8) expresses exactly the missing first-order separation of
the bulk curvature budget from the negative budget in its complement.
If the actual field equations produce such sets for all competitive
sequences, the all-metric lower coefficient follows. The present proof
does not assume that conclusion.

## 5. A finite-amplitude exclusion for the coupled diagonal profiles

For the remaining fixed-scale construction problem, use precisely the
actual profiles F,w,phi and the symbols D_0,D_3,D_H,c_0,z_0,U of I54,
Section 6.3. Subscripts on c_0,z_0 in this section distinguish them from
the global moment c above. Write

\[
 G_w=e^{2\phi}K_{F,w},\quad G_0=e^{2\phi}K_{F,0},
 \quad V_w=U-2F\phi'w'.
\]

The full fixed collar is CH; the ordinary bolt is at r_0 = sqrt(mu).
In particular F(r_0) = 0, F'(r_0) = 2/r_0, and w has the smooth
ordinary-bolt extension specified in I54. Direct subtraction of the
complete cost, including every transition, gives

\[
\begin{split}
 \frac{J(G_w)-J(G_0)}{2\pi^2}=\int r^3\bigl[
 &-4D_0F(w')^2+4F^2(w')^4+4D_Hc_0+2c_0^2\\
 &+2V_w^2-2D_3z_0+z_0^2\bigr]\,dr.                     \tag{5.1}
\end{split}
\]

Fix r_c,R,K,M independent of mu, with r_0 < r_c < R and R inside
the unchanged CH collar. On the fixed interval [r_c,R], assume

\[
 M^{-1}\le F\le M,\quad |F'|+|\phi'|\le M,\quad |w|\le K,\quad
                   \max(|D_0|,|D_3|,|D_H|)\le\eta.
                                                               \tag{5.2}
\]

**Proposition 4.** There is a positive eta_0 depending only on
r_c,R,K,M such that, if eta <= eta_0 and

\[
 D_0\le0,\qquad D_3\le0,\qquad D_H\ge0
                                     \quad(r_0<r<r_c),  \tag{5.3}
\]

then J(G_w) >= J(G_0) > 8 pi squared. The inner anisotropy has no
amplitude or derivative bound, apart from smoothness.

*Proof.* On the outer interval, the definition of V_w becomes

\[
 w''+\left(F'/F+3/r+2\phi'\right)w'+b_0(r,w)w=-V_w/F.
\]

Here b_0 extends smoothly across w = 0 and is uniformly bounded
by (5.2); the quotient sinh(aw)/w is bounded by a cosh(aK).
The terminal data w = w' = 0 are supplied by the full collar.
The elementary terminal-value estimate for this bounded first-order
system gives

\[
 \int_{r_c}^{R}r^3(w^2+(w')^2)\,dr
                      \le C\int_{r_c}^{R}r^3V_w^2\,dr.  \tag{5.4}
\]

One can apply Gronwall to the coefficients evaluated at the actual
solution w; only their bounds are used. Since c_0+z_0 <= Cw squared
on this fixed interval, the outer part of (5.1) is at least
2 integral V_w squared minus C eta integral(w squared+w' squared).
Choose eta_0 so that (5.4) absorbs the negative term. All terms of
(5.1) on the inner interval are nonnegative by (5.3). Finally G_0
is conformal to the genuine Kahler ordinary blowup K_{F,0}. I54's
whole-cell conformal bound, with exceptional area pi mu, gives

\[
 J(G_w)\ge J(G_0)\ge
       \frac{2\pi^2d(\mu+2)^2}{d-\pi^2\mu^2/2}
       +\frac14\int_C(s_{G_0}+4)^2
                    >8\pi^2.                           \tag{5.5}
\]

The denominator is the positive volume of the canonical Kahler cell.
In particular the bound is at least
8 pi squared + 8 pi squared mu + 2 pi squared mu squared. QED.

These hypotheses hold on a uniform, explicitly weighted profile
neighborhood of the low-cost recovery. On the inner region use the
uncut cscK profile F_mu of I54 and
\(p_\mu=\mu(\mu+2)/r^4\), and write F = F_mu+f. It suffices that

\[
\begin{split}
 |f''|+|f'|/r+|f|/r^2+|e^{2\phi}-1|
 +F|\phi''|+(|F'|+F/r)|\phi'|+F(\phi')^2
                                      \le p_\mu/10.     \tag{5.6}
\end{split}
\]

The definitions give
|D_0+p_mu|, |D_3+p_mu|, |D_H-p_mu| <= p_mu/2.
On the fixed outer interval a sufficiently small ordinary C2
neighborhood of the complete recovery, followed by sufficiently small
mu, gives (5.2). The radii and thresholds do not depend on mu.
This is a weighted second-derivative neighborhood, not a claim that
low energy automatically supplies those bounds.

If only (5.2) is known, keep the potentially negative inner payment

\[
 \mathfrak C_\mu=\int_{r_0}^{r_c}r^3
 \{4(D_0)_+F(w')^2+4(-D_H)_+c_0+2(D_3)_+z_0\}\,dr.
\]

The same proof gives J(G_w) >= J(G_0)-2 pi squared C_mu.
Thus an actual subthreshold cell in this outer regime necessarily has

\[
 \boxed{\mathfrak C_\mu>
       \frac{d(\mu+2)^2}{d-\pi^2\mu^2/2}-4
                                      \ge4\mu+\mu^2.}   \tag{5.7}
\]

The sign violations must correlate with actual anisotropy strongly
enough to pay this amount. Their mere occurrence is not a construction.
No bound of the reverse kind in (5.7) has been proved for arbitrary
profiles, and (5.2) has not been extracted from all low-energy cells.

## 6. The actual correlation in an almost-Kahler filling

For the nonconformal metric K itself, there is a geometric version
of the missing signed payment. Use the ordinary blowup, positive periods
t_i and relative first-Chern class of I54, Section 6.1. Locally choose
a J-anti-invariant two-form psi of squared norm two and write
\[
 \nabla\omega=\zeta\otimes\psi-J\zeta\otimes J\psi,\qquad
 n=\tfrac12|\nabla\omega|^2=2|\zeta|^2.
\]
The classical canonical Chern form is
\[
 \gamma=\operatorname{Rm}(\omega)-\zeta\wedge J\zeta,\qquad
 [\gamma]=2\pi c_1.
\]
These are formulas (21) and (25) in
[Apostolov--Armstrong--Draghici](https://faculty.fiu.edu/~draghici/research/paperfiles/Math-Ann.pdf).
Put
\[
 \xi=(\zeta\wedge J\zeta)^-,\quad |\xi|^2=n^2/8,\quad
 \beta=W^+(\omega)-(s/6+n/2)\omega,
\]
\[
 \rho'_0=(\operatorname{Ric}'-sK/4)(J\cdot,\cdot).
\]
Primes denote the J-invariant part; double primes denote the
J-anti-invariant part. In particular
\(|\operatorname{Ric}'_0|^2=2|\rho'_0|^2\). The actual form satisfies
\[
 (\gamma+\omega)^+=(s+n+4)\omega/4+\beta,\qquad
 (\gamma+\omega)^-=\rho'_0-\xi.
\]
On the full CH collar gamma + omega vanishes. After gluing the
unchanged closed CH exterior, its cohomology class has only exceptional
components. Thus, with \(C_E=\sum_i(2\pi+t_i)^2\),
\[
                    \int_C(\gamma+\omega)^2=-C_E.
\]
Expanding this identity and using
\(J(K)=2\int|\rho'_0|^2+\int|\operatorname{Ric}''|^2
+\tfrac14\int(s+4)^2\) gives
\[
 \boxed{\begin{split}
 J(K)={}&2C_E+\tfrac12\int(s+4)^2+\int\mathcal C\\
        &+2\int|\beta|^2+\int|\operatorname{Ric}''|^2,
 \end{split}}                                                   \tag{6.1}
\]
where the signed smooth density is
\[
 \mathcal C=2(\operatorname{Ric}+K)(\zeta^\#,\zeta^\#)
       +2(\operatorname{Ric}+K)((J\zeta)^\#,(J\zeta)^\#).
\]
Away from n = 0 it is
\(n\,\operatorname{tr}_{D^\perp}(\operatorname{Ric}+K)\),
where \(D^\perp\) is the two-plane spanned by zeta and J zeta.
The displayed smooth formula does not require extending that plane
across the zero set. Rotating psi rotates this pair, leaving the
density unchanged. Algebraically the term is
\(n(s+4)/2+4\langle\rho'_0,\xi\rangle\).

Consequently a genuinely subthreshold AK cell must have a sufficiently
negative torsion-weighted directional Ricci correlation. The integrated
nonintegrability N alone does not decide its sign. Nor does a small
exceptional period force N to vanish: a fixed compactly supported
compatible nonintegrable perturbation away from the shrinking bolt
retains positive N in the limit. Such an example pays the positive
cost of the background perturbation and is not subthreshold.
Equation (6.1) is a consequence of the classical canonical Chern
identity, not a new integrability theorem. Its analogue for arbitrary
conformal metrics retains the conformal terms in I54 rather than
silently identifying G with K.

## 7. Full coupled Hessian check at the low-cost recovery

The nonlinear result in Section 5 does not depend on a formal Taylor
expansion. The following separate calculation records why a quadratic
search near the entire cutoff recovery does not produce a missing
negative mode.

Choose fixed physical radii \(r_c<r_1<R\), cut the cscK profile
F_mu to CH between r_c and r_1, and write
\(s_{F_\mu}=-4+\delta_\mu\).
Then delta_mu is supported in that annulus with C1 norm O(mu).
Consider \(F=F_\mu+\epsilon f,\ \phi=\epsilon p,\ w=\epsilon z\),
with the actual fixed-bolt and collar conditions; in particular
f(r_0) = f'(r_0) = 0 and all variations vanish near R.
Put
\[
 \mathcal Sf=-f''-7f'/r-8f/r^2,\quad
 L_Fp=Fp''+(F'+3F/r)p'.
\]
For \(j=J/(2\pi^2)\), the even quadratic coefficient is
\[
 Q_{\mathrm{ev}}=\mathcal Q_{\mathrm{ev}}
 +\int r^3\{4\delta_\mu'fp'-4\delta_\mu F_\mu(p')^2
                                      +4\delta_\mu p^2\}\,dr,
\]
\[
 \mathcal Q_{\mathrm{ev}}=\int r^3
 \left\{\frac{(\mathcal Sf)^2}{6}
 +\frac{(\mathcal Sf-6L_{F_\mu}p+6p)^2}{3}
                            +4p^2+4F_\mu(p')^2\right\}\,dr.
                                                               \tag{7.1}
\]
This follows by expanding the exact even-sector expression
\[
 j=4-\frac{2d}{\pi^2}+\int r^3
       \{s_F^2/6+X^2/12+(X+4e^{2\phi})^2/4\}\,dr,
 \quad X=s_F-6L_F\phi-6F(\phi')^2.
\]
The integration by parts uses
\(\int r^3L_fp=[r^3fp']_{r_0}^{R}=0\).
The terminal ODE for S f on the fixed outer annulus controls its
H1 norm by the L2 norm of S f there. Consequently
\(Q_{\mathrm{ev}}\ge(1-C\mu)\mathcal Q_{\mathrm{ev}}\).

For the odd sector define
\[
 D_Fz=-Fz''-(F'+3F/r)z'+(16/(r^2F)-8/r^2)z.
\]
Its coefficient is
\[
 Q_{\mathrm{odd}}=\int r^3
 \{2(D_{F_\mu}z)^2-4E_VF_\mu(z')^2
                     +32E_Hz^2/r^2-64E_Vz^2/(r^2F_\mu)\}\,dr.
\]
In the cscK core \(E_V=-p_\mu,E_H=p_\mu\).
In the fixed transition annulus these two defects are O(mu).
The terminal ODE estimate, now for D_F z, therefore gives
\[
\begin{split}
 Q_{\mathrm{odd}}\ge{}&(2-C\mu)\int r^3(D_{F_\mu}z)^2\,dr\\
 &+\int_{r_0}^{r_c}r^3p_\mu
       \{4F_\mu(z')^2+32z^2/r^2+64z^2/(r^2F_\mu)\}\,dr.
\end{split}                                                     \tag{7.2}
\]
Mixed even--odd second derivatives vanish because the full functional
is even in w. Thus the coupled quadratic form is positive for small mu.
The linear derivative is
\[
 Dj[f,p,z]=\int r^3\delta_\mu
                           (\mathcal Sf-4L_{F_\mu}p+4p)\,dr.
\]
It is bounded by \(C\mu\sqrt{\mathcal Q_{\mathrm{ev}}}\);
quadratic optimization can save only O(mu squared), whereas
\[
 j(F_\mu,0,0)=(\mu+2)^2+\tfrac12\int r^3\delta_\mu^2\,dr
                                      =4+4\mu+O(\mu^2).
\]
This is a statement about the quadratic model. Finite deformations
are justified only under Section 5's actual nonlinear hypotheses.
The search tool fixes its cutoff in logarithmic coordinates instead;
its moving physical transition does not automatically inherit these
fixed-annulus uniform constants.

## 8. A global radial moment: the entire nonconformal triaxial class

There is a stronger exclusion than the neighborhood result in Section 5.
It uses one integral of the complete Ricci residual, not monotonicity
under symmetrization. In the same ordinary-bolt class let
\(\mu=r_0^2>0\), and choose R in the unchanged CH collar. No bound on
F,w,phi or their derivatives is assumed, apart from positivity and the
smooth bolt and collar conditions.
In particular \(w=(r-r_0)^2\widetilde w(r)\) and phi is smooth
in r at the bolt, as in the smooth profile class of I54.
Define
\[
 A_0=D_0-2F(w')^2,\qquad A_3=D_3-z_0,\qquad A_H=D_H+c_0,
 \qquad V_w=U-2F\phi'w',
\]
\[
 X=2A_H-A_0-A_3,\qquad Y=A_0+A_3+2A_H,
 \qquad Z=A_0-A_3.
\]
Here Y is exactly \(e^{2\phi}(s_G+4)\). Put
\[
\begin{split}
 I_R&=\int_{r_0}^Rr^{-5}\,dr
                  =\tfrac14(\mu^{-2}-R^{-4}),\\
 P_w&=\int_{r_0}^R\left\{
    \frac{2F(w')^2}{r}+\frac{8(\cosh(2w)-1)}{r^3}
                 +\frac{8\sinh^2(2w)}{r^3F}\right\}\,dr,\\
 T_\phi&=2\int_{r_0}^R\frac{F(\phi')^2}{r}\,dr,
 \qquad M=1+2/\mu+P_w-T_\phi .
\end{split}                                                     \tag{8.1}
\]
These are integrals of the actual profiles. Both P_w and T_phi are
nonnegative and finite for smooth bolt data.

**Proposition 5.** Every such conformal triaxial filling satisfies
\[
\boxed{\begin{split}
 \frac{J(G)}{2\pi^2}={}&\frac{M^2}{4I_R}
 +\frac14\int_{r_0}^R r^3
                    \left(X-\frac{M}{I_Rr^4}\right)^2dr\\
 &+\frac14\int_{r_0}^Rr^3Y^2dr
  +\frac12\int_{r_0}^Rr^3Z^2dr
  +2\int_{r_0}^Rr^3V_w^2dr .
\end{split}}                                                    \tag{8.2}
\]
In particular the whole nonconformal class \(\phi=0\), including
arbitrary finite triaxial anisotropy and arbitrary positive F, obeys
\[
 \boxed{\frac{J(K_{F,w})}{2\pi^2}
 \ge\frac{(\mu+2+\mu P_w)^2}{1-\mu^2/R^4}>4.}           \tag{8.3}
\]

*Proof.* Direct substitution in the actual residual gives
\[
\begin{split}
 X={}&F''+3F'/r-8(F-1)/r^2
       +2(F\phi')'-2F\phi'/r-2F(\phi')^2\\
    &+2F(w')^2+2c_0+z_0 .
\end{split}
\]
After multiplication by 1/r, its conformal linear terms are exactly
\(2(F\phi'/r)'\). Their boundary values vanish: F = 0 at the
bolt, phi is radially smooth there, and phi = 0 on the full collar.
The F terms have integral
\[
 \left[F'/r+4F/r^2\right]_{r_0}^R
                    +8\int_{r_0}^Rr^{-3}dr=1+2/\mu.
\]
This uses F'(r_0) = 2/r_0 and the exact outer values
F(R) = 1+R squared/6, F'(R) = R/3. Hence
\(\int X/r=M\). Pointwise,
\[
 A_0^2+A_3^2+2A_H^2=(X^2+Y^2)/4+Z^2/2.
\]
Projecting X in \(L^2(r^3dr)\) onto the single function r to
the power minus four proves (8.2). Set T_phi = 0 for (8.3). QED.

This result excludes the whole diagonal almost-Kahler class itself,
not only small anisotropy or favorable D signs. It does not contradict
the earlier descending plateau: a decrease from one high-cost metric
to another need not cross the threshold four. It also does not prove
the corresponding result for all conformal factors.

More generally put
\[
 \delta_{\mu,R}=1+\frac2\mu
                  \left(1-\sqrt{1-\mu^2/R^4}\right)>1.
\]
The entire class with \(T_\phi-P_w\le\delta_{\mu,R}\) has
J greater than 8 pi squared. Indeed M is then at least
\(2\mu^{-1}\sqrt{1-\mu^2/R^4}>0\), and (8.2) gives the
nonstrict bound; equality would require X = M/(I_R r to the fourth)
on the full collar, where the actual residual X vanishes.

Thus every actual subthreshold conformal cell necessarily satisfies
\[
 \boxed{1+\frac2\mu\left(1-\sqrt{1-\mu^2/R^4}\right)
 < T_\phi-P_w
 <1+\frac2\mu\left(1+\sqrt{1-\mu^2/R^4}\right).}         \tag{8.4}
\]
It must also make all four remaining squares in (8.2) small enough
simultaneously. This is a complete signed integral restriction on
actual metrics, not a formal choice of four independent variables.
For a fixed improvement \(J/(2\pi^2)\le4-\epsilon\), where
\(0<\epsilon<4\), the sharper necessary condition is
\[
 \mu(T_\phi-P_w)\ge
        \mu+2-\sqrt{4-\epsilon}\sqrt{1-\mu^2/R^4}.       \tag{8.5}
\]
Thus along mu tending to zero a fixed improvement requires a net
weighted conformal gradient budget of order at least mu inverse.
Merely entering the interval (8.4) by a bounded amount does not
produce such an improvement. This is a requirement on complete smooth
one-bolt cells; it is not a theorem decomposing an arbitrary multi-core
filling into separately chargeable one-bolt regions.
Controlling that middle interval from the scalar, radial and anisotropic
equations is still open. The radial identity
\[
 Z=-2F\{\phi''-\phi'/r-(\phi')^2+(w')^2\}+z_0
\]
is retained rather than treating Z as a freely assignable residual.

### 8.1 Scalar coupling and an actual zero-moment test

The scalar equation supplies a second integral, but not a bound on
T_phi alone. Set
\[
 G_\phi=\int r^3F(\phi')^2dr,\qquad
 B_\phi=\int r^3(e^{2\phi}-1)dr,\qquad n=N/(2\pi^2).
\]
The scalar identity of I54 and the vanishing endpoint term
\([r^3F\phi']=0\) give
\[
 L_Y:=\int r^3Ydr=4B_\phi-\mu^2-2\mu-n-6G_\phi,
 \qquad \mu^2T_\phi/2\le G_\phi\le R^4T_\phi/2.         \tag{8.6}
\]
Thus the Y-square in (8.2) splits exactly into
\[
 \frac{L_Y^2}{R^4-\mu^2}
 +\frac14\int r^3
           \left(Y-\frac{4L_Y}{R^4-\mu^2}\right)^2dr.    \tag{8.7}
\]

The main radial moment M can nevertheless vanish on genuine smooth
metrics. Take the complete cutoff Kahler recovery F_mu with fixed
physical cutoff radius, w = 0, and a nonzero
\(\eta\in C_c^\infty((2,3))\). For sufficiently small mu put
\[
 C_\mu=2\int_2^3F_\mu(\sqrt\mu x)(\eta'(x))^2/x\,dx,
 \qquad a_\mu^2=(\mu+2)/C_\mu,
 \qquad \phi(r)=a_\mu\eta(r/\sqrt\mu).
\]
Here C_mu tends to the positive integral with F replaced by
\(1-x^{-2}\). The metric is smooth and preserves both the bolt
and full CH collar. Direct change of variable gives
\[
             P_w=0,\qquad T_\phi=1+2/\mu,\qquad M=0.
\]
Its entire cost remains uniformly bounded: the perturbation is supported
on a region of volume O(mu squared), and its curvature is O(mu inverse)
with uniformly controlled rescaled profiles. It is still conformal to
a genuine Kahler cell, so its cost is strictly greater than 8 pi squared
by I54. In (8.2) that positive cost is carried by the remaining squares.
In particular neither a bound on M away from zero nor the universal
inequality T_phi <= P_w + 1 can finish the conformal problem. The missing
estimate must couple the full scalar variance, Z and V_w, rather than
discard them after taking the two moments.

## 9. A two-scale requirement for any fixed improvement

The radial moment and the actual almost-Kahler transfer restrict where
the remaining conformal payment could occur. This goes beyond choosing
formal values of T_phi and P_w.

**Proposition 6.** Fix R and \(0<\epsilon<4\). Suppose a sequence
of the complete cells in Section 8 has mu tending to zero and
\(j=J/(2\pi^2)\le4-\epsilon\). For every \(0<\alpha<1/4\),
\[
 \mu T_{\phi,\{r\ge\mu^\alpha\}}\longrightarrow0,
 \qquad
 \liminf\mu T_{\phi,\{r\le\mu^\alpha\}}
                       \ge2-\sqrt{4-\epsilon}>0.         \tag{9.1}
\]
At the same time the complete metric changes cannot be confined to
a CH background region whose volume tends to zero.

*Proof.* Use normalized quantities
\[
 d=R^4/4,\qquad v=(R^4-\mu^2)/4,\qquad
 m=R^4+2\mu,\qquad n=N/(2\pi^2).
\]
These equal the quantities of I54 divided by 2 pi squared; this
normalization is confined to this section. The conformal transfer
remainder is not discarded: with u = exp(-phi),
\[
 \frac{6\int|du|_G^2dV_G}{2\pi^2}
                       =6\int r^3F(\phi')^2dr=6G_\phi.
\]
The actual scalar and Weyl bounds of I54 therefore give
\[
 j\ge4-4d+
       \frac{(m+n+6G_\phi)^2+2(m-2n)^2}{12v}.
\]
The omitted term is \(\int(s_G+4)^2/(8\pi^2)\ge0\).
The exact algebraic decomposition
\[
 (m+n+6G)^2+2(m-2n)^2
             =9\left(n-\frac{m-2G}{3}\right)^2+2(m+4G)^2
\]
implies
\[
 0\le G_\phi\le
             \frac{\sqrt{24dv-6\epsilon v}-m}{4}=O_R(1). \tag{9.2}
\]
If the radicand or right side is negative, the hypothesized cell is
already excluded. On the exterior of any canonical radius rho,
\[
 T_{\phi,\{r\ge\rho\}}\le2G_\phi/\rho^4.
\]
Take rho = mu to the power alpha. The first conclusion in (9.1)
follows because 1 - 4 alpha is positive. Equation (8.5), together
with P_w nonnegative, supplies the lower bound on mu T_phi; subtract
the vanishing exterior contribution to obtain the second conclusion.

Finally, if all changes were confined to a CH region of background
volume d_s tending to zero, the general complete-cell inequality in
I54 would give
\(J\ge8\pi^2-4d_s/3\), contradicting the fixed improvement.
More precisely it requires \(d_s\ge3\pi^2\epsilon/2\).
This last bound concerns the entire modified background, not the
canonical size of the exceptional bolt. QED.

Consequently a putative fixed improvement in this class needs both
a microscopic conformal payment and a nonvanishing-scale modification
of the full geometry. A small-support conformal bubble alone cannot
provide it; neither can a uniformly bounded weighted conformal gradient
on the shrinking canonical scales. The proposition does not classify
the transition or prove that the two required mechanisms cannot coexist.
That simultaneous compatibility, including all the squares of (8.2),
is the remaining construction test in this class.


END COMPLETE SOURCE


---

## Source 3: 20260928_signed_characteristic_selection.md

Original path: `continuation/20260928_signed_characteristic_selection.md`

SHA-256: `f16ea6c525d26d9ec700cc883fe2706788eb276b3371a8485789c3eaef8a760d`

BEGIN COMPLETE SOURCE

# Signed characteristic mass and the missing bulk selection

28 September 2026. Continuation from `0fb009c`. The first-order target is
still the infimum over all metrics on the original balanced family. This
text identifies exactly what I55's measurable bulk selection requires,
supplies it in a classical Kähler setting, and tests its necessity with
actual smooth metrics. In particular, a competitive energy bound is not
enough to impose that selection, even after constant-scalar normalization.
This does not produce a coefficient below four.

## 1. The signed measure behind I55

Use the complex orientation on

\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
 \qquad A=c_1^2(X),\quad Q=k+4\ell,\quad h=Q/A,
\]

where X is one of the complex-hyperbolic covers already used in the
actual family. All curvature norms have the conventions of I54--I55.
For any smooth metric put

\[
 f_g=\frac{s^2/12+4|W^+|^2-|\operatorname{Ric}^{\circ}|^2}{8\pi^2},
 \quad N(g)=\int_M(f_g)_-,\quad T_U=\int_U f_g.
 \tag{1.1}
\]

Chern--Weil gives \(T_M=A-Q\). N is the negative mass of this particular
Levi-Civita characteristic density, not an ADM mass, a characteristic
number by itself, or the torsion energy denoted N in earlier cell formulas.
Let \(R=\int|\operatorname{Ric}|^2\), \(P=\int|\operatorname{Ric}^{\circ}|^2\),
and \(L_s=\int(s-\bar s)^2\). Then

\[
 \mathcal E=\frac{4P+L_s}{R},\qquad 8\pi^2N\le P.
 \tag{1.2}
\]

Consider h tending to zero and competitive actual metrics
\(\mathcal E=O(h)\). The classical Ricci lower bound in this family is
\(R\ge8\pi^2(A+Q)\). The signature formula gives

\[
 \int|W^+|^2\ge12\pi^2\tau
   =4\pi^2A/3-12\pi^2k.
\]

Combining it with
\(R=4P-12\int|W^+|^2+24\pi^2(A-Q)\) and \(4P\le\mathcal E R\)
proves

\[
 R=8\pi^2A+O(Q),\qquad P+L_s=O(Q),\qquad N=O(Q).
 \tag{1.3}
\]

These are bounds on actual metrics, not an optimization of formal curvature
moments. They use the classical lower bound already supplied in I44.

**Proposition 1.** In this competitive regime the following conditions
are equivalent:

\[
 \begin{split}
 &\text{there are measurable }U_j\text{ with }
 T_{U_j}=A_j+o(Q_j),\quad R_{U_j}=8\pi^2A_j+o(A_j);\\
 &N(g_j)\ge Q_j-o(Q_j).
 \end{split} \tag{1.4}
\]

The first condition is precisely the intrinsic sufficient interface in
[I55, Section 4.1](20260928_localization_and_coupled_filling.md).

*Proof.* Necessity follows from
\(T_{M\setminus U}=-Q+o(Q)\). For sufficiency choose a measurable
\(C\subset\{f<0\}\) with negative mass \(\min(N,Q)\). Such a set exists
because the finite measure \((f)_-dV\) has no atoms. On \(\{f<0\}\),
\(s^2/12\le|\operatorname{Ric}^{\circ}|^2\), so
\(|\operatorname{Ric}|^2\le4|\operatorname{Ric}^{\circ}|^2\).
Consequently \(R_C=O(Q)\). For \(U=M\setminus C\), (1.3) now gives
both required estimates. QED.

The coefficient consequence can also be seen immediately from (1.2):
(1.4) implies \(\liminf\mathcal E/h\ge4\). I55 adds its equality
information. Neither argument proves (1.4) from competitiveness.

## 2. A genuine supplier from holomorphic Morse inequalities

For this section let \(M=\operatorname{Bl}_k X\) with its specified complex
structure, with no handles, and X a closed complex-hyperbolic surface.
For every smooth Hermitian metric on the canonical line bundle write
\(\Theta=(i/2\pi)F_{K_M}\). The weak holomorphic Morse inequality gives

\[
 \limsup_{m\to\infty}\frac{2h^1(M,K_M^m)}{m^2}
 \le\int_{M(\Theta,1)}-\Theta^2. \tag{2.1}
\]

Here \(M(\Theta,1)\) is the locus with one positive and one negative
curvature eigenvalue. The classical input, including its signature
convention, is [Demailly, equations (1.11)--(1.12)](https://arxiv.org/html/1003.5067).
Only the inequality is needed, not a converse or a conjectured equality.

In the present case the left side is exactly k. Indeed K_X is ample,
Kodaira vanishing and Riemann--Roch give

\[
 h^0(X,K_X^m)=\frac{A}{2}m(m-1)+\chi(\mathcal O_X),\qquad m\ge2.
\]

Pluricanonical sections and \(\chi(\mathcal O)\) are unchanged by blowup,
while \(K_M^2=A-k\). Serre duality gives \(h^2(M,K_M^m)=0\): an
antipluricanonical effective divisor would have negative pairing with
the pullback of the ample K_X. Thus

\[
 h^1(M,K_M^m)=\frac{k}{2}m(m-1),\qquad
 \int_{M(\Theta,1)}-\Theta^2\ge k. \tag{2.2}
\]

If g is Kähler, its induced canonical curvature is minus the Ricci
form divided by \(2\pi\). Squaring removes that sign. The Kähler
identity \(|W^+|^2=s^2/24\) gives

\[
 \Theta^2=\frac{s^2/4-|\operatorname{Ric}^{\circ}|^2}{8\pi^2}\,dV
          =f_g\,dV.
\]

The signature-one set is exactly the negative-density set. Hence

\[
 \boxed{N(g)\ge k\quad\text{for every Kähler metric on }\operatorname{Bl}_k X.}
 \tag{2.3}
\]

This is a consequence of classical holomorphic Morse theory, not a new
Morse theorem. It supplies spatially signed curvature information, in
addition to the familiar integrated Ricci lower bounds. Applying
Proposition 1 proves the I55 selection for competitive Kähler sequences
in this pure-blowup class. Handles and non-Kähler metrics are not covered.
For a conformally Kähler metric the canonical Chern curvature still
satisfies (2.2), but it is no longer the density (1.1). The distinction
is essential in the following construction.

## 3. An exact radial primitive and an actual loss of negative mass

Take the ordinary one-bolt metric K_F of I54, with
\(r\ge r_0=\sqrt\mu\), volume element \(2\pi^2r^3dr\),
\(F(r_0)=0\), \(F'(r_0)=2/r_0\), and a full CH outer collar.
For \(G=e^{2\phi}K_F\), define

\[
 q=2F+\frac{rF'}2+rF\phi'-2,\qquad
 B=q^2+(2+q)r^2F(\phi')^2.
 \tag{3.1}
\]

Direct substitution of the conformal Ricci eigenvalues gives the exact
identity

\[
 \boxed{\int_{\{r\in[a,b]\}} f_G\,dV_G=B(b)-B(a).} \tag{3.2}
\]

For a reproducible derivation, let
\(r_v=-F''/2-5F'/(2r)\), \(r_h=-F'/r+4(1-F)/r^2\). The three scaled
Ricci eigenvalues, the horizontal one having multiplicity two, are

\[
\begin{split}
 A_0&=r_v-3F\phi''-(2F'+3F/r)\phi',\\
 A_3&=r_v-F\phi''-(2F'+5F/r)\phi'-2F(\phi')^2,\\
 A_H&=r_h-F\phi''-(F'+5F/r)\phi'-2F(\phi')^2.
\end{split}
\]

Put \(S=A_0+A_3+2A_H\). Conformal Weyl invariance and
\(s_{K_F}=2(r_v+r_h)\) reduce the density to

\[
 B'=\frac{r^3}{4}\left\{\frac{S^2}{12}
 +\frac{[2(r_v+r_h)]^2}{6}
 -\left(A_0^2+A_3^2+2A_H^2-\frac{S^2}{4}\right)\right\}.
 \tag{3.3}
\]

Expansion proves (3.2); the checking program independently verifies the
identity for arbitrary smooth F and phi. At an ordinary smooth bolt
B=1; on a CH collar B=r^4/4. Thus the relative characteristic integral
is correct at both ends, including its normalization.

For the uncut constant-scalar recovery metric use

\[
 F_\mu=1+\frac{r^2}{6}-\frac{c}{2r^2}+\frac{\mu^3}{3r^4},
 \qquad c=\mu(\mu+2).
\]

It has s=-4 and
\(q_0=(r^2-c/r^2)/2\). The function \(B_0=q_0^2\) decreases from one
to zero at \(r_*=c^{1/4}\), then increases. Its negative mass is exactly
one. Equivalently \(8\pi^2f=4(1-c^2/r^8)\), and direct integration
on \([\sqrt\mu,r_*]\) gives one.

Fix a small positive mu. Choose smooth eta supported near r_* with
\(\eta'(r_*)\ne0\), and set \(\phi=\varepsilon\eta\). The nondegenerate
minimum persists. Its position first shifts so as to cancel the linear
change in q; the remaining value is

\[
 \min B_\varepsilon
 =2r_*^2F_\mu(r_*)\eta'(r_*)^2\varepsilon^2+O_\mu(\varepsilon^3)>0.
 \tag{3.4}
\]

Cut F_mu to CH in a fixed annulus outside r_* where B_0' is strictly
positive. For sufficiently small mu that cutoff remains C2-close to
CH on the annulus, so its density is positive there. Small epsilon
preserves the single inner minimum and creates no additional negative
density outside. The complete smooth cell therefore satisfies

\[
 N(G_\varepsilon)=1-\min B_\varepsilon<1. \tag{3.5}
\]

Its cost J is still strictly above \(8\pi^2\), by I54's complete
conformal-Kähler estimate. It is not a cheaper cell.

Holding mu and epsilon fixed, repetition in covers with k/A tending
to zero gives actual closed metrics with \(\mathcal E=O(k/A)\) but
\(N/k<1\) by a fixed amount. The exact repetition formula is I54 (2.1).
Thus competitiveness alone does not supply Proposition 1, already in
the pure-blowup family.

The fixed-mu qualification cannot be dropped. If the perturbation is
confined to \(r\asymp\mu^{1/4}\) while mu tends to zero, B_0 at the
support boundaries is O(mu). The accumulated negative variation is
then already at least \(1-O(\mu)\). Formula (3.4) is not uniform for a
fixed perturbation amplitude in that limit; new shoulder minima can
appear. In particular this argument does not refute selection for
shrinking near-minimizers.

## 4. Constant-scalar cells and the original balanced family

The conformal bump in Section 3 disappears under Yamabe minimization
of its original conformal class. A separate construction is needed to
test the scalar-minus-four formulation of the selection target.

### 4.1 A scalar-minus-four cell with N less than one

On a fixed truncation of K_{F_mu}, solve the radial equation

\[
 (r^3F_\mu u_a')'=\frac23r^3(u_a^3-u_a),\qquad
 u_a(r_0)=1+a,\qquad (r^3F_\mu u_a')(r_0)=0. \tag{4.1}
\]

It is the conformal scalar equation for \(u_a^2K_{F_\mu}\) to have
s=-4. Smooth bolt regularity gives a smooth local solution and smooth
dependence on a; for fixed mu and fixed finite outer radius it stays
positive for sufficiently small a. For a>0 it initially exceeds one,
and the integrated equation shows that it increases, so \(u_a'(r_*)>0\).
Differentiating at a=0 gives \(v(r_0)=1\) and

\[
 (r^3F_\mu v')'=\frac43r^3v,\qquad v'(r_*)>0.
\]

Use \(\phi_a=\log u_a\) in (3.1). The same minimum calculation now gives

\[
 N_{\rm inner}=1-2r_*^2F_\mu(r_*)v'(r_*)^2a^2+O_\mu(a^3)<1.
 \tag{4.2}
\]

This inner metric is not CH on its outer collar. To complete it without
changing its inner region or its scalar curvature, apply
[Delay, Theorem 1.1 and Propositions 2.2--2.5](https://arxiv.org/html/1003.5146)
on a fixed annulus. The theorem glues sufficiently close smooth
metrics with a smooth supported correction, interpolating their scalar
curvatures, provided the reference adjoint scalar operator has no kernel.

That nondegeneracy holds for CH. In geometric Laplacian convention a
kernel function satisfies
\(\operatorname{Hess}f-(\Delta f)g+fg=0\), hence
\(\operatorname{Hess}f=(f/3)g\). Commuting derivatives forces every
sectional curvature of a plane containing a nonzero gradient to equal
-1/3. CH has different holomorphic and totally real sectional
curvatures at every point, so the gradient vanishes and then f=0.
The uniform nearby inverse in Delay's proposition permits the small
inner metric as reference as well.

Choose mu sufficiently small that K_{F_mu} is close to CH on the fixed
annulus, then choose a sufficiently small. Both metrics have scalar -4,
so the glued metric has scalar -4 everywhere. The correction tends to
zero in C2 with the annular data; the annulus retains f>0, since CH has
strictly positive f there. Consequently the completed cell has

\[
 s=-4,\qquad N_C=1-\delta<1,\qquad J_C<\infty. \tag{4.3}
\]

We can also choose \(J_C>8\pi^2\). At a=0 the unchanged inner core
already has cost \(8\pi^2+8\pi^2\mu+O(\mu^2)\) when truncated at a fixed
radius; the remainder contributes nonnegative cost. Choose a smaller
if necessary and use continuous dependence. Parameters are now fixed,
not sent to zero together with h.

### 4.2 Adding handles while retaining the negative-mass loss

Insert k_j copies of (4.3) into disjoint ball lifts in X_j. This produces
a closed scalar-minus-four metric B_j on \(X_j\#k_j\overline{\mathbb{CP}}^2\),
equal to CH away from the cells, and
\(N(B_j)=k_j(1-\delta)\). There are enough disjoint lifts because
\(k_j/A_j\to0\).

For each fixed j add the required ell_j handles by the classical
shrinking scalar-flat conformally-flat neck construction. All necks
are placed in the unchanged CH region. Denote the resulting metric
by g_{j,e}. The construction, with all transition regions included,
has the following fixed-j limits:

\[
 \begin{split}
 &g_{j,e}\longrightarrow B_j\quad\text{smoothly off the finitely many mouths},\\
 &\operatorname{Vol}(g_{j,e})\longrightarrow\operatorname{Vol}(B_j),
 \quad\int s_{g_{j,e}}^2\longrightarrow16\operatorname{Vol}(B_j),\\
 &R(g_{j,e})\longrightarrow R(B_j)+32\pi^2\ell_j.
 \end{split} \tag{4.4}
\]

Here the scalar curvature can be bounded independently of e for each
fixed j. A scaled scalar-flat neck has zero scalar curvature. Cut its
Euclidean-end error at radius equal to the square root of the neck
scale: its second-derivative error is O(1), the CH Taylor error also
gives O(1), and the transition volume tends to zero. The inserted
self-dual Weyl energy tends to zero. The last limit in (4.4) follows
from the relative identity I54 (1.1), with handle weight four. These
are exactly the classical shrinking handles already used in I44,
not a new scalar-curvature gluing theorem for handles.

Take the negative Yamabe representative \(\widehat g_{j,e}=u_{j,e}^2g_{j,e}\)
with scalar -4. Such a representative exists by the same all-metric
actual positive supply as before; no new monopole solution on a
manifold with boundary is being assumed. For fixed j the scalar lower
bound and maximum principle bound u uniformly from above. Interior
elliptic estimates give subsequential smooth convergence away from
the mouths. The limit extends across those points: it is a bounded
solution of a semilinear elliptic equation on the smooth B_j.

The limit is not zero. The actual scalar bound gives
\(16\operatorname{Vol}(\widehat g_{j,e})\ge32\pi^2A_j\), whereas the
uniform upper bound on u makes the volume of the disappearing necks
negligible. The strong maximum principle makes the limiting solution
positive. Uniqueness of the scalar-minus-four representative in a
negative conformal class then forces this limit to be one. Therefore

\[
 u_{j,e}\longrightarrow1\text{ locally smoothly off the mouths},\qquad
 S(g_{j,e})-S(\widehat g_{j,e})\longrightarrow0. \tag{4.5}
\]

The exact conformal identities of I41 now imply
\(R(\widehat g_{j,e})\to R(B_j)+32\pi^2\ell_j\). Subtract the convergent
energies on the complement of small fixed balls, then let those ball
radii shrink. The total remaining P-energy tends to
\(32\pi^2\ell_j\). Since \(8\pi^2N\le P\) on every measurable region,

\[
 \limsup_{e\to0}N(\widehat g_{j,e})
 \le k_j(1-\delta)+4\ell_j. \tag{4.6}
\]

Choose a diagonal e_j so that all fixed-j errors in (4.4)--(4.6) are
o(Q_j). The topology is now exactly the original balanced M_j, with
its inherited actual conformal/weight supply and class-square budget.
Since \(k_j/Q_j\to2/9\), the resulting metrics satisfy

\[
 \boxed{s_{g_j}=-4,\qquad \mathcal E(g_j)=O(h_j),\qquad
 \limsup\frac{N(g_j)}{Q_j}\le1-\frac{2\delta}{9}<1.} \tag{4.7}
\]

Thus Proposition 1's bulk selection does not follow even from the
constant-scalar competitive inputs on the original balanced family.
This is a failure of that stronger proposed intermediate statement,
not a failure of I55 with its hypotheses.

For completeness, the same fixed-j energy limits give

\[
 \frac{\mathcal E(g_j)}{h_j}
 \longrightarrow\frac{28}{9}+\frac{J_C}{9\pi^2}>4. \tag{4.8}
\]

The actual sequence is not asymptotically minimizing: the inherited
upper bound has coefficient at most four. It therefore does not
answer the unrestricted coefficient problem or refute selection for
sequences whose excess over the actual infimum is o(h).

## 5. The compensation that a sharp argument must retain

The sign partition gives an exact nonnegative remainder

\[
 Z(g)=\int_{\{f\ge0\}}|\operatorname{Ric}^{\circ}|^2
       +\int_{\{f<0\}}\left(\frac{s^2}{12}+4|W^+|^2\right),
 \qquad P=8\pi^2N+Z. \tag{5.1}
\]

Consequently

\[
 \mathcal E=\frac{32\pi^2N+4Z+L_s}{R},\qquad
 \frac{\mathcal E}{h}
 =\frac{4N}{Q}+\frac{Z}{2\pi^2Q}+\frac{L_s}{8\pi^2Q}+o(1)
 \tag{5.2}
\]

on every competitive sequence. This is an identity, not another
independent coercivity theorem. It explains why losing negative mass
need not lower the defect. The scalar-minus-four examples above lose
mass and pay a larger nonnegative Z remainder.

For the actual variational target, I41 permits replacing near-minimizers
by their negative Yamabe representatives. In this reduced class the
coefficient-four lower bound is equivalent to the still unproved
compensated inequality

\[
 Z(g_j)\ge8\pi^2\bigl(Q_j-N(g_j)\bigr)-o(Q_j).
 \tag{5.3}
\]

When N already exceeds Q the inequality is automatic; otherwise its
content is the payment by the rest of the actual curvature. Equation
(4.7) shows why one cannot simply delete this case. The genuinely
remaining alternatives are to prove (5.3) from actual geometry or
the actual field equations, to supply the stronger selection only
for true near-minimizers, or to construct a complete cell/sequence
whose total first-order cost is below four. No such sequence is
constructed here. The unrestricted weak zero-Weyl endpoint is also
unchanged by these arguments.

### 5.1 A necessary degeneration property of actual near-minimizers

There is a variational consequence that goes beyond relabelling (5.3).
Fix a nontrivial marked cell C of I54, with q>0 and a fixed open CH
collar. Let K be a compact family in the C4 topology consisting of
smooth positive metrics on C, all with that fixed collar. Allow a
finite union of such families on finitely many fixed cell types.

**Proposition 2.** Let g_j be scalar-minus-four metrics on the original
balanced M_j with

\[
 \mathcal E(g_j)-\alpha_j=o(h_j),\qquad
 \alpha_j=\inf_{g\text{ on }M_j}\mathcal E(g).
 \tag{5.4}
\]

If g_j contains n_j disjoint marked full-collar cells whose pullback
metrics lie in K, then \(n_j=o(Q_j)\).
No hypothesis that a smooth global minimizer exists is used.
More strongly, there is a fixed C4 neighborhood of K with the same
conclusion. The actual cells in this neighborhood need not themselves
have exact CH collars; all variations are supported away from their
boundaries.

*Proof.* The inherited upper bound on alpha_j and (5.4) first give
\(\mathcal E(g_j)=O(h_j)\). Every cell in K has positive J: zero would make it Einstein,
contradicting I54's topology and open-collar argument. Compactness and
continuity give \(J\ge j_0>0\). Since the initial metrics have s=-4,
their cell J equals P. Equation (1.3) therefore gives n_j=O(Q_j).

I54, Proposition 2 proves that every smooth nontrivial
full-CH-collar cell has a compactly supported smooth metric variation
strictly decreasing J. For each metric in K choose one sufficiently
small finite variation. Continuity in the initial metric makes that
same variation decrease J by a fixed positive amount on a neighborhood.
A finite subcover of K therefore supplies a uniform number d>0 and
finitely many variations such that each cell can be changed with
\(\Delta J\le-d\). Their changes in volume, scalar integral and Ricci
energy are uniformly bounded. All modified metrics remain positive
and keep the complete collar.

Apply those changes simultaneously on the n_j disjoint cells. Put
\(v=\Delta V\), \(i=\Delta\int s\), \(r=\Delta R\). Their absolute
values are O(n_j), and

\[
 \Delta J=r+2i+4v\le-d n_j.
\]

The actual identity \(\mathcal E=4-I^2/(VR)\), expanded at
\(I=-4V\), \(R=4V+P\), gives

\[
 \mathcal E(g'_j)-\mathcal E(g_j)
 =\frac{4\Delta J}{R}
  +O\left(\frac{h_jn_j}{A_j}+\frac{n_j^2}{A_j^2}\right).
 \tag{5.5}
\]

For example, its linear remainder is exactly \(-4Pr/R^2\); the
remaining terms are quadratic in the finite moment changes. Bounds
(1.3), scalar -4 and \(n_j/A_j=O(h_j)\) justify the uniform expansion.
Consequently, for some d'>0 and all large j with n_j>0,

\[
 \mathcal E(g'_j)\le\mathcal E(g_j)-d' n_j/A_j.
\]

Although the varied metric need not retain constant scalar curvature,
it is an allowed competitor for alpha_j. Combining this inequality
with (5.4) proves n_j=o(Q_j). QED.

The neighborhood assertion follows from the same finite subcover:
positivity of J, admissibility of the finitely many supported variations,
the strict J decrease and their moment bounds all persist in a
sufficiently small C4 neighborhood of K. The actual metric is untouched
at its boundary, so no new matching argument is needed.

Thus the fixed smooth cells responsible for (4.7) cannot persist with
positive Q-density in a true near-minimizer. A positive-density cell
description of such a sequence, if one exists, must leave every fixed
smooth compact family, vary its collar/scale, or change its geometric
decomposition. The proposition does not extract any cell description,
nor give a uniform descent rate for degenerating cells. That rate,
measured against the missing characteristic mass rather than merely
the number of cells, is a remaining route to (5.3).

## 6. Verification and next use

`tools/check_signed_characteristic_mass.py` checks (3.3), the recovery
primitive and its exact negative mass, the minimum's quadratic
coefficient, and the Kähler/Riemann--Roch normalizations. Its actual
complete-cell integration at mu=0.01, outer radius 2.5 and epsilon=0.01
gives N=0.999973955691314 and J/(2 pi squared)=4.077939349922743.
The numerical receipt illustrates Section 3, not the constant-scalar
existence theorem, which uses (4.1), localized scalar deformation and
the fixed-j limiting proof.

The two primary external inputs are Demailly's weak holomorphic Morse
inequality and Delay's localized scalar gluing theorem. The SW supply,
shrinking handles, conformal energy identities, and cover dilution are
inherited with their original assumptions. No full concentration
decomposition, geometric compactness, or universal near-minimizer
classification has been inferred from these inputs.


END COMPLETE SOURCE
