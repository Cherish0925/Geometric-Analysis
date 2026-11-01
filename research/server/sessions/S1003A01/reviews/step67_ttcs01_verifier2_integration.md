# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 67,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step67_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step67_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the corrected order-6 scalar functional scientifically. Read A02's Step-80 note/data and A01's independent verification. Develop a coordinate-free interpretation or at least a sharp invariant ansatz for the universal multiplier and Phi6 on the first-jet cone, respecting U(2) invariance and weighted homogeneity. Explain why F0,F1,F2 can each change sign, identify plausible invariant generators and dimensionless ratios, and propose exact symbolic/numerical experiments that could recover the formula without assuming the earlier false positivity. Also assess whether compact negative Einstein almost-Kahler geometry supplies any known pointwise/global control of the torsion-derivative-to-lambda ratio that could make this finite-order law globally useful.

## Integrated Scientific Memo

# Scientific memo: the corrected order-6 compatibility law

## 1. What the supplied computations establish

The corrected conclusion is **finite-order compatibility on part of the first-jet cone, not uniform positivity and not existence of an Einstein germ**.

A01’s independent evaluation confirms the three negative-\(\Phi _6\) reconstructions:

| first jet and \(\lambda\) | \(\Phi _6\) | smallest active Hessian eigenvalue | degree-6 Einstein residual |
|---|---:|---:|---:|
| gen2, \(0\) | \(-0.16527851\) | \(0.06756\) | \(6.16\times10^{-8}\) |
| gen2, \(-5\) | \(-0.23691161\) | \(0.005413\) | \(1.25\times10^{-7}\) |
| gen5, \(-5\) | \(-0.41612426\) | \(0.004679\) | \(7.69\times10^{-9}\) |

The cone residuals are approximately \(10^{-16}\), the first differentials have positive determinant, and the reduced scalar equation at the saved solution is satisfied to approximately \(10^{-15}\). The positive control instead retains \(\Phi _6=0.84191\) and a degree-6 residual of \(4.64\).

These are mutually consistent floating-point evaluations of the truncated equations. They strongly refute the earlier claim of uniform order-6 obstruction. They do not yet constitute exact algebraic solutions: the saved coefficients include \(\|H_8\|\) between \(5.8\times10^5\) and \(10^7\), so cancellation is substantial. Nor do they settle infinite-order formal or analytic existence.

Two qualifications matter:

* The law was computed on the **even branch**, with \(H_3=0\) and intended vanishing of odd coefficients. The saved \(H_5,H_7\) and odd residuals are small, not identically zero.
* The supplied material does not establish that this branch captures all higher data at an arbitrary torsion zero. Consequently, “every nondegenerate zero on a closed manifold satisfies this particular \(\Phi _6\le0\)” is stronger than the demonstrated result.

There is also an unresolved implementation discrepancy at the lsA jet with \(\lambda=-40\). The scan records a positive-definite rank-12 block and \(\Phi _6=-0.192207\), consistent with its quadratic fit; the reconstruction note reports a rank-13, ill-conditioned calculation and withdraws that value. The scan’s rank-13 record belongs to its other jet. Thus the negative scan value is not internally contradicted, but neither does it certify a reconstruction at that point.

## 2. A sharp, explicitly testable interpretation of the universal multiplier

Write
\[
E=\operatorname{Ric}(g)-\lambda g.
\]
The flat order-6 cokernel has dimension
\[
259=4\binom83+\binom73=224+35.
\]
This matches four degree-5 contracted-Bianchi identities and one degree-4 scalar compatibility. The observed 35 reduced rows, of which 34 are absorbed linearly, fit this interpretation.

More can be obtained directly from the flat symbol.

Let \(h\) be a symmetric variation satisfying
\[
h(JX,JY)=-h(X,Y).
\]
Then \(\operatorname{tr}h=0\). With the usual derivative-symbol convention, the linearized Ricci symbol is
\[
R'_\xi(h)_{ij}
=\frac12\left(
\xi_i h(\xi,e_j)+\xi_j h(\xi,e_i)
-|\xi|^2h_{ij}
-\xi_i\xi_j\operatorname{tr}h
\right).
\]
Consequently,
\[
\operatorname{tr}R'_\xi(h)=h(\xi,\xi),\qquad
R'_\xi(h)(J\xi,J\xi)
=\frac12|\xi|^2h(\xi,\xi).
\]
Thus the \(U(2)\)-invariant scalar symbol
\[
\boxed{
P_\xi(E)=E(J\xi,J\xi)-\frac12|\xi|^2\operatorname{tr}E
}
\tag{2.1}
\]
annihilates the flat Einstein operator on anti-\(J\) variations.

The other natural invariant symbols add no independent scalar obstruction: \(E(\xi,\xi)-\frac12|\xi|^2\operatorname{tr}E\) and \(E(\xi,J\xi)\) are contracted-Bianchi consequences. This identifies a particularly sharp candidate, modulo those consequences:
\[
P_0(E)=J^i{}_aJ^j{}_b\,\partial_a\partial_bE_{ij}
-\frac12\Delta\operatorname{tr}E.
\]

The candidate for the surviving functional is therefore
\[
\boxed{
\ell(E_6)=C\,\bigl[\Delta^2P_0(E_6)\bigr]_0,
}
\tag{2.2}
\]
for one normalization constant \(C\).

This is a six-derivative functional on the degree-6 Ricci residual, hence has precisely weight eight. It is an explicit flat cokernel element, not merely a qualitative invariant ansatz. What remains to be checked is whether the numerically saved universal row is this element, modulo Bianchi rows.

### Why the double trace is natural

After applying \(P_0\), \(E_6\) becomes a homogeneous quartic scalar polynomial. The only \(U(2)\)-invariant quartic scalar polynomial on \(\mathbb C^2\) is a multiple of \(|x|^4\). Its coefficient is equivalently its spherical mean or its double Laplacian at the origin. Indeed, for a homogeneous quartic \(p\) in four real variables,
\[
\fint_{S^3}p=\frac{\Delta^2p(0)}{192}.
\]
Thus (2.2) extracts the radial scalar compatibility.

Universality across four jets supports this interpretation but does not alone prove invariant universality. An exact comparison with (2.2) would settle the multiplier much more efficiently than a large unconstrained coefficient fit. Full \(SO(4)\) invariance is not expected: \(P_0\) uses \(J\); the relevant symmetry is \(U(2)\).

### Relation to the geometric scalar equation

Step 65 supplies the exact Einstein identity
\[
\begin{aligned}
\Delta q={}&8\operatorname{tr}V^2-24|\eta|^2
-\frac{3s}{2}q-\frac94q^2\\
&+16\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle,
\qquad q=|\nabla\Omega|^2,\quad u=\Omega/\sqrt2.
\end{aligned}
\tag{2.3}
\]
At a torsion zero, its constant term gives the first-jet cone. Step 65 identifies the analogous leading scalar polynomial at higher-order zeros.

This makes (2.3) the natural geometric source of the order-6 scalar compatibility. A complete identification still requires deriving its **off-Einstein defect** in terms of \(E,\nabla E,\nabla^2E\), then comparing the flat principal part and quartic trace with (2.2). The dimension count does not substitute for that calculation.

## 3. First-jet invariants and the correct dimensionless ratio

At a torsion zero put
\[
f(z,\bar z)=cz+(S+A)\bar z,\qquad
A=a\varepsilon,\qquad
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The proven cone is
\[
\|A\|^2=\|S\|^2+8|c|^2.
\tag{3.1}
\]

The determinant-line-twisted unitary action suggested by the supplied curvature dictionary is
\[
c\mapsto(\det U)c,\qquad
S\mapsto(\det U)USU^T,\qquad
a\mapsto(\det U)^2a.
\tag{3.2}
\]
Conjugating all determinant-line conventions changes the coordinate presentation, not the real invariant structure. Equation (3.2) should be checked against the implementation by transforming the geometric torsion, rather than rotating source and target independently.

Define
\[
u=|c|^2,\quad v=\|S\|^2,\quad w=|a|^2,
\qquad 2w=v+8u,
\]
and
\[
P=c^2\bar a,\qquad D=|\det S|^2,\qquad
Q=a^2\overline{\det S}.
\tag{3.3}
\]
Their relations include
\[
|P|^2=u^2w,\qquad |Q|^2=w^2D,\qquad
0\le D\le v^2/4.
\tag{3.4}
\]

These are adequate rational orbit coordinates on the nonzero cone, where \(a\ne0\). They need not be asserted to be a complete polynomial generating set at the cone vertex.

Set
\[
N=\mathrm{tn}^2
=4u+2v+2\|A\|^2
=20u+4v,\qquad R=\sqrt N.
\tag{3.5}
\]
The coframe calculation in Step 62 gives
\[
|\nabla^2\Omega|^2=4N.
\tag{3.6}
\]

The generic normalized cone has four real shape parameters: ten jet coordinates, minus one cone equation, four unitary-orbit dimensions, and one normalization. Convenient coordinates are
\[
\gamma=\frac{u}{N}\in[0,1/20],\quad
\rho=\frac{2|\det S|}{v}\in[0,1],\quad
\arg P,\quad\arg Q,
\tag{3.7}
\]
with the expected loss of phase coordinates on boundary strata.

### Necessary scaling correction

The measured scaling is
\[
(c,S,a,\lambda)\mapsto
(\mu^2c,\mu^2S,\mu^2a,\mu^2\lambda).
\]
Therefore \(N\mapsto\mu^4N\), and the correct dimensionless ratio is
\[
\boxed{
\Lambda=\frac{\lambda}{R}
=\frac{\lambda}{\sqrt{\mathrm{tn}^2}}
=\frac{2\lambda}{|\nabla^2\Omega|}.
}
\tag{3.8}
\]
The ratio \(\lambda/\mathrm{tn}^2\) used in the notes and one branch is not scale invariant. Unit-\(N\) numerical tables conceal this distinction.

The determinant is also naturally invariant:
\[
\det_{\mathbb R}Df
=9u^2+D+w^2+2\operatorname{Re}Q.
\tag{3.9}
\]
Its degenerate nonzero stratum is
\[
c=0,\qquad \rho=1,\qquad \arg Q=\pi.
\]
Thus a single “\(c^2\)-fraction” cannot organize the sign map: it omits singular-value imbalance and two relative phases.

## 4. The strongest justified ansatz for \(\Phi _6\)

With a fixed multiplier orientation, the supported weighted form is
\[
\boxed{
\Phi _6
=R^4\left[
\phi_0(X)+\Lambda\phi_1(X)+\Lambda^2\phi_2(X)
\right],
}
\tag{4.1}
\]
where \(X\) denotes the four normalized orbit parameters. Equivalently,
\[
F_0=R^4\phi_0,\qquad
F_1=R^3\phi_1,\qquad
F_2=R^2\phi_2.
\]

The \(\lambda\)-quadratic law is strongly supported numerically, but weighted homogeneity alone does not prove it. Its exact proof requires tracing \(\lambda\) through the constrained elimination.

### Polynomial baseline versus rational critical value

If \(F_i\) are polynomial invariants in the first jet, their degrees are \(4,3,2\). On the cone the minimal forms are
\[
\begin{aligned}
F_2&=\alpha u+\beta v,\\
F_1&=2\operatorname{Re}(\kappa P),\\
F_0&=A_0u^2+B_0uv+C_0v^2+D_0D
+2\operatorname{Re}(E_0Q).
\end{aligned}
\tag{4.2}
\]
This gives a small, falsifiable first interpolation model.

However, the actual reduced object is a critical value:
\[
q_{\rm red}(z)=b+j^Tz+\frac12z^THz,\qquad
\boxed{\Phi _6=b-\frac12j^TH^{-1}j.}
\tag{4.3}
\]
Hence rational invariant dependence is the natural general expectation. On a fixed-rank algebraic chart,
\[
\Phi _6=
\frac{2b\det H-j^T\operatorname{adj}(H)j}{2\det H}.
\tag{4.4}
\]
The numerator and denominator can be reconstructed before any positivity assumption.

The small-\(c\) sample has a substantial spread in \(F_2\), which suggests more shape dependence than (4.2) allows. Because those samples are merely near \(c=0\), not an exact fixed-norm \(c=0\) family, this is evidence for rational dependence, not a proof. An exact \(c=0\) scan would distinguish the possibilities immediately: every quadratic polynomial invariant is constant on that normalized slice.

### The invariant object includes Hessian inertia

If \(H\) is positive definite,
\[
q_{\rm red}(z)=0
\quad\Longleftrightarrow\quad
\Phi _6\le0.
\tag{4.5}
\]
For \(\Phi _6<0\), its active solution set is an 11-dimensional ellipsoid.

But the full \(H_4\) quadratic form has 99 positive and 84 negative directions. Definiteness was observed only after restriction to the 12-dimensional active space. Until its inertia is established throughout the intended domain, the complete compatibility object is
\[
\boxed{(\operatorname{inertia}H,\ \Phi _6)}
\tag{4.6}
\]
together with kernel-linear data at rank loss. An indefinite active quadratic generally takes both signs and does not obey the criterion (4.5).

## 5. Why all three coefficients can change sign

The data demonstrate both signs of each coefficient after fixing the same multiplier orientation:

* \(F_0<0\) at gen2, while many other jets have \(F_0>0\).
* \(F_1\) has both signs among generic jets.
* \(F_2>0\) at gen2 and the small-\(c\) samples, but \(F_2<0\) at many other jets.

There is no sum-of-squares reason for positivity. Equation (4.3) subtracts a nonnegative completion-of-square term from an algebraic term whose sign is unrestricted. Even if \(H\) is fixed positive definite and \(j=j_0+\lambda j_1\),
\[
F_2=b_2-\frac12j_1^TH^{-1}j_1,
\]
while \(F_1\) contains a cross term. Neither must have a prescribed sign. Phase and singular-value data in \(P,Q,D\) supply natural mechanisms for variation of \(F_0,F_1\).

There is a further useful symmetry.

### Even-jet sign reversal

The Taylor equations respect
\[
H_k\mapsto\mu^kH_k,\qquad
\lambda\mapsto\mu^2\lambda,\qquad
E_d\mapsto\mu^{d+2}E_d.
\]
These are algebraic identities and extend to \(\mu=i\). On a fully even real jet,
\[
\boxed{
(H_{2j},\lambda)\mapsto((-1)^jH_{2j},-\lambda)
}
\tag{5.1}
\]
again yields a real truncated solution. The first torsion jet changes sign.

If the reduction is equivariant under this operation,
\[
\Phi _6(-K,-\lambda)=\Phi _6(K,\lambda),
\]
so \(F_0,F_2\) are even and \(F_1\) is odd in \(K\). This supplies a structural reason for \(F_1\)’s sign change whenever it is nonzero.

For the first-jet-only invariant law it also predicts \(F_1=0\) at \(c=0\): there, \(K\) and \(-K\) are related by a central unitary transformation. The small-\(c\) data are consistent with this prediction.

This symmetry concerns local even jets; it does not transform compact negative Einstein geometry into compact positive geometry. Nor does it prove that a general rational \(F_1\) is a constant multiple of \(\operatorname{Im}P\). The proposed coefficient near \(12\) from two samples is an exploratory fit, not a recovered formula.

## 6. What must be included before calling the law universal at arbitrary zeros

There is a substantive possible omission in the first-jet-only parameterization.

At the 2-jet level there are 60 anti-\(J\) coefficients. Removing 35 quartic-Hamiltonian gauge directions and ten Einstein equations leaves 15 geometric parameters, naturally ten torsion-first-jet parameters and five components of \(W^-(p)\). The first-jet cone controls \(W^+(p)\), not \(W^-(p)\).

The supplied reconstruction metadata list only \(c,S,A,\lambda\). They do **not** display \(W^-(p)\), so the claim that the pipeline chose \(W^-=0\) is unverified. An equivariant linear choice would plausibly do so, but the actual curvature must be evaluated.

Likewise, \(H_3=0\) restricts odd curvature/torsion derivatives. The general law may depend on these additional data or become less restrictive after they are varied.

Thus the meaningful distinction is
\[
\Phi _6(K,\lambda)\quad\text{on the computed slice}
\]
versus
\[
\Phi _6(K,W^-(p),\text{odd lower data},\lambda)
\quad\text{for arbitrary zeros}.
\]
Whether the extra data disappear from the radial compatibility or alter its minimum is a precise unresolved mathematical question.

## 7. Experiments that can recover the formula

### A. Identify the multiplier exactly

Construct the coefficient row of
\[
E_6\longmapsto\Delta^2P_0(E_6)(0)
\]
using the saved monomial convention. Compare it with the saved \(\ell\), allowing contracted-Bianchi rows if necessary. Then verify over the rationals
\[
\ell L_6=0.
\]
This tests an explicit formula, not an unrestricted numerical ansatz. Infinitesimal \(U(2)\) generators provide a separate exact invariance check.

### B. Preserve the algebraic reduction

Use fixed algebraic coordinates and exact constrained elimination or a bordered KKT system, rather than jet-dependent orthonormal/SVD bases. This separates genuine \(\lambda\)-dependence from basis normalization.

For rational cone points, compute the critical value over \(\mathbb Q(\lambda)\). Determine whether its denominator is independent of \(\lambda\), and whether the numerator is exactly quadratic. Neither follows just from the printed Hessian eigenvalues.

The cone admits rational parametrization from a rational point, for example \(c=1,S=0,a=2\). Lines through that point generate exact test jets; generic lines avoid singular strata.

### C. Recover coefficients and invariant dependence

First test
\[
F_0=\Phi(0),\quad
F_1=\frac{\Phi(1)-\Phi(-1)}2,\quad
F_2=\frac{\Phi(1)+\Phi(-1)-2\Phi(0)}2.
\]
Use additional exact \(\lambda\)-values to verify the quadratic identity.

Fit (4.2) first. If it fails exactly, reconstruct the numerator and denominator in (4.4) using the invariant coordinates \(u,v,P,\bar P,D,Q,\bar Q\), reducing by the cone relation. Modular elimination, rational reconstruction and invariant block decomposition can make this substantially smaller than a raw Taylor-coefficient calculation.

### D. Separate phase dependence from magnitude dependence

In a Takagi frame take
\[
S=\operatorname{diag}(s_1,s_2),\qquad
c=|c|e^{i\alpha},\qquad a=|a|e^{i\beta},
\]
with \(|a|\) fixed by the cone. At fixed \(u,v,D\), scan \(\alpha,\beta\).

The polynomial baseline predicts:

* \(F_1\): only the phase \(2\alpha-\beta\);
* \(F_0\): only the phase \(2\beta-\arg\det S\);
* \(F_2\): no phase dependence.

Extra modes diagnose rational dependence or hidden geometric data. The same runs should test \(K\mapsto-K\), unitary covariance and the exact \(c=0\) prediction.

### E. Test the geometric scope

Evaluate \(W^-(p)\) from the saved \(H_2\). Then vary its five free components and the permitted \(H_3\) data while keeping the same \(K,\lambda\). Recompute the scalar minimum and Hessian inertia. Separately reduce \(S=0\) and the degenerate stratum: large values near them could reflect rank change, but the existing sample does not establish a pole.

Finally, high-precision or exact arithmetic at the three reconstructed points can turn the current evidence into certified signs, inertia and finite-order solvability. This certification would settle the truncated algebraic issue, not germ existence.

## 8. Compact negative Einstein geometry and the ratio \(\Lambda\)

The supplied identities give a useful exact pointwise interpretation but no universal ratio bound.

At a torsion zero,
\[
|\eta|^2=4u,\qquad
\operatorname{tr}V^2=4v+32u.
\]
Therefore
\[
|W^+|^2-\frac{s^2}{24}
=2|\eta|^2+\operatorname{tr}V^2
=4v+40u=N+20u.
\]
Since \(0\le u\le N/20\),
\[
\boxed{
N\le |W^+|^2-\frac{s^2}{24}\le2N.
}
\tag{8.1}
\]
Hence \(|\Lambda|=|\lambda|/\sqrt N\) compares the Einstein scale with the amplitude of the self-dual Weyl excess at the zero.

The obstruction to controlling this ratio is concrete:

1. The zero identity and cone are independent of \(\lambda\); their derivation cancels all scalar-curvature terms.
2. A positive local index measures orientation, not derivative magnitude.
3. Global charge supplies no lower bound on \(N\) at an isolated zero.
4. Integral curvature control does not directly control curvature values at isolated points.
5. Integrating (2.3) leaves the derivative source
   \[
   16\int\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle,
   \]
   without a sign established in the supplied material.

Thus neither the sources nor the branch reasoning establishes a known universal pointwise or global estimate
\[
0<c\le \frac{\sqrt N}{|\lambda|}\le C
\]
for compact negative Einstein almost-Kähler manifolds. No cited theorem proving such an estimate is supplied. Conditional curvature bounds would control one direction through (8.1); an opposite bound needs quantitative nonvanishing of the first torsion derivative. Compactness and transversality alone do not provide that quantitative bound.

Even a ratio interval would not by itself suffice: the law depends on four shape variables, \(F_2\) changes sign, and the permitted \(\Lambda\)-set need not be a single band. Moreover, the general-zero scope remains unresolved.

The strongest present global interpretation is therefore a potential **local constraint on the invariant geometry of zeros**, not a compact nonexistence theorem. A globally decisive application would require both:

* a compatibility law valid with unrestricted lower geometric data; and
* a geometric estimate or weighted localization identity forcing at least one zero into its forbidden invariant region.

The multiplier identification (2.2), the corrected scaling (3.8), and exact invariant reconstruction offer direct progress toward the first requirement without reviving the false positivity premise.