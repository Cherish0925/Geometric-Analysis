# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md",
    "Sessions/S1003A02/workspace/scripts/step60_EH_obstruction_pairing.py",
    "Sessions/S1003A02/workspace/scripts/step60_EH_sector_check.py",
    "Sessions/S1003A02/workspace/data/step60_EH_obstruction_pairing.json",
    "Sessions/S1003A02/workspace/scripts/step61_EH_cokernel_norm.py",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify Theorem 61.EH in Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md: a sharp lower bound for the Einstein defect P(g)=∫|Ric°|² near an Eguchi–Hanson desingularization of an R^4/Z2 point of an orbifold that is Einstein near p, together with a matching upper bound. Check, with explicit computation where possible:
(1) Normalizations. Is Omega=(e^03−e^12)/r^4=−(1/4)d(σ3/r²) exactly ASD and harmonic on EH_a for every a, with the stated EH metric and the convention dσ3=σ1∧σ2? Do the o_i=Ω∘ω_i span Ozuch's O(eh) (compare Ozuch §1.2.2, o_k=−θ_1^−∘θ_k^+/r^4+…)? Is ||o_i||²=π²/a⁴ correct, with RP³ level sets of volume π²r³? Are the o_i mutually orthogonal?
(2) The flux pairing. Is B_i=∫_EH⟨DRic_EH[ĥ],o_i⟩=π²(R⁺ζ)_i, as computed in step60_EH_obstruction_pairing.py, correctly a flux at infinity? Check independence of the extension, the factor 1/2 for Z2, c0=0, and consistency with Ozuch's λ_k=c⟨R⁺(H₂)ζ,ζ_(k)⟩ in (22). Is the scaling ⟨Ric°(g̃),ô⟩=a²B correct in y=x/a units, with P scale-invariant? Is the resulting lower bound P ≥ π²a⁴|R⁺ζ|²(1−…) correct in its constant?
(3) Error bookkeeping in proof (a). The weighted neighbourhood with weight w<2; the claim that the order-a⁴ part of Ric° in 1≪|y|≤Λ vanishes by the Einstein jet equation, so E=O(a⁴); the linear term ⟨k,DRic*_{g̃}ô⟩ and the quadratic term; the cutoff of ô inside the region g̃=g_V. Find any genuine gap, e.g. diffeomorphism or gauge issues (P is diffeomorphism invariant but the neighbourhood is gauge-dependent), or whether ô must be corrected to remain approximately in ker DRic*_{g̃}.
(4) The upper bound (b) via Ozuch Lemma 2.3. Is Ric°(g*)=a²Σλ_k o_k+R₄ legitimate given that Ozuch's P=DRic+δ*B is gauged (does B(ĥ₂)=0 hold, or does δ*Bĥ₂ add a Ric° term)? Is λ_k=(R⁺ζ)_k in our o-normalization? Is the O(a⁶) remainder right?
(5) Consequences in §3. Is R⁺=I on the round unit S⁴, giving 2π²a⁴ for CP²#CP²? For KE orbifolds, is R⁺=diag(Λ,0,0) and is the holomorphic resolution direction ζ=ω̂ (versus ζ⊥ω)? Is the relation to Ozuch's Theorem 0.2 second obstruction diag(0,0,Λ) correct? Is the claimed Burns/EH duality on the kernel stratum (maximal Burns saving −(μ2−μ3)²/2 at μ2μ3=0; zero saving at the isotropic AdS-Taub-bolt type) arithmetically right and correctly interpreted?
Give corrected statements where needed.

## Output

# Scientific verification memo: Theorem 61.EH

## Overall assessment

The normalization
\[
B_i=\pi^2(R_p^+\zeta)_i,\qquad \|o_i\|_{L^2(EH_1)}^2=\pi^2
\]
is consistent with the displayed Eguchi–Hanson metric, the \(\mathbb Z_2\) quotient, and the conventions used by `step60_EH_obstruction_pairing.py`. Consequently, the projected lower coefficient
\[
\pi^2a^4|R_p^+\zeta|^2
\]
is correct.

The lower-bound mechanism is mathematically sound, but several estimates in the written proof need repair. Most are bookkeeping corrections and do not alter the coefficient. The principal substantive problem is in part (b): for a generic naïve center \(\widetilde g_{a,\zeta}\), the Ozuch first-order correction differs from it by \(O(a^2)\) in the scaled EH core, so the constructed metric belongs to \(\mathcal N_C\), not to \(\mathcal N_{Ca^{2-w}}\). Thus the displayed matching infimum over shrinking neighborhoods is not established unless the center is redefined to be the adapted Einstein-modulo-obstruction approximation.

---

## 1. Eguchi–Hanson normalization

Write
\[
e^0=\frac{dr}{\sqrt f},\qquad
e^1=\frac r2\sigma_1,\qquad
e^2=\frac r2\sigma_2,\qquad
e^3=\frac{r\sqrt f}{2}\sigma_3,
\quad f=1-\frac{a^4}{r^4}.
\]
Using \(d\sigma_3=\sigma_1\wedge\sigma_2\),
\[
\begin{aligned}
d\!\left(\frac{\sigma_3}{r^2}\right)
&=\frac{\sigma_1\wedge\sigma_2}{r^2}
-\frac{2\,dr\wedge\sigma_3}{r^3}\\
&=\frac4{r^4}e^{12}-\frac4{r^4}e^{03}
=-\frac4{r^4}(e^{03}-e^{12}).
\end{aligned}
\]
Hence
\[
\Omega=-\frac14d(\sigma_3/r^2)
=\frac{e^{03}-e^{12}}{r^4}
\]
exactly for every \(a\). The cancellation of \(f\) is exact.

With orientation \(e^{0123}>0\),
\[
*e^{03}=e^{12},\qquad *e^{12}=e^{03},
\]
so \(*\Omega=-\Omega\). Since \(d\Omega=0\),
\[
d^*\Omega=-*d*\Omega=*d\Omega=0.
\]
Thus \(\Omega\) is harmonic. It is smooth across the bolt; although \(\sigma_3/r^2\) itself is not a smooth global potential there, its differential is the standard smooth \(L^2\) harmonic two-form.

### The tensors \(o_i\)

Let \(J_i\) denote the skew endomorphism associated with the parallel self-dual form \(\omega_i\). An ASD endomorphism commutes with every SD endomorphism, so
\[
o_i=\Omega J_i
\]
is symmetric. It is trace-free because the product of commuting SD and ASD skew endomorphisms lies in
\(\Lambda^+\otimes\Lambda^-\cong\operatorname{Sym}_0^2\). The usual hyperkähler Weitzenböck identification gives \(P_{EH}o_i=0\), and \(o_i\) is TT.

Pointwise,
\[
(r^4\Omega)^2=-I,\qquad
J_iJ_j=-\delta_{ij}I+\epsilon_{ijk}J_k.
\]
Therefore
\[
\langle o_i,o_j\rangle
=\operatorname{tr}(\Omega^2J_iJ_j)
=\frac4{r^8}\delta_{ij}.
\]
This proves both
\[
|o_i|^2=\frac4{r^8}
\]
and mutual pointwise orthogonality.

The volume form is
\[
dV_{EH}=\frac{r^3}{8}\,dr\,\sigma_1\wedge\sigma_2\wedge\sigma_3.
\]
For the \(\psi\)-period \(2\pi\), corresponding to \(S^3/\mathbb Z_2=\mathbb{RP}^3\),
\[
\int_{\mathbb{RP}^3}\frac18\,\sigma_1\wedge\sigma_2\wedge\sigma_3=\pi^2.
\]
Thus
\[
\|o_i\|_{L^2(EH_a)}^2
=4\pi^2\int_a^\infty r^{-5}\,dr
=\frac{\pi^2}{a^4}.
\]

This is the norm of the fixed tensor \(\Omega\circ\omega_i\). The natural period variation on \(EH_a\) is proportional to \(a^2o_i\), whose \(L^2\) norm is scale invariant. That distinction should be stated explicitly.

### Comparison with Ozuch

Ozuch §1.2.2 gives three \(L^2\) infinitesimal EH variations with leading terms
\[
O_k^4=-\frac{\theta_1^-\circ\theta_k^+}{r^4}.
\]
The tensors above span exactly the same three-dimensional space. Depending on the sign used to convert two-forms to skew endomorphisms and on the labeling of \(\theta_1^-\), the individual basis tensors differ by a common sign. At scale \(a\), they also differ from Ozuch’s natural period-normalized basis by a factor \(a^{-2}\). Neither affects the span or the squared gap coefficient, but the basis sign must remain consistent when writing the individual \(\lambda_k\).

The supplied `step61_EH_cokernel_norm.py` correctly implements the metric, the ASD calculation, and the volume integral. Its docstring says that mutual orthogonality is numerically tested, but the supplied script does not actually contain that final computation or save it to JSON. The algebra above supplies the missing verification.

---

## 2. The flux pairing

Let two extensions differ by \(q=O(r^{-2+\varepsilon})\), with corresponding derivative decay. Since \(DRic^*_{EH}o_i=0\),
integration by parts over \(\{r\le R\}\) reduces their pairing difference to a surface integral at \(r=R\). Its terms have sizes
\[
q\,\nabla o_i\,R^3=O(R^{-4+\varepsilon}),\qquad
\nabla q\,o_i\,R^3=O(R^{-4+\varepsilon}),
\]
and hence tend to zero. The pairing is independent of the extension.

The EH metric and \(o_i\) approach their flat models rapidly enough that the limiting surface flux is the flat one computed from \((h_2,o_i^{\rm flat})\).

### Factor \(1/2\), \(c_0=0\), and the script

The moment formula in `step60_EH_obstruction_pairing.py` integrates over the full unit \(S^3\), whose area is \(2\pi^2\). Multiplication by \(1/2\) is therefore exactly the \(\mathbb Z_2\) quotient factor.

For a radial cutoff \(\phi\), homogeneity gives
\[
\int_{S_r^3}\langle DRic(\phi h_2),o_i\rangle
=c_{2,i}\,r\phi''+c_{1,i}\phi'
+c_{0,i}\frac{\phi}{r}.
\]
The Einstein quadratic jet satisfies
\[
DRic_{\rm flat}(h_2)=\Lambda\delta,
\]
so its contraction with trace-free \(o_i\) vanishes. This accounts for \(c_{0,i}=0\). Since \(\phi\) rises from \(0\) to \(1\),
\[
\int_0^\infty \bigl(c_2r\phi''+c_1\phi'\bigr)\,dr=c_1-c_2.
\]
After the quotient factor, the JSON gives
\[
\begin{aligned}
B_0&=\pi^2\left(\frac s{12}+W^+_{11}\right),\\
B_1&=\pi^2W^+_{12},\\
B_2&=\pi^2W^+_{13}.
\end{aligned}
\]
Thus
\[
B_i=\pi^2(R_p^+\zeta)_i.
\]
The generic symbolic calculation contains variables for \(W^-\) and the traceless-Ricci block, and their absence from the output establishes that those sectors do not contribute. The separate sector script only samples explicit tensors, but the main symbolic script is already general.

### Normal coordinates versus Bianchi coordinates

The phrase “Bianchi/normal coordinates” is not literally correct. For example, for constant sectional curvature \(\kappa\),
\[
h_{2,ij}=-\frac{\kappa}{3}(\delta_{ij}r^2-x_ix_j)
\]
is the geodesic-normal quadratic jet, and \(B_\delta h_2\) is a nonzero linear one-form, up to the global curvature-sign convention.

This does not change the flux. The Bianchi representative differs by
\[
\mathcal L_X\delta,\qquad X=O(r^3).
\]
Extending \(X\) smoothly over EH gives
\[
\mathcal L_XEH=\mathcal L_X\delta+O(r^{-2}),
\]
and
\[
DRic_{EH}(\mathcal L_XEH)=\mathcal L_XRic(EH)=0.
\]
Extension independence therefore shows that the pure-gauge quadratic term has zero flux. The script may use the normal-coordinate representative, while Ozuch uses the Bianchi representative, with the same \(B_i\).

### Relation with Ozuch’s \(\lambda_k\)

At \(a=1\),
\[
\lambda_i\|o_i\|^2=B_i,
\]
so in the basis used by the script,
\[
\lambda_i=(R_p^+\zeta)_i.
\]
Ozuch writes
\[
\lambda_k=c\langle R^+(H_2)\zeta^+,\zeta_{(k)}^+\rangle.
\]
His displayed forms have norm \(\sqrt2\). With \(\zeta^+=\omega_1\) and \(\zeta_{(k)}^+=\omega_k\),
\[
\langle R^+\omega_1,\omega_k\rangle=2(R^+\zeta)_k.
\]
Thus the magnitude of his unspecified constant is \(c=1/2\) under these conventions; a common basis sign changes the signs of the individual \(\lambda_k\).

### Scaling

Under \(x=ay\),
\[
a^{-2}\widetilde g
=EH_1+a^2\widehat h+O(a^4|y|^4).
\]
Ricci as a covariant two-tensor is unchanged by constant metric rescaling, while the \(L^2\) norm of covariant two-tensors is invariant in dimension four. Therefore
\[
Ric^\circ(a^{-2}\widetilde g)
=a^2DRic^\circ_{EH_1}[\widehat h]+O(a^4),
\]
and
\[
\langle Ric^\circ(\widetilde g),\widehat o\rangle
=a^2B+O(a^4).
\]
Since \(\|\widehat o\|^2=\pi^2+o(1)\),
\[
\frac{(a^2\pi^2|R^+\zeta|)^2}{\pi^2}
=\pi^2a^4|R^+\zeta|^2.
\]
The leading constant in the lower estimate is therefore correct.

---

## 3. Lower-bound error estimates

Several displayed estimates need modification.

### Norm of the test tensor

The note writes
\[
\|\widehat o\|_g^2=\pi^2(1+O(a^4+\delta a^2)).
\]
The background perturbation \(a^2h_2\sim a^2r^2\) contributes
\[
a^2\int_1^\infty r^2r^{-8}r^3\,dr=O(a^2).
\]
The correct estimate is
\[
\|\widehat o\|_g^2
=\pi^2+O(a^2)+O(\delta a^2)+O(a^4).
\]
This does not alter the theorem because \(a^2\le a^{2-w}\) for \(0\le w<2\) and \(0<a<1\).

### Cancellation of the growing \(a^4\) terms

A finite Taylor expansion alone does not give a uniform \(O(a^4)\) pairing up to \(r\sim a^{-1}\): an untreated remainder \(a^6r^4\) in Ricci would integrate to \(O(a^2)\).

The required argument is instead a comparison with the exact Einstein metric \(g_V\). In scaled variables, the background curvature has the form
\[
a^2\bigl(Rm_p+O(a^2r^2)\bigr),
\]
because odd orbifold jets vanish. All terms formed purely from the background metric cancel in \(Ric^\circ\). The discrepancy comes from interaction with the ALE tail \(q_{ALE}=O(r^{-4})\). Replacing \(Rm_p\) by its variation \(O(a^2r^2)\) gives
\[
a^4r^2\cdot r^{-4}\cdot |o|\,r^3
=O(a^4r^{-3}),
\]
which is integrable. This gives the desired \(O(a^4)\) remainder.

The text’s reference to
\[
P_eH_4=\Lambda H_2-Q(H_2,H_2)
\]
captures the first instance of this cancellation, but the proof needs the exact-Einstein comparison to control all higher jets uniformly.

### Linear perturbation term

The estimate
\[
DRic^*_{\widetilde g}\widehat o
=a^2O(r^{-4})+O(\Lambda^{-6})
\]
has the correct structure. The first term follows from
\[
\widetilde g-EH=a^2O(r^2)
\]
and the decay \(o=O(r^{-4})\). The cutoff commutator has size \(O(\Lambda^{-6})\).

For \(w>0\),
\[
\int_1^\Lambda
\delta a^2r^w\cdot a^2r^{-4}\cdot r^3\,dr
=O(\delta a^4\Lambda^w).
\]
For \(w=0\), this is
\[
O(\delta a^4\log\Lambda),
\]
not \(O(\delta a^4)\). It is still \(o(a^2)\) and is absorbed by the much coarser \(C\delta a^2\) used in the final pairing estimate.

Varying the metric in the inner product, volume form, and trace-free projection also creates algebraic terms. Since the background trace-free Ricci tensor is \(a^2O(r^{-4})\), these are \(O(\delta a^4)\) after integration and do not affect the coefficient.

### Quadratic term

The written estimate
\[
O(\delta^2a^4\Lambda^{2w-2})
\]
is not correct for \(w<1\). The actual radial integral is
\[
\delta^2a^4\int_1^\Lambda r^{2w-3}\,dr
=
\begin{cases}
O(\delta^2a^4),&0\le w<1,\\
O(\delta^2a^4\log\Lambda),&w=1,\\
O(\delta^2a^4\Lambda^{2w-2}),&1<w<2.
\end{cases}
\]
Every case is \(o(a^2)\) for \(w<2\), so the final lower estimate survives.

A uniform theorem should state \(0<\delta\le\delta_0\). For unrestricted \(\delta\), a choice of \(a_0\) independent of \(\delta\) does not provide uniform nonlinear constants.

### Cutoff placement

The cutoff annulus must lie where either:

1. \(\widetilde g=g_V\) exactly, so \(Ric^\circ(\widetilde g)=0\), or  
2. an explicit gluing-annulus estimate is included.

The sentence choosing \(\Lambda=t_0/(2a)\) while saying the cutoff lies where \(\widetilde g=g_V\) depends on an unstated convention for the gluing radii. Constants can be changed to arrange this, but the metric definition must record the relevant annuli.

### Gauge and diffeomorphisms

No correction of \(\widehat o\) to an exact adjoint-kernel tensor is necessary. The residual
\[
DRic^*_{\widetilde g}\widehat o
\]
is already small enough. If desired, one may replace \(\widehat o\) by its \(g\)-trace-free projection; pairing with \(Ric^\circ(g)\) is unchanged.

The “after a diffeomorphism” definition of \(\mathcal N_\delta\) is compatible with the argument: use the representative satisfying the weighted estimate and pull the test tensor through the same diffeomorphism. Since \(P(g)\) is diffeomorphism invariant, no additional term appears.

With the preceding repairs, part (a) has the form
\[
P(g)\ge
\pi^2a^4
\left(
|R_p^+\zeta|-C(\delta+a^{2-w})
\right)_+^2
\]
for \(0<\delta\le\delta_0\).

---

## 4. Upper construction and the neighborhood mismatch

### Bianchi term in Ozuch’s equation

Ozuch solves
\[
P_{EH}\underline h_2
=\Lambda EH+\sum_i\lambda_i o_i,
\qquad
P_{EH}=DRic_{EH}+\delta^*B_{EH}.
\]
Applying \(B_{EH}\) gives a harmonic one-form equation for \(B_{EH}\underline h_2\), since
\[
B_{EH}(\Lambda EH)=0,\qquad B_{EH}o_i=0.
\]
The asymptotics \(B_{EH}\underline h_2=O(r^{-3+\varepsilon})\), together with Ricci-flatness and the absence of a decaying parallel one-form on EH, imply
\[
B_{EH}\underline h_2=0.
\]
Therefore
\[
DRic_{EH}\underline h_2
=\Lambda EH+\sum_i\lambda_i o_i.
\]
The use of the gauged operator does not add a first-order trace-free term.

With the flux normalization,
\[
\lambda_i=(R_p^+\zeta)_i
\]
in the basis used in the step-60 computation.

### Remainder estimate

To obtain
\[
Ric^\circ(g^*)
=a^2\sum_i\lambda_i o_i+R_4,
\qquad
|R_4|\lesssim a^4(1+r)^{-2},
\]
one needs three ingredients together:

- Lemma 2.3:
  \[
  \underline h_2=H_2+H_2^4+O(r^{-4+\varepsilon}),
  \qquad H_2^4=O(r^{-2});
  \]
- the quartic Einstein jet equation for \(H_4\);
- an explicit matching estimate on the gluing annulus.

Lemma 2.3 alone does not state the full nonlinear \(R_4\) estimate. The estimate is plausible because the pure growing terms cancel by the Einstein jet equation, leaving interactions such as
\[
Q(H_2,H_2^4)=O(r^{-2}).
\]
The note currently gives a sketch rather than a complete weighted estimate.

Once that estimate is available,
\[
\begin{aligned}
P(g^*)
&=a^4|\lambda|^2\|o\|^2
+O(a^6)+O(a^8\log(1/a))\\
&=\pi^2a^4|R_p^+\zeta|^2+O(a^6).
\end{aligned}
\]
The stated \(O(a^6\log(1/a))\) is a weaker valid form. If \(R_p^+\zeta=0\), the cross term disappears and the same construction gives the stronger
\[
P(g^*)=O(a^8\log(1/a)).
\]

### Main incompatibility with \(\mathcal N_{Ca^{2-w}}\)

Let \(\widehat h\) be the smooth extension used in the naïve metric. In \(y\)-coordinates,
\[
a^{-2}\widetilde g
=EH+a^2\widehat h+\cdots,
\]
whereas the adapted first-order metric is
\[
a^{-2}g^*
=EH+a^2\underline h_2+\cdots.
\]
Therefore
\[
k:=a^{-2}(g^*-\widetilde g)
=a^2(\underline h_2-\widehat h)+\cdots.
\]
On the EH core \(r=O(1)\), the difference
\(\underline h_2-\widehat h\) is generically \(O(1)\), so
\[
|k|=O(a^2).
\]
Membership in \(\mathcal N_{Ca^{2-w}}\) would require there
\[
|k|\le Ca^{2-w}a^2=Ca^{4-w},
\]
which is much smaller than \(a^2\) for every \(w<2\).

Thus, for a generic naïve center,
\[
g^*\in\mathcal N_C,
\]
but not
\[
g^*\in\mathcal N_{Ca^{2-w}}.
\]

There are two mathematically consistent formulations:

1. **Adapted center.** Define \(g^A_{a,\zeta}\) using \(\underline h_2\) from the outset. Shrinking neighborhoods centered at \(g^A\) then contain the upper metric, and the coefficient \(\pi^2\) is matched.

2. **Original naïve center.** Retain \(\widetilde g\), but only assert membership in \(\mathcal N_{C_0}\), where \(C_0\) depends on \(\underline h_2-\widehat h\). For very small \(\delta\), the infimum can retain additional \(L^2\) energy from the component of \(DRic^\circ[\widehat h]\) orthogonal to the EH cokernel.

The present statement of part (b), and hence the displayed equality for
\(\inf_{\mathcal N_\delta}P\), requires this correction.

### Uniformity in \(\zeta\)

A multiplicative formula
\[
\inf P
=\pi^2a^4|R^+\zeta|^2(1+O(\delta)+o(1))
\]
cannot be uniform as \(R^+\zeta\to0\). The uniform form is additive:
\[
\pi^2a^4\bigl(|R^+\zeta|-C\varepsilon\bigr)_+^2
\le \inf P
\le
\pi^2a^4|R^+\zeta|^2+O(a^6),
\quad
\varepsilon=\delta+a^{2-w},
\]
provided the adapted center is used. A multiplicative expression is valid when
\(|R^+\zeta|\ge r_0>0\).

Likewise, the near-extremal estimate in part (c) should contain an additive term:
\[
\|Ric^\circ-\Pi Ric^\circ\|_{L^2}^2
\lesssim
a^4\left[
\eta |R^+\zeta|^2+
\varepsilon\bigl(|R^+\zeta|+\varepsilon\bigr)
\right].
\]
The displayed version proportional only to
\(\varepsilon |R^+\zeta|^2\) is uniform only away from \(\ker R^+\).

---

## 5. Consequences

### Round \(S^4\)

For the unit round metric,
\[
W^\pm=0,\qquad s=12,\qquad
R^\pm=W^\pm+\frac{s}{12}I=I.
\]
Hence one EH insertion contributes
\[
\pi^2a^4+o(a^4),
\]
and two equal-scale insertions contribute
\[
2\pi^2a^4+o(a^4).
\]
The statement that no Einstein metric lies in the corresponding neighborhood requires
\(\delta<C^{-1}\) and \(a\) sufficiently small. The local coefficient itself is correct.

### Kähler–Einstein orbifolds

With the complex orientation, a Kähler surface has
\[
W^+=\operatorname{diag}\left(\frac s6,-\frac s{12},-\frac s{12}\right)
\]
in the basis consisting of the normalized Kähler form and its orthogonal complement. Since \(s=4\Lambda\),
\[
R^+=W^++\frac{s}{12}I
=\operatorname{diag}(\Lambda,0,0).
\]

The crepant, holomorphic EH resolution aligns the EH Kähler form with the orbifold Kähler form, so its direction is
\[
\zeta=\widehat\omega,
\]
not a vector orthogonal to \(\widehat\omega\). It therefore has leading cost
\[
\pi^2\Lambda^2a^4.
\]

For \(\zeta\perp\widehat\omega\),
\[
R^+\zeta=0.
\]
The first-order contribution vanishes, and the adapted construction gives
\[
P=O(a^8\log(1/a)),
\]
which in particular is \(O(a^6)\).

Given such a kernel direction, one may choose a basis
\[
(\zeta,\zeta',\widehat\omega)
\]
in which
\[
R^+=\operatorname{diag}(0,0,\Lambda).
\]
This is exactly the algebraic form appearing in Ozuch’s Theorem 0.2. The source theorem requires its stated global hypotheses; the pointwise matrix identity alone does not identify the entire orbifold as Kähler–Einstein. The phrase “KE orbifolds are exactly the orbifolds unobstructed through second order” should therefore be replaced by:

> Kähler–Einstein curvature has the local algebraic form required for vanishing of the second EH coefficient in every non-holomorphic kernel direction.

### Burns/EH arithmetic

On the nonpositive kernel stratum
\[
\mu_1=0,\qquad
\mu_2,\mu_3\le0,\qquad
\mu_2+\mu_3=\Lambda,
\]
\[
(\mu_2-\mu_3)^2=\Lambda^2-4\mu_2\mu_3.
\]
For fixed \(\Lambda\), this is maximal when
\[
\mu_2\mu_3=0
\]
and vanishes when
\[
\mu_2=\mu_3=\Lambda/2.
\]
Thus the Burns logarithmic correction
\[
-2\pi^2(\mu_2-\mu_3)^2\epsilon^2\log(1/\epsilon)
\]
has the stated extremizers.

Ozuch’s Example 2.1 has
\[
R^+=\operatorname{diag}(0,-3/2,-3/2),
\]
so the Burns splitting term vanishes while the EH second coefficient is proportional to
\[
\mu_2\mu_3=\frac94.
\]
The complementary interpretation is arithmetically correct.

The vanishing form of the second EH coefficient is already supplied by Biquard–Ozuch:
under \(R^+\zeta=0\),
\[
\mu^{(2)}_1
=C\det\!\left(R^+|_{\zeta^\perp}\right).
\]
For a diagonal complementary block this is \(C\mu_2\mu_3\). What remains unresolved is the exact constant in the corresponding squared-defect asymptotic and a second-order matching theorem of the form
\[
\inf P\sim c\,a^8(\mu_2\mu_3)^2.
\]
Accordingly, Conjecture 61.D should concern that quantitative constant and minimization statement, not the determinant zero set itself.

### General ALE extension

The projection principle extends to hyperkähler ALE spaces, but “verbatim” is too strong. For \(A_{n-1}\) spaces one must track:

- the full collection of \(L^2\) harmonic ASD forms;
- the period-map normalization;
- the finite-group quotient in each flux;
- possible interactions among several kernel modes;
- the weighted linear theory for the relevant ALE end.

The invariant leading object remains the squared \(L^2\) norm of the projection of the background quadratic jet onto the ALE cokernel.

---

## Corrected core statement

A scientifically supported version is:

- For a fixed naïve desingularization and \(0<\delta\le\delta_0\),
  \[
  P(g)\ge
  \pi^2a^4
  \left(
  |R_p^+\zeta|-C(\delta+a^{2-w})
  \right)_+^2.
  \]

- There is an **adapted Einstein-modulo-obstruction metric** \(g^A_{a,\zeta}\), centered on Ozuch’s \(\underline h_2\), such that
  \[
  P(g^A_{a,\zeta})
  =
  \pi^2a^4|R_p^+\zeta|^2+O(a^6),
  \]
  and, when \(R_p^+\zeta=0\),
  \[
  P(g^A_{a,\zeta})=O(a^8\log(1/a)).
  \]

- The matching infimum statement holds for neighborhoods centered at \(g^A_{a,\zeta}\). For a generic naïve center, the adapted metric is only \(O(a^2)\)-close in scaled core variables and is not contained in \(\mathcal N_{Ca^{2-w}}\).