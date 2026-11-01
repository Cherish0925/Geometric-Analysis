# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 74,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step74_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step74_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the new Step-74 theorem and numerical normalization. Check: (i) the relative Chern–Weil coefficient and subtraction of the missing CH core 3 x0^2; (ii) the interval outputs for both certified cells; (iii) the mixed closed-manifold implication d >= 4π²(A/3-k+eta n) and its cover/packing quantifiers; (iv) the CH Ric=-g ball-volume formula and the resulting beta0 and footprint efficiencies; (v) the fixed-complex Kähler Hodge-index comparison and its relation to the h=1/3 frontier; (vi) the algebraic capacity equivalence alpha<1 iff kappa>(3k-A)/4. Identify any normalization, sign, topology, or quantifier error and give corrected formulas. Also check that the added Fino construction is represented at exactly its proved scope (complete noncompact R4, not closed Goldberg).

## Integrated Scientific Memo

# Step-74 verification and corrected theorem

The relative Chern–Weil calculation and the resulting mixed Weyl-deficit improvement are correct. The substantive corrections concern the Kähler threshold, exceptional-class signs, cover notation, smoothing/support quantifiers, and the footprint fields in both JSON files. The Fino construction is represented at its proved noncompact scope.

Throughout, write
\[
I_\pm(g)=\int_M|W^\pm_g|_{\rm op}^2,\qquad
d([g])=8\pi^2\chi(M)-I_+(g)-I_-(g),
\]
and
\[
d_*(M)=\sup_{[g]}d([g]).
\]
The operator norm is the one fixed in the supplied sources:
\[
4\pi^2(2\chi+3\tau)=\frac{S}{24}+2I_+-\frac P2.
\]

## 1. Relative coefficient, topology, and missing core

Solving the chiral Chern–Weil identity for \(P\) gives
\[
\frac{P}{8\pi^2}
=\frac{S}{96\pi^2}+\frac{I_+}{2\pi^2}-(2\chi+3\tau).
\]
A reversed-\(\mathbb{CP}^2\) insertion changes \(\chi\) by \(+1\), \(\tau\) by \(-1\), and therefore \(2\chi+3\tau\) by \(-1\). Exact agreement on the outer CH collar cancels the relative boundary transgression terms. Consequently
\[
\boxed{p-1=\frac{\Delta I_+}{2\pi^2}+\frac{\Delta S}{96\pi^2}.}
\]
Thus (74.1) has the correct coefficient and sign.

In the \(\operatorname{Ric}=-6g\) normalization,
\[
s=-24,\qquad dV=\pi^2x\,dx.
\]
Hence
\[
\frac1{96\pi^2}\int_0^{x_0}s^2\,dV
=\frac{576}{96}\int_0^{x_0}x\,dx
=3x_0^2.
\]
The correct total relative scalar integral is therefore
\[
\boxed{\mathrm{ds96}_{\rm total}
=\mathrm{ds96}_{\rm shell}-3x_0^2.}
\]
The script makes this subtraction correctly, including the factor \(1/12\) converting its \(dV/(8\pi^2)\) density to \(S/(96\pi^2)\).

A useful independent check uses Gauss–Bonnet:
\[
d=\frac S{24}-\frac P2.
\]
Putting
\[
\eta=1-p+\mathrm{ds96}_{\rm total}
=-\frac{\Delta I_+}{2\pi^2}
\]
gives
\[
\boxed{\Delta d
=4\pi^2(\mathrm{ds96}_{\rm total}-p)
=-4\pi^2(1-\eta).}
\]
This agrees with the signature-based calculation.

## 2. Both cell outputs: arithmetic verified, one field incorrect

The supplied shell and \(p\) enclosures propagate consistently through
\[
\Delta I_+/(2\pi^2)=p-1-\mathrm{ds96}_{\rm total}.
\]
For clarity, the following shorter intervals have outward-rounded endpoints:

| Cell | \(\mathrm{ds96}_{\rm total}\) | \(\eta=-\Delta I_+/(2\pi^2)\) |
|---|---|---|
| \(x_0=.03,\ X=128\) | \([0.07079693356934066313,\ 0.07079693356934076916]\) | \([0.07513420079822646344,\ 0.07513420081608643992]\) |
| \(x_0=.01,\ X=8\) | \([0.02130328060295686251,\ 0.02130328060295687028]\) | \([0.02219457786936421405,\ 0.02219457786936422273]\) |

The formal all-cell values are also consistent:
\[
\begin{aligned}
X=128:\quad &[0.36041264972823538179,\ 0.36041264973519537504],\\
X=8:\quad &[0.34089945278376628329,\ 0.34089945278376628633].
\end{aligned}
\]

Some shortened intervals in the note are rounded-to-nearest rather than outward: for example, the printed upper endpoint in (74.5) is slightly below the JSON upper endpoint, and the lower endpoint in (74.8) is slightly above the JSON lower endpoint. These are harmless approximations only if marked as such; certified inequalities should use exact dyadics or genuinely outward decimal endpoints.

**Verification scope.** The bounded input permits verification of normalization and interval post-processing, not a fresh quadrature certification. The imported `FrozenCell`, frozen profiles, and original quadrature certificates are not reproduced here.

**Artifact inconsistency.** In both JSON files,
`packing.eta_per_host_Wplus_footprint` equals \(\eta/X^2\), although the recorded footprint is \(3X^2\). It is therefore too large by a factor of three. The visible script computes the correct expression \(\eta/(3X^2)\); the stored outputs do not correspond to that expression.

The slightly different \(X=128\) \(p\)-endpoints quoted in Step 69 and the supplied Step-74 JSON differ only at approximately \(10^{-20}\), with the Step-74 hull slightly enlarged. This does not affect the conclusions, but the original certificate endpoint and the subsequently enlarged hull should not be called the same exact endpoint.

## 3. Correct mixed closed-manifold theorem

Let the original ball quotient be \(X_0\). Choose a preliminary finite cover \(X'\to X_0\) with sufficiently large **global** injectivity radius. For a further finite cover \(Y\to X'\), set
\[
A_Y=c_1^2(Y)=\deg(Y\to X_0)c_1^2(X_0).
\]
Suppose \(Y\) contains \(N\) disjoint CH balls accommodating the entire smoothed cell, including its collar. For integers
\[
k\ge0,\qquad 0\le n\le\min\{k,N\},
\]
the construction gives
\[
\boxed{
d_*\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)
\ge4\pi^2\left(\frac{A_Y}{3}-k+\eta n\right).
}
\]
Here \(\eta\) is any strict certified lower bound for the cell saving.

Indeed, the CH host has \(d=4\pi^2A_Y/3\); each special insertion changes \(d\) by \(-4\pi^2(1-\eta)\); each ordinary reversed-\(\mathbb{CP}^2\) insertion costs \(4\pi^2\) in the limiting conformal connected-sum construction. Ordinary insertions can use arbitrarily small balls in the remaining open region and need not consume additional full-radius packing sites.

Thus
\[
\boxed{k<\frac{A_Y}{3}+\eta n\quad\Longrightarrow\quad\alpha(M)<1.}
\]
A positive lower bound for \(d_*\) supplies an actual positive-deficit class: choose the smoothing/gluing errors below the strict positive margin. Step 72 then supplies a subunit Yamabe representative.

The original definition \(A=c_1^2(X_0)\) must therefore be changed throughout the further-cover formulas. Merely retaining the base \(A\) gives a weaker numerical expression but does not describe the host contribution or normalized frontier correctly.

### Cover and smoothing quantifiers

The global preliminary-cover argument is the repaired one in Step 69: for a compact fundamental set \(F\), let
\[
D=\sup_{x\in F}d(x_0,x),
\]
exclude all nonidentity elements with
\[
d(x_0,\gamma x_0)\le4R_s+2D,
\]
and choose a normal finite-index subgroup avoiding them. This ensures global injectivity radius \(>2R_s\), inherited by every further cover. Excluding short displacement at one base point alone is insufficient.

Here \(R_s\) must be the **smoothed support radius**, not automatically the raw coordinate radius
\[
R(X)=\sqrt6\,\operatorname{arsinh}\sqrt X.
\]
Moreover, convergence of \(P\) alone does not preserve the Weyl-saving certificate: the smoothing must preserve \(\Delta S\) as well. A shrinking-annulus \(C^2\)-controlled smoothing provides this; alternatively, the inherited \(J_6\)-controlled smoothing must be invoked with the necessary scalar-integral convergence. The Step-69 statement \(p\le p_c+\delta\) alone is insufficient for this transfer.

If the inherited smoothing can be performed with
\[
R_s\downarrow R(X),\qquad \eta_s\to\eta,
\]
then every strict packing endpoint below is recovered by choosing the smoothing sufficiently fine. If instead one only uses Step 69’s explicitly padded radius \(R(X)+1\), the packing coefficient must be evaluated at that larger radius. The bounded input does not reproduce the smoothing proof establishing arbitrarily small support enlargement; that is the precise dependency behind the raw-radius numerical endpoints.

Once the appropriate preliminary cover is chosen, the inequality holds for **every further cover** and every admissible \(k,n\). Extra cover depth is needed only to realize integer ratios in a very narrow interval, not for the inequality itself.

## 4. CH volume, packing constants, and efficiency

Scaling \(g\) by \(6\) multiplies four-volume by \(36\), while
\[
V_{-6}(B_r)=\frac{\pi^2}{2}\sinh^4r.
\]
Therefore, at \(\operatorname{Ric}=-g\),
\[
\boxed{
V(B_R)=18\pi^2\sinh^4(R/\sqrt6)=18\pi^2X^2.
}
\]
Its small-radius leading term is \(\pi^2R^4/2\), as required.

A maximal \(2R_s\)-separated set has disjoint \(R_s\)-balls and covering \(2R_s\)-balls. Since \(V(Y)=2\pi^2A_Y\),
\[
\frac N{A_Y}\ge\frac{2\pi^2}{V(B_{2R_s})}.
\]
At the raw coordinate radius,
\[
X(2R)=4X(1+X),\qquad
\boxed{\beta_0(X)=\frac1{9[4X(1+X)]^2}.}
\]
Numerically,
\[
\begin{array}{c|c|c}
X&\beta_0(X)&1/3+\eta\beta_0(X)\\ \hline
8&1/746496&0.33333336306501022023455\ldots\\
128&1/39261044736&0.33333333333524704198024\ldots
\end{array}
\]
The quoted packing arithmetic is correct, subject to the support-radius dependency above.

Choosing \(n=\min\{k,N\}\) gives the exact normalized sufficient condition
\[
\frac13-h+\eta\min\left\{h,\frac N{A_Y}\right\}>0,
\qquad h=\frac{k}{A_Y}.
\]
For these cells, \(h<1/3+\eta\beta_0\) implies this condition: if \(k<N\), the expression is \(1/3-(1-\eta)h>0\); if \(k\ge N\), use \(N/A_Y\ge\beta_0\).

### Two distinct efficiency normalizations

At \(\operatorname{Ric}=-g\), CH has \(|W^+|_{\rm op}^2=2/3\), so
\[
\frac{I_+(B_R)}{4\pi^2}=3X^2.
\]
The note’s **deficit-saving per footprint** is
\[
\frac{\eta}{3X^2},
\]
approximately
\[
X=8:\ 1.15596759736\times10^{-4},
\qquad
X=128:\ 1.52860922848\times10^{-6}.
\]
These are the corrected JSON values. Their ratio is approximately \(75.6222\).

But the actual self-dual Weyl energy removed is \(2\pi^2\eta\), not \(4\pi^2\eta\). Its fraction of the ball’s Weyl energy is
\[
\boxed{\frac{-\Delta I_+}{I_+(B_R)}=\frac{\eta}{6X^2}.}
\]
Thus the note’s phrase “self-dual-Weyl removal per footprint” is off by a factor of two if interpreted literally.

There is also a stronger limitation on the all-cell numbers. Disjoint ball placement requires
\[
NV(B_R)\le V(Y),\qquad \frac N{A_Y}\le\frac1{9X^2}.
\]
If \(n=k\), then \(h\le1/(9X^2)\), far below \(1/3\) for either cell. Hence the formal all-cell frontiers \(0.340899\ldots\) and \(0.360413\ldots\) are **unattainable by disjoint placement of these fixed-radius cells**, not merely uncertified. They remain algebraic benchmarks for a different, potentially interacting construction.

## 5. Fixed-complex Kähler comparison and the \(h=1/3\) frontier

With \(H=\pi^*K_Y\) and \(E_i\) the effective exceptional divisor classes,
\[
K_M=H+\sum_iE_i,\qquad
\boxed{c_1(M)=-H-\sum_iE_i.}
\]
The sign in Step 74 is wrong. In fact, the numerator displayed there already implicitly uses the corrected sign.

Nor is every Kähler class proportional to \(H\) on the base. Write generally
\[
[\omega]=\pi^*a-\sum_i e_iE_i,\qquad e_i=[\omega]\cdot E_i>0,
\]
and put \(q=K_Y\cdot a>0\), \(E=\sum_i e_i\). The Hodge index theorem gives
\[
q^2\ge A_Ya^2.
\]
Therefore
\[
\frac{(c_1(M)\cdot[\omega])^2}{[\omega]^2}
=\frac{(q+E)^2}{a^2-\sum_i e_i^2}\ge A_Y,
\]
since the difference between numerator and \(A_Y\) times denominator is
\[
(q^2-A_Ya^2)+2qE+E^2+A_Y\sum_i e_i^2\ge0.
\]
Using \(\int s\,dV=4\pi c_1\cdot[\omega]\), \(V=[\omega]^2/2\), and Cauchy–Schwarz gives
\[
\boxed{
I_+=\frac S{24}
\ge\frac{4\pi^2}{3}
\frac{(c_1\cdot[\omega])^2}{[\omega]^2}
\ge\frac{4\pi^2A_Y}{3}.
}
\]

The correct chiral deficit identity is
\[
\boxed{d([g])=4\pi^2(A_Y-k)-2I_+(g).}
\]
Thus
\[
\boxed{d([g])>0\iff I_+(g)<2\pi^2(A_Y-k).}
\]
Equation (74.19a) is incorrect. It is not a norm conversion: \(2\pi^2(A_Y-k)\) and \(4\pi^2A_Y/3-4\pi^2k\) are not constant multiples. In the corresponding tensor norm, the valid threshold is \(8\pi^2(A_Y-k)\).

For Kähler metrics on this fixed blow-up complex surface,
\[
d([g])\le4\pi^2(A_Y/3-k).
\]
Consequently no such Kähler metric has positive deficit for \(k\ge A_Y/3\). Conversely, the fixed-complex Kähler infimum \(P_*=8\pi^2k\) inherited in Step 69, together with the Kähler Chern–Weil identity, yields \(I_{+,*}=4\pi^2A_Y/3\); hence positive deficit is achievable in this Kähler family for \(k<A_Y/3\).

So \(h=1/3\) is exactly the frontier **for the fixed blow-up complex structure**. This calculation does not exclude Kähler metrics for unrelated complex structures on the same smooth manifold.

## 6. Capacity equivalence: correct algebra, existential quantifier required

At a negative Yamabe representative scaled to \(s=-4\), define explicitly
\[
p=\frac P{8\pi^2},\qquad
\upsilon=\frac V{2\pi^2}-A_Y,\qquad
\kappa=\frac{A_Y}{2}-\frac{3I_+}{8\pi^2}.
\]
Then Chern–Weil gives
\[
\boxed{p=k-\frac43\kappa+\frac13\upsilon.}
\]
At this representative,
\[
\mathcal E=\frac{4P}{P+4V},
\]
so
\[
\mathcal E<1
\iff3p<A_Y+\upsilon
\iff\boxed{\kappa>\frac{3k-A_Y}{4}}.
\]
The global statement is
\[
\boxed{
\alpha(M)<1
\iff\exists\text{ negative Yamabe representative with }
\kappa>\frac{3k-A_Y}{4}.
}
\]
Equivalently, replace \(\kappa\) by its supremum over realizable representatives. This is the old capacity variable, not the parameterized field-defect \(\kappa_\beta\) used elsewhere.

A special cell changes capacity by \(3\eta/4\), recovering precisely
\[
k<A_Y/3+\eta n.
\]
For the literal fraction \(\Theta\) of the host’s total \(I_+\)-budget removed,
\[
\kappa=\frac{A_Y}{2}\Theta,\qquad
d>0\iff h<\frac13+\frac23\Theta.
\]
This verifies the factor \(2/3\). However, (74.21) should not be treated as a computed—or automatically proved—critical frontier: realizable maximal saving generally depends on \(h\). The precise formulation is
\[
\Theta_*(h)=\sup_{\text{realizable metrics/batches at }h}\Theta,
\qquad
\alpha<1\iff\Theta_*(h)>\frac{3h-1}{2}.
\]
Turning this into a single endpoint requires information about realizability as \(h\) varies.

## 7. Fino construction: scope preserved

The supplied supplement proves a smooth complete pair on
\[
\mathbb H^2\times\mathbb R^2\cong\mathbb R^4
\]
with
\[
\operatorname{Ric}=-3g,\quad W^-=0,\quad
d\Omega=0,\quad|\Omega|^2=2,\quad
|\nabla\Omega|^2=\frac{36(1-x^2)^3}{(1+3x^2)^3}>0
\]
at every finite point, including the smoothly completed bolt. The unequal Weyl-norm values \(2/3\) at the bolt and limit \(6\) at infinity establish nonhomogeneity. “Varies from \(2/3\) to \(6\)” should not imply attainment of the latter value or monotonicity unless separately proved.

This is a complete **noncompact**, non-invariant, non-Ricci-flat strictly almost-Kähler Einstein example on the underlying additive Lie group \(\mathbb R^4\). It does not settle closed negative Goldberg.

Indeed, on a closed almost-Kähler four-manifold the torsion bundle satisfies
\[
c_2(\Lambda^{0,1}\otimes\Lambda^{0,2})[M]
=5\chi+6\tau=\chi+2(2\chi+3\tau).
\]
For negative Einstein geometry both terms on the right are positive by Chern–Weil. Thus torsion must vanish somewhere, whereas this complete pair has no finite torsion zero. The same pair cannot descend unchanged to a compact quotient. This obstruction does **not** prove that torsion vanishes identically; extension through forced zeros remains a genuine closed-manifold problem.