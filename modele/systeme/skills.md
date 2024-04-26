## Problème : trouver le bon skill

Comment garantir l'unicité d'un skill ? Ou trouver le bon ?

### Exemples :

#### Skill d'immortalité
Il ne fait pas de sens qu'il y en ait plusieurs.
Comment le garantir ? S'il y en a plusieurs, comment choisir le bon ?

Mais dans le jeu, celui du joueur pourrait être différent de ceux des ennemis immortels.
Et le joueur pourrait les voler. S'ils sont eux-mêmes différents entre eux, le joueur pourrait se retouver à avoir plusieurs skills d'immortalité distincts...

#### Skill d'écrasement

Seul le joueur peut l'avoir donc pas de risque de dédoublement, mais en termes de logique s'il y a dédoublemebt ça peut poser problème.

#### Skill de magie

Puisque toutes les magies sont censées être stockées dans le même skill, qu'est-ce qui se passe lorsqu'on a plusieurs skills magiques, chacun avec ses propres magies, parfois les mêmes ?

### Solutions

#### Enterrer le problème

Limiter le vol aux skills extrasecs, rendre intrasecs tous les skills qui posent problème.
Ça ne marche pas pour le skill de magie, qu'on veut pouvoir transférer d'une classe à l'autre chez le joueur.

#### Avoir des skills uniques

Avoir des possibilités de skill, et jamais plus d'un simultanément par possibilité.
Ça éviterait aussi que le voleur stack une centaine de skills de réduction de dégats.

#### Avoir des classes uniques ?

Est-ce qu'il faudrait faire la même chose avec les classes ?
Est-ce qu'il y a un risque de dédoublement de classe ?
Est-ce que l'unicité simplifie le code ?

#### N'avoir que des skills uniques ?

Est-ce que ça fait sens pour certains skills qu'ils ne soient pas uniques ?

Presque. Les skills d'auras par exemple.
On peut bien sûr avoir plusieurs skills d'auras (d'ailleurs on va vouloir tous les récupérer en même temps).

Mais on ne peut pas avoir plusieurs skills d'aura d'instakill simultanément.

Par contre, aucun problème à avoir plusieurs skills d'auras élémentales, tant que les éléments différent.

Conclusion : en dessous d'un certain niveau hiérarchique on ne peut pas dédoubler, sauf à avoir un élément par exemple.

Comme on a les éléments, on pourrait vouloir faire la même chose avec épées et lances : créer un enum des types d'armes.
Et potentiellement définir l'énum des éléments et celui des armes dans l'éditeur ?

Les options de skill pourraient aussi être un énum des différentes choses qu'un skill peut faire.

## Problème : comment gérer le cas du joueur

Le joueur est le seul à véritablement gagner des skills en cours de partie (les autres, quand ils montent de niveau, débloquent des skills qui étaient déjà là).

### En cas de montée de niveau :

Ond evrait avoir calculé pour ne pas donner de skills redondants au joueur. N'empêche qu'ils s'ajoutent...

### En cas de vol :

Le vol peut poser problème au moment du vol, mais aussi lorsque le joueur évolue plus tard, s'il veut choisir un skill qu'il a déjà volé.

#### Ne voler que ce qu'on a pas

On ne résoud pas le problème de plus tard.

#### Ne voler que ce qu'on ne peut pas avoir par ailleurs

Mais il faut faire confiance à l'éditeur...

#### Remplacer quand un nouveau skill arrive

Ça peut être très regrettable par moment, peut-être.

#### Donner le choix au moment où il y a doublon

Ça semble raisonnable. À voir comment l'implémenter...

#### Faire une exception pour la classe voleur

On va supposer que seule la classe voleur peut posséder le skill de vol de skills (comment s'en assurer !?) et charger la classe de stocker tous les skills, y compris en double. Le joueur décide lequel est utilisé et peut changer lorsqu'il le souhaite.
