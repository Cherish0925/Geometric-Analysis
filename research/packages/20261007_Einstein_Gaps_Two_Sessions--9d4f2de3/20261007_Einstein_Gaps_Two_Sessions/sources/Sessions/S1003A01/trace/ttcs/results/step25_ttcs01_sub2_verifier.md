# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py",
    "Sessions/S1003A02/workspace/data/collapse_chiral_charge_limit.json",
    "Sessions/S1003A02/workspace/data/einstein_bolt/series_n1.json",
    "Sessions/S1003A02/workspace/scripts/ach_projected.py",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md"
  ]
}
```

## Task

Independently verify the controlled-collapse chiral charge limit and the claimed small-bolt matching orders. Read the exact symbolic charge script, its output, the regular Einstein bolt series, and the scale-free coordinate definitions. Decide precisely what follows from smooth bolt regularity alone, what additionally requires a finite-curvature/controlled F-structure matching hypothesis, and whether x=O(z^3), chi=O(z), eta=O(z) is justified at the scale-one collapsed entry. Derive the leading orders and identify any hidden coordinate or slot assumptions. Do not invent results; give equations and a concise mathematical memo.

## Output

# Memo: controlled-collapse chiral charge and small-bolt matching orders

## 0. Summary

- **The symbolic limit is correct.** Under the stated ansatz (4), the script's formula (5), \(\mathfrak b_+^{\rm end}=-2-(C+4X)^2\), is exactly right. The underlying mechanism is an exact algebraic identity, given in §1.
- **The bolt is not a controlled end.** Smooth bolt regularity alone places the bolt outside ansatz (4). There, \(p\) and \(\eta\) diverge like \(z^{-2}\) and the charge is \(1\).
- **"Finite curvature" is mislabelled.** The conditions \(x=O(z^3)\), \(\chi=O(z)\) express bounded orbit connection coefficients and bounded second fundamental form. Bounded curvature is stronger: it forces \(X=C=0\), so \(\mathfrak b_+^{\rm end}=-2\) exactly.
- **\(X\) and \(C\) are the two Kaluza–Klein amplitudes of a massive anisotropy mode.** The charge sees only the growing amplitude. A regular bolt feeds only the growing amplitude, so regular data lie on the line \(C=+4X\). That line is opposite to the kernel direction \(C=-4X\) tested numerically.
- **Bounded first jets alone do not give the \(-2\) ceiling.** With raw \(O(1)\) first jets, a cubic term appears that can push the charge above \(-2\).

Details follow.

---

## 1. Verification of the symbolic charge limit

### Conventions recovered from the script

- The metric is \(g=dt^2+\sum a_i^2\sigma_i^2\) with \(d\sigma_i=2\sigma_j\wedge\sigma_k\). Flat space is \(a_i=t\).
- Normalized radii are \(\hat a_i=a_i/r\), with \(r=(a_fa_ga_h)^{1/3}\).
- The script's `pf = af*(p+2*xi/3)` equals \(a_f'\) exactly when \(p=r'\) and \(\xi=r\beta'\), where \(\chi=rx'\) and \(\eta=rq'\).
  - So the note's "\(p=rh'\)" must mean \(h=\log r\).
  - This clashes with the slot label \(h\). The intended meaning is \(p=r'\).
- The charge variables are
\[
u_i=a_i'-\gamma_i,\qquad \gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad \mathfrak b_+=2-\textstyle\sum u_i^2-\prod u_i .
\]

### Checks of the normalization

| Case | \(u\)-values | \(\mathfrak b_+\) |
|---|---|---|
| Flat space | \(u=0\) | \(2\) |
| \(O(-1)\) bolt, slot 3 (series in `series_n1.json`) | \(u_3=1-2=-1\); \(u_{1,2}=O(t)\) | \(1\) |

For the bolt, the second row uses \((a_2^2-a_1^2)/(a_2a_3)\approx-2dt^3\) and \(a_3/a_2\to0\). Both rows agree with the stated orientation.

### Exact identity

Put \(\varepsilon_h=u_h+2\). Then
\[
\boxed{\mathfrak b_+=-2-(u_f-u_g)^2+\varepsilon_h(4-\varepsilon_h)-\varepsilon_h\,u_fu_g.}\tag{A}
\]
Under (4), the leading terms are:
- \(\gamma_h=2\cosh x-z^6e^{-x}\to2\);
- \(a_h'=O(z^3)\);
- \(\gamma_f=(1-e^{2x})/z^3+z^3\to-2X\), and \(\gamma_g\to2X\);
- \(a_f'\to P+\tfrac{2C}3+\tfrac N3\), and \(a_g'\to P-\tfrac C3+\tfrac N3\).

Hence \(\varepsilon_h\to0\), \(u_f u_g=O(1)\), and \(u_f-u_g\to C+4X\). This reproduces (5).

The \(o(\cdot)\) remainders in (4) contribute \(o(1)\), so (5) holds with little-\(o\) corrections, not only for the exact ansatz.

### Other checks

- **Exact ALF/Taub-NUT asymptotics.** With \(a_f=a_g\sim t\) and \(a_h\to\) const, one finds \(z^3=a_h/a_g\), \(r'=\tfrac23z\), and \(rq'=z\). So \(P=2/3\), \(N=1\), \(X=C=0\), and \(u_f=u_g=1\), \(u_h=-2\), giving \(\mathfrak b_+=-2\). This confirms the Berger value on a genuine U(1)-invariant end.
- **Slot symmetry.** Under \(f\leftrightarrow g\): \(x\to-x\), \(C\to-C\), and \(N\to N+C\) (because \(q\to q+x\)). Both \((C+4X)^2\) and the script's \((6P+C+2N)^2\) are invariant, as they must be.
- **The script's \(\mathfrak b_-\).** It is defined only by a comment, as \(2-\sum u^2+\prod u\), i.e. the plus formula evaluated on \(-u\). No derivation is supplied that this is the opposite-orientation charge.
  - Reversing \(t\) at fixed \(S^3\) orientation sends \(u_i\to-(a_i'+\gamma_i)\), not \(-u_i\).
  - It does not enter (5) or (6). The sentence "N enters the opposite chiral charge" rests on this unchecked definition.

---

## 2. What smooth bolt regularity alone gives

### The anisotropy mode

From `series_n1.json` (bolt in slot 3):
- \(a_{1,2}=b+\tfrac{3b^2+2}{2b}t^2+\dots\) and \(a_3=t-\tfrac{2}{3b^2}t^3+\dots\);
- the only free anisotropy is \(d=p_4-q_4\).

The listed free symbols are \(q_4,q_6\). In fact \(p_4\) and \(q_4\) are expressed through \(q_6\), and \(d\) is affine in \(q_6\). The file also gives
\[
p_6-q_6=\frac{9b^2+34}{30b^2}\,d .
\]
So the anisotropy is a single mode,
\[
\delta=\log\frac{a_1}{a_2}=\frac{d\,t^4}{b}\Big(1+\frac{4-36b^2}{30b^2}t^2+\dots\Big).
\]

**Independent hand check.** The exact Einstein difference equation (the `rhs_md` identity, with \(\Lambda\) cancelling) is
\[
x''+Sx'=\frac{8\sinh 2x}{a_h^2}-\frac{8\sinh x}{a_fa_g}. \tag{B}
\]
Linearizing near the bolt gives \(x'' + (\tfrac1t+\tfrac{8t}{3b^2})x'=(\tfrac{16}{t^2}+\tfrac{40}{3b^2})x\). With \(x=t^4(1+kt^2)\) this yields \(k=2/(15b^2)\). That agrees with the series at leading order in \(b^{-2}\).

The series coefficients have the form "scale-\(b\) Ricci-flat term \(\times(1+O(b^2))\)", e.g. \(p_2=b^{-1}+\tfrac32b\) and \(r_5\propto(53+72b^2+27b^4)/b^4\). So the bolt zone is a Ricci-flat profile at scale \(b\), with relative \(\Lambda\)-corrections of order \(b^2\).

### Orders in the scale-free variables near the bolt (\(t\ll b\), \(h=3\), \(z^3=t/b\))

\[
x=d\,b^3z^{12},\quad \chi=4d\,b^3z^{10},\quad \eta=-z^{-2}(1+O(z^6)),\quad p=\tfrac13z^{-2},\qquad \mathfrak b_+\to1 .
\]

So \(z\to0\) at the bolt is the closing limit (\(a_h'\to1\)), not a Berger end. Here \(p\) and \(\eta\) are unbounded, and the large contributions in \(p+\tfrac{2\xi}3\) cancel to give \(a_f'\to0\).

**Consequence.** Ansatz (4) cannot be read off from regularity. It concerns a different region, namely the collapsed zone at \(a_g\asymp1\).

### Monotonicity from (B)

Write \(V=a_fa_ga_h\). Equation (B) gives
\[
(Vx')'=8V\sinh x\left(\frac{2\cosh x}{a_h^2}-\frac1{a_fa_g}\right).
\]
At the bolt \(Vx'\to0\). Hence, for \(d>0\), \(x\) is positive and strictly increasing on the whole region \(\{a_h^2<2a_fa_g\cosh x\}\), which contains the bolt zone and every collapsed zone. A regular bolt with \(d\ne0\) never returns toward \(x=0\) while collapsed.

---

## 3. Hidden assumption: what (4) actually encodes

Take an orbit with \(a_g\asymp1\), \(a_h=a_gz^3\), and second fundamental form \(\mathrm{II}=\mathrm{diag}(y_i)\), \(y_i=a_i'/a_i\). Using \(r=a_ge^{x/3}z\), the following equivalences are exact.

**First jets and connection coefficients:**
- \(\chi=r(y_f-y_g)\), \(\eta=r(y_g-y_h)\), and \(p=rS/3\). Hence
\[
p,\chi,\eta=O(z)\iff|\mathrm{II}|=O(1).
\]
- \(\gamma_f=(1-e^{2x})/z^3+z^3\). Hence
\[
x=O(z^3)\iff\gamma_f,\gamma_g=O(1),
\]
i.e. bounded connection coefficients.

**Curvature:**
- Intrinsic orbit Ricci (Milnor): \(\mathrm{ric}_{ff}=\dfrac{2[e^{4x}-(1-z^6)^2]}{a_g^2e^{2x}z^6}\approx\dfrac{8X}{a_g^2z^3}\) when \(x=Xz^3\).
- The Codazzi component \(R(e_h,e_f,e_g,n)\) contains \(\mu_h(y_f-y_g)\) with \(\mu_h\approx2/a_h\).

So bounded orbit curvature together with bounded ambient curvature requires
\[
x=O(a_h^2)=O(z^6),\qquad x'=O(a_h)\ \Rightarrow\ \chi=O(z^4).
\]
In other words \(X=C=0\), and then \(\mathfrak b_+^{\rm end}=-2\) exactly, for any \(P\) and \(N\).

**Two consequences.**
1. The docstring's "finite orbit curvature requires \(x=Xz^3\)" is incorrect. Only the orbit scalar curvature stays bounded, because \(\mathrm{ric}_{ff}+\mathrm{ric}_{gg}\) cancels at order \(x/z^6\).
2. Data with \(X\ne0\) or \(C\ne0\) carry curvature of order \(1/a_h\). This is small on the fibre scale but unbounded at scale one. Physically, the anisotropy is a charge-2 Fourier mode along the collapsing fibre: amplitude \(x\) with wavelength \(\sim a_h\) gives first derivatives \(\sim x/a_h\) and curvature \(\sim x/a_h^2\).

**Status of (5)–(6).** The bound is valid on this larger \(C^1\)-controlled class, so it is the stronger statement. Its content beyond the value \(-2\) lives entirely in collapse with curvature concentrating like \(1/a_h\).

---

## 4. The scale-one entry: Kaluza–Klein structure and the regular-bolt line

### The two amplitudes

In a collapsed zone, (B) linearizes to \(x''+Sx'\approx(16/a_h^2)x\): a massive mode with mass \(4/a_h\). With \(|a_h'|\ll1\), its WKB form is
\[
x\approx z^3\big(X_+e^{4\int dt/a_h}+X_-e^{-4\int dt/a_h}\big).
\]
Using \(\chi=r x'\approx a_g z x'\) and \(r/a_h=z^{-2}\),
\[
C=4(X_+-X_-),\qquad C+4X=8X_+,\qquad C-4X=-8X_- .
\]
Therefore
\[
\boxed{\mathfrak b_+^{\rm end}=-2-64X_+^2 .}
\]
The kernel \(C+4X=0\) is exactly the decaying Kaluza–Klein mode. Equivalently, \(u_f-u_g\approx a_g(x'+4x/a_h)\): the plus charge sees the factor \((\partial_t+4/a_h)\) of \(\partial_t^2-16/a_h^2\).

### The regular bolt lies on the growing line

By the monotonicity in §2, the regular bolt solution enters the collapsed zone with \(x\) and \(x'\) of the same sign and growing. The decaying component is suppressed by \(e^{-8\int dt/a_h}\) relative to the growing one. Hence, at any entry section inside the collapsed zone,
\[
C=4X\big(1+O(z^3)+O(e^{-8\int dt/a_h})\big),\qquad \mathfrak b_+^{\rm end}\approx-2-64X^2 ,
\]
and the Q″ price is \(\ge4+64X^2\).

**Relation to the numerics.** The tested "kernel" run \((X,C)=(1,-4)\) is the pure decaying mode. It is not reachable from regular bolt data through a collapsed zone. The regular direction is \((1,+4)\), with limiting \(\mathfrak b_+=-66\). A saturation run along \((1,+4)\) is the direct numerical counterpart of regular anisotropic entry.

### Orders at the entry

From the exponential amplification across the collapsed zone (where \(a_h\approx\) const \(\sim b\)):
\[
x_{\rm entry}\sim d\,b^3\cdot\exp\Big(4\!\int_{\rm bolt\ zone}^{\rm entry}\frac{dt}{a_h}\Big)\cdot(\text{algebraic}),\qquad \int\frac{dt}{a_h}\sim\frac{1}{b}.
\]
With \(z^3\sim b\), the condition \(x=O(z^3)\) requires
\[
|d|\,b^3\lesssim b\,e^{-\kappa_0/b}.
\]
Here \(\kappa_0\) is set by the asymptotic fibre length of the scale-\(b\) Ricci-flat bolt profile. It is not computed in the supplied files.

### What is and is not justified at the entry

| Condition | Status |
|---|---|
| \(\eta,p=O(z)\) | Equivalent to \(\lvert\mathrm{II}\rvert=O(1)\) at \(a_g\asymp1\). For the U(1)-invariant family (\(d=0\)), \(x\equiv0\) gives \(X=C=0\) identically; in the Ricci-flat collapsed zone \(P=2/3+O(b/t)\), \(N=1+O(b/t)\). In the \(\Lambda\)-zone \(P,N\) stay finite but are not universal. Bolt regularity does not prove this for the actual small-bolt Einstein family. It is a matched-asymptotics statement: the rescaled bolt zone converges to the Ricci-flat profile, which the \(1+O(b^2)\) series structure supports, and the outer zone is a bounded-II collapsed limit. |
| \(x=O(z^3)\), \(\chi=O(z)\) | Not implied by regularity. It is an exponential tuning of the free parameter \(d\) against \(b\). When it holds, it forces \(C\approx4X\). |

### Prediction for the ACH1 branch

ACH1 has its fibre in slot 1 while the bolt is in slot 3, so \(x\to\infty\) is required there. The derivation predicts
\[
\log|d_\star(b)|\approx-\kappa_0/b+O(\log b),
\]
which can be compared directly against `ach_family_summary.csv`.

The continuation code interpolates \(\log d\) against \(\log b\). That is a power-law model, which would track an \(e^{-\kappa_0/b}\) law poorly. If the data instead show a power law, the collapsed plateau \(a_h\approx\) const is not forming before \(x\) becomes \(O(1)\), which would be informative in itself.

---

## 5. Raw first jets: exactly where the \(-2\) ceiling comes from

Identity (A) shows that \(\mathfrak b_+\le-2+o(1)\) needs three things:
- \(x\to0\), so that \(\gamma_h\to2\);
- \(a_h'\to0\);
- \(\varepsilon_hu_fu_g\to0\).

Take raw limits \(p\to P_0\), \(\eta\to N_0\) with \(x=Xz^3\) and \(\chi=Cz\). Then \(u_f,u_g\approx z^{-1}(P_0+N_0/3)\) and \(\varepsilon_h\approx z^2(P_0-\tfrac23N_0)\), so
\[
\boxed{\mathfrak b_+^{\rm end}=-2-(C+4X)^2-\Big(P_0+\frac{N_0}3\Big)^2\Big(P_0-\frac{2N_0}3\Big).}
\]

- **Raw \(\chi\).** \(\chi\to C_0\ne0\) adds \(-C_0^2/z^2\).
- **Raw \(x\).** \(x\to x_0\ne0\) gives \(\mathfrak b_+\approx-z^{-6}\cdot\big[4\sinh^2x_0(e^{x_0}+1)^2+8(\cosh x_0-1)e^{x_0}\sinh^2x_0\big]\). Both of these drive the charge to \(-\infty\). This agrees with the reported costs of 221–361 for raw \(x=\pm0.25\).
- **Raw \(\eta\) and \(p\).** These enter only through a sign-indefinite cubic term. The plus charge exceeds \(-2\) exactly when \(P_0<\tfrac23N_0\). This is the precise algebraic reason \(\eta\) is the dangerous coordinate.

If the reported "raw \(\Delta\eta=-8\)" means \(N_0=-8\) with \(P_0\approx0\), the formula gives \(\mathfrak b_+\to-2-1024/27\). The limiting price would then be about \(41.9\), consistent with the cost rising from \(0.545\) to \(2.94\) between \(\varepsilon=1/16\) and \(1/32\). This reading depends on how \(\Delta\eta\) and \(\varepsilon\) map to \(N_0\) and \(z\), which the supplied files do not fix.

---

## 6. Minor coordinate and slot items

- \(z\) is normalized by \(a_g\) rather than \(\sqrt{a_fa_g}\). This is immaterial once \(x\to0\).
- The labels \(f\) and \(g\) are interchangeable by the symmetry in §1.
- The bolt slot must be \(h\) for (4) to describe the small-bolt collapsed zone. In `ach_projected.py`, the ACH fibre slot \(f=1\) differs from the bolt slot 3. The Q″ entry and the ACH end therefore use different slot assignments, and the high-shear growth of \(x=\log(a_1/a_2)\) connects them.
- **Possible consistency test (conditional).** This assumes the bulk terms in (1) are the only change of \(\widehat P\) on Einstein annuli, which the supplied files do not fix. Then (1) forces \(\mathfrak b_+\) to decrease along an Einstein collapsed zone by \(\tfrac{1}{2\pi^2}\int|W^+|^2\) plus the \(s^2\) term. That would be consistent with \(-2-64X(t)^2\) decreasing as \(X\) grows. A direct numerical comparison of \(\Delta\mathfrak b_+\) with \(\int|W^+|^2\) along an anisotropic regular-bolt orbit would test the whole chain.