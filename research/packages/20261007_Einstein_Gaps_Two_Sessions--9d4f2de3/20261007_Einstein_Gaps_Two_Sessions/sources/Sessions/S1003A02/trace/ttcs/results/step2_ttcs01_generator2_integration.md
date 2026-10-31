# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 2,
  "task_field": "generator",
  "task_index": 2,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub3_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub4_generator.md"
    }
  ]
}
```

## Exact Task

Goal: decide O10, whether the zero-Weyl endpoint lower bound for the four-manifold Einstein gap holds without the Euler-density bound chi/A <= B. The extract (lines of the inherited manuscript) shows the remaining escape is radial capacity concentration of the bounded negative-spinor resolvent v (|v|^2 = m -> m_* = 128/81, (nabla^* nabla - 2)v -> 0, avg |nabla v|^2 -> 2 m_*), with first jet b = d theta_1 + c theta_2, d = -(m_3 + i m_4)/(2m), and the polynomial one-form B = v wedge nabla v in Omega^1(L^3) whose Weitzenbock potential has eigenvalue -3 radially and +1 horizontally. Scalar torus models realize nonzero capacity measure mu, so only the full coupled system (Dirac equation, type projection, determinant-curvature fit, negative spin connection with unbounded W^-, coupled Cartan equations) can forbid a zero-cost tangent. Task: write down the full rescaled tangent system at a radial-energy concentration scale as precisely as the extract allows, and then try to construct explicit radially symmetric or cylindrical (R x S^3, R^2 x T^2, or warped) solutions of that FULL system with nonzero radial mass and zero compatibility cost — or show the ansatz is obstructed, identifying which identity of the coupled system forces the obstruction (this identity is what a general Liouville theorem must use). State clearly which quantities are scale invariant, which fields keep finite energy, and whether the negative spin connection may bubble (instanton-like) and carry the capacity. Distinguish rigorously derived steps from conjectural ones; give the cheapest symbolic or numerical computation that would settle the ansatz.

## Integrated Scientific Memo

## O10 memo: the full concentration tangent, an explicit ALF solution, and the remaining obstruction

### 1. Status of the density-free endpoint

The available identities do **not** prove the zero-Weyl endpoint lower bound without the Euler-density hypothesis \(\chi/A\le B\). More importantly, the natural leading-order Liouville statement one might try to prove is false:

> There exist complete, bounded, finite-energy, nonconstant solutions of the full leading rescaled geometric system with nonzero radial mass.

A one-centre Taub–NUT space supplies such a solution. Its uncontrolled negative-spin connection bubbles in an instanton-like fashion and supports the radial capacity well. Thus a density-free proof cannot rely only on classifying leading Ricci-flat tangents as trivial. It must use information lost in the leading blow-up: the order-\(r^2\) monopole/determinant-curvature terms, global charge and multiplicity, or the cost of matching an ALF end to the exterior geometry.

This is a local tangent result, not an O10 counterexample: no closed actual monopole sequence or zero-cost global gluing has been constructed.

---

## 2. Scaling ledger and the rescaled actual equations

Let \(x_j\) be a radial concentration point, \(r_j\downarrow0\), and pull back the fields to a pointed region while setting
\[
h_j=r_j^{-2}g_j.
\]
Use the canonical identification of spinor bundles under constant metric rescaling and retain the pointwise amplitudes of \(\Phi_j\) and \(v_j\).

For the positive spinor,
\[
\begin{aligned}
D^+_{\mathcal A_j,h_j}\Phi_j&=0,\\
F_{\mathcal A_j}^{+,h_j}
 &=2i\,r_j^2\sigma_{h_j}(\Phi_j),\\
\nabla_{\mathcal A_j,h_j}^*\nabla_{\mathcal A_j,h_j}\Phi_j
 &=r_j^2(1-\rho_j/2)\Phi_j,\\
s_{h_j}&=-4r_j^2.
\end{aligned}
\tag{2.1}
\]

For the bounded negative-spinor resolvent, write
\[
e_j=(\nabla_{g_j}^*\nabla_{g_j}-2)v_j.
\]
Then
\[
\begin{aligned}
\nabla_{h_j}^*\nabla_{h_j}v_j
 &=2r_j^2v_j+r_j^2e_j,\\
D^-_{3\mathcal A_j,h_j}v_j
 &=r_jD^-_{3\mathcal A_j,g_j}v_j,\\
N_{h_j}v_j&=r_jN_{g_j}v_j,
\end{aligned}
\tag{2.2}
\]
and, with \(m_j=|v_j|^2\),
\[
\Delta_{h_j}m_j
 =4r_j^2m_j-2|\nabla_{h_j}v_j|^2
 +2r_j^2\operatorname{Re}\langle e_j,v_j\rangle .
\tag{2.3}
\]

The actual torsion origin must also be retained. Since the cubic torsion is first order,
\[
t_{h_j}(\Phi_j)=r_j\,t_{g_j}(\Phi_j),
\]
so the informative rescaled relation is
\[
v_j-r_j^{-1}t_{h_j}(\Phi_j)\longrightarrow0,
\tag{2.4}
\]
not merely \(r_jv_j-t_{h_j}(\Phi_j)\to0\), which loses the first-order content.

### Scaling of the relevant energies

Under \(h=r^{-2}g\),
\[
\begin{array}{c|c}
\text{quantity} & \text{rescaled integral}\\ \hline
\int|\nabla v|^2 & r^{-2}\int|\nabla_gv|^2\\[2mm]
\int|dm|^2 & r^{-2}\int|d_gm|^2\\[2mm]
\int|\nabla v|^4 & \text{invariant}\\
\int|\nabla^2v|^2 & \text{invariant}\\
\int|F|^2,\ \int|\mathrm{Rm}|^2 & \text{invariant}\\
\int|\nabla_h^*\nabla_hv-2r^2v|^2 & \int|e|^2 .
\end{array}
\tag{2.5}
\]

Thus curvature action is scale invariant in four dimensions, whereas the Dirichlet/capacity energy of a bounded field has length-squared scaling. A physical core of size \(r\) carries \(O(r^2)\) radial energy but \(O(1)\) curvature action.

The \(-3,+1\) potential eigenvalues of the unrescaled \(L^3\)-valued one-form Weitzenböck operator arise from curvature and Ricci normalized at the ambient scale. At concentration scale they become
\[
-3r_j^2,\qquad +r_j^2,
\tag{2.6}
\]
and disappear from the leading tangent. Therefore the negative radial potential in the manuscript does not itself obstruct a small-scale bubble.

A caveat is essential: normalized global \(L^2\)-smallness does not automatically imply local smallness after blow-up. For example,
\[
\int_{U_j}|N_{h_j}v_j|^2\,dV_{h_j}
 =r_j^{-2}\int_{U_j}|N_{g_j}v_j|^2\,dV_{g_j}.
\tag{2.7}
\]
A good-scale selection must force the right side to vanish, and analogous conditions are needed for the Dirac, Ricci, \(W^+\), determinant-curvature, and torsion-transfer errors. The tangent system below is rigorously the conditional smooth limit once those local rescaled errors vanish; existence of such a smooth tangent is not supplied by the averaged estimates alone.

---

## 3. Full leading tangent system

Assume pointed smooth convergence at a good concentration scale and local disappearance of all controlled errors. The limiting system is
\[
\boxed{
\begin{gathered}
\operatorname{Ric}_h=0,\qquad W_h^+=0,\qquad F_{\mathcal A}=0,\\
\nabla_{\mathcal A}\Phi_0=0,\qquad
|\Phi_0|^2=\rho_*=\frac43,\\
v\in\Gamma(S_h^-\otimes L),\qquad |v|\le C,\\
D^-_{3\mathcal A}v=0,\qquad
\mathsf P_{J_+}\nabla v=0,\qquad
\nabla^*\nabla v=0.
\end{gathered}}
\tag{3.1}
\]
Here \(J_+\) is the parallel complex structure selected by \(\Phi_0\). The determinant connection is locally flat. The negative spin connection need not be flat: its curvature is precisely the uncontrolled opposite-chiral curvature.

The limiting amplitude obeys
\[
\Delta m=-2|\nabla v|^2.
\tag{3.2}
\]
The global normalized convergence \(m_j\to m_*\) does not imply \(m\equiv m_*\) on the tangent, because the concentration core has vanishing relative volume. The natural matching condition is only
\[
m\longrightarrow m_* 
\quad\text{along the relevant end},
\tag{3.3}
\]
if the blow-up admits such an exterior-matching end.

### Adapted-frame form

On \(m>0\), write
\[
u=\frac{dm}{2m},\qquad z=u_1-iu_2,
\]
\[
q=(u_2,-u_1,u_4,-u_3),\qquad
\mathfrak d=-(u_3+iu_4),
\]
and
\[
b=\mathfrak d\,\theta_1+c\,\theta_2.
\tag{3.4}
\]
The notation \(\mathfrak d\) avoids confusion with exterior differentiation. In a local flat determinant gauge, the \(S^-\otimes L\) connection is
\[
\Gamma=
\begin{pmatrix}
iq&-\bar b\\
b&-iq
\end{pmatrix}.
\tag{3.5}
\]

Because this connection must be an actual negative spin connection of a torsion-free metric, one must impose both curvature equations
\[
\boxed{
(db-2iq\wedge b)^+=0,\qquad
(i\,dq-\bar b\wedge b)^+=0.
}
\tag{3.6}
\]
The second, diagonal equation is absent from a scalar amplitude model and is indispensable in testing an explicit ansatz.

The tangent Cartan equations are
\[
\begin{aligned}
d\theta_1&=iq\wedge\theta_1-\mathfrak d\,\overline{\Xi_+},\\
d\theta_2&=-iq\wedge\theta_2-\bar c\,\Xi_-
                  -2i\bar{\mathfrak d}\,e^{12},
\end{aligned}
\tag{3.7}
\]
together with their conjugates. They encode the torsion-free realization of \(q,\mathfrak d,c\); these fields cannot be prescribed independently.

The off-diagonal curvature equation becomes
\[
\begin{aligned}
0={}&
\mathcal L_1(d\mathfrak d-iq\,\mathfrak d)
+\mathcal L_2(dc-3iq\,c)\\
&-\mathfrak d^2\overline{\Xi_+}
-i c\bar{\mathfrak d}\,\Psi_1.
\end{aligned}
\tag{3.8}
\]
Thus the fifth-line coefficient \(c\) remains coupled to the radial coefficient \(\mathfrak d\); the finite-density reduction to a \(c\)-only equation is illegal here.

For the global polynomial one-form
\[
\mathcal B=v\wedge\nabla v\in\Omega^1(L^3),
\tag{3.9}
\]
the exact leading equations are
\[
\boxed{
\delta\mathcal B=0,\qquad
d^+\mathcal B
 =2m(\mathfrak d^2+c\bar z)\overline{\Xi_+}.
}
\tag{3.10}
\]
For a sufficiently decaying complete solution, integration gives the curvature-free identity
\[
\int|\nabla\mathcal B|^2
 =2\int|d^+\mathcal B|^2.
\tag{3.11}
\]
Neither side is forced to vanish. In particular, the quadratic source in (3.10) cannot be discarded as a lower-order error.

The first-jet energy is
\[
|\nabla v|^2
 =\frac{E_1+2E_2}{2m}+2m|c|^2,
\qquad
E_1=m_1^2+m_2^2,\quad E_2=m_3^2+m_4^2.
\tag{3.12}
\]

Equations (3.1) and (3.4)–(3.12) are the full leading tangent system supported by the extract. They include the Dirac equation, type projection, flat leading determinant connection, both curvature equations, and torsion-free Cartan realization.

---

## 4. Explicit nontrivial solution: one-centre Taub–NUT

Let
\[
H(x)=1+\frac{\ell}{R},\qquad R=|x|,\qquad \ell>0,
\]
and choose \(\omega\) on \(\mathbb R^3\setminus\{0\}\) satisfying
\[
d\omega=*_{\mathbb R^3}dH.
\]
The Gibbons–Hawking metric
\[
h=H\,dx\cdot dx+H^{-1}(d\psi+\omega)^2,
\qquad \psi\sim\psi+4\pi\ell,
\tag{4.1}
\]
extends smoothly over \(R=0\). Orient it so that its parallel hyperkähler forms are self-dual. Then
\[
\operatorname{Ric}_h=0,\qquad W_h^+=0.
\tag{4.2}
\]

In biaxial form,
\[
h=H\,dR^2+HR^2(\sigma_1^2+\sigma_2^2)
+\ell^2H^{-1}\sigma_3^2.
\tag{4.3}
\]
It is smooth at the nut and ALF at infinity: the Hopf circle has asymptotically finite length, while the transverse directions expand.

Choose one parallel complex structure and a sign convention for which
\[
f=x_1+ix_2
\]
is holomorphic. Let \(L\) be the trivial determinant line with flat connection. Using the Kähler identification
\[
S^-\simeq\Lambda^{0,1},
\]
set
\[
v=\sqrt{\frac{m_*}{2}}\,d\bar f.
\tag{4.4}
\]
Since
\[
|d\bar f|^2=\frac2H,
\]
its amplitude is
\[
\boxed{
m=|v|^2=\frac{m_*}{H}
=m_*\frac{R}{R+\ell}.
}
\tag{4.5}
\]
Thus \(m\) has a genuine lower well, vanishes smoothly at the nut, and tends to \(m_*\) at infinity.

### Verification of the full leading system

Because \(f\) is holomorphic on a Kähler manifold,
\[
\nabla^{1,0}(d\bar f)=0,
\tag{4.6}
\]
which is the required type projection. The form \(d\bar f\) is closed, and its \(\bar\partial\)-codifferential vanishes by the same mixed-Hessian identity. Hence
\[
D^-v=\sqrt2(\bar\partial+\bar\partial^*)v=0.
\tag{4.7}
\]
Since the scalar and determinant curvatures vanish, the spinorial Lichnerowicz formula gives
\[
\nabla^*\nabla v=0.
\tag{4.8}
\]

The connection acting on \(v\) is the actual Levi–Civita negative spin connection. Consequently both equations in (3.6) and the Cartan equations (3.7) hold automatically; this is not an independently chosen gauge-field ansatz.

### Exact energies

For a circle-invariant radial function \(a(R)\),
\[
\Delta_{\mathrm{usual},h}a
 =H^{-1}\left(a''+\frac2R a'\right).
\tag{4.9}
\]
Applying this to (4.5), with the manuscript’s positive-Laplacian convention translated through \(\Delta m=-2|\nabla v|^2\), yields
\[
\boxed{
|\nabla v|^2=\frac{m_*\ell^2}{(R+\ell)^4},
\qquad
|dm|^2=\frac{m_*^2\ell^2R}{(R+\ell)^5}.
}
\tag{4.10}
\]
Using \(dV_h=H\,d^3x\,d\psi\),
\[
\boxed{
\int|\nabla v|^2=8\pi^2m_*\ell^2,\qquad
\int|dm|^2=\frac{16\pi^2}{3}m_*^2\ell^2.
}
\tag{4.11}
\]
Both energies are finite and nonzero.

Taub–NUT also has
\[
0<\int|\mathrm{Rm}_h|^2<\infty,
\tag{4.12}
\]
and its nonflat negative spin connection is anti-self-dual Yang–Mills. Hence the uncontrolled \(W^-\) block can indeed bubble in an instanton-like manner and carry radial capacity.

The field is not purely radial as a spinor, though its norm is radial. With an adapted first plane and \(n_3=x_3/R\),
\[
E_1=|dm|^2(1-n_3^2),\qquad E_2=|dm|^2n_3^2.
\tag{4.13}
\]
Since \(|dm|^2/m=|\nabla v|^2\), (3.12) gives
\[
\frac{E_1+2E_2}{2m}
 =\frac{1+n_3^2}{2}|\nabla v|^2,
\qquad
2m|c|^2
 =\frac{1-n_3^2}{2}|\nabla v|^2.
\tag{4.14}
\]
After angular integration, two thirds of the total \(\nabla v\)-energy lies in the radial part and one third in the horizontal part. Thus \(\mathfrak d\neq0\), but \(c\) does not vanish either.

---

## 5. Compatibility with the actual torsion origin

An arbitrary harmonic negative spinor would not yet reflect the original coupled problem. Taub–NUT also passes the first-order torsion-origin test.

Let \(\Phi_0\) be a parallel positive spinor with
\[
|\Phi_0|^2=\rho_*,
\]
and let \(e_2\) be a parallel complementary positive spinor. For a suitable holomorphic/antiholomorphic choice, take
\[
\chi=a\,\bar f\,e_2,\qquad D^+\chi=0.
\tag{5.1}
\]
The linearization of the cubic torsion at \(\Phi_0\) is
\[
Q_{\Phi_0}\chi
 =\sum_i c(e^i)\Phi_0\otimes
 \bigl(\Phi_0\wedge\nabla_{e_i}\chi\bigr).
\tag{5.2}
\]
It is a nonzero constant multiple of the spinor corresponding to \(d\bar f\); choosing \(a\) appropriately gives
\[
Q_{\Phi_0}\chi=v.
\tag{5.3}
\]
Therefore, on each fixed compact set,
\[
\Phi_r=\Phi_0+r\chi+O(r^2)
\quad\Longrightarrow\quad
r^{-1}t_h(\Phi_r)=v+O(r).
\tag{5.4}
\]

This is a formal/local first-order realization of (2.4). It is **not** an exact finite-\(r\) Seiberg–Witten solution: \(\chi\) grows at infinity, and the order-\(r^2\) metric, determinant-connection, and spinor equations remain unsolved.

---

## 6. Obstruction of simpler symmetric ansätze

### 6.1 Round \(S^3\)-warped ansatz

For
\[
h=ds^2+a(s)^2g_{S^3},
\]
Ricci-flatness gives
\[
a''=0,\qquad (a')^2=1.
\tag{6.1}
\]
A smooth complete solution with a centre is Euclidean \(\mathbb R^4\). The determinant and spin connections are flat, so a bounded solution of
\[
\nabla^*\nabla v=0
\]
has componentwise bounded harmonic coefficients and is constant. Hence
\[
dm=0.
\]

The obstructing coupled identity is the **Ricci-flat Cartan equation**: under round symmetry it forces the only smooth complete geometry to be flat, eliminating the spin connection needed to support a radial well.

### 6.2 Flat \(\mathbb R^2\times T^2\)

Fourier decomposition in the torus directions reduces the rough harmonic equation to
\[
(\Delta_{\mathbb R^2}-|k|^2)v_k=0
\tag{6.2}
\]
for the usual-sign Laplacian. A radial nonzero-frequency mode is a combination of \(I_0(|k|R)\) and \(K_0(|k|R)\): the former grows, the latter is singular at the axis. The zero mode is \(A+B\log R\). Smoothness and boundedness leave only constants. Flat line holonomy only shifts the Fourier frequencies.

Here the obstruction is already the **rough harmonic equation plus regularity and boundedness**; no nonflat negative spin connection is available.

### 6.3 ALE hyperkähler ansätze

For a smooth ALE hyperkähler space with trivial flat determinant line, a bounded harmonic negative spinor has an asymptotic constant lying in the invariant subspace of the end group
\[
\Gamma\subset SU(2).
\]
For nontrivial \(\Gamma\), the defining two-dimensional negative-spin representation has no nonzero invariant vector, so the asymptotic constant vanishes. A decaying finite-energy rough-harmonic spinor then vanishes by integration by parts.

If \(\Gamma\) is trivial, Euclidean asymptotic volume ratio and Ricci flatness force the complete smooth metric to be Euclidean by Bishop–Gromov rigidity. Again only constant bounded spinors remain.

A nontrivial flat line character changes the end representation and must be checked separately. Taub–NUT evades this ALE obstruction because its end is ALF and circle-collapsed.

---

## 7. Consequences for the O10 decision

The rigorous conclusion supported by the current analysis is:

\[
\boxed{\text{The full leading coupled tangent system admits a nonzero
radial-capacity solution.}}
\]

Therefore:

1. **The Euler-density hypothesis cannot presently be removed by a leading-order tangent Liouville theorem.**
2. **Negative-spin connection bubbling is a viable carrier of the capacity defect.**
3. **The explicit bubble has exactly the density economics expected of an unrestricted escape.**

Indeed, for a physical copy \(\lambda^2h\) of the Taub–NUT core,
\[
\int|\nabla v|^2\asymp\lambda^2,\qquad
\int|dm|^2\asymp\lambda^2,\qquad
\int|\mathrm{Rm}|^2\asymp1.
\tag{7.1}
\]
If \(N\) such cores provide order-one normalized radial energy, then
\[
\frac{N\lambda^2}{V}\asymp1,
\qquad
\frac1V\int|W^-|^2\asymp\frac NV\asymp\lambda^{-2}.
\tag{7.2}
\]
Thus the required opposite-Weyl density diverges precisely as the core scale shrinks. This is compatible with the fact that every bounded-density interval has a positive endpoint gap.

What remains unknown is whether these local bubbles can be assembled into a closed sequence satisfying the actual monopole supply and with the original normalized compatibility cost tending to zero. Two obstructions may still rule this out:

* **order-\(r^2\) field compatibility:** the leading tangent has \(F_{\mathcal A}=0\), while the actual monopole source and bounded determinant-curvature model first appear at order \(r^2\);
* **ALF end matching:** a Taub–NUT end has an asymptotically finite Hopf circle. Matching it to a noncollapsed exterior, or arranging a globally collapsed exterior, may force a scale-invariant Ricci or field cost.

Accordingly, the exact O10 theorem remains unresolved. The explicit tangent rules out one natural proof strategy but does not prove failure of the endpoint bound.

---

## 8. The identity a successful general obstruction must use

No identity visible in the leading system forces triviality: Taub–NUT satisfies the Dirac equation, type projection, rough-harmonic equation, diagonal and off-diagonal curvature equations, and torsion-free Cartan equations.

Therefore any genuine Liouville/compactness obstruction must use at least one datum beyond (3.1):

1. the **next-order determinant-curvature/monopole equation** after dividing by \(r^2\);
2. the **global characteristic charge** and multiplicity of bubbles;
3. an **end-flux or transgression identity** coupling the ALF circle fibration to the exterior;
4. a quantitative **matching-cost identity** showing that changing the ALF circle scale incurs nonvanishing normalized \(\operatorname{Ric}^{\circ}\)-energy;
5. or an exact second-order identity tying the torsion parent \(\Phi\) to \(v\), stronger than the first-order realization (5.4).

The source’s leading \(\mathcal B\)-Weitzenböck identity cannot serve this role: its \(-3,+1\) potential scales away, and the curvature-free limiting identity (3.11) admits the Taub–NUT solution.

---

## 9. Cheapest decisive computations

The leading Taub–NUT ansatz is settled analytically. Its energies reduce to one-dimensional symbolic integration:
```python
import sympy as s

R, ell, m0 = s.symbols("R ell m0", positive=True)
H = 1 + ell/R
m = m0/H

grad_v_sq = s.simplify(
    (s.diff(m, R, 2) + 2*s.diff(m, R)/R)/(2*H)
)
grad_m_sq = s.simplify(s.diff(m, R)**2/H)

# d^3x contributes 4*pi*R^2 dR and psi has period 4*pi*ell
density = 16*s.pi**2*ell*H*R**2

Ev = s.integrate(density*grad_v_sq, (R, 0, s.oo))
Em = s.integrate(density*grad_m_sq, (R, 0, s.oo))
```
This returns
\[
E_v=8\pi^2m_*\ell^2,\qquad
E_m=\frac{16\pi^2}{3}m_*^2\ell^2.
\]

The cheapest computation that would materially advance the unresolved question is the order-\(r^2\) equivariant completion
\[
\begin{aligned}
h_r&=h+r^2k+\cdots,\\
\mathcal A_r&=r^2a+\cdots,\\
\Phi_r&=\Phi_0+r\chi+r^2\Phi_2+\cdots.
\end{aligned}
\tag{9.1}
\]
Substitution into the Einstein residual, self-dual curvature equation, and Dirac equation produces a linear coupled system for
\[
(k,a,\Phi_2)
\]
with sources quadratic in \(\chi\). In a biaxial Taub–NUT ansatz and an equivariant spinor sector this should reduce to radial ODEs. The decisive output is the solvability condition at the ALF end:

* a decaying/matchable solution with finite transition cost would provide the first credible local building block for an O10 escape;
* a nonzero cokernel pairing or compulsory nondecaying mode would identify the coupled identity needed for a density-free endpoint theorem.

At present, that order-\(r^2\) solvability and the global end-matching cost are the precise unresolved scientific objects.