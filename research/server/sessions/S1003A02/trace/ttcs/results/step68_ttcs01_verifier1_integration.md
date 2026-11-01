# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 68,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step68_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step68_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify or refute the Step-67 product cscK saddle formula using the actual fixed-symplectic family. Setting: M=Sigma_1(K1) x Sigma_2(K2), K1,K2<0; Q is the real part of a holomorphic quadratic differential on Sigma_1; Delta_2 f=mu f; g_t|_1=g_1(exp(t f g_1^{-1}Q)·,·), g_t|_2=g_2, with fixed omega. The claimed Taylor t^2 coefficient is 8pi^2(p-|c1^-|^2)_2 = [mu/4][mu+2(K1-K2)]||fQ||^2. Derive this from actual connection/curvature variation or an exact integrated identity, checking all factors and the claims Ric''_1=(mu/2)k, rho0'_1=0, int u_2=(mu/4)||k||^2, and (rho0,t_2^-)=-[(K1-K2)mu/8]||k||^2. Resolve the apparent conflict in the supplied direct-coordinate scripts: they use local q=z^n on H^2 and produce n-dependent extra terms, suggesting that a pointwise local density is not the global integrated Hessian. Explain precisely whether those extras are divergences/Bochner terms and whether the global saddle formula is valid. Also check that an O(t^2) conformal correction to exact constant scalar curvature leaves the coefficient unchanged by Lemma 67.1. Give a proof-quality memo, not a procedural checklist.

## Integrated Scientific Memo

# Verification memo: the product saddle survives, but its threshold is halved

Let
\[
F(g)=P(g)-8\pi^2|c_1^-|_g^2,\qquad
P(g)=\int_M|\Ric^\circ_g|^2\,dV_g,
\]
and use Taylor coefficients, not second derivatives:
\[
F(g_t)=F(g_0)+tF_1+t^2F_2+O(t^3).
\]
For the stated fixed-symplectic exponential family, the correct coefficient is
\[
\boxed{
F_2
=8\pi^2(p-|c_1^-|^2)_2
=\frac{\mu}{4}\bigl[\mu+K_1-K_2\bigr]\|fQ\|_2^2 .
}
\]
Thus the Step-67 formula is **false as written**: its curvature-difference term is twice the correct value. The local scripts contain a genuine factor-two discrepancy as well as an intrinsic-curvature divergence. These must not be conflated.

Below is a direct curvature proof, followed by a connection-level check of all four proposed inputs.

## 1. Exact geometry and the harmonic term

Write \(A=g_1^{-1}Q\), \(k=fQ\), and
\[
G_t=g_1e^{tfA}.
\]
The endomorphism \(A\) is self-adjoint, tracefree, and anticommutes with \(J_1\). Consequently
\[
\det e^{tfA}=1,\qquad J_t=e^{-tfA}J_1
\]
on the first block. The area forms and volume form are exactly fixed:
\[
dA_{G_t}=\omega_1,\qquad dV_{g_t}=\omega_1\wedge\omega_2.
\]

The splitting remains orthogonal, so
\[
*_t\omega_1=\omega_2,\qquad *_t\omega_2=\omega_1.
\]
Both forms are therefore harmonic for every \(t\), and
\[
\eta=\omega_1-\omega_2
\]
is harmonic ASD with \(|\eta|^2=2\). The fixed closed form
\[
K_1\omega_1+K_2\omega_2
\]
represents \(2\pi c_1(J_t)=2\pi c_1(J_0)\) and remains harmonic. Its ASD part is
\[
\frac{K_1-K_2}{2}\eta.
\]
Hence \(|c_1^-|_{g_t}^2\) is **exactly constant**, giving
\[
F_2=P_2.
\]
This statement concerns the harmonic Chern-class representative; it does not assert that the actual Ricci form remains fixed beyond first order.

## 2. Direct curvature derivation

Use indices \(i,j\) on \(\Sigma_1\) and \(\alpha,\beta\) on \(\Sigma_2\). Let \(\Delta^{\mathrm{tr}}=\nabla^\alpha\nabla_\alpha=-\Delta_2\). The mixed Christoffel symbols are
\[
\Gamma^i_{\alpha j}
=\frac12(G_t^{-1}\partial_\alpha G_t)^i{}_j
=\frac t2 f_\alpha A^i{}_j,
\qquad
\Gamma^\alpha_{ij}
=-\frac12\nabla^\alpha G_{t,ij}.
\]
Their trace satisfies
\[
\tr(G_t^{-1}\partial_\alpha G_t)=0.
\]

For each fixed \(y\in\Sigma_2\), denote the Gaussian curvature of the first-block metric \(G_t(\,\cdot\,,y)\) by \(K_t\). Contracting the connection gives the vertical and horizontal Ricci blocks
\[
\begin{aligned}
\Ric_V
&=K_tG_t-\frac12\Delta^{\mathrm{tr}}_2G_t
+\frac12(\nabla^\alpha G_t)G_t^{-1}(\nabla_\alpha G_t),\\
\Ric_H
&=K_2g_2-\frac14\tr\!\left(
G_t^{-1}\partial_\alpha G_t\,
G_t^{-1}\partial_\beta G_t
\right).
\end{aligned}
\]
Here the terms involving derivatives along \(\Sigma_1\) are already included in the intrinsic term \(K_tG_t\).

Because
\[
\Delta^{\mathrm{tr}}_2G_t
=t(\Delta^{\mathrm{tr}}_2f)G_tA
+t^2|df|^2G_tA^2,
\]
the two quadratic vertical gradient terms cancel. Thus
\[
\boxed{\Ric_V=K_tG_t+\frac{t\mu f}{2}G_tA.}
\]
Since \(\tr A^2=|Q|^2\),
\[
\boxed{\Ric_H=K_2g_2-N_t,\qquad
N_t=\frac{t^2}{4}|Q|^2\,df\otimes df.}
\]
The mixed Ricci block has no linear term: that term is proportional to
\(df\,\div Q\), which vanishes. It is \(O(t^2)\), so its squared norm does not contribute to \(P_2\).

Put
\[
n_t=\tr_{g_2}N_t=\frac{t^2}{4}|Q|^2|df|^2.
\]
Then
\[
s_t=2K_t+2K_2-n_t,
\]
and expansion of \(|\Ric|^2-s_t^2/4\) yields
\[
|\Ric^\circ|^2
=(K_t-K_2)^2
+\frac{t^2\mu^2f^2}{4}|Q|^2
+(K_t-K_2)n_t+O(t^3).
\tag{1}
\]

For the surface family
\[
\widehat g_\varepsilon=g_1e^{\varepsilon A},
\]
the first curvature variation vanishes:
\[
2K'_0
=\div\div Q-\Delta^{\mathrm{tr}}\tr Q-\langle K_1g_1,Q\rangle=0.
\]
Write
\[
K(\widehat g_\varepsilon)
=K_1+\varepsilon^2\kappa_2(Q)+O(\varepsilon^3).
\]
Thus \(K_t=K_1+t^2f^2\kappa_2(Q)+O(t^3)\). Its quadratic contribution in (1) integrates to zero, because the surface area form is fixed and Gauss–Bonnet gives
\[
\int_{\Sigma_1}\kappa_2(Q)\,dA_1=0.
\tag{2}
\]

Using (1)–(2), fixed volume, and
\(\int_{\Sigma_2}|df|^2=\mu\int_{\Sigma_2}f^2\), we obtain
\[
\begin{aligned}
P_2
&=\frac14\int_M
\left[\mu^2f^2|Q|^2
+(K_1-K_2)|df|^2|Q|^2\right]dV\\
&=\frac{\mu}{4}\bigl[\mu+K_1-K_2\bigr]\|fQ\|_2^2.
\end{aligned}
\]
This derivation is independent of the almost-Kähler ledger and its torsion normalization.

## 3. The linearized Ricci and primitive Ricci form claims are correct

A real holomorphic quadratic differential on the constant-curvature first factor satisfies
\[
\tr Q=0,\qquad \delta Q=0,\qquad
\nabla^*\nabla Q=-2K_1Q.
\]
Therefore \(k=fQ\) is TT and \(s'(k)=0\). In Bianchi gauge,
\[
(D\Ric)k
=\frac12\left(
\nabla^*\nabla k+\Ric\circ k+k\circ\Ric-2\mathring Rk
\right)
=\left(K_1+\frac\mu2\right)k.
\]
The \(K_1k\) term is the variation of the moving \(J_t\)-invariant tensor \(K_1G_t\). Hence
\[
\boxed{\Ric''_1=\frac\mu2k,\qquad
\|\Ric''_1\|_2^2=\frac{\mu^2}{4}\|k\|_2^2.}
\]

Equivalently, the direct vertical formula has invariant part \(K_tG_t\) and anti-invariant part \(t\mu fG_tA/2\). Since \(K'_0=0\), the invariant Ricci form is
\[
K_1\omega_1+K_2\omega_2+O(t^2).
\]
Together with \(s'_0=0\) and fixed \(\omega\), this proves
\[
\boxed{\rho'_{0,1}=0.}
\]

## 4. Connection variation identifies the missing factor two

Use the supplied form convention \(|e^{12}+e^{34}|^2=2\). At a point, choose a product orthonormal frame such that
\[
Q=q\bigl((e^1)^2-(e^2)^2\bigr),\qquad df=c\,e^3.
\]
Thus \(|Q|^2=2q^2\). Applying
\[
2g(C_XY,Z)
=(\nabla_Xk)(Y,Z)+(\nabla_Yk)(X,Z)-(\nabla_Zk)(X,Y)
\]
to \(C=(D\nabla)k\), and using that \(\omega\) itself is fixed, gives
\[
\begin{aligned}
T_{e_1}:=(\nabla\omega)'_{e_1}
&=\frac{qc}{2}(e^{14}+e^{23}),\\
T_{e_2}
&=\frac{qc}{2}(e^{13}-e^{24}),\\
T_{e_3}&=T_{e_4}=0.
\end{aligned}
\tag{3}
\]
Pure first-factor derivatives give no torsion: every oriented surface metric preserves its area form, and that area form remains \(\omega_1\).

With the induced \(T^*\otimes\Lambda^2\) **form norm**, (3) gives
\[
|T|^2=q^2c^2=\frac12|Q|^2|df|^2.
\tag{4}
\]
If instead both antisymmetric indices are summed as unrestricted tensor indices, the norm is twice (4).

Choose
\[
\phi=e^{13}-e^{24},\qquad J\phi=e^{14}+e^{23}.
\]
The standard torsion representation
\[
T=a_1\otimes\phi-Ja_1\otimes J\phi
\]
has, up to the harmless simultaneous frame sign,
\[
a_1=\frac{qc}{2}e^2,\qquad
|a_1|^2=\frac18|Q|^2|df|^2.
\]
Thus, in the normalization compatible with
\(t^-=-(a\wedge Ja)^-\) and \(2\|t^-\|^2=\int u^2\),
\[
u=|a|^2
=\frac14|\nabla\omega|_{\mathrm{form}}^2
=\frac18|\nabla\omega|_{\mathrm{tensor}}^2,
\]
and
\[
\boxed{\int_Mu_2=\frac\mu8\|k\|_2^2.}
\tag{5}
\]

The torsion one-form lies in \(T^*\Sigma_1\). Therefore
\[
(a_1\wedge Ja_1)^-=\frac{|a_1|^2}{2}\eta,
\qquad t_2^-=-\frac{u_2}{2}\eta.
\]
For \(\rho_0=r\eta\), \(r=(K_1-K_2)/2\),
\[
\boxed{
(\rho_0,t_2^-)
=-r\int_Mu_2
=-\frac{(K_1-K_2)\mu}{16}\|k\|_2^2.
}
\tag{6}
\]

The generator combined the unrestricted tensor-norm value
\(|T|^2=|df|^2|Q|^2\) with \(u=|T|^2/4\), which requires the form norm. This doubles both (5) and (6). Inserting the corrected inputs into the supplied identity
\[
F_2=\|\Ric''_1\|_2^2
-4(\rho_0,t_2^-)
+2\|(\rho'_{0,1})^{\perp\mathcal H}\|_2^2
\]
reproduces the direct curvature result exactly.

The same convention distinction applies to the Blair–Ianus energy: for this family,
\[
\left(\int s_t\,dV\right)_2=-\frac\mu4\|k\|_2^2.
\]
It equals \(-E_2/4\) for the unrestricted tensor norm, but \(-E_2/2\) for the form norm. The two conventions cannot be interchanged while retaining the same coefficient.

## 5. Precisely what the local scripts retain

The three supplied JSON outputs have the common form
\[
R_n
=\frac14\left[
\mu^2+(K_1-K_2)\mu+c_nK_1(K_1-K_2)
\right],
\qquad c_n=6,16,30.
\]
The first two terms are exactly the corrected integrated answer. The last term is the local intrinsic-curvature term from (1):
\[
2(K_1-K_2)\frac{\kappa_2(Q)}{|Q|^2}.
\]
For the sampled jets \(q=z^n\) at \(z=i\), the outputs imply
\[
\frac{\kappa_2(Q)}{|Q|^2}
=\frac{(n+1)(n+3)}4K_1.
\]

This extra density is a **curvature-transgression divergence**, not an additional global Hessian term. To see this without guessing a pointwise formula, identify the oriented orthonormal frame bundles of \(\widehat g_\varepsilon\) and \(g_1\) using \(e^{-\varepsilon A/2}\). Their \(SO(2)\) connections differ by a globally defined one-form \(b_\varepsilon\). Their Euler curvature forms consequently differ by
\[
(K(\widehat g_\varepsilon)-K_1)dA_1=db_\varepsilon
\]
with a consistent curvature sign convention. Taking the quadratic coefficient gives
\[
\kappa_2(Q)dA_1=db_2.
\]
Its integral vanishes on a closed surface. Expressing this transgression in derivatives of \(Q\) and integrating by parts yields the equivalent Bochner cancellation using
\(\nabla^*\nabla Q=-2K_1Q\).

The local polynomials \(z^n dz^2\) are not compact automorphic quadratic differentials, and sampling one point cannot remove this divergence. Nor is jet-independence required of a pointwise curvature density.

Crucially, the scripts’ difference from the generator is
\[
\frac{K_1-K_2}{4}(c_nK_1-\mu).
\]
Only the \(c_nK_1\) contribution is the divergence. The remaining
\[
-\frac{(K_1-K_2)\mu}{4}
\]
is the genuine integrated factor-two correction.

The file `step68_product_saddle_global_exact.py` does not independently verify the disputed geometry: it explicitly inserts the incorrect twist pairing before performing its algebraic simplification.

## 6. Exact constant-scalar correction preserves the coefficient

Since \(s'_0=0\), the scalar curvature is \(s_t=s_0+O(t^2)\), where
\(s_0=2(K_1+K_2)<0\). For
\[
\widetilde g_t=e^{2v_t}g_t,
\]
the linearized conformal scalar operator at \(g_0\) is
\[
L=6\Delta-2s_0.
\]
It is invertible because \(s_0<0\). The implicit function theorem therefore supplies an exact constant-scalar correction with \(v_t=O(t^2)\), whether one fixes the target scalar value or imposes a compatible normalization.

If
\(\widetilde g_t-g_t=t^2h_2+O(t^3)\), Lemma 67.1 gives
\[
F_2(\widetilde g_t)-F_2(g_t)=DF(g_0)[h_2]=0.
\]
For this particular correction, full criticality is more than necessary: the Weyl energy and \(|c_1^-|^2\) are conformally invariant in dimension four, and \(\int s^2\) is conformally stationary at constant scalar curvature. Thus the coefficient is unchanged independently of the torsion normalization issue.

## 7. Correct saddle criterion

For \(K_1<K_2\),
\[
\boxed{F_2(fQ)<0\quad\Longleftrightarrow\quad
0<\mu<K_2-K_1.}
\]
The swapped mode satisfies
\[
F_2(hQ_2)
=\frac{\lambda}{4}\bigl[\lambda+K_2-K_1\bigr]\|hQ_2\|_2^2.
\]
These are only the specified separated blocks; their nonnegativity does not establish nonnegativity of the full Hessian.

In particular, \(K_1=-2\), \(K_2=-1\), \(\mu=1\) is **quadratically marginal**, not negative. A negative mode requires \(\mu<1\). The low-eigenvalue product construction therefore still supplies genuine constant-scalar sub-tariff directions, but with the halved threshold. Whenever this strict inequality holds, Lemma 67.1 and the ledger give \(c_K<2\); the qualitative conclusion \(c_K>0\) is not contradicted.

The exact verification task is thus closed: the two Ricci first-variation claims are valid, the two torsion coefficients require the stated factor-two correction, and the global saddle formula is valid only in its corrected form.