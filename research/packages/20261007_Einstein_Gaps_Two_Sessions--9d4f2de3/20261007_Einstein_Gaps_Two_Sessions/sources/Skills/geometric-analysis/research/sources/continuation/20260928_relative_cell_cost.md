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
