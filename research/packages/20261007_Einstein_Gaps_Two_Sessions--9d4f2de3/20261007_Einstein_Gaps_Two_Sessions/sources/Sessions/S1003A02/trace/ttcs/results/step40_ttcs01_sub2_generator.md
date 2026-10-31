# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex"
  ]
}
```

## Task

Research problem: for M = X # k CPbar^2 (X minimal general type, A=c_1^2(X)), is there c>0 with P(g)=int|Ric^o|^2 >= 8 pi^2 c k for every metric when 0<k<A/3 (LeBrun only gives k - A/3), or can metrics drive P/(8pi^2 k) to 0? The Step-40 note proves: the whole Seiberg-Witten saving equals (1/2) E int rho^2 |nabla n|^2_{W2} (Nijenhuis energy of the monopole almost-complex structures) minus nonnegative terms, equivalently Weyl rise W^+(n,n) > aligned value; and that every POINTWISE combination of the exact field identities is exhausted exactly at LeBrun's threshold (binding at uniform amplitude rho=3/2). The Step-38 note shows the exceptional charge of a sign flip lives in the anti-self-dual relative curvature h^- and that paired zeros unwind through S^3. Propose the strongest concrete mathematical mechanisms (with equations, not slogans) that could supply k-dependence through genuinely global or differential information: e.g. localization of Nijenhuis energy by the fixed 4pi^2 of h^- near a 2-cycle dual to E_i, elliptic/Bochner estimates for the SW almost-complex structure, harmonic-projection J_epsilon terms, the zeta (Lee-form) cost, or integral constraints across the 2^k sign family. For each, state the precise inequality to prove, why it could hold, which test object (certified perpendicular cell with saving 0.43%, Kaehler blow-ups, diffuse-rotation metrics) could falsify it, and its cheapest decisive check. Equally, construct the most plausible counter-mechanism: a family where Nijenhuis rotation at density ~1 over volume ~10 pi^2 (1-c) per class has o(k) Walsh and zeta cost, and say what geometric construction might realize it.

## Output

The Step-40 exhaustion result reframes the problem. Pointwise algebra can at best reproduce LeBrun’s threshold, and it binds at the uniform amplitude \(\rho=3/2\). Therefore any \(k\)-dependent improvement must come from a genuinely nonlocal functional: a Hodge norm, a period, a capacity, a hypercube Fourier coefficient, or a bubbling quantization. Below I write the pure blow-up case \(M=X\#k\overline{\mathbf{CP}}^{2}\), \(Q=k\), \(s=-4\). The saving is
\[
\mathfrak S=8\pi^{2}k-P(g).
\]
The desired statement \(P(g)\ge 8\pi^{2}c k\) is exactly
\[
\mathfrak S\le 8\pi^{2}(1-c)k.
\]
The Step-40 identities give
\[
\mathfrak S
=
\frac12\mathbb E_\epsilon\int\rho_\epsilon^{2}
|\nabla n_\epsilon|^{2}_{\mathcal W_{2}}
-\text{nonnegative amplitude/Lee/Weyl/Walsh terms},
\]
and equivalently
\[
\mathfrak S
=
\mathbb E_\epsilon\int\bigl(\rho_\epsilon^{2}x_\epsilon-4|M_\epsilon|^{2}\bigr)
+\mathbb E_\epsilon\int B(\rho_\epsilon)
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^{2}
-\mathcal W,
\]
where
\[
B(\rho)=\frac{(2-\rho)(\rho-1)(3\rho+2)}{3},
\qquad
x_\epsilon=M_\epsilon(n_\epsilon,n_\epsilon).
\]
Thus a new mechanism must control the usable part of the \(\mathcal W_{2}\) (Nijenhuis) channel, or force compensating Walsh, Lee, Weyl, or harmonic-projection cost.

---

## 1. Edge compensation from the fixed ASD relative curvature

For one sign flip at \(E_i\), write \(\epsilon'=\epsilon\oplus i\) and
\[
h_i^\epsilon=\frac{f_\epsilon-f_{\epsilon'}}2.
\]
Then \([h_i^\epsilon]=\pm E_i\), and the exact Chern–Weil identity is
\[
\|h_i^{-}\|^{2}-\|h_i^{+}\|^{2}=4\pi^{2}.
\]
The Fierz identities give
\[
|h_i^{+}|^{2}
=
\frac{(\rho_\epsilon-\rho_{\epsilon'})^{2}}{8}
+\frac{|w_{\epsilon\epsilon'}|^{2}}{2},
\qquad
w_{\epsilon\epsilon'}=\Phi_\epsilon\wedge\Phi_{\epsilon'}.
\]
The relative Maxwell equation, up to the conventional numerical factor, is
\[
d^{*}h_i^\epsilon \sim \operatorname{Im}(\zeta_\epsilon-\zeta_{\epsilon'}).
\]
The fixed \(4\pi^{2}\) in the ASD part is therefore tied to the Lee-form difference.

For a one-blow-up normalization, or for a localized edge contribution after cutting off the other exceptional classes, the paired identity has the form
\[
P-8\pi^{2}
=
2\|\bar f^{-}\|^{2}
+2\|h_i^{+}\|^{2}
+\frac{\mathcal R_\epsilon+\mathcal R_{\epsilon'}}2
-2(K_\epsilon+K_{\epsilon'}),
\]
where \(\mathcal R_\epsilon\) is the single-field alignment/amplitude remainder and
\[
K_\epsilon=\int|\nabla_{\mathcal A_\epsilon}\Phi_\epsilon|^{2}.
\]
Hence a per-edge tariff \(P\ge 8\pi^{2}c\) is equivalent to the kinetic compensation estimate
\[
\boxed{
2(K_\epsilon+K_{\epsilon'})
\le
2\|\bar f^{-}\|^{2}
+2\|h_i^{+}\|^{2}
+\frac{\mathcal R_\epsilon+\mathcal R_{\epsilon'}}2
+8\pi^{2}(1-c).
}
\tag{E1}
\]
Averaging over all \(i\) and \(\epsilon\) would give \(P\ge 8\pi^{2}c k\).

Why this could hold: the relative class \(\pm E_i\) forces \(h_i^{-}\) to carry a fixed \(4\pi^{2}\). If the kinetic excess in \(K_\epsilon+K_{\epsilon'}\) sits in the free \(\mathcal W_{2}\) channel far from the support of the ASD harmonic representative of \(E_i\), the relative Maxwell equation and the Bochner system for \(u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle\) should convert that excess into either \(h_i^{+}\), the alignment remainder, or Lee-form cost. In a localized form, with a cutoff \(\chi_i\) adapted to the tube around the dual 2-cycle, one would want
\[
\boxed{
\int \chi_i\,\rho_\epsilon^{2}|\nabla n_\epsilon|^{2}_{\mathcal W_{2}}
\le
C\int \chi_i\bigl(|M_\epsilon|^{2}+|\zeta_\epsilon|^{2}+(2-\rho_\epsilon)^{2}\bigr)
+C\int_{\operatorname{supp}|\nabla\chi_i|}|\psi_\epsilon|^{2}|\nabla\chi_i|^{2}
+8\pi^{2}(1-c_i).
}
\tag{E1loc}
\]
Summing over \(i\) would produce the desired \(k\)-dependence.

Falsifying objects: a pair of solutions with \(h_i^{-}\) essentially harmonic ASD, \(h_i^{+}=o(1)\), \(\zeta_\epsilon-\zeta_{\epsilon'}=o(1)\), and large diffuse \(\mathcal W_{2}\) rotation would refute (E1). The certified perpendicular cell is the first concrete test: it already realizes a subunit coefficient \(c\approx0.99566273277\), so any mechanism predicting a larger universal \(c\) is incompatible with that cell.

Cheapest decisive check: evaluate the paired residual
\[
2(K_\epsilon+K_{\epsilon'})
-
2\|\bar f^{-}\|^{2}
-2\|h_i^{+}\|^{2}
-\frac{\mathcal R_\epsilon+\mathcal R_{\epsilon'}}2
\]
on the certified cell for one sign flip. Then compare with \(8\pi^{2}(1-c)\). If the residual is much smaller than \(8\pi^{2}\), the edge compensation mechanism cannot by itself give a strong \(c\). A reduced ODE ansatz with \(h_i=\eta_i+d\alpha\), \(\eta_i\) the ASD harmonic representative of \(E_i\), constant \(\rho\), and \(n\) rotating in one coordinate direction, gives the cheapest model for testing (E1).

---

## 2. Bochner localization of the Bloch form

Let \(\psi_\epsilon=2\sqrt2\,\sigma(\Phi_\epsilon)\). The self-dual Weitzenböck formula gives
\[
\int|\nabla\psi_\epsilon|^{2}
=
2\|d\psi_\epsilon\|^{2}
+2\int (W^{+}-W_{0,\epsilon})(\psi_\epsilon,\psi_\epsilon)
+\int\frac{\rho_\epsilon^{2}}{3}(4-\rho_\epsilon^{2}).
\]
Under the Dirac equation, Step 40 gives
\[
|d\psi_\epsilon|^{2}=2\rho_\epsilon|b_\epsilon|^{2},
\]
where \(b_\epsilon\) is the Lee phase component, while the \(\mathcal W_{2}\) component lies in \(\ker d\). The first-jet decomposition contains
\[
|\nabla\psi_\epsilon|^{2}
=
4\rho_\epsilon|a_\epsilon|^{2}
+4\rho_\epsilon^{2}|v_{2,\epsilon}|^{2}
+2\rho_\epsilon|a_\epsilon+J'b_\epsilon|^{2},
\]
and
\[
4|v_{2,\epsilon}|^{2}=|\nabla n_\epsilon|^{2}_{\mathcal W_{2}}.
\]
Thus the integrated Weitzenböck formula is the only exact identity converting the free \(\mathcal W_{2}\) energy into Weyl misalignment, amplitude depletion, and Lee cost.

A local version with a cutoff \(\chi_i\) around the \(i\)-th exceptional region would be
\[
\boxed{
\begin{aligned}
\int \chi_i\,\rho_\epsilon^{2}|\nabla n_\epsilon|^{2}_{\mathcal W_{2}}
\le{}&
C\int\chi_i\Bigl(|M_\epsilon|^{2}+|\zeta_\epsilon|^{2}+(2-\rho_\epsilon)^{2}\Bigr)\\
&+C\int |\psi_\epsilon|^{2}|\nabla\chi_i|^{2}.
\end{aligned}
}
\tag{E2}
\]
If the ASD relative charge \(4\pi^{2}\) forces \(\psi_\epsilon\) to have a quantized flux through the annulus where \(|\nabla\chi_i|\neq0\), then the last term supplies a per-exceptional price. This would localize the Nijenhuis energy near the dual cycle and prevent it from being spread diffusely for free.

Why this could hold: the \(\mathcal W_{2}\) component is invisible to \(d\psi\), but it is still present in \(|\nabla\psi|^{2}\). A cutoff Weitzenböck identity forces that invisible energy to be paid by either Weyl misalignment \(M_\epsilon\), Lee cost \(\zeta_\epsilon\), amplitude depletion, or a flux term across the cutoff annulus. The fixed ASD charge of the sign flip is the natural source of the flux quantization.

Falsifying objects: a diffuse-rotation metric in which \(\rho\approx1.6\), \(M\) and \(\zeta\) are small, and the \(\mathcal W_{2}\) energy is spread over a large region so that the cutoff flux term can be made \(o(1)\) per class. The certified perpendicular cell again gives a concrete test: if its cutoff residual is much smaller than \(8\pi^{2}\) per class, this mechanism alone cannot yield a strong \(c\).

Cheapest decisive check: apply (E2) to the certified cell with a family of cutoffs around the exceptional sphere and compute the scaling of the annulus term. If the annulus term remains \(O(1)\) as the cutoff radius varies, the mechanism is alive. If it decays with the cell’s exceptional area, the mechanism is too weak.

---

## 3. Walsh mass, harmonic projection, and scalar-volume exchange

The Walsh part has a remarkably rigid global expression. For the sign family,
\[
J_\epsilon
=
\|f_\epsilon^{+}-(f_\epsilon^{+})_{H}\|^{2}
=
\frac12\int\rho_\epsilon^{2}-4\pi^{2}p_\epsilon,
\qquad
p_\epsilon=(a_{\epsilon,g}^{+})^{2}.
\]
The Walsh determinant contribution satisfies
\[
\mathcal W
=
8\pi^{2}\bigl(\mathbb E_\epsilon p_\epsilon-A\bigr)
+2\mathbb E_\epsilon J_\epsilon.
\]
But the spinor Hodge identity gives
\[
\mathbb E_\epsilon\int\rho_\epsilon^{2}
=
8\pi^{2}\mathbb E_\epsilon p_\epsilon
+2\mathbb E_\epsilon J_\epsilon.
\]
Therefore
\[
\boxed{
\mathcal W
=
\mathbb E_\epsilon\int\rho_\epsilon^{2}-8\pi^{2}A.
}
\tag{3.1}
\]
Since \(\mathcal W\ge0\) and \(\rho_\epsilon\le2\),
\[
\mathbb E_\epsilon\int\rho_\epsilon^{2}\ge8\pi^{2}A,
\]
and
\[
\boxed{
V(g)
\ge
2\pi^{2}A
+\frac14\mathbb E_\epsilon\int(4-\rho_\epsilon^{2})
+\frac14\mathcal W.
}
\tag{3.2}
\]
This is a global mass constraint absent from pointwise algebra.

Because
\[
C_{+}(g)=\frac1{2\pi^{2}}\int|W^{+}|^{2}+\frac{V}{6\pi^{2}},
\]
the scalar part of \(C_{+}\) charges any volume increase. Relative to the Kähler-scale volume \(2\pi^{2}A\), the depletion term \(\mathbb E\int(4-\rho^{2})\) forces a scalar cost in the saving of size
\[
8\pi^{2}\cdot\frac{1}{6\pi^{2}}\cdot\frac14\mathbb E\int(4-\rho^{2})
=
\frac13\mathbb E\int(4-\rho^{2}).
\]
A candidate global tariff is therefore
\[
\boxed{
\begin{aligned}
\mathfrak S
\le{}&
\mathbb E_\epsilon\int
\left[
\sup_{x,M}\bigl(\rho^{2}x-4|M|^{2}+B(\rho)\bigr)
-\frac13(4-\rho^{2})
\right]\\
&-\frac43\mathcal W
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^{2}
+o(k),
\end{aligned}
}
\tag{E3}
\]
with the algebraic constraint \(|M|^{2}\ge \frac32x^{2}\). The supremum gives
\[
\sup_{x}\bigl(\rho^{2}x-6x^{2}\bigr)=\frac{\rho^{4}}{24}.
\]
A sharper version would replace the free supremum by the admissible Weyl eigenvalues allowed by the harmonic projections \(J_\epsilon\).

Why this could hold: the identity (3.1) couples all \(2^{k}\) fields. A saving region with \(\rho\approx1.6\) lowers \(\int\rho^{2}\); because \(\rho\le2\), the average mass can be restored only by increasing volume or by increasing \(\mathcal W\). Both are charged in \(C_{+}\). Thus a low-density depletion region cannot be free once the global mass constraint is imposed.

The harmonic-projection terms \(J_\epsilon\) supply a second route. If the self-dual curvature \(f_\epsilon^{+}=\rho_\epsilon n_\epsilon/\sqrt2\) rotates away from the harmonic representative of \(a_\epsilon\), then
\[
J_\epsilon=\|f_\epsilon^{+}-(a_\epsilon^{+})_{g}\|^{2}
\]
grows. A Hodge spectral estimate of the form
\[
\boxed{
J_\epsilon
\ge
\lambda(g)^{-1}\|d^{*}f_\epsilon^{+}\|^{2}
}
\tag{3.3}
\]
would convert rotation into \(J\)-cost. Since \(d^{*}f_\epsilon\) is controlled by \(\zeta_\epsilon\), this connects harmonic projection to Lee cost.

Falsifying objects: a family with \(\rho\approx1.6\) on volume \(O(k)\), \(V=2\pi^{2}A+o(k)\), and \(\mathcal W=o(k)\). Such a family would violate the mass-volume exchange in (3.2). Kähler blow-ups saturate \(\rho=2\) and \(\mathcal W=0\), so they test the sharpness of the mass constraint but not the saving channel. The certified perpendicular cell tests whether a small saving region can evade the volume cost.

Cheapest decisive check: compute \(V\), \(\mathbb E\int\rho^{2}\), \(\mathcal W\), and \(J_\epsilon\) for the certified cell. Then solve the constrained one-dimensional variational problem in \(\rho\) using the exact polynomials \(B(\rho)\), \(m(\rho)\), and the pointwise envelope from Step 40, now augmented by the mass constraint (3.1). If the constrained maximum saving per class is still large, the mass mechanism alone is insufficient.

---

## 4. Lee-form periods and relative winding

The imaginary part of \(\zeta_\epsilon\) is the Lee-form source for the curvature. In a suitable normalization,
\[
d^{*}f_\epsilon =2\,\operatorname{Im}\zeta_\epsilon.
\]
For a sign flip,
\[
d^{*}h_i^\epsilon
=
\operatorname{Im}(\zeta_\epsilon-\zeta_{\epsilon'}).
\]
If the relative section
\[
u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle
\]
has a zero cycle dual to \(E_i\), and if the unwinding through \(w_{\epsilon\epsilon'}\) is small, then the phase of \(u_{\epsilon\epsilon'}\) winds around a linking circle \(\gamma_i\). This gives
\[
\int_{\gamma_i}\operatorname{Im}(\zeta_\epsilon-\zeta_{\epsilon'})=2\pi.
\]
Cauchy–Schwarz then yields
\[
\boxed{
\int |\zeta_\epsilon-\zeta_{\epsilon'}|^{2}
\ge
\frac{4\pi^{2}}{\operatorname{length}(\gamma_i)^{2}}.
}
\tag{E4}
\]
A conformally invariant version would use capacity:
\[
\boxed{
\sum_i\mathbb E_\epsilon\int
|\zeta_\epsilon-\zeta_{\epsilon^{i}}|^{2}
\ge
C\sum_i\operatorname{Cap}(E_i)^{-1}.
}
\tag{E4cap}
\]
If the capacities of the exceptional cycles are bounded below under the normalization \(s=-4\) and \(P=O(k)\), this gives an \(\Omega(k)\) Lee cost.

Why this could hold: the relative connection \(h_i\) has fixed ASD charge. If the zero of \(u\) is paid by phase winding rather than by orthogonality through \(w\), the Lee form must carry the period. The Maxwell equation then forces \(L^{2}\) Lee energy.

Falsifying objects: the Step-38 \(S^{3}\) unwinding mechanism. The phase winding of \(u\) can disappear through the \(w\)-component because \(\pi_{1}(S^{3})=0\). If \(|w_{\epsilon\epsilon'}|\) is large where \(u=0\), the period condition is not forced. Long tubes around exceptional spheres also make capacities small, allowing the Lee cost to decay.

Cheapest decisive check: compute periods of \(\operatorname{Im}\zeta_\epsilon-\operatorname{Im}\zeta_{\epsilon'}\) on the certified cell and measure \(\int|w_i|^{2}\). If the period is absent and \(w_i\) carries the topological information, the Lee-period mechanism is not active. A tube model with exceptional area \(A_E\) and radius \(r\) should show whether the Lee cost scales like \(A_E/r^{2}\) and can be made \(o(1)\).

---

## 5. Hypercube Fourier constraints across the \(2^{k}\) family

The sign family is a hypercube. The Walsh decomposition is a Fourier expansion:
\[
f_\epsilon^{+}=\sum_{I\subset\{1,\dots,k\}}\chi_I(\epsilon)f_I^{+},
\qquad
\chi_I(\epsilon)=\prod_{i\in I}\epsilon_i.
\]
Parseval gives
\[
\mathbb E_\epsilon\|f_\epsilon^{+}\|^{2}
=
\sum_I\|f_I^{+}\|^{2}.
\]
Edge differences satisfy
\[
\sum_{i=1}^{k}\mathbb E_\epsilon
\|f_\epsilon^{+}-f_{\epsilon^{i}}^{+}\|^{2}
=
4\sum_{I\neq\varnothing}|I|\,\|f_I^{+}\|^{2}.
\]
Thus the Walsh cost \(\mathcal W\) controls not only the total non-zero-mode energy but, with weights \(|I|\), the total edge variation.

A useful sufficient inequality would be
\[
\boxed{
\mathbb E_\epsilon\|f_\epsilon^{+}-f_{\epsilon^{i}}^{+}\|^{2}
+
\mathbb E_\epsilon\int|w_{\epsilon\epsilon^{i}}|^{2}
+
\mathbb E_\epsilon\int(\rho_\epsilon-\rho_{\epsilon^{i}})^{2}
\ge
\tau
}
\tag{E5edge}
\]
for each \(i\), with a universal \(\tau>0\). Summing over \(i\) would give
\[
\boxed{
\sum_{I\neq\varnothing}|I|\,\|f_I^{+}\|^{2}
+
\text{relative }w\text{ and amplitude terms}
\ge
\frac{\tau k}{4}.
}
\tag{E5}
\]
Since \(\mathcal W\) contains \(\sum_{I\neq\varnothing}\|f_I^{+}\|^{2}\), this would force Walsh cost of order \(k\) unless the edge variation is carried by \(w\) or amplitude depletion.

Why this could hold: each edge corresponds to a line bundle of class \(\pm E_i\). If the two spinors are not orthogonal and their amplitudes are comparable, their self-dual curvature directions must differ by an amount related to the topological class. The hypercube Fourier structure then converts many edge differences into nontrivial Walsh modes.

Falsifying objects: a highly coordinated family where
\[
f_\epsilon^{+}=f_0^{+}+\sum_i\epsilon_i\beta_i
\]
with \(\|\beta_i\|_{L^{2}}=o(1)\) but \(|\nabla\beta_i|_{L^{2}}=O(1)\). Then edge \(L^{2}\) differences and Walsh norms are small, while Nijenhuis energy can remain large. The Step-38 \(S^{3}\) unwinding again permits edge topology to be carried by \(w\) rather than by \(f^{+}\)-variation.

Cheapest decisive check: compute the first Walsh modes \(f_{\{i\}}^{+}\) and a few higher modes for the certified cell. If the edge \(L^{2}\) differences are \(o(1)\) per edge, the hypercube mechanism cannot supply a large \(c\). A finite-dimensional toy model on \(\{\pm1\}^{k}\) with prescribed edge differences and small Fourier tail gives an immediate sanity test.

---

## 6. Core quantization and ALE/CH end corrections

If a minimizing sequence for total curvature concentrates, Anderson-type compactness gives ideal bubbles. For a connected core \(N\) with \(m=b_{2}(N)\), \(r=b_{1}(N)\), \(e\) ends, end-group correction \(q_\infty\), and eta correction \(\eta_\infty\), the relative curvature cost is
\[
P_N
=
8\pi^{2}m+32\pi^{2}r
+16\pi^{2}(e-2+q_\infty)
-24\pi^{2}\eta_\infty
+4W_N^{+}+\frac{S_N}{12}.
\]
For AE ends this gives a cost at least of order \(8\pi^{2}m\) plus end terms. Quotient ends can reduce the topological part drastically; Eguchi–Hanson-type spaces with one \(\mathbb Z_{2}\) end have \(P_N=0\) while \(m=1\).

A \(k\)-dependent lower bound would follow from a marked gluing statement:
\[
k=\sum_\nu m_\nu,
\]
together with an estimate
\[
\boxed{
\sum_\nu
\left[
8\pi^{2}m_\nu
+32\pi^{2}r_\nu
+16\pi^{2}(e_\nu-2+q_{\infty,\nu})
-24\pi^{2}\eta_{\infty,\nu}
+4W_{N_\nu}^{+}
+\frac{S_{N_\nu}}{12}
\right]
\ge
8\pi^{2}c k.
}
\tag{E6}
\]
If the topology of the blow-up family forces AE ends, or prevents enough quotient-end cancellation, then \(c>0\) follows. If quotient ends are allowed and can be glued without large neck cost, this route may produce subunit or even vanishing coefficients.

Why this could hold: the exceptional classes have square \(-1\). If each is carried by an AE core, the core cost is essentially \(8\pi^{2}\) per class. The known subunit cell must then exploit quotient-end or orbifold-type corrections.

Falsifying objects: a sequence of ALE or complex-hyperbolic orbifold cells with \(m=1\) and \(P_N/m\to0\). The certified perpendicular cell is a finite-radius manifestation of this possibility. If one can glue \(k\) such cells with neck cost \(o(k)\), the core quantization route cannot give a positive universal \(c\).

Cheapest decisive check: compute the minimal value of \(P_N/m\) among ALE/CH cells compatible with the sign-family Spin\(^c\) structures and the scalar \(-4\) normalization. Then estimate the neck cost for gluing \(k\) such cells into \(X\). If the infimum is \(0\), this mechanism cannot supply a positive \(c\).

---

# Most plausible counter-mechanism

The strongest counter-mechanism should hide the exceptional topology in ASD curvature while keeping the self-dual Walsh data almost independent of the sign vector.

Let \(\eta_i\) be ASD harmonic representatives of the exceptional classes, chosen so that
\[
E_i^{+}=0,
\qquad
\|\eta_i^{-}\|^{2}=4\pi^{2},
\]
and the \(\eta_i\) have essentially disjoint supports in thin exceptional tubes. Let \(f_0^{+}\) be a common self-dual form and take
\[
f_\epsilon
=
f_0+\sum_i\epsilon_i\eta_i+\beta_\epsilon,
\]
where \(\beta_\epsilon\) is exact and is chosen so that
\[
f_\epsilon^{+}=\frac{\rho_\epsilon}{\sqrt2}n_\epsilon.
\]
The sign dependence of the cohomology is carried by the ASD forms \(\eta_i\), not by the self-dual Walsh modes. Thus the Walsh coefficients \(f_I^{+}\) can be made small if the self-dual variations are small in \(L^{2}\).

Now choose a common amplitude \(\rho_0\approx1.6\) and a family of directions
\[
n_\epsilon
=
\exp\Bigl(\sum_i\epsilon_i\theta_i T_i\Bigr)n_0,
\]
where each \(\theta_i\) is supported in a unit-size cell \(B_i\), has
\[
\int_{B_i}|\nabla\theta_i|^{2}\sim 1,
\qquad
\int_{B_i}\theta_i^{2}=o(1),
\]
and is chosen purely in the \(\mathcal W_{2}\) component, so that the Lee component vanishes to leading order. By the Step-40 pointwise Dirac analysis, the \(\mathcal W_{2}\) component is not seen by the Dirac equation at first jet level; hence \(\zeta_\epsilon\) can remain small. Because the \(\theta_i\) have small \(L^{2}\) and disjoint supports, the Walsh modes \(f_I^{+}\) are \(o(1)\) per class. The relative ASD charge remains in \(\eta_i\), and the zeros of the relative inner products \(u_{\epsilon\epsilon'}\) can unwind through the \(w\)-fields in \(S^{3}\), avoiding Lee periods.

The saving per cell is approximately
\[
\frac12\rho_0^{2}\int_{B_i}|\nabla\theta_i|^{2}
+
B(\rho_0)\operatorname{Vol}(B_i)
+
\rho_0^{2}x_i\operatorname{Vol}(B_i)
-
4\int_{B_i}|M_i|^{2}.
\]
Choosing \(M_i\) with eigenvalues
\[
x_i,\quad -\frac{x_i}{2},\quad -\frac{x_i}{2},
\qquad
x_i=\frac{\rho_0^{2}}{12},
\]
saturates the pointwise Weyl tradeoff
\[
\rho_0^{2}x-4|M|^{2}
\le
\frac{\rho_0^{4}}{24}.
\]
Thus the local saving density can approach the Step-40 pointwise optimum while \(\mathcal W\) and \(\zeta\) remain \(o(1)\) per class.

A geometric realization could be built from ramified ball quotients or complex-hyperbolic cusp resolutions. The exceptional class is carried by the ASD curvature of the quotient end, while the nonintegrable almost-complex rotation occurs in the bulk of the cell. The Step-38 complex-hyperbolic stable-manifold conditions
\[
\mathcal B+6L=0,
\qquad
\mathcal A-(\sqrt{13}-1)\delta=0
\]
give the correct asymptotic conditions for a collocation or shooting construction of such cells. If a sequence of cells can make the saving per cell approach \(8\pi^{2}\) while \(\mathcal W_{\text{cell}}+\|\zeta_{\text{cell}}\|^{2}\to0\), then gluing \(k\) such cells into \(X\) would drive
\[
\frac{P}{8\pi^{2}k}\to0.
\]
If the supremal cell saving is instead \(8\pi^{2}(1-\sigma)\), the same construction gives the candidate limiting coefficient \(c=\sigma\).

The decisive local computation is therefore the constrained cell variational problem:
maximize the Step-40 saving density subject to the Seiberg–Witten equations, the correct complex-hyperbolic asymptotics, and the requirements
\[
\mathcal W_{\text{cell}}=o(1),
\qquad
\|\zeta_{\text{cell}}\|^{2}=o(1).
\]
The value of that supremum is exactly the quantity that distinguishes a positive universal tariff from a family driving the normalized Ricci energy to zero.