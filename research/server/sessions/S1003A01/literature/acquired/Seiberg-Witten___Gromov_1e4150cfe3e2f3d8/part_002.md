---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Seiberg-Witten ⇒ Gromov]

Corollary 3.1.4 There is a subsequence of the Fn which converges in the weak topology to a current F.This current should be thought of as the “limit” of solutions to the Seiberg-Witten solutions with increasing pertubation parameter. It shares many of the same properties as the Fn

Claim 3.1.5 The current F satisfies the following properties 1. It is closed (i.e. Fd(−) = 0)2. It is integral (i.e. dμ = 0 and μ evaluates to an integer on all closed cycles implies F( μ) ∈ Z).) 3. It is Poincaré dual to c1(L) (i.e. F( μ) = [ μ] ⋅ c1(L) .) Our construction of F will give it an important geometric interpretation. The support of F will be a psuedoholomorphic curve. For an example of why how one might visualize this, consider the bump functions 

δr (x) = 1

re  x2 

> r2

which become more concentrated with increasing parameter r. These converge to the Dirac delta distribution, n which “picks out” a point on the real line. In a similar fashion, by increasing the parameter r for the Seiberg-Witten solution, the currents Fn converge to F which picks out a 2 dimensional subspace. The proof of 3 should be motivated from this Fundamental Proposition. 

Proposition 3.1.6   

> Support of F

The support of F is contained in a set C that has finite 2-dimensional Hausdorff measure. We spend the rest of this section proving this proposition. 

> V.2014/11/17.09:25:57

24 SW ⇒ Gromov 

## 3.2 Constructing C

Here, we provide an outline for the construction of C, a subset of M with Hausdorff dimension 2 that contains the support of F. The process for showing that this set has Hausdorff dimension 2 is as follows: • Prove a bunch of useful inequalities about solutions to the Seiberg-Witten equations. We won’t do this. • (Subsection 3.2.1) Understand the energy function around zeros of solutions of the Seiberg-Witten equations. • (Subsection 3.2.2) Another characteristic of solutions to the Seiberg-Witten equations is that all of the “interesting” parts of the spinor field die off at an exponential rate away from the zero set. • (Subsection 3.2.3) Use the above two ideas to construct a certain number of balls that contain a large percentage of the energy associated to Fn, and use that to make a statement about how much of the support of Fn is contained within those balls. Take the limit F = lim n→∞ Fn, and use the earlier sections to show that the support of this current must be contained in a set of Hausdorff dimension 2 with finite measure. • (Subsection 3.2.4) Finally, we motivate some of the structure of F, and why we might expect the support to be a psuedoholomorphic curve by showing that F is of type 1 − 1.

3.2.1 Energy of the Seiberg-Witten Equations 

The Seiberg-Witten equations come with an associated energy functional, and understanding bounds on this energy gives us information on the solutions. Instead of trying to characterize the moduli space of SW equations with this energy functional, we will be interested in showing that the majority of the energy of a solution to the Seiberg-Witten equations is concentrated near the zero section of the equations; these bound will give topological data on the zeros of the Seiberg-Witten solutions. 

Definition 3.2.1 Given a solution to the r-perturbed Seiberg-Witten equations (A, (α, β )) , and an open set U , define the 

energy of α over U by the integral 

EU ∶= r

4 SU

S1 − S αS2S

The center of Taubes’s proof centers on the fact that the energy of the function cannot be too big; at the same time, one can show that there must be some large amount of energy concentrated around the zeros of 

α.

Proposition 3.2.2  

> Monotonicity

Let (A, (α, β )) be a solution to the r-perturbed Seiberg-Witten equations. Then there is a constant c ≥ 1

depending only on the choice of spin structure and Riemannian metric such that given: • r is greater than c

• A geodesic ball of radius 1 

> C

≥ s ≥ 12r 12

centered at x

Then we have the following lower and upper bounds for the energy • (Upper Bound) EB ≤ Cs 2

• (Lower Bound) Provided that SαS < 12 we have that EB ≥ 1 

> C+1

s2.This energy bound can be used to give produce a function whose derivatives are large when α is small, but whose overall size is bounded everywhere. 

Proposition 3.2.3 Let (A, (α, β )) be a solution to the r-perturbed Seiberg-Witten equations. Then there is a constant c ≥ 1

depending only on the choice of spin structure and Riemannian metric such whenever r ≥ 1 there exists a 

> V.2014/11/17.09:25:57

3.2 Constructing C 25 

smooth function u ∶ M → C such that 

SuS ≤ c

12 d∗du ≥r whenever SαS < 12

Sd∗du S ≤ cr 

The energy bound is not used directly to construct the function u, but it provides an argument for the structure of points where α ≤ 12 . In order to construct the function u, Taubes first constructs a covering for the set where α ≤ 12 by balls using the bounds on the energy of α. The function is then created by smoothing out the characteristic equations for these balls. The properties of this covering are summarized in the following 3 lemmas: 

Lemma 3.2.4 Given (A, (α, β )) as before, there exists a constant c such that for r ≥ C and a fixed r −12 < ρ < ρ0~100 ,we have the following: • The set where SαS ≤ 12 can be covered by cρ2 balls of radius ρ.• This set of covering balls {Bi} can be chosen in such a way that if we replace them with balls of half radius, the set is disjoint. This gives us a nice bound on the “size” of the support of the Seiberg Witten solutions. We also have that the balls capture a large portion of the energy— that is, by choosing a set with slightly larger α, we need not go out much farther from this set of balls to achieve this alpha value. 

Lemma 3.2.5 Given λ > 0, there exists a constant c with dependence on λ , metric and choice of spin structure, with the following property. Let (A, (α, β )) be a solution to the Seiberg Witten equations as before. Let V be the set of points where SαS ≤ 12 , and V ′ the set of points of size less that 34 . Cover the set V as in Lemma 3.2.1, and let B be a ball from this set. Let B′ be a ball of radius cr 12

centered at B. Then 

vol (( M − V ′) ∩ B′) ≥ λ vol (B).

Finally, we have a bound on how clumped together the balls need to be. 

Lemma 3.2.6 There is a constant c which depends only on the spin structure and metric such that if B(n) is a ball of radius nr 12

, the number of balls from the covering in Lemma 3.2.1 whose centers lie in B(n) is less than 

cn 2.These bounds on covering balls will become useful later when we explore the creation of the set C.

3.2.2 Exponential Decay of Solutions 

In this section, we will discuss about Exponential decay estimates . Before we proceed, we would like to emphasize the significance of exponential decay estimates . Taubes’s paper relies heavily on the fact that the size of α, β and ∇′ 

> A

all drop off exponentially in value from the zero set of α and in the parametery r.This means that by increasing r, we can localize the non-trivial behavior of the Sieberg-Witten solutions to around the zero set of α.

> Weitzenböck formula

We recall the isomorphism 

S+ = E ⊕ ( K−1 ⊗ E).

Then every section ψ can be written of the form 

r 12 ⋅ ( αu 0 + β)

> V.2014/11/17.09:25:57

26 SW ⇒ Gromov 

where α is a section of E, α ⋅ u0 is a section of E summand of S+, and β is a section of the K−1 ⊗ E

summand. Let’s recall the Seiberg-Witten equation 

~∂Aψ = 0

F + 

> A

= 14 τ (ψ ⊗ ψ∗)

For Exponential decay estimates , we will mainly deal with inequalities induced from the first equation of the Seiberg-Witten equation. Since the Dirac operator is defined by 

~∂Aψ ∶= σ(▽ Aψ) ∶ S+ → S+ ⊗ T ∗X → S−,

we can apply ~∂A twice to ψ. Then, we get ~∂2

> A

ψ = 0 for every solution of Seiberg-Witten equation. After some computations (also using F + 

> A

= 14 τ (ψ ⊗ ψ∗)), the equation ends up with an equation, Weitzenböck formula ,

∇∗

> A

∇Aψ + r

4 ψ + 12 ⋅ c+(F +

> A

)ψ = 0. (3.1) (Here, ∇∗ 

> A

is the adjoint of ∇A.) The equation above is, in fact, the whole thing we need in order to prove results about Exponential decay estimates .

Differential Inequalities 

We will skip precise calculation process but give results and simple explanations about them. In this section we will use c and cn to stand for a variety of different constants. The first inequality we would like to get is 

12 d∗dS∇ aαS2 + S∇ a∇aαS2 + r

4 SαS2S∇ aαS2

≤ c ⋅ ( r ⋅ ( 1 − S αS2) + 1)S∇ aαS2

+ c ⋅ S∇ aαS  ( 1 + rSβS) ⋅ S∇ ′

> A

βS + ( rSαS2 + 1)S βS + S∇ ′

> A

∇′

> A

βS  .

First, project the equation ~∂2

> A

ψ = 0 onto the E summand of S+ = E ⊕ ( K−1 ⊗ E). Then, take the action by 

∇a and inner product with ∇aα. One thing to be noted is that c only depends on the Riemannian metric. Using an easy inequality that 2Sf SS gS ≤ rSf S2 + 1 

> r

SgS2, we can convert this inequality to 

12 d∗dS∇ aαS2 + S∇ a∇aαS2 + r

4 SαS2S∇ aαS2

≤  c1 ⋅ r(1 − S aS) 2 + r

16  S∇ aαS2

+ c1 ⋅ rSβS2 + c1 ⋅ S∇ ′

> A

βS2 + 32 

r S∇ ′

> A

∇′

> A

βS2 (3.2) In a very similar sense, project the Eq 3.1 onto the K−1 ⊗ E summand and then take the action by ∇′ 

> A

and the inner product with ∇′

> A

β. Then we get 

12 d∗dS∇ ′

> A

βS2 + S∇ ′

> A

∇′

> A

βS2 + r

4 SαS2S∇ ′

> A

βS2

≤ c2 ⋅ ( r(1 − S αS2) + 1) ⋅ S∇ ′

> A

βS2

+ c2S∇ ′

> A

βS  ( 1 + rSαSS βS) ⋅ S∇ aαS + rSαSS βS2 + S∇ a∇aαS  .

For the next step, we again use the simple inequality we have used before. Then, we get 

12 d∗dS∇ ′

> A

βS2 + S∇ ′

> A

∇′

> A

βS2 + r

4 SαS2S∇ ′

> A

βS2

≤ ( c3r(1 − S αS2) + r

16 )S∇ ′

> A

βS2 + c3SβS2

+ c3S∇ aαS2 + 32 

r S∇ a∇aαS2 (3.3) 

> V.2014/11/17.09:25:57

3.2 Constructing C 27 

Now, we have got two inequalities which we want to add to each other after some scalar multiplication. Calculating (3.2) + r 

> 32

× ( 3.3), we get an inequality 

12 d∗dy + r

4 SαS2y ≤  c4r(1 − S αS) 2 + r

16  y + c4rSβS2 (3.4) where y ∶= S∇ aαS2 + r 

> 32

S∇ ′

> A

βS2.Before we get into the main step, we shall induce an inequality from (3.1) again. Simply, take the inner product of (1) with β.

12 d∗dSβS2 + S∇ AβS2 + r

4 SβS2(1 + S αS2 + S βS2) − c1SβS2 ≤ c2SβSS∇ aαS.

With r > 16 c1, this inequality (also using the inequality 2Sf SS gS ≤ rSf S2 + 1 

> r

SgS2) can be simplified as 

12 d∗dSβS2 + r

4 SαS2SβS2 ≤ − r

8 SβS2 − S∇ AβS2 + c3

r S∇ aαS2. (3.5) Finally, we get an inequality (as a result of (3.4) + r2 

> 16 c3

× ( 3.5))

12 d∗dy 1 + r

4 SαS2y1 ≤  c4r(1 − S αS2) + r

8  y1

where y1 ∶= S∇ aαS2 + r 

> 32

S∇ ′

> A

βS2 + r2 

> 16 c3

SβS2.Here, the reason we have Exponential decay outside of some α−1(0) is that we can make SαS < 1 very close to 1 for all points x ∈ X such that dist (x, α −1(0)) ≥ c5r− 12 for some constant c5. (This is a general fact for a solution of the Seiberg-Witten equation.) Then this gives 

12 d∗dy 1 + r

32 y1 ≤ 0

for all x ∈ X such that dist (x, α −1(0)) ≥ c5r− 12 .Now, define a function Hy (x) for x, y ∈ X as 

1

dist (x, y )2 exp − 1

c r 12 dist (x, y ) + c ⋅ exp − 1

c r 12  .

The main role of this function comes from the fact that 

12 d∗dH y + r

32 Hy ≥ 0

as long as dist (x, y ) ≥ c ⋅ r− 12 . We now define 

h ∶= Q 

> i

Hxi

where {xi} ⊂ α−1(0) is maximal such that Br− 12 (xi)’s are disjoint. Then, the behavior of h(x) is bounded by 

h(x) ≤ c6 ⋅ r exp (− 1

c r 12 ⋅ dist (x, α −1(0))) 

where dist (x, α −1(0)) . Now, we can find a constant c8 such that 

12 d∗d(y1 − c8 ⋅ h) + r

32 (y1 − c8 ⋅ h) ≤ 0

where dist (x, α −1(0)) ≥ c5 ⋅ r− 12 and on the boundary where dist (x, α −1(0)) = c5 ⋅ r− 12 , y1 − c8 ⋅ h ≤ 0.So, this gives a differential inequality with some initial boundary condition. Hence, y1 is bounded by a scalar multiple of h and h has Exponential decay . Therefore, y1’s each term has Exponential decay estimates. 

> V.2014/11/17.09:25:57

28 SW ⇒ Gromov Proposition 3.2.7 For a fixed Spin c structure ˜P , there exists a constant c such that for any solution (A, (α, β ) to the Seiberg-Witten equations, we have the following bounds: 

r(1 − S αS2), r2~3SβS, SFαS, r1~2S∇ AαS, rS∇ ′

> A

βS ≤ cr exp − r1~2

c dist (x, α −1(0)) 

3.2.3 Covering the Solution with Balls 

With the knowledge that the zero section of the solutions can be covered by a set of balls of radius ρ that grow in number as ρ2, (Lemma 3.2.1), and that the majority of the interesting behavior of the Seiberg Witten equations is contained in a small volume around the zero section (Subsection 3.2.2), we are ready to prove that the support of the current F is contained in a set of Hausdorff Dimension 2. For each N define the set Λn(N ) to be the set of c(256 )N balls with radius r ⋅ ( 16 )−N centered at the points that cover α−1 

> n

(0). We may assume that the center of these balls are contained in α−1 

> n

(0). We may then take U (N ) to be the set of c(256 )N balls of radius 4 ⋅ ( 16 )−N that eventually contain all of the Λn(N ) for sufficiently large n. These U (N ) are nested inside of each other. Define the set 

C ∶=  

> N

U (N )

Notice that C here is independently defined of the choices that we make for these balls. It is clear from construction that C has finite 2-dimensional Hausdorff measure. But C also has the following nice properties: 

Lemma 3.2.8 The set C has the following properties • It has finite 2-dimensional Hausdorff measure. • There is a constant C such that for all x ∈ C, and B a ball of radius ρ, then the 2-dimensional Hausdorff measure of C ∩ B is at least Cρ 2.• C contains the support of F

While the full details of this proof are rather technical, the basic idea is as follows: The Hausdorff dimension of C follows simply from the construction of C. Recall that the Hausdorff dimension is simply the smallest d such that the d-dimensional Hausdorff measure of C is still finite, and the 

d-Hausdorff measure is given by 

Hd(C) = lim  

> r0→0

inf 

> ∞

Q

> i=1

rdi 

where the infinum is over all covers of C by balls of radius ri < r0. Since the number of balls in U (N )

grows as 256 N , while the radius of the balls shrink as 16 −N we have that the d = 2 will still produce a finite 2-Hausdorff measure of the set as 256 = 16 2.The monotonicity formula Proposition 3.2.1 shows that the majority of the energy of a solution must be near the zero section. This shows that balls centered at C have intersection with C of “proper” 2 dimensional area. Two show that C contains the support of F, consider a bump μ supported outside of C C . Then for some 

N , μ will be disjoint from Un(N ) for all large n. Since the balls in Un(N ) were designed to decrease at subexponential rate, while the size of the curvature grows at an exponential rate, we have, 

SF n(μ)S ≤ c ⋅ r ⋅ exp r 12 

> n

16 −N  ⋅ sup 

> x

Sμ(x)S .

This shows that the support of F does not contain the support of μ, proving the lemma. 

3.2.4 Further Properties of C

While we will not show that C is a psuedoholomorphic curve, we will provide some indications of why we should expect it to be one. We can show that C is in some way “ J-invariant.” On the space of 2 forms there 

> V.2014/11/17.09:25:57

3.2 Constructing C 29 

is an involution defined by multiplication by J. By taking duals, we get an involution of J on the space of currents. We say that a current if type 1 − 1 if it is invariant under this J involution. 

Lemma 3.2.9 The current F is of type 1 − 1.

Proof. Let us test a form μ against Fn. We may assume that μ is locally supported around C, as we have shown that the behavior of μ away from C does not Fn(μ) as n → ∞ . We have that 

Fn(μ − Jμ )

is dependent on only the terms not fixed by J. These are the terms in F + 

> An

which are linear in βn and β∗

> n

. It can be shown that 

SβnS2 ≤ cr 1 − S αS2 + cr2

> n



where c is some constant. Therefore, the terms of F + 

> An

that are linear are bounded by 

SF n(μ − Jμ )S ∼YS βnSS μSY L1

Using Hölder’s inequality and the fact that μ has support close to C

≤Y χU (N )βnYL1 YμYL∞

≤ sup SμS ⋅ Y χU (N )Y2 ⋅ Y βnYL2

≤c sup SμS ⋅ ( vol (U (N )) 12 ⋅ Y rn(1 − S αnS2)Y L1

Becuase of compactness we have that the first term is bounded. The second term goes to zero. The last term in this is bounded by the energy bound above. Taking the limit as n → 0, we see that F( μ − Jμ ) = 0. This proves that F is of type 1 − 1. ∎

This places fairly strong conditions on the support of F, suggesting that it has some kind of J-invariant properties. While we will not go so far as to actually show that the tangent space to the support is J invariant, we should be very hopeful that this is the case from this result. 

3.2.5 Other Properties of C

This exposition only covers a small portion of Taubes’s proof. From here, Taubes goes on to prove that the set C is not just a 2 dimensional set, but a psuedoholomorphic curve. The techniques used in this part are rather technical, but here is an outline of the methodology for the rest of the paper: • One of the constructions that we did not cover is describing the “local structure of α−1(0).” By using a sufficently small trivialization, Taubes compares the zero sets of the Seiberg-Witten solutions over 

M to the zeros of the the Seiberg-Witten solutions over C × C. While these generally do not have the same structure, they are similar enough that we can pay a very small price for working in one or the other. • The structure of C is studied by looking at its intersections with Psuedoholomorphic disks. One uses an argument similar to the (1 − 1)-ness of F to show that the set C intersects certain disks positively. The claim is that for every disk σ ∶ D → M the assignement 

I(σ) ∶= lim  

> n→∞

SD

i

2π σ∗FAn

has the following propeties : 1. If σ(D) doesn’t intersect C, I(σ) = 0

2. I(σ) is defined up to homotopy. 

> V.2014/11/17.09:25:57

30 SW ⇒ Gromov 

3. I respects muliplicity of covering, that is if θk ∶ D → D is the degree k mapping, then I(σθ k) = 

kI (σ).4. I(σ) is additive across disjoint unions. 5. If σ is pseudoholomorphic, then I(σ) > 0.• Taubes then shows that 2 dimensional surfaces that correspond to positive cohomology assignements (given by the conditions above) necessarily correlate to pseudoholomorphic curves. Furthermore, the positive cohomology assignment gives us the multiplicity that we should count the curve with in the Gromov-Taubes invariant. 

## 3.3 Where to Proceed from here 

This theorem had some interesting implications about Gromov type invariants. We summarize some of the major results discussed in [17] here. 

Theorem 3.3.1 Let M be an oriented 4-manifold with b+ 

> 2

> 1. Then the Gromov Invariants are not dependent on choice of symplectic form (other than a choice of canonical line bundle.) This follows trivially from the fact that the Seiberg-Witten equations are diffeomorphism invariant. This is rather remarkable, as the Gromov invariants look like they have a great deal of dependence on choice of symplectic structure. 

Theorem 3.3.2 Let X be a compact oriented 4-manifold with b+ 

> 2

> 1 and symplectic form ω. Let e ∈ H2(Z) with 

SW (e) ≠ 0. Then the Poincaré dual to e is represented by the fundamental class of an embedded, symplectic curve with ginus 1 + e ⋅ e.This means that elements of homology with non-trivial Seiberg-Witten invariant are representatble by nice symplectic curves. 

Theorem 3.3.3 The manifold CP 2 has unique (up to symplectomorphism) symplectic structure. The proof of this relies on the fact that the Seiberg-Witten invariants of CP 2 vanish due to positive curvature of CP 2. This allows the construction of a certain type of 2-sphere. A theorem of gromov states that such a two sphere impleis the existence of symplectomorphism to the standard Kähler form. The technique for proving that CP 2 has unique symplectic structure can be used to show that other manifolds admit no symplectic structure at all. Finally, this proof gives us an idea of where to start to define “Gromov-type” invariants for non-symplectic manifolds. There exists manifolds with non-zero Seiberg-Witten invariants which do not admit symplectic structure. If M does not admit a symplectic structure, we can pick 

ω to be a nontrivial ASD harnomic 2 form, which vanishes at points of M . The theorem suggest that there is still a theory of psuedo-holomorphic curves for degenerate ω given by the Seiberg-Witten equations. 

> V.2014/11/17.09:25:57

# Bibliography 

[1] Simon K Donaldson et al. “An application of gauge theory to four-dimensional topology”. In: J. Differential Geom 18.2 (1983), pp. 279–315. [2] José Figueroa-O’Farrill. Spin Geometry . Lecture Notes. University of Edinburgh, 2010. [3] Mikhael Gromov. “Pseudo holomorphic curves in symplectic manifolds”. In: Inventiones mathemati-cae 82.2 (1985), pp. 307–347. [4] Michael Hutchings and Clifford Henry Taubes. “An introduction to the Seiberg-Witten equations on symplectic manifolds”. In: Symplectic Geometry and Topology, Eliashberg, Y. and Traynor, L. ed., IAS/Park City Math. Series 7 (1999), pp. 103–142. [5] Jürgen Jost, Xiaowei Peng, and Guofang Wang. “Variational aspects of the Seiberg-Witten functional”. In: arXiv preprint dg-ga/9504003 (1995). [6] Dusa McDuff. J-holomorphic curves and quantum cohomology . Vol. 6. American Mathematical Soc., 1994. [7] Dusa McDuff. “Lectures on Gromov invariants for symplectic 4-manifolds”. In: Gauge theory and symplectic geometry . Springer, 1997, pp. 175–210. [8] John W Morgan. The Seiberg-Witten equations and applications to the topology of smooth four-manifolds . Vol. 44. Princeton University Press, 1996. [9] Liviu I Nicolaescu. Notes on Seiberg-Witten theory . Vol. 28. American Mathematical Society, 2000. [10] Athanase Papadopoulos. “Introduction to Teichmiiller theory, old and new”. In: Handbook of Teich-müller theory 1 (2007), p. 1. [11] Yongbin Ruan. “Symplectic Topology and Complex Surfaces”. In: Geometry and Analysis on Complex Manifolds : Festschrift for Professor S Kobayashi’s 60th Birthday (1994), pp. 171–197. [12] Nathan Seiberg and Edward Witten. “Electric-magnetic duality, monopole condensation, and con-finement in N = 2 supersymmetric Yang-Mills theory”. In: Nuclear Physics B 426.1 (1994), pp. 19– 52. [13] Clifford H Taubes. “SW ⇒Gr: From the Seiberg-Witten Equations to Pseudo-Holomorphic Curves”. In: Journal of the American Mathematical Society (1996), pp. 845–918. [14] Clifford Henry Taubes et al. “Counting pseudo-holomorphic submanifolds in dimension 4”. In: J. Differential Geom 44.4 (1996), pp. 818–893. [15] Clifford Henry Taubes et al. “Gr=SW: counting curves and connections”. In: Journal of Differential Geometry 52.3 (1999), pp. 453–609. [16] Clifford Henry Taubes et al. “Gr ⇒SW: from pseudo-holomorphic curves to Seiberg-Witten solutions”. In: Journal of Differential Geometry 51.2 (1999), pp. 203–334. [17] Clifford Henry Taubes. “The Seiberg-Witten and Gromov invariants”. In: Math. Res. Lett 2.2 (1995), pp. 221–238. [18] Peter Woit. Clifford Algebras and Spin Groups . Lecture Notes. Columbia, 2012.


## Native file acquisition

```json
[
  {
    "url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
    "final_url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
    "name": "SymplecticProjectMain.pdf",
    "size": 540837,
    "role": "primary_object_file",
    "status": "downloaded",
    "checksum": "sha256:7d223b91a35fc9900b383032d02c90ac9577171abce452d2303882d66ec7db3e",
    "identity_bound": true,
    "parent_url": "https://jeffhicks.net/files/SymplecticProjectMain.pdf",
    "primary_label": false,
    "download_eligible": true,
    "label": ""
  }
]
```
