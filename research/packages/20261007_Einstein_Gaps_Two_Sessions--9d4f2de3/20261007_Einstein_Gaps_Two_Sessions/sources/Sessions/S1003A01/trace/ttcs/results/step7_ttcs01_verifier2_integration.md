# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step7_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step7_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Critically read the perpendicular P/J computations and the exact-CH factorization as a geometric analyst. Verify the smooth bolt assumptions and the assertion that C2-matched numerical profiles can be approximated by smooth exact-CH-collar cells with vanishing P and J change. If true, supply a precise cutoff lemma with a scaling estimate; if not, state the required jet matching and why the current polynomial envelope is inadequate. Also determine whether the exact Cartan identities plus CH endpoint map suggest a rigorous fixed-slot P≥8π² or J≥8π² proof, a plausible counterprofile, or neither. Keep the result limited to the diagonal perpendicular branch and distinguish P from J.

## Integrated Scientific Memo

# Verification memo: diagonal perpendicular branch

## Conclusions

- The main `wpow=2` profiles have the correct smooth \(O(-1)\)-bolt jets. The `wpow=1` family is generically not smooth at the bolt.
- The terminal envelope is not literally an exact CH collar, but it matches the CH profile to second order. It can therefore be replaced on a shrinking terminal interval by a smooth exact-CH collar with
  \[
  \Delta P,\ \Delta J_6\to0.
  \]
  For the actual cubic envelope, the change is \(O(\varepsilon^3)\) for each fixed profile.
- The exact Cartan identities and endpoint map are consistent. On an exact CH segment, both transverse quadratic forms admit explicit ground-state factorizations, so the sign-changing potential in the minus channel alone does not furnish a counterprofile.
- Nevertheless, neither \(P\ge 8\pi^2\) nor \(J_6\ge 8\pi^2\) is proved for the full diagonal perpendicular family. No subthreshold profile has been produced either. The remaining obstruction is the nonlinear bolt-to-collar transition and its signed cubic term.
- \(P\) and \(J_6\) must remain separate:
  \[
  J_6=P+\frac14\int(s+24)^2\,dV.
  \]
  A \(P\)-counterprofile need not violate the \(J_6\) threshold, while a proof for \(P\) would imply the corresponding result for \(J_6\).

Everything below concerns only the fixed diagonal perpendicular ansatz.

---

## 1. Smooth bolt verification

Consider
\[
g=\frac{dx^2}{4G(x)}+F(x)\sigma_1^2+x\sigma_2^2+xe^{w(x)}\sigma_3^2
\]
near the bolt \(x=x_0\). Put \(\rho=x-x_0\) and
\[
dt=\frac{d\rho}{2\sqrt G}.
\]
If
\[
F=f_1\rho+O(\rho^2),\qquad G=g_1\rho+O(\rho^2),
\]
then
\[
t=\sqrt{\rho/g_1}+O(\rho^{3/2}),\qquad
F=f_1g_1t^2+O(t^4).
\]
With the stated normalization of the Hopf circle, absence of a cone singularity requires
\[
\boxed{F'(x_0)G'(x_0)=f_1g_1=1.}
\]

For a smooth ordinary blow-up bolt, the two noncollapsing coefficients must agree through radial order \(t^2\). Their difference must satisfy
\[
xe^w-x=O(t^4),
\]
equivalently
\[
\boxed{w=O(\rho^2).}
\]
In bolt-adapted axes,
\[
a^2=x,\qquad b^2=xe^w,\qquad c^2=F,
\]
this gives
\[
a=A+\alpha t^2+O(t^4),\quad
b=A+\alpha t^2+O(t^4),\quad
c=t+O(t^3),\qquad A=\sqrt{x_0}.
\]

For the implemented profiles, \(u=\log(x/x_0)/\ell\) and
\[
\operatorname{smooth}(u)=10u^3-15u^4+6u^5=O(u^3)=O(\rho^3)
\]
at the bolt. Hence
\[
F=\rho e^{q_F}+O(\rho^3),\qquad
G=\rho e^{q_G}+O(\rho^3).
\]
The coefficient shift enforces
\[
q_F(0)+q_G(0)=0,
\]
and therefore \(F'(x_0)G'(x_0)=1\).

For `wpow=2`,
\[
w=\log(1+x)\operatorname{smooth}(u)
  +u^2(1-u)^3\sum_j c_jT_j(2u-1)
  =O(\rho^2),
\]
so these profiles have the required smooth bolt jet. For `wpow=1`, the free anisotropy is generally \(O(\rho)=O(t^2)\), which is incompatible with the weight-four tangential mode unless its leading coefficient accidentally vanishes. Thus the rough `wpow=1` profiles are not generally smooth cells.

---

## 2. Precise exact-collar cutoff lemma

Let
\[
F_0=x,\qquad G_0=x(1+x),\qquad w_0=\log(1+x)
\]
be the CH profile near the outer endpoint \(X\), and set
\[
q=(F-F_0,G-G_0,w-w_0).
\]

### Lemma

Suppose \(F,G,w\) are smooth from the interior, \(F,G>0\), and
\[
q(X)=q'(X)=q''(X)=0.
\]
Then for all sufficiently small \(\varepsilon>0\) there is a smooth diagonal profile \(g_\varepsilon\) such that

\[
g_\varepsilon=g\quad\text{on }x\le X-2\varepsilon,
\]
\[
g_\varepsilon=g_{CH}\quad\text{on }x\ge X-\varepsilon,
\]
and
\[
P(g_\varepsilon)\to P(g),\qquad
J_6(g_\varepsilon)\to J_6(g).
\]

More quantitatively, define
\[
\omega_2(\varepsilon)=
\sup_{X-2\varepsilon\le x\le X}
\left(
|q''|+\varepsilon^{-1}|q'|+\varepsilon^{-2}|q|
\right).
\]
Then \(\omega_2(\varepsilon)\to0\) and
\[
\boxed{
|P(g_\varepsilon)-P(g)|
+
|J_6(g_\varepsilon)-J_6(g)|
\le C\varepsilon\,\omega_2(\varepsilon)^2=o(\varepsilon).
}
\]

If additionally
\[
|\partial_x^j q(x)|\le A(X-x)^{3-j},
\qquad 0\le j\le3,
\]
then
\[
\boxed{
|P(g_\varepsilon)-P(g)|
+
|J_6(g_\varepsilon)-J_6(g)|
\le C A^2\varepsilon^3.
}
\]

Here \(C\) depends on uniform ellipticity and bounded background profile jets on a fixed neighborhood of \(X\).

### Proof

Choose \(\chi\in C^\infty([0,\infty))\) with
\[
\chi=0\ \text{on }[0,1],\qquad
\chi=1\ \text{on }[2,\infty),
\]
and put \(r=X-x\). Define
\[
q_\varepsilon(x)=\chi(r/\varepsilon)q(x),
\]
and add its three components to \((F_0,G_0,w_0)\).

This profile equals CH for \(r\le\varepsilon\), equals the original profile for \(r\ge2\varepsilon\), and remains positive for small \(\varepsilon\). Product differentiation gives, for \(0\le j\le2\),
\[
|\partial_x^j q_\varepsilon|
\le C\varepsilon^{2-j}\omega_2(\varepsilon).
\]
In particular, the metric two-jet differs from the CH two-jet by
\[
O(\omega_2(\varepsilon)).
\]
Since curvature is a smooth function of the metric, its inverse, and its first two derivatives on this uniformly nondegenerate outer collar,
\[
|\Ric^\circ_{g_\varepsilon}|
+
|\Ric_{g_\varepsilon}+6g_\varepsilon|
\le C\omega_2(\varepsilon).
\]
The modified interval has length \(O(\varepsilon)\), and its volume density is uniformly bounded. Hence both defect energies there are
\[
O\!\left(\varepsilon\omega_2(\varepsilon)^2\right).
\]
The removed terminal piece of the original profile obeys the same estimate.

Under cubic vanishing, the cutoff two-jet is \(O(A\varepsilon)\), giving \(O(A^2\varepsilon^3)\).

### Application to the polynomial envelope

Writing \(v=1-u\),
\[
\operatorname{smooth}(u)=1-10v^3+15v^4-6v^5,
\]
and the free terminal factors are \(O(v^3)\). Since \(u\mapsto x=x_0e^{\ell u}\) is a smooth local diffeomorphism at \(u=1\),
\[
F-x=O((X-x)^3),\quad
G-x(1+x)=O((X-x)^3),\quad
w-\log(1+x)=O((X-x)^3).
\]
Thus the stored profiles satisfy the stronger hypothesis, and their exact-collar approximants have
\[
\Delta P+\Delta J_6=O(\varepsilon^3)
\]
for each fixed profile.

Therefore the polynomial envelope is adequate for producing limiting exact-collar competitors. It should not itself be described as exact CH on an open collar. No uniform estimate in \(x_0\to0\) follows without controlling the profile coefficients, but a diagonal choice \(\varepsilon=\varepsilon(x_0)\) makes the cutoff error arbitrarily small profile by profile.

---

## 3. Cartan identities and endpoints

The cyclic relabeling
\[
(a,b,c)=(\sqrt x,\sqrt{xe^w},\sqrt F)
\]
is orientation preserving. With
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k,\qquad
\lambda_i=\frac{a_ja_k}{a_i},
\]
the symbolic Cartan calculation verifies
\[
|\Ric^\circ|^2
=\sum_i\left(\frac{\dot u_i}{a_i}
-\frac{2H_i}{a_ja_k}\right)^2,
\]
\[
s=-2\sum_i\left(\frac{\dot u_i}{a_i}
+\frac{2H_i}{a_ja_k}\right),
\]
and, for
\[
C(u)=u_1^2+u_2^2+u_3^2+u_1u_2u_3,
\]
\[
\dot C=abc\sum_i
\frac{\dot u_i}{a_i}\frac{2H_i}{a_ja_k}.
\]
Consequently
\[
\frac{P}{8\pi^2}
=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.
\]

The smooth bolt limits are
\[
u_{\rm bolt}=(0,0,-1),\qquad C_{\rm bolt}=1.
\]
On exact CH,
\[
a=c=\sqrt x,\qquad b=\sqrt{x(1+x)},
\]
and
\[
u_{\rm CH}=(0,3x,0),\qquad C_{\rm CH}=9x^2.
\]
Thus
\[
\Phi=C-u_2^2
\]
has relative endpoint values
\[
\Phi_{\rm bolt}=1,\qquad \Phi_{\rm CH}=0.
\]
This validates the relative square completion
\[
\frac{P}{8\pi^2}-1
=\int\left(S_1+S_2+S_3+\frac{2u_1u_2u_3}{\lambda_2}\right)dt.
\]

---

## 4. Exact CH factorization

On an exact CH interval, the two transverse quadratic forms are
\[
\mathcal Q_\pm[v]
=\int\left(p(v')^2+V_\pm v^2\right)dx,
\qquad p=\frac{x(1+x)}4,
\]
with
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.
\]

They possess positive zero modes
\[
\phi_+=x(1+x)^{1/2},\qquad
\phi_-=x(1+x)^{-5/2},
\]
satisfying
\[
V_\pm=\frac{(p\phi_\pm')'}{\phi_\pm}.
\]
Hence on \([\xi,1]\),
\[
\boxed{
\mathcal Q_\pm[v]
=
\int_\xi^1 p\phi_\pm^2
\left(\frac v{\phi_\pm}\right)'^{\!2}dx
+
[b_\pm v^2]_\xi^1,
}
\]
where
\[
b_+(x)=\frac{2+3x}{8},\qquad
b_-(x)=\frac{2-3x}{8}.
\]

Thus, for perturbations vanishing at both ends of the CH segment,
\[
\mathcal Q_\pm[v]\ge0.
\]
In particular, the sign change of \(V_-\) does not itself yield a compactly supported negative direction.

If only \(v(1)=0\), the lower endpoint contributes
\[
-b_\pm(\xi)v(\xi)^2.
\]
A global proof must absorb this trace term using the preceding transition region. The CH factorization alone does not establish the full cell inequality.

---

## 5. Why the relative completion does not yet prove \(P\ge8\pi^2\)

The signed cubic is generically adverse even arbitrarily close to the smooth bolt. Write
\[
a=A+\alpha t^2+O(t^4),\quad
b=A+\alpha t^2+O(t^4),\quad
c=t+\gamma t^3+O(t^5).
\]
Then
\[
u_1=\kappa t+O(t^3),\qquad
u_2=\kappa t+O(t^3),\qquad
u_3=-1+O(t^2),
\]
where
\[
\kappa=2\alpha-\frac1A,
\]
while
\[
\lambda_2=t+O(t^3).
\]
Therefore
\[
u_1u_2u_3=-\kappa^2t^2+O(t^4),
\]
and
\[
\frac{2u_1u_2u_3}{\lambda_2}
=-2\kappa^2t+O(t^3).
\]
Thus smoothness does not imply \(u_1u_2u_3\ge0\); generically it implies the opposite near the bolt.

The unresolved \(P\)-problem is a global nonlinear estimate coupling:

1. the three positive relative-flow squares;
2. the negative part of \(2u_1u_2u_3/\lambda_2\);
3. the reconstruction equations for \(a,b,c\);
4. the smooth bolt jets;
5. the CH endpoint and the explicit CH trace terms.

The CH ground-state identities are favorable evidence for a matrix Hardy/Riccati proof but do not control the transition.

---

## 6. Separate status of \(J_6\)

For
\[
J_6=\int|\Ric+6g|^2\,dV
\]
one has exactly
\[
J_6-P=\frac14\int(s+24)^2\,dV\ge0.
\]
In the Cartan variables this is the additional rank-one square
\[
\frac{J_6-P}{8\pi^2}
=\frac14\int abc\left[
\sum_i\left(\frac{\dot u_i}{a_i}
+\frac{2H_i}{a_ja_k}\right)-12
\right]^2dt.
\]

Accordingly:

- \(P\ge8\pi^2\) would immediately imply \(J_6\ge8\pi^2\);
- \(J_6\ge8\pi^2\) may hold even if \(P<8\pi^2\) is possible;
- a \(P\)-counterprofile is not automatically a \(J_6\)-counterprofile.

The scalar square plausibly supplies the extra coercivity needed for a direct \(J_6\) theorem, but no supplied identity quantitatively dominates the transition cubic.

Also, \(P\) is scale invariant in dimension four, whereas \(J_6\) is not scale invariant with the numeral \(6\) fixed. The correct covariance is
\[
J_{\lambda/c}(cg)=J_\lambda(g),
\]
so in particular
\[
J_1(6g)=J_6(g).
\]

---

## 7. Verdict from the numerics and exact identities

All stored smooth profiles satisfy
\[
P>8\pi^2,\qquad J_6>8\pi^2,
\]
and approach the threshold from above as \(x_0\downarrow0\). Because of the cutoff lemma, these are also limiting costs of genuine smooth exact-CH-collar cells.

They are not certified minima. At \(x_0=.01\), degree eight, the nominal \(J\)-optimized profile even has lower \(P\) than the nominal \(P\)-optimized profile, and the reported gradients remain around \(10^{-4}\)–\(10^{-3}\). Hence the tables establish explicit upper competitors and stability evidence, not a lower bound.

The signed cubic is substantial: in the recorded decomposition it cancels roughly \(42\%\) of the positive squares. It cannot be discarded perturbatively. Conversely, the exact CH factorization rules out the simplest proposed countermechanism—localizing a negative mode solely in the sign-changing \(V_-\) potential.

Therefore the present evidence supports **neither** a rigorous fixed-slot proof nor a plausible realized counterprofile. It supplies a credible proof mechanism—global matrix Hardy/Riccati coercivity, especially after adding the \(J_6\) scalar square—but the nonlinear transition estimate remains unproved. No supplied smooth, positive, exact-collar profile has \(P<8\pi^2\) or \(J_6<8\pi^2\).