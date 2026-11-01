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
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step61_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step61_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Critically verify the Step-60 note after Spirit #72. Read the actual note, exact pinching data/script, Step-59 zero-charge note, and the primary Apostolov–Drăghici survey and Apostolov–Drăghici–Moroianu splitting paper. Determine precisely which statements remain valid and which require correction: (i) Weitzenböck/Rayleigh localization and the distinction between λ_min=s/6 and norm saturation at a torsion zero, including the exact identity |W+|^2-s^2/24=|eta|^2+|W3+|^2; (ii) same-orientation Kähler metric lemma, especially the claim that a holomorphic 2-form of constant norm is parallel; (iii) opposite-orientation correspondence—whether closed complementary forms imply integrable plane fields and minimal complex-curve leaves, but not holomorphic subbundles or product splitting; (iv) the rescaled Kähler metrics with constant Ricci eigenvalues and the negative compact alternative; (v) fixed-manifold conclusions for real/complex hyperbolic quotients using LeBrun/BCG. Give corrected theorem statements and direct proof guidance, not procedural commentary.

## Integrated Scientific Memo

# Verification memo: corrected Step 60

The Weitzenböck identity, closed-manifold pinching exclusion, exact Bianchi–VIII pinching, and same-orientation Kähler rigidity are valid. The essential corrections are:

- a torsion zero fixes a **Rayleigh quotient**, not necessarily the least eigenvalue;
- even when \(\Omega\) is an eigenform at that zero, it need not be a least eigenform;
- complementary closed forms yield smooth integrable plane fields with minimal complex-curve leaves, **not holomorphic tangent subbundles**;
- product splitting in Proposition 60.4 must mean splitting **along those particular plane fields**;
- the compact negative opposite-orientation problem is precisely the unresolved negative alternative in the Apostolov–Drăghici–Moroianu paper;
- the fixed-manifold conclusions follow from the BCG/LeBrun rigidity statements quoted in Step 60, but those primary rigidity papers are not present here.

## 1. Weyl localization and the exact saturation identity

Use the note’s form and curvature-operator norms:
\[
|\Omega|^2=2,\qquad u=\Omega/\sqrt2,\qquad q=|\nabla\Omega|^2.
\]
The self-dual Weitzenböck formula gives
\[
0=\nabla^*\nabla\Omega-2W^+\Omega+\frac s3\Omega.
\]
Since \(|\Omega|\) is constant,
\[
q=2\langle W^+\Omega,\Omega\rangle-\frac{2s}{3},
\qquad
r:=\langle W^+u,u\rangle=\frac s6+\frac q4.
\]
Thus
\[
q\ge4\left(\lambda_{\min}(W^+)-\frac s6\right).
\]
These formulas do not require Einstein.

### Exact orthogonal decomposition

Let \(H=u^\perp\subset\Lambda^+\). Write
\[
W^+=
\begin{pmatrix}
r&v^*\\
v&-\frac r2\operatorname{Id}_H+B
\end{pmatrix},
\qquad \operatorname{tr}_H B=0.
\]
In the Step-59 normalization,
\[
\eta=W^+\Omega-r\Omega=\sqrt2\,v,\qquad W_3^+=B.
\]
Consequently
\[
|W^+|^2=\frac32r^2+|\eta|^2+|W_3^+|^2,
\]
and hence
\[
\boxed{
|W^+|^2-\frac{s^2}{24}
=
|\eta|^2+|W_3^+|^2+\frac{sq}{8}+\frac{3q^2}{32}.
}
\tag{1}
\]
In particular, **at a torsion zero**,
\[
\boxed{
|W^+|^2-\frac{s^2}{24}=|\eta|^2+|W_3^+|^2.
}
\tag{2}
\]
The identity requested in the task is therefore a zero-set identity, not an identity on the entire almost-Kähler manifold.

### Corrected localization theorem

Let \((M^4,g,\Omega)\) be closed almost-Kähler Einstein with \(s<0\), oriented by \(\Omega\). Then
\[
Z=\{\nabla\Omega=0\}\ne\varnothing,
\]
and
\[
Z\subset
\left\{\lambda_{\min}(W^+)\le s/6\right\}
\cap
\left\{|W^+|^2\ge s^2/24\right\}.
\]
At every \(z\in Z\),
\[
\langle W^+u,u\rangle=s/6.
\]

The three relevant conditions must remain separate:

1. **Eigenform condition**
   \[
   \eta(z)=0
   \iff W^+\Omega=(s/6)\Omega.
   \]

2. **Least-eigenvalue boundary**
   \[
   \lambda_{\min}(W^+_z)=s/6
   \iff
   \eta(z)=0
   \quad\text{and}\quad
   \operatorname{spec}(W^+|_H)\subset[s/6,\infty).
   \]
   Equivalently, because \(s<0\),
   \[
   \eta(z)=0,\qquad
   \|W_3^+(z)\|_{\mathrm{op}}\le -s/4.
   \]
   Thus the assertion in one supplied analysis that
   \(\lambda_{\min}=s/6\iff\eta=0\) is false.

3. **Norm saturation**
   \[
   |W^+_z|^2=s^2/24
   \iff \eta(z)=W_3^+(z)=0.
   \]
   This gives the full Kähler-type operator
   \[
   W^+_z=\operatorname{diag}(s/6,-s/12,-s/12)
   \]
   in an orthonormal basis beginning with \(u\).

For example, with \(s=-6\), the algebraic operator
\[
W^+=\operatorname{diag}(-1,-2,3),\qquad u=e_1,
\]
has the required Rayleigh quotient and \(\eta=0\), but
\(\lambda_{\min}=-2<s/6\). The operator
\(\operatorname{diag}(-1,-1,2)\) has \(\lambda_{\min}=s/6\), but its norm is strictly greater than \(s^2/24\). These are algebraic distinctions, not constructed Einstein–almost-Kähler germs.

The Step-59 assertion for zeros of order at least two,
\(\eta=W_3^+=0\), places those zeros in the **norm-saturation stratum**. Neither the Rayleigh argument nor topology establishes this for first-order zeros.

### Charge and pinching exclusion

The survey explicitly identifies the torsion bundle and its top Chern number:
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\qquad
\langle c_2(E),[M]\rangle=5\chi+6\tau.
\]
For a closed Einstein metric with \(s\ne0\),
\[
\chi>0,\qquad
2\chi+3\tau
=\frac1{4\pi^2}\int_M\left(2|W^+|^2+\frac{s^2}{24}\right)>0,
\]
so
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
Thus \(T=\nabla\Omega\) has a zero. Its supported Euler class over \(Z\) also gives a relative class supported in
\(\Sigma_-=\{\lambda_{\min}\le s/6\}\). This does **not** assign positive multiplicity to every zero.

Both exclusions in Corollary 60.2 are correct:
\[
\lambda_{\min}(W^+)>s/6\ \text{everywhere},
\quad\text{or}\quad
|W^+|^2<s^2/24\ \text{everywhere}
\]
precludes any compatible almost-Kähler structure on a closed negative Einstein four-manifold. The norm condition implies the eigenvalue condition by the trace-free \(3\times3\) eigenvalue estimate.

## 2. Exact pinching control: conclusions valid, root labels incorrect

The supplied script and JSON agree with the rational formulas in Steps 59–60. For \(1/3<p<1\), all three \(w_i+2\) are positive.

Direct sign proofs remove the misleading root-count labels:

- \(3p^3+3p^2-3p+1\) is increasing for \(p>1/3\) and equals \(4/9\) at \(1/3\).
- \(1+3p+3p^2-3p^3\) is positive there; its derivative is
  \(3(1-p)(1+3p)>0\).
- For \(u=p^2\),
  \[
  G(u)=21u^3-3u^2+15u-1
  \]
  satisfies \(G'(u)=63u^2-6u+15>0\) and \(G(1/9)=160/243>0\).

Likewise,
\[
|W^+|^2-6
=-\frac{18(1-p^2)^3f(p^2)}{(3p^2+1)^6},
\quad
f(u)=189u^3-207u^2+87u-5.
\]
Here
\[
f'(u)=567u^2-414u+87>0,\qquad f(1/9)=64/27,
\]
so the norm difference is strictly negative.

The JSON entries reporting one root “in \((1/3,1)\)” for \(w_2+2\) and the pinching numerator count the endpoint \(p=1\). There are **no open-interval roots**. Relabel those entries as closed-interval counts, or remove endpoint factors before counting. The script’s comment that it records where norm pinching “fails” is also inaccurate: norm pinching holds throughout the branch, including the smooth bolt.

Thus, accepting the geometric completion established in Step 59,
\[
\lambda_{\min}(W^+)>-2,\qquad |W^+|^2<6
\]
at every finite point, including the bolt, while
\[
\operatorname{spec}(W^+)\longrightarrow(1,-2,1),
\qquad q\longrightarrow0
\]
at the infinite end. At the bolt,
\[
q=32/3,\qquad \eta=W_3^+=0,\qquad |W^+|^2=2/3.
\]
Equation (1) checks this exactly:
\[
2/3-6=-\frac32(32/3)+\frac3{32}(32/3)^2=-16/3.
\]

The example demonstrates sharpness of the **closed-versus-complete distinction** and approach to the pinching boundary. It does not establish first-order zero rigidity or classify all boundary cases.

## 3. Same-orientation Kähler lemma: valid, including constant norm implies parallel

**Correct theorem.** On a connected compact Kähler surface \((M,g,I,\omega_I)\), every compatible almost-Kähler form inducing the complex orientation is parallel. If \(g\) is not Ricci-flat, it equals \(\pm\omega_I\).

The proof in Step 60 is valid, with the following precise interpretation. Kähler Hodge decomposition gives
\[
\Omega=f\omega_I+\operatorname{Re}\theta,
\qquad \theta\in H^0(M,K_I).
\]
The harmonic \((1,1)\)-component is self-dual, hence pointwise proportional to \(\omega_I\). Its closedness implies
\[
df\wedge\omega_I=0,
\]
so \(f\) is constant. The constant norm of \(\Omega\) then makes \(|\theta|\) constant.

If that constant is positive, \(\theta\) is a nowhere-vanishing holomorphic frame of the **line bundle** \(K_I\). In this frame its Chern connection is
\[
D\theta=\partial\log|\theta|^2\otimes\theta.
\]
Thus \(D\theta=0\). For a Kähler metric, this is the Levi-Civita-induced connection on \(K_I\), so \(\theta\) is parallel. Its parallel trivialization forces the canonical-bundle curvature, hence the Ricci form, to vanish. If \(\theta=0\), normalization gives \(f=\pm1\).

This is a line-bundle argument; constant norm of a holomorphic section of an arbitrary higher-rank bundle would not suffice.

The survey, §6, proof of Corollary 6, explicitly invokes Apostolov–Drăghici, *Hermitian conformal classes and almost Kähler structures on 4-manifolds*, [8, Th. 1], for this same-metric, same-orientation rigidity. Replace “likely classical” by that attribution.

The subsequent deformation paragraph in Step 60 is **not established by the supplied sources**. The lemma proves rigidity at a fixed metric, not the stated direct-sum linearization or the asserted cancellation of second-order cross terms. Those claims need a separate gauge-fixed linearization and second-order compatibility calculation.

## 4. Opposite orientation: smooth complex-curve foliations, not holomorphic subbundles

Let \(J\) be orthogonal and oppositely oriented to the Kähler structure \(I\). Then \(I,J\) commute, and
\[
P=-IJ,\qquad P^2=1
\]
is symmetric, with orthogonal \(I\)-invariant rank-two eigendistributions \(D_\pm\). Let
\[
\alpha=\omega_I|_{D_+},\qquad \beta=\omega_I|_{D_-}.
\]
Then
\[
\omega_I=\alpha+\beta,\qquad \Omega_J=\alpha-\beta.
\]
If \(J\) is almost-Kähler, \(\alpha,\beta\) are closed. Their kernels are integrable: for a closed constant-rank form \(\gamma\) and \(X,Y\in\ker\gamma\),
\[
\iota_{[X,Y]}\gamma=0.
\]
Thus \(D_\pm\) are Frobenius-integrable. Their leaves have \(I\)-invariant tangent spaces, so each leaf is a complex curve and is calibrated by \(\omega_I\), hence minimal.

Conversely, suppose \(D_\pm\) are orthogonal, complementary, \(I\)-invariant and integrable. For the characteristic area form \(\alpha\), the only potentially nonzero components of \(d\alpha\) are:

- two \(D_+\) arguments and one \(D_-\) argument: the mean-curvature term of \(D_+\);
- one \(D_+\) argument and two \(D_-\) arguments: the integrability obstruction of \(D_-\).

Both vanish. Hence \(d\alpha=d\beta=0\), giving an opposite almost-Kähler \(J\).

**Corrected Proposition 60.4**
\[
\boxed{
\begin{gathered}
\text{Opposite-orientation compatible almost-Kähler structures}\\
\longleftrightarrow
\text{ordered orthogonal splittings into complementary}\\
\text{\(I\)-invariant, Frobenius-integrable real plane fields.}
\end{gathered}}
\]
Their leaves are minimal complex curves. Furthermore,
\[
J\text{ Kähler}
\iff D_\pm\text{ parallel}
\iff D_\pm\text{ both totally geodesic}
\iff g\text{ locally splits with }D_\pm\text{ as its factors}.
\tag{3}
\]

The last qualifier is necessary. Merely knowing that \(g\) admits *some* local product decomposition does not identify an arbitrary \(J\) with its product complex structures. In particular, the survey records the local strict almost-Kähler question for the product Einstein metric on \(\mathbb CH^1\times\mathbb CH^1\) as unresolved there.

For the second fundamental forms of the complex-curve leaves, the correct relation is
\[
B(IX,Y)=I B(X,Y)=B(X,IY),
\qquad B(IX,IY)=-B(X,Y).
\]
They are trace-free but can be nonzero. The note’s unqualified description as “complex-antilinear” should be replaced by these identities.

### Why holomorphic foliation theory does not yet apply

An \(I\)-invariant smooth involutive plane field need not define a holomorphic line subbundle of \(T^{1,0}M\). Closedness of its characteristic \((1,1)\)-form is weaker than holomorphic dependence of its tangent line in transverse directions.

The survey’s Proposition 5 supplies an explicit local counterexample to automatic product splitting:
\[
g=g_\Sigma+w\,dz^2+w^{-1}(dt+v\,dz)^2,\qquad h=w+iv
\]
with \(h\) nonconstant holomorphic. It has a Kähler structure \(I\) and a commuting strict almost-Kähler structure of the opposite orientation. Hence the complementary forms are closed and the leaves are minimal complex curves, but the splitting is not parallel.

If both orthogonal distributions were holomorphic subbundles, their orthogonal holomorphic splitting would be preserved by the Kähler Chern connection, yielding a parallel splitting. Thus Baum–Bott/Brunella methods require an additional holomorphicity theorem; it cannot be assumed from Proposition 60.4.

The cohomological statement is valid:
\[
[\alpha]^2=[\beta]^2=0,\qquad
[\alpha]\cdot[\beta]=\operatorname{Vol}_g(M).
\]
For \(\operatorname{Ric}=\lambda g\), \(\lambda<0\),
\[
c_1(K_I)=-\frac{\lambda}{2\pi}\bigl([\alpha]+[\beta]\bigr).
\]
These are real isotropic classes; integrality is not supplied. The proposed connection-curvature formula in Step 60 is not derived in the provided texts.

## 5. Rescaling and the exact compact negative alternative

The splitting paper, §2.1, Lemma 2, applies without assuming holomorphic eigendistributions.

Starting with Kähler–Einstein \(h\),
\[
\operatorname{Ric}_h=\lambda h,\qquad \lambda<0,
\]
and an opposite almost-Kähler \(J\), define
\[
h_t=h|_{D_+}+t\,h|_{D_-},\qquad t>0.
\]
Its fundamental forms are
\[
\omega_{I,t}=\alpha+t\beta,\qquad
\Omega_{J,t}=\alpha-t\beta.
\]
Thus \(h_t\) is Kähler for \(I\) and almost-Kähler for \(J\). In complex dimension two,
\[
d\mu_{h_t}=t\,d\mu_h.
\]
The determinant changes by a constant, so
\[
\rho_{h_t}=\rho_h,\qquad
\operatorname{Ric}_{h_t}=\operatorname{Ric}_h
\]
as covariant tensors. The Ricci **endomorphism**, however, has eigenvalues
\[
\boxed{\lambda,\ \lambda/t.}
\]
For \(t\ne1\), these are distinct negative constants.

Conversely, if a Kähler metric \(g\) has Ricci eigenvalues \(a<b<0\), its eigenforms satisfy
\[
\alpha=\frac{b\omega_I-\rho}{b-a},\qquad
\beta=\frac{\rho-a\omega_I}{b-a}.
\]
They are closed. Flipping \(I\) on one eigenspace gives the commuting opposite almost-Kähler structure, and
\[
\widetilde g=g|_{E_a}+\frac ba\,g|_{E_b}
\]
is Kähler–Einstein with Einstein constant \(a\).

For fixed \(a,b\), this is the correspondence in the paper’s Corollary 1. Strictness corresponds precisely to nonparallel eigendistributions.

**Correct compact alternative.** The splitting paper’s Theorem 2 and Lemmas 5–6 establish:

- a compact Kähler surface with two distinct constant Ricci eigenvalues and at least one nonnegative eigenvalue is locally a product of constant-curvature curves;
- in the nonproduct case, both eigenvalues are negative, \((M,I)\) is minimal of general type with ample canonical bundle, and
  \[
  \tau(M,I)>0,\qquad \tau(M,I)\in2\mathbb Z;
  \]
- conversely, the existence of such a nonproduct negative-eigenvalue metric is equivalent to a negative Kähler–Einstein metric carrying a **strict opposite-orientation** almost-Kähler structure.

Within this class, \(\tau=0\) forces integrability, by Lemma 6. The complex structure attached to the general-type conclusion is the original integrable structure \(I\), not the strict almost-complex structure \(J\); this avoids the notation ambiguity in the survey’s restatement.

Thus Step 60’s “unresolved case” should explicitly include this established equivalence and the even-positive-signature restriction. The sources leave the existence of the nonproduct negative alternative unresolved. The Weyl localization adds the necessary condition
\[
\lambda_{\min}(W_I^-)\le s/6
\]
somewhere, but does not close that alternative.

A normalization warning: when the papers describe factors as having “scalar curvatures \(\lambda,\mu\),” their Ricci-eigenvalue notation should not be copied literally. A real \(2k\)-dimensional factor with Einstein constant \(\lambda\) has scalar curvature \(2k\lambda\); for a curve, \(\lambda\) is its Gauss curvature.

## 6. Symmetric metrics and fixed smooth manifolds

### The three negative Einstein symmetric types

For the specified symmetric metrics, Step 60’s conclusions are correct:

1. **Real hyperbolic four-manifold:** no compatible almost-Kähler structure in either orientation.
2. **Complex-hyperbolic surface:** exactly \(\pm\omega_I\).
3. **Locally \(\mathbb H^2\times\mathbb H^2\):** every compatible almost-Kähler form is parallel. On a finite cover preserving the factors and their orientations, the possibilities are
   \[
   \pm(\omega_1+\omega_2),\qquad
   \pm(\omega_1-\omega_2),
   \]
   with descent determined by the deck action.

For item 3, apply the compact same-orientation lemma to the product complex structure having the orientation of the given form.

The survey, §6, Corollaries 2–3, already excludes real-hyperbolic space and oppositely oriented complex-hyperbolic space **even locally**. Its Corollary 6 also excludes compact locally homogeneous critical strict almost-Kähler four-manifolds. Accordingly, replace the claim that global charge is what first removes reversed ball quotients: it provides an independent compact proof and the broader open-pinching exclusion.

These statements concern the three negative **Einstein** symmetric types, not every locally symmetric metric with negative scalar curvature.

### Fixed-manifold implications

Assuming the BCG and LeBrun Einstein-rigidity statements quoted in Step 60,
\[
g=c\,\phi^*g_0,\qquad c>0,
\]
the exact conclusions are:

- a closed smooth manifold diffeomorphic to a compact real-hyperbolic four-manifold admits no almost-Kähler Einstein pair;
- on a closed smooth manifold diffeomorphic to a compact complex-hyperbolic surface, every almost-Kähler Einstein pair has the form
  \[
  \boxed{
  (g,\Omega)=
  \bigl(c\,\phi^*g_0,\ \pm c\,\phi^*\omega_0\bigr).
  }
  \]
  It induces the transported complex orientation.

For a ball quotient, \(\tau=\chi/3>0\), so a self-diffeomorphism cannot reverse its complex orientation.

For the real-hyperbolic rigidity input, the standard proof mechanism is concrete. Normalize an arbitrary negative Einstein metric by \(\operatorname{Ric}=-3g\). BCG gives
\[
\operatorname{Vol}(g)\ge\operatorname{Vol}(g_0),
\]
whereas Einstein Gauss–Bonnet gives
\[
6\operatorname{Vol}(g_0)
=8\pi^2\chi
=\int_M|W_g|^2+6\operatorname{Vol}(g).
\]
Thus equality holds, \(W_g=0\), and rigidity identifies the metric. Nonnegative Einstein constant is excluded by the exponential-growth fundamental group of a compact hyperbolic quotient versus polynomial volume growth under nonnegative Ricci curvature.

**Evidence boundary:** neither the primary BCG paper nor LeBrun’s *Einstein metrics and Mostow rigidity* is included. The supplied survey and splitting paper do not independently verify the exact LeBrun theorem statement, numbering, or absence of a \(b_+\) hypothesis. The deductions above are exact consequences of the rigidity statement quoted in Step 60, not a fresh primary-text verification of that input.

Finally, two reductions should be weakened:

- Einstein uniqueness on a locally \(\mathbb H^2\times\mathbb H^2\) manifold would suffice for the all-metrics Goldberg conclusion; the latter is not equivalent to uniqueness.
- On a minimal general-type surface, proving that every Einstein metric is Kähler in the relevant orientation would settle the same-orientation question, but Lemma 60.3 applies only after that Kähler property is established. Proposition 60.4 likewise addresses only metrics already known to be Kähler.