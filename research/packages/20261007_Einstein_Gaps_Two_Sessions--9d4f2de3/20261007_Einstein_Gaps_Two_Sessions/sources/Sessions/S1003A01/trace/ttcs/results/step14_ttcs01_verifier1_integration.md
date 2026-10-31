# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step14_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step14_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently examine the Step-14 mathematical synthesis. Check especially: (i) the frozen-core cluster saving inequality and its interpretation at overlap depth w=1.6; (ii) whether the exact one-dimensional minimization for A_T(q)=∫_0^T e^{4t}(q''+4q')^2 with clamped endpoint data really tends to 64 Delta^2; (iii) whether that reduced result justifies only a conditional route to diagonal coercivity rather than a lower bound for the full cell problem; and (iv) what the new rigorous X=32 and X=64 cell enclosures establish. Identify any mathematical or interpretive correction that should be made, and state the strongest sound implication for the Einstein-gap programme.

## Integrated Scientific Memo

# Step‑14 verification memo

## 1. Frozen-core cluster budget

Let the protected cores \(C_i\) be pairwise disjoint and suppose the cluster metric agrees with the isolated cell metric \(g_i\) on \(C_i\). Since the defect density is nonnegative,
\[
J_6(g_{\rm cl})
\ge \sum_i J_6(g_i;C_i),
\]
hence
\[
\boxed{\;
\sum_iJ_6(g_i)-J_6(g_{\rm cl})
\le
\sum_iJ_6(g_i;M_i\setminus C_i).
\;}
\]
The same argument applies to \(P=\int|\operatorname{Ric}^{\circ}|^2\). Thus each adjustable exterior contributes to the global saving budget only once; independently optimized pair savings cannot simply be summed over all edges. At quadratic order this is the positivity of the single Gram form
\[
\Bigl\|\sum_i Ah_i\Bigr\|_{L^2}^2\ge0,
\]
not a collection of independent pairwise inequalities.

### Interpretation at \(w=1.6\)

For the \(X=8\) witness,
\[
r_{\rm cut}=\rho-w
=1.762747174039086-1.6
=0.162747174039086.
\]
The exterior-budget file gives
\[
\frac{J_6(r>r_{\rm cut})}{8\pi^2}
=0.1510633950729049.
\]
Thus for a pair, the frozen-core inequality allows as much as
\[
\frac{2J_{\rm cell}-J_{\rm pair}}{8\pi^2}
\le 2(0.1510633951)=0.3021267901.
\]
The measured pair saving \(1.25\times10^{-5}\) is only about \(4.1\times10^{-5}\) of this ceiling. Therefore:

* the per-cell accounting principle is exact;
* at \(w=1.6\), however, it is quantitatively far too weak to constrain ordinary finite-coordination packing;
* it prevents unrestricted edge-by-edge multiplication, but does **not** show that several pair savings cannot coexist in a realistic cluster.

The \(r>1\) budget,
\[
J_6(r>1)/(8\pi^2)=1.98972\times10^{-4},
\]
cannot be applied to the \(w=1.6\) witness: that construction guarantees only that \(r<0.16275\) is frozen. It becomes relevant only for a separately constructed cluster that preserves \(r<1\).

A precision caveat is also needed. The inequality is exact, but these exterior numbers are grid quadratures; the file reports a total grid-versus-record discrepancy \(2.21\times10^{-7}\). Likewise, the very small \(X=16\) pair savings at \(w=1.2,1.4\) have no supplied rigorous error enclosure. The \(w=1.6\) effects are larger, but all pair signs remain numerical rather than certified.

---

## 2. Exact weighted one-dimensional minimum

Consider
\[
\mathcal A_T(q)=\int_0^T e^{4t}(q''+4q')^2\,dt,
\qquad
q(0)=0,\quad q(T)=\Delta,\quad q'(0)=q'(T)=0.
\]
Set \(v=q'\), \(f=v'+4v\), and \(\varepsilon=e^{-4T}\). The Euler–Lagrange equations yield
\[
f(t)=C+\frac{\mu}{4}e^{-4t},
\]
and hence
\[
v(t)=\frac C4(1-e^{-4t})+\frac{\mu}{4}t e^{-4t}.
\]
The condition \(v(T)=0\) gives
\[
C=-\frac{\mu T\varepsilon}{1-\varepsilon}.
\]
The displacement condition \(\int_0^T v=\Delta\) gives
\[
\Delta=\mu D_T,
\qquad
D_T=
\frac{1-e^{-4T}}{64}
-\frac{T^2e^{-4T}}{4(1-e^{-4T})}.
\]
For the critical point,
\[
\mathcal A_T^{\min}=\mu\Delta,
\]
so
\[
\boxed{\;
\mathcal A_T^{\min}
=
\frac{\Delta^2}{
\displaystyle
\frac{1-e^{-4T}}{64}
-\frac{T^2e^{-4T}}{4(1-e^{-4T})}}
\longrightarrow 64\Delta^2.
\;}
\]
For \(\Delta=\log(2.196)\),
\[
64\Delta^2=39.60310999103562,
\]
exactly matching the JSON. Thus the Step‑14 limit is mathematically correct.

The script field called `resistance` is
\[
\frac{\Delta^2}{\mathcal A_T^{\min}}=D_T\longrightarrow\frac1{64},
\]
so the terminology should distinguish the energetic coefficient \(64\) from the compliance/resistance factor \(1/64\) appearing in inequalities of the form
\[
|\Delta\Phi|^2\le \mathcal A\,R_\Phi.
\]

### Important interpretive correction: the controlled mismatch is not merely \(q\)

Writing
\[
\Phi=q+\frac14q',
\]
one has the exact model identity
\[
\Phi'=\frac14(q''+4q').
\]
Therefore the weighted Cauchy–Schwarz estimate controls the change of \(\Phi\), not \(q\) alone. The clamped conditions make \(\Delta\Phi=\Delta q=\Delta\), but this identification is lost if the entrance slope is free.

Indeed,
\[
q(t)=\Delta(1-e^{-4t})
\]
moves from \(0\) to \(\Delta\) at zero action because \(q''+4q'=0\), while \(q'(0)=4\Delta\). Consequently, the positive limit \(64\Delta^2\) requires:

1. exponential ACH weighting with a fixed normalization at the tube entrance;
2. a nonzero change in the flux-corrected variable \(\Phi\);
3. control of the entrance and exit slopes.

Thus “lengthening a noncollapsed ACH transition does not erase resistance” is correct only under these boundary/flux conditions. The minimizer concentrates the forcing near the low-weight entrance; it does not distribute the mismatch uniformly along a long collar.

For comparison, the unweighted problem has exact minimum
\[
\mathcal A^{(0)}_T
=
\frac{16\Delta^2}{T-\frac12\tanh(2T)}
\sim \frac{16\Delta^2}{T},
\]
so its cost does tend to zero.

---

## 3. Consequence for diagonal coercivity: conditional only

The reduced calculation is not a lower bound for the full cell problem. For a diagonal Bianchi IX metric, put
\[
W=a_1a_2a_3,\qquad q=\log(a_2/a_3).
\]
Subtracting the exact \(22\) and \(33\) Ricci equations gives
\[
\boxed{\;
(Wq')'=W(V-E),
\;}
\]
where
\[
E=(\operatorname{Ric}^{\circ})_{22}
-(\operatorname{Ric}^{\circ})_{33},
\]
and
\[
V=
\operatorname{Pot}_2-\operatorname{Pot}_3
=
\frac{4(a_2^2-a_3^2)(a_2^2+a_3^2-a_1^2)}{W^2}.
\]
The model \(q''+4q'=f\) is recovered only after replacing \(W'/W\) by \(4\) and neglecting \(V\).

Since the trace-free Ricci tensor is diagonal,
\[
|\operatorname{Ric}^{\circ}|^2\ge \frac12E^2.
\]
Thus a genuine diagonal calibration is available, but it contains the actual volume \(W\), the potential \(V\), and boundary flux. For example, let
\[
G(t)=\int_t^\infty W(s)^{-1}\,ds,
\qquad
\Phi_G=q+GWq'.
\]
Then
\[
\Phi_G'=GW(V-E),
\]
and Cauchy–Schwarz gives
\[
\left|
\Phi_G(t_1)+
\int_{t_1}^{\infty}GWV\,dt
\right|^2
\le
\left(\int_{t_1}^{\infty}E^2W\,dt\right)
\left(\int_{t_1}^{\infty}G^2W\,dt\right),
\]
assuming the exact-CH outer collar makes the terminal flux vanish. This is the correct nonlinear form of the proposed resistance mechanism.

To deduce a positive diagonal cell lower bound, one still needs uniform control of:

* entrance into a noncollapsed ACH regime;
* the volume normalization, equivalently an upper bound for
  \(\int G^2W\);
* the potential contribution \(\int GWV\);
* the flux-corrected mismatch \(\Phi_G\), including entrance slope;
* rigorous Rossi separation from \(\rho=1\) over the entire Einstein filling family;
* degenerating bolt parameters and competitors that leave the ACH tube.

The supplied \(\rho_{\min}\simeq2.196\) is numerical shooting evidence, not a rigorous endpoint separation. Moreover, most of the current cell energy lies in the inner/core region: for the \(X=8\) example roughly \(85\%\) already lies inside \(r<0.163\), while only about \(2\times10^{-4}\) lies beyond \(r=1\). Hence the simple asymptotic tube model can at most control residual mismatch transported through the outer end; the main coercive problem is an inner nonlinear one.

Accordingly, Step 14 supplies a plausible and partially exact **conditional route** to positivity in the diagonal class. It proves neither
\[
\mathfrak P_{1,0}>0,\qquad
\mathfrak J_{1,0}>0,
\]
nor any lower bound for nonsymmetric or non-diagonal competitors.

---

## 4. What the \(X=32\) and \(X=64\) Arb enclosures establish

The rigorous normalized intervals are
\[
\begin{array}{c|cc}
X&
J_6/(8\pi^2)&P/(8\pi^2)\\ \hline
32&
[0.9987367698625724,\ 0.9987367698714824]&
[0.9987321473767184,\ 0.9987321473883820]\\[1mm]
64&
[0.9987027644738578,\ 0.9987027644835269]&
[0.9987000858929286,\ 0.9987000859072952].
\end{array}
\]
Therefore the \(X=64\) explicit profile gives the rigorous upper bounds
\[
\boxed{\;
\frac{\mathfrak J_{1,0}}{8\pi^2}
\le0.9987027644835269,
\qquad
\frac{\mathfrak P_{1,0}}{8\pi^2}
\le0.9987000859072952,
\;}
\]
provided the profile ansatz indeed supplies the stated smooth, positive, exact-collar admissible metric. Equivalently,
\[
1-\frac{J_6}{8\pi^2}\ge0.0012972355164731,
\qquad
1-\frac{P}{8\pi^2}\ge0.0012999140927048.
\]

The intervals are disjoint, so the fixed \(X=64\) witness is rigorously better than the fixed \(X=32\) witness. For \(J_6/(8\pi^2)\), the certified improvement is at least
\[
0.9987367698625724-0.9987027644835269
=3.4005379\times10^{-5}.
\]

These enclosures certify the integrals of two explicit profiles. They do **not** certify:

* convergence as \(X\to\infty\);
* saturation near \(0.9987\);
* existence of a complete finite-energy limiting metric;
* optimality within the finite-dimensional ansatz;
* attainment or a positive lower bound for the cell infimum.

The \(X=64\) optimizer’s gradient norm \(3.2\times10^{-3}\) makes any claim of numerical saturation especially premature. The ordinary floating-point records lie outside the narrow Arb balls at their final digits, so only the Arb intervals should be quoted as rigorous values.

## Strongest sound implication for the Einstein-gap programme

Step 14 establishes two complementary but one-sided facts:

1. **Constructive upper bound:** an explicit admissible diagonal cell has rigorously enclosed cost
   \[
   J_6<0.998703\,(8\pi^2),\qquad
   P<0.998701\,(8\pi^2),
   \]
   strictly improving the \(X=32\) witness.

2. **Conditional obstruction to vanishing cost:** in a uniformly normalized, noncollapsed ACH tube, a clamped change of the flux-corrected Rossi mode has a finite positive weighted cost; the exact model coefficient is \(64\), or compliance \(1/64\).

The central unresolved object is a uniform nonlinear calibration/compactness theorem connecting the inner bolt geometry to a nonzero flux-corrected Rossi mismatch at a controlled ACH entrance. Until that is proved—and the numerical Rossi separation is rigorously enclosed—the work gives no positive lower Einstein gap, even in the full diagonal cell problem, and still less for all four-manifold metrics.