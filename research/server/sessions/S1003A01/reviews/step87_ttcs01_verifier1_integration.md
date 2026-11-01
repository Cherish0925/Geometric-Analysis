# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 87,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step87_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step87_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of the Step-87 note (Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md) on Einstein rigidity near a negative Kähler–Einstein orbifold with one A1 node (generic nodal quintic surface). Research context: closed negative almost-Kähler Einstein (Goldberg) problem and Einstein metrics near KE orbifold endpoints; earlier work reduced the question to a scale-uniform C^1 estimate of Ozuch's normal obstruction Lambda_I. The note claims to replace that derivative estimate by (i) an exact eigenvalue statement (Prop 87.2, from Nagy eq. (17): harmonic primitive (1,1) forms give Hermitian TT eigentensors of the Einstein operator with eigenvalue -2E), (ii) an exact secant along the Biquard–Rollin CSCK family varying the real Kronheimer period zeta_r: Ric-Eg=rho_0(.,J.) with rho_0 harmonic ASD in class 2 pi c1 - E[omega], giving Lambda_I = E zeta_r (1+o(1)) and P=-2(2pi c1-E[omega])^2 (§3, Lemma 87.3), and (iii) a C^0 degree argument (Theorem 87.4) showing the corrected CSCK family fills Ozuch's reduced Einstein-modulo-obstruction family, so every nearby Einstein metric is KE; plus Lemma 87.5 (bubble is orientation-matched EH, no trees) and Cor 87.6 (no strict AKE nearby via the length obstruction). Please check carefully and write a direct scientific memo: (1) correctness of the cohomological identities and normalizations (|Ric0|^2=2|rho0|^2, period int_delta rho_0 = -E zeta_r, theta^2 -> -2, EH L2 form normalization ||theta||^2=2, A=E i.e. c0=1) — compare with the JSON data; (2) whether Prop 87.2 is correct including the claim that no small nonzero TT eigenvalue arises from the degeneration (are o_J, o_K really exact kernel at KE smoothings? is the count 78+2 correct?); (3) the logic of Theorem 87.4: is the EmO correction estimate ||k|| <= C|zeta_r| o(1) justified given Ozuch-type uniform inverses, is uniqueness used correctly, does the degree argument on shells really give surjectivity onto the reduced family (and is the reduced family a graph over parameters so that 'hitting the parameter' identifies the metric), and is anything circular; (4) whether the weighted hypothesis (Hp-w) is plausible with the stated rates, and whether CSCK metrics in classes with zeta_r != 0 on smoothings (and resolutions, Theorem C) really exist uniformly over all directions on S^2 under Biquard–Rollin non-degeneracy for A1; (5) Lemma 87.5's proof (Bishop–Gromov exclusion of trees, Gauss–Bonnet/signature comparison with EH, pi_1 argument); (6) any hidden gap that would invalidate Corollary 87.6, and what is genuinely new versus standard. Separate proved, conditional, and false statements; propose repairs where something fails.

## Integrated Scientific Memo

# Verification memo: Step 87

## Main conclusion

The exact Kähler identities and Proposition 87.2 are correct. They give a useful **period-normalized calibration**
\[
\langle \operatorname{Ric}-Eg,\hat o_I\rangle
=E\zeta_r+o(|\zeta_r|)
\]
along a suitably controlled CSCK comparison family.

They do **not yet prove endpoint rigidity**. The remaining issue is not the algebraic coefficient: it is a uniform comparison between the CSCK family and **one fixed Ozuch reduction**, including its gauge, obstruction space, weighted norms, and parameter slice. The degree argument is valid after that comparison is established, but cannot establish it.

In particular:

- Lemma 87.3 needs a small analytic repair before being called proved.
- The global cut-off \(o_J,o_K\) are not exact kernel tensors.
- The absence of additional eigenvalues approaching zero needs a separate spectral result.
- The correction in Theorem 87.4 must be made in the same reduction whose parameters are used in the degree argument.
- Corollary 87.6 follows for the prescribed complex orientation; its proof does not address an opposite-oriented almost-Kähler structure.

## 1. Exact identities, JSON checks, and the coefficient

Throughout, \(c_1=c_1(T^{1,0}M)\), not \(c_1(K_M)\), and the orientation is the complex orientation.

### CSCK identities: correct

For a Kähler surface with \(s=4E\),
\[
\rho_0=\rho-E\omega
\]
is closed and primitive:
\[
\Lambda_\omega\rho=2E,\qquad \Lambda_\omega\omega=2.
\]
Thus \(\rho_0\) is ASD and harmonic. With the composition convention of the note,
\[
\operatorname{Ric}^{\circ}(X,Y)=\rho_0(X,JY),\qquad
|\operatorname{Ric}^{\circ}|^2=2|\rho_0|^2.
\]
Consequently
\[
P=\int_M|\operatorname{Ric}^{\circ}|^2
=2\|\rho_0\|_{L^2}^2
=-2[\,2\pi c_1-E[\omega]\,]^2.
\]
These are exact, standard Kähler/Chern–Weil identities.

Set \(C=c_1^2\), \(T=\theta^2\), and
\[
[\omega]=\lambda\left(\frac{2\pi c_1}{E}+\varepsilon\theta\right),
\qquad c_1\cdot\theta=0.
\]
The scalar-curvature normalization gives
\[
\lambda=\frac{4\pi^2C}{4\pi^2C+E^2\varepsilon^2T}.
\]
Using \(\theta=\delta^{1,1}\), hence \(\theta\cdot\delta=T\), one obtains
\[
\zeta_r=[\omega]\cdot\delta=\lambda\varepsilon T,\qquad
\int_\delta\rho_0=-E\zeta_r,
\]
and
\[
\frac{P}{E^2\zeta_r^2}
=-\frac2T-\frac{E^2\varepsilon^2}{2\pi^2C}.
\]
All these expressions agree with the JSON.

Writing
\[
\delta=\theta+\eta,\qquad \eta=\delta^{2,0}+\delta^{0,2},
\]
gives
\[
T=-2-\eta^2.
\]
Thus \(T\le-2\), and \(T\to-2\) when the global holomorphic periods of the vanishing cycle tend to zero. The estimate \(\eta=O(|\zeta_c|)\) uses controlled Hodge metrics and the local vanishing-period calculation; it is not a symbolic consequence of the JSON.

At \(\zeta_r=0\), the chosen class has \(\varepsilon=0\), \(\lambda=1\), and \([\rho_0]=0\). Harmonicity then proves \(\rho_0=0\), so the CSCK metric is KE without needing a separate CSCK uniqueness theorem.

### Eguchi–Hanson normalization: correct, with an orientation clarification

The supplied script gives
\[
\theta_{EH}=-\frac{4c}{r^4}(e^{03}+e^{12}),\qquad
\int_S\theta_{EH}=-\frac{4\pi c}{a^2}.
\]
Therefore \(c=a^2/(2\pi)\) yields
\[
\int_S\theta_{EH}=-2,\qquad
|\theta_{EH}|=\frac{2\sqrt2\,a^2}{\pi r^4},\qquad
\|\theta_{EH}\|_{L^2}^2=2.
\]
Indeed,
\[
\|\theta_{EH}\|^2
=\int_a^\infty\frac{32c^2}{r^8}\frac{r^3}{8}(8\pi^2)\,dr
=\frac{8\pi^2c^2}{a^4}.
\]

The displayed form is self-dual for the ordered frame orientation \(e^{0123}\). To identify it as the ASD representative of \(PD(S)\), one must use the opposite, hyperkähler complex orientation. Then
\[
\int\theta_{EH}\wedge\theta_{EH}=-2=S^2.
\]
The JSON checks magnitude and period, but does not itself check this orientation sign.

### Calibration: \(A=E\) in the note’s coordinate, not automatically Ozuch’s raw coordinate

Let
\[
o_I=\theta_{EH}\circ I.
\]
Then
\[
\|o_I\|^2=2\|\theta_{EH}\|^2=4,\qquad \hat o_I=o_I/2.
\]
If the harmonic concentration comparison is valid,
\[
\rho_0=\frac{E\zeta_r}{2}\theta_{EH}+o_{L^2}(|\zeta_r|),
\]
and hence
\[
\Lambda_I
=\langle\operatorname{Ric}^{\circ},\hat o_I\rangle
=E\zeta_r+o(|\zeta_r|),\qquad
P=\Lambda_I^2(1+o(1)).
\]
Thus \(c_0=1\) for the explicitly defined **period coordinate and \(L^2\)-unit test tensor**.

Ozuch’s supplied text uses metric parameters \(\zeta\), parameter-derivative tensors \(o_k\), and coefficients with an unspecified constant \(c>0\). The conversion to the bolt-period coordinate must be computed before calling this a calibration of his *raw* coefficient. Likewise, a pairing with the physical Einstein defect is not automatically the coefficient of his gauge-fixed reduced equation.

## 2. Lemma 87.3: correct mechanism, incomplete proof as written

Two ingredients are missing from the displayed proof:

1. the cutoff form’s norm must be measured in the **actual CSCK metric**, not only in exact EH;
2. the exterior class \(y\) needs a representative with uniformly bounded \(L^2\) norm.

Both can be handled directly under uniform geometric comparison.

Let \(d=E\zeta_r/2\). The decomposition
\[
[\rho_0]=d\delta+y
\]
has \(y\cdot\delta=0\) exactly, because
\[
[\rho_0]\cdot\delta=-E\zeta_r=d\delta^2.
\]
Thus \(y\) is an exterior class in the Mayer–Vietoris decomposition. A bounded exterior basis represented away from the node gives
\[
\|\gamma_y\|_{L^2}\le C|y|,
\]
provided the exterior metrics converge uniformly on its support. The class calculation gives
\[
|y|=O\!\left(|\zeta_r|(|\eta|+|\varepsilon|)\right).
\]

There is a particularly useful exact identity. If \(\alpha\) is any closed representative of \([\rho_0]\), then
\[
\boxed{\ \|\alpha-\rho_0\|_{L^2}^2=2\|\alpha^+\|_{L^2}^2.\ }
\]
Indeed, harmonicity gives Pythagoras, while ASD gives
\[
\|\rho_0\|^2=-[\rho_0]^2=-\int\alpha\wedge\alpha.
\]
Choose
\[
\alpha=d\,\theta_{EH}^{\rm cut}+\gamma_y.
\]
The cutoff tail contributes \(O((a/R)^2)\) to its self-dual \(L^2\) component. Metric comparison contributes an additional \(o(1)\) term. Consequently
\[
\|\rho_0-d\theta_{EH}^{\rm cut}\|_{L^2}
\le |d|\bigl[O((a/R)^2)+o(1)\bigr]+C|y|.
\]

This establishes the intended relative \(L^2\) concentration once those uniform comparisons are supplied. It also resolves the differing assessments of the lemma: the exact identity is sound, but it does not remove the need to bound the exterior representative or compare the actual Hodge star with EH.

It still does **not** establish Hp-w.

## 3. Proposition 87.2 and the spectrum

### Proposition 87.2: proved

Nagy §4.1, equation (17), identifies the Hermitian Einstein operator with \(\Delta_d-2E\):
\[
g^{-1}(\Delta_d-2E)A=(\Delta_EH)\circ J.
\]
For harmonic primitive \(\theta\), the associated \(H_\theta\) is trace-free and divergence-free, and
\[
\Delta_EH_\theta=-2E\,H_\theta.
\]
On Hermitian TT tensors,
\[
\langle\Delta_EH,H\rangle\ge -2E\|H\|^2,
\]
with equality precisely for primitive harmonic real \((1,1)\) forms.

For a smooth quintic, the multiplicity **in this sector is exactly**
\[
h^{1,1}-1=44.
\]
“At least 44” remains harmless when referring to the full TT spectrum.

Ozuch’s gauge-fixed linearization is \(P=\frac12\Delta_E\), so its corresponding eigenvalue is \(-E\), not \(-2E\).

### The \(78+2\) count: correct; the literal tensor claim: false

The smooth quintic has 40 complex deformation directions, hence an 80-real-dimensional, integrable negative-KE Einstein kernel. The nodal stratum has 39 complex directions, hence 78 real exterior directions. The two additional real directions arise from smoothing.

However:

- cut-off EH tensors are not globally divergence-free merely because their uncut ALE versions are;
- cut-off \(o_J,o_K\) are not exact global kernel elements;
- \(J,K\) here are local hyperkähler structures, not globally parallel structures on a quintic.

The correct statement is that suitably normalized, globally corrected smoothing tangents are exact KS kernel tensors and approximate the local EH pair, subject to an appropriate gluing comparison. The typo “remaining \(3+78\)” should be “remaining \(2+78\).”

Similarly, \(H_{\theta_t}\) is an exact eigenmode; the cutoff tensor it approximates is not.

### “No small nonzero TT eigenvalue”: not proved by Proposition 87.2

The Hermitian bound is uniform and immediately excludes such eigenvalues in that sector. It says nothing by itself about a uniform positive gap above the anti-Hermitian kernel.

A proof for the full TT operator needs a uniform complement estimate or spectral-gluing theorem that controls exterior, ALE, and intermediate-neck concentration. Kernel counting alone is insufficient. BR’s estimates for the **form Laplacian** are not that theorem.

The supplied Ozuch material provides relevant complementary inverse templates and explicitly treats exact-versus-approximate kernels through Lemma 3.9 and Proposition 3.10. It does not directly prove the claimed quintic \(L^2\)-spectral statement. Retain this as a separate input, with its norm and theorem specified.

Finally, the sentence identifying the normal derivative directly with the eigenmode’s Rayleigh quotient suppresses the factor \(1/2\) and the conversion between a period derivative and a unit tensor. Nonvanishing is compatible; numerical equality requires that conversion.

## 4. Theorem 87.4: a viable argument after fixing the reduction

### What the supplied Ozuch source supports

The source explicitly describes:

- GH-near Einstein metrics represented in a weighted gluing slice: Definition 1.29 and the preceding paragraph;
- complementary inverse estimates: for example Proposition 3.10, item (2);
- a unique EmO solution for a specified base, obstruction space, and orthogonality condition: Definition 3.21;
- correction estimates controlled by the projected source: Lemma 3.23.

These substantiate the architecture. The exact general result O1 for the negative nodal quintic still rests on Ozu19a,b, whose full texts are not supplied here.

### The important correction: use one fixed gauge and obstruction bundle

An EmO metric constructed with one base/cokernel is not automatically an EmO metric for another. A parameter extraction map alone does not preserve the projected equation. Thus the proof’s use of uniqueness is unjustified unless \(\Xi(p)\) was constructed in precisely the reduction indexed by \(\pi(\Xi(p))\).

A clean repair is:

1. For each CSCK parameter \(p\), find \(q=m(p)\) and a diffeomorphism \(\phi_p\) so that
   \[
   \bar g_p=\phi_p^*g_p^{\rm CSCK}
   \]
   lies in the prescribed Ozuch gauge and satisfies
   \[
   \bar g_p-g_q^D\perp\widetilde O_q.
   \]
   This is a modulation/slice problem. Uniform invertibility must be checked in scale-adapted coordinates, not inferred from an unscaled Gram matrix.

2. Let \(G(q)\) be the unique Ozuch EmO graph. In that **same slice**, prove
   \[
   \|G(m(p))-\bar g_p\|_X
   \le C\|\Pi_{m(p)}^\perp\Phi_{g_{m(p)}^D}(\bar g_p)\|_Y
   =o(|\zeta_r(p)|),
   \]
   where
   \[
   X=C_{\beta,*}^{2,\alpha},\qquad Y=r_D^{-2}C_\beta^\alpha.
   \]

3. Prove that the obstruction pairing changes by \(o(|\zeta_r|)\):
   \[
   \ell_{m(p)}(\Phi(G(m(p))))
   =E\zeta_r(p)+o(|\zeta_r(p)|).
   \]
   This requires a bounded pairing estimate for the linear and quadratic terms in these norms, including gauge and changing test-tensor effects.

At \(\zeta_r=0\), \(\bar g_p\) is Einstein and satisfies the slice conditions. Uniqueness gives \(G(m(p))=\bar g_p\).

This formulation avoids the ambiguous “correction, then parameter extraction” in the note.

### Degree argument: correct under the matching hypothesis

Suppose, in compatible marked coordinates,
\[
|m_\zeta(v,\zeta)-\zeta|\le\eta|\zeta|,
\qquad |m_v(v,\zeta)-v|\le\eta,\qquad \eta<\frac12.
\]
For a target \((v^*,\zeta^*)\), the straight-line homotopy avoids it on the boundary of
\[
|v-v^*|<2\eta,\qquad
|\zeta^*|/2<|\zeta|<2|\zeta^*|.
\]
The identity has degree one there, so the target is hit. Domain margins must be reserved for the shell.

Because \((\mathbb R^3\setminus0)/\pm\) is nonorientable, use either:

- a compatible marked lift;
- degree modulo two; or
- a small ball about \(\zeta^*\), avoiding zero and its antipode.

The degree proves surjectivity of **\(m\)**. Hitting a parameter identifies the metric only because \(G(q)\) is a unique graph with the stated gauge, orthogonality, and projected equation.

There is no inherent circularity. There would be circularity if the modulation comparison, uniform inverse, or graph identification were justified by the desired rigidity itself.

## 5. Hp-w and uniform BR existence

### Hp-w: plausible, but its stated rates are unproved

The hypothesis should be written in Ozuch’s actual source norm:
\[
\|\Pi_q^\perp\Phi_{g_q^D}(\bar g_p)\|_{r_D^{-2}C_\beta^\alpha}
\le \epsilon(|\zeta|)\,|\zeta_r|,
\qquad \epsilon(r)\to0.
\]
The note’s \(C_\beta^\alpha\) notation omits a load-bearing \(r_D^{-2}\) factor.

The scaling explains why this is plausible. A period-normalized EH form has physical size
\[
|\theta_{EH}|\sim a^2r^{-4},
\]
so in the core \(r\sim a\),
\[
r_D^2|\theta_{EH}|=O(1).
\]
Thus relative convergence in rescaled core geometry can yield precisely \(o(|\zeta_r|)\) in the source norm. This is not a consequence of an \(L^2\) estimate.

BR supplies the right tools:

- approximate-kernel error: Lemma 22;
- harmonic versus approximate-harmonic comparison: Corollary 23;
- cohomology-to-weighted-form norm comparison: Proposition 29.

To apply these, one must transfer the estimates to the **final CSCK metrics**, compare their forms with the **chosen Ozuch obstruction bundle**, and translate BR’s negative form weights into Ozuch’s positive tensor weights.

The final CSCK metric has only the quoted crude relative estimate
\[
O\!\left(a^{(1-\beta_{\rm BR})(\delta+2)}\right).
\]
This exponent can be small. It does not, by itself, establish the specific \(O(a^{2-\beta_{\rm Ozu}})\) rate asserted in Hp-w’s sketch. A weaker positive power may suffice, but must survive the norm conversion. Also, Definition A.4’s constant tensors belong to the **domain correction norm**; they must be handled through gauge and inverse estimates rather than treated as an unspecified source-norm component.

The needed unknown is therefore a **uniform weighted comparison of the normalized harmonic defect with the fixed reduction’s obstruction line**, valid even when \(|\zeta_r|\ll|\zeta|\).

### BR existence: fixed admissible rays are covered; whole-direction uniformity is an extension

BR Theorems B and C really do allow varying Kähler classes, including \(\zeta_r\ne0\). For \(A_1\), the combined Kronheimer wall is only the origin, so nonzero combined directions encounter no ALE wall degeneration.

However, Definition 2 also includes the order condition \(p\le\mathbf d\), and the existence of a valid family of \((1,1)\)/Kähler classes. For the explicit linear-period rays on a suitable Weyl cover these conditions can be arranged; “the wall is only zero” is not the entire hypothesis.

Pure resolution directions are covered by Theorem C with positive area on the effective exceptional curve. The negative real direction requires the Weyl-related marking/resolution choice. One fixed simultaneous-resolution chart does not contain both signs as Kähler classes. A global comparison family must be assembled with compatible charts and transition maps.

Uniformity over directions is geometrically plausible: normalized \(A_1\) ALE models are EH rotations, and BR §2.2 gives smooth ALE dependence and the \(SO(3)\) action. Nevertheless, the paper’s raywise theorem is not a verbatim multiparameter, uniform, continuous-family theorem.

Uniformity in the exterior parameter \(v\) requires **recentering at \(g_v\)**. Applying BR’s estimate relative to \(g_V\) would incorrectly require the exterior deformation to be \(O(a^2)\), excluding sequences with \(|v|\gg|\zeta|\).

Finally, BR’s pointwise closeness alone does not prove
\[
m_\zeta(p)-\zeta(p)=o(|\zeta|).
\]
Relative matching needs core rescaling, period/marking control, and the scale-adapted slice estimate.

## 6. Lemma 87.5: sound after stating the compactness and topology inputs

The conclusion can be proved without a general classification of arbitrary Ricci-flat ALE spaces.

Use noncollapsed Einstein bubble-tree compactness, smooth convergence on the regular exterior, and topology decomposition. On the fixed four-manifold, Einstein Gauss–Bonnet supplies a uniform curvature-energy bound.

- At a regular limit point, a nonflat ALE bubble would have asymptotic volume ratio one, contradicting Bishop–Gromov rigidity.
- At the node, a nonflat intermediate ALE orbifold has asymptotic volume ratio \(1/2\). An interior singular point of order \(|\Gamma'|\) would give
  \[
  \frac1{|\Gamma'|}\ge\frac12.
  \]
  Nontriviality forces order two and equality, hence a flat cone, contrary to nonflatness.

This excludes additional **nonflat** tree levels. Flat “ghost” levels can be suppressed; the literal inequality does not exclude them.

For the resulting smooth ALE bubble \(N\), Mayer–Vietoris and signature additivity give
\[
\chi(N)=2,\qquad b_2(N)=1,\qquad \tau(N)=-1.
\]
Here the exterior/orbifold signature is \(-34\), and the boundary is the rational homology sphere \(\mathbb{RP}^3\).

Since \(\eta(\mathbb{RP}^3)=0\), ALE Gauss–Bonnet and signature give, with
\[
A_\pm=\int_N|W^\pm|^2,
\]
\[
A_++A_-=12\pi^2,\qquad A_+-A_-=-12\pi^2.
\]
Hence \(A_+=0\). Orientation matching is therefore a consequence of topology, not an assumption.

The standard finite-fundamental-group result for Ricci-flat ALE manifolds gives \(d=|\pi_1(N)|<\infty\). The universal cover has asymptotic volume ratio \(d/2\le1\), so \(d\le2\). If \(d=2\), equality makes the cover Euclidean; a nontrivial finite Euclidean isometry group cannot act freely. Thus \(d=1\).

Ricci-flatness and \(W^+=0\) make \(\Lambda^+\) flat; simple connectedness supplies a global hyperkähler triple. Kronheimer then identifies \(N\) as EH.

The note’s equality-case phrase “flat \(\mathbb R^4/\pm1\)” should be replaced by this universal-cover argument.

## 7. Corollary, novelty, and final status

For the same orientation, Corollary 87.6 follows from the repaired conditional theorem. An almost-Kähler form is harmonic, self-dual, and of constant length. On a KE quintic,
\[
H_g^+=\mathbb R\omega_J\oplus\operatorname{Re}H^{2,0}.
\]
Writing it as \(a\omega_J+\operatorname{Re}\beta\), pointwise orthogonality forces \(|\beta|\) constant. A nonzero such holomorphic two-form would be nowhere zero and trivialize \(K_M\), impossible since \(c_1(K_M)^2=5\). Hence the form is \(\pm\omega_J\).

An opposite-oriented almost-Kähler form is ASD in the complex orientation. The displayed argument gives no conclusion about it. State the orientation convention explicitly or add a separate exclusion theorem.

The assertion “every \(g\in\mathcal U\) has \(D_W=0\)” must be restricted to Einstein metrics. Moreover, \(D_W\) and the organizing identity are not defined in the supplied materials, so their numerical claims cannot be verified here.

**Established:** the CSCK cohomological identities, EH magnitude/period normalization, Proposition 87.2, and the \(78+2=80\) deformation count. The bubble identification is justified with the stated standard compactness/ALE inputs.

**Conditional:** relative CSCK calibration on the full direction family, Hp-w, relative modulation matching, the exact Ozuch uniqueness graph, and therefore Theorem 87.4 and the same-oriented corollary.

**Incorrect if read literally:** raw cut-off modes being exact global kernel tensors; obtaining relative parameter matching from pointwise closeness alone; invoking uniqueness across different reductions; and treating the displayed \(H^+\) proof as orientation-independent.

The genuinely promising contribution is the **CSCK secant plus finite-dimensional degree mechanism**. The eigenvalue and Chern–Weil identities are standard, and BR already constructs the comparison metrics raywise. A new endpoint-rigidity theorem would result from proving the uniform, gauge-compatible weighted and modulation comparison above—not from the symbolic calibration alone.