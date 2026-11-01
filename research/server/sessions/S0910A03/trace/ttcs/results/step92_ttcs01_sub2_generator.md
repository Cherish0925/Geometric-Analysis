# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step91_separator_stability_and_barriers.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/data/step92_jacobi_concentration_models.json",
    "Sessions/S0910A03/workspace/data/step92_weighted_jacobi_transform.json"
  ]
}
```

## Task

The active Yau-26 subproblem is a free T^2-invariant two-ended approximately negative-Einstein connector. At its invariant minimizing separator C, let rho=e^sigma, s be base arclength, V=|II|^2=kappa^2+h_nu^2/2+e_nu/2+Q, h=sigma_s, and e_s=|U_s|^2. The verified formulas are: (i) for every smooth periodic phi, ∫rho V phi^2 <= ∫rho[(phi_s)^2+(3-E_nunu)phi^2]; (ii) R_q=-2h_s-(3/2)h^2-e_s/2; (iii) minimal Gauss R_q=-6+D-V, |D|<=4delta; (iv) Maxwell dq=±2rho * E_mix, with normalized |b|<=2sqrt(2)delta, and Q=(1/2)e^{-3sigma}q^T M^{-1}q; (v) orbit equation tau_sigma(U)=-grad Q+Z, |Z|<=2delta. Develop the strongest mathematically valid interaction among the full Jacobi form, scalar identity, Maxwell transport, and orbit equation. Look especially for a new nonlocal inequality that controls concentration of Q or e_nu on C, or else give an explicit formal/local-data mechanism showing why these equations still permit concentration. Keep all hypotheses and identify exact missing bridge; do not infer a pointwise bound from stability.

## Output

## The load‑bearing new object: fuse the two scalar‑curvature expressions into a pointwise identity

The verified data contain two independent formulas for the same intrinsic scalar curvature of the 3‑manifold $\Sigma=\pi^{-1}(C)$ with metric $q=ds^2+G(s)$: the one‑dimensional reduction (ii) and the minimal Gauss equation (iii). Equating them is not an averaged statement — it holds at every point of $C$:

$$
-2h_s-\tfrac32h^2-\tfrac12e_s=-6+D-V
\;\Longrightarrow\;
\boxed{\,V=-6+D+2h_s+\tfrac32h^2+\tfrac12e_s\,}\tag{$\star$}
$$

with $|D|\le4\delta$. Since $V=\kappa^2+\tfrac12h_\nu^2+\tfrac12e_\nu+Q\ge Q$, this gives a **pointwise** relation

$$
Q\;\le\;2h_s+\tfrac32h^2+\tfrac12e_s-6+4\delta .\tag{$\star\star$}
$$

This is the coupling the other equations need. Averaging $(\star)$ against $\rho\,ds$ reproduces the Step‑88 identity (2.5) and gives nothing new; the pointwise content is what lets Maxwell transport bite. Its immediate message: **a spike of $Q$ cannot exist alone — it forces a simultaneous spike in the tangential data $\{h_s,\,h^2,\,e_s\}$.** Either $h_s$ carries it (then $h$ jumps by $\sim\!\tfrac12\!\int V$), or $e_s$ carries it (then $e_s\approx 2Q$ on the spike). The transport equation then discriminates between these two options and forbids both.

## A genuinely new integral inequality from the full Jacobi form

Substitute $(\star)$ into the stability form (i). The potential $3-E_{\nu\nu}-V$ becomes $9-E_{\nu\nu}-D-2h_s-\tfrac32h^2-\tfrac12e_s$. Integrate the $-2h_s$ term by parts against the weight $\rho$ (using $\rho_s=\rho h$) and complete the square in the drift:

$$
\int_C\rho\Big[(\phi_s+2h\phi)^2+\big(9-E_{\nu\nu}-D-\tfrac72h^2-\tfrac12e_s\big)\phi^2\Big]\,ds\ \ge\ 0
\quad\forall\phi.\tag{$\diamondsuit$}
$$

The $V$‑spike has been absorbed: the potential in $(\diamondsuit)$ is now bounded **above** by $9+5\delta$. The distinguished periodic test function that annihilates the drift is
$$
\phi_0=\rho^{-2},\qquad \phi_{0,s}+2h\phi_0=-2\rho^{-2}h+2h\rho^{-2}=0 .
$$
It is single‑valued on $C$ because $\rho$ is. Feeding $\phi_0$ into $(\diamondsuit)$ kills the kinetic term and leaves

$$
\boxed{\ \int_C\rho^{-3}\Big(\tfrac72h^2+\tfrac12e_s\Big)\,ds\ \le\ \int_C\rho^{-3}\,(9-E_{\nu\nu}-D)\,ds\ \le\ (9+5\delta)\!\int_C\rho^{-3}\,ds.\ }\tag{$\triangle$}
$$

This is new and rigorous, using only (i)–(iii). It is the **first control of a $\int h^2$ quantity** at the separator: earlier notes (2.5, Step 91) treated $\langle h^2\rangle$ as uncontrolled, but $(\triangle)$ bounds the $\rho^{-3}$‑weighted $\int h^2$ and $\int e_s$ **together**. At the Koiso totally geodesic center ($h=0,\,e_s=12,\,D=E=0$) it reads $6\le9$, so it carries genuine slack rather than being an identity.

## The Maxwell transport promotes the mass bound into a sup bound

Restrict the invariant transport inequality (iv)/(Step 90 §5) $|dw+\tfrac32w\,d\sigma|\le\tfrac12w|dU|+|b|$ to the unit tangent $T$ of $C$, with $w=\sqrt{2Q}$ and $|b|\le2\sqrt2\,\delta=:\beta$:

$$
\big|w_s+\tfrac32hw\big|\le \tfrac12\sqrt{e_s}\,w+\beta .
$$

Set $S:=\rho^{3/2}\sqrt{Q}=\tfrac1{\sqrt2}\rho^{3/2}w$, which removes the $\tfrac32hw$ drift:
$$
\boxed{\ |S_s|\ \le\ \tfrac12\sqrt{e_s}\,S+\tfrac{\beta}{\sqrt2}\,\rho^{3/2}.\ }\tag{$\heartsuit$}
$$

Two facts close the loop against stability:

**Mass bound.** Stability with $\phi=1$ gives $\int_C\rho V\le(3+\delta)\int_C\rho$, and $V\ge Q$, so $\langle Q\rangle_C\le 3+\delta$. Hence the ($\rho$‑weighted) mass of any $Q$‑spike is $O(1)$.

**Rate–width incompatibility.** Consider a putative concentration $Q\sim A$ of width $\ell_0$. Two exclusive routes are allowed by $(\star)$:

- *$e_s$ carries the spike* ($e_s\approx 2A$). Then the transport rate in $(\heartsuit)$ is $\tfrac12\sqrt{e_s}\approx\sqrt{A/2}$. Raising $S$ from a bounded background to its spike value accumulates an exponent $\tfrac12\!\int\!\sqrt{e_s}\sim\sqrt{A/2}\,\ell_0$; to actually rise one needs $\sqrt{A/2}\,\ell_0\gtrsim\log(\sqrt A/\text{background})$, i.e. $\ell_0\gtrsim A^{-1/2}\log(1/\delta)$. Feeding this into the mass bound $A\ell_0\lesssim 3\ell$ gives $\sqrt A\,\log(1/\delta)\lesssim 3\ell$, hence
$$
\boxed{\ Q_{\max}\ \lesssim\ \frac{9\,\ell^2}{\big(\log(1/\delta)\big)^2}\ }\qquad(\text{small charge background}),
$$
which $\to0$ as $\delta\to0$.

- *$h_s$ carries the spike* ($e_s$ small). Then the transport rate $\tfrac12\sqrt{e_s}$ is small, so over a short width $\ell_0$ the multiplier $\exp(\tfrac12\!\int\sqrt{e_s})\approx1$ and the source $\tfrac{\beta}{\sqrt2}\rho^{3/2}$ can raise $S$ only by $O(\delta\ell_0)$. This route cannot build a tall $Q$ at all.

So **whichever way $(\star)$ balances the spike, transport blocks it.** Equivalently, the clean min‑to‑max form: let $S$ attain its extrema at $s_*,s_0$ with $Q(s_0)\le\langle Q\rangle\le3+\delta$; integrating $(\heartsuit)$ along the shorter arc,
$$
Q_{\max}\ \le\ \Lambda^{3}\,(3+\delta)\,\exp\!\Big(\sqrt{\tfrac{\ell}{2}\textstyle\int_C e_s}\Big)\ +\ (\delta\text{-source}),\qquad \Lambda:=\frac{\rho_{\max}}{\rho_{\min}}\Big|_C.\tag{$\clubsuit$}
$$

This is the sought nonlocal inequality: it converts the stability *mass* bound on $Q$ into a *pointwise* bound by charging the growth against the finite exponential budget of $(\heartsuit)$, whose total $\int e_s$ is itself finite by $(\triangle)$. Concentration of $Q$ is prevented, not by stability alone, but by the transport–mass interaction.

**Then $e_\nu$ follows.** Once $Q$ is bounded, the orbit equation (v) $\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z$ has forcing of magnitude $|\nabla_{\mathbb H^2}Q|=Q$ (Step 90 §2) plus $|Z|\le2\delta$, both now bounded, and target $\mathbb H^2$ of curvature sign $-$. The weighted tension field of $U$ is therefore bounded, and an elliptic/tension estimate for the harmonic‑map‑with‑potential system controls $e=|dU|^2$ and hence its normal part $e_\nu$. There is no first‑order transport for $e_\nu$ as there is for the charge; its sup control routes through the second‑order orbit equation with $Q$ as bounded data.

## Why this is not yet a theorem — the exact missing bridges

The mechanism $(\clubsuit)$ is airtight *given three inputs that (i)–(v) do not by themselves supply on $C$*:

1. **Cross‑weight bridge / $\rho$‑oscillation $\Lambda$.** Stability and $\phi_0$ give bounds in *two different weights*: $\langle\cdot\rangle_\rho$ (mass) and the $\rho^{-3}$‑weighted $(\triangle)$ (for $e_s,h^2$). Passing between them, i.e. bounding $\int_C e_s$ *unweighted* or the product $\int\rho^3\!\int\rho^{-3}$, needs control of $\Lambda=\rho_{\max}/\rho_{\min}$ on $C$. Internally this closes only for short separators: writing $m=\oint h^2$, $(\triangle)$ gives $m\le\tfrac27(9+5\delta)\Lambda^3\ell$ and $\log\Lambda\le\tfrac12\sqrt{\ell m}$, a self‑consistent pair forcing $\Lambda\to1$ when $\ell<\ell_*(\delta)$ but permitting large $\Lambda$ for long $C$. The natural way to remove the length restriction is the **global elliptic equation** $L\sigma=6+Q-T$, $|T|\le2\delta$ (Step 90 eq 1.1): with $Q$ mass‑bounded and $|T|$ small, a Harnack/oscillation estimate for $\sigma$ restricted to $C$ would bound $\Lambda$ independently of $\ell$. This is the single most valuable next computation.

2. **Rigorous circle Grönwall with vanishing charge.** $(\heartsuit)$ is a differential inequality; the min‑to‑max integration and the case $Q\to0$ (where $\log S$ is singular but $S$ is not) must be handled by integrating $S$ itself, not $\log S$, and by choosing the arc that avoids re‑entering the spike. The scaling argument above is the correct heuristic; the clean statement is $(\clubsuit)$, which needs (1) to make $\int e_s$ explicit.

3. **Transport constant for general $M$.** $(\heartsuit)$ uses the invariant inequality $|dw+\tfrac32w\,d\sigma|\le\tfrac12w|dU|+|b|$; Step 90 §5 verified the constants for diagonal $M$ and stated the invariant version. The coefficient $\tfrac12$ on $\sqrt{e_s}$ and the source $\tfrac{\beta}{\sqrt2}\rho^{3/2}$ should be re‑derived for general $M$ in the present normalization, since the whole sup bound scales with them.

## The other face: what stability + identity alone permit (the concentration mechanism)

To see that transport is *essential*, drop (iv) and ask what (i)+$(\star)$ allow. Prescribe local data with $h\equiv0$ (so $\rho$ constant on $C$, $\Lambda=1$), a charge spike $Q=A\chi(s/\ell_0)$ of unit mass ($A\ell_0=$ fixed $\le3\ell$), and let the shape map $U$ wiggle so that $e_s=2Q+12+O(\delta)$ carries $(\star)$; $q$ (the charge) and $U$ (the shape) are independent fields, so this is admissible local data. Check $(\diamondsuit)$: with $h=0$ the potential is $9-E_{\nu\nu}-D-\tfrac12e_s$, a shallow constant $\approx9$ with a narrow well of *integrated* strength $\int\tfrac12 e_s\approx1$. The ground state of $-\partial_s^2+9$ on the circle is depressed by only $O(1)$ by a unit‑strength well, staying positive; so $(\diamondsuit)$ holds. Hence **stability together with the scalar identity comfortably tolerate an arbitrarily tall, bounded‑mass $Q$‑spike.** What excludes it is exactly $(\heartsuit)$: with $e_s\approx2A$ the accumulated transport exponent over width $\ell_0\sim1/A$ is $\sqrt{A/2}\cdot A^{-1}=A^{-1/2}\to0$, so the charge *cannot physically rise* to height $A$ over that width. This is the precise sense in which "no pointwise bound follows from stability" (the Step 92 JSON conclusion) is correct, and the precise place where the Maxwell law changes the answer.

## Summary of the interaction structure

$(\star)$ is the hinge: it trades a $Q$/$e_\nu$ concentration for a tangential $\{h_s,h^2,e_s\}$ concentration. The full Jacobi form with the drift‑annihilating test $\phi_0=\rho^{-2}$ yields the new two‑sided weighted control $(\triangle)$ of $h^2$ and $e_s$. The Maxwell transport $(\heartsuit)$, whose rate is $\tfrac12\sqrt{e_s}$, then reads $(\triangle)$ as a finite exponential budget and, against the stability mass bound $\langle Q\rangle\le3+\delta$, forces $(\clubsuit)$ — a finite sup bound preventing $Q$‑concentration, with $Q_{\max}\to0$ like $\ell^2/\log^2(1/\delta)$ when the charge background is small. The orbit equation (v) then transfers this to $e_\nu$ through the bounded harmonic‑map forcing $|\nabla Q|=Q$. The whole chain becomes a theorem the moment the $\rho$‑oscillation on $C$ is bounded from the global $L\sigma=6+Q-T$ elliptic equation; that Harnack estimate, plus the general‑$M$ transport constant, are the two concrete pieces of mathematics still to be supplied.