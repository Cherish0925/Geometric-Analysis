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

# Verification Memo: Step 94 charge-sign correction and the invariant fixed-charge identity

## 1. The diagonal identity does not exclude an interior maximum — confirmed, with a sharper structural reading

The two forms are algebraically equivalent under $L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle$. Using $L\log Q=\tfrac{LQ}{Q}-\tfrac{|\nabla Q|^2}{Q^2}$,
$$
L\log Q=\frac1Q\Big(\tfrac{|\nabla Q|^2}{Q}-18Q-4Q^2\Big)-\frac{|\nabla Q|^2}{Q^2}=-18-4Q,
$$
so (1.1) $\Leftrightarrow$ (1.2) exactly. At an interior maximum of a positive $Q$ one has $\nabla Q=0$ and $\Delta Q\le0$, hence $LQ=\Delta Q\le0$; the identity gives $LQ=-18Q-4Q^2<0$, which *satisfies* $LQ\le0$. There is no sign contradiction. Equivalently $L\log Q<0$ is superharmonicity, which places the *minimum*, not the maximum, at the ends. The withdrawal of the former maximum-exclusion corollary is mathematically forced and correct.

One point strengthens the note's own framing and unifies it with §4. On a *closed* weighted manifold, $\int Lu\,e^\sigma\,dvol=0$ for every smooth $u$, so $L\log Q=-18-4Q<0$ everywhere is impossible on a closed base — the inference "looked" valid because it is valid there. The connector base is an open cylinder, and integrating the exact diagonal identity over a region $B$ gives the genuine replacement:
$$
\int_B(18+4Q-e_\perp)\,e^\sigma\,dvol=-\int_{\text{ends}} e^\sigma\,\partial_n\log Q .
$$
The negative left side must be balanced by end flux of $\log Q$; this is precisely the redshift of $Q$ toward the cusps. The maximum principle is not merely unavailable — it is structurally replaced by a global end-flux balance, which is the same object §4 seeks. This also explains why the note is right to work with the vector charge $q$ (regular, $dq$ exact) rather than $\log Q$: $\log Q\to-\infty$ at OT zeros and at the ends, so the scalar flux integral is singular exactly where control is needed.

## 2. The scalar even countermodel is valid

For $y''=-18-4e^y$, multiplying by $y'$ and integrating with $y(0)=\log Q_0,\ y'(0)=0$ gives
$$
(y')^2=36(\log Q_0-y)+8(Q_0-e^y),
$$
matching (1.3). Since $y''\le-18$ everywhere, $y$ is strictly concave with $y(x)\le\log Q_0-9x^2$, so $Q=e^y$ has a strict interior maximum and decays faster than Gaussian at both ends. The recorded $\log Q(\pm8)\approx-580\approx-9\cdot64$ and terminal slope $\approx-144\approx-18\cdot8$ are exactly the analytic prediction, and the first-integral residual $\sim10^{-9}$ is consistent. This is a legitimate scalar witness that $L\log Q<0$ coexists with an interior positive maximum and with $Q\to0$ at both ends without $Q\equiv0$. It is not a solution of the coupled reduction, as stated. Item 2 of the withdrawal is correctly supported.

## 3. The invariant fixed-charge identity is correct in every sign and normalization

**Busemann structure of $F$.** In the Iwasawa chart, $\det M=1$, $M^{-1}$ and $F=\tfrac12 e^{-\alpha}(q_1-\zeta q_2)^2+\tfrac12 q_2^2e^{\alpha}$ reproduce the script output; the Christoffel symbols $\Gamma^\alpha_{\zeta\zeta}=e^{-2\alpha}$, $\Gamma^\zeta_{\alpha\zeta}=-1$ are correct for $h=d\alpha^2+e^{-2\alpha}d\zeta^2$ ($K=-1$). The symbolic residuals for $\operatorname{Hess}F=Fh$ and $|\nabla F|^2=F^2$ are zero, and from these
$$
\operatorname{Hess}\beta=\frac{\operatorname{Hess}F}{F}-\frac{dF\otimes dF}{F^2}=h-d\beta\otimes d\beta,\qquad |\nabla\beta|^2=\frac{|\nabla F|^2}{F^2}=1 .
$$
This is exactly the horocyclic/Busemann identity on curvature $-1$: level sets of $\beta$ are horocycles of geodesic curvature $1$, so $\log F$ is a Busemann function. The geometry is not incidental; it is what makes $-Q\nabla\beta$ act as a unit-gradient source.

**Orbit equation.** With $Q=e^{-3\sigma}F(U)$ and $\sigma$ frozen at the target level, $\nabla_{\mathbb H^2}Q=e^{-3\sigma}\nabla_{\mathbb H^2}F=e^{-3\sigma}F\nabla\beta=Q\nabla\beta$, so $\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q=-Q\nabla\beta$ (2.4) is consistent with Step 90 (1.2)/(2.2). The diagonal check ($M=I$, $q=(q_0,0)$): $\beta=\text{const}-\alpha$, $\nabla\beta=-\partial_\alpha$, $\tau_\sigma=Q\partial_\alpha$, matching $L\alpha=Q$.

**Chain rule and assembly.** For the weighted map Laplacian,
$$
L(\beta\circ U)=\operatorname{Hess}\beta(dU,dU)+d\beta(\tau_\sigma U)=\big(e-|d(\beta\circ U)|^2\big)-Q,
$$
using $\operatorname{Hess}\beta(dU,dU)=|dU|^2-\sum_i d\beta(dU e_i)^2=e-|d(\beta\circ U)|^2$ and $d\beta(-Q\nabla\beta)=-Q|\nabla\beta|^2=-Q$. Then $\log Q=-3\sigma+\beta\circ U$ with $L\sigma=6+Q$ gives
$$
L\log Q=-3(6+Q)+e-|d(\beta\circ U)|^2-Q=-18-4Q+e-|d(\beta\circ U)|^2 .
$$
This matches (2.7), and the script residual is zero. The transverse energy $e_\perp=e-|d(\beta\circ U)|^2=\sum_i t_i^2\ge0$ because $|d\beta|=1$ forces $|d(\beta\circ U)|^2\le e$. The $e_\perp=0$ specialization recovers (1.1). The constant $-18$ is $-3\cdot6$ from the area equation; the $-4Q$ is $-3Q$ (area) $-Q$ (orbit tension); these are correctly attributed. The general $LQ$ carries an extra $+Q\,e_\perp$ over the diagonal (1.1), consistent with $LQ=QL\log Q+|\nabla Q|^2/Q$.

At a critical point of $Q$, $L\log Q=-18-4Q+e_\perp$, and since the Step 92 concentrated Koiso germs make $\sup e_\perp$ (transverse orbit energy) unbounded even under full stability and exact Einstein equations, the sign is genuinely undetermined — the maximum-exclusion argument does not merely fail marginally, it has no controllable reaction term. This is correctly stated.

**Independent cross-check of the transport inequality.** The identity is internally consistent with Step 90/92's Maxwell transport: $\log w=\text{const}-\tfrac32\sigma+\tfrac12\beta\circ U$ gives $|dw+\tfrac32w\,d\sigma|=\tfrac12 w\,|d(\beta\circ U)|\le\tfrac12 w|dU|$ for fixed charge, exactly the coefficient in (5.1)/(4.1), with the variable-charge $|b|$ added. The $\tfrac12$ and the unit-gradient property come from the same Busemann fact.

## 4. What remains, and what is set aside

Set aside (correctly): interior-maximum exclusion from (6.1)–(6.2); "$Q\to0$ both ends $\Rightarrow Q\equiv0$"; the diagonal identity reproving the OT obstruction; any weak-formulation route to $Q=O(\delta^2)$; and the Step 93 backward-transport thresholds $\delta^{**}=0.186,0.210$ (the $e^{3R}$ growth is the decisive correction, and the forward Gronwall kernel was misread as a reverse bound).

Retained (correctly): the exact mixed-Ricci conservation $dq_a=0$ is Liu's principal-stratum result $\nabla_\Sigma\alpha=\nabla_\Sigma\beta=0$ and is solid. Its consequence — exact OT on one open end plus exact Einstein on a connected region forces $q\equiv0$ there, hence OT, hence the Steps 85–88 Bochner/resolvent obstruction applies — is valid *only where the entire connected region is exactly Einstein*. On the $\delta$-forced interior $dq=O(\delta)\ne0$, so this does not reach the connector; the note keeps this distinction cleanly. The physical/coordinate distinction is correct: $Q=e^{-3\sigma}F$ can redshift to zero with the conserved $q\ne0$ (the Step 90 radial cores realize this to $Q_0=100$). The Koiso germ OT statement and forward cusp damping $w(n)\le e^{-3n}w(0)+O(\delta)$ are valid.

## 5. Two-ended vector-charge flux: strongest derivative-free content and the missing coercive object

**Strongest derivative-free identity.** From Liu's law $\operatorname{Ric}(Z,V_a)=-\tfrac1{2\rho}\langle d\alpha_a,JZ\rangle$ and the vanishing of the mixed background term ($g(Z,V_a)=0$), for $E=\operatorname{Ric}+3g$ one has the *exact one-form identity*
$$
dq_a=-2\rho\,*_\gamma E(\cdot,V_a),\qquad |dq_a|=2\rho\,|E_{\mathrm{mix},a}|\le 2\rho\,\delta .
$$
Because $q_a$ is a globally defined scalar potential, this yields the two exactness relations
$$
q_a(\gamma_+)-q_a(\gamma_-)=\int_\gamma dq_a,\qquad \oint dq_a=0 ,
$$
and pointwise $|q_a(s)|\le 2\delta\int_{\gamma}\rho$. These three are the sharpest derivative-free statements; there is no derivative-free pointwise amplitude control beyond them, because the frame weight $\rho$ is not itself bounded by the $C^0$ Ricci defect.

**Does stability plus two exact OT ends give amplitude coercivity? No, not presently.** Exact OT at both ends gives $q(\gamma_\pm)=0$, so $\int_\gamma dq=0$: a cancellation, not an amplitude bound. Along a path the potential can reach $|q|\lesssim2\delta\int\rho\,ds$, and where $\rho$ is large over a long connector this accumulates order-one charge from $C^0$-small $E$ — exactly the $w(0)\asymp\beta_0 e^{3R}$ growth of the Step 93 scalar witness and the Step 90 redshift cores. Separator stability (3.3) delivers $\sup_C Q\le C_Q(\delta)$, but the constant is enormous ($\sim6\times10^{10}$ even at $\delta=0$), it is not small, and it lives on the single separator curve. The Step 92 tangential-Maxwell coupling ($c^2\le20\mathcal W$) is what converts the tangential capacity into that finite slice height; but there is no first-order transport for the normal orbit energy $e_\nu$, and the concentrated Koiso germs show $\sup e_\nu$ unbounded under full stability and exact Einstein. Hence separator data does not propagate normally into the interior, and neither the exactness relations nor separator stability control $Q_+=\sup_B Q$ or the interior amplitude of $q$.

**The flux pairing (4.6) and the indispensable extra estimate.** For $u$ solving a massive/Dirichlet problem with opposite constants on the two exact collars,
$$
\int_B\langle dq,du\rangle=-\int_B q\,d^*du+\text{end terms},
$$
end terms vanishing when $q=0$ on the exact collars, and the left side is bounded by $2\delta\int_B\rho|du|$ from the identity. Coercivity — turning this into $\|q\|\le C(\delta)$ with $C\to0$ — requires a lower spectral/capacity constant for the weighted quotient operator $d^*d+\text{mass}$ that does not degenerate under arbitrary connector length or orbit-volume growth. The Step 93 scalar example shows unweighted two-end capacity is insufficient. The one structural handle not yet used is that $\rho=e^\sigma$ cannot grow freely: $L\sigma=6+Q$ ties $\rho$-growth to an area/$Q$-budget. A *weighted, area-coupled* capacity estimate whose constant is governed by the area equation and the separator Jacobi form is therefore indispensable; nothing supplied so far provides amplitude coercivity without it. The note's identification of this object is accurate, and the choice of the vector charge $q$ over $\log Q$ is well-motivated by the singularity of $\log Q$ at OT zeros.

## 6. Net assessment

Every sign and normalization in the Step 94 correction and in the invariant identity $L\log Q=-18-4Q+e-|d(\beta\circ U)|^2$ is correct; the Busemann property of $\log F$, the orbit equation $\tau_\sigma=-Q\nabla\beta$, and the transport coefficient $\tfrac12$ all cohere. The withdrawals are forced. What is provable now is: exact-region charge conservation with the twist-free obstruction, forward cusp damping, finite (non-small) separator slice height, and the exactness/zero-net-flux relations for $q$. What is absent is any coercive amplitude bound; the added weighted end-flux identity in §1 above and the area–capacity coupling in §5 pinpoint that the same missing object — a weighted, geometry-coupled source-to-charge estimate — governs both the failed scalar maximum principle and the two-ended vector flux. No statement here reaches the forced two-ended connector, non-symmetric graph metrics, the $\Lambda>0$ branch, higher dimensions, or Yau 26, and the notes represent this accurately.