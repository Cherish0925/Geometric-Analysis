# Step 23: Cooperative persistence theorem for componentwise energy

> **Step 24 correction.** The dissipation-locality part of this note remains useful, but the maximal `r`-net repair is not valid as an input for the selected maximal-function good supports in the actual LeBrun sequence. A maximal net over all of `M` contains bad centers where the critical product `A_alpha^2||F||_2` is not initially small. Thus the graph/cooperative theorem is conditional on an all-center smallness family; it does not by itself replace Li's all-center hypothesis. Step 24 uses a buffered selected support with `supp chi` strictly inside `{eta=1}` so that the energy estimate uses only the good support where the initial maximal-function bound holds.
the passage from the absorption argument (Section 4 there) to the componentwise
differential inequality (4.3) was not justified because neighbor dissipations
appeared after Sobolev absorption.  The resolution is that a careful re-examination
of the exact tensor inequality shows the Sobolev absorption is **within each
component**, so no neighbor dissipation coupling exists.  The resulting cooperative
system gives all the required componentwise bounds from standard theory.

## 1. Setup and component geometry

We study the normalized cutoff flow

\[
\partial_t g = -2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

**Corrected covering geometry (repairs TTCS-identified gap).** Use a
**maximal \(r\)-net** \(\{p_\alpha\}\) on \((M,g_0)\):

\[
d(p_\alpha,p_\beta)\ge r\ (\alpha\ne\beta),
\qquad \bigcup_\alpha B_r(p_\alpha)=M.
\]

Maximality forces the second condition.  Define smooth cutoffs

\[
\eta_\alpha\in C^\infty_c(B_{3r}(p_\alpha)),\quad
\eta_\alpha|_{B_{2r}(p_\alpha)}=1,\quad
|\nabla\eta_\alpha|\le C r^{-1},
\]

and supports \(U_\alpha=B_{3r}(p_\alpha)\).  The \(r\)-separation gives a bounded
overlap number \(N\) for the family \(\{U_\alpha\}\).

**Covering subordination.** At any \(x\in M\), the covering property gives
\(p_\beta\) with \(d(x,p_\beta)\le r<2r\), so \(\eta_\beta(x)=1\).  Hence

\[
\sum_\beta\eta_\beta(x)^2\ge 1 \quad\text{for all }x\in M.
\tag{1.0}
\]

Consequently, for any \(\alpha\),

\[
\int_{U_\alpha}F^2
\le \int_{U_\alpha}\!\sum_\beta\eta_\beta^2F^2
=\sum_{\beta\sim\alpha}H_{2,\beta},
\tag{1.0'}
\]

where \(\beta\sim\alpha\) means \(U_\beta\cap U_\alpha\ne\emptyset\), i.e.,
\(d(p_\alpha,p_\beta)\le 6r\).  This condition was not satisfied by the
previous construction (centers at \(10r\), supports \(B_{5r}\)).

The relative Sobolev coefficient on each \(U_\alpha\) satisfies

\[
A_\alpha^2\lesssim r^2\operatorname{Vol}(U_\alpha)^{-1/2},
\qquad
\frac{A_\alpha}{A_\beta}\le C_A \quad(\beta\sim\alpha).
\tag{1.1}
\]

Define the component energy and dissipation:

\[
H_{2,\alpha}=\int\eta_\alpha^2 F^2\,d\mu,\qquad
D_{2,\alpha}=\int\eta_\alpha^2 a|\nabla\operatorname{Rm}|^2\,d\mu,
\tag{1.2}
\]

and the weighted versions

\[
S_\alpha=A_\alpha^4 H_{2,\alpha},\qquad
Z_\alpha=A_\alpha^4 D_{2,\alpha},\qquad
\Gamma(t)=\sup_\alpha S_\alpha(t)^{1/2}.
\tag{1.3}
\]

## 2. Why dissipation stays local: the exact absorption

Testing the curvature evolution against \(\eta_\alpha^2 F^0 H = \eta_\alpha^2 H\)
(i.e., \(q=2\) in the power-energy framework), the standard computation from
Step 20 equation (5.1) gives

\[
\frac{d}{dt}H_{2,\alpha}+c_2D_{2,\alpha}
\le \underbrace{\int\eta_\alpha^2 aF^3}_{R_{2,\alpha}}
+C r^{-2}\underbrace{\int_{U_\alpha}F^2}_{\text{localization}}.
\tag{2.1}
\]

The localization terms involve \(|\nabla\eta_\alpha|^2\) and
\(|\nabla a|^2/a\), both supported in \(U_\alpha\) and bounded by
\(Cr^{-2}\int_{U_\alpha}F^2\) (using Whitney estimates).

**The crucial observation**: the reaction \(R_{2,\alpha}\) is absorbed using the
test function \(v=\eta_\alpha a^{1/2}F\), which is compactly supported in
\(B_{3r}(p_\alpha)= U_\alpha\).  By Hölder,

\[
R_{2,\alpha}
=\int(\eta_\alpha a^{1/2}F)^2\cdot F\,d\mu
\le\|F\|_{L^2(U_\alpha)}\|\eta_\alpha a^{1/2}F\|_{L^4(U_\alpha)}^2.
\tag{2.2}
\]

The Sobolev embedding on \(U_\alpha\) gives

\[
\|\eta_\alpha a^{1/2}F\|_{L^4(U_\alpha)}^2
\le A_\alpha^2\!\left(\int_{U_\alpha}|\nabla(\eta_\alpha a^{1/2}F)|^2
+r^{-2}\int\eta_\alpha^2 aF^2\right).
\tag{2.3}
\]

Expanding the gradient:

\[
\int_{U_\alpha}|\nabla(\eta_\alpha a^{1/2}F)|^2
\le 3\int\eta_\alpha^2 a|\nabla F|^2
+3\int\eta_\alpha^2\frac{|\nabla a|^2}{4a}F^2
+3\int a|\nabla\eta_\alpha|^2F^2.
\]

The first term is bounded by \(CD_{2,\alpha}\) (the \(\alpha\)-component
dissipation, since \(|\nabla F|\le|\nabla\operatorname{Rm}|\)).  The second
and third are \(Cr^{-2}\int_{U_\alpha}F^2\), using Whitney bounds.
Both are supported in \(U_\alpha\); **no neighbor dissipation appears**.

Therefore

\[
\|\eta_\alpha a^{1/2}F\|_{L^4}^2
\le A_\alpha^2\!\left(CD_{2,\alpha}+Cr^{-2}\int_{U_\alpha}F^2\right).
\tag{2.4}
\]

Define the critical product

\[
\gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)}.
\tag{2.5}
\]

Since supports overlap with bounded multiplicity,
\(\int_{U_\alpha}F^2\le\sum_{\beta:U_\beta\cap U_\alpha\ne\emptyset}H_{2,\beta}\),
so \(\gamma_\alpha\le C\sqrt{N}C_A^2\Gamma(t)\le C_{NCA}\Gamma_*\) under the
first-exit condition.  Substituting (2.4) and (2.5) into (2.2):

\[
R_{2,\alpha}\le \gamma_\alpha\cdot D_{2,\alpha}
+C\gamma_\alpha r^{-2}\int_{U_\alpha}F^2.
\tag{2.6}
\]

The key point: the dissipation \(D_{2,\alpha}\) in (2.6) is the
**\(\alpha\)-component dissipation**, not a neighbor's.  Absorbing into (2.1):

\[
\frac{d}{dt}H_{2,\alpha}+(c_2-\gamma_\alpha)D_{2,\alpha}
\le C(\gamma_\alpha+1) r^{-2}\int_{U_\alpha}F^2.
\tag{2.7}
\]

When \(\gamma_\alpha<c_2/2\) (ensured by \(\Gamma_*\) small), the full dissipation
constant \(c_2/2\) is retained.  The right side involves only \(H\)-type neighbor
terms through \(\int_{U_\alpha}F^2\le\sum_{\beta\sim\alpha}H_{2,\beta}\).

## 3. The cooperative vector inequality

Multiplying (2.7) by \(A_\alpha^4\):

\[
\boxed{
S_\alpha'+\frac{c_2}{2}Z_\alpha
\le\frac{b}{r^2}\sum_{\beta\sim\alpha}\tilde B_{\alpha\beta}S_\beta,
\qquad
\tilde B_{\alpha\beta}=\left(\frac{A_\alpha}{A_\beta}\right)^4.}
\tag{3.1}
\]

The row sums of \(\tilde B\) are bounded:

\[
L=\sum_{\beta\sim\alpha}\tilde B_{\alpha\beta}
\le N\cdot C_A^4.
\tag{3.2}
\]

**There is no \(\varepsilon \tilde BZ\) term.**  This is the main structural
advance: the dissipation is absorbed within each component, so the resulting
system is a standard cooperative (nonneg-matrix) ODE coupled only through
\(H\)-energy, not through gradients.

## 4. Componentwise persistence

For a nonneg vector \(S(t)\ge0\) satisfying
\(S'\le MS\) with \(M\) nonneg and row sums \(\le R\), the comparison principle
gives

\[
S_\alpha(t)\le [e^{tM}S(0)]_\alpha,
\qquad
\text{row sums of }e^{tM}\le e^{tR}.
\]

Therefore

\[
S_\alpha(t)\le e^{tR}\max_\beta S_\beta(0)=e^{tR}\Gamma(0)^2.
\tag{4.1}
\]

With \(R=bL/r^2\) and \(t=T=\theta r^2\):

\[
\boxed{
\Gamma(T)\le e^{bL\theta/2}\Gamma(0).}
\tag{4.2}
\]

For \(\theta\le 1/(2bL)\), the amplification is at most \(e^{1/4}\approx1.28\).
The first-exit condition \(\Gamma(t)\le\Gamma_*\) is preserved whenever
\(\Gamma_*\ge e^{bL\theta/2}\Gamma(0)\).

## 5. Componentwise integrated dissipation

From (3.1), integrating and using (4.1):

\[
\frac{c_2}{2}\int_0^TZ_\alpha\,dt
\le S_\alpha(0)+\frac{bL}{r^2}\int_0^Te^{bLs/r^2}\,ds\cdot\Gamma(0)^2
\le (1+e^{bL\theta})\Gamma(0)^2.
\]

Hence

\[
\boxed{
\int_0^TZ_\alpha\,dt\le C(b,L,\theta)\Gamma(0)^2.}
\tag{5.1}
\]

This gives componentwise integrated curvature dissipation, independent of the
number of components.

## 6. Spacetime and pointwise cubic potential

From the same critical product (2.6), at each time \(s\):

\[
H_{3,\alpha}(s)=\int\eta_\alpha^2 aF^3
\le\gamma_\alpha(D_{2,\alpha}(s)+Cr^{-2}H_{2,\alpha}(s)).
\]

Since \(\gamma_\alpha\le C\Gamma_*\), integrating and using (4.1)--(5.1):

\[
\int_0^TH_{3,\alpha}\,ds
\le C\Gamma_*\left(\frac{Z_\alpha}{A_\alpha^4}
+\frac{\theta}{A_\alpha^4}\sup_s S_\alpha\right)
\le \frac{C\Gamma_*\Gamma(0)^2}{A_\alpha^4}.
\tag{6.1}
\]

Hence \(A_\alpha^4\int_0^TH_{3,\alpha}\,ds\le C\Gamma_*^3\).

By time averaging, there exists \(t_*\in[T/2,T]\) with

\[
H_{3,\alpha}(t_*)\le\frac{2}{T}\int_0^TH_{3,\alpha}
\le\frac{C\Gamma_*^3}{A_\alpha^4 T}.
\]

The \(q=3\) energy inequality has the same cooperative structure
\(\tilde H_3'\le\frac{C}{r^2}\tilde B\tilde H_3\).  Propagating from \(t_*\)
gives, for \(t\in[T/2,T]\):

\[
\boxed{
A_\alpha^4H_{3,\alpha}(t)\le\frac{C\Gamma_*^3}{t}.}
\tag{6.2}
\]

This is the cubic potential needed for the subsequent finite-exponent route.

## 7. Unweighted defect: triangular estimate

The defect equation, from Step 20 eq. (7.2), is

\[
\frac{d}{dt}Q_\alpha+\frac{c_E}{2}\int\eta_\alpha^2a|\nabla E|^2
\le C r^{-2}\sum_{\beta\sim\alpha}\tilde B_{\alpha\beta}Q_\beta,
\tag{7.1}
\]

where \(Q_\alpha=\int\eta_\alpha^2|E|^2\).  The curvature potential
\(a|\operatorname{Rm}||E|^2\) is absorbed by the same Sobolev mechanism
applied to \(w=\eta_\alpha a^{1/2}E\):

\[
\int a|\operatorname{Rm}|\,|\eta E|^2
\le\gamma_\alpha\!\left(\int a|\nabla(\eta E)|^2+r^{-2}\int\eta^2|E|^2\right).
\]

The gradient integral involves \(a|\nabla E|^2\) (the \(\alpha\)-component
\(E\)-dissipation) and localization terms.  **Again no neighbor dissipation.**
After absorption (\(\gamma_\alpha<c_E/2\)):

\[
Q_\alpha(T)\le e^{bL\theta}\max_\beta Q_\beta(0).
\tag{7.2}
\]

Summing with bounded overlap:

\[
\frac{Q_{\text{total}}(T)}{A}
\le NC_A^4 e^{bL\theta}\frac{Q_{\text{total}}(0)}{A}.
\tag{7.3}
\]

Since \(Q_{\text{total}}(0)/A\to0\) and the constant is fixed,
\(Q_{\text{total}}(T)/A\to0\).  This is the triangular \(Q\) preservation.

## 8. Fixed \(J_6\) persistence

The defect-moment

\[
J_{6,\alpha}=\int\eta_\alpha^2 a^4|E|^6
\]

satisfies the same cooperative structure because the curvature potential
\(a|\operatorname{Rm}||E|^6\) is absorbed by the critical product
\(\gamma_\alpha\) and the corresponding \(|E|^6\)-dissipation.  No \(1/t\)
coefficient from time zero is needed because \(J_6\) uses the current critical
absorption directly:

\[
\int aF\cdot z_6^2
\le\gamma_\alpha(X_{6,\alpha}+r^{-2}J_{6,\alpha}),
\qquad z_6=\eta a^{5/2}|E|^3.
\tag{8.1}
\]

Consequence:

\[
J_{6,\alpha}(T)\le e^{bL\theta}J_{6,\alpha}(0).
\tag{8.2}
\]

## 9. Connection to finite-exponent smoothing

The cooperative persistence theorem provides the exact inputs for the
Steps 20--21 finite-exponent route:

1. **\(q=2\) energy**: \(S_\alpha(t)\le C\Gamma(0)^2\) and
   \(\int_0^TZ_\alpha\le C\Gamma(0)^2\).
2. **Parabolic Sobolev**: four-dimensional embedding gives spacetime \(L^3\).
3. **Cubic potential**: \(A^4H_3(t)\le C\Gamma^3/t\) on \([T/2,T]\).
4. **\(q=3\) estimate with time cutoff**: the spacetime \(L^3\) pays for the
   time-cutoff source, yielding time-uniform spatial \(L^3\) on \([3T/4,T]\).
5. **Weighted Moser \(q\to3q/2\)**: A03's convergent product hierarchy
   yields \(|a\operatorname{Rm}|\le C\Gamma/t\) on each component.
6. **Defect**: \(Q(T)/A\to0\) and \(J_6(T)\le CJ_6(0)\).

The weaker terminal bound \(|a\operatorname{Rm}(T)|\le Cr^{-2}\) already
suffices for bounded curvature on plateau buffers, since \(r\) is fixed before
the sequence limit.

## 10. Why the resolvent is not needed (but remains valid)

The Strategist suggested a resolvent \(P=(I-\rho\tilde B)^{-1}\) to handle
a possible \(\varepsilon\tilde BZ\) neighbor dissipation term.  The exact
tensor calculation shows \(\varepsilon=0\): the Sobolev variable
\(v=\eta_\alpha a^{1/2}F\) has compact support within \(U_\alpha\), so its
gradient integral decomposes into the \(\alpha\)-component dissipation and
\(r^{-2}H\) localization terms within \(U_\alpha\).  No neighbor gradient
contributes.  TTCS independently confirmed this in all five gradient
components and all geometric variation terms.

The resolvent remains a valid tool for the hypothetical
\(\varepsilon>0\) case.  When \(\varepsilon=0\), it reduces to the
cooperative comparison.

## 10b. Covering subordination repair

TTCS also identified that the old ball family (centers at \(10r\),
supports \(B_{5r}\)) failed the covering subordination \((1.0')\):
the annulus \(B_{5r}\setminus B_{4r}\) was not covered by any
\(\eta_\beta^2\ge1\) region.  The corrected maximal \(r\)-net geometry
in Section 1 resolves this: at every point, some \(\eta_\beta=1\), so
\(\sum\eta_\beta^2\ge1\) everywhere and \((1.0')\) holds.

## 11. What is proved vs. what remains

This theorem is **conditional** on the provisional first-exit interval:
bilipschitz metric comparability, bounded Sobolev comparability ratios, and
sufficiently small \(\Gamma_*\).  These must be verified simultaneously as
part of the first-exit loop.  However, the theorem resolves the structural
obstacle from Step 22: componentwise energy persistence no longer requires
assuming componentwise absorption or summing over all components.

The exact tensor inequality (2.1) itself remains a schematic claim.  The
precise verification requires: measure evolution \(\partial_t d\mu=-a\operatorname{tr}(E)d\mu\),
inverse metric variation in \(F\), algebraic curvature terms, Hessian-\(a\)
integrations by parts, and the \(E=\operatorname{Ric}+g\) closure.  Step 20
provides the schematic derivation; the current note shows that whatever the
precise coefficients, the structural feature (no neighbor \(Z\)) is forced by
the support geometry of the testing function.

Even if fully established, the result addresses only the critical
four-dimensional negative LeBrun/Ishida-LeBrun laboratory.  The positive
branch, arbitrary four-manifolds, dimensions \(n\ge5\), the original
all-dimensional proposition, and Lean formalization remain open.

## 12. Nash semigroup: refuted for the critical step

A03's message #304 gives a decisive counterexample to the Nash shortcut.
The Hardy potential \(V=\kappa/|x|^2\) in \(\mathbb R^4\) with \(\kappa<1\)
satisfies the form bound \(\int V\phi^2\le\kappa\int|\nabla\phi|^2\), yet
the associated heat kernel has the singularity
\(p_t(x,y)\sim r^{-\sigma}\) with \(\sigma=1-\sqrt{1-\kappa}>0\), and
\(L^2\to L^\infty\) ultracontractivity **fails**.  This matches the
Milman--Semenov on-diagonal bound
\(t^{-2}(1\wedge\sqrt t/|x|)^{2\sigma}\).

Since the cutoff weight \(a=\chi^2\) creates an analogous critical inverse-square
potential near the transition \(\{\chi=0\}\), the abstract Nash \(L^2\to L^\infty\)
lemma cannot bypass the critical \(H_2\to H_3\) upgrade.

The correct **two-stage architecture** is:

- **Stage 1 (critical):** use the \(q=2\) cooperative persistence from this
  theorem, then four-dimensional parabolic Sobolev to obtain spacetime \(L^3\),
  then the \(q=3\) inequality with time cutoff to produce time-uniform spatial
  \(H_3\) on a positive-time slab.  This is the irreducible critical step.

- **Stage 2 (subcritical):** once \(H_3\) is available, curvature is a spatially
  subcritical potential (\(p=3>n/2=2\) in 4D), and the \(q\to3q/2\) Moser
  iteration proceeds with convergent constants.

Nash may help Stage 2 but cannot replace Stage 1.  The cooperative persistence
theorem provides the input for Stage 1: componentwise \(H_2\) and \(D_2\) bounds.

## Files

- Verification script: `workspace/scripts/step23_cooperative_persistence.py`
- This note: `workspace/notes/step23_cooperative_persistence_theorem.md`
- Parent: `workspace/notes/step22_current_energy_formulation.md`
- Tensor inequality source: `workspace/notes/step20_closed_tensor_estimate.md`
- Weak moment estimate: `workspace/notes/step22_weak_nested_moment_estimate.md`
