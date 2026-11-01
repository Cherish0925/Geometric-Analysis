# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 50,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step50_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step50_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of the Step-50 note (Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md), which claims: (1) Lemma 1.1/Cor 1.2: via pointwise Chern–Gauss–Bonnet, the eps^2 log(1/eps) corner coefficient F of a perpendicular Burns insertion g_bg+eps(k_B+k_0) can be computed from 4|W+|^2+s^2/12 instead of |Ric0|^2 (exact-form terms change only off-diagonal z^a y^b coefficients), so F depends only on Rm_p, and the W^- dependence is a nonnegative minimized square kappa(W^-) >= 0; (2) Theorem 2.1: the explicit corrector k0^W = (3/2)sym(h_W k_B) - (1/4)tr(h_W k_B) delta cancels the first-order W+ and s source for all W^- (exact sympy check for one W^- plus SU(2)_- equivariance/irreducibility); (3) Theorem 3.1: hence on every compact negative KE surface, at every point, P(g_eps)/8pi^2 = 1 - 9 eps^2 log(1/eps) + O(eps^2), with the order-eps bucket ell shown to vanish by an invariance + CH-comparison + Burns P-criticality/flux argument; (4) the Yamabe shortcut E(ĝ) <= 4P(g)/(P(g)+8pi^2 A) and Corollary 4.1. Check especially: the degree counting in Lemma 1.1(c) (are there any W^- ⊗ W^- terms at degree -4 besides |W+_1|^2, s_1^2? any 4-jet terms?); the analyticity/parity claims and whether the transgression G(y,z) is analytic so that diagonal coefficients agree; whether the order-eps bucket ell can be nonzero for a general KE point (is ell truly a U(2)_zeta-invariant LINEAR functional of (Rm_p,k0) only, blending-independent; is the CH comparison with Ch.5 (5.A) legitimate); the representation theory (SU(2)_- fixes zeta and omega; W^- spin 2; Ric0 spin 1); the equivariance argument for general W^-; the sign/convention of the CGB identity; the Yamabe inequality P(ĝ)-P(g)=(S(ĝ)-S(g))/12 and S minimized by the Yamabe metric when Y<0. Identify any gap that could invalidate the theorem and say precisely what extra argument would fill it. Read the scripts and data to see what was actually computed.

## Integrated Scientific Memo

# Verification memo

## Main conclusion

The explicit \(W^{-}\) compatibility identity is valid, and the weighted-degree argument supports the claimed universal logarithmic coefficient for the specified corrector. Two statements need correction:

1. The characteristic form denoted \(p\) must be the **signature density**, not the conventionally normalized first Pontryagin form.
2. Equality of optimized coefficients does **not** hold for every invariant corrector class: the supplied degree-\(\le2\) data contradict that assertion.

The principal unfinished argument in the note is the elimination of the order-\(\varepsilon\) term. It can be supplied directly by a Burns first-variation flux calculation, without comparing to the absent Ch.5 construction. That calculation gives
\[
\boxed{\ell=-R_p^{+}(\zeta,\zeta)}
\]
in the note’s \(P/(8\pi^{2})\) and Burns-\(\varepsilon\) normalization. Thus \(\ell=0\) for the perpendicular KE insertion. Details follow.

The numerical value \(F_{\rm CH}(c^*)=-18\) is reproduced by the supplied numerical data; its cited exact Ch.5 derivation is not included here. Consequently, the exact numerical coefficient \(-9\) remains dependent on that cited symbolic input.

---

## 1. CGB identity and the diagonal coefficient

Write
\[
P(g)=\int|\operatorname{Ric}^{\circ}|^{2}\,dV,
\qquad S(g)=\int s^{2}\,dV,
\]
using the operator-Frobenius Weyl norm employed in the scripts. Let \(e\) and \(l\) be the Euler and signature forms, normalized by
\[
\int e=\chi,\qquad \int l=\tau.
\]
Then
\[
8\pi^{2}e
=\left(|W^{+}|^{2}+|W^{-}|^{2}
-\frac12|\operatorname{Ric}^{\circ}|^{2}
+\frac{s^{2}}{24}\right)dV,
\]
\[
12\pi^{2}l=(|W^{+}|^{2}-|W^{-}|^{2})dV.
\]
Therefore
\[
|\operatorname{Ric}^{\circ}|^{2}dV
=\left(4|W^{+}|^{2}+\frac{s^{2}}{12}\right)dV
-16\pi^{2}e-24\pi^{2}l.
\]
The sign is correct. If the note’s \(p\) means \(p_{1}\), with \(\int p_{1}=3\tau\), its coefficient must instead be \(-8\pi^{2}p_{1}\).

### Analyticity of the transgression

For the explicit, antipodally even correctors, the diagonal-coefficient argument is sound. A precise justification is:

* Express the connection comparison and Chern–Weil transgression in a common metric-bundle identification, obtained analytically using a positive square root.
* In cylinder variables,
  \[
  g=\delta+zK_B(\theta)+\sum_{j\ge2}r^{j}H_j(\theta)+zr^{2}K_0(\theta).
  \]
  Metric inversion and square roots are analytic while the metric is positive definite.
* The scale-compensated connection and curvature, \(rA\) and \(r^{2}\mathrm{Rm}\), are analytic in \((r,z)\). Pullback of the transgression three-form to \(S_r^3\) cancels its scaling powers. Its sphere integral \(G(r,z)\) is consequently analytic, with **no \(\log r\) term**.
* Antipodal integration makes \(G\) even in \(r\), hence analytic in \(y=r^{2}\).

At fixed \(\varepsilon\),
\[
r\partial_r=2y\partial_y-2z\partial_z,
\qquad
r\partial_r(z^{a}y^{b})=2(b-a)z^{a}y^{b}.
\]
Thus exact-form terms cannot alter \(z^{2}y^{2}\).

This requires evenness of the corrector for the particular \((y,z)\)-analytic formulation. It is not automatically true for every homogeneous degree-zero tensor. Analyticity in \((r,z)\), with the corresponding weighted-degree argument, is the appropriate more general formulation.

---

## 2. Degree counting: no four-jet term or hidden \(W^{-}\)-square

Assign component degrees
\[
\deg h_j=j,\qquad \deg k_B=-2,\qquad \deg k_0=0.
\]
A curvature monomial involving metric perturbations of degrees \(d_1,\ldots,d_m\) has degree
\[
d_1+\cdots+d_m-2.
\]
Use orthonormal-frame components of \(\mathcal R=(W^{+},s)\), and write
\[
\mathcal R=\mathcal R_0+\varepsilon\mathcal R_1
+\varepsilon^{2}\mathcal R_2+\cdots.
\]
Exact scalar-flatness and ASD of \(\delta+\varepsilon k_B\) eliminate every pure-Burns term in \(\mathcal R\).

The relevant degrees are:

\[
\begin{array}{c|c}
\text{term}&\text{degree}\\ \hline
\mathcal L(k_0),\ \mathcal B(h_2,k_B)&-2\\
\mathcal B(h_3,k_B)&-1\\
\mathcal B(h_4,k_B),\ \mathcal C(h_2,h_2,k_B)&0\\
\mathcal B(k_B,k_0),\ \mathcal C(h_2,k_B,k_B)&-4\\
\mathcal C(h_3,k_B,k_B)&-3\\
\mathcal C(h_4,k_B,k_B),\
\mathcal D(h_2,h_2,k_B,k_B)&-2 .
\end{array}
\]

Hence the order-\(\varepsilon^{2}\), degree-\(-4\) density contains:

1. The square of
   \[
   \mathcal R_{1,-2}
   =\mathcal B(h_2,k_B)+\mathcal L(k_0).
   \]
2. The pairing of \(\mathcal R_0(p)\) with \(\mathcal R_{2,-4}\), which is linear in \(h_2,k_0\).
3. Volume corrections multiplying background squares.
4. **Also**, first-order volume corrections multiplying
   \[
   \langle\mathcal R_0(p),\mathcal R_{1,-2}\rangle.
   \]
   This last contribution is omitted from the note’s enumeration. It is linear in \(h_2,k_0\), not merely a background constant.

The omission does not affect the \(W^{-}\)-square conclusion: these extra contributions are linear in the \(W^{-}\) sector and average to zero for the equivariant construction.

There is no possible four-jet contribution: it would have to pair with a nonzero pure-Burns curvature term of lower degree, and those terms vanish. Likewise, two \(h_W\) factors in \(\mathcal R_2\) have degree \(-2\), not \(-4\). Therefore
\[
\boxed{\text{the only quadratic \(W^{-}\) contribution is }
4|W_{1}^{+,W}|^{2}+(s_1^W)^{2}/12.}
\]

The apparent four-jet dependence in the Step-49 Ricci formulation is consistent with this: it disappears after integration through the characteristic-form identity.

---

## 3. Representation theory and the exact corrector

The representation statements are correct:

* \(SU(2)_{-}\) acts trivially on \(\Lambda^{+}\), so it fixes both \(\zeta\) and \(\omega\).
* \(W^{-}\in\operatorname{Sym}^{2}_{0}\Lambda^{-}\) is the irreducible real spin-2 module.
* \(\operatorname{Ric}^{\circ}\in\Lambda^{+}\otimes\Lambda^{-}\) is three copies of spin 1.
* The Burns tail and CH quadratic jet are \(SU(2)_{-}\)-invariant.

For a **linear, group-stable** corrector space, isotypic decomposition separates the CH problem from the spin-2 least-squares problem. The correct formulation is
\[
\inf_{\mathcal K}F_X
=\inf_{\mathcal K}F_{\rm CH}
+\inf_{k\in\mathcal K^{(2)}}
\frac1{8\pi^{2}}\int_{S^{3}}
\left[
4|S_W+L_Wk|^{2}
+\frac{(\sigma_W+L_sk)^{2}}{12}
\right]d\Omega .
\]
“Invariant class” alone is insufficient if the class is nonlinear or its sectors cannot be varied independently.

Also, not every term “linear in \(W^{-}\)” vanishes with an arbitrary fixed corrector: the pairing with a spin-2 corrector is precisely the cancellation mechanism. What vanishes is its pairing with the CH/trivial sector and the remaining linear averaged terms.

### What was actually computed

`step50_exact_identity.py` forms the exact mixed curvature using:

* the linear second-derivative formula;
* mixed products of lowered Christoffels;
* first-order frame corrections in all four curvature slots;
* the linear curvature of
  \[
  k_0^W=\frac32\operatorname{sym}(h_Wk_B)
  -\frac14\operatorname{tr}(h_Wk_B)\delta.
  \]

There is no missing inverse-metric contribution at mixed order: the base Christoffels vanish, so inverse-metric corrections to their quadratic product start at higher order.

The JSON records exact vanishing of nine redundant \(W^{+}\)-matrix entries and \(s\), as well as purity of \(h_W\) and a nonzero uncorrected source. Thus the tested Weyl jet is nonzero.

Define the residual map \(T:W^{-}\mapsto(W^{+},s)\)-valued angular fields. It is linear and \(SU(2)_{-}\)-equivariant. Its kernel contains the tested nonzero vector and is an invariant subspace of the irreducible spin-2 domain. Therefore \(T=0\) for every \(W^{-}\). This proves Theorem 2.1.

One documentation discrepancy: the exact script’s docstring advertises an exact pure-\(k_B^2\) check, but its body does not perform that check. Exact scalar-flat ASD Burns geometry supplies it; the JAX script also checks the second derivative numerically.

### What the numerical data establish

The data give
\[
\|S_W\|_f^{2}/(8\pi^{2})=5.6,\qquad
\kappa_{\le2}=2.1,\qquad
\kappa_{\le4}\simeq3.2\times10^{-29}.
\]
The independent Ricci/Laurent evaluation gives
\[
F_{H^{2}\times H^{2}}(c^*+tk_0^W)
=-18+5.6(1-t)^2
\]
at the sampled values, and on CH
\[
F_{\rm CH}(c^*+tk_0^W)=-18+5.6t^2.
\]
The isolated Ricci mixed-source norm \(3.95555\ldots\) is not the full \(W^{-}\) logarithmic cost; its missing terms come from the other Laurent contributions.

The degree-\(\le2\) space is \(SO(4)\)-stable. Accordingly, the last sentence of Corollary 2.2 is false as written. Equality holds when the source belongs to \(L(\mathcal K)\); containing the displayed \(k_0^W\) is sufficient, not necessary. The degree-\(\le4\) class and unrestricted smooth correctors qualify.

For the actual corrector used in Theorem 3.1,
\[
F_X(k_0^{c^*}+k_0^W)=F_{\rm CH}(k_0^{c^*}),
\]
so this correction does not impair the construction.

---

## 4. A direct repair of the order-\(\varepsilon\) argument

The supplied materials do not contain Ch.5 (5.A) or the full multiplicative construction. Its asymptotic comparison therefore cannot be independently verified here. More importantly, classification of invariant functionals on arbitrary pairs \((\mathrm{Rm},k_0)\) is not limited to \(s,W^{+}_{\zeta\zeta}\). That classification becomes applicable only after substituting a natural curvature-dependent corrector.

Both issues can be avoided by computing the first-variation flux.

### 4.1 Burns boundary variation

Let
\[
g_B=\delta+k_B,\qquad E_B=\operatorname{Ric}_{g_B}.
\]
Since \(s_B=0=W_B^{+}\), Burns is \(P\)-critical for compactly supported variations. For a variation \(q\) on a truncated end, integration by parts gives
\[
DP_{g_B}(q)=\mathcal B_R(q)
\]
when \(q\) vanishes near the bolt, where the outer boundary term is
\[
\mathcal B_R(q)=
\int_{S_R}\left[
2E_{ij}n^i\nabla^kq_{kj}
-E_{ij}\nabla_nq_{ij}
+(\nabla_nE_{ij})q_{ij}
-E_{ij}n^i\nabla^j\operatorname{tr}q
\right]dA.
\]
The terms involving \(\nabla^iE_{ij}\) vanish because \(s_B=0\). Algebraic curvature and norm-variation terms contribute to the interior Euler–Lagrange expression, which is zero.

This immediately proves blending independence. For \(q=O(R^{-2})\), with derivative decay, the flux is \(O(R^{-4})\); for a degree-zero corrector it is \(O(R^{-2})\). Thus
\[
\lim_{R\to\infty}\mathcal B_R(k_0)=0.
\]
In particular, the order-\(\varepsilon\) coefficient is independent of **all** bounded degree-zero correctors, not just \(k_0^W\).

### 4.2 Evaluate the growing normal-coordinate jet

Let \(\operatorname{Ric}_p=\lambda\delta\), so \(s=4\lambda\), and
\[
h_{ij}=-\frac13R_{ikjl}x^kx^l.
\]
Then
\[
h_{ij}x^i=0,\qquad
\operatorname{tr}h=-\frac{\lambda}{3}r^2,\qquad
\partial^kh_{kj}=\frac{\lambda}{3}x_j.
\]

The leading Burns Ricci tensor is
\[
E_B=b+O(r^{-6}),\qquad
b=\frac{2}{r^4}
\left(\delta-2\theta\otimes\theta
-2J_\zeta\theta\otimes J_\zeta\theta\right),
\quad \theta=x/r.
\]
For example, its radial component follows directly from the Burns radii:
\[
\operatorname{Ric}_{rr}
=-\frac{2}{(r^2+1)^2}
=-2r^{-4}+O(r^{-6});
\]
Kähler symmetry and scalar-flatness give the other leading eigenvalues.

Replacing the metric, connection, normal and measure by their Euclidean leading terms in the flux changes its limit by zero. Homogeneity yields
\[
\mathcal B_\infty(h)
=\int_{S^3}
\left[
2b_{ij}\theta^i\partial^kh_{kj}
-6b_{ij}h_{ij}
-b_{ij}\theta^i\partial^j\operatorname{tr}h
\right]d\Omega .
\]
Using the identities above,
\[
\mathcal B_\infty(h)
=\int_{S^3}
\left[
\frac{4\lambda}{3}
-8R(J_\zeta\theta,\theta,J_\zeta\theta,\theta)
\right]d\Omega .
\]

The self-dual part of \(\theta\wedge J_\zeta\theta\) is the fixed unit form \(\zeta/\sqrt2\); its anti-self-dual part averages isotropically. Therefore, for an Einstein algebraic curvature tensor,
\[
\fint_{S^3}R(J_\zeta\theta,\theta,J_\zeta\theta,\theta)\,d\Omega
=\frac{s}{12}+\frac12W^{+}(\zeta,\zeta).
\]
As \(\operatorname{Vol}(S^3)=2\pi^2\),
\[
\boxed{
\mathcal B_\infty(h)
=-8\pi^2\left(W^{+}(\zeta,\zeta)+\frac{s}{12}\right)
=-8\pi^2R^{+}(\zeta,\zeta).
}
\]

### 4.3 Identification with the construction’s bucket

After \(x=\sqrt\varepsilon\,\xi\), the first scaled perturbation is
\[
q=\chi_{\rm in}\bigl(h_2(\xi)+k_0(\xi)\bigr).
\]
Its first variation over the Burns end is convergent: for an Einstein jet,
\[
E_B=O(\rho^{-4}),\qquad
D\operatorname{Ric}^{\circ}_{g_B}(h_2+k_0)=O(\rho^{-2}),
\]
so the radial integral is \(O(\rho^{-3})\,d\rho\), not \(O(\rho^{-1})\,d\rho\).

The analytic neck expansion identifies its convergent first-order integral with the inner-transition plus neck order-\(\varepsilon\) bucket. The omitted tail at \(\rho=T/\sqrt\varepsilon\) contributes \(O_T(\varepsilon^2)\). Hence
\[
\ell=\frac{\mathcal B_\infty(h_2)}{8\pi^2}
=-R_p^{+}(\zeta,\zeta).
\]
At a KE point with \(\zeta\perp\omega\),
\[
W^{+}(\zeta,\zeta)=-s/12,
\qquad R^{+}(\zeta,\zeta)=0.
\]
Thus \(\ell=0\), independently of blending and of the chosen degree-zero corrector.

This supplies the substantive missing argument and explains geometrically why perpendicular insertion is first-order neutral.

---

## 5. Remainder and logarithmic term

For the explicit even corrector, the averaged Ricci density per \(d\log r\) is analytic in \((y,z)\), uniformly on a sufficiently small neck. Einstein background and exact Burns boundary data imply
\[
\psi(y,z)-\psi_B(z)=z^2y\,\phi(y,z).
\]
Writing
\[
\phi(y,z)=\phi(0,z)+y\phi_3(y,z)
\]
gives
\[
\psi-\psi_B=z^2y\phi(0,z)+\varepsilon^2\phi_3(y,z).
\]
The first part produces the bucket just evaluated. For the second,
\[
|\phi_3(y,z)-\phi_3(0,0)|\le C_T(y+z),
\]
and \(\int(y+z)\,d\log r=O_T(1)\). Consequently
\[
\varepsilon^2\int\phi_3\,d\log r
=\frac{F}{2}\varepsilon^2\log(1/\varepsilon)
+O_T(\varepsilon^2).
\]
Here \(\phi_3(0,0)=F\) under the stated normalization.

The inner \(h_3\) linear contribution vanishes by antipodal parity; the remaining inner errors are \(O(\varepsilon^2)\). The outer transition costs \(O_T(\varepsilon^2)\), because the background is Einstein.

Thus, accepting the cited exact CH input \(F_{\rm CH}(c^*)=-18\),
\[
\frac{P(g_\varepsilon)}{8\pi^2}
=1-9\varepsilon^2\log(1/\varepsilon)+O_{X,p,T}(\varepsilon^2).
\]
The leading \(1\) is also consistent with the global identity: blow-up changes \(2\chi+3\tau\) by \(-1\), contributing \(+8\pi^2\) to \(P\).

---

## 6. Yamabe shortcut and the scope of the consequences

Conformal invariance of \(\int|W^{+}|^2\) gives exactly
\[
P(\widehat g)-P(g)=\frac{S(\widehat g)-S(g)}{12}.
\]
For a negative Yamabe class,
\[
Y([g])\ge-\|s_-(g)\|_2
\]
by Hölder’s inequality in the Yamabe quotient. Hence
\[
S(g)\ge\|s_-(g)\|_2^2\ge Y([g])^2.
\]
The constant-scalar-curvature Yamabe representative attains equality, so \(P(\widehat g)\le P(g)\).

Under the actual scalar-curvature supply
\[
S(\widehat g)\ge32\pi^2A,
\]
monotonicity yields
\[
E(\widehat g)
\le\frac{4P(\widehat g)}{P(\widehat g)+8\pi^2A}
\le\frac{4P(g)}{P(g)+8\pi^2A}.
\]
This part is correct.

A fixed sufficiently small cell has \(P=8\pi^2(1-\delta)\), \(\delta>0\), and can be replicated in disjoint lifted balls. Corollary 4.1 additionally depends on the absent balance definitions, handle estimates, metric-supply hypotheses, and capacity for the specified number of cells. Its displayed family coefficient cannot be independently verified from this bundle.

Finally, §6’s non-Einstein extension needs qualification. Although the **local logarithmic coefficient** has the stated two-jet dependence, a general non-Einstein background also has a first-order bulk variation
\[
\varepsilon\,DP_{g_{\rm bg}}\!\left[\chi(k_B+k_0)\right].
\]
It need not reduce to pointwise \(R_p^{+}(\zeta,\zeta)\). Such a reduction requires bulk \(P\)-criticality, or a separate argument controlling that interior term.

**Remaining exact input:** an included symbolic evaluation of \(F_{\rm CH}(c^*)=-18\). The supplied scripts and data verify the \(W^{-}\) identity exactly and corroborate the number numerically; they do not themselves contain the cited exact CH coefficient calculation.