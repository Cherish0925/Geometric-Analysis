# Actual monopole intersections and global phase mixing

## 1. A global consequence of the bounded calibration

The bounded forms of [Round 17](round17_integral.md) approximate
curvatures of actual determinant line bundles. This permits intersection
pairings to be computed by global \(L^2\) wedge products, without
restricting forms to collapsing cycles. A common Weyl tensor forces all
these forms into approximately the same *unoriented* line. The signs may
vary over the manifold; their joint distribution, however, is constrained
by the intersection form.

This note proves two consequences:

1. the normalized intersection matrix approaches the convex hull of
   rank-one sign matrices;
2. nonextremal intersections force small scalar-Laplacian
   eigenvalues, with their multiplicity controlled by an intersection
   covariance matrix, through globally smooth phase observables.

The second conclusion is a quantitative global cost of phase mixing,
not a claim that the phase cannot switch. It is valid on the original
metric and needs neither noncollapse nor a lower spectral bound.

### Assumptions and normalized errors

Let \(M\) be a closed connected oriented smooth four-manifold.
For a smooth metric \(g\), suppose the specified classes
\(a_1,\ldots,a_m\) have actual unperturbed Seiberg--Witten solutions,
and

\[
 a_i^2=A>0,\qquad A\ge T:=2\chi(M)+3\tau(M).
 \tag{1}
\]

Actual monopole classes make this assumption available for all metrics.
The classes need not have nonzero ordinary Seiberg--Witten invariants.
No sum or difference of them is assumed to be a monopole.

Suppose the mean scalar curvature is negative and set

\[
 \kappa=-\frac1{4V}\int s>0,\qquad
 B=\int s^2-32\pi^2 A,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 L=\int(s+4\kappa)^2,
 \tag{2}
\]
\[
 b=\frac{B}{\kappa^2V},\quad
 p=\frac{P}{\kappa^2V},\quad
 \ell=\frac{L}{\kappa^2V},\quad
 \epsilon=b+p+\ell,\quad
 r=\frac{2\pi^2 A}{\kappa^2V}.
 \tag{3}
\]

Round 17 gives \(B\ge0\). The mean-scalar normalization gives exactly

\[
 r=1+\frac{\ell-b}{16}.
 \tag{4}
\]

All estimates below assume \(\epsilon\le1\); thus
\(15/16\le r\le17/16\).
Write \(\mathbb E f=V^{-1}\int_M f\,d\mu\).
Let \(G\) denote the metric-independent intersection matrix

\[
 G_{ij}=\frac{a_i\cdot a_j}{A},\qquad G_{ii}=1.
 \tag{5}
\]

The constants are not optimized.

## 2. The joint intersection theorem

Define the finite sign-correlation polytope

\[
 \mathcal C_m
 =\operatorname{conv}\{zz^{\mathsf T}:z\in\{-1,1\}^m\}.
 \tag{6}
\]

This definition, rather than any classification of its facets, is all
that is used.

**Theorem 1.** Under (1)--(3), there is \(C\in\mathcal C_m\) such that

\[
 \boxed{\max_{i,j}|G_{ij}-C_{ij}|\le24\sqrt\epsilon.}
 \tag{7}
\]

The constant is independent of the number of classes. More concretely,
there are measurable signs \(\sigma_i:M\to\{-1,1\}\), with
\(\sigma_1=1\), for which

\[
 C_{ij}=\mathbb E(\sigma_i\sigma_j).
 \tag{8}
\]

Consequently

\[
 \left|
 \frac{\operatorname{Vol}\{\sigma_i\sigma_j=1\}}{V}
            -\frac{1+G_{ij}}2
 \right|\le12\sqrt\epsilon.
 \tag{9}
\]

The signs are used only measurably. Their derivatives, the
orientability of a Weyl eigenline bundle, and continuity of a global
unit eigenvector are not assumptions.

### Consequence: integral odd-sum constraints

For \(n=(n_1,\ldots,n_m)\in\mathbb Z^m\) with \(\sum_i n_i\) odd,
every sign vector satisfies \((n\cdot z)^2\ge1\). Hence

\[
 \boxed{
 \frac{(\sum_i n_i a_i)^2}{A}
 \ge1-24\|n\|_1^2\sqrt\epsilon.}
 \tag{10}
\]

If the left side is \(1-\eta<1\), every metric covered by (1)--(3)
has

\[
 \epsilon\ge
 \min\!\left\{1,\frac{\eta^2}{576\|n\|_1^4}\right\}.
 \tag{11}
\]

This is an intersection criterion, not an assertion that a particular
violating lattice configuration is realized by monopoles.

## 3. Proof: from actual curvature to common measurable signs

Apply Round 17 separately to each actual solution. Let \(\varphi_i\)
be its smooth capped self-dual form and let
\(\mathcal F_i=iF_{\mathfrak A_i}\), so
\([\mathcal F_i/(2\pi)]=a_i\).
Normalize

\[
 u_i=\frac{\varphi_i}{4\kappa},\qquad
 f_i=\frac{\mathcal F_i}{\sqrt2\,\kappa},\qquad
 Q(u)=u\otimes u-\frac{|u|^2}{3}I.
 \tag{12}
\]

The following estimates follow directly from Round 17:

\[
 \begin{gathered}
 |u_i|\le2,\qquad
 \mathbb E(|u_i|-1)^2\le\alpha:=\frac{b+\ell}{8},\\
 \mathbb E|\nabla u_i|^2\le\frac{\kappa b}{4},\qquad
 \mathbb E|f_i-u_i|^2
       \le z_0:=\frac{3b}{16}+\frac{\ell}{8},\\
 \mathbb E|W^+/\kappa+Q(u_i)|^2
       \le e_0:=\frac p4+\frac{27b}{16}+\frac{19\ell}{12}.
 \end{gathered}
 \tag{13}
\]

The last inequality uses \(T-A\le0\) in the exact capped
Hodge--Chern--Weil identity, not equality of these numbers.
Also, the exact determinant-curvature formula gives

\[
 \mathbb E|f_i|^2
 =r+\frac{\|\mathcal F_i^-\|_2^2}{\kappa^2V}
 \le r+\frac b8\le\frac{19}{16}.
 \tag{14}
\]

In particular all the full two-forms \(f_i\), including their
anti-self-dual parts, have a controlled global norm.

Choose a measurable unit vector \(v_i\) along \(u_i\) where it is
nonzero and any measurable unit vector at its zeros. Such a
measurable choice in \(\Lambda^+\) exists using finitely many local
trivializations. Then

\[
 \mathbb E|u_i-v_i|^2\le\alpha,\qquad
 \mathbb E|Q(u_i)-Q(v_i)|^2\le6\alpha.
 \tag{15}
\]

Indeed \(Q(u_i)=|u_i|^2Q(v_i)\),
\(|Q(v_i)|^2=2/3\), and \(|u_i|+1\le3\).
The common tensor \(W^+\) in (13) gives

\[
 \mathbb E|Q(u_i)-Q(u_1)|^2\le4e_0.
 \tag{16}
\]

Combining the three differences in (15)--(16),

\[
 \mathbb E|Q(v_i)-Q(v_1)|^2\le36\alpha+12e_0.
 \tag{17}
\]

For unit vectors \(v,w\),

\[
 |Q(v)-Q(w)|^2=2(1-\langle v,w\rangle^2),\qquad
 \min_{\sigma=\pm1}|v-\sigma w|^2
       =2(1-|\langle v,w\rangle|)
       \le|Q(v)-Q(w)|^2.
 \tag{18}
\]

Set \(n=v_1\), and choose \(\sigma_i\) by this minimum, resolving
zero scalar products measurably. Take \(\sigma_1=1\). Equations
(15)--(18) imply

\[
 \mathbb E|u_i-\sigma_i n|^2
 \le74\alpha+24e_0
 \le50\epsilon .
 \tag{19}
\]

This treats low-amplitude and zero sets by their amplitude cost,
not by deleting them without an error estimate.

The full determinant curvatures satisfy

\[
 \mathbb E|f_i-\sigma_i n|^2
 \le2z_0+100\epsilon\le101\epsilon .
 \tag{20}
\]

Using the Hodge star and the actual Chern classes,

\[
 \mathbb E\langle f_i,*f_j\rangle
 =\frac1V\int f_i\wedge f_j
 =\frac{2\pi^2}{\kappa^2V}\,a_i\cdot a_j
 =rG_{ij}.
 \tag{21}
\]

Because \(n\) is self-dual, (14), (20), and Cauchy--Schwarz yield

\[
 |rG_{ij}-\mathbb E(\sigma_i\sigma_j)|
 \le\sqrt{101\epsilon}
                 \left(\sqrt{19/16}+1\right)
 \le22\sqrt\epsilon .
 \tag{22}
\]

The distribution of the finite-valued vector
\((\sigma_1,\ldots,\sigma_m)\) under normalized volume defines
\(C\in\mathcal C_m\). Since \(|C_{ij}|\le1\), (4) gives

\[
 |G_{ij}-C_{ij}|
 \le\frac{22\sqrt\epsilon+\epsilon/16}{15/16}
 \le24\sqrt\epsilon .
 \tag{23}
\]

This proves Theorem 1. Pairing with \(nn^{\mathsf T}\) proves (10).
For (11), if \(\epsilon\le1\), rearrange (10); if
\(\epsilon>1\), the displayed minimum is automatic.

## 4. A smooth observable makes switching cost measurable

Projective alignment alone does not stop signs occupying different
large regions. Its new differential consequence comes from the
*smooth* function

\[
 h_{ij}=\langle u_i,u_j\rangle.
 \tag{24}
\]

Let \(\lambda_1(g)>0\) be the first positive eigenvalue of the scalar
Laplacian on the connected closed manifold, and let
\(q=G_{ij}\) with \(|q|\le1\).

**Theorem 2 (intersection-forced small eigenvalue).**

\[
 \boxed{
 \frac{\lambda_1(g)}{\kappa}
       \bigl(1-q^2-64\sqrt\epsilon\bigr)_+
 \le4b .}
 \tag{25}
\]

In particular, if \(|q|<1\) and
\(\epsilon\le(1-q^2)^2/128^2\), then

\[
 \boxed{
 \frac{\lambda_1(g)}{\kappa}
 \le\frac{8}{1-q^2}\,
       \frac{\int s^2-32\pi^2A}{\kappa^2V}.}
 \tag{26}
\]

Thus normalized scalar-energy saturation with uniformly nonextremal
intersection forces the scalar spectral gap to vanish. A lower
spectral bound is a possible additional obstruction, not a hidden
premise of the theorem.

**Proof.** The bounds \(|u_i|,|u_j|\le2\) and (13) give

\[
 |dh_{ij}|^2
 \le8(|\nabla u_i|^2+|\nabla u_j|^2),\qquad
 \mathbb E|dh_{ij}|^2\le4\kappa b.
 \tag{27}
\]

Equation (19) and the triangle inequality in normalized \(L^2\) give

\[
 \|h_{ij}-\sigma_i\sigma_j\|_{L^2(d\mu/V)}
 \le3\sqrt{50\epsilon}.
 \tag{28}
\]

In particular,
\(\mathbb E h_{ij}^2\ge1-2\sqrt{450\epsilon}\).
The comparison with the actual intersection, using (13)--(14)
without the measurable signs, is

\[
 |\mathbb E h_{ij}-rq|
 \le\sqrt{z_0}\left(\sqrt{19/16}+2\right)
 \le2\sqrt\epsilon .
 \tag{29}
\]

Since \(|q|\le1\), (4) implies
\(|\mathbb E h_{ij}-q|\le3\sqrt\epsilon\).
Also \(|h_{ij}|\le4\); hence
\[
 |(\mathbb E h_{ij})^2-q^2|\le15\sqrt\epsilon .
 \tag{30}
\]
It follows that
\[
 \operatorname{Var}(h_{ij})
 \ge1-q^2-(2\sqrt{450}+15)\sqrt\epsilon
 \ge1-q^2-64\sqrt\epsilon.
 \tag{31}
\]

The variational definition of \(\lambda_1\), applied to the globally
smooth function \(h_{ij}-\mathbb E h_{ij}\), now gives (25).
There is no differentiation of \(n\), \(v_i\), or \(\sigma_i\).
Equation (26) follows by absorbing half of \(1-q^2\). \(\square\)

A useful equivalent consequence is that if
\(\lambda_1(g)/\kappa\ge\lambda_*>0\) and \(|q|<1\), then

\[
 \epsilon\ge
 \min\left\{1,\frac{(1-q^2)^2}{128^2},
                     \frac{\lambda_*(1-q^2)}8\right\}.
 \tag{32}
\]

The spectral input in (32) must be proved for the metrics in question;
it is not inferred from non-virtual-Kähler topology.

### Several independent phase modes

Relabel a collection of \(n+1\) actual classes as
\(a_0,a_1,\ldots,a_n\), retaining (1)--(5). Set
\[
 \Sigma_{ij}=G_{ij}-G_{0i}G_{0j}\qquad(1\le i,j\le n).
 \tag{32a}
\]
This is a specified topological matrix. At finite error it is not
assumed positive semidefinite.

**Theorem 3 (intersection-forced spectral cluster).** Suppose
\(\Sigma\) has at least \(r_0\) eigenvalues at least \(s_0>0\).
Then
\[
 \boxed{
 \frac{\lambda_{r_0}(g)}{\kappa}
          (s_0-160n\sqrt\epsilon)_+\le4nb .}
 \tag{32b}
\]
In particular, if \(\epsilon\le(s_0/(320n))^2\), then
\[
 \boxed{\frac{\lambda_{r_0}(g)}{\kappa}\le\frac{8n}{s_0}b.}
 \tag{32c}
\]
Here \(\lambda_j\) are the positive scalar-Laplacian eigenvalues,
counted with multiplicity.

**Proof.** Let \(h_i=\langle u_0,u_i\rangle\). These are globally
smooth. Take the common signs from Theorem 1 with \(\sigma_0=1\).
Equations (27)--(29) apply to every \(h_i\), giving
\[
 \mathbb E|dh_i|^2\le4\kappa b,\qquad
 \|h_i-\sigma_i\|_{L^2(d\mu/V)}\le\sqrt{450\epsilon}.
 \tag{32d}
\]
In addition, (14) and (21) imply
\[
 |G_{ij}|\le1+\frac{b}{8r}\le\frac{17}{15}.
 \tag{32e}
\]
The proof of (29), (4), and (32e) give
\(|\mathbb Eh_i-G_{0i}|\le3\sqrt\epsilon\) without the extra
assumption \(|G_{0i}|\le1\).
Since \(|h_i|\le4\) and \(|\sigma_i|=1\), (32d) yields
\[
 |\mathbb E(h_ih_j)-\mathbb E(\sigma_i\sigma_j)|
        \le5\sqrt{450\epsilon}.
 \tag{32f}
\]
Using (7), and then comparing the products of the means, gives
\[
 \begin{split}
 |\mathbb E(h_ih_j)-G_{ij}|
       &\le(5\sqrt{450}+24)\sqrt\epsilon,\\
 |(\mathbb Eh_i)(\mathbb Eh_j)-G_{0i}G_{0j}|
       &\le16\sqrt\epsilon.
 \end{split}
 \tag{32g}
\]
Thus the actual covariance matrix \(\Gamma\) of the smooth
functions \(h_i\) satisfies
\[
 \max_{ij}|\Gamma_{ij}-\Sigma_{ij}|
      \le160\sqrt\epsilon,\qquad
 \|\Gamma-\Sigma\|_{\rm op}\le160n\sqrt\epsilon.
 \tag{32h}
\]

Let \(E\subset\mathbb R^n\) be an \(r_0\)-dimensional spectral
subspace of \(\Sigma\) on which \(\Sigma\ge s_0I\).
For \(t\in E\), set
\(H_t=\sum_i t_i(h_i-\mathbb E h_i)\).
If \(s_0-160n\sqrt\epsilon>0\), then
\[
 \mathbb E H_t^2\ge(s_0-160n\sqrt\epsilon)|t|^2,\qquad
 \mathbb E|dH_t|^2\le4n\kappa b\,|t|^2.
 \tag{32i}
\]
The first estimate makes \(t\mapsto H_t\) injective. Its image is
therefore an \(r_0\)-dimensional space of mean-zero smooth
functions. The scalar min--max principle proves (32b); when the
positive part vanishes, (32b) is automatic. Equation (32c) follows.
\(\square\)

This conclusion counts genuine scalar low modes. It is stronger
than an upper bound on a connection-Laplacian eigenvalue of a
two-form: the test functions are obtained from pairings of
different actual classes and have topologically forced variance.

## 5. Actual connected-sum application outside the shear category

Let \(X\) and \(Y\) be compact almost-complex four-manifolds with
\(b_1=0\), \(b_+\equiv3\pmod4\), odd canonical Seiberg--Witten
invariant, and positive canonical squares \(A_X,A_Y\).
The Bauer--Furuta connected-sum theorem gives actual monopoles

\[
 a=c_1(X)+c_1(Y),\qquad
 c=c_1(X)-c_1(Y)
 \tag{33}
\]

on \(M=X\#Y\). Their squares and pairing are

\[
 A=A_X+A_Y,\quad T=A-4,\quad
 q=\frac{a\cdot c}{A}
       =\frac{A_X-A_Y}{A_X+A_Y},\quad
 1-q^2=\frac{4A_XA_Y}{(A_X+A_Y)^2}.
 \tag{34}
\]

The actual-class input, including independent signs, is classical;
see [Ishida--LeBrun, *Curvature, Connected Sums, and
Seiberg--Witten Theory*, Proposition 6, Theorem 9 and
Proposition 10](https://arxiv.org/pdf/math/0111228).
For two summands the fourth-summand congruence in their common
statement is unnecessary; alternatively it can be met by adding
auxiliary almost-complex examples before applying the theorem with
\(m=2\).

Equations (25)--(26) apply to every metric of negative mean scalar
curvature on this actual smooth connected sum. If both components
contribute a uniformly positive fraction of \(A\), any sequence
with \(\epsilon\to0\) must have \(\lambda_1/\kappa\to0\).
This identifies a genuine global low-frequency mode; it is not a
claim that the connected sum has already been constructed with
pointwise Ricci error tending to zero.

### Explicit growing family and several small eigenvalues

Take a smooth degree \(d\) hypersurface
\(X_d\subset\mathbb{CP}^3\), where \(d\ge8\) is divisible by four,
and let \(M_d=X_d\#X_d\).
Adjunction and the hyperplane class \(H\) give
\(K_{X_d}=(d-4)H|_{X_d}\), \(H^2[X_d]=d\), so

\[
 A_X=d(d-4)^2,\qquad
 A_d=2d(d-4)^2,\qquad T_d=A_d-4.
 \tag{35}
\]

The hypersurface sequence and
\(H^1(\mathbb{CP}^3,\mathcal O(-d))=
 H^2(\mathbb{CP}^3,\mathcal O(-d))=0\)
give \(q(X_d)=0\). Its Kähler Hodge decomposition gives
\[
 p_g(X_d)=\binom{d-1}{3},\qquad
 b_+(X_d)=1+2\binom{d-1}{3}\equiv3\pmod4 .
 \tag{36}
\]
For \(d=4j\), the binomial coefficient equals
\((4j-1)(2j-1)(4j-3)/3\), an odd integer.
The canonical invariant is \(\pm1\), by
[Taubes, *More Constraints on Symplectic Forms from Seiberg--Witten
Invariants*, Theorem 1](https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/1995/0002/0001/MRL-1995-0002-0001-a002.pdf).
Thus (33) applies. One can literally meet the four-factor
version of Theorem 9 with \(X_d,X_d,K3,K3\):
their \(b_+\)-sum is \(4\pmod8\).

For the two classes in (33), \(q=0\). Hence every metric on \(M_d\)
with \(\epsilon\le1/128^2\) satisfies

\[
 \boxed{\frac{\lambda_1(g)}{\kappa}\le8b.}
 \tag{37}
\]

Here \(A_d\to\infty\) and \(T_d/A_d\to1\). This is the natural
regime in which normalized errors could vanish without pretending
that the fixed connected-sum topological loss disappears.

More generally take
\[
 M_{m,d}=\#_{j=1}^{m}X_d,\qquad m\in\{2,3,4\},\qquad
 A_{m,d}=m\,d(d-4)^2,\quad T_{m,d}=A_{m,d}-4(m-1).
 \tag{37a}
\]
Four identical \(X_d\) satisfy the total \(b_+\) congruence in the
four-factor Bauer theorem, since \(4b_+(X_d)\equiv4\pmod8\).
Thus all the signed sums of the \(c_j=c_1(X_d)\) are actual
monopoles. Choose
\[
 a_0=\sum_jc_j,\qquad a_i=a_0-2c_i\quad(1\le i\le m).
 \tag{37b}
\]
Their intersection covariance is exactly
\[
 \Sigma=4\left(\frac1m I-\frac1{m^2}\mathbf1\mathbf1^{\mathsf T}\right).
 \tag{37c}
\]
It has rank \(m-1\), with every positive eigenvalue \(4/m\).
Theorem 3, with \(n=m\), therefore gives
\[
 \boxed{
 \epsilon\le\frac1{(80m^2)^2}
 \quad\Longrightarrow\quad
 \frac{\lambda_{m-1}(g)}{\kappa}\le2m^2b.}
 \tag{37d}
\]
In particular, relative scalar/Ricci saturation on the growing
three- or four-summand families forces, respectively, at least two
or three scalar low modes. The argument does not assume that the
unknown metrics have visible necks, respect the connected-sum
presentation geometrically, or converge to separate components.

### The relative-saturation hypothesis is realized by actual metrics

For fixed \(m\in\{2,3,4\}\), these growing connected sums do admit
metrics with
\[
 B=O_m(1),\qquad P=O_m(1),\qquad L=O_m(1),\qquad
 \kappa\longrightarrow1,\qquad
 \epsilon=O_m(A_{m,d}^{-1}).
 \tag{37e}
\]
Here the norms are integral, not pointwise.

To see this, endow each \(X_d\) with its negative
Kähler--Einstein metric normalized by \(\operatorname{Ric}=-g\).
Its canonical bundle is ample because \(d>4\), so the classical
negative Kähler--Einstein existence theorem applies. Its volume is
\(2\pi^2d(d-4)^2\).
Choose finitely many distinct attachment points. For each \(d\),
choose a common radius \(t_d\to0\) so small that on each attachment
ball the rescaled normal-coordinate metric is as close to Euclidean
as desired in \(C^2\) on a fixed annulus. No uniform original
curvature bound as \(d\) varies is required for this choice.

Remove the small balls and join adjacent components by a fixed
smooth two-ended spherical connector scaled by \(t_d^2\).
Choose that connector to equal Euclidean radial annuli near its
ends. A fixed cutoff interpolates the rescaled original annular
metric to the Euclidean end metric. The rescaled transition and
connector metrics have uniform positive definiteness and \(C^2\)
bounds on fixed compact domains. In dimension four their
\(\int|\operatorname{Ric}|^2\) and \(\int s^2\) are invariant under
constant scaling, so the total cost of these finitely many regions
is \(O_m(1)\). Their volume is \(O_m(t_d^4)\), and their absolute
scalar integral is \(O_m(t_d^2)\).

Off these regions the original metrics are unchanged and Einstein.
Thus
\[
 \begin{split}
 V&=2\pi^2 A_{m,d}+O_m(t_d^4),\\
 \int s&=-4V+O_m(t_d^2),\\
 \int s^2&=32\pi^2A_{m,d}+O_m(1),\qquad P=O_m(1).
 \end{split}
 \tag{37f}
\]
Equation (8) of Round 17 ensures \(B\ge0\). The middle line gives
\(\kappa=1+O_m(t_d^2/V)\). On the unchanged region the contribution
to \(L\) is \(16(\kappa-1)^2\) times its volume; on the surgery
region the preceding \(L^2\) estimates give \(O_m(1)\). This proves
(37e).

This is the classical scale-critical connected-sum energy
construction, used only to show nonvacuity. It does **not** give a
Yau26 input with small \(L^\infty\) Ricci error: the connector can
have curvature of order \(t_d^{-2}\).
The new all-metric conclusion is that **any** sequence on these
smooth types with the same relative saturation, not just this
explicit neck sequence, must have at least \(m-1\) small scalar
eigenvalues. For the metrics in (37e), (37d) gives
\(\lambda_{m-1}/\kappa=O_m(A_{m,d}^{-1})\).

For a fixed \(M_d\), absolute simultaneous saturation is already
impossible. The signed identity of Round 17 gives
\[
 \frac14P+\frac{27}{16}B+\frac{19}{12}L\ge8\pi^2,
 \tag{38}
\]
because \(T_d-A_d=-4\). The new assertion is the spectral
restriction on *relative* saturation, not a rediscovery of a fixed
connected-sum curvature-energy gap. Ishida--LeBrun's same paper
already establishes sharp absolute Ricci-energy bounds for these
connected sums (Theorem C).

## 6. What is additional to the earlier Hodge and Walsh arguments?

The scalar inequalities alone bound projected class lengths and
imply pairwise Cauchy--Schwarz constraints. They do not algebraically
force membership in \(\mathcal C_m\). For example,

\[
 G_*=
 \begin{pmatrix}
 1&-1/2&-1/2\\
 -1/2&1&-1/2\\
 -1/2&-1/2&1
 \end{pmatrix}
 \tag{39}
\]

is positive semidefinite and satisfies every pairwise bound
\(|G_{ij}|\le1\), but \(\mathbf1^{\mathsf T}G_*\mathbf1=0\),
whereas every \(C\in\mathcal C_3\) has
\(\mathbf1^{\mathsf T}C\mathbf1\ge1\).
This is a linear-algebra separation, not a claim that \(G_*\) is
realized by actual monopole classes.

[Round 2](round2_rigidity.md) obtained measurable projective
alignment and spatial phase separation at the different, forbidden
calibration, including a full monopole sign cube. This note neither
recounts that as new nor assumes its sign-cube hypothesis. It uses
the realizable calibration and the actual determinant curvatures to
produce a joint intersection distribution, and then uses bounded
first derivatives to obtain the scalar spectral estimate (25).
This latter estimate quantifies the previously uncontrolled global
phase-switching alternative.

For the closed shear manifolds, the known ordinary basic set in
one orientation is only \(\{\pm a\}\), so \(q=\pm1\); (25) is
correctly uninformative. The opposite-orientation class cannot be
inserted as another self-dual class. This theorem does not
manufacture additional monopoles on those manifolds.

Finally, (21) integrates over all of \(M\). No \(L^2\)-to-cycle
trace estimate is used. For a closed test two-form \(\theta\),
Round 17 also gives the direct period-duality estimate

\[
 \left|2\pi\,a_i\cdot[\theta]
       -\frac1{2\sqrt2}\int\varphi_i\wedge\theta\right|
 \le\sqrt{\frac38B+\frac14L}\,\|\theta\|_2.
 \tag{40}
\]

If one wants periods on a degenerating family of cycles, one must
still supply controlled dual forms \(\theta\); their norms do not
become bounded merely because the cycles are topologically fixed.

## 7. Scope and verification

Theorems 1--3 concern any metrics satisfying the stated actual
monopole assumptions. They do not require an Einstein equation or
a geometric ansatz. For a near-negative-Einstein input,
\(P+L/4=\int|\operatorname{Ric}+\kappa g|^2\);
scalar-energy saturation controls the remaining \(B\).
Thus they constrain a possible Yau26 input sequence in a different
topological category from the closed shear examples.

A small \(\lambda_1\) is not itself a contradiction. The next
mathematical question is whether a proposed topology and Ricci
pinching admit the required low-frequency phase mixing, or whether
an independently proved spectral, capacity, or geometric bound
prevents it. Neither its prevention nor a new sign-branch solution
is claimed here.

[The accompanying exact checks](round18_periods_check.py) verify
the projective-distance identities, all coefficient bounds,
normalization of the wedge pairing, the finite sign constraints,
the separating Gram example, and the hypersurface/congruence
application. The measurable-choice and analytic Rayleigh arguments
are proved above; finite computation does not replace them.
