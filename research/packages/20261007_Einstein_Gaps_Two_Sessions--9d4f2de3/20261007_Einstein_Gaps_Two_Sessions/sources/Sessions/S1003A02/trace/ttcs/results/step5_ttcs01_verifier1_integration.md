# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 5,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step5_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the proposed density-free endpoint Theorem L and Corollary K in the Step 4 note. Verify the exact rewriting of V kappa_beta; all inequality directions; the optimized gamma and coefficient a(theta,beta); the discriminant and thresholds theta=2/3, beta=8, theta=3/4; and, crucially, close the proof for every original metric by using the actual conformal-monopole hypotheses, Yamabe normalization, conformal transfer, and the finite-parameter theorem with its true b=(-a^2)_+/V factor. State an exact corrected theorem and proof if valid, and flag any quantifier/constant flaw. Also verify the Kähler blow-up corollary's p>=A, a^2=T_+, Noether density calculation and universal constant under its stated p_g hypothesis.

## Integrated Scientific Memo

# Verification memo: corrected Theorem L and Corollary K

## 1. Verdict

The proposed density-free endpoint theorem is valid under the stated actual conformal-monopole supply, but the Step 4 proof is incomplete for arbitrary original metrics until the Yamabe normalization and conformal-transfer argument is inserted.

The exact algebra, inequality directions, optimized \(\gamma\), coefficient \(a(\theta,\beta)\), discriminant, and thresholds \(2/3,8,3/4\) are correct, with one textual correction:

- at \(\theta=2/3\), the numerator is nonnegative and has a single double zero at \(\beta=8\); it is not negative on an interval.

The finite-parameter theorem must be used with its actual factor
\[
b=\frac{(-a^2)_+}{V}.
\]
In the branch where it is needed, \(T_+>0\) and \(a^2\ge T_+\), hence \(a^2>0\) and \(b=0\) exactly.

In fact, under \(T_+\le\theta A\) with fixed \(\theta<3/4\), the proof gives the stronger conclusion
\[
\kappa_\beta(g)\ge c_0(\theta)>0
\qquad(\beta\ge2),
\]
and therefore also the stated weaker bound with the factor \((\beta-2)^2/\beta^2\).

The Kähler blow-up corollary is correct under its stated \(p_g\ge1\) hypothesis. Its universal constant is
\[
c_K=\min\{c_L(7/10),\,c_{\mathrm{FD}}(413/10)\}>0.
\]

---

## 2. Exact rewriting and signs

Put
\[
Q=\int_M\frac{(s+4)^2}{4}.
\]
Since
\[
\Ric+g=\Ric^\circ+\frac{s+4}{4}g,
\qquad
|\Ric+g|^2=|\Ric^\circ|^2+\frac{(s+4)^2}{4},
\]
we have
\[
V\kappa_\beta=P+Q+D_\beta.
\]
Using
\[
4\pi^2T_+=\frac S{24}+2W-\frac P2,
\qquad
P=\frac S{12}+4W-8\pi^2T_+,
\]
gives
\[
\boxed{
V\kappa_\beta
=
\left(\frac{13}{12}+\frac1\beta\right)S
 +(6\beta+10)W+Q
 -8\pi^2T_+-72\pi^2p.
}
\tag{2.1}
\]

LeBrun’s estimate and Young’s inequality imply, for every \(\gamma>0\),
\[
72\pi^2p
\le \int(s-\sqrt6|W^+|)^2
\le (1+\gamma^{-1})S+6(1+\gamma)W.
\tag{2.2}
\]

Suppose \(T_+\ge0\) and \(T_+\le\theta A\). Since \(p\ge A\),
\[
T_+\le\theta p.
\]
Writing
\[
\lambda=1+\frac{\theta}{9},
\]
one obtains
\[
-8\pi^2T_+-72\pi^2p
\ge-72\pi^2\lambda p.
\]
Multiplying (2.2) by \(-\lambda\) reverses the inequality:
\[
-72\pi^2\lambda p
\ge
-\lambda(1+\gamma^{-1})S
-6\lambda(1+\gamma)W.
\]
Therefore
\[
V\kappa_\beta\ge Q+
\left[\frac{13}{12}+\frac1\beta-\lambda(1+\gamma^{-1})\right]S
+\left[6\beta+10-6\lambda(1+\gamma)\right]W.
\tag{2.3}
\]

To keep the \(W\)-coefficient nonnegative one needs
\[
\gamma\le\gamma_{\max}
=\frac{9\beta-\theta+6}{9+\theta}.
\]
The \(S\)-coefficient increases with \(\gamma\), so this is the optimal admissible choice. It cancels the \(W\)-term and yields
\[
V\kappa_\beta\ge a(\theta,\beta)S+Q,
\tag{2.4}
\]
where
\[
\boxed{
a(\theta,\beta)=
\frac{
(\frac34-\theta)\beta^2+
(\frac12-\frac{11}{4}\theta)\beta+
6-\theta
}{
\beta(9\beta-\theta+6)
}.
}
\tag{2.5}
\]

For \(a>0\),
\[
as^2+\frac{(s+4)^2}{4}
\ge\frac{16a}{1+4a};
\]
the minimum is attained at \(s=-4/(1+4a)\). Thus
\[
\boxed{
\kappa_\beta\ge\frac{16a(\theta,\beta)}
 {1+4a(\theta,\beta)}
}
\tag{2.6}
\]
whenever \(a(\theta,\beta)>0\).

All inequality directions in this computation are correct.

---

## 3. Discriminant and the three thresholds

Let
\[
N_\theta(\beta)
=
\left(\frac34-\theta\right)\beta^2
+\left(\frac12-\frac{11}{4}\theta\right)\beta
+6-\theta.
\]
Then
\[
a(\theta,\beta)=\frac{N_\theta(\beta)}
{\beta(9\beta-\theta+6)}.
\]
Its discriminant is
\[
\begin{aligned}
\Delta(\theta)
&=
\left(\frac12-\frac{11}{4}\theta\right)^2
-4\left(\frac34-\theta\right)(6-\theta)\\
&=\frac{57}{16}\theta^2+\frac{97}{4}\theta-\frac{71}{4}\\
&=\boxed{\frac{57}{16}
\left(\theta-\frac23\right)
\left(\theta+\frac{142}{19}\right)}.
\end{aligned}
\tag{3.1}
\]

Consequently:

### \(0\le\theta<2/3\)

Here \(\Delta<0\) and the leading coefficient is positive, so
\[
N_\theta(\beta)>0
\]
for every \(\beta\). Moreover,
\[
a(\theta,\beta)\longrightarrow
\frac1{12}-\frac{\theta}{9}>0.
\]
Hence \(\inf_{\beta\ge2}a(\theta,\beta)>0\).

### \(\theta=2/3\)

Here
\[
\boxed{
N_{2/3}(\beta)=\frac{(\beta-8)^2}{12}.
}
\tag{3.2}
\]
Thus the elementary coefficient vanishes only at the double root
\(\beta=8\). This corrects the note’s phrase that \(N<0\) on an interval at the endpoint \(\theta=2/3\).

### \(2/3<\theta<3/4\)

The two roots are
\[
\boxed{
\beta_\pm(\theta)=
\frac{\frac{11}{4}\theta-\frac12\pm\sqrt{\Delta(\theta)}}
 {2(\frac34-\theta)}.
}
\tag{3.3}
\]
Furthermore,
\[
N_\theta(2)=10-\frac{21}{2}\theta>0,
\qquad
N_\theta(8)=58-87\theta<0,
\]
so
\[
2<\beta_-(\theta)<8<\beta_+(\theta),
\]
and \(N_\theta<0\) precisely on
\[
(\beta_-(\theta),\beta_+(\theta)).
\]
Also \(\beta_+(\theta)\to\infty\) as \(\theta\uparrow3/4\).

### \(\theta=3/4\)

The quadratic term disappears:
\[
N_{3/4}(\beta)
=-\frac{25}{16}\beta+\frac{21}{4},
\]
which is negative for \(\beta>84/25\). Equivalently,
\[
a_\infty(\theta)
:=\lim_{\beta\to\infty}a(\theta,\beta)
=\frac1{12}-\frac{\theta}{9}
\]
is positive exactly for \(\theta<3/4\).

Thus:

- \(2/3\) is the first ratio where an elementary bad parameter appears;
- that parameter is \(\beta=8\);
- \(3/4\) is the large-\(\beta\) threshold.

The Chern–Weil alignment at \(\beta=8\) is also correct:
\[
\boxed{
D_8
=108\pi^2\left(T_+-\frac23p\right)
+\frac{27}{2}P.
}
\tag{3.4}
\]

The JSON formulas are algebraically correct, but its `beta0_first_positive` scan is not informative: when \(2/3<\theta<3/4\), \(a\) is positive near \(\beta=2\), then negative on \((\beta_-,\beta_+)\), then positive again. The roots, not the first positive sample, are the relevant data.

---

## 4. Corrected density-free theorem

### Theorem L′

Fix \(\theta<3/4\). Let \(M\) be a closed connected oriented smooth four-manifold, and let \([g]\) be a conformal class. Suppose a fixed Spin\(^c\) structure with determinant class \(a\) admits an ordinary unperturbed monopole solution for every metric in \([g]\). Put
\[
p=(a_h^+)^2,
\]
which is conformally invariant in dimension four. Assume
\[
p\ge A>0,\qquad a^2\ge T_+,\qquad T_+\le\theta A.
\]
Then there is \(c_L(\theta)>0\), depending only on \(\theta\), such that every \(h\in[g]\) and every finite \(\beta\ge2\) satisfy
\[
\boxed{
\kappa_\beta(h)\ge c_L(\theta).
}
\tag{4.1}
\]
In particular,
\[
\boxed{
\kappa_\beta(h)\ge
c_L(\theta)\frac{(\beta-2)^2}{\beta^2}.
}
\tag{4.2}
\]

No Euler-density hypothesis is used.

If this is stated over all metrics on \(M\), the supplying Spin\(^c\) structure may be selected separately for each conformal class only if the supplier permits that choice; within each class, one fixed structure must supply solutions throughout the class, and the same \(A,\theta\) must work uniformly.

### Proof

#### Case 1: \(T_+\le0\)

Drop the nonnegative term \(-8\pi^2T_+\) and use the preceding argument with \(\theta=0\). Then
\[
a(0,\beta)
=
\frac{\beta^2/4+\beta/6+2}{\beta(3\beta+2)}.
\]
Indeed
\[
12\left(\frac{\beta^2}{4}+\frac{\beta}{6}+2\right)
-\beta(3\beta+2)=24,
\]
so \(a(0,\beta)\ge1/12\). Equation (2.6) gives
\[
\kappa_\beta\ge1.
\tag{4.3}
\]
No condition on \(a^2\) is needed in this case.

#### Case 2: \(T_+>0\) and \(0\le\theta<2/3\)

Because \(p\ge A\),
\[
T_+\le\theta A\le\theta p.
\]
The discriminant analysis shows \(a(\theta,\beta)>0\) for all
\(\beta\ge2\), and its positive limit at infinity implies
\[
\underline a_\theta
:=\inf_{\beta\ge2}a(\theta,\beta)>0.
\]
Hence
\[
\kappa_\beta\ge
\frac{16\underline a_\theta}{1+4\underline a_\theta}>0.
\tag{4.4}
\]
Again, no hypothesis on \(a^2\) is needed.

#### Case 3: \(T_+>0\) and \(2/3\le\theta<3/4\)

Set \(\beta_+(2/3)=8\), use (3.3) when \(\theta>2/3\), and let
\[
B_\theta=2\beta_+(\theta).
\]
For \(\beta\ge B_\theta\), the elementary coefficient is positive. Since it has a positive limit at infinity,
\[
m_\theta:=
\inf_{\beta\ge B_\theta}
\frac{16a(\theta,\beta)}
 {1+4a(\theta,\beta)}>0.
\]
Thus
\[
\kappa_\beta(g)\ge m_\theta
\qquad(\beta\ge B_\theta)
\tag{4.5}
\]
for every original metric \(g\).

It remains to treat
\[
2\le\beta\le B_\theta.
\]

The actual conformal supply and \(p>0\) force the Yamabe constant of \([g]\) to be negative: on a constant-scalar representative with nonnegative scalar curvature, the monopole Weitzenböck identity would force the spinor, and hence \(a^+\), to vanish, contradicting \(p>0\). Let \(\widehat g\in[g]\) be normalized by
\[
s_{\widehat g}=-4.
\]

Write
\[
\delta=S(g)-S(\widehat g)\ge0.
\]
Conformal invariance of \(p\), \(W\), and \(T_+\), together with Chern–Weil, gives
\[
\widehat P=P-\frac{\delta}{12},
\qquad
\widehat D_\beta
=D_\beta-\left(1+\frac1\beta\right)\delta.
\tag{4.6}
\]
Since LeBrun’s estimate with \(\gamma=\beta\) gives \(D_\beta\ge0\) for every metric, in particular
\[
\widehat D_\beta\ge0.
\]
Thus
\[
0\le\delta\le D_\beta\le V\kappa_\beta.
\tag{4.7}
\]

Writing \(e=s_g+4\), the Ricci part gives
\[
\int e^2\le4V\kappa_\beta.
\]
The exact volume identity is
\[
16\widehat V
=16V-8\int e+\int e^2-\delta.
\]
By Cauchy–Schwarz and (4.7),
\[
\frac{\widehat V}{V}
\ge1-\sqrt{\kappa_\beta}-\frac{\kappa_\beta}{16}.
\tag{4.8}
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
\tag{4.9}
\]
whenever the denominator is positive.

Now \(T_+>0\) and \(a^2\ge T_+\), so
\[
a^2>0,
\qquad
b=\frac{(-a^2)_+}{\widehat V}=0.
\tag{4.10}
\]
The true single-parameter theorem therefore gives
\[
\frac{\widehat P}{\widehat V}
+\frac{\widehat D_\beta}{\beta\widehat V}
\ge
c_{\rm par}\frac{(\beta-2)^2}{\beta^4}.
\tag{4.11}
\]
Since \(\widehat D_\beta\ge0\),
\[
\widehat\kappa_\beta
=\frac{\widehat P+\widehat D_\beta}{\widehat V}
\ge
c_{\rm par}\frac{(\beta-2)^2}{\beta^4}.
\tag{4.12}
\]

If \(\kappa_\beta(g)\ge1/16\), there is already a uniform positive lower bound. If \(\kappa_\beta(g)\le1/16\), then
\[
1-\sqrt{\kappa_\beta}-\frac{\kappa_\beta}{16}
\ge
1-\frac14-\frac1{256}
=\frac{191}{256},
\]
so (4.9)–(4.12) imply
\[
\kappa_\beta(g)
\ge
\frac{191}{256}c_{\rm par}
\frac{(\beta-2)^2}{\beta^4}.
\tag{4.13}
\]

This estimate alone degenerates at \(\beta=2\), but the elementary coefficient is strictly positive on a neighborhood of \(\beta=2\): indeed
\[
N_\theta(2)=10-\frac{21}{2}\theta
>10-\frac{63}{8}=\frac{17}{8}.
\]
Hence one may choose a fixed \(\beta_0(\theta)>2\), below the first root when \(\theta>2/3\), such that (2.6) gives a positive uniform bound on
\([2,\beta_0(\theta)]\). On the remaining compact interval
\([\beta_0(\theta),B_\theta]\), the function
\[
\frac{(\beta-2)^2}{\beta^4}
\]
has a positive minimum. Combining this with (4.13), and then with (4.5), yields (4.1).

This proves the theorem. ∎

### Constant dependence

The constant is uniform in the manifold, conformal class, supplying structure, \(A\), metric, and \(\beta\), but it depends essentially on the fixed \(\theta<3/4\). There is no positive constant uniform as \(\theta\uparrow3/4\), since
\[
a_\infty(\theta)=\frac1{12}-\frac{\theta}{9}\downarrow0
\]
and the bad parameter interval becomes unbounded.

The assumption \(a^2\ge T_+\) is only needed in the window
\(2/3\le\theta<3/4\). For \(T_+\le0\) or \(\theta<2/3\), the elementary argument does not use it.

---

## 5. Verification of Corollary K

### Corrected statement

Let \(X\) be a minimal Kähler surface of general type with
\[
p_g(X)\ge1,
\qquad
A=c_1^2(X)>0,
\]
and let
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},
\qquad k\ge0.
\]
Then there is a universal constant \(c_K>0\), independent of
\(X,k,g,\beta\), such that every metric \(g\) on \(M\) and every finite \(\beta\ge2\) satisfy
\[
\boxed{
\kappa_\beta(g)\ge
c_K\frac{(\beta-2)^2}{\beta^2}.
}
\tag{5.1}
\]

### Monopole supply and the projection budget

For a compact Kähler surface,
\[
b_+(X)=1+2p_g(X)\ge3.
\]
Thus the canonical Seiberg–Witten class has no chamber ambiguity, and the iterated blow-up formula supplies basic classes
\[
a_\varepsilon=K_X+\sum_{i=1}^k\varepsilon_iE_i,
\qquad
\varepsilon_i\in\{\pm1\},
\]
as actual monopole classes.

For any metric, averaging over all signs gives
\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(K_X^+)^2+\sum_i(E_i^+)^2
\ge(K_X^+)^2.
\]
Since the anti-self-dual intersection form is negative definite,
\[
(K_X^+)^2\ge K_X^2=A.
\]
Therefore at least one sign choice satisfies
\[
\boxed{p=(a_\varepsilon^+)^2\ge A.}
\tag{5.2}
\]
The signs may depend on the conformal class, but harmonic self-dual projection is conformally invariant, so one selected class works throughout that conformal class.

### Square and \(T_+\)

Because \(E_i^2=-1\) and \(K_X\cdot E_i=0\),
\[
a_\varepsilon^2=K_X^2-k=A-k.
\tag{5.3}
\]
For the complex orientation,
\[
T_+(X)=2\chi(X)+3\tau(X)=c_1^2(X)=A,
\]
and each blow-up changes \((\chi,\tau)\) by \((1,-1)\), hence decreases \(T_+\) by one. Thus
\[
\boxed{
a_\varepsilon^2=T_+(M)=A-k.
}
\tag{5.4}
\]

### Large blow-up regime

If
\[
k\ge\frac3{10}A,
\]
then
\[
T_+(M)=A-k\le\frac7{10}A.
\]
Theorem L′ applies with \(\theta=7/10<3/4\). If \(k\ge A\), then \(T_+\le0\), covered by its first case.

### Bounded-density regime

Suppose
\[
k<\frac3{10}A.
\]
Let \(q=h^{1,0}(X)\) and \(\chi_h=1-q+p_g\). Noether’s inequality gives
\[
A=K_X^2\ge2p_g-4
=2\chi_h+2q-6,
\]
hence
\[
\chi_h\le\frac{A-2q+6}{2}.
\]
Using
\[
c_2(X)=12\chi_h-A,
\]
one gets
\[
c_2(X)\le5A+36-12q.
\tag{5.5}
\]
A blow-up increases the topological Euler characteristic by one, so
\[
\chi(M)=c_2(X)+k
<5A+36-12q+\frac3{10}A.
\]
Since \(q\ge0\) and \(A=c_1^2(X)\) is a positive integer,
\[
\boxed{
\frac{\chi(M)}A
\le\frac{53}{10}+\frac{36}{A}
\le\frac{413}{10}=41.3.
}
\tag{5.6}
\]
The finite-density endpoint theorem therefore applies with
\[
B=\frac{413}{10}.
\]

Consequently,
\[
\boxed{
c_K=
\min\left\{
c_L\!\left(\frac7{10}\right),
c_{\mathrm{FD}}\!\left(\frac{413}{10}\right)
\right\}>0
}
\tag{5.7}
\]
is universal.

---

## 6. Exact flaws and scope restrictions

1. **Missing transfer in the Step 4 proof.**  
   The single-parameter theorem is stated on the \(s=-4\) Yamabe representative. It cannot be applied directly to an arbitrary original metric. Equations (4.6)–(4.13) supply the missing transfer.

2. **True finite-parameter factor.**  
   The theorem is
   \[
   (1+b)\left(\frac PV+\frac{D_\beta}{\beta V}\right)
   \ge c_{\rm par}\frac{(\beta-2)^2}{\beta^4},
   \qquad
   b=\frac{(-a^2)_+}{V}.
   \]
   In the relevant window, \(T_+>0\) and \(a^2\ge T_+\), so \(b=0\). It would be incorrect to suppress this factor without that observation.

3. **Endpoint \(\theta=2/3\).**  
   The elementary numerator is
   \[
   (\beta-8)^2/12.
   \]
   There is a double zero, not a negative interval.

4. **Dependence on \(\theta\).**  
   The theorem provides \(c_L(\theta)>0\) for each fixed
   \(\theta<3/4\). It does not provide a constant uniform as
   \(\theta\uparrow3/4\).

5. **Kähler scope.**  
   The proof covers minimal Kähler surfaces of general type with
   \(p_g\ge1\) and their blow-ups. The broader sentence “no counterexample can be Kähler” is not justified for all Kähler surfaces without separate monopole and topological inputs.

6. **Why Corollary K retains the \((\beta-2)^2\) factor.**  
   The large-blow-up branch has a stronger positive constant, but the bounded-density branch includes \(k=0\) Kähler–Einstein examples for which
   \[
   \kappa_\beta=\frac{4(\beta-2)^2}{\beta}.
   \]
   Thus the corollary’s vanishing at \(\beta=2\) is genuinely necessary.