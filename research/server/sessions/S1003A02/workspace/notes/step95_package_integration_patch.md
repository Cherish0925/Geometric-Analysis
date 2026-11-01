# Step 95 — theorem-package integration patch for the verified transfer scope and full-absorption screen

This short file is an insertion-ready research asset for Agent2. The full proof and computational evidence are in
`step95_verified_transfer_lattice_thresholds.md`, `workspace/scripts/step95_filler_lattice_screen.py`, and
`workspace/data/step95/filler_lattice_screen_certificate.json`.

## Scope theorem for the transfer method

Let a negative Einstein orbifold over a ball-quotient host resolve to
\(X\#k\overline{\mathbb{CP}}^2\) by known Kähler Ricci-flat ALE fillers, and set
\[
k_b=k-\sum_j b_2(N_j),\quad
S_{\rm cx}=\sum_{\rm cx}(1-|\Gamma_j|^{-1}),\quad
S_{\rm rev}=\sum_{\rm rev}(1-n_j^{-2}).
\]
The transferred scalar/mixed Seiberg–Witten inequalities imply
\[
S_{\rm cx}+\frac29S_{\rm rev}\le\frac k6+k_b.
\]
For complex-oriented fillers only, the sharper finite-\(A\) relation is
\[
S_{\rm cx}\le k_b+\beta(k,A),\qquad
\beta(k,A)=\frac{k(5y+1)}{18(1+y)},\quad y=\sqrt{1-3k/A}.
\]
Here \(k_b\) is a rank deficit, not a chosen set of embedded exceptional spheres. Each retained rank contributes one unit of slack to these aggregate inequalities. They can still exclude retained-rank configurations whose total filler cost exceeds the slack; what they do not encode is class-by-class placement, discriminant linking, or singular monopole data after the displayed budgets pass. A Wahl ball absorbs no rank. Pure Wahl configurations have \(k_b=k\), while Wahl points can coexist with a full-rank Kronheimer system at \(k_b=0\). Surviving retained-rank or Wahl sectors therefore require new singular information—APS/Dedekind data coupled to another global identity, orbifold monopoles, or type-T local analysis—not repetition of the same aggregate smooth transfer.

For a general minimal general-type host the exact envelope is
\[
9C_-+2C_++42k+12(3c_2-c_1^2)\ge0,
\]
coming from the identity
\[
9x+3T-(\sqrt{8x}+\sqrt{T-x})^2
=2(\sqrt{T-x}-\sqrt{2x})^2.
\]

## Full-absorption theorem

Assume the ball-quotient/aspherical lattice hypotheses, use only complex-oriented Kronheimer fillers, and let all \(k\) blow-up ranks lie in the fillers (\(k_b=0\)). Their root lattice embeds in \(-I_k\). Since norm-two vectors are \(\pm e_i\pm e_j\), the signed-support classification gives
\[
R=\bigoplus_iD_{a_i},\qquad a_i\ge2,\qquad\sum_i a_i=k.
\]
The low-rank conventions are \(D_2=A_1\oplus A_1\) and \(D_3=A_3\); E-types never embed, and an \(A_r\) component other than \(A_3\) consumes one more coordinate than its rank. The exact curvature cost is
\[
c(D_2)=1,\qquad c(D_3)=\frac34,\qquad
c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4),
\]
and every possible Einstein bulk must satisfy
\[
\sum_i c(D_{a_i})\le\beta(k,A).
\]
Since \(c(D_a)>a/6\) for \(2\le a\le5\), every full absorption contains a \(D_a\) block with \(a\ge6\); hence \(k\ge6\). At \(k=6\), the only arithmetic/lattice possibility is \(D_6\), with
\[
A\ge A_{\rm crit}=\frac{3675}{64};
\]
for a ball quotient \(A\in9\mathbb Z\), the first off-wall passing value is \(A=63\). The first mixed rows occur at \(k=11\): \(D_3\oplus D_8\) needs \(A\ge9409/96\) (first multiple of nine 99), while \(D_4\oplus D_7\) needs \(A\ge196249/160\) (first multiple 1233). These are necessary curvature-and-lattice possibilities only. A full-rank D-system has finite index in \(I_k\), so compatible link pairings, a compact complement, and a negative Einstein metric remain separate existence problems.

## Explicit scope exclusions

- The theorem above does not classify Şuvaina \(d\ge2\) intersection forms.
- Wahl additions increase charge cost but do not absorb rank; they are not represented by a D-block partition.
- The exact enumeration stored in Step 95 covers \(2\le k\le40\); the universal “some \(D_{\ge6}\)” theorem comes from the signed-support proof, not extrapolation.
- The scripts report the first off-wall value \(A>3k\). At \(A=3k\), \(\beta=k/18\), and passing equality rows belong to the unresolved wall problem.
- No passing row constructs an orbifold, an Einstein metric, or a near-minimizing sequence.
