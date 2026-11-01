---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: DEFORMATION THEORY OF SCALAR-FLAT KAHLER ALE SURFACES]

# DEFORMATION THEORY OF SCALAR-FLAT KAHLER ALE SURFACES

> Source: https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf
> Fetched: 2026-10-07 03:55
> Method: FULLTEXT_HTML_JINA|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "tavily",
  "source_url": "https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf",
  "metadata": {
    "provenance_urls": [
      "https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "\"original formula leading Kuranishi term reduced energy expansion gluing Burns metric scalar-flat ALE four-manifold\" original authoritative source conference proceedings preprint"
      },
      {
        "source": "tavily",
        "query": "\"original formula leading Kuranishi term reduced energy expansion gluing Burns metric scalar-flat ALE four-manifold\" original authoritative source"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf",
      "name": "Han_Viaclovsky_May_17_2016.pdf",
      "label": "",
      "role": "primary_object_file",
      "parent_url": "https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf",
      "identity_bound": true,
      "primary_label": false,
      "download_eligible": true
    }
  ]
}
```

## Source description

Abstract. We prove a Kuranishi-type theorem for deformations of complex struc-tures on ALE Kahler surfaces. This is used to prove that for any scalar- at Kahler ALE surface, all small deformations of complex structure also admit scalar- at Kahler ALE metrics. A local moduli space of scalar- at Kahler ALE metrics is then constructed, which is shown to be universal up to small di eomorphisms

## Retrieved source content

Title: Han_Viaclovsky_May_17_2016.pdf

URL Source: https://www.math.uci.edu/~jviaclov/preprints/Han_Viaclovsky_May_17_2016.pdf

Published Time: Tue, 17 May 2016 17:43:48 GMT

Number of Pages: 48

Markdown Content:
DEFORMATION THEORY OF SCALAR-FLAT K ¨ AHLER ALE SURFACES 

JIYUAN HAN AND JEFF A. VIACLOVSKY 

Abstract. We prove a Kuranishi-type theorem for deformations of complex struc-tures on ALE K¨ ahler surfaces. This is used to prove that for any scalar-flat K¨ ahler ALE surface, all small deformations of complex structure also admit scalar-flat K¨ ahler ALE metrics. A local moduli space of scalar-flat K¨ ahler ALE metrics is then constructed, which is shown to be universal up to small diffeomorphisms (that is, diffeomorphisms which are close to the identity in a suitable sense). A formula for the dimension of the local moduli space is proved in the case of a scalar-flat K¨ ahler ALE surface which deforms to a minimal resolution of C2/Γ, where Γ is a finite subgroup of U(2) without complex reflections. 

Contents 

1. Introduction 12. Notation 73. ALE K¨ ahler surfaces 84. Small deformations of complex structure 12 5. Versality of Kuranishi family 15 6. Essential deformations of complex structure 18 7. Stability of K¨ ahler metrics 24 8. Deformations of scalar-flat K¨ ahler metrics 26 9. Versality and uniqueness of the moduli space 31 10. Deformations of the minimal resolution 34 11. Examples 37 12. Appendix 40 References 46 1. Introduction 

This article is concerned with the following class of metrics: 

Definition 1.1. An ALE K¨ ahler surface (X, g, J ) is a K¨ ahler manifold of complex dimension 2 with the following property. There exists a compact subset K ⊂ M and a diffeomorphism ψ : X \ K → (R4 \ B)/Γ, such that for each multi-index I of order |I| 

∂I (ψ∗(g) − gEuc ) = O(r−μ−|I| ),(1.1) 

Date : May 17, 2016. The authors were partially supported by NSF Grant DMS-1405725. This paper was completed while the authors were in residence at Mathematical Sciences Research Institute in Berkeley, Cali-fornia. The authors would like to thank MSRI for their support, and for providing such an excellent working environment.  

> 12JIYUAN HAN AND JEFF A. VIACLOVSKY

as r → ∞ , where Γ is a finite subgroup of U(2) containing no complex reflections, B

denotes a ball centered at the origin, and gEuc denotes the Euclidean metric. The real number μ is called the order of g.

Remark 1.2. In this paper, henceforth Γ will always be a finite subgroup of U(2) containing no complex reflections. We are interested in the class of scalar-flat K¨ ahler ALE metrics. These are in-teresting since they are extremal in the sense of Calabi [Cal85], and they arise as “bubbles” in gluing constructions for extremal K¨ ahler metrics [ALM15a, ALM15b, AP06, APS11, BR15, RS05, RS09]. In the case of scalar-flat K¨ ahler ALE metrics, it is known that there exists an ALE coordinate system for which the order of such a metric is at least 2 [LM08]. We note that for an ALE K¨ ahler metric of order μ, there exist ALE coordinates for which 

∂I (J − JEuc ) = O(r−μ−|I| ),(1.2) for any multi-index I as r → ∞ , where JEuc is the standard complex structure on Euclidean space [HL15]. There are many known examples of scalar-flat K¨ ahler ALE metrics: 

• SU(2) case: when Γ ⊂ SU(2), Kronheimer has constructed families of hy-perk¨ ahler ALE metrics [Kro89a] on manifolds diffeomorphic to the minimal resolution of C2/Γ. In [Kro89b], Kronheimer also proved a Torelli-type theo-rem classifying hyperk¨ ahler ALE surfaces. In the Ak case, these metrics were previously discovered by Eguchi-Hanson for k = 1 [EH79], and by Gibbons-Hawking for all k ≥ 1 [GH78]. 

• Cyclic case: For the 1 

> p

(1 , q )-action, Calderbank-Singer constructed a family of scalar-flat K¨ ahler ALE metrics on the minimal resolution of any cyclic quotient singularity [CS04]. These metrics are toric and come in families of dimension 

k − 1, where k is the length of the corresponding Hirzebruch-Jung algorithm. For q = 1 and q = p − 1, these metrics are the LeBrun negative mass metrics and the toric multi-Eguchi-Hanson metrics, respectively [LeB88, GH78]. 

• Non-cyclic non-SU(2) case: The existence of scalar-flat K¨ ahler metrics on the minimal resolution of C2/Γ, was shown by Lock-Viaclovsky [LV14]. The question we address in this paper is whether the scalar-flat K¨ ahler property is preserved under small deformations of complex structure. In the cases where Γ ⊂ SU(2), the hyperk¨ ahler quotient construction produces hyperk¨ ahler metrics for the minimal resolution complex structure as well as for all small deformations of the minimal resolution complex structure. In the case of the LeBrun negative mass metrics, using arguments from twistor theory, Honda has shown that all small de-formations of the complex structure on O(−n) also admit scalar-flat K¨ ahler metrics [Hon13, Hon14]. For the case of general Γ, in [LV14], employing Honda’s result, it was shown that some of small deformations of complex structure admit scalar-flat K¨ ahler ALE metrics. DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 3

Our main result in this paper shows that for any scalar-flat K¨ ahler ALE surface, all 

small deformations of complex structure admit scalar-flat K¨ ahler ALE metrics. Our proof is analytic in nature, and in particular, gives a new analytic proof of Honda’s result on O(−n) mentioned above. To state our result precisely, we next recall some basic facts regarding deformations of complex structures. For a complex manifold ( X, J ), let Λ p,q denote the bundle of (p, q )-forms, and let Θ denote the holomorphic tangent bundle. The deformation complex Γ(Θ) ¯∂

−→ Γ(Λ 0,1 ⊗ Θ) ¯∂

−→ Γ(Λ 0,2 ⊗ Θ) (1.3) corresponds to a real complex Γ( T X ) LX J

−−→ Γ( End a(T X )) N ′

> J

−→ Γ((Λ 2,0 ⊕ Λ0,2)R) ⊗ T X ),(1.4) where LX J is the Lie derivative of J,

End a(T X ) = {I ∈ End (T X ) : IJ = −JI }(1.5) (the subscript a is used here since these are exactly the endomorphisms which extend to C-antilinear endomorphisms of the complexified tangent bundle), and N ′ 

> J

is the linearization of Nijenhuis tensor 

N (X, Y ) = 2 {[JX, JY ] − [X, Y ] − J[X, JY ] − J[JX, Y ]}(1.6) at J. The isomorphism from the complex (1.3) to (1.4) is simply taking the real part of a section. If g is a Hermitian metric compatible with J, then let  denote the ¯∂-Laplacian 

 ≡ ¯∂∗ ¯∂ + ¯∂ ¯∂∗,(1.7) where ¯∂∗ denotes the formal L2-adjoint. Each bundle in the complex (1.3), admits a -Laplacian, and these correspond to real Laplacians on each bundle in the com-plex (1.4). We will use the same -notation for these real Laplacians. To state our most general result, we need the following definition. This is necessary because there is a gauge freedom of Euclidean motions in the definition of ALE coordinates. 

Definition 1.3. Let ( X, g, J ) be a K¨ ahler ALE surface. For any bundle E in the complex (1.3) or (1.4), and τ ∈ R, define 

Hτ (X, E ) = {θ ∈ Γ( X, E ) : θ = 0 , θ = O(rτ ) as r → ∞} .(1.8) Define 

W = {Y ∈ H 1(X, T X ) | LY g = O(r−1), LY J = O(r−3), as r → ∞} .(1.9) Finally, define the real subspace 

Hess (X, End a(T X )) ⊂ H −3(X, End a(X)) (1.10) 4 JIYUAN HAN AND JEFF A. VIACLOVSKY 

(ess is short for essential) to be the L2-orthogonal complement in H−3(X, End a(X)) of the subspace 

V = {θ ∈ H −3(X, End a(T X )) | θ = LY J, Y ∈ W}.(1.11) Our main result is the following. 

Theorem 1.4. Let (X, g, J ) be a scalar-flat K¨ ahler ALE surface. Let −2 < δ < −1,

0 < α < 1, and k an integer with k ≥ 4 be fixed constants. Define 

j = dim R

(Hess (X, End a(T X )) ),(1.12) 

and let b2 denote the second Betti number of X. Let 

B = B1 × B2,(1.13) 

where B1 is an 1-ball in Hess (X, End a(T X )) , B2 is an 2-ball in H−3(X, Λ1,1) (both using the L2-norm). Define 

d = j + b2.(1.14) 

Then there is a family F of scalar-flat K¨ ahler metrics near g, parametrized by B, that is, there is a differentiable mapping 

F : B1 × B2 → M et (X),(1.15) 

into the space of smooth Riemannian metrics on X, with F = F (B1 × B2) satisfying the following “versal” property: there exists a constant 3 > 0 such that for any scalar-flat K¨ ahler metric ˜g ∈ B3 (g), there exists a diffeomorphism Φ : X → X, Φ ∈ Ck+1 ,α loc ,such that Φ∗ ˜g ∈ F, where 

B3 (g) = {g′ ∈ Ck,α loc (S2(T ∗X)) | ‖ g − g′‖Ck,α δ (S2(T ∗X)) <  3}.(1.16) 

Remark 1.5. The norm in (1.16) is a certain weighted H¨ older norm, see Section 2 for the precise definition. For a more precise description of the diffeomorphism Φ, see Theorem 9.2 below. In order to state our next result, we must recall some facts about vector fields and diffeomorphisms. If ( X, g ) is an ALE metric, and Y is a vector field on X, the Riemannian exponential mapping exp p : TpX → X induces a mapping ΦY : X → X(1.17) by ΦY (p) = exp p(Y ).(1.18) If Y ∈ Ck,α s (T X ) has sufficiently small norm, ( s < 0 and k will be determined in specific cases) then Φ Y is a diffeomorphism. We will use the correspondence Y 7 → ΦY

to parametrize a neighborhood of the identity, analogous to [Biq06]. 

Definition 1.6. We say that Φ : X → X is a small diffeomorphism if Φ is of the form Φ = Φ Y for some vector field Y satisfying 

‖Y ‖Ck+1 ,α δ+1 

<  4(1.19) for some 4 > 0 sufficiently small which depends on 3.DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 5

The family F is not necessarily “universal”, because some elements in F might be isometric. However, the following theorem shows that after taking a quotient by an action of the holomorphic isometries of the central fiber ( X, g, J ), the family F is in fact universal (up to small diffeomorphisms). 

Theorem 1.7. Let (X, g, J ) be as in Theorem 1.4, and let G denote the group of holomorphic isometries of (X, g, J ). Then there is an action of G on F with the following properties. 

• Two metrics in F are isometric if they are in the same orbit of G.

• If two metrics in F are isometric by a small diffeomorphism then they must be the same. 

Since each orbit represents a unique isometry class of metric (up to small diffeo-morphism), we will refer to the quotient M = F/G as the “local moduli space of scalar-flat K¨ ahler ALE metrics near g.” The local moduli space M is not a manifold in general, but its dimension is in fact well-defined, and we define 

m = dim( M).(1.20) 

Remark 1.8. We should point out that our local moduli space of metrics contains small rescalings, i.e, g 7 → 1 

> c2

g(c·, c ·) for c close to 1. If one considers scaled metrics as equivalent (which we do not), then the dimension would decrease by 1. 1.1. Deformations of the minimal resolution. As mentioned above, there are families of examples of scalar-flat K¨ ahler ALE metrics on minimal resolutions of isolated quotient singularities. For convenience, we next recall the definition of a minimal resolution. 

Definition 1.9. Let Γ ⊂ U(2) be as above. Then, a smooth complex surface X is called a minimal resolution of C2/Γ if there is a mapping π : X → C2/Γ such that the restriction π : X \ π−1(0) → C2/Γ \ { 0} is a biholomorphism, and π−1(0) is a divisor in X containing no −1 curves. The divisor π−1(0) is called the exceptional divisor .In the cyclic case, the exceptional divisor is a string of rational curves with normal crossing singularities. In the case that Γ is non-cyclic, it was shown by Brieskorn, see [Bri68], that the exceptional divisor is a tree of rational curves with normal crossing singularities. There are three Hirzebruch-Jung strings attached to a single curve, called the central rational curve . The self-intersection number of this curve will be denoted −bΓ, and the total number of rational curves will be denoted by kΓ.A specialized version of Theorem 1.4 is the following. 

Theorem 1.10. Let (X, g, J ) be any scalar-flat K¨ ahler ALE metric on the minimal resolution of C2/Γ, where Γ ⊂ U(2) is as above. Define 

jΓ = 2 

> kΓ

∑

> i=1

(ei − 1) ,(1.21) 6 JIYUAN HAN AND JEFF A. VIACLOVSKY 

where −ei is the self-intersection number of the ith rational curve, and kΓ is the number of rational curves in the exceptional divisor, and let 

dΓ = jΓ + kΓ.(1.22) 

Then there is a family, F, parametrized by a ball in RdΓ , of scalar-flat K¨ ahler metrics near g with the “versal” property stated in Theorem 1.4. The dimension mΓ of the local moduli space M is given in Table 1.1. 

Table 1.1. Dimension of local moduli space of scalar-flat K¨ ahler metrics Γ ⊂ U(2) dΓ mΓ13 (1 , 1) 5 2 

> 1
> p

(1 , 1) , p ≥ 4 2p − 1 2p − 5 

> 1
> p

(1 , q ), q 6 = 1 , p − 1 jΓ + kΓ jΓ + kΓ − 2non-cyclic, not in SU(2) jΓ + kΓ jΓ + kΓ − 1

Remark 1.11. The dimension of the moduli space of hyperk¨ ahler metrics is known to be 3 k − 3 in the Ak, D k and Ek cases for k ≥ 2, and equal to 1 in the A1 case [Kro86]. Our method of parametrizing by complex structures and K¨ ahler classes overcounts in this case (i.e., F is not injective), since a hyperk¨ ahler metric is K¨ ahler with respect to a 2-sphere of complex structures, see Section 11 for some further remarks. For other related results in the Ricci-flat case, see [CH14, CMR15]. Our final result applies to a generic deformation of the minimal resolution. 

Theorem 1.12. Let (X, g, J ) be any scalar-flat K¨ ahler ALE surface which deforms to the minimal resolution of C2/Γ, where Γ ⊂ U(2) is as above, through a smooth path of ALE K¨ ahler metrics. If G(g) = {e} then the local moduli space F is smooth near g and is a manifold of dimension m = mΓ.

Remark 1.13. The assumption that X deforms to the minimal resolution of C2/Γis reasonable. In [Joy00, Section 8.9], Joyce remarks that any K¨ ahler ALE surface with group Γ ⊂ U(2) is birational to a deformation of C2/Γ. There are several possible components of the deformation of such a cone, here we consider surfaces in the “Artin component” of deformations of C2/Γ. We note however that there are some known examples of scalar-flat K¨ ahler metrics on non-Artin components, which are free quotients of hyperk¨ ahler metrics of Ak-type, see for example [S ¸uv12]. We end the introduction with an outline of the paper. In Section 2, we begin with the definitions of the weighted H¨ older spaces which will be used throughout the paper. Then, in Section 3 we give some analysis of the complex analytic compactifications, due to Hein-LeBrun-Maskit [HL15, LM08], of K¨ ahler ALE spaces. In Section 4, we study the deformation of complex structures using an adaptation of Kuranishi’s theory to ALE spaces. The main point is that since the manifold is non-compact, the sheaf cohomology group H1(X, Θ) should be replaced by an appropriate space of decaying DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 7

harmonic forms. In Section 5, several key results about gauging and diffeomorphisms are proved, which are used to prove “versality” of the family constructed in Section 4. In Section 6, a refined gauging procedure is carried out, to construct the Kuranishi family of “essential” deformations. In Section 7, we generalize Kodaira-Spencer’s stability theorem for K¨ ahler structures to the ALE setting, using some arguments of Biquard-Rollin [BR15]. In Section 8, we adapt the LeBrun-Singer-Simanca theory of deformations of extremal K¨ ahler metrics to the ALE setting [LS93, LS94]. In Section 9, we prove the versal property of the family F, using a local slicing theorem, and prove Theorem 1.7. In Section 10, we restrict attention to the minimal resolution, and prove Theorems 1.10 and 1.12, and discuss the dimensions given in Table 1.1. In Section 11, we discuss several examples to illustrate the theory, and give more explicit formulas for the dimension of the moduli space mΓ. Finally, the Appendix contains some technical results about minimal resolutions needed in Section 10. 1.2. Acknowledgements. The authors would like to thank Olivier Biquard, Ronan Conlon, Akira Fujiki, Ryushi Goto, Hans-Joachim Hein, Nobuhiro Honda, and Claude LeBrun, for numerous helpful discussions on deformations of complex structures. Olivier Biquard, Joel Fine, and Jason Lotay provided crucial assistance with the slicing arguments. We would also like to thank Michael Lock for valuable discussions on properties of subgroups of U(2). 2. Notation 

We begin with the definition of weighted H¨ older spaces, which will be used through-out the paper. 

Definition 2.1. Let E be a tensor bundle on X, with Hermitian metric ‖ · ‖ h. Let ϕ

be a smooth section of E. We fix a point p0 ∈ X, and define r(p) to be the distance between p0 and p. Then define 

‖ϕ‖C0 

> δ

:= sup 

> p∈X

{

‖ϕ(p)‖h · (1 + r(p)) −δ

}

(2.1) 

‖ϕ‖Ckδ := ∑

> |I|≤ k

sup 

> p∈X

{

‖∇ I ϕ(p)‖h · (1 + r(p)) −δ+|I| 

}

,(2.2) where I = ( i1, . . . , i n), |I| = ∑nj=1 ij . Next, define [ϕ]Cαδ−α := sup 

> 0<d (x,y )<ρ inj

{

min {r(x), r (y)}−δ+α ‖ϕ(x) − ϕ(y)‖h

d(x, y )α

}

,(2.3) where 0 < α < 1, ρinj is the injectivity radius, and d(x, y ) is the distance between x

and y. The meaning of the tensor norm is to use parallel transport along the unique minimal geodesic from y to x, and then take the norm of the difference at x. The weighted H¨ older norm is defined by 

‖ϕ‖Ck,α δ

:= ‖ϕ‖Ckδ + ∑

> |I| =k

[∇I ϕ]Cαδ−k−α ,(2.4) 8 JIYUAN HAN AND JEFF A. VIACLOVSKY 

and the space Ck,α δ (X, E ) is the closure of {ϕ ∈ C∞(X, E ) : ‖ϕ‖Ck,α δ

< ∞} .

Remark 2.2. The dual space of H¨ older space is not a H¨ older space, but for the purpose of computing the dimension of cokernel of a Fredholm operator of order o,

H : Ck,α δ → Ck−o,α δ−o ,(2.5) we consider the adjoint operator as mapping between H¨ older spaces 

H∗ : Ck,α  

> −4−δ+o

→ Ck−o,α  

> −4−δ

,(2.6) since the adjoint weight to weight δ is −4 − δ, and using elliptic regularity. 3. ALE K¨ ahler surfaces 

In this section, we will prove several results about ALE K¨ ahler surfaces which will be needed later. We note that the results in this section do not use the scalar-flat assumption. In [LM08, HL15], LeBrun-Maskit and Hein-LeBrun analyzed the asymptotic be-havior of the metric and complex structure near infinity of ALE K¨ ahler surfaces. The next proposition gives a summary of their results. (See also [Li14] for other related results on complex analytic compactifications). 

Proposition 3.1 (Hein-LeBrun-Maskit) . Let X∞ be an end of an ALE K¨ ahler surface 

(X, g, J ) with metric g asymptotic to Euclidean metric at rate 

|∇ I

> Euc

(gj,k − δj,k )) | = O(ρ−|I|− 1−)(3.1) 

for |I| = 0 , 1 if  > 1/2 or for |I| = 0 , . . . , 4 if  ∈ (0 , 1/2] ; here ∇Euc denotes the Euclidean derivative. Then there is a surface S containing an embedded holomorphic curve C ' CP 1 with self-intersection 1, such that the universal cover ˜X∞ of X∞ is biholomorphic to S \ C.Let (X, g, J ) be a K¨ ahler ALE surface, then X has one end and can be analytically compactified to a smooth compact surface ˆX by adding a tree of rational curves E∞.The surface ˆX is a rational surface or a ruled surface. Also, X can be compactified to an orbifold surface ˆXorb by adding a single rational curve at ∞.

Remark 3.2. The orbifold compactification ˆXorb has cyclic singularities on the ratio-nal curve at ∞. The smooth compactification ˆX is obtained from ˆXorb by resolving these singularities. 

Remark 3.3. When Γ is trivial, the metric is asymptotically flat, in which case X

is biholomorphic to Bl p1,...,p k C2, see [HL15]. Consider the space of holomorphic vector fields on X with at most growth of order τ

Zτ (X, Θ) = {Z ∈ Γ( X, Θ) | ¯∂Z = 0 , Z = O(rτ ) as r → ∞} .(3.2) The first vanishing result we need is the following. DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 9

Proposition 3.4. Let (X, g, J ) be an ALE K¨ ahler surface. If τ < 0 then 

dim Zτ (X, Θ) = 0 .(3.3) 

Let 0 < τ < 1. If X is biholomorphic to C2, then 

dim Zτ (X, Θ) = 2 ,(3.4) 

otherwise, 

dim Zτ (X, Θ) = 0 .(3.5) 

Proof. Let X∞ = X \ B(R). Let R be sufficiently large, then by Proposition 3.1, the universal cover ˜X∞ can be analytically compactified by adding a rational curve C

at infinity, where C has self-intersection +1. By [HL15], there exists a smooth map [ξ1, ξ 2, f ] that maps S = ˜X∞ ∪ C to CP 2, which maps C holomorphically to {f = 0 }

as a curve CP 1 ⊂ CP 2, where 

ξj = {holomorphic part } + O(|f |3),(3.6) as f → 0. Let 

zj = xj + √−1yj = ξj

f , (j = 1 , 2) (3.7) where {x1, y 1, x 2, y 2} gives an ALE coordinate on ˜X∞, and |J − JEuc | = O(|z|−3) as 

z → ∞ . Let (v, w ) = 

( 1

z1

, z2

z1

)

(3.8) where {v = 0 } represents the complement of one point in C.First, let σ be a decaying holomorphic vector field on X, which can be lifted to ˜σ on ˜X∞. Note that ˜ σ can be extended to C2 smoothly by using a cut-off function. Since ¯∂ − ¯∂Euc = O(|z|−3) and ¯∂ ˜σ = 0 on ˜X∞,¯∂Euc ˜σ = ∑

> i,j

hi,j d¯zi ⊗ ∂∂z j

= O(|z|−3|σ|),(3.9) as z → ∞ . By using the ¯∂Euc -Poincar´ e lemma, there exist 

pj = O(|z|−2σ) ∈ C∞(C2), ¯∂p j = ∑

> i

hi,j d¯zi.(3.10) The formula for pj can be written out explicitly as follows. Let 

qj = 12π√−1

∫

> C

h2,j (z1, ζ 2)dζ 2 ∧ d¯ζ2

ζ2 − z2

q′ 

> j

= 12π√−1

∫

> C

(h1,j − ¯∂1qj )( ζ1, z 2)dζ 1 ∧ d¯ζ1

ζ1 − z1

,

(3.11) where the integral formula is valid since hi,j = o(|z|−3). Then pj = qj + q′ 

> j

. Then we have ˜ σ − ∑ 

> j

pj ∂∂z j is a decaying ¯∂Euc -holomorphic vector field on C2, which must 10 JIYUAN HAN AND JEFF A. VIACLOVSKY 

vanish identically. The growth rate of σ can be dropped by 2 iteratively by this argument, so we can assume that σ decays at any rate in the coordinates {z1, z 2}.Let σ∗ ∈ C∞(X, Ω1) denote the dual of σ with respect to the K¨ ahler metric g,˜σ∗ be the lifting of σ∗ on ˜X∞. The section ˜ σ∗ is also holomorphic and we have ˜σ∗ = O(|z|−10 ) as z → ∞ since we can assume ˜ σ decays to any order. The coordinate change gives: dz 1 = −1 

> v2

dv, dz 2 = 1 

> v

dw − wv2 dv , |z|2 = 1 

> |v|2

(1 + |w|2). Then ˜ σ∗ = O(|v|8)near C and can be extended to C with ˜ σ∗ = 0 on C. Consider the exact sequence 0 → N ∗ 

> C

→ Ω1|C → Ω1(C) → 0,(3.12) where Ω 1|C is the restriction of the bundle Ω 1 on C, Ω 1(C) is the cotangent bundle of C and NC is the normal bundle of C in S. Then we have Ω 1|C = O(−2) ⊕ O (−1). This implies ˜ σ∗ vanishes on any rational curve with self-intersection +1 on S. Since 

C has self-intersection +1, H1(C, N ∗ 

> C

⊗ Θ( C)) = 0, so C is rigid in S. Then there is an open neighborhood U ⊂ S of C, such that ˜ σ∗ vanishes identically over U . Then 

σ∗ vanishes on an open subset of X, which implies that σ∗ and σ vanishes identically on X.Finally, assume that σ ∈ Z τ (X, Θ) where 0 < τ < 1. In particular σ = 0. Since there is no indicial root between 0 and 1, σ admits an expansion with bounded leading term. Then σ can be lifted to ˜X∞ of the form {a ∂∂z 1 + b ∂∂z 2 + decaying terms },where a, b are constants. If Γ is nontrivial, then a ∂∂z 1 + b ∂∂z 2 is not Γ-equivariant, so 

a ∂∂z 1 + b ∂∂z 2 = 0, and σ vanishes by the argument above. From Remark 3.3, it is clear that dim( Zτ (X, Θ)) is equal to 2 only in the case that X is biholomorphic to C2, and is zero otherwise. 



Next, we consider harmonic (0 , 2)-forms with values in the holomorphic tangent bundle. 

Proposition 3.5. Let X be a K¨ ahler ALE surface. Then Hδ(X, Λ0,2 ⊗ Θ) = 0 , where 

δ ∈ (−2, −1) .Proof. The proposition follows an argument in [LM08, Theorem 4.2], with minor modifications. For completeness, we give a proof here following their idea. Let σ ∈Hδ(X, Λ0,2 ⊗ Θ). Recall that the conjugated Hodge star operator ¯ ∗ maps σ to a 

-harmonic form σ∗ ∈ H δ(X, Λ2,0 ⊗ Ω1). Let ˜ σ∗ be its lifting on ˜X∞ . Following the same notion as in the proof of Proposition 3.4, we have ˜σ∗ = ∑

> j

aj dz 1 ∧ dz 2 ⊗ dz j + O(|z|−3|˜σ∗|),(3.13) where aj are ¯∂Euc -holomorphic functions and aj = O(|z|δ) as z → ∞ . As shown in the proof of Proposition 3.4, aj = 0, so ˜ σ∗ = O(|z|δ−3) as z → ∞ . Since the growth rate of ˜ σ∗ can be dropped by 3 iteratively, ˜ σ∗ can decay to any order under the coordinate of {z1, z 2}, then ˜ σ∗ can be extended to C with ˜ σ∗ = 0 on C. Since Ω2,0 ⊗ Ω1|C = (Ω 1(C) ⊕ N ∗ 

> C

) ⊗ (Ω 2,0(C) ⊗ N ∗ 

> C

),(3.14) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 11 

we have Ω2,0 ⊗ Ω1|C = ( O(−2) ⊕ O (−1)) ⊗ (O(−2) ⊗ O (−1)) = O(−5) ⊕ O (−4) .(3.15) This implies that ˜ σ∗ vanishes on any rational curve with self-intersection +1 on ˜X∞.By the same argument as in Proposition 3.4, there is an open neighborhood U ⊂ S

of C, such that ˜ σ∗ vanishes identically over U . Then σ vanishes on an open subset of 

X, which implies that σ vanishes identically on X. 

The next Proposition shows that Hδ(X, Λ0,1 ⊗ Θ) automatically has a faster decay-ing rate. 

Proposition 3.6. Let X be an ALE K¨ ahler surface, and ˆX be its analytic compact-ification. Then for any −3 < τ < 0 we have 

Hτ (X, Λ0,1 ⊗ Θ) = H−3(X, Λ0,1 ⊗ Θ) ,(3.16) 

and if Γ is not cyclic or Γ = Z/2Z, then 

Hτ (X, Λ0,1 ⊗ Θ) = H−4(X, Λ0,1 ⊗ Θ) .(3.17) 

Proof. First, we will show that any decaying harmonic element φ ∈ H0(X, Λ0,1 ⊗ Θ) has a decay rate of at least O(r−3) at infinity. Since X is K¨ ahler, by [Mor07, Part 5], the operator  admits an expansion near infinity of the form 

 = 12∇∗∇ + R(3.18) on Λ 0,1 ⊗ Θ, where ∇ is the covariant derivative on Λ 0,1 ⊗ Θ, and R is an operator given by curvature forms acting on the same bundle. The leading term of ∇∗∇ is the Euclidean Laplacian ∆ Euc , so we have 

 = 12∆Euc + Q, (3.19) where Q denotes lower order terms. The element φ admits an expansion of the form 

φ = f + O(r−3+ ),(3.20) as r → ∞ , where f is of the form 

f = ∑

> i,j

fi,j 

r2 d¯zi ⊗ ∂∂z j

,(3.21) and fi,j are constants. Since φ is -harmonic, both ¯∂f = 0 and ¯∂∗f = 0. It is easy to see that this implies that each fi,j = 0. Consequently, φ = O(r−3+ ) as r → ∞ .Since φ admits an expansion with harmonic leading term, we must have φ = O(r−3). Furthermore, if Γ is not cyclic or Γ = Z/2Z, then Γ contains the element −1. The leading term of φ is of the form 

f = ∑

> k,l

Akl 

r4 d¯zk ⊗ ∂∂z l

,(3.22) 12 JIYUAN HAN AND JEFF A. VIACLOVSKY 

where Akl is a linear combination of z1, ¯z1, z 2, ¯z2. Since any such nonzero f is not invariant under the action of −1, we must have f = 0, and then φ = O(r−4). This finishes the proof of (3.16) and (3.17). 



The following Proposition will be used in Section 7. 

Proposition 3.7. Let (X, g, J ) be an ALE K¨ ahler surface. Then 

b1(X) = 0 ,(3.23) 

where b1(X) denotes the first Betti number of X. Furthermore, for τ < 0,

dim( Hτ (X, Λ0,2)) = dim( Hτ (X, Λ2,0)) = 0 .(3.24) 

Proof. Let U be a tubular neighborhood of E∞, ˆX = X ∪E∞ be the analytic compact-ification of X. By Proposition 3.1, ˆX is either a rational surface or a ruled surface, then b1( ˆX) = 0. Since E∞ is a tree of rational curves, b1(U ) = 0 and b1(X ∩ U ) = 0. Then by the Mayer-Vietoris theorem, b1(X) = 0. Since dim( Hτ (X, Λ0,2)) = dim( Hτ (X, Λ2,0)), we just need to show the latter one equals to zero. The proof is similar to the proof of Proposition 3.5, so we will skip some details. For any σ ∈ H τ (X, Λ2,0), let ˜ σ be its lifting on ˜X∞. Then ˜σ = a · dz 1 ∧ dz 2 + O(|z|−3 ˜σ)(3.25) where a = O(|z|τ ) as r → ∞ is a ¯∂Euc -holomorphic function. Then a = 0, and ˜σ = O(|z|−3+ τ ), which implies that ˜ σ can decay to any order in the ALE coordinates 

{z1, z 2}. Consequently, ˜ σ can be extended to C. Furthermore, Ω2,0|C = Ω 2,0(C) ⊗ N ∗ 

> C

= O(−3) .(3.26) This implies that ˜ σ vanishes on an open neighborhood of C, so σ vanishes identically on X.



4. Small deformations of complex structure 

First we need a fixed point theorem for operators on Banach spaces (see, for example [BR15]). 

Lemma 4.1. Let F : B1 → B 2 be a bounded differentiable operator between Banach spaces. In a small neighborhood of 0 ∈ B 1, F (x) = F (0) + F ′(0) x + Q(x), where 

‖Q(x) − Q(x′)‖B2 ≤ C0 · (‖x‖B1 + ‖x′‖B1 ) · ‖ x − x′‖B1 .(4.1) 

Assume that ‖F (0) ‖B2  1. Then (i) If F ′(0) is an isomorphism with right inverse G bounded by C1, then there exists a ball B(0 , s ) ⊂ B 1 such that there exists a unique x ∈ B(0 , s ) with F (x) = 0 .(ii) If F ′(0) is Fredholm and surjective, with right inverse bounded by C1, then there is an s > 0, so that F −1(0) ∩ B(0 , s ) is isomorphic to U ⊂ ker( F ′(0)) , where U is a small neighborhood of the origin. DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 13 

The following lemma gives the properties of the linearized operator we will need in order to invoke Lemma 4.1. 

Lemma 4.2. Let (X, g, J ) be a K¨ ahler ALE surface. The linear operator 

P : Ck,α δ−1(X, Λ0,1 ⊗ Θ) ( ¯∂∗, ¯∂)

−−−→ Ck−1,α δ−2 (X, Θ) ⊕ Ck−1,α δ−2 (X, Λ0,2 ⊗ Θ) (4.2) 

is surjective and Fredholm, for some k ≥ 3 and δ ∈ (−2, −1) .Proof. It is not hard to see that P is an elliptic operator, and that the indicial roots of P are integral. Consequently, by standard weighted space theory, P is Fredholm since δ is non-integral [LM85]. The cokernel is given by ker( P ∗) = {(σ1, σ 2) ∈ Ck−1,α  

> −2−δ

(Θ) ⊕ Ck−1,α  

> −2−δ

(Λ 0,2 ⊗ Θ) : ¯∂∗σ2 = ¯∂σ 1}.(4.3) Let ( σ1, σ 2) ∈ ker( P ∗), then ¯∂∗σ1 = 0 , ¯∂∗ ¯∂σ 1 = ¯∂∗ ¯∂∗σ2 = 0 ,(4.4) which implies that σ1 is -harmonic. From Proposition 3.4, σ1 = 0. Then ¯∂σ 2 = 0 , ¯∂∗σ2 = 0 ,(4.5) and the vanishing of σ2 follows from Proposition 3.5. Since ker( P ∗) = 0, and P is Fredholm, P is surjective. 

Now we prove a weighted version of Kuranishi’s theorem. 

Theorem 4.3. Let (X, J 0, g 0) be a K¨ ahler ALE surface, and let B1 be an 1-ball around 0 in H−3(X, Λ0,1 ⊗ Θ) . Then there is a differentiable family of complex struc-tures Jt for t ∈ B1 such that 

Jt = J0 + φ(t), φ (t) ∈ Ck,α δ−1(X, Λ0,1 ⊗ Θ) , δ ∈ (−2, −1) , k ≥ 3(4.6) 

where φ(t) satisfies 

φ(t) = t + φ(t)⊥,(4.7) 

where φ(t)⊥ is L2-orthogonal to H−3(X, Λ0,1 ⊗ Θ) , and 

¯∂∗(φ(t)) = 0 .(4.8) 

Furthermore, there exists an ′ > 0, such that if J = J0 + φ is any integrable complex structure satisfying 

‖φ‖Ck,α δ−1

<  ′, and ¯∂∗(φ) = 0 ,(4.9) 

then φ is in the family Jt.Finally, for any t ∈ B1 , there exists a constant C such that ‖φ(t)‖Ck,α 

> −3

≤ C · 1.14 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Proof. Define the operator 

F : Ck,α δ−1(X, Λ0,1 ⊗ Θ) → Ck−1,α δ−2 (X, Θ) ⊕ Ck−1,α δ−2 (X, Λ0,2 ⊗ Θ) 

φ 7 → ( ¯∂∗φ, ¯∂φ + [ φ, φ ]) ,

(4.10) where [ φ, φ ] is a globally defined operator, which can be expressed locally as [φ, φ ] = 12

[ ∑ 

> i,j

φi,j d¯zi ⊗ ∂∂z j

, ∑

> k,l

φk,l d¯zk ⊗ ∂∂z l

]

(4.11) = ∑

> i,j,k,l

φi,j 

∂φ k,l 

∂z j

d¯zi ∧ d¯zk ⊗ ∂∂z l

.(4.12) Formally, [ φ, φ ] can be written as φ ∗ ∇ φ, where ∗ means a linear combination of quadratic terms, each involving some contraction of φ with ∇φ.Clearly, F is a bounded differentiable mapping, and F ′(0) = ( ¯∂∗, ¯∂). Obviously, in a small neighborhood of 0 in Ck,α δ−1(X, Λ0,1 ⊗ Θ), F admits an expansion F =

F (0) + F ′(0) + Q. We next prove the estimate (4.1). Let r denote the radius. For any two elements φ, φ ′ ∈ Ck,α δ−1(Λ 0,1 ⊗ Θ), we have 

r2−δ|[φ, φ ] − [φ′, φ ′]| = r2−δ|[φ ∗ ∇ φ] − [φ′ ∗ ∇ φ′]|

= r2−δ|φ ∗ (∇φ − ∇ φ′) − (φ − φ′) ∗ ∇ φ′|≤ rδ−1{r1−δ|φ|r2−δ|∇ φ − ∇ φ′| + r1−δ|φ − φ′|r2−δ|∇ φ′|} ≤ rδ−1(r1−δ(|φ| + |φ′|))( r2−δ(|φ − φ′| + |∇ φ − ∇ φ′|)) .

(4.13) Next, let x 6 = y ∈ X, with r(x) < r (y). Similarly, we have 

r(x)2−δ |([ φ, φ ] − [φ′, φ ′])( x) − ([ φ, φ ] − [φ′, φ ′])( y)|

d(x, y )α

≤ r(x)δ−1

{

r(x)1−δ |φ(x) − φ(y)|

d(x, y )α |∇ φ(x) − ∇ φ′(x)|r(x)2−δ

}

+

r(y)δ−1

{

r(x)2−δ |(∇φ(x) − ∇ φ′(x)) − (∇φ(y) − ∇ φ′(y)) |

d(x, y )α |φ(y)|r(y)1−δ

}

+

r(x)δ−1

{

r(x)1−δ |(φ(x) − φ′(x)) − (φ(y) − φ′(y)) |

d(x, y )α |∇ φ′(x)|r(x)2−δ

}

+

r(y)δ−1

{

r(x)2−δ |∇ φ′(x) − ∇ φ′(y)|

d(x, y )α |φ(y) − φ′(y)|r(y)1−δ

}

.

(4.14) This shows that 

‖[φ, φ ] − [φ′, φ ′]‖C0,α δ−2

≤ C0(‖φ‖C1,α δ−1

+ ‖φ′‖C1,α δ−1

)‖φ − φ′‖C1,α δ−1

.(4.15) The higher derivative terms can be handled similarly, to prove 

‖[φ, φ ] − [φ′, φ ′]‖Cj−1,α δ−2

≤ Cj (‖φ‖Cj,α δ−1

+ ‖φ′‖Cj,α δ−1

)‖φ − φ′‖Cj,α δ−1

, 1 ≤ j ≤ k(4.16) which shows that Q satisfies (4.1). DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 15 

By Lemma 4 .2, we know P = F ′(0) is Fredholm. We can choose a right inverse operator G such that the image of G is L2-orthogonal to H−3(X, Λ0,1 ⊗ Θ). By Lemma 4.1, we have that F −1(0) is locally isomorphic to a small neighborhood of 0 in Hδ−1(X, Λ0,1 ⊗ Θ), such that for each t ∈ B1 , there is a φ(t) = t + φ(t)⊥ ∈ F −1(0), where φ(t)⊥ is L2-orthogonal to H−3(X, Λ0,1 ⊗ Θ), and J0 + φ(t) is the corresponding complex structure. It is a straightforward consequence of the implicit function the-orem that the mapping ψ : t 7 → φ(t) is differentiable. This finishes the proof of the existence of the family of complex structures. By the fixed point Lemma 4.1, near 0, the zero set of ( ¯∂∗, ¯∂ +[ , ]) is locally bijective to the kernel of ( ¯∂∗, ¯∂), which is H−3(X, Λ0,1 ⊗ Θ). Thus there exists an ′ > 0 such that for any ‖φ‖Ck,α δ−1

<  ′, ¯∂∗φ = 0, ¯∂φ + [ φ, φ ] = 0, then J = J0 + φ is in the family we just constructed. Next we will show that φ(t) ∈ Ck,α  

> −3

(X, Λ0,1 ⊗ Θ) for t ∈ B1 . In fact, we will show that for any φ ∈ Ck,α δ (X, Λ0,1 ⊗ Θ) that satisfies the system ¯∂φ = −[φ, φ ], ¯∂∗φ = 0 ,(4.17) then φ ∈ Ck,α  

> −3

(X, Λ0,1 ⊗ Θ). To see this, (4.17) implies that φ ∈ Ck−2,α  

> 2δ−2

(X, Λ0,1 ⊗ Θ). Then outside of a compact subset, ∆Euc φ = φ + (∆ Euc − )φ = O(r2δ−2),(4.18) which implies that 

φ = ∑

> i,j

ai,j 

r2 d ¯zi ⊗ ∂∂z j

+ O(r−3+ ),(4.19) where ai,j are constants and ai,j  

> r2

is ∆ Euc -harmonic. By the same argument as in the proof of (3.16), we have ai,j = 0. Then a similar argument shows that φ ∈

Ck,α  

> −3

(X, Λ0,1 ⊗ Θ). The last statement follows from finite-dimensionality of the kernel. 



5. Versality of Kuranishi family 

The next result shows that any nearby complex structure can be brought into the family Jt by a suitable diffeomorphism. Of course, the implicit function theorem requires a mapping between Banach spaces to be differentiable. The following lemma, inspired by [Biq06], will be used below to this end. 

Lemma 5.1. Let (X, g 0, J 0) be a K¨ ahler ALE surface with g0 ∈ C∞. Then for any sufficiently small  > 0, for any smooth K¨ ahler ALE metric ‖g − g0‖Ck,α δ

<  , there exists an 1 > 0, such that for an 1-ball B1 ⊂ Ck+1 ,α δ+1 (T X ), the map ΨΨ : B1 → Ck,α δ (S2(T ∗X)) 

Y 7 → ΦY ∗g − g

(5.1) 

is smooth. 16 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Proof. First, for any g such that ‖g − g0‖Ck,α δ

<  where  is sufficiently small, there exist constants λ, i 0, such that ‖Ric (g)‖Ck−2,α ≤ λ, ρinj (g) ≥ i0 > 0. Then, following [And90], for any 2 > 0, there exists a cover of harmonic coordinate charts {Brs (xs)},such that rs ≥ rharm , where rharm = rharm (λ, i 0,  2, k, α ) > 0, and for any y ∈ Brs (xs), 

gij (xs) = δij , (1 + 2)−1δij ≤ gij (y) ≤ (1 + 2)δij , r k+αharm |gij (y)|Ck,α ≤ (1 + 2),(5.2) where ( u1, . . . , u 4) is the harmonic coordinate of Brs (xs), and gij (y) = g(y)( ∂∂u i , ∂∂u j ). Now let Y ∈ Ck+1 ,α (T B rs (xs)), with ‖Y ‖Ck+1 ,α <  3, where 3 > 0. Note that Y has at least the same regularity in harmonic coordinates as in the original ALE coordinates. Then Y can be represented as Y = ∑4 

> j=1

Yj ∂∂u j , where each Yj ∈ Ck+1 ,α (Brs (xs)). Fix any y ∈ Brs (xs), and indices i, j , and define Gij (Y ) = (Φ Y )∗gij (y). Then for any positive integer L, when 3 is sufficiently small, Gij (Y ) has the Taylor expansion: 

Gij (Y ) = ∑

> |L|≤ L

DLGij (0) Y l1 

> 1

. . . Y ln

> n

l1! · . . . · ln! + O(|Y |L+1 ),(5.3) where L denotes a multi-index, as |Y | → 0. There exist similar expansions for 

GI 

> ij

(Y ) = ( ∇I ΦY ∗g)y

( ∂∂u i

, ∂∂u j

)

,(5.4) with |I| ≤ k + α. Note that (Φ Y )∗g(y) = ∑

> i,j

Gij d((Φ Y )∗ui) ⊗ d((Φ Y )∗uj ),(5.5) and similar Taylor expansions hold for (Φ Y )∗ui. These expansions imply that Ψ is smooth over an 3-ball B3 ⊂ Ck+1 ,α (T B rs (xs)), i.e, for Ψ|Brs (xs) : B3 → Ck,α (S2(T ∗Brs (xs))) ,(5.6) the Lth-differential DLΨ exists, and ‖DLΨ‖ ≤ C, where C = C(λ, i 0,  2, k, α, L ) is independent of the choice of harmonic coordinate chart. Denote by A1,2 a Euclidean annulus of radius between 1 and 2, with a metric satifying the boundeness assumptions at the beginning. Since A1,2 can be obviously be covered by finitely many harmonic coordinate charts, by the argument above, Ψ |A1,2 is smooth. Then by a standard dilation argument, which dilates AR, 2R to A1,2, we have for B3 ⊂ Ck+1 ,α δ+1 (T A R, 2R), Ψ|AR, 2R : B3 → Ck,α δ (S2(T ∗AR, 2R)) (5.7) is smooth, and there exists a constant C = C(λ, i 0,  2, k, α, L ), such that the estimate 

‖DLΨ|AR, 2R ‖ ≤ C holds. Note that C is indepedent of the dilation factor R. Since we can choose R arbitarily large, then for 1 > 0 sufficiently small, we have for 

B1 ⊂ Ck+1 ,α δ+1 (T X ), Ψ : B1 → Ck,α δ (S2(T ∗X)) (5.8) is smooth as a mapping between Banach spaces. DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 17 

Lemma 5.2. Let (X, J 0, g 0) be a K¨ ahler ALE surface with g0 ∈ C∞. There exists an ′ 

> 1

> 0 such that for any complex structure ‖J1 − J0‖Ck,α δ

<  ′

> 1

, where k ≥ 3, α ∈

(0 , 1) , δ ∈ (−2, −1) , there exists a unique diffeomorphism Φ, of the form ΦY for 

Y ∈ Ck+1 ,α δ+1 (T X ) such that δ0(Φ ∗(J1)) = 0 . Consequently, Φ∗(J1) is in the family Jt

from Theorem 4.3. Proof. Let J1 = J0 + φ, where ‖φ‖Ck,α δ

<  ′ 

> 1

for some small ′ 

> 1

to be determined later, and ¯∂φ + [ φ, φ ] = 0. Note that δ0J0 = 0 since ω0 = √−12 g0(J0·, ·) is K¨ ahler. Define the operator N as: 

Ck+1 ,α δ+1 (T X ) × Ck,α δ (X, Λ0,1 ⊗ Θ) → Ck−1,α δ−1 (T ∗X)(Y, φ ) 7 → δΦY ∗g0 (J0 + φ),

(5.9) where Φ Y is defined in (1.18), and δΦY ∗g0 is the divergence operator associated to metric g0. Note that 

δΦY ∗g0 (J0 + φ) = 0 ⇔ δg0 Φ∗ 

> Y

(J0 + φ) = 0 ,(5.10) so a zero of N satisfies the desired gauge condition. (The latter map is not differen-tiable, which is why we consider the former, see [Biq06].) By Lemma 5.1, Φ Y ∗g0 acts smoothly on Ck+1 ,α δ+1 (T X ), so Φ Y ∗g0 has the expansion: ΦY ∗g0 = g0 + h(5.11) where ‖h‖Ck,α δ

≤ C‖Y ‖Ck+1 ,α δ+1 

, for Y sufficiently small. In particular, we have the estimate |h| ≤ Cr δ‖Y ‖Ck+1 ,α δ+1 

. We also have the expansion of ∇ΦY ∗g0

∇ΦY ∗g0 = ∇g0 + A1 + A2,(5.12) where A1 is the linear order term, and by the expansion formula 

∇g0+h = ∇g0 + ( g0 + h)−1 ∗ ∇ g0 h, (5.13) [GV16, Formula 3.39], and the estimate of h, we have 

|A1| ≤ C · rδ−1‖Y ‖Ck+1 ,α δ+1 

;(5.14) 

A2 denotes the lower order terms, and |A2| ≤ C · rδ−2‖Y ‖Ck+1 ,α δ+1 

. Then the divergence operator δΦY ∗g0 admits an expansion 

δΦY ∗g0 = δg0 + δ1 + δ2,(5.15) where 

δ1 = h ∗ ∇ g0 + g0 ∗ A1, δ 2 = δΦY ∗g0 − δg0 − δ1,(5.16) and ∗ means a linear combination of tensor contractions. By the expansion of δΦY ∗g0 ,it is clear that δΦY ∗g0 (J0 + φ) ∈ Ck−1,α δ−1 (T ∗X), and N is well-defined bounded map between corresponding Banach spaces. A similar argument shows that N is smooth. Note that the exponential map and the one-parameter group of diffeomorphisms 18 JIYUAN HAN AND JEFF A. VIACLOVSKY 

induced by a vector field both have the same linearization at time 0. Consequently, at (0 , 0), the linearization of N restricted to the tangent space of the first variable is 

D N0 : Ck+1 ,α δ+1 (T X ) → Ck−1,α δ−1 (T ∗X)

Y 7 → δ0LY J0 = 0Y, 

(5.17) where the adjoint operator of D N0 is: (D N0)∗ : Ck+1 ,α  

> −3−δ

(T ∗X) → Ck−1,α  

> −5−δ

(T X )

η 7 → (0η)#.

(5.18) The kernel of ( D N0)∗ consists of those η ∈ Ck+1 ,α  

> −3−δ

(T ∗X) such that ( 0η)# = 0, which implies that η# is the real part of a holomorphic vector field. From Proposition 3.4, 

η = 0. Since the cokernel of D N0 is trivial, D N0 is surjective. Note also that the kernel of D N0 is trivial. Of course, in a small neighborhood of (0 , 0) in Ck+1 ,α δ+1 (T X ) × Ck,α δ (X, Λ0,1 ⊗ Θ), 

D N is surjective. Since N is smooth, condition (4.1) is satisfied, so by Lemma 4.1, there exists a unique diffeomorphism Φ Y such that Φ ∗ 

> Y

J1 − J0 is divergence-free. Since Φ ∗ 

> Y

(J1) − J0 satisfies equations (4.17), following the last part of the proof in Theorem 4.3, Φ ∗ 

> Y

(J1) − J0 ∈ Ck,α  

> −3

(X, Λ0,1 ⊗ Θ). Then by Theorem 4.3, Φ ∗ 

> Y

(J1) is in the family Jt. 

6. Essential deformations of complex structure 

The aruments in this section are inspired by [CT94, Theorem 3.1], with some appropriate modifications for the smoothness arguments. Recall that the space W is defined as 

W = {Y ∈ H 1(X, T X ) | LY g0 = O(r−1), LY J0 = O(r−3), as r → ∞} .(6.1) Clearly, W is finite-dimensional. Next, we prove two lemmas which will be important in the subsequent gauging theorem. 

Lemma 6.1. For Z ∈ W sufficiently small, the time-one flow for the one-parameter group of diffeomorphisms generated by Z exists. Furthermore, there exist a matrix 

A ∈ U(2) and vector ˆ0 ∈ C2, such that in ALE coordinates, 

d(Φ Z (x), Ax + ˆ 0) = O(r−2+ ),(6.2) 

as r → ∞ , for any  > 0.Proof. First, note that Z ∈ W admits an expansion 

Z = Z1 + Z0 + Z−2+ ,(6.3) for any  > 0, where Z1 is in the Lie algebra of U(2), Z0 is vector field with constant coefficients, and Z−2+  = O(r−2+ ) as r → ∞ . To see this, by standard harmonic expansion for kernel elements of 0, we have that any Z ∈ W satisfies 

Z = Z1 + Z0 + O(r−1+ ),(6.4) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 19 

where Z1 is any vector field which is homogeneous of degree one, and Z0 is a vector field with constant coefficients. The conditions that LZ g0 = O(r−1) and LZ J0 = O(r−3)as r → ∞ imply that LZ1 gEuc = 0 and LZ1 JEuc = 0, that is, Z1 is in the Lie algebra of U(2). Next, 

LZ1+Z0 J0 = LZ1+Z0 (J0 − JEuc ) = LZ1+Z0 (O(r−3)) ,(6.5) which implies that 

LZ0+Z1 J0 = O(r−3),(6.6) as r → ∞ . Consequently, 

0(Z − Z1 − Z0) = O(r−4).(6.7) Since there is no harmonic term of degree −1, the claimed expansion (6.3) follows. Clearly for Z sufficiently small in norm, the one-parameter group of diffeomor-phisms which is defined by 

x′(t) = Z(x(t)) , x (0) = x, (6.8) exists by the standard short-time existence theorem for ODEs. By the expansion (6.3), x(t) will be given by a family of rotations in U(2), and translations plus decaying terms. 

Next, for Z ∈ W, we define Φ Z : X → X to be time-one flow for the one-parameter group of diffeomorphisms generated by Y . Note that this is different from the defini-tion given in (1.18). The next lemma states some useful properties of W, which will be needed in the proof of the subsequent gauging theorem. 

Lemma 6.2. Let (X, J 0, g 0) be a K¨ ahler ALE surface, the space W satisfies the following properties: 

• There exists a small neighborhood U ⊂ W of 0, and an ′ > 0 such that if g1 is any metric satisyfing ‖g1 − g0‖Ck,α δ

<  ′, then there exists a constant C, such that for any Z ∈ U ,

‖Φ∗ 

> Z

g1 − g0‖Ck,α δ

≤ C(‖Z‖Ck+1 ,α 

> 1

+ ′).(6.9) 

• Given  > 0 sufficiently small, for any complex structure J1 = J0 + φ such that 

‖φ‖Ck,α 

> −3+ 

<  ′ for some sufficiently small ′, there exists a small neighborhood 

U ⊂ W of 0, and a constant C, such that for any Z ∈ U ,

‖Φ∗ 

> Z

J1 − LZ J1 − J0‖Ck,α 

> −3+ 

≤ C · (‖Z‖Ck+1 ,α 

> 1

)2 + ′.(6.10) 20 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Proof. First, we address the estimate (6.9). Let Φ A, ˆ0 denote the mapping x 7 → Ax +ˆ 0.Using Lemma 6.1, 

|Φ∗ 

> Z

g1 − g0| = |Φ∗ 

> Z

g1 − g1 + g1 − g0| ≤ | Φ∗ 

> Z

g1 − g1| + |g1 − g0|≤ | (Φ A, ˆ0 + O(r−2+ )) ∗(δij + O(rδ)) − (δij + O(rδ)) | + ′rδ

≤ C‖Z‖Ck+1 ,α 

> 1

rδ + ′rδ + o(rδ)

≤ Cr δ(‖Z‖Ck+1 ,α 

> 1

+ ′).

as r → ∞ . Since Φ Z is the time one flow of Z ∈ W, and W is finite-dimensional, a similar estimate holds on any compact subset of X, so the C0 

> δ

part of the norm is bounded by the right hand side of (6.9). Higher regularity estimates are similar, and are omitted. Next we will discuss (6.10). As in the first part, since W is finite-dimensional, we only need to make estimates outside of a compact set BR(p0), where a global coordinate exists. Let γ : [0 , 1] → X be the path γ(t) = Φ tZ (x). First, we estimate 

r(x)3−|Φ∗ 

> Z

J0 − J0 − LZ J0|(x) ≤ Cr 3−

∫ 10

|Φ∗ 

> tZ

(LZ J0)( γ(0)) − LZ J0(γ(0)) |dt 

≤ Cr 3−

∫ 10

∫ t

> 0

|LZ (LZ J0)( γ(s)) |dsdt. 

(6.11) By the expansion (6.3), given c > 0, the estimates (1 − c)r(γ(s)) ≤ r(x) = r(γ(0)) ≤ (1 + c)r(γ(s)) (6.12) are satisfied for all Z sufficiently small in norm. Also, 

|LZ (LZ J0)|(γ(s)) ≤ Cr (γ(s)) −5|Z(γ(s)) |2,(6.13) so we have 

r(x)3−|Φ∗ 

> Z

J0 − J0 − LZ J0|(x) ≤ C

∫ 10

∫ t

> 0

r(γ(s)) 3−r(γ(s)) −5|Z|2(γ(s)) dsdt 

≤ C

∫ 10

∫ t

> 0

r(γ(s)) −2−|Z|2(γ(s)) dsdt ≤ C‖Z‖2

> Ck+1 ,α
> 1

.

(6.14) Next, we estimate 

r(x)3−|Φ∗ 

> Z

φ − φ − LZ φ|(x) ≤ Cr 3−

∫ 10

|Φ∗ 

> tZ

(LZ φ)( γ(0)) − LZ φ(γ(0)) |dt 

≤ Cr 3−

∫ 10

∫ t

> 0

|LZ (LZ φ)( γ(s)) |dsdt. 

(6.15) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 21 

Since |LZ (LZ φ)|(γ(s)) ≤ Cr (γ(s)) −5+ |Z|2(γ(s)), similarly, we have the estimate 

r(x)3−|Φ∗ 

> Z

φ − φ − LZ φ|(x) ≤ C

∫ 10

∫ t

> 0

r(γ(s)) 3−(r(γ(s)) −5+ |Z|2(γ(s))) dsdt 

≤ C

∫ 10

∫ t

> 0

r(γ(s)) −2|Z|2(γ(s)) dsdt ≤ C‖Z‖2

> Ck+1 ,α
> 1

.

(6.16) It follows that 

r(x)3−|Φ∗ 

> Z

J1 − J1 − LZ J1|(x)

≤ r(x)3−{| Φ∗ 

> Z

J0 − J0 − LZ J0|(x) + |Φ∗ 

> Z

φ − φ − LZ φ|(x)} ≤ C‖Z‖2

> Ck+1 ,α
> 1

,

(6.17) where C is uniform for all Z ∈ W of sufficiently small norm. Higher derivative estimates are similar, and are omitted. Finally, (6.10) follows from 

‖Φ∗ 

> Z

J1 − J0 − LZ J1‖Ck,α 

> −3+ 

≤ ‖ Φ∗ 

> Z

J1 − J1 − LZ J1‖Ck,α 

> −3+ 

+ ‖φ‖Ck,α 

> −3+ 

≤ C · ‖ Z‖2

> Ck+1 ,α
> 1

+ ′.

(6.18) 



Recall that 

V = {θ ∈ H −3(X, End a(T X )) | θ = LY J, Y ∈ W}.(6.19) The deformations of complex structure arising from elements of V become trivial if one takes into account changes of coordinates at infinity, as the following theorem shows. 

Theorem 6.3. Let (X, J 0, g 0) be a K¨ ahler ALE surface with g0 ∈ C∞. There exists an ′ 

> 1

> 0 such that for any complex structure ‖J1 − J0‖Ck,α δ

<  ′

> 1

, where k ≥ 3, α ∈

(0 , 1) , δ ∈ (−2, −1) , there exists a diffeomorphism Φ, of the form ΦY1 ◦ ΦZ ◦ ΦY2

for Y1, Y 2 ∈ Ck+1 ,α δ+1 (T X ) and Z ∈ W, such that δ0(Φ ∗(J1) − J0) = 0 , and such that 

Φ∗(J1) − J0 is L2-orthogonal to V. Furthermore, there exists a constant C so that 

‖Φ∗J1 − J0‖Ck,α 

> −3

< C ′

> 1

.(6.20) 

Proof. Let J1 = J0 + φ, where φ ∈ Ck,α δ (X, Λ0,1 ⊗ Θ), and ¯∂φ + [ φ, φ ] = 0. By Lemma 5.2 and Theorem 4.3, without loss of generality, we may assume that φ(t) ∈

Ck,α  

> −3

(X, Λ0,1 ⊗ Θ). Define the operator N as: 

Ck+1 ,α  

> −2+ 

(T X ) × Ck,α 

> −3+ 

(Λ 0,1 ⊗ Θ) × W → Ck−1,α  

> −4+ 

(T ∗X) × Rm

(Y, φ, Z ) 7 →

{

δΦY ∗g0 (Φ ∗ 

> Z

(J0 + φ(t))) ,

∫

〈Φ∗ 

> Z

(J0 + φ), ΦY ∗v1〉ΦY ∗g0 dV ΦY ∗g0 ,

· · · ,

∫

〈Φ∗ 

> Z

(J0 + φ), ΦY ∗vm〉ΦY ∗g0 dV ΦY ∗g0

}

,

(6.21) 22 JIYUAN HAN AND JEFF A. VIACLOVSKY 

where 0 <   1, δΦY ∗g0 is the divergence operator associated to the metric Φ Y ∗g0,

m = dim( V), {v1, . . . , v m} is an orthonormal basis of V. Recall that Φ Y is induced by the exponential map of the decaying field Y . By Lemma 5.1 with domain weight 

−3 + , the mapping Y 7 → ΦY ∗g0 − g0 is smooth, so we have the following expansions as shown in the proof of Lemma 5.2: ΦY ∗g0 = g0 + h, (6.22) where h satisfies |h| ≤ C · r−3+ ‖Y ‖Ck+1 ,α 

> −2+ 

. Also, 

∇ΦY ∗g0 = ∇g0 + A1 + A2(6.23) where A1 is the linear order term, satisfying |A1| ≤ C ·r−4+ ‖Y ‖Ck+1 ,α 

> −2+ 

, and A2 denotes the lower order terms, satisfying |A2| ≤ C · r−5+ ‖Y ‖Ck+1 ,α 

> −2+ 

.The divergence operator δΦY ∗g0 admits an expansion 

δΦY ∗g0 = δg0 + δ1 + δ2,(6.24) where 

δ1 = h ∗ ∇ g0 + g0 ∗ A1, δ 2 = δΦY ∗g0 − δg0 − δ1.(6.25) We also have the expansion Φ∗ 

> Z

(J0 + φ(t)) = I + II + III, (6.26) where 

I = J0 + φ(t)

II = LZ (J0 + φ(t)) 

III = Φ ∗ 

> Z

(J0 + φ(t)) − I − II. 

(6.27) with 

|II | ≤ | ¯∂0Z| + |LZ φ(t)| ≤ C · r−3+ (1 + ′

> 1

)‖Z‖Ck+1 ,α 

> 1

(6.28) and by (6.10) 

|III | ≤ C · r−3+  · (′ 

> 1

+ ‖Z‖2

> Ck+1 ,α
> 1

).(6.29) By direct computation, we have 

|δg0 I| = |δg0 φ(t)| ≤ ′ 

> 1

· r−4+ 

|δg0 II | = |0Z + δg0 (LZ φ(g)) | ≤ (C + ′

> 1

) · r−4+ ‖Z‖Ck+1 ,α 

> 1

|δg0 III | ≤ C · r−4+ (‖Z‖2

> Ck+1 ,α
> 1

+ ′

> 1

).

(6.30) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 23 

Also by the above estimates we have 

|δ1I| = |h ∗ ∇ g0 φ(t) + g0 ∗ A1(J0 + φ(t)) | ≤ (C + ′

> 1

) · r−4+ ‖Y ‖Ck+1 ,α 

> −2+ 

|δ1II | = |h ∗ ∇ g0 LZ (J0 + φ(t)) + g0 ∗ A1LZ (J0 + φ(t)) |≤ (C + ′

> 1

) · r−4+ ‖Z‖Ck+1 ,α 

> 1

‖Y ‖Ck+1 ,α 

> −2+ 

|δ1III | ≤ C · r−4+ (‖Z‖2

> Ck+1 ,α
> 1

+ ′

> 1

)‖Y ‖Ck+1 ,α 

> −2+ 

.

(6.31) The terms δ2I, δ 2II and δ2III obey similar estimates. Consequently, 

|δΦY ∗g0 (Φ ∗ 

> Z

(J0 + φ(t))) | ≤ (C + ′

> 1

) · r−4+ (‖Y ‖Ck+1 ,α 

> −2+ 

+ ‖Z‖Ck+1 ,α 

> 1

).(6.32) Higher regularities can be estimated similarly, which shows that N does indeed map into the claimed image space and it is bounded. Similar arguments show that N is smooth, since W is finite-dimensional, and N is linear over φ.At (0 , 0, 0), the linearization of N restricted on the tangent of the first and third variables is: 

D N0 : Ck+1 ,α  

> −2+ 

(T X ) × W → Ck−1,α  

> −4+ 

(T ∗X) × Rm

(Y, Z ) 7 →

{

δ0LY J0 = 0Y, 

∫

〈LZ J0 − LY J0, v 1〉g0 dV g0 ,

· · · ,

∫

〈LZ J0 − LY J0, v m〉g0 dV g0

}

.

(6.33) Restricting the domain and image, consider DN0 mapping from Ck+1 ,α  

> −2+ 

(T X ) to 

Ck−1,α  

> −4+ 

(T ∗X). The adjoint of this restricted mapping, which we again denote by 

D N0, is: (D N0)∗ : Ck+1 ,α  

> −

(T ∗X) → Ck−1,α  

> −2−

(T X )

η 7 → (0η)#.

(6.34) The kernel of ( D N0)∗ consists of those η ∈ Ck+1 ,α  

> −

(T ∗X) such that ( 0η)# = 0, which implies that η# is the real part of a holomorphic vector field. From Proposition 3.4, 

η = 0. Since the cokernel of D N0 is trivial, D N0 is surjective on the restricted domain and range. It follows that the full mapping DN0 is surjective, since V is generated by LZ J0 for 

Z ∈ W. Clearly then, in a small neighborhood of (0 , 0, 0), D N is surjective. Since the mapping N is smooth, Condition (4.1) is satisfied, so the existence of diffeomorphism Φ then follows from Lemma 4.1. Finally, it is easy to see that there exists a constant 

C so that 

‖LZ J1‖Ck,α 

> −3

≤ C ′

> 1

,(6.35) so the estimate (6.20) follows from (6.10). 24 JIYUAN HAN AND JEFF A. VIACLOVSKY 

7. Stability of K¨ ahler metrics 

In this section, we want to generalize Kodaira-Spencer’s stability theory of K¨ ahler metrics to ALE surfaces to the family of complex structures found above [KS60]. Specifically, we want to find a smooth family of K¨ ahler forms on ( X, J t) for t small, where Jt for t ∈ B1 ⊂ H ess (X, Λ0,1 ⊗ Θ) is the family of complex structures con-structed in Section 4. In a slight abuse of notation, the notation Xt will stand for (X, J t). All the norms below in this section are based on the central metric g0.

Lemma 7.1. The integer-valued function dim( Hτ (Xt, Λp,q )) is upper semicontinuous at t = 0 , for any τ ∈ (−2, 0) .Proof. The Hodge Laplacian ∆ d = dd ∗ + d∗d is a Fredholm operator on Ck,α τ (−2 <τ < 0, k ≥ 2). The following is proved in [Bar86]: If P is a pseudo-differential operator such that ‖P − 12 ∆d‖op <  for some  sufficiently small, then ker( P ) ≤ ker(∆ d), where 

‖ · ‖ op is the norm of operators from Ck,α τ to Ck−2,α τ −2 , which is defined as: 

‖P ‖op = sup {‖ P (u)‖Ck−2,α τ −2

: ‖u‖Ck,α τ = 1 }.(7.1) We may apply this to the operator P = t = ¯∂t 

> ∗

¯∂t + ¯∂t ¯∂t

> ∗

, since we have ‖t − 

> 12

∆d‖op <  when t ∈ ∆d1 

> γ

is small enough (when t = 0, 0 = 12 ∆d by the K¨ ahler identities). Then dim( Hτ (Xt, Λp,q )) ≤ dim( Hτ (X0, Λp,q )) .(7.2) 



Let e·,· 

> t

denote the dimension of the space of t-harmonic forms with decay rate of τ . Note that by a similar argument as in Proposition 3.6, any such harmonic form must decay like O(r−3) as r → ∞ . So by [Joy00, Sections 8.4 and 8.9], and Proposition 3.7, we have 

b2,00 = b0,20 = b1,00 = b0,10 = 0 .(7.3) From semi-continuity, it follows that 

e2,0 

> t

= e0,2 

> t

= e1,0 

> t

= e0,1 

> t

= 0 .(7.4) The proof of the following theorem is inspired by [BR15]. 

Theorem 7.2. By choosing 1 small enough, for the family of deformation (X, J t),

t ∈ B1 , there exists a smooth family of K¨ ahler forms ωt on Xt, and 

‖ωt − ω0‖Ck,α δ

≤ C · ‖ t‖Ck,α 

> −3

≤ C · 1(7.5) 

for some constant C, and some k ≥ 3, δ ∈ (−2, −1) .Furthermore, letting G denote the group of holomorphic isometries of (X, g 0, J 0),the mapping 

ℵ : B1 → Λ2(T ∗X)

t 7 → ωt

(7.6) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 25 

can be chosen equivariantly with respect to the action of G. That is, ℵ(ι∗t) = ι∗ℵ(t),for all ι ∈ G.Proof. Let gt = 12 (g+g◦Jt) be the Hermitian metric on Xt, where g is the Riemannian metric of the central fiber and Jt is the complex structure of Xt. Let t = ¯∂t 

> ∗

¯∂t +¯∂t ¯∂t 

> ∗

be the ¯∂t−Laplacian defined with respect to gt. Let ω′ 

> t

= √−12 gt(Jt , ) be the corresponding (1 , 1)-form. We want to perturb ω′ 

> t

to acquire a K¨ ahler form ωt. We have ω′ 

> t

= ωht + φt, where ωht is the t-harmonic part of ω′

> t

, which is asymptotic to 

dz t ∧ d¯zt at the rate of −δ, with ‖φt‖Ck,α δ

≤ C‖tω′

> t

‖Ck−2,α δ−2

. We next show that this claimed decomposition is valid. Consider the following Fredholm operator 

t : Ck,α δ (Xt, Λ1,1) → Ck−2,α δ−2 (Xt, Λ1,1).(7.7) The kernel ker ∗ 

> t

⊂ Ck,α 

> −2−δ

(Xt, Λ1,1) is of finite dimension. For any σ ∈ ker ∗ 

> t

, σ

admits an expansion 

σ =

> 2

∑

> k=1

ak

r2 dz t ∧ d¯zt + O(r−3)(7.8) as r → ∞ , where ak are constants. Since 0 = 

∫

> X

〈σ, tσ〉gt dV gt = lim 

> R→∞

{ ∫

> B(R)

(〈 ¯∂σ, ¯∂σ 〉gt + 〈 ¯∂∗σ, ¯∂∗σ〉gt

)dV gt

+

∫

> S(R)

(〈σ, ¯∂r y ¯∂σ 〉gt + 〈 ¯∂∗σ, ¯∂r yσ〉gt

)dA gt

}

=

∫

> X

(〈 ¯∂σ, ¯∂σ 〉gt + 〈 ¯∂∗σ, ¯∂∗σ〉gt

)dV gt .

(7.9) This shows that ¯∂σ = 0, ¯∂∗σ = 0. Since also ¯∂t − ¯∂Euc = O(r−3), we have ¯∂Euc σ =

O(r−5). Then ak = 0 and σ = O(r−3). This implies that tω′ 

> t

∈ (ker ∗ 

> t

)⊥ ∩

Ck−2,α δ−2 (Xt, Λ1,1), which is the L2-complement of ker ∗ 

> t

in Ck−2,α δ−2 (Xt, Λ1,1). Then there exists a φt ∈ Ck,α δ (Xt, Λ1,1) such that tφt = tω′ 

> t

and ‖φt‖Ck,α δ

≤ C‖tω′

> t

‖Ck−2,α δ−2

.Then we can let ωht = ω′ 

> t

− φt which is t-harmonic. 

Proposition 7.3. If tωht = 0 , then ¯∂tωht = 0 .Proof. ¯∂ttωht = t ¯∂tωht = 0, then ¯∂tωht is t-harmonic, with decay rate of −(δ − 1). However, e2,1 

> t

= e0,1 

> t

= 0 by the upper semi-continuity and since the conjugate Hodge-star operator maps harmonic forms to harmonic forms. Then ¯∂tωht = 0. 

We want to find ωt such that dω t = 0; for this we need a lemma. 

Lemma 7.4. We have ∂tωht = ¯∂tat, where at ∈ Ck,α δ (Xt, Λ2,0), k ≥ 3. Furthermore, 

‖at‖Ck,α δ

≤ C‖∂tωht ‖Ck−1,α δ−1

≤ C′‖t‖Ck,α δ

(7.10) 

Proof. First note that ¯∂t∂tωht = −∂t ¯∂tωht = 0 .(7.11) 26 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Then 

∂tωht ∈ Ck−1,α δ−1 (Xt, Λ2,1) = Hδ−1(Xt, Λ2,1) ⊕ tCk+1 ,α δ+1 (Xt, Λ2,1).(7.12) (This decomposition follows since t is Fredholm on Ck,α δ+1 (Xt, Λ2,1).) Then 

∂tωht = ht + ( ¯∂t ¯∂∗ 

> t

+ ¯∂∗ 

> t

¯∂t)ft(7.13) with ft ∈ Ck+1 ,α δ+1 (Xt, Λ2,1), where ht is the harmonic part. Since ¯∂t∂tωHt = 0, it follows that t ¯∂tft = 0. From injectivity of t on Ck,α δ , we have ¯∂tft = 0. Then 

∂tωht = ht + ¯∂t ¯∂∗ 

> t

ft = ht + ¯∂tat,(7.14) where at = ¯∂∗ 

> t

ft ∈ Ck,α δ (Xt, Λ2,0). Since e2,1 

> t

= 0, then ht = 0, and ∂tωht = ¯∂tat.Since dim( Hδ+1 (Xt, Λ2,1)) = 0, 

t : Ck+1 ,α δ+1 (Xt, Λ2,1) → Ck−1,α δ−1 (Xt, Λ2,1)(7.15) is an isomorphism. Then ‖ft‖Ck+1 ,α δ+1 

≤ C‖∂tωht ‖Ck−1,α δ−1

implies that 

‖a‖Ck,α δ

≤ C‖∂tωht ‖Ck−1,α δ−1

≤ C′‖t‖Ck,α δ

,(7.16) 



Now we have at ∈ Ck,α δ (Xt, Λ2,0) and ¯∂t ¯at = 0. Let δ + 2 not be a indicial root of 

t, then 

t : Ck+2 ,α δ+2 (Xt, Λ0,2) → Ck,α δ (Xt, Λ0,2)(7.17) is Fredholm. Since dim( H−4−δ(Xt, Λ0,2)) = 0, it follows that t is surjective. We can therefore choose ft ∈ Ck+2 ,α δ+2 (Xt, Λ0,2) such that ¯ at = tft = ¯∂t ¯∂∗ 

> t

ft with 

‖ft‖Ck+2 ,α δ+2 

≤ C‖ ¯at‖Ck,α δ

≤ C′‖t‖Ck,α δ

.(7.18) Let ¯βt = ¯∂∗ 

> t

ft, and let ωt = ωht + ¯∂tβt. Then dω t = ∂tωht − ¯∂tat = 0. Choose 1 to be small enough, then ωt is a closed positive (1,1)-form. 

8. Deformations of scalar-flat K¨ ahler metrics 

Notice that the previous sections did not use the scalar-flat assumption; this section is where we start using it. 8.1. The linearized operator. In previous sections, we have shown that there ex-ists a family of decaying deformation of complex structure with dimension equal to dim( Hess (X, Λ0,1 ⊗ Θ)), and there exists a smooth family of K¨ ahler forms along the deformation. In this section, we will show that near an initial scalar-flat K¨ ahler ALE metric ω0, there is a smooth family of scalar-flat K¨ ahler ALE metrics under these deformations. The arguments in this section are inspired by [LS93, LS94]. DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 27 

Denote S(ω0 + √−1∂ ¯∂f ) as the scalar curvature of X with metric ω0 + √−1∂ ¯∂f .We now consider S as mapping between weighted H¨ older spaces, with some 0 <   1

S : Ck,α  (X) → Ck−4,α −4 (X)

f 7 → S(ω0 + √−1∂ ¯∂f ).

(8.1) Its linearization and adjoint are maps between: 

L : Ck,α  (X) → Ck−4,α −4 (X)(8.2) 

L∗ : Ck,α  

> −

(X) → Ck−4,α  

> −4−

(X).(8.3) By direct calculation, 

L(f ) := D S (ω0 + √−1∂ ¯∂f ) = −(∆ 2f + Ri, ¯j ∇i∇¯j f ).(8.4) Define ¯∂#f = gi, ¯j 

> 0

¯∂j f . Also by direct calculation, ( ¯∂ ¯∂#)∗( ¯∂ ¯∂#)f = ∆ 2f + Ri, ¯j ∇i∇¯j f + ∇kS∇kf. (8.5) Clearly then, when ω0 is scalar-flat, L(f ) = −( ¯∂ ¯∂#)∗( ¯∂ ¯∂#)( f ), see [LS94]. The following lemma shows that the linearized mapping is surjective. 

Lemma 8.1. For 0 <   1, k ≥ 4, L is surjective. Proof. Obviously, L is an elliptic operator, and the indicial roots of L are the integers. Consequently, by standard weighted space theory, L is Fredholm since δ is non-integral [LM85]. Let f ∈ ker( L∗), then f = O(r−) and ( ¯∂ ¯∂#)∗( ¯∂ ¯∂#)f = 0. Since 

f ( ¯∂ ¯∂#)∗( ¯∂ ¯∂#)f = o(r−4),(8.6) integrating by parts, It follows that ¯∂ ¯∂#f = 0, so ¯∂#f is a holomorphic vector field on 

X which has a decay rate of −( − 1), and Proposition 3.4 then implies that ¯∂#f = 0. Since f is a real-valued function, f must be constant; but since f = O(r−), we have 

f ≡ 0. We have shown that ker( L∗) = {0}, so L is surjective. 

Proposition 8.2. For 0 <   1 and k ≥ 4, ker( L) is spanned by the constants. Proof. The operator L admits an expansion near infinity of the form L = ∆ 2 

> Euc

+ Q,where Q represents lower order terms. Let 

N (L, τ ) = Index( L : Ck,α τ (X) → Ck−4,α τ −4 (X)) .(8.7) Then, by the relative index theorem of Lockhart-McOwen, 

N (L,  ) − N (L, −) = N (∆ 2

> Euc

,  ) − N (∆ 2

> Euc

, −) = 2 .(8.8) see [LM85]. The above argument shows that Ker (L) ∩ Ck,α  

> −

(X) = {0}, which implies that ker( L) ∩ Ck,α  (X) = {constants }.(8.9) 

28 JIYUAN HAN AND JEFF A. VIACLOVSKY 

8.2. Construction of F. Now we start the construction of the class F. First, we show a weighted version ∂ ¯∂−lemma on ALE surfaces. This is similar to [Joy00, Theorem 8.4.4], but with slightly different assumptions. 

Lemma 8.3. Consider the K¨ ahler ALE surface (X, J 0, g 0). Let ζ ∈ Ck,α δ (X, Λ1,1) be a real (1 , 1) form, for some k ≥ 2 and δ ∈ (−2, −1) , be a real form, satisfying dζ = 0 .Then there exists θ ∈ Ck+2 ,α δ+2 (X) such that ζ = ζh + √−1∂ ¯∂θ , and ‖θ‖Ck+2 ,α δ+2 

≤

C · ‖ ζ − ζh‖Ck,α δ

, where ζh ∈ H δ(X, Λ1,1).Proof. Since ζ is closed, can be decomposed as ζ = ζh + ∂η + ¯∂ξ , where ζh ∈Hδ(X, Λ1,1), η ∈ Ck+1 ,α δ+1 (X, Λ0,1), and ξ ∈ Ck+1 ,α δ+1 (X, Λ1,0). Since ζ is a real form, we can assume that η = ξ. Consider the operator  and its Fredholm adjoint ∗:

 : Ck+3 ,α δ+3 (X, Λ0,1) → Ck+1 ,α δ+1 (X, Λ0,1)

∗ : Ck+3 ,α  

> −3−δ

(X, Λ0,1) → Ck+1 ,α  

> −δ−5

(X, Λ0,1)(8.10) This implies that  has finite-dimensional cokernel. Then we have 

η = ηh + γ = ηh + ¯∂ ¯∂∗γ + ¯∂∗ ¯∂γ, (8.11) where γ ∈ Ck+3 ,α δ+3 (X, Λ0,1) and ηh is the -harmonic part. Without loss of generality, assume ηh = 0. Since g0 is K¨ ahler, ∂ ¯∂∗( ¯∂γ ) = − ¯∂∂ ∗( ¯∂γ ) = 0, so we can assume that ¯∂γ = 0. Then ζ = ζh + √−1∂ ¯∂θ ′, where θ′ = 2 Im ( ¯∂∗γ) ∈ Ck+2 ,α δ+2 (X). Now consider the Fredholm operator 

F = √−1∂ ¯∂ : Ck+2 ,α δ+2 (X) → Ck,α δ (X, Λ1,1)(8.12) Let (ker F ∗)⊥ be the L2-complement of ker F ∗ in Ck,α δ (X, Λ1,1). The argument above shows that ker F ∗ = ker ∗. Then ζ − ζh ∈ (ker F ∗)⊥. By the same argument as in the proof of Theorem 7.2, we can show that there exists a θ ∈ Ck+2 ,α δ+2 (X), such that 

√−1∂ ¯∂θ = ζ − ζh, and ‖θ‖Ck+2 ,α δ+2 

≤ C‖ζ − ζh‖Ck,α δ

for some constant C. 

Theorem 8.4. Let (X, J 0, g 0) be a scalar-flat K¨ ahler ALE metric on a surface X.Then there is family F of scalar-flat K¨ ahler metrics near g0, parametrized by B, that is, there is a differentiable mapping 

F : B1 × B2 → M (X),(8.13) 

into the space of smooth Riemannian metrics M(X) with F = F (B1 × B2). Fur-thermore, letting G denote the group of holomorphic isometries of (X, J 0, g 0), the mapping F is equivariant with respect to the action of G. That is, for ι ∈ G, and 

(t, ρ ) ∈ B1 × B2, we have F (ι∗t, ι ∗ρ) = ι∗F (t, ρ ).Proof. Recall the parameter space B = B1 × B2, where 

B1 = B1 (0) ⊂ H ess (X0, End a(T X 0)); B2 = B2 (0) ⊂ H δ(X0, Λ1,1) ' H1,1(X0).

(8.14) DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 29 

Let t denote the parameter of B1. By Section 7, dim( Hδ(Xt, Λp,q )) (using the metric determined by ωt) is upper semicontinuous, and dim( Hδ(X0, Λ1,1)) = dim( H1,1(X0)) dim( Hδ(X0, Λ2,0)) = dim( Hδ(X0, Λ0,2)) = 0 .

(8.15) So for 1 sufficiently small, dim( Hδ(Xt, Λ2,0)) = dim( Hδ(Xt, Λ0,2)) = 0 ,(8.16) and also dim( Hδ(Xt, Λ2,0)) ≥ dim( H2,0(Xt)) dim( Hδ(Xt, Λ0,2)) ≥ dim( H0,2(Xt)) .

(8.17) This implies that dim( H2(Xt)) = dim( H1,1(Xt)) which is a topological invariant. Then dim( H2(Xt)) ≤ dim( Hδ(Xt, Λ1,1)) ≤ dim( Hδ(X0, Λ1,1)) = = dim( H2(X0)) = dim( H2(Xt)) .

(8.18) This implies that dim( Hδ(Xt, Λ1,1)) = dim( H2(Xt)) is constant, so choose a smooth family of isomorphisms ψt which map Hδ(X0, Λ1,1) to Hδ(Xt, Λ1,1) for t sufficiently small. Note that G acts on Hδ(X0, Λ1,1), and from Theorem 7.2, G also acts on 

Hδ(Xt, Λ1,1). Clearly we can choose ψt to be equivariant with respect to these actions. It has been shown in Section 7 that there is a smooth family of K¨ ahler forms ωt.Let ρ ∈ B2, define 

ω(t, ρ ) = ωt + ψt(ρ)(8.19) Now consider the mapping 

S : B1 × B2 × Ck,α  (X) → Ck−4,α −4 (X),(8.20) defined by 

S : ( t, ρ, f ) 7 → S(ω(t, ρ ) + √−1∂t ¯∂tf ).(8.21) We endow the domain with the product norm, where B1 and B2 have the L2-norm. By direct calculation, the linearization of S at 0 is: 

DS = (∗, −Ric h, L)

(8.22) where Ric h is the harmonic part of Ricci form. Since L is surjective as shown in Lemma 8.3, DS is surjective by the lemma above. Next, we recall the expansion of the curvature tensor 

Rm (g0 + h) = Rm (g0) + ( g0 + h)−1 ∗ ∇ 2h + ( g0 + h)−2 ∗ ∇ h ∗ ∇ h, (8.23) where ∗ denotes a various tensor contractions, and h is a symmetric tensor such that 

g0 + h is a Riemannian metric [GV16, Formula 3.40]. In our case, h can be written as 

h(, ) = ( ω(t, ρ ) + √−1∂t ¯∂tf )( −Jt, ) − ω(0 , 0)( −J0, ).(8.24) 30 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Next, by (7.5), we have the estimates 

|h| ≤ C(|t| + |ρ| + |∇ 2f |) ≤ C(rδ‖t‖Ck,α δ

+ rδ‖ρ‖Ck,α δ

+ r−2+ ‖f ‖Ck,α  )

|∇ h| ≤ C(|∇ t| + |∇ ρ| + |∇ 3f |) ≤ C(r−1+ δ‖t‖Ck,α δ

+ r−1+ δ‖ρ‖Ck,α δ

+ r−3+ ‖f ‖Ck,α  )

|∇ 2h| ≤ C(|∇ 2t| + |∇ 2ρ| + |∇ 4f |) ≤ C(r−2+ δ‖t‖Ck,α δ

+ r−2+ δ‖ρ‖Ck,α δ

+ r−4+ ‖f ‖Ck,α  ).

(8.25) Then by (8.23), we have 

S(g0 + h) − DS · h = C0(g0, h ) ∗ Rm (g0) ∗ h ∗ h

+ C1(g0, h ) ∗ h ∗ ∇ 2h + C2(g0, h ) ∗ ∇ h ∗ ∇ h, 

(8.26) where C0(g0, h ), C 1(g0, h ), and C2(g0, h ) are bounded functions, when h is sufficiently small. Without loss of generality, we can assume that −2 +  < δ . Then 

|S(g0 + h) − DS · h| ≤ C{r−2|h|2 + |h| · |∇ 2h| + |∇ h| · |∇ h|} ≤ C · r−2+2 δ · (‖t‖Ck,α δ

+ ‖ρ‖Ck,α δ

+ ‖f ‖Ck,α  )2(8.27) which implies that 

‖S(g0 + h) − DS · h‖Ck,α 

> −4+ 

≤ C(‖t‖Ck,α δ

+ ‖ρ‖Ck,α δ

+ ‖f ‖Ck,α  )2.(8.28) Furthermore, 

‖S(g0 + h) − S(g0 + h′) − DS · (h − h′)‖Ck,α 

> −4+ 

≤

C · (‖t − t′‖Ck,α δ

+ ‖ρ − ρ′‖Ck,α δ

+ ‖f − f ′‖Ck,α 

)

· (‖t‖Ck,α δ

+ ‖ρ‖Ck,α δ

+ ‖f ‖Ck,α 

> 1

+ ‖t′‖Ck,α δ

+ ‖ρ′‖Ck,α δ

+ ‖f ′‖Ck,α 

).

(8.29) Since B1 and B2 are finite-dimensional, we can replace the corresponding norms by the L2-norm. This shows that S satisfies the condition (4.1). Then by Lemma 4.1, the zero set of S is in one-to-one correspondence with the kernel of S′(0). Since any solution of the nonlinear equation can be written as a kernel element plus a unique element in the image of a bounded right inverse for the linearized operator, the zero set of S can also be written as a graph over B1 ×B2. That is, for any ( t, ρ ) ∈ B1 ×B2,there exists a unique f (t, ρ ), up to constants, of 

S(t, ρ, f (t, ρ )) = 0 ,(8.30) so a family of scalar-flat K¨ ahler metrics over B can be constructed as 

F : ( t, ρ ) 7 → g(t, ρ ) = 

(

ω(t, ρ ) + √−1∂t ¯∂tf (t, ρ )

)

(−Jt·, ·),(8.31) where g(0 , 0) = g0. It is a straightforward consequence of the implicit function theo-rem that the mapping F is differentiable. Then the image of F gives us the family of scalar-flat K¨ ahler metrics F, and the construction is clearly equivariant with respect to the action of G.DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 31 

To finish the proof, we show that metrics in F are smooth. By the result of [TV05a], any K¨ ahler constant scalar curvature metric satisfies an equation of the form ∆Ric = Rm ∗ Ric, (8.32) where the right hand side denotes quadratic curvature contractions involving the full curvature tensor Rm and the Ricci tensor. By a Moser iteration method and regularity bootstrap argument in harmonic coordinates, it follows that g is smooth, see [TV05b, Theorem 6.4]. 

9. Versality and uniqueness of the moduli space 

In this section, all norms are defined based on the initial K¨ ahler metric g0. We let (g1, J 1) be any scalar-flat K¨ ahler metric satisfying ‖g1 − g0‖Ck,α δ

<  3, (for some k ≥ 4, 

δ ∈ (−2, −1), and 3 will be determined later). We begin with the following lemma. 

Lemma 9.1. For 3 sufficiently small, if ‖g1 − g0‖Ck,α δ

<  3, then there exists a diffeomorphism Φ0 : X → X and constants C1, C 2 so that 

‖Φ∗

> 0

g1 − g0‖Ck,α δ

< C 13(9.1) 

‖Φ∗

> 0

J1 − J0‖Ck,α δ

< C 23.(9.2) 

Proof. Let ∇0 denote the covariant derivative of g0, and Γ 0, Γ1 denote the Christoffel symbols of g0, g 1, respectively. Then ‖Γ1 −Γ0‖Ck−1,α δ−1

< C 3, so in particular |Γ1 −Γ0| < 

> C 3
> (1+ r)−δ+1

as r → ∞ .Since ( gi, J i) is K¨ ahler, ∇iJi = 0 for i = 0 , 1. We now estimate |J1 − J0|(p) along any geodesic ray γ starting at p0. From [HL15, Lemma 1.1], both J1 and J0 have a finite limit along γ as t → ∞ , and furthermore 

Ji = ( Ji)0 + O(r−2),(9.3) where ( Ji)0 is a constant complex structure on R4 for i = 0 , 1. We are assuming that (J0)0 = JEuc . Clearly, there exists a diffeomorphism Φ 0 : X → X so that Φ∗

> 0

J1 = JEuc + O(r−2),(9.4) as r → ∞ such that (9.1) is satisfied. This can be done, for example, by connecting a rotation defined on the complement of a large ball X \ B(p0, 2R) to the identity transformation on B(p0, R ) by smooth path of rotations of each sphere on the annulus 

A(R, 2R). We then have 

|Φ∗

> 0

J1 − J0|(p) = |Φ∗

> 0

J1 − J0|(p) − lim  

> t→∞

|Φ∗

> 0

J1 − J0|(γ(t)) 

≤

∫ ∞

> s=r

|∇ 0(Φ ∗

> 0

J1 − J0)( γ(s)) |ds 

≤

∫ ∞

> s=r

|∇ 0Φ∗

> 0

J1(γ(s)) |ds <

∫ ∞

> s=r

C · 3

(1 + s)−δ+1 ds ≤ C′ · 3

(1 + r)−δ .

(9.5) 32 JIYUAN HAN AND JEFF A. VIACLOVSKY 

Since this estimate is true along any ray, it follows that ‖Φ∗

> 0

J1 − J0‖C0 

> δ

< C ′3. We can estimate the higher regularities in the same way, and (9.2) follows. 

We next prove the “versality” of our family F. That is, for g1 as above, there exists a diffeomorphism Φ such that Φ ∗g1 is in the class F.

Theorem 9.2. Let −2 < δ < −1 be fixed. There exists an 3 > 0 such that for any scalar-flat K¨ ahler metric (g1, J 1) satisfying ‖g1 − g0‖Ck,α δ

≤ 3, there exists a diffeomorphism Φ : X → X of the form Φ0 ◦ ΦY1 ◦ ΦZ ◦ ΦY2 where Φ0 is as in Lemma 9.1, Y1, Y 2 ∈ Ck+1 ,α δ+1 (T X ), and Z ∈ W, such that Φ∗g1 ∈ F. Furthermore, there exists a constant C so that 

‖Φ∗g1 − g0‖Ck,α δ

≤ C 3.(9.6) 

Proof. Let Φ 0 denote the diffeomorphism from Lemma 9.1. Then Φ ∗

> 0

J1 satisfies the assumptions of Theorem 6.3, so there exists a diffeomorphism ˜Φ satisyfing the prop-erties stated in that theorem. In particular, ˜Φ is of the form ˜Φ = Φ Y1 ◦ ΦZ ◦ ΦY2 ,where Y1, Y 2 ∈ Ck+1 ,α δ+1 (T X ), and Z ∈ W. The estimate (9.6) for Φ 0 ◦ ˜Φ is then proved as follows. For Φ Y1 , we estimate 

‖Φ∗ 

> Y1

Φ∗

> 0

g1 − g0‖Ck,α δ

≤ ‖ Φ∗ 

> Y1

Φ∗

> 0

g1 − Φ∗

> 0

g1‖Ck,α δ

+ ‖Φ∗

> 0

g1 − g0‖Ck,α δ

≤ C 3.(9.7) This estimate holds since Φ ∗

> 0

g1 is also a scalar-flat K¨ ahler metric which is smooth by the last observation in the proof of Theorem 8.4, so when 3 is sufficiently small, Lemma 5.1 holds for g1. The same argument applies to Φ Y2 . The estimate (9.6) then follows from (9.7), (6.9) and Lemma 9.1. Let ω1 denote the K¨ ahler form of Φ ∗g1. It was shown in Section 8 that dim( H1,1(Xt)) is locally constant, which implies H1,1(X0) ' H1,1(Xt) for any t ∈ B1. Then there exists a ρ ∈ H δ(X0, Λ1,1) such that [ ω(φess , ρ )] = [ ω1] ∈ H1,1(Xt), where ω(φess , ρ ) is defined in (8.19). Let g′ = F (φess , ρ ), and let ω′ denote the corresponding K¨ ahler form. Then by Lemma 8.3, ω′ −ω1 = √−1 ¯∂t ¯∂∗ 

> t

f for some potential function f ∈ Ck+2 ,α δ+2 (X), and ‖f ‖Ck+2 ,α δ+2 

≤ C‖ω′ − ω1‖Ck,α δ

.As shown in the proof of Theorem 8.4, in a neighborhood of g0, a scalar-flat K¨ ahler metric is uniquely determined by the K¨ ahler class and complex structure. This implies that g′ = g1. 

This completes the proof of Theorem 1.4. Next, we will complete the proof of Theorem 1.7. From Theorem 8.4, the mapping F is G-equivariant. That is, for 

ι ∈ G, and ( t, ρ ) ∈ B1 × B2, we have F (ι∗t, ι ∗ρ) = ι∗F (t, ρ ). This clearly implies that two elements in the same orbit of G are isometric, which proves the first statement in Theorem 1.7. For the second statement in Theorem 1.7, we need the following lemma, which says that in the non-hyperk¨ ahler case, the dimension of F is the same as the dimension of the parameter space. 

Lemma 9.3. Let (X, g, J ) be as above. If g is not hyperk¨ ahler then F is injective, so 

dim( F) = d = dim( B1 × B2).DEFORMATION THEORY OF SCALAR-FLAT K ¨AHLER ALE SURFACES 33 

Proof. If F (φ1, ρ 1) = F (φ2, ρ 2) = ˜ g, then the metric ˜ g is K¨ ahler with respect to the two complex structures J1 and J2, corresponding to φ1 and φ2, respectively. We have Ji ∈ End (T X ) ( i = 1 , 2) such that J2 

> i

= −1. Locally, Ji can be considered as an purely imaginary Hamiltonian number. Define 

J3 = J1J2 − J2J1

‖J1J2 − J2J1‖,(9.8) where for p ∈ X,

‖Ji(p)‖ = sup 

> 06=v∈TpX

{‖Ji(v)‖h

‖v‖h

}

.(9.9) Then J3 ∈ End (T X ). We claim that J3 is well-defined, J23 = −1, J1, J 2, J 3 are linearly independent. Clearly, (J1J2 − J2J1)( J1J2 − J2J1) = −2 + ( J1J2J1J2 − J2J1J2J1).(9.10) Since J1J2J1J2 − J2J1J2J1 is real and has norm which is < 2, we have that (J1J2 − J2J1)( J1J2 − J2J1) 6 = 0 ,(9.11) so J3 is well-defined, and J3 · J3 = −1. If we write J1, J 2 locally as Hamiltonian numbers a1I + b1J + c1K, a2I + b2J + c2K (where ai, b i, c i ∈ R, I2 = J2 = K2 = −1), then 

J1J2 − J2J1 = ( b0c1 − b1c0)I + ( c0a1 − c1a0)J + ( a0c1 − a1c0)K, (9.12) which is linearly independent with J1 and J2. Then J1, J 2, J 3 are linearly independent. As a result, {J1, J 2, J 3} gives a hyperk¨ ahler structure. Then we have proved that, if Γ 6 ⊂ SU(2), then J1 = J2, then by the proof of Theorem 8.4, F is injective. 

The next proposition immediately implies the second part of Theorem 1.7. 

Proposition 9.4. For any two element g1, g 2 ∈ F associated to divergence-free com-plex structures J1, J 2, if there exists a small diffeomorphism ΦY which is induced by the exponential map of a vector field Y ∈ Ck+1 ,α δ+1 (T X ), such that g1 = Φ ∗ 

> Y

g2, then 

g1, g 2 are the same. Proof. First, assume X is non-hyperk¨ ahler. Since Φ ∗ 

> Y

g2 = g1, by Lemma 9.3, J1 =Φ∗ 

> Y

J2. However by Lemma 5.2, there is a unique small diffeomorphism that gauges 

J2 to be divergence-free. Then Φ Y = Id , g1 = g2.When X is hyperk¨ ahler, then by rotating the hyperk¨ ahler sphere, there exists a J′

> 1

such that J′ 

> 1

is compatible with g1 and ( X, Φ∗ 

> Y

J2) is biholomorphic to ( X, J ′

> 1

). Then by the same argument above, g1 = g2. 

Since F is of finite dimension, and G is a compact group action on F, the dimen-sion m of M = F/G is well-defined. In the non-hyperk¨ ahler case, by Lemma 9.3, 