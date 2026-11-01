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
    "Sessions/S1003A01/workspace/notes/step60_kahler_rigidity_weyl_pinching_goldberg.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/data/step60/pinching_control.json",
    "Sessions/S1003A01/workspace/scripts/step60_pinching_control.py",
    "Knowledge/objects/papers/The-curvature-and-the-integrability-of-almost-Kahler-manifolds-a-survey--0b93a46cd986--155063d8a5c0/object.md",
    "Knowledge/objects/papers/A-SPLITTING-THEOREM-FOR-KÄHLER-MANIFOLDS-WHOSE-RICCI-TENSORS-HAVE-CONST--10f85263858c--3bd939358128/object.md"
  ]
}
```

## Task

Critically verify the Step-60 note after Spirit #72. Read the actual note, exact pinching data/script, Step-59 zero-charge note, and the primary Apostolov–Drăghici survey and Apostolov–Drăghici–Moroianu splitting paper. Determine precisely which statements remain valid and which require correction: (i) Weitzenböck/Rayleigh localization and the distinction between λ_min=s/6 and norm saturation at a torsion zero, including the exact identity |W+|^2-s^2/24=|eta|^2+|W3+|^2; (ii) same-orientation Kähler metric lemma, especially the claim that a holomorphic 2-form of constant norm is parallel; (iii) opposite-orientation correspondence—whether closed complementary forms imply integrable plane fields and minimal complex-curve leaves, but not holomorphic subbundles or product splitting; (iv) the rescaled Kähler metrics with constant Ricci eigenvalues and the negative compact alternative; (v) fixed-manifold conclusions for real/complex hyperbolic quotients using LeBrun/BCG. Give corrected theorem statements and direct proof guidance, not procedural commentary.

## Output

# Scientific verification memo

## 1. Weyl localization: valid, with a sharper pointwise decomposition

Let
\[
u=\frac{\Omega}{\sqrt2},\qquad q=|\nabla\Omega|^2,\qquad
r=\langle W^+u,u\rangle .
\]
The Weitzenböck formula gives
\[
q=2\langle W^+\Omega,\Omega\rangle-\frac{2s}{3}
  =4r-\frac{2s}{3},
\]
hence
\[
\boxed{r=\frac{s}{6}+\frac q4.}
\]
Therefore
\[
q\ge 4\left(\lambda_{\min}(W^+)-\frac{s}{6}\right),
\]
and at every torsion zero \(z\),
\[
\boxed{\langle W^+u,u\rangle(z)=\frac{s}{6}},\qquad
\lambda_{\min}(W^+_z)\le \frac{s}{6}.
\]

The last inequality need not be equality. The zero only fixes the Rayleigh quotient in the \(\Omega\)-direction.

### Exact \(W^+\)-decomposition

Write \(H=u^\perp\subset\Lambda^+\), and decompose
\[
W^+u=ru+v,\qquad v\in H.
\]
With the Step-59 normalization,
\[
\eta:=W^+(\Omega)-r\Omega=\sqrt2\,v,\qquad |\eta|^2=2|v|^2.
\]
If \(A\) is the \(H\to H\) block of \(W^+\), set
\[
W_3^+:=A+\frac r2\operatorname{Id}_H;
\]
this is trace-free on \(H\). The three orthogonal pieces have norms
\[
|W_1^+|^2=\frac32r^2,\qquad |W_2^+|^2=|\eta|^2,\qquad
|W_3^+|^2=|W_3^+|_{\mathrm{HS}}^2.
\]
Consequently,
\[
\boxed{
|W^+|^2-\frac{s^2}{24}
=
|\eta|^2+|W_3^+|^2+\frac{s q}{8}+\frac{3q^2}{32}.
}
\]
At a torsion zero \(q=0\), this becomes the requested identity
\[
\boxed{
|W^+|^2-\frac{s^2}{24}=|\eta|^2+|W_3^+|^2.
}
\]

Thus:

* Every torsion zero satisfies \(|W^+|^2\ge s^2/24\).
* Norm equality holds exactly when
  \[
  \eta=0,\qquad W_3^+=0,
  \]
  equivalently
  \[
  W^+=\operatorname{diag}\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right)
  \]
  in a basis beginning with \(u\).
* The equation \(\lambda_{\min}=s/6\) is weaker than norm equality. It forces \(u\) to lie in the least eigenspace, hence \(\eta=0\), but it does not force \(W_3^+=0\).

For example, with \(s=-6\),
\[
W^+=\operatorname{diag}(-1,-1,2),\qquad u=e_1
\]
has Rayleigh quotient and least eigenvalue \(s/6=-1\), while
\[
|W^+|^2=6>\frac{s^2}{24}=\frac32.
\]
This algebraic example separates least-eigenvalue equality from norm saturation.

### Corrected localization theorem

For a closed almost-Kähler Einstein four-manifold with \(s<0\), the zero set
\[
Z=\{\nabla\Omega=0\}
\]
is nonempty because
\[
\langle c_2(E),[M]\rangle=5\chi+6\tau
=\chi+2(2\chi+3\tau)>0.
\]
Moreover,
\[
Z\subseteq\left\{\lambda_{\min}(W^+)\le \frac{s}{6}\right\}
       \cap\left\{|W^+|^2\ge\frac{s^2}{24}\right\}.
\]
Since \(T=\nabla\Omega\) is nonzero outside the first set, \(c_2(E)\) is the image of a relative class in
\[
H^4\!\left(M,M\setminus\{\lambda_{\min}\le s/6\};\mathbb Z\right).
\]

Hence both pinching exclusions in Step 60 are valid:
\[
\lambda_{\min}(W^+)>\frac{s}{6}\quad\text{everywhere}
\]
or
\[
|W^+|^2<\frac{s^2}{24}\quad\text{everywhere}
\]
precludes a compatible almost-Kähler structure.

For future zero-germ work, three distinct conditions should remain separated:
\[
\eta=0 \Longleftrightarrow \Omega\text{ is a }W^+\text{-eigenform},
\]
\[
\lambda_{\min}=s/6 \Longleftrightarrow
\eta=0\text{ and the other eigenvalues are }\ge s/6,
\]
\[
|W^+|^2=s^2/24 \Longleftrightarrow \eta=W_3^+=0.
\]

## 2. Exact pinching data: formulas are correct; two JSON root labels are not open-interval counts

The exact factorizations prove, for \(1/3<p<1\),
\[
w_i+2>0,\qquad i=1,2,3.
\]
Indeed:

* For \(w_1+2\), the remaining cubic
  \[
  3p^3+3p^2-3p+1
  \]
  is increasing on this interval and equals \(4/9\) at \(p=1/3\).

* For \(w_2+2\),
  \[
  w_2+2=\frac{6(1-p)^3(1+3p+3p^2-3p^3)}{(3p^2+1)^3},
  \]
  and the second factor is positive and increasing up to \(p=1\).

* For \(w_3+2\), writing \(u=p^2\),
  \[
  21u^3-3u^2+15u-1
  \]
  has derivative \(63u^2-6u+15>0\) and value \(160/243\) at \(u=1/9\).

Similarly,
\[
|W^+|^2-\frac{s^2}{24}
=
-\frac{18(1-p^2)^3f(p^2)}{(3p^2+1)^6},
\]
where
\[
f(u)=189u^3-207u^2+87u-5.
\]
Here
\[
f'(u)=567u^2-414u+87>0,\qquad f(1/9)=\frac{64}{27},
\]
so the norm difference is strictly below zero for every finite \(p\in(1/3,1)\).

The JSON entries

```text
"w2+2_roots_in_(1/3,1)": "1"
"pinching_numerator_roots_in_(1/3,1)": "1"
```

are incompatible with their labels as open-interval counts. In both cases the exact factorization shows that the recorded root is \(p=1\), where a factor \((p-1)^3\) occurs. There is no root in the open interval.

Thus the geometric conclusion is correct:
\[
\lambda_{\min}(W^+)>-2,\qquad |W^+|^2<6
\]
at every finite point, while
\[
\lambda_{\min}(W^+)\to-2,\qquad |W^+|^2\to6,\qquad q\to0
\]
as \(p\to1\). The global identity above explains how the norm can remain below \(6\):
\[
|W^+|^2-6
=
|\eta|^2+|W_3^+|^2-\frac{3q}{2}+\frac{3q^2}{32}.
\]

## 3. Same-orientation Kähler lemma: valid, with a precise line-bundle argument

Let \((M,g,I,\omega_I)\) be a compact Kähler surface and let \(\Omega\) be a compatible almost-Kähler form inducing the complex orientation. Since \(\Omega\) is harmonic and self-dual,
\[
\Omega=f\omega_I+\operatorname{Re}\theta,
\]
where \(f\) is constant and \(\theta\in H^0(M,K_I)\).

The constant-length equation for \(\Omega\) makes \(|\theta|\) constant. If \(\theta\) vanishes somewhere, it is identically zero. Otherwise it is a nowhere-zero holomorphic frame of the canonical line bundle. In the holomorphic frame \(\theta\), the Chern connection satisfies
\[
D\theta=\partial\log|\theta|^2\otimes\theta.
\]
Because \(|\theta|\) is constant, \(D\theta=0\). On a Kähler manifold, the Chern connection on \(K_I\) is the connection induced by the Levi-Civita connection, so \(\theta\) is parallel. This line-bundle argument is valid; constant norm alone would not imply parallelness for a higher-rank holomorphic bundle.

Therefore \(\Omega\) is parallel. If \(\theta\not\equiv0\), the curvature of \(K_I\) vanishes, so the Ricci form and Ricci tensor vanish. Hence:
\[
\boxed{\text{If }g\text{ is not Ricci-flat, then }\Omega=\pm\omega_I.}
\]

The unnumbered deformation paragraph following the lemma is not derived in the supplied papers. In particular, the direct-sum description of the gauge-fixed linearized Einstein–almost-Kähler system and the treatment of the stated cross terms require a separate linearization. The elementary implication
\[
\Delta|\sigma|^2=0
\Longrightarrow |\sigma|\text{ constant}
\Longrightarrow \sigma\text{ parallel}
\Longrightarrow \operatorname{Ric}=0
\]
is correct for a holomorphic \(2\)-form, but the preceding second-order reduction is not established by the supplied material.

## 4. Opposite orientation: the foliation correspondence is valid after a wording correction

Let \(J\) be \(g\)-orthogonal and induce the orientation opposite to \(I\). Then \(I\) and \(J\) commute, and
\[
P=-IJ
\]
is a symmetric involution with \(I\)-invariant rank-two eigendistributions
\[
TM=D_+\oplus D_-.
\]
Writing
\[
J=I\text{ on }D_+,\qquad J=-I\text{ on }D_-,
\]
and denoting the corresponding rank-two forms by \(\omega_\pm\), one has
\[
\omega_I=\omega_++\omega_-,\qquad \Omega_J=\omega_+-\omega_-.
\]

If \(\Omega_J\) is closed, then both \(\omega_\pm\) are closed. A closed constant-rank form has an integrable kernel, so
\[
D_-=\ker\omega_+,\qquad D_+=\ker\omega_-
\]
are Frobenius-integrable. Each leaf is \(I\)-invariant and therefore is a complex curve in the leafwise sense. Such curves are calibrated by \(\omega_I\), hence minimal.

Conversely, suppose \(D_\pm\) are orthogonal, complementary, \(I\)-invariant and integrable. Their leaves are complex curves and therefore minimal. For the characteristic form \(\omega_+\):

* its \((D_+,D_+,D_-)\) component of \(d\omega_+\) is the mean-curvature term and vanishes by minimality;
* its \((D_+,D_-,D_-)\) component vanishes because \(D_-\) is integrable.

Thus \(d\omega_+=0\), and similarly \(d\omega_-=0\). Hence \(\Omega_J\) is closed.

The corrected statement is therefore:

\[
\boxed{
\begin{aligned}
&\text{Opposite-orientation compatible almost-Kähler structures}\\
&\quad\longleftrightarrow
\text{ ordered orthogonal pairs of complementary,}\\
&\qquad\text{\(I\)-invariant, Frobenius-integrable plane fields.}
\end{aligned}}
\]

The phrase “foliations by \(I\)-holomorphic curves” should mean that individual leaves are complex curves. It does not imply that \(D_\pm\) are holomorphic line subbundles of \(T^{1,0}M\).

Nor do closure, integrability and minimality imply local product geometry. Indeed,
\[
\nabla J=I\nabla P
\]
is determined by the second fundamental tensors of the two foliations, and those tensors may be nonzero while their traces vanish. One has
\[
J\text{ Kähler}
\Longleftrightarrow
D_\pm\text{ parallel}
\Longleftrightarrow
D_\pm\text{ both totally geodesic}
\Longleftrightarrow
g\text{ locally a Riemannian product}.
\]
The strict local models in Proposition 5 of the supplied survey provide Kähler \(I\) together with a commuting strict almost-Kähler \(J\), so they directly show that the foliation conditions do not force product splitting. If both orthogonal line distributions were holomorphic subbundles, the Kähler Chern connection would preserve the orthogonal holomorphic splitting, yielding parallel distributions and hence a product.

## 5. Rescaling and the compact \(a,b<0\) alternative

The Apostolov–Drăghici–Moroianu paper gives a stronger formulation of the opposite-orientation problem.

Let \(h\) be Kähler–Einstein,
\[
\operatorname{Ric}_h=\lambda h,\qquad \lambda<0,
\]
and let \(J\) be a commuting opposite-orientation almost-Kähler structure. With the splitting \(D_+\oplus D_-\), define
\[
h_t=h|_{D_+}+t\,h|_{D_-},\qquad t>0.
\]
Its two fundamental forms are
\[
\omega_{I,t}=\omega_++t\omega_-,
\qquad
\Omega_{J,t}=\omega_+-t\omega_-,
\]
so \(h_t\) is Kähler for \(I\) and almost-Kähler for \(J\).

In complex dimension two,
\[
d\mu_{h_t}=t\,d\mu_h.
\]
The determinant changes by the constant factor \(t\), so the Ricci form and Ricci tensor remain unchanged. Relative to \(h_t\), the Ricci endomorphism has eigenvalues
\[
\boxed{\lambda,\qquad \lambda/t.}
\]
For \(t\ne1\), these are two distinct constants below zero. Conversely, if a Kähler metric has distinct constant Ricci eigenvalues
\[
a<b<0,
\]
then rescaling the \(b\)-eigenspace by \(b/a\) produces a Kähler–Einstein metric with Einstein constant \(a\), together with the commuting opposite almost-Kähler structure.

Thus the compact strict opposite-orientation problem is equivalent to the nonproduct case of the constant-Ricci-eigenvalue problem. Theorem 2 of the splitting paper gives:

* either the metric is locally a product of two constant-curvature Riemann surfaces;
* or both Ricci eigenvalues are \(<0\), the complex surface is minimal of general type with ample canonical bundle, and its complex-orientation signature satisfies
  \[
  \tau>0,\qquad \tau\in2\mathbb Z.
  \]

In the second case, reversing orientation produces an Einstein strict almost-Kähler structure. Conversely, a compact strict opposite-orientation structure on an \(s<0\) Kähler–Einstein surface produces precisely such a Kähler metric with two constant Ricci eigenvalues. This topological and geometric information should accompany the “unresolved case” discussion in Step 60.

## 6. Locally symmetric and fixed-manifold conclusions

### Symmetric metric

Theorem 60.5 is mathematically sound after the foliation wording above:

1. A compact real-hyperbolic four-manifold has no compatible almost-Kähler structure for either orientation.

2. A compact complex-hyperbolic surface with its standard metric has exactly
   \[
   \pm\omega_I
   \]
   as compatible almost-Kähler forms.

3. For a compact locally \(\mathbb H^2\times\mathbb H^2\) metric, every compatible almost-Kähler structure is parallel. On a finite cover preserving both oriented factors, it is one of
   \[
   \pm(\omega_1+\omega_2),\qquad
   \pm(\omega_1-\omega_2).
   \]

For item 3, choose whichever product complex structure has the same orientation as the pulled-back almost-Kähler form and apply the same-orientation lemma.

The survey already states, in its Section 6 Corollary 3, that real hyperbolic four-space and complex hyperbolic two-space with the nonstandard orientation admit no compatible almost-Kähler structure even locally. Thus the global charge proof is an alternative compact proof in those cases, not the only mechanism known in the supplied literature. The survey’s Corollary 6 also already excludes strict structures on compact locally homogeneous critical almost-Kähler four-manifolds.

### Fixed smooth manifold

For a real-hyperbolic quotient, the Einstein rigidity mechanism can be written directly. Normalize an Einstein metric by
\[
\operatorname{Ric}=-3g.
\]
BCG gives
\[
\operatorname{Vol}(g)\ge\operatorname{Vol}(g_0).
\]
Chern–Gauss–Bonnet gives
\[
8\pi^2\chi
=\int_M\left(|W|^2+6\right)d\mu_g
=6\operatorname{Vol}(g_0),
\]
hence
\[
\operatorname{Vol}(g)
=
\operatorname{Vol}(g_0)-\frac16\int_M|W|^2d\mu_g
\le\operatorname{Vol}(g_0).
\]
Equality follows, so \(W=0\) and \(g\) is standard up to scale and diffeomorphism. Since the standard metric admits no compatible almost-Kähler structure, no Einstein metric on that smooth manifold participates in an almost-Kähler Einstein pair.

Using the LeBrun rigidity theorem quoted in Step 60 for compact complex-hyperbolic surfaces, every Einstein metric is likewise a scale and pullback of the standard metric. If
\[
g=c\,\phi^*g_0,
\]
then pushing an almost-Kähler form through \(\phi\) and dividing by \(c\) reduces the question to the standard metric. The same-orientation lemma gives \(\pm\omega_I\), while the opposite orientation is excluded. Therefore
\[
\boxed{\Omega=\pm c\,\phi^*\omega_I.}
\]

So the fixed-manifold conclusions are correct in the precise form:

* a smooth compact real-hyperbolic four-manifold supports no almost-Kähler Einstein pair;
* on a smooth compact complex-hyperbolic surface, every almost-Kähler Einstein pair is the standard Kähler–Einstein pair up to diffeomorphism, scale and sign.

The supplied archive contains only the metadata-level record of LeBrun’s 1995 paper, not its full text. Thus the complex-hyperbolic deduction is mathematically exact from the rigidity statement quoted in Step 60, while the theorem numbering and absence of any \(b_+\) hypothesis are not independently readable from the supplied primary artifact.