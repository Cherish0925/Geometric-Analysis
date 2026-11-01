# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Knowledge/objects/papers/Chern-simons-forms-on-associated-bundles-and-boundary-terms--3042b35791e1--e9926094f32d/object.md",
    "Knowledge/objects/papers/Equivariant-differential-characters-and-Chern-Simons-bundles--77afec5243aa--a7a34ef1ebd0/object.md"
  ]
}
```

## Task

Construct the corrected Pontryagin/transgression approach for a collapsed near-critical Ishida–LeBrun sequence. Use the Levi-Civita characteristic density rho_+=(1/(4pi^2))(s^2/24+2|W+|^2-|Ric0|^2/2), whose L1 distance from 3/(16pi^2) tends to zero, so characteristic mass follows volume. Compare the Levi-Civita connection on Lambda^2_+ to a basic or split connection on a regular circle/nil collapse region. Derive the exact Chern–Simons transgression structure, explain what non-basic/O'Neill terms must persist for rho_+ to remain diffuse, and seek an inequality linking diffuse characteristic density to fixed-scale cover accessibility, fiber holonomy, or eigenline rotation. Avoid assuming local charge quantization or concentration at NUT cores. Give concrete equations and a viable proof program or a counterexample mechanism.

## Output

## Scientific memo: the self‑dual Pontryagin density as a collapsing $SO(3)$ gauge field

The task is really asking to re‑cast the $\lambda<0$ four‑dimensional threshold problem as a statement about one $SO(3)$ connection — the Levi‑Civita connection $A^+$ on $\Lambda^2_+M$ — carrying a fixed topological charge $p_1(\Lambda^2_+)=2\chi+3\tau=2A/3$ whose density is forced to spread out. Below I build that reformulation, give the exact transgression algebra, isolate which structural terms must survive a circle/nil collapse, and extract a concrete inequality that links diffuse density to fiber holonomy, cover accessibility, and eigenline rotation. I then state where a genuine counterexample would have to live.

### 1. $\rho_+$ is the Chern–Weil density of $A^+$, and near threshold its curvature is spectrally rigid

$A^+$ has curvature $F^+\in\Omega^2(M,\mathfrak{so}(3))\cong\Omega^2(M,\Lambda^2_+)$. As an endomorphism of $\Lambda^2_+$, its self‑dual block is $W_++\tfrac{s}{12}\mathrm{Id}$ and its mixed $\Lambda^2_+\!\otimes\!\Lambda^2_-$ block is $\tfrac12\operatorname{Ric}^\circ$. With $P(F)=\tfrac1{8\pi^2}\operatorname{tr}(F\wedge F)$,
$$
\rho_+\,d\mu \;=\; \tfrac1{8\pi^2}\operatorname{tr}(F^+\wedge F^+)\;=\;\tfrac1{4\pi^2}\Big(\tfrac{s^2}{24}+2|W_+|^2-\tfrac12|\operatorname{Ric}^\circ|^2\Big)d\mu,\qquad \int_M\rho_+\,d\mu = \tfrac{2A}{3}.
$$
The calibrated profile ($s\to-4$ uniformly, $|W_+|^2\to\tfrac1{24}$ in $L^1$, $|\operatorname{Ric}^\circ|^2\to0$) gives the stated diffuseness
$$
\Big\|\rho_+-\tfrac{3}{16\pi^2}\Big\|_{L^1}\to0,\qquad\text{hence}\qquad \int_U\rho_+\,d\mu=\tfrac{3}{16\pi^2}\operatorname{Vol}(U)+o(1)
$$
for every region carrying a fixed fraction of $\operatorname{Vol}=\tfrac{32\pi^2A}{9}$. Two consequences deserve emphasis:

- **Charge follows volume.** Because the density is asymptotically absolutely continuous with respect to $d\mu$ with constant weight $\tfrac3{16\pi^2}$, no positive part of $2A/3$ can collect on a set of shrinking volume. This is the exact reason a Taub–NUT‑type core, where $p_1$ concentrates near a bolt, is *not* the diffuse regime; concentration is forbidden a priori rather than assumed away.
- **Spectral rigidity of $F^+|_{\Lambda^2_+}$.** With $s/12\to-1/3$ and $\mathrm{Spec}(W_+)\to(-\tfrac16,\tfrac1{12},\tfrac1{12})$, the self‑dual block of $F^+$ tends to the sign‑definite operator with eigenvalues $(-\tfrac12,-\tfrac14,-\tfrac14)$, all strictly below zero and with a fixed gap $\tfrac14$ between the simple and double eigenspaces. So $A^+$ is not a free gauge field: its self‑dual curvature is asymptotically definite with prescribed spectrum. A definite curvature operator with $|F^+|^2\to\tfrac{17}{24}$ in $L^1$ is exactly the object that resists collapse of the bundle.

### 2. Exact transgression relative to a collapse‑adapted connection

For any second $SO(3)$ connection $A^\flat$ on $\Lambda^2_+$, set $a=A^+-A^\flat$, $A_t=A^\flat+ta$, $F_t=F^\flat+t\,d^\flat a+t^2\,a\wedge a$. The Chern–Simons relative form
$$
TP(A^+,A^\flat)=\tfrac1{4\pi^2}\int_0^1\operatorname{tr}(a\wedge F_t)\,dt,\qquad d\,TP(A^+,A^\flat)=P(F^+)-P(F^\flat),
$$
is the exact primitive. Choose $A^\flat$ **basic** on a regular collapse region $U\to B$ with $\dim B\le 3$ (a connection pulled back from the collapsed base, e.g. the base Levi‑Civita action on the frame $\{\omega_i\}$). Then $P(F^\flat)$ is a $4$‑form pulled back from a $\le3$‑manifold, so $P(F^\flat)=0$ and
$$
\boxed{\ \int_U\rho_+\,d\mu=\int_{\partial U}TP(A^+,A^\flat)\ }\tag{2.1}
$$
The interior bulk charge equals a flux through the enclosing hypersurface $\partial U$. Diffuseness forces the right side to grow like $\tfrac3{16\pi^2}\operatorname{Vol}(U)$ — a bulk quantity produced by a codimension‑one integral. With bounded transgression integrand this is only possible if $\partial U$ has $3$‑volume comparable to $\operatorname{Vol}(U)$, i.e. the region is long and thin (diameter growth), **or** the primitive is not globally defined and the deficit is carried by singular strata.

The rigorous accounting of that alternative is the heterotic/Johnson transgression on the associated sphere bundle. Take the unit $W_+$‑eigenline section $\sigma$ of $S(\Lambda^2_+)$ (the lowest eigenform, well defined where the spectral gap holds). Johnson's identity $d\Phi P_1=P_1(\Omega)-P_1(\Psi)$ with $P_1(\Psi)=0$ on this $S^2$‑bundle gives, exactly as in his Prop. 2.1/2.4,
$$
\int_U\rho_+\,d\mu=\sum_{p\in Z(\sigma)}\mathrm{ind}_p(\sigma)\;+\;\int_{\partial U}\sigma^*\Phi P_1(A^+).\tag{2.2}
$$
The point sum is an **integer** localized at eigenvalue‑crossing loci $\{\lambda_2(W_+)=\lambda_1(W_+)\}$; the second term is the smooth flux. Diffuseness ($\int_U\rho_+\sim\operatorname{Vol}(U)$, not an integer) means the integer part cannot supply $O(\operatorname{Vol})$: the crossing set cannot carry the mass. So again the diffuse charge must ride the smooth flux term, pushing toward a long $\partial U$ (diameter) or toward noncollapse.

### 3. Only the vertical–mixed curvature carries $\rho_+$; the O'Neill scaling

Model a regular circle collapse as $g=\pi^*g_B+\ell^2\eta\otimes\eta$, unit vertical coframe $\theta=\ell\eta$, $d\theta=\ell\,\pi^*\beta$, horizontal $\{e^1,e^2,e^3\}$, $d\mu=\theta\wedge dV_B$. Decompose $F^+=F^+_H+\theta\wedge\Xi$, $\Xi=\iota_VF^+$ (unit $V$). Because $\operatorname{tr}(F^+_H\wedge F^+_H)$ is a horizontal $4$‑form on a $3$‑manifold and vanishes,
$$
\boxed{\ \rho_+=\tfrac1{4\pi^2}\,\star_B\!\operatorname{tr}\!\big(\Xi\wedge F^+_H\big),\qquad |\rho_+|\le\tfrac1{4\pi^2}\,|\Xi|\,|F^+_H|.\ }\tag{3.1}
$$
Thus **diffuse $\rho_+$ requires the fiber‑directional curvature $\Xi=\iota_VF^+$ to be bounded below in $L^1$:** $|\iota_VF^+|\,|F^+_H|\ge \tfrac34+o(1)$. This is the exact "non‑basic term that must persist."

Now the O'Neill scaling determines whether a *bounded‑curvature* regular collapse can supply this. For totally geodesic fibers the mixed curvature is governed by the twist tensor $A_XY=\tfrac12\mathcal V[X,Y]$, with $|A|\sim\ell|\beta|$, so
$$
\Xi=R(V,\cdot)\big|_{\Lambda^2_+}=O\big(|A|^2+|\nabla A|\big)=O\big((\ell|\beta|)^2+\ell|\nabla\beta|\big),\qquad |W_+|\sim(\ell|\beta|)^2.
$$
Matching $|W_+|^2\to\tfrac1{24}$ and $|\Xi|\ge c$ both force the **maximal‑twist condition** $\ell|\beta|=O(1)$. Since $\ell\to0$, this needs $|\beta|\to\infty$: the fibration's Chern density over base $2$‑cells diverges. A bounded‑geometry base with fixed Chern numbers gives $|\beta|=O(1)$, hence $\ell|\beta|\to0$, hence $\Xi\to0$ and $\rho_+\to0$ on that region. In words: **an ordinary bounded‑curvature circle collapse over bounded base geometry carries asymptotically no self‑dual Pontryagin density.** This is the analytic content behind the topological fact that infranil fibers are parallelizable and contribute zero characteristic mass; here it is made local and quantitative through (3.1).

### 4. Eigenline reduction: the near‑symplectic Euler form and its $O(1)$ non‑closedness

Where the gap $g(x)=\lambda_2(W_+)-\lambda_1(W_+)\ge c>0$ holds, $\Lambda^2_+=L\oplus L^\perp$, $L=\langle\sigma_1\rangle$ rank $1$, $L^\perp$ rank $2$. Write $A^+$ in this splitting with off‑diagonal second fundamental form $\Phi\in\Omega^1(\mathrm{Hom}(L,L^\perp))$ — the eigenline rotation. The Weitzenböck computation gives $\int|\nabla\sigma_1|^2=(1+o(1))\int|\sigma_1|^2$, i.e.
$$
\|\Phi\|_{L^2}^2=(1+o(1))\operatorname{Vol},
$$
so the rotation energy is $O(1)$, not small. The $SO(2)$ curvature $F^{L^\perp}$ of the rank‑$2$ factor is an honest local Euler form, and the structure identity for a reduced $SO(3)$ bundle reads
$$
\operatorname{tr}(F^+\wedge F^+)=F^{L^\perp}\!\wedge F^{L^\perp}\;-\;2\,\langle \nabla^\perp\Phi\wedge\nabla^\perp\Phi\rangle\;+\;2\,d\!\left\langle\Phi\wedge \iota\,F^{L^\perp}\right\rangle.\tag{4.1}
$$
This exhibits the whole diffuse density as a competition between two mechanisms:

- **Near‑symplectic channel.** $F^{L^\perp}\!\wedge F^{L^\perp}$ diffuse means $F^{L^\perp}$ is a definite‑magnitude $2$‑form with $\tfrac1{4\pi^2}\int F^{L^\perp}\!\wedge F^{L^\perp}=e(L^\perp)^2=-\tfrac{2A}{3}$ — morally the Ricci/Kähler form of the forbidden almost‑Kähler structure appearing directly at the level of curvature densities. The essential obstruction to promoting this into the Ishida–LeBrun contradiction is that $F^{L^\perp}$ is **not closed**: $dF^{L^\perp}$ is exactly the rotation $\Phi$, and $\|\Phi\|_{L^2}^2=O(\operatorname{Vol})$. The $O(1)$ eigenline rotation is precisely the $O(1)$ non‑closedness that prevents a naive symplectic class from forming without compactness. Full $SO(3)$ Bianchi keeps $\tfrac1{8\pi^2}\operatorname{tr}(F^+\wedge F^+)$ topological; the non‑closedness of $F^{L^\perp}$ is compensated by the $\Phi$ terms in (4.1).
- **Rotation channel.** $\langle\nabla^\perp\Phi\wedge\nabla^\perp\Phi\rangle$ diffuse means the eigenline itself twists fast enough to generate the Pontryagin density. This is the channel compatible with a twisted/nil collapse and is the live counterexample route.

Combining §3 with (4.1): whichever channel dominates, the diffuse $4$‑form needs the vertical coframe $\theta$, so it needs $O(1)$ **vertical** structure — either vertical $F^{L^\perp}$ (a definite fiber magnetic field) or vertical rotation $\nabla_V\Phi$ (fiber holonomy of $\Lambda^2_+$ bounded below). Step‑9's estimate $\int|\nabla_V\sigma_1|^2=O(\ell^2)$ shows that under bounded curvature the vertical rotation vanishes; so under bounded curvature the *only* surviving source is a definite vertical $F^{L^\perp}$, i.e. definite fiber holonomy — which returns us to §3's maximal‑twist requirement.

### 5. The decisive inequality: diffuse density $\Rightarrow$ fiber‑holonomy area $\Rightarrow$ accessibility

Fix the curvature‑good set $G_i$ of §step9 (where $\mathcal M_1|Rm|^2\le K_0$, $\operatorname{Vol}(G_i)\ge V_\infty/2$); on it $\varepsilon$‑regularity yields effective bounds $|Rm|\le\Lambda(K_0)$ at a definite scale. The holonomy of $A^+$ around a fiber loop $\gamma_x$ of length $\ell$ satisfies, when $\gamma_x$ bounds a disk $D$,
$$
\big|\mathrm{hol}_{A^+}(\gamma_x)-\mathrm{Id}\big|=\Big|\!\int_D F^+\Big|+O\!\big(|F^+|^2\mathrm{Area}(D)^2\big).
$$
Diffuseness plus (3.1) forces the fiber curvature lower bound $|\iota_VF^+|\ge c$ on a positive‑volume subset, hence the fiber holonomy is bounded below, hence with $|F^+|\le\Lambda$,
$$
\boxed{\ \mathrm{Area}(D)\ \ge\ \frac{c}{\Lambda}\ >\ 0\ }\tag{5.1}
$$
for every disk spanning a charge‑carrying fiber. **A collapsing fiber that carries diffuse self‑dual charge cannot be a small contractible loop.** This is exactly the maximal‑rank/accessibility input the Naber–Zhang local‑cover package requires and the exact place where the Taub–NUT–AdS countermodel is inapplicable in the closed diffuse setting: there the collapsing $\psi$‑circle bounds a small disk through the NUT (Area $\to0$), so $|\iota_VF^+|\to0$ there and the charge is *not* diffuse near the collapse — the model concentrates $p_1$ at the core, precisely the excluded behavior. So the closed diffuse‑charge hypothesis supplies what the local model lacked. The chain is
$$
\text{diffuse }\rho_+\ \xrightarrow{(3.1)}\ |\iota_VF^+|\ge c\ \xrightarrow{(5.1)}\ \text{fiber holonomy‑area}\ge c/\Lambda\ \Rightarrow\ \text{local cover noncollapsed at }r_0(c,\Lambda),
$$
and then the bounded‑geometry exclusion theorem produces the smooth $\operatorname{Ric}=-g$ limit, saturating the mixed monopole estimate and yielding the $\lambda<0$ Kähler–Einstein structure that the connected‑sum topology of the $D=A/3$ family excludes. On the good set this closes the collapse escape route.

### 6. Where a counterexample must hide: the $\Lambda^2_-$ concentration channel and the energy budget

The argument runs on the curvature‑good set. The reverse‑orientation Pontryagin density
$$
\rho_-=\tfrac1{4\pi^2}\Big(\tfrac{s^2}{24}+2|W_-|^2-\tfrac12|\operatorname{Ric}^\circ|^2\Big),\qquad \int_M\rho_-=2\chi-3\tau,
$$
is **not** pinned by the near‑Einstein condition, because $|W_-|^2$ is only bounded through $\tau$, not calibrated. So all topological complexity that must concentrate is free to route through $\Lambda^2_-$: an anti‑self‑dual bubbling on shrinking sets (an ALE/ALF scalar‑flat or Ricci‑flat blow‑up carrying $W_-$‑energy and part of $\tau$), while $\Lambda^2_+$ stays diffuse and near‑calibrated on the complement. The genuine counterexample mechanism, if one exists, is therefore:

- a positive‑volume good region where $\Lambda^2_+$ is diffuse, definite, and by §5 noncollapsed — this region wants to become Kähler–Einstein and is where the obstruction bites; against a counterexample it must be prevented from filling definite volume;
- a small‑volume bad set where the $W_+$ gap $g(x)$ degenerates, $L^\perp$ is undefined, and where the eigenline‑crossing indices of (2.2) plus $W_-$ concentration absorb the topology, at the price of $\int|Rm|^2$ on shrinking volume.

Two quantitative pressures constrain the bad set. First, the topological energy budget $\int_M|Rm|^2\le E_0(A)$ caps how much curvature can concentrate: bubbling on volume $v\to0$ with $\int|F|^2\sim\!O(1)$ is allowed, but the *number* and *strength* of bubbles is bounded, and each smooth noncollapsed blow‑up is Ricci‑flat (so cannot itself carry the calibrated $\rho_+=\tfrac3{16\pi^2}$, which needs $s=-4$). Second, diffuseness of $\rho_+$ means the bad set cannot carry self‑dual charge, so the $\Lambda^2_+$ topology $2A/3$ lives entirely on the good, noncollapsed, near‑Kähler region — the region the obstruction forbids. A refutation of the pinching statement on this family would thus require a sequence in which the good region either splits into infinitely many diameter‑growing collars (so the flux in (2.1)/(2.2) is spread over a $\partial U$ of volume $\sim\operatorname{Vol}$) without ever accumulating a noncollapsed Kähler–Einstein germ, or in which the $W_+$ gap degenerates on a set of *positive* volume so that $L^\perp$ and the accessibility chain of §5 never apply. Both are sharply testable.

### 7. Proof program and computations that would decide it

The following are the quantities whose control would convert the above into a theorem or expose the counterexample.

1. **Gap‑set volume estimate.** Prove $\operatorname{Vol}\{x:\ g_i(x)<c\}\to0$ quantitatively from $|W_+|^2\to\tfrac1{24}$ in $L^1$ and the sharp spectrum, with a rate in $\delta_i$. If the bad set has volume $\to0$, the eigenline splitting and (5.1) hold on a definite‑volume good set. A positive‑volume gap set would be the counterexample's home; testing whether the calibrated $L^1$ profile permits it is decisive.

2. **Vertical‑curvature lower bound.** Establish rigorously the $L^1$ lower bound $|\iota_VF^+|\ge c$ on the charge‑carrying good set from (3.1), tracking the horizontal factor $|F^+_H|$ (bounded above by $|Rm|$). This is the analytic heart; it converts diffuseness into fiber holonomy.

3. **Holonomy‑to‑accessibility.** Turn (5.1) into the precise maximal‑rank hypothesis of the local‑cover noncollapse package on the good set, using the $\varepsilon$‑regularity effective bound $\Lambda(K_0)$. The output is a fixed $r_0$ noncollapse and a $C^{2,\alpha}$ harmonic chart, feeding the exclusion theorem.

4. **Energy accounting for the $W_-$ channel.** Bound the number and strength of anti‑self‑dual bubbles by $E_0(A)$, and show each Ricci‑flat blow‑up cannot host the calibrated $\rho_+$ density, so the diffuse self‑dual charge is trapped on the good region.

5. **Symbolic verification.** Recompute the coefficients in (4.1) and confirm the spectral values $F^+|_{\Lambda^2_+}\to(-\tfrac12,-\tfrac14,-\tfrac14)$, $|F^+|^2\to\tfrac{17}{24}$, and $\rho_+\to\tfrac3{16\pi^2}$ against `verify_deficit_constants.py`‑style scripts; check the Johnson normalization giving (2.2) with $\int_{\pi^{-1}(p)}\Phi P_1=1$, so eigenline‑crossing indices are genuine integers.

The unifying scientific content is that the $\lambda<0$ threshold problem in dimension four is equivalent to a collapse question for a *single* $SO(3)$ Yang–Mills field of bounded energy, definite curvature, and volume‑diffuse instanton density; and that diffuseness of that density is exactly the maximal‑rank/holonomy‑area input which the local collapse models (Taub–NUT included) do not by themselves furnish. Whether that input can be denied on a positive‑volume set — through gap degeneration or diameter‑spreading collars while routing all concentration through $\Lambda^2_-$ — is the precise fork on which either a rigidity theorem for this family or an explicit counterexample sequence turns.