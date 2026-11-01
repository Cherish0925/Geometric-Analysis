---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: gluing manifolds with boundary and bordisms - Scholars' Bank]

Φ( z, −t, θ ) if ( z, t, θ ) ∈ N 1(K)Φ−1(z, −t, θ ) if ( z, t, θ ) ∈ N 2(K).

For each ε ∈ (0 , 12 ), we construct the generalized connected sum 

M =

(

(M1 \ V ε2 

> 1

)t(M2 \ V ε2 

> 2

)

)

/ ∼ε

where we introduce a relation ∼ε on the annuli ( V 11 \V ε2 

> 1

)t(V 12 \V ε2 

> 2

): If y ∈ V 11 \V ε2 

> 1

,then y ∼ε (F2 ◦ Ψε ◦ F −11 )( y). Observing that gε is invariant under Ψ ε, the metric descends to M . This finishes the definition of the family of Riemannian manifolds (M, g ε). Recalling that we assume the mean curvature HgK vanishes on ∂K , the proof of the following proposition is very similar to argument in Proposition 2.1.3 and so we omit it. 

Proposition 2.1.6. There is a constant C > 0, independent of ε, such that 

|Rgε | ≤ Cε −1 cosh 1−m(t), |Hgε | ≤ C cosh 2−m(t)48 on T ε(0 , 0) and 

∫

> M

|Rgε |dμ gε = O(εm−2),

∫

> ∂M

|Hgε |dσ gε = O(εm−2).

As for the local a priori estimate, we will need to again decompose the boundary of ∂T ε(α1, α 2) into two pieces 

∂1T ε(α1, α 2) = {(z, t, θ ) ∈ T ε(α1, α 2) : t = log ε + α1 or t = − log ε − α2}

∂2T ε(α1, α 2) = {(z, t, θ ) ∈ T ε(α1, α 2) : z ∈ ∂K }.

We will use the same notation for ∂1T ε(α1, α 2) and ∂2T ε(α1, α 2) as we did in the case of boundary embeddings. There is also an analogue of the estimates in Propositions 2.1.2 and 2.1.5 for the present case of relative embeddings. Its proof is very similar to that of Proposition 2.1.5 and we leave it to the reader. 

Proposition 2.1.7. Given γ ∈ (0 , m − 2) there are ε-uniform constants α1, α 2 > 1

and C > 0 satisfying the following statement for all ε ∈ (0 , e − max {α1,α 2}). If v, f ∈C0(T ε(α1, α 2)) satisfy ∆gε v = f , then 

v ≤ Cψ −γε

(

sup  

> Tε(α1,α 2)

|ψγ+2  

> ε

f | + sup  

> ∂1Tε(α1,α 2)

|ψγε v| + sup  

> ∂2Tε(α1,α 2)

|ψγ+1  

> ε

∂ν v|

)

pointwise on T ε(α1, α 2) and 

|| v|| C0   

> γ(Tε(α1,α 2))

≤ C

(

|| f || C0  

> γ+2 (Tε(α1,α 2))

+ || v|| C0   

> γ(∂1Tε(α1,α 2))

+ || ∂ν v|| C0 

> γ+1 (∂2Tε(α1,α 2))

)

.

49 2.2. The Linear Analysis 

Now that we have constructed the generalized connected sum ( M, g ε), we will turn our attention to equation (1.6). At this point, there is no need to consider the interior, boundary, and relative embedding cases independently as we did in Section 2.1. Unless otherwise mentioned, from now on we will speak of all three cases simultaneously. 

Our first task will be to study the family of linear operators (∆ gε , ∂ ν ) for ε ∈

(0 , 12 ). Before we continue, now is a good time to make some informal remarks. The first non-zero Steklov eigenvalue of (∆ gε , ∂ ν ), which we write as λε, is the smallest number such that the following equation admits a non-constant solution f



∆gε f = 0 on M∂ν f = λεf on ∂M. 

In general, λε → 0 as ε → 0. For this reason, there is no general result which would provide us a useful ε-uniform C0(M ) estimate for our linear problem. This in mind, we take two measures to combat this degeneracy. In addition to working in the weighted Banach spaces C0 

> γ

(M ) we introduced in Section 2.1, we will initially solve (with estimates) a modification of the linear problem. Speaking informally, this auxiliary problem is formulated by projecting the linear problem along a hand-made model for the first non-constant eigenfunction. This model is a function denoted by βε which takes the values 1 on M1 \ V ε 

> 1

, −1 on M2 \ V ε 

> 2

, and interpolates between them on the neck so that ∫ 

> M

βεdμ gε = 0 (see Section 2.21). 50 Given γ ∈ (0 , m − 2) and suitable functions f ∈ C 0

> γ+2

(M ), ` ∈ C 0 

> γ

(∂M ), we will produce a function u ∈ C 0 

> γ

(M ) satisfying 



∆gε u = f on M∂ν u = ` − λβ ε on ∂M 

(2.4) where λ is a real number depending on f and `. Notice that the functions f, ` must satisfy ∫

> M

f dμ gε =

∫

> ∂M

`dσ gε , (2.5) which is simply Green’s formula applied to u. We will refer to (2.5) as the orthogonality condition of equation (2.4). As we produce this solution, we also obtain an ε-uniform C0 

> γ

-norm a priori estimate for u using standard elliptic estimates on (M∗, g ∗) with the local a priori estimate of Propositions 2.1.2, 2.1.5, and 2.1.7. 

2.21. The linear problem I 

For each α1, α 2 > 1, let us fix ρ1 and ρ2, two smooth functions on M1 t M2

satisfying 

ρ1 =



1 on M1 \ T ε(α1, 0) 0 on M2 \ T ε(0 , −2 log ε − α1 − 1) 

ρ2 =



1 on M2 \ T ε(0 , α 2)0 on M1 \ T ε(−2 log ε − α2 − 1, 0) and ∂ν ρ1 ≡ 0, and ∂ν ρ2 ≡ 0 on ∂M 1 t ∂M 2. Understanding that ρ1 and ρ2 descend to the connected sum M , we then define βε : M → R by βε := ρ1 − ρ2.51 In the case of interior embeddings, where we have not altered the original metrics on the boundary, it is immediate that 

∫

> ∂M

βεdσ gε = 0 since we assume Vol g1 (∂M 1) = Vol g2 (∂M 2). To arrange for βε to have vanishing average value on the boundary in the case of boundary and relative embeddings (where dσ gε is affected by the gluing), we may have to choose α1 and α2 differently. However, notice that this can always be achieved by only increasing either α1 or α2.Since the estimates of Propositions 2.1.2, 2.1.5, and 2.1.7 also hold for these larger parameters, from now on we will assume that α1 and α2 have been chosen so that Propositions 2.1.2, 2.1.5, and 2.1.7 apply and ∫ 

> ∂M

βεdσ gε = 0 .

In this section we build an approximate solution to (2.4) which is straight-forward to estimate, but accumulates many error terms in a gluing process. This construction is summarized in the following lemma which will subsequently be applied iteratively to establish a genuine solution to the linear problem (2.4), with estimates. 

Lemma 2.2.1. Let γ ∈ (0 , m − 2) and B ∈ (0 , 1) . There is an ε0 > 0 such that the following statement is satisfied for all ε ∈ (0 , ε 0): Suppose f ∈ C 0

> γ+2

(M ) and 

` ∈ C 0

> γ+1

(∂M ) satisfy ∫

> M

f dμ gε =

∫

> ∂M

`dσ ε.

52 Then there is λ ∈ R, a function u ∈ C 0 

> γ

(M ), and an error term E ∈ C 0

> γ+2

(M )

satisfying 

∆gε u = f + E in M∂ν u = ` − λβ ε on ∂M 

∫ 

> M

udμ gε = 0 

Moreover, u, λ, and E satisfy the following estimates 

|| u|| C0   

> γ(M)

≤ C(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)

|λ| ≤ C(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)

|| E|| C0  

> γ+2 (M)

≤ Cε Bγ (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)

where the constant C > 0 is independent of ε and B.Proof. First we let ρT := 1 − ρ1 − ρ2 so that {ρ1, ρ T , ρ 2} forms a partition of unity on 

M . We decompose f and ` with respect to this partition, writing 

f1 = f ρ 1, fT = f ρ T , f2 = f ρ 2,`1 = `ρ 1, `T = `ρ T , `2 = `ρ 2.

Next, we produce an approximate solution on the neck T ε(α1, α 2). 

Claim 2.2.2. For the parameters γ, B and functions f, ` in Lemma 2.2.1, there is a unique function ˜uT ∈ C 0 

> γ

(T ε(α1, α 2)) satisfying 



∆gε ˜uT = fT in T ε(α1, α 2)˜uT = 0 on ∂1T ε(α1, α 2)

∂ν ˜uT = `T on ∂2T ε(α1, α 2).

(2.6) 53 Moreover, there is a constant CT > 0, independent of ε, such that 

|| ˜uT || C0   

> γ(Tε(α1,α 2))

≤ CT

(

|| fT || C0  

> γ+2 (Tε(α1,α 2))

+ || `T || C0 

> γ+1 (∂2Tε(α1,α 2))

)

.

Proof. Notice that T ε(α1, α 2) is a compact manifold with corners. This allows us to apply the regularity theory in [18] – by [18, Theorem 1], there is a unique function ˜uT ∈ C 2 (T ε(α1, α 2) ∪ ∂2T ε(α1, α 2)) ∩ C 0(T ε(α1, α 2)) solving equation (2.6). We may then apply Proposition 2.1.2, 2.1.5, and 2.1.7 with the parameter γ from the hypothesis of Lemma 2.2.1 and the function ˜ uT to arrive at the estimates in the claim. We extend the domain of ˜ uT to all of M , which we will continue to call ˜ uT ,by declaring ˜ uT = 0 on M \ T ε(α1, α 2). While ˜ uT may not be differentiable on 

∂1T ε(α1, α 2), the function uT := ρT ˜uT is differentiable since the support of ρT is contained in T ε(α1 + 1 , α 2 + 1). One can compute ∆gε uT = fT − q1 − q2

∂ν uT = `T − q∂ 

> 1

− q∂

> 2

where q∗ := ∆ gε (ρ∗ ˜uT ) and q∂ 

> ∗

:= ∂ν (ρ∗ ˜uT ). The quantities q∗ and q∂ 

> ∗

will be accounted for in the next step. We now turn to the pieces of M which come from the original manifolds M∗. We define λ according to the formula 

λ := 1

∫ 

> ∂M

(ρ1 + ρ2)dσ gε

(∫ 

> ∂M

(`β ε + q∂ 

> 1

− q∂ 

> 2

)dσ gε −

∫

> M

(f β ε + q1 − q2)dμ gε

)

, (2.7) 54 which can be interpreted as the projection of f and ` along βε. Observe that, for 

∗ = 1 , 2, this choice of λ implies 

∫

> M

(f∗ + q∗)dμ gε −

∫

> ∂M

(`ρ ∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗)dσ gε = 0 , (2.8) which we will use later. Using standard elliptic techniques [19][20], we may consider a distributional solution ˜ u∗ to the following system 



∆g∗ ˜u∗ = f∗ + q∗ + b∗δι∗ in M∗

∂ν ˜u∗ = `∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗ on ∂M ∗

∫ 

> M

˜u∗dμ g∗ = 0 where δι∗ denotes the Dirac distribution supported on the submanifold ι∗(K). Applying Green’s theorem to ˜ u∗, the constant b∗ is forced to be 

b∗ = 1Vol gK (K)

(∫ 

> ∂M ∗

(`∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗)dσ g∗ −

∫

> M∗

(f∗ + q∗)dμ g∗

)

.

Claim 2.2.3. There is a constant C′ > 0 independent of ε such that 

|˜u∗| ≤ C′(|| f || C0(M ) + || `|| C0(∂M ))

on M∗ \ V 1 

> ∗

,

|˜u∗| ≤ C′|x|2−m(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)

on V 1 

> ∗

, and 

|λ| ≤ C′(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

).

55 Proof. To estimate ˜ u∗, it will be useful to consider the decomposition ˜ u∗ = u∗ + ˆ u∗

where 

∆g∗ u∗ = f∗ + q∗ + Vol gK (K)b∗ in M∗

∂ν u∗ = `∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗ on ∂M ∗

∫ 

> M∗

u∗dμ g∗ = 0 



∆g∗ ˆu∗ = −Vol gK (K)b∗ + b∗δι∗ in M∗

∂ν ˆu∗ = 0 on ∂M ∗

∫ 

> M∗

ˆu∗dμ g∗ = 0 One can think of u∗ and ˆ u∗ as the finite and Green’s function parts of ˜ u∗, respectively. Near the submanifold ι∗(K), one can use the Green’s function construction presented in [19] to see that ˆ u∗ takes the form ˆu∗ = b∗

(m − 2) ωm−1

(|x|2−m + O(|x|3−m))

where ωm−1 is the volume of unit sphere Sm−1 and the term O(|x|3−m) depends only on the geometry of ( M∗, g ∗). It follows that there is a constant C0, independent of ε,such that 

|ˆu∗| ≤ C0b∗|x|m−2 (2.9) on V 1 

> ∗

.56 Next, we consider u∗. By taking p = n and k = 0 in the Lp estimate (A.1) from Theorem A.1.1 in the Appendix applied to u∗, there is a constant C1 > 0 so that 

|| u∗|| W 2,n (M∗,g ∗) ≤C1

( ∥∥∥∥f∗ + q∗ − V ol gK (K)

V ol g∗ (M∗)b∗

∥∥∥∥Ln(M∗,g ∗)

+ || `∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗|| W 1,n ∂ (M∗,g ∗)

)

for ∗ = 1 , 2 where C1 depends only on n and the geometry of ( M1, g 1), (M2, g 2). Now we may use the Sobolev Embedding Theorem [19, Theorem 2.30] and the Trace Theorem [20, Theorem B.10] to obtain the following C0 estimate 

|| u∗|| C0(M∗) ≤C2

( ∥∥∥∥f∗ + q∗ − V ol gK (K)

V ol g∗ (M∗)b∗

∥∥∥∥C0(M∗)

+ || `∗ + q∂ 

> ∗

+ ( −1) ∗λρ ∗|| C0(∂M ∗)

)

(2.10) where C2 is a constant depending only on n and the geometry of ( M1, g 1), (M2, g 2). To finish the proof of the claim, it suffices to estimate b∗, q ∗, and q∂ 

> ∗

. It will be convenient to consider the cases ∗ = 1 , 2 separately – in what follows, the statements will be made for ∗ = 1, though analogous arguments hold for ∗ = 2 and this is left to the reader. Subtracting (2.8) from b1 shows 

b1 = 1Vol gK (K)

( ∫  

> ∂2Tε(0 ,0) \∂2Tε(α1,0)

(`1 + q∂ 

> 1

− λρ 1)

(√ g∂ 

> 1

− √g∂ε

√g∂

> 1

)

dσ g1

−

∫  

> Tε(0 ,0) \Tε(α1,0)

(f1 + q1)

(√g1 − √gε

√g1

)

dμ g1

)

(2.11) where √g∂ 

> 1

and √g∂ε denote the Riemannian measures of g1|∂M 1 and gε|M1 ,respectively. Notice that we only integrate over T ε(0 , 0) \ T ε(α1, 0) since it contains 57 the supports spt( ρ1) ∩ spt( √g1 − √gε). We will inspect each term in the expression (2.11). On T ε(0 , 0) \ T ε(α1 + 1 , 0), notice that √g1 − √gε = O(εm−2) and on this portion of the boundary of M we have √g∂ 

> 1

− √g∂ε = O(εm−2). Using this, we can find a constant C3 which depends on γ and α1, though not on ε, such that the following inequalities hold 

∫  

> ∂2Tε(0 ,0) \∂2Tε(α1,0)

∣∣∣∣∣`1

(√ g∂ 

> 1

− √g∂ε

√g∂

> 1

)∣ ∣∣∣∣ dσ g1 ≤ C3εm−2|| `|| C0 

> γ+1 (∂M )

∫  

> Tε(0 ,0) \Tε(α1,0)

∣∣∣∣f1

(√g1 − √gε

√g1

)∣ ∣∣∣ dμ g1 ≤ C3εm−2|| f || C0 

> γ+2 (M)

.

Next we require pointwise bounds on q1 and q∂ 

> 1

in order to estimate (2.10). By definition of q1 and q∂ 

> 1

, we have the expressions 

q1 = (∆ gε ρ1)˜ uT + 2 gε(∇ρ1, ∇˜uT ) + ρ1(∆ gε ˜uT ) and q∂ 

> 1

= ρ1∂ν ˜uT

where we have used the fact that ∂ν ρ1 ≡ 0 on ∂M . It is worthwhile to note that the support of ∇ρ1 satisfies spt( ∇ρ1) ⊂ { y ∈ M1 : e−α1−1 ≤ dist g1 (y, ι 1(K)) ≤ 1},

which we emphasize does not depend on ε. With this and the pointwise estimates of 

gε in mind, notice that, for any α1 and α2, we may assume that ρ1 has been chosen so that both |∆gε ρ1| and |∇ ρ1|2 

> gε

are uniformly bounded in ε. Using this observation and the estimates of Propositions 2.1.2, 2.1.5, and 2.1.7, one can show 

|| (∆ gε ρ1)˜ uT || C0   

> γ(M)

≤ C4(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)58 for some C4 independent of ε. Inspecting (2.6), we can find a constant C5, depending on γ and α1 but not ε, so that 

|| ρ1∆gε ˜uT || C0(M ) ≤ C5|| f || C0 

> γ+2 (M)

|| ρ1∂ν ˜u|| C0(∂M ) ≤ C5|| `|| C0 

> γ+1 (∂M )

.

The final term we need to estimate is gε(∇ρ1, ∇˜up). Let us define 

Dα1 := T ε(α1, 0) \ T ε(α1 + 1 , 0) .

Since ˜ up is a solution to a Poisson equation on the region Dα1 , we may apply the classical gradient estimate [19], along with the pointwise estimates of gε above, to find an ε-uniform constant C6 satisfying 

|∇ ˜uT |2 

> gε

(y) ≤ C6

dist g1 (y, ∂D α1 )(|| ˜uT || C0(Dα1 ) + || fT || C0(Dα1 ))for all y ∈ Dα1 . Using this estimate with the Cauchy-Schwarz inequality, we can estimate the final term in the expression for q1

|gε(∇ρ1, ∇˜uT )|(y) ≤ C7(|| ˜uT || C0   

> γ(Dα1)

+ || fT || C0 

> γ+2 (Dα1)

)for another ε-uniform constant C7.Summarizing our work so far, we have found a constant C8, independent of ε,such that 

q1(y) ≤ C8(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

) (2.12) 

q∂ 

> 1

(y) ≤ C8(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M

)59 for all y ∈ Dα1 . Notice that C8 depends only on the geometry of ( M1, g 1), (K, g K ), 

γ, and α1. Integrating (2.12) yields the desired estimate of λ from the statement of the lemma. In turn, this estimate on λ, (2.12), and the expression (2.11) gives an estimate of the form 

|b1| ≤ e(m−2) tC9(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

)Finally, recalling (2.9) and (2.10), we have arrived at the desired estimate of |˜u1|.Now we chose cut-off functions which will be used to glue together the functions ˜u1, u T , and ˜ u2 from the above claims. For the parameter B ∈ (0 , 1) from the hypothesis of Lemma 2.2.1, let φ1, φ 2 : M → [0 , 1] be smooth functions satisfying 

φ1 =



1 on M1 \ T ε(−B log ε, 0) 0 on M2 \ T ε(0 , −(2 − B) log ε − 1) 

φ2 =



1 on M1 \ T ε(0 , −B log ε)0 on M2 \ T ε(−(2 − B) log ε − 1, 0) which are monotone in t and have vanishing normal derivatives ∂ν φ∗ ≡ 0. φ1 and 

φ2 are not to be confused with the barrier functions φδ used in Section 2.12. Since 

ε ∈ (0 , e − max( α1,α 2)), we may have spt( ∇φ∗) ⊂ T ε(α1, α 2). Next, we will define the approximate solution 

u := φ1 ˜u1 + uT + φ2 ˜u2.

Observe that the above claims, along with the choice of φ∗, imply the estimate on 

|| u|| C0   

> γ(M)

in Lemma 2.2.1. Our final task will be to inspect the error term. 60 Since the cut-off functions have vanishing normal derivative, we have 

∂ν u = `1 + `T + `2 = `

and so we have accumulated no error term on the boundary. Moving on the the laplacian of u, it is straight-forward to compute (keeping the support of ∇φ∗ in mind) ∆gε u =∆ gε (φ1 ˜u1) + ∆ gε up + ∆ gε (φ2 ˜u2)=∆ gε (φ1)˜ u1 + gε(∇φ1, ∇˜u1) + φ1f ρ 1 + φ1q1 + φ1b1δι1(K)

+ ∆ gε (φ2)˜ u2 + gε(∇φ2, ∇˜u2) + φ2f ρ 2 + φ2q2 + φ2b2δι2(K)

+ f ρ T − q1 − q2

=f + E1 + E2

where E∗ = (∆ gε φ∗)˜ u∗ + gε(∇φ∗, ∇˜u∗). And so the error in the statement of Lemma 2.2.1 is given by E := E1 + E2.By symmetry, it suffices to estimate the term E1. Observe that E1 is supported in the annular region 

{(z, t, θ ) ∈ T ε(0 , 0) : t ∈ [(1 − B) log ε, (1 − B) log ε + 1] }.

By a careful choice of φ1 and applying the same gradient estimate used above (see [19] and [18]), one can find a constant C10 , independent of ε, such that 

|| E1|| C0  

> γ+2 (M)

≤ C10 εBγ (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1 (∂M )

).

61 This finishes the proof of Lemma 2.2.1 

2.22. The linear problem II 

Lemma 2.2.1 can be refined by solving (2.4) without accumulating the error term 

E.

Lemma 2.2.4. Let γ ∈ (0 , m − 2) . There exists a choice of parameters α1, α 2 > 1,

ε0 > 0, and a constant C > 0 such that the following statement is satisfied for all 

ε ∈ (0 , ε 0). Given f ∈ C 0

> γ+2

(M ) and ` ∈ C 0

> γ+1

(∂M ) satisfying ∫ 

> M

f dμ gε = ∫ 

> ∂M

`dσ gε ,there is a constant λ = λ(f, ` ) ∈ R and a function u ∈ C 0 

> γ

(M ) satisfying 



∆gε u = f in M∂ν u = ` − λβ ε on ∂M 

∫ 

> M

u dμ gε = 0 

with the estimates 

|| u|| C0   

> γ(M)

≤ C(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)

|λ| ≤ C(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)

Moreover, the constant C > 0 depends only on (M1, g 1), (M2, g 2), (K, g K ), γ .Proof. We will iteratively construct sequences 

f (j) ∈ C 0

> γ+2

(M ), `(j) ∈ C 0

> γ+1

(∂M ), u(j) ∈ C 0 

> γ

,λ(j) ∈ R, E(j) ∈ C 0

> γ+2

(M )62 and show they converge in appropriate senses. Setting f (0) := f and `(0) := `, Lemma 2.2.1 supplies a triple u(0) , λ (0) , and E(0) solving 



∆gε u(0) = f (0) + E(0) on M∂ν u(0) = `(0) − λ(0) βε on ∂M 

with estimates. Observe the assumption on f, ` implies that ∫ 

> M

E(0) dμ gε = 0. Next set f (1) := −E(0) , `(1) := 0 and again apply Lemma 2.2.1 to obtain u(1) , λ (1) ,

and E(1) satisfying the appropriate equations and estimates. In general, for j ≥ 1, apply Lemma 2.2.1 with f (j) = −E(j−1) , `(j) = 0, and B ∈ (0 , 1) (to be chosen later) to obtain functions u(j), λ (j), and E(j) upon noting that ∫ 

> M

E(j−1) dμ gε = 0. In other words, for each j ≥ 1, we have 



∆gε u(j) = f (j) + E(j) in M∂ν u(j) = −λ(j)βε on ∂M 

along with a constant C > 0, independent of ε and j, such that 

|| u(j)|| C0   

> γ(M)

≤ C|| f (j)|| C0  

> γ+2 (M)

≤ C(Cε Bγ )j−1(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)

|λ(j)| ≤ C|| f (j)|| C0  

> γ+2 (M)

≤ C(Cε Bγ )j−1(|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)

|| E(j)|| C0  

> γ+2 (M)

≤ Cε Bγ || f (j)|| C0  

> γ+2 (M)

≤ (Cε Bγ )j (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)Now consider the partial sums 

v(N ) := 

> N

∑

> j=0

u(j), μ(N ) := 

> N

∑

> j=0

λ(j)

63 and observe that only one error term remains when computing ∆ gε v(N )



∆gε v(N ) = f + E(N ) in M∂ν v(N ) = ` − μ(N )βε on ∂M. 

Now choose B ∈ (0 , 1) so that Cε Bγ for all ε ∈ (0 , ε 0). One can inspect the above estimates from Lemma 2.2.1 and conclude that the partial sums v(N ), μ(N ) form Cauchy sequences in their respective Banach spaces. In fact, the error term vanishes as we take j → ∞ || E(N )|| C0  

> γ+2 (M)

≤ (Cε Bγ )j (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

) → 0.

This gives us a real number λ and a function u ∈ C 0 

> γ

such that 

E(N ) → 0, v(N ) → u, μ(N ) → λ, 

the convergence being in the appropriate space. As for the estimates of u and λ,observe that 

|| v(N )|| C0  

> γ+2 (M)

≤

> N

∑

> j=0

|| u(j)|| C0 

> γ+2 (M)

≤

> N

∑

> j=0

C(Cε Bγ (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

)

→ C

1 − Cε Bγ (|| f || C0  

> γ+2 (M)

+ || `|| C0 

> γ+1

),

which gives the estimate in Lemma 2.2.4. The desired bound on λ follows from a similar computation. 64 2.3. Returning to the Fixed Point Problem 

The aim of the next two sections is to finish the proofs of Theorems 2.0.7, 2.0.9, and 2.0.9 by producing a function ψ ∈ C∞(M ) which solves the equation (1.6) on (M, g ε) for each ε ∈ (0 , ε 0). Since we are seeking a small conformal change to gε, we will write the conformal factor as ψ = 1 + u. In terms of u, equation (1.6) becomes 



∆gε u = Fε(u) in M∂ν u = F ∂ε (u) on ∂M 

(2.13) where we have introduced the sort-hand notation 

Fε(u) := cnRgε (1 + u)

F ∂ε (u) := 2 cn(Q(1 + u) nn−2 − Hgε (1 + u)) for some constant Q. The convergence statements in Theorems 2.0.7, 2.0.9, and 2.0.11 will follow as consequences of our construction of u. Upon producing a solution u to (2.13), observe that (1 + u) 4 

> n−2

gε will be scalar-flat and have constant boundary mean curvature Q.In what follows, for a given γ ∈ (0 , m − 2), we will restrict our attention to 

u ∈ C 0 

> γ

(M ) which lie in the ball of radius rε := ε2γ about 0 ∈ C 0 

> γ

(M ). We will denote this ball by Bγrε . Let us suppose for a moment that we have in hand a solution 

u ∈ Bγrε to (2.13). Integrating by parts will tell us the mean curvature of the resulting conformal metric 

Q =

> 12

∫ 

> M

Rgε (1 + u)dμ gε + ∫ 

> ∂M

Hgε (1 + u)dσ gε

∫ 

> ∂M

(1 + u) nn−2 dσ gε

.

65 Using the L1 estimates on Rgε and Hgε from Propositions 2.1.1, 2.1.3, and 2.1.6, one finds |Q| = O(εm−2). Before we solve (2.13), we will first use our linear analysis to establish a solution to the following projected version of the problem 



∆gε u = Fε(u) in M∂ν u = F ∂ε (u) − λFε(u)βε on ∂M. 

(2.14) Later, we will arrange for the vanishing of term λFε(u), giving a genuine solution to (2.13). To phrase (2.14) as a fixed point problem, we introduce the following maps 

Fε : C0 

> γ

(M ) → C 0

> γ+2

(M ) × C 0

> γ+1

(∂M ), v 7 → (Fε(v), F ∂ε (v)) 

Gε : C0

> γ+2

(M ) × C 0

> γ+1

(∂M ) → C 0 

> γ

(M ), (v, w ) 7 → Gε(v, w )where Gε(v, w ) is the solution to the boundary problem 



∆gε Gε(v, w ) = v in M∂ν Gε(v, w ) = w − λGε(v,w )βε on ∂M, 

whose existence is given by Lemma 2.2.4. Evidently, solving (2.14) is equivalent to finding a fixed point of the composition 

Pε : C0 

> γ

(M ) → C 0 

> γ

(M ), v 7 → Gε(Fε(v), F ∂ε (v)) for some γ.66 Proposition 2.3.1. Let γ ∈ (0 , 12 ). There is an ε0 > 0 such that Pε(Bγrε ) ⊂ Bγrε for all ε ∈ (0 , ε 0).Proof. As usual, Ck for k = 1 , 2, 3 . . . will denote positive constants independent of 

ε. For v ∈ Bγrε , we may apply Lemma 2.2.4 with the functions Fε(v), F ∂ε (v)) to get a solution, Pε(v), of the linear problem along with the estimate 

|| Pε(v)|| C0   

> γ(M)

≤ C1

(

|| Fε(v)|| C0  

> γ+2 (M)

+ || F ∂ε (v)|| C0 

> γ+1 (∂M )

)

.

It is suffices to dominate || Fε(v)|| C0  

> γ+2 (M)

and || F ∂ε (v)|| C0  

> γ+1 (∂M )

by the product of rε

and some positive power of ε.We begin with the first summand. Applying Propositions 2.1.1, 2.1.3, and 2.1.6 and the definition of ψε,

|Fε(v)ψγ+2  

> ε

| ≤ C2(|Rgε |ψγ+2  

> ε

+ |Rgε | · | v|ψγ+2  

> ε

)

≤ C3(εm−2 + rεεm−2)

≤ C4rεεm−2−2γ .

For the second summand in the estimate, we have 

|F ∂ε (v)|ψγ+1  

> ε

≤ C5(ψγ+1  

> ε

|Q|(1 + v) nn−2 − ψγ+1  

> ε

|Hgε |(1 + v)) 

≤ C6εm−2rε.

Together, we have shown 

|| Pε|| C0   

> γ(M)

≤ C7rεεm−2−2γ ,

67 as claimed. It is a good time to observe a fact we will use later – the proofs in this section hold if |Q| was only O(εm−22 ), so long as we restrict ourselves to γ ∈ (0 , 14 ). Now we are ready to solve (2.14). 

Proposition 2.3.2. Let γ ∈ (0 , 12 ). There exists an ε0 > 0 so that, for each ε ∈

(0 , ε 0), (2.14) has a smooth solution u ∈ Bγrε .Proof. We will proceed by showing that the mapping Pε is contractive on the ball 

Bγrε . In other words, we will show that there is a ε0 > 0 so that 

|| Pε(u) − Pε(v)|| C0   

> γ(M)

≤ K|| u − v|| C0  

> γ(M)

for all ε ∈ (0 , ε 0) and u, v ∈ Bγrε . We begin by applying Lemma 2.2.4t 

|| Pε(u) − Pε(v)|| C0   

> γ(M)

≤ C

(

|| Fε(u) − Fε(v)|| C0  

> γ+2 (M)

+ || F ∂ε (u) − F ∂ε (v)|| C0 

> γ+1 (∂M )

)

,

where C > 0 is independent of ε. By Proposition 2.3.1, all involved terms lie in Bγrε

for small ε.For the first summand, keeping in mind the pointwise estimate on |Rgε | from Propositions 2.1.1, 2.1.3, and 2.1.6, and the restriction on m, we find 

ψγ+2  

> ε

|Fε(u) − Fε(v)| ≤ C8ψγ+2  

> ε

|Rgε (u − v)|≤ C9ε cosh 3−m(t)|| u − v|| C0  

> γ(M)

≤ C9ε|| u − v|| C0  

> γ(M)

.

68 We can perform a similar estimate for the boundary term 

ψγ+1  

> ε

|F ∂ε (u) − F ∂ε (v)| = C10 ε cosh( t)ψγε |Q((1 + u) nn−2 − (1 + v) nn−2 ) − Hgε (u − v)|≤ C11 |Q| · || u − v|| C0   

> γ(∂M )

+ C12 ε cosh( t)|Hgε | · || u − v|| C0  

> γ(∂M )

≤ || u − v|| C0 

> γ

(C13 εm−2 + C14 ε).

Since all the constants Ci are independent of ε, we can find an ε0 > 0 which makes 

Pε a contractive mapping on Bγrε for ε < ε 0.The Banach fixed point theorem applied to Pε on Bγrε gives a fixed point of Pε,which we call uε. Evidently, uε is a solution to equation (2.14), concluding the proof of Proposition 2.3.2. 

2.4. Vanishing of λFε(v)

In the last section we found, for all sufficiently small ε, a solution uε ∈ C 0 

> γ

(M ) to 



∆gε uε = Fε(uε) in M∂ν uε = F ∂ε (uε) − λFε(uε)βε on ∂M. 

The corresponding conformal metric (1 + uε) 4 

> n−2

gε will be scalar flat, but will have boundary mean curvature equal to 

Q − 12cn

(1 + u) −nn−2 λFε(uε)βε

which is non-constant. Next, we will show that ε-small conformal changes can be made to the original metrics g1 and g2 before applying the gluing procedure such that, after 69 applying the above construction and fixed point argument, the new projection term 

λ ˜Fε(uε) will vanish. Fix ˜w1 and ˜w2, two non-zero smooth functions supported on the interiors of 

M1 \ V ε 

> 1

and M2 \ V ε 

> 2

, respectively. For real parameters a∗ (∗ = 1 , 2) which will be chosen later, we consider the functions 

w∗ := a∗εm−22 ˜w∗

and use them to deform the original metrics ˜g∗ := (1 + w∗) 4 

> n−2

g∗.

Replacing g1 and g2 with ˜ g1 and ˜ g2 in the geometric gluing construction presented in Section 2.1, we produce a new family of metrics ˜ gε on the generalized connected sum 

M . Of course, ˜ gε only differs from gε on the supports of w1 and w2. Keeping in mind that sup M |w∗| = O(εn−22 ), all of the analysis we have done on the family of linear operators (∆ gε , ∂ ν ) also holds for the new family (∆ ˜gε , ∂ ν ). Namely, the proof of the a priori estimate in Lemma (2.2.4) also works for the metrics ˜ gε. As usual, we will assume that α1 and α2 have be chosen so that ∫ 

> ∂M

βεdσ ˜gε = 0. Next, we need to gather information about the new scalar curvature and boundary mean curvature. Notice that the support of R˜gε has three disjoint components – T ε(0 , 0) and the supports of w∗. Since R˜gε agrees with Rgε on T ε(0 , 0), we still have the estimate of Propositions 2.1.1, 2.1.3, and 2.1.6 there. On the support of w∗, the formula for scalar curvature under conformal change reads 

R˜gε = R˜g∗ = − 1

cn

(1 + w∗)− n+2  

> n−2

∆g∗ w∗

70 and we conclude that R˜gε = O(εm−22 ) on the supports of w∗. Hence, there is a constant 

C > 0 such that 

|R˜gε | ≤ Cε m−22 ψ1−mε (t).

As for the mean curvature of the boundary, H˜gε does not differ from Hgε since w∗ is supported away from the boundary. Now, upon restricting our choice of γ to the interval (0 , 14 ), we may apply the fixed point argument from Section 2.3 to produce a solution ˜ uε ∈ Bγrε ⊂ C 0 

> γ

(M ) to 



∆˜gε ˜uε = ˜Fε(˜ uε) in M∂ν ˜uε = ˜F ∂ε (˜ uε) − λ ˜Fε(˜ uε)βε on ∂M 

where ˜Fε(u) := cnR˜gε (1 + u) and ˜F ∂ε (u) := 2 cn( ˜Q(1 + u) nn−2 − H˜gε (1 + u)). Once this is achieved, the conformal metric (1 + ˜ uε) 4 

> n−2

˜gε will be scalar flat and have boundary mean curvature equal to 

˜Q − 12cn

(1 + ˜ uε)− nn−2 λ ˜Fε(˜ uε)βε

where the constant ˜Q can be computed by integrating by parts 

˜Q =

> 12

∫ 

> M

R˜gε (1 + ˜ uε)dμ ˜gε + ∫ 

> ∂M

H˜gε (1 + ˜ uε)dσ ˜gε

∫ 

> ∂M

(1 + ˜ uε) nn−2 dσ ˜gε

.

As before, the projection term λ ˜Fε(˜ vε) may be non-zero, though it now (continuously) depends on the parameters a∗. We will exploit this to establish the following proposition, concluding the proof of Theorems 2.0.7, 2.0.9, and 2.0.11. The following 71 properties of the metrics ˜ g∗ will be useful in our computations later this section ∆˜g∗ · = − 12cn

(1 + w∗)− n+2  

> n−2

g∗(∇w∗, ∇· ) + (1 + w∗) −4 

> n−2

∆g∗ ·

dμ ˜gε = (1 + w∗) 2nn−2 dμ gε .

Proposition 2.4.1. For small ε, there is a choice of the real parameters a1 and a2

such that the resulting rough projection λ ˜Fε(˜ uε) vanishes. Proof. It suffices to show that the sign of λ ˜Fε(˜ uε) can be changed by manipulating a1

and a2. From the proof of Lemma 2.2.4, we may regard λ ˜Fε(uε) as the following sum 

λ ˜Fε(uε) =

> ∞

∑

> j=0

λ(j)˜Fε(uε)

where each term has estimate 

|λ(j)˜Fε(˜ vε)| ≤ C(Cε Bγ )j (|| ˜Fε(˜ uε)|| C0   

> γ(M)

+ || ˜F ∂ε (˜ uε)|| C0 

> γ+1 (∂M )

),

where C > 0 is uniform in ε. From this expression we see that the sign of λ ˜Fε(uε), for small ε and an appropriate choice of B, is determined by the first term in the sum. We will need to recall the formula for λ(0) from the proof of Lemma 2.2.4 

λ(0) := 1

∫ 

> ∂M

(ρ1 + ρ2)dσ ˜gε

( ∫

> M

˜Fε(˜ uε)βεdμ ˜gε −

∫

> ∂M

˜F ∂ε (˜ uε)βεdσ ˜gε ++

∫

> M

(∆ ˜gε (ρ1 ˜uT ) − ∆˜gε (ρ2 ˜uT )) dμ ˜gε −

∫

> ∂M

(∂˜ν (ρ1 ˜uT ) − ∂˜ν (ρ2 ˜uT )) dσ ˜gε

)

72 where ˜ uT is the solution to 



∆˜gε ˜uT = ˜Fε( ˜ uε)ρT on T ε(α1, α 2)˜uT ≡ 0 on ∂1T ε(α1, α 2)

∂ν ˜uT = ˜F ∂ε (˜ uε)ρT on ∂2T ε(α1, α 2)which originally appeared in the first step in the proof of Lemma 2.2.4. Next, we will inspect each of the terms in this expression for λ(0) .Unpacking the notations in the first term, we have 

∫

> M

˜Fε(˜ vε)βεdμ ˜gε = cn

∫

> M

(R˜g1 + Rgε + R˜g2 )(1 + ˜ uε)( ρ1 − ρ2)dμ ˜gε .

Recalling that ˜ uε lies in Bγrε ⊂ C 0 

> γ

(M ) and applying the pointwise estimate of Rgε , it is straightforward to show 

∫

> M

Rgε (1 + ˜ uε)ρ∗dμ ˜gε = −4mVol( K)ωm−1 + O(e−α∗ εm−2)and ∫

> M

R˜g∗ ρ∗dμ ˜gε = 1

cn

∫

> M∗

|∇ w∗|2 

> g∗

dμ g∗

where ωm−1 denotes the volume of the unit ( m − 1)-sphere. After integrating by parts, the remaining piece of the first term can be written as ∫

> M

R˜g∗ ˜uεdμ ˜gε =

∫

> M∗

w∗∆g∗ ˜uεdμ g∗ +

∫

> ∂M ∗

w∗∂ν ˜uεdσ g∗ + O(εm−2+ γ ).

73 Now we Taylor expand and rearrange the above expression for ∆ ˜g∗ and ∂˜ν

∆g∗ ˜uε =

(

1 + 4

n − 2w∗ + O(εm−2)

)

∆˜g∗ ˜uε − 2g∗(∇w∗, ∇˜uε)+ + 2 w∗g∗(∇w∗, ∇˜uε) + O(εm−2+2 γ )

∂ν ˜uε =

(

1 + 2

n − 2w∗ + O(εm−2)

)

∂˜ν ˜uε

and multiply by w∗ to find 

∫

> M

R˜g∗ ˜uεdμ ˜gε =

∫

> M∗

w∗ ˜Fε(˜ uε)dμ g∗ +

∫

> ∂M

w∗( ˜F ∂ε (˜ uε) − λ ˜Fε(˜ uε)βε)dσ gε + O(εm−2+ γ )=

∫

> M

|∇ w∗|2 

> g∗

dμ g∗ − λ ˜Fε(˜ uε)O(εm−22 ) + O(εm−2+ γ )where we have used the formula for R˜gε in the expression for ˜Fε(˜ uε) and integrated by parts. To summarize our efforts so far, we have found 

∫

> M

˜Fε(˜ vε)βεdμ ˜gε = ( cn − 1) 

(∫ 

> M1

|∇ w1|2 

> g1

dμ g1 −

∫

> M2

|∇ w2|2 

> g2

dμ g2

)

− λ ˜Fε(˜ uε)O(εm−22 )+ + O(e− max( α1,α 2)εm−2). (2.15) Moving along to the next term in the expression for λ(0) , we have 

∫

> ∂M

˜F ∂ε (˜ uε)βεdσ ˜gε = 2 cn

∫

> ∂M

( ˜Q(1 + ˜ uε) nn−2 − H˜gε (1 + ˜ uε))( ρ1 − ρ2)dσ ˜gε .

Now since H˜gε ≡ Hgε , we have 

∫

> ∂M

H˜gε (1 + ˜ uε)ρ∗dσ ˜gε = O(e−α∗ εm−2)74 which can be seen by computing Hgε on this portion of the neck, noting that the cut off functions ξ and η both take the value of 1 on the support of ρ1.Now is a good time to comment on the convergence statements in the main theorems. As we have mentioned already, we may apply the pointwise estimate of 

R˜gε and the C0 

> γ

-norm of ˜ vε to find that ˜Q satisfies the estimate 

| ˜Q| = O(εm−22 ).

Evidently, ˜Fε(˜ uε) = O(εm−22 ) on the support of w∗ and λ ˜Fε(˜ uε) = O(ε(m−2) /2). Using the computations made in this section, one can inspect the formula for ˜Q and improve our estimate to | ˜Q| = O(εm−2), as claimed in Theorems 2.0.7. 2.0.9. and 2.0.11. This can be used to estimate the remaining term in the expression for ∫ 

> ∂M

˜Fε(˜ uε)βεdσ ˜gε

and conclude ∫

> ∂M

˜F ∂ε (˜ vε)βεdσ ˜gε = O(e− max( α1,α 2)εm−2). (2.16) The final two integrals in the expression for λ(0) will be treated together. Integrating by parts, we have 

∫

> M

∆gε (ρ∗ ˜uT )dμ ˜gε −

∫

> ∂M

∂ν (ρ∗ ˜uT )dσ ˜gε =

∫

> M

(ρ∗∆gε ˜uT + 2( gε(∇ρ∗, ∇˜uT ) + ˜ uT ∆gε ρ∗)−

˜uT ∆gε ρ∗)dμ gε −

∫

> ∂M

ρ∗∂ν ˜uT dσ gε

=

∫

> M

ρ∗ρT ˜Fε(˜ uε) − ˜uT ∆gε ρ∗dμ gε −

∫

> ∂M

ρ∗ρT ˜F ∂ε (˜ uε)dσ gε

75 where we have used the fact that ∂ν ρ∗ ≡ 0. In order to proceed, we will need the pointwise estimate of Propositions 2.1.2, 2.1.5, and 2.1.7: ˜uT ≤ Cψ γε

(

|| ˜Fε(˜ uε)|| C0  

> γ+2 (Tε(α1,α 2))

+ || ˜F ∂ε (˜ uε)|| C0 

> γ+1 (∂2Tε(α1,α 2))

)

≤ C′εm−2ψγε

for C, C ′ > 0 independent of ε. Keeping in mind that ρ∗ρT and ∆ ˜gε (ρ∗) vanish outside of T ε(α1, −2 log ε − α1 − 1) if ∗ = 1 and T ε(−2 log ε − α2 − 1, α 2) if ∗ = 2, one can use the pointwise estimate on ˜ uT to find 

∫

> M

∆gε (ρ∗ ˜uT )dμ ˜gε −

∫

> ∂M

∂ν (ρ∗ ˜uT )dσ ˜gε = O(e−α∗ εm−2).

Combining the above estimates, we have 

λ(0) =( cn − 1) 

(∫ 

> M1

|∇ w1|2 

> g1

dμ g1 −

∫

> M2

|∇ w2|2 

> g2

dμ g2

)

−

λ(0) O(εm−22 ) + O(e− max( α1,α 2)εm−2).

Since ||∇ w∗|| L2 = a∗O(εm−2), we can choose α1, α 2 so that the term ||∇ w1|| L2 −||∇ w2|| L2 dominates the rest of the expression for λ(0) . Evidently, one can vary the parameters a1 and a2 so that the sign of λ(0) – and hence the sign of λ ˜Fε(˜ vε) – changes. As we previously noted, λ ˜Fε(˜ vε) depends continuously on a1 and a2, so we conclude that there are suitable values of a1 and a2 for which the projection term λ ˜Fε(˜ vε) vanishes. This finishes the proof of Theorems 2.0.7, 2.0.9, and 2.0.11. 76 2.5. The Non-critical Case 

So far, we have produced a family of metrics (1 + ˜ uε) 4 

> n−2

˜gε on M , each scalar-flat and having constant boundary mean curvature of size O(εm−2). In this section we will prove Theorems 2.0.8, 2.0.10, and 2.0.12, where we arrange for this mean curvature to vanish entirely. To achieve this, we will need yet another alteration to the above construction. From now on, we assume that neither of the original manifolds are Ricci-flat with totally geodesic boundary , i.e. we assume that max(sup 

> M∗

|ric g∗ |, sup 

> ∂M ∗

|Ag∗ |) > 0for both ∗ = 1 and 2. Let S∗ be a positive-definite symmetric 2-tensor with spt( S∗) ⊂ ((M∗ \ ι1

> ∗

) ∩ (spt(Ric g∗ ) ∪ spt( Ag∗ )) ) .

For a real parameter ˜ r∗, set r∗ := ˜ r∗εm−2 and consider the following variation of gε

˜gε := gε + r1S1 + r2S2, ˜g∗ := g∗ + r∗S∗.

We apply the constructions of the previous two section to ˜ gε in order to produce a family of solutions, v = vε(r1, r 2) ∈ Bγrε to 



∆˜gε v = ˜Fε(v, r 1, r 2) in M∂ν v = ˜F ∂ε (v, r 1, r 2) − λ ˜Fε(v,r 1,r 2)βε on ∂M 

77 where ˜Fε(v, r 1, r 2) := cnR˜gε (1 + v)is defined as usual, but ˜F ∂ε (v, r 1, r 2) := −2cnH˜gε (1 + v)has been altered so that, supposing we can arrange for λ ˜Fε(v,r 1,r 2) = 0, the boundary mean curvature of (1 + v) 4 

> n−2

˜gε is exactly 0. As before, we will assume that 

∫ 

> ∂M

βεdσ ˜gε = 0, which can be achieved for any r1 and r2 by an appropriate choice of 

α1 and α2.Notice that our choice of r∗ ensures R˜gε satisfies the same pointwise bounds as in the previous sections. This will allow us to apply the results of Section 2.3 with trivial modifications once we verify 

∫

> M

˜Fε(v, r 1, r 2)dμ ˜gε =

∫

> ∂M

˜F ∂ε (v, r 1, r 2)dσ ˜gε . (2.17) The second and final step is to arrange for the vanishing of λ ˜Fε(v,r 1,r 2).Let us take a moment to explain why simultaneous vanishing of the Ricci tensor and second fundamental form can potentially be an obstruction to achieving the conclusions of Theorems 2.0.8, 2.0.10, and 2.0.12. Briefly, ( M, g ε) may be in the same conformal class as an Einstein metric with Neumann boundary conditions in the sense of [21] and the total scalar curvature plus mean curvature functional Q(gε)may stable under even non-conformal perturbations. For the metric ˜ gε, we can follow 78 the calculations of [5] to compute 

Q(˜ gε) = Q(gε) + 2 cn

> 2

∑

> ∗=1

r∗

(∫ 

> M

g∗(S∗, Ric g∗ )dμ g∗ −

∫

> ∂M

g∗(S∗, A g∗ )dσ g∗

)

+

O(r21 ) + O(r22 )= Q(gε) + 2 cn

> 2

∑

> ∗=1

r∗

(∫ 

> M

K∗dμ g∗ −

∫

> ∂M

K∂ 

> ∗

dσ g∗

)

+ O(ε2( m−2) )where we have introduced the notation K∗ := g∗(S∗, Ric g∗ ) and K∂ 

> ∗

:= g∗(S∗, A g∗ ). From this formula, we can see that if both Ric g∗ and Ag∗ vanish identically for 

∗ = 1 and 2, the first variation of Q(gε) vanishes for all choices of S∗ and we will be unable to correct the term F (gε) with a small (relative to ε) perturbation of gε

away from the gluing locus to achieve the desired vanishing mean curvature. This reasoning heuristically explains why our construction may fail to produce scalar-flat metrics with vanishing boundary mean curvature on M without assumptions on the Ricci tensor and second fundamental form. 

2.51. Achieving the orthogonality condition 

In this subsection, we will give a description of the values r1 and r2 for which (2.17) is satisfied. 

Proposition 6. For small ε and v ∈ Bγrε , there is a smooth function fv defined on a neighborhood U of εm−2 

> 2

such that 

∫

> M

˜Fε(v, r 1, f v(r1)) dμ ˜gε =

∫

> ∂M

˜F ∂ε (v, r 1, f v(r1)) dσ ˜gε

for all r1 ∈ U .79 Proof. For any v ∈ Bγrε ⊂ C 0 

> γ

(M ), we introduce the function 

Gv,ε (r1, r 2) := 1

cn

( ∫

> M

˜Fε(v, r 1, r 2)dμ ˜gε −

∫

> ∂M

˜F ∂ε (v, r 1, r 2)dσ ˜gε

)

=

∫

> M

Rgε dμ gε + 2 

∫

> ∂M

Hgε dσ gε + ∑

> ∗=1 ,2

r∗

(∫ 

> M1

K∗dμ g∗ −

∫

> ∂M ∗

K∂ 

> ∗

dσ g∗

)

+ Lv(r1, r 2) + Qv(r1, r 2)where we have introduced the notation 

Lv(r1, r 2) := 

∫

> M

vR gε dμ gε + ∑

> ∗=1 ,2

r∗

(∫ 

> M∗

vK ∗dμ g∗ −

∫

> ∂M ∗

vK ∂ 

> ∗

dσ g∗

)

− 2

∫

> ∂M ∗

vH gε dσ gε

Qv(r1, r 2) := ∑

> ∗=1 ,2

∫

> M∗

R˜g∗ (1 + v)dμ g∗ − 2

∫

> ∂M ∗

H˜gε (1 + v)

− r∗

∫

> M∗

K∗(1 + v)dμ g∗ + r∗

∫

> ∂M ∗

K∂ 

> ∗

(1 + v)dσ g∗ + O(ε2( m−2) ).Lv and Qv can be interpreted as the linear and quadratic parts, respectively, of Gv,ε .We also introduce the function Hε(r1, r 2) := Gv,ε (r1, r 2) − Lv(r1, r 2) − Qv(r2, r 2). For simplicity, we will pick S∗ to satisfying the following conditions. We assume that S∗ has been chosen so that ∫ 

> M

K∗dμ g∗ − ∫ 

> ∂M ∗

K∂ 

> ∗

dσ g∗ = 1 and we will only consider the case when 

∫

> M

Rgε dμ gε + 2 

∫

> ∂M

Hgε dσ gε < 0,

though the argument is very similar if this quantity is positive. Since this term is 

O(εm−2), we will scale the metric gε so that it is equal to −εm−2. Now Hε takes the form 

Hε(r1, r 2) = −εm−2 + r1 + r2

80 and the vanishing locus of Hε(r1, r 2) is given by {(r1, r 2) : r1 + r2 = εm−2}. We will see that the zero set of Gv,ε (r1, r 2) is uniformly close to this set. It is straight forward to check that there is a constant C > 0, independent of ε

and v ∈ Bγrε , such that 

Lv(r1, r 2), Q v(r1, r 2) ≤ C1εm−2+ γ .

So, for any η > 0, there is sufficiently small ε so that 

|Lv(r1, r 2)|, |Qv(r1, r 2)| ≤ η

2 εm−2.

It follows that 

{Gv,ε (r1, r 2) = 0 } = {(r1, r 2) : r1 + r2 = εm−2 − Lv(r1, r 2) − Qv(r1, r 2)}⊂ { (r1, r 2) : (1 − η)εm−2 ≤ r1 + r2 ≤ (1 + η)εm−2} =: Zε.

From these remarks, we can find many zeroes of Gv,ε . For instance, setting r′ 

> 1

:= 

εm−2/2, for any v ∈ Bγrε , there is a number r′ 

> 2

= r′

> 2

(v) with ( r′

> 1

, r ′

> 2

(v)) ∈ Zε and 

Gv,ε (r′

> 1

, r ′

> 2

(v)) = 0. However, we will still need a degree of freedom to arrange for 

λ ˜Fε = 0 in the next subsection. Fortunately, for each v ∈ Bγrε we will find a 1-parameter family of solutions near ( r′

> 1

, r ′

> 2

) by applying the implicit function theorem to Gv,ε .81 Computing the derivatives of Gε,v ,

∣∣∣∣

∂∂r ∗

Gε,v (0 , 0) 

∣∣∣∣ =

∣∣∣∣∫

> M∗

K∗(1 + v)dμ g∗ −

∫

> ∂M ∗

K∂ 

> ∗

(1 + v)dσ g∗

∣∣∣∣

≥

∣∣∣∣∫

> M∗

K∗dμ g∗ −

∫

> ∂M ∗

K∂ 

> ∗

dσ g∗

∣∣∣∣

− || v|| C0(M )

(∫ 

> M∗

|K∗|dμ g∗ +

∫

> ∂M ∗

|K∂ 

> ∗

|dσ g∗

)

≥ 12for ∗ = 1 , 2 and all v ∈ Bγrε . From this we can find a radius R > 0, uniform in ε and 

v ∈ Bγrε , so that that 

∣∣∣ ∂∂r ∗ Gv,ε 

∣∣∣ ≥ 14 on BR(0) ⊂ R2.

r1

r2

RR

{Hε(r1, r 2) = 0 }

fv

r′ 

> 1

εm−2

Zε

FIGURE 2.5. The region Zε and the function fv in the r1r2-plane. After perhaps restricting to smaller ε, the set Zε ∩ { r1, r 2 ≥ 0} is contained in 

BR(0). We may now apply the implicit function theorem on Gv,ε about the points (r′

> 1

, r ′

> 2

(v)) to obtain, for every v ∈ Bγrε , open neighborhoods U (v) and V (v) containing 

r′ 

> 1

and r′

> 2

(v), respectively, and a function fv : U (v) → V (v) so that Gv,ε (r1, f v(r1)) = 0 82 for all r ∈ U (v) (see Figure 2.5.). In fact, we know apriori that fv can be extended to the interval (0 , (1 − η)εm−2), and so we may choose open sets U and V which are independent of v ∈ Bγrε . Since the graph of each fv lies in Zε they may be extended to fv : U → V .Before we continue, we will need one more property of the family {fv}v∈Bγrε . By construction, we have 

fv(r1) = 

∫

> M

Rgε dμ gε + 2 

∫

> ∂M

Hgε (1 + v)dσ gε − r1 + Lv(r1, f v(r1)) + Qv(r1, r 2).

From this one can see, for small ε and any r1, r ′ 

> 1

∈ U , that 

|fv(r1) − fv(r′

> 1

)| ≤ 4|r1 − r′

> 1

|.

Now Ascoli-Arzela tells us that {fv}v∈Bγrε is precompact in the C0(U ) norm. This function f will have the same Lipschitz norm bound. 

2.52. Vanishing of the rough projection 

Paralleling Section 2.3, we introduce the map ˜Pε : C0 

> γ

(M ) → C 0 

> γ

(M ) sending a function v to the solution of 



∆˜gε ˜Pε(v) = ˜Fε(v, r ′

> 1

, f v(r′

> 1

)) in M∂ν ˜Pε(v) = ˜F ∂ε (v, r ′

> 1

, f v(r′

> 1

)) − λ ˜Fε(v,r ′ 

> 1,f v(r′
> 1))

βε on ∂M 

The arguments of that section can be repeated to show ˜Pε is also a contraction mapping on Bγrε for small ε and γ ∈ (0 , 14 ). This shows that {( ˜Pε)j (0) }∞ 

> j=1

converges to a fixed point ˜ vε ∈ Bγrε with respect to the C0 

> γ

-norm. From the previous section, 83 after passing to a subsequence, the functions f( ˜Pε)j (0) also converge to a continuous function f : U → V which verifies the orthogonality condition for ˜ vε. We conclude that, for any r1 ∈ U , we have 



∆˜gε ˜vε = ˜Fε(˜ vε, r 1, f (r1)) in M∂ν ˜vε = ˜F ∂ε (˜ vε, r 1, f (r1)) − λ ˜Fε(˜ vε,r 1,f (r1)) βε on ∂M. 

(2.18) The following proposition will complete the proof of Theorems 2.0.8, 2.0.10, and 2.0.12. 

Proposition 7. There exists an ε0 > 0 so that for all ε ∈ (0 , ε 0) there is a choice of 

r1 ∈ U for which λ ˜Fε(˜ vε,r 1,f (r1)) vanishes where ˜ vε is given by (2.18). 

Proof. Since λ ˜Fε(˜ vε,r 1,f (r1)) is continuous in r1, it suffices to show that its sign can be controlled by r1 ∈ U . Following Section 2.5, for small ε, the sign of λ ˜Fε(˜ vε,r 1,f (r1)) is controlled by the sign of 

λ(0) = 1

∫ 

> ∂M

(ρ1 + ρ2)dσ ˜gε

( ∫

> M

˜Fε(˜ vε, r 1, f (r1)) βεdμ ˜gε

−

∫

> ∂M

˜F ∂ε (˜ vε, r 1, f (r1)) βεdσ ˜gε +

∫

> M

(∆ ˜gε (ρ1 ˜uT )

− ∆˜gε (ρ2 ˜uT )) d˜gε −

∫

> ∂M

∂ν (ρ1 ˜uT ) − ∂ν (ρ2 ˜UT )dσ ˜gε

)

.

As before, we have 

∫

> M

∆˜gε (ρ∗ ˜uεp)dμ ˜gε +

∫

> ∂M

∂ν (ρ∗ ˜uT )dσ ˜gε = O(e−α∗ εm−2)84 for ∗ = 1 , 2. For the first term appearing in the above expression for λ(0) , we have 1

cn

∫

> M

˜Fε(˜ vε, r 1, f (r1)) dμ ˜gε = r1

∫

> M1

K1dμ g1 − f (r1)

∫

> M2

K2dμ g2

+

∫

> M

Rgε βεdvol gε + O(εm−2+2 γ )= r1

∫

> M1

K1dμ g1 − f (r1)

∫

> M2

K2dμ g2 + O(e− min( α1,α 2)εm−2)The boundary term has a similar estimate 1

cn

∫

> ∂M

˜F ∂ε (˜ vε, r 1, f (r1)) βεdσ ˜gε = − r1

∫

> ∂M 1

K∂ 

> 1

dσ g1 + f (r1)

∫

> ∂M 2

K∂ 

> 2

dσ g2

+ O(e− min( α1,α 2)εm−2).

Summing these three expressions together gives us the expression we are looking for 

λ(0) = r1 − f (r1) + O(e− max( α1,α 2)εm−2).

Hence, we can choose large α1 and α2 so that the sign of λ ˜Fε(˜ vε,r 1,f (r1)) is controlled by r1 − f (r1). Evidently, the graph of f must intersect the line {r1 = r2} in Zε (see Figure 2.5.) and we conclude that the sign of r1 − f (r1) changes as r1 varies over U ,finishing the proof of Proposition 2.52. 85 CHAPTER III PART II: MINIMAL HYPERSURFACES WITH FREE BOUNDARY AND PSC-BORDISM This chapter contains material which appears in a preprint written by the present author and Boris Botvinnik. The present author and Boris Botvinnik worked collaboratively on the content and exposition of all sections in this chapter. 

3.1. Preliminaries and Theorem 1.5.3 

In this section, we will prove Theorem 1.5.3. Before we begin, let us prepare by recalling the notion of stable minimality and the impact of the non-trivial boundary of M .

3.11. Stable minimal hypersurfaces with free boundary 

Let ( M, ¯g) be a compact oriented ( n + 1)-dimensional Riemannian manifold with nonempty boundary ∂M . Assume W ⊂ M is a properly embedded hypersurface. Let ¯h denote the restriction metric ¯h = ¯ g|W and fix a unit normal vector field 

νW on W which is compatible with the orientation. This determines the second fundamental form AW on W given by the formula AW 

> ¯g

(X, Y ) = ¯ g(∇X Y, ν W ) for vector fields X and Y tangential to W . The trace of AW 

> ¯g

with respect to the metric ¯h gives the mean curvature HW 

> ¯g

= tr ¯hAW 

> ¯g

. We will often omit the sub- and super-scripts, writing ν, A, and H if there is no risk of ambiguity. 

Definition 3.1.1. Let W ⊂ M be a properly embedded hypersurface. A variation 

of the hypersurface W ⊂ M is a smooth one-parameter family {Ft}t∈(−ε,ε ) of proper embeddings Ft : W → M , t ∈ (−ε, ε ) such that F0 coincides with the inclusion 86 W ⊂ M . A variation {Ft}t∈(−ε,ε ) is said to be normal if the curve t 7 → Ft(x) meets 

W orthogonally for each x ∈ W .The vector field X = ddt Ft|t=0 is called the variational vector field associated to 

{Ft}t∈(−ε,ε ). For normal variations, the associated variational vector field takes the form φ · νW for some function φ ∈ C∞(W ). Clearly, a variation {Ft}t∈(−ε,ε ) gives a smooth function t 7 → Vol( Ft(W )). 

Definition 3.1.2. A properly embedded hypersurface W ⊂ (M, ¯g) is minimal with free boundary if  

> ddt

Vol( Ft(W )) ∣∣t=0 = 0 for all variations {Ft}t∈(−ε,ε ).More notation: we denote by dσ and dμ the volume forms of ( W, ¯h) and ( ∂W, h ), where h = ¯h|∂W is the induced metric. We denote the outward-pointing unit length normal to ∂M by ν∂ . Below, Lemmas 3.1.1 and 3.1.2 contain well-known formulas, see [22]. 

Lemma 3.1.1. Let (M, ¯g) be an oriented Riemannian manifold and let W ⊂ M be a properly embedded hypersurface. If {Ft}t∈(−ε,ε ) is a variation of W with variational vector field X, then 

ddt Vol( Ft(W )) 

∣∣∣∣t=0 

= −

∫

> W

HW ¯g(X, ν W )dμ +

∫

> ∂W

¯g(X, ν ∂M )dσ. (3.1) 

In particular, a hypersurface W is minimal with free boundary if and only if HW 

> ¯g

≡ 0

and W meets the boundary ∂M orthogonally. 

87 Definition 3.1.3. A properly embedded minimal hypersurface with free boundary 

W is stable if  

> d2
> dt 2

Vol( Ft(W )) 

∣∣∣t=0 

≥ 0for all variations {Ft}t∈(−ε,ε ).If a hypersurface W is minimal with free boundary, then any variational vector field must be parallel to νW on ∂W since the variation must go through proper embeddings. Hence, it is enough to consider only normal variations to analyze the second variation of the volume functional. 

Lemma 3.1.2. Let (M, ¯g) be an oriented Riemannian manifold and let W ⊂ M be a properly embedded minimal hypersurface with free boundary. Let {Ft}t∈(−ε,ε ) be a normal variation with variational vector field φ · νW . Then 

d2

dt 2 Vol( Ft(W )) |t=0 =

∫

> W

(|∇ φ|2 − φ2(Ric ¯g(νW , ν W ) + |AW |2)) dμ 

−

∫

> ∂W

φ2A∂M (νW , ν W )dσ, (3.2) 

where Ric ¯g denotes the Ricci tensor of (M, ¯g).

It will be useful to rewrite equation (3.2). The Gauss-Codazzi equations for a minimal hypersurface W ⊂ M imply 

RM 

> ¯g

= RW 

> ¯h

+ 2Ric ¯g(νW , ν W ) + |AW |2

on W . Here RM 

> ¯g

and RW 

> ¯h

are the scalar curvatures of ( M, ¯g) and ( W, ¯h), respectively. It follows that the inequality d2 

> dt 2

Vol( Ft(W )) 

∣∣∣t=0 

≥ 0 is equivalent to 

∫

> W

|∇ φ|2dμ ≥

∫

> W

12φ2 (RM 

> ¯g

− RW 

> ¯h

+ |AW |2) dμ −

∫

> ∂W

φ2A∂M (νW , ν W )dσ. (3.3) 88 3.12. Conformal Laplacian with minimal boundary conditions 

The proof of Theorem 1.5.3 will rely on some basic facts about the conformal Laplacian on manifolds with boundary. Let ( W, ¯h) be an n-dimensional manifold with non-empty boundary ( ∂W, h ) where h = ¯h|∂W . We consider the following pair of operators acting on C∞(W ): 



L¯h = −∆¯h + cnRW 

> ¯h

in WB¯h = ∂ν + 2 cnH∂W  

> ¯h

on ∂W , 

where ν is the outward pointing normal vector to ∂W and cn = n−24( n−1) .Recall that if φ ∈ C∞(W ) is a positive function, then the scalar and boundary mean curvatures of the conformal metric ˜h = φ 4 

> n−2

¯h are given by 



R˜h = c−1 

> n

φ− n+2  

> n−2

· L¯hφ in WH˜h = 12 c−1 

> n

φ− nn−2 · B¯hφ on ∂W . 

(3.4) We consider a relevant Rayleigh quotient and take the infimum: 

λ1 = inf   

> φ6≡0∈H1(W)

∫

> W

(|∇ φ|2 + cnRW 

> ¯h

φ2) dμ + 2 cn

∫ 

> ∂W

H∂W  

> ¯h

φ2dσ 

∫ 

> W

φ2dμ . (3.5) According to standard elliptic PDE theory, we obtain an elliptic boundary problem, denoted by ( L¯h, B ¯h), and the infimum λ1 = λ1(L¯h, B ¯h) is the principal eigenvalue of the minimal boundary problem (L¯h, B ¯h). The corresponding Euler-Lagrange equations are the following: 

L¯hφ = λ1φ in WB¯hφ = 0 on ∂W. 

(3.6) 89 This problem was first studied by Escobar [6] in the context of the Yamabe problem on manifolds with boundary. Let φ be a solution of (3.6). It is well-known that the eigenfunction φ is smooth and can be chosen to be positive. A straight-forward computation shows that the conformal metric ˜h = φ 4 

> n−2

¯h has the following scalar and mean curvatures: 



R˜h = λ1φ− 4 

> n−2
> 1

in WH˜h ≡ 0 on ∂W . 

(3.7) In particular, the sign of the eigenvalue λ1 is a conformal invariant, see [6, 9]. 

3.13. Proof of Theorem 1.5.3 

Let ( M, ¯g) and W ⊂ M be as in Theorem 1.5.3. From the assumption H∂M ≡ 0, one can use the Gauss equations to show that A∂M (ν, ν ) = −H∂W where H∂W is the mean curvature of ∂W as a hypersurface of W . Now, using the condition RM 

> ¯g

> 0, the stability inequality (3.3) implies 

∫

> W

(

|∇ φ|2 + 12RW

> ¯h

)

dμ +

∫

> ∂W

φ2H∂W dσ ≥ 0 (3.8) for all functions φ ∈ H1(W ) with strict inequality if φ 6 ≡ 0. By simple manipulation, the inequality (3.8) may be written as 

∫

> W

(|∇ φ|2 + cnRW

> ¯h

) dμ + 2 cn

∫

> ∂W

φ2H∂W dσ > (1 − 2cn)

∫

> W

|∇ φ|2dμ (3.9) for all φ 6 ≡ 0 ∈ H1(W ). The right hand side of (3.9) is non-negative since 1 − 2cn = 

> n
> 2( n−1)

> 0. Furthermore, the left hand side of (3.9) coincides with the numerator of the Rayleigh quotient in equation (3.5). We conclude that the principal eigenvalue 90 λ1 = λ1(L¯h, B ¯h) is positive. Let φ be an eigenfunction corresponding to λ1. Then, according to (3.7), the metric ˜h = φ 4 

> n−2

¯h has positive scalar curvature and zero mean curvature on the boundary. This completes the proof of Theorem 1.5.3. 

3.2. Cheeger-Gromov Convergence of Minimizing Hypersurfaces 

Here we introduce the notion of smooth convergence of hypersurfaces we require for the proof of Theorem 1.5.6. First, we consider the case when the hypersurfaces are embedded in the same ambient ( n + 1)-dimensional manifold M . Below we use coordinate charts Φ j : Uj → M , where Uj is an open subset of Rn+1 + =

{(x1, . . . , x n+1 ) ∈ Rn+1 : xn+1 ≥ 0}. 

> Pxηx+u(x)ηU

FIGURE 3.1. The hypersurface graph( u)Let P ⊂ Rn+1 be a hyperplane equipped with a normal unit vector η, and 

U ⊂ Rn+1 + be an open subset. Then for a function u : P ∩ U → R, we denote by graph( u) its graph , see Fig. 3.1.: graph( u) = {x + u(x)η | x ∈ P ∩ U }.

Definition 3.2.1. Let k ≥ 1 be an integer. Let ( M, ¯g) be an ( n + 1)-dimensional compact Riemannian manifold and let {Σi}∞ 

> i=1

be a sequence of smooth, properly 91 embedded hypersurfaces. Then we say that the sequence {Σi}∞ 

> i=1

converges to a smooth embedded hypersurface Σ ∞ Ck-locally as graphs if there exist (i) coordinate charts Φ j : Uj → M for j = 1 , . . . , N ;(ii) hyperplanes Pj ⊂ Rn+1 equipped with unit normal vectors ηj for j = 1 , . . . , N ;(iii) smooth functions ui,j : Pj ∩ Uj → R for j = 1 , . . . , N , i = 1 , 2, . . . , and i = ∞,which satisfy the following conditions: (a) 

> N

⋃

> j=1

Φj (graph( ui,j ) ∩ Uj ) = Σ i for i = 1 , 2, . . . and i = ∞;(b) for each j = 1 , . . . , N , ui,j → u∞,j in the Ck(Pj ∩ Uj ) topology as i → ∞ .We say the sequence {Σi}∞ 

> i=1

converges to a smooth embedded hypersurface Σ ∞

smoothly locally as graphs if it converges Ck-locally as graphs for all k = 1 , 2, . . . .Next, we consider a sequence {(Mi, Σi, ¯gi, Si)}∞

> i=1

, where ( Mi, ¯gi) is a Riemannian manifold, Σ i ⊂ Mi is a properly embedded smooth hypersurface, and Si ⊂ Mi acompact subset, playing a role of a base-point or a finite collection of base points. 

Definition 3.2.2. Let k ≥ 1 be an integer, and {(Mi, Σi, ¯gi, Si)}∞ 

> i=1

be a sequence as above, where dim Mi = n + 1. We say that {(Mi, Σi, ¯gi, Si)}∞ 

> i=1

Ck-converges to (M∞, Σ∞, ¯g∞, S∞) if there is an exhaustion of M∞ by precompact open sets 

S∞ ⊂ U1 ⊂ U2 ⊂ · · · ⊂ M∞, M∞ =

> ∞

⋃

> i=1

Ui

and maps Ψ i : Ui → Mi which are diffeomorphisms onto their images for each i =1, 2, . . . , such that (1) dist M∞ 

> H

(S∞, Ψ−1 

> i

(Si)) → 0 as i → ∞ , where dist M∞ 

> H

is the Hausdorff distance for subsets of the manifold M∞;92 (2) the sequence {Ψ∗ 

> i

¯gi} converges to ¯ g∞ in the Ck(Ui)-topology as i → ∞ ;(3) the sequence of hypersurfaces {Ψ−1 

> j

(Σ i)}∞ 

> i=1

converges Ck-locally as graphs in the manifold M∞ to Σ ∞ ∩ Uj as i → ∞ for each j = 1 , . . . , N .

Remark 3.2.1. We notice that the conditions (1) and (2) imply that the sequence 

{(Mi, ¯gi, Si)}∞ 

> i=1

Ck-converges to ( M∞, ¯g∞, S∞) in the Cheeger-Gromov topology. We say that {(Mi, Σi, ¯gi, Si)}∞ 

> i=1

smoothly converges to ( M∞, Σ∞, ¯g∞, S∞) if it 

Ck-converges for all k ≥ 1. Then we say that {(Mi, Σi, ¯gi, Si)}∞ 

> i=1

sub-converges to (M∞, Σ∞, ¯g∞, S∞) if it has a subsequence which converges to ( M∞, Σ∞, ¯g∞, S∞). In this case we write (Mi, Σi, ¯gi, Si) −→ (M∞, Σ∞, ¯g∞, S∞).

3.21. Main convergence result 

We are ready to set the stage for the main result of this section. Let ( Y, g ) be a closed, oriented n-dimensional Riemannian manifold with a homology class α ∈

Hn−1(Y ; Z). As we discussed in Section 1.5, the class α gives the Poincar` e dual class 

Dα = [ γ] ∈ H1(Y ; Z) represented by some map γ : Y → S1. Furthermore, we assume that there is a bordism (M, ¯g, ¯γ) : ( Y, g, γ ) (Y ′, g ′, γ ′) (3.10) for some triple ( Y ′, g ′, γ ′). In the above, ¯ γ : M → S1 represents a class [¯ γ] ∈ H1(M ; Z)Poincar` e dual to a class ¯ α ∈ Hn(M, ∂M ; Z). 93 Recall that Y ⊂ ∂M and ¯ g = g + dt 2 near Y . For a real number L ≥ 0, we consider the following Riemannian manifold (ML, ¯gL) := ( M ∪Y ×{− L} (Y × [−L, 0]) , ¯gL),

where ¯ gL restricts to ¯ g on M and to the product-metric g + dt 2 on Y × [−L, 0]. We obtain another bordism (ML, ¯gL, ¯γL) : ( Y, g, γ ) (Y ′, g ′, γ ′), (3.11) where [¯ γL] is the image of [¯ γ] under the isomorphism H1(M ; Z) ∼= H1(ML; Z). We refer to the bordism ( ML, ¯gL, ¯γL) as the L-collaring of (M, ¯g, ¯γ). Below we will take 

L be an integer i = 1 , 2, . . . , and write ¯ αL ∈ Hn(M, ∂M ; Z) for the class Poincar` edual to [¯ γL]. 

Main Lemma. Let ( M, ¯g, ¯γ) : ( Y, g, γ ) (Y ′, g ′, γ ′) be a bordism as in (3.10) and denote by ( Mi, ¯gi, ¯γi) the i-collaring of ( M, ¯g, ¯γ) as in (3.11) for i = 0 , 1, 2, . . . . Fix a basepoint in each component of Y , denote their union by S, and let Si be the image of S under the inclusion 

Y ∼= Y × { 0} ⊂ Y × [−i, 0] ⊂ Mi.

Assume Wi ⊂ Mi is an oriented homologically volume minimizing representative of ¯αi for i = 0 , 1, 2, . . . . If X ⊂ Y is an embedded hypersurface which is the only volume minimizing representative of α ∈ Hn−1(Y ; Z), then there is smooth subconvergence (Mi, W i, ¯gi, Si) −→ (Y × (−∞ , 0] , X × (−∞ , 0] , g + dt 2, S∞)94 as i → ∞ where S∞ ⊂ Y × { 0} is the inclusion of S.

Remark 3.2.2. In Main Lemma, we allow the manifold Y ′ to be empty. 

3.22. Proof of the Main Lemma: outline 

Consider the limiting space Y × (−∞ , 0], with the exhaustive sequence Ui =

Y ×(−i−1, 0] and maps Ψ i : Ui → Mi taking Ui identically onto Y ×(−i−1, 0] ⊂ Mi.Our choice of Ui and Ψ i satisfy the conditions (1) and (2) from Definition 3.2.2 for obvious reasons. It will be useful to equip M with a height function F : M → [−1, 0] satisfying 

Y = F −1(0) and Y ′ = F −1(−1). Extend this function to Mi by 

Fi(x) = 



t if x = ( y, t ) ∈ Y × [−i, 0] 

F (x) − i if x ∈ M.      

> YWRi
> Mi
> 0
> −R
> −R−1
> −i−1
> Fi

FIGURE 3.2. The hypersurface W Ri ↪→ Mi. In this figure, Y ′ = ∅.95 For any positive integer i and heights 0 ≤ R < R ′ ≤ i, we write 

W Ri = F −1 

> i

([ −R, 0]) and Wi[−R′, −R] = F −1 

> i

([ −R′, −R]) .

Let α ∈ Hn−1(Y ; Z) be the class from the statement of Main Lemma. For L > 0 let 

α × [−L, 0] ∈ Hn(Y × [−L, 0] , Y × {− L, 0}; Z)be the product of α and the fundamental class of ([ −L, 0] , {− L, 0}). We will break up the proof of Main Lemma into three claims. 

Claim 3.2.1. Let L > 0. The hypersurface X × [−L, 0] ⊂ Y × [−L, 0] is the only homologically volume-minimizing representative of α × [−L, 0] .

Claim 3.2.2. For each R > 0, Vol( W Ri ) → R · Vol( X) as i → ∞ .

Claim 3.2.3. For each R > 0, there is a sequence {aRi }∞ 

> i=1

such that, for each j =1, 2, . . . , the hypersurfaces {Ψ−1 

> j

(W RaRi

)}∞ 

> i=1

converge smoothly locally as graphs in Y ×

(−∞ , 0] .

Now we show how Main Lemma follows from Claims 3.2.1, 3.2.2, and 3.2.3. Indeed, by Claim 3.2.3, for each k = 1 , 2, . . . , there is a sequence {aki }∞ 

> i=1

such that, for each j = 1 , 2, . . . , the hypersurfaces {Ψ−1 

> j

(W kaki

)}∞ 

> i=1

converges smoothly locally as graphs to some hypersurface 

W∞,k ⊂ Y × (−∞ , 0] .

96 We notice that the hypersurface W∞,k is contained in Y × [−k, 0] and represents the class α × [−k, 0]. Since the convergence is smooth, we have Vol(Ψ −1 

> j

(W∞,k )) = lim  

> i→∞

Vol(Ψ −1 

> j

(W kaki

)) = k · Vol( X),

where the last equality follows from Claim 3.2.2. However, according to Claim 3.2.1, the only volume minimizing representative of α×[−k, 0] is the hypersurface X×[−k, 0] which has the volume k · Vol( X). Thus W∞,k must be X × [−k, 0]. Evidently, the diagonal sequence {Φ−1 

> j

(Waii )}∞ 

> i=1

has the property that, for each k > 0, Φ −1 

> j

(W kaii

)converges smoothly locally as graphs to X × [−k, 0]. This then completes the proof of Main Lemma. 

3.23. Proof of Claim 3.2.1 

Let Σ ⊂ Y × [−L, 0] be a properly embedded hypersurface representing the class 

α × [−L, 0]. Consider the projection function P : Σ → [−L, 0]. The coarea formula [23, Theorem 5.3.9] applied to P yields 

∫

> Σ

|∇ P |dμ =

∫ 0

> −L

Hn−1(P −1(t)) dt , (3.12) where Hn−1 denotes the ( n − 1)-dimensional Hausdorff measure associated to the metric h + dt 2 on Y × [−L, 0]. Notice that P is weakly contractive in the sense that 

|P (x) − P (y)| ≤ dist Σ(x, y )97 for all x, y ∈ Σ. Thus we have the pointwise bound |∇ P | ≤ 1. Furthermore, since 

P −1(t) represents the class α ∈ Hn−1(Y × { t}; Z) for each t ∈ [−L, 0], 

Hn−1(P −1(t)) ≥ Vol( X)with equality if and only if P −1(t) is X. Combining this observation with (3.12), we conclude Vol(Σ) ≥ L · Vol( X)with equality if and only if Σ = X × [−L, 0]. This completes the proof of Claim 3.2.1. 

3.24. Proof of Claim 3.2.2 

Before we begin, we will construct particular (in general, non-minimizing) properly embedded hypersurfaces NL ⊂ ML representing αL with which to compare Vol( WL) against. Let X ⊂ Y and W0 ⊂ M0 be as in Main Lemma. Since ∂W 0 ∩ Y and X

represent the same homology class, they are bordant via a smooth, properly embedded hypersurface ι : U ↪ → Y × [0 , 1]. We identify [0 , 1] ∼= [ −L, −L + 1] to obtain the embedding 

ιL : U ↪ → [] ιY × [0 , 1] ∼= Y × [−L, −L + 1] ↪→ ML.

Clearly the embedding ι : U ↪ → Y × [0 , 1] may be chosen so that 

NL := W0 ∪∂W 0 UL ∪ (X × [−L + 1 , 0]) ,

where UL = ιL(U ), is a smooth properly embedded hypersurface of ML.98 Evidently, Vol( NL) = Vol( W0) + Vol( UL) + ( L − 1)Vol( X) and NL represents the same homology class as WL. Since WL is homologically area-minimizing, we have Vol( WL) ≤ Vol( NL). In other words, we obtain the inequality 

YW RL

NL

UL

ML

0

−R

−L + 1 

−LY × (−∞ , 0] 

FIGURE 3.3. The hypersurface NL ↪→ ML.Vol( W RL ) + Vol( WL \ W RL ) ≤ Vol( W0) + Vol( UL) + ( L − 1)Vol( X) (3.13) for any 0 < R < L − 1. Now we are ready to prove Claim 3.2.2. Assume it fails. Then there exist ε0, R 0 >

0 and an increasing sequence of whole numbers {ai}∞ 

> i=1

such that the inequality Vol( W R0 

> ai

) > R 0 · Vol( X) + ε0 (3.14) holds for all i. Combining the inequality (3.13) with the assumption (3.14), we have Vol( W0) + Vol( Uai ) + ( ai − 1)Vol( X) > Vol( Wai \ W R0 

> ai

) + ε0 + R0Vol( X). (3.15) 99 Now we will inspect the first term in the right hand side of (3.15): Vol( Wai \ W R0 

> ai

) = Vol( Wai [ai−1 − ai, −R0]) + Vol( Wai [−ai − 1, a i−1 − ai]) 

≥ (ai − ai−1 − R0)Vol( X) + Vol( Wai−1 )

> (ai − ai−1)Vol( X) + ε0 + Vol( Wai−1 \ W R0 

> ai−1

). (3.16) Here we use Claim 3.2.1 in the first inequality and the assumption (3.14) in the second. Combining (3.15) with (3.16), we obtain Vol( W0)+Vol( Uai )+( ai −1)Vol( X) > (ai −ai−1 +R0)Vol( X)+2 ε0 +Vol( Wai−1 \W R0 

> ai−1

).

We iterate the argument to find Vol( W0) + Vol( Uai ) + ( a1 − R0 − 1)Vol( X) > i · ε0 + Vol( Wa1 ) (3.17) for every i = 1 , 2, . . . . Since the left hand side of (3.17) is independent of i, we arrive at a contradiction by taking i to be sufficiently large. 

3.25. Proof of Claim 3.2.3 

While the proof of Claim 3.2.3 is rather technical, it is essentially a consequence of standard tools used in the study of stable minimal hypersurfaces. For instance, see [24] for a similar result in a 3-dimensional context. We divide the proof into three steps, referring to Appendix A when necessary. To begin, we require the following straight-forward volume bound. 100 Step 1. For each R > 0, there is a constant VR > 0 such that Vol( Wi[−λ − R, −λ]) ≤ VR

holds for all i and all λ ∈ [0 , i − R]. In particular, Vol( Wi ∩ BMi 

> R

(x)) ≤ VR for all i

and x ∈ Mi.The next key ingredient is the following uniform bound on the second fundamental form AWL .

Step 2. There is a constant C1 > 0, depending only on the geometry of ( M, ¯g), such that sup 

> x∈WL

|AWL (x)|2 ≤ C1 for L ≥ 0. Step 2 is a consequence of [25, Corollary 1.1]. See Appendix, Section A.32 for more details. 

Step 3. For each R > 0 and j = 1 , 2, . . . , the sequence of hypersurfaces Ψ −1 

> j

(W Ri )sub-converges smoothly locally as graphs as i → ∞ .

Proof of Step 3. We restrict our attention to the tail of the sequence {W Ri }∞

> i=1

, where 

i ≥ R + 1. This allows us to consider each W Ri and W R+1  

> i

as hypersurfaces of 

Y × (−∞ , 0] which is where we will show the convergence. By rescaling the original metric ¯ g, we will assume that inj g ≥ 1 and the bounds sup x∈B1(y) |¯gij (x) − δij | ≤ μ0, sup x∈B1(y)

∣∣∣∂¯gij  

> ∂x k

(x)

∣∣∣ ≤ μ0

hold for 1 ≤ i, j, k ≤ n + 1 in geodesic normal coordinates centered about any y ∈

Y × (−∞ , 0] where μ0 is the constant from Lemma A.2.1. Let r = min( 124 , 16√20 C0 )where C0 is the constant from Step 2. 101 We cover Y × [−R, 0] by a finite collection of open balls U = {Br(yl)}Nl=1 . Notice that each Br(yl) ⊂⊂ Y × [−R − 1, 0]. Consider a ball Br(yl) in U with the property that 

W R+1  

> i

∩ Br(yl) 6 = ∅

for infinitely many i. Unless explicitly stated, we will continue to denote all subsequences by W R+1  

> i

. Our next goal is to show that the sequence of hypersurfaces 

{W Ri ∩ Br(yl)}∞ 

> i=1

sub-converges smoothly locally as graphs. We choose a subsequence of W R+1  

> i

and points xi ∈ W R+1  

> i

∩Br(yl) which converge to some point x∞ ∈ Br(yl). Now it will be convenient to work in the tangent space to the point x∞. We use the short-hand notation φ = exp ¯gx∞ and let 

B = φ−1(B1(x∞)) ⊂ Tx∞ (Y × [−L − 1, 0]) .

Consider the properly embedded hypersurfaces Σ i ⊂ B with base points pi ∈ Σi,given by Σi = φ−1(B1(x∞) ∩ W Ri ), pi = φ−1(xi).

We also write Z = φ−1(yl) Since W Ri ⊂ Mi are minimal, Σ i are minimal hypersurfaces in B with respect to the metric ¯ gB = ( φ−1)∗(¯ g). Notice that the choice of r allows us to apply Corollary A.2.1 to each Σ i ⊂ B at 

pi with s = 3 r. For each i = 1 , 2, . . . , we obtain an open subset Ui ⊂ Tpi Σi ∩ B, a unit normal vector ηi ⊥ Tpi Σi, and a function ui : Ui → R satisfying the bounds (A.5) and such that graph( ui) = BΣi 

> 6r

(pi). Moreover, the connected component of B¯gB 

> 3r

(pi) ∩ Σi

containing x0 lies in BΣi 

> 6r

(pi). We use compactness of Sn and pass to a subsequence so that the vectors ηi

converge to some vector η∞ ∈ Sn. Let P∞ ⊂ Tx∞ (Y × [−L − 1, 0]) be the hyperplane 102 perpendicular to η∞. For large enough i, we may translate and rotate the sets Ui to obtain open subsets U ′ 

> i

⊂ P∞ and functions u′ 

> i

: U ′ 

> i

→ R such that 1. graph( u′

> i

) = BΣi 

> 4r

(pi); 2. the ball BP∞ 

> 2r

(0) ⊂ U ′ 

> i

;3. for each k ≥ 1 and α ∈ (0 , 1) there is a constant C′ > 0, depending only on n,

k, α, and the geometry of g, such that 

|| u′

> i

|| Ck,α (U ′  

> i)

≤ C′,

see Fig. 3.4.. In particular, writing u′′  

> i

= u′

> i

|BP∞ 

> 2r(0)

, the sequence {u′′  

> i

}i is uniformly bounded in Ck,α (BP∞ 

> 2r

(0)). Moreover, the connected component of B2r(pi) ∩ Σi

containing pi is contained in graph( u′′  

> i

). It follows that Σ ′

> i

, the connected component of Br(Z) ∩ Σi containing pi, lies in graph( u′′  

> i

). 

B2r(0) 

x′

U ′

> i

Ui

Σ′

> i

TpiΣi

P∞

xpi

0

ui(x)

u′

> i

(x)

B

FIGURE 3.4. The functions u′ 

> i

and hypersurfaces Σ ′

> i

By Arzela-Ascoli, one can find a subsequence of u′′  

> i

converging in Ck(BP∞ 

> 2r

(0)) to a function u∞ : BP∞ 

> 2r

(0) → R. In particular, u∞ is a strong solution to the 103 minimal graph equation on BP∞ 

> 2r

(0) with respect to ¯ gB and Σ ′ 

> i

converge as graphs to graph( u∞). To summarize our current progress, the components of W R+1  

> i

∩ Br(yl)containing xi sub-converge smoothly to φ(graph( u∞)). This finishes our work with the hypersurfaces Σ ′

> i

.Now suppose that there is a second sequence of connected components within 

W R+1  

> i

∩ Br(yl). We can repeat the above process to obtain a second limiting hypersurface. Observe that the number of components of W R+1  

> i

∩ Br(yl) uniformly bounded in i. Indeed, using the notation above, for any component ¯Σi ⊂ W R+1  

> i

∩

Br(yl), we have Vol ¯gB (Σ ′

> i

) ≥ Vol ¯gB (BP∞ 

> r

(0)) ,

which is uniformly bounded below in terms of r and the geometry of g. However, Step 1 implies that Vol( W Ri ∩ Br(yl)) is bounded above uniformly in i so the number of connected components W Ri ∩ Br(yl) is uniformly bounded in i. Hence the above process terminates after finitely many iterations. We conclude that the sequence 

{W Ri ∩Br(yl)}∞ 

> i=1

sub-converges smoothly locally as graphs to a minimal hypersurface Σ∞,l .Now, restricting to this subsequence, we turn our attention to another ball Br(yl′ )in the cover U. We repeat the above argument to obtain a further subsequence and limiting minimal hypersurface Σ ∞,l ′ . Repeating this process for each element of U produces a subsequence converging to a minimal hypersurface W R 

> ∞

= ⋃Nl=0 Σ∞,l 

smoothly locally as graphs. This completes the proof of Claim 3.2.3, and consequently, the proof of Main Lemma. 104 3.3. Proof of Theorem 1.5.6 

In order to prove Theorem 1.5.6, we have to use fundamental facts relating conformal geometry and psc-bordism. We briefly recall necessary results, following the conventions in [26]. Let Y be a compact closed manifold with dim Y = n given together with a conformal class C of Riemannian metrics. Then the Yamabe constant 

of ( Y, C ) is defined as 

Y (Y ; C) = inf 

> g∈C

∫ 

> Y

Rgdμ g

Vol g(Y )n−2

> n

.

We say that a conformal class C is positive if Y (Y ; C) > 0. It is well-known that C

is positive if and only if there exists a psc-metric g ∈ C.Now let Z : Y0 Y1 be a bordism between closed manifolds Y0 and Y1. Suppose we are given conformal classes C0 and C1 on Y0 and Y1, respectively. Let ¯C be a conformal class on Z, such that ¯C|Y0 = C0 and ¯C|Y1 = C1, i.e. ∂ ¯C = C0 t C1.Denote by ¯C0 = {¯g ∈ ¯C : H¯g ≡ 0} the subclass of those metrics with vanishing mean curvature of the boundary. Then the relative Yamabe constant of (( Z, ¯C), (Y0 t

Y1, C 0 t C1)) is defined as 

Y ¯C (Z, Y 0 t Y1; C0 t C1) = inf  

> ¯g∈¯C0

∫ 

> Z

R¯gdμ ¯g

Vol ¯g(Z)n−2

> n

.

This gives the relative Yamabe invariant 

Y (Z, Y 0 t Y1; C0 t C1) = sup  

> ¯C, ∂ ¯C=C0tC1

Y ¯C (Z, Y 0 t Y1; C0 t C1).

Now we assume that the conformal classes C0 and C1 are positive. Then we say that positive conformal manifolds ( Y0, C 0) and ( Y1, C 1) are positive-conformally bordant if there exists a conformal manifold ( Z, ¯C) and a bordism Z : Y0 Y1 between Y0 and 105 Y1 such that ∂ ¯C = C0 t C1 and Y ¯C (Z, Y 0 t Y1; C0 t C1) > 0. In this case, we write (Z, ¯C) : ( Y0, C 0) (Y1, C 1). We need the following result which relates the above notions to psc-bordisms. 

Theorem 3.3.1. [26, Corollary B] Let Y0 and Y1 be closed manifolds of dimension 

n ≥ 3, Z : Y0 Y1 be a bordism between Y0 and Y1, and g0 and g1 be psc-metrics on 

Y0 and Y1, respectively. Then Y (Z, Y 0 t Y1; [ g0] t [g1]) > 0 if and only if the boundary metric g0 tg1 on Y0 tY1 may be extended to a psc-metric ¯g on Z such that ¯g = gj +dt 2

near Yj for j = 0 , 1.

3.31. Long collars 

We are ready to prove Theorem 1.5.6 for n ≤ 6. The adjustments required to adapt the following proof to the case n = 7 are provided in Appendix A.33. Let ( Y0, g 0, γ 0) and ( Y1, g 1, γ 1) be the manifolds from Theorem 1.5.6 and let 

α0 ∈ Hn−1(Y0; Z) and α1 ∈ Hn−1(Y1; Z) be the classes Poincar` e dual to γ0 and γ1,respectively. It is convenient to use the notation 1 Y = Y0 t − Y1 and 

α = ( ι0)∗α0 − (ι1)∗α1 ∈ Hn−1(Y ; Z),

where ιj : Yj ↪→ Y is the inclusion map for j = 0 , 1. Then we consider hypersurfaces 

X0 ⊂ Y0 and X1 ⊂ Y0 which are homologically volume minimizing representatives of the classes α0 and −α1. The existence of such smooth X0 and X1 is guaranteed in this range of dimensions, see [3]. Notice that, by a small conformal change which does not effect the assumptions on ( Yj , g j , γ j ), we may assume that Xj is the only     

> 1Here we emphasize a proper orientation on Y0and Y1

106 representative of αj with minimal volume for j = 0 , 1, see [27, Lemma 1.3]. We write (X, h X ) for the Riemannian manifold ( X0 t X1, g 0|X0 t g1|X1 ). Now we choose a psc-bordism ( Z, ¯g, ¯γ) : ( Y0, g 0, γ 0) (Y1, g 1, γ 1). We will use (Z, ¯g, ¯γ) to construct a psc-bordism which satisfies the conclusion of Theorem 1.5.6. We denote by ¯ α ∈ Hn(Z; Z) the homology class Poincar` e dual to ¯ γ. Then ∂ ¯α = α,see Lemma 1.5.5. Now for each i = 1 , 2, . . . , we consider the i-collaring of the bordism ( Z, ¯g, ¯γ), denoted by ( Zi, ¯gi, ¯γi), as in Section 3.21. By Theorem 1.5.4, there exists properly embedded hypersurfaces Wi ⊂ Zi which are homologically volume minimizing and represents ¯αi. The restrictions of ¯ gi to Wi and ∂W i are denoted by ¯hi and hi,respectively. In preparation to apply Main Lemma, we fix basepoints xj ∈ Xj for each j = 0 , 1and set S = {x0, x 1} ⊂ X. Naturally, the set S is identified with the subsets Si in (X × { 0}) ⊂ ∂Z i for i = 1 , 2, . . . and with S∞ in the boundary of the cylinder (X × { 0}) ⊂ (Y × (−∞ , 0]). According to Main Lemma we may find a subsequence 

{ai}∞ 

> i=1

such that (Zai , W ai , ¯gai , Sai ) −→ (Y × (−∞ , 0] , X × (−∞ , 0] , g + dt 2, S∞)smoothly as i → ∞ and the Riemannian manifolds ( ∂W ai , h ai ) converge to ( X, h X )in the smooth Cheeger-Gromov topology as i → ∞ .

Remark 3.3.1. We note that the manifolds ( ∂W ai , h ai ), ( X, h X ) are compact and so there is no need to specify base points for this convergence. The following is a special case of a much more general fact on the behavior of elliptic eigenvalue problems under smooth Cheeger-Gromov convergence (see [28]). 107 Lemma 3.3.2. Let {(Mi, g ′

> i

)}∞ 

> i=1

be a sequence of compact Riemannian manifolds smoothly converging to a compact Riemannian manifold (M∞, g ′∞) in the Cheeger-Gromov sense. If Y (M∞; [ g′∞]) > 0, then, upon passing to a subsequence, 

Y (Mi; [ g′

> i

]) > 0 for all sufficiently large i.Proof. For each i = 1 , 2, . . . , we denote by λ1,i = λ1(Lg′ 

> i

) the principal eigenvalue of the conformal Laplacian on ( Mi, g ′

> i

). Let φi ∈ C∞(Mi) be the eigenfunction satisfying 

Lg′ 

> i

φi = λ1,i φi, sup 

> Mi

φi = 1 . (3.18) Since {(Mi, g ′

> i

)}∞ 

> i=1

is converging in the Cheeger-Gromov topology to a compact manifold, the coefficients of the operator Lg′ 

> i

are bounded in the C1-norm uniformly in i. In particular, there is a constant C1 > 0, independent of i, such that |Rg′ 

> i

| ≤ C1

on Mi. An obvious estimate on the Rayleigh quotient (3.5) shows that the sequence 

{λ1,i }∞ 

> i=1

is uniformly bounded above and below. This allows us to apply the Schauder estimate Theorem A.1.2 to φi uniformly in i. Using Arzel´ a-Ascoli, we can find a subsequence, still denoted by {(Mi, g ′

> i

)}∞

> i=1

,

{φi}∞

> i=1

, and {λ1,i }∞

> i=1

, a function φ∞ ∈ C∞(M∞), and a number λ1,∞ such that 

φi → φ∞ λ1,i → λ1,∞

where the former convergence is in the C2,α -topology. This allows us to take the limit of equation (3.18) as i → ∞ . Namely, φ∞ is a non-zero solution of the equation 

Lg∞ φ∞ = λ1,∞φ∞

108 and so λ1,∞ ≥ λ1(Lg∞ ). On the other hand, we have assumed that λ1(Lg∞ ) > 0. Hence λ1,i > 0 for all sufficiently large i.Now we return to the proof of Theorem 1.5.6. Since X is a stable minimal hypersurface of Y with trivial normal bundle, Theorem 1.5.1 implies that 

Y (X, [gX ]) > 0. Now we may apply Lemma 3.3.2 to find Y (∂W ai , [hai ]) > 0 for sufficiently large i. Fix such an i and let h′ 

> ai

∈ [hai ] be a psc metric on ∂W ai . Since each Wai is a stable minimal hypersurface with free boundary and trivial normal bundle, Theorem 1.5.3 states that Y (Wai , ∂W ai ; [ ¯hai ]) > 0 for all i ∈ N. Finally, we use Theorem 3.3.1 to find a psc-metric ˜hai on Wai which restricts to h′ 

> ai

+ dt 2 near 

∂W ai . This completes the proof of Theorem 1.5.6 for n ≤ 6. 109 APPENDIX GEOMETRIC ANALYSIS BACKGROUND Let us first describe the structure of this Appendix. In Section A.1, we state the basic regularity facts for solutions of elliptic equations both with and without boundary conditions. These facts are used in both Part One and Part Two. In Section A.2, we recall relevant facts on the minimal graph equation and provide the Schauder estimates we use in the proof of Main Lemma from Part Two. Section A.3 is dedicated to Theorem 1.5.4. Here we recall necessary results on currents and state well-known facts on their compactness and regularity, adapted to our setting. Section A.31 describes a simple doubling method which is a convenient technical tool in the remaining sections. In Section A.32, we justify Step 2 from the proof of Claim 3.2.3. In Section A.33, we discuss regularity issues in dimension 8 and prove Theorem 1.5.6 for n = 7. 

A.1. Elliptic Estimates 

In Part One, we use a regularity result for solutions of linear elliptic problems which is suited for the linear analysis in Section 2.21. The following theorem is a version of elliptic Lp estimate, tailored to the Neumann problem. 

Theorem A.1.1. cf. [20, Theorem 3.2] Let (N, g N ) be a compact Riemannian manifold with boundary ∂N . Assume that v ∈ W k+2 ,p (N, g N ) for some k, p ∈ N0

satisfies ∫ 

> N

v dμ gN = 0 . Then there is a constant C depending only on the geometry of (N, g N ), k, and p such that 

|| v|| W k+2 ,p (N,g N ) ≤ C

(

|| ∆gN v|| W k,p (N,g N ) + || ∂ν v|| W k+1 ,p ∂ (N,g N )

)

. (A.1) 110 where the norm || · || W k,p ∂ (N,g N ) is defined by 

|| F || W k,p ∂ (N,g N ) := inf {|| G|| W k,p (N,g N ) : G ∈ W k,p (N, g N ), G |∂N = F }.

In Part Two, we will need the following standard Schauder estimate for solutions of linear elliptic propblems. 