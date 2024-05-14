Ils y a des skills qui influencent les statistique, il ne faudra pas les oublier !

# Comment fonctionnent les statistiques ?

Et en particulier pour la question du vol

## Idée

Pour chaque statistique, les agissants ont une valeur de base égale à leur niveau (cohérent avec les calculs de priorité jusqu'à maintenant).

Ils ont ensuite une variation due à l'espèce. (Possiblement négative ?)

Enfin, ils ont leur propre statistique. Pour faire les calculs, on ajoute les trois.

### Avantages

#### Role de l'espèce

Les espèces jouent un rôle plus important. La similarité au sein d'une espèce fait sens.

#### Vol raisonable

Lors du vol, on ne vole que la statistique propre. L'agissant volé ne perd pas sa statistique complètement.

L'agissant qui vole obtient le max entre sa statistique propre et celle volée. La modification semble pouvoir être raisonnable.

#### Valeur intuitive pour le joueur

En gardant les trois (niveau, espèce, propre) entre 1 et 10, on obtient des valeurs dans un intervale familier, à priori comparable d'une stat à l'autre.

### Désavantages

#### Intérêt du niveau du vol

Bien que ce ne soit pas forcément mieux avec d'autres systèmes, le niveau du vol peut difficilement jouer un rôle dans le vol de statistique avec ce système.

Il pourrait tout au plus influencer la durée du vol, déterminer quelles statistiques sont volées, et réduire l'écart de priorité nécessaire au vol.

#### Calculs pour obtenir les "vraies" statistiques

Si toutes les stats se situent entre 1 et 30, il va falloir déterminer une formule de calcul pour un certain nombre d'entre elles.

Par exemple, les pv_max et la régénération des PVs ne peuvent pas être au même ordre de grandeur.

Il est plus difficile de faire le lien entre la statistique et la valeur associée, et donc d'évaluer précisément l'impact d'une modification de statistique.

Les formules pourraient difficilement être linéaires.

Par exemple, si les vitesses vont de 1 à 30, certains agissants seraient 30 fois plus rapides que d'autres. Je serais forcé de les ramener à un ordre de grandeur similaire en jouant sur les latences de leurs skills respectifs.

Aussi, les affinités sont multiplicatives (supposément entre 0 et +\infty). De plus, celle du joueur doit pouvoir diminuer.

#### Double callibration pour l'équilibrage

Il faudra équilibrer à la fois les formules et les statistiques individuelles.

## Et les modificateurs ?

Les skills, items et effets (magies et autres boosts) donnent-ils jusqu'à 30 points supplémentaires de statistique ?

Même si trouver les skills et items parfait est rare, est-ce que ça fait beaucoup ? Est-ce qu'ils devraient être limités à +5 ?

Et à quel point est-ce que les débuffs devraient être puissants ? Jusqu'à -5 ? -10 ?

Et lorsqu'on a plusieurs items avec des effets similaires, est-ce qu'ils se stackent ?

### Limiter les effets

Si on a plusieurs effets qui affectent la même statistique, on garde le plus fort buff et le plus fort débuff ?

Ça résoudrait le problème de stacker les buffs.

Pour les skills, est-ce qu'on peut faire la même chose ?
Plutôt que s'embêter à les rendre uniques ?

## Affinités

Il ferait sens que les affinités ne soient pas modifiées par le niveau.

En fait, peut-être que le niveau devrait entrer en compte dans les formules, plutôt que dans la statistique sommée.

# Quelles statistiques ?

Qu'est-ce qu'il y a comme statistiques dans le jeu ?

## PVs et PMs

Ou plutôt les PVs et PMs max.

Les plus évidentes, puisqu'on le voit en permanence.

À priori pas modifiables par le biais d'effets, items ou skills.

Doit pouvoir changer pour le joueur par contre.

Varie selon l'espèce et l'individu.

Varie selon le niveau.

## Régénérations

Les PVs et PMs se régénèrent à chaque tour (sauf s'ils sont au max).

Les deux régénérations se comportent différement.

La régénération des PMs dépend principalement de l'agissant (est-ce que c'est un utilisateur de magie ou non). La régénération des PVs est plus constante au sein d'une espèce.

### Régénération des PVs

La régénération des PVs se décompose en trois valeurs :
- une régénération maximale ;
- une régénération minimale à laquelle on descend à chaque fois qu'on est touché par une attaque ;
- une régénération de la régénération qui détermine à quelle vitesse la régénération revient à la normale.

La régénération maximale pourrait être modifiable par les items, les skills et les effets.

Les deux autres pourraient être proportionelles à la régénération maximale. Peut-être décidées au niveau de l'espèce ?

C'est surtout là pour donner une sensation de dynamique et accélerer la récupération entre les combats sans les affecter.

Mais il faut quand même que ça soit différent entre le joueur et les slimes, d'où l'idée de distinguer selon l'espèce.

## Vitesse

Est-ce que ça a vraiment besoin de varier ? Il suffit de faire varier la latence des actions pour obtenir le même résultat.

La vitesse permettrait donc à des membres d'une même espèce, qui possède le même skill actif, de faire les choses à différents rythmes. Est-ce vraiment nécessaire ?

Si le jeu va trop vite, ça devient difficile pour le joueur de contrôler son personnage.

Après, rien n'empêche de montrer le reste comme allant plus lentement.

Il y a un cas où une "vitesse" propre à chaque agissant apparaît : les auras et magies de glace qui ralentissent leurs victimes.

Enfin, une vitesse propre à chaque espèce pourrait participer à l'équilibrage du voleur.

S'il y avait des boosts, items ou skills liés à la vitesse, il faudrait qu'ils aient un faible impact.

## Force

Sert à déterminer les dégâts.

La statistique la plus évidente à vouloir modifier en combat.

Modifiable par le biais d'effets, items et skills.

Dépend probablement un peu de l'espèce, principalement de l'agissant (un mage en a moins, naturellement).

## Priorité

Conditionne certains trucs qui ne peuvent pas vraiment dépendre d'autres stats, comme la prise de controle lors d'une réanimation, l'instakill, le vol, etc.

Dépend principalement de l'agissant (voire même pas du tout de l'espêce), puisque le but est d'éviter que ces trucs fonctionnent aussi facilement sur un boss que sur un mob.

## Affinités

Les affinités modifie les interactions en fonctions des éléments impliqués.

Il s'agit toujours de multiplier ou diviser une valeur (dégâts, modificateur de la vitesse associé à un ralentissement, modificateur de la vision associé à une opacité, etc.) donc la formule de l'affinité devra être exponentielle en fonction de la statistique sous-jacente.

Les affinités sont définies par l'espèce. Certains rares individus peuvent en avoir des différentes (le joueur peut modifier ses affinités par exemple).

## Immunités

Les immunités interviennent dans les maladies de diverses façons.

Les espèces peuvent avoir des immunités spécifiques à certaines maladies ou familles de maladies.

Les agissants malades peuvent (selon la maladie) augmenter leur immunité à leur maladie et/ou à la famille de maladies à laquelle leur maladie appartient. Il y a donc des différences individuelle qui apparaissent avec le temps.

Certains effets, comme des vaccins, peuvent modifier une immunité.

Est-ce que les immunités sont affectées par le niveau ?

Supposons pour l'instant que non.
