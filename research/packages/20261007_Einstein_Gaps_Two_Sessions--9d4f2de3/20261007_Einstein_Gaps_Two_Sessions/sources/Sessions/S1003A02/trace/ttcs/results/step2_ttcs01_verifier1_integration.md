# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 2,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematics and code behind the O11 blow-up cell computation for four-manifold Einstein gaps. (1) Verify the exact identity P - 8 pi^2 Q = (S - 32 pi^2 A)/12 + 4(W_+ - (4/3) pi^2 A) on X # k CP2bar # l(S^1xS^3) with Hilbert-Schmidt norms on two-forms (conventions file), and the cell identity P(U) = 8pi^2 + 4 Delta W_+ + Delta S/12 for a blown-up ball agreeing with complex hyperbolic metric near the boundary; check signs, orientation (complex orientation, E.E=-1) and that Burns gives exactly 8 pi^2. (2) Check the U(2) cohomogeneity-one curvature code: frame brackets, Koszul formula, curvature-operator sign, the identification of the complex orientation (the script's 'SD' block is anti-complex since FS gives W+=0 there), bolt regularity F'(x0)G'(x0)=1 for O(-1), smoothness/H^2 matching at X, and the Kahler exact optimum P/8pi^2 = 1 + 6x0 + 9x0^2(1+X^-2). (3) Check the claim that the linear coefficient 6x0 equals the Hodge-index Kahler bound (c1.omega)^2/omega^2 with epsilon = 3 x0 in Ric=-6g units. (4) Judge whether the numerical evidence (table in the note) really supports 'every U(2) cell has P > 8pi^2 and the slope tends to 6 also for non-Kahler cells', and identify any parametrization blind spot (e.g. phi=(1-u)^3 freezing near X, monotone b=sqrt(x), fixed outer CH region, degree 12) that could hide a cell with P < 8pi^2. (5) Assess the heuristic that the order-x0 coefficient is universal beyond U(2) because Burns is critical; state precisely what would have to be proved and whether log terms could enter. Give a direct scientific memo with any errors found and their consequences.

## Integrated Scientific Memo

# O11 blow-up cell computation: verification memo

## 1. Exact Chern–Weil identities

With Hilbert–Schmidt operator norms on \(\Lambda^2\),
\[
4\pi^2T_+=\frac{S}{24}+2W_+-\frac P2,
\qquad
P=\frac S{12}+4W_+-8\pi^2T_+.
\]

For
\[
M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\qquad A=c_1^2(X),\quad Q=k+4\ell,
\]
one blow-up changes \((\chi,\tau)\) by \((1,-1)\), hence \(T_+=2\chi+3\tau\) by \(-1\); an \(S^1\times S^3\) summand changes \(\chi\) by \(-2\), hence \(T_+\) by \(-4\). Therefore
\[
T_+(M)=A-Q.
\]
For the Kähler–Einstein metric on \(X\),
\[
S_{\rm KE}=32\pi^2A,\qquad W_+^{\rm KE}=S_{\rm KE}/24=\frac43\pi^2A.
\]
Consequently the claimed all-metric identity is exact:
\[
\boxed{
P(g)-8\pi^2Q
=\frac{S(g)-32\pi^2A}{12}
+4\left(W_+(g)-\frac43\pi^2A\right).
}
\]

For a blown-up ball \(U\) replacing a ball \(B\), with identical boundary metric and first-jet data, the boundary transgression terms cancel. In the complex orientation,
\[
\chi(U)-\chi(B)=1,\qquad \tau(U)-\tau(B)=-1,
\]
because the exceptional curve has \(E^2=-1\). Thus
\[
\Delta T_+=2(1)+3(-1)=-1.
\]
Since the complex-hyperbolic ball is Einstein, \(P(B)=0\), and hence
\[
\boxed{
P(U)=8\pi^2+4\Delta W_++\frac{\Delta S}{12}.
}
\]
The sign \(+8\pi^2\) is correct and depends on using the complex orientation and \(E^2=-1\).

For Burns, \(K=x-x_0\), so with \(H=K-x=-x_0\),
\[
L=x^2H''-2H=2x_0.
\]
Therefore
\[
P_{\rm Burns}
=4\pi^2\int_{x_0}^{\infty}\frac{(2x_0)^2}{x^3}\,dx
=8\pi^2.
\]
Thus Burns gives exactly, not asymptotically, \(8\pi^2\).

A related point: for matched boundary data, the relative signature identity gives
\[
W_-(U)=12\pi^2+\Delta W_+.
\]
Hence the observed \(W_-(U)>12\pi^2\) is equivalent to \(\Delta W_+>0\), not independent evidence.

---

## 2. U(2) curvature code

### Frame, connection, and curvature sign

For
\[
E_0=\partial_t,\quad E_1=X_1/b,\quad E_2=X_2/b,\quad E_3=X_3/a,
\]
and \([X_1,X_2]=2X_3\) cyclically, the implemented brackets are correct:
\[
[E_0,E_1]=-\frac{b'}bE_1,\quad
[E_0,E_2]=-\frac{b'}bE_2,\quad
[E_0,E_3]=-\frac{a'}aE_3,
\]
\[
[E_1,E_2]=\frac{2a}{b^2}E_3,\quad
[E_2,E_3]=\frac2aE_1,\quad
[E_3,E_1]=\frac2aE_2.
\]
The Koszul formula
\[
2\langle\nabla_{E_i}E_j,E_k\rangle
=c_{ij}^{k}-c_{jk}^{i}+c_{ki}^{j}
\]
is also implemented correctly.

The stored convention is
\[
R_{ijkl}=\langle R(E_i,E_j)E_k,E_l\rangle,
\qquad
R=\nabla_i\nabla_j-\nabla_j\nabla_i-\nabla_{[i,j]}.
\]
With this index ordering, the minus sign in `Rop` is necessary to make the round unit sphere’s curvature operator \(+\mathrm{Id}_{\Lambda^2}\). The Ricci contraction and subtraction of \(s/12\) on each chiral block are consistent. The squared \(3\times3\) Frobenius norms are the required operator Hilbert–Schmidt norms.

### Orientation error in the first script

There is a genuine documentation/labeling error in `u2_curvature.py`. With
\[
d\sigma_3=-2\sigma_1\wedge\sigma_2
\]
and \(a=bb'\), a Kähler form is, up to sign,
\[
\omega=e^0\wedge e^3-e^1\wedge e^2.
\]
This is anti-self-dual for the script’s orientation
\[
e^0\wedge e^3\wedge e^1\wedge e^2=e^{0123}.
\]
Thus that orientation is anti-complex, and the script’s raw `SD` block is anti-complex. This is exactly why Fubini–Study gives zero Weyl curvature in the raw `Wp` block.

The downstream swap in `u2_xcoord.py`,
```python
'wpsq_c': conv(U.wmsq),
'wmsq_c': conv(U.wpsq)
```
is correct. Accordingly, the numerical cell identity uses complex \(W^+\) correctly. The comments/docstring of `u2_curvature.py` should be corrected; any future direct use of `U.wpsq` as complex \(W^+\) would be wrong.

### \(x\)-coordinate and volume

For
\[
g=\frac{dx^2}{4G}+F\sigma_3^2+x(\sigma_1^2+\sigma_2^2),
\]
the transformations
\[
\frac{dx}{dt}=2\sqrt G,\qquad a=\sqrt F,\qquad b=\sqrt x
\]
and
\[
dV=\pi^2x\sqrt{\frac FG}\,dx
\]
are correct. Since \(bb'=\sqrt G\), the Kähler condition \(a=bb'\) is exactly \(F=G\).

For complex hyperbolic space,
\[
F=G=x+x^2,\qquad \operatorname{Ric}=-6g,\qquad s=-24,
\]
and over \(0\le x\le X\),
\[
S(B_X)=288\pi^2X^2,\qquad
W_+(B_X)=12\pi^2X^2.
\]
Thus the JAX reference value
\[
72\pi^2X^2=S(B_X)/12+4W_+(B_X)
\]
is correct.

### Bolt regularity

Writing
\[
F=f_1(x-x_0)+O((x-x_0)^2),\qquad
G=g_1(x-x_0)+O((x-x_0)^2),
\]
and setting \(x-x_0=g_1r^2+O(r^4)\), the normal metric is
\[
dr^2+f_1g_1r^2\sigma_3^2+O(r^4).
\]
Since the Hopf fiber has period \(2\pi\), smoothness of the \(O(-1)\) bolt requires
\[
\boxed{F'(x_0)G'(x_0)=1.}
\]
The bolt area is
\[
\operatorname{Area}(E)=\pi x_0.
\]
Because the Kähler base profile has \(K'(x_0)=1\), the JAX constraint
\[
p_1(x_0)+p_2(x_0)=0
\]
enforces the product-of-slopes condition exactly.

### Outer matching

The four boundary conditions used in `kahler_cell_exact.py` match \(K\) and \(K'\), hence the metric is \(C^1\) across \(x=X\). In general \(K''\) jumps, so the displayed extremizer does **not** literally agree with complex hyperbolic space on an open collar. It is a piecewise-smooth \(C^{1,1}\) representative, locally \(H^2\), and has finite curvature energy.

It can be smoothed in an arbitrarily thin annulus and made exactly complex hyperbolic near the boundary with energy change tending to zero. Thus it computes the variational infimum in the \(H^2\) closure, but the note should distinguish “matched at the boundary” from “equal on a collar.”

The perturbation factor \(\phi=(1-u)^3\) forces the perturbation and its first two \(x\)-derivatives to vanish at \(X\) relative to this base profile; it does not repair the base profile’s second-derivative jump or create an open exact collar.

---

## 3. Exact Kähler variational calculation

For \(K=x+H\),
\[
P=4\pi^2\int_{x_0}^{X}\frac{L^2}{x^3}\,dx,
\qquad L=x^2H''-2H.
\]
The Euler–Lagrange equation is
\[
(x^{-1}L)''-2x^{-3}L=0,
\]
so
\[
L=c_1x^3+c_2,
\qquad
H=\frac{c_1}{4}x^3-\frac{c_2}{2}+\alpha x^2+\frac{\beta}{x}.
\]
The four endpoint conditions in the script uniquely determine the coefficients. In terms of the resulting \(c_1,c_2\),
\[
\frac{P_{\rm K}}{8\pi^2}
=
\frac{c_1^2}{8}(X^4-x_0^4)
+c_1c_2(X-x_0)
+\frac{c_2^2}{4}(x_0^{-2}-X^{-2}).
\]

The expression quoted in the note,
\[
\boxed{
\frac{P_{\rm K}}{8\pi^2}
=1+6x_0+9x_0^2(1+X^{-2})+O_X(x_0^3),
}
\]
is correct as a small-\(x_0\), fixed-\(X\) expansion. It is **not** the exact finite-\(X\) formula. In the limit \(X\to\infty\), the answer becomes exactly
\[
(1+3x_0)^2=1+6x_0+9x_0^2.
\]
Accordingly, “Kähler exact optimum” is appropriate for the variational solution, but the displayed truncated polynomial must be called its expansion.

---

## 4. Hodge-index coefficient

In \(\operatorname{Ric}=-6g\) units,
\[
[\omega_X]=-\frac{\pi}{3}c_1(X).
\]
For \(k\) equal exceptional areas \(\pi x_0\),
\[
[\omega]=[\omega_X]-\pi x_0\sum_{i=1}^k e_i,
\qquad
c_1(M)=c_1(X)-\sum_{i=1}^k e_i,
\]
where \(e_i^2=-1\). Therefore
\[
[\omega]^2=\pi^2\left(\frac A9-kx_0^2\right),
\qquad
c_1(M)\cdot[\omega]
=-\pi\left(\frac A3+kx_0\right).
\]
The Kähler scalar estimate gives
\[
S\ge32\pi^2
\frac{(A/3+kx_0)^2}{A/9-kx_0^2}.
\]
Since \(W_+=S/24\) for a Kähler surface,
\[
P=\frac S4-8\pi^2(A-k).
\]
Writing \(h=k/A\),
\[
\boxed{
\frac{P}{8\pi^2k}
\ge
1+\frac{6x_0+9(1+h)x_0^2}{1-9hx_0^2}.
}
\]
In particular,
\[
\frac{P}{8\pi^2k}\ge1+6x_0,
\]
and in the sparse regime,
\[
\frac{P}{8\pi^2k}
\ge1+6x_0+9x_0^2+O(hx_0^2).
\]
Thus \(\varepsilon=3x_0\) gives the claimed \(1+2\varepsilon\) linear term. The coefficient \(6x_0\) is exactly the Hodge-index Kähler penalty. The additional finite-cell contribution \(9x_0^2X^{-2}\) is interpolation/boundary cost, not part of the global Hodge-index bound.

The linear coefficient is therefore a theorem for Kähler metrics without any U(2) assumption. It is not yet a theorem for non-Kähler cells.

---

## 5. What the numerical evidence does and does not show

Every profile actually returned in `u2_cell_grid2.jsonl` has
\[
P(U)>8\pi^2.
\]
At the smallest scale,
\[
P/(8\pi^2)-1\approx1.794\times10^{-3},
\]
whereas the identity residual is at most about \(2.5\times10^{-8}\); the sign is therefore robust for the evaluated profiles.

The small-scale data also support
\[
\frac{P/(8\pi^2)-1}{x_0}\longrightarrow6:
\qquad
5.4519,\;5.8756,\;5.9807
\]
for \(x_0=0.03,0.003,0.0003\) at \(X=10\). The split is
\[
\frac{4\Delta W_+}{8\pi^2x_0}\to4,
\qquad
\frac{\Delta S/12}{8\pi^2x_0}\to2.
\]

The non-Kähler saving relative to the Kähler optimum is consistent with
\[
P_{\rm nonK}
=
P_{\rm K}
-C\,8\pi^2x_0^2\log(1/x_0)+O(x_0^2),
\]
with the supplied small-scale values suggesting \(C\) of order \(8\!-\!10\). This is evidence, not a resolved asymptotic coefficient; a polynomial-degree sweep is required. The note’s statement that the gain at \(x_0=3\times10^{-4}\) is \(0.06x_0\) is numerically inaccurate: it is about \(0.022x_0\) relative to the Kähler value.

The topological identity residual checks chirality, normalization, and quadrature consistency, but is not completely independent because \(P,S,W_\pm\) all come from the same symbolic curvature implementation. The exact Kähler and model-space tests are the stronger independent checks.

The defensible numerical conclusion is:

> Every returned degree-12, monotone-\(b\), single-bolt profile has \(P>8\pi^2\), and the small-\(x_0\) values are consistent with slope \(6\).

It does **not** establish that every U(2)-invariant cell has \(P>8\pi^2\). Minimization over a finite-dimensional family supplies upper bounds on the true infimum, not lower bounds.

### Parametrization blind spots

1. **Monotone \(b\):** the global coordinate \(x=b^2\) excludes turning points, internal necks, and profiles requiring several radial charts.

2. **Degree 12:** narrow transition layers, slowly decaying modes, or resonant logarithmic modes may be poorly represented. The leading coefficient appears stable; the putative \(x_0^2\log x_0\) coefficient is much more sensitive.

3. **Outer freezing:** \(\phi=(1-u)^3\) heavily suppresses deformations near \(X\). This is compatible with an exact-collar problem but may hide efficient transition layers at fixed degree.

4. **Local optimization:** runs start from the Kähler solution in a nonconvex problem. There is no multistart or basin analysis, and several rows terminate at the function-evaluation cap rather than convergence.

5. **No degree-convergence study:** high quadrature resolution does not replace degree \(12,16,20,\dots\) comparisons and independent restarts.

6. **Fixed CH exterior:** appropriate for the planted-cell problem, but it excludes global competitors where the exterior deforms together with the core.

7. **Single centered bolt:** no clustered blow-ups or different orbit structures are represented.

The claimed \(X\)-insensitivity is accurate at small \(x_0\), but not uniformly: differences become several percent around \(x_0=0.3\) and roughly ten percent by \(x_0=3\).

A further structural limitation is important. Diagonal U(2)-invariant metrics of this form carry invariant Hermitian structures. Thus the ansatz tests an aligned complex/Hermitian sector and does not automatically cover a Burns complex structure rotated relative to the complex-hyperbolic complex structure. That relative orientation is a potential first-order modulus.

---

## 6. Universality beyond U(2)

Burns satisfies
\[
s=0,\qquad W^+=0
\]
in its complex orientation, so
\[
\mathcal F(g)=\int\left(\frac{s^2}{12}+4|W^+|^2\right)dV
\]
vanishes there and is stationary under suitably decaying variations with controlled ALE boundary terms. This explains why ordinary transverse shape changes are expected to enter quadratically.

It does **not** by itself prove that the glued order-\(x_0\) coefficient is universally \(6\). The leading correction is a boundary/flux pairing between the Burns \(r^{-2}\) asymptotic mode and the background curvature. One must control all zero modes that can modify that pairing: diffeomorphisms, scaling, ALE mass/tail, scalar-flat ASD deformations, and the relative orientation of the Burns complex structure.

In particular, complex-hyperbolic isotropy does not force orientation independence. Its \(U(2)\) isotropy fixes \(\omega_{\rm CH}\) and need only make the coefficient a function of the angle \(\theta\) between the Burns and CH Kähler forms. At linear order in the ambient curvature, the possible dependence has the schematic form
\[
\kappa(\theta)=a+b\,P_2(\cos\theta).
\]
The present U(2) computation determines only the aligned value \(\kappa(0)=6\). It does not determine \(\min_\theta\kappa(\theta)\). A triaxial or off-diagonal Bianchi IX computation is the smallest cohomogeneity-one extension capable of testing this modulus.

A precise perturbative theorem would set \(x_0=\varepsilon^2\) and consider marked one-bolt cells which, after rescaling and gauge fixing, converge in weighted \(C^{2,\alpha}\) or \(H^2\) spaces to a Burns metric, with no additional bubbles or necks. The required conclusion is
\[
P(U_{\varepsilon,\theta})
=
8\pi^2\left(1+\kappa(\theta)\varepsilon^2\right)
+O\!\left(\varepsilon^4\log\frac1\varepsilon\right),
\]
followed by a proof that
\[
\min_\theta\kappa(\theta)=6
\]
if universality is to hold. Equivalently, one needs
\[
P(U_\varepsilon)\ge
8\pi^2(1+6x_0)
-Cx_0^2\log(1/x_0)
\]
uniformly over the allowed nonsymmetric perturbations.

That requires:

- gauge-fixed linearization and weighted Fredholm theory on Burns;
- classification of the kernel modulo diffeomorphism, including scale, mass, rotations, and ASD deformations;
- coercivity of the Hessian transverse to that kernel;
- explicit evaluation of the ALE-end flux pairing;
- proof relating the relevant tail/mass parameter to the intrinsic exceptional area;
- control of the transition annulus and replacement by an exact CH collar;
- minimization over the relative-orientation modulus.

### Logarithmic terms

Terms of order
\[
x_0^2\log(1/x_0)
\]
are plausible in four dimensions because resonant tail interactions can produce \(r^{-1}\,dr\) integrals. The numerical non-Kähler saving is consistent with such a term.

Criticality of Burns alone does **not** exclude
\[
x_0\log(1/x_0).
\]
Its absence must be established by the indicial and flux calculation, showing cancellation of the potentially resonant first-order cross term. The ASD/scalar-flat structure of Burns and Einstein/half-conformally-flat structure of CH strongly suggest such cancellation, but it is not proved by the supplied computation. Consequently the safe asymptotic claim is currently numerical:
\[
P/(8\pi^2)=1+6x_0+o(x_0)
\]
inside the searched ansatz, with evidence that the next correction contains \(x_0^2\log(1/x_0)\).

## Final assessment

The global identity, cell identity, topology sign, bolt condition, curvature-operator sign, downstream complex-chirality choice, Burns value, and Hodge-index coefficient \(6x_0\) are correct. The principal corrections are:

1. `u2_curvature.py` labels the raw chirality opposite to the complex orientation; `u2_xcoord.py` repairs this correctly.
2. The displayed Kähler formula is a small-\(x_0\) expansion, not the exact finite-\(X\) expression.
3. The extremizing profile is boundary-matched in \(C^1/H^2\), not literally CH on an open collar, although collar smoothing preserves the infimum.
4. “Every U(2) cell has \(P>8\pi^2\)” is not proved; only every returned parametrized profile has that property.
5. The slope-\(6\) universality heuristic misses possible ALE kernel and relative-complex-orientation modes. Criticality of Burns is insufficient until the flux pairing is computed and minimized over those modes.
6. The data plausibly reveal a non-Kähler \(x_0^2\log(1/x_0)\) saving, but neither its coefficient nor the absence of an order-\(x_0\log x_0\) term is yet rigorous.