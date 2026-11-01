# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 60,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step60_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step60_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Part A of the Step-59 note (Theorem 59.R, the rigorous second-order Burns expansion, and Corollary 59.KE, p_*(X#k CPbar^2) < 8 pi^2 k for every minimal surface of general type), as corrected by Part C. Check specifically and give corrected statements where needed: (1) smoothness in (sigma, r, y) of the rescaled far-annulus metric G_{sigma,r} and of the density difference, the claimed factorization r^4 * gamma~(sigma,r) with gamma~(0,r)=0, and the Taylor/log bookkeeping that yields 4 pi^2 Phi eps^2 log(1/eps) + O(eps^2) including the cutoff psi_eps for K and the inner region O(eps^2 R^4); whether 'F+ quadratic in the perturbation of a C-null model' really excludes 3-jets/4-jets from the log term. (2) The distributional evaluation of the order-eps term E_1 = 2 kappa R+(zeta,zeta): validity of reducing to lim_{eta->0} int ell_g(chi_eta B) using only E_P=0 near p (P-critical, not Einstein), the replacement chi A -> ddbar(chi log r^2), the linearized Kahler identity W+' = (s'/12) diag(2,-1,-1), the Green flux, and the sign/normalization 2 kappa = -8 pi^2 (compare A01's independent flux theta_2 = 8 pi^2 mu_zeta in Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md). (3) The Schur argument that W- cross terms with the SU(2)_- invariant block vanish after S^3 integration, and the W- self-term killed by k0^W (Part C.1 reports an exact pointwise check and a representation artifact in the exact script; judge the artifact explanation using step60_jax_check.py and step60_jax_check_Wplus.py). (4) The order of limits for canonical models with ADE points (Kronheimer gluing at scale lambda, then lambda -> 0 at fixed eps), whether the error constants in 59.R are uniform in lambda given g_lambda = g_KE near the p_i, and whether the conclusion 'strict inequality for every minimal surface of general type' is correctly obtained (note p_* is an infimum so a sequence suffices). (5) Whether the eigenvector hypothesis on zeta and the kernel/interior sign scope (Part C.2) are stated correctly everywhere in Parts A-C. Return a direct scientific memo: what is proved, what must be repaired, and exact corrected wording.

## Integrated Scientific Memo

# Verification memo: Step 59, Part A, with Part C corrections

## Conclusion

The **second-order expansion and the strict inequality**
\[
p_*(X\#k\overline{\mathbb{CP}}^{\,2})<8\pi^2k
\]
survive verification. The argument needs precise repairs, principally:

- choose the insertion support entirely inside the \(P\)-critical neighborhood;
- correct a factor of two in the distributional chiral flux;
- distinguish the geometric coefficient from the older script’s frozen-projector expression;
- restrict the explicit minimized formula—not the expansion theorem—to eigenvector directions;
- state the kernel sign assertion for the **optimized coefficient with the remaining curvature sectors canceled**, not for arbitrary correctors or arbitrary \(P\)-critical jets;
- correct the mixed coefficient in the displayed \(K^*\);
- explicitly choose \(\varepsilon\) before the ADE gluing parameter \(\lambda\).

The numerical scripts supplied here support the reported comparisons but import computational modules not included in this input. Their numerical agreement is not, by itself, an exact pointwise identity. The \(W^-\) cancellation is an inherited exact identity explicitly stated in both supplied notes; the geometric explanation below shows why its symmetric residual, rather than the older signed expression, is the relevant object.

---

## 1. Rescaling, factorization, and the logarithmic remainder

Write the normal-coordinate components as
\[
g(x)=\delta+h(x),\qquad
h(ry)=r^2q(r,y),\qquad q(0,y)=h_2(y).
\]
Here \(q\) is smooth in \((r,y)\) on a fixed shell
\[
U=\{1/2\le |y|\le2\}.
\]
This follows from Taylor’s formula with integral remainder and \(h(0)=Dh(0)=0\). It does **not** require \(h(x)/|x|^2\) to extend smoothly as a Cartesian function at \(x=0\).

The correct rescaled components are
\[
G_{\sigma,r}(y)=\delta+\sigma A(y)+h(ry)+\sigma r^2K(y)
=B_\sigma+r^2\bigl(q(r,y)+\sigma K(y)\bigr),
\quad B_\sigma=\delta+\sigma A.
\]
There is no additional \(r^{-2}\) multiplying the component matrix \(h(ry)\): the pullback’s two factors of \(r\) cancel the overall metric rescaling.

This family is smooth in the independent variables
\[
(\sigma,r,y)\in[0,(4R^2)^{-1}]\times[0,\rho]\times U
\]
and positive definite after reducing \(\rho\), with all other data fixed.

### Cutoff qualification

Near the ends of the far annulus, this auxiliary family need not equal the rescaled cutoff metric on **all** of \(U\). What is needed, and holds, is equality of their metric two-jets along \(|y|=1\) for
\[
2R\sqrt\varepsilon\le r\le\rho,\qquad \sigma=\varepsilon/r^2.
\]
The cutoffs must satisfy
\[
\psi_\varepsilon=1\quad(r\ge2R\sqrt\varepsilon),\qquad
\chi_\rho=1\quad(r\le\rho),
\]
with smooth flat matching at the plateau endpoints. Curvature densities on these spheres can therefore be evaluated using \(G_{\sigma,r}\).

### Density factorization

Since
\[
\mathcal C(B_\sigma)=0
\]
for every \(\sigma\), smooth dependence on metric two-jets gives
\[
\mathcal C(G_{\sigma,r})=r^2Q(\sigma,r,y)
\]
with \(Q\) smooth. Thus, in a fixed coordinate density,
\[
F_+(G_{\sigma,r})\,d\mu_{G_{\sigma,r}}=r^4H(\sigma,r,y).
\]
Subtracting the rescaled background \(G_{0,r}\) yields
\[
F_+(G_{\sigma,r})d\mu_{G_{\sigma,r}}
-F_+(G_{0,r})d\mu_{G_{0,r}}
=r^4\widetilde H(\sigma,r,y),
\qquad \widetilde H(0,r,y)=0.
\]
Consequently, after sphere integration,
\[
f(r)=r^{-1}\gamma(\varepsilon/r^2,r),\qquad
\gamma(\sigma,r)=r^4\widetilde\gamma(\sigma,r),\qquad
\widetilde\gamma(0,r)=0.
\]
The asserted factorization is valid.

Taylor expansion gives
\[
\widetilde\gamma
=\sigma\gamma_1(r)+\sigma^2\gamma_2(r)
+\sigma^3\gamma_3(\sigma,r).
\]
Putting \(a_\varepsilon=2R\sqrt\varepsilon\),
\[
I_f
=\varepsilon\int_{a_\varepsilon}^{\rho}r\gamma_1(r)\,dr
+\varepsilon^2\int_{a_\varepsilon}^{\rho}\frac{\gamma_2(r)}r\,dr
+\varepsilon^3\int_{a_\varepsilon}^{\rho}
\frac{\gamma_3(\varepsilon/r^2,r)}{r^3}\,dr.
\]
The last term is \(O(\varepsilon^2/R^2)\). Since
\(\gamma_2(r)=\gamma_2(0)+O(r)\), the middle term is
\[
\frac12\gamma_2(0)\varepsilon^2\log(1/\varepsilon)
+O_R(\varepsilon^2).
\]
Moreover,
\[
\gamma_2(0)=
\int_{S^3}[\sigma^2]\left(
|D\mathcal C_{B_\sigma}[h_2+\sigma K]|^2_{B_\sigma}
d\mu_{B_\sigma}\right)
=8\pi^2\Phi.
\]
Hence the logarithmic term is exactly
\[
4\pi^2\Phi\,\varepsilon^2\log(1/\varepsilon).
\]

### Why higher jets cannot enter this logarithm

The substantive argument is the combination of the \(C\)-null model and the square:
\[
G_{\sigma,r}
=B_\sigma+r^2(h_2+\sigma K)+r^3h_3+r^4h_4+\cdots,
\]
\[
\mathcal C(G_{\sigma,r})
=r^2C_2(\sigma)+r^3C_3(\sigma)+r^4C_4(\sigma)+\cdots.
\]
The \(r^4\) density coefficient is solely \(|C_2|^2\). The third jet first contributes at \(r^5\); the fourth jet and nonlinear curvature terms first contribute at \(r^6\). They change \(\gamma_2(r)-\gamma_2(0)\), whose integral against \(dr/r\) is finite.

Thus “quadratic in the perturbation” is sufficient **only when understood as**
\[
\mathcal C(B_\sigma)=0,\qquad F_+=|\mathcal C|^2,
\qquad G_{\sigma,r}-B_\sigma=O(r^2).
\]
No parity assumption on a general \(K\) is needed.

### Inner region and \(\psi_\varepsilon\)

Under \(x=\sqrt\varepsilon\,u\),
\[
\varepsilon^{-1}\Phi_{\sqrt\varepsilon}^*\widetilde g_\varepsilon
=B_1+\varepsilon\bigl(q_\varepsilon(u)+\psi(|u|/R)K(u)\bigr).
\]
The background perturbation pulls back smoothly to the blow-up, and the cutoff removes \(K\) near the exceptional divisor. On the compact blown-up region \(|u|\le2R\), the perturbation is \(O_R(\varepsilon)\) in the required derivative norms. Therefore
\[
\int_{r\le2R\sqrt\varepsilon}F_+(\widetilde g_\varepsilon)d\mu
=O_R(\varepsilon^2).
\]
The corresponding background integral is \(O(\varepsilon^2R^4)\). The cutoff transition contributes only \(O_R(\varepsilon^2)\), not a logarithm.

**Correct wording:** use \(O_R(\varepsilon^2)\) for the inner estimate. Writing \(O(\varepsilon^2R^4)\) with an \(R\)-dependent implicit constant is harmless but does not establish uniform \(R^4\)-growth as \(R\to\infty\). No such uniformity or limit is required.

---

## 2. The order-\(\varepsilon\) coefficient: local criticality suffices

Choose \(\rho\) so that
\[
E_P(g)=0\quad\text{throughout }B_{2\rho}(p),
\]
and set \(B=\chi_\rho(A+K)\). The far and outer linear terms combine into
\[
\varepsilon E_1+O_R(\varepsilon^2),\qquad
E_1=\int_{X\setminus\{p\}}\ell_g(B).
\]

A useful precise normal-coordinate estimate is
\[
\ell_g(B)
=2\langle\mathcal C_g(p),L_0B\rangle
+O(r)|L_0B|
+O(r^2)|\partial^2B|
+O(r)|\partial B|+O(1)|B|,
\quad L_0=D\mathcal C_\delta.
\]
For \(A\), the otherwise dangerous leading term vanishes:
\[
L_0A=0\quad(r>0).
\]
Thus \(\ell_g(A)=O(r^{-2})\), and also \(\ell_g(K)=O(r^{-2})\). This proves absolute integrability and shows that the omitted inner linear integral is
\[
\varepsilon\int_{r<a_\varepsilon}\ell_g(B)=O(\varepsilon^2R^2).
\]

For a cutoff \(\chi_\eta\) supported near \(p\), the tensor
\((1-\chi_\eta)B\) is smooth and compactly supported inside the critical neighborhood. First variations of \(P\) and \(\int F_+\) agree for smooth compactly supported variations, so
\[
\int\ell_g((1-\chi_\eta)B)=0.
\]
Therefore
\[
E_1=\lim_{\eta\to0}\int\ell_g(\chi_\eta B).
\]
This reduction genuinely uses only local \(P\)-criticality, not Einsteinity. Without criticality on the whole insertion support, an additional bulk first variation remains.

The localization errors tend to zero; the \(K\)-part is \(O(\eta^2)\). Consequently
\[
E_1=2\langle\mathcal C_g(p),c_A\rangle,\qquad
c_A=\int_{\mathbb R^4\setminus0}L_0(\chi A)\,dx.
\]

### Potential replacement and the factor-two correction

The difference
\[
\chi A-\partial\bar\partial_\zeta(\chi\log r^2)
\]
is smooth and compactly supported in an annulus. Every component of \(L_0\) is a constant-coefficient second-order divergence, so its integral on this difference vanishes.

Let
\[
M_\zeta=3\zeta\otimes\zeta-I
=\operatorname{diag}(2,-1,-1)_\zeta.
\]
Along a fixed-complex-structure Kähler variation of the flat metric,
\[
(W^+)'=\frac{s'}{12}M_\zeta.
\]
Variation of the Kähler eigenframe causes no additional term, since \(s=W^+=0\) at the flat base. But \(\mathcal C=(2W^+,s/\sqrt{12})\), so the correct formula is
\[
\boxed{c_A=m\left(\frac{M_\zeta}{6},\frac1{\sqrt{12}}\right),}
\]
not the printed \(M_\zeta/12\).

With the stated normalization,
\[
\partial\bar\partial_\zeta\phi
=\frac14\bigl(\operatorname{Hess}\phi+
J_\zeta^T\operatorname{Hess}\phi J_\zeta\bigr),
\]
and flat scalar linearization gives
\[
s'(\partial\bar\partial_\zeta\phi)=-\frac14\Delta^2\phi.
\]
Indeed, \(\operatorname{tr}(\partial\bar\partial\phi)=\Delta\phi/2\) and its double divergence is \(\Delta^2\phi/4\).

For \(\chi=1\) near zero,
\[
\int_{\mathbb R^4\setminus0}\Delta^2(\chi\log r^2)\,dx=16\pi^2.
\]
This is the punctured-domain Green flux: with \(\Delta=\sum_i\partial_i^2\),
\(\Delta^2\log r^2=-16\pi^2\delta_0\) distributionally, and the full distributional integral of the compactly supported potential’s bi-Laplacian is zero. Hence
\[
m=-4\pi^2.
\]
Using \(\langle W^+,M_\zeta\rangle=3W^+(\zeta,\zeta)\),
\[
\boxed{E_1=2mR^+_p(\zeta,\zeta)
=-8\pi^2R^+_p(\zeta,\zeta).}
\]
Thus \(\kappa=-4\pi^2\), independently of calibration. This matches both Step 20’s scalar flux \(4\pi^2\) and A01’s outward flux
\(\theta_2=8\pi^2\mu_\zeta\), whose contribution is \(-\varepsilon\theta_2\).

---

## 3. \(W^-\): Schur cancellation and the computational artifact

### Integrated cross terms

The Burns tail and the \((s,W^+)\) jet are fixed by \(SU(2)_-\). The invariant corrector \(K^*\) is fixed as well. In contrast,
\[
W^-\in\operatorname{Sym}^2_0(\Lambda^-)
\]
is the nontrivial irreducible spin-two representation. The map
\[
W^-\longmapsto
\left(h_W,\,
k_0^W=\frac32\operatorname{sym}(h_WA)
-\frac14\operatorname{tr}(h_WA)\delta\right)
\]
is equivariant.

Polarizing the **entire** integrated \(\sigma^2\) coefficient produces an invariant linear functional of \(W^-\) when one argument is the invariant block. That functional is zero. This proves cancellation of all cross terms, including terms arising from the higher \(\sigma\)-coefficients of the linearized curvature and the metric-dependent norm and volume—not merely a selected \(\langle Y_{\rm inv},Y_W\rangle\) term.

For a pure \(W^-\) jet,
\[
D\mathcal C_\delta[h_W]=0,
\]
so its self-coefficient is the nonnegative norm-square of the geometric first residual. The exact identity stated in the supplied notes says \(k_0^W\) kills this residual pointwise. Together with Schur cancellation, this removes arbitrary \(W^-\) from the Einstein coefficient.

### What went wrong in the older script

The script constructs
\[
X=P_+R'P_+-\frac{s'}{12}P_+
\]
using the projector at \(t=0\), while differentiating the curvature endomorphism in a fixed coordinate pair basis. The true derivative also contains projector-variation terms:
\[
(W^+)'=
X+P_+'R_BP_++P_+R_BP_+' ,
\]
since \(s(B_\sigma)=0\).

In a frame orthonormal for \(B_\sigma\), let \(H'\) denote the derivative of the two-form inner-product matrix. Hodge-star variation gives
\[
P_+'=\tfrac12[P_+,H'].
\]
Using \(P_+R_BP_+=0\), the missing \(++\)-block is
\[
\frac12\left(H'_{+-}R_{-+}-R_{+-}H'_{-+}\right),
\]
which is skew-adjoint. The true chiral derivative is self-adjoint, so this term precisely cancels the skew part of \(X\).

At order \(\sigma\), the background curvature is \(O(\sigma)\); consequently this skew defect depends on \(h_2\), but not on \(K\), which occurs in the perturbation as \(\sigma K\). For \(X_0=0\), writing \(X_1=S+N\) gives
\[
\operatorname{tr}X_1^2=|S|^2-|N|^2,
\]
and the geometric coefficient is
\[
\boxed{4|\operatorname{sym}X_1|^2+s_1^2/12,}
\]
not \(4\operatorname{tr}X_1^2+s_1^2/12\). This explains the same negative deficit before and after adding \(k_0^W\), exactly as reported in C.1.

### Necessary limitation of the \(W^+\) check

`step60_jax_check_Wplus.py` uses
\[
W^+=
\begin{pmatrix}
2&0&0\\
0&-3&1\\
0&1&1
\end{pmatrix},
\]
so \(\zeta\) **is an eigenvector**. Its two tests vary \(K\), not that eigenvector condition.

At the Euclidean leading order, the skew defect in the invariant curvature sector is proportional to the skew product of \(\zeta\) with \((R^+\zeta)^\perp\): in a radial frame, the mixed two-form action of the normal-coordinate jet is a scalar multiple of \(I\) plus a multiple of \(W^+\), while the Burns mixed curvature selects the \(\zeta\)-line. It therefore vanishes on the eigenvector locus. This explains why the exact eigenvector calculation is unaffected.

**Replace C.1’s unrestricted sentence by:**

> The exact \((s,W^+)\) coefficient used in §A.3, restricted to \(w_{12}=w_{13}=0\), is unaffected by this defect. The supplied orthonormal-frame JAX check tests this locus for \(K=0\) and a generic invariant \(K\). It does not establish correctness of the older script off the eigenvector locus.

The reported exact pointwise \(W^-\) check and the inherited identity are stronger than the single numerical sample. The supplied JAX script alone does not prove cancellation for every point and every \(W^-\).

### Corrector coefficient

The script defines mixed products by
\[
u\odot v=\tfrac12(u\otimes v+v\otimes u).
\]
The JSON and differentiation of its quadratic form give \(k_5=2w_{23}/3\). Thus the unambiguous corrected representative is
\[
\boxed{
\begin{aligned}
K^*={}&\frac{s}{24}dr^2
+\left(-\frac{s}{48}+\frac{7w_{11}}6+\frac{w_{22}}3\right)s_1^2\\
&+\frac{2w_{23}}3\,s_1\odot s_2
+\left(-\frac{s}{48}+\frac{5w_{11}}6-\frac{w_{22}}3\right)s_2^2 .
\end{aligned}}
\]
The printed \(4w_{23}/3\) is inconsistent with this convention. The KE-perpendicular specialization, where \(w_{23}=0\), is unaffected.

---

## 4. Eigenvector and sign scope

There are three distinct statements.

### General expansion

Theorem 59.R and the geometric definition (A.2) require **no eigenvector hypothesis**. They apply to every fixed unit \(\zeta\) and every fixed smooth homogeneous degree-zero \(K\).

### Explicit optimized coefficient

For \(\zeta\) an eigenvector and \(\operatorname{Ric}^\circ_p=0\), the invariant calculation, together with \(W^-\) cancellation, yields
\[
\boxed{
\Phi_{\rm opt}
=-\mu_1(\mu_1-s/8)-|T|^2
=-\frac12\mu_1(\mu_1-\mu_2-\mu_3)
-\frac12(\mu_2-\mu_3)^2.}
\]
Here \(T\) is the trace-free restriction of \(R^+\) to \(\zeta^\perp\).

For the \((s,W^+)\) sector, minimizing over invariant correctors suffices: the functional is convex in \(K\), its quadratic part is a flat chiral-linearization norm-square, and compact-group averaging decreases it. For Einstein jets, the equivariant \(W^-\) corrector attains the same value.

The supplied materials do **not** certify a Ricci-trace-free cancellation for general \(P\)-critical jets. One should not promote the search for such a corrector into a proved minimized formula. A fixed uncanceled Ricci residual has a nonnegative self-term.

### Kernel versus interior

On the eigenvector kernel locus,
\[
\Phi_{\rm opt}=-|T|^2\le0.
\]
This is **not** a sign statement for arbitrary \(K\), nor for general \(P\)-critical jets with an uncanceled Ricci sector.

In the strict cone \(R^+<0\), the optimized coefficient has no universal sign:
\[
W^+=0\quad\Longrightarrow\quad
\Phi_{\rm opt}=s^2/288>0.
\]
It is subordinate to the positive first-order cost \(-8\pi^2\varepsilon\mu_1\).

A zero Rayleigh value with \(R^+\zeta\ne0\) forces \(R^+\) to be indefinite. A01’s supplied exact mixed-block computation gives an unbounded-below logarithmic functional through a Hessian-null corrector direction. This does not invalidate the expansion for each fixed \(K\), and a positive eigenvalue already supplies a first-order saving.

The JSON flag `"leak_solvable": true` does not resolve that mixed-block question: it records only whether `sympy.solve` returned a dictionary, without recording or verifying its domain or all substituted gradient equations. Moreover, the off-eigenvector density is precisely where the older representation requires correction. The source-level artifact still needing reconciliation is that flag versus the explicit null-direction coupling. The decisive object is the geometric functional’s coefficients of the Hessian-null \(dr\odot s_i\) directions, together with a substitution check of every claimed stationary equation.

**Replace C.2’s hypothesis sentence by:**

> Theorem 59.R holds for every unit \(\zeta\) and fixed degree-zero corrector. The explicit optimized formula and \(K^*\) in §A.3 assume that \(\zeta\) is an eigenvector of \(R^+\). On \(R^+\le0\), a zero Rayleigh direction is automatically a kernel eigenvector.

**Replace C.3’s opening by:**

> For Einstein backgrounds, unit directions satisfying \(R^+\zeta=0\), and arbitrary \(W^-\), A01 proves the stated no-order-\(\varepsilon\) expansion, uniformly on compact families of admissible insertion data.

Corollary 59.Rig remains conditional on its energy/topology ledger. Its Ricci-smallness extension should be expressed quantitatively as
\[
|T|^2>Q_{\rm Ric}
\]
for an explicitly chosen Ricci residual, or sufficiently
\[
|T|^2>C|\operatorname{Ric}^\circ_p|^2.
\]
It does not require an uncertified global minimum over Ricci correctors. The Einstein-only differential lemma from A01 cannot be applied to a merely \(P\)-critical bulk; C.3 correctly identifies this limitation.

---

## 5. ADE gluing: uniformity and strict inequality

Choose the insertion balls in the regular locus of the canonical model, disjoint from all ADE gluing regions. The supplied construction permits
\[
g_\lambda=g_{\rm KE}
\]
on fixed neighborhoods containing those balls, while \(P(g_\lambda)\to0\).

All terms in the insertion density difference are supported in these fixed neighborhoods. Thus the local difference \(I(\varepsilon)\) is actually independent of \(\lambda\), not merely bounded by a uniform error estimate. No global curvature bound for \(g_\lambda\), and no global \(P\)-criticality, is needed.

For \(k\) insertions,
\[
\frac{P(\widetilde g_{\lambda,\varepsilon})}{8\pi^2}
=\frac{P(g_\lambda)}{8\pi^2}
+k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2),
\]
uniformly in \(\lambda\).

Fix \(\varepsilon>0\) sufficiently small that the negative logarithmic term dominates the uniform remainder. Then choose \(\lambda\) so that \(P(g_\lambda)\) is smaller than the resulting saving. This gives an **actual smooth competitor** below \(8\pi^2k\). Equivalently, taking \(\lambda\to0\) at that fixed \(\varepsilon\) gives an infimum bound strictly below the threshold.

Consequently the stated strict inequality holds for every minimal surface of general type, using the canonical-model/orbifold-KE inputs stated in the supplied note. No limit metric or attainment is required. The additional comparison with the Kähler infimum depends on Theorem \(K_\infty\), whose proof is not supplied here and is not needed for the unrestricted strict upper bound.

---

## Corrected theorem and corollary wording

### Theorem 59.R

> Let \(g\) be a smooth metric on a closed oriented four-manifold \(X\). Choose normal coordinates near \(p\), and choose \(\rho\) so that \(E_P(g)=0\) on \(B_{2\rho}(p)\). Fix a unit \(\zeta\in\Lambda^+_p\), a smooth homogeneous degree-zero symmetric tensor \(K\) on \(\mathbb R^4\setminus0\), fixed \(R\ge1\), and the cutoffs of A.1. For sufficiently small \(\varepsilon\), the resulting metric is smooth on \(X\#\overline{\mathbb{CP}}^{\,2}\), and
> \[
> P(\widetilde g_\varepsilon)
> =P(g)+8\pi^2
> -8\pi^2\varepsilon R^+_p(\zeta,\zeta)
> +4\pi^2\Phi(Rm_p,\zeta,K)\varepsilon^2\log(1/\varepsilon)
> +O(\varepsilon^2),
> \]
> where \(\Phi\) is the geometric expression (A.2). The remainder depends only on the fixed local metric and insertion data. No eigenvector assumption is required.
>
> If \(\operatorname{Ric}^\circ_p=0\) and \(\zeta\) is an eigenvector of \(R^+_p\), the optimized coefficient is
> \[
> \Phi_{\rm opt}=-\mu_1(\mu_1-s/8)-|T|^2,
> \]
> attained by the corrected \(K^*+k_0^W\).

### Corollary 59.KE

> Let \(X\) be a compact Kähler–Einstein surface with \(s\ne0\), and \(k\ge1\). At \(k\) distinct points choose unit directions
> \(\zeta_i\in\omega^\perp=\ker R^+\). The corrected insertions satisfy
> \[
> \frac{P(\widetilde g_\varepsilon)}{8\pi^2}
> =k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2),
> \]
> and therefore
> \[
> p_*(X\#k\overline{\mathbb{CP}}^{\,2})<8\pi^2k.
> \]
> For any minimal surface of general type, use its orbifold Kähler–Einstein canonical model and a Kronheimer gluing sequence equal to that metric on fixed insertion neighborhoods. The same expansion holds with the added term \(P(g_\lambda)/(8\pi^2)\), uniformly in \(\lambda\). Choosing \(\varepsilon\) first and then \(\lambda\) proves the same strict inequality.

These are competitor upper bounds. They establish neither a positive lower gap nor attainment, and they do not eliminate the strictly negative \(R^+\) regime.