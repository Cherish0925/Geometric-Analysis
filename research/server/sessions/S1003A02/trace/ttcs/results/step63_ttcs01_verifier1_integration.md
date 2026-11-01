# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 63,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step63_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step63_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-62/63 derivations on M = X#kCP̄² (X minimal general type, A = c1²(X), P = ∫|Ric°|², p = P/8π²). Check each with explicit conventions (AAD: |Ω|²=2, ∇Ω = a⊗φ − Ja⊗Jφ, s*−s=|∇Ω|²=4|a|², κ_J = s+6u with u=|a|², W2 = ½(ρ*''⊗Ω+Ω⊗ρ*''), γ_J = R(Ω) − a∧Ja). (1) Identity 62.1 and Theorem 62.A (step62 note §1–3). (2) Theorem 63.T: the general Gauss formula γ_J = R(Ω)+α∧β for an arbitrary orthogonal J with ∇Ω = α⊗φ+β⊗Jφ (sign, factor, gauge independence, that it represents 2πc1(J)), that R(Ω)^- = ρ0 with |ρ0|² ≤ |Ric°|²/2, the Hodge step ‖γ^-‖ ≥ 2π|c1^-|, the choice of class a_ε with |a_ε^-|² ≥ k+Π and existence of J with c1(J)=a_ε (Wu), and the Kähler-tariff reduction. (3) Proposition 63.AK: P = 2‖γ^-‖² + ∫u(5u+s) + 2∫|ρ*''|² + 4∫|W3|², including norms |W1|²=κ²/24, |W2|²=|ρ*''|², and the Sekigawa consistency check and the AK-Einstein consequences. (4) §3 emptiness of the 62.A equality locus: does LeBrun's Prop 2.4 equality plus Cauchy–Schwarz really force u constant; is N a section of a bundle with c2 = c2+2c1² = 5χ+6τ, and is 5χ+6τ = c2(X)+2A−k on M; the Taubes/Li–Liu period argument. (5) §4 model numbers: constant-torsion bound p ≥ (A−k)(2−3u)²/(u(4−3u)); the variance–slack relation ∫(u−ū)² = 8π²σ; the ASD-patch saturating configuration (υ=5k, patch volume 18π², ½∫u² = 4π²k, p=0) and the \overline{FPP} numerology; the two-ended AE neck bound P ≥ 32π². Report every error with the corrected statement, and say which conclusions survive.

## Integrated Scientific Memo

# Verification memo: Steps 62–63

Use the AAD curvature convention and operator norms on \(\Lambda^2\), with
\[
|\Omega|^2=|\phi|^2=|J\phi|^2=2,\qquad
u=|a|^2=\frac14|\nabla\Omega|^2,
\]
\[
s^*-s=4u,\qquad \kappa_J=s+6u.
\]
Distinguish the pointwise conformal scalar curvature \(\kappa_J\) from the conformal-class Weyl deficit \(\kappa[g]\). Write
\[
C=A-k,\qquad B=A+\upsilon,\qquad V(\widetilde g)=2\pi^2B.
\]

**Main findings.** The Gauss–Hodge theorem 63.T and identity 63.AK are correct, including their signs and constants. Identity 62.1 is correct after an intermediate coefficient correction. The fixed-\(\kappa\) bound needs a corrected domain and interpretation. The constant-positive-torsion bound is valid in the lowest-eigenvalue range, contrary to one branch’s rejection; however, the formal-mode torsion used in the note is miscalculated. Equality exclusion survives. The patch calculations are formal density calculations, not a metric construction, and several conclusions drawn from them need qualification.

## 1. Identity 62.1 and Theorem 62.A

The supplied LeBrun Chern–Weil formula gives
\[
P=4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2C.
\]
At the negative Yamabe representative,
\[
\int s^2=32\pi^2B,\qquad
\int|W^+|^2=\frac{4\pi^2}{3}(A-2\kappa).
\]
Consequently,
\[
\boxed{p(\widetilde g)=k-\frac43\kappa+\frac13\upsilon.}
\]
The first term in Step 62’s substitution is **\(\frac23(A-2\kappa)\), not \(\frac16(A-2\kappa)\)**. The final identity is unaffected.

Conformal invariance of the Weyl integral and \(\int s_g^2\ge Y[g]^2\) give
\[
\boxed{p(g)\ge p(\widetilde g).}
\]

Let
\[
\Pi=\max_\varepsilon(a_\varepsilon^+)^2-A.
\]
LeBrun’s Theorem 2.3, multiplied by \(9/4\), and the \(L^2\) triangle inequality yield
\[
\boxed{2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}
       \ge3\sqrt{A+\Pi}.}
\tag{1}
\]
All constants in (62.2) are correct.

### Correct fixed-\(\kappa\) statement

Since \(\kappa\le A/2\), put \(y=\sqrt{1-2\kappa/A}\). For \(0\le\kappa\le A/2\), (1) implies
\[
\upsilon\ge A\left[\left(\frac{3-y}{2}\right)^2-1\right],
\]
hence
\[
\boxed{
p(g)\ge L_A(k,\kappa)
=k-\kappa+\frac12\left(A-\kappa-\sqrt{A^2-2A\kappa}\right).
}
\tag{2}
\]
Thus the fixed-\(\kappa\) inequality remains valid **above** \(4A/9\), up to \(A/2\). Its expansion is correctly
\[
L_A(k,\kappa)=k-\kappa+\frac{\kappa^2}{4A}
+\frac{\kappa^3}{4A^2}+O(\kappa^4/A^3).
\]

The threshold \(4A/9\) is a monotonicity threshold:
\[
\frac{\partial L_A}{\partial\kappa}
=-\frac32+\frac1{2\sqrt{1-2\kappa/A}},
\]
so \(L_A\) decreases up to \(4A/9\), then increases, attaining
\[
\min L_A=k-\frac A3.
\]
The note’s statement that above \(4A/9\) only the unconditional bound remains is therefore incorrect for a **specified** \(\kappa\). Its assertion elsewhere that \(L_A\) decreases for \(\kappa<2A\) is also incorrect.

For \(\kappa<0\), the safe and stronger useful statement is
\[
\boxed{p(g)\ge k-\frac43\kappa,}
\tag{3}
\]
using \(\upsilon\ge0\). Squaring \(3-y\) does not justify (2) for arbitrarily negative \(\kappa\). A corrected theorem should use (3) for \(\kappa<0\) and (2) for \(0\le\kappa\le A/2\).

The conditional \(k^2/A\) consequence survives in its intended small-\(k/A\) range: if \(\kappa_*\le k\) and \(k\le4A/9\), then
\[
\inf_g P(g)\ge
4\pi^2\left(A-k-\sqrt{A^2-2Ak}\right).
\]
More generally, using \(L_A(k,\kappa_*)\) requires \(\kappa_*\le4A/9\). The analogous substitution \(\kappa\le k+\beta p\) requires the substituted upper endpoint to remain in the decreasing range; its small-\(k/A\) asymptotic conclusion survives.

### An important logical error in the “reading” of 62.1

The two summands
\[
k-\kappa,\qquad \frac13(\upsilon-\kappa)
\]
are not both necessarily nonnegative: \(\kappa\) may exceed \(k\). Therefore \(p/k\to0\) does **not** imply that both summands tend to zero separately.

In particular, Corollary 62.D’s claims
\[
\kappa/k\to1,\qquad \upsilon-\kappa=o(k),\qquad \Pi=o(k)
\]
do not follow from 62.1–62.2 alone. The formal patch densities below have \(p=0,\ \kappa=2k,\ \upsilon=5k\), with cancellation between the two summands. For \(\kappa\ge0\), these estimates imply only
\[
\kappa\ge k-p,\qquad
\upsilon=4\kappa-3k+3p,
\]
together with (1). They supply no upper bound forcing \(\kappa/k\to1\), and no geometric convergence to the equality locus.

## 2. Theorem 63.T: full verification

### Gauss formula, sign and gauge

For an arbitrary positive-orientation orthogonal \(J\), write \(\psi=J\phi\). The complete frame equations are
\[
\nabla\Omega=\alpha\otimes\phi+\beta\otimes\psi,
\]
\[
\nabla\phi=-\alpha\otimes\Omega+b\otimes\psi,\qquad
\nabla\psi=-\beta\otimes\Omega-b\otimes\phi.
\]
The \(\psi\)-coefficient of \(d^\nabla\nabla\phi\) is
\[
db+\alpha\wedge\beta.
\]
The curvature coefficient, with AAD’s convention, is \(-R(\Omega)\). Therefore
\[
\boxed{\gamma_J=-db=R(\Omega)+\alpha\wedge\beta.}
\tag{4}
\]
There is no missing factor of two. For almost-Kähler \(J\), \(\alpha=a,\ \beta=-Ja\), so (4) becomes precisely AAD (25):
\[
\gamma_J=R(\Omega)-a\wedge Ja.
\]

Under \(\phi'=\cos\theta\,\phi+\sin\theta\,\psi\),
\[
\alpha'=\cos\theta\,\alpha+\sin\theta\,\beta,\qquad
\beta'=-\sin\theta\,\alpha+\cos\theta\,\beta,\qquad
b'=b+d\theta.
\]
Thus both \(db\) and \(\alpha\wedge\beta\) are gauge-independent. The projected connection on
\[
(\Omega^\perp,J)\cong K_J^{-1}
\]
has curvature \(i\,db\). With \(c_1=[iF/(2\pi)]\),
\[
\boxed{[\gamma_J]=2\pi c_1(J).}
\]
This argument does not require \(d\Omega=0\).

### Ricci normalization and twist

Singer–Thorpe gives
\[
R(\Omega)^-=\frac12\widetilde{\operatorname{Ric}^{\circ}}(\Omega).
\]
The \(J\)-anti-invariant Ricci component anticommutes with \(J\) and disappears from this expression. Hence
\[
\boxed{
R(\Omega)^-=\rho_0=\operatorname{Ric}_0'\circ J,\qquad
|\rho_0|^2=\frac12|\operatorname{Ric}_0'|^2
\le\frac12|\operatorname{Ric}^{\circ}|^2.
}
\tag{5}
\]

Since
\[
|\nabla\Omega|^2=2(|\alpha|^2+|\beta|^2),
\]
and a decomposable two-form has equally sized self-dual and anti-self-dual parts,
\[
\boxed{
|(\alpha\wedge\beta)^-|
\le\frac1{4\sqrt2}|\nabla\Omega|^2,\qquad
\mathcal T_J\le\frac1{4\sqrt2}\|\nabla\Omega\|_{L^4}^2.
}
\tag{6}
\]

### Hodge step

For \(\gamma_J=H+d\theta\), \(H^-\) is harmonic and orthogonal to \((d\theta)^-\). Thus
\[
\boxed{
\|\gamma_J^-\|_2^2
=4\pi^2|c_1(J)^-|^2+\|(d\theta)^-\|_2^2.
}
\tag{7}
\]
Combining (4)–(7) proves
\[
\boxed{
P\ge2\bigl(2\pi|c_1(J)^-|-\mathcal T_J\bigr)_+^2.
}
\tag{8}
\]

### Best class and Wu existence

Fix a consistent sign for the pulled-back class \(c_1(X)\). Each
\[
a_\varepsilon=c_1(X)+\sum_i\varepsilon_iE_i
\]
is an integral lift of \(w_2(M)\), with
\[
a_\varepsilon^2=A-k=2\chi(M)+3\tau(M).
\]
The four-dimensional almost-complex existence criterion gives \(J\) with \(c_1(J)=a_\varepsilon\); it can be made orthogonal to any prescribed metric without changing \(c_1\).

Sign averaging gives
\[
\Pi\ge|c_1(X)^-|^2+\sum_i|E_i^+|^2.
\]
For a maximizing sign,
\[
\boxed{|a_\varepsilon^-|^2=k+\Pi}
\]
is an **equality**, not merely a lower bound. Consequently,
\[
\boxed{
\sqrt{P/2}\ge2\pi\sqrt{k+\Pi}
-\inf_{J:\,c_1(J)=a_\varepsilon}\mathcal T_J.
}
\]

### Kähler reduction and scope

For the Kähler \(J\), \(\mathcal T_J=0\). On the blow-up Kähler cone, Hodge index gives
\[
(c_1(J)^+)^2
=\frac{(c_1(J)\cdot[\omega])^2}{[\omega]^2}\ge A,
\]
so \(|c_1(J)^-|^2\ge k\), and
\[
\boxed{P\ge8\pi^2k.}
\]
One must apply (8) to the **actual parallel Kähler structure**, not assume the maximizing sign structure is parallel. Extending this assertion to every complex structure on the underlying smooth manifold requires a separate minimal-model identification theorem; Wu and sign averaging do not supply it.

The collar-twist discussion is not a verified global estimate from these sources. Moreover, in a parallel trivialization a one-parameter rotation of \(\Omega\) sweeps zero spherical area, so \(\alpha\wedge\beta=0\) there even if \(|\nabla\Omega|\ne0\). The bound (6) can be very nonsharp; it does not establish a matching lower twist cost for the proposed collar.

## 3. Proposition 63.AK and Einstein consequences

AAD’s decomposition has
\[
|W_1^+|^2
=\left(\frac{\kappa_J}{6}\right)^2
+2\left(\frac{\kappa_J}{12}\right)^2
=\frac{\kappa_J^2}{24}.
\]
For
\[
W_2^+=\frac12(\rho_*''\otimes\Omega+\Omega\otimes\rho_*''),
\]
orthogonality to \(\Omega\) and \(|\Omega|^2=2\) give
\[
\boxed{|W_2^+|^2=|\rho_*''|^2.}
\]

Furthermore,
\[
(a\wedge Ja)^+=\frac u2\Omega,
\]
so
\[
\boxed{
\gamma_J^+=\frac{s+2u}{4}\Omega+\rho_*''
=\frac{s+s^*}{8}\Omega+\rho_*'',\qquad
|\gamma_J^+|^2=\frac{(s+2u)^2}{8}+|\rho_*''|^2.
}
\]
Substitute
\[
4\pi^2c_1(J)^2=\|\gamma_J^+\|_2^2-\|\gamma_J^-\|_2^2
\]
into Chern–Weil, and use
\[
\frac{(s+6u)^2}{6}+\frac{s^2}{12}
-\frac{(s+2u)^2}{4}=su+5u^2.
\]
This proves exactly
\[
\boxed{
P=2\|\gamma_J^-\|_2^2+\int u(5u+s)
+2\int|\rho_*''|^2+4\int|W_3^+|^2.
}
\tag{9}
\]

All coefficients in 63.AK are correct. In particular,
\[
P\ge8\pi^2|c_1(J)^-|^2-\int u(|s|-5u)_+.
\]

For Einstein metrics, \(s\) is constant:

* If \(s\ge0\), every term in (9) is nonnegative, forcing \(u=0\). This correctly recovers Sekigawa’s conclusion in dimension four.
* If \(s<0\), \(\rho_0=0\) and
  \[
  \|\gamma_J^-\|_2^2=\frac12\int u^2,
  \]
  giving
  \[
  \boxed{
  \int u(|s|-6u)
  =2\int|\rho_*''|^2+4\int|W_3^+|^2,
  }
  \]
  \[
  \boxed{\int|\nabla\Omega|^4\ge128\pi^2|c_1(J)^-|^2.}
  \]
  The first identity is a weighted integral restriction, **not** a pointwise bound \(u\le|s|/6\).

The advertised LeBrun barrier is correct as an algebraic relaxation. At \(s=-4,\ W_2=W_3=0\), Hodge flux gives
\[
B(2-u)^2\ge4(A+\Pi).
\]
Ignoring additional twist restrictions and taking \(\Pi=0\) yields
\[
p\ge k+A\,\frac{u(5u-4)}{(2-u)^2},
\]
whose minimum on \(0\le u\le2/3\) is \(k-A/3\), attained algebraically at \(u=1/2\).

## 4. Equality exclusion

### Equality really forces constant torsion

For equality in (2), all discarded inequalities must be equalities, including \(\Pi=0\). LeBrun Proposition 2.4 supplies an almost-Kähler structure with
\[
\Omega\text{ in the lowest eigenspace},\qquad
s+s^*\text{ constant},\qquad W^+\text{ \(J\)-invariant}.
\]
Since the Yamabe metric already has \(s=-4\),
\[
s+s^*=2s+4u
\]
immediately forces \(u\) constant. Cauchy–Schwarz also makes \(|W^+|\) constant. Here \(J\)-invariance gives \(W_2=W_3=0\).

### Nijenhuis bundle and topology

AAD identifies \(\nabla\Omega\), equivalently the Nijenhuis tensor up to the stated identification, with a section of the underlying real bundle of
\[
\Lambda^{0,1}\otimes\Lambda^{0,2}
\cong T^{1,0}\otimes K^{-1}.
\]
For this complex rank-two bundle,
\[
\boxed{
c_2(T^{1,0}\otimes K^{-1})
=c_2(M)+2c_1(J)^2=5\chi(M)+6\tau(M).
}
\]
A nowhere-zero section forces its top Chern number to vanish. On the blow-up,
\[
\boxed{5\chi+6\tau=c_2(X)+2A-k.}
\]
This excludes constant \(u>0\) whenever \(k\ne c_2(X)+2A\), not only when the number is positive. At that exceptional value, this argument alone gives no contradiction. The note’s unqualified positivity for all \(k\) must be restricted accordingly.

### Period contradiction

If \(\Pi=0\), then \(E_i^+=0\). Since an almost-Kähler form is harmonic and self-dual,
\[
E_i\cdot[\Omega]=0.
\]
The supplied LeBrun Proposition 3.2 explicitly excludes this: the other blow-up monopole class, differing by \(2E_i\), and Taubes’ theorem force a pseudo-holomorphic exceptional sphere with strictly positive area.

Thus, under Step 62’s sign-family hypotheses,
\[
\boxed{k\ge1\implies\text{the equality locus is empty}.}
\]
The supplied source already contains the needed period argument; an additional Li–Liu invocation is unnecessary here. This is exact nonattainment, not quantitative stability.

## 5. Model calculations and their corrected meaning

### 5.1 Constant positive torsion: resolving the conflicting verifications

Assume genuinely almost-Kähler,
\[
s=-4,\qquad W_2=W_3=0,\qquad u\text{ constant}.
\]
Then
\[
\boxed{p=B\left(1-2u+\frac32u^2\right)-C.}
\tag{10}
\]
Because
\[
\gamma^+=\frac{u-2}{2}\Omega
\]
is closed, both parts of the closed Chern form are harmonic. Hence
\[
|c_1^+|^2=\frac{B(2-u)^2}{4},\qquad
|c_1^-|^2=\frac{B(2-u)^2}{4}-C,\qquad
\mathcal T^2=\pi^2Bu^2.
\]
The exact twist inequality is therefore
\[
\boxed{
2\sqrt p+u\sqrt B\ge\sqrt{B(2-u)^2-4C}.
}
\tag{11}
\]

For \(u>0\), squaring these nonnegative quantities and inserting (10) gives
\[
2Bu(2-3u)\le4u\sqrt{Bp}.
\]
When \(0<u\le2/3\), this yields
\[
p\ge\frac B4(2-3u)^2,
\]
equivalently
\[
\boxed{Bu(4-3u)\ge4C.}
\tag{12}
\]
For \(C>0\), eliminating \(B\) gives
\[
\boxed{
p\ge C\,\frac{(2-3u)^2}{u(4-3u)}.
}
\tag{13}
\]

Thus **the note’s constant-torsion bound is valid for \(0<u\le2/3\)**. The branch rejecting it overlooked the division by \(u\). At \(u=0\), (11) becomes an equality and imposes no such restriction; cscK blow-ups do not contradict (13). The divergence as \(u\downarrow0\) concerns an everywhere-positive, constant-torsion family under the additional curvature assumptions, not the Kähler case.

For \(u>2/3\), the above squaring no longer gives the displayed positive lower bound. In the intended lowest-eigenvalue model, \(\kappa_J=-4+6u\le0\) already enforces \(u\le2/3\).

### Formal-mode torsion is miscalculated

The formal mode in Step 62 has eigenvalues
\[
\left(-x,\frac x2,\frac x2\right),\qquad x=\frac23-h,\qquad h=k/A.
\]
Therefore
\[
\kappa_J=-6x=-4+6h,\qquad
\boxed{u=h=k/A,}
\]
not \(2k/(3A)\). Consequently (13) would force, for small \(h\),
\[
\boxed{p\gtrsim A^2/k,}
\]
rather than \(3A^2/(2k)\).

The simpler best-class estimate gives
\[
p\ge\left(\sqrt{k+\Pi}-\frac{u\sqrt B}{2}\right)_+^2
=k\left(1-\frac12\sqrt{k/A}+O((k/A)^{3/2})\right)^2
\]
for \(B\sim A,\ \Pi=0\). The coefficient is \(1/2\), not \(1/3\).

Both forms exclude the diffuse formal mode **as an exact almost-Kähler model with these hypotheses**. Neither excludes arbitrary non-AK near-minimizers without additional control.

### 5.2 Variance is not exactly the 62.A slack

For
\[
m=\frac1V\int u,\qquad v=\frac1V\int(u-m)^2,
\]
the axial model has the exact formulas
\[
\int|W^+|^2=\frac V6\bigl[(2-3m)^2+9v\bigr],
\]
\[
p=B\left(1-2m+\frac32m^2+\frac32v\right)-C,
\qquad
\int(u-m)^2=2\pi^2Bv.
\]
Let the actual 62.A slack be
\[
\sigma=p-L_A(k,\kappa)=\frac{\upsilon-\upsilon_L(\kappa)}3.
\]
If \(m\to0,\ B/A\to1,\ \Pi=0\), and the underlying LeBrun integral estimate is saturated to the relevant order, expansion gives
\[
\sigma=\frac A4v+\text{higher-order terms},
\]
so only then
\[
\boxed{\int(u-m)^2=8\pi^2\sigma[1+o(1)].}
\]
The note’s exact equality is incorrect. Nonzero LeBrun slack contributes to \(\sigma\) independently of variance.

### 5.3 ASD-patch densities

Set \(u=2/3\) on total volume \(V_p=18\pi^2k\), and \(u=0\) elsewhere, with \(B=A+5k\). The residual volume is
\[
V-V_p=2\pi^2(A-4k).
\]
Hence this formal distribution requires
\[
\boxed{k\le A/4.}
\]
The arithmetic is otherwise correct:
\[
36V-20V_p=72\pi^2A,\qquad
\frac12\int u^2=4\pi^2k,\qquad
\kappa=2k,\qquad p=0.
\]

It does **not** saturate the Cauchy–Schwarz step of 62.A: \(|W^+|\) takes two different values. Indeed,
\[
\sigma=-L_A(k,2k)
=2k-\frac A2+\frac12\sqrt{A^2-4Ak},
\]
whereas
\[
\frac1{8\pi^2}\int(u-m)^2
=\frac{k(A-4k)}{A+5k}.
\]
These agree only to leading order as \(k/A\to0\), not exactly.

Nor is this a smooth almost-Kähler Einstein construction. If \(p=0\), then \(\operatorname{Ric}''=0\). With \(W_2=W_3=0\), AAD Corollary 1, equation (37), reduces to
\[
d^J(\kappa_J-s)=6\,d^Ju=0,
\]
forcing \(u\) constant. Globally, AAD Theorem 2 also makes a compact Einstein AK metric with \(W_2=0\) Kähler. A transition must therefore activate curvature components omitted by the patch model.

The concrete identity governing that transition is
\[
2d^Ju
=2\langle\delta W_3^+,\Omega\rangle
+2\delta\rho_*''
-\langle\rho_*'',\nabla_J\Omega\rangle
+\langle A^+,\Omega\rangle,
\]
with \(A_Z=(d^\nabla\operatorname{Ric}'')_Z+\iota_{JZ}d\rho\).
It identifies the necessary transition channels, but does not by itself give a uniform positive wall-energy constant.

### 5.4 Reversed fake projective planes and joining

The reversed-FPP numerical match is correct:
\[
\chi=3,\quad \tau=-1,\quad 2\chi+3\tau=3,\quad
W^+=0,\quad s=-4,\quad V=18\pi^2,
\]
with rational intersection form \(\langle-1\rangle\).

But \(\overline{\mathrm{FPP}}\) has \(b^+=0\), so it admits no orientation-compatible symplectic form. Its negative-definite intersection form also cannot support an almost-complex first Chern class of square \(3\). It therefore does **not** supply the asserted closed AK torsion patch. A bounded region’s Euler/signature numbers cannot be inferred from its curvature integral without boundary terms.

Also,
\[
(2\chi+3\tau)(X\sqcup k\,\overline{\mathrm{FPP}})=A+3k,
\]
whereas a connected sum has \(A-k\). Each joining removes four units. A full KE copy of \(X\) plus \(k\) normalized reversed FPPs has volume \(2\pi^2(A+9k)\), not the model’s \(2\pi^2(A+5k)\). The latter has removed four units of host volume per summand.

Accordingly, the density model does not prove that all available inequalities are blind to the summand, or that a low-cost competitor exists. The proposed SW extension to general negative-definite summands is not established by the supplied sources.

### 5.5 Two-ended AE neck

For a complete two-ended AE metric on \(S^3\times\mathbb R\), with sufficient decay and finite curvature integrals, each Euclidean end contributes \(1\) to Gauss–Bonnet:
\[
\frac1{8\pi^2}\int
\left(|W|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}\right)
=\chi-2=-2.
\]
Thus
\[
\boxed{
P=2\int|W|^2+\frac1{12}\int s^2+32\pi^2
\ge32\pi^2.
}
\]
This is correct. It prices a genuine complete two-ended AE limit, not every finite or fat transition region. Applying it to a degenerating connected-sum family requires establishing such neck limits and accounting for their energy.

## Conclusions that survive

* The exact Weyl/Yamabe identity, corrected fixed-\(\kappa\) bound, and conditional small-\(k/A\) law survive.
* Theorem 63.T and Proposition 63.AK survive in full, including the Einstein constraints.
* The \(k\ge1\) equality locus is empty under the sign-family assumptions, directly by the supplied Taubes period argument.
* Constant **positive** torsion in the axial lowest-eigenvalue model obeys the strong bound (13); the formal-mode torsion and its numerical coefficients need correction.
* Patch arithmetic survives only as a restricted formal density model, \(k\le A/4\). It is neither an AK construction nor simultaneous equality in 62.A.
* The remaining quantitative object is a coercive estimate linking the transition identity—or controlled non-AK frame twist—to curvature/slack. Exact rigidity and AE neck pricing do not yet furnish that estimate.