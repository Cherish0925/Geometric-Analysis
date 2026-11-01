# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/trace/ttcs/results/step83_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Almost-Kähler-smoothings-of-compact-complex-surfaces-with-A-1-singulari--577e023dd490--0aaf7a1a8cdc/object.md"
  ]
}
```

## Task

Critically check the Step-83 no-concentration theorem and sharpen it for a one-level A1/Eguchi–Hanson degeneration of closed negative almost-Kähler Einstein four-manifolds. In particular: (i) verify the measure-defect sign argument and extension of the constant-length harmonic form across the orbifold point; (ii) decide exactly what convergence of the forms/torsion is available and what is not (especially normalized torsion direction); (iii) derive the linearized equations for an AKE pair (g_t,omega_t) at a Kähler–Einstein metric in a gauge that distinguishes complex/Kähler tangent directions from genuinely nonintegrable directions; and (iv) analyze what the Eguchi–Hanson core contributes, including its 3-dimensional L2 Einstein kernel and hyperkähler parallel forms. State any correction needed in Step 83 and formulate a rigorously scoped local normal-rigidity proposition whose missing weighted estimate is explicit. Do not infer full local rigidity merely from energy vanishing or action constancy.

## Output

# Scientific verification memo

## 1. Measure-defect argument and orbifold extension

The sign mechanism in Theorem 83.5 is correct.

Let \(U_{n,\delta}\) be the part of \(M\) converging to a \(\delta\)-neighborhood of the orbifold singular set, and define
\[
m_W=\lim_{\delta\downarrow0}\lim_n
\int_{U_{n,\delta}}|W_n^+|^2\,dV_{g_n}\ge 0.
\]
Since \(s=s_0\) is fixed and \(\operatorname{Vol}(U_{n,\delta})=O(\delta^4)\), the scalar term has no atom there. Smooth convergence elsewhere gives
\[
D(V)=\lim_nD(g_n)+m_W,
\qquad
\lim_nD(g_n)=D(V)-m_W.
\tag{1.1}
\]

For
\[
\tau_n=|W_{3,n}^+|^2+\frac{3q_n^2}{32},
\qquad q_n=|\nabla\omega_n|^2,
\]
define, after a subsequence,
\[
m_T=\lim_{\delta\downarrow0}\lim_n
\int_{U_{n,\delta}}\tau_n\,dV_{g_n}\ge0.
\]
Smooth convergence off the singular points gives
\[
\lim_nT_{\mathrm{AK}}(g_n)=T_{\mathrm{AK}}(V)+m_T.
\tag{1.2}
\]
The orbifold identity
\[
D(V)=T_{\mathrm{AK}}(V)
\tag{1.3}
\]
follows from the same local AAD identity and orbifold Stokes, once \(\omega_V\) is extended smoothly. Combining (1.1)–(1.3) with \(D(g_n)=T_{\mathrm{AK}}(g_n)\) yields
\[
T_{\mathrm{AK}}(V)+m_T
=T_{\mathrm{AK}}(V)-m_W,
\]
hence
\[
\boxed{m_W=m_T=0.}
\tag{1.4}
\]
No bubble energy identity is used. The opposing signs of the two measure defects are the entire mechanism.

### Extension of \(\omega_V\)

On compact subsets of \(V_{\mathrm{reg}}\), the pullbacks of \(\omega_n\) satisfy
\[
(d+d^*)\omega_n=0,\qquad |\omega_n|=\sqrt2,
\]
so interior elliptic estimates give smooth subsequential convergence to a bounded harmonic self-dual form \(\omega_V\).

In a lifted orbifold chart \(B^4\setminus\{0\}\), test the Hodge–de Rham equation against a smooth test form using a cutoff \(\chi_\varepsilon\). Boundedness of \(\omega_V\) gives an error bounded by
\[
C\int_{B_{2\varepsilon}\setminus B_\varepsilon}|d\chi_\varepsilon|
=O(\varepsilon^3).
\]
Thus \((d+d^*)\omega_V=0\) distributionally across the origin. Elliptic regularity for the smooth lifted orbifold metric gives a smooth \(\Gamma\)-invariant extension. Self-duality and
\[
|\omega_V|=\sqrt2
\]
persist by continuity. In particular,
\[
\omega_V\wedge\omega_V=2\,dV_{g_V},
\]
so the extension remains orbifold symplectic and defines an orbifold almost-Kähler structure.

The extension argument is therefore valid; the precise statement is convergence after oriented orbifold convergence maps and passage to a subsequence.

---

## 2. What convergence is actually obtained

For a one-level \(A_1\) degeneration with one Eguchi–Hanson core, the following conclusions are available.

### Bulk

After pullback by the convergence maps,
\[
(g_n,\omega_n)\longrightarrow (g_V,\omega_V)
\]
smoothly on every compact subset of \(V_{\mathrm{reg}}\). The form \(\omega_V\) extends smoothly over the \(A_1\) point as above.

### Torsion measures

Equation (1.4) implies the precise statements
\[
\lim_{\delta\downarrow0}\limsup_n
\int_{U_{n,\delta}}|W_{3,n}^+|^2\,dV_{g_n}=0,
\]
and
\[
\lim_{\delta\downarrow0}\limsup_n
\int_{U_{n,\delta}}|\nabla\omega_n|^4\,dV_{g_n}=0.
\tag{2.1}
\]
The two summands have no concentration separately because both are at least zero.

If the orbifold endpoint is Kähler–Einstein, then \(T_{\mathrm{AK}}(V)=0\), and therefore
\[
\int_M|W_{3,n}^+|^2\,dV_{g_n}\to0,
\qquad
\int_M|\nabla\omega_n|^4\,dV_{g_n}\to0.
\tag{2.2}
\]
Fixed volume also gives \(\|\nabla\omega_n\|_{L^2}\to0\).

### Eguchi–Hanson core

At the curvature scale \(r_n\),
\[
\tilde g_n=r_n^{-2}g_n,\qquad
\tilde\omega_n=r_n^{-2}\omega_n.
\]
After pointed gauges and a diagonal subsequence,
\[
(\tilde g_n,\tilde\omega_n)
\longrightarrow (g_{\mathrm{EH}},\Omega_\infty)
\]
smoothly on compact subsets. Here
\[
|\Omega_\infty|=\sqrt2,\qquad
d\Omega_\infty=0,\qquad
*_{g_{\mathrm{EH}}}\Omega_\infty=\Omega_\infty.
\]
Since \(m_W=0\),
\[
W^+_{g_{\mathrm{EH}}}=0.
\]
The harmonic-form Weitzenböck identity then gives
\[
\nabla^{g_{\mathrm{EH}}}\Omega_\infty=0.
\]
Thus the core is Eguchi–Hanson in the orientation for which its hyperkähler forms are self-dual.

With the curvature-operator norm used in Step 83, the core may still carry
\[
\int_{\mathrm{EH}}|W^-|^2\,dV=12\pi^2.
\]
Hence \(m_W=0\) does not make the core flat. It excludes the opposite orientation, for which this full Eguchi–Hanson curvature would appear in \(W^+\).

### What is not obtained

There is no canonical matching statement between the extended value \(\omega_V(p)\) and the parallel form \(\Omega_\infty\) at the ALE end. The two forms arise from separate compactness procedures. A weighted neck estimate is needed to identify their asymptotic directions.

Likewise, no convergence follows for
\[
\frac{\nabla\omega_n}{|\nabla\omega_n|},
\qquad
\frac{W_{3,n}^+}{|W_{3,n}^+|},
\]
where defined. These quantities become undefined at torsion zeros and can rotate where their magnitudes are very small. Even the normalized torsion measures
\[
\frac{\tau_n\,dV_{g_n}}{T_{\mathrm{AK}}(g_n)}
\]
are not controlled when \(T_{\mathrm{AK}}(g_n)\to0\): dividing by a vanishing total mass discards (2.1).

A simple neck model illustrates the issue. On a conformal cylinder of length \(L\), a unit vector can rotate by order one with speed \(O(L^{-1})\), while
\[
\int_0^L |u'(t)|^4\,dt=O(L^{-3})\to0.
\]
Thus vanishing \(L^4\) torsion energy does not identify the directions at the two ends of a long neck.

---

## 3. Linearized AKE equations at a Kähler–Einstein pair

Let
\[
\operatorname{Ric}_g=\lambda g,\qquad \lambda=\frac{s}{4}<0,
\]
and normalize \(\lambda\) so that scaling is removed. Write
\[
h=\dot g,\qquad \beta=\dot\omega,\qquad H=g^{-1}h.
\]
For a two-form \(\alpha\), set
\[
(H\!\cdot\!\alpha)(X,Y)
=\alpha(HX,Y)+\alpha(X,HY).
\]

Use Bianchi gauge
\[
B_gh=\delta h+\frac12d\operatorname{tr}h=0.
\]
The linearized Einstein equation is
\[
\Delta_Eh=0.
\tag{3.1}
\]
For fixed \(\lambda<0\), the trace and divergence equations reduce this to the TT slice
\[
\delta h=0,\qquad \operatorname{tr}h=0.
\tag{3.2}
\]

The linearizations of the almost-Kähler equations are:

1. Closedness:
   \[
   d\beta=0.
   \tag{3.3}
   \]

2. Self-duality:
   \[
   2\beta^-=\dot *\,\omega
   =*\left(\frac12\operatorname{tr}h\,\omega-H\!\cdot\!\omega\right).
   \tag{3.4}
   \]

3. Constant length:
   \[
   \langle\beta,\omega\rangle=\frac12\operatorname{tr}h.
   \tag{3.5}
   \]

The supplied Nagy paper, equation (5) and Theorem 1.6, records Koiso’s description for \(\lambda<0\):
\[
hJ=-Jh,\qquad \bar\partial h=0,\qquad \delta h=0.
\tag{3.6}
\]
For such an anti-Hermitian \(h\),
\[
H\!\cdot\!\omega=0.
\]
Equations (3.2)–(3.5) therefore reduce to
\[
\beta^- =0,\qquad
\langle\beta,\omega\rangle=0,\qquad
d\beta=0.
\tag{3.7}
\]
A closed self-dual form is harmonic, and on a Kähler surface
\[
\beta\in
\mathcal H^2_+(M)\cap\omega^\perp
=\operatorname{Re}H^{2,0}(M).
\tag{3.8}
\]

Consequently, modulo diffeomorphisms and scaling, the linearized AKE solution space splits as
\[
\boxed{
\bigl\{(h,0):h\in\mathscr E_{\mathrm{KE}}(g)\bigr\}
\oplus
\bigl\{(0,\beta):\beta\in\operatorname{Re}H^{2,0}(M)\bigr\}.
}
\tag{3.9}
\]

### Geometric meaning of the two summands

Define \(K_\beta\) by
\[
g(K_\beta X,Y)=\beta(X,Y).
\]
Differentiating \(\omega_t(X,Y)=g_t(J_tX,Y)\) gives
\[
\dot J=K_\beta-HJ.
\tag{3.10}
\]

- The \((h,0)\) directions are precisely the infinitesimal complex/Kähler–Einstein directions in the fixed-symplectic representative. Equation \(\bar\partial h=0\) is the linearized integrability equation.

- The \((0,\beta)\) directions are additional infinitesimal almost-Kähler directions. If such a direction were also infinitesimally integrable, then linearizing the identity “closed compatible form plus integrable complex structure implies \(\nabla\omega=0\)” would give
  \[
  \nabla\beta=0.
  \]
  A nonzero parallel \((2,0)\)-form is incompatible with \(\lambda<0\). Hence a nonzero \(\beta\) in (3.8) is genuinely nonintegrable at first order.

In this product gauge, the linearized torsion is
\[
\left.\frac{d}{dt}\right|_{0}\nabla^{g_t}\omega_t
=\nabla\beta.
\tag{3.11}
\]
Thus
\[
q_t=|\nabla\omega_t|^2
=t^2|\nabla\beta|^2+O(t^3).
\tag{3.12}
\]
The Step-77 energy contains \(q_t^2\), so this term begins at order \(t^4\). In the standard \(U(2)\)-decomposition of \(W^+\), the first-order rotation of the Kähler line enters \(W_2^+\); \(W_3^+\) begins at second order. Therefore \(T_{\mathrm{AK}}\) does not detect the normal directions (3.8) at the linear level. This is one reason energy vanishing alone does not provide a uniform local theorem near a degenerating Kähler configuration.

If \(H^{2,0}(M)=0\), the extra summand in (3.9) disappears. For an orbifold, the same statement uses orbifold harmonic forms and \(H^{2,0}_{\mathrm{orb}}(V)\).

---

## 4. The Eguchi–Hanson core modes

Ozuch’s supplied paper describes the \(L^2\) Einstein kernel of Eguchi–Hanson as three-dimensional:
\[
\mathbf O(g_{\mathrm{EH}})
=\operatorname{span}\{\mathbf o_1,\mathbf o_2,\mathbf o_3\},
\]
with
\[
\mathbf o_k=O_k^4+O(r^{-8}),\qquad
O_k^4=-\frac{\theta_1^-\circ\theta_k^+}{r^4}.
\tag{4.1}
\]
These are the infinitesimal variations of the three-parameter family
\[
g_{\mathrm{EH},\zeta^+},\qquad \zeta\in\mathbb R^3\setminus\{0\}.
\]
The radial \(\zeta\)-variation changes the Eguchi–Hanson size, while the two angular variations change its hyperkähler direction relative to the asymptotic frame. All three are genuine Ricci-flat ALE deformations.

Eguchi–Hanson also has a parallel self-dual triple
\[
\Omega_1,\Omega_2,\Omega_3,\qquad
\nabla\Omega_a=0,\qquad |\Omega_a|=\sqrt2.
\]
The bubble form has the form
\[
\Omega_\infty=a_1\Omega_1+a_2\Omega_2+a_3\Omega_3,
\qquad
a_1^2+a_2^2+a_3^2=1.
\tag{4.2}
\]
The coefficients depend on the subsequence and the ALE frame.

Relative to a selected \(\Omega_\infty\), the tangent space to the sphere of parallel Kähler forms is two-dimensional. These form rotations are bounded rather than \(L^2\). They must be treated separately from the three \(L^2\) metric modes.

Each metric mode in (4.1) can be paired with a variation of the parallel hyperkähler triple so that the resulting infinitesimal pair remains Kähler and torsion-free. Therefore:

- the three \(L^2\) modes are gluing/Kähler modes, not evidence for nonintegrability;
- the two transverse parallel-form rotations are also torsion-free on the isolated core;
- asymptotic matching to the bulk determines which combinations can occur globally;
- \(m_W=m_T=0\) does not remove any of these core modes.

This is the central analytic issue in passing from no concentration to uniform local normal rigidity.

---

## 5. Corrections to the Step-83 formulation

The mathematical core of Theorem 83.5 is valid. Its precise formulation should incorporate the following points.

1. “\(\omega_n\to\omega_V\) smoothly” means after pullback by the regular-region convergence maps and passage to a subsequence.

2. On each rescaled bubble, convergence of \(\tilde\omega_n\) is likewise subsequential and gauge-dependent.

3. The theorem yields unnormalized measure convergence:
   \[
   |W_{3,n}^+|^2dV_{g_n}\to |W_{3,V}^+|^2dV_{g_V},
   \qquad
   |\nabla\omega_n|^4dV_{g_n}\to|\nabla\omega_V|^4dV_{g_V},
   \]
   with no atom at the orbifold point. It yields no convergence of normalized torsion directions or normalized torsion probability measures.

4. In the one-level \(A_1\) case, the bubble is orientation-matched Eguchi–Hanson, but the theorem does not identify \(\Omega_\infty\) with \(\omega_V(p)\) in a common asymptotic frame.

5. The discussion of torsion-zero counts migrating into Kähler bubbles remains a proposed topological bookkeeping mechanism; no zero-count formula follows from Theorem 83.5.

6. Local constancy of the Einstein action applies near each individual smooth Einstein metric. Along a family approaching an orbifold, the size of those smooth neighborhoods may tend to zero. Infinitely many smooth Einstein components with positive deficits tending to zero remain compatible with Theorems 83.1 and 83.5.

Vernier’s supplied paper constructs almost-Kähler smoothings with constant Hermitian scalar curvature, not Einstein metrics. It therefore supplies neither an AKE Einstein branch nor the coupled weighted estimate described below.

---

## 6. A precise conditional normal-rigidity proposition

The following formulation isolates the analytic input absent from Step 83.

### Proposition — uniform normal rigidity near a one-level \(A_1\) Kähler branch

Let \((V,g_0,\omega_0)\) be a compact Kähler–Einstein four-orbifold with \(s<0\), one \(A_1\) point, and
\[
H^{2,0}_{\mathrm{orb}}(V)=0.
\tag{6.1}
\]
Assume there is a finite-dimensional family \(\mathcal K_\varepsilon\) of exact Kähler–Einstein desingularizations on \(M\), with one orientation-matched Eguchi–Hanson core and no lower bubble levels. Assume \(\mathcal K_\varepsilon\) parameterizes:

- the orbifold Koiso modes;
- the three transported Eguchi–Hanson \(L^2\) modes \(\mathbf o_1,\mathbf o_2,\mathbf o_3\);
- the compatible variations of the selected parallel hyperkähler form.

For \(z=(g_\varepsilon^K,\omega_\varepsilon^K)\in\mathcal K_\varepsilon\), consider the gauge-fixed AKE map
\[
\mathcal F_{\varepsilon,z}(g,\omega)=
\left(
\operatorname{Ric}_g-\lambda g+\delta_g^*B_{g_\varepsilon^K}g,\;
d\omega,\;
P_g^-\omega,\;
|\omega|_g^2-2
\right).
\tag{6.2}
\]
Its nearby zeros are normalized almost-Kähler Einstein pairs.

Let \(\rho_\varepsilon\) be the standard orbifold/ALE radius, and define
\[
\|u\|_{C^{k,\alpha}_\delta}
=
\sum_{j=0}^k
\sup \rho_\varepsilon^{\,j-\delta}|\nabla^ju|
+\text{weighted Hölder term}.
\]
Set
\[
X_\delta=
C^{2,\alpha}_\delta(S^2T^*M)
\oplus
C^{1,\alpha}_\delta(\Lambda^2T^*M),
\]
with the corresponding mixed-order target \(Y_\delta\), using weights \(\delta-2\) for the Einstein component, \(\delta-1\) for \(d\beta\), and \(\delta\) for the algebraic components.

Suppose there are \(\delta\), \(C\), and \(\varepsilon_0>0\), independent of \(\varepsilon\), such that
\[
\begin{aligned}
\|(h,\beta)\|_{X_\delta}
\le C\Bigg(&
\|D\mathcal F_{\varepsilon,z}(h,\beta)\|_{Y_\delta}\\
&+\sum_j|\langle h,k_j\rangle_{L^2(V)}|
+\sum_{i=1}^3|\langle \tilde h,\mathbf o_i\rangle_{L^2(\mathrm{EH})}|
+\sum_{a=2}^3|\mathfrak m_a(\tilde\beta)|
\Bigg),
\end{aligned}
\tag{6.3}
\]
where:

- \(k_j\) are the orbifold Koiso modes;
- \((\tilde h,\tilde\beta)\) are the rescaled core fields;
- \(\mathfrak m_2,\mathfrak m_3\) are the coefficients of the two parallel forms transverse to the selected \(\Omega_\infty\), measured on a fixed rescaled neck cross-section.

Assume also the uniform Taylor estimate
\[
\|\mathcal F_{\varepsilon,z}(z+u)
-\mathcal F_{\varepsilon,z}(z)
-D\mathcal F_{\varepsilon,z}u\|_{Y_\delta}
\le C\|u\|_{X_\delta}^2.
\tag{6.4}
\]

Then there are \(\rho>0\) and \(\varepsilon_1>0\), independent of \(\varepsilon\), such that every normalized AKE Einstein pair within weighted distance \(\rho\) of \(\mathcal K_\varepsilon\), for \(0<\varepsilon<\varepsilon_1\), belongs to \(\mathcal K_\varepsilon\). In particular, it is Kähler–Einstein.

### Proof

Modulation by the parameters of \(\mathcal K_\varepsilon\) makes the finite-dimensional terms in (6.3) vanish. Write the pair as \(z+u\) with \(u\) orthogonal to the displayed modes. Since both the given pair and \(z\) solve (6.2),
\[
D\mathcal F_{\varepsilon,z}u
=
-\bigl[\mathcal F_{\varepsilon,z}(z+u)
-\mathcal F_{\varepsilon,z}(z)
-D\mathcal F_{\varepsilon,z}u\bigr].
\]
Equations (6.3)–(6.4) give
\[
\|u\|_{X_\delta}\le C'\|u\|_{X_\delta}^2.
\]
For \(\|u\|_{X_\delta}<1/(2C')\), this forces \(u=0\).

### The unresolved analytic object

The absent input is the uniform estimate (6.3), especially its control of:

1. slow rotations on the long neck;
2. the two bounded parallel-form rotations on Eguchi–Hanson;
3. the three \(L^2\) Einstein core modes after gluing-parameter modulation.

If \(H^{2,0}_{\mathrm{orb}}(V)\neq0\), additional moments
\[
\langle\beta,\phi_\ell\rangle,
\qquad
\phi_\ell\in\operatorname{Re}H^{2,0}_{\mathrm{orb}}(V),
\]
must be added to (6.3), followed by a finite-dimensional reduced equation for those normal modes. The linearized equations alone leave these modes present, and neither \(T_{\mathrm{AK}}\to0\) nor action constancy computes that reduced equation.

Thus Step 83 establishes a strong no-concentration theorem and identifies the Kähler nature of every bubble, but uniform normal rigidity at the one-level \(A_1\) configuration rests on the coupled weighted estimate and finite-dimensional matching described above.