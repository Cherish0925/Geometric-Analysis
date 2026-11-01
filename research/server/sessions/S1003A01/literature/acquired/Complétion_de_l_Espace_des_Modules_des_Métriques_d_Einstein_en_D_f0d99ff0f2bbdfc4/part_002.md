---
retention_scope: session
part: 2
total_parts: 7
---

[Part 2/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

tr ghdvg = 0 avec les notations du lemme ci-dessus. Les métriques proches en jauge divergence et de même volume que g0 au voi-sinage de g0 sont donc exactement Φ−1 

> g0

({0}). Il se trouve que pour une métrique d’Einstein g0, la linéarisation de Φg0 en g0 appliquée à un 2-tenseur h satisfaisant  

> ∫
> M

tr g0 hdvg0 = 0 est 12

> (

∇∗ 

> g0

∇g0 h − 2 ˚Rg0 (h) − ∇ 2 

> g0

tr g0 h − (δg0 δg0 h)g0 + (∆ g0 tr g0 h)g0 + Λ(tr g0 h)g0

> )

qui est un opérateur autoadjoint et elliptique (et donc Fredholm). Il a donc en particulier un noyau de dimension finie. On appelle son noyau l’ensemble des 

déformations infinitésimales d’Einstein de g0.

Remarque 1.23 . Koiso caractérise de plus ces déformations d’ essentielles car elles sont transverses aux déformations triviales de changement d’échelle et d’action par le groupe des difféomorphismes. 

Lemme 1.24. L’ensemble des déformations infinitésimales de g0 est l’ensemble des 2-tenseurs symétriques h sur M tels que dg0 Φg0 (h) = 0 et ∫ 

> M

tr g0 hdvg0 = 0 

(ce qui fixe infinitésimalement le volume). C’est équivalent à avoir 34 Chapitre 1. Espace de modules des métriques d’Einstein 

— tr g0 h = 0 

— δg0 h = 0 

— Pg0 (h) := 12 ∇∗ 

> g0

∇g0 h − ˚Rg0 (h) = 0 .Démonstration. La linéarisation de l’opérateur Φg0 en g0 d’Einstein et dans la direction de h satisfaisant ∫ 

> M

tr g0 hdvg0 = 0 est (dg0 Φg0 )( h) = 12

> (

∇∗∇h − 2˚R( h) − ∇ 2trh − (δδh )g0 + (∆ trh )g0 + Λ( trh )g0

> )

,

où toutes les opérations sont faites par rapport à g0.Intéressons-nous à son noyau et linéarisons g 7 → δg(Φg0 (g)) = δgδ∗ 

> g

δg0 g en 

g0 dans la direction h du noyau de dg0 Φg0 , cela donne 0 = δg0

> (

dg0 Φg0 (h))

=(δg0 δ∗ 

> g0

)δg0 h car Φg0 (g0) = 0. Par inversibilité de δg0 δ∗ 

> g0

sur l’image de δg0 on obtient 

δg0 h.L’équation ( dg0 Φg0 )( h) = 0 se simplifie donc en 

∇∗∇h − 2˚R( h) − ∇ 2trh + (∆ trh )g + Λ( trh )g = 0 .

Si Λ 6 0, en prenant la trace de cette expression, comme Ric( g0) = Λ g0, on obtient ∆g0 tr g0 h + Λtr g0 h = 0 . (1.12) Il est alors clair par intégration par parties contre h sur notre variété compacte sans bord que si la moyenne de la trace de h est nulle, alors tr g0 (h) = 0. Si Λ > 0, quitte à effectuer un changement d’échelle, on peut supposer que Λ = n − 1. La première valeur propre de −∆, λ1 satisfait alors λ1 > n avec égalité sur la sphère seulement. En effet, si ∆ f + λ1f = 0, alors ∆ df + λ1df = 0. Par la formule de Bochner, on a alors (∇∗∇ − λ1)df + Ric( df ) = 0 ,

et donc, en prenant le produit scalaire avec df ,

‖∇ df ‖2 − λ1‖df ‖2 6 −(n − 1) ‖df ‖2.

Maintenant, comme ∆ f = tr (∇df ), on a l’inégalité 

‖∇ df ‖2 > 1

n‖∆f ‖2 = λ1

n ‖df ‖2.

On obtient donc bien λ1 > n, et (1.12) implique que trh = 0. 3. Structure au voisinage d’une métrique lisse 35 

# 3 Structure de l’espace de modules autour d’une métrique lisse 

Le pré-espace de modules des métriques d’Einstein au voisinage de g0, définition 1.17, Eg0 (M ) a une structure analytique au voisinage de g0.

3.1 Applications analytiques entre espaces de Banach 

Rappelons des définitions et théorèmes de base sur les applications analytiques entre espaces de Banach et les sous-ensembles analytiques qui nous serons utiles. Soient ak : V k → W , k ∈ N des formes k-linéaires symétriques continues sur 

V à valeur dans W . La série entière notée x ∈ V 7 → ∑ 

> k

akxk ∈ W d’un espace de Banach V à valeur dans un espace de Banach W est définie comme la somme des 

ak(x, ..., x ). On dira quelle converge si la somme réelle ∑ 

> k

‖ak(x, ..., x )‖W converge. On en dérive la définition d’une application analytique 

Définition 1.25 (Application analytique) . Soient V et W des espaces de Banach, et U un ouvert de V . Une application f : V → W est dite analytique si pour tout point x ∈ U , f est égale à une série entière convergente au voisinage de x.Cette définition est adaptée au cadre de l’analyse, et en particulier, le théorème des fonctions implicites est valable pour cette régularité. 

Lemme 1.26 ([Whi65, Implicit Function Theorem, p. 1081]) . Soient X, Y et Z

des espaces de Banach, et A un ouvert de X × Y . Supposons qu’une application analytique f : A → Z satisfasse pour (x0, y 0) ∈ A,1. f (x0, y 0) = 0 ,

2. d(x0,y 0)f (0 , . ) : Y 7 → Z est un homéomorphisme. Alors, 1. il existe N (x0), un voisinage ouvert de x0 dans X et une unique application continue g : N (x0) → Y telle que g(x0) = y0, (x, g (x)) ∈ A pour x ∈ N (x0),et 

f (x, g (x)) = 0 ,

2. g est analytique, 36 Chapitre 1. Espace de modules des métriques d’Einstein 

3. dxg = −(

d(x,g (x)) f (0 , . ))−1

◦ (

d(x,g (x)) f (., 0) )

.

Plus tard dans cette thèse, on se basera sur des métriques seulement approxi-mativement d’Einstein et qui ne seront pas analytiques. Il sera crucial de noter que les opérations entre tenseurs n’ayant qu’une régularité Hs locale pour s assez grand en fonction de la dimension ou ayant une régularité Ck,α pour k plus grand que le nombre de dérivations sont en fait analytiques. Cela s’obtient en étendant la preuve de [Koi83, Lemma 13.7] au cas (plus simple) des espaces de Hölder. L’outil principal est la théorie développée dans [Pal68] et la propriété cruciale est que pour ces régularités, l’ensemble de fonctions forme une algèbre muni de la multiplication ponctuelle. 

Lemme 1.27. Soient E et F des fibrés vectoriels sur une variété M de dimension 

n ∈ N, et EC et F C leurs complexifications. Soit f une section de E, et soit 

ψ : U ⊂ E → F , où U est un voisinage de l’image de f , une application C∞

préservant les fibres. Supposons que ψ admette une extension ψC : U C ⊂ EC → F C

préservant les fibres telle que la restriction de ψC à chaque fibre soit holomorphe. Alors, l’application Ψ : Hs(E) → Hs(F ) définie par 

Ψ( u) = ψ ◦ u

définie sur un voisinage de l’image de f est analytique pour s > ⌊ n

> 2
> ⌋

+ 1 .De même, l’application Ψ : Ck,α (E) → Ck,α (F ) définie par Ψ( u) = ψ◦u définie sur un voisinage de l’image de f est analytique pour k + α > 0.

Nous n’aurons en particulier pas besoin d’utiliser la régularité analytique des fonctions ou des métriques auxquelles on aura affaire, mais seulement une régula-rité partielle. 

Corollaire 1.28 ([Koi83, Lemma 13.9]) . La composition, la différenciation et les contractions sont des opérations analytiques entre espaces Hs locaux pour s

suffisamment grand en fonction de la dimension et de l’opération. C’est aussi le cas entre espaces Ck,α pour tout k, α tels que k + α plus grand que le nombre de dérivations. 

3.2 Structure d’ensemble analytique de l’espace de modules 

Nous allons montrer qu’au voisinage d’une métrique lisse g0, le pré-espace de modules Eg0 (M ) a une structure de sous-ensemble analytique d’une sous-variété analytique de dimension finie de M(M ). 3. Structure au voisinage d’une métrique lisse 37 

Définition 1.29 (Sous-ensemble analytique) . Soit X une variété analytique. Nous dirons que Z ⊂ X est un sous-ensemble analytique de X s’il existe d ∈ N et une application analytique F : X → Rd telle que 

Z = F −1{0}.

Remarque 1.30 . D’après le profond théorème de structure de Łojasiewicz (voir [Łoj65]), un sous-ensemble analytique est une union de sous-variétés analytiques. 

3.2.1 Structure analytique du pré-espace de modules classique 

La preuve classique de la structure de sous-ensemble analytique du pré-espace de modules due à Koiso consiste à s’intéresser à l’ensemble des zéros de Φg0 .

Proposition 1.31 ([Koi83, Theorem 3.1]) . Soit g0 une métrique d’Einstein sur une variété M . Alors, il existe U un voisinage ouvert de g0 dans M(M ) muni de la distance C2,α (g0) tel que l’espace Φ−1 

> g0

({0}) ∩ U ait une structure de sous-ensemble analytique d’une sous-variété analytique Wg0 de M(M ) de dimension finie. De plus l’espace tangent à Wg0 , Tg0 Wg0 est l’ensemble ker dg0 Φg0 des déformations infinitésimales de g0.Démonstration. Soit M n une variété différentielle et g0 une métrique d’Einstein sur 

M de volume 1. Démarrons cette preuve en définissant la variété Wg0 sur laquelle on s’appuiera. Pour 0 < α < 1 et k ∈ N, l’application Φg0 : Ck+2 ,α → Ck,α est analytiques grâce au corollaire 1.27. On définit πg0 : Ck,α → Im( dg0 Φg0 ) une projection sur Im( dg0 Φg0 ) (dont un supplémentaire est de dimension finie). Et posons Fg0 = πg0 Φg0 : Ck+2 ,α →

Im( dg0 Φg0 ). C’est une submersion par construction, et l’ensemble 

Wg0 := F −1 

> g0

({0}),

est alors une variété analytique de dimension finie dont l’espace tangent à g0 est ker dg0 Φg0 par le théorème des fonctions implicites qui assure de plus que son espace tangent est l’ensemble des déformations infinitésimales de g0.Maintenant, Φg0 est une fonction analytique sur la variété analytique Wg0 , et 

Φ−1 

> g0

({0}) en est donc une sous-variété analytique. 

Remarque 1.32 . On voit donc qu’a priori, l’ensemble Φ−1 

> g0

({0}) est de dimension inférieure à Wg0 . La raison en est que toutes les déformations infinitésimales ne sont pas intégrables , c’est-à-dire qu’étant donnée h une déformation infinitésimale 38 Chapitre 1. Espace de modules des métriques d’Einstein de g0, il n’existe pas nécessairement de courbe t ∈ [−1, 1] → gt ∈ Φ−1 

> g0

({0}) de métriques telles que ∂tgt|t=0 = h. Lorsque pour une déformation infinitésimale h,une telle courbe existe, on qualifiera h d’ intégrable Remarque 1.33 . L’intégrabilité d’une déformation infinitésimale h est équivalente à son intégrabilité formelle, c’est-à-dire à l’existence d’une série g0 + th + ∑  

> l>2tl
> l!

hl

satisfaisant formellement l’équation d’Einstein, voir [Koi83, Theorem 3.2] dont la preuve est une application de [Art68]. 

Corollaire 1.34. Soit g0 une métrique d’Einstein sur une variété M . Si toutes les déformations infinitésimales de g0 sont intégrables, alors le pré-espace de modules 

Eg0 (M ) a une structure de sous-variété analytique dans un voisinage de g0 et son espace tangent est l’ensemble des déformations infinitésimales de g0.

3.2.2 Un nouveau pré-espace de modules adaptable au voisinage d’une métrique non-lisse 

Nous proposons une construction de pré-espace de modules qui se générali-sera au voisinage des métriques singulières, voir la dernière section du chapitre 4. L’objectif est de définir une section de l’espace de modules des métriques d’Ein-stein (à isométries près) sans avoir à mettre nos métriques en jauge par rapport à g0, ce qui ne sera pas possible dans le cas singulier où la métrique g0 ne sera pas lisse ou pas définie sur la même variété. Définissons, pour une métrique g,

πg := Id − δ∗ 

> g

(δgδ∗ 

> g

)−1δg, où ( δgδ∗ 

> g

)−1 est l’inverse de δgδ∗ 

> g

: ker( δg)⊥g → ker( δg)⊥g

une projection sur le noyau de δg. Nous allons définir une autre section du pré-espace de modules au voisinage d’une métrique g0 compact ou ALE. En notant 

O(g0) le noyau L2 de Pg0 sur l’ensemble des 2-tenseurs à trace et divergence nulles, et en en choisissant ( oi){16i6d} une base orthonormée, nous définissons pour 

v = ( v1, ..., v d) ∈ Rd la métrique 

gv := g0 +

> d∑
> i=1

vioi

qui est une première approximation d’une potentielle déformation d’Einstein de 

g0 dans la direction v. L’ensemble des gv pour v ∈ Rd est l’espace tangent en g0 àl’ensemble des métriques que l’on qualifiera d’Einstein modulo obstructions par la suite. 

Une nouvelle mise en jauge. 3. Structure au voisinage d’une métrique lisse 39 

Lemme 1.35. Soit (M n, g 0) une variété d’Einstein compacte. Alors, pour tout 

k ∈ N et 0 < α < 1 il existe ε > 0 tel que pour toute métrique g satisfaisant 

‖g − g0‖Ck,α 6 ε et Vol( g) = Vol( g0), il existe un unique v ∈ O(g0) pour lequel il existe un difféomorphisme ϕ : M → M et une constante c > 0 tels que l’on ait 

δgv (ϕ∗g) = 0 ,

et 

ϕ∗g − gv ⊥gv πgv O(g0).

De plus, le difféomorphisme ϕ est proche de l’identité en norme Ck+1 ,α , et v est proche de 0.Démonstration. D’après le théorème de la tranche d’Ebin, lemme 1.16 et sa preuve, lemme 1.15, pour toute métrique g et tout v ∈ Rd suffisamment petit, il existe un unique champ de vecteurs X(g, v ) ⊥gv ker δ∗ 

> g0

tel que l’on ait 

δgv exp ∗ 

> X(g,v )

g = 0 .

Nous cherchons alors naturellement v tel qu’on ait en plus exp ∗ 

> X(g,v )

g − gv ⊥gv

πgv O(g0). Or, comme δgv (exp ∗ 

> X(g,v )

g −gv) = 0, c’est équivalent à avoir exp ∗ 

> X(g,v )

g −

gv ⊥gv O(g0) car pour tout o ∈ O(g0), πgv o − o ⊥gv ker δgv .Considérons alors l’application 

F : ( g, v ) 7 → πgv

> O(g0)
> (

exp ∗ 

> X(g,v )

g − gv

> )

,

où πgv 

> O(g0)

est la projection orthogonale pour gv sur O(g0). Nous considérerons F

sur un voisinage de ( g0, 0) dans (

Ck,α ∩ { g′| Vol( g′) = Vol( g0)})

× Rd, pour k ∈ N

à valeur dans O(g0). On peut lui appliquer le théorème des fonctions implicites, lemme 1.26. En effet, F (g0, 0) = 0 et d(g0,0) F (0 , v ) = v est bien un isomorphisme et les espaces (

Ck,α ∩ { g′| Vol( g′) = Vol( g0)})

× Rd et O(g0) sont bien de Banach. Ainsi, il existe une application analytique (unique en tant qu’application continue) 

V telle que pour toute métrique g dans un voisinage de g0, on ait 

F (g, V (g)) = 0 .

On en déduit en particulier, pour toute métrique g d’Einstein dans un C1,α -voisinage de g0 telle que Vol( g) = Vol( g0), il existe un unique élément de Rd, V (g), 40 Chapitre 1. Espace de modules des métriques d’Einstein tel que 1. δgV (g) (exp ∗  

> X(g,V (g))

g) = 0, et 2. exp ∗  

> X(g,V (g))

g − gV (g) ⊥gV (g) πgV (g) O(g0). et donc en particulier, nous avons ΦgV (g)

(

exp ∗  

> X(g,V (g))

g)

= 0. Réciproquement, si ˆgv satisfait ΦgV (g)

(

ˆgv

)

= 0, alors Ric(ˆ gv) = Λˆ gv et δgv ˆgv = 0. 

Un nouveau pré-espace de modules au voisinage de g0. Nous définissons alors E∗ 

> g0

(M ) comme l’ensemble des métriques g dans un voisinage C1,α de g0

satisfaisant, il existe v ∈ Rd tel que : 1. Ric( g) = Λ g, Vol( g) = Vol( g0), 2. g − gv ⊥gv πgv O(g0), 3. δgv g = 0. Pour chaque v, nous allons voir qu’il existe au plus une solution à l’aide d’une réduction de Lyapunov-Schmidt dans la proposition suivante. Les v pour lesquels il existe ˆ gv satisfaisant ˆ gv − gv ⊥gv πgv O(g0) et ΦgV (g)

(

ˆgv

)

= 0 paramètrent alors 

E∗ 

> g0

(M ) et nous donnent bien une tranche de E(M ) au voisinage de g0 à isométrie près. 

Proposition 1.36. Soit M n une variété différentielle, et soit g0 ∈ E(M ), et d la dimension du noyau L2 de dg0 Φg0 parmi les 2-tenseurs à trace nulle, noté O(g0),et choisissons (oi)i une base orthonormée de O(g0).Alors, il existe ε > 0 tel que pour tout v ∈ Rd tel que |v| < ε , il existe une unique métrique ˆgv telle que si l’on note gv := g0 + ∑ 

> i

vioi,

Φgv (ˆ gv) = E(ˆ gv) + δ∗ 

> ˆgv

δgv ˆgv ∈ πgv O(g0),

et satisfaisant les conditions de jauge suivantes : 1. ‖g0 − ˆgv‖C1,α 6 2ε,2. gv − ˆgv ⊥L2(gv ) πgv O(g0).De plus, l’ensemble des déformations d’Einstein modulo obstructions ,

ˆWg0 := {

ˆgv | v ∈ Rd, |v| < ε }

est une sous-variété analytique de g0 +Ck,α , et l’ensemble des métriques d’Einstein, 

E∗ 

> g0

(M ) = {

ˆgv ∈ ˆWg0 | Φgv (ˆ gv) = 0 }3. Structure au voisinage d’une métrique lisse 41 

est un sous-ensemble analytique de la variété analytique ˆWg0 .Démonstration. Soient ( M n, g 0) une variété d’Einstein, ( oi){16i6d} une base ortho-normée de O(g0), v = ( v1, ..., v d) ∈ Rd, et ∑ 

> i

vioi ∈ O(g0). Dans la preuve qui suit, tous les produits scalaires sont ceux de la métrique gv := g0 + ∑ 

> i

vioi.Soit k ∈ N, le lemme se montre par théorème des fonctions inverses pour les applications analytiques appliqué à l’application analytique Ψ : Rd × Ck+2 ,α →

Ck,α × Ck+2 ,α , qui a une métrique g associe Ψ( v, g ) := 

> (

πgv  

> πgv O(g0)⊥

Φgv (g) , π gv 

> πgv O(g0)

(g − gv)

> )

.

La linéarisation de l’opérateur en gv est inversible pour v suffisamment petit. En effet, en g0, la linéarisation d(0 ,g 0)Ψ(0 , . ) est 

> (

πg0 

> O(g0)⊥

dg0 Φg0 , π g0

> O(g0)
> )

qui est inversible par définition de O(g0) qui est le noyau et le conoyau de la linéarisation de Φg0 .Les termes quadratiques sont classiquement contrôlés à partir de la forme sché-matique des variations de la courbure de Ricci, en notant abusivement ∗ diverses contractions de tenseurs : Ric( g + h) = Ric( g) + ( g + h)−1 ∗ Rm( g) + ( g + h)−2 ∗ ∇ 2h + ( g + h)−3 ∗ ∇ h ∗ ∇ h. 

Il existe donc C > 0 ne dépendant que de g0 tel que ‖Ψ( v, g v)‖Ck,α (g0) 6 C|v|2

par le contrôle des termes non-linéaires. On déduit du théorème des fonctions implicites pour les applications analytiques, lemme 1.26 que pour v suffisamment petit, il existe une unique solution ˆ gv de Ψ(v, ˆgv) = 0 telle que pour C′ > 0 ne dépendant que de g0, on ait 

‖ˆgv − gv‖Ck+2 ,α (g0) 6 C′|v|2.

L’application v → ˆgv est analytique et injective pour v dans un voisinage U de zéro. L’ensemble ˆWg0 := {ˆgv, v ∈ U } a donc une structure de sous-variété analytique de 

Ck+2 ,α pour U suffisamment petit. Sur ˆWg0 , l’application ˆ gv 7 → E(ˆ gv) est analytique et s’annule exactement sur les métriques d’Einstein. 42 Chapitre 1. Espace de modules des métriques d’Einstein 

# 4 Voisinage d’une métrique lisse au sens de Gromov-Hausdorff 

Durant toute la suite de cette thèse, nous étudierons souvent des suites de métriques satisfaisant diverses propriétés de courbure (bien souvent d’Einstein). Il nous sera donc souvent utile d’étudier leur comportement limite. Pour cela, il nous faudra utiliser une topologie ayant de bonnes propriétés de compacité. Une telle topologie sera donnée par la distance de Gromov-Hausdorff. 

4.1 Distance de Gromov-Hausdorff et compacité 

Rappelons tout d’abord les définitions et propriétés de base de la distance de Gromov-Hausdorff. 

Définition 1.37 (Distance de Hausdorff, dH ). Soit ( Z, d ) un espace métrique et soient X et Y des sous-ensembles de Z. On définit la distance de Hausdorff entre 

X et Y comme : 

dHZ (X, Y ) := max 

> (

sup 

> x∈X

d(x, Y ) sup 

> y∈Y

, d (y, X ),

> )

.

Définition 1.38 (Distance de Gromov-Hausdorff, dGH ). Soient ( X, d X ) et ( Y, d Y )deux espaces métriques compacts. On définit la distance de Gromov-Hausdorff, 

dGH , entre ( X, d X ) et ( Y, d Y ) par 

dGH 

> (

(X, d X ) , (Y, d Y ))

:= inf  

> Z

dHZ (X, Y )où l’infimum est pris sur les espaces métriques ( Z, d ) et les plongements isomé-triques de ( X, d X ) et ( Y, d Y ) dans ( Z, d ). 

Remarque 1.39 . Il y a plusieurs définitions différentes de cette distance qui in-duisent la même topologie sur l’ensemble des espaces métriques. La définition que l’on a choisie est celle introduite par Gromov et a l’avantage de justifier le nom de cette topologie. Il est aussi possible de définir la convergence d’espaces non compacts qui revient à une convergence sur les compacts. 

Définition 1.40 (Distance de Gromov-Hausdorff pointée) . Soient ( X, d X , x ) et (Y, d Y , y ) deux espaces métriques pointés. On définit la distance de Gromov-Hausdorff pointée, encore notée dGH , entre ( X, d X , x ) et ( Y, d Y , y ) par l’infimum 4. Voisinage d’une métrique lisse au sens de Gromov-Hausdorff 43 des ε > 0 tels que l’on ait 

dGH 

> (

(X, d X , x ), (Y, d Y , y ))

:= inf {

ε , d GH 

> (

BdX (x, ε −1) , B dY (y, ε −1))

< ε }

Cette notion de distance est entre autres motivée par le crucial théorème de compacité de Gromov, théorème 0.1 énoncé en introduction, mais elle a des appli-cations dans de nombreux autres domaines. 

Remarque 1.41 . La borne sur la courbure de Ricci n’est présente dans les hypo-thèse que parce qu’elle assure que l’espace obtenu est doublant , c’est-à-dire que le volume de ses boules ne peut pas croître à une vitesse plus qu’exponentielle en leur diamètre. 

Remarque 1.42 . Cette notion de convergence a donc d’excellentes propriétés de convergence dans le cadre qui nous intéresse mais est extrêmement faible. En particulier, elle ne dit rien sur les propriétés topologiques d’espaces proches les uns des autres. Par exemple, tout espace métrique compact est limite d’espaces métriques discrets, et il n’y a aucun espoir de contrôler la dimension ou le nombre de composantes connexes sans hypothèse supplémentaire. L’enjeu est alors souvent de tout d’abord étudier les propriétés particulières des métriques de la suite afin de déterminer si les limites possibles ont une certaine régularité. Il convient ensuite d’étudier si la convergence a lieu dans un sens plus fort qui préserverait par exemple des propriétés topologiques, géométriques ou analytiques. 

4.2 Compacité de Cheeger-Gromov 

Un premier exemple d’ensemble de métriques auquel la compacité de Gromov s’applique est l’ensemble des métriques à courbures sectionnelles bornées. La ré-férence [HH97] et les articles mentionnés dedans donnent un bon panorama des premiers résultats de cette théorie. Au contrôle des métriques en coordonnées harmoniques du corollaire 1.5, nous pouvons ajouter le théorème profond de Cheeger-Gromov-Taylor. 

Théorème 1.43 ([CGT82, Theorem 4.7]) . Soit (M, g ) une variété riemannienne dont les courbures sectionnelles sont bornées par K, le volume minoré par v et le diamètre majoré par D.Alors, il existe une borne inférieure i = i(K, v, D ) > 0 sur le rayon d’injectivité de (M, g ).44 Chapitre 1. Espace de modules des métriques d’Einstein 

Esquisse de preuve. Considérons un point x ∈ M , puis tirons en arrière la mé-trique autour de x grâce à des coordonnées géodésiques jusqu’au rayon de conju-gaison, conj x qui est minoré à l’aide des courbures sectionnelles. Nous obtenons ainsi une métrique lisse sur une boule de rayon conj x.Le rayon d’injectivité, inj x majore la longueur des géodésiques qui se referment sur elles-mêmes. Cela permet de minorer le nombre de préimages disjointes de la boule B(x, inj x) dans la carte géodésique de rayon conj x par un nombre N > conj x 

> inj x

.Nous avons donc une inégalité 

N Vol( B(0 , inj x)) 6 Vol( B(0 , conj x)) . (1.13) Par l’inégalité de Bishop-Gromov sur la boule Vol( B(0 , conj x)) où la courbure de Ricci est minorée, on obtient un contrôle du type 

conj x

inj x

6 N 6 Vol( B(0 , conj x)) Vol( B(0 , inj x)) 6 C(K, v, D )conj nx

inj nx

. (1.14) On en déduit donc que pour n > 2 (le cas n = 1 est beaucoup plus simple), on a 

inj x > C′(K, v, D ) 1 

> n−1

conj x. (1.15) En combinant les énoncés de la proposition 1.5 et du théorème 1.43, nous obtenons le théorème de compacité de Cheeger-Gromov. 

Corollaire 1.44 (Compacité de Cheeger-Gromov) . Soit (Mi, g i)i une suite de variétés riemanniennes satisfaisant 1. leurs courbures sectionnelles sont uniformément bornées 2. leurs volumes sont uniformément minorés 3. leurs diamètres sont uniformément majorés Alors, il existe une sous-suite telle que toutes les variétés soient difféomorphes. Elles convergent de plus, à difféomorphisme-près de manière C1,α vers une va-riété riemannienne (M∞, g ∞) dont la métrique est de classe C1,α en coordonnées harmoniques. Esquisse de preuve. La partie la plus difficile de cette preuve, que nous ne déve-lopperons pas ici, est la construction d’un difféomorphisme entre deux variétés proches au sens de Gromov-Hausdorff. Une bonne référence est [GW88]. 4. Voisinage d’une métrique lisse au sens de Gromov-Hausdorff 45 L’idée est d’effectuer un recouvrement de Vitali de l’une des deux variétés par des boules harmoniques puis d’en déduire un recouvrement similaire sur la seconde variété à l’aide de la proximité de Gromov-Hausdorff. Cela nous donne des difféomorphismes locaux qu’il faut ensuite “recoller” en un difféomorphisme global. La technique classique est de considérer des barycentres des points différentes cartes qui se superposent. Le contrôle des métriques en coordonnées géodésiques (ou presque linéaires) puis harmoniques, permet alors de contrôler la distance entre les métriques et de prouver une convergence en norme C1,α , voir encore une fois [GW88]. 

4.3 Régularité des métriques d’Einstein 

4.3.1 ε-régularité des métriques à courbure de Ricci bornée 

Présentons tout d’abord un résultat de [And89], voir aussi [CC96] et [CN15, section 2.2]. Il affirme qu’une métrique à courbure de Ricci bornée qui est locale-ment proche au sens de Gromov-Hausdorff d’une boule Euclidienne, a en réalité une courbure bornée. 

Proposition 1.45 (ε-régularité, [And89]) . Pour tout n ∈ N, il existe ε > 0 tel que pour toute variété riemannienne (M, g ), s’il existe un point p ∈ M , tel que l’on ait 1. | Ric g | < ε sur Bg(p, 2) , et 2. dGH 

> (

(Bg(p, 2) , g ), (Bge (0 , 2) , g e))

< ε ,alors, on a 

| Rm g | 6 1, sur Bg(p, 1) . (1.16) 

Si la métrique est d’Einstein, les dérivées de la métriques sont aussi uniformément contrôlées. Remarque 1.46 . La deuxième hypothèse de la proposition 1.45 est équivalente (à une constante différente-près) à avoir un volume proche de celui de la boule Euclidienne d’après [Col97, Theorem 0.8]. 

Remarque 1.47 . Ce résultat est faux en supposant uniquement une borne inférieure sur la courbure de Ricci. Il suffit de lisser un cône sur une sphère de rayon plus petit que 1 mais arbitrairement proche de 1 à l’aide d’une métrique à courbure positive pour obtenir des contre-exemples. 46 Chapitre 1. Espace de modules des métriques d’Einstein 

Remarque 1.48 . Un résultat encore plus difficile d’ ε-régularité de [CN15] donne la même conclusion en remplaccant la deuxième hypothèse par 

dGH 

> (

(Bg(p, 2) , g ), (BRn−3×C(Z)(0 , 2) , g e))

< ε, 

pour C(Z) un cône quelconque. Nous retrouvons le lemme 1.45 avec C(Z) = 

C(S2). 

4.3.2 De Gromov-Hausdorff à C∞

Nous en déduisons par régularité elliptique que pour toute métrique d’Einstein, les métriques d’Einstein suffisamment proches au sens de Gromov-Hausdorff sont en fait proches dans le sens lisse du début du chapitre. 

Corollaire 1.49. Soit (M, g 0) une variété d’Einstein compacte à constante d’Ein-stein bornée par n − 1. Alors, pour tout δ > 0, il existe η > 0 tel que si (N, g ) est une variété riemannienne à courbure de Ricci bornée par 10 6(n − 1) telle que 

dGH 

> (

(M, g 0), (N, g ))

< η, 

alors, M = N et il existe un difféomorphisme ϕ : M → M tel que 

‖g − g0‖C1,α < δ. 

Si (N, g ) est d’Einstein, on peut de plus obtenir des contrôles pour les dérivées d’ordre supérieur. Démonstration. Soit ( M, g 0) une variété d’Einstein, et soit K tel que | Rm g0 | < K ,0 < v 0 < Vol( M, g 0) et D0 > diam (M, g 0). D’après la proposition 1.3 combinée à 1.43, pour tout ε > 0, il existe r0 = r0(ε, K, v 0) > 0 tel que pour tout point p de 

M , on ait 

dGH 

> (

Bg0 (p, 2r0), B ge (2 r0))

< ε

2r0. (1.17) Supposons, quitte à prendre r0 plus petit, que 10 6(n − 1) < εr20

. Soit maintenant (N, g ) à courbure de Ricci bornée par 10 6(n−1) satisfaisant dGH 

> (

(M, g 0), (N, g ))

< 

> ε
> 2

r0. Alors, grâce à (1.17) sur chaque boule de rayon 2 de ( N, g ), on a 

dGH 

> (

(Bg(p, 2r0), g ), (Bge (0 , 2r0), g e))

< ε

2r0.4. Voisinage d’une métrique lisse au sens de Gromov-Hausdorff 47 On en déduit en choisissant ε la constante du lemme 1.45 que l’on a 

| Rm g | 6 1

r20

sur toute la variété ( N, g ). Par la convergence du volume de [Col97], on déduit alors du théorème 1.44 de compacité de Cheeger-Gromov, par un argument par contradiction, que pour tout δ > 0, il existe η pour lequel si l’on a 

dGH 

> (

(M, g 0), (N, g ))

< η, 

pour 0 < η < ε 

> 2

r0 suffisamment petit, alors 

‖g − g0‖C1,α < δ. 

En utilisant alors la structure analytique de l’espace de modules des métriques d’Einstein au voisinage d’une métrique lisse prouvée dans la section précédente, nous en déduisons que la constante d’Einstein est la même pour toutes les mé-triques suffisamment dGH −proches et de même volume qu’une métrique d’Einstein lisse donnée. 

Corollaire 1.50. Soit (M, g 0) une variété d’Einstein compacte à constante d’Ein-stein Λ telle que |Λ| 6 n − 1. Alors il existe η > 0 tel que pour toute va-riété d’Einstein (N, g ) à courbure de Ricci bornée par 10 6(n − 1) satisfaisant 

Vol( N, g ) = Vol( M, g 0) et 

dGH 

> (

(M, g 0), (N, g ))

< η, 

on ait Ric( g) = Λ g.Démonstration. Soit ( M, g 0) une variété d’Einstein et soit η > 0 suffisamment petit pour que le δ(η) du corollaire 1.49 soit suffisamment petit pour que les métriques ( N, g ) de l’énoncé appartiennent au voisinage U de la proposition 1.31 (la régularité elliptique de l’équation d’Einstein permet de passer de C1,α à C2,α ). L’ensemble des métriques à distance dGH au plus η de ( M, g 0) et satisfaisant les hypothèses de l’énoncé a ainsi une structure de sous-ensemble analytique. C’est donc localement une union de sous-variétés analytiques et donc localement connexe (quitte à choisir un voisinage plus petit), avec de plus des courbes analytiques reliant les métriques à g0. Comme la différentielle de g 7 → Rg = 1Vol( N,g ) 

> ∫
> N

Rg dvg48 Chapitre 1. Espace de modules des métriques d’Einstein en une métrique d’Einstein est nulle pour les déformations à volume constant, nous en déduisons que R est constante. Comme elle est proportionnelle à la constante d’Einstein divisée par le volume qui est supposé constant, la constante d’Einstein est constante. 

Remarque 1.51 . En dimension 4 on peut se défaire de l’hypothèse sur la borne de la courbure de Ricci de g dans les deux énoncés précédents en la remplaccant par une condition topologique à l’aide de la formule (2.2). 

# 5 Applications 

Présentons maintenant deux applications des résultats précédents. Le premier est la preuve de la complétude de l’espace de modules des métriques d’Einstein en dimension 2 et 3, ce qui motivera la complétion de l’espace de modules en dimension 4 présentée dans le chapitre suivant (ch. 2) puis dans le reste de la thèse. Le deuxième est la rigidité des métriques à courbures sectionnelles constantes égales à 1 dans un sens fort et quantitatif qui nous servira dans le chapitre 3. 

5.1 Complétude de l’espace de modules en dimension 2

et 3 pour la distance de Gromov-Hausdorff 

En dimension 2, il n’y a qu’une notion de courbure, celle de Gauss qui vaut à une constante près la courbure de Ricci et la courbure scalaire. En effet, les courbures sectionnelles sont définies comme les courbures de Gauss de plans géo-désiques, or il n’y en a qu’un ici, les différentes moyennes de cette unique courbure sont donc proportionnelles. En dimension 3, la courbure de Ricci contrôle aussi le tenseur de courbure de Riemann car nous avons la formule suivante, 

Rijkl = gik Rjl − gil Rjk − gjk Ril + gjl Rik − 12 R( gik gjl − gil gjk ), (1.18) qui peut par exemple être retrouvée dans [Ham82, Theorem 8.1], où les Rijkl sont les courbures sectionnelles et les Rij les composantes de la courbure de Ricci en coordonnées. Lorsque l’on considère des suites de métriques d’Einstein en dimension 2 et 3 à courbure de Ricci bornée, alors, leur courbure Riemannienne est bornée et l’on se retrouve dans le cadre du corollaire 1.44. 5. Applications 49 

Théorème 1.52. Soit (Mi, g i)i une suite de variétés d’Einstein de dimension 

2 ou 3 de volume 1, de courbure de Ricci uniformément bornée et de diamètre uniformément borné. Alors, il existe une sous-suite convergeant vers une variété lisse d’Einstein et de plus, la convergence a lieu au sens C∞.Remarque 1.53 . Bien que ces espaces de modules soient complets au sens de Gromov-Hausdorff, ils ne sont pas compacts. En effet, lorsque l’on autorise leur diamètre à tendre vers l’infini, deux types de dégénérescences sont envisageables : l’effondrement et la formation de cusps hyperboliques. k 

> (a) Effondrement. (b) Formation de cusp.

Figure 1.1 – Dégénérescences de métriques d’Einstein en dimension 2. Nous verrons qu’en dimension 4 des singularités coniques peuvent se former à distance de Gromov-Hausdorff finie. Avec la formation de cusps et l’effondrement, ce sont les seuls types de dégénérescences qui apparaissent en dimension 4, voir [And92] pour une preuve dans le cadre L2 et [CT06] pour une preuve pour la distance de Gromov-Hausdorff. 

5.2 Proximité Ck,α d’ordre optimal avec une métrique ronde 

Montrons dans cette partie que l’on peut obtenir un contrôle d’ordre optimal entre une métrique à courbures sectionnelles presque égales à 1 et une métrique ronde lorsque le volume est minoré. Une conséquence du théorème de compacité de Cheeger-Gromov, théorème 1.44 est le lemme suivant. 50 Chapitre 1. Espace de modules des métriques d’Einstein 

Lemme 1.54. Pour tout n, 0 < α < 1, δ > 0 et v0 > 0, il existe ε > 0 tel que si 

(M n, g ) satisfait 1. 1 − ε < Sec (g) < 1 + ε,2. et Vol( M ) > v 0,alors il existe Γ un sous-groupe fini de SO (n + 1) (dont le cardinal est majoré par une fonction de v0), et un difféomorphisme Φ : Sn/Γ → M tel que : 

> ∥∥∥

Φ∗g − gSn/Γ∥∥∥C1,α 6 δ, 

où gSn/Γ est une métrique à courbures sectionnelles constantes égales à 1 sur Sn/

Γ.

Nous allons en fait montrer le résultat suivant qui est un raffinement du lemme 1.54. 

Proposition 1.55. Soit (M, g 0) une variété à courbures sectionnelles constantes égales à 1, et k ∈ N. Alors, il existe δ > 0 et C > 0, tel que si une métrique g sur 

M satisfait : 

‖g − g0‖Ck+1 ,α 6 δ, 

alors, il existe un difféomorphisme Φ : M → M , pour lequel 

‖Φ∗g − g0‖Ck+1 ,α 6 C∥∥∥ Ric( g) − (n − 1) g∥∥∥Ck .

Remarque 1.56 . Il suffit en fait que la métrique d’Einstein g0 n’admette pas de déformations infinitésimales pour avoir un résultat similaire. C’est par exemple aussi le cas si la métrique est à courbures sectionnelles négatives. 

Corollaire 1.57. Pour tout n, 0 < α < 1 et v0 > 0, il existe ε0 > 0 et C > 0 tels que pour tout 0 < ε < ε 0, si (M n, g ) satisfait : 1. 1 − ε < Sec (g) < 1 + ε,2. et Vol( M, g ) > v 0,alors il existe Γ un sous-groupe fini de SO (n + 1) (dont le cardinal est majoré par une fonction de v0), et un difféomorphisme Φ : Sn/Γ → M tel que 

‖Φ∗g − g0‖C1,α 6 Cε. 

Remarque 1.58 . Ce qui est important pour nous ici, c’est que le ε de l’estimation finale soit bien celui de l’inégalité 1 − ε < Sec (g) < 1 + ε.5. Applications 51 

Proposition 1.59. Si une métrique g0 a des courbures sectionnelles constantes égales à 1, alors la linéarisation de Φg0 : g 7 → E(g) + δ∗ 

> g

δg0 g au voisinage de g0 est inversible sur les 2-tenseurs h satisfaisant ∫ 

> M

tr g0 hdvg0 .Démonstration. D’après le lemme 1.24, l’équation dg0 Φg0 h = 0 se réduit à 

∇∗∇h − 2˚R( h) = 0 .

Si les courbures sectionnelles de g0 sont toutes égales à 1, alors, ˚Rg0 (h) = tr g0 (h)g0 − h, 

et donc, comme tr g0 h = 0, on obtient 

∇∗∇h + 2 h = 0 ,

qui implique que h = 0 par intégration par parties contre h.Maintenant, lorsque nous avons un opérateur inversible entre espaces de Ba-nach, nous avons en fait un contrôle uniforme sur son inverse. 

Lemme 1.60. Pour tout opérateur linéaire Fredholm et injectif P entre des espaces de Banach X et Y , il existe C = C(P ) > 0, et ε0 = ε0(P ) > 0 tels que : pour tout opérateur P ′ satisfaisant pour tout u ∈ X,

‖(P ′ − P )u‖Y 6 ε0‖u‖X ,

on ait : 

‖u‖X 6 C‖P ′u‖Y .

Ce lemme est une conséquence du théorème de l’inverse de Banach appliqué à l’opérateur Fredholm P en restreignant l’espace d’arrivée Y à l’image de P qui est fermée par hypothèse. On déduit alors du théorème des fonctions inverses 1.12 et des contrôles du lemme 1.60 le résultat suivant. 

Corollaire 1.61. Si une métrique g0 a des courbures sectionnelles constantes égales à 1, alors pour tout l ∈ N, il existe δ > 0, et C > 0 tels que, si une métrique 

g satisfait ‖g − g0‖W l+2 ,p 6 δ et a le même volume que g0, alors, 

‖g − g0‖W l+2 ,p 6 C‖Φg0 (g)‖W l,p .52 Chapitre 1. Espace de modules des métriques d’Einstein Maintenant que l’on a montré que la linéarisation de notre opérateur était inversible, on peut conclure en utilisant le théorème des fonctions inverses pour estimer à quelle distance il se trouve du seul zéro de l’opérateur d’Einstein en jauge divergence, la métrique g0 que l’on a fixée. 

Proposition 1.62. Soit (M, g 0) une variété à courbures sectionnelles constantes égales à 1, et k ∈ N. Alors, il existe δ > 0 et C > 0, tel que si une métrique g sur 

M satisfait : 

‖g − g0‖Ck+1 ,α 6 δ

alors, il existe un difféomorphisme Φ : M → M , si k > 1,

‖Φ∗g − g0‖Ck+1 ,α 6 C 

> ∥∥∥

Ric( g) − (n − 1) g 

> ∥∥∥Ck−1,α

,

ou bien, si k = 0 ,

‖Φ∗g − g0‖C1,α 6 C∥∥∥ Ric( g) − (n − 1) g∥∥∥C0 .

Démonstration. Soit ( M, g 0) une variété à courbures sectionnelles égales à 1, et soit δ > 0 la constante du lemme 1.15, et de celui du corollaire 1.61. Alors, d’après le lemme 1.15, il existe un difféomorphisme Φ : M → M tel que 

δg0 Φ∗g = 0 .

On a donc, ‖Φg0 (Φ ∗g)‖Ck 6 ∥∥∥ Ric( g) − (n − 1) g∥∥∥Ck , et par le corollaire 1.61, on en déduit qu’il existe C > 0, indépendante de ε telle que 

‖g − g0‖Ck+1 ,α 6 Cε, 

car sur la sphère, pour p suffisamment grand, W k+2 ,p se plonge continûment dans 

Ck+1 ,α , et Ck se plonge continûment dans W k,p .Chapitre 2 Complétion au sens de Gromov-Hausdorff de l’espace de modules des métriques d’Einstein en dimension 4

Dans ce chapitre et dans la suite de cette thèse, nous nous focalisons sur la di-mension 4. Contrairement aux dimensions inférieures, l’espace de modules des mé-triques d’Einstein n’est plus complet lorsqu’il est muni de la distance de Gromov-Hausdorff. Nous rappelons tout d’abord quelques particularités de la dimension 4 qui motivent cette étude. Nous présentons ensuite la complétion de l’espace de modules des métriques d’Einstein de dimension 4. Nous verrons que le seul type de dégénérescence possible fait apparaître des espaces singuliers qui se forment après la contraction des bulles du problème. 

Contributions. Nous présentons des preuves concises et peut-être plus mo-dernes de résultats montrés au cours des années 70 et 80, ce qui permet de fixer les notations et d’avoir des résultats de base clairs pour la suite de la thèse. 

# 1 Métriques d’Einstein en dimension 4

Comme évoqué en introduction, la dimension 4 présente des caractéristiques spécifiques en géométrie et en topologie. Nous en présentons quelques unes dans cette section. 53 54 Chapitre 2. Complétion de GH en dimension 4 

1.1 Quelques particularités des métriques d’Einstein lisses en dimension 4

Certaines de ces propriétés de la dimension 4 que nous exhibons ci-dessous permettent de justifier le côté “optimal” des métriques d’Einstein pour cette di-mension. 

1.1.1 Variétés topologiques et différentiables en dimension 4La topologie en dimension 4 est un vaste sujet dans lequel beaucoup de résultats sont frappants et inattendus, voir par exemple [Sco05]. Ce domaine se trouve à l’intersection de la topologie de “haute” et de “basse” dimension et semble hériter de leurs difficultés respectives. Tout au long de cette thèse, nous utiliserons le terme de variété pour désigner une variété différentielle . De même le terme topologie , désignera une structure dif-férentiable fixée (dont la régularité n’a pas d’importance par un théorème classique de Whitney). Nous ne nous poserons donc jamais la question du choix d’une struc-ture différentiable sur une variété topologique qui apparait à partir de la dimension 4. Pour illustrer la difficulté de cette question, mentionnons d’une part que le nombre de structures différentiables sur la sphère (topologique) S4 n’est toujours pas connu, et d’autre part qu’il existe une infinité non dénombrable de structures différentiables sur R4 topologique d’après la théorie de Donaldson. 

1.1.2 Courbure et 2-formes en dimension 4En dimension 4, l’étoile de Hodge restreinte aux 2-formes, ∗ : Ω 2 → Ω2 satisfait 

∗2 = Id et ses valeurs propres sont donc ±1. On note alors Ω 2 

> ±

les espaces propres associés qui sont tous les deux de dimension 3, Ω + est l’ensemble des 2-formes 

autoduales alors que Ω − est l’ensemble des formes anti-autoduales , et l’on a Ω2 = Ω 2+ ⊕ Ω2

> −

.

Cette somme directe est orthogonale pour le produit scalaire donné par la forme bilinéaire ω 7 → ω ∧ ω qui satisfait de plus ω± ∧ ω± = ±| ω±|2dvol si ω± ∈ Ω2

> ±

.Grâce à cette somme directe, l’endomorphisme symétrique sur les 2-formes, 1. Métriques d’Einstein en dimension 4 55 noté R donné par la courbure Riemannienne se décompose par blocs, 

R =:  

> 

R+ Ric 0

Ric 0 R− 

> 

,

où les Ric 0 forment la partie sans trace de la courbure de Ricci, et où R± := 

W ± + R12 , avec R la courbure scalaire, et où les tenseurs sans trace W ± sont les parties autoduale et anti-autoduale du tenseur de Weyl, W .Nous dirons qu’une métrique d’Einstein est autoduale si l’on a W − = 0 et 

anti-autoduale si W + = 0. 

1.1.3 Norme L2 de la courbure 

En dimension 4, une quantité naturelle pour mesurer à quel point une métrique est courbée est la norme L2 du tenseur de courbure de Riemann, noté Rm. Celle-ci est invariante par changement d’échelle pour cette dimension. La formule de Chern-Gauss-Bonnet implique que pour toute métrique g sur une variété M de dimension 4, nous avons 

> ∫
> M

| Rm g |2dvg = 8 π2χ(M ) + 

> ∫
> M

| Ric 0 

> g

|2dvg, (2.1) où Ric 0 

> g

= Ric g −Rg 

> 4

g, est la partie sans trace de la courbure de Ricci et χ(M ) la caratéristique d’Euler qui ne dépend pas de g.On en déduit donc que les métriques satisfaisant Ric 0 ≡ 0 sont les seules 

à minimiser ∫ 

> M

| Rm g |2dvg lorsqu’elles existent, et que pour une telle métrique,  

> ∫
> M

| Rm g |2dvg = 8 π2χ(M ) est de plus purement topologique. La condition Ric 0 

> g

≡

0 est en fait équivalente à la condition d’Einstein par la contraction de la seconde égalité de Bianchi qui donne δg

> (

Ric g −R( g)2 g)

= 0. En effet, comme Ric 0 

> g

= 0 implique Ric g = Rg 

> 4

g, nous avons donc nécessairement d Rg = 0 puis Ric g est constante. Cette norme L2 sera vue comme une énergie contrôlée de manière purement topologique et sera à la base de la plupart de nos arguments analytiques. 

1.1.4 Inégalité d’Hitchin-Thorpe 

Pour une variété d’Einstein de dimension 4, comme vu dans la partie précé-dente, la formule de Chern-Gauss-Bonnet implique la formule, 

χ(M ) = 18π2

> ∫
> M

| Rm |2dv = 18π2 

> ∫
> M
> (

R2

24 + |W +|2 + |W −|2

> )

dv, (2.2) 56 Chapitre 2. Complétion de GH en dimension 4 qui nous assure déjà que pour qu’une métrique d’Einstein existe sur une variété 

M nous avons nécessairement χ(M ) > 0 avec égalité pour les métriques plates uniquement. La formule de signature de Hirzebruch est 

τ (M ) = 112 π2

> ∫
> M
> (

|W +| − | W −|2)

dv. (2.3) De plus, comme ∫ 

> M

|W ±|2dv > 0 et ∫ 

> M

R2 dv > 0, grâce à (2.2) et (2.3), on obtient l’inégalité de Hitchin-Thorpe suivante pour les variétés d’Einstein, 2χ(M ) > 3|τ (M )|.

avec égalité si et seulement si M est un quotient du tore plat ou d’une variété hyperkählérienne. On en déduit qu’il existe des variétés en dimension 4 sur lesquelles il n’existe pas de métrique d’Einstein. 

Exemple 2.1 (Variétés de dimension 4 sans métriques d’Einstein) . Simplement avec la condition χ(M ) > 0, nous pouvons trouver des variétés de dimension 4 n’admettant pas de métriques d’Einstein. Par exemple les fibrés en cercle sur 

M 3 6 = T3 ou bien, les produits de surfaces S2 × Σγ pour γ > 2 où Σ γ est la surface de genre γ n’admettent pas de métriques d’Einstein. 

1.2 Variétés Ricci-plates ALE et singularités orbifolds 

En dimension 4, les métriques d’Einstein n’ont plus nécessairement une cour-bure bornée et peuvent développer des singularités. Nous verrons dans la partie suivante que ces singularités sont les plus simples et lisses envisageables et que l’on peut comprendre leur formation au sens de Gromov-Hausdorff. Présentons donc des exemples de telles dégénérescences. 

1.2.1 Définitions 

Donnons pour commencer les définitions d’ orbifold et d’ espace asymptotique-ment localement euclidien (ALE) qui seront respectivement les espaces singuliers et les modèles de singularités des dégénérescences que l’on étudiera. 

Définition 2.2 (Orbifold (à singularités isolées)) . Nous dirons qu’un espace mé-trique ( Mo, g o) est un orbifold (à singularités isolées) s’il existe ε0 > 0 et un nombre fini de points ( pk)k de Mo que l’on qualifiera de singuliers tels que l’on ait les propriétés suivantes : 1. Métriques d’Einstein en dimension 4 57 1. l’espace ( Mo\{ pk}k, g o) est une variété riemannienne, 2. pour chaque point singulier pk de Mo, il existe un voisinage de pk, Uk ⊂ Mo,un sous-groupe fini Γ k ⊂ SO (4) agissant librement sur la sphère, et un difféomorphisme Φ k : Be(0 , ε 0) ⊂ R4/Γk → Uk ⊂ Mo pour lequel Φ ∗

> k

go est lisse lorsqu’elle est tirée en arrière sur R4, et donc en particulier 

rle|∇ l(Φ ∗

> k

go − ge)|C2(ge) 6 Clr2 

> e

.

Définition 2.3 (Variété ou orbifold asymptotiquement localement euclidienne (ALE)) . On dira qu’une variété ou un orbifold ( N n, g ) est asymptotiquement lo-calement euclidien (ALE) s’il existe τ > 0 et un compact K ⊂ N , un rayon 

R > 0, Γ un sous-groupe fini de SO (n) dont l’action est libre sur Sn−1, et un dif-féomorphisme Ψ ∞ : ( Rn/Γ) \Be(0 , R ) 7 → N \K tels que, si l’on note ge la métrique euclidienne projetée sur Rn/Γ, on ait, pour tout k ∈ N,

ρk∣∣∣∇ke (Ψ ∗∞g − ge)∣∣∣ge

= O(ρ−τ ),

sur (

Rn/Γ)

\Be(0 , R ), où ρ = de(., 0). Au voisinage des singularités orbifolds, nous avons des difféomorphismes locaux Ψ k introduits dans la définition 2.2. Les exemples les plus simples sont non-compacts et modélisent à la fois les singularités des orbifolds et les infinis des ALE. 

Exemple 2.4 (Les cônes plats R4/Γ) . Soit Γ ⊂ SO (4) agissant librement sur la sphère S3 c’est-à-dire n’ayant que {0} ou R4 entier (si Γ = {Id }) comme ensemble de points fixes sur R4. L’espace quotient R4/Γ est alors localement euclidien. C’est de plus un cône sur la variété d’Einstein S3/Γ. Le cas particulier de Γ = Z2 = {± Id } correspond à S3/Z2 = RP 3.Donnons quelques exemples d’orbifolds compacts. 

Exemple 2.5 (L’orbifold plat T4/Z2). Considérons maintenant le tore T4 = R4/

Z4. L’action multiplicative de Z2 = {± 1} sur R4 descend sur T4, et on note T4/Z2

l’orbifold quotient obtenu. Il a seize singularités modelées sur R4/Z2 à tous les points ( ε1, ε 2, ε 3, ε 4) avec les εi ∈ { 0, 12 }.

Exemple 2.6 (L’orbifold sphérique S4/Z2). La sphère S4 peut être vue comme 

S4 ⊂ R5. On notera S4/Z2 la variété obtenue comme quotient de S4 par l’identifi-cation antipodale pour les 4 premières coordonnées de R5.58 Chapitre 2. Complétion de GH en dimension 4 

Exemple 2.7 (L’orbifold hyperbolique H4/Z2). L’orbifold H4/Z2 est obtenu par identification antipodale en carte géodésique globale sur le disque de Poincaré H4.xx

Figure 2.1 – Exemples d’orbifolds. 

Remarque 2.8 . Voir l’exemple des métriques AdS-Taub-Bolt en annexe B pour un orbifold non compact (asymptotiquement hyperbolique). 

1.2.2 Exemples de dégénérescences de variétés d’Einstein en dimension 4Montrons tout d’abord à l’aide d’exemples que contrairement aux métriques d’Einstein en dimension 2 et 3, l’ensemble des métriques d’Einstein en dimension 4 à volume et à diamètre uniformément contrôlés n’est pas compact. Il y a donc un nouveau phénomène : les dégénérescences orbifolds. Nous verrons dans la suite que c’est exactement qui empêche l’espace de modules des métriques d’Einstein d’être complet en dimension 4 lorsqu’il est muni de la distance de Gromov-Hausdorff. 

La variété Ricci-plate ALE d’Eguchi-Hanson. En dimension 4, une nou-veauté par rapport aux dimensions inférieures est le fait qu’il existe des métriques Ricci-plates autre que l’espace euclidien avec une croissance euclidienne des vo-lumes. 1. Métriques d’Einstein en dimension 4 59 La métrique d’Eguchi-Hanson est une métrique sur T ∗S2 qui est Ricci-plate et asymptotique au cône plat R4/Z2. Notons ( x, y, z, t ) des coordonnées dans une base orthonormale de R4, et définissons ρ := √x2 + y2 + z2 + t2, et une base de 1-formes invariantes sur la sphère S3, ( α1, α 2, α 3) par, 

α1 := 1

ρ2 (xdy − ydx + zdt − tdz )

α2 := 1

ρ2 (xdz − zdx − ydt + tdy )

α3 := 1

ρ2 (xdt − tdx + ydz − zdy ). (2.4) À l’aide de ces 1-formes, la métrique ronde sur la sphère S3 s’écrit α21 + α22 + α23,et la métrique Euclidienne s’écrit donc dρ 2 + ρ2gS3 = dρ 2 + ρ2(α21 + α22 + α23). Hors de la section nulle de T ∗S2 représentée par ρ = 0, la métrique gEH s’écrit (avec l’identification T ∗S2\S2 ≈ (R4/Z2)\{ 0}) : 

gEH := 

> √

ρ4

1 + ρ4 (dρ 2 + ρ2α21) + 

> √

1 + ρ4(α22 + α23). (2.5) En ρ = 0, la métrique est asymptotique à d 

> (ρ2
> 2
> )2

+ 4  

> (ρ2
> 2
> )2

α21 + ( α22 + α23) et se prolonge bien de manière lisse à l’origine grâce à une sphère ronde S2 (avec la métrique α22 + α23) totalement géodésique, parce que 2 α1 est de longueur 2 π sur 

R4/Z2. À l’infini, la métrique est asymptotique à la métrique plate dρ 2 + ρ2(α21 +

α22 + α23). Cette métrique satisfait Ric( gEH ) = 0 et R+(gEH ) = 0. 

Figure 2.2 – Formation de singularité orbifold. Par invariance par rééchelonnement, pour t > 0, les métriques tg EH restent Ricci-plates et asymptotiques à R4/Z2. De plus, par définition du cône asympto-60 Chapitre 2. Complétion de GH en dimension 4 tique, nous avons (T ∗S2, tg EH ) t→0

−−→

> dGH

R4/Z2.

On observe donc la formation d’une singularité R4/Z2 à la limite alors que la courbure de Ricci et le volume de la boule de rayon 1 restent bornés. 

Remarque 2.9 . Il existe d’autres exemples explicites de métriques Ricci-plates (et même hyperkählériennes) U (2)-invariants asymptotiques à R4/Zk pour k > 2, [GH78]. 

Remarque 2.10 . Nous avons aussi décrit dans l’annexe B un exemple explicite de dégénérescence dans le cadre asymptotiquement hyperbolique avec la famille de métriques AdS-Taub-Bolt qui développent une singularité R4/Z2.

Métriques hyperkählériennes sur la surface K3. Dans le cas compact, les dégénérescences connues n’ont pas d’expression explicite. Cependant, il est possible d’approcher ce phénomène et d’en avoir une bonne représentation géométrique asymptotique par recollement-perturbation. L’exemple le plus connu est sur la surface K3 où une suite de métriques Ricci-plates (hyperkählériennes) converge vers l’orbifold T4/Z2.

Lemme 2.11. Il existe une suite de métriques hyperkählériennes convergeant vers l’orbifold T4/Z2 et telles que tous les éclatements à l’échelle de la courbure aux 16 

points singuliers convergent vers la métrique d’Eguchi-Hanson au sens de Gromov-Hausdorff pointé. Remarque 2.12 . Il existe de la même manière des exemples de dégénérescences de variétés de Kähler-Einstein avec des constantes d’Einstein constantes égales à ±1 dégénérant vers des orbifolds de Kähler-Einstein, voir l’article d’exposition [Nak94] et ses références. 

1.2.3 Sous-groupes finis de SO (4) agissant librement sur S3

Remarquons que l’ensemble des singularités qui peuvent se former s’injecte dans l’ensemble des sous-groupes finis de SO (4) qui agissent librement sur S3.Décrivons cs sous-groupes. L’algèbre C2 s’identifie à celle des quaternions H grâce l’isomorphisme suivant (a + ib, c + id ) ∈ C2 → a + ib + ( c + id )j = a + ib + jc + kd ∈ H,

avec les relations i2 = j2 = k2 = ijk = −1. 1. Métriques d’Einstein en dimension 4 61 Si l’on note ∗ la multiplication des quaternions, on peut alors définir l’applica-tion ϕ : S3 × S3 → SO (4) définie pour c ∈ H par 

ϕ(a, b )( c) = a ∗ c ∗ ¯b, 

qui est en fait un revêtement à deux feuillets. Cette identification est pratique pour identifier les sous-groupes de SO (4). Par exemple, la multiplication à droite par un élément de S3 (ou plus précisément la restriction de ϕ à 1 × S3) est équivalente à l’action de SU (2), et SU (2) ≈ S3. De même, la restriction de ϕ à S1 × S3 est un revêtement à deux feuillets de U (2). On appellera U (2) := ϕ(S3 × S1) qui sera vu comme U (2) avec l’orientation opposée. 

Théorème 2.13 ([Sco83, Theorem 4.10]) . Si Γ est un sous-groupe fini de SO (4) 

agissant librement sur S3, alors Γ est conjugué à un sous-groupe fini de U (2) ou un sous-groupe fini de U (2) .

Cela signifie qu’il suffit de considérer les sous-groupes finis de U (2) et les chan-gements d’orientation pour atteindre tous les sous-groupes finis de SO (4). Ces sous-groupes sont classifiés dans le théorème 4.11 de [Sco83] comme les projections des Zk × G où G est un sous-groupe fini de S3 ≈ SU (2), voir [LV16, Table 1] pour une liste des groupes possibles. 

1.2.4 Exemples connus d’orbifolds Ricci-plats ALE 

Présentons brièvement les exemples connus d’orbifolds Ricci-plats ALE qui sont tous kählériens. Il est souvent conjecturé que ce sont les seuls espaces Ricci-plats ALE. 

Orbifolds ALE hyperkählériens. Les seuls exemples connus d’orbifolds Ricci-plats ALE sont kählériens. Tous ces exemples sont classifiés, et on a une paramé-trisation satisfaisante de l’espace des modules de ces métriques Ricci-plates ALE. Donnons tout d’abord certaines propriétés des exemples hyperkählériens. 

Théorème 2.14 (Métriques Ricci-plates ALE hyperkählériennes, [Kro89a, Kro89b]) .

Soit Γ un sous-groupe fini de SU (2) . Alors, il existe kΓ ∈ N∗ et DΓ une union de sous-espaces vectoriels de R3kΓ de codimension au moins 3 contenant 0, tels que l’espace de modules des variétés hyperkählériennes asymptotiques à R4/Γ soit pa-ramétré sur R3kΓ par des métriques (Xζ , g ζ )ζ∈R3kΓ telles que ζ 7 → gζ soit analytique. Remarque 2.15 . Pour tout ζ ∈ R3kΓ \DΓ, Xζ est difféomorphe à la résolution mi-nimale de C2/Γ. 62 Chapitre 2. Complétion de GH en dimension 4 

Remarque 2.16 . Lorsque ζ ∈ R3kΓ s’approche de DΓ avec les notations du théo-rème 2.14, les métriques convergent au sens de Gromov-Hausdorff pointé vers des 

orbifolds Ricci-plats ALE. 

Orbifolds Ricci-plats ALE kählériens. Les autres exemples kählériens sont classifiés dans [Suv11]. Ils sont tous asymptotiques à des groupes cycliques de type 1

dn 2 (1 , dnm − 1) ⊂ U (2) ,

c’est-à-dire le groupe cyclique d’ordre dn 2 engendré par : 

> 

e i2πdn 2 00 ei2π(dnm −1)  

> dn 2
> 

,

où d > 1, n > 2 et n et m sont premiers entre eux. Ce groupe admet un sous-groupe cyclique 1 

> dn

(1 , −1) ⊂ SU (2) d’ordre dn engendré par 

> 

ei2πdn 00 e−i2πdn  

> 

,

et on note Adn −1 la singularité R4/ 1 

> dn

(1 , −1). D’après [Suv11], les variétés kählériennes Ricci-plates ALE dont le groupe à l’infini n’est pas dans SU (2) sont asymptotiques à R4/ 1 

> dn 2

(1 , dnm − 1) et sont des quotients d’instantons gravitationnels de Gibbons-Hawking [GH78] asymptotiques à R4/ 1 

> dn

(1 , −1) par l’action d’un groupe d’isométries Zn. D’après la fin de la partie 6.2 de [BR15], cela ne laisse que 3 d−1 degrés de liberté, et on peut donc paramétrer ces métriques sur R3d−1\D 1  

> dn 2(1 ,dnm −1)

avec encore une fois un sous-ensemble de codimension 3 à éviter pour avoir des espaces lisses. 

Remarque 2.17 . Nous voyons donc qu’avec les variétés Ricci-plates ALE kählé-riennes (avec une de leurs orientations), nous n’atteignons pas tous les sous-groupes de SO (4) agissant sur S3, mais seulement ceux contenus dans SU (2) et les groupes 1 

> dn 2

(1 , dnm − 1) ⊂ U (2). Il n’est pas clair que les autres groupes puissent modeler les infinis d’espaces Ricci-plats ALE non plats. Pour Γ = 1 

> dn 2

(1 , dnm − 1), nous noterons dΓ := 3 d − 1, et pour Γ ⊂ SU (2), nous noterons dΓ := 3 kΓ, où kΓ est la constante du théorème 2.14. 1. Métriques d’Einstein en dimension 4 63 

1.3 Questions sur les métriques d’Einstein en dimension 4

Terminons cette section en listant quelques questions et conjectures sur les variétés d’Einstein, en particulier en dimension 4. Nous verrons ainsi que des questions basiques sont toujours ouvertes. 

L’ensemble des métriques d’Einstein sur une 4-variété fixée. L’ensemble des solutions de l’équation d’Einstein sur une variété donnée est loin d’être com-pris, même sur les variétés les plus simples. 

Question 2.18. Existe-t-il une métrique d’Einstein autre que la métrique ronde sur S4 ?La réponse est négative en dimension 2 et 3 alors qu’elle est positive pour des dimensions supérieures, et ce même avec la structure différentiable habituelle de la sphère [Böh98]. 

Question 2.19. Y a-t-il un nombre fini de constantes d’Einstein possibles (à volume fixé) sur une variété différentielle donnée en dimension 4 ? Un résultat plus fort serait le suivant. 

Question 2.20. Y a-t-il un nombre fini de composantes connexes pour l’ensemble des métriques d’Einstein en dimension 4 ? Notons que c’est une question subtile pour laquelle la dimension 4 est la di-mension critique entre deux comportements bien distincts. En effet, la réponse à cette question est positive jusqu’en dimension 3 et fausse à partir de la dimension 5 car E(S3 × S2) a un nombre infini de composantes connexes d’après [WZ90]. Comme signalé dans [And10], la question est en réalité celle de la structure de l’ensemble de l’espace des modules des métriques d’Einstein au voisinage de son bord. 

Les dégénérescences de 4-variétés d’Einstein. Question 2.21. Existe-t-il des variétés ou orbifolds Ricci-plats (mais non plats) ALE asymptotiques à tous les cônes R4/Γ pour Γ ⊂ SO (4) fini, agissant librement sur la sphère et classifiés dans le théorème 2.13 ? Une réponse positive à la question suivante donnerait une réponse négative à la question 2.21 d’après la remarque 2.17. 64 Chapitre 2. Complétion de GH en dimension 4 

Question 2.22 ([BKN89, 3), page 315]) . Les variétés Ricci-plates ALE sont-elles nécessairement kählériennes ? 

Remarque 2.23 . Dans [BKN89], Bando, Kasue et Nakajima présentent cette ques-tion comme une conjecture. Cependant la justification semble être la conjecture analogue dans le cadre Yang-Mills qui a été contredite [SSU89] la même année. 

Question 2.24. Existe-t-il des métriques Ricci-plates compactes à holonomie gé-nérique ? Un angle d’attaque pour obtenir une réponse négative serait de construire une dégénérescence orbifold qui ne serait pas hyperkählérien en désingularisant un orbifold Ricci-plat. 

Question 2.25. Existe-t-il des exemples de dégénérescences orbifolds pour des métriques non-kählériennes ? Comme indiqué en introduction, la notion d’Einstein est entre autres motivée par le fait qu’elle corresponde à autant d’équations qu’il n’y a de degrés de liberté. L’intuition (confirmée dans le cadre asymptotiquement hyperbolique) est alors que l’espace de modules des métriques d’Einstein devrait génériquement être discret. On s’attend au contraire à ce que les dégénérescences viennent de courbes de métriques et qu’elles soient alors associées à des comportements très particuliers. 

Remarque 2.26 . Il existe aussi beaucoup d’orbifolds kählériens qui ne peuvent pas être désingularisés par des métriques de Kähler-Einstein lisses. Il existe en effet des orbifolds sur des surfaces de Del Pezzo avec des seconds nombres de Betti arbitrairement grands alors qu’une métrique lisse sur une telle surface a un second nombre de Betti majoré par 9, voir l’exposition [And10]. Pour répondre à toutes ces questions, il est crucial de comprendre la complétion de l’espace de modules des métriques d’Einstein en dimension 4. C’est précisément l’objectif de cette thèse. 

# 2 Arbre de singularités 

L’objectif de cette section est de présenter les idées principales du théorème classique d’Anderson et Bando-Kasue-Nakajima ci-dessous. D’après ce théorème, la complétion au sens de Gromov-Hausdorff de l’espace de modules des métriques d’Einstein en dimension 4 consiste à ajouter des espaces singuliers particuliers, les 

orbifolds d’Einstein . Ils décrivent de plus les limites possibles au sens de Gromov-Hausdorff (pointé) d’éclatements. 2. Arbre de singularités 65 

Théorème 2.27 ([And89, BKN89]) . Soit (M 4 

> i

, g i)i∈N une suite de variétés d’Ein-stein de dimension 4 et de même constante d’Einstein satisfaisant : pour tout 

i ∈ N,1. le diamètre de (M 4 

> i

, g i) est uniformément majoré, 2. le volume de (M 4 

> i

, g i) est uniformément minoré, 3. l’énergie Ei := ∫  

> M4
> i

|Rm( gi)|2 

> gi

dvgi est uniformément majorée (c’est le cas si 

M 4 

> i

= M 4). Alors, il existe une sous-suite (M 4 

> i

, g i) convergeant vers un orbifold d’Einstein 

(M 4

> ∞

, g ∞), l’ espace singulier .De plus, à chaque singularité se forme un arbre de singularités , c’est-à-dire que les éclatements non triviaux convergent vers des orbifolds ALE qui se recollent avec une structure d’arbre. Ils sont reliés par des anneaux intermédiaire de basse énergie. 

Plutôt que de nous intéresser aux éclatements à l’échelle de la courbure comme cela a été fait historiquement, nous allons montrer qu’il est possible de directement identifier une structure d’arbre de singularités. 

2.1 Contrôles uniformes et ε-régularité 

Présentons pour commencer deux résultats qui nous permettent de traduire nos hypothèses géométriques en des contrôles analytiques uniformes. Tout d’abord, nous avons un contrôle uniforme de la constante de Sobolev d’une zone D qui est définie comme l’infimum des constantes S telles que l’on ait : pour toute fonction 

v de classe C1 à support compact, en notant ¯ v la moyenne de v sur D, on ait 

> ( ∫
> D

|v − ¯v| 2nn−2 

> )n−2
> n

6 S

> ∫
> D

|∇ v|2.

Lemme 2.28 ([Cro80, Theorem 13]) . Soit (M, g ) une variété riemannienne de dimension n telle que : — le diamètre est majoré par D0 > 0,— le volume est minoré par v0 > 0,— la courbure de Ricci est constante et minorée par −3.La constante de Sobolev S est majorée de la manière suivante : il existe une 66 Chapitre 2. Complétion de GH en dimension 4 

constante C > 0 ne dépendant que de la dimension telle que, 

S 6 C  

> (∫D0
> 0

sinh( s)ds )n−1

v0

> 
> n+1
> n−1

.

Des itérations de Nash-Moser combinées à des formules de la section suivante permettent alors de montrer que les régions avec une petite “énergie”, c’est-à-dire une petite norme L2 de leur courbure, sont bien contrôlées. 

Lemme 2.29 ([Gao90, Theorems 4.8, 4.9 et 4.11]) . Soit (M, g ) une variété d’Ein-stein de dimension 4 telle que : — le diamètre est majoré par D0 > 0,— le volume est minoré par v0 > 0,— la courbure de Ricci est constante et minorée par −3.Alors, il existe ε > 0 tel que pour tout ρ > 0 satisfaisant 

> ∫
> B(x, 2ρ)

| Rm g |2

> g

dvg < ε 2,

on ait sur B(x, ρ )

| Rm g |g 6 1

ρ2 .

2.2 Concentration de l’énergie à différentes échelles 

Étudions maintenant plus précisément les dégénérescences de métriques d’Ein-stein en dimension 4. Nous verrons qu’à part en un nombre fini de points, la convergence est lisse vers un espace lisse. Nous verrons qu’aux points que l’on qualifiera de singuliers , la courbure peut aussi diverger à des vitesses différentes et qu’il se forme des arbres de singularités .

Proposition 2.30. Soit (M, g i)i une suite de variétés d’Einstein satisfaisant : 1. Vol( gi) = 1 ,2. diam (gi) < D 0 pour D0 > 0 fixé. Alors, il existe une sous-suite convergeant vers un espace métrique (X∞, d ∞)

avec un nombre fini de points singuliers , (pk)k. C’est-à-dire que (X∞\{ pk}, d ∞) est une variété d’Einstein (incomplète) de dimension 4. Au cours de la dégénérescence se forment des arbres de singularités en chaque point singulier. Plus précisément, il existe des suites d’éclatements convergeant au sens de Gromov-Hausdorff vers des espaces non-compacts et lisses hors d’un nombre fini de points singuliers. 2. Arbre de singularités 67 

Démonstration. Soit ( M, g i)i une suite de métriques d’Einstein satisfaisant les hypothèses 1 et 2 de l’énoncé. Alors, d’après le théorème de compacité de Gromov, théorème 0.1, il existe une sous-suite convergeant au sens de Gromov-Hausdorff vers un espace métrique limite ( M∞, d ∞). Montrons que c’est un espace lisse à part à un nombre fini de points où des arbres de singularités de forment. Définissons donc pour commencer l’ensemble des points singuliers : 

S := 

> {

p ∈ M∞, ∀pi → p, ∀r > 0, lim inf  

> i
> ∫
> Bgi(pi,r )

| Rm( gi)|2 

> gi

dvgi > ε 

> }

,

où ε > 0 est la constante du lemme 2.29, et où les pi sont des points où la courbure diverge et convergeant grâce à la convergence de Gromov-Hausdorff vers 

p. Ce sont donc les points où l’on ne pourra à aucune échelle obtenir des bornes sur la courbure et une convergence lisse grâce au lemme 2.29. Il n’y a qu’un nombre fini de tels points car à chacun d’entre eux est associée une énergie strictement supérieure à ε. Il y en a donc un nombre inférieur à 8π2χ(M )

> ε

par (2.2). Hors de ces points, ( M∞, d ∞) est une variété d’Einstein de métrique lisse notée g∞ d’après le lemme 2.29, et la norme L2 de sa courbure est uniformément bornée par convergence lisse sur les compacts. Définissons alors r∞ tel que pour tout p ∈ S,

> ∫
> Bp(r∞)\p

| Rm( g∞)|2 

> g∞

dvg∞ < ε

2,

Comme la convergence est lisse sur les compacts de M∞\S, il existe pour tout i,

ri tel que ∫

> A(ri,r ∞)

| Rm( gi)|2 

> gi

dvgi = ε. 

Nous pouvons alors considérer une sous-suite de la suite ( M, r −2 

> i

gi, p i)i convergeant vers un espace métrique non compact. Par le même argument qu’au dessus, la limite est lisse hors d’un nombre fini de points et la norme L2 de sa courbure est bornée. L’espace est de plus non plat par définition de ri.En conclusion, nous obtenons une limite singulière ( M∞, d ∞) lisse partout sauf à un nombre fini de points. À chacun de ces points, en éclatant à la bonne échelle, nous trouvons un premier espace non trivial qui peut lui aussi toujours avoir des singularités. On peut alors éclater à ces points singuliers jusqu’à avoir une limite lisse, Ricci-plate et noncompacte. En effet chaque éclatement non lisse a une énergie plus grande que ε > 0. 68 Chapitre 2. Complétion de GH en dimension 4 

Remarque 2.31 . Le résultat est le même avec des topologies Mi variables tant que leur caractéristique d’Euler est bornée car cela contrôle l’énergie L2. On se ramène en fait à une topologie fixée en considérant une sous-suite. 

Remarque 2.32 . Ce genre de formation d’arbres de singularités est typique des problème variationnels en dimension critique, c’est-à-dire lorsque l’énergie étudiée est invariante par changement d’échelle comme c’est le cas ici avec la norme L2 de la courbure. 

Remarque 2.33 . Il manque plusieurs aspects important d’un bon résultat de conver-gence en arbre de singularités. Nous n’avons par exemple pour l’instant pas montré qu’il n’y avait pas d’énergie perdue dans les anneaux de basse courbure que l’on a identifiés. Nous n’avons pas non plus déterminé de lien entre la topologie M

et celles des différentes limites, ni obtenu de structure pour ces mêmes limites. Pour obtenir ces résultat, les articles [And89] et [BKN89] (et même [Ban90] qui s’appuie sur ces résultats) se focalisent sur la structure de M∞ et des limites d’écla-tements, mais nous verrons que tout découle en fait de l’analyse dans les anneaux intermédiaires et nous nous restreindrons donc à cette étude. 

# 3 Contrôle de la courbure des anneaux de basse énergie 

La norme du tenseur de courbure pour une métrique d’Einstein satisfait des équations différentielles particulières qui impliquent en fait que dans toute zone annulaire de basse énergie, la courbure se concentre aux bords de l’anneau. La démonstration de ce fait est l’objet de cette section qui est largement inspi-rée des techniques mises en œuvre dans [BKN89] puis [Ban90]. La difficulté ajoutée dans notre cas est que l’on s’intéresse à des anneaux finis dont les rapports entre les rayons intérieur et extérieur varient (et divergent lorsque des singularités se forment). Dans [BKN89], l’analyse est faite dans les cas limites où le rayon exté-rieur est infini ou bien dans le cas où le rayon intérieur est nul. 

Proposition 2.34. Soit (M, g ) une variété d’Einstein de dimension 4 telle que : — le diamètre est majoré par D0 > 0,— le volume est minoré par v0 > 0,— la courbure de Ricci est constante et minorée par −3.Il existe des constantes ε1 > 0, C > 0, β1 > 0 et β2 > 0 dépendant uniquement de D0 et v0 telles que si l’on a un anneau de basse courbure de rayons ρ1 > 0 et 3. Contrôle de la courbure des anneaux de basse énergie 69 

ρ2 > 0, avec ρ2 > 8ρ1 : ∫

> A(ρ1,ρ 2)

| Rm |2 < ε 21,

alors pour tout 2ρ1 6 ρ 6 ρ2 

> 4

, on a : 

ρ2| Rm | 6 C 

> (

ρ1

ρ

> )β1

+ 

> (

ρρ2

> )β2
> (∫
> A(ρ1,ρ 2)

| Rm |2 

> )12

sur l’anneau A(ρ, 2ρ).

La preuve de cette proposition se trouve dans la section 3.3 de ce chapitre. Ce qui signifie qu’au milieu de l’anneau, il y a un bien meilleur contrôle qu’ini-tialement prévu par les théorèmes d’ ε-régularité classiques comme le lemme 2.29 qui donneraient seulement ρ2| Rm | 6 C‖ Rm ‖L2(A(ρ1,ρ 2)) .Analytiquement, cela permettra de faire de l’analyse dans des espaces à poids où les opérateurs qui nous intéressent sont Fredholm. 

Remarque 2.35 . L’énoncé et sa preuve sont très proches de la proposition 3 de [Ban90]. La différence est la présence du facteur (∫ 

> A(ρ1,ρ 2)

| Rm |2) 12 .

3.1 Inégalités différentielles sur la courbure 

Les estimations sur la courbure qui nous permettent de construire des coordon-nées sur la zone de transition (ou autrement dit un difféomorphisme entre cette zone et un anneau d’un cône plat) viennent toutes d’une formule de Weitzenböck et de ce qu’elle implique sur le tenseur de courbure d’une variété d’Einstein. 

Proposition 2.36. Pour tout n ∈ N, il existe C > 0 telle que pour toute variété d’Einstein de dimension n :

∆| Rm | > −C| Rm |2.

Démonstration. Notons d : Γ(Ω p ⊗ Ω2) → Γ(Ω p+1 ⊗ Ω2) la différentielle extérieure quelque soit p ∈ N, et δ son adjoint formel. En considérant le laplacien dδ + δd , on a la formule de Weitzenböck [BL81, Theorem 3.2] suivante : (dδ + δd ) Rm = ∇∗∇ Rm + Q(Rm) ,

où Q est une forme quadratique ne dépendant que de la dimension. 70 Chapitre 2. Complétion de GH en dimension 4 Cette formule implique l’égalité suivante : ∆| Rm |2 := −∇ ∗∇| Rm |2 = −2 〈(dδ + δd ) Rm , Rm 〉+2 |∇ Rm |2 −2 〈Q(Rm) , Rm 〉 .

Dans le cas d’une variété d’Einstein, la courbure est harmonique pour le la-placien − (dδ + δd ). En effet, la seconde identité de Bianchi assure d’une part que 

d Rm = 0 ,

et d’autre part que pour trois champs de vecteurs X,Y et Zδ Rm( X, Y, Z ) = d∇ Ric( Y, Z, X ),

où pour h un 2 tenseur on définit d∇h(X, Y, Z ) := ∇X h(Y, Z ) − ∇ Y h(X, Z ). Pour une variété d’Einstein, comme Ric est constante, nous avons (dδ + δd ) Rm = 0 .

On peut ainsi écrire : ∆| Rm |2 > −2 〈Q(Rm) , Rm 〉 ,

par l’inégalité de Cauchy-Schwarz. On en déduit qu’il existe C′ > 0, telle que : ∆| Rm |2 > −C′| Rm |3.

Maintenant, comme pour toute fonction g : R → R, et α ∈ R on a ∆( gα) = α(α − 1) gα−2|∇ g|2 + αg α−1∆g, (2.6) on en déduit, pour g = | Rm |2 et α = 12 , que : ∆| Rm | = −14| Rm |−3 ∣∣∣∇| Rm |2∣∣∣2

+ 12| Rm |−1∆| Rm |2 > −C′

2 | Rm |2.

Une autre inégalité différentielle est satisfaite par la norme de la courbure. 

Proposition 2.37. Pour tout n ∈ N, il existe γ∗ > 0 et C > 0 telles que pour toute variété d’Einstein de dimension n :

∆| Rm |1−γ∗ > −C| Rm |2−γ∗ .3. Contrôle de la courbure des anneaux de basse énergie 71 

Remarque 2.38 . De plus, en dimension 4, on peut choisir γ∗ = 23 (ce qu’on ne prouvera pas ici, voir [BKN89]). 

Démonstration. La preuve consiste à reprendre l’égalité : ∆| Rm |2 = 2 |∇ Rm |2 − 〈 Q(Rm) , Rm 〉 , (2.7) et d’être plus précis au niveau du contrôle du terme 2 |∇ Rm |2 avec l’estimation suivante connue sous le nom d’inégalité de Kato améliorée :

Lemme 2.39 ([BKN89, lemme 4.9], [CGH00, Théorème 5.1]) . Pour tout n ∈ N,il existe γ∗ > 0 tel que l’on ait pour toute métrique d’Einstein de dimension n :

(1 + γ∗)|(Rm , ∇ Rm) |2 6 | Rm |2|∇ Rm |2,

où (Rm , ∇ Rm)( X) = (Rm , ∇ Rm( X)) .

Le terme 2 |∇ Rm |2 de (2.7), peut donc être contrôlé par : 

|∇ Rm |2 > (1 + γ∗)|(∇ Rm , Rm) |2

| Rm |2 = (1 + γ∗)|∇| Rm ‖2.

On en déduit donc ∆| Rm |2 > 2(1 + γ∗)|∇| Rm ‖2 − C′| Rm |3. (2.8) En utilisant la formule (2.6) avec g = | Rm |2 et α = 1−γ∗ 

> 2

, on a : ∆| Rm |1−γ∗ = − (1 + γ∗)(1 − γ∗)4 | Rm |2(1−γ∗ 

> 2−2

)|∇| Rm |2|2

+ 1 − γ∗

2 | Rm |2(1−γ∗ 

> 2−1

)∆| Rm |2.

En utilisant l’inégalité (2.8), on obtient : ∆| Rm |1−γ∗ > − (1 + γ∗)(1 − γ∗)4 | Rm |2(1−γ∗ 

> 2−2

)|∇| Rm |2|2

+ 1 − γ∗

2 | Rm |2(1−γ∗ 

> 2−1

) (

2(1 + γ∗)|∇| Rm || 2 − C′| Rm |3)

.

Comme |∇| Rm |2|2 = 4 | Rm |2 |∇| Rm || 2, les deux premiers termes se com-pensent et il reste exactement : ∆| Rm |1−γ∗ > −C′(1 − γ∗)2 | Rm |2−γ∗ .72 Chapitre 2. Complétion de GH en dimension 4 De ces inégalités, on va pouvoir déduire des contrôles sur | Rm | venant de l’étude de l’inéquation différentielle ∆ u > −f u en prenant u = | Rm |1−γ∗ ou 

| Rm | et f = C| Rm |.

3.2 Étude des solutions de l’équation ∆u > −f u 

On présente ici des lemmes techniques sur les solutions de l’équation ∆u > −f u. 

L’analyse de [BKN89] est adaptée d’une part à Rn\B(0 , 1) et d’autre part à 

B(0 , 1) \{ 0} et leurs espaces à poids respectifs. Ici, nous utilisons plutôt l’analyse de [Ban90] où l’étude est adaptée aux an-neaux. Nous obtenons des contrôles dans des espaces à poids qui en un sens ne dépendent pas du rapport des rayons intérieurs et extérieurs et qui sont donc pra-tiques lorsque ces rapports varient (et divergent dans notre cas). Lorsque le rayon intérieur tend vers 0 à rayon extérieur constant égal à 1, on retrouve les espaces à poids habituels sur B(0 , 1) \{ 0} et quand le rayon extérieur tend vers l’infini à rayon intérieur constant égal à 1, on retrouve les espaces classiques sur Rn\B(0 , 1). 

Convexité des intégrales de u dans les zones de petite énergie. Pour cela on commence par contrôler des quantités intégrales sur u (qui représentera soit | Rm |, soit | Rm |1−γ∗ ), essentiellement par injections de Sobolev. 

Lemme 2.40 ([Ban90, Lemma 1,2]) . Soient n ∈ N S > 0, V > 0, 1 < p 0 < p 1.Alors, il existe ε0(S, V, p 0, p 1) > 0, C(S, V, p 0) > 0, β1(S, V, p 0), β 2(S, V, p 0) > 0

tels pour tous 0 < ρ 1 < 18 ρ2 que si (M, g ) est une variété riemannienne pointée de dimension n telle que que sur un anneau de rayons ρ1 et ρ2, A(ρ1, ρ 2), on ait : 1. la constante de Sobolev sur l’anneau majorée par S.2. vol (A(ρ1, ρ )) 6 V ρ n pour tous ρ1 6 ρ 6 ρ2.Soit f ∈ Ln 

> 2

et u ∈ Lp, avec 1 < p 0 6 p 6 p1 une solution de : 

∆u > −f u. 

Alors, si ∫

> A(ρ1,ρ 2)

f n 

> 2

6 εn 

> 2
> 0

,

on a, pour tout ρ tel que ρ1 6 ρ 6 8ρ 6 ρ2 :3. Contrôle de la courbure des anneaux de basse énergie 73 

1. la fonction u est en fait aussi dans L nn−2 p :

> (∫
> A(2 ρ, 4ρ)

u nn−2 p 

> )n−2
> n

6 Cρ −2

> ∫
> A(ρ, 8ρ)

up.

2. si on a de plus p > 2, l’énergie d’un anneau est contrôlée par sa distance aux deux bords de l’anneau : Il existe β1 > 0 et β2 > 0 tels que : 

> ∫
> A(2 ρ, 4ρ)

up 6 C 

> (

ρ1

ρ

> )β1

+ 

> (

ρρ2

> )β2
> ∫
> A(ρ1,ρ 2)

up.