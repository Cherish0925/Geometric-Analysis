# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step94_horizontal_noether_identity.py",
    "Sessions/S0910A03/workspace/data/step94_horizontal_noether_identity.json",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md"
  ]
}
```

## Task

Verify the proposed invariant horizontal Noether/Bianchi identity for the full two-dimensional free-T2 reduction. With horizontal residual H=Ric_B-Hess sigma-(1/2)d sigma^2-(1/2)U*h-Q gamma+3 gamma, area residual T=L sigma-6-Q, orbit residual Z=tau_sigma(U)+grad_U Q, and variable-charge work one-form m_q=D_qQ[dq]=e^{-3sigma}<M^-1q,dq>, check whether
2 div_sigma H-d tr H = -dT-T d sigma-<Z,dU>-m_q
is exactly correct in signs and coefficients. Derive it independently using contracted Bianchi, harmonic-map stress divergence, and the total differential dQ=d_UQ-3Q d sigma+D_qQ[dq]. Then specialize to gamma=dr^2+psi^2dtheta^2, H=C dr^2, T=Z=0, diagonal charge, and verify it gives C'=-2(u+h)C-wb with the Step90 physical normalization. Explain whether this identity supplies a genuinely independent two-ended constraint or is a propagation/compatibility identity, and identify the most useful global adjoint pairing or moment it yields when q and H vanish on exact end collars but T,Z and Ricci defects are only C0-small. Flag any issue arising because H,T,Z are all blocks of the same Ricci defect rather than independent sources.

## Output

# Scientific verification memo

## 1. Result and conventions

With
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle,\qquad
\tau_\sigma(U)=\tau(U)+dU(\nabla\sigma),
\]
and divergence taken in the first tensor index, the identity
\[
\boxed{
2\operatorname{div}_\sigma H-d\operatorname{tr}H
=-dT-T\,d\sigma-\langle Z,dU\rangle-m_q
}
\]
is exactly correct for
\[
T=L\sigma-6-Q,\qquad
Z=\tau_\sigma(U)+\nabla_UQ,
\]
\[
m_q=D_qQ[dq]=e^{-3\sigma}\langle M^{-1}q,dq\rangle.
\]
All signs and factors \(1/2,2,3\) agree.

Here \(\langle Z,dU\rangle\) denotes the one-form
\[
\langle Z,dU\rangle_j=\langle Z,dU(\partial_j)\rangle_h.
\]

There is one important notation conversion relative to Step 90. There,
\(T_{90}=\operatorname{tr}_{\rm orb}E\) and
\[
L\sigma=6+Q-T_{90}.
\]
Thus
\[
T_{\rm here}=L\sigma-6-Q=-T_{90}.
\]
If the Step 90 block variable is used instead, the two \(T\)-terms in the identity become
\[
+dT_{90}+T_{90}\,d\sigma.
\]

---

## 2. Independent tensor derivation

Set
\[
s=d\sigma,\qquad A=U^*h,\qquad e=\operatorname{tr}_\gamma A=|dU|^2.
\]
On the two-dimensional base,
\[
H=\operatorname{Ric}
-\operatorname{Hess}\sigma-\frac12s\otimes s
-\frac12A-Q\gamma+3\gamma.
\]

Its trace is
\[
\operatorname{tr}H
=R-\Delta\sigma-\frac12|s|^2-\frac12e-2Q+6.
\tag{2.1}
\]

The required covariant identities are
\[
\operatorname{div}\operatorname{Ric}=\frac12dR,
\]
\[
\operatorname{div}\operatorname{Hess}\sigma
=d\Delta\sigma+\operatorname{Ric}(\nabla\sigma,\cdot),
\]
\[
\operatorname{div}(s\otimes s)
=(\Delta\sigma)s+\operatorname{Hess}\sigma(\nabla\sigma,\cdot),
\]
and, equivalently to harmonic-map stress conservation,
\[
\operatorname{div}A
=\langle\tau(U),dU\rangle+\frac12de.
\tag{2.2}
\]

Substituting these into \(\operatorname{div}H\), and using
\[
d|s|^2=2\operatorname{Hess}\sigma(\nabla\sigma,\cdot),
\]
gives the useful intermediate formula
\[
\operatorname{div}H
=\frac12d\operatorname{tr}H-\frac12d\Delta\sigma
-\operatorname{Ric}(\nabla\sigma,\cdot)
-\frac12(\Delta\sigma)s
-\frac12\langle\tau(U),dU\rangle.
\tag{2.3}
\]

From the definition of \(H\),
\[
\begin{aligned}
\operatorname{Ric}(\nabla\sigma,\cdot)
={}&H(\nabla\sigma,\cdot)
+\operatorname{Hess}\sigma(\nabla\sigma,\cdot)
+\frac12|s|^2s\\
&+\frac12A(\nabla\sigma,\cdot)+(Q-3)s.
\end{aligned}
\tag{2.4}
\]
Adding \(H(\nabla\sigma,\cdot)\) to form \(\operatorname{div}_\sigma H\), and using
\[
A(\nabla\sigma,\cdot)
=\langle dU(\nabla\sigma),dU\rangle,
\]
yields
\[
\operatorname{div}_\sigma H
=\frac12d\operatorname{tr}H-\frac12dL\sigma
-\frac12\langle\tau_\sigma(U),dU\rangle
+\left(3-Q-\frac12L\sigma\right)d\sigma.
\tag{2.5}
\]

Now insert
\[
L\sigma=6+Q+T,\qquad dL\sigma=dQ+dT:
\]
\[
\begin{aligned}
\operatorname{div}_\sigma H
={}&\frac12d\operatorname{tr}H-\frac12dT-\frac12dQ
-\frac12\langle\tau_\sigma(U),dU\rangle\\
&-\frac32Q\,d\sigma-\frac12T\,d\sigma.
\end{aligned}
\tag{2.6}
\]

For
\[
Q(\sigma,U,q)=\frac12e^{-3\sigma}q^TM(U)^{-1}q,
\]
the total differential is
\[
\boxed{
dQ=d_UQ-3Q\,d\sigma+m_q,
}
\tag{2.7}
\]
where
\[
d_UQ=\langle\nabla_UQ,dU\rangle,\qquad
m_q=e^{-3\sigma}\langle M^{-1}q,dq\rangle.
\]
Also,
\[
\tau_\sigma(U)=Z-\nabla_UQ.
\]
Consequently,
\[
-\frac12dQ-\frac12\langle\tau_\sigma(U),dU\rangle
=
\frac32Q\,d\sigma-\frac12m_q-\frac12\langle Z,dU\rangle.
\tag{2.8}
\]
This cancels the \(-\frac32Q\,d\sigma\) term in (2.6), leaving
\[
\operatorname{div}_\sigma H
=\frac12d\operatorname{tr}H-\frac12dT
-\frac12T\,d\sigma-\frac12\langle Z,dU\rangle-\frac12m_q.
\]
Multiplication by two and subtraction of \(d\operatorname{tr}H\) gives the proposed identity.

The supplied SymPy file reproduces the same component expression,
\[
\frac12d\operatorname{tr}H-\frac12dT
-\frac12T\,d\sigma-\frac12\langle Z,dU\rangle-\frac12m_q.
\]
That script verifies coefficient substitution after the covariant divergence formulas have been entered; the derivation above independently establishes those geometric steps.

---

## 3. Radial specialization

Let
\[
\gamma=dr^2+\psi(r)^2d\theta^2,\qquad
u=\sigma',\qquad h=\frac{\psi'}{\psi},
\]
and write the horizontal residual tensor as
\[
H=C(r)\,dr^2.
\]
Then
\[
\operatorname{tr}H=C,
\]
and direct computation with the warped-product connection gives
\[
(\operatorname{div}H)_r=C'+hC.
\]
Therefore
\[
(\operatorname{div}_\sigma H)_r=C'+(u+h)C
\]
and
\[
\left(2\operatorname{div}_\sigma H-d\operatorname{tr}H\right)_r
=C'+2(u+h)C.
\tag{3.1}
\]

For
\[
M=\operatorname{diag}(e^\alpha,e^{-\alpha}),\qquad q=(q(r),0),
\]
define the signed physical charge and source
\[
\widetilde w=e^{-(3\sigma+\alpha)/2}q,\qquad
b=e^{-(3\sigma+\alpha)/2}q'.
\]
Then
\[
Q=\frac12\widetilde w^{\,2},
\qquad
m_q(\partial_r)
=e^{-3\sigma-\alpha}qq'
=\widetilde w\,b.
\tag{3.2}
\]
On the Step 90 taper, where \(q\ge0\), \(\widetilde w=w=\sqrt{2Q}\). If \(q\) changes sign, using \(w=\sqrt{2Q}\) instead gives
\[
m_q=\operatorname{sgn}(q)\,w\,b;
\]
the signed \(\widetilde w\) avoids this ambiguity.

With \(T=Z=0\), equations (3.1)–(3.2) give
\[
C'+2(u+h)C=-wb,
\]
or
\[
\boxed{
C'=-2(u+h)C-wb.
}
\]
Thus the coefficient and sign agree exactly with Step 90. There is no extra factor \(1/2\): Step 90’s mixed Ricci component is \(b/2\), while the charge-work term itself is \(wb\).

---

## 4. Global weighted adjoint pairing

Let
\[
d\mu_\sigma=e^\sigma d\mu_\gamma.
\]
For a smooth vector field \(X\) vanishing on chosen end cuts, weighted integration by parts gives
\[
\boxed{
\begin{aligned}
\int_B m_q(X)\,d\mu_\sigma
=\int_B\Big[
&2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X\\
&+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\Big]\,d\mu_\sigma .
\end{aligned}}
\tag{4.1}
\]
No derivatives of \(H,T,Z\) occur. This is the main weak form available when the Ricci residual is controlled only in \(C^0\).

For \(X=\nabla\phi\),
\[
\boxed{
\begin{aligned}
\int_Bm_q(\nabla\phi)\,d\mu_\sigma
=\int_B\Big[
&2H:\operatorname{Hess}\phi
-(\operatorname{tr}H)L\phi\\
&+T\Delta\phi
-\langle Z,dU(\nabla\phi)\rangle
\Big]\,d\mu_\sigma .
\end{aligned}}
\tag{4.2}
\]
A useful choice is an end-separating \(\phi\), constant on deep portions of both exact collars and adapted to the formal adjoint of
\[
H\longmapsto2\operatorname{div}_\sigma H-d\operatorname{tr}H.
\]

If \(q=0\) on the collars, then \(Q=0\) there and the total differential can be integrated once more:
\[
\begin{aligned}
\int_Bm_q(X)\,d\mu_\sigma
=\int_B\Big[
Q(-\operatorname{div}X+2X\sigma)
-\langle\nabla_UQ,dU(X)\rangle
\Big]d\mu_\sigma.
\tag{4.3}
\]
Equating (4.1) and (4.3) gives a fully zeroth-order, geometry-coupled charge pairing. It uses neither \(dT\) nor derivatives of the Ricci residual.

If \(X\) does not vanish at the end cuts, the additional term is
\[
\sum_{\Sigma_\pm}\int_{\Sigma_\pm}e^\sigma
\left[
-2H(\nu,X)+(\operatorname{tr}H-T)\langle\nu,X\rangle
\right]dS_\gamma.
\tag{4.4}
\]
Thus \(H=0\) alone does not remove every end contribution when \(T\) is merely small; either \(T\) must vanish there or \(X\) should be tapered to zero inside the collars.

---

## 5. The radial adjoint moment

For the radial rank-one tensor, choose
\[
\phi'=e^\sigma\psi.
\]
Then
\[
\phi''=(u+h)\phi',
\]
and hence
\[
2H:\operatorname{Hess}\phi-(\operatorname{tr}H)L\phi=0.
\]
The corresponding integrating factor is
\[
\mu=e^{2\sigma}\psi^2,\qquad \mu'=2(u+h)\mu.
\]

For general radial \(T,Z\), the tensor identity becomes
\[
C'+2(u+h)C
=-T'-uT-\langle Z,U'\rangle-m_q(\partial_r).
\]
Multiplication by \(\mu\) and one integration gives
\[
\boxed{
[\mu(C+T)]_{r_-}^{r_+}
+\int_{r_-}^{r_+}\mu
\left[
m_q(\partial_r)+\langle Z,U'\rangle-(u+2h)T
\right]dr=0.
}
\tag{5.1}
\]

If \(C=T=0\) at both end cuts,
\[
\boxed{
\int_{r_-}^{r_+}e^{2\sigma}\psi^2
\left[
wb+\langle Z,U'\rangle-(u+2h)T
\right]dr=0.
}
\tag{5.2}
\]
In the Step 90 setting \(T=Z=0\), this reduces to the second weighted moment
\[
\boxed{
\int_{r_-}^{r_+}e^{2\sigma}\psi^2\,wb\,dr=0.
}
\tag{5.3}
\]
Equivalently, for one-sided initial data \(C(r_-)=0\),
\[
C(r)
=-\frac1{e^{2\sigma(r)}\psi(r)^2}
\int_{r_-}^{r}e^{2\sigma}\psi^2\,wb\,ds.
\tag{5.4}
\]
This is precisely the Step 90 propagation formula. It is distinct from the ordinary charge-flux relation \(\int q'\,dr=0\).

For diagonal \(M\), writing \(v=\alpha'\),
\[
wb=Q'+(3u+v)Q.
\]
When \(q=0\) at both ends, (5.3) is equivalently
\[
\boxed{
\int e^{2\sigma}\psi^2\,(u+v-2h)Q\,dr=0.
}
\tag{5.5}
\]
This version contains no derivative of the mixed source and may be useful for sign analysis of a proposed two-ended throat.

---

## 6. Scientific interpretation

The identity is a Bianchi/Noether propagation relation, not an additional local field equation. For a metric from the full free-\(T^2\) reduction it holds automatically.

It nevertheless produces a substantive solvability relation when only part of the reduced equations is imposed. In the radial taper:

- setting \(T=Z=0\) and the angular horizontal component to zero does not leave \(C\) freely adjustable;
- the mixed forcing \(b\) propagates \(C\) through (5.4);
- requiring \(C=0\) at both ends imposes the weighted work moment (5.3).

The residual blocks are linked even before this differential identity is used. In the Step 90 normalization,
\[
H=E_B,\qquad
T_{\rm here}=-\operatorname{tr}_{\rm orb}E,\qquad
Z=-2\widehat E_{\rm orb,0},
\]
while \(dq\) is proportional to \(E_{\rm mix}\). Thus \(H,T,Z,b\) are not separately specifiable source functions. An arbitrary \(b\) together with \(H=T=Z=0\) need not arise from any metric; in the rank-one radial system, the identity explicitly forces the resulting \(C\).

Finally, the adjoint pairing does not by itself turn \(C^0\)-small Ricci residual into a uniformly small charge-work moment. Indeed,
\[
|m_q|\le \sqrt{2Q}\,|b|,
\]
and (4.2) contains weighted integrals involving \(|dU||d\phi|\), \(|\operatorname{Hess}\phi|\), and the connector volume. These factors may grow strongly in an expanding region. The identity therefore supplies an exact signed moment and removes derivatives of the Ricci residual, but a quantitative two-ended obstruction additionally requires geometry-controlled adjoint norms or a sign mechanism for the weighted integrand.