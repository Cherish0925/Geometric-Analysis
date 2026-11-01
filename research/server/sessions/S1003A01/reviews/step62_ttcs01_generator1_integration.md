# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 62,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step62_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step62_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Closed negative Goldberg problem (closed 4-manifold, Einstein Ric=lambda g with lambda<0, almost-Kahler Omega; does Omega have to be Kahler?). New local result (attached note): at every torsion zero, |nabla^2 Omega|^2 = 4trV^2 - 12|eta|^2, so the first torsion jet lies on the cone ||A||^2=8|c|^2+||S||^2 and every nondegenerate zero has index +1; W3+ != 0 at every zero with nonzero first jet; the identity is lambda-independent and Ricci-flat Gibbons-Hawking degenerate zeros lie on it. Topology forces total torsion charge 5chi+6tau>0. Propose the strongest concrete next mathematical mechanisms that could turn this into a global obstruction or, conversely, into a construction of a negative-scalar closed or local counterexample germ with an isolated zero. Candidates to evaluate rigorously, not just list: (a) a next-order (cubic/third-jet) identity obtained from Delta^2 of the Weitzenbock identity or from Bianchi relations between nabla^2 W+ and nabla^3 Omega, and whether lambda can enter there; (b) a pointwise elliptic inequality for q or for |nabla Omega| near zeros (e.g. Delta q >= ... using the global AAD Weitzenbock), giving a maximum-principle or Morse/Poincare-Hopf argument tied to the forced positive charge; (c) combining index +1 with the localization of zeros in {lambda_min(W+)<=s/6} and the Hopf/linking-sphere picture; (d) a model local negative AKE germ with an isolated nondegenerate zero (e.g. a cohomogeneity-one or toric ansatz with a fixed point) that would show the local theory cannot close Goldberg. For each, state precisely what would have to be computed and what result would change the global judgment.

## Integrated Scientific Memo

# Scientific memo: what the zero cone can—and cannot—do for negative Goldberg

The new zero identity eliminates the negative-index **nondegenerate** first jets previously allowed by the half-twistor equation. It does not conflict with the global charge: positive-index zeros are exactly what \(5\chi+6\tau>0\) requires. The next mechanisms must therefore supply either:

- a sign-sensitive obstruction to **all** strict torsion-zero germs;
- a compactness-dependent restriction on how positive zeros coexist with the strict region;
- or an actual analytic negative-Einstein germ realizing an admissible isolated zero.

The strongest concrete computations are the full weight-six prolongation, a second-order-zero identity derived below, the Hessian of \(q\) at strict critical points, and a triaxial \(SU(2)\)-nut realization problem. Scalar differentiation or curvature localization alone is insufficient.

## 1. Normalization and the exact differential identity to prolong

Use throughout
\[
\Delta=\operatorname{tr}\nabla^2,\qquad
u=\Omega/\sqrt2,\qquad T=\nabla\Omega,\qquad q=|T|^2,
\]
and the **operator-block** convention
\[
W^+=
\begin{pmatrix}
r&\eta^T\\
\eta&-\frac r2 I+V
\end{pmatrix},
\qquad r=\frac s6+\frac q4,\qquad \operatorname{tr}V=0.
\]
Thus
\[
|W^+|^2-\frac{s^2}{24}
=2|\eta|^2+\operatorname{tr}V^2+\frac{sq}{8}+\frac{3q^2}{32}. \tag{1}
\]
The \(\eta\)-norm in some earlier notes is twice this operator-block norm.

The harmonic-form and Einstein Weyl equations are
\[
\Delta u=-2W^+u+\frac s3u,\qquad
\Delta W^+=\frac s2W^+-6(W^+)^2+2|W^+|^2I. \tag{2}
\]
Differentiating \(r=\langle W^+u,u\rangle\) gives an exact, usable global formula:
\[
\boxed{
\Delta q
=8\operatorname{tr}V^2-24|\eta|^2
-\frac{3s}{2}q-\frac94q^2
+16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle .
} \tag{3}
\]
Here the almost-Kähler gauge implies
\[
\sum_i\nabla_i u\otimes\nabla_i u
=\frac q4 I_{u^\perp},
\]
which simplifies the otherwise separate \(W^+\ast T\ast T\) term.

At a torsion zero, (3) becomes
\[
2|\nabla T|^2=8\operatorname{tr}V^2-24|\eta|^2,
\]
recovering Step 62. For \(f(z)=cz+(S+A)\bar z\),
\[
\|A\|^2=8|c|^2+\|S\|^2,\qquad
\det_{\mathbb R}Df=9|c|^4+|\det(S+A)|^2\ge0. \tag{4}
\]
Consequently every nondegenerate zero has index \(+1\), and every zero with \(\nabla T\ne0\) has
\[
\operatorname{tr}V^2=\frac14|\nabla T|^2+3|\eta|^2,\qquad
|W^+|^2-\frac{s^2}{24}
=\frac14|\nabla T|^2+5|\eta|^2>0. \tag{5}
\]

Equation (3), rather than a conjectural “global cone identity,” is the correct starting point. Away from zeros, \(\nabla^b\alpha\), \(\nabla T\), and the curvature pieces differ by torsion-dependent terms; their identification must be computed before extending (4) pointwise.

## 2. Candidate (a): full prolongation, not a lone \(\Delta^2\) scalar equation

### 2.1 Where scalar curvature can enter

At a zero write
\[
K=\nabla T,\qquad L=\nabla^2T,\qquad U=\nabla W^+.
\]
The scaling weights are
\[
[s]=[K]=[W]=2,\qquad [L]=[U]=3.
\]
Thus weight six permits
\[
s\,Q_2(K),\qquad W\ast K\ast K,\qquad |L|^2,\qquad
K\ast\nabla^3T,
\]
as well as contractions involving curvature derivatives. In particular, scalar curvature can enter the degree-six system through a quadratic expression in the first torsion jet.

This does **not** mean it first appears anywhere at degree six: differentiated equations already contain \(s\) at odd order. What first becomes possible at weight six is a scalar-curvature-dependent **quadratic restriction on \(K\)**.

For the rough-Laplacian polynomial
\[
P_s(W)=-\frac s2W+6W^2-2|W|^2I,
\]
its derivative at
\[
W_0=\operatorname{diag}(s/6,-s/12,-s/12)
\]
has eigenvalues
\[
\frac s2,\quad 0,\quad-\frac{3s}{2} \tag{6}
\]
on the scalar Kähler ray, \(W_2^+\), and \(W_3^+\), respectively. The \(V\)-piece therefore has positive rough-Laplacian mass when \(s<0\).

This is useful structural information, not coercivity: at a zero with \(K\ne0\), \(W^+(p)\ne W_0\), and the omitted nonlinear and higher-jet terms may absorb that mass.

### 2.2 Why \(\Delta^2q\) alone is unlikely to restrict \(K\)

At \(T=0\),
\[
\Delta^2|T|^2
=4|\nabla^2T|^2+2|\Delta T|^2
+8\langle\nabla T,\nabla\Delta T\rangle
+\text{curvature-commutator terms}. \tag{7}
\]
The last pairing couples \(K\) to higher jets. Eliminating traced derivatives using (2) does not automatically eliminate all those higher jets. Thus neither a cubic identity nor a sum of squares in \(K\) follows simply by applying another Laplacian.

The decisive finite-dimensional object is the projection of the **full prolonged system** onto the first-jet cone:
\[
\pi_D:\{\text{Einstein–AK jets through order }D\}\longrightarrow
\{(c,A,S):\|A\|^2=8|c|^2+\|S\|^2\}. \tag{8}
\]
It must retain:

- differentiated closure and compatibility of \(\Omega\);
- the soldered half-twistor equation and differentiated Ricci identities;
- \(\delta W^+=0\) and its derivatives;
- curvature commutators, including the \(W^-\) contributions;
- the Einstein equations in a fixed gauge.

A useful algebraic procedure is to solve the new highest-order jets linearly and project their forcing terms onto the cokernel. The resulting obstruction polynomials—not raw equation counts—are the potential new restrictions on \(K\).

The reported Step-62 degree-four residuals are numerical compatibility evidence, not exact existence. No completed degree-five result is supplied.

**Results that change the judgment.**

1. A cokernel identity
   \[
   0=(-s)C|K|^2+\sum_\rho|\mathcal L_\rho|^2,\qquad C>0,
   \]
   would exclude all first-order zeros for \(s<0\). It would still leave higher-order zeros and zeros with a rank-deficient nonzero \(K\).

2. Surjectivity of (8) at degrees five and six over an open nondegenerate sector would substantially weaken a low-order local obstruction. It would not establish an actual germ.

3. Formal integrability at an ordinary integral element, followed by a convergence theorem, or an explicit convergent ansatz, would establish local existence.

Odd-order equations can also have nontrivial cokernels; parity alone does not prove they merely solve for higher jets.

### 2.3 A new exact identity for zeros of order at least two

There is a further local consequence available directly from (2).

Suppose
\[
T(p)=0,\qquad \nabla T(p)=0.
\]
Then
\[
W^+(p)=W_0,\qquad \nabla u(p)=\nabla^2u(p)=0.
\]
Set
\[
L=\nabla^2T=\nabla^3\Omega,\qquad U_i=\nabla_iW^+.
\]
Since \(dr(p)=0\), write
\[
U_i=
\begin{pmatrix}
0&\eta_i^T\\
\eta_i&V_i
\end{pmatrix},\qquad \operatorname{tr}V_i=0.
\]
Let
\[
E=\sum_i|\eta_i|^2,\qquad F=\sum_i\operatorname{tr}V_i^2.
\]
The differentiated harmonic-form equation gives
\[
\Delta T(p)=-2\sqrt2\,U_i u,\qquad |\Delta T|^2=8E.
\]
Moreover, \(P_s(W_0)=0\), so applying \(\Delta\) to the Weyl equation at \(p\) yields
\[
\Delta^2W^+
=-12\sum_iU_i^2+4\sum_i|U_i|^2I.
\]
Applying \(\Delta^2\) to \(r=\langle W^+u,u\rangle\), the surviving product terms give
\[
\Delta^2r=4F-20E.
\]
Meanwhile
\[
\Delta^2q=4|L|^2+16E=4\Delta^2r.
\]
Hence
\[
\boxed{
|\nabla^3\Omega|^2(p)
=4\sum_i\operatorname{tr}V_i^2
-24\sum_i|\eta_i|^2 .
} \tag{9}
\]

This identity is again \(\lambda\)-independent. It is the concrete second-jet analogue of Step 62, with coefficient \(24\), not \(12\), on the differentiated off-diagonal block.

The remaining calculation is exact and finite: solve the degree-two homogeneous half-twistor equation, impose differentiated curvature soldering and Bianchi relations, express \(E,F\) in its coefficients, and determine the signature and zero set of (9). Merely treating \(U\) and \(L\) as independent misses the restriction.

At a higher-order zero, \(s\) multiplies lower vanishing jets and therefore disappears from the lowest homogeneous compatibility. A sign-sensitive obstruction must generally occur at a **subleading** order. Linearized mass (6) alone cannot exclude all finite vanishing orders.

## 3. Candidate (b): scalar inequalities versus the topology of strict critical points

### 3.1 The maximum-principle direction matters

At a nondegenerate zero,
\[
q(x)=|Kx|^2+O(|x|^3),\qquad
\operatorname{Hess}q(p)=2K^*K>0,\qquad
\Delta q(p)=2|K|^2>0. \tag{10}
\]
Thus a lower bound such as \(\Delta q\ge-Cq\) does not exclude zeros: it is consistent with a nonnegative function having a strict minimum.

An estimate
\[
\Delta q\le Cq
\]
would exclude a zero by the strong minimum principle, but it would contradict the admissible nondegenerate zero jets unless derived from genuinely additional compatibility. Equation (3) displays the obstruction to a naive derivation: the \(\nabla W^+\ast T\) term has no obvious pointwise sign.

The refined Kato constant \(3/4\) from Step 75 can improve exponents in inequalities for \(|\alpha|^\gamma\); it does not remove this curvature-derivative coupling or fix the negative-scalar sign.

A curvature-coupled quantity is more plausible. Dimensionally suitable choices include
\[
F=q+\frac{\gamma}{|s|}
\left(|W^+|^2-\frac{s^2}{24}\right),\qquad s<0.
\]
The additional exact equation is
\[
\frac12\Delta|W^+|^2
=|\nabla W^+|^2+\frac s2|W^+|^2-18\det W^+. \tag{11}
\]
The substantive calculation is to decompose the cross term in (3), absorb it using the gradient term in (11), and optimize \(\gamma\). A resulting inequality must have a useful sign at a **compactly attained** extremum.

The complete strict example tests specific claims: \(q\) has an interior bolt maximum, so no universally subharmonic nonconstant \(q\) is possible. This does not rule out every coupled scalar or every compact maximum-principle argument.

### 3.2 A concrete global consequence: forced negative critical charge

Assume all torsion zeros are nondegenerate and the remaining critical points of \(q\) are isolated and Morse. Then
\[
N=\#Z=5\chi+6\tau.
\]
Every torsion zero is a minimum of \(q\) and contributes \(+1\) to the index of \(\nabla q\). Poincaré–Hopf therefore gives
\[
\boxed{
\sum_{\substack{dq=0\\q>0}}\operatorname{ind}(\nabla q)
=\chi-N=-2(2\chi+3\tau)<0 .
} \tag{12}
\]
If \(O,E\) count odd- and even-Morse-index strict critical points,
\[
O-E=2(2\chi+3\tau).
\]
Thus a hypothetical closed example with simple torsion zeros requires at least \(2(2\chi+3\tau)\) odd-index strict critical points.

This is a genuine new global target, but a Laplacian controls only the trace of the Hessian—not its Morse parity.

At a strict critical point, with \(D=\nabla^b\alpha\),
\[
dq=0\quad\Longrightarrow\quad D^*\alpha=0,
\]
so \(D\) is singular. The exact local computation is therefore:

\[
\text{Einstein–AK jets with }q>0,\ dq=0
\quad\longmapsto\quad \operatorname{Hess}q.
\tag{13}
\]
In metric torsion coordinates,
\[
\operatorname{Hess}q(X,Y)
=2\langle\nabla_XT,\nabla_YT\rangle
+2\langle T,\nabla^2_{(X,Y)}T\rangle. \tag{14}
\]
Determine whether the allowed Hessians include odd-index signatures, or whether the equations force a Hermitian/even-index Hessian. Full freedom in the trace-free part would defeat a pointwise Morse-parity argument; an even-index theorem would contradict (12) under its hypotheses.

### 3.3 Critical surfaces and degenerate zeros cannot be suppressed

For a Morse–Bott critical component \(C\), its contribution is
\[
(-1)^{\nu(C)}\chi(C),
\]
where \(\nu\) is the normal Morse index. The supplied complete example has a genus-\(g\) bolt that is a normal maximum of \(q\): normal index \(2\), contribution \(2-2g<0\). Hence even normal index does not prevent negative critical charge.

Any compact obstruction must also control negative-Euler-characteristic critical surfaces or more general critical sets. Holomorphicity of such surfaces and the relation \(N_C^2=K_C\), verified for the explicit bolt, are **not** established for general AKE critical surfaces.

Likewise:

- an isolated degenerate zero of \(T\) is still a strict minimum of \(q\), with gradient index \(+1\);
- its torsion index is not determined by the first-jet determinant;
- a rank-deficient first jet does not imply an isolated zero at all.

The Gibbons–Hawking control validates the cone and its degenerate stratum; it does not supply a linking degree for an isolated zero.

## 4. Candidate (c): positive charge, Weyl localization, and a usable Hopf obstruction

### 4.1 Localization is stronger, but not yet quantitative

Every zero with \(K\ne0\) lies in
\[
\mathcal U=\{|W^+|^2>s^2/24\}.
\]
If \(c\ne0\), then \(\eta\ne0\), and
\[
\lambda_{\min}(W^+)<s/6.
\]
A nondegenerate zero with \(c=0\) may still lie on the eigenvalue threshold while having strict norm excess. These two thresholds must remain separate.

There is no contradiction in placing all \(5\chi+6\tau\) positive zeros in small balls in \(\mathcal U\). Nor does (5) give a universal Weyl-energy payment per zero. The jet amplitude may tend to zero, while the size of a controlled neighborhood depends on higher derivatives and geometry.

In particular, a universal excess-ball radius of order \(|s|^{-1/2}\) does not follow from (1): \(\eta\) and \(V\) vary, often already at linear order. Such a radius would require quantitative derivative and noncollapse assumptions.

### 4.2 The precise linking obstruction

At a nondegenerate zero, in a local trivialization,
\[
\widehat T:S^3\to S^3
\]
has degree \(+1\). Projectivizing the complex torsion vector gives
\[
[\alpha]:S^3\to\mathbb{CP}^1,\qquad
\operatorname{Hopf}([\alpha])=+1, \tag{15}
\]
with orientations fixed by the Euler-class convention.

Thus a local obstruction would follow from a curvature-derived complex tangent line that:

1. extends across the zero; and
2. is homotopic on the linking sphere to \([\alpha]\).

An extending line has zero Hopf invariant. Step 62 supplies \(V(p)\ne0\), which may permit inversion of a transverse curvature coefficient in a Bianchi-derived formula.

The missing theorem is **not** simply that \(V\ne0\): \(V\) acts on \(u^\perp\subset\Lambda^+\), whereas the torsion line lies in a twisted tangent representation. No supplied identity identifies those lines. Moreover, nonzero \(V\) does not guarantee a simple eigenvalue of the full \(W^+\).

The concrete calculation is to rewrite the differentiated AAD/Bianchi equations in spinor or unitary components and test whether they recover \([\alpha]\) as the image/kernel of a smooth tangent tensor involving \(V,\eta,\nabla W^+\). If the equations retain a freely rotating symmetric derivative \(S\), this curvature-extension mechanism fails.

### 4.3 An exact weighted-charge formula

Let \(\Psi_\nabla\) be the angular form on the unit sphere bundle of \(E\), normalized by
\[
d\Psi_\nabla=-\pi^*e(E),\qquad
\int_{S(E_x)}\Psi_\nabla=1.
\]
For isolated zeros and a smooth weight \(h\),
\[
\boxed{
\sum_p h(p)\operatorname{ind}_p(T)
=\int_Mh\,e(E)
-\int_{M\setminus Z}dh\wedge\widehat T^*\Psi_\nabla .
} \tag{16}
\]
Taking \(h\) to be a cutoff of the smooth Weyl excess in (1) turns localization into an exact differential identity.

The necessary computation is the second term in AAD variables. A sign estimate or a lower bound tied to a unit of charge would add information absent from the ordinary AAD balance. Smooth norm weights are not automatically incapable of using topology now that all nondegenerate indices are positive; however, they remain unsigned and require separate treatment of degenerate zeros.

For reference, the supplied AAD balance and (1) imply
\[
\boxed{
\int_M\left(|W^+|^2-\frac{s^2}{24}\right)
=-\int_M\left(\operatorname{tr}V^2+\frac{3q^2}{32}\right).
} \tag{17}
\]
Thus strict AKE geometry has negative **average** Weyl excess despite positive excess at simple zeros. Any quantitative localization method must estimate that competition.

The proposed Seiberg–Witten refinement in the branch material is potentially complementary, but its external curvature estimate and chamber hypotheses are not supplied here. It cannot be used as an established input. Also, numerical canonical-class conclusions from Hodge-index equality require a Kähler/Hodge setting; they do not follow for a general almost-Kähler manifold.

## 5. Candidate (d): a triaxial \(SU(2)\) nut is a credible local realization test

### 5.1 Symmetry sharply selects the possible first jets

At an \(SU(2)\) nut, the tangent representation is the fundamental complex representation, and the determinant twist is trivial. Therefore \(E_p\) has no invariant vector, forcing
\[
T(p)=0.
\]
The invariant real first derivatives consist of the scalar complex-linear and skew complex-antilinear modes:
\[
S=0,\qquad f=cz+A\bar z.
\]
The cone becomes
\[
\|A\|^2=8|c|^2.
\]
Every nonzero such jet has \(c\ne0\), and is automatically nondegenerate:
\[
|a|^2=4|c|^2,\qquad
\det_{\mathbb R}Df=25|c|^4>0. \tag{18}
\]
Thus this symmetry reduces the isolated-zero problem to finding a nonzero admissible amplitude.

It also forces \(W^-(p)=0\), while allowing a nontrivial \(W^+(p)\).

Two useful exclusions:

- At an effective \(T^2\) fixed point, tangent weights \(\xi_1,\xi_2\) are independent, whereas \(E\)-weights are \(2\xi_1+\xi_2,\xi_1+2\xi_2\). None matches a tangent weight up to sign, so invariant \(DT(p)=0\).
- At a \(U(2)\) nut, the central circle has weight \(1\) on the tangent representation and \(3\) on \(E\); **all** first-jet modes vanish. The earlier claim that only a pure \(c\)-mode survives is incorrect.

For a toric germ, the adjacent circle-fixed surfaces force torsion to vanish along those surfaces. Such an invariant fixed-point model cannot realize the requested isolated nondegenerate zero.

### 5.2 The actual ODE problem

Take
\[
d\sigma_i=2\sigma_j\wedge\sigma_k,\qquad
g=dt^2+\sum_i a_i(t)^2\sigma_i^2,
\]
with chirality chosen so that
\[
\omega_i=e^{0i}+e^{jk}
\]
extends to smooth self-dual forms at the nut, and put
\[
\Omega=\sum_i x_i(t)\omega_i,\qquad \sum_i x_i^2=1.
\]
Closure is
\[
(x_i a_j a_k)'=2x_i a_i. \tag{19}
\]
The diagonal Einstein equations are
\[
-\sum_i\frac{a_i''}{a_i}=\lambda,
\]
\[
-\frac{a_i''}{a_i}
-\frac{a_i'}{a_i}\left(\frac{a_j'}{a_j}+\frac{a_k'}{a_k}\right)
+\frac{2\bigl(a_i^4-(a_j^2-a_k^2)^2\bigr)}
{a_i^2a_j^2a_k^2}
=\lambda. \tag{20}
\]
Use regular-nut expansions
\[
a_i=t(1+\gamma_i t^2+\delta_i t^4+\cdots),\qquad
x_i=x_i^0+\xi_i t^2+\zeta_i t^4+\cdots.
\]
Then
\[
\sum_i\gamma_i=-\frac{\lambda}{6},
\]
and (19) gives
\[
\xi_i=\frac12\kappa_i x_i^0,\qquad
\kappa_i=6\gamma_i-4\sum_\ell\gamma_\ell.
\]
The first norm condition is
\[
\sum_i\kappa_i(x_i^0)^2=0. \tag{21}
\]
It is the zero Rayleigh identity. Higher norm coefficients must reproduce the zero cone and then test the new compatibility.

The essential calculations are:

1. Convert the polar series to quaternionic Cartesian coordinates and verify smoothness, chirality, and \(DT(0)\).
2. Solve Einstein recursion together with **all** coefficients of \(\sum x_i^2=1\); closure plus a unit initial value does not preserve norm automatically.
3. Determine whether a nonzero cone amplitude survives, particularly through the weight-six obstruction.
4. Establish convergence of the regular-singular recursion.

A change \(\rho=t^2\) is useful, but does not by itself yield an ordinary nonsingular analytic ODE. Convergence requires control of indicial equations/resonances or an applicable analytic existence theorem for the coupled constrained system.

A convergent nonzero branch proves a negative-scalar local strict AKE germ with an isolated index-\(+1\) zero. It would decisively rule out a universal local “no torsion zeros” proof of Goldberg.

Failure in this ansatz proves only a symmetric restriction unless the obstruction can be extracted invariantly from the full jet system. Merely changing Bianchi-VIII structure constants to Bianchi IX is not justified: positivity, real form, and regular-nut boundary conditions must all be recomputed.

Finally, continuous symmetry cannot persist in a closed negative-Einstein example: the Killing-field Bochner identity forces every Killing field to vanish when \(\lambda<0\). The nut is a local compatibility test, not a compact construction.

## Mathematical consequences that would genuinely decide the issue

| Computed result | Consequence |
|---|---|
| Sign-coercive full prolongation excluding every finite vanishing order | Analyticity and forced zeros yield closed Goldberg. |
| Exclusion only of nondegenerate first jets | Degenerate and higher-order zeros remain; no global conclusion yet. |
| Convergent \(SU(2)\)-nut or nonsymmetric germ realizing (4) | Universal local zero exclusion is false; compact obstructions must be genuinely global. |
| Even-index strict critical-point theorem, with control of critical components | Contradicts the negative critical charge (12). |
| Extending curvature line homotopic to the torsion line | Contradicts the local Hopf invariant (15). |
| Quantitative angular-form/energy estimate from (16) | Can connect positive zero charge to compact curvature budgets; localization alone cannot. |

The precise unresolved local object is an **analytic negative-Einstein almost-Kähler germ with an admissible nonzero first torsion jet**. The precise unresolved global object is a restriction on the strict region capable of balancing—or forbidding—the positive torsion charge together with the negative critical charge of \(q\). Equations (3), (9), (12), and (16) make those objects directly computable rather than merely suggestive.