# Step 72: weighted shear budget for graph-neck matching

Session: S0910A01.  Agent3 / Actuator.  Execute.

## 1. Purpose

The graph-manifold route has two attractive but still unjoined pieces: strong
Einstein nonexistence information for certain graph-type four-manifolds, and
local/neck constructions that might create metrics with small negative Einstein
defect.  A03's recent reflection-core identity is useful, but it must be read
with the shear term present.  The identity does not by itself prove convergence
to a cusp; it gives a weighted balance that any proposed reflection-to-cusp
neck must satisfy pointwise along each normal trajectory.

This step turns that balance into a reproducible numerical measurement and
uses it to read A03-style low-mode boundary-value runs together with the full
Ricci residual, not just the spatial Einstein block.

Files:

- script: `Sessions/S0910A01/workspace/scripts/step72_graph_neck_shear_budget.py`
- data: `Sessions/S0910A01/workspace/data/step72_graph_neck_shear_budget.json`
- A03 source note: `Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md`

## 2. Normal identity with the correct sign

For a Gaussian metric
\[
 g=dt^2+h_t
\]
on a torus collar, let \(S\) be the shape operator of \(h_t\),
\(H=\operatorname{tr}S\),
\[
 B=S-I,\qquad b=H-3,
\]
and set \(E=\operatorname{Ric}+3g\).  The normal-normal equation gives
\[
 b' + 2b + |B|^2 = -E_{00}.
\]
Multiplying by \(e^{2t}\) and integrating from \(0\) to \(R\),
\[
 e^{2R}b(R)-b(0)+\int_0^R e^{2t}|B|^2\,dt
 =-\int_0^R e^{2t}E_{00}\,dt. \tag{2.1}
\]
Thus for a reflection-center to cusp-end match,
\[
 S(0)=0,
 \qquad H(R)=3,
\]
one has \(b(0)=-3\), \(b(R)=0\), and therefore
\[
 3+\int_0^R e^{2t}|S-I|^2\,dt
 =-\int_0^R e^{2t}E_{00}\,dt. \tag{2.2}
\]
If \(|E_{00}|\le\delta\) pointwise, then necessarily
\[
 \delta\ge
 {2\left(3+\int_0^R e^{2t}|S-I|^2\,dt\right)
  \over e^{2R}-1}. \tag{2.3}
\]
The left side of (2.3) is a weighted normal-equation cost.  It is only a
necessary measurement: small value in (2.3) does not produce an Einstein neck,
because the tangential equations, the mixed constraint, gauge, topology, and
boundary compatibility still have to be solved in maximum norm.

A03's earlier phrasing that exact reflection cores approach the cusp
exponentially is therefore too strong.  From (2.1) with \(E_{00}=0\), one only
gets
\[
 3-H(t)=e^{-2t}\left(3+\int_0^t e^{2s}|B(s)|^2\,ds\right),
\]
so \(H<3\) and a lower bound on \(3-H\).  The accumulated shear can prevent
\(H\) from approaching \(3\).

## 3. Reproducible measurement

The script implements three families of profiles.

1. **Normal-equation tanh profile.**  This has \(S=u(t)I\),
\(u=\tanh t\), and \(E_{00}=0\).  It satisfies the normal equation exactly but
has \(H(R)<3\) at every finite \(R\).  Hence it is not a finite-end cusp match.
The quantity (2.3), interpreted as the residual needed to force the endpoint
from \(H(R)<3\) to \(H(R)=3\), decays exponentially: about \(2.20\times10^{-1}\)
at \(R=2\), \(4.03\times10^{-3}\) at \(R=4\), and \(1.35\times10^{-6}\) at
\(R=8\).  The actual normal balance for the unforced endpoint is zero to
quadrature accuracy.

2. **Tanh with a final endpoint patch.**  This keeps the normal profile close
to \(\tanh t\) and adds a compact final correction so that \(H(R)=3\).  This
shows that the scalar weighted normal balance alone does not forbid small
finite-end matching: for fixed patch length, the measured maximum \(|E_{00}|\)
decays with \(R\): for patch length \(L=1\), about \(2.97\times10^{-1}\) at
\(R=2\), \(5.69\times10^{-3}\) at \(R=4\), and \(1.91\times10^{-6}\) at
\(R=8\).  This is an important negative result against an oversimplified
no-go argument: the weighted shear term does not by itself block
\(\delta\to0\) if the shape operator has already become exponentially close to
\(I\) before the final boundary adjustment.

3. **Late transition profiles.**  Profiles that keep \(S\) near zero for most
of the neck and move to \(I\) only in a final interval of fixed length retain
an order-one value of (2.3) as \(R\) grows: for final transition lengths
\(L=0.5,1,2\), the normalized costs are approximately \(1.63,0.914,0.321\)
at \(R=8\), nearly the same as at \(R=12\).  A long neck is therefore not enough
unless the terminal shear has already been driven down over a long enough
region.  Generic whole-neck interpolation can make the weighted average small,
but its pointwise \(|E_{00}|\) remains about \(3\), so it cannot satisfy
operator-norm pinching.

These one-dimensional profiles are not geometric constructions; they isolate
what the normal identity can and cannot prove.

## 4. Reading the A03-style spatial BVP samples

The script also reran A03's low-mode diagonal \(T^2\)-invariant Dirichlet
boundary-value formulation, but measured all displayed Ricci-defect components
from the symbolic formulas in
`Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json`.

The runs solve only the spatial/tangential evolution block.  Once the projected
shape variables are used consistently, the low-mode samples have the following
maximum residuals:

| case | solver status | full component sup | main residuals |
|---|---:|---:|---|
| \(R=0.5\), anisotropic expand | converged | \(3.17\times10^1\) | \(E_{00}=31.7\), \(E_{01}=6.44\) |
| \(R=1.0\), anisotropic expand | converged | \(2.33\times10^1\) | \(E_{00}=23.3\), \(E_{01}=5.28\) |
| \(R=1.0\), round cusp target | converged | \(5.39\times10^3\) | \(E_{00}=5393\), tangential components large |

The spatial solver's convergence is therefore not evidence for an approximate
Einstein neck.  In these samples the full residual is dominated by the normal
and mixed equations, and the center data are not reflection-compatible
(
\(S(0)\ne0\)
).  This is useful because it prevents the graph route from being advanced by
a local stand-in that does not meet the pointwise Ricci pinching requirement.

## 5. Consequences for the graph route

The graph route remains open but more sharply specified.

- The reflection identity supplies an exact necessary balance, not a proof that
long exact cores approach a cusp.  The accumulated weighted shear must be
measured or controlled.
- The normal equation alone is not a no-go: a profile that becomes exponentially
close to \(S=I\) before the end can be patched with exponentially small
normal residual.
- Late finite transition is bad: fixed-length end matching after a mostly
geodesic core carries order-one normalized shear cost.
- Whole-neck interpolation can hide cost in an average but fails the pointwise
operator-norm residual.
- The current low-mode spatial Dirichlet solver does not solve the full
Einstein boundary problem; the next computation must include gauge-fixed full
residual equations and boundary data compatible with reflection parity and the
constraint equations.

Thus the useful next execution target is not to make the neck longer in the
same stand-in model, but to solve or linearize the full constraint-compatible
elliptic boundary-value problem while recording two quantities at every step:
\[
 \|\operatorname{Ric}+3g\|_{\mathrm{op},\infty}
 \quad\text{and}\quad
 {2\left(3+\int_0^R e^{2t}|S-I|^2dt\right)\over e^{2R}-1}
\]
for reflection-to-cusp data.  If the first can be made small while the second
has the required matching sign and scale, the graph construction becomes a
serious negative-branch candidate.  If the linearized full problem has an
unremovable normal/mixed obstruction or the shear cost cannot be made small
under constraint-compatible data, the graph route loses its present appeal.

## 6. Step 71 repair verification

Before turning to this graph computation I ran the Step 71 repair verifier:

```
python Sessions/S0910A01/workspace/scripts/step71_regression_repairs_verify.py
```

It passed 18/18 and wrote
`Sessions/S0910A01/workspace/data/step71_regression_repairs_verify.json`.
After updating the selected-support verifier to match the Step 71 Noether
repair, I reran

```
python Sessions/S0910A01/workspace/scripts/step70_support_lemma_verify.py
python Sessions/S0910A01/workspace/scripts/step68_assembly_verify.py
```

The selected-support script now passes 33/33 and the IL assembly still passes
30/30.  These script checks are structural rather than independent proof of the
analytic estimates, but they confirm that the bounded Step 71 repairs have been
absorbed in the local files.
