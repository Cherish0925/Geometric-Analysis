# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Reviewer",
  "task_field": "reviewer",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step46_lemmaM_elementary_and_AC.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Sessions/S1003A01/workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md",
    "Knowledge/materials/openai-math-20261007/continuation/20261007_openai_math_connections/connections.md"
  ]
}
```

## Task

Read the consolidated O11/two-scale note as a critical geometric analyst. Check the exact algebra of the formal common-mode evaluation against Theorem K, the dependency ordering and quantifiers of the closed identity/Kähler tariff/full-sign field theorems/A_C/K/A01 rotated cells, and whether the governing k^2/A conjecture is scientifically supported without being presented as proved. Integrate the newly supplied source map: explain whether the De Giorgi same-test identity, Coulomb infimum-preserving bridge, exact-two-form inverse, or curvature-action decomposition materially changes the proposed next route. Return concrete mathematical repairs and identify the single highest-value next proof object; do not offer publication advice.

## Output

# Reading memo: Step 47, the O11 two-scale program

## 1. The scientific spine as it now reads

Step 47 makes the closed pure-blow-up line usable in proof order. The structure that is visible to a reader is this:

- **Topological requirement.** The same-metric closed identity forces any blow-up of \(X\) with \(A=K_X^2\) and \(0<k<A/3\) to lower \(C_+\) by \(k\).
- **Field-side information.** Theorems N, W and K say where that saving can sit: in shallow depletion, in \(W_2\) rotation, and in an \(L^1\) departure of \(W^+\) from the Kähler orbit.
- **Perturbative input.** \(A_C\) is the only perturbative coercivity theorem.
- **Upper objects.** The certified cells and A01's rotated cells are the upper objects that any lower theorem must accommodate.
- **Governing conjecture.** The \(k^2/A\) law is offered as the governing conjecture.

The note labels the conjecture as conjectural and keeps \(A_C\), K and the rotated cells inside their stated hypotheses. That discipline should be preserved.

The spine has one serious gap. Step 47 accounts for the self-dual half of the Chern–Weil budget and never prices the anti-self-dual half. Once that half is written down, the support for the \(k^2/A\) law depends on the host. The next route then changes.

## 2. The formal common mode against Theorem K: the algebra is correct

I recomputed every displayed line of §3:

- \(\beta(2-h)=h(4-5h)/(2-h)^2\), since the numerator is \(32-16h-5(2-h)^2-12=4h-5h^2\).
- \(h-\beta=h^2(1+h)/(2-h)^2\), \(c(h)=h(1+h)/(2-h)^2\), and \(1-c=(4-5h)/(2-h)^2\).
- \(\beta(2-h)=2\theta-3\theta^2\) with \(\theta=h/(2-h)\), so the mode is the AK\(\Gamma\) equality family, as the theorem package says.
- The spectrum \((-\tfrac23+h,\tfrac13-\tfrac h2,\tfrac13-\tfrac h2)\) is consistent with the closed identity. With \(|W^+|^2=\tfrac32\lambda^2\), \(s=-4\) and \(V=8\pi^2A/(2-h)^2\), one gets \(C_+=A(6h^2-8h+4)/(2-h)^2=A(1-\beta)\). This is exactly \(A-k+P/8\pi^2\).
- The distance to \(\mathcal K\) is attained with aligned eigenframes (Hoffman–Wielandt) and equals \(\sqrt{3/2}\,h\). Hence \(D_{\mathcal K}=4\sqrt6\pi^2k/(2-h)^2\).
- \(D_{\mathcal K}/D_{\min}=4/(4-5h)\), which gives \(12/7\) at \(h=1/3\).
- Directly, \((8\pi^2k-P)/\big(\tfrac{4\sqrt6}{3}D_{\mathcal K}\big)=1-\tfrac54h\).

Three further exact facts sharpen the reading.

1. **Size of the formal value.** \(P_{\rm formal}=8\pi^2A\,h^2(1+h)/(2-h)^2=2\pi^2k^2/A\,(1+O(h))\). If the conjecture were sharp with this mode as extremal, then \(c_0=2\pi^2\). In Step 47's normalization, the conditional Cotton law \((\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A})^2\approx16\pi^4k^2/(\Lambda A)\) is compatible with the formal mode only if \(\Lambda\ge8\pi^2\).

2. **Contact with LeBrun.** The mode touches LeBrun's bound at \(h=1/2\), since \(c(1/2)=1/3=1-1/(3h)\). This is \(\theta=1/3\), the minimum of \(\Gamma\). The contact lies outside the open range, so LeBrun's threshold and the common mode are one family.

3. **What K's saturation means.** K is saturated to relative order \(h\) along towers. Its linear \(L^1\) form therefore cannot by itself produce a quadratic law. The quadratic must come from passing from \(L^1\) to \(L^2\) plus an independent coercivity. The available chain is:
   - In the \(s=-4\) gauge, \(V\le 6\pi^2(A-k+P/8\pi^2)\). This follows from \(S/(96\pi^2)\le C_+\).
   - Hence \(\|E\|_2^2\ge(\int\operatorname{dist})^2/V\ge\pi^2(1-c)^2k^2/A\,(1+o(1))\).
   - Wherever \(\int\operatorname{dist}(W^+,\mathcal K)\le C_K\sqrt{VP}\) holds, one gets \(P\ge 6\pi^4(1-c)^2k^2/(C_K^2V)\).
   - For the formal mode, \(\int\operatorname{dist}/\sqrt{VP}=\sqrt6/(2\sqrt{1+h})\approx1.22\).

   **Repair to §2.** Its sentence "the signed identities and closed identity make the natural diffuse cost quadratic" should be replaced by this chain. No identity in the package bounds \(P\) below by \(\|E\|_2^2\). The closed identity is linear in \(\delta W^+\) at first order.

## 3. Dependencies and quantifiers: concrete repairs

**(a) \(A_C\) is a ball-quotient theorem, not a KE-host theorem.** Lemma M uses the homogeneity of \(\mathbb{CH}^2\): the Landau state \(\cosh^{-3}r\), the potential \(9\tanh^2r\), and the decay exponents. Step 47 §2 says "perturbative KE canonical-branch regime"; it should say ball quotients.

On a blow-up, no metric lies in the \(A_C\) neighbourhood, so \(A_C\) closes nothing on \(M\) until it is localized. Item 7 should say this plainly.

The useful content for O11 is steps 1–4 of its proof: Yamabe normalization, DeTurck gauge, and the Koiso TT gap giving \(P(\hat g)\ge(\kappa/8)^2\|h\|_{H^2}^2\). These steps are Riemannian and do not use Seiberg–Witten theory. Only steps 5–6, and hence the branch-selection problem, involve the monopole.

**(b) Two quantities are both called \(R\).** \(R_{W_2}=\mathbb E\int\rho^2|\nabla n|^2_{W_2}\) (Theorem N, §4) and \(R=\mathbb E\int|\nabla n|^2_{W_2}\) (Step 43, §2) differ by the weight. The bound \(P\ge8\pi^2k-2R\) loses a factor through \(\rho\le2\).

In the almost-Kähler setting, Proposition 43.C's left side is exactly \(\tfrac12\int a|\nabla n|^2=R_{W_2}/8\), because \(a=\rho^2/4\) and \(\nabla n\) is pure \(W_2\). The conditional law should be stated with \(R_{W_2}\). Then no hypothesis \(a\ge a_0\) is needed on the left. The zero-set difficulty moves to the adjoint terms. It is removed there if the test field is built from the smooth bilinear \(W_0=\tfrac14(\tfrac{\rho^2}{3}I-\psi\otimes\psi)\) rather than from \(n\).

**(c) Asking for "scalar variance on the Yamabe representative" asks for zero.** The measurable quantities are:
- \(P(g)-P(\hat g)=\big(S(g)-S(\hat g)\big)/12\), exact because \(W_+\) is conformally invariant;
- the almost-Kähler representative's variance, which Proposition 46.V predicts grows like \(\operatorname{Area}(E)/|t|\).

**(d) Hypotheses on the hosts.** Theorems N and K need \(b^+\ge2\), simple type, basic classes \(\pm K_X\), and \(A-k>0\). For ball-quotient hosts this means \(p_g\ge1\), which excludes fake projective planes.

**(e) What the formal-mode check is.** The computation in §3 checks K against an object that Lemma T excludes as a metric. Its value is the saturation statement in §2 above. It is not evidence that the mode is approximable.

**(f) Missing implication in §2.** Exact-collar cells glued into a ball quotient add their costs. Hence \(\inf_MP\le8\pi^2k\,p_{1,0}\). Any positive fixed-topology bound for pure blow-ups of a ball quotient therefore implies \(p_{1,0}>0\), and through Theorem D(iii) the nonexistence of standard-CR diagonal Einstein fillings.

The conjecture thus contains the cell problem of package §9.1. It is not independent of it.

**(g) Entropy does not reach the open range.** This was computed here with the mechanism of package §3.3. For an Einstein metric, \(2\chi-3|\tau|\ge\lambda^2V/6\pi^2\ge h^4V/54\pi^2\). With \(h_{\mathbb{CH}^2}=4\) and \(V=\pi^2\chi(Y)/6\) at \(\operatorname{Ric}=-6\), this gives \(2\chi-3|\tau|\ge\tfrac{64}{81}|d|\chi(Y)\). The real-hyperbolic case of the same computation reproduces the package's \(2|d|\chi(Y)\).

For \(Y\#k\overline{\mathbb{CP}}^2\) with \(k<\chi(Y)=A/3\), the left side is \(\chi+5k\) or \(3\chi-k\). Both exceed \(\tfrac{64}{81}\chi\). So a positive gap in the open range would be a genuinely new nonexistence statement.

## 4. The missing half of the ledger, and why it splits the conjecture

The closed identity gives \(P=8\pi^2k+4\Delta W_++\tfrac43\delta V\) in the \(s=-4\) gauge. Subtracting the signature identity \(W_+-W_-=12\pi^2\tau(M)\) gives, **for every metric on \(M=X\#k\overline{\mathbb{CP}}^2\)**,
\[
W_-(g)+\frac{S(g)-32\pi^2A}{48}=10\pi^2k+\frac{8\pi^2}{3}\bigl(\chi(X)-3\tau(X)\bigr)+\frac{P(g)}4 .
\]
Equivalently, \(\Delta W_-=10\pi^2k+P/4-\delta V/3\) relative to the KE value. This is the closed-manifold form of the package's cell relation \(\Delta W_+-\int|W^-|^2=-12\pi^2\).

Applied to the formal mode, it requires \(\delta V=2\pi^2k\) and \(\Delta W_-=\tfrac{28}{3}\pi^2k\). Step 47 never locates this anti-self-dual energy.

**Ball-quotient hosts.** Here \(W^-_{KE}=0\). At fixed scalar curvature the first variation of volume vanishes at an Einstein metric, since \(\int\langle\operatorname{Ric},h\rangle=\lambda\int\operatorname{tr}h=0\). So both \(\Delta W_-\) and \(\delta V\) are quadratic in the deviation from \(g_\Gamma\).

A diffuse common mode therefore needs \(|W^-|\sim\sqrt h\) everywhere: a curvature departure of order \(\sqrt h\), not \(h\). Two estimates then bound \(\int|\delta W^-|^2\) by a multiple of \(P\):
- **Low frequency.** The Koiso coercivity of \(A_C\) step 4 gives \(\int|\delta W^-|^2\le C\|h\|_{H^2}^2\le C'P\).
- **High frequency.** Computed here: for TT \(h\) at frequency \(\xi\), all three curvature blocks equal \(\tfrac12A\), where \(A_{ij}=-\tfrac12h_{ij}\). Hence \(|\delta W^+|^2=|\delta W^-|^2=|\delta\operatorname{Ric}^\circ|^2/4\). Conformal and gauge parts add nothing to \(W^\pm\).

Either way the \(10\pi^2k\) budget costs \(P\gtrsim k\) unless it sits in cores or in regions far from CH. So in the near-CH regime of ball-quotient blow-ups the expected law is **linear**, with constant set by cells. This holds conditionally on localization, and it needs no field selection at all.

**Hosts with \(W^-_{KE}\neq0\).** Here \(\Delta W_-\) has the first-order term \(2\int\langle W^-_{KE},\delta W^-\rangle\). A smooth deviation of size \(h\) pays the budget at cost \(\sim h^2V\sim k^2/A\). This is where the quadratic mechanism survives perturbatively.

**Unifying principle.** The linear channels of the Chern–Weil budget are the nonzero Weyl halves of the host:
- Real-hyperbolic hosts have neither channel; this is Theorem H's full tariff.
- Ball quotients have only \(W^+\).
- General KE hosts have both.

**A second exact consequence for the AK common mode.** With \(W^+=(1-\tfrac32h)K_n\), constant coefficient, and \(da=0\), Proposition 43.B gives \(\delta W^+=(1-\tfrac32h)\mathcal T(\nabla n)\). Hence \(\|C^+\|_2^2=\tfrac12(1-\tfrac32h)^2\int|\nabla n|^2\gtrsim k\), while \(P\sim k^2/A\).

Since \(|C^+|\lesssim|\nabla\operatorname{Ric}^\circ|\) at constant \(s\), any realization has Ricci frequency at least \((A/k)^{1/2}\). The "two scales" are therefore literal: a microscale \(\sqrt{k/A}\) inside the CH macroscale. On the Cotton route, the second-jet bound \(\|\mathcal C^*U\|\lesssim\|\operatorname{Rm}\|_2\) is saturated only by this microstructure.

**Repair to §2.** State the conjecture per host class. For ball-quotient hosts it is supported only in nonperturbative regimes. Add \(W_-\), its location (cores or bulk), and \(\int|\nabla\operatorname{Ric}^\circ|^2\) to the §4 measurement list.

## 5. The supplied source map

**Curvature-action decomposition: changes the route materially.** Its rule is to impose Bianchi at the level of representations before estimating. This produced the exact symbol identity above, which prices oscillatory anti-self-dual budget with no localization at all. It also identifies the free \((5/2,1/2)\) component of \(\nabla W^+\), not controlled by \(P\), as the term that Cotton transport must avoid.

**Coulomb bridge: supports the global-identity strategy, with one warning.** The budget identity of §4 is a global comparison identity whose constant \(10\pi^2k\) plays the role of the singular constants \(c_i\) that "cannot be dropped". The bridge's entry step has no analogue yet: there is no existence or separation statement for minimizers of \(P\), as package §8 records. A bulk/cell decomposition must therefore come from coercivity, not from naming cells.

**Exact-two-form inverse \(\|h\|^2=2\|h^+\|^2\): specific use.** It gives cover-uniform control of period-preserving corrections \(da\) with \((da)^-=\tfrac12\dot\star\Omega\) when many rotated cells are glued. This addresses A01's host-period stiffness without a one-form gap. It does not reach the lower bound.

**De Giorgi same-test identity: affects only the form of collar terms.** The SW analogue of \(q=1-v^2\) is the depletion, through the Weitzenböck identity \(\int\eta^2|\nabla\Phi|^2=\int\eta^2|\Phi|^2(1-|\Phi|^2/4)+\text{cutoff terms}\). Rotation is the defect term, and the cutoff terms are weighted by depletion gradients. This is the paying-by-depletion loop of Step 43, so it does not supply the missing estimate. Equation (4.7) already shows that the naive test has no defect.

## 6. Highest-value next proof object

**Theorem L (localized Einstein coercivity on a near-CH bulk, SW-free).** Let \(\Omega\Subset\Omega_1\subset M\), with \(\Omega_1\) a unit thickening of \(\Omega\). Suppose \(\hat g\) is \(\varepsilon_0\)-close to \(g_\Gamma\) in \(C^{2,\alpha}_b\) on \(\Omega_1\), after a local diffeomorphism, measured on unit balls of the universal cover. Then, in local DeTurck gauge,
\[
\int_\Omega\bigl(|W^-|^2+|W^+-W^+_\Gamma|^2\bigr)+\delta V(\Omega)\le C\Bigl[P(\hat g;\Omega_1)+\|h\|^2_{H^1(\Omega_1\setminus\Omega)}\Bigr],
\]
with \(C\) depending only on \(\mathbb{CH}^2\). The ingredients are the Bianchi-gauge operator's \(L^2\) gap on compactly supported tensors (no \(L^2\) Einstein deformations of \(\mathbb{CH}^2\)) and the pointwise masses of \(A_C\) steps 1–2.

**What L would decide.**
- **Ball-quotient hosts.** Combined with the budget identity, the \(10\pi^2k\) anti-self-dual budget must sit within unit distance of cores, up to \(C\cdot P\) plus the collar flux. Near-CH pure blow-ups of ball quotients then reduce exactly to the cell infimum \(p_{1,0}\).
- **General hosts.** Combined with K and Cauchy–Schwarz, L gives \(P\gtrsim k^2/A\) in the diffuse near-host regime, which is the conjecture's scale.

L replaces Step 47's item 1. It removes branch selection entirely, because K and the budget identity are field-free in their conclusions. It also removes the zero-set, Lee and \(a\ge a_0\) issues.

**Tests available now.**
- The certified and rotated cells glued into ball quotients have an exact CH bulk. L must place their \(\Delta W_-=\Delta W_++12\pi^2\) per cell in the cores.
- The formal mode with small \(h\) must be excluded near CH.
- The collar flux must match local Einstein deformations sourced at cores.

**What remains open after L.** The cell problem; the nonperturbative regime of Proposition 46.T, regime 3; and the Cotton/microstructure question for hosts with \(W^-\neq0\).