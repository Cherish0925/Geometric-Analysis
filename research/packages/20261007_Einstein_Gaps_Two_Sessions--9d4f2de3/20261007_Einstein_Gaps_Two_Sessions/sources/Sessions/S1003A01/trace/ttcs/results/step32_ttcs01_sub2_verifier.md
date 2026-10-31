# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md",
    "Knowledge/objects/papers/Invariants-of-some-compactified-Picard-modular-surfaces-and-applications--a2801b1afe2c--6270e445600c/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex",
    "Skills/geometric-analysis/research/paper/sections/linear_coercivity.tex"
  ]
}
```

## Task

Independently verify the theorem-level ramified Kähler–Einstein background and actual-field part of the proposed Einstein-gap transfer. Read the revised Step-31 note and the cited original-source representations. Check: (i) whether a preliminary principal-congruence cover can contain the required fixed buffered CH ball and later high-ramification congruence covers can be taken inside it; (ii) whether Biquard–Guenancia gives smooth compact Ric=-g pullbacks and uniform local C^2 convergence on every lifted marked ball; (iii) the Hurwitz/adjunction/log-proportionality formulas for A=K^2 and Delta=3chi-A; (iv) the positive-r tower assertion, especially the use of Dzambic’s index and boundary self-intersection formulas to obtain Delta→∞ and Delta/A→0; (v) ampleness/minimal general type and LeBrun’s metricwise polarized class after blowups and S1xS3 handles, including b+=1 chambers, exceptional signs, p>=A, and a^2>=T+. Give precise corrections if any step is stronger than its sources.

## Output

# Step 31: verification of the ramified Kähler–Einstein background and the Seiberg–Witten field

## Summary

The five ingredients hold up to small repairs. None of the repairs changes a formula used downstream. Four places are stated more strongly than, or more loosely than, the cited sources support:

- **The group setup.** The covers must be Galois over the preliminary base. Principal congruence subgroups of one ambient arithmetic group provide this.
- **Convergence for vector cone angles.** Biquard–Guenancia (BG) prove smooth convergence for proportional cone-angle vectors. For a general vector of angles they only assert it. A short monotonicity sandwich closes the gap.
- **The Džambić index formula.** As printed, it is ambiguous at split primes. Restricting the level to inert primes, or using the order of the finite group directly, removes the ambiguity.
- **The \(b^+=1\) discussion.** It is never needed for large \(m\), because \(p_g\to\infty\). A clean chamber argument is supplied below in case it is wanted.

## (i) Preliminary congruence cover and the embedded buffered ball

**The embedding argument is correct.** Set \(R_{\rm tot}=R_{128}+\text{buffer}\). By proper discontinuity, the set
\[
F=\{\gamma\ne1:\ d(\tilde x,\gamma\tilde x)\le 2R_{\rm tot}\}
\]
is finite. Suppose \(\Gamma\subset GL_3(\mathcal O_K)\) and \(\bigcap_m\Gamma(m)=\{1\}\). Then some \(\Gamma(m_0)\) misses \(F\). Every subgroup of \(\Gamma(m_0)\) also misses \(F\), so the ball embeds in the preliminary quotient and in every later cover.

The étale cover \(X_m\to\Gamma(m_0)\backslash\mathbb B^2\) is trivial over the contractible ball. The ball therefore has exactly \(d_m=\deg\) disjoint isometric lifts.

**Arithmetic check of the radius.** With \(\mathrm{Ric}=-g\) the holomorphic sectional curvature is \(-2/3\), so \(d(0,z)=\sqrt6\,\operatorname{artanh}|z|\). Then
\[
\sqrt6\,\operatorname{arsinh}\sqrt{128}=\sqrt6\,\ln\!\big(\sqrt{128}+\sqrt{129}\big)=7.6451\ldots
\]
This agrees with the note, under the cell convention \(X=|z|^2/(1-|z|^2)\). That convention is assumed here, not verified.

**Correction 1: the later covers must be Galois over the preliminary base.** BG §4.3 uses a single cone angle \(\beta_\lambda=1/v_{m,\lambda}\) on each cusp curve \(D_\lambda\) of the base. The orbifold pullback is smooth only if every component of \(\pi_m^{-1}(D_\lambda)\) has the same ramification index. Galois covers give this; BG write "up to taking a further cover, one can assume … Galois".

The sentence "literal nesting is not used" is harmless. However, "cofinal sequence of further congruence covers" should read "covers \(\Gamma_j\triangleleft\Gamma(m_0)\)".

The cleanest concrete realization is:
- \(\Gamma_0=\Gamma_K(n_0)\subset SU(h,\mathcal O_K)\), with \(n_0\) odd, coprime to \(d\), and \(N((n_0))>3\). This group is neat by Džambić Lemma 2.6. Enlarge \(n_0\) until \(F\cap\Gamma_0=\emptyset\).
- \(\Gamma_j=\Gamma_K(n_0n_j)\). It is normal in \(\Gamma_K\), hence normal in \(\Gamma_0\), so the covers are Galois automatically.

The note's phrase "principal congruence subgroup of \(\Gamma\)" presupposes a realization \(\Gamma=G(\mathbb Z)\), as BG §4.3 does. For an arbitrary neat arithmetic \(\Gamma\), use \(\Gamma\cap\Gamma_K(n)\) after fixing a commensurability with a Picard group.

**Ramification indices grow along this tower.** BG's Mumford citation gives \(\ell\mid v_{m,\lambda}\) for suitable \(m(\ell)\). A direct route is available for \(\Gamma_K(n_0n_j)\):
- The normal coordinate to \(D_\lambda\) in the toroidal compactification is \(\exp(2\pi i t/\tau)\), where \(\tau\) generates \(\Gamma\cap Z(U_\lambda)\).
- So \(v_{j,\lambda}=[\Gamma_0\cap Z(U_\lambda):\Gamma_j\cap Z(U_\lambda)]\).
- Writing \(Z(U_\lambda)=\{1+tN_\lambda\}\), membership in \(\Gamma_K(n)\) requires \(tN_\lambda\in nM_3(\mathcal O_K)\).
- Hence \(v_{j,\lambda}\gtrsim n_j\to\infty\) for every \(\lambda\).

The ramification index multiplies through intermediate covers, so divisibility is preserved.

## (ii) Biquard–Guenancia: smooth compact pullbacks with \(\mathrm{Ric}=-g\), and uniform local \(C^2\) convergence

**What the source states.**
- Theorem 1.1 is proved for angle vectors \(\beta a_\lambda\) with fixed ratios \(a_\lambda\) and a single \(\beta\to0\).
- §4.1 asserts, without a separate proof, that the general-vector case "carries over with no significant change". It prints the conclusion as \(C^\infty_{\rm loc}(U^*)\), which is evidently meant as \(C^\infty_{\rm loc}(X^\circ)\).
- §4.3 uses the general vector \(\beta_m=(1/v_{m,\lambda})_\lambda\). These ratios need not be fixed along the tower.

**Gap fill (Correction 2).** BG prove componentwise monotonicity: for \(\beta\le\beta'\) componentwise,
\[
\frac{\hat\varphi_\beta+\tau_\beta}{1-\delta_0^{-1}\sum_\lambda\beta_\lambda}\ \le\ \frac{\hat\varphi_{\beta'}+\tau_{\beta'}}{1-\delta_0^{-1}\sum_\lambda\beta'_\lambda}.
\]
For a sequence \(\beta^{(m)}\), set \(b_m^\pm=\max_\lambda/\min_\lambda\beta^{(m)}_\lambda\). Then \(\beta^{(m)}\) is sandwiched between the diagonal vectors \(b_m^-\mathbf 1\le\beta^{(m)}\le b_m^+\mathbf 1\). The normalizing factors tend to 1 and \(\tau\to0\). The diagonal potentials decrease to \(\hat\varphi\) by Theorem 1.1 with \(a_\lambda\equiv1\).

This gives \(C^0_{\rm loc}\) convergence of the potentials along any sequence with \(\max_\lambda\beta^{(m)}_\lambda\to0\). The Chern–Lu Laplacian bound and the bootstrap are local and uniform, which yields \(C^\infty_{\rm loc}(X^\circ)\). One also needs \(\beta_\lambda\le\delta_0/2N\), which holds for large \(m\).

**Smoothness of the pullback.** For \(\beta_\lambda=1/v_\lambda\), the conic Kähler–Einstein metric is the orbifold Kähler–Einstein metric by uniqueness. Its pullback under a Galois cover ramified to order exactly \(v_\lambda\) is smooth. BG state this in §4.3.

**Uniformity over lifts.** The pullback is a local isometry on each lift. Hence \(\varepsilon_m=\|g_m-g_{CH}\|_{C^2(K)}\) is literally the same number on all \(d_m\) lifts, and it tends to 0. Correct as written.

## (iii) Hurwitz, adjunction and log-proportionality

All formulas are correct:
- **Hurwitz.** \(\pi^*D_\lambda=v_\lambda D'_\lambda\), so \(K_{\bar X_m}=\pi^*(L-\sum_\lambda\beta_\lambda D_\lambda)\).
- **Adjunction.** The \(D_\lambda\) are disjoint elliptic curves, so \(L\cdot D_\lambda=0\). Hence \(A_m/d_m=L^2+\sum_\lambda\beta_\lambda^2D_\lambda^2\).
- **Euler characteristic.** \(\chi(\bar X_m)=d_m\,e(X^\circ)\).
- **Log proportionality.** Džambić Prop. 3.2 gives \(c_2(\bar X)=e(X^\circ)\) and \(c_1^2=3c_2+D^2\). Together with \(K^2=L^2+D^2\), this gives \(L^2=3e(X^\circ)\).
- **Positivity.** \(\Delta_m=-d_m\sum_\lambda\beta_\lambda^2D_\lambda^2>0\), using \(D_\lambda^2<0\). Also \(d_m\asymp A_m\).

**Useful addition.** In \(\bar X_m\), \((D'_\lambda)^2_{\rm tot}=d_m\beta_\lambda^2D_\lambda^2\). Therefore
\[
\Delta_m=-\,T_m\cdot T_m ,
\]
the self-intersection of the toroidal divisor of \(\bar X_m\) itself. This is Džambić Prop. 3.2 applied to \(\bar X_m\), since \(\bar X_m\) is the toroidal compactification of the neat \(\Gamma_j\backslash\mathbb B^2\). It links (iii) to (iv) exactly.

## (iv) The tower with \(r>0\)

The qualitative statement is correct. Its precise form follows.

**Correction 3: the index formula.** Džambić's Theorem 2.5 is printed as a product over prime *ideals*. At a split \(p\), \(\Gamma(\mathfrak p)=\Gamma(p)\), because \(G(\mathbb Z_p)\cong SL_3(\mathbb Z_p)\). A literal reading of the formula for \((n)\) with a split factor would double the exponent. Two remedies:
- take \(n_j\) with only inert prime factors, coprime to \(2d\); or
- use \(|G(\mathbb Z/n)|\asymp n^8\) directly.

**The resulting quantities.**
- Index: \(I(n)\asymp n^8\). This is "degree eight" in the rational level \(n\), and degree four in \(N(\mathfrak a)=n^2\).
- Width parameter: \(\vartheta_{(n)}=n\) when \(\gcd(n,d)=1\), because \(N(\sqrt{-d})=d\) is prime to \(n\).
- Hypotheses of Prop. 3.5 (neat, \(N>3\), odd level, the \(\mathbb Q(\sqrt{-7})\) exception avoided): all hold.

Then
\[
\Delta_j=-T_j^2=\frac{h_K\eta_K I(n_j)}{n_j^2}\asymp n_j^6\to\infty,
\qquad
A_j=I(n_j)\Big(3c_2(Y(1))-\frac{h_K\eta_K}{n_j^2}\Big),
\]
so
\[
\frac{\Delta_j}{A_j}=\frac{h_K\eta_K/n_j^2}{3c_2(Y(1))-h_K\eta_K/n_j^2}\asymp n_j^{-2}\to0 .
\]
These \(\Delta_j\) are exactly the Step-31 \(\Delta_m\), by the identity in (iii). In particular \(\Delta\asymp A^{3/4}\), so prescribing \(r>0\) gives \(Q\asymp A^{3/4}\) and \(h\asymp A^{-1/4}\). For \(r=0\), the choice \(Q\asymp\sqrt{A\Delta}\asymp A^{7/8}\) is valid.

**The surgery algebra is verified.**
- On \(\bar X_m\): \(2\chi-3\tau=4\chi-A=A/3+4\Delta/3\).
- With \(k=2(Q-\Delta)/9\) and \(\ell=7Q/36+\Delta/18\): \(k+4\ell=Q\) and \(5k-4\ell=Q/3-4\Delta/3\).
- Hence \(T_-=(A+Q)/3\) and \(T_+=A-Q\), each up to \(O(1)\) rounding.
- \(U_{\rm top}=1+h+O(A^{-1})\), and \(O(A^{-1})=o(h)\) because \(Q\to\infty\).
- \(k\ge0\) requires \(r\le1\).

Define \(h:=(k+4\ell)/A\) after rounding. Then \(T_+=A(1-h)\) holds exactly, as the linear-window theorem requires.

## (v) Ampleness, minimal general type, and LeBrun's class

**Ampleness.** The KE argument is valid: \([\omega_m]=2\pi c_1(K)\), so \(K\) is positive and therefore ample by Kodaira. A more direct route: BG show \(K+\sum_\lambda(1-\beta_\lambda)D_\lambda\) is ample for small \(\beta\), and its pullback \(K_{\bar X_m}\) under a finite map is ample. From ampleness, \(K\cdot E>0\) excludes \((-1)\)-curves, and \(K^2>0\) gives general type.

Džambić Theorem 4.1 gives only general type, not ampleness.

**Correction 4: \(b^+=1\) never occurs for large \(m\).** We have
\[
\chi(\mathcal O)=\frac{A+(A+\Delta)/3}{12}\to\infty,
\qquad p_g\ge\chi(\mathcal O)-1,
\qquad b^+=2p_g+1\to\infty .
\]
The chamber discussion can therefore be dropped.

If it is retained, the correct justification is as follows:
- \(c=-K\) satisfies \(c^2=A>0\), so it is timelike on \(M\).
- The sign choice \(E_j\cdot\omega_H\le0\) gives \(a\cdot\omega_H\ge c\cdot\omega_H>0\).
- The set of forward \(\omega\) with \(a\cdot\omega>0\) is convex. It contains the connected-sum metrics with small exceptional spheres, where the blow-up formula applies. So the invariant is the same nonzero value for every \(H\).

**Nonzero invariant on \(\bar X_m\).** The canonical Spin\(^c\) structure with \(c_1(L)=-K\) has invariant \(\pm1\) (Witten, \(b^+>1\)). LeBrun's hypothesis \((2\chi+3\tau)(X)=A>0\) holds.

**LeBrun Proposition 3.2.**
- Virtual dimension: \(\big(a^2-(2\chi+3\tau)(M)\big)/4=\ell\), which matches the \(\ell\) holonomy insertions.
- Positive square: with \(a=c-\sum_jE_j\) and \(c^+\cdot E_j\le0\),
\[
(a^+)^2=(c^+)^2-2\sum_jc^+\cdot E_j+\Big|\sum_jE_j^+\Big|^2\ \ge\ (c^+)^2\ \ge\ c^2=A .
\]
- Class square: \(a^2=A-k\ge A-k-4\ell=T_+\).
- Conformal invariance: the polarization \(H\), and hence the selected structure, is constant on each conformal class.

Two source points to record:
- LeBrun's first displayed line writes \((c^+_1)^2=([c_1(X)]^++\sum_jE_j^+)^2\). This conflicts with \(c_1(L)=c_1(X)-\sum_jE_j\), but his subsequent expansion is the correct minus version, so this is a typo in the source.
- Nonvanishing on the connected sum, including the handle insertions, is LeBrun's citation of Fintushel–Stern and Ozsváth–Szabó, not something proved in that paper.

## Unresolved

Nothing in items (i)–(v) remains open once Corrections 1–4 are inserted. The upper construction, the cell certificate and the \(B-b_+\) material were not examined.