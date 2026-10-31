# Q1: exact Einstein candidates on blowups — deductions and remaining obstruction

Date: 2026-10-08. Read the Q1 statement and inherited estimates in `01_Research_Synthesis.tex`, and A01 Step 48, the corrected Burns insertion statement, and the almost-Hermitian flux discussion in `02_Mathematical_Source_Companion.tex`.

## 1. A concrete additional consequence of the inherited coercivity

Let (X) be a minimal complex surface of general type, (A=c_1^2(X)>0), and (M=X\#k\overline{\mathbb{CP}}^2), (k\ge1). Put (T=2\chi+3\tau=A-k). Assume the manuscript's actual sign-class supply and its same-solution estimate

\[
\Sigma\le C(P+D_2),\qquad \Sigma=S-32\pi^2p,
\]

in the (a^2=T), hence (Y=0), branch, where

\[
S=\int s^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,
\quad p=(a^+)^2\ge A.
\]

The constant can always be enlarged so (C>8/9). Define

\[
\theta=\frac{8}{9C-8}>0.
\]

**Proposition.** Every Einstein metric (g_E) on (M), if one exists, satisfies

\[
\boxed{\int_M|\operatorname{Ric}_{g_E}|^2
\ge 8\pi^2\bigl(A+(1+\theta)k\bigr).}
\]

The stronger solution-dependent form is

\[
\int|\operatorname{Ric}_{g_E}|^2
\ge 8\pi^2\{p+(1+\theta)(p-T)\}.
\]

**Proof.** An Einstein candidate has negative scalar curvature by the positive actual monopole budget, and (P=0\). Chern–Weil gives

\[
W_+=2\pi^2T-\frac{S}{48}.
\]

The manuscript's definition

\[
D_2=\frac32 S+18W_+-72\pi^2p
\]

therefore gives the exact identity

\[
D_2=\frac98S+36\pi^2T-72\pi^2p
=\frac98\Sigma-36\pi^2(p-T).
\]

Insert this into \(\Sigma\le CD_2\):

\[
\left(\frac{9C}{8}-1\right)\Sigma\ge36\pi^2C(p-T).
\]

Consequently

\[
\Sigma\ge32\pi^2\frac{9C}{9C-8}(p-T)
=32\pi^2(1+\theta)(p-T).
\]

Since (R=S/4) for an Einstein metric, the first assertion follows from (p\ge A\) and (p-T\ge k\). No compactness or minimizer assumption enters. □

LeBrun's exact classical result is

\[
\inf_g\int_M|\operatorname{Ric}_g|^2=8\pi^2(A+k).
\]

Thus the new coercivity, if accepted as an established project theorem, yields an explicit separation of every Einstein candidate from the Ricci-energy infimum:

\[
\boxed{R(g_E)-\inf_gR(g)\ge8\pi^2\theta k.}
\]

This is a legitimate new corollary of the inherited core, not a solution of Q1 or a new independent analytic mechanism. It is especially useful for excluding a tempting false argument: an Einstein metric globally minimizes (P\), but need not globally minimize (R=P+S/4\). A lower-(R\) competitor does not contradict its existence.

## 2. Why the Burns insertion theorem cannot itself exclude an Einstein candidate

The insertion theorem changes (M\) to (M\#\overline{\mathbb{CP}}^2\). Even at an Einstein background it gives

\[
P(g_\varepsilon)=8\pi^2
-8\pi^2\varepsilon\mathcal R^+_p(\zeta,\zeta)
+O(\varepsilon^2\log(1/\varepsilon)).
\]

The leading positive topological term remains. At a favorable kernel point the strict inequality is (P(g_\varepsilon)<8\pi^2\), not (P(g_\varepsilon)<0\). There is neither a competitor on the original smooth manifold nor a contradiction to (P(g_E)=0\).

The relocation argument in the source becomes effective only if a minimizing configuration already has a detachable bubble with a proven energy identity and legitimate reattachment. A hypothetical smooth Einstein metric has no such bubble supplied by its topology alone. The existence of an exceptional sphere does not supply a Burns asymptotic region of that metric.

## 3. A numerical compatibility test for the proposed short proof

The inherited estimates are compatible with formally Einstein curvature budgets for sufficiently small (h=k/A\). This can be shown rather than merely asserted.

Fix (C>8/9\) and choose

\[
L>\frac{9C}{9C-8}>1.
\]

Set formal data

\[
P=0,\quad p=A,\quad a^2=T=A(1-h),
\quad S=32\pi^2A(1+Lh),
\]

\[
W_+=\frac{4\pi^2A}{3}
\left[1-\frac{L+3}{2}h\right].
\]

These satisfy the positive-orientation Chern–Weil identity and (W_+>0\) for small (h\). Also

\[
\Sigma=32\pi^2ALh,
\qquad D_2=36\pi^2A(L-1)h,
\]

so \(\Sigma<CD_2\) by the choice of (L\). The N1 constraint at (P=0\) is

\[
\frac13-h\ge\varepsilon_0,
\]

and is satisfied whenever (h<1/3-\varepsilon_0\).

Every classical finite-parameter inequality (D_\beta\ge0\) is also satisfied for sufficiently small positive (h\). Indeed, with

\[
f_h(\beta)=\frac{D_\beta}{8\pi^2A},
\]

direct substitution gives

\[
f_h(\beta)=\frac{(\beta-2)^2}{\beta}
+h(\beta+1)\left(\frac{4L}{\beta}-\frac{L+3}{2}\right).
\]

At (h=0\) the only zero for \(\beta>0\) is the strict quadratic minimum \(\beta=2\). At that point the (h\)-coefficient is \(9(L-1)/2>0\). Uniform positivity near \(2\) follows from completing the square, with a positive (O(h)\) term dominating the (O(h^2)\) displacement of the minimum. On compact subsets away from \(2\), positivity persists by continuity. At \(\beta\to0\) and \(\beta\to\infty\), the respective coefficients are \(4(1+Lh)>0\) and \(1-(L+3)h/2>0\). Therefore (f_h>0\) for all \(\beta>0\) once (h>0\) is sufficiently small.

The other-orientation Weyl budget can also be nonnegative. For example, take formal minimal-model data \(\chi(X)=A/2\), as for products of hyperbolic curves. Then

\[
W_- =\frac{4\pi^2A}{3}
+\pi^2Ah\left(10-\frac{2L}{3}\right)>0
\]

for small (h\). Both Chern–Weil identities are then satisfied.

These data are not asserted to come from an actual metric or an actual SW solution. Their exact significance is that the displayed integrated estimates, including I40 and N1, do not algebraically exclude all small blowups. A proof of Q1 must use an additional differential or global realization constraint. In particular, changing the parameter \(\beta\) within these inequalities cannot alone settle Q1.

## 4. A genuine Einstein-specific route, and its exact missing input

LeBrun's 2005 symplectic minimality theorem states that a closed almost-Kähler Einstein four-manifold with negative star-scalar curvature is smoothly indecomposable as (N\#\overline{\mathbb{CP}}^2\). Thus Q1 would follow for a candidate (g_E\) if one could produce a global two-form \(\omega\) such that

\[
d\omega=0,\quad *_g\omega=\omega,\quad |\omega|_g^2=2,
\quad s^*=s+|\nabla\omega|^2<0.
\]

This uses a geometric fact specific to the candidate Einstein metric. The underlying manifold's symplectic form does not supply it: compatibility with another metric is insufficient. Normalizing a nowhere-zero self-dual harmonic form changes its closure unless its norm is constant; making the corresponding metric almost-Kähler by a nonconstant conformal factor generally destroys Einstein.

The actual SW quadratic form is not automatically closed or constant-length either. Establishing the displayed conditions from the full actual field equations would therefore be a new theorem, not a missing sentence in the current manuscript. The source's frame-twist formula explains one obstruction: on an Einstein candidate the ASD canonical flux must be carried by the twist; the present bounds are lower bounds on that twist, not an upper bound that forces its vanishing.

## 5. Research status and sources

This work does not settle unrestricted Q1. It proves an explicit Einstein-candidate Ricci-energy separation conditional only on the inherited project coercivity, establishes a formal compatibility family blocking a short algebraic closure, and identifies why the new construction does not provide exact Einstein nonexistence.

Primary sources checked:

1. C. LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, arXiv:math/0003068, Theorem 4.3: exact \(\inf R=8\pi^2(A+k+4\ell)\). https://arxiv.org/pdf/math/0003068
2. C. LeBrun, *Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves*, arXiv:math/0409290, Theorem A and Theorem B; Theorem A explicitly excludes the smooth blowup decomposition under negative star-scalar curvature. https://arxiv.org/pdf/math/0409290
3. C. LeBrun, *An Overview of Einstein 4-Manifolds*, arXiv:2609.03033v1, the classical sign-class argument and strict one-third obstruction. https://arxiv.org/html/2609.03033v1

The 2005 paper's discussion of an asserted Oguri–Sekigawa upper bound is explicitly tentative in that source and is not used here.
