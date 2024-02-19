Les consommables (potions et parchemins) ont besoin d'effets (ou d'actions).

# Idées de consommables que je veux voir dans le jeu :
### Parchemin vierge
Un parchemin qu'un mage peut imprégner d'une magie à utiliser plus tard.
### Parchemin d'enseignement de magie
Un parchemin qu'on peut utiliser pour apprendre une nouvelle magie.
### Parchemin de boule de feu (et autre projectiles élémentaires)
Donc un parchemin pré-imprégné, en gros.
### Potion de soin
La base.
### Potion de poison
C'était un piège !
### "Vaccins"
Quatre potions randomisées qui immunisent plus ou moins bien contre une maladie avec plus ou moins d'effets secondaires.

## Et quelques idées douteuses :
### Parchemin d'enseignement de skill
Vu le peu de skills qu'il y a pour l'instant et la difficulté à les obtenir, c'est probablement une mauvaise idée.
### Potion de mana
Vu qu'il existe les magies économiques, dont la réserve de mana, et que la limite au mana disponible sera utilisée pour empêcher l'utilisation de certains sorts par la plupart des utilisateurs, c'est probablement une mauvaise idée.

## Mais il en faut quand même un peu plus ?
Avoir des consommables, c'est bien ! (C'est moi qui dit ça...)

On pourrait en avoir qui boostent différents trucs temporairement, ou qui jouent sur des méchaniques moins liées aux combats (comme quoi ?).

# Différence potion/parchemin
## La différence de méchanique
Les potions peuvent se boire sans condition. Les parchemins s'activent, avec un coût de mana.
## Et dans l'implémentation ?
On pourrait se contenter de donner des effets moins puissants aux potions, mais il semble logique de plus les distinguer.
Les parchemins sont très liés à la magie (peu/pas utiles/utilisables pour un non-mage).

# L'état actuel des effets et actions
## Effets
### Principe
Les effets sont des éléments fourre-tout qui gèrent les méchaniques du jeu. Les attaques, magies, éléments de support et de santé passent presque tous par des effets.
### Effets existants :
#### Protections
Les protections de groupes, individuelles ou de zone défendent contre les attaques. Un parchemin pourraient être imprégné d'une magie de protection de zone, s'il en existe, mais ça ne fait pas beaucoup de sens. Je verrais plutôt les protections réservées aux tanks.
#### Maladies
Les maladies sont des effets qui se propagent d'agissant en agissant. Il y en a à certains étages qui peuvent menacer le joueur et son groupe.
On pourrait imaginer utiliser une potion de maladie comme projectile pour contaminer des ennemis, mais ce n'est pas dans les méchaniques actuelles du jeu. Qu'est-ce qu'il se passerait si on lançait une potion de soin ? Autre chose ?
La potion de maladie peut aussi être une potion piégée (soit pour pousser agressivement les joueurs à prendre le skill d'observation, soit comme un piège que les joueurs expérimentés éviteront par réflexe, parce qu'ils connaîtront les positions des consommables pièges par coeur).
#### Poison
Le poison tue à petit feu et ne se soigne pas tout seul (contrairement aux maladies), mais il ne se transmet pas non plus.
On pourrait aussi immaginer un effet lorsqu'on lance une potion de poison, sinon c'est purement un piège.
(Puisque certains ennemis (comme les slimes) ramassent certains items, est-ce que le joueur pourrait s'en servir pour les piéger ?)
#### Combustion
Contraîrement au poison qui augmente jusqu'à un certain seuil, les effets de combustion meurent petit-à-petit.
Ils pourraient être d'autres éléments que le feu.
Les flammes se propageront sur certains décors, mais pas d'agissant à agissant.
Ça ne fait pas beaucoup de sens dans une potion, ni dans un parchemin.
#### Soins
La potion de soin est la potion par excellence. Il existe aussi des effets d'immunité, de médicament, d'antidote, etc. pour retirer les effets précédents.
Il serait aussi possible d'envisager une stratégie de porteur sain pour contaminer les ennemis.
C'est là qu'on aura beaucoup de potions.
#### Enseignement
L'apprentissage d'une magie. Il faudra divers parchemins pour les nombreuses magies à collectionner.
#### Dopage
Et tous les effets de renforcement d'une façon générale.
Ça fait un peu plus de sens dans une potion que sur un parchemin, quoique.
#### Instakill
Pour les besoins de la magie du même nom. Il n'a pas sa place dans un consommable.
Pareil pour les effets des magies économiques et les enchantements.
Pareil pour les effets d'attaques (placés sur la victime par l'action d'attaque).
#### Téléportation
Un parchemin de retour pourrait téléporter à un endroit prédéterminé.
À part ça, il s'agit plutôt d'un parchemin portant une magie de téléprotation.
## Actions
### Principe
Les actions sont ce que les agissants font. Utiliser un consommable passera toujours par une action.
### Actions existantes
#### Magies
Un parchemin imprégné peut porter une magie. Toutes les magies du jeu sont disponibles à l'imprégnation.
#### Actions de skills
Les actions qui sont déclenchées par un skill. Ça va de la marche aux attaques en passant par les blocages et les lancers.
Ces actions n'ont pas lieu de se trouver sur un consommable.
#### Placement d'effet
Permet d'utiliser les effets mentionnés précédemment.
#### Imprégnation
Permet d'imprégner (ou de faire imprégner) un parchemin de n'importe quelle magie disponible.

# Conclusion
On a déjà de quoi faire avec les effets existants.
Pour créer certains parchemins il faut spécifier une magie, est-ce qu'on lie le parchemin à une magie correspondante ou on spécifie les paramètres de la magie dans la création du parchemin ?

Donc trois catégories de parchemins : imprégnés, magie, effets.
Uniquement effets pour les potions.
