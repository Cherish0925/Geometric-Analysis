# Step 87: CSCK calibration of the A1 normal obstruction and Einstein rigidity near a nodal negative-KE endpoint

Agent2, Execute. This continues the Step-86 handoff and Spirit #109/#110. The one-node quintic is the
working family, chosen because it can be tested, not because it is the only family of interest. The point
of this note is to separate which inputs the conclusion actually uses, so that the mechanism can be
carried to other families.

Script and data: `workspace/scripts/step87_csck_calibration.py` writes `workspace/data/step87/csck_calibration.json`.
All the exact identities used below have zero residual there.

## 0. What changes

Step 85 reduced the strict-AKE question near a smoothable A1 KE endpoint to a scale-uniform $C^1$ estimate
$\partial_{\zeta_I}\Lambda_I=A+o(1)$, $A=c_0 s/4$, for Ozuch's raw normal obstruction. Step 86 proposed
obtaining it by $C^1$ extension on the real blow-up of period space.

This note replaces the derivative estimate with two exact statements and a $C^0$ degree argument.

1. **Exact linear statement (§2).** On every smooth KE fibre near the endpoint, the Kähler normal mode is an
   exact TT eigentensor of the Einstein operator, with eigenvalue $-2E$. It is not merely an approximate kernel
   element.
2. **Exact nonlinear secant (§3).** Along the actual Biquard–Rollin CSCK family, which varies the real
   Kronheimer period $\zeta_r$, the full Einstein tensor is
   $\operatorname{Ric}-Eg=\operatorname{Ric}^\circ=\rho_0(\cdot,J\cdot)$. Here $\rho_0$ is the
   harmonic anti-self-dual representative of a cohomology class that is linear in $\zeta_r$ to leading order.
   Consequently $\Lambda_I=E\,\zeta_r\,(1+o(1))$ with no differentiation, and $c_0=1$ in the natural normalization.
3. **Coverage by degree (§4).** If the corrected CSCK family matches Ozuch's parameters to relative $C^0$
   accuracy, a degree argument shows that it fills the reduced Einstein-modulo-obstruction family. Every
   nearby Einstein metric then has $\zeta_r=0$ and is Kähler–Einstein.

Strict AKE is then excluded near the endpoint by Prop. 85.1 alone (§5). Neither the Step-85 center theorem
nor the neck-trace theorem is load-bearing on this route.

## 1. The family and its parameters (Spirit #110, Kloosterman §3)

$X_0=\{F_0=0\}\subset\mathbb P^3$ is a quintic with exactly one ordinary node $p$; it is otherwise generic.
Facts used, each checked in the JSON:

- $K_{X_0}=\mathcal O(1)$ is ample and the singularity is canonical $A_1$. $X_0$ has no holomorphic vector fields: it is of general type.
- **Embedded and abstract deformations.** $T^1_{\rm emb}=\mathbb C[x]_5/J_5$ has dimension $56-16=40$. For
  $d\ge 3$, $J_d/\mathbb C F$ is the tangent space of $\operatorname{Aut}\mathbb P^3$ (Kloosterman §3, lines 101–105).
  For $d\ge5$, embedded and abstract deformations agree (only $d=2,4$ are exceptional).
- **The 39+1 split.** The locally trivial (equisingular, $-2$-curve preserving) tangent space is
  $(I/J)_5=I_5/J_5$, where $I$ is the ideal of the node; its dimension is $55-16=39$ (Kloosterman §3).
  One node imposes one condition in degree 5, so there is no defect, and the nodal locus is smooth of
  dimension 39. The evaluation $G\mapsto G(p)$ maps $T^1_{\rm emb}\to T^1_{p}=\mathbb C$ surjectively with
  kernel $(I/J)_5$. Hence there are **39 complex locally trivial directions plus 1 smoothing direction**,
  making 40 directions, which equals $h^1(\Theta)$ for a smooth quintic.
- **Local smoothing.** Locally $F_0+tG$ reads $u^2+v^2+w^2=-tG(p)\cdot(\text{unit})$, so the versal parameter
  is $c=tG(p)$. On the Weyl double cover $c=q^2$, and $q$ is Kronheimer's $\zeta_c$.
- **Topology.** For the smooth fibre $M$: $c_1^2=5$, $\chi=55$, $\tau=-35$, $b_2=53$, $h^{1,1}=45$, $p_g=4$.
  For the orbifold $V$: $b_2=52$, $\chi_{\rm top}=54$. The vanishing class $\delta$ has $\delta^2=-2$ and $c_1\cdot\delta=0$.
- **Exterior Einstein premoduli of $V$** (Lemma 87.1).

**Lemma 87.1 (exterior centers are Kähler).** Near the orbifold KE metric $g_V$, the orbifold Einstein
premoduli coincides with the 78-real-dimensional family of orbifold KE metrics on locally trivial deformations.

*Proof.* (i) Nagy's identification of the Einstein kernel with the anti-$J$ Kodaira–Spencer space
$\{h\in\operatorname{Sym}^{2,-}:\bar\partial h=0,\delta h=0\}$ is adapted to the orbifold. The proof is local
plus Hodge theory on compact orbifolds; the Step-85 verifier flagged this as an adaptation, not a quotation.
This gives kernel dimension $2h^1(\Theta^{\rm orb}_V)=78$. (ii) Each of the 39 complex locally trivial
deformations is unobstructed, by smoothness of the nodal locus, and carries a unique orbifold KE metric
(orbifold Aubin–Yau). (iii) By Koiso, the premoduli is the zero set of a real-analytic Kuranishi map on the
78-dimensional kernel ball. That zero set contains a 78-dimensional submanifold, hence an open set, hence
the whole ball. $\square$

$H^{2,0}\neq0$ ($p_g=4$) throughout, so nothing here relies on vanishing holomorphic 2-forms.

## 2. Exact linear statement: the Kähler normal mode is an exact eigenmode

Nagy (object `2603.09028…`, lines 362–366), eq. (17): for $H\in\operatorname{Sym}^{2,+}$ with
$A=g(HJ\cdot,\cdot)\in\Omega^{1,1}$,
$$g^{-1}(\Delta_d-2E)A=(\Delta_E H)\circ J .$$

**Proposition 87.2.** Let $(M,g,J)$ be KE with $\operatorname{Ric}=Eg$, $E<0$, and let $\theta$ be a
harmonic primitive real $(1,1)$ form; such forms are exactly the harmonic ASD forms of type (1,1) in the
complex orientation. Then $H_\theta:=\theta\circ J$ is a TT tensor with
$$\Delta_E H_\theta=-2E\,H_\theta .$$
On the Hermitian (J-invariant) TT sector, $\Delta_E\ge-2E$, with equality exactly on these modes. For a
smooth quintic the multiplicity is at least $h^{1,1}-1=44$.

*Proof.* Apply Nagy (17) with $\Delta_dA=0$. The tensor is trace-free because $\theta$ is primitive, and
$\delta H_\theta\propto J\delta\theta=0$. The lower bound follows from $\Delta_d\ge0$. $\square$

The checks (b) confirm the algebra: $\theta\circ I$ is symmetric, trace-free and $I$-Hermitian, while
$\theta\circ J$ and $\theta\circ K$ are $I$-anti-Hermitian and pointwise orthogonal to it. Also
$|\theta\circ I|^2=2|\theta|^2$ and $|\operatorname{Ric}^\circ|^2=2|\rho_0|^2$.

**Consequence on the degenerating KE fibres $g_t$.** The harmonic representative $\theta_t$ of the primitive
class $\delta^{1,1}_t$ concentrates on the neck, by §3.2. So $H_{\theta_t}$ is, to relative accuracy $o(1)$,
Ozuch's cut-off obstruction element $\tilde o_I=\chi\,\theta_{EH}\circ I$, and it is an **exact** eigentensor
with eigenvalue $-2E$.

In Ozuch's core units ($\tilde g=a^{-2}g$) this eigenvalue becomes $-2Ea^2\to0$, which is why $\tilde o_I$
appears as an approximate kernel element. In global units it is uniformly nonzero. The remaining 3+78
approximate kernel elements behave differently: the two anti-Hermitian EH modes ($\zeta_c$) together with the
78 exterior KS modes form exactly the 80-dimensional KS kernel on $g_t$, which is integrable. So there is
**no small nonzero TT eigenvalue coming from the degeneration**: every approximate kernel element is either
an exact integrable kernel element or an exact eigenmode with eigenvalue $-2E$.

That no other small eigenvalues exist is the standard spectral-convergence statement for orbifold
degenerations. It is cited, not reproved.

This is the linear content of "$A\neq0$": the normal derivative of the reduced obstruction at the Kähler
sheet is the Rayleigh quotient of an exact eigenmode, so no estimate of a remainder is needed at the sheet.
Uniform control away from the sheet is supplied by §3.

## 3. Exact nonlinear secant along the CSCK family

### 3.1 Cohomological identities (checks (c))

Take a Kähler class $[\omega]=\lambda(2\pi c_1/E+\varepsilon\theta)$ on a smooth fibre, or on a resolution in
Theorem C. Here $\theta=\delta^{1,1}$ is the (1,1)-projection of the vanishing class; it satisfies
$c_1\cdot\theta=0$ and $\theta\cdot\delta=\theta^2\to-2$. For a CSCK metric in this class, rescaled so that $s\equiv4E$:

- $\bar s=8\pi\,c_1\cdot[\omega]/[\omega]^2$ fixes $\lambda=4\pi^2c_1^2/(4\pi^2c_1^2+E^2\varepsilon^2\theta^2)$.
- $\rho_0=\rho-E\omega$ is closed and primitive (1,1), hence ASD and harmonic. Its class is $[\rho_0]=2\pi c_1-E[\omega]$; primitivity residual $=0$.
- **Exact defect:** $\operatorname{Ric}-Eg=\operatorname{Ric}^\circ=\rho_0(\cdot,J\cdot)$, and
  $$P=\int|\operatorname{Ric}^\circ|^2=2\|\rho_0\|^2=-2\,(2\pi c_1-E[\omega])^2 .$$
- With $\zeta_r:=\int_\delta\omega=\lambda\varepsilon\theta^2$:
  $$\frac{P}{E^2\zeta_r^2}=-\frac{2}{\theta^2}-\frac{E^2\varepsilon^2}{2\pi^2c_1^2}\ \longrightarrow\ 1 .$$
- **Period of the defect:** $\int_\delta\rho_0=-E\zeta_r$, exactly, since $c_1\cdot\delta=0$.

The CSCK Einstein tensor vanishes identically when $\zeta_r=0$, because the CSCK metric in the KE class is
the KE metric. Its size is fixed by topology.

### 3.2 Concentration of $\rho_0$ on the neck (checks (a))

**Eguchi–Hanson normalization.** On $EH_a$ with Euler $\sigma$'s, set $\theta_{EH}=d(c\,r^{-2}\sigma_3)$. It is
closed for every $V(r)$, the frame coefficients cancel $V$, and it is (anti)self-dual of the type opposite to
the hyperkähler forms. Its pointwise norm is $|\theta_{EH}|=2\sqrt2\,a^2/(\pi r^4)$ when $\int_S\theta_{EH}=-2$.
Then $\|\theta_{EH}\|_{L^2}^2=2=|S\cdot S|$, so $\int\theta_{EH}\wedge\theta_{EH}=S\cdot S$, and it is the
$L^2$ Poincaré dual of the bolt. (A first attempt with mismatched $\sigma$-normalizations gave decay $r^{-6}$
and norm 1; the corrected computation has degree $-4$ decay, as Step 85 B1 and Ozuch require.)

**Lemma 87.3 ($L^2$ concentration, proved).** Write $[\rho_0]=\tfrac{E\zeta_r}{2}\,\delta+y$, where $y$ pairs
with exterior classes at size $O(|\zeta_r|(|\delta^{2,0}|+\varepsilon))$ and $|\delta^{2,0}|=O(|\zeta_c|)$.
Let $\theta_{EH}^{\rm cut}=\theta_{EH}-d(\chi\beta)$, where $\theta_{EH}=d\beta$ outside the bolt,
$\beta\sim a^2r^{-3}$, and the cutoff sits at radius $R$. This is a closed compactly supported representative
of $PD(\delta)$ with $\|\theta^{\rm cut}_{EH}\|^2=2+O((a/R)^4)$.

Since $\rho_0$ is the harmonic, hence $L^2$-minimizing, representative of its class:
$$\Big\|\rho_0-\tfrac{E\zeta_r}{2}\theta^{\rm cut}_{EH}\Big\|_{L^2}\le |E\zeta_r|\,O((a/R)^2)+O(\|y\|).$$
This uses $\|\alpha\|^2\ge|\int\alpha\wedge\alpha|$ for closed $\alpha$ and the Pythagorean identity for exact
differences. So all but a relative $o(1)$ of the $L^2$ mass of the Einstein defect lies in the single
direction $\tilde o_I$.

### 3.3 The calibrated obstruction

With $\hat o_I=\tilde o_I/\|\tilde o_I\|$ and $\Lambda_I(g)=\langle\operatorname{Ric}-Eg,\hat o_I\rangle$:
$$\Lambda_I(g^{\rm CSCK}_{v,\zeta_c,\zeta_r})=\tfrac{E\zeta_r}{2}\,\|\theta_{EH}\circ I\|\,(1+o(1))=E\,\zeta_r\,(1+o(1)),\qquad
P(g^{\rm CSCK})=\Lambda_I^2(1+o(1)).$$
So, in the normalization $\zeta_r=\int_\delta\omega$, $|\omega|^2=2$, with an $L^2$-unit obstruction:
$$\boxed{A=E=s/4,\quad c_0=1.}$$
This agrees with Ozuch's leading term $R^+(p)\zeta$ with $R^+(p)=(s/4)\,\hat\omega\otimes\hat\omega$ at a KE
point, which vanishes on the complex-period plane $I^\perp$. The anti-Hermitian obstructions satisfy
$\Lambda_J=\Lambda_K=o(|\zeta_r|)$ along the family, because the CSCK defect is $J$-Hermitian.

## 4. From the calibration to rigidity

**Inputs.** Each is a statement about published constructions; none is a new mechanism.

- **(O1) Ozuch reduction** [Ozu19a,b], as used in \cite{ozuch2020higher,ozuch2021integrability}. Every
  Einstein metric sufficiently close to $(V,g_V)$ with one EH bubble is, after a diffeomorphism, the unique
  Einstein-modulo-obstruction metric $g_{v,\zeta}$ in the $C^{2,\alpha}_{\beta,*}$-ball about $g^D_{v,\zeta}$.
  The parameters are $v\in$ orbifold kernel ($\mathbb R^{78}$) and $\zeta\in\Lambda^+_p/\pm$ ($\mathbb R^3$).
  The complementary inverse is uniform. *Cited, not yet read in the original.*
- **(BR-u) Uniform CSCK family** \cite{biquardsmoothing}. For A1 the only wall is $\{0\}$, so
  non-degeneracy (Def. 2) holds for every direction $\dot\zeta\in S^2$, including the resolution directions
  $\zeta_c=0$ (Theorem C). The CSCK metrics exist with constants uniform over the compact sphere of
  directions and over $v$, and depend continuously on $(v,\zeta)$. Corollary 35 gives
  $\|\phi_t\|_{C^{4,\alpha}_{\delta+2}}\le C\varepsilon^{2-\beta(\delta+2)}$ for each fixed ray; uniformity
  over rays is the claim to be checked in the proof.
- **(M) Matching.** In Bianchi gauge with respect to $g^D_{\iota(p)}$, the CSCK metric lies in Ozuch's
  uniqueness ball, and its Ozuch parameter after the EmO correction differs from the natural
  identification $\iota(p)$ by $\le\eta|\zeta|$ in $\zeta$ and $\le\eta$ in $v$, with $\eta<1/2$. This is a
  $C^0$ statement; BR's pointwise closeness $O(\varepsilon^{(1-\beta)(\delta+2)})$ (proof of Lemma 33) is the
  relevant input.
- **(Hp-w) Weighted form of Lemma 87.3.**
  $\|(\operatorname{Ric}-Eg)^{\perp}\|_{C^{\alpha}_{\beta}}\le o(1)\,|\zeta_r|$ in Ozuch's source norm. Here
  $\perp$ means orthogonal to the approximate cokernel, normalized so that $\langle\cdot,\hat o_I\rangle$ has
  size $|E\zeta_r|$.
  *Sketch:* in EH units the orthogonal part is $a^2b^{-2}$ against $\Psi\sim b^{-4}$, giving weighted relative
  size $O(a^{2-\beta})$; in the exterior it is $O(a^2)$. Writing this in Ozuch's norms, including the
  $H_k$ part of Def. A.4, remains to be done.

**Theorem 87.4 (conditional on O1, BR-u, M, Hp-w).** Let $X_0$ be a generic one-node quintic with orbifold
KE metric $g_V$ ($\operatorname{Ric}=-g$), and let $M$ be the smooth quintic four-manifold. There is a
Gromov–Hausdorff neighbourhood $\mathcal U$ of $(V,g_V)$ such that every Einstein metric on $M$ with
$\operatorname{Ric}=-g$ lying in $\mathcal U$ is Kähler–Einstein for some smooth quintic complex structure.

*Proof.*
(1) **Degeneration type** (Lemma 87.5). Any such metric lies in Ozuch's family with one orientation-matched EH bubble; then (O1) applies.
(2) **Corrected CSCK metrics.** Let $\Xi(p)=g^{\rm CSCK}_p+k_p$ be the EmO correction. Its source is
$\Phi(g^{\rm CSCK}_p)=\zeta_r\Psi_p$ with $\Psi_p=E\hat o_I+o(1)$ (§3, Hp-w), so
$\|k_p\|\le C|\zeta_r|\,o(1)$ by the uniform inverse. Hence
$\Lambda_I(\Xi(p))=E\zeta_r(1+o(1))+O(\|k_p\|\,\|L^*\hat o_I\|+\|k_p\|^2)=E\zeta_r(1+o(1))$.
When $\zeta_r=0$, $k_p=0$ and $\Xi(p)$ is the KE metric.
(3) **Coverage.** By (M), $\pi\circ\Xi$ is a continuous map of the conical parameter region with relative
displacement $<1/2$. For any target $(v^*,\zeta^*)$, $\zeta^*\neq0$, the straight-line homotopy to $\iota$ on
the shell $\{|v-v^*|\le2\eta,\ |\zeta^*|/2\le|\zeta|\le2|\zeta^*|\}$ avoids the target, so the degree is 1 and
$(v^*,\zeta^*)$ is hit.
(4) **Conclusion.** An Einstein $g\in\mathcal U$ is $g_{v^*,\zeta^*}$ with $\Lambda(g)=0$. By (3),
$g_{v^*,\zeta^*}=\Xi(p)$ for some $p$, using uniqueness in (O1). By (2), $0=\Lambda_I=E\zeta_r(1+o(1))$
forces $\zeta_r=0$, so $g=\Xi(p)$ is the KE metric of the fibre with parameter $(v,\zeta_c)$. Exterior
centers are covered by Lemma 87.1. $\square$

Neither $\partial_\zeta\Lambda$ nor a $C^1$ extension on the real blow-up is used. The only derivative-type
information is the uniform inverse already contained in (O1). Injectivity of $\Xi$ is not needed.

**Lemma 87.5 (bubble type, proved from standard inputs).** Let $g_n$ be Einstein on $M$ with
$\operatorname{Ric}=-g_n$, converging in GH to $(V,g_V)$. Then the convergence is noncollapsed (volume
continuity under a lower Ricci bound) and of orbifold type (Anderson, Bando–Kasue–Nakajima). There is exactly
one bubble, at $p$; it is Eguchi–Hanson, orientation-matched, with no tree.

*Proof.*
- At smooth points of $V$, a bubble is Ricci-flat ALE with trivial group at infinity, hence flat by Bishop–Gromov.
- An intermediate orbifold bubble with group $\mathbb Z_2$ at infinity and an orbifold point of group $\Gamma'$
  satisfies $1/|\Gamma'|\ge1/2$ by Bishop–Gromov, with equality only if it is flat. Hence it has no orbifold
  points, and there are no trees.
- The single bubble $N$ has $\chi(N)=\chi(M)-\chi_{\rm top}(V)+1=2$, $b_2=1$, $\tau=-1$ in the orientation of
  $M$. It is Ricci-flat ALE with end $\mathbb R^4/\{\pm1\}$, the same group embedding as EH.
- Gauss–Bonnet and signature with identical boundary terms then give
  $\int_N|W^+|^2=\int_{EH}|W^+|^2=0$.
- Ricci-flat with $W^+=0$ makes $\Lambda^+$ flat. Since $|\pi_1(N)|\cdot\tfrac12\le1$ (Euclidean volume growth
  of the universal cover), with equality only for flat $\mathbb R^4/\pm1$, which is not a manifold, $\pi_1(N)=1$.
- So $N$ is hyperkähler, and by Kronheimer it is EH. $\square$

## 5. Consequences for Goldberg and the Einstein-gap programme

**Corollary 87.6 (conditional as in 87.4).** No strict almost-Kähler Einstein metric, and indeed no
non-Kähler Einstein metric, on the quintic manifold lies in $\mathcal U$.

*Proof.* Let $g\in\mathcal U$ be Einstein and AKE with $\omega$. By 87.4, $g$ is KE for some $J'$. By
Prop. 85.1, $H^+_g=\mathbb R\omega_{J'}\oplus\operatorname{Re}H^{2,0}_{J'}$, and a constant-length element
equals $\pm\omega_{J'}$ (otherwise $|\beta|$ would be a nonzero constant, trivializing $K$). So $g$ is Kähler. $\square$

On this route, the Step-85 second-order center theorem and the neck-trace theorem are no longer
load-bearing. Classifying all nearby Einstein metrics is stronger than classifying nearby AKE metrics, and
the length obstruction of Prop. 85.1 then finishes. The Step-85 results remain valid independent statements.

**Relation to $D_W$.** For every $g\in\mathcal U$, $D_W(g)=0$. A positive Weyl deficit, which Q1 needs and
which strict AKE would require, cannot be realized by Einstein metrics GH-near a negative-KE A1 endpoint of
this kind.

The CSCK identity $P=-2(2\pi c_1-E[\omega])^2$ shows that the non-Einstein comparison metrics carry Einstein
defect $P\approx E^2\zeta_r^2$, which is quadratic and topological. This is the same competition as in the
organizing identity $8\pi^2k-P=4D_W-(S-32\pi^2A)/4$, now realized on one concrete family.

## 6. What transfers, what does not

The mechanism uses four ingredients:
- (a) an actual Kähler comparison family whose Einstein defect is the harmonic ASD representative of a class linear in $\zeta_r$;
- (b) global realization of every local period direction: locally trivial unobstructed, with $T^1_{\rm glob}\to\oplus_xT^1_x$ surjective;
- (c) Ozuch reduction with a uniform inverse;
- (d) $C^0$ matching.

**Transfers formally to:**
- any canonically polarized surface with any number of $A_1$ nodes, no defect, and no vector fields. Here
  $\Lambda_{I,x}=E(\zeta_r)_x+o(|\zeta_r|)$, since the harmonic duals of distinct $\delta_x$ concentrate at
  distinct nodes;
- nodal KE del Pezzo surfaces with discrete automorphisms ($E>0$; Spotti's setting), with the opposite sign.
  For $E>0$ the Hermitian gap of §2 becomes $\Delta_d-2E$, which is not nonnegative, so §2 changes but §3 does not;
- ADE points with the Cartan form: $\Lambda_I=E\,C\zeta_r$ in $\mathfrak h_{\mathbb R}$, with $C$ invertible.

**Does not transfer as stated:**
1. **Several nodes at different scales.** BR take one ray. Uniformity over all ratios of node scales is not established.
2. **$A_k$ ($k\ge2$), $D$, $E$.** The walls $D_\theta$ are nontrivial. Directions near walls produce orbifold
   bubble trees, where (O1) and (BR-u) are not uniform.
3. **Failure of full local-period coverage or obstructed locally trivial deformations.** Kloosterman's defect measures dependence of the node conditions and can obstruct equisingular deformation theory; it does not mean that a nodal hypersurface has no smoothing. A generic polynomial deformation can still smooth the nodes and, for degree at least five, yields canonically polarized KE fibres. What can fail is independent realization of every prescribed local smoothing direction, or integration of every locally trivial tangent. The CSCK comparison therefore need not cover the full Einstein parameter space. The remaining anti-Hermitian equations are worth investigating, but neither missing comparison coverage nor a complex-deformation obstruction establishes an additional Einstein root. The period calibration along controlled CSCK directions retains the qualifications in §9.
4. **Collapse, cusps, diameter divergence, and positive-deficit Einstein components** away from KE endpoints.
   Nothing here addresses them.

## 7. Neck flux with Ozuch's constant tensors (Spirit #110)

In Def. A.4, $h=h_*+\sum_k\chi_{A_k}H_k$ with constant trace-free $H_k$. On the annulus, $g_e+H_k$ is again
flat, so the Step-85 flux law should be applied in the linear frame adapted to $g_e+H_k$. Only $h_*$ and the
model errors $r^2+a^4r^{-4}$ enter the moving-neck error integral. The transition regions of $\chi_{A_k}$
contribute $O(|H_k|)$, with no $\log(1/a)$ factor. Integrating $|H_k|$ along the whole neck would wrongly
require $|H_k|\log(1/a)\to0$.

This repairs hypothesis (H) of Step 85 §8. It is no longer needed for Theorem 87.4.

## 8. Remaining work

- Read [Ozu19a,b] for the exact form of (O1): the neighbourhood, the uniqueness ball and the uniform inverse.
- Prove (BR-u) and (M) by tracking BR §§3–4 with constants uniform over $\dot\zeta\in S^2$, including Theorem C directions.
- Write (Hp-w) in $C^\alpha_{\beta}$ with the $H_k$ part.
- Examine the actual anti-Hermitian reduced equations when local-period coverage or locally trivial integrability fails (§6.3); do not infer an Einstein construction from that failure alone.
- Keep the unrestricted problems open: Q1 existence on $X\#k\overline{\mathbb{CP}}^2$ (the full mixed bound
  $D_W\ge4\pi^2k+(8\pi^2A/9)(1-\sqrt{1-3k/A})^2$), the Q2 optimal tariff, Q3 smooth global attainment, and
  closed Goldberg away from KE endpoints.


## 9. Independent verification and the repaired status (TTCS `trace/ttcs/results/step87_ttcs01_verifier1_integration.md`, branches `step87_ttcs01_sub{1,2}_verifier.md`)

This section takes precedence over §§2–5 wherever the two disagree.

**Confirmed.**
- The CSCK identities ($\lambda$, primitivity, $P=-2[2\pi c_1-E[\omega]]^2$, $\zeta_r=\lambda\varepsilon T$, $\int_\delta\rho_0=-E\zeta_r$, the ratio formula) are correct. Here $c_1=c_1(T^{1,0})$.
- Writing $\delta=\theta+\eta$ with $\eta=\delta^{2,0}+\delta^{0,2}$ gives $T=\theta^2=-2-\eta^2\le-2$, and $T\to-2$ when the global holomorphic periods of $\delta$ tend to $0$.
- At $\zeta_r=0$ we have $[\rho_0]=0$, so harmonicity alone gives $\rho_0=0$; no separate CSCK-uniqueness argument is needed.
- EH normalization: the magnitude, period and $\|\theta_{EH}\|^2=2$ are correct. The form is SD for the frame order $e^{0123}$ and ASD for the hyperkähler/complex orientation, in which $\int\theta\wedge\theta=-2=S^2$.
- Prop. 87.2 is correct. Its multiplicity is **exactly** $h^{1,1}-1=44$ in the Hermitian TT sector. For Ozuch's operator $P=\tfrac12\Delta_E$ the eigenvalue is $-E$.
- The count $78+2=80$ is correct. In §2, "remaining 3+78" should read "remaining 2+78".

**Corrections.**
1. *Exact kernel versus cutoff.* The cut-off tensors $o_J,o_K$ are not exact global kernel tensors. The correct statement: the globally corrected smoothing tangents are exact Kodaira–Spencer kernel tensors and approximate the local EH pair. Likewise $H_{\theta_t}$ is exact, while the cut-off $\tilde o_I$ only approximates it.
2. *"No small nonzero TT eigenvalue."* This does not follow from Prop. 87.2. The Hermitian sector is uniformly $\ge-2E$, but the gap above the anti-Hermitian kernel requires a separate spectral-gluing or complement estimate. This is now listed as input **(S)**.
3. *Lemma 87.3.* The mechanism is right, and the proof is repaired as follows. For any closed $\alpha$ in the class of $\rho_0$,
$$\|\alpha-\rho_0\|_{L^2}^2=2\|\alpha^+\|_{L^2}^2$$
by Pythagoras together with $\|\rho_0\|^2=-[\rho_0]^2=-\int\alpha\wedge\alpha$. Take $\alpha=d\,\theta^{\rm cut}_{EH}+\gamma_y$, where $d=E\zeta_r/2$ and $y\cdot\delta=0$ exactly. This needs two further inputs: comparison of the actual CSCK Hodge star with the EH one on the core and neck, and a bounded exterior representative $\gamma_y$ with $\|\gamma_y\|\le C|y|$ under uniform exterior convergence. The lemma is therefore "proved modulo uniform metric comparison", not unconditional.
4. *Calibration.* $A=E$ (so $c_0=1$) holds in the **period coordinate $\zeta_r=\int_\delta\omega$ with an $L^2$-unit test tensor**. Converting to Ozuch's raw metric parameters $\zeta$ and his gauge-fixed reduced coefficient has not been done. The statement "normal derivative equals the Rayleigh quotient" carries the factor $\tfrac12$ and this conversion.
5. *Theorem 87.4.* Uniqueness may only be invoked inside **one** fixed reduction. The repaired architecture is:
   - (i) *Modulation.* For each CSCK parameter $p$, find $q=m(p)$ and a diffeomorphism $\phi_p$ such that $\bar g_p=\phi_p^*g^{\rm CSCK}_p$ lies in Ozuch's gauge and satisfies $\bar g_p-g^D_q\perp\tilde O_q$. Solvability must be checked in scale-adapted coordinates.
   - (ii) *Graph comparison.* Let $G(q)$ be Ozuch's unique EmO graph. Show $\|G(m(p))-\bar g_p\|_{C^{2,\alpha}_{\beta,*}}\le C\|\Pi^\perp_{m(p)}\Phi(\bar g_p)\|_{r_D^{-2}C^\alpha_\beta}=o(|\zeta_r|)$.
   - (iii) *Pairing stability.* Show $\ell_{m(p)}(\Phi(G(m(p))))=E\zeta_r+o(|\zeta_r|)$, controlling linear, quadratic, gauge and test-tensor variation in these norms.
   - (iv) *Degree.* Show the relative matching $|m_\zeta-\zeta|\le\eta|\zeta|$, $|m_v-v|\le\eta$, $\eta<\tfrac12$. Then apply degree with a marked lift, mod-2 degree, or a small ball around $\zeta^*$ avoiding $0$ and $-\zeta^*$, since $(\mathbb R^3\setminus0)/\pm$ is nonorientable. Hitting $q$ identifies the metric only through the graph $G$.
   
   The argument is not circular, provided (i)–(iii) are not justified by the rigidity they are meant to prove.
6. *(Hp-w)* must be written in Ozuch's source norm $r_D^{-2}C^\alpha_\beta$. The constant tensors $H_k$ of Def. A.4 belong to the **domain** norm and are handled by the gauge and the inverse. BR's crude relative estimate $O(a^{(1-\beta)(\delta+2)})$ does not by itself give the rate $a^{2-\beta}$ in the sketch; a weaker positive power may suffice after norm conversion. The live unknown is a uniform weighted comparison of the normalized harmonic defect with the fixed obstruction line, including the regime $|\zeta_r|\ll|\zeta|$. Useful BR tools: Lemma 22, Corollary 23, Proposition 29.
7. *(BR-u)* BR Theorems B and C are raywise. The hypotheses are more than "the wall is $\{0\}$": Definition 2 also requires the order condition $p\le\mathbf d$ and an admissible family of (1,1)/Kähler classes. The negative real direction requires the Weyl-related marking: one simultaneous-resolution chart does not carry both signs of $\zeta_r$ as Kähler classes, so charts must be patched. Uniformity in $v$ requires **recentering at $g_v$**; measuring against $g_V$ would wrongly force $|v|=O(a^2)$. BR's pointwise closeness does not by itself give $m_\zeta-\zeta=o(|\zeta|)$; core rescaling, marking and slice control are needed.
8. *Lemma 87.5.* The proof is sound with the following points made explicit:
   - Bubble-tree compactness, with the energy bound from Einstein Gauss–Bonnet.
   - Bishop–Gromov excludes nonflat intermediate levels; flat ghost levels are suppressed separately.
   - $\eta(\mathbb{RP}^3)=0$, so $A_++A_-=12\pi^2$ and $A_+-A_-=-12\pi^2$, hence $A_+=0$. Orientation matching therefore follows from topology.
   - $|\pi_1(N)|=d<\infty$; the universal cover has asymptotic volume ratio $d/2\le1$; if $d=2$ the cover is Euclidean, and a nontrivial finite group cannot act freely on it. So $d=1$. This replaces the phrase "flat $\mathbb R^4/\pm1$".
9. *Corollary 87.6, orientation.* The $H^+$ argument covers AK forms that are SD in the complex orientation. **Repair for the reversed orientation (added here):** suppose an Einstein KE metric $g$ admits an AK structure for $\bar M$. By Thm 83.2(b), the reversed-orientation deficit is
$$D'=\int\Big(\frac{s^2}{24}-|W^-|^2\Big)=\frac{\widehat S^2}{16}-2\pi^2(2\chi-3\tau).$$
For KE metrics $\widehat S^2/16=2\pi^2(2\chi+3\tau)$, so $D'=12\pi^2\tau$. For the quintic $\tau=-35$, so $D'=-420\pi^2<0$, which contradicts $D'=T'_{\rm AK}\ge0$. Hence a KE quintic metric admits no oppositely oriented AK structure. In the complex orientation its Kähler forms $\pm\omega_J$ remain allowed; the constant-length harmonic-form argument excludes strict AK structures there. Thus, conditional on Theorem 87.4, the Einstein neighbourhood contains no strict AKE metric in either orientation—not no AK structures. Spirit checked this orientation calculation directly after the Step; it does not discharge any analytic hypothesis of Theorem 87.4.
10. "$D_W=0$ on $\mathcal U$" applies to **Einstein** metrics in $\mathcal U$.

**Status after verification.**
- *Established:* the CSCK/Chern–Weil identities; the EH normalization; Prop. 87.2 (exact multiplicity 44 in the Hermitian sector); the 39+1 and 78+2 counts; Lemma 87.1 (modulo the orbifold adaptation of Nagy/Koiso); Lemma 87.5 (with the stated standard compactness and ALE inputs); the reversed-orientation exclusion for KE metrics with $\tau<0$.
- *Conditional:* the relative CSCK calibration over the full direction family; Lemma 87.3 (uniform metric comparison); (S); (Hp-w); modulation and relative matching; (O1); and therefore Theorem 87.4 and Corollary 87.6.
- *Withdrawn as literal statements:* cut-off modes as exact kernel tensors; parameter matching from pointwise closeness; uniqueness across different reductions; an orientation-free $H^+$ argument.

**What is genuinely new here:** replacing the Step-85/86 scale-uniform derivative target by the **CSCK secant plus a $C^0$ finite-dimensional degree argument**, together with the identification of the remaining analytic content. That content is a uniform, gauge-compatible weighted modulation comparison between the BR CSCK family and one fixed Ozuch reduction. The eigenvalue and Chern–Weil identities are standard. BR construct the comparison metrics raywise.

## 10. Spirit boundary clarification: normalize the residual before estimating it

The very small normal-displacement regime can be formulated without subtracting two nearly equal curvature tensors. With the notation of §3.1, put $C=c_1^2$ and $T=\theta^2$. For $\zeta_r\ne0$, direct substitution of $\lambda$ and $\zeta_r=\lambda\varepsilon T$ gives the exact cohomological identity
$$\frac{[\rho_0]}{\zeta_r}=-\frac{E}{T}\theta+\frac{E^2\varepsilon}{2\pi C}c_1.$$
For fixed nonzero complex smoothing parameter, this class extends across $\varepsilon=0$. Its harmonic representative for the actual CSCK metric equals $\rho_0/\zeta_r$ away from zero; at the KE sheet it is $-E\theta_{\rm harm}/T$. Thus the estimate relative to $|\zeta_r|$ can be sought as a uniform weighted estimate on a normalized harmonic form, including arbitrarily small $|\zeta_r|/|\zeta|$. In a controlled nodal limit $T\to-2$, its expected core limit is $(E/2)\theta_{EH}$.

This algebra is exact; uniform convergence of these harmonic representatives in Ozuch's source norm, their identification with the fixed obstruction bundle, gauge modulation, and pairing stability remain unproved. Neither the cohomological formula nor the existing $L^2$ estimate supplies them. The continuation should exploit the harmonic equation and this regular normalized class rather than regard a numerical recovery of $P\sim E^2\zeta_r^2$ as a test of the missing global comparison. The source-scope and orientation corrections above were made by Spirit at the Step-87 boundary.
