# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 66,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step66_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step66_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify, as a careful differential geometer, the identities and theorems in two notes about the Einstein-defect ledger on M = X#kCP̄² (X minimal general type). (1) Step-65 identities 65.1–65.3 (file step65_cell_exceptional_flux_ledger.md §1): the claim that for every orthogonal J the ASD part of R(Ω) equals B_gΩ (B_g the Ric° block Λ⁺→Λ⁻), the metric-only pairing ⟨t_J⁻,h⟩ = 2π⟨a,h⟩ − ∫⟨Ω,B*h⟩, the definition 𝔉_h=√2∫|B*h|, the Cauchy–Schwarz bound P/2 ≥ 𝔉²/‖h‖² (check the constant using |Ric°|²=4|B|²), and the ledger p=(1−δ)²/‖h‖²+L. (2) Step-66 (file step66_rank_one_exceptional_ricci_rigidity.md): Prop 66.Y (WLOG constant scalar curvature since P(g)−P(ĝ)=(1/12)(∫s²−Y²)≥0 for Y<0); Lemma 66.D div(φ∘ψ)=ψ(δφ) for SD φ and closed ASD ψ (symbolic check JSON supplied); the splitting L = L_rank + L_amp and the equality characterization B = cΩ̂₀⊗h; Theorem 66.R (constant s ⇒ Ω₀ closed hence almost-Kähler with J-invariant Ricci, ρ₀ ∝ h harmonic; extension across Z(h) via H³(Z)=0; converse via AAD (26) dρ=*(JδRic'')); Theorem 66.EM (L_rank=0 with constant s ⇔ Riemannian Einstein–Maxwell Ric°=φ∘h=½(F∘F)₀ with F=φ+h harmonic; check the factor ½ and the boundedness hypothesis near Z(h)); identities (66.3)–(66.5) obtained by inserting γ⁻=ρ₀+t⁻ into Prop 63.AK P=2‖γ⁻‖²+∫u(5u+s)+2‖ρ*''‖²+4‖W₃‖² with |t⁻|²=u²/2 and P=2‖ρ₀‖² when Ric''=0; Corollary 66.S (s≥0 ⇒ δ_b∈[−½,0], Kahler tariff p≥|b⁻|²); Prop 66.W weak estimate. Report precisely any sign, factor, quantifier, or regularity error, whether each statement is proved as written, and the corrected statement where needed. Also judge whether the interpretation in §5 (equality class = Einstein ∪ cscK ∪ strictly-AK J-invariant-Ricci with [ρ₀]∥a⁻; strictly-AK part = the open 4D Blair–Ianus problem at negative constant s) is accurate.

## Integrated Scientific Memo

# Verification memo: Steps 65–66

Use the conventions
\[
\mathcal R=
\begin{pmatrix}
W^++s/12&B^*\\
B&W^-+s/12
\end{pmatrix},
\qquad B:\Lambda^+\to\Lambda^-,
\qquad |\Ric^\circ|^2=4|B|^2,
\]
and \(P=\|\Ric^\circ\|_2^2,\ p=P/(8\pi^2)\). Pairings below are \(L^2\) pairings unless explicitly stated otherwise.

**Main conclusion.** The curvature-block identity, flux bound, divergence lemma, constant-scalar rigidity mechanism, torsion identities, nonnegative-scalar corollary, and weak Bianchi estimate are mathematically sound. The notes nevertheless require corrections to the normalization of the ledger, a saving inequality, several quantifiers, the unconditional Einstein–Maxwell interpretation, and the identification with the Blair–Ianus problem. Neither a connected interpolation between the proposed endpoints nor a near-equality compactness theorem has been proved.

## 1. Step 65: identities and normalization

### 65.1: correct, with orientation and pairing conventions specified

For an **orientation-compatible** orthogonal almost-complex structure, \(\Omega\in\Lambda^+\), so directly from the block decomposition,
\[
\boxed{(\mathcal R\Omega)^-=B\Omega.}
\]
There is no additional factor \(1/2\). This is the primitive Ricci form of the \(J\)-invariant part of \(\Ric^\circ\), not a statement that all of \(\Ric^\circ\) is \(J\)-invariant.

The supplied Step-63 identity gives
\[
\gamma_J^- =B\Omega+t_J^-,
\qquad [\gamma_J]=2\pi c_1(J).
\]
Consequently, for \(c_1(J)=a\) and harmonic ASD \(h\),
\[
\boxed{
(t_J^-,h)
=2\pi(h_a^-,h)-\int_M\langle\Omega,B^*h\rangle\,d\mu .
}
\tag{1}
\]
Thus 65.1 is correct if \(\langle a,h\rangle=(h_a^-,h)\). For the intersection pairing instead,
\[
(h_a^-,h)=-a\cdot[h],
\]
so the topological term is \(-2\pi a\cdot[h]\).

“Every orthogonal \(J\)” must mean every \(J\) inducing the chosen orientation; an orientation-reversing \(J\) has \(\Omega\in\Lambda^-\), and the asserted block formula does not apply.

### 65.2: correct constant

Since \(|\Omega|=\sqrt2\), define
\[
\mathcal F_h=\sqrt2\int_M|B^*h|\,d\mu.
\]
Then
\[
(t_J^-,h)\ge 2\pi(h_a^-,h)-\mathcal F_h.
\]
Also,
\[
\begin{aligned}
\mathcal F_h^2
&\le 2\left(\int_{\operatorname{supp}B}|B|\,|h|\right)^2\\
&\le 2\|B\|_2^2\|h\|_{L^2(\operatorname{supp}B)}^2
=\frac P2\|h\|_{L^2(\operatorname{supp}\Ric^\circ)}^2.
\end{aligned}
\]
Hence the coefficient in 65.2 is exactly correct:
\[
\boxed{\frac P2\ge
\frac{\mathcal F_h^2}{\|h\|_{L^2(\operatorname{supp}\Ric^\circ)}^2}.}
\tag{2}
\]
The quotient needs a nonzero denominator. For a ledger valid also at Einstein metrics, use the full norm of nonzero \(h\).

### 65.3: not correct as written for arbitrary \(h\)

Put
\[
H=\|h\|_2^2,\qquad q_h=(h_a^-,h)>0,
\qquad
\delta_h=1-\frac{\mathcal F_h}{2\pi q_h},
\]
and
\[
L_h=\frac1{4\pi^2}\left(\frac P2-\frac{\mathcal F_h^2}{H}\right)\ge0.
\]
The exact, rescaling-invariant ledger is
\[
\boxed{
p=\frac{q_h^2}{H}(1-\delta_h)^2+L_h.
}
\tag{3}
\]
Moreover, every class-\(a\) structure satisfies
\[
(t_J^-,h)\ge2\pi q_h\delta_h.
\]

The note mixes \(\mathcal F_h\), formed from unnormalized \(h\), with the pairing against \(\widehat h=h/\|h\|_2\). That definition of \(\delta\) is not homogeneous in \(h\). Its displayed ledger
\[
p=(1-\delta)^2/H+L
\]
holds only after imposing \(q_h=1\) and using the consistent definition \(\delta=1-\mathcal F_h/(2\pi)\).

Equivalently, using unit \(L^2\) norm throughout,
\[
q=(h_a^-,\widehat h),\qquad
\delta=1-\frac{\mathcal F_{\widehat h}}{2\pi q},
\qquad
p=q^2(1-\delta)^2+L.
\tag{4}
\]

The sentence “a sub-tariff metric must have
\(\mathcal F_h<2\pi\sqrt p\,\langle a,\widehat h\rangle\)” does **not** follow. The valid implication is
\[
\mathcal F_{\widehat h}\le2\pi\sqrt p;
\qquad
p<q^2\ \Longrightarrow\
\mathcal F_{\widehat h}<2\pi q,\quad\delta>0.
\tag{5}
\]
The extra factor \(q\) in the stated bound is unjustified.

### The saving inequality has the wrong direction

Under \(q_h=1\),
\[
\boxed{
1-p=2\delta-\delta^2-L
-(1-\delta)^2(H^{-1}-1).
}
\tag{6}
\]
If \(H\le1\), this gives the useful upper bound
\[
1-p\le2\delta-\delta^2-L.
\]
For \(0\le\delta\le1\), the stronger-looking expression printed in the note instead satisfies
\[
1-p\ \ge\
2\delta-\delta^2-L+(1-H^{-1}),
\]
not \(\le\). The difference is
\[
\delta(2-\delta)(H^{-1}-1).
\]

### The numerical table does not exactly implement the displayed normalization

At \(x_0=.03\), the supplied entries give
\[
1-\delta=.99451,\qquad \mathcal F_h/(2\pi)=.99459.
\]
These differ beyond their printed rounding. With \(H=.99897\) and the printed flux, the ledger term is approximately
\[
(.99459)^2/.99897=.99023,
\]
rather than the printed \(.99008\).

This establishes a mismatch between the stated formulas and printed columns, not the cause of that mismatch. The absent Step-65 script and full-precision data would be needed to determine whether different domains, pairings, or normalizations were used. A period normalization on a cell alone does not automatically establish the required global \(q_h=1\).

## 2. Exact splitting of the loss

Off \(Z(h)\), define the **block-aligned** SD form
\[
\beta_h=\frac{B^*h}{|h|^2},
\qquad
B_\parallel(v)=\langle\beta_h,v\rangle h,
\qquad B_\perp=B-B_\parallel.
\]
Set
\[
c=\frac{\int|\beta_h||h|^2}{H}.
\]
Then
\[
\boxed{
L_h=\frac1{2\pi^2}\left[
\|B_\perp\|_2^2+
\int_M(|\beta_h|-c)^2|h|^2\,d\mu
\right].
}
\tag{7}
\]
This proves the proposed rank/amplitude splitting, with its normalization made explicit.

The correct amplitude quantity is
\[
|\beta_h|=\frac{|B^*h|}{|h|^2},
\]
**not** \(|B^*h|/|h|\), as stated in Step 65.

For connected \(M\) and nonzero harmonic \(h\), its zero set has measure zero. Thus
\[
L_h=0
\iff
B(v)=c\,\langle\widehat\Omega_0,v\rangle h
\quad\text{off }Z(h),
\tag{8}
\]
where \(c\ge0\) is constant and \(|\widehat\Omega_0|=1\). If \(c=0\), \(B=0\) globally. If \(c>0\), the field is uniquely determined by \(B^*h\).

The notation \(\widehat\Omega_0\otimes h\) is harmless if used for an element of \(\Lambda^+\otimes\Lambda^-\); as an operator, the usual output-first convention gives \(h\otimes\widehat\Omega_0\).

## 3. Proposition 66.Y: correct conformal reduction, incomplete topological justification

Gauss–Bonnet gives
\[
P(g)=2\int|W_g|^2+\frac1{12}\int s_g^2-16\pi^2\chi(M).
\]
For the Yamabe representative \(\widehat g\) of a class with \(Y[g]<0\),
\[
\boxed{
P(g)-P(\widehat g)
=\frac1{12}\left(\int s_g^2-Y[g]^2\right)\ge0.
}
\tag{9}
\]
Equality holds precisely when \(g\) is the negative constant-scalar Yamabe representative, up to scaling.

One direct justification is to write \(g=v^2\widehat g\), let \(s_{\widehat g}=s_0<0\), and use \(\Delta=\nabla^i\nabla_i\):
\[
\int s_g^2-Y[g]^2
=36\int\left(\frac{\Delta v}{v}\right)^2
-12s_0\int\frac{|\nabla v|^2}{v^2}.
\tag{10}
\]
Both terms are nonnegative and equality forces \(v\) constant.

Thus minimizing \(P\) over all metrics reduces to the constant-negative-scalar slice, provided the admissible metric class is preserved by Yamabe replacement. Fixed-volume normalization is compatible with this reduction.

Two qualifications:

* General type does **not** imply \(b^+>1\):
  \[
  b^+(X)=1+2p_g(X).
  \]
  The stated SW justification fails when \(p_g=0\). Extending the conclusion to all minimal general-type surfaces requires the appropriate negative-Yamabe theorem, including the \(b^+=1\) case. Its full statement is not supplied here.
* The parenthetical formula \(3\int(\Delta u/u)^2+24\int|\nabla u|^2\) is not a universal conformal identity as written. Formula (10) shows the required scalar normalization and denominator for an ordinary conformal factor. A different variable or reference normalization must be specified to justify that parenthetical expression.

Yamabe replacement can change \(L_h\) and its equality condition. It reduces the **infimum problem**; it does not classify \(L_h=0\) for nonconstant-scalar metrics.

## 4. Lemma 66.D: correct sign and coefficient

With the script’s conventions
\[
T_{ab}=\phi_{ac}\psi_{cb},
\qquad
(\delta\phi)_c=-\nabla^a\phi_{ac},
\]
normal coordinates give
\[
\nabla^aT_{ab}
=\psi_{bc}(\delta\phi)_c+\phi_{ac}\nabla^a\psi_{cb}.
\]
For SD \(\phi\) and ASD \(\psi\), the second term is a contraction of the Maxwell operator on \(\psi\), and vanishes if \(d\psi=0\). Therefore
\[
\boxed{\operatorname{div}(\phi\circ\psi)=\psi(\delta\phi).}
\tag{11}
\]
The sign is positive and the coefficient is \(1\).

Also,
\[
\psi^2=-\tfrac12|\psi|^2\Id,\qquad
\delta\phi=-*d\phi,
\]
so on \(\{\psi\ne0\}\),
\[
\operatorname{div}(\phi\circ\psi)=0
\iff d\phi=0.
\]

The supplied JSON corroborates the coefficient and all four components for the polynomial specialization. The script chooses specialized random coefficients; it is not a universal symbolic proof. The tensorial calculation supplies that proof. Likewise, a nonclosed control example does not show that the extra term is nonzero for every nonclosed \(\psi\).

## 5. Theorem 66.R: valid with the stated analytic inputs and corrected scope

Assume \(M\) connected, \(h\not\equiv0\), \(L_h=0\), and \(c>0\). Let \(\Omega_0=\sqrt2\,\widehat\Omega_0\). The corresponding tensor has
\[
\Ric^\circ=c'\Omega_0\circ h
\]
for a fixed nonzero \(c'\).

The block-to-tensor conversion must not be confused with an isometric identification: its norm factor is \(2\). In the script’s matrix convention and the usual positive-curvature curvature operator,
\[
B(v)=\langle\beta_h,v\rangle h
\quad\Longrightarrow\quad
\Ric^\circ=-2\beta_h\circ h,
\]
so for (8), \(c'=-\sqrt2c\). Leaving \(c'\) unspecified, as the theorem does, accommodates this sign.

### Bianchi equation and extension

Contracted Bianchi and (11) yield
\[
c'h(\delta\Omega_0)=\frac14ds,
\qquad
\boxed{\delta\Omega_0=-\frac{h(ds)}{2c'|h|^2}.}
\tag{12}
\]
This formula is correct. It determines the Lee form through the usual \(J_0\)-relation; \(\delta\Omega_0\) itself is not the Lee form.

For constant \(s\), \(\Omega_0\) is closed and coclosed off \(Z(h)\). Using the stated nodal-set theorem,
\[
\dim_{\mathrm H}Z(h)\le2,\qquad
\mathcal H^3(Z(h))=0.
\]
Here \(\mathcal H^3\) is **Hausdorff measure**, not cohomology \(H^3\). This gives cutoffs with \(\|d\chi_j\|_{L^1}\to0\). Boundedness of \(\Omega_0\) then makes it distributionally closed and coclosed on \(M\). Elliptic regularity makes it smooth, with \(|\Omega_0|^2=2\) everywhere. It is therefore globally symplectic and compatible with \(g\).

This proves the extension claimed in 66.R, subject to the quoted nodal-set theorem. For a disconnected manifold, nonzero \(h\) somewhere is insufficient: one must impose the hypothesis on each component being classified.

### Structure and converse

The product \(\Omega_0\circ h\) commutes with \(J_0\), hence \(\Ric''=0\). Moreover,
\[
\rho_0=B\Omega_0=\sqrt2c\,h
\]
is harmonic.

Conversely, using the supplied AAD formula
\[
d\rho=*(J\delta\Ric''),
\]
a constant-scalar AK metric with \(\Ric''=0\) has
\[
d\rho_0=0,\qquad
B(v)=\tfrac12\langle\Omega_0,v\rangle\rho_0.
\tag{13}
\]
Thus \(L_h=0\) if \(\rho_0\) is a constant multiple of \(h\). The factor \(1/2\) is correct.

For fixed nonzero \(h\), the precise converse is
\[
L_h=0
\iff
\rho_0=0\ \text{or}\ \rho_0\in\mathbb Rh
\]
within this AK class. Since both forms are harmonic, their class-level and form-level proportionality are equivalent.

The assertion that every resulting \(b=c_1(J_0)\) must be one of the fixed classes \(\pm K_X\pm\sum E_i\) is not established by the supplied Taubes/Li–Liu reference. Fortunately none of (66.3)–(66.5) requires that assertion. Similarly, \(p=|b^-|^2=k+\Pi\) requires the separately specified best-sign hypothesis; only the first equality is automatic for cscK.

## 6. Theorem 66.EM: correct algebra, conditional global equivalence

Distinguish the block form \(\beta_h\) above from the **Ricci-product form** \(\phi_h\), defined by
\[
\Ric^\circ=\phi_h\circ h.
\]
With the preceding conventions, \(\phi_h=-2\beta_h\).

If \(L_{\rm rank}=0\) and \(s\) is constant, (11) proves that \(\phi_h\) is harmonic on \(M\setminus Z(h)\). **If it is locally bounded near \(Z(h)\)**, the same removal argument extends it harmonically to \(M\).

For \(F=\phi_h+h\), SD and ASD skew endomorphisms commute and their squares are scalar. Hence
\[
(F\circ F)_0=2\phi_h\circ h,
\qquad
\boxed{\Ric^\circ=\tfrac12(F\circ F)_0.}
\tag{14}
\]
The factor \(1/2\) is exactly correct for this displayed equation.

Calling (14) Einstein–Maxwell requires stating its sign and field normalization. For example, the alternative convention
\[
(\Ric+\widetilde F\circ\widetilde F)_0=0
\]
is obtained here with
\[
\widetilde F=(\phi_h-h)/\sqrt2.
\]
These are equivalent descriptions after the indicated transformation of the two chiral components.

Conversely, a global harmonic Maxwell field with \(F^-=\lambda h\), for a constant \(\lambda\), has rank-aligned tracefree Ricci tensor, so \(L_{\rm rank}=0\).

**What is not proved:** the unconditional assertion
\[
L_{\rm rank}=0\iff\text{global Einstein–Maxwell}.
\]
The rank condition controls
\[
\int|\phi_h|^2|h|^2,
\]
not boundedness of \(\phi_h\) at zeros of \(h\). Without removability, it yields only an Einstein–Maxwell field on the complement. The theorem’s conditional paragraph is correct; its subsequent unconditional organizational bullets must retain this hypothesis.

For \(L=0\), constant nonzero \(|\phi_h|\) supplies boundedness automatically, and 66.R applies. The conformally Kähler remarks are consistent after fixing field normalization: \(|\omega_K|_g=\sqrt2 f^2\) for \(g=f^{-2}g_K\), so the amplitude loss is a weighted variance of \(f^2\), up to the normalization factor.

## 7. Identities 66.3–66.5 and Corollary 66.S

Suppose \(\rho_0=F\widehat h\), where \(\|\widehat h\|_2=1\), and set
\[
D=(t^-,\widehat h),\qquad
\Phi_b=2\pi(h_b^-,\widehat h).
\]
Then
\[
\boxed{\Phi_b=F+D,\qquad P=2F^2.}
\tag{15}
\]
For \(\Phi_b\ne0\), put \(\delta_b=D/\Phi_b\). Thus
\[
\boxed{
p=\frac{\Phi_b^2}{4\pi^2}(1-\delta_b)^2.
}
\tag{16}
\]
This becomes \(p=|b^-|^2(1-\delta_b)^2\) only when \(\widehat h\parallel h_b^-\).

The signed quantity \(F\) here differs from the nonnegative metric flux:
\[
\mathcal F_{\widehat h}=|F|.
\]
Accordingly, \(\delta_b\) agrees with the Step-65 metric deficit only under the appropriate positive-sign choice.

Using the supplied, algebraically consistent 63.AK identity and
\[
\gamma^-=\rho_0+t^-,
\qquad |t^-|^2=u^2/2,
\]
gives
\[
\boxed{
4FD+\int u(6u+s)
+2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2=0.
}
\tag{17}
\]
Equivalently,
\[
\boxed{
4\Phi_b^2\delta_b(1-\delta_b)
=\int u(-s-6u)
-2\|\rho_*''\|_2^2-4\|W_3^+\|_2^2.
}
\tag{18}
\]
All signs and coefficients in 66.3–66.5 are correct. For general AK metrics the corresponding identity is indeed
\[
\|\Ric''\|_2^2
=4(\rho_0,t^-)+\int u(6u+s)
+2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2.
\]

### Corollary 66.S: proved under its explicit hypotheses

If \(s\ge0\) and \(\Phi_b>0\),
\[
4FD\le-6\int u^2\le-12D^2.
\]
Therefore
\[
D(\Phi_b+2D)\le0,
\qquad
\boxed{-\tfrac12\le\delta_b\le0.}
\]
Consequently
\[
p\ge\frac{\Phi_b^2}{4\pi^2},
\]
and \(p\ge|b^-|^2\) when \(\widehat h\parallel h_b^-\). Also \(\delta_b=0\) iff \(u=0\), hence iff the structure is Kähler. This proves the stated corollary, but does not by itself eliminate every strictly AK member with \(s\ge0\).

### Correct negative-scalar consequence

For \(s<0\), combine (17) with \(\int u^2\ge2D^2\):
\[
\boxed{-s\int u\ge4\Phi_b^2\delta_b(1+2\delta_b).}
\tag{19}
\]
If \(\widehat h\parallel h_b^-\) and
\[
p\le(1-\eta)^2|b^-|^2,\qquad 0<\eta<1,
\]
then
\[
|1-\delta_b|\le1-\eta,
\quad\text{so}\quad
\eta\le\delta_b\le2-\eta,
\]
and (19) implies
\[
-s\int u\ge4\Phi_b^2\eta(1+2\eta).
\]
The note omitted the needed alignment hypothesis for this deduction. On the positively oriented non-Einstein branch \(F>0,\Phi_b>0\), the upper range further reduces to \(\delta_b<1\).

## 8. Proposition 66.W: estimate correct, structural interpretation unproved

For
\[
\Ric^\circ=\phi_h\circ h+R_\perp
\]
and constant \(s\),
\[
h(\delta\phi_h)=-\operatorname{div}R_\perp.
\]
For compactly supported \(\xi\) off \(Z(h)\), skew-adjointness of \(h\) and integration by parts give
\[
\boxed{
|(\delta\phi_h,\xi)|
\le\|R_\perp\|_2
\left\|\nabla(h^{-1}\xi)\right\|_2,
\qquad h^{-1}\xi=-2h(\xi)/|h|^2.
}
\tag{20}
\]
There is no sign error in the absolute-value estimate. With the normalized splitting (7),
\[
\|R_\perp\|_2^2=8\pi^2L_{\rm rank}.
\]

This proves weighted weak closedness and weighted amplitude control. It does **not** prove that a sequence is close to a global AK structure: the test norm degenerates near \(Z(h)\), and no uniform control of the inverse weights, geometry, or nonzero amplitude is supplied. The phrase “weakly close to \((AK_{\rm Ric})\)” should be replaced by these two precise estimates.

## 9. Correct interpretation of §5

For fixed nonzero harmonic ASD \(h\), on the constant-scalar slice the proved set-theoretic classification is
\[
\boxed{
\{L_h=0\}
=
\{\text{Einstein}\}
\;\cup\;
\left\{
\begin{array}{l}
\text{constant-scalar AK metrics with \(J\)-invariant Ricci},\\
\rho_0\in\mathbb Rh
\end{array}
\right\}.
}
\tag{21}
\]
The integrable members of the second set are the aligned cscK metrics; its nonintegrable members are strictly AK. Einstein and AK descriptions can overlap. With \(h\) representing \(a^-\), the harmonic-form condition is equivalent to \([\rho_0]\in\mathbb R a^-\).

The strictly AK part is **a restricted instance of**, not “precisely,” the four-dimensional Blair–Ianus problem. It additionally imposes constant negative scalar curvature, a prescribed manifold, and exceptional-class alignment. The supplied literature descriptions identify no compact strictly AK example satisfying these hypotheses; they do not establish an equivalence between this restricted problem and the unrestricted Blair–Ianus question.

Three further corrections are necessary:

* Nothing proves that strictly AK members have \(0<\delta_b<1\). For \(s<0\), (18) also allows \(\delta_b<0\). The interval \(0<\delta_b<1\) describes the positive-flux **sub-tariff** branch, not all strictly AK equality metrics.
* Nothing constructs a connected \(L=0\) locus or an Einstein–Maxwell path joining cscK to Einstein. The proposed endpoints classify possible objects, not an existing interpolation.
* At \(\delta_b=0\), (17) forces Kählerness for \(s\ge0\), but not for \(s<0\). Thus the converse description “\(\delta_b=0\) is the Kähler end” is unsupported in the relevant negative-scalar regime.

The useful logical observation survives: a universal inequality \(L\ge c\delta\), \(c>0\), excludes Einstein metrics because their metric deficit is \(\delta=1\) and \(L=0\). Positive \(\alpha(M)\) is stronger still than Einstein nonexistence. The remaining mathematical objects are therefore precise: removability for the rank-only field, quantitative compactness/coercivity for (20), and existence or integrability of the aligned constant-negative-scalar AK class. The supplied identities alone settle none of those three issues.