# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Sessions/S1003A02/workspace/scripts/step59_exact_log_coefficient.py",
    "Sessions/S1003A02/workspace/data/step59_exact_log_coefficient.json",
    "Sessions/S1003A02/workspace/scripts/step60_jax_check.py",
    "Sessions/S1003A02/workspace/scripts/step60_jax_check_Wplus.py",
    "Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Verify Part A of the Step-59 note (Theorem 59.R, the rigorous second-order Burns expansion, and Corollary 59.KE, p_*(X#k CPbar^2) < 8 pi^2 k for every minimal surface of general type), as corrected by Part C. Check specifically and give corrected statements where needed: (1) smoothness in (sigma, r, y) of the rescaled far-annulus metric G_{sigma,r} and of the density difference, the claimed factorization r^4 * gamma~(sigma,r) with gamma~(0,r)=0, and the Taylor/log bookkeeping that yields 4 pi^2 Phi eps^2 log(1/eps) + O(eps^2) including the cutoff psi_eps for K and the inner region O(eps^2 R^4); whether 'F+ quadratic in the perturbation of a C-null model' really excludes 3-jets/4-jets from the log term. (2) The distributional evaluation of the order-eps term E_1 = 2 kappa R+(zeta,zeta): validity of reducing to lim_{eta->0} int ell_g(chi_eta B) using only E_P=0 near p (P-critical, not Einstein), the replacement chi A -> ddbar(chi log r^2), the linearized Kahler identity W+' = (s'/12) diag(2,-1,-1), the Green flux, and the sign/normalization 2 kappa = -8 pi^2 (compare A01's independent flux theta_2 = 8 pi^2 mu_zeta in Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md). (3) The Schur argument that W- cross terms with the SU(2)_- invariant block vanish after S^3 integration, and the W- self-term killed by k0^W (Part C.1 reports an exact pointwise check and a representation artifact in the exact script; judge the artifact explanation using step60_jax_check.py and step60_jax_check_Wplus.py). (4) The order of limits for canonical models with ADE points (Kronheimer gluing at scale lambda, then lambda -> 0 at fixed eps), whether the error constants in 59.R are uniform in lambda given g_lambda = g_KE near the p_i, and whether the conclusion 'strict inequality for every minimal surface of general type' is correctly obtained (note p_* is an infimum so a sequence suffices). (5) Whether the eigenvector hypothesis on zeta and the kernel/interior sign scope (Part C.2) are stated correctly everywhere in Parts A-C. Return a direct scientific memo: what is proved, what must be repaired, and exact corrected wording.

## Output

# Scientific memo: verification of Step 59, Part A

## 1. Overall conclusion

The second-order Burns expansion is mathematically sound after several precise repairs:

1. The far-annulus factorization and logarithmic bookkeeping are valid for fixed \(R\), provided \(2R\sqrt\varepsilon<\rho\) and the cutoff defining \(\psi_\varepsilon\) is already equal to \(1\) at \(r=2R\sqrt\varepsilon\).
2. The order-\(\varepsilon\) flux is
   \[
   E_1=-8\pi^2R_p^+(\zeta,\zeta).
   \]
   In the displayed computation of \(c_A\), the \(W^+\)-component must be \(mM_\zeta/6\), not \(mM_\zeta/12\), where \(M_\zeta=\operatorname{diag}(2,-1,-1)\). With the stated \(\partial\bar\partial\)-normalization, \(m=-4\pi^2\).
3. The \(W^-\) corrector is valid. The matrix expression used by the older exact script is not the geometric squared norm in sectors whose zeroth-order chiral curvature vanishes. Part C.1 identifies the correct symmetric component, and the exact identity for \(k_0^W\) removes that residual pointwise.
4. The strict inequality for every minimal surface of general type follows from the inherited Kronheimer gluing sequence. The order must be: choose \(\varepsilon\) first so that the logarithmic saving dominates the uniform \(O(\varepsilon^2)\) term, then choose \(\lambda\) so that \(P(g_\lambda)\) is smaller than that saving.
5. The expansion theorem itself does not require \(\zeta\) to be an eigenvector. The explicit minimized formula for \(\Phi\), its sign description, and the displayed \(K^*\) do require the eigenvector assumption. The no-linear-term A01 formula quoted in Part C.3 additionally requires \(R^+\zeta=0\).

With these repairs, Corollary 59.KE is established:
\[
p_*\!\left(X\#k\overline{\mathbb {CP}}^{\,2}\right)<8\pi^2k
\]
for every minimal surface \(X\) of general type and every \(k\ge1\).

---

## 2. Far-annulus expansion and the logarithmic term

Set
\[
B_\sigma=\delta+\sigma A,\qquad
a_\varepsilon=2R\sqrt\varepsilon.
\]
On \(a_\varepsilon\le r\le\rho\), one has \(\psi_\varepsilon=1\) and \(\chi_\rho=1\). After the rescaling \(x=ry\),
\[
r^{-2}\Phi_r^*\widetilde g_\varepsilon
 =G_{\sigma,r}
 =B_\sigma+r^2q_{\sigma,r},
\qquad
q_{\sigma,r}(y)=\bar h(ry,y)+\sigma K(y),
\qquad
\sigma=\frac{\varepsilon}{r^2}.
\]

### Smoothness

Although \(h(x)/|x|^2\) need not be a smooth function of \(x\) at \(x=0\), the expression
\[
\frac{h(ry)}{r^2}
  =h_2(y)+rh_3(y)+r^2h_4(y)+\cdots
\]
is smooth in \((r,y)\in[0,\rho]\times U\), where \(U=\{1/2\le |y|\le2\}\). Thus \(G_{\sigma,r}\) is smooth in the independent variables
\[
(\sigma,r,y)\in
\left[0,\frac1{4R^2}\right]\times[0,\rho]\times U.
\]
For sufficiently small \(\rho\), these metrics remain uniformly positive definite.

Since the Burns family is scalar-flat and anti-self-dual,
\[
\mathcal C(B_\sigma)=0
\]
for every \(\sigma\). Smooth dependence of the curvature operator on the metric and its first two derivatives therefore gives
\[
\mathcal C(G_{\sigma,r})=r^2Q(\sigma,r,y)
\]
with \(Q\) smooth. Consequently,
\[
F_+(G_{\sigma,r})\,d\mu_{G_{\sigma,r}}
   =r^4H(\sigma,r,y)
\]
with \(H\) smooth. At \(\sigma=0\), \(G_{0,r}\) is exactly the rescaled background metric. Hence the density difference has the form
\[
F_+(G_{\sigma,r})d\mu_{G_{\sigma,r}}
 -F_+(G_{0,r})d\mu_{G_{0,r}}
 =r^4\widetilde H(\sigma,r,y),
\qquad
\widetilde H(0,r,y)=0.
\]

After integration over the unit sphere, write
\[
\widetilde\gamma(\sigma,r)
 =\int_{S^3}\widetilde H(\sigma,r,y).
\]
The far-annulus contribution is therefore
\[
I_f
 =\int_{a_\varepsilon}^{\rho}
   r^3\widetilde\gamma\!\left(\frac{\varepsilon}{r^2},r\right)\,dr.
\]

### Taylor expansion and logarithm

Uniform Taylor expansion in \(\sigma\) gives
\[
\widetilde\gamma(\sigma,r)
 =\sigma\gamma_1(r)+\sigma^2\gamma_2(r)
   +\sigma^3\gamma_3(\sigma,r).
\]
Substitution of \(\sigma=\varepsilon/r^2\) yields
\[
I_f
 =\varepsilon\int_{a_\varepsilon}^{\rho}r\gamma_1(r)\,dr
 +\varepsilon^2\int_{a_\varepsilon}^{\rho}\frac{\gamma_2(r)}r\,dr
 +\varepsilon^3\int_{a_\varepsilon}^{\rho}
        \frac{\gamma_3(\varepsilon/r^2,r)}{r^3}\,dr.
\]

The last term is
\[
O\!\left(\varepsilon^3a_\varepsilon^{-2}\right)
 =O\!\left(\frac{\varepsilon^2}{R^2}\right).
\]
Smoothness gives \(\gamma_2(r)=\gamma_2(0)+O(r)\), so
\[
\begin{aligned}
\varepsilon^2\int_{a_\varepsilon}^{\rho}\frac{\gamma_2(r)}r\,dr
&=\varepsilon^2\gamma_2(0)
   \log\frac{\rho}{2R\sqrt\varepsilon}
   +O(\varepsilon^2)\\
&=\frac12\gamma_2(0)\varepsilon^2\log(1/\varepsilon)
   +O(\varepsilon^2).
\end{aligned}
\]
At \(r=0\),
\[
Q(\sigma,0,\cdot)
 =D\mathcal C_{\delta+\sigma A}[h_2+\sigma K],
\]
and hence
\[
\gamma_2(0)=8\pi^2\Phi.
\]
This gives exactly
\[
4\pi^2\Phi\,\varepsilon^2\log(1/\varepsilon).
\]

### Dependence on the metric jets

The rescaled bulk expansion is
\[
G_{\sigma,r}
 =B_\sigma
  +r^2(h_2+\sigma K)+r^3h_3+r^4h_4+\cdots .
\]
Because \(\mathcal C(B_\sigma)=0\),
\[
\mathcal C(G_{\sigma,r})
 =r^2C_2(\sigma)+r^3C_3(\sigma)+r^4C_4(\sigma)+\cdots.
\]
Thus the degree-\(r^4\) term of the chiral square is \(|C_2(\sigma)|^2\). Terms involving \(h_3\) first occur at degree \(r^5\), and terms involving \(h_4\) first occur at degree \(r^6\). Equivalently, \(h_3\) changes \(\gamma_2(r)\) by \(O(r)\), while \(h_4\) changes it by \(O(r^2)\); neither affects the logarithmic coefficient.

Therefore the statement that only the two-jet enters \(\Phi\) is correct. The essential mechanism is not merely that \(F_+\) is quadratic: it is the combination
\[
\mathcal C(B_\sigma)=0
\quad\text{and}\quad
F_+=|\mathcal C|^2.
\]

---

## 3. Inner region and the cutoff \(\psi_\varepsilon\)

Under \(x=\sqrt\varepsilon\,u\),
\[
\varepsilon^{-1}\Phi_{\sqrt\varepsilon}^*
\widetilde g_\varepsilon
 =g_{B,1}
  +\varepsilon\Bigl(
       |u|^2\bar h(\sqrt\varepsilon u,u)
       +\psi(u/R)K(u)
    \Bigr).
\]
The cutoff removes \(K\) near the exceptional curve, so the term in parentheses is a smooth tensor on the blown-up ball \(\{|u|\le2R\}\). For fixed \(R\), it is bounded in every required \(C^m\)-norm.

Since \(\mathcal C(g_{B,1})=0\),
\[
\mathcal C\!\left(
\varepsilon^{-1}\Phi_{\sqrt\varepsilon}^*
\widetilde g_\varepsilon\right)
 =O_R(\varepsilon).
\]
Scale invariance of \(F_+d\mu\) then gives
\[
\int_{r\le2R\sqrt\varepsilon}
 F_+(\widetilde g_\varepsilon)\,d\mu_{\widetilde g_\varepsilon}
 =O_R(\varepsilon^2).
\]
For the background,
\[
\int_{r\le2R\sqrt\varepsilon}F_+(g)\,d\mu_g
 =O(\varepsilon^2R^4).
\]

Thus the useful statement is
\[
I_{\mathrm{inner}}=O_R(\varepsilon^2).
\]
Writing \(O(\varepsilon^2R^4)\) is harmless when \(R\) is fixed and the hidden constant is allowed to depend on \(R\), but it does not by itself provide a uniform polynomial estimate as \(R\to\infty\). No passage \(R\to\infty\) is used in Theorem 59.R.

The transition of \(\psi_\varepsilon\) lies entirely in this rescaled compact region and therefore contributes \(O_R(\varepsilon^2)\), with no logarithm.

---

## 4. Order-\(\varepsilon\) term and direct flux normalization

Let
\[
B=\chi_\rho(A+K),
\]
with \(B_{2\rho}(p)\) contained in the region where \(E_P(g)=0\). The first-order terms from the far and outer regions combine into
\[
E_1=\int_{X\setminus\{p\}}\ell_g(B).
\]

### Local integrability

The local estimate in the Step-59 proof should be written more precisely as
\[
\ell_g(B)
 =2\langle\mathcal C_g(p),L_0B\rangle
  +O(r)|L_0B|
  +O(r^2)|\partial^2B|
  +O(r)|\partial B|
  +O(1)|B|.
\]
The \(O(r^2)\) coefficient in front of \(\partial^2B\) comes from normal coordinates, where \(g-\delta=O(r^2)\).

For the Burns tail,
\[
L_0A=0\qquad(r>0),
\]
and \(A,\partial A,\partial^2A\) have orders \(r^{-2},r^{-3},r^{-4}\), respectively. Hence \(\ell_g(A)=O(r^{-2})\). For homogeneous degree-zero \(K\), \(L_0K=O(r^{-2})\), so \(\ell_g(K)=O(r^{-2})\) as well. Thus \(E_1\) converges absolutely, and omitting the ball \(r<2R\sqrt\varepsilon\) changes the linear contribution by
\[
\varepsilon\,O((R\sqrt\varepsilon)^2)
 =O(\varepsilon^2R^2).
\]

### Use of local \(P\)-criticality

Let \(\chi_\eta\) equal \(1\) near \(p\) and vanish for \(r\ge2\eta\). Then
\[
(1-\chi_\eta)B
\]
is a smooth compactly supported tensor inside the \(P\)-critical neighborhood. Since the first variations of \(P\) and \(\int F_+\) agree on a closed manifold,
\[
\int_X\ell_g((1-\chi_\eta)B)=0.
\]
Therefore
\[
E_1
 =\lim_{\eta\to0}\int_X\ell_g(\chi_\eta B).
\]
Einsteinity is not needed here; local \(P\)-criticality is sufficient.

### Distributional calculation

The \(K\)-part tends to zero like \(O(\eta^2)\). The leading term is
\[
E_1=2\langle\mathcal C_g(p),c_A\rangle,
\qquad
c_A=\int_{\mathbb R^4\setminus\{0\}}L_0(\chi A)\,dx.
\]

Because
\[
A=\partial\bar\partial_\zeta\log r^2
\]
away from the origin, the difference
\[
\chi A-\partial\bar\partial_\zeta(\chi\log r^2)
\]
is smooth and compactly supported in an annulus. Each component of \(L_0\) is a constant-coefficient second-order divergence, so its integral on this difference is zero.

Let
\[
M_\zeta=\operatorname{diag}(2,-1,-1)
       =3\,\zeta\otimes\zeta-I_{\Lambda^+}.
\]
For a Kähler variation of the flat metric,
\[
(W^+)'=\frac{s'}{12}M_\zeta.
\]
Since \(\mathcal C=(2W^+,s/\sqrt{12})\), this gives
\[
c_A
 =m\left(\frac{M_\zeta}{6},\frac1{\sqrt{12}}\right),
\qquad
m=\int_{\mathbb R^4\setminus\{0\}}s'
   \bigl(\partial\bar\partial(\chi\log r^2)\bigr)\,dx.
\]
The factor \(M_\zeta/12\) printed in Step 59 is off by a factor of two.

With
\[
\partial\bar\partial\phi
 =\frac14\bigl(\operatorname{Hess}\phi
      +J_\zeta^T(\operatorname{Hess}\phi)J_\zeta\bigr),
\]
the flat scalar linearization is
\[
s'(\partial\bar\partial\phi)=-\frac14\Delta^2\phi.
\]
For a cutoff equal to \(1\) near the origin,
\[
\int_{\mathbb R^4\setminus\{0\}}
   \Delta^2(\chi\log r^2)\,dx=16\pi^2,
\]
and hence
\[
m=-4\pi^2.
\]
Since \(\operatorname{tr}W^+=0\),
\[
\langle W^+,M_\zeta\rangle=3W^+(\zeta,\zeta).
\]
It follows that
\[
\begin{aligned}
E_1
 &=2m\left(
 W^+(\zeta,\zeta)+\frac{s}{12}
 \right)\\
 &=-8\pi^2R^+(\zeta,\zeta).
\end{aligned}
\]
This agrees exactly with the independent A01 flux computation.

---

## 5. \(W^-\) sector and the script artifact

For a pure \(W^-\) jet,
\[
D\mathcal C_\delta[h_2^W]=0.
\]
The geometric order-\(\sigma\) residual is a self-adjoint \(W^+\)-operator together with a scalar component. If \(X_1\) denotes the older script’s fixed-pair-basis matrix, the actual density in this sector is
\[
4\left|\operatorname{sym}X_1\right|^2+\frac{s_1^2}{12}.
\]
Writing \(X_1=S+N\), with \(N\) skew-symmetric,
\[
\operatorname{tr}(X_1^2)=|S|^2-|N|^2.
\]
Thus the script expression \(4\operatorname{tr}(X_1^2)+s_1^2/12\) contains the extraneous term \(-4|N|^2\). This explains the values reported in Part C.1.

The JAX computations using a Cholesky orthonormal frame give:

- \(W^-\), \(K=0\): agreement with the symmetric-part expression;
- \(W^-\), \(K=k_0^W\): geometric coefficient numerically zero, while the older signed expression is \(-0.113\);
- Ricci-trace-free samples: again agreement with the symmetric-part expression;
- the \((s,W^+)\) samples: agreement between the exact script and JAX to approximately fifteen digits.

The pointwise corrector
\[
k_0^W
 =\frac32\operatorname{sym}(h_Wk_B)
  -\frac14\operatorname{tr}(h_Wk_B)\,\delta
\]
satisfies
\[
\operatorname{sym}X_1=0,\qquad s_1=0
\]
exactly. Together with the inherited exact Step-50 identity, this proves that the \(W^-\) self-term vanishes.

For the mixed term, the \((s,W^+)\) block and its invariant corrector are fixed by \(SU(2)_-\), while \(W^-\in\operatorname{Sym}^2_0(\Lambda^-)\) is the irreducible spin-two representation. The integrated cross term is therefore an \(SU(2)_-\)-invariant linear functional of \(W^-\), and no such nonzero functional exists. Hence the cross term vanishes after integration over \(S^3\).

The exact eigenvector formula remains
\[
\Phi
 =-\frac12\mu_1(\mu_1-\mu_2-\mu_3)
  -\frac12(\mu_2-\mu_3)^2.
\]

A minor coefficient inconsistency also appears in the printed \(K^*\). The JSON output gives \(k_5=2w_{23}/3\). Thus, if
\[
u\odot v=\frac12(u\otimes v+v\otimes u),
\]
the \(k_9=0\) representative is
\[
\begin{aligned}
K^*={}&\frac{s}{24}dr^2
 +\left(-\frac{s}{48}+\frac{7w_{11}}6+\frac{w_{22}}3\right)s_1^2\\
&+\frac{2w_{23}}3\,s_1\odot s_2
 +\left(-\frac{s}{48}+\frac{5w_{11}}6-\frac{w_{22}}3\right)s_2^2.
\end{aligned}
\]
The coefficient \(4w_{23}/3\) in the note is not consistent with the script’s stated symmetric-product convention.

---

## 6. Canonical models and the order of parameters

For a minimal surface \(X\) of general type, its canonical model has only ADE singularities. Choose the insertion points \(p_i\) in the regular locus, away from the ADE gluing regions. The standard cutoff construction may be arranged so that
\[
g_\lambda=g_{\mathrm{KE}}
\]
on fixed neighborhoods of all \(p_i\), while
\[
P(g_\lambda)\longrightarrow0.
\]

The constants in Theorem 59.R are then uniform in \(\lambda\), because:

- the inserted metric differs from \(g_\lambda\) only in those fixed neighborhoods;
- all local jets there are exactly those of \(g_{\mathrm{KE}}\);
- local \(P\)-criticality holds there;
- the cutoffs, \(K^*\), \(k_0^W\), \(R\), and \(\rho\) are fixed;
- the rest of the manifold enters only through the baseline value \(P(g_\lambda)\).

Thus
\[
\frac{P(\widetilde g_{\lambda,\varepsilon})}{8\pi^2}
 =\frac{P(g_\lambda)}{8\pi^2}
  +k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
  +O(\varepsilon^2),
\]
with the \(O(\varepsilon^2)\) constant independent of \(\lambda\).

Choose \(\varepsilon\) so small that
\[
-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
 +O(\varepsilon^2)<-\delta_\varepsilon
\]
for some \(\delta_\varepsilon>0\). Then choose \(\lambda\) so small that
\[
P(g_\lambda)<8\pi^2\delta_\varepsilon.
\]
This produces an actual smooth metric on
\[
X\#k\overline{\mathbb {CP}}^{\,2}
\]
whose \(P\)-energy is strictly less than \(8\pi^2k\). Since \(p_*\) is an infimum, no convergence or attainment statement is needed.

---

## 7. Eigenvector and sign statements

The proper separation is:

- **Theorem 59.R:** valid for every unit \(\zeta\) and every fixed degree-zero \(K\).
- **Closed formula for the minimized \(\Phi\):** assumes \(R^+\zeta=\mu_1\zeta\), equivalently \(w_{12}=w_{13}=0\).
- **Kernel eigenline:** if \(\mu_1=0\),
  \[
  \Phi=-\frac12(\mu_2-\mu_3)^2\le0.
  \]
- **Strict cone \(R^+<0\):** \(\Phi\) has no uniform sign. For \(W^+=0\),
  \[
  \Phi=\frac{s^2}{288}>0.
  \]
  This term is subordinate to the first-order cost because \(-\varepsilon\mu_1>0\).
- **Zero Rayleigh value without an eigenline:** if
  \[
  R^+(\zeta,\zeta)=0,\qquad R^+\zeta\ne0,
  \]
  the expansion remains valid for each fixed \(K\), but the infimum of the logarithmic coefficient over the degree-zero corrector family is \(-\infty\). The associated symmetric operator is indefinite and already has a direction giving a first-order saving.
- **Semidefinite case:** if \(R^+\le0\) and \(R^+(\zeta,\zeta)=0\), then automatically \(R^+\zeta=0\), so the eigenvector formula applies.

The sentence in Part C.2 should therefore read:

> Theorem 59.R and the definition of \(\Phi\) require no eigenvector assumption. The explicit minimized formula in §A.3 and the displayed optimal corrector assume that \(\zeta\) is an eigenvector of \(R^+\).

The first sentence of Part C.3 should read:

> For an Einstein background, a unit vector \(\zeta\) satisfying \(R^+\zeta=0\), and arbitrary \(W^-\), A01 proves uniformly on compact families of such insertion data that
> \[
> P(g_\varepsilon)
> =P(g)+8\pi^2
>  -4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)
>  +O(\varepsilon^2).
> \]

---

## 8. Corrected theorem and corollary

### Theorem 59.R, corrected

Let \(g\) be smooth on a closed oriented four-manifold \(X\), and assume \(E_P(g)=0\) on a neighborhood containing \(B_{2\rho}(p)\). Fix a unit \(\zeta\in\Lambda_p^+\), a smooth homogeneous degree-zero corrector \(K\) on \(\mathbb R^4\setminus\{0\}\), and fixed \(R\ge1\). Then, for sufficiently small \(\varepsilon\),
\[
\boxed{
P(\widetilde g_\varepsilon)
 =P(g)+8\pi^2
  -8\pi^2\varepsilon R_p^+(\zeta,\zeta)
  +4\pi^2\Phi(Rm_p,\zeta,K)
       \varepsilon^2\log(1/\varepsilon)
  +O(\varepsilon^2).
}
\]
The constant in the remainder depends on the fixed local metric, cutoffs, \(\rho\), \(R\), \(\zeta\), and \(K\). Moreover,
\[
\Phi
 =\frac1{8\pi^2}\int_{S^3}
 [\sigma^2]\left(
 \left|
 D\mathcal C_{\delta+\sigma A}[h_2+\sigma K]
 \right|_{\delta+\sigma A}^2
 d\mu_{\delta+\sigma A}
 \right).
\]
No eigenvector assumption is used in this statement.

### Corollary 59.KE, corrected

Let \(X\) be a compact Kähler–Einstein surface with \(s\ne0\), and let \(k\ge1\). Choose disjoint points \(p_i\) and unit vectors
\[
\zeta_i\in\omega^\perp=\ker R^+.
\]
Using \(K^*+k_0^W\) at each point gives
\[
\frac{P(\widetilde g_\varepsilon)}{8\pi^2}
 =k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
  +O(\varepsilon^2),
\]
and therefore
\[
p_*\!\left(X\#k\overline{\mathbb {CP}}^{\,2}\right)<8\pi^2k.
\]

If \(X\) is any minimal surface of general type, use its orbifold Kähler–Einstein canonical model and a Kronheimer gluing sequence \(g_\lambda\) on \(X\), chosen to equal the orbifold Kähler–Einstein metric near fixed regular points \(p_i\). Then
\[
\frac{P(\widetilde g_{\lambda,\varepsilon})}{8\pi^2}
 =\frac{P(g_\lambda)}{8\pi^2}
  +k-\frac{ks^2}{64}\varepsilon^2\log(1/\varepsilon)
  +O(\varepsilon^2),
\]
uniformly in \(\lambda\). Choosing \(\varepsilon\) first and then \(\lambda\) proves the same strict inequality for every minimal surface of general type.