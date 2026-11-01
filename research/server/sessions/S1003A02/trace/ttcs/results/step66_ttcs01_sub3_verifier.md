# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/scripts/step66_rank1_bianchi_check.py",
    "Sessions/S1003A02/workspace/data/step66_rank1_bianchi_check.json"
  ]
}
```

## Task

Verify, as a careful differential geometer, the identities and theorems in two notes about the Einstein-defect ledger on M = X#kCP̄² (X minimal general type). (1) Step-65 identities 65.1–65.3 (file step65_cell_exceptional_flux_ledger.md §1): the claim that for every orthogonal J the ASD part of R(Ω) equals B_gΩ (B_g the Ric° block Λ⁺→Λ⁻), the metric-only pairing ⟨t_J⁻,h⟩ = 2π⟨a,h⟩ − ∫⟨Ω,B*h⟩, the definition 𝔉_h=√2∫|B*h|, the Cauchy–Schwarz bound P/2 ≥ 𝔉²/‖h‖² (check the constant using |Ric°|²=4|B|²), and the ledger p=(1−δ)²/‖h‖²+L. (2) Step-66 (file step66_rank_one_exceptional_ricci_rigidity.md): Prop 66.Y (WLOG constant scalar curvature since P(g)−P(ĝ)=(1/12)(∫s²−Y²)≥0 for Y<0); Lemma 66.D div(φ∘ψ)=ψ(δφ) for SD φ and closed ASD ψ (symbolic check JSON supplied); the splitting L = L_rank + L_amp and the equality characterization B = cΩ̂₀⊗h; Theorem 66.R (constant s ⇒ Ω₀ closed hence almost-Kähler with J-invariant Ricci, ρ₀ ∝ h harmonic; extension across Z(h) via H³(Z)=0; converse via AAD (26) dρ=*(JδRic'')); Theorem 66.EM (L_rank=0 with constant s ⇔ Riemannian Einstein–Maxwell Ric°=φ∘h=½(F∘F)₀ with F=φ+h harmonic; check the factor ½ and the boundedness hypothesis near Z(h)); identities (66.3)–(66.5) obtained by inserting γ⁻=ρ₀+t⁻ into Prop 63.AK P=2‖γ⁻‖²+∫u(5u+s)+2‖ρ*''‖²+4‖W₃‖² with |t⁻|²=u²/2 and P=2‖ρ₀‖² when Ric''=0; Corollary 66.S (s≥0 ⇒ δ_b∈[−½,0], Kahler tariff p≥|b⁻|²); Prop 66.W weak estimate. Report precisely any sign, factor, quantifier, or regularity error, whether each statement is proved as written, and the corrected statement where needed. Also judge whether the interpretation in §5 (equality class = Einstein ∪ cscK ∪ strictly-AK J-invariant-Ricci with [ρ₀]∥a⁻; strictly-AK part = the open 4D Blair–Ianus problem at negative constant s) is accurate.

## Output

# Differential-geometric verification memo

Let \((\,\cdot\,,\,\cdot\,)_{L^2}\) denote the \(L^2\) pairing of forms, and use the curvature-operator decomposition
\[
\mathcal R=
\begin{pmatrix}
W^++\frac{s}{12} & B^*\\[2mm]
B & W^-+\frac{s}{12}
\end{pmatrix},
\qquad
B:\Lambda^+\longrightarrow \Lambda^-,
\qquad
|\Ric^\circ|^2=4|B|^2.
\]

## 1. Step 65: frame flux and the exact ledger

### 1.1 The ASD curvature block and (65.1)

For \(\Omega\in\Lambda^+\),
\[
(\mathcal R\Omega)^-=B\Omega.
\]
There is no extra factor \(1/2\) here: that factor is already incorporated into the identification of \(B\) with \(\Ric^\circ\). With the primitive Ricci-form convention of Steps 63–66,
\[
\rho_0^J=B\Omega,
\qquad
|\rho_0^J|^2=\frac12|\Ric_0'|^2.
\]

From
\[
\gamma_J^- = B\Omega+t_J^-,
\qquad
H(\gamma_J^-)=2\pi h_a^-,
\]
testing against a harmonic ASD form \(h\) gives
\[
(t_J^-,h)_{L^2}
=
2\pi(h_a^-,h)_{L^2}
-
\int_M\langle B\Omega,h\rangle\,d\mu
=
2\pi(h_a^-,h)_{L^2}
-
\int_M\langle\Omega,B^*h\rangle\,d\mu.
\tag{1}
\]
Thus (65.1) is correct provided \(\langle a,h\rangle\) denotes the Hodge \(L^2\) pairing \((h_a^-,h)_{L^2}\).

If instead \(\langle a,[h]\rangle\) denotes the ordinary intersection pairing, then, since \(h\) is ASD,
\[
\int_M h_a\wedge h=-(h_a^-,h)_{L^2},
\]
and the topological term in (1) is \(-2\pi\,a\cdot[h]\). The note should state explicitly which pairing is intended.

Since \(|\Omega|=\sqrt2\),
\[
\left|\int_M\langle\Omega,B^*h\rangle\right|
\le \sqrt2\int_M|B^*h|
=:\mathcal F_h,
\]
so
\[
(t_J^-,h)_{L^2}\ge 2\pi(h_a^-,h)_{L^2}-\mathcal F_h.
\]
This holds for every orthogonal \(J\) with the specified \(c_1(J)\).

### 1.2 The Cauchy–Schwarz coefficient

Pointwise,
\[
|B^*h|\le |B|\,|h|.
\]
Consequently,
\[
\begin{aligned}
\mathcal F_h^2
&=2\left(\int_M|B^*h|\right)^2\\
&\le
2\left(\int_{\operatorname{supp}B}|B|\,|h|\right)^2\\
&\le
2\left(\int_M|B|^2\right)
\left(\int_{\operatorname{supp}B}|h|^2\right)\\
&=\frac{P}{2}\,
\|h\|^2_{L^2(\operatorname{supp}\Ric^\circ)}.
\end{aligned}
\]
Therefore
\[
\boxed{\quad
\frac P2\ge
\frac{\mathcal F_h^2}
{\|h\|^2_{L^2(\operatorname{supp}\Ric^\circ)}}
\quad}
\]
with exactly the coefficient appearing in Step 65. Using the full norm \(H=\|h\|_2^2\) gives the slightly weaker but globally cleaner inequality
\[
\frac P2\ge\frac{\mathcal F_h^2}{H}.
\tag{2}
\]
The full norm is the one compatible with the Step-66 equality analysis and remains meaningful when \(B=0\).

### 1.3 Correct normalization of (65.3)

For arbitrary nonzero \(h\), put
\[
q_h:=(h_a^-,h)_{L^2}>0,\qquad H:=\|h\|_2^2,
\qquad
\delta_h:=1-\frac{\mathcal F_h}{2\pi q_h}.
\]
Then define
\[
L_h:=
\frac1{4\pi^2}
\left(
\frac P2-\frac{\mathcal F_h^2}{H}
\right)\ge0.
\]
Since \(p=P/(8\pi^2)\),
\[
\boxed{\quad
p=\frac{q_h^2}{H}(1-\delta_h)^2+L_h.
\quad}
\tag{3}
\]

Thus the displayed Step-65 formula
\[
p=\frac{(1-\delta)^2}{\|h\|^2}+L
\]
is correct only under the normalization
\[
(h_a^-,h)_{L^2}=1.
\]
This appears to be the normalization used in the numerical table: its “Hodge” column is exactly \((1-\delta)^2/\|h\|^2\).

There is a notational mismatch if \(\delta\) is defined using \(\langle a,\widehat h\rangle\) with \(\widehat h=h/\|h\|\), while \(\mathcal F_h\) is still formed from unnormalized \(h\). A scale-invariant alternative is
\[
\widehat h=\frac h{\|h\|},\qquad
q=(h_a^-,\widehat h),\qquad
\delta=1-\frac{\mathcal F_{\widehat h}}{2\pi q},
\]
which yields
\[
p=q^2(1-\delta)^2+L_{\widehat h}.
\]

### 1.4 What the two parts of \(L\) measure

Off \(Z(h)\), define
\[
\varphi_h:=\frac{B^*h}{|h|^2}\in\Lambda^+,
\qquad
B_\parallel(v):=\langle\varphi_h,v\rangle h,
\qquad
B_\perp:=B-B_\parallel.
\]
Then
\[
|B_\parallel|^2=\frac{|B^*h|^2}{|h|^2}.
\]
Writing
\[
Q:=\int|B|^2-\frac{\left(\int|B^*h|\right)^2}{H},
\qquad
L=\frac{Q}{2\pi^2},
\]
one has
\[
Q=
\underbrace{
\int\left(
|B|^2-\frac{|B^*h|^2}{|h|^2}
\right)}_{Q_{\rm rank}=\|B_\perp\|_2^2}
+
\underbrace{
\left[
\int|\varphi_h|^2|h|^2
-
\frac{\bigl(\int|\varphi_h||h|^2\bigr)^2}{H}
\right]}_{Q_{\rm amp}}.
\tag{4}
\]
Moreover,
\[
Q_{\rm amp}
=
\int (|\varphi_h|-c)^2|h|^2,
\qquad
c=\frac{\int|\varphi_h||h|^2}{H}.
\]

Hence \(L=0\) exactly when
\[
B(v)=c\,\langle\widehat\Omega_0,v\rangle h
\tag{5}
\]
for a constant \(c\ge0\) and a unit SD field \(\widehat\Omega_0\) on \(M\setminus Z(h)\). Formula (5) removes the tensor-order ambiguity in the note: under the usual convention \(u\otimes v:x\mapsto u\langle v,x\rangle\), one writes \(B=c\,h\otimes\widehat\Omega_0\), not \(c\,\widehat\Omega_0\otimes h\).

The amplitude quantity that must be constant is
\[
\frac{|B^*h|}{|h|^2}=|\varphi_h|,
\]
not \(|B^*h|/|h|\). Step 66 uses the correct weighted-variance formulation.

---

## 2. Step 66

### 2.1 Proposition 66.Y

Gauss–Bonnet gives
\[
P(g)
=
2\int_M|W_g|^2\,d\mu_g
+\frac1{12}\int_Ms_g^2\,d\mu_g
-16\pi^2\chi(M).
\]
Because \(\int|W|^2\) is conformally invariant in dimension four, if \(\widehat g\) is the Yamabe representative of \([g]\), then
\[
P(g)-P(\widehat g)
=
\frac1{12}
\left(
\int s_g^2\,d\mu_g-Y[g]^2
\right).
\tag{6}
\]
For \(Y[g]<0\),
\[
\int s_g^2\ge \int (s_g^-)^2\ge Y[g]^2,
\]
and equality occurs exactly when \(g\) is, up to scale, the constant-scalar Yamabe metric. Thus Proposition 66.Y is correct.

The reduction of \(\alpha(M)\) to constant-scalar metrics is valid provided the allowed metric class is preserved under conformal Yamabe replacement; fixed-volume normalization causes no problem because \(P\) is scale invariant.

One topological sentence needs refinement. A minimal complex surface of general type has
\[
b^+(X)=1+2p_g(X),
\]
so general type alone does not imply \(b^+>1\). Surfaces with \(p_g=0\) have \(b^+=1\). If the running assumptions include \(b^+>1\), the stated SW argument applies. Otherwise a separate LeBrun result covering the \(b^+=1\) case is needed to conclude that every conformal class has \(Y[g]<0\).

### 2.2 Lemma 66.D

With
\[
T_{ab}=(\phi\circ\psi)_{ab}=\phi_{ac}\psi_{cb},
\qquad
(\delta\phi)_c=-\nabla^a\phi_{ac},
\]
one obtains in normal coordinates
\[
\nabla^aT_{ab}
=
\psi_{bc}(\delta\phi)_c
+
\phi_{ac}\nabla^a\psi_{cb}.
\]
For \(\phi\) SD and \(\psi\) ASD, the second summand is the opposite-chirality Maxwell operator on \(\psi\); it vanishes when \(d\psi=0\). Since a closed ASD form is also coclosed,
\[
\boxed{\quad
\operatorname{div}(\phi\circ\psi)=\psi(\delta\phi).
\quad}
\tag{7}
\]
The coefficient and sign are correct.

The supplied JSON confirms \(\kappa_1=1\), symmetry, trace zero, and all four components for the symbolic specialization. The universal proof is the normal-coordinate or spinor calculation; the random polynomial computation is a useful coefficient test rather than a replacement for that calculation.

Since
\[
\psi^2=-\frac12|\psi|^2\operatorname{Id},
\]
\(\psi\) is invertible wherever nonzero. Thus
\[
\operatorname{div}(\phi\circ\psi)=0
\iff
\delta\phi=0
\iff
d\phi=0
\]
on \(\{\psi\ne0\}\), the last equivalence using self-duality of \(\phi\).

### 2.3 Theorem 66.R

Assume \(L_h=0\) and \(c>0\). With \(\Omega_0=\sqrt2\,\widehat\Omega_0\), the rank-one condition can be written
\[
\Ric^\circ=c'\,\Omega_0\circ h
\tag{8}
\]
for a constant \(c'\ne0\).

The contracted Bianchi identity gives
\[
\operatorname{div}\Ric^\circ=\frac14ds.
\]
Applying (7),
\[
c'h(\delta\Omega_0)=\frac14ds.
\]
Since \(h^{-1}=-2h/|h|^2\),
\[
\boxed{\quad
\delta\Omega_0
=
-\frac{h(ds)}{2c'|h|^2}.
\quad}
\tag{9}
\]
The formula is correct. Strictly speaking, \(\delta\Omega_0\) itself is not the Lee form; the almost-Hermitian Lee form is \(\pm J_0\delta\Omega_0\), depending on convention.

If \(s\) is constant, then \(\delta\Omega_0=0\). Self-duality gives \(d\Omega_0=0\) off \(Z(h)\).

The removal argument is also sound, with one notational correction: what is required is
\[
\mathcal H^3(Z(h))=0
\]
for three-dimensional Hausdorff measure, not ordinary cohomology \(H^3(Z(h))\). Bär’s nodal-set theorem supplies Hausdorff dimension at most two. One can therefore choose cutoffs \(\chi_j\) with
\[
\|d\chi_j\|_{L^1}\longrightarrow0.
\]
Because \(\Omega_0\) is bounded and closed/coclosed off \(Z(h)\), it is closed and coclosed distributionally on \(M\). Elliptic regularity makes it smooth. Since \(|\Omega_0|^2=2\) almost everywhere, smoothness implies \(|\Omega_0|^2\equiv2\); hence it is symplectic and defines a global compatible almost-complex structure.

From (8), \(\Ric^\circ\) commutes with \(J_0\), so the Ricci tensor is \(J_0\)-invariant. Also
\[
\rho_0=B(\Omega_0)=C h
\]
for a constant \(C\), and is therefore harmonic.

Conversely, for a constant-scalar almost-Kähler metric with \(J_0\)-invariant Ricci tensor, AAD’s formula
\[
d\rho=*(J\delta\Ric'')
\]
gives \(d\rho=0\). Since
\[
\rho=\frac{s}{4}\Omega_0+\rho_0,
\]
with \(s\) constant and \(d\Omega_0=0\), \(\rho_0\) is closed; being ASD, it is harmonic. Algebraically,
\[
B(v)=\frac12\langle\Omega_0,v\rangle\rho_0.
\tag{10}
\]
Thus \(L_h=0\) whenever \(h\) is a constant multiple of \(\rho_0\). This proves the converse, including the factor \(1/2\) in (10).

### 2.4 The Einstein–Maxwell layer

Suppose
\[
\Ric^\circ=\phi_h\circ h,
\]
with \(\phi_h\) SD and \(h\) ASD. For
\[
F=\phi_h+h,
\]
self-dual and anti-self-dual endomorphisms commute, while
\[
\phi_h^2=-\frac12|\phi_h|^2\operatorname{Id},
\qquad
h^2=-\frac12|h|^2\operatorname{Id}.
\]
Therefore
\[
(F\circ F)_0
=
\phi_h\circ h+h\circ\phi_h
=
2\phi_h\circ h,
\]
and hence
\[
\boxed{\quad
\Ric^\circ=\frac12(F\circ F)_0.
\quad}
\tag{11}
\]
The factor \(1/2\) is correct for the displayed field equation.

With \(s\) constant, (7) gives \(h(\delta\phi_h)=0\) off \(Z(h)\), hence \(d\phi_h=\delta\phi_h=0\) there. If \(\phi_h\) is locally bounded near \(Z(h)\), the same Hausdorff-measure cutoff argument extends it to a smooth harmonic SD form. Thus \(F\) is harmonic.

The boundedness assumption is materially used. \(L_{\rm rank}=0\) alone allows the quotient \(B^*h/|h|^2\) to grow near zeros of \(h\); the supplied proof does not remove such singular behavior without additional integrability.

Different Einstein–Maxwell references place a sign or scalar coefficient in front of \((F\circ F)_0\). Equation (11) is internally correct; calling it the standard Einstein–Maxwell equation requires declaring that convention. The rank-one/harmonic equivalence is unchanged after rescaling the SD and ASD components appropriately.

Conversely, if an Einstein–Maxwell field has \(F^-=\lambda h\) for a constant \(\lambda\), then its tracefree Ricci tensor is a rank-one product of \(F^+\) and \(h\), so \(L_{\rm rank}=0\). The case \(\lambda=0\) is the Einstein subcase.

### 2.5 Identities (66.3)–(66.5)

Assume \(\widehat h\) is \(L^2\)-unit and
\[
\rho_0=F\widehat h,\qquad
D=(t^-,\widehat h),\qquad
\Phi_b=2\pi(h_b,\widehat h).
\]
Since \(\gamma^-=\rho_0+t^-\),
\[
\boxed{\Phi_b=F+D.}
\tag{12}
\]

When \(\Ric''=0\),
\[
P=2\|\rho_0\|^2=2F^2,
\]
and therefore
\[
\boxed{
p=\frac{F^2}{4\pi^2}
=
\langle h_b,\widehat h\rangle^2(1-\delta_b)^2,
\qquad
\delta_b=\frac D{\Phi_b}.
}
\tag{13}
\]
If \(\widehat h\) is parallel to \(h_b^-\), this becomes
\[
p=|b^-|^2(1-\delta_b)^2.
\]

For an almost-Kähler structure,
\[
t^-=(-a\wedge Ja)^-,
\qquad
|t^-|^2=\frac12u^2,
\qquad
u=|a|^2.
\]
Substituting \(\gamma^-=\rho_0+t^-\) and \(P=2\|\rho_0\|^2\) into Proposition 63.AK gives
\[
\boxed{
4FD+\int u(6u+s)
+2\|\rho_*''\|^2
+4\|W_3^+\|^2=0.
}
\tag{14}
\]
Using \(F=\Phi_b(1-\delta_b)\) and \(D=\Phi_b\delta_b\),
\[
\boxed{
4\Phi_b^2\delta_b(1-\delta_b)
=
\int u(-s-6u)
-2\|\rho_*''\|^2
-4\|W_3^+\|^2.
}
\tag{15}
\]
All coefficients in (66.3)–(66.5) are correct.

For general almost-Kähler metrics,
\[
P=2\|\rho_0\|^2+\|\Ric''\|^2,
\]
and the same calculation gives
\[
\|\Ric''\|^2
=
4\langle\rho_0,t^-\rangle
+\int u(6u+s)
+2\|\rho_*''\|^2
+4\|W_3^+\|^2,
\]
also with the stated coefficients.

### 2.6 Corollary 66.S

For \(s\ge0\), equation (14) gives
\[
4FD
\le -6\int u^2.
\]
Since \(\widehat h\) is unit,
\[
D^2\le\|t^-\|^2=\frac12\int u^2,
\]
so
\[
4FD\le-12D^2.
\]
Equivalently,
\[
D(F+3D)=D(\Phi_b+2D)\le0.
\]
If \(\Phi_b>0\), division by \(\Phi_b^2\) yields
\[
\delta_b(1+2\delta_b)\le0,
\qquad
\boxed{\delta_b\in[-1/2,0].}
\tag{16}
\]
Then
\[
p=\frac{\Phi_b^2}{4\pi^2}(1-\delta_b)^2
\ge\frac{\Phi_b^2}{4\pi^2}.
\]
When \(\widehat h\parallel h_b^-\),
\[
\boxed{p\ge|b^-|^2.}
\]
If \(\delta_b=0\), equation (14) becomes a sum of terms that are all at least zero, so \(u=0\), and the structure is Kähler. Conversely, Kähler implies \(t^-=0\) and \(\delta_b=0\). Corollary 66.S is therefore correct as written, with the explicit assumptions \(\Phi_b>0\) and \(\|\widehat h\|_2=1\).

### 2.7 Proposition 66.W

Write
\[
\Ric^\circ=\phi_h\circ h+R_\perp
\]
off \(Z(h)\), with \(R_\perp\) orthogonal to the \(h\)-rank-one component. Constant \(s\) gives
\[
h(\delta\phi_h)=-\operatorname{div}R_\perp.
\]
For a compactly supported one-form \(\xi\) off \(Z(h)\), put
\[
\eta=h^{-1}\xi=-\frac{2h(\xi)}{|h|^2}.
\]
Using skew-adjointness of \(h\) and integration by parts,
\[
\begin{aligned}
(\delta\phi_h,\xi)
&=(\delta\phi_h,h\eta)\\
&=-(h\delta\phi_h,\eta)\\
&=(\operatorname{div}R_\perp,\eta)\\
&=-(R_\perp,\nabla\eta).
\end{aligned}
\]
Hence
\[
\boxed{
|(\delta\phi_h,\xi)|
\le
\|R_\perp\|_2
\left\|\nabla(h^{-1}\xi)\right\|_2.
}
\tag{17}
\]
This is correct. It is an \(H^{-1}\)-type estimate with weights singular near \(Z(h)\). The sentence saying that near equality is “weakly close” to the almost-Kähler equality structure is heuristic unless a topology and uniform control of \(h^{-1}\) and \(\nabla h\) are supplied; equation (17) itself is rigorous.

---

## 3. Interpretation of the equality class and the Blair–Ianus problem

On the constant-scalar slice and for the full-norm ledger, the set-theoretic description is correct:

1. \(B=0\), equivalently \(\Ric^\circ=0\): Einstein metrics.

2. \(B\ne0\) and \(L_h=0\): constant-scalar almost-Kähler metrics with \(J\)-invariant Ricci tensor and
   \[
   \rho_0=C h,
   \qquad\text{equivalently}\qquad
   [\rho_0]\in\mathbb R[a^-].
   \]

3. Inside item 2, the integrable members are cscK metrics satisfying the same cohomological alignment; the remaining members are strictly almost-Kähler.

Two interpretive phrases should be weakened mathematically:

- The classification does not construct a connected family from the Kähler endpoint to the Einstein endpoint, nor does it establish existence for any intermediate value \(0<\delta_b<1\). It classifies what an individual \(L=0\) metric must be.

- The strictly almost-Kähler equality metrics form a special subproblem of the four-dimensional Blair–Ianus question, not the whole question. They carry the extra requirements
  \[
  s=\text{constant}<0,
  \qquad
  [\rho_0]\in\mathbb R[a^-].
  \]
  Blair–Ianus asks for integrability of all compact almost-Kähler four-manifolds with \(J\)-invariant Ricci tensor, without these two extra requirements. An affirmative Blair–Ianus theorem would eliminate the strict equality branch, while a general Blair–Ianus counterexample need not satisfy the exceptional-class alignment used here.

The literature description supplied in the notes is otherwise consistent: local strictly almost-Kähler models with \(J\)-invariant Ricci do not produce compact examples, and no compact four-dimensional strictly almost-Kähler example of this type is identified in the cited material. The equality problem therefore lies inside the unresolved \(s<0\) Blair–Ianus/Goldberg landscape, but is a more specialized existence problem.

## Bottom line

- The curvature-block identity, frame pairing, flux estimate, divergence identity, Yamabe reduction, rigidity mechanism, Einstein–Maxwell algebra, equations (66.3)–(66.5), Corollary 66.S, and estimate (66.6) all have the correct principal signs and numerical factors.
- The ledger requires a stated normalization of \(h\); for arbitrary \(h\), equation (3) is the correct formula.
- The weighted amplitude quantity is \(|B^*h|/|h|^2\).
- The removal argument requires Hausdorff measure \(\mathcal H^3(Z(h))=0\).
- The \(b^+>1\) justification does not cover every minimal surface of general type unless that hypothesis is separately imposed.
- The Blair–Ianus interpretation is structurally apt but is an inclusion into that open problem, not an equivalence with its full four-dimensional form.