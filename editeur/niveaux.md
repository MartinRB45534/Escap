# Qu'est-ce qui a obligatoirement des niveaux ?
## Le joueur
Le joueur évolue et progresse en montant de niveau. C'est un peu la base du jeu.
## Les classes et les skills
Les classes et les skills du joueur évoluent avec lui. C'est la classe principale du joueur qui détermine son niveau, et donc ses stats.
#### Bémol :
Qu'en est-il des skills globaux, obtenus en récompense d'accomplissements, et qui se conservent d'une partie à l'autre ?
Avoir des niveaux là-dessus pourrait faire un peu beaucoup.
## Les PNJs
Les PNJs accompagnent, il faut qu'ils évoluent aussi.

# Qu'est-ce qui serait mieux sans niveaux ?
#### Les skills globaux
Déjà mentionné, probablement lourd s'il faut encore les faire monter de niveau pour vraiment terminer le jeu.
## Les items uniques
Certains items (clés, l'objet à voler qui bloque l'un des niveaux de la classe voleur, les éléments de scénario) n'existent qu'en un seul exemplaire.
Avoir des niveaux sur ces items n'aurait pas de sens (quoique ça pourrait se justifier si c'est fait avec soin).
## Les ingrédients
Les ingrédients sont utilisés pour les recettes. Requérir un niveau spécifique d'ingrédient complexifierait beaucoup l'alchimie. Les ingrédients n'ont pas lieu d'avoir des niveaux.
## Certains effets
L'effet de sursis (un item perçant qui peut peut-être continuer sa trajectoire s'il parvient à tuer l'agissant sur sa case) n'a aucune raison d'avoir un niveau.
L'attaque générée par un projectile lors de l'impact pourrait avoir un niveau lié à celui de l'item (si l'item en a un), ou celui du skill utilisé pour lancer le projectile (si le projectile est lancé par un skill), mais aucun des deux n'est complètement satisfaisant. L'attaque devrait juste renvoyer à l'item.
#### À noter :
Ces effets ne sont pas directement créés dans l'éditeur. Ils peuvent rester sans niveau, sans que ce soit incompatible avec une présence complète de niveaux dans le jeu.

# Qu'est-ce qui serait mieux avec niveau, mais peut s'en passer ?
## La plupart des effets
Presque tous les effets sont liés à un skill (attaque, magie, aura), qui a lui-même un niveau.
Ce serait cool que la description de l'effet (avec une observation suffisante) mentionne le skill et son niveau.
## La plupart des items
Certains items sont créés par des skills (skills de génération de projectiles, alchimie) et leurs stats dépendront du niveau du skill. Il est cohérent que l'item ait aussi ce niveau.
Les items non uniques font sens avec un niveau. Le jeu pourrait comprendre peu d'items, mais de niveaux de plus en plus élevés.
## Les agissants
De même que pour les items, avoir des gobelins au niveau, puis au niveau 2, etc. permet sans trop multiplier les ennemis de faire progresser la difficulté du jeu.
#### Alternative :
Pour les agissants comme les items, l'alternative est d'avoir les mêmes ennemis mais sans le lien que leur donneraient le fait d'être juste le même à un autre niveau, ni l'indication de puissance que le niveau implique.
## Les actions
Les actions sont liées à des skills, qui ont des niveaux. Il est cohérent que les actions aient aussi des niveaux.
En réalité les actions (comme les effets) redirigeraient vers le skill associé (avec son niveau).
## Les murs et les cases
Les murs seront plus ou moins difficiles à briser, les cases proteront des auras plus ou moins fortes.
Il sera plus simple de s'y repérer si tout ça a des niveaux.
## Certains décors
Les décors interragissent avec le joueur de diverses façons. Ils occupent une case, peuvent être détruits, certains peuvent affecter le joueur ou lui fournir des items. (Un décors pourrait aussi attaquer en lançant des projectiles, par exemple.)
Tout ça serait mieux avec des niveaux.

# Comment est-ce que je peux avoir des niveaux partout ?
## Question des skills globaux
Je pense qu'on verra plus tard. Ils sont tellements distincts du reste du jeu (et arriveront dans tellement longtemps) qu'on s'occupera de leur cas à part le moment venu.
## Question des clés
Les clés sont un peu à part, mais il y en a beaucoup dans le jeu. On peut leur donner des niveaux (et changer leurs stats (poids, frottement, etc.) en fonction) indépendamment des portes qu'elles ouvrent.
## Question des items uniques
Les items uniques pourraient avoir un niveau. Du point de vue du lore, si il se trouve qu'il n'y a qu'un seul exemplaire de tel objet et qu'il se trouve être au niveau 6, c'est comme ça.
#### Un cas particulier qui me dérange quand même :
Pour la fin liée à la nouvelle Le goût de la vengeance, le joueur doit trouver un livre. Ce serait bizarre que ce livre ait lui aussi un niveau. Qu'est-ce qu'un livre de niveau 1 ? 6 ? 10 ?
#### Et si le livre était un décors ?
Le livre pourrait être posé sur une table, et l'ensemble serait un décors avec lequel le joueur interragirait. Il n'y aurait pas besoin de niveau pour le livre. Mais il faudrait peut-être un niveau pour le décors. Pas parfait mais acceptable s'il y a d'autres tables de niveaux inférieurs précédemment.
## Question des ingrédients
Les ingrédients pourraient avoir un niveau. Certains sont trouvés dans le labyrinthe, d'autres peuvent être achetés (produits par le boss du marchant à partir des cadavres qu'on vend, entre autres). Pour ceux trouvés, je peux fixer le niveaux selon l'étage. Pour ceux transformés, le niveau peut être dépendants du niveau du cadavre. Pour les autres vendus, le marchand pourrait en proposer de chaque niveau.
#### Ça fait un peu beaucoup d'items, là, non ?
En multipliant par 10, ça fait tout de suite beaucoup plus d'items. Pas top.
Comme les items non uniques, on peut essayer de limiter le nombre d'items et jouer sur les niveaux pour apporter une progression. Mais si on compte au moins deux items par espèce (peau et dent comme pour les gobelins), avec seulement ombriul, orc, gobelin, on est déjà à 60 ingrédients différents.
### Quel impact des niveaux sur le gameplay ?
Contrairement aux items uniques qui n'apparaissent qu'à un niveau dans tout le jeu, les ingrédients devront exister en plusieurs exemplaires de chaque niveau. Il faut que ces niveaux aient un impact sur le gameplay.
#### Utilisation distincte ?
Les items pourraient apparaître dans des recettes complètement différentes selon leur niveau. Attention à ce que le joueur ne s'y perde pas. Certaines recettes deviendraient innaccessibles par manque d'ingrédients de bas niveau. Pas top.
#### Remplaçabilité ?
Les items de niveau supérieur pourraient remplacer les items de niveau inférieur. Attention à ne pas les gacher par innatention.
#### Détermine le niveau du produit ?
Le niveau le plus bas parmis les ingrédients pourrait déterminer le niveau du produit de la recette (limité toujours par le niveau du skill d'alchimie ? à moins que le niveau du skill serve uniquement à déterminer les recettes accessibles).
#### Temps de ramassage et de préparation de la recette
Si l'alchimie reste un skill actif, il faudrait qu'elle ait une latence associée. Le niveau des ingrédients pourrait l'impacter. Le niveau des ingrédients impacterait aussi leur temps de ramassage.

# Conclusion
On va donner des niveaux à à peu près tout, et essayer de faire coller le lore.
Au final tout ça n'a d'importance qu'à cause de l'observation, donc c'est peut-être sur ce skill qu'il faut se poser des questions.

### C'est à dire, à peu près tout ?
En vrai pas tant de choses que ça :
 - les agissants ;
 - les skills ;
 - les items permanents ;
 - les décors ;
 - les cases.

Tout le reste n'aura que des références (si il y a lieu) à des objets nivelés.