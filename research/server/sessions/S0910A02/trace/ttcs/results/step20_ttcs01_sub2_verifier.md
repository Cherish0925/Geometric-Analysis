# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step13_preceptor_toric_spectral_review.md",
    "Sessions/S0910A02/workspace/notes/step14_faberkrahn_reduced_system_and_fork.md",
    "Sessions/S0910A02/workspace/notes/step19_toric_rod_corner_matching_execute.md",
    "Sessions/S0910A02/workspace/notes/step12_toric_determinant_volume_gap_probes.md"
  ]
}
```

## Task

I am testing a proposed reduction of a 4D toric volume-gap question to a 2D Dirichlet eigenvalue question, for the Yau Problem 26 positive-branch crux on #_k(S^2 x S^2). Please verify the LOGIC and CORRECTNESS of the reduction and tell me exactly what the decisive 2D computation is, catching any gap. SETUP (see step13_preceptor_toric_spectral_review.md and step12/step14 notes): A T^2-invariant 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a curved polygon, geodesic edges, right-angle corners), with w = pq the orbit-area density, vanishing on partial Omega, positive inside. For exact Einstein Ric=g: -Delta_B w = 2 w (twist-free), so w is the Dirichlet ground state with eigenvalue 2; for delta-pinched positive metrics lambda_1^Dir(Omega, g_B) in [2(1-delta), 2(1+delta)]. Volume identity: Vol_4 = 4 pi^2 int_Omega w dA_B; and 2 int w = -int_{partial Omega} partial_nu w ds = total flux = sum of rod fluxes, where on a p-rod smooth toric closure gives |grad p| = 1 so partial_nu w = q there, i.e. rod flux = int_rod q ds (area of the collapsing 2-sphere). Gauss-Bonnet with right-angle corners pins int_Omega K_B dA = 2 pi - (pi/2) m, m = number of corners = chi(M) = 2k+2. Step 19 found a formal collapsing SEED: on even polygon m=2k+2 with alternating primitive labels, each rod has edge curvature K_B|edge = -A with A = m^2, transverse profile Q'' + (1+2A) Q = 0, rod length pi/sqrt(1+2A), rod flux 2/(1+2A), total flux ~ 1/m -> 0, base perimeter -> pi/sqrt(2). QUESTIONS: (1) Is it correct that the ENTIRE volume-gap fork reduces to whether a 2D disk with the pinned Gauss-Bonnet total, geodesic edges, right-angle corners, can sustain lambda_1^Dir approx 2 while int_Omega w (equivalently total flux, equivalently 4D volume) collapses to 0 as m -> infinity? (2) CRUCIAL: is int_Omega w really free to collapse independently, or is its scale fixed by the boundary normalization partial_nu w = (surviving fiber value) at each rod, so that the question is not a normalized eigenvalue question but a question about the ground state with GEOMETRICALLY FIXED Neumann data? Clarify whether lambda_1 approx 2 plus Area(Omega) >= c > 0 (Faber-Krahn, Step 14) already forces int w >= c' > 0, or whether a thin/concentrated w can have small integral while the eigenvalue stays near 2. (3) Does the negative-curvature-near-edges seed actually RAISE lambda_1 above 2(1+delta) (spectrally forbidding the collapse, giving a chi-uniform BUILD gap), or can strongly negative boundary-localized curvature keep lambda_1 approx 2 while shrinking the volume (BREAK candidate survives)? Give the sharpest rigorous statement you can about how lambda_1^Dir of a curved polygon responds to boundary-localized very negative curvature at fixed area, and whether McKean-type or curved-Faber-Krahn / total-curvature bounds decide it. Be concrete about which inequality is the right lever. Do NOT invent literature results; if a specific theorem is needed, name precisely what statement is required.

## Output

## Verifier memo: the toric → 2D reduction for the $\#_k(S^2\times S^2)$ positive-branch fork

### 0. What is solid before the three questions

The algebraic skeleton is sound and I can reproduce its internal logic. For a twist-free $T^2$-invariant $g=g_B+p^2d\theta^2+q^2d\phi^2$ with $w=pq$:

- $-\Delta_B w=2w$ with $w>0$ inside $\Omega$ and $w=0$ on $\partial\Omega$ forces $w$ to be a *positive* Dirichlet eigenfunction, hence the ground state and $\lambda_1^{\rm Dir}(\Omega,g_B)=2$ exactly. This step is correct.
- $2\!\int_\Omega w=-\int_{\partial\Omega}\partial_\nu w=\sum_i\int_{\rm rod_i}q_{\rm surv}\,ds$ and $\mathrm{Vol}_4=4\pi^2\int_\Omega w$. Correct.
- The upper bound $\lambda_1^{\rm Dir}\le 2(1+\delta)$ under $\|g^{-1}\mathrm{Ric}-I\|_{\rm op}\le\delta$ is the Rayleigh quotient of the trial function $w$; this is the direction actually used by Faber–Krahn, and it is sound. One correction: the two-sided statement $\lambda_1\in[2(1-\delta),2(1+\delta)]$ is not what the trace/Rayleigh argument gives — only the upper side is derived. The lower side $\lambda_1\ge 2(1-\delta)$ would require $w$ to be genuinely near the true ground state, which is a separate statement. Nothing downstream needs the lower side, but the notes should stop writing it as established.

So the reduction of *volume collapse* to *$\int_\Omega w\to0$* is exact within the invariant twist-free class. Two facts frame everything below: (a) the reduction to the invariant class itself (Step 13 obligation "general-to-invariant reduction") is assumed, so a full 2D resolution decides only the invariant subproblem, not $P_4^+$; and (b) the eigenvalue equation is only *one* of the coupled reduced equations.

### 1. Q1 — the fork does **not** reduce to a pure eigenvalue question

The correct reduced object is the full coupled system (your Step 14, eqs 1–4), not eq 1 alone:

1. $-\Delta_B w=2w$, $w=0$ on $\partial\Omega$;
2. $\mathrm{div}_B(w\nabla v)=0$, $v\to\pm\infty$ alternately at rods $(v=\log(p/q))$;
3. traceless horizontal equation $(\log w)_{zz}+\tfrac12[(\log w)_z^2+v_z^2]=0$;
4. $K_B=\tfrac14(|\nabla v|^2-|\nabla\log w|^2)$.

Two structural points follow.

- $K_B$ is **not** an input you may set to satisfy Gauss–Bonnet; eq 4 *determines* it from the fields, and then $g_B$ (its curvature) must be self-consistent with eqs 1–2. Consequently "$\int_\Omega K_B\,dA=2\pi-\tfrac\pi2 m$" is a compatibility identity the field configuration must reproduce, not a free assumption. The seed's "$K_B|_{\rm edge}=-A$, $A=m^2$" is a prescription for a quantity that, in a genuine solution, is dictated by $|\nabla v|^2-|\nabla\log w|^2$.
- Eq 3 is the load-bearing global constraint and is the one Step 19 never tested. Step 19 verified rod ODEs, corner jets, and determinant/label compatibility — all *local*. Eq 3 couples the *shape* of the ground state to the potential $v$ over the whole disk; its global solvability with $m$ matched logarithmic singularities of $v$ is exactly what is unknown.

So the accurate statement of Q1 is: the fork reduces to whether the coupled system 1–4, with unit-slope closure on **all** rods and right-angle geodesic corners, admits a family with $m\to\infty$ and $\int_\Omega w\to0$. Rewriting it as "can a disk with pinned Gauss–Bonnet and $\lambda_1\approx2$ have $\int_\Omega w\to0$" drops eqs 2–4, which is where the answer lives.

### 2. Q2 — the decisive correction: $\int_\Omega w$ is a *gauge freedom* of eqs 1–4

This is the sharpest correction to the intended picture, and it is airtight.

**Claim.** Eqs 1–4 are invariant under $w\mapsto c\,w$ (any constant $c>0$) with $v$ and $g_B$ held fixed.

*Verification.* (1) is linear in $w$; (2) $\mathrm{div}(cw\nabla v)=c\,\mathrm{div}(w\nabla v)=0$; (3) and (4) depend on $w$ only through $\log w$, and $\nabla\log(cw)=\nabla\log w$, $(\log(cw))_{zz}=(\log w)_{zz}$. So $(cw,v,g_B)$ solves the same system. ∎

Therefore $\lambda_1^{\rm Dir}=2$ says **nothing** about $\int_\Omega w$: the eigenvalue equation is scale-blind, and $\int_\Omega w$ is a free multiplicative parameter of eqs 1–4. This is *not* a normalized eigenvalue question.

What breaks the scale is the smooth-closure condition $|\nabla p|=1$ on the collapsing circle (unit slope). It is not a normalization one imposes for convenience; it is the no-cone condition. I checked this concretely on $S^2\times S^2$: with $p=\sin x$, $q=\sin y$, flat $g_B$, rescaling $w\mapsto c\,w$ gives $p'=\sqrt c\sin x$. The rod metric $dx^2+c\sin^2x\,d\theta^2$ still has $K\equiv1$ but slope $\sqrt c$ at $x=0$, i.e. a cone unless $c=1$. So eqs 1–4 admit the whole one-parameter family; only $c=1$ closes smoothly. This confirms both that eqs 1–4 are genuinely scale-invariant and that unit slope is the scale-fixing input.

**The key consequence for your Q2.** Unit slope constrains the *collapsing* fiber, $|\nabla p_{\rm coll}|=1$. But
$$
\partial_\nu w\big|_{\rm rod}=|\nabla p_{\rm coll}|\cdot q_{\rm surv}=q_{\rm surv},
$$
the value of the *surviving* fiber. The surviving fiber is free to be uniformly small. In the Step-19 seed $q_{\rm surv}(s)=\sin(\omega s)/\omega$ has amplitude $1/\omega\sim1/m$: unit slope holds on the collapsing side (no cone), yet $\partial_\nu w\sim1/m$ everywhere on $\partial\Omega$, so $\int_\Omega w=\tfrac12\sum_i\int q_{\rm surv}\sim1/m\to0$. The corner matching $Q'(0)=1$ keeps the surviving profile smooth at fixed points while its interior amplitude stays $O(1/m)$.

Hence, directly answering Q2: **unit slope does not force $\int_\Omega w\ge c'$.** The "geometrically fixed Neumann data" you hoped for pins the derivative of the *collapsing* fiber, not the amplitude of the *surviving* one, and it is the surviving amplitude that carries the volume. Faber–Krahn (using $\lambda_1\le2(1+\delta)$) bounds only the base **area** $A\ge\pi j_0^2/(2(1+\delta))$; it does not bound $\int_\Omega w$, because $\int_\Omega w$ is not comparable to $A$ once the ground state is normalized by the small surviving fibers rather than by its own $L^2$ or sup. A thin, uniformly small $w$ over a base of area $\ge9$ keeps $\lambda_1=2$ (scale-blind) while $\int_\Omega w\to0$. So the naive pinning does not hold.

### 3. Q3 — negative-curvature-near-edges does **not** raise $\lambda_1$; the eigenvalue is the wrong lever

McKean-type lower bounds ($\lambda_0\ge(n-1)^2a^2/4$ for $K\le-a^2$) require curvature below zero *everywhere on a complete manifold*; they do not apply to curvature concentrated in thin collars of a compact disk. So they cannot be invoked to forbid the seed.

A direct estimate settles the response of $\lambda_1$ to edge-localized strongly-signed curvature at fixed area. The seed has $K_B\sim-m^2$ in collars of width $\varepsilon\sim1/m$ along rods of length $\sim1/m$; the affected area is $\sim m\cdot(1/m)(1/m)=O(1/m)\to0$. The ground state there is $w\sim q_{\rm surv}\,t\sim(1/m)(1/m)=1/m^2$, so $\int_{\rm collars}w^2\sim(1/m)(1/m^2)^2=1/m^5$, negligible against $\int_\Omega w^2\sim A\cdot(1/m)^2\sim1/m^2$. The Rayleigh quotient is therefore governed by the bulk, and the collar perturbs $\lambda_1$ by $O(1/m^3)$. So $\lambda_1$ stays inside $[2(1-\delta),2(1+\delta)]$ and the collapse is **not** spectrally forbidden. The BREAK candidate survives the spectral test.

Sharpest rigorous statement I can give: for the Dirichlet ground state, metric perturbations supported in a collar of $g_B$-width $\varepsilon$ where the ground state has $L^2$-mass $O(\varepsilon^{3})$ move $\lambda_1$ by $o(1)$ as $\varepsilon\to0$, regardless of the pointwise curvature magnitude there. Edge-localized curvature of large magnitude and either sign is spectrally invisible in this regime. This is why neither McKean nor a curved-Faber–Krahn bound is the right lever.

### 4. A tempting isoperimetric lever, and why the corners defeat its naive form

There is a real geometric tension worth stating precisely, together with why it is not yet a contradiction. Faber–Krahn gives base area $\gtrsim\pi j_0^2/2\approx9$, while the seed's total rim length is $\sum_i L_i=mL_m\to\pi/\sqrt2\approx2.22$. For a simply connected domain the Bol–Fiala isoperimetric inequality $L^2\ge 4\pi A-2A\!\int_\Omega K^+\,dA$ (classical; the exact coefficient and the hypothesis $\int K^+<2\pi$ should be checked against a source before quantitative use) would then force $\int_\Omega K_B^+\gtrsim2\pi$: the disk must carry order-$2\pi$ of curvature above zero to enclose area $\ge9$ with such a short rim.

But this does **not** close into a contradiction, for a reason the notes have not spelled out: the domain has $m$ right-angle corners, each a convex turning of exterior angle $\pi/2$. In the corner form of Gauss–Bonnet / Bol–Fiala these turnings act as positive concentrated curvature of total mass $m\pi/2\to\infty$, which is exactly what lets a short-rim, moderate-area, many-cornered domain exist (balanced by $\int_\Omega K_B=2\pi-\tfrac\pi2 m\to-\infty$). So the area-vs-perimeter tension is absorbed by the corner turnings, and the Faber–Krahn constant $\pi j_0^2$ itself is not reliable here — Step 14's own note that "the sharp constant depends on $g_B$" is the correct reading, and convex corners plus $K_B<0$ can push it below the flat value. I therefore do not offer the isoperimetric contradiction as decisive; it is defeated by the corner budget. This is the concrete reason the signed Gauss–Bonnet total (Step 13's remark that it controls only $\int K_B$, not $\int K_B^-$) is insufficient, and why a second lever built on $\int K^+$ alone will not decide the fork unless corner turnings are carried explicitly.

### 5. The decisive 2D computation

Because the eigenvalue is scale-blind (§2) and edge curvature is spectrally invisible (§3) and the signed Gauss–Bonnet total is corner-degenerate (§4), the fork is decided by the **global solvability of the coupled system 1–4 with unit slope on all rods**, and specifically by two objects Step 19 did not touch:

1. **Simultaneous unit slope (equal-slope rigidity).** Eqs 1–4 fix the configuration only up to $w\mapsto cw$; one constant $c$ can set $|\nabla p|=1$ on a single rod. Smooth closure requires it on all $m$ rods at once, i.e. the un-normalized solution must have *equal* collapsing-fiber slopes on every rod. This is automatic in the fully symmetric seed but is a genuine $(m{-}1)$-fold constraint for any non-symmetric assembly, and it is the exact place where non-coordinate labels / asymmetric rod data could obstruct.
2. **Global traceless equation (eq 3) with $m$ matched log-singular potentials.** Given the ground state $w$ (eq 1) and the div-free potential $v$ (eq 2, with prescribed $\pm\infty$ singularities at alternating rods), eq 3 must hold in the interior and eq 4 must reproduce $\int K_B=2\pi-\tfrac\pi2 m$. This is the untested global compatibility.

Concretely, the computation that would move the judgment is the one Step 14 §9 already named, but with the *right measured quantity*: on model $m$-gons ($m=6,8,10,\dots$) solve the coupled iteration — fix a conformal factor / $g_B$, solve eq 1 for $w$ and eq 2 for $v$ with the seed's rod singularities, recompute $K_B$ from eq 4, update $g_B$, and then measure the **residual of eq 3** and the **spread of collapsing-fiber slopes across rods**, *not* the eigenvalue. If the eq-3 residual and slope-spread can be driven to zero as $m$ grows while $\int_\Omega w\to0$, BREAK is real; if they are bounded below uniformly in $m$, that is the $\chi$-uniform BUILD obstruction. The Step-18 warning about coarse finite-difference residuals applies: the measured quantity must be a genuine solution residual at controlled resolution, not a global norm on an uncontrolled family.

### 6. The theorem that a BUILD conclusion would require

I will not attribute this to any existing result. The statement that must be proved (or refuted) is a coupled gradient/Harnack estimate, of the form:

> For any smooth solution $(w,v,g_B)$ of eqs 1–4 on a simply connected disk with geodesic edges, right-angle corners, unit-slope closure on all $m$ rods, and $\lambda_1^{\rm Dir}=2$, the total surviving-fiber flux satisfies $\sum_i\int_{\rm rod_i}q_{\rm surv}\,ds\ge c_0>0$ with $c_0$ independent of $m$.

Equivalently, one needs a lower bound on the boundary flux of the unit-slope-normalized ground state that is uniform in the corner number. The natural mechanism is that eq 3 forbids the potential $v$ from carrying $m$ independent log-singularities of matched strength while $w$ remains uniformly $O(1/m)$ near all of $\partial\Omega$ — i.e. a rigidity coupling $v$'s singular structure to $w$'s decay rate that the seed's local jets cannot see. Faber–Krahn and McKean are not this theorem; the correct lever is an interior gradient estimate for $(\log w, v)$ tied to unit-slope closure. Absent such an estimate, the current record neither proves the $\chi$-uniform gap nor exhibits a genuine global metric; Step 19's local certificate removes a local obstruction but does not decide the fork, exactly as its §5 states.

### 7. One-line summary of the corrections

- Q1: reduces to the full system 1–4 with unit slope, not to the eigenvalue equation; eq 4 makes $K_B$ dependent, and eq 3 is the untested global constraint.
- Q2: $\int_\Omega w$ is a gauge freedom of eqs 1–4 (verified on $S^2\times S^2$ via the cone at $c\ne1$); unit slope fixes the *collapsing*-fiber slope, while $\partial_\nu w=q_{\rm surv}$ can shrink uniformly, so $\int_\Omega w\to0$ is not obstructed; Faber–Krahn bounds area, not $\int_\Omega w$.
- Q3: edge-localized strongly-signed curvature perturbs $\lambda_1$ by $O(1/m^3)$; McKean is inapplicable; the spectral lever does not forbid collapse, and the naive isoperimetric contradiction is absorbed by the $m\pi/2$ corner turnings.
- Decisive computation: global solvability of eqs 1–4 measured by the eq-3 residual and cross-rod slope spread on model $m$-gons; the BUILD statement needed is a $m$-uniform lower bound on total surviving-fiber flux for the unit-slope-normalized ground state.