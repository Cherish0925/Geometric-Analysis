# Integral shear balancing and a closed Einstein--Hilbert variation

## 1. Question and result

The single-shear calculation in `round14_shear.md` leaves a nonzero
fiber-Teichmüller force after solving the connection equation. This note
determines when several such forces can cancel, with the integral gluing
data retained. Cancellation is possible on an actual closed construction;
it is not merely the formal observation that the stress of a Hodge dual
has the opposite sign.

Let \(F\) be a closed oriented surface of genus \(p\ge2\), \(h\) a metric
of curvature \(-3\), and \(b_1,\ldots,b_m\in H^1(F;2\pi\mathbb Z)\).
Write \(\beta_j(h)\) for their harmonic representatives. For fixed
positive weights \(q_j\), define
\[
 \mathcal H_q(h)=\sum_jq_j\int_F|\beta_j|_h^2\,d\mu_h,
 \qquad
 S_q=\sum_jq_j\left(\beta_j\otimes\beta_j
                    -\tfrac12|\beta_j|^2h\right).             \tag{1}
\]

The following statements will be proved.

1. The fiber-moduli force is exactly \(S_q\), which is TT. The potential
   \(\mathcal H_q\) is stationary on marked hyperbolic metrics if and
   only if \(S_q=0\), equivalently the associated harmonic map to the
   flat torus with metric \(\sum q_jd\theta_j^2\) is weakly conformal.
2. For two nonzero classes, cancellation forces a holomorphic or
   antiholomorphic branched covering of a flat torus. Its degree is
   \[
      |d|=\left|\frac1{(2\pi)^2}\int_F b_1\wedge b_2\right|.
                                                               \tag{2}
   \]
   Consequently \(d=0\) and \(|d|=1\) cannot balance on \(p\ge2\).
3. There are integral pairs with \(d=2\) on a genus-two fiber for which
   cancellation is exact. They give a fixed closed two-shear manifold
   whose optimized near-Einstein family is stationary under every
   simultaneous hyperbolic fiber variation, for every collar size.

These are statements about an explicitly identified part of the full
Einstein equation. Each nonzero shear still has a negative waist
projection. Fiber balance neither solves the other modes nor supplies a
Yau26 counterexample.

The harmonic-map interpretation is classical. What is used here is its
exact realization by the shear capacity of the closed Round-11/14
construction, including an integral balanced example and a degree-one
obstruction to this particular balancing mechanism.

## 2. Variation without differentiating an uncontrolled harmonic inverse

Consider a smooth marked family \(h_s\), and let \(Q=\dot h_0\) be TT.
The cohomology classes are fixed, so
\(\dot\beta_j=d\xi_j\). Since \(\beta_j\) is coclosed,
\[
 \int_F\langle\beta_j,d\xi_j\rangle\,d\mu_h=0.
\]
Differentiating the inverse metric and volume form therefore gives
\[
 D\mathcal H_q[Q]=-\int_F\langle S_q,Q\rangle\,d\mu_h.        \tag{3}
\]
For a harmonic one-form,
\[
 \nabla^i(\beta_i\beta_j-\tfrac12|\beta|^2h_{ij})
 =\beta^i(\nabla_i\beta_j-\nabla_j\beta_i)=0.                 \tag{4}
\]
Thus \(S_q\) is itself an admissible TT variation. Such variations
integrate to a path of curvature-\(-3\) metrics: uniformize \(h+sQ\);
the first conformal correction vanishes because the scalar-curvature
variation of \(Q\) is zero and the conformal scalar linearization is
invertible. In particular,
\[
 D\mathcal H_q[S_q]=-\|S_q\|_2^2.                            \tag{5}
\]
This proves stationarity if and only if \(S_q=0\), with no compactness
assumption on the whole Teichmüller space.

Integral periods give circle-valued maps \(u_j:F\to\mathbb R/2\pi\mathbb Z\)
with \(du_j=\beta_j\). Their product \(U=(u_1,\ldots,u_m)\) is harmonic
into the flat torus \(T_q\). Its pulled-back metric has trace-free part
\(S_q\). Hence \(S_q=0\) is exactly weak conformality. Equivalently, with
\(*dx=dy\) in an oriented isothermal coordinate and
\(\omega_j=\beta_j+i*\beta_j\),
\[
                         \sum_jq_j\omega_j^2=0.              \tag{6}
\]
The forms \(\omega_j\) are holomorphic. Formula (6) is the vanishing
Hopf differential, not an extra condition inferred from an integrated
energy alone.

## 3. Two integral classes: a sharp topological distinction

Suppose \(m=2\), both classes are nonzero, and \(S_q=0\). Equation (6)
factorizes into two holomorphic one-form factors. On a connected compact
Riemann surface their product can vanish identically only when one
factor vanishes identically (use a neighborhood where one factor is
nonzero, then analytic continuation). It follows that
\[
       \beta_2=\pm\sqrt{q_1/q_2}\,*\beta_1.                 \tag{7}
\]
The sign is global. With the orientation corresponding to that sign,
\(U:F\to (T^2,q_1d\theta_1^2+q_2d\theta_2^2)\) is holomorphic.
It is nonconstant; compactness makes it a finite branched covering.
Its signed topological degree is exactly (2). Thus \(d=0\) is impossible.
If \(|d|=1\), every fiber has multiplicity one, so there is no ramification
and the map is biholomorphic. This contradicts \(p\ge2\).

No converse for every integral pair of degree at least two is asserted.
The existence of a suitable branched covering in the specified homotopy
class is additional information.

There is also an exact energy identity. Put
\(I=\int_F\beta_1\wedge\beta_2=(2\pi)^2d\), and take
\(s=\operatorname{sign}I\) when \(I\ne0\). Then
\[
 \boxed{\mathcal H_q
   =2\sqrt{q_1q_2}|I|
     +\|\sqrt{q_1}\beta_1+s\sqrt{q_2}*\beta_2\|_2^2.}       \tag{8}
\]
Indeed \(\langle\beta_1,*\beta_2\rangle d\mu=-\beta_1\wedge\beta_2\).
Equality in the resulting energy bound is precisely (7) with the
appropriate sign. For \(d=1\) the lower bound is not attained. This does
not by itself give a positive uniform gap on noncompact Teichmüller
space. On any compact set of marked metrics and positive normalized
weights, however, continuity and the absence of zeros imply a positive
lower bound on \(\|S_q\|_2\).

At a balanced metric, (8) also gives the entire second variation without
discarding the changing harmonic representatives. If
\(\zeta_s=\sqrt{q_1}\beta_1(h_s)
       +s_0\sqrt{q_2}*_{h_s}\beta_2(h_s)\),
where \(s_0=\operatorname{sign}d\), then \(\zeta_0=0\) and
\[
       \frac{d^2}{ds^2}\mathcal H_q(h_s)\bigg|_{s=0}
                       =2\|\dot\zeta_0\|_2^2\ge0.          \tag{8a}
\]
Terms from varying the norm vanish because \(\zeta_0=0\). Thus this
fiber equilibrium is a genuine minimum of the Hodge potential, not
merely a cancellation with an undetermined quadratic sign. Its null
space is the linearized condition \(\dot\zeta_0=0\); identifying that
space with a complete integrable moduli space is not needed here.

If every \(b_j=n_jb\) for a single nonzero real class, then

\[
 S_q=(\sum_jq_jn_j^2)T_\beta\ne0,                            \tag{9}
\]
so the rank-one obstruction remains valid for any number of collars.

## 4. A balanced integral example, including the branch points

Start with a square complex torus \(E=\mathbb C/(2\pi\mathbb Z+
2\pi i\mathbb Z)\). Cut each of two copies along the same embedded arc
joining distinct points \(P,Q\), and glue opposite banks crosswise.
The connected double cover \(p:F\to E\) is simply branched over \(P,Q\).
The pulled-back complex structure extends smoothly across these points
using \(z=w^2\); Riemann--Hurwitz gives
\[
                    \chi(F)=2\chi(E)-2=-2.
\]
Thus \(F\) has genus two. Let \(h\) be the curvature-\(-3\) metric in
this conformal class. Set
\[
               \beta_1=p^*dx,\qquad\beta_2=p^*dy.            \tag{10}
\]
These forms have periods in \(2\pi\mathbb Z\). They are smooth and
harmonic even at the branch points: they are the real and imaginary
parts of the holomorphic form \(p^*dz\), whose zeros there are allowed.
The star on one-forms is conformally invariant, hence
\[
        *\beta_1=\beta_2,\quad T_{\beta_1}+T_{\beta_2}=0,
        \int_F\beta_1\wedge\beta_2=2(2\pi)^2.               \tag{11}
\]
For equal weights this is an exact, integral solution of the fiber-force
equation. In the local branch coordinate \(z=w^2\), the ordinary
Euclidean covectors are
\(\beta_1=2u\,du-2v\,dv\) and
\(\beta_2=2v\,du+2u\,dv\); direct multiplication verifies (11),
including the common zero. The accompanying program checks this local
model, but existence of the cover is the geometric argument above.

## 5. The force is an exact variation on the closed four-manifold

Use the pure-shear subclass of `round11_closed_gluing.md`: all fibers
are the same marked \(F\), and all edge diffeomorphisms on \(F\) are the
identity. Edge \(j\) has a fixed integral circle-valued shear \(u_j\).
Choose hyperbolic product blocks with disjoint collars and profiles

\[
 g=dt^2+a_j(t)^2(d\phi+z_j(t)\beta_j(h))^2+h,
 \quad a_j=c_j\cosh(kt),\quad k=\sqrt3,                     \tag{12}
\]
where \(z_j\) is constant near both ends and its jump is one. Write
\[
                 q_j=\int a_j^3(z_j')^2dt>0.                \tag{13}
\]
The harmonic representatives can be used on a fixed smooth manifold:
their difference from the original shear forms is exact. The associated
circle translations extend over boundary collars and identify the
isotopic boundary gluings smoothly as \(h\) varies locally. No changing
integral lattice or topology is involved.

The determinant of (12) is independent of the connection. The fiber
area is fixed by Gauss--Bonnet, so the closed volume is the same \(V_*\)
for all these fiber variations. The scalar curvature is exactly

\[
                     s=-12-\tfrac12a_j^2(z_j')^2|\beta_j|^2
                                                               \tag{14}
\]
on the collars and \(-12\) outside. This formula does not require the
Maxwell equation, so it remains valid on the smooth cutoff bands.
Consequently the normalized Einstein--Hilbert functional is exactly

\[
 \boxed{\mathscr S(g)=V_*^{-1/2}\int_Ms_gd\mu_g
            =-12\sqrt{V_*}-\frac\pi{\sqrt{V_*}}\mathcal H_q(h).}
                                                               \tag{15}
\]
All exterior product terms have been included. In particular,
\[
 D_h\mathscr S[Q]=\frac\pi{\sqrt{V_*}}\langle S_q,Q\rangle_2.
                                                               \tag{16}
\]
Thus (11), with equal profiles and collar sizes, cancels *every*
simultaneous fiber-moduli variation of this closed family, exactly and
not only to leading order. Take one block \(B_{r,4}\times F\), \(r\ge0\),
and pair its four boundary circles into two self-edges with the two
maps supplied by (10). The result is a fixed closed oriented smooth
four-manifold, with
\[
                  \chi(M)=(2-2r-4)(-2)=4r+4.                \tag{17}
\]
Its Round-14 optimized profiles have \(\delta_{-3}=O(c^2)\) for equal
waist \(c\to0\); both edge shears are nonzero and integral. No claim is
made that this smooth topology is new in the literature or outside
every surface-bundle description.

The balanced family is not Einstein: for either edge the actual waist
receiver gives
\[
       \langle\operatorname{Ric}+3g,H_j\rangle
       =-3k\|\beta_j\|_2^2c^3+O(c^6)<0.                   \tag{18}
\]
The two localized receivers have disjoint supports; canceling the sum
of fiber stresses does not cancel either waist equation.

## 6. What the calculation changes in the full matching problem

The full low-mode system has at least two distinct sets of equations:

\[
 \begin{cases}
 \text{fiber shape: }\sum_jq_jT_{\beta_j}
                         +\text{exterior/nonlinear response}=0,\\
 \text{individual waist: }\mathscr F_j
                         +\text{boundary/nonlinear response}_j=0.
 \end{cases}                                                  \tag{19}
\]

A single sign argument on the shape equation cannot decide every
integral multi-shear object. Conversely, the degree-one and rank-one
cases give genuine noncancellation within the common-fiber shape
potential. The remaining question is whether an *arbitrary* Einstein
correction has an exterior/nonlinear response capable of compensating
these forces. Equation (15) settles the product-family contribution;
it does not remove the other responses in (19).

The exact collar boundary operator is computed separately in
`round15_boundary_response.md`. Its indefinite conormal part is why
positivity of a Dirichlet complement cannot simply be promoted to
positivity of the complete matching equation.

## 7. Relation to established work and verification

The interpretation of the Hopf differential as the metric variation
of harmonic-map energy belongs to classical harmonic-map/Teichmüller
theory. A primary reference for the coupled metric/map gradient and
its vanishing-Hopf condition is Rupflin--Topping--Zhu,
[*Asymptotics of the Teichmüller harmonic map flow*, equations (1.1)--(1.2)](https://arxiv.org/pdf/1209.3783). No theorem about long-time flow is
needed in this note. Equations (3)--(8) have been derived directly.

`round15_shear_balance_check.py` checks the stress variation, star
cancellation, rank-two energy identity, local branched model, scalar
action factors, and deliberately nonconformal test inputs. It does
not numerically certify a branched covering or an Einstein solution.
