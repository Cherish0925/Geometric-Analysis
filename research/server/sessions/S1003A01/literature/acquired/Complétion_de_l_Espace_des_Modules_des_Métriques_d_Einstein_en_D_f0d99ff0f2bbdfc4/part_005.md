---
retention_scope: session
part: 5
total_parts: 7
---

[Part 5/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

˜δgD (ψ∗gE ) = 0 .

En particulier, on a 

ΦgD (ψ∗gE ) = 0 .

# 3 Résolution de l’équation d’Einstein modulo obstructions 

Nous montrons maintenant qu’il est toujours possible de produire des mé-triques d’Einstein modulo certaines obstructions (le conoyau de la linéarisation de l’opérateur d’Einstein) dans nos espaces à poids. Le résultat principal est le théorème 4.51 qui nous permet de perturber tout recollement naïf gD en une mé-trique d’Einstein et nous assure en particulier d’après les résultats du chapitre 3 précédent que toute métrique d’Einstein proche d’un orbifold d’Einstein au sens de Gromov-Hausdorff est une petite perturbation dans nos normes à poids d’une désingularisation naïve gD.3. Résolution de l’équation d’Einstein modulo obstructions 159 Nous avons vu dans le corollaire 4.40 qu’à un difféomorphisme-près, toute métrique d’Einstein g proche de ( Mo, g o) au sens de Gromov-Hausdorff est une solution de ΦgD (g) := E(g) + δ∗ 

> g

˜δgD g = 0 .

Afin d’étudier cette équation, nous étudions tout d’abord naturellement sa linéarisation sur les déformations préservant infinitésimalement le volume, c’est-à-dire que les 2-tenseurs h satisfaisant ∫ 

> M

tr ghdvg = 0. Grâce au lemme 1.8, cela donne la formule suivante pour la dérivée en gD,¯PgD (h) := dgD ΦgD (h) = 12

> (

∇∗ 

> gD

∇gD h − 2˚RgD (h)

− 2δ∗ 

> gD

δgD h + 2 δ∗ 

> gD

˜δgD h − (δgD δgD h)gD

+ (∆ gD tr gD h)gD − ∇ 2 

> gD

tr gD h

+ Ric gD ◦h + h ◦ Ric gD − RgD h + 〈Ric gD , h 〉gD gD

+ 12R( g)h − 12 Vol( g)

> ∫
> M
> 〈

Ric( gD) − R( gD)2 , h 

> 〉
> gD

dvgD

> )

,

(4.38) en dimension 4. Si gD était une métrique d’Einstein et h est un 2-tenseur sans trace et à divergence nulle, l’opérateur ¯PgD se réduirait à 

PgD := 12∇∗ 

> gD

∇gD − ˚RgD ,

qui est bien plus simple à étudier. Comme gD est presque d’Einstein, nous étudie-rons principalement l’opérateur PgD et nous nous y ramènerons par approximation quand nous chercherons des informations particulières sur ¯PgD .

3.1 Noyau et conoyau de la linéarisation sur les espaces modèles 

Poids critiques pour Pe = 12 ∇∗

> e

∇e sur (R4/Γ, g e) et contraintes de jauge. 

Comme décrit dans la preuve de la proposition 4.19, les éléments du noyau de 

Pe sur R4/Γ sont des sommes de 2-tenseurs homogènes dont les coefficients dans une base orthonormée de R4 sont homogènes d’ordre k ou −2 − k pour k ∈ N.Cependant, certains de ces tenseurs ne pourront pas apparaître dans nos dévelop-pements car ils ne sont pas en jauge divergence ou à trace nulle d’après le lemme 2.50. Il n’y a donc pas de poids critique autre que 0 entre −4 et 2. 160 Chapitre 4. Désingularisation de métriques d’Einstein 

Noyau de l’opérateur P . Décrivons maintenant le noyau L2 de P sur nos espaces, cela nous servira aussi dans les parties suivantes. 

Lemme 4.41 (Noyau L2 et décroissant à l’infini de l’opérateur d’Einstein) . Soit 

(N, g b) un orbifold Ricci-plat ALE, et définissons Pb := 12 ∇∗ 

> b

∇b − ˚Rb, et O(gb), le noyau L2 de Pb. Alors, pour tout 0 < β < 1, le noyau de Pb sur C2,α β, ∗ coïncide avec 

O(gb).Les éléments O(gb) décroissent au moins en r−4 

> b

à l’infini, et pour tout ob ∈

O(gb), on a le développement suivant dans des coordonnées à l’infini, 

ob = O4 + O(r−5 

> b

),

avec O4 un 2-tenseur harmonique homogène décroissant en r−4 

> b

.Soit aussi (Mo, g o) un orbifold d’Einstein compact. Le noyau L2 de Po, noté 

O(go), coïncide aussi avec le noyau de Po sur C2,α β, ∗ pour tout 0 < β < 1.Démonstration. Prouvons le résultat pour un orbifold ALE, ( N, g b). Remarquons que pour la métrique euclidienne ge, l’opérateur Pe satisfait une estimations el-liptique sur les anneaux compacts : il existe C > 0 tel que pour tout 2-tenseur symétrique lisse h, on ait 

‖h‖W 2,2(Ae(1 ,2)) 6 C(

‖h‖L2(Ae(1 /2,4)) + ‖Peh‖L2(Ae(1 /2,4)) 

)

.

Maintenant sur ( N, g b), pour ρ assez grand, gb 

> ρ2

sur l’anneau de rayons ((1 /2) ρ, 4ρ)est proche de ge sur l’anneau de rayons (1 /2, 4), cela implique donc que comme 

P gbρ2 est proche de Pe := 12 ∇∗

> e

∇e, et l’on a donc 

‖h‖W 2,2(A(ρ, 2ρ), gbρ2 ) 6 2C(

‖h‖L2(A((1 /2) ρ, 4ρ), gbρ2 ) + ‖P gbρ2 h‖L2(A((1 /2) ρ, 4ρ), gbρ2 )

)

,

puis par régularité elliptique entre espaces de Sobolev 

‖h‖W 4,2(A(ρ, 2ρ), gbρ2 ) 6 2C(

‖h‖L2(A((1 /2) ρ, 4ρ), gbρ2 ) + ‖P gbρ2 h‖W 2,2(A((1 /2) ρ, 4ρ), gbρ2 )

)

,

et comme W 4,2(A((1 /2) ρ, 4ρ), gb 

> ρ2

) s’injecte continûment dans C0, nous avons 

|h| gbρ2 (x) 6 C‖h‖W 4,2(A(ρ, 2ρ), gbρ2 ) 6 2C2(

‖h‖L2(A((1 /2) ρ, 4ρ), gbρ2 )+‖P gbρ2 h‖W 2,2(A((1 /2) ρ, 4ρ), gbρ2 )

)

pour x sur l’image de la sphère de rayon 3 ρ/ 2. Or, la norme L2 de 2-tenseur est 3. Résolution de l’équation d’Einstein modulo obstructions 161 invariante par changement d’échelle en dimension 4, et donc, 

|h|gb (x) = 1

ρ2 |h| gbρ2 (x) 6 2C2

ρ2

> (

‖h‖L2(( A((1 /2) ρ, 4ρ),g b) + ‖P gbρ2 h‖W 2,2(( A((1 /2) ρ, 4ρ), gbρ2 )

> )

.

(4.39) Dans le cas de o ∈ O(gb), comme Pbo = 0, et o ∈ L2, et donc ‖o‖L2(( A((1 /2) ρ, 4ρ),g b) →

0 quand ρ → +∞, on déduit de (4.39) que r2 

> b

o → 0. Un tel 2-tenseur h est en fait nécessairement à divergence et trace nulle. En effet, nous avons 

δgb Pgb = 12∇∗ 

> gb

∇gb δgb ,

et tr gb Pgb = 12∇∗ 

> gb

∇gb tr gb .

Ainsi, si Pgb h = 0 et h = O(r−δb ) pour un δ > 0, alors δgb h = 0, et tr gb h = 0 par le principe du maximum. On en déduit du lemme 2.50 que h décroît au moins en 

ρ−4 et que son terme principal est un 2-tenseur harmonique. De la même manière au voisinage d’une singularité d’un orbifold ( Mo, g o) ou d’un orbifold Ricci-plat ALE ( N, g b), comme il n’y a pas de 2-tenseur harmonique à croissance linéaire du fait de l’action du groupe non-trivial, on obtient qu’un élément du noyau L2 a un développement 

o = O0 + O2 + O(r3 

> b

),

où O0 et O2 sont des 2-tenseurs homogènes harmoniques en r0 

> o

et r2 

> o

respectivement. 

Estimations sur les inverses. Comme nous l’avons déjà montré pour l’opéra-teur δδ ∗ dans le lemme 4.32, les opérateurs Pgo et Pgbj sont injectifs sur l’orthogonal de leurs noyaux respectifs. 

Lemme 4.42. Soient (N, g b) un orbifold Ricci-plat ALE et (Mo, g o) un orbifold d’Einstein, et 0 < β < 1.Alors, les opérateurs 

Pb : O(gb)⊥ ∩ C2,α β, ∗ (gb) → r−2 

> b

Cαβ (gb),

et 

Po : O(go)⊥ ∩ C2,α β, ∗ (go) → r−2 

> o

Cαβ (go)

sont injectifs et il existe Co > 0 et Cb > 0, tels que l’on ait pour tous 2-tenseurs 162 Chapitre 4. Désingularisation de métriques d’Einstein 

hb ⊥ O(gb) sur N et ho ⊥ O(go) sur Mo,

C−1 

> b

‖Pbhb‖r−2  

> bCαβ(gb)

‖hb‖C2,α β, ∗ (gb) 6 Cb‖Pbhb‖r−2  

> bCαβ(gb)

, (4.40) 

et 

C−1 

> o

‖Poho‖r−2   

> oCαβ(go)

6 ‖ho‖C2,α β, ∗ (go) 6 Co‖Poho‖r−2  

> oCαβ(go)

. (4.41) 

De plus, leurs conoyaux respectifs sont O(gb) et O(go).Démonstration. Les opérateurs elliptiques et bornées entre espaces à poids 

Po : C2,α  

> −β

(go) → r−2 

> o

Cα 

> −β

(go),

et 

Pb : r−βb C2,α  

> 0

(gb) → r−2−βb Cα 

> 0

(gb)sont Fredholm pour 0 < β < 1 car on évite ainsi les poids critiques possibles proches de zéro : −2 et 1. Étudions leurs noyaux et conoyaux. Intéressons nous tout d’abord au cas d’un orbifold d’Einstein ( Mo, g o) et re-marquons que C2,α  

> −β

(go) ⊂ L2(go), et O(go) ⊂ C2,α β, ∗ (go) ⊂ C2,α  

> −β

(go) donc le noyau de 

Po : C2,α  

> −β

(go) → r−2 

> o

Cα 

> −β

(go) est réduit à O(go). Comme Po est auto adjoint et que l’on est strictement entre deux poids critiques, son conoyau est le noyau de Po sur 

r−2 

> o

Cαβ (go) ⊂ L2(go) qui est lui aussi réduit à O(go). De même, le conoyau de Pb : r−βb C2,α  

> 0

(gb) → r−2−βb Cα 

> 0

(gb) est le noyau de Pb

sur r−2+ βb Cα 

> 0

(gb) qui est réduit à O(gb). Pour en déduire les noyaux des opérateurs 

Po : C2,α β, ∗ (go) → r−2 

> o

Cαβ (go),

et 

Pb : C2,α β, ∗ (gb) → r−2 

> b

Cαβ (gb),

il suffit alors de remarquer que comme le seul poids critique pour P entre −β et 

β est 0, le noyau de Po : C2,α  

> −β

(go) → r−2 

> o

Cα 

> −β

(go) appartient à C2,α β, ∗ (go) et celui de 

Pb : r−βb C2,α  

> 0

(gb) → r−2−βb Cα 

> 0

(gb) à C2,α β, ∗ (gb). Pour les conoyaux, comme dans la fin de la preuve de la proposition 4.31, on utilise le fait que 

Po

(

C2,α β, ∗ (go))

= Po

(

C2,α  

> −β

(go))

∩ r−2 

> o

Cαβ (go),

et 

Pb

(

C2,α β, ∗ (gb))

= Pb

(

r−βb C2,α  

> 0

(gbj ))

∩ r−2 

> b

Cαβ (gb).3. Résolution de l’équation d’Einstein modulo obstructions 163 

Approximation des noyaux et conoyaux sur une désingularisation naïve. 

Nous souhaitons résoudre l’équation E(g) = 0 pour une métrique g proche de gD

modulo le noyau et le conoyau de la linéarisation de l’opérateur d’Einstein. Nous utiliserons plutôt des noyaux et conoyaux approchés composés des déformations infinitésimales d’Einstein de chaque espace modèle tronquées sur l’arbre de singu-larités. Soit oo ∈ O(go) et et oj ∈ O(gbj ), et oo = oo, ∗ + ∑ 

> k

χBo(pk ,ε )oo,k et oj =

oj, ∗ + ∑ 

> k

χBj (pk ,ε )oj,k leurs décompositions respectives en un 2-tenseur de C2,α β et des 2-tenseurs constants approchés au voisinages des points singuliers. On définit alors sur M les 2-tenseurs suivants ˜oo,t := χM 16 to oo, ∗ + ∑

> k

χAk (t,ε )oo,k ,

et ˜oj,t := χN 16 tj oj, ∗ + ∑

> k

χAk (t,ε )oj,k .

Remarque 4.43 . Nous avons ˜ oo,t = oo sur M 16 to , et ˜ oj,t = oj sur N 16 tj .

Définition 4.44 (Espace des obstructions tronquées) . Soit ( M, g D = gDϕ,t ) une désingularisation naïve d’un orbifold d’Einstein ( Mo, g o). Sur M , nous noterons ˜O(gD) := 

{

˜oo,t + ∑

> j

˜oj,t , oo ∈ O(go), oj ∈ O(gbj )

}

,

l’espace des obstructions tronquées .

Remarque 4.45 . Pour 0 < β < 2, par régularité elliptique pour les éléments de 

O(go) et des O(gbj ) et le contrôle C40 des fonctions de coupure, on a 

∥∥∥∥˜oo,t + ∑

> j

Tj ˜oj,t 

∥∥∥∥C0(gD )

≈

∥∥∥∥˜oo,t + ∑

> j

Tj ˜oj,t 

∥∥∥∥C2,α β, ∗ (gD )

≈ sup (

‖oo‖C0(go), ‖oj ‖C0(gbj )

)

,

et 

∥∥∥∥˜oo,t + ∑

> j

˜oj,t 

∥∥∥∥L2(gD )

≈

∥∥∥∥˜oo,t + ∑

> j

˜oj,t 

∥∥∥∥r−2   

> DCαβ(gD)

≈ sup (

‖oo‖L2(go), ‖oj ‖L2(gbj )

)

.

Nous avons vu dans le corollaire 4.40 que pour toute métrique g satisfaisant 

E(g) = 0 proche de ( Mo, g o) au sens de Gromov-Hausdorff, il existe une désingu-164 Chapitre 4. Désingularisation de métriques d’Einstein larisation naïve gD et un difféomorphisme ϕ : M → M tel qu’on ait 

ΦgD (ϕ∗g) := E(ϕ∗g) + δ∗ 

> ϕ∗g

˜δgD ϕ∗g = 0 .

Nous montrons que l’on peut perturber gD + v orthogonalement à ˜ O(gD) pour des paramètres t et v ∈ ˜O(gD) suffisamment petits en une métrique ˆ gv = ˆ gϕ,t,v qui aura les mêmes paramètres de jauge (qui appartient à un même supplémentaire du noyau) mais sera solution de : 

ΦgD (ˆ g) ∈ ˜O(gD).

Contrôle de l’inverse de la linéarisation. Nous pouvons tout d’abord mon-trer que la linéarisation est inversible et que l’on peut contrôler son inverse indé-pendamment des échelles de recollement à l’aide du lemme 4.42. Montrons tout d’abord que l’opérateur π ˜O(gD )⊥ PgD est très proche de PgD pour un arbre suffisamment dégénéré. 

Lemme 4.46. Il existe C > 0 tel que pour tout 2-tenseur h ∈ C2,α β, ∗ (gD), on ait 

∥∥∥(

π ˜O(gD )⊥ PgD − PgD

)

h

∥∥∥r−2    

> DCαβ(gD)

6 Ct 12

> max

‖h‖C2,α β, ∗ (gD ).

Remarque 4.47 . Ici, la constante C ne dépend que des constantes Co et Cbj du lemme 4.42. 

Démonstration. La preuve est similaire à celle de l’estimation (4.18). D’après l’équivalence des normes de la remarque 4.45, il suffit de contrôler la norme L2(gD)de la projection sur ˜ O(gD). Sur Mo, pour oo ∈ O(go), on a Pgo (oo) = 0. On peut alors intégrer par parties en utilisant le fait que PgD est auto-adjoint 

∣∣∣∣∫

> M

〈PgD h, ˜oo,t 〉gD dvgD

∣∣∣∣ =

∣∣∣∣∫

> M

〈h, P gD (˜ oo,t )〉gD dvgD

∣∣∣∣,

et on peut décomposer, comme gD = go sur M 16 to

PgD (˜ oo,t ) = Pgo oo + Pgo (( χM 16 to − 1) oo, ∗)+ Pgo

( ∑

> k

(χAk (t,ε 0) − χBo(pk ,ε 0))oo,k 

)) 

+ (

Pgo − PgD

)( ∑

> k

χAk (t,ε 0)oo,k 

)

(4.42) 3. Résolution de l’équation d’Einstein modulo obstructions 165 pour obtenir, grâce aux contrôles des χM ro et à la remarque 4.45 pour r > 0 les estimations suivantes (comparer avec la preuve de (4.18)) 

|Pgo (( χM 16 to − 1) oo, ∗)|go 6 C‖oo‖L2(go)1{2t   

> 14
> k<r D<4t
> 14
> k}

t− 12 

> k

, (4.43) 

∣∣∣∣Pgo

( ∑

> k

(χAk (t,ε 0) − χBo(pk ,ε 0))oo,k 

))∣ ∣∣∣ 6 C‖oo‖L2(go)1{ε−10 t    

> 12
> k<r D<2ε−10t
> 12
> k}

t−1 

> k

, (4.44) et 

∣∣∣∣(

Pgo − PgD

)( ∑

> k

χAk (t,ε 0)oo,k 

)∣ ∣∣∣ 6 C‖oo‖L2(go)1{ε−10 t   

> 12
> k<r D<2t
> 14
> k}

t2

> k

r−6 

> D

. (4.45) Comme nous avons pour C > 0 indépendante de t Vol ge

({ 

2t14 

> k

< r D < 4t14

> k

}) 

6

Ct k, Vol ge

({ 

ε−10 t12 

> k

< r D < 2ε−10 t12

> k

}) 

6 Cε −40 t2

> k

, et ∫     

> {ε−10t
> 12
> k<r D<2t
> 14
> k}

t2

> k

r−6 

> D

.r 3

> D

dv ge 6

Ct max , on en déduit en intégrant les contrôles (4.43), (4.44) et (4.45) des différents termes de (4.42) que l’on a 

∣∣∣∣∫

> M

〈PgD h, ˜oo,t 〉gD dvgD

∣∣∣∣ 6 Ct 12 

> k

‖h‖C2,α β, ∗ (gD )‖oo‖L2(go). (4.46) De même, pour les bulles Nj , on a pour oj ∈ O(gbj ) par invariance conforme de la norme L2 des 2-tenseurs en dimension 4 et comme Pgt = tP g pour toute métrique 

g et tout t > 0, 

∫

> M

〈PgD h, χ oj 〉gD dvgD =

∫

> M

〈 hTj

, P gDTj

˜oj

〉

> gDTj

dvgDTj

=

∫

> M

〈 hTj

, P gbj ˜oj

〉

> gbj

dvgbj

le contrôle aux points singuliers est le même et à l’infini nous avons 

Pgb

(

˜oj,t 

)

= Pgbj oj + Pgbj (( χN 16 tj − 1) oj, ∗),

et donc, comme oj = O(r−4 

> bj

), nous avons 

∣∣∣PgD (˜ oj,t )

∣∣∣gbj

6 C‖oj ‖L2(gbj )1{ 12 t−1/4   

> j<r bj<t −1/4
> j}

r−6 

> bj

≈ C‖oj ‖L2(gbj )1{ 12 t−1/4   

> j<r bj<t −1/4
> j}

t32 

> j

,

et donc comme le volume de l’anneau de rayons 12 T 12 

> j

t− 14 

> j

et T 12 

> j

t− 14 

> j

est comparable 166 Chapitre 4. Désingularisation de métriques d’Einstein à T 2 

> j

t−1 

> j

et ∣∣∣χN 16 tj

> hTj

∣∣∣gbj

6 ‖h‖C2,α β, ∗ (gD ) ponctuellement, nous avons 

∣∣∣∣∫

> M

〈PgD h, ˜oj,t 〉gD dvgD

∣∣∣∣ 6 Ct 12

> max

‖h‖C2,α β, ∗ (gD )‖oj ‖L2(gbj ), (4.47) et finalement, 

∥∥∥(

π ˜O(gD )⊥ P Dg − P Dg

)

h

∥∥∥r−2    

> DCαβ(gD)

6 Ct 12

> max

‖h‖C2,α β, ∗ (gD ).

Remarque 4.48 . Ici, les constantes ne dépendent que des constantes Co et Cbj du lemme 4.42 et Ce, εe de la proposition 4.19. 

Lemme 4.49. Soient 0 < β < 1, k ∈ N, 0 < α < 1 et (M, g D) une désingu-larisation naïve d’un orbifold d’Einstein compact ou ALE par un arbre de singu-larités. Alors, il existe τD > 0, εD > 0 et CD > 0 ne dépendant que de β, et des métriques go et gbj tels que pour tmax < τ D et pour toute métrique g telle que 

‖g − gD‖C2,α β, ∗ (gD ) 6 εD, l’opérateur 

π ˜O(gD )⊥ Pg : ˜ O(gD)⊥ ∩ C2,α β, ∗ (gD) → ˜O(gD)⊥ ∩ r−2 

> D

Cαβ (gD),

où π ˜O(gD )⊥ est la projection orthogonale pour gD sur ˜O(gD)⊥, soit inversible et tel que l’on ait pour tout 2-tenseur h ⊥ ˜O(gD) sur M ,

‖h‖C2,α β, ∗ (gD ) 6 CD‖π ˜O(gD )⊥ Pgh‖r−2   

> DCαβ(gD)

.

Remarque 4.50 . Ici, les constantes de l’énoncé ne dépendent que des constantes 

Co et Cbj du lemme 4.42 et Ce, εe de la proposition 4.19. 

Démonstration. La preuve est similaire à celle du lemme 4.37. L’idée est encore une fois de prolonger les 2-tenseurs sur les espaces modèles et d’en déduire le contrôle sur l’arbre de singularités entier. Soit 0 < ε < ε 1/(2 −β) 

> D

< ε 0 pour εD > 0 que l’on choisira suffisamment petit au cours de la preuve. Supposons que tmax < ε 4 de manière à avoir sur chaque anneau 

Ak := Ak(t, ε ) entre Nk et Nj , l’existence d’un difféomorphisme Φk : Ae(ε−1√

Tj

√tk, ε 

√

Tj ) ⊂ R4/Γk → A k ⊂ M, 3. Résolution de l’équation d’Einstein modulo obstructions 167 tel que tout 0 < β < 1, il existe C > 0, 

∥∥∥∥Φ∗

> k

gD − ge

∥∥∥∥C2,α β (Ae(ε−1√Tj 

> √tk,ε

√Tj )) 

6 Cε 2−β < Cε D.

Jusqu’à la fin de la preuve, nous prendrons la notation 

Ak := Ae(ε−1√

Tj

√tk, ε 

√

Tj ).

Soit h un 2-tenseur symétrique sur M . Grâce à la proposition 4.19 et à sa généralisation à des métriques proches de ge grâce à la proposition 4.28, pour εD

et tmax suffisamment petits, on peut choisir des 2-tenseurs Hk constants à traces nulles sur R4/Γk tels qu’on ait sur A(√

Tj t1/4 

> k

) := Ae((1 /2) √

Tj t1/4 

> k

, 4√

Tj t1/4 

> k

)

‖Φ∗

> k

h − Hk‖C2,α      

> 0(A(T1/2
> jt1/4
> k))

6 Ce

(

ε−β tβ

> 4
> k

∥∥∥Pge Φ∗

> k

h∥∥∥r−2   

> eCαβ(Ak)

+ 4 ε−1t14 

> k

‖Φ∗

> k

h − Hk‖C2,α β (Ak )

)

6 2Ce

(

ε−β tβ

> 4
> k

∥∥∥(

PgD h)

> |A k

∥∥∥r−2   

> DCαβ(gD)

+ 4 ε−1t14 

> k

‖(h − χAk Hk)‖C2,α β (gD )

)

. (4.48) Considérons alors la décomposition 

h = h∗ + ∑

> k

χAk Hk

pour le reste de la preuve. Nous définissons alors un 2-tenseur ho prolongeant h à Mo de la manière sui-vante : 

ho := χM t/ 16 

> o

h∗ + ∑

> k∈Ko

χBo(pk ,ε )Hk,

où Ko est l’ensemble des k tels que Ak ∩ M to 6 = ∅. En notant ho, ∗ := χM t/ 16 

> o

h∗, nous avons 

‖ho, ∗‖C2,α β (go) > ‖ho, ∗‖C0  

> β(go)

> ‖(h∗)|M to ‖C0  

> β(gD)

,

car la norme de h∗ sur M to est atteinte hors de la zone endommagée par le recol-lement. Comme la métrique gD est proche en fonction de tmax de la métrique go sur 168 Chapitre 4. Désingularisation de métriques d’Einstein 

M t/ 16  

> o

par (4.26), on a de plus le contrôle suivant grâce à (4.48), 

‖(PgD h)|M t/ 16 

> o

‖r−2    

> DCαβ(gD)

> ‖Pgo ho‖r−2  

> oCαβ(go)

− CC e

∑

> k

‖(PgD h)|A k ‖r−2   

> DCαβ(gD)

− γ(tmax )‖h‖C2,α β, ∗ (gD ), (4.49) où γ(tmax ) → 0 quand tmax → 0 (comparer avec (4.29) pour les champs de vec-teurs). Comme h ⊥ ˜O(gD), nous avons 

> ‖πO(go )ho‖C2,α β, ∗
> ‖ho‖C2,α β, ∗

→ 0 lorsque tmax → 0, nous avons en particulier ‖ho‖C2,α β, ∗

6 2‖πO(go)⊥ ho‖C2,α β, ∗

pour tmax assez petit. Par le lemme 4.42, comme Poho = Po(πO(go)⊥ ho), cela implique le contrôle 

‖ho‖C2,α β, ∗ (go) 6 2Co‖Poho‖r−2  

> oCαβ(go)

.

L’estimation (4.49) et le lemme 4.46 impliquent alors que pour tmax suffisamment petit, il existe C > 0 tel qu’on ait 

‖(h∗)|M to ‖C0   

> β(gD)

+ ∑

> k∈Ko

|Hk|ge − Cγ (tmax )‖h‖C2,α β, ∗ (gD ) 6 C‖π ˜O(gD )⊥ PgD h‖r−2   

> DCαβ(gD)

.

(4.50) En effet, sur un orbifold ( Mo, g o), les 2-tenseurs constants de la décomposition définissant la norme ‖.‖C2,α β, ∗

sont déterminés par la remarque 4.26. On considère ensuite le 2-tenseur h1 := h − ∑ 

> k∈Ko

Hk qui satisfait pour C > 0dépendant des constantes précédentes, 

‖π ˜O(gD )⊥ PgD h1‖r−2    

> DCαβ(gD)

6 C‖π ˜O(gD )⊥ PgD h‖r−2    

> DCαβ(gD)

+ Cγ (tmax )‖h‖C2,α β, ∗ (gD )

(4.51) grâce au contrôle (4.50) de ∑ 

> k∈Ko

|Hk|ge .Étant donné j ∈ Ko, l’orbifold Ricci-plat ALE ( Nj , g bj ) est recollé à Mo et on peut prolonger le 2-tenseur h1 = h∗ + ∑ 

> l / ∈Ko

χAl Hl à Nj par 

hj := χN t/ 16 

> j

h∗ + ∑

> l∈Kj

χBj (pl,ε )Hl,

où Kj est l’ensemble des k / ∈ Ko tels que Ak ait une intersection non vide avec le voisinage de N tj . Ce que l’on gagne en considérant h1 plutôt que h, est le fait qu’il n’y ait pas de 2-tenseur constant à prolonger à l’infini de Nj .3. Résolution de l’équation d’Einstein modulo obstructions 169 En notant hj, ∗ := χN t/ 16 

> j

h∗, on a 

‖hj, ∗‖C2,α β (gbj ) > ‖hj, ∗‖C0   

> β(gbj)

> ‖(h∗)|N tj ‖C0  

> β(gD)

, (4.52) et par (4.48) et comme gD 

> Tj

est très proche de gbj sur N t/ 16  

> j

en fonction de tmax , on a de plus le contrôle suivant grâce à (4.48) : 

∥∥∥(

PgD h1

) 

> |Nt/ 16
> j

∥∥∥r−2    

> DCαβ(gD)

> ‖Pgbj hj ‖r−2   

> bjCαβ(gbj)

− CC e

∑

> k

‖(PgD h1)|A k ‖r−2   

> DCαβ(gD)

− γ(tmax )‖h‖C2,α β, ∗ (gD ), (4.53) où γ(tmax ) → 0 quand tmax → 0. Nous obtenons alors un contrôle sur ( h∗)N tj et sur les Hk, k ∈ Kj grâce au lemme 4.32 en utilisant encore le fait que h ⊥ ˜O(gD)qui implique que pour tmax assez petit, nous avons 

‖hj ‖rj C3,α β, ∗ (gbj ) 6 2Cj ‖Pgbj hj ‖r−2   

> jCαβ(gbj)

.

On obtient donc grâce aux estimations (4.53), (4.48) et au lemme 4.46, l’estimation 

‖(h∗)|N tj ‖C0 

> β

+ ∑

> k∈Kj

|Hk|ge − Cγ (tmax )‖h‖C2,α β, ∗ (gD ) 6 C‖π ˜O(gD )⊥ PgD h‖r−2   

> DCαβ(gD)

.

(4.54) En itérant aux autres orbifolds Ricci-plats ALE, nous obtenons des contrôles similaires à (4.54) sur tous les Nj et avec le contrôle (4.50) nous avons finalement 

(

1 − Cγ (tmax ))

‖h‖C2,α β, ∗ (gD ) 6 C‖π ˜O(gD )⊥ PgD h‖r−2   

> DCαβ(gD)

,

et donc le résultat énoncé pour g = gD pour tmax suffisamment petit. Pour passer à une autre métrique g proche de gD, il suffit d’utiliser la propo-sition 4.28 pour s’assurer que pour ‖g − gD‖C2,α β, ∗ (gD ) arbitrairement petit, Pg est arbitrairement proche de PgD pour la norme d’opérateur sur C2,α β, ∗ (gD). L’opérateur P étant auto adjoint sur une variété compacte, son injectivité implique sa surjectivité. 170 Chapitre 4. Désingularisation de métriques d’Einstein 

3.2 Résolution de l’équation d’Einstein modulo obstructions 

Montrons maintenant que l’on peut toujours résoudre une équation d’Einstein 

modulo obstructions . Rappelons qu’être d’Einstein et en jauge divergence réduite par rapport à une désingularisation naïve gD est équivalent à annuler l’opérateur 

ΦgD : g 7 → E(g) + δ∗ 

> g

˜δgD g. 

Théorème 4.51. Soient (Mo, g o) un orbifold d’Einstein compact ou ALE de di-mension 4 tel que Ric( go) = Λ go, pour Λ ∈ R, et soit (Nj , g bj )j un arbre de singularités permettant de désingulariser (Mo, g o) avec une configuration de dés-ingularisation D, et 0 < β < 1.Alors, il existe τ > 0, ε > 0 ne dépendant que des métriques go et gbj tels que pour toute désingularisation naïve gD := gDϕ,t , satisfaisant tmax < τ , et ϕ = ( ϕk)k ∈

Isom( R4/Γk)k, et pour tout v ∈ ˜O(gD) satisfaisant ‖v‖C0  

> β, ∗(gD)

< ε , il existe une 

unique solution ˆgv = ˆ gϕ,t,v de l’équation 

ΦgD (ˆ gv) ∈ ˜O(gD),

satisfaisant les conditions suivantes : 1. ‖ˆgv − gD‖C2,α β, ∗

6 2ε,2. ˆgv − (gD + v) est orthogonal à ˜O(gD) pour le produit L2 de gD.Remarque 4.52 . Ici, les constantes ne dépendent que des constantes Co et Cbj du lemme 4.42 et Ce, εe de la proposition 4.19. 

Démonstration. Soit ( M, g Dϕ,t ) = ( M, g D) une désingularisation naïve d’un orbifold (Mo, g o) par un arbre de singularités ( Nj , g bj ). Définissons l’opérateur Ψ : gD + ( ˜O(gD)⊥ ∩ C2,α β, ∗

> )

→ ˜O(gD)⊥ ∩ r−2 

> D

Cαβ (gD), Ψ( g) := π ˜O(gD )⊥ ΦgD (g) = π ˜O(gD )⊥

> (

E(g) + δ∗ 

> g

˜δgD (g))

,

où π ˜O(gD )⊥ est la projection orthogonale sur ˜ O(gD)⊥ pour le produit L2(gD). La conclusion de l’énoncé pour v = 0 se réécrit alors : il existe une unique solution g

à l’équation Ψ( g) = 0. Cherchons à appliquer le théorème des fonctions inverses 1.12 à Ψ. Calculons donc tout d’abord sa différentielle en gD. La linéarisation de l’opérateur Ψ en gD3. Résolution de l’équation d’Einstein modulo obstructions 171 est donc pour tout 2-tenseur symétrique h,

dgΨ( h) = π ˜O(gD )⊥ ¯Pg(h),

où ¯PgD est explicité dans (4.38). Montrons que cette linéarisation en gD est in-versible et d’inverse borné. Nous cherchons à nous ramener à l’opérateur P = 

> 12

∇∗∇h − ˚R( h) pour lequel l’inversibilité a été prouvée dans le lemme 4.49. Tout d’abord, par l’estimation (4.18), nous avons 

‖˜δgD h − δgD h‖rD C3,α β, ∗ (gD ) 6 Ct 12

> max

‖h‖C2,α β, ∗ (gD ),

et nous en déduisons que le terme −2δ∗ 

> g

δgh + 2 δ∗ 

> g

˜δgD h − (δgD δgD h)gD de (4.38) est contrôlé de la manière suivante 

‖ − 2δ∗ 

> g

δgh + 2 δ∗ 

> g

˜δgD h − (δgD δgD h)gD‖r−2    

> DCαβ(gD)

6 Ct 12

> max

‖h‖C2,α β, ∗ (gD ). (4.55) Remarquons de plus que la courbure de Ricci de gD est presque constante dans le sens suivant 

‖ Ric( gD) − ΛgD‖r−2 

> DCαβ

6 Ct 2−β 

> 4
> max

, (4.56) car Ric( gD) − ΛgD = 0 pour rD > 2t1/4max , et sur le reste de la variété, | Ric( gD) −

ΛgD| 6 C. Ainsi, pour tmax arbitrairement petit, dgD Ψ est proche (comme opéra-teur de C2,α β, ∗ dans r−2 

> D

Cαβ ) à une puissance de tmax -près de l’opérateur π ˜O(gD )⊥ ˆPgD ,où, pour un 2-tenseur h, nous notons ˆPgD (h) := 12

(

∇∗ 

> gD

∇gD h − 2˚RgD (h)

− ∇ 2 

> gD

tr gD h + (∆ gD tr gD h)gD + RgD

4 (tr gD h)gD

)

,

où l’on a négligé les termes de divergence par (4.55), et simplifié les termes impli-quant la courbure par (4.56) dans l’expression (4.38). Pour tout 2-tenseur v, nous avons la décomposition en un 2-tenseur conforme et un 2-tenseur sans trace v = tr gD v 

> 4

gD + ( v − tr gD v 

> 4

gD) qui est gD-orthogonale. Maintenant, nous avons tr gD

(

π ˜O(gD )⊥ ˆPgD (h)

)

= tr gD ˆPgD (h) − tr gD

(

π ˜O(gD ) ˆPgD (h)

)

.172 Chapitre 4. Désingularisation de métriques d’Einstein Comme pour un élément ˜ o de ˜ O(gD), nous avons 

‖(tr gD ˜o)gD‖r−2 

> DCαβ

‖˜o‖r−2 

> DCαβ

→ 0 (4.57) lorsque tmax → 0, l’opérateur tr gD (π ˜O(gD )⊥ ˆPgD ) est arbitrairement proche de l’opé-rateur tr gD ˆPgD (comme opérateurs de C2,α β, ∗ dans r−2 

> D

Cαβ ) qui est à son tour arbi-trairement proche de ∆ gD + Λ pour tmax arbitrairement petit car notre métrique est presque d’Einstein d’après (4.56) et à la preuve du lemme 1.24. Pour la partie sans trace en rappelant que pour tout 2-tenseur h, h = π ˜O(gD )⊥ h+

π ˜O(gD )h, nous avons la décomposition suivante : 

π ˜O(gD )⊥ ˆPgD (h) − tr gD

(

π ˜O(gD )⊥ ˆPgD (h)) gD

4 = π ˜O(gD )⊥

(

ˆPgD (h) − tr gD

( ˆPgD (h)) gD

4

)

− π ˜O(gD )tr gD

( ˆPgD (h)) gD

4+

(

tr gD

(

π ˜O(gD ) ˆPgD (h))) gD

4 . (4.58) En utilisant une nouvelle fois (4.56) et le fait que la trace des éléments de ˜ O(gD) est petite, nous voyons que la partie sans trace de π ˜O(gD )⊥ ˆPgD (h) est arbitrairement proche de la projection sur ˜ O(gD) de la partie sans trace de ˆPgD (h), c’est-à-dire de 

π ˜O(gD )⊥

(

PgD (h) − (

∇2 

> gD

tr gD h − ∆gD tr gD hgD

4

)) 

.

Décomposons alors h et l’opérateur π ˜O(gD ) ˆPgD (h) de cette manière en une partie conforme et une partie sans trace. Nous obtenons un opérateur par blocs : 

π ˜O(gD )⊥ ˆPgD =

 ∆gD + Λ 0

π ˜O(gD )⊥

(

∆gD tr gD hgD 

> 4

− ∇ 2 

> gD

tr gD h)

π ˜O(gD )⊥ PgD

 + AgD

où AgD : C2,α β, ∗ → r−2 

> D

Cαβ est un opérateur arbitrairement petit lorsque tmax est arbitrairement petit. Il nous reste alors à montrer que 

 ∆gD + Λ 0

π ˜O(gD )⊥

(

∆gD tr gD hgD 

> 4

− ∇ 2 

> gD

tr gD h)

π ˜O(gD )⊥ PgD



de C2,α β, ∗ dans r−2 

> D

Cαβ est un opérateur inversible avec un inverse uniformément borné indépendamment de t pour tmax suffisamment petit. Il suffit de le montrer pour les deux blocs diagonaux séparément. L’opérateur ∆ gD + Λ est inversible 3. Résolution de l’équation d’Einstein modulo obstructions 173 avec un inverse indépendant de t d’après la preuve du lemme 1.24 et l’estimation (4.56), et c’est aussi le cas pour l’opérateur π ˜O(gD )⊥ PgD d’après le lemme 4.49. On conclut à l’aide du lemme 1.60 que la linéarisation de Ψ en gD est inversible et a un inverse borné car elle est arbitrairement proche d’un opérateur inversible. 

Remarque 4.53 . L’opérateur ¯PgD n’est, lui, pas auto-adjoint car la métrique gD

n’est pas d’Einstein. Tous les termes sont auto-adjoints un à un sauf −∇ 2

> g

tr gh,

−(δgδgh)g, et 〈Ric g, h 〉gg, on remarque que l’adjoint de h 7 → ∇ 2

> g

tr gh est h 7 →

(δgδgh)g, mais le terme h 7 → 〈 Ric g, h 〉gg dont l’adjoint est h 7 → (tr gh) Ric g empêche ¯PgD d’être auto-adjoint. Pour appliquer le théorème des fonctions inverses, lemme 1.12 à l’opérateur Ψ, il reste à contrôler les termes non-linéaires. Or, comme les variations de la courbure de Ricci s’écrivent schématiquement, pour une variation h d’une métrique g,Ric( g + h) = Ric( g) + ( g + h)−1 ∗ Rm( g) + ( g + h)−2 ∗ ∇ 2h + ( g + h)−3 ∗ ∇ h ∗ ∇ h, 

où ∗ désigne diverses opérations multilinéaires et par la proposition 4.16, les termes non-linéaires QgD (h) := Ψ( gD + h) − Ψ( gD) − dgD Ψ( h) satisfont le contrôle 

‖QgD (h)−QgD (h′)‖r−2   

> DCαβ(gD)

6 C

((

‖h‖Cα   

> 0(gD)

+ ‖h′‖Cα  

> 0(gD)

)

‖h − h′‖Cα  

> 0(gD)

‖ Rm( gD)‖r−2   

> DCαβ(gD)

+ ‖h − h′‖Cα  

> 0(gD)

(

‖∇ 2h‖r−2    

> DCαβ(gD)

+ ‖∇ 2h′‖r−2   

> DCαβ(gD)

)

+(

‖h‖Cα   

> 0(gD)

+ ‖h′‖Cα  

> 0(gD)

)

‖∇ 2(h − h′)‖r−2   

> DCαβ(gD)

+ 2 ‖∇ (h − h′)‖r−1   

> DCαβ(gD)

(

‖∇ h‖r−1    

> DCαβ(gD)

+ ‖∇ (h′)‖r−1   

> DCαβ(gD)

))

6 3C(

‖h‖C2,α β, ∗ (gD ) + ‖h′‖C2,α β, ∗ (gD )

)

‖h − h′‖C2,α β, ∗ (gD ).

D’après le théorème des fonctions inverses, lemme 1.12, comme on a le contrôle 

‖Ψ( gD)‖r−2    

> DCαβ(gD)

6 Ct 2−β 

> 4
> max

,

il existe donc une unique solution ˆ g pour tmax suffisamment petit, à l’équation Ψ(ˆ g) = 0 qui satisfait de plus ‖gD − ˆg‖C2,α β, ∗ (gD ) 6 ‖Ψ( gD)‖r−2    

> DCαβ(gD)

6 Ct 2−β 

> 4
> max

.Maintenant, nous n’avons résolu l’équation qu’au voisinage de gD et sur l’ortho-gonal de ˜ O(gD). En s’intéressant pour v ∈ ˜O(gD) à l’opérateur Ψ v(g) := Ψ( g + v), le contrôle des termes non-linéaires est exactement le même pour cet opérateur, et pour v arbitrairement petit, dgD +vΨv est arbitrairement proche de dgD Ψ qui est 174 Chapitre 4. Désingularisation de métriques d’Einstein inversible. On en déduit qu’il existe ε > 0 tel que pour tout ‖v‖C0   

> β(gD)

< ε , il existe une unique solution ˆ gv de Ψ v(ˆ gv) = 0, et la conclusion de l’énoncé. 

Remarque 4.54 . En ajoutant v, on détériore l’estimation sur Ψ v(gD + v) qui n’est plus contrôlé que par : 

‖Ψv(gD + v)‖r−2    

> DCαβ(gD)

6 C(

‖v‖2   

> C2,α β(gD)

+ t2−β

> 4
> max
> )

.

Nous verrons dans le chapitre 5 suivant que sans hypothèse sur l’intégrabilité des déformations infinitésimales, on ne peut pas espérer mieux. 

Corollaire 4.55. Avec les notations du théorème 4.51, l’application v 7 → ˆgv est analytique. Démonstration. C’est une conséquence du théorème des fonctions implicites pour les applications analytiques. Définissons l’application (v, h ) 7 → Ψ(ˆ g0 + v + h)de ˜ O(gD) × ( ˜O(gD)⊥ ∩ C2,α β, ∗

> )

→ ˜O(gD)⊥ ∩ r−2 

> D

Cαβ (gD) où l’on note Ψ( g) := π ˜O(gD )⊥ ΦgD (g) = π ˜O(gD )⊥

> (

E(g) + δ∗ 

> g

˜δgD (g))

,

comme dans la preuve du théorème 4.51 et où ˆ g0 est la solution donnée par le théorème 4.51 pour v = 0. L’application ( v, h ) 7 → Ψ(ˆ g0 + v + h) est analytique car E et g 7 → δ∗ 

> g

le sont, et car ˜δgD et π ˜O(gD )⊥ sont linéaires. Nous savons que ‖ˆg0 − gD‖ 6 Ct 2−β 

> 4
> max

, et que dgD Ψest inversible d’après la preuve du théorème 4.51. Nous en déduisons que dˆg0 Ψ est aussi inversible. Le théorème des fonctions implicites, lemme 1.26, nous assure alors, par l’uni-cité de la solution ˆ gv du théorème 4.51 pour v petit, que l’application v 7 →

ˆgv − (gD + v) est analytique, puis que v 7 → ˆgv est analytique. 

Remarque 4.56 . Grâce à la proposition 4.39, il est possible d’écrire le résultat sous une autre forme en imposant directement à g d’être en jauge divergence réduite par rapport à gD. Il faut alors modifier ˜ O(gD) par πg ˜O(gD), où πgh := 

h − δ∗

> g
> (

˜δgδ∗

> g
> )−1

δgh est une projection sur le noyau de ˜δg, voir la preuve de [Biq13, Proposition 9.1] et en particulier l’opérateur défini dans [Biq13, (66)] pour plus de détails. Le résultat se réécrit de la manière suivante. Avec les mêmes suppositions, 3. Résolution de l’équation d’Einstein modulo obstructions 175 nous avons aussi une unique solution ˆ gv = ˆ gϕ,t,v de l’équation 

E(ˆ gv) ∈ πˆgv ˜O(gD),

satisfaisant les conditions suivantes : 1. ‖ˆgv − gD‖C2,α β, ∗

6 2ε,2. ˜δgD ˆgv = 0, 3. ˆ gv − (gD + v) est orthogonal à ˜ O(gD) pour le produit L2 de gD.Ces deux définitions de métriques d’Einstein modulo obstructions sont différentes, mais donnent les mêmes métriques lorsqu’elles sont d’Einstein. Grâce au corollaire 4.40, nous avons le résultat suivant. 

Corollaire 4.57. Soient D0, v 0 > 0, l ∈ N, et β = β(v0, D 0) > 0 obtenu dans le corollaire 4.5. Alors, pour tout ε > 0, il existe δ = δ(ε, D 0, v 0, l ) > 0 tel que si 

(M, g E ) est une variété d’Einstein satisfaisant — le volume est minoré par v0 > 0,— le diamètre est majoré par D0,— la courbure de Ricci est bornée | Ric | 6 3.et telle que pour un orbifold d’Einstein (Mo, g o),

dGH 

> (

(M, g E ), (Mo, g o))

6 δ, 

alors, il existe une désingularisation naïve (M, g D + v) de (Mo, g o) par un arbre de singularités, et un difféomorphisme ψ : M → M tels que 

ψ∗gE = ˆ gv,

où ˆgv est la perturbation de gD + v construite dans le théorème 4.51. 

L’ensemble des métriques Ricci-plates sur la surface K3 désingularisant l’orbi-fold T4/Z2 est un exemple d’application de ce théorème. C’est un cas particulier où E(g) n’est pas seulement orthogonal aux déformations infinitésimales de l’or-bifold et des variétés Ricci-plates ALE, mais s’annule pour tous paramètres de recollement. 

Exemple 4.58 (Désingularisation d’Einstein de T4/Z2). Une construction pro-posée par Gibbons-Pope [GP79] et Page [Pag78] et obtenue rigoureusement par Topiwala [Top87a, Top87b] pour la première fois permet de désingulariser l’orbi-fold T4/Z2 de l’exemple 2.5 qui a 16 points singuliers modelés sur R4/Z2. L’idée est 176 Chapitre 4. Désingularisation de métriques d’Einstein de recoller à chacun des points singuliers des copies de la variété d’Eguchi-Hanson (voir (2.5) pour sa définition) qui sont Ricci-plates et asymptotiques à R4/Z2 dans la même orientation (pour pouvoir utiliser des techniques de géométrie kählé-rienne), c’est-à-dire que les paramètres de recollements sont dans SO (4). Il est ensuite possible de perturber la métrique obtenue en une métrique Ricci-plate. Il y a de nombreuses ambiguïtés dans la construction qui peuvent être vues de deux manières différentes : 1. il y a un espace de dimension 3 de déformations intégrables de la métrique d’Eguchi-Hanson (qui sont toutes homothétiques). 2. lorsque l’on recolle la i-ème métrique d’Eguchi-Hanson, il y a un paramètre d’échelle ti > 0 et un paramètre de rotation ϕi ∈ SO (4) à choisir. Ces deux sources d’ambiguïtés sont en fait équivalentes dans cet exemple car les rotations et changements d’échelle des recollements peuvent être vus comme des variations de la métrique d’Eguchi-Hanson. Cette métrique étant U (2)-invariante, les rotations correspondent à SO (4) /U (2) et donc à deux dimensions de défor-mations et le changement d’échelle correspond à la troisième déformation de la métrique. À ces ambiguïtés de recollements, il faut ajouter les déformations plates à trace et divergence nulles de T4/Z2 qui forment un espace de dimension 9 (com-posé des 2-tenseurs symétriques constants à trace nulle). En tout, il y a donc 57 = 9 + 16 × 3 directions de déformation indépendantes qui correspondent aux noyaux des opérateurs d’Einstein des espaces modèles. 

Figure 4.3 – Approximation de métrique hyperkählérienne. 4. Préespace de modules autour d’une métrique singulière 177 

# 4 Préespace de modules directionnel au voisinage d’une métrique singulière 

Soit M une variété différentiable de dimension 4 et considérons ( Mo, g o) ∈

∂oE(M ) ⊂ E(M )GH \E(M ) une métrique orbifold du bord de son espaces de modules des métriques d’Einstein. D’après le théorème 3.42, toutes les métriques d’Einstein proches dans au sens de Gromov-Hausdorff de ( Mo, g o) sont en réalité proches d’une désingularisation naïve ( M, g Dt ) de ( Mo, g o) au sens Ck,α β, ∗ pour une configuration de désingularisation D.On définit alors par analogie avec la définition 1.17 le préespace de modules 

directionnel au voisinage d’une métrique singulière. 

Définition 4.59 (Préespace de modules des métriques d’Einstein au voisinage d’une métrique singulière) . Nous définissons EDgo (M ), le préespace de modules des métriques d’Einstein sur M au voisinage de ( Mo, g o) et dans la direction D, comme l’ensemble des métriques d’Einstein g sur M pour lesquelles il existe t tel que l’on ait ‖g − gDt ‖C2,α β, ∗ (gDt ) < ε pour ε > 0 la constante du théorème 4.51 et v ∈ ˜O(gDt )pour lequel on ait : 1. E(g) = 0, Vol( g) = Vol( go), 2. g − (

gDt + v)

⊥gDt

˜O(gDt ), 3. ˜δgDt g = 0. 

Remarque 4.60 . Ce préespace est directionnel dans le sens où il ne couvre pas toutes les désingularisations de Gromov-Hausdorff de ( Mo, g o), mais seulement celles faisant apparaître l’arbre de singularités donné par D. En effet, cela corres-pondrait à toutes les configurations d’arbres de singularités aboutissant à ( Mo, g o)qui ne sont pas toutes C2

> β, ∗

-proches les unes des autres. Étant donnée une suite quelconque de métriques d’Einstein lisses ( gi)i sur M convergeant vers ( Mo, g o), alors, quitte à prendre une sous-suite, toutes les métriques gi sont dans un unique 

préespace de modules directionnel EDgo (M ). 

Remarque 4.61 . En général, il n’est pas clair que l’on puisse recoller ensemble ces préespaces de modules directionnels pour obtenir un vrai voisinage de ∂oE(M ). Dans le cas kählérien, ces différentes directions recouvrent l’espace des paramètre des désingularisations kählériennes de R4/Γ, c’est-à-dire un espace RdΓ \DΓ, où DΓ

est une union finie de sous-espaces vectoriels, et les différents arbres de singularités correspondent à des voisinages particuliers de l’ensemble DΓ qui paramètrent les métriques orbifolds. 178 Chapitre 4. Désingularisation de métriques d’Einstein 

Proposition 4.62. Le pré-espace de modules directionnel EDgo (M ) est l’ensemble des zéros de E sur l’ensemble des métriques ˆgt,v au voisinage des gDt du théorème 4.51. 

Comme E est analytique, il suffirait de comprendre la structure de l’ensemble des ˆ gt,v ou des obstructions associées pour déterminer la structure locale de l’espace de modules au voisinage de sa frontière. Notons qu’en adaptant le corollaire 4.55, cet ensemble a une structure analytique là où t > 0 et l’on retrouve la structure analytique au voisinage d’une métrique lisse de la proposition 1.31 avec notre paramétrisation particulière. La question se résume donc, comme on aurait pu s’y attendre, à comprendre ce qu’il se passe autour de t = 0. Chapitre 5 Obstructions à la désingularisation de certains orbifolds d’Einstein 

Dans ce chapitre, dont les résultats sont essentiellement tirés de [Ozu19b], nous étudions les obstructions à la résolution de l’équation d’Einstein du chapitre précédent (ch. 4). Nous montrons que ces obstructions ne s’annulent pas dans certaines situations et en déduisons que certaines métriques d’Einstein singulières ne peuvent jamais être désingularisées, même au sens le plus faible de Gromov-Hausdorff. Cela répond à la question 0.5 posée dans les années 80. 

Contributions. Nous étudions les obstructions à la dGH -désingularisation d’or-bifolds par des métriques d’Einstein lisses du chapitre précédent (ch. 4). Nous étendons donc le résultat d’obstruction de [Biq13, Biq16, Biq17] valable pour la désingularisation par une métrique d’Eguchi-Hanson et sous des hypothèses res-trictives dans plusieurs directions : nous autorisons — une simple dGH -proximité avec l’orbifold, — l’orbifold à avoir des déformations infinitésimales d’Einstein (pas nécessai-rement intégrables), — plusieurs singularités, — des bulles quelconques à déformations infinitésimales d’Einstein intégrables. Dans le cas conjecturalement général des formations d’arbres d’orbifolds Ricci-plats ALE en un nombre arbitraire de points, nous retrouvons l’obstruction de [Biq13], det R = 0, à tous les points singuliers. Nous en déduisons que sous des hypothèses topologiques répandues sur la variété M , comme la condition spin, 179 180 Chapitre 5. Obstructions à la désingularisation l’obstruction det R = 0 doit être satisfaite aux points singuliers des métriques de 

∂oE(M ). Nous exhibons enfin la première obstruction générale à la désingularisation d’orbifolds sphériques et hyperboliques sans supposition sur les bulles apparais-sant. 

# 1 Contrôle des obstructions 

Montrons tout d’abord un lemme technique qui contrôle les distances entre métriques et les obstructions. 

Proposition 5.1. Soit 0 < α < 1, et (M, g D = gDϕ,t ) une désingularisation naïve. Il existe ε > 0 et C > 0 tels que si la métrique (M, ˆg = ˆ gϕ,t, 0) obtenue par le théorème 4.51 (noter qu’ici v = 0 ) est une métrique d’Einstein satisfaisant : 1. ‖ˆg − gD‖C2,α β, ∗ (gD ) 6 2ε,2. ˜δgD ˆg = 0 ,3. ˆg − gD est orthogonal à ˜O(gD) pour le produit L2 de gD.et si une métrique gA, satisfait : 1. ‖gA − gD‖C2,α β, ∗ (gD ) 6 2ε,2. gA − gD est orthogonal à ˜O(gD) pour le produit L2 de gD,alors, en notant Ψ( gA) = π ˜O(gD )⊥ ΦgD (gA), on a 

‖ˆg − gA‖C2,α β, ∗ (gD ) 6 C∥∥∥Ψ( gA)∥∥∥r−2   

> DCαβ(gD)

, (5.1) 

et si l’on note oA := π ˜O(gD )ΦgD (gA), on a 

‖oA‖L2(gD ) 6 (

‖Ψ( gA)‖r−2    

> DCαβ(gD)

+ ‖Ψ( gD)‖r−2   

> DCαβ(gD)

+ t12

> max

)

‖Ψ( gA)‖r−2   

> DCαβ(gD)

. (5.2) 

Démonstration. Remarquons tout d’abord que l’inégalité (5.1) est une consé-quence directe de la preuve du théorème 4.51. En effet, le théorème des fonctions inverses utilisé permet en fait de contrôler la distance d’une métrique gA à l’unique solution ˆ g de Ψ(ˆ g) = 0 en fonction de la valeur de Ψ( gA). On a plus précisément 

‖gA − ˆg‖C2,α β, ∗ (gD ) 6 C‖Ψ( gA)‖r−2   

> DCαβ(gD)

.1. Contrôle des obstructions 181 En combinant cela avec le contrôle similaire ‖gD − ˆg‖C2,α β, ∗ (gD ) 6 ‖Ψ( gD)‖r−2   

> DCαβ(gD)

,nous avons alors pour tout 2-tenseur h sur M , en notant ¯PgA := dgA ΦgD

∥∥∥( ¯PgA − ¯PgD

)

h∥∥∥r−2    

> DCαβ(gD)

6 ∥∥∥( ¯PgA − ¯Pˆg

)

h∥∥∥r−2    

> DCαβ(gD)

+ ∥∥∥( ¯Pˆg − ¯PgD

)

h∥∥∥r−2   

> DCαβ(gD)

6 C(

‖gA − ˆg‖C2,α β, ∗ (gD ) + ‖ˆg − gD‖C2,α β, ∗ (gD )

)

‖h‖C2,α   

> 0(gD)

6C(

‖Ψ( gA)‖r−2    

> DCαβ(gD)

+ ‖Ψ( gD)‖r−2   

> DCαβ(gD)

)

‖h‖C2,α   

> 0(gD)

.

Grâce à l’inégalité (4.46), au contrôle sur hA := ˆ g − gA ⊥ ˜O(gD) et en remarquant que r−2 

> D

Cαβ (gD) ⊂ L2(gD), on a 

∣∣∣〈 ¯PgA hA, ˜oo,t 

〉

> L2

∣∣∣ 6 C′∥∥∥( ¯PgA − ¯PgD

)

hA∥∥∥r−2 

> DCαβ

‖˜oo,t ‖L2 + ∣∣∣〈 ¯PgD hA, ˜oo,t 

〉

> L2

∣∣∣

6 C′∥∥∥( ¯PgA − ¯PgD

)

hA∥∥∥r−2 

> DCαβ

‖˜oo,t ‖L2 + Ct 12

> max

‖oo‖L2 ‖hA‖C2,α β, ∗

6 CC ′γ(gA, g D, t max )‖oo‖L2 ‖hA‖C2,α β, ∗

.

où C, C ′ > 0 ne dépendent que de β, et où γ(gA, g D, t max ) := (

‖Ψ( gA)‖r−2    

> DCαβ(gD)

+

‖Ψ( gD)‖r−2    

> DCαβ(gD)

+ t12

> max

)

. Et de même sur les N tj , on a les mêmes contrôles aux points singuliers et à l’infini on utilise l’inégalité (4.47), pour oj ∈ O(gbj ), on a donc 

∣∣∣〈 ¯PgD hA, ˜oj,t 

〉 

> L2(gD)

∣∣∣ 6 CC ′γ(gA, g D, t max )‖oj ‖L2(gbj )‖hA‖C2,α β, ∗ (gD ). (5.3) Soit oA la projection orthogonale sur ˜ O(gD) de ΦgD (gA). Comme ΦgD (ˆ g) = 0, et dgA ΦgD = ¯PgA , nous avons 

−oA = ΦgD (ˆ g) − oA = Ψ( gA) + ¯PgA hA + QgA (hA), (5.4) où les termes non-linéaires QgA (hA) = ΦgD (ˆ g) − ΦgD (gA) − dgA ΦgD (hA) satisfont 

‖QgA (hA)‖r−2   

> DC0(M)

6 C‖hA‖2

> C0
> β, ∗

6 C∥∥∥Ψ( gA)∥∥∥2   

> r−2
> DC0
> β(gD)

, (5.5) et on a donc par définition des normes à poids, pour o ∈ ˜O(gD), 

∣∣∣〈

o, Q gA (hA)〉 

> L2(gD)

∣∣∣ 6 C‖o‖L2

∥∥∥Ψ( gA)

∥∥∥2   

> r−2
> DC0
> β(gD)

,182 Chapitre 5. Obstructions à la désingularisation et donc, comme Ψ( gA) ⊥gD oA par définition de Ψ, on a par (5.4), 

−‖ oA‖2  

> L2(gD)

=

> 〈

ΦgD (ˆ g) − oA, oA

> 〉
> gD

= 〈 ¯PgA hA + QgA (hA), oA〉 

> gD

,

Finalement, grâce à (5.3) et (5.5) nous avons donc 

‖oA‖2  

> L2(gD)

6 γ(gA, g D, t max )‖Ψ( gA)‖r−2   

> DCαβ(gD)

‖oA‖L2(gD ).

Remarque 5.2 . L’inégalité (5.1) signifie que si l’on arrive à construire une métrique 

gA qui annule presque l’opérateur Ψ, alors gA est en fait une bonne approxima-tion de ˆ g. Cela nous permettra de décrire de manière arbitrairement précise les métriques d’Einstein qui dégénèrent. L’inégalité (5.2) est un résultat d’obstruction. En effet, si l’on peut construire une métrique d’approximation gA, pour laquelle ΦgD (gA) est petit, mais sans que 

oA := π ˜O(gD )ΦgD (gA) ne le soit, alors cela signifie qu’il ne peut pas y avoir de variété d’Einstein proche au sens de Gromov-Hausdorff de l’orbifold ( Mo, g o) dans les mêmes jauges. 

# 2 Obstruction en un des points singuliers 

Afin d’exhiber de premières obstructions à la désingularisation d’orbifolds, nous allons construire une meilleure approximation de la dégénérescence des variétés d’Einstein qui nous assure que l’on approche une métrique d’Einstein modulo obstructions par (5.1), et on en déduira des obstructions sur l’orbifold limite par (5.2). Dans cette section, nous nous restreignons à montrer qu’une obstruction est satisfaite à un point singulier si l’on suppose qu’il n’y a pas d’arbre de singula-rités. L’analyse nécessaire pour l’obtenir à tous les points est développée dans la section suivante, et les arbres de singularités kählériennes sont considérés dans la quatrième section de ce chapitre. Pour cela nous faisons apparaître les termes quadratiques du développement de la métrique orbifold à un point singulier à l’infini de la bulle que l’on recolle dans la proposition 5.3. L’erreur faite dans le recollement est alors plus faible et la métrique obtenue plus proche d’être Einstein dans les normes qui nous inté-ressent d’après le corollaire 5.9. Cela permet de déduire un résultat d’obstruction 2. Obstruction en un des points singuliers 183 à la désingularisation de Gromov-Hausdorff d’orbifolds d’Einstein par des variétés Ricci-plates ALE dont les déformations infinitésimales sont intégrables dans les corollaires 5.12 et 5.32. 

2.1 Perturbation des bulles par les termes quadratiques de la métrique orbifold 

Traitons pour commencer le cas où l’on désingularise un orbifold d’Einstein par des variétés Ricci-plates ALE que l’on ne perturbe qu’orthogonalement au noyau approché ˜ O(gD), ce qui revient à appliquer le théorème 4.51 pour v = 0. C’est le cadre habituel des théorèmes de perturbation et de l’obstruction de [Biq13] car les orbifolds considérés dans [Biq13] n’ont pas de déformations infinitésimales d’Einstein. Au voisinage d’un point singulier orbifold, il existe des coordonnées où 

go = ge + H2 + O(r3 

> o

),

et 

δeH2 = 0 ,

où H2 est un 2-tenseur symétrique dont les coefficients sont des polynômes homo-gènes de degré 2. On souhaite donc ajouter à l’orbifold ALE des termes asymptotiques au tenseur d’ordre principal à la singularité, H2, tout en annulant la linéarisation de l’opé-rateur d’Einstein pour minimiser l’erreur. Il se trouve que ce n’est pas toujours possible, et que l’on ne peut que résoudre l’équation modulo obstructions . Notons 

O4(gbj ) l’orthogonal des éléments de O(gbj ) qui décroissent en o(r−4 

> b

) à l’infini. On notera O4(gb) l’espace de ces tenseurs homogènes harmoniques sur R4/Γ. Ces tenseurs sont harmoniques homogènes sur R4/Γ et décroissent en r−4 

> b

.Une conséquence du lemme 4.42 est que l’on peut toujours résoudre l’équation de prolongement de H2 sur la bulle modulo obstructions explicites. Considérons o4

> i

une base orthonormée de O4(gbj ), et O4 

> i

leur terme dominant harmonique homo-gène décroissant en r−4 

> e

.

Proposition 5.3. Soit (N, g b) un orbifold Ricci-plat ALE asymptotique à R4/Γ et 

H2 un 2-tenseur homogène quadratique sur R4/Γ et λ ∈ R tels qu’on ait : 

¯PeH2 + λg e = 0 .184 Chapitre 5. Obstructions à la désingularisation 

Alors, il existe un 2-tenseur h2, et des réels λi tels que (h2, λ i) soit une solution de 

¯Pbh2 + λg b = ∑

> i

λio4 

> i

,

|h2 − χH 2|gb = O(r−2 

> b

),

où χ est une fonction de coupure à support dans un voisinage de l’infini de (N, g b)

où les coordonnées ALE sont définies et où 

λi := −

∫

> S3/Γ

(

3〈H2, O 4 

> i

〉ge + O4

> i

(

∇etr eH2, ∂ re

)) 

dvS3/Γ.

L’ensemble des solutions est en fait (h2 + O(gb), λ i).Démonstration. Nous avons ¯Pb(χH 2) + λg b ∈ r−2 

> b

Cαβ (gb) pour 0 < β < 1 car dans un voisinage de l’infini, gb − ge = O(r−4 

> b

). Le lemme 4.42 est valable avec l’opérateur ¯Pb plutôt que l’opérateur Pb grâce au théorème 4.51 dans le cas où ( Mo, g o) = ( N, g b) est un orbifold Ricci-plat ALE.. Il existe donc h′ ∈ C2,α β (gb) tel que ¯Pb(χH 2 + h′) + λg b = ∑ 

> i

λioi avec 

λi = −

∫

> S3/Γ

(

3〈H2, O 4 

> i

〉ge + 12O4

> i

(

∇etr eH2, ∂ re

)) 

dvS3/Γ, (5.6) où O4 

> i

est le terme d’ordre −4 du développement de oi à l’infini. En effet, par intégration par parties, en utilisant le fait que tr boi = 〈gb, oj 〉gb = 0 et δboi = 0, nous obtenons, 

〈 ¯Pb(χH 2), oj 〉L2 = 12 lim 

> ρ→∞

∫

> rb6ρ

〈∇ ∗ 

> b

∇b(χH 2) − ∇ 2 

> b

tr b(χH 2), oj 〉gb dvgb

= 12 lim 

> ρ→∞

∫

> rb=ρ

(

〈χH 2, ∇noj 〉gb − 〈∇ n(χH 2), oj 〉gb

+ oj (∇btr bχH 2, ∂ rb ))

dSρ

= −

∫

> S3/Γ

(

3〈H2, O 4 

> i

〉ge + 12O4

> i

(

∇etr eH2, ∂ re

)) 

dvS3/Γ.

Les valeurs de λi de (5.6) assurent donc bien que l’on ait ¯Pb(χH 2) + λg b − ∑

> i

λioi ⊥gb O(gb).

Remarque 5.4 . Le fait que l’on ne puisse pas résoudre Pb(h2) = Λ gb est la raison profonde pour laquelle certains orbifolds ne peuvent pas être désingularisés par 2. Obstruction en un des points singuliers 185 des variétés d’Einstein. La quantité ∫

> S3/Γ

〈H2, O 4 

> i

〉ge dvS3/Γ peut être vue comme un produit scalaire du polynôme homogène harmonique quadratique 2, H(i)2 , tel que 

O4 

> i

= H(i)2

> r6
> e

avec H2.

Remarque 5.5 . Dans le cas où H2 n’est pas en jauge de Bianchi et ne satisfait donc que de Ric( H2) = Λ ge, en adaptant [Biq13, Proposition 3.1] on peut aussi résoudre 

dgb Ric( h2) = Λ gb + ∑ 

> i

λio4 

> i

, avec 

λi = −

> ∫
> S3/Γ
> (

3〈H2, O 4 

> i

〉ge + O4

> i
> (

BeH2, ∂ re

> ))

dvS3/Γ.

L’intérêt est que l’on peut alors mettre les termes quadratiques de la métrique d’Einstein dans des jauges plus pratiques que la jauge de Bianchi suivant les si-tuations. 

2.2 Contrôle de l’opérateur d’Einstein modulo obstructions 

On remarque alors que gb + th 2 est bien une métrique sur une boule de rayon de l’ordre t− 12 . En particulier, pour t suffisamment petit, c’est une métrique sur la boule de rayon t− 14 , et on peut recoller cette métrique (plutôt que de recoller naïvement la métrique ALE) à la métrique orbifold exactement comme dans la définition 3.3 des désingularisations naïves. La métrique obtenue sera appelée approximation d’Einstein modulo obstruc-tions , et on la notera gA = gAϕ,t . Elle dépend elle aussi de choix de jauge au niveau des recollements et des paramètres d’échelle. Le principal avantage de cette construction, et la raison pour laquelle elle est appelée approximation est le meilleur contrôle suivant. 

Proposition 5.6 (Adaptation de [Biq13, Lemme 5.2]) . Soit (N, g b, p ) un orbifold Ricci-plat ALE, et H2 le terme quadratique d’une métrique orbifold d’Einstein go

asymptotique au même cône que (N, g b, p ), et soient h2 un 2-tenseur sur N et λi

les réels obtenus par la proposition 5.3 ou la remarque 5.5 à partir de H2.En notant gtb := gb + th 2 sur Bgb (p, t − 14 ) pour t > 0 suffisamment petit, on a le contrôle suivant de l’opérateur d’Einstein, pour p ∈ N , pour tout k ∈ N, il existe 

Ck > 0 telle que : 

(1 + rb)2+ k

> ∣∣∣∣

∇kgtb

> (

Ric( gtb) − R( gtb)2 gtb + tλg tb + δtgb δ∗ 

> gb

gtb + t ∑

> i

λio4

> i
> )∣ ∣∣∣gb

6 Ckt2(1 + rb)4.186 Chapitre 5. Obstructions à la désingularisation 

Remarque 5.7 . Les différents choix de h2 dans la proposition 5.3 ne changent que la constante devant t2(1 + rb)4 dans l’estimation. 

Remarque 5.8 . Pour rb >> 1, t2(1 + rb)4 vaut approximativement ( √tr b)4 = r4 

> o

.C’est cohérent avec l’erreur venant des termes quadratiques de la courbure de Ricci sur l’orbifold. Ces contrôles se répercutent sur les métriques d’approximation gA.

Corollaire 5.9. Soit (M, g D) une désingularisation naïve d’un orbifold d’Einstein 

(Mo, g o) par des variétés Ricci-plates ALE (Nj , g bj ) aux échelles tj > 0, et soit (oij )i

une base orthonormée de O4(gbj ).Soit gA = gAϕ,t une métrique d’approximation d’Einstein modulo obstructions et β > 0. Alors, on a le contrôle suivant pour tmax > 0 suffisamment petit, pour tout k ∈ N il existe Ck > 0 telle qu’on ait : 

> ∥∥∥

π ˜O(gD )⊥ ΦgD (gA)∥∥∥r−2    

> DCkβ(gD)

6 Ckt3−β 

> 4
> max

, (5.7) 

et, ∥∥∥∥π ˜O(gD )ΦgD (gA) − ∑

> j

tj

> ∑
> i

λji ˜oij,t  

> ∥∥∥∥L2(gD)

6 C0t32

> max

. (5.8) 

Et la métrique gA satisfait les conditions suivantes, 1. ‖gA − gD‖C2,α β, ∗ (gD ) 6 2ε,2. gA − gD est orthogonal à ˜O(gD) pour le produit L2 de gD,Démonstration. Traitons le cas du recollement d’une variété ( N, g b) à l’échelle 

t > 0, le cas général s’obtient en itérant les désingularisations car les contrôles nécessaires sont locaux. Sur M 16 to , nous avons par hypothèse Ric( go) = Λ go, (5.9) et sur N 16 tj , d’après la proposition 5.6, nous avons Ric( gtb) − R( gtb)2 gtb + tλg tb + δtgb δ∗ 

> gb

gtb + t ∑

> i

λio4 

> i

= O(tr 2 

> b

). (5.10) Maintenant, au point p, le développement de go en coordonnées géodésiques est 

go = ge + H2 + O(r3 

> o

), (5.11) et t(gb+th 2) a le développement suivant pour t− 14 6 rb 6 t− 14 d’après la proposition 2. Obstruction en un des points singuliers 187 5.3 

t(gb + th 2) = ge + H2 + O(t2r−2 

> b

+ tr −4 

> b

), (5.12) avec les contrôles adaptés pour les dérivées jusqu’à l’ordre 2. Nous contrôlons donc le recollement sur l’anneau de rayons rD = t14 et rD = 2 t14 qui est en 

O(t2(√tr D)−2 + t(√tr D)−4 + r3

> D

) = O(t34 ), puis par définition des normes à poids nous avons 

‖ΦgD (gA) − t ∑

> i

λi ˜oi‖r−2    

> DC2,α β(gD)

6 Ct 3−β 

> 4

. (5.13) La seconde inégalité s’obtient en intégrant l’inégalité de la proposition 5.6 contre les ˜ oi, pour tout o ∈ O(gb), nous avons alors 

> ∣∣∣∣〈

ΦgD (gA) − t ∑

> i

λi ˜oi, ˜o 

> 〉
> gD
> ∣∣∣∣

6 C‖˜o‖L2(gD )t32 . (5.14) 

Remarque 5.10 . Le contrôle (5.7) est faible et ne “voit” en particulier pas le terme  

> ∑
> j

tj 

> ∑
> i

λji ˜oij,t qui est de l’ordre de tmax en norme r−2 

> D

Ckβ (gD). Le second contrôle “voit” le conoyau pour les j tels que t32 

> max

 tj .

Remarque 5.11 . Avec la désingularisation naïve d’un orbifold Ricci-plat, nous avons seulement le contrôle suivant : 

‖ Ric( gD) − ΛgD‖r−2    

> DCkβ(gD)

6 C′

> k

t12 − β 

> 4
> max

,

et donc seulement ‖Ψ( gD)‖r−2    

> DCkβ(gD)

6 C′

> k

t12 − β

> 4
> max

2.3 Une première obstruction 

Nous pouvons maintenant utiliser a proposition 5.1 appliquée à la métrique gA

ci-dessus. Avec les contrôles du corollaire 5.9. Nous obtenons le résultat d’obstruc-tion suivant. 

Corollaire 5.12. Soit (Mo, g o) un orbifold d’Einstein ayant une seule singularité et (N, g b) une variété Ricci-plate ALE. Alors, si l’on note H2 les termes quadratiques du développement de go en coor-données géodésiques, et (O4 

> j

)j une base de O4(gb), l’espace des termes homogènes en r−4 

> b

asymptotiques des O(gb), il est impossible de perturber gD en une métrique 188 Chapitre 5. Obstructions à la désingularisation 

d’Einstein en jauge divergence réduite orthogonalement à ˜O(gD) si 

> ∫
> S3
> (

3〈H2, O 4 

> j

〉 + O4 

> j

(BeH2, ∂ re ))

dvS3 6 = 0 .

2.4 Une question d’intégrabilité 

Nous avons donc montré que l’on pouvait construire de meilleures approxi-mations d’Einstein à l’aide d’une métrique Ricci-plate ALE fixée. Cependant, le théorème 3.42 ne dit rien sur la vitesse d’apparition (la constante εi du théorème 3.42) de cette variété Ricci-plate ALE. Comme dans le théorème 4.51, pour en tenir compte, nous devons fixer une jauge de projection v ∈ ˜O(gD) sur le noyau de la linéarisation de la courbure de Ricci sur la variété Ricci-plate ALE. Pour ne pas endommager les contrôles de la proposition 5.6, il ne suffit pas d’ajouter une déformation du noyau et nous allons devoir supposer que les dé-formations que l’on considère sont intégrables pour se ramener au cas v = 0, adapter la proposition 5.1 à notre nouveau cadre, et utiliser les estimations de la proposition 5.6. 

Remarque 5.13 . L’estimation [Biq13, (61)] est incorrecte mais le résultat principal de [Biq13] reste vrai comme nous le verrons dans la suite de cette partie car la métrique d’Eguchi-Hanson n’a que des déformations intégrables. Cela signifie tout de même qu’il ne suffit pas d’ajouter des éléments du noyau approché. 

Définition 5.14 (Variété Ricci-plate ALE à déformations intégrables) . On dira qu’une métrique Ricci-plate ALE gb n’a que des déformations intégrables si pour tout v ∈ O(gb) suffisamment petit, il existe une métrique Ricci-plate ALE ¯ gb,v 

satisfaisant ¯ gb,v − (gb + v) ⊥ O(gb) et ‖¯gb,v − gb‖L2(gb) 6 2‖v‖L2 , et telle que 

δgb ¯gb,v = 0. 

Remarque 5.15 . Toutes les déformations infinitésimales L2 d’orbifolds Ricci-plats ALE sont automatiquement à divergence nulle et à trace nulle. En effet, pour un tel orbifold ( M, g b) Ricci-plat, on a δgb Pgb = 12 ∇∗ 

> gb

∇gb δgb , et tr gb Pgb = 12 ∇∗ 

> gb

∇gb tr gb .Ainsi, si Pgb h = 0 et h = O(r−δb ) pour un δ > 0, alors δgb h = 0, et tr gb h = 0 par le principe du maximum. 

Remarque 5.16 . D’après [Koi83, Corollary 3.5] si pour tout v ∈ O(gb), il existe (gt)t∈[−1,1] une courbe de métriques Ricci-plates ALE dans les mêmes coordonnées que gb, telle que ∂tgt|t=0 = v, alors gb est à déformations intégrables. 

Remarque 5.17 . Tous les exemples connus d’espaces Ricci-plats ALE n’ont que des déformations intégrables car ce sont des quotients d’espaces hyperkählériens. 2. Obstruction en un des points singuliers 189 

2.4.1 Espaces de Hölder à poids et développements asymptotiques des métriques Ricci-plates ALE 

Introduisons encore de nouveaux espaces à poids qui nous permettront de contrôler les termes asymptotiques de nos métriques ALE. Le contrôle de ces termes asymptotiques sera crucial pour obtenir des résultats d’obstructions dans la suite du chapitre. 

Définition 5.18 (Norme C2,α β, ∗∗ sur un orbifold ALE) . Soit ( N, g b) un orbifold ALE, soit h un 2-tenseur sur N , et supposons que h = H4 + O(r−4−βb ) pour β > 0. Pour χ, une fonction de coupure à support dans un voisinage de l’infini où gb ades coordonnées ALE, on définit sa norme C2,α β, ∗∗ par 

‖h‖C2,α β, ∗∗ 

:= sup r4 

> b

|H4|ge + ∥∥∥(1 + rb)4(h − χH 4)∥∥∥C2,α β, ∗

.

Cette définition est motivée par le lemme suivant. 

Lemme 5.19. Soit (N, g b) un orbifold ALE. Alors, il existe C > 0 telle que l’on ait, pour tout h ∈ C2,α β, ∗ , h ⊥ O(gb),

‖h‖C2,α β, ∗∗ 

6 C‖(1 + rb)4 ¯Pgb h‖r−2 

> bCαβ

. (5.15) 

Démonstration. D’après la théorie des opérateurs elliptiques entre espaces de Höl-der à poids, l’opérateur ¯Pgb : (1 + rb)−4C2,α  

> −β

→ (1 + rb)−4r−2 

> b

Cα 

> −β

est Fredholm de noyau O(gb) et conoyau O(gb) car il n’y a pas de poids critique autre que 0 entre 2 et −4. Cela implique que ¯Pgb : (1+ rb)−4C2,α  

> −β

∩O(gb)⊥ → (1+ rb)−4r−2 

> b

Cα 

> −β

∩O(gb)⊥

est inversible avec un inverse borné. De plus, nous avons ¯P −1

> gb
> (

(1 + rb)−4r−2 

> b

Cαβ

> )

= C2,α β, ∗∗ car −4 est le premier poids critique négatif de ¯P en jauge divergence, et le résultat énoncé vient alors du fait que l’inverse est borné. En particulier, l’analyse du théorème 4.51 s’étend au cas où ( Mo, g o) est un or-bifold Ricci-plat ALE et où la norme C2,α β, ∗ (go) est remplacée par la norme C2,α β, ∗∗ (go). En effet, tous les contrôles sont locaux au voisinage des points singuliers ou venant des estimations sur l’inverse de l’opérateur sur le reste de la variété exactement comme ceux de (5.15). Nous en déduisons le contrôle suivant sur les termes asymp-totiques des ALE. 

Corollaire 5.20. Soit (N, g b) un orbifold Ricci-plat ALE et notons (N B , g Bt ) une désingularisation naïve de (N, g b) par un arbre d’orbifolds Ricci-plats ALE recollés suivant une configuration B avec des échelles relatives t.190 Chapitre 5. Obstructions à la désingularisation 

Soit ¯gt,v l’unique métrique (d’après le théorème 4.51) satisfaisant, pour ε > 0

suffisamment petit : 1. ‖gBt − ¯gt,v ‖C2,α β, ∗ (gBt ) < 2ε,2. (gBt + v) − ¯gt,v est L2(gBt )-orthogonal à ˜O(gBt ), et 3. π ˜O(gBt )⊥ ΦgBt (¯ gt,v ) = 0 .Alors, pour tout 0 < β < 1, nous avons ¯gt,v = ge + ¯H4 

> v

+ O(r−4−βB ) pour ¯H4

> v

homogène en r−4 

> e

. Il existe aussi δ > 0 tel que pour toute métrique g sur N B

satisfaisant g − (gBt + v) ⊥ ˜O(gBt ), et ‖(1 + rB )4π ˜O(gBt )⊥ ΦgBt (g)‖r−2    

> BCαβ(gBt)

< ε nous ayons le développement g = ge + H4 + O(r−4−βB ) pour ¯H4 

> v

homogène en r−4 

> e

et 

r4 

> B

|H4 − ˆH4 

> v

|gBt 6 C‖(1 + rb)4π ˜O(gBt )⊥ ΦgBt (g)‖r−2   

> BCαβ(gBt)

.

2.4.2 Une nouvelle désingularisation naïve 

Dans le cas où ( Mo, g o) est une variété Ricci-plate ALE, et qu’il n’y a donc pas de désingularisation à considérer, le théorème 4.51 se réécrit de la manière suivante. 

Corollaire 5.21. Soit (N, g b) une variété Ricci-plate ALE. Alors, il existe ε > 0

tel que pour tout v ∈ O(gb), ‖v‖C2,α β, ∗ (gb) < ε , il existe une unique métrique ¯gb,v 

satisfaisant : 1. Φgb (¯ gb,v ) ∈ O(gb),2. ‖gb − ¯gb,v ‖C2,α β, ∗ (gb) < 2ε,3. (gb + v) − ¯gb,v est orthogonal à O(gb) pour le produit L2 de gb.Il existe de plus C > 0 ne dépendant que de gb tel qu’on ait 

‖(gb + v) − ¯gb,v ‖C2,α β, ∗ (gb) 6 C‖v‖2

> C2,α β, ∗∗ (gb)

,

ce qui implique le contrôle suivant 

¯gb,v = gb + v + O(‖v‖2 

> C2,α β, ∗(gb)

(1 + rb)−4). (5.16) 

Démonstration. La première partie de l’énoncé est une conséquence directe du théorème 4.51. pour la seconde partie, on a ‖(1+ rb)4πO(gb)⊥ Φgb (gb +v)‖Cαβ (gb)( gb) <C‖v‖2

> C2,α β, ∗

car ‖v‖C2,α β, ∗∗ 

∼ ‖ v‖C2,α β, ∗

(v décroît comme r−4 

> b

à l’infini d’après le lemme 4.41) et car par définition πO(gb)⊥ dgb Φgb (v) = 0. Ainsi, d’après le corollaire 5.20, nous avons (5.16). 2. Obstruction en un des points singuliers 191 Sur un orbifold d’Einstein non désingularisé, le théorème 4.51 (voir aussi le théorème 5.40 dans la suite) se réécrit de la manière suivante. 

Proposition 5.22. Soit (Mo, g o) une variété Ricci-plate ALE. Alors, il existe 

ε > 0 tel que pour tout v ∈ O(go), ‖v‖C2,α β, ∗ (go) < ε , il existe une unique métrique 

¯go,v satisfaisant : 1. Ric(¯ go,v ) − R(¯ go,v )2 ¯go,v + λ¯go,v + δ∗ 

> ¯go,v

δgo ¯go,v = oo ∈ O(go),2. ‖go − ¯go,v ‖C2,α β, ∗ (gb) < 2ε,3. (go + v) − ¯go,v est orthogonal à O(go) pour le produit L2 de go.Il existe de plus C > 0 ne dépendant que de gb tel qu’on ait 

‖(go + v) − ¯go,v ‖C2,α β, ∗ (go) 6 C‖v‖2 

> C2,α β, ∗(gb)

.

Étant donnés v ∈ ˜O(gD) et t = ( tj )j , nous définissons alors ¯ gDv comme le recollement naïf (définition 3.3) de ¯ go,v o avec les tj ¯gbj ,v j pour vo ∈ O(go) et vj ∈

O(gbj ) satisfaisant ¯gDv − (gD + v) ⊥ ˜O(gD).

Remarquons alors que si les orbifolds Ricci-plats ALE ( Nj , g bj ) n’ont que des déformations intégrables, ¯ gDv est bien un recollement de variétés Ricci-plates ALE exactement comme celui de la définition 3.3, mais cette fois à la métrique ¯ go,v o (qui n’est pas nécessairement d’Einstein). On obtient alors comme dans la proposition 5.1 un résultat d’obstruction, mais seulement contre les coupures des déformations des ¯ gbj ,v j .Définissons, pour v ∈ ˜O(gD) l’ensemble ˜OB (¯ gDv ) ⊂ ˜O(¯ gDv ) des troncatures (comme dans la définition 4.44) des éléments des O(¯ gbj ,v j ) seuls. Nous avons alors les propriétés suivantes pour ¯ gDv .1. ‖gD − ¯gDv ‖C2,α β, ∗ (gD ) 6 2ε,2. les métriques sont en jauge par rapport à gD + v,¯gDv − (gD + v) ⊥ ˜O(gD),

3. Notre opérateur Ψ = π ˜O(gD )⊥ Φ est contrôlé indépendamment de v,

‖Ψ(¯ gDv )‖r−2    

> DCαβ(gD)

6 Ct 2−β 

> 4
> max

, (5.17) 192 Chapitre 5. Obstructions à la désingularisation 4. pour tout h ∈ C2,α β, ∗ et oBv ∈ ˜OB (¯ gDv ), 

∣∣∣〈 ¯P¯gDv h, oBv

〉∣ ∣∣ 6 Ct 12 ‖h‖C2,α β, ∗

‖oBv ‖L2(¯ gDv ). (5.18) 

Remarque 5.23 . La dernière estimation (5.18) se montre exactement comme le lemme 4.46. En utilisant le contrôle (5.18) pour remplacer (5.3) dans la preuve de la pro-position 5.1, nous pouvons remplacer gDt + v par ¯ gDt,v proposition 5.1 et obtenir un contrôle valable pour v 6 = 0 aussi. 

Proposition 5.24. Soit 0 < α < 1, et (M, g D) une désingularisation naïve de 

(Mo, g o) par des variétés Ricci-plates ALE, (Nj , g bj )j . Soit alors v ∈ O(gD) et soit ˆgv := ˆ gϕ,t,v l’unique métrique d’Einstein modulo obstructions proche de gD

satisfaisant : 1. ‖ˆgv − gD‖C2,α β, ∗ (gD ) 6 2ε,2. ˆgv − (gD + v) est orthogonal à ˜O(gD) pour le produit L2 de gD,obtenue par le théorème 4.51. Supposons que ˆgv soit d’Einstein. Soit gAv une métrique satisfaisant : 1. ‖gAv − gD‖C2,α β, ∗ (gD ) 6 2ε,2. gAv − (gD + v) est orthogonal à ˜O(gD) pour le produit L2 de gD,alors, en notant Ψ( gAv ) = π ˜O(gD )⊥ ΦgD (gAv ), on a 

‖ˆgv − gAv ‖C2,α β, ∗ (gD ) 6 C∥∥∥Ψ( gAv )∥∥∥r−2   

> DCαβ(gD)

, (5.19) 

et si l’on note oBv := π ˜OB (¯ gDv )ΦgD (gAv ), on a 

‖oBv ‖L2(gD ) 6

(

‖Ψ( gAv )‖r−2    

> DCαβ(gD)

+ ‖Ψ(¯ gDv )‖r−2   

> DCαβ(gD)

+ t12

> max

)

‖Ψ( gAv )‖r−2   

> DCαβ(gD)

. (5.20) 

2.4.3 Une meilleure approximation de métrique d’Einstein modulo obstructions 

Soit vo ∈ O(go) et ¯H2 les termes quadratiques du développement de ¯ go,v o dans des coordonnées locales où elle est en jauge divergence par rapport à ge autour d’un point singulier p où nous avons donc ¯ go,v o = ge + ¯H2 + O(r3 

> e

), et où l’on sait que Φgo (¯ go,v o ) = oo = Oo + O(r2 

> e

) avec tr ge Oo = 0 et δge Oo = 0. 2. Obstruction en un des points singuliers 193 En développant en ge, grâce aux formules du début de la preuve du théorème 4.51 pour ¯Pgo = dgo Φgo , nous avons pour λ = R(¯ go,vo )4

0 = Φgo (¯ go,v o ) − Oo = λg e + ¯Pe( ¯H2) − Oo + O(r2 

> e

)= λg e + 12

> (

∇∗

> e

∇e ¯H2 − ∇ 2

> e

tr e ¯H2 + (∆ etr e ¯H2)ge

> )

− Oo + O(r2 

> e

) (5.21) 

Proposition 5.25. Soit (N, g b) un orbifold Ricci-plat ALE asymptotique à R4/Γ

et ¯H2 un 2-tenseur homogène quadratique à divergence nulle sur R4/Γ, λ ∈ R et 

Oo un 2-tenseur constant sur R4/Γ tels qu’on ait : 

¯Pe ¯H2 + λg e = Oo.

Alors, il existe un 2-tenseur ¯h2, et des réels ¯λi tels que (¯h2, ¯λi) soit une solution de 

¯Pb¯h2 + λg b = χOo + ∑

> i

¯λioi,

|¯h2 − χ ¯H2|gb = O(r−2 

> b

),

où χ est une fonction de coupure à support dans un voisinage de l’infini de (N, g b)

où les coordonnées ALE sont définies et où 

¯λi := −

> ∫
> S3/Γ
> (

3〈 ¯H2, O 4 

> i

〉ge + O4

> i
> (

∇etr e ¯H2, ∂ re

> ))

dvS3/Γ +

> ∫
> N

χ〈Oo, oi〉gb dvb.

L’ensemble des solutions est en fait (¯h2 + O(gb), ¯λi).Démonstration. Nous avons ¯Pb(χ ¯H2) + λg b − χOo ∈ r−2 

> b

Cαβ (gb) pour 0 < β < 1car dans un voisinage de l’infini, gb − ge = O(r−4 

> b

). Le lemme 4.42 est valable avec l’opérateur ¯Pb plutôt que l’opérateur Pb grâce au théorème 4.51 dans le cas où ( Mo, g o) = ( N, g b) est un orbifold Ricci-plat ALE. Il existe donc ¯h′ ∈ C2,α β (gb) tel que ¯Pb(χ ¯H2 + ¯h′) + λg b = χOo + ∑ 

> i

¯λioi avec ¯λi = −

> ∫
> S3/Γ
> (

3〈 ¯H2, O 4 

> i

〉ge + 12O4

> i
> (

∇etr e ¯H2, ∂ re

> ))

dvS3/Γ +

> ∫
> N

χ〈Oo, oi〉gb dvb, (5.22) où O4 

> i

est le terme d’ordre −4 du développement de oi à l’infini. En effet, par intégration par parties, en utilisant le fait que tr boi = 〈gb, oj 〉gb = 0 et δboi = 0, 194 Chapitre 5. Obstructions à la désingularisation nous obtenons, 

〈 ¯Pb(χ ¯H2), oj 〉L2 = 12 lim ρ→∞ 

∫

> rb6ρ

〈∇ ∗ 

> b

∇bχ ¯H2 − ∇ 2 

> b

tr bχ ¯H2, oj 〉gb dvgb

= 12 lim ρ→∞ 

∫

> rb=ρ

(

〈χ ¯H2, ∇noj 〉gb − 〈∇ n(χ ¯H2), oj 〉gb

+ oj (∇btr bχ ¯H2, ∂ rb ))

dSρ

= −

∫

> S3/Γ

(

3〈 ¯H2, O 4 

> i

〉ge + 12O4

> i

(

∇etr e ¯H2, ∂ re

)) 

dvS3/Γ.

Maintenant, l’intégrale ∫ 

> N

χ〈Oo, oi〉gb dvb converge bien que 〈Oo, oi〉gb = O(r−4 

> b

)car dans des coordonnées ALE, r4 

> b

oi = ϕij dx idx j + O(r−1 

> b

), où les ϕij : S3 → R

sont des fonctions propres non constantes et ont donc des moyennes nulles. Ainsi, 

∫

> {rb=ρ}

〈Oo, oi〉gb dSρ = O(r−2 

> b

) et l’intégrale converge bien. Les valeurs de ¯λi de (5.22) assurent donc bien que l’on ait ¯Pb(χ ¯H2) + λg b − χOo − ∑

> i

¯λioi ⊥gb O(gb).

Maintenant, si l’on a une métrique d’Einstein (sans obstruction) nous retrou-vons l’obstruction indépendante de la jauge de la remarque 5.5 (voir la fin de la preuve de [Biq13, Proposition 3.1]). 

Corollaire 5.26. Soit H2 un 2-tenseur quadratique satisfaisant de Ric( H2) = Λ ge,et soit V un champ de vecteur dont les coefficients sont homogènes et en r3 

> e

et satisfont δeδ∗ 

> e

V = −δeH2, et définissons ¯H2 := H2 + δ∗ 

> e

V qui satisfait δe ¯H2 = 0 .Alors, nous avons 

¯λi = λi,

où 

¯λi := −

∫

> S3/Γ

(

3〈 ¯H2, O 4 

> i

〉ge + 12O4

> i

(

∇etr e ¯H2, ∂ re

))

dvS3/Γ,

et 

λi := −

∫

> S3/Γ

(

3〈H2, O 4 

> i

〉ge + O4

> i

(

BeH2, ∂ re

)) 

dvS3/Γ

Soit ( Mo, g o) un orbifold d’Einstein et v ∈ ˜O(gD). Nous définissons alors ¯ gAv

comme le recollement naïf (définition 3.3) de ¯ go,v o avec les tj

(

¯gbj ,v j + tj ¯hj

> 2

)

pour 

vo ∈ O(go) et vj ∈ O(gbj ) et ¯hj 

> 2

asymptotique à ¯Hj 

> 2

et tel que ¯P¯gbj ,v j

¯hj 

> 2

+ λ¯gbj ,v j =

χOo, où ¯Hj 

> 2

sont les termes quadratiques du développement de ¯ go,v o dans des coordonnées locales où elle est en jauge divergence par rapport à ge autour de 2. Obstruction en un des points singuliers 195 chaque point singulier pj satisfaisant ¯ gDv − (gD + v) ⊥ ˜O(gD), et χN tj

¯hj 

> 2

⊥ ˜O(gD).

Nous avons les contrôles suivants. 

Corollaire 5.27. Soient 0 < β < 1, (M, g D) une désingularisation naïve d’un orbifold d’Einstein (Mo, g o) par des variétés Ricci-plates ALE (Nj , g bj ) dont les déformations infinitésimales L2 sont intégrables. Notons de plus (oij )i une base orthonormée de O(gbj ).Alors, il existe des réels ¯λji pour lesquels on a le contrôle suivant : pour tmax > 0

suffisamment petit, pour tout k ∈ N il existe Ck > 0, tel que 

> ∥∥∥

π ˜O(gD )⊥ ΦgD (¯ gA)∥∥∥r−2    

> DCkβ(gD)

6 Ckt3−β 

> 4
> max

, (5.23) 

et pour tout i0 et j0, on ait en notant ˜oij la coupure de oij sur M (voir définition 4.44), 〈

ΦgD (¯ gA) − ∑

> j

tj

> ∑
> i

¯λji ˜oij , ˜oi0 

> j0
> 〉
> L2(gD)

6 C0t32

> max

. (5.24) 

Tout en satisfaisant, 1. ‖¯gA − gD‖C2,α β, ∗ (gD ) 6 2ε,2. ¯gA − gD est L2(gD)-orthogonal à ˜O(gD).Démonstration. Traitons encore une fois le recollement en un point singulier p et à l’échelle t > 0 d’une bulle ( N, g b) car l’estimation est locale. Nous noterons ¯H2

les termes quadratiques du développement de ¯ go,v o au point p en jauge divergence par rapport à ge, et ¯h2 le 2-tenseur obtenu par la proposition 5.25 satisfaisant 

χN tj

¯hj 

> 2

⊥ ˜O(gD). Sur M 16 to , nous avons par hypothèse 

Φgo (¯ go,v o ) = oo ∈ O(go), (5.25) et sur N 16 t, nous avons 

Φgb (t(gb + t¯h2)) = χOo + t ∑

> i

¯λioi + O(r2

> D

). (5.26) Maintenant, au point p, le développement de ¯ go,v o dans des coordonnées locales où elle est en jauge divergence par rapport à ge est ¯go,v o = ge + ¯H2 + O(r3 

> o

), (5.27) 196 Chapitre 5. Obstructions à la désingularisation le développement de oo en p est 

oo = Oo + O(r2 

> o

).

De même, t(gb + t¯h2) a le développement suivant pour t− 14 6 rb 6 t− 14

t(gb + t¯h2) = ge + ¯H2 + O(t2r−2 

> b

+ tr −4 

> b

), (5.28) avec les contrôles adaptés pour les dérivées jusqu’à l’ordre 2. Nous avons finalement sur l’anneau de rayons rD = t14 et rD = 2 t14 ,

ΦgD (¯ gA) − ˜oo − t ∑

> i

¯λi ˜oi = O(

t34

)

. (5.29) D’après (5.25), (5.26) et (5.29) appliqués à toutes les singularités, nous avons l’estimation (5.23). Enfin, grâce à (5.26) appliqué à toutes les singularités, nous avons (5.24). 

Lemme 5.28. Soient ¯λji (v) les réels du corollaire 5.27 précédent pour le recolle-ment de métriques (Nj , ¯gbj ,v j ) plutôt que (Nj , g bj ). Nous avons le contrôle suivant, 

|¯λji (v) − ¯λji (0) | 6 C(

‖v‖C00 (gD ) + ‖ ¯H2‖C02 (go)

)

‖v‖C00 (gD ). (5.30) 

Démonstration. Nous cherchons à contrôler les variations de ¯λi = −

∫

> S3/Γ

(

3〈 ¯H2, O 4 

> i

〉ge + O4

> i

(

∇etr e ¯H2, ∂ re

)) 

dvS3/Γ +

∫

> N

χ〈Oo, oi〉gb dvb

en fonction de v = ˜ vo + ˜ vj .Pour ¯H2(0) et ¯H2(vo), les termes quadratiques des développements de go et ¯go,v o , nous avons 

‖ ¯H2(0) − ¯H2(vo)‖C02 (ge) 6 C‖vo‖C0(go) (5.31) et, 

|Oo|ge 6 C‖vo‖C0(go) (5.32) d’après le théorème 5.40 qui est énoncé dans la suite, mais qui est une conséquence directe du théorème 4.51 ne reposant que sur le fait que l’analyse sur un orbifold peut se faire sans poids à leurs points singuliers en considérant des revêtements locaux à ses points singuliers. D’après le corollaire 5.21 précédent, pour vj ∈ O(gbj ) suffisamment petit, nous avons ¯gbj ,v j = gbj + vj + O(‖vj ‖2  

> C2,α β, ∗(gbj)

(1 + rbj )−4). (5.33) 2. Obstruction en un des points singuliers 197 Cela implique que les termes d’ordre −4 des déformations infinitésimales de ¯ gbj ,v j

sont proches de ceux des déformations infinitésimales de gbj et que leurs différences sont de l’ordre de O(‖vj ‖C2,α β, ∗ (gbj )). On en déduit donc que 

|¯λji (v) − ¯λji (0) | 6 C(

‖v‖C00 (gD ) + ‖ ¯H2‖C02 (go)

> )

‖v‖C0(gD ).

Remarque 5.29 . En supposant que O(go) = 0, on peut en réalité être un peu plus précis dans l’expression de la différence ¯λi(v) − ¯λi(0) en revenant à leur obtention par intégration par parties, sur ( N, g b) dans la proposition 5.25. Nous obtenons alors ¯λi(v) − ¯λi(0) = 〈 ¯Q(2)  

> gb

(v, h 2) − λv, oi

> 〉

+ O(‖v‖2 

> C0

), où ¯Q(l) 

> gb

sont les termes 

l-linéaires du développement de Φgb en gb.

Remarque 5.30 . La différence entre ¯λi(v) et ¯λi(0) devient alors assez explicite dans le cas où gb est hyperkählérien. Dans la proposition 4 de [Biq17], le terme ¯Q(2)  

> gb

(v, h 2) − λv est calculé dans le cas de la métrique d’Eguchi-Hanson en sup-posant que ¯λi(0) = 0. Dans le cas le moins dégénéré (où la partie autoduale de la courbure en p, R+(H2) est de rang 2 et Λ 6 = 0), la différence ¯λi(v) − ¯λi(0) = 

〈v, oi〉(

oi(R+(H2)) − Λoi

> )

ne s’annule jamais pour v 6 = 0. 

Remarque 5.31 . Dans le cas où il existe des déformations infinitésimales non in-tégrables de gb, on ne peut plus espérer voir d’obstructions par les méthodes pré-cédentes. En effet, la métrique se développe en ¯ gb,v = gb + v + w + O(|v|3), où w

satisfait : ¯Q(2)  

> gb

(v, v ) + ¯Pgb (w) = πO(gb) ¯Q(2)  

> gb

(v, v ) ∈ O(gb),

et on a potentiellement πO(gb) ¯Q(2)  

> gb

(v, v ) = O(|v|2) si v n’est pas une déformation intégrable. D’autre part, en considérant la métrique ¯ gtb,v := 1 

> t

¯gAv , on a le dévelop-pement suivant de Φgb sur N 16 t,

Φgb (¯ gtb,v ) = Φgb (¯ gb,v ) + t ¯Pb(¯h2) + tQ (2)  

> gb

(v, h 2) + O(t2).

Avant l’ordre t2 il y a donc trois premières sources d’obstructions : 1. la projection de Φgb (¯ gb,v ) = O(|v|2) sur O(gb), 2. la projection de tP b(h2) = O(t) sur O(gb), et 3. la projection de tQ (2)  

> gb

(v, h 2) = O(t|v|) sur O(gb). Il n’y a alors que si Ric(¯ gb,v ) = 0, ou si |v|  t que l’on peut espérer voir les obstructions d’ordre t qui sont celles qui nous intéressent. 198 Chapitre 5. Obstructions à la désingularisation 

Corollaire 5.32. Soit (Mo, g o) un orbifold d’Einstein, et (Mi, g i)i une suite de va-riétés d’Einstein convergeant vers (Mo, g o) au sens de Gromov-Hausdorff et telle que les éclatements non triviaux au point singulier apparaissant le plus lentement (c’est-à-dire qui a la courbure la plus basse) converge vers (N, g b), une variété 

(c’est-à-dire sans formation d’arbre de singularités) Ricci-plate ALE dont les dé-formations infinitésimales sont intégrables .Alors, si l’on note H2 les termes quadratiques du développement de go en co-ordonnées géodésiques, et (O4 

> j

)j une base de O4(gb), on a : 

∫

> S3

(

3〈H2, O 4 

> j

〉 + O4 

> j

(BeH2, ∂ re ))

dvS3 = 0 .

Démonstration. Soit ( Mo, g o) un orbifold d’Einstein, et supposons qu’il existe une suite de métriques d’Einstein ( Mi, g i)i convergeant vers ( Mo, g o) au sens de Gromov-Hausdorff. D’après le corollaire 4.40, il existe une sous-suite toujours no-tée ( Mi, g i)i telle que pour i assez grand, il existe une désingularisation naïve (M, g Dti ), et vi ∈ ˜O(gDti ) avec vi → 0 et un difféomorphisme ϕi : M → M tel que 

ϕ∗ 

> i

gi = ˆ gti,v i , où ˆ gti,v i est la perturbation du théorème 4.51. Fixons alors k0 pour lequel tk0,i = tmax ,i . Quitte à prendre une sous-suite, on peut supposer que k0 est constant car il n’y a qu’un nombre fini de singularités. Supposons que l’orbifold Ricci-plat ALE apparaissant à la singularité pk0 soit lisse, et qu’il n’y ait donc pas d’arbre de singularités. D’après le corollaire 5.27, il existe une approximation ¯ gAti,v i satisfaisant 

‖π ˜O(gD )⊥ ΦgDti

(¯ gAti,v i )‖r−2   

> D,i Cαβ(gDti,v i)

6 Ct 3−β

> 4
> max ,i

,

et ∥∥∥∥oBi − ∑

> k

tk,i 

∑

> j

¯λkj (vi)˜ ojk,i,t i

∥∥∥∥L2

6 Ct 32

> max ,i

,

où ˜ ojk,i est une base orthonormée d’éléments de ˜ OB (¯ gDti,v i ) et où l’on a repris la notation oBi = π ˜OB (¯ gDti,v i )ΦgDti

(¯ gAti,v i ), et 1. ‖¯gAti,v i − gDti ‖C2,α β, ∗ (gDti ) 6 2ε,2. ¯ gAti,v i − (gDi + vi) est orthogonal à ˜ O(gDti ) pour le produit L2 de gDti .Utilisons la proposition 5.24. Avec les contrôles (5.17) et (5.23), l’estimation (5.20) pour 0 < β < 12 se réécrit 

tk,i |¯λkj (vi)| 6 C

(

t3−β 

> 4
> max ,i

+ t2−β

> 4
> max ,i

)

t3−β 

> 4
> max ,i

6 Ct 5−2β 

> 4
> max ,i

 tmax ,i . (5.34) 3. Obstruction à tous les points singuliers 199 Maintenant, nous savons que vi → 0, et d’après le lemme 5.28, cela implique que les ¯λkj (vi) tendent vers les ¯λkj (0). Les ¯λk0 