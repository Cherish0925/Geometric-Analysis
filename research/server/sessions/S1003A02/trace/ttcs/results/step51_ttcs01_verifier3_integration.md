# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 51,
  "task_field": "verifier",
  "task_index": 3,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Theorem K-infinity in the Step-50 note: for the blow-up (including infinitely-near points) of any minimal compact complex surface of general type, is inf over Kähler metrics of P exactly 8π²k and not attained? Check the lower formula and Hodge-index argument for nef non-ample K_X; the Arezzo-Pacard hypotheses on the canonical orbifold and subsequent smooth blow-ups; the Kähler class signs and epsilon expansion; whether negative cscK metrics are Yamabe representatives; and the statement D_W=0, DeltaV→0. Return a precise theorem, scope, and any needed repair.

## Integrated Scientific Memo

## Verification of Theorem \(K_\infty\)

### Correct theorem and scope

Let \(X\) be a minimal compact complex surface of general type, let
\[
A=K_X^2>0,
\]
and let \((M,J)\) be obtained from \(X\) by \(k\) successive complex blow-ups at arbitrary smooth points of the intermediate surfaces. Thus the centers may be distinct or infinitely near. Then
\[
\boxed{\inf_{g\ \mathrm{K\ddot ahler\ for}\ J}
\int_M |\operatorname{Ric}_g^\circ|^2\,d\mu_g=8\pi^2k.}
\]
If \(k\ge1\), every such Kähler metric satisfies the strict inequality
\[
P(g)>8\pi^2k,
\]
so the infimum is not attained.

The qualification “Kähler for the fixed blown-up complex structure \(J\)” is essential. The supplied sources do not establish the same claim when the infimum ranges over Kähler metrics associated with arbitrary complex structures on the underlying smooth four-manifold.

The Step-50 conclusion is therefore correct after repairing the treatment of infinitely-near exceptional classes and the Arezzo–Pacard construction.

---

## 1. Exact Kähler formula

For a Kähler metric \(g\) with Kähler class \(\Omega=[\omega]\), use
\[
d\mu=\frac{\omega^2}{2},\qquad \operatorname{Vol}(g)=\frac{\Omega^2}{2}.
\]
On a Kähler surface,
\[
|W^+|^2=\frac{s^2}{24},
\]
and Chern–Weil gives
\[
P(g)=\int_M|\operatorname{Ric}^\circ|^2\,d\mu
=\frac14\int_Ms^2\,d\mu-8\pi^2c_1^2(M).
\]
Moreover,
\[
\int_Ms\,d\mu=4\pi c_1(M)\cdot\Omega=-4\pi K_M\cdot\Omega,
\]
so
\[
\bar s=-\frac{8\pi K_M\cdot\Omega}{\Omega^2}.
\]
Since
\[
c_1^2(M)=K_M^2=A-k,
\]
splitting \(s=\bar s+(s-\bar s)\) yields
\[
\boxed{
\frac{P(g)}{8\pi^2}
=
\frac{(K_M\cdot\Omega)^2}{\Omega^2}
+\frac1{32\pi^2}\int_M(s-\bar s)^2\,d\mu
-A+k.}
\tag{1}
\]
Thus the formula and coefficient in Step 50 are correct.

---

## 2. Lower bound for nef, non-ample \(K_X\)

For infinitely-near blow-ups, the notation in Step 50 must be corrected.

Let \(e_i\in H^2(M;\mathbb Z)\) denote the **total transform class** of the exceptional divisor introduced at the \(i\)-th blow-up. Then
\[
e_i\cdot e_j=-\delta_{ij},\qquad
\pi^*K_X\cdot e_i=0,\qquad
K_M=\pi^*K_X+\sum_{i=1}^ke_i.
\tag{2}
\]
These statements generally fail if \(e_i\) is interpreted as the irreducible strict transform on the final surface. Each total transform is nevertheless a nonzero effective divisor, hence
\[
e_i\cdot\Omega>0
\tag{3}
\]
for every Kähler class \(\Omega\).

Set \(L=\pi^*K_X\). A minimal surface of general type has \(K_X\) nef and big, so
\[
L^2=A>0.
\]
The Hodge index theorem gives
\[
(L\cdot\Omega)^2\ge L^2\Omega^2=A\Omega^2.
\tag{4}
\]
No ampleness assumption on \(K_X\) is required. Nefness and bigness also give \(L\cdot\Omega>0\). Therefore, when \(k\ge1\),
\[
K_M\cdot\Omega
=L\cdot\Omega+\sum_i e_i\cdot\Omega
>L\cdot\Omega>0,
\]
and hence
\[
\frac{(K_M\cdot\Omega)^2}{\Omega^2}>A.
\]
Equation (1) then gives
\[
\boxed{P(g)>8\pi^2k}
\tag{5}
\]
for every Kähler metric on \((M,J)\). This proves both the lower bound and nonattainment once a recovery sequence is constructed.

A useful quantitative form is obtained by writing
\[
\Omega=tL+\beta,\qquad L\cdot\beta=0.
\]
Then \(t>0\), \(\beta^2\le0\), and with
\[
b=\sum_i e_i\cdot\Omega>0
\]
one has
\[
\frac{P}{8\pi^2}-k
=
\frac{2tAb+b^2+A|\beta^2|}
     {t^2A+\beta^2}
+\frac1{32\pi^2}\int(s-\bar s)^2\,d\mu.
\tag{6}
\]
Consequently any Kähler recovery sequence must simultaneously have vanishing normalized exceptional areas, projective convergence of its class to \(\pi^*K_X\), and vanishing Calabi energy.

---

## 3. Correct use of Arezzo–Pacard

Let
\[
q:X\longrightarrow \bar X
\]
be the canonical-model contraction. The supplied Arezzo–Pacard source provides precisely the following inputs:

1. \(\bar X\) has isolated quotient singularities \(\mathbb C^2/\Gamma_j\) with \(\Gamma_j\subset SU(2)\).
2. \(\bar X\) carries a negative Kähler–Einstein orbifold metric.
3. Its automorphism group is discrete, so it is nondegenerate in the sense required by Theorem 1.3.
4. The \(SU(2)\) singularities admit crepant Ricci-flat ALE resolutions of Kronheimer/Joyce type with the needed asymptotics.
5. Theorem 1.3 therefore produces negative cscK metrics on the minimal resolution \(X\).
6. Theorem 1.1 can then be applied successively at arbitrary smooth points of \(X\) and of every subsequent blow-up.

This last sequential step is essential. A single simultaneous application of Theorem 1.3 on \(\bar X\) does **not** cover:

- blow-up centers lying on the canonical exceptional \((-2)\)-configuration;
- centers lying on previously created exceptional curves;
- general infinitely-near configurations.

The valid construction is:

1. desingularize the canonical model to obtain cscK metrics on \(X\);
2. perform the prescribed smooth blow-ups successively using Theorem 1.1;
3. use independent small parameters and take a diagonal sequence.

Arezzo–Pacard explicitly notes that holomorphic vector fields on a blow-up correspond to vector fields on the base vanishing at the centers. Since the surfaces in question have discrete automorphism group, nondegeneracy persists and the iteration is legitimate.

---

## 4. Kähler classes and the upper limit

Write the orbifold Kähler–Einstein class as
\[
[\omega_{\mathrm{KE}}]=\lambda\,c_1(K_{\bar X}),\qquad \lambda>0.
\]
Crepantness gives \(q^*K_{\bar X}=K_X\). After resolving the canonical singularities, the cscK classes can be written
\[
\Omega_\delta=\lambda K_X+\xi_\delta,
\tag{7}
\]
where
\[
K_X\cdot\xi_\delta=0,\qquad
\xi_\delta^2\le0,\qquad
\xi_\delta\to0.
\tag{8}
\]
The plus sign in (7) is correct: \(\xi_\delta\) has positive areas on the resolution curves despite lying in a negative-definite subspace.

After the prescribed \(k\) smooth blow-ups, the final class has the form
\[
\Omega_{\delta,\mathbf t}
=\pi^*\Omega_\delta-\sum_{i=1}^k t_i e_i,
\qquad t_i>0.
\tag{9}
\]
The minus sign is correct because
\[
\Omega_{\delta,\mathbf t}\cdot e_i=t_i>0.
\]

Let
\[
T=\sum_i t_i,\qquad Q=\sum_i t_i^2.
\]
Using the orthogonal total-transform basis,
\[
K_M\cdot\Omega_{\delta,\mathbf t}
=\lambda A+T,
\qquad
\Omega_{\delta,\mathbf t}^2
=\lambda^2A+\xi_\delta^2-Q.
\tag{10}
\]
The constructed metrics are cscK, so the variance term in (1) vanishes. Hence
\[
\boxed{
\frac{P(\Omega_{\delta,\mathbf t})}{8\pi^2}
=
k+\frac{(\lambda A+T)^2}
        {\lambda^2A+\xi_\delta^2-Q}
-A.}
\tag{11}
\]
Taking \(\delta\to0\) and then all \(t_i\to0\), or choosing a diagonal sequence, gives
\[
P(\Omega_{\delta,\mathbf t})\longrightarrow8\pi^2k.
\tag{12}
\]
Combined with (5), this proves the theorem.

### Status of the \(\varepsilon\)-expansion

If one has a genuinely common scale
\[
\xi_\varepsilon=\varepsilon^2c,\qquad
t_i=\varepsilon^2a_i,
\]
then
\[
\frac{P}{8\pi^2}
=
k+\frac{(\lambda A+\varepsilon^2\sum_i a_i)^2}
{\lambda^2A+\varepsilon^4(c^2-\sum_i a_i^2)}
-A
=
k+\frac{2\varepsilon^2}{\lambda}\sum_i a_i+O(\varepsilon^4).
\tag{13}
\]
Thus the coefficient and sign in Step 50 are correct.

For arbitrary infinitely-near configurations, however, iterated Theorem 1.1 directly supplies a multiparameter family, not necessarily a common-\(\varepsilon\) family with uniform estimates. The proof should therefore use (11)–(12); equation (13) should be presented only under the additional common-scale parametrization.

---

## 5. Negative cscK metrics and Yamabe normalization

Every cscK member of this construction has negative scalar curvature. Indeed,
\[
s=\bar s=-\frac{8\pi K_M\cdot\Omega}{\Omega^2}<0.
\]
A constant negative scalar-curvature metric is the Yamabe minimizer in its conformal class, uniquely up to homothety. This follows from the maximum principle applied to the Yamabe equation after two constant-scalar-curvature representatives are scaled to have the same negative scalar curvature.

Thus these metrics may be rescaled to
\[
s_{\hat g}\equiv-4,
\]
and \(\hat g\) is their Yamabe representative. Constant rescaling preserves the Kähler property and the scale-invariant functional \(P\).

---

## 6. \(D_W\) and \(\Delta V\)

With the complex orientation, every Kähler surface satisfies
\[
|W^+|^2=\frac{s^2}{24}.
\]
After normalizing \(s=-4\),
\[
|W^+|^2=\frac23
\]
pointwise. Therefore, for the Step-50 definition
\[
D_W(\hat g)=\int_M\left(\frac23-|W^+|^2\right)d\mu_{\hat g},
\]
one has
\[
\boxed{D_W(\hat g)=0}
\tag{14}
\]
exactly, not merely asymptotically.

The normalization \(s=-4\) and the average-scalar-curvature formula imply
\[
K_M\cdot\Omega=\frac{\Omega^2}{2\pi}.
\]
Therefore
\[
\frac{(K_M\cdot\Omega)^2}{\Omega^2}
=\frac{\operatorname{Vol}_{\hat g}(M)}{2\pi^2}.
\]
Defining
\[
\Delta V(\hat g)
=\operatorname{Vol}_{\hat g}(M)-2\pi^2A,
\]
equation (1), with \(s\) constant, becomes
\[
\boxed{
\frac{P(\hat g)}{8\pi^2}-k
=\frac{\Delta V(\hat g)}{2\pi^2}.}
\tag{15}
\]
Equivalently,
\[
P(\hat g)-8\pi^2k=4\Delta V(\hat g).
\tag{16}
\]
Hence each actual member has \(\Delta V>0\), while the recovery sequence satisfies
\[
\boxed{\Delta V\to0.}
\tag{17}
\]

These identities apply to the negative cscK recovery family. For a general non-cscK Kähler metric, its Yamabe representative need not remain Kähler, so the same pointwise \(D_W=0\) assertion cannot be transferred automatically.

---

## 7. Required replacement for Step 50, §5

The section should be revised as follows:

- specify that the infimum is over Kähler metrics for the fixed blown-up complex structure;
- use total-transform exceptional classes for infinitely-near blow-ups;
- separate canonical-model desingularization from subsequent smooth blow-ups;
- allow independent gluing parameters and prove convergence through (11), rather than assuming a universal common \(\varepsilon\);
- state explicitly that the negative cscK metrics are Yamabe representatives after scaling;
- record the exact identities
  \[
  D_W=0,\qquad
  \Delta V=2\pi^2\left(\frac{P}{8\pi^2}-k\right)\to0.
  \]

With these repairs, Theorem \(K_\infty\) is established for all prescribed finite sequences of blow-ups, including infinitely-near points.

For completeness, when \(k=0\), the same argument gives \(\inf_{\mathrm{K\ddot ahler}}P=0\). It is attained if \(K_X\) is ample, by the negative Kähler–Einstein metric. If \(K_X\) is nef but non-ample, equality would force the Kähler class to be proportional to \(K_X\), impossible because \(K_X\) has zero intersection with the contracted \((-2)\)-curves; the crepant cscK family approaches \(0\) without attaining it.