# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step72_verification_bundle.md",
    "Sessions/S1003A02/workspace/scripts/step72_weyl_deficit_identity.py",
    "Sessions/S1003A02/workspace/data/step72_weyl_deficit_identity.json",
    "Sessions/S1003A02/workspace/scripts/step72_dumbbell_numeric.py",
    "Sessions/S1003A02/workspace/data/step72_dumbbell_numeric.json"
  ]
}
```

## Task

Verify every statement (A)–(G) in this focused bundle. Check constants, conformal/Yamabe quantifiers, Ricci-flat boundary cases, dumbbell smoothness and O(1) estimates, connected-sum deficit arithmetic, the #n CPbar2 threshold, the general-type KE deficit, and the conversion to the W+ inequality in the stated endomorphism norm. Give corrected statements and concise proofs wherever needed. Do not assume the desired result.

## Output

# Verification memo: Step 72 statements (A)–(G)

**Summary.** The identities (A), (B), (E) and (F) and the inequality (G) are correct. Three repairs are needed:

1. **Ricci-flat metrics.** At \(R=0\) the functional equals 4, not \(0/0\).
2. **Non-Yamabe metrics in (D).** The reduction to the Yamabe representative needs the inequality \(S\ge Y^2\) inside every conformal class. For \(Y<0\) this is a separate lemma, not stated in the bundle.
3. **Signature of a blow-up.** The bundle's intermediate formula for \(\tau(X\#k\overline{\mathbb{CP}}^2)\) is off by a factor 3. The final form of (G) is nonetheless correct.

Some statements can be sharpened. The signature bound gives \(d\le 4\pi^2T_{\min}\) directly, so the "chiral lower bound" is not needed. The value \(d_*(\#_n\overline{\mathbb{CP}}^2)\) is determined exactly. The attainment statement needs the correct orientation half, and full conformal flatness when \(\tau=0\). Combining (D) with the LeBrun scalar estimate gives a positive lower bound on \(\alpha\) in part of the band.

## 1. Convention check

At round \(S^4\): \(s=12\) and \(V=8\pi^2/3\), so \(S=384\pi^2\) and \(S/24=16\pi^2=8\pi^2\chi\). The standard Gauss–Bonnet formula in the \((0,4)\)-tensor norm is
\[
32\pi^2\chi=\int\big(|W|_t^2-2|\mathrm{Ric}^\circ|^2+s^2/6\big).
\]
Dividing by 4 gives the session formula with \(|W|^2=|W|_t^2/4\), which is the endomorphism norm on \(\Lambda^2\). The signature formula \(48\pi^2\tau=\int(|W^+|_t^2-|W^-|_t^2)\) becomes \(12\pi^2\tau\), as stated.

A useful cross-check: \(8\pi^2\chi+12\pi^2\tau=\int(2|W^+|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)\). This is LeBrun's normalization, so the session norm equals LeBrun's.

## 2. The functional \(\mathcal E\) and statement (A)

Pointwise, \(|\mathrm{Ric}-\lambda g|^2=|\mathrm{Ric}^\circ|^2+(s-4\lambda)^2/4\). Hence
\[
\frac{\int|\mathrm{Ric}-\lambda g|^2}{\lambda^2V}=\frac{R}{V}\mu^2-\frac{2T_s}{V}\mu+4,\qquad \mu=1/\lambda .
\]
For \(R>0\) the minimum over \(\mu\in\mathbb R\) is \(4-T_s^2/(VR)=(4P+L_s)/R\). The value \(\mu=0\) is excluded, but the infimum is still correct: it is attained at \(\mu=T_s/R\) if \(T_s\ne0\), and equals 4 if \(T_s=0\).

**Correction for Ricci-flat metrics.** If \(R=0\) the expression is identically 4, so \(\mathcal E(g)=4\). Formula (A) is valid exactly when \(R>0\). In all cases \(0\le\mathcal E\le4\).

Derivation of (A): \(4P+L_s-R=3P-S/4+L_s\). Substituting \(3P=6\mathcal W+S/4-48\pi^2\chi\) gives
\[
\mathcal E-1=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R}.
\]
This is confirmed by the symbolic residual 0 in the JSON. Also \(L_s\ge0\) by Cauchy–Schwarz, with equality iff \(s\) is constant.

## 3. Statements (B), (C), (D)

**(B).** At a Yamabe metric, \(L_s=0\) and \(S=s^2V=Y^2\). Then
\[
R(\widehat g)=P+Y^2/4=Y^2/3-2d,\qquad \mathcal E(\widehat g)=1-6d/R(\widehat g).
\]
This is valid whenever \(R(\widehat g)>0\), which holds if \(Y\ne0\). Note that \(R(\widehat g)=Y^2/3-2d\) depends only on the conformal class, so the non-uniqueness of Yamabe minimizers when \(Y>0\) is irrelevant. Also \(P(\widehat g)\ge0\) gives \(Y^2\ge24d\).

**(C) — correct, and the hypothesis \(Y\ne0\) can be dropped.**

- *Forward.* If \(\mathcal E(g)<1\), then \(R>0\), since \(R=0\) gives \(\mathcal E=4\). With \(L_s\ge0\), (A) gives \(d>0\).
- *\(d>0\) forces \(Y\ne0\).* If \(Y=0\), the scalar-flat Yamabe metric has \(P=-2d<0\), which is impossible.
- *Converse.* If \(d>0\), then \(Y\ne0\) and (B) gives \(\mathcal E(\widehat g)<1\).

So \(\alpha<1\iff d_*(M)>0\), where \(d_*=\sup_{[g]}d\). A class with \(Y=0\) always has \(d\le0\). A Ricci-flat metric has \(d=0\) and \(\mathcal E=4\). Neither case affects (C).

**(D) — needs a missing lemma.** The bundle replaces each class by its Yamabe metric. To justify this one must show that \(\inf_{g\in[g]}\mathcal E=\mathcal E(\widehat g)\) when \(d>0\). Write
\[
\mathcal E(g)-1=\frac{L_s-6d}{S/3-2d}.
\]
For \(d>0\) and \(R(g)>0\):
\[
\mathcal E(g)-1\ \ge\ \frac{-6d}{S/3-2d}\ \ge\ \frac{-6d}{Y^2/3-2d}.
\]
The second inequality requires \(S(g)\ge Y^2\) for every \(g\) in the class.

- **Case \(Y>0\).** \(T_s/\sqrt V\ge Y>0\), so \(S\ge T_s^2/V\ge Y^2\).
- **Case \(Y<0\) (LeBrun's argument).** Write \(\widehat g=u^2g\) with \(\int u^4d\mu_g=1\) and \(\hat s\equiv Y\). The conformal change formula is \(Yu^3=6\Delta_gu+s_gu\). Multiply by \(u\) and integrate:
\[
Y=\int(6|\nabla u|^2+s_gu^2)\,d\mu_g\ \ge\ -S^{1/2}\Big(\int u^4\Big)^{1/2}=-S^{1/2},
\]
so \(S\ge Y^2\).

Classes with \(d\le0\) give \(\mathcal E\ge1\) by (A) when \(R>0\), and \(\mathcal E=4\) when \(R=0\). Together with \(\alpha\le1\) from (E), the corrected form of (D) is
\[
\alpha(M)=1-6\max\Big\{0,\ \sup_{[g]:\,d>0}\frac{d}{Y^2/3-2d}\Big\}
=1-\max\Big\{0,\sup_{d>0}\frac{18d}{Y^2-6d}\Big\}.
\]
For \(d>0\) the infimum of \(\mathcal E\) over the class is attained exactly at the Yamabe metrics, because the first inequality is strict unless \(L_s=0\).

## 4. Dumbbell (E) and the case \(T_{\min}\le0\)

**Geometry.** \(dr^2+f^2g_{S^3}=f^2(dt^2+g_{S^3})\) with \(dt=dr/f\), so the metric is conformally flat and \(W\equiv0\). The cylinder data check:

- \(\mathrm{Ric}=(0,2,2,2)\) and \(s=6\);
- \(\mathrm{Ric}^\circ=(-\tfrac32,\tfrac12,\tfrac12,\tfrac12)\), so \(|\mathrm{Ric}^\circ|^2=3\) and \(|\mathrm{Ric}|^2=12\);
- volume per unit length \(2\pi^2\), giving \(P=6\pi^2L\), \(S=72\pi^2L\), \(T_s=12\pi^2L\), \(R=24\pi^2L\).

In the script, the formulas \(k_0=-f''/f\), \(k_1=(1-f'^2)/f^2\), \(s=6(k_0+k_1)\) and the blend derivatives are all correct.

**Smoothness.** The quintic smoothstep has \(w'''\ne0\) at the ends of the blend, so the script's metric is only \(C^2\). It is adequate for the integrals but is not smooth. Replacing it by a \(C^\infty\) cutoff changes only fixed cap integrals and does not affect the asymptotics in \(L\).

**Asymptotics.** Let \(S_c,T_c,V_c,P_c\) be the fixed cap integrals. Expanding,
\[
L_s\to S_c-12T_c+36V_c=\int_{\text{caps}}(s-6)^2\,dV\approx1520.79 .
\]
The data give 1514.46 at \(L=200\), approaching this value. The cylinder contributes zero to \(3P-S/4\), since \(18\pi^2-18\pi^2=0\). Hence
\[
L(\mathcal E-1)\to\frac{3P_c-S_c/4+L_s^\infty}{24\pi^2}=\frac{573.3}{236.87}\approx2.42 .
\]
The data give 2.337 at \(L=200\), trending to this limit. The same number follows from (A): \(-96\pi^2+1520.79=573.3\). The Gauss–Bonnet residual of about \(10^{-14}\) confirms \(\chi=2\) for the caps.

**Gluing in \(M\).** The gluing happens in a fixed region independent of \(L\). All five integrals become (fixed) + \(L\cdot\)(cylinder), and \(\mathcal E=1+O(1/L)\). Therefore \(\alpha(M)\le1\) for every closed \(M\). This is correct.

**Sharpening: \(\alpha=1\) follows directly.** Since \(\mathcal W\ge|\mathcal W^+-\mathcal W^-|=12\pi^2|\tau|\),
\[
d([g])\le4\pi^2(2\chi-3|\tau|)=4\pi^2T_{\min}.
\]
So \(T_{\min}\le0\) gives \(d\le0\) for every class, hence \(\alpha\ge1\), hence \(\alpha=1\). No separate chiral bound is needed.

**Attainment.**

- *If \(T_{\min}<0\):* \(\mathcal E-1\ge-6d/R>0\) whenever \(R>0\), and \(\mathcal E=4\) when \(R=0\). So \(\alpha=1\) is never attained.
- *If \(T_{\min}=0\):* \(\mathcal E(g)=1\) forces \(R>0\), \(d=0\) and \(L_s=0\). Constant \(s\) has the sign of \(Y\). If \(Y=0\), then \(P=S/12=0\), so \(R=0\), a contradiction. Hence \(Y\ne0\). Conversely, a class with \(d=0\) and \(Y\ne0\) gives \(\mathcal E(\widehat g)=1\).

**Correction to the attainment statement.** \(d=0\) means \(\mathcal W=12\pi^2|\tau|\). This requires \(W^-\equiv0\) if \(\tau>0\) and \(W^+\equiv0\) if \(\tau<0\). If \(\tau=0\) (and hence \(\chi=0\)), it requires \(W\equiv0\), i.e. a locally conformally flat class, not merely half conformally flat.

Example: on K3 the hyperkähler class has \(W^+=0\) but \(Y=0\), so it gives \(\mathcal E=4\). Attainment on K3 therefore depends on whether some class with \(W^+\equiv0\) and \(Y<0\) exists. The supplied material does not settle this.

## 5. Connected sums (F) and \(\#_n\overline{\mathbb{CP}}^2\)

**(F).** The arithmetic is exact (JSON residual 0). Subadditivity of \(\mathcal W_*\) is a literature input attributed to Kobayashi. It also follows from a direct argument:

- In a ball of radius \(2\varepsilon\), write \(g-\delta=O(r^2)\) and cut off to the flat metric.
- The curvature on the annulus is \(O(1)\) and its volume is \(O(\varepsilon^4)\), so the Weyl energy there tends to 0.
- Join the two flat balls by a conformally flat neck (inversion); conformal invariance of \(\mathcal W\) does the rest.

**\(\overline{\mathbb{CP}}^2\).** For Fubini–Study, Gauss–Bonnet with \(P=0\) and \(\mathcal W=S/24\) gives \(S=288\pi^2\) and \(\mathcal W=12\pi^2=12\pi^2|\tau|\). Hence \(\mathcal W_*=12\pi^2\) and \(d_*=12\pi^2\). Iterating (F):
\[
d_*(\#_n\overline{\mathbb{CP}}^2)\ge12\pi^2n-16\pi^2(n-1)=(16-4n)\pi^2 .
\]
This is correct, and consistent with \(d_*(S^4)=16\pi^2\) at \(n=0\).

**Sharpening.** The signature bound gives \(d_*\le4\pi^2(2(n+2)-3n)=(16-4n)\pi^2\). Hence, for every \(n\ge0\),
\[
d_*(\#_n\overline{\mathbb{CP}}^2)=4\pi^2(4-n),\qquad \mathcal W_*=12\pi^2n=12\pi^2|\tau| .
\]

**Thresholds.**

- \(n\le3\): \(\alpha<1\). Statement (D) shows that the actual value of \(\alpha\) depends on \(Y\) through \(18d/(Y^2-6d)\), not on \(d_*\) alone.
- \(n\ge4\): \(T_{\min}=4-n\le0\), so \(\alpha=1\).
- \(n=4\): attainment is equivalent to an anti-self-dual class (\(W^+=0\), since \(\tau=-4<0\)) with \(Y\ne0\). LeBrun's explicit self-dual metrics on \(\#_n\mathbb{CP}^2\) are reported to have positive scalar curvature. If that is confirmed in the source, \(\alpha(\#_4\overline{\mathbb{CP}}^2)=1\) is attained. This is a literature input I have not verified here.

## 6. General-type KE surfaces and (G)

**KE constants.** For a Kähler–Einstein metric \(\mathcal W^+=S/24\) and \(P=0\). Signature plus Gauss–Bonnet give
\[
8\pi^2\chi=S/8-12\pi^2\tau,\qquad S=32\pi^2(2\chi+3\tau)=32\pi^2A .
\]
Then \(d=S/24=4\pi^2A/3\) and \(R=8\pi^2A\), so \(d=R/6\) and \(\mathcal E=0\). These are correct.

**Lower bound on \(d_*\).** \(d_*(X\#k\overline{\mathbb{CP}}^2)\ge4\pi^2(A/3-k)\) is correct. So \(k<A/3\) gives \(\alpha<1\).

**Signature error.** The bundle writes \(\tau(X\#k\overline{\mathbb{CP}}^2)=(A-2\chi)-k\). The correct formula, from \(A=2\chi+3\tau\), is
\[
\tau'=\frac{A-2\chi(X)}{3}-k,\qquad \chi'=\chi(X)+k,\qquad 2\chi'+3\tau'=A-k .
\]
With the bundle's formula one would get \(3A-4\chi-k\) in place of \(A-k\).

**Conversion to (G).** Using \(\mathcal W=2\mathcal W^+-12\pi^2\tau'\) for each metric:
\[
\inf\mathcal W<8\pi^2\chi'\iff 2\inf\mathcal W^+<4\pi^2(2\chi'+3\tau')\iff\inf_g\int|W^+|^2<2\pi^2(A-k).
\]
So (G) is correct in the session (endomorphism, LeBrun) norm, with the complex orientation. In the \((0,4)\)-tensor norm it reads \(\inf\int|W^+|_t^2<8\pi^2(A-k)\).

Since \(\mathcal W^+\ge0\), the band ends at \(k=A\). Independently, \(d\le4\pi^2(2\chi'-3|\tau'|)\le4\pi^2(A-k)\) whatever the sign of \(\tau'\). So \(k\ge A\) gives \(\alpha=1\).

**Additional consequence of (D) in the band.** This uses LeBrun's Seiberg–Witten estimate \(\int s^2\ge32\pi^2c_1^2(X)\) for every metric on \(X\#k\overline{\mathbb{CP}}^2\). This is a literature input; its hypotheses, such as \(b^+\ge2\) or the chamber conditions when \(b^+=1\), should be checked in the source. The estimate gives \(Y<0\) and \(Y^2\ge32\pi^2A\). Since \(18d/(Y^2-6d)\) increases in \(d\) and decreases in \(Y^2\), set \(d\le4\pi^2(A-k)\); the denominator is \(8\pi^2(A/3+k)>0\). Then
\[
\alpha(X\#k\overline{\mathbb{CP}}^2)\ \ge\ \frac{12k-8A}{A+3k}.
\]
- The bound equals 1 at \(k=A\), consistent with §4.
- It is positive for \(2A/3<k<A\).
- For \(A/3\le k\le2A/3\) it says nothing new.

There, the question of whether \(\alpha<1\) is exactly the question of whether \(\inf\int|W^+|^2<2\pi^2(A-k)\). The Seiberg–Witten inequalities couple \(s\) and \(W^+\) and do not bound \(\int|W^+|^2\) alone. Resolving the band therefore needs either a pure-\(W^+\) lower bound on blow-ups, or gluing constructions that drive \(\int|W^+|^2\) below \(2\pi^2(A-k)\).