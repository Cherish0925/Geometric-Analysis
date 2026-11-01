---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: On the moduli space of locally conformally flat manifolds and collapsed constant scalar manifolds]

M admits a smooth constant scalar curvature metric in [g].Proof of Corollary 3.28. If ( M, g ) is not conformally equivalent to the football orbifold with the spherical metric, then by Theorem 3.27, the mass for the conformal Green’s function metric at each point m(ˆ gx) > 0. Now, we choose a singularity x ∈ M . Since ( M, g ) is LCF, the local distortion constant is purely determined by the mass (See Lemma 9.7 in [45]), we can use Schoen’s test function in [53] and conclude that Yorb (M, [g]) < Y (Sn)|Γx|, where Γ x is the orbifold group. Since this strict inequality holds for any orbifold singularity, we can apply Theorem 2.13. For the case where ( M, g ) is conformally equivalent to the football orbifold with the spherical metric, then it is obvious that it contains a metric which is of constant scalar curvature. 95 G-H G-H Non-orientable Schwarzchild ALE Non-orientable Cap Football 

Figure 3.4: Two non-orientable GH limiting configurations. Top row (Example 3.3): the limit is a non-orientable cap, and one non-orientable Schwarzschild ALE bubble detaches. 

Bottom row (Example 3.4): the limit is the football metric S4/Γ, and two non-orientable Schwarzschild ALE pieces bubble off. 96 Chapter 4 Collapsing Constant Scalar Curvature Metrics 

# 4.1 The Question of Cheeger–Fukaya–Gromov 

The Cheeger–Fukaya–Gromov (CFG) collapsing theory [19, 26, 29, 28] describes the structure of sequences of Riemannian manifolds that collapse with bounded sectional curvature to a lower-dimensional limit. A central consequence is the existence of an almost-free nilpotent group action N on the collapsing manifolds whose orbits are precisely the collapsing fibers. A metric is N -invariant if it is invariant under this nilpotent group action. 

Assumption 1. Let {(M ni , g i)} be a sequence of closed n-dimensional Riemannian manifold such that: 

• The Riemannian curvature is uniformly bounded: 

∥ Rm( gi)∥C0 ≤ C0, (4.1) 97 • The diameter is bounded from above: d(Mi, g i) ≤ C.

• The sequence collapses to a low dimensional manifold, i.e.: 

(M ni , g i) → (Xd, g ∞) (4.2) 

in the Gromov-Hausdorff sense to a manifold X, where d < n .

For the collapsing sequence satisfying Assumption 1, the limit space ( Xd, g ∞) carries a natural metric-measure structure (Xd, g ∞, dν ), where dν = χ dV g∞ and 

χ(x) := lim 

> i→∞

vol( F −1 

> i

(x)) vol( Mi) (4.3) is the relative volume function . The natural self-adjoint Laplacian on L2(X, dν ) is the drift Laplacian 

∆χh := ∆ X h + ⟨∇ log χ, ∇h⟩X , (4.4) which is the Laplacian for N -invariant functions on Mi in the collapsing limit (see Lemma 4.10). The main theorem of this chapter is the following. 

Theorem 4.1 (Collapsing CSC metrics are N -invariant up to perturbation [68]) . Let {(M ni , g i)}

be a sequence of closed n-dimensional Riemannian manifolds satisfying: 1. Bounded curvature : ∥ Rm( gi)∥C0 ≤ C0;2. Bounded diameter : d(Mi, g i) ≤ C;3. Constant scalar curvature : S(gi) ≡ v for a fixed constant v;4. Collapse : (M ni , g i) → (Xd, g ∞) in the Gromov–Hausdorff sense, where d < n ;

98 5. Spectral condition (only when v > 0): the drift Laplacian ∆χ defined in (4.4) 

does not have vn−1 as an eigenvalue on (X, g ∞), i.e. there are no nonzero solutions 

h ∈ W 2,p (X) of 

−∆χh = vn − 1 h. (4.5) 

Then, for all sufficiently large i, there exist smooth metrics g′ 

> i

on Mi such that: (i) ∥gi − g′

> i

∥W 1,p → 0 for any p > n ;(ii) g′ 

> i

is N -invariant; (iii) S(g′

> i

) ≡ v if v̸ = 0 ; or S(g′

> i

) ≡ vi with vi → 0 if v = 0 ;(iv) (Mi, g ′

> i

) → (X, g ∞) in the Gromov–Hausdorff sense. 

Remark 4.1. For v ≤ 0, no spectral condition is imposed. When v = 0 , we cannot achieve 

S(g′

> i

) = 0 exactly since 0 ∈ Spec( −∆χ) always (constants are in the kernel); instead we obtain S(g′

> i

) = vi → 0.

Remark 4.2. The spectral condition (4.5) is used to ensure that the linearized conformal scalar curvature operator is uniformly invertible in the limit (Proposition 4.13). 

Remark 4.3. The convergence in (i) is in the Sobolev norm W 1,p rather than the pointwise 

Ck,α norm. This is because the CFG averaging procedure, starting from only bounded cur-vature ( k = 0 ), produces an N -invariant metric with C0,α and W 1,p control, but not higher regularity (see Theorem 4.6). 

## Proof strategy 

The proof of Theorem 4.1 has three steps. 99 Step 1: N -invariant metric with finite regularity. Using the CFG fibration theorem [19] and the finite-regularity estimates of §4.2, with only the bounded curvature hypothesis 

∥ Rm( gi)∥C0 ≤ C0 (no Ricci flow smoothing), we obtain an N -invariant nearby metric ˆ gi

satisfying 

∥ˆgi − gi∥C0,α ≤ Cτ i, ∥ˆgi − gi∥W 1,p loc 

≤ Cτ i, (4.6) where τi → 0 is the collapse scale. At this stage, the scalar curvature satisfies only a distributional estimate: 

∥S(ˆ gi) − v∥W −1,p (X,ν i) ≤ Cτ i, (4.7) in the negative Sobolev space on the base (Proposition 4.11). 

Step 2: Analysis on the base X in Sobolev spaces. Since ˆ gi is N -invariant, conformal perturbations by N -invariant factors reduce to equations on the base X. We work in the weighted Sobolev spaces W 1,p (X, ν i) and their duals W −1,p (X, ν i), where dν i = χi dvol( gX,i ). The conformal perturbation operator Pˆgi : W 1,p (X, ν i) → W −1,p (X, ν i) is analyzed via its linearization ˆLˆgi (Proposition 4.11). 

Step 3: Conformal perturbation via implicit function theorem. We conformally per-turb g′ 

> i

= (1+ hi)4/(n−2) ˆgi to make the scalar curvature exactly constant, by solving Pˆgi (hi) = 0 (or P0,ˆgi (hi) = 0 when v = 0) via the implicit function theorem (Lemma 4.14). The uni-form invertibility of the linearized operator on N -invariant functions (Proposition 4.13), which uses the eigenvalue convergence theorem ( §4.3), provides the required estimates. This is carried out in §4.5– §4.6. 100 4.2 Cheeger–Fukaya–Gromov Theory with Finite Reg-ularity 

The original CFG theory [19] works with C∞ regularity. For our purposes we need quan-titative finite-regularity versions ( Ck,α and W k,p estimates) of the fibration theorem, the flat-connection construction, and the invariant nearby metric. 

## 4.2.1 Finite-regularity fibration and connections 

In our application, we focus mainly on finite H¨ older and Sobolev regularity. Thus, we will state the finite regularity version of the theorem with the additional Riemannian curvature 

Ck assumption. 

Assumption 2. Let {(M ni , g i)} be a sequence of closed n-dimensional Riemannian manifold such that: 

• The Riemannian curvature is uniformly bounded: 

∥ Rm( gi)∥Ck ≤ Ck, (4.8) 

for some k ≥ 0,

• The diameter is bounded from above: d(Mi, g i) ≤ C.

Corollary 4.2 (CFG fibration with finite regularity) . Let {(M ni , g i)} and (Xd, g ∞) be as in the CFG Fibration Theorem [19], with fibration maps Fi : Mi → X. If in addition the Assumption 2 is satisified, then 1. for all large i:

∥Fi∥Ck+2 ,α ≤ C(n, C k, X ), ∥AF −1 

> i(x)

∥Ck,α ≤ C(n, C k, X ),

101 for any 0 < α < 1.2. fo all large i:

∥Fi∥W k+3 ,p ≤ C(n, C k,p , X ), ∥AF −1 

> i(x)

∥W k+1 ,p ≤ C(n, C k,p , X ).

for any p > 1.Proof. From the convergence theory, around each xi ∈ Mi the local universal cover converges in Ck+1 ,α (resp. W k+1 ,p ) in the local equivariant Gromov–Hausdorff sense. H¨ older case: the metric is locally Ck+1 ,α , so the harmonic functions constructed in the CFG fibration proof admit uniform Ck+2 ,α Schauder estimates. The fibration regularity follows. Sobolev case: using ∆( ∇u) = ∇∆u + Ric( ∇u) and W k+2 ,p estimates together with the Banach algebra structure of W k,p for large p, one obtains W k+3 ,p control. 

Theorem 4.3 (CFG connection difference regularity) . Under the Assumption 2, for any open U ⊆ X and for all large i, there exists a family of flat connections {∇ xi }x∈U on the fiber 

Zxi = F −1 

> i

(x) such that: 1. {∇ xi } is a uniform Ck+1 ,α (resp. W k+2 ,p ) family in x ∈ U .2. The difference from the Levi-Civita connection satisfies 

∥∇ xi − ∇ LC i ∥Ck,α ≤ C(n, C k, X ) · τi

 resp. ∥ · ∥ W k+1 ,p ≤ Cτ i

,

where τi → 0 is the collapse scale. 3. For each fiber Zxi , there is an affine isomorphism ψx : Γ \N → Zxi with uniform Ck+2 ,α 

(resp. W k+3 ,p ) estimate, depending smoothly on x in Ck+1 ,α (resp. W k+2 ,p ). 

102 Proof. Parts (1) and (2) follow from the Section 4 of Cheeger-Fukaya-Gromov [19] con-struction of local invariant pure nilpotent structures. The bounded curvature condition 

∥ Rm( gi)∥Ck ≤ Ck ensures that, locally, the geometry is controlled in Ck+1 ,α or W k+2 ,p . The affine connection ∇xi is constructed in [19] by an averaging process from the construction of Theorem 1.12 in the z-variable, which involves integration of the gq,q ′

∇q′

, which have Ck,α 

or W k+1 ,p regularity (this takes one derivative of the gq,q ′

), against the invariant measure, which has Ck+1 ,α or W k+2 ,p regularity, since it only depends on the underlying Riemannian structure. The difference tensor Si = ∇xi − ∇ LC i satisfies the elliptic estimates bounded by the scale of the collapse τi, yielding the uniform bounds in Ck,α (or W k+1 ,p ) on each fiber, which gives Part (2). Since we are averaging with respect to the Riemannian volume form, the connection ∇xi itself has Ck+1 ,α (or W k+2 ,p ) regularity in the parameter x, which gives us Part (1). For part (3), we must construct the affine isomorphism ψx : Γ \N → Zxi and establish its regularity. First, we need to apply Malcev’s Theorem. For any simply connected open subset U ⊆ X, by choosing a local trivialization, consider F −1 

> i

(U ) ≃ U ×Γ\N and ˜F −1 

> i

(U ) ≃

U × N . This induces a family of homomorphism from π1(Zxi ) to Γ. As in [19], By Malcev’s Theorem, any finitely generated torsion-free nilpotent group Γ uniquely embeds as a uniform (cocompact) lattice in a unique simply connected nilpotent Lie group N . The real form of 

N is uniquely determined by the rational completion of Γ. This gives us our standard model space Γ \N .As in [19], The connection ∇xi on Zxi constructed in part (1) is flat and has parallel torsion. Therefore, Zxi is an affinely flat manifold. We consider the universal cover ˜Zxi , equipped with the pullback connection ˜∇xi . Because ˜∇xi is flat and has parallel torsion, we can construct a developing map Dx : ˜Zxi → N . By the [19], the holonomy group of ∇xi is trivial, and the monodromy representation maps π1(Zxi ) = Γ into the affine group NL ⋊ Aut( N ). The developing map is an equivariant affine diffeomorphism between ˜Zxi and N hence this map 103 descends to the quotient by the action of Γ 

ψx : Γ \N → Zxi . (4.9) The regularity of the map ψx is determined by the regularity of the affine connection ∇xi from which the developing map Dx is constructed. The developing map is essentially obtained by fixing a frame and integrating the parallel transport equation. In particular, it solves 

∂2(ψx)a

∂u b∂u c + (Γ xi )kbc 

∂(ψx)a

∂u k = 0 (4.10) where u are the local coordinates on Γ \N . It immediately follows that if the connection 

∇xi is in Ck,α , then ψx is uniformly bounded in Ck+2 ,α with respect to the fiber variables. Similarly, if ∇xi ∈ W k+1 ,p , the resulting map ψx is in W k+3 ,p .Finally, the dependence of ψx on the base point x ∈ U is determined by the variation of the connections ∇xi with respect to x, which is of Ck+1 ,α (or W k+2 ,p ). 

Lemma 4.4 (Local trivialization regularity) . Under the Assumption 2, for each small simply connected open U ⊆ X there exists a local trivialization 

ΦU,i : F −1 

> i

(U ) ∼

−→ U × Γ\N 

with uniform Ck+2 ,α (resp. W k+3 ,p ) estimate. Proof. With the assumption above, by Corollary 4.2, the fibration map Fi : Mi → X,satisfies uniform ∥Fi∥Ck+2 ,α or ∥Fi∥W k+3 ,p estimate. Let U ⊆ X be a simply connected open subset. Since Fi are submersions, by implicit function theorem, there exists a local section 

σi : U → F −1 

> i

(U ) ⊆ Mi, so that Fi ◦ σi = Id on U with uniform ∥σi∥Ck+2 ,α or ∥σi∥W k+3 ,p 

estimate respectively. 104 On the local universal cover, ˜F −1 

> i

(U ), we have the fiber-wise affine isomorphism: ˜ψx : N → ˜Zxi . (4.11) With a little abuse of notation, we denote ˜ψx : NL → Aut( ˜Zxi ) as the isomorphism of group action. By Theorem 1.13, the fiber-wise group action generated by the right invariant vector field on N extend to a group action on ˜F −1 

> i

(U ). For each fiber ˜Zx′ 

> i

, we have the map 

ϕx′ : Aut( Zxi ) → Aut( Zx′ 

> i

). (4.12) Thus, we define the fiber-wise action on x′ by: ψx′ := ϕ−1 

> x′

◦ ˜ψx. which gives us the action as ˜ψi : NL → Aut( ˜F −1 

> i

(U )) (4.13) with the property that Fi( ˜ψi(g)p) = Fi(p), for any p ∈ Mi, g ∈ N L. By (3) of Theorem 4.3 and Theorem 1.13, the mapping ˜ψi has a uniform Ck+2 ,α or W k+3 ,p loc estimate, respectively. Thus, we can define our local trivilization ˜Φ−1 

> U,i

: U × N → ˜F −1 

> i

(U ) (4.14) (x, g ) 7 → ˜ψi(g) · ˜σi(x), (4.15) where ˜ σi is a lift to ˜F −1 

> i

(U ). Note that, by Theorem 1.13, ˜ψi is invariant under Γ. Thus, ˜Φ−1 

> U,i

descends to U × Γ\N , which is the desired local trivialization with regularity. 

Remark 4.4. The construction of this local trivialization is different from the one from [19]. In [19], they use the normal exponential map to construct the tublar neighborhood of the center fiber. In our case, we use the improved regularity given by the harmonic coordinate, which is optimal. Also, instead of using the family of affine isomorphism of the fiber using 

105 Riemannian structure, we directly use the fiber-wise isomorphism given by Malcev’s Theorem, which does not lose regularity. 

## 4.2.2 The N -invariant nearby metric 

Since the definition of right invariant vector field is independent the choice of the local trivialization, we have the following regularity for the right invariant vector field. 

Corollary 4.5 (Right-invariant vector field regularity) . Let V be a right-invariant vector field on ^F −1 

> i

(U ) ∩ B˜xi (2 τi). Then 

∥V ∥Ck+1 ,α ≤ C(n, C k, X ) · | V (˜ xi)|  resp. ∥V ∥W k+2 ,p ≤ C|V (˜ xi)|.

Proof. Note, the right-invariant vector field on ˜F −1 

> i

(U ) is given by the pull-back of the right-invariant vector field using ˜ΦU,i . Then, the C0 (L∞) norm of V in both cases is uniformly bounded by |V (˜ xi)|, depends on the C0 norm of the Riemannian metric. Let Sx := ∇xi − ∇ LC i on the fiber. Denote Ax as the second fundamental form of the fiber of F −1 

> i

(x), which we regard as a tensor on the universal cover ˜F −1 

> i

(U ). By Theorem 1.11, 

∥Ax∥C0 is uniformly bounded. Since V is a right invariant vector field, by (1.16), we have: 

∥∇ V ∥C0 ≤ ∥ SxV ∥C0 + ∥AxV ∥C0 + ∥∇ xi V ∥C0 ≤ C∥V ∥C0 , (4.16) by ODE comparison, we have the desired C1 estimate. For the higher order estimate, since 

∇xi V produces a constant right invariant vector field (recall (1.16)), we have 

∥∇ kV ∥C0 ≤ ∥ (∇k−1Sx)V ∥C0 + ∥(∇k−1Ax)V ∥C0 . (4.17) Thus, the estimate follows from Corollary 4.2 and Theorem 4.3. 106 Now, we are ready to construct the N -invariant metric 

Definition 4.1. The tensor Ti on Mi is called N -invariant if for every x ∈ X, there is a simply connected neighborhood U ⊆ X such that F −1 

> i

(U ) ≃ U × N /Γ. Then on the universal cover ˜F −1 

> i

(U ) ≃U × N , the pull-back tensor ˜Ti is invariant under N -action. 

Follow [19], we can construct the nearby N -invariant metric using average method. The upshot is that we have the finite regularity estimate. 

Theorem 4.6 (N -invariant nearby metric estimate) . Under the finite regularity assumption, for all large i there exists an N -invariant metric ˆgi on Mi such that, for every U ⊆ X and any compact K ⊆ ^F −1 

> i

(U ):

∥ˆgi − gi∥Ck,α ≤ C(n, C k, X ) · τi

 resp. ∥ˆgi − gi∥W k+1 ,p   

> loc (K)

≤ C(n, C k,p , X, K ) · τi

.

Proof. The construction follows the averaging method in the section 4 of [19]. By Theorem 1.11, Λ = NL ∩ Γ is normal in Γ with uniform finite index, by passing to the finite cover, it is enough to consider the case Γ ⊆ N L.On ˜F −1 

> i

(U ) ≃ U × N . Let h ∈ N L, then we regard h ∈ Aut( ˜F −1 

> i

(U )). Consider h 7 → h∗gi.Note that this map is constant on the Γ orbit. Since the group NL is nilpotent, it is unimodular. Therefore, the space Γ \N L admits a canonical left-invariant measure dμ of total volume 1. Thus, we construct the metric: ˆgi =

Z

> Γ\N

h∗gidμ. (4.18) Thus, ˆ gi is a left-invariant metric on ˜F −1 

> i

(U ). For each h ∈ N L, there exists a right invariant vector field Vh so that h = exp( Vh). By the 107 fundamental theorem of calculus, we have: 

h∗gi − gi =

Z 10

ddt (exp ∗(tV h)gi) dt =

Z 10

(exp ∗(tV h))( LVh gi)dt. (4.19) Thus, we have: 

∥ˆgi − gi∥ ≤ Cn max  

> h∈Γ\N

(∥D exp( Vh)∥ · ∥∇ Vh∥). (4.20) Now by the collapsing assumption, the diameter of each fiber is less than τi. For every x ∈ U ,choose a lift ˜ xi on ˜F −1 

> i

(U ). Then |Vh(˜ xi)| ≤ C · τi. By the expansion of Jacobi field (see, for example, Section 5 of [45]), k-th nilpotentcy of group N , and Theorem 4.3, 

∥D exp( Vh)∥ = ∥

> ∞

X

> n=0

(−1) n

(n + 1)! ad nVh ∥ ≤ ∥ 

> k

X

> n=0

(−1) n

(n + 1)! ad nVh ∥ ≤ ∥ (1 + Cτ i) Id ∥ ≤ C. 

(4.21) By Corollary 4.5, ∥∇ Vh∥ ≤ C · τi, so we are done. 

Corollary 4.7 (Curvature estimate for invariant nearby metric) . With the notation of The-orem 4.6, for k ≥ 2:

∥ Rm(ˆ gi) − Rm( gi)∥Ck−2,α ≤ C(n, C k, X ) · τi,

and similarly in W k−1,p  

> loc

.Proof. Immediate from Theorem 4.6 and the fact that Rm is a second-order differential operator in the metric. 108 4.3 Convergence of Eigenvalues of the Laplacian 

The key spectral input for the proof of Theorem 4.1 is Fukaya’s theorem [27] on eigenvalue convergence under measured Gromov–Hausdorff collapse. We state the relevant definitions and the theorem precisely. 

Definition 4.2 (Measured Gromov–Hausdorff convergence) . Let μ be a Borel measure on 

X. We say 

(Xα, d α, μ α) → (X, d ∞, μ )

in the measured Gromov–Hausdorff (mGH) sense if there exists a Borel measurable εα-approximation ψα : Xα → X with εα → 0 such that the pushed-forward measures converge weakly: 

Z

> X

u d (( ψα)∗μα) →

Z

> X

u dμ for all u ∈ C∞(X).

In the collapsing setting, set μi = dvol gi / vol( Mi). The collapse ( Mi, g i) → (X, g ∞) then gives the mGH convergence ( Mi, g i, μ i) → (X, g ∞, μ ), where μ = χ dvol g∞ and χ is the 

relative volume function 

χ(x) = lim 

> i→∞

vol( F −1 

> i

(x)) vol( Mi) .

By the improved regularity of the fibration Fi (Theorem ?? ), χi → χ in C1,α and W 2,p for any 0 < α < 1 and p > 1. 

Theorem 4.8 (Eigenvalue convergence under collapsing [27]) . In the collapsing setting 

(Mi, g i) → (X, g ∞) with d = dim X ≥ 1, let λk(Mi, g i) denote the k-th eigenvalue of the Laplacian on (Mi, g i). Then: 

109 1. lim  

> i→∞

λk(Mi, g i) = λk exists for each k ≥ 0.2. λk is the k-th eigenvalue of the drift Laplacian ∆ χ on L2(X, μ ), defined weakly by the bilinear form 

Q(f1, f 2) = 

Z

> X

⟨∇ f1, ∇f2⟩g∞ dμ, 

or explicitly 

∆χ = ∆ g∞ + ⟨∇ log χ, ∇ · ⟩ g∞ .

Proof. Take the mGH convergence ( Mi, g i, μ i) → (X, g ∞, μ ). The relative volume functions 

χi are uniformly bounded and equicontinuous by the CFG fibration theorem, so by Arzel` a– Ascoli, χi → χ in C1,α . Integration by parts on the eigenfunction equation gives the weak formula for ∆ χ:

Z

> X

⟨∇ f1, ∇f2⟩ dμ =

Z

> X

⟨∇ f1, ∇f2⟩χ dvol g∞ = −

Z

> X

 ∆g∞ f1 + ⟨∇ log χ, ∇f1⟩f2 dμ. 

The eigenvalue convergence λk(Mi, g i) → λk is the content of [27]. 

Remark 4.5. Applying this to our setting: under the bounded curvature assumption, χi → χ

in C1,α and W 2,p . By the averaging construction of ˆgi in Theorem 4.6, the fiber volume is unchanged, hence χi(gi) = χi(ˆ gi), and we also have χ(ˆ gi) → χ in C1,α and W 2,p .

Remark 4.6. Theorem 4.8 does not assert pointwise convergence of ∆gi to ∆χ. It does imply: if v/ (n − 1) /∈ Spec( −∆χ), then for all large i the value v/ (n − 1) is also not an eigenvalue of the relevant operator on (Mi, g i). This is the spectral condition needed in Theorem 4.1 and applied in the uniform injectivity estimate (Proposition 4.13). Note that the spectral condition is only required when v > 0. When v ≤ 0, the linearized 

110 operator is automatically invertible (resp. invertible on mean-value-zero functions when v =0) without any additional assumption. 

# 4.4 Proof Strategy: Invariant Metric and Scalar Cur-vature Estimates 

In this section we carry out Steps 1 and 2 of the proof of Theorem 4.1: producing the N -invariant metric ˆ gi close to gi in W 1,p , and establishing the scalar curvature estimate in the distributional norm W −1,p on the base. We work throughout under Assumption 3 with only 

∥ Rm( gi)∥C0 ≤ C0.

Assumption 3. Let {(M ni , g i)} be a sequence of closed n-dimensional Riemannian manifold such that: 

• The Riemannian curvature is uniformly bounded: 

∥ Rm( gi)∥C0 ≤ C0, (4.22) 

• The diameter is bounded from above: d(Mi, g i) ≤ C.

• The scalar curvature S(gi) ≡ v, where v is a constant; 

• The sequence collapses to a low dimensional manifold, i.e.: 

(M ni , g i) → (Xd, g ∞) (4.23) 

in the Gromov-Hausdorff sense to a manifold X, where d < n .

111 • If v > 0, the operator 

∆χh ≡ ∆X h + ∇ log χ · ∇ X h (4.24) 

does not have vn−1 as an eigenvalue, where χ is defined above, i.e, there are no non-zero solutions on X of 

−∆χh = vn − 1h. (4.25) 

## 4.4.1 The N -invariant nearby metric 

By Theorem 4.6 applied with k = 0, for all sufficiently large i there exists an N -invariant metric ˆ gi on Mi satisfying 

∥ˆgi − gi∥C0,α ≤ C(n, C 0, X ) · τi, (4.26) 

∥ˆgi − gi∥W 1,p loc (K) ≤ C(n, C 0, p, X, K ) · τi (4.27) for any 0 < α < 1, p > n , and compact K ⊆ ^F −1 

> i

(U ). 

Remark 4.7. Unlike the higher-regularity case, when only ∥ Rm( gi)∥C0 is bounded, the cur-vature tensor of ˆgi is not necessarily close to that of gi. This is because the CFG averaging procedure controls the metric only in C0,α and W 1,p .

## 4.4.2 Scalar curvature in the distributional norm 

Since ˆ gi only has W 1,p bounds, its scalar curvature S(ˆ gi) is not pointwise bounded. However, the difference S(ˆ gi) − S(gi) is controlled in a negative Sobolev norm. Recall the Lee–LeFloch formula [44]: for two metrics g, h ∈ W 1,∞ 

> loc

(M ) with difference tensor 112 Υ = Γ( g) − Γ( h), 

S(g) − S(h) = div h T + Q, (4.28) where T k = gij Υkij −gik Υjji and Q is quadratic in Υ. Integrating by parts, S(g)−S(h) defines a bounded functional on W 1,p  

> 0

(M ) via 

⟨S(g) − S(h), ϕ ⟩ := 

Z

> M



−T · ∇ h ϕ dvol (g)

> dvol (h)

 + Q ϕ dvol (g)

> dvol (h)



dvol (h). (4.29) In particular, 

∥S(g) − S(h)∥W −1,p (K) ≤ C(n, p, K ) · ∥ g − h∥W 1,p (K). (4.30) Applying (4.30) to g = ˆ gi and h = gi with S(gi) ≡ v, and using (4.27): 

Theorem 4.9. Let {(M ni , g i)} satisfy Assumption 3. Then on ^F −1 

> i

(U ), for every p > n and compact K,

∥S(ˆ gi) − v∥W −1,p (K) ≤ C(n, C 0, X, K ) · τi. (4.31) 

## 4.4.3 Laplacian on N -invariant functions 

Lemma 4.10 (Laplacian on N -invariant functions [62]) . Let u ∈ C∞(Mi) be N -invariant and ˆgi N -invariant. Using the second fundamental form decomposition ∇∂a ∂b = ¯∇∂a ∂b +

A(∂a, ∂ b),

∆ˆgi u = ∆ gX,i u + ⟨Hi, ∇X u⟩, (4.32) 113 where gX,i = ˆ gi|ker dF ⊥ 

> i

is the base metric and Hi = tr Ai is the mean curvature vector of the fibers. Moreover, gX,i → g∞ in the W 1,p sense on X, and Hi → ∇ g∞ log χ in W 1,p .Consequently, defining dν i = χi dvol (gX,i ) and the drift Laplacian ∆νi := ∆ gX,i +⟨∇ log χi, ∇·⟩ ,for N -invariant functions, 

∆ˆgi u = ∆ νi Πi(u), (4.33) 

and in the limit, 

∆νi

> i→∞

−−−→ ∆χ := ∆ g∞ + ⟨∇ log χ, ∇ · ⟩ g∞ in W 1,p -sense. (4.34) 

Proof. The splitting (4.32) follows from the definition of the second fundamental form and N -invariance: since u is constant on fibers, ∇u is horizontal, and the fiber Laplacian contributes only ⟨Hi, ∇u⟩.For the convergences: by the equivariant Gromov-Hausdorff diagram ( ^F −1 

> i

(U ), ˜gi, Γi, ˜pi) ( ˜U∞, ˜g∞, N , ˜p∞)(F −1 

> i

(U ), g i) (U, g ∞) 

> eq GH πiπ∞
> Fi

with Fi of uniform W 3,p bound (Corollary 4.2), the inner products of horizontal lifts converge in W 1,p , giving gX,i → g∞.For the mean curvature: the N -invariant metric decomposes as ˆ gi = F ∗ 

> i

gX,i +( ciχi)2/(n−d)gN (ωi(·), ω i(·)), so Hi = ∇gi log χi. Since the fibration converges in W 3,p , Ai → A∞ in W 1,p , hence 

Hi → ∇ g∞ log χ in W 1,p .114 4.4.4 Weighted Sobolev spaces on the base 

Since ˆ gi is N -invariant, every N -invariant function u on Mi corresponds to a function Π i(u)on X. We transfer the analysis to X using the weighted measure dν i = χi dvol (gX,i ). 

Definition 4.3. Define Lp(X, ν i) with norm ∥f ∥pLp(X,ν i) = R 

> X

|f |p dν i, and W 1,p (X, ν i) with norm ∥f ∥W 1,p (X,ν i) = ∥∇ f ∥Lp(X,ν i) + ∥f ∥Lp(X,ν i).Define the dual space W −1,p (X, ν i) = ( W 1,q (X, ν i)) ∗ with 1/p + 1 /q = 1 .When v = 0 , define the mean-value-zero subspaces: 

W 1,p  

> 0

(X, ν i) := 

n

ϕ ∈ W 1,p (X, ν i) : 

Z

> X

ϕ dν i = 0 

o

, (4.35) 

W −1,p  

> 0

(X, ν i) := {f ∈ W −1,p (X, ν i) : f (1) = 0 }. (4.36) The identification Π i intertwines the W 1,p loc -norm on ^F −1 

> i

(U ) with the W 1,p (X, ν i)-norm, and similarly for W −1,p . In particular, Theorem 4.9 gives 

∥Πi(S(ˆ gi)) − v∥W −1,p (X,ν i) ≤ Cτ i. (4.37) 

# 4.5 Linearized Equation Estimates 

In Step 3 of the proof of Theorem 4.1, we seek a conformal factor ψi = 1+ hi (an N -invariant function on X) such that g′ 

> i

= ψ4/(n−2)  

> i

ˆgi has exactly constant scalar curvature. This section establishes the analytic estimates on the base ( X, g X,i , dν i) needed to apply the implicit function theorem. 115 4.5.1 The operator P and its linearization 

Proposition 4.11 (P -operator in the Sobolev setting) . Under Assumption 3, let ˆgi be the 

N -invariant metric from Theorem 4.6. Set Θi := v − S(ˆ gi).For N -invariant ϕ, via the projection Πi(ϕ) ∈ C∞(X) and the drift Laplacian ∆νi = ∆ gX,i +

⟨∇ log χi, ∇·⟩ , define the conformal perturbation operator on the base: 

Pˆgi (ϕ) := −4n − 1

n − 2∆νi ϕ + S(ˆ gi)(1 + ϕ) − v(1 + ϕ)(n+2) /(n−2) , (4.38) 

viewed as a map Pˆgi : W 1,p (X, ν i) → W −1,p (X, ν i) for p > d .Write Pˆgi (h) = Pˆgi (0) + ˆLˆgi h + Qˆgi (h) where 

ˆLˆgi := −4n − 1

n − 2∆νi −



v · 4

n − 2 − Θi



. (4.39) 

Then: 

(i) Initial error : for i ≫ 0,

∥Pˆgi (0) ∥W −1,p (X,ν i) = ∥Θi∥W −1,p (X,ν i) ≤ Cτ i. (4.40) (ii) Linearization : the linearized operator at h = 0 is ˆLˆgi .

(iii) Quadratic remainder : for hj ∈ W 1,p (X, ν i) with ∥hj ∥W 1,p < s 0 sufficiently small, there exists C2 = C2(s0) so that 

∥Qˆgi (h1) − Qˆgi (h2)∥W −1,p (X,ν i) ≤ C2

 ∥h1∥W 1,p + ∥h2∥W 1,p 

∥h1 − h2∥W 1,p . (4.41) 

Proof. Part (i): Pˆgi (0) = Θ i = v − S(ˆ gi). By (4.37), ∥Θi∥W −1,p (X,ν i) ≤ Cτ i.116 Part (ii): Direct computation; differentiating the Yamabe equation −an∆ˆgi (1+ ϕ)+ S(ˆ gi)(1+ 

ϕ) = S(g′

> i

)(1 + ϕ)(n+2) /(n−2) (with an = 4( n − 1) /(n − 2)) at ϕ = 0 gives ˆLˆgi .Part (iii): The nonlinear term Qˆgi (h) = −v[(1 + h)(n+2) /(n−2) − 1 − n+2  

> n−2

h] is analytic in h.The Sobolev embedding W 1,p (X, ν i) ,→ C0(X) (for p > d ) and Taylor’s theorem give the Lipschitz estimate (4.41). In the case v = 0, we need to consider the space W 1,p  

> 0

(X, ν i) ⊆ W 1,p (X, ν i) defined as 

Z

> X

ϕdν i = 0 (4.42) for ϕ ∈ W 1,p  

> 0

(X, ν i). We define the nonlinear functional: 

vi = vi(ϕ) = 

R 

> X

S(ˆ gi)(1 + ϕ)dν i

R 

> X

(1 + ϕ) n+2  

> n−2

dν i

. (4.43) Thus 

vi(0) = 

Z

> X

S(ˆ gi)dν i (4.44) Then define 

P0,ˆgi : W 1,p  

> 0

(X, ν ) → W −1,p  

> 0

(X, ν ) (4.45) by 

ϕ 7 → − 4n − 1

n − 2∆ˆgi ϕ + S(ˆ gi) · (1 + ϕ) − vi(ϕ) · (1 + ϕ) n+2  

> n−2

, (4.46) 117 The linearized operator can be computed as ˆL0,ˆgi h = −4n − 1

n − 2∆νi h +



Θi − n + 2 

n − 2vi(0) 



h −

Z

> X



Θi − n + 2 

n − 2vi(0) 



hdν ′

> i

. (4.47) We also have 

Q0,ˆgi (h) = P0,ˆgi (h) − P0,ˆgi (0) − ˆL0,ˆgi h, (4.48) and it can be computed as 

Q0,ˆgi (h) = −vi(h) · (1 + h) n+2  

> n−2

+   n + 2 

n − 2

vi(0) · h +

Z

> X



Θi −   n + 2 

n − 2

vi(0) 



hdν i + vi(0) .

(4.49) The analog of Proposition 4.11 holds for P0,ˆgi , we do not restate it here. 

## 4.5.2 Calder´ on-Zygmund estimate 

Proposition 4.12 (Calder´ on-Zygmund estimate on the base) . For p > d and i ≫ 1, there exists a constant C, independent of i, such that for any h ∈ W 1,p (X, ν i):

∥h∥W 1,p (X,ν i) ≤ C



∥ ˆLˆgi h∥W −1,p (X,ν i) + ∥h∥W −1,p (X,ν i)



. (4.50) 

Proof. Since gX,i → g∞ in C0,α (Lemma 4.10), the operators ˆLˆgi converge to ˆL∞ = −4n−1 

> n−2

∆χ−

v · 4 

> n−2

in an appropriate sense. These are non-collapsing elliptic operators on X with uni-formly bounded coefficients (in W 1,p ), so standard Calder´ on-Zygmund theory applies. The constant C is independent of i for large i.118 4.5.3 Uniform injectivity 

Proposition 4.13 (Uniform injectivity of ˆLˆgi ). Under Assumption 3 with limiting manifold 

(X, g ∞).

Case v̸ = 0 : For i sufficiently large, the map ˆLˆgi : W 1,p (X, ν i) → W −1,p (X, ν i) is uniformly injective for p > d : there exists δ0 > 0 independent of i such that 

∥ ˆLˆgi h∥W −1,p (X,ν i) ≥ δ0∥h∥W 1,p (X,ν i) (4.51) 

for all h ∈ W 1,p (X, ν i).When v > 0, this uses the spectral condition (4.5) : v/ (n − 1) /∈ Spec( −∆χ). When v < 0,the estimate holds without any spectral condition. 

Case v = 0 : The map ˆL0,ˆgi : W 1,p  

> 0

(X, ν i) → W −1,p  

> 0

(X, ν i) satisfies the same uniform injec-tivity estimate (4.51) for h ∈ W 1,p  

> 0

(X, ν i). Moreover, Ker( ˆL0,ˆgi ) ∼= Coker( ˆL0,ˆgi ) ∼= R.Proof. Case v̸ = 0 : By contradiction. If (4.51) fails, there exist hi ∈ W 1,p (X, ν i) with 

∥hi∥W 1,p (X,ν i) = 1 and εi := ˆLˆgi hi → 0 in W −1,p (X, ν i). Since p > d , the Sobolev embedding gives hi ∈ C0,α (X) ( α = 1 − d/p ) with uniform bound. By Arzel` a-Ascoli, passing to a subsequence, hi → h∞ in C0,β for β < α .Since χi → χ∞ in C1,α and dν i → dν ∞ weakly, for any test function ψ ∈ W 1,p ∗

(X, g ∞)(where 1 /p + 1 /p ∗ = 1): 

⟨ ˆLˆgi hi, ψ ⟩ =

Z

> X

4n − 1

n − 2⟨∇ hi, ∇ψ⟩ dν i − 4

n − 2vh iψ dν i + Θ i(hiψ) = εi(ψ) → 0. (4.52) 119 Taking i → ∞ , using ∥Θi∥W −1,p ≤ Cτ i → 0: 

Z

> X

4n − 1

n − 2⟨∇ h∞, ∇ψ⟩ dν ∞ − 4

n − 2v h ∞ψ dν ∞ = 0 , (4.53) i.e. h∞ solves −∆χh∞ = vn−1 h∞ weakly on X.When v > 0: by the spectral condition (4.5), h∞ ≡ 0. When v < 0: the operator −∆χ − vn−1

is coercive (since −v/ (n − 1) > 0), so again h∞ ≡ 0. By the Calder´ on-Zygmund estimate (Proposition 4.12), ∥hi∥W 1,p → 0, contradicting ∥hi∥W 1,p =1. 

Case v = 0 : The proof is identical. To confirm h∞ ∈ W 1,p  

> 0

: since ∥hi∥L∞ ≤ C (Sobolev) and hi ∈ W 1,p  

> 0

(by assumption), the dominated convergence theorem gives R 

> X

h∞ dν ∞ = 0. Then −∆χh∞ = 0 with mean value zero implies h∞ ≡ 0. 

# 4.6 Nonlinear Equation Solution 

We now combine the estimates of the preceding sections to solve the nonlinear equation via the implicit function theorem, completing the proof of Theorem 4.1. 

Lemma 4.14 (Implicit function theorem for Banach spaces) . Let H : E → F be a smooth map between Banach spaces. Write Q = H − H(0) − H′(0) . Assume: (1) There exist C1 > 0 and s0 > 0 such that 

∥Q(x) − Q(y)∥F ≤ C1(∥x∥E + ∥y∥E )∥x − y∥E for all x, y ∈ BE (0 , s 0).

(2) The linearized operator H′(0) : E → F is an isomorphism with ∥[H′(0)] −1∥F →E ≤ C2.If s < min( s0, 1/(2 C1C2)) and ∥H(0) ∥F < s/ (2 C2), then there is a unique x ∈ BE (0 , s )120 solving H(x) = 0 .Proof. Rewrite H(x) = 0 as x = −[H′(0)] −1(H(0) + Q(x)). Under the hypotheses, the right-hand side defines a contraction on BE (0 , s ) by the Banach fixed-point theorem. 

Theorem 4.15 (Existence of N -invariant CSC perturbation) . Under Assumption 3 with 

∥ Rm( gi)∥C0 ≤ C0, for all i ≫ 0 there exists hi ∈ C∞(X) with 

∥hi∥W 1,p (X,ν i) ≤ Cτ i, τi → 0, (4.54) 

solving: 

• Pˆgi (hi) = 0 if v̸ = 0 ;

• P0,ˆgi (hi) = 0 if v = 0 , where 

P0,ˆgi (ϕ) := −4n − 1

n − 2∆νi ϕ + S(ˆ gi)(1 + ϕ) − vi(ϕ)(1 + ϕ)(n+2) /(n−2) , (4.55) 

and vi(ϕ) :=      

> R
> XS(ˆ gi)(1+ ϕ)dν i
> R
> X(1+ ϕ)(n+2) /(n−2) dν i

, maps W 1,p  

> 0

(X, ν i) → W −1,p  

> 0

(X, ν i).Consequently, the conformal metric g′ 

> i

:= (1 + hi)4/(n−2) ˆgi satisfies: (i) g′ 

> i

is N -invariant; (ii) ∥gi − g′

> i

∥W 1,p → 0 for any p > n ;(iii) S(g′

> i

) ≡ v if v̸ = 0 ; or S(g′

> i

) ≡ vi(hi) with vi(hi) → 0 if v = 0 ;(iv) (Mi, g ′

> i

) → (X, g ∞) in the Gromov–Hausdorff sense. This completes the proof of Theorem 4.1. Proof. Case v̸ = 0 : Apply Lemma 4.14 with E = W 1,p (X, ν i), F = W −1,p (X, ν i), and 121 H = Pˆgi .

• Quadratic estimate: Proposition 4.11(iii) provides the constant C1 for estimate on Qˆgi .

• Invertibility: By Proposition 4.13, ˆLˆgi is uniformly injective. Combined with Propo-sition 4.12 (Calder´ on-Zygmund estimate), ˆLˆgi is an isomorphism with uniform bound 

C2 independent of i.

• Smallness of H(0) : By Proposition 4.11(i), ∥Pˆgi (0) ∥W −1,p ≤ Cτ i → 0. Since τi → 0, all conditions of Lemma 4.14 are satisfied for large i. The unique solution 

hi ∈ W 1,p (X, ν i) satisfies (4.54). Smoothness hi ∈ C∞(X) follows from standard elliptic regularity. 

Case v = 0 : Use E = W 1,p  

> 0

(X, ν i), F = W −1,p  

> 0

(X, ν i), and H = P0,ˆgi . The analog of Propo-sition 4.11 holds for P0,ˆgi , and Proposition 4.13 (Case v = 0) gives the uniform injectivity of the modified linearized operator ˆL0,ˆgi : W 1,p  

> 0

→ W −1,p  

> 0

. The argument is otherwise identical. 

Verification of conclusions: 

(i): g′ 

> i

is N -invariant because ˆ gi is N -invariant and hi is N -invariant (it descends from a function on X). (ii): By (4.54), ∥hi∥W 1,p (X,ν i) ≤ Cτ i → 0. The conformal change (1 + hi)4/(n−2) → 1 in W 1,p ,giving ∥g′ 

> i

− ˆgi∥W 1,p ≤ C∥hi∥W 1,p → 0. Combined with ∥ˆgi − gi∥W 1,p ≤ Cτ i, we get (ii). (iii): Pˆgi (hi) = 0 is exactly the CSC equation S(g′

> i

) = v when v̸ = 0. For v = 0: 

P0,ˆgi (hi) = 0 gives S(g′

> i

) = vi(hi); since | R 

> X

S(ˆ gi) dν i| ≤ ∥ S(ˆ gi) − v∥W −1,p ≤ Cτ i and 

R 

> X

(1 + hi)(n+2) /(n−2) dν i → 1, we get vi(hi) → 0. (iv): The Gromov–Hausdorff convergence follows from (4.54) and Sobolev embedding: ∥hi∥C0 ≤

C∥hi∥W 1,p ≤ Cτ i → 0, so g′ 

> i

is uniformly close to gi in C0 and converges to the same GH 122 limit. 

Proof of Theorem 4.1. By Assumption 3, there exists an N -invariant nearby metric ˆ gi from Theorem 4.6. By Theorem 4.15, the metric g′ 

> i

= (1 + hi)4/(n−2) ˆgi satisfies all the required conclusions: (1) When v < 0: no eigenvalue assumption; S(g′

> i

) ≡ v;(2) When v = 0: no eigenvalue assumption; S(g′

> i

) ≡ vi → 0; (3) When v > 0: the eigenvalue assumption guarantees uniform injectivity via Proposi-tion 4.13; S(g′

> i

) ≡ v.123 Chapter 5 Further Discussions and Open Problems 

# 5.1 A Gluing Construction of Constant Scalar Curva-ture Metrics 

The main theorem of Chapter 4 produces, from a collapsing CSC sequence, a nearby N -invariant CSC sequence. A complementary direction is to construct collapsing CSC sequences from scratch by gluing. In this section we describe Joyce’s gluing theorem for connected sums [38] and a generalization due to a new paper by Viaclovsky–Wang [68] that allows one of the factors to be itself collapsing. 

## 5.1.1 Joyce’s gluing theorem 

Theorem 5.1 (Constant scalar curvature metrics on connected sums [38]) . Let (M n 

> 1

, g 1) and 

(M n 

> 2

, g 2) be compact Riemannian manifolds, each with constant scalar curvature S(gj ) = v > 

0. Let pj ∈ Mj be base points. Then for all sufficiently small gluing parameter t > 0, the 

124 connected sum M1#M2 admits a constant scalar curvature metric gt with S(gt) = vt → v as 

t → 0.In the LCF setting (both factors locally conformally flat), gt can be chosen LCF as well. Construction sketch. The gluing uses the Green’s function metric : on ( Mj , g j ) with S(gj ) = 

v > 0, the conformal Green’s function Gpj at pj satisfies ( −an∆ + S)Gpj = δpj . Setting ˆgj = G4/(n−2)  

> pj

gj on Mj \{ pj } gives an asymptotically flat (AF) manifold. The gluing identifies the annular region near p1 with the annular region near infinity in the AF manifold from 

M2, via the identification ι scaled by t. An implicit function theorem argument (invertibility of the linearized scalar curvature operator on each factor) perturbs the approximate metric to exact constant scalar curvature; see [38] for the complete details. 

## 5.1.2 Collapsing factors and a new type of degeneration 

Joyce’s construction requires both factors to be non-collapsing (positive injectivity radius at the gluing point). The Viaclovsky–Wang generalization allows one factor to be collapsing. 

Definition 5.1 (Collapsing factor) . A family (Znt , g t) parametrized by t ∈ (0 , t 0) is a col-lapsing factor (at base point zt ∈ Zt) if: 1. | Rm( gt)| ≤ C1 uniformly; 2. inj gt (zt) → 0 as t → 0;3. (Zt, g t) → (Xd, g ∞) in the Gromov–Hausdorff sense with d < n , with smooth equivari-ant convergence on local universal covers. The quintessential example is a family of metrics on a fixed manifold M n fibering over Xd

with infranilmanifold fibers, where the fiber directions have diameter O(t).

Theorem 5.2 (VW gluing theorem: collapsing factors [68]) . Let (Znt , g t) be a collapsing 

125 factor with S(gt) ≡ v and base point zt. Let (N n, ˆg) be an asymptotically flat manifold with 

S(ˆ g) = 0 . Suppose the spectral condition of Theorem 4.1 holds on the limit (X, g ∞).Then, for t sufficiently small and suitable gluing parameters a = a(t), b = b(t) with b ≪

inj gt (zt), the connected sum Zt#M (where N = M \ { p}, p ∈ M ) admits a constant scalar curvature metric g′ 

> t

such that: (i) S(g′

> t

) = a2b2v + O(a2+ δ) for some δ > 0;(ii) g′ 

> t

is N -invariant; (iii) As t → 0, the family (Zt#M, g ′

> t

) degenerates: the Zt-factor collapses while the M -factor remains at fixed scale. Construction sketch. The gluing identifies: 

• the annular region At(bt, 2bt) ⊆ Zt around zt (at scale bt ≪ inj gt (zt)), and 

• the annular region AN (a−1 

> t

, 2a−1 

> t

) ⊆ N near infinity, via ι(x) = atbtx. This produces an approximate metric g(a,b ) on Zt#M .In the gluing (damage) zone, the curvature of the collapsing factor contributes | Rm( ι∗(a−2b−2gZ )) | =

O(a2b2), and |S(g(a,b ))| = O(a2b2) in the damage zone. The perturbation g′ 

> t

= (1 + ϕ)4/(n−2) g(a,b ) is found by solving the nonlinear scalar curvature equation on Zt#M . The linearized operator L = − 4 

> n−2

(( n − 1)∆ + S) is uniformly invertible on N -invariant functions by Proposition 4.13 (which applies because the spectral condition is inherited from the collapsing factor). The implicit function theorem (Lemma 4.14) gives the perturbation ϕ with ∥ϕ∥Ck,α ≤ Ca 2b2.

Remark 5.1. The VW construction produces new types of degenerations not visible in 

126 Joyce’s original framework: one factor collapses (fibers shrink to zero) while the other (the AF piece) remains non-degenerate. These are natural boundary components of the moduli space of collapsing CSC manifolds, parallel to the ALE bubbles that appear at the boundary of the non-collapsing moduli space (Chapter 3). 

# 5.2 An ε-Regularity Theorem in the Collapsing Setting 

The ε-regularity lemma (Lemma 3.2) is a cornerstone of the non-collapsing moduli space theory: a small Ln/ 2-norm of curvature on a ball implies pointwise curvature control on the half-ball. In the collapsing setting this lemma fails in its naive form, but may hold in the special cases. 

## 5.2.1 Failure in the collapsing setting 

Remark 5.2 (Contrast between collapsing and non-collapsing) . In the non-collapsing case (Tian–Viaclovsky [64, 65], Anderson [3], Bando–Kasue–Nakajima [10]): if (M n, g ) has 

Y (M, [g]) ≥ μ0 > 0 (giving a uniform Sobolev constant), then 

Z 

> Br(x)

| Ric |n/ 2 dV < ε 0 =⇒ sup 

> Br/ 2(x)

| Ric | ≤ Cr2

Z 

> Br

| Ric |n/ 2 dV 

2/n 

.

The Yamabe constant lower bound provides a uniform Sobolev inequality, which is the key input to the Moser iteration. In the collapsing setting, the Sobolev constant degenerates (volume ratios vol( Br)/r n → 0), so the Ln/ 2-norm can be small simply because the volume is small — not because the curvature is pointwise small. See Example 5.1 for an explicit counterexample. 

Example 5.1 (Counterexample to naive ε-regularity with μ0 = 0) . Let (Σ , h ) be a complete non-compact hyperbolic surface with finite total volume ( S(h) = −1) and let (S2, g ) be the 

127 standard sphere ( S(g) = 2 ). The product (S2 × Σ, g × h) is LCF with scalar curvature 

S = 2 − 2 = 0 .Rescale by a > 0: under a2(g × h), we have | Ric | ≡ 2a−2. Since Σ is non-compact with finite volume, for any ε > 0 there exist points x ∈ S2 × Σ near a cusp such that vol a2(g×h)(B1(x)) ≤ 

> ε
> 4

a4. Therefore 

Z

> B1(x)

| Ric |n/ 2 dV ≤ 2n/ 2a−n · ε

4a4 = 2n/ 2ε

4 a4−n,

which is less than ε0 for small a (when n = 4 ). Yet | Ric | = 2 a−2 → ∞ , so the pointwise curvature is large. The naive ε-regularity fails. 

## 5.2.2 The conjecture 

We aim to compactify the moduli space M(n, 0+, C 0) by assuming positive Yamabe and to fully describe the degeneration behavior as metrics approach the boundary of the moduli space, analogous to the K3 case treated in [61]. A central analytic input is an ε-regularity statement for LCF manifolds assuming only a positive Yamabe invariant. 

Conjecture 5.3. (3D ε-regularity for LCF, positive Yamabe) There exist universal constants 

C and ε0 > 0 with the following property. If (M, g ) ∈ M (3 , 0+, C 0) and for some geodesic ball Br one has 

Z

> Br

| Ric |32 dv < ε 0,

then the pointwise bound 

sup 

> Br/ 2

| Ric | ≤ Cr2

 Z

> Br

| Ric |32 dv 

23

holds. 

128 The planned approach is a contradiction / blow-up argument following the strategy in [61]. The main difficulties arise from possible noncompact bubble limit: in dimension four certain bad limits (for example S2 × H2) cannot be easily excluded and require additional input. This will be showed in the futuer work. 

# 5.3 The Full Picture of the LCF Moduli Space 

The Tian–Viaclovsky compactification (Chapter 3) describes the non-collapsing part of the boundary of the LCF moduli space M: GH limits are compact LCF orbifolds with ALE bubble trees. The work of this thesis raises the natural question: what happens at the 

collapsing part of the boundary, where injectivity radii degenerate? In this section we present examples of new degeneration types and discuss the open problems they raise. 

## 5.3.1 Collapsing LCF sequences and their limits 

Example 5.2 (Collapsing to an orbifold limit) . Consider S3 × R with the standard product metric g = dr 2 + gS3 . Via the conformal embedding ϕ : S3 × R → R4 with pull-back metric 

ϕ∗gR4 = dt 2 + t2gS3 (where t = er), define the conformal maps γk : x 7 → e1/k Ax on R4 with 

A = diag(1 , 1, −1, −1) ∈ O(4) .

The lift ϕ∗γk : ( x, t ) 7 → (Ax, t + 1 

> k

) is a free isometry on S3 × R. The quotient 

(Mk, g k) = ( S3 × R/⟨ϕ∗γk⟩, quotient metric ) ∼= S3 ×A S1

is a mapping torus. Since each (Mk, g k) is LCF (the conformal structure descends from R4)with | Rm( gk)| ≤ C, and as k → ∞ :

(Mk, g k) GH 

−−→ (S3/A, g S3/A ),

129 where the limit is an orbifold (the fixed-point set of A on S3 is an S1, giving a codimension-2 singular set). This shows that LCF manifolds can collapse with bounded curvature to an LCF orbifold — a different mechanism from the ALE bubbling in the Tian–Viaclovsky theory. 

Example 5.3 (Collapsing to a manifold with boundary) . Define γk : x 7 → e1/k Akx on R4

with 

Ak =



11cos 2πk − sin 2πk

sin 2πk cos 2πk



.

In spherical coordinates {r, ϕ, θ, γ } on R4, Ak rotates γ 7 → γ +2 π/k . The quotient (Mk, g k) = (S3 × R/⟨ϕ∗γk⟩, quotient ) is again LCF with bounded curvature. As k → ∞ , Ak → Id , so the γ-direction is collapsed. The limiting metric on the remaining coordinates (ϕ, θ ) is dϕ 2 + sin 2ϕ dθ 2, isometric to a hemisphere. Thus 

(Mk, g k) GH 

−−→ (D2, g S2 ),

where D2 ∼= S2+ is the hemisphere — a manifold with boundary . This type of limit is entirely absent from the Tian–Viaclovsky compactification (which gives compact orbifolds without boundary). 

## 5.3.2 Scalar curvature is not preserved under collapsing 

One sever problem is that the lower dimensional limit may have different scalar curvature. Here is one example in the zero Yamabe case. 130 Example 5.4 (Scalar curvature can jump) . Consider (S2 ×H2, g ×h) where g is the standard spherical metric (curvature +1 ) and h is the hyperbolic metric (curvature −1) in the upper half-plane model. Write h = e−2tdx 2 + dt 2 (y = et), so that g × h = g + e−2tdx 2 + dt 2 and 

S(g × h) = 2 − 2 = 0 .Form the quotient (Mk, g k) by the isometry γk : ( θ1, θ 2, x, t ) 7 → (θ1, θ 2, x + 1 /k, t ). As k → ∞ ,the x-direction collapses and 

(Mk, g k) GH 

−−→ (S2 × R, g + dt 2).

But S(gk) ≡ 0 while S(g + dt 2) = S(g) = 2 ̸ = 0 . Scalar curvature is not preserved under collapsing. This phenomenon is explained by the drift Laplacian: the limit scalar curvature involves the relative volume density χ (via the drift Laplacian eigenvalue condition in Theorem 4.1), and the relationship between the scalar curvatures of the collapsing metrics and the base is governed by this non-trivial coupling. 

## 5.3.3 Open problems 

The examples above reveal three new boundary components of the LCF moduli space that lie beyond the Tian–Viaclovsky compactification: 1. Collapsing limits as orbifolds (Example 5.2): the limit is an LCF orbifold, but reached by collapsing rather than by ALE bubbling. 2. Manifolds with boundary as limits (Example 5.3): the limit space has boundary, a qualitatively new phenomenon. 3. Scalar curvature jumps (Example 5.4): CSC sequences can collapse to non-CSC limits. 131 These lead naturally to the following open problems: 1. Compactification of the collapsing moduli space : describe a compact closure of the moduli space of collapsing LCF CSC metrics with bounded curvature, analogous to the Tian–Viaclovsky compactification for the non-collapsing case. 2. ε-regularity in the collapsing setting : prove Conjecture 5.3, which would be the key analytic tool for any such compactification. 3. Full boundary description : classify all Gromov–Hausdorff limits of sequences ( M ni , g i) ∈M (allowing both collapsing and non-collapsing degenerations). The non-collapsing boundary is described by Chapters 3 of this thesis; the collapsing boundary remains an open problem. If Conjecture 5.3 is established, curvature concentration can occur only at finitely many points, and one expects that the collapsing and gluing phenomena constructed in Section §5.1 capture the worst-case degenerations in the boundary of 

M(n, 0+, C 0). 132 Bibliography 

[1] K. Akutagawa. Computations of the orbifold Yamabe invariant. Math. Z. , 271:611–625, 2012. [2] K. Akutagawa and B. Botvinnik. Yamabe metrics on cylindrical manifolds. Geom. Funct. Anal. , 13(2):259–333, 2003. [3] M. T. Anderson. Ricci curvature bounds and Einstein metrics on compact manifolds. 

J. Amer. Math. Soc. , 2(3):455–490, 1989. [4] M. T. Anderson. A survey of Einstein metrics on 4-manifolds. In Surveys in Differential Geometry. Vol. XIII. Geometry, Analysis, and Algebraic Geometry , volume 13 of Surv. Differ. Geom. , pages 1–39. Int. Press, Somerville, MA, 2009. [5] M. T. Anderson and J. Cheeger. cα-compactness for manifolds with ricci curvature and injectivity radius bounded below. J. Differential Geom. , 35(2):265–281, 1992. [6] B. N. Apanasov. Discrete Groups in Space and Uniformization Problems , volume 40 of 

Mathematics and Its Applications . Kluwer Academic Publishers, 1991. [7] T. Aubin. ´Equations diff´ erentielles non lin´ eaires et probl` eme de Yamabe concernant la courbure scalaire. J. Math. Pures Appl. , 55:269–296, 1976. [8] S. Axler, P. Bourdon, and W. Ramey. Harmonic Function Theory , volume 137 of 

Graduate Texts in Mathematics . Springer, 2nd edition, 2001. [9] S. Bando. Bubbling out of Einstein manifolds. Tohoku Math. J. (2) , 42(2):205–216, 1990. [10] S. Bando, A. Kasue, and H. Nakajima. On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth , volume 97. 1989. [11] R. Bartnik. The mass of an asymptotically flat manifold. Comm. Pure Appl. Math. ,39(5):661–693, 1986. [12] A. L. Besse. Einstein Manifolds , volume 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete . Springer, 1987. [13] O. Biquard. D´ esingularisation de m´ etriques d’Einstein, I. Invent. Math. , 192(1):197– 252, 2013. 133 [14] R. Brooks. The bottom of the spectrum of a Riemannian covering. J. Reine Angew. Math. , 357:101–114, 1985. [15] G. Carron and M. Herzlich. Conformally flat manifolds with nonnegative ricci curvature. 

Compositio Mathematica , 142(3):798–810, 2006. [16] J. Cheeger. Finiteness theorems for riemannian manifolds. In Am. J. Math. , volume 92, pages 61–74, 1970. [17] J. Cheeger and T. H. Colding. On the structure of spaces with ricci curvature bounded below. I. J. Differential Geom. , 46(3):406–480, 1997. [18] J. Cheeger and D. G. Ebin. Comparison Theorems in Riemannian Geometry . North-Holland, 1975. [19] J. Cheeger, K. Fukaya, and M. Gromov. Nilpotent structures and invariant metrics on collapsed manifolds. J. Amer. Math. Soc. , 5(2):327–372, 1992. [20] B.-L. Chen, S.-H. Tang, and X.-P. Zhu. Complete classification of compact four-manifolds with positive isotropic curvature. J. Differential Geom. , 91(1):41–80, 2012. [21] X. Dai. Positive mass theorem for spaces with isolated conical singularities, 2025. Preprint. [22] B. Devyver and K. Kroencke. Lp-cohomology and Hodge decompositions for ALE spaces. J. Geom. Anal. , 28:2481–2528, 2018. [23] M. P. do Carmo. Riemannian Geometry . Mathematics: Theory & Applications. Birkh¨ auser, 1992. [24] L. C. Evans. Partial Differential Equations , volume 19 of Graduate Studies in Mathe-matics . American Mathematical Society, 2nd edition, 2010. [25] B. Farb and D. Margalit. A Primer on Mapping Class Groups , volume 49 of Princeton Mathematical Series . Princeton University Press, 2012. [26] K. Fukaya. Collapsing of riemannian manifolds and eigenvalues of laplace operator. 

Invent. Math. , 87:517–547, 1987. [27] K. Fukaya. Collapsing of Riemannian manifolds and eigenvalues of Laplace operator. 

Invent. Math. , 87(3):517–547, 1987. [28] K. Fukaya. Collapsing Riemannian manifolds to ones of lower dimensions. J. Differential Geom. , 25(1):139–156, 1987. [29] K. Fukaya. A boundary of the set of the riemannian manifolds with bounded curvatures and diameters. J. Differential Geom. , 28(1):1–21, 1988. [30] D. Gilbarg and N. S. Trudinger. Elliptic Partial Differential Equations of Second Order .Classics in Mathematics. Springer, 2nd edition, 2001. 134 [31] A. Grigor’yan. Analytic and geometric background of recurrence and non-explosion of the Brownian motion on Riemannian manifolds. Bull. Amer. Math. Soc. (N.S.) ,36(2):135–249, 1999. [32] M. Gromov. Almost flat manifolds. J. Differential Geom. , 13(2):231–241, 1978. [33] R. S. Hamilton. Four-manifolds with positive isotropic curvature. Comm. Anal. Geom. ,5:1–92, 1997. [34] Y. Imayoshi and M. Taniguchi. An Introduction to Teichm¨ uller Spaces . Springer, 1992. [35] H. Izeki. On the decomposition of conformally flat manifolds. Journal of the Mathe-matical Society of Japan , 45(1):105–119, 1993. [36] H. Izeki. Limit sets of Kleinian groups and conformally flat Riemannian manifolds. 

Invent. Math. , 122(3):603–625, 1995. [37] H. Izeki. A deformation of flat conformal structures. Transactions of the American Mathematical Society , pages 4939–4964, 1996. [38] D. Joyce. Constant scalar curvature metrics on connected sums. Int. J. Math. Math. Sci. , (7):405–450, 2003. [39] T. Ju and J. Viaclovsky. Conformally prescribed scalar curvature on orbifolds. Com-munications in Mathematical Physics , 398(2):877–923, 2023. [40] B. Kleiner and J. Lott. Notes on Perelman’s papers. Geom. Topol. , 12(5):2587–3024, 2008. [41] P. Koebe. ¨Uber die uniformisierung beliebiger analytischer kurven. Nachr. Ges. Wiss. G¨ ottingen , pages 191–210, 1907. [42] R. S. Kulkarni and U. Pinkall. Conformal Geometry , volume 12 of Aspects of Mathe-matics . Vieweg, 1988. [43] C. LeBrun. Counter-examples to the generalized positive action conjecture. Communi-cations in Mathematical Physics , 118(4):591–596, 1988. [44] D. A. Lee and P. G. LeFloch. The positive mass theorem for manifolds with distribu-tional curvature. Comm. Math. Phys. , 339(1):99–120, 2015. [45] J. M. Lee and T. H. Parker. The Yamabe problem. Bull. Amer. Math. Soc. (N.S.) ,17(1):37–91, 1987. [46] A. Naber and R. Zhang. Topology and ε-regularity theorems on collapsed manifolds with ricci curvature bounds. Geom. Topol. , 20(5):2575–2664, 2016. [47] S. Nayatani. Patterson-Sullivan measure and conformally flat metrics. Mathematische Zeitschrift , 225:115–131, 1997. 135 [48] T. Ozuch. Noncollapsed degeneration and desingularization of Einstein 4-manifolds. 

Geom. Topol. , 26(4):1483–1579, 2022. [49] S. Peters. Convergence of riemannian manifolds. Compositio Math. , 62(1):3–16, 1987. [50] P. Petersen. Riemannian Geometry , volume 171 of Graduate Texts in Mathematics .Springer, 3rd edition, 2016. [51] H. Poincar´ e. Sur l’uniformisation des fonctions analytiques. Acta Math. , 31:1–63, 1907. [52] E. A. Ruh. Almost flat manifolds. J. Differential Geom. , 17(1):1–14, 1982. [53] R. Schoen. Conformal deformation of a Riemannian metric to constant scalar curvature. 

J. Differential Geom. , 20(2):479–495, 1984. [54] R. Schoen, L. Simon, and S.-T. Yau. Curvature estimates for minimal hypersurfaces. 1975. [55] R. Schoen and S.-T. Yau. On the proof of the positive mass conjecture in general relativity. Comm. Math. Phys. , 65(1):45–76, 1979. [56] R. Schoen and S.-T. Yau. On the proof of the positive mass conjecture in general relativity. Comm. Math. Phys. , 65:45–76, 1979. [57] R. Schoen and S.-T. Yau. On the structure of manifolds with positive scalar curvature. 

Manuscripta Math. , 28:159–183, 1979. [58] R. Schoen and S.-T. Yau. Proof of the positive mass theorem. II. Comm. Math. Phys. ,79(2):231–260, 1981. [59] R. Schoen and S.-T. Yau. Conformally flat manifolds, Kleinian groups and scalar cur-vature. Invent. Math. , 92(1):47–71, 1988. [60] A. Selberg. On discontinuous groups in higher-dimensional symmetric spaces. In Con-tributions to function theory , pages 147–164. Tata Institute of Fundamental Research, 1960. [61] A. Sun and J. Zhang. Local fibration structure theorem for collapsed riemannian man-ifolds. arXiv preprint , 2020. arXiv:2004.09990. [62] S. Sun and R. Zhang. Collapsing geometry of hyperk¨ ahler 4-manifolds and applications. 

Acta Math. , 232(2):325–424, 2024. [63] W. P. Thurston. The Geometry and Topology of Three-Manifolds . Princeton University, 1980. Princeton lecture notes, Chapter 13 (Orbifolds). [64] G. Tian and J. Viaclovsky. Bach-flat asymptotically locally Euclidean metrics. Invent. Math. , 160(1):19–54, 2005. [65] G. Tian and J. Viaclovsky. Moduli spaces of critical Riemannian metrics in dimension four. Adv. Math. , 196(2):346–372, 2005. 136 [66] G. Tian and J. Viaclovsky. Volume growth, curvature decay, and critical metrics. Com-ment. Math. Helv. , 83(4):889–911, 2008. [67] N. S. Trudinger. Remarks concerning the conformal deformation of Riemannian struc-tures on compact manifolds. Ann. Scuola Norm. Sup. Pisa , 22:265–274, 1968. [68] J. Viaclovsky and X. Wang. Collapsing constant scalar curvature metrics, 2026. In preparation. [69] X. Wang. On the structure of locally conformally flat orbifolds and ale manifolds. arXiv preprint arXiv:2511.09857 , 2025. [70] E. Witten. A new proof of the positive energy theorem. Comm. Math. Phys. , 80(3):381– 402, 1981. [71] E. Witten. A new proof of the positive energy theorem. Comm. Math. Phys. , 80(3):381– 402, 1981. [72] H. Yamabe. On a deformation of Riemannian structures on compact manifolds. Osaka Math. J. , 12:21–37, 1960. 137 Appendix A The proof of Cheeger-Fukaya-Gromov Theorem 

# A.1 Proof of Theorem 1.11 

We will first construct such C2,α fibration map under the assumption, follows the idea of the proof of Proposition 6.6 of [46]. 

Step 1 : the existence of local fibration map. We first fix a scale ϵ > 0 and consider the rescaled metric g′ 

> i

:= ϵ−2gi converge to g′∞ =

ϵ−2g∞. By the assumption, for any sequence {xi} with xi ∈ M ni and xi → x ∈ Xd and the ball ( B4(xi), g ′

> i

) → (B4(x), g ′∞) in the Gromov-Hausdorff sense. We can choose the scaling parameter ϵ so small such that (1) The Gromov-Hausdorff distance ( B4(x), g ′∞) with the Euclidean ball B4(0 d) is less than 

ϵ;(2) The Ricci curvature Ric( gi) ≥ − (n − 1) ϵ.138 (3) The harmonic radius of g′∞ is greater than 3. Then, we can use the construction of harmonic function from Section 6 of [17]. For every i

large, there exists a harmonic map Φixi : B2(xi) → Rd (A.1) such that Φ ixi : B2(xi) → B2(0 d) is a τ (ϵ)-Gromov-Hausdorff approximation with the follow-ing gradient estimate 

|∇ Φi,α xi |(p) ≤ 1 + τ (ϵ), (A.2) and the integral estimate 1vol( B2(xi)) (

> d

X

> α,β =1

Z

> B2(xi)

|⟨∇ Φi,α xi , ∇Φi,β xi ⟩ − δα,β |dvol gi +

> d

X

> α=1

Z

> B2(xi)

| Hess Φ i,α xi |2dvol gi ) < τ (ϵ).

(A.3) To get pointwise C2,α esimate for Φ ixi , consider the pull-back metric ( B2(0 n), ˆg′

> i

), where we define ˆ g′ 

> i

:= exp ∗ 

> xi

g′ 

> i

as the pull-back metric on the local universal cover B2(0 n) ⊆ Rn.Then, the pull-back function ˆΦixi := Φ ixi ◦ exp xi is harmonic. By our curvature assumption, the conjugate radius is bounded from below and thus the injective radius of ( B2(0 n), ˆg′

> i

) is bounded from below. Thus, we have the metric, under a suitable coordinate, is uniformly 

C1,α bounded. Thus, the coefficient of the Lapalcian ∆ ˆg′ 

> i

is uniform C0,α bounded. Thus, we can apply the standard Schauder estimate and conclude pointwise C2,α esimate 

∥Φi,α xi ∥C2,α (B1(xi)) < C (n). (A.4) To check the nondegeneracy, we need to show that there is no critical point in B1(xi). In 139 fact, we want to show the following pointwise estimate: 

> d

X

> α,β =1

|⟨∇ Φi,α xi , ∇Φi,β xi ⟩ − δα,β | < τ (ϵ). (A.5) This can be proved by combining uniform relative volume comparison and a compactness argument. On the limit X. By our assumption, X is a compact Riemannian manifold. Let B3(xi)converges to B3(x∞) ⊆ X. Then, there exists harmonic coordinate system 

Hx∞ = ( u1, ..u d) : B3(x∞) → Rd (A.6) with the point-wise estimate Pdα,β =1 |⟨∇ uα, ∇uβ ⟩ − δα,β | < τ (ϵ), and uniform C2,α estimate. Thus, we can define a local map Fxi = H−1 

> x∞

◦ Φixi : B1(xi) → B1(x∞), with point-wise C2,α 

estimate. By choosing ϵ small enough, there is no critical point and thus defines a local fiber bundle with fiber of dimension n − d.

Step 2 : get a global fibration map via patching. Again, we fix the scaling ϵ as well. Now, we want to define a partition of unit for each 

Mi when i is large with uniform C2,α estimate. First, we need to construct a set of cut off function centered at any pi ∈ Mi with the cutting radius 1. In another, we want to find ψpi

so that: 

ψpi (x) = 



1, x ∈ B12

(pi)0, x ∈ Mi \ B1(pi)(A.7) for every pi with ∥ψpi ∥C2,α ≤ C, which is independent of i. This cut-off function is constructed 140 in Theorem 6.33 of [17]. First, we construct the following functions: 



∆kpi = κ, x ∈ B1(pi) \ B12

(pi)

kpi = 1 , x ∈ ∂B 12

(pi)

kpi = 0 , x ∈ ∂B 1(pi).

(A.8) For some κ > 0, which only depends on the dimension. Take Ψ : R → [0 , 1] as a smooth cut-off function. Then, we construct ψpi = Ψ ◦ kpi . It is the desired cut-off function by [17]. We care about its regularity. By our curvature boundedness assumption, the coefficient of the Laplacian is uniform C0,α bounded, so by Schauder estimate, we can improve the regularity of such cut-off function to C2,α , follow the argument of [17]. We can construct the partition of unity with uniform C2,α estimate now. We choose a cover 

{B1(qk)}Nk=1 so that Mi ⊆ ∪ Nk=1 B1(qk) and we define the partition of unity subordinate to this cover by: 

ϕk = ψqk

PNj=1 ψqj

. (A.9) Note that N is uniformly bounded by bounded curvature of the sequence and non-collapsing assumption of X.To patch local fibration maps together, we need to introduce the following function on X to determine the image of the fibration. Define the distance-like function: 

ηq∞ : B1(q∞) × B1(q∞) → R+, (x, y ) 7 →

> d

X

> α=1

|uα(x) − uα(y)|2 (A.10) and the global distance-like function η : Mi × X → R+:

η(pi, p ∞) = 

> N

X

> k=1

ϕkηqk 

> ∞

(Fqk (pi), p ∞). (A.11) 141 On each local chart Hpk 

> ∞

, by the harmonic coordinate estimate, |ηq∞ − d2 

> g′∞

| ≤ τ (ϵ). Thus, it can be easily seen that η(pi, ·) is a convex function on X, hence has a unique minimum, 

ρ(pi). Thus, we can define the global map: 

Fi : Mi → X, pi 7 → ρ(pi). (A.12) Now, we examine the regularity. Note ηq∞ is smooth, then η(pi, ·) is smooth function, C2,α 

in pi varaible. Consider G(pi, y ) = ∇yη(pi, y ). By convexity, ∇yG(pi, y ) > 0. Thus, by the implicit function theorem, the map pi 7 → ρ(pi) is C2,α . It is a well-defined map, with 

dg′∞ (Fi(pi), F xi (pi)) ≤ τ (ϵ) and 

|⟨∇ Φi,α xi , ∇Φi,β xi ⟩ − ⟨∇ (Fi ◦ Hx∞ )α, ∇(Fi ◦ Hx∞ )β ⟩| ≤ τ (ϵ). (A.13) Similarly, Fi is a C2,α fibration map with fiber of dimension n − d.Now, we shall prove the rest of the theorem. To show the C0,α bound for the fiber second fundamental form. Note that we have: 

AF −1 

> i(x)

(V, W ) = Hess Fi(V, W )

|∇ Fi| (A.14) for V, W ∈ ker( dF i). Thus, we have: 

∥AF −1 

> i(x)

∥C0,α ≤ C(n)∥Fi∥C2,α . (A.15) To show that Fi is an almost-Riemannian submersion, we can use the contradiction argument given in [61]. Suppose not, there exists a sequence of vector vi ∈ Txi Mi, perpendicular to the fiber direction, and a constant τ0 ≥ 0 so that ||dF i(vi)|g∞

> |vi|gi

− 1| ≥ τ0. We may assume |vi|gi = 1. Consider the local equivariant Gromov-Hausdorff convergence of local universal cover 142 ( ˜B˜xi (r), ˜gi, G i) ( ˜B˜x∞ (r), ˜g∞, G ∞)(Bxi (r), g i) (Bx∞ (r), g ∞) 

> C1,α
> πiπ∞
> GH

where πi is the local universal cover map, π∞ is a Riemannian submersion. Thus, ˜Fi = Fi ◦πi

converges to π∞ in C2,β . Let ˜ vi be a lift of vi. Thus, ˜ vi converges to ˜ v∞ with |dπ ∞ ˜v∞| = 1. This violates the assumption ||dF i(vi)|g∞

> |vi|gi

− 1| ≥ τ0.143 Appendix B Orbifold Points in Pairs 

This appendix proves Theorem 3.17: in an oriented compact LCF orbifold with positive Yamabe invariant, the orbifold singular points appear in antipodal pairs. The proof uses the following lemma from the theory of discrete groups. 

# B.1 A Lemma on Hyperbolic Elements 

Lemma B.1 ([6], p. 52) . Let g1, g 2 ∈ G ≤ C(n), where g1 is hyperbolic (has exactly two fixed points on Sn and expansion factor α̸ = 1 ). If g1 and g2 have precisely one common fixed point, then G is not discrete. Proof. Without loss of generality let the common fixed point be ∞, and write Sn = Rn ∪{∞} .Since g1 is hyperbolic with g1(∞) = ∞ and g1(0) = 0 (the second fixed point of g1, which is different from ∞ by assumption), and g2(∞) = ∞ but g2(0) ̸ = 0, we may write 

g1(x) = αU 1x, g2(x) = βU 2x + b, 

where α ∈ (0 , 1) (replacing g1 by g−11 if necessary), β > 0, U1, U 2 ∈ O(n), and b ∈ Rn \ { 0}.144 Consider the sequence of M¨ obius transformations 

hk = g2gk 

> 1

g−12 g−k 

> 1

.

A direct computation gives 

hk(x) = U2U k 

> 1

U −12 U −k 

> 1

(x) − αkU2U k 

> 1

U −12 (b) + b. 

Case 1 : U m 

> 1

= Id for some m ≥ 1. Setting k = jm :

hjm (x) = x − αjm b + b j→∞ 

−−−→ x + b. 

The limit x 7 → x + b is a parabolic (non-identity) M¨ obius transformation. Hence G contains elements hjm accumulating at x 7 → x + b̸ = Id, so G is not discrete. 

Case 2 : U1 has infinite order. For any ε > 0, there exists kε ≥ 1 with |U kε 

> 1

(y) − y| < ε 

for all y ∈ B(0 , r ) (by the pigeonhole principle for the compact group ⟨U1⟩ ≤ O(n)). Then 

|hkε (x) − (x + b)| ≤ | αkε | | b| + Cε → 0 as ε → 0 (taking kε → ∞ simultaneously). Again 

hkε → x + b, so G is not discrete. 

# B.2 Proof of Theorem 3.17 

Theorem B.2 (Fixed points appear in pairs; Theorem 3.17 restated) . Let G ≤ C(n) be a discrete group acting on Sn properly discontinuously, with limit set Λ and no parabolic elements. Assume dim H Λ < (n − 2) /2. Let Γ ≤ G be a local isotropy subgroup with isolated fixed points. Then the fixed points of Γ appear in pairs unless the quotient Sn/G is non-orientable. Proof. Let s ∈ Sn be a fixed point of some non-trivial γ ∈ Γ. By Lemma 3.16, Γ is (conjugate 145 to) a finite subgroup of O(n). For any A ∈ O(n) acting on Sn, if it has an isolated fixed point s, then −s is also a fixed point (since A ∈ O(n) and the eigenvectors come in ± pairs over R for the action on Rn ⊂ Rn+1 with Sn−1 the unit sphere). Explicitly: if As = s,

s ∈ Sn ⊂ Rn+1 , then A(−s) = −As = −s. So Γ also fixes −s ∈ Sn.It remains to show that s and −s lie in different G-orbits (i.e., they correspond to two distinct orbifold points of M = Ω /G ) unless the quotient is non-orientable. Suppose −s is in the same G-orbit as s. We treat two cases. 

Case 1 : −s / ∈ Λ (so −s ∈ Ω, the domain of discontinuity). Then there exists γ0 ∈ G with γ0(s) = −s. Set s = 0 and −s = ∞ in the stereographic chart. By Corollary 1.8 of [6], since γ0 maps 0 7 → ∞ and preserves coordinate spheres centered at 

s (because the local group Γ fixes s and γ0 maps s 7 → − s), we can write γ0(v) = r2U v/ |v|2

for some U ∈ O(n) (the term q′ = 0 since γ0 maps round spheres St to round spheres SR

centered at ∞). Then γ20 (v) = U 2v, so γ20 fixes s = 0. Since γ0 has no fixed points in Ω (it maps 0 7 → ∞ 

with 0 , ∞ /∈ Ω), γ20 |Ω is a deck transformation fixing s. By assumption γ20 ∈ Γ (a finite group), so γ2m 

> 0

= Id for some m. Since dim H(Sn \ Ω) = dim H Λ < (n − 2) /2, by the Liouville theorem (Theorem 2.9) a conformal map agreeing with the identity on a set of positive Hausdorff dimension ( n − 2) /2 must be the identity globally; hence γ2m 

> 0

= Id as a M¨ obius transformation. We may assume γ20 = Id, so U 2 = Id and U = A−1DkA for some A ∈ O(n)and diagonal Dk with k entries +1 and n − k entries −1. The element γ0 fixes a Sk ⊂ Sn; the condition dim H Λ < (n − 2) /2 requires k < (n − 2) /2. 

• If Dk = −Id ( k = −1, i.e. U = −Id): For odd n, the composition γ0 ◦ α (where α is a generator of Γ) fixes a Sn−1, creating a non-isolated fixed point — contradicting that Γ has only isolated fixed points. For even n, γ0 is orientation-reversing, so the quotient 146 Sn/G is non-orientable. 

• If k ≥ 0: The fixed Sk lies in Λ, violating dim H Λ < (n − 2) /2 for k ≥ (n − 2) /2. For smaller k, a similar parity argument produces either a non-isolated fixed point (contradiction) or an orientation-reversing element (non-orientable quotient). 

Case 2 : −s ∈ Λ. We claim −s is not a hyperbolic fixed point of G. Suppose otherwise: let h ∈ G be hyperbolic with lim k→∞ hk(x) = −s for all x ∈ Ω. Since s / ∈ Λ by assumption, the other fixed point of 

h is some s0̸ = s with lim k→∞ h−k(x) = s0.For any δ ∈ Γ, the conjugate δ−1hδ ∈ G is also hyperbolic with fixed points −s (preserved since Γ fixes s and −s) and δ−1(s0). Since δ(s) = s, we have δ−1(s0)̸ = s in general. Hence 

h and δ−1hδ are both hyperbolic with the single common fixed point −s. By Lemma B.1, 

G is not discrete — contradiction. Therefore −s is not a hyperbolic fixed point of G, and by the classification of elements of 

C(n) (elliptic, parabolic, hyperbolic), −s cannot be in Λ as an attracting fixed point of any hyperbolic element. Since G has no parabolic elements by assumption and the only remaining option (elliptic fixed points with −s ∈ Λ) leads to dim H Λ ≥ (n − 2) /2 (a contradiction with the hypothesis), Case 2 cannot occur. In both cases, the assumption that s and −s are in the same G-orbit leads to a contradiction (or a non-orientable quotient). Hence in the orientable case, s and −s lie in different G-orbits, giving a pair of distinct antipodal orbifold points. Since the antipodal involution is a fixed-point-free pairing on the set of orbifold singular points, that set has even cardinality. 147


## Native file acquisition

```json
[
  {
    "url": "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf",
    "name": "qt31v740r5.pdf",
    "size": 0,
    "role": "primary_object_file",
    "status": "download_failed",
    "error": "invalid_content",
    "http_status": 0,
    "reason": "object download returned an HTML landing/error page",
    "retry_after": 0,
    "identity_bound": true,
    "parent_url": "https://escholarship.org/content/qt31v740r5/qt31v740r5.pdf",
    "primary_label": false,
    "download_eligible": true,
    "label": ""
  }
]
```
