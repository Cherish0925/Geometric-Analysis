# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 84,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step84_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step84_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Critically check the Step-83 no-concentration theorem and sharpen it for a one-level A1/Eguchi–Hanson degeneration of closed negative almost-Kähler Einstein four-manifolds. In particular: (i) verify the measure-defect sign argument and extension of the constant-length harmonic form across the orbifold point; (ii) decide exactly what convergence of the forms/torsion is available and what is not (especially normalized torsion direction); (iii) derive the linearized equations for an AKE pair (g_t,omega_t) at a Kähler–Einstein metric in a gauge that distinguishes complex/Kähler tangent directions from genuinely nonintegrable directions; and (iv) analyze what the Eguchi–Hanson core contributes, including its 3-dimensional L2 Einstein kernel and hyperkähler parallel forms. State any correction needed in Step 83 and formulate a rigorously scoped local normal-rigidity proposition whose missing weighted estimate is explicit. Do not infer full local rigidity merely from energy vanishing or action constancy.

## Integrated Scientific Memo

# Verification memo: no concentration, AKE linearization, and an \(A_1\)/Eguchi–Hanson core

**Theorem 83.5’s measure-defect mechanism is correct.** It proves smooth subsequential convergence on the regular bulk and on fixed rescaled bubble regions, removability of the limiting form, and absence of **absolute** self-dual Weyl and torsion-energy concentration. It does **not** prove convergence of normalized torsion, uniform weighted closeness of the pairs, or local rigidity at an orbifold endpoint.

The one-level \(A_1\) case identifies the relevant additional modes: three \(L^2\) Eguchi–Hanson metric modes and two bounded parallel-form rotations. They are torsion-free on the isolated core, but their global matching equations cannot be discarded. Below is a corrected conditional normal-rigidity statement with that issue explicit.

## 1. The sign argument and removable singularity

Use the conventions of Step 83:
\[
q=|\nabla\omega|^2,\qquad
t_{\rm AK}=|W_3^+|^2+\frac{3}{32}q^2,\qquad
D=\int\left(\frac{s^2}{24}-|W^+|^2\right)dV.
\]
The inherited AAD identity is \(D=T_{\rm AK}=\int t_{\rm AK}\).

Let \(U_{n,\delta}\) denote the shrinking region corresponding to a \(\delta\)-neighborhood of the singular point. Fixed scalar curvature and volume convergence give
\[
\lim_n\int_M|W_n^+|^2\,dV_n
=\int_V|W_V^+|^2\,dV_V+m_W,\qquad m_W\ge0,
\]
and hence
\[
\lim_nD(g_n)=D(V)-m_W.                                      \tag{1}
\]
The sign is important: losing a nonnegative Weyl integral **increases** the bulk deficit.

Smooth convergence away from the point, together with positivity of \(t_{\rm AK}\), gives
\[
\lim_nT_{\rm AK}(g_n)=T_{\rm AK}(V)+m_T,\qquad m_T\ge0.       \tag{2}
\]
Existence of the total-energy limit follows from (1) and \(T_{\rm AK}(g_n)=D(g_n)\).

Once the form extends smoothly, the same local AAD differential identity integrates on the compact orbifold:
\[
D(V)=T_{\rm AK}(V).                                        \tag{3}
\]
This uses orbifold Stokes, not ordinary characteristic numbers of the underlying singular space. Combining (1)–(3),
\[
T_{\rm AK}(V)+m_T=T_{\rm AK}(V)-m_W,
\]
so
\[
\boxed{m_W=m_T=0.}                                        \tag{4}
\]
Equivalently, Fatou alone yields
\[
T_{\rm AK}(V)\le\lim_nT_{\rm AK}(g_n)=T_{\rm AK}(V)-m_W,
\]
which forces both equality and \(m_W=0\). No bubble-energy identity or neck-energy theorem is needed.

### Extension of the form

After oriented convergence maps and a subsequence, harmonicity and \(|\omega_n|=\sqrt2\) give interior elliptic estimates and
\[
\omega_n\longrightarrow\omega_V
\quad\text{in }C^\infty_{\rm loc}(V_{\rm reg}).
\]
Lift to a smooth orbifold chart \(B^4\setminus\{0\}\). The lifted form is bounded and satisfies
\[
(d+d^*)\omega_V=0.
\]
A cutoff supported on \(B_{2\varepsilon}\), with derivative \(O(\varepsilon^{-1})\), produces a distributional error bounded by
\[
C\|\omega_V\|_\infty\int_{B_{2\varepsilon}\setminus B_\varepsilon}
|d\chi_\varepsilon|=O(\varepsilon^3).
\]
Thus the equation holds across \(0\) distributionally. Elliptic regularity for the smooth lifted metric yields a smooth, invariant extension. Closedness, self-duality, and length pass by continuity; in particular,
\[
\omega_V\wedge\omega_V=2\,dV_V.
\]
The extension is genuinely orbifold symplectic. For \(A_1\), the action \(-1\) is trivial on two-forms and imposes no extra restriction on \(\omega_V(p)\).

**Correction to Step 83:** the integrated AAD identity is not merely a pointwise curvature identity; its divergence terms must be integrated. The smooth extension and orbifold Stokes supply exactly the required justification.

## 2. Exact scope of convergence

### Statements proved by Theorem 83.5

Under the stated noncollapsed orbifold convergence:

* \((g_n,\omega_n,J_n)\) converge smoothly on compact subsets of \(V_{\rm reg}\), after pullback and subsequence.
* The quadratic curvature and torsion measures have no defect at the singular point.
* Since the torsion summands are nonnegative, separately
  \[
  \lim_{\delta\downarrow0}\limsup_n\int_{U_{n,\delta}}
  |W_{3,n}^+|^2\,dV_n=0,\qquad
  \lim_{\delta\downarrow0}\limsup_n\int_{U_{n,\delta}}
  |\nabla\omega_n|^4\,dV_n=0.                              \tag{5}
  \]
  The same applies to shrinking necks contained in these regions.
* At a curvature scale \(r_n\to0\), set
  \[
  g_n'=r_n^{-2}g_n,\qquad \omega_n'=r_n^{-2}\omega_n.
  \]
  Both self-duality and length \(\sqrt2\) are preserved. On fixed compact subsets of a smooth pointed bubble,
  \[
  (g_n',\omega_n')\longrightarrow(g_b,\Omega_b)
  \quad\text{smoothly},
  \]
  with \(\operatorname{Ric}_{g_b}=0\) and \(W_b^+=0\).

The self-dual Weitzenböck formula is
\[
0=\nabla^*\nabla\Omega_b+\frac{s_b}{3}\Omega_b
       -2W_b^+(\Omega_b).
\]
Its constant-length consequence gives \(\nabla\Omega_b=0\). Thus an Eguchi–Hanson bubble must have the hyperkähler orientation inherited from \(M\).

If the endpoint pair is Kähler–Einstein, then
\[
\|W_{3,n}^+\|_{L^2}\to0,\qquad
\|\nabla\omega_n\|_{L^4}\to0.
\]
Bounded total volume also gives \(\|\nabla\omega_n\|_{L^2}\to0\).

### Statements not proved

1. **Unrescaled pointwise torsion need not tend to zero on the core.** Smooth rescaled convergence says, on a fixed rescaled compact set,
   \[
   r_n|\nabla\omega_n|_{g_n}\to0,
   \]
   not \(|\nabla\omega_n|_{g_n}\to0\).

2. **Normalized torsion has no established compactness.** Neither
   \[
   \frac{\nabla\omega_n}{|\nabla\omega_n|},
   \qquad
   \frac{\nabla\omega_n}{\|\nabla\omega_n\|_{L^4}},
   \qquad
   \frac{t_{{\rm AK},n}\,dV_n}{T_{\rm AK}(g_n)}
   \]
   is controlled by (5). Pointwise directions are undefined at zeros. If total torsion tends to zero, an arbitrarily large fraction of that vanishing energy can lie in a shrinking neck or core.

3. **The bulk and core parallel-form directions are not identified by the defect argument.** It constructs \(\omega_V(p)\) and \(\Omega_b\) through different convergence maps. Matching them requires a common asymptotic frame and a harmonic-form neck estimate.

The assertion that an indicial gap automatically supplies this matching is an unfinished argument, not a theorem established in the supplied texts. In particular, “even harmonic coefficients” is not a sufficient indicial analysis: \(d\omega=0\), self-duality, gauge identifications, and the perturbed neck operator must all be included.

A useful precise matching estimate would be
\[
\lim_{\delta\downarrow0}\limsup_n
\sup_{Rr_n<r<\delta}
|\omega_n-A_n|_{\rm frame}=0
\quad\text{as }R\to\infty,                                \tag{6}
\]
where \(A_n\) is a **single** constant self-dual form on the whole neck. This would identify the ALE asymptotic value with \(\omega_V(p)\).

There is a credible route to (6): separate the flat closed/self-dual operator’s constant-form modes from its nonzero indicial modes, and bound their coupling by an integrable-in-\(d\log r\) metric error. Merely uniform smallness on a neck of diverging logarithmic length does not suffice. Ozuch’s decoupled norms are relevant to this route, but the supplied paper does not state or prove the requisite form estimate.

Accordingly, replace “torsion never escapes into bubbles” by:

> No positive amount of the unnormalized torsion energy is lost into any shrinking bubble or neck region.

## 3. Linearized AKE equations at a negative KE pair

Let
\[
\operatorname{Ric}_g=Eg,\qquad E=s/4<0,\qquad
\omega(X,Y)=g(JX,Y).
\]
Fix \(E\), removing scaling, and write
\[
h=\dot g,\qquad H=g^{-1}h,\qquad \beta=\dot\omega.
\]
Use Bianchi gauge
\[
B_gh=\delta h+\frac12d\operatorname{tr}h=0.
\]
With the Einstein operator convention in Nagy,
\[
\Delta_E=\nabla^*\nabla-2\mathring R,
\]
the metric equation is
\[
\Delta_Eh=0.
\]
Taking its trace gives \((\Delta-2E)\operatorname{tr}h=0\); negativity of \(E\) forces
\[
\operatorname{tr}h=0,\qquad\delta h=0.                     \tag{7}
\]

For a two-form, define
\[
(H\cdot\alpha)(X,Y)=\alpha(HX,Y)+\alpha(X,HY).
\]
The remaining linearized equations are
\[
d\beta=0,                                                  \tag{8}
\]
\[
2\beta^-=\dot *\,\omega
=*\left(\frac12\operatorname{tr}h\,\omega-H\cdot\omega\right),\tag{9}
\]
\[
\langle\beta,\omega\rangle=\frac12\operatorname{tr}h.        \tag{10}
\]
Equation (10) follows by differentiating \(|\omega|_g^2=2\); the metric variation of the squared norm is \(-\operatorname{tr}h\).

### Complex/Kähler versus normal directions

Nagy §4.1 records the negative-KE decomposition:
\[
\ker\Delta_E\cap\operatorname{Sym}^{2,+}=0,
\]
\[
\mathscr E(g)=
\{h:hJ=-Jh,\ \bar\partial h=0,\ \delta h=0\}.               \tag{11}
\]
For anti-Hermitian \(H\), \(H\cdot\omega=0\). Equations (8)–(10) reduce to
\[
d\beta=0,\qquad\beta^- =0,\qquad\beta\perp\omega
\quad\text{pointwise}.
\]
On a Kähler surface this is precisely the real space of holomorphic two-forms. Therefore, modulo simultaneous diffeomorphisms and scaling,
\[
\boxed{
\ker L_{\rm AKE}
=\{(h,0):h\in\mathscr E(g)\}
 \oplus\{(0,\beta):\beta\in\operatorname{Re}H^{2,0}(M)\}.
}                                                         \tag{12}
\]
The orbifold version uses smooth invariant tensors and \(H^{2,0}_{\rm orb}(V)\).

If \(K_\beta\) is defined by \(g(K_\beta X,Y)=\beta(X,Y)\), then
\[
\dot J=K_\beta-HJ.                                        \tag{13}
\]
The first summand in (12) consists of **infinitesimally integrable complex directions**. It need not integrate to an actual complex or KE family: complex deformations can be obstructed.

For these directions, the linearized Kähler equation is satisfied. Explicitly, if
\[
2g(C_h(X)Y,Z)
=(\nabla_Xh)(Y,Z)+(\nabla_Yh)(X,Z)-(\nabla_Zh)(X,Y),
\]
then
\[
\dot{\nabla\omega}(X;Y,Z)
=(\nabla_X\beta)(Y,Z)
-\omega(C_h(X)Y,Z)-\omega(Y,C_h(X)Z).
\]
The last two terms cancel for \(h\) satisfying (11). Consequently, on (12),
\[
\boxed{\dot{\nabla\omega}=\nabla\beta.}                    \tag{14}
\]

A nonzero \(\beta\in\operatorname{Re}H^{2,0}\) cannot be parallel when \(E<0\): a parallel holomorphic volume form would force the Ricci form to vanish. Thus the second summand consists of genuinely nonintegrable first-order pair directions.

This also explains why the energy identity is weak at linear order:
\[
q_t=t^2|\nabla\beta|^2+O(t^3),\qquad q_t^2=O(t^4).
\]
At a KE metric, \(W_3^+\) has zero first variation along (12): the KE metric modes satisfy the linearized Kähler curvature identities, while a first-order rotation of the Kähler line enters the off-diagonal \(W_2^+\) component, not \(W_3^+\). Hence \(T_{\rm AK}\) has no coercive quadratic term on these normal form modes.

### What Nagy’s second-order result does—and does not—give

In Nagy’s pointwise volume-form gauge,
\[
g^{-1}g_t=I+tH_1+\frac{t^2}{2}H_2+\cdots,
\qquad H_2^+=H_1^2.
\]
Direct expansion shows
\[
(g_t^{-1}\omega)^2=-I+O(t^3).
\]
Thus the fixed form \(\omega\) remains algebraically compatible to second order. This is a substantive connection between Einstein jets and almost-Kähler jets.

It is **not** automatic second-order complex integrability. Nagy Remark 4.22 identifies a potentially nonzero harmonic Maurer–Cartan obstruction
\[
\bar\partial\mathbf h_2+[h_1,h_1]^c,
\]
in the paper’s complex-deformation parametrization. Numerical factors must be translated before substituting metric Taylor coefficients.

No general second-order obstruction formula for mixed \((h,\beta)\) directions was established by either derivation. In particular, the proposed exact self-dual correction and its claimed solvability should not be used without a separate proof.

## 4. What the Eguchi–Hanson core contributes

### Curvature and topology

In the permitted orientation,
\[
\operatorname{Ric}_{\rm EH}=0,\qquad W_{\rm EH}^+=0,
\]
but \(W_{\rm EH}^-\neq0\). In the curvature-operator normalization of Step 83, ALE Gauss–Bonnet gives
\[
\int_{\rm EH}|W^-|^2\,dV
=8\pi^2\left(2-\frac12\right)=12\pi^2.
\]
Thus no \(W^+\) concentration does not mean no curvature concentration.

The bolt/vanishing sphere has self-intersection \(-2\). Replacing one \(A_1\) neighborhood by this core adds one negative second-homology direction. The ALE contribution to the curvature expression for \(2\chi+3\tau\) is zero, consistent with
\[
T_+^{\rm curv}(V)=T_+(M).
\]

One may say that a reversed EH bubble would contribute positive \(W^+\) energy and is excluded. One should not assert \(m_W\in\{0,12\pi^2\}\) for a general one-level convergence **without** additionally invoking a complete curvature-energy identity eliminating other neck defects. The sign argument avoids that requirement.

### Three \(L^2\) Einstein modes

Ozuch §1.2.2 supplies
\[
\ker_{L^2}P_{\rm EH}
=\operatorname{span}\{\mathbf o_1,\mathbf o_2,\mathbf o_3\},
\qquad
P_{\rm EH}=\tfrac12\Delta_E,
\]
with
\[
\mathbf o_k=-r^{-4}\theta_1^-\circ\theta_k^+
             +O(r^{-8}).                                  \tag{15}
\]
They are the three variations of the framed ALE parameter
\(\zeta\in\mathbb R^3\setminus\{0\}\): one size and two angular directions.

Let \(\Theta\) generate the ASD \(L^2\) harmonic two-forms, and let
\(\Omega_1,\Omega_2,\Omega_3\) be a parallel self-dual hyperkähler triple. Intrinsically the kernel is represented by
\[
\Theta\circ\Omega_i.
\]
For a selected Kähler form \(\Omega_a\):

* \(\Theta\circ\Omega_a\) is Hermitian;
* the two perpendicular compositions are anti-Hermitian.

All three admit compatible hyperkähler pair deformations and therefore have zero linearized torsion. **Anti-Hermitian does not mean nonintegrable**: the two anti-Hermitian core modes are complex deformation directions.

There is an important global correction to the first proposed rigidity formulation: all three core modes cannot simply be assumed to be freely modulatable parameters of exact negative KE desingularizations. At fixed \(E\), an exact KE pair satisfies
\[
E[\omega]=2\pi c_1.
\]
On a crepant \(-2\) vanishing class, this forces zero symplectic period. The core Hermitian area-changing mode is consequently constrained by global period/matching equations, rather than automatically being tangent to an exact KE branch.

### Parallel forms are a separate, non-\(L^2\) sector

The bubble form is
\[
\Omega_b=a_i\Omega_i,\qquad |a|=1.
\]
Its fixed-length parallel-form variations form a two-dimensional tangent space to \(S^2\). They are bounded, nondecaying, and not \(L^2\).

There are no nonzero decaying self-dual harmonic forms on EH: since \(W^+=s=0\), their squared norm is subharmonic; decay and the maximum principle force vanishing. The ASD form \(\Theta\) does not supply an independent normal self-dual form mode.

Thus the isolated core supplies **no new nonintegrable decaying linear pair mode**, but it supplies metric kernel modes and bounded form modes that can defeat a uniform inverse unless correctly matched.

### Smoothing geometry: a conditional consequence

Ozuch’s first obstruction selects the framed EH parameter direction:
\[
R_V^+(p)\widehat\zeta=0.
\]
Its applicability requires the stated gluing-framework hypotheses; the supplied higher-order paper assumes integrable orbifold Einstein deformations.

At a KE point,
\[
R_V^+=W_V^++\frac{s}{12}I
=\operatorname{diag}(E,0,0)
\]
with nonzero eigenline \(\mathbb R\omega_V(p)\). **If neck matching (6) holds**, then
\[
\widehat\zeta\perp\Omega_b(\infty).
\]
The bolt is then Lagrangian for the selected limiting hyperkähler form: this is the smoothing configuration described by Vernier, not the holomorphic exceptional-divisor configuration for that selected complex structure. The second displayed curvature obstruction is automatic for this rank-one KE curvature.

Without form matching, orthogonality to \(\omega_V(p)\) does not yet establish orthogonality to the selected bubble form. Also, this limiting conclusion does not make every finite-\(n\) sphere exactly Lagrangian.

Vernier constructs constant **Hermitian scalar curvature** AK smoothings, not Einstein smoothings. Her fourth-order scalar inverse is not an inverse for the coupled AKE system.

## 5. A rigorously scoped local normal-rigidity proposition

Here is a formulation that does not suppress constrained core modes or assume unobstructed complex deformation theory.

### Conditional proposition

Let \((V,g_0,\omega_0)\) be a compact negative KE orbifold with one \(A_1\) point. Suppose a family \(\mathcal K_\varepsilon\) of **exact** KE pairs on \(M\) has a one-level, orientation-matched EH degeneration to this pair.

Assume:

1. Near \(\mathcal K_\varepsilon\), simultaneous diffeomorphism gauge and modulation along its **actual** tangent parameters define a uniformly controlled normal slice.
2. There are decoupled orbifold/ALE weighted spaces \(X_\delta,Y_\delta\), an admissible weight, and \(C\) independent of \(\varepsilon\), for which the gauge-fixed AKE linearization satisfies
   \[
   \boxed{
   \|u\|_{X_\delta}\le C\|L_{\varepsilon,z}u\|_{Y_\delta},
   \qquad u\in N_z\mathcal K_\varepsilon .
   }                                                       \tag{16}
   \]
3. In the same coordinates, the nonlinear remainder satisfies
   \[
   \|\mathcal F_{\varepsilon,z}(z+u)
     -\mathcal F_{\varepsilon,z}(z)-L_{\varepsilon,z}u\|_{Y_\delta}
   \le C\|u\|_{X_\delta}^2.                                \tag{17}
   \]

Then a weighted neighborhood of radius independent of \(\varepsilon\) contains no strict AKE pair: every AKE zero in that neighborhood belongs to \(\mathcal K_\varepsilon\).

**Proof.** Modulate to write the pair as \(z+u\) in the normal slice. Both pairs solve the AKE equations, so (16)–(17) imply
\[
\|u\|_{X_\delta}\le C^2\|u\|_{X_\delta}^2.
\]
Uniformly sufficiently small \(u\) must vanish. This proves normal rigidity, not isolation of the metric.

### Explicit operator and missing estimate

On the Bianchi slice, use
\[
\mathcal F(g,\omega)=
\left(
\operatorname{Ric}_g-Eg+\delta_g^*B_{g_z}g,\;
d\omega,\;
P_g^-\omega,\;
|\omega|_g^2-2
\right).
\]
At a KE pair,
\[
L(h,\beta)=
\left(
\tfrac12\Delta_Eh,\;
d\beta,\;
\beta^--\tfrac12\dot *\,\omega,\;
2\langle\beta,\omega\rangle-\operatorname{tr}h
\right).                                                  \tag{18}
\]
One possible mixed-order choice is decoupled \(C^{2,\alpha}_\delta\) norms for both fields, with targets \(C^{0,\alpha}_{\delta-2}\) for the metric equation, \(C^{1,\alpha}_{\delta-1}\) for closedness, and \(C^{2,\alpha}_\delta\) for algebraic constraints. The norms must explicitly separate constant neck tensors and bounded self-dual form modes; plain positive-weight norms do not capture them correctly.

The unknown in (16) is a **uniform normal estimate through the long neck**, including:

* bulk \(\operatorname{Re}H^{2,0}_{\rm orb}(V)\) modes;
* all three transported EH \(L^2\) metric modes;
* the two transverse parallel-form modes;
* their period and asymptotic matching equations.

Only modes genuinely tangent to \(\mathcal K_\varepsilon\) may be removed by modulation. Adding moments for the other modes gives an inverse **modulo a finite-dimensional space**, not rigidity. Their reduced equations must then be shown to eliminate non-Kähler solutions. The assumption \(H^{2,0}_{\rm orb}(V)=0\) removes one bulk obstruction sector, but does not prove the remaining uniform estimate.

Finally, the proposition is deliberately weighted-local. To obtain a statement for all GH-near one-level AKE pairs, one also needs a theorem placing those pairs in its uniform weighted neighborhood. Step 83 supplies no such theorem for the forms.

### An alternative scalar hypothesis

If an Einstein-modulo-obstructions construction is available, a different sufficient input is a uniform inequality
\[
|\widehat S(\hat g_{\zeta,v})^2-\widehat S(V)^2|^{1-\theta}
\le C\|\mathcal O(\zeta,v)\|_{\rm weighted}.                \tag{19}
\]
At exact Einstein zeros this gives exact action equality; for the matched \(A_1\) topology and a KE bulk, \(D=0\), so every AKE pair is Kähler.

But (19) is itself unproved. The supplied sources do not establish analytic continuation across the degenerate parameter, identify the obstruction map with the gradient of this squared-action function, or prove definability. Ozuch’s logarithmic matching terms make an unsupported appeal to ordinary analyticity especially inappropriate.

## Conclusion

Step 83 establishes a strong closure theorem:
\[
\boxed{\text{AKE bulk extension}+\text{no absolute }W^+\text{/torsion defect}
+\text{torsion-free, orientation-matched bubbles}.}
\]
The unresolved object is not another energy identity. It is quantitative control of the **coupled pair and its normal modes across the neck**, together with the finite-dimensional period/matching equations.

Neither \(T_{\rm AK}(g_n)\to0\), nor Kähler bubble limits, nor action constancy on individual smooth Einstein components supplies that control. These facts leave open strict AKE components whose deficits tend to zero while accumulating at the orbifold stratum.