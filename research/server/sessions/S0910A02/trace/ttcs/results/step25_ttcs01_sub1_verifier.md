# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/scripts/step25_weighted_curvature_identity_test.py",
    "Sessions/S0910A02/workspace/data/step25_weighted_curvature_identity_test.json",
    "Sessions/S0910A02/workspace/notes/step20_global_build_break_analysis.md",
    "Sessions/S0910A02/workspace/notes/step14_faberkrahn_reduced_system_and_fork.md"
  ]
}
```

## Task

Independently check a claimed correction in a toric reduced-Einstein computation for Yau Problem 26. Context: a twist-free diagonal T^2-invariant Einstein 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a polygon), with w = pq, v = log(p/q). The verified reduced equations are: (1) -Delta_B w = 2w with w=0 on dOmega (Einstein lambda=1); the individual warping equations -Delta_B p=(K_B-1)p, -Delta_B q=(K_B-1)q, and <grad p, grad q> = -K_B w. On each rod (boundary segment) the collapsing fiber vanishes at unit slope and the surviving fiber Q(s) satisfies Q''+(1-2K_edge)Q=0 with Q'(0)=1,Q'(L)=-1, giving the exact rod identity int_rod (1-2K_edge)Q ds = 2, i.e. flux Phi_i = int Q ds = 2 + 2 int_rod K_edge Q ds.

CLAIM 1 TO CHECK: A prior note (Step 20) recorded an interior identity 'int_Omega K_B w = int_Omega w'. I now claim this clean interior identity is FALSE because the Green's-identity derivation drops boundary/corner terms. My evidence: for the exact product S^2 x S^2, Omega = [0,pi]^2 flat (K_B=0 in interior), w = sin x sin y, so int_Omega K_B w = 0 but int_Omega w = 4, a contradiction. Is my reasoning correct that the clean interior weighted-curvature identity does not hold, and that the only rigorous boundary-anchored constraints are (a) total flux = 2 int w and (b) the per-rod identity int(1-2K_edge)Q=2? Or is there a correct corner/edge-corrected version of int K_B w = int w that I am missing (e.g. with explicit corner delta-curvature terms), and if so what is it exactly?

CLAIM 2 TO CHECK: For a single rod with constant edge curvature K_edge = -A (A>0), Q = sin(sqrt(1+2A) s)/sqrt(1+2A), L = pi/sqrt(1+2A). I compute the Q-weighted negative-curvature charge G_i := int_rod (-K_edge) Q ds = int_0^L A Q ds = 2A/(2A+1), which tends to 1 as A -> infinity, and Phi_i = 2/(2A+1) = 2 - 2 G_i, tending to 0. Verify these two integrals and the relation Phi_i = 2 - 2 G_i exactly. Confirm or refute that a single constant-curvature rod can drive its flux to 0 while its Q-weighted negative charge G_i saturates at 1.

Do the exact integral algebra yourself. State whether each claim holds, and flag any sign or boundary-term error. Do not invent external literature; reason only from the stated equations.

## Output

## Scientific verification memo

### 1. The interior identity \(\int_\Omega K_Bw=\int_\Omega w\)

The identity is false. However, the contradiction comes from a reversed sign in the stated individual warping equations, not from an omitted edge or corner term.

The product example fixes the Laplacian convention:

\[
p=\sin x,\qquad q=\sin y,\qquad K_B=0,
\]

so

\[
-\Delta_Bp=p,\qquad -\Delta_Bq=q.
\]

Thus the equations compatible with the product metric are

\[
\boxed{-\Delta_Bp=(1-K_B)p,\qquad
-\Delta_Bq=(1-K_B)q,}
\]

rather than \(-\Delta_Bp=(K_B-1)p\).

This sign is also forced algebraically. If one uses the stated sign together with

\[
\langle\nabla p,\nabla q\rangle=-K_Bpq,
\]

then

\[
-\Delta_B(pq)
=(4K_B-2)pq,
\]

which is incompatible with \(-\Delta_Bw=2w\) unless \(K_B=1\). With the corrected sign,

\[
\Delta_Bp=(K_B-1)p,\qquad \Delta_Bq=(K_B-1)q,
\]

and therefore

\[
\Delta_B(pq)
=2(K_B-1)pq-2K_Bpq=-2pq,
\]

exactly as required.

### 2. Correct Green identity

Let \(\Phi_p\) denote the sum of the fluxes over all rods where \(p\) collapses. Green’s formula gives

\[
\int_\Omega q(-\Delta_Bp)\,dA
=
\int_\Omega\langle\nabla p,\nabla q\rangle\,dA
-\int_{\partial\Omega}q\,\partial_\nu p\,ds.
\]

On a \(p\)-rod, \(\partial_\nu p=-1\), so \(q\,\partial_\nu p=-Q\); on a \(q\)-rod, \(q=0\). Hence

\[
\int_{\partial\Omega}q\,\partial_\nu p\,ds=-\Phi_p.
\]

Using the corrected equation,

\[
\int_\Omega(1-K_B)w\,dA
=
-\int_\Omega K_Bw\,dA+\Phi_p,
\]

and the curvature terms cancel:

\[
\boxed{\Phi_p=\int_\Omega w\,dA.}
\]

Similarly,

\[
\boxed{\Phi_q=\int_\Omega w\,dA.}
\]

Consequently,

\[
\boxed{\sum_i\Phi_i=\Phi_p+\Phi_q=2\int_\Omega w\,dA.}
\]

If the reversed equation \(-\Delta p=(K_B-1)p\) is inserted instead, one obtains

\[
\Phi_p=2\int_\Omega K_Bw\,dA-\int_\Omega w\,dA,
\]

and combining this with total flux produces the spurious identity
\(\int K_Bw=\int w\).

### 3. Corner terms do not repair that identity

For smooth toric closure, near a corner one has the local behavior \(p=O(r_1)\), \(q=O(r_2)\), with bounded first derivatives. After removing a small arc of radius \(\varepsilon\),

\[
q\,\partial_\nu p\,ds=O(\varepsilon)\,O(1)\,O(\varepsilon)
=O(\varepsilon^2),
\]

so its integral vanishes as \(\varepsilon\to0\). Thus Green’s formula acquires no corner residue.

Likewise, if right-angle corner contributions from Gauss–Bonnet are represented as atomic curvature measures, their \(w\)-weighted contribution is zero because \(w=0\) at every corner. Edge-supported curvature measures are also annihilated by \(w=0\) along every rod. Hence they cannot change the flat-square value

\[
\int_\Omega K_Bw\,dA=0
\]

into \(\int_\Omega w\,dA=4\).

There is therefore no corner-corrected version of the proposed interior identity arising from the stated equations. The exact replacements are:

\[
\Phi_p=\Phi_q=\int_\Omega w\,dA,
\]

\[
\sum_i\Phi_i=2\int_\Omega w\,dA,
\]

and

\[
\Phi_i=2+2\int_{\mathrm{rod}_i}K_{\rm edge}Q_i\,ds.
\]

Summing the rod identities also gives the useful edge formula

\[
\boxed{
\int_\Omega w\,dA
=
m+\sum_{i=1}^m\int_{\mathrm{rod}_i}K_{\rm edge}Q_i\,ds.
}
\]

For \(S^2\times S^2\), \(m=4\), \(K_{\rm edge}=0\), and this reads \(\int w=4\), exactly.

---

### 4. Constant-curvature rod calculation

Set

\[
K_{\rm edge}=-A,\qquad
\omega=\sqrt{1+2A},\qquad
L=\frac{\pi}{\omega},
\]

and

\[
Q(s)=\frac{\sin(\omega s)}{\omega}.
\]

Then \(Q'(s)=\cos(\omega s)\), so \(Q'(0)=1\) and \(Q'(L)=-1\). The flux is

\[
\begin{aligned}
\Phi_i
&=\int_0^{\pi/\omega}\frac{\sin(\omega s)}{\omega}\,ds\\
&=\frac1{\omega^2}\int_0^\pi\sin t\,dt\\
&=\frac{2}{\omega^2}
=\boxed{\frac{2}{1+2A}}.
\end{aligned}
\]

Since \(A\) is constant,

\[
\begin{aligned}
G_i
&=\int_0^L A Q(s)\,ds\\
&=A\Phi_i\\
&=\boxed{\frac{2A}{1+2A}}.
\end{aligned}
\]

Therefore

\[
\Phi_i+2G_i
=
\frac{2+4A}{1+2A}=2,
\]

or equivalently,

\[
\boxed{\Phi_i=2-2G_i.}
\]

Moreover,

\[
\lim_{A\to\infty}\Phi_i=0,
\qquad
\lim_{A\to\infty}G_i=1.
\]

Thus the constant-\(K_{\rm edge}=-A\) rod ODE indeed permits arbitrarily small rod flux while \(G_i\) approaches \(1\). This is a local rod statement; it does not itself produce an orbit space solving all coupled interior equations.

### 5. Script inconsistency

The SymPy computation and the JSON fields

\[
G_i=\frac{2A}{2A+1},\qquad
\texttt{check\_Phi=2-2G}=0,\qquad
\lim G_i=1
\]

are correct. The manually written `KEY` text incorrectly replaces \(2A/(2A+1)\) by \(A/(2A+1)\). The `part_B_reconcile` block repeats that omitted factor \(2\), producing its nonzero difference artificially.