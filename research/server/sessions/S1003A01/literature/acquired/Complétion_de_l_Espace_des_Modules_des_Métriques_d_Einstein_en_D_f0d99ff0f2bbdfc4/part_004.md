---
retention_scope: session
part: 4
total_parts: 7
---

[Part 4/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

pour 2 ρ1 < s < (1+2 r0)2 ρ1. De plus pour 116 Chapitre 3. De Gromov-Hausdorff à C∞ à poids tout s, il existe une constante C = C(n, α ) > 0 telle qu’en rappelant la notation 

η(s) := Cε  

> (

ρ1

s

> )β1

+ 

> (

sρ2 

> )β2
> 

,

on ait les contrôles suivant a priori sur les ˜Σs :— le rayon d’injectivité normale de ˜Σs et le rayon d’injectivité des points de ˜Σs dans M sont minorés par 3 sr 0 d’après les lemmes 3.14 et 3.20, — H ˜Σ1 ≡ n−1 

> s

, et ‖A˜Σs 

> s

− g ˜Σs 

> s2

‖Cα < Cη (s), — sur l’anneau {x, d Mg (x, Σ) < 3sr 0}, on a ‖ Rm ‖C4(g) 6 Cη (s) 

> s2

.Nous pouvons donc une nouvelle fois utiliser la proposition 3.36 à partir de l’hy-persurface Σ 2(1+2 r0)ρ1 pour obtenir un feuilletage par des hypersurfaces à courbure moyenne constante égale à n−1 

> s

jusqu’à s = 2(1 + 2 r0)2ρ1. Encore une fois, les contrôles a priori de la proposition 3.24 de l’ordre de Cη (s) nous permettent d’ité-rer ce procédé et de construire des hypersurfaces à courbure moyenne constante jusqu’à s = 2(1 + 2 r0)kρ1 pour tout k tel que 2(1 + 2 r0)kρ1 < 12 ρ2 ce qui est le résultat énoncé. 

# 6 Construction de coordonnées et contrôle de la métrique 

Pour construire un difféomorphisme de la zone, nous allons nous appuyer sur une hypersurface où nos contrôles sont optimaux et suivre les lignes de gradient de la coordonnée s pour construire naturellement un difféomorphisme entre les hypersurfaces à courbure moyenne constante. 

6.1 Coordonnées basées sur le feuilletage 

Dans le feuilletage construit dans la proposition 3.39, il y a une hypersurface à courbure moyenne constante qui est mieux contrôlée que les autres à son échelle, c’est ˜Σ¯ρ où η(¯ ρ) = min ρ1<ρ<ρ 2 η(ρ), qui satisfait les propriétés suivantes par les propositions 2.34 et 3.24 : 1. il existe un difféomorphisme ϕ : Sn−1/Γ → ˜Σ¯ρ tel que : pour tout k ∈ N et 0 < α < 1, il existe C = C(k, α, n, r 0) > 0 pour laquelle, 

> ∥∥∥∥

ϕ∗g ˜Σ¯ρ

¯ρ2 − gSn/Γ

> ∥∥∥∥Ck,α (gSn/Γ)

< Cη (¯ ρ),6. Coordonnées optimales et contrôle de la métrique 117 2. pour tout k ∈ N et 0 < α < 1, il existe C = C(k, α, n ) > 0 telle que 

> ∥∥∥∥

A˜Σ¯ρ

¯ρ − g ˜Σ¯ρ

¯ρ2   

> ∥∥∥∥Ck,α
> (g˜Σ ¯ρ
> ¯ρ2
> )

6 Cη (¯ ρ).

3. pour tout k ∈ N, il existe C = C(k, n ) > 0 telle que sur l’anneau [ 12 ¯ρ, 2¯ ρ] on ait, ¯ρ2+ k∣∣∣∇k Rm ∣∣∣g 6 Cη (¯ ρ).

Nous définissons alors un difféomorphisme Φ : [ ρ1, ρ 2] × Sn−1/Γ → ˜A(ρ1, ρ 2) de la manière suivante : en ¯ ρ,Φ(¯ ρ, x ) = ϕ(x),

où ϕ est le difféomorphisme du point 1 précédent, et pour tout s ∈ [ρ1, ρ 2], 

∂sΦ( s, x ) = us(x)N ˜Σs

> (

(Φ( s, x ))

= −grad  

> (

1

s

> )

,

où us est telle que Φ( s, Sn−1/Γ) = ˜Σs. C’est un difféomorphisme sur son image car deux courbes suivant le flot donné par le champ de vecteurs −grad ( 1

> s
> )

, qui ne s’annule pas, ne peuvent pas se rencontrer si elles ne sont pas confondues. 

6.2 Expression de la métrique 

Dans de telles coordonnées, la métrique a la forme suivante, Φ∗g(s, x ) = us(x)2ds 2 + s2hs(x),

où hs est une métrique sur Sn−1/Γ. Prenons les notations suivantes pour la suite où l’on tirera toujours la situation en arrière sur Rn/Γ : — ϕs(x) = Φ( s, x ), ce qui implique que s2hs = ϕ∗ 

> s

g ˜Σs .— H(s) = ϕ∗ 

> s

H ˜Σs ≡ n−1 

> s

,— A(s) = ϕ∗ 

> s

A˜Σs ,— N (s) = ϕ∗ 

> s

N ˜Σs

— fi(s) = d(s,. )Φ(0 , e i), où les ei(x) forment une base orthonormée de TxSn−1/

Γ, — ∇s = ϕ∗ 

> s

∇˜Σs ,— ∆ s = ϕ∗ 

> s

∆˜Σs , où ∆ ˜Σs est l’opérateur de Laplace-Beltrami (à valeur propres 118 Chapitre 3. De Gromov-Hausdorff à C∞ à poids négatives) associé à g ˜Σs ,— grad s le gradient pour s2hs,— K(s)ji = g(

Rm g(N (s), f i(s)) fj (s), N (s))

,On a les variations suivantes des quantités géométriques montrées en annexe dans le corollaire A.7, mais aussi prouvées dans le théorème 3.2 de [HP99]. 

Lemme 3.40 (Corollaire A.7, [HP99, Theorem 3.2]) . Étant donnée une variation 

∂sΦ( s, x ) = usN ˜Σs , on a les variations suivantes des quantités géométriques : 1. ∂s

> (

s2hs

> )

= 2 usA(s),2. ∂sN (s) = grad sus,3. ∂sA(s)ij = −∇ si ∇sj us + ( ∑ 

> k

A(s)ik A(s)kj + K(s)ji

> )

,4. ∂sH(s) = −

> (

∆s + ∣∣∣A(s)∣∣∣2

+ Ric (

N (s), N (s)))

us.

6.3 Contrôle de la métrique 

Contrôlons maintenant la métrique dans ces coordonnées. L’objectif est la pro-position suivante. 

Proposition 3.41. Avec les notations précédentes en particulier le difféomor-phisme Φ : [2 ρ1, 12 ρ2] × Sn−1/Γ → ˜A(2 ρ1, 12 ρ2), et si l’on note ge := ds 2 + s2gSn−1

,on a de plus les contrôles suivants sur Φ∗g = us(x)2ds 2 +s2hs(x) : pour tout l ∈ N,il existe C(l, n, v 0, D 0) > 0 telle que pour tout s ∈ [

2ρ1, 14 ρ2

> ]

, on a sur l’anneau 

[s, 2s],

‖u − 1‖Cl(ge) 6 Cη (s),

et 

‖h − gSn−1/Γ‖Cl(ge) 6 Cη (s),

et donc, pour tout s ∈ [2 ρ1, 14 ρ2], sur l’anneau de rayons s et 2s,

‖Φ∗g − ge‖Cl(ge) 6 Cη (s).

Démonstration. Notons pour commencer que le point 4 du lemme 3.40 implique que us satisfait l’équation suivante sur Sn−1/Γ pour tout sn − 1

s2 =

> (

∆s + ∣∣∣A(s)∣∣∣2

+ Ric( s)(

N (s), N (s)))

us. (3.17) En effet, en suivant la perturbation normale par usN ˜Σs = −grad ( 1

> s
> )

, la variation première de la courbure moyenne est exactement −n−1 

> s2

. On en déduit en particulier 6. Coordonnées optimales et contrôle de la métrique 119 que l’on a pour tout s,

(

∆s +

∣∣∣A(s)

∣∣∣2

+Ric (

N (s), N (s)))

(us −1) = n − 1

s2 −

∣∣∣A(s)

∣∣∣2

−Ric( s)(

N (s), N (s))

,

(3.18) D’après la proposition 3.24, tant que ‖hs −gSn−1/Γ‖C1,α (gSn−1/Γ) est suffisamment petit, il existe C = C(α, n ) > 0 telle que pour tout s,

∥∥∥∥

A(s)

s − hs

∥∥∥∥Cα(hs)

6 Cη (s). (3.19) Comme s2∣∣∣ Ric( s)(

N (s), N (s))∣ ∣∣ = s2|Λ| < η(s), cela implique que le second membre de (3.18) satisfait : il existe C = C(α, n ) > 0 telle que pour tout s,

∥∥∥∥n − 1 − s2∣∣∣A(s)∣∣∣2

− s2 Ric( s)(

N (s), N (s))∥∥∥∥Cα(gSn−1/Γ)

6 Cη (s).

De même, pour le membre de gauche, pour toute fonction v : Sn−1/Γ → R

∥∥∥∥s2

(

∆s +

∣∣∣A(s)

∣∣∣2

+ Ric( s)(

N (s), N (s)))

v−

(

∆Sn−1/Γ + n − 1

)

v

∥∥∥∥Cα(gSn−1/Γ)

6 Cη (s)‖v‖C2,α (gSn−1/Γ).

Comme ∆ Sn−1/Γ +n−1, est un opérateur elliptique inversible,on obtient le contrôle suivant par le lemme 1.60 : il existe C = C(n, α ) > 0 telle que pour tout s

‖us − 1‖C2,α (gSn−1/Γ) 6 Cη (s). (3.20) Montrons maintenant que pour tout s ∈ [2 ρ1, 12 ρ2], ‖hs − gSn−1/Γ‖C1,α (gSn−1/Γ)

reste petit. Nous allons en fait montrer qu’il existe C′′ = C′′ (n, α ) > 0 telle que 

‖hs − gSn−1/Γ‖C1,α (gSn−1/Γ) 6 C′η(s). La première égalité du lemme 3.40 se réécrit 

∂s

(

hs − gSn−1/Γ)

= 2

s

(

uAs

s − hs

)

,

or, par le contrôle (3.20), et la proposition 3.24, il existe C = C(n, α ) > 0 telle que l’on ait 

∥∥∥∥uAs 

> s

− hs

∥∥∥∥C1,α (gSn−1/Γ)

6 Cη (s). En se rappelant que 

η(s) := Cε 

[( ρ1

s

)β1

+

( sρ2

)β2 ]

,120 Chapitre 3. De Gromov-Hausdorff à C∞ à poids on en déduit que pour ¯ ρ < s 0 < 12 ρ2, on a 

∥∥∥hs0 − gSn−1/Γ∥∥∥C1,α (gSn−1/Γ) 6C

(

η(¯ ρ) + 

∫ s0

> ¯ρ

2

s η(s)ds 

)

=Cη (¯ ρ) + 

( 2C′ερβ2

> 2

∫ s0

> ¯ρ

sβ2−1ds 

)

=Cε ¯ρβ2

ρβ2

> 2

+

( 2C′ερβ2

> 2

(sβ2 

> 0

− ¯ρβ2 )

)

6C′′ η(s0).

et de même, pour 2 ρ1 < s 0 < ¯ρ,

∥∥∥hs0 − gSn−1/Γ∥∥∥C1,α (gSn−1/Γ) 6 C′′ η(s0).

Pour obtenir des contrôles des autres dérivées de u et hs, on utilise les autres égalités du lemme 3.40 : d’après l’égalité 2, et le contrôle (3.20), il existe C =

C(n, α ) tel qu’on ait pour tout s

‖∂sN (s)‖C1,α (hs) 6 Cη (s) (3.21) d’après d’égalité 3 et les contrôles (3.20), (3.19) et (3.21), et comme les dérivées 

l-ièmes de la courbures sont bornées par s−2−lη(s), il existe C = C(n, α ) > 0 telle qu’on ait pour tout s :

∥∥∥∥∂s

( A(s)

s

)∥ ∥∥∥Cα(hs)

6 Cη (s). (3.22) En dérivant l’égalité 4 par rapport à s, et en utilisant les inégalités ‖∂shs‖C1,α 6

Cη (s), et (3.22), il existe C = C(n, α ) > 0 telle qu’on ait pour tout s :

∥∥∥∥(

∆Sn−1/Γ + n − 1

)

∂sus

∥∥∥∥Cα(Sn−1/Γ) 

6 Cη (s).

On en déduit que pour tout s, ‖∂sus‖C2,α (hs) 6 Cη (s). En itérant, on obtient des contrôles de toutes les dérivées dans les directions tangentielles et normales. 6. Coordonnées optimales et contrôle de la métrique 121 

6.4 Proximité de la métrique d’Einstein et de la désingularisation naïve en norme Ck à poids 

Maintenant, pour obtenir un difféomorphisme global sur toute la variété M ,nous recollons les difféomorphismes locaux entre les domaines Mo(ε), Nj (ε) et 

Ak(t, ε ) et les domaines Mo(ε), Nj (ε) et Ak(t, ε ), par exemple à l’aide des tech-niques de centre de masse présentées entre autre dans [GW88]. Nous obtenons le résultat suivant. 

Théorème 3.42. Soit D0, v 0 > 0 et soit (M E 

> i

, g E 

> i

)i une suite de variétés d’Einstein telle que : — les volumes sont minorés par v0 > 0,— les diamètres sont majorés par D0,— les courbures de Ricci sont bornées | Ric | 6 3.Alors, il existe une sous-suite à topologie M fixe proche d’une désingularisation naïve (M, g Dϕi,t i ) d’un orbifold (Mo, g o) par des arbres de singularités (Nj , g bj , p j )

au sens suivant : pour tout l ∈ N et i assez grand il existe, C(l, v 0, D 0) > 0,

β1(v0, D 0) > 0 et β2(v0, D 0) > 0, εi > 0 εi → 0, et un difféomorphisme Φi : M →

M satisfaisant 1. sur Mo(εi), on a ∥∥∥∥Φ∗gE 

> i

− go

> ∥∥∥∥Cl(go)

6 Cε i.

2. aux différentes échelles Ti,j (associées à ti), sur Nj (εi) on a 

> ∥∥∥∥

Φ∗gE

> i

Ti,j 

− gbj 

> ∥∥∥∥Cl(gbj)

6 Cε i.

3. dans les zones annulaires intermédiaires, Ak(εi) incluses dans l’anneau de rayons ρi,k  

> 1

= 18 T 12

> i,k

ε−1 

> i

, ρi,k  

> 2

= 8 T 12 

> i,j

εi, pour tout ρi,k  

> 1

6 ρ 6 12 ρi,k  

> 2

, sur les anneaux de rayons ρ et 2ρ en notant Φρ = Φ ◦ ϕρ, où ϕρ est l’homothétie de rapport ρ sur le cône R4/Γk muni de la métrique plate notée ge,

> ∥∥∥∥

Φ∗

> ρ

gE

> i

ρ2 − ge

> ∥∥∥∥Cl(Ae(1 ,2))

6 Cε i 

> [(

ρi,k 

> 1

ρ

> )β1

+ 

> (

ρρi,k  

> 2
> )β2]

.

Remarque 3.43 . La valeur optimale pour ( β1, β 2) est en fait (4 , 2) avec une preuve similaire à la proposition 2.51, mais nous n’en aurons pas besoin pour la suite. 122 Chapitre 3. De Gromov-Hausdorff à C∞ à poids Chapitre 4 Désingularisations de métriques d’Einstein par recollement-perturbation 

Dans ce chapitre, dont les résultats sont essentiellement tirés du début de [Ozu19b], nous nous attaquons à la réciproque des résultats du chapitre précédent (ch.3). Nous étudions l’existence et l’unicité des métriques d’Einstein dans des voisinages C∞ à poids de nos recollements naïf. Nous montrons qu’il est toujours possible de trouver une unique métrique d’Einstein modulo obstructions dans un tel voisinage. 

Contributions. Nous développons une analyse dans des espaces à poids adaptés au cadre général des dégénérescences de métriques d’Einstein réelles. Cette analyse est aussi nouvelle dans le cadre kählérien. Nous en déduisons une réciproque au résultat du chapitre précédent (ch. 3) : toute désingularisation naïve gDt d’orbifold peut être perturbée en une métrique d’Einstein modulo certaines obstructions .En combinant cela aux résultats du chapitre précédent (ch. 3), nous produisons donc toutes les métriques d’Einstein dGH -proches de métriques singulières par recollement-perturbation. Cela éclaire la structure de l’espace de modules E(M )au dGH -voisinage de son bord ∂oE(M ). De plus, les obstructions que l’on obtient s’annulent si et seulement s’ il est possible de dGH -désingulariser un orbifold par des métriques d’Einstein lisses. 123 124 Chapitre 4. Désingularisation de métriques d’Einstein 

# 1 Espaces fonctionnels 

Définissons pour commencer les différents espaces fonctionnels dans lesquels l’analyse du reste de cette thèse se place. 

Note 4.1. Dans les résultats de ce chapitre, lorsqu’aucune hypothèse n’est spécifiée sur un orbifold d’Einstein (Mo, g o), il peut être indifféremment supposé compact ou ALE. 

1.1 Une réécriture du contrôle entre les métriques 

Pour Γ un sous-groupe fini de SO (4) agissant librement sur S3, notons ( R4/

Γ, g e) le quotient de l’espace plat par Γ, et re := de(., 0). Soient ( Mo, g o) un orbifold d’Einstein, et ( M, g D) une désingularisation naïve de ( Mo, g o) par un arbre d’or-bifolds Ricci-plats ALE ( Nj , g bj ) recollés à des échelles Tj > 0. Il existe ε0 > 0 tel que l’on ait les propriétés suivantes. Pour chaque point singulier pk de Mo de sin-gularité R4/Γk, d’après la proposition 2.51, il existe un voisinage de pk, Uk ⊂ Mo

et un difféomorphisme Φ k : Be(0 , ε 0) ⊂ R4/Γk → Uk ⊂ Mo où la métrique est contrôlée. 

Définition 4.2 (Fonction ro sur un orbifold) . On définit ro une fonction lisse sur 

Mo satisfaisant ro := Φ ∗

> k

re sur chaque Uk, et telle que sur Mo\Uk, on ait ε0 < r o < 1(les différents choix possibles seront équivalents pour nos applications). De même, toujours d’après la proposition 2.51, sur chaque orbifold Ricci-plat ALE Nj , il existe Uk des voisinages des points singuliers pk et U∞ un voisinage de l’infini et des difféomorphismes Ψ k : Be(0 , ε 0) ⊂ R4/Γk → Uk ⊂ Nj et Ψ ∞ : ( R4/

Γ∞)\Be(0 , ε −10 ) → U∞ ⊂ Nj grâce auxquels la métrique est bien contrôlée. 

Définition 4.3 (Fonction rbj sur un orbifold ALE) . On définit rbj une fonction lisse sur Nj satisfaisant rbj := Ψ ∗

> k

re sur chaque Uk, et rbj := Ψ ∗∞re sur U∞, et telle que ε0 < r bj < ε −10 sur le reste de Nj (les différents choix possibles seront équivalents pour nos applications). Dans le chapitre 3 précédent, pour 0 < ε 6 ε0 nous avons utilisé un recouvre-ment M = Mo(ε) ∪ ⋃ 

> j

Nj (ε) ∪ ⋃ 

> k

Ak(t, ε ). Rappelons que si ( Nj , g bj ) est recollé à ( Nk, g bk ), on note alors l’échelle relative tj := Tj 

> Tk

, et tj = Tj si ( Nj , g bj , p j ) est recollé à ( Mo, g o). La variété M est aussi découpée en M = M to ∪ ⋃ 

> j

N tj , où 

M to := Mo\( ⋃ 

> k

Φk(Be(0 , t 14 

> k

)) )

,1. Espaces fonctionnels 125 où tk > 0 l’échelle de recollement de Nk au point singulier pk ∈ Mo, et où 

N tj := (

Nj \Ψ∞

> (

(R4/Γ∞)\Be(0 , 2t− 14 

> j

))) 

\( ⋃ 

> k

Ψk(Be(0 , t 14 

> k

))

.

Sur M 16 to ⊂ M to, on a gD = go et sur chaque N 16 tj ⊂ N tj , on a gD = Tj gbj .On définit aussi tmax := max j tj . Par définition des recollements, sur l’intersection 

N tj ∩M to on a alors √

Tj rbj = ro, et sur l’intersection N tj ∩N tk, on a √

Tj rbj = √Tkrbk .

Définition 4.4 (La fonction rD sur une désingularisation naïve) . Sur une désin-gularisation naïve ( M, g D), on définit une fonction rD de la manière suivante : 1. rD = ro sur M to,2. rD = √

Tj rbj sur chaque N tj .La fonction rD est lisse sur M .Cette fonction nous permet de réécrire le théorème. 

Corollaire 4.5. Soit D0, v 0 > 0, l ∈ N et soit (M E 

> i

, g E 

> i

)i une suite de variétés d’Einstein telle que : — les volumes sont minorés par v0 > 0,— les diamètres sont majorés par D0,— les courbures de Ricci sont bornées | Ric | 6 3.Alors, il existe β = β(v0, D 0) > 0, une sous-suite (M, g E 

> i

)i à topologie M fixe, un difféomorphisme ϕi : M → M et des désingularisations naïves (M, g Di ) d’un orbi-fold d’Einstein (Mo, g o) par des orbifolds Ricci-plats ALE (Nj , g bj , p j ) aux échelles 

ti telles que M = M ti 

> o

∪ ⋃ 

> j

N ti 

> j

et pour tout l ∈ N et i ∈ N assez grand : 1. sur M ti 

> o

, on ait 

r−β+lD,i 

> ∣∣∣

∇lgo (gE 

> i

− go)∣∣∣go

6 1

i ,

2. sur N ti 

> j

, avec Ti,j l’échelle de Nj associée à ti,

max  

> (

rD,i 

> √

Ti,j 

> )−β+l

, 

> (

rD,i 

> √

Ti,j 

> )β+l
> ∣∣∣∣∣

∇l 

> (

gE

> i

Ti,j 

− gbj

> )∣∣∣∣∣gbj

6 1

i .

Remarque 4.6 . Sur un anneau intermédiaire Ak(t, ε ) où Nk se recolle à Nj , les rayons extérieur et intérieur sont (à une constante près) ρ′ = √Tk et ρ = √

Tj =

√tj

√Tk, et on retrouve bien un contrôle avec un poids max  

> (

rD

> √

Tj

> )−β

, 

> (

rD

√Tk 

> )β
> 

≈ max  

> [(

ρrD

> )β

, 

> (

rD

ρ′ 

> )β]

126 Chapitre 4. Désingularisation de métriques d’Einstein équivalent au dernier contrôle du théorème 3.42. 

1.2 Espaces de Hölder à poids sur les orbifolds et ALE 

Définissons tout d’abord des espaces à poids sur des variétés asymptotiques à des cônes ou ayant des singularités coniques. Pour les orbifolds, on considère une norme qui est bornée pour les tenseurs qui décroissent aux points singuliers. 

Définition 4.7 (Norme à poids sur un orbifold) . Soit β ∈ R, k ∈ N, 0 < α < 1 et (Mo, g o) un orbifold. Définissons alors pour tout tenseur s sur Mo,

‖s‖Ck,α β (go) := sup 

> Mo

r−βo 

> (k∑
> i=0

rio|∇ igo s|go + rk+αo [∇kgo s]Cα(go)

> )

.

Remarque 4.8 . Le rayon d’injectivité en un point x ∈ Mo est équivalent à ro.Pour les variétés ALE, on considère une norme qui est bornée pour les tenseurs qui décroissent à l’infini. 

Définition 4.9 (Norme à poids sur une variété ALE) . Soit β ∈ R, k ∈ N, 0 <α < 1 et ( N, g b) une variété ALE. Définissons pour tout tenseur s sur N ,

‖s‖Ck,α β (gb) := sup 

> N

rβb 

> (k∑
> i=0

rib|∇ igb s|gb + rk+αb [∇kgb s]Cα(gb)

> )

.

Remarque 4.10 . Le rayon d’injectivité en un point x ∈ N est équivalent à rbj .

Définition 4.11 (Norme à poids sur les orbifolds ALE) . On définit aussi natu-rellement une norme à poids pour β ∈ R, k ∈ N et 0 < α < 1 sur un orbifold ALE (N, g b) par le maximum des deux normes précédentes. 

‖s‖Ck,α β (gb) := sup 

> N
> {

max( rβb , r −βb ) 

> (k∑
> i=0

rib|∇ igb s|gb + rk+αb [∇kgb s]Cα(gb)

> )}

.

qui est bornée sur les tenseurs décroissant à l’infini et aux points singuliers. Sur des espaces non compacts, les opérateurs elliptiques asymptotiques à des laplaciens ont de bonnes propriétés Fredholm dans ces espaces à poids. Ce n’est pas le cas des espaces de Hölder ou Sobolev classiques, voir [LM85] par exemple. 1. Espaces fonctionnels 127 

1.3 Espaces fonctionnels sur les arbres de singularités 

Supposons que ( M, g D) soit une désingularisation naïve de ( Mo, g o) par un arbre de singularités ( Nj , g bj ). Pour tmax < ε 40, pour ε0 > 0 la constante du début de la partie 1.1 ne dépendant que de go et des gbj , on définit la norme à poids globale de la manière suivante. Choisissons une partition de l’unité : 1 = χM to + ∑

> j

χN tj ,

où χM to à support dans M to et valant 1 sur M 16 to et χN tj à support dans N tj et valant 1 sur N 16 tj , sont des fonctions de coupure telles que pour tout k ∈ N, il existe Ck > 0 telle que |∇ kgD χ(x)|gD 6 Ck  

> rD(x)k

.

Définition 4.12 (Norme à poids adaptée aux arbres de singularités) . Soit β ∈ R et 

k ∈ N, 0 < α < 1. On définit pour s ∈ T M ⊗l+ ⊗ T ∗M ⊗l− un tenseur ( l+, l −) ∈ N2,avec l := l+ − l− le poids conforme associé à la section. 

‖s‖Ck,α β (gD ) := ‖χM to s‖Ck,α β (go) + ∑

> j

T l 

> 2
> j

‖χN tj s‖Ck,α β (gbj ).

Remarque 4.13 . La présence de T l 

> 2
> j

vient du fait que sur N tj , la métrique gD est proche de Tj gbj . En effet, pour s un tenseur ( l+, l −) de poids conforme l+ − l−,nous avons 

|s|Tj gbj = T l 

> 2
> j

|s|gbj .

Figure 4.1 – Norme à poids pour une singularité. Cette norme a l’avantage d’être adaptée aux cas de plusieurs singularités et d’arbres de singularités. 128 Chapitre 4. Désingularisation de métriques d’Einstein 

Figure 4.2 – Norme à poids sur un arbre de singularités. Grâce à cette norme, on peut par exemple décrire les métriques d’Einstein proches d’orbifolds au sens de Gromov-Hausdorff. 

Corollaire 4.14. Soient D0, v 0 > 0, l ∈ N, et β = β(v0, D 0) > 0 obtenu dans le corollaire 4.5. Alors, pour tout ε > 0, il existe δ = δ(ε, D 0, v 0, l ) > 0 tel que si 

(M, g E ) est une variété d’Einstein satisfaisant — le volume est minoré par v0 > 0,— le diamètre est majoré par D0,— la courbure de Ricci est bornée | Ric | 6 3.et telle que pour un orbifold d’Einstein (Mo, g o),

dGH 

> (

(M, g E ), (Mo, g o))

6 δ, 

alors, il existe une désingularisation naïve (M, g D) de (Mo, g o) par un arbre de singularités et un difféomorphisme ϕ : M → M tels que 

> ∥∥∥

ϕ∗gE − gD∥∥∥Clβ (gD ) 6 ε. 

Démonstration. Soit l ∈ N. Raisonnons par l’absurde et considérons une suite de contre-exemples, c’est-à-dire une suite de variétés d’Einstein ( Mi, g i)i telles que Vol( gi) > v0 > 0, diam (gi) < D 0 et | Ric( gi)|gi 6 3 convergeant au sens de Gromov-Hausdorff vers un orbifold d’Einstein ( Mo, g o), mais telles qu’il existe 

ε > 0 pour lequel pour tout i ∈ N et toute désingularisation naïve ( Mi, g Di ) de (Mo, g o), et tout difféomorphisme Φ i : Mi → Mi, on ait ‖Φ∗ 

> i

gi − gDi ‖Clβ (gD ) > ε .D’après le corollaire 4.5, il existe alors une sous-suite ( M, g i)i à topologie fixée, et une suite ( M, g Di ) contredisant cela pour i assez grand par définition de la norme à poids. 1. Espaces fonctionnels 129 La norme à poids est équivalente à la somme de celles des espaces modèles Mo,

Nj sur les tenseurs respectivement à support dans M to et N tj . Sur les anneaux de basse courbure Ak(t, ε 0) tirés en arrière sur des anneaux plats Ae(ρ1, ρ 2) ⊂ R4/Γ, elle est équivalente à une norme particulière qui permet de contrôler indépendam-ment des rayons les sommes de tenseurs qui décroissent au centre de l’anneau et de tenseurs qui décroissent à l’infini. 

Définition 4.15 (Norme à poids adaptée à un anneau) . Soient 0 < ρ 1 < ρ 2,

β ∈ R, k ∈ N, 0 < α < 1 et un tenseur s sur ( Ae(ρ1, ρ 2), g e) et la fonction 

re := de(0 , . ). On définit η(re) := max 

(( ρ1

> re

)β

,

( re

> ρ2

)β )

, et la norme, 

‖s‖Ck,α β (Ae(ρ1,ρ 2)) : = sup 

> Ae(ρ1,ρ 2)

[

η−1(re)

( k∑

> i=0

rie|∇ ige s|ge + rk+αe [∇kge s]Cα(ge)

)] 

.

Dans la suite, nous utiliserons souvent des espaces f C k,α β pour une fonction f

définie et lisse hors des points singuliers. Ils seront toujours munis de la norme suivante 

‖s‖f C k,α β

:= 

∥∥∥∥

sf

∥∥∥∥Ck,α β

.

Remarquons que par définition de rD, il existe une constante C = C(m, k, α ) >

0 dépendant des fonctions de coupure telle que 1

C ‖s‖rmD Ck,α β (gD ) 6 ‖χM to s‖rmo Ck,α β (go) + ∑

> j

T l−m 

> 2
> j

‖χN tj s‖rmbj Ck,α β (gbj ) 6 C‖s‖rmD Ck,α β (gD ).

(4.1) Finissons par lister quelques propriétés de ces normes à poids. 

Proposition 4.16. Soient β 6 β′, et k + α 6 k′ + α′, et m, m ′ ∈ Z. Pour toutes les normes à poids précédentes notées génériquement rmCk,α β , nous avons les propriétés suivantes : pour des tenseurs s et s′

— ‖s‖rmCk,α β

6 ‖s‖rmCk′,α ′

> β′

,— ‖∇ ks‖rmCk′−k,α β

6 ‖s‖rm+k Ck′,α β

— si ∗ est une composition, un produit ou une contraction de tenseurs, il existe 

C = C(∗, k, α, m, m ′, β, β ′) > 0 telle que 

‖s ∗ s′‖rm+m′ Ck,α β+β′

6 C‖s‖rmCk,α β

‖s′‖rm′ Ck,α β′

.

En particulier, pour un 2-tenseur h ∈ C2,α β (gD) et un champ de vecteurs X ∈

rDC3,α β (gD), on a pour Pg := 12 ∇∗

> g

∇g − ˚Rg,130 Chapitre 4. Désingularisation de métriques d’Einstein 

— PgD h ∈ r−2 

> D

Cαβ (gD),— δgD h ∈ r−1 

> D

C1,α β (gD),— δ∗ 

> gD

X ∈ C2,α β (gD),— δgD δ∗ 

> gD

X ∈ r−1 

> D

C1,α β (gD).

1.4 Estimations de Schauder à poids 

Des estimations de Schauder sont valables dans ces normes à poids pour l’opé-rateur P := 12 ∇∗∇ − ˚R. 

Proposition 4.17. Pour tous β > 0 et 0 < α < 1, il existe C > 0 et ε > 0 tels que si h est un 2-tenseur symétrique sur (M, g D), et g une métrique sur M telle que 

‖g − gD‖C2,α β (gD ) 6 ε, 

alors, 

‖h‖C2,α β (gD ) 6 C(

‖Pgh‖r−2    

> DCαβ(gD)

+ ‖h‖C0  

> β(gD)

)

.

Démonstration. Soit g une métrique sur M telle qu’on ait ‖g − gD‖C2,α β (gD ) 6 ε,pour ε > 0 que l’on choisira suffisamment petit au cours de la preuve. Sur les compacts Mo(ε0) de l’orbifold et Nj (ε0) des ALE privés de leurs points singuliers, on a une estimation elliptique sur les opérateurs Pgo et Pgbj : il existe 

C1 > 0 telle que pour tous 2-tenseurs ho à support dans Mo(ε0) et hj à support dans Nj (ε0), on ait 

‖ho‖C2,α (go) 6 C1

(

‖Pgo ho‖Cα(go) + ‖ho‖C0(go)

)

,

et 

‖hj ‖C2,α (gbj ) 6 C1

(

‖Pgbj hj ‖Cα(gbj ) + ‖hj ‖C0(gbj )

)

.

Par hypothèse, il existe C > 0 ne dépendant que de go et gbj tel que ‖g −

go‖C2,α (go) 6 Cε sur Mo(ε0) et 

∥∥∥ gTj − gbj

∥∥∥C2,α (gbj ) 6 Cε sur Nj (ε0). On en déduit que pour ε suffisamment petit, les opérateurs Pg et P gTj

, qui sont proches des opérateurs Pgo et Pgbj , satisfont pour tous ho à support dans Mo(ε0) et hj à support dans Nj (ε0), 

‖ho‖C2,α (go) 6 2C1

(

‖Pgho‖Cα(go) + ‖ho‖C0(go)

)

,

et 

‖hj ‖C2,α (gbj ) 6 2C1

(∥ ∥∥P gTj

hj

∥∥∥Cα(gbj ) + ‖hj ‖C0(gbj )

)

.1. Espaces fonctionnels 131 Sur chaque anneau presque plat Ak(t, ε 0), sur l’anneau Aρ := {ρ 6 rD 6 2ρ},il existe un difféomorphisme ϕρ : Ae(1 , 2) → A ρ tel que 

∥∥∥∥

ϕ∗

> ρ

gρ2 − ge

∥∥∥∥C1,α 

6 Cη (ρ)ε. 

Ainsi par ellipticité, pour ε suffisamment petit, il existe C2 > 0, telle que pour tout 2-tenseur h à support compact dans Ae(1 , 2) on ait, 

‖h‖C2,α (Ae(1 ,2)) 6 2C2

(

‖h‖C0(Ae(1 ,2)) + ∥∥∥Pϕ∗

> ρgρ2

h∥∥∥Cα(Ae(1 ,2)) 

)

.

En revenant à ( M, g ), cela implique que pour ε suffisamment petit, on ait 

‖h‖C2,α (Aρ, gρ2 ) 6 4C2

(

‖h‖C0(Aρ, gρ2 ) + ∥∥∥P gρ2 h∥∥∥Cα(Aρ, gρ2 )

)

.

La norme d’un 2-tenseur s se comporte de la manière suivante par changement d’échelle, pour t > 0 : 

|s|gt = t|s|g,

et l’opérateur P se comporte de la manière suivante par changement d’échelle, pour t > 0 : Pgt = tP g. En multipliant les deux côtés de l’égalité par r−2 

> D

, on obtient 

‖h‖C2,α (Aρ,g ) 6 4C2

(

‖h‖C0(Aρ,g ) + r2

> D

‖Pgh‖Cα(Aρ,g )

)

.

Étant donnés les contrôles sur les dérivées de rD, on en déduit le résultat énoncé par définition des normes à poids en multipliant les deux côtés de l’inégalité par le poids de la norme. Des estimations analogues sont aussi valables pour l’opérateur elliptique δδ ∗

avec une preuve analogue. 

Proposition 4.18. Pour tous β > 0 et 0 < α < 1 il existe C > 0 et ε > 0 tels que si X est un champ de vecteurs sur (M, g D), et g une métrique sur M telle que 

‖g − gD‖C2,α β (gD ) 6 ε, 

alors, 

‖X‖rD C3,α β (gD ) 6 C(

‖δgδ∗ 

> g

X‖r−1    

> DC1,α β(gD)

+ ‖X‖rD C0  

> β(gD)

)

.132 Chapitre 4. Désingularisation de métriques d’Einstein 

1.5 Normes de découplage 

Nous montrons maintenant que pour espérer de bons contrôles pour les opéra-teurs P et δδ ∗ dans les zones annulaires de notre variété, nous devons considérer séparément l’influence des 2-tenseurs constants pour P et des champs de vecteurs linéaires du noyau de δeδ∗ 

> e

pour δδ ∗.

Estimations sur les anneaux Ae(ε, ε −1) de (R4, g e). Étudions tout d’abord la situation sur des anneaux plats. 

Proposition 4.19. Soient 0 < β < 1, 0 < α < 1, et Pge = 12 ∇∗

> e

∇e −˚Re = 12 ∇∗

> e

∇e.Il existe Ce > 0, et εe > 0 tels que pour tout 2-tenseur h sur un anneau de rayons 

0 < ε < ε e et 1 

> ε

, il existe un 2-tenseur constant H0 et un 2-tenseur H∗ défini sur l’anneau Ae(ε, ε −1) satisfaisant 

∇∗

> e

∇eH∗ = 0 ,

‖H∗‖C2,α   

> 1(Ae(2 ε, (1 /2) ε−1))

6 Ce‖h − H0‖C2,α β (Ae(ε,ε −1)) , (4.2) 

(remarquer la norme C2,α  

> 1

pour le membre de gauche) et, 

‖h − H0 − H∗‖C2,α β (Ae(2 ε, (1 /2) ε−1)) 6 Ce‖Pge h‖r−2  

> eCαβ(Ae(ε,ε −1))

. (4.3) 

Cela implique en particulier le contrôle suivant, pour tout x ∈ Ae(1 /2, 2) ,

|h − H0(x)|ge + |∇ h(x)|ge + |∇ 2h(x)|ge + [ ∇2h]Cα(g)(x)

6 Ce

(

(2 ε)β ‖Pge h‖r−2   

> eCαβ(Ae(ε,ε −1))

+ 2 ε‖h − H0‖C2,α β (Ae(ε,ε −1)) 

)

.

(4.4) 

Démonstration. Remarquons pour commencer que (4.4) est une conséquence de (4.2) et (4.3). En effet, h − H0 = ( h − H0 − H∗) + H∗, et on a donc, en notant 

‖s‖C2,α (1 /2,2) := sup 

> x∈Ae(1 /2,2)

|s(x)|ge + |∇ s(x)|ge + |∇ 2s(x)|ge + [ ∇2s]Cα(g)(x),

‖h − H0‖C2,α (1 /2,2) 6 ‖h − H0 − H∗‖C2,α (1 /2,2) + ‖H∗‖C2,α (1 /2,2) 

6 (2 ε)β ‖h − H0 − H∗‖C2,α β (Ae(ε,ε −1)) + 2 ε‖H∗‖C2,α  

> 1(Ae(ε,ε −1))

6 Ce

(

(2 ε)β ‖Pge h‖r−2   

> eCαβ(Ae(ε,ε −1))

+ 2 ε‖h − H0‖C2,α β (Ae(ε,ε −1)) 

)

,1. Espaces fonctionnels 133 par définition des normes à poids et en supposant, pour Ce > 0, les inégalités (4.3) et (4.2). D’après le lemme 2.49, sur R4\{ 0}, les 2-tenseurs harmoniques sont sommes de 2-tenseurs harmoniques homogènes dont les coefficients sont proportionnels à rj

pour j ∈ Z\{− 1}. Ces 2-tenseurs harmoniques s’écrivent plus précisément rke Hk

ou r−2−ke Hk pour k ∈ N, où Hk est un 2-tenseur radial dont les coefficients, une fois restreints à la sphère unité sont des fonctions propres du laplacien de valeurs propres −k(k + 2). En particulier, on remarque que tout 2-tenseur harmonique non constant s’écrit comme un 2-tenseur constant plus un tenseur explosant au moins en r−2 

> e

en 0 ou en re à l’infini. Pour tout 2-tenseur h sur Ae(ε, ε −1), définissons ˜H la solution du problème de Dirichlet suivant, en notant Se(r) := {re = r},

> 

∇∗

> e

∇e ˜H = 0 ,

˜H = h sur Se(ε) ∪ Se(ε−1).

Plus précisément, ˜H = ∑

> k>0

(εr e)k ˜H+ 

> k

+ ( ε−1re)−2−k ˜H− 

> k

où, si l’on décompose en harmoniques sphériques h|Se(ε) = ∑ 

> k

Hk(ε) et h|Se(ε−1) = ∑ 

> k

Hk(ε−1), on a le système 

Hk(ε−1) = ˜H+ 

> k

+ ε4+2 k ˜H− 

> k

,Hk(ε) = ε2k ˜H+ 

> k

+ ˜H− 

> k

,

et donc, 

˜H+ 

> k

= 11 − ε4+4 k

> (

Hk(ε−1) − ε4+2 kHk(ε))

,

˜H− 

> k

= 11 − ε4+4 k

> (

Hk(ε) − ε2kHk(ε−1))

,

(4.5) Posons ˜H∗ := ˜H − ˜H+0 . Comme ∇∗

> e

∇e ˜H∗ = 0, par régularité elliptique entre espaces de Sobolev et injection de Sobolev sur l’anneau Ae(ρ/ 2, 4ρ) ⊂ Ae(ε, ε −1), il existe une constante C > 0 indépendante de h telle qu’on ait, 

‖ ˜H∗‖C0(Ae(ρ, 2ρ)) 6 Cρ2 ‖ ˜H∗‖L2(Ae(ρ/ 2,4ρ)) , (4.6) donc pour contrôler la norme C01 (Ae(ε, ε −1)) de ˜H∗, il nous suffit donc de contrôler la norme L2 de ˜H∗ sur les différents anneaux Ae(ρ, 2ρ) ⊂ Ae(ε, ε −1). Les égalités (4.5) et le fait que les décompositions en harmoniques sphériques soient orthogo-nales nous donnent alors l’estimation suivante pour ε suffisamment petit et une 134 Chapitre 4. Désingularisation de métriques d’Einstein certaine constante C > 0, 

‖ ˜H∗‖2 

> L2(Ae(ρ, 2ρ))

6 2

∫

> Ae(ρ, 2ρ)

∑

> k>0

∣∣∣(reε)k+1 (

Hk+1 (ε−1) − ε4+2( k+1) Hk+1 (ε))

+ ( reε−1)−2−k(

Hk(ε) − ε2kHk(ε−1))∣ ∣∣2

6 C

∫

> Ae(ρ, 2ρ)

(reε)2(

|(h − ˜H+0 )|Se(ε)|2 + ε8|(h − ˜H+0 )|Se(ε−1)|2)

+ ( reε−1)−4(

|(h − ˜H+0 )|Se(ε)|2 + |(h − ˜H+0 )|Se(ε−1)|2)

6 C2ρ4ε2(

ρ1 + ρ−1)2

‖h − ˜H+0 ‖2  

> C0
> β(Ae(ε,ε −1))

(4.7) car |(h − ˜H+0 )|Se(ε)|ge 6 ‖h − ˜H+0 ‖C0  

> β(Ae(ε,ε −1))

et |(h − ˜H+0 )|Se(ε−1)|ge 6 ‖h −

˜H+0 ‖C0  

> β(Ae(ε,ε −1))

par définition de la norme. En combinant (4.6) et (4.7), on obtient 

‖ ˜H∗‖C01 (Ae(ε,ε −1)) 6 C‖h − ˜H+0 ‖C0  

> β(Ae(ε,ε −1))

(4.8) Fixons x0 ∈ Se(1) et modifions notre 2-tenseur ˜H pour obtenir un 2-tenseur 

H tel que h − H s’annule en x0 et sur Se(ε) tout en étant constant sur Se(ε−1). Le seul choix possible à l’aide de 2-tenseurs harmoniques est 

H := 

(

˜H+0 − c0

1 − ε2

)

+

(

˜H∗ + ε2

1 − ε2

c0

r2

> e

)

,

où c0 = ( h− ˜H)( x0). Nous allons tout d’abord prouver le contrôle (4.2) de l’énoncé. Notons H0 := ˜H+0 − c0 

> 1−ε2

la partie constante de H, et H∗ := ˜H∗ + 11−ε2 

> c0
> (ε−1re)2

sa partie variable. D’après (4.7), la partie ˜H∗ = ∑

> k>1

(εr e)k ˜H+ 

> k

+( ε−1re)−2−k ˜H− 

> k

est bien contrôlée en norme L2 par les parties de moyenne nulle de h−H0 sur Se(ε) et Se(ε) (qui sont les mêmes que h − ˜H0). Il nous reste alors à contrôler le terme en r−2 

> e

, c’est-à-dire 11 − ε2

(1 − ε2) ˜H− 

> 0

+ c0

ε−2r2

> e

.

D’après (4.5), | ˜H− 

> 0

| est contrôlé par la différence entre la valeur moyenne de h−H0

sur la sphère Se(ε) et celle sur la sphère Se(ε−1) (qui est la même que h − ˜H0). Nous avons donc | ˜H− 

> 0

| 6 3‖h − H0‖C0 

> β

pour ε suffisamment petit. Pour contrôler 

|c0| en fonction de ‖h − H0‖C0 

> β

, il suffit de noter que la valeur moyenne de h − H0

sur Se(ε−1) vaut ε4 ˜H− 

> 0

+ c0, et que l’on a donc |c0|ge 6 (1 + 3 ε4)‖h − H0‖C0 

> β

car 

| ˜H− 

> 0

|ge 6 3‖h − H0‖C0 

> β

.Nous en déduisons donc finalement l’existence d’une constante C > 0 telle que 1. Espaces fonctionnels 135 nous ayons, en passant de contrôles L2 à des contrôles C0 à l’aide de (4.6) appliqué à H∗,

‖H∗‖C01 6 C‖h − H0‖C0 

> β

,

et donc l’inégalité (4.2) énoncée. Prouvons l’estimation (4.3), et raisonnons par l’absurde en supposant qu’il existe une suite de réels strictement positifs εi → 0, et une suite de 2-tenseurs hi

sur des anneaux Ae(εi, ε −1 

> i

) satisfaisant, ‖hi − Hi‖C0  

> β(Ae(ε,ε −1))

= 1, et 

‖Pehi‖r−2    

> eC0
> β(Ae(εi,ε −1
> i))

6 1

i .

Soit alors xi une suite de points de Ae(εi, ε −1 

> i

) où la norme C0 

> β

(Ae(εi, ε −1 

> i

)) de ¯hi := hi − Hi est atteinte. On peut en extraire une sous-suite ayant l’un des comportements suivants : 1. re(xi) → +∞, et εire(xi) → 0, 2. re(xi) → +∞, et εire(xi) → c > 0, 3. re(xi) → 0 et ε−1 

> i

re(xi) → +∞,4. re(xi) → 0 et ε−1 

> i

re(xi) → c > 0, 5. re(xi) → c > 0. Dans tous les cas, nous pouvons effectuer un changement d’échelle pour fixer 

re(xi) = 1 en posant pour tout x,

h′

> i

(x) := ¯hi

(

re(xi)x)

εβi (re(xi)β + re(xi)−β

) ,

qui satisfait donc 

(

∇∗

> e

∇eh′

> i

)

(x) = re(xi)2(

∇∗

> e

∇e¯hi

)

(re(xi)x).

Comme nous avions par hypothèse les contrôles ¯hi(x) 6 εβi

(

re(x)β + re(x)−β )

,

et 

|∇ ∗

> e

∇e¯hi|(x) 6 1

i re(x)−2εβi

(

re(x)β + re(x)−β )

,

notre nouveau 2-tenseur h′ 

> i

s’annule en x0 

> re(xi)

et sur Se(εire(xi)−1), et est constant 136 Chapitre 4. Désingularisation de métriques d’Einstein sur le bord Se(ε−1 

> i

re(xi)−1). Il satisfait de plus pour tout x

|h′

> i

|(x) 6

> (

(re(xi)re(x)) β + ( re(xi)re(x)) −β )

re(xi)β + re(xi)−β

et 

|∇ ∗

> e

∇eh′

> i

|(x) 6 1

i re(x)−2 (( re(xi)re(x)) β + ( re(xi)re(x)) −β )

re(xi)β + re(xi)−β .

Dans les différents cas, quitte à extraire une sous-suite, on obtient alors une des situations limites suivantes, 1. sur ( R4/Γ) \{ 0}, une solution h′∞ de Peh′∞ = 12 ∇∗

> e

∇eh′∞ = 0, et sup r−β h′∞ =1. Or, il n’existe pas de telle solution car les 2-tenseurs harmoniques dé-croissent au moins en O(r) en 0 s’ils s’y annulent et doivent donc aussi croître à cette vitesse à l’infini. C’est absurde. 2. sur ( Be(1 /c )/Γ) \{ 0}, une solution h′∞ de Peh′∞ = 0, et sup r−β h′∞ = 1, et telle que ( h′∞)|Se(1 /c ) soit constant. L’unique solution du problème de Di-richlet avec annulation en zéro et une condition constante sur Se(1 /c ) est 

h′∞ = 0, ce qui est absurde. 3. sur ( R4/Γ) \{ 0}, une solution h′∞ de Peh′∞ = 0, et sup rβ h′∞ = 1. Or, il n’existe pas de telle solution car les 2-tenseurs harmoniques tendant vers 0 à l’infini décroissent au moins en O(r−2) à l’infini, et explosent donc au moins à cette vitesse en 0. Finalement, h′∞ = 0, ce qui est absurde. 4. sur ( R4/Γ) \Be(1 /c ), une solution h′∞ de Peh′∞ = 0, et sup rβ h′∞ = 1 et (h′∞)|Se(1 /c ) = 0. Sur ( R4/Γ) \Be(1 /c ), l’unique solution du problème de Di-richlet sur avec décroissance à l’infini et annulation sur Se(1 /c ) étant nulle, nous avons h∞ = 0, ce qui est absurde. 5. sur ( R4/Γ) \{ 0}, une solution h′∞ de Peh′∞ = 0, et sup( rβ + r−β )h′∞ = 1 satisfaisant h′∞ 

> (x0
> c
> )

= 0. Les conditions Peh′∞ = 0, et sup( rβ + r−β )h′∞ = 1 impliquent que h′∞ est constant, comme h′∞ s’annule en x0 

> c

, h′∞ = 0, ce qui est absurde. Nous en déduisons donc qu’il existe εe > 0 et Ce > 0 tels que pour tout 0 < ε < ε e

et tout 2-tenseur h sur l’anneau Ae(ε, ε −1), on ait 

‖h − H0‖C2,α β (Ae(ε,ε −1)) 6 Ce‖Pgh‖r−2  

> eCαβ(Ae(ε,ε −1))

.

Le passage d’un contrôle en norme C0 

> β

à un contrôle en norme C2,α β est une conséquence des estimations elliptiques qui sont valables sur les anneaux plats d’après la fin de la preuve de la proposition 4.17. 1. Espaces fonctionnels 137 Avec une preuve tout à fait analogue en utilisant la décomposition harmonique des 1-formes sur un cône de [CT94, (2.16)-(2.19)] (voir aussi la section 2.1 de ce chapitre pour le cas particulier des cônes plats), nous avons le même résultat pour les champs de vecteurs, mais cette fois-ci, nous ne voulons pas tuer les constantes, mais le noyau linéaire de δδ ∗ sur R4/Γ. Sur R4, l’opérateur elliptique 

δδ ∗ = ∇∗∇ − 12d∗d = dd ∗ + 12d∗d, 

a son noyau restreint aux champs de vecteurs linéaires du noyau de δeδ∗ 

> e

parmi les champs de vecteurs en O(r1−β + r1+ β ) pour 0 < β < 1, voir le lemme 4.30 pour une preuve de ce résultat et la section 2.1 de ce chapitre pour une description du noyau. 

Proposition 4.20. Soit 0 < β < 1. Il existe Ce > 0, et εe > 0 tels que si un champ de vecteurs X satisfait ‖X‖reC3,α β (Ae(ε,ε −1)) 6 1 sur un anneau de rayons 

0 < ε < ε e et 1 

> ε

, alors, il existe un champ de vecteurs linéaire du noyau de δeδ∗ 

> e

,

Y0, et un élément Y∗ du noyau de δeδ∗ 

> e

satisfaisant 

‖Y∗‖reC3,α   

> 1(Ae(ε,ε −1))

6 Ce‖X − Y0‖reC3,α β (Ae(ε,ε −1)) ,

(remarquer la norme reC3,α  

> 1

pour le membre de gauche) et 

‖X − Y0 − Y∗‖reC3,α β (Ae(ε,ε −1)) 6 Ce‖δge δ∗ 

> ge

X‖r−1  

> eC1,α β(Ae(ε,ε −1))

.

Cela implique en particulier le contrôle suivant, pour tout x ∈ Ae(1 /2, 2) ,

|(X − Y0)( x)|ge + |∇ (X − Y0)( x)|ge + |∇ 2(X − Y0)( x)|ge + [ ∇2(X − Y0)] Cα(g)(x)

6 Ce

(

(2 ε)β ‖δgδ∗ 

> g

‖r−1   

> eC1,α β(Ae(ε,ε −1))

+ 2 ε‖X − Y0‖reC3,α β (Ae(ε,ε −1)) 

)

.

(4.9) 

Les noyaux approchés sur les anneaux : 2-tenseurs constants et champs de vecteurs linéaires du noyau de δeδ∗ 

> e

. Soit ( M, g D) une désingularisation naïve d’orbifold d’Einstein ε-décrite par un arbre de singularités pour ε > 0. Pour chaque anneau Ak(t, ε ) de la définition 3.7 entre de Nk et Nj ou Nk et Mo, il existe un difféomorphisme Φk : Ae(ε−1√

Tj

√tk, ε 

√

Tj ) ⊂ R4/Γk → A k(t, ε ) ⊂ M, 138 Chapitre 4. Désingularisation de métriques d’Einstein tel qu’il existe C > 0 pour lequel, pour tout 0 < β < 1, 

> ∥∥∥∥

Φ∗

> k

gD − ge 

> ∥∥∥∥C2,α β(Ae(ε−1

√Tj 

> √tk,ε

√Tj )) 

6 Cε 2−β . (4.10) À cause des 2-tenseurs constants que l’on peut approcher sur ( M, g D) par coupure sur les anneaux Ak(t, ε ), nous ne pouvons pas obtenir d’estimations indépendantes des échelles de recollement sur ( M, g D) du type ‖h‖C2,α β (gD ) 6

C‖PgD h‖r−2   

> DCαβ(gD)

. De tels contrôles sont nécessaires pour appliquer un théorème des fonctions inverses. En effet, nous avons les estimations suivantes d’après la proposition 4.28 montrée dans la suite. 

Note 4.21. La plupart du temps, dans le reste de cette thèse, nous oublierons abu-sivement les difféomorphismes Φk au voisinage des points orbifolds afin d’alléger les notations. Par exemple, le 2-tenseur χAk (t,ε )Φ∗

> k

(H) sera noté χAk (t,ε )H sur M .

Proposition 4.22. Sur une désingularisation naïve (M, g D), pour tout 0 < β < 1,il existe C > 0 tel que pour Hk un 2-tenseur constant, on ait à la fois 

‖PgD (χAk (t,ε )Hk)‖r−2    

> DCαβ(gD)

6 C|Hk|ge ,

et 

‖χAk (t,ε )Hk‖C0   

> β(gD)

> 12t− β

> 4
> max

|Hk|ge .

Les champs de vecteurs linéaires du noyau de δeδ∗ 

> e

empêchent eux aussi les estimations indépendantes de t pour l’opérateur δδ ∗ d’après la proposition 4.28. 

Proposition 4.23. Sur une désingularisation naïve (M, g D), pour tout 0 < β < 1,il existe C > 0 tel que pour Xk un champ de vecteur linéaire du noyau de δeδ∗ 

> e

, on ait à la fois 

‖δgD δ∗ 

> gD

(χAk (t,ε )Xk)‖r−1    

> DC1,α β(gD)

6 C‖Xk‖reC00 (ge),

et 

‖χAk (t,ε )Xk‖C0   

> β(gD)

> 12t− β

> 4
> max

‖Xk‖reC00 (ge).

Norme à poids modulo les noyaux approchés des anneaux. Les pro-positions 4.19 et 4.20 montrent en fait que l’on peut contrôler l’inverse de nos opérateurs une fois que l’on résout nos équations modulo les 2-tenseurs constants et les champs de vecteurs linéaires du noyau de δeδ∗ 

> e

sur R4. Les propositions 4.22 et 4.23 montrent que l’on ne peut pas espérer mieux, et qu’il convient de trai-ter séparément ces 2-tenseurs et ces champs de vecteurs. Nous introduisons donc 1. Espaces fonctionnels 139 de nouvelles normes dans ce but. Elles sont similaires aux normes introduites, essentiellement pour la même raison, dans [Bam12]. 

Définition 4.24 (Norme ‖.‖Ck,α β, ∗

sur les 2-tenseurs) . Soit h un 2-tenseur sur (M, g D), ( Mo, g o) ou ( N, g b). On définit sa norme Ck,α β, ∗ par 

‖h‖Ck,α β, ∗

:= inf 

> h∗,H k

‖h∗‖Ck,α β

+ ∑

> k

|Hk|ge ,

où l’infimum est pris sur les ( h∗, H k) satisfaisant h = h∗ + ∑ 

> k

χAk (t,ε )Hk (ou h =

h∗ + ∑ 

> k

χBe(ε)Hk sur Mo ou Nj ), pour Hk des 2-tenseurs constants à trace nulle sur R4/Γk.

Définition 4.25 (Norme ‖.‖rC k,α β, ∗

sur les champs de vecteurs) . Soit X un champ de vecteurs sur sur ( M, g D), ( Mo, g o) ou ( N, g b). On définit sa norme rC k,α β, ∗ , où r

est la fonction rD, ro ou rb correspondante par 

‖X‖rC k,α β, ∗

:= inf 

> X∗,X k

‖X∗‖rC k,α β

+ ∑

> k

‖Xk‖rC 00 (ge),

où l’infimum est pris sur les ( X∗, X k) satisfaisant X = X∗ + ∑ 

> k

χAk (t,ε )Xk (ou 

X = X∗ + ∑ 

> k

χBe(ε)Xk sur Mo ou Nj ). 

Remarque 4.26 . Par définition des normes à poids, sur un orbifold compact ou ALE, les décompositions h = h∗ + ∑ 

> k

χBe(ε)Hk et X = X∗ + ∑ 

> k

χBe(ε)Xk sont uniques et déterminées respectivement par les limites de h et de Xk 

> r

lorsque r → 0(où r = ro ou r = rb), sinon la norme diverge. 

Remarque 4.27 . Par définition, on a 

‖.‖Ck,α β, ∗

6 ‖.‖Ck,α β

, et ‖.‖rC k,α β, ∗

6 ‖.‖rC k,α β

,

et les espaces ( Ck,α β, ∗ , ‖.‖Ck,α β, ∗

) et ( rC k,α β, ∗ , ‖.‖rC k,α β, ∗

) sont clairement de Banach. 

1.5.1 Estimations dans ces normes 

Montrons qu’il est possible de contrôler en normes rmCk,α β les images par les opérateurs P et δδ ∗ d’éléments de rmCk,α β, ∗ .

Proposition 4.28. Soient 0 < β < 1, (M•, g •), un des espaces (Mo, g o), (Nj , g bj )

ou (M, g D), g une métrique, h un 2-tenseur symétrique et X un champ de vecteurs 140 Chapitre 4. Désingularisation de métriques d’Einstein 

sur M•. On a alors les contrôles suivants : 

‖Pg• h‖r−2   

> •Cαβ(g•)

6 C‖h‖C2,α β, ∗ (g•),

‖δg• δ∗ 

> g•

X‖r−1   

> •C1,α β(g•)

6 C‖X‖r•C3,α β, ∗ (g•),

‖Pg(h) − Pg• (h)‖r−2   

> •Cαβ(g•)

6 C‖g − g•‖C2,α β, ∗ (g•)‖h‖C2,α β, ∗ (g•),

et 

‖δgδ∗ 

> g

(X) − δg• δ∗ 

> g•

(X)‖r−1   

> •C1,α β(g•)

6 C‖g − g•‖C2,α β, ∗ (g•)‖X‖r•C3,α β, ∗ (g•).

Démonstration. Montrons le résultat pour gD la preuve pour les autres espaces est très similaire. Pour les deux premières inégalités, considérons h un 2-tenseur et X un champ de vecteurs sur M , et des décompositions h = h∗ + ∑ 

> k

χAk (t,ε )Hk

et X = X∗ + ∑ 

> k

χAk (t,ε )Xk. La proposition 4.16 implique que l’on a les contrôles suivants pour h∗ et X∗,

‖PgD h∗‖r−2    

> DCαβ(gD)

6 C‖h∗‖C2,α β (gD ), (4.11) et 

‖δgD δ∗ 

> gD

X∗‖r−1    

> DC1,α β(gD)

6 C‖X∗‖rD C3,α β (gD ). (4.12) Sur R4/Γ, nous avons PeHk = 0 et δeδ∗ 

> e

Xk = 0, et pour tout l ∈ N,

|∇ lχk|gD 6 Clr−lD . (4.13) Donc, grâce au contrôle (4.10) de la différence entre Φ ∗

> k

gD et ge, nous avons 

‖PgD (χAk (t,ε )Hk)‖Cαβ (gD ) 6 C|Hk|ge , (4.14) et 

‖δgD δ∗ 

> gD

(χAk (t,ε )Xk)‖r−1    

> DC1,α β(gD)

6 C‖Xk‖reC00 (ge), (4.15) en tirant en arrière la situation à l’aide du difféomorphisme Φk : Ae(ε−1√

Tj

√tk, ε 

√

Tj ) ⊂ R4/Γk → A k(t, ε ) ⊂ M. 

En sommant les contrôles (4.11) et (4.14) d’une part, et les contrôles (4.12) et (4.15) d’autre part, nous obtenons les deux premières inégalités avec les normes 

C2,α β, ∗ .Intéressons nous maintenant aux deux dernières inégalités qui sont plus dé-1. Espaces fonctionnels 141 licates. Le contrôle que l’on vise est local, écrivons donc l’expression des deux opérateurs en coordonnées dans une base locale ( ei)i. Pour un 2-tenseur h, et un champs de vecteurs X, en notant hij = h(ei, e j ) et Rijkl , les courbures sectionnelles, on a 

Pg(h)ij = 12

(

∇∗

> g

∇gh) 

> ij

− gkp glq Rikjl hpq , (4.16) et, pour ω = g(X, . )(δgδ∗ 

> g

X)i = −12gki ∇k

(

∇iωj + ∇j ωi

)

, (4.17) où ∇i est la dérivée covariante pour g dans la direction ei. On voit alors directement grâce aux estimations de la proposition 4.16 que l’on a les contrôles en norme C2,α β :

‖Pg(h) − PgD (h)‖r−2    

> DCαβ(gD)

6 C‖g − gD‖C2,α β (gD )‖h‖C2,α β (gD ),

et 

‖δgδ∗ 

> g

(X) − δgD δ∗ 

> gD

(X)‖r−1    

> DC1,α β(gD)

6 C‖g − gD‖C2,α β (gD )‖X‖rD C3,α β (gD ).

Afin d’obtenir un contrôle en norme C2,α β, ∗ , après avoir noté que la norme C2,α 

> 0

est majorée par la norme C2,α β, ∗ , la remarque cruciale est alors que dans (4.16), tous les termes font au moins intervenir une dérivée de h ou de g − gD. On a donc le contrôle plus précis sur h un 2-tenseur à support dans Ak(t, ε 0), 

∥∥∥Pg(h) − PgD (h)∥∥∥r−2    

> DCαβ(gD)

6C

(

‖g − gD‖C2,α   

> 0(gD)

‖∇ 2h‖r−2   

> DCαβ(gD)

+ ‖∇ (g − gD)‖r−1   

> DC1,α β(gD)

‖∇ h‖r−1   

> DC1,α β(gD)

+ ‖∇ 2(g − gD)‖r−2   

> DCαβ(gD)

‖h‖C2,α   

> 0(gD)

)

(remarquer les normes C2,α  

> 0

(gD) qui sont majorées par la norme C2,α β, ∗ ). Il reste à contrôler les dérivées des troncatures de 2-tenseurs constants pour montrer que les termes ‖∇ h‖r−2    

> DCαβ(gD)

et ‖∇ 2h‖r−2    

> DCαβ(gD)

sont contrôlés par ‖h‖C2,α β,x (gD )

et de même pour g − gD. Considérons donc χAk (t,ε )Hk où Hk est constant sur R4/

Γk. Comme Hk est constant sur R4, on a ∇eHk = 0, puis, comme les fonctions de coupures sont bornées en norme C20 (gD) par (4.13), pour i ∈ { 1, 2}, on a 

‖∇ i(χAk (t,ε )Hk)‖r−iD C2−i,α β (gD ) 6 C|Hk|ge ,

ce qui suffit pour conclure pour les 2-tenseurs. 142 Chapitre 4. Désingularisation de métriques d’Einstein Pour les champs de vecteurs, nous avons la réécriture suivante, pour X un champ de vecteurs à support dans Ak(t, ε 0)

∥∥∥δgδ∗ 

> g

(X) − δgD δ∗ 

> gD

(X)∥∥∥r−1    

> DC1,α β(gD)

6 C(∥ ∥∥(δg − δgD )( LX g)∥∥∥r−1   

> DC1,α β(gD)

+

∥∥∥δgD (LX (gD − g)) 

∥∥∥r−1   

> DC1,α β(gD)

)

.

Soit Xk dans le noyau linéaire de δeδ∗ 

> e

, alors le 2-tenseur LXk ge est constant et pour Hk un 2-tenseur symétrique constant nous avons δge (LXk Hk) = 0 sur R4.Nous en déduisons alors l’inégalité annoncée pour les champs de vecteurs après un argument similaire à celui pour l’opérateur P .

1.5.2 Estimations elliptiques 

Des estimations elliptiques sont toujours valables dans ces normes. 

Proposition 4.29. Soit 0 < β < 1, g une métrique, h un 2-tenseur symétrique et X un champ de vecteurs sur Mo (respectivement Nj , ou M ). Alors, il existe 

ε∗ = ε∗(go, g bj , g D, β ) > 0 et C > 0 tels que si l’on a ‖g − g•‖C2,α β, ∗ (g•) 6 ε∗, où g•

est l’une des normes go, gbj ou gD, alors, 

‖h‖C2,α β, ∗ (g•) 6 C(

‖Pgh‖r−2   

> •Cαβ(g•)

+ ‖h‖C0

> β, ∗(g•)

)

,

et 

‖X‖r•C3,α β, ∗ (g•) 6 C(

‖δgδ∗ 

> g

X‖r−1•C1,α β (g•) + ‖X‖r•C0

> β, ∗(g•)

)

.

Démonstration. Soit g• une des métriques go, gbj ou gD, et pour tout k, Hk un 2-tenseur constant à trace nulle sur R4/Γk, et Xk un champ de vecteurs linéaire du noyau de δδ ∗ sur R4/Γk. Soient de plus h∗ un 2-tenseur de C2,α β (g•) et X∗

un champ de vecteurs de r•C3,α β (g•), et définissons h = h∗ + ∑ 

> k

χAk (t,ε )Hk et 

X = X∗ + ∑ 

> k

χAk (t,ε )Xk.On a alors les contrôles suivants : 

‖Pg• (χAk (t,ε )Hk)‖r−2   

> •Cαβ(g•)

6 C|Hk|ge ,

et 

‖δg• δ∗ 

> g•

(χAk (t,ε )Xk)‖r−1   

> •C1,α β(g•)

6 C‖Xk‖reC00 (ge).

Ainsi, pour h∗, on a 

‖Pg• h∗‖r−2 

> •Cαβ

6 ‖Pg• h‖r−2   

> •Cαβ(g•)

+ C ∑

> k

|Hk|ge ,2. Jauge divergence réduite 143 et l’estimation annoncée pour g = g• est alors une conséquence des estimations elliptiques dans les espaces à poids du lemme 4.17 qui donnent 

‖h∗‖C2,α β (g•) 6 C(

‖Pg• h∗‖r−2   

> •Cαβ(g•)

+ ‖h∗‖C0 

> β(g•)
> )

,

et permettent de conclure que 

‖h‖C2,α β, ∗ (g•) 6 C′(

‖Pgh‖r−2   

> •Cαβ(g•)

+ ‖h‖C0

> β, ∗(g•)
> )

.

Le même argument marche pour l’opérateur δδ ∗ sur les champs de vecteurs à l’aide des estimations elliptiques du lemme 4.18. La proposition 4.28 permet enfin de passer de la métrique g• à une métrique g

telle que ‖g − g•‖C2,α β, ∗ (g•) 6 ε∗.

# 2 Jauge divergence réduite 

Lorsque l’orbifold d’Einstein que l’on approche est à courbure scalaire néga-tive, on peut toujours mettre nos métriques en jauge de Bianchi à l’aide d’un petit difféomorphisme (voir [Biq13, Lemme 8.2] adapté à nos normes). Lorsque la courbure de Ricci de notre variété d’Einstein n’est pas négative, ce n’est plus nécessairement vrai, mais la mise en jauge divergence, elle, est toujours possible. C’est l’objet de cette sous-section dont le résultat principal est la proposition 4.39 qui généralisera le théorème 1.16 au cas des métriques au voisinage d’une métrique singulière. Le principe est le même que dans la section 3.2.2 du premier chapitre, et les analogues des métriques gv sont les différentes métriques de désingularisation naïve gD que l’on interprète comme des déformations de l’orbifold ( Mo, g o). Pour cette mise en jauge, nous proposons une approche par théorème du point fixe de Banach qui nécessite l’étude de l’équation linéarisée : 

δδ ∗X = −δh, 

où X est un champ de vecteurs, et h un 2-tenseur. Dans notre cadre de dégénérescence et d’espaces à poids particuliers on sou-haite obtenir des estimations indépendantes des échelles de recollement des dif-férents espaces. Une difficulté est que l’orbifold limite pourrait avoir avoir des champs de Killing qui ne se prolongent pas aux bulles se formant. L’opérateur δδ ∗

prendrait alors des valeurs arbitrairement petites sur ces champs de vecteurs, et 144 Chapitre 4. Désingularisation de métriques d’Einstein on ne pourrait pas espérer obtenir de contrôles. La mise en jauge pourrait donc complètement perturber nos métriques dans les normes ‖.‖C2,α β, ∗

.

2.1 Noyau de la linéarisation 

Intéressons nous à l’opérateur δδ ∗ sur un cône plat ( R4/Γ, g e) puis sur un orbifold ( Mo, g o) et sur des orbifolds Ricci-plats ALE ( Nj , g bj ). 

Sur un cône plat. Étudions tout d’abord l’opérateur δδ ∗ sur les 1-formes d’un cône plat. Sur le cône plat ( R4/Γ, g e) = ( R+ ×S3/Γ, dr 2 +r2gS ), comme utilisé dans [CT94, Section 2], toute 1-forme sur R4/Γ se décompose en somme de 1-formes d’un des deux types suivants préservés par δδ ∗ :1. p(r)ψ, où δS ψ = 0, et d∗ 

> S

dS ψ = μψ ,2. r−1l(r)ϕdr + u(r)rd S ϕ, et d∗ 

> S

dS ϕ = νϕ ,où u, p, l : R+ → R, ϕ : S3/Γ → R et où ψ est une 1-forme sur S3/Γ. D’après [AV12], grâce au calcul des valeurs propres de l’opérateur de Laplace-Beltrami et du laplacien de Hodge sur les 1-formes de la sphère de [Fol89, Theorem C], les solutions de δeδ∗ 

> e

ω = 0 s’écrivent alors comme des sommes de 1-formes des types suivants 1. ra± 

> j

ψ avec a± 

> j

:= ±(1 + j), j ∈ N∗,2. rb± 

> j

dS ϕ + b± 

> j

rb± 

> j−1

ϕdr , ou 2 rb± 

> j+2

dS ϕ + b∓ 

> j

rb± 

> j+1

ϕdr , avec b± 

> j

= −1 ± (1 + j), 

j ∈ N.Comme nous sommes intéressés par la résolution d’une équation du type 

δδ ∗X = −δh, 

où X est un champ de vecteurs, et h un 2-tenseur appartenant à C2,α β, ∗ , nous chercherons naturellement X dans rDC3,α β, ∗ . Les poids critiques de δeδ∗ 

> e

sont les valeurs γ ∈ R telles qu’il existe une 1-forme homogène en rγe annulant δeδ∗ 

> e

. Nous sommes donc intéressés par les poids critiques autour du poids 1 des champs de vecteurs linéaires du noyau de δeδ∗ 

> e

.

Lemme 4.30. Sur (R4/Γ) \{ 0} pour Γ 6 = {Id }, 1 est le seul poids critique entre 

−3 et 2.Démonstration. D’après la discussion précédant le lemme, les poids critiques sont a priori de la forme a± 

> j

− 1 = −1 ± (1 + j) pour j ∈ N∗, b± 

> j

− 1 = −2 ± (1 + j)avec j ∈ N, ou b± 

> j

+ 1 = ±(1 + j) avec j ∈ N. Remarquons pour commencer que 2. Jauge divergence réduite 145 

a± 

> j

− 1 ∈ (−3, 2) pour j ∈ N∗ implique que a± 

> j

− 1 = 1, pour les tenseurs de la forme ra± 

> j

ψ, il n’y a donc pas de poids critique de ce type autre que 1 entre −3 et 2. Pour les poids b± 

> j

− 1, il y a a priori aussi le poids 0 et le poids −1 dans ( −3, 2), et pour b± 

> j

− 1, il y a −1 et −2. Ces valeurs ne peuvent cependant pas apparaître sur un cône plat R4/Γ pour Γ 6 = {Id }. En effet, les valeurs b± 

> j

−1 = 0 et b± +1 = −2n’apparaissent que si −3 est valeur propre de l’opérateur de Laplace-Beltrami sur la section du cône, or ce n’est pas possible sur S3/Γ car il n’existe pas de fonction linéaire Γ-invariante sur R4. Pour écarter les valeurs b± 

> j

− 1 = −1 et b± 

> j

+ 1 = −1(qui est la valeur critique pour effectuer certaines intégrations par parties dans la suite), il faut utiliser la forme des solutions. Dans le premier cas, b± 

> j

= 0 donne 

rb± 

> j

dS ϕ + b± 

> j

rb± 

> j−1

ϕdr = dS ϕ, 

pour ∆ S ϕ = 0, et donc ϕ constante, puis dS ϕ = 0. Dans le second cas l’égalité 

b± 

> j

= −2, et donc b∓ 

> j

= 0, donne 2rb± 

> j+2

dS ϕ + b∓ 

> j

rb± 

> j+1

ϕdr = dS ϕ, 

pour ∆ S ϕ = 0, et donc ϕ constante, puis dS ϕ = 0. Les champs de vecteurs posant problème dans les zones annulaires sont alors les champs de vecteurs duaux des 1-formes solutions à croissance linéaires (de poids critique 1) de δeδ∗ 

> e

ω = 0. Elles sont sommes de 1-formes des 3 types suivants : 1. r2ψ, où ψ est le dual d’un champ de vecteurs de Killing sur S3,2. rdr , (associés à la valeur propre ν = 0), 3. 2 rϕdr + r2dS ϕ, (associés à la valeur propre ν = 8). 

Sur un orbifold ou un espace ALE. Comme il n’y a pas de poids critique autre que 1 dans ( −3, 2), nous avons le résultat suivant sur un orbifold ALE. 

Proposition 4.31. Soit (N, g b) un orbifold Ricci-plat ALE. Pour 0 < β < 1,l’opérateur 

δgb δ∗ 

> gb

: rbC3,α β, ∗ → r−1 

> b

C1,α β

est bijectif. Soit (Mo, g o) un orbifold d’Einstein compact. Pour 0 < β < 1, l’opérateur 

δgo δ∗ 

> go

: roC3,α β, ∗ → r−1 

> o

C1,α β146 Chapitre 4. Désingularisation de métriques d’Einstein 

est Fredholm et son noyau et son conoyau sont restreints à Ko l’ensemble des champs de vecteurs de Killing de (Mo, g o).Démonstration. Pour les singularités orbifolds, nous allons dans un premier temps autoriser nos tenseurs à être en r1−β pour 0 < β < 1 aux singularités, plutôt que d’être dans des espaces rC 3,α β, ∗ pour utiliser la théorie des opérateurs elliptiques dans des espaces de Hölder à poids (voir [PR78, Chapter 2]). Considérons tout d’abord un orbifold d’Einstein ( Mo, g o) et l’opérateur δgo δ∗ 

> go

: roC3,α  

> −β

→ r−1 

> o

C1,α  

> −β

.Son noyau est composé des champs de vecteurs de Killing de go que l’on notera 

Ko car si pour X ∈ roC3,α  

> −β

on a δgo δ∗ 

> go

X = 0, en intégrant par parties contre X,on obtient 0 = 

∫

> Mo

〈δgo δ∗ 

> go

X, X 〉dvo

=

∫

> Mo

|δ∗ 

> go

X|2 

> go

dvo + lim 

> r→0

∫

> {ro=r}

δ∗ 

> go

X(n, X )=

∫

> Mo

|δ∗ 

> go

X|2 

> go

dvo,

où n = ∇ro 

> |∇ ro|

, car le terme de bord qui est de la forme lim r→0(O(r−β+1 −β+3 )) s’annule. De même, son conoyau est égal au noyau de δgo δ∗ 

> go

sur r−3 

> o

C1,α β qui est aussi réduit à Ko car il n’y a pas de poids critique entre −3 et 1. Sur un orbifold ALE ( N, g b), supposons qu’un champ de vecteurs X ∈ r1−βb C3,α 

> 0

satisfasse δgb δ∗ 

> gb

X = 0. Comme il n’y a pas de poids critique entre −3 et 1, nous avons en fait X = O(rb) quand rb → 0 aux points singuliers de ( N, g b), et X =

O(r−3 

> b

) à l’infini. Considérons alors l’intégration par parties suivante 0 = 

∫

> N

〈δgb δ∗ 

> gb

X, X 〉dvb

=

∫

> N

|δ∗ 

> gb

X|2 

> gb

dvb − lim ρ→∞ 

∫

> {rb=r}

δ∗ 

> gb

X(n, X ) + lim 

> r→0

∫

> {rb=ρ}

δ∗ 

> gb

X(n, X )=

∫

> N

|δ∗ 

> gb

X|2 

> gb

dvb.

En effet, le terme de bord s’annule car c’est la somme de la limite pour rb → ∞ d’un 

O(|X|gb |∇ X|gb r3 

> b

) = O(r−4 

> b

) et de la limite quand rb → 0 d’un O(|X|gb |∇ X|gb r3 

> b

) = 

O(r4 

> b

). Nous en déduisons donc que δ∗ 

> gb

X = 0, puis comme gb est Ricci-plate, (

δb + 

> 12

dtr b

)

δ∗ 

> gb

X = ∇∗ 

> b

∇bX = 0, ce qui implique que ∇bX = 0 par intégration par parties contre X, et finalement, que X est parallèle sur N . Comme X tend vers 0 à l’infini, nous avons X = 0. L’opérateur δgb δ∗ 

> gb

: r1−βb C3,α  

> 0

→ r−1−βb C1,α  

> 0

est donc injectif. 2. Jauge divergence réduite 147 Le conoyau de l’opérateur autoadjoint δgb δ∗ 

> gb

: r1−βb C3,α  

> 0

→ r−1−βb C1,α  

> 0

est égal au noyau de δgb δ∗ 

> gb

sur r−3+ βb C1,α  

> 0

qui est aussi réduit à {0} car il n’y a pas de poids critiques entre −3 + β et 1 − β. L’opérateur δgb δ∗ 

> gb

: r1−βb C3,α  

> 0

→ r−1−βb C1,α  

> 0

est donc bijectif. Passons finalement aux opérateurs 

δgo δ∗ 

> go

: roC3,α β, ∗ → r−1 

> o

C1,α β

et 

δgb δ∗ 

> gb

: rbC3,α β, ∗ → r−1 

> b

C1,α β .

Comme les espaces rbC3,α β, ∗ et roC3,α β, ∗ ne sont respectivement que la somme directe de rbC3,α β et roC3,α β avec un espace de dimension fini composé des troncatures de champs de vecteurs de linéaires, l’image reste bien fermée et de codimension finie. Nous pouvons être plus précis en remarquant que 

δgo δ∗

> go

(

roC3,α β, ∗

)

= δgo δ∗

> go

(

roC3,α 

> −β

)

∩ r−1 

> o

C1,α β .

En effet, nous avons δgo δ∗

> go

(

roC3,α β, ∗

)

⊂ δgo δ∗

> go

(

roC3,α 

> −β

)

∩ r−1 

> o

C1,α β car roC3,α β, ∗ ⊂ roC3,α 

> −β

et grâce à la proposition 4.28, et réciproquement, si pour X ∈ roC3,α  

> −β

nous avons 

δgo δ∗ 

> go

X ∈ r−1 

> o

C1,α β , alors, comme le seul poids critique entre 1 − β et 1 + β est 1 et correspond au noyau linéaire de δeδ∗ 

> e

, nous avons X ∈ roC3,α β, ∗ . De même, nous concluons que 

δgb δ∗

> gb

(

rbC3,α β, ∗

)

= δgb δ∗

> gb

(

r1−βb C3,α 

> 0

)

∩ r−1 

> b

C1,α β ,

et finalement, δgo δ∗ 

> go

: roC3,α β, ∗ → r−1 

> o

C1,α β est Fredholm avec Ko comme noyau et conoyau, et δgb δ∗ 

> gb

: rbC3,α β, ∗ → r−1 

> b

C1,α β est bijectif. 

2.2 Contrôle de l’inverse de la linéarisation 

Lemme 4.32. Soit 0 < β < 1 et 0 < α < 1, alors, il existe Co > 0 et εo > 0

dépendant de go tels que si ‖g − go‖C2,α β, ∗ (Mo) 6 εo alors l’opérateur 

δgδ∗ 

> g

: K⊥ 

> o

∩ roC3,α β, ∗ (go) → r−1 

> o

C1,α β (go)

est injectif et on a plus précisément pour tout champ de vecteurs X ∈ K⊥ 

> o

sur Mo

‖X‖roC3,α β, ∗ (go) 6 Co‖δgδ∗ 

> g

X‖r−1  

> oC1,α β(go)

.148 Chapitre 4. Désingularisation de métriques d’Einstein 

Il existe aussi Cj > 0 et εj > 0 dépendant de gbj tels que si ‖g−gbj ‖C2,α β, ∗ (Nj ) 6 εj

alors l’opérateur 

δgδ∗ 

> g

: rbj C3,α β, ∗ (gbj ) → r−1 

> bj

C1,α β (gbj )

soit injectif et tel que l’on ait pour tout champ de vecteurs X sur Nj ,

‖X‖rbj C3,α β, ∗ (gbj ) 6 Cj ‖δgδ∗ 

> g

X‖r−1   

> bjC1,α β(gbj)

.

Démonstration. Remarquons pour commencer que si X ∈ roC3,α β, ∗ (go), alors l’or-thogonalité à Ko est bien définie et définit un fermé de roC3,α β, ∗ (go). Il suffit alors d’observer que pour une autre métrique g sur Mo et pour tout X ∈ roC3,α β (go), on a le contrôle 

∥∥∥(

δgo δ∗ 

> go

− δgδ∗

> g

)

X∥∥∥r−1   

> oC1,α β(go)

6 C‖g − go‖C2,α β, ∗ (Mo)‖X‖roC3,α β, ∗ (go)

par la proposition 4.28, et le même argument donne un contrôle similaire pour les métriques gbj . Nous pouvons alors utiliser le lemme 1.60 pour contrôler les inverses des deux opérateurs et conclure. Ces contrôles se répercutent sur les arbres de singularités avec des paramètres de recollement suffisamment petits. Nous approchons pour cela le noyau Ko sur notre désingularisation naïve ( M, g D) de la manière suivante. Pour tout Xo ∈ Ko,d’après la remarque 4.26, sur un orbifold, il existe une unique décomposition 

Xo = Xo, ∗ + ∑

> k

χBo(pk ,ε 0)Xo,k ,

où ∑ 

> k

χBo(pk ,ε 0) = χ(ε−10 ro), telle que ‖Xo‖roC3,α β, ∗

= ‖Xo, ∗‖roC3,α β

+ ∑ 

> k

‖Xo,k ‖reC00

(toutes les autres décompositions donnant une norme infinie). On définit alors ˜ Ko

comme l’espace vectoriel des champs de vecteurs sur M de la forme ˜Xo,t := χM 16 to Xo, ∗ + ∑

> k

χAk (t,ε 0)Xo,k ,

pour Xo ∈ Ko, où χM 16 to est la fonction de troncature de la définition 3.6. Nous avons alors ˜ Xo,t = Xo sur M 16 to .

Remarque 4.33 . Par régularité elliptique sur Mo, les normes L2, rDC3,α β, ∗ et r−1 

> D

C1,α β

sont équivalentes sur l’espace Ko. Comme la norme C40 des fonctions de coupure est bornée, on en déduit que pour ε et tmax assez petits, les normes L2, rDC3,α β, ∗ et 

r−1 

> D

C1,α β sont équivalentes sur ˜ Ko.2. Jauge divergence réduite 149 

Définition 4.34 (Jauge divergence réduite) . Nous définissons l’opérateur de di-vergence réduite , ˜δg := π ˜K⊥ 

> o

δg, où π ˜K⊥ 

> o

est la projection orthogonale L2(gD) sur ˜K⊥ 

> o

. On dira qu’une métrique g1 est en jauge divergence réduite par rapport à une métrique g2 si ˜δg2 g1 = 0. Remarquons tout d’abord que l’opérateur ˜δgD est en fait très proche de δgD

pour un arbre suffisamment dégénéré. 

Lemme 4.35. Sur M , les opérateurs ˜δgD et δgD sont proches, et plus précisément, il existe C > 0 tel que pour tout 2-tenseur h ∈ C2,α β, ∗ (gD), on ait, 

∥∥∥(˜δgD − δgD )h∥∥∥r−1    

> DC1,α β(gD)

6 Ct max ‖h‖C2,α β, ∗ (gD ). (4.18) 

Démonstration. D’après la remarque 4.33, pour montrer le résultat, il suffit de montrer que la projection L2 sur ˜ Ko de δgD h est petite. Nous procédons naturel-lement par intégration par parties. Soit ˜ Xo,t ∈ ˜Ko pour Xo ∈ Ko. Nous avons, 

∣∣∣∣∫

> M

(δgD h)( ˜Xo,t 

)

dvgD

∣∣∣∣ =

∣∣∣∣∫

> M

〈h, δ ∗ 

> gD

( ˜ Xo,t )〉gD dvgD

∣∣∣∣,

or, on a δgD = δgo sur M 16 to ⊂ M to, et donc, comme δ∗ 

> go

Xo = 0, 

δ∗ 

> gD

( ˜ Xo,t ) = δ∗ 

> go

(( χM 16 to − 1) Xo, ∗) + δ∗

> go

( ∑

> k

(χAk (t,ε 0) − χBo(pk ,ε 0))Xo,k 

)

+ (

δ∗ 

> go

− δ∗

> gD

)( ∑

> k

χAk (t,ε 0)Xo,k 

)

. (4.19) Nous allons contrôler chacun de ces termes. Sur M 16 to , χM 16 to Xo, ∗ est égal à Xo, ∗ sauf sur les anneaux de rayons 2 t14 

> k

et 4 t14 

> k

, et de la même manière χAk (t,ε 0) − χBo(pk ,ε 0)

est à support dans ε−10

√tk < r D < 2ε−10

√tk, les fonctions de coupure satisfont pour tout ε−1

> o

√tk < r < ε o et pour tout l ∈ N∗, il existe Cl > 0 tel que si l’on note 

1A la fonction indicatrice d’un ensemble A,

rl|∇ lχM r4 

> o

|go 6 Cl1{r<r D <2r},

pour les champs de vecteurs, nous avons 

rlD

(

|∇ lXo, ∗|go +

∣∣∣∣∇l ∑

> k

Xo,k 

∣∣∣∣go

)

6 Cl‖Xo‖roClβ, ∗ rD,150 Chapitre 4. Désingularisation de métriques d’Einstein et enfin pour les métriques, nous avons 

rlD

∣∣∣∇l(

gD − go

)∣ ∣∣go

6 Cl1{rD <t  

> 14
> k}

(

r2 

> D

+ t2

> k

r−4

> D

)

,

On déduit alors de la proposition 4.16 que l’on a les contrôles suivants sur les termes de (4.19), 

|δ∗ 

> gD

(( χM 16 to − 1) Xo, ∗)|go 6 C‖Xo‖roC10 (go), (4.20) et que sur l’anneau de rayons ε−10

√tk < r D < 2ε−10

√tk,

∣∣∣∣δ∗

> go

( ∑

> k

(

χAk (t,ε 0) − χBo(pk ,ε 0))Xo,k 

)∣ ∣∣∣ 6 C1{ε−10   

> √tk<r D<2ε−10
> √tk}

‖Xo‖roC10 (go), (4.21) et 

∣∣∣∣(

δ∗ 

> go

− δ∗

> gD

)( ∑

> k

χAk (t,ε 0)Xo,k 

)∣ ∣∣∣ 6 C1{ε−10   

> √tk<r D<t
> 14
> k}

t2

> k

r−4 

> D

‖Xo‖roC10 (go). (4.22) Enfin, comme nous avons pour C > 0 indépendant de t, Vol ge

(

Ae

(

t14 

> k

, 2t14

> k

)) 

6

Ct max ,, Vol ge

(

Ae

(

ε−10

√tk, 2ε−10

√tk

)) 

6 Ct 2

> k

, et 

∣∣∣ ∫    

> {ε−10
> √tk<r D<t
> 14
> k}

t2

> k

r−4 

> D

.r 3

> D

dv ge

∣∣∣ 6

Ct 2 

> k

log tk, nous pouvons intégrer les contrôles (4.20), (4.21) et (4.22) des différents termes de (4.19), pour obtenir 

∣∣∣∣∫

> M

〈δgD h, ˜Xo,t 〉gD dvgD

∣∣∣∣ 6 Ct max ‖h‖C00 (gD )‖Xo‖roC00 (go).

On en déduit finalement qu’en notant ˜ Yo,t = πKo δgD h, nous avons ˜δgD h = π ˜K⊥ 

> o

δgD h =

δgD h − ˜Yo,t avec 

‖ ˜Yo,t ‖r−1    

> DC1,α β(gD)

6 Ct max ‖h‖C00 (gD ),

par l’équivalence des normes de la remarque 4.33. 

Remarque 4.36 . Nous avons aussi le contrôle en norme rDCl,α β, ∗(gD) pour tout l par l’équivalence des normes de la remarque 4.33. 

Lemme 4.37. Soient 0 < β < 1, 0 < α < 1 et (M, g D = gDt ) une désingularisation naïve d’orbifold d’Einstein compact ou ALE par un arbre de singularités. Alors, il existe τD > 0 et εD > 0 et CD > 0, ne dépendant que de β et des métriques go et 

gbj , tels que pour tmax < τ D, et toute métrique g satisfaisant ‖g −gD‖C2,α β, ∗ (gD ) 6 εD,l’opérateur 

˜δgδ∗ 

> g

: ˜ K⊥ 

> o

∩ rDC3,α β, ∗ (gD) → ˜K⊥ 

> o

∩ r−1 

> D

C1,α β (gD)2. Jauge divergence réduite 151 

soit inversible et que l’on ait pour tout champ de vecteurs X ⊥ ˜Ko sur M ,

‖X‖rD C3,α β, ∗ (gD ) 6 CD‖˜δgδ∗ 

> g

X‖r−1   

> DC1,α β(gD)

.

Démonstration. Soit 0 < ε < ε 1/(2 −β) 

> D

< ε 0 pour εD > 0 et ε que l’on choisira suffisamment petits au cours de la preuve, et supposons que tmax < ε 4 de manière à avoir sur chaque anneau Ak(t, ε ) entre Nk et Nj ou Nk et Mo (auquel cas, on fixera To = 1), l’existence d’un difféomorphisme Φk : Ae(ε−1√

Tj

√tk, ε 

√

Tj ) ⊂ R4/Γk → A k(t, ε ) ⊂ M, 

tel que pour tout 0 < β < 1, il existe C > 0, 

∥∥∥∥Φ∗

> k

gD − ge

∥∥∥∥C2,α β (Ae(ε−1√Tj 

> √tk,ε

√Tj )) 

6 Cε 2−β < Cε D. (4.23) Jusqu’à la fin de la preuve, nous prendrons les notations 

Ak := Ae(ε−1√

Tj

√tk, ε 

√

Tj ) et Ak := Ak(t, ε ).

Nous cherchons donc τD > 0 suffisamment petit pour que si tmax < τ D, il existe 

CD > 0, ne dépendant que des constantes εo > 0, Co > 0, εj , Cj > 0, εe et Ce du lemme 4.32 et de la proposition 4.20, telle qu’on ait pour tout X ⊥ ˜Ko

‖X‖rD C3,α β, ∗ (gD ) 6 CD‖˜δgD δ∗ 

> gD

X‖r−1   

> DC1,α β(gD)

.

D’après l’estimation (4.18), pour tmax suffisamment petit, il suffit d’avoir 

‖X‖rD C3,α β, ∗ (gD ) 6 CD‖δgD δ∗ 

> gD

X‖r−1   

> DC1,α β(gD)

.

Et par les estimations elliptiques du lemme 4.29, il suffit de montrer qu’il existe une constante C′ 

> D

telle que 

‖X‖rD C0  

> β, ∗(gD)

6 C′

> D

‖δgD δ∗ 

> gD

X‖r−1   

> DC1,α β(gD)

.

Les difféomorphismes Φ k : Ak → A k permettent de ramener la situation sur 

R4 et le rapport des rayons extérieur et intérieur des anneaux Ak est ε2t−1/2 

> k

qui est arbitrairement grand pour tmax arbitrairement petit. D’après la proposition 4.20 et grâce aux contrôles de la proposition 4.28, il existe εe > 0 tel que si l’on a ‖Φ∗

> k

gD − ge‖C2,α β, ∗ (Ak ) < ε D < ε e, alors, il existe des champs de vecteurs linéaires 152 Chapitre 4. Désingularisation de métriques d’Einstein 

Xk du noyau de δeδ∗ 

> e

tels que les champs de vecteurs χAk Xk dans les anneaux Ak

satisfassent 

‖Φ∗

> k

X − Xk‖reC3,α      

> 0(A(T1/2
> jt1/4
> k))

6 CeT 12 

> j

t14

> k

(

ε−β tβ

> 4
> k

∥∥∥δge δ∗ 

> ge

Φ∗

> k

X∥∥∥r−1   

> eC1,α β(Ak)

+ 2 ε−1t14 

> k

‖Φ∗

> k

X − Xk‖reC3,α β (Ak )

)

6 2CeT 12 

> j

t14

> k

(

ε−β tβ

> 4
> k

∥∥∥(

δgD δ∗ 

> gD

X)

> |A k

∥∥∥r−1   

> DC1,α β(gD)

+ 2 ε−1t14 

> k

‖(X − χAk Xk)Ak ‖rD C3,α β (gD )

)

(4.24) sur A(√

Tj t1/4 

> k

) := Ae((1 /2) √

Tj t1/4 

> k

, 4√

Tj t1/4 

> k

). Considérons alors la décomposition 

X = X∗ + ∑

> k

χAk Xk (4.25) pour le reste de la preuve. L’objectif est maintenant de montrer qu’il existe une constante CD > 0 telle que 

‖X∗‖rD C3,α β (gD ) + ∑

> k

‖Xk‖reC00 (ge) 6 CD‖δgD δ∗ 

> gD

X‖r−1   

> DC1,α β(gD)

.

Pour ce faire, nous allons nous ramener aux espaces Mo ou Nj où de tels contrôles ont été montrés dans le lemme 4.32. Sur M t/ 16  

> o

, la métrique gD est proche de la métrique go. Plus précisément, 

gD − go est à support dans M t/ 16  

> o

\M 16 to , où sur chaque anneau Ak, 12 t1/4 

> k

< r D <

2t1/4 

> k

, et pour tout l ∈ N, il existe Cl > 0 tel que dans ces zones, on ait 

t l 

> 4
> k

|∇ l(gD − go)|go 6 Clt12 

> k

. (4.26) Comme M 16 to ⊂ M to ⊂ M t/ 16  

> o

, il existe une fonction de coupure χM t/ 16 

> o

à support dans M t/ 16  

> o

telle que χM t/ 16 

> o

≡ 1 sur M to et telle que pour tout l ∈ N, il existe Cl > 0pour lequel dans chaque Ak,

t l 

> 4
> k

|∇ lχM t/ 16 

> o

|gD 6 Cl. (4.27) On définit alors un champ de vecteurs Xo sur Mo par 

Xo := χM t/ 16 

> o

X∗ + ∑

> k∈Ko

χBo(pk ,ε )Xk,2. Jauge divergence réduite 153 où Ko est l’ensemble des k tels que l’anneau Ak ait une intersection non vide avec 

M to.Par construction, on a donc le contrôle suivant en notant Xo, ∗ := χM t/ 16 

> o

X∗,

‖Xo, ∗‖roC3,α β (go) > ‖Xo, ∗‖roC0  

> β(go)

> ‖(X∗)|M to ‖rD C0  

> β(gD)

, (4.28) car on a X∗ = Xo, ∗ sur M to.Sur M t 

> 16
> o

, nous avons, 

δgD δ∗ 

> gD

X = δgo δ∗ 

> go

Xo + δgo δ∗ 

> go

(X − Xo) + (

δgD δ∗ 

> gD

− δgo δ∗

> go

)

X. 

Comme les fonctions de coupures sont bornées en norme C3,α  

> 0

(gD) et C3,α  

> 0

(go) par (4.27), et leurs dérivées à support dans M t/ 16  

> o

\M to, nous avons la borne inférieure suivante grâce à (4.24) et à (4.26) pour C > 0 dépendant de la fonction de coupure, 

∥∥∥(

δgD δ∗ 

> gD

X) 

> |Mt/ 16
> o

∥∥∥r−1    

> DC1,α β(gD)

> ‖δgo δ∗ 

> go

Xo‖r−1  

> oC1,α β(go)

− C∥∥∥(X∗)|M t/ 16   

> o\Mto

∥∥∥rD C3,α β (gD )

− CC 2

∑

> k∈Ko

t12 

> k

‖X‖rD C3,α β, ∗

> ‖δgo δ∗ 

> go

Xo‖r−1  

> oC1,α β(go)

− 2CC e

(∥∥∥(

δgD δ∗ 

> gD

X)

> |A k

∥∥∥r−1   

> DC1,α β(gD)

+ ∑

> k∈Ko

εβ−1t1−β 

> 4
> k

‖(X − χAk (t,ε )Xk)Ak ‖rD C3,α β (gD )

)

− CC 2

∑

> k∈Ko

t12 

> k

‖X‖rD C3,α β, ∗

, (4.29) car la coupure n’est effectuée que sur X∗, donc l’erreur entre X et Xo sur M t/ 16  

> o

est de l’ordre de |Φ∗

> k

(X − χAk (t,ε )Xk)|ge sur Ae((1 /2) √

Tj t1/4 

> k

, 4√

Tj t1/4 

> k

) qui est estimé dans (4.24), et l’erreur entre gD et go est estimée dans (4.26). Maintenant, comme lorsque tmax → 0, nous avons 

‖πKo Xo‖roC3,α β, ∗ (go)

‖Xo‖roC3,α β, ∗ (go)

→ 0car X ⊥ ˜Ko, et en particulier, pour t assez petit, nous avons 

‖Xo‖roC3,α β, ∗ (go) 6 ‖πKo Xo‖roC3,α β, ∗ (go) + ‖πK⊥ 

> o

Xo‖roC3,α β, ∗ (go) 6 2‖πK⊥ 

> o

Xo‖roC3,α β, ∗ (go).154 Chapitre 4. Désingularisation de métriques d’Einstein Par le lemme 4.32 appliqué à πK⊥ 

> o

Xo qui satisfait δgo δ∗ 

> go

(πK⊥ 

> o

Xo) = δgo δ∗ 

> go

Xo, nous avons donc pour tmax suffisamment petit, 

‖Xo‖roC3,α β, ∗ (go) 6 2Co‖δgo δ∗ 

> go

Xo‖r−1  

> oC1,α β(go)

. (4.30) Et donc, grâce à (4.28) et (4.29), pour tmax suffisamment petit, et en notant C′ := 

CC 2 + 2 CoCC eεβ−1 et γ(tmax ) := ∑ 

> k

t12 

> max

+ t1−β 

> 4
> max

, nous avons 

‖(X∗)|M to ‖rD C0   

> β(gD)

+ ∑

> k∈Ko

‖Xk‖reC00 (ge) − C′γ(tmax )‖X‖rD C0 

> β, ∗(gD)

6‖Xo‖roC3,α β, ∗ (go) − C′γ(tmax )‖X‖rD C0 

> β, ∗(gD)

6Co‖δgo δ∗ 

> go

Xo‖r−1   

> oC1,α β(go)

− C′γ(tmax )‖X‖rD C0 

> β, ∗(gD)

62Co(1 + CC e)

∥∥∥δgD δ∗ 

> gD

X

∥∥∥r−1   

> DC1,α β(gD)

. (4.31) Où l’on a successivement utilisé (4.28), (4.30) et (4.29). En effet, sur un orbifold ( Mo, g o), les champs de vecteurs de la décomposition 

Xo = Xo, ∗ + ∑ 

> k∈Ko

χBo(pk ,ε )Xk atteignant l’infimum de la définition de la norme 

‖.‖roC3,α β, ∗

sont déterminés par la limite de r−1 

> o

Xo à chacun des points singuliers d’après la remarque 4.26. Ici, l’infimum est donc bien atteint avec les Xk de la décomposition (4.25). On considère ensuite le champ de vecteurs X1 := X −∑ 

> k∈Ko

χAk Xk qui satisfait pour une certaine constante C > 0, 

‖δgD δ∗ 

> gD

X1‖r−1    

> DC1,α β(gD)

6 C(

‖δgD δ∗ 

> gD

X‖r−1    

> DC1,α β(gD)

+ γ(tmax )‖X‖rD C0 

> β, ∗(gD)

)

(4.32) grâce au contrôle (4.31) de ∑ 

> k∈Ko

‖Xk‖reC00 (ge).Étant donné j ∈ Ko, l’orbifold Ricci-plat ALE ( Nj , g bj ) est recollé à Mo et on peut prolonger le champ de vecteurs X1 = X∗ + ∑ 

> l / ∈Ko

χAl Xl à Nj par 

Xj := χN t/ 16 

> j

X∗ + ∑

> l∈Kj

χBj (pl,ε )Xl,

où Kj est l’ensemble des k 6 = j tels que Ak ait une intersection non vide avec N tj .

Remarque 4.38 . Ce que l’on gagne en considérant X1 plutôt que X, est le fait qu’il n’y ait pas de champ de vecteurs linéaire du noyau de δeδ∗ 

> e

à prolonger à l’infini de Nj . Le champ de vecteurs Xj appartient donc bien à rbj C3,α β, ∗ (gbj ). La métrique gD 

> Tj

est proche de la métrique gbj sur N t/ 16  

> j

, et la différence gD 

> Tj

− gbj2. Jauge divergence réduite 155 est à support dans N t/ 16 

j \N 16 tj , où l’on a 12

√

Tj t14

k < r D = √

Tj rbj < 2√

Tj t14

k

aux points singuliers et 12

√

Tj t− 14

j < r D = √

Tj rbj < 2√

Tj t− 14

j à l’infini, et plus précisément, il existe pour tout l ∈ N, Cl > 0 tel qu’on ait 

t l

> 4

k

∣∣∣∣∇l

( gD

Tj

− gbj

)∣ ∣∣∣gbj

6 Clt12

k , (4.33) et 

t− l

> 4

j

∣∣∣∣∇l

( gD

Tj

− gbj

)∣ ∣∣∣gbj

6 Clt12

j . (4.34) En notant Xj, ∗ := χN t/ 16 

> j

X∗, nous avons 

‖Xj, ∗‖rbj C3,α β (gbj ) > ‖Xj, ∗‖rbj C0 

> β

(gbj ) > ‖X∗‖rD C0 

> β

(gD ), (4.35) et grâce à (4.24) et aux inégalités (4.33) et (4.34), en écrivant 

δgD δ∗

gD X1 = δgbj δ∗

gbj

Xj + δgbj δ∗

gbj

(X1 − Xj ) + (

δgD δ∗

gD − δgbj δ∗

gbj

)

X1,

nous avons 

∥∥∥(

δgD δ∗

gD X1

)

|N t/ 16 

> j

∥∥∥r−1 

> D

C1,α β (gD ) > ‖δgbj δ∗

gbj

Xj ‖r−1 

> bj

C1,α β (gbj )

− 2CC e

(

‖(

δgD δ∗

gD X1

)

|A k

‖r−1 

> D

C1,α β (gD )

+ ∑

k∈Kj

εβ−1t1−β

> 4

k ‖(X∗)Ak ‖rD C3,α β (gD )

)

− CC 2t12

k ‖X1‖rD C3,α β, ∗

− CC 2t12

j ‖X1‖rD C3,α β, ∗

, (4.36) où nous noterons que par définition ‖X1‖rD C3,α β, ∗

6 ‖X∗‖rD C3,α β

+∑

k∈Kj ‖Xk‖reC00 (ge).Grâce au lemme 4.32, qui nous donne 

‖Xj ‖rj C3,α β, ∗ (gbj ) 6 Co‖δgbj δ∗

gbj

Xj ‖r−1 

> j

C1,α β (gbj ),

et grâce au contrôle (4.32), nous avons alors pour une constante C > 0 ne dépen-dant que des constantes annoncées, le contrôle 

‖(X∗)|N tj ‖rD C0 

> β

(gD ) + ∑

k∈Kj

‖Xk‖reC00 (ge) − Cγ (tmax )‖X‖rD C0

> β, ∗

(gD )

6 C∥∥∥δgD δ∗

gD X∥∥∥r−1 

> D

C1,α β (gD ), (4.37) 156 Chapitre 4. Désingularisation de métriques d’Einstein similaire à (4.31). En itérant aux autres orbifolds Ricci-plats ALE, nous obtenons des contrôles analogues à (4.37) sur tous les Nj qui, avec (4.31) sur Mo, donnent le contrôle sur 

M entier. Il existe donc finalement C > 0 dépendant des constantes précédentes, et donc seulement de β, de go et des gbj telle qu’on ait 

‖X∗‖rD C0   

> β(gD)

+ ∑

> k

‖Xk‖reC00 (ge) − Cγ (tmax )‖X‖rD C0 

> β, ∗(gD)

6 C∥∥∥δgD δ∗ 

> gD

X∥∥∥r−1   

> DC1,α β(gD)

et donc le résultat énoncé pour g = gD car M = M t 

> 0

∪ ⋃ 

> j

N tj pour tmax suffisam-ment petit. Pour passer à une autre métrique g proche de gD, il suffit d’utiliser la propo-sition 4.28 pour s’assurer que pour ‖g − gD‖C2,α β, ∗ (gD ) arbitrairement petit, ˜δgδ∗ 

> g

est arbitrairement proche de δgD δ∗ 

> gD

pour la norme d’opérateur sur rDC3,α β, ∗ (gD). Enfin, notons que ( ˜δgD )∗ = δ∗ 

> gD

π ˜K⊥ 

> o

, et donc que ˜δgD δ∗ 

> gD

est autoadjoint sur ˜ K⊥ 

> o

.Son injectivité implique donc sa surjectivité sur la variété compacte ( M, g D). Nous pouvons alors mettre nos métriques en jauge les unes par rapport aux autres grâce à un théorème de point fixe. 

Proposition 4.39. Soient 0 < β < 1 et (M, g D) = ( M, g Dϕ,t ) une désingulari-sation naïve d’un orbifold d’Einstein compact ou ALE, (Mo, g o). Alors, il existe 

εD, τ D, C D > 0 qui ne dépendent que de β et des métriques go et gbj telles que pour 

tmax 6 τD et pour toute métrique g satisfaisant ‖g − gD‖C2,α β, ∗ (gD ) 6 εD, il existe un unique champ de vecteurs X ⊥ ˜Ko sur M pour lequel, 

˜δgD (exp ∗ 

> X

g) = 0 ,

où exp X est le difféomorphisme exp X : x ∈ M 7 → exp gD 

> x

(X(x)) .Nous avons de plus, ‖X‖rD C3,α β, ∗ (gD ) 6 CD‖˜δgD (g − gD)‖r−1   

> DC1,α β(gD)

, et donc, il existe η : R+ → R+ avec lim 0 η = 0 telle qu’on ait 

‖ exp ∗ 

> X

g − g‖C2,α β, ∗ (gD ) 6 η(

‖g − gD‖C2,α β, ∗ (gD )

)

.

Démonstration. Soit g une métrique sur M , satisfaisant ‖g − gD‖C2,α β, ∗

6 ε pour 

ε > 0 que l’on choisira suffisamment petit au cours de la preuve, et définissons l’opérateur Fg : rDC3,α β, ∗ (gD) → r−1 

> D

C1,α β (gD) qui associe à un champ de vecteurs X2. Jauge divergence réduite 157 la 1-forme 

Fg(X) := ˜δ(exp gD X)∗gD g. 

L’objectif est alors de trouver X tel que Fg(X) = 0, ce qui impliquera bien que ˜δgD (exp gD X)∗g = 0 car pour tout difféomorphisme ϕ, nous avons ϕ∗(δgD ϕ∗g) = 

δϕ∗gD g (en appliquant ϕ∗ à gD qui est C∞, nous ne perdons pas de régularité). L’application g 7 → Fg est linéaire, et la linéarisation de FgD autour de zéro est ˜δgD δ∗ 

> gD

qui est inversible entre les orthogonaux de ˜ Ko d’après le lemme 4.37. Il reste alors à contrôler les termes non-linéaires dans nos normes, ce qui est une conséquence du comportement de nos normes par rapport aux opérations habituelles, voir la proposition 4.16. Nous pouvons donc mettre nos métriques en jauge par rapport à gD à l’aide du théorème de point fixe quantitatif énoncé dans le lemme 1.12. Enfin, remarquons que pour un champ de vecteurs linéaire Xk du noyau de δeδ∗ 

> e

,le 2-tenseur δ∗ 

> e

Xk est constant. Cela nous permet de définir, pour toute métrique 

g sur M , une application continue ψg : rDC3,α β, ∗ → C2,α β, ∗ qui à un champ de vecteurs 

X associe le 2-tenseur 

ψg(X) := exp ∗ 

> X

g, 

Cette application est continue car pour tout difféomorphisme ϕ : M → M , nous avons (ϕ∗g)( x)kl = g(ϕ(x)) ij 

∂iϕ∂x k

∂j ϕ∂x l

dans des coordonnées locales et donc, pour tout champ de vecteurs X∗ ∈ rDC3,α β ,le 2-tenseur exp ∗ 

> X

g − g est bien arbitrairement petit en norme C2,α β, ∗ . Pour la partie constante il suffit de remarquer que pour un champ de vecteurs linéaires Xk, le 2-tenseur exp ∗ 

> Xk

ge est constant et | exp ∗ 

> Xk

ge|ge 6 C‖Xk‖reC0 , et plus généralement, que pour Hk constant exp ∗ 

> Xk

Hk est aussi constant avec un contrôle similaire. 

2.3 Métriques d’Einstein en jauge divergence réduite 

L’intérêt de notre mise en jauge divergence réduite est de nous permettre d’uti-liser l’opérateur suivant dont la linéarisation est elliptique contrairement à E.Définissons 

ΦgD (g) := E(g) + δ∗ 

> g

˜δgD g = Ric( g) − R( g)2 g + R( g)4 g + δ∗ 

> g

˜δgD g. 

On remarque que si E(g) = 0, et ˜δgD g = 0, alors ΦgD (g) = 0. Réciproquement, si 

ΦgD (g) = 0, alors E(g) = 0, et ˜δgD g = 0. En effet, E(g) est à divergence nulle par 158 Chapitre 4. Désingularisation de métriques d’Einstein l’identité de Bianchi, et on a donc ˜δgΦgD (g) = ( ˜δgδ∗ 

> g

)˜δgD g, or pour g proche de gD,(˜δgδ∗ 

> g

) est inversible sur l’image de ˜δgD par le lemme 4.37, et donc ˜δgD g = 0. Le noyau de ΦgD décrit donc exactement les métriques d’Einstein en jauge divergence réduite au voisinage de gD = gDϕ,t .

Corollaire 4.40. Soient D0, v 0 > 0, l ∈ N, et β = β(v0, D 0) > 0 obtenu dans le corollaire 4.5. Alors, pour tout ε > 0, il existe δ = δ(ε, D 0, v 0, l ) > 0 tel que si 

(M, g E ) est une variété d’Einstein satisfaisant — le volume est minoré par v0 > 0,— le diamètre est majoré par D0,— la courbure de Ricci est bornée | Ric | 6 3.et telle que pour un orbifold d’Einstein (Mo, g o),

dGH 

> (

(M, g E ), (Mo, g o))

6 δ, 

alors, il existe une désingularisation naïve (M, g D) de (Mo, g o) par un arbre de singularités, et un difféomorphisme ψ : M → M tels que 

> ∥∥∥

ψ∗gE − gD∥∥∥Clβ, ∗(gD ) 6 ε, 

et 