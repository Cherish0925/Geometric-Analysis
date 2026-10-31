# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step28_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step28_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Formulate the b-independent scale-one saturation problem for diagonal Bianchi-IX metrics suggested by the small-b Taub-bolt/Λ-Taub-NUT/ACH transition. The inner limiting state is a Hopf-collapsed Berger/Taub-bolt neck; the terminal condition is the rho=1 standard-CR ACH stable set. Use the complete trace-free Ricci controls H,E,D with cost ∫ r^3(3H^2/16+E^2/6+D^2/8)dt, not D alone. Derive a mathematically executable state-control boundary-value problem, identify symmetries/scalings and the correct b-free entry/exit conditions, and explain how to distinguish a positive saturation payment from arbitrarily cheap steering. Ground the derivation in the provided exact diagonal equations and accumulated notes; do not invent numerical results.

## Integrated Scientific Memo

## \(b\)-independent scale-one saturation problem

Use the slot convention
\[
g=dt^2+F^2\sigma_f^2+G^2\sigma_g^2+C^2\sigma_h^2,
\]
where \(F\) is the eventual ACH Reeb direction, \(G,C\) the eventual contact directions, and \(C\) is the Hopf circle collapsed in the small-\(b\) Taub-bolt/\(\Lambda\)-Taub-NUT neck. Thus the inner neck is
\[
F\simeq G=A,\qquad C/A=\varepsilon\downarrow0,
\]
whereas standard complex hyperbolic infinity requires
\[
G/C\to1,\qquad \frac{F}{GC}\to1,\qquad \rho_\infty=1.
\]
The problem is therefore a genuine permutation of geometric roles, not merely control of the contact anisotropy.

### 1. Exact state–control equations and full cost

Write
\[
F=re^{2\beta/3},\qquad
G=re^{-\beta/3+q/2},\qquad
C=re^{-\beta/3-q/2},\qquad h=\log r.
\]
Then \(r^3=FGC=W\), \(q=\log(G/C)\), and
\[
\beta=\log\frac{F}{\sqrt{GC}}.
\]
Let
\[
u=h',\qquad v=\beta',\qquad w=q'
\]
and use as controls the complete trace-free Ricci combinations
\[
D=R_{gg}-R_{hh},\qquad
E=R_{ff}-\frac{R_{gg}+R_{hh}}2,\qquad
H=R_{00}-\frac{R_{ff}+R_{gg}+R_{hh}}3.
\]
The exact diagonal equations supplied in Step 26 are
\[
\begin{aligned}
D&=-q''-3h'q'+e^{-2h}\mathcal V_D,\\
E&=-\beta''-3h'\beta'+e^{-2h}\mathcal V_E,\\
H&=-2h''-\frac23(\beta')^2-\frac12(q')^2+e^{-2h}\mathcal V_H,
\end{aligned}
\]
where
\[
\begin{aligned}
\mathcal V_D&=
8\left(e^{-4\beta/3}\sinh 2q-e^{2\beta/3}\sinh q\right),\\
\mathcal V_E&=
4e^{8\beta/3}-4e^{2\beta/3}\cosh q
-8e^{-4\beta/3}\sinh^2q,\\
\mathcal V_H&=
\frac23e^{8\beta/3}-\frac83e^{2\beta/3}\cosh q
+\frac83e^{-4\beta/3}\sinh^2q.
\end{aligned}
\]
Equivalently,
\[
\begin{aligned}
h'&=u,&\beta'&=v,&q'&=w,\\
u'&=-\frac12H-\frac13v^2-\frac14w^2+\frac12e^{-2h}\mathcal V_H,\\
v'&=-3uv+e^{-2h}\mathcal V_E-E,\\
w'&=-3uw+e^{-2h}\mathcal V_D-D.
\end{aligned}
\tag{1}
\]
The exact normalized defect is
\[
\boxed{\;
\widehat P
=\int r^3\left(\frac3{16}H^2+\frac16E^2+\frac18D^2\right)dt .
\;}
\tag{2}
\]
This is the indispensable correction to a \(D\)-only CR-control model: \(D\) changes \(G/C\), \(E\) changes the Reeb/contact splitting, and \(H\) pays for the associated radial/volume acceleration.

---

## 2. Removal of the absolute scale

Introduce conformal radial time and scale-free velocities
\[
d\tau=\frac{dt}{r},\qquad
p=rh',\qquad \xi=r\beta',\qquad \eta=rq',
\]
together with
\[
\bar H=r^2H,\qquad \bar E=r^2E,\qquad \bar D=r^2D.
\]
For the scale-free state
\[
Y=(\beta,q,p,\xi,\eta)
\]
one obtains
\[
\boxed{
\begin{aligned}
\dot\beta&=\xi,\\
\dot q&=\eta,\\
\dot p&=p^2-\frac13\xi^2-\frac14\eta^2
       +\frac12\mathcal V_H-\frac12\bar H,\\
\dot\xi&=-2p\xi+\mathcal V_E-\bar E,\\
\dot\eta&=-2p\eta+\mathcal V_D-\bar D ,
\end{aligned}}
\tag{3}
\]
and, exactly,
\[
\boxed{\;
\widehat P=\int
\left(\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\right)d\tau .
\;}
\tag{4}
\]
Thus neither the dynamics nor the cost contains \(h\), the bolt radius \(b\), or another absolute length.

This is the quotient of the original invariance
\[
t\mapsto\lambda t,\qquad (F,G,C)\mapsto\lambda(F,G,C),
\]
under which \(h\mapsto h+\log\lambda\), while \(Y,\tau,\bar H,\bar E,\bar D\) and \(\widehat P\) are unchanged. The remaining symmetries are:

* translation of \(\tau\);
* exchange of the contact slots,
  \[
  q\mapsto-q,\quad \eta\mapsto-\eta,\quad \bar D\mapsto-\bar D;
  \]
* permutations of orbit slots before the bolt and terminal Reeb sectors are fixed.

---

## 3. Correct \(b\)-free entry condition

At a scale-one section of the collapsed \(\Lambda\)-Taub-NUT neck, set
\[
F=G=A,\qquad C=\varepsilon A,\qquad \varepsilon\downarrow0,
\]
and define the normalized first-jet data
\[
U=A',\qquad V=A\,\frac{C'}C.
\]
Then
\[
q=\log\varepsilon^{-1},\qquad
\beta=\frac12\log\varepsilon^{-1},
\]
and direct substitution gives
\[
\boxed{
\begin{aligned}
p&=\varepsilon^{1/3}\frac{2U+V}{3},\\
\xi&=\varepsilon^{1/3}\frac{U-V}{2},\\
\eta&=\varepsilon^{1/3}(U-V).
\end{aligned}}
\tag{5}
\]
The limiting \(\Lambda\)-Taub-NUT profile recorded in the source is
\[
A(s)=\frac{\sinh(\sqrt2s)}{\sqrt2},\qquad
U(A)=\sqrt{1+2A^2},\qquad
V(A)=\frac{2A^2}{\sqrt{1+2A^2}},
\tag{6}
\]
while the small-bolt matching gives
\[
\varepsilon_b(A)=\frac{C}{A}
=\frac{2b}{\sqrt3}\frac{U(A)}A+o(b).
\tag{7}
\]
Hence, for \(A\) in any compact scale-one interval
\[
K=[A_-,A_+]\Subset(0,\infty),
\]
the limit \(b\to0\) is precisely \(\varepsilon\to0\) in the entry family
\[
\boxed{
I_\varepsilon(A)=
\left(
\frac12\log\varepsilon^{-1},
\log\varepsilon^{-1},
\varepsilon^{1/3}\frac{2U(A)+V(A)}3,
\varepsilon^{1/3}\frac{U(A)-V(A)}2,
\varepsilon^{1/3}(U(A)-V(A))
\right).
}
\tag{8}
\]
This Taub-bolt/\(\Lambda\)-Taub-NUT first-jet ray is essential. Allowing arbitrary bounded Berger first jets would enlarge the entry set by geometries not obtained from the small-\(b\) matching.

A useful regularization is
\[
x=\beta-\frac q2=\log(F/G),\qquad z=e^{-q/3}=\varepsilon^{1/3},
\qquad \chi=\xi-\frac{\eta}{2}.
\]
The entry face is
\[
z\to0,\qquad x\to0,\qquad \chi\to0.
\]
Along \(x=0\), exact cancellation gives
\[
\mathcal V_D=4(z^2-z^8),\qquad
\mathcal V_E=2(z^2-z^8),\qquad
\mathcal V_H=-\frac83z^2+\frac23z^8.
\tag{9}
\]
Moreover,
\[
\dot x=\chi,\qquad
\dot\chi=-2p\chi+\mathcal V_x-\bar E+\frac12\bar D,
\tag{10}
\]
with
\[
\mathcal V_x=
4z^{-4}\!\left(e^{8x/3}-e^{-4x/3}\right)
+4z^2\!\left(e^{-4x/3}-e^{2x/3}\right),
\tag{11}
\]
so
\[
\mathcal V_x=16z^{-4}x+O(z^{-4}x^2+z^2x).
\]
This is the scale-free form of the \(4/C\) collapsed-neck instability. Crucially, the effective shape control is
\[
a=-\bar E+\frac12\bar D,
\]
not \(\bar D\) alone. For fixed \(a\),
\[
\min_{-\bar E+\bar D/2=a}
\left(\frac16\bar E^2+\frac18\bar D^2\right)
=\frac18a^2,
\]
attained at
\[
\bar E=-\frac34a,\qquad \bar D=\frac12a.
\]
The \(\bar H\)-channel remains independently necessary.

Because exponentially small \(x\)-seeds can be amplified to order one, the limiting entry condition must be defined as the limit of the finite-\(\varepsilon\) problems. One must not replace it in advance by an arbitrary “free saturation phase.”

---

## 4. Correct standard-CR terminal condition

Choose a fixed small ACH section \(\zeta=\zeta_*>0\), where
\[
\zeta=\frac1{GC}=e^{-2h+2\beta/3}.
\]
At this section
\[
h=\frac{\beta}{3}-\frac12\log\zeta_*,
\]
and the scale state maps to the compact ACH variables by
\[
\mathcal A_{\zeta_*}(Y)
=(y_f,y_g,y_h,\kappa,q,\zeta_*),
\]
where
\[
\boxed{
\begin{aligned}
y_f&=\sqrt{\zeta_*}\,e^{-\beta/3}
       \left(p+\frac23\xi\right),\\
y_g&=\sqrt{\zeta_*}\,e^{-\beta/3}
       \left(p-\frac13\xi+\frac12\eta\right),\\
y_h&=\sqrt{\zeta_*}\,e^{-\beta/3}
       \left(p-\frac13\xi-\frac12\eta\right),\\
\kappa&=\sqrt{\zeta_*}\,e^\beta .
\end{aligned}}
\tag{12}
\]

Let \(\Sigma_{\mathrm{std}}(\zeta_*)\) be the stable set, on this section, of the uncontrolled compact Einstein flow that converges to
\[
E(0)=(2,1,1,1,0,0).
\]
Equivalently, a point \(W\) belongs to \(\Sigma_{\mathrm{std}}(\zeta_*)\) when:

1. it satisfies the Einstein Hamiltonian constraint;
2. its forward uncontrolled orbit has no \(+2\) outgoing mode;
3. its limiting CR invariant is
   \[
   \Phi_\infty=0,\qquad \rho_\infty=1.
   \]

A computational residual is therefore
\[
\mathcal R(W)=
\bigl(\mathcal U_+(W),\,\Phi_\infty(W),\,\mathcal C(W)\bigr),
\tag{13}
\]
and the terminal manifold in scale-free coordinates is
\[
\boxed{
\overline\Sigma_{\mathrm{std}}(\zeta_*)
=\{Y:\mathcal R(\mathcal A_{\zeta_*}(Y))=0\}.
}
\tag{14}
\]
It can equivalently be parameterized inward from \(E(0)\) by its stable modes. At fixed \(\zeta_*\), the \(-2\) CH radial-phase mode is fixed by the section; the physical stable directions are the \(-4\) and \(-6\) modes, with the \(-8\) direction excluded by the Einstein constraint.

The finite-section condition
\[
\widetilde\Phi
=q+\frac14(y_g-y_h)-\zeta\sinh q=0
\]
is not by itself exact: the source identity gives
\[
\widetilde\Phi'=F-\frac14D,
\]
with \(F=\zeta^2G\) only inside the ACH block, so an \(O(\zeta_*^2)\) terminal drift remains. The correct condition is \(\Phi_\infty=0\), obtained by outward integration or stable-manifold parameterization.

If one wants immediate attachment to exact CH rather than to a standard-CR Einstein tail, replace (14) by
\[
\mathcal A_{\zeta_*}(Y)=H(\zeta_*),
\]
where
\[
H(\zeta_*)=
\left(
\sqrt{1+\zeta_*}+\frac1{\sqrt{1+\zeta_*}},
\sqrt{1+\zeta_*},
\sqrt{1+\zeta_*},
\sqrt{1+\zeta_*},
0,\zeta_*
\right).
\tag{15}
\]
For the infimum these formulations agree after sending the cutoff outward, by the standard-CR truncation theorem.

---

## 5. The executable saturation value

For a compact scale-one phase interval \(K\Subset(0,\infty)\), define
\[
\boxed{
\begin{aligned}
\mathcal V_{\mathrm{sat}}(K)
=\liminf_{\varepsilon\downarrow0}\;
\inf\Bigg\{&
\int_0^T
\left(
\frac3{16}\bar H^2+
\frac16\bar E^2+
\frac18\bar D^2
\right)d\tau :\\
&Y(0)=I_\varepsilon(A),\quad A\in K,\\
&Y(T)\in\overline\Sigma_{\mathrm{std}}(\zeta_*),\quad T>0,\\
&Y\text{ solves \((3)\)}
\Bigg\}.
\end{aligned}}
\tag{16}
\]
This is the \(b\)-independent, scale-one saturation problem suggested by the Taub-bolt/\(\Lambda\)-Taub-NUT/ACH transition.

The \(\liminf\) is deliberate: it retains any boundary-layer use of the exponentially unstable collapsed mode. A stronger conclusion requires proving convergence of the finite-\(\varepsilon\) value functions and independence of the admissible compact interval \(K\) once it contains all possible scale-one saturation phases.

---

## 6. Extremal equations

Writing (3) as
\[
\dot Y=F(Y)+B\bar u,\qquad
\bar u=(\bar H,\bar E,\bar D),
\]
gives
\[
B=
\begin{pmatrix}
0&0&0\\
0&0&0\\
-\frac12&0&0\\
0&-1&0\\
0&0&-1
\end{pmatrix},
\qquad
R=\operatorname{diag}\!\left(\frac3{16},\frac16,\frac18\right).
\]
For
\[
\mathcal H=\lambda\cdot(F+B\bar u)+\bar u^TR\bar u,
\]
pointwise minimization yields
\[
\boxed{
\bar H=\frac43\lambda_p,\qquad
\bar E=3\lambda_\xi,\qquad
\bar D=4\lambda_\eta .
}
\tag{17}
\]
Together with
\[
\dot\lambda=-\partial_Y\mathcal H
\]
this is a ten-dimensional state–costate boundary-value system. Free terminal time imposes \(\mathcal H=0\); free \(A\in K\) imposes
\[
\lambda(0)\cdot\partial_A I_\varepsilon(A)=0
\]
for an interior minimizing \(A\); and
\[
\lambda(T)\perp T_{Y(T)}\overline\Sigma_{\mathrm{std}}(\zeta_*).
\]
The variables \((x,z,p,\chi,\eta)\), with the factorizations (9)–(11), are preferable near collapse because they avoid catastrophic cancellation.

---

## 7. Positive payment versus arbitrarily cheap steering

### Zero-cost connection

If an uncontrolled orbit,
\[
\bar H=\bar E=\bar D=0,
\]
emerges from the finite-\(\varepsilon\) collapsed entry family and reaches the standard-CR stable set in the limit, then
\[
\mathcal V_{\mathrm{sat}}(K)=0.
\]
This is precisely a scale-quotiented small-bolt Einstein connection to \(\rho_\infty=1\).

Absence of an exact uncontrolled connection is not sufficient for positivity: the collapsed instability could give unbounded control gain.

### Projected controllability Gramian

Along an uncontrolled reference orbit \(\bar Y\), linearize:
\[
\delta\dot Y=A(\tau)\delta Y+B\,\delta\bar u.
\]
The weighted controllability Gramian is
\[
\mathcal G_T=
\int_0^T
\Psi(T,s)\,BR^{-1}B^T\,\Psi(T,s)^T\,ds,
\tag{18}
\]
where
\[
BR^{-1}B^T
=\operatorname{diag}_{(p,\xi,\eta)}
\left(\frac43,6,8\right).
\]
Project \(\mathcal G_T\) onto the normal bundle of the terminal stable set, represented by the three residuals
\[
(\mathcal U_+,\Phi_\infty,\mathcal C).
\]

* If a projected eigenvalue diverges as \(\varepsilon\to0\), a fixed terminal correction may cost \(o(1)\). This identifies an arbitrarily cheap steering channel.
* If the projected Gramian stays uniformly bounded and the uncontrolled exit family remains a positive distance from the terminal stable set, the linearized payment is positive. A nonlinear proof must additionally prevent low-cost escape from the reference tube.

### Hamilton–Jacobi certificate

A global lower-bound certificate is a \(C^1\) function \(S(Y)\) satisfying
\[
\boxed{
F(Y)\cdot\nabla S+
\frac13S_p^2+\frac32S_\xi^2+2S_\eta^2\le0.
}
\tag{19}
\]
Indeed, completing squares against the three controls gives
\[
\widehat P\ge S(Y(T))-S(Y(0)).
\]
Consequently,
\[
\inf_{\overline\Sigma_{\mathrm{std}}}S
-\limsup_{\varepsilon\to0}\sup_{A\in K}S(I_\varepsilon(A))
=c>0
\]
implies
\[
\mathcal V_{\mathrm{sat}}(K)\ge c.
\tag{20}
\]

Conversely, cheap steering requires an explicit admissible family satisfying the full estimate
\[
\int
\left(\frac3{16}\bar H_\varepsilon^2+
\frac16\bar E_\varepsilon^2+
\frac18\bar D_\varepsilon^2\right)d\tau\to0.
\tag{21}
\]
Small \(D\)-cost alone is inconclusive: rapid slot rotation can transfer the cost to \(E\), and the corresponding volume acceleration to \(H\).

### Flux localization

The chiral transgressions remain useful as state constraints. A bounded-geometry Hopf-collapsed entry has
\[
(\mathfrak b_+,\mathfrak b_-)\to(-2,2),
\]
and every segment satisfies
\[
\widehat P\ge
\mathfrak b_\pm(T)-\mathfrak b_\pm(0).
\]
Thus ordinary decollapse toward a near-round orbit is expensive; in particular the \(+\)-flux rises from \(-2\) to \(2\), costing at least \(4\). Ordinary Berger/ALF necks are likewise separated from a developed Rossi ACH region by the Euler flux. These inequalities do not settle the residual high-shear route, because the relevant flux may decrease there. They instead confine any putative cheap optimizer to the singular high-shear sector governed by (3)–(4).

Hence the unresolved scientific quantity is exactly the value (16). Positivity requires a coercive dynamic-programming/Gramian-plus-no-escape argument for the full \(H,E,D\) system; vanishing requires an explicit finite-\(\varepsilon\) family reaching the \(\rho=1\) stable set with the complete cost (21) tending to zero.