# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read the Theorem E proof package and the new off-bolt Weyl computation. Decide what is rigorously proved by the analytic/Fuchsian plus CAPD/Wazewski chain, and separately what the floating-point off-bolt spectra support about conformal Kählerness. Check the use of Derdzinski: does finding three distinct eigenvalues in both chiral Weyl blocks at one interior point exclude the Einstein metric from being locally conformal to a Kähler metric in either orientation? Note that at t=0.5 and d in the validated interval the reported A eigenvalues are approximately (-0.845829,-0.841893,1.687721) and B approximately (-1.9603,0.4966,1.4637), with scalar -24 and Ricci0 norm 2.5e-11. Explain what remains to turn this into a computer-assisted theorem if interval rigor matters.

## Integrated Scientific Memo

## Verification memo

### 1. What the Fuchsian–CAPD–Ważewski chain rigorously proves

Subject to the correctness of the cited Arb/CAPD interval computations, the package gives a genuine computer-assisted existence theorem:

> For some
> \[
> d_0\in I=[0.28697953,0.28701987],
> \]
> the diagonal Bianchi IX bolt solution with \(b=4/5\) extends to a complete real-analytic Einstein metric
> \[
> \operatorname{Ric}=-6g
> \]
> on \(\mathcal O(-1)\to\mathbb{CP}^1\), and has an ACH end with
> \[
> q_\infty\in[0.7839621877,0.7850029323],\qquad
> \rho_\infty=e^{q_\infty}\in[2.1901328142,2.1924133694].
> \]

The chain establishes the following points.

1. **Analytic bolt family.**  
   For every \(d\in I\), the complex-disc Fuchsian contraction constructs a unique local solution
   \[
   a_1=A(t^2),\qquad a_2=B(t^2),\qquad a_3=tC(t^2),
   \]
   satisfying the smooth \(\mathcal O(-1)\)-bolt conditions and
   \[
   A-B=d\,t^4+O(t^6).
   \]
   This is stronger than a formal power series: the remainder is enclosed and the contraction factor is \(0.0325\).

2. **Einstein constraint.**  
   The note overloads \(C\), using it both for \(a_3/t\) and for the constraint. Writing the latter as \(\mathcal H\),
   \[
   \mathcal H'=-2S\mathcal H,\qquad S=t^{-1}+O(t).
   \]
   Thus
   \[
   t^2\exp\!\left(2\int_0^t(S(r)-r^{-1})\,dr\right)\mathcal H(t)
   \]
   is constant. Bolt regularity makes its limit at \(t=0\) zero, hence \(\mathcal H\equiv0\). Therefore the constructed solutions satisfy the full Einstein equations.

3. **Validated finite-time transport.**  
   The corrected CAPD field was symbolically matched to the Einstein vector field. The 40 parameter tiles cover all of \(I\), include the Fuchsian remainder, and are transported to \(T=2.75\) into the verified cusp block.

4. **Ważewski selection.**  
   The endpoint tiles lie in opposite unstable slabs, while the stable faces and \(\zeta=\zeta_0\) are ingress faces and the \(q\)-faces cannot be reached. In fact, the strict slab margin implies the endpoint trajectories must leave through opposite \(u\)-faces unless an endpoint itself stays forever, which would already suffice. Continuous dependence on \(d\), supplied by the uniform Fuchsian contraction and ODE dependence, then gives at least one \(d_0\in I\) whose trajectory remains in the block for all future time.

5. **ACH convergence and Rossi enclosure.**  
   Inside the block,
   \[
   \zeta(t)\le \zeta(T)e^{-c(t-T)},\qquad c=1.998462\ldots,
   \]
   and all transverse equilibrium coordinates are \(O(\zeta)\). The quadratic drift estimate for
   \[
   \widetilde\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q
   \]
   gives
   \[
   |q_\infty-\widetilde\Phi(T)|
   \le \frac{M\zeta(T)^2}{2c}
   \le 4.57\times10^{-4},
   \]
   producing the stated rigorous intervals. Completeness follows because \(t\) is radial arclength on \([0,\infty)\) and the principal orbits are compact.

The chain proves **existence**, not uniqueness of \(d_0\), uniqueness of the Einstein filling, the numerical branch picture, or standard-CR nonexistence. In particular, it does not rigorously identify \(d_0\) with the floating shooting value \(0.286999618893\). The assertion that \(\rho\ne1\) gives a nonstandard homogeneous CR sphere additionally uses the standard classification of left-invariant CR structures on \(S^3\); that classification is invoked but not proved in the supplied files.

Claims stronger than this—such as the full isometry group being exactly \(SU(2)\), exclusion of Hermitian structures, or a definitive chirality assignment—are not established by the supplied rigorous package and are unnecessary for the requested conclusion.

---

### 2. What the off-bolt computation actually supports

At \(t=0.5\), for the central floating parameter, the reported chiral spectra are
\[
A\approx(-0.845828848,-0.841892645,1.687721493),
\]
\[
B\approx(-1.960260539,0.496554187,1.463706352).
\]
Their adjacent gaps are approximately
\[
A:\quad 0.00393620,\ 2.52961,
\qquad
B:\quad 2.45681,\ 0.96715.
\]
At both endpoints of the validated \(d\)-interval, the smallest gaps remain approximately \(0.003936\) and \(0.967\). The values
\[
s=-24+O(10^{-11}),\qquad |\operatorname{Ric}^{\circ}|\simeq2.5\times10^{-11}
\]
are strong consistency checks on the ODE-derived radial two-jet and the independent coordinate/JAX curvature evaluation. The bolt and large-\(t\) limits also agree numerically with the exact bolt blocks and the complex-hyperbolic asymptotics.

Thus the floating computation gives compelling evidence that both chiral Weyl operators have simple spectrum at an interior orbit for the desired Einstein trajectory. It is not yet a theorem because:

- the shooting and curvature evaluation use floating point;
- only the two endpoints and one central \(d\) were sampled;
- the Ważewski proof selects an unspecified \(d_0\in I\);
- sampling those three values does not exclude a spectral collision at an unsampled \(d\).

The small Einstein residual is an implementation check, not a rigorous eigenvalue-error bound.

---

### 3. Correct conformal-Kähler implication

Yes: **three distinct eigenvalues in both chiral Weyl blocks at one interior point exclude a conformally Kähler neighborhood of that point in either orientation.**

The required implication is elementary and does not need the difficult converse part of Derdziński’s theorem. If
\[
\widehat g=e^{2f}g
\]
is Kähler on an open set, then in its complex orientation
\[
\operatorname{spec}(W^+_{\widehat g})
=
\left\{\frac{\widehat s}{6},
-\frac{\widehat s}{12},
-\frac{\widehat s}{12}\right\}.
\]
Hence \(W^+_{\widehat g}\) has a repeated eigenvalue, including the scalar-flat case where it vanishes. In four dimensions the splitting
\[
\Lambda^2=\Lambda^+\oplus\Lambda^-
\]
is conformally invariant, and conformal rescaling multiplies the corresponding Weyl endomorphism by a scalar without changing eigenvalue multiplicities. Therefore:

- simple \(W^+\)-spectrum excludes conformal Kählerness in one orientation;
- simple \(W^-\)-spectrum excludes it in the opposite orientation;
- simple spectra in both blocks at the same point exclude both orientations locally.

The exact bolt spectra do **not** give this conclusion because each has multiplicity pattern \((2,1)\), as bolt isotropy forces. They do exclude the Einstein metric itself from being Kähler: for scalar curvature \(-24\), a Kähler block would have spectrum \((-4,2,2)\), whereas the exact bolt blocks are
\[
\left\{\frac{41}{8},-\frac{41}{16},-\frac{41}{16}\right\},
\qquad
\left\{\frac{91}{8},-\frac{91}{16},-\frac{91}{16}\right\}.
\]

There is a useful global strengthening. For either chiral block define the discriminant
\[
\Delta_\pm=\prod_{i<j}(\lambda_i^\pm-\lambda_j^\pm)^2.
\]
For a trace-free symmetric \(3\times3\) operator \(W\), equivalent formulas are
\[
\Delta(W)
=\frac12\bigl(\operatorname{tr}W^2\bigr)^3-27\det(W)^2
=\frac12\left[(\operatorname{tr}W^2)^3
-6(\operatorname{tr}W^3)^2\right].
\]
The metric is real analytic, so \(\Delta_\pm\) are real-analytic scalar functions. If the metric were conformally Kähler on any nonempty open set in a given orientation, the corresponding discriminant would vanish there and hence, by analytic continuation on the connected manifold, vanish identically. Therefore rigorous positivity of **both** discriminants at one point would exclude conformal Kählerness on every nonempty open subset, in either orientation—not merely near that point.

---

### 4. What is needed for an interval-rigorous theorem

The natural certificate is a uniform statement over the entire validated parameter interval:

\[
\Delta_+(t_*,d)>0,\qquad \Delta_-(t_*,d)>0
\quad
\text{for all }d\in I
\]
at a fixed radius such as \(t_*=0.5\) or \(1\).

A rigorous implementation requires:

1. **Validated state boxes at \(t_*\).**  
   Transport all 40 Fuchsian parameter tiles to \(t_*\). This automatically includes the unknown Ważewski-selected \(d_0\).

2. **An exact moving-frame curvature formula.**  
   Use the orthonormal coframe
   \[
   e^0=dt,\qquad e^i=a_i\sigma_i
   \]
   to express \(W^\pm\) algebraically in \(a_i,y_i,y_i'\), and eliminate \(y_i'\) using the exact Einstein vector field. This is preferable to interval autodifferentiation through Euler coordinates and Cholesky factorization.

3. **Outward-rounded symmetric Weyl blocks.**  
   Derive the self-adjoint trace-free blocks directly. The floating code symmetrizes after evaluation; a proof should not depend on correcting numerical asymmetry afterward.

4. **Certified simplicity.**  
   Either compute disjoint interval eigenvalue enclosures or prove
   \[
   0\notin \Delta_\pm(\text{state box})
   \]
   on every parameter tile. Direct pairwise eigenvalue differences may be numerically sharper than a fully expanded discriminant, especially for the \(A\)-block, whose smallest observed gap is only \(3.94\times10^{-3}\).

5. **A written conformal-multiplicity lemma.**  
   Record the Kähler Weyl spectrum and conformal invariance of chiral multiplicities, followed by the real-analytic continuation argument if the global “no conformally Kähler open subset” statement is claimed.

The observed margins at \(t=0.5\)—approximately \(3.9\times10^{-3}\) for \(A\) and \(0.97\) for \(B\)—make such a certificate plausible. Until these interval evaluations are supplied, the scientifically correct status is:

- **Theorem E and its Rossi enclosure:** computer-assisted theorem;
- **the metric itself is non-Kähler:** rigorously proved by the exact bolt computation;
- **non-conformal-Kählerness in either orientation:** strongly supported by floating-point off-bolt spectra, but not yet interval-certified.