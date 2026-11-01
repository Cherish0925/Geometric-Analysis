---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Higher order obstructions to the desingularization of Einstein metrics]

We define T4/Z2 as the quotient of R4/(2 LZ4) for some L ∈ GL (4 , R) by the action of {Id , −Id }. A metric on T4/Z2 can be seen as an 2 LZ4-invariant and Z2-invariant metric on R4. It is therefore determined by its values on any cube L([ a, a + 1] 4) for a ∈ R. We will denote ( T4/Z2, gL) the orbifold obtained with the matrix L.All of the infinitesimal Ricci-flat deformations of a flat T4/Z2 are inte-grable. More precisely, all of the Ricci-flat deformations of T4/Z2 are flat Higher order obstructions to the desingularization 941 and can be seen as either varying the above invertible matrix L, or as mod-ifying the scalar product, that is by adding a constant symmetric 2-tensor of norm smaller than 1 to the metric gL.This orbifold has 16 singular points with R4/Z2 singularities. We will denote 

S := {L(1,  2,  3,  4),  i ∈ { 0, 1}} + 2 LZ4

its singular set on R4 before the taking the quotients by 2 LZ4 and {Id , −Id }.

Remark 3.1. Since this orbifold is flat, it clearly satisfies our obstruction 

(0.2) .

3.2. Partial hyperk¨ ahler desingularizations and estimates 

In the rest of the article, we consider ( M, g DL,ζ ) a na¨ ıve desingularization of (T4/Z2, gL) for L ∈ GL (4 , R) by positively oriented Eguchi-Hanson metrics (eh ζ +

> i

)i∈S+ for ζi ∈ R3\{ 0} at a subset S+ of the 16 singular points of 

T4/Z2 and by negatively oriented ( eh ζ −

> j

)j∈S− for ζj ∈ R3\{ 0} at a subset 

S− of the singular points. We denote ζ = (( ζ+ 

> i

)i∈S+, (ζ− 

> j

)j∈S−). We will first be interested in its partial hyperk¨ ahler desingularizations obtained by perturbation of the metric only desingularized by Eguchi-Hanson metrics in the same orientation. 

3.2.1. Hyperk¨ ahler partial desingularizations of T4/Z2 and approx-imations. Let us define ( M±, g D 

> ±

) := ( MS±, g DL,ζ ±) the partial desingular-izations where the only points which are desingularized are S± by the above Eguchi-Hanson metrics ( eh ζ ±

> i

)i∈S±. They can be perturbed to hyperk¨ ahler orbifolds. 

Lemma 3.2. Let gD 

> ±

:= gDL,ζ ± be a na¨ ıve desingularization of T4/Z2 thanks to Eguchi-Hanson metrics (7) glued in one given orientation at some or all singular points. Then, the Einstein modulo obstructions perturbation of gD 

> ±

, denoted 

g± := gL,ζ ± and defined in [Ozu19b] is hyperk¨ ahler. Sketch of proof. It is well-known (or can be proven from [Don12]) that the moduli space of the Ricci-flat and even hyperk¨ ahler (orbifold) metrics on 

M± is of maximal dimension 3 |S±| + 9 which is the same as the space of Ricci-flat modulo obstructions metrics of [Ozu19b]. Using a connectedness argument similar to that of [Ozu20t, Proposition 5.70] for the moduli space of Kronheimer’s gravitational instantons, we conclude that any Einstein mod-ulo obstruction perturbation of a metric gD 

> ±

is actually Ricci-flat (and even hyperk¨ ahler). 942 Tristan Ozuch To obtain more information about these hyperk¨ ahler metrics g±, it suf-fices to construct metrics which are approximately Ricci-flat by [Ozu19b]. 

Remark 3.3. We will in particular need to have a good approximation of the Riemannian curvature tensor of g± at the remaining singular points. We will see that we have |Rg±| ∼ | ζ±|2, and the previous control (50) in 

O(|ζ±| 32 − β 

> 4

) is not sufficient for our purpose. 

3.2.2. Approximation of the partial hyperk¨ ahler desingularizations. 

We want to find good enough approximations to be able to control the cur-vature of our hyperk¨ ahler partial desingularizations. Consider the following construction. On the orbifold ( T4/Z2, gL), for any harmonic homogeneous symmetric 2-tensor on R4/Z2 with |H 4|e ∼ r−4 

> e

and a singular point i ∈ S, we can solve the equation (60) 

⎧⎪⎪⎨⎪⎪⎩

PLh4 = 0 , and BLh4 = 0 ,h4 = H 4 + 0 + O(r−) for any  > 0 at the singular point i, h4 ⊥ O(gL).

somewhat explicitly (notice that there is no obstruction contrarily to (35)). Indeed, as in [BK17], one would expect the periodization of the sum of the symmetric 2-tensors H to be a solution. At x ∈ R4, this would look like (61) ∑

> a∈Z4

H 4(L(2 a) + x − i).

However except in the most symmetric cases, like the one treated in [BK17], this periodization diverges (it is a sum of terms in r−4 over a Z4 grid). One way around it is simply to substract to each term of the sum the mean value of it over a period, namely, we define (62) h4(x) = ∑

> a∈Z4

(H 4(L(2 a) + x − i) − H 4

> av

(L, i, 2a)),

where H 4

> av

(L, i, 2a) is the average of H 4(x) on the set i + L(2 a + [ −1, 1] 4). This sum converges because we have ∇lH 4 = O(r−4−l 

> e

) which is summable on Z4\{ 0} for l > 0. In particular, the curvature is summable. Note moreover that, by construction, h4 of (62) is indeed orthogonal to the infinitesimal deformations of gL which are constant symmetric 2-tensor and that BgLh4 =0 as well as tr gLh4 = 0. Higher order obstructions to the desingularization 943 

Remark 3.4. The point is that the symmetric 2-tensors we have substracted are constant and therefore, the curvature induced are the same as those of the sum (61) .

Let, H 4(ζ± 

> i

) for i ∈ S± be the r−4-asymptotic terms of the metric eh ζ ±

> i

,see (11). Consider the unique symmetric 2-tensor h4(ζ± 

> i

) as in (62) which is asymptotic to H 4(ζ± 

> i

) at i and bounded everywhere else while satisfying 

h4(ζ± 

> i

) ⊥gL O(gL). Consider now a singular point i ∈ S± and denote |ζ±| = max i′∈S± |ζ± 

> i′

|.We have the following expansion of the sum ∑  

> i′=i

h4(ζ± 

> i′

) = H0(i) + H2(i) + 

O(d(i, . )4) at i with |H0(i)| = O(|ζ±|2) a constant symmetric 2-tensor, and 

|H2(i)| = O(|ζ±|2)r2

> e

. For some linear isomorphism φi with, ‖φi − Id ‖ =

O(|ζ±|2), we have e + H0(i) = φ∗ 

> i

e. In the coordinates of (7), the metric 

φ∗ 

> i

eh ζ ±

> i

(see Remark 2.6 for the meaning of this action of the diffeomorphism) is asymptotic to e + H0(i). Consider now h2(i) a solution to Pφ∗ 

> ieh ζ±
> i

h2(i) ∈

O(φ∗ 

> i

eh ζ ±

> i

), with h2(i) = H2(i) + + O(r−2+ ) for all  > 0 from (20). Since the perturbation g± is Ricci-flat, we actually have (63) Pφ∗ 

> ieh ζ±
> i

h2(i) = 0 .

Note that h2(i) it is determined up to O(φ∗ 

> i

eh ζ ±

> i

). We choose the solution which is orthogonal to O(φ∗ 

> i

eh ζ ±

> i

) for the L2-product induced by φ∗ 

> i

eh ζ ±

> i

on 

S2 as in (20). 

Definition 3.5 (Approximate hyperk¨ ahler metric gA

> ±

). We define the ap-proximate hyperk¨ ahler metric gA 

> ±

in a way similar to Definition 1.21): we glue the different φ∗ 

> i

eh ζ ±

> i

+ h2(i) for i ∈ S± to the metric gL + ∑ 

> i∈S±

h4(ζ± 

> i

)

at the points i ∈ S± with cut-off at distance at |ζ± 

> i

| 16 , that is with the fol-lowing metric on the gluing region: 

χ(|ζ± 

> i

|− 16 re)

(

φ∗ 

> i

eh ζ ±

> i

+ h2(i)

)

+ (1 − χ(|ζ± 

> i

|− 16 re))(

gL + ∑

> i∈S±

h4(ζ± 

> i

)

)

.

3.2.3. Control of the partial hyperk¨ ahler desingularizations. We now justify the qualifier “approximate” for the metric gA

> ±

.

Proposition 3.6. We have the following control on the metric: for all k ∈

N, there exists C = C(k, L ) > 0, such that 

(64) ‖gA 

> ±

− g±‖C kβ, ∗(gD  

> ±)

 C|ζ±|2+ 23 − β 

> 6

.944 Tristan Ozuch 

In particular, at each remaining singular point p, we have 

(65) 

∣∣∣RgA 

> ±

− Rg±

∣∣∣gD

> ±

 C|ζ±|2+ 23 − β 

> 6

.

Remark 3.7. We a priori had Rg± = O(|ζ±|2) so this is indeed a good approximation of Rg± as ζ± → 0. The controls of (50) in |ζ| 32 − β 

> 4

are not precise enough here. Proof. Thanks to [Ozu20t, Proof of Theorem 4.51], it is enough to control the values of ΦgD 

> ±

(gA

> ±

) in r−2 

> D

Ck,α β (gD 

> ±

) in order to obtain (64), where for two metrics g and g′, we define 

Φg(g′) := Ric( g′) + δ∗

> g′

Bgg′

as in the first section. Estimates similar to [Biq13, Lemma 14.2] and [BK17, Proposition 3.4], yield the following controls. For all k ∈ N, there exists 

Ck > 0 for which for a given singular point i0, in the neighborhood of i0

1. in the region where rD > 2|ζ± 

> i0

| 16 , we have gA 

> ±

= gL + h4 and gD 

> ±

= gL

and therefore, since the linear terms vanish, that is dgLΦgLh4 = 0, the error is at least quadratic. Since rkD|∇ kh4|gD 

> ±

 C|ζ±|2r−4 

> D

, we have 

rkD|∇ kΦgD 

> ±

(gA

> ±

)|gA 

> ±

 Ck|ζ±|4r−10  

> D

,

2. in the region where rD < |ζ± 

> i0

| 16 , we have gA 

> ±

= eh ζ ±

> i

+ h2 and gD 

> ±

=

eh ζ ±

> i

. Like above, by (63) we also only have to control the nonlinear terms, and since rkD|∇ kh2|gD 

> ±

 C|ζ±|2r2

> D

, we find 

rkD|∇ kΦgD 

> ±

(gA

> ±

)|gA 

> ±

= |ζ±|4r2

> D

,

3. in the region where |ζ± 

> i0

| 16 < r D < 2|ζ± 

> i0

| 16 , gA 

> ±

and gD 

> ±

are respectively an interpolation between gL + h4 and eh ζ ±

> i

+ h2 and an interpolation between gL and eh ζ ±

> i

thanks to a cut-off function. Now we have 

rkD

∣∣∣∇k((gL + h4) − (eh ζ ±

> i

+ h2

))∣ ∣∣e  C|ζ±|2r4 

> D

+ |ζ±|4r−8 

> D

, and 

rkD

∣∣∣∇k(gL − eh ζ ±

> i

)∣∣∣e  C|ζ±|2r2 

> D

+ |ζ±|2r−4 

> D

,

and since |ζ±|1/6 < r D < 2|ζ±|1/6, by controlling the cut-off function, we find r2+ kD |∇ kΦgD 

> ±

(gA

> ±

)|gA 

> ±

 C|ζ±|2+ 23 .Higher order obstructions to the desingularization 945 Finally, since the control is straightforward away from the singular points, we obtain 

‖ΦgD 

> ±

(gA

> ±

)‖r−2     

> DCk,α β(gD
> ±)

 C|ζ±|2+ 23 − β 

> 6

,

which gives the estimate (64), see the argument of [Ozu20t, Theorem 4.51]. 

3.2.4. Approximation of the infinitesimal deformations. Let us ap-proximate the kernel of Pg±, O(g±) thanks to the following symmetric 2-tensors. 

Definition 3.8. We define ˜O(gA

> ±

) the linear space spanned by the infinites-imal variations of (L, ζ ±)  → gA 

> ±

= gAL,ζ ±.

Let us start by recalling a general lemma for operators between Banach spaces which will be useful to approximate the elements of the kernel of our operator on the hyperk¨ ahler partial desingularizations. 

Lemma 3.9 ([Ozu19b]) . Let P, P ′ : X → Y be two operators between two Banach spaces X and Y for which there exists C > 0 1100 C >  > 0 and a finite-dimensional linear subspace K′ and S′ a supplement of K′ in X such that we have 1. for any x ∈ X, ‖(P − P ′)x‖Y  ‖x‖X ,

2. for any x ∈ S′, ‖x‖X  C‖P ′x‖Y ,

3. for any x ∈ K′, ‖P ′x‖Y  ‖x‖X ,

4. dim (ker P ) = dim (K′).Then, for any element k′ of K′, there exists an element k of ker P such that 

‖k − k′‖X  2C 

1 − C ‖k′‖X .

Proposition 3.10. Let O(g±) be the kernel of Pg±. Then, for any o± ∈

O(g±), there exist oA 

> ±

∈ ˜O(gA

> ±

) such that we have 

‖o± − oA

> ±

‖C 2,α β, ∗ (gD  

> ±)

 C|ζ±|2+ 23 − β 

> 6

.

Proof. Let us apply Lemma 3.9 with P = Pg±, P ′ = PgA

> ±

, K′ = ˜O(gD 

> ±

) and 

S′ = ˜O(gA

> ±

)⊥. We have the following controls: there exists C > 0 indepen-dent of |ζ±| small enough 946 Tristan Ozuch 1. for any h ∈ C2,α β, ∗ (gD 

> ±

), by Proposition 3.6, we have 

‖(Pg± − PgA

> ±

)h‖r−2     

> DCαβ(gD
> ±)

 C|ζ±|2+ 23 − β 

> 6

‖h‖C 2,α β, ∗ (gD 

> ±)

,

2. for any h ∈ C2,α β, ∗ (gD 

> ±

) ∩ ˜O(gA

> ±

)⊥, by [Ozu19b], we have 

‖h‖C 2,α β, ∗ (gD  

> ±)

 C‖PgA

> ±

h‖r−2    

> DCαβ(gD
> ±)

,

3. by an estimation very similar to that of Proposition 3.6, which we therefore omit, for any oA ∈ ˜O(gA

> ±

), 

‖PgA

> ±

oA‖r−2     

> DCαβ(gD
> ±)

 C|ζ±|2+ 23 − β 

> 6

‖oA‖C 2,α β, ∗ (gD 

> ±)

,

4. and, dim O(g±) = dim ˜O(gA

> ±

) since every gluing configuration can be perturbed to a Ricci-flat manifold by Lemma 3.2. We can therefore apply Lemma 3.9 and obtain the stated estimate. Using the control of o± of Proposition 2.19, we moreover have the fol-lowing estimate of the infinitesimal variation of Rg in the direction of o±:for C > 0, we have (66) 

∣∣∣∂o±Rg± − ∂oA

> ±

RgA

> ±

∣∣∣gA

> ±

 C|ζ±|2+ 23 − β 

> 6

‖o±‖L2(g±)

where we denoted ∂o±Rg± the differential of g±  → Rg± at g± in the direc-tion o±.

3.3. Total desingularizations modulo obstructions 

Let us start by using a notation which will be convenient for this section. 

Definition 3.11. For a section s on (R4/Z2)\{ 0}, we will write s ∝ rk 

> e

if 

s ∈ rk

> e

Cl

> −

(R4/Z2) for all l ∈ N and  > 0.For k ∈ Z and f : ( R3)16  → R+ 

> ∗

, we will write s ∝ f (ζ)rk 

> e

if as the parameters ζ → 0, we have s = ( f (ζ) + o(f (ζ)) s′ for s′ ∝ rk

> e

.

Remark 3.12. For any l  0, we have rk 

> e

log l(re) ∝ rk

> e

.

Let us now consider the total desingularization of the partial hyperk¨ ahler desingularizations g± by gluing the Eguchi-Hanson metrics eh ζ ∓

> j

at the re-maining singular points j ∈ S∓. Here, the hyperk¨ ahler orbifold ( M±, g±)Higher order obstructions to the desingularization 947 will play the role of ( Mo, go) in Section 2. From the obstruction result of Theorem 0.2, we can already say that in order to desingularize the orbifold (M±, g±) by a nondegenerate sequence of Einstein manifolds in the Gromov-Hausdorff sense, it is necessary that the condition Rg± = 0 is satisfied at every remaining singular point. This was done thanks to an approximate development at order 4, see Definition 2.15. In this section, we are interested in the more challenging situation of a sequence of desingularization of a sequence of metrics g±,n , and this requires an approximation at an even higher order. 

3.3.1. An approximate Einstein modulo obstructions metric. Let 

L ∈ GL (4 , R) and ζ =

(

(ζ± 

> i

)i∈S±, (ζ∓ 

> j

)j∈S∓

)

∈ (R3)|S±| × (R3)|S∓| ∼ (R3)16 .

Definition 3.13 (Total desingularizations, gDL,ζ ). We define gDL,ζ the na¨ ıve gluing at all j ∈ S∓ of the metrics eh ζ ∓

> j

to the metric g±. Recall the notation 

|ζ±| = max i∈S± |ζi|.

As in Section 2, the goal of the present section is to construct better approximate Einstein modulo obstructions metric in order to identify the obstructions. 

Proposition 3.14. Let L0 ∈ GL (4 , R). Then there exists C > 0 and a neighborhood U of (L0, 0) ∈ GL (4 , R)×(R3)16 such that there exists a smooth family of metrics (gAL,ζ )(L,ζ )∈U for which if we denote ˜O(gAL,ζ ) the space of the infinitesimal deformations of (L, ζ )  → gAL,ζ , we have 1. ‖gAL,ζ − gDL,ζ ‖C 2,α β, ∗ (gDL,ζ ) → 0 as ζ → 0,2. gAL,ζ − gDL,ζ ⊥L2(gAL,ζ ) ˜O(gAL,ζ ), and 3. ‖ΦgAL,ζ (gAL,ζ ) − oAL,ζ ‖r−2    

> DCαβ(gDL,ζ )

 C|ζ±|1+ β 

> 12

|ζ∓|3− β 

> 4

for oAL,ζ ∈ ˜O(gAL,ζ )

explicited in the proof. 

Let us consider the development of the metric g± at the singular point 

j ∈ S∓,(67) g± = e + ∑

> m∈N∗

Hj, 2m, with Hj, 2m ∝ | ζ±|2r2m

> e

by Proposition 3.6, and similarly, for each j, at infinity we have (68) eh ζ ∓

> j

= e + ∑

> m∈N∗

H 4m(ζ∓ 

> j

), with H 4m(ζ∓ 

> j

) ∝ | ζ∓|2mr−4m 

> e

.948 Tristan Ozuch 

3.3.2. Extension of the first asymptotic terms. As in Section 2, we define 2-tensors satisfying the following equations for ( oj,k )k a basis of 

O(eh ζ ±

> j

) and λkj ∈ R as in (22): (69) 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

hj, 2 = ∑

> k

λjkoj,k 

hj, 2 = Hj, 2 + O(|ζ±|2 · | ζ∓ 

> j

|2r−2+  

> e

),

∫

> S2

〈hj, 2, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3}

for Hj, 2 as in (67) and we have a converging development in a neighborhood of infinity. (70) hj, 2 = Hj, 2 + H 4 

> j, 2

+ ∑

> m2

H 4mj, 2 , with H 4mj, 2 ∝ | ζ±|2|ζ∓|2mr2−4m 

> e

.We then define the extension of the obstructions o4 

> j,m

for m ∈ { 1, 2, 3}

as the unique solutions to the following equation as in (34): (71) 

⎧⎪⎨⎪⎩

Pg±o4 

> j,m

∈ O(go),

o4 

> j,m

= O4 

> j,m

+ O(r−2− 

> e

) for any  > 0 at the singular point j

o4 

> j,m

⊥ O(go)for O4 

> j,m

∝ | ζ∓ 

> j

|r−4 

> e

and O4 

> j,m, 2

∝ | ζ±|2|ζ∓ 

> j

|r−2 

> e

the asymptotic term of the infinitesimal variation of h2 of (70) as eh ζ ∓

> j

is perturbed in the direction 

oj,m like in Section 2. For the first approximation term on M±,

⎧⎪⎪⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎪⎪⎩

Pg±h4 = ∑

> k

λjko4 

> j,k

+ ∑

> l

νlvl,h4 = H 4(ζ∓ 

> j

) + H 4 

> j, 2

+ O(|ζ±|2 · | ζ∓|2r− 

> e

)for any  > 0 at the singular point j, h4 ⊥ O(go)(72) for H 4(ζ∓ 

> j

) as in (68) with H 4 

> j, 2

determined in (70) and we have a converging development (73) h4 = H 4(ζ∓ 

> j

) + H 4 

> j, 2

+ ∑

> m2

H 4

> j, 2m

Higher order obstructions to the desingularization 949 in a neighborhood of each singular point j, with H 4 

> j, 2m

∝ | ζ∓ 

> j

|2|ζ±|2r2m−4 

> e

.Let us come back to the development (67) of g± at a singular point 

j ∈ S∓ and the term Hj, 4. We know that Hj, 4 ∝ | ζ±|2r4 

> e

and satisfies 

PeHj, 4 + Q(2)  

> e

(Hj, 2, H j, 2) = 0 .

Since Hj, 2 ∝ | ζ±|2r2

> e

, one would therefore expect by homogeneity to have 

Hj, 4 ∝ | ζ±|4r4 

> e

instead of the above Hj, 4 ∝ | ζ±|2r4

> e

. The reason is that 

Hj, 4 might have a harmonic part in |ζ±|2r4 

> e

while its part compensating the quadratic terms in Hj, 2 is ∝ | ζ±|4r4

> e

. By Lemma A.5 in the Appendix, there exists ˚Hj, 4 such that ˚Hj, 4 ∝ | ζ±|2r4 

> e

such that Hj, 4 − ˚Hj, 4 ∝ | ζ±|4r4 

> e

and satisfying Pe ˚Hj, 4 = 0. The crucial thing to note is that the extension of the harmonic part ˚Hj, 4 on eh ζ ∓

> j

does not induce any obstruction by [Biq16, (25), proof of Lemma 9]. This will ensure that we can indeed “see” the second obstruction μj, 1 = 0 for all j. More precisely, there exists ˚hj, 4 for which we have: (74) 

⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩

Peh ζ∓

> j

˚hj, 4 = 0 ˚hj, 4 = ˚Hj, 4 + O(|ζ±|2 · | ζ∓ 

> j

|2r

> e

), for any  > 0

∫

> S2

〈˚hj, 4, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3}.

We can therefore define the following 2-tensors on each ( T ∗S2, eh ζ ∓

> j

): 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

hj, 4 + Q(2) 

> eh ζ∓
> j

(hj, 2, h j, 2) = ∑

> k

μjkoj,k 

hj, 4 = Hj, 4 + H 4 

> j, 4

+ O(|ζ±|2 · | ζ∓ 

> j

|2r−2+  

> e

) for any  > 0,

∫

> S2

〈hj, 4, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3}

(75) where H 4 

> j, 4

is defined in (73) and satisfies 

PeH 4 

> j, 4

+ Q(2)  

> e

(Hj, 4, H 4(ζ∓ 

> j

)) + Q(2)  

> e

(Hj, 2, H 4

> j, 2

) + Q(3)  

> e

(Hj, 2, H j, 2, H 4(ζ∓ 

> j

)) = 0 which ensures that (75) has a unique solution as in Section 2. The coefficients 

μjk are the same as in (23), and one has (76) 

∥∥∥∑

> k

μjkoj,k 

∥∥∥L2(eh ζ∓ 

> j
> )

= O(|ζ±|4|ζ∓|2).950 Tristan Ozuch Remark that the factor |ζ±|4 comes from the previous discussion about extending a harmonic tensor ˚H4 and the difference between H 4 − ˚H4 ∝|ζ ±|4r4

> e

.We will need to extend higher order terms of the orbifold and ALE in order to produce a better approximation of the Einstein modulo obstructions perturbation of gDζ,v . We have to obtain good enough controls to “see” an obstruction of the same order as in (76). 

3.3.3. Extension of the higher order terms. We then also extend the obstructions of the orbifold g± to the Eguchi-Hanson metrics to ensure a good approximation. Consider the development of vl ∈ O(g±) at the singu-lar point j: vl = Vj,l, 0 +Vj,l, 2 +Vj,l, 4 +Vj,l, 6 +O(‖vl‖L2 ·| ζ±|2r8

> e

), we define the extensions vj,l, 0 = Vj,l, 0 + O(|ζ∓|2r−4+  

> e

), vj,l, 2 = Vj,l, 2 + O(|ζ±|2|ζ∓|2r−2+  

> e

)and vj,l, 4 = Vj,l, 4 + O(|ζ±|2|ζ∓|2r

> e

) for all  > 0 satisfying: 

Peh ζj vj,l, 0 = 0 ,

where there are no obstructions by Lemma 2.7, 

Peh ζj vj,l, 2 + Q(2) 

> eh ζj

(h2, vj,l, 0) ∈ O(eh ζ ∓

> j

) and 

Peh ζj vj,l, 4 + Q(2) 

> eh ζj

(hj, 2, vj,l, 2) + Q(2) 

> eh ζj

(hj, 4, vj,l, 0) + Q(3) 

> eh ζj

(hj, 2, h j, 2, vj,l, 0)

∈ O(eh ζ ∓

> j

),

and we will take the solutions which are orthogonal to O(eh ζ ∓

> j

) for the 

L2-product on S2 induced by eh ζ ∓

> j

.Like in the decomposition for Hj, 4, from the 2-tensor Hj, 6 of (67) there exists ˚Hj, 6 ∝ | ζ±|2r6 

> e

for which we have Hj, 6 − ˚Hj, 6 ∝ | ζ±|4r6

> e

, and (77) Pe ˚Hj, 6 = 0 ,

Indeed, considering the quadratic 2-tensor Hj, 6 satisfying 

PeHj, 6 + Q(2)  

> e

(Hj, 2, H j, 4) + Q(3)  

> e

(Hj, 2, H j, 2, H j, 2) = 0 ,

as |ζ ±| → 0, one finds a 2-tensor ˚Hj, 6 satisfying (77) and Hj, 6 − ˚Hj, 6 ∝|ζ ±|4r6

> e

, since Hj, 2 ∝ | ζ+|2r2 

> e

and Hj, 4 ∝ | ζ+|2r4 

> e

by Lemma A.5 in the Appendix. Higher order obstructions to the desingularization 951 

Lemma 3.15. There exists a unique 2-tensor ˚hj, 6 satisfying the following identity: 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

˚hj, 6 − ∑

> l

νlvj,l, 0 = 0 ˚hj, 6 = ˚Hj, 6 + ˚H 4 

> j, 6

+ O(|ζ±|2 · | ζ∓ 

> j

|2r−4+  

> e

) for any  > 0

∫

> S2

〈˚hj, 6, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3},

(78) 

where ˚H 4 

> j, 6

∝ | ζ±|2|ζ∓|2r2 

> e

satisfies Pe ˚H 4 

> j, 6

= −Q(2)  

> e

( ˚Hj, 6, H 4(ζ∓ 

> j

)) + ∑ 

> l

νlVj,l, 0

while the restriction of the coefficients of ˚H 4 

> j, 6

in a basis of the covering R4,once restricted to S3 are L2(S3)-orthogonal to the eigenfunctions associated to the second eigenvalue of the Laplacian on S3.

Remark 3.16. Note that ˚H 4 

> j, 6

is different from H 4 

> j, 6

defined in (73) . They are both ∝ | ζ±|2|ζ∓|2r2

> e

, and so is their difference. Proof. Let ˚Hj, 6 be as in (77). The term H 4 

> j, 6

in the development (73) satisfies for all  > 0: (79) PeH 4 

> j, 6

+ Q(2)  

> e

( ˚Hj, 6, H 4(ζ∓)) − ∑

> l

νlVj,l, 0 = O(|ζ±|4|ζ∓|2r

> e

),

since we have Hj, 6 − ˚Hj, 6 ∝ | ζ±|4r6

> e

, Hj, 2 ∝ | ζ±|2r2 

> e

and Hj, 4 ∝ | ζ±|2r4

> e

.Thanks to Lemma A.5, we therefore find ˚H 4 

> j, 6

with ˚H 4 

> j, 6

∝ | ζ±|2|ζ∓|2r2

> e

satisfying (80) Pe ˚H 4 

> j, 6

+ Q(2)  

> e

( ˚Hj, 6, H 4(ζ∓)) − ∑

> l

νlVj,l, 0 = 0 .

The 2-tensor ˚H 4 

> j, 6

is defined by (80) up to the harmonic quadratic 2-tensors on R4/Z2, and we choose the unique solution such that the restriction of the coefficients of ˚H 4 

> j, 6

in a basis of the covering R4, once restricted to S3 are 

L2(S3)-orthogonal to the eigenfunctions associated to the second eigenvalue of the Laplacian on S3.Without loss of generality by rescaling and by acting on Hj, 6, ˚Hj, 6 and 

Vj, 0 by an element of O(4) \SO (4), we will study the existence of ˚hj, 6 and the vanishing of the associated obstructions on eh , that is, as if we had 

ζ± 

> j

= (1 , 0, 0) +.952 Tristan Ozuch 

Remark 3.17. This may change the orientation and in particular makes the curvature of ˚Hj, 6 become selfdual. This will let us use the more convenient usual Eguchi-Hanson metric in our computations. 

For a smooth cut-off function χ supported at the infinity of eh we have 

Peh (χ( ˚Hj, 6 + ˚H 4

> j, 6

)) − ∑ 

> l

νlvj,l, 0 = O(|ζ±|2r−4 

> e

). By [Biq13, Proposition 2.1], one can find a smooth 2-tensor h′ decaying at infinity such that 

Peh (χ( ˚Hj, 6 + ˚H 4

> j, 6

) + h′) − ∑

> l

νlvj,l, 0 ∈ O(eh ), with 

∥∥Peh 

(

χ( ˚Hj, 6 + ˚H 4

> j, 6

) + h′)

− ∑

> l

νlvj,l, 0

∥∥r−2    

> eh Cαβ(eh )

 C|ζ±|2

for some C > 0 depending on the metric eh only. There now remains to prove that the obstruction actually vanishes. For this, again by [Biq13, Proposition 2.1], we need to prove that for all k ∈{1, 2, 3}

∫ 

> T∗S2

〈Peh (χ( ˚Hj, 6 + ˚H 4

> j, 6

)) − ∑

> l

νlvj,l, 0 , ok

〉

> eh

dv eh = 0 .

Let us use the formalism of [Biq16] in order to show this. Let us denote Ω the closed anti-selfdual 2-form generating of the L2-cohomology of eh as in [Biq13, (5)]. We will need its asymptotics at infinity: (81) Ω = θ−

> 1

r4 − θ− 

> 1

+ 12 ω+1

r8 + O(r−12  

> e

)= d

(

dC( 1

r2

)

+ α1

4r6 + O(r−11  

> e

)

)

,

where dC is the operator defined as dC = 12iπ (∂ − ∂) in complex geometry. As in the first Section, we use the identification of traceless 2-tensors and (commuting) compositions of a selfdual and an anti-selfdual 2-form, see Remark 1.13. We will use this on both the flat metric e for which a basis of Ω +(e) is ( ω+ 

> k

)k∈{ 1,2,3} and for the Eguchi-Hanson metric, we will use the basis (˜ ω+ 

> k

)k∈{ 1,2,3} of Ω +(eh ) satisfying ˜ ω+ 

> k

= ω+ 

> k

+ O(r−4 

> e

) at infinity. We can therefore rewrite 

• ˚Hj, 6 = ∑ 

> k

˜φkj, 6 ◦ ˜ω+ 

> k

for ˜φkj, 6 ∈ Ω−(eh ), as well as ˚Hj, 6 = ∑ 

> k

φkj, 6 ◦ ω+

> k

for φkj, 6 ∈ Ω−(e), Higher order obstructions to the desingularization 953 

• ˚H 4 

> j, 6

= ∑ 

> k

˜φ4,k j, 6 ◦ ˜ω+ 

> k

for ˜φ4,k j, 6 ∈ Ω−(eh ), as well as ˚H 4 

> j, 6

= ∑ 

> k

φ4,k j, 6 ◦ ω+

> k

for φ4,k j, 6 ∈ Ω−(e), 

• ∑ 

> l

νlvj,l, 0 = ∑ 

> k

˜V kj, 0 ◦ ˜ω+ 

> k

, for ˜V kj, 0 ∈ Ω−(eh ) as well as ∑ 

> l

νlVj,l, 0 =

∑ 

> k

V kj, 0 ◦ ω+ 

> k

, for V kj, 0 ∈ Ω−(e), 

• ok = Ω ◦ ˜ω+ 

> k

see [Biq16], 

• recall also that H 4 = − θ− 

> 1◦ω+1
> 2r4
> e

.This lets us rewrite several of the above identities: 

• the equality (77) becomes (82) (d−d∗)eφkj, 6 = 0 , or equivalently ( dd ∗)eφkj, 6 ∈ Ω+(e)

• the equality (80) becomes: (83) (d−d∗)eh (φkj, 6 + φ4,k j, 6 ) − ˜V k 

> 0

= O(r−4 

> e

)

• a direct extension of [Biq16, Lemme 3] to the computation of the bi-linear terms of the selfdual part of the Riemannian curvature. Let 

φ := ∑ 

> k

φk ◦ ω+ 

> k

and ψ := ∑ 

> k

ψk ◦ ω+ 

> k

be infinitesimal Ricci-flat defor-mations of e which satisfy Be(φ) = Be(ψ) = 0. Assume additionally that tr eφ = 0 and d ∗ dφ k = 0, then the second variation of the selfdual part of the curvature at e in the directions φ and ψ, is: 

R+,(2)  

> e

(φ, ψ ) = − 12 [ae(φ), a e(ψ)] +,

where ae(φ) and ae(ψ) are respectively the first variations of the connection on the bundle of selfdual 2-forms at e in the directions 

φ and ψ. In the particular case of φ = H 4 and ψ = ˚Hj, 6, since 

ae(H 4) = − ∗ d( θ−

> 1
> 2r4
> e

) = 0, we find (84) R+,(2)  

> e

( ˚Hj, 6, H 4) = 0 .

• the equalities (80) and (84) imply that in a neighborhood of infinity we have 

dd ∗

> eh

( ˜φkj, 6 + ˜φ4,k j, 6

) − ˜V k 

> 0

= ( d+d∗)eφkj, 6 + ( d+d∗)eφ4,k j, 6 + O(r−4 

> e

)= −deR+( ˚Hj, 6) − deR+( ˚H 4

> j, 6

) + O(r−4 

> e

).

(85) 954 Tristan Ozuch Following the integration by parts of the proof of [Biq16, Lemma 7], since Ω ∈ Ω−(eh ), by (81) and by (85), we have 1

‖ok‖L2

∫ 

> T∗S2

〈Peh (χ( ˚Hj, 6 + ˚H 4

> j, 6

)) − ∑

> l

νlvj,l, 0 , ok

〉

> eh

dv eh 

= − 1

‖Ω‖L2

∫ 

> T∗S2

Ω ∧ (dd ∗

> eh

( ˜φkj, 6 + ˜φ4,k j, 6

) − ˜V k

> 0

)

= − 1

‖Ω‖L2

∫ 

> T∗S2

d

(

dC( 1

r2

> e

)

+ α1

4r6

> e

+ O(r−11  

> e

)

)

∧

(

dd ∗

> eh

( ˜φkj, 6 + ˜φ4,k j, 6

) − ˜V k

> 0

)

= − 1

‖Ω‖L2

lim 

> r→+∞

∫

> {re=r}

(

dC( 1

r2

> e

)

+ α1

4r6

> e

)

∧ ((d+d∗)eφkj, 6 + ( d+d∗)eφ4,k j, 6

)

= + 1

‖Ω‖L2

lim  

> r→+∞

r4

∫

> {re=1 }

dC( 1

r2

> e

)

∧ deR+( ˚Hj, 6)( ω+ 

> k

)+ 1

‖Ω‖L2

lim 

> r→+∞

∫

> {re=1 }

α1

4r6

> e

∧ deR+( ˚Hj, 6)( ω+ 

> k

)+ 1

‖Ω‖L2

lim 

> r→+∞

∫

> {re=1 }

dC( 1

r2

> e

)

∧ deR+( ˚H 4

> j, 6

)( ω+ 

> k

).

(86) Now, the coefficients of deR+( ˚Hj, 6)( ω+ 

> k

) are harmonic functions in r4

> e

and their restrictions to a sphere {re = r} = r · S3/Z2 are eigenfunctions of the Laplacian associated to the second eigenvalue on S3/Z2 (fourth eigen-value on S3). They are therefore L2(S3/Z2)-orthogonal to the coefficients of the restriction of dC( 1

> r2
> e

) or α1

> 4r6
> e

to S3/Z2.Similarly, by the two formulas of [Biq13, Proposition 2.1] and [Biq16, Lemme 7], we know that ∫ 

> {re=r}

dC( 1

> r2
> e

) ∧ deR+( ˚H 4

> j, 6

)( ω+ 

> k

) is proportional to 

∫

> S3/Z2

〈 ˚H 4

> j, 6

, O 4

> k

〉dv S3/Z2, where O4 

> k

is explicited in (14) and once restricted to a sphere {re = r}, O4 

> k

has eigenfunctions of the Laplacian on S3/Z2

associated to the first eigenvalue as coefficients. By construction, ˚H 4 

> j, 6

is orthogonal to this eigenspace. The obstructions therefore vanish. We then extend the next term of the development of om, for m ∈ { 1, 2, 3}

to the orbifold. Recall that oj,m = O4 

> j,m

+ O8 

> j,m

+ O(|ζ|5r−12  

> e

), with O4 

> j,m

∝|ζ ∓|r−4 

> e

and O8 

> j,m

∝ | ζ∓|3r−8 

> e

. We can therefore find by the general method Higher order obstructions to the desingularization 955 of [Biq13, Section 10] o8 

> j,m

satisfying 

⎧⎪⎪⎨⎪⎪⎩

Pg±o8 

> j,m

+ Q(2) 

> g±

(o4

> j,m

, o4

> j,m

) + Q(2) 

> g±

(o4

> j,m

, h 4) ∈ O(g±)

o8 

> j,m

= O8

> m

(ζ∓ 

> j

) + O(|ζ±|2|ζ∓|4r−6− 

> e

) for any  > 0 at the point j

o8 

> j,k

⊥ O(go).

(87) We then need to come back to the orbifold in order to find: 

⎧⎪⎪⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎪⎪⎩

Pg±h8 + Q(2) 

> g±

(h4, h 4) − ∑

> k

λjko8 

> j,m

∈ O(g±)

h8 = H 8(ζ∓ 

> j

) + H 8 

> j, 2

+ H 8 

> j, 4

+ ˚H 8 

> j, 6

+ ˚H 8 

> j, 8

+ O(|ζ±|2|ζ∓|4r−2− 

> e

),

∀ > 0 at jh8 ⊥ O(go)(88) with H 8(ζ∓ 

> j

), H 82 , H 84 and ˚H 86 from (67), (70), and the asymptotic terms of (75) and (78) and ˚H 8 

> j, 8

∝ | ζ±|2|ζ∓|4. We moreover have a converging development 

h8 = H 8(ζ∓ 

> j

) + H 8 

> j, 2

+ H 8 

> j, 4

+ ˚H 8 

> j, 6

+ ˚H 8 

> j, 8

+ ∑

> m5

H 8

> j, 2m

with H 8 

> j, 2m

∝ | ζ±|2|ζ∓|4r2m−8 

> e

in a neighborhood of j. We moreover have the control (89) ∥∥Pg±h8 + Q(2) 

> g±

(h4, h 4) − ∑

> k

λjko8

> j,m

∥∥L2(g±) = O(|ζ±|2 · | ζ∓ 

> j

|4)which will be sufficient on the orbifold. As for ˚Hj, 6 defined in (77) from Hj, 6, one finds ˚Hj, 8 from Hj, 8 of (67). More precisely, we have Hj, 8 − ˚Hj, 8 ∝ | ζ±|4r8 

> e

where ˚Hj, 8 ∝ | ζ±|2r8 

> e

satisfies 

Pe ˚Hj, 8 = ∑ 

> l

νlVj,l, 2.

As in Lemma 3.15, we prove that one can extend ˚Hj, 8 on eh ζ ∓

> j

without obstruction. 

Lemma 3.18. There exists a unique 2-tensor ˚hj, 8 satisfying the following 956 Tristan Ozuch 

identity: 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

˚hj, 8 − ∑

> l

νlvj,l, 2 = 0 ˚hj, 8 = ˚Hj, 8 + ˚H 4 

> j, 8

+ ˚H 8 

> j, 8

+ O(|ζ±|2 · | ζ∓ 

> j

|2r−6+  

> e

) for any  > 0

∫

> S2

〈˚hj, 8, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3},

(90) 

where ˚H 4 

> j, 8

∝ |ζ±|2|ζ∓|2r4 

> e

satisfies Pe ˚H 4 

> j, 8

= −Q(2)  

> e

( ˚Hj, 8, H 4(ζ∓ 

> j

)) + 

∑ 

> l

νlVj,l, 2, and where ˚H 8 

> j, 8

∝ | ζ±|2|ζ∓|4 satisfies 

Pe ˚H 8 

> j, 8

= −Q(2)  

> e

( ˚Hj, 8, H 8(ζ∓ 

> j

)) − Q(2)  

> e

( ˚Hj, 8, H 4(ζ∓ 

> j

), H 4(ζ∓ 

> j

)) + ∑

> l

νlV 4

> j,l, 2

,

for V 4 

> j,l, 2

defined by vj,l, 2 = Vj,l, 2 + V 4 

> j,l, 2

+ o(|ζ±|2|ζ∓|4r−6 

> e

)

Proof. The proof of the existence of ˚hj, 8 satisfying 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

˚hj, 8 − ∑

> l

νlvj,l, 2 ∈ O(eh )˚hj, 8 = ˚Hj, 8 + ˚H 4 

> j, 8

+ ˚H 8 

> j, 8

+ O(|ζ±|2 · | ζ∓ 

> j

|6r−6+  

> e

) for any  > 0

∫

> S2

〈˚hj, 8, oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3},

(91) is very similar to that of ˚hj, 6 of Lemma 3.15 once ˚H 4 

> j, 8

and ˚H 8 

> j, 8

are identified like ˚H 4 

> j, 6

is in Lemma 3.15. We will therefore omit the proof. Let us focus on showing that the obstructions vanish. Again, after rescal-ing and acting by a rotation in O(4) \SO (4), we will work on the usual metric 

eh . Mimicking the computation of (86), and dropping the terms not con-tributing to the boundary term, we find 

〈

Peh 

(χ( ˚Hj, 8 + ˚H 4 

> j, 8

+ ˚H 8

> j, 8

)) − ∑

> l

νlvj,l, 2 , ok

〉

(92) = lim 

> r→+∞

(∫

> {re=r}

(

dC( 1

r2

> e

)

+ α1

4r6

> e

)

∧ deR+( ˚Hj, 8)( ω+ 

> k

)Higher order obstructions to the desingularization 957 +

∫

> {re=r}

dC( 1

r2

> e

)

∧ deR+( ˚H 4

> j, 8

)( ω+ 

> k

)

)

= lim 

> r→+∞

(

r6

∫

> {re=1 }

dC( 1

r2

> e

)

∧ deR+( ˚Hj, 8)( ω+ 

> k

)+ r2

∫

> {re=1 }

α1

4r6

> e

∧ deR+( ˚Hj, 8)( ω+ 

> k

)+ r2

∫

> {re=1 }

dC( 1

r2

> e

)

∧ deR+( ˚H 4

> j, 8

)( ω+ 

> k

)

)

because of the homogeneity of each term: 

• dC

( 1

> r2
> e

)

∝ r−3 

> e

,

• α1

> 4r6
> e

∝ r−7

> e

• deR+( ˚Hj, 8)( ω+ 

> k

) ∝ | ζ±|2r6

> e

• deR+( ˚H 4

> j, 8

)( ω+ 

> k

) ∝ | ζ±|2|ζ∓|2r2

> e

.We see that the obstruction either vanishes or is infinite. However 〈Peh 

(χ( ˚Hj, 8 + ˚H 4 

> j, 8

+ ˚H 8

> j, 8

)) − ∑ 

> l

νlvj,l, 2, ok

〉 is finite because both 

Peh 

(χ( ˚Hj, 8+ ˚H 4

> j, 8

+ ˚H 8

> j, 8

))−∑ 

> l

νlvj,l, 2 and ok are in L2(eh ). The obstruction therefore necessarily vanishes. Similarly, there exists ˚hj, 10 satisfying: for ˚Hj, 10 the harmonic part of 

Hj, 10 from (67) and ˚H 4 

> j, 10

and ˚H 8 

> j, 10

associated from the development of h4

of (72) and h8 of (88): 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ∓

> j

˚hj, 10 − ∑

> l

νlvj,l 4 ∈ O(eh ζ ∓

> j

)˚hj, 10 = ˚Hj, 10 + ˚H 4 

> j, 10

+ ˚H 8 

> j, 10

+ O(|ζ±|2 · | ζ∓ 

> j

|6r−2+  

> e

) for any  > 0

∫

> S2

〈˚hj, 10 ,oj,k 〉eh ζ∓

> j

dv eh ζ∓  

> j|S2

= 0 for all k ∈ { 1, 2, 3},

(93) with ‖Peh ζ∓

> j

˚hj, 10 − ∑

> l

νlvj,l 4‖L2(eh ζ∓ 

> j
> )

= O(|ζ±|2|ζ∓|5).(94) 

Remark 3.19. The obstruction may not vanish here, but it is small enough for our present purpose: it is better than μ1 ∼ | ζ±|4|ζ∓|2 when ζ± ∼ ζ∓ as for transverse or nondegenerate desingularizations. 958 Tristan Ozuch Let us define 

eh [10]  

> ζ∓
> j

:= eh ζ ∓

> j

+ hj, 2 + hj, 4 +

> 5

∑

> m=3

˚hj, 2m

which is a metric for re  1, and 

g[8]  

> ±

:= g± + h4 + h8

which is a metric for |ζj| 12  re. On the region where |ζj| 12  re  1, we have (95) rk

> e

∣∣∣∇k(eh [10]  

> ζ∓
> j

− g[8] 

> ±

)∣∣∣  C

(

|ζ±|2r12  

> e

+ |ζ∓ 

> j

|6r−12  

> e

+ |ζ±|2|ζ∓ 

> j

|2r2)

,

which is minimized at re = |ζ±|− 112 · | ζ∓ 

> j

| 14 , in a neighborhood of the singular point j.

Proof of Proposition 3.14. We define an approximate desingularization gAL,ζ 

as the gluing of eh [10]  

> ζ∓
> j

to g[8]  

> ±

at the singular point j and with a gluing scale at 

|ζ±|− 112 · | ζ∓ 

> j

| 14 < r e < 2|ζ±|− 112 · | ζ∓ 

> j

| 14 . As in Definition 2.16, we will denote ˜O(gAL,ζ ) the space of the infinitesimal deformations of ( L, ζ ± 

> i

, ζ ∓ 

> j

)  → gAL,ζ .

Remark 3.20. The space ˜O(gAL,ζ ) is different from the space ˜O(gD) of [Ozu19b] but yields better estimates. The results of [Ozu19b] with ˜O(gD)

therefore hold with ˜O(gAL,ζ ).

Denote oAL,ζ as the element of ˜O(gAL,ζ ) associated to the same variations of 

L and the ζ± 

> i

as ∑ 

> l

νlvl(L, ζ ) ∈ O(g±) defined in (72), and to the variations of each ζ∓ 

> j

associated to ∑

> k

(λjk(L, ζ ) + μjk(L, ζ )) oj,k . From the construction of the eh [10]  

> ζ∓
> j

and g[8]  

> ±

we find: 1. on the region where gAL,ζ = eh ζ ∓

> j

+ hj, 2 + hj, 4 + ∑5 

> m=3

˚hj, 2m, we have: (Ric −Λ)( gAL,ζ ) = ∑

> k

(λjk + μjk + O(|ζ±|2|ζ∓|5))oj,k 

+ ∑

> l

(νl + O(|ζ±|2|ζ∓|4))( vj,l, 0 + vj,l, 2 + vj,l, 4)+ O(|ζ±|4r4 

> e

+ |ζ±|2r10  

> e

),Higher order obstructions to the desingularization 959 2. on the region where gAL,ζ = g± + h4 + h8, we have: (Ric −Λ)( gAL,ζ ) = ∑

> k

(λjk + μjk + O(|ζ±|2|ζ∓|5))(o4 

> j,k

+ o8

> j,k

)+ ∑

> l

(νl + O(|ζ±|2|ζ∓|4)) vl

+ O(|ζ∓|6r−14  

> e

)3. on the gluing region at j, we find: (Ric −Λ)( gAL,ζ ) = ∑

> k

(λjk + μjk + O(|ζ±|2|ζ∓|5))oj,k 

+ ∑

> l

(νl + O(|ζ±|2|ζ∓|4)) vl

+ O(|ζ±|4r4 

> e

+ |ζ±|2r10  

> e

+ |ζ∓|6r−14  

> e

).

Let us finally mention the controls on the elements of ˜O(gAL,ζ ) which let us conclude. Recall that for ζj, (k) ∈ Ω∓, we have oj,k = ∂ζj, (k)eh ζ ∓

> j

, and consider 

vl one of the elements of the orthonormal basis of O(go). On the region where gAL,ζ = eh [10]  

> ζ∓
> j

, where rD < |ζ±|− 112 · | ζ∓ 

> j

| 14 : r2

> D

∣∣∂ζj, (k)gAL,ζ − oj,k 

∣∣eh ζ∓

> j



C|ζ±|2|ζ∓|2r−2 

> D

, on the region where gAL,ζ = g[8]  

> ±

, where rD > 2|ζ±|− 112 · | ζ∓ 

> j

| 14

r2

> D

∣∣∂ζj, (k)gAL,ζ − (o4 

> j,k

+ o8

> j,k

)∣ ∣g±

< C (|ζ±|6r−12  

> D

+ |ζ±|2|ζ∓|2r−2

> D

).

We have similar controls between ∂vlgAL,ζ and vl where gAL,ζ = g[8]  

> ±

and between ∂vlgAL,ζ and vj,l, 0 + vj,l, 2 + vj,l, 4 where gAL,ζ = eh [10]  

> ζ∓
> j

.As a consequence, using the fact that on the gluing region where 

|ζ ±|− 112 |ζ∓ 

> j

| 14  rD  |ζ±|− 112 · | ζ∓ 

> j

| 14 , the difference between the metrics is controlled by (95) we globally find 

‖ΦgAL,ζ (gAL,ζ ) − oAL,ζ ‖r−2  

> DCαβ

 C|ζ±|1+ β 

> 12

|ζ∓|3− β 

> 4

.

which proves the statement of Proposition 3.14. 

3.3.4. Controls on the approximate Einstein modulo obstructions metric. By [Ozu19b], we can always solve the Einstein equation modulo obstructions. 960 Tristan Ozuch 

Definition 3.21 (Total Einstein modulo obstructions desingularization ˆ gL,ζ ).

For L ∈ GL (4 , R), and ζ small enough depending on L (as determined in [Ozu19b]), we define ˆgL,ζ as the unique metric satisfying for some  = (L) >

0 independent on ζ determined in [Ozu19b]: 

• ‖ ˆgL,ζ − gAL,ζ ‖C 2,α β, ∗ (gAL,ζ ) <  ,

• ΦgAL,ζ (ˆ gL,ζ ) ∈ ˜O(gAL,ζ ), and 

• ˆgL,ζ − gAL,ζ is L2(gAL,ζ )-orthogonal to ˜O(gAL,ζ ).

First, we have a good control on the projection on ˜O(gAL,ζ ). The proof is analogous to the proof of Lemma 2.18 above so we omit it, compare also with [Biq13, Lemma 13.2]. 

Lemma 3.22. Let h be a symmetric 2-tensor on M , and let oA ∈ ˜O(gAL,ζ ),then we have the following estimate, there exists C > 0 such that 

∣∣∣∣〈

PgDL,ζ h, oA〉

> L2(gDL,ζ )

∣∣∣∣  C|ζ±|2|ζ∓|1− β 

> 2

‖h‖C 0

> β, ∗

‖oA‖L2.

Replacing the control [Ozu20t, (4.46), Lemma 4.46] by the above Lemma 3.22 in the proof of [Ozu20t, Proposition 5.1], we get the following statement as a direct consequence. 

Lemma 3.23. There exists  > 0 and C > 0 such that we have 

(96) ‖ˆgL,ζ − gAL,ζ ‖C 2,α β, ∗ (gAL,ζ )  C∥∥ΦgAL,ζ (gAL,ζ ) − oAL,ζ 

∥∥r−2   

> DCαβ(gAL,ζ )

,

and moreover if the metric (M, ˆgL,ζ ) is an Einstein metric, then, we have 

‖oAL,ζ ‖L2(gAL,ζ )  C(‖ΦgAL,ζ (gAL,ζ ) − oAL,ζ ‖r−2    

> DCαβ(gAL,ζ )

+ |ζ∓|1− β 

> 2

|ζ±|2)

× ‖ ΦgAL,ζ (gAL,ζ ) − oAL,ζ ‖r−2   

> DCαβ(gAL,ζ )

.(97) Together with the control of Proposition 3.14, Lemma 3.23 implies both a control of the metric and the obstructions. 

Remark 3.24. For small ζ, we can essentially treat the obstructions com-ing from variations of different ζ± 

> i

, ζ∓ 

> j

or L as orthogonal to each other. Indeed, for the different infinitesimal variations, we have the following con-trols showing where each of the infinitesimal deformation has most of its mass: 

• | ∂z∓

> j

gALk,ζ k|gALk ,ζ k

 C|ζ∓ 

> j

|‖ ∂z∓

> j

gALk,ζ k‖L2

(|ζ∓ 

> j

| 12 + dgALk ,ζ k

(j, . ))−4Higher order obstructions to the desingularization 961 

• | ∂z±

> i

gALk,ζ k|gALk ,ζ k

 C|ζ± 

> i

|‖ ∂z±

> i

gALk,ζ k‖L2

(|ζ± 

> i

| 12 + dgALk ,ζ k

(i, . ))−4

• | ∂KgALk,ζ k|gALk ,ζ k

 C‖∂KgALk,ζ k‖L2.Estimating the L2-product of two of the above infinitesimal, we see that as 

|ζ| → 0, they become arbitrarily close to being orthogonal. 

Corollary 3.25. We have the following controls: 

• ‖ ˆgL,ζ − gAL,ζ ‖C 2,α β, ∗ (gAL,ζ )  C|ζ±|1+ β 

> 12

|ζ∓|3− β 

> 4

,

• and ‖oAL,ζ ‖L2(gAL,ζ )  C|ζ±|3+ β 

> 12

|ζ∓|4− 3β 

> 4

which rewrites as, for all j ∈

S∓ and k ∈ { 1, 2, 3}, for any 0 < β < 1 (chosen small enough) 

(98) λjk(L, ζ ) + μjk(L, ζ ) = O(|ζ±|2|ζ∓|5 + |ζ±|3+ β 

> 12

|ζ∓|4− 3β 

> 4

),

with |ζ ±|2|ζ∓|5 from (94) , and for all l,

(99) νl(L, ζ ) = O(|ζ±|2|ζ∓|4 + |ζ±|3+ β 

> 12

|ζ∓|4− 3β 

> 4

),

where the additional error in |ζ±|2|ζ∓|4 comes from (89) .

Remark 3.26. Recall that a priori, we only had λjk(L, ζ ) = O(|ζ±|2|ζ∓|),

μjk(L, ζ ) = O(|ζ±|4|ζ∓|2) and νl = O(|ζ±|2|ζ∓|2).

3.4. Obstruction to the total desingularization 

We will now prove that there are obstructions to the Gromov-Hausdorff desingularization of T4/Z2 by Einstein metrics. 

Proposition 3.27. Assume that there exists a sequence of Einstein modulo obstructions metrics (ˆ gLn,ζ n = gLn,ζ n)n∈N which are actually Einstein with 

ζn → 0 and Ln → L∞ where det( L∞) > 0. Up to taking a subsequence, we consider the following limits: ζ ∓   

> n,j
> |ζ∓
> n|

→ ζ∓∞,j , ζ ±   

> n,i
> |ζ±
> n|

→ ζ±∞,i and ζ ∓  

> n,j
> |ζ∓
> n,j |

→ φ∓∞,j , as well as the limit 

(100) RL∞,ζ ±∞ := lim 

> n→∞

1

|ζ± 

> n

|2 Rg±,n = lim 

> n→∞

1

|ζ± 

> n

|2 RgA

> ±,n

.

Then, 1. one always has 

(101) RL∞,ζ ±∞(j)( φ∓∞,j ) = 0 ,962 Tristan Ozuch 

for all the deformations (0 , z ±) of (L∞, ζ ±∞), we have 

(102) ∑

> j∈S±

〈

∂(0 ,z ±)RL∞,ζ ±∞(j)( ζ∓∞,j ), ζ ∓∞,j 

〉

= 0 ,

and for all the deformations (K, 0) of (L∞, ζ ±∞), and (vl)l an orthonor-mal basis of O(g±) and νl(L∞, ζ ∞) the obstructions of (72) , we have 

(103) ∑

> l

〈∂(K, 0) g±, vl〉L2(g±)νl(L∞, ζ ∞) = 0 .

2. If we assume that the sequence (gLn,ζ n)n∈N is a nondegenerate or sta-ble sequence of Einstein desingularizations, then, one moreover has: 

(104) RL∞,ζ ±∞(j) = 0 at every j ∈ S∓.

Remark 3.28. The assumption det( L∞) > 0 for L∞ ∈ GL (4 , R) ensures that there is no collapsing and a bounded diameter in our degeneration and therefore that we stay in the context of [And89, BKN89, Ozu19a, Ozu19b]. 

Remark 3.29. When (101) is satisfied, from (41) , we have the following rewriting of the obstruction (103) :

(105) ∑

> j∈S±

〈

∂(K, 0) RL∞,ζ ±∞(j)( ζ∓∞,j ), ζ ∓∞,j 

〉

= 0 .

Proof of Proposition 3.27. Let us assume that there exists a sequence of Einstein modulo obstructions (ˆ gLn,ζ n = gLn,ζ n)n∈N which are Einstein with 

ζn → 0 and Ln → L∞ = Id. By compactness, up to taking a subsequence, for all j ∈ S∓ and all i ∈ S±, we have ζ ∓  

> n,j
> |ζ∓
> n,j |

→ ζ∓∞,j , ζ ±   

> n,i
> |ζ±
> n|

→ ζ±∞,i and    

> ζ∓
> n,j
> |ζ∓
> n,j |

→ φ∓∞,j as n → +∞. By (98) and (99), for any 0 < β < 1 (chosen small enough), we have (106) λjk(Ln, ζ n) + μjk(Ln, ζ n) = O(|ζ± 

> n

|2|ζ∓ 

> n

|5 + |ζ± 

> n

|3+ β 

> 12

|ζ∓ 

> n

|4− 3β 

> 4

),

and for all l,(107) νl(Ln, ζ n) = O(|ζ± 

> n

|2|ζ∓ 

> n

|4 + |ζ± 

> n

|3+ β 

> 12

|ζ∓ 

> n

|4− 3β 

> 4

),Higher order obstructions to the desingularization 963 We directly see from (106) that lim 

> n→∞

λjk(Ln, ζ n)

|ζ± 

> n

|2|ζ∓ 

> n

| = 0 because μjk(Ln, ζ n) = O(|ζ± 

> n

|4|ζ∓ 

> n

|2) which proves (101) by the value the obstruction (24) and the control of the curvature of Proposition 3.6. Similarly, from (107) we find lim 

> n→∞

νl(Ln, ζ n)

|ζ± 

> n

|2|ζ∓ 

> n

|2 = 0 which proves (103). In order to prove (102), we note that the constant part (the limit at the singular point) of ∂(0 ,z ±)g± scales like |ζ± 

> n

|2. Thanks to the expression (36) of the obstruction, this tells us that the obstruction induced by the constant part (the limit at the singular point) scales like 

|ζ ± 

> n

|4|ζ∓ 

> n

|2 because we have H 42 ∝ | ζ± 

> n

|2|ζ∓ 

> n

|2r−2 

> e

in the development (70). In the limit, we are left with the obstruction coming from the nonconstant part of ∂(0 ,z ±)g± whose interpretation in (41) yields the obstruction (102) using the control of the variations of the curvature (66). We conclude exactly as in the proof of Theorem 0.2 by using (106) as a replacement for (51). More precisely, if we assume towards a contradiction that the obstruction (104) is not satisfied, that is lim n→∞ μj, 1(Ln,ζ n)     

> |ζ±
> n|4|ζ∓
> n|2

= 0 is not satisfied, then since we have |Rg±| ∼ | ζ± 

> n

|2, the estimates (55) and (56) become 

λj

> 1

(L∞, φ n,j ) = O(|ζ± 

> n

|2|φn,j − φ∞,j |2), and 

∣∣(λj

> 2

(L∞, φ n,j ), λ j

> 3

(L∞, φ n,j ))∣ ∣  c|ζ± 

> n

|2|φn,j − φ∞,j |, for some c > 0.

As in the proof of Theorem 0.2, we find a contradiction using (106) for 

k = 2 , 3 and then k = 1. Similarly, as in the proof of Theorem 0.2 one can use the eigenvalue estimate of [Biq17] to deal with the stable situation thanks to the estimate of Corollary 3.25. 

Remark 3.30. Allowing some Eguchi-Hanson metrics to be glued at negli-gible scale might not preserve the obstruction R± = 0 at the associated point and might reduce the number of obstructions by 2 per such point. Indeed, 

R± is in the 5-dimensional space of traceless symmetric 2-tensors and the first obstructions λk = 0 , give 3 independent equations. But we will see that the scale being negligible means that we lose the 3 degrees of freedom. These situations should therefore be more obstructed even without the obstruction 

R± = 0 .964 Tristan Ozuch 

4. Explicit obstructions to the desingularization of T4/Z2

Let us now make the obstructions of Proposition 3.27 more explicit as the vanishing of polynomial functions of the ζ±, whose coefficients depend on the flat metric gL alone. Recall from (13) that the curvature of the Eguchi-Hanson metric eh ζ +

and by their first asymptotic term ζ +◦ρ(ζ)− 

> r4

has the form 12 πtr ρ(ζ)−⊗ρ(ζ)−

> r6

where ρ(ζ)− is defined in Definition 1.14. 

Note 4.1. During all of this section, we will often identify R3 and Ω+ or Ω−

thanks to the bases (ω± 

> i

)i∈{ 1,2,3}. This will make it more convenient to find identities relating different obstructions in Lemma 4.6 for instance. That is why we are defining the selfdual or anti-selfdual curvature-like quantities bx

and BLx on R3. We will also use the identification R3 ⊗ R3 ≈ Ω± ⊗ Ω± ≈

(Ω ±)∗ ⊗ Ω± ≈ End (Ω ±).

For x ∈ R4 and ζ, ζ ′ ∈ R3\{ 0}, we define bx(ζ, ζ ′) := 12 ρx(ζ)−⊗ρx(ζ ′)− 

> |x|6

,where ρx for x ∈ R4 is the rotation explicited in (8). Note that ρ−x = ( ρx)t =(ρx)−1 = ρx. For any z, z ′ ∈ R3, we have (108) 〈bx(ζ, ζ ′)z, z ′〉 := 12 〈ρx(ζ), z 〉〈 ρx(ζ′), z ′〉|x|6 .

We also define the following bilinear form with values in R3 ⊗ R3:(109) BLx (ζ, ζ ′) := πtr 

∑

> a∈Z4

bL(x−2a)(ζ, ζ ′)for x ∈ R4 and L a 4 × 4 matrix, where πtr is the projection on the traceless part. 

Lemma 4.2. Let (M±, g A

> ±

) be one of the partial desingularizations of T4/Z2

of Definition (3.5) . Then, for any j0 ∈ S− and any ζ ∈ R3 and the associated 

ζ − ∈ Ω− (thanks to the basis (ω− 

> i

)i∈{ 1,2,3}), we have 

(110) R−

> gA
> +

(j0)ζ− = ∑

> i∈S+

(BLj0−i(ζi, ζ i)ζ)−

where again BLj0−i(ζi, ζ i)ζ ∈ R3 and (BLj0−i(ζi, ζ i)ζ)− ∈ Ω−.Proof. Away from the glued Eguchi-Hanson metrics, gA 

> +

equals 

gL + ∑ 

> i∈S+

h4  

> ζ+
> i

where the h4  

> ζ+
> i

are explicited in (62). By Remark 3.4 and the formula (13), the induced curvature is therefore given by (110). Higher order obstructions to the desingularization 965 We have the following properties for BLx (ζ, ζ ′) for any x ∈ R4 and 

ζ, ζ ′ ∈ R3

1. BLx (ζ, ζ ′) = BLx (ζ′, ζ ),

2. BLx (ζ, ζ ′) = BL

> −x

(ζ, ζ ′), 3. BLx+a(ζ, ζ ′) = BLx (ζ, ζ ′) for a ∈ Z4,

Corollary 4.3. The obstruction (101) rewrites for all j0 ∈ S−,

(111) ∑

> i∈S+

〈BLj0−i(ζi, ζ i)ζj0, ζ j0

〉 = 0 .

and from (102) for j0 ∈ S− and an infinitesimal deformation of ζj0 in the direction zj0:

(112) ∑

> i∈S+

〈BLj0−i(zj0, ζ j0)ζi, ζ i

〉 = 0 .

For the value of the obstructions (105) , against a deformation K of the matrix L, denoting ∂KBLj−i the linearization of L  → BLj−i for i ∈ S+ and 

j ∈ S− at L and in the direction K, we have 

(113) ∑

> i∈S+

∑

> j∈S−

〈∂KBLj−i(ζi, ζ i)ζj, ζ j

〉 = 0 .

Finally, the obstruction (104) rewrites for any j0 ∈ S−:

(114) ∑

> i∈S+

BLj0−i(ζi, ζ i) = 0 

The analogous obstructions hold for the other orientation. 

Remark 4.4. The obstruction identified in [BK17] corresponds to the non-vanishing of the one obstruction 

∑

> i∈S+

∑

> j∈S−

〈BLj−i(ζi, ζ i)ζj, ζ j

〉 = 0 

(which is clearly implied by (111) ), in the particular situation where 

• L = Id ,

• the sets S± follow a chessboard pattern (see [BK17] or Section 4.3), 

• for all i ∈ S+, j ∈ S−, ζi = (1 , 0, 0) and ζj = (1 , 0, 0) .966 Tristan Ozuch 

Remark 4.5. If the Eguchi-Hanson metrics are glued at comparable scales, then: 

• the obstructions (111) correspond to 3|S+| equations for 3|S−| + 9 pa-rameters given by the |S−| vectors ζ− 

> j

and the matrix L,

• the obstructions (114) correspond to 5|S+| equations since R is sym-metric trace-free for 3|S−| + 9 parameters given by the |S−| vectors ζ−

> j

and the matrix L,

• the obstructions (113) are 9 equations, for the different deformations of the torus, for 3|S+| + 3 |S−| + 9 = 57 parameters, 

• the obstructions (112) are 3|S−| equations for 3|S+| + 9 parameters. Since we have analogous obstructions in the other orientation, we see that we a priori have many more obstructions to satisfy than parameters. We will reduce the number of these equations in the next section. 

4.1. Equivalent obstructions 

Let us show that many of the above equations are actually equivalent. Let us therefore just assume that we have the obstructions (114) at every singular point in both orientations and prove that some of the other obstructions are already satisfied. 

4.1.1. Against the deformation of the Eguchi-Hanson metrics. Lemma 4.6. We have the following equality for all i ∈ S+, j ∈ S−, ζ ∈

(R3)|S+| × (R3)|S−| and z ∈ R3,

〈BLj−i(ζi, z )ζj, ζ j

〉 = 〈BLj−i(ζj, ζ j)ζi, z 〉,

and therefore the above obstruction (114) at all singular points in the oppo-site orientation implies that the obstructions (112) vanish. 

Remark 4.7. This shows that the first obstructions coming from the defor-mations of the Eguchi-Hanson metrics are seen whether we first desingular-ize the positive ones or the negative ones. Proof. Given the expression of BLj−i of (109), we will study for a ∈ Z4 aterm of the above expressions. Because of the symmetries of B, we can simply study 〈πtr bx(ζi, z )ζj, ζ j〉. We will first consider z proportional to ζi

to obtain 

〈πtr bx(ζi, ζ i)ζj, ζ j

〉 = 〈( 12 ρx(ζi) ⊗ ρx(ζi) − 4|ζi|2I3

)ζj, ζ j

〉

(115) Higher order obstructions to the desingularization 967 = 12 〈ρx(ζi), ζ j

〉2 − 4|ζi|2|ζj|2

(116) = 12 〈( ρx(ζj) ⊗ ρx(ζj) − 4|ζj|2I3

)ζi, ζ i

〉

(117) = 〈πtr bx(ζj, ζ j)ζi, ζ i

〉,(118) where we used the fact that ρ−x = ( ρx)T = ( ρx)−1 = ρx. For z ⊥ ζi,

〈πtr bx(ζi, z )ζj, ζ j〉 = 〈( 12 ρx(ζi) ⊗ ρx(z))ζj, ζ j

〉

(119) = 12 〈ρx(ζi), ζ j

〉〈 ρx(z), ζ j

〉

(120) = 12 〈( ρx(ζj) ⊗ ρx(ζj) − 4|ζj|2I3

)ζi, z 〉

(121) = 〈πtr bx(ζj, ζ j)ζi, z 〉.(122) This proves the statement. 

4.1.2. Against the flat deformations of the torus. The last deforma-tions to consider are the flat deformations of the torus which are equivalent to variations of the matrix L used in the definition of BLx . For the form of the obstruction (105), we compute the following expression and leave the details to the reader. 

Lemma 4.8. Let us consider an infinitesimal variation of the flat torus seen as an infinitesimal variation of the matrix L in the direction KL −1,and assume that the obstruction (114) is satisfied in both orientations. Then, the obstruction (105) for a variation KL −1 of L is equivalent to 

∑

> i∈S+

∑

> j∈S−

∑

> a∈Z4

〈L(i − j − 2a), K (i − j − 2a)〉|L(i − j − 2a)|2

〈πtr bL(i−j−2a)(ζi, ζ i)ζj, ζ j

〉 = 0 (123) 

Remark 4.9. The deformations of the matrix Id orthogonal to those in the space spanned by the πtr (ek ⊗ ek) for (ek)k∈{ 1,2,3,4} the usual basis of R4,are equivalent to rotations of the torus and therefore to the rotation of the Eguchi-Hanson metrics and have already been considered above. 

Corollary 4.10. The obstructions of Corollary 4.3 reduce to 84 polynomial equations in the ζi and ζj with coefficients depending on L only. 968 Tristan Ozuch 

4.2. Some obstructed situations 

We therefore see from Remark 4.5 that even though some obstructions are equivalent, there are many remaining ones that outnumber the degrees of freedom we have. Indeed, we have only ruled out the last type of obstructions corresponding to (112). Let us now give an example of configuration of desingularization which cannot yield Ricci-flat (or even Einstein) metrics thanks to the obstructions identified in Corollary 4.3. 

Theorem 4.11. There does not exist a sequence Einstein metrics 

(M, gn)n∈N converging in the Gromov-Hausdorff sense to (T4/Z2, gL∞) with 

L∞ = Id by bubbling out exactly 1 positively oriented Eguchi-Hanson metric and 15 negatively oriented one. 

Remark 4.12. This is an obstruction to any Gromov-Hausdorff desingu-larization under a topological assumption. Proof. Let ( M, gn)n∈N be a sequence of Einstein metrics converging to ( T4/

Z2, gL∞) with L∞ = Id in the Gromov-Hausdorff sense while bubbling out Eguchi-Hanson metrics and let us assume without loss of generality that 

S+ = {0} and S− is the complement of {0} among the singular points of 

T4/Z2. Then, according to [Ozu19b], up to taking a subsequence, for all 

n, there exist Ln, ζ+ 

> n, 0

and ζ− 

> n,j

for j ∈ S−, such that the metrics gn are isometric to Einstein modulo obstructions perturbations of gDLn,ζ n.Let us show that the limit rescaled curvature R− 

> L∞,ζ +
> ∞

(j) defined in Proposition 3.27 is invertible at a singular point j ∈ S−. This will lead to a contradiction by the obstruction (101). By Lemma 4.2, we have an expression of R− 

> L∞,ζ +
> ∞

(j): it is a nonvanishing multiple of (124) ∑

> a∈Z4

πtr 

θ− 

> 1

((1 , 0, 0, 0) + 2 a) ⊗ θ− 

> 1

((1 , 0, 0, 0) + 2 a)

|(1 , 0, 0, 0) + 2 a|6 .

The value of the summand at a = 0 and a = ( −1, 0, 0, 0) is (125) πtr (ω− 

> 1

⊗ ω− 

> 1

) = 13 (2 ω− 

> 1

⊗ ω− 

> 1

− ω− 

> 2

⊗ ω− 

> 2

− ω− 

> 3

⊗ ω− 

> 3

),

which is invertible on Ω −. For the sum of the norms of the remaining terms, Higher order obstructions to the desingularization 969 that is, 

∑

> a∈Z4\{ 0,(−1,0,0,0) }

∣∣∣πtr 

θ− 

> 1

((1 , 0, 0, 0) + 2 a) ⊗ θ− 

> 1

((1 , 0, 0, 0) + 2 a)

|(1 , 0, 0, 0) + 2 a|6

∣∣∣,

we numerically have the control 

∑

> a∈Z4\{ 0,(−1,0,0,0) }

1

|(1 , 0, 0, 0) + 2 a|6 ≈ 0.19 < 23 .

This is not enough to make the sum (124) non invertible given the expression (125). The result follows by (111). 

Remark 4.13. The above proof works for many other limits than L∞ = Id 

and it is likely that it is true for any L∞, but it requires some control of the compactness of the lattice generated by L∞. Theorem 4.11 particular holds even with some of the most compact lattices like the D4 lattice. By compactness, we loosely mean how close the points of the lattice are to each other. 

Conjecture 4.14. The statement of Theorem 4.11 holds even without the assumption L∞ = Id , but only assuming that det( L∞) > 0.

For stable or nondegenerate Ricci-flat deformations, one does not sim-ply have R − 

> L∞,ζ +
> ∞

(j) invertible, but R − 

> L∞,ζ +
> ∞

(j) = 0. Since it is a sum of terms of the form (124) based at each singular point, it is direct to see that R− 

> L∞,ζ +
> ∞

(j) = 0 requires at least 3 Eguchi-Hanson metrics in this orientation. 

Corollary 4.15. There does not exist a sequence of stable Ricci-flat metrics 

(M, gn)n∈N converging in the Gromov-Hausdorff sense to (T4/Z2, gL∞) with 

L∞ = Id by bubbling out at most 3 positively oriented Eguchi-Hanson metric and the rest of negatively oriented ones. 

4.3. A family of desingularizations satisfying the obstructions 

Let us now specialize our discussion to the regular torus with L = Id and with the so-called chessboard pattern considered in [BK17]. We study the 48-dimensional space of gluings to the (fixed) regular torus and test it against the 16 × 5 + 4 = 84 obstruction equations identified in Section 4. Perhaps surprisingly, in this most symmetric situation, we will find a family of solutions to all of our 84 equations. This family of solutions is 14-dimensional. 970 Tristan Ozuch 

Remark 4.16. It will be clear from our proof and computations in this section that in the configuration considered in [BK17], many of these 84 

equations are not satisfied. 

The chessboard configuration already considered in [BK17] is defined as: 

S− = ({(a1, a 2, a 3, a 4) ∈ Z4, a 1 + a2 + a3 + a4 ∈ 2Z}/Z4)/Z2 and 

S+ = ({(a1, a 2, a 3, a 4) ∈ Z4, a 1 + a2 + a3 + a4 ∈ 1 + 2 Z}/Z4)/Z2.

Remark 4.17. In this chessboard configuration, let i ∈ S±. Then, we have the following configuration of other singular points: 

• at distance 0 is i ∈ S±

• at distance 1, there are 4 points in S∓

• at distance √2, there are 6 points in S±,

• at distance √3, there are 4 points in S∓, and 

• at distance 2, there is a point in S±.We will denote ic the opposite of i which is the point at maximal distance 

2 from i.

Here we will work under the assumption that for all i,

ζi = ζic.

We will denote e1 = (1 , 0, 0, 0) ∈ S+ and similarly ei ∈ S+ for i ∈ { 1, 2, 3, 4}

the other vectors of the canonical basis of R4. Let us introduce the following notations for the coordinates of our gluing parameters ζei:

ζei =: ( xi, y i, z i),

for i ∈ { 1, 2, 3, 4}. Let us denote x = ( x1, x 2, x 3, x 4), y = ( y1, y 2, y 3, y 4) and 

z = ( z1, z 2, z 3, z 4) the three vectors in R4 we obtain. 

Proposition 4.18. Using the above notations, let us assume that the family 

(x, y, z ) of vectors of R4 forms an orthogonal family of R4 with constant length. Then, the obstructions (105) and the obstructions (104) at every 

j ∈ S− are satisfied. Sketch of proof (some computer-based arguments involved). Let us consider a desingularization configuration as above. Higher order obstructions to the desingularization 971 Let us study the curvature at the singular point 0 ∈ S− induced by the other Eguchi-Hanson metrics glued at the points of S+. From (110), we know that this exactly equals (126) 

> 4

∑

> i=1

BId  

> ei

(( xi, y i, z i), (xi, y i, z i)) + BId  

> eci

(( xi, y i, z i), (xi, y i, z i)) .

Numerically, we obtain the following form for BId  

> ei

(( xi, y i, z i), (xi, y i, z i))+ 

BId  

> eci

(( xi, y i, z i), (xi, y i, z i)): 

⎡⎣

a · (2 x2 

> i

− y2 

> i

− z2 

> i

) b · xiyi b · xizi

b · xiyi a · (−x2 

> i

+ 2 y2 

> i

− z2 

> i

) b · yizi

b · xizi b · yizi a · (−x2 

> i

− y2 

> i

+ 2 z2 

> i

)

⎤⎦ ,

for some real numbers a ≈ 0.69 and b ≈ 2.0, and similar formulas for the other i by symmetries. Therefore, the equation (127) 

> 4

∑

> i=1

BId  

> ei

(( xi, y i, z i), (xi, y i, z i)) + BId  

> eci

(( xi, y i, z i), (xi, y i, z i)) = 0 .

coming from the obstruction (114) reduces to having both 

> 4

∑

> i=1

x2 

> i

=

> 4

∑

> i=1

y2 

> i

=

> 4

∑

> i=1

z2 

> i

, and 

> 4

∑

> i=1

xiyi =

> 4

∑

> i=1

xizi =

> 4

∑

> i=1

yizi = 0 .

This means that we are looking for an orthogonal family of 3 vectors x =(xi)i, y = ( yi)i and z = ( zi)i with same length in R4. This is given by an element of R+ × RP 3 × O(3). More precisely, the element of R is equal to ∑4 

> i=1

x2 

> i

= ∑4 

> i=1

y2 

> i

= ∑4 

> i=1

z2 

> i

, the element of RP 3 is a line orthogonal to (x, y, z ) in R4 and O(3) is the orthonormal basis ( x/ |x|, y/ |y|, z/ |z|) in the orthogonal of the element of RP 3. This set is 7-dimensional. Similarly, we can study the variations of the curvature when L = Id in the directions ei ⊗ ei for i ∈ { 1, 2, 3, 4}. We again find numerically that the obstructions (105) are of the form: 

⎡⎣

c · (2 x2 

> i

− y2 

> i

− z2 

> i

) d · xiyi e · xizi

d · xiyi c · (−x2 

> i

+ 2 y2 

> i

− z2 

> i

) f · yizi

e · xizi f · yizi c · (−x2 

> i

− y2 

> i

+ 2 z2 

> i

)

⎤⎦ ,972 Tristan Ozuch for some nonvanishing real numbers c, d, e, f which depend on the direction in which the deformation is done. Therefore, they also vanish under the conditions ∑4 

> i=1

x2 

> i

= ∑4 

> i=1

y2 

> i

= ∑4 

> i=1

z2 

> i

and ∑4 

> i=1

xiyi = ∑4 

> i=1

xizi =∑4 

> i=1

yizi = 0. Moreover, because we have similar equations and degrees of freedom in the other orientation, we obtain a 14-dimensional family of candidates satisfying all of the obstructions of Corollary 4.3. 

Example 4.19. Some examples of solutions to the above equations are 

ζ1 = (1 , 1, 1) , ζ2 = (1 , −1, −1) , ζ3 = ( −1, 1, −1) and ζ4 = ( −1, −1, 1) and 

(128) 

ζ1 = (1 , 0, 0) , ζ2 =

(

0, 1/√2, 0

)

, ζ3 =

(

0, 0, 1/√2

)

and ζ4 = (1 , 0, 0) .

(129) 

Appendix A. Function spaces 

For a tensor s, a point x, α > 0 and a Riemannian manifold ( M, g ). The H¨ older seminorm is defined as [s]C α(g)(x) := sup 

> {y∈TxM, |y|<inj g(x)}

∣∣∣ s(x) − s(exp gx(y)) 

|y|α

∣∣∣g.

For orbifolds, we consider a norm bounded for tensors decaying at the singular points. 

Definition A.1 (Weighted H¨ older norms on an orbifold) . Let β ∈ R, k ∈ N,

0 < α < 1 and (Mo, g o) an orbifold. Then, for any tensor s on Mo, we define 

‖s‖C k,α β (go) := sup 

> Mo

r−βo

( k∑

> i=0

rio|∇ igos|go + rk+αo [∇kgos]C α(go)

)

.

For ALE manifolds, we will consider a norm bounded for tensors decay-ing at infinity. 

Definition A.2 (Weighted H¨ older norms on an ALE orbifold) . Let β ∈ R,

k ∈ N, 0 < α < 1 and (N, g b) be an ALE manifold. Then, for all tensor s

on N , we define 

‖s‖C k,α β (gb) := sup 

> N

rβb

( k∑

> i=0

rib|∇ igbs|gb + rk+αb [∇kgbs]C α(gb)

)

.Higher order obstructions to the desingularization 973 On M , using a partition of unity 1 = χM to + ∑ 

> j

χN tj with χM to equals to 1 where gDt = go and χN tj equals to 1 where gDt = tjgbj (see [Ozu19a]), we can define a global norm. 

Definition A.3 (Weighted H¨ older norm on a na¨ ıve desingularization) . Let 

β ∈ R, k ∈ N and 0 < α < 1. We define for s ∈ T M ⊗l+ ⊗ T ∗M ⊗l− a tensor 

(l+, l −) ∈ N2, with l := l+ − l− the associated conformal weight, 

‖s‖C k,α β (gD) := ‖χM to s‖C k,α β (go) + ∑

> j

T l 

> 2
> j

‖χN tj s‖C k,α β (gbj ).

A.1. Decoupling norms 

We actually need a last family of norms to get good analytic properties for our operators, see [Ozu19b]. With the notations of Definition 1.2, denote for each singular point k, Ak(t,  0) := (Φ k)∗Ae(−10

√tk,  0) and Bk(0) := (Φ k)∗Be(0 ,  0), as well as cut-off functions χAk(t, 0) and χBk(0) respectively supported in Ak(t,  ) and Bk(0), and equal to 1 on Ak(t, 20) and Bk(0/2). 

Definition A.4 (Ck,α β, ∗ -norm on 2-tensors) . Let h be a 2-tensor on (M, g D),

(Mo, g o) or (N, g b). We define its Ck,α β, ∗ -norm by 

‖h‖C k,α β, ∗

:= inf 

> h∗,H k

‖h∗‖C k,α β

+ ∑

> k

|Hk|ge,

where the infimum is taken on the (h∗, (Hk)k) satisfying h = h∗ +∑ 

> k

χAk(t, 0)Hk for (M, g D) or h = h∗+∑ 

> k

χBk(0)Hk for (Mo, g o) or (N, g b),where each Hk is some constant and trace-free symmetric 2-tensors on 

R4/Γk.

A.2. An application of the analysis on weighted spaces 

Consider for n ∈ N, for γ ∈ N\{ 3 − n, . . . , −1} and 0 < β < 1 the Fredholm operator 

Pe : rγ 

> e

C2,α  

> −β

(Rn\{ 0})  → rγ−2 

> e

Cα

> −β

(Rn\{ 0}),

where the norms Cl,α 

> −β

(Rn\{ 0}) on symmetric 2-tensors denote the norm on 

Rn\{ 0} seen as orbifold at 0 like in Definition A.1 and ALE at infinity like in definition A.2. This operator is Fredholm and its kernel is composed of homogeneous harmonic 2-tensors in rγ 

> e

. Its L2-cokernel is the kernel of 

Pe : rn+2 −γ 

> e

C2,α β (Rn\{ 0})  → rn−γ 

> e

Cαβ (Rn\{ 0}),974 Tristan Ozuch which is reduced to {0}. As a direct consequence of the open mapping the-orem, we have the following result. 

Lemma A.5. Let n ∈ N, for γ ∈ N\{ 3 − n, . . . , −1} and 0 < β < 1. Then, there exists C > 0 such that for any symmetric 2-tensor v ∈ rγ−2 

> e

Cα

> −β

(Rn\{ 0}),there exists a 2-tensor h satisfying Peh = v, with 

‖h‖rγ    

> eC2,α
> −β(Rn\{ 0})

 C‖v‖rγ−2  

> eCα
> −β(Rn\{ 0})

.

References 

[Ach19] B. Acharya, Supersymmetry, Ricci flat manifolds and the string landscape , preprint arXiv:1906.06886 [hep-th]. [And89] M. T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds , J. Amer. Math. Soc. 2 (1989), no. 3, 455–490. http://www.jstor.org/stable/1990939 [And92] M. T. Anderson, The L2 structure of moduli spaces of Einstein metrics on 4-manifolds , Geometric and Functional Analysis 2, no. 1, 29–89 (March 1992). [And10] M. T. Anderson, A survey of Einstein metrics on 4-manifolds .Handbook of Geometric Analysis, No. 3, 1–39, Adv. Lect. Math. (ALM), 14. Int. Press, Somerville, MA (2010). [BKN89] S. Bando, A. Kasue, H. Nakajima, On a construction of coordi-nates at infinity on manifolds with fast curvature decay and max-imal volume growth , Invent. Math. 97, no. 2, 313–349 (1989). [Biq13] O. Biquard, D´ esingularisation de m´ etriques d’Einstein. I , In-vent. Math. 192, no. 1, 197–252 (2013). http://link.springer.com/ article/10.1007/s00222-012-0410-7 [Biq16] O. Biquard, D´ esingularisation de m´ etriques d’Einstein. II , Invent. Math. 204, no. 2, 473–504 (2016). [Biq17] O. Biquard, Non d´ eg´ en´ erescence et singularit´ es des m´ etriques d’Einstein asymptotiquement hyperboliques en dimension 4 , Math. Ann. 372, no. 1–2, 531–553 (2018). [BR15] O. Biquard, Y. Rollin, Smoothing singular constant scalar curva-ture K¨ ahler surfaces and minimal Lagrangians , Adv. Math. 285, 980–1024 (2015). Higher order obstructions to the desingularization 975 [BK17] S. Brendle, N. Kapouleas, Gluing Eguchi-Hanson metrics and a question of Page , Comm. Pure Appl. Math 70, 1366–1401 (2017). [CT06] J. Cheeger, G. Tian, Curvature and injectivity radius estimates for Einstein 4-manifolds , J. Amer. Math. Soc. 19, 487–525 (2006). [Don12] S. K. Donaldson, Calabi-Yau metrics on Kummer surfaces as a model gluing problem , Advances in Geometric Analysis, 109–118, Adv. Lect. Math. 21. International Press, Somerville, MA (2012). [EH78] T. Eguchi, A. Hanson, Asymptotically flat self-dual solutions to Euclidean gravity , Physics Letters B 74, 249–251 (1978). [Fin11] J. Fine, A gauge theoretic approach to the anti-self-dual Einstein equations , arXiv:1111.5005, 2011. [GP79] G. W. Gibbons, C. N. Pope, The positive action conjecture and asymptotically euclidean metrics in quantum gravity , Comm. Math. Phys. 66, 267–290 (1979). [Koi83] N. Koiso, Einstein metrics and complex structures , Invent. Math. 73, no. 1, 71–106 (1983). [Kro89a] P. B. Kronheimer, The construction of ALE spaces as hyper-K¨ ahler quotients , J. Differential Geom. 29, no. 3, 665–683 (1989). https://projecteuclid.org/euclid.jdg/1214443066 [LS94] C. LeBrun, M. Singer, A Kummer-type construction of self-dual 4-manifolds , Math. Ann. 300, 165–180 (1994). [LM85] R. B. Lockhardt, R. C. McOwen, Elliptic operators on noncompact manifolds , Ann. Sci. Normale Sup. Pisa IV-12 (1985), 409–446. [Ozu19a] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds I ,preprint, arXiv:1909.12957 [math.DG]. [Ozu19b] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II ,preprint, arXiv:1909.12960 [math.DG]. [Ozu20t] T. Ozuch, Compl´ etion de l’espace de modules des m´ etriques d’Einstein en dimension 4 , PhD thesis. [PR78] F. Pacard, T. Rivi` ere, Linear and Nonlinear Aspects of Vortices ,Progress in Nonlinear Differential Equations and their Applica-tions, 39. Birkh¨ auser, Boston, MA (2000). [Pag78] D. N. Page, A physical picture of the K3 gravitational instanton ,Physics Letters B 80, 55–57 (1978). 976 Tristan Ozuch [Pag81] D. N. Page, A periodic but nonstationary gravitational instanton ,Physics Letters B 100, 313–315 (1981). [PP87] D. N. Page, C. Pope, Inhomogeneous Einstein metrics on complex line bundles , Classical Quantum Gravity 4 (1987), 213–225. [Spo14] C. Spotti, Deformations of Nodal K¨ ahler–Einstein Del Pezzo Sur-faces with Finite Automorphism Groups , J. London Math. Soc. 89 (2014). [Top87a] P. Topiwala, A new proof of the existence of K¨ ahler-Einstein met-rics on K3 I , Invent. Math. 89, 425–448 (1987). [Top87b] P. Topiwala, A new proof of the existence of K¨ ahler-Einstein met-rics on K3, II , Invent. Math. 89, 449–454 (1987). [Yau78] S. T. Yau, On the Ricci curvature of a compact K¨ ahler manifold and the complex Monge-Amp` ere equation , I. Comm. Pure Appl. Math., 31, 339–441 (1978).
