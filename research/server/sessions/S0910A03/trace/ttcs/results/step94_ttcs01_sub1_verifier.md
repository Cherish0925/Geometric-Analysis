# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/scripts/step94_invariant_charge_identity.py",
    "Sessions/S0910A03/workspace/data/step94_invariant_charge_identity.json",
    "Sessions/S0910A03/workspace/scripts/step94_scalar_superharmonic_countermodel.py",
    "Sessions/S0910A03/workspace/data/step94_scalar_superharmonic_countermodel.json",
    "Sessions/S0910A03/workspace/notes/step93_signed_transport_and_koiso_ot.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/workspace/notes/step88_source_note_twist.md",
    "Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md"
  ]
}
```

## Task

Independently check the Step 94 correction and invariant full-charge derivation. In the convention L=Delta+grad sigma·grad, verify that the diagonal identity LQ=|dQ|^2/Q-18Q-4Q^2 does not exclude an interior maximum and that the scalar even solution y''=-18-4e^y is a valid sign countermodel. Then verify, for fixed nonzero q and F(U)=1/2 q^T M(U)^-1q, beta=log F, using Hess F=Fh and |grad F|^2=F^2 together with L sigma=6+Q and tau_sigma(U)=-Q grad beta, that L log Q=-18-4Q+e-|d(beta o U)|^2. Check all signs and normalizations against the supplied reduction notes/scripts. Assess precisely what remains valid from exact charge conservation and the OT Bochner/resolvent obstruction, versus what must be withdrawn. Finally analyze the proposed two-ended vector-charge flux pairing: identify the strongest derivative-free identity obtainable from Liu's mixed Ricci law, and whether separator stability plus both exact OT end collars presently provide any coercive amplitude bound or whether an additional weighted capacity/area estimate is indispensable. Give a direct mathematical memo, not procedural advice.

## Output

# Scientific verification memo

## 1. Diagonal identity and the maximum principle

For
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle
\]
the drift chain rule gives, wherever \(Q>0\),
\[
L\log Q=\frac{LQ}{Q}-\frac{|dQ|^2}{Q^2}.
\]
Thus
\[
LQ=\frac{|dQ|^2}{Q}-18Q-4Q^2
\]
is exactly equivalent to
\[
L\log Q=-18-4Q.
\]

At an interior maximum \(p\),
\[
dQ(p)=0,\qquad LQ(p)=\Delta Q(p)\le 0.
\]
The equation then gives
\[
LQ(p)=-18Q(p)-4Q(p)^2<0,
\]
which is fully compatible with the maximum principle. The same observation applies to \(\log Q\). The equation instead excludes a positive interior local minimum in the diagonal case, since there \(L\log Q\ge0\).

Hence the former inference excluding an interior positive maximum has the inequality direction reversed.

### Scalar sign countermodel

Consider
\[
y''=-18-4e^y,\qquad y(0)=\log Q_0,\qquad y'(0)=0,\qquad Q_0>0.
\]
Multiplication by \(2y'\) gives
\[
\frac{d}{dx}(y')^2
=-36y'-8e^yy',
\]
and therefore
\[
(y')^2=36(\log Q_0-y)+8(Q_0-e^y).
\]
This is the stated first integral.

The solution is even by uniqueness. For \(x>0\),
\[
y''<-18,\qquad y'(x)<0,\qquad y(x)\le \log Q_0-9x^2.
\]
Since \(e^{y(x)}\le Q_0\), the acceleration stays between two finite constants on each finite interval, so the solution extends for all \(x\). The preceding quadratic estimate gives
\[
y(x)\longrightarrow-\infty,\qquad e^{y(x)}\longrightarrow0
\]
as \(x\to\pm\infty\). Moreover,
\[
Q''(0)=Q_0y''(0)=Q_0(-18-4Q_0)<0,
\]
so \(Q=e^y\) has a strict positive maximum \(Q_0\) at the origin.

This analytically establishes the countermodel. The four numerical runs agree: monotonicity on \(x\ge0\) is recorded as true, and the first-integral residuals lie between \(8.99\times10^{-10}\) and \(9.60\times10^{-10}\). It is only a scalar elliptic sign model; it does not satisfy the coupled reduced Einstein system.

## 2. Fixed full charge on \(\mathbb H^2\)

To avoid confusing the Iwasawa coordinate with \(\log F\), write that coordinate as \(\zeta\):
\[
M=
\begin{pmatrix}
e^\alpha+\zeta^2e^{-\alpha}&\zeta e^{-\alpha}\\
\zeta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\qquad
h=d\alpha^2+e^{-2\alpha}d\zeta^2.
\]
For \(q=(q_1,q_2)\ne0\),
\[
F=\frac12q^TM^{-1}q
=\frac12\left[e^{-\alpha}(q_1-\zeta q_2)^2+e^\alpha q_2^2\right]>0.
\]
The nonzero Christoffel symbols are
\[
\Gamma^\alpha_{\zeta\zeta}=e^{-2\alpha},
\qquad
\Gamma^\zeta_{\alpha\zeta}
=\Gamma^\zeta_{\zeta\alpha}=-1,
\]
matching the JSON output. Direct differentiation gives
\[
\operatorname{Hess}F=Fh,\qquad |\nabla F|_h^2=F^2.
\]

Put
\[
\beta=\log F.
\]
Then
\[
\operatorname{Hess}\beta
=\frac{\operatorname{Hess}F}{F}-\frac{dF\otimes dF}{F^2}
=h-d\beta\otimes d\beta,
\qquad
|\nabla\beta|^2=1.
\]

With the supplied normalization
\[
Q=e^{-3\sigma}F(U),
\qquad e=|dU|^2,
\]
the exact orbit equation from Step 90 is
\[
\tau_\sigma(U)=-\nabla_UQ
=-e^{-3\sigma}\nabla F
=-Q\nabla\beta.
\]
Thus the drift-map chain rule yields
\[
\begin{aligned}
L(\beta\circ U)
&=\operatorname{Hess}\beta:dU\otimes dU
 +d\beta(\tau_\sigma U)\\
&=e-|d(\beta\circ U)|^2-Q.
\end{aligned}
\]
Using \(L\sigma=6+Q\) and
\[
\log Q=-3\sigma+\beta\circ U,
\]
one obtains
\[
\boxed{
L\log Q=-18-4Q+e-|d(\beta\circ U)|^2.}
\]

All coefficients are therefore correct. In particular, the fourth copy of \(Q\) consists of \(3Q\) from \(-3L\sigma\) and \(Q\) from the target-force term.

The remainder has the invariant sum-of-squares form
\[
e_\perp:=e-|d(\beta\circ U)|^2
=\sum_i
\left\langle dU(E_i),J_{\mathbb H^2}\nabla\beta\right\rangle^2
\ge0.
\]
Consequently
\[
L\log Q=-18-4Q+e_\perp.
\]
At a maximum of \(Q\), this only gives
\[
e_\perp\le18+4Q;
\]
it gives no upper estimate for \(Q\).

### Diagonal cross-verification

For \(q=(q_0,0)\) and \(\zeta=0\),
\[
\beta=\log(q_0^2/2)-\alpha.
\]
The orbit equation becomes
\[
L\alpha=Q,
\]
and
\[
\log Q=\text{constant}-3\sigma-\alpha.
\]
Hence
\[
L\log Q=-3(6+Q)-Q=-18-4Q,
\]
which independently verifies both signs and the normalization. In this aligned reduction \(e_\perp=0\).

The SymPy script correctly verifies the target identities and the abstract chain algebra exactly. It inserts, rather than derives, the reduced equations \(L\sigma=6+Q\) and \(\tau_\sigma U=-Q\nabla\beta\); those inserted equations agree with Step 90.

## 3. Exact charge conservation and OT consequences

Let \(K_a\) be the two Killing fields and
\[
\varepsilon_a(Z):=E(Z,K_a),
\qquad E=\operatorname{Ric}+3g.
\]
Since horizontal and orbit directions are orthogonal,
\[
E(Z,K_a)=\operatorname{Ric}(Z,K_a).
\]
Liu’s displayed formula gives
\[
\varepsilon_a(Z)
=-\frac1{2\rho}dq_a(JZ),
\qquad \rho=\sqrt{\det G}=e^\sigma.
\]
Equivalently,
\[
\boxed{dq_a(W)=2\rho\,E(JW,K_a).}
\]
The Hodge-star version carries the corresponding orientation sign.

In invariant norms this is the exact identity
\[
\boxed{
e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle
=4\,G^{ab}
\langle E(\cdot,K_a),E(\cdot,K_b)\rangle
=4|E_{\mathrm{mix}}|_{\mathrm{HS}}^2.}
\]
Thus, with \(b\) defined in Step 90,
\[
|b|=2|E_{\mathrm{mix}}|_{\mathrm{HS}}
\le2\sqrt2\,\delta
\]
when \(\|E\|_{\mathrm{op}}\le\delta\).

For an exact Einstein metric with \(\operatorname{Ric}=-3g\),
\[
E_{\mathrm{mix}}=0,\qquad dq=0.
\]
If an exact OT open collar has \(q=0\), constancy forces \(q=0\) on the connected exact Einstein principal region. Since \(q=\rho Gf\) and \(G\) is invertible there, this also forces the connection curvature \(f\) to vanish.

By contrast,
\[
Q=\frac12e^{-3\sigma}q^TM^{-1}q\longrightarrow0
\]
does not imply \(q\to0\). A fixed nonzero coordinate charge can have vanishing physical energy through growth of the area and orbit factors. Thus asymptotic decay of \(Q\) cannot replace an open OT collar.

The following parts remain mathematically intact:

- the diagonal differential identity itself;
- exact conservation \(dq=0\);
- propagation of \(q=0\) from an OT open collar through a connected exact Einstein region;
- the Koiso-germ OT conclusion once its initial mixed data give \(q=0\);
- the independently derived OT Bochner/resolvent argument for globally OT metrics.

The following statements must be removed:

- exclusion of an interior positive maximum from \(LQ<0\);
- deduction \(Q\equiv0\) from \(Q\to0\) at both ends;
- use of the diagonal formula unchanged for a general orbit map;
- an independent reproof of the OT connector obstruction from the \(Q\)-equation;
- derivation of \(Q=O(\delta^2)\) merely by moving derivatives off the mixed Ricci source.

The number \(\delta_*\approx0.246\) belongs to the separate Steps 85–88 OT argument. Those derivations are not included in the supplied packet, so the present calculation establishes that Step 94 does not alter that argument, but does not independently recompute the numerical value.

## 4. Two-ended vector flux pairing

The strongest derivative-free statement is already the pointwise Liu identity
\[
dq_a(W)=2\rho E(JW,K_a),
\]
together with its invariant norm equality above. It implies, for any path \(\gamma\),
\[
q_a(\gamma(1))-q_a(\gamma(0))
=2\int_\gamma \rho\,E(J\dot\gamma,K_a)\,dt.
\]
If both terminal collars are OT, both endpoint values vanish and hence
\[
\int_\gamma \rho\,E(J\dot\gamma,K_a)\,dt=0.
\]
Similarly all periods vanish. These are exact vector cancellation relations, not amplitude estimates.

For a fixed \(\ell\in\mathbb R^2\), let
\[
q_\ell=\ell^aq_a,\qquad K_\ell=\ell^aK_a.
\]
On a quotient segment \(\Omega\) ending inside the two OT collars,
\[
\boxed{
\int_\Omega\langle dq_\ell,du\rangle\,d\mu
=-\int_\Omega q_\ell\Delta u\,d\mu
=2\int_\Omega\rho\,
 \langle E(J\cdot,K_\ell),du\rangle\,d\mu.}
\]
The terminal-circle terms vanish because \(q_\ell=0\) there. The drift-weighted form is
\[
\int_\Omega\rho\langle dq_\ell,du\rangle\,d\mu
=-\int_\Omega\rho q_\ell Lu\,d\mu.
\]

Equation (4.6) in Step 94 needs a notation clarification. With the session convention \(\Delta=\operatorname{div}\nabla\), the unambiguous volume term is \(-\int q\,\Delta u\). If \(d^\ast\) denotes the standard formal adjoint, then \(d^\ast du=-\Delta u\), and the same term is \(+\int q\,d^\ast du\), not \(-\int q\,d^\ast du\). Also, because \(q\) has two components, the displayed pairing is componentwise or must first be contracted with \(\ell\); otherwise it is vector-valued.

If \(u\) is harmonic with opposite end values, the pairing is simply zero. A massive test gives one weighted moment of \(q\). Neither controls its maximum. The elementary interval model illustrates the missing coercivity:
\[
q(0)=q(L)=0,\qquad |q'|\le\delta
\]
still permits a triangular profile with
\[
\max|q|=\frac{\delta L}{2}.
\]
It can also be placed between a separator where \(q=0\) and one OT collar. This model is not a reduced Einstein metric; it demonstrates that endpoint cancellation, one separator trace, and a first-order source estimate alone cannot produce a length-independent amplitude estimate.

The separator Jacobi form controls charge mass on the separator, and its coupling to tangential Maxwell transport gives the finite Step 92 estimate
\[
\sup_CQ\le C_Q(\delta).
\]
It does not control normal transport through the connector. That transport contains
\[
|h_\nu|+\sqrt{e_\nu},
\]
and Step 92’s exact Koiso germs show that \(e_\nu\) can be arbitrarily large at the separator while stability and the local Einstein constraints remain satisfied.

A coercive estimate would therefore need a geometry-dependent inequality of the schematic form
\[
\int_\Omega q^TAq\,d\mu_\sigma
\le C\int_\Omega(dq)^TA(dq)\,d\mu_\sigma
+\text{separator trace contribution},
\qquad
A=e^{-3\sigma}M^{-1},
\]
with \(C\) independent of connector length and area growth, followed by a Green or transport estimate converting this to pointwise control. Ordinary two-end capacity degenerates on long cylinders; for instance, the Dirichlet energy of the linear function taking values \(-1\) and \(1\) on an interval of length \(L\) is \(4/L\).

Thus the supplied separator stability, exact OT collars, and Liu source law presently give conservation, cancellation, and a finite separator value, but no uniform interior amplitude estimate. A matrix-weighted capacity or spectral estimate tied to
\[
L\sigma=6+Q-T
\]
and the horizontal/orbit equations is the missing mathematical substance.