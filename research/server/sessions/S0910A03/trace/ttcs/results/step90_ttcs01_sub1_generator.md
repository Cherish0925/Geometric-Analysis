# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step89_twist_bochner_and_resolvent.md",
    "Sessions/S0910A03/workspace/scripts/step90_charge_potential_verify.py",
    "Sessions/S0910A03/workspace/data/step90_charge_potential_verify.json",
    "Sessions/S0910A03/workspace/scripts/step90_exchange_inequality_verify.py",
    "Sessions/S0910A03/workspace/data/step90_exchange_inequality_verify.json",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step88_source_note_twist.md"
  ]
}
```

## Task

Develop the structured Maxwell-area-orbit-map system for an approximately Einstein free-T^2 metric after the Step 90 charge-potential cancellation. Starting from Q=(1/2)e^{-3σ}q^T M^{-1}q, S_F=-grad_H Q, the mixed Ricci law for dq, Lσ=6+Q-tr_orb E, and the base drift equation, look for a geometrically natural energy or variable-potential comparison that controls physical twist without differentiating Ricci defect. Explore combinations of orbit energy e, |∇σ|^2, Q, and the normalized physical charge amplitude, and distinguish what can be proved from what merely looks plausible. Identify either (i) a coercive inequality compatible with exact OT ends and a minimal separator, or (ii) a concrete concentration/escape mechanism consistent with all reduced equations. Provide explicit equations and the most decisive next computation or proof, not broad brainstorming.

## Output

### 1. Reduced system and the normalization that matters

Let  
\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
G=e^\sigma M,\quad \det M=1,\quad \rho=e^\sigma,
\]
on a free \(T^2\)-region over a surface \(B\). Put
\[
L=\Delta_\gamma+\langle\nabla\sigma,\nabla\cdot\rangle,\qquad
e=|dU|^2,\qquad p^2=|\nabla\sigma|^2,
\]
where \(U:B\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2\) is represented by \(M\). The twist charge and twist energy are
\[
q_a=\rho G_{ab}(*_\gamma F^b),\qquad
Q=\frac12e^{-3\sigma}q^TM^{-1}q.
\]

For the approximately Einstein tensor
\[
E=\operatorname{Ric}_g+3g,
\]
write
\[
T=\operatorname{tr}_{\rm orb}E,\qquad
\Theta=\tau_\sigma(U)-S,\qquad S=-\nabla_{\mathbb H^2}Q.
\]
Then the reduced equations are
\[
\boxed{\tau_\sigma(U)=S+\Theta,}
\]
\[
\boxed{L\sigma=6+Q-T,}
\]
\[
\boxed{\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
=(-3+Q)\gamma+\frac12U^*h_{\mathbb H^2}+E_B.}
\]
The mixed Ricci law gives the normalized charge derivative
\[
b_i=e^{-3\sigma/2}M^{-1/2}\nabla_iq,\qquad
|b|^2=e^{-3\sigma}M^{ab}\gamma^{ij}(\nabla_iq_a)(\nabla_jq_b)
=4|E_{\rm mix}|_{\rm HS}^2.
\]
Thus under \(\|E\|_{\rm op}\le\delta\),
\[
|\Theta|\le2\delta,\qquad |T|\le2\delta,\qquad |b|\le2\sqrt2\,\delta,\qquad |E_B|\le\delta .
\]

A normalization point that affects every estimate is
\[
\boxed{\operatorname{Hess}_{\mathbb H^2}Q=Qh_{\mathbb H^2},\qquad
|\nabla_{\mathbb H^2}Q|^2=Q^2.}
\]
Therefore, for
\[
\zeta_i=\langle\nabla Q,U_i\rangle,\qquad
m_i=D_qQ[\nabla_iq],
\]
one has
\[
|\zeta|\le Q\sqrt e,\qquad |m|\le\sqrt{2Q}\,|b|.
\]
The exchange term satisfies
\[
X:=\langle d\sigma,\zeta\rangle,\qquad |X|\le p\,Q\sqrt e,
\]
while the charge-variation term from Step 90 obeys
\[
R_q:=\sum_i\langle U_i,D_qS[\nabla_iq]\rangle,\qquad
|R_q|\le\sqrt{2Qe}\,|b|.
\]

---

### 2. Structured Bochner identity after the charge-potential cancellation

Let
\[
A_{ij}=\langle U_i,U_j\rangle,\qquad
A_{\sigma\sigma}=|dU(\nabla\sigma)|^2,
\]
and
\[
\Phi(A)=\frac12\operatorname{tr}(A^2)+2\det A\ge\frac12e^2.
\]
Using
\[
\langle dU,DS\rangle=-Qe+3X+R_q
\]
and the \(+Qe\) term in the base drift curvature, the \(Qe\) terms cancel. With
\[
V_\Theta(X)=\langle dU(X),\Theta\rangle,
\]
the exact pointwise identity is
\[
\boxed{
\begin{aligned}
\frac12Le
&=|D dU|^2+\frac12A_{\sigma\sigma}+\Phi(A)-3e
+3X+R_q \\
&\quad +E_B:A+\operatorname{div}_\sigma V_\Theta
+\langle\nabla Q,\Theta\rangle-|\Theta|^2 .
\end{aligned}}
\tag{2.1}
\]
This is the useful form: no derivative of \(E\) appears. The price is the exchange term \(3X\), which is too large to estimate directly unless \(Q\) is already controlled.

---

### 3. Flux-form \(LQ\): including \(Q\) without differentiating mixed Ricci

A direct \(LQ\) calculation would contain \(Lq\), hence derivatives of the mixed defect. The right way is to put that part into divergence form. Let
\[
P_a=\frac{\partial Q}{\partial q_a}=e^{-3\sigma}(M^{-1}q)^a,\qquad
Z_Q=\sum_aP_a\nabla q_a .
\]
Then
\[
|Z_Q|=|m|\le\sqrt{2Q}\,|b|.
\]

Modulo the weighted divergence \(\operatorname{div}_\sigma Z_Q\), all \(q\)-terms reduce to first derivatives:
\[
\boxed{
\begin{aligned}
LQ
&=\operatorname{div}_\sigma Z_Q
+Qe-4Q^2-18Q+3QT+9Qp^2 \\
&\quad -6X-R_q-3Y+\langle\nabla Q,\Theta\rangle,
\end{aligned}}
\tag{3.1}
\]
where
\[
Y=\langle d\sigma,m\rangle,\qquad |Y|\le p\sqrt{2Q}\,|b|.
\]

The scalar area-gradient Bochner identity is
\[
\boxed{
\begin{aligned}
\frac12L p^2
&=|\operatorname{Hess}\sigma|^2-3p^2-2Qp^2+\frac12p^4
+\frac12A_{\sigma\sigma}+E_B(\nabla\sigma,\nabla\sigma) \\
&\quad +X+Y-\operatorname{div}_\sigma(T\nabla\sigma)
+T(6+Q-T).
\end{aligned}}
\tag{3.2}
\]

Equations (2.1), (3.1), and (3.2) contain the full Maxwell-area-orbit coupling using only \(E\), not \(\nabla E\).

---

### 4. The natural cancellation energy

The coefficients in (2.1), (3.1), (3.2) single out
\[
\boxed{W=e+2Q+3|\nabla\sigma|^2.}
\]
Indeed,
\[
\frac12LW=\frac12Le+LQ+\frac32L|\nabla\sigma|^2,
\]
and the three troublesome first-order exchanges cancel exactly:
\[
3X-6X+3X=0,
\]
\[
R_q-R_q=0,
\]
\[
-3Y+3Y=0.
\]

Thus one obtains the structured identity
\[
\boxed{
\begin{aligned}
\frac12LW
&=\operatorname{div}_\sigma\mathcal J
+|DdU|^2+3|\operatorname{Hess}\sigma|^2
+2A_{\sigma\sigma}+\Phi(A)\\
&\quad +\frac32p^4+3Qp^2+Qe
-3e-9p^2-18Q-4Q^2\\
&\quad +E_B:A+3E_B(\nabla\sigma,\nabla\sigma)
+2\langle\nabla Q,\Theta\rangle-|\Theta|^2\\
&\quad +18T+6QT-3T^2,
\end{aligned}}
\tag{4.1}
\]
with flux
\[
\boxed{\mathcal J=V_\Theta+Z_Q-3T\nabla\sigma.}
\tag{4.2}
\]
The flux is small in the exact sense
\[
|\mathcal J|
\le |\Theta|\sqrt e+\sqrt{2Q}|b|+3|T|p
\le (2+2\sqrt2+2\sqrt3)\delta\,\sqrt W.
\tag{4.3}
\]

This is the cleanest energy identity presently visible. It is geometrically natural: \(e\) is orbit-shape energy, \(2Q\) is twice physical twist energy, and \(3|\nabla\sigma|^2\) is forced by the area equation. The coefficients are not adjustable if one wants simultaneous cancellation of \(X\), \(R_q\), and \(Y\).

---

### 5. What the \(W\)-identity gives, and what it does not give by itself

The identity (4.1) is strong because it packages every derivative of the charge into the flux \(\mathcal J\), whose size is controlled by \(\delta\sqrt W\). It is exactly the structure needed for a massive-resolvent or Caccioppoli argument without differentiating the Ricci defect.

However, the zero-order part of (4.1) is not coercive in \(W\). The obstruction is not a bookkeeping artifact; it is built into the reduced equations.

At a point with
\[
d\sigma=0,\qquad dU=0,\qquad dq=0,\qquad T=\Theta=E_B=0,
\]
take \(Q=Q_0>0\). The exact reduced equations can be satisfied at second order by choosing, in normal base coordinates and in a target geodesic coordinate \(\alpha\) aligned with \(q\),
\[
\sigma=\sigma_0+\frac{6+Q_0}{4}|x|^2+O(|x|^3),
\]
\[
\alpha=\alpha_0+\frac{Q_0}{4}|x|^2+O(|x|^3),
\]
\[
K_\gamma(x_0)=\frac32Q_0.
\]
Then
\[
L\sigma(x_0)=6+Q_0,\qquad \tau_\sigma(U)(x_0)=S(x_0),\qquad
\operatorname{Ric}_B-\operatorname{Hess}\sigma=(-3+Q_0)\gamma .
\]
At this point
\[
W(x_0)=2Q_0,
\]
and the exact right-hand side of (4.1), with the Hessian terms evaluated from the equations, equals
\[
3|\operatorname{Hess}\sigma|^2+|DdU|^2-18Q_0-4Q_0^2
=\frac32(6+Q_0)^2+\frac12Q_0^2-18Q_0-4Q_0^2
=54-2Q_0^2.
\]
Thus no inequality of the form
\[
\frac12LW\ge \operatorname{div}_\sigma\mathcal J+aW^2-bW-C
\]
with \(a>0\) can follow from the variables \(e,Q,|\nabla\sigma|^2\) alone. Large physical twist can sit at a common critical point of \(\sigma\) and \(U\), with the area Hessian and orbit Hessian satisfying the exact equations, while the \(W\)-reaction carries a \(-2Q_0^2\) contribution.

So the \(W\)-identity is the right cancellation identity, but it is not yet a pointwise ceiling mechanism for \(Q\).

---

### 6. First-order physical twist transport

Let
\[
w=\sqrt{2Q}=e^{-3\sigma/2}|M^{-1/2}q|.
\]
From \(dQ=-3Q\,d\sigma+\zeta+m\), one obtains the invariant first-order inequality
\[
\boxed{
|dw+\tfrac32w\,d\sigma|
\le \frac12w\,|dU|+|b|.
}
\tag{6.1}
\]
In a diagonal charge orientation, \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\), \(q=(q_1,0)\), this becomes the exact scalar equation
\[
\boxed{
w'+\frac12(3\sigma'+\alpha')w=b,
\qquad
w=e^{-(3\sigma+\alpha)/2}q_1.
}
\tag{6.2}
\]
On the round expanding cusp, \(\sigma'=2,\alpha'=0\), hence
\[
w'+3w=b.
\]
Forward along the cusp, \(w\) is damped. But if an exact OT end imposes \(w=0\) after some open tail, then a small \(b\) in a transition layer can cancel a previously damped value of \(w\). Running the equation inward, the same damping becomes exponential amplification.

This is the essential Maxwell-area mechanism: exact OT ends force \(q=0\) on the end, but approximate mixed Ricci only controls \(b\), and \(b\) is measured after multiplication by \(e^{-3\sigma/2}M^{-1/2}\). A large interior coordinate charge can be removed where the physical amplitude \(w\) has already been red-shifted to \(O(\delta)\).

---

### 7. Concrete concentration mechanism consistent with the reduced equations

A high-twist core can be seeded by an exact local solution jet with constant charge.

Use a local polar base disk with
\[
\gamma=dr^2+\psi(r)^2d\theta^2,
\]
diagonal orbit map \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\), and \(q=(q_0,0)\) on the core. Then
\[
Q=\frac12e^{-3\sigma-\alpha}q_0^2,
\]
and the exact radial reduced equations are
\[
\sigma''+\left(\frac{\psi'}{\psi}+\sigma'\right)\sigma'=6+Q,
\]
\[
\alpha''+\left(\frac{\psi'}{\psi}+\sigma'\right)\alpha'=Q,
\]
\[
K-\sigma''=-3+Q+\frac12(\sigma')^2+\frac12(\alpha')^2,
\]
\[
K-\frac{\psi'}{\psi}\sigma'=-3+Q,
\qquad K=-\frac{\psi''}{\psi}.
\]
At \(r=0\), smoothness gives
\[
\psi(r)=r-\frac{K_0}{6}r^3+O(r^5),
\]
and the exact equations impose
\[
\sigma(r)=\sigma_0+\frac{6+Q_0}{4}r^2+O(r^4),
\]
\[
\alpha(r)=\alpha_0+\frac{Q_0}{4}r^2+O(r^4),
\]
\[
K_0=\frac32Q_0.
\]
The physical amplitude then satisfies
\[
w'+D(r)w=0,\qquad D(r)=\frac12(3\sigma'+\alpha').
\]
Near the core,
\[
D(r)=\left(Q_0+\frac92\right)r+O(r^3),
\]
so
\[
w(r)\approx w_0\exp\!\left[-\frac12\left(Q_0+\frac92\right)r^2\right].
\]
Thus a core with \(Q_0\gg1\) red-shifts its own physical twist over radius
\[
r\sim \sqrt{\frac{\log(w_0/\delta)}{Q_0}}.
\]
After that radius, \(w\) can be \(O(\delta)\). One may then taper \(q\) to zero with
\[
|b|=\left|e^{-(3\sigma+\alpha)/2}q'\right|\le 2\sqrt2\,\delta,
\]
because the taper occurs where the physical amplitude is already small. The remaining end can be exactly OT, \(q=0\), with constant \(U\).

This mechanism is compatible with the reduced equations at the core, with the mixed Ricci law in the taper, and with exact OT ends. The minimal-separator identity is not contradicted: any completed metric still satisfies
\[
\langle e_s\rangle\ge 12+2\langle Q\rangle-8\delta,
\]
and the charged region supplies large orbit/area curvature where a minimizing separator samples it, while a separator in a low-\(Q\) collar only sees the usual OT floor.

The decisive unresolved mathematical substance is not an \(e\)-Bochner sign; it is whether this red-shift/taper profile can be promoted from formal local jets to a complete two-ended free-\(T^2\) metric with all components of \(E\) uniformly \(O(\delta)\), or whether some global identity couples the red-shift integral to the separator floor strongly enough to forbid it.

---

### 8. The decisive computation/proof object

The sharp low-dimensional model is the diagonal radial core plus taper system:
\[
\gamma=dr^2+\psi(r)^2d\theta^2,\qquad
M=\operatorname{diag}(e^\alpha,e^{-\alpha}),\qquad
q=(q(r),0),
\]
\[
Q=\frac12e^{-3\sigma-\alpha}q^2,
\]
\[
w=e^{-(3\sigma+\alpha)/2}q,\qquad
w'+\frac12(3\sigma'+\alpha')w=b,
\]
with defect variables measured directly by
\[
T=6+Q-L\sigma,
\]
\[
\Theta_\alpha=L\alpha-Q,
\]
\[
E_{rr}=K-\sigma''+3-Q-\frac12(\sigma')^2-\frac12(\alpha')^2,
\]
\[
E_{\theta\theta}=K-\frac{\psi'}{\psi}\sigma'+3-Q,
\]
\[
b=e^{-(3\sigma+\alpha)/2}q'.
\]
The core has \(b=T=\Theta=E_B=0\) to the computed order; the taper is acceptable precisely when
\[
|b|,\ |T|,\ |\Theta|,\ |E_B|\le C\delta
\]
while \(q\) reaches zero before the exact OT end.

If this model can be integrated and matched with those inequalities, it gives an explicit twist escape inside the free-\(T^2\) reduction. If instead one proves a Hardy-type estimate from exact OT end data,
\[
\|w\|_{L^\infty(B)}
\le C\|b\|_{L^\infty(B)}
\]
with \(C\) independent of red-shift length and compatible with the separator geometry, then \(Q=O(\delta^2)\), and the Step 87/89 resolvent obstruction becomes stable under approximate twist. The \(W=e+2Q+3|\nabla\sigma|^2\) identity is the natural analytic object for that proof, because it is the only combination above that cancels \(X\), \(R_q\), and \(Y\) without differentiating the Ricci defect.