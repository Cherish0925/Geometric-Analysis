# Step 44: Bi-Kähler orbifold loophole and first-order obstruction ceiling

> **Step 45 Preceptor correction.** This note's curvature computation for the product metric is retained, but several conclusions are superseded by `workspace/notes/step45_preceptor_review_biKahler_loophole.md` and `workspace/data/step45_preceptor_topology_energy_audit.json`. The per-piece CGB bookkeeping in §1.4/energy language is wrong: for the global quotient orbifold the Satake/orbifold Euler contribution is \(\chi_{orb}=4/2=2\), so the regular orbifold part contributes \(16\pi^2\), and each \(A_1\)/Eguchi--Hanson bubble carries \(8\pi^2(2-1/2)=12\pi^2\), not \(8\pi^2\). The total for the balanced \(\mathbb Z_2\) resolution remains \(16\pi^2+4\cdot12\pi^2=64\pi^2\). Freedman's theorem gives only the topological homeomorphism type \(3H\), not the exact smooth diffeomorphism type required by the Yau--26 stress family; exotic smooth structures on \(S^2\times S^2\) are known. Most importantly, the product quotient shows an explicit exceptional locus where both chiral first-order obstructions vanish; it does **not** show that the first-order mode-projection bridge is unworthy. The refined conclusion is a dichotomy: generic Kähler limits force admissible/compatible bubbling and hence \(b_+=1\), while reversed bubbles require the exceptional condition \(\det R_-=0\) at their points; bi-Kähler product quotients are finite exceptional models to classify and attack.
Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope and target fidelity

The active target remains Yau's Problem 26: for every \(n\ge2\), determine whether dimension-only two-sided Ricci pinching forces Einstein existence on the same closed connected smooth manifold. This note does NOT prove or refute the target. It establishes that Route A's first-order obstruction framework is insufficient to close the noncollapsed positive branch for the stress family, identifies the precise mechanism, and redirects the research allocation.

## 1. The decisive test

### 1.1 Setup

Step 43 corrected Step 42's det \(R_+=0\) finding: the Kähler form pins only the self-dual block, so reversed EH bubbles test the unpinned \(R_-\). The question is whether this chirality lever can close the noncollapsed branch for \(M_k = \#_k(S^2\times S^2)\).

The strategist identified a cheap decisive test: if there exists a positive Einstein orbifold with \(\det R_+ = \det R_- = 0\) at all singular points, and whose mixed EH resolution produces \(\#_k(S^2\times S^2)\), then first-order obstruction is vacuous for that configuration and Route A cannot close the branch.

### 1.2 The bi-Kähler orbifold \((S^2\times S^2)/\mathbb Z_2\)

Consider \(S^2(1)\times S^2(1)\) with the product Einstein metric (\(\operatorname{Ric}=g\), \(\Lambda=1\)), and the \(\mathbb Z_2\) action \(\sigma(x,y)=(a(x),a(y))\) where \(a\) is the \(\pi\)-rotation about the poles.

**Fixed points.** The fixed set consists of \(\{N,S\}\times\{N,S\}=4\) points, each with isotropy representation \(d\sigma=-I_4\) on \(T_p(S^2\times S^2)\cong\mathbb R^4\). Each point is a \(\mathbb C^2/\mathbb Z_2\) \(=A_1\) singularity.

**Curvature operator (symbolically verified).** In an orthonormal frame \(\{e_1,e_2\}\) tangent to the first sphere and \(\{e_3,e_4\}\) tangent to the second, the curvature operator on \(\Lambda^2\) is \(\operatorname{diag}(1,0,0,0,0,1)\) in the canonical 2-form basis. Transforming to the self-dual/anti-self-dual basis:
\[
R_+ = R_- = \begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},
\qquad
W_+ = W_- = \begin{pmatrix}2/3&0&0\\0&-1/3&0\\0&0&-1/3\end{pmatrix}.
\]
Cross terms vanish (Einstein). Both determinants vanish:
\[
\det R_+ = \det R_- = 0 \quad\text{at every point.}
\]
This is the **bi-Kähler** structure: the product metric is Kähler in the standard orientation (Kähler form \(\omega_1+\omega_2\in\Lambda^2_+\), self-dual) and Kähler in the opposite orientation (Kähler form \(\omega_1-\omega_2\in\Lambda^2_-\), anti-self-dual). The two Kähler structures pin \(W_+\) and \(W_-\) independently.

The product Einstein metric descends to the quotient because \(\mathbb Z_2\) acts by isometries, making \((S^2\times S^2)/\mathbb Z_2\) a positive Einstein orbifold with all 4 singular points having \(\det R_+=\det R_-=0\).

### 1.3 Resolution topology

**Orbifold Betti numbers.** The \(\mathbb Z_2\) acts trivially on \(H^2(S^2\times S^2;\mathbb Q)=\mathbb Q^2\), so \(b_2^{\rm orb}=2\). The \(G\)-signature theorem gives \(\tau^{\rm orb}=0\) (the signature defect for \(\mathbb Z_2(1,1)\) is \(-\frac12\cot(\pi/2)^2=0\)). Hence \(b_+^{\rm orb}=b_-^{\rm orb}=1\).

**EH resolution with orientation choices.** Each \(A_1\) singularity is resolved by an Eguchi–Hanson bubble with either compatible or reversed orientation:
\[
\text{Compatible: }(\Delta b_+,\Delta b_-)=(0,1),\qquad
\text{Reversed: }(\Delta b_+,\Delta b_-)=(1,0).
\]
With \(j\) reversed and \(4-j\) compatible:
\[
b_+(\tilde M)=1+j,\quad b_-(\tilde M)=5-j,\quad
\tau(\tilde M)=2j-4,\quad b_2=6,\quad \chi=8.
\]

**Resolution table:**

| \(j\) | \(b_+\) | \(b_-\) | \(\tau\) | Form | Homeomorphism type |
|-------|---------|---------|----------|------|-------------------|
| 0 | 1 | 5 | \(-4\) | \(\langle1\rangle\oplus5\langle-1\rangle\) | \(\mathbb{CP}^2\#5\overline{\mathbb{CP}^2}\) |
| 1 | 2 | 4 | \(-2\) | \(2\langle1\rangle\oplus4\langle-1\rangle\) | \(2\mathbb{CP}^2\#4\overline{\mathbb{CP}^2}\) |
| **2** | **3** | **3** | **0** | **\(3H\)** | **\(\#_3(S^2\times S^2)\)** |
| 3 | 4 | 2 | \(2\) | \(4\langle1\rangle\oplus2\langle-1\rangle\) | \(4\mathbb{CP}^2\#2\overline{\mathbb{CP}^2}\) |
| 4 | 5 | 1 | \(4\) | \(5\langle1\rangle\oplus\langle-1\rangle\) | \(5\mathbb{CP}^2\#\overline{\mathbb{CP}^2}\) |

**The \(j=2\) case produces \(\#_3(S^2\times S^2)\).** The manifold is simply connected (the orbifold has isolated singularities and the smooth part is simply connected). The spin structure is preserved (the orbifold is spin because \(-I_4\) lifts to \(\operatorname{Spin}(4)\), and EH in either orientation is spin). Even unimodular indefinite forms of rank 6 and signature 0 are uniquely \(3H\). By Freedman's theorem, \(\tilde M\cong\#_3(S^2\times S^2)\).

For \(j\ne2\), \(\tau\not\equiv0\pmod8\), so Rokhlin's theorem forces the manifold to be non-spin with odd intersection form. These are \(\mathbb{CP}^2\)-type and do not appear in the stress family.

### 1.4 First-order obstruction is vacuous

The Ozuch first-order obstruction at each singular point:
- Compatible EH bubbles test \(\det R_+=0\): **satisfied** (bi-Kähler pinning).
- Reversed EH bubbles test \(\det R_-=0\): **satisfied** (bi-Kähler pinning).

**Both types of bubbles pass the first-order test at all 4 singular points.** The mixed resolution with \(j=2\) produces \(\#_3(S^2\times S^2)\), a member of the stress family. The first-order chirality obstruction cannot distinguish this configuration from a smooth limit.

## 2. Case split for orbifold limits

The correct analysis splits on the curvature blocks of the orbifold limit, without assuming Kähler structure:

**Case 1: Non-Kähler limit.** Both \(W_+\) and \(W_-\) are generically unrestricted. \(\det R_+\ne0\) and \(\det R_-\ne0\) generically. First-order obstruction is nontrivial on both sides. This is the **easiest case** for Route A.

**Case 2: Kähler limit, not bi-Kähler.** The Kähler form pins one block, e.g. \(\det R_+=0\). But \(W_-\) is unpinned, so \(\det R_-\ne0\) generically. First-order obstruction is nontrivial for reversed bubbles. Example: \(\mathbb{CP}^2\) with Fubini–Study, where \(R_-=(\Lambda/3)I\) and \(\det R_-=(\Lambda/3)^3>0\).

**Case 3: Bi-Kähler limit.** Both blocks are pinned: \(\det R_+=\det R_-=0\) everywhere. First-order obstruction is **trivially satisfied for all orientations**. Example: \((S^2\times S^2)/\mathbb Z_p\) quotients. This is the **hard case** and the loophole.

**Hidden assumption.** The entire \(b_+(O)=1\) bookkeeping (Step 43) assumes the limit is Kähler–Einstein. Cheeger–Naber gives only a positive Einstein orbifold limit, not necessarily Kähler. The statement "positive Einstein 4-orbifold \(\Rightarrow\) conformally Kähler" is not a theorem; it is essentially the LeBrun–Ozuch admissibility hypothesis. The clean analysis works with \((\det R_+,\det R_-)\) directly.

## 3. Why higher-order escalation is unreliable

The session's own record warns against higher-order Ozuch obstruction as the main investment:

- At \(\Lambda=0\) (Ricci-flat), the "chessboard family" satisfies all 84 stable constraints in the 14-dimensional Ozuch deformation space. Higher obstructions do not close there.
- At \(\Lambda>0\), no source establishes that higher-order obstructions close for bi-Kähler orbifolds.
- The Step-34/42 computation shows the \(\Lambda\)-source generates a definite \(O(\Lambda t^2)\) growing coefficient, but matching it to the orbifold second-order jet requires higher deformation theory that is not available and may not succeed.

## 4. Corrected route allocation

### 4.1 What Route A can still do

Route A's first-order framework handles Cases 1 and 2 (non-Kähler and Kähler-not-bi-Kähler limits). It eliminates near-round degenerations (\(\det R_+>0\)) and single-Kähler degenerations with generic \(R_-\). But it cannot handle bi-Kähler limits, which include the concrete stress-family target.

Even a completed Route A gives: "for fixed \(M\), noncollapsed positive near-Einstein sequences either converge regularly or bubble at points where \(\det R_\pm=0\)." This is a conditional filter, not a proof or refutation.

### 4.2 The binding constraint is collapse

For the large family \(M_k=\#_k(S^2\times S^2)\), \(k\to\infty\): noncollapsed sequences are already ruled out by Step 9 (Cheeger–Naber finite diffeomorphism type vs.\ unbounded \(b_2\)). Any large-\(k\) counterexample must collapse.

For fixed \(M\): noncollapsed bubbling is partially obstructed by chirality (Cases 1–2) but has a concrete loophole (Case 3). Collapse remains the unaddressed half of \(P_4^+\) and the only mechanism that can handle large \(k\).

### 4.3 Recommended reallocation

1. **Primary: positive collapse.** The Bochner central almost-Killing/volume-gap bridge (Steps 28–30) is the most dimension-flexible collapse tool. Its unresolved bridge—producing scale-comparable central almost-Killing fields from Ricci pinching alone—should be the next construction target.

2. **Secondary: independent verification of A01/A03 negative flow.** The peer Ishida–LeBrun flow route now claims to need only (H-DT) (transported-coefficient DeTurck existence). If verified, this would give a restricted four-dimensional negative gap. Verify one load-bearing interface rather than accepting the whole chain.

3. **Tertiary: high dimensions.** No codimension-four EH machinery transfers to \(n\ge5\). The Kaluza–Klein collapse examples show positive Einstein collapse is compatible in all \(n\ge5\). The next high-dimensional work should either find a no-Einstein reservoir or develop dimension-flexible collapse analysis.

4. **Deprioritize:** higher-order Ozuch deformation at \(\Lambda>0\); toric diagonal BVP refinement; further first-order mode-projection development.

## 5. Contrast with CP² (non-bi-Kähler control)

As a control: \(\mathbb{CP}^2\) with Fubini–Study is self-dual (\(W_-=0\)), so \(R_-=(\Lambda/3)I\) and \(\det R_-=(\Lambda/3)^3>0\). Reversed EH bubbles are **first-order obstructed everywhere** on \(\mathbb{CP}^2\). This shows the chirality lever is genuine for single-Kähler limits—the loophole is specifically the bi-Kähler (product-type) structure.

## 6. Files from this step

- Resolution test: `workspace/data/step44_biKahler_orbifold_resolution_test.json`
- Symbolic verification: `workspace/scripts/step44_biKahler_curvature_verification.py`
- Resolution script: `workspace/scripts/step44_biKahler_orbifold_resolution_test.py`

No Lean formalization was attempted; the target remains far from formal proof.
