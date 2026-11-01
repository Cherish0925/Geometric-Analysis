# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step81_evolution.json",
    "Sessions/S0910A03/workspace/data/step81_contraction_analysis.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md"
  ]
}
```

## Task

Verify the following chain of results for the reflected Einstein evolution from T²-invariant constant-area centers on T³ with Ric=-3g:

1. ORBIT MATRIX PARAMETRIZATION: In SL(2,R)/SO(2) with metric ds²=(1/2)tr((M⁻¹dM)²), geodesic polar gives M=cosh(d)I+sinh(d)n(θ) with n=[[cosθ,sinθ],[sinθ,-cosθ]], n²=I. The metric is dd²+sinh²(d)dθ² (curvature -1). A rotating loop d=d*, θ=kz has energy k²sinh²(d*). Setting this to 12 gives R(q₀)=-6 for constant area.

2. S'(0) EIGENVALUES: The reflected Einstein germ has S(0)=0, S'(0)=Ric(q₀)+3I. For constant-area centers: the z-eigenvalue is -|A|²+3=-3 (universal). The orbit eigenvalues have trace 6 but split depending on k and d*. Numerical: k=2 gives orbit eigenvalues ≈(9.93,-3.93); k=8 gives ≈(18.09,-12.09). Derive the exact analytical formula for the orbit eigenvalues.

3. ANGULAR-SLIP ENERGY PRESERVATION: For the perturbation d=d*+εcos(k̃z), θ=k₀z+εB₀sin(k̃z)/k̃ with B₀=-(k₀/k̃)coth(d*), the H² speed² deviates from 12 by O(ε²) with coefficient ~20. Verify this cancellation analytically: what is the exact O(ε²) coefficient? Does the cancellation extend to the orbit Ricci components, not just the trace?

4. UNIVERSAL AVERAGE CONTRACTION: For ANY constant-area center with R(q₀)=-6: ⟨|A|²⟩=6, hence ⟨u'(0)⟩=-3. For non-constant area: ⟨u'(0)⟩=-3+⟨h²⟩. Is this derivation correct? What are the assumptions?

5. VII₀ COLLAPSE: The ODE evolution for the Bianchi VII₀ system shows finite-distance collapse at r≈0.3-0.4 for all k=2,...,8. The cascade is K>3→u'<0→a↓→K↑. Does this collapse persist in the z-dependent (non-VII₀) case? Specifically: if u'(0,z)=-3+O(ε²) everywhere (from result 3), can the z-dependent evolution avoid collapse through spatial redistribution?

6. IMPLICATIONS FOR GRAPH CONSTRUCTION: Does the collapse force O(1) Ricci defect near the center, preventing ||E||_∞→0? Or is there an escape through non-constant-area centers, non-OT geometry, or non-reflected metrics?

## Output

# Scientific verification memo

## Summary

1. The \(SL(2,\mathbb R)/SO(2)\) parametrization and normalization are correct. For a constant-area \(T^2\)-invariant center,
   \[
   R(q_0)=-\frac12|U_z|_{\mathbb H^2}^2,
   \]
   so \(R(q_0)=-6\) is equivalent to hyperbolic speed squared \(12\).

2. For the rotating loop \(d=d_*,\theta=kz\), the exact orbit eigenvalues of \(S'(0)\) are
   \[
   \boxed{3\pm \sqrt{3(k^2+12)}}.
   \]
   The \(z\)-eigenvalue is exactly \(-3\).

3. The angular-slip formula in the question has one extra factor of \(\tilde k^{-1}\). With the corrected normalization, the speed-squared expansion is
   \[
   12+\varepsilon^2\!\left[\tilde k^2\sin^2(\tilde kz)
   -(2k_0^2+12)\cos^2(\tilde kz)\right]+O(\varepsilon^3).
   \]
   For \(k_0=2,\tilde k=1\), the pointwise coefficient is
   \[
   1-21\cos^2z,
   \]
   and the uniform coefficient in \(\sup|\,|U_z|^2-12|\) is exactly \(20\). The orbit Ricci tensor still changes at order \(\varepsilon\).

4. The average formula
   \[
   \langle u'(0)\rangle=-3+\langle h^2\rangle
   \]
   is correct for the unweighted unit-arclength average. The center-volume-weighted average is instead always \(-3\). The `nonconst_c*` entries in `step81_contraction_analysis.json` describe variable loop speed at constant orbit area and do not test the nonconstant-area formula.

5. Exact Bianchi VII\(_0\) solutions do reach a finite radial singularity; this follows analytically from the Step 78 equations. The numerical records place the apparent endpoints at \(0.24\)–\(0.36\), not uniformly \(0.3\)–\(0.4\). No corresponding monotonic quantity has been established for the full \(z\)-dependent matrix system.

6. An order-one Ricci defect is forced only for a connector that remains in the fixed VII\(_0\) ansatz: Step 78 gives the quantitative threshold \(3/5\). The supplied results do not give such a lower bound for general \(z\)-dependent OT connectors. Exact reflected non-OT geometry is unavailable under the standard commuting reflection because the twist constants vanish.

---

## 1. Orbit matrix and center scalar curvature

Let
\[
n(\theta)=
\begin{pmatrix}
\cos\theta&\sin\theta\\
\sin\theta&-\cos\theta
\end{pmatrix},
\qquad n^2=I,\qquad \operatorname{tr}n=0,
\]
and
\[
M=\cosh d\,I+\sinh d\,n(\theta).
\]
Its eigenvalues are \(e^d,e^{-d}\), so \(M\) is symmetric positive definite and \(\det M=1\). Also
\[
M^{-1}=\cosh d\,I-\sinh d\,n.
\]

Writing \(t=\partial_\theta n\) and \(J=nt\), direct multiplication gives
\[
\frac12\operatorname{tr}\bigl((M^{-1}dM)^2\bigr)
=dd^2+\sinh^2d\,d\theta^2.
\]
The Gaussian curvature of \(dd^2+f(d)^2d\theta^2\) is \(-f''/f\); for \(f=\sinh d\), it is \(-1\).

Now take the center metric
\[
q_0=dz^2+M_{ab}(z)\,d\xi^a d\xi^b,
\qquad Q=M^{-1}M_z.
\]
Because \(\det M=1\), \(\operatorname{tr}Q=0\). The orbit shape operator within \(q_0\) is
\[
\mathcal A=\frac12Q,
\]
and
\[
|\mathcal A|^2=\frac14\operatorname{tr}(Q^2)
=\frac12|U_z|_{\mathbb H^2}^2.
\]
The curvature formulas are
\[
\operatorname{Ric}_{q_0}(\partial_z,\partial_z)
=-|\mathcal A|^2,
\qquad
R(q_0)=-|\mathcal A|^2
=-\frac12|U_z|_{\mathbb H^2}^2.
\]
Therefore
\[
R(q_0)=-6
\quad\Longleftrightarrow\quad
|U_z|_{\mathbb H^2}^2=12.
\]

For \(d=d_*,\theta=kz\),
\[
|U_z|^2=k^2\sinh^2d_*,
\]
hence
\[
\boxed{k^2\sinh^2d_*=12},
\qquad
d_*=\operatorname{arsinh}\frac{\sqrt{12}}{|k|}.
\]

The polar angle \(\theta\) is twice the orbit eigenframe angle used in the Step 78 coframe. Thus the Step 78 coframe frequency \(k_{\mathrm{VII}}\) corresponds to polar frequency \(k=2k_{\mathrm{VII}}\).

---

## 2. Exact spectrum of \(S'(0)\)

For
\[
g=dr^2+q_r,\qquad S=\frac12q_r^{-1}\partial_rq_r,
\]
the tangential Einstein equation gives
\[
S'=\operatorname{Ric}(q_r)+3I-HS.
\]
At a reflected face, \(S(0)=H(0)=0\), so
\[
S'(0)=\operatorname{Ric}(q_0)+3I.
\]

For the rotating loop, with \(s=\sinh d_*\), \(c=\cosh d_*\),
\[
Q'=-k^2sc\,n.
\]
Since the orbit Ricci endomorphism is
\[
\operatorname{Ric}_{\mathrm{orb}}=-\frac12Q',
\]
its two eigenvalues are
\[
\pm L,\qquad L=\frac{k^2}{2}sc.
\]
Using \(k^2s^2=12\),
\[
L=6\coth d_*
=\sqrt{3(k^2+12)}.
\]
Consequently
\[
\boxed{\operatorname{Spec}S'(0)
=
\left\{
-3,\,
3+\sqrt{3(k^2+12)},\,
3-\sqrt{3(k^2+12)}
\right\}.}
\]

The trace is
\[
-3+(3+L)+(3-L)=3,
\]
as also follows from \(R(q_0)+9=3\).

Numerically:

- \(k=2\):
  \[
  L=\sqrt{48}=6.9282032303,
  \]
  \[
  \lambda_{\mathrm{orb}}=(9.9282032303,-3.9282032303).
  \]

- \(k=8\):
  \[
  L=\sqrt{228}=15.0996688705,
  \]
  \[
  \lambda_{\mathrm{orb}}=(18.0996688705,-12.0996688705).
  \]

The nearby values in `step81_evolution.json` have small discretization errors. For example, its \(k=8\) entry also has \(\operatorname{Ric}_{zz}=-5.99518\) rather than \(-6\), so it is not an exact evaluation of the analytic center.

---

## 3. Angular-slip expansion

Set
\[
m=k_0,\qquad q=\tilde k,\qquad
s=\sinh d_*,\qquad c=\cosh d_*,
\qquad m^2s^2=12.
\]

### Normalization issue

The question writes
\[
\theta=mz+\varepsilon B_0\frac{\sin(qz)}q,
\qquad
B_0=-\frac mq\coth d_*.
\]
Then
\[
\theta_z=m+\varepsilon B_0\cos(qz),
\]
and the first-order variation of the speed squared is
\[
2\varepsilon m^2sc\left(1-\frac1q\right)\cos(qz).
\]
Thus this is \(O(\varepsilon^2)\) only when \(q=1\).

Either of the following equivalent conventions gives the intended cancellation:
\[
\theta=mz+\varepsilon b\sin(qz),
\qquad
b=-\frac mq\coth d_*,
\]
or
\[
\theta=mz+\varepsilon B\frac{\sin(qz)}q,
\qquad
B=-m\coth d_*.
\]

### Exact second-order term

Using the corrected convention,
\[
d=d_*+\varepsilon\cos(qz),
\qquad
\theta_z=m-\varepsilon m\coth d_*\cos(qz).
\]
Since
\[
|U_z|^2=d_z^2+\sinh^2(d)\theta_z^2,
\]
expansion gives
\[
\boxed{
|U_z|^2
=
12+\varepsilon^2
\left[
q^2\sin^2(qz)-(2m^2+12)\cos^2(qz)
\right]
+O(\varepsilon^3).
}
\]

For \(m=2,q=1\),
\[
|U_z|^2
=
12+\varepsilon^2(\sin^2z-20\cos^2z)+O(\varepsilon^3)
=
12+\varepsilon^2(1-21\cos^2z)+O(\varepsilon^3).
\]
Hence:

- minimum coefficient: \(-20\);
- maximum coefficient: \(1\);
- uniform absolute coefficient: \(20\);
- circle mean coefficient: \(-19/2\).

This matches `step81_contraction_analysis.json`: at \(\varepsilon=0.01\), the recorded speed interval is approximately
\[
[12-20.09197\,\varepsilon^2,\;12+\varepsilon^2],
\]
with the difference from \(20\) coming from higher orders.

Because
\[
u'(0)=3-\frac12|U_z|^2
\]
for constant orbit area,
\[
u'(0,z)
=
-3-\frac{\varepsilon^2}{2}
\left[
q^2\sin^2(qz)-(2m^2+12)\cos^2(qz)
\right]
+O(\varepsilon^3).
\]

### Orbit Ricci does change at first order

Let \(t=\partial_\theta n\) and \(J=nt\). For arbitrary \(d(z),\theta(z)\),
\[
Q'
=
(d''-sc\,\theta'^2)n
+(2c^2d'\theta'+sc\,\theta'')t
-(2sc\,d'\theta'+s^2\theta'')J.
\]
For the corrected slip,
\[
Q'
=
-m^2sc\,n
+\varepsilon\left[
(m^2-q^2)\cos(qz)n
-mqc^2\sin(qz)t
+mqsc\sin(qz)J
\right]
+O(\varepsilon^2).
\]
Therefore
\[
\operatorname{Ric}_{\mathrm{orb}}=-\frac12Q'
\]
has order-\(\varepsilon\) diagonal and off-diagonal changes.

At points where \(\sin(qz)=0\), its two eigenvalues change by
\[
\mp\frac{\varepsilon}{2}(m^2-q^2)\cos(qz).
\]
Thus the slip preserves the scalar and \(zz\)-Ricci component to first order, but not the traceless orbit Ricci tensor.

Also, the raw perturbed center has \(R=-6+O(\varepsilon^2)\), rather than exactly \(-6\). An exact reflected Einstein center needs second-order corrections to the loop or an area/base response. If orbit area remains constant and \(R=-6\) is restored exactly, then \(|U_z|^2=12\) and \(u'(0)=-3\) exactly.

---

## 4. Average contraction and its assumptions

Use unit arclength \(s\) on the quotient circle and write
\[
q_0=ds^2+G_{ab}(s)d\xi^a d\xi^b.
\]
Define
\[
\mathcal A=\frac12G^{-1}\dot G,
\qquad
h=\operatorname{tr}\mathcal A
=\frac{d}{ds}\log\sqrt{\det G}.
\]
The \(T^2\) orbits are intrinsically flat. Their foliation equations give
\[
\operatorname{Ric}_{q_0}(\nu,\nu)
=-\dot h-|\mathcal A|^2,
\]
\[
R(q_0)=-2\dot h-h^2-|\mathcal A|^2.
\]
At an exact reflected Einstein face,
\[
R(q_0)=-6
\]
and
\[
u'(0,s)=3-\dot h-|\mathcal A|^2
=-3+\dot h+h^2.
\]

### Constant orbit area

If \(h=0\), then
\[
|\mathcal A|^2=6
\]
pointwise and
\[
\boxed{u'(0,s)=-3}
\]
pointwise. The average statement is therefore weaker than the actual identity.

### Unweighted arclength average

For
\[
\langle f\rangle_s=\frac1L\int_0^L f(s)\,ds,
\]
periodicity gives \(\langle\dot h\rangle_s=0\). Averaging \(R=-6\) yields
\[
\langle h^2+|\mathcal A|^2\rangle_s=6.
\]
Hence
\[
\boxed{
\langle u'(0)\rangle_s
=-3+\langle h^2\rangle_s.
}
\]
Thus a noncontracting unweighted mean requires
\[
\langle h^2\rangle_s\ge3.
\]

If \(G=e^\sigma M\), \(\det M=1\), and
\[
e=\frac12\operatorname{tr}\bigl((M^{-1}\dot M)^2\bigr),
\]
then
\[
|\mathcal A|^2=\frac12h^2+\frac12e,
\]
and the scalar equation becomes
\[
\boxed{e=12-4\dot h-3h^2.}
\]
In particular \(e\ge0\) imposes a real coupling between area variation and orbit-shape energy.

### Center-volume-weighted average

With \(\rho=\sqrt{\det G}\),
\[
\langle f\rangle_\rho
=
\frac{\int f\rho\,ds}{\int\rho\,ds}.
\]
Since \(\dot\rho=h\rho\),
\[
\langle\dot h\rangle_\rho=-\langle h^2\rangle_\rho.
\]
The scalar equation then gives
\[
\langle|\mathcal A|^2\rangle_\rho
=6+\langle h^2\rangle_\rho,
\]
and consequently
\[
\boxed{\langle u'(0)\rangle_\rho=-3.}
\]

Thus the formula \(-3+\langle h^2\rangle\) requires the unweighted unit-arclength convention. Uniform coordinate-\(z\) sampling gives the same quantity only when \(z\) is unit arclength.

### What the attached `nonconst_c*` data represent

The speed intervals in `step81_contraction_analysis.json` are exactly
\[
e_{\min}=3(2-c)^2,\qquad e_{\max}=3(2+c)^2.
\]
Together with
\[
u'=3-\frac e2,
\]
they give
\[
\langle u'\rangle=-3-\frac34c^2,
\]
which reproduces every listed mean. These are variable-speed, constant-area loops:
\[
e(z)=3(2+c\cos z)^2.
\]
Their scalar curvature is \(R=-e/2\), which is not identically \(-6\) for \(c\ne0\). They therefore do not provide numerical evidence for the nonconstant-area identity above.

The derivation assumes a smooth free \(T^2\) action over a quotient circle, unit horizontal arclength, flat torus orbits, periodic \(h\), exact reflection \(S(0)=0\), and the exact Gauss relation \(R(q_0)=-6\).

---

## 5. Exact VII\(_0\) finite radial singularity and the \(z\)-dependent system

For the exact Step 78 VII\(_0\) equations,
\[
u'+Hu=3-K,
\]
\[
p'+Hp=2K\coth d,
\]
\[
(\log K)'=-2u+2\coth d\,p,
\]
with
\[
K(0)=6,\qquad u<0,\qquad p>0,\qquad K>6.
\]
Combining the normal and Hamilton equations gives the useful scalar equation
\[
\boxed{H'=9-H^2-K.}
\]

Since \(K\ge6\),
\[
H'\le3-H^2,
\]
so
\[
H(r)\le\sqrt3\tanh(\sqrt3r)<\sqrt3
\]
as long as the solution is smooth.

Using the integrating factor in the \(u\)-equation,
\[
-u(r)
\ge
3\int_0^r
\exp\!\left(-\int_t^rH(s)\,ds\right)dt
\ge
\sqrt3(1-e^{-\sqrt3r}).
\]
Therefore
\[
(\log K)'
\ge-2u
\ge2\sqrt3(1-e^{-\sqrt3r}),
\]
and hence
\[
K(r)\ge
6\exp\!\left(
2\sqrt3r-2(1-e^{-\sqrt3r})
\right).
\]
Thus \(K\) crosses \(10\) after finite radius if smoothness persists that far. From then on,
\[
H'\le-1-H^2,
\]
so
\[
(\arctan H)'\le-1.
\]
Consequently \(H\) cannot remain finite for arbitrarily large \(r\). This proves a finite maximal radial interval for the exact VII\(_0\) solution. It does not by itself identify which metric coefficient degenerates first, though the numerical data show \(a\) becoming very small while \(K\) and \(|H|\) diverge.

The numerical endpoints in `step81_evolution.json` are:

\[
\begin{array}{c|ccccc}
k&2&3&4&6&8\\ \hline
r_{\max}&0.3624&0.3395&0.3160&0.2739&0.2407
\end{array}
\]
so the recorded interval is approximately \(0.24\)–\(0.36\). Values shown at \(r=0.5,1,2,3\) mostly repeat the terminal state and are not integrations beyond \(r_{\max}\). The file contains no entries for \(k=5,7\).

### Why the same proof does not transfer to \(z\)-dependent OT geometry

For a general reflected Einstein metric,
\[
H'=3-|S|^2,
\qquad
R(q_r)=-6+H^2-|S|^2,
\]
so
\[
H'=9-H^2+R(q_r).
\]
The VII\(_0\) proof uses the special identity
\[
R(q_r)=-K
\]
and the monotonicity of the single potential \(K\). In the full matrix system, \(R(q_r)\) contains area derivatives, matrix-map energy, and spatial derivatives; there is no supplied analogue of monotone \(K\).

For an exact scalar-\(-6\), constant-area center,
\[
u'(0,z)=-3
\]
everywhere. This determines only the first radial shape coefficient:
\[
u(r,z)=-3r+O(r^3).
\]
The slip changes the orbit part of \(S'(0)\) at order \(\varepsilon\), so its feedback into higher radial jets occurs earlier than the \(O(\varepsilon^2)\) change in \(u'(0)\).

The full orbit equation
\[
\operatorname{div}\bigl(\rho M^{-1}dM\bigr)=0
\]
allows radial and tangential matrix fluxes to redistribute locally, subject to
\[
\int_{S^1}\rho M^{-1}M_r\,dz=0
\]
from reflection. This removes the VII\(_0\) scalar monotonicity, but no constructed solution in the supplied material demonstrates avoidance of the finite singularity.

A separate exact-OT fact also matters: if \(M_r=0\) at the reflection face and \(M=P\) is exactly constant at a finite outer face, convexity of
\[
\frac12d_{\mathbb H^2}(M,P)^2
\]
forces \(M\equiv P\). Thus exact finite relaxation to an exactly constant orbit map is impossible. Approximate Einstein equations and an approximately constant outer map introduce weighted forcing terms, for which no decisive estimate is supplied.

---

## 6. Consequences for graph connectors

### Fixed VII\(_0\) ansatz

Step 78 proves that if
\[
\|\operatorname{Ric}+3g\|_{\mathrm{op}}\le\delta\le\frac35,
\]
then
\[
u<0,\qquad p>0,\qquad K>K_0\ge6-4\delta
\]
throughout every smooth positive-radius segment. Since an expanding tail requires \(u\approx1\), a connector remaining in this ansatz must satisfy
\[
\sup\|\operatorname{Ric}+3g\|_{\mathrm{op}}>\frac35
\]
somewhere before reaching the tail data. This is an order-one tensor estimate independent of the numerical singularity.

### General \(z\)-dependent geometry

No analogous estimate appears in the supplied equations or computations. The exact VII\(_0\) solution has \(E=0\) throughout its smooth inner segment while its shape contracts, so contraction itself does not create Ricci defect. An order-one defect follows only after proving that every small-defect route to expanding data inherits a monotone quantity or compatibility identity; none has been established for the full matrix system.

The Step 80 residual peak near \(r\approx0.2\) is not such an identity. That computation used a second-jet carrier while the estimated fourth jet had size about \(149\), a low Fourier truncation, and an averaged objective. Its sampled supremum therefore does not furnish a geometric lower bound.

### Available geometric mechanisms

- **Nonconstant orbit area:**  
  It changes the pointwise relation to
  \[
  u'(0)=-3+\dot h+h^2.
  \]
  The unweighted mean can become noncontracting only when
  \(\langle h^2\rangle_s\ge3\), while the center-volume-weighted mean remains \(-3\). This requires order-one area variation and the coupled relation
  \[
  e=12-4\dot h-3h^2.
  \]

- **Full OT matrix dependence on \((r,z)\):**  
  The angular-slip computation shows a genuine new tensor direction: scalar stress is unchanged to first order while orbit Ricci changes at first order. This mechanism is absent from fixed VII\(_0\), but no full connector has yet been exhibited.

- **Non-OT exact reflected geometry:**  
  Under a reflection that fixes the center and preserves the two commuting Killing fields, the twist scalars are constant for \(\operatorname{Ric}=-3g\) and reverse sign under reflection. They therefore vanish identically. Hence this mechanism is unavailable for an exact reflected \(T^2\)-symmetric core with the standard reflection action. For approximate equations, twist can accumulate from the Ricci defect over a long connector.

- **Non-reflected initial data:**  
  When \(S(0)\ne0\), the Hamilton relation is
  \[
  R(q_0)-H(0)^2+|S(0)|^2=-6,
  \]
  together with the Codazzi equations. The scalar-\(-6\) center and the universal value \(u'(0)=-3\) no longer follow. This is mathematically distinct from the reflected construction.

Accordingly, the supplied results establish an exact finite radial singularity and an order-one defect threshold for fixed VII\(_0\), but they do not establish an order-one defect threshold for general reflected \(T^2\)-invariant connectors.