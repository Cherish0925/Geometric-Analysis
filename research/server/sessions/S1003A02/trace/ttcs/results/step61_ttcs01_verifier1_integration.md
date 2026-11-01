# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 61,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step61_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step61_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Theorem 61.EH in Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md: a sharp lower bound for the Einstein defect P(g)=∫|Ric°|² near an Eguchi–Hanson desingularization of an R^4/Z2 point of an orbifold that is Einstein near p, together with a matching upper bound. Check, with explicit computation where possible:
(1) Normalizations. Is Omega=(e^03−e^12)/r^4=−(1/4)d(σ3/r²) exactly ASD and harmonic on EH_a for every a, with the stated EH metric and the convention dσ3=σ1∧σ2? Do the o_i=Ω∘ω_i span Ozuch's O(eh) (compare Ozuch §1.2.2, o_k=−θ_1^−∘θ_k^+/r^4+…)? Is ||o_i||²=π²/a⁴ correct, with RP³ level sets of volume π²r³? Are the o_i mutually orthogonal?
(2) The flux pairing. Is B_i=∫_EH⟨DRic_EH[ĥ],o_i⟩=π²(R⁺ζ)_i, as computed in step60_EH_obstruction_pairing.py, correctly a flux at infinity? Check independence of the extension, the factor 1/2 for Z2, c0=0, and consistency with Ozuch's λ_k=c⟨R⁺(H₂)ζ,ζ_(k)⟩ in (22). Is the scaling ⟨Ric°(g̃),ô⟩=a²B correct in y=x/a units, with P scale-invariant? Is the resulting lower bound P ≥ π²a⁴|R⁺ζ|²(1−…) correct in its constant?
(3) Error bookkeeping in proof (a). The weighted neighbourhood with weight w<2; the claim that the order-a⁴ part of Ric° in 1≪|y|≤Λ vanishes by the Einstein jet equation, so E=O(a⁴); the linear term ⟨k,DRic*_{g̃}ô⟩ and the quadratic term; the cutoff of ô inside the region g̃=g_V. Find any genuine gap, e.g. diffeomorphism or gauge issues (P is diffeomorphism invariant but the neighbourhood is gauge-dependent), or whether ô must be corrected to remain approximately in ker DRic*_{g̃}.
(4) The upper bound (b) via Ozuch Lemma 2.3. Is Ric°(g*)=a²Σλ_k o_k+R₄ legitimate given that Ozuch's P=DRic+δ*B is gauged (does B(ĥ₂)=0 hold, or does δ*Bĥ₂ add a Ric° term)? Is λ_k=(R⁺ζ)_k in our o-normalization? Is the O(a⁶) remainder right?
(5) Consequences in §3. Is R⁺=I on the round unit S⁴, giving 2π²a⁴ for CP²#CP²? For KE orbifolds, is R⁺=diag(Λ,0,0) and is the holomorphic resolution direction ζ=ω̂ (versus ζ⊥ω)? Is the relation to Ozuch's Theorem 0.2 second obstruction diag(0,0,Λ) correct? Is the claimed Burns/EH duality on the kernel stratum (maximal Burns saving −(μ2−μ3)²/2 at μ2μ3=0; zero saving at the isotropic AdS-Taub-bolt type) arithmetically right and correctly interpreted?
Give corrected statements where needed.

## Integrated Scientific Memo

# Verification of Theorem 61.EH

**Verdict.** The exact EH norm and the step-60 flux give the correct leading obstruction energy
\[
\boxed{\pi^2a^4|R_p^+\zeta|^2.}
\]
However, Theorem 61.EH is **not correct as stated**. Its principal defects are:

1. the “naïve” comparison metric is insufficiently defined and need not have the expansion used in the proof;
2. the upper metric generally lies in \(\mathcal N_C\), not \(\mathcal N_{Ca^{2-w}}\);
3. an upper bound for the **total** functional requires the background to be Einstein globally, not merely near \(p\);
4. the uniform multiplicative infimum and near-extremal statements fail near \(\ker R^+\);
5. the KE and second-order consequences overstate what Ozuch proves.

The lower-bound argument can be repaired, and in fact its perturbation error is smaller than the stated \(O(\delta)\) error. This yields a useful sharper result for every fixed bounded neighborhood parameter.

## 1. Exact normalizations

Use
\[
e^0=f^{-1/2}dr,\quad e^1=\frac r2\sigma_1,\quad
e^2=\frac r2\sigma_2,\quad e^3=\frac{r\sqrt f}{2}\sigma_3,
\qquad f=1-a^4r^{-4},
\]
with orientation \(e^{0123}>0\). Then
\[
dr\wedge\sigma_3=\frac2r e^{03},\qquad
\sigma_1\wedge\sigma_2=\frac4{r^2}e^{12}.
\]
Consequently, with the stipulated convention \(d\sigma_3=\sigma_1\wedge\sigma_2\),
\[
d(\sigma_3/r^2)
=-\frac4{r^4}(e^{03}-e^{12}),
\]
so
\[
\boxed{\Omega=\frac{e^{03}-e^{12}}{r^4}
=-\frac14d(\sigma_3/r^2)}
\]
holds exactly for every \(a>0\). Since \(*e^{03}=e^{12}\), this is ASD, closed, and therefore coclosed.

There is an important qualification: this potential is defined on the complement of the bolt. **\(\Omega\) is smooth and harmonic globally, but is not globally exact.** Its bolt period is nonzero: in the compatible bolt orientation,
\[
\int_{S^2}\Omega=-\frac{\pi}{a^2}.
\]

Let \(J_i\) be the skew endomorphisms associated to the parallel SD Kähler forms \(\omega_i\), of form norm \(\sqrt2\). An ASD skew endomorphism commutes with every \(J_i\), and
\[
(r^4\Omega)^2=-I,\qquad
J_iJ_j=-\delta_{ij}I+\epsilon_{ijk}J_k.
\]
Thus \(o_i=\Omega\circ J_i\) is symmetric and trace-free, and
\[
\boxed{\langle o_i,o_j\rangle=\frac4{r^8}\delta_{ij}.}
\]
Harmonicity of \(\Omega\), parallelness of \(J_i\), and the hyperkähler identification
\(\operatorname{Sym}_0^2\simeq\Lambda^-\otimes\Lambda^+\) give
\[
\delta o_i=0,\qquad P_{EH}o_i=0.
\]
They therefore span the three-dimensional \(L^2\) kernel \(\mathbf O(eh)\) described in Ozuch §1.2.2.

The volume statements must distinguish **shell density** from **level-set area**:
\[
dV=\frac{r^3}{8}\,dr\,\sigma_{123},\qquad
\int_{\mathbb{RP}^3}\frac18\sigma_{123}=\pi^2.
\]
Hence
\[
\int_{\{r\le R\}}F(r)\,dV=\pi^2\int_a^R F(r)r^3\,dr,
\]
but the actual induced area of the EH level set is
\[
\boxed{\operatorname{Area}(\{r=\mathrm{const}\})=\pi^2r^3\sqrt f.}
\]
The norm calculation remains exactly correct:
\[
\boxed{\|o_i\|_{L^2(EH_a)}^2
=4\pi^2\int_a^\infty r^{-5}\,dr=\frac{\pi^2}{a^4}.}
\]

### Comparison with Ozuch

Ozuch’s ALE radial coordinate \(\rho\) and the displayed area-radius coordinate \(r\) satisfy
\[
r^4=\rho^4+a^4,\qquad \alpha_1=\sigma_3/2
\]
after relabeling axes. At \(a=1\), the leading tensors agree in magnitude with
\[
O_k^4=-\theta_1^-\circ\theta_k^+/\rho^4.
\]
A common sign depends on the identification of two-forms with endomorphisms and the ASD axis convention. This sign affects individual obstruction coefficients, not the squared energy. At general \(a\), the natural period-normalized variations are proportional to \(a^2o_i\), whose \(L^2\) norm is scale invariant.

The supplied norm script verifies the relevant exterior derivative and norm integrals, but does not actually implement the orthogonality check advertised in its docstring. The algebra above establishes that check exactly.

## 2. Flux pairing and its constant

Because \(o_i\) is TT and \(P_{EH}o_i=0\),
\[
DRic_{EH}^*o_i=0.
\]
Thus
\[
B_i=\int_{EH}\langle DRic_{EH}\widehat h,o_i\rangle\,dV
\]
is a boundary flux at infinity, with no contribution from the smooth bolt.

Extension independence requires derivative estimates as well as
\(\widehat h-h_2=O(r^{-2+\varepsilon})\). If two extensions differ by \(q\), their boundary terms satisfy
\[
q\,\nabla o_i\,R^3,\quad \nabla q\,o_i\,R^3
=O(R^{-4+\varepsilon})\longrightarrow0.
\]
The EH corrections to the limiting flat flux likewise vanish.

### Check of the supplied computation

The sphere-moment formula in `step60_EH_obstruction_pairing.py` integrates over the full \(S^3\), whose area is \(2\pi^2\). The final factor \(1/2\) is therefore exactly the \(\mathbb Z_2\) quotient factor.

For a radial cutoff \(\phi\),
\[
B_i=\frac12\int_0^\infty
\left(c_{2,i}r\phi''+c_{1,i}\phi'
+c_{0,i}\frac{\phi}{r}\right)\,dr.
\]
For the Einstein jet, \(DRic_\delta h_2=\Lambda\delta\), whose contraction with the flat trace-free tensor vanishes pointwise. Hence \(c_0=0\), and
\[
B_i=\frac12(c_{1,i}-c_{2,i}).
\]
The supplied JSON gives
\[
\boxed{
B=\pi^2\left(s/12+W^+_{11},\,W^+_{12},\,W^+_{13}\right)
=\pi^2R_p^+\zeta.}
\]

There is also an independent scalar-sector check. For the unit round sphere,
\[
h_{2,ij}=-\frac13(r^2\delta_{ij}-x_ix_j).
\]
Contraction of \(DRic_\delta(\phi h_2)\) with the first flat obstruction tensor gives full-sphere radial density
\[
\frac{2\pi^2}{3}(r\phi''+4\phi').
\]
Therefore
\[
c_2=\frac{2\pi^2}{3},\qquad c_1=\frac{8\pi^2}{3},\qquad
B_1=\pi^2,
\]
reproducing the JSON at \(s=12,\ W^+=0\).

The main symbolic script includes the general \(W^-\) and traceless-Ricci variables, which disappear from its reported answer. The auxiliary sector script supplies examples, not by itself a proof for all sectors. The imported curvature-construction module is not supplied here, so its implementation cannot be directly audited; the flux structure and independent scalar check corroborate the normalization.

### Normal gauge versus Bianchi gauge

“Bianchi/normal coordinates” should be replaced by two distinct representatives. The geodesic-normal jet
\[
h_{2,ij}=-\tfrac13R_{iajb}x^ax^b
\]
is generally **not** in flat Bianchi gauge when \(\Lambda\ne0\).

This does not change the Ricci flux. A cubic coordinate change adds \(\mathcal L_X\delta\), and
\[
\mathcal L_XEH=\mathcal L_X\delta+O(r^{-2}),\qquad
DRic_{EH}(\mathcal L_XEH)=0.
\]
Thus the normal-coordinate computation has the same \(B_i\) as Ozuch’s Bianchi representative.

At \(a=1\), in the basis used for the flux,
\[
\lambda_i\pi^2=B_i,\qquad
\boxed{\lambda_i=(R_p^+\zeta)_i.}
\]
Ozuch uses SD forms of norm \(\sqrt2\), so
\(\langle R^+\omega_1,\omega_i\rangle=2(R^+\zeta)_i\).
His unspecified positive constant is compatible with magnitude \(1/2\) once the individual basis signs are aligned. It is safer to state the coefficient in the explicitly normalized basis above rather than equate signed bases without recording that alignment.

### Scaling

With \(F_a(y)=ay\), set
\[
G_a=a^{-2}F_a^*g.
\]
Then
\[
G_a=EH_1+a^2\widehat h+O(a^4|y|^4),
\qquad
Ric^\circ(G_a)=a^2DRic^\circ_{EH_1}\widehat h+\cdots.
\]
Constant metric rescaling preserves the \(L^2\) norm of covariant two-tensors in dimension four. Therefore
\[
\langle Ric^\circ(G_a),o_i\rangle=a^2B_i+\cdots,
\]
and the projected energy is
\[
\frac{|a^2B|^2}{\pi^2}
=\boxed{\pi^2a^4|R_p^+\zeta|^2}.
\]

## 3. Repairs to the lower-bound proof

### The comparison metric must be specified

A pure EH core interpolated to \(g_V\) at a fixed physical radius generally has an \(O(t_0^2)\) mismatch independent of \(a\); it does not have the expansion used in the note.

The intended center must instead be a **jet-extended superposition**, schematically
\[
g_V+\chi_{t_0}(EH_a-\delta),
\]
with the background jets extended smoothly over the bolt. In scaled variables its core must satisfy
\[
\widetilde G_a=EH_1+a^2\widehat h_2+a^4\widehat h_4+\cdots,
\]
and match the exact background outside the fixed gluing region. The lower estimate below applies to this explicitly controlled center.

### Test-tensor norm

The background perturbation \(a^2h_2=O(a^2r^2)\) produces an \(O(a^2)\), not merely \(O(a^4)\), norm error:
\[
\|\chi_Lo_b\|_g^2
=\pi^2+O(a^2)+O(\delta a^2)+O(L^{-4}),
\qquad |b|=1.
\]

### Einstein-jet cancellation

The order-\(a^4\) pure-background terms cancel by the quartic Einstein jet equation. The surviving EH-tail interactions are \(O(a^4r^{-2})\), whose pairing with \(o=O(r^{-4})\) has radial density \(O(a^4r^{-3})\), integrable at infinity.

But a finite Taylor expansion alone does not control the entire region \(r\lesssim a^{-1}\): an untreated growing remainder can contribute at leading order. The repair is to compare with the **exact Einstein background**, so all pure-background terms cancel together. The curvature variation is
\[
a^2(Rm_p+O(a^2r^2)),
\]
and its interaction with the \(O(r^{-4})\) EH tail gives the integrable remainder above. This establishes the required pairing expansion
\[
\langle Ric^\circ(\widetilde G_a),\chi_Lo_i\rangle
=a^2B_i+O(a^4).
\]

### Perturbation estimates

Write \(k=G_a-\widetilde G_a\), with
\[
|\nabla^jk|\le \delta a^2(1+r)^{w-j}.
\]
The approximate adjoint-kernel residual has the structure
\[
(DRic^\circ_{\widetilde G_a})^*(\chi_Lo_i)
=a^2O(r^{-4})+O(L^{-6})
\]
on the cutoff shell. No correction to an exact adjoint-kernel tensor is needed at this accuracy.

The linear pairing error is
\[
O\!\left(\delta a^4J_w(L)+\delta a^2L^{w-2}\right),
\quad
J_w(L)=
\begin{cases}
1+\log L,&w=0,\\
O(L^w),&w>0.
\end{cases}
\]
The quadratic error is
\[
O\!\left(\delta^2a^4K_w(L)\right),\qquad
K_w(L)=
\begin{cases}
O(1),&0\le w<1,\\
O(1+\log L),&w=1,\\
O(L^{2w-2}),&1<w<2.
\end{cases}
\]
Thus “every error integral converges for \(w<2\)” is false literally; some grow or are logarithmic. Their **scaled contributions are nevertheless \(o(a^2)\)**.

Variations of the inner product, volume element, and trace-free projection must also be included. They are controlled by the same estimates and the \(O(a^2)\) test-norm error.

For \(L\asymp t_0/a\), define
\[
\varepsilon_w(a,\delta)=C\left[
a^2+
\begin{cases}
\delta a^2(1+|\log a|),&w=0,\\
\delta a^{2-w},&0<w<2
\end{cases}
+
\begin{cases}
\delta^2a^2,&w<1,\\
\delta^2a^2(1+|\log a|),&w=1,\\
\delta^2a^{4-2w},&1<w<2.
\end{cases}
\right].
\]
For bounded \(\delta\), this tends to zero. Cauchy–Schwarz then gives the stronger repaired bound
\[
\boxed{
P(g)\ge
\pi^2a^4\bigl(|R_p^+\zeta|-\varepsilon_w(a,\delta)\bigr)_+^2.}
\]
In particular, the note’s weaker \(C(\delta+a^{2-w})\) estimate survives after these repairs.

### Cutoff and diffeomorphisms

The asserted placement \(L=t_0/(2a)\) in a region where \(\widetilde g=g_V\) is not implied by the definition. Either place the cutoff beyond the gluing annulus, within the Einstein neighborhood, or explicitly estimate that annulus. Both give the same leading constant.

A diffeomorphism-saturated neighborhood is legitimate: work with the representative satisfying the estimate and transport the test tensor with that representative. No Bianchi gauge is needed for the **lower** variational estimate. What is not justified is identifying this unusually tight, \(O(a^2)\)-core neighborhood with Ozuch’s GH neighborhood.

## 4. Upper bound: gauge, construction, and neighborhood mismatch

### The gauged operator does not create a first-order Ricci defect

For Ozuch’s Bianchi quadratic jet,
\[
P_{EH}\underline h_2=\Lambda EH+\sum_i\lambda_i o_i,
\qquad \underline h_2=H_2+O(r^{-2}).
\]
Applying \(B_{EH}\), using the linearized contracted Bianchi identity, gives
\[
\tfrac12\nabla^*\nabla(B_{EH}\underline h_2)=0.
\]
Because \(B_\delta H_2=0\), the one-form \(B_{EH}\underline h_2\) decays as \(O(r^{-3})\). Integration by parts implies it is parallel, and decay implies it vanishes. Hence
\[
\boxed{B_{EH}\underline h_2=0,\qquad
DRic_{EH}\underline h_2=\Lambda EH+\sum_i\lambda_i o_i.}
\]
This proves the needed gauge statement; it should not simply be asserted as part of Lemma 2.3.

Using the normal-coordinate jet directly in the gauged equation would not justify the same conclusion. Its Bianchi term is growing, and gauged and ungauged fluxes can differ by a nonzero boundary term.

### Nonlinear remainder

Lemma 2.3 supplies
\[
\underline h_2=H_2+H_2^4+O(r^{-4+\epsilon}),\qquad
H_2^4=O(r^{-2}).
\]
Combine this with the exact Einstein background and a smooth matching construction. Then the first-order adapted metric has
\[
Ric^\circ(G_a^*)=a^2\sum_i\lambda_i o_i+R_a,\qquad
|R_a|\le Ca^4(1+r)^{-2}
\]
in the core, with corresponding fixed-physical-annulus bounds. The cancellation argument and matching estimates are additional work beyond the statement of Lemma 2.3.

These estimates yield
\[
\|R_a\|_2^2=O(a^8\log(1/a)),\qquad
a^2\left|\left\langle\sum_i\lambda_i o_i,R_a\right\rangle\right|
=O(a^6).
\]
Thus
\[
\boxed{P(g_a^*)=\pi^2a^4|R_p^+\zeta|^2+O(a^6).}
\]
The stated \(O(a^6\log(1/a))\) is a valid weaker remainder. When \(R_p^+\zeta=0\), this construction instead gives
\[
\boxed{P(g_a^*)=O(a^8\log(1/a)).}
\]

An exact \(a^6\) coefficient \(2\pi^2\langle\lambda,\mu\rangle\) is **not established** by the note’s first-order construction: it requires the fully matched second-order metric, gauge corrections, and metric-dependent pairing expansion.

### Failure of the claimed membership

For a generic center with extension \(\widehat h_2\),
\[
G_a^*-\widetilde G_a
=a^2(\underline h_2-\widehat h_2)+\cdots.
\]
At \(r=O(1)\), this is generically \(O(a^2)\), whereas
\(\mathcal N_{Ca^{2-w}}\) requires \(O(a^{4-w})\). Therefore
\[
\boxed{g_a^*\in\mathcal N_{C_0}\ \text{in general, not }
\mathcal N_{Ca^{2-w}}.}
\]

There are two consistent sharp formulations:

- **Adapted center:** use \(\underline h_2\) in the center itself. Its energy supplies the upper bound in arbitrarily small neighborhoods of that center.
- **Generic center:** retain it, but require \(\delta\ge C_0\) to contain the upper metric. The sharper lower estimate above still converges to the coefficient \(\pi^2|R^+\zeta|^2\) for fixed \(C_0\).

For arbitrarily small \(\delta\) around a generic center, no matching upper bound follows; additional energy in the component orthogonal to the EH cokernel can remain.

Finally, if \(g_V\) is Einstein only near \(p\), a construction unchanged elsewhere has
\[
P(g_a^*)=P(g_V)+\pi^2a^4|R_p^+\zeta|^2+O(a^6).
\]
The displayed upper bound without \(P(g_V)\) requires global Einsteinness, or must be stated for a localized defect.

### Infimum and near-extremal statements

The uniform statement must be additive:
\[
\pi^2a^4(q-\varepsilon)_+^2
\le \inf P
\le \pi^2a^4q^2+O(a^6),\qquad q=|R^+\zeta|,
\]
in a neighborhood containing the adapted upper metric. A multiplicative asymptotic is valid only when \(q\) is bounded below.

Let \(\Pi_g\) be the actual \(L^2(g)\) projection onto the cutoff obstruction space. The repaired near-extremal estimate is
\[
\boxed{
\|(1-\Pi_g)Ric^\circ(g)\|_2^2
\le \pi^2a^4\bigl[\eta q^2+Cq\varepsilon\bigr],}
\]
with Gram-matrix errors absorbed into \(\varepsilon\). This follows directly by subtracting the projected-energy lower bound from the assumed total energy. The original error proportional to \(\varepsilon q^2\) is not uniform near \(q=0\).

## 5. Consequences and second-order interpretation

### Round sphere

For unit sectional curvature,
\[
s=12,\qquad W^\pm=0,\qquad R^\pm=I.
\]
Two equal-scale insertions therefore have adapted leading energy
\[
\boxed{2\pi^2a^4.}
\]
The orbifold notation must mean the suspension quotient with involution
\[
(x_1,\dots,x_4,x_5)\mapsto(-x_1,\dots,-x_4,x_5),
\]
which has two \(A_1\) points, not the antipodal quotient \(\mathbb{RP}^4\). Appropriate same-orientation resolutions give the stated \(\mathbb{CP}^2\#\mathbb{CP}^2\), up to orientation.

This is a local sharp asymptotic, not a universal rate for all sequences with \(P\to0\).

### Kähler–Einstein directions

In the complex orientation,
\[
W^+=\operatorname{diag}(s/6,-s/12,-s/12),\qquad
\boxed{R^+=\operatorname{diag}(\Lambda,0,0).}
\]
The holomorphic exceptional-curve resolution direction is indeed
\(\zeta=\widehat\omega\), giving leading cost \(\pi^2\Lambda^2a^4\).

For \(\zeta\perp\widehat\omega\), the leading obstruction vanishes. But calling these directions simply “non-Kähler” is misleading: EH is hyperkähler and is Kähler also for the complex structure associated to \(\widehat\omega\). The bolt has zero \(\widehat\omega\)-period and is Lagrangian in that structure. These period directions are associated with the local smoothing interpretation rather than the holomorphic exceptional-curve resolution. Local compatibility does not prove existence of a global Kähler or Einstein smoothing.

In a basis \((\zeta,\zeta',\widehat\omega)\),
\[
R^+=\operatorname{diag}(0,0,\Lambda).
\]
This satisfies the algebraic conclusion of Ozuch’s Theorem 0.2. That theorem is necessary, not sufficient, and has the stated compactness, integrability, and stability/rigidity hypotheses. It does **not** prove that KE orbifolds are exactly those unobstructed through second order, nor that existence is invariably decided only by third and higher local obstructions.

### Burns/EH arithmetic and the already-known second obstruction

Write the complementary eigenvalues as \(u,v\), avoiding confusion with Ozuch’s coefficients \(\mu_k\). On the nonpositive kernel stratum,
\[
u+v=\Lambda,\qquad uv\ge0,\qquad
(u-v)^2=\Lambda^2-4uv.
\]
At fixed \(\Lambda<0\), the splitting is maximal exactly when \(uv=0\), and zero exactly when \(u=v=\Lambda/2\). Thus the extremizers of the **quoted** Burns saving are arithmetically correct. Its coefficient cannot be independently verified from the supplied files, which contain no Burns calculation.

Ozuch §2.1.4 already proves, when the first obstruction vanishes,
\[
\boxed{\mu_1=C\det(R^+|_{\zeta^\perp}),\qquad C>0}
\]
in his conventions. Therefore the determinant zero set in Conjecture 61.D is not conjectural. What remains unresolved is the explicitly normalized coefficient, the other second-order components, and a matching minimized-defect theorem at order \(a^8\).

For the AdS Taub–bolt example,
\[
R^+=\operatorname{diag}(0,-3/2,-3/2),
\]
so the splitting vanishes but the complementary determinant is \(9/4\). This is a curvature type ruled out in the relevant **compact** settings; the AH example itself does admit Einstein desingularizations because conformal-infinity deformations can compensate obstructions.

The invariants “splitting” and “determinant” are not independent at fixed trace. Moreover, an \(a^8\) minimized-defect law must restrict background Einstein deformations and direction/scale changes: Ozuch’s Corollary 2.12 explains how a changing first obstruction can compensate the second one.

### Other ALE bubbles

The projection principle remains useful:
\[
\text{leading energy}=B^{T}G^{-1}B\,a^4,
\qquad G_{ij}=\langle o_i,o_j\rangle.
\]
But the extension is not “verbatim.” One must determine decay, period normalization, all cokernel modes, and matching errors. Ozuch Remark 2.21 explicitly notes curvature-derivative obstructions for \(A_k\) singularities. The quadratic-jet flux principle does not by itself establish the asserted full \(A_n\) or Wahl theory.

**Corrected core result:** the EH flux and Gram matrix rigorously identify the sharp coefficient; the repaired weighted lower estimate preserves it for fixed bounded \(\delta\); a matching upper metric is obtained from the Bianchi-gauge adapted first-order solution, with \(O(a^6)\) energy remainder. Matching in the original shrinking neighborhood, an unrestricted second-order \(a^8\) law, and passage from GH proximity or small \(P\) to these weighted neighborhoods remain unproved.