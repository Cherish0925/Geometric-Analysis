# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 62,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step62_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step62_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Research generation on the decisive remaining quantity in the four-manifold Einstein-gap lower-bound problem. Step 62 (file attached) shows that on M=X#kCP2bar (X minimal general type, A=c1^2(X), SW nonzero) the Einstein defect obeys the exact identity P/8pi^2=(k-kappa)+(upsilon-kappa)/3 at the Yamabe representative, with kappa the conformal Weyl deficit (kappa=A/2-(3/8pi^2)int|W+|^2) and upsilon the Yamabe excess, and LeBrun forces upsilon>=kappa+3kappa^2/4A. Hence the open-range lower bound is governed only by how much self-dual Weyl energy kappa per exceptional class a conformal structure can remove while keeping P small. Generate serious, mathematically specific mechanisms (a) to PROVE a bound kappa<=k+beta*p (or kappa_* = A/2-(3/8pi^2)inf int|W+|^2 <= k, or the stronger Gursky-type kappa<=k/2) — e.g. Weyl-energy localization/epsilon-regularity on blow-up necks, conformal capacity of a (-1)-class, harmonic ASD representatives of E_i and Weitzenböck formulas on Lambda^-, twistor or Penrose-type arguments, Bach-flow monotonicity, use of the full 2^k sign family on the Lambda^- side, orientation reversal with Bauer-Furuta; and (b) to REFUTE it by construction: conformal structures removing more than 8pi^2/3 of W+ energy per CP2bar summand at bounded P (ASD gluing à la Taubes/Donaldson-Friedman, large Burns cores, conformally symplectic or LeBrun-equality almost-Kähler metrics, period-violating approximations of the formal common mode). For each, state the precise inequality or construction, its quantifiers, which known objects (Kähler kappa<=0; certified CH cell kappa≈0.056/class, upsilon≈0.212/class; formal common mode kappa≈k) it must accommodate, and the cheapest decisive calculation. Do not invent literature; name precise knowledge requests if needed.

## Integrated Scientific Memo

# Scientific memo: the exceptional-class Weyl budget

The remaining problem is genuinely a Weyl-energy problem, but two corrections materially change its interpretation:

1. **Small Einstein defect does not, without a Weyl cap, force \(\kappa\sim k\).** The terms in
   \[
   p=k-\kappa+\frac{\upsilon-\kappa}{3}
   \]
   can cancel when \(\kappa>k\). Thus Step 62.D cannot be used to prove the cap it implicitly assumes.

2. **There are two distinct dangerous endpoints:** \(W^+=0\) conformal structures, which maximize \(\kappa=A/2\), and \(W^-=0\) negative Einstein structures, which can have \(p=0\) and \(\kappa\gg k\). Neither endpoint is supplied by the present materials as an actual metric on the required manifold.

The most concrete advances are an exact localization ledger, an explicit second-order obstruction target, and a corrected \(\Lambda^-\) sign-family identity.

Throughout, \(P\) and \(p=P/(8\pi^2)\) refer to the negative Yamabe representative unless stated otherwise. A coupled estimate there implies the same estimate with \(P(g)\) for arbitrary representatives.

## 1. Exact targets and the corrected feasible region

Write \(\mathcal W^\pm=\int|W^\pm|^2\). The proposed estimates are exactly
\[
\boxed{
\begin{aligned}
\kappa\le k+\beta p
&\iff 3\mathcal W^++\beta P\ge4\pi^2(A-2k)\\
&\iff 3\mathcal W^-+\beta P
 \ge4\pi^2(A-9\tau_X)+28\pi^2k,
\end{aligned}}
\tag{1}
\]
and
\[
\boxed{\kappa\le k/2
\iff 3\mathcal W^-\ge4\pi^2(A-9\tau_X)+32\pi^2k.}
\tag{2}
\]
For a ball quotient \(A=9\tau_X\), these require respectively \(7/9\) and \(8/9\) of the \(12\pi^2\) anti-self-dual Weyl energy of an isolated \(\overline{\mathbb{CP}}^{\,2}\) model.

The quantifier matters. A constant \(\beta\) uniform over a family of \(X,k\) yields a uniform \(k^2/A\) law; a constant depending arbitrarily on \(M\) does not determine the asymptotic coefficient. The pure cap is nontrivial only for \(k<A/2\); the task’s open range \(k<A/3\) lies within that interval.

### The exact LeBrun envelope

For \(0\le\kappa\le A/2\), put \(y=\sqrt{1-2\kappa/A}\). The supplied mixed estimate gives
\[
\upsilon_L(\kappa)-\kappa=\frac{3A}{4}(1-y)^2,
\]
hence
\[
\boxed{
p\ge L_A(k,\kappa)
=k-\kappa+\frac A4(1-y)^2.}
\tag{3}
\]
This fixed-\(\kappa\) bound remains valid above \(4A/9\); it reaches its minimum \(k-A/3\) at \(\kappa=4A/9\), then increases. The unconditional minimum does not replace the stronger fixed-\(\kappa\) inequality.

Retaining the period quantity \(\Pi\) improves (3) by
\[
\frac{3\Pi}{4}
-\frac{\sqrt{A-2\kappa}}2
 \bigl(\sqrt{A+\Pi}-\sqrt A\bigr).
\]
For \(\kappa\ge0\), this improvement is at least \(\Pi/2\). Therefore
\[
\boxed{
p\ge k-\kappa+\frac{\kappa^2}{4A}+\frac{\Pi}{2}.}
\tag{4}
\]

In the small-\(h=k/A\) regime, parameterize
\[
\kappa=k+q\frac{k^2}{A}+o(k^2/A),\quad
p=r\frac{k^2}{A}+o(k^2/A),\quad
\Pi=\pi_{\rm per}\frac{k^2}{A}+o(k^2/A).
\]
Then
\[
\boxed{q+r\ge\frac14+\frac{\pi_{\rm per}}2.}
\tag{5}
\]
Additional LeBrun or Cauchy–Schwarz slack raises the right-hand side. This is the useful second-order diagnostic:

- pure cap: \(q\le0\);
- coupled cap: \(q\le\beta r\);
- formal common mode: \((q,r,\pi_{\rm per})=(0,1/4,0)\);
- algebraic Einstein endpoint: \((q,r,\pi_{\rm per})=(1/4,0,0)\).

The first zero of (3), for \(0<k<A/3\), is
\[
\kappa_E(k)=\frac A9\left(2+6\frac{k}{A}
-2\sqrt{1-3\frac{k}{A}}\right)
=k+\frac{k^2}{4A}+O(k^3/A^2).
\tag{6}
\]
Thus the existing inequalities allow Einstein data with \(\kappa>k\). Exact equality at this first endpoint would also demand the equality structure and vanishing periods; its geometric realization is a separate, much stronger problem.

### What the existing \(\Lambda^+\) estimates can and cannot prove

Optimizing the weighted quadratic consequences of LeBrun’s envelope gives
\[
\mathcal W^++tY^2\ge
\frac{72\pi^2At}{1+6t}.
\]
For (1), the required weight is
\[
t_\beta=\frac{\beta}{12(3+4\beta)}.
\]
Comparison of constants shows that these scalar–\(W^+\) inequalities alone imply the coupled cap precisely in the band
\[
\boxed{k\ge A\frac{1+\beta}{2+3\beta}.}
\tag{7}
\]
The threshold tends to \(A/3\) as \(\beta\to\infty\). This is an algebraic limitation of the envelope, not a theorem that all richer SW information is ineffective. It identifies exactly what new information must accomplish below \(A/3\).

### Calibration

| Object | \(\kappa/k\) | \(\upsilon/k\) | \(p/k\) |
|---|---:|---:|---:|
| Kähler recovery | \(0\), approached from below | \(0\) | \(1\) |
| Certified CH cell ledger | \(\approx0.05635\) | \(\approx0.21238\) | \(\approx0.99566\) |
| Formal common mode, \(h\to0\) | \(1-O(h^2)\) | \(1+\tfrac34h+O(h^2)\) | \(\tfrac14h+O(h^2)\) |

All three accommodate the pure and coupled caps. The strong cap accommodates the two genuine calibration families but **excludes realization of the formal common mode**. That distinction must remain explicit. The supplied cell ledger is not itself a closed replica construction.

Without a cap, \(p/k\to0\) need not imply \(\kappa/k\to1\), \(\upsilon-\kappa=o(k)\), or \(\Pi=o(k)\). With the pure cap, (4) does force \(k/A\to0\), \(\kappa/k\to1\), and \(\Pi/k\to0\).

## 2. Most direct proof/refutation mechanism: relative \((-1)\)-capacity

### A precise local problem

For a ball-quotient host normalized to \(s=-4\), replace a CH ball \(B_R\) by a smooth core \(C\) carrying one exceptional generator, with the same metric on an open collar. Define
\[
c(C)=\frac{3}{8\pi^2}
 \left(\mathcal W^+(B_R)-\mathcal W^+(C)\right),\qquad
e(C)=\frac{P(C)}{8\pi^2}.
\tag{8}
\]
Since \(|W^+_{\rm CH}|^2=2/3\),
\[
c(C)\le\frac{\operatorname{Vol}(B_R)}{4\pi^2}.
\tag{9}
\]
A necessary condition for a one-core violation \(c>1\) is therefore removal of CH volume exceeding \(4\pi^2\).

More importantly, cancellation of the signature transgression on identical collars gives the exact relative ledger
\[
\mathcal W^+(C)-\mathcal W^-(C)-\mathcal W^+(B_R)
=-12\pi^2,
\]
or
\[
\boxed{c(C)=\frac92-\frac{3}{8\pi^2}\mathcal W^-(C).}
\tag{10}
\]
Consequently, the local coupled-cap target is exactly
\[
\boxed{3\mathcal W^-(C)+\beta P(C)\ge28\pi^2.}
\tag{11}
\]
For a rank-\(q\) core, replace the right-hand side by \(28\pi^2q\). The strong target is \(32\pi^2q\).

This avoids assigning an invariant “energy of the exceptional sphere” before specifying the boundary geometry. With only asymptotic or mismatched collars, (10) needs an explicit signature transgression; it cannot be silently discarded.

### Quantifiers and limitations

A theorem asserting (11) for **every smooth core with fixed CH collar**, or a suitably uniform class of ACH ends, would establish the cap for exact-CH cell replacements. It would not yet establish the all-metric theorem:

- an arbitrary conformal structure need not admit a CH exterior;
- exceptional classes may cluster, collapse, or mix with the residual topology;
- for general-type hosts, the residual requirement
  \[
  3\mathcal W^-+\beta P\ge4\pi^2(A-9\tau_X)
  \]
  on a punctured minimal-model component is another theorem, not an automatic allocation.

The source’s localized CH coercivity is useful precisely in its stated regime. It controls exterior perturbations and boundary mismatch, but does not supply core capacity.

An isolated ASD \(\overline{\mathbb{CP}}^{\,2}\) model has \(\mathcal W^-=12\pi^2\), leaving an \(8\pi^2\) reserve in \(3\mathcal W^-\) relative to (11). This reserve is not itself a proof: a macroscopic splice can alter the interface ledger. Conversely, “large Burns cores always give \(\kappa\approx0\)” is too strong; the Burns model’s energy does not determine the energy of its CH transition.

### Cheapest decisive calculation

Use the existing biaxial/Bianchi IX machinery to compute the Pareto frontier
\[
\Phi_R(e_0)=
\sup\{c(C): C\text{ closes smoothly on an }O(-1)\text{ bolt},
\ C=\mathrm{CH}\text{ near }\partial B_R,\ e(C)\le e_0\}.
\tag{12}
\]
Compute the relative \(W^\pm\), \(P\), and boundary signature ledger independently. Scalar \(-4\) is a useful numerical constraint, not necessary for a pure Weyl-cap counterexample.

The separating tests are:

- \(\Phi_R(e_0)>1/2\): refutes the strong all-conformal-class cap;
- \(\Phi_R(e_0)>1\): refutes the pure cap;
- \(c>1+\beta e\): refutes the specified coupled cap, since global Yamabe normalization only lowers \(P\).

A validated profile below the capacity threshold proves only the corresponding ansatz theorem. A validated violating profile, with genuine smooth collar matching, is much more decisive: one can insert it into an appropriate host.

For replication, the precise additional inputs are compact CH hosts or covers containing sufficiently many disjoint \(R\)-balls, smooth closed gluing, and control of any nonexact collar error. No global Yamabe solve is needed to refute the pure cap; it is needed only to sharpen the measured coupled frontier.

## 3. Harmonic exceptional forms: a real \(\Lambda^-\) channel, with a specific obstruction

Let \(\eta_i\) be harmonic representatives of \(E_i\). Their Gram matrices satisfy
\[
G^-_{ij}=\delta_{ij}+G^+_{ij}.
\tag{13}
\]
Thus the exceptional subspace supplies at least \(k\) units of ASD harmonic mass. At \(s=-4\),
\[
2\int W^-(\eta_i^-,\eta_i^-)
=\|\nabla\eta_i^-\|_2^2-\frac43\|\eta_i^-\|_2^2.
\tag{14}
\]
Set
\[
\rho=\sum_i\eta_i^-\otimes\eta_i^-,
\qquad \rho_0=\rho-\frac{\operatorname{tr}\rho}{3}I.
\]
Then
\[
2\int\langle W^-,\rho_0\rangle
=D,\qquad
D=\sum_i\|\nabla\eta_i^-\|_2^2
-\frac43\sum_i\|\eta_i^-\|_2^2,
\]
and hence, when the denominator is nonzero,
\[
\boxed{\mathcal W^-\ge
\frac{D^2}{4\int|\rho_0|^2}.}
\tag{15}
\]

This is substantive but not yet a topological Weyl floor. The missing statement is an estimate controlling **anisotropy and concentration**, not merely \(G^-\ge I\):

- pointwise isotropy can make \(\rho_0\) small;
- derivative and negative scalar contributions can cancel in \(D\);
- concentration can make the denominator large.

A plausible proof mechanism is a diffuse/concentrated dichotomy: derive a connection/frame estimate on diffuse regions, and apply relative capacity to concentrated rank-\(q\) clusters. The numerical constants \(28\pi^2\) or \(32\pi^2\) must emerge from that estimate, rather than being inserted into a restatement of the desired theorem.

**Cheapest calculation:** solve the harmonic exceptional-form ODE on the Burns and certified cells, and record separately
\[
\|\eta^-\|_2^2,\quad
\|\nabla\eta^-\|_2^2,\quad
\int|\rho_0|^2,\quad
\int W^-(\eta^-,\eta^-).
\]
This identifies whether the observed energy surplus is accessible to (15), or is primarily an interface phenomenon.

### Corrected full-sign-family identity

There is a useful extension, but the differential identities in the first branch need correction. Let \(f_\varepsilon=F_\varepsilon/(2\pi i)\), so its cohomology class is \(a_\varepsilon\). Closedness gives
\[
df_\varepsilon^-=-df_\varepsilon^+,
\qquad
d^*f_\varepsilon^-=d^*f_\varepsilon^+,
\]
not the negative sign stated there. The Hodge Laplacian preserves \(\Lambda^\pm\); its two-form Weitzenböck curvature term is \(s/3-2W^\pm\), with no off-diagonal \(\operatorname{Ric}^\circ f^+\) term. Therefore
\[
\boxed{
2\int W^-(f_\varepsilon^-,f_\varepsilon^-)
=\|\nabla f_\varepsilon^-\|_2^2
-\frac43\|f_\varepsilon^-\|_2^2
-2\|df_\varepsilon^+\|_2^2.}
\tag{16}
\]
The averaged mass still satisfies
\[
2^{-k}\sum_\varepsilon\|f_\varepsilon^-\|_2^2
\ge |K_X^-|^2+\sum_i|E_i^-|^2\ge k.
\tag{17}
\]
But the spinor-source term in (16) has an unfavorable sign. A successful completion must control it and extract trace-free covariance. Exceptional mass alone does not yield exceptional Weyl energy.

A particularly informative finite calculation is the Walsh decomposition of \(f_\varepsilon\): its first-order coefficients are closed representatives of the individual \(E_i\). Deriving the exact averaged identity and bounds for \(df_\varepsilon^+=d\,q(\Phi_\varepsilon)\) tests whether the hypercube supplies information genuinely absent from the scalar envelope.

### Reverse-orientation almost-Kähler gauge

For a harmonic ASD form \(\psi\) without zeros, the conformal metric
\[
g_\psi=(|\psi|_g/\sqrt2)\,g
\]
makes \(\psi\) an almost-Kähler form on \(\bar M\). If \(m=\|\psi\|_{L^2(g)}^2\), then \(\operatorname{Vol}(g_\psi)=m/2\). The Hermitian scalar identity gives
\[
B:=4\pi c_1(J_\psi)\cdot[\psi]
-\frac23\int s_{g_\psi}\,d\mu_{g_\psi}
=\int W^-(\psi,\psi)\,d\mu_{g_\psi},
\]
and
\[
\boxed{\mathcal W^-\ge\frac{3B^2}{4m}.}
\tag{18}
\]
To reach \(28\pi^2/3\), one needs
\[
|B|\ge \frac{4\sqrt7}{3}\pi\sqrt m.
\]
For forms with zero circles, singular conformal geometry and boundary corrections must be included. Moreover, applying (18) separately to \(k\) forms does not permit adding \(k\) lower bounds on the same energy.

The precise knowledge needed is the zero-set correction to the Hermitian scalar identity, plus control of \(c_1(J_\psi)\cdot[\psi]\) and the conformal scalar integral. Computing these quantities on the existing cells is cheaper than assuming a universal exceptional Chern pairing.

## 4. Critical-metric and localization routes: what would make them valid

For \(\beta>0\), the all-metric coupled cap is the variational assertion
\[
\inf_g\mathcal J_\beta(g)\ge4\pi^2(A-2k),
\qquad
\mathcal J_\beta=3\mathcal W^++\beta P.
\tag{19}
\]
Within each conformal class, its minimum occurs at the Yamabe representative.

A critical-metric approach would need:

1. controlled minimizing or suitably stationary sequences;
2. noncollapse/Sobolev control, or an explicit treatment of collapse;
3. bubble and interface energy accounting retaining exceptional lattice rank;
4. capacity bounds on the limiting pieces.

Small \(P\) alone supplies no elliptic regularity for arbitrary metrics. Even for critical metrics, the proposed branch estimate using only small \(\int(|W|^2+|\operatorname{Ric}^\circ|^2)\) needs a scalar term: at \(s=-4\), a local estimate must include an \(r^2\) background contribution or full curvature energy. These hypotheses cannot be hidden inside “epsilon-regularity.”

The positive-Yamabe Gursky argument does not transfer directly. For harmonic \(W^+\),
\[
0=\int\left(|\nabla W^+|^2+\frac s2|W^+|^2-18\det W^+\right),
\]
and the scalar term is negative here. A new SW, critical-equation, or exceptional-frame term is required.

A softened strong estimate
\[
\mathcal W^+\ge\frac{4\pi^2}{3}(A-k)-cP
\iff \kappa\le k/2+3c\,p
\tag{20}
\]
would still exclude the formal common mode for fixed \(c\) as \(k/A\to0\). The cheapest algebraic test is the exact integrated Bach identity paired with \(\operatorname{Ric}^\circ\), retaining the indefinite cubic terms. The schematic estimate proposed by a branch is not established by the supplied sources.

There is also a useful simplification specific to CH hosts: on the **closed unblown-up** ball quotient,
\[
\mathcal W^+=12\pi^2\tau_X+\mathcal W^-,
\qquad W^-_{\rm CH}=0.
\]
Thus CH already minimizes \(\mathcal W^+\) among all metrics on that topology. A same-topology Hessian calculation cannot reveal a negative Weyl direction. On punctured regions, negative relative variation must come through boundary transgression; the local problem is again interface capacity.

Bach flow decreases Weyl energy, hence increases \(\kappa\), but need not decrease \(P\) or preserve a usable collar. It is a construction mechanism only if the trajectory satisfies a measured favorable tradeoff in \((\kappa,p)\). A gradient flow of \(\mathcal J_\beta\) is variationally more aligned with (19), but monotonicity alone proves no topological lower bound.

## 5. Construction endpoints: distinguish ASD from self-dual Einstein

### A. ASD conformal structures: \(W^+=0\)

Every such structure has
\[
\kappa=A/2,
\qquad p\ge k-A/4.
\tag{21}
\]
The second inequality is the exact fixed-\(\kappa\) LeBrun bound, stronger here than the unconditional \(k-A/3\) bound. Signature also requires
\[
k\ge\tau_X.
\tag{22}
\]

Therefore an actual ASD structure:

- refutes the pure cap if \(k<A/2\);
- refutes the strong cap if \(k<A\);
- refutes the specified coupled cap if
  \[
  p<\frac{A/2-k}{\beta}.
  \]

For ball quotients, the conformal search interval begins at \(k=A/9\). An ASD Einstein candidate must satisfy
\[
\boxed{A/9\le k\le A/4.}
\tag{23}
\]
This corrects the first branch’s search interval by including the signature requirement.

Taubes/Donaldson–Friedman gluing is decisive only with a quantitative blow-up count and, for the coupled estimate, Ricci-energy control. The index
\[
\operatorname{ind}_{ASD}
=\frac12(15\chi_X+29\tau_X)-7k
=\frac{37}{9}A-7k
\]
for a ball quotient is not an existence threshold. Extracting the actual obstruction space killed per summand is the cheap discriminating literature calculation.

### B. Self-dual negative Einstein structures: \(W^-=0\)

For a ball-quotient topology, Einstein and self-dual bookkeeping gives
\[
\boxed{
\kappa=\frac92k,\qquad
\upsilon=15k,\qquad
p=0,\qquad
\operatorname{Vol}=2\pi^2A+30\pi^2k.}
\tag{24}
\]
For \(0<k\le A/9\), these data satisfy the displayed scalar/mixed LeBrun constraints. In particular,
\[
2\sqrt{A+15k}+\sqrt{A-9k}\ge3\sqrt A.
\]
They directly demonstrate why Step 62.D’s cancellation argument fails. They are **formal global data**, not an existence result and not a verification of all field or differential equations.

An actual compact metric realizing (24) would refute every finite-\(\beta\) coupled cap and give \(P=0\). This is a serious alternative to the near-LeBrun-equality endpoint: it has substantial LeBrun slack and does not require \(\Pi\to0\).

Two local restrictions are useful:

- A conformally flat neighborhood of a \((-1)\)-sphere is impossible. Its simply connected disk bundle would develop locally diffeomorphically into \(S^4\), making its tangent bundle spin, whereas its restriction to the zero section has nonzero \(w_2\).
- An exact self-dual Einstein cell cannot agree with CH on an open collar and then differ inside; Einstein unique continuation forces local CH continuation.

The first restriction excludes placing the exceptional sphere inside a purely real-hyperbolic pocket. It does **not** exclude a non-conformally-flat self-dual Einstein bolt.

The definite-connection route deserves a sharply bounded test. For \(W^-=0\) and \(\operatorname{Ric}^\circ=0\), the \(\Lambda^-\) connection has curvature \((s/12)I\) in the ASD block. Investigate whether this can occur near an \(O(-1)\) bolt. Restriction of an \(SO(3)\) bundle to \(S^2\) is classified by \(w_2\); there is no \(p_1\) degree on \(S^2\). Odd \(w_2\) alone does not rule out a definite connection.

**Cheapest calculation:** check the regular-bolt expansions and topology of the explicitly named Pedersen or Calderbank–Pedersen families, then calculate the CH matching cost. This is a knowledge request, not an assertion that these families realize the required bolt.

## 6. Period-degenerate, almost-Kähler constructions

The formal common mode lies at the leading-order pure-cap boundary. Merely approximating it would test the \(k^2/A\) coefficient, not refute \(\kappa\le k\). A refutation requires a positive second-order \(q\).

A geometrically meaningful target is a sequence of actual smooth metrics, with \(k/A\to0\), satisfying
\[
\kappa=k+q\frac{k^2}{A}+o(k^2/A),\qquad
p=r\frac{k^2}{A}+o(k^2/A).
\tag{25}
\]
The desired outcomes are \(q>0\) for a pure-cap counterexample, or \(q>\beta r\) for a coupled counterexample. Equation (5) quantifies the cost of period opening. To approach the ideal line \(q+r=1/4\), both \(\Pi\) and equality slack must be \(o(k^2/A)\), not merely \(o(k)\).

Exact LeBrun equality with \(\Pi=0\) conflicts with the supplied Taubes exceptional-period obstruction. Approximating equality may still be possible through collapse; no quantitative lower bound on that approximation cost is present.

A Lyapunov–Schmidt expansion cannot legitimately start at the formal common tensor: no underlying closed metric or invertible linearization has been supplied. Before such an expansion, one needs an actual approximate solution, its residual in the full geometric/field equations, and a controlled inverse modulo genuine kernels.

A cheaper available calculation is the rotated-cell expansion
\[
\kappa(\psi)=\kappa_0+a\psi^2+\cdots,\quad
p(\psi)=p_0+b\psi^2+\cdots,\quad
\Pi(\psi)=c\psi^2+\cdots.
\tag{26}
\]
A frame rotation alone preserves \(|W^+|^2\); \(a\) comes from the actual metric correction, not from period rotation. The sources do not establish these coefficients. Since \(\kappa_0\approx0.056\), small rotations of this cell cannot by themselves reach \(1/2\) or \(1\), but their coefficients can expose the mechanism that must be continued nonperturbatively.

An interface/collapse construction should retain the Step 61 linking-form and lattice ledger. In particular, replacing a \((-1)\)-class by an \(A_1\), Wahl, or other orbifold resolution without checking the integral lattice does not construct the specified \(X\#k\overline{\mathbb{CP}}^{\,2}\).

## 7. Twistor and reverse-orientation inputs: precise scope

Twistor/Penrose methods are naturally suited to an ASD endpoint \(\mathcal W^+\to0\), not a slight violation of \(\kappa\le k\) when \(k/A\ll1\): there \(\mathcal W^+\) remains order \(A\). A quantitative twistor argument needs curvature/noncollapse control upgrading small twistor Nijenhuis tensor from \(L^2\) to a deformation-theoretically useful norm. None is supplied.

Orientation reversal converts (1) to a \(W^+\) estimate on
\[
\bar M=\bar X\#k\mathbb{CP}^2.
\]
Useful monopole or Bauer–Furuta data must be computed there; they cannot be inherited by reversing orientation. Ordinary reverse-orientation mixed estimates would still involve scalar energy. The genuinely new requirement is an invariant or family invariant retaining the \(k\) positive generators and producing a Weyl-only or Weyl–\(P\) estimate.

The first calculation is the connected-sum stable class, its expected dimensions, and relevant vanishing hypotheses. The branches’ expectation of vanishing is not established by the supplied sources.

## Decisive remaining objects and knowledge requests

The supplied material does not close an all-metric cap. It reduces the unresolved content to concrete objects:

1. **Relative core frontier:** a rigorously computed or proved inequality
   \[
   \sup_C\bigl(c(C)-\beta e(C)\bigr)\le1
   \]
   for smooth CH-collared \((-1)\)-cores, including clustered rank-\(q\) cores. This is the closest calculation to both proof and counterexample.

2. **Diffuse exceptional-frame estimate:** a bound supplementing (15)–(17) that converts harmonic/sign-family mass into trace-free ASD curvature, with concentration charged to core capacity.

3. **Actual second-order metrics:** coefficients \(q,r,\pi_{\rm per}\) in (25), satisfying the full equations rather than only the curvature ledger. Their signs distinguish a cap from a near-Einstein continuation.

4. **Quantitative ASD/SDE existence input:** actual gluing thresholds, bolt topologies, and Yamabe Ricci costs.

Precise literature requests are: LeBrun’s complete mixed-estimate equality analysis; APS/ACH signature transgressions with normalizations and fixed CR boundary data; negative-Yamabe compactness for critical quadratic-curvature metrics; quantitative Taubes and Donaldson–Friedman obstruction counts; topology of negative self-dual Einstein bolt families; definite-connection obstructions on odd disk bundles; and reverse-orientation Bauer–Furuta connected-sum/vanishing results.

The key distinction is now sharper than a scalar susceptibility question: **a proof must prevent smooth cores, interfaces, or global Einstein phases from extracting the exceptional ASD-energy reserve; a counterexample must exhibit that extraction with the full topological and Ricci ledger intact.**