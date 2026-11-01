# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Consider the following mathematical problem arising in the negative branch of Yau Problem 26.

We seek a complete, non-ASD Einstein metric on ℝ × T³ with Ric = -3g that has two Poincaré-Einstein (PE) ends and a totally geodesic T³ center (equivalently, a reflected half-core on [0,∞) × T³ with S(0)=0 and PE at infinity). The ASD obstruction rules out Li-Liu-type fillings. The conformal infinity satisfies R_γ < -12.

Generate concrete mathematical mechanisms or structural arguments addressing:

(A) EXISTENCE/NON-EXISTENCE: Are there known results about non-ASD PE Einstein metrics on (0,∞) × T³? Anderson's boundary theory gives Fredholm index 0 for the PE boundary map. For the Li-Liu ASD sector, the Toda equation uniquely determines the filling. What is the dimension of the non-ASD moduli? Is there a parity or topological argument for/against non-ASD fillings?

(B) FORWARD EVOLUTION: From center data (q₀, S=0) with R(q₀)=-6 on T³, the Einstein evolution is well-posed after DeTurck gauge-fixing. Under what conditions does the forward evolution produce a PE end (rather than a singularity)? The pure cosh warped product requires Ric(q₀) = -2q₀, impossible on T³ by Preissmann. So the evolution is genuinely anisotropic. What structural conditions on q₀ control the long-time behavior?

(C) OBSTRUCTION MECHANISMS: Could a Bochner-type, index-theory, or topological argument prove that NO reflected Einstein core exists on ℝ × T³? The Witten-Yau one-endedness doesn't apply (negative Yamabe). The integrated shear identity R_γ = -12 - 4∫e^{2r}|S-I|²dr provides quantitative constraints. Is there a global monotonicity or Pohozaev-type identity that separates reflected centers from PE ends?

(D) DEFECT-BASED ALTERNATIVE: If no exact reflected core exists, could a family of approximate Einstein metrics with defect → 0 still work for the graph construction? The tail mechanism can flatten anisotropy at vanishing cost. If an exact obstruction exists, it might not extend to approximate metrics (analogous to how nearby Einstein metrics don't exist but the manifold might carry a distant Einstein metric).

Develop the most promising ideas with concrete mathematical content, equations, and testable predictions.

## Output

A useful way to view the reflected half-core is as an index-zero scattering problem between two “two-function” data sets:

\[
(q_0,\ S(0)=0,\ R(q_0)=-6)
\quad\longrightarrow\quad
(\gamma,\ g_3),
\]

where \(q_0\) is the center metric on \(T^3\), \(\gamma\) is the canonical PE infinity representative determined by the center distance \(r\), and \(g_3\) is the TT holographic datum.

## A. Non-ASD PE fillings: expected moduli and topology

For a four-dimensional PE Einstein metric in geodesic form,

\[
g=dr^2+q_r,\qquad \operatorname{Ric}_g=-3g,
\]

the expansion at infinity is

\[
q_r=e^{2r}\Big(\gamma-\operatorname{Sch}(\gamma)e^{-2r}
+g_3e^{-3r}+O(e^{-4r})\Big),
\]

with

\[
\operatorname{tr}_\gamma g_3=0,\qquad \operatorname{div}_\gamma g_3=0.
\]

Modulo diffeomorphism and conformal rescaling, \(\gamma\) has two local functional degrees of freedom in dimension three. A TT tensor \(g_3\) also has two local functional degrees of freedom, but for an actual filling \(g_3\) is selected by the nonlinear filling map. Thus Anderson’s Fredholm index-zero picture says: for a regular filling, the map

\[
\Pi:\{\text{PE Einstein fillings modulo diffeo}\}\to
\{\text{conformal infinities}\}
\]

has index zero. For fixed \(\gamma\), local fillings are governed by the kernel of the gauged Lichnerowicz operator; generically this kernel is zero, so fixed-\(\gamma\) fillings are isolated. With \(\gamma\) free, the moduli is infinite-dimensional in the same functional size as conformal infinity.

The center side has the same count. At \(r=0\),

\[
S(0)=0,\qquad R(q_0)=-6.
\]

A three-metric has six components; quotienting by \(\operatorname{Diff}(T^3)\) removes three; the scalar equation removes one. Again two functional degrees remain. So the reflected-center shooting problem is dimensionally balanced, not visibly ruled out by a parity count.

The ASD sector is special. For self-dual or anti-self-dual PE four-metrics, the TT datum is not free: in standard PE formulas it is tied to the Cotton-York tensor of \(\gamma\), up to orientation and normalization conventions. Equivalently, the ASD sheet is a special graph

\[
g_3=\mathcal C_{\mathrm{ASD}}(\gamma),
\]

rather than the general PE response. The Li-Liu Toda construction lies on such a chiral sheet and gives one PE end plus one cusp end. A reflected center cannot lie in this sheet, because reflection reverses orientation and would force both chiral Weyl halves to vanish, hence constant sectional curvature, incompatible with a totally geodesic \(T^3\).

Topologically, there is no immediate parity obstruction to non-ASD fillings on \(\mathbb R\times T^3\). The full reflected metric has \(\chi=0\) and \(\tau=0\). The Chern-Gauss-Bonnet identity for an Einstein PE four-manifold with a totally geodesic compact face gives schematically

\[
8\pi^2\chi
=
\int |W|^2\,dV+6V_{\mathrm{ren}},
\]

with no compact-face term when the face is totally geodesic. Since \(\chi=0\),

\[
V_{\mathrm{ren}}=-\frac16\int |W|^2\,dV.
\]

This enforces \(V_{\mathrm{ren}}\le0\), with strict inequality away from the locally hyperbolic case, but it does not eliminate non-ASD metrics. The signature formula similarly relates

\[
\int (|W^+|^2-|W^-|^2)
\]

to eta/Chern-Simons data at infinity and at the compact face. Reflection makes the doubled chiral contribution cancel. Thus topology distinguishes ASD from non-ASD behavior but does not by itself prohibit mixed Weyl curvature.

A concrete existence mechanism worth isolating is cusp opening. Li-Liu gives an ASD PE-plus-cusp metric. A non-ASD deformation of the cusp model, if present in the linearized Einstein operator, could replace the cusp asymptotic by a second PE asymptotic after a long transition. The decisive object is the bounded or mildly growing kernel of the gauged Einstein operator on the Li-Liu cusp background, decomposed into ASD and non-ASD parts. A non-ASD even Jacobi field whose PE-end trace changes \(g_3\) away from the Cotton-York sheet would be a strong mechanism for two-PE metrics. If the non-ASD kernel is zero near every Li-Liu cusp, any reflected core would have to be finite-amplitude rather than a small deformation of the Toda family.

Relevant source families to inspect precisely:

- Anderson’s PE infinity map and degree theory for four-manifolds.
- Self-dual PE stress tensor versus Cotton-York tensor.
- Einstein cusp-opening and PE Dehn-filling constructions.
- Toral AdS soliton / toral black-hole metrics as non-ASD PE examples on \(D^2\times T^2\), not on \([0,\infty)\times T^3\).

## B. Forward evolution from the center

In Gaussian gauge the exact equations are

\[
q_r'=2q_rS,
\]

\[
S'+HS=\operatorname{Ric}(q_r)^\sharp+3I,
\]

\[
H'=3-|S|^2,
\]

with constraints

\[
R(q_r)+|S|^2-H^2=-6,
\qquad
\operatorname{div}_{q_r}S=dH.
\]

At the center,

\[
S(0)=0,\qquad R(q_0)=-6,
\]

and therefore

\[
S'(0)=\operatorname{Ric}(q_0)^\sharp+3I.
\]

The even Taylor expansion begins

\[
q_r=q_0+r^2\big(\operatorname{Ric}(q_0)+3q_0\big)+O(r^4).
\]

For \(T^2\)-cohomogeneity-one center metrics, the center theorem gives a point where

\[
\lambda_{\min} S'(0)\le -3.
\]

Since \(\operatorname{tr}S'(0)=3\), the least violent eigenvalue pattern is approximately

\[
(-3,3,3),
\]

with traceless part norm squared \(24\). Thus the center necessarily begins with strong anisotropic acceleration; the problem is not to avoid anisotropy but to transport it into the PE \(g_3\) datum without forming a singularity.

A clean dynamical formulation uses normalized variables

\[
\bar q_r=e^{-2r}q_r,\qquad
u=3-H,\qquad
P=S-\frac{H}{3}I.
\]

Then

\[
S-I=P-\frac{u}{3}I,
\]

and the exact equations imply

\[
\bar q_r'=2\bar q_r\left(P-\frac{u}{3}I\right),
\]

\[
u'=|P|^2+\frac{u^2}{3}-2u,
\]

\[
P'+(3-u)P=e^{-2r}\operatorname{Ric}(\bar q_r)^{\circ\sharp},
\]

while the Hamilton constraint becomes

\[
e^{-2r}R(\bar q_r)
=
-4u+\frac{2}{3}u^2-|P|^2.
\]

A PE end means

\[
\bar q_r\to\gamma
\]

smoothly and

\[
u=-\frac{R_\gamma}{4}e^{-2r}+O(e^{-4r}),
\]

\[
P=\operatorname{Ric}(\gamma)^{\circ\sharp}e^{-2r}
-\frac32\,\gamma^{-1}g_3\,e^{-3r}
+O(e^{-4r}).
\]

Thus long-time PE behavior requires the weighted shear to be finite:

\[
\int_0^\infty e^{2r}|S-I|^2\,dr<\infty.
\]

Several structural features of \(q_0\) matter.

First, the normalized metrics \(\bar q_r\) must remain precompact and nondegenerate. If one material direction sees

\[
\int_0^{r_*}\langle S(r)V(r),V(r)\rangle\,dr\to-\infty,
\]

then a collapse occurs before a PE end forms. Diagonal ansätze keep the contracting direction fixed, which is severe. Non-diagonal orbit-shape data

\[
G=\rho U,\qquad U:S^1\to \operatorname{SL}(2,\mathbb R)/\operatorname{SO}(2),
\]

can rotate the contracting eigendirection and distribute strain among torus cycles. This is a genuine mechanism absent from scalar \(d=b-c\) searches.

Second, high-frequency center data are amplified by the hyperbolic tail. In the flat expanding model,

\[
\psi_k''+3\psi_k'-k^2e^{-2t}\psi_k=0,\qquad
\psi_k(0)=1,\quad \psi_k'(0)=0,
\]

one has

\[
\psi_k(\infty)=\frac{\sinh k}{k},
\qquad
e^{2t}\psi_k'(t)\to k\sinh k.
\]

Thus the center-to-infinity map is exponentially ill-conditioned in frequency. A smooth PE end from shooting data is therefore expected only for center data lying on a very regular stable leaf, plausibly analytic or Gevrey in any symmetry-reduced model.

Third, the sharp center-energy regime is important. In the \(T^2\)-cohomogeneity-one class,

\[
q_0=ds^2+G(s)_{ab}dx^adx^b,\qquad
A=\frac12G^{-1}G',
\]

the scalar identity gives

\[
R(q_0)=-2h'-|A_0|^2-\frac32h^2.
\]

For \(R(q_0)=-6\),

\[
\int\rho |A_0|^2
=
6\int\rho+\frac12\int\rho h^2.
\]

The least violent center data have \(h\approx0\) and nearly constant \(|A_0|^2\approx6\), i.e. orbit-shape loops in the hyperbolic plane with nearly constant speed. Such data minimize unnecessary focusing and are better candidates for long-time evolution than sinusoidal low-amplitude data.

## C. Global obstruction mechanisms

There is a stronger pointwise monotonicity than the earlier

\[
R_\gamma=-12-4\int_0^\infty e^{2r}|S-I|^2\,dr.
\]

Since

\[
H'=3-|S|^2
\]

and

\[
|S|^2\ge \frac{H^2}{3},
\]

comparison with

\[
y'=3-\frac{y^2}{3},\qquad y(0)=0
\]

gives

\[
H(r)\le 3\tanh r.
\]

Therefore

\[
3-H(r)\ge 3(1-\tanh r),
\]

and the PE expansion yields the pointwise scalar inequality for the canonical infinity representative:

\[
-\frac{R_\gamma}{4}
=
\lim_{r\to\infty}e^{2r}(3-H)
\ge 6.
\]

Hence

\[
\boxed{R_\gamma\le -24.}
\]

Equality forces \(P\equiv0\), so

\[
S=\frac{H}{3}I,
\]

and the metric is warped:

\[
g=dr^2+\cosh^2(r)\,q_0.
\]

Then

\[
\operatorname{Ric}(q_0)=-2q_0,
\]

which is impossible on \(T^3\). Thus a reflected \(T^3\) core must satisfy

\[
\boxed{R_\gamma<-24}
\]

pointwise in the canonical representative.

The refined identity is also useful. Let

\[
u=3-H,\qquad
w=3(1-\tanh r).
\]

Then

\[
u'=|P|^2+\frac{u^2}{3}-2u,
\]

\[
w'=\frac{w^2}{3}-2w,
\]

so

\[
(u-w)'
=
\left(\frac{u+w}{3}-2\right)(u-w)+|P|^2.
\]

Since \(u(0)=w(0)=3\),

\[
u(r)-w(r)
=
\int_0^r
\exp\!\left(
\int_s^r\left(\frac{u(t)+w(t)}3-2\right)dt
\right)
|P(s)|^2\,ds
\ge0.
\]

Consequently

\[
-\frac{R_\gamma}{4}
=
6+\lim_{r\to\infty} e^{2r}(u-w).
\]

This is a Pohozaev-type separation between the Fuchsian warped case and every genuinely anisotropic core. It does not itself prohibit the desired metric, because \(T^3\) supports metrics with scalar far below \(-24\), but it gives a sharp scalar signature that every computation or construction must reproduce.

Bochner-type routes appear less promising in their basic forms. The center \(T^3\) is a stable minimal hypersurface because

\[
Q(\varphi)
=
\int_{T^3}\left(|\nabla\varphi|^2
-(\operatorname{Ric}_g(n,n)+|S|^2)\varphi^2\right)
=
\int_{T^3}\left(|\nabla\varphi|^2+3\varphi^2\right)>0.
\]

This stability is compatible with \(R(q_0)=-6\). Harmonic one-form and spin-Dirac Bochner formulas also do not have the sign needed to force absence, since the ambient scalar is \(-12\) and \(\operatorname{Ric}=-3g\).

Index theory likewise gives structure rather than an immediate contradiction. The linearized Einstein operator in TT gauge controls local deformations; its kernel determines whether fixed-\(\gamma\) fillings are isolated. Reflection decomposes the kernel into even and odd parts. A nonzero even non-ASD kernel would support bifurcation of reflected metrics. Zero kernel near known ASD/cusp models would only say that nearby non-ASD reflected metrics are absent there; it would not eliminate finite-amplitude ones.

The most concrete global tests are therefore:

\[
R_\gamma<-24,
\]

\[
V_{\mathrm{ren}}=-\frac16\int |W|^2,
\]

and the signature/eta relation tying

\[
\int(|W^+|^2-|W^-|^2)
\]

to Chern-Simons data of \(\gamma\) and \(q_0\). A candidate metric must satisfy all three simultaneously.

## D. Approximate Einstein metrics with small defect

Let

\[
E=\operatorname{Ric}_g+3g.
\]

The exact monotonicity changes to

\[
u'=|P|^2+\frac{u^2}{3}-2u+E_{rr},
\]

hence

\[
(e^{2r}u)'
=
e^{2r}\left(|P|^2+\frac{u^2}{3}+E_{rr}\right).
\]

Thus a pointwise small defect can have order-one weighted effect if the transition length reaches the expanding scale:

\[
\int_0^R e^{2r}E_{rr}\,dr
\sim
\delta e^{2R}.
\]

For

\[
R\sim \frac12\log(1/\delta),
\]

this term is already order one. Therefore an exact monotonicity obstruction need not persist for approximate metrics with \(\|E\|_\infty\to0\).

The traceless transport has the same feature. With defect,

\[
P'+HP
=
\operatorname{Ric}(q_r)^{\circ\sharp}-E_T^\circ,
\]

or in CMC expanding gauge,

\[
(e^{3a}P)'
=
e^a\operatorname{Ric}(q_r)^{\circ\sharp}
-
e^{3a}E_T^\circ.
\]

The small tensor \(E_T^\circ\) is multiplied by \(e^{3a}\). Hence a long, far-out bridge can tune the finite PE stress while keeping the operator norm of the Ricci defect small. This is exactly why the adiabatic tail can flatten anisotropy at vanishing cost in \(\|\operatorname{Ric}+3g\|_\infty\).

A plausible approximate construction has three pieces:

1. **Exact reflected germ.** Start with analytic \(q_0\) satisfying \(R(q_0)=-6\) and \(S(0)=0\). Use the even Einstein expansion for a short interval.

2. **Forced expanding bridge.** Choose \(a(r)\), \(P(r)\), and \(\bar q_r\) so that \(H\to3\), \(P\to0\), and \(e^{-2a}\operatorname{Ric}(\bar q_r)\to0\), while allowing

   \[
   \|E\|_\infty\le \delta.
   \]

   The weighted moments

   \[
   \int e^{2r}E_{rr}\,dr,\qquad
   \int e^{3a}E_T^\circ\,dr
   \]

   can remain finite and nonzero.

3. **Adiabatic tail.** Once

   \[
   S=(1-\varepsilon)I+P,\qquad
   \varepsilon+\|P\|\ll1,
   \qquad
   e^{-2a}\|\operatorname{Ric}(\bar q)\|\ll1,
   \]

   attach a long flattening region. The Step 73 mechanism gives

   \[
   \|\operatorname{Ric}+3g\|_\infty
   \le C\left(K^{-1}+K^{-2}+e^{-2a_0}\right),
   \]

   while removing order-one orbit anisotropy.

The observable signature of such an approximate sequence is that the ordinary defect norm tends to zero, but the renormalized defect moments do not:

\[
\|E\|_\infty\to0,
\]

while

\[
\int e^{2r}E_{rr}\,dr=O(1),
\qquad
\int e^{3a}E_T^\circ\,dr=O(1).
\]

Thus even if exact reflected cores are absent, approximate cores can still feed the graph construction, provided the topology chosen for the final closed manifold admits no Einstein metric and the Ricci pinching interval is fixed around \(-3\).