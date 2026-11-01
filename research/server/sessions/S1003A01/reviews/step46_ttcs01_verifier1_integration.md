# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 46,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step46_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step46_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-46 note and its computation against the inherited O10 equations and the exact TN/TNAdS sources. Check especially: (i) why a periodic one-compatible-nut block is topologically inadmissible; (ii) the distinction among circle Chern degree, scalar mass flux, and determinant/torsion boundary data; (iii) the half-order expansion Phi=Phi0+L chi1+..., the coefficient a=sqrt(2)/3, and the exact parent Hessian-energy calculation; (iv) the Hermite jet interpolation identity and its four-dimensional collapsed-cell scaling; (v) the correction that the raw TN field requires a leading q-pairing rather than solving the normalized resolvent equation at the flux-balance radius; and (vi) whether the finite marked-block problem states the correct residual and Cauchy scales. Identify any mathematical error, convention ambiguity, missing hypothesis, or stronger consequence. Give corrected formulas where needed.

## Integrated Scientific Memo

# Step‑46 verification memo

## Verdict

The central conclusions of Step 46 are sound, but several claims need narrower hypotheses or corrected interpretation:

1. A one-compatible-nut periodic cell is impossible **only if the periodic identifications preserve a globally oriented free \(S^1\)-bundle structure** on the punctured orbit space.
2. Circle Chern degree, scalar mass flux, determinant-line boundary data, and torsion index are genuinely distinct.
3. The first spinor correction is \(L\chi _1\), with
   \[
   a=\frac{\sqrt2}{3},
   \qquad
   \int_{B_R}|\nabla^2\chi|^2
   =\frac{32\pi^2}{9}\ell^2\Bigl(\frac R{R+\ell}\Bigr)^2,
   \]
   but this exact Hessian formula is a **Ricci-flat TN tangent calculation**, not an exact TNAdS positive-spinor calculation.
4. The Hermite identity and \(L^{-2}\) reset cost are correct, subject to a controlled collar and a common gauge/normal orientation.
5. The raw TN field has a leading \(q\)-pairing; choosing the mass-balance radius does not solve the normalized resolvent equation.
6. The interior residual scales in the finite-block problem are correct, but the Cauchy formulation and joining law require refinement. In particular, (6.5) describes jets on sections separated by distance \(L\), not direct gluing across one common interface.

The largest computational caveat is that the Step‑46 script combines TN and TNAdS quantities in the same rows. Its fifth-section pairing is exact for the raw **TN** field and establishes the correct leading obstruction, but it does not compute the TNAdS spinorial resolvent residual.

---

## 1. Periodic one-nut topology

Let \(Q\) be the orbit space of the free part of a semi-free \(S^1\)-action, after removing a small neighborhood of one compatible nut. Let \(\Omega\) be the curvature of a normalized principal-circle connection. Then
\[
d\Omega=0,\qquad
\frac1{2\pi}\int_{S^2_{\rm nut}}\Omega=+1
\]
up to the chosen orientation convention.

If opposite faces of a fundamental block are identified by bundle-preserving maps, their contributions cancel. The quotient is a punctured closed orbit space, and Stokes gives
\[
0=\frac1{2\pi}\int_Qd\Omega
  =\frac1{2\pi}\int_{\partial Q}\Omega
  =-\frac1{2\pi}\int_{S^2_{\rm nut}}\Omega=-1,
\]
a contradiction. With a genuine outer boundary,
\[
\deg_{\rm circ}(Y_{\rm out})
 =\sum_a \deg_{\rm circ}(S^2_{{\rm nut},a})
\]
after consistent boundary orientation; bolts and anti-nuts contribute their corresponding signed terms.

The necessary hypothesis should be explicit:

- there is a globally defined, oriented circle generator on the punctured block;
- the action is free away from the specified fixed components;
- all periodic identifications preserve the principal \(S^1\)-bundle.

The current O10 estimates do not themselves produce such a global circle action. If the transition collar abandons the circle structure, the Hopf degree need not remain defined through that collar. Thus Step 46 proves inadmissibility of a **circle-compatible periodic cell model**, not of every abstract four-dimensional gluing containing a TN-like core.

---

## 2. The boundary quantities are inequivalent

### Geometric circle degree

This is an integer on a two-cycle in the orbit space:
\[
\deg_{\rm circ}(\Sigma)
 =\frac1{2\pi}\int_\Sigma\Omega\in\mathbb Z.
\]
It concerns the geometric orbit bundle.

### Scalar mass flux

For \(m=|v|^2\) and
\[
q=(\nabla^*\nabla-2)v,
\]
with the conventions of the note,
\[
\int_{\partial\Omega}\partial_\nu m
 =2\int_\Omega|\nabla v|^2
  -4\int_\Omega m
  -2\operatorname{Re}\int_\Omega\langle q,v\rangle.
\]
This is a real, metric-dependent three-boundary integral. It can be \(o(L^6)\) while the circle degree is \(1\). Conversely, a nonzero scalar flux contains no integral Chern information.

One must distinguish absolute smallness from normalized smallness: a raw flux \(O(L^6)\) tends to zero absolutely but remains of the same order as the cell volume.

### Determinant and torsion data

The actual Spin\(^c\) fields carry:

- \(A^{\tan}\), modulo boundary gauge;
- relative determinant degree or a reference-dependent Chern–Simons invariant;
- \(\Phi|_Y\) and the appropriate boundary derivative/projection;
- \(t_\Phi|_Y\) and, when nonvanishing, its relative index.

A nut neighborhood is a four-ball, so its determinant line may be trivial even though its boundary carries the degree-one geometric Hopf fibration. Hence
\[
\deg_{\rm circ}\neq c_1(L)
\]
in general. Likewise \(|v|^2\) cannot determine connection holonomy or the homotopy class of \(t_\Phi/|t_\Phi|\).

A torsion index is defined only after choosing a boundary trivialization and proving \(t_\Phi\neq0\) on the boundary. An \(H^1\)-small bulk error does not by itself supply pointwise nonvanishing of the trace.

---

## 3. Half-order spinor parent and Hessian energy

On the Ricci-flat TN tangent, choose parallel \(e_1,e_2\) and set
\[
\Phi_0=\sqrt{\rho_*}\,e_1,\qquad
\rho_*=\frac43,\qquad
\chi=a\,\bar f\,e_2.
\]
The linearized cubic torsion has coefficient
\[
2\rho_*a=\sqrt{m_*},
\qquad m_*=\frac{128}{81}.
\]
Thus
\[
a=\frac{\sqrt{m_*}}{2\rho_*}
 =\frac{\sqrt2}{3}.
\]
Changing Clifford or complex-structure convention can multiply \(a\) by a unit complex phase or interchange \(f\) and \(\bar f\), but not change \(|a|\) or the energy.

Since \(x=LX\) and \(f(x)=L F(X)\),
\[
\chi(x)=L\,a\,\overline{F(X)}e_2.
\]
Therefore
\[
\Phi=\Phi_0+L\chi_1(X)+L^2\chi_2(X)+\cdots,
\]
not \(\Phi_0+L^2\chi_1+\cdots\). In (6.2), \(\bar f\) inside \(\chi_1\) must mean the **cell-coordinate** function; retaining the physical \(f\) there would count the factor \(L\) twice.

For
\[
v_{\rm TN}=\sqrt{\frac{m_*}{2}}\,d\bar f,
\]
parallelness of \(e_2\) gives
\[
|\nabla^2\chi|^2
 =\frac{2a^2}{m_*}|\nabla v|^2
 =\frac9{32}|\nabla v|^2.
\]
Using
\[
E_{\rm TN}(R)
 =8\pi^2m_*\ell^2
   \left(\frac R{R+\ell}\right)^2,
\]
one obtains
\[
\boxed{
\int_{B_R}|\nabla^2\chi|^2
 =\frac{32\pi^2}{9}\ell^2
   \left(\frac R{R+\ell}\right)^2.
}
\]

The TN and TNAdS radial volume densities coincide:
\[
dV=16\pi^2\ell R(R+\ell)\,dR.
\]
Hence
\[
\operatorname{Vol}(B_R)
 =16\pi^2\ell
   \left(\frac{R^3}{3}+\frac{\ell R^2}{2}\right).
\]
At \(R=cL,\ \ell=L^3,\ c^3=3/4\),
\[
\operatorname{Vol}(B_{cL})
 =4\pi^2L^6+8\pi^2c^2L^8,
\]
so
\[
\frac{\int|\nabla^2\chi|^2}{\operatorname{Vol}(B_{cL})}
 \longrightarrow \frac89.
\]

This \(8/9\) is the exact TN-parent leading density. On TNAdS the chosen TN parallel spinor frame is no longer parallel, so the complete TNAdS Hessian includes connection corrections and cross terms. The note should call the result an exact tangent calculation and a leading TNAdS asymptotic, not an exact full TNAdS spinor energy.

---

## 4. Hermite interpolation and collapsed scaling

For Hilbert-space-valued \(u\in H^2([0,L])\), the cubic Hermite interpolant uniquely minimizes \(\int|u''|^2\), and
\[
\boxed{
\inf\int_0^L|u''|^2
 =
 \frac{12}{L^3}
 \left|u_1-u_0-\frac L2(p_0+p_1)\right|^2
 +\frac1L|p_1-p_0|^2.
}
\]
The script verifies this formula correctly.

For a collapsed cell whose normal width is \(L\), transverse three-volume is \(A_L\asymp L^5\), and total four-volume is \(A_LL\asymp L^6\), the reset data
\[
u_1=u_0,\qquad p_1=p_0=p
\]
give
\[
E_{\rm cell}\ge A_L\,\frac{12|p|^2}{L},
\qquad
\frac{E_{\rm cell}}{\operatorname{Vol}_{\rm cell}}
 \ge\frac{12|p|^2}{L^2}.
\]
Thus the \(L^{-2}\) divergence is correct.

The covariant application requires:

- a collar of thickness comparable to \(L\) with uniformly controlled geometry;
- parallel transport or temporal gauge along its normal direction;
- one common oriented normal for comparing the two cross-sections;
- a fixed spin/determinant gauge identification;
- RMS or integrated control over the transverse cross-section.

Under those hypotheses, bounded density requires
\[
p_1-p_0=O(L),\qquad
u_1-u_0-\frac L2(p_0+p_1)=O(L^2).
\]
Moreover, if a fraction \(\eta_L\) of the cells undergo a fixed-size reset, a uniform global Hessian-density bound forces
\[
\eta_L=O(L^2).
\]
Thus even a positive-density family of reset cells is impossible.

### Correction to the interpretation of (6.5)

For two cross-sections separated by physical distance \(L\), with derivatives measured along the same oriented normal, the Hermite matching law is of the displayed form.

For direct gluing across one common interface, however, smoothness requires
\[
\Phi_j=G_{ij}\Phi_i,
\qquad
\nabla_{\nu_j}\Phi_j=-G_{ij}\nabla_{\nu_i}\Phi_i,
\]
because the two outward normals are opposite. Analogous conditions hold for \(v\), and \(A^{\tan}\) must transform by the usual gauge law.

Therefore (6.5) should not be called the direct interface matching condition. It is a slow-variation condition between corresponding sections or cell centers separated by \(L\).

---

## 5. Raw TN pairing versus the TNAdS problem

On Ricci-flat TN,
\[
\nabla^*\nabla v_{\rm TN}=0,
\]
so
\[
q_{\rm TN}=(\nabla^*\nabla-2)v_{\rm TN}=-2v_{\rm TN}.
\]
Consequently,
\[
\boxed{
\operatorname{Re}\int_{B_R}\langle q_{\rm TN},v_{\rm TN}\rangle
 =-2M(R),
}
\]
where
\[
M(R)=\frac{16\pi^2}{3}m_*\ell R^3.
\]
Also
\[
\Phi_m^{\rm TN}(R)=2E_{\rm TN}(R).
\]
At the exact balance radius
\[
R(R+\ell)^2=\frac{3\ell}{4},
\]
one has \(2E=4M\), hence
\[
\operatorname{Re}\int\langle q_{\rm TN},v_{\rm TN}\rangle
 =-2M=-E.
\]
At the asymptotic radius \(R=cL,\ c^3=3/4\),
\[
-2M=-8\pi^2m_*\ell^2
\]
exactly, while \(-E\) differs by \(O(L^8)\).

A useful stronger consequence follows from Cauchy–Schwarz:
\[
\|q_{\rm TN}\|_2^2
 \ge
 \frac{\left|\int\langle q_{\rm TN},v_{\rm TN}\rangle\right|^2}
      {\|v_{\rm TN}\|_2^2}
 =4M.
\]
At \(R=cL\),
\[
\boxed{
\|q_{\rm TN}\|_2^2
 \ge16\pi^2m_*L^6.
}
\]
Thus the raw TN field definitively fails the desired \(o(L^6)\) squared-residual scale.

### TN/TNAdS ambiguity in the script

The script uses:

- TNAdS proper normal factor \(\sqrt{F/H}\) for `proper_dm_over_L`;
- TN formulas for `flux`, `tangent_energy`, and `grad_v_sq`.

For the scalar profile \(m=m_*R/(R+\ell)\), the TNAdS scalar flux would be
\[
\Phi_m^{\rm TNAdS}(R)
 =16\pi^2\ell R^2F(R)m'(R)
 =F(R)\Phi_m^{\rm TN}(R),
\]
not the value stored as `flux`.

More fundamentally, no actual TNAdS section has been specified whose norm is exactly \(m_*R/(R+\ell)\). If the base one-form \(d\bar f\) is simply retained under the TNAdS metric, then
\[
|v_0|_{\rm TNAdS}^2
 =\frac{m_*}{H}
 \left(1+\frac{F-1}{2}\sin^2\theta\right),
\]
so an \(O(L^2)\) angular correction already appears.

Thus equation (5.2) is exact for the raw TN harmonic field. For a specified TNAdS extension \(v^\sharp\), the exact identity is only
\[
\operatorname{Re}\int\langle q_{\rm AdS},v^\sharp\rangle
 =
E_{\rm AdS}-2M_{\rm AdS}
-\frac12\Phi_{m,\rm AdS}.
\]
Recovering \(-2M+o(L^6)\) requires actual estimates for
\[
E_{\rm AdS},\qquad M_{\rm AdS},\qquad \Phi_{m,\rm AdS},
\]
including the TNAdS spin connection and the chosen determinant connection.

Accordingly, the valid conclusion is:

> The balance radius cancels the desired leading energy–mass ledger, but the uncorrected TN tangent field has a leading \(q\)-pairing and cannot itself be the small-residual field. An actual TNAdS torsion/resolvent correction is necessary.

It is not yet established that the exact TNAdS raw continuation has precisely the coefficient claimed in (5.3).

---

## 6. Residual and Cauchy scales of the marked block

Because
\[
\operatorname{Vol}(\mathcal B_L)\asymp L^6,
\]
the conditions
\[
\|q_L\|_{L^2}=o(L^3),\qquad
\|t_{\Phi_L}-v_L\|_{H^1}=o(L^3)
\]
are the correct per-block scales, interpreted explicitly as
\[
\int|q_L|^2=o(L^6),
\]
and
\[
\int\bigl(|t_{\Phi_L}-v_L|^2+
 |\nabla(t_{\Phi_L}-v_L)|^2\bigr)=o(L^6).
\]
If \(v_L\) is uniformly bounded, then
\[
\left|\int\langle q_L,v_L\rangle\right|
 \le \|q_L\|_2\|v_L\|_2=o(L^6),
\]
which is exactly what the mass-flux identity requires.

The inherited type and Dirac residuals should be stated explicitly, if they are part of the target:
\[
\|D^-_{3A_L}v_L\|_2=o(L^3),\qquad
\|\mathsf P_{J_+}\nabla v_L\|_2=o(L^3),
\]
together with any remaining prolongation residuals. Global normalized estimates provide such bounds only for selected good blocks unless a uniform local theorem is proved.

### Natural boundary sizes

The leading model predicts
\[
\Phi-\Phi_0=O(L),\qquad
\nabla_\nu\Phi=O(1),\qquad
v=O(1),\qquad
\nabla_\nu v=O(L).
\]
Since \(\operatorname{Vol}(Y_L)\asymp L^5\),
\[
\|\Phi-\Phi_0\|_{L^2(Y_L)}=O(L^{7/2}),\qquad
\|\nabla_\nu\Phi\|_{L^2(Y_L)}=O(L^{5/2}),
\]
\[
\|v\|_{L^2(Y_L)}=O(L^{5/2}),\qquad
\|\nabla_\nu v\|_{L^2(Y_L)}=O(L^{7/2}).
\]
Any scale for \(A^{\tan}\) requires a chosen boundary gauge and sufficient curvature control; it should not be inferred solely from the available \(W^+\) and Ricci estimates.

The tuple in (6.4) is appropriately viewed as an **output record**, not freely prescribable Cauchy data. The monopole equations are first order modulo gauge, while the resolvent equation is second order. Simultaneously prescribing all traces and normal derivatives would generally overdetermine the problem. A precise boundary map must specify:

- temporal or Coulomb gauge;
- quotient by the boundary gauge group;
- Sobolev trace spaces;
- a common normal orientation;
- elliptic boundary projections for the Dirac component;
- reference trivializations for Chern–Simons and relative indices.

---

## 7. Computational status

The Step‑46 script correctly verifies:

\[
a=\frac{\sqrt2}{3},\qquad
\frac{2a^2}{m_*}=\frac9{32},\qquad
\text{parent density}=\frac89,
\]
the Hermite coefficient \(12\), and the TN pairing coefficient \(-2M\).

It does **not** compute:

- the TNAdS spin connection acting on the proposed negative spinor;
- \((\nabla^*_{3A}\nabla_{3A}-2)v\) on TNAdS;
- the determinant-curvature equation;
- the nonlinear cubic torsion;
- existence of the finite marked block.

Also, the supplied `verify_gh_tangent.py` is not directly executable as written: it uses `sqrtg` and `cs` before their definitions. Its analytic TN claims can still be checked independently, but the script needs reordering before it serves as reproducible verification.

## Precise unresolved object

The remaining local problem is to choose an actual Spin\(^c\) extension on the exact TNAdS block and solve, with coherent boundary jet,
\[
D_A^+\Phi=0,\qquad F_A^+=2i\sigma(\Phi),
\]
together with
\[
v\approx t_\Phi,\qquad
(\nabla^*_{3A}\nabla_{3A}-2)v=q,\qquad
\|q\|_2=o(L^3),
\]
plus the inherited Dirac/type projections. The decisive quantities are the resulting complete boundary map and
\[
E_{\rm AdS}-2M_{\rm AdS}
-\frac12\Phi_{m,\rm AdS}
 =\operatorname{Re}\int\langle q,v\rangle.
\]
This calculation determines whether the TN leading pairing can be corrected to \(o(L^6)\), or whether a nonzero order-\(L^6\) obstruction remains.