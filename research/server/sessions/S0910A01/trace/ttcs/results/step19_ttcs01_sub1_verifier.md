# TTCS Independent Branch Record

```json
{
  "step_id": 19,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A01/workspace/scripts/step19_whitney_energy_transfer.py",
    "Sessions/S0910A01/workspace/scripts/step19_tensor_whitney_absorption.py",
    "Sessions/S0910A01/workspace/notes/step18_weighted_cutoff_system.md",
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md"
  ]
}
```

## Task

Verify the mathematical correctness of the Whitney-ball reduction for the degenerate cutoff-flow curvature estimate. The construction claims: (1) On Whitney balls B_{crχ₀}(y) in the support of a cutoff flow ∂_tg = -2χ²(Ric+g), Bishop-Gromov comparison transfers total support energy ∫_Ω|Rm|² ≤ CK₀Vol(Ω) to Whitney-ball Li smallness ℓ⁴ fint|Rm|² ≤ CK₀r⁴ with the χ₀ canceling. (2) The Sobolev product A_ℓ||Rm||₂ ≤ C√K₀ r² is independent of χ₀ and collapsed volume. (3) On each Whitney ball, a≈a₀=χ₀², so the operator is non-degenerate; time θr² provides smoothing at ALL Whitney levels simultaneously because the diffusion-to-ball ratio √θ/c is χ₀-independent. (4) The Moser iteration gives |aRm|≤C/t with C independent of χ₀. (5) For U=aE and p>2, ||U||_∞ ≤ Ca₀^{1-2/p}t^{-2/p}||E(0)||_p, so the weighted defect improves as a₀→0. Check: (a) Is the BG comparison in Section 3 correct — does ℓ⁴/Vol(B_ℓ) exactly cancel the χ₀⁴ in ℓ⁴? (b) Does the Sobolev product really cancel the cutoff level algebraically? (c) Is the time matching correct — does physical time θr² suffice for all Whitney levels? (d) Are there hidden obstacles: does the cutoff perturbation (a-a₀)E on the Whitney ball remain absorbable through the Moser iteration? (e) Does the finite-overlap Whitney cover create cumulative constants that could depend on χ₀? (f) Is the claim that ∇²a can be fully removed by integration by parts in the tensor energy correct?

## Output

# Scientific memo: Whitney-ball reduction

## Overall assessment

The scale cancellations in items (1)–(3) are mathematically sound after two corrections:

1. the curvature-energy hypothesis must be local to each base support ball, rather than only an average over an arbitrary union of support balls;
2. the Bishop–Gromov cancellation is uniform in \(\chi _0\), not an exact algebraic identity at finite radius.

The passage from these scale facts to item (4) is not supplied by the note. In particular, the estimate \(a-a_0=O(c^2a_0)\) is incorrect, the curvature equation contains coupled \(E\)-sources after integration by parts, and direct absorption through every Moser exponent has \(p\)-dependent constants. Item (5) is correct for the constant-coefficient heat model, but its tensor-flow analogue still depends on a weighted curvature-potential estimate.

---

## (a) Bishop–Gromov transfer

Let

\[
W=B_{g_0}(y,\ell),\qquad \ell=cr\chi _0,\qquad \chi _0=\chi(y),
\]

and suppose \(W\subset \Omega_j=B_{5r}(p_j)\), with

\[
\int_{\Omega_j}|\mathrm{Rm}(g(t))|^2\,d\mu_t
   \le C_1\bar K_0\,\mathrm{Vol}_{g_0}(\Omega_j).
\]

Here \(\bar K_0\) denotes an unnormalized mean-curvature bound, with units
\(\mathrm{length}^{-4}\). Metric comparability gives

\[
\ell^4\fint_W^{g(t)}|\mathrm{Rm}|^2
 \le C(\zeta,n)C_1\bar K_0\,
 \ell^4\frac{\mathrm{Vol}_{g_0}(\Omega_j)}
                {\mathrm{Vol}_{g_0}(W)}.
\]

Since \(y\in B_{5r}(p_j)\),

\[
\Omega_j\subset B_{g_0}(y,10r).
\]

Under \(\operatorname{Ric}_{g_0}\ge-3g_0\), Bishop–Gromov gives

\[
\frac{\mathrm{Vol}_{g_0}(B_{10r}(y))}
     {\mathrm{Vol}_{g_0}(B_\ell(y))}
\le \frac{V_{-1}(10r)}{V_{-1}(\ell)}.
\]

Consequently,

\[
\ell^4\fint_W|\mathrm{Rm}|^2
 \le C\bar K_0\,\ell^4\frac{V_{-1}(10r)}{V_{-1}(\ell)}.
\]

In dimension four,

\[
V_{-1}(s)=2\pi^2\int_0^s\sinh^3u\,du.
\]

Since \(\sinh u\ge u\),

\[
V_{-1}(\ell)\ge \frac{\pi^2}{2}\ell^4,
\]

while \(V_{-1}(10r)\le C(r_0)r^4\) for \(r\le r_0\). Hence

\[
\boxed{\ell^4\fint_W|\mathrm{Rm}|^2
       \le C(r_0,\zeta)\bar K_0r^4,}
\]

uniformly for every \(\chi _0>0\).

Thus the \(\chi _0^4\) dependence disappears in the upper bound. It does not cancel exactly against the hyperbolic model volume, because \(V_{-1}(\ell)\) is not exactly proportional to \(\ell^4\). The script `step19_whitney_energy_transfer.py` correctly illustrates the small-radius asymptotics.

### Locality issue

If

\[
\Omega=\bigcup_{j=1}^N\Omega_j
\]

and only

\[
\int_\Omega|\mathrm{Rm}|^2\le \bar K_0\mathrm{Vol}(\Omega)
\]

is known, the same conclusion need not hold uniformly on one component. The integral may concentrate in a single \(\Omega_j\), producing a factor comparable to
\(\mathrm{Vol}(\Omega)/\mathrm{Vol}(\Omega_j)\). The argument is uniform when each base support ball, or a bounded enlargement of it, has its own energy estimate.

There is also a notation mismatch between Sections 3 and 11. If the hypothesis is

\[
r^4\fint_{B_{6r}}|\mathrm{Rm}|^2\le K_0,
\]

then the transferred quantity is \(CK_0\), not \(CK_0r^4\). The latter form follows when \(\fint|\mathrm{Rm}|^2\le\bar K_0\). These two versions should use different symbols.

---

## (b) Sobolev product

Use the squared relative Sobolev inequality in dimension four,

\[
\|\varphi\|_{L^4(W)}^2
 \le S_\ell\int_W
       \bigl(|\nabla\varphi|^2+\ell^{-2}\varphi^2\bigr),
\qquad
S_\ell\le C\frac{\ell^2}{\mathrm{Vol}(W)^{1/2}}.
\]

Then

\[
\begin{aligned}
S_\ell\|\mathrm{Rm}\|_{L^2(W)}
&\le
C\frac{\ell^2}{\mathrm{Vol}(W)^{1/2}}
   \bigl(\bar K_0\mathrm{Vol}(\Omega_j)\bigr)^{1/2}\\
&\le
C\sqrt{\bar K_0}\,\ell^2
 \left(\frac{V_{-1}(10r)}{V_{-1}(\ell)}\right)^{1/2}\\
&\le C\sqrt{\bar K_0}\,r^2.
\end{aligned}
\]

Therefore both the cutoff level and the absolute ball volume disappear:

\[
\boxed{S_\ell\|\mathrm{Rm}\|_2
       \le C\sqrt{\bar K_0}\,r^2.}
\]

This is the correct quantity in

\[
\int a|\mathrm{Rm}|^3
 =\int |\mathrm{Rm}|\,|\chi\eta\mathrm{Rm}|^2
 \le \|\mathrm{Rm}\|_2
       \|\chi\eta\mathrm{Rm}\|_4^2.
\]

There is a notation inconsistency in the supplied files. If \(A_\ell\) denotes the norm-form coefficient

\[
\|\varphi\|_4
 \le A_\ell\bigl(\|\nabla\varphi\|_2+
                  \ell^{-1}\|\varphi\|_2\bigr),
\]

then

\[
A_\ell\asymp \frac{\ell}{\mathrm{Vol}(W)^{1/4}},
\qquad S_\ell=A_\ell^2,
\]

and the reaction coefficient is \(A_\ell^2\|\mathrm{Rm}\|_2\), not
\(A_\ell\|\mathrm{Rm}\|_2\).

The numerical value \(0.111\) in the scripts omits the relative Sobolev constant, the energy-persistence constant, metric-comparison factors, and tensor coefficients. It verifies scaling but does not determine absorption.

---

## (c) Uniform physical time

On \(W=B_\ell(y)\),

\[
|\chi-\chi _0|\le \frac{L}{r}\ell=Lc\chi _0.
\]

Thus, when \(Lc<1\),

\[
(1-Lc)^2a_0\le a\le(1+Lc)^2a_0,
\qquad a_0=\chi _0^2.
\]

The diffusion radius during physical time \(T=\theta r^2\) is

\[
\sqrt{a_0T}
 =\chi _0r\sqrt{\theta}.
\]

Since \(\ell=cr\chi _0\),

\[
\frac{\sqrt{a_0T}}{\ell}=\frac{\sqrt{\theta}}{c}.
\]

Hence a cylinder of diffusion radius at most \(\ell/2\) fits whenever

\[
\theta\le \frac{c^2}{4},
\]

independently of \(\chi _0\). Equivalently, the time to diffuse across the entire Whitney ball is

\[
\frac{\ell^2}{a_0}=c^2r^2,
\]

also independent of \(\chi _0\).

This time matching is correct. When \(\theta<c^2\), the flow does not traverse the whole Whitney ball, but interior parabolic estimates only require the smaller cylinder of radius \(\sqrt{a_0t}\).

For enlarged balls used in nested cutoffs, one needs \(qLc<1\), where \(q\) is the enlargement factor.

---

## (d) Variable cutoff coefficient and Moser iteration

The relative variation is

\[
\frac{|a-a_0|}{a_0}
 \le Lc(2+Lc),
\]

which is \(O(Lc)\), not \(O(c^2)\). For \(L=2\) and \(c=0.1\), this upper bound is \(0.44\), exactly consistent with the interval \([0.64,1.44]\) displayed in the note.

The appropriate formulation is therefore a variable-coefficient uniformly parabolic equation on each Whitney ball, rather than a constant-coefficient flow plus a harmless forcing term. Differentiating

\[
(a-a_0)E
\]

twice in the curvature evolution produces a principal coefficient change, first derivatives of \(a\), and Hessian terms. Small amplitude alone does not make this a lower-order perturbation.

After rescaling space by \(\ell\) and time by \(\ell^2/a_0=c^2r^2\),

\[
\frac{a}{a_0}\asymp1,\qquad
\frac{\ell|\nabla a|}{a_0}=O(cL),\qquad
\frac{\ell^2}{a_0}\frac{|\nabla a|^2}{a}=O(c^2L^2).
\]

These are uniform in \(\chi _0\), so the coefficient degeneracy itself has been removed locally.

Two further analytical points remain in the supplied derivation:

1. Direct high-exponent absorption is not uniform in \(p\). For the model inequality
   \[
   K_t\le a\Delta K+CaK^2,
   \]
   testing by \(K^{p-1}\) gives a reaction coefficient proportional to \(p\):
   \[
   \frac{d}{dt}\int K^p
   +c_p\int a|\nabla K^{p/2}|^2
   \le Cp\int aK^{p+1}+\cdots.
   \]
   Absorption by the critical \(L^2\) norm therefore requires smallness depending on \(p\). Passing through \(p=2,4,8,\ldots\) to infinity is not an \(O(\log n)\) finite process. A two-stage curvature-potential argument, or an explicitly adapted Li theorem, is needed.

2. The curvature equation has \(E\)-dependent inhomogeneous terms. The curvature energy is therefore coupled to defect energy; it does not reduce to the curvature-only inequality written in Section 6.

Accordingly, the supplied notes establish uniform Whitney scaling but not yet

\[
|a\,\mathrm{Rm}|\le \frac Ct.
\]

The script `step19_tensor_whitney_absorption.py` performs arithmetic on a schematic inequality; it does not derive the tensor evolution or execute a parabolic iteration.

---

## (e) Whitney overlap

For radii \(\ell_y=cr\chi(y)\), intersecting enlarged balls have comparable radii. Indeed, Lipschitz control gives

\[
|\chi(y_i)-\chi(y_j)|
 \le \frac{L}{r}d(y_i,y_j)
 \le q cL\bigl(\chi(y_i)+\chi(y_j)\bigr),
\]

so \(q cL<1\) yields a uniform ratio between \(\ell_i\) and \(\ell_j\). Local volume doubling from the Ricci lower bound then gives bounded overlap

\[
N=N(n,L,c,q,r_0),
\]

independent of the cutoff level. Countably many levels accumulating toward \(\{\chi=0\}\) do not introduce an additional factor for unnormalized integrals:

\[
\sum_\alpha\int_{W_\alpha}F
 \le N\int_{\{\chi>0\}}F.
\]

However, Section 10 writes

\[
\sum_\alpha R_{W,\alpha}\le N R_{\mathrm{total}}
\]

without fixing whether \(R_{W,\alpha}\) is an integral or
\(\ell_\alpha^4\fint_{W_\alpha}\). The displayed estimate is valid for unnormalized integrals. It does not follow from overlap for normalized quantities, because each term carries the varying weight

\[
\frac{\ell_\alpha^4}{\mathrm{Vol}(W_\alpha)}.
\]

Uniform local estimates are naturally organized through a supremum over Whitney balls or through unnormalized support-summed energies.

The base supports \(\Omega_j\) also need bounded multiplicity or separate local energy budgets. A single average over an arbitrarily large union introduces dependence on its component count or volume distribution.

---

## (f) Hessian of \(a\)

An explicit \(\nabla^2a\) factor can be removed from a localized integral identity by one integration by parts, but this produces defect terms that are absent from Section 6.

For \(H=\mathrm{Rm}\), a representative contribution is

\[
I=\int\eta^2\langle\nabla^2a*E,H\rangle.
\]

Integrating once gives schematically

\[
\begin{aligned}
I={}&-\int\eta^2\nabla a*\nabla E*H
     -\int\eta^2\nabla a*E*\nabla H\\
   &-2\int\eta\nabla\eta*\nabla a*E*H.
\end{aligned}
\]

Using \(\nabla E=\nabla\operatorname{Ric}\), hence
\(|\nabla E|\le C|\nabla H|\), and Young’s inequality,

\[
\begin{aligned}
|I|\le{}&
\varepsilon\int\eta^2a|\nabla H|^2\\
&+C_\varepsilon\int\eta^2\frac{|\nabla a|^2}{a}
          \bigl(|H|^2+|E|^2\bigr)\\
&+C\int a|\nabla\eta|^2|H|^2
 +C\int\eta^2\frac{|\nabla a|^2}{a}|E|^2.
\end{aligned}
\]

Since

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le \frac{4L^2}{r^2},
\]

there is no inverse power of \(\chi\). But there is an \(r^{-2}\int|E|^2\) source, not merely an \(r^{-2}\int|H|^2\) remainder. At exponent \(p>2\), the analogous term is

\[
C\int\frac{|\nabla a|^2}{a}
       |E|^2|H|^{p-2}.
\]

Thus a pointwise Hessian estimate may be avoidable in weak tensor energies, but the resulting curvature estimate is coupled to defect energies and lower powers of curvature. The curvature-only schematic inequality in Section 6 omits this structure.

---

## Weighted defect model

For constant \(a=a_0\) in four dimensions,

\[
U(t)=a_0e^{a_0t\Delta}E(0),
\]

and the Euclidean \(L^p\)-to-\(L^\infty\) estimate gives

\[
\|U(t)\|_\infty
 \le C(a_0t)^{-2/p}\|U(0)\|_p
 =C a_0^{1-2/p}t^{-2/p}\|E(0)\|_p.
\]

This algebra is correct. For \(p>2\), \(1-2/p>0\), and the coefficient decreases as \(a_0\to0\) if the initial \(L^p\) norm is held fixed. On a Whitney ball, that norm also decreases with its volume when \(E(0)\) is pointwise bounded.

For the actual tensor equation, uniform pointwise control additionally requires the curvature potential and the first-derivative cutoff terms. The fixed-\(p\) estimate in the A03 note supplies a spatial \(L^p\) layer, while its passage to

\[
\|aE(t)\|_\infty
 \le C_p\delta(r^2/t)^{2/p}
\]

still uses either \(|a\mathrm{Rm}|\le C/t\) or the stated weighted \(L^3\) curvature-potential bound.

## Bottom line

- **BG transfer:** valid per local base support; uniform rather than exact in \(\chi _0\).
- **Sobolev cancellation:** valid, with the squared Sobolev coefficient.
- **Time matching:** correct and uniform across Whitney levels.
- **Cutoff coefficient:** uniformly parabolic after Whitney rescaling, but its variation is \(O(cL)\), not \(O(c^2)\).
- **Finite overlap:** uniform in \(\chi _0\) for unnormalized integrals; the normalized-energy summation needs reformulation.
- **Hessian terms:** removable from localized weak identities, but they leave coupled \(E\)-energy sources.
- **Pointwise curvature and defect estimates:** compatible with the Whitney scaling, but not derived by the supplied tensor script or schematic Moser argument.