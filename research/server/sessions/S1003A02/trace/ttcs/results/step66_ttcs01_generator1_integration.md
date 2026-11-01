# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 66,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step66_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step66_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Context: the unrestricted Einstein-defect problem α(M)=inf∫|Ric°|² on M=X#kCP̄² (X minimal general type, A=c₁²(X), open range 0<k<A/3 where LeBrun's SW bound is vacuous). Step 65 proved a metric-only exceptional flux ledger p=(1−δ)²/‖h‖²+L (δ = exceptional Ricci-flux deficit, L ≥ 0 misalignment). Step 66 showed (on the constant-scalar slice, which is WLOG) that L splits as L_rank+L_amp; L_rank=0 is exactly the Riemannian Einstein–Maxwell system with F⁻ ∝ the exceptional harmonic ASD form ĥ_a; L=0 is the subclass with |F⁺| constant = AK metrics with J-invariant Ricci (Blair–Ianus class), joining cscK (δ=0, p=|a⁻|²≥k) to Einstein (δ=1, p=0). The near-equality Bianchi estimate gives no coercivity. Generate the strongest scientifically serious ideas for what new information could decide the open range, now that the problem is organized by Einstein–Maxwell theory: (i) Seiberg–Witten curvature estimates adapted to Einstein–Maxwell metrics or to metrics near the EM layer (what inequality, which class, which weight), and whether they would give a k-threshold or a k²/A law; (ii) whether the Blair–Ianus variational characterization (critical points of ∫s on ω-compatible metrics) plus Taubes' symplectic SW theory constrains the strictly-AK members with [ρ₀]∥a⁻ and δ near 1 (e.g. via c₁·[ω], Hermitian scalar curvature integrals, the exceptional (−1)-spheres being symplectic); (iii) a construction route: conformally Kähler or other EM metrics on general-type blow-ups with small L_amp and δ bounded away from 0, or an argument they cannot exist; (iv) a quantitative formulation that is genuinely weaker than Einstein nonexistence but still gives a tariff for metrics near the Kähler end (δ ≤ δ₀). For each idea give the exact inequality or construction, why it might work, the decisive first computation, and what would falsify it. Do not invent literature; name precise knowledge requests where needed.

## Integrated Scientific Memo

# Einstein–Maxwell information that could decide the open range

Put
\[
P=\int_M|\operatorname{Ric}^{\circ}|^2,\qquad p=\frac{P}{8\pi^2},
\qquad Q=|a^-|^2\ge k,
\]
where \(a\) is a best-sign monopole class. Normalize the exceptional harmonic direction by \(\|\hat h\|_2=1\), and define
\[
\Phi=2\pi\sqrt Q,\qquad
\mathcal F=\sqrt2\int|B^*\hat h|,\qquad
\delta=1-\frac{\mathcal F}{\Phi}.
\]
Then the normalization-independent ledger is
\[
\boxed{p=Q(1-\delta)^2+L_{\rm rank}+L_{\rm amp}.}\tag{1}
\]

The scientific opportunity is to intersect the Maxwell equality structure with *additional differential or symplectic information*. Another algebraic estimate on the existing curvature components will not suffice.

Two qualifications matter throughout:

* The global identification \(L_{\rm rank}=0\Rightarrow\) Einstein–Maxwell still requires extension of the aligned SD form through \(Z(h)\); Step 66 proves this under local boundedness. Arbitrary near-rank-one metrics do not automatically supply a global harmonic \(F^+\).
* The signed AK twist deficit \(\delta_b=D/\Phi_b\) coincides with the metric deficit \(\delta\) only when the Chern class, exceptional direction, and Ricci orientation match. Below, formulas involving \(Q\) and \(\delta_b\) assume \(b=a\), \(\hat h\parallel b^-\), and \(0\le\delta_b\le1\). Otherwise replace \(Q\) by \(\langle b,\hat h\rangle^2\), without automatically asserting it is at least \(k\).

## 1. Seiberg–Witten estimates: the useful weight, the unavailable remainder, and the correct target

### 1.1 Use the harmonic self-dual Maxwell field—not a normalized SW spinor

On a genuine EM solution, the natural SW test form is
\[
\psi=F^+.
\]
It is globally harmonic and avoids the normalized-spinor singularities established in Step 64. If \(\psi\) is nowhere zero, then
\[
q=\frac{|\psi|_g}{\sqrt2},\qquad
\widehat g=qg,\qquad \omega=\psi
\]
defines an almost-Kähler metric. The first class to test is \(b=c_1(J_\omega)\); the blow-up sign family should then be retained separately.

The precise literature request is the harmonic-form version of LeBrun’s weighted monopole estimate, including hypotheses, signs, and equality:
\[
\int_M\left(\frac23s+2\lambda_{\min}(W^+)\right)|\psi|\,d\mu
\ \le\ 4\pi\sqrt2\,a\cdot[\psi].\tag{2}
\]
This is a candidate imported theorem, not proved by the supplied sources. Its Kähler calibration is correct.

A particularly decisive computation can already be made. On the AK slice, with
\[
u=\frac{|\nabla\omega|^2}{4},\qquad
r=\frac{\langle W^+\omega,\omega\rangle}{2}=\frac{s}{6}+u,
\]
the Hermitian scalar-curvature identity is
\[
4\pi b\cdot[\omega]=\int(s+2u).
\]
Thus the slack in (2), for \(\psi=\omega\), is exactly
\[
\boxed{
\mathcal E_b(\omega)
=2\sqrt2\int_M\bigl(r-\lambda_{\min}(W^+)\bigr).
}\tag{3}
\]

**Consequences.** This weighted estimate measures failure of \(\omega\) to be a lowest Weyl eigenform; it does **not** directly price torsion. In particular, the proposed remainder
\[
\mathcal E_b(\omega)\ge c\int|\nabla\omega|^2
\]
cannot be asserted: its left side vanishes whenever \(\omega\) is a lowest eigenform, without algebraically forcing \(u=0\). Any strengthened SW proof must identify which retained squares control eigenvector or eigenvalue defects and which permit strict AK equality. A positive full-gradient remainder would be an additional integrability theorem, not routine bookkeeping in the SW proof.

The sign-family identity
\[
2^{-k}\sum_\varepsilon
(a_\varepsilon\cdot[\omega])^2
=(K_X\cdot[\omega])^2+\sum_i(E_i\cdot[\omega])^2\tag{4}
\]
is useful for retaining exceptional areas. But independent SW solutions for different signs do not automatically produce a common additive remainder. Equation (4) is intersection algebra, not yet an exceptional-class tariff.

### 1.2 The strongest credible mechanism: intersect the two equality systems

LeBrun’s scalar/Weyl equality structure supplies special \(J\)-invariant \(W^+\), while constant-amplitude EM supplies \(J\)-invariant Ricci. Their intersection is the setting in which the compact AAD Gray-condition rigidity from the supplied sources may force Kählerness.

The useful new object is therefore a **joint rigidity defect**, not torsion alone:
\[
\mathcal S_{\rm L}(g)
=\upsilon-\upsilon_{\rm L}(\kappa),
\]
together with \(L_{\rm rank}\) and \(L_{\rm amp}\). A targeted quantitative theorem would be
\[
\boxed{
\kappa\le k+\beta p+C\mathcal E_{\rm EM},
}\tag{5}
\]
or, more ambitiously,
\[
\boxed{
\kappa\le(1-\eta)k+\beta p+C\mathcal E_{\rm EM}.
}\tag{6}
\]
Here \(\mathcal E_{\rm EM}\) must be a specified, controlled distance to *global* Maxwell structure, not merely formal weighted closedness.

On exact EM metrics, (5) gives the \(k^2/A\) scale:
\[
p\ge \frac{k^2}{4(1+\beta)A}\bigl(1+O(k/A)\bigr).
\]
Equation (6) instead yields a per-class tariff, at least
\[
p\ge\frac{\eta k}{1+\beta},
\]
in the relevant Weyl-envelope range.

**Decisive first computation.** Write the compact AAD Gray-rigidity integral identity on the EM layer, preserving its *tested contractions*. Identify whether its error is controlled by the LeBrun slack and Maxwell amplitude variance, rather than by the full \(W_3^+\) and \(\rho_*''\) norms. Step 64 shows why full-norm estimates fail: those components can be large enough to finance negative-scalar torsion.

**Falsification.** A compact EM sequence with
\[
\frac{(\kappa-k)_+}{p}\longrightarrow\infty
\]
falsifies every finite-\(\beta\) exact-EM version of (5). An Einstein metric itself falsifies it in the open range: the known envelope requires \(\kappa>k\) when \(p=0\). Thus (5) includes Einstein nonexistence; it is not an easier theorem merely because it is phrased on the EM layer.

### 1.3 Precision required near EM

An exact-EM theorem alone does not prove an unrestricted gap. A useful distance is
\[
\mathcal E_{\rm EM}(g,h)
=\frac1{8\pi^2}
\inf_{\psi\in\mathcal H_g^+}
\|\operatorname{Ric}^{\circ}-\psi\circ h\|_2^2,\tag{7}
\]
with \(h\) fixed by its cohomological normalization. The missing analytic implication is a bound of (7) by \(L_{\rm rank}\), despite zeros of \(h\), degeneration of the metric, and possible unboundedness of the extracted aligned field.

Moreover, an error \(C\sqrt{A L_{\rm rank}}\) is generally too large for the sharp \(k^2/A\) conclusion. The permitted Weyl overshoot near a cheap state is only \(O(k^2/A)\). Since \(L_{\rm rank}\le p\), a square-root error can, at best by this argument, leave a much smaller scale of order \(k^4/A^3\).

Finally, Step 62’s assertion that \(p/k\to0\) itself forces \(\kappa/k\to1\) needs correction. The proved identities give
\[
\upsilon=4\kappa-3k+3p,
\]
and hence a lower constraint on \(\kappa\), not the missing upper constraint. They do not force near-equality in LeBrun or \(\Pi=o(k)\) without additional control. A formal mode saturating the envelope is a diagnostic, not a necessary limit of all cheap metrics.

**Knowledge requests:** the exact weighted theorem (2); retained squares in LeBrun’s scalar/Weyl proof; the compact AAD Gray-rigidity identity and its quantitative errors; Maxwell-source terms in the \(W^+\) differential identities.

## 2. Blair–Ianuş and Taubes: what actually constrains the dangerous AK class

### 2.1 Correct the Chern-form object

For a strictly AK metric, the closed Riemannian Ricci form is **not generally the Chern representative**. The supplied frame identity is
\[
\gamma_J=R(\omega)+t_J,\qquad [\gamma_J]=2\pi c_1(J).
\]
In particular,
\[
2\pi b^-=\rho_0+\mathsf H^-(t^-),\tag{8}
\]
not \(2\pi b^-=\rho_0\).

Also \(\omega\) is self-dual harmonic, so
\[
\mathsf H^-(\omega)=0.
\]
A feasibility problem assigning exceptional ASD flux to \([\omega]^-\) is therefore invalid. The flux is carried by **quadratic torsion**, while \([\omega]\) enters through areas and the Hermitian scalar integral.

### 2.2 A rigorous torsion–volume bound, and why ordinary canonical positivity stops short

On the aligned AK class at \(s=-4\), set
\[
I=\int u,\quad S=\int u^2,\quad
\mathcal Q=2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2.
\]
Step 66 gives
\[
4I=4\Phi^2\delta(1-\delta)+6S+\mathcal Q,\qquad
S\ge2\Phi^2\delta^2.
\]
Therefore
\[
\boxed{I\ge\Phi^2(\delta+2\delta^2).}\tag{9}
\]
For \(K_\omega=-b\),
\[
4\pi K_\omega\cdot[\omega]=4V-2I.\tag{10}
\]
Assuming the relevant Taubes canonical positivity \(K_\omega\cdot[\omega]>0\), equations (9)–(10) imply
\[
\boxed{
V>2\pi^2Q(\delta+2\delta^2).
}\tag{11}
\]
At \(\delta=1\), this says \(V>6\pi^2Q\). Only with the *additional* near-extremal volume condition \(V\simeq2\pi^2A\) does it recover \(Q<A/3\).

This calculation explains precisely why canonical positivity alone does not close the open range: the Yamabe volume can grow. No supplied theorem gives the needed upper bound.

A sharper consequence combines (9) with \(I^2\le VS\):
\[
I=\Phi^2\delta(1-\delta)+\frac32S+\frac14\mathcal Q
\ge\Phi^2\delta(1-\delta)+\frac{3I^2}{2V}.
\]
Thus
\[
\Phi^2\delta(1-\delta)\le \frac V6,
\]
and, more usefully, the admissible \(I\) must satisfy this quadratic constraint *together with* (9). This gives a concrete feasibility test for proposed AK profiles, but still does not exclude \(\delta\to1\).

### 2.3 The genuinely new symplectic inequality to investigate

After a symplectic blow-down, write
\[
K_\omega=K_0+\sum E_i,\qquad
K_\omega\cdot[\omega]=K_0\cdot[\omega_0]+\sum e_i,\qquad
[\omega_0]^2=2V+\sum e_i^2.
\]
A strong target is
\[
\boxed{
K_0\cdot[\omega_0]\ge\sqrt{A[\omega_0]^2}.
}\tag{12}
\]
This is Kähler Hodge-index behavior; it is **not** automatic for symplectic forms when \(b^+>1\). A proof would need the EM/AK differential structure or an additional theorem about the symplectic canonical class.

If (12) holds, dropping positive exceptional-area terms yields
\[
Q(\delta+2\delta^2)
\le A+\upsilon-\sqrt{A(A+\upsilon)}.\tag{13}
\]
For small \(\upsilon/A\), its right side is \(\upsilon/2+O(\upsilon^2/A)\). Combining (13) with an EM susceptibility upper bound \(\upsilon\le k+Cp\) would impose a substantial tariff near \(\delta=1\).

**Decisive first computation.** Determine whether the cohomology classes compatible with the *actual EM Chern decomposition* can violate (12). A generic positive-cone quadratic program is insufficient: no complete symplectic-cone description for these general-type blow-ups is supplied.

**Falsification.** A symplectic blow-down class satisfying the relevant topology and
\[
K_0\cdot[\omega_0]<\sqrt{A[\omega_0]^2}
\]
disproves an unrestricted version of (12), but not an EM-restricted version. The latter requires realizing the class by an aligned AK metric.

### 2.4 Exceptional spheres provide a localized torsion-flux test

If an exceptional class has a \(J\)-holomorphic sphere representative \(E_i\) for the **given** AK structure, then
\[
2\pi
=\int_{E_i}\gamma_J
=-e_i+\int_{E_i}\rho_0+\int_{E_i}t_J,\qquad e_i>0.\tag{14}
\]
Near \(\delta=1\), torsion must supply the Chern flux despite the negative scalar contribution.

The first meaningful computation is the exact restriction of \(t_J\) to \(TE_i\), followed by a tubular estimate linking its surface integral to the *Ricci-priced* contraction in the AAD identity. A bound by \(\int_{E_i}u\) alone is not enough: neither a surface trace nor a tube radius is controlled by the unrestricted hypotheses.

**Falsification:** fixed exceptional torsion flux carried in increasingly thin tubes with vanishing relevant Ricci-priced energy. The Step-64 SW Hopf logarithm does not automatically rule this out; it concerns a singular normalized-spinor field, not every smooth AK Nijenhuis core.

**Knowledge request:** the precise Taubes/Gromov theorem ensuring an embedded exceptional \(J\)-sphere for this fixed compatible \(J\), including nongeneric structures and possible cusp representatives.

### 2.5 Blair–Ianuş stationarity is not stability

For fixed \(\omega\),
\[
\int s=4\pi b\cdot[\omega]-2\int u.
\]
Thus \(J\)-invariant Ricci characterizes critical points of the torsion energy \(I(J)\). It does not say they minimize it. A negative Hessian direction cannot exclude a Blair–Ianuş saddle; nor does positivity of a Hessian prevent a family of critical points from approaching \(\delta=1\).

The useful calculation is the linearized stationarity operator and its kernel near a cscK blow-up. A kernel permitting a nonintegrable branch with increasing harmonic twist would supply an infinitesimal construction mechanism. A kernel consisting only of Kähler moduli and gauge directions could support local rigidity. Connecting its stability to minimization of \(P\) requires a separate argument.

## 3. Construction: eliminate the easy Hermitian route, then test genuinely non-Hermitian EM geometry

### 3.1 Conformally Kähler EM has a direct obstruction

Suppose
\[
g=f^{-2}g_K,\qquad F^+=\omega_K,\qquad F^-=h,
\]
with \(g_K\) Kähler. Harmonicity and the SD/ASD splitting of two-forms are conformally invariant in dimension four; \(h\) does **not** vary with \(f\) when its class and \(g_K\) are fixed.

The EM stress tensor is \(J\)-invariant. The conformal Ricci formula gives
\[
\operatorname{Ric}_g^\circ
=\operatorname{Ric}_{g_K}^\circ
+2f^{-1}(\nabla_K^2f)_0.
\]
Consequently
\[
(\nabla_K^2 f)''=0.\tag{15}
\]
On a Kähler manifold, (15) means \(J\nabla_K f\) is a holomorphic Killing field. Therefore:

\[
\boxed{
H^0(M,T^{1,0}M)=0
\quad\Longrightarrow\quad f\ \text{is constant}.
}\tag{16}
\]

For the usual complex general-type blow-up, this excludes nonconstant conformally Kähler EM metrics. The remaining constant-factor solutions have constant scalar Kähler geometry and cannot produce a positive twist deficit.

The needed knowledge request is narrow: verify absence of holomorphic vector fields for every complex structure being admitted on the underlying smooth manifold—not merely the original blow-up structure. There is no need first to solve a conformal elliptic continuation problem on a complex structure with no such fields.

### 3.2 General EM becomes a conformally AK system—but not a symmetry theorem

For nowhere-zero \(F^+\), put
\[
q=|F^+|_g/\sqrt2,\quad \widehat g=qg,\quad
\omega=F^+,\quad \ell=\log q,\quad h=F^-.
\]
In the Step-66 EM normalization,
\[
\operatorname{Ric}_{\widehat g}^{\circ}
+\left(\widehat\nabla^2\ell+\tfrac12d\ell\otimes d\ell\right)_0
=q\,\omega\circ_{\widehat g}h,\tag{17}
\]
\[
s_g=q\left(s_{\widehat g}+3\widehat\Delta\ell
-\tfrac32|d\ell|_{\widehat g}^2\right)=\text{constant}.\tag{18}
\]
The amplitude loss is proportional to
\[
\int(q-\bar q_h)^2|h|_{\widehat g}^2\,d\mu_{\widehat g}.\tag{19}
\]

These equations give an exact construction system. Their anti-Hermitian part is
\[
\operatorname{Ric}_{\widehat g}''
+\left(\widehat\nabla^2\ell+\tfrac12d\ell\otimes d\ell\right)''=0.\tag{20}
\]
Unlike the Kähler case, (20) does not directly make \(J\widehat\nabla q\) Killing: derivatives of \(J\) intervene.

A serious proposed obstruction is a weighted identity pricing \(\mathcal L_{J\nabla q}\widehat g\) by terms that vanish under EM. If it forced a Hamiltonian circle action, the relevant symplectic action classification could obstruct general-type topology. The decisive first computation is the exact torsion remainder in that identity. A sign-indefinite surviving term defeats this shortcut; a nonconstant compact EM example with no corresponding symmetry would falsify it outright.

### 3.3 Charged bolt–host matching is the most concrete new construction test

Step 64 supplies a zero-defect \(O(-1)\) Einstein interior whose first boundary jets do not match the CH host. Maxwell parameters might remove that mismatch.

A nonredundant local ansatz is
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+c(t)^2\sigma_3^2,
\]
\[
F^\pm=f_\pm(t)(e^{03}\pm e^{12}),
\]
with \(d\sigma_3=2\sigma_1\wedge\sigma_2\). Maxwell closure is exactly
\[
\boxed{(a^2f_\pm)'=\pm2cf_\pm.}\tag{21}
\]
The Ricci equation depends on the product \(f_+f_-\). Bolt regularity and the exceptional period fix part of the data; they must be imposed before counting independent charge parameters.

**Decisive first computation:** solve the scalar-\(-4\) EM ODE and expand its boundary metric, second fundamental form, and Maxwell data in the shrinking-bolt regime. Pair the resulting mismatch with the actual connector cokernel from the Einstein test. Determine whether the new Maxwell parameter changes its leading coefficient through zero.

Important restrictions:

* An exact CH exterior has \(\operatorname{Ric}^\circ=0\). With nonzero \(F^+\), it cannot support a nonzero \(F^-\); harmonic unique continuation forbids simply turning off the exceptional field on an open exterior. The host must also be perturbed.
* \(F^+\mapsto\lambda F^+\), \(F^-\mapsto\lambda^{-1}F^-\) preserves the stress tensor. Apparent charge freedom disappears once the exceptional normalization is fixed.
* Vanishing finite-dimensional mismatch is only an entrance to gluing. A shrinking connector needs an actual \(P\)-estimate; shrinking volume alone does not make four-dimensional curvature-squared cost vanish.

A sign-definite mismatch for every regular charged bolt, or a zero possible only at the cscK calibration, would falsify this ansatz as a sub-tariff construction. Successful matching would be genuinely new evidence, unlike another pointwise diffuse balance.

## 4. A Kähler-end tariff genuinely weaker than Einstein nonexistence

### 4.1 A proved restricted tariff already exists

For any fixed \(\delta_0<1\), equation (1) immediately gives
\[
\boxed{
\delta\le\delta_0
\quad\Longrightarrow\quad
P\ge8\pi^2k(1-\delta_0)^2.
}\tag{22}
\]
This makes no claim about Einstein metrics. The substantive improvement is to recognize \(\delta\le\delta_0\) from independently measurable geometry.

On the aligned AK class, (9) does exactly that. If
\[
I\le\varepsilon\Phi^2,
\]
then
\[
\delta+2\delta^2\le\varepsilon,\qquad
\boxed{
\delta\le\frac{\sqrt{1+8\varepsilon}-1}{4}.
}\tag{23}
\]
Inserting (23) into (1) gives an explicit torsion-controlled tariff. This stronger estimate avoids the ambiguity of bounding only \(\delta(1-\delta)\), which cannot distinguish the Kähler and Einstein ends.

### 4.2 The local spectral target is linear in deficit unless the quadratic calculation says otherwise

There is an important correction to the proposed cscK Hessian tests. Along a smooth metric family through a Kähler equality metric, choose a smooth compatible \(J_t\) with fixed Chern class. Since \(\nabla\omega_0=0\),
\[
t_{J_t}=O(t^2).
\]
The maximizing Ricci-flux direction also agrees with \(\omega_0\) at \(t=0\). From the frame identity,
\[
\Phi_t\delta_t
=\langle t_{J_t}^-,\hat h_t\rangle
-\left(\mathcal F_t-\int\langle\omega_t,B_t^*\hat h_t\rangle\right).\tag{24}
\]
Both terms are second order, so
\[
\delta_t=O(t^2),\qquad L_t=O(t^2).
\]
Thus the constraint \(\dot\delta=1\) proposed for a Hessian quotient is generally unavailable. Conversely, a local \(L\ge cQ\delta\) is **not** ruled out by smooth variation: deficit itself starts quadratically.

Write
\[
\delta_t=t^2d_2(v)+o(t^2),\qquad
L_t=t^2\ell_2(v)+o(t^2).
\]
The correct generalized spectral problem is
\[
\boxed{
c_K=\inf_{d_2(v)>0}\frac{\ell_2(v)}{Qd_2(v)}.
}\tag{25}
\]
Metric dependence of the harmonic representative, gauge directions, zeros of \(h\), and flux differentiability must all be included.

If \(c_K>0\), with a quantitative remainder controlled on a slice transverse to moduli, one obtains locally
\[
L\ge cQ\delta,
\]
and hence, for \(0\le\delta\le\delta_0\),
\[
p\ge Q\min_{0\le d\le\delta_0}\bigl[(1-d)^2+cd\bigr].\tag{26}
\]
A direction with \(d_2>0\), \(\ell_2=0\) falsifies linear local coercivity and identifies a candidate aligned non-Kähler branch. A weaker \(L\ge cQ\delta^2\) might survive, but requires higher-order analysis.

No uniform constant follows from the numerical Burns-cell ratios. Those are degenerating cell families, not the Hessian of a fixed compact cscK metric. Uniformity as exceptional areas shrink is a separate neck-spectral problem. Nor may individual exceptional ledgers simply be summed: they repeatedly bound the same \(P\). Use the aggregate best-sign class, or prove an orthogonal multi-channel estimate.

## Scientific conclusion

The strongest new analytic object is a **quantitative intersection of LeBrun equality and Maxwell alignment**, with errors controlled sharply enough to yield \(\kappa\le k+\beta p\). The weighted Maxwell SW estimate alone prices Weyl-direction error, not torsion. Taubes positivity plus Blair–Ianuş stationarity supplies the exact bound (9), but cannot prevent volume growth or exclude saddles. Nonconstant conformally Kähler EM geometry is obstructed when the complex structure has no holomorphic vector fields; genuinely non-Hermitian EM or charged-bolt matching remains a meaningful construction test.

Three concrete calculations distinguish these possibilities:

1. the tested AAD rigidity remainder on the EM layer;
2. the charged-bolt boundary mismatch and connector cokernel;
3. the cscK quadratic quotient (25).

Meanwhile, (22)–(23) already provide rigorous restricted tariffs without asserting Einstein nonexistence. The unresolved global object is the price of **large exceptional harmonic twist with small Ricci flux**, including Maxwell-field zeros, amplitude variation, and degeneration—not another unweighted torsion-energy estimate.