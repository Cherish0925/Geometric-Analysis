---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: UC Berkeley]

− Lω)ϕ = −∂ϕ · ∂S (ω) − ∂S (ω) · ∂ϕ − 12ϕ∆ωS(ω). (4.1.1) In particular, L∗ 

> ω

and Lω only differ by first order terms in ϕ. Note that the highest order terms in Lω and L∗ 

> ω

are the bilaplacian associated to ω. Not only that, but on Mp in the normal coordinate z these terms approximate the usual Euclidean bilaplacian near p, and since η is aymptotically Euclidean and scalar flat, Lη = L∗ 

> η

approximates the Euclidean bilaplacian near infinity. In general we know little about the kernel of L∗ 

> ω

when ω is not cscK. However, fix an 

L2-orthonormal basis f1, ..., f d for the kernel of Lω.

Lemma 4.1.2. There exists points q1, ..., q d ∈ Mp such that the operator 

˜L∗ 

> ω

: C4,α (M ) → C0,α (M )˜L∗

> ω

ϕ := L∗

> ω

ϕ −

> d

X

> i=1

ϕ(qi)fi

is an isomorphism. Proof. First, regardless of the choice of q1, ..., q d, if we have ˜L∗

> ω

ϕ = 0, then we must have that L∗

> ω

ϕ = 0 since the fi are each orthogonal to the image of L∗

> ω

.We claim that we can find q1, ..., q d ∈ Mp, and a basis ϕ1, ..., ϕ d for ker( L∗

> ω

) such that for 1 ≤ i ≤ d the vectors 

vi := ( ϕi(q1), ..., ϕ i(qd)) are linearly independent. If this were true, then suppose there was some nonzero ϕ in the kernel of ˜L∗

> ω

. Then ϕ is also in the kernel of L∗ 

> ω

so ϕ = Pdj=1 cj ϕj , and we would have 0 = 

> d

X

> j=1

cj ϕj (qi)for each i. This means there is a nonzero vector orthogonal to each vTi , which contradicts the linear independence of the vi, so ˜L∗ 

> ω

is injective. For surjectivity, ˜L∗ 

> ω

differs from the index zero operator L∗ 

> ω

by an operator of finite rank, and so is also index zero. Then injectivity implies surjectivity. Now we prove our claim. We do so inductively; first, if ϕ1 ∈ ker( L∗

> ω

) is nonzero then of course we can find a point q1 ∈ Mp such that ϕ1(q1)̸ = 0. Now, suppose we have found CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 30 points q1, ..., q d−1 and linear independent functions ϕ1, ..., ϕ d−1 in the kernel of L∗ 

> ω

such that for 1 ≤ i ≤ d − 1 the vectors 

v′ 

> i

:= ( ϕi(q1), ..., ϕ i(qd−1)) are linearly independent. Let ϕd ∈ ker( L∗

> ω

) linearly independent of ϕ1, ..., ϕ d−1. Suppose there is qd ∈ Mp such that ϕd(qd)̸ = 0 and vd is linearly dependent of v1, ..., v d−1 defined in the same way as above (they themselves are linearly independent due to the linear independence of the v′

> i

). Then we have that there exists constant a1, ..., a d−1 such that 

> d−1

X

> j=1

aj ϕj (qi) − ϕd(qi) = 0 for 1 ≤ i ≤ d, 

> d−1

X

> j=1

aj ϕj − ϕd̸ ≡ 0.

Then replacing ϕd with Pd−1 

> j=1

aj ϕj − ϕd and replacing qd with a point where this function is nonzero yields the claim, since in that case vd would be equal to zero in its first d − 1components. If we could not find such a qd, then ϕd(qd)̸ = 0 implies that v1, ..., v d are linearly indepen-dent as desired. From now on we fix q1, ..., q d ∈ Mp to be a set of points for which the conclusion of the above lemma holds. When we blow up, we are pushed onto studying the operator ˜L∗ 

> ωϵ

: C4,α δ (Bl pM ) → C0,α δ (Bl pM )˜L∗ 

> ωϵ

ϕ := L∗ 

> ωϵ

ϕ −

> d

X

> i=1

ϕ(qi)fi. (4.1.3) Due to the geometry of ωϵ, on Mp this operator behaves like ˜L∗ 

> ω

restricted to Mp so we need: 

Proposition 4.1.4. Consider for now ˜L∗ 

> ω

as an operator ˜L∗ 

> ω

: C4,α δ (Mp) → C0,α δ−4(Mp).

• If δ > 4 − 2n, then ˜L∗ 

> ω

has trivial kernel. 

• If n = 2 , fix δ ∈ (−1, 0) . Then if ϕ ∈ C4,α δ (Mp) is in the kernel of ˜L∗

> ω

, in B1 we have 

ϕ = a log |z| + b + θ

for some a, b ∈ R and θ ∈ C4,α δ+2 (Mp).Proof. The proof of the first claim is exactly the same as what appears in [3], or [31]. For the second claim, first note that since near p we can use holomorphic normal coordinates 

ωjk = δjk + O(|z|2), if f ∈ Ck,α δ (Mp) we have ˜L∗

> ω

(f ) + 14∆2

> euc

(f ) ∈ Ck−4,α δ−2 (Mp) (4.1.5) CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 31 as long as δ < 2 (otherwise we have to account for the zeroth order terms in ˜L∗

> ω

). We would usually only expect Ck−4,α δ−4 (Mp) since these are fourth order operators. Now consider ϕ ∈ C4,α δ (Mp) such that ˜L∗

> ω

ϕ = 0. If we let χ be a cutoff supported in B1

that is equal to 1 in B1/2, then from 4.1.5 ∆2

> euc

(χϕ ) ∈ C0,α δ−2(C2 \ { 0}).

From Proposition 3.3.2 there is θ ∈ C4,α δ+2 (C2 \ { 0}) such that θ − χϕ is biharmonic and in 

C4,α δ (C2 \ { 0}). The only biharmonic functions with δ ∈ (−1, 0) are multiples of log |z| and constants, and thus there are constants a, b ∈ R such that 

χϕ = a log |z| + b + θ. 

Near the exceptional divisor L∗ 

> ωϵ

= L∗ 

> ϵ2η

= Lϵ2η = 1 

> ϵ4

Lη, where the last two equalities are due to the fact that η is cscK and the ( −2) −homogeneity of the scalar curvature, respectively. There, we are able to use the injectivity of Lη when viewed as an operator on the weighted spaces on Bl 0Cn when δ < 0. Finally, to prove the desired estimates on ˜L∗ 

> ωϵ

we need Schauder estimates which are independent of ϵ.

Lemma 4.1.6. Fix δ < 0. There exists a positive constant C independent of all ϵ > 0 small such that for all ϕ ∈ C4,α δ (Bl pM )

|| ϕ|| C4,α δ (Bl pM ) ≤ C(|| ϕ|| C0   

> δ(Bl pM)

+ || ˜L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM )).

Proof. First, we define a function ρ : Bl pM → R which describes the weights in the norms on Bl pM ,

ρ(z) = 



1 |z| ≥ 1

|z| ϵ ≤ | z| ≤ 1

ϵ |z| ≤ ϵ.

Now, η is asymptotically Euclidean, M is compact, and the sectional curvatures of ωϵ satisfy a uniform bound in the Ck,α  

> −2

(Bl pM ) norm 3.3.7, and thus we have that there exists some 

r > 0 independent of ϵ such that the injectivity radius of ωϵ is bounded below by rρ (z). This implies that for any κ > 0 one can find fix an r small enough independent of ϵ such that at each point x ∈ Bl pM , in the normal coordinates of radius rρ (x) with respect to ωϵ centered at x we have 11 + κ|| · || Ck,α 

> (rρ (x)) −2ωϵ

≤ || · || Ck,α ≤ (1 + κ)|| · || Ck,α 

> (rρ (x)) −2ωϵ

, (4.1.7) where the middle norm is measured with respect to the Euclidean metric in the normal coordinates. Since L∗ 

> ωeuc

= −14 ∆2

> euc

, after possibly taking r even smaller we further have for any ϕ

11 + κ|| L∗ 

> (rρ (x)) −2ωϵ

ϕ|| Ck−4,α ≤ || 14∆2

> euc

ϕ|| Ck−4,α ≤ (1 + κ)|| L∗ 

> (rρ (x)) −2ωϵ

ϕ|| Ck−4,α ,CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 32 again in the normal coordinate ball, and these norms are measured in the Euclidean norm with respect to the normal coordinates. Now, applying the usual Schauder estimates for the Euclidean bilaplacian, there is a constant D > 0 such that in any of these normal coordinate balls 

|| ϕ|| Ck,α ≤ D(|| ϕ|| C0 + || 14∆2

> euc

ϕ|| Ck−4,α ).

Due to the comparisons of the Euclidean H¨ older norms with the H¨ older norms for ωϵ 4.1.7 we then have 

|| ϕ|| Ck,α 

> (rρ (x)) −2ωϵ

≤ D(1 + κ)2(|| ϕ|| C0 + || L∗ 

> (rρ (x)) −2ωϵ

ϕ|| Ck−4,α ).D(1 + κ)2 has no dependence on ϵ. Noting that L∗ 

> (rρ (x)) −2ωϵ

= ( rρ (x)) 4L∗ 

> ωϵ

and applying this estimate to ρ(x)−δϕ over all of these normal coordinate balls we have a C > 0 independent of ϵ such that 

|| ϕ|| C4,α δ (Bl pM ) ≤ C(|| ϕ|| C0   

> δ(Bl pM)

+ || L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM )).

Now to get the estimate for ˜L∗ 

> ωϵ

, note that there is c > 0 independent of ϵ such that 

|| ˜L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM ) − || L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM ) ≤ c|| ϕ|| C0   

> δ(Bl pM)

max  

> i

|| fi|| C0,α δ−4(Bl pM ).

The result then follows from the fact that the norms || fi|| C0,α δ−4(Bl pM ) are uniformly bounded from above in ϵ when δ < 0. We are now ready to prove the main estimate. 

Proposition 4.1.8. Fix δ ∈ (−1, 0) sufficiently small. Consider the operator 

˜L∗ 

> ωϵ

: C4,α δ (Bl pM ) → C0,α δ−4(Bl pM ).

• Suppose n > 2. For ϵ > 0 small there exists a constant K > 0 independent of ϵ such that for all ϕ ∈ C4,α δ (Bl pM ),

|| ϕ|| C4,α δ (Bl pM ) ≤ K|| ˜L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM ).

• Suppose n = 2 . For ϵ > 0 small there exists a constant K > 0 independent of ϵ such that for all ϕ ∈ C4,α δ (Bl pM ),

|| ϕ|| C4,α δ (Bl pM ) ≤ Kϵ δ|| ˜L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM ).

Proof. We will prove both cases simultaneously and comment where the differences occur. We argue by contradiction: suppose there exists a sequence of functions ϕi such that 

|| ϕi|| C4,α δ (Bl pM ) = 1 , || ˜L∗ 

> ωϵi

ϕi|| C0,α δ−4(Bl pM ) ≤ 1

i , (4.1.9) CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 33 in the n > 2 case, and in the n = 2 case we assume furthermore there is ϵi → 0 such that 

|| ϕi|| C4,α δ (Bl pM ) = 1 , || ˜L∗ 

> ωϵi

ϕi|| C0,α δ−4(Bl pM ) ≤ ϵ−δi

i . (4.1.10) From the uniform Schauder estimates Lemma 4.1.6, we have up to choosing a subsequence 

ϕi → ϕ∞ locally in C4,α on Mp with ϕ∞ ∈ C4,α δ (Mp), where we may have had to replace α

which a slightly smaller constant. Step 1: We show ϕ∞ ≡ 0 on Mp. When n > 2 this immediately follows from the fact that ˜L∗

> ω

ϕ∞ = 0 on Mp and our choice of δ due to Proposition 4.1.4. When n = 2, our slightly stronger assumption 4.1.10 gives for each 1 ≤ j ≤ d

Z

> Bl pM

fj ˜L∗ 

> ωϵi

(ϕi)ω2

> ϵi

2 =

Z

> Bl pM

fj L∗ 

> ωϵi

(ϕi)ω2

> ϵi

2 −

> d

X

> k=1

ϕi(qk)

Z

> Bl pM

fj fk

ω2

> ϵi

2 < Ci , (4.1.11) where C is a constant independent of ϵ. First note that since f1, ..., f d were assumed to be 

L2-orthonormal that lim 

> i→∞

Z

> Bl pM

fj fk

ω2

> ϵi

2 = δjk ,

and on the other hand we have 

Z

> Bl pM

fj L∗ 

> ωϵi

(ϕi)ω2

> ϵi

2 =

Z

> Bl pM

Lωϵi (fj )ϕi

ω2

> ϵi

2 .

Now we need to analyze this term as i → ∞ . We break up our manifold into M \ B2rϵi ,

B2rϵi \ Brϵi , and Brϵi , recalling that rϵ = ϵβ as defined in section 2. For M \ B2rϵi , in this region ωϵi = ω so we have 

Z 

> M\B2rϵ i

Lωϵi (fj )ϕi

ω2

> ϵi

2 =

Z 

> M\B2rϵ i

Lω(fj )ϕi

ω2

2 = 0 .

Next, in Brϵi after the coordinate change z = ϵiw we have ωϵi = ϵ2 

> i

η. Note that Lϵ2η = 1 

> ϵ4

Lη,so from the equation for the linearization of scalar curvature we have 

Z

> Brϵ i

Lωϵi (fj )ϕi

ω2

> ϵi

2 =

Z

> ˜Brϵ i ϵ−1
> i

−

14∆2

> η

(fj (ϵiw)) + 12Ric η · ∇ 2

> η

(fj (ϵiw)) 



ϕi(ϵiw)η2

2=

Z

> ˜Brϵ i ϵ−1
> i

−[ηkℓ ∂k∂ℓ(ηab ∂a∂b(fj (ϵiw))) + Ric kℓ η ∂k∂ℓ(fj (ϵiw))] ϕi(ϵiw)η2

2 .

We also have that from the asymptotics of the Burns-Simanca metric, ηkℓ = δkℓ + O(|w|−2), Ric kℓ η = O(|w|−4), |∇ k(fj (ϵw )) | ≤ Cϵ k, and |ϕi(ϵw )| = |ϕi(z)| ≤ Cϵ δ, where C represents possibly different constants but nevertheless is independent of ϵ. Thus, 

Z

> Brϵ i

Lωϵi (fj )ϕi

ω2

> ϵi

2 ≤ C  ϵ4 

> i

+ ϵ2

> i

 ϵδVol η( ˜Brϵi ϵ−1 

> i

) ≤ Cϵ 2 

> i

ϵδi r4 

> ϵi

ϵ−4 

> i

= Cϵ 4β−2+ δi ,CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 34 so this goes to zero as i → ∞ as long as β > 1/2 and δ is taken small enough. Lastly, we look at the integral over B2rϵi \ Brϵi . Here we have 

Z 

> B2rϵ i\Brϵ i

Lωϵi (fj )ϕi

ω2

> ϵi

2 =

Z 

> B2rϵ i\Brϵ i

−

14∆2 

> ωϵi

fj + 12Ric ωϵi · ∇ 2 

> ωϵi

fj



ϕi

ω2

> ϵi

2 .

From the explicit formula for ωϵi 3.2.2, in the region rϵi ≤ | z| ≤ 2rϵi we have 

ωkℓ ϵi = δkℓ + O

 ϵ2

> i

r2

> ϵi

log |ϵi|



, Ric kℓ ωϵi = O

 ϵ2

> i

r4

> ϵi

log |ϵi|



,

and thus 

Z 

> B2rϵ i\Brϵ i

Lωϵi (fj )ϕi

ω2

> ϵi

2 ≤ C



1 + ϵ2

> i

r4

> ϵi

log |ϵi|



ϵδVol ωϵi (B2rϵi \ Brϵi )

≤ Cϵ 2 

> i

r−4 

> ϵi

log |ϵi|ϵδi r4 

> ϵi

= Cϵ 2+ δi log |ϵi|.

This goes to zero as i → ∞ for δ small. The upshot is that from 4.1.11 we then get lim 

> i→∞

Z

> Bl pM

fj ˜L∗ 

> ωϵi

(ϕi)ω2

> ϵi

2 = |ϕ∞(qj )| = 0 ,

and thus on Mp, we not only have ˜L∗

> ω

ϕ∞ = 0 but 

L∗

> ω

ϕ∞ = 0 .

We then have that in B1 there is a, b ∈ R and θ ∈ C4,α δ+2 (Mp) such that ϕ∞ = a log |z| + b + θ

from Proposition 4.1.4. Step 1.5: Continuing our focus on the n = 2 case, we now show that there is a constant 

κ̸ = 0 such that for any ξ ∈ C∞(M ), 

Z

> M

Lω(ξ)ϕ∞

ω2

2 = −aκξ (p).

Thus, testing this equation with ξ ≡ 1, we must have that a = 0. Therefore ϕ∞ extends smoothly to all of M , being a bounded weak solution to an elliptic equation on M . Then 

ϕ∞ ≡ 0 by the invertibility of ˜L∗ 

> ω

on M (Lemma 4.1.2), as desired. This is the key step that necessitates us proving estimates on L∗ 

> ωϵ

instead of Lωϵ . Anyway, we write 

Z

> M

Lω(ξ)ϕ∞

ω2

2 = lim 

> r→0

Z 

> M\Br

−

14∆2

> ω

ξ + 12Ric ω · ∇ 2

> ω

ξ



ϕ∞

ω2

2 .CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 35 Now we apply integration by parts to each term in the integrand. Denoting by N the unit normal to the boundary sphere ∂B r, we first look at 

Z 

> M\Br

∆2

> ω

(ξ)ϕ∞

ω2

2 =

Z 

> M\Br

ξ∆2

> ω

(ϕ∞)ω2

2 −

Z

> ∂B r

ξ∇N (∆ ωϕ∞)Vol ∂B r +

Z

> ∂B r

∆ω(ϕ∞)∇N (ξ)Vol ∂B r

−

Z

> ∂B r

∆ω(ξ)∇N (ϕ∞)Vol ∂B r +

Z

> ∂B r

ϕ∞∇N (∆ ωξ)Vol ∂B r .

We investigate the boundary terms as r → 0. Since ϕ∞ behaves like a log |z| near zero, we have that the last three terms all go to zero in r since the terms involving the derivatives of ϕ∞ blow up at most like O(r−2), whereas the volume of ∂B r decays like O(r3). The only issue is the first boundary term. When r is small we have 

ξ∇N (∆ ωϕ∞) = aξ ∇N [( δkℓ + O(r2)) ∂k∂ℓ log |z|] + ξ∇N (∆ ωθ).

Due to the estimate on θ, the last term decays at worst like O(rδ−1), and so integrating and taking the limit we have lim 

> r→0

Z 

> M\Br

−14∆2

> ω

(ξ)ϕ∞

ω2

2 =

Z

> M

−14∆2

> ω

(ϕ∞)ξ ω2

2 + lim 

> r→0

a

4

Z

> ∂B r

ξ∇N (∆ euc log |z|)Vol ∂B r

=

Z

> M

−14∆2

> ω

(ϕ∞)ξ ω2

2 + aκξ (p).

For the other integration by parts, we have 

Z 

> M\Br

(Ric ω · ∇ 2

> ω

ξ)ϕ∞

ω2

2=

Z 

> M\Br

ξtr ω∇ω(tr ω∇ω(ϕ∞Ric ω)) ω2

2 +

Z

> ∂B r

⟨∇ ξ ⊗ N b, ϕ ∞Ric ω⟩Vol ∂B r

−

Z

> ∂B r

ξ(tr ω∇(ϕ∞Ric ω))( N )Vol ∂B r .

Both of the boundary terms have integrands which blow up no worse than O(r−1), so both boundary terms go to zero as r → 0. Thus, we finally have that 

Z

> M

Lω(ξ)ϕ∞

ω2

2 =

Z

> M

ξL ∗

> ω

(ϕ∞)ω2

2 − aκξ (p) = −aκξ (p),

since ϕ∞ is in the kernel of L∗ 

> ω

on Mp.Step 2: The rest of the proof is now the same in any dimension and proceeds as in [31]. To recount, we have as in 4.1.9 ϕi such that 

|| ϕi|| C4,α δ (Bl pM ) = 1 , || ˜L∗ 

> ωϵi

(ϕi)|| C0,α δ−4(Bl pM ) < 1

i ,CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 36 (the second bound is actually slightly stronger in n = 2) and ϕi → 0 locally in C4,α , where again we may have to replace α with a slightly smaller constant. We then have the uniform Schauder estimate of Lemma 4.1.6 

|| ϕi|| C4,α δ (Bl pM ) ≤ C(|| ϕi|| C0   

> δ(Bl pM)

+ || ˜L∗ 

> ωϵi

(ϕi)|| C0,α δ−4(Bl pM )),

so then we have 1 ≤ C|| ϕi|| C0   

> δ(Bl pM)

+ Ci ⇐⇒ 1

C − 1

i ≤ || ϕi|| C0   

> δ(Bl pM)

≤ 1,

and so || ϕi|| C0   

> δ(Bl pM)

is uniformly bounded below by a positive constant, say C′. Applying the uniform Schauder estimates to ψi := ϕi  

> || ϕi|| C0
> δ(BlpM )

we get 

|| ψi|| C4,α δ (Bl pM ) ≤ C + Ci|| ϕi|| C0  

> δ(Bl pM)

≤ C + CiC ′ .

Since the last term goes to zero we have a family of functions such that 

|| ψi|| C0   

> δ(Bl pM)

= 1 , || ψi|| C4,α δ (Bl pM ) ≤ C, (4.1.12) 

|| L∗ 

> ωϵi

(ψi)|| C0,α δ−4(Bl pM ) → 0, ψ i → 0 locally in C4,α on Mp. (4.1.13) Now, we want to look at the point xi ∈ Bl pM where ρ−δi ψi achieves its maximum, where 

ρi is as defined in the proof of Lemma 4.1.6 but with respect to ϵi, which due to the above assumptions is when 

ρ−δi (xi)ψi(xi) = 1 .

Since ψi → 0 locally on Mp, ρi(xi) → 0. Then ϵ−1 

> i

ρi(xi) is either bounded or unbounded; one can think of the former case as the ψi concentrating close to the exceptional divisor as 

i → ∞ , the latter case is when ψi concentrates in the Euclidean neck region. Step 3: We first suppose the former. In this case we have that ϵ−1 

> i

ρi(xi) < R for some R

and for all i. Then under the identification of B1 ⊂ Bl pM with the ball ˜Bϵ−1 ⊂ Bl 0Cn, we have that all the xi are inside ˜BR. Thus, up to taking a subsequence we have xi → x∞ ∈ ˜BR.Rescaling by ϵi, ϵ−δi ψi can be viewed as functions on larger subsets of Bl 0Cn still with a uniform C4,α δ (Bl 0Cn) bound from 4.1.12. Thus we have that up to a subsequence and replacing α, ϵ−δi ψi → ψ∞ locally in C4,α on Bl 0Cn.Now note that on Bl 0Cn we have that ϵ−2 

> i

ωϵi locally converges to the Burns-Simanca metric η and thus since 

ϵ−δi || L∗ 

> ωϵi

ψi|| C0,α δ−4(Bl pM ) → 0 from 4 .1.13, and Lϵ−2 

> iωϵi

= ϵ4 

> i

Lωϵi ,

we have Lηψ∞ = 0 on Bl 0C2. On the other hand by assumption 

ϵ−δi ρi(xi)δ > R δ,CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 37 and by definition of xi

ψi(xi) = ρi(xi)δ,

so 

ψ∞(x∞) ≥ Rδ.

Thus, we have a contradiction of Proposition 3.3.4 since ψ∞ decays at infinity but is nonzero. Step 4: Lastly, we need to deal with the case when ϵ−1 

> i

ρi(xi) is unbounded. Note again that ρi(xi) → 0, and thus in this case we have ρi(xi) = |xi|. Choose ri → 0 and Ri → ∞ 

such that 

Ri|xi| → 0, r i|xi|ϵ−1 

> i

→ ∞ .

We consider the annulus Ai := BRi|xi| \ Bri|xi|. By rescaling by |xi|, we identify Ai with 

BRi \ Bri ⊂ Cn \ { 0}. On BRi \ Bri we consider the metric |xi|−2ωϵi (here ωϵi on BRi \ Bri

is ωϵi on Ai pulled back along the rescaling by |xi|). The point of these annuli is that on 

Mp they are shrinking to p, where ω is becoming euclidean, and on Bl 0Cn they are going to infinity where the Burns-Simanca metric is Euclidean. In other words, these metrics converge locally in any Ck norm to the standard Euclidean metric on Cn \ { 0}.Now, under this identification all of the points xi lie on the unit sphere in Cn \ { 0}, and thus up to a subsequence xi → x∞. Further, the functions |xi|−δψi, when viewed as functions on larger annuli in Cn \{ 0}, inherit uniform C4,α δ bounds from 4.1.12. Thus, up to a sequence 

|xi|−δψi → ψ∞ locally in C4,α for possibly smaller α. We then have ψ∞ ∈ C4,α δ and 

ψ∞(x∞) = 1 , ∆2

> euc

ψ∞ = 0 ,

a contradiction of Proposition 3.3.2 based on our choice of δ.The above proposition can be summarized as follows. 

Corollary 4.1.14. Let δ ∈ (−1, 0) sufficiently small. 

• Suppose n > 2. For ϵ small there exists a constant K > 0 independent of ϵ such that 

˜L∗ 

> ωϵ

is an isomorphism and 

|| ( ˜L∗ 

> ωϵ

)−1|| C4,α δ →C0,α δ−4

≤ K. 

• Suppose n = 2 . For ϵ small there exists a constant K > 0 independent of ϵ such that 

˜L∗ 

> ωϵ

is an isomorphism and 

|| ( ˜L∗ 

> ωϵ

)−1|| C4,α δ →C0,α δ−4

≤ Kϵ δ.

Proof. The above proposition shows that ˜L∗ 

> ωϵ

is injective. The operator ˜L∗ 

> ωϵ

differs from the index zero operator L∗ 

> ωϵ

by a finite rank operator, and thus must also have index zero. Thus we also have surjectivity, and the statement about the norms follows directly. CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 38 We wish to draw attention to the fact that we could have proven the exact same estimates but for the operator Lωϵ in n ≥ 3. This makes the remainder of the proof of our main results slightly cleaner, we only insist on L∗ 

> ωϵ

to uniformize the approach across dimensions. The precise reason that we are unable to prove the estimates for Lωϵ in n = 2 is due to the added analytic difficulty necessitating the existence of a function on M in the kernel of L∗ 

> ω

which is nonvanishing at the blowup point. Since our problem is open in nature (in the topological sense), one could ask if this condition is satisfied for K¨ ahler metrics near our initial metric 

ω, perhaps even within its own K¨ ahler class. Similar generic aspects of eigenfunctions have been studied for example by Uhlenbeck [34] in the obviously less restrictive Riemannian case, it would be interesting to study similar questions in the K¨ ahler case. So, we end this section with a question. 

Question 4.1.15. If (M, ω ) is a compact K¨ ahler manifold, then does any open set containing 

ω in the K¨ ahler class [ω] contain a K¨ ahler metric ω′ such that Lω′ has only constants in its kernel? 

# 4.2 Alteration of ωϵ and the n = 2 Case 

For this section we assume n = 2 exclusively. We will construct instead a metric ˜ ωϵ on 

Bl pM which is a slight alteration of ωϵ but still is a scaling down of the Burns-Simanca metric in Brϵ . The main advantage will be that the gluing annulus B2rϵ \ Brϵ will have better behavior, namely we will no longer have to multiply the log term in the definition of ωϵ by a cutoff. This better approximation is necessitated by the need to prove some estimate on the difference S(ωϵ) − S(ω). What appears here is only a minor alteration to the construction in [31]. The main point is to argue that there exists a function g ∈ Ker( L∗

> ω

) on all of M , and a function Γ on Mp such that 

LωΓ = g (4.2.1) on Mp, and Γ( z) = log |z|+ψ(z) near p, where ψ ∈ C4,α  

> 1

(Mp). Note that by elliptic regularity 

g must be smooth on M , and Γ is also smooth on Mp.To this end, let χ once again be a cutoff supported in B2 and equal to 1 in B1. Let 

χr := χ(z/r ) for any r > 0. Then we will define the metric 

ω′ 

> r

:= √−1∂∂ (|z|2 + χr(z)φ(z)) on C2 \ { 0}. This metric is flat outside B2r and equal to ω in Br. We need the following estimates. 

Lemma 4.2.2. • For any δ ∈ R and sufficiently small r > 0 there is a positive constant 

C independent of r such that 

|| (Lω′ 

> r

+ 14∆2

> euc

)f || C0,α δ−4(C2\{ 0}) ≤ Cr 2|| f || C4,α δ (C2\{ 0})CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 39 

for any f : C2 \{ 0} → R. Then for r sufficiently small Lω′ 

> r

is an isomorphism whenever 

δ is not an indicial root of ∆2

> euc

.

• For any δ ≤ − 2 we have Lω′ 

> r

(log |z|) ∈ C0,α δ (B1).Proof. For the first claim, outside of B2r we already have that L˜ωr = −14 ∆2

> euc

, so we only focus within B2r. Note that within B2r we have 

∇i(χrφ) = O(|z|4−i),

and the metric is given by 

ω′ 

> r,jk

= δjk + ∂j ∂k(χrφ).

As long as r is sufficiently small, in B2r we have 

ω′jk r = δjk − ∂j ∂k(χrφ) + O(|z|4).

For the Ricci curvature in B2r we have 

Rjk = ∂j ∂k(log det[ δℓm + ∂ℓ∂m(χrφ)]) = ∂j ∂k(∂ℓ∂ℓ(χrφ)) + O(|z|2),

so then we have that in B2r

Lω′ 

> r

f = −14∆2

> euc

f + δℓm ∂ℓ∂m[∂j ∂k(χrφ)∂j ∂kf ] + ∂j ∂k(∂ℓ∂ℓ(χrφ)) ∂j ∂kf + O(|z|).

Thus we have in B2r there is some constant C such that 

|z|2

14∆2

> euc

f + Lω′ 

> r

f



= |z|2(δℓm ∂ℓ∂m[∂j ∂k(χrφ)∂j ∂kf ] + ∂j ∂k(∂ℓ∂ℓ(χrφ)) ∂j ∂kf + O(|z|)) 

≤ Cr 2∂j ∂kf

for r small, which proves the desired estimate. For the second claim we have 

Lω′ 

> r

log |z| = −14∆2 

> euc

log |z| + δℓm ∂ℓ∂m[∂j ∂k(χrφ)∂j ∂k log |z|]+∂j ∂k(∂ℓ∂ℓ(χrφ)) ∂j ∂k log |z| + O(|z|−1).

The claim then follows since log |z| is biharmonic away from zero. From this lemma we have that for any r sufficiently small there exists ξ1 ∈ C4,α  

> 2−τ

for any 

τ > 0 such that 

Lω′ 

> r

(ξ1) = Lω′ 

> r

(log |z|),

which implies that near pLω(χr(z) log |z| − χr(z)ξ1(z)) = 0 ,CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 40 and the left side is a function on all of M . Arguing in the exact same fashion as in Lemma 4.1.2, if g1, ..., g d is an L2-orthonormal basis for Ker( L∗

> ω

) then there exists points 

q′

> 1

, ..., q ′ 

> d

∈ Mp such that there is a function ξ2 ∈ C4,α (M ) satisfying 

Lω(χr log |z| − χrξ1 − ξ2) = −

> d

X

> i=1

ξ2(q′

> i

)gi

on Mp. We can subtract a constant from ξ2 to ensure that ξ2(p) = 0, and then we set Γ = χr(log |z| − ξ1) − ξ2,

which then has the desired properties. Now we define ˜ωϵ := ωϵ + ϵ2√−1∂∂ (γ1(Γ − log ϵ)) . (4.2.3) We have that near p, Γ( z) = log |z| + ψ with ψ ∈ C4,α  

> 1

(Mp), so we can alternatively write ˜ωϵ = √−1∂∂ (|z|2 + γ1(z)φ(z) + ϵ2 log |z| + ϵ2γ1(z)ψ(z)) . (4.2.4) Note that in this presentation it is clear that we have preserved the property that the metric is equal to ϵ2η in Brϵ after changing coordinates. Lastly, we will need to have the same bounds on ( ˜L∗ 

> ˜ωϵ

)−1 as we did for ( ˜L∗ 

> ωϵ

)−1. We have them because || γ1Γ|| C4,α    

> 2(Bl pM)

≤ C log |rϵ|

> r2
> ϵ

, and using Lemma 3.3.6 in the last inequality we have 

|| ϕ|| C4,α δ (Bl pM ) ≤ Kϵ δ|| ˜L∗ 

> ωϵ

ϕ|| C0,α δ−4(Bl pM ) ≤ Kϵ δ(|| ˜L∗ 

> ˜ωϵ

ϕ|| C0,α δ−4(Bl pM ) + || (L∗ 

> ωϵ

− L∗ 

> ˜ωϵ

)ϕ|| C0,α δ−4(Bl pM ))

≤ Kϵ δ(|| ˜L∗ 

> ˜ωϵ

ϕ|| C0,α δ−4(Bl pM ) + C(ϵ2(1 −β)β log |ϵ|)|| ϕ|| C4,α δ (Bl pM )),

which is equivalent to 

|| ϕ|| C4,α δ (Bl pM ) ≤ Kϵ δ

1 − KCϵ 2(1 −β)+ δβ log |ϵ||| ˜L∗ 

> ˜ωϵ

ϕ|| C0,α δ−4(Bl pM )

≤ (K + 1) ϵδ|| ˜L∗ 

> ˜ωϵ

ϕ|| C0,α δ−4(Bl pM ),

(4.2.5) for small ϵ, given that δ ∈ (−1, 0). We will just replace K + 1 with K when discussing this bound later. 

# 4.3 Further Estimates and Completion of the Perturbation 

Per 4.0.1, we now use the estimates on ( ˜L∗ 

> ωϵ

)−1 and ( ˜L∗ 

> ˜ωϵ

)−1 to find and solve an equation with right hand side going to zero as ϵ → 0, providing the main result. We deal with the 

n > 2 case first. CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 41 

## The Equation for n > 2:

We would like to find ϕ solving the equation 

S(ω) − S(ωϵ + √−1∂∂ϕ ) = −∂ϕ · ∂S (ωϵ) − ∂S (ωϵ) · ∂ϕ − 12ϕ∆ωϵ S(ωϵ) −

> d

X

> i=1

ϕ(qi)fi, (∗1)for each ϵ sufficiently small, where the fi and qi are as in Lemma 4.1.2. Linearizing, we can instead write S(ωϵ + √−1∂∂ϕ ) as 

S(ωϵ + √−1∂∂ϕ ) = S(ωϵ) + Lωϵ (ϕ) + Qωϵ (ϕ),

where Qωϵ (ϕ) are the higher order terms. Then the equation ( ∗1) is equivalent to 

S(ω) − S(ωϵ) − Qωϵ (ϕ) = Lωϵ ϕ − ∂ϕ · ∂S (ωϵ) − ∂S (ωϵ) · ∂ϕ − 12ϕ∆ωϵ S(ωϵ) −

> d

X

> i=1

ϕ(qi)fi.

From the formula 4.1.1 and the definition 4.1.3 we recognize the right side of the equation now as ˜L∗ 

> ωϵ

ϕ, multiplying both sides by the inverse we have that ( ∗1) is equivalent to ( ˜L∗ 

> ωϵ

)−1(S(ω) − S(ωϵ) − Qωϵ (ϕ)) = ϕ. 

Now, if we consider the map 

Nϵ : C4,α δ (Bl pM ) → C4,α δ (Bl pM )

ϕ 7 → ( ˜L∗ 

> ωϵ

)−1(S(ω) − S(ωϵ) − Qωϵ (ϕ)) ,

(∗1) can be rephrased as a fixed point problem for the nonlinear operator Nϵ. We will now work to apply the Banach fixed point theorem. We already have bounds on ( ˜L∗ 

> ωϵ

)−1 from Corollary 4.1.14, we also need bounds on S(ωϵ) − S(ω) and Qωϵ (ϕ). 

Lemma 4.3.1. Let k be a nonnegative integer, α ∈ (0 , 1) , and δ ∈ R. Then if c0 is as in Lemma 3.3.6 and 

|| ϕ1|| Ck+4 ,α   

> 2(Bl pM)

, || ϕ2|| Ck+4 ,α    

> 2(Bl pM)

≤ c0,

then there is some C > 0 independent of ϵ such that 

|| Qωϵ (ϕ2)−Qωϵ (ϕ1)|| Ck,α δ (Bl pM ) ≤ C(|| ϕ1|| Ck+4 ,α    

> 2(Bl pM)

+|| ϕ2|| Ck+4 ,α   

> 2(Bl pM)

)|| ϕ1 −ϕ2|| Ck+4 ,α δ (Bl pM ),

for all ϵ small. Proof. By the mean value inequality there is a t ∈ [0 , 1] such that χ = tϕ 1 +(1 −t)ϕ2 satisfies 

|| Qωϵ (ϕ2) − Qωϵ (ϕ1)|| Ck,α δ (Bl pM ) ≤ || DQ ωϵ,χ (ϕ2 − ϕ1)|| Ck,α δ (Bl pM ).CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 42 On the other hand we have 

DQ ωϵ,χ = Lωχ − Lωϵ ,

where ωχ := ωϵ + √−1∂∂χ . Then since || χ|| Ck+4 ,α    

> 2(Bl pM)

≤ c0 by Lemma 3.3.6 we have 

|| Qωϵ (ϕ2) − Qωϵ (ϕ1)|| Ck,α δ (Bl pM ) ≤ C|| χ|| Ck+4 ,α   

> 2(Bl pM)

|| ϕ1 − ϕ2|| Ck+4 ,α δ (Bl pM )

≤ C(|| ϕ1|| Ck+4 ,α    

> 2(Bl pM)

+ || ϕ2|| Ck+4 ,α   

> 2(Bl pM)

)|| ϕ1 − ϕ2|| Ck+4 ,α δ (Bl pM ).

Lemma 4.3.2. Let δ < 0 be chosen sufficiently small. There is a constant c1 > 0 independent of ϵ such that if 

|| ϕ1|| C4,α   

> 2(Bl pM)

, || ϕ2|| C4,α    

> 2(Bl pM)

≤ c1,

then 

||N ϵ(ϕ1) − N ϵ(ϕ2)|| C4,α δ (Bl pM ) ≤ 12|| ϕ1 − ϕ2|| C4,α δ (Bl pM ),

for all ϵ small. Proof. First, we have that 

Nϵ(ϕ1) − N ϵ(ϕ2) = ( ˜L∗ 

> ωϵ

)−1(Qωϵ (ϕ2) − Qωϵ (ϕ1)) .

From the bound on ( ˜L∗ 

> ωϵ

)−1 in Corollary 4.1.14 and the bounds in Lemma 4.3.1, the result follows once c1 is chosen small enough. 

Lemma 4.3.3. For ϵ sufficiently small we have 

|| S(ωϵ) − S(ω)|| C2,α δ−4(Bl pM ) ≤ Cr 4−δϵ

for some constant C independent of ϵ.Proof. S(ωϵ) ≡ S(ω) on M \ B2rϵ and S(ωϵ) ≡ 0 on Brϵ , so the lemma really only needs to be checked in B2rϵ \ Brϵ . Rewriting 3.2.2 in n ≥ 3, in this region the key is that 

ωϵ = ωeuc + √−1∂∂ (γ1(z)φ(z) + ϵ2γ2(z)ψ(ϵ−1z)) ,

and for any δ

|| γ1(z)φ(z) + ϵ2γ2(z)ψ(ϵ−1z)|| C6,α δ (B2rϵ \Brϵ ) ≤ Cr 4−δϵ .

This estimate is because when ϵ is small, in the annulus B2rϵ \ Brϵ we have 

ϵ2ψ(ϵ−1z) = O



ϵ2 r4−2nϵ

ϵ4−2n



= O(r4 

> ϵ

),

specifically due to our choice of β. With this estimate we can conclude 

|| S(ωϵ)|| C2.α δ−4(B2rϵ \Brϵ ) ≤ Cr 4−δϵ .CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 43 Combining all the estimates, we can solve ( ∗1). 

Proposition 4.3.4. Assume n > 2 and δ < 0 sufficiently small. Then for all ϵ > 0

sufficiently small, (∗1) admits a solution with || ϕ|| C4,α δ (Bl pM ) ≤ c1ϵ2−δ.Proof. Let B denote the ball of radius c1ϵ2−δ in C4,α δ (Bl pM ). If ϕ ∈ B , then || ϕ|| C4,α    

> 2(Bl pM)

≤

c1. Then the above estimates give that Nϵ is a contraction on B for ϵ small. We show in addition that Nϵ(B) ⊂ B for ϵ small, from which the proposition follows immediately by the Banach fixed point theorem. First, we have from Lemma 4.3.2 

||N ϵ(ϕ)|| C4,α δ (Bl pM ) ≤ ||N ϵ(ϕ) − N ϵ(0) || C4,α δ (Bl pM ) + ||N ϵ(0) || C4,α δ (Bl pM )

≤ 12|| ϕ|| C4,α δ (Bl pM ) + ||N ϵ(0) || C4,α δ (Bl pM ).

Recall Nϵ(0) = ( ˜L∗ 

> ωϵ

)−1(S(ω) − S(ωϵ)), so from the uniform estimates on ( ˜L∗ 

> ωϵ

)−1 in Corol-lary 4.1.14 and the estimate on S(ω) − S(ωϵ) in Lemma 4.3.3 we have independent of ϵ the bound 

||N ϵ(0) || C4,α δ (Bl pM ) ≤ Cr 4−δϵ .

Now, (4 − δ)β > 2 − δ when n > 2 and δ is chosen small enough, so then when ϵ is sufficiently small 

||N ϵ(0) || C4,α δ (Bl pM ) ≤ 12c1ϵ2−δ,

which completes the proof. 

## The Equation for n = 2 :

The n = 2 case is only very slightly different. We instead solve the equation 

S(ω) − S(˜ ωϵ + √−1∂∂ϕ ) = −∂ϕ · ∂S (˜ ωϵ) − ∂S (˜ ωϵ) · ∂ϕ − 12ϕ∆˜ωϵ S(˜ ωϵ) −

> d

X

> i=1

ϕ(qi)fi − ϵ2g, (∗2)where we have the addition of g from 4.2.1. By an entirely similar calculation as above, ( ∗2)is equivalent to ( ˜L∗ 

> ˜ωϵ

)−1(S(ω) − S(˜ ωϵ) + ϵ2g − Q˜ωϵ (ϕ)) = ϕ, 

so we instead consider the fixed point problem for the operator 

Nϵ : C4,α δ (Bl pM ) → C4,α δ (Bl pM )

ϕ 7 → ( ˜L∗ 

> ˜ωϵ

)−1  S(ω) − S(˜ ωϵ) + ϵ2g − Q˜ωϵ (ϕ) .

Once again we just need to prove similar estimates as in the n > 2 case. CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 44 

Lemma 4.3.5. Let δ < 0 be chosen sufficiently small. There is a constant c1 > 0 independent of ϵ such that if 

|| ϕ1|| C4,α   

> 2(Bl pM)

, || ϕ2|| C4,α    

> 2(Bl pM)

≤ c1ϵ−δ,

then 

||N ϵ(ϕ1) − N ϵ(ϕ2)|| C4,α δ (Bl pM ) ≤ 12|| ϕ1 − ϕ2|| C4,α δ (Bl pM ),

for all ϵ small. Proof. The proof is identical to Lemma 4.3.2, we just need ϵ−δ to account for the slightly weaker bound on ( ˜L∗ 

> ˜ωϵ

)−1.

Lemma 4.3.6. Let δ < 0 be chosen sufficiently small. For ϵ sufficiently small we have 

|| S(˜ ωϵ) − ϵ2g − S(ω)|| C2,α δ−4

≤ Cr 4−δϵ

for some constant C independent of ϵ.Proof. In Brϵ there is nothing to prove since there ˜ ωϵ is scalar flat. In B2rϵ \ Brϵ we have from rewriting 4.2.4 ˜ωϵ = ωeuc + √−1∂∂ (ϵ2 log |z| + γ1(φ + ϵ2ψ)) .

Since Lωeuc = −14 ∆2 

> euc

2.2.4 we have 

S(˜ ωϵ) = −14∆2

> euc

(γ1(φ + ϵ2ψ)) + Qωeuc (ϵ2 log |z| + γ1(φ + ϵ2ψ)) .

Now, for the Qωeuc term we have, recalling that ψ ∈ C4,α  

> 1

(Mp)

|| Qωeuc (ϵ2 log |z| + γ1(φ + ϵ2ψ)) || C2,α δ−4(B2rϵ \Brϵ )

≤ C|| ϵ2 log |z| + γ1(φ + ϵ2ψ)|| C6,α    

> 2(B2rϵ \Brϵ )

|| ϵ2 log |z| + γ1(φ + ϵ2ψ)|| C6,α δ (B2rϵ \Brϵ )

≤ C(ϵ2−2β log |ϵ| + ϵ2β )( ϵ2−δ log |ϵ| + ϵ(4 −δ)β ) ≤ r4−δϵ ,

where we have used Lemma 4.3.1, and thus 

|| S(˜ ωϵ)|| C2,α δ−4(B2rϵ \Brϵ ) ≤ Cr 4−δϵ .

On M \ B2rϵ we have from 4.2.3 ˜ ωϵ = ω + ϵ2√−1∂∂ Γ and thus from 4.2.1 

S(˜ ωϵ) = S(ω) + ϵ2LωΓ + Qω(ϵ2Γ) = S(ω) + ϵ2g + Qωϵ (ϵ2Γ) .

We can estimate the last term using Lemma 4.3.1 once again to get 

|| Qωϵ (ϵ2Γ) || C2,α δ−4(M \B2rϵ ) ≤ C|| ϵ2Γ|| C6,α    

> 2(M\B2rϵ )

|| ϵ2Γ|| C6,α δ (M \B2rϵ ) ≤ C ϵ2

r2

> ϵ

log |ϵ| ϵ2

rδϵ

log |ϵ| ≤ Cr 4−δϵ

due to our range of β. Putting these regions together gives the desired estimate. CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 45 Combining all the estimates, we can solve ( ∗2). 

Proposition 4.3.7. Assume n = 2 and δ < 0 sufficiently small. Then for all ϵ > 0

sufficiently small, (∗2) admits a solution with || ϕ|| C4,α δ (Bl pM ) ≤ c1ϵ2−2δ.Proof. Let B denote the ball of radius c1ϵ2−2δ in C4,α δ (Bl pM ). If ϕ ∈ B , then || ϕ|| C4,α    

> 2(Bl pM)

≤

c1ϵ−δ. Then the above estimates give that Nϵ is a contraction on B for ϵ small. Again, we show that Nϵ(B) ⊂ B for ϵ small, and we conclude by the Banach fixed point theorem. First, we have using Lemma 4.3.5 

||N ϵ(ϕ)|| C4,α δ (Bl pM ) ≤ ||N ϵ(ϕ) − N ϵ(0) || C4,α δ (Bl pM ) + ||N ϵ(0) || C4,α δ (Bl pM )

≤ 12|| ϕ|| C4,α δ (Bl pM ) + ||N ϵ(0) || C4,α δ (Bl pM ).

Recall Nϵ(0) = ( ˜L∗ 

> ˜ωϵ

)−1 (S(ω) − S(˜ ωϵ) + ϵ2g), so from the uniform estimates on ( ˜L∗ 

> ˜ωϵ

)−1 from 4.2.5 and the estimates in Lemma 4.3.6 on S(ω) − S(˜ ωϵ) + ϵ2g we have independent of ϵ the bound 

||N ϵ(0) || C4,α δ (Bl pM ) ≤ Cϵ δr4−δϵ .

Now, δ + (4 − δ)β > 2 − 2δ for our range of β if δ is chosen small enough, so then when ϵ is sufficiently small 

||N ϵ(0) || C4,α δ (Bl pM ) ≤ 12c1ϵ2−2δ,

which completes the proof. 

## Proof of the Main Result: 

Once again, the point is that both ( ∗1) and ( ∗2) are equations for the difference S(ω) −

S(ωϵ + √−1∂∂ϕ ), and we can solve them with sufficiently good estimates on ϕ and S(ωϵ)and their derivatives, so that the right hand side of the equation becomes small in ϵ. This gives us our main result. 

Proof. (of the Main Result) Let’s do the n = 2 case, the n > 2 case is entirely similar, just without the g term. We can get that ( ∗2) has a solution with || ϕ|| C4,α δ (Bl pM ) ≤ c1ϵ2−2δ for all 

ϵ sufficiently small (Proposition 4.3.7). If we can show that max  

> M

| − ∂ϕ · ∂S (˜ ωϵ) − ∂S (˜ ωϵ) · ∂ϕ − 12ϕ∆˜ωϵ S(˜ ωϵ) −

> d

X

> i=1

ϕ(qi)fi − ϵ2g| → 0, as ϵ → 0,

then S(ωϵ + √−1∂∂ϕ ) will have the same sign everywhere as S(ω). Since M is compact, g

and the fi are bounded, and |ϕ| ≤ c1ϵ2 on all of M , so we do not need to be concerned about CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 46 the last two terms. For the first two terms, note first of all that S(˜ ωϵ) ≡ 0 in Brϵ , so in that region we are fine. In M \ Brϵ we have 

|∇ ϕ| ≤ c1rδ−1 

> ϵ

ϵ2−2δ = c1ϵ2−β+( β−2) δ,

|∇ [S(ωϵ) − ϵ2g − S(ω)] | ≤ Cr δ−5 

> ϵ

r4−δϵ = Cϵ −β ,

and ϵ2(1 −β)+( β−2) δ → 0 as ϵ → 0 for our range of β, so the terms −∂ϕ · ∂S (˜ ωϵ) − ∂S (˜ ωϵ) · ∂ϕ 

are fine. What remains is the term −12 ϕ∆˜ωϵ S(˜ ωϵ). For this note once again that in M \ Brϵ

we have 

|ϕ| ≤ c1rδϵ ϵ2−2δ = c1ϵ2+( β−2) δ,

|∇ 2[S(ωϵ) − ϵ2g − S(ω)] | ≤ Cr δ−6 

> ϵ

r4−δϵ = Cϵ −2β ,

and ϵ2(1 −β)+( β−2) δ → 0 as ϵ → 0 for our range of β.Lastly, we need to check that any solution ϕ to ( ∗1) or ( ∗2) will be smooth, so that the metric we construct on Bl pM with our desired scalar curvature properties is indeed smooth. This is a routine elliptic bootstrapping argument but we will write the details anyway. Let 

ϕ ∈ C4,α (Bl pM ) be a solution to ( ∗1) or ( ∗2). Then in particular, in either case for some 

h ∈ C∞(M ), 

S(˜ ωϵ + √−1∂∂ϕ ) = ∂ϕ · ∂S (˜ ωϵ) + ∂S (˜ ωϵ) · ∂ϕ + 12ϕ∆˜ωϵ S(˜ ωϵ) + h. 

We can also split this into a system of equations 12∆˜ωϕ F = ∂ϕ · ∂S (˜ ωϵ) + ∂S (˜ ωϵ) · ∂ϕ + 12ϕ∆˜ωϵ S(˜ ωϵ) + h, 

log det(˜ gϕ,jk ) = F, 

where for convenience we have written ˜ ωϕ := ˜ ωϵ + √−1∂∂ϕ , and for the associated metric ˜ gϕ.For the first equation, we see that F solves a linear second order elliptic PDE with coefficients in C2,α (Bl pM ), and the right hand side is in C3,α (Bl pM ), so we have that F ∈ C4,α (Bl pM ). Differentiating both sides of the second equation we get (˜ gϕ)jk ∂j ∂k(∂iϕ) = −(˜ gϕ)jk (∂i ˜gϵ,jk ) + ∂iF, 

so ∂iϕ can be thought of as solving a linear second order elliptic PDE with coefficients in 

C2,α (Bl pM ) and right hand side in C2,α (Bl pM ). Since we already had that ∂iϕ ∈ C3,α (Bl pM )this yields that ∂iϕ ∈ C4,α (Bl pM ), and finally ϕ ∈ C5,α (Bl pM ). Continuing this argument inductively gives that ϕ is actually smooth. CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 47 

# 4.4 Positive Scalar Curvature K¨ ahler Surfaces and Further Discussion 

## Positive Scalar Curvature K¨ ahler Surfaces 

The most interesting consequences of the main result come in the case of positive scalar curvature in complex dimension 2. If ( M, ω ) is a K¨ ahler manifold, and ρ is its Ricci form, recall we have the following equation for the total scalar curvature, 

Z

S(ω)ωn

n! = 2πc 1(M ) ∪ [ω]n−1

(n − 1)! , (4.4.1) showing that the total scalar curvature of a K¨ ahler metric actually only depends on the K¨ ahler class. This formula can be used to show that the positivity of total scalar curvature has a dramatic effect on the holomorphic sections of the canonical bundle. 

Proposition 4.4.2 (Yau [36]) . Let M be a compact complex manifold for which there exists a K¨ ahler metric of positive total scalar curvature. Then M has Kodaira dimension −∞ ,that is, the canonical bundle of M and all of its powers have no global holomorphic sections. Moreover, the converse is true in the case of compact K¨ ahler surfaces. 

We will now list some basic facts about the Kodaira-Enriques classification of complex surfaces, for which a reference is [6]. Kodaira dimension is invariant under blowup, and the Kodaira-Enriques classification classifies the K¨ ahler surfaces of Kodaira dimension −∞ up to blowups at points. First of all, a complex surface is called minimal if it has no complex submanifolds biholomorphic to CP 1 with self-intersection −1. Equivalently, a complex sur-face is minimal if it cannot be obtained from another via blowing up at a point. Furthermore, every complex surface is obtained from a minimal one via a finite sequence of blowups at points. The Kodaira-Enriques classification gives the minimal K¨ ahler surfaces of Kodaira dimension −∞ as follows. 

Proposition 4.4.3. Any compact K¨ ahler surface of Kodaira dimension −∞ is obtained from CP 2 or P(E) by a finite sequence of blowups at points, where E → Σ is a rank two holomorphic vector bundle over a compact Riemann surface. 

A surface which is birationally equivalent to CP 2 is called rational . Among the surfaces of Kodaira dimension −∞ , these are precisely those with zero first betti number [6]. Any surface of the form P(E) as above is known as a ruled surface . Of course, the Fubini-Study metric has positive scalar curvature, and it was shown in [36] that ruled surfaces also admit positive scalar curvature K¨ ahler metrics. Thus, our main result shows we can replace positive total scalar curvature in Yau’s result with pointwise positive scalar curvature in the case of K¨ ahler surfaces. Due to the gluing construction for positive scalar curvature Riemannian metrics of Gro-mov and Lawson, it was already known that these surfaces at least had Riemannian metrics CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 48 of positive scalar curvature [19]. In fact, one can say even more. A complex surface is said to be of K¨ ahler-type if there exists a Riemannian metric which is K¨ ahler with respect to the complex structure. This is equivalent to having even first betti number [6]. It was shown first in the minimal case in [24] and then in the general case in [16] using Seiberg-Witten in-variants that the existence of a positive scalar curvature Riemannian metric, not necessarily K¨ ahler, on a compact complex surface of K¨ ahler type, is enough to conclude the complex structure has Kodaira dimension −∞ . Thus, we have verified Theorem B. The contribution of this dissertation is validating the presence of (2) in Theorem B. One can phrase this result as drawing the following equivalences. First, positive scalar curvature Riemannian geometry and positive scalar curvature K¨ ahler geometry are in some sense the same on compact real 4 −manifolds for which a K¨ ahler structure exists (ignoring polarizations). Second, the algebro-geometric condition of Kodaira dimension −∞ for a compact complex algebraic surface can be differential geometrically restated as the existence of a K¨ ahler metric with positive scalar curvature. 

## Higher Dimensions and Further Questions 

The natural question to ask is if Theorem B extends to higher dimensions. The equivalence with Riemannian positive scalar curvature does not persist in higher dimensions. In [23] the counterexample of a smooth hypersurface of degree n + 3 in CP n+1 where n ≥ 3 is provided. This variety is simply connected and non-spin with real dimension ≥ 6, and thus it has a Riemannian metric of positive scalar curvature by the results of [19]. However, it has Kodaira dimension n and thus no positive scalar curvature K¨ ahler metric. On the other hand, there exists many conjectures in the literature on the relationship between positive (total) scalar curvature of K¨ ahler metrics (and non-K¨ ahler generalizations) and algebraic geometry in arbitrary dimension; a discussion of these conjectures can be found for example in [35]. In higher dimensions, one replaces (5) in Theorem B with the following notion: a complex manifold M is said to be uniruled if every point in M is contained in a rational curve , that is, a smooth complex curve biholomorphic to CP 1. We state here a K¨ ahler version of the conjecture. 

Conjecture 4.4.4. Let (M, ω ) be a compact K¨ ahler manifold of arbitrary dimension. Then the following are equivalent. 1. M has a K¨ ahler metric for which the total scalar curvature is positive. 2. M has a K¨ ahler metric of positive scalar curvature. 3. M has Kodaira dimension −∞ .4. M is uniruled. 

It is reasonable to contend that this may be optimistic. In dimension n ≥ 3, K¨ ahler manifolds, and in fact projective manifolds, are not closed under bimeromorphic transforma-tion, leading to the definition of the Fujiki and Moishezon classes, or manifolds birational to CHAPTER 4. PERTURBING TO APPROXIMATE SCALAR CURVATURE 49 K¨ ahler and projective manifolds, respectively. The proof of our main result makes heavy use of this unique property for surfaces. However, balanced manifolds , Hermitian manifolds with co-closed associated (1,1)-form, are closed under bimeromorphic transformation [1] [2]. Then the approach of [36] can be mirrored to show (1) and (4) are equivalent for balanced metrics on Moishezon manifolds [13], where one must consider instead the Chern scalar curvature in the case of a non-K¨ ahler balanced metric. Still, this is at most a warning sign for one particular approach to the above conjecture. Recently, Ou [26] extended the results of [7] to K¨ ahler manifolds, which together with the results of [35] implies that (1) and (4) are equivalent for K¨ ahler manifolds if one weakens the condition on the metric to being Gauduchon . Namely, uniruled is equivalent to non-pseudoeffective canonical bundle (meaning it does not admit a singular metric with weakly positive curvature) [26], which is equivalent to the existence of a Gauduchon metric with positive total Chern scalar curvature [35]. A Gauduchon metric is a Hermitian metric whose associated (1,1)-form’s ( n − 1)th exterior power is ∂∂ −closed. The equivalence of (3) and (4) in general is already a deep conjecture in birational ge-ometry and so we will not address it here. The proposal of the equivalence of (1) and (2) is perhaps the most optimistic. Philosophically, we interpret this as a question of whether having pointwise positive scalar curvature is truly an algebraic concept for K¨ ahler metrics, or just a vestige of the differential geometric point of view, unlike the total scalar curvature which certainly is algebraic. Some hope for the algebraic nature of pointwise positive scalar curvature is provided by the recent work of Sha [28] on a systolic inequality for the holo-morphic 2-systole of a positive scalar curvature K¨ ahler surface. In particular, the minimum volume of a holomorphic curve in a positive scalar curvature K¨ ahler surface is controlled by the inverse of the minimum of its scalar curvature. In this vein, one can ask if pointwise positive scalar curvature, like total scalar curvature, is really a property of the K¨ ahler class, that is, the polarization . We summarize the above in the following questions. 

Question 4.4.5. If (M, ω ) is a compact K¨ ahler manifold which admits a Gauduchon metric with positive (resp. negative) total Chern scalar curvature, then must it also admit a positive (resp. negative) total scalar curvature K¨ ahler metric? 

Question 4.4.6. If (M, ω ) is a compact K¨ ahler manifold with positive (resp. negative) total scalar curvature, then does the K¨ ahler class [ω] also admit a K¨ ahler metric with pointwise positive (resp. negative) scalar curvature? 

The positive case of Question 4.4.5 is simply the missing piece of the equivalence of (1) and (4) in Conjecture 4.4.4 after the work of [26] and [35]. An affirmative answer in the negative case would also provide a K¨ ahler version of the relationship between the image of total scalar curvature and pseudoeffectivity of the (anti-)canonical bundle in [35]. An affirmative answer to Question 4.4.6 would show that the existence of a positive (or negative) scalar curvature K¨ ahler metric is a property of the polarization. 50 

# Bibliography 

[1] Lucia Alessandrini and Giovanni Bassanelli. “Metric properties of manifolds bimero-morphic to compact K¨ ahler spaces”. In: J. Differential Geom. 37.1 (1993), pp. 95– 121. issn : 0022-040X,1945-743X. url : http://projecteuclid.org/euclid.jdg/ 1214453424 .[2] Lucia Alessandrini and Giovanni Bassanelli. “Modifications of compact balanced man-ifolds”. In: C. R. Acad. Sci. Paris S´ er. I Math. 320.12 (1995), pp. 1517–1522. issn :0764-4442. [3] Claudio Arezzo and Frank Pacard. “Blowing up and desingularizing constant scalar curvature K¨ ahler manifolds”. In: Acta Math. 196.2 (2006), pp. 179–228. issn : 0001-5962,1871-2509. doi : 10.1007/s11511- 006- 0004- 6 . url : https://doi.org/10. 1007/s11511-006-0004-6 .[4] Claudio Arezzo and Frank Pacard. “Blowing up K¨ ahler manifolds with constant scalar curvature. II”. In: Ann. of Math. (2) 170.2 (2009), pp. 685–738. issn : 0003-486X,1939-8980. doi : 10 . 4007 / annals . 2009 . 170 . 685 . url : https : / / doi . org / 10 . 4007 / annals.2009.170.685 .[5] Claudio Arezzo, Frank Pacard, and Michael Singer. “Extremal metrics on blowups”. In: Duke Math. J. 157.1 (2011), pp. 1–51. issn : 0012-7094,1547-7398. doi : 10.1215/ 00127094-2011-001 . url : https://doi.org/10.1215/00127094-2011-001 .[6] Wolf P. Barth et al. Compact complex surfaces . Second. Vol. 4. Ergebnisse der Math-ematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]. Springer-Verlag, Berlin, 2004, pp. xii+436. isbn : 3-540-00832-2. doi :

10.1007/978-3-642-57739-0 . url : https://doi.org/10.1007/978-3-642-57739-0.[7] S´ ebastien Boucksom et al. “The pseudo-effective cone of a compact K¨ ahler manifold and varieties of negative Kodaira dimension”. In: J. Algebraic Geom. 22.2 (2013), pp. 201–248. issn : 1056-3911,1534-7486. doi : 10.1090/S1056-3911-2012-00574-8 .

url : https://doi.org/10.1090/S1056-3911-2012-00574-8 .[8] Garrett M. Brown. The sign of scalar curvature on K¨ ahler blowups . arxiv:2405.12189. 2024. BIBLIOGRAPHY 51 [9] Xiuxiong Chen and Jingrui Cheng. “On the constant scalar curvature K¨ ahler metrics (I)—A priori estimates”. In: J. Amer. Math. Soc. 34.4 (2021), pp. 909–936. issn : 0894-0347,1088-6834. doi : 10.1090/jams/967 . url : https://doi.org/10.1090/jams/ 967 .[10] Xiuxiong Chen, Simon Donaldson, and Song Sun. “K¨ ahler-Einstein metrics on Fano manifolds. I: Approximation of metrics with cone singularities”. In: J. Amer. Math. Soc. 28.1 (2015), pp. 183–197. issn : 0894-0347,1088-6834. doi : 10.1090/S0894-0347-2014-00799-2 . url : https://doi.org/10.1090/S0894-0347-2014-00799-2 .[11] Xiuxiong Chen, Simon Donaldson, and Song Sun. “K¨ ahler-Einstein metrics on Fano manifolds. II: Limits with cone angle less than 2 π”. In: J. Amer. Math. Soc. 28.1 (2015), pp. 199–234. issn : 0894-0347,1088-6834. doi : 10.1090/S0894-0347-2014-00800-6 .

url : https://doi.org/10.1090/S0894-0347-2014-00800-6 .[12] Xiuxiong Chen, Simon Donaldson, and Song Sun. “K¨ ahler-Einstein metrics on Fano manifolds. III: Limits as cone angle approaches 2 π and completion of the main proof”. In: J. Amer. Math. Soc. 28.1 (2015), pp. 235–278. issn : 0894-0347,1088-6834. doi :

10.1090/S0894- 0347- 2014- 00801- 8 . url : https://doi.org/10.1090/S0894-0347-2014-00801-8 .[13] Ionut ¸ Chiose, Rare¸ s R˘ asdeaconu, and Ioana S ¸uvaina. “Balanced metrics on uniruled manifolds”. In: Comm. Anal. Geom. 27.2 (2019), pp. 329–355. issn : 1019-8385,1944-9992. doi : 10.4310/CAG.2019.v27.n2.a3 . url : https://doi.org/10.4310/CAG. 2019.v27.n2.a3 .[14] Ruadha´ ı Dervan and Lars Martin Sektnan. Extremal K¨ ahler metrics on blowups . arXiv:2110.13579. 2021. [15] Simon Donaldson. “Remarks on gauge theory, complex geometry and 4-manifold topol-ogy”. In: Fields Medallists’ Lectures , pp. 384–403. doi : 10.1142/9789812385215_0042 .eprint: https://www.worldscientific.com/doi/pdf/10.1142/9789812385215_ 0042 . url : https://www.worldscientific.com/doi/abs/10.1142/9789812385215_ 0042 .[16] Robert Friedman and John W. Morgan. “Algebraic surfaces and Seiberg-Witten in-variants”. In: J. Algebraic Geom. 6.3 (1997), pp. 445–479. issn : 1056-3911,1534-7486. [17] Akira Fujiki. “The moduli spaces and K¨ ahler metrics of polarized algebraic varieties”. In: S¯ ugaku 42.3 (1990), pp. 231–243. issn : 0039-470X,1883-6127. [18] Phillip Griffiths and Joseph Harris. Principles of algebraic geometry . Pure and Applied Mathematics. Wiley-Interscience [John Wiley & Sons], New York, 1978, pp. xii+813. 

isbn : 0-471-32792-1. [19] Mikhael Gromov and H. Blaine Lawson Jr. “The classification of simply connected manifolds of positive scalar curvature”. In: Ann. of Math. (2) 111.3 (1980), pp. 423–434. 

issn : 0003-486X. doi : 10.2307/1971103 . url : https://doi.org/10.2307/1971103 .BIBLIOGRAPHY 52 [20] Nigel Hitchin. “On the curvature of rational surfaces”. In: Differential geometry (Proc. Sympos. Pure Math., Vol. XXVII, Part 2, Stanford Univ., Stanford, Calif., 1973) .Vol. Vol. XXVII, Part 2. Proc. Sympos. Pure Math. Amer. Math. Soc., Providence, RI, 1975, pp. 65–80. [21] Daniel Huybrechts. Complex geometry . Universitext. An introduction. Springer-Verlag, Berlin, 2005, pp. xii+309. isbn : 3-540-21290-6. [22] Kunihiko Kodaira. “On K¨ ahler varieties of restricted type (an intrinsic characterization of algebraic varieties)”. In: Ann. of Math. (2) 60 (1954), pp. 28–48. issn : 0003-486X. 

doi : 10.2307/1969701 . url : https://doi.org/10.2307/1969701 .[23] Claude LeBrun. “Kodaira dimension and the Yamabe problem”. In: Comm. Anal. Geom. 7.1 (1999), pp. 133–156. issn : 1019-8385,1944-9992. doi : 10.4310/CAG.1999. v7.n1.a5 . url : https://doi.org/10.4310/CAG.1999.v7.n1.a5 .[24] Claude LeBrun. “On the scalar curvature of complex surfaces”. In: Geom. Funct. Anal. 

5.3 (1995), pp. 619–628. issn : 1016-443X,1420-8970. doi : 10.1007/BF01895835 . url :

https://doi.org/10.1007/BF01895835 .[25] August Newlander and Louis Nirenberg. “Complex analytic coordinates in almost com-plex manifolds”. In: Ann. of Math. (2) 65 (1957), pp. 391–404. issn : 0003-486X. doi :

10.2307/1970051 . url : https://doi.org/10.2307/1970051 .[26] Wenhao Ou. A characterization of uniruled compact K¨ ahler manifolds . arXiv:2501.18088. 2025. [27] Frank Pacard and Tristan Rivi` ere. Linear and nonlinear aspects of vortices . Vol. 39. Progress in Nonlinear Differential Equations and their Applications. The Ginzburg-Landau model. Birkh¨ auser Boston, Inc., Boston, MA, 2000, pp. x+342. isbn : 0-8176-4133-5. doi : 10.1007/978-1-4612-1386-4 . url : https://doi.org/10.1007/978-1-4612-1386-4 .[28] Zehao Sha. The 2-systole on compact K¨ ahler surfaces with positive scalar curvature .arXiv:2601.02901. 2026. [29] Santiago R. Simanca. “K¨ ahler metrics of constant scalar curvature on bundles over 

CP n−1”. In: Math. Ann. 291.2 (1991), pp. 239–246. issn : 0025-5831,1432-1807. doi :

10.1007/BF01445203 . url : https://doi.org/10.1007/BF01445203 .[30] Myong-Hee Sung. “K¨ ahler surfaces of positive scalar curvature”. In: Ann. Global Anal. Geom. 15.6 (1997), pp. 509–518. issn : 0232-704X,1572-9060. doi : 10.1023/A:1006543703319 .

url : https://doi.org/10.1023/A:1006543703319 .[31] G´ abor Sz´ ekelyhidi. An introduction to extremal K¨ ahler metrics . Vol. 152. Gradu-ate Studies in Mathematics. American Mathematical Society, Providence, RI, 2014, pp. xvi+192. isbn : 978-1-4704-1047-6. doi : 10.1090/gsm/152 . url : https://doi. org/10.1090/gsm/152 .BIBLIOGRAPHY 53 [32] G´ abor Sz´ ekelyhidi. “Blowing up extremal K¨ ahler manifolds II”. In: Invent. Math. 200.3 (2015), pp. 925–977. issn : 0020-9910,1432-1297. doi : 10.1007/s00222-014-0543-y .

url : https://doi.org/10.1007/s00222-014-0543-y .[33] G´ abor Sz´ ekelyhidi. “On blowing up extremal K¨ ahler manifolds”. In: Duke Math. J. 

161.8 (2012), pp. 1411–1453. issn : 0012-7094,1547-7398. doi : 10 . 1215 / 00127094 -1593308 . url : https://doi.org/10.1215/00127094-1593308 .[34] Karen Uhlenbeck. “Generic properties of eigenfunctions”. In: Amer. J. Math. 98.4 (1976), pp. 1059–1078. issn : 0002-9327,1080-6377. doi : 10.2307/2374041 . url : https: //doi.org/10.2307/2374041 .[35] Xiaokui Yang. “Scalar curvature on compact complex manifolds”. In: Trans. Amer. Math. Soc. 371.3 (2019), pp. 2073–2087. issn : 0002-9947,1088-6850. doi : 10.1090/ tran/7409 . url : https://doi.org/10.1090/tran/7409 .[36] Shing Tung Yau. “On the curvature of compact Hermitian manifolds”. In: Invent. Math. 25 (1974), pp. 213–239. issn : 0020-9910,1432-1297. doi : 10.1007/BF01389728 .

url : https://doi.org/10.1007/BF01389728 .[37] Shing Tung Yau. “On the Ricci curvature of a compact K¨ ahler manifold and the com-plex Monge-Amp` ere equation. I”. In: Comm. Pure Appl. Math. 31.3 (1978), pp. 339– 411. issn : 0010-3640,1097-0312. doi : 10.1002/cpa.3160310304 . url : https://doi. org/10.1002/cpa.3160310304 .


## Native file acquisition

```json
[
  {
    "url": "https://escholarship.org/content/qt5zp3d8hc/qt5zp3d8hc.pdf",
    "name": "qt5zp3d8hc.pdf",
    "size": 0,
    "role": "primary_object_file",
    "status": "download_failed",
    "error": "invalid_content",
    "http_status": 0,
    "reason": "object download returned an HTML landing/error page",
    "retry_after": 0,
    "identity_bound": true,
    "parent_url": "https://escholarship.org/content/qt5zp3d8hc/qt5zp3d8hc.pdf",
    "primary_label": false,
    "download_eligible": true,
    "label": ""
  }
]
```
