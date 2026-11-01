---
retention_scope: session
part: 7
total_parts: 7
---

[Part 7/7 of: Complétion de l’Espace des Modules des Métriques d’Einstein en Dimension 4]

Corollaire 5.100. Soit (Mo, g o) un orbifold sphérique ou hyperbolique. Alors, il n’existe pas de suite de variétés d’Einstein (Mi, g i)i telle que 

(Mi, g i) GH 

−−→ (Mo, g o),

et telle que les éclatements non-triviaux de 

(

Mi, gi 

> ti

, p i

)

pour ti → 0, ti > 0 et 6. Une obstruction générale 235 

pi ∈ Mi convergent vers des variétés Ricci-plates ALE (c’est-à-dire sans qu’arbre se forme) dont les déformations infinitésimales sont intégrables. Démonstration. D’après le corollaire 5.32, si les termes quadratiques du dévelop-pement de go sont H2, l’obstruction induite par la déformation o1 est 

> ∫
> S3
> (

3〈H2, O 41 〉ge + O41 (BeH2, ∂ re ))

dv = 0 ,

qui n’est jamais satisfaite d’après le théorème 5.98. En d’autres termes, ces orbifolds ne peuvent pas être désingularisés au sens de Gromov-Hausdorff à l’aide de variétés Ricci-plates ALE dont les déformations infinitésimales sont intégrables. Nous ne pouvons donc par exemple pas désingula-riser S4/Z2 par recollement de variétés Ricci-plates ALE dont les déformations sont intégrables. De même, en généralisant nos résultats au cadre asymptotiquement hyperbolique et non-dégénéré par les méthodes de [Biq13], il n’est pas possible de désingulariser H4/Z2, le disque de Poincaré H4 quotienté par la relation d’équiva-lence exp x0 (v) = exp x0 (−v) pour x0 ∈ H4 fixé par des bulles intégrables – c’était une conjecture d’Anderson. L’obstruction à la désingularisation d’orbifolds sphériques ou hyperboliques est identifiée généralement dans le théorème, mais nous avons pour l’instant besoin d’une hypothèse d’intégrabilité pour conclure à une obstruction générale au sens de Gromov-Hausdorff. 

Conjecture 5.101. Les orbifolds (singuliers) sphériques et hyperboliques de di-mension 4 ne peuvent pas être limites de variétés d’Einstein au sens de Gromov-Hausdorff. 236 Chapitre 5. Obstructions à la désingularisation Appendices 

> 237

# Annexe A Perturbation d’hypersurfaces 

Soit Σ une hypersurface orientable d’une variété ( M, g ), et supposons qu’il existe ε > 0 tel que l’application F : [ −ε, ε ] × Σ → M définie par 

F (s, x ) = γx(s),

soit un difféomorphisme sur son image, où γx partant de x ∈ Σ est la géodésique dont la vitesse initiale est N Σ 

> x

normale à Σ. Considérons alors une application w : Σ → [−ε, ε ] ayant une norme C2,α (Σ) suffisamment petite, et définissons Σ( w) comme étant l’hypersurface image de l’application G : Σ → Σ( w) ⊂ M définie par 

G(x) = F (w(x), x ).

Nous allons contrôler la géométrie de Σ( w), ce qui sera important dans le chapitre 3. 

# 1 Perturbations normales quelconques 

L’objectif de cette annexe est la preuve de l’estimation suivante de la cour-bure moyenne de H(Σ( w)), mais au cours de la preuve, nous obtiendrons d’autres formules utiles. 

Proposition A.1. La courbure moyenne de Σ( w) dans une zone où le rayon d’injectivité est minoré par r0 > 0 est donnée par 

H(Σ( w)) = H(Σ) − JΣ,M w + Q2Σ,M (w),

239 240 Chapitre A. Perturbation d’hypersurfaces 

où 

JΣ,M := ∆ Σ + |AΣ|2 + Ric M (N, N )

est l’opérateur de Jacobi associé à l’hypersurface et où Q2Σ,M satisfait : pour tout 

l ∈ N, 0 < α < 1, il existe C = C(α, l, n, ‖ Rm ‖Cl+2 , ‖A‖Cl+1 , r 0)

‖Q 2Σ,M (w) − Q 2Σ,M (w′)‖Cl,α 6 C‖w − w′‖Cl+2 ,α 

> (

‖w‖Cl+2 ,α + ‖w′‖Cl+2 ,α 

> )

,

Note A.2. Tout au long de la preuve, pour tout k ∈ N, on notera Qk 

> Σ,M

les opérateurs d’ordre k, c’est-à-dire satisfaisant un contrôle du type : pour tout l, il existe C > 0 telle que 

‖Q k 

> Σ,M

(w) − Q k 

> Σ,M

(w′)‖Cl,α 6 C‖w − w′‖Cl+2 ,α 

> (

‖w‖Cl+2 ,α + ‖w′‖Cl+2 ,α 

> )k−1

.

Contrôle de la métrique ambiante. Dans les coordonnées induites par F , la métrique a une expression de la forme suivante, 

F ∗g = ds 2 + (1 + s)2gs,

où gs est une métrique sur Σ. Notons que g0 est la métrique induite par g sur Σ. Notons de plus Σ s := F (s, Σ) l’hypersurface equidistante. 

Remarque A.3 . Nous allons surtout utiliser cette écriture de la métrique dans des situations qui correspondent approximativement à Σ ≈ Sn−1 plongée dans l’espace 

M ≈ Rn de la même manière que la sphère unité dans l’espace euclidien. Dans l’espace euclidien, on a ds 2 + (1 + s)2gSn−1

, et c’est pour cette raison que l’on a introduit le facteur (1 + s)2 devant gs.Nous avons le contrôle suivant sur la métrique gs.

Lemme A.4. Soit |s| 6 inf (

‖ Rm ‖− 12 

> ∞

, (sup Σ |A|)−1, ε )

, et (e1, ..., e n−1) une base orthonormée pour g0, on a l’estimation suivante de la métrique gs de Σ dans la base (ei)i

(1 + s)2(gs)ij = δij + 2 sA ij + s2

> ( ∑
> k

Aik Ajk − Kji

> )

+ Q3Σ,M (s), (A.1) 

où les Aij sont les composantes de la seconde forme fondamentale de Σ dans 

(e1, ..., e n−1), et où Kij := g(Rm( ej , N )N, e i), où N est la normale sortante à Σ.Remarque A.5 . Dans le cas de la sphère Sn−1 plongée dans l’espace euclidien Rn,pour laquelle on a Aij = δij , Kji = 0 et Rm = 0. On a donc exactement gs = g0.1. Perturbations normales quelconques 241 

Démonstration. Soit x ∈ Σ et X ∈ TxΣ. Définissons X(s) ∈ TF (x,s )Σs pour tout 

s ∈ [−ε, ε ] le champ de Jacobi le long de γx = F (x, . ) tel que X(0) = X et 

∂sX(0) = Ax(X) où Ax est la seconde forme fondamentale Σ vue comme une 1-forme à valeurs vectorielles. On a pour tout s ∈ [−ε, ε ], et pour tout (0 , X ) ∈

T(s,x )([ −ε, ε ] × Σ) : 

dF (x,s )(0 , X ) = X(s).

En effet, si l’on considère une courbe cs : [ −1, 1] → Σs sur Σ s, alors, elle correspond à une courbe c de Σ : pour tout t ∈ [−1, 1], 

cs(t) = F (c(t), s ).

On peut donc lui associer la famille de géodésiques ( γc(t))t partant de c(t) et dont la vitesse initiale est N Σ(c(t)). Le champ de Jacobi correspondant à la variation autour de t = 0 (en particulier la variation c′

> s

(0)) a donc pour condition initiale 

c′(0) et pour première variation la seconde forme fondamentale de Σ appliquée à 

c′(0) qui est la variation de la vitesse initiale, la normale. Cela va nous permettre d’exprimer gs en fonction de g0. En effet, si l’on consi-dère X et Y dans TxΣ et X(s) et Y (s) les vecteurs de T Σs associés, on a 

gF (x,s )(X(s), Y (s)) = gF (x,s )(dF (x,s )X, dF (x,s )Y )= F ∗g(x,s )(X, Y )= (1 + s)2gs(X, Y ).

Il nous suffit donc de contrôler les champs de Jacobi du type s 7 → X(s) pour un vecteur X donné pour contrôler la métrique gs pour tout s.Soient x ∈ Σ, X ∈ TxΣ et le champ de Jacobi associé X(s) ∈ TF (x,s )Σs.Considérons une base orthonormée ( e1, ..., e n−1) de TxΣ transportée parallèlement le long de γx en s 7 → (es

> 1

, ..., e sn−1), qui est une base orthonormée de TF (x,s )Σs (à ne pas confondre avec les champs de Jacobi ei(s) partant de ei). Notons alors Xi(s) := g(X(s), e si ) les composantes de X(s) dans cette base. Si l’on note Kij (s) := g(Rm( esj , γ ′(s)) γ′(s), e si ), l’équation de Jacobi s’écrit pour tout 

i,(Xi)′′ (s) + ∑

> j

Xj (s)Kij (s) = 0 .242 Chapitre A. Perturbation d’hypersurfaces On a donc pour tout i,

Xi(s) = Xi + sA (X)i −

∫ s

> 0

∫ v

> 0

∑

> j

Xj (u)Kij (u)dudv. (A.2) Notons que l’on peut contrôler le dernier terme de la manière suivante : posons 

QΣ,M (s) := ∫ s

> 0

∫ v

> 0

∑ 

> j

Xj (u)Kij (u)dudv − s2

> 2

∑ 

> j

Xj Kji (0). Nous avons, 

QΣ,M (s) = 

∫ s

> 0

∫ v

> 0

∑

> j

Xj (u)Kij (u)dudv − s2

2

∑

> j

Xj Kji (0) =

∫ s

> 0

∫ v

> 0

( ∑

> j

Xj (u)Kij (u) − Xj Kji (0) 

)

dudv 

=

∫ s

> 0

∫ v

> 0

( ∑

> j

Xj [

Kij (u) − Kji (0) ]

+ [

Xj (u) − Xj ]

Kji (u)

)

dudv. 

Pour le premier terme, sur Σ, [

Kij (u) − Kji (0) ]

est contrôlé en norme Cl,α par 

‖ Rm ‖Cl,α dans la direction Σ. Pour w et w′ des fonction Cl+2 ,α de Σ, contrôlons le terme, 

x 7 →

∫ w(x)

> w′(x)

∫ v

> 0

∑

> j

Xj [

Kij (u) − Kji (0) ]

dudv. 

On cherche à contrôler sa norme Cl+α. Contrôlons sa norme C1 pour plus de clarté, les autres contrôles s’obtiennent de la même manière, 

∂k

( ∫ w(.)

> w′(.)

∫ v

> 0

∑

> j

Xj [

Kij (u) − Kji (0) ]

dudv 

)

=

∫ w(.)

> w′(.)

∫ v

> 0

∑

> j

∂k(Xj [

Kij (u) − Kji (0) ]

)dudv 

+ ∂kw′(.)

∫ w′(.)0

∑

> j

Xj [

Kij (u) − Kji (0) ]

du 

− ∂kw(.)

∫ w(.)0

∑

> j

Xj [

Kij (u) − Kji (0) ]

du 

=

∫ w(.)

> w′(.)

∫ v

> 0

∑

> j

∂k(Xj [

Kij (u) − Kji (0) ]

)dudv 

+ ∂kw′(.)

∫ w′(.)

> w(.)

∑

> j

Xj [

Kij (u) − Kji (0) ]

du 

+ ( ∂kw′(.) − ∂kw′(.)) 

∫ w(.)0

∑

> j

Xj [

Kij (u) − Kji (0) ]

du, 1. Perturbations normales quelconques 243 et donc, en dérivant k + 1 fois, nous avons 

∥∥∥∥∫ w(.)

> w′(.)

∫ v

> 0

∑

> j

Xj [

Kij (u) − Kji (0) ]

dudv 

∥∥∥∥Ck+1 

6 ‖w − w′‖Ck (‖w‖C0 + ‖w′‖C0 )‖X‖Ck+1 (‖w‖Ck + ‖w′‖Ck )‖∇ Rm ‖Ck+1 

+ ‖w′‖Ck+1 ‖w − w′‖Ck ‖X‖Ck ‖(‖w‖Ck + ‖w′‖Ck )∇ Rm ‖Ck

+ ‖w − w′‖Ck+1 ‖w‖Ck ‖X‖Ck ‖w‖Ck ‖∇ Rm ‖Ck

6 3 ( ‖X‖Ck+1 ‖∇ Rm ‖Ck+1 ) ‖w − w′‖Ck+1 (‖w‖Ck+1 + ‖w′‖Ck+1 )2 .

Tant que |u| 6 inf (

(| Rm |)− 12 , (sup Σ |A|)−1)

(ce qui ne sera pas restrictif dans nos applications), on a des contrôles uniformes des Xj (u) grâce à l’équation de Jacobi qu’ils satisfont, et grâce à l’équation de Riccati satisfaite par ∂sXj 

> Xj

. On peut donc contrôler la différence [ Xj (u) − Xj ] en terme de la courbure ambiante et des valeurs propres de la seconde forme fondamentale de Σ : pour tout l ∈ N, il existe 

C = C(l, n ) > 0, telle que 

∥∥∥Xj (u) − Xj ∥∥∥Ck 6 C (

|u|‖ A‖Ck+1 + |u|2‖ Rm ‖Ck+1 

)

.

Pour le second terme, on cherche à contrôler l’application suivante en norme Ck,α :

x 7 →

∫ w(x)

> w′(x)

∫ v

> 0

∑

> j

[

Xj (u) − Xj ]

Kji (u)dudv. 

Comme pour le premier terme, on obtient une borne de la norme Ck+1 ,3

(

‖A‖Ck+1 +(

‖w‖Ck+1 +‖w′‖Ck+1 

)

‖ Rm ‖Ck+1 

)

‖w−w′‖Ck+1 

(

‖w‖Ck+1 +‖w′‖Ck+1 

)2

.

On en déduit donc que pour ‖Xj ‖C1 6 1, QΣ,M : Ck+2 ,α → Ck,α satisfait le contrôle 

‖QΣ,M (w) − QΣ,M (w′)‖Ck,α 63(

‖ Rm ‖Ck+2 + ‖A‖Ck+1 

)

× (

‖w′‖Ck+2 ,α + ‖w‖Ck+2 ,α 

)

‖w − w′‖Ck+2 ,α .

C’est donc un Q3Σ,M .Si l’on considère ( ei)i une base orthonormée de TxΣ et les champs de jacobi associés ei(s), en notant eki (s) = g(ei(s), e sk), et en notant Aij les composantes de 244 Chapitre A. Perturbation d’hypersurfaces la seconde forme fondamentale de Σ dans la base ( ei)i, on a 

eki (s) = δik + sA ik −  

> ∫s
> 0
> ∫v
> 0
> ∑
> l

eli(u)Kkl (u)dudv 

par (A.2). Ainsi, pour tous i, j , et pour s 6 inf (

(sup ImF | Rm |)− 12 , (sup Σ |A|)−1)

,on a (1 + s)2(gs)ij = g(ei(s), e j (s)) = ∑

> k

eki (s)ekj (s)= δij + s ∑

> k

(Aik δjk + δik Ajk )+ s2

> ( ∑
> k

Aik Ajk − 12

> ∑
> k,l
> (

δil Kkl (0) δjk + δik δjl Kkl (0) ))

+ Q3Σ,M (s)(1 + s)2(gs)ij = δij + 2 sA ij + s2

> ( ∑
> k

Aik Ajk − Kji (0) 

> )

+ Q3Σ,M (s).

Géométrie des surfaces perturbées normalement. Nous contrôlons donc bien les hypersurfaces equidistantes à Σ, passons maintenant aux perturbations normales plus compliquées. Soit w : Σ → [−ε, +ε] une application ayant une norme suffisamment petite dans C2,α (Σ), et définissons H(Σ( w)) comme étant l’hypersurface image de l’application G : Σ → Σ( w) ⊂ M définie par : 

G(x) = F (w(x), x ).

Première forme fondamentale de Σ( w). La famille ( ei(w(x)) i, définie à partir de champs de Jacobi partant d’une base orthonormée de TxΣ est une base de l’espace tangent à l’hypersurface equidistante Σ w(x). Utilisons la pour décrire l’espace tangent à Σ( w) en F (w(x), x ). Notons ∂iw les variations pre-mières de w suivant les ei qui forment une base orthonormée de T Σ. Comme 

dF (w(x),x )(ei, 0) = ei(w(x)) et dF (w(x),x )(0 , 1) = N Σw(x) , le vecteur normal à Σ w(x)

l’hypersurface equidistante à Σ, nous avons 

dG x(ei) = dF (w(x),x )(ei, ∂ iw(x)) = ei(w(x)) + ∂iw(x)N Σw(x) .1. Perturbations normales quelconques 245 Notons alors pour tout i, fi(x) := ei(w(x)) + ∂iw(x)N Σw(x) les vecteurs d’une base de TF (x,w (x)) Σ( w). Tous nos calculs seront effectués dans cette base. Comme on prendra la trace du résultat final (pour obtenir la courbure moyenne), on ne cherchera pas à en faire une base orthonormée. On en déduit l’expression suivante pour la métrique induite sur l’hypersurface Σ( w) dans la base ( fi)i. Comme g(ei(w(x)) , N Σw(x) ) = 0, nous avons 

gΣ( w) 

> ij

= g(

ei(w(x)) + ∂iw(x)N Σw(x) , e j (w(x)) + ∂j w(x)N Σw(x)

)

= ( gw(x))ij + ∂iw(x)∂j w(x). (A.3) = ( gw(x))ij + Q2Σ,M (w)= δij + 2 w(x)(

Aij − δij 

)

+ Q2Σ,M (w).

où l’on rappelle que gw(x) est la métrique de l’hypersurface équidistante Σ w(x).

Normale à Σ( w). Afin de calculer la seconde forme fondamentale de Σ( w), nous devons tout d’abord calculer sa normale. Cherchons la sous la forme suivante, 

N Σ( w) := N Σw(x) + ∑ 

> k

bkek(w(x)) 

|N Σw(x) + ∑ 

> k

bkek(w(x)) |, (A.4) pour des fonctions bk de Σ. Elle doit être orthogonale à toute la base ( fj )j , c’est-à-dire que pour tous k et j, on doit avoir 

g

(

N Σw(x) + ∑

> k

bkek(w(x)) , f j (x)

)

= 0 ,

or, fj (x) = ej (w(x)) + ∂j w(x)N Σw(x) , puis 

g

(

N Σw(x) + ∑

> k

bkek(w(x)) , f j (x)

)

= ∑

> k

bk(gw(x))kj + ∂j w(x).

La normale N Σ( w) est donc l’unique vecteur de la forme (A.4) où les bk sont les solutions de ∑

> k

bk(gw(x))kj = −∂j w(x). (A.5) Notons que comme ( gw(x))kj = 11+ w(x)2 δkj + Q1Σ,M (w) = δkj + Q1Σ,M (w). On en 246 Chapitre A. Perturbation d’hypersurfaces déduit donc que bk = ∂kw(x) + Q2Σ,M (w),puis 

∣∣∣∣N Σw(x) + ∑

> k

bkek(w(x)) 

∣∣∣∣

> 2

= 1 + ∑

> j,k

bj bk

= 1 + g(∂kw(x), ∂ kw(x)) = 1 + Q2Σ,M (w(x)) . (A.6) 

Seconde forme fondamentale de Σ( w). La seconde forme fondamentale de Σ( w) dans la base fi s’écrit 

AΣ( w) 

> ij

= g(∇fi N Σ( w), f j ).

Développons cette expression grâce à (A.4) et en utilisant le fait que g(

N Σw(x) +

∑ 

> k

bkek(w(x)) , f j

)

= 0, 

AΣ( w) 

> ij

= g(∇fi N Σ( w), f j )= g

(

∇fi

( N Σw(x) + ∑ 

> k

bkek(w(x)) 

|N Σw(x) + ∑ 

> k

bkek(w(x)) |

)

, f j

)

= g

( ∇fi (N Σw(x) + ∑ 

> k

bkek(w(x)) 

|N Σw(x) + ∑ 

> k

bkek(w(x)) | , f j

)

.

Maintenant, par (A.6), |N Σw(x) + ∑ 

> k

bkek(w(x)) | est proche de 1 à un terme quadratique près ce qui est l’ordre de précision que l’on vise. Calculons donc les composantes ˜Aij := |N Σw(x) + ∑ 

> k

bkek(w(x)) |AΣ( w) 

> ij

= AΣ( w) 

> ij

+ Q2Σ,M (w(x)) qui sont plus simples, ˜Aij = g(

∇fi

(

N Σw(x) + ∑

> k

bkek(w(x)) )

, f j

)

= g(

∇fi N Σw(x) , f j

)

+ g(

∇fi (∑

> k

bkek(w(x)) , f j

)

(A.7) Développons maintenant chacun des deux termes de (A.7). Pour le premier terme, comme N Σw(x) est la vitesse d’une géodésique, nous avons, 

g(

∇fi (N Σw(x) ), f j

)

= g(

∇ei(w(x))+ ∂iw(x)N Σw(x) N Σw(x) , f j

)

= g(

∇ei(w(x)) N Σw(x) , f j

)

+ ∂iw(x)g(

∇N Σw(x) N Σw(x) , f j

)

= g(

∇ei(w(x)) N Σw(x) , f j

)

+ 0 = g(

∇ei(w(x)) N Σw(x) , e j (w(x)) )

(A.8) 1. Perturbations normales quelconques 247 C’est donc la seconde forme fondamentale de l’hypersurface équidistante Σ w(x).Or, on contrôle les valeurs propres de la seconde forme fondamentale grâce à l’équation de Riccati qu’elles satisfont. Si ( εi(s)) i est une base de vecteurs propres pour la seconde forme fondamentale de Σ s en γx(s), les valeurs propres associées 

κi satisfont l’équation de Riccati 

κ′

> i

(s) = −κ2 

> i

(s) − Kii (s),

où, Kii = g(

Rm( N s, ε i(s)) εi(s), N s)

.On en déduit donc, que pour w petit devant ‖A‖−1 

> ∞

et ‖ Rm ‖− 12 

> ∞

, les valeurs propres κi(w(x)) de la seconde forme fondamentale de Σ w(x) sont contrôlées par 

κi(w(x)) = κi(0) − w(x) (

κ2 

> i

(0) + Kii (0) )

+ Q2Σ,M (w(x)) . (A.9) Pour le second terme de (A.7), on a : 

g(

∇fi (∑

> k

bkek(w(x)) , f j

> )

= ∇fi

> (

g( ∑ 

> k

bkek(w(x)) , f j

> ))

− ∑

> k

bkg(

∇fi (ek(w(x)) , f j

> )

= ∂2 

> ij

w + ∑

> l

(Γ Σ( w))lij ∂lw, (A.10) où les (Γ Σ( w))lij sont les symboles de Christoffel de gΣ( w) dans la base ( fi)i. C’est en fait l’expression en coordonnées de Hess gΣ( w) w.Comparons maintenant Hess gΣ( w) w à Hess gΣ w. Cela revient à comparer les symboles de Christoffel des métriques. Nous savons, par (A.3) que la métrique de Σ( w) en x est celle de Σ w(x) au terme ∂iw(x)∂j w(x), qui est quadratique en w,près. On en déduit donc que Γ Σ( w) = Γ Σw(x) + Q2Σ,M (w). Maintenant, on a aussi un contrôle entre la métrique associée à Σ( w(x)) et celle de Σ grâce à (A.1). On en déduit que les symboles de Christoffel sont proches à un Q1Σ,M (w)-près, mais cette erreur multipliée par ∂lw donc : 

g

> (

∇fi

> ( ∑
> k

bkek(w(x)) )

, f j

> )

= Hess gΣ w + Q2Σ,M (w). (A.11) 

Courbure moyenne de Σ( w). Il nous reste maintenant à prendre la trace de la seconde forme fondamentale calculée dans la partie précédente à l’aide de la métrique gΣ( w). Notons qu’il suffit de prendre celle de ˜A à notre niveau de précision car |N Σw(x) + ∑ 

> k

bkek(w(x)) | = 1 + Q2Σ,M (w). Pour le premier terme (A.8), cela 248 Chapitre A. Perturbation d’hypersurfaces revient à sommer les valeurs propres estimées par (A.9), et pour le second terme, cela revient à prendre la trace de la Hessienne. Pour la trace du premier terme (A.8), les métriques gΣ( w) et gw(x) sont proches à un terme quadratique en w près, et on peut donc prendre la trace avec gw(x) en n’induisant qu’une erreur quadratique en w. On obtient donc approximativement la somme des valeurs propres estimées dans (A.9) : 

H(Σ) − w(x)(

|AΣ|2 + Ric( N Σ, N Σ))

+ Q2Σ,M (w),

où H(Σ) := ∑ 

> i

κi(0) est la courbure moyenne de Σ et où |AΣ|2 = ∑ 

> i

κ2 

> i

(0) est la somme des carrés des valeurs propres de la seconde forme fondamentale de Σ. Pour le second terme, l’erreur que l’on fait en prenant la trace avec gΣ pour faire apparaître son laplacien est d’ordre 1. Comme le terme s’applique déjà à w,cela signifie que l’erreur totale sera d’ordre 2 en w,

−∆Σw + Q2Σ,M (w).

Au total, on obtient, 

H(Σ( w)) = H(Σ) − JΣ,M w + Q2Σ,M (w), (A.12) où JΣ,M := ∆ Σ + |AΣ|2 + Ric( N Σ, N Σ) est l’opérateur de Jacobi de l’hypersurface Σ plongée dans M .

# 2 Perturbations infinitésimales 

Grâce aux estimations générales précédentes, on déduit des formules de per-turbations normales infinitésimales. Elles sont résumées dans le corollaire suivant. Étant donnée une immersion lisse ϕ0 : N n−1 → M n, on considère une variation du type suivant, 

∂sϕs = usN ϕs(N ), (A.13) pour une certaine fonction us : N → R lisse. 

Remarque A.6 . Les formules suivantes sont montrées directement dans le théorème 3.2 de [HP99], où l’orientation est opposée à la notre, mais où les variations sont du type ∂sϕs = −usN ϕs(N ). On retombe donc sur les mêmes formules. 

Corollaire A.7. Étant donnée une déformation comme (A.13) , on a les variations suivantes des quantités géométriques : 2. Perturbations infinitésimales 249 

1. ∂sϕ∗

s g = 2 usAϕs(N ),2. ∂sN ϕs(N ) = grad ϕs(N )us,3. ∂sAϕs(N )

ij = −∇ ϕs(N )

i ∇ϕs(N )

j us + (

Aik Akj + Kji

)

,4. ∂sHϕs(N ) = −

(

∆ϕs(N ) +

∣∣∣Aϕs(N )∣∣∣2

+ Ric (

N ϕs(N ), N ϕs(N )))

us.250 Chapitre A. Perturbation d’hypersurfaces Annexe B Dégénérescence orbifold des métriques AdS-Taub-Bolt 

Présentons le seul exemple explicite connu de dégénérescence orbifold autre que ceux donnés par les instantons gravitationnels d’Eguchi-Hanson et de Gibbons-Hawking. Les métriques AdS-Taub-Bolt, définies dans [PP87], sont une famille de mé-triques U (2)-invariantes, d’Einstein et asymptotiquement hyperboliques sur T ∗S2.Elles dégénèrent vers un orbifold d’Einstein avec une singularité R4/Z2. Par manque de référence suffisamment précise sur l’apparition de la métrique d’Eguchi-Hanson, nous décrivons en détails cette dégénérescence. Cela permet d’exhiber sur un exemple concret les coordonnées et les différentes constructions de cette thèse. 

# 1 Limite d’éclatements 

La famille de métriques d’AdS-Taub-Bolt dépend d’un paramètre s > 1 et définit une métrique lisse sur ( s, +∞) × S3/Z2 ≈ T 2S2\S2 définie dans [HHP99] par (avec un simple changement de variables ψ = E1/2 

> s

τ ), 

gT B (s) = Es

4

( 4( u2 − 1) 

Fs(u) du 2 + Fs(u)

u2 − 1α21 + ( u2 − 1)( α22 + α23)

)

, (B.1) où nous avons 

Fs(u) : = Esu4 + (4 − 6Es)u2 +

[

− Ess3 + (6 Es − 4) s + 3Es − 4

s

]

u + (4 − 3Es)= Esu(u3 − s3) + (4 − 6Es)( u2 − su ) + (3 Es − 4) 

( us − 1

)

.

251 252 Chapitre B. Dégénérescence des métriques AdS-Taub-Bolt et Es := 43(1+ s) . La métrique se complète en une métrique lisse sur T ∗S2 en ajoutant une sphère S2 totalement géodésique de métrique ( s2 − 1)( α22 + α23) à u = s. Cette sphère se contracte donc sur un point lorsque s → 1. Rappelons que pour ε > 0, la métrique d’Eguchi-Hanson peut aussi être définie sur ( ε, +∞) × S3/Z2 par 

gEH (ε) = 

> (

1 − ε4

r4

> )−1

dr 2 + r2

4

> (

1 − ε4

r4

> )

α21 + r2

4 (α22 + α23). (B.2) La métrique se complète encore une fois sur T ∗S2 à l’aide d’une sphère totalement géodésique de métrique ε2 

> 4

(α22 + α23) à r = ε qui se contracte en un point lorsque 

ε → 0. Nous allons montrer que c’est bien la “bulle” de notre dégénérescence, et que l’espace singulier est l’orbifold U (2)-invariant et autodual dont la métrique est 

gT B (1) qui a pour expression 

u + 1 (u − 1)( u2 + 2 u + 3) du 2 + (u − 1)( u2 + 2 u + 3) 6( u + 1) α21 + (u + 1)( u − 1) 9 (α22 + α23).

(B.3) Trouvons des coordonnées dans lesquelles la métrique gT B (s) pour s proche de 1, est proche de ( s2 − 1) gEH , gR4/Z2 et gT B (1) sur différentes parties de la variété. La métrique converge clairement vers gT B (1) pour r > 1 lorsque s → 1 donc nous sommes principalement intéressés par le cas où r est proche de s qui est lui-même proche de 1. Afin de faire correspondre les parties des métriques proportionnelles à α22 + α23,lorsque s est proche de 1 nous considérons le changement de variable s = 1 + η2

pour η > 0 petit et u2 = η2r2 + 1 qui donne du 2 = η2r2 

> 1+ η2r2

dr 2. La métrique se réécrit : 

gT B (1 + η2) = E1+ η2

4 

> (

4η4r4

(1 + η2r2)Gη2 (r2)η2dr 2 + Gη2 (r2)

η4r4 η2r2α21 + η2r2(α22 + α23)

> )

,

(B.4) où Gη2 (r2) := F1+ η2 (√1 + η2r2). Soyons plus précis sur le comportement de Gη2 (r2) quand η → 0 pour r borné (restant donc dans une région où la métrique devrait ressembler à la métrique d’Eguchi-Hanson). Nous avons 

E1+ η = 43(2 + η) = 23 − η

6 + O(η2).2. L’ordre de précision suivant 253 alors qu’après la compensation (absolument pas évidente) des termes en O(1) et en O(η2), nous avons 

Gη2 (r2) = η4

> (

r4 − 4

> )

+ O(η3). (B.5) En insérant ce contrôle dans (B.4), nous obtenons l’estimée 32η2 gT B (1 + η2) = 

> (

1 − 4

r4

> )−1

dr 2 + 14

> (

1 − 4

r4

> )

r2α21 + 14r2(α22 + α23) + O(η2),

(B.6) Nous voyons ainsi la métrique gEH (√2) apparaître au premier ordre comme at-tendu dans les théorèmes de [And89, BKN89]. 

Remarque B.1 . L’erreur en η2 vers la métrique d’Eguchi-Hanson sur N (ε) = {r < ε−1} est celle estimée dans [Biq13, Ozu19b]. 

Remarque B.2 . Dans la convergence vers l’orbifold sur Mo(ε) = {r > η −1ε}, nous n’obtenons qu’une convergence en η2 alors que pour une dégénérescence compacte, l’erreur serait en η4 (l’erreur commise en étendant le terme en r−4 de la métrique ALE). La raison est que l’infini conforme de la métrique doit être modifié pour que la dégénérescence ait lieu comme décrit dans la dernière section de [Biq13]. 

Remarque B.3 . Cette forme explicite de la métrique et son développement asymp-totique quand η → 0 converge effectivement vers une métrique plate dans l’anneau de basse courbure et vers une métrique hyperbolique à l’infini. L’anneau de basse courbure A(ε) est la région où 132 ε−1 < r < 32 η−1ε et la métrique a un développe-ment convergeant en puissances de η2 et r2 dans cette région, l’erreur est même en 

η2r2 + r−4 comme prévu par le théorème 3.42. L’expression entière est en réalité analytique en r2 et en η2 dans nos coordonnées. 

# 2 L’ordre de précision suivant 

Nous pouvons de plus calculer le terme suivant du développement de 23η2 gT B (1+ 

η2) = gEH (√2) + η2h2 + O(η4), avec 

h2 = r4(

− 5r6 − 3r4 + 12 r2 + 20 )

6r4 − 4 dr 2 − r6 + 3 r4 − 12 r2 − 424 r4 α21, (B.7) 254 Chapitre B. Dégénérescence des métriques AdS-Taub-Bolt qui est solution de l’équation dgEH (√2) Ric( h2) = −3gEH (√2). Le 2-tenseur h2 est de plus asymptotique lorsque r → +∞ au 2-tenseur quadratique 

H2 := −56r2dr 2 − r2

24 r2α21,

qui est bien le terme quadratique de la métrique gT B (1) en r = 0 et satisfait donc dge Ric( H2) = −3ge. En effet, en appliquant une fois de plus le changement de variable r2 = u2 − 1 à l’expression (B.3), et après avoir estimé E1 = 23 et 

F1(√1 + r2) = r4 − r6 

> 6

+ O(r8), nous trouvons 

gT B (1) = r2

r4 − r6 

> 6

+ O(r8)

r2

1 + r2 dr 2 + r4 − r6 

> 6

+ O(r8)4r2 α21 + r2

4 (α22 + α23), (B.8) qui a le développement 

gT B (1) = dr 2 + 14r2(α21 + α22 + α23) − r2 

> (

56dr 2 + r2

24 α21

> )

+ O(r4) (B.9) = gR4/Z2 + H2 + O(r−3). (B.10) On vérifie de plus que la courbure à la singularité R4/Z2 satisfait Ric 0 = 0 car la métrique est d’Einstein et que dans les bases habituelles de Ω ±, nous avons 

R− =

> 

−1 0 00 −1 00 0 −1 

> 

,

car la courbure est autoduale, et finalement 

R+ =

> 

0 0 00 −32 00 0 −32 

> 

,

a un noyau de dimension 1 et donc det R+ = 0. On retrouve bien que la mé-trique d’Eguchi-Hanson apparaît dans la direction du noyau de dimension 1 de l’endomorphisme de courbure de gT B (1) à son point singulier comme attendu par [Biq13]. 

Remarque B.4 . L’espace limite gT B (1) est autodual (c’est-à-dire qu’il satisfait 

W − = 0), mais ce n’est pas le cas des métriques gT B (s) pour s > 1. Une ma-nière de s’en convaincre pour s − 1  1 est de remarquer que sur la partie proche de 3( s−1) 2 

> 2

gEH , la courbure est proche de celle de 3( s−1) 2 

> 2

gEH qui est anti-autoduale, 2. L’ordre de précision suivant 255 et que sur la partie proche de gT B (1), la courbure est presque autoduale. Les variations de l’infini conforme sont aussi uniquement des changements de la partie en α21 de la métrique pour un choix naturel de représentant de la métrique conforme. 256 Chapitre B. Dégénérescence des métriques AdS-Taub-Bolt Bibliographie 

[AV12] A.G. Ache ; J.A. Viaclovsky, Obstruction-flat asymptotically locally Euclidean metrics . Geom. Funct. Anal. 22 (2012), no. 4, 832–877 [And89] M.T. Anderson, Ricci Curvature Bounds and Einstein Metrics on Compact Manifolds . J. Amer. Math. Soc. 2 (1989), no. 3, 455–490. [And92] M. T. Anderson, The L2 structure of moduli spaces of Einstein me-trics on 4-manifolds , Geometric and Functional Analysis, March 1992, Volume 2, Issue 1, pp 29–89 [And10] M.T. Anderson, A survey of Einstein metrics on 4-manifolds . Hand-book of geometric analysis, No. 3, 1–39, Adv. Lect. Math. (ALM), 14, Int. Press, Somerville, MA, 2010. [Art68] Michael Artin, On the Solutions of Analytic Equations , Inventiones mathematicae 5 (1968) : 277-291 [Auv18] H. Auvray, From ALE to ALF gravitational instantons . Compos. Math. 154 (2018), no. 6, 1159–1221. [Bam12] R.H. Bamler, Construction of Einstein metrics by generalized Dehn filling . J. Eur. Math. Soc. (JEMS) 14 (2012), no. 3, 887–909. [BKN89] S. Bando ; A. Kasue ; H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal vo-lume growth . Invent. Math. 97 (1989), no. 2, 313–349. [Ban90] S. Bando, Bubbling out of Einstein manifolds . Tohoku Math. J. (2) 42 (1990), no. 2, 205–216. [Bes87] A.L. Besse, Einstein manifolds , Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], 10. Springer-Verlag, Berlin, 1987. [BM88] E. Bierstone, P. D. Milman, Semianalytic and subanalytic sets , Pu-blications mathématiques de l’I.H.É.S., tome 67 (1988), p. 5-42 257 258 Chapitre 5. Bibliographie [Biq07] O. Biquard, Polycopié on differential geometry and global analysis. 

http://www.math.ens.fr/ biquard/dgga2007.pdf (2007) [Biq13] O. Biquard, Désingularisation de métriques d’Einstein. I . Invent. Math. 192 (2013), no. 1, 197–252. [Biq16] O. Biquard, Désingularisation de métriques d’Einstein. II . Invent. Math. 204 (2016), no. 2, 473–504. [Biq17] O. Biquard, Non dégénérescence et singularités des métriques d’Ein-stein asymptotiquement hyperboliques en dimension 4 . Math. Ann. 372 (2018), no. 1-2, 531–553. [BH19] O. Biquard ; H. Hein, The renormalized volume of a 4-dimensional Ricci-flat ALE space . arXiv :1901.03647 [math.DG] [BR09] O. Biquard ; Y. Rollin, Wormholes in Ach Einstein Manifolds . Trans. Amer. Math. Soc. 361 (2009), no. 4, 2021–2046. [BR15] O. Biquard ; Y. Rollin, Smoothing singular constant scalar curvature Kähler surfaces and minimal Lagrangians. Adv. Math. 285 (2015), 980–1024. [Böh98] C. Böhm, Inhomogeneous Einstein metrics on low-dimensional spheres and other low-dimensional spaces. Invent math 134, 145–176 (1998) [BL81] J.-P. Bourguignon ; B. H. Lawson, Stability and isolation phenomena for Yang-Mills fields. Comm. Math. Phys. 79 (1981), no. 2, 189–230. [BK17] S. Brendle ; N. Kapouleas Gluing Eguchi–Hanson metrics and a ques-tion of Page , Commun. Pure Appl. Math. 70 (2017) 1366–1401 [CGH00] D. J. Calderbank ; P. Gauduchon ; M. Herzlich, Refined Kato inequali-ties and conformal weights in Riemannian geometry. J. Funct. Anal., vol. 173 (2000), 214-255. [CC96] J. Cheeger ; T.H. Colding, Lower bounds on Ricci curvature and the almost rigidity of warped products . Ann. of Math. (2) 144 (1996), no. 1, 189–237. [CGT82] J. Cheeger ; M.Gromov ; M. Taylor, Finite propagation speed, kernel estimates for functinos of the laplace operator, and the geometry of complete Riemannian manifolds . J. Differential Geom. 17 (1982), no. 1, 15–53. [CN15] J. Cheeger ; A. Naber, Regularity of Einstein Manifolds and the Codimension 4 Conjecture . Ann. of Math. (2) 182 (2015), no. 3, 1093–1165. . 259 [CT94] J. Cheeger ; G. Tian, On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature de-cay . Invent. Math. 118 (1994), no. 3, 493–571. [CT06] J. Cheeger ; G. Tian, Curvature and injectivity radius estimates for Einstein 4-manifolds , J. Amer. Math. Soc. 19 (2006), 487-525 [CEV17] O. Chodosh ; M. Eichmair ; A. Volkmann, Isoperimetric structure of asymptotically conical manifolds . J. Differ. Geom. 105 (2017), 1–19. [Col97] T.H. Colding, Ricci Curvature and Volume Convergence. Ann. of Math. (2) 145 (1997), no. 3, 477–501. [Cro80] C. Croke, Some isoperimetric inequalities and eigenvalue estimates. 

Ann. Sci. École Norm. Sup. (4) 13 (1980), no. 4, 419–435. [DK81] D. M. DeTurck ; J. L. Kazdan, Some regularity theorems in Rieman-nian geometry , Ann. Sci. Ecole Norm. Sup. (4), 14 (1981), p. 249-260 [Ebi70] David G. Ebin, The manifold of Riemannian metrics , 1970 Global Analysis (Proc. Sympos. Pure Math., Vol. XV, Berkeley, Calif., 1968) pp. 11–40 Amer. Math. Soc., Providence, R.I. [Fol89] G.B. Folland, Harmonic analysis of the de Rham complex on the sphere . Reine Angew. Math. 398 (1989), 130–143. [Gao90] L. Gao, Einstein metrics . J. Diff. Geom. 32 (1990), 155-183. [GH78] G.W. Gibbons ; S.W. Hawking, Gravitational multi-instantons . Phy-sics Letters B Volume 78, Issue 4, 9 October 1978, Pages 430-432 [GP79] G.W. Gibbons ; C.N. Pope, The positive action conjecture and asymp-totically euclidean metrics in quantum gravity . Comm. Math. Phys. 66, 267–290 (1979) [GW88] R. E. Greene ; H. Wu, Lipschitz convergence of Riemannian mani-folds. , Pacific J. Math. Volume 131, Number 1 (1988), 119-141. [Gro81] M. Gromov, Structures métriques pour les variétés riemanniennes .Textes Mathématiques Paris (1981), 1-120. (rédigé par Lafontaine et Pansu). (in French) [Ham82] R. Hamilton, Three-manifolds with positive Ricci curvature. J. Diffe-rential Geom. 17 (1982), no. 2, 255–306. [HV16] J. Han ; J. Viaclovsky Deformation theory of scalar-flat Kähler ALE surfaces. Amer. J. Math. 141. (2016) [HV20] J. Han ; J. Viaclovsky Existence and compactness theory for ALE scalar-flat Kähler surfaces. Forum of Mathematics, Sigma, 8, E1. 260 Chapitre 5. Bibliographie [HHM04] T. Hausel ; E. Hunsicker ; R. Mazzeo, Hodge cohomology of gravita-tional instantons , Duke Math. J. Volume 122, Number 3 (2004), 485-548. [HHP99] S. W. Hawking ; C. J. Hunter ; and Don N. Page, NUT charge, anti-de Sitter space, and entropy, Phys. Rev. D (3) 59 (1999), no. 4, 044033, 6[HH97] E. Hebey ; M. Herzlich, Harmonic coordinates, harmonic radius and convergence of Riemannian manifolds, Rend. Mat. Appl. (7) 17 (1997), 569–605 (1998). [HP99] G. Huisken ; A. Polden, Geometric evolution equations for hypersur-faces . Calculus of variations and geometric evolution problems (Ce-traro, 1996),45–84. Lecture Notes in Math., 1713, Springer, Berlin, 1999 [Jos84] J. Jost, Harmonic mappings between Riemannian manifolds, Can-berra Univ.Press, 1984. [KL16] V. Kapovitch ; J. Lott, On noncollapsed almost Ricci-flat 4-manifolds .Amer. J. Math. 141, p. 737-755 [Kas88] A. Kasue, A compactification of a manifold with asymptotically non-negative curvature, Ann. Sci. Ecole Norm. Sup. (4) 21 (1988), 593-622. [KB90] R. Kobayashi ; S. Bando, Ricci-flat Kähler metrics on affine algebraic manifolds. II . Mathematische Annalen (1990) Volume : 287, Issue : 1, page 175-180 [Koi83] N. Koiso, Einstein Metrics and Complex Structures . Invent. Math. 73 (1983), no. 1, 71–106. [Kro89a] P.B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients . J. Differential Geom. Volume 29, Number 3 (1989), 665-683. [Kro89b] P.B. Kronheimer, A Torelli-type theorem for gravitational instantons .J. Differential Geom. Volume 29, Number 3 (1989), 685-697. [LV16] M. Lock ; J. Viaclovsky, Quotient singularities, eta invariants, and self-dual metrics . Geom. Topol. Volume 20, Number 3 (2016), 1773-1806. [LM85] R.B. Lockhardt ; R.C. McOwen, Elliptic operators on noncompact manifolds . Ann. Sci. Normale Sup. Pisa IV-12 (1985), 409–446. . 261 [Łoj65] S. Łojasiewicz, Ensembles semi-analytiques , I.H.E.S. Lecture notes (1965) [McC02] D. McCullough, Isometries of elliptic 3-manifolds , J. London Math. Soc. 65 (2002), 167–182. [Nak90] H. Nakajima, Self-Duality of ALE Ricci-Flat 4-Manifolds and Posi-tive Mass Theorem . Adv. Stud. Pure Math. Recent Topics in Diffe-rential and Analytic Geometry, T. Ochiai, ed. (Tokyo : Mathematical Society of Japan, 1990), 385 - 396 [Nak94] H. Nakajima, A convergence theorem for Einstein metrics and the ALE spaces , in Selected papers on number theory, algebraic geometry, and differential geometry. American Mathematical Society Transla-tions, Series 2, 160. 1994. [Ozu19a] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds I . pre-print. [Ozu19b] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II . pre-print. [PR78] F. Pacard ; T. Rivière , Linear and Nonlinear Aspects of Vortices , . Progress in Nonlinear Differential Equations and their Applications, 39. Birkhäuser, Boston, MA, 2000. [PX09] F. Pacard ; X. Xu, Constant mean curvature spheres in Riemannian manifolds . Manuscripta Mathematica. 128, 3 (2009), 275-295 [Pag78] D.N. Page, A physical picture of the K3 gravitational instanton , Phy-sics Letters B80, 55–57 (1978) [Pag81] D.N. Page, A periodic but nonstationary gravitational instanton, Phy-sics Letters B100, 313–315 (1981) [PP87] D. N. Page ; C. N. Pope, Inhomogeneous Einstein metrics on complex line bundles , Classical and Quantum Gravity, Volume 4, Number 2 [Pal68] R. Palais, Foundations of global non-linear analysis , W. A. Benjamin, Inc., New York-Amsterdam 1968 [Pet98] P. Petersen, Riemannian geometry , New York Springer cop. 1998, Graduate texts in mathematics 171 [Sco83] P. Scott, The geometries of 3-manifolds, Bull. London Math. Soc. 15 (1983), no. 5, b401–487. [Sco05] A. Scorpan, The Wild World of 4-Manifolds, Amer. Math. Soc., Pro-vidence, RI, 2005. 262 Chapitre 5. Bibliographie [SSU89] L. M. Sibner ; R. J. Sibner ; and K. Uhlenbeck, Solutions to Yang—Mills equations that are not self-dual Proc. Natl. Acad. Sci. U S A. 1989 Nov ; 86(22) : 8610–8613. [Spo14] C. Spotti, Deformations of nodal Kähler-Einstein del Pezzo surfaces with discrete automorphism groups, J. Lond. Math. Soc. (2) 89 (2014), 539–558. [Suv11] I. Suvaina, ALE Ricci-flat Kähler metrics and deformations of quo-tient surface singularities . Ann. Global Anal. Geom. 41 (2012), no. 1, 109–123. [Top87a] P. Topiwala, A new proof of the existence of Kähler-Einstein metrics on K3 I . Invent. Math. 89, 425–448 (1987) [Top87b] P.Topiwala, A new proof of the existence of Kähler-Einstein metrics on K3, II . Invent. Math. 89, 449–454 (1987) [WZ90] M. Wang ; W. Ziller Einstein metrics on principal torus bundles , J. Differential Geom. 31 (1990), no. 1, 215–248. [Whi65] E. F. Whittlesey, Analytic Functions in Banach Spaces , Proc. Amer. Math. Soc. 16 (1965), 1077–1083. [Ye96] R. Ye, Constant mean curvature foliation: singularity structure and curvature estimate. Pacific J. Math. Volume 174, Number 2 (1996), 569-587. ABSTRACT We study the completion of the set of unit-volume Einstein 4-manifolds. Their degenerations were observed in the 70's and understood in the 80's in a Gromov-Hausdorff sense. We prove that any smooth Einstein 4-manifold close to a singular one in a mere Gromov-Hausdorff sense is the result of a gluing-perturbation procedure that we develop. This new description lets us extend Biquard's obstruction to a general setting, allowing multiple singularities and trees of singularities and only assuming a Gromov-Hausdorff convergence. This enables the construction of new Einstein metrics and also sheds light on the structure of the moduli space of Einstein 4-manifolds near its boundary. MOTS CLÉS Variétés d'Einstein, Compacité, Dimension 4, Espace de modules RÉSUMÉ Nous étudions la complétion de l'ensemble des métriques d'Einstein à volume normalisé en dimension 4. Leurs dégénérescences ont été observées dans les années 70 et comprises au sens de Gromov-Hausdorff dans les années 80. Nous montrons que toute métrique d'Einstein proche au sens de Gromov-Hausdorff d'une métrique singulière est le résultat d'un processus de recollement-perturbation que l'on développe. Cette nouvelle description nous permet d'étendre une obstruction observée par Biquard au cadre général autorisant la formation d'arbres de singularités en un nombre arbitraire de points et en supposant une simple proximité de Gromov-Hausdorff. Elle rend aussi possible de KEYWORDS Einstein manifolds, Compactness, Dimension 4, Moduli space


## Native file acquisition

```json
[
  {
    "url": "https://tristanozuch.github.io/publications/these_ozuch_tristan.pdf",
    "final_url": "https://tristanozuch.github.io/publications/these_ozuch_tristan.pdf",
    "name": "these_ozuch_tristan.pdf",
    "size": 2516675,
    "role": "primary_object_file",
    "status": "downloaded",
    "checksum": "sha256:71eb9ac053892caff678ca35f3f9c67a68d50be2bf06fd8c1320919f315debcb",
    "identity_bound": true,
    "parent_url": "https://tristanozuch.github.io/publications/these_ozuch_tristan.pdf",
    "primary_label": false,
    "download_eligible": true,
    "label": ""
  }
]
```
