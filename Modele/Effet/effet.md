# Effets

## Que faire des effets ?

Problème :
Le type-checking strict n'aime pas les effets et leurs méthodes `execute` et `action` dont le type d'argument varie.

Les effets commencent déjà à se séparer en plusieurs groupes : sur les cases, les auras sont stockées à part ; les magies et la majeure partie des attaques ont été transformées en actions (les deux constituant une grande part des anciens effets).

Il n'y a pas d'effet qui puisse se placer à la fois sur un agissant et un item, ou un agissant et une case, on pourrait les distinguer sur ce critère pour commencer.

Par contre, il y a les `Enchantements` qui englobent des effets sur beaucoup d'éléments différents.

D'autres exemples ?
Les `Evenements`, `OneShot`, etc. peuvent être présents sur des choses très différentes.

## Listons les effets actuels.

Par temps d'appel :
 - `On_need` (spécialement créé pour les réserves de mana, 1 agissant) ;
 - `OnTick` (à chaque tour, sans plus de précision) :
   - `OnDebutTour` (beaucoup d'enchantements, poison, obscurité, investissement, 2 items, 1 case, 13 agissants) ;
   - `OnPostDecision` (maladie, confusion, 2 agissants) ;
   - `OnPostAction` (blizzard, téléportation, instakill, protection, soin, 2 cases, 3 agissants) ;
   - `On_fin_tour` (enseignement, sursis, réanimation, résurection, antidote, médicament, purification, soin, 3 items, 5 agissants) ;
 - `OnAttack` (appelé sur les attaques, protections, 1 agissant, 1 case).

Par durée d'appel :
 - `OneShot` (9 agissants, 1 item) ;
 - `Delaye` (comme `OneShot`, avec un délai, 1 case) ;
 - `Evenement` (sur plusieurs tours et hérite de `OnTick` (appelé à chaque tour), blizzard, obscurité, investissement, aura, 3 cases, 1 agissant) ;
 - `Enchantement` (hérite de `Evenement`, cas particulier, 12 agissants, 2 items) ;
 - `TimeLimited` (sur plusieurs tours mais appelé irrégulièrement, dopage, protections, 2 agissants, 1 case).

Par source :
 - action (donc souvent skill actif) :
   - magie (certaines magies produisent des effets, dont les enchantements) ;
   - attaque (une attaque peut être aussi une magie) ;
   - protection (pareil, peut aussi être une magie) ;
   - consommation (l'effet était stocké dans un consommable, peut encore être une magie) ;
 - aura (skill passif) ;
 - autre effet :
   - attaques (une attaque sur la case cause une attaque sur son occupant, s'il y en a un) ;
   - maladies (se propagent par contagion) ;
 - automatique (sursis par exemple, pour les items).

## Comment les séparer ?

Séparer les enchantements du reste n'est probablement pas nécessaire : les boosts peuvent être appliqués directement sur la magie associée.

Pour les attaques, magies, blocages, etc. je pourrais inclure l'action qui l'a généré en attribut (comme les actions ont leur agissant en attribut).

Distinguer les effets plus précisément selon ce qu'ils impactent : placer les effets de statistiques sur l'objet `Statistiques`.

La classe `Effet` est-elle nécessaire ?
Et la mécanique `execute()` et `action()` ?

L'objet de `execute()` et `action()` est de séparer l'appel régulier à l'effet (`execute()`, appelé à chaque tour) de ce que l'effet fait (`action()`, appelé par `execute()` quand il le faut, selon la classe).
`execute()` sert entre autres à comptabiliser le temps d'application de l'effet pour ceux qui durent plusieurs tours mais n'ont rien besoin de faire à part au début et à la fin.

Le modèle `execute()` - `action()` est repris dans la classe `Action`, est-ce que c'était vraiment une bonne idée ?

Comment gérer d'une part le décompte du temps et d'autre part les actions intermittente ?

C'est pratique d'avoir un compteur de temps qui vérifie au passage s'il faut réaliser une action.

## Idées

Donner à l'effet la case, l'agissant ou l'item qu'il affecte (comme les `Action` actuellement). Plus besoin de les passer en paramètre, donc possibilité de fonctions `execute()` ou `action()` uniformes.

Redonner à tous les effets l'héritage de la classe `Effet`.

Revoir la nécessité des phases : l'affichage se fera entièrement à partir de la vue, qui incluera des vues d'effets si possible.

## Affichage

Actuellement, les effets peuvent passer en phase d'affichage avant de terminer (en particulier ceux qui sont placés et retirés au même tour, sans affichage entre temps).

Pour les afficher sans utiliser les phases, il faudrait les laisser plus longtemps (les placer un tour avant de les activer, ou nettoyer les effets terminés après la vision).

## Phases

Actuellement, les différentes phases sont :
 - `"Démarrage"` (vient d'être créé, `execute()` n'a jamais été appelé) ;
 - `"En cours"` (`execute()` doit être appelé selon les besoins) ;
 - `"Affichage"` (`execute()` ne doit plus être appelé, mais l'effet doit rester pour les besoins de l'affichage) ;
 - `"Terminé"` (l'effet sera nettoyé à la première occasion).

On a déjà dévié de ça pour les `Action`, avec le système de latence. Les `Evenement` ont à la fois un temps restant (similaire à la latence), et une phase.

Le passage de `"Démarrage"` à `"En cours"` est surtout utile pour les effets qui font une action au début (et parfois une action inverse à la fin), comme les enchantements avec des effets sur les stats. Ces mécaniques ont déjà été retirées.

Si on retire les effets terminés juste après la vision, on n'a plus besoin de la phase `"Affichage"`.

Il suffit d'un moyen (par exemple une méthode) pour savoir si l'effet est terminé, et les phases n'ont plus de raison d'être.

## `action()` et `execute()`

Ces deux fonctions pourraient n'être conservées que pour les effets à appeler à chaque tour (actuellement `OnTick`). Les réserves de mana par exemple n'en ont pas besoin. À renommer peut-être.

## Effets uniques

Certains effets ne peuvent avoir qu'un représentant par support, comme les actions (une seule action à la fois), les maladies (on n'est pas deux fois malade de la même maladie), etc.

On pourrait ajouter un effet de feu (l'agissant ou l'item est en feu), qui se propage comme les maladies mais en épargnant les alliés de son responsable (friendly fire off).

Pour les actions, certains agissants pourraient en faire plusieurs à la fois : je pense en particulier à Kumoko dont les parallel minds peuvent utiliser des magies, recueillir de l'information, ou utiliser certains skills pendant que le corps accompli une autre action. C'est probablement un problème pour plus tard.