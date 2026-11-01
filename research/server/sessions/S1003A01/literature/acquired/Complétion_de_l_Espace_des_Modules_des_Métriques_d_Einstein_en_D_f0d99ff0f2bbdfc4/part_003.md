---
retention_scope: session
part: 3
total_parts: 7
---

[Part 3/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

Remarque 2.41 . Les hypothèses techniques 1 et 2 de ce lemme seront satisfaites par les variétés que l’on considérera car elles sont à courbure de Ricci bornée et non effondrées grâce à l’inégalité de Bishop-Gromov et au lemme 2.28. 

Convexité en norme L∞. Nous avons donc un contrôle de quantités intégrales sur u. Des itérations de Moser, vont nous permettre d’en déduire un contrôle en norme L∞.

Lemme 2.42 ([Ban90, Lemma 3]) . Sous les hypothèses du lemme 2.40, si l’on suppose de plus f ∈ Lq pour q > n 

> 2

et u ∈ Lp, p > 1, et qu’il existe A > 0 tel que pour tout ρ ∈ [ρ1, ρ2 

> 8

] on ait, 

> ∫
> A(ρ, 8ρ)

f q 6 Aρ −(2 q−n),

alors, il existe C = C(A, S, V, p, q ) > 0 telle que, 

sup 

> A(2 ρ, 4ρ)

up 6 Cρ −n

> ∫
> A(ρ, 8ρ)

up.

3.3 Conséquences pour la courbure des anneaux de basse énergie 

Remarquons alors que les anneaux de basse énergie reliant deux échelles de for-mation de singularité satisfont effectivement les hypothèses techniques des lemmes 2.40 et 2.42 précédents. Rappelons nos hypothèses : — le diamètre est majoré par D0 > 0, — le volume est minoré par v0 > 0, — la courbure de Ricci est constante et minorée par −(n − 1). 74 Chapitre 2. Complétion de GH en dimension 4 La constante de Sobolev est elle aussi contrôlée par le diamètre, le volume et la courbure de Ricci d’après le lemme 2.28 et l’hypothèse 1 du lemme 2.42 est donc satisfaite. Les dégénérescences que l’on considère sont à volume minoré et diamètre majoré ce qui combiné à la borne inférieure sur la courbure de Ricci implique que les volumes des anneaux sont majorés par le théorème de Bishop-Gromov. L’hypothèse 2 du lemme 2.42 est donc satisfaite. 

Preuve de la proposition 2.34. Soit une zone annulaire satisfaisant les hypothèses de l’énoncé. Elle satisfait donc les hypothèses techniques des lemmes 2.40 et 2.42. D’après les propositions 2.36 et 2.37, u1 := | Rm | et u2 := | Rm |1−γ∗ satisfont ∆u1 > −f u 1, et ∆ u2 > −f u 2,

avec f := C| Rm | = Cu 1 = Cu 11−γ∗ 

> 2

. Nous allons leur appliquer les lemmes précé-dents afin d’obtenir le contrôle souhaité. Soit ε1 > 0 telle que : ε1 < C −1/2ε0 où ε0 est la constante introduite dans le lemme 2.40. On a alors bien ∫ 

> A(ρ1,ρ 2)

f 2 < ε 20, et en appliquant le point 1 du lemme 2.40 à u1, on obtient, avec p = 2 : 

> (∫
> A(2 ρ, 4ρ)

u41 

> )12

6 Cρ −2

> ∫
> A(ρ, 8ρ)

u21.

Maintenant, comme f = −Cu 1, on a : 

> ∫
> A(2 ρ, 4ρ)

f 4 6 C2ρ−4

> ( ∫
> A(ρ, 8ρ)

f 2

> )2

6 Aρ −(2 ×4−4) ,

avec A = C2 (∫ 

> A(ρ1,ρ 2)

f 2)2

6 C2ε20. En d’autres termes, f satisfait en fait les hypothèses du lemme 2.42 avec q = 4 > n 

> 2

= 2. En considérant u2 et p′ := 2(1 −γ∗) > 

> nn−2

= 2, il existe donc une constante C′ (du lemme 2.42) telle qu’on ait : sup 

> A(2 ρ, 4ρ)

up′ 

> 2

6 C′ρ−n

> ∫
> A(ρ, 8ρ)

up′ 

> 2

,

c’est-à-dire : sup 

> A(2 ρ, 4ρ)

| Rm |2 6 C′ρ−4

> ∫
> A(ρ, 8ρ)

| Rm |2. (2.9) Or, par le point 2 du lemme 2.40, avec le même p′ := 2(1 −γ∗) > 2 il existe β1 > 0 et 4. Orbifolds et espaces ALE 75 

β2 > 0 tels que l’on ait : 

> ∫
> A(ρ, 8ρ)

| Rm |2 6 C 

> (

ρ1

ρ

> )2β1

+ 

> (

ρρ2

> )2β2
> ∫
> A(ρ1,ρ 2)

| Rm |2. (2.10) Les inégalités (2.9) et (2.10) combinées donnent le contrôle énoncé : sup 

> A(2 ρ, 4ρ)

| Rm |2 6 Cρ −4 

> (

ρ1

ρ

> )2β1

+ 

> (

ρρ2

> )2β2
> ∫
> A(ρ1,ρ 2)

| Rm |2.

Remarque 2.43 . On peut obtenir des résultats tout à fait analogues en dimension 

n en supposant des contrôles bien moins naturels sur la norme Ln 

> 2

de la courbure de Riemann. 

# 4 Orbifolds et espaces ALE 

Montrons maintenant nos espaces limites sont en réalité des orbifolds et orbi-folds ALE. Nous obtiendrons ainsi une bonne description de la dégénérescence à toutes les échelles. 

4.1 Structure des singularités 

Nous avons donc des contrôles ponctuels satisfaisants sur la courbure dans les anneaux reliant les différentes échelles de singularités. 

Corollaire 2.44. Soit g∞ une des limites de l’arbre de singularités identifié dans la proposition 2.30. Il existe β > 0 tel qu’on ait 1. au voisinage des points singuliers de g∞, la courbure est un O(r−2+ β ), où r

est la distance au point singulier et 2. à l’infini, si g∞ est noncompact, la courbure est un O(r−2−β ), où r est la distance à un point quelconque fixé. 

Après la construction de coordonnées, ce contrôle de la courbure implique que les différentes limites obtenues dans la proposition 2.30 sont des orbifolds et que leurs infinis sont ALE. 

Proposition 2.45. Soit β > 0 la constante du corollaire 2.44 précédent. Au voi-sinage de chaque point singulier il existe des constantes Ck > 0 pour k ∈ N et un 76 Chapitre 2. Complétion de GH en dimension 4 

difféomorphisme local ϕ d’un voisinage de 0 dans (R4/Γ, g e) vers un voisinage du point singulier de (M∞, g ∞) tel que l’on ait 

rke |∇ ke (ϕ∗g∞ − ge)|ge < C krβe (2.11) 

De même, il existe un difféomorphisme ψ entre un voisinage de l’infini de (R4/

Γ, g e) vers un voisinage de l’infini d’un limite d’éclatements de la proposition 2.30, tel que l’on ait 

rke |∇ k(ψ∗g∞ − ge)|ge < C kr−βe . (2.12) 

Idées de preuve. Nous ne donnons qu’une idée de preuve ici car le chapitre 3 sui-vant apportera une preuve plus générale. Nous avons donc un contrôle de la cour-bure d’après le corollaire 2.44 et nous souhaitons montrer que dans de bonnes coordonnée, cela traduit un contrôle de la métrique. L’idée est assez naturellement d’utiliser des coordonnées géodésiques qui sont bien contrôlées par la courbure ambiante par l’équation de Riccati. En considérant donc une carte géodésique au voisinage d’un point singulier, on obtient le contrôle énoncé. Pour le contrôle à l’infini, un argument un peu plus subtil est nécessaire. La première étape est de trouver une hypersurface Σ 0 à seconde forme fondamentale presque constante, ce qui est assuré par un résultat difficile de [Kas88]. Enfin, l’idée est de considérer les géodésiques partant orthogonalement vers l’extérieur de l’hypersurface Σ 0. L’équation de Riccati assure alors d’une part que les géodésiques ne s’intersectent pas, mais cela assure de plus que la seconde forme fondamentale des lignes de niveaux de la distance à Σ 0, une fois rééche-lonnée converge vers l’identité lorsque la distance tend vers l’infini. Le contrôle de la courbure ambiante implique alors que ces sphères rééchelonnées convergent vers une variété à courbures sectionnelles positives constantes par les formules de Gauss. D’après le lemme 1.54, c’est donc un quotient de la sphère ronde S3 par un groupe fini Γ ⊂ SO (4) agissant librement dessus. En particulier, comme il n’y a pas de point conjugué, hors du compact à l’intérieur de l’hypersurface Σ 0, la variété est difféomorphe à ( R4\Be(0 , 1)) /Γ. En intégrant l’équation de Riccati le long des géodésiques depuis l’infini jusqu’à Σ0, on obtient alors un contrôle de la métrique restreinte aux hypersurfaces et de leur seconde forme fondamentale. On en déduit un contrôle de la métrique ambiante qui est proche de la métrique plate avec une décroissante à l’infini. On déduit aussi du contrôle sur la courbure des anneaux de la proposition 2.34 que l’ énergie , c’est-à-dire le carré de la norme L2 de la courbure, de la suite de 4. Orbifolds et espaces ALE 77 variétés dégénérant correspond exactement à la somme des énergies de l’orbifold limite et des différents orbifolds Ricci-plats ALE qui apparaissent. 

Corollaire 2.46 (Conservation de l’énergie) . Sous les hypothèses du théorème 2.34, l’énergie de (M 4 

> i

, g i) est égale à la somme de l’énergie de l’orbifold (M 4

> ∞

, g ∞)

et de celles de toutes les variétés Ricci-plates ALE apparaissant dans les arbres de singularités se formant aux points singuliers de (M 4

> ∞

, g ∞).

Nous en déduirons aussi à l’aide des constructions de coordonnées du chapitre 3 les théorèmes de structures suivants pour nos arbres de singularités. 

Théorème 2.47 ([Ban90, Theorem 1, Proposition 2]) . Soit (M 4 

> i

, g i)i∈N une suite de variétés d’Einstein de dimension 4 et de même constante d’Einstein satisfai-sant : 1. le diamètre de (M 4 

> i

, g i) est uniformément majoré, 2. le volume de (M 4 

> i

, g i) est uniformément minoré, 3. l’énergie ∫  

> M4
> i

|Rm( gi)|2dv(gi) est uniformément majorée (cette hypothèse est en fait impliquée par les deux précédentes d’après [CN15]). Alors, il existe une sous-suite (M 4 

> i

, g i) convergeant vers un orbifold d’Einstein 

(M 4

> ∞

, g ∞) au sens de Gromov-Hausdorff. Pour chaque point singulier p∞ dont la singularité est modelée sur R4/Γ pour 

Γ un sous-groupe de SO (4) , il existe une suite de points (pi)i∈N de M 4 

> i

de haute courbure |Rm( gi)|(pi) → ∞ , et une suite de réels Ti → 0 appelés premières échelles 

de singularité tels que : (

M 4 

> i

, gi 

> Ti

, p i

> )

converge au sens de Gromov-Hausdorff vers 

(N, g b, p ) un orbifold Ricci-plat ALE asymptotique à R4/Γ. De plus, pour tout 

ε > 0, il existe δ > 0 ne dépendant que de ε > 0, (N, g b, p ) et (M 4

> ∞

, g ∞) tel qu’en notant Ai(δ) l’anneau de rayons √Ti 

> δ

et δ centré en pi, on ait pour i suffisamment grand : ∫

> Ai(δ)

| Rm( gi)|2dv(gi) < ε 2.

Remarque 2.48 . Plus généralement, il se forme un arbre de singularités en chaque point singulier comme décrit dans la proposition 2.30. En effet, en considérant ensuite la suite de métriques pointées (

M 4 

> i

, gi 

> Ti

, p i

> )

, on obtient de nouvelles “pre-mières” échelles de singularités. On peut alors itérer jusqu’à obtenir tout l’arbre de singularités. Pour δ > 0 assez petit et i assez grand, chaque boule Bgi (pi, δ ) a la topologie d’un recollement d’un nombre fini, k ∈ N, d’orbifolds Ricci-plats ALE 

{(Nj , g bj , p j )} pour j ∈ { 1, ..., k } avec un nombre fini de singularités. L’infini de chaque orbifold Ricci-plat ALE asymptotique à R4/Γ est recollé au point singulier d’un autre orbifold modelé sur R4/Γ le long d’une sphère S3/Γ. 78 Chapitre 2. Complétion de GH en dimension 4 

4.2 Coordonnées d’ordre optimal 

Finalement, nous pouvons en réalité montrer que la courbure décroît à des ordres particuliers aux points singuliers et à l’infini. 

Lemme 2.49 (Fonctions harmoniques sur R4/Γ) . Soit f une fonction harmonique bornée sur un anneau Ae(r1, r 2) de R4/Γ centré en zéro de rayons 0 6 r1 < r 2 6

+∞. Alors, c’est une somme dénombrable de fonctions harmoniques homogènes de degrés k et −2 − k pour k ∈ N. De plus, pour Γ 6 = {Id }, nous avons k 6 = 1 .Démonstration. Soit f une fonction harmonique bornée sur un anneau Ae(r1, r 2). C’est donc la solution du problème de Dirichlet donné par f|Se(r1) sur Se(r1), la sphère de rayon r1 et f|Se(r2) sur Se(r2). Notons que si r2 = + ∞, nous considérons sa limite à l’infini comme étant une condition de Dirichlet. Cherchons à construire une autre solution du problème de Dirichlet comme dans l’énoncé du lemme. Le principe du maximum nous assurera qu’elle est égale à f . Développons f|Se(r1) et f|Se(r2) en harmoniques sphériques. C’est-à-dire qu’il existe des fonctions propres du laplacien sur S3/Γ associées à la valeur propre 

−k(k + 2) pour k ∈ N, Fk(r1) et Fk(r2), telles que l’on ait : 

f|Se(r1) = ∑

> k

Fk(r1), (2.13) et 

f|Se(r2) = ∑

> k

Fk(r2). (2.14) Notons alors que les rke Fk et les r−2−ke Fk sont harmoniques où re est la distance euclidienne à 0. Si r1 = 0, alors nous avons f = ∑

> krke
> rk
> 2

Fk(r2) par le principe du maximum et si 

r2 = + ∞, alors nous avons f = lim re→+∞ f + ∑

> kr2+ k
> 1
> r2+ ke

Fk(r1). Dans le cas intermédiaire où la fonction est bornée sur un anneau fini, la solution est un peu moins directe. Nous cherchons un développement 

> ∑
> k>0

rke ˜F + 

> k

+ r−2−ke ˜F −

> k

dont les valeurs aux bords sont 

> ∑
> k>0

rk 

> 1

˜F + 

> k

+ r−2−k 

> 1

˜F − 

> k

= ∑

> k>0

Fk(r1)4. Orbifolds et espaces ALE 79 et ∑

> k>0

rk 

> 2

˜F + 

> k

+ r−2−k 

> 2

˜F − 

> k

= ∑

> k>0

Fk(r2),

c’est-à-dire que l’on pose ˜F + 

> k

= 1

rk 

> 1

r−2−k 

> 2

− rk 

> 2

r−2−k

> 1
> (

r−2−k 

> 2

Fk(r1) − r−2−k 

> 1

Fk(r2))

,

et ˜F − 

> k

= 1

rk 

> 1

r−2−k 

> 2

− rk 

> 2

r−2−k

> 1
> (

− rk 

> 2

Fk(r1) + rk 

> 1

Fk(r2))

.

Le principe du maximum nous assure donc encore une fois que f = ∑ 

> k>0

rke ˜F + 

> k

+

r−2−ke ˜F − 

> k

.Le fait que k = 1 n’apparaisse pas lorsque Γ 6 = {Id } vient simplement du fait qu’une fonction linéaire (un reF1) invariante par Γ est nécessairement nulle et que la valeur propre −3 n’apparaît alors pas sur S3/Γ. 

Lemme 2.50. Sur R4/Γ pour Γ 6 = {Id }, il n’y a pas de 2-tenseur homogène harmonique dont les coefficients soient d’ordre −2 ou −3 en jauge de Bianchi, il n’y en a en particulier pas en jauge divergence et à trace nulle. Démonstration. Ce résultat est prouvé dans [CT94, p. 537-538]. Un 2-tenseur ho-mogène harmonique h à coefficients d’ordre −2 ou −3 sur R4/Γ se tire en arrière sur R4 comme des matrices dont les coefficients sont des fonctions harmoniques homogènes. Comme vu dans la preuve précédente, si Γ 6 = {Id }, alors la valeur propre −3 n’apparaît pas et il n’y a pas de 2-tenseur harmonique en r−3.Un élément du noyau de ∇∗

> e

∇e homogène à coefficients d’ordre −2 s’écrit H0

> r2
> e

pour H0 un 2-tenseur constant sur R4. Un tel 2-tenseur n’est à divergence nulle que s’il s’annule car nous avons 

δe 

> (

H0

r2

> e
> )

= 2 H0(∂re , . )

r3

> e

,

et, si x ∈ R4 un vecteur propre de H0 de valeur propre λ, comme ∂re (x) = x 

> |x|

, et nous avons alors δe 

> (H0
> r2
> e
> )
> x

( x 

> |x|

) = −2H0( x     

> |x|,x
> |x|)
> r3
> e(x)

= −2 λr3  

> e(x)

.

Proposition 2.51. Au voisinage de chaque point singulier il existe des constantes 

Ck > 0 pour k ∈ N et un difféomorphisme local ϕ d’un voisinage de 0 dans (R4/

Γ, g e) vers un voisinage du point singulier de (M∞, g ∞) tel que l’on ait 

rke |∇ ke (ϕ∗g∞ − ge)|ge < C kr2 

> e

(2.15) 80 Chapitre 2. Complétion de GH en dimension 4 

Et de plus, la métrique ϕ∗g∞ est lisse (et même analytique) lorsqu’elle est tirée en arrière sur R4.De même, il existe un difféomorphisme ψ entre d’un voisinage de l’infini de 

(R4/Γ, g e) vers un voisinage de l’infini d’un limite d’éclatements de la proposition 2.30, tel que l’on ait 

rke |∇ k(ψ∗g∞ − ge)|ge < C kr−4 

> e

. (2.16) 

Démonstration. Considérons les coordonnées obtenues dans la proposition 2.45. Il est alors possible de construire des coordonnées dans lesquelles la métrique est en jauge de Bianchi par rapport à la métrique Euclidienne. En effet, cela revient à résoudre le problème de Dirichlet suivant : 

B(exp ge X)∗ge g = 0 ,

avec la condition de bord 

X = 0 sur Be(0 , ε )pour un certain ε > 0. L’équation satisfaite par ϕ∗g qui est d’Einstein par rapport à ge se réécrit alors 

∇∗

> e

∇e(ϕ∗g − ge) = Λ( ϕ∗g) + Qe(ϕ∗g), (2.17) où Qe est quadratique en ϕ∗g et ses deux premières dérivées. Par hypothèse, nous avons rie|∇ ie(ϕ∗g − ge)|ge = O(rβe ), puis (2.17) implique 

∇∗

> e

∇e(ϕ∗g − ge) = O(1) + O(r−2+2 βe ) (2.18) puis comme il n’y a pas d’élément du noyau de ∇∗

> e

∇e décroissant plus lentement que r2 en zéro, nous avons rie|∇ ie(ϕ∗g − ge)|ge = O(rmin(2 β, 2)  

> e

). En itérant cet argu-ment, nous obtenons finalement que 

rie|∇ ie(ϕ∗g − ge)|ge = O(r2 

> e

).

Pour montrer que la métrique est lisse une fois tirée en arrière sur R4, on utilise le théorème de singularité effaccable [BKN89, Theorem 5.1] dont la preuve est essen-tiellement contenue dans [Gao90] et qui est basée sur un argument par itérations de Moser plus simple que celui de la partie précédente. La preuve dans le cas noncompact est similaire et s’appuie sur le fait que les éléments du noyau en 1 

> r2

ou 1 

> r3

et en jauge de Bianchi sont nuls d’après le lemme 2.50. 4. Orbifolds et espaces ALE 81 

Remarque 2.52 . On ne peut pour l’instant rien dire à propos de la métrique sur un anneau fini de basse énergie. En effet, le contrôle de la métrique passe par la construction de coordonnées qui s’appuient sur l’asymptotique de la métrique à l’infini ou au point singulier, ce qui n’est pas encore établi sur un anneau fini. Nous verrons comment une nouvelle construction de coordonnées optimales permet de s’en sortir et permettrait aussi de retrouver le lemme précédent. 82 Chapitre 2. Complétion de GH en dimension 4 Chapitre 3 De Gromov-Hausdorff à C∞ àpoids au voisinage d’une métrique singulière 

Dans ce chapitre, dont les résultats sont essentiellement tirés de [Ozu19a], nous montrons que toute métrique d’Einstein suffisamment proche d’un orbifold d’Einstein au sens de Gromov-Hausdorff est en fait proche de la désingularisation de l’orbifold par le recollement a priori naïf de variétés Ricci-plates ALE aux points singuliers de l’orbifold. Cette proximité est mesurée par une norme C∞ àpoids (voir le théorème 3.42) qui est plus forte que la norme C∞ et qui est cruciale pour les chapitres 4 et 5 suivants. La difficulté principale de la preuve consiste à analyser les anneaux de basse courbure qui relient les bulles et les espaces singuliers et à y construire des coordonnées optimales. Le résultat principal est le théorème 3.42 énoncé à la fin du chapitre. 

Contributions. Nous raffinons la convergence des métriques d’Einstein vers leurs limites singulières en dimension 4. Nous prouvons qu’une telle dégénéres-cence est contrôlée dans des espaces de Hölder à poids. Cette convergence est cruciale car c’est dans ces espaces que l’analyse de la suite de la thèse se placera. 83 84 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

# 1 Arbres des singularités et désingularisations naïves 

Donnons pour commencer des définitions et expliquons pourquoi notre preuve se résume à étudier les anneaux de basse courbure analysés dans le chapitre 2 précédent. 

1.1 Désingularisation naïve d’orbifold 

Par [Ban90] et les résultats du chapitre 2, lorsqu’une suite de métriques d’Ein-stein dGH -converge vers un orbifold d’Einstein, un arbre de singularités se forme à chaque point singulier. Un tel arbre de singularités donne en réalité aussi une configuration de désingularisation de l’orbifold par des orbifolds ALE. 

Définition 3.1 (Configuration de désingularisation) . Soit ( Mo, g o) un orbifold d’Einstein et So l’ensemble de ses points singuliers, et ( Nj , g bj )j une famille d’es-paces ALE Ricci-plats asymptotiques à R4/Γj à l’infini et ( Sbj )j l’ensemble de ses points singuliers. Définissons aussi une application de recollement 

p : j 7 → pj ∈ So ∪ ⋃

> k

Sbk ,

où la singularité en pj est aussi R4/Γj . Nous appellerons 

D := (

(Mo, g o, S o), (Nj , g bj , S bj )j , p )

une configuration de désingularisation pour ( Mo, g o). 

Exemple 3.2. Les arbres de singularités du chapitre précédent (ch. 2) apparais-sant dans les dégénérescences de variétés d’Einstein sont des configurations de désingularisation. La question 0.5 s’intéresse donc à sa réciproque : quand est-ce qu’une configuration de désingularisation D est l’arbre de singularités apparaissant lors d’une dégénérescence de métriques d’Einstein ? Définissons les métriques qui imiteront la dégénérescence de métriques d’Ein-stein décrite dans le chapitre 2. Nous qualifierons ces désingularisations de naïves 

dans un premier temps et le but de ce chapitre sera de montrer que ce sont fina-lement de bonnes approximations de la dégénérescence. Définissons tout d’abord le recollement naïf d’un espace ALE à une singularité d’un orbifold. Reprenons pour cela la constante ε0 > 0 des définitions 2.2 et 2.3. 1. Arbres des singularités et désingularisations naïves 85 Soit 0 < 2ε < ε 0, 0 < t < ε 4, ( Mo, g o) un orbifold, et Φ : Be(0 , ε 0) ⊂ R4/

Γ → U une carte locale autour d’un point singulier p ∈ Mo satisfaisant Φ ∗go =

ge + O(r2 

> e

). Soit aussi ( N, g b) un orbifold ALE asymptotique à R4/Γ, et Ψ ∞ : ( R4/

Γ∞)\Be(0 , ε −10 ) → N \K une carte d’un voisinage de l’infini où l’on a Ψ ∗∞gb =

ge +O(r−4 

> e

), voir le lemme 2.51. Considérons finalement χ : R+ → R+, une fonction de coupure C∞ supportée dans [0 , 2] et égale à 1 sur [0 , 1], et définissons pour tout 

s > 0, ϕs : x ∈ R4/Γ → sx ∈ R4/Γ, ce qui induit en particulier l’identification suivante 

ϕ√t(Ae(ε−10 , ε 0t−1/2)) = Ae(ε−10

√t, ε 0).

Nous définissons alors l’orbifold Mo#N comme N recollé à Mo à l’aide du difféomorphisme Φ ◦ϕ√t ◦Ψ−1 : Ψ( Ae(ε−10 , ε 0t−1/2)) → Φ( Ae(ε−10

√t, ε 0)) identifiant leurs anneaux Φ( Ae(ε−10

√t, ε 0)) et Ψ( Ae(ε−10 , ε 0t−1/2)). 

Définition 3.3 (Recollement naïf d’espace ALE à un orbifold) . On définit une 

désingularisation naïve de ( Mo, g o) en p par ( N, g b) à l’échelle t, que l’on notera (Mo#N, g o#p,t gb) où l’on définit go#p,t gb = go sur Mo\U , go#p,t gb = tg b sur K ⊂

N , et en tirant en arrière sur l’anneau plat la métrique interpole entre les métriques ALE et orbifold 

go#p,t gb = χ(t−1/4re)Φ ∗go + t(

1 − χ(t−1/4re))

ϕt1/2,∗Ψ∗∞gb

sur A(t, ε 0) := Ae(ε−10

√t, ε 0). 

Figure 3.1 – Recollement naïf. Plus généralement, il est possible de désingulariser des orbifolds itérativement à l’aide d’arbres d’orbifolds Ricci-plats ALE. Soient 0 < 2ε < ε 0, ( Mo, g o) un orbifold d’Einstein orbifold et ( Nj , g bj )j un arbre d’orbifolds Ricci-plats ALE tels que M = Mo#j Nj soit donnée par une 86 Chapitre 3. De Gromov-Hausdorff à C∞ à poids configuration de désingularisation D, et soit t = ( tj )j avec 0 < t j < ε 4 les échelles relatives de recollement .

Définition 3.4 (Désingularisation naïve d’un orbifold) . La métrique de désingu-larisation naïve gDt est alors le résultat de la construction itérative suivante. Démarrer avec une bulle la plus profonde ( Nj , g bj ), c’est-à-dire avec j pour lequel Sj = ∅. Si pj ∈ Nk (la même chose marche avec pj ∈ Mo), alors remplacer (Nk, g bk , S j ) par ( Nk#Nj , g bk #pj ,t j gbj , S k\{ pj }), supprimer ( Nj , g bj , ∅) dans D et restreindre p par l → pl sur l 6 = j dans D. Considérer ensuite une autre bulle la plus profonde, et appliquer le procédé précédent jusqu’à ce qu’il n’y ait plus de point singulier. Pour t = ( tj )j , si Nj est recollé à pj ∈ Nj1 , et Nj1 est recollé à pj1 ∈ Nj2 , ..., 

Njk−1 est recollé à Njk , qui est recollé à Mo, on définit Tj := tj tj1 tj2 ...t jk l’échelle de la bulle j. Avec cette notation, sur chaque Nj (2 ε), la métrique est Tj gbj .

Remarque 3.5 . Notre construction dépend d’un choix de jauge : la manière de faire correspondre les infinis des bulles et les voisinages de points singuliers de l’orbifold grâce à ϕt peut être composée avec n’importe quelle isométrie de R4/Γk. Il y a donc deux jauges de recollement, l’échelle tk, et ϕk ∈ Isom( R4/Γk). Ces jauges reviennent simplement à recoller des métriques Ricci-plates ALE différentes. 

Définition 3.6. On définit des coupures χM to et χN tj qui valent 1 respectivement sur les parties isométriques à M to := Mo\Bgo (pk, 2t14 

> k

) et N tj := Nj ∩ Bgbj (pj , t − 14 

> k

)à support dans Mo\Bgo (pk, t 14 

> k

) et N tj := Nj ∩ Bgbj (pj , 2t− 14 

> k

). 

1.2 Coordonnées sur une désingularisation naïve 

La métrique ci-dessus permet d’identifier dans M des régions où la métrique est proche de celle de l’orbifold, de l’ALE ou d’un anneau plat reliant les deux. 

Définition 3.7 (Zones modèles sur un arbre de singularités : Mo(ε), Nj (ε) et 

Ak(t, ε )) . Avec les notation des définitions 2.2 et 2.3, for 0 < ε 6 ε0, on notera — Mo(ε) := Mo\ 

> ( ⋃
> k

Φk(Be(0 , ε )) 

> )

⊂ Mo,

— N (ε) := N \ 

> ( ⋃
> k

Ψk(Be(0 , ε )) ∪ Ψ∞

> (

(R4/Γ∞)\Be(0 , ε −1)))

⊂ Nj ,

— Aj (t, ε ) := Ae

> (

ε−1√

Tj

√tj , ε √

Tj

> )

⊂ R4/Γk.Nous voyons que ces ensembles se plongent naturellement dans notre variété M

grâce à notre construction de désingularisation naïve, et on utilisera la même notation sur M .1. Arbres des singularités et désingularisations naïves 87 

Remarque 3.8 . Mo(ε) N (ε) et Aj (t, ε ) sont les ensembles compacts des orbifolds privés de leurs points singuliers qui apparaissent dans le théorème 2.47. Ils sont de plus exhaustifs lorsque ε tend vers zéro. Nous avons donc un recouvrement de M = Mo#j Nj adapté à une dégénéres-cence à échelles relatives ( tj )j :

M = ⋃

> j
> (

Nj (ε) ∪ Aj (t, ε ))

∪ Mo(ε). (3.1) L’objectif de ce chapitre sera d’identifier chacune de ces régions avec une région d’une métrique d’Einstein proche d’un orbifold au sens de Gromov-Hausdorff. 

1.3 Coordonnées sur une variété d’Einstein 

Le résultat principal de notre première partie est que toute métrique d’Einstein dégénérant (c’est-à-dire s’approchant d’un orbifold d’Einstein au sens de Gromov-Hausdorff) n’est pas seulement décrite par un arbre de singularités au sens de Gromov-Hausdorff, mais a une métrique ε-proche de celle d’une désingularisation naïve dans un sens Ck à poids, voir le théorème 3.42. 

Définition 3.9 (Variété ε-décrite par un arbre de singularités) . Pour ε > 0, et 

l ∈ N, nous dirons qu’une variété riemannienne ( M, g ) est ε-décrite en norme Cl

par une désingularisation naïve de ( Mo, g o), ( M, g Dt ), s’il existe un difféomorphisme Φ : M → M tel que si l’on note Φ( Mo(ε)) =: Mo(ε) ⊂ M , Φ( Nj (ε)) =: Nj (ε) ⊂ M

et Ak(t, ε ) la composante connexe de de M \M o(32 ε) ∪ ⋃ 

> j

Nj (32 ε) ayant une intersection non-vide avec Ψ ∞

> (

Nk(ε)\Be(0 , ε −1))

on ait : 1. sur Mo(ε), 

‖Φ∗g − go‖Cl(go) = ∥∥∥Φ∗g − gD∥∥∥Cl(gD ) 6 ε, 

2. sur la zone Nj (ε), 

> ∥∥∥∥∥

Φ∗gTj

− gbj 

> ∥∥∥∥∥Cl(gbj)

=

> ∥∥∥

Φ∗g − gD∥∥∥Cl(gD ) 6 ε, 

3. et sur Ak(t, ε ), ∫ 

> Ak(t,ε )

| Rm g |2dvg < ε 2.

Proposition 3.10. Sous les hypothèses du théorème 2.47, étant donnée une suite 

(Mi, g i)i de métriques d’Einstein convergeant au sens de Gromov-Hausdorff vers un orbifold d’Einstein (Mo, g o), il existe une désingularisation naïve (Mi, g Dti ) et 88 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

une sous-suite telle que pour tout ε > 0 et l ∈ N, pour i suffisamment grand, la variété (Mi, g i) est ε-décrite par (Mi, g Dti ) en norme Cl.Démonstration. Soit ( Mi, g i)i −−→ 

> GH

(Mo, g o) une suite de variétés satisfaisant les hypothèses du théorème 2.47. Quitte à prendre une sous-suite, pour tout point singulier de Mo, il existe une suite d’échelles Ti > 0 et de points pi de Mi de haute courbure |Rm( gi)|(pi) → ∞ pour lesquels (

Mi, gi 

> Ti

, p i

> )

converge de manière lisse sur les compacts d’un orbifold Ricci-plat ALE ( Nj , g bj , p j ) privé de ses points singuliers. La convergence est de plus lisse à distance uniformément minorée des points singulier d’après les résultats du chapitre 2 car les métriques d’Einstein proches au sens de Gromov-Hausdorff y ont une borne inférieure sur leur rayon harmonique. Soit ε > 0 et l ∈ N, en considérant un compact Nj (ε), il existe ij ∈ N tel que pour tout i > i j , il existe un difféomorphisme sur son image Φ i : Nj (ε) → Mi avec ∥∥∥∥ Φ∗  

> igi
> Tj,i

− gbj

> ∥∥∥∥Cl

6 ε et de même, il existe un rang io à partir duquel les métriques sont Cl-proches sur Mo(ε). Comme la norme L2 de la courbure riemannienne est uniformément bornée d’après [CN15], il n’y a qu’un nombre fini de telles échelles dans chaque arbre de singularités, nous pouvons considérer le maximum les rangs 

ij et io pour obtenir le résultat énoncé. Le contrôle de la norme L2 de la courbure dans les anneaux intermédiaires est prouvée dans le théorème 2.47 du chapitre 2. 

Figure 3.2 – Correspondance entre les zones modèles. 2. Des premières coordonnées dans les anneaux intermédiaires 89 

Remarque 3.11 . L’existence de bonnes coordonnées sur les zones Mo(ε) et Nj (ε)est donc déjà présente dans les théorèmes de [And89, BKN89] raffinés dans [Ban90] qui ont été présentés dans le chapitre 2. L’objectif premier de ce chapitre est de construire des bonnes coordonnées sur les zones Ak(t, ε ). 

# 2 Des premières coordonnées dans les anneaux intermédiaires 

La difficulté principale ici pour la construction de coordonnées (et supplémen-taire par rapport à [BKN89]) est que l’on ne dispose pas d’un comportement asymptotique (à l’infini ou à un point singulier) sur lequel nous pouvons baser notre construction. Nous allons commencer par construire des premiers systèmes de coordonnées locales par ε-régularité. Cela nous aidera ensuite à obtenir un système de coordonnées optimales. 

2.1 Construction des premières coordonnées 

L’objectif de cette section est de prouver la proposition suivante. 

Proposition 3.12. Pour tous δ > 0, D0 > 0, v0 > 0, E > 0 et l ∈ N, il existe 

ε2 > 0 tel que si une variété d’Einstein satisfait : — le diamètre est majoré par D0 > 0,— le volume est minoré par v0 > 0,— la courbure de Ricci est minorée par −3,— il existe un anneau A(ρ1, ρ 2) avec 4ρ1 < ρ 2 satisfaisant : 

> ∫
> A(ρ1,ρ 2)

| Rm |2 6 ε22,

et tel que ∫ 

> B(ρ2)

| Rm |2 6 E (c’est toujours satisfait pour une certaine constante E(v0, D 0) d’après [CN15]), — le rapport des volumes des boules associées est presque euclidien 

> ∣∣∣∣

Vol( B(ρ2)) Vol( B(ε2ρ1)) − ρ42

(ε2ρ1)4 

> ∣∣∣∣

6 ε2.

Alors, pour tout ρ ∈ [

2ρ1, 14 ρ2

> ]

il existe un domaine ˆA(

ρ, 2ρ)

proche de l’anneau 90 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

A(

ρ, 2ρ)

au sens suivant, 

A(

(1 + δ)ρ, (2 − δ)ρ)

⊂ ˆA(

ρ, 2ρ)

⊂ A(

(1 − δ)ρ, (2 + δ)ρ)

,

tel qu’il existe Γ sous-groupe fini de SO (4) et un difféomorphisme 

Φρ : Ae(1 , 2) ⊂ R4/Γ → ˆA(

ρ, 2ρ)

⊂ M, 

pour lesquels on ait : ∥∥∥∥

Φ∗

> ρ

gρ2 − ge

> ∥∥∥∥Cl(Ae(1 ,2))

6 δ. 

Notre situation est non-effondrée à toutes les échelles par une application de l’inégalité de Bishop-Gromov. 

Lemme 3.13. Soit (M, g ) une variété riemannienne de diamètre inférieur à D0 >

0 et de volume supérieur à v0 > 0 et ayant une courbure de Ricci minorée par 

−(n − 1) κ < 0. Alors, pour tout 0 6 r 6 D0, nous avons, 

Vol g(Bg(r)) > Vol g−κ (Bg−κ (r)) Vol g−κ (Bg−κ (D0)) v0

où g−κ est la métrique de l’espace simplement connexe à courbures sectionnelles constantes égales à −κ. En particulier, il existe C = C(κ, D 0, v 0) > 0 telle que l’on ait 

Vol g(Bg(r)) > Cr 4. (3.2) Le rayon d’injectivité est bien contrôlé sur les zones correspondant à l’orbifold et les orbifolds ALE grâce à la proximité avec des métriques modèles du corollaire 2.47. Il est de plus contrôlé dans les zones intermédiaires coniques d’après le lemme suivant. 

Lemme 3.14. Sous les hypothèses de la proposition 3.12, il existe une constante 

r0 > 0 ne dépendant que de D0, v0, telle qu’en tout point de l’anneau A(

2ρ1, 12 ρ2

> )

à distance ρ du centre, le rayon d’injectivité et le rayon harmonique soient minorés par r0ρ.Démonstration. Considérons un point x à distance ρ ∈ [2 ρ1, 12 ρ2] du centre de l’anneau et la boule B(x, ρ 

> 2

). Le volume de B(x, ρ 

> 2

) est minoré grâce à l’inégalité de Bishop-Gromov par C1ρ4 pour une constante C1 ne dépendant que de v0 et 

D0, voir le lemme 3.13. Pour contrôler la courbure, on peut utiliser le théorème d’ ε-régularité de [Gao90], lemme 2.29, voir aussi [And89] et [BKN89]. Ainsi, pour 2. Des premières coordonnées dans les anneaux intermédiaires 91 

ρ ∈ [4 ρ1, 14 ρ2], quitte à réduire la constante ε2 de l’énoncé, alors la norme L2 de la courbure sur la boule B(x, ρ 

> 2

) est plus petite que la constante ε du lemme 2.29. La courbure à distance ρ est donc plus petite que 1 

> ρ2

par le lemme 2.29. Par le théorème 1.43, les contrôles sur la courbure et le volume à l’échelle ρ

impliquent qu’il existe une constante r1 > 0 dépendant du volume de la boule de rayon ρ et d’une borne sur la courbure à cette échelle telle qu’en tout point à distance ρ, le rayon d’injectivité soit minoré par r1ρ. Comme la courbure est bornée, il existe 0 < r 0 < r 1 dépendant de r1 et de la borne sur la courbure telle le rayon harmonique soit minoré par r0.L’outil essentiel pour prouver l’existence des premières coordonnées de la pro-position 3.12 sera le théorème de presque rigidité des cônes de Cheeger et Colding. 

Lemme 3.15 ([CC96, Theorem 4.85]) . Pour tout δ > 0, il existe κ > 0 tel que pour tout r > 0, si (M n, g ) satisfait, Ric( g) > −(n−1) κr −2 et qu’il existe un point 

p ∈ M auquel, 

Vol( B(p, κr )) 

v−κr −2 (κr ) − Vol( B(p, 2r)) 

v−κr −2 (2 r) < κ, 

où v−κr −2 (s) est le volume de la boule de rayon s dans l’espace simplement connexe à courbures sectionnelles constantes égales à −κr −2, alors, il existe un cône mé-trique (C(X), d C(X), 0) tel que diam (X) 6 π et, 

dGH 

> ((

B(p, r ), p )

, (

BC(X)(0 , r ), 0))

6 δr. 

Nous allons avoir besoin d’un raffinement de ce résultat dans notre cas. Pour obtenir une preuve ne se basant pas sur les techniques de [And89, BKN89] et en particulier uniquement basée sur l’étude des anneaux de basse courbure comme dans le second chapitre, nous n’utilisons pas le fait que les limites soient des ALE et orbifolds. 

Lemme 3.16 (Presque cône volumique dans une variété d’Einstein de dimension 4) . Pour tous δ > 0, l ∈ N, v0 > 0, et E > 0, il existe κ > 0 tel que pour tout 

r > 0, si (M 4, g ) satisfait Ric( g) = Λ g avec, |Λ| 6 3κr −2 et qu’il existe un point 

p ∈ M pour lequel, 

Vol( B(p, r )) > v0r4,

Vol( B(p, κr )) 

v−κr −2 (κr ) − Vol( B(2 r)) 

v−κr −2 (2 r) < κ, 92 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

et ∫

> B(p, 2r)

| Rm |2dv 6 E, 

alors, il existe un sous-groupe fini Γ ⊂ SO (4) (dont le cardinal est majoré par une fonction de v0), et un difféomorphisme Φ : Ae(δ, (1 − δ)) → ˆA(δr, (1 − δ)r), où, 

A(2 δr, (1 − 2δ)r) ⊂ ˆA(δr, (1 − δ)r) ⊂ A 

> (

12δr, 

> (

1 − 12δ

> )

r

> )

, (3.3) 

tel que sur l’anneau Ae(δr, (1 − δ)r), on ait : 

> ∥∥∥∥

Φ∗gr2 − ge

> ∥∥∥∥Cl(ge)

6 δ. (3.4) 

Remarque 3.17 . Les hypothèses sur la courbure et sur le volume ne sont présentes que pour majorer le cardinal du groupe Γ pour avoir compacité. On évite ainsi les suites de variétés d’Einstein proches de cônes R4/Γi où le cardinal de Γ i diverge. Dans une telle situation, la suite convergerait vers le cône R+. Ces hypothèses sur le volume et la courbure sont de plus redondantes ici, par la dernière section de [CN15]. 

Démonstration. Par changement d’échelle on se ramène à r = 1. Prouvons ce résultat par contradiction en supposant qu’il existe δ > 0, E > 0 et v0 > 0, et une suite de contre-exemples ( M 4 

> i

, g i, p i)i satisfaisant : — Vol( Bi(pi, 1)) > v 0 > 0, — ∫ 

> Bi(pi,2)

| Rm i |2dvi 6 E,— il existe κi → 0 et Λ i, |Λi| 6 3κi pour lesquels Ric( gi) = Λ igi et Vol( Bi(pi,κ i))   

> v−κi(κi)

−  

> Vol( Bi(pi,2))
> v−κi(2)

< κ i,mais pour laquelle, quel que soit Γ sous-groupe fini de SO (4), il n’existe pas de difféomorphisme Φ : Ae(δ, (1 − δ)) → ˆA(δ, (1 − δ)) où ˆA(δ, (1 − δ)) satisfait (3.3), et tel qu’on ait le contrôle (3.4). Daprès le théorème 0.1, comme Vol( Bi(pi, 1)) > v 0 > 0 et Ric( gi) > −3, une sous-suite des boules de rayon 1 pointées converge au sens de Gromov-Hausdorff vers un espace métrique que l’on notera ( Y, d Y , p ). Par le lemme 3.15, quitte à reprendre une sous-suite, pour tout i, on peut supposer que κi est suffisamment petit pour que l’on ait 

dGH 

> ((

Bi(p, 1) , p i

> )

, (

BC(Xi)(0 , 1) , 0))

6 1

i ,

pour un certain cône métrique ( C(Xi), d C(Xi), 0) tel que diamX i 6 π. Par in-2. Des premières coordonnées dans les anneaux intermédiaires 93 égalité triangulaire, la suite (

BC(Xi)i (0 , 1) , 0)

converge aussi vers ( Y, d Y , p ) au sens de Gromov-Hausdorff. Maintenant, comme les C(Xi) munis des distances 

dC(Xi)

> (

(r, x ), (s, y ))

:= 

> √

r2 + s2 − 2rs cos( dXi (x, y )) dGH -convergent, on en dé-duit en fixant r > 0 et s > 0 que les ( Xi, d Xi ) dGH -convergent vers ( X, d X ), et donc que la limite est un cône métrique, ( Y, d Y , p ) = ( C(X), d C(X), 0). Par la proposition 2.30, nous savons que la limite ( Y, d Y , p ) privée d’un nombre fini de points singuliers est une métrique d’Einstein lisse et que la convergence est lisse sur les compacts. La limite de ( Bi(pi, 1) , g i, p i) au sens de Gromov-Hausdorff est donc à la fois la boule de rayon 1 d’un cône métrique et une variété d’Einstein de dimension 4 hors d’un nombre fini de points singulier. Un cône n’ayant qu’un nombre fini de points singuliers est un cône sur une variété lisse. De plus un cône d’Einstein est nécessairement Ricci-plat car la cour-bure de Ricci d’un cône s’annule dans la direction radiale. La limite est donc un cône sur une variété d’Einstein lisse de dimension 3 et de constante d’Einstein 2. C’est donc un quotient de S3 par un sous-groupe Γ ⊂ SO (4) car en dimension 3, les métriques d’Einstein sont à courbures sectionnelles constantes par (1.18). Il existe donc un difféomorphisme Φ : Ae(δ, (1 − δ)) → ˆA(δr, (1 − δ)r) satisfaisant (3.3) et (3.4), ce qui est absurde. On peut donc maintenant utiliser ces résultats pour construire des premières coordonnées dans les zones intermédiaires. 

Preuve de la proposition 3.12. Soient δ > 0, D0 > 0, v0 > 0, E > 0, Λ ∈ [−3, 3] et l ∈ N, et une variété de dimension 4, ( M, g ) satisfaisant : — Ric( g) = Λ g,— le diamètre est majoré par D0 > 0, — le volume est minoré par v0 > 0, — il existe p ∈ M , et ρ2 > 0, tels qu’on ait : ∫ 

> B(p,ρ 2)

| Rm |2 6 E.94 Chapitre 3. De Gromov-Hausdorff à C∞ à poids Remarquons que ces hypothèses impliquent une borne sur Λ ρ22

E >

∫

> B(ρ2)

| Rm |2dv

> 6

∫

> B(ρ2)

| Ric |2dv

> 24Λ 2 Vol( B(ρ2)) 

> 24 v0Λ2 Vol g−| Λ| (Bg−| Λ| (ρ2)) Vol g−| Λ| (Bg−| Λ| (D0)) 

> 24 v0Λ2 Vol g−3 (Bg−3 (ρ2)) Vol g−3 (Bg−3 (D0)) 

> C(D0, v 0)Λ 2ρ42, (3.5) puis Λ ρ22 6 E1/2 

> C(D0,v 0)1/2

=: C′(E, D 0, v 0). Soit l ∈ N, et notons 0 < κ 0 < 14 la constante du lemme précédent associée à nos constantes δ, l et E. Cherchons ε2 > 0 suffisamment petit pour satisfaire les hypothèses du lemme 3.16 avec la constante κ0 > 0. Pour tous 0 < 4ρ1 6 ρ2 pour lesquels on a : 

∫

> A(ρ1,ρ 2)

| Rm |2 6 ε22,

et ∣∣∣∣

Vol( B(ρ2)) Vol( B(ε2ρ1)) − ρ42

(ε2ρ1)4

∣∣∣∣ 6 ε2,

nous avons en fait, par l’inégalité de Bishop-Gromov, pour C′′ (E, D 0, v 0) > 0, 

∣∣∣∣

Vol( B(ρ2)) Vol( B(ρ1)) − ρ42

ρ41

∣∣∣∣ 6 C′′ (E, D 0, v 0)ε2, (3.6) et pour tout ρ et κ0 > 0 pour lesquels ρ1 < κ 0ρ < 2ρ < ρ 2,

∣∣∣∣

Vol( B(2 ρ)) Vol( B(κ0ρ)) − (2 ρ)4

(κ0ρ)4

∣∣∣∣ 6 C′′ (E, D 0, v 0)ε2. (3.7) Nous pouvons donc supposer en choisissant ε2 assez petit que Vol( A(ρ1, ρ 2)) >

c(E, D 0, v 0)ρ42 pour 4 ρ1 < ρ 2 pour c(E, D 0, v 0) > 0. Cherchons donc à obtenir une meilleure borne sur Λ pour être sous les hypothèses du lemme 3.16. Comme 2. Des premières coordonnées dans les anneaux intermédiaires 95 Ric = Λ g, on a 

ε22 >

> ∫
> A(ρ1,ρ 2)

| Rm |2dv

> 6

> ∫
> A(ρ1,ρ 2)

| Ric |2dv

> 24Λ 2 Vol( A(ρ1, ρ 2)) 

> 24 c(E, D 0, v 0)Λ 2ρ42

et nous avons donc |Λ| 6 ε2(24 c(E, D 0, v 0)) −1/2ρ−22 . Ainsi, pour ε2 assez petit, nous sommes donc sous les hypothèses du lemme 3.16 pour tout ρ en choisissant 

ε2 pour lequel on ait 

κ0 = ε2 max((24 c(E, D 0, v 0)) −1/2, 1, C ′′ (E, D 0, v 0)) ,

car nous contrôlons la croissance du volume entre κ0ρ et 2 ρ à l’aide de (3.7). La conclusion de la proposition 3.12 est donc satisfaite pour tout ρ1 < ρ < 14 ρ2 avec 

δ(κ0) > 0. 

2.2 Utilité de ces premières coordonnées 

Le difféomorphisme de la proposition 3.12 nous permet de tirer notre géométrie en arrière sur des anneaux plats où la métrique d’Einstein g est C∞-proche de la métrique plate ge.Nous allons utiliser cette proximité pour construire et contrôler des hypersur-faces proches d’être à seconde forme fondamentale constante pour la métrique d’Einstein. Les lemmes suivants concernent les métriques proches de la métrique plate sur Ae  

> (14

, 4)

, et impliqueront directement les résultats sur A(14 ρ, 4ρ) pour 

ρ > 0 par changement d’échelle. 

Note 3.18. Ici et dans la suite, on prend la convention de considérer des normales 

sortantes . Pour une hypersurface Σ de normale sortante N Σ, on définit la seconde forme fondamentale par AΣ(X, Y ) := 〈X, ∇Y N Σ〉, qui nous assure que les sphères dans l’espace euclidien sont à seconde forme fondamentale positive. 

Lemme 3.19. Pour tout l ∈ N, il existe C > 0 et δ0 > 0 tels que si une métrique 

g sur Ae  

> (14

, 4)

satisfait, 

‖g − ge‖Cl+1 (Ae( 14 ,4)) 6 δ0,96 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

on ait, pour tout s ∈ [ 14 , 4]

, en notant Ss la sphère de rayon s de Rn/Γ, Ss a une seconde forme fondamentale pour g, ASs 

> g

qui satisfait, 

∥∥∥∥

ASs

> g

s − gSs

s2

∥∥∥∥Cl( gSss2 )

6 C‖g − ge‖Cl+1 (Ae( 14 ,4)) ,

et de plus, on a, 

∥∥∥∥

gSs

s2 − gSn−1/Γ

∥∥∥∥Cl+1 (gSn−1/Γ)

6 C‖g − ge‖Cl+1 (Ae( 14 ,4)) .

Démonstration. Il suffit de remarquer que la seconde forme fondamentale fait in-tervenir une dérivée de la métrique qui est contrôlée par hypothèse. Comme pour 

ge, les hypersurfaces Ss ont une seconde forme fondamentale constante égale à  

> gSn−1/Γ
> s

, on en déduit le résultat. Étant donnée une hypersurface orientable et lisse Σ, on définit son rayon d’in-jectivité normale , inj ⊥ 

> g

(Σ) comme le supremum des r > 0 tels que l’application 

F g : Σ × [−r, r ] → M définie par F g(x, s ) := γgx(s), où γgx est la géodésique pour g

telle que γgx(0) = x, et γ′gx(0) est la normale sortante à Σ, soit un difféomorphisme sur son image. 

Lemme 3.20. Pour tout l ∈ N et ε > 0, il existe C > 0 et δ > 0 tel que si une métrique g satisfait : 

‖g − ge‖Cl+2 (Ae( 14 ,4)) 6 δ, 

et si une hypersurface Σ ⊂ Ae

( 12 , 2)

satisfait ‖AΣ 

> ge

‖Cl+1 6 10 , alors, on ait les deux propriétés suivantes concernant les perturbations normales d’hypersurfaces : — les rayons d’injectivité normale de Σ pour g et ge, inj ⊥ 

> g

(Σ) , et inj ⊥ 

> ge

(Σ) 

satisfont ∣∣∣∣

inj ⊥ 

> g

(Σ) inj ⊥ 

> ge

(Σ) − 1

∣∣∣∣ 6 ε. 

— les deux applications exponentielles normales sont proches l’une de l’autre sur Σ × [

− (1 − ε)inj ⊥ 

> ge

(Σ) , (1 − ε)inj ⊥ 

> ge

(Σ) ]

: il existe un champ de vecteurs 

X sur Rn/Γ, ‖X‖Cl+1 (ge) < ε , pour lequel on a, 

F g ◦ (F ge )−1 = ϕX ,

où ϕX : p 7 → exp ge 

> p

(X(p)) .Démonstration. Les courbes F g(x, . ) = γgx(.) et F ge (x, . ) = γge 

> x

(.) sont respective-2. Des premières coordonnées dans les anneaux intermédiaires 97 ment les solutions des équations des géodésiques pour g et ge,

> 

∇γ′ 

> x

γ′ 

> x

= 0 ,γx(0) = x, γ′

> x

(0) = Nx.

(3.8) où N gx et N ge 

> x

sont les normales sortantes à Σ pour les deux métriques. Par hy-pothèse, les métriques g et ge sont Cl+2 -proches. Cela implique que les Nx sont 

Cl+2 -proches, et que ∇g et ∇ge sont Cl+1 -proches. Par continuité par rapport aux conditions initiales et aux paramètres des so-lutions d’équations différentielles d’ordre 2, on en déduit qu’étant donnée une hypersurface Σ fixée, pour tout ε > 0, il existe δ > 0 tel que si la différence entre les deux métriques est plus petite que δ en norme Cl+2 , alors la différence entre les géodésiques normales est petite en norme Cl dans le sens suivant : il existe un champ de vecteurs X défini le long de chaque γge 

> x

tel que 

γgx(s) = ϕX (γge 

> x

(s)) := exp γge x (s)

> (

X(γge 

> x

(s)) )

.

Par continuité par rapport aux conditions initiales et aux paramètres, vu comme comme champ de vecteurs sur Rn/Γ, nous avons ‖X‖Cl+1 (ge) < ε . L’égalité γgx(s) = 

ϕX (γge 

> x

(s)) se réécrit : 

F g = ϕX ◦ F ge .

On en déduit en particulier que si une hypersurface Σ ′ est une petite pertur-bation normale de Σ pour la métrique g, alors c’est aussi une petite perturbation normale de Σ pour la métrique ge, et inversement. 

Corollaire 3.21. Pour tout ε0 > 0 et l ∈ N, il existe C > 0 et δ0 > 0, tels que pour toute métrique g satisfaisant, 

‖g − ge‖Cl+2 (Ae( 14 ,4)) 6 δ0,

et pour toute hypersurface Σ ⊂ Ae  

> (12

, 2)

telle que ‖AΣ 

> ge

‖Cl+1 6 10 , on ait : pour toute fonction w : Σ → R telle que ‖w‖Cl 6 ε0, et en notant Σ( w) := 

{F (x, w (x)) , x ∈ Σ},1. il existe w′ : Σ → R telle que ‖w′‖Cl 6 2ε0 telle que 

Σge (w) = Σ g(w′),98 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

2. il existe w′′ : Σ → R telle que ‖w′′ ‖Cl 6 2ε0 telle que 

Σg(w) = Σ ge (w′′ ).

Démonstration. D’après le lemme 3.20 précédent, on a F g = ϕX ◦ F ge , pour X

arbitrairement petit en norme Cl+1 en fonction de δ0. En ajoutant l’hypothèse que 

‖AΣ 

> ge

‖Cl+1 6 10, on s’assure du fait que qu’il existe ε0 tel que sur Σ × [−2ε0, 2ε0], les métriques ( F ge )∗ge et gp := ( ge)|Σ + ds 2 soient arbitrairement proches en norme 

Cl. Cela implique que [

(F ge )−1 ◦ ϕX ◦ F ge

]

= ϕeXe ,

où Xe est le tiré en arrière de X par F ge , et ϕeXe (p) := exp ge 

> p

(Xe(p)). On a donc 

‖Xe‖Cl+1 (ge) 6 ε0. Par la proximité des métriques ( F ge )∗ge et gp, ϕeXe = ( ϕΣ

> Xp
> Σ

, ϕ R

> Xp
> R

), où ‖Xp

> Σ

‖Cl(gΣ) + ‖Xp

> R

‖Cl(ds 2) 6 2ε0.Maintenant, pour tout ( x, s ) ∈ Σ × [−2ε0, 2ε0], nous avons 

F g(x, s ) = F ge ◦

[

(F ge )−1 ◦ ϕX ◦ F ge

]

(x, s ),

= F ge ◦ (ϕΣ

> Xp
> Σ

, ϕ R

> Xp
> R

)( x, s )= F ge

(

ϕΣ

> Xp
> Σ

(x), ϕ R

> Xp
> R

(s))

En particulier, pour tout w : Σ → [−2ε0, 2ε0], nous avons 

F g(x, w (x)) = (

ϕΣ

> Xp
> Σ

(x), w ′(ϕΣ

> Xp
> Σ

(x)) )

,

où w′ := ϕR

> Xp
> R

◦ w ◦ (

ϕΣ

> Xp
> Σ

)−1

. Par les contrôles de Xp 

> R

et Xp 

> Σ

que l’on peut supposer arbitrairement petits quitte à prendre δ0 plus petit, on en déduit le résultat. 

# 3 Contrôle des hypersurfaces à courbure moyenne constante dans les zones de basse courbure 

Expliquons pourquoi les hypersurfaces à courbure moyenne constante sont in-téressantes et bien contrôlées dans notre situation. On contrôle à la fois la manière dont elles sont plongées dans M et leur géométrie intrinsèque à l’aide de la cour-bure ambiante. 3. Contrôle des hypersurfaces CMC 99 

Note 3.22. Tout au long de cette partie, nous noterons les hypersurfaces à cour-bure moyenne constante avec un tilde pour insister sur leur particularité. 

Définition 3.23 (Espaces de Hölder) . Les normes Ck,α seront toujours prises à l’échelle du rayon d’injectivité. C’est-à-dire que l’on définit la norme Ck,α d’une fonction f de la manière suivante : 

‖f ‖Ck,α := ‖f ‖C0 + ... + ‖∇ kg f ‖C0 + [ ∇kg f ]α,

où [h]α = sup 

> {(x,y )|d(x,y )<inj }
> ∣∣∣∣

h(x) − h(y)

d(x, y )α

> ∣∣∣∣g

.

Le but de cette section est la proposition suivante. 

Proposition 3.24. Pour tout k ∈ N et 0 < α < 1, il existe ε > 0 et C = C(k, α ) >

0 pour lesquels, si ˜Σ est une hypersurface d’une variété (M n, g ) satisfaisant : 1. sa courbure moyenne est constante égale à n − 1,2. il existe Γ un sous-groupe fini de SO (n), et un difféomorphisme Φ : Sn−1/

Γ → ˜Σ tels qu’on ait : 

> ∥∥∥

Φ∗g ˜Σ − gSn−1/Γ∥∥∥C1,α (Sn−1/Γ) 6 ε. 

3. la courbure ambiante est basse : sur ˜Σ, 

> ∥∥∥

Rm( g)∥∥∥Ck (g) 6 ε, 

alors : — la seconde forme fondamentale est presque constante à l’échelle de la cour-bure dans un sens fort, 

> ∥∥∥

A˜Σ − g ˜Σ∥∥∥Ck,α 6 C∥∥∥ Rm( g)∥∥∥Ck (g),

— il existe un difféomorphisme Ψ : Sn−1/Γ → ˜Σ tel que, 

> ∥∥∥

Ψ∗g ˜Σ − gSn−1/Γ∥∥∥Ck+1 ,α (Sn−1/Γ) 6 C∥∥∥ Rm( g)∥∥∥Ck (g).

Précisons les notations que nous emploierons dans cette partie : — ∇˜Σ : la connexion de Levi-Civita de l’hypersurface, — ∇ : la connexion de Levi-Civita de l’espace ambiant, 100 Chapitre 3. De Gromov-Hausdorff à C∞ à poids — N ˜Σ : la normale sortante à l’hypersurface, — A˜Σ(X, Y ) : la seconde forme fondamentale de l’hypersurface qui sera vue soit comme un 2-tenseur de l’espace tangent à ˜Σ, — H ˜Σ : la courbure moyenne de l’hypersurface, — pour B un 2-tenseur symétrique sur ˜Σ, on définit : (d∇˜Σ

B)( X, Y ) := ∇˜Σ 

> X

B(Y, . ) − ∇ ˜Σ 

> Y

B(X, . ).

— on notera δ∇˜Σ

l’adjoint formel de d∇˜Σ

.

Équations satisfaites par la seconde forme fondamentale d’une hyper-surface en terme de la courbure ambiante. Lemme 3.25. On a les formules suivantes pour la seconde forme fondamentale d’une hypersurface Σ quelconque : pour tous champs de vecteurs X, Y, Z sur Σ,

d∇Σ

AΣ(X, Y, Z ) = g(

Rm( X, Y )N Σ, Z )

,

et 

δ∇Σ

AΣ(X) = Ric (

N Σ, X )

− dH Σ(X).

Démonstration. La première égalité est connue sous le nom de formule de Codazzi-Mainardi, voir [Pet98, Chapter 4, Theorem 4]. Montrons la seconde égalité. Rappelons notre convention de considérer la nor-male sortante N Σ pour définir la seconde forme fondamentale par AΣ(X, Y ) := 

〈X, ∇Y N Σ〉. Considérons ( ei)i une base orthonormée sur l’espace tangent à l’hy-persurface, et X un champ de vecteurs. Fixons un point de l’hypersurface Σ auquel nous supposerons, sans perte de généralité (car nous manipulons des tenseurs) que les dérivées des champs de vecteurs ei s’annulent. Nous avons (δ∇Σ

AΣ)( X) = −

> n−1∑
> i=1

∇Σ 

> ei

(AΣ(ei, X )) = −

> n−1∑
> i=1
> 〈

ei, ∇Σ 

> ei

∇X N Σ〉

= −

> n−1∑
> i=1
> 〈

ei, ∇ei ∇X N Σ〉

,

car la différence entre les connexions est orthogonale à l’hypersurface. 3. Contrôle des hypersurfaces CMC 101 On a d’autre part HΣ = ∑n−1

> i=1
> 〈

ei, ∇ei N Σ〉

et donc : 

dH Σ(X) = d 

> (n−1∑
> i=1
> 〈

ei, ∇ei N Σ〉)

(X)=

> n−1∑
> i=1
> 〈

ei, ∇X ∇ei N Σ〉

.

Étant donné que ( e1, ..., e n−1, N Σ) forme une base orthonormée, et comme pour toute extension N du champ de vecteurs N Σ à l’espace ambiant, la quantité 

> 〈

N, ∇N ∇X N − ∇ X ∇N N − ∇ [N,X ]

> 〉

s’annule par symétries de la courbure riemannienne, on a : 

> n−1∑
> i=1
> 〈

ei, ∇X ∇ei N Σ − ∇ ei ∇X N Σ〉

= Ric( X, N Σ),

on a donc le résultat énoncé. 

Contrôle de la seconde forme fondamentale par estimations elliptiques. 

On en déduit donc les égalités suivantes dans notre cas à courbure moyenne constante, pour A˜Σ la seconde forme fondamentale vue comme un 2-tenseur, 

d∇˜Σ

A˜Σ(X, Y, Z ) = g(

Rm( X, Y )N ˜Σ, Z )

,

et 

δ∇˜Σ

A˜Σ(X) = Ric (

N ˜Σ, X )

.

En notant A˜Σ0 la partie sans trace de A˜Σ pour g ˜Σ, on a même 

d∇˜Σ

A˜Σ0 (X, Y, Z ) = g(

Rm( X, Y )N ˜Σ, Z )

,

et 

δ∇˜Σ

A˜Σ0 (X) = Ric (

N ˜Σ, X )

.

Les seconds membres étant bien contrôlés par la courbure ambiante, on espère avoir un contrôle de A˜Σ0 en remarquant que l’opérateur d∇˜Σ

+ δ∇˜Σ

est elliptique et inversible. C’est l’objet des lemmes suivants. 

Lemme 3.26. L’opérateur d∇˜Σ

+ δ∇˜Σ

agissant sur les 2-tenseurs symétriques sur 

˜Σ est elliptique. De plus, pour toute métrique g sur Sn−1 suffisamment proche en 102 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

norme C0 de la métrique ronde gSn−1

, d∇Sn−1

+ δ∇Sn−1

est injectif sur l’ensemble des tenseurs ayant une trace nulle pour g.Démonstration. Le symbole de cet opérateur appliqué à ξ ∈ T ∗ ˜Σ est la somme du produit extérieur par ξ et du produit intérieur par le champ de vecteurs associé à ξ

par la métrique. Le noyau du premier est l’ensemble des formes proportionnelles à ξ

et pour le second celles qui sont orthogonales. Le noyau du symbole de l’opérateur 

d∇˜Σ

+ δ∇˜Σ

est donc nul et l’opérateur est elliptique. D’après [Bes87, 12.69], le laplacien associé : − ˆ∆˜Σ := δ∇˜Σ

d∇˜Σ

+ d∇˜Σ

δ∇˜Σ

a la forme suivante pour h un 2-tenseur symétrique, 

− ˆ∆˜Σh = ( ∇˜Σ)∗∇˜Σh − ˚R˜Σ

h + h ◦ Ric ˜Σ,

où ˚R( h) est l’action de la courbure sur les 2-tenseurs symétriques : pour ( ei)i une base orthonormée, ˚R( h)( X, Y ) = ∑

> i

h(

Rm( ei, X )Y, e i

)

,

en coordonnées, cela s’écrit ˚R( h)ij := Rm iklj hmn gkm gln . Sur la sphère unité de dimension n − 1, où l’on a Rm Sn−1 

> iklj

= gij gkl − gil gkj , et donc ˚RSn−1

(h)ij = tr (h)gij −

hij , et α ◦ Ric Sn−1

= ( n − 2) α. Ainsi, on obtient : 

− ˆ∆Sn−1

h = ( ∇Sn−1

)∗∇Sn−1

h + ( n − 1) h − tr (h)Id . (3.9) Soit h0 un 2-tenseur C1,α symétrique à trace nulle pour gSn−1

dans le noyau de l’opérateur. La trace de h0 est nulle, et donc d’après (3.9), nous avons (∇Sn−1

)∗∇Sn−1

h0 + ( n − 1) h0 = 0 .

En prenant le produit scalaire L2 avec h0, on obtient 

‖∇ Sn−1

h0‖2 

> L2

+ ( n − 1) ‖h0‖2 

> L2

= 0 , (3.10) et enfin h0 = 0. L’opérateur d∇Sn−1

+ δ∇Sn−1

est donc injectif sur les tenseurs sans trace pour gSn−1

.Considérons maintenant une métrique g proche de gSn−1

: il existe ε > 0 que 3. Contrôle des hypersurfaces CMC 103 l’on choisira suffisamment petit a posteriori tel que, 

‖g − gSn−1

‖C0 6 ε. 

On veut montrer que l’opérateur d∇Sn−1

+δ∇Sn−1

est aussi inversible sur les tenseurs à trace nulle pour g. Soit donc h un 2-tenseur de trace nulle pour g. Par proximité des métriques, pour ε assez petit, il existe C = C(n) telle que : 

|tr Sn−1

h|Sn−1 6 Cε |h|Sn−1 . (3.11) On a toujours 

− ˆ∆Sn−1

h = ( ∇Sn−1

)∗∇Sn−1

h + ( n − 1) h − tr Sn−1

(h)Id ,

et donc, grâce à (3.11), si (

d∇Sn−1

+ δ∇Sn−1 )

h = 0, alors 0 > ‖∇ Sn−1

h‖2 + ( n − 1 − Cε )‖h‖2,

et donc h = 0 si ε est assez petit pour avoir n − 1 > Cε . On en déduit que 

d∇Sn−1

+ δ∇Sn−1

est injectif sur les tenseurs de trace nulle pour g.

Corollaire 3.27. Il existe ε > 0 tel que si Σ est une hypersurface d’une variété 

(M n, g ) pour laquelle il existe Γ un sous-groupe fini de SO (n), et un difféomor-phisme Φ : Sn−1/Γ → ˜Σ tel que l’on ait 

∥∥∥Φ∗g ˜Σ − gSn−1/Γ∥∥∥W l+1 ,p (Sn−1/Γ) 6 ε. 

Alors, pour tout 1 6 p < +∞ et l ∈ N, il existe C > 0 tel que pour tout 

2-tenseur symétrique u sur ˜Σ de trace nulle pour g ˜Σ, on ait, 

‖u‖W l+1 ,p 6 C

(∥∥∥δ∇˜Σ

u∥∥∥W l,p + ∥∥∥d∇˜Σ

u∥∥∥W l,p 

)

.

Démonstration. Nous avons le contrôle suivant sur la différence avec l’opérateur sur la sphère : pour tout p > 1, il existe une constante C > 0 telle que pour tout 2-tenseur de classe W l+1 ,p , u on ait : 

∥∥∥∥Φ∗(

d∇˜Σ

+ δ∇˜Σ )

u − (

d∇Sn−1

+ δ∇Sn−1 )

u

∥∥∥∥W l,p 

6 Cε ‖u‖W l+1 ,p .

La conclusion vient alors des estimations elliptiques pour les opérateurs Fred-holm injectifs du lemme 1.60 énoncé dans le premier chapitre. 104 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

Démonstration de la proposition 3.24. Soit 0 < α < 1, et p > n 

> 1−α

. Alors, W 1,p 

s’injecte continûment dans Cα, c’est-à-dire qu’il existe C1 = C1(p, α, n ) > 0 tel que pour tout 2-tenseur u, on ait : 

‖u‖Cα 6 C1‖u‖W 1,p .

Définissons les opérateurs, P := δ∇Sn−1

+ d∇Sn−1

et P ′ := Φ ∗(

δ∇˜Σ

+ d∇˜Σ )

qui agissent entre les espaces de Banach W 1,p et Lp. D’après le lemme 3.26, P

est injectif sur les 2-tenseurs sans trace. Grâce à l’expression du lemme 3.25 de l’opérateur δ∇˜Σ

+ d∇˜Σ

appliqué à A˜Σ0 et en considérant tous les opérateurs par rapport à g on a par le corollaire 3.27 : 

∥∥∥A˜Σ0

∥∥∥W 1,p 6 C

(∥∥∥δ∇˜Σ

A˜Σ0

∥∥∥Lp + ∥∥∥d∇˜Σ

A˜Σ0

∥∥∥Lp

)

= C (∥ ∥∥ Rm( ., . )N ˜Σ∥∥∥Lp + ∥∥∥ Ric( N ˜Σ)∥∥∥Lp

)

.

Comme l’hypersurface a un volume majoré (proche de celui de Sn−1/Γ), il existe de plus C2 = C2(p, n ) > 0 telle que l’on ait : 

‖ Ric( N ˜Σ)‖Lp 6 C2‖ Rm( ., . )N ˜Σ‖C0 ,

et 

‖ Rm( ., . )N ˜Σ‖Lp 6 C2‖ Rm( ., . )N ˜Σ‖C0 .

Par injection de W 1,p dans Cα, on en déduit que 

‖A˜Σ0 ‖Cα 6 2C1C2C‖ Rm( ., . )N ˜Σ‖C0 ,

qui est le résultat énoncé pour k = 0. Expliquons maintenant comment obtenir des estimations d’ordre supérieur par récurrence. Supposons donc que pour l ∈ N, on ait les contrôles suivants sur l’hypersurface ˜Σ : il existe C > 0 telle que, 1. ∥∥∥ Rm( g)∥∥∥Cl+1 (g) 6 ε,2. 

∥∥∥A˜Σ − g ˜Σ∥∥∥Cl,α 6 C

∥∥∥ Rm( g)

∥∥∥Cl(g),3. il existe un difféomorphisme Ψ : Sn−1/Γ → ˜Σ tel qu’on ait 

∥∥∥Ψ∗g ˜Σ − gSn−1/Γ∥∥∥Cl+1 ,α (Sn−1/Γ) 6 C∥∥∥ Rm( g)∥∥∥Cl(g).3. Contrôle des hypersurfaces CMC 105 En notant Rm ˜Σ la courbure riemannienne de ˜Σ, l’équation de Gauss pour la cour-bure s’écrit : 

g(Rm ˜Σ(X, Y )Z, W ) = g(Rm( X, Y )Z, W )+ A˜Σ(X, Z )A˜Σ(Y, W ) − A˜Σ(Y, Z )A˜Σ(X, W ).

Les contrôles 1 et 2 impliquent donc qu’il existe C = C(α, l, n ) > 0 telle que l’on ait ∥∥∥ Ric( g ˜Σ) − (n − 1) g ˜Σ∥∥∥Cl,α 6 C∥∥∥ Rm( g)∥∥∥Cl+1 (g),

et grâce à la proposition 1.62 du chapitre 1. 

Proposition 3.28 (Proposition 1.62) . Soit (M, g 0) une variété à courbures sec-tionnelles constantes égales à 1, et k ∈ N. Alors, il existe δ > 0 et C > 0, tels que si une métrique g sur M satisfait : 

‖g − g0‖Ck+1 ,α 6 δ

alors, il existe un difféomorphisme Φ : M → M , pour lequel on a si k > 1,

‖Φ∗g − g0‖Ck+1 ,α 6 C∥∥∥ Ric( g) − (n − 1) g∥∥∥Ck−1,α ,

ou bien, si k = 0 ,

‖Φ∗g − g0‖C1,α 6 C∥∥∥ Ric( g) − (n − 1) g∥∥∥C0 .

On en déduit donc dans notre cas qu’il existe un difféomorphisme ˜Ψ˜Σ : Sn−1/

Γ → ˜Σ tel qu’on ait 

∥∥∥ ˜Ψ∗

> ˜Σ

g ˜Σ − gSn−1/Γ∥∥∥Cl+2 ,α (Sn−1/Γ) 6 C∥∥∥ Rm( g)∥∥∥Cl+1 (g).

Ce dernier contrôle combiné aux contrôles en norme Cl+1 sur la courbure im-plique par régularité elliptique (comme dans la preuve avec k = 0) qu’il existe une constante C′ = C′(l + 1 , α, n ) > 0 pour laquelle on ait 

∥∥∥A˜Σ − g ˜Σ∥∥∥Cl+1 ,α 6 C′∥∥∥ Rm( g)∥∥∥Cl+1 (g).106 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

# 4 Perturbation d’hypersurfaces à seconde forme fondamentale presque constante 

Durant toute la construction on se ramènera toujours au cas où la courbure moyenne de l’hypersurface a une valeur moyenne égale à n − 1 par changement d’échelle. Montrons comment il est possible de perturber une hypersurface à se-conde forme fondamentale presque constante dans une zone à basse courbure en une hypersurface à courbure moyenne constante. 

Proposition 3.29. Pour tout 0 < r 0 < 16 et S0 > 0, il existe C > 0 et 0 < ε < r0

> C

tels que pour toute hypersurface Σ difféomorphe à Sn−1/Γ, pour Γ 6 = {Id } de volume minoré par S0, d’une variété (M, g ) satisfaisant : 1. le rayon d’injectivité normale de Σ et le rayon d’injectivité des points de Σ

dans M sont minorés par 3r0,2. ∥∥∥AΣ − gΣ∥∥∥Cα 6 ε,3. sur l’anneau {x, d Mg (x, Σ) < 3r0}, on a ∥∥∥ Rm( g)∥∥∥C4(g) < ε ,Alors, il existe une unique fonction w satisfaisant ‖w‖C2,α 6 Cε et telle que l’on ait 

HΣ( w) ≡ n − 1,

où l’on a noté Σ( w) := {γx(w(x)) , x ∈ Σ}, où γx est la géodésique telle que 

γx(0) = x, et γ′

> x

(0) est la normale unitaire sortante à Σ. On a de plus le contrôle suivant, 

‖w‖C2,α 6 C

> ∥∥∥

HΣ − (n − 1)  

> ∥∥∥Cα

.

Remarque 3.30 . Rappelons que l’on a défini les normes de Hölder à l’échelle du rayon d’injectivité, voir la définition 3.23. Dans nos applications, les contrôles sur le rayon d’injectivité seront des conséquences du lemme 3.14, et les différents contrôles de la courbure, de la partie précédente. En général, la construction de sphères à courbure moyenne constante est déli-cate (voir par exemple [Ye96, PX09]) car elle passe par la construction d’un inverse à droite pour l’opérateur ∆ Sn−1 + ( n − 1) (où ∆ Sn−1 est l’opérateur de Laplace-Beltrami avec des valeurs propres négatives) qui n’est pas inversible. Cependant, dans notre cas, nos hypersurfaces ne sont pas difféomorphes à Sn−1, mais à Sn−1/

Γ pour Γ 6 = {Id }. La différence que cela induit est que −(n − 1) n’est plus une valeur propre du laplacien. En effet, les fonctions propres associées à la valeur propre −(n − 1) sont les restrictions de fonctions linéaires sur Rn à la sphère. 4. Perturbation de presque sphères 107 Cette différence rend la construction beaucoup plus simple dans notre cas (voir aussi [CEV17] pour la même remarque dans le cas des variétés asymptotiquement coniques). 

Remarque 3.31 . Géométriquement, cela vient du fait qu’étant donnée Sn−1 ⊂ Rn,les simples translations de la sphères sont des perturbations à courbure moyenne constante. Dans le cas de Sn−1/Γ ⊂ Rn/Γ, ce n’est plus le cas, le centre est fixé car il est distingué comme point fixe de l’action du groupe Γ. 

Coordonnées géodésiques normales. Construisons pour commencer des co-ordonnées au voisinage d’une hypersurface satisfaisant les hypothèses de la pro-position 3.29. 

Lemme 3.32. Soit Σ une hypersurface satisfaisant les hypothèses de la proposition 3.29. Alors, il existe un difféomorphisme Φ : Ae(1 −2r0, 1+2 r0) → { x, d (x, Σ) < 2r0}

tel qu’on ait pour C > 0,

‖Φ∗g − ge‖C1,α (ge) 6 Cε, 

où ε > 0 est la constante de la proposition 3.29. Démonstration. Considérons le difféomorphisme Fg : Σ × [−2r0, 2r0] obtenu à partir des géodésiques normales sortant de Σ. Nous utilisons alors nos contrôles sur la seconde forme fondamentale et la courbure ambiante et intégrons l’équation de Riccati satisfaite par les champs de Jacobi donnés par les changements de points sur l’hypersurface Σ. Nous obtenons ainsi comme dans le lemme A.4 (voir aussi le lemme 3.37) le contrôle suivant pour 

C = C(n, v 0) > 0, en notant s le paramètre des géodésiques s’annulant sur Σ : 

‖F ∗ 

> g

g − (ds 2 + s2gΣ)‖C1,α 6 Cε. (3.12) D’après les hypothèses de la proposition 3.29, quitte à choisir ε arbitrairement petit, la seconde forme fondamentale est arbitrairement proche d’être constante et la courbure ambiante arbitrairement petite. En particulier, d’après l’équation de Gauss, le lemme 1.54 et la proposition 1.62, cela implique qu’il existe Γ ⊂ SO (4) tel que quitte à reparamétrer Σ, pour une certaine constante C = C(n, v 0) > 0, on ait 

‖gΣ − gSn−1/Γ‖C1,α 6 Cε. 

En combinant cela avec le contrôle (3.12), nous obtenons le contrôle énoncé. 108 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

Perturbations normales de l’hypersurface. Considérons des perturbations normales de l’hypersurface de la forme Σ( w) := {γx(w(x)) , x ∈ Σ} pour une fonc-tion w sur Σ. La courbure moyenne de ces hypersurfaces admet le développement suivant démontré dans l’annexe A. 

Lemme 3.33 (Proposition A.1) . Pour tout 0 < r 0 < 16 et toute hypersurface lisse 

Σ ⊂ M dont les rayons d’injectivité et d’injectivité normale sont supérieurs à 3r0,il existe ε > 0 tel que pour toute fonction w : Σ → R telle que ‖w‖C2,α 6 ε, la courbure moyenne de Σ( w) est donnée par : 

H(Σ( w)) = H(Σ) − JΣ,M w + QΣ,M (w),

où 

JΣ,M := ∆ Σ + |AΣ|2 + Ric M (N, N )

est l’opérateur de Jacobi associé à l’hypersurface et où QΣ,M est telle que, pour une constante C > 0 dépendant de la norme C4 de la courbure et de la norme Cα

de la seconde forme fondamentale et de r0, on ait : 

‖QΣ,M (w) − QΣ,M (w′)‖Cα 6 C‖w − w′‖C2,α 

> (

‖w‖C2,α + ‖w′‖C2,α 

> )

.

La proposition 3.29 est alors une conséquence du lemme suivant appliqué à Σ. 

Lemme 3.34. Pour tout r0 > 0, il existe ε > 0 tel que si une métrique g sur l’anneau Ae(1 − r0, 1 + r0) ⊂ Rn/Γ pour Γ ⊂ SO (n) avec Γ 6 = {Id } satisfait — ‖g − ge‖C1,α 6 ε,— pour la sphère unité centrée en zéro notée S ⊂ Rn/Γ, on ait 

‖ASg − g|S ‖Cα 6 ε, 

— pour la courbure sur Ae(1 − r0, 1 + r0), on ait 

‖ Rm g ‖C4 6 ε, 

alors, il existe ε1 = ε1(r0, ε, n, α ) > 0 telle qu’il y ait une unique solution w

satisfaisant ‖w‖C2,α 6 ε1 à l’équation 

Hg(S(w)) ≡ n − 1,

où Hg est la courbure moyenne pour la métrique g et où S(w) = {γx(w(x)) , x ∈ S}

pour γx la géodésique partant en x normalement de S.4. Perturbation de presque sphères 109 

On a de plus le contrôle : 

‖w‖C2,α 6 C ‖Hg(S) − (n − 1) ‖Cα .

Démonstration. C’est une conséquence du théorème des fonctions inverses, lemme 1.12. On y munit toujours S des normes de Hölder par rapport à la restriction de 

ge à S.En considérant l’opérateur Φ : C2,α (S) → C0,α (S) défini par Φ : w ∈ C2,α (S) 7 → Hg(S(w)) − (n − 1) ∈ C0,α (S),

on est bien sous les hypothèses du lemme 1.12, avec Φ(0) = Hg(S) − (n − 1), 

d0Φ = JS,g ,

Note 3.35. Dans cette preuve, on précisera la métrique plutôt que la variété dans pour l’opérateur de Jacobi et les termes non-linéaires de la courbure moyenne. 

1. L’opérateur JS,g est inversible et a un inverse borné en fonction du ε > 0 de l’énoncé : −(n−1) n’est pas une valeur propre du laplacien car Γ 6 = {Id }, donc 

JS,g e est inversible et a un inverse borné. De plus, par proximité des métriques et par le contrôle de la seconde forme fondamentale et de la courbure de Ricci, il existe C1 > 0 telle que, 

‖JS,g e − JS,g ‖ 6 C1ε, 

pour la norme d’opérateur de C2,α (S) dans Cα(S). En effet, la différence en norme C1,α entre les métriques est plus petite que 

ε, la norme C4 de la courbure est plus petite que ε et la différence entre les secondes formes fondamentales en norme Cα est plus petite que ε. L’inverse de JS,g peut donc être uniformément borné. 2. Les termes non-linéaires sont contrôlés de manière quadratique avec une constante C > 0 dépendant de r0, α et ε :

‖QS,g (w) − QS,g (w′)‖Cα 6 C‖w − w′‖C2,α (‖w‖C2,α + ‖w′‖C2,α ).

3. Comme la seconde forme fondamentale est presque constante, on a : 

‖Hg(S) − (n − 1) ‖Cα 6 ε. 

Il existe donc une unique solution w à l’équation Φ( w) = 0 telle que ‖w‖C2,α 6110 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

ε1 := min   

> (12CC 1

, 2C1ε, 

> )

. Cette solution satisfait en fait, pour C′ > 0, 

‖w‖C2,α 6 C′‖Hg(S) − (n − 1) ‖Cα .

Preuve de la proposition 3.29. D’après le lemme 3.32, sous les hypothèses de la proposition 3.29, alors, il existe un difféomorphisme Φ : Ae(1 − 2r0, 1 + 2 r0) →{x, d (x, Σ) < 2r0} tel qu’on ait pour C > 0, —

‖Φ∗g − ge‖C1,α (ge) 6 Cε, 

— pour la sphère unité centrée en zéro notée S ⊂ Rn/Γ, on ait 

‖AS 

> Φ∗g

− (Φ ∗g)|S ‖Cα 6 ε, 

— pour la courbure sur Ae(1 − r0, 1 + r0), on ait 

‖ Rm Φ∗g ‖C4 6 ε, 

où ε > 0 est la constante des hypothèses de la proposition 3.29, pour lequel la métrique Φ ∗g satisfait les hypothèses du lemme 3.34 avec S = Φ ∗Σ la sphère unité de Rn/Γ. En appliquant le lemme 3.34, nous obtenons l’énoncé de la proposition 3.29. Pour Σ satisfaisant les hypothèses de la proposition 3.29 définissons alors ˜Σ := Σ( w), où w est l’unique solution donnée par le théorème des fonctions inverses. C’est une perturbation de Σ en une hypersurface à courbure moyenne constante. 

# 5 Feuilletage des anneaux de basse courbure par des hypersurfaces à courbure moyenne constante 

Nous allons donc maintenant construire une famille d’hypersurfaces à courbure moyenne constante feuilletant nos anneaux de basse courbure. 5. Feuilletage CMC des anneaux de basse courbure 111 

5.1 Feuilletage local 

Construisons tout d’abord un feuilletage local au voisinage d’une hypersurface à courbure moyenne constante donnée. 

Proposition 3.36 (Feuilletage local) . Pour tout 0 < r 0 < 16 , il existe C > 0 et 

0 < ε < r0 

> C

tels que si une hypersurface ˜Σ1 difféomorphe à Sn−1/Γ, Γ 6 = {Id } et de volume minoré par S0 > 0, d’une variété (M, g ) satisfait : — le rayon d’injectivité normale de ˜Σ1 et le rayon d’injectivité des points de 

˜Σ1 dans M sont minorés par 3r0,— H ˜Σ1 ≡ n − 1, et ‖A˜Σ1 − g ˜Σ1 ‖Cα < ε ,— sur l’anneau {x, d Mg (x, Σ) < 3r0}, on a ‖ Rm ‖C4 6 ε.Alors, pour s ∈ [ 11+2 r0 , 1 + 2 r0

> ]

, il existe une famille d’hypersurfaces ˜Σs àcourbure moyenne constante égale à n−1 

> s

qui feuillète une sous-partie ˜A  

> (11+2 r0

, 1 + 2r0

> )

de l’anneau qui satisfait : 

> {

x, d Mg (x, Σ) < r 0

> }

⊂ ˜A 

> (

11 + 2 r0

, 1 + 2 r0

> )

⊂ {

x, d Mg (x, Σ) < 3r0

> }

.

La construction que l’on propose consiste à perturber normalement les lignes de niveaux de la fonction distance à l’hypersurface ˜Σ1 en des hypersurfaces à cour-bure moyenne constante grâce à la proposition 3.29. Définissons les hypersurfaces equidistantes Σ s := {γx(s − 1) , x ∈ ˜Σ1} où γx

est la géodésique sortante partant normalement en x de l’hypersurface ˜Σ. Ces hypersurfaces feuillètent l’anneau défini par {x, d Mg (x, Σ) < 3r0} par définition de l’injectivité normale, et ce sont elles que l’on va perturber en des hypersurfaces à courbure moyenne constante. Leur géométrie est bien contrôlée par la courbure ambiante et l’hypersurface ˜Σ1.

Lemme 3.37. Pour tout 0 < r 0 < 16 , il existe C > 0 et 0 < ε < r0 

> C

tels que si une hypersurface ˜Σ1 difféomorphe à Sn−1/Γ, Γ 6 = {Id } et à volume minoré par S0 > 0,d’une variété (M, g ) satisfait : — le rayon d’injectivité normale de ˜Σ1 et le rayon d’injectivité des points de 

˜Σ1 dans M sont minorés par 3r0,— H ˜Σ1 ≡ n − 1, et ‖A˜Σ1 − g ˜Σ1 ‖Cα < ε ,— sur l’anneau {x, d Mg (x, Σ) < 3r0}, on a ‖ Rm ‖C4 6 ε,112 Chapitre 3. De Gromov-Hausdorff à C∞ à poids 

alors, 

> ∥∥∥∥

AΣs

s − gΣs

s2  

> ∥∥∥∥Cα
> (gΣss2
> )

6 C(

‖A˜Σ1 − g ˜Σ1 ‖Cα + |s − 1|‖ Rm ‖C0 + |s − 1|2‖ Rm ‖C4

> )

6 C(1 + r20 )ε. (3.13) 

et 

> ∥∥∥∥

HΣs

s − n − 1

s2  

> ∥∥∥∥Cα
> (gΣss2
> )

6 C(

|s − 1|‖ Ric ‖C0 + |s − 1|2‖ Rm ‖C4

> )

6 C(

r0 + r20

> )

ε, 

(3.14) 

Démonstration. Ces estimations reposent sur les contrôles de l’équation de Riccati satisfaite par la seconde forme fondamentale. Étant donnée une hypersurface ˜Σ1

de rayon d’injectivité inférieur à 3 r0 > 0, on définit un champ de vecteurs N sur la zone {x, d Mg (x, ˜Σ) < 3r0} grâce aux normales unitaires sortantes des hypersurfaces equidistantes Σ s.En notant, pour X un champ de vecteurs sur M , S(X) := ∇X N , pour lequel 

g(S(X), Y ) = A(X, Y ), on a (∇N S)( X) = −(S2(X) + Rm( X, N )N ). (3.15) En supposant ‖S|Σ1 − Id ‖Cα < ε pour ε > 0 assez petit, on peut suivre S le long des géodésiques normales, et en intégrant l’équation de Riccati précédente, il existe 

C > 0 telle que pour |s − 1| 6 r0 6 16 , on ait 

> ∥∥∥∥

S|Σs

s − Id 

s2

> ∥∥∥∥Cα

6 ‖S|Σ1 − Id ‖Cα + C|s − 1|‖ Rm ‖C0 + C|s − 1|2‖ Rm ‖C4 .

En notant κi(s) les valeurs propres de la seconde forme fondamentale de Σ s, et (ei(s)) une base orthonormée de vecteurs propres associée, si l’on projette (3.15) sur ei(s), on obtient : 

κ′

> i

(s) = − (

κi(s)2 + g(

Rm( N s, e i(s)) ei(s), N s)) 

.

En sommant cela sur i, on trouve H′(s) = −(

|A|2(s) + Ric( N s, N s))

. Avec pour condition initiale H(1) ≡ n − 1, on obtient le second contrôle énoncé. 

Démonstration de la proposition 3.36. Grâce aux contrôles (3.13), et (3.14), on peut utiliser le lemme 3.34 pour perturber normalement chaque hypersurface Σ s

en une hypersurface à courbure moyenne constante égale à n−1 

> s

notée ˜Σs. On 5. Feuilletage CMC des anneaux de basse courbure 113 en déduit l’existence d’une famille d’hypersurfaces ( ˜Σs)s∈[ 11+2 r0 ,1+2 r0] à courbure moyenne constante égale à n−1 

> s

pour chaque s. Chacune de ces hypersurfaces est définie à partir d’une unique fonction ws de ˜Σ1 dans R définie par la proposition 3.29, ˜Σs = Σ( s(1 + ws)) := {γx(s(1 + ws(x))) , x ∈ ˜Σ1},

et on a le contrôle 

‖ws‖C2,α 6 C(ε|s − 1| + ε|s − 1|2).

Montrons maintenant que la famille d’hypersurfaces feuillète bien l’anneau. Nous allons plus précisément montrer qu’étant donnés s et s′ ∈ [ 11+2 r0 , 1 + 2 r0], suffisamment proches et tels que s < s ′, ˜Σs′ s’écrit comme perturbation normale de ˜Σs avec une fonction ws′ 

> s

: ˜Σs → R strictement positive. Le fait qu’elles s’écrivent comme perturbation normale l’une de l’autre est une conséquence directe du fait que ce sont des petites perturbations (en norme C2,α ) des hypersurfaces equidis-tantes à ˜Σ1.Par le lemme 3.34, pour s et s′ suffisamment proches, la fonction ws′ 

> s

satisfait 

‖ws′ 

> s

‖C2,α 6 2|s′ − s| et est solution de l’équation 

−J˜Σs,M (ws′ 

> s

) = n − 1

s′ − n − 1

s + Q˜Σs,M (ws′ 

> s

), (3.16) où il existe C = C(ε, n, α, r 0) > 0 indépendante de s telle que pour toutes fonctions 

w, et w′, on ait ‖Q˜Σs,M (w) − Q˜Σs,M (w′)‖Cα 6 C‖w − w′‖C2,α (‖w‖C2,α + ‖w′‖C2,α ). On a donc ‖Q˜Σs,M (ws′ 

> s

)‖Cα 6 4C|s′ − s|2 pour |s′ − s| suffisamment petit. De plus, comme s ˜Σs est proche de Sn−1/Γ, J˜Σs,M est un opérateur elliptique inversible car à un difféomorphisme-près, il est proche de ∆ Sn−1/Γ + n − 1 qui est inversible. D’après (3.16), nous avons 

> ∥∥∥∥

J˜Σs,M (ws′ 

> s

− (s′ − s)) 

> ∥∥∥∥Cα

6 C(

(s′ − s)2 + ε(s′ − s))

,

puis par estimations elliptiques et inversibilité de l’opérateur, il existe donc C =

C(α, n ) > 0 telle que 

‖ws′ 

> s

− (s′ − s)‖C2,α 6 C(

(s′ − s)2 + ε(s′ − s))

.

En tout, on a donc ws′ 

> s

= ( s′ − s) + O(

(s′ − s)2 + ε(s′ − s))

, et en particulier, pour 

s′ − s et ε suffisamment petit (en fonction de n et α), ws′ 

> s

> 0. On en déduit donc que pour tous s, s ′ ∈ [ 11+2 r0 , 1 + 2 r0], les hypersurfaces ˜Σs et ˜Σs′ sont deux-à-deux disjointes et feuillètent l’anneau. En effet, on vient de voir 114 Chapitre 3. De Gromov-Hausdorff à C∞ à poids que si s < s ′ et |s − s′| est assez petit, l’hypersurface ˜Σs′ est strictement incluse d’un côté de ˜Σs. En se rappelant que pour tout s, ˜Σs = ˜Σ1(s(1 + ws)), cela signifie que pour tout x, l’application s 7 → (s(1 + ws(x))) est strictement croissante, et donc que l’on a bien un feuilletage de la zone. 

Remarque 3.38 . Il n’était pas directement possible d’assurer que deux hypersur-faces ˜Σs et ˜Σs′ ne se rencontraient pas pour s, s ′ ∈ [ 11+2 r0 , 1 + 2 r0], en effet le contrôle ‖ws‖C2,α 6 C(ε|s − 1| + ε|s − 1|2) n’est pas suffisamment bon pour em-pêcher que l’on ait ws(x) = ws′ (x′) lorsque s − 1 est beaucoup plus grand que 

s − s′.

5.2 Feuilletage global 

Revenons maintenant au cadre qui nous intéresse. Considérons une variété d’Einstein proche d’un orbifold d’Einstein au sens de Gromov-Hausdorff. D’après le théorème 2.47, cette variété est en fait ε-décrite par un arbre de bulles ALE désingularisant l’orbifold, et on a donc des coordonnées satisfaisantes sur les parties 

Mo(ε) et Nk(ε) difféomorphes à des compacts de l’orbifold et des bulles privés de leurs points singuliers. Nous sommes ici intéressés par les anneaux intermédiaires Ak(t, ε ) de basse énergie reliant ces parties. Ces anneaux sont inclus dans un anneau A(ρ1, ρ 2) centré en un point p pour ρ1 := 18 ε−1T 12 

> k

et ρ2 := 8 εT 12 

> j

tel que l’anneau A( 14 ρ1, 4ρ2

> )

ait une basse courbure. Rappelons ce que l’on sait sur un tel anneau : 1. la courbure est contrôlée par le théorème 2.34 : pour tout l ∈ N, il existe 

C > 0 telle qu’à distance ρ ∈ [ ρ1 

> 2

, 2ρ2

> ]

de p,

ρ2+ l∣∣∣∇l Rm ∣∣∣ 6 η(ρ) := Cε  

> (

ρ1

ρ

> )β1

+ 

> (

ρρ2 

> )β2
> 

,

2. par la proposition 3.12, il existe δ(ε) tel que δ(ε) → 0 lorsque ε → 0 et pour tout 2 ρ1 < ρ < 14 ρ2, il existe un domaine ˆA(

ρ, 2ρ)

satisfaisant 

A(

(1 + δ)ρ, (2 − δ)ρ)

⊂ ˆA(

ρ, 2ρ)

⊂ A(

(1 − δ)ρ, (2 + δ)ρ)

,

Γ sous-groupe fini de SO (4) et un difféomorphisme Φρ : Ae(1 , 2) ⊂ R4/Γ → ˆA(

ρ, 2ρ)

⊂ M, 5. Feuilletage CMC des anneaux de basse courbure 115 pour lesquels on ait, 

> ∥∥∥∥

Φ∗

> ρ

gρ2 − ge

> ∥∥∥∥Cl+2 (Ae(1 ,2))

6 δ. 

3. par le lemme 3.19, il existe donc une hypersurface Σ ρ1 dont la seconde forme fondamentale satisfait ∥∥∥ AΣρ1 

> g
> ρ1

− gρ21  

> ∥∥∥Cl+1 (gρ21
> )

6 δ.4. par les lemmes 3.14 et 3.20 il existe r0 > 0 tel que le rayon d’injectivité en tout point x est minoré par 3 r0d(x, p ), et le rayon d’injectivité normale à une hypersurface proche d’une sphère de rayon s au sens du lemme 3.19 soient minorés par 3 r0s.La difficulté principale de la construction de coordonnées sur un tel anneau est le fait que le rayon intérieur, ρ1, est négligeable par rapport au rayon où nos contrôles sont optimaux (¯ ρ := ( ρβ1 

> 1

ρβ2 

> 2

) 1 

> β1+β2

qui minimise η). Les hypersurfaces à courbure moyenne constante sont donc un bon outil dans ce contexte car elles peuvent être construites dans toute la zone, et car la proposition 3.24 permet de les contrôler. 

Proposition 3.39. Il existe ε0 > 0, et C > 0 tels que pour tout 0 < ε < ε 0,si (M, g ) est une variété d’Einstein ε-décrite par un arbre de singularités, et soit 

Ak(t, ε ) un anneau intermédiaire inclus dans un anneau A(4 ρ1, 14 ρ2) satisfaisant  

> ∫
> A(ρ1,ρ 2)

| Rm |2dv < ε 2. Alors, il existe un feuilletage d’une zone ˜A(

2ρ1, 12 ρ2

> )

bornée par deux hypersurfaces à courbures moyennes constantes respectivement égales à  

> n−12ρ1

et n−1  

> 12ρ2

, contenant Ak(t, ε ) et satisfaisant 

A

> (

(2 + Cε )ρ1, 

> (

12 − Cε 

> )

ρ2

> )

⊂ ˜A(

2ρ1, 12ρ2

> )

⊂ A

> (

(2 − Cε )ρ1, 

> (

12 + Cε 

> )

ρ2

> )

,

par des hypersurfaces à courbures moyennes constantes notées ˜Σs si leur courbure moyenne est égale à n−1 

> s

.Démonstration. En considérant Φ 2ρ1 le difféomorphisme de la proposition 3.12 à l’échelle 2 ρ1, on définit une hypersurface Σ 2ρ1 := Φ 2ρ1,∗S ⊂ M , où S est la sphère unité centrée en zéro de R4/Γ. D’après les lemmes 3.19 et 3.20, et le corollaire 3.21, nous avons une hypersurface à seconde forme fondamentale presque constante dans un anneau proche d’un anneau plat de R4/Γ et nous sommes sous les hypothèses du lemme 3.34. Nous pouvons alors la perturber en une hypersurface ˜Σ2ρ1 de courbure moyenne constante égale à n−12ρ1 .D’après la proposition 3.36, il existe un feuilletage par des hypersurfaces ˜Σs àcourbure moyenne constante égale à n−1 

> s