---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds]

Step 4 (Schoen 1984). For the remaining cases ( n = 3 , 4, 5 and the LCF case, where Aubin’s Weyl correction vanishes), Schoen used the Positive Mass Theorem : for a confor-mal factor G (the conformal Green’s function at a point p), the metric ˆ g = G4/(n−2) g is asymp-totically flat, and Y (M, [g]) < Y (Sn) holds if and only if the ADM mass mADM (ˆ g) > 0. By the PMT ( §2.3), mADM ≥ 0 with equality only on ( Rn, g Eucl ). This completes the proof. 46 Remark 2.2 (Sign of the Yamabe constant as conformal invariant) . The sign of Y (M, [g]) 

is a conformal invariant: 

• Positive Yamabe class (Y > 0): the conformal Laplacian Lg is a positive operator, and [g] contains a metric of positive scalar curvature. In this thesis, “PSC” always means Y > 0.

• Zero Yamabe class (Y = 0 ): [g] contains a scalar-flat metric. Examples: flat tori 

Tn and balanced products Sk × Hn−k.

• Negative Yamabe class (Y < 0): every metric in [g] has total scalar curvature negative. Example: hyperbolic manifolds Hn/Γ.

Theorem 2.13 (Orbifold Yamabe existence [2, 1]) . Let (M, g ) be a compact Riemannian orbifold with isolated singularities, local groups Gi ≤ O(n). Then: 

Yorb (M, [g]) ≤ Y (Sn) min  

> i

|Gi|−2/n . (2.7) 

If the inequality is strict, there exists a smooth conformal metric with constant scalar curva-ture (a Yamabe minimizer). 

The factor |Gi|−2/n reflects that a test function concentrated near the singular point pi sees the orbifold chart Rn/G i and gains a volume factor |Gi|−1. This theorem is used in §?? to solve the Yamabe problem on LCF orbifolds. The Yamabe theorem guarantees a canonical representative — a CSC metric — in every conformal class, a fact exploited throughout Chapter 3 where we study moduli spaces of such representatives. The sign of the Yamabe constant (positive, zero, or negative) is a coarser but fundamental conformal invariant that determines which of the three broad classes a manifold belongs to. The key non-negativity ingredient in Schoen’s completion of Step 4 is 47 the Positive Mass Theorem, which we review next. 

# 2.3 Positive Mass Theorem 

The Positive Mass Theorem (PMT) is used in this thesis in two ways: (i) as the key ingredient in Schoen’s completion of the Yamabe problem ( §2.2, Step 4), and (ii) as the model for the LCF ALE orbifold PMT proved in Chapter 3 ( §3.27). 

Definition 2.10 (ADM mass [11]) . Let (M n, g ) be an ALE manifold with a single end, and let {xi} be the asymptotic coordinates on the end. The ADM mass of the end is 

m(g) = lim 

> r→∞

12( n − 1) ωn

Z

> Sr

(∂igij − ∂j gii )νj dσ, (2.8) 

where Sr = {| x| = r}, ν is the outward unit normal, and ωn is the volume of the unit ball in Rn. The integral converges when the scalar curvature Rg is integrable. For AF manifolds (Γ = {1}), this coincides with the classical general-relativistic definition. 

Remark 2.3. The ADM mass is well-defined for ALE orbifolds as well, and each end carries its own mass. For ALE manifolds with non-trivial group Γ at infinity, the PMT does not hold in general: LeBrun constructed anti-self-dual ALE metrics in dimension 4 with Rg = 0 

and m(g) < 0. The PMT holds in the LCF ALE setting (Chapter 3, Theorem 3.27). 

Theorem 2.14 (Positive Mass Theorem [55]) . Let (M n, g ) be a complete asymptotically flat Riemannian manifold with n ≤ 7, non-negative scalar curvature Rg ≥ 0, and integrable Rg.Then m(g) ≥ 0, with equality if and only if (M, g ) is isometric to (Rn, g Eucl ).Proof sketch (Schoen-Yau minimal surface method). The proof proceeds by contradiction. Assuming m(g) < 0, one perturbs g near infinity to produce an AF metric with Rg ≥ 0 and 

m(g) < 0 that admits a stable minimal hypersurface Σn−1 (existence via the Plateau 48 problem: the negative mass creates a barrier forcing the area functional to have a minimum on large spheres). The second variation formula for area gives 0 ≤ δ2 Area(Σ) = −

Z

> Σ

(|II |2 + Ric( ν, ν )) f 2 dσ 

for any variation function f . Combined with the Gauss equation and Rg ≥ 0, this leads to a contradiction (the stability inequality forces the induced scalar curvature RΣ to be non-negative, but a topological argument on Σ shows it must be zero, and then Σ is flat and the original manifold is flat). The dimension restriction n ≤ 7 ensures Σ is smooth (no interior singularities). The Schoen-Yau argument relies on the existence and regularity of stable minimal hypersur-faces, which fails in high dimensions ( n ≥ 8) due to possible interior singularities. Witten’s spinorial proof, which we state next, bypasses this difficulty entirely. 

Theorem 2.15 (Witten’s spinorial proof [70]) . Let (M n, g ) be a complete spin asymptotically flat manifold with Rg ≥ 0. Then m(g) ≥ 0, with equality iff (M, g ) ∼= ( Rn, g Eucl ).Proof sketch. Since M is spin, the Dirac operator /D acts on spinors. Solve /Dψ = 0 with 

ψ → ψ0 (constant spinor) at infinity. The Weitzenb¨ ock formula /D2 = ∇∗∇ + Rg/4 gives, on integration by parts: 

m(g) · | ψ0|2 =

Z

> M



|∇ ψ|2 + Rg 

> 4

|ψ|2



dV g ≥ 0.

Equality forces ∇ψ = 0 and Rg = 0, implying ( M, g ) is flat. The two proofs above assume the manifold is asymptotically flat (trivial group at infinity). In the LCF setting, the developing map provides a conformally natural way to handle the ALE case (non-trivial group at infinity), leading to a version of the PMT that applies directly 49 Schoen-Yau (1979) Witten (1981) Method Stable minimal hypersurfaces Dirac operator / spinors Spin structure Not required Required Dimension n ≤ 7 All n

Rigidity Isometric to Rn Parallel spinor ⇒ flat Table 2.1: Comparison of the two proofs of the classical PMT. to the blow-up limits arising in the LCF moduli theory. 

Theorem 2.16 (Schoen-Yau PMT for LCF manifolds [59]) . Let (M n, g ) be a complete LCF manifold with n ≥ 3, Rg ≥ 0, and an asymptotically Euclidean (AE) end. Suppose the developing map ϕ : fM → Sn is injective. Then m(g) ≥ 0, with equality if and only if (M, g )

is conformally equivalent to (Rn, g Eucl ).The same conclusion holds for ALE orbifolds with group Γ at infinity, with equality iff (M, g )

is the flat cone Rn/Γ.Proof sketch. Step 1 (Conformal compactification). Using the developing map, confor-mally compactify ( M, g ) to a compact LCF orbifold ( ˆM , ˆg) by adding a point p∞ at infinity. 

Step 2 (Green’s function). The conformal Laplacian Lˆg is non-negative (since Rg ≥ 0and Y ( ˆM , [ˆ g]) > 0). Let Gp∞ be the positive Green’s function of Lˆg at p∞: LˆgGp∞ = δp∞ ,

Gp∞ > 0 (maximum principle). 

Step 3 (Mass identification). Near p∞ (corresponding to |x| → ∞ on M ), by the harmonic expansion (Lemma 1.4): 

Gp∞ (x) = c(n)|x|2−n + m + O(|x|−1),

where m is proportional to mADM (g). 

Step 4 (Non-negativity). If m < 0, then Gp∞ would become negative for large |x| (the 50 constant term m dominates c(n)|x|2−n → 0), contradicting Gp∞ > 0. Hence m ≥ 0. 

Step 5 (Rigidity). If m = 0, the metric G4/(n−2)  

> p∞

ˆg is scalar-flat and complete; by the classification of scalar-flat LCF AE manifolds, ( M, g ) ∼= ( Rn, g Eucl ). 

Remark 2.4. This theorem is the direct predecessor of the LCF ALE orbifold PMT proved in §3.27, which extends it to the setting of ALE orbifolds with non-trivial group Γ at infinity. It is also the key step in Schoen’s resolution of the Yamabe problem for LCF manifolds: the strict positivity of the ADM mass (whenever (M, g )̸ ∼= Rn) precisely gives Y (M, [g]) < Y (Sn),completing Step 4 of the proof of Theorem 2.12. 

Classical PMT LCF PMT (SY88) Setting AF spin manifolds LCF manifolds/ALE orbifolds Key tool Minimal surfaces / Dirac Developing map + Green’s function Dimension n ≤ 7 (SY) or all n (Witten) All n ≥ 3Rigidity Isometric to Rn Conformally equivalent to Rn

Table 2.2: Comparison of the classical and LCF Positive Mass Theorems. With the Yamabe theorem and the Positive Mass Theorem in place, we have the two funda-mental existence and non-negativity results for CSC metrics on LCF manifolds. The next section surveys the standard examples and known classification results, organized by Yamabe class, which motivate the moduli-space questions studied in Chapter 3. 

# 2.4 Examples and Classification Results for LCF Man-ifolds 

We survey the standard examples of LCF manifolds and the known classification results, organized by Yamabe class. 51 2.4.1 Standard examples of LCF manifolds and their Yamabe class 

The following table summarizes the canonical LCF manifolds. Manifold Yamabe class Developing map image Limit set Λ 

Rn Y = 0 Rn ⊂ Sn {pt }

(Sn, g round ) Y > 0 (max) Sn ∅

Sn/Γ, Γ ≤ O(n + 1) finite Y > 0 Sn ∅

Sn−1 × R Y > 0 Sn \ { N, S } {N, S }

Sn−1 × S1 Y > 0 Sn \ { N, S } {N, S }

Tn (flat) Y = 0 Rn ⊂ Sn {pt }

Rn/Γ, Γ ≤ O(n) finite Y = 0 Rn {pt }

Hn/Γ, Γ cocompact Y < 0 Bn ⊂ Sn Sn−1

Sk(κ) × Hn−k(κ) (balanced) Y = 0 Sn \ Sn−k−1 Sn−k−1

Sn−1 × S1#Sn−1 × S1 Y > 0 Sn \ Λ Cantor Set Table 2.3: Standard LCF manifolds by Yamabe class. 

• Flat torus Tn = Rn/Zn: Flat metric, W = 0 trivially; Y (Tn) = 0. The developing map is the universal cover Rn → Rn, with the limit set a single point. 

• Round sphere (Sn, g round ): Constant curvature +1, W = 0; the Yamabe constant 

Y (Sn) is the maximum over all compact manifolds. 

• Spherical space forms Sn/Γ: Constant curvature +1, Y > 0. The developing map is the covering Sn → Sn/Γ. These are the building blocks of LCF manifolds with PSC (§2.4.2). 

• Round cylinder Sn−1 × R: Product with curvatures +1 and 0, LCF by Theorem 2.2 (Case 1). The scalar curvature is Rg = ( n − 1)( n − 2) > 0 (positive Yamabe class). The developing map sends the cylinder to Sn \{ N, S } via stereographic projection from both poles. 

• Hyperbolic space forms Hn/Γ: Constant curvature −1, W = 0; Y < 0. The developing map is the Poincar´ e ball inclusion Hn ,→ Bn ⊂ Sn, with Λ = Sn−1 (full boundary sphere). 52 • Balanced products Sn1 (κ)×Hn2 (κ) with ( n1 −1) κ = ( n2 −1) κ: LCF by Theorem 2.2 (Case 2), Rg = 0 (zero Yamabe class). 

• Flat cone Rn/Γ, Γ ≤ O(n) finite: The model ALE end; Y = 0. See Definition 1.6. The Yamabe class of each example above is not a coincidence: it reflects the global curvature sign and the geometric complexity of the developing map. Among these, the positive Yamabe class is the most rigid and admits the most complete classification. 

## 2.4.2 Classification of LCF manifolds in the positive Yamabe class 

Now, we are at the point to state some existing results of classification of LCF manifolds in the positive Yamabe class. First, it is the Izeki’s theorem of conformal connected sum. 

Theorem 2.17 (Izeki [36]) . Let (M n, g ) be a compact LCF manifold with dim H(Λ) < 1.The M is conformally equivalent to the finite quotient of 

#mj=1 

 Sn−1 × S1),

for some m ≥ 0. In particular, when m = 0 , M is conformally equivalent to a spherical space form. 

The key analytic input is the size of the limit set Λ of Γ. For compact LCF manifolds with 

Y > 0, Schoen–Yau gives dim H(Λ) ≤ (n − 2) /2. In dimensions n = 3 , 4, to obtain the strict estimate dim H(Λ) < 1, one uses Brooks’ non-amenability criterion for coverings (hence positive bottom spectrum) together with the Izeki/Sullivan dimension–spectrum relation [14, 36]; this is exactly the strict inequality needed in the low-dimensional classification step. The finite quotient is comming from the Selberg’s Lemma (cf. Theorem 2.11). Note that this classification also holds for good LCF orbifolds. All the LCF orbifolds with positive Yamabe class are good will be shown in Theorem 3.13. Hence, Theorem 2.17 holds 53 for orbifolds as well. To actually classify M in dimension n = 3 or 4, we need the following classification theorems. 

## 2.4.3 Classification in dimension 3 

In dimension 3, the topology of compact positive-scalar-curvature manifolds (orbifolds) is classified by Schoen–Yau and Geometrization (Perelman/Kleiner–Lott): 

M 3 ∼= # ( S3/Γi) # # ( S2 × S1).

This classification is not LCF-specific, but for compact LCF manifolds (orbifolds) with Y > 

0, it is fully compatible with the Kleinian/Izeki description and confirms the same topological possibilities in dimension 3. 

Theorem 2.18 (3D classification [40, 57]) . Let M 3 be a compact 3-manifold that admits an LCF metric with positive scalar curvature. Then M is conformally equivalent to a connected sum of spherical space forms and copies of S2 × S1 with compact quotient. Proof sketch. The topology comes from the classification of PSC 3-manifolds: 1. By Schoen–Yau, PSC in dimension 3 excludes incompressible tori. 2. By Perelman’s geometrization (in the Kleiner–Lott formulation), compact 3-manifolds with PSC decompose as connected sums of spherical space forms and S2 × S1 factors. 3. Therefore any compact 3-manifold carrying an LCF PSC metric has exactly this topol-ogy. 4. Use the fact that all the manifolds (orbifolds) in the classification admits a LCF metric with PSC. 54 5. The conformal connected sum is given by [37]. The compact three-dimensional topology in the PSC regime is well understood, while the noncompact case provides important models for ALE end geometry used later in Chapter 3. 

## 2.4.4 Classification in dimension 4 

In dimension 4, a compact LCF manifold with Y > 0 has W = 0 and R > 0, hence positive isotropic curvature (PIC). The Ricci-flow/PIC classification by Hamilton and Chen–Tang– Zhu, yields the following complete topological classification. 

Theorem 2.19 (4D LCF classification [36, 33, 20]) . Let M 4 be a compact 4-manifold (orb-ifold) that admits an LCF metric with positive scalar curvature. Then M is conformally equivalent to a connected sum of quotients 

M ∼= S4/Γ1# · · · # S4/Γk# ( S3 × S1)/Γ′

> 1

# · · · # ( S3 × S1)/Γ′

> m

,

where Γi, Γ′ 

> j

are finite groups acting freely on S4 and S3 × S1 respectively. Proof sketch. The argument parallels the 3D case, combining PSC/PIC topology with the Kleinian framework. 1. An LCF metric with Y > 0 satisfies W = 0 and R > 0. In dimension 4, W = 0 and 

R > 0 together imply positive isotropic curvature (PIC). 2. By Hamilton’s theorem [33], a compact 4-manifold with PIC is diffeomorphic to a con-nected sum of S4 and S3 × S1 factors. Chen–Tang–Zhu [20] completed the classification in the orbifold setting, using Ricci flow with surgery and the fact the PIC condition is preserved by Ricci flow. 3. [37] then identifies the conformal type with the connected sum of quotients of S4 and 55 S3 × S1.The four-dimensional case thus mirrors the three-dimensional picture: the PIC condition plays the role that geometrization plays in dimension 3, and the limit-set estimate dim H(Λ) <

1 is the common bridge between the Kleinian description and the topological classification in both dimensions. 

## 2.4.5 Complete noncompact LCF manifolds with non-negative Ricci curvature 

Lastly, we conclude this section by the classification result with LCF and Ricci curvature nonnegative condition. This gives us a very limited case of LCF manifolds. 

Theorem 2.20 (Carron-Herzlich[15]) . Let (M n, g ) be a complete non-compact LCF manifold with Ric( g) ≥ 0. Then (M, g ) is isometric (up to a finite quotient) to Rn, Sn−1 × R, Sn, or a quotient thereof, or globally conformally equivalent to Rn with a conformal non-flat metric with nonnegative Ricci curvature. 

This is the noncompact analog of the cylinder Sn−1 × R. Together, the compact and non-compact examples in this section provide the palette of LCF manifolds that appear as limits and building blocks in the moduli space theory of Chapter 3. 

# 2.5 Moduli Space Analogy: Teichm¨ uller Space 

The study of LCF metrics on a fixed manifold M fits naturally into a broader tradition of parametrizing geometric structures up to equivalence. Before developing the LCF moduli space in Chapter 3, we recall the classical two-dimensional prototype — Teichm¨ uller space — and draw the analogy that motivates the higher-dimensional theory. 56 2.5.1 Teichm¨ uller space of a surface 

Let Σ g denote a closed orientable surface of genus g ≥ 2. A marked complex structure on Σ g

is an equivalence class of pairs (Σ g, J ), where J is a complex structure, under orientation-preserving diffeomorphisms isotopic to the identity. 

Definition 2.11 (Teichm¨ uller space [34, 25]) . The Teichm¨ uller space Tg of genus g ≥ 2 is the space of marked complex structures on Σg:

Tg = (Σ g, J )  Diff 0(Σ g),

where Diff 0(Σ g) denotes diffeomorphisms isotopic to the identity. The moduli space of Rie-mann surfaces is the further quotient 

Mg = Tg

 MCG(Σ g),

where MCG(Σ g) is the mapping class group. 

g = 0 g=1 g=2 

Figure 2.1: Compact Riemann surfaces of genus g = 0, 1, and 2. The Teichm¨ uller space Tg

parametrizes complex (equivalently, constant-curvature) structures on genus-g surfaces. The key metric-geometric content of Tg comes from the Uniformization theorem, which identifies complex structures with constant-curvature metrics. 57 Theorem 2.21 (Uniformization [41, 51]) . Every compact Riemann surface (Σ g, J ) admits a unique (up to scaling) Riemannian metric g0 of constant curvature that is compatible with 

J:

K(g0) = 



+1 g = 0 (S2),

0 g = 1 (T2),

−1 g ≥ 2 (hyperbolic surface ).

In particular, within each conformal class [g0] on Σg there exists a unique unit-area constant-curvature representative. 

Thus Tg can equivalently be viewed as parametrizing unit-area hyperbolic metrics on Σ g (for 

g ≥ 2), or flat metrics for g = 1. One of the central results of two-dimensional geometry is that Tg is homeomorphic to R6g−6 (for g ≥ 2) and carries a natural complex structure [34]. The Deligne-Mumford compactification Mg of Mg is obtained by allowing noded (nodal) surfaces, i.e., surfaces in which simple closed geodesics degenerate to cusps of length zero. The boundary ∂Mg thus consists of lower-complexity Riemann surfaces with orbifold singu-larities. 

## 2.5.2 The LCF moduli space as a higher-dimensional analog 

Remark 2.5 (Analogy to higher dimensions) . The LCF moduli space studied in Chapter 3 is the natural higher-dimensional analog of Tg. The dictionary is as follows. 

The Uniformization theorem (Theorem 2.21) guarantees that within each conformal class on a Riemann surface there is a canonical constant-curvature metric. The Yamabe theorem (Theorem 2.12) plays exactly the same role in higher dimensions: within each conformal class [ g] on a compact Riemannian manifold ( M n, g ), there exists a metric of constant scalar curvature. This is why CSC metrics — rather than LCF metrics per se — are the preferred 58 2D (Riemann surfaces) nD (LCF manifolds, n ≥ 4)

Compact surface Σ g −→ Compact LCF manifold ( M n, [g]) Complex structure J −→ LCF conformal structure [ g], W ≡ 0Conformal class [ g0] −→ Conformal class [ g] with Y (M, [g]) > 0Uniformization theorem −→ Yamabe theorem (Theorem 2.12) Constant-curvature metric −→ CSC (Yamabe) metric in [ g]Teichm¨ uller space Tg −→ LCF moduli space M

Deligne-Mumford compactification −→ TV orbifold compactification (Ch. 3) Noded surface (boundary) −→ LCF orbifold with ALE bubbles Table 2.4: Dictionary between Teichm¨ uller theory and LCF moduli theory. canonical representatives in the moduli space. The Tian-Viaclovsky compactification theorem (Theorem 3.1, stated and proved in §3.1) is the analog of the Deligne-Mumford compactification: it asserts that the moduli space M of unit-volume positive-Yamabe LCF metrics with Ln/ 2 bounded curvature has compact closure in the Gromov-Hausdorff topology, with boundary consisting of compact LCF orbifolds. The bubble limits — the ALE manifolds that appear at concentration points — play the role of the nodal components in ∂Mg.The analogy breaks down in one important respect: whereas Tg ∼= R6g−6 is a finite-dimensional smooth manifold, the LCF moduli space is infinite-dimensional as a na¨ ıve space of metrics. One imposes the curvature bound R 

> M

| Rm |n/ 2 dV g ≤ C precisely to recover pre-compactness (via the ε-regularity Lemma 2.4 and the volume comparison Theorem 2.7), bringing the analogy back into focus. 59 Chapter 3 Locally Conformally Flat Moduli Space 

This chapter presents the original results of the thesis, based on the paper On the locally conformally flat ALE manifolds [69]. The narrative arc is: set up the moduli space compact-ification problem ( §3.1), observe that blow-up limits are ALE manifolds, study LCF ALE manifolds in depth ( §3.2– §3.3), prove the main good-orbifold and classification theorems (§3.4– §3.5), apply those theorems back to describe the moduli space boundary ( §3.6), and close with the Positive Mass Theorem and Yamabe problem for LCF orbifolds ( §3.7). 

# 3.1 The Moduli Space and Tian-Viaclovsky Compact-ification 

Now, we begin to study the moduli space. Let a compact manifold M n (n ≥ 3) carrying a locally conformally flat (LCF) metric of positive scalar curvature. We study the following moduli space. 60 Definition 3.1 (LCF moduli space) . Let [g] be an LCF conformal class on M with Y (M, [g0]) >

0. For constants C > 0, set 

M(n, μ, C ) = (M n, g ) R(g) ≡ 1, Y (M, [g]) ≥ μ > 0, ∥| Rm g |∥ Ln/ 2(M,g ) ≤ C .

Elements of M are regarded up to pull-back by diffeomorphisms isotopic to the identity. 

The Ln/ 2 curvature bound is the conformally invariant analogue of the L2 energy in dimension 4; it controls both regularity and topology. The main compactification result is due to Tian-Viaclovsky [64, 65]. An improvement is done in [69]. 

Theorem 3.1 (Tian-Viaclovsky compactification [64, 65], Wang [69]) . The moduli space 

M(n, μ 0, C ), for some μ0 > 0, has compact closure in the Gromov-Hausdorff topology. Any GH limit is a compact LCF orbifold (M∞, g ∞) with at most finitely many singular points and 

Y (M∞, [g∞]) > 0.Moreover, each singular point p ∈ M∞ has a neighborhood conformally diffeomorphic to a cone Rn/Γp for a finite group Γp ≤ O(n); in particular M∞ is a good orbifold (Theo-rem 3.13). 

Remark 3.1. The good-orbifold assertion uses Theorem 3.13, proved in §3.4 below. The GH limit exists by the Cheeger-Gromov compactness theorem on the regular region provided by Lemma 3.2; its good-orbifold structure is the new contribution of this thesis. 

The proof of compactness rests on two analytic tools: the ε-regularity lemma and the gap lemma, which together control where curvature can concentrate. 

Lemma 3.2 (ε-regularity for LCF metrics (cf. Lemma 2.4) . There exist ε0, C 0 > 0 depending 

61 Gromov-Hausdorff  

> blow up (Mi, g i)(M∞, g ∞)( ˆM∞,ˆM∞)

Figure 3.1: A sequence ( Mi, g i) ∈ M converging in the Gromov-Hausdorff topology to an LCF orbifold ( M∞, g ∞). At each concentration point a rescaled bubble ( ˆM∞, ˆg∞), a non-compact LCF ALE manifold, detaches. 

only on n such that: if (M n, g ) is a LCF manifold with Y (M, [g]) > 0 and 

Z 

> Br(x)

| Rm g |n/ 2 dV g < ε 0,

then sup Br/ 2(x) | Rm g | ≤ C0r−2.Proof sketch. The Kato inequality (Lemma 2.5) gives ∆ | Ric | ≥ − C| Rm || Ric |. Combined with a Moser iteration using the Calder´ on-Zygmund estimate (Theorem 1.3) on Ln/ 2 balls, this yields the pointwise bound. The LCF condition W ≡ 0 ensures | Rm | ≤ C| Ric |, closing the iteration. See [64] for the complete argument. Using Lemma 3.2, we can prove the following energy gap lemma. 

Lemma 3.3 (Gap lemma) . There exists ε1 > 0 such that: if (M n, g ) is a complete LCF 

62 manifold with R 

> M

| Rm g |n/ 2 dV g < ε 1, then g is flat. Proof. Apply Lemma 3.2 with r → ∞ : the pointwise curvature bound sup Br | Rm | ≤ 

C0r−2 → 0 forces Rm ≡ 0, hence g is flat. By these two lemmas, curvature concentration in any sequence gi ∈ M can occur at only finitely many points (where R 

> Br

| Rm |n/ 2 ≥ ε0 for every r > 0). At each such concentration point the following blow-up analysis applies. 

Lemma 3.4 (ALE blow-up lemma) . Let (Mi, g i) ∈ M be a sequence with a concentration point xi → x∞. Set ri = | Rm gi (xi)|−1/2 → 0. Then the rescaled sequence (Mi, r −2 

> i

gi, x i) has a subsequence converging in C∞ 

> loc

to a complete non-compact LCF ALE orbifold (Σ , g Σ, x ∞)

with 

Z

> Σ

| Rm gΣ |n/ 2 dV gΣ < ∞, | Rm gΣ (x∞)| = 1 .

Proof. Rescaling normalizes curvature at xi to 1. The Ln/ 2 bound and the TV volume com-parison (Theorem 2.7) give volume non-collapse and ALE asymptotics at infinity. Cheeger-Gromov compactness (Theorem 1.7) then yields a C∞ 

> loc

limit, which inherits W ≡ 0. At a different scaling scale, we can use these two lemmas to conclude the curvature concen-tration region will look like the ALE model. 

Theorem 3.5 (Finite bubble tree structure) . Let (Mi, g i) ∈ M be a sequence converging in the Gromov-Hausdorff sense to (M∞, g ∞), and let S ⊂ M∞ be the finite set of concentration points. There exists a finite rooted tree T — the bubble tree — with the following properties: (i) The root node corresponds to (M∞, g ∞).(ii) Each non-root node corresponds to a complete non-compact LCF ALE orbifold (Σ α, g α)63 with R 

> Σα

| Rm gα |n/ 2 dV < ∞.(iii) Each leaf node corresponds to a complete non-compact smooth LCF ALE manifold. (iv) Each edge of T connects a parent node to a child node via a neck region diffeomorphic to (Sn−1/Γ) × (0 , 1) for a finite group Γ ≤ O(n).(v) The total number of non-root nodes is at most C/ε 1, where C is the Ln/ 2 curvature bound in M and ε1 is the gap constant of Lemma 3.3. (vi) In particular, a neighborhood of singular point is diffeomorphic to an ALE manifold. Proof. We use the bubble tree scaling argument of Bando [9]; see also [66]. 

Step 1: First-level bubbles (children of the root). Fix x ∈ S and let xi → x with B(xi, r ) →

B(x, r ) in the Gromov-Hausdorff sense. Choose r∞ > 0 small enough that sup 

> B(xi,r ∞)

| Rm( gi)| = | Rm( gi)|(xi) → ∞ ,

Z

> B(x,r ∞)

| Rm( g∞)|n 

> 2

dv ≤ ε0

2 ,

where ε0 is the constant from Lemma 3.2. Denote A(r1, r 2) = B(x, r 2) \ B(x, r 1). Choose r(i) < r ∞ such that 

Z

> Ai(r(i),r ∞)

| Rm( gi)|n 

> 2

dv = ε0.

Since curvature concentrates at x, we have r(i) → 0, so for i large and any fixed 0 < r 0 < r ∞

we have r(i) < r 0.

Neck region. For any fixed r0 ∈ (0 , r ∞) the annulus Ai(r0, r ∞/2) lies entirely above scale 

r(i), so R 

> Ai(r0,r ∞/2)

| Rm |n/ 2 < ε 0. Lemma 3.2 then gives a pointwise curvature bound on 

Ai(r0, r ∞/2); the LCF condition W ≡ 0 promotes this via the elliptic system for Ricci 64 curvature to C∞ convergence ( Ai(r0, r ∞/2) , g i) C∞

−−→ (A∞(r0, r ∞/2) , g ∞), and the neck is diffeomorphic to ( Sn−1/Γx) × (0 , 1). 

First bubble. Consider the rescaled sequence ( Mi, r (i)−2 gi, x i). In the rescaled metric the annulus Ai(r(i), r ∞) becomes Ai(1 , r ∞/r (i)), which exhausts A(1 , ∞) as r(i) → 0. By the choice of r(i), the Ln/ 2 curvature energy in this region is exactly ε0; applying Lemma 3.2 ball by ball outside B1 gives a uniform curvature bound there, while the total Ln/ 2 energy bound on all of ( Mi, r (i)−2gi) and the TV volume comparison (Theorem 2.7) ensure volume non-collapse and ALE asymptotics at infinity. Thus ( Mi, r (i)−2 gi, x i) subconverges in C∞

> loc

to a complete LCF ALE orbifold (Σ (1) , g (1) ) with R 

> Σ(1)

| Rm g(1) |n/ 2 dV < ∞.

Step 2: Iterated blow-up. The first-level bubble Σ (1) may itself have curvature concentration points, corresponding to additional scales of blow-up inside B(xi, r (i)) that are not resolved at scale r(i). At any such concentration point y ∈ Σ(1) , let yi ∈ Mi be a sequence of points with yi → y in the rescaled metric r(i)−2gi. Define ρ(i) < R ∞ (for a suitably chosen R∞ > 0in the rescaled coordinates) by 

Z 

> A(1)
> i(ρ(i),R ∞)

| Rm( r(i)−2gi)|n 

> 2

dv r(i)−2gi = ε0,

where A(1)  

> i

denotes the annulus in the rescaled metric centered at yi. Since r(i)−2gi is itself a rescaling of gi, the further rescaling ρ(i)−2(r(i)−2gi) is equivalent to working at the combined scale r(i)ρ(i) in the original metric gi. The same argument as Step 1 shows that ( Mi, (r(i)ρ(i)) −2 gi, y i) subconverges to a second-level LCF ALE orbifold (Σ (2) , g (2) ), connected to Σ (1) by a neck ( Sn−1/Γy) × (0 , 1). We continue inductively: at each level k,any concentration point of Σ (k) yields a scale r(k)(i) → 0 in the level-k rescaled metric, and the combined scale produces the next bubble Σ (k+1) .

Step 3: Finiteness and smooth leaf nodes. By Lemma 3.3, every non-flat complete LCF manifold satisfies R | Rm |n/ 2 dV ≥ ε1. Each bubble Σ (k) at any level is a distinct non-65 flat limit contributing at least ε1 to the total Ln/ 2 energy of the original sequence, and these contributions are disjoint (they arise from disjoint scales and regions). Since the total energy is bounded by C, the tree T has at most C/ε 1 non-root nodes, and the induction terminates in finitely many steps. At a leaf node Σ (k), no further concentration points exist, so the rescaled sequence at that level has uniformly bounded curvature everywhere. In particular, there are no interior orb-ifold points (which would correspond to further blow-ups), and Σ (k) is a smooth complete LCF ALE manifold. Lemma 3.4 shows that LCF ALE manifolds and orbifolds are the fundamental building blocks of the moduli space boundary. We now study their structure in depth. The key tools are the totally umbilic geometry of ALE ends, the harmonic expansion of the conformal factor, and the injectivity of the end group — all developed in §3.2– §3.3. 

# 3.2 Locally Conformally Flat ALE Manifolds 

The blow-up limits produced by Lemma 3.4 are non-compact LCF ALE manifolds (or orb-ifolds). In this section we analyze their end structure using the developing map as the central tool. Recall Definition 1.6: an ALE manifold of order τ > 0 has an end diffeomorphic to (Rn \ B)/Γ with Γ ≤ O(n) finite and gij = δij + O(r−τ ), ∂mgij = O(r−τ −| m|). 

Definition 3.2 (LCF ALE manifold) . A LCF ALE manifold is a complete Riemannian manifold (M n, g ) that is both locally conformally flat (Definition 2.1) and asymptotically locally Euclidean (Definition 1.6). 

66 3.2.1 Totally umbilic submanifolds 

To study the conformal embedding, we need to understand the conformal invariant geometric objects. Motivated by this, we study the conformal invariant submanifolds. 

Definition 3.3 (Totally umbilic submanifold) . A hypersurface N n−1 ⊂ (M n, g ) is totally umbilic if II x = λ(x) g|N for some λ ∈ C∞(N ).

Totally umbilic submanifolds are conformally invariant: under a conformal change ˆ g = e2ψg,the second fundamental form transforms as 

bII( X, Y ) = II( X, Y ) − ˆg(X, Y ) ∇ψ normal ,

so umbilic points are preserved. It can be easily seen that the totally umbilic submanifolds are invariant under conformal change. Note that this invariance is pointwise, i.e., the umbilic points are invariant under conformal change. For ( M, g ), if there is a conformal embedding ϕ : M → Sn, and ( M, g ) is not conformally equivalent to ( Sn, g Sn ), then by the stereographic projection, we have a conformal embedding ¯ϕ : M → Rn. Thus, all the totally umbilic submanifolds in ( M, g ) are totally umbilic in Rn,which gives a very strong constraint. Recall the classical theorem of totally umbilic submanifolds in Rn. This is an old theorem that dates back to Cartan. Since it is difficult to find the precise reference, we include the proof as well. 

Theorem 3.6 (Totally umbilic hypersurfaces in Rn). Let n ≥ 3. The only closed totally umbilic hypersurfaces in Rn are round spheres Sn−1(r).

67 Proof. Let i : N , → Rn be a closed totally umbilic hypersurface with II = λg |N .

Step 1: λ is constant. By the Codazzi equation, for tangential vector fields X, Y, Z on N :(∇X II)( Y, Z ) = ( ∇Y II)( X, Z ).

Since II = λg |N , the left side equals ( Xλ )g(Y, Z ) and the right side equals ( Y λ )g(X, Z ). Setting Y = Z to a unit vector perpendicular to X gives ( Xλ ) = 0 for all X tangent to N ,so λ is constant on N .

Step 2: Identifying the center. For λ > 0, define 

c := i(x) + 1

λ⃗ ν(x),

where ⃗ν is the unit inward normal. Then for any tangential X:

∇X c = ∇X i + 1

λ∇X⃗ν = X − 1

λA(X) = X − 1

λ(λX ) = 0 ,

using A(X) = λX (since II( X, ·) = λg (X, ·)). Hence c is a constant vector (the center), and 

|i(x) − c| = 1 /λ for all x ∈ N . Thus i(N ) ⊂ Sn−1(1 /λ ). Since N is a closed connected hypersurface inside this sphere and has the same dimension, i(N ) = Sn−1(1 /λ ). Combined with Theorem 2.10, we have, if ( M, g ) is an LCF manifold with non-negative scalar curvature, then the only closed totally umbilic submanifolds in the universal covers are the conformal round spheres. 

Remark 3.2. In the ALE setting, the large coordinate spheres ∂B r/Γ ∼= Sn−1/Γ become asymptotically totally umbilic as r → ∞ . By the conformal invariance in Definition 3.3, their images under the developing map ϕ : ˜M → Sn are asymptotically round spheres. This is the key geometric observation exploited throughout this section. 

68 The totally umbilic structure of large coordinate spheres is a qualitative constraint: it tells us the shape of the ALE end in the developing map image. To get quantitative control on the conformal factor and ultimately to read off the ADM mass, we need the asymptotic expansion of harmonic functions on ALE manifolds. 

## 3.2.2 Harmonic functions on ALE manifolds 

Now, we recall the theory of harmonic functions in ALE manifolds. This is very similar to the case of Lemma 1.4. 

Theorem 3.7 (Harmonic expansion on ALE manifolds [22]) . Let (M n, g ) be an ALE mani-fold of order τ > 0, and let u be a bounded function that satisfies ∆gu = 0 outside a compact set on one ALE end. Then u has an asymptotic expansion on that end: 

u(x) = c + A r 2−n + O(r2−n−ε),

as r = d(x, o ) → ∞ , for constants c, A ∈ R and some ε > 0. The same statement holds for the equation ∆u + κS gu = 0 (with Sg ∈ O(r−2−τ )). Proof. We decompose u = u0 + u1 on the ALE end outside a compact set, where u0 satisfies ∆Rn/Γu0 = 0 and u1 = O(r−ε). This decomposition is achieved by solving the Poisson equation for the metric perturbation term in a weighted Sobolev space: since gij − δij ∈

O(r−τ ), the operator ∆ g − ∆Rn is a lower-order perturbation with decay, and the L2-theory on ALE spaces (using the weighted Sobolev embedding) gives u1 ∈ O(r−ε) for some ε > 0depending on τ .For the Euclidean part u0: bounded harmonic functions on Rn/Γ lift to bounded harmonic functions on Rn \ B. By Lemma 1.4 (spherical harmonic expansion on Rn), every bounded harmonic function outside a ball expands as u0 = c + P 

> ℓ≥0

hℓ, where hℓ is a spherical 69 harmonic of degree ℓ times r2−n−ℓ (for ℓ ≥ 1) or a constant (for ℓ = 0). The only term that can fail to decay as r → ∞ with rate better than r2−n is the ℓ = 0 mode. Hence 

u0 = c + Ar 2−n + O(r2−n−1). Iterating the estimate on u1 with the Calder´ on-Zygmund estimate (Theorem 1.3) on successive annuli gives the stated ε > 0. The harmonic expansion of Theorem 3.7 provides the precise asymptotics of the conformal factor at each ALE end. Combining this with the totally umbilic sphere argument, we can now show that every LCF ALE manifold with non-negative scalar curvature is actually AE: the group Γ at each end must be trivial. 

## 3.2.3 LCF ALE manifolds are AE 

Now, we can prove the main theorem for LCF ALE manifolds structure. 

Theorem 3.8 (LCF ALE manifolds are AE) . Let (M n, g ) be a LCF ALE manifold with 

Rg ≥ 0. Suppose the universal cover ˜M admits a conformal embedding ϕ : ˜M , → Sn. Then 

(M, g ) is asymptotically Euclidean (AE): every ALE end has trivial group Γ = {e}.Proof. Without loss of generality assume ( M, g ) has one ALE end with group Γ ≤ O(n). We produce a totally umbilic Sn−1/Γ inside ( M, g ) for large scales, then apply Theorem 3.6 to force Γ = {e}.

Step 1: Conformal factor. Since ϕ(M ) ⊊ S n, pick p ∈ Sn \ ϕ(M ) and apply stereographic projection πp : Sn \ { p} → Rn. The composition ¯ϕ = πp ◦ ϕ : M → Rn is a conformal embedding with ¯ϕ∗(gRn ) = u4/(n−2) g for some u ∈ C∞(M ), u > 0. Since Rg ≥ 0, the function u satisfies 

−∆gu + anRgu = 0 , an = n−24( n−1) ,

with u bounded away from a fixed base point. By Theorem 3.7 (applied to the equation 70 ∆u + anSu = 0 with S = O(r−2−τ )), on the ALE end: 

u = r2−n + O(r2−n−ε), ε > 0,

after normalizing so that the leading coefficient A = 1. 

Step 2: Conformal comparison on an annulus. Fix R ≫ 1 and consider the annular region in the ALE chart: 

Ag(R, 4R) = {x ∈ M : R ≤ dist g(x, z ) ≤ 4R}.

In the inverted coordinate ρ = 1 /r and conformal metric ˆ g = r−4g, we have Ag(R, 4R) = 

Aˆg(1 /(4 R), 1/R ). Adding the compactification point x0 (corresponding to the end), the metric g0 = u4/(n−2) g satisfies 

g0 = (1 + O(ρε))ˆ g near x0,

so ( B(x0, δ ), g 0) ⊂ (Rn/Γ, g flat ) is part of the flat cone with vertex at x0.

Claim : For R large enough, there is a conformal embedding of A(2 R, 3R) ⊂ (Rn/Γ, g flat )into ( Ag(R, 4R), g ). 

Proof of Claim : The ratio of the two distance functions q(x) = dist g0 (x, x 0)/ dist ˆg(x, x 0) is continuous on B(x0, δ ) \ { x0} with lim x→x0 q(x) = 1. Hence there exists η(δ) → 0 such that (1 − η(δ)) ρ ≤ dist g0 (x, x 0) ≤ (1 + η(δ)) ρ for x ∈ B(x0, δ ). For R = 1 /δ large enough, the claim follows. 

Step 3: Totally umbilic sphere. On the flat cone ([2 R, 3R] × Sn−1/Γ, dt 2 + t2gSn−1/Γ), 71 the hypersurface {5R/ 2} × Sn−1/Γ has second fundamental form II = 2

t g {5R/ 2}× Sn−1/Γ = 45R g {5R/ 2}× Sn−1/Γ,

so it is totally umbilic. Since totally umbilic submanifolds are conformally invariant (Defini-tion 3.3), the conformal embedding of Step 2 transfers this to a totally umbilic N ∼= Sn−1/Γinside ( Ag(R, 4R), g ). 

Step 4: Contradiction unless Γ = {e}. By the Schoen-Yau embedding (Theorem 2.10), 

ϕ(N ) is a totally umbilic submanifold of Sn, hence a round sphere Sn−1 (the M¨ obius image of a totally umbilic sphere remains a sphere). Since N ∼= Sn−1/Γ is the quotient of a sphere by Γ, and ϕ(N ) ∼= Sn−1, we need Sn−1/Γ ∼= Sn−1, which forces Γ = {e}. Repeating for each ALE end completes the proof. 

(Ag(R, 4R), g )

ψ : E → Rn/Γ

# (M,g) (Rn/Γ, g f lat )

Figure 3.2: An ALE manifold ( M, g ) and its end E, diffeomorphic to ( Rn \ B)/Γ. The two colored curves are large coordinate spheres that become totally umbilic under the conformal map ¯ϕ : M → Rn.Theorem 3.8 shows that every universal cover of an ALE manifold has trivial group: each ALE end is actually AE. It follows that the AE ends of the universal cover, under the developing map, all converge to isolated points in Sn. We now use this to give a global 72 description of the universal cover. 

## 3.2.4 Universal cover as a domain in Sn

In addition, we can prove the following structure theorem for the universal cover of the LCF, ALE manifolds. 

Proposition 3.9 (Universal cover of a LCF ALE manifold) . Let (M n, g ) be a LCF ALE manifold with Rg ≥ 0. The universal cover ˜M is diffeomorphic to Sn \ (Λ ∪ I), where Λ ⊂ Sn

is the limit set of Γ = ρ(π1(M )) and I is a discrete set of points corresponding to the AE ends of ˜M .Proof. By Theorem 2.10, the developing map gives a conformal embedding ϕ : ˜M , → Sn. By Theorem 3.8, every ALE end of ˜M is actually AE (trivial group at infinity). 

Step 1: One-point compactification of each end. Fix an AE end. For each k ≥ 1, consider the annulus 

Ak = {x ∈ ˜M : kr ≤ dist( x, z ) ≤ (k + 1) r}.

By the AE condition and the ALE chart, the slice {(k + 12 )r} × Sn−1 is C1,α -close to a round sphere for large k. Applying the totally umbilic argument from the proof of Theorem 3.8, there exist totally umbilic spheres Nk ∼= Sn−1 in Ak. Let Ck ⊂ ˜M be the compact region bounded by Nk (containing the base point z); then C1 ⊂ C2 ⊂ · · · exhausts the end. 

Step 2: Convergence to a point. Under ϕ, the images Sk = ϕ(Nk) ∼= Sn−1 are pairwise disjoint round spheres in Sn with ϕ(Ck) ⊂ ϕ(Ck+1 ). By Theorem 2.7 of [59] applied to the developing map, lim k→∞ rad( Sk) = 0. Hence T 

> k

ϕ(Cck) is a single point {xi} ∈ Sn: the AE end converges to xi.73 Step 3: Compactified universal cover. Adding the compactification points, set 

M = ϕ( ˜M ) ∪ { xi : i ∈ I},

with the spherical metric. By van Kampen’s theorem and n ≥ 3, adding finitely many isolated points does not change simple connectivity, so M is simply connected. The deck transformation group Γ extends to a properly discontinuous action on M .Since Γ acts properly discontinuously on Sn \ Λ, we have ϕ( ˜M ) ⊂ Sn \ Λ. Each compactifi-cation point xi satisfies xi /∈ Λ: if xi ∈ Λ, it would be a limit of orbit points, but the AE end converges to xi non-periodically, contradicting proper discontinuity. Hence ˜M ∼= Sn \ (Λ ∪ I), where I = {xi} is discrete. 

# 3.3 Structure Theory of LCF ALE Manifolds and Orb-ifolds 

Having embedded the universal cover ˜M as a domain in Sn (Proposition 3.9), we now analyze the Kleinian group action on that domain. The main results are the injectivity theorem (Theorem 3.10) and the manifold cover (Proposition 3.12). 

## 3.3.1 Injectivity theorem 

Theorem 3.10 (Injectivity of the end group [69]) . Let (M n, g ) be a complete LCF ALE manifold with Rg ≥ 0, and let Ek be an ALE end with group Γk ≤ O(n). Then the inclusion 

ik : Ek ,→ M induces an injective homomorphism 

(ik)∗ : Γ k ,→ π1(M ).

74 Proof. Consider 

Sr = {x : x in the k-th end , dist( x, z ) = r}

to be the distance sphere. For r large enough, ( Sr, j ∗g/r 2) and ( Sn−1/Γk, g Sn−1/Γk ) are C1,α -close by the ALE condition, so Sr ∼= Sn−1/Γk and π1(Sr) ∼= Γ k. (Here j∗g denotes the pullback metric under j : Sr ,→ M in the tangential directions.) Let ( ˜M , p ∗g) be the Riemannian universal cover with covering map p : ˜M → M . Choose 

z0 ∈ p−1(z); by lifting geodesics from z0, we obtain a lift ˜Sr ⊂ ˜M of Sr, and p| ˜Sr : ˜Sr → Sr

is a covering map. By Proposition 3.9, ˜M has only AE ends (trivial group), so for r large, ˜Sr lies inside an AE end of ˜M and is C1,α -close to the round sphere; hence ˜Sr ∼= Sn−1. Since 

π1( ˜Sr) = {e}, ˜Sr is the universal cover of Sr.Now let γ ∈ ker( ik)∗ ≤ Γk ∼= π1(Sr). Since ( ik)∗(γ) is trivial in π1(M ), any loop ℓ ⊂ Sr

representing γ is null-homotopic in M . Hence γ acts trivially as a deck transformation of ˜M , and the lift ˜ℓ ⊂ ˜Sr of ℓ is a closed loop. Since π1( ˜Sr) = π1(Sn−1) = {e} for n ≥ 3, ˜ℓ is null-homotopic in ˜Sr, so ℓ is null-homotopic in Sr, giving [ γ] = e in π1(Sr) = Γ k. Therefore (ik)∗ is injective. 

## 3.3.2 Local isotropy groups 

In particular, for each γ ∈ Γk < π 1(M ), acting as a deck transformation, it fixes the com-pactification point xk. It therefore induces a conformal map on a small ball Bϵ centered at xk, and by the Liouville theorem (Theorem 2.9) this map extends uniquely to a M¨ obius transformation fixing xk. Thus: 

Corollary 3.11. For each Γk < π 1(M ), the holonomy image satisfies ρ(Γ k) < C (n), and 

ρ(Γ k) fixes {xk}, where C(n) is the conformal group of Sn.

75 Note that the action ρ(π1(M )) extends to the conformal compactification M . Moreover, this action is properly discontinuous, so 

M ′ := M /ρ (π1(M )) is a compact orbifold (cf. Definition 1.3). In particular, 

M ′ = M ∪ { x1, . . . , x m},

which is the one-point compactification of each end of M . Since M ′ is a quotient of the manifold M , it is a good orbifold with each local group Γ i injecting into π1(M ). Since M = Ω /Γ for some open set Ω ⊆ Sn and a discrete group Γ ≤ C(n) (Definition 2.5), we say that M ′ is a Kleinian orbifold (see §2.1). Thus, M ′ is a Kleinian orbifold. 

## 3.3.3 Finite manifold cover 

Now, apply Selberg’s lemma (Theorem 2.11), we have the following fact about Kleinian orbifold. 

Proposition 3.12 (Existence of a manifold cover) . Let M ′ be a good Kleinian orbifold. Then there exists a compact Kleinian manifold N such that 

p : N → M ′

is a finite covering map. Proof. Since M = Ω /Γ for some open set Ω ⊆ Sn and Γ ≤ C(n), by Theorem 2.11 there exists a normal subgroup H ⊴ Γ of finite index that is torsion-free. Note that a torsion-free element of C(n) acts without fixed points (Definition 2.6). Thus H acts freely on Ω, and the 76 quotient N ∼= Ω /H is a compact smooth manifold whose fundamental group is isomorphic to H. The covering map N → M ′ ∼= Ω /Γ has finite degree [Γ : H] < ∞.

# 3.4 The Good Orbifold Theorem 

Now, we link the geometry of LCF orbifolds with positive scalar curvature with ALE man-ifolds of nonnegative scalar curvature. In the following, we show that the conformal com-pactification of the nonnegtative scalar curvature, LCF, ALE manifolds is a compact LCF orbifold with positive Yamabe invariant, assembling the results of §3.2– §3.3. 

Theorem 3.13 (Good orbifold theorem) . Every compact LCF orbifold (M n, g ) with Rg > 0

and n ≥ 3 is a good orbifold: there exists a smooth compact manifold ˜M and a finite group 

Γ acting smoothly and freely on ˜M with M ∼= ˜M / Γ.Proof. Let {xi}mi=1 be the orbifold singular points of M .

Step 1: Conformal blow-up. Since Rg > 0, the conformal Laplacian Lg = −an∆g + Rg

(with an = 4( n − 1) /(n − 2)) is positive. For each orbifold singular point xi, there exists a positive Green’s function Gi for Lg with pole at xi. The superposition G = P 

> i

Gi > 0 gives a conformal metric ˜g = G 4 

> n−2

g

on M \ { xi}. Near each xi, the Green’s function has a pole; pulling back to the local orbifold chart Rn/Γxi , the blown-up metric ( B(xi, ε ) \ { xi}, ˜g) is a complete ALE orbifold end with group Γ xi and order n − 2 (see Corollary 3.14). Thus ( M \ { xi}, ˜g) is a multi-ALE manifold of order n − 2, and πorb 1 (M ) ∼= π1(M \ { xi}). 

Step 2: Injectivity of local isotropy. By Proposition 3.9 applied to the multi-ALE man-77 ifold ( M \ { xi}, ˜g), the universal cover ^M \ { xi} embeds as a domain in Sn. By Theorem 3.10 and Corollary 3.11, each local isotropy group Γ xi injects into π1(M \ { xi}) ∼= πorb 1 (M ). 

Step 3: Kleinian good orbifold. By the orbifold goodness criterion [63], an orbifold is good if and only if each local isotropy group injects into the orbifold fundamental group. Step 2 provides exactly this injectivity, so M is a good Kleinian orbifold: M = Ω /Γ for a domain Ω ⊂ Sn and a discrete group Γ ≤ C(n). 

Step 4: Smooth manifold cover. By Proposition 3.12 (Selberg lemma), there exists a finite-index torsion-free normal subgroup H ⊴ Γ, and the quotient N = Ω /H is a smooth manifold covering M with finite degree [Γ : H] < ∞.

Corollary 3.14 (Optimal ALE decay) . Let (M n, g ) be a LCF scalar-flat ALE manifold of order τ > 0. Then there exist charts at infinity for every end in which 

gij = δij + O(r−(n−2) ), ∂mgij = O(r−(n−2) −| m|),

i.e. (M, g ) is ALE of order n−2. If (M, g ) has Rg ≥ 0, then a conformal metric ˜g = u4/(n−2) g

exists that is scalar-flat and ALE of order n − 2.Proof. Since Rg = 0 and ( M, g ) is LCF, the conformal Laplacian is Lg = −an∆g. By Theorem 3.15 (proved below), ( M, g ) conformally compactifies to a compact LCF orbifold ( ˆM , ˆg) with Y ( ˆM , [ˆ g]) > 0. On ( ˆM , ˆg), the conformal Green’s function Gp at a singular point p admits the expansion (using the LCF condition to eliminate the logarithmic term; see Lemma 6.4 of [45]): 

Gp = r2−n + A + O(r), r = dist ˆg(·, p ),

without any log r correction. The conformal factor u = G1/(n−2)  

> p

then satisfies u = r(2 −n)/(n−2) (1+ 78 O(r2)), which translates back to an ALE decay rate of order n − 2 in the original chart at infinity. 

# 3.5 Classification Results 

We now classify LCF ALE manifolds and compact LCF orbifolds using the structure theory of §3.2– §3.4. The strategy in each case is the same: use the good-orbifold theorem and conformal compactification to reduce to a compact problem, then apply known results from topology and conformal geometry. The three main results are: conformal compactification (Theorem 3.15), the pairing of orbifold points (Theorem 3.17), and the dimension-specific diffeomorphism type. 

## 3.5.1 Conformal compactification and Yamabe invariant 

Theorem 3.15 (Conformal compactification) . Let (M n, g ) be a complete LCF ALE manifold with Rg ≥ 0. Then (M, g ) conformally compactifies to a compact LCF orbifold ( ˆM , ˆg) with 

Yorb ( ˆM , [ˆ g]) > 0.Proof. Without loss of generality assume ( M, g ) has one ALE end with group Γ ≤ O(n). We construct the compactification in two steps. 

Step 1: Inverted metric. Fix z ∈ M and let r(x) = dist g(x, z ). Define the inverted metric ˆg = r−4g; in the inverted coordinate ρ = 1 /r , the ALE condition gives ˆ g = δ + O(ρτ ) near the compactification point x0 = {r = ∞} . Thus a neighborhood of x0 in ( M ∪ { x0}, ˆg) is isomorphic to a ball B(0 , ε )/Γ ⊂ Rn/Γ with an isolated orbifold point at the origin. 

Step 2: Positive Yamabe invariant. We use the PMT for LCF ALE orbifolds (Theo-rem 3.27, proved in §3.7): mADM (M, g ) ≥ 0. The conformal compactification ˆM = M ∪ { x0} carries the LCF conformal structure [ˆ g]. 79 For the Yamabe invariant, choose the conformal Green’s function Gx0 for Lˆg at x0. Its expansion near x0 reads Gx0 = cρ 2−n +mADM +O(ρ) (after normalizing by a positive constant 

c depending on n and Γ). Since mADM ≥ 0 and Gx0 > 0, the Schoen argument (as in [59]) shows: 

Yorb ( ˆM , [ˆ g]) ≥ 0.

Strict positivity Yorb > 0 follows from mADM > 0 (which holds unless ( M, g ) is flat, in which case ˆM is a spherical space form with Y > 0 anyway) or by a direct check using the positivity of Rˆg.The conformal compactification theorem reduces all questions about ALE ends to questions about orbifold points of a compact LCF orbifold with positive Yamabe invariant. The next key fact about such orbifold points is their pairing structure, which follows from the orientability of the developing map image. 

## 3.5.2 Local isotropy and paired orbifold points 

To study the local isotropy subgroups, we first show that we can conjugate the local group Γi to be a subgroup of O( n). 

Lemma 3.16 (Local isotropy conjugates into O(n)) . Let (M n, g ) be a compact LCF orbifold with Y > 0 and let p ∈ M be an orbifold point with local isotropy group Gp. Then ρ(Gp) ≤

C(n) is conjugate to a finite subgroup of O(n).Proof. By Corollary 3.11, ρ(Gp) fixes a single point p′ ∈ Sn. The stabilizer in C(n) of a point 

p′ ∈ Sn is, after conjugating so that p′ = ∞ (the north pole in the stereographic model), the 80 group of similarities: 

C(n)p′ = {x 7 → αU x + b : α > 0, U ∈ O(n), b ∈ Rn} ∼= O(n) ⋉ (R>0 × Rn).

A finite subgroup of C(n)p′ has no elements of infinite order, so its dilation part α must equal 1 (otherwise αk → 0 or ∞, giving an infinite-order element). Hence ρ(Gp) maps to 

O(n) ⋉ R n with α = 1. But a finite subgroup of the Euclidean group O(n) ⋉ R n with a fixed point (here p′, the pre-image of ∞) must be conjugate into O(n) (since fixing b = 0 without loss of generality after translating the fixed point to the origin). For a subgroup Γ ≤ O( n) acting on Sn, if it has a fixed point, it fixes the antipodal point as well. It seems that the non-trivial orbifold points must appear in pairs. This will be the case if this subgroup does not contain parabolic elements. 

Theorem 3.17 (Orbifold points come in pairs) . Let (M n, g ) be an oriented compact LCF orbifold with Y > 0. Assume there are no parabolic elements in Γ and dim H Λ < (n −

2) /2. Then the orbifold singular points decompose into pairs of antipodal fixed-point sets; in particular the total number of orbifold points is even. Proof. Proved in Appendix B. 

Corollary 3.18 (Orientable ALE ends come in pairs) . Let (M n, g ) be an orientable LCF ALE manifold. If π1(M ) contains no parabolic element, then the ALE ends with non-trivial group Γ̸ = {1} appear in pairs. Proof. Let M ′ be the conformal compactification of M . By Theorem 3.15, Yorb (M ′) > 0. By Proposition 3.12, there exists a compact manifold cover N → M ′, and the positive orbifold Yamabe constant passes to Y (N ) > 0. By Proposition 4.7 of [59], dim H(Λ) ≤ (n − 2) /2, and since Y (N ) > 0, Corollary 3.4 of [47] gives the strict inequality dim H(Λ) < (n − 2) /2. Since 81 π1(M ) has no parabolic element, Theorem 3.17 applies, and the orbifold singular points of 

M ′—which correspond to the non-trivial ALE ends of M —appear in pairs. With the pairing result in hand, we can now state the dimension-specific diffeomorphism classification. In dimensions 3 and 4, the LCF and PSC conditions together leave only a small list of possible topological types, determined by Perelman’s geometrization (dimension 3) and Hamilton’s PIC classification (dimension 4). 

## 3.5.3 Dimension-specific classification 

Now, we obtain some classification theorems of the orbifolds in low dimensions. Thus, we also classify the ALE spaces in these cases. 

Theorem 3.19 (3D classification of compact LCF orbifolds with PSC) . Let (M 3, g ) be a compact LCF orbifold with Y > 0. Then M is a good orbifold covered by a spherical space form S3/Γ or a connected sum #k(S2 × S1). In particular, it is conformal equivalent to the connected sum of the quotients S3/Γ and S1 × S2/Γ, i.e., 

M ∼= S3/Γ1#S3/Γ2#... S3/Γk#S2 × S1/Γ′

> 1

#... S2 × S1/Γ′

> m

,

where all the orbifold points are Z2-quotient singularities. Proof. By Theorem 3.13, M is a good orbifold with a finite smooth manifold cover ˜M 3.Since ˜M has positive scalar curvature (inherited via the finite cover), by Theorem 2.18 (the 3D LCF classification of §2.4.3), ˜M is diffeomorphic to a spherical space form or a connected sum # k(S2 × S1). Quotienting by the finite deck group gives the stated orbifold forms. For the conformal connected sum: note the above decomposition can be viewed as the connected sum of orbifolds near the manifold points. Thus, we can apply Theorem 2.7 from [35]. 82 Theorem 3.20 (4D classification of compact LCF orbifolds with PSC) . Let (M 4, g ) be a compact LCF orbifold with Y > 0. Then a finite smooth manifold cover of M is diffeomorphic to S4 or a connected sum #k(S1 × S3) for some k ≥ 0. In particular, it conformal equivalent to the connected sum of the quotients S4/Γ and S1 × S3/Γ, i.e., 

M ∼= S4/Γ1#S4/Γ2#... S4/Γk#S3 × S1/Γ′

> 1

#... S3 × S1/Γ′

> m

.

Proof. Theorem 3.13 provides a finite smooth manifold cover ˜M 4 with R > 0. In dimension 4, the LCF condition ( W = 0) combined with R > 0 implies positive isotropic curvature (PIC); see [33]. Hamilton’s classification of closed 4-manifolds with PIC [33] states that any such manifold is diffeomorphic to S4 or a connected sum # k(S1 × S3), k ≥ 1 (cf. Theorem 2.19). In particular, CP 2 does not arise, since it does not admit a metric of positive isotropic curvature. The rest of the argument just follows the 3D case. As a consequence of our 4D result, we can refined the result of [20]. 

Corollary 3.21 (Positive isotropic curvature in 4D) . A 4D compact LCF orbifold with pos-itive isotropic curvature and Y > 0 has a finite manifold cover diffeomorphic to a connected sum #k(S1 × S3), k ≥ 0.Proof. By Theorem 3.13 and Proposition 3.12, there is a finite smooth manifold cover ˜M 4.Positive isotropic curvature is preserved under finite covers. Hamilton’s theorem [33] classifies closed 4-manifolds with PIC as connected sums # k(S1 × S3) (after passing to a finite cover if necessary; in our case the cover is already smooth). 

Remark 3.3. The corollary a priori seems to have nothing to do with LCF metrics. The connection is pointed out by [20], namely: a compact four-orbifold with at most isolated singularities admits positive isotropic curvature if and only if it admits an LCF metric with positive scalar curvature (Corollary 2 in [20]). Since the conclusion is topological, we work 

83 on its LCF metric. 

In low dimension, we have the following corollary about the ALE ends in dimension 3 or 4. 

Corollary 3.22 (ALE ends in dimensions 3 and 4) . For n = 3 or 4, the ends of an orientable LCF ALE manifold (M n, g ) with Rg ≥ 0 are either groups for the ALE ends are trivial (trivial group) or appear in antipodal pairs corresponding to orbifold points of the conformal compactification. In particular, when n = 3 , orientable LCF ALE manifold with Rg ≥ 0 is Asymptotically flat (trival group). Proof. Apply Theorem 3.15 to compactify ( M, g ) to an oriented compact LCF orbifold ˆM

with Y > 0. The non-trivial ends are orbifold points of ˆM . By n = 3 or 4, we have dim H(Λ) <

1. We can apply Theorem 6.2 in [36] and Selberg’s lemma (Theorem 2.11). There is a torsion-free normal subgroup of ρ(π1(M )) containing no parabolic elements. By Corollary 3.18 (which follows from the Appendix theorem), these appear in antipodal pairs. Note, when n

is odd, the local isotropy group is isomorphic to Z2 ⊆ O( n), which is orientation-reversing. So by Theorem 3.10, when M is orientable, then it has no such orbifold points. It is natural to make the following conjecture in higher dimension. 

Conjecture 3.23 (Pairs conjecture in high dimensions) . For n ≥ 5, the non-trivial ALE ends of any orientable LCF ALE manifold (M n, g ) with Rg ≥ 0 appear in antipodal pairs. 

The pairing conjecture in dimensions n ≥ 5 is the natural extension of the result proved in Appendix B under the limit set dimension hypothesis. The Schwarzschild example illustrates why orientability is essential for the pairing. 84 3.5.4 The Schwarzschild example and the pairs conjecture 

Orientable ALE manifolds with more than one end can be easily constructed. An example can be constructed as follows: on Sn/Γ, where Γ ≤ O( n) has two fixed points, s and −s, with the standard spherical metric. Consider the Green’s function metric blown up at s and −s,the resulting manifold ( M, G 4 

> n−2

gSn ) is diffeomorphic to the standard Schwarzschild metric modulo Γ. We call such a manifold the Schwarzschild ALE manifold. In low dimension, the non-trivial ALE ends of an orientable ALE space appear in pairs. 

Example 3.1 (Schwarzschild ALE metric) . The Schwarzschild ALE metric on Rn \ { 0}/Γ

is 

gSchw =



1 + mrn−2

 4

> n−2

gflat , m > 0, r = |x|.

This metric is LCF (conformal to flat), ALE of order n − 2, and satisfies RgSchw = 0 .

The non-orientable cousin is the quotient of the same metric by the antipodal map σ : x 7 →−x on the Sn−1 at infinity. This yields a non-orientable LCF ALE manifold ( M/σ, g Schw )with a single non-trivial end (group Z2), showing that the pairing result (Theorem 3.17) fails in the non-orientable case. 

Example 3.2. If the dimension n is even, then the antipodal map is an orientation-reversing map. Then Sn/{− Id } is non-orientable. Consider the universal cover ˜M ∼= Sn \ { x, −x},blown up at x and −x, then M / Γ is a Schwarzschild ALE manifold. If Γ contains no 

Z2-rotation, we can further do a quotient (otherwise, we fix the equator). Then (M, g ) ∼=(RP n \ { p}, g RP n )/Γ, which is an LCF, ALE manifold with one end. But it is not orientable. Such a one-end, non-orientable ALE is illustrated in Figure 3.3. We call such a metric a 

non-orientable Schwarzschild ALE .

Note that the same construction does not hold when n is odd. In this case, the only non-85 trivial Γ is the Z2 action, which leaves the resulting quotient contains edge singularities. 

σ

Quotient by σ

Blow up (M, g )(M/σ, g )(M/σ \ { o}, G 4

> n−2

g)

Figure 3.3: The Schwarzschild ALE manifold ( M, g ) (left), its quotient ( M/σ, g ) by the antipodal map (center), and the blow-up at the resulting single orbifold point, which produces the football metric Sn/Z2 (bottom). 

# 3.6 Application to the Moduli Space: Refined Descrip-tion 

We now apply the structural results of §3.1– §3.5 to give a refined description of the Gromov-Hausdorff boundary of the LCF moduli space M(n, μ 0, C ) in the oriented setting, for some 

μ0 > 0. Throughout this section n = 3 or 4. We write M+ = M+(n, μ 0, C ) for the subspace 86 of M consisting of oriented metrics. Recall from Theorem 3.1 that any Gromov-Hausdorff limit of a sequence in M is a compact LCF good orbifold with Yorb ≥ 0, and from Theorem 3.5 that the curvature concentration at the singular points is organized into a finite bubble tree of complete LCF ALE orbifolds. 

## 3.6.1 The oriented moduli space 

Lemma 3.24 (Conformal blow-up of ALE orbifold singularities) . Let (M, g ) be a complete LCF ALE orbifold with Rg ≥ 0 and finitely many isolated orbifold singularities {q1, . . . , q s}.Then there exists a positive function H on M \ { qi}, harmonic with respect to Lg = −an∆g +

Rg, such that (M \ { qi}, H 4 

> n−2

g) is a smooth LCF ALE manifold with R ≥ 0.Proof. By the existence theory for the Green’s function on ALE spaces [31], for each qi there exists a positive Green’s function Gi for Lg with pole at qi. The superposition H = P 

> i

Gi > 0is a positive solution of LgH = 0 on M \ { qi}, with the leading singularity Gi ∼ ci r2−n near each qi resolving the orbifold point into an ALE end. Since Rg ≥ 0 and LgH = 0 with 

H > 0, the conformal change formula gives RH4/(n−2) g = H−(n+2) /(n−2) LgH = 0, so the blown-up metric is scalar-flat (in particular R ≥ 0). An alternative construction is given by Lemma 2.1 of [39]. 

Theorem 3.25 (GH limits in the oriented moduli space) . Let n = 3 or 4, and let (M ni , g i)

be a sequence of closed, oriented, LCF manifolds in M+(n, μ 0, C ). Let (M∞, g ∞) be any Gromov-Hausdorff limit, with finite singular set S = {x1, . . . , x k} ⊂ M∞ as provided by Theorem 3.1. Then: 1. (M∞, g ∞) is a compact oriented LCF good orbifold with Yorb (M∞, [g∞]) > 0.

87 2. At each singular point x ∈ S, the tangent cone decomposes as 

TxM∞ =

> m

G

> j=1

C Sn−1/Γj

,

and the number of non-trivial factors (those with Γj̸ = {1}) is even. 3. When n = 3 , the singular set S is empty; that is, (M∞, g ∞) is a smooth manifold. Proof. Part (1) . Theorem 3.1 provides ( M∞, g ∞) as a compact LCF orbifold with Yorb ≥ 0. Since each ( Mi, g i) is oriented, the limit is oriented away from S; as S has codimension ≥ 2the orientation extends globally. Theorem 3.13 shows M∞ is a good orbifold. 

Part (2) . We argue by induction on the depth of the bubble tree (Theorem 3.5). The bubble tree has finite depth because, by Lemma 3.3, every non-flat LCF manifold carries at least 

ε1 > 0 of Ln/ 2-curvature energy, and the total energy is bounded by C.

Base case. The leaf nodes of the bubble tree are complete smooth LCF ALE manifolds (Nℓ, g ℓ) (Theorem 3.5(iii)). Each ( Nℓ, g ℓ) inherits Rgℓ ≥ 0 from the sequence and is oriented. By Corollary 3.18, the non-trivial ends of ( Nℓ, g ℓ) appear in pairs. Via the neck structure of the bubble tree (Theorem 3.5(iv)), each end of ( Nℓ, g ℓ) corresponds to a cone factor in the tangent cone of the parent node at the blow-up point. Hence the non-trivial cone factors contributed by ( Nℓ, g ℓ) to its parent are even in number. 

Inductive step. Fix a level-ℓ non-leaf node ( Nℓ, g ℓ) in the bubble tree; it is a complete LCF ALE orbifold with finitely many isolated orbifold singularities Sℓ = {q1, . . . , q s}. Assume the claim holds for all bubbles at levels below ℓ: for each qj ∈ Sℓ, the bubble attached at qj has an even number of non-trivial ends, so an even number of non-trivial cone factors appear in 

Tqj Nℓ.By Lemma 3.24, applied to the LCF ALE orbifold ( Nℓ, g ℓ) with singularities Sℓ, there exists 88 a positive conformal factor H on Nℓ \ Sℓ, producing a smooth LCF ALE manifold (Xℓ, ˜gℓ) =  Nℓ \ Sℓ, H 4 

> n−2

gℓ



with R˜gℓ ≥ 0. The ends of ( Xℓ, ˜gℓ) fall into two groups: (a) the original non-trivial ends of ( Nℓ, g ℓ) at spatial infinity, and (b) the new ends opened at each qj ∈ Sℓ by the conformal blow-up. Since ( Xℓ, ˜gℓ) is an oriented LCF ALE manifold with R ≥ 0, Corollary 3.18 implies the total number of non-trivial ends is even. By the inductive hypothesis, the ends in group (b) arising at each qj already account for an even count in aggregate. Therefore the ends in group (a) are also even in number; translated back through the neck structure, the non-trivial cone factors in TxM∞ contributed by ( Nℓ, g ℓ) appear in pairs. Applying the induction from the deepest level up to the root M∞ completes the proof of Part (2). 

Part (3) . Every orbifold singular point x ∈ S has local isotropy group Γ x ≤ O(n) acting freely on Sn−1. Since M∞ is oriented, Γ x ≤ SO (n). For n = 3: every non-identity element of 

SO (3) is a rotation, which fixes exactly two antipodal points on S2, hence cannot act freely. Thus Γ x = {1} for all x ∈ S, so S = ∅ and M∞ is a smooth manifold. 

Corollary 3.26. Let n = 4 and Γ ≤ SO (4) be a non-trivial finite group acting freely on S3.The football orbifold S4/Γ (Definition 2.8) cannot be realized as a Gromov-Hausdorff limit of any sequence (M 4 

> i

, g i) ∈ M +(4 , μ 0, C ).Proof. The football orbifold S4/Γ has exactly two orbifold singular points (the north and south poles), each with tangent cone C(S3/Γ) — a single non-trivial cone factor. Theo-89 rem 3.25(2) requires the number of non-trivial cone factors at each singular point to be even, but 1 is odd. Hence S4/Γ cannot arise as a GH limit. 

Remark 3.4. Corollary 3.26 is the oriented LCF analogue of results in the Einstein setting. Anderson [4] raised the general question of which Einstein orbifolds can be desingularized by Einstein metrics. Biquard [13] identified analytic obstructions to such desingularizations, and Ozuch [48] proved that S4/Γ cannot be approximated by a sequence of Einstein manifolds with Eguchi-Hanson bubbles. Our result is an analogue for oriented LCF manifolds: the single non-trivial cone at each pole of the football is an obstruction to its appearance as an oriented LCF GH limit. 

## 3.6.2 Non-orientable limiting configurations 

Outside the oriented setting, the pairing constraint of Theorem 3.25(2) fails, and new limiting configurations appear. We describe two explicit constructions, both in dimension n = 4, showing that non-orientable irreducible multifolds can be realized as non-collapsing Gromov-Hausdorff limits of non-orientable LCF 4-manifolds. The gluing and perturbation techniques are standard and follow [38]; we omit the analytic details and focus on the geometric content. A slight difference from M+(n, μ 0, C ) is that the metrics constructed are only constant scalar curvature (not necessarily Yamabe minimizers), but all moduli space results in §3.1 hold in the same form for the moduli space of constant scalar curvature metrics with bounded Sobolev constant and bounded diameter. 

Definition 3.4 (Non-orientable cap) . Let n be even, Γ ≤ SO (n) a finite group acting freely on Sn−1, and extend the Γ-action to Rn+1 via the first n coordinates. Assume the antipodal map σ of Sn−1 does not belong to Γ. Let ˜Γ = ⟨Γ, ˜σ⟩ where ˜σ denotes the antipodal map of 

Sn. The non-orientable cap is the orbifold Sn/˜Γ.

Remark 3.5. Taking the Green’s function metric of the non-orientable cap at its unique 

90 orbifold point recovers the non-orientable Schwarzschild ALE manifold of Example 3.1: acomplete LCF ALE manifold with a single non-trivial end with group Γ at infinity. Being non-orientable, it does not contradict Corollary 3.18. 

Example 3.3 (Non-orientable sequence converging to non-orientable cap) . Let (N1, h 1) be the non-orientable Schwarzschild ALE manifold with group Γ at infinity (Remark 3.5), and let (N2, h 2) be the non-orientable cap S4/˜Γ, which has a single irreducible Γ-singularity. For each t > 0, glue the truncated ALE manifold (N1, h 1) to (N2, h 2) along the collar neighborhood of the singularity with gluing parameter t. Using the perturbation techniques of [38], for t

sufficiently small one can conformally perturb the glued metric to a positive constant scalar curvature LCF metric gt on the resulting non-orientable 4-manifold Mt.As t → 0, the ALE piece (N1, h 1) bubbles off and the sequence (Mt, g t) converges in the Gromov-Hausdorff sense to (N2, h 2). This is illustrated in the top row of Figure 3.4. 

In contrast to Corollary 3.26, the football metric does arise as a Gromov-Hausdorff limit of a non-orientable sequence: 

Example 3.4 (Non-orientable sequence converging to football metric) . Let (N1, h 1) be the non-orientable Schwarzschild ALE manifold of Example 3.1, with Γ containing no Z2-rotation. Let (N2, h 2) be the football orbifold S4/Γ equipped with the spherical quotient metric; note (N2, h 2) is orientable and has exactly two irreducible Γ-singularities (the north and south poles). For each t > 0, glue two copies of the truncated ALE manifold (N1, h 1) to (N2, h 2), one at each of the two singularities, with the same gluing parameter t. For t sufficiently small, the techniques of [38] produce a positive constant scalar curvature LCF metric gt on the resulting non-orientable 4-manifold Mt.As t → 0, the two ALE pieces bubble off and (Mt, g t) converges in the Gromov-Hausdorff 

91 sense to (N2, h 2). This is illustrated in the bottom row of Figure 3.4. 

Remark 3.6. The non-orientable one-ended ALE metric (N1, h 1) plays the same role here as the caps Cσ 

> Γ

in [20]: in both cases, a non-orientable ALE piece is glued onto an orbifold singularity to produce a smooth (or smoother) manifold carrying a canonical curvature con-dition. Chen-Zhu cap off singularities to run the Ricci flow; here we cap off singularities to produce a converging sequence in the moduli space. 

# 3.7 The positive mass theorem for LCF, ALE orbifolds 

Finally, we discuss the positive mass theorem. First, we recall the ADM mass: 

Definition 3.5. Let (M, g ) be an ALE manifold. Let the coordinate on one end be {xi} for 

r large. Then the ADM mass of this end is the following functional: 

m(g) := lim 

> r→∞

12( n − 1) ω

Z

> Sr

(∂igij − ∂j gii )∂j ⌞dv, 

where ω is the volume of the unit ball in Rn.

The positive mass theorem states that in asymptotically flat manifolds with non-negative scalar curvature, with the condition that the scalar curvature is integrable, the mass is non-negative, with zero mass if and only if the asymptotically flat manifold is isometric to (Rn, g Rn ). This was proved by Schoen-Yau [56], [58] using minimal surfaces, and by Witten [71] using spinors. This was generalized to AE ends of orbifolds in [39], and to AE ends of spaces with isolated conical singularities in [21]. It is natural to ask the same question on ALE manifolds. However, counterexamples were found by LeBrun [43]. Thus, a naive extension of the positive mass theorem is not true. Note that LeBrun’s counterexamples are anti-self-dual in real dimension 4. 92 Now, we prove the positive mass theorem in the LCF case: 

Theorem 3.27 (PMT for LCF ALE orbifolds) . Let (M n, g ) be a complete LCF ALE orbifold with n ≥ 3, group Γ ≤ O(n), and Rg ≥ 0 with Rg ∈ L1. Then m(g) ≥ 0, with equality if and only if (M, g ) is isometric to (Rn/Γ, g flat ).Proof of Theorem 3.27. Our method is an indirect method from [59]. By our assumption, the scalar curvature is integrable hence the mass is well-defined. From Lemma 3.4, we can conformally blow-up the orbifold singularities and form an ALE manifold. From Theorem 3.15, we can choose the conformal Green’s function so that the conformal metric is scalar-flat, and the coordinate such that the ADM mass is well-defined. Let ( M, u 4 

> n−2

g) to be the above conformal scalar-flat, ALE metric. We want to relate the mass between ( M, u 4 

> n−2

g) and ( M, g ). Note that we can adjust the scaling such that u solves: 



− ∆u + c(n)Su = 0 

u → 1 as |x| → ∞ 

Note that S ≥ 0. The asymptotic of u is: 

u = 1 + Ar 2−n + O(r2−n−ϵ)as r = |x| → ∞ . Using Green’s formula, Theorem 3.7, and the maximal principle, we have 

A = −C R 

> M

uSdv , for some C ≥ 0. In particular, A ≤ 0. Then, the mass m(u 4 

> n−2

g) = 

m(g) + ( n − 1) A ≤ m(g). Thus, it is enough to prove the mass is positive for scalar-flat ALE metrics. By the previous discussion, consider the conformal compactification, ( M ′, g ′), of ( M, g ). Consider the manifold cover, N , (Proposition 3.12), with the pull-back metric on N is 93 g = P ∗g.Consider xi ∈ M ′, which is an orbifold point with the local group Γ i. Let the minimal Green’s function at xi is Gi. Now, we pull back Gi to N . Denote Gi = P ∗Gi. As in [59], choose s ∈ P −1(xi), there exists a minimal Green’s function on N , Gs, with a singular point at s. Thus, Gi ≥ Gs. By the maximal principle of the conformal Laplacian with positive Yamabe constant, we have either Gi > G s or Gi = Gs.If Gi > G s, then, in the inverted coordinate at s, near infinity, 

Gi(x) = 1 + Ei|x|2−n + O(|x|1−n)and 

Gs(x) = 1 + Es|x|2−n + O(|x|1−n),

then we know Ei > E s. Since P is a local isometry, then m(G 4 

> n−2
> i

g) > m (G 4 

> n−2
> s

g). By 

N being an LCF manifold and by Proposition 4.3 in [59], we have m(G 4 

> n−2
> s

g) ≥ 0, thus 

m(G 4 

> n−2
> i

g) > 0. If Gi = Gs, then P −1(xi) = s. Thus, all the deck transformations on N fix s. Thus, Γi ∼= π1(M )/π 1(N ). By the previous case, if m(G 4 

> n−2
> s

g) > 0, then it is done. Otherwise, 

m(G 4 

> n−2
> s

g) = 0, then by Proposition 4.3 in [59], π1(N ) = {e}. Thus, π1(M ) ∼= Γ i, which means N ∼= Sn since there is no limiting set. Thus, by Lemma 3.16, ( M ′, g ′) is conformal to (Sn, g Sn )/Γi, the football orbifold with the spherical quotient metric. If Γ i is not trivial, ( M, g )is either conformal to ( Rn \ { 0}, g Sch )/Γi, the Schwarzschild ALE manifolds, in the manifold case; or conformal to ( Rn, g f lat )/Γi, the flat cone metric, in the orbifold case. By direct computation: In the manifold case: m(g) > 0. Otherwise, M ′ ∼= Sn. If m(g) = 0, it is true if and only if ( M, g ) ∼= ( Rn, g Rn ). In the orbifold case: m(g) = 0 and ( M, g ) ∼= ( Rn, g Rn )/Γ. 94 A direct corollary is a special case of the orbifold Yamabe problem. 

Corollary 3.28. Let (M n, g ) be a compact LCF good orbifold with Yorb (M, [g]) > 0. Then 