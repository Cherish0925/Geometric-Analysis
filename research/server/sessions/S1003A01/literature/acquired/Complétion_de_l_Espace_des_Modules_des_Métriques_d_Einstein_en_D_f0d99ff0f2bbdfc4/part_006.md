---
retention_scope: session
part: 6
total_parts: 7
---

[Part 6/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

> j

(0) n’étant que des constantes dépen-dant uniquement de la géométrie de ( Mo, g o) et de celle de ( Nk, g bk ), elles doivent nécessairement s’annuler pour que l’inégalité (5.34) soit satisfaite lorsque ti tend vers zéro. En revenant à l’expression des ¯λk0 

> j

(0) nous obtenons l’obstruction que l’on peut écrire en coordonnées géodésiques grâce au corollaire 5.26. On obtient ainsi l’égalité énoncée. 

Remarque 5.33 . La preuve donne un résultat plus fort : si toutes les échelles d’ap-paritions des singularités sont comparables (c’est-à-dire, s’il existe 0 < β < 1 tel que pour tout k, k ′, on ait t5−β 

> 4
> k′,i

< t k,i < t 45−β 

> k′,i

) et qu’il n’y a que des variétés à dé-formations intégrables dans l’arbre de singularités, alors l’obstruction est valable à toutes les singularités de l’orbifold. Nous verrons dans la section suivante que l’on peut montrer généralement que l’obstruction est satisfaite à tous les points singuliers. 

# 3 Obstructions à des désingularisations partielles et totales 

Notre théorème d’existence et d’unicité de la désingularisation d’un orbifold d’Einstein par une métrique d’Einstein modulo obstructions est en fait aussi va-lable pour les désingularisations partielles d’un orbifold. Cela nous permet de découpler plus précisément les influences des différentes bulles. Nous en déduisons principalement dans le corollaire 5.43 que la première obstruction exhibée dans le corollaire 5.32 est valable à tous les points singuliers. 

3.1 Désingularisations naïves partielles et espaces à poids 

Dans la définition 3.3, nous avions défini les désingularisations naïves d’un orbifold d’Einstein ( Mo, g o) par le recollement d’arbres d’orbifolds Ricci-plats ALE (Nj , g bj ). Ici, nous définissons de la même manière des désingularisations partielles en n’imposant pas à la désingularisation d’avoir la topologie d’une variété, mais seulement d’un orbifold “moins singulier” que Mo.On choisit donc So un sous-ensemble des singularités de Mo et pour chaque 

j, Sj un sous-ensemble des singularités de Nj , et les recollements des ALE ne se feront qu’en ces points singuliers et exactement comme dans la définition 3.3. La différence est que l’on obtient ainsi un orbifold singulier aux singularités de Mo\So200 Chapitre 5. Obstructions à la désingularisation et aux singularités de Nj \Sj . En notant S = ( So, (Sj )j ) et M := Mo#j Nj où la combinatoire des recollements est donnée par une configuration de désingulari-sation D (en les points de S seulement), on définit les désingularisations naïves exactement comme dans la définition 3.3. Nous allons aussi adapter les définitions des fonctions ro, rb et rD en reprenant donc les notations de la section 1.1 du chapitre précédent. 

Définition 5.34 (Fonction ro,S o sur un orbifold) . On définit ro,S o une fonction lisse sur Mo satisfaisant ro,S o := Φ ∗

> k

re sur chaque voisinage Uk de pk ∈ So, et telle que sur le reste de Mo, on ait ε0 < r o,S o < 1 (les différents choix possibles seront équivalents pour nos applications). 

Définition 5.35 (Fonction rbj ,S j sur un orbifold ALE) . On définit rbj ,S j une fonc-tion lisse sur Nj satisfaisant rbj ,S j := Ψ ∗

> k

re sur chaque voisinage Uk de pk ∈ Sj ,et rbj ,S j := Ψ ∗∞re sur U∞, et telle que ε0 < r bj ,S j < ε −10 sur le reste de Nj (les différents choix possibles seront équivalents pour nos applications). 

Définition 5.36 (Fonction rD,S sur une désingularisation naïve) . Sur une désin-gularisation naïve ( M, g D), on définit une fonction rD,S de la manière suivante : 1. rD,S = ro,S o sur M to,2. rD,S = √

Tj rbj ,S j sur chaque N tj .La fonction rD,S est lisse sur M .

Espaces de Hölder à poids sur les orbifolds et ALE. Pour les orbifolds, on considérera une norme qui sera bornée pour les tenseurs qui décroissent aux points de So.

Définition 5.37 (Norme à poids sur un orbifold) . Soit β ∈ R, k ∈ N, 0 < α < 1et ( Mo, g o, S o) un orbifold. Définissons alors pour tout tenseur s sur Mo,

‖s‖Ck,α β (go,S o) := sup 

> Mo

r−βo,S o 

> (k∑
> i=0

rio,S o |∇ igo s|go + rk+αo,S o [∇kgo s]Cα(go)

> )

.

Définition 5.38 (Norme à poids sur les orbifolds ALE) . Soit β ∈ R, k ∈ N et 0 < α < 1 sur un orbifold ALE ( N, g b, S ), on définit pour tout tenseur s sur N la norme suivante 

‖s‖Ck,α β (gb,S ) := sup 

> N
> {

max( rβb,S , r −βb,S ) 

> (k∑
> i=0

rib,S |∇ igb s|gb + rk+αb,S [∇kgb s]Cα(gb)

> )}

.

qui est bornée sur les tenseurs décroissant à l’infini et aux points de S.3. Obstruction à tous les points singuliers 201 

Espaces fonctionnels sur les désingularisations partielles. Supposons que (M, g D, S ) soit une désingularisation naïve partielle de ( Mo, g o, S o) par un arbre d’orbifolds Ricci-plats ALE ( Nj , g bj , S j ). Pour tmax suffisamment petit, on définit la norme suivante. 

Définition 5.39 (Norme à poids adaptée aux arbres de singularités) . Soit β ∈ R et 

k ∈ N, 0 < α < 1. On définit pour s ∈ T M ⊗l+ ⊗ T ∗M ⊗l− un tenseur ( l+, l −) ∈ N2,avec l := l+ − l− le poids conforme associé à la section. 

‖s‖Ck,α β (gD ,S ) := ‖χM to s‖Ck,α β (go,S o) + ∑

> j

T l 

> 2
> j

‖χN tj s‖Ck,α β (gbj ,S j ).

Toute l’analyse précédente de cette section concernant des orbifolds avec les poids issus de ro et des rbj est valable avec les ro,S o et rj,S j en utilisant des revête-ments locaux finis aux points singuliers n’appartenant pas à So, ou aux Sj . Nous noterons les différentes constantes en précisant les points de So, Sj ou S où les recollements ont lieu. 

3.2 Résolution de l’équation d’Einstein modulo obstructions pour les désingularisations partielles 

Les singularités orbifolds ne modifiant pas l’analyse en considérant des revête-ments locaux au niveau des points laissés singuliers, la preuve du théorème 4.51 est en fait valable pour les désingularisations partielles d’orbifolds d’Einstein. 

Théorème 5.40. Soient 0 < β < 1, (Mo, g o, S o) un orbifold d’Einstein com-pact ou ALE tel que Ric( go) = Λ go, pour Λ ∈ R, et soit D une configuration de désingularisation partielle par des orbifolds Ricci-plats ALE (Nj , g bj , S j )j .Alors, il existe τ > 0 et ε > 0 ne dépendant que de β et des constantes Co,S o ,

εo,S o , Cj,S j et εj,S j du lemme 4.42, et Ce > 0 et εe > 0 du lemme 4.19 tels que pour toute désingularisation naïve gDS := gDϕ,t ;S , satisfaisant tmax < τ , et ϕ = ( ϕk)k ∈

Isom (R4/Γk)k, et pour tout v ∈ ˜O(gD) satisfaisant ‖v‖C0  

> β, ∗(gD)

< ε , il existe une 

unique solution ˆgv;S = ˆ gϕ,t,v ;S de l’équation 

ΦgDS (ˆ gv;S ) ∈ ˜O(gDS ),

satisfaisant les conditions suivantes : 1. ‖ˆgv;S − gDS ‖C2,α β, ∗

6 2ε,2. ˆgv;S − (gDS + v) est orthogonal à ˜O(gDS ) pour le produit L2 de gDS .202 Chapitre 5. Obstructions à la désingularisation 

De plus, il existe C > 0 indépendant de t et v telle qu’on ait 

‖ˆgv;S − (gDS + v)‖C2,α β, ∗ (gDS ) 6 C(

‖v‖2   

> C2,α β(gDS)

+ t2−β

> 4
> max; S

)

.

3.3 Désingularisations totales et approximations d’Einstein modulo obstructions 

Soit ( Mo, g o) un orbifold d’Einstein et soit p, un de ses points singuliers, dont la singularité est R4/Γ. Définissons alors So le complémentaire de {p} parmi les points singuliers de Mo, soit ( MSo , g DSo ) une désingularisation partielle de ( Mo, g o)ne laissant que le point p singulier et soit ( MSo , ˆgSo ) une perturbation de ( MSo , g DSo +

vSo ) satisfaisant 

ΦgDSo 

(ˆ gSo ) = ˜ o(So) ∈ ˜O(gDSo ).

La métrique ˆ gSo a le développement suivant dans des coordonnées locales où elle est en jauge divergence par rapport à ge

ˆgSo = ge + ˆH2 + O(r3 

> o

) (5.35) où ¯Pe ˆH2 + λg e = ˜Oo, avec ˜ Oo la limite de ˜ o(So) ∈ ˜O(gDSo ) en zéro qui satisfait 

| ˜Oo|ge 6 C‖vSo ‖C00 (go) d’après la proposition 5.22, et où λ = R(ˆ gSo )4 .Soit de plus ( N, g b) un orbifold Ricci-plat ALE asymptotique à R4/Γ, χ une fonction de coupure à support dans un voisinage de l’infini où gb a des coordonnées ALE, et ( oi)i une base orthonormée de O(gb). D’après la proposition 5.25, il existe alors ˆh2 un 2-tenseur sur N asymptotique à ˆH2 et des réels ˆλi tels qu’on ait ¯Pbˆh2 + λg b = χ ˜Oo + ∑

> i

ˆλioi

avec ˆλi = −

∫

> S3/Γ

3〈 ˆH2, O 4 

> i

〉ge + 12O4

> i

(

∇etr e ˆH2, ∂ re

)

dvS3/Γ +

∫

> N

χ〈 ˜Oo, oi〉gb dvb.

Définissons alors ( M, ˆgAp,t ) la métrique obtenue par recollement naïf (définition 3.3) de ( N, g b + tˆh2) à ( MSo , ˆgSo ) à l’échelle t > 0, et ¯ gDv celle du recollement naïf de (N, g b) à ( MSo , ¯gDSo,v o ) à l’échelle t. Nous avons le contrôle suivant. 

Proposition 5.41. Pour tmax = max( tmax ,S o , t ) > 0 suffisamment petit, pour tout 3. Obstruction à tous les points singuliers 203 

k ∈ N il existe des réels ˆλi, Ck > 0 pour lesquels, on a 

∥∥∥π ˜O(gD )⊥ ΦgD (ˆ gAp,t )

∥∥∥r−2    

> DCkβ(gD)

6 Ckt3−β 

> 4

, (5.36) 

et pour tout i0, en notant (˜ oi) la projection de la base orthonormée oi sur ˜O(gD)

〈

ΦgD (ˆ gAp,t ) − t ∑

> i

ˆλi ˜oi, ˜oi0

〉 

> L2(gD)

6 C0t32 , (5.37) 

tout en satisfaisant, 1. ‖ˆgAp,t − gD‖C2,α β, ∗ (gDp,t ) 6 2ε,2. ˆgAp,t − (gD + v) est orthogonal à ˜O(gD) pour le produit L2 de gD.Remarque 5.42 . Ce que l’on gagne donc en passant par des désingularisations partielles est le contrôle en t plutôt que tmax comme dans le corollaire 5.27. 

Démonstration. Sur M 16 tSo , nous avons par hypothèse 

Φgo (ˆ gSo ) = ˜ o(So) = ˜ Oo + O(r2 

> o

) ∈ ˜O(gDSo ), (5.38) et sur N 16 t, nous avons 

Φgb (t(gb + tˆh2)) = χ ˜Oo + t ∑

> i

ˆλioi + O(r2

> D

). (5.39) Maintenant, comme au point p, le développement de ˆ gSo dans des coordonnées locales où elle est en jauge divergence par rapport à ge est ˆgSo = ge + ˆH2 + O(r3 

> o

), (5.40) et que t(gb + tˆh2) a le développement suivant pour t− 14 6 rb 6 t− 14

t(gb + tˆh2) = ge + ˆH2 + O(t2r−2 

> b

+ tr −4 

> b

), (5.41) avec les contrôles adaptés pour les dérivées jusqu’à l’ordre 2, nous avons sur l’an-neau de rayons rD = t14 et rD = 2 t14 ,

ΦgD (ˆ gAp,t ) − ˜o(So) 

> p,t

− t ∑

> i

ˆλi ˜oi = O(

t34

)

, (5.42) où ˜ o(So) 

> p,t

= χMo\B(p,t 1/4) ˜o(So) 

> ∗

+ χAp(ε0) ˜o(So)(p), où A(ε0) est l’anneau ε−10

√t < r D <ε0 entre N et Mo. D’après (5.38), (5.39) et (5.42), nous avons l’estimation (5.36). 204 Chapitre 5. Obstructions à la désingularisation Ensuite, nous avons grâce à (5.41), (5.39) et (5.42), le contrôle 

〈

ΦgD (ˆ gAp,t ) − t ∑

> i

ˆλi ˜oi,t , ˜oi0,t 

〉

> L2(gDp,t )

6 C0t32 . (5.43) En recollant des ¯ gbj ,v j pour vj ∈ ˜O(gD) plutôt que gbj à ˆ gSo,v So , on atteint toutes les jauges gAp,t − (gD + v) ⊥ ˜O(gD) pour v ∈ ˜O(gD) sans détériorer les estimations. D’après le lemme 5.28, la différence entre ˆλi(0) associé à gb et ˆλi(v) associé à ¯ gb,v ,est contrôlée 

|ˆλi(v) − ˆλi(0) | 6 C(

‖v‖C00 (gD ) + ‖ ˆH2‖C02 (go)

)

‖v‖C00 (gD ). (5.44) De plus, grâce au théorème 5.40, en notant ¯H2 les termes quadratiques de go

dans des coordonnées où elle est en jauge divergence par rapport à ge, nous avons les contrôles 

‖ ¯H2 − ˆH2‖C02 (ge) 6 C(

t2−β 

> 4
> max,S o

+ ‖vSo ‖C2,α β, ∗

)

, (5.45) et 

| ˜Oo|ge 6 C(

t2−β 

> 4
> max,S o

+ ‖vSo ‖C2,α β, ∗

)

, (5.46) Finalement, en utilisant ces contrôles et (5.44) et l’expression des obstructions ˆλi, nous obtenons que ˆλi(v) → ¯λi lorsque ( tmax ,S o , v So , v ) → (0 , 0, 0). Ainsi, avec la même preuve que pour le corollaire 5.32 en fixant le point p a priori et en considérant ˆ gAp,t,v plutôt que ¯ gAt,v , nous obtenons le résultat d’obstruction suivant. 

Corollaire 5.43. Soit (Mo, g o) un orbifold d’Einstein, et (Mi, g i)i une suite de va-riétés d’Einstein convergeant vers (Mo, g o) au sens de Gromov-Hausdorff et telle que les éclatements non triviaux convergent vers des variétés Ricci-plates ALE (c’est-à-dire sans formation d’arbre de singularités) dont les déformations infini-tésimales sont intégrables .Alors, pour tout point singulier p ∈ Mo, si l’on note H2 les termes quadratiques du développement de go en coordonnées géodésiques en p, et (O4 

> j

)j une base de 

O4(gb), on a : ∫

> S3

(

3〈H2, O 4 

> j

〉 + O4 

> j

(BeH2, ∂ re ))

dvS3 = 0 .4. Obstruction à la formation d’arbres de bulles connues 205 

# 4 Obstruction à la formation d’arbre d’orbifolds kählériens Ricci-plats 

Rendons notre résultat plus concret en interprétant les obstructions qui appa-raissent lorsqu’une suite de métriques d’Einstein dGH -converge vers un orbifold en faisant apparaître des arbres d’orbifolds Ricci-plats ALE kählériens. Il est parfois conjecturé (dans [BKN89] par exemple) que c’est le cas général. Nous allons voir que la condition sur la courbure det R = 0 aux points singuliers de l’orbifold déjà identifiée dans [Biq13, Biq16] dans le cas de la métrique d’Eguchi-Hanson sous des hypothèses restrictives est en fait générale. Le résultat principal de cette section est le corollaire 5.77. 

4.1 Recollement de la métrique d’Eguchi-Hanson et obstructions 

Nous montrons que quel que soit l’orbifold Ricci-plat ALE kählérien que l’on considère, il y a une obstruction commune à la désingularisation. C’est celle qui ap-paraît au point singulier de l’orbifold dans le cas du recollement d’Eguchi-Hanson décrite dans [Biq13] : det R+ = 0 ,

au point singulier, où R+ est la partie auto-duale de la courbure définie au début du chapitre 2. Génériquement , il y a en réalité des obstructions supplémentaires correspondant à l’annulation totale de la partie auto-duale de la courbure au point singulier : 

R+ = 0 .

Remarque 5.44 . En recollant les bulles avec l’orientation opposée, c’est-à-dire avec un paramètre de recollement dans O(4) \SO (4) l’obstruction commune se réécrit det R− = 0 et donc en général, comme l’équation d’Einstein implique que la courbure est diagonale par blocs dans la somme directe des 2-formes autoduales et anti-autoduales, l’obstruction s’écrit det R = 0 .

Remarque 5.45 . Les orbifolds des exemples 2.6 et 2.7 ne satisfont pas cette obstruc-tion et il n’est donc pas possible de les désingulariser de cette manière. L’orbifold limite de la famille de métriques d’AdS-Taub-Bolt de l’annexe B ou l’orbifold plat 206 Chapitre 5. Obstructions à la désingularisation 

T4/Z2 de l’exemple 2.5 satisfont cette condition. Comme nous l’avons vu dans la section précédente, les premières obstructions à la désingularisation d’un orbifold ( Mo, g o) par une variété Ricci-plate ALE ( N, g b)viennent des déformations infinitésimales décroissant en r−4 

> b

à l’infini. Comme décrit parmi les exemples du chapitre 2, à l’infini la métrique d’Eguchi-Hanson a le développement suivant : 

gEH = ge − 1

r4

> e

(dr 2 

> e

+ r2 

> e

α21 − r2 

> e

α22 − r2 

> e

α23) + O(r−8 

> e

).

Ce comportement asymptotique se généralise à l’espace de modules des métriques Ricci-plates ALE sur T ∗S2 (qui ne sont que des rotations et rééchelonnements de 

gEH ). D’après le théorème 2.14, l’espace de modules des métriques Ricci-plates ALE au voisinage de la variété d’Eguchi-Hanson ( T ∗S2, g EH ) est de dimension 3 et est composé de métriques notées ( gζ )ζ pour ζ = ( ζ1, ζ 2, ζ 3) ∈ R3\{ 0}. De plus, il existe un difféomorphisme Φ ζ d’un voisinage de l’infini de R4\Z2 dans un voisinage de l’infini de T ∗S2 tel que l’on ait Φ ∗ 

> ζ

gζ = ge + hζ + O(r−8 

> e

), où pour tout 

ζ ∈ R3\{ 0},

hζ = − ∑

> j,k,l

ζ2

> j

dr 2 

> e

+ r2 

> e

α2 

> j

− r2 

> e

α2 

> k

− r2 

> e

α2

> l

r4

> e

− ζ1ζ2

r2 

> e

α1.α 2 + redr e.α 3

r4

> e

− ζ1ζ3

r2 

> e

α1.α 3 − redr e.α 2

r4

> e

− ζ2ζ3

r2 

> e

α2.α 3 − redr e.α 1

r4

> e

,

où la somme est prise sur les ( j, k, l ) tels que l ≡ k + 1 ≡ j + 2 mod 3. 

Remarque 5.46 . Toutes les métriques ainsi obtenues pour des différents ζ 6 = 0 sont en fait homothétiques les unes aux autres, et pour la valeur (interdite) ζ = 0, on a ( X0, g 0) = R4/Z2, où la sphère S2 est écrasée en un point. 

Remarque 5.47 . Pour tout ζ, le terme hζ est harmonique homogène, à divergence et trace nulle par rapport à la métrique euclidienne. 

Corollaire 5.48. On a en fait gEH = g(1 ,0,0) , et on retrouve 

h(1 ,0,0) = −dr 2 

> e

+ r2 

> e

α21 − r2 

> e

α22 − r2 

> e

α23

r4

> e

.4. Obstruction à la formation d’arbres de bulles connues 207 

En faisant varier ζ au voisinage de (1 , 0, 0) , on obtient au premier ordre des dé-formations infinitésimales de gEH .Elles sont engendrées par les déformations dans les trois directions ζ1, ζ2 et ζ3,notées o1, o2 et o3 qui ont les développements oi = O4 

> i

+ O(r−8 

> e

)

1. O41 := 2 dr 2      

> e+r2
> eα2
> j−r2
> eα2
> k−r2
> eα2
> l
> r4
> e

,2. O42 := r2 

> eα1.α 2+redr e.α 3
> r4
> e

,3. O43 := r2 

> eα1.α 3−redr e.α 2
> r4
> e

.Remarque 5.49 . Les déformations infinitésimales o1, o2 et o3 ont une interpré-tation géométrique : o1 est infinitésimalement un changement d’échelle à l’infini et o2 et o3 viennent de rotations de l’infini suivant les vecteurs de Killing de S3

respectivement duaux de α3 et α2 (voir la sous-section 6.1 de ce chapitre). 

Remarque 5.50 . Comme les métriques de l’espace de modules autour de gEH lui sont homothétiques, leurs déformations infinitésimales sont simplement O41 , O42 et 

O43 tirées en arrière par un difféomorphisme. 

Reformulation des obstructions. D’après les corollaires 5.32 et 5.43, pour qu’un orbifold d’Einstein puisse être désingularisé au sens de Gromov-Hausdorff par la métrique d’Eguchi-Hanson, il faut que ses termes quadratiques (en coor-données géodésiques par exemple), H2, satisfassent les conditions 

λi = −

> ∫
> S3
> (

3〈H2, O 4 

> i

〉ge + O4 

> i

(Be(H2), ∂ re ))

dvS3 = 0 pour i = 1 , 2, 3. D’après [Biq13], ces conditions peuvent se réécrire comme une condition sur la courbure R(H2), qu’engendrent ces termes d’ordre 2. Plus pré-cisément, on définit R(H2) : Λ 2R4 → Λ2R4 comme l’opérateur de courbure au point 0 commun aux métriques ayant un développement ge + H2 + O(r3 

> e

) en 0. En dimension 4, on a donc toujours la décomposition de la courbure : 

R(H2) =:  

> 

R+(H2) Ric 0(H2)Ric 0(H2) R−(H2) 

> 

.

De plus, l’application H2 7 → R(H2) est linéaire. Si l’on se place dans une jauge radiale, c’est-à-dire si H2(∂re , . ) = 0, on a une décomposition 

H2 = ∑

> ij

Hij βiβj ,208 Chapitre 5. Obstructions à la désingularisation où βi = re2αi. Dans la base naturelle de Ω + composée de ω1 := dx 1 ∧dx 2 +dx 3 ∧dx 4,

ω2 := dx 1 ∧ dx 3 − dx 2 ∧ dx 4 et ω3 := dx 1 ∧ dx 4 + dx 2 ∧ dx 3, on a l’égalité : 

R+(H2) = tr e(H)I3 − 6H

où H est la matrice des Hij .

Remarque 5.51 . De la même manière on obtient la décomposition de R−(H2) à partir de la décomposition de H2 dans une base A∗βi où A est un élément de 

O(4) \SO (4). Pour les déformations oi on obtient les égalités suivantes pour les trois obs-tructions : 

λi = −12

> ∫
> S3
> (

3〈H2, O 4 

> i

〉ge + O4 

> i

(BeH2, ∂ re ))

dvS3 = 〈R+(H2)( ω1), ω i〉.

Corollaire 5.52 ([Biq13, Theorem 4.1]) . Les obstructions 

> ∫
> S3
> (

3〈H2, O i〉ge + O4 

> i

(BeH2, ∂ re ))

dvS3 = 0 

pour i = 1 , 2, 3 contre H2 un 2-tenseur quadratique tel que de Ric H2 = Λ ge sont équivalentes à la condition : 

R+(H2)( ω) = 0 ,

pour ω une 2-forme dépendant de la jauge de recollement. En particulier, on a toujours 

det R+(H2) = 0 .

Manifestement, ces conditions ne dépendent pas particulièrement de la mé-trique d’Eguchi-Hanson, mais des termes O4 

> i

d’ordre −4 des déformations infini-tésimales de la bulle recollée. 

4.2 Autres variétés Ricci-plates ALE kählériennes et obstructions 

Nous avons succinctement décrit les autres variétés Ricci-plates ALE connues dans la section 1.2.4 du chapitre 2. Nous allons maintenant être plus précis et en particulier étudier leurs déformations infinitésimales. 4. Obstruction à la formation d’arbres de bulles connues 209 

Déformations des instantons gravitationnels et obstructions. Étudions maintenant ces déformations pour les orbifolds Ricci-plats ALE connus. Nous en déduirons que l’obstruction est générale. Dans ces prochaines pages, nous repre-nons les notations de la section 1.2.4 du chapitre 2. 

Lemme 5.53 ([Auv18, Theorem 2.1]) . Soit Γ un sous-groupe fini de SU (2) , et soient kΓ ∈ N∗ et DΓ ⊂ R3kΓ du théorème 2.14. Alors, pour chaque ζ = ( ζ1, ζ 2, ζ 3) ∈

(RkΓ )3\DΓ, il existe un difféomorphisme Φζ entre des voisinages des infinis de R4/

Γ et de Xζ tel que Φ∗ 

> ζ

gζ = ge + hζ + O(r−6 

> e

), où, 

hζ = − ∑

> j,k,l

|ζj |2 dr 2 

> e

+ r2 

> e

α2 

> j

− r2 

> e

α2 

> k

− r2 

> e

α2

> l

r4

> e

− 〈 ζ1, ζ 2〉r2 

> e

α1.α 2 − redr e.α 3

r4

> e

− 〈 ζ1, ζ 3〉r2 

> e

α1.α 3 + redr e.α 2

r4

> e

− 〈 ζ2, ζ 3〉r2 

> e

α2.α 3 − redr e.α 1

r4

> e

,

où la première somme est prise sur les (j, k, l ) tels que l ≡ k + 1 ≡ j + 2 mod 3 .Remarque 5.54 . La formule ci-dessus est aussi valable pour les métriques orbifolds avec ζ ∈ DΓ par la proposition 3.14 de [Kro89a]. On en déduit que le recollement de tout orbifold hyperkählérien ALE qui n’est pas plat est obstrué par les obstructions données par les déformations infinitési-males par variation des ζi.

Corollaire 5.55. Soient Γ un sous-groupe fini de SU (2) , et ζ ∈ R3kΓ \DΓ. Alors il existe un difféomorphisme Φ entre des voisinages des infinis de R4/Γ et de Xζ

tel que les 2-tenseurs harmoniques homogènes O41 , O42 et O43 soient des termes en 

r−4 

> e

de déformations infinitésimales de Φ∗gζ .En particulier, les conditions ∫

> S3
> (

3〈H2, O 4 

> i

〉ge + O4 

> i

(BeH2, ∂ re ))

dS = 0 pour un 

2-tenseur quadratique H2 tel que de Ric H2 = Λ ge impliquent que 

det R+(H2) = 0 .

Démonstration. Soient Γ un sous-groupe fini de SU (2), et ζ 6 = 0. Il existe donc 

l ∈ { 1, ..., k Γ} tel que la l-ième coordonnée de ( ζ1, ζ 2, ζ 3) ∈ (RkΓ )3, ( ζl

> 1

, ζ l

> 2

, ζ l

> 3

)soit non-nulle. Comme pour la métrique d’Eguchi-Hanson où toutes les métriques 210 Chapitre 5. Obstructions à la désingularisation sont homothétiques à celle avec ζ = (1 , 0, 0), grâce à l’action de SO (4) et d’une homothétie, on obtient une métrique g˜ζ avec ( ˜ζl

> 1

, ˜ζl

> 2

, ˜ζl

> 3

) = (1 , 0, 0). Les variations infinitésimales associées aux variations de ( ˜ζl

> 1

, ˜ζl

> 2

, ˜ζl

> 3

) seulement sont alors asymptotiques à O41 , O42 et O43 , et l’obstruction det R+(H2) = 0 est une conséquence du corollaire 5.52. 

Remarque 5.56 . Le cas de la métrique d’Eguchi-Hanson (ou des ζl parallèles), est en fait le cas le moins obstrué. La condition d’obstruction est R+ = 0 pour des ζ

génériques lorsque kΓ > 1. Les derniers exemples connus de variétés Ricci-plates ALE sont seulement käh-lériens, et sont en fait des quotients de variétés hyperkählériennes par des groupes cycliques. On en déduit le même résultat d’obstruction. 

Corollaire 5.57. Soit Γ un groupe 1 

> dn 2

(1 , dnm − 1) ⊂ U (2) pour d > 1, n > 2 et 

n et m premiers entre eux, et pour ζ ∈ RdΓ \DΓ, gζ une métrique Ricci-plate ALE kählérienne asymptotique à R4/Γ. Alors pour H2 un 2-tenseur homogène sur R4/Γ

satisfaisant de Ric H2 = Λ ge, les conditions 

> ∫
> S3
> (

3〈H2, O 4 

> i

〉ge + O4 

> i

(BeH2, ∂ re ))

dvS3 = 0 ,

pour O4 

> i

les termes d’ordre −4 des déformations infinitésimales L2 de gζ impliquent que 

det R+(H2) = 0 .

Démonstration. Soit 1 

> dn 2

(1 , dnm −1) ⊂ U (2) un sous-groupe fini de U (2), et ( N, g b)un orbifold Ricci-plate ALE asymptotique à R4/Γ non plate. D’après [Suv11], ( ˜N , ˜gb) le revêtement universel de ( N, g b) est un orbifold hyperkählérien asymp-totique à ˜Γ = 1 

> dn

(1 , −1) ⊂ 1 

> dn 2

(1 , dnm − 1). Soit H2, un 2-tenseur homogène sur 

R4/Γ, il se relève aussi sur R4/˜Γ en ˜H2.Revenons à la source de l’obstruction qui est la proposition 5.3, et plus précisé-ment l’existence d’un 2-tenseur h2 asymptotique à H2 tel que dgb Ric( h2) = Λ gb. Si un tel 2-tenseur existe sur ( N, g b), on peut le relever en un 2-tenseur ˜h2 sur ( ˜N , ˜gb)asymptotique à ˜H2 et satisfaisant d˜gb Ric( ˜h2) = Λ˜ gb ce qui implique, de nouveau d’après la proposition 5.3 et au corollaire 5.55, la condition det R+( ˜H2) = 0 puis det R+(H2) = 0. 

Remarque 5.58 . Les preuves ci-dessus n’utilisent pas le côté kählérien des mé-triques étudiées. Elles s’appliquent en particulier à toute métrique Ricci-plate ALE dont les termes d’ordre −4 ne s’annulent pas et permet de déduire des obstruc-tions pour d’autres métriques Ricci-plates ALE (s’il en existe) à partir du calcul 4. Obstruction à la formation d’arbres de bulles connues 211 des termes d’ordre −4 de [BH19, Proposition 2.5]. Il n’est cependant pour l’ins-tant pas clair que les termes d’ordre −4 d’une métrique Ricci-plate ALE non-plate soient non-nuls. 

4.3 Arbres de singularités et obstructions 

Nous allons maintenant traiter le cas d’arbres d’orbifolds Ricci-plats ALE käh-lériens. 

4.3.1 Contrôle uniforme des métriques hyperkählériennes ALE 

Soit Γ 1 ∈ SU (2) et ζ1 ∈ DΓ1 fixé tel que l’orbifold ALE ( Xζ1 , g ζ1 ) du théorème 2.14 ait une singularité R4/Γ pour Γ ⊂ SU (2). Notons alors ¯ gζ1,v pour v ∈ O(gζ1 )pour v que l’on choisira assez petit la déformation Ricci-plate (et même hyper-kählérienne) de gζ1 donnée par le corollaire 5.21. L’objectif de cette sous-section est de montrer que pour ζ ∈ R3kΓ avec |ζ| = 1, il existe une échelle τ > 0 telle que pour tout t < τ , le recollement naïf de gζ à ¯ gζ1,v à l’échelle t, noté gBv,t,ζ peut être perturbé en une métrique Ricci-plate modulo obstructions que l’on notera ˆ gv,t,ζ .Le recollement naïf gBv,t,ζ est Ricci-plat partout sauf sur l’anneau où le recolle-ment a lieu. On obtient donc un contrôle 

‖ΦgBv,t,ζ (gBv,t,ζ )‖r−2    

> BCαβ(gBv,t,ζ )

6 Ct 2−β

> 4

où C > 0 ne dépend que de ζ1 et v car les coordonnées ALE de gζ sont uniformé-ment contrôlées par |ζ| = 1 dans les coordonnées de [Kro89a, Corollaire 3.14]. En reprenant la preuve par théorème des fonctions inverse du théorème 4.51, pour perturber gBv,t,ζ en une métrique Ricci-plate modulo obstructions, pour mon-trer l’existence de ˆ gv,t,ζ , il nous suffirait de montrer que 

π ˜O(gBv,t,ζ )⊥ PgBv,t,ζ : ˜ O(gBv,t,ζ )⊥ ∩ C2,α β, ∗ (gBv,t,ζ ) → ˜O(gBv,t,ζ )⊥ ∩ r−2 

> B

Cαβ (gBv,t,ζ )est uniformément borné avec un inverse uniformément borné pour |ζ| = 1 et t

suffisamment petit et de contrôler les termes non-linéaires de ΦgBv,t,ζ . En se fixant 

ζ1 et v, il suffirait alors de montrer par le lemme 4.49 que 

Pgζ : O(gζ )⊥ ∩ C2,α β, ∗ (gζ ) → O(gζ )⊥ ∩ r−2 

> ζ

Cαβ (gζ )est inversible avec un inverse borné et de contrôler les termes non-linéaires. Ce n’est cependant pas le cas lorsque ζ → DΓ, c’est-à-dire lorsque gζ dégénère. Il 212 Chapitre 5. Obstructions à la désingularisation convient alors dans ces situations de remplacer les normes par rapport à gζ par des normes par rapport à une désingularisation naïve gBζ proche de gζ pour garder une échelle de recollement uniforme. 

Proposition 5.59. Pour tout Γ ⊂ SU (2) , et tout ε > 0, il existe C = C(Γ , ε ) > 1

telle que pour tout ζ ∈ R3kΓ avec |ζ| = 1 , il existe une métrique de désingularisation naïve (partielle si ζ ∈ DΓ et totale si ζ / ∈ DΓ, voir définitions 3.3) gBζ d’un orbifold 

gζo avec ζo ∈ DΓ et |ζo| = 1 asymptotique à R4/Γ par des orbifolds hyperkählériens 

gζj pour |ζj | = 1 et ζj ∈ RkΓj pour |Γj | < |Γ|, pour laquelle en notant 

R(gBζ ) := sup     

> h⊥˜O(gB)∩C2,α β, ∗(gB)

‖h‖C2,α β, ∗ (gB )

‖PgB h‖r−2   

> BCαβ(gB)

+ sup   

> h∈C2,α β, ∗(gB)

‖PgB h‖r−2   

> BCαβ(gB)

‖h‖C2,α β, ∗ (gB )

,

on ait 1. ‖gBζ − gζ ‖C2,α β, ∗ (gBζ ) < εR(gBζ ) ,2. R(gBζ ) 6 C,3. il existe des coordonnées ALE d’ordre 4 pour gBζ hors d’une boule de rayon 

C.Remarque 5.60 . Les normes de cet énoncé prises par rapport à gBζ sont des normes à poids d’arbre de singularités et décroissent donc dans les anneaux de basse courbure ce qui permet d’avoir des contrôles uniformes lorsque des zones de haute courbure apparaissent. 

Remarque 5.61 . Ce qui est crucial dans cet énoncé est que la constante C soit indépendante de la métrique gζ et en particulier que l’on puisse approcher les mé-triques singulières correspondant à ζ ∈ DΓ tout en gardant des contrôles uniformes. La constante ε sert essentiellement à déterminer à partir de quelle proximité on préférera remplacer une métrique lisse gζ par un arbre de singularités dans nos ap-plications. En effet, la désingularisation naïve triviale composée de gBζ = gζ seule est toujours un candidat satisfaisant la première et la dernière propriété. 

Démonstration. Soit ε > 0. Montrons ce résultat par récurrence sur l’ordre k du groupe à l’infini. C’est tout d’abord vrai pour le groupe d’ordre Z2 d’ordre 2 car les différentes métriques obtenues pour |ζ| = 1 sont isométriques à la métrique d’Eguchi-Hanson et le contrôle espéré est satisfait pour la désingularisation naïve triviale composée de la métrique elle-même. 4. Obstruction à la formation d’arbres de bulles connues 213 Supposons donc que la propriété soit satisfaite pour tous les groupes d’ordre inférieur à k − 1 > 2 et montrons qu’elle tient toujours pour un groupe Γ d’ordre 

k.Raisonnons alors encore une fois par récurrence sur l’énergie de nos orbifolds hyperkählériens ALE, c’est-à-dire sur le carré de la norme L2 de la courbure Rie-mannienne qui est une quantité topologique proportionnelle à la dimension de la cohomologie (orbifold) L2 en degré 2 pour ces instantons gravitationnels. D’après les résultats du chapitre 2, il y a une perte de norme L2 de la courbure dans les bulles qui se forment et donc si l’on fixe le groupe à l’infini, plus cette énergie est petite, plus l’orbifold est singulier. Considérons pour l’initialisation, le cas des orbifolds gζ , ζ ∈ R3kΓ , |ζ| = 1 avec la plus petite énergie possible. Supposons par l’absurde qu’il existe une suite de métriques orbifolds gζi , |ζi| = 1 avec l’énergie minimale et telles que pour toute désingularisation naïve (voir définition 3.3) gB d’un orbifold hyperkählérien asymptotique à R4/Γ, on ait 1. soit, ‖gζi − gB ‖C2,α β, ∗ (gB ) > εR(gB ) ,2. soit, R(gB ) > i ,3. soit, il n’existe pas de coordonnées ALE d’ordre 4 hors de toute boule de rayon i,et supposons quitte à prendre une sous-suite que ces métriques aient la même topologie. 

Remarque 5.62 . Le fait que la topologie soit la même est en réalité déjà assuré par notre hypothèse de minimalité. De plus les espaces que l’on obtient sous cette hypothèse sont les instantons gravitationnels de rang 1 introduits dans [Biq16]. Dans les coordonnées données par [Kro89a, Proposition 3.14] où la dépen-dance entre les métriques est analytique, toutes les métriques gζi admettent des coordonnées ALE d’ordre 4 avec un contrôle uniforme en norme r−4 

> ζi

C3(gζi ) dans un voisinage uniforme de l’infini, où rζi est la fonction de la définition 4.9. On en déduit qu’il ne peut y avoir de concentration L2 de la courbure que dans un com-pact de diamètre uniformément majoré et de volume uniformément minoré par l’inégalité de Bishop-Gromov (ou [Kro89a, Lemma 3.3]). Par minimalité de l’éner-gie, il ne peut pas y avoir de formation d’arbre de singularités car sinon l’orbifold ALE asymptotique à Γ aurait une énergie plus petite. Il existe donc une métrique 

gζ∞ telle que les gζi convergent de manière lisse (en considérant des revêtements locaux aux singularités orbifolds) vers gζ∞ , et donc ‖gζi − gζ∞ ‖C2,α β, ∗ (gζ∞ ) → 0 quand 214 Chapitre 5. Obstructions à la désingularisation 

i → ∞ où nous avons ‖.‖C2,α β, ∗ (gζ∞ ) ≈ ‖ (1 + rζ∞ )β .‖C2,α (gζ∞ ) ici car on utilise des revêtements locaux aux singularités éventuelles de gζ∞ . De plus, il existe des coor-données d’ordre 4 hors d’une boule ayant un rayon uniformément contrôlé d’après le corollaire 5.20 ce qui contredit donc la troisième propriété pour i assez grand. La désingularisation naïve triviale gB = gζ∞ contredit les deux autres hypothèses de départ. En effet, pour la première hypothèse, la convergence est lisse et a donc lieu dans l’espace C2,α β, ∗ (gζ∞ ) où le poids n’est qu’à l’infini. D’autre part, comme 

Pgζ∞ est elliptique, il existe C > 0 telle que pour tout h ⊥ O(gζ∞ ), on ait 

‖h‖C2,α β, ∗ (gζ∞ ) 6 C‖Pgζ∞ h‖r−2   

> ζ∞Cαβ(gζ∞)

,

ce qui contredit la seconde hypothèse. Considérons maintenant un niveau d’énergie E > 0 supérieur et supposons que la propriété soit satisfaite par tous les instantons gravitationnels asymptotiques à 

R4/Γ et dont le carré de la norme L2 de la courbure est strictement inférieure à 

E. Raisonnons encore une fois par l’absurde et supposons que l’on ait une suite de contre-exemples ζi ∈ R3kΓ |ζi| = 1 satisfaisant ‖ Rm gζi ‖2  

> L2(gζi)

= E avec pour toute désingularisation naïve gB d’un orbifold hyperkählérien asymptotique à R4/Γ, — soit, ‖gζi − gB ‖C2,α β, ∗ (gB ) > εR(gB ) ,— soit, R(gB ) > i ,— soit, il n’existe pas de coordonnées ALE d’ordre 4 hors d’une boule de rayon 

i.Comme dans l’argument pour le niveau d’énergie minimal, si aucune singularité ne se formait et que l’on avait une convergence lisse (et C2,α β, ∗ (gζ∞ )) vers un orbifold gζ∞

avec une borne R(gζ∞ ). Nous avons donc la formation d’un arbre de singularités. Plus précisément, quitte à prendre une sous-suite, il existe une suite de désingula-risations naïves gB′ 

> ζi

d’un orbifold hyperkählérien asymptotique à R4/Γ, composées d’un orbifold ALE gζo avec |ζo| = 0 asymptotique à R4/Γ et d’orbifolds ALE gζj

avec |ζj | = 1, ζj ∈ R3kΓj avec |Γj | < |Γ| = k (on peut toujours le supposer car gtζ 

est isométrique à tg ζ ) à des échelles ti,j , pour laquelle on ait ‖gζi − gB′ 

> ζi

‖C2,α β, ∗

→ 0quand i → ∞ . De plus, toutes les métriques gζo et gζj sont hyperkählériennes d’après [Ban90]. Le carré de la norme L2 de la courbure de gζo est strictement in-férieur à E car on perd de l’énergie dans les singularités, et les gζj ont des groupes à l’infini d’ordre inférieur à k − 1 d’après l’inégalité de Bishop-Gromov. Quitte à remplacer par les désingularisations naïves de notre hypothèse de récurrence pour obtenir une nouvelle désingularisation naïve gBζi , nous contrôlons les inverses des opérateurs P des différents orbifolds ALE sur l’orthogonal de leur noyau (ou noyau 4. Obstruction à la formation d’arbres de bulles connues 215 approché) de manière uniforme en fonction des constantes précédentes. D’après le lemme 4.42, nous obtenons un contrôle uniforme sur l’inverse de l’opérateur P sur notre désingularisation naïve. Cela contredit les hypothèses de départ et démontre l’énoncé. Le lemme suivant nous permettra entre autres de contrôler le noyau de l’opé-rateur Pgζ à partir du noyau approché ˜ O(gBζ ). 

Lemme 5.63. Soient P et P ′ deux opérateurs entre des espaces de Banach X et 

Y pour lesquels il existe C > 0, 1100 C > ε > 0 et un sous-espace de dimension finie 

K′ ⊂ X et S′ un supplémentaire de K′ dans X tels que l’on ait : 1. pour tout x ∈ X,

‖(P − P ′)x‖Y 6 ε‖x‖X ,

2. pour tout x ∈ S′,

‖x‖X 6 C‖P ′x‖Y ,

3. pour tout x ∈ K′,

‖P ′x‖Y 6 ε‖x‖X ,

4. et dim (ker P ) = dim (K′).Alors, pour tout élément k de ker P , il existe un élément k′ de K′ tel qu’on ait 

‖k − k′‖X 6 2Cε 

1 − Cε ‖k′‖X . (5.47) 

Démonstration. Soit k ∈ ker P , et considérons sa décomposition k = k′ + s′ dans la somme directe X = K′ ⊕ S′. Par la première hypothèse, nous avons 

‖P ′k‖Y 6 ε‖k‖X , (5.48) par la seconde, nous avons 

‖s′‖X 6 C‖P ′s′‖Y (5.49) et par la troisième, nous avons 

‖P ′k′‖Y 6 ε‖k′‖X . (5.50) En utilisant (5.48), (5.49) et (5.50) ensemble, nous obtenons 

ε‖k‖X > ‖P ′s′‖Y − ‖ P ′k′‖Y > ‖s′‖X

C − ε‖k′‖X , (5.51) 216 Chapitre 5. Obstructions à la désingularisation puis comme k = k′ + s′,

‖s′‖X 6 Cε (

‖k‖X + ‖k′‖X

)

6 2Cε ‖k′‖X + Cε ‖s′‖X ,

et finalement 

‖k − k′‖X = ‖s′‖X 6 2Cε 

1 − Cε ‖k′‖X .

Remarque 5.64 . Avec les trois premières hypothèses du lemme 5.63, nous avons toujours l’inégalité 

dim ker P 6 dimK ′,

et tout élément de ker P est proche d’un élément de K′ (sa projection sur K′

parallèlement à S′) au sens de (5.47). On déduit du lemme 5.63 et des estimations 1 et 2 de la proposition 5.59 que pour tout Γ ⊂ SU (2) et pour tout ε > 0 assez petit en fonction de Γ seulement, pour tout ζ ∈ R3kΓ et pour la métrique gBζ obtenue par la proposition 5.59 avec ε,on a le contrôle suivant avec C = C(Γ , ε ) > 0 : pour tout h ⊥ O(gζ ), 1

C ‖h‖C2,α β, ∗ (gBζ ) < ‖Pgζ h‖r−2    

> BCαβ(gBζ)

< C ‖h‖C2,α β, ∗ (gBζ ). (5.52) On en déduit que l’on peut définir des perturbations Ricci-plates modulo obs-tructions de nos désingularisations naïves. 

Corollaire 5.65. Soit (Xζ1 , g ζ1 ) un orbifold Ricci-plat ALE pour ζ1 ∈ DΓ1 fixé ayant une singularité R4/Γ pour Γ ⊂ SU (2) . Alors, il existe ε > 0 et τ > 0 tels que pour tous 0 < t < τ , ζ ∈ R3kΓ avec |ζ| = 1 et v ∈ O(gζ1 ) avec ‖v‖C2,α β, ∗ (gζ1 ) < τ ,si l’on note gBB v,t,ζ le recollement naïf de la métrique (Xζ , g Bζ ), de la proposition 5.59 pour la constante ε, à la singularité R4/Γ de ¯gζ1,v (défini avant cet énoncé), et si l’on note gBv,t,ζ le recollement naïf de (Xζ , g ζ ) à l’échelle t, il existe une unique métrique ˆgv,t,ζ satisfaisant — gBv,t,ζ − ˆgv,t,ζ ⊥ ˜O(gBv,t,ζ ),— ‖gBv,t,ζ −ˆgv,t,ζ ‖C2,α β, ∗ (gBB v,t,ζ ) 6 2τ (remarquer la norme de désingularisation naïve 

gBB  

> v,t,ζ

), et — ΦgBv,t,ζ (ˆ gv,t,ζ ) ∈ ˜O(gBv,t,ζ ).De plus, la métrique ˆgv,t,ζ dépend de manière lisse de v, t et ζ.Démonstration. Comme vu dans la discussion au début de cette section, pour le 4. Obstruction à la formation d’arbres de bulles connues 217 recollement naïf gBv,t,ζ , nous avons un contrôle 

‖ΦgBv,t,ζ (gBv,t,ζ )‖r−2    

> BCαβ(gBB v,t,ζ )

6 Ct 2−β

> 4

où C > 0 ne dépend que de ζ1 et v. Maintenant, à l’aide du contrôle (5.52) pour remplacer les contrôles du lemme 4.42, nous pouvons reprendre la preuve du lemme 4.49 pour montrer que pour τ assez petit en fonction de Γ et ζ1 seuls, l’opérateur 

π ˜O(gBv,t,ζ )⊥ PgBv,t,ζ : ˜ O(gBv,t,ζ )⊥ ∩ C2,α β, ∗ (gBB v,t,ζ ) → ˜O(gBv,t,ζ )⊥ ∩ r−2 

> B

Cαβ (gBB v,t,ζ ),

est uniformément borné (indépendemment de ζ et de t et v assez petits) inversible avec un inverse uniformément borné, où l’on remarquera encore une fois que les normes sont définies par rapport à la désingularisation naïve gBB v,t,ζ . La preuve du théorème 4.51 nous permet alors de montrer par théorème des fonctions inverses qu’il existe une unique solution ˆ gv,t,ζ aux équations de l’énoncé. Comme dans le corollaire 4.55, la dépendance lisse de la métrique est une conséquence du théorème des fonctions implicites pour les fonctions lisses appliqué à l’application Ψ : ( v, t, ζ, h ) 7 → π ˜O(gBv,t,ζ )⊥ ΦgBv,t,ζ (gBv,t,ζ + h)pour h ⊥ ˜O(gBv,t,ζ ). 

Remarque 5.66 . En définissant différemment nos désingularisations naïves, nous pourrions en réalité obtenir une dépendance analytique mais ce ne sera pas néces-saire pour la suite. Par exemple nous aurions pu recoller les métriques gtζ à une échelle τ petite et fixée plutôt que la métrique gζ à une échelle t

4.3.2 Recollement d’instantons gravitationnels 

Remarquons tout d’abord que toutes les jauges de recollement d’instantons gravitationnels données par les isométries du cône R4/Γ sont équivalentes à recoller un instanton gravitationnel avec la jauge du lemme 5.53 mais avec un paramètre 

ζ différent. 

Lemme 5.67. Soit (Mo, g o) un orbifold (compact ou ALE) ayant une singularité 

R4/Γ en p avec Γ ⊂ SU (2) , et soit ζ ∈ R3kΓ avec les notations du théorème 2.14. Soit de plus ψ une isométrie du cône R4/Γ préservant l’orientation. Alors, il existe ζ′ ∈ R3kΓ tel que le recollement naïf de (Xζ , g ζ ) en p avec les coordonnées ALE données par [Kro89a, Proposition 3.14] composé avec ψ au 218 Chapitre 5. Obstructions à la désingularisation 

moment d’identifier le cône à l’infini et de la singularité (voir la remarque 3.5) soit isométrique au recollement naïf de (Xζ′ , g ζ′ ) à (Mo, g o) en p sans composer avec une isométrie du cône. Démonstration. Reprenons les notations de la section 1.2.3 du chapitre 1 pour les sous-groupes de SO (4). Le résultat est clair pour le cas où Γ = Z2 et où ψ ∈ SO (4) car la métrique d’Eguchi-Hanson est U (2)-invariante et l’action de ψ sur la mé-trique revient à une action de SO (4) /U (2) ≈ SU (2) /U (1) ≈ SO (3) /U (1) sur le paramètre ζ ∈ R3 du théorème 2.14. Pour un autre groupe Γ ⊂ SU (2), avoir 

ψ ∈ Isom( R4/Γ) implique que ψ soit un élément du normalisateur de Γ dans SO (4) qui implique donc ψ ∈ ϕ(S3 × NΓ), où NΓ est le normalisateur de Γ dans SU (2) (voir [McC02] pour un calcul de ces normalisateurs) et où ϕ : S3 × S3 → SO (4) est le revêtement à deux feuillets défini dans la section 1.2.3 du chapitre 1. Étudions maintenant l’action du normalisateur de Γ, ϕ(S3 × NΓ), sur une métrique de [Kro89a] dans les coordonnées de [Kro89a, Proposition 3.14]. Revenons pour cela à la construction de ces espaces. Elle part de 

P := C2 ⊗ End (R),

où C2 est vue comme la représentation standard de SU (2) et où R est la représen-tation régulière de SU (2). Notons P Γ l’ensemble des éléments de P invariants par Γ, F , l’ensemble des éléments commutant avec Γ vu comme un sous-ensemble des transformations unitaires de R, et notons enfin T le sous-groupe des complexes de norme 1 qui agit trivialement. Les instantons gravitationnels asymptotiques à 

C2/Γ sont alors définis comme les quotients hyperkählériens de P Γ par F/T .Par définition, le normalisateur ϕ(S3 × NΓ) agit sur P Γ et commute à l’action de F . Il agit donc sur l’ensemble des solutions des équations de l’application de moment μ : P Γ → (f/t)∗ ⊗ R3 où f et t sont les algèbres de Lie de F et T respecti-vement. Plus précisément, en notant Ik, k ∈ { 1, 2, 3} les trois structures complexes de P Γ données par l’identification de C2 et de l’ensemble des quaternions, pour tout ξ ∈ f/t, les trois coordonnées de μ satisfont les équations 

grad (μk.ξ ) = Ik(Vξ),

où Vξ est le champ de vecteurs sur P Γ engendré par l’action de ξ (voir aussi l’exemple 4.5.2 de la thèse de Kronheimer). La partie SU (2) à laquelle Γ et NΓ

appartiennent commute aux trois structures complexes car elle est identifiée à la multiplication à droite par un quaternion de norme 1 (voir la section 1.2.3). On en 4. Obstruction à la formation d’arbres de bulles connues 219 déduit que NΓ agit par isométrie sur la métrique hyperkählérienne μ−1(ζ)/(F/T )pour tout ζ ∈ (f/t)∗ ⊗ R3. La partie SU (2) du normalisateur, qui est identifiée à la multiplication à gauche par un quaternion de norme 1, agit par rotation sur les trois structures complexes. Plus précisément, un élément n− ∈ SU (2) en-voie μ−1(ζ)/(F/T ) sur μ−1(Ad (n−)ζ)/(F/T ) où Ad (n−) est l’action standard de 

SU (2) /± ≈ SO (3) sur le facteur R3 de ( f/t)∗ ⊗ R3.Pour conclure, il reste à assurer que cette action du normalisateur est bien l’action standard sur le cône asymptotique R4/Γ dans les coordonnées de [Kro89a, Proposition 3.14]. Pour cela, on utilise l’identification R4/Γ ≈ μ−1(0) /(F/T ) de [Kro89a, Corollary 3.2] qui permet tout d’abord d’assurer que le normalisateur agit de manière standard sur R4/Γ (et par isométries) par l’argument d’au dessus. La correspondance des infinis de μ−1(ζ)/(F/T ) et de μ−1(0) /(F/T ) pour les co-ordonnées de [Kro89a, Proposition 3.14] donnée par [Kro89a, (3.13)] nous assure que l’action du normalisateur est bien l’action standard sur le cône asymptotique 

R4/Γ. Ainsi, le recollement naïf de la métrique ( Xζ , g ζ ) ≈ μ−1(ζ)/(F/T ) pour ζ ∈

R3kΓ ≈ (f/t)∗ ⊗ R3 composée avec l’isométrie ψ = ϕ(ψ−, ψ +) est isométrique au recollement naïf de ( Xζ′ , g ζ′ ) avec ζ′ = Ad (ψ−)ζ.Remarquons ensuite que tout orbifold hyperkählérien ALE peut être désingu-larisé en une variété hyperkählérienne ALE. 

Lemme 5.68 ([Ban90]) . Soit (Xζ1 , g ζ1 ) un orbifold ALE hyperkählérien avec une singularité R4/Γ. Alors, pour tout t > 0, il existe ζt 

> 0

∈ R3kΓ \DΓ et vt ∈ O(gζ1 )

satisfaisant lim t→0 vt = 0 et lim t→0 Xζt 

> 0

= Xζ0 ∈ R3kΓ \DΓ, tels que la désingula-risation d’Einstein modulo obstructions (Xζ1 #Xζ0 , ˆgvt,t,ζ t 

> 0

) du corollaire 5.65 soit hyperkählérienne et donc un instanton gravitationnel de Kronheimer. Démonstration. Le résultat de [Ban90, Theorem 4] nous assure que pour t assez petit, il existe ζ0 pour lequel il existe une métrique hyperkählérienne gt satisfaisant 

‖gt − gB 

> 0,t,ζ 0

‖(1+ rB )−β C2,α    

> 0(gB
> 0,t,ζ 0)

6 γ(t),

où lim t→0 γ(t) = 0. Nous pouvons alors appliquer notre construction de coor-données du chapitre 3 à ( Xζ1 #Xζ0 , g t) afin d’obtenir un difféomorphisme ϕ :

Xζ1 #Xζ0 → Xζ1 #Xζ0 grâce auquel nous avons le meilleur contrôle 

‖ϕ∗gt − gB 

> 0,t,ζ 0

‖C2,α β, ∗ (gB  

> 0,t,ζ 0)

6 Cγ (t).220 Chapitre 5. Obstructions à la désingularisation Nous pouvons ensuite mettre cette métrique ϕ∗gt en jauge divergence réduite par rapport à gB 

> 0,t,ζ 0

à l’aide d’un petit difféomorphisme ψ : Xζ1 #Xζ0 → Xζ1 #Xζ0

d’après la proposition 4.39. L’unicité du théorème 4.51 et le fait que les déforma-tions infinitésimales de ( Xζ0 , g ζo ) s’intègrent en des courbes t 7 → (Xζ0(t), g ζ0(t)) par la classification de [Kro89a, Kro89b] nous assure alors qu’il existe vt ∈ ˜O(gB 

> 0,t,ζ 0

)et ζt 

> 0

tels que l’on ait 

ψ∗(ϕ∗gt) = ˆ gvt,t,ζ t 

> 0

,

avec ˆ gvt,t,ζ t 

> 0

une des métriques construites dans le théorème 4.51. 

Remarque 5.69 . Notons que [HV20, Theorem 6.2] permet de recoller et perturber des instantons gravitationnels lisses dans toutes les directions lisses. 

Proposition 5.70. Il existe τ > 0 tel que pour tous (v, t, ζ ) ∈ (

BC2,α β, ∗ (gζ1 )(0 , τ ) ∩

O(gζ1 ))

× (0 , τ ) × (S3kΓ−1\DΓ), la métrique ˆgv,t,ζ de la proposition 5.65 soit iso-métrique à une métrique hyperkählérienne de [Kro89a]. Démonstration. Pour montrer ce résultat, nous remarquons tout d’abord que l’en-semble (

BC2,α β, ∗ (gζ1 )(0 , τ ) ∩ O(gζ1 ))

× (0 , τ ) × (S3kΓ−1\DΓ)est connexe car DΓ est une union finie de sous-espaces de codimension au moins 2 dans S3kΓ−1. Il nous suffit alors de montrer que l’ensemble 

E = {

(v, t, ζ ) ∈ (

BC2,α β, ∗ (gζ1 )(0 , τ ) ∩ O(gζ1 ))

× (0 , τ ) × (S3kΓ−1\DΓ), Ric(ˆ gv,t,ζ ) = 0 }

qui est non-vide d’après le lemme 5.68 est ouvert et fermé car une métrique Ricci-plate ayant la topologie Xζ1 #Xζ est nécessairement hyperkählérienne d’après [Nak90]. Elle est donc isométrique à gξ(v,t,ζ ) pour ξ(v, t, ζ ) ∈ R3kΓ1 \DΓ1 .La fermeture de E est une conséquence directe de la continuité (et même la dépendance lisse) de (v, t, ζ ) ∈ (

BC2,α β, ∗ (gζ1 )(0 , τ ) ∩ O(gζ1 ))

× (0 , τ ) × (S3kΓ−1\DΓ) 7 → Ric(ˆ gv,t,ζ )prouvée dans le corollaire 5.65. Pour l’ouverture, supposons que pour ( v, t, ζ ) fixé, nous ayons Ric(ˆ gv,t,ζ ) = 0. La métrique ˆ gv,t,ζ est donc une des métriques hyperkählériennes de [Kro89a]. Il existe un espace de la même dimension que ˜ O(gBv,t,ζ ) de déformations hyperkählé-riennes au voisinage de gξ(v,t,ζ ) et donc de même pour les déformations Ricci-plates de ˆ gv,t,ζ . En effet, comme les métriques ¯ gζ1,v et gζ2 et gξ(v,t,ζ ) sont hyperkählériennes, 4. Obstruction à la formation d’arbres de bulles connues 221 leurs déformations infinitésimales hyperkählériennes sont de dimension trois fois celle de leur cohomologie L2 en degré 2, et la dimension de cette cohomologie est additive pour les recollements naïfs que l’on effectue. D’après le lemme 5.63 appliqué à P = Pˆgv,t,ζ , P ′ = PgBv,t,ζ , K′ = ˜ O(gBv,t,ζ ) et S′ =˜O(gBv,t,ζ )⊥, les déformations infinitésimales Ricci-plates de ˆ gv,t,ζ sont arbitrairement proches d’éléments de ˜ O(gBv,t,ζ ). On en déduit que les petites déformations Ricci-plates de ˆ gv,t,ζ qui restent dans BC2,α β, ∗ (gBv,t,ζ ,2ε) pour ε > 0 la constante du théorème 4.51 sont isométriques à des métriques ˆ gv′,t ′,ζ ′ où les de ( v′, t ′, ζ ′) atteignent un voisinage entier de ( v, t, ζ ) dans (

BC2,α β, ∗ (gζ1 )(0 , τ ) ∩ O(gζ1 ))

× (0 , τ ) × (S3kΓ−1\DΓ). L’ensemble est donc ouvert. 

4.3.3 Obstructions à la formation d’arbres d’orbifolds ALE kählériens 

Utilisons les notations de la preuve de la proposition 5.55, et paramétrons l’en-semble des variétés Ricci-plates ALE asymptotiques à R4/Γ par ( Xζ , g ζ )ζ∈R3kΓ \DΓ

dans l’énoncé qui suit. 

Lemme 5.71. Soit (Xζ0 , g ζ0 ), pour ζ0 ∈ DΓ un orbifold Ricci-plat kählérien asymptotique à R4/Γ. Alors, pour tout ζ ∈ R3kΓ suffisamment proche de ζ0, il existe (Nk, g bk )k un arbre d’orbifolds Ricci-plats ALE kählériens désingularisant 

R4/Γ, t = ( tk)k > 0 avec t1 = 1 et (N1, g b1 ) = ( Xζ0 , g ζ0 ) tels que (Xζ , g ζ ) soit isométrique à (N, ¯gb,t ) la perturbation (itérée) de la proposition 5.70 de (N, g Bv,t,ζ ),la désingularisation naïve obtenue en recollant les (Nk, g bk ) aux échelles relatives 

tk.Il existe ε > 0 tel que pour ζ suffisamment proche de ζ0, il existe un difféomor-phisme Φζ entre des voisinages des infinis de (Xζ , g ζ ) et de R4/Γ et o1(ζ), o2(ζ)

et o3(ζ), des éléments de O(gζ ) satisfaisant pour tout i ∈ { 1, 2, 3},

Φ∗ 

> ζ

oi(ζ) = O4 

> i

+ O(r4+ βB ),

où les O4 

> i

= O(r−4 

> B

) sont les 2-tenseurs du corollaire 5.48, et avec ‖oi(ζ)‖L2(gζ ) > ε.Démonstration. D’après le corollaire 5.20, ( Xζ , g ζ ) = ( N, ¯gb,t ) est une petite per-turbation Ricci-plate et kählérienne d’une désingularisation naïve ( N, g Bt ) pour 

t suffisamment petit en fonction de ζ. De plus, les termes en r−4 

> e

de ( Xζ , g ζ )convergent vers ceux de ( Xζ0 , g ζ0 ) lorsque ζ → ζ0 d’après le corollaire 5.20. Par hypothèse, il existe l ∈ { 1, ..., k Γ} tel que ζl 

> 0

6 = 0, et donc, pour ζ suffi-samment proche de ζ0, nous avons ζl 6 = 0 par continuité. Exactement comme dans la preuve de la proposition 5.55, cela implique qu’il existe un difféomorphisme Φ ζ222 Chapitre 5. Obstructions à la désingularisation entre des voisinages des infinis de ( Xζ , g ζ ) et de R4/Γ et des déformations infini-tésimales de gζ , o1(ζ), o2(ζ) et o3(ζ) telles qu’il existe C > 0 indépendant de ζ

pour lequel on a pour tout i ∈ { 1, 2, 3},

∣∣∣Φ∗ 

> ζ

oi(ζ) − O4

> i

∣∣∣ 6 Cr −4−βB

d’après le corollaire 5.20. En particulier, comme O4 

> i

6 = 0, il existe ε > 0 dépendant de C et β, mais indépendant de ζ tel que l’on ait ‖oi(ζ)‖L2(gζ ) > ε.

Lemme 5.72. Soit gBt un recollement naïf d’orbifolds Ricci-plats ALE kählériens et ¯gb,t sa perturbation Ricci-plate ALE kählérienne obtenue dans la proposition 5.70. Alors pour tout 2-tenseur w ∈ r−2 

> B

Cαβ (gBt ), il existe un unique 2-tenseur u ∈

˜O(gBt )⊥

> gBt

∩ C2,α β, ∗ (gBt ), tel que 

¯P¯gb,t u = πO(¯ gb,t )⊥ w. (5.53) 

Nous avons de plus le contrôle suivant pour C = C(gBt ) > 0,

‖u‖C2,α β, ∗ (gBt ) 6 ‖πO(¯ gb,t )⊥ w‖r−2   

> BCαβ(gBt)

.

Remarque 5.73 . Ce qui est crucial dans ce lemme est le fait que la solution ne soit pas seulement contrôlée en norme C2,α β, ∗ (¯ gb,t ) qui ne “voit” pas les différentes échelles de l’arbre de singularités, mais en norme C2,α β, ∗ (gBt ) d’arbre de singularités qui les distingue et qui se comporte donc bien quand t → 0. 

Démonstration. D’après le théorème 5.40, nous avons le contrôle 

‖¯gb,t − gBt ‖C2,α β, ∗ (gBt ) 6 Ct 2−β 

> 4
> max

, (5.54) qui, combiné à la preuve du théorème 4.51 implique que pour tmax suffisamment petit, l’opérateur ¯P¯gb,t est injectif sur ˜ O(gBt )⊥ ∩ C2,α β, ∗ (gBt ). De plus, pour 0 < β < 1, son conoyau sur r−2 

> B

Cαβ (gBt ) est égal à son noyau sur r−2 

> B

Cα 

> −β

(gBt ) qui est O(¯ gb,t ). En effet, pour toute métrique Ricci-plate ALE ¯gb,t , le noyau et le conoyau de ¯P¯gb,t : C2,α β, ∗ (¯ gb,t ) → r−2 

> b

Cαβ (¯ gb,t ) sont égaux à O(¯ gb,t )car en prenant la divergence de l’égalité ¯P¯gb,t (h) = 0 pour h ∈ C2,α β, ∗ (¯ gb,t ), on obtient δ¯gb,t δ∗ 

> ¯gb,t

(δ¯gb,t h) = 0, et finalement δ¯gb,t h = 0 d’après la proposition 4.32. En prenant la trace de l’équation restante, on trouve ∇∗ 

> ¯gb,t

∇¯gb,t (tr ¯gb,t h) = 0, et comme 

h décroît à l’infini, tr ¯gb,t h = 0. Finalement P¯gb,t (h) = 0, et on conclut que le noyau 4. Obstruction à la formation d’arbres de bulles connues 223 de ¯P¯gb,t : C2,α β, ∗ → r−2 

> b

Cαβ est O(¯ gb,t ), et de la même manière que son conoyau est aussi O(¯ gb,t ). 

Corollaire 5.74. Soit (N, ¯gb,t ) la perturbation Ricci-plate ALE kählérienne de la proposition 5.70 d’un recollement d’orbifolds Ricci-plats ALE, (N, g B = gBt ). Sup-posons que (N1, g b1 ) soit asymptotique à R4/Γ, considérons ¯H2 un 2-tenseur ho-mogène quadratique sur R4/Γ tel que ¯Pe ¯H2 + λg e = Oo pour un 2-tenseur constant 

Oo et λ ∈ R.Alors, il existe ¯h2 un 2-tenseur sur N et χ, une fonction de coupure à support dans un voisinage de l’infini indépendant des tk où (N, ¯gb,t ) a des coordonnées ALE, tel qu’on ait 

¯P¯gb,t 

¯h2 + λ¯gb,t − χOo = ∑

> i

¯λioi ∈ O(¯ gb,t ).

Il existe C > 0 indépendant des tk tels qu’on ait 

‖¯h2 − χ ¯H2‖C2,α β, ∗ (gB ) 6 C‖ ¯H2‖r2 

> eC0(ge)

.

Démonstration. Considérons ¯H2 un 2-tenseur quadratique sur R4/Γ tel que ¯Pe ¯H2 +

λg e = Oo, et soit χ une fonction de coupure sur N1 à support dans un voisinage de l’infini où ( N1, g b1 ) a des coordonnées ALE on notera aussi χ sur N la coupure prolongée par 0 sur les orbifolds ALE inférieurs. Comme dans un voisinage de l’infini, ¯ gb,t est une petite (indépendamment de t suffisamment petit) perturbation de gB en norme C2,α β, ∗∗ (gB ), quitte à choisir un plus petit voisinage de l’infini, on peut supposer que ce système de coordonnées est aussi ALE pour ¯ gb,t .Nous avons alors 

‖ ¯P¯gb,t (χ ¯H2) + λ¯gb,t − χOo‖r−2    

> BCαβ(gB)

6 C‖ ¯H2‖r2  

> eC00

.

En effet, dans un voisinage de l’infini où χ ≡ 1, comme ¯ gb,t − ge = O(r−4 

> B

), on a ¯P¯gb,t (χ ¯H2) + λ¯gb,t = Oo + O(r−4 

> B

), et sur le reste de la variété, on a le contrôle attendu par définition de la norme r−2 

> B

Cαβ (gB ). D’après le lemme 5.72, il existe un unique 2-tenseur h′ ∈ C2,α β, ∗ (gB ) ∩ ˜O(gB )⊥, tel qu’on ait ¯P¯gb,t (χ ¯H2 + h′) + λ¯gb,t − χOo ∈ O(¯ gb,t ).

De plus, d’après la proposition 5.25, l’élément de O(¯ gb,t ) est explicite. Plus préci-sément, considérons ( oi)i une base orthonormée de O(¯ gb,t ), et supposons grâce au difféomorphisme Φ t du lemme 5.71 que les trois premiers éléments sont asympto-224 Chapitre 5. Obstructions à la désingularisation tiques à ciΦt, ∗O4 

> i

pour ci > 1 

> ε

. Nous avons la valeur explicite suivante de ¯P¯gb,t (χ ¯H2 + h′) + λ¯gb,t − χOo = ∑

> i

¯λioi,

où, nous avons pour i = 1 , 2, 3¯λi := −

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

χ〈Oo, oi〉¯gb,t dvb.

Soit ( Mo, g o) un orbifold d’Einstein et p un de ses points singuliers de singu-larité R4/Γ, So l’ensemble des singularités de Mo\{ p}, et soit ( Nk, g bk )k un arbre d’orbifolds Ricci-plats ALE kählériens recollés dans la même orientation et dés-ingularisant R4/Γ. Soit de plus ˆ gSo,v So une désingularisation naïve modulo obs-tructions de ( Mo, g o, S o) dont les termes quadratiques du développement en jauge divergence au point p sont ˆH2, t1 > 0 et ¯ gb,t un recollement Ricci-plat kählérien des ( Nk, g bk )k à des échelles relatives t = ( tk)k > 0 donné par la proposition 5.70, et un 2-tenseur ˆh2 sur N et les réels ˆλi obtenus par le lemme 5.74. Définissons la métrique d’approximation ˆ gAv comme le recollement naïf (défini-tion 3.3) de ˆ gSo,v So et de t1

> (

¯gb,t + t1ˆh2

> )

où χˆh2 ⊥ O(¯ gb,t ). Nous avons le contrôle suivant qui se montre comme ceux des corollaires 5.9 et 5.27. 

Corollaire 5.75. Soit ˆgAv une métrique d’approximation d’Einstein modulo obs-tructions comme ci-dessus et β > 0. Alors, nous avons le contrôle suivant pour 

tmax > 0 suffisamment petit : pour tout k ∈ N il existe Ck > 0,

> ∥∥∥

π ˜O(gD )⊥ ΦgD (ˆ gAv )∥∥∥r−2    

> DCkβ(gD)

6 Ckt3−β 

> 4
> 1

, (5.55) 

et pour tout o ∈ O(gb), en notant ˜o sa coupure sur M de la définition 4.44, 

> 〈

ΦgD (ˆ gAv ) − t1

> ∑
> i

ˆλi ˜oi, ˜o 

> 〉
> L2(gD)

6 C0‖o‖L2(gb)t32 

> 1

, (5.56) 

tout en satisfaisant, 1. ‖ˆgAv − gD‖C2,α β, ∗ (gD ) 6 2ε,2. ˆgAv − (gD + v) est orthogonal à ˜O(gD) pour le produit L2 de gD.Remarque 5.76 . Ce qui est crucial ici est qu’en considérant les espaces à poids 

C2,α β, ∗ (gBt ) adaptés à l’arbre de singularités se formant, nous obtenons un contrôle par une puissance de t1 seulement. 5. Obstructions sous des hypothèses topologiques 225 On en déduit alors, comme dans les corollaires 5.32 et 5.43 que l’obstruction est satisfaite à la limite à tous les points singuliers de ( Mo, g o) sous l’hypothèse que les orbifolds ALE apparaissant sont kählériens. 

Théorème 5.77. Soit (Mo, g o) un orbifold d’Einstein, et supposons qu’il existe 

(Mi, g i)i une suite de variétés d’Einstein telle que 

(Mi, g i) GH 

−−→ (Mo, g o).

Alors, (Mo, g o) satisfait det R(go) = 0 à tous ses points singuliers où les arbres de singularités se formant au sens de Gromov-Hausdorff d’après le théorème 2.47 sont composés d’orbifolds Ricci-plats ALE kählériens recollés dans la même orien-tation. Remarque 5.78 . Le résultat est optimal pour la singularité R4/Z2 dans le sens où c’est la seule obstruction locale à la désingularisation. En effet, en combinant l’exis-tence de désingularisations montrée dans [Biq13] avec notre résultat d’obstruction, dans le cas de métriques d’Einstein non-dégénérées et asymptotiquement hyperbo-liques et ayant une singularité R4/Z2, on voit qu’il existe une désingularisation au sens de Gromov-Hausdorff (et avec une vitesse de convergence donnée à l’infini) grâce la métrique d’Eguchi-Hanson si et seulement si la condition det R(go) = 0 est satisfaite. 

Remarque 5.79 . Nous ne pouvons pour l’instant pas déduire de résultat d’obstruc-tion si des arbres de singularités non kählériens apparaissent. La raison est qu’il n’y a pas de raison que les arbres d’orbifolds ALE Ricci-plats se recollent en une métrique Ricci-plate ALE. Les obstructions à ce recollement Ricci-plat pourraient alors compenser celles venant des termes de courbure de l’orbifold si les bulles les plus profondes apparaissent à des échelles relatives plus lentes. 

# 5 Obstructions sous des hypothèses topologiques 

Donnons maintenant des conditions topologiques qui assurent que les bulles qui apparaissent sont kählériennes. Cela nous permet de montrer des résultats d’obstructions sous ces conditions dans le théorème 5.84, et le corollaire 5.86. 226 Chapitre 5. Obstructions à la désingularisation 

5.1 Inégalité de Hitchin-Thorpe et désingularisations d’orbifolds d’Einstein 

Dans cette partie, nous montrons que désingulariser un orbifold d’Einstein par des métriques d’Einstein détériore nécessairement l’inégalité de Hitchin-Thorpe satisfaite par l’orbifold, voir le théorème 5.84. Le cas où l’inégalité est préservée est le cas précis où tous les orbifolds Ricci-plats ALE des arbres de singularités sont kählériens et que tous les recollements se font dans la même orientation, et il y a alors obstruction. Dans le cas des orbifolds et des variétés ALE, pour être cohérent avec la formule de Chern-Gauss-Bonnet (2.2) et la formule de Hirzebruch (2.3) pour les variétés d’Einstein compactes de dimension 4, il faut modifier la définition topologique de la caractéristique d’Euler et de la signature à l’aide d’un terme de bord. Il se trouve que les quantités intégrales (2.2) et (2.3) définies dans le chapitre 2 sont des invariants topologiques lorsque l’on considère des orbifolds et espaces ALE si l’on fixe des comportements ALE à l’infini et orbifolds aux singularités. Nous les noterons ˜ χ et ˜ τ pour les distinguer de la caractéristique d’Euler et de la signature habituels. Pour les variétés Ricci-plates ALE, Nakajima a obtenu une inégalité tout à fait analogue à celle d’Hitchin-Thorpe. 

Théorème 5.80 ([Nak90, Theorem 4.2]) . Soit (N, g b) une variété Ricci-plate ALE de dimension 4. Alors, on a l’inégalité suivante entre la caractéristique d’Euler et la signature des orbifolds ALE, 

2 ˜ χ(N ) > 3|˜τ (N )|,

avec égalité si et seulement si (N, g b) est un orbifold Ricci-plat ALE kählérien. Remarque 5.81 . En particulier, les seules variétés Ricci-plates ALE difféomorphes à des résolutions minimales de singularités ou leurs quotients sont kählériennes. Les invariants ˜ τ et ˜ χ sont additifs par recollement de variétés ALE à un orbifold (avec la même orientation pour ˜ τ ). Si M = Mo#j Nj , on a alors 

τ (M ) = ˜ τ (Mo) + ∑

> j

˜τ (Nj ),

et 

χ(M ) = ˜ χ(Mo) + ∑

> j

˜χ(Nj ).5. Obstructions sous des hypothèses topologiques 227 Cela implique directement : 2χ(M ) − 3|τ (M )| = 2 

> (

˜χ(Mo) + ∑

> j

˜χ(Nj )

> )

− 3

> ∣∣∣∣

˜τ (Mo) + ∑

> j

˜τ (Nj )

> ∣∣∣∣

> 2 ˜ χ(Mo) − 3|˜τ (Mo)| + ∑

> j
> (

2 ˜ χ(Nj )) − 3|˜τ (Nj )|)

> 2 ˜ χ(Mo) − 3|˜τ (Mo)|.

Comme tous les termes sont positifs, on voit qu’il y a égalité si et seulement si pour tout j on a 2 ˜ χ(Nj ) − 3|˜τ (Nj )| = 0 et qu’en plus tous les recollements sont faits dans une même orientation pour laquelle ˜ τ (Mo) et tous les ˜ τ (Nj ) sont du même signe. 

Exemple 5.82. Si ( Mo, g o) est un orbifold hyperkählérien, alors les seules désin-gularisations au sens de Gromov-Hausdorff préservant l’inégalité sont hyperkählé-riens et correspondent au recollement de bulles hyperkählériennes dans la même orientation. 

Exemple 5.83. La sphère S4 peut être vue comme S4 ⊂ R5 = R × R4. On notera S4/Γ la variété obtenue comme quotient de S4 par l’action de Γ pour les 4 premières coordonnées de R5. L’orbifold obtenu a des courbures sectionnelles constantes égales à 1, et deux points singuliers aux pôles avec des singularités modelées sur R4/Γ. Pour Γ ⊂ SU (2), une désingularisation d’Einstein de S4/Γ préservant l’inéga-lité de Hitchin-Thorpe est nécessairement difféomorphe à M = S4/Γ# XΓ#XΓ

pour XΓ une résolution minimale de la singularité S2/Γ. Par exemple, c’est le cas pour pour XZ2 = T ∗S2, S4/Z2#T ∗S2#T ∗S2 = S2 × S2.En étudiant le cas d’égalité dans les inégalités précédentes, on obtient une situation assez restreinte. 

Théorème 5.84. Soit (Mo, g o) un orbifold d’Einstein avec l’orientation donnant 

˜τ (Mo) > 0, et supposons que (M, g i)i soit une suite de métriques d’Einstein conver-geant au sens de Gromov-Hausdorff vers (Mo, g o).On a alors l’inégalité suivante, 

2χ(M ) − 3|τ (M )| > 2 ˜ χ(Mo) − 3˜ τ (Mo).

De plus, on a égalité, si et seulement si M est une désingularisation de Mo par recollement d’arbres d’orbifolds kählériens Ricci-plates ALE dans la même orien-tation (c’est-à-dire avec des paramètres de recollement dans SO (4) ), et dans ce 228 Chapitre 5. Obstructions à la désingularisation 

cas d’égalité on a la condition 

det R+(go) = 0 

à tous les points singuliers. Remarque 5.85 . La condition d’égalité limite les groupes des singularités pouvant apparaître. Une application directe de ce théorème est par exemple le résultat suivant. 

Corollaire 5.86. Soit Γ ⊂ SU (2) , (Mi, g i)i une suite de métriques d’Einstein convergeant au sens de Gromov-Hausdorff vers l’orbifold sphérique S4/Γ. Alors, pour i assez grand, nous avons 

2χ(Mi) − 3|τ (Mi)| > 2 ˜ χ(Mo) − 3|˜τ (Mo)|.

5.2 Variétés spin 

Une autre manière d’assurer que les bulles apparaissant sont bien des instantons gravitationnels est d’imposer à la suite de variétés dégénérant d’être spin. Notre résultat est essentiellement une application du théorème suivant de Nakajima. 

Théorème 5.87 ([Nak90, Corollary 3.3]) . Soit (N, g b) une variété spin et Ricci-plate ALE asymptotique à R4/Γ pour Γ un sous-groupe fini de SU (2) , alors, (N, g b)

est un instanton gravitationnel. 

Nous en déduisons un résultat d’obstruction pour les désingularisations d’or-bifolds par des métriques d’Einstein spin. La preuve du théorème 1.1 de [KL16] dont l’outil principal est le théorème 5.87 implique que l’orbifold limite et les bulles apparaissant sont spin et recollées dans la même orientation. Si les bulles sont asymptotiques à des quotients de R4 par des sous-groupes de SU (2), on utilise le théorème 5.87 pour obtenir le corollaire suivant. 

Théorème 5.88. Soit (Mi, g i)i une suite de variétés spin d’Einstein de dimension 

4 convergeant vers un orbifold d’Einstein (Mo, g o). Alors, (Mo, g o) est spin et à ses points singuliers ayant un groupe inclus dans SU (2) , on a 

det R = 0 .

Remarque 5.89 . Il n’y avait pas de restriction sur le groupe des singularités dans le cadre de [KL16]. Cela vient du fait que dans la preuve de [KL16], des hypothèses 5. Obstructions sous des hypothèses topologiques 229 (topologiques encore une fois) sont faites sur le noyau de l’opérateur de Dirac de la suite dégénérant ce qui assure chez [KL16] que l’orbifold limite n’a que des singularités données par des sous-groupes de SU (2). 

5.3 Bornes sur la courbure de Ricci et condition d’Einstein 

Notre résultat montre qu’il y a une différence fondamentale entre la condition d’Einstein et des conditions de pincement sur la courbure de Ricci lorsque l’on autorise la formation de singularités. On déduit des corollaires 5.84 et 5.86 qu’il existe une obstruction à la désingularisation d’orbifolds d’Einstein par des mé-triques d’Einstein lisses qui n’est pas présente sous l’hypothèse que la courbure de Ricci est arbitrairement pincée. 

Figure 5.1 – Exemple de situation obstruée. 

Corollaire 5.90. Soit Γ un sous-groupe fini de SU (2) , et M = S4/Γ# XΓ#XΓ

(recollement aux deux singularités orbifolds), où XΓ est la résolution minimale de la singularité C2/Γ. Alors, pour tout 1 6 p < +∞,1. il existe une suite de métriques (M, g i)i telles que l’on ait — ‖ Ric( gi) − 3gi‖Lp(gi) 6 1 

> i

,— Ric( gi) > 3gi (ou bien Ric( gi) 6 3gi), et — (

M, g E

> i
> )

−−→

> GH
> (

S4/Γ, g S4/Γ

> )

,mais, 2. il n’ existe pas de suite de métriques d’Einstein (M, g E 

> i

) telle que — Ric( gE 

> i

) = 3 gE 

> i

, et — (

M, g E

> i
> )

−−→

> GH
> (

S4/Γ, g S4/Γ

> )

.230 Chapitre 5. Obstructions à la désingularisation 

Démonstration. La seconde partie est une conséquence du corollaire d’obstruction 5.32 car la courbure de la sphère ne satisfait jamais la condition det R = 0. Pour la première partie, on remarque que notre métrique d’approximation gAt

définie dans le corollaire 5.9 satisfait ‖ Ric( gAt ) − ΛgAt ‖L∞(gAt ) = O(1) mais est seulement non-nulle sur des domaines de volume de l’ordre de t, et qu’en choisis-sant des ti suffisamment petit, on a donc le contrôle en norme Lp pour p < +∞.Pour obtenir une désingularisation avec une courbure de Ricci minorée (ou majorée de la même manière) par celle de l’orbifold, il faut être un peu plus fin. Notons tout d’abord qu’en calculant les obstructions à la désingularisation de S4/

Z2 par des métriques d’Eguchi-Hanson avec une échelle maximale tmax suffisam-ment petite, nous avons 

| Ric( gAt ) − 3gAt |gAt 6 1 + δ(tmax ) (5.57) où δ(tmax ) → 0 quand tmax → 0. Considérons pour ε > 0 et b > 1, une fonction de coupure χb,ε , supportée [0 , bε ] et égale à 1 on [0 , ε ] dont la k-ième dérivée est un O( 1log( b) ε−k)

. Une manière de construire une telle fonction est la suivante, soit u : R → R+ une fonction de coupure C∞ égale à 1 sur [ −∞ , 0], et s’annulant sur [1 , +∞]. Soient ε > 0 et b > 1et posons 

χb,ε : x ∈ R4 7 → u 

> (

log( |x|/ε )log b

> )

. (5.58) Elle satisfait bien les propriétés attendues. Définissons alors la métrique 

gb,ε := dr 2 + sin (

(1 + χb,ε )r)

gS3/Γ.

Supposons que ε → 0, b → +∞ et bε → 0, la métrique orbifold devient alors arbitrairement proche de S4/Γ au sens de Gromov-Hausdorff. De plus, les cour-bures sectionnelles de gb,ε sont minorées par 1 − C  

> log b

→ 1 pour une constante 

C > 0 uniforme. Recollons alors naïvement t(gEH + 2 th 2), où h2 est asymptotique à −13 r2 

> e

gS3/Γ aux points singuliers avec tmax  ε2, afin que la zone de recollement se trouve dans 0 6 r < ε où la métrique gb,ε est égale à dr 2 + sin 2(2 r)gS3/Γ comme pour la sphère de rayon 12 dont les courbures sectionnelles sont constantes égales à 4. Pour r < ε , les contrôles sont les mêmes que sur gAt 

> 4

, et la métrique satisfait donc Ric > 3 par (5.57) car 4 (

3 − (1 − δ(tmax )) )

> 3. Comme la métrique satisfait 6. Une obstruction générale 231 Ric > 3− C 

> log( b)

pour les r plus grands, on peut simplement réechelonner légèrement (en fonction de C 

> log bb→∞

−−−→ 0) pour s’assurer d’avoir Ric > 3 partout. La question reste cependant ouverte pour le cas des pincements de la courbure de Ricci en norme L∞.

Question 5.91. Existe-t-il une suite de variétés ( S2 × S2, g i) satisfaisant 3 − 1 

> i

6

Ric( gi) 6 3 + 1 

> i

convergeant au sens de Gromov-Hausdorff vers S4/Z2 ?

# 6 Une obstructions à la désingularisation d’orbifolds sphériques et hyperboliques 

Nous exhibons finalement une obstruction à la désingularisation d’orbifolds sphériques et hyperboliques par des variétés Ricci-plates ALE générales (pas néces-sairement kählériennes) dans le théorème 5.98. Nous en déduirons qu’il n’existe pas de désingularisation d’orbifolds sphériques ou hyperboliques au sens de Gromov-Hausdorff à l’aide de variétés Ricci-plates ALE dont les déformations infinitési-males sont intégrables dans le corollaire 5.100. 

6.1 Production de déformations infinitésimales par prolongement de champs de Killing conformes à l’infini 

Nous proposons une construction de déformations infinitésimales par prolon-gements harmoniques des isométries du cône asymptotique d’un espace Ricci-plat ALE quelconque (et en particulier pas nécessairement kählérien). Cela éclaire de plus le sens des déformations infinitésimales de gEH .

Changement d’échelle. Proposition 5.92. Soit (N, g b) un orbifold Ricci-plat ALE asymptotique à R4/Γ,et un difféomorphisme Φ entre voisinages de l’infini de N et R4/Γ.Alors, il existe un unique champ de vecteurs X sur (N, g b) tel que Φ∗X =2re∂re + o(re), ∇∗∇X = 0 et X = ∇u, où u est l’unique solution de −∇ ∗∇u = 8 ,telle que u = r2 

> b

+ o(1) .

De plus, (LX gb)◦ = LX gb−4gb, la partie sans trace de LX gb est une déformation infinitésimale de gb à divergence et trace nulle. 232 Chapitre 5. Obstructions à la désingularisation 

Démonstration. L’existence et l’unicité de la fonction u est obtenue dans la preuve du théorème 2 de [BH19]. Le 2-tenseur ( L∇ugb)◦ est bien une déformation infini-tésimale L2 de gb car l’équation Ric = 0 est invariante par changement d’échelle et action du groupe des difféomorphismes, mais aussi que la divergence et la trace de ( L∇ugb)◦ = 2Hess gb u − 4gb s’annulent car −∇ ∗∇u = 8. 

Exemple 5.93. La déformation o1 := O41 + O(r−6 

> b

) de la métrique d’Eguchi-Hanson est proportionnelle à cette déformation. 

Rotation de l’infini. En jouant sur les symétries des termes d’ordre −4 de l’orbifold. Il y a en général un espace de dimension dim (SO (4)) = 6 de déforma-tions ainsi construites, mais certaines peuvent s’annuler en fonction des symétries de l’ALE. Par exemple, la métrique d’Eguchi-Hanson est invariante par U (2) qui est de dimension 4, et SO (4) /U (2) est de dimension 2. 

Proposition 5.94 ([BH19, Section 4]) . Soit (N, g b) un orbifold Ricci-plat ALE asymptotique à R4/Γ, et un difféomorphisme Φ entre voisinages de l’infini de N

et R4/Γ.Alors, pour tout X0 ∈ so (4) , il existe un unique champ de vecteurs harmonique sur (N, g b) tel que 

Φ∗X = X0 + o(re).

De plus, pour un tel champ de vecteurs X, LX gb est une déformation infinité-simale de gb à divergence et trace nulle. Elle s’annule si et seulement si X est un champ de Killing de gb.

Exemple 5.95. Les déformations oi = O4 

> i

+ O(r−6 

> b

) pour i = 2 ou i = 3 de la métrique d’Eguchi-Hanson sont proportionnelles à ces déformations par rotation de l’infini pour X0 valant le champ de Killing de S3 respectivement dual de α3 et de α2.

Remarque 5.96 . Ces déformations sont intégrables car elles viennent simplement de changement de coordonnées et d’échelle de la variété globale. Ainsi, une variété rigide, c’est-à-dire dont toutes les déformations sont de ce type, n’aura que des déformations intégrables et entrera dans le cadre du corollaire 5.100 de la fin de cette partie. La métrique d’Eguchi-Hanson en est un exemple et heuristiquement la plupart des métriques d’Einstein devrait l’être. 6. Une obstruction générale 233 

6.2 Orbifolds Ricci plats ALE et volume maximal 

Résumons ici des résultats obtenus par Biquard-Hein dans [BH19]. Nous les uti-liserons pour montrer que la déformation infinitésimale que l’on vient de construire dans la proposition 5.92 est non-nulle et peut donc être utilisée pour exhiber des obstructions à certaines désingularisations. 

Théorème 5.97 ([BH19, Theorem A, Theorem B]) . Soit (N, g b) un orbifold Ricci-plat ALE asymptotique à un cône plat R4/Γ, soit Ψ un difféomorphisme entre les infinis de (N, g b) et de son cône asymptotique R4/Γ, et soit u est l’unique solution de −∇ ∗∇u = 8 , u = r2 

> b

+ o(1) . Alors, il existe un compact K ⊂ M tel que M \K

soit feuilleté par des hypersurfaces Σρ à courbure moyenne constante 3 

> ρ

.De plus, si l’on note Ωρ l’intérieur de Σρ, la limite suivante existe : 

V := lim 

> ρ→∞
> [

Vol gb (Ω ρ) − Vol ge (B(0 , ρ )/Γ) ]

, (5.59) 

et on a en fait V 6 0, avec égalité si et seulement si (N, g b) = ( R4/Γ, g e).On a de plus le développement plus précis 

u = r2 

> b

+ br2

> b

+ O(r−3 

> b

),

avec 

b = −4 V|∂B (0 , 1) /Γ| > 0.

On a l’expression suivante pour le développement de (L∇gb ugb)◦ = (2Hess gb u − 4gb)(L∇gb ugb)◦(∂rb , ∂ rb ) = 8br4

> b

+ O(r−5 

> b

) (5.60) 

6.3 Obstruction à la désingularisation d’orbifolds sphériques et hyperboliques 

Nous allons maintenant tirer profit du fait que la déformation o1 = (2Hess gb u−

4gb) ne s’annule jamais pour une métriques non plate. 

Théorème 5.98. Soit (N, g b) un orbifold Ricci-plat ALE et H2 les termes qua-dratiques d’une métrique sphérique ou hyperbolique en coordonnées géodésiques, et 

O41 les termes d’ordre −4 de la déformation o1 = (2Hess gb u − 4gb).Alors, on a ∫

> S3
> (

3〈H2, O 41 〉ge + O41 (BeH2, ∂ re ))

dv 6 = 0 .234 Chapitre 5. Obstructions à la désingularisation 

Remarque 5.99 . Il est donc impossible de désingulariser de manière classique (or-thogonalement au noyau) ces orbifolds d’après le corollaire 5.12. 

Démonstration. Pour une métrique hyperbolique, on a H2 = r4 

> e
> 3

(α21 + α22 + α23) en coordonnées géodésiques, et pour une métrique sphérique, H2 = −r4 

> e
> 3

(α21 +α22 +α23). Remarquons alors que, comme ge = dr 2 

> e

+ r2 

> e

(α21 + α22 + α23), on a 0 = tr ge O41 =

O41 (∂re , ∂ re ) + 〈r2 

> e

(α21 + α22 + α23), O 41 〉 et donc 

〈r2 

> e

(α21 + α22 + α23), O 41 〉ge =tr ge O41 − O41 (∂re , ∂ re )= − O41 (∂re , ∂ re ).

Pour l’autre partie de l’obstruction, on a Be

(

r4 

> e

(α21 + α22 + α23))

= 6 re∂re . En effet, 

r4 

> e

(α21 + α22 + α23) = r2 

> e

ge − r2 

> e

dr 2 

> e

, et 

Be(r2 

> e

ge) = δe(r2 

> e

ge) + 12dtr e(r2 

> e

ge)= −2rege(∂re ) + 4 redr e

= 2 redr e,

et 

Be(r2 

> e

dr 2 

> e

) = δe(r2 

> e

dr 2 

> e

) + 12dtr e(r2 

> e

dr 2 

> e

)= δe

( ∑

> ij

xixj dx idx j

)

+ redr e

= − ∑ 

> i6=j

xj dx j − 2 ∑

> j

xj dx j + redr e

= −4redr e.

Et donc finalement, en re = 1, 

O41 (Be

(

r4 

> e

(α21 + α22 + α23))

, ∂ re ) = 6 O41 (∂re , ∂ re ) = −192 V|∂B (0 , 1) /Γ| > 0.