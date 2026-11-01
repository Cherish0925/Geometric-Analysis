# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "reviewer",
  "task_index": 1,
  "type": "Reviewer",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step47_ttcs01_sub3_reviewer.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step47_ttcs01_sub4_reviewer.md"
    }
  ]
}
```

## Exact Task

Read the consolidated O11/two-scale note as a critical geometric analyst. Check the exact algebra of the formal common-mode evaluation against Theorem K, the dependency ordering and quantifiers of the closed identity/Kähler tariff/full-sign field theorems/A_C/K/A01 rotated cells, and whether the governing k^2/A conjecture is scientifically supported without being presented as proved. Integrate the newly supplied source map: explain whether the De Giorgi same-test identity, Coulomb infimum-preserving bridge, exact-two-form inverse, or curvature-action decomposition materially changes the proposed next route. Return concrete mathematical repairs and identify the single highest-value next proof object; do not offer publication advice.

## Integrated Scientific Memo

# Critical review of the consolidated O11/two-scale note

## 1. Formal common mode versus Theorem K

The algebra in Step 47 §3 is correct. With
\[
h=\frac{k}{A},\qquad r=2-h,\qquad
\beta(r)=\frac{16}{r}-5-\frac{12}{r^2},
\]
one obtains
\[
\beta(2-h)=\frac{h(4-5h)}{(2-h)^2},
\qquad
h-\beta(2-h)=\frac{h^2(1+h)}{(2-h)^2}.
\]
Therefore
\[
P_{\rm form}
=8\pi^2A\frac{h^2(1+h)}{(2-h)^2}
=2\pi^2\frac{k^2}{A}\bigl(1+2h+O(h^2)\bigr),
\]
and
\[
c(h):=\frac{P_{\rm form}}{8\pi^2k}
=\frac{h(1+h)}{(2-h)^2},\qquad
1-c(h)=\frac{4-5h}{(2-h)^2}.
\]

For
\[
\operatorname{spec}(W^+)
=\left(-\frac23+h,\frac13-\frac h2,\frac13-\frac h2\right),
\]
the nearest scalar-\(-4\) Kähler-orbit tensor is the aligned one for \(0<h<1/3\), so
\[
\operatorname{dist}(W^+,\mathcal K)
=\sqrt{h^2+2(h/2)^2}
=\sqrt{\frac32}\,h.
\]
Using \(r^2V=8\pi^2A\),
\[
D_{\mathcal K}
:=\int\operatorname{dist}(W^+,\mathcal K)
=\frac{4\sqrt6\,\pi^2k}{(2-h)^2}.
\]
Theorem K demands
\[
D_{\min}
=\sqrt6\,\pi^2(1-c(h))k
=\frac{\sqrt6\,\pi^2(4-5h)k}{(2-h)^2},
\]
hence
\[
\frac{D_{\mathcal K}}{D_{\min}}
=\frac4{4-5h}
=1+\frac54h+O(h^2),
\]
and at \(h=1/3\) the ratio is \(12/7\). Equivalently,
\[
\frac{8\pi^2k-P_{\rm form}}
{(4\sqrt6/3)D_{\mathcal K}}
=1-\frac54h.
\]
Thus the formal mode verifies the first-order sharpness and scaling of K.

Two qualifications must be inserted directly into §3:

1. This is a **formal algebraic consistency test**, not an evaluation on an admissible closed metric. Lemma T excludes the exact mode because it combines a nowhere-zero self-dual harmonic form with zero exceptional periods.
2. Near-saturation of a linear \(L^1\) inequality does not prove a quadratic \(P\)-law. A separate coercive passage from Weyl departure or field rotation to \(P\) is still missing.

A useful additional identity is
\[
\beta(2-h)=2\theta-3\theta^2,\qquad
\theta=\frac{h}{2-h},
\]
so the mode is exactly the formal \(\alpha=0,\eta=1\) equality family of AK\(\Gamma\). It meets LeBrun’s \(\theta=1/3\) minimum at \(h=1/2\), outside the open range \(h<1/3\).

---

## 2. Correct dependency order and quantifiers

### 2.1 Same-metric closed identity

For every oriented metric on
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},
\]
with the chosen orientation and \(A=K_X^2\),
\[
C_+(g)
=\frac1{2\pi^2}\int|W^+|^2
+\frac1{96\pi^2}\int s^2
=A-k+\frac{P(g)}{8\pi^2}.
\]
This is metric-universal and precedes all Yamabe, Kähler, and monopole assumptions. It cannot be combined with separate infima of the two terms defining \(C_+\).

### 2.2 Kähler tariff

This is a category theorem, logically independent of the full-sign-field route. It requires a fixed blow-up complex structure, its canonical decomposition
\[
K_M=K_0+\sum_iE_i,
\]
a Kähler class \(\Omega\), the relevant positive-cone/Hodge-index relation for \(K_0\), and
\[
e_i=\Omega\cdot E_i>0.
\]
Then
\[
C_+
=\frac{(K_M\cdot\Omega)^2}{\Omega^2}
+\frac1{32\pi^2}\int(s-\bar s)^2>A
\]
for \(k>0\), hence
\[
P>8\pi^2k.
\]
The consolidation should say “strict for every Kähler metric when \(k>0\),” while separately noting that equality of the Kähler **infimum** with \(8\pi^2k\) needs a Kähler recovery family. Simple type alone is not a hypothesis sufficient for this argument.

### 2.3 Full-sign identities

Theorems N/W/E and the amplitude identity require:

- a scalar-\(-4\) Yamabe representative \(\hat g\);
- for every sign class
  \[
  a_\epsilon=c+\sum_i\epsilon_iE_i,
  \]
  an irreducible unperturbed solution on the same metric;
- for \(b^+\ge2\), the stated chamber-independent invariant and limiting argument;
- \(A-k>0\) to exclude reducibles;
- for \(b^+=1\), the retained chamber condition;
- simple type for the \(8\pi^2k\) benchmark.

“Simultaneous solutions” means one solution is selected separately for each Spin\(^c\) structure on the same metric; it does not mean there is a coupled moduli problem.

The amplitude consequence is
\[
P(\hat g)\ge8\pi^2k-4L,\qquad
L=\mathbb E_\epsilon\int(2-\rho_\epsilon)_+.
\]
Since \(P(g)\ge P(\hat g)\), the hypothesis \(P(g)\le8\pi^2ck\) gives
\[
L\ge2\pi^2(1-c)k.
\]

### 2.4 Separate the two rotation energies

The consolidation currently conflates weighted and unweighted quantities. Define
\[
R_\rho
:=\mathbb E_\epsilon\int
\rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2,
\qquad
R_0
:=\mathbb E_\epsilon\int
|\nabla n_\epsilon|_{\mathcal W_2}^2.
\]
Theorem N gives
\[
8\pi^2k-P(\hat g)\le\frac12R_\rho,
\]
so
\[
P(g)\le8\pi^2ck
\quad\Longrightarrow\quad
R_\rho\ge16\pi^2(1-c)k.
\]
Using \(0\le\rho\le2\),
\[
R_\rho\le4R_0,\qquad
P(\hat g)\ge8\pi^2k-2R_0.
\]
The optimization
\[
P\ge \frac{R^2}{\Lambda A}
\quad\Longrightarrow\quad
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
\]
as written in Step 43 uses \(R=R_0\). If a transport theorem is instead formulated for \(R_\rho\), its constants and the optimization must be rewritten rather than silently identifying the two energies.

In Proposition 43.C, the exact weighted left side is advantageous:
\[
\frac12\int a|\nabla n|^2
=\frac18\int\rho^2|\nabla n|^2
\]
for the almost-Kähler \(W_2\) jet. A future zero-set-safe formulation should use the smooth bilinear \(W_0\), not division by \(\rho\) to define \(n\).

### 2.5 Theorem K

Theorem K should occur immediately after the full-sign identities, before \(A_C\):
\[
8\pi^2k-P(g)
\le8\pi^2k-P(\hat g)
\le\frac{4\sqrt6}{3}
\int\operatorname{dist}(W^+_{\hat g},\mathcal K).
\]
It is independent of canonical-branch selection, but “field-selection-free” means only that the final inequality does not depend on which solutions were chosen after the full sign-family existence hypothesis has supplied them.

### 2.6 Theorem \(A_C\)

The proved theorem is specifically for compact complex-hyperbolic ball quotients globally and uniformly locally \(C^{2,\alpha}\)-close, after one scale and diffeomorphism, to the model metric. It controls only the unique nearby canonical monopole branch:
\[
R_{\rm can}\le CP.
\]
It does **not** yet prove a statement on a CH bulk region inside a blow-up. Such a localization requires outer-layer/collar terms, and applying the monopole conclusion additionally requires branch selection.

Accordingly, these formulations are too strong and should be weakened:

- “perturbative KE regime” \(\rightarrow\) “global perturbative ball-quotient regime”;
- “closes diffuse canonical-branch rotation throughout a CH bulk” \(\rightarrow\) “excludes it on globally close closed quotients; its localized blow-up analogue is open”;
- “a small-per-class construction must leave the KE neighbourhood on extensive sets” is not yet proved.

The Riemannian part of \(A_C\)—Yamabe normalization, DeTurck gauge and Einstein-operator coercivity—is broader in usefulness than the branch statement and is the natural basis for localization.

### 2.7 Rotated A01 cells

The upper objects need to be separated:

1. The diagonal zero-period cell has the certified interval
   \[
   \frac{P}{8\pi^2}\in
   [0.995662732753254329\ldots,\,
    0.995662732771114200\ldots].
   \]
2. The rotated family is a continuity construction:
   \[
   J(g_\psi)=J(g_*)+O(\psi^2)<1
   \]
   for sufficiently small nonzero \(\psi\), with nonzero exceptional period. Its displayed derivative \(t'(0)=0.6960\) is floating-point, though positivity has a robust pointwise sign argument. No interval-certified admissible \(\psi\)-range or rotated cost is supplied.

Thus “certified and rotated upper objects” should not suggest that the rotated family itself has the same interval certificate. It does nevertheless prove the essential geometric fact: subthreshold metrics can be conformal to smooth almost-Kähler metrics with small nonzero exceptional periods.

Finally, “measure scalar variance on the Yamabe representative” is erroneous: its scalar curvature is constant. The meaningful measurements are
\[
P(g)-P(\hat g)=\frac{S(g)-S(\hat g)}{12},
\]
the variance on the conformal almost-Kähler representative, and the degeneration of its conformal factor.

---

## 3. Status of the \(k^2/A\) conjecture

The supplied results support \(k^2/A\) as a serious **diffuse-transport candidate scale**, but not as a proved or matched asymptotic law.

### Positive evidence

- The formal common mode gives
  \[
  P_{\rm form}\sim2\pi^2\frac{k^2}{A}.
  \]
- It asymptotically saturates Theorem K.
- Proposition 43.C identifies the Cotton pairing through which extensive rotation could incur a quadratic Cauchy–Schwarz cost.
- \(A_C\) excludes one global perturbative canonical-branch realization.
- Rotated cells rule out restoration of an \(O(k)\) tariff merely from symplectic or conformally almost-Kähler structure.

### Missing facts

- No nonperturbative theorem proves
  \[
  P\gtrsim \frac{k^2}{A}.
  \]
- No closed upper family realizes
  \[
  P\lesssim \frac{k^2}{A}.
  \]
- The known cell construction gives an \(O(k)\) upper bound with coefficient below \(1\) in units \(8\pi^2\), not a coefficient tending to zero with \(k/A\).
- The exact formal mode is topologically inadmissible.
- The Cotton estimate still contains uncontrolled second jets, \(E=W^+-W_0\), amplitude/Lee terms, zero-set cutoffs and boundary terms.

Therefore “governing two-scale conjecture” should be replaced by something like:

> **Diffuse quadratic-transport conjecture.** In a specified family of pure blow-ups—e.g. an indicated cover family, with constants uniform in cover degree and \(k/A\)—the diffuse channel may obey a lower bound of order \(k^2/A\). Whether this is the unrestricted sharp scale depends on nonperturbative cores/collars and on a matching upper construction.

The constant \(c_0\) must be uniform over a stated family. For a single fixed manifold, writing \(P\ge c_0k^2/A\) with an unrestricted manifold-dependent \(c_0\) largely repackages positivity.

### The neglected anti-self-dual ledger

A particularly important repair is to record the complementary exact Chern–Weil budget. Combining the closed identity with signature gives
\[
W_-(g)+\frac{S(g)-32\pi^2A}{48}
=
10\pi^2k+\frac{8\pi^2}{3}\bigl(\chi(X)-3\tau(X)\bigr)
+\frac{P(g)}4.
\]
Relative to an appropriate KE reference,
\[
\Delta W_-=10\pi^2k+\frac P4-\frac{\delta V}{3}
\]
in scalar-\(-4\) normalization.

This does not by itself disprove the quadratic conjecture, but it shows that a putative common mode must also locate an order-\(k\) anti-self-dual Weyl budget. For complex-hyperbolic hosts, where the KE background has \(W^-=0\), this is a potentially stronger obstruction to a diffuse near-CH realization than Theorem K. Any claim that the formal mode explains the unrestricted ball-quotient asymptotics is premature until this budget is priced. At minimum, §4 should add measurements of

\[
\int|W^-|^2,\qquad
\int|\nabla\operatorname{Ric}^{\circ}|^2,
\]
and the location of the \(W^-\) energy relative to cores and collars.

The source material does not establish the proposed localized \(W^-\)-coercivity theorem, so a linear law for ball-quotient hosts is not yet a result. It is, however, a decisive reason to formulate the quadratic conjecture by geometric regime rather than universally.

---

## 4. Effect of the newly supplied source map

### 4.1 De Giorgi same-test identity: changes the desired proof architecture

The identity
\[
Q(F)=\sum_jQ(\xi_j)
-\int\min_b\sum_j|\nabla\xi_j-\xi_jb|^2
\]
shows how one common test retains a switching/rotation square that is lost by estimating branches separately. This is directly relevant to the present circularity: \(E\), depletion, amplitude gradients and rotation are currently put on different sides of inequalities and can pay for one another.

It does not supply an SW theorem. The naive variation gives
\[
Q^{\rm SW}(0,\eta\Phi)
=\int\left(|\Phi|^2|d\eta|^2+
4\eta^2|q(\Phi)|^2\right),
\]
with no negative geometric-defect term. Moreover, distinct sign structures have different determinant lines, so a literal pointwise Euclidean combination across signs is unavailable without a bundle-correct construction.

Its material consequence is therefore precise: the next field estimate should seek a **single coupled connection–spinor test** retaining rotation/depletion and alignment errors in one quadratic identity, rather than separately bounding \(E\) and \(\nabla a\) by the depletion budget.

### 4.2 Coulomb infimum-preserving bridge: clarifies the global passage, not the local estimate

The transferable chain is
\[
\text{infimum-preserving approximation}
\to
\text{entry for minimizing objects}
\to
\text{global comparison identity}
\to
\text{all-competitor bound}.
\]
This materially warns against inferring the unrestricted closed infimum from exact-collar cells. No O11 entry theorem currently forces arbitrary near-minimizers into the cell class, and no convex square decomposition analogous to the fixed-background Poisson problem is known for \(P(g)\).

Thus it strengthens the need for either a direct closed-manifold coercive inequality or a genuine bulk/core entry theorem. It supplies neither by itself.

### 4.3 Exact-two-form inverse: useful auxiliary bridge, not the missing coercivity

For exact two-forms,
\[
\|h\|_2^2=2\|h^+\|_2^2,\qquad
h=2dd^*G\varphi,
\]
avoids requiring a uniform one-form spectral gap when reconstructing an exact correction from its self-dual part. This can help with period-preserving gluing corrections and perhaps the A01 host-period compatibility problem.

It does not control the central objects directly:

- relative sign-flip curvature represents \(\pm E_i\), so it is not globally exact before subtracting a harmonic representative;
- the fixed anti-self-dual topological charge remains after that subtraction;
- \(E=W^+-W_0\) is a Weyl endomorphism, not a closed two-form;
- no higher-derivative, positivity or coupled Dirac estimate follows.

Hence it does not change the main quadratic route.

### 4.4 Curvature-action decomposition: materially sharpens the Riemannian route

The useful principle is to impose Bianchi and representation constraints before estimating the curvature action. It reinforces, rather than removes, the Cotton obstruction: away from Einstein metrics,
\[
\delta W^+=C^+\sim\nabla\operatorname{Ric}^{\circ},
\]
and \(P\) alone does not control this derivative. The cited Einstein cancellation also does not generally eliminate \(W^-\); its final positivity still uses additional curvature assumptions.

Its strongest contribution here is strategic and concrete:

- retain the Cotton source inside the integrated identity rather than estimate it prematurely;
- analyze the linearized curvature blocks in Bianchi gauge;
- include the anti-self-dual budget;
- separate low-frequency Einstein deformations from high-frequency curvature production.

This makes a localized, purely Riemannian CH-bulk coercivity theorem more immediately tractable than the full nonperturbative SW transport estimate.

---

## 5. Highest-value next proof object

The single highest-value next object is a **localized complex-hyperbolic Einstein coercivity theorem with explicit collar flux**, formulated without monopole branch selection.

A suitable target is:

> Let \(\Omega\Subset\Omega_1\) with a controlled unit-thickness collar, and suppose the scalar-\(-4\) Yamabe metric \(\hat g\), after a local diffeomorphism, is \(C^{2,\alpha}\)-close on \(\Omega_1\) to a complex-hyperbolic metric \(g_{\rm CH}\). In local DeTurck/Bianchi gauge, prove
> \[
> \int_\Omega\left(
> |W^-_{\hat g}|^2+
> |W^+_{\hat g}-W^+_{\rm CH}|^2
> \right)
> +|\mathrm{RV}_\Omega|
> \le
> C\left[
> \int_{\Omega_1}|\operatorname{Ric}^{\circ}_{\hat g}|^2
> +\mathcal B(\Omega_1\setminus\Omega)
> \right],
> \]
> where \(C\) is model-uniform and \(\mathcal B\) is an explicit gauge-invariant collar/outer-layer term that can be summed or absorbed in a bulk/core decomposition.

The exact treatment of signed relative volume may require replacing \(|\mathrm{RV}_\Omega|\) by the coercive quadratic scalar-normalized volume defect plus an explicitly retained boundary flux; it should not be asserted positive before derivation.

This theorem has the highest leverage because it:

1. localizes the already-proved Riemannian core of \(A_C\);
2. removes canonical-branch selection from the immediate obstruction;
3. prices the missing \(W^-\) ledger on ball-quotient hosts;
4. forces the certified and rotated cells’ order-\(k\) curvature budget into cores/collars, exactly where their construction places it;
5. distinguishes whether the formal \(k^2/A\) mode can occur in a near-CH bulk or requires nonperturbative microstructure;
6. supplies the entry mechanism needed before any cell lower bound can govern the unrestricted closed infimum.

After this object, the problem separates cleanly: CH bulk becomes coercive, while the remaining unresolved scientific object is the nonperturbative core/collar channel—equivalently, positivity and sharp value of the relevant exact-CH cell infimum. The broader actual-field inequality
\[
(8\pi^2k-P)_+\lesssim\sqrt{AP}
\]
would be more global, but presently requires a new SW same-test identity plus zero-set, amplitude, Lee and alignment control. The localized Riemannian theorem is both closer to the established \(A_C\) machinery and capable of changing the judgment on the proposed quadratic scale.