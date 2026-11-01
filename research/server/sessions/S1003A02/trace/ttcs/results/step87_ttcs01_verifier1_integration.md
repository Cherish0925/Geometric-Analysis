# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 87,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical correctness and exact scope of Lemma 86.S and Lemma 86.S′ in theorem_package_v1.md. Focus on the cutoff scaling rho=epsilon^{tau/(tau+2)}, C^2 annular curvature and integral estimates, iteration for ALE trees, continuity of the Einstein defect, whether scalar variance is automatically controlled, and the Ricci-flat bulk case. For Wahl/T singularities, read Suvaina's primary source and determine whether the Milnor-fibre metrics have the derivative-controlled order-4 ALE asymptotics required. For Lemma 86.S′, decide the minimal hypotheses under which the displayed defect ledger follows, identify any missing denominator case or interaction term, and distinguish standard cutoff-glued families from arbitrary degenerating sequences. Give exact corrected statements/proofs where needed.

## Integrated Scientific Memo

# Verification memo: Lemmas 86.S and 86.S′

**Verdict.** Lemma 86.S is correct for standard cutoff gluing with derivative-controlled ALE ends. Its scalar-variance conclusion is automatic, but its tree extension needs relative-scale bookkeeping. The Ricci-flat bulk requires a separate argument: these cutoff metrics have \(\mathscr D\to4\), not \(0\).

Lemma 86.S′ has the correct scalar-flat bubble ledger **when its limiting denominator is positive**. It needs a zero-denominator clause and a qualification of the claimed strict movement toward \(4\). No interaction survives in the stated limit, but finite-scale strict improvement requires information beyond this lemma.

Şuvaina’s primary source supplies the necessary Milnor-fibre metrics. Although Definition 1.1 explicitly records only order-four metric and complex-structure decay, her finite-centre Gibbons–Hawking construction yields order-four decay with derivatives in a centred, equivariant end chart.

## 1. Cutoff estimates and corrected Lemma 86.S

Use the notation
\[
V(g)=\operatorname{Vol}(g),\quad S(g)=\int s_g,\quad
H(g)=\int s_g^2,\quad R(g)=\int|\operatorname{Ric}_g|^2.
\]
In dimension four,
\[
R=P+\frac14H,\qquad L_s=H-\frac{S^2}{V},
\]
and, for \(R>0\),
\[
\mathscr D(g)=4-\frac{S^2}{VR}=\frac{4P+L_s}{R}.
\]
At \(R=0\), the original definition gives \(\mathscr D=4\).

### Local calculation

In an orbifold normal chart, lifted to its uniformizing cover,
\[
g=\delta+q,\qquad |\partial^\ell q|\le Cr^{2-\ell},
\quad 0\le\ell\le2.
\]
Require a matching ALE end chart with
\[
h=\delta+t,\qquad
|\partial^\ell t|\le Cr^{-\tau-\ell},
\quad 0\le\ell\le2,\quad \tau>0.
\]
“Matching” means a chosen orientation-preserving, equivariant cone identification, not just an abstract isomorphism of groups or links.

After scaling by \(\varepsilon^2\), the metric components in physical coordinates \(y=\varepsilon x\) are \(h(y/\varepsilon)\). On \(r\asymp\rho\), a smooth radial cutoff therefore gives
\[
\sum_{\ell=0}^2\rho^\ell
|\partial^\ell(g_{\varepsilon,\rho}-\delta)|
\le C\eta,\qquad
\eta=\rho^2+(\varepsilon/\rho)^\tau.
\]
For small \(\eta\), inverse metrics are uniformly bounded and the curvature formula yields
\[
|\operatorname{Rm}_{g_{\varepsilon,\rho}}|
\le C\rho^{-2}(\eta+\eta^2)
\le C\rho^{-2}\eta.
\]
Consequently,
\[
\int_{\mathrm{ann}}|\operatorname{Ric}|^2+
\int_{\mathrm{ann}}s^2
\le C\big[\rho^4+(\varepsilon/\rho)^{2\tau}\big].
\tag{1}
\]
This estimate includes cutoff derivatives and their cross terms.

Balancing the two metric errors gives
\[
\rho^2=(\varepsilon/\rho)^\tau,\qquad
\boxed{\rho=\varepsilon^{\tau/(\tau+2)}}.
\]
Then \(\rho\to0\), \(\rho/\varepsilon\to\infty\), and annular curvature is \(O(1)\). The annular volume and the integrals in (1) are \(O(\rho^4)\); also
\[
\int_{\mathrm{ann}}|s|=O(\rho^4).
\]

The truncated filler has volume
\[
\varepsilon^4\operatorname{Vol}_h\{r<\rho/\varepsilon\}
=O(\rho^4),
\]
by ALE volume growth. If it is Ricci-flat, its \(R,S,H,P\) contributions vanish. The removed bulk ball has bounded curvature and contributes \(O(\rho^4)\).

Thus, for finitely many insertions, with
\[
E=\sum_j\rho_j^4,
\]
one obtains
\[
\begin{aligned}
V(g_\varepsilon)&=V(g)+O(E),&
S(g_\varepsilon)&=S(g)+O(E),\\
H(g_\varepsilon)&=H(g)+O(E),&
R(g_\varepsilon)&=R(g)+O(E),\\
P(g_\varepsilon)&=P(g)+O(E),&
L_s(g_\varepsilon)&=L_s(g)+O(E).
\end{aligned}
\tag{2}
\]
In particular, control of \(L_s\) uses the **scalar-square estimate**, not merely convergence of \(V,S,R\).

### Exact corrected statement

> **Lemma 86.S.** Let \((V,g)\) be a compact oriented four-orbifold, smooth in orbifold charts, with finitely many isolated singularities whose local groups act freely on \(S^3\). At each singularity choose a Ricci-flat ALE filler with an orientation-matched equivariant end identification and
> \[
> |\partial^\ell(h_j-\delta)|\le C_jr^{-\tau_j-\ell},
> \qquad 0\le\ell\le2,\quad \tau_j>0.
> \]
> Standard cutoff gluing of \(\varepsilon_j^2h_j\) at
> \(\rho_j=\varepsilon_j^{\tau_j/(\tau_j+2)}\) gives (2).
> If \(R(g)>0\), then
> \[
> \mathscr D(g_\varepsilon)=\mathscr D(g)+O(E).
> \]
> If \(g\) is Einstein with constant \(\Lambda\ne0\), then
> \[
> P(g_\varepsilon)+L_s(g_\varepsilon)=O(E),
> \qquad \mathscr D(g_\varepsilon)=O(E).
> \]

The last conclusion also follows directly by testing the defining infimum at \(\lambda=\Lambda\). On the exactly Ricci-flat core,
\[
|\operatorname{Ric}-\Lambda g_\varepsilon|^2=4\Lambda^2,
\]
but that core has volume \(O(E)\); the annulus has bounded residual, and the exterior residual is zero. The denominator tends to \(\Lambda^2V(g)>0\).

Hence the scalar-variance proviso is unnecessary **for these constructed families over a nonzero-scale Einstein bulk**. This does not establish automatic variance control for arbitrary sequences with \(P\to0\), or the finer condition \(L_s=o(a^4)\) needed for a sharp \(a^4\) defect coefficient on corrected metrics.

Balancing gives the advertised upper rate, not a general optimality theorem. A universal lower bound for arbitrary cutoffs, gauges, or corrected metrics does not follow from (1). In Step 56.U, \(\rho=\lambda^{1/2}\) correctly gives \(O(\lambda^2)\); for order four, the balanced choice improves this elementary bound to \(O(\lambda^{8/3})\).

## 2. Finite ALE trees: relative scales matter

Let an ALE orbifold parent, in its own units, have an inner insertion at relative scale \(\delta\), with cutoff radius
\[
\sigma=\delta^{\tau/(\tau+2)}.
\]
Its inner annular \(R,H,P\) errors are \(O(\sigma^4)\). If the parent is then scaled by \(a^2\), these energies remain \(O(\sigma^4)\): they are scale invariant in dimension four. By contrast, the scalar integral and volume errors become respectively
\[
O(a^2\sigma^4),\qquad O(a^4\sigma^4).
\]

Therefore a fixed relative inner transition does **not** become energetically negligible just because its physical radius tends to zero. A valid finite-tree extension requires every relative inner smoothing parameter to tend to zero, with disjoint, compatible gluing regions. For fixed finite trees, an adequate total error is
\[
E_{\mathrm{tree}}
=\sum_{\text{outer }j}\rho_j^4+
  \sum_{\text{inner }v}\sigma_v^4\longrightarrow0.
\]
All conclusions above then hold with this error. To retain a particular outer \(O(\rho^4)\) rate, choose the inner parameters so that
\(\sum_v\sigma_v^4=O(\rho^4)\).

For varying ALE metrics or moduli, uniform end estimates are additionally necessary. They are not supplied merely by pointwise existence of an ALE chart for each member.

## 3. Ricci-flat bulk: the omitted continuity argument

The formula for \(\mathscr D\) cannot be evaluated continuously at \(R=0\). Nevertheless, the standard cutoff family has a definite limit.

If the bulk and fillers are Ricci-flat, scalar curvature is supported only on shrinking transition regions \(A_\varepsilon\). Whenever \(R(g_\varepsilon)>0\),
\[
S(g_\varepsilon)^2
\le \operatorname{Vol}(A_\varepsilon)H(g_\varepsilon)
\le4\operatorname{Vol}(A_\varepsilon)R(g_\varepsilon).
\]
Thus
\[
0\le4-\mathscr D(g_\varepsilon)
\le \frac{4\operatorname{Vol}(A_\varepsilon)}{V(g_\varepsilon)}
\longrightarrow0.
\]
If \(R(g_\varepsilon)=0\), its defect is already \(4\).

Therefore
\[
\boxed{P(g_\varepsilon)\to0,\qquad \mathscr D(g_\varepsilon)\to4.}
\]
This proves \(P_*=0\), but supplies no \(\alpha=0\) conclusion. It is a property of these localized cutoff families, not a general continuity theorem at Ricci-flat metrics.

## 4. Şuvaina’s primary-source input

The supplied full text establishes:

- **Theorem A:** nearby fibres of a one-parameter \(\mathbb Q\)-Gorenstein smoothing admit ALE Ricci-flat Kähler metrics in every Kähler class.
- **Theorem 2.2:** the singularities are rational double points or
  \[
  \frac1{dn^2}(1,dnm-1),\qquad (m,n)=1.
  \]
- **Section 3 and Proposition 3.3:** cyclic class-\(T\) fibres are free \(\mathbb Z_n\)-quotients of \(A_{dn-1}\) smoothings; \(d=1\) gives the Wahl rational balls.
- **Section 5:** the covering metrics have the finite-centre Gibbons–Hawking description
  \[
  h=V^{-1}\omega^2+V\,dx^2,\qquad
  V(x)=\frac12\sum_{\alpha=1}^{dn}|x-x_\alpha|^{-1}.
  \]
  The centres form \(d\) regular \(n\)-gons in horizontal planes, and the quotient action is isometric and free.

Definition 1.1 explicitly states \(h-h_0=O(r^{-4})\) and \(J-J_0=O(r^{-4})\), **without derivative notation**. The needed derivative statement can, however, be derived from this explicit construction.

Translate the centre set to satisfy \(\sum_\alpha x_\alpha=0\). For these symmetric configurations only an axial translation is needed; it commutes with the quotient action. With \(t=|x|\),
\[
V_0=\frac{dn}{2t},\qquad
\partial^k(V-V_0)=O(t^{-3-k})
\tag{3}
\]
for every fixed \(k\), by the convergent finite-centre multipole expansion. The dipole is absent.

The curvature difference of the circle connections has zero flux at infinity. A radial end gauge supplies a connection correction whose base-coordinate coefficients and derivatives are \(O(t^{-3-k})\); equivalently its angular coefficients are \(O(t^{-2})\). This gauge can be chosen equivariantly. Since the four-dimensional cone radius satisfies \(r^2\asymp t\), both the potential and connection corrections give relative metric error \(O(t^{-2})=O(r^{-4})\). Differentiating the explicit formulas gives
\[
\boxed{|\partial^\ell(h-h_0)|\le C_\ell r^{-4-\ell}}
\]
in the centred cone chart, in particular for \(\ell\le2\). The finite quotient preserves these local estimates and produces the stated asymptotic group.

Thus **Wahl and general cyclic class-\(T\) Milnor-fibre metrics meet Lemma 86.S’s hypothesis with \(\tau=4\)**. The accurate attribution is that derivative control follows from Şuvaina’s construction, not that Definition 1.1 explicitly states it. Without centring, a dipole can give only order two in the chosen chart; that still suffices for continuity but changes the elementary rate.

## 5. Corrected Lemma 86.S′ and its minimal scope

For a finite collection of fixed scalar-flat ALE/AE bubbles, put
\[
Q=\sum_jP(N_j).
\]
Use matching end identifications and derivative-controlled decay through order two. The balanced cutoffs suffice, but are not necessary for the limiting ledger: any choices satisfying
\[
\rho_j\to0,\qquad \varepsilon_j/\rho_j\to0
\]
make the transition energy in (1) tend to zero.

The end estimates imply
\[
|\operatorname{Ric}_h|=O(r^{-2-\tau}),\qquad
\int_{r>T}|\operatorname{Ric}_h|^2=O(T^{-2\tau}).
\]
Thus finite Ricci energy—and hence finite \(P\)—is automatic for a fixed smooth ALE bubble under these hypotheses. Scale invariance and exhaustion of the truncated bubbles give
\[
\begin{aligned}
V(g_\varepsilon)&\to V(g),&
S(g_\varepsilon)&\to S(g),&
H(g_\varepsilon)&\to H(g),\\
P(g_\varepsilon)&\to P(g)+Q,&
R(g_\varepsilon)&\to R(g)+Q,&
L_s(g_\varepsilon)&\to L_s(g).
\end{aligned}
\tag{4}
\]

> **Lemma 86.S′, corrected.** Under these standard cutoff hypotheses, if \(R(g)+Q>0\), then
> \[
> \boxed{
> \mathscr D(g_\varepsilon)\longrightarrow
> \frac{4P(g)+L_s(g)+4Q}{R(g)+Q}
> =4-\frac{S(g)^2}{V(g)[R(g)+Q]}.
> }
> \]
> If \(R(g)+Q=0\), the displayed fraction is undefined. The bulk and all bubbles are then Ricci-flat, and the standard cutoff family instead has \(\mathscr D(g_\varepsilon)\to4\).

At the purely analytic level, the positive-denominator defect limit needs only convergence of \(V,S,R\) to the displayed values. Relations (4) explain its decomposition into \(P\), scalar variance, and bubble contributions.

### Weaker bubble hypotheses

Scalar-flatness is necessary only for writing the bubble term as \(P(N)\). For arbitrary derivative-controlled ALE bubbles, let
\[
Q_R=\sum_jR(N_j),\qquad H_j=\int_{N_j}s^2.
\]
Their volume tends to zero, and their scalar integrals tend to zero by Cauchy–Schwarz on the shrinking inserted regions, using bounded Ricci energy. Hence the corresponding formula is
\[
\mathscr D_\infty
=
\frac{4P(g)+L_s(g)+
\sum_j[4P(N_j)+H_j]}
{R(g)+Q_R}
=
4-\frac{S(g)^2}{V(g)[R(g)+Q_R]}.
\tag{5}
\]
For trees, all vertices must be accounted for and relative transition energies must vanish as in §2.

### Movement toward \(4\) and zero defect

If \(R(g)>0\), the scalar-flat formula becomes
\[
\mathscr D_\infty
=\frac{R(g)\mathscr D(g)+4Q}{R(g)+Q}.
\]
It increases strictly precisely when
\[
Q>0\quad\text{and}\quad S(g)\ne0.
\]
If \(\mathscr D(g)=4\), adding positive-energy bubbles leaves the value \(4\). This corrects “does so exactly when \(P(N)>0\).”

For a fixed bulk and positive limiting denominator, the limiting defect is zero exactly when
\[
P(g)=L_s(g)=Q=0.
\]
The bulk is therefore Einstein with nonzero Einstein constant, and all bubbles are Ricci-flat. This characterizes **zero limits of these glued families**, not all possible zero-infimum mechanisms on the smooth manifold.

## 6. Interaction terms and finite-scale strictness

There is no missing surviving interaction term in (4): annular cross terms vanish by (1), omitted tails vanish, and scalar-flat interiors contribute no scalar integral or scalar-square energy.

The assertion that a finite-scale Burns saving makes \(4k/(A+k)\) strict is a separate theorem, not a consequence of 86.S′. For Burns,
\[
\tau=2,\quad x_0=\varepsilon^2,\quad
\rho=\varepsilon^{1/2}=x_0^{1/4},
\]
so this lemma’s error is \(O(x_0)\). It neither resolves the linear response nor detects a kernel-direction saving of order \(x_0^2\log(1/x_0)\). At finite scale, changes in \(S,V\), scalar variance, and \(R\) must also be handled if one estimates \(\mathscr D\) directly.

However, full high-order expansions of all three quantities are **not necessary** for the infimum bound: the package’s negative-Yamabe comparison
\[
\alpha\le\frac{4p}{A+p}
\]
already turns a separately proved \(p<k\) into the strict inequality. The appropriate verification pointer is therefore the independent Burns recovery/strictness result and its Yamabe bridge, not Lemma 86.S′ alone.

## 7. Arbitrary degenerations: what survives without an energy identity

Smooth bulk and bubble convergence alone does not imply (4). Unlisted neck or concentration energy may survive; volume and scalar integral may also escape.

A useful conditional extension is the following. Suppose an arbitrary sequence has disjoint bulk/bubble convergence, bounded \(R(g_i)\), and
\[
V(g_i)\to V(g_\infty)>0.
\]
Volume convergence plus smooth bulk convergence makes the volume outside a bulk exhaustion negligible. Cauchy–Schwarz then gives \(S(g_i)\to S(g_\infty)\). Lower semicontinuity on disjoint regions gives
\[
\liminf R(g_i)\ge
L:=R(g_\infty)+\sum_bR(N_b).
\]
If \(L>0\), monotonicity in \(R\) yields
\[
\boxed{
\liminf\mathscr D(g_i)\ge
4-\frac{S(g_\infty)^2}{V(g_\infty)L}.
}
\]
Equality needs a Ricci-energy identity, not merely bubble extraction. If an additional energy \(E_R\) survives while \(V,S\) have these limits, the actual limiting denominator is \(L+E_R\).

When \(L=0\), this argument cannot evaluate the quotient or prove a limit of \(4\). Unlike a standard cutoff family, an arbitrary sequence can have diffuse small scalar/Ricci errors outside the shrinking regions; absolute convergence of \(S_i,R_i\) does not control their ratio. This is the precise boundary between the two lemmas and an unrestricted degeneration theorem.

## 8. Numerical verification

The supplied script and JSON are consistent with the analytic calculation:

- exact symbolic profiles give \((s,|\operatorname{Ric}|^2)=(12,36)\) for round curvature and \((0,0)\) for flat and Eguchi–Hanson metrics;
- the angular-factor-omitted round reference is \(V=1/12,\ S=1,\ R=3\);
- with \(\rho=a^{2/3}\), the defect values fit exponent \(2.6400\), consistent with \(O(a^{8/3})\), and \(\mathscr D/\rho^4\) stabilizes near \(38\).

The cutoff derivatives use finite differences and integration is floating-point. These data support the rate for this particular profile, but certify neither a universal sharp rate nor the claimed diffeomorphism type or orientation of the resolution.