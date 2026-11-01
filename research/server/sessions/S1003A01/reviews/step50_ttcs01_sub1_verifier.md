# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md",
    "Sessions/S1003A01/workspace/notes/step49_kernel_log_coefficient_general_background.md",
    "Sessions/S1003A01/workspace/scripts/step50_wminus_compatibility.py",
    "Sessions/S1003A01/workspace/scripts/step50_exact_identity.py",
    "Sessions/S1003A01/workspace/scripts/step50_check_corrector_ric0.py",
    "Sessions/S1003A01/workspace/data/step50/exact_identity.json",
    "Sessions/S1003A01/workspace/data/step50/wminus_compat_A4.json",
    "Sessions/S1003A01/workspace/data/step50/wminus_compat_A2.json",
    "Sessions/S1003A01/workspace/data/step50/natural_corrector.json",
    "Sessions/S1003A01/workspace/data/step50/corrector_check_ric0form.json",
    "Sessions/S1003A01/workspace/scripts/step49_kernel_log_coefficient.py"
  ]
}
```

## Task

Verify the mathematics of the Step-50 note (Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md), which claims: (1) Lemma 1.1/Cor 1.2: via pointwise Chern–Gauss–Bonnet, the eps^2 log(1/eps) corner coefficient F of a perpendicular Burns insertion g_bg+eps(k_B+k_0) can be computed from 4|W+|^2+s^2/12 instead of |Ric0|^2 (exact-form terms change only off-diagonal z^a y^b coefficients), so F depends only on Rm_p, and the W^- dependence is a nonnegative minimized square kappa(W^-) >= 0; (2) Theorem 2.1: the explicit corrector k0^W = (3/2)sym(h_W k_B) - (1/4)tr(h_W k_B) delta cancels the first-order W+ and s source for all W^- (exact sympy check for one W^- plus SU(2)_- equivariance/irreducibility); (3) Theorem 3.1: hence on every compact negative KE surface, at every point, P(g_eps)/8pi^2 = 1 - 9 eps^2 log(1/eps) + O(eps^2), with the order-eps bucket ell shown to vanish by an invariance + CH-comparison + Burns P-criticality/flux argument; (4) the Yamabe shortcut E(ĝ) <= 4P(g)/(P(g)+8pi^2 A) and Corollary 4.1. Check especially: the degree counting in Lemma 1.1(c) (are there any W^- ⊗ W^- terms at degree -4 besides |W+_1|^2, s_1^2? any 4-jet terms?); the analyticity/parity claims and whether the transgression G(y,z) is analytic so that diagonal coefficients agree; whether the order-eps bucket ell can be nonzero for a general KE point (is ell truly a U(2)_zeta-invariant LINEAR functional of (Rm_p,k0) only, blending-independent; is the CH comparison with Ch.5 (5.A) legitimate); the representation theory (SU(2)_- fixes zeta and omega; W^- spin 2; Ric0 spin 1); the equivariance argument for general W^-; the sign/convention of the CGB identity; the Yamabe inequality P(ĝ)-P(g)=(S(ĝ)-S(g))/12 and S minimized by the Yamabe metric when Y<0. Identify any gap that could invalidate the theorem and say precisely what extra argument would fill it. Read the scripts and data to see what was actually computed.

## Output

# Scientific verification memo

## Overall assessment

The local algebra behind the universal logarithmic coefficient is strong:

- The Chern–Gauss–Bonnet/signature reduction is correct once the characteristic-form normalization is stated precisely.
- Weighted homogeneity shows that the \(z^{2}y^{2}\) coefficient uses only \(h_{2}\), hence only \(\mathrm{Rm}_{p}\); neither \(h_{4}\) nor a \(W^{-}\otimes W^{-}\) contribution can enter this coefficient outside the squared first-order source.
- The explicit tensor
  \[
  k_{0}^{W}=\frac32\operatorname{sym}(h_{W}k_{B})
  -\frac14\operatorname{tr}(h_{W}k_{B})\,\delta
  \]
  is supported by an exact rational-function computation for one nonzero \(W^{-}\) vector, and the irreducibility argument extends it to every \(W^{-}\).
- The coefficient \(F=-18\), and therefore
  \[
  \frac{P(g_\varepsilon)}{8\pi^{2}}
  =1-9\varepsilon^{2}\log(1/\varepsilon)+O(\varepsilon^{2}),
  \]
  is algebraically established once the global gluing expansion has no surviving order-\(\varepsilon\) term.

The remaining substantive issue is Theorem 3.1: the analyticity factorization is mathematically plausible and can be made rigorous, but the order-\(\varepsilon\) comparison with the CH construction still needs a written first-variation sphere-flux lemma and an explicit asymptotic comparison of the two CH necks. No contradiction to the theorem appears in the supplied material, but that argument is not yet a complete proof.

There is also one definite textual error: the statement that
\[
\inf_{\mathcal K}F_X=\inf_{\mathcal K}F_{\rm CH}
\]
for every \(SO(4)\)-invariant corrector class is contradicted by the degree-\(\le2\) computation, where the difference is \(2.1\). Equality holds for classes containing \(k_{0}^{W}\), such as the degree-\(\le4\) class, or for the unrestricted smooth degree-zero class.

---

## 1. Chern–Gauss–Bonnet reduction

### 1.1 Normalization and sign

With \(E=\operatorname{Ric}^{\circ}\), let \(e\) be the Euler density normalized by \(\int e=\chi\), and let \(l\) be the signature density normalized by \(\int l=\tau\). In the norm convention used by the scripts,
\[
8\pi^{2}e
=\left(|W^{+}|^{2}+|W^{-}|^{2}
-\frac12|E|^{2}+\frac{s^{2}}{24}\right)dV,
\]
and
\[
12\pi^{2}l=(|W^{+}|^{2}-|W^{-}|^{2})dV.
\]
Therefore
\[
|E|^{2}dV
=
\left(4|W^{+}|^{2}+\frac{s^{2}}{12}\right)dV
-16\pi^{2}e-24\pi^{2}l.
\]

Thus the displayed identity in the note is correct if its \(p\) denotes the signature density \(l\). If \(p\) means the standard first Pontryagin form \(p_{1}\), for which \(\int p_{1}=3\tau\), the last term is instead \(-8\pi^{2}p_{1}\). This normalization should be stated explicitly.

The numerical convention is consistent with
\[
\int_{\mathbf{CP}^{2}}|W^{+}|^{2}=12\pi^{2}.
\]

### 1.2 Why exact forms do not alter the \(z^{2}y^{2}\) coefficient

For two metrics on the annulus, the differences of their Euler and signature forms are exact. After integration over \(S^{3}_{r}\), their contribution to the density per \(d\log r\) has the form
\[
r\partial_{r}G(r,\varepsilon).
\]
Writing
\[
y=r^{2},\qquad z=\frac{\varepsilon}{r^{2}},
\]
and differentiating at fixed \(\varepsilon\),
\[
r\partial_{r}=2y\partial_{y}-2z\partial_{z}.
\]
Hence
\[
r\partial_{r}(z^{a}y^{b})=2(b-a)z^{a}y^{b}.
\]
The diagonal terms \(a=b\), including \(z^{2}y^{2}\), vanish identically.

For the explicit correctors in Theorem 3.1, analyticity is available as follows. In the cylinder variables,
\[
g=\delta+r^{2}H_{2}(\omega)+r^{3}H_{3}(\omega)+\cdots
+zK_{B}(\omega)+zyK_{0}(\omega).
\]
Metric inversion, connection formation, curvature, and the Chern–Simons transgression are analytic operations while the metric remains positive definite. After expressing the sphere flux in a scale-invariant frame, all powers of \(r\) produced by coordinate derivatives are balanced by the sphere measure and the \(d\log r\) normalization. Thus the averaged flux is analytic in \((r,z)\) near \((0,0)\). Since \(K_{B}\) and the explicit \(K_{0}\) are antipodally even, odd powers of \(r\) integrate to zero, so the result is analytic in \((y,z)\).

A full proof should write this using a fixed interpolation \(g_{t}\) between the two metrics and the standard Chern–Simons forms. No logarithm can arise inside \(G\), because it is obtained from local rational operations and an integration only in the interpolation parameter \(t\).

### 1.3 Degree counting and absence of four-jet terms

Assign homogeneous metric degrees
\[
\deg h_{j}=j,\qquad \deg k_{B}=-2,\qquad \deg k_{0}=0.
\]
A curvature monomial involving metric tensors of degrees \(d_{1},\dots,d_{m}\) has degree
\[
d_{1}+\cdots+d_{m}-2.
\]

The first order in \(\varepsilon\) that can have curvature degree \(-2\) is
\[
\mathcal R^{(1)}_{-2}
=
\mathcal B(h_{2},k_{B})+\mathcal L(k_{0}),
\qquad
\mathcal R=(W^{+},s).
\]
Indeed:

- \(h_{2}\) with \(k_{B}\) has degree \(2-2-2=-2\);
- \(\mathcal L(k_{0})\) has degree \(0-2=-2\);
- \(h_{3}\) with \(k_{B}\) has degree \(-1\);
- \(h_{4}\) with \(k_{B}\) has degree \(0\).

Consequently the squared first-order source gives
\[
\left|\varepsilon\mathcal R^{(1)}_{-2}\right|^{2}
\sim\varepsilon^{2}r^{-4},
\]
which is precisely logarithmic after multiplication by \(r^{4}d\log r\).

At second order in \(\varepsilon\), curvature degree \(-4\) can arise only from

\[
\mathcal B(k_{B},k_{0})
\quad\text{and}\quad
\mathcal C(h_{2},k_{B},k_{B}).
\]
Their degrees are
\[
-2+0-2=-4,
\qquad
2-2-2-2=-4.
\]
By contrast,
\[
\deg \mathcal C(h_{3},k_{B},k_{B})=-3,\qquad
\deg \mathcal C(h_{4},k_{B},k_{B})=-2,
\]
and a term with two copies of \(h_{2}\) and two copies of \(k_{B}\) has degree
\[
2+2-2-2-2=-2.
\]
Thus:

1. \(h_{4}\) cannot enter the logarithmic coefficient in the \((W^{+},s)\) representation.
2. A term quadratic in \(W^{-}\), which would require two copies of \(h_{W}\), also has the wrong degree.
3. Pure \(k_{B}\)-terms vanish in \(W^{+}\) and \(s\) because \(\delta+\varepsilon k_{B}\) is exactly ASD and scalar-flat.
4. Norm and volume corrections multiplying the background values involve only \(W^{+}_{\rm bg}\) and \(s_{\rm bg}\); they cannot produce \(W^{-}\)-dependence.

This validates the main degree-counting assertion in Lemma 1.1(c).

---

## 2. Representation theory and the completed square

### 2.1 Relevant representations

For the chosen orientation,
\[
SO(4)\simeq \bigl(SU(2)_{+}\times SU(2)_{-}\bigr)/\{\pm1\}.
\]
The factor \(SU(2)_{-}\) acts trivially on \(\Lambda^{+}\). It therefore fixes both \(\zeta\) and \(\omega\). Moreover,
\[
W^{-}\in\operatorname{Sym}^{2}_{0}(\Lambda^{-})
\]
is the real spin-\(2\) irreducible representation, while
\[
\operatorname{Ric}^{\circ}\in\Lambda^{+}\otimes\Lambda^{-}
\]
is, as an \(SU(2)_{-}\)-module, three copies of spin \(1\).

This justifies:

- no invariant linear functional on \(W^{-}\);
- no invariant linear functional on \(\operatorname{Ric}^{\circ}\);
- orthogonality between the CH source, which is \(SU(2)_{-}\)-trivial, and the \(W^{-}\) source, which lies in the spin-\(2\) sector.

One sentence in Corollary 1.2 needs refinement. A fixed spin-\(2\) corrector can pair with the \(W^{-}\) source; that pairing is exactly what produces the cancellation. The accurate decomposition is
\[
F_X(k_{0}^{(0)}+k_{0}^{(2)}+\cdots)
=
F_{\rm CH}(k_{0}^{(0)})
+
\left\|S_{W}+\mathcal Lk_{0}^{(2)}\right\|^{2}_{4W^{+}+s}
+\text{other squared sectors}.
\]
There is no pairing between the CH sector and the spin-\(2\) sector, but there is generally a pairing between \(S_{W}\) and \(k_{0}^{(2)}\).

For a linear group-stable corrector space, minimization separates into these isotypic components.

### 2.2 Exact identity

Define
\[
T(W^{-})
=
\left(
W_{\rm flat}^{+\,\prime\prime}(h_{W},k_{B})
+W_{\rm flat}^{+\,\prime}(k_{0}^{W}),
\;
s_{\rm flat}^{\prime\prime}(h_{W},k_{B})
+s_{\rm flat}^{\prime}(k_{0}^{W})
\right).
\]
The map \(T\) is linear and \(SU(2)_{-}\)-equivariant:

- \(W^{-}\mapsto h_{W}\) is natural;
- \(k_{B}\) is \(SU(2)_{-}\)-invariant;
- matrix multiplication, symmetrization, trace, and multiplication by \(\delta\) are equivariant;
- the flat curvature linearization is equivariant.

The exact SymPy script proves \(T(W_{0}^{-})=0\) for the nonzero product-background vector
\[
h_{W}=h_{2,H^{2}\times H^{2}}-h_{2,\rm CH}.
\]
The script also verifies
\[
W^{+\,\prime}(h_{W})=0,\quad
s'(h_{W})=0,\quad
\operatorname{Ric}^{\circ\,\prime}(h_{W})=0,
\]
so \(h_{W}\) is pure \(W^{-}\), and `source_nonzero=true` confirms that the tested vector is nonzero.

Since the kernel of \(T\) is an invariant subspace of the irreducible real spin-\(2\) module and contains a nonzero vector, it is the entire module. This is a complete argument for all algebraic \(W^{-}\).

The rational curvature calculation in `step50_exact_identity.py` includes the required mixed Christoffel-product terms and first-order orthonormal-frame corrections. No additional inverse-metric term is missing at mixed order, because the base Christoffel symbols vanish.

The JSON records nine displayed \(W^{+}\)-matrix entries plus \(s\); these are redundant because \(W^{+}\) is symmetric and trace-free, but their vanishing is sufficient.

The script documentation says that the pure \(k_{B}^{2}\) identity is also verified exactly, whereas the script itself does not perform that exact calculation. The numerical JAX data give it at approximately \(4\times10^{-14}\), and the geometric fact that the Burns metric is exactly ASD and scalar-flat supplies the exact result independently.

### 2.3 Numerical corroboration

The independent computations are mutually consistent:

- `wminus_compat_A4.json` gives
  \[
  \|S_{W}\|^{2}/(8\pi^{2})=5.6,\qquad
  \kappa\simeq3.2\times10^{-29}.
  \]
- The flat corrector quadratic blocks in the \((W^{+},s)\) and \(\operatorname{Ric}^{\circ}\) formulations agree to \(1.8\times10^{-15}\).
- `corrector_check_ric0form.json` gives
  \[
  F_{H^{2}\times H^{2}}(c^{*}+t k_{0}^{W})
  =-18+5.6(1-t)^{2}
  \]
  at the sampled values, while on CH it gives
  \[
  F_{\rm CH}(c^{*}+t k_{0}^{W})=-18+5.6t^{2}.
  \]

The fact that the isolated mixed \(\operatorname{Ric}^{\circ}\) source has norm \(3.9555\ldots\), rather than \(5.6\), is not an inconsistency. In the \(\operatorname{Ric}^{\circ}\) representation, further Laurent terms involving higher jets and exact-form bookkeeping contribute to the full logarithmic coefficient. The complete quadratic form recovers \(5.6\).

### 2.4 Correction to the universal corrector-class sentence

The degree-\(\le2\) space is \(SO(4)\)-invariant, yet the data give
\[
\kappa_{\deg\le2}=2.1.
\]
Therefore the sentence asserting equality of the two infima for every \(SO(4)\)-invariant class is false.

The correct statement is:

> If the corrector space contains \(k_{0}^{W}\) for every algebraic \(W^{-}\), and is stable under the relevant group projections, then the optimized logarithmic coefficient agrees with the CH value.

The degree-\(\le4\) polynomial/rational class has this property; the degree-\(\le2\) class does not.

This textual correction does not affect Theorem 3.1, which explicitly uses \(k_{0}^{W}\).

---

## 3. General KE construction and the order-\(\varepsilon\) term

### 3.1 Analytic factorization

For the explicit even corrector, the proposed factorization is sound. Let \(\psi(y,z)\) be the angularly averaged \(|\operatorname{Ric}^{\circ}|^{2}\) density per \(d\log r\), and let \(\psi_{B}(z)\) be its flat-Burns value. Then:

- At \(z=0\), the metric is \(g_{\rm bg}\), so \(\operatorname{Ric}^{\circ}=0\). Analyticity gives
  \[
  \psi(y,z)=O(z^{2}).
  \]
- At \(y=0\), the metric is the flat Burns metric because both \(h_{2}y\) and \(zyk_{0}\) vanish:
  \[
  \psi(0,z)=\psi_{B}(z).
  \]

Consequently
\[
\psi(y,z)-\psi_{B}(z)=z^{2}y\,\phi(y,z)
\]
for analytic \(\phi\). Writing
\[
\phi(y,z)=\phi(0,z)+y\phi_{3}(y,z)
\]
gives
\[
\psi-\psi_{B}
=
z^{2}y\,\phi(0,z)
+\varepsilon^{2}\phi_{3}(y,z).
\]

The first term integrates as
\[
\int z^{2}y\,\phi(0,z)\,d\log r
=
\frac{\varepsilon}{2}
\int_{\varepsilon/T^{2}}^{1/4}\phi(0,z)\,dz,
\]
up to orientation of the endpoints. This is an order-\(\varepsilon\) contribution plus \(O(\varepsilon^{2}/T^{2})\).

For the second term, analyticity gives a uniform estimate
\[
|\phi_{3}(y,z)-\phi_{3}(0,0)|
\le C_{T}(y+z).
\]
Since
\[
\int y\,d\log r=O(T^{2}),\qquad
\int z\,d\log r=O(1),
\]
one obtains
\[
\varepsilon^{2}
\int\phi_{3}(y,z)\,d\log r
=
\frac{\varepsilon^{2}}{2}\phi_{3}(0,0)
\log(1/\varepsilon)+O_{T}(\varepsilon^{2}).
\]
With the note’s normalization, \(\phi_{3}(0,0)=F=-18\), producing \(-9\varepsilon^{2}\log(1/\varepsilon)\).

This part needs a written analytic lemma, but the mechanism and estimates are correct.

### 3.2 Inner transition and odd powers

In scaled coordinates \(x=\sqrt{\varepsilon}\,\xi\),
\[
g_{\varepsilon}
=
\varepsilon\left[
g_{B}
+\varepsilon\bigl(h_{2}(\xi)+k_{0}(\xi)\bigr)
+\varepsilon^{3/2}h_{3}(\xi)+O(\varepsilon^{2})
\right].
\]
The functional \(P=\int|\operatorname{Ric}^{\circ}|^{2}\) is scale invariant. For compactly supported variations of Burns,
\[
DP_{g_{B}}=0,
\]
which also follows from the integrated CGB identity because \(W^{+}_{g_{B}}=0=s_{g_{B}}\).

The \(h_{3}\) term is odd under \(\xi\mapsto-\xi\), while the Burns metric and radial blending are invariant under this map. Its linear contribution therefore integrates to zero. The first unaccounted terms are \(O(\varepsilon^{2})\).

### 3.3 What remains to establish for \(\ell=0\)

The invariance argument becomes rigorous after composing the first-order functional with the chosen corrector:
\[
\mathcal L(W^{-})
=
\ell\bigl(h_{\rm KE}+h_{W},
k_{0}^{c^{*}}+k_{0}^{W}(W^{-})\bigr).
\]
Linearity gives
\[
\mathcal L(W^{-})
=
\ell(h_{\rm KE},k_{0}^{c^{*}})
+
\ell(h_{W},k_{0}^{W}(W^{-})).
\]
The second term is an \(SU(2)_{-}\)-invariant linear functional on the spin-\(2\) module, and hence vanishes. Thus every KE point has the same order-\(\varepsilon\) coefficient as CH.

This formulation is cleaner than classifying invariant functionals on the pair \((\mathrm{Rm},k_{0})\). Before substituting \(k_{0}=k_{0}(\mathrm{Rm},\zeta)\), that pair admits many linear functionals involving the independent corrector variable. The classification by \(s\) and \(W^{+}(\zeta,\zeta)\) applies only after the corrector has been chosen equivariantly from the curvature data.

The remaining CH comparison requires the following precise first-variation lemma.

Let \(q\) be a variation of the Burns metric on a truncated end. Integration by parts in the first variation gives
\[
DP_{g_{B}}(q;\rho_{1}<|\xi|<\rho_{2})
=
\mathcal B_{\rho_{2}}(q)-\mathcal B_{\rho_{1}}(q),
\]
where \(\mathcal B_{\rho}(q)\) is a sphere integral involving
\[
\operatorname{Ric}^{\circ}_{g_{B}},\quad
\nabla\operatorname{Ric}^{\circ}_{g_{B}},\quad
q,\quad\nabla q.
\]
It must then be shown that:

1. Compactly supported changes of the inner blending give zero first-order contribution.
2. If two neck variations differ by
   \[
   q_{1}-q_{2}=O(\rho^{-2}),\qquad
   \nabla^{j}(q_{1}-q_{2})=O(\rho^{-2-j}),
   \]
   then
   \[
   \mathcal B_{\rho}(q_{1}-q_{2})\longrightarrow0.
   \]
   Since Burns curvature is \(O(\rho^{-4})\), the sphere integrand is \(O(\rho^{-7})\) and its integral is \(O(\rho^{-4})\).
3. In a common coordinate gauge, the additive CH neck and the Ch.5 neck have the same growing and constant first-order terms:
   \[
   q_{\rm Ch.5}
   =
   h_{2,\rm CH}+k_{0}^{c^{*}}+O(\rho^{-2})
   \]
   with the corresponding derivative estimates.
4. Ch.5’s expansion indeed has zero order-\(\varepsilon\) coefficient in the same normalization.

Items 1–2 are standard consequences of Burns criticality and decay. Item 3 requires an explicit expansion of the Ch.5 formulas; it is asserted in the note but not demonstrated in the supplied files. A direct computation of \(\mathcal B_{\rho}(h_{2,\rm CH}+k_{0}^{c^{*}})\) would be an equally complete replacement.

Until that sphere-flux comparison is written, Theorem 3.1 remains an outlined theorem rather than a complete proof. The exact \(W^{-}\) cancellation does not by itself remove a universal CH order-\(\varepsilon\) term; its vanishing comes specifically from the CH calculation and the flux equivalence.

---

## 4. Yamabe step

Let
\[
S(g)=\int_{M}s_{g}^{2}\,dV_{g}.
\]
Conformal invariance of \(\int|W^{+}|^{2}\) and invariance of the characteristic numbers give, for conformal metrics,
\[
P(\widehat g)-P(g)
=
\frac{S(\widehat g)-S(g)}{12}.
\]

If \(Y(M)<0\), then every conformal class has Yamabe constant below zero. Its Yamabe representative \(\widehat g\) minimizes \(S\) in that class. One direct proof is to set \(s_{-}=\max\{-s,0\}\). The Yamabe variational formula implies
\[
Y([g])\ge-\|s_{-}\|_{L^{2}},
\]
so every metric in the class satisfies
\[
S(g)\ge \|s_{-}\|_{2}^{2}\ge Y([g])^{2}.
\]
The constant-scalar-curvature Yamabe metric attains \(S=Y([g])^{2}\). Hence
\[
P(\widehat g)\le P(g).
\]

If the available Seiberg–Witten estimate gives
\[
S(\widehat g)\ge32\pi^{2}A,
\]
then
\[
E(\widehat g)
=
\frac{4P(\widehat g)}
{P(\widehat g)+S(\widehat g)/4}
\le
\frac{4P(\widehat g)}
{P(\widehat g)+8\pi^{2}A}
\le
\frac{4P(g)}
{P(g)+8\pi^{2}A}.
\]
Both inequalities have the stated direction because \(x\mapsto4x/(x+c)\) is increasing for \(x,c\ge0\).

Thus the Yamabe shortcut is correct under the stated Seiberg–Witten supply.

For a fixed local cell, Theorem 3.1 gives
\[
P=8\pi^{2}(1-\delta)
\]
with \(\delta>0\) after choosing \(\varepsilon\) sufficiently small, since the logarithmic term dominates the bounded \(O(\varepsilon^{2})\) coefficient. Replication in lifted isometric balls is geometrically consistent.

The precise family formula
\[
\limsup\frac{\alpha(M_{j})}{h_{j}}
\le4(1-\delta\theta)
\]
also uses the balance relations among \(A_{j},Q_{j},h_{j},k_{j}\), and \(\ell_{j}\) from the earlier programme. Those definitions and relations are not present in the supplied files, so that numerical coefficient cannot be independently reconstructed here. The local cell estimate and the Yamabe inequality provide the required new input.

---

## Final scientific status

1. **Lemma 1.1 and the degree count:** correct after fixing the signature/Pontryagin normalization and writing the analytic transgression lemma. No \(h_{4}\) or extra \(W^{-}\otimes W^{-}\) term can contribute to the logarithmic coefficient.

2. **Corollary 1.2:** the squared-sector structure is correct for linear group-stable corrector spaces, with the isotypic decomposition stated explicitly. The phrase that all terms linear in \(W^{-}\) vanish should distinguish a fixed invariant corrector from a spin-\(2\) corrector chosen linearly from \(W^{-}\).

3. **Theorem 2.1:** the exact computation plus irreducibility gives a complete proof for all algebraic \(W^{-}\).

4. **Corollary 2.2:** \(F=-18\) for the explicit \(c^{*}+k_{0}^{W}\) corrector is supported exactly and numerically. Equality of optimized coefficients is valid only for corrector spaces containing \(k_{0}^{W}\); the degree-\(\le2\) data disprove the unrestricted “every class” wording.

5. **Theorem 3.1:** the logarithmic coefficient and the analytic remainder mechanism are sound. The missing scientific substance is the explicit Burns first-variation sphere-flux formula together with the asymptotic comparison to the Ch.5 CH neck. That argument is what establishes the disappearance of the order-\(\varepsilon\) bucket.

6. **Yamabe shortcut:** correct, including the sign of the conformal variation and the monotonicity used in the final estimate.