# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md",
    "Sessions/S1003A02/workspace/scripts/o10_localization.py",
    "Sessions/S1003A02/workspace/data/o10_localization.json",
    "Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex",
    "Skills/geometric-analysis/research/paper/sections/single_parameter_statement.tex",
    "Skills/geometric-analysis/references/results-and-questions.md",
    "Skills/geometric-analysis/references/conventions-and-literature.md"
  ]
}
```

## Task

Independently check the proposed density-free endpoint Theorem L and Corollary K in the Step 4 note. Verify the exact rewriting of V kappa_beta; all inequality directions; the optimized gamma and coefficient a(theta,beta); the discriminant and thresholds theta=2/3, beta=8, theta=3/4; and, crucially, close the proof for every original metric by using the actual conformal-monopole hypotheses, Yamabe normalization, conformal transfer, and the finite-parameter theorem with its true b=(-a^2)_+/V factor. State an exact corrected theorem and proof if valid, and flag any quantifier/constant flaw. Also verify the Kähler blow-up corollary's p>=A, a^2=T_+, Noether density calculation and universal constant under its stated p_g hypothesis.

## Output

# Scientific verification memo

## 1. Main result

The density-free endpoint theorem is valid for every original metric, provided the stated “actual conformal monopole” hypothesis is retained throughout its conformal class. The elementary computation is correct. The bounded-\(\beta\) argument in the note requires the Yamabe transfer from `finite_density_endpoint.tex`; applying the single-parameter theorem directly to the original metric is not justified.

The true factor
\[
b=\frac{(-a^2)_+}{V}
\]
causes no loss in the only branch where the single-parameter theorem is needed: there \(T_+>0\) and \(a^2\ge T_+\), hence \(a^2>0\) and \(b=0\).

Two textual corrections are needed:

1. At \(\theta=2/3\), the quadratic does not become \(<0\) on an interval: it equals \((\beta-8)^2/12\) and vanishes only at \(\beta=8\).
2. The constant depends essentially on the fixed value of \(\theta<3/4\). The argument supplies no single positive constant uniform as \(\theta\uparrow3/4\).

---

## 2. Exact rewriting and inequality directions

Write
\[
Q=\int_M\frac{(s+4)^2}{4}.
\]
Since
\[
\Ric+g=\Ric^\circ+\frac{s+4}{4}g,\qquad
|\Ric+g|^2=|\Ric^\circ|^2+\frac{(s+4)^2}{4},
\]
one has
\[
V\kappa_\beta=P+Q+D_\beta.
\]
The chiral Chern–Weil identity
\[
4\pi^2T_+=\frac S{24}+2W-\frac P2
\]
is equivalent to
\[
P=\frac S{12}+4W-8\pi^2T_+.
\]
Therefore
\[
\boxed{
V\kappa_\beta
=\left(\frac{13}{12}+\frac1\beta\right)S
 +(6\beta+10)W+Q
 -8\pi^2T_+-72\pi^2p.
}
\tag{2.1}
\]

LeBrun’s estimate and Young’s inequality give, for every \(\gamma>0\),
\[
72\pi^2p
\le \int(s-\sqrt6|W^+|)^2
\le (1+\gamma^{-1})S+6(1+\gamma)W.
\tag{2.2}
\]

Suppose \(T_+\le\eta p\), with \(0\le\eta<3/4\). Then
\[
-8\pi^2T_+-72\pi^2p
\ge -(72+8\eta)\pi^2p
=-72\pi^2\lambda p,
\qquad
\lambda=1+\frac{\eta}{9}.
\]
Multiplying (2.2) by \(-\lambda\) reverses its direction:
\[
-72\pi^2\lambda p
\ge
-\lambda(1+\gamma^{-1})S
-6\lambda(1+\gamma)W.
\]
Thus
\[
V\kappa_\beta\ge
Q+
\left[\frac{13}{12}+\frac1\beta-\lambda(1+\gamma^{-1})\right]S
+
\left[6\beta+10-6\lambda(1+\gamma)\right]W.
\tag{2.3}
\]

To retain a coefficient of \(W\) that is at least zero, one needs
\[
\gamma\le\gamma_{\max}
=\frac{9\beta-\eta+6}{9+\eta}.
\]
The coefficient of \(S\) in (2.3) increases with \(\gamma\), so the optimal admissible choice is precisely \(\gamma_{\max}\). It makes the \(W\)-coefficient zero and gives
\[
V\kappa_\beta\ge a(\eta,\beta)S+Q,
\tag{2.4}
\]
where
\[
\boxed{
a(\eta,\beta)=
\frac{
(\frac34-\eta)\beta^2+
(\frac12-\frac{11}{4}\eta)\beta+
6-\eta
}{
\beta(9\beta-\eta+6)
}.
}
\tag{2.5}
\]

For \(a>0\),
\[
as^2+\frac{(s+4)^2}{4}
\ge \frac{16a}{1+4a},
\]
because the minimum occurs at \(s=-4/(1+4a)\). Hence
\[
\boxed{
\kappa_\beta\ge\frac{16a(\eta,\beta)}
 {1+4a(\eta,\beta)}
}
\tag{2.6}
\]
whenever \(a(\eta,\beta)>0\).

All signs in the note’s elementary argument are therefore correct.

---

## 3. The quadratic thresholds

Let
\[
N_\eta(\beta)
=\left(\frac34-\eta\right)\beta^2
+\left(\frac12-\frac{11}{4}\eta\right)\beta
+6-\eta.
\]
Its discriminant is
\[
\begin{aligned}
\Delta(\eta)
&=\left(\frac12-\frac{11}{4}\eta\right)^2
 -4\left(\frac34-\eta\right)(6-\eta)\\
&=\frac{57}{16}\eta^2+\frac{97}{4}\eta-\frac{71}{4}\\
&=\boxed{\frac{57}{16}
\left(\eta-\frac23\right)
\left(\eta+\frac{142}{19}\right)}.
\end{aligned}
\]

Consequently:

- For \(0\le\eta<2/3\), one has \(\Delta<0\), the leading coefficient is positive, and \(N_\eta(\beta)>0\) for every \(\beta\).
- At \(\eta=2/3\),
  \[
  N_{2/3}(\beta)=\frac{(\beta-8)^2}{12}.
  \]
  Thus the elementary coefficient vanishes only at \(\beta=8\).
- For \(2/3<\eta<3/4\),
  \[
  N_\eta(2)=10-\frac{21}{2}\eta>0,\qquad
  N_\eta(8)=58-87\eta<0,
  \]
  so there are roots
  \[
  \boxed{
  \beta_\pm(\eta)=
  \frac{\frac{11}{4}\eta-\frac12\pm\sqrt{\Delta(\eta)}}
       {2(\frac34-\eta)}
  }
  \]
  satisfying
  \[
  2<\beta_-(\eta)<8<\beta_+(\eta).
  \]
  The numerator is \(<0\) exactly for
  \(\beta\in(\beta_-,\beta_+)\).
- Since
  \[
  \lim_{\beta\to\infty}a(\eta,\beta)
  =\frac1{12}-\frac{\eta}{9},
  \]
  the large-\(\beta\) coefficient is positive exactly when
  \(\eta<3/4\).
- At \(\eta=3/4\),
  \[
  N_{3/4}(\beta)=-\frac{25}{16}\beta+\frac{21}{4},
  \]
  which is \(<0\) for \(\beta>84/25\). The elementary estimate therefore supplies no large-\(\beta\) coercivity there.

The special value \(\beta=8\) agrees with
\[
\boxed{
D_8
=108\pi^2\left(T_+-\frac23p\right)
+\frac{27}{2}P,
}
\]
obtained by substituting the Chern–Weil formula into
\[
D_8=\frac98S+54W-72\pi^2p.
\]

The JSON formulas for \(\gamma_{\max}\), \(a\), \(a_\infty\), and the Kähler–Einstein value agree with these calculations. The field `beta0_first_positive` is not useful for the interval analysis: for \(\eta=0.7\) and \(0.74\), it returns a value near \(2\), although \(a\) later becomes \(<0\) before becoming positive again. The two roots, especially \(\beta_+\), are the relevant quantities.

---

## 4. Corrected density-free theorem

### Theorem L′

Let \(\theta<3/4\). Let \(M\) be a closed connected oriented smooth four-manifold and let \([g]\) be a conformal class. Suppose a fixed Spin\(^c\) structure with determinant class \(a\) admits an ordinary unperturbed monopole solution for every metric in \([g]\). Put
\[
p=(a_h^+)^2,
\]
which is independent of \(h\in[g]\). Assume
\[
p\ge A>0,\qquad a^2\ge T_+,\qquad T_+\le\theta A.
\]
Then there is \(c_L(\theta)>0\), depending only on \(\theta\), such that every \(h\in[g]\) and every finite \(\beta\ge2\) satisfy
\[
\boxed{
\kappa_\beta(h)\ge
c_L(\theta)\frac{(\beta-2)^2}{\beta^2}.
}
\tag{4.1}
\]
No estimate involving \(\chi(M)/A\) is used.

For a theorem over all metrics on \(M\), the Spin\(^c\) structure may be selected separately on each conformal class, but the same \(A\) and the displayed inequalities must hold uniformly, and the selected structure must supply solutions throughout that class.

### Proof

#### Case 1: \(T_+\le0\)

Set \(\eta=0\). Then \(T_+\le\eta p\), and
\[
a(0,\beta)
=\frac{\beta^2/4+\beta/6+2}{\beta(3\beta+2)}
\ge\frac1{12}.
\]
Equation (2.6) yields
\[
\kappa_\beta\ge1.
\]
This proves (4.1), with any \(c_L(\theta)\le1\). In particular, if the original \(\theta\) is \(<0\), then \(T_+\le\theta A<0\), and this case applies.

#### Case 2: \(T_+>0\) and \(0\le\theta<2/3\)

Since \(p\ge A\),
\[
T_+\le\theta A\le\theta p.
\]
The quadratic analysis gives \(a(\theta,\beta)>0\) for all \(\beta\ge2\), and
\[
a(\theta,\beta)\longrightarrow
\frac1{12}-\frac{\theta}{9}>0.
\]
Continuity on the compactified interval \([2,\infty]\) gives
\[
\underline a_\theta
:=\inf_{\beta\ge2}a(\theta,\beta)>0.
\]
Therefore
\[
\kappa_\beta\ge
\frac{16\underline a_\theta}{1+4\underline a_\theta}
\ge
\frac{16\underline a_\theta}{1+4\underline a_\theta}
\frac{(\beta-2)^2}{\beta^2}.
\]

#### Case 3: \(T_+>0\) and \(2/3\le\theta<3/4\)

Define \(\beta_+(2/3)=8\), use the root above for \(\theta>2/3\), and put
\[
B_\theta=2\beta_+(\theta).
\]
For \(\beta\ge B_\theta\), one has \(a(\theta,\beta)>0\), and
\[
m_\theta:=
\inf_{\beta\ge B_\theta}
\frac{16a(\theta,\beta)}{1+4a(\theta,\beta)}>0.
\]
Hence
\[
\kappa_\beta\ge m_\theta
\ge m_\theta\frac{(\beta-2)^2}{\beta^2}
\qquad(\beta\ge B_\theta).
\tag{4.2}
\]

It remains to treat \(2\le\beta\le B_\theta\) for an arbitrary original metric \(g\).

The actual conformal monopole and \(p>0\) force the Yamabe constant of \([g]\) to be strictly below zero: otherwise a constant-scalar representative with \(s\ge0\), together with the spinor Weitzenböck formula, would force the monopole spinor and \(a^+\) to vanish, contradicting \(p>0\). Let \(\widehat g\in[g]\) be normalized by
\[
s_{\widehat g}=-4.
\]

Set
\[
\delta=S(g)-S(\widehat g)\ge0.
\]
Conformal invariance of \(W\), \(p\), and \(T_+\), together with Chern–Weil, gives
\[
\widehat P=P-\frac{\delta}{12},\qquad
\widehat D_\beta
=D_\beta-\left(1+\frac1\beta\right)\delta.
\tag{4.3}
\]
LeBrun’s estimate with \(\gamma=\beta\) gives \(D_\beta\ge0\) for every metric; in particular \(\widehat D_\beta\ge0\). Thus
\[
0\le\delta\le D_\beta\le V\kappa_\beta.
\tag{4.4}
\]

Writing \(e=s_g+4\), one has
\[
\int e^2\le4V\kappa_\beta
\]
and
\[
16\widehat V
=16V-8\int e+\int e^2-\delta.
\]
Cauchy–Schwarz and (4.4) give
\[
\frac{\widehat V}{V}
\ge1-\sqrt{\kappa_\beta}-\frac{\kappa_\beta}{16}.
\tag{4.5}
\]
Moreover,
\[
\widehat P+\widehat D_\beta
\le P+D_\beta
\le V\kappa_\beta.
\]
Since \(s_{\widehat g}=-4\),
\[
\widehat\kappa_\beta
=\frac{\widehat P+\widehat D_\beta}{\widehat V},
\]
and therefore
\[
\boxed{
\widehat\kappa_\beta
\le
\frac{\kappa_\beta}
 {1-\sqrt{\kappa_\beta}-\kappa_\beta/16}
}
\tag{4.6}
\]
whenever the denominator is positive.

Here \(T_+>0\) and \(a^2\ge T_+\), so \(a^2>0\) and the true single-parameter factor is exactly
\[
b=\frac{(-a^2)_+}{\widehat V}=0.
\]
The single-parameter theorem therefore gives
\[
\frac{\widehat P}{\widehat V}
+\frac{\widehat D_\beta}{\beta\widehat V}
\ge c_{\rm par}\frac{(\beta-2)^2}{\beta^4}.
\]
Since \(\widehat D_\beta\ge0\) and \(\beta\ge2\),
\[
\widehat\kappa_\beta
=\frac{\widehat P+\widehat D_\beta}{\widehat V}
\ge c_{\rm par}\frac{(\beta-2)^2}{\beta^4}.
\tag{4.7}
\]

If \(\kappa_\beta\ge1/16\), then
\[
\kappa_\beta\ge\frac1{16}\frac{(\beta-2)^2}{\beta^2}.
\]
If \(\kappa_\beta\le1/16\), the denominator in (4.6) is at least
\[
1-\frac14-\frac1{256}=\frac{191}{256}.
\]
Combining (4.6) and (4.7),
\[
\kappa_\beta
\ge\frac{191}{256}c_{\rm par}
\frac{(\beta-2)^2}{\beta^4}
\ge
\frac{191c_{\rm par}}{256B_\theta^2}
\frac{(\beta-2)^2}{\beta^2}.
\tag{4.8}
\]

Taking
\[
c_L(\theta)=
\min\left\{
1,\,
m_\theta,\,
\frac1{16},\,
\frac{191c_{\rm par}}{256B_\theta^2}
\right\}
\]
in this case completes the proof. ∎

The dependence deteriorates as \(\theta\uparrow3/4\): both \(a_\infty\to0\) and \(\beta_+(\theta)\to\infty\).

---

## 5. Kähler blow-up corollary

### Corollary K′

Let \(X\) be a minimal Kähler surface of general type with \(p_g(X)\ge1\), let
\[
A=c_1^2(X)>0,
\]
and let
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},\qquad k\ge0.
\]
Then there is a universal \(c_K>0\), independent of \(X,k,g,\beta\), such that every metric \(g\) on \(M\) and every finite \(\beta\ge2\) satisfy
\[
\boxed{
\kappa_\beta(g)\ge
c_K\frac{(\beta-2)^2}{\beta^2}.
}
\]

### Verification of the monopole data

For a Kähler surface,
\[
b_+(X)=1+2p_g(X)\ge3,
\]
so the canonical Seiberg–Witten class and its blow-up classes have no chamber dependence. The iterated blow-up formula supplies
\[
a_\varepsilon
=K_X+\sum_{i=1}^k\varepsilon_iE_i,
\qquad \varepsilon_i\in\{\pm1\},
\]
as actual monopole classes.

For any metric, average the positive-projection squares over all sign choices:
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(K_X^+)^2+\sum_{i=1}^k(E_i^+)^2
\ge (K_X^+)^2.
\]
Since \((K_X^-)^2\le0\),
\[
(K_X^+)^2\ge K_X^2=A.
\]
Hence at least one sign choice satisfies
\[
p=(a_\varepsilon^+)^2\ge A.
\]
The sign may depend on the conformal class, which is permitted by both endpoint theorems.

Also,
\[
a_\varepsilon^2
=K_X^2+\sum_iE_i^2
=A-k.
\]
For the complex orientation,
\[
T_+(X)=2\chi(X)+3\tau(X)=c_1^2(X)=A,
\]
and each blow-up decreases \(T_+\) by one. Therefore
\[
\boxed{a_\varepsilon^2=T_+(M)=A-k.}
\]

### The two \(k\)-regimes

If
\[
k\ge\frac3{10}A,
\]
then
\[
T_+(M)=A-k\le\frac7{10}A.
\]
Theorem L′ with \(\theta=7/10\) gives the desired estimate with \(c_L(7/10)\).

Now suppose
\[
k<\frac3{10}A.
\]
Let \(q=h^{1,0}(X)\) and \(\chi_h=1-q+p_g\). Noether’s inequality gives
\[
A=K_X^2\ge2p_g-4=2\chi_h+2q-6.
\]
Thus
\[
\chi_h\le\frac{A-2q+6}{2}.
\]
Using \(c_2(X)=12\chi_h-A\),
\[
c_2(X)\le5A+36-12q.
\]
A blow-up increases the topological Euler characteristic by one, so
\[
\chi(M)=c_2(X)+k
<5A+36-12q+\frac3{10}A.
\]
Since \(q\ge0\) and \(A\) is a positive integer,
\[
\boxed{
\frac{\chi(M)}A
\le\frac{53}{10}+\frac{36}{A}
\le\frac{413}{10}=41.3.
}
\]
The finite-density endpoint theorem applies with \(B=413/10\).

Consequently one may take
\[
\boxed{
c_K=
\min\left\{
c_L\!\left(\frac7{10}\right),
c_{\rm FD}\!\left(\frac{413}{10}\right)
\right\}>0.
}
\]

Thus Corollary K is correct under its stated assumptions. The broader sentence “no counterexample can be Kähler” is established here only for minimal Kähler surfaces of general type with \(p_g\ge1\) and their blow-ups; other Kähler surfaces require their own monopole and topological inputs.