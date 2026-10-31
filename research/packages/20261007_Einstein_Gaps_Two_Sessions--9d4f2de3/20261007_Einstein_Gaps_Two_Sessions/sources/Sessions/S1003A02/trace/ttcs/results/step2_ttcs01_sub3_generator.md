# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/extracts/O10_unbounded_density_37900_38960.tex",
    "Sessions/S1003A02/workspace/notes/step1_field_compatibility_and_route_portfolio.md",
    "Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex",
    "Skills/geometric-analysis/references/conventions-and-literature.md"
  ]
}
```

## Task

Goal: decide O10, whether the zero-Weyl endpoint lower bound for the four-manifold Einstein gap holds without the Euler-density bound chi/A <= B. The extract (lines of the inherited manuscript) shows the remaining escape is radial capacity concentration of the bounded negative-spinor resolvent v (|v|^2 = m -> m_* = 128/81, (nabla^* nabla - 2)v -> 0, avg |nabla v|^2 -> 2 m_*), with first jet b = d theta_1 + c theta_2, d = -(m_3 + i m_4)/(2m), and the polynomial one-form B = v wedge nabla v in Omega^1(L^3) whose Weitzenbock potential has eigenvalue -3 radially and +1 horizontally. Scalar torus models realize nonzero capacity measure mu, so only the full coupled system (Dirac equation, type projection, determinant-curvature fit, negative spin connection with unbounded W^-, coupled Cartan equations) can forbid a zero-cost tangent. Task: write down the full rescaled tangent system at a radial-energy concentration scale as precisely as the extract allows, and then try to construct explicit radially symmetric or cylindrical (R x S^3, R^2 x T^2, or warped) solutions of that FULL system with nonzero radial mass and zero compatibility cost — or show the ansatz is obstructed, identifying which identity of the coupled system forces the obstruction (this identity is what a general Liouville theorem must use). State clearly which quantities are scale invariant, which fields keep finite energy, and whether the negative spin connection may bubble (instanton-like) and carry the capacity. Distinguish rigorously derived steps from conjectural ones; give the cheapest symbolic or numerical computation that would settle the ansatz.

## Output

## A geometric tangent that survives the coupled equations

There is a substantive candidate beyond the scalar torus model: **a Taub–NUT hyperkähler metric with an opposite-chiral spinor obtained from a holomorphic coordinate**. Its amplitude has a radial lower well, its radial Dirichlet energy is finite and nonzero, and it satisfies the complete geometric equations that survive a small-scale rescaling. The connection supporting it is the actual Levi–Civita spin connection, not an independently prescribed gauge field.

This does not construct an unrestricted O10 sequence. It does show that a Liouville theorem excluding every complete, finite-energy geometric tangent would be false. The distinction between Euclidean-volume-growth tangents and circle-collapsed tangents is therefore mathematically consequential.

### 1. Rescaling the actual equations

Let \(r_j\downarrow0\), and use pointed pullbacks with
\[
h_j=r_j^{-2}g_j.
\]
Identify the spinor bundles by the canonical identification for constant metric rescaling, retaining the amplitudes of \(\Phi_j\) and \(v_j\). Connections remain the same differential operators on the pulled-back bundles; their components in \(h_j\)-orthonormal frames acquire the appropriate powers of \(r_j\).

The actual positive-spinor equations become
\[
\begin{aligned}
D^+_{\mathcal A_j,h_j}\Phi_j&=0,\\
F_{\mathcal A_j}^{+,h_j}
 &=2i\,r_j^2\sigma_{h_j}(\Phi_j),\\
\nabla_{\mathcal A_j,h_j}^*\nabla_{\mathcal A_j,h_j}\Phi_j
 &=r_j^2(1-\rho_j/2)\Phi_j,\\
s_{h_j}&=-4r_j^2.
\end{aligned}
\tag{1}
\]
Here \(\sigma_{h_j}\) uses the quadratic spinor map normalized with respect to \(h_j\).

For the bounded opposite-chiral section, writing
\[
e_j=(\mathcal L_{g_j}-2)v_j,
\]
one has
\[
\begin{aligned}
\mathcal L_{h_j}v_j&=2r_j^2v_j+r_j^2e_j,\\
D^-_{3\mathcal A_j,h_j}v_j
 &=r_jD^-_{3\mathcal A_j,g_j}v_j,\\
N_{h_j}v_j&=r_jN_{g_j}v_j.
\end{aligned}
\tag{2}
\]
Consequently,
\[
\Delta_{h_j}m_j
 =4r_j^2m_j-2|\nabla_{h_j}v_j|^2
   +2r_j^2\operatorname{Re}\langle e_j,v_j\rangle.
\tag{3}
\]

The actual origin of \(v_j\) must also be retained. The cubic torsion satisfies
\[
t_{h_j}(\Phi_j)=r_jt_{g_j}(\Phi_j).
\]
Thus the informative relation is
\[
v_j-r_j^{-1}t_{h_j}(\Phi_j)\longrightarrow0
\tag{4}
\]
in whatever local rescaled topology can be obtained. Merely retaining
\(r_jv_j-t_{h_j}(\Phi_j)\to0\) loses the first-order origin of \(v_j\).

The relevant scaling is:

| Quantity | Integral under \(h=r^{-2}g\) |
|---|---:|
| \(\displaystyle\int|\nabla v|^2\) | \(r^{-2}\displaystyle\int|\nabla_gv|^2\) |
| \(\displaystyle\int|dm|^2\) | \(r^{-2}\displaystyle\int|d_gm|^2\) |
| \(\displaystyle\int|\nabla v|^4\) | unchanged |
| \(\displaystyle\int|\nabla^2v|^2\) | unchanged |
| \(\displaystyle\int|F|^2,\ \int|\mathrm{Rm}|^2\) | unchanged |
| \(\displaystyle\int|\mathcal L_hv-2r^2v|^2\) | \(\displaystyle\int|e|^2\) |

In particular, the capacity energy of a bounded field is **not** scale invariant in dimension four: a geometrically similar core of radius \(r\) carries energy of order \(r^2\). Curvature action is scale invariant.

This also explains why the original potential eigenvalues do not persist at a small-scale tangent. The eigenvalues \(-3,+1\) of the \(L^3\)-valued one-form operator become
\[
-3r_j^2,\qquad r_j^2.
\tag{5}
\]
At leading order both vanish.

There is an important analytical qualification to the passage from (1)–(4) to a smooth tangent. The supplied averaged estimates do not by themselves produce pointed metric compactness, nor do they make every rescaled local error small. For example, on a pulled-back region \(U_j\),
\[
\int_{U_j}|N_{h_j}v_j|^2\,dV_{h_j}
 =r_j^{-2}\int_{U_j}|N_{g_j}v_j|^2\,dV_{g_j}.
\]
A geometric tangent retaining the type equation requires this expression to tend to zero. Analogous local estimates are needed for the Dirac and torsion-transfer errors. Uncontrolled opposite-chiral curvature can prevent convergence to a smooth connection even when all controlled curvature blocks disappear.

The equations below describe a **smooth zero-cost geometric tangent**, conditional on obtaining such local convergence.

### 2. The complete leading geometric system

If the controlled curvature errors vanish locally in scale-invariant \(L^2\), the bounded determinant-curvature model disappears under rescaling. The resulting system is
\[
\boxed{
\begin{gathered}
\operatorname{Ric}_h=0,\qquad W_h^+=0,\qquad F_{\mathcal A}=0,\\
\nabla_{\mathcal A}\Phi_0=0,\qquad |\Phi_0|^2=\rho_*=\frac43,\\
v\in\Gamma(S_h^-\otimes L),\qquad |v|\le C,\\
D^-_{3\mathcal A}v=0,\qquad
\mathsf P_{J_+}\nabla v=0,\qquad
\nabla^*\nabla v=0.
\end{gathered}}
\tag{6}
\]
The almost-complex structure \(J_+\) selected by \(\Phi_0\) is now parallel. Locally the metric is hyperkähler, oriented so that its parallel Kähler forms are self-dual. The determinant connection is flat, but the opposite-chiral spin connection can have nonzero anti-self-dual curvature.

The amplitude equation is
\[
\Delta m=-2|\nabla v|^2.
\tag{7}
\]
The original convergence \(m_j\to m_*\) in normalized measure does **not** require \(m\equiv m_*\) on a concentration tangent. A core with vanishing relative volume can retain a full amplitude profile. Matching \(m\to m_*\) at an end is a natural additional condition, not an immediate consequence of the averaged convergence.

Here is the adapted-frame form of (6), retaining both radial and horizontal variables. Write the radial coefficient as \(\mathfrak d\), to distinguish it from the exterior derivative:
\[
\begin{aligned}
u&=\frac{dm}{2m},\qquad z=u_1-iu_2,\\
q&=(u_2,-u_1,u_4,-u_3),\\
\mathfrak d&=-(u_3+iu_4),\qquad
b=\mathfrak d\,\theta_1+c\,\theta_2.
\end{aligned}
\tag{8}
\]
In a local flat determinant gauge, the connection on \(S^-\otimes L\) is
\[
\Gamma=
\begin{pmatrix}
iq&-\bar b\\
b&-iq
\end{pmatrix}.
\tag{9}
\]
Its entire curvature matrix, not only its off-diagonal entry, must be anti-self-dual:
\[
\boxed{
(db-2iq\wedge b)^+=0,\qquad
(i\,dq-\bar b\wedge b)^+=0.
}
\tag{10}
\]
The second equation is the diagonal curvature equation. It is indispensable when testing an explicit connection ansatz.

The extract’s coframe equations reduce to
\[
\begin{aligned}
d\theta_1&=iq\wedge\theta_1-\mathfrak d\,\overline{\Xi_+},\\
d\theta_2&=-iq\wedge\theta_2-\bar c\,\Xi_-
                    -2i\bar{\mathfrak d}\,e^{12}.
\end{aligned}
\tag{11}
\]
Together with their conjugates, these encode the torsion-free Levi–Civita realization. The off-diagonal equation in (10) becomes
\[
\begin{aligned}
0={}&
\mathcal L_1(d\mathfrak d-iq\,\mathfrak d)
+\mathcal L_2(dc-3iq\,c)\\
&-\mathfrak d^2\overline{\Xi_+}
-i c\bar{\mathfrak d}\,\Psi_1.
\end{aligned}
\tag{12}
\]
Thus \(c\) cannot be isolated from the radial variables even at the tangent level.

The global polynomial object remains
\[
\mathcal B=v\wedge\nabla v,
\]
and satisfies
\[
\boxed{
\delta\mathcal B=0,\qquad
d^+\mathcal B
 =2m(\mathfrak d^2+c\bar z)\overline{\Xi_+}.
}
\tag{13}
\]
For sufficiently decaying finite-energy fields, its integrated identity is
\[
\int|\nabla\mathcal B|^2
 =2\int|d^+\mathcal B|^2.
\tag{14}
\]
Neither side is required to vanish. The quadratic term in (13) is part of the full system, not an error.

Finally,
\[
|\nabla v|^2
 =\frac{E_1+2E_2}{2m}+2m|c|^2,
\qquad
E_1=m_1^2+m_2^2,\quad E_2=m_3^2+m_4^2.
\tag{15}
\]
Equations (8)–(15) exhibit precisely where the scalar model acquires geometric content: \(q,b\) must come from an actual torsion-free metric connection, and both curvature entries in (10) must hold.

### 3. An explicit warped solution: Taub–NUT

Let
\[
H(x)=1+\frac{\ell}{R},\qquad R=|x|,\qquad \ell>0,
\]
and choose \(\omega\) on \(\mathbb R^3\setminus\{0\}\) with
\[
d\omega=*_{\mathbb R^3}dH.
\]
The Gibbons–Hawking metric is
\[
h=H\,dx\cdot dx+H^{-1}(d\psi+\omega)^2,
\qquad \psi\sim\psi+4\pi\ell.
\tag{16}
\]
It extends smoothly across the nut at \(R=0\). Orient it so that its parallel hyperkähler forms are self-dual. Then
\[
\operatorname{Ric}_h=0,\qquad W_h^+=0.
\]

In biaxial \(S^3\) coordinates this is
\[
h=H\,dR^2
 +HR^2(\sigma_1^2+\sigma_2^2)
 +\ell^2H^{-1}\sigma_3^2,
\tag{17}
\]
with the Hopf angle of period \(4\pi\). Near the nut,
\[
s=2\sqrt{\ell R}+O(R^{3/2}),
\]
and (17) approaches
\[
ds^2+\frac{s^2}{4}
(\sigma_1^2+\sigma_2^2+\sigma_3^2).
\]
At infinity the Hopf circle has finite length while the two transverse sphere directions grow. Thus the metric is asymptotically locally flat with cubic volume growth.

For one parallel complex structure, a suitable choice of sign makes
\[
f=x_1+ix_2
\]
holomorphic. Take the determinant line trivial with its flat connection. Under the parallel Kähler spinor identification
\[
S^-\simeq\Lambda^{0,1},
\]
define
\[
v=\sqrt{\frac{m_*}{2}}\,d\bar f.
\tag{18}
\]
The identification here is unitary. Since
\[
|d\bar f|^2=\frac2H,
\]
the amplitude is
\[
\boxed{
m=|v|^2=\frac{m_*}{H}
      =m_*\frac{R}{R+\ell}.
}
\tag{19}
\]

This field satisfies all of (6):

* On a Kähler metric, \(d\bar f\) is covariantly constant in the \((1,0)\) directions:
  \[
  \nabla^{1,0}(d\bar f)=0.
  \]
  This is the type projection appearing in the extract.
* The form is closed. Its \(\bar\partial\)-codifferential vanishes because the mixed covariant derivative above vanishes.
* Therefore the Kähler–Dirac identity gives
  \[
  D^-v=\sqrt2(\bar\partial+\bar\partial^*)v=0.
  \]
* With scalar curvature and determinant curvature zero, the spinorial Lichnerowicz formula gives
  \[
  \nabla^*\nabla v=0.
  \]

The connection is the Levi–Civita spin connection of (16). Hence the diagonal equation, off-diagonal equation, and coframe equations (10)–(12) hold automatically. This construction does not specify \(b,q\) independently and then hope that a metric realizes them.

The amplitude is radial, although the spinor itself is equivariant rather than invariant under the whole rotation group.

#### Exact energy calculation

For a circle-invariant function \(a(R)\),
\[
\Delta_{\mathrm{usual},h}a
 =H^{-1}\left(a''+\frac2R a'\right).
\]
Applying this to (19) gives
\[
\Delta_{\mathrm{usual},h}m
 =\frac{2m_*\ell^2}{(R+\ell)^4}.
\]
Thus
\[
\boxed{
|\nabla v|^2=\frac{m_*\ell^2}{(R+\ell)^4},\qquad
|dm|^2=\frac{m_*^2\ell^2R}{(R+\ell)^5}.
}
\tag{20}
\]
Since
\[
dV_h=H\,d^3x\,d\psi,
\]
the energies are
\[
\boxed{
\int|\nabla v|^2=8\pi^2m_*\ell^2,\qquad
\int|dm|^2=\frac{16\pi^2}{3}m_*^2\ell^2.
}
\tag{21}
\]
Both are finite and strictly positive. The field is smooth at the nut; the zero of \(m\) is not a singularity of \(v\).

The same metric has finite, nonzero opposite-chiral curvature action,
\[
0<\int|\mathrm{Rm}_h|^2<\infty.
\tag{22}
\]
Its opposite-chiral spin connection is an actual anti-self-dual Yang–Mills connection. This provides the instanton-like geometry capable of supporting the amplitude well.

There is even a concrete radial/horizontal split. With the first adapted plane selected by \(d\bar f\), set \(n_3=x_3/R\). Then
\[
E_1=|dm|^2(1-n_3^2),\qquad
E_2=|dm|^2n_3^2.
\]
Because \(|dm|^2/m=|\nabla v|^2\), equation (15) gives
\[
\frac{E_1+2E_2}{2m}
 =\frac{1+n_3^2}{2}|\nabla v|^2,
\qquad
2m|c|^2
 =\frac{1-n_3^2}{2}|\nabla v|^2.
\tag{23}
\]
Angular integration assigns two thirds of the total gradient energy to the radial part and one third to the horizontal part. In particular, this solution retains \(\mathfrak d\neq0\); it is not the reduced fifth-line model.

#### Retaining the actual torsion origin

The field (18) also has an infinitesimal positive-spinor parent. Let \(\Phi_0\) be parallel, with norm squared \(\rho_*\), and let \(e_2\) be a parallel complementary positive spinor. A suitable conjugate of \(f\) gives a spinor
\[
\chi=a\,\bar f\,e_2
\]
satisfying \(D^+\chi=0\). The linearization of cubic torsion at \(\Phi_0\) is
\[
Q_{\Phi_0}\chi
 =\sum_i c(e^i)\Phi_0\otimes
       \bigl(\Phi_0\wedge\nabla_{e_i}\chi\bigr).
\tag{24}
\]
It is a nonzero constant multiple of the spinor corresponding to \(d\bar f\). Choosing \(a\) gives \(Q_{\Phi_0}\chi=v\).

Consequently, on each fixed compact set,
\[
\Phi_r=\Phi_0+r\chi+O(r^2)
\quad\Longrightarrow\quad
r^{-1}t_h(\Phi_r)=v+O(r).
\tag{25}
\]
This supplies the first-order relation missing from an arbitrary independently chosen harmonic spinor. The order-\(r^2\) monopole and metric equations are not established by (25), and \(\chi\) grows at infinity.

### 4. Which simpler ansätze are obstructed?

The Taub–NUT solution identifies why round radial models and flat cylindrical models are too small a class.

**Round \(S^3\) warping.** For
\[
h=ds^2+a(s)^2g_{S^3},
\]
Ricci-flatness gives
\[
a''=0,\qquad (a')^2=1.
\]
A smooth complete model with a center is Euclidean \(\mathbb R^4\). Its determinant and spin connections are flat. Components of a bounded solution of \(\nabla^*\nabla v=0\) are bounded harmonic functions, hence constant. There is no radial energy.

Here the decisive coupled identity is the Ricci equation, which removes the geometric connection capable of supporting the well.

**Flat \(\mathbb R^2\times T^2\).** Fourier expansion in the torus directions reduces the rough harmonic equation to
\[
(\Delta_{\mathbb R^2}-|k|^2)v_k=0
\]
using the usual Laplacian. For radial modes, the regular nonzero-frequency solution grows like \(I_0(|k|R)\), while the decaying solution \(K_0(|k|R)\) is singular at the axis. The zero-frequency radial solution is \(A+B\log R\). Smoothness and boundedness leave only constants. A flat line holonomy merely shifts the Fourier frequencies.

**Smooth hyperkähler ALE models with trivial flat determinant line.** At infinity a bounded harmonic spinor approaches a spinor invariant under the end group \(\Gamma\subset SU(2)\), assuming the usual ALE elliptic asymptotics. The opposite-chiral spin representation is the defining two-dimensional representation. A nontrivial \(\Gamma\) has no nonzero invariant vector in this representation. Thus the asymptotic constant vanishes; the decaying finite-energy field is zero by integration of the rough harmonic equation.

If \(\Gamma\) is trivial, Ricci-flatness and Euclidean asymptotic volume ratio force the smooth complete metric to be Euclidean by Bishop–Gromov volume comparison. Again the bounded spinor is constant.

The precise end representation matters if a nontrivial flat line character is present. Taub–NUT avoids the ALE argument through circle collapse at infinity, not through an independently chosen curvature source.

### 5. What the tangent says about O10

The geometric content established above is
\[
\boxed{\text{A complete ALF tangent can carry nonzero radial capacity
and satisfy the full leading coupled system.}}
\]

It follows that the sought unrestricted argument cannot simply assert that every complete Ricci-flat, opposite-chiral, finite-energy tangent is trivial. Any successful exclusion must retain additional information about the ends, the relation to exterior geometry, or equations at another asymptotic order.

Three distinctions are especially important.

**Finite energy does not mean finite scale-invariant capacity.** For a physical copy \(\lambda^2h\) of the Taub–NUT core,
\[
\int|\nabla v|^2\asymp\lambda^2,\qquad
\int|dm|^2\asymp\lambda^2,\qquad
\int|\mathrm{Rm}|^2\asymp1.
\tag{26}
\]
Therefore \(N\) comparable cores carrying a fixed amount of normalized radial energy would have
\[
\frac{N\lambda^2}{V}\asymp1,
\qquad
\frac1V\int|W^-|^2\asymp\frac{N}{V}\asymp\lambda^{-2}.
\tag{27}
\]
This is exactly the density regime absent from the finite-density theorem.

**The bounded determinant-curvature fit has two asymptotic orders.** At leading rescaled order its bounded model vanishes, giving \(F_{\mathcal A}=0\). Recovering that model after division by \(r_j^2\) requires substantially stronger local error estimates. The supplied averaged fit does not provide them on every capacity core. Similarly, the monopole source in (1) is an order-\(r_j^2\) term. The Taub–NUT construction solves the surviving geometric tangent equations and the first-order torsion relation, not an exact finite-scale monopole completion.

**A smooth ALF core still needs a real exterior.** Its end is a circle fibration over \(S^2\), not an approximately round Euclidean end. Expanding that circle to attach the core to a noncollapsed exterior can generate a scale-invariant Ricci cost. Conversely, a globally collapsed arrangement might permit a different matching geometry. Nothing in the explicit local solution computes that transition cost or supplies an actual closed monopole.

This end-matching problem is a sharper object than another scalar radial estimate. It asks whether the ALF spin connection carrying the capacity can be embedded into a closed actual-field configuration while the combined transition and field cost, divided by total volume, tends to zero.

### 6. The smallest decisive computations

The leading ansatz is settled analytically by the Gibbons–Hawking and Kähler–Dirac identities. Its energy calculation needs only one-variable symbolic algebra:
```python
import sympy as s

R, ell, m0 = s.symbols("R ell m0", positive=True)
H = 1 + ell/R
m = m0/H

q = s.simplify((s.diff(m, R, 2) + 2*s.diff(m, R)/R)/(2*H))
rad = s.simplify(s.diff(m, R)**2/H)
density = 16*s.pi**2*ell*H*R**2

Ev = s.integrate(density*q, (R, 0, s.oo))
Em = s.integrate(density*rad, (R, 0, s.oo))
```
The outputs are the expressions in (20)–(21). A tensor computation of (9)–(12) on the biaxial coframe would expose the radial and horizontal coefficients explicitly, but is not needed to establish their Levi–Civita realization.

The genuinely unresolved symbolic calculation is the **order-\(r^2\) completion** of
\[
h_r=h+r^2k+\cdots,\qquad
\mathcal A_r=r^2a+\cdots,\qquad
\Phi_r=\Phi_0+r\chi+r^2\Phi_2+\cdots.
\tag{28}
\]
It couples the linearized Ricci equation, the self-dual curvature equation for \(a\), and the Dirac equation for \(\Phi_2\), with end behavior compatible with a real exterior. In a biaxial metric family and an equivariant spinor representation, the relevant tensor and spinor harmonics reduce this to radial equations rather than a four-dimensional numerical PDE. The quaternionic Taub–NUT/Pedersen self-dual Einstein family is a natural source family for the metric part; invariant Seiberg–Witten equations supply the field part.

The mathematical alternatives are now concrete: a completion with affordable end matching would supply an actual high-density escape mechanism; an unavoidable transition or field cost would identify the additional coupled identity needed for a global O10 theorem. The leading Taub–NUT tangent itself already demonstrates that opposite-chiral connection bubbling can carry the radial capacity.