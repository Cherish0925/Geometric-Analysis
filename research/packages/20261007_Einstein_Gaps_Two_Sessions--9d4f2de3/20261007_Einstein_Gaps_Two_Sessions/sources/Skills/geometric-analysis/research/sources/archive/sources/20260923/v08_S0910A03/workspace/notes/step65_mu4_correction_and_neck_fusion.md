# Step 65: \(\mu_4\) lower bound and entropy–slice exploration — corrected in Step 67

> **Step 67 correction.** Retain the nonzero-normalization Chern–Weil lower bound and the explicit negative-scalar \(T^3\) computation. Withdraw the claimed exact determination of \(\mu_4\), the noncollapsed Ricci-flat coercivity statement, the higher-genus-product example, the ambient dimension cascade, and every curved-collar closure. See `step67_corrections_and_analytic_neck_reopening.md`.

Session: S0910A03. Agent2 / Constructor. Phase: Explore.
Companion script: `workspace/scripts/step65_mu4_and_slice_mechanism.py`;
data: `workspace/data/step65_mu4_and_slice_mechanism.json`.

This note (i) corrects the Step 64 record on the slice-defect invariant
\(\mu_4\), as mandated by the Strategist, (ii) states the corrected slice-defect
cascade, (iii) extracts the gap-theorem consequences that were overlooked, and
(iv) builds the requested fusion: a concrete, checkable program connecting the
CSS entropy near-equality of Step 64 to the Step 63 flat-slice barrier.

---

## 1. Correction: \(\mu_4\) is not unknown — it is a special case of the Step 2 estimate

### 1.1 The Gauss–Bonnet pinching bound

On any closed oriented 4-manifold, the Chern–Gauss–Bonnet formula reads
\[
8\pi^2\chi(M)=\int_M\Bigl(|W|^2+\tfrac{s^2}{24}-\tfrac{|\mathring{\operatorname{Ric}}|^2}{2}\Bigr)d\mu ,
\qquad \mathring{\operatorname{Ric}}=\operatorname{Ric}-\tfrac{s}{4}g .
\]
If \(\|\operatorname{Ric}-\Lambda g\|_{\mathrm{op}}\le\delta|\Lambda|\) with
\(\delta\in[0,1)\), then at every point
\[
s^2/24\ \ge\ \tfrac{2}{3}\Lambda^2(1-\delta)^2,
\qquad
\tfrac12|\mathring{\operatorname{Ric}}|^2\ \le\ 2\delta^2\Lambda^2 ,
\]
so, since \(|W|^2\ge0\),
\[
\chi(M)\ \ge\ \frac{\operatorname{Vol}(M)\,\Lambda^2}{8\pi^2}
\Bigl[\tfrac23(1-\delta)^2-2\delta^2\Bigr].
\]
The bracket vanishes exactly at \(\delta=\delta_0\), where
\[
\tfrac23(1-\delta_0)^2=2\delta_0^2
\quad\Longrightarrow\quad
\delta_0=\frac{\sqrt3-1}{2}\approx0.3660 ,
\]
and is positive for \(\delta<\delta_0\) (verified numerically, Part A of the
script; the equality at \(\delta_0\) holds to machine precision). Hence

> **Chern–Weil exclusion (same as Step 2's \(2\chi>3|\tau|\) corollary, with
> \(\tau=0\)).** Every closed 4-manifold with \(\chi(M)\le0\) admits **no**
> metric with \(\|\operatorname{Ric}-\Lambda g\|_{\mathrm{op}}<\delta_0|\Lambda|\),
> for any \(\Lambda\ne0\). On such a manifold, for every metric and every
> \(\Lambda\ne0\),
> \(\|\operatorname{Ric}-\Lambda g\|_{\mathrm{op}}\ge\delta_0|\Lambda|\).

The role of the Weyl tensor is the opposite of what the Step 64 caveat claimed:
\(|W|^2\) sits on the **forced-positive** side of the identity, so it only
*worsens* the deficit for a pinched metric. There is no Weyl cancellation of
the scalar-versus-trace-free mismatch.

### 1.2 Consequences

**(a) A lower bound for \(\mu_4\).**
\[
\mu_4\;=\;\inf_{\gamma\in\mathcal M(T^4)}\|\operatorname{Ric}_\gamma+3\gamma\|_{C^0}
\;\ge\;3\,\delta_0\;=\;\frac{3(\sqrt3-1)}{2}\;\approx\;1.0981 .
\]
In particular \(\mu_4>0\). This does not determine the exact infimum.

**(b) The slice-defect cascade.** For unit-volume \(T^m\) metrics:

| \(m\) | mechanism | bound |
|---|---|---|
| 2 | Gauss–Bonnet \(\int R\,dA=0\) vs \(R\to-2\) | \(\mu_2=1\) |
| 3 | \(\|\operatorname{Ric}+2g\|_{\mathrm{op}}<2/3\Rightarrow K<0\); Preissmann excludes \(\mathbb Z^3\) | \(\mu_3\ge2/3\) |
| 4 | Chern–Gauss–Bonnet, above | \(\mu_4\ge1.098\) |
| \(\ge5\) | **no known mechanism** | \(\mu_5,\dots\) open |

The obstruction genuinely opens only at slice dimension \(\ge5\): for odd \(m\ge5\)
there is no Euler characteristic and no Preissmann control (Ricci does not
control sectional curvature in \(m\ge4\), and dimension 4 is saved only by
Gauss–Bonnet). Determining \(\mu_5\) is adjacent to a known hard open problem —
whether \(T^n\), \(n\ge5\), can approach negative Einstein metrics, equivalently
the exotic-torus question of whether a negative Einstein metric can exist on an
exotic torus — so \(\mu_5\) is **monitored, not attacked**.

**(c) A cheap absolute gap class (both signs).** Every closed 4-manifold with
\(2\chi\le3|\tau|\) — the Hitchin–Thorpe non-strict-failure class, e.g.
\(T^4\) (\(0=0\)), K3 (\(48=48\)), \(\#_k\mathbb{CP}^2\) and
\(\#_k\overline{\mathbb{CP}}{}^2\) with \(k\ge4\) (equality at \(k=4\),
violators beyond), (no product \(\Sigma_g\times\Sigma_h\) with \(g,h\ge2\): those have \(\chi>0,\tau=0\) and admit an Einstein product) — carries **no**
metric pinched below \(\delta_0|\Lambda|\) of *either* sign.
(\(\#_k(S^2\times S^2)\) is **not** in this class: \(2\chi-3|\tau|=4+4k>0\);
nor are A02's balanced \(\chi=8\) mixed rows, which all have
\(2\chi-3|\tau|\in\{4,10,16\}\).) This is a
topological class gap at a fixed absolute threshold, with no entropy,
Seiberg–Witten, compactness, or no-Einstein input; the exclusion holds even
though these manifolds' Einstein status is irrelevant. For Yau 26 it kills the
counterexample direction on this whole class in one line: the class cannot
carry *any* tight metric, hence cannot witness the failure of either branch.
The Di Cerbo extended graph manifolds escape this cheap mechanism only because
their hyperbolic pieces force \(\chi>0\) (they satisfy \(2\chi>3|\tau|\) — they
are *not* Hitchin–Thorpe violators), which is precisely why they require the
harder entropy machinery.

**(d) Withdrawn Ricci-flat-scale inference.** The former assertion that \(\operatorname{Vol}\ge1\) and \(|s|\le1\) force \(\int|\operatorname{Ric}|^2\ge1/3\) is false; a unit-volume flat torus is a counterexample. The Chern–Weil estimate above requires a fixed nonzero Einstein normalization \(\Lambda\ne0\).

### 1.3 What was wrong in Step 64

`step64_mu4_bifurcation.md` claimed (i) \(\mu_4\) unknown, (ii) "Weyl absorbs
the discrepancy", (iii) a caveat retracting the Euler-characteristic argument
as "vacuous". All three are backwards; (ii) and (iii) contradict the sign
structure of the Chern–Gauss–Bonnet integrand. The peer circulation
(#448, #449, #450) inherited the error; a correction message is sent in this
step. The surviving content of that file is recorded in
`step64_mu4_cascade_corrected.md`.

---

## 2. The fusion program: forcing the \(O(1)\) defect into the neck

Step 64 showed the Di Cerbo exclusion is equality-saturated: under
\(\|\operatorname{Ric}+3g\|_\infty\le\delta\) the CSS inequality
\(h(g)\operatorname{Vol}_g(M)^{1/4}\ge3P^{1/4}\) combined with the degraded
Bishop–Gromov bound \(h\le3+\delta\) gives only
\(\operatorname{Vol}\ge(1-\tfrac{4\delta}{3}+O(\delta^2))\,P\) — the margin
relaxes instead of binding. The Strategist's fusion question: **does
near-equality in this chain force the \(O(1)\) defect to localize into the neck
region, where the flat-slice barrier then applies?**

### 2.1 Setting and geometric identities

Let \(M\) be a closed extended graph 4-manifold with pieces
\(\{(V_i,g_{-1})\}_{i=1}^k\), \(P=\sum_i\operatorname{Vol}_{g_{-1}}(V_i)\),
and let \(g\) satisfy \(\|\operatorname{Ric}+3g\|_{\mathrm{op}}\le\delta\),
\(\delta<3/2\). Every piece carries its JSJ toral boundary; choose, in a collar
of each boundary component, a local warped model
\(g=dr^2+\gamma_r\), \(\gamma_r\) a metric on \(T^3\), with
\(S=\tfrac12\gamma_r^{-1}\gamma_r'\), \(H=\operatorname{tr}S\), and define the
**slice anisotropy**
\[
\Psi(r)\;:=\;|S|^2-\tfrac13H^2\;=\;|\mathring S|^2\ \ge\ 0 .
\]

**Warped-collar identities** (Part C of the script; both residuals
\(\sim10^{-16}\)):
\[
\tag{G} R(\gamma_r)\;=\;R_M-2\operatorname{Ric}(\nu,\nu)+H^2-|S|^2 ,
\qquad
\tag{R} H'\;=\;-\operatorname{Ric}(\nu,\nu)-|S|^2 .
\]
Under the pinching, \(R_M=-12+\rho\), \(\operatorname{Ric}(\nu,\nu)=-3+e\),
\(|\rho|\le4\delta\), \(0\le e\le\delta\), whence
\[
\tag{G$'$} R(\gamma_r)\;=\;-6+H^2-|S|^2+(\rho-2e),
\qquad
\tag{R$'$} H'\;=\;3-|S|^2-e .
\]

### 2.2 The slice-level forced-defect lemma and the transition cost

**Lemma (slice defect, Preissmann scale).**
\(\|\operatorname{Ric}_{\gamma}+2\gamma\|_{\mathrm{op}}<\tfrac23\) is impossible
on \(T^3\): in dimension 3, \(\operatorname{Ric}\le(-2+\tfrac23)\gamma\) forces
every sectional curvature \(K\le-\tfrac23<0\), and Preissmann excludes
\(\mathbb Z^3\) from a closed negatively curved manifold.

Writing \(D(\gamma):=\|\operatorname{Ric}_\gamma+2\gamma\|_{C^0(\gamma)}\ge2/3\):

- At a **near-minimal slice** (\(H^2\le\tfrac14\), \(\delta<1/8\)): (G$'$) gives
  \(R(\gamma_r)\le-5+O(\delta)\), hence
  \(s=\operatorname{tr}\operatorname{Ric}_\gamma\le-5+O(\delta)\), so
  \(s+6\ge1-O(\delta)\) and
  \[
  D(\gamma_r)\ \ge\ \tfrac{s+6}{3}\ \ge\ \tfrac13-O(\delta).
  \]
- At **any** slice with \(|H|\le2\): the same computation gives
  \(D(\gamma_r)\ge\tfrac19\) for \(\delta\le1/10\), decaying to \(0\) only at
  \(|H|=3\) (the exact-Einstein value).

So the slice defect is **uniformly \(O(1)\) away from the calibrated value
\(H^2=9\), \(\Psi=0\)** — and the Step 63 barrier \(H^2\ge9-6\delta\) forbids
\(H\) from *crossing* that value with the right sign structure (a contracting
cusp, \(H>0\), cannot reach \(H=0\)).

**Raychaudhuri transition cost.** Integrating (R$'$) between slices \(r_1<r_2\),
\[
\tag{C} H(r_2)-H(r_1)\;=\;\int_{r_1}^{r_2}\bigl(3-e-\Psi-\tfrac13H^2\bigr)\,dr .
\]
Near the calibrated regime (\(H^2\approx9\), \(\Psi\approx0\), \(e\approx0\))
the integrand is \(\approx0\): the shape operator can *remain* near calibration
only by staying isotropic. Any departure of \(\Psi\) from \(0\), or of \(H^2\)
from \(9\), contributes a definite signed drift to \(H\). The cost of moving
from the piece-interior profile toward any non-calibrated slice profile is
therefore *visible in \(H\)*, and the barrier forbids the sign change — this is
the quantitative content of "the neck cannot be threaded."

### 2.3 The conjecture (fusion statement)

> **Conjecture F (forced localization).** There exist
> \(\delta_0\in(0,\tfrac32)\) and \(c>0\), depending only on the combinatorial
> type of the dual graph, such that every metric on a closed extended graph
> 4-manifold \(M\) with \(\|\operatorname{Ric}+3g\|_{\mathrm{op}}\le\delta_0\)
> satisfies the following: at least one piece \(V_i\) has a toral collar
> carrying a slice \(\gamma_r\) with \(D(\gamma_r)\ge c\). Equivalently: no
> tight metric can make *every* JSJ collar simultaneously
> \((H^2,\Psi,e)\)-near-calibrated.

The chain (G$'$)/(R$'$) + barrier + slice lemma proves Conjecture F in the
**doubly-warped model class** — collars of the form \(dr^2+\gamma_r\) with the
pinching imposed as a constraint — since there \(H^2\ge9-6\delta\) on the
contracting side and any slice with \(H^2\le\tfrac14\) already has
\(D\ge\tfrac13-O(\delta)\). What is missing for the full statement is exactly
the entropy input: forcing at least one collar to leave the calibrated band
without assuming a warped model. That missing input is the analytic heart of
the program and is where the CSS/Jacobian structure must enter.

### 2.4 Analytic route 1 — Jacobian chain localization

The CSS inequality is proved through the universal cover \(\widetilde M\):
the Jacobian \(J(t,\theta)\) of the geodesic exponential map on the unit
tangent bundle satisfies
\[
h(g)\ \ge\ \limsup_{t\to\infty}\ \frac{1}{t}\log J(t,\theta)
\]
for almost every \(\theta\), and CSS sum piecewise entropy lower bounds
(\(h_i=3\) per hyperbolic piece) against this global growth rate. Near-equality
of the chain at \(O(\delta)\) therefore constrains the *geodesic-wise* growth:
for a set of directions \(\theta\) of Liouville measure \(\ge1-\sqrt\delta\) one
must have
\[
\limsup_{t\to\infty}\tfrac1t\log J(t,\theta)\ \ge\ 3-O(\sqrt\delta).
\]
A geodesic spends its collar crossings in a region whose slice geometry is
controlled by (G$'$)/(R$'$). **Target Lemma J:** for a unit-speed geodesic
crossing a collar whose slices stay in the calibrated band
(\(|H-\sqrt{9-6\delta}\,|\le\varepsilon\), \(\Psi\le\varepsilon^2\)) for time
\(T\), the transverse Jacobi growth along the crossing satisfies
\(\log J_{\text{collar}}\le(3-\kappa(\varepsilon,\delta))T\) with
\(\kappa>0\) explicit. If Lemma J holds, near-equality forces every collar to
leave the calibrated band on a positive Liouville-measure set of crossings —
delivering a slice with \(D\ge c\) and proving Conjecture F. The flat-slice
barrier is what makes the calibrated band dynamically coherent (contracting
side cannot exit toward \(H=0\)), so the barrier enters precisely here.

### 2.5 Analytic route 2 — Ricci-flow probe

Run normalized Ricci flow \(\partial_tg=-2(\operatorname{Ric}+3g)\) from a tight
metric (\(\|\operatorname{Ric}+3g\|_\infty\le\delta\)). Scalar maximum principle:
\(\partial_t s\ge\Delta s+\tfrac23(s+12)(s+3)\), so \(\min s\to-12\)
exponentially; if the flow is immortal and noncollapsing at the scalar level,
\(g(t)\) approaches Ricci soliton geometry. On the other hand
\(\partial_t\operatorname{Vol}=-\int(s+12)\to0\), so
\(\operatorname{Vol}(g(t))\to V_\infty\ge P-O(\delta)\) — the volume approaches
the CSS lower bound. **If** a (weak) convergence theory in this regime forces
the limit's collars to be calibrated, the slice lemma obstructs the limit
unless some collar develops \(O(1)\) defect along the flow — again Conjecture F,
now witnessed by the flow. This route trades the Jacobian analysis for a
compactness/rigidity theory for collapsing Ricci limits — adjacent to open
stability questions, hence *second* priority, per the Strategist.

### 2.6 Computational route 3 — soliton-obstruction audit (cheap, first)

Before either analytic route, audit the smooth calibration space. The
calibrated band (\(H^2=9\), \(\Psi=0\), \(e=0\)) is exactly the cusp condition;
the question is which *global* smooth geometries can sit in the band along an
entire collar. Expanding (G$'$)/(R$'$) with the full Ricci system in the
double-warped class gives a finite-dimensional ODE reduction; its smooth
global solutions on \(T^3\times[a,b]\) with boundary profiles matching
hyperbolic-cusp data can be enumerated numerically (collocation on
\((a_1(r),a_2(r),a_3(r))\) with pointwise pinching penalized). **Output:**
either a smooth calibrated collar family (which would *refute* Conjecture F in
the model class and redirect the gap search to the twist/twisted-collar
sector), or a quantified failure curve \(\delta_{\min}(\text{profile})\)
supporting the conjecture and calibrating the constants \(c,\delta_0\) for the
analytic attack. This is the concrete, checkable intermediate the Strategist
asked for: it decides where the \(O(1)\) defect must live *before* investing in
entropy stability.

### 2.7 Scope discipline

- Conjecture F is a statement in the doubly-warped collar class plus one
  entropy/Jacobian lemma short of a theorem; it is recorded as a conjecture
  with a model-class proof, not as a result.
- Full quantitative CSS stability (a deficit exponent \(\alpha\) for
  \(h\operatorname{Vol}^{1/4}-3P^{1/4}\ge cD^\alpha\)) is adjacent to open
  entropy-rigidity stability questions and is **not** the first target.
- \(\mu_5\) and the \(n\ge6\) KK construction remain monitored, not attacked.
- None of this touches the IL restricted module (A01) or the positive branch
  (A02); the two cheap corollaries in §1.2(c,d) are independent of both.

---

## 3. What this step established

1. \(\mu_4\ge3(\sqrt3-1)/2\approx1.098\), by the session's Step 2 Chern–Weil estimate; this is a lower bound, not an exact determination (script Part A checks the threshold identity).
2. The corrected cascade: obstruction mechanisms at slice dimensions 2
   (Gauss–Bonnet), 3 (Preissmann), 4 (Gauss–Bonnet); open from dimension 5.
3. Cheap absolute gap: no tight metric of either sign on any closed 4-manifold
   with \(2\chi\le3|\tau|\); threshold \(\delta_0=(\sqrt3-1)/2\), no
   compactness or gauge theory needed.
4. **Withdrawn in Step 67:** the stated noncollapsed Ricci-flat coercivity on \(T^4\) is false.
5. A computed counterexample to the "pointwise force needs a positive Hessian"
   intuition: an explicit smooth \(S^1\)-invariant metric on \(T^3\) with
   \(R<0\) everywhere (max \(R\approx-1.67\times10^{-2}\); the defect factor
   \(\Delta\Phi+|\nabla\varphi|^2\) stays \(\ge0.30\) while the conformal
   weight \(e^{-2u}\) concentrates on small disks) — the pointwise scalar
   constraint is satisfiable, so the neck obstruction must come from the
   integrated/trace-level equations and Preissmann, exactly as the program
   assumes (script Part B).
6. Warped-collar identities (G), (R) verified to machine precision (Part C).
7. Conjecture F was formulated, but its claimed curved-slice/model-class proof is withdrawn in Step 67; the full coupled Gaussian collar remains open.
