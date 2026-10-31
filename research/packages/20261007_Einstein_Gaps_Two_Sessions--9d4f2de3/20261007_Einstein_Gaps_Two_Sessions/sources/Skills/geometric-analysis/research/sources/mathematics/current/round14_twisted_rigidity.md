# Twisted monopole extension and positive-b-plus connected sums

## 1. A larger analytic input than all-metric monopoles on a cover

The finite-cover criterion in `round14_rigidity.md` does not exhaust the
available gauge input. For its analytic proof, the cover equations only
need to be solvable for the **deck-invariant curvature weights actually
used by the proof**. Pin-minus monopoles supply exactly this input,
including on connected sums whose ordinary Seiberg--Witten invariants
vanish. The argument below checks that restriction explicitly.

**Invariant-weight lemma.** Let \((\widetilde X,\widetilde g)\) be a
closed oriented four-manifold with a finite group of orientation-preserving
isometries \(G\). Fix one ordinary spin-c structure with real Chern class
\(\widetilde a\). Suppose that for every smooth positive \(G\)-invariant
function \(f\), the weighted equations

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi)                 \tag{1.1}
\]

have a solution in this structure. Then the integral calibration theorem
of round 4 holds for \((\widetilde X,\widetilde g,\widetilde a)\),
with its original universal constant and square cost. Solutions are not
required to be invariant, and no solvability on non-invariant metrics
or for non-invariant weights is asserted.

**Proof.** There are only three kinds of weight in the full proof chain.

1. The signed scalar inequality uses \(f=1\).
2. The spectral inequality uses \(f_\epsilon=\sqrt{q_\epsilon}\), where
   \(q_\epsilon\) is a positive smooth majorant of
   \(h=(-2s/3-2\lambda_{\min}(W^+))_+\), converging uniformly to \(h\).
3. The bounded-spinor estimate uses positive smooth majorants of
   \(f_0=\max\{\sqrt{\max(-s+\sqrt6|W^+|,3)},(-s)_+/4\}\).

Both \(h\) and \(f_0\) are \(G\)-invariant. Start with any smooth
majorant converging uniformly and replace it by
\(|G|^{-1}\sum_{\gamma\in G}f\circ\gamma\). This preserves positivity,
the majorant property and uniform convergence. The square root in case 2
also remains invariant. Thus (1.1) supplies every solution invoked in
round 3, Section 6, and round 4, Sections 3--6.

All subsequent operations take place on the smooth ordinary spinor and
line bundles upstairs: Weitzenbock identities, the Hessian estimate,
the determinant-curvature identity, the polynomial Weyl tensor and its
weak Bianchi self-test. They impose no equivariance condition on the
spinor or test tensor. The measurable lowest-eigenline projector need
not be selected equivariantly either; it is used only for pointwise
norm estimates. No additional weighted solution is requested at that
step. Therefore the proof and all constants are unchanged. QED.

## 2. Twisted integral-gap theorem

Let \(\pi:\widetilde X\to X\) be a nontrivial double cover of a closed
oriented four-manifold, and let \(\ell\) denote the associated real
sign local system. A genuine spin-c-minus structure has an associated
\(O(2)\) characteristic bundle and a twisted Euler class
\(a\in H^2(X;\ell)\). Assume that for the metric being tested its
Pin-minus equations have solutions throughout that conformal class.
This assumption holds, in particular, for a nonzero Pin-minus basic
class with \(b_+^\ell\ge2\).

The required lifting statement is the one in
[Ishida--Matsuo--Nakamura, Section 2 and Proposition 8](https://arxiv.org/pdf/1505.05948):
the pulled-back structure is ordinary spin-c, with Chern class
\(\widetilde a=\pi^*a\), and a lifted twisted solution is an ordinary
Seiberg--Witten solution, after matching the constant spinor normalization.
Consequently conformal covariance supplies (1.1) for every positive
deck-invariant weight: the weight descends, the corresponding conformal
metric is still a metric on \(X\), and one lifts its solution before
applying the ordinary conformal transformation.

For the lifted metric, the harmonic projection and intersection form obey

\[
 \widetilde a^2=2a^2,\qquad
 (\widetilde a^+)^2=2(a^+)^2,\qquad
 \widetilde V=2V,\qquad \widetilde T=2T.                 \tag{2.1}
\]

Here products of two sign-local-system classes are untwisted. Pullback
commutes with the twisted Laplacian and with Hodge star; the factor two
in the norms is integration over the covering sheets. This verifies the
normalization rather than treating the twisted Euler class as an
ordinary Chern class downstairs.

**Theorem.** Suppose that for every metric \(g\) on \(X\) one may
select such a twisted class on a fixed double cover, with the same class
working for all weights in that conformal class, and

\[
                  (a_g^+)^2\ge A>0,\qquad a_g^2\ge T_X.
                                                               \tag{2.2}
\]

Then the existing universal constant gives

\[
 \boxed{\displaystyle
 \mathcal E_X(g)+\left(\frac{T_X}{A}-\frac23\right)_+
                  \ge c_*>0\qquad\hbox{for every }g.}           \tag{2.3}
\]

If the last square hypothesis is instead \(a_g^2\ge-C_A A\), the
corresponding constant is \(c(C_A)>0\). There is no degree loss or new
geometric condition.

**Proof.** Apply the invariant-weight lemma upstairs. The Hessian proof
uses the actual Hermitian positive-spinor bundle and its line connection
there, so there is no missing global complex structure on the downstairs
real spinor bundle. Its determinant energy remains

\[
 \int_{\widetilde X}|F_A|^2
    =2\int_{\widetilde X}|F_A^+|^2-4\pi^2\widetilde a^2.
\]

The normalized negative-square cost is
\(( -\widetilde a^2)_+/\widetilde V=(-a^2)_+/V\).
The lifted monopole quadratic form is sign-equivariant; its square
\(\psi\otimes\psi\), and hence
\(A_\psi=|\psi|^2I/24-\psi\otimes\psi/8\), is an ordinary
Weyl-operator model. Alternatively all testing may simply be performed
upstairs without descending this model. The topology-transfer algebra,
positive-sign scalar obstruction and optimization in the Einstein
constant are unchanged. Use (2.1) and exact invariance of
\(\mathcal E\) under pullback to obtain (2.3). QED.

The square hypothesis in (2.2) is explicit. It is **not** inferred from
the virtual dimension formula of arbitrary Pin-minus moduli spaces,
which differs from the ordinary SW dimension formula. The concrete
application below verifies it from the actual glued classes.

## 3. Concrete positive-b-plus surgeries

Let \(M\) be a closed oriented four-manifold with \(b_+(M)\ge2\)
and a spin-c structure with odd ordinary SW invariant and

\[
                     c^2=A=T_M=2\chi(M)+3\tau(M)>0.
\]

For example, any symplectic \(M\) with positive canonical square and
\(b_+\ge2\) supplies such a class. Let \(N\) have \(b_+(N)=0\),
set \(k=b_2(N)\), \(l=b_1(N)\), and let

\[
 Z=\mathop{\#}_{j=1}^{n}(S^2\times\Sigma_{r_j})
      \#\mathop{\#}_{i=1}^{m}(S^1\times Y_i),
 \qquad r_j\ge1,\qquad n+m\ge1,                        \tag{3.1}
\]

where the \(Y_i\) are arbitrary closed oriented three-manifolds. Put
\(X=M\#N\#Z\). The choice \(N=S^4\) simply means no \(N\) summand.
No Yamabe assumption on \(N\) or \(Y_i\) is imposed: only the
nonvanishing theorem, not the paper's Yamabe-equality conclusion, is used.

The classical input is
[Ishida--Matsuo--Nakamura, Proposition 9 and its proof](https://arxiv.org/pdf/1505.05948).
It provides actual Pin-minus basic classes, with independently selectable
exceptional signs, of the form

\[
 a=c+\sum_{j=1}^{k}\epsilon_j e_j+t,
 \qquad (a_g^+)^2\ge A,
 \qquad a^2=A-k.                                       \tag{3.2}
\]

Here the first summand is untwisted, the \(e_j\) form the negative
diagonal part, and \(t\) is the torsion twisted class on \(Z\).
The nonvanishing proof, including its local-system construction, is an
external gauge-theoretic input; the Euler-characteristic computation
alone does not produce these classes.

For connected sums, \(T(U\#V)=T(U)+T(V)-4\). Since
\(T_N=4-4l-k\), \(T_{S^2\times\Sigma_r}=8-8r\), and
\(T_{S^1\times Y}=0\), define

\[
       D=k+4l+\sum_{j=1}^{n}(8r_j-4)+4m.
\]

Then

\[
 T_X=A-D,\qquad a^2-T_X=D-k
          =4l+\sum_j(8r_j-4)+4m\ge0.                   \tag{3.3}
\]

The square condition in (2.2) is now verified. Thus

\[
 \boxed{\displaystyle
 \mathcal E_X(g)+\left(\frac13-\frac DA\right)_+\ge c_* .}
                                                               \tag{3.4}
\]

This permits positive-b-plus connected-sum summands, unlike the earlier
negative-definite connected-sum corollary. When at least one
\(S^2\times\Sigma_{r_j}\) occurs, ordinary SW and ordinary
stable-cohomotopy SW invariants vanish in this family, as noted in the
same paper's introduction. Their vanishing cannot be used to dismiss
the twisted input. Its double cover also has several positive-b-plus
connected-sum factors, so the proof must not pretend that it has an
ordinary nonzero SW invariant.

### An explicit critical family with vanishing ordinary invariants

For each \(j\ge1\), take

\[
 M_j=\Sigma_2\times\Sigma_{3j+1},\qquad
 Z_j=\mathop{\#}_{i=1}^{2j}(S^2\times T^2),\qquad
 X_j=M_j\#Z_j.
\]

The product canonical invariant is \(\pm1\), and

\[
 A_j=8(2-1)((3j+1)-1)=24j,\qquad
 D_j=4(2j)=8j,\qquad
 T_{X_j}=16j,\qquad \frac{T_{X_j}}{A_j}=\frac23.
\]

The new estimate therefore gives the uniform endpoint statement

\[
                  \boxed{\mathcal E_{X_j}(g)\ge c_*}
\]

for every \(j\) and every smooth metric. Ordinary SW and ordinary
stable-cohomotopy SW invariants vanish on these manifolds, while the
twisted classes in (3.2) remain available. This is the quantitative
critical situation: the classical strict exact inequality alone does
not supply a common positive gap for arbitrary metrics across this
infinite family.

### Application to the new closed shear manifolds

Take the smallest closed shear example from round 12:
\(\chi(M)=4\), \(\tau(M)=0\), \(b_+(M)=5\), hence \(A=8\).
The canonical invariant is \(\pm1\). For

\[
                         X=M\#(S^2\times T^2)
\]

one has \(D=4\), \(T_X=4\), and (3.4) becomes

\[
                          \mathcal E_X(g)\ge c_* .      \tag{3.5}
\]

The unmodified \(M\) admits the already constructed
\(\delta_-\to0\) metrics, but **no construction on this modified
smooth manifold can retain arbitrarily small integral Einstein defect**.
This excludes all pointwise near-Einstein constructions there as well.
It is an ansatz-independent conclusion, despite the ordinary invariants
of the modified manifold being zero. Ricci-flat metrics are separately
excluded by the positive twisted monopole scalar estimate.

This last example has \(D/A=1/2\), strictly beyond the classical
critical ratio \(1/3\). A positive defect bound there is also available
from classical twisted curvature estimates away from equality. It is
a useful application to the current construction, not the appropriate
example on which to base the novelty of the quantitative endpoint.

## 4. Position relative to the known theorem

The cited 2016 paper already proves exact Einstein obstructions on this
connected-sum family; its Theorem 16 requires \(D<A/3\) for Einstein
existence. No priority is claimed for that classical obstruction or for
Pin-minus equations. The present consequence replaces a strict exact
threshold by the uniform, all-metric relative integral inequality
(3.4), using the existing self-test theorem with genuinely verified
twisted input.

The extension does not improve the unmodified closed shear ratio. Its
near-Einstein sequence bounds twisted projection budgets just as it
bounds ordinary ones; applying a twisted scalar inequality along that
sequence cannot create a larger budget for the same manifold.
The positive result is instead a new range of surgeries and quotients
to which the integral rigidity mechanism applies.

The finite checks in `round14_rigidity_check.py` include the factors of
two, the connected-sum loss and the explicit shear application. Weighted
solvability and the invariant-weight lemma are proved above, not tested
by those finite calculations.
