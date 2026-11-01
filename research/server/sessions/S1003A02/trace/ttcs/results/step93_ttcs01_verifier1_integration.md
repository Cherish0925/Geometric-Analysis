# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step93_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step93_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical correctness and exact scope of A01 Step-74 Theorem 74.A. Check: transfer of the smooth scalar-curvature lower bound through arbitrary A1 orbifold resolution; all characteristic-number normalizations; the weighted-mean lower bound for the human defect; the Green-football cap construction and its topology/asymptotics; exact values of P_{*,orb} and alpha_orb; equality and nonattainment statements; and what this genuinely supersedes in A02 Theorem 87.O. Pay special attention to whether the scalar lower bound needs the stated SW supply or follows unconditionally for general-type blowups from the Yamabe invariant, and to fake-projective-plane/b^+=1 scope. Give precise corrections if needed.

## Integrated Scientific Memo

# Verification memo — Theorem 74.A

## Conclusion and corrected scope

The numerical formulas in Theorem 74.A are correct, **using the inherited smooth identification (R)**:
\[
\operatorname{Res}_{\rm EH}\bigl(S^4/\mathbb Z_2\bigr)
\cong \overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}.
\]
For every compact ball quotient \(X\), including a fake projective plane, and
\[
V_m=X\#m(S^4/\mathbb Z_2),\qquad A=c_1^2(X),\qquad k=2m\ge2,
\]
one has
\[
\boxed{P_{*,\mathrm{orb}}(V_m)=8\pi^2k,\qquad
\alpha_{\mathrm{orb}}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}.}
\]
There is no Einstein orbifold metric on \(V_m\).

Two substantive corrections strengthen the statement:

1. **No additional (SW) hypothesis is needed.** The scalar lower bound follows from the smooth resolution’s Yamabe invariant, unconditionally for general-type blow-ups and all \(b^+\).
2. **The attainment claim can be substantially sharpened:**
   \[
   \boxed{P_{*,\mathrm{orb}}(V_m)\text{ is never attained},}
   \]
   and
   \[
   \boxed{\alpha_{\mathrm{orb}}(V_m)\text{ is not attained if }k\ne A/3.}
   \]
   At \(k=A/3\), attainment is exactly the existence of a half-conformally-flat orbifold metric with constant negative scalar curvature. The supplied material does not decide this existence question.

The nonattainment improvement follows from a short variational argument given below; neither branch completed that argument.

---

## 1. Transfer of the scalar bound through resolution

The supplied full text of LeBrun, *Kodaira Dimension and the Yamabe Problem*, Theorem 2, states
\[
\mathcal Y(X\#k\overline{\mathbb{CP}}^{\,2})
=-4\pi\sqrt{2c_1^2(X)}
\]
for every general-type surface and its blow-ups. Lemma 1 and Proposition 1 there imply
\[
\int s^2\ge32\pi^2A
\]
for every smooth metric on the resolution. More strongly, the Yamabe quotient and Hölder give
\[
-\|s^-_{\widetilde g}\|_2
\le Y([\widetilde g])
\le\mathcal Y(M_k)=-4\pi\sqrt{2A},
\]
hence
\[
\int_{M_k}(s^-_{\widetilde g})^2\ge32\pi^2A.
\tag{1}
\]

For an **arbitrary smooth orbifold metric** \(g\), use equivariant normal coordinates at each \(A_1\) point:
\[
g=\delta+O(r^2),\qquad \partial^j(g-\delta)=O(r^{2-j}),\quad j\le2.
\]
Insert a scaled, orientation-matched EH metric whose end satisfies
\[
h-\delta=O(r^{-4})
\]
with two derivative bounds. With scale \(\varepsilon\) and cutoff radius
\[
\rho=\varepsilon^{2/3},
\]
the annular metric error is
\[
O\!\left(\rho^2+(\varepsilon/\rho)^4\right)=O(\rho^2).
\]
Its second derivatives, and therefore its curvature, are \(O(1)\); the annular volume is \(O(\rho^4)\). The exact filler is Ricci-flat. Thus
\[
S(g_\varepsilon)\to S(g),\qquad P(g_\varepsilon)\to P(g),
\]
and also
\[
\int(s^-_{g_\varepsilon})^2\to\int_{V_m}(s^-_g)^2.
\]
Passing (1) to the limit yields
\[
\boxed{\int_{V_m}(s^-_g)^2\ge32\pi^2A.}
\tag{2}
\]

This transfer does not require the denominator condition \(R>0\) in Lemma 86.S: that condition concerns continuity of \(\mathscr D\), not convergence of scalar or Ricci energies.

**Exact meaning of “arbitrary resolution.”** The argument works for every orbifold metric, using the chosen EH resolution that gives \(M_k\). It does not assert that every possible orientation or filling choice has a general-type smooth target. One compatible resolution suffices to constrain the original orbifold metric.

**Topological qualification.** The supplied package records the smooth identification (R) via its \(T^2\)-equivariant/Orlik–Raymond input. Characteristic numbers and Freedman alone do not prove a diffeomorphism. Accordingly, the verification of the scalar transfer retains (R) as an inherited smooth-topological input, rather than claiming that the displayed characteristic-number calculation independently proves it.

---

## 2. Characteristic numbers and all constants used in 74.A

Here \(I_\pm\) use the Weyl endomorphism norm, while \(P\) uses the ordinary symmetric-tensor norm of \(\operatorname{Ric}^\circ\). These conventions give
\[
16\pi^2\chi_{\rm orb}=S/12+2W-P,\qquad
12\pi^2\tau_{\rm orb}=I_+-I_-,
\quad W=I_++I_-.
\tag{3}
\]
They agree with the chiral identity in the supplied LeBrun paper.

For the ball quotient,
\[
\chi(X)=A/3,\qquad \tau(X)=A/9.
\]
For the football \(O=S^4/\mathbb Z_2\),
\[
\chi_{\rm orb}(O)=1,\qquad \tau_{\rm orb}(O)=0.
\]
The \(A_1\) link has \(\eta(\mathbb{RP}^3)=0\). Regular-point connected sum subtracts two from Euler characteristic, so
\[
\chi_{\rm orb}(V_m)=A/3-m=A/3-k/2,\qquad
\tau_{\rm orb}(V_m)=A/9.
\]
Consequently,
\[
T_+(V_m)=A-k,\qquad T_-(V_m)=A/3-k.
\tag{4}
\]

For the smooth resolution,
\[
\chi(M_k)=A/3+k,\qquad \tau(M_k)=A/9-k.
\]
Each complex-oriented EH filler has
\[
(c_+,c_-)=(0,-6),\qquad I_+=0,\quad I_-=12\pi^2.
\]
Thus \(C_+=0,\ C_-=-6k\), and the general charge ledger reproduces (4). The Euler increment is \(3/2\) per point, hence \(3m\) in total.

Signature gives
\[
W\ge I_+-I_-=\frac{4\pi^2A}{3}.
\]
Writing
\[
\sigma=S-32\pi^2A\ge0,\qquad
w=W-\frac{4\pi^2A}{3}=2I_-\ge0,
\]
equation (3) gives exactly
\[
P=8\pi^2k+\frac{\sigma}{12}+2w,
\qquad
R=P+S/4=8\pi^2(A+k)+\frac{\sigma}{3}+2w.
\tag{5}
\]
All coefficients in the lower-bound proof are correct.

---

## 3. Weighted mean and Einstein exclusion

Set \(b=4k/(A+k)\). Equation (5) implies
\[
\frac{4P}{R}
=
\frac{
b\,8\pi^2(A+k)+1\cdot(\sigma/3)+4\cdot(2w)
}{
8\pi^2(A+k)+\sigma/3+2w
}.
\]
This is the stated weighted mean of \(b,1,4\), with nonnegative weights and a strictly positive first weight. Therefore
\[
\mathscr D=\frac{4P+L_s}{R}\ge
\min\{1,b\}.
\]
Also \(P\ge8\pi^2k>0\), excluding Einstein metrics of every sign, including Ricci-flat ones.

The stronger scalar transfer (2) makes \(R>0\) automatic throughout this variational domain.

---

## 4. Green-football cap: curvature, topology and recovery

For
\[
h=(1+r^{-2})^2\delta
\quad\text{on }\mathbb R^4\setminus\{0\},
\]
the conformal factor is harmonic, so \(s_h=0\); conformal flatness gives \(W_h=0\). Direct computation yields
\[
|\operatorname{Ric}^\circ_h|^2
=\frac{192r^8}{(1+r^2)^8},
\qquad
d\mu_h=2\pi^2\frac{(1+r^2)^4}{r^5}\,dr.
\]
Hence
\[
P(h)=384\pi^2\int_0^\infty\frac{r^3}{(1+r^2)^4}\,dr
=32\pi^2,
\]
and
\[
P(h;\ r>R)
=\frac{\pi^2(96R^2+32)}{(1+R^2)^3}
=\frac{96\pi^2}{R^4}+O(R^{-6}).
\]
Moreover,
\[
|\operatorname{Ric}^\circ_h|
=8\sqrt3\,r^{-4}+O(r^{-6}).
\]
These agree with the script and JSON.

The involution
\[
\iota(x)=\frac{\sigma x}{|x|^2},
\qquad \sigma=\operatorname{diag}(-1,-1,-1,1),
\]
is an orientation-preserving isometry: inversion and \(\sigma\) each reverse orientation. Its fixed points are \(\pm e_4\), and its differential there is \(-I\). It exchanges the two AE ends.

The two-point compactification is the round \(S^4\); on it the involution is the standard rotation with two isolated fixed points. Its quotient is \(O\), and the exchanged end pair becomes one regular point. Thus
\[
G=(\mathbb R^4\setminus0,h)/\iota
\]
is \(O\) minus a regular point, with two \(A_1\) singularities and one ordinary AE end. Degree-two integration gives
\[
P(G)=16\pi^2.
\]
For \(R>1\), the quotient end is represented one-to-one by \(r>R\); its omitted tail is therefore the full one-end tail above, not half that tail. The noncompact Euler check
\[
0=\chi_{\rm orb}(G)=1-\frac{P(G)}{16\pi^2}
\]
also agrees.

**Minor notation repair:** the compact truncated cap is the complement of the AE region \(r>R\) in \(G\). The notation “\(\{|x|\le R\}\subset G\)” should be interpreted this way; \(r\) is not globally invariant under \(\iota\).

After scaling and putting \(y=\varepsilon x\), the cap end is
\[
\left(1+\frac{\varepsilon^2}{|y|^2}\right)^2\delta.
\]
On the interpolation annulus, with \(\rho=\varepsilon^{1/2}\),
\[
\partial^j(g_X-\delta)=O(\rho^{2-j}),\qquad
\partial^j(g_{\rm cap}-\delta)=O(\varepsilon^2\rho^{-2-j}),
\quad j\le2.
\]
Curvature is \(O(1)\) on volume \(O(\varepsilon^2)\); omitted cap energy is \(O((\varepsilon/\rho)^4)=O(\varepsilon^2)\). The compact cap volume shrinks, while its scalar and Weyl curvatures vanish. Therefore
\[
P\to16\pi^2m=8\pi^2k,\quad
S\to32\pi^2A,\quad
W\to4\pi^2A/3,\quad L_s\to0,
\]
and
\[
\mathscr D\to\frac{4k}{A+k}.
\]
The topology is precisely \(X\#mO\).

The regular-point dumbbell construction supplies the other recovery value. On a unit \(S^3\times[0,L]\),
\[
s=6,\quad |\operatorname{Ric}|^2=12,\quad
|\operatorname{Ric}^\circ|^2=3.
\]
Both \(4P\) and \(R\) grow as \(24\pi^2L\), whereas \(L_s=O(1)\). Thus \(\mathscr D\to1\). These two constructions prove both exact infima.

---

## 5. Equality and the missing nonattainment argument

The source’s algebraic equality conditions are correct, but its statement that attainment remains open for \(k<A/3\) is too weak.

### No \(P\)-minimizer exists, for any \(k\)

If \(P=8\pi^2k\), equation (5) forces
\[
S=32\pi^2A,\qquad W^-=0.
\tag{6}
\]
Such a metric would be a global \(P\)-minimizer and hence stationary under all smooth orbifold metric variations.

Orbifold Gauss–Bonnet gives
\[
P=2W+S/12-16\pi^2\chi_{\rm orb}.
\tag{7}
\]
Since \(W\) is conformally invariant, conformal stationarity of \(P\) implies conformal stationarity of \(S\), hence
\[
\Delta s=0.
\]
Integration by parts on the compact orbifold gives \(s\) constant. By (2) and (6), this constant is strictly negative.

Next, signature gives for every variation
\[
W=2I_-+12\pi^2\tau_{\rm orb}.
\]
At \(W^-=0\), the first variation of \(I_-=\int|W^-|^2\) vanishes. Therefore \(\delta W=0\) for every metric variation. At constant scalar curvature,
\[
\delta S(h)=-2s\int\langle\operatorname{Ric}^\circ,h\rangle\,d\mu.
\]
Equation (7) and stationarity now imply
\[
0=\delta P(h)
=-\frac{s}{6}\int\langle\operatorname{Ric}^\circ,h\rangle\,d\mu
\]
for every \(h\). Since \(s\ne0\), this forces \(\operatorname{Ric}^\circ=0\), contradicting \(P=8\pi^2k>0\).

Thus
\[
\boxed{P(g)>8\pi^2k\quad\text{for every individual orbifold metric}.}
\tag{8}
\]
This proof needs neither mixed-inequality equality theory nor an orbifold monopole rigidity theorem. Equivalently, the proposed half-conformally-flat, constant-scalar \(P\)-critical non-Einstein object cannot exist: half-conformal flatness makes the Weyl functional stationary, so \(P\)-criticality at nonzero constant scalar forces Einstein.

### Consequences for \(\alpha_{\rm orb}\)

- **If \(k<A/3\):** equality in the weighted mean requires \(\sigma=w=0\), and equality in \(\mathscr D\ge4P/R\) requires \(L_s=0\). In particular it requires equality in the \(P\)-bound, impossible by (8). Thus \(\alpha_{\rm orb}\) is not attained.
- **If \(k>A/3\):** the positive fixed weight multiplies \(4k/(A+k)>1\); hence every metric has \(\mathscr D>1\). The value \(1\) is not attained. This also follows from \(T_-=A/3-k<0\) using signature alone.
- **If \(k=A/3\):**
  \[
  \mathscr D=1\iff w=0,\ L_s=0
  \iff W^-=0,\quad s\text{ constant}.
  \]
  Equation (2) forces \(s<0\). Here \(\sigma\) need not vanish; indeed (8) forces \(\sigma>0\) for any attaining metric. This remaining existence problem is not settled by the supplied sources.

The mixed-transfer calculation in the original equality paragraph is numerically correct: a hypothetical \(P\)-minimizer would satisfy
\[
|W^+|^2=s^2/24.
\]
But it is only a necessary condition for an object now shown not to exist.

---

## 6. Fake-projective-plane and \(b^+=1\) scope

There is no fake-plane exclusion from 74.A.

The scalar argument uses LeBrun’s Yamabe theorem, whose supplied statement covers all general-type surfaces. Thus no chamber qualification is required.

The mixed estimate also has an all-\(b^+\) source already present:
LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Theorem 2.3 and the class-selection argument in Proposition 3.2 give
\[
\int(s-\sqrt6|W^+|)^2\ge72\pi^2A.
\]
The factor follows by multiplying Theorem 2.3 by \(9/4\). Its proof selects a suitable polarized monopole class metric-wise, including when \(b^+=1\). One need not assert that all signed blow-up classes are globally chamber-independent monopole classes.

Accordingly, replace the (SW) box by the two established smooth curvature inputs and their citations. The arithmetic that \(b^+(X)=1\) forces a ball quotient to have \(A=9,\ p_g=q=0\) is correct, but does not create an unresolved chamber exception.

---

## 7. What genuinely supersedes Theorem 87.O

The Weyl-deficit formula remains correct and unchanged:
\[
d_{*,\rm orb}(V_m)
=4\pi^2(A/3-k)=4\pi^2(A/3-2m).
\]
Indeed, the cap family realizes \(\inf W=4\pi^2A/3\). Its lower-bound relation to 74.A is transparent:
\[
P=S/12-2d
\ge32\pi^2A/12-8\pi^2(A/3-k)=8\pi^2k.
\]

What changes is the Einstein and variational interpretation:

- Replace “Einstein \(V_m\) requires \(2m<A/3\)” by **“no Einstein orbifold metric exists on \(V_m\) for any \(m\ge1\)”**.
- The cap construction controls \(P,S,L_s\) simultaneously, beyond the Weyl-energy recovery used in 87.O.
- The exact \(P\)- and human-defect infima, with the corrected nonattainment conclusions, are new information.
- Any invariant Einstein metric on the stated double cover would descend to \(V_m\), so this also excludes the corresponding involution-invariant Einstein architecture. Under the supplied covering identification,
  \[
  P_*^\iota=2P_{*,\rm orb}=32\pi^2m,\qquad
  \alpha^\iota=\min\{1,8m/(A+2m)\}.
  \]

The weaker Einstein clause requires correction in A02 §22.6(6), §24.1(4), §24.4 and the corresponding front-matter passages.

This does **not** exclude smooth Einstein metrics on \(M_k\), other orbifold topologies, or other absorption patterns. Nor does it give the orbifold lower bound to smooth competitors: supplied finite-scale constructions give
\[
P_*(M_k)<8\pi^2k.
\]
It does exclude a smooth-orbifold regular-locus limit on this fixed \(V_m\) for a \(P\)-minimizing sequence on \(M_k\): nonnegative-energy lower semicontinuity would give
\[
\liminf P(g_i)\ge P(g_\infty)\ge8\pi^2k>P_*(M_k).
\]
No bubble-energy identity is needed for that consequence.

**Remaining exact scientific object:** only the threshold attainment question in this paired-\(A_1\) variational problem remains undecided:
\[
k=A/3,\qquad
\exists\,g\text{ on }V_m\text{ with }W^-=0,\ s\equiv\text{constant}<0?
\]
The exact values and all other attainment assertions above are settled by the supplied inputs and the variational argument.