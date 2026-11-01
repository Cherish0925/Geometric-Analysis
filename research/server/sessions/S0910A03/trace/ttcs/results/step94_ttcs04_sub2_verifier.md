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

## Verifier memo — invariant horizontal Noether/Bianchi identity for the free-T² reduction

### Result of the check

The relation
$$2\,\mathrm{div}_\sigma H-d\,\mathrm{tr}H=-dT-T\,d\sigma-\langle Z,dU\rangle-m_q$$
is correct in signs and coefficients. I reconstructed it independently from the contracted Bianchi identity, the Bochner commutation, the harmonic-map stress divergence, the area and orbit equations, and the chain rule for $Q$, and every substitution the script uses is a genuine tensor identity, not a bookkeeping convenience. The residual is zero for a real reason, and the two internal cancellations that actually test the coefficients (see below) both fire correctly.

### Independent derivation and where the coefficients are genuinely tested

With $H=\mathrm{Ric}_B-\mathrm{Hess}\,\sigma-\tfrac12 d\sigma^2-\tfrac12 A-Q\gamma+3\gamma$, $A=U^*h$, $e=|dU|^2$, the pieces are all standard and I confirm each:

- $\mathrm{div}\,\mathrm{Ric}_B=\tfrac12 dR_B$ (base contracted Bianchi, 2D).
- $\mathrm{div}\,\mathrm{Hess}\,\sigma=d\Delta\sigma+\mathrm{Ric}_B(\nabla\sigma,\cdot)$ (commutation).
- $\mathrm{div}(d\sigma\otimes d\sigma)=\Delta\sigma\,d\sigma+\mathrm{Hess}\,\sigma(\nabla\sigma,\cdot)$.
- $\mathrm{div}(U^*h)_j=\langle\tau(U),dU\rangle_j+\tfrac12\partial_j e$. I recomputed this from $A_{ij}=h_{ab}\partial_iU^a\partial_jU^b$: the tension term comes from $\gamma^{ik}\nabla_k\partial_iU$, the $\tfrac12\partial_j e$ from the symmetric second slot. The sign convention $\tau=\gamma^{ik}\nabla_k\partial_iU$ is the one used consistently.
- $d|\nabla\sigma|^2=2\,\mathrm{Hess}\,\sigma(\nabla\sigma,\cdot)$; $\mathrm{div}(Q\gamma)=dQ$; $\mathrm{div}(3\gamma)=0$.

Two cancellations are the real coefficient tests:

1. The $\tfrac14\,de$ produced by $-\mathrm{div}(\tfrac12 A)$ cancels exactly against the $\tfrac14\,de$ inside $\tfrac12 dR_B$ (which carries the $-\tfrac12 e$ from $\mathrm{tr}H$). This confirms the coefficient $\tfrac12$ in front of $U^*h$ in $H$ is the value forced by the harmonic-map stress tensor — a wrong coefficient there would leave an uncancelled $de$.
2. $\tfrac14\,d|\nabla\sigma|^2=\tfrac12\,\mathrm{Hess}\,\sigma(\nabla\sigma,\cdot)$ cancels the $-\tfrac12\,\mathrm{Hess}_s$ term. This confirms the $\tfrac12 d\sigma^2$ coefficient.

The nontrivial structural point: the intrinsic base tension $\tau(U)$ is upgraded to the drift tension $\tau_\sigma(U)=\tau(U)+dU(\nabla\sigma)$ automatically, because the $\mathrm{Ric}_B(\nabla\sigma,\cdot)$ term from the Hessian commutation is replaced through the horizontal reduction equation, and its $\tfrac12 A(\nabla\sigma,\cdot)$ part combines with $\tfrac12\langle\tau,dU\rangle$ into $\tfrac12\langle\tau_\sigma,dU\rangle$. This is correct and is what makes the orbit equation $\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z$ enter with the right weight.

Finally $dQ=-3Q\,d\sigma+d_UQ+D_qQ[dq]$ with $D_qQ[dq]=e^{-3\sigma}\langle M^{-1}q,dq\rangle$ (from $Q=\tfrac12 e^{-3\sigma}q^TM^{-1}q$) removes the $d_UQ$ and the $\tfrac32 Q\,d\sigma$ bookkeeping terms, leaving precisely $\tfrac12 d\,\mathrm{tr}H-\tfrac12 dT-\tfrac12 T\,d\sigma-\tfrac12\langle Z,dU\rangle-\tfrac12 m_q$. Doubling reproduces the stated identity with the stated signs.

One point about the script itself: it is componentwise, treating several contractions as independent symbols, and the terms proportional to $d\sigma$ are carried as implicit unit coefficients until the hand-built `pre`. I checked that `pre` faithfully re-attributes those coefficients to $\sigma_j$, so the final zero residual is a real comparison, not a construction artifact. A fully tensorial recomputation on explicit data would strengthen this (see final section).

### Radial specialization

For $\gamma=dr^2+\psi^2d\theta^2$, $H=C\,dr^2$, $T=Z=0$, diagonal charge:

- $\mathrm{div}(C\,dr^2)_r$: with $\Gamma^r_{\theta\theta}=-\psi\psi'$, $\Gamma^\theta_{r\theta}=\psi'/\psi=h$, I get $\nabla_rH_{rr}=C'$ and $\gamma^{\theta\theta}\nabla_\theta H_{\theta r}=hC$, so $(\mathrm{div}H)_r=C'+hC$.
- Weighting adds $H(\nabla\sigma,\cdot)_r=uC$ with $u=\sigma'$, giving $\mathrm{div}_\sigma H_r=C'+(u+h)C$.
- $\mathrm{tr}H=C$, so $(d\,\mathrm{tr}H)_r=C'$.

Then $2(C'+(u+h)C)-C'=-m_q|_r$ gives $C'=-2(u+h)C-m_q|_r$. The physical normalization is consistent: for $M=\mathrm{diag}(e^\alpha,e^{-\alpha})$, $q=(q(r),0)$,
$$m_q|_r=e^{-3\sigma}\langle M^{-1}q,q'\rangle=e^{-3\sigma-\alpha}qq',$$
while $w=\sqrt{2Q}=e^{-3\sigma/2-\alpha/2}q$ and $b=e^{-(3\sigma+\alpha)/2}q'$, so $wb=e^{-3\sigma-\alpha}qq'=m_q|_r$. Hence $C'=-2(u+h)C-wb$, matching Step 90 (6.4a)/(7.3a) with $H=\psi'/\psi=h$.

This match is a meaningful cross-check, not a tautology: Step 90 obtained $C'=-2(u+H)C-wb$ by directly differentiating the unused $rr$-component residual, an independent route. Two derivations agreeing on both the drift coefficient $-2(u+h)$ and the product source $-wb$ is strong evidence the identity's packaging of the four defect blocks is complete in the radial case.

### Nature of the relation: propagation/compatibility, not independent field data

This is a component of the single 4D contracted Bianchi identity $2\,\mathrm{div}_gE=d\,\mathrm{tr}_gE$ (with $E=\mathrm{Ric}_g+3g$), reorganized into base variables. It is satisfied automatically by any configuration for which the area equation, orbit equation, and the definitions of $H,T,Z$ hold; it adds no new equation. In the radial case it is a first-order linear transport for $C=E_{rr}$ sourced by the other blocks, i.e. constraint propagation: $C(0)=0$ together with vanishing source forces $C\equiv0$, and in general
$$C(L)=-e^{-2I(L)}\int_0^L e^{2I(s)}wb\,ds,\qquad I'=u+h.$$
So the terminal $C(L)$ is not a free endpoint value; it is fixed by integrating the mixed source against the weight. The interpretation stored in the JSON — that $H$ is coupled to area, orbit, and charge residuals and is not a freely tunable endpoint condition — is accurate, and this identity is the abstract reason a monotone one-sign discharge leaves $C(L)\neq0$ (Step 90 §7).

### The same-defect structure and what it prevents

$H=E_B$, $T=\mathrm{tr}_{\rm orb}E$, $Z=-2\widehat E_0$, and $m_q$ (through $dq=2\rho *E_{\rm mix}$) are all blocks of one tensor $E$. Under the pinching input $\|E\|_{\rm op}\le\delta$ every term is $O(\delta)$ simultaneously. The identity therefore reads (weighted derivative of an $O(\delta)$ block) $=$ (other $O(\delta)$ blocks): there is no term of a different order to play against, so the relation cannot by itself bootstrap smallness of the interior charge $Q_+$. The radial case sharpens this usefully: the source is the product $wb$, so if $w,b=O(\delta)$ then $C=O(\delta^2)$ — the horizontal block is second order in the mixed defect. That is a real and reusable observation, but it is a compatibility consequence, not an independent condition on $Q$. This is exactly why treating $H,T,Z,m_q$ as four independent levers would be mistaken.

Note also a genuine notation hazard between the session notes: Step 90 (1.1) uses $L\sigma=6+Q-T$ with $T=\mathrm{tr}_{\rm orb}E$, while the Step 94 script uses $T=L\sigma-6-Q$. These $T$ differ by sign. The identity's $-dT-T\,d\sigma$ is correct for the Step 94 sign; importing it into the Step 90 convention requires flipping those two terms. The radial check is insensitive to this because $T=0$ there.

### Most useful global pairing when $q,H$ vanish on exact end collars and $T,Z,E$ are only $C^0$-small

Pair the one-form identity with a base vector field and integrate against the drift measure $d\mu_\sigma=e^\sigma dA_\gamma$, for which $\mathrm{div}_\sigma$ is self-adjoint. Because $H$ (hence $\mathrm{tr}H$) and $q$ vanish on the exact end collars, integration by parts kills the collar terms from the $H$ blocks and from the charge, and the mixed-source term becomes a two-ended pairing.

- Contracting with a drift-harmonic two-ended potential $u$ ($Lu=0$, $u\to\pm1$ on the two collars) turns the identity into
$$\int_B\langle m_q,\nabla u\rangle\,d\mu_\sigma=\int_B\big[-2\langle\mathrm{div}_\sigma H,\nabla u\rangle+\langle d\,\mathrm{tr}H,\nabla u\rangle+\langle dT,\nabla u\rangle+T\langle d\sigma,\nabla u\rangle+\langle Z,dU(\nabla u)\rangle\big]d\mu_\sigma.$$
  After moving derivatives off the vanishing $H,\mathrm{tr}H,q$, the right side is controlled entirely by the $C^0$-small blocks $T,Z,\|H\|=O(\delta)$ times weighted derivatives of $u$. This is precisely the vector flux/capacity object Step 94 §4 (4.7)–(4.9) is chasing; the Noether identity is what supplies the divergence structure converting the local mixed source $m_q$ into that global weighted pairing.

- The alternative contraction with $X=\nabla\sigma$ gives a weighted virial/Pohozaev relation between $\int\langle H,\mathrm{Hess}\,\sigma\rangle$, $\int\mathrm{tr}H\,L\sigma$ (with $L\sigma=6+Q+T$ feeding the area equation), and $\int$(source$\cdot\nabla\sigma$). This one directly injects the $6+Q$ area growth and is the more promising candidate for extracting an order-one interior cost.

The honest reading, consistent with the note's own benchmarks: this pairing yields the correct adjoint object but is coercivity-neutral. Its usefulness for a two-ended obstruction hinges on a weighted geometry-coupled Poincaré/Hardy bound (Step 94 (4.9)) whose constant is uniform in connector length and area growth. Step 94 §6's exact redshift-taper, where $\rho\sim e^{\sqrt6 r}$ makes the physical source $\sim e^{-3\sqrt6 R/2}$ while the weighted ratio grows $\sim e^{2\sqrt6 R}$, and Step 90 §7's discharge cores, both show that weight growth defeats the naive capacity: $C^0$-small sources can still support order-one interior charge. So the identity organizes the two-ended problem into the right pairing but does not close it; the missing ingredient is the uniform weighted capacity, not a better use of Bianchi.

### What would strengthen the confirmation

1. A fully tensorial recomputation on explicit smooth data — pick $\gamma$, $\sigma$, an Iwasawa orbit map $U=(\alpha,\beta)$, and $q(r,z)$; assemble all four blocks of the 4D Ricci defect and verify the one-form identity at several points and in several directions $j$ (not only the radial $r$-direction). The present componentwise verification cannot see a dropped mixed-block divergence term; the radial agreement with Step 90's independent $rr$-differentiation is reassuring but is a single direction with the $\theta\theta$ block imposed exactly. A generic-direction check would confirm that the mixed block is fully captured by $m_q$ in the non-radial setting.
2. State the normalization range explicitly: the constants $6$ and $3$ fix this to the 4D T²-over-2D reduction with $\Lambda=-3$. The identity is a tool inside the negatively-curved T²-symmetric connector sub-problem and does not itself bear on the general $n\ge2$ statement.