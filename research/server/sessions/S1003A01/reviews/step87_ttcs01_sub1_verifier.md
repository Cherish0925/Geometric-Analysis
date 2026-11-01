# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md",
    "Sessions/S1003A01/workspace/data/step87/csck_calibration.json",
    "Sessions/S1003A01/workspace/scripts/step87_csck_calibration.py",
    "Knowledge/objects/papers/Smoothing-singular-extremal-Kähler-surfaces-and-minimal-Lagrangians--76bcf086d1fb--80cf6934cc4e/object.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the mathematics of the Step-87 note (Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md) on Einstein rigidity near a negative Kähler–Einstein orbifold with one A1 node (generic nodal quintic surface). Research context: closed negative almost-Kähler Einstein (Goldberg) problem and Einstein metrics near KE orbifold endpoints; earlier work reduced the question to a scale-uniform C^1 estimate of Ozuch's normal obstruction Lambda_I. The note claims to replace that derivative estimate by (i) an exact eigenvalue statement (Prop 87.2, from Nagy eq. (17): harmonic primitive (1,1) forms give Hermitian TT eigentensors of the Einstein operator with eigenvalue -2E), (ii) an exact secant along the Biquard–Rollin CSCK family varying the real Kronheimer period zeta_r: Ric-Eg=rho_0(.,J.) with rho_0 harmonic ASD in class 2 pi c1 - E[omega], giving Lambda_I = E zeta_r (1+o(1)) and P=-2(2pi c1-E[omega])^2 (§3, Lemma 87.3), and (iii) a C^0 degree argument (Theorem 87.4) showing the corrected CSCK family fills Ozuch's reduced Einstein-modulo-obstruction family, so every nearby Einstein metric is KE; plus Lemma 87.5 (bubble is orientation-matched EH, no trees) and Cor 87.6 (no strict AKE nearby via the length obstruction). Please check carefully and write a direct scientific memo: (1) correctness of the cohomological identities and normalizations (|Ric0|^2=2|rho0|^2, period int_delta rho_0 = -E zeta_r, theta^2 -> -2, EH L2 form normalization ||theta||^2=2, A=E i.e. c0=1) — compare with the JSON data; (2) whether Prop 87.2 is correct including the claim that no small nonzero TT eigenvalue arises from the degeneration (are o_J, o_K really exact kernel at KE smoothings? is the count 78+2 correct?); (3) the logic of Theorem 87.4: is the EmO correction estimate ||k|| <= C|zeta_r| o(1) justified given Ozuch-type uniform inverses, is uniqueness used correctly, does the degree argument on shells really give surjectivity onto the reduced family (and is the reduced family a graph over parameters so that 'hitting the parameter' identifies the metric), and is anything circular; (4) whether the weighted hypothesis (Hp-w) is plausible with the stated rates, and whether CSCK metrics in classes with zeta_r != 0 on smoothings (and resolutions, Theorem C) really exist uniformly over all directions on S^2 under Biquard–Rollin non-degeneracy for A1; (5) Lemma 87.5's proof (Bishop–Gromov exclusion of trees, Gauss–Bonnet/signature comparison with EH, pi_1 argument); (6) any hidden gap that would invalidate Corollary 87.6, and what is genuinely new versus standard. Separate proved, conditional, and false statements; propose repairs where something fails.

## Output

# Scientific verification memo: Step 87

## Overall assessment

The exact Kähler and cohomological calculations are correct with the stated form and period conventions. In particular:

- Proposition 87.2 follows from Nagy’s equation (17).
- The identities
  \[
  P=-2(2\pi c_1-E[\omega])^2,\qquad
  \int_\delta\rho_0=-E\zeta_r
  \]
  are correct.
- With \(\int_\delta\theta_{EH}=-2\), \(\|\theta_{EH}\|_{L^2}^2=2\), and
  \(\hat o_I=(\theta_{EH}\circ I)/2\), the leading coefficient is
  \[
  \Lambda_I=E\zeta_r(1+o(1)).
  \]
  Thus \(c_0=1\) in the period coordinate \(\zeta_r=\int_\delta\omega\).

The rigidity theorem is still conditional in a substantial way. Its logical structure is sound once the four inputs O1, BR-u, M, and Hp-w are supplied in their required uniform forms. The two most substantial unresolved pieces are:

1. a weighted, parameter-uniform concentration theorem strong enough to imply Hp-w;
2. relative parameter matching
   \[
   \zeta_{\mathrm{Ozuch}}=\zeta_{\mathrm{period}}+o(|\zeta|),
   \]
   which does not follow merely from the pointwise BR metric estimate quoted in the note.

Lemma 87.5 is consistent with the standard bubble-tree, ALE topology, and APS formulas, though several standard intermediate facts should be stated explicitly. Corollary 87.6 is correct when the almost-Kähler orientation agrees with the quintic complex orientation; without that orientation convention, its displayed proof does not treat an opposite-oriented almost-Kähler form.

---

## 1. Cohomological identities and normalization

### 1.1 CSCK defect

For a Kähler surface with scalar curvature \(s=4E\), let
\[
\rho_0=\rho-E\omega.
\]
Since \([\rho]=2\pi c_1\),
\[
[\rho_0]=2\pi c_1-E[\omega].
\]
The constant scalar curvature condition gives \(\Lambda_\omega\rho=2E\), while
\(\Lambda_\omega(E\omega)=2E\). Hence \(\rho_0\) is primitive. It is closed, primitive, and of type \((1,1)\), so in complex orientation it is ASD and harmonic.

With
\[
\operatorname{Ric}^{\circ}(X,Y)=\rho_0(X,JY),
\]
the pointwise norm relation is
\[
|\operatorname{Ric}^{\circ}|^2=2|\rho_0|^2.
\]
This agrees with the matrix calculation in `csck_calibration.json`. Therefore
\[
P:=\int_M|\operatorname{Ric}^{\circ}|^2
   =2\|\rho_0\|_{L^2}^2
   =-2\int_M\rho_0\wedge\rho_0
   =-2(2\pi c_1-E[\omega])^2.
\]

This part of §3.1 is exact.

### 1.2 The scaling factor \(\lambda\)

Write
\[
[\omega]=\lambda\left(\frac{2\pi}{E}c_1+\varepsilon\theta\right),
\qquad c_1\cdot\theta=0.
\]
For a Kähler surface,
\[
\bar s=\frac{8\pi\,c_1\cdot[\omega]}{[\omega]^2}.
\]
Imposing \(\bar s=4E\) gives
\[
\lambda=
\frac{4\pi^2c_1^2}
     {4\pi^2c_1^2+E^2\varepsilon^2\theta^2},
\]
exactly as in the JSON file.

Since
\[
\zeta_r=[\omega]\cdot\delta
       =\lambda\varepsilon\,\theta^2,
\]
and \(c_1\cdot\delta=0\),
\[
\int_\delta\rho_0
=(2\pi c_1-E[\omega])\cdot\delta
=-E\zeta_r.
\]
The JSON expression
\[
\frac{P}{E^2\zeta_r^2}
=-\frac{2}{\theta^2}
-\frac{E^2\varepsilon^2}{2\pi^2c_1^2}
\]
is also correct.

For the vanishing class,
\[
\delta^2=-2,\qquad
\delta=\delta^{1,1}+\delta^{2,0}+\delta^{0,2}.
\]
The real \((2,0)+(0,2)\) summand has positive square, so
\[
\theta^2=(\delta^{1,1})^2\longrightarrow -2
\]
as the complex period tends to zero. Consequently
\[
P=E^2\zeta_r^2(1+o(1)).
\]

### 1.3 Eguchi–Hanson form

For
\[
\theta_{EH}=d(cr^{-2}\sigma_3),
\]
the script correctly obtains the frame coefficients
\[
-\frac{4c}{r^4}(e^{03}+e^{12})
\]
in its chosen frame orientation, and
\[
\int_S\theta_{EH}=-\frac{4\pi c}{a^2}.
\]
Choosing \(c=a^2/(2\pi)\) gives
\[
\int_S\theta_{EH}=-2,\qquad
\|\theta_{EH}\|_{L^2}^2=2,\qquad
|\theta_{EH}|=\frac{2\sqrt2\,a^2}{\pi r^4}.
\]

One orientation convention should be made explicit: the class with bolt period \(-2\) represents \(PD(S)\) and satisfies
\[
\int\theta_{EH}\wedge\theta_{EH}=S^2=-2.
\]
Thus it is ASD in the complex orientation. The script verifies the period and norm, but it does not by itself verify this wedge-product sign; the sign follows after fixing the complex orientation opposite to the frame orientation in which the displayed coefficient is self-dual.

### 1.4 Calibration coefficient

Let
\[
o_I=\theta_{EH}\circ I.
\]
The pointwise Kähler algebra gives
\[
\|o_I\|_{L^2}^2=2\|\theta_{EH}\|_{L^2}^2=4,
\qquad
\hat o_I=\frac{o_I}{2}.
\]
Because
\[
\int_\delta\rho_0=-E\zeta_r
\]
and \(\int_\delta\theta_{EH}=-2\), the concentrating part is
\[
\rho_0=\frac{E\zeta_r}{2}\theta_{EH}+o_{L^2}(|\zeta_r|).
\]
Hence
\[
\operatorname{Ric}^{\circ}
=\frac{E\zeta_r}{2}o_I+o_{L^2}(|\zeta_r|),
\]
and therefore
\[
\Lambda_I
=\langle\operatorname{Ric}^{\circ},\hat o_I\rangle
=E\zeta_r(1+o(1)).
\]

Thus
\[
A=E=\frac{s}{4},\qquad c_0=1
\]
in the coordinate \(\zeta_r=\int_\delta\omega\).

This does not yet identify \(c_0=1\) in Ozuch’s raw metric parameter. Ozuch’s \(\zeta\) convention may differ from the period by a fixed factor. A direct conversion between the Kronheimer metric coordinate and \(\int_\delta\omega\) is needed before equating the two normalizations.

### 1.5 Status of Lemma 87.3

The \(L^2\) concentration mechanism is correct, but the lemma is not fully proved as written. The missing analytic object is a uniformly controlled representative of the exterior class \(y\).

A clean formulation is to use linearity of harmonic projection:
\[
\mathcal H(a\delta+y)-a\theta_{EH}^{\rm cut}
=a\bigl(\mathcal H(\delta)-\theta_{EH}^{\rm cut}\bigr)+\mathcal H(y).
\]
For the pure \(\delta\)-class, the minimizing property and
\[
\|\theta_{EH}^{\rm cut}\|^2
=2+O((a/R)^4)
\]
give
\[
\|\mathcal H(\delta)-\theta_{EH}^{\rm cut}\|
=O((a/R)^2).
\]
One still needs a uniform estimate
\[
\|\mathcal H(y)\|_{L^2}\le C\|y\|_{\mathrm{ext}}
\]
for exterior classes under degeneration. This is standard gluing Hodge theory but is not supplied by the topological inequality alone.

---

## 2. Proposition 87.2 and the low spectrum

### 2.1 Exact eigenvalue statement

Nagy’s equation (17) states that for a Hermitian symmetric tensor \(H\), with associated real \((1,1)\)-form
\[
A=g(HJ\cdot,\cdot),
\]
one has
\[
g^{-1}(\Delta_d-2E)A=(\Delta_EH)\circ J.
\]
For \(H_\theta=\theta\circ J\), the associated form is \(-\theta\), up to the sign convention in the tensor-form identification. If \(\theta\) is harmonic, then
\[
\Delta_EH_\theta=-2E\,H_\theta.
\]

Primitivity gives \(\operatorname{tr}H_\theta=0\), and coclosedness gives
\(\delta H_\theta=0\). Thus \(H_\theta\) is TT.

For any Hermitian TT tensor,
\[
\langle\Delta_EH,H\rangle
=\langle(\Delta_d-2E)A,A\rangle
\ge -2E\|A\|^2.
\]
Equality holds exactly when \(A\) is harmonic. Therefore Proposition 87.2 is correct.

For a smooth quintic,
\[
\dim_{\mathbb R}\mathcal H^{1,1}_{\mathrm{prim}}
=h^{1,1}-1=44.
\]
So the multiplicity statement is correct.

### 2.2 The \(o_J,o_K\) modes

The raw cut-off tensors \(o_J,o_K\) are not themselves exact global kernel elements. What is correct is:

- the two local EH modes corresponding to the complex period extend, after global corrections, to two exact anti-Hermitian Kodaira–Spencer kernel elements;
- the 78 real locally trivial orbifold directions extend to 78 further kernel elements;
- together these form the 80-dimensional smooth-quintic Einstein kernel.

The count is
\[
78+2=80=2h^1(\Theta_M).
\]
Thus the dimension count is correct, but the wording should distinguish the raw cut-off modes from their corrected global representatives.

### 2.3 Absence of additional eigenvalues tending to zero

This conclusion does not follow from Proposition 87.2 alone. It requires a spectral convergence theorem for the tensor Einstein operator on an orbifold–ALE degeneration.

The expected decomposition is:

- 78 exterior anti-Hermitian zero modes;
- 3 EH \(L^2\) zero modes;
- after gluing, 80 become exact zero modes;
- the remaining local Hermitian mode becomes the exact eigenmode with eigenvalue \(-2E\).

If a spectral gluing theorem shows that every eigenvector with eigenvalue tending to zero comes from the exterior kernel or the EH \(L^2\) kernel, the dimension count proves the stated conclusion. That theorem is not quoted precisely in Step 87. The sentence calling this “standard spectral convergence” should be attached to a specific theorem or retained as an additional input.

---

## 3. Theorem 87.4

### 3.1 EmO correction estimate

Let \(\Pi^\perp\) denote projection away from the approximate obstruction space. The complementary equation has the form
\[
\Pi^\perp\Phi(g^{\rm CSCK}+k)=0.
\]
If O1 supplies a uniform inverse and Hp-w supplies
\[
\|\Pi^\perp\Phi(g^{\rm CSCK})\|_Y
\le \epsilon(|\zeta|)\,|\zeta_r|,
\qquad \epsilon(|\zeta|)\to0,
\]
then the contraction argument gives
\[
\|k\|_X\le C\epsilon(|\zeta|)|\zeta_r|.
\]
Thus the estimate in step (2) of the theorem is justified from O1 plus Hp-w. It is not a consequence of the \(L^2\) concentration lemma by itself.

The obstruction then changes by
\[
\Lambda_I(g^{\rm CSCK}+k)-\Lambda_I(g^{\rm CSCK})
=O(\|k\|\|L^*\hat o_I\|+\|k\|^2),
\]
so a uniform bound for \(L^*\hat o_I\) suffices to retain
\[
\Lambda_I(\Xi(p))=E\zeta_r(1+o(1)).
\]

At \(\zeta_r=0\), the CSCK metric is already KE and solves the full Einstein equation. Uniqueness in the complementary slice then gives \(k=0\).

### 3.2 Degree argument

The shell argument is valid on a marked linear parameter space if:

1. \(\pi\circ\Xi\) has a continuous lift to \((v,\zeta)\in\mathbb R^{78}\times(\mathbb R^3\setminus\{0\})\);
2. the matching estimate is relative in \(\zeta\);
3. O1 makes the EmO family a unique graph over these parameters.

On the outer sphere \(|\zeta|=2|\zeta^*|\), the distance to \(\zeta^*\) is at least
\(|\zeta|/2\), so \(\eta<1/2\) keeps the straight-line homotopy away from the target. The inner sphere and the \(v\)-sphere are handled similarly. Thus the degree is one.

The quotient \(\zeta\sim-\zeta\) needs a marked lift. A cleaner local version uses a ball
\[
|\zeta-\zeta^*|<r|\zeta^*|,\qquad r<1,
\]
with
\[
\eta(1+r)<r.
\]
This ball avoids both \(0\) and the opposite marked point, so the Weyl quotient is locally a genuine chart.

“Hitting the parameter” identifies the metric only if O1 contains uniqueness of the EmO solution for each parameter. Mere representation of every Einstein metric is insufficient. Under the stated uniqueness graph, the inference
\[
\pi(\Xi(p))=(v^*,\zeta^*)\quad\Longrightarrow\quad
\Xi(p)=g_{v^*,\zeta^*}
\]
is correct.

There is no circular dependence in the argument: Ozuch’s reduction describes all nearby metrics solving the complementary equation, while the CSCK calibration determines the remaining finite-dimensional equation.

### 3.3 Matching is the central unresolved point

The estimate
\[
\zeta_{\mathrm{Ozuch}}
=\zeta_{\mathrm{natural}}+o(|\zeta|)
\]
is stronger than ordinary metric closeness. The BR estimate
\[
\|\phi_t\|_{C^{4,\alpha}_{\delta+2}}
\le C\varepsilon^{2-\beta(\delta+2)}
\]
does not by itself imply relative control of the modulation parameter, since that norm can be much larger than the period scale \(|\zeta|\sim\varepsilon^2\).

The relative estimate should instead come from:

- exact complex and Kähler periods;
- a marked modulation map for the EH parameters;
- orthogonality to the three EH Jacobi fields;
- a uniform slice estimate converting period agreement into parameter agreement.

Until this is written, M remains an essential independent hypothesis.

---

## 4. Hp-w and Biquard–Rollin uniformity

### 4.1 Hp-w

Hp-w is plausible but not established by the displayed rate heuristic. A suitable precise object is
\[
u_p:=\frac{\rho_0(\,\cdot\,,J\,\cdot\,)}{E\zeta_r},
\qquad \zeta_r\ne0,
\]
extended at \(\zeta_r=0\) by differentiation in the real-period direction. The required theorem is a parameter-uniform weighted estimate
\[
u_p=\hat o_I+r_p,\qquad
\|\Pi^\perp r_p\|_{C^\alpha_\beta}=o(1)
\]
on the real blow-up of the full \(A_1\) parameter space.

BR’s weighted Hodge estimates, especially the approximate-kernel discussion and Propositions 21–30, provide the appropriate analytic framework. However, the note’s rate
\[
O(a^{2-\beta})
\]
is not derived in Ozuch’s exact source norm, and the constant \(H_k\) components from Definition A.4 are not treated. The observation in §7 correctly prevents a spurious logarithm, but it does not yet produce the full Hp-w estimate.

### 4.2 Uniform CSCK existence

For \(A_1\), the Kronheimer wall is only the origin. Therefore every nonzero unit direction in
\[
(\zeta_r,\Re\zeta_c,\Im\zeta_c)\in S^2
\]
is nondegenerate in BR’s sense. The local ALE models vary smoothly over this compact sphere and, for \(A_1\), are related by the hyperkähler \(SO(3)\)-action. This makes uniform constants highly plausible.

BR Theorem C includes the pure resolution direction \(\zeta_c=0\), while Theorem B handles smoothing directions. For a fixed marking, only the Kähler-positive half of the pure resolution line is admissible; the other half is obtained after the Weyl reflection. Thus the natural parameter space is the marked double cover or its \(\mathbb Z_2\) quotient.

What is not supplied verbatim by BR is a jointly continuous multiparameter family over all small \((v,\zeta)\), with constants uniform across the sphere and across \(\zeta_c=0\). A parameter-dependent fixed-point argument over a compact family of tangent gravitons should give it, but this is additional analysis.

---

## 5. Lemma 87.5

The bubble identification is mathematically consistent with the standard orbifold compactness and bubble-tree package.

1. A bubble at a smooth point has trivial group at infinity. Its asymptotic volume ratio is one, so Bishop–Gromov rigidity makes it flat.

2. A first bubble at the node has group \(\mathbb Z_2\) at infinity. If it had an orbifold point with local group \(\Gamma'\), Bishop–Gromov gives
   \[
   \frac1{|\Gamma'|}\ge\frac12.
   \]
   A nontrivial local group must therefore be \(\mathbb Z_2\), giving equality and hence a flat cone. This excludes interior orbifold points and therefore excludes further tree levels.

3. Euler additivity gives
   \[
   \chi(N)=\chi(M)-\chi_{\rm top}(V)+1=55-54+1=2.
   \]
   Standard ALE topology gives finite \(\pi_1\), \(b_1=b_3=0\), hence \(b_2=1\). Novikov additivity gives \(\tau(N)=-1\).

4. \(N\) and orientation-matched EH have the same \(\chi\), \(\tau\), group at infinity, and APS end correction. The ALE Gauss–Bonnet and signature formulas therefore give the same values of
   \[
   \int|W^+|^2,\qquad \int|W^-|^2.
   \]
   Since the matching EH orientation has \(W^+=0\), one obtains \(W^+_N=0\).

5. Ricci-flatness and \(W^+=0\) make the connection on \(\Lambda^+\) flat. If \(d=|\pi_1(N)|\), the universal cover has asymptotic volume ratio \(d/2\le1\). If \(d=2\), equality forces the universal cover to be Euclidean. No nontrivial finite deck group acts freely on \(\mathbb R^4\), so \(d=1\).

6. A simply connected Ricci-flat ALE four-manifold with flat \(\Lambda^+\) is hyperkähler. Kronheimer’s classification with group \(\mathbb Z_2\) at infinity gives Eguchi–Hanson.

For a complete written proof, the finite fundamental group of an ALE space, the ALE homology facts, and the precise bubble-tree theorem should be cited. The geometric conclusion itself is correct.

---

## 6. Corollary 87.6

If the almost-Kähler orientation is the same as the quintic complex orientation, the argument is correct. The almost-Kähler form is then a self-dual harmonic form of constant norm. For a KE quintic,
\[
H_g^+=\mathbb R\omega_{J'}\oplus\operatorname{Re}H^{2,0}_{J'}.
\]
Writing
\[
\omega=a\omega_{J'}+\beta,
\]
constant length forces \(|\beta|\) to be constant. A nonzero holomorphic \(2\)-form of constant positive norm is nowhere zero and trivializes \(K\), impossible for a quintic with ample canonical bundle. Hence \(\beta=0\), and the normalization of an almost-Kähler form gives \(\omega=\pm\omega_{J'}\).

If the almost-Kähler form induces the opposite orientation, it lies in \(H_g^-\), not in the displayed \(H_g^+\). The proof then gives no conclusion. Thus either the session convention must explicitly fix the quintic orientation, or an additional argument for constant-length ASD harmonic forms is needed.

The sentence “for every \(g\in\mathcal U\), \(D_W(g)=0\)” should read “for every Einstein \(g\in\mathcal U\)” unless \(\mathcal U\) denotes only the Einstein moduli set.

---

## Status summary

### Established by the supplied calculations and sources

- Quintic deformation and topology counts.
- The CSCK cohomological formulas.
- The norm factor \(|\operatorname{Ric}^{\circ}|^2=2|\rho_0|^2\).
- The EH period and \(L^2\)-norm normalization.
- Proposition 87.2.
- The coefficient \(A=E\) in the period coordinate.
- The bubble identification, using standard ALE and bubble-tree inputs.

### Conditional but logically coherent

- Uniform BR family over all \(A_1\) directions.
- Weighted concentration Hp-w.
- Relative matching M.
- The Ozuch uniqueness graph O1 in the exact form used.
- Theorem 87.4 and the resulting local Einstein rigidity.

### Requiring reformulation

- \(o_J,o_K\) are not raw exact kernel tensors; their globally corrected extensions are.
- “No additional eigenvalues tending to zero” needs a precise spectral gluing theorem.
- Lemma 87.3 does not yet prove the weighted estimate needed later.
- \(c_0=1\) is established for \(\zeta_r=\int_\delta\omega\), not yet for Ozuch’s raw coordinate.
- Corollary 87.6 needs the same-orientation convention.
- The literal statement about \(D_W\) should be restricted to Einstein metrics.

The most substantive new element is the synthesis of the exact CSCK secant with a degree argument on the reduced EmO family. The eigenvalue identity and the Chern–Weil formulas are standard consequences of Kähler geometry; the prospective rigidity theorem becomes new once Hp-w and relative parameter matching are proved uniformly.