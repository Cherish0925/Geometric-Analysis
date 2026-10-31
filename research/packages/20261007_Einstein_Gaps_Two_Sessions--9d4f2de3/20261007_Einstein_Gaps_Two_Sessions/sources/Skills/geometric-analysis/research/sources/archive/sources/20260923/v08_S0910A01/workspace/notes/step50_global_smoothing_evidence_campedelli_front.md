# Step 50: global-smoothing evidence on the Campedelli/product-quotient front

## 0. Correction to Step 49 framing

The Step 49 note found a real mechanism but stated it too categorically.  The correct gain is:

* Kernel-directed local Eguchi--Hanson parameters at an $A_1$ point point in the same infinitesimal direction as complex node smoothing.
* If those local smoothings globalize in a Q-Gorenstein family whose nearby smooth fibers have ample canonical class, Aubin--Yau supplies a negative Kähler--Einstein metric on a smooth fiber, and simultaneous resolution identifies the smooth fiber diffeomorphically with the minimal resolution of the nodal central model.
* This is a concrete Einstein-existence mechanism to test, not a theorem that every product-quotient surface is an existence case and not a theorem that this front cannot produce a counterexample.

Mixed-chirality fillings remain outside this complex smoothing mechanism.  Conversely, failure of a complex/Q-Gorenstein smoothing for a particular model would not prove Einstein nonexistence on the underlying smooth four-manifold; another Einstein metric or another complex structure could still exist.

## 1. Source-level shortcut from order-eight Campedelli literature

The Strategist pointed to the fact that the chosen BCGP $K^2=2$ row has fundamental group $(\mathbb Z_2)^3$, of order eight.  The source check gives a useful but not decisive shortcut.

### 1.1 What BCGP says

BCGP, *Quotients of products of curves*, records near line 84 that numerical Campedelli surfaces with algebraic fundamental group of order $8$ or $9$ have been classified by Mendes Lopes--Pardini--Reid and related sources, and that for order $8$ the fundamental group equals the algebraic fundamental group and is not the dihedral group $D_4$.

The BCGP table identifies the selected product-quotient row as
\[
K^2=2,\quad T_1=T_2=(4,4,4),\quad g_1=g_2=3,
\quad G=\mathbb Z_4^2,
\quad H_1(S,\mathbb Z)=\pi_1(S)=(\mathbb Z_2)^3.
\]
The expanded §6.7 data give the actual two diagonal branch triples
\[
S_1=((1,3),(1,0),(2,1)),\qquad
S_2=((3,2),(0,1),(1,1))
\]
in $\mathbb Z_4^2$.  These actual triples matter: the common signature $(4,4,4)$ alone does not determine the relative character pairing in the obstruction calculation.

### 1.2 What Mendes Lopes--Pardini--Reid proves

The retrieved MPR source `Campedelli surfaces with fundamental group of order 8` proves:

* If $Y$ is a minimal general-type surface with $K_Y^2=16$, $p_g(Y)=7$, $q(Y)=0$ and a free action by a group $G$ of order $8$, then the canonical image $\bar Y\subset\mathbb P^6$ is a complete intersection of four quadrics and is the canonical model of $Y$.
* In the $G=(\mathbb Z_2)^3$ case this was already known from Miyaoka; MPR then handles groups containing an element of order $4$.
* A degree-eight étale cover of a Campedelli surface is the universal cover, and the covering group is the topological fundamental group; $D_4$ is excluded.

This source does not by itself identify the BCGP $G=\mathbb Z_4^2$ product-quotient row with the classical seven-line $(\mathbb Z_2)^3$ Campedelli component, nor does it prove a smoothing component statement for that row.

### 1.3 What Alexeev--Pardini supplies

Alexeev--Pardini's compactification paper is much more directly useful for global smoothing of classical $(\mathbb Z_2)^3$ Campedelli surfaces.  It states that:

* The paper describes an explicit compactification for the component of Campedelli surfaces with $\pi_1=(\mathbb Z_2)^3$ by $\mathbb Z_2^3$-covers of $\mathbb P^2$ branched along seven labelled lines.
* A surface in this component is a $\mathbb Z_2^3$-cover $X\to\mathbb P^2$ with building data seven lines $D_g$, $0\ne g\in\mathbb Z_2^3$, for which the cover has canonical singularities.
* If the seven lines are in general position, the cover is smooth.  If three distinct lines $D_{g_1},D_{g_2},D_{g_3}$ meet and the three labels generate $\mathbb Z_2^3$, the cover has an $A_1$ singularity.  If $g_1+g_2+g_3=0$, the degeneration instead gives noncanonical $\frac14(1,1)$ singularities.
* $K_X=\pi^*(h/2)$ and $K_X^2=2$, so the canonical class on these canonical models is ample; $|2K_X|$ is pulled back from lines in $\mathbb P^2$.
* Locally in the line-arrangement moduli, the family of covers is obtained by deforming the seven lines.  Thus a labelled line arrangement with only independent triple concurrences gives an explicit global smoothing by moving the lines to general position.

This gives a concrete smoothing component, but only for models actually expressible as classical $(\mathbb Z_2)^3$ seven-line covers or known to lie in that component.

## 2. A real six-nodal classical Campedelli boundary model

I wrote and ran

`Sessions/S0910A01/workspace/scripts/step50_six_nodal_campedelli_arrangement.py`.

It checks the exact line arrangement
\[
 x=0,
\quad y=0,
\quad z=0,
\quad x-y=0,
\quad y-z=0,
\quad x-z=0,
\quad x-y+z=0
\]
in $\mathbb P^2$.  Exact integer projective arithmetic gives:

* seven distinct lines;
* nine intersection points total;
* multiplicity census `{2: 3, 3: 6}`;
* no point of multiplicity $\ge4$;
* six triple points with line-index triples
\[
(0,1,3), (0,2,5), (0,4,6), (1,2,4), (2,3,6), (3,4,5).
\]

The script then searches all labellings by the seven nonzero elements of $\mathbb F_2^3$ and finds 1680 labellings for which every triple-point label set is a basis.  One such labelling is
\[
\begin{array}{c|c}
\text{line} & \text{label}\
\hline
x & (0,0,1)\\
y & (0,1,0)\\
z & (0,1,1)\\
x-y & (1,0,0)\\
y-z & (1,0,1)\\
x-z & (1,1,1)\\
x-y+z & (1,1,0).
\end{array}
\]

By the Alexeev--Pardini criterion, the associated classical Campedelli canonical model has exactly six $A_1$ singularities, ample canonical class, and a global smoothing obtained by moving the seven lines to general position.  After the standard ADE simultaneous-resolution/base-change argument, the minimal resolution of this explicit six-nodal canonical model is diffeomorphic to nearby smooth fibers.  Aubin--Yau gives those smooth fibers negative Kähler--Einstein metrics.  Therefore this explicit minimal resolution carries a negative Einstein metric.

This establishes that the smoothing mechanism is not merely formal: six-nodal Campedelli boundary points with the required global smoothing really exist inside the classical component.  It does **not** identify this boundary point with the BCGP $G=\mathbb Z_4^2$ product-quotient row.

## 3. Character calculation for the selected BCGP $\mathbb Z_4^2$ row

I also wrote and ran

`Sessions/S0910A01/workspace/scripts/step50_z4x4_character_smoothing_test.py`.

Using the actual BCGP §6.7 branch triples
\[
S_1=((1,3),(1,0),(2,1)),\qquad
S_2=((3,2),(0,1),(1,1)),
\]
Chevalley--Weil for abelian covers of $\mathbb P^1$ gives
\[
H^0(K_{C_1})=((2,3))\oplus((3,0))\oplus((3,1)),
\]
\[
H^0(K_{C_2})=((0,3))\oplus((1,2))\oplus((3,3)).
\]
Each curve has genus $3$.  Every order-two element fixes only four points on either curve, so the curves are non-hyperelliptic; the multiplication map identifies
\[
H^0(2K_C)\cong \operatorname{Sym}^2 H^0(K_C).
\]
The resulting character decompositions are
\[
H^0(2K_{C_1})=(0,2)+(1,0)+(1,3)+(2,0)+(2,1)+(2,2),
\]
\[
H^0(2K_{C_2})=(0,1)+(0,2)+(1,1)+(2,0)+(2,2)+(3,2).
\]
Consequently
\[
\dim \left(H^0(2K_{C_1})\otimes H^0(K_{C_2})\right)^G=0,
\]
\[
\dim \left(H^0(K_{C_1})\otimes H^0(2K_{C_2})\right)^G=0.
\]
Thus the finite character side of
\[
H^0(\Omega^1_S\otimes K_S)
\]
vanishes for the displayed BCGP pair, assuming the usual quotient/reflexive-form/RDP-resolution comparison is applicable in this nodal product-quotient setting.

This is stronger than the Step 49 numerical observation.  It suggests that the sufficient condition
\[
H^2(T_S)=0
\]
may actually hold for the selected $\mathbb Z_4^2$ product-quotient surface, which by Lee--Park/Burns--Wahl would globalize every choice of local $A_1$ Q-Gorenstein smoothing parameters.  If that sheaf comparison is verified source-level, the selected BCGP row itself would have a global smoothing and hence an exact negative Einstein metric on its underlying smooth resolution.

What remains before treating this as established:

1. Verify the precise sheaf comparison
\[
H^0(\Omega^1_S\otimes K_S)
\cong
\left(H^0(2K_{C_1})\otimes H^0(K_{C_2})\right)^G
\oplus
\left(H^0(K_{C_1})\otimes H^0(2K_{C_2})\right)^G
\]
for the minimal resolution of a quotient with six $A_1$ singularities, including extension across codimension-two fixed points and the Burns--Wahl/RDP comparison.
2. Confirm that $H^2(T_S)=0$ indeed implies global Q-Gorenstein smoothing of all six nodes for this canonical model, not merely a subspace of local smoothings.
3. Connect the resulting smoothed surface to the smooth four-manifold of the minimal resolution through simultaneous resolution/Ehresmann in this particular family.
4. Separately determine whether the BCGP row lies in the classical Alexeev--Pardini component.  The common fundamental group $(\mathbb Z_2)^3$ and numerical invariants do not by themselves prove this.

## 4. Relation to Yau 26

The negative product-quotient front has become a useful existence laboratory rather than a direct obstruction source.  The explicit six-nodal classical model proves that the complex-smoothing/Aubin--Yau route can produce exact Einstein metrics on nodal Campedelli resolutions.  The BCGP character computation gives concrete evidence that the selected $\mathbb Z_4^2$ product-quotient row may also smooth globally.

This does not solve Yau 26.  It only says that one formerly tempting counterexample/stress-test class is more likely to be compatible with Einstein existence.  It also reinforces an important structural lesson: local near-Einstein input metrics and exact Einstein existence can align through deformation theory, so failed exact gluing is not a safe route to nonexistence.  Mixed-chirality fillings and positive $S^2\times S^2$ quotient rows remain outside the negative Aubin--Yau mechanism.

## 5. A03 flow correction recorded

Peer message #381 corrects A03's earlier #379: A03 Step 51 should not be cited as a proof of the normalized Yang--Wang start.  The flat $T^4$ example with nonconstant cutoff creates curvature from zero via
\[
\left.\frac{d}{dt}\operatorname{Rm}\right|_{t=0}=g\wedge\nabla^2(\chi^2),
\qquad
\int |\operatorname{Rm}(g(t))|^2=48\pi^4t^2+O(t^3)
\]
for the reported cutoff.  The critical homothety cancellation does not remove spatial Hessian forcing.  A Xu fixed-point repair with metric-only pullback produces a transported cutoff, because
\[
\varphi^*(\widehat a\widehat g)=(\widehat a\circ\varphi)\varphi^*\widehat g,
\]
not a fixed original cutoff.  The remaining correct target is a coupled transported-coefficient system for $(\widehat g,\widehat a)$ with
\[
\widehat a=a\circ\varphi_t^{-1},
\qquad
\partial_t\widehat a=\widehat a\,W(\widehat a),
\]
plus the metric equation with $-2\widehat a\widehat g$; the positive-time shifted $T/U/C$ continuation remains separate.  A01 route files should not present the restricted IL analytic flow module as settled on the basis of A03 Step 51.
