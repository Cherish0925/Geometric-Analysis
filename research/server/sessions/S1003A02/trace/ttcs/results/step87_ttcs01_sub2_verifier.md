# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step56_orbifold_attainment_zero_energy_bound_Tpoint_interaction.md",
    "Sessions/S1003A02/workspace/scripts/step86_lemma86S_check.py",
    "Sessions/S1003A02/workspace/data/step86/lemma86S_check.json",
    "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md"
  ]
}
```

## Task

Independently verify the mathematical correctness and exact scope of Lemma 86.S and Lemma 86.S′ in theorem_package_v1.md. Focus on the cutoff scaling rho=epsilon^{tau/(tau+2)}, C^2 annular curvature and integral estimates, iteration for ALE trees, continuity of the Einstein defect, whether scalar variance is automatically controlled, and the Ricci-flat bulk case. For Wahl/T singularities, read Suvaina's primary source and determine whether the Milnor-fibre metrics have the derivative-controlled order-4 ALE asymptotics required. For Lemma 86.S′, decide the minimal hypotheses under which the displayed defect ledger follows, identify any missing denominator case or interaction term, and distinguish standard cutoff-glued families from arbitrary degenerating sequences. Give exact corrected statements/proofs where needed.

## Output

# Verification memo: Lemma 86.S, Lemma 86.S′, and the Şuvaina Milnor-fibre input

## Summary

- **Lemma 86.S (cutoff gluing of Ricci-flat ALE bubbles).** The cutoff exponent, the annular estimates, the continuity of \(\mathscr D\), and the automatic control of scalar variance are all correct. The proof leaves three things implicit:
  - the gluing needs an equivariant, orientation-matched identification of the cone at infinity with the orbifold chart;
  - the "Ricci-flat bulk" consequence does not follow from continuity of \(\mathscr D\), because \(\mathscr D\) is discontinuous at \(R=0\); it needs its own short argument (§1.4);
  - the rate \(O(\rho^4)\) is sharp for this naive scheme.
- **Şuvaina's Milnor-fibre metrics.** Her paper does not state derivative-controlled order-4 asymptotics. Her Definition 1.1 gives only \(C^0\) decay \(O(r^{-4})\) for \(g\) and \(J\). The derivative control is nevertheless true and follows from her explicit Gibbons–Hawking description, provided the centres are first translated so that the dipole term vanishes (§2).
- **Lemma 86.S′ (scalar-flat bubble ledger).** The displayed ledger is correct as a limit of cutoff-glued families. It holds under weaker hypotheses than stated (scalar-flatness is not needed if \(P(N)\) is replaced by \(R(N)=\int_N|\mathrm{Ric}|^2\)). It omits the case \(R(g)+\sum R(N_j)=0\). It does not imply the "finite-scale Burns saving makes strict" sentence: the lemma's error \(O(\rho^4)\) is of order \(x_0\), while the log saving is of order \(x_0^2\log(1/x_0)\).
- **Arbitrary sequences.** The correct general statement is a one-sided inequality, and it needs volume convergence (§3.5).

---

## 1. Lemma 86.S

### 1.1 Structure of the functional

For \(R=\int|\mathrm{Ric}|^2>0\), write \(S=\int s\) and \(V=\mathrm{Vol}\). Minimizing over \(\mu=1/\lambda\),
\[
\frac{\int|\mathrm{Ric}-\lambda g|^2}{\lambda^2V}=4-\frac{2S\mu}{V}+\frac{R\mu^2}{V}.
\]
The minimum is \(\mathscr D=4-S^2/(VR)\), attained at \(\mu=S/R\). If \(S=0\) the infimum is approached as \(\mu\to0\) and equals \(4\).

Consequences:

- \(\mathscr D\in[0,4]\), because \(S^2\le V\int s^2\le4VR\).
- \(\mathscr D\) is continuous on \(\{R>0\}\) as a function of \((R,S,V)\).
- \(\mathscr D\) is increasing in \(R\) and in \(V\). This monotonicity is used in §3.
- Using \(4R=4P+\int s^2\) gives the corpus form \(\mathscr D=(4P+L_s)/R\).
- **\(\mathscr D\) is not continuous at \(R=0\).** A near-Ricci-flat metric with nearly constant scalar curvature \(s\equiv c\ne0\) and \(P\ll c^2V\) has \(S^2/(VR)\to4\), so \(\mathscr D\to0\). Any statement about Ricci-flat bulks therefore needs a separate argument.

### 1.2 Cutoff exponent and annular estimates — correct

Setting and conventions:

- Orbifold normal coordinates on the uniformizing chart give \(g=\delta+e_g\) with \(|\partial^ke_g|\lesssim r^{2-k}\).
- The scaled bubble \(\varepsilon^2\Phi^*h\) at \(x=\varepsilon y\) gives \(\delta+e_h\) with \(|\partial^ke_h|\lesssim(\varepsilon/r)^\tau r^{-k}\) for \(k\le2\).
- The cutoff \(\chi(r/\rho)\) has \(|\partial^k\chi|\lesssim\rho^{-k}\).

On \(\rho\le r\le2\rho\), the deviation \(e=\chi e_g+(1-\chi)e_h\) satisfies \(|\partial^ke|\lesssim\rho^{-k}\big(\rho^2+(\varepsilon/\rho)^\tau\big)\). Curvature is \(\partial^2e+(\partial e)^2\) times bounded factors. Hence
\[
|\mathrm{Rm}|\lesssim \rho^{-2}\big(\rho^2+(\varepsilon/\rho)^\tau\big).
\]
The choice \(\rho=\varepsilon^{\tau/(\tau+2)}\) gives \((\varepsilon/\rho)^\tau=\varepsilon^{2\tau/(\tau+2)}=\rho^2\). The two errors balance and \(|\mathrm{Rm}|=O(1)\) on an annulus of volume \(O(\rho^4)\). Two side conditions also hold for every \(\tau>0\):

- \(\rho\to0\), so the annulus shrinks inside the chart;
- \(\rho/\varepsilon=\varepsilon^{-2/(\tau+2)}\to\infty\), so the cutoff lies in the ALE region.

Integral changes:

| Region | \(\int\lvert\mathrm{Ric}\rvert^2\) | \(\int s\) | Volume |
|---|---|---|---|
| Annulus | \(O(\rho^4)\) | \(O(\rho^4)\) | \(O(\rho^4)\) |
| Deleted ball \(B_{2\rho}\) of \(g\) | \(O(\rho^4)\) | \(O(\rho^4)\) | \(O(\rho^4)\) |
| Bubble core \(\{r<\rho\}\) | \(0\) | \(0\) | \(\varepsilon^4\mathrm{Vol}_h\{r_N<\rho/\varepsilon\}\le C\rho^4\) (ALE volume growth) |

**Balancing is optimal for this scheme.** The core is exactly Ricci-flat over volume \(\asymp\rho^4\), so it contributes \(4\Lambda^2\rho^4\) to \(\int|\mathrm{Ric}-\Lambda g|^2\). The annular error is \(\asymp(\varepsilon/\rho)^{2\tau}\). Minimizing \(\rho^4+(\varepsilon/\rho)^{2\tau}\) gives the same \(\rho\). The exponent \(4\tau/(\tau+2)\) (\(=8/3\) for \(\tau=4\)) is therefore the best rate obtainable with an exactly Ricci-flat core; better rates require corrected metrics, as the package already says.

### 1.3 Hypotheses the proof uses but the statement leaves implicit

1. **Equivariant chart matching.** The ALE chart \(\Phi_j:N_j\setminus K_j\to(\mathbb R^4\setminus B)/\Gamma_j'\) must use a group \(\Gamma_j'\) conjugate to \(\Gamma_j\) inside \(SO(4)\). The resulting smooth manifold depends on that conjugation and on its orientation. For Wahl points this is exactly the "complex orientation" choice of Prop. 56.U; \(1/n^2(1,q)\) and \(1/n^2(1,-q)\) give different links.
2. **Smooth convergence of the cone chart.** Only \(k\le2\) derivative decay is used, plus the volume bound \(\mathrm{Vol}_h\{r<T\}\le CT^4\).
3. **Uniformity for families of bubbles.** If the bubble varies (internal moduli of a Wahl/T fibre with \(d\ge2\), or Kähler-class ratios), the decay constant \(C\) must be uniform. Otherwise the configuration is a tree and §1.6 applies.

### 1.4 Ricci-flat bulk — the consequence is right, the proof route is not

The lemma assumes \(\mathrm{Ric}_g\not\equiv0\), and continuity of \(\mathscr D\) does not cover \(R(g)=0\) (§1.1). The correct argument is Cauchy–Schwarz on the support of \(s\).

If \(g\) is Ricci-flat, \(s_{g_\varepsilon}\) is supported in the annuli and bubble cores, a set of volume \(O(\rho^4)\). Then
\[
S^2\le\mathrm{Vol}(\mathrm{supp}\,s)\int s^2\le 4\,\mathrm{Vol}(\mathrm{supp}\,s)\,R(g_\varepsilon),
\qquad
\frac{S^2}{VR}\le\frac{4\,O(\rho^4)}{V}\to0 .
\]
Hence \(\mathscr D(g_\varepsilon)\to4\); if \(g_\varepsilon\) happens to be exactly Ricci-flat, \(\mathscr D=4\) by convention. This holds for any bubbles, Ricci-flat or not. It proves the sentence "a Ricci-flat orbifold has \(\mathscr D=4\) and gives only \(P_*=0\)". It is also why the α-readings of 52.9, 56.B, 58.O and 59.N correctly exclude \(\Lambda=0\).

### 1.5 Scalar variance is automatically controlled — confirmed

\(\mathscr D\) depends only on \((R,S,V)\), and all three change by \(O(\rho^4)\). The term \(L_s=\int s^2-S^2/V\) is therefore controlled without any extra hypothesis. The core contributes \(\bar s^2\cdot O(\rho^4)\) to \(L_s\).

For an Einstein orbifold with \(\Lambda\ne0\):
\[
\mathscr D(g_\varepsilon)=O(\rho^4)=O\big(\varepsilon^{4\tau/(\tau+2)}\big).
\]
The removal of the "vanishing scalar variance" proviso in Cor. 52.9, 56.A–B, 58.O and 59.N is legitimate for these cutoff-glued families. For Prop. 56.U's α-form, \(\alpha(M')\le\mathscr D(V,g)\) holds for every smooth orbifold \(g\), including Ricci-flat \(g\), where it is trivial because \(\alpha\le1\).

A minor point in the Step-56 note: \(\rho=\lambda^{1/2}\) gives \(O(\lambda^2)\), whereas the balanced \(\rho=\lambda^{2/3}\) gives \(O(\lambda^{8/3})\) for both \(P\) and \(\mathscr D\).

### 1.6 ALE trees — correct, with the scale bookkeeping made explicit

Let a Ricci-flat ALE orbifold \(N_1\) have an orbifold point \(q\) where \(h_1\) is a smooth orbifold metric (\(h_1=\delta+O(r^2)\) in normal coordinates). Glue \(\varepsilon_2^2h_2\) at \(q\) with \(\rho_2=\varepsilon_2^{\tau_2/(\tau_2+2)}\), in \(N_1\)-units, inside \(\varepsilon_1^2h_1\).

In \(V\)-units this inner annulus has radius \(\varepsilon_1\rho_2\), curvature \(O(\varepsilon_1^{-2})\), and volume \(O(\varepsilon_1^4\rho_2^4)\). Its contributions are:

| Quantity | Contribution |
|---|---|
| \(\int\lvert\mathrm{Ric}\rvert^2\) (scale-invariant) | \(O(\rho_2^4)\) |
| \(\int s\) | \(O(\varepsilon_1^2\rho_2^4)\) |
| Volume | \(O(\varepsilon_1^4\rho_2^4)\) |

So the one-shot multiscale metric has \((R,S,V)\to(R(g),S(g),V(g))\) as \(\varepsilon_1\to0\) and \(\varepsilon_2\to0\), in any order or jointly. The cone of \(N_2\) must match the group at \(q\) as in §1.3(1).

### 1.7 Numerical check `step86_lemma86S_check.py`

The model is round \(S^4/\pm1\) (\(\Lambda=3\)) resolved by two EH spaces, with \(\varepsilon=a\), \(\tau=4\), \(\rho=a^{2/3}\). The script's conventions are right:

- the profile \(A=B=\sin u/2\) is the round metric in Euler forms;
- EH has \(\psi\)-period matching the \(\mathbb Z_2\) quotient;
- the core volume uses \(FAB^2=u^3/8\);
- the convention checks give \(s,|\mathrm{Ric}|^2=12,36\) (round) and \(0,0\) (flat, EH).

From the JSON, \(\mathscr D/\rho^4=31.1,\,36.3,\,37.8,\,38.2,\,38.4\) for \(a=0.2\) down to \(0.0125\). The ratio stabilizes, so the fitted exponent \(2.64\) is a pre-asymptotic value of \(8/3\). Since \(V\to1/12\), the core alone accounts for \(4\cdot(\rho^4/64)/(1/12)=0.75\rho^4\); the remaining \(\approx37.6\rho^4\) is annular. This confirms that the \(O(\rho^4)\) rate is attained, not merely an upper bound. The topology of the resolution (intersection form \(\langle-1\rangle^{2}\) in the EH orientation, i.e. \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\)) is not tested by the script.

---

## 2. Wahl and T singularities: what Şuvaina's source supplies

**What the source says.**
- Definition 1.1 requires only \(\pi_*g-h_0=O(r^{-4})\) and \(\pi_*J-J_0=O(r^{-4})\). No derivatives are stated.
- Theorem A gives a unique ALE Ricci-flat Kähler metric in each Kähler class of a \(\mathbb Q\)-Gorenstein smoothing fibre.
- Prop. 3.3 treats \(d=1\): the rational ball \(B_{n,m}\), \(\pi_1=\mathbb Z_n\), end \(L(n^2,nm-1)\), with a unique metric. The scale of the metric is the radius of the centre polygon, which is the smoothing parameter.
- Sections 3 and 5 realize every such metric as the free \(\mathbb Z_n\)-quotient of the Gibbons–Hawking/Hitchin \(A_{dn-1}\) metric. The \(dn\) centres are the vertices of \(d\) regular \(n\)-gons in horizontal planes \(b=b_i\), centred on the \(b\)-axis. The group \(\mathbb Z_n\) acts by \(a\mapsto\rho^{-m}a\), \(b\mapsto b\), \(\theta\mapsto\theta+2\pi/n\).

**The source also checks the group action is free.** Here \(\Gamma=\frac1{dn^2}(1,dnm-1)\subset U(2)\subset SO(4)\). Any prime \(p\mid dn\) satisfies \(dnm-1\equiv-1\pmod p\), so both weights are units mod \(dn^2\). The action on \(S^3\) is free, as Lemma 86.S requires.

**Supplying derivative-controlled order 4.**

1. *Dipole.* Write \(V(x)=\frac12\sum_i|x-x_i|^{-1}=\frac{dn}{2|x|}+V_1+V_2+\cdots\) with \(V_\ell\) homogeneous of degree \(-\ell-1\). The dipole \(V_1\) is proportional to \(\sum_i x_i=(n\sum_ib_i)e_b\).
   - For \(d=1\) the single polygon is centred at the origin and \(V_1=0\) automatically. This matches the Step-56 quadrupole \(-(n^2R_c^2/4)P_2/|x|^3\).
   - For \(d\ge2\), translate along the \(b\)-axis so that \(\sum b_i=0\). The source notes that \(b\)-translations give equivalent metrics, and they commute with the \(\mathbb Z_n\) action.
   
   After this, \(V-V_0=O(|x|^{-3})\) with \(\partial^k\)-derivatives \(O(|x|^{-3-k})\).
2. *Connection.* Choose the connection correction \(\omega-\omega_0\) in radial gauge. This gauge is equivariant under rotations about the \(b\)-axis, hence \(\mathbb Z_n\)-invariant. Then \(\omega-\omega_0=O(|x|^{-3})\) with derivatives.
3. *Conversion to cone coordinates.* With \(|x|\asymp r^2\) and the flat model given by \(V_0\), \(\omega_0\) (the cone \(\mathbb C^2/\mathbb Z_{dn}\), whose further \(\mathbb Z_n\) quotient is \(\mathbb C^2/\Gamma_{dn^2}\)), the relative error is \(O(|x|^{-2})=O(r^{-4})\). In the cone metric, the \(k\)-th derivatives are \(O(r^{-4-k})\).

So \(\tau=4\) with all derivatives holds for every Şuvaina Milnor fibre, for both the Wahl balls (\(d=1\)) and the general T fibres. The model is a quotient of a quotient-invariant GH metric, so equivariance is built in. Lemma 86.S therefore applies; it needs only \(k\le2\) and any \(\tau>0\). Without step 1, a nonzero dipole for \(d\ge2\) gives only order 2 in the given chart. That still suffices for Lemma 86.S, but not for the "order 4" assertion.

The package's parenthetical "(τ=4 … for Šuvaina's Milnor-fibre metrics …)" should cite this GH multipole argument, not Şuvaina's Definition 1.1 alone.

---

## 3. Lemma 86.S′: corrected statement, hypotheses, and reach

### 3.1 Correct general form

Bubbles enter the three quantities differently:
- \(\int|\mathrm{Ric}|^2\) and \(\int s^2\) are scale-invariant in dimension 4, so each bubble contributes its full \(R(N)\) and \(\int_N s^2\);
- \(\int s\) scales by \(\varepsilon^2\) and volume by \(\varepsilon^4\), so the bubble's contributions to \(S\) and \(V\) vanish in the limit.

**Lemma 86.S′ (corrected).** Let \((V,g)\) be a compact orbifold with \(R(g)>0\). Attach bubbles \((N_j,h_j)\): complete AE (smooth points, \(\Gamma=1\)) or ALE (matched cyclic or other free groups, §1.3(1)), possibly orbifold trees. Assume derivative-controlled decay \(|\partial^k(h-\delta)|\le Cr^{-\tau-k}\), \(k\le2\), \(\tau>0\), uniform along the family. Glue them at \(\rho_j=\varepsilon_j^{\tau/(\tau+2)}\) with \(\varepsilon_j\to0\). Then
\[
\mathscr D(g_\varepsilon)\longrightarrow 4-\frac{S(g)^2}{V(g)\,[R(g)+\sum_jR(N_j)]}
=\frac{4P(g)+L_s(g)+\sum_j\big(4P(N_j)+\int_{N_j}s^2\big)}{R(g)+\sum_jR(N_j)} .
\]
For scalar-flat \(N_j\), \(R(N_j)=P(N_j)\) and this is the displayed ledger.

**Proof additions beyond §1.2.**
- \(\mathrm{Ric}_h=O(r^{-2-\tau})\), so \(R(N)<\infty\) for every \(\tau>0\). The hypothesis "finite \(P(N_j)\)" is redundant under \(C^2\) decay.
- The truncations \(\int_{r<\rho/\varepsilon}|\mathrm{Ric}_h|^2\) converge to \(R(N)\).
- The bubble's scalar integral is \(\varepsilon^2\int_{r<\rho/\varepsilon}s_h\). It is \(O(\varepsilon^2)\) for \(\tau>2\), \(O(\varepsilon^2\log(\rho/\varepsilon))\) for \(\tau=2\), and \(O(\varepsilon^\tau\rho^{2-\tau})=O(\rho^4)\) for \(\tau<2\). All tend to \(0\).
- The bubble's volume is \(O(\rho^4)\).
- The cross term \(\bar s\int s_N\) in \(L_s\) vanishes in the limit.

Scalar-flatness is therefore not a necessary hypothesis; it is only what turns \(R(N)\) into \(P(N)\).

### 3.2 Missing denominator case

If \(R(g)+\sum R(N_j)=0\) (Ricci-flat bulk and Ricci-flat bubbles), the formula reads \(0/0\). The correct value is \(\lim\mathscr D(g_\varepsilon)=4\), by the support argument of §1.4. If \(R(g)=0\) but some \(R(N_j)>0\), the formula gives \(4\), consistent with §1.4. If \(S(g)=0\) with \(R(g)>0\), it gives \(4\).

### 3.3 Möbius reading and the zero-value sentence

\(\mathscr D_{\rm new}=(\mathscr D\,R+4R_N)/(R+R_N)\) is the convex combination of \(\mathscr D\) and \(4\) with weights \(R\) and \(R_N\). A bubble moves the value toward \(4\) iff \(R_N>0\) and \(\mathscr D<4\). This corrects "exactly when \(P(N)>0\)" for bubbles that are not scalar-flat.

The limit is \(0\) iff all of the following hold:
- \(P(g)=L_s(g)=0\) (Einstein; on an orbifold, \(\mathrm{Ric}^\circ=0\) forces \(s\) constant);
- \(R(g)>0\) (i.e. \(\Lambda\ne0\));
- every \(R(N_j)=0\) (Ricci-flat bubbles).

This is exact for a fixed bulk.

For varying bulks \(g_i\), dilution of a bubble with \(R_N>0\) would need \(R(g_i)\to\infty\) while \(\mathscr D(g_i)\to0\). Chern–Weil prevents this: \(R\le8\pi^2(4\mathfrak p+3T_+)\) and \(P\le\mathscr D R/4\) give \(R\le24\pi^2T_+/(1-\mathscr D)\) on manifolds. On orbifolds \(T_+\) carries local \(\eta\)/Euler corrections at the singular points. So the sentence extends to varying bulks once the orbifold \(T_+\) is used. As written, it concerns fixed-bulk glued families, which is correct.

### 3.4 Interaction terms, and what strictness needs

All interaction terms vanish in the limit:
- Theorem F's \(-8\pi^2x_0\mathbf R^+_p(\zeta,\zeta)\);
- the ALE quadrupole pairing at order \(\varepsilon^4\) (no log at \(P\)-critical bulks, Lemma 56.L).

The finite-scale sentence is a different matter. For Burns, \(\tau=2\) and \(x_0=\varepsilon^2\), so \(\rho=x_0^{1/4}\) and the lemma's error is \(O(\rho^4)=O(x_0)\). This is the same order as Theorem F's linear term and much larger than the kernel-direction saving \(\frac{\Phi}{2}x_0^2\log(1/x_0)\) of 57.Φ/59.R.

Strictness of \(\alpha<4k/(A+k)\) therefore needs, independently of 86.S′:
- \(R\) expanded to \(o(x_0^2\log(1/x_0))\) (59.R supplies the \(P\) part);
- \(S\) expanded to the same accuracy (the Burns scalar flux \(4\pi^2x_0\) is linear in \(x_0\));
- \(V\) expanded to the same accuracy.

The \(\mathscr D\)-variation at a Kähler–Einstein base with \(s=-4\) makes the weights explicit:
\[
d\mathscr D=\frac{2\,dS+dR+4\,dV}{V}.
\]
A linear \(dS\) of order \(x_0\) would dominate unless it cancels or is absent. The "scalar-neutral at log order, \(s_1=0\)" input of 69.KE is exactly what is required. The package sentence "which finite-scale Burns saving then makes strict" should point to 69.KE's expansion of \((R,S,V)\), not to 86.S′.

### 3.5 Glued families versus arbitrary degenerating sequences

86.S′ is a theorem about constructed families. For an arbitrary sequence \(g_i\) on \(M\), the robust statement is a one-sided inequality.

**Proposition.** Suppose \(g_i\) converges in the bubble-tree sense:
- smoothly on compact subsets of \(V\setminus\{p_j\}\) to an orbifold bulk \(g_\infty\);
- after rescaling, smoothly on compact sets to bubbles \(N_b\) on disjoint regions.

Suppose also \(\sup_iR(g_i)<\infty\) and \(\mathrm{Vol}(g_i)\to V(g_\infty)\). Then
\[
\liminf_i\mathscr D(g_i)\ \ge\ 4-\frac{S(g_\infty)^2}{V(g_\infty)\,[R(g_\infty)+\sum_bR(N_b)]}.
\]

*Proof.*
- Fatou on disjoint regions gives \(\liminf R_i\ge R_\infty+\sum R(N_b)\); energy lost in necks only increases \(R_i\).
- Let \(U_i\) be the complement of a large bulk compact set, with \(\mathrm{Vol}(U_i)\to0\). Then \(|\int_{U_i}s|\le(4\,\mathrm{Vol}(U_i)R_i)^{1/2}\to0\), so \(S_i\to S_\infty\).
- \(\mathscr D\) is increasing in \(R\) (§1.1). \(\square\)

Equality requires an energy identity (no neck energy), which is the delicate (4.43)-type input already flagged for Anderson's theorem.

Mechanisms outside this proposition:
- **Volume escaping into necks or collapsing regions.** Then \(V_i\not\to V_\infty\) and \(S_i\) can shift; the proposition breaks.
- **Total or partial collapse.** There is no bulk limit.
- **\(R_i\to\infty\).** This is excluded on fixed topology when \(\mathscr D_i<1-\delta\), by the Chern–Weil bound.

The package's "not a lower-semicontinuity theorem for arbitrary sequences" is accurate. The proposition above is the precise replacement, and its hypothesis \(\mathrm{Vol}\to V_\infty\) is the one the α-version of 59.Z does not yet supply (§20.5).

---

## 4. Corrected text for Lemma 86.S

**Lemma 86.S (corrected).** Let \((V,g)\) be a compact orbifold with isolated points \(p_j\). Let each local group \(\Gamma_j\subset SO(4)\) act freely on \(S^3\), linearly in \(g\)-normal coordinates of the uniformizing chart. Let \((N_j,h_j)\) be Ricci-flat ALE orbifolds (trees allowed) whose cone groups are \(SO(4)\)-conjugate to \(\Gamma_j\) by the chosen orientation-preserving identification. Assume \(|\partial^k(\Phi_*h_j-\delta)|\le Cr^{-\tau-k}\) for \(k\le2\), some \(\tau>0\). Glue with \(\rho=\varepsilon^{\tau/(\tau+2)}\).

Then \(R,S,V\) each change by \(O(\rho^4)\). Hence:
1. if \(R(g)>0\), \(\mathscr D(g_\varepsilon)=\mathscr D(g)+O(\rho^4)\);
2. if \(g\) is Einstein with \(\Lambda\ne0\), \(\mathscr D(g_\varepsilon)=O(\varepsilon^{4\tau/(\tau+2)})\), and this rate is attained by the cutoff scheme;
3. if \(R(g)=0\), \(\mathscr D(g_\varepsilon)\to4\), by Cauchy–Schwarz on \(\mathrm{supp}\,s\) and not by continuity.

Şuvaina's Milnor-fibre metrics satisfy the hypothesis with \(\tau=4\) once the GH centres are centred so the dipole vanishes (§2); Kronheimer/EH spaces satisfy it as well.