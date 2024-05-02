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

Et à quelle point est-ce que les débuffs devraient être puissants ? Jusqu'à -5 ? -10 ?

Et lorsqu'on a plusieurs items avec des effets similaires, est-ce qu'ils se stackent ?

### Limiter les effets

Si on a plusieurs effets qui affectent la même statistique, on garde le plus fort buff et le plus fort débuff ?

Ça résoudrait le problème de stacker les buffs.

Pour les skills, est-ce qu'on peut faire la même chose ?
Plutôt que s'embêter à les rendre uniques ?
