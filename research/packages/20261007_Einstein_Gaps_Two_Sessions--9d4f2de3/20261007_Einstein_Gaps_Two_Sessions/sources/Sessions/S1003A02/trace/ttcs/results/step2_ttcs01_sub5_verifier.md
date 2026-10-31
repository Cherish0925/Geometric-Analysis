# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md",
    "Sessions/S1003A02/workspace/scripts/u2_curvature.py",
    "Sessions/S1003A02/workspace/scripts/u2_xcoord.py",
    "Sessions/S1003A02/workspace/scripts/kahler_cell_exact.py",
    "Sessions/S1003A02/workspace/scripts/u2_cell_jax_log.py",
    "Sessions/S1003A02/workspace/data/u2grid/u2_cell_grid2.jsonl",
    "Sessions/S1003A02/workspace/figures/u2_cell_cost.png",
    "Skills/geometric-analysis/references/conventions-and-literature.md",
    "Skills/geometric-analysis/references/results-and-questions.md"
  ]
}
```

## Task

Check the mathematics and code behind the O11 blow-up cell computation for four-manifold Einstein gaps. (1) Verify the exact identity P - 8 pi^2 Q = (S - 32 pi^2 A)/12 + 4(W_+ - (4/3) pi^2 A) on X # k CP2bar # l(S^1xS^3) with Hilbert-Schmidt norms on two-forms (conventions file), and the cell identity P(U) = 8pi^2 + 4 Delta W_+ + Delta S/12 for a blown-up ball agreeing with complex hyperbolic metric near the boundary; check signs, orientation (complex orientation, E.E=-1) and that Burns gives exactly 8 pi^2. (2) Check the U(2) cohomogeneity-one curvature code: frame brackets, Koszul formula, curvature-operator sign, the identification of the complex orientation (the script's 'SD' block is anti-complex since FS gives W+=0 there), bolt regularity F'(x0)G'(x0)=1 for O(-1), smoothness/H^2 matching at X, and the Kahler exact optimum P/8pi^2 = 1 + 6x0 + 9x0^2(1+X^-2). (3) Check the claim that the linear coefficient 6x0 equals the Hodge-index Kahler bound (c1.omega)^2/omega^2 with epsilon = 3 x0 in Ric=-6g units. (4) Judge whether the numerical evidence (table in the note) really supports 'every U(2) cell has P > 8pi^2 and the slope tends to 6 also for non-Kahler cells', and identify any parametrization blind spot (e.g. phi=(1-u)^3 freezing near X, monotone b=sqrt(x), fixed outer CH region, degree 12) that could hide a cell with P < 8pi^2. (5) Assess the heuristic that the order-x0 coefficient is universal beyond U(2) because Burns is critical; state precisely what would have to be proved and whether log terms could enter. Give a direct scientific memo with any errors found and their consequences.

## Output

# Scientific verification memo

## 1. Chern–Weil identities, topology, orientation, and the Burns value

With the operator Hilbert–Schmidt convention in `conventions-and-literature.md`,
\[
4\pi^2T_+=\frac{S}{24}+2W_+-\frac{P}{2},
\]
so
\[
P=\frac{S}{12}+4W_+-8\pi^2T_+.
\]
For
\[
M=X\#k\overline{\mathbb {CP}}^{\,2}\#\ell(S^1\times S^3),
\]
a complex blow-up changes \((\chi,\tau)\) by \((1,-1)\), hence changes \(T_+=2\chi+3\tau\) by \(-1\). A connected sum with \(S^1\times S^3\) changes \((\chi,\tau)\) by \((-2,0)\), hence changes \(T_+\) by \(-4\). Therefore
\[
T_+(M)=A-k-4\ell=A-Q.
\]
For the Kähler–Einstein metric on \(X\),
\[
S_{\rm KE}=32\pi^2A,\qquad W_+^{\rm KE}=\frac{S_{\rm KE}}{24}
=\frac43\pi^2A.
\]
Substitution gives exactly
\[
\boxed{
P-8\pi^2Q
=\frac{S-32\pi^2A}{12}
+4\left(W_+-\frac43\pi^2A\right).
}
\]
All constants and signs here are correct.

For a blow-up cell \(U\) replacing a ball \(B\), the disk bundle of degree \(-1\) has
\[
\chi(U)=2,\qquad \tau(U)=-1,
\]
whereas \(\chi(B)=1,\tau(B)=0\). Thus
\[
\Delta T_+=2(1)+3(-1)=-1.
\]
If the two metrics coincide on an outer collar, the transgression terms cancel, and
\[
P(U)-P(B)
=\frac{\Delta S}{12}+4\Delta W_+-8\pi^2\Delta T_+.
\]
Since the complex-hyperbolic ball is Einstein, \(P(B)=0\), yielding
\[
\boxed{
P(U)=8\pi^2+4\Delta W_++\frac{\Delta S}{12}.
}
\]
The sign \(+8\pi^2\) is tied to the complex orientation and \(E\!\cdot\!E=-1\). Reversing chirality without swapping \(W^+\) and \(W^-\) would give the wrong relative formula.

For Burns, \(K=x-x_0\), hence \(H=-x_0\) and
\[
L=x^2H''-2H=2x_0.
\]
Using
\[
P=4\pi^2\int_{x_0}^{\infty}\frac{L^2}{x^3}\,dx
\]
gives
\[
P_{\rm Burns}
=16\pi^2x_0^2\int_{x_0}^{\infty}x^{-3}\,dx
=8\pi^2.
\]
Thus the complete Burns metric has exactly the stated value. In the complex orientation it has \(s=0\) and \(W^+=0\).

---

## 2. U(2) curvature code and geometric regularity

### 2.1 Frame brackets and Koszul formula

For
\[
E_0=\partial_t,\qquad E_1=X_1/b,\qquad E_2=X_2/b,\qquad E_3=X_3/a,
\]
with \([X_1,X_2]=2X_3\) cyclically, the script uses
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
These are correct. The implemented Koszul formula
\[
2\langle\nabla_{E_i}E_j,E_k\rangle
=c_{ij}^{k}-c_{jk}^{i}+c_{ki}^{j}
\]
is also correct.

The stored tensor is
\[
R_{ijkl}=\langle R(E_i,E_j)E_k,E_l\rangle.
\]
With this ordering, the explicit minus sign in `Rop` is necessary: on a unit round sphere it makes the curvature operator \(+\mathrm{Id}_{\Lambda^2}\). The Ricci contraction
\[
\operatorname{Ric}_{jk}=\sum_i R_{ijki}
\]
then has the standard positive value on the round sphere. The resulting \(3\times3\) Frobenius norms are precisely operator Hilbert–Schmidt norms, as required by the manuscript convention.

### 2.2 Orientation label in `u2_curvature.py`

There is a real labeling error in the comments of `u2_curvature.py`.

For the stated bracket convention, \(d\sigma_3=-2\sigma_1\wedge\sigma_2\). When \(a=bb'\), a closed Kähler form is
\[
\omega=-a\,dt\wedge\sigma_3+b^2\sigma_1\wedge\sigma_2
=-e^0\wedge e^3+e^1\wedge e^2.
\]
Its complex volume orientation is the opposite of
\[
e^0\wedge e^3\wedge e^1\wedge e^2.
\]
Consequently the raw `SD` block in `u2_curvature.py` is anti-complex. This is exactly why Fubini–Study gives zero in the raw `Wp` block rather than the raw `Wm` block.

The downstream correction in `u2_xcoord.py`,
```python
'wpsq_c': conv(U.wmsq),
'wmsq_c': conv(U.wpsq)
```
is correct. Thus the numerical \(W_+\) values and the cell identity use complex chirality correctly, despite the incorrect orientation comments in the first script. Any later use of `U.wpsq` directly as complex \(W^+\) would reverse the two chiral blocks.

### 2.3 Coordinate conversion and volume

From \(x=b^2\) and
\[
g=\frac{dx^2}{4G}+F\sigma_3^2+x(\sigma_1^2+\sigma_2^2)
\]
one gets
\[
\frac{dx}{dt}=2\sqrt G,\qquad a=\sqrt F,\qquad b=\sqrt x,
\]
and
\[
dV=\pi^2x\sqrt{\frac FG}\,dx.
\]
These formulas are correctly implemented. Since
\[
bb'=\sqrt G,
\]
the Kähler equation \(a=bb'\) is exactly \(F=G\).

The complex-hyperbolic checks are consistent:
\[
K=x+x^2,\qquad s=-24,\qquad \operatorname{Ric}=-6g,
\]
and
\[
S(B_X)=288\pi^2X^2,\qquad
W_+(B_X)=12\pi^2X^2.
\]
The value `Fball=72*pi^2*X^2` in the JAX script is therefore
\[
S(B_X)/12+4W_+(B_X),
\]
as intended.

### 2.4 Bolt regularity and exceptional area

If
\[
F=f_1(x-x_0)+O((x-x_0)^2),\qquad
G=g_1(x-x_0)+O((x-x_0)^2),
\]
then setting \(x-x_0=g_1r^2+O(r^4)\) gives
\[
g=dr^2+f_1g_1r^2\sigma_3^2
+x_0(\sigma_1^2+\sigma_2^2)+O(r^2).
\]
The Hopf fiber generated by \(X_3\) has period \(2\pi\), so smoothness of the degree-\(-1\) bolt requires
\[
\boxed{F'(x_0)G'(x_0)=1.}
\]
The base metric \(\sigma_1^2+\sigma_2^2\) has area \(\pi\), hence
\[
\operatorname{Area}(E)=\pi x_0.
\]

In the exponential parametrization, the Kähler base profile has \(K'(x_0)=1\). The imposed relation
\[
p_1(x_0)+p_2(x_0)=0
\]
therefore enforces the product-of-slopes condition exactly.

### 2.5 Outer matching regularity

The four Kähler conditions
\[
H(x_0)=-x_0,\quad H'(x_0)=0,\quad
H(X)=X^2,\quad H'(X)=2X
\]
produce a metric that is \(C^1\) across \(x=X\) when joined to complex hyperbolic space. It is piecewise smooth and locally \(H^2\); generally \(H''(X)\) does not equal the complex-hyperbolic value.

Thus the computed profile does not literally coincide with the exterior metric on an open collar. It represents the \(H^2\) closure of that class. A \(C^1\), piecewise-smooth profile can be modified in an annulus of width \(\delta\) to become exactly complex hyperbolic near the outer hypersurface, with curvature-energy change \(O(\delta)\). Therefore the variational infimum is unchanged, although the displayed extremal profile need not itself be smooth across the join.

The factor
\[
\phi=(1-u)^3
\]
makes the perturbation and its first two \(x\)-derivatives vanish at \(X\), relative to the Kähler base. It does not make the metric equal to the exterior metric on an open collar, and it does not repair the base profile’s second-derivative jump.

---

## 3. Exact Kähler variational problem and the Hodge-index comparison

For \(K=x+H\),
\[
P=4\pi^2\int_{x_0}^X\frac{L^2}{x^3}\,dx,
\qquad
L=x^2H''-2H.
\]
The Euler–Lagrange equation is
\[
(x^{-1}L)''-2x^{-3}L=0,
\]
whose general solution is
\[
L=c_1x^3+c_2.
\]
Thus
\[
H=\frac{c_1}{4}x^3-\frac{c_2}{2}+c_3x^2+\frac{c_4}{x}.
\]
The four endpoint conditions uniquely determine the coefficients. An exact convenient expression for the energy is
\[
\boxed{
\frac{P_{\rm K}}{8\pi^2}
=\frac{c_1^2}{8}(X^4-x_0^4)
+c_1c_2(X-x_0)
+\frac{c_2^2}{4}(x_0^{-2}-X^{-2}),
}
\]
with \(c_1,c_2\) obtained from the four linear equations in `kahler_cell_exact.py`.

The polynomial displayed in the note is not the exact finite-\(X\) expression. It is the small-\(x_0\) expansion
\[
\boxed{
\frac{P_{\rm K}}{8\pi^2}
=1+6x_0+9x_0^2(1+X^{-2})+O_X(x_0^3).
}
\]
It becomes exactly
\[
(1+3x_0)^2=1+6x_0+9x_0^2
\]
in the \(X\to\infty\) problem. The table numerically agrees with the finite-\(X\) expansion; for example \(x_0=0.1,X=10\) gives a value slightly above \(1.6909\), namely \(1.691516\), due to the omitted higher terms.

### Hodge-index calculation

Let \(e_i=\mathrm{PD}[E_i]\), \(e_i^2=-1\), and take equal exceptional areas \(\pi x_0\). Since \(\operatorname{Ric}=-6g\),
\[
[\omega_X]=-\frac{\pi}{3}c_1(X).
\]
On the blow-up,
\[
[\omega]=[\omega_X]-\pi x_0\sum_{i=1}^k e_i,
\qquad
c_1(M)=c_1(X)-\sum_{i=1}^k e_i.
\]
Hence
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
For a Kähler surface \(W_+=S/24\), so
\[
P=\frac S4-8\pi^2(A-k).
\]
Writing \(h=k/A\),
\[
\frac{P}{8\pi^2k}
\ge
1+\frac{6x_0+9(1+h)x_0^2}{1-9hx_0^2}.
\]
In particular,
\[
\frac{P}{8\pi^2k}\ge1+6x_0,
\]
and in the sparse regime \(h\to0\),
\[
\frac{P}{8\pi^2k}
\ge1+6x_0+9x_0^2+O(h).
\]
Thus setting \(\varepsilon=3x_0\) gives \(1+2\varepsilon\) at linear order. The identification of the coefficient \(6x_0\) with the Hodge-index estimate is correct. The finite-\(X\) term \(9x_0^2X^{-2}\) is an extra interpolation cost and is not supplied by the global Hodge calculation.

---

## 4. What the numerical data establish

For every returned profile in the supplied JSON file,
\[
P_{\rm cell}>8\pi^2.
\]
At \(x_0=3\times10^{-4}\), the excess is about \(1.79\times10^{-3}\), far larger than the recorded identity residual. The residuals actually range from about \(1.3\times10^{-12}\) to \(2.45\times10^{-8}\), so the sign of the excess for the evaluated profiles is numerically stable.

The small-\(x_0\) split is also persuasive:
\[
\frac{4\Delta W_+}{8\pi^2x_0}\approx3.98,\qquad
\frac{\Delta S/12}{8\pi^2x_0}\approx2.00,
\]
giving a total slope near \(6\). The values
\[
5.981,\quad 5.876,\quad 5.45
\]
as \(x_0\) decreases from \(0.03\) to \(0.003\) to \(0.0003\) are consistent with
\[
\lim_{x_0\to0}\frac{P/(8\pi^2)-1}{x_0}=6.
\]

There is also evidence for a logarithmic second-order improvement. For \(X=10\),
\[
\frac{P_{\rm K}-P_{\rm nonK}}
{x_0^2\log(1/x_0)}
\]
is approximately \(9.0,8.7,7.8,8.0\) at \(x_0=0.0003,0.003,0.03,0.1\). Thus the data fit
\[
P_{\rm nonK}
=P_{\rm K}-C\,x_0^2\log(1/x_0)+\cdots
\]
better than a regular \(O(x_0^2)\) correction. Since \(x_0^2\log(1/x_0)=o(x_0)\), this remains compatible with slope \(6\).

The topological identity residual is useful for confirming the chirality swap, constants, and quadrature consistency. It is not fully independent of the curvature derivation, because \(P,S,W_\pm\) all originate from the same symbolic Riemann tensor. The exact Kähler values and the flat, round, Fubini–Study, complex-hyperbolic, and Burns tests provide the more independent verification.

### Parametrization blind spots

The computations do not supply a lower bound for the full U(2) variational problem. They provide explicit upper values obtained from a finite-dimensional search. The following geometric and numerical sectors are absent:

1. **Monotone orbit radius.** Using \(x=b^2\) globally assumes \(b\) is monotone. U(2)-invariant cells containing an internal neck, a turning point of \(b\), or multiple radial charts are omitted.

2. **Degree 12.** The logarithmic Chebyshev representation has only 24 coefficients. It may miss narrow layers, slowly decaying modes, or profiles requiring more angular-orbit distortion in the radial functions.

3. **Outer-jet restriction.** The cubic factor forces the perturbation’s first two jets to vanish relative to \(K_{\rm opt}\) at \(X\). Exact-collar profiles satisfy even stronger vanishing, so this is natural in an infinite-dimensional closure, but at degree 12 it can bias how efficiently a transition layer is represented.

4. **One initial profile and a nonconvex objective.** The reported optimization starts from the Kähler profile. Several rows ended because the function-evaluation cap was reached, and the JSON file contains neither final gradient norms nor Hessian information. Distinct local minima could remain unseen.

5. **No degree or multistart sweep in the supplied data.** Quadrature resolution is high, but convergence with respect to polynomial degree and random or structured restarts is not documented.

6. **Fixed complex-hyperbolic exterior data.** This is appropriate for a local planted-cell problem, but it omits global competitors in which the exterior geometry changes together with the core.

7. **Single centered bolt.** Clustered blow-ups and other orbit structures are absent.

The statement supported by the files is therefore:

> Every returned degree-12, monotone-\(b\), single-bolt U(2) profile has \(P>8\pi^2\), and its small-\(x_0\) behavior is consistent with slope \(6\).

The stronger statement for every U(2)-invariant cell is not derived by the computation alone. The reported \(X\)-insensitivity is accurate in the small-\(x_0\) rows; at \(x_0=0.3\) the variation is about \(3\%\), and at \(x_0=3\) the \(X=10\) and \(X=50\) values differ by roughly \(10\%\).

---

## 5. Universality beyond U(2)

Burns has
\[
s=0,\qquad W^+=0,
\]
so the functional
\[
\mathcal F(g)=\int\left(\frac{s^2}{12}+4|W^+|^2\right)dV
\]
vanishes there and is a sum of squares. Its first variation vanishes for variations for which the ALE-end terms are controlled. This explains why a decaying shape perturbation does not immediately change the zero-background value at first order.

That observation alone does not determine the \(x_0\) coefficient after insertion into complex-hyperbolic geometry. The coefficient comes from matching the Burns \(r^{-2}\) mode with the quadratic normal-coordinate curvature mode of the exterior. Variations that alter the ALE mass term, scaling mode, or another zero mode can alter this flux pairing unless those modes are fixed or classified.

A precise perturbative result would take the following form. Put \(x_0=\epsilon^2\). For marked one-bolt cells that, after rescaling and gauge fixing, approach a unit Burns metric in weighted \(C^{2,\alpha}\) or weighted \(H^2\) spaces, with no additional bubbles or necks,
\[
\boxed{
P(U_\epsilon)
\ge
8\pi^2\left(1+6\epsilon^2\right)
-C\epsilon^4\log(1/\epsilon).
}
\]
Equivalently,
\[
\liminf_{\epsilon\to0}
\frac{P(U_\epsilon)/(8\pi^2)-1}{\epsilon^2}\ge6.
\]

The mathematical ingredients behind such a result are:

- a gauge-fixed expansion on the growing Burns region;
- classification of the kernel of the linearized scalar/\(W^+\) map, including diffeomorphism, scale, mass, and any scalar-flat anti-self-dual deformation modes;
- coercivity of the second variation transverse to those modes;
- an explicit computation of the ALE-end flux, giving \(48\pi^2x_0\);
- control of the transition annulus and exact complex-hyperbolic collar;
- a relation between the asymptotic mass parameter and \(\operatorname{Area}(E)/\pi\). Outside U(2), the marked sphere’s area need not automatically determine the ALE mass.

The \(U(2)\) isotropy of complex-hyperbolic curvature helps: at linear order, nontrivial angular representations should be orthogonal to the invariant exterior curvature mode. The invariant scale/mass sector still requires explicit analysis.

Logarithmic terms are entirely plausible. Four-dimensional scale invariance and resonant ALE indicial roots naturally produce integrals of \(r^{-1}\), hence \(\epsilon^4\log(1/\epsilon)\), or \(x_0^2\log(1/x_0)\). The supplied numerical differences strongly point in that direction. Such terms do not alter the coefficient \(6\). Criticality of Burns by itself does not exclude an \(x_0\log x_0\) term; excluding that term requires the linearized indicial and flux computation.

## Bottom line

The global identity, relative cell identity, bolt normalization, Burns value, curvature-operator sign, downstream chirality choice, and Hodge-index coefficient \(6x_0\) are mathematically consistent. Two corrections are important:

1. `u2_curvature.py` labels the raw chirality opposite to the complex orientation; `u2_xcoord.py` repairs it correctly.
2. \(1+6x_0+9x_0^2(1+X^{-2})\) is a finite-\(X\) asymptotic expansion, not the exact finite-\(X\) formula.

The numerical profiles provide strong evidence for \(P>8\pi^2\) and slope \(6\) inside the searched ansatz, together with a likely \(x_0^2\log(1/x_0)\) non-Kähler improvement. They do not by themselves establish the corresponding lower estimate for all U(2) cells or for nonsymmetric cells.