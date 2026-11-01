# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 54,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step54_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step54_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify, adversarially and constructively, Theorem 54.A and Lemmas 54.1-54.3 in step54_k1_ball_quotient_attainment_theorem.md. The setting: X compact ball quotient other than a fake projective plane, M = X # CPbar^2, P = int |Ric°|^2; an Anderson case-(I) minimizing configuration with only trivial-group cone points. Check in particular: (1) Lemma 54.1 two-orientation cost formula c(N)=4(e-1)+4b1+b^- - 5b^+ for multi-ended AE bubbles with Gamma=1, including the boundary-term hypotheses; (2) Lemma 54.2: is each capped bubble really a connected summand of M, including multi-ended bubbles and graph loops; (3) Lemma 54.3: M=Z#R, b+(M)>=2, Z PSC with b+(Z)>=1 implies SW_M=0 even when b+(R)=0 -- is the neck-stretching argument correct (reducibles on Z side avoided by generic perturbation; irreducibles by PSC)? Is there a known counterexample or a cleaner citation? (4) the pi_1 argument: freely indecomposable PD4 lattice, Hopf surjection H2(Y)->H2(pi1 Y), conclusion that each bubble compactification is a homotopy sphere; (5) part (iii): SW_{V#Sigma}=SW_V for a PSC homotopy sphere; constant negative scalar curvature; Einstein-or-non-Bach-flat; the 'no bubbles if all hat N_k are standard S^4' step via Bishop-Gromov; (6) whether the upper bound (U) p_*(M)<8 pi^2 legitimately follows from the analytic CH-collar cell of web_research_collected.tex Ch.5 for EVERY non-fake-plane ball quotient (collar radius issue); (7) the general-k extension inequality sum[4(e-1)+4b1+beta] < k and its use of Lemma 54.3; (8) the collapse lemma (free circle action region is spin, so cannot carry E) and the orbifold parity remark (absorbing E needs a in H2(X) with a^2=-1 when m=1); (9) the BCG+Bishop computation in data JSON and Remark 4; (10) the answer to A01 on Koiso local rigidity near ball quotients (TT gap 2 from Rcirc eigenvalues -2,+4). Give corrected statements where something fails, and say precisely which hypotheses (H_sm, H_lsc, H_dec, H_eq, H_rem) each conclusion needs. Also assess whether the 'gate economy' paragraph's analysis of the rescaled perturbation coefficient eps*ell^{4-4p} is right and whether a better choice of p(eps) or a different argument gives bubble-scale P-criticality.

## Integrated Scientific Memo

# Verification memo: Step 54

**Theorem 54.A survives under its stated geometric hypotheses, but its proof must be reordered.** The charge formula is correct; the claimed consequence that multiple ends or positive \(b_1\) alone force a positive charge is not. Two further corrections are essential:

- Remark 4 reverses the comparison with the Kähler-type \(W^+\)-energy.
- Bubble-scale \(P\)-criticality does **not** require proving that the rescaled perturbation coefficient vanishes. A compact-replacement argument establishes it directly once smooth bubble convergence is available.

The supplied Chapter 5 does resolve the earlier collar-radius concern: its analytic cell is constructed for **every fixed \(R>0\)**.

## 1. Lemma 54.1: correct formula, incorrect consequence

Assume \(N\) is connected, smooth, oriented, complete, of finite topology, with finitely many AE ends, all having trivial group. Under derivative-controlled decay
\[
\partial^j(g-\delta)=O(r^{-\tau-j}),\qquad \tau>0,
\]
through the derivatives needed for curvature and boundary transgression, the characteristic integrals converge absolutely. Each end contributes the Euclidean Gauss–Bonnet boundary value \(1\); the signature correction tends to zero.

Writing \(\widehat N\) for the smooth manifold obtained by capping all ends,
\[
\chi(N)=\chi(\widehat N)-e,\qquad
e_{\rm GB}(N)=\chi(N)-e=\chi(\widehat N)-2e,
\]
and
\[
\tau(N)=\tau(\widehat N).
\]
Here \(\tau(N)\) means the signature of the compact truncation, equivalently of its cap; it is not a signature of the degenerate ordinary intersection pairing on the open manifold.

Thus
\[
\begin{aligned}
2e_{\rm GB}+3\tau
&=2(2-2b_1+b^++b^-)-4e+3(b^+-b^-)\\
&=-\bigl[4(e-1)+4b_1+b^--5b^+\bigr].
\end{aligned}
\]
Consequently,
\[
\boxed{
P(N)=4\int_N|W^+|^2+\frac1{12}\int_Ns^2
+8\pi^2\bigl[4(e-1)+4b_1+b^--5b^+\bigr],
}
\]
with the analogous reversed-orientation formula. Therefore
\[
P(N)\ge8\pi^2\max\{c(N),c(\bar N),0\}.
\]
The JSON examples, including Schwarzschild’s \(32\pi^2\), are consistent with this formula.

### Boundary hypotheses

Positive-rate derivative decay is sufficient as stated. For the boundary identities alone, it can be weakened to derivative-controlled flat convergence on rescaled annuli,
\[
g-\delta=o(1),\quad r\,\partial g=o(1),\quad r^2\partial^2g=o(1),
\]
**provided finite curvature energy and the required boundary/eta convergence are separately ensured**. Bare “order zero ALE” or \(C^{1,\alpha}\) convergence without curvature control is not an adequate substitute.

Positive-rate decay remains useful elsewhere: it gives the Sobolev compactification needed for the PSC conclusion of Lemma 53.Y.

### What fails after the lemma

Set \(D=4(e-1)+4b_1\). The exact inexpensive-charge condition is
\[
c,\bar c\le0
\quad\Longleftrightarrow\quad
D\le\min\{5b^+-b^-,\,5b^--b^+\}.
\]
It does **not** imply \(e=1\) or \(b_1=0\).

For example,
\[
e=2,\qquad b_1=0,\qquad b^+=b^-=1
\]
gives \(c=\bar c=0\). This topology has actual scalar-flat two-ended AE realizations: take a PSC metric on \(S^2\times S^2\), sum its positive conformal-Laplacian Green functions at two points, and conformally blow up those points. Similarly, a one-pole construction on
\[
(S^1\times S^3)\#(S^2\times S^2)
\]
has \(e=1,b_1=1,b^+=b^-=1\), again with both charges zero.

These examples invalidate the **claimed topological charging argument**. Zero charge does not itself establish that their actual \(P\)-energy is below \(8\pi^2\).

The semidefinite assertion is correct: a nonzero semidefinite cap has a positive charge in one orientation. The needed repaired statement is stronger and simpler after the SW step:
\[
\boxed{
b^+(\widehat N)=0
\quad\Longrightarrow\quad
P(N)\ge8\pi^2\,[4(e-1)+4b_1+b_2].
}
\tag{1}
\]

## 2. Lemma 54.2: summand structure is valid, including loops and multiple ends

Use the **normalized bulk components**, splitting reducible vertices into their cone branches. Record every \(S^3\) attachment, including deeper-tree attachments, in the resolved gluing graph. Cap every incident boundary sphere of each vertex piece.

For a finite connected graph \(\mathcal G\) of such pieces,
\[
\boxed{
M\cong\#_aV_a\ \#\ \#_k\widehat N_k\
\#\ \#^{\,b_1(\mathcal G)}(S^1\times S^3).
}
\tag{2}
\]
Gluing the edges of a spanning tree gives the connected sum of the vertex caps. Each remaining edge joins two boundary spheres of an already connected manifold and introduces an \(S^1\times S^3\) summand. The \(S^3\) gluing-map ambiguity causes no additional factor, since orientation-preserving diffeomorphisms of \(S^3\) are isotopic to the identity.

Therefore every cap is individually a connected summand, even for a multi-ended bubble or a graph with cycles. This is distinct from **relocating** a bubble to one bulk point: that operation still requires a one-attachment subtree, as corrected in Step 53.

No smooth **metric** removability at bulk cone points is needed for (2); the smooth caps are supplied by the diffeomorphism-level decomposition. If a purported bubble vertex retains unresolved interior punctures, those must be resolved or included among its capped incident boundaries.

Under scalar-flatness and positive-rate derivative decay, the corrected Lemma 53.Y supplies a smooth PSC metric on every bubble cap. All ends are compactified separately.

### Additional group-theoretic information

Since
\[
\pi_1(M)=\Gamma
\]
is a one-ended \(PD_4\) group, it is freely indecomposable and is not \(\mathbb Z\). Applying \(\pi_1\) to (2) shows, independently of energy, that
\[
b_1(\mathcal G)=0,
\]
and exactly one vertex cap has nontrivial fundamental group, isomorphic to \(\Gamma\).

Thus graph loops are already excluded by the lattice group. Connectedness of the normalized bulk still uses the case-(I) incidence structure: once bubbles have one outer end and no interior branching attachments, they cannot bridge distinct bulk components.

## 3. Lemma 54.3: valid even when \(b^+(R)=0\)

The statement is correct for ordinary Seiberg–Witten invariants:
\[
M=Z\#R,\quad b^+(M)>1,\quad
Z\text{ PSC},\quad b^+(Z)>0
\quad\Longrightarrow\quad SW_M=0.
\]

If \(b^+(R)>0\), ordinary connected-sum vanishing applies without using PSC.

If \(b^+(R)=0\), then
\[
b^+(Z)=b^+(M)>1.
\]
The proposed one-sided neck-stretching argument is sound, subject to the standard cylindrical-end compactness theorem:

1. Arrange a PSC metric on \(Z\setminus B^4\) with a round product end.
2. For a fixed Spin\(^c\) structure, choose a small compactly supported self-dual perturbation on this side.
3. The Weitzenböck formula excludes irreducible finite-energy monopoles when the perturbation is sufficiently small relative to the positive scalar lower bound.
4. Reducibles must satisfy
   \[
   2\pi\,\mathcal H^+c_1(L)=\mathcal H^+\eta.
   \]
   The \(L^2\) harmonic self-dual space has dimension \(b^+(Z)>0\). Compactly supported perturbations can vary its projection freely, so a small generic perturbation avoids this prescribed value.
5. A sequence of solutions on increasingly long connected-sum necks would limit to a finite-energy monopole on the \(Z\)-side, a contradiction.

The round \(S^3\) has only the reducible critical point; its Dirac kernel and \(H^1\) vanish. “Nondegenerate” here is understood after gauge fixing, accounting for the reducible stabilizer.

No counterexample is supplied or produced. The exact supporting citation is **not verified in the bounded sources**: neither “Kronheimer–Mrowka/Morgan–Szabó–Taubes” nor the branch’s paraphrased negative-definite gluing formula is a precise citation. The required theorem is:

> Cylindrical-end SW compactness across a round \(S^3\) neck, allowing a small perturbation supported on one PSC summand and permitting arbitrary \(b_1\) on the other summand.

For the theorem’s application, this standard neck argument is sufficient; it should not be replaced by an unverified formula for all invariants of arbitrary negative-definite summands.

## 4. Correct proof of Theorem 54.A(i)–(ii)

The non-fake-plane hypothesis gives \(b^+(X)\ge3\). Indeed,
\[
p_g=\frac{c_2}{3}-1+q,\qquad b^+=2p_g+1.
\]
When \(c_2=3,q=0\), the rational Betti numbers are those of \(\mathbb{CP}^2\), precisely the fake-plane case. Otherwise \(p_g\ge1\).

The blow-up formula gives nonzero ordinary SW invariants on
\[
M=X\#\overline{\mathbb{CP}}^2.
\]

The corrected order of proof is:

1. By (U) and \(\mathrm H_{\rm lsc}\),
   \[
   P(V,g_0)+\sum_kP(N_k)\le p_*(M)<8\pi^2.
   \tag{3}
   \]
2. By Lemma 54.2 and \(\mathrm H_{\rm dec}\), every cap is a PSC connected summand of \(M\).
3. Lemma 54.3 and \(SW_M\ne0\) imply
   \[
   b^+(\widehat N_k)=0.
   \]
   This step does not require the energy bound.
4. Apply (1). Its nonnegative integer bracket must vanish, since \(P(N_k)<8\pi^2\):
   \[
   e_k=1,\qquad b_1(\widehat N_k)=0,\qquad b_2(\widehat N_k)=0.
   \tag{4}
   \]
5. The case-(I) graph therefore has one normalized bulk component and only one-attachment bubble pieces:
   \[
   M\cong V\#\Sigma,\qquad \Sigma=\#_k\widehat N_k.
   \]

The original proof’s inference from \(c,\bar c\le0\) before eliminating \(b^+\) must be deleted.

### Fundamental group and homotopy spheres

The connected-sum decomposition gives
\[
\Gamma\cong\pi_1(V)*\bigast_k\pi_1(\widehat N_k).
\]
Freely indecomposable \(\Gamma\) permits only one nontrivial factor. If a bubble factor were nontrivial, it would be \(\Gamma\). The Hopf exact sequence gives a surjection
\[
H_2(\widehat N_k;\mathbb Q)\twoheadrightarrow
H_2(\Gamma;\mathbb Q).
\]
But its source is zero by (4), whereas
\[
H_2(\Gamma;\mathbb Q)=H_2(X;\mathbb Q)\ne0
\]
because \(X\) is aspherical and Kähler. Hence every bubble cap is simply connected.

For a closed simply connected oriented four-manifold, \(H_2\) is torsion-free, by Poincaré duality and universal coefficients. Thus each cap is an integral homology sphere, hence a homotopy sphere by Hurewicz and Whitehead, and is homeomorphic to \(S^4\) by Freedman.

It follows that \(V\) is homeomorphic to \(M\), and the exceptional class \(E\) lies in the bulk \(H_2\)-summand. For every bubble,
\[
P(N_k)=4\int|W^+|^2=4\int|W^-|^2<8\pi^2.
\]

These conclusions use \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec}\), not \(\mathrm H_{\rm eq}\) or \(\mathrm H_{\rm rem}\).

## 5. Part (iii): attainment, SW transfer, scalar sign and flat-bubble exclusion

Under smooth bulk removability and vanishing-error reassembly, replacing the bulk metric by arbitrary smooth \(h\) gives
\[
p_*(M)\le P(h)+\sum_kP(N_k).
\]
Together with \(\mathrm H_{\rm eq}\), this proves
\[
P(g_0)=p_*(V),\qquad
p_*(M)=p_*(V)+\sum_kP(N_k).
\tag{5}
\]

### SW transfer through the homotopy sphere

The PSC gluing argument in the note is valid. The cap sum \(\Sigma\) is a PSC homotopy sphere. Its unique Spin\(^c\) structure has \(c_1=0\); on the cylindrical completion, the reducible has:

- no \(H^1\) deformation;
- no self-dual harmonic obstruction;
- no Dirac kernel, by PSC.

Its Dirac index is zero. Standard \(S^3\) gluing therefore preserves SW under the natural identification of Spin\(^c\) structures, up to the homology-orientation sign:
\[
SW_{V\#\Sigma}=\pm SW_V.
\]
The sign-free equality in Step 54 should be interpreted with compatible orientations. Nonvanishing is unaffected.

The stronger branch assertion that PSC can be omitted relies on an additional gluing theorem not present in the sources. It is unnecessary here.

### Constant negative scalar curvature

An attained smooth \(P\)-minimizer is critical; its trace equation gives
\[
\Delta s=0.
\]
On connected closed \(V\), \(s\) is constant.

Transferred basic classes include \(K\pm E\), with square \(A-1>0\). Their nonvanishing excludes \(s>0\), and the monopole scalar estimate excludes \(s=0\). In fact the all-sign averaging argument gives the stronger estimate
\[
\int_Vs^2\ge32\pi^2A:
\qquad
\frac12\bigl(\|(K+E)^+\|^2+\|(K-E)^+\|^2\bigr)
=\|K^+\|^2+\|E^+\|^2\ge A.
\]
Thus \(s<0\).

Using
\[
P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi,
\]
a Bach-flat \(P\)-critical metric is stationary for \(\int s^2\). At constant scalar curvature,
\[
\nabla\!\int s^2=-2s\,\operatorname{Ric}^{\circ}.
\]
Hence \(s\ne0\) forces Einstein. Otherwise the attained bulk minimizer is non-Bach-flat. The dichotomy is correct.

### Standard caps imply no nontrivial bubbles

If all caps are diffeomorphic to \(S^4\), then \(V\cong M\). Equation (5) forces every \(P(N_k)=0\). Scalar-flatness then gives \(\operatorname{Ric}_{N_k}=0\).

For a complete Ricci-flat AE manifold with trivial group, Bishop–Gromov’s ratio
\[
\frac{\operatorname{Vol}B_r(p)}{\omega_4r^4}
\]
is nonincreasing, tends to \(1\) as \(r\downarrow0\), and also tends to \(1\) at infinity. Equality rigidity makes the manifold Euclidean. Such a flat scale is not a genuine curvature bubble and is discarded.

This proves smooth attainment on \(M\) under the standard-cap assumption. Without it, attainment and a possible Einstein metric are established **on \(V\)**, not necessarily on the original smooth \(M\). Remark 3 must retain this distinction.

### Energy equality can alternatively be derived

Under \(\mathrm H_{\rm rem}\), the stated decay, the fixed diffeomorphism-level decomposition, and vanishing interpolation energy, reassembly gives
\[
p_*(M)\le P(V)+\sum P(N_k).
\]
Combined with \(\mathrm H_{\rm lsc}\), it proves equality. Thus \(\mathrm H_{\rm eq}\) is a sufficient explicit gate, but becomes redundant if this reassembly theorem is established independently.

## 6. Upper bound (U): the supplied source resolves the collar issue

Chapter 5 explicitly states and constructs its cell for **every \(R>0\)**. With \(T=R/2\), it is exactly CH for \(t\ge R\), smooth at the ordinary negative-blow-up bolt, and has
\[
\frac{P(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2).
\]

For an individual compact ball quotient, select an embedded CH ball with matching collar, taking \(R\) below its injectivity radius. Fix this \(R\), then choose \(\epsilon\) sufficiently small. The negative logarithmic term dominates the fixed \(O_R(\epsilon^2)\) remainder. Since the exterior CH metric has \(P=0\), insertion gives
\[
\boxed{p_*(X\#\overline{\mathbb{CP}}^2)<8\pi^2.}
\]
No quotient-uniform radius or remainder constant is needed.

This upper bound also holds for fake projective planes. Their exclusion is needed for the chamber-independent SW argument, not for the construction. The fixed numerical cell may fail to fit some quotients; it is not needed.

A minor wording correction: a constructed competitor yields
\[
p_*(M)\le P(g_\epsilon)<8\pi^2.
\]
Do not write \(p_*<\) the unspecified asymptotic expression “for every admissible \(\epsilon\).”

## 7. General \(k\): correct after the same proof-order repair

For every fixed \(k\), insert cells in \(k\) disjoint small CH balls:
\[
p_*(M_k)<8\pi^2k.
\]
PSC summand vanishing first gives \(b^+(\widehat N_j)=0\). Then
\[
\boxed{
\sum_j[4(e_j-1)+4b_1(\widehat N_j)+b_2(\widehat N_j)]<k.
}
\tag{6}
\]
This is the note’s displayed inequality, because its \(\beta\) reduces to \(b_2\) after \(b^+=0\).

Before that step, the available charge is
\[
\max\{D+b^--5b^+,D+b^+-5b^-,0\},
\]
not
\[
D+\max\{b^--5b^+,b^+-5b^-,0\}.
\]
These expressions differ for indefinite caps.

Equation (6) gives total bubble rank \(<k\). If \(p_*(M_k)<32\pi^2\), all bubbles are one-ended; in particular this follows from the cell bound for \(k\le4\).

### A useful stronger topological consequence

The degree-one blowdown map \(M_k\to X\) is a classifying map. By free indecomposability, only one vertex cap carries \(\Gamma\). If that vertex is \(Y\), the classifying map factors up to homotopy through the degree-one collapse \(M_k\to Y\), so \(Y\to X\) has degree one. Therefore
\[
Q_X\hookrightarrow Q_Y
\]
isometrically over \(\mathbb Q\), and \(b^+(Y)\ge b^+(X)\).

A bubble cannot be that vertex, since every bubble has \(b^+=0\). Hence **every bubble cap is simply connected**, also for general \(k\), and the unique \(\Gamma\)-carrying vertex is bulk.

Moreover, the classifying map is null-homotopic on every simply connected bubble. Its \(H_2\)-image in \(M_k\) therefore lies in the blowdown kernel
\[
\operatorname{span}_{\mathbb Z}\{E_1,\ldots,E_k\}.
\]
This gives a precise interpretation of “not all exceptional classes escape”: the total exceptional rank in bubble summands is \(<k\). For disconnected normalized bulk, the degree-one argument applies to the unique group-carrying bulk component.

## 8. Collapse and orbifold arithmetic

### Free circle region

For a free circle action on an oriented smooth region \(C\),
\[
S^1\longrightarrow C\stackrel\pi\longrightarrow B,
\]
the quotient is an orientable three-manifold and
\[
TC\cong\pi^*TB\oplus\underline{\mathbb R}.
\]
Orientable three-manifolds are parallelizable, so \(w_2(C)=0\).

For \(x=i_*y\), \(y\in H_2(C;\mathbb Z)\), naturality and Wu’s formula give
\[
x^2\equiv\langle w_2(M),x\rangle
=\langle w_2(C),y\rangle=0\pmod2.
\]
Thus \(E^2=-1\) prevents \(E\) from lying wholly in the image of \(H_2(C)\). This says nothing about a class split across the interface, and does not automatically extend to finite-isotropy or general \(F\)-structure regions.

Also, the assertion that part (i) applies “verbatim” to case-(II) bubbles is too broad: Lemma 54.2’s **closed connected-summand decomposition** must be supplied for those bubble attachments. The local charge identity still applies, but the open/collapsed bulk can have other interfaces.

### Orbifold roots

For a root \(r=a+mE\) with \(r^2=-2\),
\[
\boxed{a^2=m^2-2.}
\]
Hence:

- if \(m\) is odd, \(a^2\) is odd;
- if \(m=\pm1\), \(a^2=-1\).

The displayed equation does **not** prove that absorption forces odd \(m\). That requires a precise definition of absorption and the integral lattice/interface calculation. Neither Lemma 52.9(v) nor that calculation is supplied.

An even-\(m\) root, such as \(a+2E\) with \(a^2=2\), illustrates that the equation allows mixing with \(E\); it is not by itself a counterexample to a more restrictive, separately proved full-absorption statement.

Delete the unconditional inference “absorption needs odd \(m\), therefore a square-\(-1\) class.” Even assuming odd \(m\), the particular root requires square \(-1\) only for \(|m|=1\). The non-Kähler conclusion remains dependent on the absent parity lemma.

## 9. BCG–Bishop and Remark 4

Let \(n=c_2(X)\), so \(A=3n\), and normalize an Einstein metric by \(\operatorname{Ric}=-6g\), \(s=-24\).

Bishop gives \(h(g)\le3\sqrt2\); CH has \(h_0=4\). The degree-one map to \(X\) and the BCG entropy inequality give
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\ge\left(\frac4{3\sqrt2}\right)^4
=\frac{64}{81}.
\]
The JSON arithmetic is correct.

The all-sign LeBrun bound gives \(S\ge32\pi^2A\), whereas
\[
576\operatorname{Vol}(X)=32\pi^2A.
\]
Thus \(\operatorname{Vol}(g)\ge\operatorname{Vol}(X)\), stronger than BCG–Bishop.

From \(T_+(M)=A-1\) and \(\chi(M)=n+1\),
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\le3-\frac1n,\qquad
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\le2+\frac2n.
\]
These are also correct.

**The Weyl conclusion is reversed.** For Einstein \(g\),
\[
\int|W^+|^2=2\pi^2(A-1)-\frac{S}{48},
\]
so
\[
\boxed{
\int|W^+|^2-\frac{S}{24}
=2\pi^2(A-1)-\frac{S}{16}
\le-2\pi^2.
}
\]
Any such Einstein metric has integrated \(W^+\)-energy strictly **below**, not above, the Kähler-type value. Equality with that type would require
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
=1-\frac1{3n},
\]
contradicting LeBrun. The entropy/topological window remains nonempty.

## 10. A01: Koiso rigidity and the TT gap

In the supplied normalization,
\[
\mathring R=-2\quad\text{on Hermitian trace-free tensors},
\qquad
\mathring R=4\quad\text{on anti-Hermitian tensors},
\]
of real dimensions \(3\) and \(6\). These eigenvalues do not alone imply the gap, since the second sector has a negative zeroth-order contribution to \(\nabla^*\nabla-2\mathring R\).

The TT Codazzi–Bochner identity supplies the missing estimate:
\[
\|\nabla h\|_2^2
\ge\langle\mathring Rh,h\rangle-\lambda\|h\|_2^2,
\qquad \lambda=-6.
\]
Therefore
\[
\boxed{
\langle(\nabla^*\nabla-2\mathring R)h,h\rangle
\ge6\|h\|_2^2-\langle\mathring Rh,h\rangle
\ge2\|h\|_2^2.
}
\]
The gap \(2\) is correct and lattice-independent. It is an **integrated TT estimate**, not a pointwise estimate.

Gauge-fixed implicit-function theory gives local Einstein rigidity up to diffeomorphism and scale in \(C^{2,\alpha}\), or \(H^s\), \(s>4\). Raw \(H^2\)-closeness does not give pointwise metric control.

The cover-uniform neighborhood claim additionally needs the uniformly-local Hölder inverse theorem cited as “Lemma M.” That lemma is **not supplied**. Finite covers of a fixed quotient preserve local geometry and the TT gap, but these facts alone do not verify the asserted global inverse bound in the stated norm. The general negative-KE/Kuranishi statement is a separate imported deformation theorem, not a consequence of the displayed CH eigenvalues.

## 11. Rescaled perturbation: a stronger energy estimate and a cleaner proof of criticality

The scaling formula is exact:
\[
\varepsilon Q_p(g)
=\varepsilon\ell^{4-4p}
\int(\ell^4+|\operatorname{Ric}_{\hat g}|^2)^p\,dV_{\hat g},
\qquad \hat g=\ell^{-2}g.
\]
Write \(\kappa=\varepsilon\ell^{4-4p}\). The perturbation is zeroth order **in curvature**, but its metric Euler–Lagrange operator is fourth order.

### The bound is stronger for actual smooth near-minimizers

For fixed \(p>1\), put
\[
I_\varepsilon=\inf_{\operatorname{Vol}=1}(P+\varepsilon Q_p).
\]
Testing against fixed smooth metrics gives \(I_\varepsilon\to p_*(M)\). If genuine smooth metrics \(g_i\) satisfy
\[
P(g_i)+\varepsilon_iQ_p(g_i)\le I_{\varepsilon_i}+o(1),
\]
then
\[
\boxed{
0\le\varepsilon_iQ_p(g_i)
\le I_{\varepsilon_i}-p_*(M)+o(1)\to0.
}
\tag{7}
\]
This is stronger than the \(O(1)\) bound used in “gate economy.”

If a chosen scale satisfies the actual Ricci normalization
\[
\ell_i^{4p-4}\int_{B_{\ell_i}}|\operatorname{Ric}|^{2p}\ge c_0>0,
\]
then (7) gives \(\kappa_i\to0\), for fixed \(p\). No \(p(\varepsilon)\) is needed.

Two qualifications matter:

- An \(L^6\)-**full-curvature** radius does not automatically satisfy this Ricci lower bound; Ricci-flat bubbles have nonzero Weyl curvature.
- An incomplete fixed-\(\varepsilon\) limit pair need not satisfy \(P\ge p_*(M)\). Derive (7) on the underlying smooth near-minimizers, then pass appropriate nonnegative bounds to their limits.

Under smooth convergence, a non-Ricci-flat bubble has positive Ricci integral on some compact set, so (7) again forces \(\kappa_i\to0\). A Ricci-flat bubble is already \(P\)-critical.

The proposed exponential scale bound and \(p-1=o(\varepsilon)\) are a correct **conditional algebraic observation**, but the energy estimate in the note does not prove that scale bound. Allowing \(p\downarrow1\) also weakens the supercritical compactness estimates.

### Compact replacement avoids the coefficient issue entirely

Suppose the actual smooth sequence satisfies \(P(g_i)\to p_*(M)\) and converges smoothly on compact subsets at a bubble scale. If a compactly supported metric variation on the bubble lowered its \(P\)-energy by \(\delta>0\), transplant it into \(g_i\). Scale invariance and compact smooth convergence give
\[
P(\widetilde g_i)=P(g_i)-\delta+o(1)<p_*(M),
\]
a contradiction. Unit volume is restored by a global rescaling without changing \(P\).

Hence every such bubble is locally minimizing for \(P\), and therefore \(P\)-critical. This uses neither energy equality nor \(\kappa_i\to0\). Its trace equation gives \(\Delta s=0\); AE curvature decay gives \(s\to0\), so the maximum principle gives \(s=0\). The curvature-functional identity then makes the bubble Bach-flat.

**The remaining analytic object is smooth bubble convergence/strong enough curvature convergence to transplant competitors, followed by derivative-controlled end decay.** Vanishing of the effective perturbation coefficient is not the decisive gate once that convergence exists.

## 12. Hypothesis ledger

All rows involving configurations retain Anderson case-(I) diffeomorphism-level reassembly.

| Conclusion | Required hypotheses |
|---|---|
| Upper bound (U) | Chapter 5 cell only; none of the five gates |
| Smooth connected-summand caps | \(\mathrm H_{\rm sm}\), resolved graph topology; bubble smoothness from \(\mathrm H_{\rm dec}\) |
| PSC caps | Scalar-flatness and positive-rate derivative decay in \(\mathrm H_{\rm dec}\) |
| \(b^+\) of every cap is zero | Summand topology, PSC, \(SW_M\ne0\); no energy gate |
| One-ended, homologically trivial bubbles | Above, (U), \(\mathrm H_{\rm lsc}\), characteristic boundary identities |
| Homotopy spheres, connected bulk, \(V\approx M\) | Thus \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec}\), plus the group/Hopf argument |
| \(P(N)=4\int|W^\pm|^2\) | Previous topology and bubble scalar-flatness |
| Smooth bulk attainment and energy splitting | Add \(\mathrm H_{\rm rem},\mathrm H_{\rm eq}\), and vanishing-error reassembly |
| Negative constant scalar and Einstein/non-Bach-flat dichotomy | Smooth bulk attainment and PSC-homotopy-sphere SW gluing |
| No genuine bubbles, attainment on \(M\) | Previous row plus every cap diffeomorphic to \(S^4\) |
| General-\(k\) charge/rank bound | \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec}\); no equality/removability gate |
| Bubble \(P\)-criticality by replacement | Actual \(P\)-minimizing sequence and compact smooth bubble convergence; no equality gate |

The repaired theorem excludes **homologically or topologically charged smooth bubbling**. It does not by itself exclude collapse, nontrivial-group orbifold absorption, or nonflat exotic-homotopy-sphere bubbles. Those are the precise remaining geometries, rather than failures of the charge identity or of the SW/Hopf mechanism.