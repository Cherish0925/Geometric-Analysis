# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step57_rational_branch_and_global_tests.md",
    "Sessions/S1003A01/workspace/notes/step57_bianchiVIII_strict_AKE_negative.md",
    "Sessions/S1003A01/workspace/scripts/step57_classA_metric_only.py",
    "Sessions/S1003A01/workspace/scripts/step56_bianchiA_ake.py",
    "Sessions/S1003A01/workspace/scripts/step56_akeA_propagate.py"
  ]
}
```

## Task

Independently verify the proposed explicit Bianchi-VIII cohomogeneity-one almost-Kähler Einstein pair. Read the exact rational formulas and the underlying class-A convention/code. Check the mathematical chain: structure equations and orientation; coefficient normalization |Omega|^2=2; direct closure dOmega=0; Ric(g)=-3g; strictness q>0; and whether the reported opposite-chirality Weyl block W^-=0 follows. Identify any sign, normalization, or logical error. Give a concise rigorous proof route that does not depend on numerical ODE shooting or on primality of a modular ideal. Distinguish exact local existence from end extension and novelty.

## Output

## Verification memo

### 1. Conventions and exact orthonormal-frame data

Take
\[
I=(1/3,1),\qquad
d\sigma _1=-2\sigma _2\wedge\sigma _3,\quad
d\sigma _2=2\sigma _3\wedge\sigma _1,\quad
d\sigma _3=2\sigma _1\wedge\sigma _2,
\]
so \(n=(-1,1,1)\). Let
\[
e^0=dt=\sqrt G\,dp,\qquad e^i=a_i\sigma_i,\qquad a_i=\sqrt{A_i},
\]
with the displayed rational \(G,A_i\), and orient by \(e^{0123}>0\). Then
\[
de^i=h_i e^{0i}+2W_i e^{jk},
\qquad
h_i=\frac{a_i'}{a_i},\qquad
W_i=\frac{n_i a_i}{a_ja_k}.
\]

Put
\[
R=1+3p^2,\qquad
\rho=\sqrt{\frac{9p^2-1}{R}},\qquad
k=\frac{dp}{dt}=\frac{(1-p^2)\rho}{2}.
\]
Direct simplification gives
\[
\begin{aligned}
h_1&=\rho\frac{-3p^3+9p^2-3p+1}{(3p-1)R},\\
h_2&=\rho\frac{3p^3+9p^2+3p+1}{(3p+1)R},\\
h_3&=\rho\frac{3p^4+1}{2pR},
\end{aligned}
\]
and
\[
W_1=-\frac{(1-p)(3p-1)}{8p\rho},\qquad
W_2=\frac{(1+p)(3p+1)}{8p\rho},\qquad
W_3=\frac{6p(1-p^2)}{\rho R^2}.
\]
These signs agree with the class-A convention in the scripts. All later identities reduce to rational algebra using
\[
\rho^2=\frac{9p^2-1}{R},\qquad
\frac{\rho'}{\rho}=\frac{9p}{9p^2-1}-\frac{3p}{R}.
\]

### 2. Einstein equation

For cyclic \((i,j,k)\), exact substitution gives
\[
Q:=\sum_{i<j}h_ih_j+\sum_iW_i^2-2\sum_{i<j}W_iW_j=3
\]
and
\[
k\frac{dh_i}{dp}
=-h_i(h_1+h_2+h_3)
+2\bigl(W_i^2-(W_j-W_k)^2\bigr)+3.
\]
These are precisely the class-A Einstein equations with \(\lambda=-3\):
\[
h_i'=-h_iS+2\bigl(W_i^2-(W_j-W_k)^2\bigr)-\lambda,
\qquad Q+\lambda=0.
\]
They follow independently from the Cartan connection of the displayed coframe, so the result is
\[
\operatorname{Ric}(g)=-3g,\qquad s=-12.
\]

There is one scale bookkeeping point. At \(p=\tfrac12\),
\[
(h,W)=\frac{3\sqrt{35}}{16}
\left(
\frac{176}{147},\frac{656}{735},\frac{76}{147};
-\frac1{15},1,\frac{192}{245}
\right).
\]
Thus the rational point in the note has \(Q=256/105\), whereas the explicit metric has \(Q=3\). Using the unscaled rational point together with \(\lambda=-3\) would be incorrect; the explicit \(p\)-metric includes the required homothety.

### 3. Form normalization and closure

With
\[
\omega_i=e^{0i}+e^{jk},
\]
the chosen orientation makes \(\omega_i\) self-dual and
\[
|\omega_i|^2=2,\qquad \langle\omega_i,\omega_j\rangle=0\quad(i\ne j).
\]
Set
\[
\Omega=x_1\omega_1+x_2\omega_2,\qquad x_i=\sqrt{X_i},
\]
where
\[
X_1=\frac{(1-p)^3(3p+1)}{16p^3},\qquad
X_2=\frac{(1+p)^3(3p-1)}{16p^3}.
\]
The exact numerator identity
\[
(1-p)^3(3p+1)+(1+p)^3(3p-1)=16p^3
\]
gives \(X_1+X_2=1\), hence
\[
|\Omega|^2=2.
\]
This resolves the apparent distinction between coefficient norm \(1\) and form norm \(\sqrt2\).

Moreover,
\[
d\omega_i=(h_j+h_k-2W_i)e^{0jk}=-\mu_i e^{0jk},
\qquad
\mu_i=2W_i-h_j-h_k.
\]
The explicit functions satisfy
\[
\begin{aligned}
\mu_1
&=\frac{k}{2}\frac{d}{dp}\log X_1
=-\frac{3(1+p)^3\rho}{4p(3p+1)},\\
\mu_2
&=\frac{k}{2}\frac{d}{dp}\log X_2
=\frac{3(1-p)^3\rho}{4p(3p-1)}.
\end{aligned}
\]
Therefore \(x_i'=\mu_i x_i\), and consequently
\[
d\Omega
=\sum_{i=1}^2(x_i'-\mu_i x_i)e^{0jk}=0.
\]
Since \(\Omega\) is self-dual, closed, nondegenerate, and has norm squared \(2\), it defines the required almost-Kähler structure on \(I\times SL(2,\mathbb R)\), or on any locally defined compatible quotient.

### 4. Strictness

Let
\[
C_1=W_1-W_2-W_3,\quad
C_2=-W_1+W_2-W_3,\quad
C_3=-W_1-W_2+W_3,
\]
and \(b_i=h_i+C_i\). The frame connection gives exactly
\[
|\nabla\Omega|^2
=2\left[
\sum_iX_i\mu_i^2
+(X_1+X_2)b_3^2+X_1b_2^2+X_2b_1^2
\right].
\]
Substitution reduces this to
\[
q(p)=|\nabla\Omega|^2
=\frac{36(1-p^2)^3}{(1+3p^2)^3}.
\]
Thus \(q(p)>0\) for every \(p\in(1/3,1)\). It tends to \(32/3\) at the finite endpoint and to \(0\) only as \(p\to1\). The pair is therefore pointwise non-Kähler throughout the open interval.

### 5. Exact verification of \(W^-=0\)

Define the normalized anti-self-dual basis
\[
\phi_i^-=\frac{e^{0i}-e^{jk}}{\sqrt2}.
\]
The diagonal class-A connection splits the curvature operator into the three planes
\[
\operatorname{span}\{e^{0i},e^{jk}\};
\]
there are no entries mixing distinct \(i\).

For cyclic \((i,j,k)\), set
\[
K_{0i}=-(h_i'+h_i^2),\qquad
P_i=-(C_i'+h_iC_i).
\]
Here \(P_i=\langle\mathcal R(e^{0i}),e^{jk}\rangle\). Einstein implies
\[
K_{jk}=K_{0i},
\]
and hence
\[
\left\langle\mathcal R\phi_i^-,\phi_i^-\right\rangle
=K_{0i}-P_i.
\]

The explicit \(h_i,W_i\) obey the three elementary identities
\[
k\frac{d}{dp}(h_i-C_i)+h_i(h_i-C_i)=1.
\]
Equivalently,
\[
K_{0i}-P_i=-1.
\]
Therefore
\[
\mathcal R|_{\Lambda^-}=-\operatorname{Id}.
\]
Since \(s/12=-1\) and
\[
\mathcal R|_{\Lambda^-}=W^-+\frac{s}{12}\operatorname{Id},
\]
it follows exactly that
\[
\boxed{W^-=0}.
\]
This is the chirality opposite to \(\Omega\). Reversing the orientation interchanges the labels \(W^+\) and \(W^-\).

### 6. Local result versus endpoint geometry

The formulas alone prove an exact real-analytic almost-Kähler Einstein pair on every subinterval of \((1/3,1)\); neither ODE shooting nor any modular-ideal property enters this proof.

At \(p=1/3\), writing \(\delta=p-\tfrac13\) and taking \(t\) as distance from the endpoint,
\[
\delta=\frac29t^2+O(t^4),\qquad
A_1=t^2+O(t^4),\qquad A_2,A_3\to6,
\]
while
\[
A_2-A_3=t^4\,\beta(t^2),\qquad
x_1=1+O(t^2),\qquad x_2=t\,\gamma(t^2)
\]
for analytic \(\beta,\gamma\). These are the representation-theoretic orders expected when the \(E_1\)-circle has period \(2\pi\), its adjoint action on the horizontal plane has weight \(2\), and the normal disk has weight \(1\). A full extension statement additionally requires fixing the \(SL(2,\mathbb R)\) cover or lattice and writing \(g,\Omega\) in a nonsingular polar frame. The supplied asymptotics are strongly compatible with such an extension but are logically separate from the local theorem.

At \(p=1\),
\[
\sqrt G\sim \frac{1}{\sqrt2(1-p)},
\]
so the radial distance diverges. Completeness of a resulting global example follows once the finite endpoint has been attached in the stated bundle model.

No supplied source identifies this metric with an existing family. Its geometric validity and its literature identity are separate questions.

### Conclusion

Under the stated class-A and orientation conventions, the explicit rational formulas pass all requested exact tests:

\[
d\Omega=0,\qquad |\Omega|^2=2,\qquad
\operatorname{Ric}=-3g,\qquad
|\nabla\Omega|^2=\frac{36(1-p^2)^3}{(1+3p^2)^3}>0,\qquad
W^-=0.
\]

The only substantive bookkeeping traps are the homothety between the rational base point and the \(\lambda=-3\) metric, and the orientation-dependent labeling of the Weyl blocks.