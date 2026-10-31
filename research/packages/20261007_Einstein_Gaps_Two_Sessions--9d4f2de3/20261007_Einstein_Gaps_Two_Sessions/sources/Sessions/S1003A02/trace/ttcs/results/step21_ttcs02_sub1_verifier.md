# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md",
    "Sessions/S1003A02/workspace/scripts/ach_weyl_degeneracy_offbolt.py",
    "Sessions/S1003A02/workspace/data/ach_capd/weyl_degeneracy_offbolt.json",
    "Sessions/S1003A02/workspace/data/ach_capd/rossi_enclosure_b0.8.json",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Independently read the Theorem E proof package and the new off-bolt Weyl computation. Decide what is rigorously proved by the analytic/Fuchsian plus CAPD/Wazewski chain, and separately what the floating-point off-bolt spectra support about conformal Kählerness. Check the use of Derdzinski: does finding three distinct eigenvalues in both chiral Weyl blocks at one interior point exclude the Einstein metric from being locally conformal to a Kähler metric in either orientation? Note that at t=0.5 and d in the validated interval the reported A eigenvalues are approximately (-0.845829,-0.841893,1.687721) and B approximately (-1.9603,0.4966,1.4637), with scalar -24 and Ricci0 norm 2.5e-11. Explain what remains to turn this into a computer-assisted theorem if interval rigor matters.

## Output

# Independent scientific memo

## 1. What the analytic/Fuchsian–CAPD–Ważewski chain establishes

Taken together, the objects cited in `step15_ach_projected_theory.md` form a coherent computer-assisted existence proof.

### Local bolt solution

For every
\[
d\in I=[0.28697953,0.28701987],\qquad b=\frac45,
\]
the Fuchsian fixed-point argument constructs a unique solution near \(t=0\) with
\[
a_1=A(t^2),\qquad a_2=B(t^2),\qquad a_3=tC(t^2),
\]
where \(A,B,C\) are holomorphic in \(s=t^2\), \(A(0)=B(0)=4/5\), \(C(0)=1\), and
\[
A-B=d\,t^4+O(t^6).
\]
The exact order-six polynomial, complex-disc residual enclosures, and contraction factor \(0.0325\) establish real analyticity and the smooth \(\mathcal O(-1)\) bolt conditions, not merely a formal series.

There is a notation collision in the sentence about the Einstein constraint: \(C\) denotes both the radial factor \(a_3/t\) and, earlier, the constraint. A clean argument uses \(\mathcal H\) for the constraint:
\[
\mathcal H'=-2S\mathcal H,\qquad S=t^{-1}+O(t).
\]
Then
\[
t^2\exp\!\left(2\int_0^t\left(S(r)-\frac1r\right)\,dr\right)\mathcal H(t)
\]
is constant. Smoothness of the bolt makes \(\mathcal H=O(1)\), so this expression tends to zero as \(t\to0\), and therefore \(\mathcal H\equiv0\). This is the needed link from the tangential second-order equations to the full Einstein equation.

### Validated transport

The source-level symbolic comparison in `ach_capd_field_check.py` establishes that the corrected CAPD vector field is algebraically the Einstein vector field in the cancellation-free variables. The 40 parameter tiles cover all of \(I\), and the Fuchsian remainder is included in their initial interval states.

The CAPD transport to \(T=2.75\) gives, for every \(d\in I\), a state in
\[
B(1,10^{-2},[0.70,0.90]).
\]
The leftmost tile lies in the lower unstable slab and the rightmost tile lies in the upper unstable slab. The stable faces point inward, \(\zeta=10^{-2}\) points inward, \(\zeta=0\) is not reached at finite time, and the integrated \(q\)-motion is smaller than the verified distance to the \(q\)-faces.

Continuous dependence on \(d\)—available from the uniform Fuchsian contraction and ordinary ODE dependence—then makes the two unstable exit sets relatively open. If either endpoint remains in the block forever, it already supplies the desired parameter. Otherwise, the two endpoints belong to different disjoint open exit sets, which cannot cover the connected interval \(I\). Hence there is at least one
\[
d_0\in I
\]
whose orbit remains in the block for all \(t\ge T\).

### Asymptotic geometry

For this \(d_0\),
\[
\zeta(t)\le \zeta(T)e^{-c(t-T)},\qquad c=1.998462045\ldots .
\]
Inverting the eigen-coordinate transformation shows that all compact variables approach the equilibrium curve at the same rate. The estimate on
\[
\widetilde\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q
\]
gives
\[
\left|q_\infty-\widetilde\Phi(T)\right|
 \le \frac{M\zeta(T)^2}{2c},
\]
and the supplied interval arithmetic yields
\[
q_\infty\in[0.7839621877,0.7850029323],
\]
\[
\rho_\infty=e^{q_\infty}
 \in[2.1901328142,2.1924133694].
\]
Thus the end is asymptotically complex hyperbolic with fibre direction \(\sigma_1\), and its CR infinity is a Rossi sphere distinct from the standard member \(\rho=1\). The stated \(O(e^{-1.99t})\) rate follows from \(1.99<c\).

Completeness follows because \(t\) is radial arclength, the bolt is smooth, the principal \(SU(2)\)-orbits are compact, and any curve escaping to \(t=\infty\) has length at least its total variation in \(t\).

Accordingly, the chain proves existence of a complete real-analytic \(SU(2)\)-invariant Einstein metric
\[
\operatorname{Ric}=-6g
\]
on the total space of \(\mathcal O(-1)\to\mathbb{CP}^1\), with the stated Rossi parameter enclosure.

It does not identify a unique \(d_0\), nor does it identify the numerical value
\[
0.286999618893
\]
with the parameter selected by the topological continuation argument. It also does not establish the full numerical branch, standard-CR nonexistence, or uniqueness among all Einstein metrics. The relations \(a_1\not\equiv a_2\) and \(a_2/a_3\to\rho_\infty\ne1\) rigorously establish triaxiality in the diagonal family; classification of the full isometry group would require an additional isometry argument.

## 2. Exact bolt curvature versus conformal Kähler geometry

The repaired exact bolt calculation gives the two unordered chiral Weyl spectra
\[
\left\{\frac{41}{8},-\frac{41}{16},-\frac{41}{16}\right\},
\qquad
\left\{\frac{91}{8},-\frac{91}{16},-\frac{91}{16}\right\}.
\]
Both Weyl halves are nonzero, so the metric is neither self-dual nor anti-self-dual.

Because the Einstein metric has scalar curvature \(-24\), if this same metric were Kähler in its complex orientation, its corresponding Weyl block would have spectrum
\[
\left\{\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right\}
=\{-4,2,2\}.
\]
Neither bolt block has this spectrum. Thus the exact bolt computation excludes a parallel complex structure in either orientation.

It does not by itself exclude a conformally Kähler structure. Under a nonconstant conformal change, the Weyl eigenvalues may be multiplied by a point-dependent factor, while their multiplicities remain unchanged. Both bolt blocks already have the required \(1+2\) multiplicity pattern, forced there by bolt isotropy.

## 3. Correct use of the Derdziński Weyl-eigenvalue argument

Suppose on an open set
\[
\widehat g=e^{2f}g
\]
is Kähler. In four dimensions the Hodge decomposition
\[
\Lambda^2=\Lambda^+\oplus\Lambda^-
\]
is conformally invariant. With the complex orientation of \(\widehat g\),
\[
\operatorname{spec}(W^+_{\widehat g})
=
\left\{\frac{\widehat s}{6},
-\frac{\widehat s}{12},
-\frac{\widehat s}{12}\right\}.
\]
As a Weyl endomorphism, conformal rescaling only multiplies this block by a nonzero scalar factor. Hence the corresponding chiral block of \(g\) has at most two distinct eigenvalues at every point of that open set. For the opposite complex orientation, the same statement applies to the other chiral block.

Therefore:

- three distinct eigenvalues in \(W^+\) at a point exclude a conformally Kähler neighborhood of that point with one orientation;
- three distinct eigenvalues in \(W^-\) exclude the other orientation;
- three distinct eigenvalues in both blocks at the same point exclude both orientations there.

This implication is sound. The exclusion direction is actually the elementary Kähler Weyl-multiplicity fact plus conformal invariance; the deeper converse direction of Derdziński is not needed.

There is also a useful analytic strengthening here. Define the chiral discriminants
\[
\Delta_\pm
 =\prod_{i<j}(\lambda_i^\pm-\lambda_j^\pm)^2.
\]
For a trace-free \(3\times3\) Weyl block,
\[
\Delta_\pm
=
\frac12\bigl(\operatorname{tr}(W_\pm^2)\bigr)^3
-27\det(W_\pm)^2.
\]
The metric furnished by the Fuchsian construction is real analytic, so \(\Delta_\pm\) are real-analytic scalar functions. A conformally Kähler open set forces one of them to vanish throughout that open set. Real-analytic continuation would then make that discriminant vanish on the connected manifold. Thus rigorous positivity of both discriminants at one interior point would exclude even a conformally Kähler open patch anywhere on the manifold, in either orientation.

## 4. What the floating-point spectra support

At \(t=0.5\) for the central numerical parameter, the reported spectra are
\[
\operatorname{spec}(A)
\approx(-0.8458288480,-0.8418926447,1.6877214927),
\]
\[
\operatorname{spec}(B)
\approx(-1.9602605387,0.4965541871,1.4637063516).
\]
The adjacent gaps are approximately
\[
A:\quad 0.0039362033,\ 2.5296141374,
\]
\[
B:\quad 2.4568147258,\ 0.9671521645.
\]
At the two endpoints of \(I\), the smallest \(A\)-gap remains about \(0.003936\), and the smallest \(B\)-gap remains about \(0.967\). The corresponding discriminants are approximately
\[
\Delta_A\approx 6.36\times10^{-4},
\qquad
\Delta_B\approx 6.6\times10^{1}.
\]
Thus both blocks are well away from a repeated eigenvalue in floating arithmetic, although the first block has the quantitatively smaller separation.

The values
\[
s=-24+O(10^{-11}),\qquad
|\operatorname{Ric}^{\circ}|\approx2.5\times10^{-11}
\]
show strong agreement between the ODE-determined radial two-jet and the independent coordinate/JAX curvature implementation. Trace-freeness and near-symmetry of the displayed Weyl matrices give further internal consistency.

Scientifically, these data strongly support that the validated Einstein filling is not conformally Kähler in either orientation. They do not yet establish that statement mathematically for the Ważewski-selected metric, for three reasons:

1. `weyl_degeneracy_offbolt.py` uses floating-point shooting and JAX arithmetic.
2. It samples only \(d_-\), the numerical central value, and \(d_+\); the existence proof supplies an unspecified \(d_0\in I\).
3. Endpoint and midpoint sampling do not exclude a repeated spectrum at an unsampled parameter value.

The small Ricci residual is persuasive implementation evidence, but it is not an enclosure for the Weyl eigenvalue errors.

## 5. Ingredients of an interval-certified conformal-Kähler exclusion

A computer-assisted theorem can be assembled directly from the existing validated flow:

1. **Uniform state enclosure at \(t=0.5\).**  
   The 40 Fuchsian/CAPD parameter tiles already represent every \(d\in I\). Their interval states at \(t=0.5\) would enclose, in particular, every possible Ważewski-selected \(d_0\).

2. **Exact homogeneous curvature formula.**  
   In an oriented orthonormal coframe
   \[
   e^0=dt,\qquad e^i=a_i\sigma_i,
   \]
   both \(W^+\) and \(W^-\) can be written using \(a_i,y_i,y_i'\). The Einstein vector field replaces \(y_i'\) by elementary expressions in the CAPD state. This avoids interval differentiation through Euler coordinates and gives direct outward-rounded Weyl matrices.

3. **Exact symmetry and chirality identification.**  
   The true Weyl blocks are self-adjoint and trace-free. The present code symmetrizes the floating matrices before diagonalization; an interval proof should instead derive the self-adjoint blocks from the moving-frame formula. Since both chiral blocks are tested, swapping the labels \(+\) and \(-\) would not affect the final geometric conclusion.

4. **Certified spectral simplicity.**  
   Either disjoint interval eigenvalue enclosures or a strictly positive interval for
   \[
   \Delta_\pm
   =
   \frac12(\operatorname{tr}W_\pm^2)^3-27(\det W_\pm)^2
   \]
   would suffice. For the nearly repeated \(A\)-pair, the displayed matrix has a \(2\times2\) subblock with off-diagonal entry about \(1.346\times10^{-3}\); exploiting the exact block form may avoid cancellation in the discriminant. The observed \(A\)-gap of roughly \(3.94\times10^{-3}\) is large compared with the reported transport and floating errors, so this appears numerically accessible.

5. **Uniformity over all parameter tiles.**  
   Positivity of both discriminants on every one of the 40 \(d\)-tiles would automatically apply to the unknown \(d_0\), without refining the topological existence argument or locating \(d_0\) uniquely.

Once those interval statements are available, the result would be:

> For the complete Einstein metric selected by the Ważewski argument, both chiral Weyl operators have simple spectrum at \(t=0.5\). Hence no conformal multiple is Kähler near that orbit in either orientation; by real analyticity, no nonempty open subset of the manifold is conformally Kähler in either orientation.

In summary, Theorem E’s complete Einstein filling and its nonstandard Rossi CR infinity are established by the analytic and validated-flow package. The exact bolt calculation establishes non-Kählerness of the Einstein metric itself. The new off-bolt spectra give compelling evidence for the stronger non-conformally-Kähler result, and the Derdziński multiplicity argument is mathematically appropriate; what remains is a uniform interval enclosure of the two Weyl discriminants for all \(d\in I\) at one interior radius.