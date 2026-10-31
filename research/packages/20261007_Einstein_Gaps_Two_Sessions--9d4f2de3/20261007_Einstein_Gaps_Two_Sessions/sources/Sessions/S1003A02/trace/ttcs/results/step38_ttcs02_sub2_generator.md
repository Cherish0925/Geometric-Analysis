# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Knowledge/objects/papers/Algebraic-surfaces-and-Seiberg-Witten-invariants--d573804ced34--70869ee25818/object.md"
  ]
}
```

## Task

Develop the paired-monopole route into an exact covariant PDE/energy identity, or show structurally why it cannot yield a per-exceptional-class excess. Let two actual Seiberg-Witten solutions correspond to determinant classes differing by 2E_i, with relative twisting line N of c1=E_i, u=<Phi',Phi> in N* and w=Phi wedge Phi'. Starting from the Dirac and curvature equations in the stated normalization, derive as far as possible: covariant derivative/Bochner equations for u and w; how the relative connection curvature (f-f')/2 enters; whether a Bogomolny/vortex completion relates its 4pi^2 negative-square charge to amplitude depletion, |w|^2, or relative spin-direction energy; and what hypotheses would make a positive tariff possible. Test the formula against the two essential regimes: Kähler amplitude vortex along E, and perpendicular null-period geometry where orthogonality/rotation can carry the zero. A useful result should be an exact identity, a precise conditional inequality, or a precise obstruction/countermechanism—not a generic research list.

## Output

## The paired single-class problem, resolved into exact identities plus a precise reason no local excess exists

Set $N=N_{\epsilon'\epsilon}$, $c_1(N)=E:=E_i$, $E^2=-1$. Two actual solutions in the stated normalization ($s=-4$, $|\sigma(\Phi)|^2=|\Phi|^4/8$, $\rho=|\Phi|^2\le2$):
$$D_A\Phi=0,\quad F_A^+=2i\sigma(\Phi);\qquad D_{A'}\Phi'=0,\quad F_{A'}^+=2i\sigma(\Phi').$$
Relative connection $B$ on $N$, $\nabla_{A'}=\nabla_A\otimes1+1\otimes\nabla_B$, $F_{A'}-F_A=2F_B$. Write $F_B=i\varphi$, $\varphi$ real, $[\varphi/2\pi]=\pm E$. Objects: $u=\langle\Phi',\Phi\rangle\in\Gamma(N^*)$, $w=\Phi\wedge\Phi'\in\Gamma(\det S^+\otimes N)$.

### 1. Exact relative-curvature splitting (where the $4\pi^2$ lives)

From the two curvature equations, the self-dual relative curvature is pinned to field bilinears, while the whole mandatory charge is thrown into the anti-self-dual part:
$$\varphi^+=\sigma(\Phi')-\sigma(\Phi),\qquad |\varphi^+|^2=\tfrac14|f^+_\epsilon-f^+_{\epsilon'}|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2},$$
$$\int\varphi\wedge\varphi=4\pi^2E^2\cdot(-1)=4\pi^2\ \Longrightarrow\ \boxed{\;\|\varphi^-\|_2^2=\|\varphi^+\|_2^2+4\pi^2\;}$$
This is the decisive structural fact at the single-class level. The $4\pi^2$ is **not** a quantity the equations convert into amplitude depletion, $|w|^2$, or rotation energy: those three are exactly $\|\varphi^+\|^2$, and topology forces $\|\varphi^-\|^2$ to exceed $\|\varphi^+\|^2$ by a fixed amount. The Seiberg–Witten equations determine $\varphi^+$ pointwise and say nothing pointwise about $\varphi^-$. A Bogomolny completion wants $\|\varphi^-\|^2\le\|\varphi^+\|^2+(\text{field energy})$; the identity gives the reverse with a rigid gap. So the per-class charge sits in the anti-self-dual $U(1)$ sector, which the local system leaves free. This is monopole blindness made exact for one class.

### 2. Exact Bochner equations for $u$ and $w$

Using the SW Weitzenböck $\nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi$, $\nabla_{A'}^*\nabla_{A'}\Phi'=(1-\rho'/2)\Phi'$ and the product rule for the rough Laplacian,
$$\boxed{\;\Delta_B u=\Big(2-\tfrac{\rho+\rho'}{2}\Big)u-2\big(\nabla_{A'}\Phi',\nabla_A\Phi\big)_{\!\rm tr},\qquad
\Delta w=\Big(2-\tfrac{\rho+\rho'}{2}\Big)w-2\big(\nabla_A\Phi\wedge\nabla_{A'}\Phi'\big)_{\!\rm tr}.}$$
The potential $V=2-\tfrac{\rho+\rho'}{2}\in[0,2]$ is $\ge0$ throughout. Pairing the first with $u$ and integrating on closed $M$,
$$\|\nabla_B u\|_2^2+2\,\mathrm{Re}\!\int\big\langle(\nabla_{A'}\Phi',\nabla_A\Phi)_{\rm tr},u\big\rangle=\int V|u|^2 .$$
The relative curvature enters only through the commutator when one tries to turn $(\nabla_{A'}\Phi',\nabla_A\Phi)_{\rm tr}$ into a signed square: the two Dirac equations fix the Clifford traces $\sum e_j\!\cdot\!\nabla_{A,e_j}\Phi=0$ and likewise for $\Phi'$, hence they control the $J$-$(0,1)$ part of $\nabla_B u$ **only relative to each spinor's own almost-complex structure** $J_\Phi,J_{\Phi'}$ (the direction of $\sigma(\Phi),\sigma(\Phi')$). The cross term is sign-definite exactly when $J_\Phi=J_{\Phi'}$; it is sign-indefinite when they disagree. Thus no free Bogomolny bound exists, and $u\equiv0$ (pointwise orthogonal spinors) always solves this Bochner — the countermechanism is admissible, not excluded.

### 3. The paired data is the Walsh single-coordinate projection — no new positive term

Decompose $f_\epsilon=\bar f-\varphi$, $f_{\epsilon'}=\bar f+\varphi$, where $\bar f=\tfrac12(f_\epsilon+f_{\epsilon'})$ represents $\tfrac12(a_\epsilon+a_{\epsilon'})=c+\sum_{j\ne i}\epsilon_jE_j$ (the $E_i$ term cancels). Then
$$\tfrac12\big(\|f_\epsilon^-\|^2+\|f_{\epsilon'}^-\|^2\big)=\|\bar f^-\|^2+\|\varphi^-\|^2,\qquad \|\varphi^-\|^2\ge4\pi^2 .$$
Here $\varphi$ **is** the Walsh component $f_{\{i\}}$ and $\bar f$ **is** the $i$-removed field. Because $P$ contains $+2\|f^-_\epsilon\|^2$ (the chern-single-cost identity), the sign-average over the single coordinate reproduces $+2\|\varphi^-\|^2\ge8\pi^2$ per class — exactly the term the full Walsh identity already extracts. The Fierz relations $|u|^2+|w|^2=\rho\rho'$, $|u|^2-|w|^2=\rho\rho'\,n\!\cdot\!n'$ show $u,w$ carry no information beyond $(\rho,\rho',n\!\cdot\!n')$, which are the same data entering the single-field decomposition. Consequence, stated as a proposition one can prove by the Parseval step above:

> The paired triple $(u,w,\varphi)$ for one sign flip is the single-coordinate Walsh projection of the sign-averaged simultaneous identity. It recovers the full $8\pi^2$ per class inside $2\mathbb E\|f^-\|^2=2\|\bar f^-\|^2+2\|\varphi^-\|^2$, and it reproduces the kinetic deficit $-4\mathbb E K$ unchanged. It introduces no term capable of dominating that deficit, because $\varphi^-$ is $L^2$-orthogonal to the field bilinears it would have to control.

So the paired route **cannot** yield a per-class excess beyond $8\pi^2Q-4\mathbb E K$: the only genuinely new object, $\varphi^-$, is topologically forced but field-undetermined, and its coupling into $P$ is the already-known contribution, not a surplus.

### 4. The one conditional inequality that would help, and the regime test

The usable positive content is a self-dual-projection bound. Since $\varphi/2\pi$ represents $\pm E$, its self-dual part dominates the self-dual harmonic projection of the class:
$$\boxed{\;\int_M\Big(\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}\Big)=\|\varphi^+\|_2^2\ \ge\ 4\pi^2\,(E^+_g)^2\;}$$
where $(E^+_g)^2$ is the self-dual square of $E$ for the metric $g$ (the quantity in LeBrun's $\mathfrak a^2(M)=\inf_H\max_a(a^+_H)^2=A$).

**Kähler amplitude-vortex regime.** Both canonical-type solutions have aligned $J_\Phi=J_{\Phi'}=J_0$, so $w\equiv0$, $n\!\cdot\!n'=1$; $u=\overline{\alpha'}\alpha$ with $\alpha'$ an honest holomorphic section vanishing to order $1$ along the exceptional curve. The Bochner cross term is sign-definite, Poincaré–Lelong applies against the Kähler form, and the exceptional area $e_i=E\!\cdot\![\omega]>0$ gives a genuine amplitude vortex. Here the full tariff is already secured globally and more cheaply by $C_+(g)=\tfrac1{32\pi^2}\int s^2\ge A$, $P\ge8\pi^2k$ (Theorem K-blow-up); the per-class bound is a scalar-curvature statement, robust as $e_i\to0$.

**Perpendicular null-period regime.** Here $J_{\Phi'}=-J_\Phi$ at the orthogonality locus: $n'=-n$, $u\to0$ by $\cos\gamma\to-1$, $|w|^2\to\rho\rho'$ with $\rho,\rho'$ staying near $2$. The field's compatible self-dual form has vanishing projection on $E$: $(E^+_g)^2=0$, so the conditional inequality is vacuous, Wirtinger/Poincaré–Lelong give nothing, and the vortex charge of $u$ is carried by $\omega$-null relative spin rotation. The extreme $u\equiv0$ (identically orthogonal spinors, $w$ full) is admissible by the Bochner of §2. This is precisely the cheap cell $P/(8\pi^2)\approx0.9957$ per blow-up, and the slight dip below $1$ is the Weyl–volume exchange of Theorem C, not a paired-field effect.

### 5. What a positive tariff would require (a global input, not a local identity)

A per-class excess of order $8\pi^2$ on a near-minimizing sequence is equivalent to a uniform lower bound $\min_i(E^+_{i,g})^2\ge\delta>0$, i.e. the self-dual projections of the exceptional classes do not collapse into the anti-self-dual subspace. The convex budget $\mathfrak a^2(M)=\mathfrak b^2(M)=A$ controls the aggregate self-dual projection of the full sign family but permits individual $(E^+_i)^2\to0$; the perpendicular cell realizes exactly this collapse. Equivalently, in the signed-density language $P=8\pi^2N+Z$, what is wanted is the compensation $Z\ge8\pi^2(Q-N)-o(Q)$, i.e. the scalar-square / Weyl allocation among exceptional regions, controlling where the forced anti-self-dual charge $\varphi^-$ is deposited. The paired algebra does not supply this: it is Parseval-equivalent to the averaged field identity and transfers the whole difficulty into the undetermined anti-self-dual sector. The input that could change the verdict is a construction either (i) forcing $(E^+_{i,g})^2$ bounded below for every competitive closed metric with $b_+\ge2$ (yielding $\|\varphi^+\|^2$, hence the $|w|^2$/rotation energy, per class), or (ii) producing a closed metric with $b_+\ge2$ carrying the whole sign family simultaneously in which the perpendicular null-period cell survives with $\sum_i(E^+_{i,g})^2=o(Q)$ — which would show the per-class tariff genuinely dips below $8\pi^2$. Deciding between these is a global self-dual-projection question about the metric, independent of the $u,w$ construction.