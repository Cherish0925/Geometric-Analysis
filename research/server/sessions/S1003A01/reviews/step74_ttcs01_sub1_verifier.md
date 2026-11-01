# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/notes/spirit_step72_orbifold_scalar_transfer.md",
    "Sessions/S1003A01/workspace/notes/spirit_step73_mixed_curvature_transfer.md"
  ]
}
```

## Task

Verify, as a mathematician, the theorems in step74_orbifold_transfer_theorem.md. Focus on load-bearing points: (1) Theorem 74.A lower bound: is the use of A02's Lemma 86.S to transfer S>=32pi^2 A from smooth resolution metrics on X#kCPbar^2 to every orbifold metric on V_m=X#m(S^4/Z2) valid (orientation matching of Eguchi-Hanson so the resolution really is X#2m CPbar^2; chi_orb=A/3-m; tau_orb=A/9 with zero A1 eta; Gauss-Bonnet normalization 16pi^2 chi = S/12+2W-P)? Is the convex-combination argument for D_orb>=min{1,4k/(A+k)} correct? (2) Upper construction: is h=(1+r^-2)^2 delta with involution x->diag(-1,-1,-1,1)x/|x|^2 really the Green blow-up of S^4/Z2 at a regular point, with A1 points of the correct orientation type for the resolution topology, and are the gluing estimates with rho=eps^{1/2} correct (decay order 2 end, CH background normal coordinates)? Does the glued orbifold have the topology V_m? (3) Theorem 74.B mixed transfer: is the limit argument correct, in particular the treatment of the monopole class depending on the metric and the cross term int s|W+|? Is B_+=-2pi^2 c_+ for Ricci-flat fillers consistent with the charge convention c_pm=2/|Gamma|-2chi-+3tau-+3eta and P(N)=4I_pm+S/12+8pi^2 c_pm? (4) Theorem 74.C: Einstein Chern-Weil I_pm=2pi^2(T_pm - x), x=S/96pi^2; the Cauchy-Schwarz bound for constant s<0; the formulas T_+=A-k+C_+, T_-=A/3+5k+C_-; the large-A linear form 9C_-+2C_++42k>=0; exact x_min=(A/27)[4-sqrt(1-3k/A)]^2; and Corollary 74.D for Ricci-flat Kahler fillers (c_+=0, c_-=-4(chi-1/|Gamma|)). (5) The equality-structure paragraph for possible minimizers. Report any error with a corrected statement, and say which statements are fully proved vs. need extra hypotheses (e.g. b^+(X)=1 chamber issues, regularity of orbifold metrics).

## Output

# Mathematical verification memo

## Summary

The main formulas in Theorems 74.A–74.D are mathematically consistent. Under the stated smooth Seiberg–Witten supply hypothesis and the convergence/topology content attributed to A02 Lemmas 86.S/86.S′, the lower bounds in 74.A, the mixed transfer in 74.B, and the Einstein-bulk inequalities in 74.C are proved.

The Green-cap upper construction is also valid, with one presentational repair: \((1+\varepsilon ^2|y|^{-2})^2\delta\) describes the ordinary AE end of the quotient cap, not the entire cap core. The scaled quotient core must be glued in behind that end.

There is one substantive error in the equality paragraph:

- a minimizer of \(P\) need not have constant scalar curvature from the displayed argument;
- constancy follows for a minimizer of \(\mathscr D\) when \(4k/(A+k)<1\), because equality then forces \(L_s=0\).

Also, the phrase “Kähler–Einstein metric with nonzero trace-free Ricci” is internally incompatible: an Einstein metric has \(\operatorname{Ric}^{\circ}=0\). The equality argument produces only the Kähler-type norm identity
\[
|W^+|^2=\frac{s^2}{24},
\]
not a Kähler structure or an Einstein equation.

---

## 1. Theorem 74.A: lower bound

### 1.1 Orbifold characteristic numbers

Let \(O=S^4/\mathbb Z_2\), where the action has two isolated \(A_1\) points. Since \(O\) is a global quotient,
\[
\chi_{\mathrm{orb}}(O)=\frac{\chi(S^4)}2=1.
\]
Regular-point connected sum satisfies
\[
\chi_{\mathrm{orb}}(Y\#O)=\chi_{\mathrm{orb}}(Y)+1-2
=\chi_{\mathrm{orb}}(Y)-1.
\]
Therefore
\[
\chi_{\mathrm{orb}}(V_m)=\chi(X)-m=\frac A3-m.
\]

The round quotient is conformally flat, so its analytic orbifold signature is zero. Equivalently, the signature \(\eta\)-invariant of the \(A_1\) link \(L(2,1)=\mathbb{RP}^3\) is zero. Hence
\[
\tau_{\mathrm{orb}}(V_m)=\tau(X)=\frac A9.
\]

These formulas are correct.

### 1.2 Orientation of the Eguchi–Hanson resolutions

At each singular point the local action is \(-I\) on an oriented copy of \(\mathbb R^4\). With the standard complex orientation, Eguchi–Hanson has
\[
\chi=2,\qquad \tau=-1,\qquad \eta_{\mathbb{RP}^3}=0,
\]
and
\[
(c_+,c_-)=(0,-6).
\]
Thus resolving the two singularities contributed by one copy of \(O\) changes the smooth characteristic numbers by
\[
\Delta\chi
=2\left(2-\frac12\right)-1=2,\qquad
\Delta\tau=2(-1)=-2
\]
relative to \(X\). This agrees with
\[
X\#2\overline{\mathbb{CP}}^{\,2}.
\]

The characteristic-number computation alone does not identify a diffeomorphism type, but the standard oriented resolution of this quotient region is
\[
\big(\overline{\mathbb{CP}}^{\,2}\#
\overline{\mathbb{CP}}^{\,2}\big)\setminus B^4.
\]
Thus the topology asserted in the note is correct if Lemma 86.S contains the stated oriented resolution identification:
\[
V_m\rightsquigarrow X\#2m\overline{\mathbb{CP}}^{\,2}.
\]

Using the opposite Eguchi–Hanson orientation would interchange chirality and give the wrong smooth resolution, so orientation matching is essential.

### 1.3 Transfer of the scalar estimate

For a \(C^\infty\) orbifold metric in local quotient charts, equivariant normal coordinates give
\[
g=\delta+O(r^2).
\]
If Lemma 86.S produces smooth metrics \(g_\varepsilon\) on
\[
M_k=X\#k\overline{\mathbb{CP}}^{\,2},\qquad k=2m,
\]
with
\[
S(g_\varepsilon)\longrightarrow S(g),
\]
then the smooth all-metric estimate
\[
S(g_\varepsilon)\ge 32\pi^2A
\]
passes directly to
\[
S(g)\ge32\pi^2A.
\]

No convergence of monopole classes is involved here. What is required is that the smooth estimate apply to every recovery metric \(g_\varepsilon\). For \(b^+(X)\ge2\), the usual blow-up classes and convexity give the advertised supply. When \(b^+(X)=1\), an explicit chamber statement applying to every recovery metric is still required; the parenthetical comment in the note should be read as part of hypothesis (SW), not as an automatic consequence.

### 1.4 Chern–Weil lower bound

With the stated normalization,
\[
16\pi^2\chi_{\mathrm{orb}}
=\frac S{12}+2W-P,
\qquad
12\pi^2\tau_{\mathrm{orb}}=I_+-I_-.
\]
Since \(I_\pm\ge0\),
\[
W=I_++I_-\ge |I_+-I_-|
=12\pi^2\tau_{\mathrm{orb}}
=\frac{4\pi^2A}{3}.
\]

Set
\[
\sigma=S-32\pi^2A,\qquad
w=W-\frac{4\pi^2A}{3}.
\]
Then \(\sigma,w\ge0\), and substitution of
\(\chi_{\mathrm{orb}}=A/3-k/2\) gives
\[
P=8\pi^2k+\frac{\sigma}{12}+2w.
\]
Since \(R=P+S/4\),
\[
R=8\pi^2(A+k)+\frac{\sigma}{3}+2w.
\]

Now
\[
\frac{4P}{R}
=
\frac{
\frac{4k}{A+k}\,8\pi^2(A+k)
+1\cdot\frac{\sigma}{3}
+4\cdot2w
}{
8\pi^2(A+k)+\frac{\sigma}{3}+2w
}.
\]
This is exactly a weighted mean of
\[
\frac{4k}{A+k},\qquad 1,\qquad 4
\]
with weights \(8\pi^2(A+k),\sigma/3,2w\). Therefore
\[
\mathscr D(g)
=\frac{4P+L_s}{R}
\ge\frac{4P}{R}
\ge\min\left\{1,\frac{4k}{A+k}\right\}.
\]

The denominator is automatically positive because \(A+k>0\). Also,
\[
P\ge8\pi^2k>0
\]
excludes an Einstein orbifold metric. This part of Theorem 74.A is complete under (SW) and the resolution convergence from Lemma 86.S.

---

## 2. Green-football upper construction

### 2.1 Green-function interpretation

Write the round metric on \(S^4\setminus\{\infty\}\) as
\[
g_{S^4}=\frac{4}{(1+r^2)^2}\delta.
\]
Define
\[
\Phi(r)=\frac{(1+r^2)(1+r^{-2})}{2}.
\]
Then
\[
\Phi^2g_{S^4}=(1+r^{-2})^2\delta=h.
\]
The function \(\Phi\) is, up to normalization, the sum of the two conformal-Laplacian Green kernels with poles at \(0\) and \(\infty\). Thus \(h\) is the two-ended Green blow-up of the round sphere at those antipodal points.

The map
\[
\iota(x)=\sigma\frac{x}{|x|^2},
\qquad
\sigma=\operatorname{diag}(-1,-1,-1,1),
\]
has the following properties:

1. inversion reverses orientation in dimension four, and \(\det\sigma=-1\), so their composition preserves orientation;
2. \(\iota^2=1\);
3. \(r\mapsto r^{-1}\), so the two AE ends are exchanged;
4. the fixed points are exactly
   \[
   (0,0,0,\pm1);
   \]
5. at each fixed point,
   \[
   D\iota=-I.
   \]

Consequently the quotient has exactly two standard oriented \(A_1\) points. The orbit \(\{0,\infty\}\) becomes one regular point of \(S^4/\mathbb Z_2\). Therefore
\[
G=(\mathbb R^4\setminus\{0\},h)/\langle\iota\rangle
\]
is indeed the Green blow-up of \(O=S^4/\mathbb Z_2\) at a regular point.

### 2.2 Curvature calculation

The script calculation can also be verified directly. If \(u=1+r^{-2}\), then \(h=u^2\delta\) is scalar-flat because \(u\) is harmonic away from the origin. It is conformally flat, so \(W_h=0\). In warped coordinates one obtains
\[
|\operatorname{Ric}^{\circ}_h|^2
=\frac{192r^8}{(1+r^2)^8}.
\]
Thus
\[
|\operatorname{Ric}^{\circ}_h|
=8\sqrt3\,r^{-4}+O(r^{-6}),
\]
and
\[
P(h)=32\pi^2.
\]
More precisely,
\[
\int_{r>R}|\operatorname{Ric}^{\circ}_h|^2\,d\mu_h
=
\frac{96\pi^2}{(R^2+1)^2}
-\frac{64\pi^2}{(R^2+1)^3}
=
96\pi^2R^{-4}+O(R^{-6}).
\]

Orbifold integration over the quotient divides the total energy by two:
\[
P(G)=16\pi^2.
\]

### 2.3 Gluing estimate

On the ordinary AE end of the scaled quotient cap, the metric is
\[
g_{\mathrm{cap},\varepsilon}
=(1+\varepsilon^2r^{-2})^2\delta.
\]
The formula should be stated only on the AE coordinate region. For \(r\lesssim\varepsilon\), one inserts the scaled quotient core containing the two \(A_1\) points.

On the transition annulus \(r\asymp\rho\),
\[
|\partial^j(g_X-\delta)|
\le C\rho^{2-j},
\]
while
\[
|\partial^j(g_{\mathrm{cap},\varepsilon}-\delta)|
\le C\left(
\varepsilon^2\rho^{-2-j}
+\varepsilon^4\rho^{-4-j}
\right),
\qquad j\le2.
\]
For \(\rho=\varepsilon^{1/2}\), the metric perturbations are \(O(\varepsilon)\), first derivatives are \(O(\varepsilon^{1/2})\), and second derivatives are \(O(1)\). Hence curvature is \(O(1)\) on an annulus of volume
\[
O(\rho^4)=O(\varepsilon^2).
\]
Its contributions to \(S,W,P\) are therefore \(O(\varepsilon^2)\).

The removed cap tail begins at
\[
R=\rho/\varepsilon=\varepsilon^{-1/2},
\]
so its \(P\)-energy is
\[
O(R^{-4})=O(\varepsilon^2).
\]
Thus each inserted quotient cap contributes
\[
P=16\pi^2+O(\varepsilon^2),\qquad S=O(\varepsilon^2),\qquad W=O(\varepsilon^2).
\]

Since the complex-hyperbolic metric satisfies
\[
P(g_X)=0,\qquad
S(g_X)=32\pi^2A,\qquad
W(g_X)=I_+(g_X)=\frac{4\pi^2A}{3},
\]
one gets
\[
P(g_\varepsilon)\to16\pi^2m=8\pi^2k,
\]
\[
S(g_\varepsilon)\to32\pi^2A,\qquad
W(g_\varepsilon)\to\frac{4\pi^2A}{3}.
\]
The scalar curvature is zero on the cap core and equals the constant scalar curvature of \(g_X\) away from the shrinking regions, so
\[
\operatorname{Vol}(g_\varepsilon)\to\operatorname{Vol}(g_X),
\qquad
\int s_{g_\varepsilon}\to s_X\operatorname{Vol}(g_X),
\]
and consequently
\[
L_s(g_\varepsilon)
=S(g_\varepsilon)
-\frac{\left(\int s_{g_\varepsilon}\right)^2}
{\operatorname{Vol}(g_\varepsilon)}
\longrightarrow0.
\]

Hence
\[
\mathscr D(g_\varepsilon)\longrightarrow
\frac{4k}{A+k}.
\]

Topologically, gluing \(m\) copies of \(G=O\setminus B^4\) into \(m\) ordinary balls in \(X\) gives
\[
X\#mO=V_m.
\]
The cylinder construction at an ordinary point gives \(\mathscr D\to1\). Therefore
\[
\inf_{\mathscr G_{\mathrm{orb}}(V_m)}P=8\pi^2k,
\qquad
\alpha_{\mathrm{orb}}(V_m)
=\min\left\{1,\frac{4k}{A+k}\right\}.
\]

After the core/end wording repair, the upper construction is complete.

---

## 3. Theorem 74.B: mixed curvature transfer

For each recovery metric \(g_\varepsilon\), hypothesis (SW) supplies some class \(\mathbf a_\varepsilon\) with
\[
(\mathbf a_\varepsilon^+)^2\ge A.
\]
The cited smooth estimate then gives
\[
\int_{M_k}
\left(s_{g_\varepsilon}
-\sqrt6\,|W^+_{g_\varepsilon}|\right)^2
\ge72\pi^2A.
\]
Only the numerical right-hand side is used. The classes may vary with \(\varepsilon\).

Expanding the left-hand side gives
\[
S(g_\varepsilon)
-2\sqrt6\int s_{g_\varepsilon}|W^+_{g_\varepsilon}|
+6I_+(g_\varepsilon).
\]
On the scaled filler cores, \(s=0\). On transition annuli \(A_\varepsilon\),
\[
\left|
\int_{A_\varepsilon}s\,|W^+|
\right|
\le
\left(\int_{A_\varepsilon}s^2\right)^{1/2}
\left(\int_{A_\varepsilon}|W^+|^2\right)^{1/2}.
\]
Thus the cross term tends to zero whenever the scalar energy of the annuli tends to zero and their Weyl energy stays bounded. The gluing estimates used in 86.S/86.S′ give the stronger statement that both annular energies tend to zero.

It follows that
\[
S(g_\varepsilon)\to S(g),
\]
\[
I_+(g_\varepsilon)\to I_+(g)+B_+,
\]
and
\[
\int s_{g_\varepsilon}|W^+_{g_\varepsilon}|
\to
\int_V s_g|W^+_g|.
\]
Therefore
\[
\int_V(s-\sqrt6|W^+|)^2+6B_+
\ge72\pi^2A.
\]

For a Ricci-flat filler,
\[
P(N)=S(N)=0.
\]
The charge identity
\[
P(N)=4I_+(N)+\frac{S(N)}{12}+8\pi^2c_+(N)
\]
then gives
\[
I_+(N)=-2\pi^2c_+(N),
\]
hence
\[
B_+=-2\pi^2C_+.
\]
The transferred inequality becomes
\[
\int_V(s-\sqrt6|W^+|)^2
\ge72\pi^2A+12\pi^2C_+.
\]

Theorem 74.B is therefore correct under the stated ALE decay and annular \(L^2\)-curvature properties.

---

## 4. Theorem 74.C

### 4.1 Einstein Chern–Weil formulas

For an Einstein orbifold, \(P=0\). Set
\[
x=\frac{S}{96\pi^2}.
\]
Combining Gauss–Bonnet and signature gives
\[
T_+=2\chi_{\mathrm{orb}}+3\tau_{\mathrm{orb}}
=x+\frac{I_+}{2\pi^2},
\]
\[
T_-=2\chi_{\mathrm{orb}}-3\tau_{\mathrm{orb}}
=x+\frac{I_-}{2\pi^2}.
\]
Hence
\[
I_\pm=2\pi^2(T_\pm-x).
\]

Scalar transfer and \(I_\pm\ge0\) imply
\[
\frac A3\le x\le\min(T_+,T_-).
\]

The assertion that the Einstein constant satisfies \(\lambda<0\) is imported from Lemma 86.S. It is not needed for inequality (3.1), because pointwise
\[
(s-\sqrt6|W^+|)^2
\le (|s|+\sqrt6|W^+|)^2
\]
for either sign of \(s\).

### 4.2 Cauchy–Schwarz calculation

Since \(s\) is constant,
\[
\int(|s|+\sqrt6|W^+|)^2
\le
\left(\sqrt S+\sqrt{6I_+}\right)^2.
\]
Using
\[
S=96\pi^2x,\qquad
I_+=2\pi^2(T_+-x),
\]
the right-hand side is
\[
12\pi^2
\left[\sqrt{8x}+\sqrt{T_+-x}\right]^2.
\]
Combining this with Theorem 74.B gives
\[
\left[\sqrt{8x}+\sqrt{T_+-x}\right]^2
\ge6A+C_+.
\]
Equation (3.1) is correct.

The function
\[
f(x)=\left[\sqrt{8x}+\sqrt{T_+-x}\right]^2
\]
is concave and satisfies
\[
f(x)\le9T_+,
\]
with equality at
\[
x=\frac{8T_+}{9}.
\]
Thus clipping \(8T_+/9\) to the allowed interval is the correct maximization procedure.

### 4.3 Charge formulas for \(T_\pm\)

For
\[
M_k=X\#k\overline{\mathbb{CP}}^{\,2},
\]
one has
\[
T_+(M_k)=A-k,\qquad
T_-(M_k)=\frac A3+5k.
\]
Charge additivity gives
\[
T_+(V)=A-k+C_+,
\qquad
T_-(V)=\frac A3+5k+C_-.
\]
These formulas agree with the paired-\(A_1\) computation, where
\[
C_+=0,\qquad C_-=-6k,
\]
giving
\[
T_+(V_m)=A-k,\qquad
T_-(V_m)=\frac A3-k.
\]

### 4.4 Large-\(A\) expansion

Put
\[
e=C_+-k,\qquad d=C_-+5k.
\]
Then
\[
T_+=A+e,\qquad T_-=\frac A3+d.
\]
For fixed \(k,C_\pm\) and large \(A\), the upper endpoint \(x=T_-\) is active. Expansion there gives
\[
f(T_-)-(6A+C_+)
=
9C_-+2C_++42k
-\frac{3(e-3d)^2}{4A}
+O\!\left(\frac{(|e|+|d|)^3}{A^2}\right).
\]
Thus the leading relations are
\[
C_-+5k\ge0,
\qquad
9C_-+2C_++42k\ge0.
\]
The text’s \(O(k^2/A)\) notation is justified only when \(C_\pm=O(k)\). A cleaner formulation is
\[
9C_-+2C_++42k+O(k^2/A)\ge0.
\]
The displayed second-order term also explains why a configuration with zero leading linear term can still miss the exact finite-\(A\) inequality.

### 4.5 Exact \(C_+=0\) formula

When \(C_+=0\),
\[
T_+=A-k.
\]
Solving
\[
\left[\sqrt{8x}+\sqrt{A-k-x}\right]^2=6A
\]
for the smaller root gives
\[
x_{\min}
=\frac A{27}
\left(4-\sqrt{1-\frac{3k}{A}}\right)^2.
\]
A real root requires
\[
k\le\frac A3.
\]
For this range, \(T_+\ge x_{\min}\), so the remaining exact requirement is
\[
T_-\ge x_{\min}.
\]

Let
\[
t=\sqrt{1-\frac{3k}{A}}.
\]
Then
\[
x_{\min}-\frac{A+k}{3}
=\frac{4A}{27}(1-t)^2.
\]
For \(k>0\), this is strictly positive. Hence
\[
C_-
\ge x_{\min}-\frac A3-5k
>-\frac{14k}{3}.
\]
All formulas in this part are correct.

---

## 5. Corollary 74.D

For a Ricci-flat Kähler ALE filler in its complex orientation,
\[
W^+=0.
\]
The \(+\) charge identity gives
\[
c_+=0.
\]
The ALE Gauss–Bonnet energy is
\[
I_-=8\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right),
\]
and the \(-\) charge identity gives
\[
c_-=-4\left(\chi(N)-\frac1{|\Gamma|}\right).
\]

Writing
\[
Q=\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right),
\]
the inequality \(T_-\ge x_{\min}\) becomes
\[
Q\le
\frac14\left(\frac A3+5k-x_{\min}\right).
\]
Its expansion is
\[
Q\le
\frac{7k}{6}
-\frac{k^2}{12A}
-\frac{k^3}{8A^2}
+O\!\left(\frac{k^4}{A^3}\right).
\]
Thus the asymptotic expression in the note is correct.

The statement that a filler with \(b_2=r\) contributes at least \(r+\tfrac12\) uses the standard ALE topology
\[
\chi(N)=1+b_2(N)
\]
and a nontrivial group at infinity, so \(1/|\Gamma|\le1/2\). Under those assumptions,
\[
\chi(N)-\frac1{|\Gamma|}
=r+1-\frac1{|\Gamma|}
\ge r+\frac12.
\]

---

## 6. Correct equality structure

Suppose first that
\[
P=8\pi^2k.
\]
Then the identity
\[
P=8\pi^2k+\frac{\sigma}{12}+2w
\]
forces
\[
\sigma=w=0.
\]
Therefore
\[
S=32\pi^2A,\qquad I_-=0,\qquad
I_+=\frac{4\pi^2A}{3}.
\]

For the Eguchi–Hanson resolution, \(B_+=0\), so Theorem 74.B gives
\[
F:=\int(s-\sqrt6|W^+|)^2\ge72\pi^2A.
\]
On the other hand,
\[
F\le
H:=\int(|s|+\sqrt6|W^+|)^2
\le
\left(\sqrt S+\sqrt{6I_+}\right)^2
=72\pi^2A.
\]
Hence equality holds throughout. Equality in Cauchy–Schwarz gives
\[
|W^+|=\frac{|s|}{\sqrt{24}}
\]
pointwise, and equality \(F=H\) gives
\[
s\le0.
\]
Thus every \(P\)-minimizer would satisfy
\[
W^-=0,\qquad
s\le0,\qquad
|W^+|^2=\frac{s^2}{24},\qquad
P=8\pi^2k.
\]
The displayed reasoning does **not** make \(s\) constant.

Now suppose
\[
\mathscr D=\frac{4k}{A+k}<1,
\]
equivalently \(k<A/3\). Equality in the weighted-mean lower bound forces
\[
\sigma=w=0,
\]
and equality in
\[
\mathscr D\ge\frac{4P}{R}
\]
forces
\[
L_s=0.
\]
Therefore \(s\) is constant. Since \(S>0\) and the mixed-equality argument gives \(s\le0\),
\[
s<0.
\]
A \(\mathscr D\)-minimizer below one would therefore satisfy
\[
W^-=0,\qquad
s\equiv\text{constant}<0,\qquad
|W^+|^2=\frac{s^2}{24},\qquad
P=8\pi^2k>0.
\]

The norm identity is the familiar Kähler-type relation for \(W^+\), but by itself it neither constructs an almost-complex structure nor determines the eigenvalue structure of \(W^+\). It should not be described as Kähler–Einstein, especially because \(P>0\).

---

## 7. Proof status and remaining assumptions

| Result | Mathematical status |
|---|---|
| 74.A scalar and \(P\) lower bounds | Complete from (SW), the oriented resolution \(V_m\rightsquigarrow M_{2m}\), and \(S(g_\varepsilon)\to S(g)\). |
| 74.A normalized lower bound | Complete; the weighted-mean calculation is exact. |
| 74.A Green-cap upper bound | Complete after specifying that the radial formula describes the AE end and that the scaled quotient core is inserted behind it. |
| Exact \(\inf P\) and \(\alpha_{\mathrm{orb}}\) | Complete once the regular-point cylinder family giving \(\mathscr D\to1\) is included. |
| 74.B mixed transfer | Complete for scalar-flat ALE fillers with the stated decay, vanishing annular scalar energy, bounded annular Weyl energy, and \(I_+\)-energy convergence. |
| 74.C algebra and optimization | Complete; all constants and chiral formulas are correct. |
| Assertion \(\lambda<0\) | Depends on the cited conclusion of Lemma 86.S; it is not needed to derive (3.1). |
| 74.D budget | Complete as a necessary Einstein-bulk inequality for orientation-matched Ricci-flat Kähler fillers. |
| Equality paragraph | Requires the correction above: scalar constancy belongs only to a \(\mathscr D\)-minimizer below one, not to a \(P\)-minimizer from the given argument. |

Finally, “all smooth orbifold metrics” should mean compact oriented effective orbifolds with isolated quotient points and \(C^\infty\) invariant lifts in uniformizing charts. Extending the statements to rough metrics would require a separate approximation and lower-semicontinuity argument. The catalogue statements produced by `step74_neck_and_screen.py` are verified on the finite list of \(A\)-values coded there; assertions for every admissible \(A\) require either an analytic monotonicity argument or exact symbolic inequalities beyond that sampled list.