---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: gluing manifolds with boundary and bordisms - Scholars' Bank]

Theorem A.1.2. [29, Corollary 6.3] Let Ω ⊂ Rn be an open set and let α ∈ (0 , 1) .Suppose u ∈ C2,α (Ω) satisfies a uniformly elliptic equation 

Lu = aij (x)uij + bi(x)ui + c(x)u = 0 

with aij , b i, c ∈ Cα(Ω) and ellipticity constant λ > 0. If Ω′ ⊂⊂ Ω with dist Ω(Ω ′, ∂ Ω) = 

d, then there is a constant C > 0, depending on d, λ, || aij || Cα(Ω) , || bi|| Cα(Ω) , || c|| Cα(Ω) , n ,and α, such that 

|| u|| C2,α (Ω ′) ≤ C|| u|| C0(Ω) . (A.2) 

A.2. The Minimal Graph Equation 

This section is concerned with local properties of hypersurfaces in Riemannian manifolds. Throughout this section we will consider the unit ball in Euclidian space 

B = B1(0) ⊂ Rn+1 equipped with a Riemannian metric g and a hypersurface Σ n ⊂ B.The balls of radius s > 0 centered at x ∈ Σ induced by g and g|Σ are denoted by 

Bgs (x) ⊂ B and BΣ 

> s

(x) ⊂ Σ, respectively. Assume there is a point x0 ∈ Σ ∩ B1/4(0). The following straight-forward Riemannian version of [30, Lemma 2.4] allows us to consider Σ locally as a graph over Tx0 Σ. 111 Lemma A.2.1. There is a constant μ0 > 0 so that if g satisfies 

sup 

> x∈B

|gij (x) − δij | ≤ μ0, sup 

> x∈B

∣∣∣∂g ij  

> ∂x k

(x)

∣∣∣ ≤ μ0 (A.3) 

for 1 ≤ i, j, k ≤ n + 1 in standard Euclidian coordinates, then the following holds: If 

s > 0 satisfies 

dist Σ(x0, ∂ Σ) ≥ 3s, sup Σ |Ag|2 ≤ 120 s2 ,

then there is an open subset U ⊂ Tx0 Σ ⊂ Rn+1 , a unit vector η normal to Tx0 Σ, and a function u : U → R such that 1. graph( u) = BΣ2s(x0);2. |∇ u| ≤ 1 and |∇∇ u| ≤ 1 

> s√2

hold pointwise. Moreover, the connected component of Bgs (x0) ∩ Σ containing x0 lies in BΣ2s(x0).

Now we will give a useful expression for the mean curvature of a graph. Let 

U ⊂ Rn be an open set with standard coordinates x′ = ( x1, . . . , x n) and let g be a Riemannian metric on U × R ⊂ Rn+1 . For a function u : U → R, consider its graph graph( u) = {(x′, u (x′)) ∈ Rn+1 : x′ ∈ U }.

For i = 1 , . . . , n , we have the tangential vector fields Ei = ∂∂x i + ∂u ∂x i 

> ∂∂x n+1

and the upward-pointing unit vector field ν normal to graph( u). Writing hij = g(Ei, E j ) for 112 the restriction metric, the mean curvature of graph( u) can be written 

Hg = hij g(ν, ∇Ei Ej )=

(

gij − ∇iu∇j u

> 1+ |∇ u|2

) [ ∂2u∂x i∂x j + Γ n+1  

> ij

+ ∂u ∂x i Γn+1   

> n+1 j

+ ∂u ∂x j Γn+1   

> n+1 i

+ ∂u ∂x i 

> ∂u ∂x j

Γn+1  

> n+1 n+1

− ∂u ∂x r

(

Γrij + ∂u ∂x i Γrn+1 j + ∂u ∂x j Γri n +1 + ∂u ∂x i 

> ∂u ∂x j

Γrn+1 n+1 

) ] 

,

(A.4) see [30, Section 7.1] for a detailed exposition in the 3-dimensional case. Next, we will apply the Schauder estimates to the geometric setting in Section 3.2. 

Corollary A.2.1. Suppose the unit ball B = B1(0) ⊂ Rn+1 is equipped with a Riemannian metric g satisfying sup 

> x∈B

|gij (x) − δij | ≤ μ0, sup 

> x∈B

∣∣∣∣

∂g ij 

∂x k (x)

∣∣∣∣ ≤ μ0

in Euclidian coordinates for all 1 ≤ i, j, k ≤ n + 1 where μ0 is the constant from Lemma A.2.1. Let C > 0 be given and set r = min( 18 , 1√80 C ). Assume that Σ ⊂ B is a properly embedded minimal hypersurface with respect to g such that sup B |Ag|2 ≤ C

and there is a point x0 ∈ Br(0) ∩ Σ. Then there is a smooth function u : U → R on 

U ⊂ Tx0 Σ and a unit normal vector to Tx0 Σ such that 1. graph( u) = BΣ2r(x0); 2. |∇ u| ≤ 1 and |∇∇ u| ≤ 1 

> s√2

hold pointwise; 113 3. for each k ≥ 1 and α ∈ (0 , 1) there is a constant C′ > 0, depending only on 

n, k, α, and || g|| Ck,α (B), such that 

|| u|| Ck,α (U ) ≤ C′. (A.5) Moreover, the connected component of Br(x0) ∩ Σ containing x0 is contained in 

BΣ2r(x0). 

Proof. The choice of radius r allows us to apply Lemma A.2.1 to obtain an open subset U ⊂ Tx0 Σ ⊂ Rn+1 , a unit vector η normal to Tx0 Σ, and a smooth function 

u : U → R such that graph( u) = BΣ2s(x0), |∇ u| ≤ 1, and |∇∇ u| ≤ 1 

> s√2

on U . Since Σ is minimal, u solves equation H = 0. Now since || u|| C1,α (U ) is bounded for any fixed 

α ∈ (0 , 1), one can inspect the expression A.4 to see that u solves a linear elliptic equation with coefficients bounded in Cα in terms of μ0 and r. This allows us to apply Theorem A.1.2 to obtain the estimate || u|| C2,α (U ′) ≤ C|| u|| C0(U ) for some C > 0depending only on μ0 and r. Standard elliptic estimates [29, Section 6] give a similar estimate in the Ck,α -norm for any k.

A.3. Details on Theorem 1.5.4 

Let us recall some basic notions from theory of integer multiplicity currents. The main reference for this material is [15, Chapter 4]. For an open subset U ⊂ Rn+k, let Ω n(U ) denote the space of all n-forms on Rn+k

with compact support in U . An n-current on U is a continuous linear functional 

T : Ω n(U ) → R and collection of such T for a vector space Dn(U ). The boundary of 114 an n-current T is the ( n − 1)-current ∂T defined by (∂T )( ω) = T (dω ), ω ∈ Ωn−1(U ).

The mass of T ∈ D n(U ) is given by M(T ) = sup {T (ω) : ω ∈ Ωn(U ), |ω| ≤ 1}. For example, if T is given by integration along a smooth oriented submanifold M , then 

M(T ) = Vol( M ). Let Hn denote the n-dimensional Hausdorff measure on Rn+k. A current T ∈Dn(U ) is called integer multiplicity rectifiable (or simply rectifiable ) if it takes the form 

T (ω) = 

∫

> M

ω(ξ(x)) θ(x)dHn(x), ω ∈ Ωn(U ), where (A.6) 1. M ⊂ U is Hn-measurable and countably n-rectifiable, see [15, Section 3.2.14]; 2. θ : M → Z is locally Hn-integrable; 3. for Hn-almost every x ∈ M , ξ : M → ΛnT Rn+k takes the form ξ(x) = e1∧. . . ∧en

where {ei}ni=1 form an orthonormal basis for the approximate tangent space 

TxM , see [15, Section 3.2.16]. 

Remark A.3.1. The above definition of integer multiplicity rectifiable currents can also be extended to Riemannian manifolds ( M, g ) – one defines the mass of a current using the Hausdorff measure given by the metric g.The regular set reg( T ) of a rectifiable n-current T is given by the set of points x ∈

spt( T ) for which there exists an oriented n-dimensional oriented C1-submanifold M ⊂

U , r > 0, and m ∈ Z satisfying 

T |Br (x)(ω) = m ·

∫  

> M∩Br(x)

ω, ∀ω ∈ Ωn(U ).

115 The singular set sing( T ) is given by spt( T ) \ reg( T ). The abelian group of n-dimensional integral flat chains on U is given by 

Fn(U ) = {R + ∂S : R ∈ D n(U ) and S ∈ D n+1 (U ) are rectifiable }.

Now we consider subsets B ⊂ A ⊂ U . We have the group of integral flat cycles 

Cn(A, B ) = {T ∈ F n(U ) : spt( T ) ⊂ A, spt( ∂T ) ⊂ B, or n = 0 }

and the subgroup of integral flat boundaries 

Bn(A, B ) = {T + ∂S : T ∈ F n(U ), spt( T ) ⊂ B, S ∈ F n+1 (U ), spt( S) ⊂ A}.

The quotient groups Hn(A, B ) = Cn(A, B )/Bn(A, B ) are the n-dimensional integral current homology groups .There is a natural transformation between the integral singular homology functor and the integral current homology functor which induces an isomorphism 

Hn(A, B ; Z) ∼= Hn(A, B ) in the category of local Lipschitz neighborhood retracts, see [15, Section 4.4.1]. This isomorphism can be combined with a basic compactness result for rectifiable currents to find volume minimizing representatives of homology classes. 

Lemma A.3.1. Let (M, ¯g) be a compact (n + 1) -dimensional Riemannian manifold with boundary and consider an integral homology class α ∈ Hn(M, ∂M ; Z). Let ˜α ∈

Hn(M, ∂M ) be the image of α under the isomorphism Hn(M, ∂M ; Z) → Hn(M, ∂M ).Then there exists a homologically volume minimizing integer multiplicity rectifiable current T ∈ ˜α.

116 Proof. By the Nash embedding theorem there is an isometric embedding ι : M →

Rn+k for some sufficiently large k. Let ˆM be the image of this embedding and set ˆα = ι∗ ˜α ∈ Hn( ˆM , ∂ ˆM ). Applying the compactness result in [15, Section 5.1.6], we obtain a homologically volume minimizing current ˆT ∈ C n( ˆM , ∂ ˆM ) representing ˆ α.Since ι is an isometry, ( ι−1)∗ ˆT is the desired current. Since Lemma A.3.1 guarantees the existence of homologically volume minimizing representative for the homology class α from the hypothesis of Theorem 1.5.4, the final ingredient is regularity theory for volume minimizing rectifiable currents with free boundary. The following is a regularity theorem due to M. Gr¨ unter [17, Theorem 4.7] adapted to the context of an ambient Riemannian metric. See [18, 22, 31] for Riemannian adaptations of similar results. 

Theorem A.3.2. Let S ⊂ Rn+1 be an n-dimensional smooth submanifold, U ⊂

Rn+1 an open set with ∂S ∩ U = ∅, and g a Riemannian metric on U with bounded injectivity radius and sectional curvature. Suppose T ∈ F n(U ) with spt( ∂T ) ⊂ S

satisfies Mg(T ) ≤ Mg(T +R) for all open W ⊂⊂ U and all R ∈ F n(U ) with spt( R) ⊂

W and spt( ∂R ) ⊂ S. Then we have 

– sing( T ) = ∅ if n ≤ 6

– sing( T ) is discrete for n = 7 

– dim H(sing( T )) ≤ n − 7 if n > 7

where dim H(A) denotes the Hausdorff dimension of a subset A ⊂ U .

We will briefly explain how Theorem 1.5.4 follows from Theorem A.3.2. Let 

T be the volume minimizing representative of ¯ α from Theorem 1.5.4. For a point 117 x ∈ spt( T ), set φ = exp ¯gx and consider 

U = φ−1(B¯gr′ (x)) ⊂ TxM, S = φ−1(∂M ∩ B¯gr (x)) ,T ′ = ( φ−1)∗T ∈ D n(U ), g = ( φ−1)∗ ¯g, 

where 0 < r ′ < r ≤ inj(¯ g). By Theorem A.3.2, the singular set of T ′ is empty and so there is a neighborhood V of 0 ∈ U such that T ′|V is given by an integer multiple of integration along a C1-submanifold M ⊂ V . Locally, M can be written as the graph of a C1-function which weakly solves the minimal surface equation. Standard elliptic PDE methods imply that M is smooth, see, for instance the proof of Lemma A.3.3 below. 

A.31. Doubling minimal hypersurfaces with free boundary 

In this section we consider the reflection of a free boundary stable minimal hypersurface over its boundary. To fix the setting, let ( M, ¯g) be an ( n+1)-dimensional compact oriented Riemannian manifold with boundary ∂M and restriction metric 

g = ¯g|∂M . Assume that there is a neighborhood of the boundary on which ¯g = g∂M + dt 2. The double of ( M, ¯g) is the smooth closed manifold MD given by 

MD = M ∪∂M (−M ). Notice that the double MD comes equipped with an involution 

ι : MD → MD which interchanges the two copies of M and fixes the doubling locus 

∂M ⊂ MD. Since ¯ g splits as a product near the boundary, one can also form the smooth doubling of ¯ g, denoted by ¯ gD, by setting ¯ gD = ¯ g on M and ¯ gD = ι∗ ¯g on −M .

Lemma A.3.3. Let (M, ¯g) be a compact oriented Riemannian manifold with boundary with ¯g = g + dt 2 near ∂M . If Σ ⊂ M be a properly embedded minimal 

118 hypersurface with free boundary, then double of Σ, given by ΣD = Σ ∪∂Σ ι(Σ) is a smooth minimal hypersurface of (MD, ¯gD). Moreover, if Σ is stable, then so is ΣD.Proof. First, we will show that Σ D is a smooth hypersurface. Clearly, Σ D is smooth away from the doubling locus ∂Σ ⊂ MD. Let x0 ∈ ∂Σ and let r > 0 be less than the injectivity radius of ¯ gD. Set φ = exp ¯gD 

> x0

and consider ˆΣ = φ−1(Σ ∩ Br(x0)) , ˆΣD = φ−1(Σ D ∩ Br(x0)) , ˆg = φ∗ ¯gD

and ν, the unit normal vector field to ˆΣ with respect to ˆ g. Evidently, ˆΣ is a minimal hypersurface in Tx0 MD with free boundary contained in Tx0 ∂M ⊂ Tx0 MD with respect to ˆ g. We choose an orthonormal basis for Tx0 MD so that, writing x ∈ Tx0 M as (x1, . . . , x n+1 ) in this basis, 1. Tx0 ∂ ˆΣ = {(x1, . . . , x n−1, 0, 0) };2. Tx0 ˆΣ = {(x1, . . . , x n, 0) };3. Tx0 ∂M = {(x1, . . . , x n−1, 0, x n+1 )}.This can be accomplished since Σ meets ∂M orthogonally. In these coordinates, the involution ι now takes the form ( x1, . . . , x n, x n+1 ) 7 → (x1, . . . , −xn, x n+1 ). Notice that, because the second fundamental form of ∂M vanishes, φ−1(∂M ∩ Br(x0)) is contained in the hyperplane {(x1, . . . , x n+1 ) : xn = 0 }.For a radius r′ < r , we consider the n-dimensional ball 

Bnr′ (0) = {x ∈ Tx0 M : xn+1 = 0 , || x|| < r ′},

119 the n-dimensional half-ball Bnr′,+(0) = {x ∈ Bnr′ (0) : xn ≥ 0}, and the cylinder 

Cr′ (0) = {x ∈ Tx0 M : ( x1, . . . , x n, 0) ∈ Bnr′ (0) }.

For small enough r′, we may write ˆΣ ∩ Cr′ (0) as the graph of a function 

u : Bnr′,+(0) → R, graph( u) = ˆΣ ∩ Cr′ (0) where graph( u) = {(x1, . . . , x n, u (x1, . . . , x n)) : ( x1, . . . , x n, 0) ∈ Bnr′ (0) }. Now we may form the doubling of u to a function uD : Bnr′ (0) → R, setting 

uD(x1, . . . , x n) = 



u(x1, . . . , x n) if xn ≥ 0

u(x1, . . . , x n−1, −xn) if xn < 0.

To show Σ D is smooth at x0, it suffices to show that uD is smooth along {x ∈

Bnr′ (0) : xn = 0 }.From the free boundary condition, we have ∂u ∂x n ≡ 0 on {xn = 0 } and so uD has a continuous derivative on all of Bnr′ (0). Since ˆΣ is smooth and minimal, uD is smooth and solves the minimal graph equation (A.4) with respect to the metric ˆ gD in the strong sense on {x ∈ Bnr′ (0) : xn 6 = 0 }. Moreover, it follows from ∂u ∂x n ≡ 0 on {xn = 0 }

and the ι-invariance of ¯ gD that uD solves the minimal graph equation weakly on the entire ball Bnr′ (0). From this point, the smoothness of uD is a standard application of tools from nonlinear elliptic PDE theory, so we will be brief (see [30, Lemma 7.2]). Standard estimates for minimizers implies uD ∈ H2(Bnr′ (0)) (see [32, Section 8.3.1]). Writing 120 the equation (A.4) in divergence form, we have 

∂∂x i

(

aij ∂u D

∂x j + biuD

)

= 0 (A.7) where the coefficients aij and bi depend on uD and are only differentiable. Since uD

weakly solves equation (A.7), 

∫ 

> Bnr′(0)

(

aij ∂u D

∂x j + biuD

) ∂ψ ∂x i dx = 0 ,

for any test function ψ ∈ C∞ 

> 0

(Bnr′ (0)) Taking ψ to be of the form − ∂w ∂x k for some function w and integrating by parts, one finds ∂u D 

> ∂x k

is a weak solution of a uniformly elliptic linear equation with L∞ coefficients for each k = 1 , . . . , n .Now we may apply the DeGiorgi-Nash theorem (see [29, Theorem 8.24]) to conclude that, for each r′′ < r ′ there is an α ∈ (0 , 1) such that ∂u D 

> ∂x k

∈ C0,α (Bnr′′ (0)) for each k = 1, . . . , n . Now uD ∈ C1,α (Bnr′′ (0)) and the functions ∂u D 

> ∂x k

solve a uniformly elliptic linear equation with H¨ older coefficients. The Schauder estimates from Theorem A.1.2 allow us to conclude that ∂u D 

> ∂x k

∈ C2,α (Br′ (0)). This argument may be iterated, see [29, Section 8], to conclude uD ∈ Ck,α (Bnr′′ (0)) for any k. This finishes the proof that uD is a smooth solution to the mean curvature equation across the doubling locus {xn = 0 } and hence Σ D is a smooth minimal hypersurface. The last step is to show that Σ D is stable. Let φ ∈ C∞(Σ D) define a normal variation and write φ = φ0 + φ1 where φ0 is invariant under the involution and φ1 is anti-invariant under the involution. Now we will consider the second variation of the 121 volume of Σ D with respect to φ.

δ2

> φ

(Σ D) = 

∫

> ΣD

|∇ φ|2 − φ2(Ric( ν, ν ) + |A|2)dμ 

=

∫

> ΣD

|∇ φ0|2 + 2 g(∇φ0, ∇φ1) + |∇ φ1|2 − (φ20 + 2 φ0φ1 + φ21)(Ric( ν, ν ) + |A|2)dμ 

= δ2 

> φ0

(Σ D) + δ2 

> φ1

(Σ D) + 

∫

> ΣD

2g(∇φ0, ∇φ1) − 2φ0φ1(Ric( ν, ν ) + |A|2)dμ 

= 2 δ2 

> φ0|Σ

(Σ) + 2 δ2 

> φ1|Σ

(Σ) ≥ 0where the last equality follows from the fact that g(∇φ0, ∇φ1) and φ0φ1 are anti-invariant under the involution. This completes the proof of Lemma A.3.3. 

A.32. Second fundamental form bounds 

In this section, we will prove Step 2 in Section 3.25. Let ( Mi, ¯gi) and Wi be as in Main Lemma. The uniform second fundamental form bounds for the stable minimal hypersurfaces Wi ⊂ Mi can be reduced to a classical estimate due to Schoen-Simon [25] for stable minimal hypersurfaces in Riemannian manifolds. In the following, ( M, ¯g) is a complete ( n + 1)-dimensional Riemannian manifold, x0 ∈ M ,

ρ0 ∈ (0 , inj ¯g(x0)), and μ1 is a constant satisfying sup Bρ(0) 

∣∣∣∂¯gij 

> ∂x k

∣∣∣ ≤ μ1, sup Bρ(0) 

∣∣∣ ∂2 ¯gij  

> ∂x k∂x l

∣∣∣ ≤ μ21, (A.8) on the metric ball Bρ0 (x0) in geodesic normal coordinates ( x1, . . . , x n+1 ) centered at 

x0.

Theorem A.3.4 (Corollary 1 [25]) . Suppose Σ is an oriented embedded C2-hypersurface in an (n + 1) -dimensional Riemannian manifold (M, ¯g) with x0 ∈ Σ,

μ1 satisfies (A.8) , and μ satisfies the bound ρ−n 

> 0

Hn(Σ ∩ Bρ0 (x0)) ≤ μ. Assume that 

122 Hn(Σ ∩ Bρ0 (x0)) < ∞ and Hn−2(sing(Σ) ∩ Bρ0 (x0)) = 0 . If n ≤ 6 and Σ is stable in 

Bρ0 (x0), then 

sup  

> Bρ0(x0)

|AΣ| ≤ Cρ0

,

where C depends only on n, μ, and μ1ρ0.Proof of Step 2. By Lemma A.3.3, the doubling ( Wi)D is a smooth stable minimal hypersurface of ( Mi)D. In particular, the singular set of ( Wi)D is empty. Moreover, the manifolds ( Mi)D have uniformly bounded geometry so that the injectivity radius is uniformly bounded from below by some ρ0 > 0, and there is a constant μ1 so that the bounds (A.8) hold in normal coordinates about any x ∈ (Mi)D, any ρ ∈ (0 , ρ 0), and all i = 1 , 2. . . . . According to Step 1, there is a constant μ such that 

ρ−n 

> 0

Vol( Wi ∩ Bρ(x)) ≤ μ

for all i = 1 , 2, . . . . Hence, we may uniformly apply Theorem A.3.4 on any ball 

Bρ0 (x0) ⊂ (Mi)D intersecting Wi to obtain the bound in Step 2. 

A.33. Generic regularity in dimension 8 

It is well known that codimension one volume minimizing currents, in general, have singularities if the ambient space is of dimension 8 or larger. However, in [27] N. Smale developed a method for removing these singularities in 8-dimensional Riemannian manifolds by making arbitrarily small conformal changes. In this section, we will describe the modifications necessary to adapt his method to the case of Theorem 1.5.6 with n = 7. First, we will describe the perturbation result we will use. Let M be a compact (n + 1)-dimensional manifold. For k = 3 , 4, . . . , let Mk 

> 0

denote the class of Ck metrics 123 on M which split isometrically as a product on some neighborhood of ∂M . Fix a relative homology class α ∈ Hn(M, ∂M ; Z). We will show the following. 

Theorem A.3.5. Let g0 ∈ M k 

> 0

and n = 7 . For ε > 0, there exists a metric g ∈ M k

> 0

and a g0-volume minimizing current T representing α such that || g − g0|| Ck < ε and 

spt( T ) is smooth. 

The proof of Theorem A.3.5 follows by showing the constructions in [27] can be performed on the doubled manifold MD (see Appendix A.31) in an involution-invariant manner. We proceed in two lemmas. The first lemma holds in any dimension. 

Lemma A.3.6. Let g0 ∈ M k 

> 0

and suppose T is a homologicly g0-volume minimizing current representing α. For ε > 0, there is a metric g ∈ M k 

> 0

such that || g − g0|| Ck < ε 

and T is the only g-volume minimizing current representative of α.Proof. Let A, dμ = θd Hn, and ξ be the underlying rectifiable set, measure, and choice of orientation for the approximate tangent space of A associated to the current 

T (see Section A.3). We may write A = ∪Nj=1 Aj where each Aj are connected. Choose 

pj ∈ reg( Aj ) \ ∂M and ρ > 0 so that (Bρ(pj ) ∩ Aj ) ⊂ (reg( A) \ ∂M ) , j = 1 , . . . , N. 

Perhaps restricting to smaller ρ, let x = ( x1, . . . , x n) be geodesic normal coordinates for Bρ(pj ) ∩ Aj and let t be the signed distance on Bρ(pj ) from Aj determined by ξ.This gives Fermi coordinates ( t, x ) on Bρ(pj ). Now fix a bump function η : A → [0 , 1] satisfying 

η(x) = 



1 for x ∈ Bρ/ 2(pj ) ∩ Aj

0 for x ∈ Bρ(pj ) \ B3ρ/ 4(pj )124 for each j = 1 , . . . N . Also fix a smooth function φ : R → R with spt( φ) ⊂ [−3/4, 3/4], 

φ(t) ≥ 0 on [ −1, 1] , φ (0) = 1 , and φ(r) < 1 if r 6 = 0 .

Consider the function φ¯ε : M → R given by 

φ¯ε(y) = 



1 − ¯εk+1 φ(t/ ¯ε)η(x) if y = ( x, t ) ∈ Bρ(pj ) for some j

1 otherwise for ¯ ε > 0 satisfying spt( φ¯ε) ⊂ ∪ Nj=1 B3ρ/ 4(pj ). We have the perturbed metrics g¯ε =

φ 2 

> n
> ε

g0 ∈ M k 

> 0

. It is straight-forward to show that there exists ε1 ∈ (0 , ε ) such that, for any ¯ ε ∈ (0 , ε 1], T is the only g¯ε-volume minimizing representative of α (see [27]). Perhaps restricting to smaller values of ¯ ε, we may also arrange for || g − g¯ε|| Ck < ε .This completes the proof of Lemma A.3.6. 

Lemma A.3.7. Let n = 7 , k ≥ 3, g0 ∈ M k, and ε > 0. Suppose T is the only g0-volume minimizing representative of α, then there exists g ∈ M k such that 

|| g − g0|| Ck < ε and α may be represented (up to multiplicity) by a smooth g-volume minimizing hypersurface. Proof. Following [27], we construct a conformal factor which will slide the minimizing current off itself in one direction and appeal to a perturbation result for isolated singularities which allows us to conclude that this new current has no singularity. Write ( MD, g 0,D) for the doubling of ( M, g 0) (see Section A.31) with involution ι :

MD → MD. The current T may also be doubled to obtain an involution-invariant current TD on MD. Similarly to Section A.31, TD is locally g0,D-volume minimizing. Let A = ∪Nj=1 Aj , dμ = θd H7, and ξ be the underlying set, measure, and orientation associated to T , as in the proof of Lemma A.3.6. 125 Let ρ0 > 0 and fix a smooth function φ : R → R satisfying 1. φ(−t) = −φ(t),

2. φ(t) ≥ 0 for t ≥ 0,

3. φ(t) = t for t ∈ [0 , ρ0 

> 4

],

4. φ(t) = ρ0 

> 2

for t ∈ [ρ0 

> 2

, 3ρ0 

> 4

],

5. φ(t) = 0 for t ≥ ρ0.

Let {Bρ(pj )}Nj=1 be a collection of disjoint metric balls in ˚M centered at regular points pj ∈ Aj . Choose ρ0 > 0 small enough to ensure that, in Fermi coordinates (t, x ) for Aj with ξ pointing into the side corresponding to t > 0, the function ( t, x ) 7 →

φ(t)η(x) is supported in ∪Nj=1 Bρ(pj ). For a fixed s ∈ (0 , 1) and a parameter ¯ ε ∈ (0 , 1), consider the functions u¯ε : Σ → R given by 

u¯ε(y) = 



1 − ¯εsφ(t)η(x) if y = ( t, x ) ∈ ∪ Nj=1 Bρ(pj )1 otherwise. The conformal metrics g¯ε = u 2 

> n
> ¯ε

g0 will be used to find the desired smooth representative. Since g¯ε splits as a product near ∂M , we may consider the corresponding ι-invariant metric g¯ε, D on MD.For sake of contradiction, suppose that there is a sequence ¯εi → 0 and homologically g¯εi -volume minimizing currents Ti representing α with sing( Ti) 6 = ∅

for all i = 1 , 2, . . . . Since M(Ti) is uniformly bounded in i, Ti weakly converges to some homologically g0-volume minimizing current T∞ which also represents α. Since 

T is assumed to be the unique such current, we must have T∞ = T . Write Pi, dμ i,126 and ξi for the set, measure, and orientation corresponding to Ti for i = 1 , 2, . . . . Let 

Qi be a connected component of Pi with sing( Qi) 6 = ∅ for each i = 1 , 2, . . . . Now 

Qi converges in the Hausdorff sense to some sheet Q of T . By the Allard regularity theorem [33], this convergence is smooth away from sing( Q). Hence, after passing to a subsequence, yi converges to some y ∈ sing( Q). In terms of the doubled manifold, the ι-invariant currents Ti, D are homologically 

g¯εi,D-volume minimizing, Ti, D weakly converge to T0,D, and the doubled sets Qi, D

converge to QD smoothly away from sing( QD). Now let N ⊂ MD be a small distance neighborhood of QD so that N \ QD consists of two disjoint, open sets N− and N+ on which the signed distance to QD is negative and positive, respectively. In the doubled manifold, we may directly apply the following results from [27]. 

Lemma A.3.8. [27, Proposition 1.6] For large i, we have 1. Qi, D ∩ N − = ∅

2. Qi, D ∩ N + \ spt( φεi η)D 6 = ∅.

In light of Lemma A.3.8, the Simon maximum principle [34] shows (Qi, D \ spt( φiη)D) ⊂ (N+ \ spt( φiη)D)for each i = 1 , 2, . . . . Recalling that Qi, D converges to QD in the Hausdorff distance, we may apply the perturbation result [35, Theorem 5.6] to conclude that Qi, D is smooth for sufficiently large i. This contradiction finishes the proof of Lemma A.3.7. Theorem A.3.5 follows by first applying Lemma A.3.6 to approximate g0 with a metric g1 supporting a unique minimizing representative of α then applying 127 Lemma A.3.7 to approximate g1 with a metric g2 and obtain a g2-volume minimizing representative of α.

Proof of Theorem 1.5.6 for n = 7 . We will closely follow the argument presented in Section 3.3. Let ( Z, ¯g, ¯γ) : (Y0, g 0, γ 0) (Y1, g 1, γ 1) be a psc-bordism and let (Zi, ¯gi, ¯γi) be the corresponding i-collaring for i = 1 , 2, . . . . As usual, we denote by ¯ αi ∈ H7(Zi, ∂Z i; Z) the Poincar´ e dual to ¯ γi.For each i = 1 , 2, . . . , we apply Theorem A.3.5 to obtain a metric ˆ gi on Zi so that 

|| ˆgi − ¯gi|| Ci

> ¯gi

≤ 1

i

and ¯ αi can be represented by a smooth ˆ gi-volume minimizing hypersurface Wi. It follows from the proofs of Lemmas A.3.6 and A.3.7 that ˆ gi can and will be chosen so that {ˆgi 6 = ¯ gi} ⊂ M1 ⊂ Mi for i = 1 , 2, . . . . Indeed, the perturbations required to form ˆ gi are supported on balls centered about chosen regular points of ¯ gi-volume minimizing currents and one can always find regular points of minimizers of ¯ αi in 

M1 ⊂ Mi. Evidently, ˆ gi has positive scalar curvature for all sufficiently large i. Since ˆgi = ¯ gi on Y × [−i, 0] ⊂ Zi, the proof of the Main Lemma shows that there is a subconvergence (Zi, W i, ˆgi, Si) → (Y × (−∞ , 0] , X × (−∞ , 0] , g + dt 2, S)where Y, X, g, Si, and S∞ are defined as in Section 3.3. One can now directly apply the argument from 3.31 to finish the proof of Theorem 1.5.6 for n = 7. 128 REFERENCES CITED [1] J. Kazdan and F. W. Warner. Scalar curvature and conformal deformation of Riemannian structure. J. Differential Geometry , 10:113–134, 1975. [2] M. Gromov and H. B. Lawson, Jr. The classification of simply connected manifolds of positive scalar curvature. Ann. of Math. (2) , 111(3):423–434, 1980. [3] R. Schoen and S. T. Yau. On the structure of manifolds with positive scalar curvature. Manuscripta Math. , 28(1-3):159–183, 1979. [4] R. Schoen. Conformal deformation of a Riemannian metric to constant scalar curvature. J. Differential Geom. , 20(2):479–495, 1984. [5] H. Ara´ ujo. Critical points of the total scalar curvature plus total mean curvature functional. Indiana Univ. Math. J. , 52(1):85–107, 2003. [6] J. Escobar. Conformal deformation of a Riemannian metric to a scalar flat metric with constant mean curvature on the boundary. Ann. of Math. (2) , 136(1): 1–50, 1992. [7] J. Escobar. The Yamabe problem on manifolds with boundary. J. Differential Geom. , 35(1):21–84, 1992. [8] J. Escobar. Addendum: “Conformal deformation of a Riemannian metric to a scalar flat metric with constant mean curvature on the boundary” [Ann. of Math. (2) 136 (1992), no. 1, 1–50; MR1173925 (93e:53046)]. Ann. of Math. (2) , 139(3):749–750, 1994. [9] J. Escobar. Conformal deformation of a Riemannian metric to a constant scalar curvature metric with constant mean curvature on the boundary. Indiana Univ. Math. J. , 45(4):917–943, 1996. [10] L. Mazzieri. Generalized connected sum construction for nonzero constant scalar curvature metrics. Comm. Partial Differential Equations , 33(1-3):1–17, 2008. [11] D. Joyce. Constant scalar curvature metrics on connected sums. Int. J. Math. Math. Sci. , (7):405–450, 2003. [12] R. Mazzeo, D. Pollack, and K. Uhlenbeck. Connected sum constructions for constant scalar curvature metrics. Topol. Methods Nonlinear Anal. , 6(2): 207–233, 1995. [13] L. Mazzieri. Generalized connected sum construction for scalar flat metrics. 

Manuscripta Math. , 129(2):137–168, 2009. 129 [14] F. Morgan. Geometric measure theory . Elsevier/Academic Press, Amsterdam, fourth edition, 2009. A beginner’s guide. [15] H. Federer. Geometric measure theory . Die Grundlehren der mathematischen Wissenschaften, Band 153. Springer-Verlag New York Inc., New York, 1969. [16] T. Schick. A counterexample to the (unstable) Gromov-Lawson-Rosenberg conjecture. Topology , 37(6):1165–1168, 1998. [17] M. Gr¨ uter. Optimal regularity for codimension one minimal surfaces with a free boundary. Manuscripta Math. , 58(3):295–343, 1987. [18] G. Lieberman. Mixed boundary value problems for elliptic and parabolic differential equations of second order. J. Math. Anal. Appl. , 113(2):422–440, 1986. [19] T. Aubin. Some nonlinear problems in Riemannian geometry . Springer Monographs in Mathematics. Springer-Verlag, Berlin, 1998. [20] K. Wehrheim. Uhlenbeck compactness . EMS Series of Lectures in Mathematics. European Mathematical Society (EMS), Z¨ urich, 2004. [21] M. Anderson. On boundary value problems for Einstein metrics. Geom. Topol. ,12(4):2009–2045, 2008. [22] A. Fraser and M. M. Li. Compactness of the space of embedded minimal surfaces with free boundary in three-manifolds with nonnegative Ricci curvature and convex boundary. J. Differential Geom. , 96(2):183–200, 2014. [23] S. Krantz and H. Parks. Geometric integration theory . Cornerstones. Birkh¨ auser Boston, Inc., Boston, MA, 2008. [24] H. I. Choi and R. Schoen. The space of minimal embeddings of a surface into a three-dimensional manifold of positive Ricci curvature. Invent. Math. , 81(3): 387–394, 1985. [25] R. Schoen and L. Simon. Regularity of stable minimal hypersurfaces. Comm. Pure Appl. Math. , 34(6):741–797, 1981. [26] K. Akutagawa and B. Botvinnik. Manifolds of positive scalar curvature and conformal cobordism theory. Math. Ann. , 324(4):817–840, 2002. [27] N. Smale. Generic regularity of homologically area minimizing hypersurfaces in eight-dimensional manifolds. Comm. Anal. Geom. , 1(2):217–228, 1993. [28] B. Botvinnik and O. M¨ uller. Cheeger-gromov convergence in a conformal setting. Preprint 2015. arXiv:1512.07651. 130 [29] D. Gilbarg and N. Trudinger. Elliptic partial differential equations of second order . Classics in Mathematics. Springer-Verlag, Berlin, 2001. [30] T. Colding and W. Minicozzi. A course in minimal surfaces , volume 121 of 

Graduate Studies in Mathematics . American Mathematical Society, Providence, RI, 2011. [31] R. Schoen, L. Simon, and S. T. Yau. Curvature estimates for minimal hypersurfaces. Acta Math. , 134(3-4):275–288, 1975. [32] L. Evans. Partial differential equations , volume 19 of Graduate Studies in Mathematics . American Mathematical Society, Providence, RI, second edition, 2010. [33] W. Allard. On the first variation of a varifold. Ann. of Math. (2) , 95:417–491, 1972. [34] L. Simon. A strict maximum principle for area minimizing hypersurfaces. J. Differential Geom. , 26(2):327–335, 1987. [35] R. Hardt and L. Simon. Area minimizing hypersurfaces with isolated singularities. J. Reine Angew. Math. , 362:102–129, 1985. 131
