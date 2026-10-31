# Integral rigidity for bounded self-dual forms

This note isolates the analytic mechanism behind the integral monopole gap.
It proves an abstract theorem whose input is a bounded self-dual two-form with
a Hodge-Laplacian budget, rather than a monopole spinor. This makes the
production of a calibration and its differential budget separate inputs.
It is an analytic criterion; no new family of smooth topologies is asserted
to satisfy its hypotheses.

All manifolds are smooth, closed, oriented and four-dimensional. Curvature
is normalized relative to \(\operatorname{Ric}=-g\). Two-forms have the
exterior-algebra norm; \(W^+\) has the Hilbert--Schmidt operator norm. Write
\(\fint=\operatorname{Vol}^{-1}\int\), and let \(\Delta_H\) denote the
nonnegative Hodge Laplacian.

## 1. The bounded two-form criterion

For a smooth self-dual two-form \(\psi\), set

\[
 q=|\psi|^2,\qquad
 A_\psi={q\over24}I-{1\over8}\psi\otimes\psi,
 \qquad R=W^+-A_\psi.
\]

Define the defect and source budget

\[
 d=\fint_M\left(|\operatorname{Ric}+g|^2+|R|^2+(q-2)^2\right),
 \qquad B=\fint_M|\Delta_H\psi|^2.
\]

**Theorem.** For each finite \(K>0\), there is \(c(K)>0\) such that
\(\|\psi\|_\infty\le K\) implies

\[
                    \boxed{(1+B)d\ge c(K).}              \tag{1}
\]

**Small-source corollary.** For a possibly smaller \(c_0(K)>0\),

\[
 \boxed{\quad
 \fint_M\left(
 |\operatorname{Ric}+g|^2+|R|^2+(q-2)^2+|\Delta_H\psi|^2
 \right)\ge c_0(K).
 \quad}                                                     \tag{1a}
\]

No spin structure, monopole class, curvature bound, scalar sign, Sobolev
constant, injectivity radius or diameter bound is required. In particular,
for bounded *harmonic* self-dual forms \(B=0\), giving a gap for the
three zeroth-order defects alone. No small first-derivative defect is
assumed, even in the nonharmonic case.
The boundedness of the form and its Hodge-Laplacian control are genuine
hypotheses, not consequences of a cohomology class alone.

The theorem excludes a specific incompatible calibration: Ricci curvature
near \(-g\), Weyl curvature near \(A_\psi\), and \(|\psi|^2\) near two.
For a product of curvature-minus-one surfaces the simple Weyl eigenvalue
is \(-2/3\), not the target \(-1/6\). Thus the theorem does not exclude
the realizable hyperbolic-product Weyl model and does
not assert a universal Ricci gap without the other summands.

## 2. Re-derivation of the bundle Hessian estimate

Let \(u\) be a smooth section of a metric bundle, with compatible connection
\(\nabla\). Set \(H_{ij}=\nabla_i\nabla_j u\), including the cotangent
Levi-Civita correction, \(L=\operatorname{tr}H\), and
\(F_{ij}=[\nabla_i,\nabla_j]\). Use the component convention
\(|F|^2=\sum_{ij}|F_{ij}|_{\rm HS}^2\).

First, integration of the divergence of
\(|\nabla u|^2\langle u,\nabla u\rangle^\sharp\) gives

\[
 \|\nabla u\|_4^2\le(2+\sqrt4)\|u\|_\infty\|H\|_2.
                                                               \tag{2}
\]

This is a covariant integration-by-parts inequality, not a Sobolev
embedding. To check the curvature terms, first interchange the two
Hessian slots:

\[
 \int|H|^2-\sum_{ij}\int\langle H_{ij},H_{ji}\rangle
 =\frac12\sum_{ij}\int|F_{ij}u|^2.
\]

Integrate the second expression once and then commute derivatives on the
bundle-valued one-form \(\nabla u\). The cotangent curvature gives Ricci;
the bundle curvature acts on \(\nabla u\). Integrating the trace term once
more yields

\[
\begin{split}
 \int|H|^2={}&\int|L|^2
 -\int\operatorname{Ric}_{ij}\langle\nabla_i u,\nabla_j u\rangle\\
 &+\sum_{ij}\int\langle F_{ij}\nabla_j u,\nabla_i u\rangle
 +\frac12\sum_{ij}\int|F_{ij}u|^2.                         \tag{3}
\end{split}
\]

There is no differentiated-curvature term. Swapping the Hessian slots
*before* commuting is important. The scalar specialization fixes the
Ricci sign. With \(K_u=\|u\|_\infty\), Holder, (2), and Young give

\[
 \|\nabla^2u\|_2^2\le
 2\|L\|_2^2+32K_u^2\|\operatorname{Ric}\|_2^2
                         +33K_u^2\|F\|_2^2.              \tag{4}
\]

This recovers the inherited estimate, including its coefficient and the
absence of a hidden Sobolev or curvature-derivative hypothesis.

## 3. Proof of the two-form criterion

Assume \(d\le1\); otherwise the conclusion is immediate after reducing
\(c(K)\). Put \(\mathcal B=1+B+d\). All constants below
depend only on \(K\) and the dimension. Put \(E=\operatorname{Ric}+g\)
and \(\eta=\Delta_H\psi\).

### 3.1 The self-dual connection supplies the second-order budget

The curvature of \(\Lambda^+\) is the representation of the Riemann
operator projected to its self-dual output. Hence

\[
 |F^{\Lambda^+}|^2\le C\left(|W^+|^2+s^2+
                               |\operatorname{Ric}^{\circ}|^2\right).
                                                               \tag{5}
\]

The \(W^-\) block does not act on \(\Lambda^+\). Since
\(|A_\psi|^2=q^2/96\) and \(q\le K^2\), the \(E,R\) budgets give

\[
 \fint\left(|\operatorname{Ric}|^2+|F^{\Lambda^+}|^2\right)
 \le C_K(1+d).
\]

The self-dual Weitzenbock equation is

\[
 \nabla^*\nabla\psi=\eta+2W^+\psi-(s/3)\psi.
\]

Apply (2)--(4) to \(u=\psi\). Differentiating the quadratic polynomial
\(A_\psi\) and the scalar \(q\) then gives

\[
 \fint\left(|\nabla^2\psi|^2+|\nabla\psi|^4+
              |\nabla^2A_\psi|^2+|\Delta q|^2\right)
 \le C_K\mathcal B.
                                                               \tag{6}
\]

Here \(\Delta=d^*d\) on functions, and
\(\Delta q=2\langle\nabla^*\nabla\psi,\psi\rangle
-2|\nabla\psi|^2\). All estimates are extensive before division by
volume; no lower volume bound enters.

### 3.2 Amplitude control and a coercive divergence identity

The amplitude itself need not have a smooth square root at its zeros.
Use the globally smooth quantity \(q\), rather than divide by \(|\psi|\).
Integration by parts and (6) give

\[
 \fint|dq|^2=\fint(q-2)\Delta q
                  \le C_K\sqrt{d\mathcal B}.             \tag{7}
\]

There is a useful pointwise identity, valid for arbitrary smooth
self-dual forms without first-order equations. Let
\(J=\operatorname{div}W(A_\psi)\). The full contraction in the checker
gives

\[
 |J|^2={q|\nabla\psi|^2\over64}+{q|d\psi|^2\over32}
       -{|dq|^2\over192}
       +{\langle\iota_{\nabla q}\psi,*d\psi\rangle\over32}.
                                                               \tag{8}
\]

The last inner product is at most
\(\sqrt q\,|dq|\,|d\psi|\) in absolute value. Young's inequality
therefore gives the pointwise coercivity

\[
 \boxed{\quad
 q\bigl(|\nabla\psi|^2+|d\psi|^2\bigr)
        \le64|J|^2+{4\over3}|dq|^2.
 \quad}                                                     \tag{8a}
\]

This is polynomial at zeros, and introduces no division by \(q\).
It will control the derivative terms for the two-sided selection theorem
in Section 6. Small amplitude error and a second-order budget now supply
the weighted derivative information previously obtained from monopoles.

### 3.3 Weak Bianchi gives a small self-test

Let \(W(A)\) be the algebraic Weyl four-tensor represented by \(A\), and
\(J=\operatorname{div}W(A_\psi)\). The projections to \(\Lambda^+\)
are parallel. The contracted Bianchi identity, followed by integration
by parts, gives for every smooth test tensor \(T\)

\[
 \left|\int\langle J,T\rangle\right|
 \le C\left(\|E\|_2+\|R\|_2\right)\|\nabla T\|_2.      \tag{9}
\]

This is a weak derivative estimate, not an estimate on \(\nabla E\).
The tensor \(J\) is smooth, so \(T=J\) is an admissible test. Moreover
\(|\nabla J|\le C|\nabla^2A_\psi|\). Therefore (6) implies

\[
                 \fint|J|^2\le C_K\sqrt{d\mathcal B}.    \tag{10}
\]

### 3.4 The same self-test has a positive lower bound

The inherited weighted Hodge and divergence identities admit the
following entirely polynomial version:

\[
\begin{split}
 \int|J|^2=\int\Big(&-{s q^2\over192}-{q^3\over384}
       +{q\langle R\psi,\psi\rangle\over32}
       +{q|d\psi|^2\over16}-{5|dq|^2\over384}\\
       &+{\langle\iota_{\nabla q}\psi,*d\psi\rangle\over16}
                           \Big).                         \tag{11}
\end{split}
\]

It follows by testing the self-dual Hodge equation against \(q\psi\)
and contracting the derivative of \(A_\psi\); the pointwise contraction
is independently checked in the accompanying program. Because (11) is
polynomial in \(\psi,\nabla\psi\), it extends across all zeros of
\(\psi\); no spinor-square representation is used.

At \(s=-4,q=2,R=0\), its algebraic part equals \(1/16\). On
\(0\le q\le K^2\), polynomial Lipschitz estimates give an averaged
error bounded by
\(C_K\fint(|s+4|+|q-2|+|R|)\le C_K\sqrt d\).
The last term is bounded below by
\(-\{q|d\psi|^2+|dq|^2\}/32\). Absorb its first contribution into
the positive \(q|d\psi|^2/16\) already present in (11). The remaining
derivative error is at worst \(-17|dq|^2/384\), controlled by (7).
In particular this argument does not assume \(d\psi\) small.
Consequently

\[
           \fint|J|^2\ge {1\over16}-C_K\sqrt{d\mathcal B}.\tag{12}
\]

Combining (10) and (12) yields
\(1/16\le C'_K\sqrt{d(1+B+d)}\). For \(d\le1\),
\(1+B+d\le2(1+B)\), proving (1) after choosing a sufficiently small
\(c(K)>0\). For (1a), if its left side is \(z\le1\), then
\(d\le z\), \(B\le z\), and \((1+B)d\le2z\). Thus
\(c_0(K)=\min\{1,c(K)/2\}\) suffices.

## 4. What the monopole proof actually requires

For the inherited integral gap, one fixes a metric \(g\) and a single
spin-c structure with \(p=(a_g^+)^2>0\). The analytic construction only
requires ordinary unperturbed Seiberg--Witten solutions for every metric
in \([g]\). Indeed, solving on \(\widehat g=f^{-2}g\) gives on \(g\)

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi),
\]

for every positive smooth weight \(f\). The self-dual polarization is
conformally invariant. Every remaining Hessian, Hodge and Bianchi step
takes place on this one metric. Neither \(b_+>1\) nor persistence over
metrics outside \([g]\) is used in those analytic steps.

This is already the scope of [the Round13 chamber result](round13_chamber.md),
not a new Round21 extension. In \(b_+=1\) applications, chamber invariance
and passage from perturbed invariants to unperturbed solutions still have
to be established. The Hessian identity cannot supply them.

For the monopole argument specifically, the determinant connection energy
is controlled by

\[
 \|F_A\|_2^2=2\|F_A^+\|_2^2-4\pi^2a^2.
\]

That is the origin of the negative-square cost. The theorem in Section 1
avoids this connection by acting directly on \(\Lambda^+\), but replaces
the monopole PDE with a bounded-form and Hodge-budget hypothesis. It
therefore does **not** remove the square cost from the existing monopole
theorem: the harmonic projection need not preserve a maximum bound, and a
small \(d\psi\) does not bound \(\Delta_H\psi\) by itself.

More precisely, let \(\kappa\) and \(B_a=(-a^2)_+/V\) have the meanings
in [Round4, Theorem 1](round4_rigidity.md). The inherited bounded-spinor,
Hessian and fourth-power-gradient estimates imply

\[
 B=\fint|\Delta_H\psi|^2\le C(1+\kappa+B_a)+o(1).
\]

Indeed, the quadratic map from \(\Phi\) to \(\psi\) gives
\(|\nabla^2\psi|\le C(|\Phi||\nabla_A^2\Phi|+|\nabla_A\Phi|^2)\);
the two-form Weitzenbock formula adds only the already controlled
\(W^+,s\) terms. The Weyl approximation and amplitude estimates give
simultaneously

\[
                         d\le C\kappa+o(1).
\]

The bounded-form theorem therefore returns
\(\kappa(1+\kappa+B_a)\ge c\), and hence the inherited
\((1+B_a)\kappa\ge c'\) after splitting \(\kappa\le1\) and
\(\kappa>1\). This is a structural recovery of the earlier calibration
gap, not a second independent topological theorem. It displays precisely
where a different construction of a bounded form could replace the
monopole input, and which quantitative budget that construction must supply.

## 5. Research use and verification scope

The new analytic formulation offers a distinct input route: a family of
bounded, almost-harmonic self-dual forms with the indicated calibration
would be impossible even without monopole solvability. For a harmonic
form, only its maximum bound and the three zeroth-order calibration
defects remain. Producing these hypotheses on a new topological family is
an open step; a formal cohomology vector does not suffice.

The checker verifies the Hessian curvature coefficients on a noncommuting
constant connection, the full twelve-variable divergence contraction, and
the polynomial conversion used in (11). The general integration-by-parts
and PDE arguments are the proofs above, not consequences of running the
checker. The inherited statements have been checked at these analytic
interfaces; this note does not certify every earlier topological input.

## 6. Quantitative selection of the Kähler calibration

The forbidden Weyl model is one member of a family, not an isolated
numerical accident. For a constant real parameter \(t\), put

\[
 A_{\psi,t}=t\left({q\over3}I-\psi\otimes\psi\right),
 \quad R_t=W^+-A_{\psi,t},\quad
 d_t=\fint\left(|E|^2+|R_t|^2+(q-2)^2\right).
                                                               \tag{13}
\]

Thus \(t=1/8\) is the model in Theorem (1). At \(q=2\), the Weyl
eigenvalues prescribed by \(A_{\psi,t}\) are
\((-4t/3,2t/3,2t/3)\). The negative Kähler--Einstein value is
\(t=1/2\).

**Branch-selection theorem.** Fix \(K,T<\infty\). For
\(\|\psi\|_\infty\le K\) and \(|t|\le T\),

\[
 \boxed{\quad |t|\,|1-2t|\le C(K,T)
                  \sqrt{d_t(1+B+d_t)}.\quad}             \tag{14}
\]

A quantitative spectral-selection consequence is

\[
 \boxed{\quad
 \operatorname{dist}(t,\{0,1/2\})^2
       \le C(K,T)(1+B)d_t\qquad(d_t\le1).
 \quad}                                                   \tag{14a}
\]

Indeed, \(\operatorname{dist}(t,\{0,1/2\})\le2|t|\,|1-2t|\)
for every real \(t\), since the larger of the distances to zero and
one-half is at least one-quarter. Also \(1+B+d_t\le2(1+B)\).
The two branches are vanishing Weyl amplitude and the negative
Kähler--Einstein amplitude, not an arbitrary list of forbidden constants.

Consequently \((1+B)d_t\) has a uniform positive lower bound when \(t\)
is restricted to a compact subset of \(\mathbb R\setminus\{0,1/2\}\).
On any parameter set \(t_0\le|t|\le T\), with \(t_0>0\), one further has

\[
 |2t-1|+\fint\left(|\nabla\psi|^2+|d\psi|^2\right)
 \le C(K,t_0,T)\sqrt{d_t(1+B+d_t)}\qquad(d_t\le1).       \tag{15}
\]

Thus a bounded-source-budget calibration with vanishing defect and
nonzero Weyl amplitude selects the Kähler value and an almost-parallel
form. This is an integral conclusion; it does not supply coordinates,
pointwise metric closeness or compactness.

**Proof.** Let \(J_t=\operatorname{div}W(A_{\psi,t})\). Since
\(A_{\psi,t}=8tA_\psi\), one has \(J_t=8tJ\), with \(J\) here denoting
the divergence of the original polynomial on the same form and metric.
The second-order estimates remain valid uniformly for bounded \(t\),
with \(\mathcal B_t=1+B+d_t\). In the weak Bianchi test the derivative
of \(J_t\) has one factor \(|t|\), so

\[
                  \fint|J_t|^2\le C_{K,T}\,|t|
                                      \sqrt{d_t\mathcal B_t}. \tag{16}
\]

The weighted Hodge contraction becomes exactly

\[
\begin{split}
 \int|J_t|^2=\int\Big(&-{t^2s q^2\over3}
       -{4t^3q^3\over3}+2t^2q\langle R_t\psi,\psi\rangle
       +4t^2q|d\psi|^2-{5t^2\over6}|dq|^2\\
       &+4t^2\langle\iota_{\nabla q}\psi,*d\psi\rangle
                    \Big).                               \tag{17}
\end{split}
\]

Its algebraic part at \(s=-4,q=2,R_t=0\) is
\(P(t)=(16/3)t^2(1-2t)\). The pointwise coercivity (8a) rescales to

\[
 t^2q\bigl(|\nabla\psi|^2+|d\psi|^2\bigr)
          \le |J_t|^2+{4\over3}t^2|dq|^2.                \tag{18}
\]

In (17), the absolute derivative contribution is at most
\(6|J_t|^2+(65/6)t^2|dq|^2\): the positive closedness term costs at
most \(4|J_t|^2+(16/3)t^2|dq|^2\), and Young's inequality bounds the
cross term by \(2|J_t|^2+(14/3)t^2|dq|^2\). This uses (18), not an
assumption that \(d\psi\) is small. Together with the zeroth-order
algebraic error and the amplitude estimate (7),

\[
 |P(t)|\le 7\fint|J_t|^2+
                  C_{K,T}t^2\sqrt{d_t\mathcal B_t}.       \tag{18a}
\]

This is valid on both sides of \(t=1/2\), including negative \(t\).
Combine (16) and (18a), divide by \(|t|>0\), and use \(|t|\le T\),
obtaining (14).
The case \(t=0\) is automatic. For \(d_t>1\), (14) follows after
enlarging the constant since its left side is bounded and its right
square root is at least one.

For (15), (14) first bounds \(|2t-1|\) by its right side divided by
\(t_0\). On \(\{q\ge1\}\), (18), (16) and (7) give
an averaged bound \(C_{K,t_0,T}\sqrt{d_t\mathcal B_t}\) for
\(|\nabla\psi|^2+|d\psi|^2\). On \(\{q<1\}\), the relative volume
is at most \(\fint(q-2)^2\le d_t\). The fourth-power gradient estimate
(6), and \(|d\psi|^2\le3|\nabla\psi|^2\), bound its contribution by
\(C_{K,T}\sqrt{d_t\mathcal B_t}\). This proves (15) without assuming
closedness.

For comparison, the unweighted Hodge identity is

\[
 \fint|\nabla\psi|^2
 =2\fint|d\psi|^2-
  \fint\left({s q\over3}+{4tq^2\over3}
                               -2\langle R_t\psi,\psi\rangle\right).
                                                               \tag{19}
\]

The parenthesized expression differs in average from
\((8/3)(2t-1)\) by at most \(C_{K,T}\sqrt{d_t}\).
Nonnegativity of the left side gives the one-sided estimate

\[
 (2t-1)_+\le C_{K,T}\left(\sqrt{d_t}+\fint|d\psi|^2\right).
                                                               \tag{20}
\]

It becomes source-budget-free when \(d\psi=0\), but not for arbitrary
forms under zeroth-order control alone.

At zero defect and \(t\ne0\), (14) forces \(t=1/2\), and (15) gives
\(\nabla\psi=0\). The norm-squared-two self-dual form is then the
parallel Kähler form of an orthogonal complex structure, and
\(\operatorname{Ric}=-g\) makes the metric negative Kähler--Einstein.
This endpoint is genuinely realized; parallelness of the Kähler form
does not imply that the metric is a global product. At \(t=0\), the divergence
polynomial loses sensitivity; (14) makes no assertion that an exact
calibrated example exists there.

This extension identifies the realizable equality model of the analytic
mechanism. It does not change which monopole classes are available, and
it does not by itself extend the topological range of the earlier
integral gap.

## 7. The same analytic criterion for either Einstein sign

The spectral-selection argument itself is not restricted to the negative
Einstein sign. For \(\sigma\in\{-1,+1\}\), put

\[
E_\sigma=\operatorname{Ric}-\sigma g,\qquad
d_{\sigma,t}=\fint\left(
|E_\sigma|^2+|W^+-A_{\psi,t}|^2+(q-2)^2\right).
\]

With the same bounded-form and bounded-parameter hypotheses,

\[
\boxed{\quad
|t|\,|\sigma+2t|
\le C(K,T)\sqrt{d_{\sigma,t}(1+B+d_{\sigma,t})}.
\quad}                                                     \tag{21}
\]

In particular, for \(d_{\sigma,t}\le1\),

\[
\operatorname{dist}(t,\{0,-\sigma/2\})^2
\le C(K,T)(1+B)d_{\sigma,t}.                               \tag{22}
\]

To verify this, replace the scalar target \(-4\) by \(4\sigma\) in
(17). Its calibrated algebraic value becomes
\[
P_\sigma(t)=-\frac{16}{3}t^2(\sigma+2t).
\]
The curvature budget uses
\(|\operatorname{Ric}|\le|E_\sigma|+2\), the amplitude estimate is
unchanged, and weak Bianchi differentiates neither constant multiple
of the metric. Equations (16), (18) and (18a) therefore hold with
this \(P_\sigma\) and \(d_{\sigma,t}\); division by \(|t|\) proves
(21), including its trivial \(t=0\) case. The distance estimate follows
as before. For \(|t|\ge t_0>0\), the same good/bad-amplitude argument
controls \(\fint(|\nabla\psi|^2+|d\psi|^2)\).

At zero defect and \(t\ne0\), this forces \(t=-\sigma/2\) and a
parallel norm-squared-two self-dual form. The metric is then
Kähler--Einstein with \(\operatorname{Ric}=\sigma g\).
The positive Kähler--Einstein amplitude is \(-1/2\), not \(+1/2\).
This extension concerns the analytic criterion only: it does not supply
positive-side monopole classes or a Yau26 positive-branch obstruction.
