# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/data/step105/cap_charge_check.json",
    "Sessions/S1003A01/workspace/notes/spirit_step91_global_reduction_and_carrier_scope.md"
  ]
}
```

## Task

Independently check the new A02 Theorem 105.Q/Corollaries 105.L and 105.H in the supplied note. Re-derive all signs, orientations, constants, and limiting arguments from the stated Theorem-G convention. Pay special attention to: boundary orientation in Q_+, whether C^2 boundary convergence controls eta as asserted; existence/order of the double limit defining c_j; whether volume convergence implies cap volume tends to zero; the cap contribution to LeBrun’s mixed estimate and the optimization leading to 9k+8 sum c_j <=3A; Dai–Wei’s adiabatic eta normalization; the formula c=4-r for an S3 Hopf cap; and the inference that a zero-charge -I4 cap must carry its odd form through energy-free collapse. Distinguish proved consequences under (E) from heuristic topology. If a statement needs repair, give the corrected statement and proof. Also assess whether a w2/spin or eta/Dirac argument can actually exclude the zero-charge four-class cap without assuming what is to be proved.

## Output

## Independent verification memo: Theorem 105.Q, Corollaries 105.L and 105.H

The sign convention, constants, and algebra in Step 105 are largely correct, but the analytic hypotheses need one repair: the eta part of the APS link term is not controlled by the stated \(C^2_{\rm loc}\) convergence alone. Under a strengthened convergence/asymptotic hypothesis, the cap-charge identity and the LeBrun transfer are valid. The zero-charge four-class cap is not excluded by the arguments given; a \(w_2\)/spin or eta/Dirac argument would require additional structure not presently supplied.

---

### 1. Theorem-G signs and orientation conventions

With the Step-33 conventions

\[
\chi(D)=\int_D e+\mathcal E,\qquad 
\int_D L=\tau(D)+\mathcal H,
\]

and

\[
e=\frac1{8\pi^2}\Bigl(|W|^2-\frac12|\mathrm{Ric}^\circ|^2+\frac{s^2}{24}\Bigr),
\qquad
L=\frac1{12\pi^2}(|W^+|^2-|W^-|^2),
\]

one has

\[
2e+3L
=
\frac1{4\pi^2}
\Bigl(
2|W^+|^2-\frac12|\mathrm{Ric}^\circ|^2+\frac{s^2}{24}
\Bigr).
\]

Since

\[
2\chi+3\tau
=
\int_D(2e+3L)+2\mathcal E-3\mathcal H,
\]

it follows that

\[
\widehat P(D)
=
\frac1{2\pi^2}\int_D|W^+|^2
+
\frac1{96\pi^2}\int_Ds^2
-
(2\chi+3\tau)(D)
+
\mathcal Q_+(\partial D),
\]

where

\[
\mathcal Q_+=2\mathcal E-3\mathcal H.
\]

Similarly,

\[
\mathcal Q_-=2\mathcal E+3\mathcal H.
\]

Thus the printed formula

\[
\mathcal Q_\pm=2\mathcal E\mp 3\mathcal H
\]

is correct.

Orientation reversal changes the signs of both \(\mathcal E\) and \(\mathcal H\). Hence for a 3-manifold link \(L\),

\[
\mathcal Q_\pm(-L)=-\mathcal Q_\pm(L).
\]

This is the essential sign rule for caps.

---

### 2. Cap identity: correct sign, but eta convergence needs a stronger hypothesis

Let \(C_j^{(\rho)}\) be a cap component of \(M\setminus \Omega_\rho\). Its oriented outer link is \(-L_{j,\rho}\), where \(L_{j,\rho}\) is oriented as part of \(\partial\Omega_\rho\). Applying Theorem G to the cap gives

\[
\widehat P(g_i;C_j^{(\rho)})
=
C_+(g_i;C_j^{(\rho)})
-
(2\chi+3\tau)(C_j)
+
\mathcal Q_+(-L_{j,\rho};g_i).
\]

Using orientation reversal,

\[
\mathcal Q_+(-L_{j,\rho};g_i)
=
-\mathcal Q_+(L_{j,\rho};g_i).
\]

Therefore

\[
C_+(g_i;C_j^{(\rho)})
=
(2\chi+3\tau)(C_j)
+
\mathcal Q_+(L_{j,\rho};g_i)
+
\widehat P(g_i;C_j^{(\rho)}).
\]

Since

\[
0\le \widehat P(g_i;C_j^{(\rho)})\le \widehat P(g_i;M)\to0,
\]

one obtains, for fixed \(\rho\),

\[
\lim_i C_+(g_i;C_j^{(\rho)})
=
(2\chi+3\tau)(C_j)
+
\lim_i\mathcal Q_+(L_{j,\rho};g_i),
\]

provided the link charge converges.

This is exactly the sign used in Step 105:

\[
c_j(\rho)
=
(2\chi+3\tau)(C_j)
+
\mathcal Q_+(L_{j,\rho};g_\infty).
\]

Then

\[
c_j
=
\lim_{\rho\to0}c_j(\rho)
=
(2\chi+3\tau)(C_j)
+
\sum_{\ell\in J_j}\mathcal Q_+^\infty(L_\ell),
\]

with each \(L_\ell\) oriented as part of \(\partial\Omega_\rho\). The sign is correct.

#### Analytic repair

The proof says that the eta invariant depends smoothly on the link metric because the kernel dimension is topological. That is not enough as stated.

The link charge is

\[
\mathcal Q_+=2\mathcal E-3\mathcal H,
\qquad
\mathcal H=\eta+\int T_{p_1}.
\]

The terms \(\mathcal E\) and the local transgression \(\int T_{p_1}\) are local in the metric jet and are controlled by sufficiently strong \(C^2\) convergence on the link. The eta invariant \(\eta\) is spectral and nonlocal. The odd-signature operator has kernel dimension determined by the topology of the link, but \(\eta\) also depends on the signs of nonzero eigenvalues. Convergence only in \(C^2\) does not by itself guarantee convergence of \(\eta\). One needs either:

1. \(C^\infty\) convergence, or sufficiently high regularity convergence, on collars of the links together with a uniform spectral gap away from the topological kernel; or  
2. an adiabatic fibred-cusp formula, such as the Dai–Wei formula, which supplies the limit of \(\mathcal H\) directly.

A corrected version of the theorem should therefore assume:

> **(E\(^+\))** In addition to (E), for every fixed \(\rho\), the induced metrics on the links \(L_{j,\rho}\) converge smoothly enough that the odd-signature eta invariants converge, and for each end the limit  
> \[
> \mathcal Q_+^\infty(L_\ell)
> =
> \lim_{\rho\to0}\mathcal Q_+(L_{\ell,\rho};g_\infty)
> \]
> exists.

Under (E\(^+\)), the fixed-\(\rho\) limit and then the \(\rho\to0\) limit defining \(c_j\) exist.

Without the existence of \(\mathcal Q_+^\infty\), the double limit is not supplied by (E) alone. The sentence “by the first identity itself” is circular unless one already knows that the \(C_+\)-mass of the end tail has a limit. The Dai–Wei fibred-cusp asymptotics provide this in the circle-bundle cusp case; a general finite-volume Einstein end requires additional information.

---

### 3. Scalar part and cap volume

The scalar argument is essentially correct, but the reason should be stated slightly differently.

For fixed \(\rho\), the caps do not need to converge geometrically to \(g_\infty\). What is needed is the total volume convergence:

\[
\mathrm{Vol}(g_i;M)\to \mathrm{Vol}(g_\infty;\Omega),
\]

together with local convergence on \(\Omega_\rho\), which gives

\[
\mathrm{Vol}(g_i;\Omega_\rho)\to \mathrm{Vol}(g_\infty;\Omega_\rho).
\]

Therefore

\[
\mathrm{Vol}(g_i;M\setminus\Omega_\rho)
\to
\mathrm{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]

Since \(\Omega_\rho\uparrow\Omega\) and \(\Omega\) has finite volume,

\[
\mathrm{Vol}(g_\infty;\Omega\setminus\Omega_\rho)\to0.
\]

Now

\[
\int_{C_j}s_i^2
\le
2\int_M(s_i-\bar s_i)^2
+
2\bar s_i^2\,\mathrm{Vol}(g_i;C_j).
\]

The first term tends to zero by hypothesis. The second term is controlled by the total cap volume, which tends to zero after \(\rho\to0\). Hence

\[
\lim_{\rho\to0}\limsup_i \int_{C_j}s_i^2=0.
\]

Consequently,

\[
c_j
=
\lim_{\rho\to0}\lim_i
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+_{g_i}|^2,
\]

and therefore \(c_j\ge0\).

This part is valid under the volume convergence already present in (E).

---

### 4. Dai–Wei normalization and the formula \(c=(2\chi+3\tau)(C)+e_{\rm out}-3\operatorname{sign}e_{\rm out}\)

For a circle-fibred cusp with Euler number \(e\), where the link is oriented as \(\partial\overline\Omega\), Step 105 uses

\[
\mathcal E\to0,
\qquad
\mathcal H\to \frac e3-\operatorname{sign}e.
\]

Therefore

\[
\mathcal Q_+^\infty
=
2\mathcal E-3\mathcal H
=
-3\Bigl(\frac e3-\operatorname{sign}e\Bigr)
=
-e+3\operatorname{sign}e.
\]

This is the orientation in which \(L\) belongs to \(\partial\Omega\).

If the same link is oriented as the outer link of the cap, its Euler number is

\[
e_{\rm out}=-e.
\]

Then

\[
\mathcal Q_+^\infty(L_{\partial\Omega})
=
-e+3\operatorname{sign}e
=
e_{\rm out}-3\operatorname{sign}e_{\rm out}.
\]

Thus

\[
c
=
(2\chi+3\tau)(C)
+
e_{\rm out}
-
3\operatorname{sign}e_{\rm out}.
\]

The sign convention is consistent.

---

### 5. Model checks and one presentational correction

The table checks are algebraically correct under the above convention.

#### Taub–NUT, \(W^-=0\) orientation

Here

\[
\chi=1,\qquad \tau=0,\qquad e_{\rm out}=-1.
\]

Then

\[
(2\chi+3\tau)(C)=2,
\]

and

\[
e_{\rm out}-3\operatorname{sign}e_{\rm out}
=
-1-3(-1)=2.
\]

Therefore

\[
c=4.
\]

The independent Taub–NUT calculation gives

\[
\frac1{8\pi^2}\int |W^+|^2=1.
\]

Since

\[
C_+
=
\frac1{2\pi^2}\int |W^+|^2
=
4\cdot \frac1{8\pi^2}\int |W^+|^2,
\]

the corresponding value of \(C_+\) is \(4\). The table entry should therefore be read as saying that the normalized \(W^+\)-integral is \(1\), hence \(C_+=4\). As printed, the phrase “independent value of \(C_+\)” next to \(\frac1{8\pi^2}\int|W^+|^2=1\) could mislead; the actual \(C_+\)-value is \(4\).

#### Taub–NUT, \(W^+=0\) orientation

Here

\[
\chi=1,\qquad \tau=0,\qquad e_{\rm out}=+1,
\]

so

\[
c=2+1-3=0,
\]

matching \(C_+=0\).

#### Taub-bolt on \(O(-1)\)

Here

\[
\chi=2,\qquad \tau=-1,\qquad e_{\rm out}=-1.
\]

Then

\[
(2\chi+3\tau)=4-3=1,
\]

and

\[
c=1+(-1)-3(-1)=3.
\]

This matches the Step-27 value.

#### Multi-Taub–NUT \(A_{m-1}\), \(W^+=0\) orientation

Here

\[
\chi=m,\qquad \tau=-(m-1),\qquad e_{\rm out}=m.
\]

Then

\[
(2\chi+3\tau)=2m-3m+3=3-m,
\]

and

\[
e_{\rm out}-3\operatorname{sign}e_{\rm out}=m-3.
\]

Hence

\[
c=0
\]

for every \(m\ge1\). This is consistent with the hyperkähler \(W^+=0\) orientation.

The orientation relation to Step 33 is also consistent. In Step 33, the model charge \((-2,2)\) for the Taub–NUT link is the charge with the link oriented as the outer link of the enclosed region. In Step 105, the link entering the cap identity is oriented as part of \(\partial\Omega_\rho\), the opposite orientation, giving \(+2\) in the \(+\)-charge.

---

### 6. Exceptional \(S^3\)-Hopf caps and the formula \(c=4-r\)

Let

\[
C\cong \#r\,\overline{\mathbb{CP}}^2\setminus B^4,
\qquad
\partial C=S^3.
\]

Then

\[
\chi(C)=r+1,
\qquad
\tau(C)=-r.
\]

Therefore

\[
(2\chi+3\tau)(C)
=
2(r+1)-3r
=
2-r.
\]

For the admissible chirality,

\[
e_{\rm out}=-1,
\]

so

\[
e_{\rm out}-3\operatorname{sign}e_{\rm out}
=
-1+3=2.
\]

Thus

\[
c=(2-r)+2=4-r.
\]

For the opposite chirality,

\[
e_{\rm out}=+1,
\]

so

\[
e_{\rm out}-3\operatorname{sign}e_{\rm out}
=
1-3=-2,
\]

and

\[
c=(2-r)-2=-r.
\]

Because Theorem 105.Q gives \(c\ge0\), the opposite chirality is impossible for \(r>0\), and the admissible chirality requires \(r\le4\). This part is correct under (E\(^+\)) and the fibred Hopf asymptotics.

For disk-bundle caps \(D(-p)\) with link \(L(p,1)\), the same calculation gives

\[
c_{\rm disk}=4-p,
\qquad
c_{\rm opposite}=p-2,
\]

matching the JSON check.

---

### 7. LeBrun mixed estimate and the inequality \(9k+8\sum c_j\le3A\)

Assume the LeBrun estimate

\[
\int_M(s-\sqrt6\,|W^+|)^2\ge72\pi^2A
\]

for all metrics on \(M\).

Let

\[
\phi_i=s_i-\sqrt6\,|W^+_{g_i}|.
\]

Split \(M\) into \(\Omega_\rho\) and the caps. For each fixed \(i\),

\[
\int_M\phi_i^2
=
\int_{\Omega_\rho}\phi_i^2
+
\sum_j\int_{C_j^{(\rho)}}\phi_i^2.
\]

Pass to the limit \(i\to\infty\), then \(\rho\to0\).

#### Cap contribution

On a cap,

\[
\int_{C_j}s_i^2\to0
\]

in the iterated limit, while

\[
\frac1{2\pi^2}\int_{C_j}|W^+_{g_i}|^2\to c_j.
\]

Thus

\[
\|W^+_{g_i}\|_{L^2(C_j)}^2\to2\pi^2c_j.
\]

By Cauchy–Schwarz,

\[
\int_{C_j}(s_i-\sqrt6|W^+_{g_i}|)^2
\le
\bigl(\|s_i\|_{L^2(C_j)}+\sqrt6\,\|W^+_{g_i}\|_{L^2(C_j)}\bigr)^2.
\]

The scalar term disappears in the iterated limit, giving

\[
\lim_{\rho\to0}\limsup_i
\int_{C_j^{(\rho)}}\phi_i^2
\le
6\cdot 2\pi^2c_j
=
12\pi^2c_j.
\]

#### Einstein-domain contribution

On \(\Omega\), write

\[
\int_\Omega s_\infty^2=96\pi^2x,
\qquad
\int_\Omega |W^+_\infty|^2=2\pi^2y.
\]

Then

\[
C_+(g_\infty;\Omega)=x+y.
\]

Again by Cauchy–Schwarz,

\[
\int_\Omega(s_\infty-\sqrt6|W^+_\infty|)^2
\le
\left(\sqrt{96\pi^2x}+\sqrt{12\pi^2y}\right)^2.
\]

For fixed \(x+y\), the right-hand side is at most

\[
(96\pi^2+12\pi^2)(x+y)
=
108\pi^2(x+y).
\]

Hence

\[
\int_\Omega\phi_\infty^2
\le
108\pi^2C_+(g_\infty;\Omega).
\]

By Theorem 105.Q(3),

\[
C_+(g_\infty;\Omega)=A-k-\sum_jc_j.
\]

Therefore

\[
\int_\Omega\phi_\infty^2
\le
108\pi^2\left(A-k-\sum_jc_j\right).
\]

Adding the cap contribution gives

\[
72\pi^2A
\le
108\pi^2\left(A-k-\sum_jc_j\right)
+
12\pi^2\sum_jc_j.
\]

Divide by \(\pi^2\):

\[
72A
\le
108A-108k-108\sum_jc_j+12\sum_jc_j.
\]

Thus

\[
108k+96\sum_jc_j\le36A,
\]

or

\[
\boxed{9k+8\sum_jc_j\le3A.}
\]

The constants are correct.

The second inequality follows from the scalar estimate. If

\[
\int_Ms^2\ge32\pi^2A,
\]

and the cap scalar contributions vanish in the limit, then

\[
96\pi^2x\ge32\pi^2A,
\]

so

\[
x\ge \frac A3.
\]

Since

\[
x+y=A-k-\sum_jc_j
\]

and \(y\ge0\),

\[
A-k-\sum_jc_j\ge \frac A3,
\]

hence

\[
\boxed{k+\sum_jc_j\le\frac{2A}{3}.}
\]

This is also correct.

---

### 8. Corollary 105.H and the Hopf-collapse channel

Assume all exceptional classes lie in \(N\) admissible \(S^3\)-Hopf caps carrying

\[
r_1,\dots,r_N\ge1,
\qquad
\sum_j r_j=k.
\]

For each such cap,

\[
c_j=4-r_j.
\]

Substitute into

\[
9k+8\sum_jc_j\le3A.
\]

Then

\[
9k+8\sum_j(4-r_j)
=
9k+32N-8k
=
k+32N.
\]

Therefore

\[
\boxed{k+32N\le3A.}
\]

If each class sits in its own cap, then \(N=k\), giving

\[
33k\le3A,
\]

or

\[
\boxed{k\le \frac A{11}.}
\]

If classes are packed four to a cap, then \(N=k/4\), giving

\[
k+8k\le3A,
\]

or

\[
\boxed{k\le\frac A3.}
\]

This is exactly the smooth threshold, so the four-class zero-charge Hopf cap is invisible to this transferred LeBrun inequality. The algebra is correct.

The statement that the channel is “excluded” in the singleton regime means only that such a configuration cannot occur under the hypotheses (E\(^+\)), the Dai–Wei Hopf asymptotics, and the LeBrun estimate. It is not an unconditional exclusion of all Hopf-collapse geometry unless those hypotheses are independently supplied by a compactness theorem for actual \(\mathscr D\to0\) sequences.

---

### 9. What follows, and what does not, for the zero-charge four-class cap

For \(r=4\) and \(e_{\rm out}=-1\),

\[
c=4-r=0.
\]

Theorem 105.Q then gives

\[
C_+(g_i;C)\to0,
\qquad
\int_C s_i^2\to0,
\qquad
\widehat P(g_i;C)\to0.
\]

Equivalently,

\[
\int_C |W^+_{g_i}|^2\to0,
\qquad
\int_C s_i^2\to0,
\qquad
\int_C |\mathrm{Ric}^\circ_{g_i}|^2\to0.
\]

This does not force \(W^-\) to vanish. The minus identity gives additional information. For \(C=\#4\,\overline{\mathbb{CP}}^2\setminus B^4\),

\[
\chi=5,\qquad \tau=-4,
\]

so

\[
(2\chi-3\tau)(C)=10+12=22.
\]

For the admissible chirality \(e_{\rm out}=-1\), the corresponding minus link charge is

\[
\mathcal Q_-^{\rm cap}=-2.
\]

Since \(\widehat P\to0\),

\[
C_-(C)
=
(2\chi-3\tau)(C)-\mathcal Q_-^{\rm cap}
=
22-(-2)
=
24.
\]

Thus a zero-charge four-class cap may still carry

\[
\frac1{2\pi^2}\int_C|W^-|^2\to24,
\]

or equivalently

\[
\frac1{8\pi^2}\int_C|W^-|^2\to6.
\]

So the cap is invisible to the \(C_+\)/LeBrun mixed estimate, but it is not invisible to full curvature or to the minus chiral charge.

The note’s geometric picture—that curvature concentration would have to appear as anti-self-dual Ricci-flat bubbles, with simply connected ones being hyperkähler in the \(W^+=0\) orientation—is consistent with the vanishing of \(\mathrm{Ric}^\circ\), \(s\), and \(W^+\). However, that picture is not a theorem following from Theorem 105.Q alone. It requires an independent bubbling/collapse decomposition for sequences with

\[
\widehat P\to0,\qquad
\int s^2\to0,\qquad
\int |W^+|^2\to0.
\]

Such a decomposition is not supplied in the note.

---

### 10. Can \(w_2\)/spin exclude the zero-charge four-class cap?

Not by itself.

The cap

\[
C=\#4\,\overline{\mathbb{CP}}^2\setminus B^4
\]

has intersection form \(-I_4\), which is odd. A smooth spin 4-manifold with \(S^3\) link would have an even intersection form. This is the source of the suggested obstruction.

But in the degeneration picture, the topology of \(C\) need not be carried by a single smooth spin bubble. It could be distributed among:

1. simply connected hyperkähler bubbles, which have even forms;  
2. non-simply-connected anti-self-dual Ricci-flat pieces;  
3. collapsed regions with an F-structure or other volume-collapsing geometry.

The odd part of \(-I_4\) must indeed be carried somewhere, but nothing in the current argument forces it to be carried by a piece with positive \(C_+\)-energy. A collapsed region can carry topological information, including \(w_2\), while its curvature energy tends to zero. Therefore \(w_2\) alone does not produce a lower bound on \(c\).

A spin argument would become decisive only if one first proved a decomposition theorem stating that all second homology of the cap is carried by noncollapsed simply connected hyperkähler bubbles, or by pieces with even intersection forms. But that theorem would already amount to excluding the zero-charge four-class cap.

Thus a \(w_2\)/spin argument cannot currently exclude the cap without assuming the desired conclusion in some form.

---

### 11. Can eta/Dirac arguments exclude it?

Also not with the present input.

The plus-charge computation already uses the eta invariant of the odd-signature operator. A Dirac or spin\(^c\) eta invariant is a different spectral quantity. To turn it into an obstruction one would need at least:

1. a fixed supplied smooth basic class or spin\(^c\) structure on the sequence;  
2. global \(L^4\) spinor control and \(L^2\) curvature control from the Seiberg–Witten equations;  
3. local elliptic convergence on the Einstein region;  
4. an equivariant removable-singularity theorem across the collapsed cap;  
5. an adiabatic Dirac eta formula for the Hopf-collapsed link;  
6. identification of the limiting spin\(^c\) holonomy on the link.

These are precisely the missing analytic steps already identified in the correction of 104.M. Without them, an eta/Dirac argument would have to assume the existence and limiting form of the monopole field it is meant to control.

Therefore no currently supplied eta/Dirac invariant excludes the zero-charge four-class cap.

---

### 12. Proved consequences versus heuristic topology

Under the strengthened hypotheses (E\(^+\)) and Dai–Wei fibred-cusp asymptotics, the following are valid:

1. The cap-charge identity  
   \[
   c_j=(2\chi+3\tau)(C_j)+\sum_{\ell\in J_j}\mathcal Q_+^\infty(L_\ell).
   \]

2. The positivity \(c_j\ge0\).

3. The scalar vanishing on caps and the identification  
   \[
   c_j=\lim_{\rho\to0}\lim_i\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+_{g_i}|^2.
   \]

4. The global decomposition  
   \[
   C_+(g_\infty;\Omega)=A-k-\sum_jc_j.
   \]

5. The LeBrun transfer  
   \[
   9k+8\sum_jc_j\le3A.
   \]

6. The \(S^3\)-Hopf charge formula  
   \[
   c=4-r
   \]
   in the admissible chirality.

7. The chirality selection and the four-class bound \(r\le4\).

8. The singleton-cap threshold \(k\le A/11\) and the four-per-cap threshold \(k\le A/3\).

The following are not proved by the current material:

1. That an actual \(\mathscr D\to0\) sequence satisfies (E) or (E\(^+\)).  
2. That the relevant ends have Dai–Wei fibred-cusp asymptotics.  
3. That the odd-signature eta invariants converge under the originally stated \(C^2_{\rm loc}\) convergence.  
4. That a zero-charge four-class cap cannot occur.  
5. That \(w_2\), spin, or eta/Dirac invariants alone exclude that cap.

The zero-charge four-class cap remains the precise open object. The inequalities show why it is invisible to the transferred LeBrun estimate, but they do not decide whether the cap can be realized geometrically.