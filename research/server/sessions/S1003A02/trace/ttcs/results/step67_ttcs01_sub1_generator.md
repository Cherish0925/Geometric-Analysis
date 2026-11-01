# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md"
  ]
}
```

## Task

Theorem 67.K gives c_K > 0 at cscK metrics (zero-free exceptional harmonic form), and Lemma 67.1 shows c_K >= 2 is equivalent to second-order local minimality of LeBrun's functional C_+ - |c1^+|^2_g = p - |c1^-|^2 at the cscK metric on the constant-scalar slice. Design the cheapest decisive computation or argument for the sign of the Hessian of P - 8 pi^2 |c1^-|^2_g at a cscK metric with negative scalar curvature, e.g. Sigma_g x Sigma_h with constant curvatures K1 != K2 < 0 (s = 2K1+2K2), using separation of variables in eigenfunctions of the two factors (Laplace spectra are free parameters lambda, mu >= 0, so the result should be a statement for all spectral parameters), or a structural argument (Weitzenböck/Bochner on Beltrami differentials, Gursky–Viaclovsky-type stability of quadratic functionals, LeBrun's convexity estimates). In the almost-Kähler sector the note gives 8 pi^2 (p-q^2)_2 = s int u_2 + 2||rho*''_1||^2 + 4||W3_1||^2 + 2||(rho0_1)^{perp H}||^2. Say which tensor modes can make it negative, what the low-mode competition is, and whether any explicit low mode (e.g. compatible deformations J_t = J exp(tA) built from a holomorphic quadratic differential or from d f for a first eigenfunction) already decides the sign. Also say what a negative direction would mean for the gap problem (a non-Kähler sub-|c1^-|^2 direction near cscK) and what a positive answer would give (local Kähler tariff). Be concrete: formulas, mode types, what to compute.

## Output

The cheapest computation is to eliminate \(\rho^{*\,\prime\prime}_1\) and \(W_{3,1}\) before separating variables. The almost-Kähler identity from Step 66 linearizes to  
\[
\|\Ric''_1\|_2^2
=
4(\rho_0,t_2^-)
+s\int u_2
+2\|\rho^{*\,\prime\prime}_1\|_2^2
+4\|W_{3,1}\|_2^2,
\qquad
t_2^-=-(a_1\wedge Ja_1)^- .
\]
Hence the Hessian in the question is
\[
\boxed{\;
\mathfrak Q(k):=
8\pi^2(p-q^2)_2(k)
=
\|\Ric''_1\|_2^2
-4(\rho_0,t_2^-)
+2\|(\rho'_{0,1})^{\perp\mathcal H}\|_2^2 .
\;}
\tag{1}
\]
This is much cheaper than separately computing the three curvature components in the original formula: one linearized Ricci tensor, one algebraic twist pairing, and one Hodge projection suffice.

## 1. Product geometry and the only lowering term

Let
\[
(M,g,J,\omega)=
(\Sigma_1,g_1,J_1,\omega_1)\times
(\Sigma_2,g_2,J_2,\omega_2),
\qquad K_1,K_2<0,
\]
with \(K_1\ne K_2\). Put
\[
\eta=\omega_1-\omega_2,\qquad
r=\frac{K_1-K_2}{2}.
\]
Then
\[
s=2(K_1+K_2),\qquad
\rho_0=r\eta,\qquad |\eta|^2=2,
\]
and the harmonic representative of \(c_1^-\) is zero-free.

Split the first torsion one-form as
\[
a_1=a_1^{(1)}+a_1^{(2)},\qquad
a_1^{(i)}\in T^*\Sigma_i .
\]
Since
\[
(\eta,t_2^-)
=
-\|a_1^{(1)}\|_2^2+\|a_1^{(2)}\|_2^2,
\]
formula (1) becomes
\[
\boxed{\;
\mathfrak Q(k)
=
\|\Ric''_1\|_2^2
+4r\bigl(\|a_1^{(1)}\|_2^2-\|a_1^{(2)}\|_2^2\bigr)
+2\|(\rho'_{0,1})^{\perp\mathcal H}\|_2^2 .
\;}
\tag{2}
\]

Thus every square is favorable. The only lowering mechanism is torsion concentrated in:

- \(T^*\Sigma_1\) when \(K_1<K_2\);
- \(T^*\Sigma_2\) when \(K_2<K_1\).

This immediately identifies the dangerous tensor modes.

## 2. A completely explicit separated mode

Take a real holomorphic quadratic differential on \(\Sigma_1\), viewed as a tracefree Codazzi tensor
\[
Q\in\Gamma(S_0^2T^*\Sigma_1),\qquad
\delta Q=0,\qquad
\nabla^*\nabla Q=-2K_1Q.
\]
Let
\[
\Delta_2f=\mu f,\qquad \Delta_2=d^*d,\qquad \mu\ge0,
\]
and define the four-dimensional variation
\[
k=fQ
\]
on the \(T\Sigma_1\)-block, with all other blocks zero.

It is already in the desired tangent space:
\[
\tr k=0,\qquad \delta k=0,\qquad
s'(k)=\delta\delta k-\langle\Ric,k\rangle=0.
\]
It is also a fixed-\(\omega\) compatible variation. If \(A=g_1^{-1}Q\), one convenient realization is
\[
g_t|_{T\Sigma_1}=g_1(e^{tfA}\,\cdot,\cdot),\qquad
J_t|_{T\Sigma_1}=e^{-tfA}J_1,
\]
with \(g_2,J_2\) unchanged. Then \(\omega_1+\omega_2\) is fixed.

### Linearized Ricci tensor

The Bianchi-gauge Ricci formula gives
\[
(D\Ric)k
=
\frac12\bigl(
\nabla^*\nabla k+\Ric\circ k+k\circ\Ric-2\mathring Rk
\bigr).
\]
Using
\[
\nabla^*\nabla k=(\mu-2K_1)k,\qquad
\mathring Rk=-K_1k,
\]
one obtains
\[
(D\Ric)k=\left(K_1+\frac{\mu}{2}\right)k.
\]
The \(K_1k\) part is exactly the variation of the \(J_t\)-invariant tensor \(K_1g_{1,t}\). Therefore
\[
\boxed{\quad \Ric''_1=\frac{\mu}{2}k,\qquad
\|\Ric''_1\|_2^2=\frac{\mu^2}{4}\|k\|_2^2. \quad}
\tag{3}
\]

The primitive \(J_t\)-invariant Ricci form is stationary:
\[
\rho'_{0,1}=0.
\tag{4}
\]

### Torsion

A direct connection variation gives
\[
|(\nabla\omega)_1|^2=|df|^2|Q|^2.
\]
Since \(u=|\nabla\omega|^2/4\),
\[
\int u_2
=
\frac14\int |df|^2|Q|^2
=
\frac{\mu}{4}\|k\|_2^2.
\tag{5}
\]
The associated AAD torsion one-form is supported in \(T^*\Sigma_1\). Consequently
\[
(\rho_0,t_2^-)
=
-r\int u_2
=
-\frac{r\mu}{4}\|k\|_2^2.
\tag{6}
\]

Substitution into (1) yields the exact separated eigenvalue:
\[
\boxed{\;
\mathfrak Q(fQ)
=
\frac{\mu}{4}\bigl[\mu+2(K_1-K_2)\bigr]\|fQ\|_2^2 .
\;}
\tag{7}
\]

Interchanging the two factors gives, for a holomorphic quadratic differential \(Q_2\) on \(\Sigma_2\) and \(\Delta_1h=\lambda h\),
\[
\boxed{\;
\mathfrak Q(hQ_2)
=
\frac{\lambda}{4}\bigl[\lambda+2(K_2-K_1)\bigr]\|hQ_2\|_2^2 .
\;}
\tag{8}
\]

These formulas hold for every spectral parameter \(\lambda,\mu\ge0\).

## 3. The low-mode answer

Suppose \(K_1<K_2\), so the first factor has larger curvature magnitude. Formula (7) gives
\[
\mathfrak Q(fQ)<0
\quad\Longleftrightarrow\quad
0<\mu<2(K_2-K_1).
\tag{9}
\]
Similarly, if \(K_2<K_1\), then
\[
\mathfrak Q(hQ_2)<0
\quad\Longleftrightarrow\quad
0<\lambda<2(K_1-K_2).
\tag{10}
\]

Thus a necessary spectral condition for local Kähler minimality is
\[
\begin{cases}
\lambda_1(\Sigma_2)\ge 2(K_2-K_1),&K_1<K_2,\\[2mm]
\lambda_1(\Sigma_1)\ge 2(K_1-K_2),&K_2<K_1.
\end{cases}
\tag{11}
\]

This already gives explicit products where the Hessian has a downward direction. For example, take
\[
K_1=-2,\qquad K_2=-1.
\]
Choose \(\Sigma_2\) with \(\lambda_1(\Sigma_2)<2\), obtainable by pinching a separating geodesic, and take any nonzero holomorphic quadratic differential \(Q\) on \(\Sigma_1\). Then
\[
\mathfrak Q(f_1Q)=\frac{\lambda_1}{4}(\lambda_1-2)\|f_1Q\|_2^2<0.
\]

This shows that \(c_K\ge2\) is not universal even among zero-free product examples.

### What the familiar modes do

- A holomorphic quadratic differential by itself corresponds to \(\mu=0\) or \(\lambda=0\). Equations (7)–(8) then give zero. These are tangent to genuine product cscK Teichmüller families.
- A Hamiltonian deformation generated by \(df\) is a symplectic-diffeomorphism mode and also gives zero.
- The decisive mode is a holomorphic quadratic differential on one factor whose amplitude is a low scalar eigenfunction on the other factor. Its torsion is proportional to \(df\). The Ricci square costs \(O(\mu^2)\), while the exceptional twist term contributes \(O((K_1-K_2)\mu)\); the latter wins for sufficiently small \(\mu\).

## 4. Why this is a genuine constant-scalar direction

The displayed family is constant-scalar to first order because \(s'(k)=0\). Its scalar curvature can be made exactly constant by an \(O(t^2)\) conformal correction. On mean-zero conformal factors the relevant linear operator is
\[
6\Delta-2s,
\]
which is invertible since \(s<0\). Because the first derivative of
\[
P-8\pi^2|c_1^-|^2
\]
vanishes at the cscK metric, an \(O(t^2)\) correction does not change the quadratic coefficient (7) or (8).

## 5. Cheapest completion for a fixed product

If the first eigenvalue lies above the threshold in (11), the remaining separated blocks can be handled without computing \(W_3\) or \(\rho^{*\,\prime\prime}\). Decompose compatible anti-Hermitian tensors into:

1. \(Q_1f_\mu\) and \(f_\lambda Q_2\): the \(1\times1\) blocks already evaluated.
2. Scalar-derived tensors
   \[
   (\nabla_i^2 f)_0
   \]
   together with the anti-linear mixed tensors formed from \(df_\lambda\) and \(dg_\mu\).
3. Mixed tensors formed from exact, coexact, or harmonic one-forms on the two factors.
4. Kähler and diffeomorphism zero modes.

After imposing \(\delta k=0\) and \(s'(k)=0\), each \((\lambda,\mu)\)-sector is a small real symmetric matrix. Every entry reduces using
\[
\|df\|_2^2=\lambda\|f\|_2^2,
\]
\[
\|(\nabla^2f)_0\|_2^2
=
\frac12\lambda(\lambda-2K_i)\|f\|_2^2,
\]
\[
\nabla^*\nabla Q=-2K_iQ,
\qquad
\nabla^*\nabla\alpha=(\nu-K_i)\alpha
\quad\text{when}\quad
\Delta_H\alpha=\nu\alpha.
\]
Insertion into (2) produces polynomial matrices in
\[
\lambda,\mu,K_1,K_2.
\]
Their principal part grows like \((\lambda+\mu)^2\), whereas the lowering twist term grows only like
\[
|K_1-K_2|(\lambda+\mu).
\]
Thus only low spectral parameters can affect the sign. The twisted-Teichmüller blocks are especially efficient because their Ricci square vanishes quadratically as \(\mu\to0\), while their twist contribution vanishes only linearly.

## 6. Meaning for \(c_K\) and the Einstein-gap problem

For the mode above,
\[
\mathfrak Q=\ell_2-2q^2d_2.
\]
If (9) or (10) holds, then automatically
\[
d_2>0,\qquad
\frac{\ell_2}{q^2d_2}<2,
\qquad
c_K<2.
\]
The nearby constant-scalar metrics satisfy
\[
P(g_t)<8\pi^2|c_1^-|_{g_t}^2
\]
for small \(t\ne0\). This is a genuine non-Kähler sub-\(|c_1^-|^2\) branch near the cscK endpoint, though it is not an aligned \(L=0\) branch; Theorem 67.K still gives \(c_K>0\).

Conversely, if every separated block is \(\ge0\), with kernel consisting only of cscK moduli and diffeomorphisms, then
\[
c_K\ge2.
\]
A uniform transverse lower bound gives the local Kähler tariff
\[
L\ge 2q^2\delta+O(\|g-g_0\|^3),
\qquad
p\ge q^2+O(\|g-g_0\|^3),
\]
and a strict spectral margin yields a corresponding quadratic excess away from the cscK family.