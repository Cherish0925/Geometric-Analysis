# O10: what an orthogonal obstruction would have to prove

> Status update at completion: the finite-density O10 problem is closed by `O10_All_Finite_Density.md`, using the line-bundle method. This file preserves the earlier literature/orthogonal-obstruction investigation; its unproved sharp rank-two flux criterion is not needed for the new theorem.

2026-09-29. Research note. This examines the Huang–Ozuch suggestion in the newly supplied assessment against the actual weak endpoint system. The Hilbert-space lemma, Weyl decomposition, and concentration criterion below are independent calculations. They do not solve unrestricted O10.

## 1. Verified primary source and exact interface

Yiqi Huang and Tristan Ozuch, *Regularity of Einstein 5-manifolds via 4-dimensional gap theorems*, arXiv:2512.21317v2, 16 February 2026: <https://arxiv.org/html/2512.21317v2>.

Theorem 1.1 concerns exact Einstein orbifolds GH-close to a fixed compact spherical or hyperbolic four-orbifold. Theorem 2.20 places such metrics in a gluing family. Corollary 2.18 supplies a scale-uniform inverse estimate in weighted Hölder spaces. Corollary 3.2 controls the rescaling component of the bubble-tree obstruction by small multiples of its other components. Its proof compares the radial order-minus-four coefficient at ALE infinity, including the gauge correction. Proposition 3.5 gives a nonzero rescaling component from the exterior. Proposition 3.10 bounds the constructed approximation error by a quantity smaller than the largest exterior gluing parameter. Section 3.3 then rules out cancellation.

Thus the source provides an angle estimate and an error estimate at the **same gluing scale**. It does not assert the corresponding estimate for arbitrary metrics with small average squared Einstein residual. The imported proof requires both a geometric gluing description and a norm comparison absent from general O10.

Primary-source locations: equations (2.12), (3.3), (3.6)–(3.11), (3.14), (3.26), (3.29)–(3.30). Browser retrieval references: `turn141view0`, `turn143view0`, `turn143view1`, `turn145view0`, `turn145view1`.

## 2. The precise vector lemma

Let H be a real Hilbert space, e a unit vector, and write u = x e + y with y perpendicular to e. Suppose

\[
 |x|\le\epsilon\|y\|+r,
 \qquad \epsilon,r\ge0.
\tag{1}
\]

For any real a,

\[
 \boxed{\|a e+u\|\ge
 \frac{(|a|-r)_+}{\sqrt{1+\epsilon^2}}.}
\tag{2}
\]

Indeed,

\[
 |a|\le |a+x|+|x|
 \le |a+x|+\epsilon\|y\|+r
 \le \sqrt{1+\epsilon^2}\|a e+u\|+r.
\]

For r = 0 this is sharp: the minimizing correction has

\[
 x=-\frac{a\epsilon^2}{1+\epsilon^2},
 \qquad \|y\|=\frac{|a|\epsilon}{1+\epsilon^2}.
\]

If an additional approximation error z is present, the lower bound loses at most \(\|z\|\). This is an actual coercive estimate, but its application requires proof of (1). Decomposing an obstruction into parallel and perpendicular components alone supplies no such relation.

There is also a dimension issue. A family of relations

\[
 |x|\le\sum_{k=1}^{N_j}\epsilon_{jk}|y_k|
\]

gives (1) with \(\epsilon_j=(\sum_k\epsilon_{jk}^2)^{1/2}\). Knowing that every coefficient is small is insufficient when \(N_j\to\infty\). For instance \(\epsilon_{jk}=N_j^{-1/2}\) tends to zero individually, but its operator norm remains one. An unrestricted O10 argument needs the operator-norm version, or an independent bound on the total obstruction dimension.

## 3. The scale issue survives even after granting a bubble tree

Suppose hypothetically that a weak O10 sequence has a suitable gluing description and that (2) produces a residual of size \(c t_j\), where \(t_j\downarrow0\) is a gluing parameter. Such a bound excludes an exact solution, and excludes an error \(o(t_j)\). It does not exclude an error that merely tends to zero.

The elementary scaling example is already decisive. A tensor of pointwise norm of order one supported in a region of volume of order \(t_j^2\) has squared L2 norm of order \(t_j^2\). Hence its normalized squared L2 norm tends to zero when the total volume stays bounded below. A nonzero obstruction on every shrinking core can therefore be consistent with a vanishing average residual.

This is not a proposed actual O10 counterexample: the monopole system and all matching conditions have not been imposed. It proves a logical point about the proposed import. A finite-scale nonvanishing theorem does not imply the volume-scale lower bound required by O10. A successful adaptation must show that the aggregate obstruction has squared norm comparable to V, or that the actual field controls the residual relative to every relevant gluing scale. Neither follows from \(\fint|\mathrm{Ric}+g|^2\to0\).

## 4. A global vector decomposition already available in O10

Assume an actual zero-endpoint sequence, scalar curvature minus four, and a fixed finite bound on

\[
 b_j=\fint|W_j^-|^2.
\]

Use the bounded resolvent section v from the preceding continuation and set

\[
 a=|v|^2,\quad m_*=128/81,\quad Q=-iq_-(v),\quad q_0^2=m_*^2/8.
\]

The already established strong-current and Hopf-form calculations give

\[
 a\to m_*\text{ in }L^2_{\rm avg},\qquad |v|\le C,
\]

\[
 \fint\langle W^-Q,Q\rangle\to5m_*^2/12,
 \qquad |Q|^2=a^2/8.
\tag{3}
\]

Define the smooth polynomial tensor

\[
 W_0=\frac5{q_0^2}
 \left(Q\otimes Q-\frac{|Q|^2}{3}I\right).
\tag{4}
\]

No normalization by Q is used, so (4) remains smooth at its zeros. Since W is trace free,

\[
 \fint\langle W^-,W_0\rangle
 =\frac5{q_0^2}\fint\langle W^-Q,Q\rangle\to50/3.
\]

Also

\[
 |Q\otimes Q-|Q|^2I/3|^2=\frac23|Q|^4,
 \qquad \fint|W_0|^2\to50/3.
\]

Writing R = W minus W0, one obtains, for **every** bounded-b zero sequence,

\[
 \boxed{\fint\langle R,W_0\rangle\to0,
 \qquad \fint|R|^2=b_j-50/3+o(1).}
\tag{5}
\]

The previous endpoint theorem used the special case where the right side tends to zero. Formula (5) records what remains when it does not. It is a restatement of that established pairing, not a new threshold theorem.

### 4.1 Which vector components can carry the excess?

Fix d with \(0<d^2<m_*\), let \(G_j=\{|v|\ge d\}\), and let \(Z_j=M_j\setminus G_j\). The relative volume of Z tends to zero. On G put \(n=Q/|Q|\) and write the symmetric trace-free Weyl operator as

\[
 W^-=
 \begin{pmatrix}
  \lambda & z^*\\
  z & C-\lambda I_2/2
 \end{pmatrix},
 \qquad \operatorname{tr}C=0.
\tag{6}
\]

This is independent of the choice of orthonormal frame in the plane perpendicular to n. Pointwise,

\[
 |W^-|^2=\frac32\lambda^2+2|z|^2+|C|^2.
\tag{7}
\]

The omitted pairing on Z tends to zero: Q is bounded, W has bounded normalized L2 norm, and Z has relative volume tending to zero. On G, replacing \(a^2\) by \(m_*^2\) in \(\langle WQ,Q\rangle=a^2\lambda/8\) is legitimate by L2 duality. Thus (3) yields

\[
 \fint_{G_j}\lambda\to10/3.
\]

Completing the square in (7) consequently gives

\[
 \boxed{
 b_j-\frac{50}{3}
 =\fint_{G_j}\left[
   \frac32\left(\lambda-\frac{10}{3}\right)^2
    +2|z|^2+|C|^2\right]
   +\fint_{Z_j}|W^-|^2+o(1).}
\tag{8}
\]

Formula (8) separates four possible payments: axial variation, an off-axis column, the trace-free planar block, and curvature concentrated where v is small. The last term cannot be discarded using the small volume of Z: this is exactly the critical concentration problem.

For example the abstract matrices

\[
 \operatorname{diag}(10/3,-5/3+t,-5/3-t)
\]

have the required axial pairing for every t but energy \(50/3+2t^2\). This is not a geometric realization. It shows that the known scalar pairing does not establish a small-angle relation among the excess components. The actual differential equations must provide that missing restriction.

## 5. A sharp concentration statement would close every bounded-density zero sequence

This is a concrete conditional criterion, rather than a claim that a Chern estimate has already achieved it.

Pass to a subsequence with \(b_j\to b<\infty\) and define the opposite-Weyl concentration amount

\[
 \Gamma_W=\lim_{T\to\infty}\limsup_j
  \fint_{\{|W_j^-|>T\}}|W_j^-|^2.
\]

Since W0 is uniformly bounded, W and R = W minus W0 have the same concentration amount. To check this, their thresholds differ by a bounded constant, and

\[
 \fint_{\{|W|>T\}}
 \big||W|^2-|R|^2\big|
 \le C\fint_{\{|W|>T\}}(|W|+1)
 \le Cb/T+Cb/T^2.
\]

The reverse estimate is identical. Equation (5) therefore implies

\[
 \boxed{\Gamma_W\le b-50/3.}
\tag{9}
\]

The exact actual Chern–Weil limit is already known:

\[
 \lim_j\frac{c_2(E_j)[M_j]}{V_j}
 =\frac5{12\pi^2}+\frac b{8\pi^2}.
\tag{10}
\]

Consequently the following sharp concentration upper bound would be impossible:

\[
 \limsup_j\frac{c_2(E_j)[M_j]}{V_j}
 \le\frac{\Gamma_W}{8\pi^2}.
\tag{11}
\]

Indeed, (9)–(11) would give

\[
 \frac5{12\pi^2}+\frac b{8\pi^2}
 \le\frac{b-50/3}{8\pi^2},
\]

an immediate contradiction. A remainder smaller than \(5/(2\pi^2)\) in (11) would also suffice, since the difference of the two displayed sides is exactly that constant.

The existing rank-two cutoff/transgression estimate has the form \(c_2/V\le C\Gamma_W\), with a nonsharp coefficient and derivative concentration terms absorbed into C. It does **not** imply (11). The motivation for investigating (11) is that the curvature of E in the opposite chirality has a bounded model plus a vanishing L2 error, so concentrating connection curvature has one dominant chirality. Turning that observation into the sharp Chern defect coefficient requires an actual control of the transgression or the connection concentration measure on the degenerating geometry. Ordinary Cauchy–Schwarz estimates lose precisely this coefficient.

This criterion is restricted to bounded b. An unbounded-density sequence also needs a compatible normalization or a separate argument.

## 6. Outcome

The new assessment identifies a useful proof architecture but supplies no theorem applicable directly to weak O10. The missing content can now be stated precisely: a scale-correct angle estimate for actual O10 defects, or a sharp Chern concentration statement such as (11). Equations (2), (8), and (9) expose the required constants and components. They do not enlarge the already proved endpoint range by themselves.

The first-prolongation theorem remains valid input. Its removal of three derivative directions does not yet establish (1) for the residual Weyl components or (11) for the Chern defect; the surviving complex derivative component and concentrated transgression have to be controlled by another actual identity.
