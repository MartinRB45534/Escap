Dans le système, on va devoir créer deux trucs :

## Les classes

Les classes n'ont d'impact à peu près que chez le joueur (et peut-être sur le comportement du voleur)

### Propriétés des classes :

#### Nom

Chaque classe a un nom.

#### Skills intrasecs

Une classe peut avoir des skills intrasecs. Ces skills peuvent être conditionnés à un niveau de la classe (on ne les a pas si le niveau de la classe est inférieur à la condition).

#### Conditions d'évolution

Utilisé surtout par le joueur et les PNJs humains (et quelques rares monstres évolutifs).
Les conditions d'évolution sont souvent sur la quantité d'xp accumulé par la classe.
Rarement, certaines classes pourraient avoir des conditions différentes (le voleur doit dérober un objet spécifique pour passer un niveau de sa classe ou d'un de ses skills, à décider).

## Les skills

Les skills sont divers et variés, faut-il plus les distinguer ?

### Propriétés des skills :

#### Nom

Chaque skill a un nom.

#### Autres

Les skills ont besoin d'autres propriétés selon ce qu'ils sont.

### Types de skills :

#### Skills intrasecs/skills extra

Il faut faire la distinction pour que les classes soient capables de chosir spécifiquement parmi les intrasecs.

#### Skills passifs/skills actifs

Chaque type particulier de skill est soit actif soit passif, mais pas forcément nécessaire de faire une distinction pour ça.

#### Vision

Chaque agissant devrait en avoir un, en intrasec de sa classe principale. Le skills exact varie probablement d'une espèce à l'autre, peut-être plus.

#### Aura (et auras élémentales)

Les skills d'aura requierent le choix d'un effet associé.

Est-ce que c'est plus compliqué pour les auras élémentales ?

#### Affinité élémentale

Réfléchir à comment la modification d'affinité est calculée. Est-ce que c'est le cadeau d'évolution de l'arbre élémental ? Ou est-ce que le cadeau d'évolution est une modification directe de la stat d'affinité et ces skills sont intrasecs aux classes d'élémentaux ? Ou à la classe d'élémentaliste ?

#### Manipulation d'arme (et de bouclier)

Les skills de manipulation augmentent les effets de l'item associée. Probablement intrasec à la classe associée à l'item ?

#### Écrasement & observation

Important pout les builds associés, mais seul le joueur peut les avoir.

Il faudra peut-être retravailler les mécaniques de priorité pour l'écrasement.

À voir aussi comment l'observation fonctionne exactement.

#### Défense

Il pourrait en exister plusieurs versions (comme pour les items défensifs). L'un d'elles est accessible au joueur (pourquoi pas plusieurs ?) en récompense d'évolution.

#### Magie infinie

Seul le joueur peut l'obtenir ?
À voir comment la perte de PVs causée par les PMs négatifs est calculée.

#### Essence magique et immortalité

Kumoko aura aussi l'essence magique, certains ennemis auront l'immortalité (peut-être en skill intrasec à une classe de mort-vivant ?), et le joueur peut obtenir les deux.

Il faux fixer le taux de conversion PM -> PV pour chaque niveau de l'essence magique, et les taux de réduction des stats pour chaque niveau de l'immortalité.

#### Analyse

L'analyse est-elle un skill passif ou actif ?
Plutôt actif au sens où le joueur fait le choix de l'utiliser en cliquant sur un mot-clé observé.
Plutôt passif au sens où l'analyse ne produit pas d'action (donc pas de latence, par exemple).

Comment calculer les niveaux de récursion (une fois que la récursion devient possible) ?

#### Déplacement

Chaque agissant devrait en avoir un, en intrasec de sa classe principale.

#### Ramasse

Seul le joueur l'a ? Les slimes ont quelque-chose d'équivalent mais c'est les seuls à interragir avec les items, non ?

En tous cas, il faut définir la durée de ramassage par item.

#### Attaques

Permet d'attaquer.

Peut proposer plusieurs formes d'attaque (certaines conditionnées à un niveau du skill).

Certaines formes (potentiellement toutes) peuvent être conditionnées à la possession d'une arme spécifique (lance ou épée).

Pour les controles, il sera utile de lier une même touche à plusieurs formes si elles utilisent des armes différentes (facilite le changement d'arme). Est-ce qu'il ne s'agirait pas dans certains cas d'une même forme avec des effets différents selon l'arme ?
Est-ce qu'il est même possible d'obtenir les techniques de lance et d'épée dans une même run ?

Touches conditionnées à l'arme -> À réfléchir plutôt pour les touches que pour les skills.

#### Blocage

Permet d'utiliser un bouclier pour se protéger.

Le joueur est probablement le seul à faire ça.

Propose plusieurs formes de protection conditionnées au niveau du skill.

#### Magie

Beaucoup d'agissants en ont un.

Quel impact du skill ?
Son niveau décide du niveau des magies lancées.
Le skill stocke aussi les magies disponibles.
Autre chose ?

Est-ce qu'il existe un unique skill de magie, et les magies sont attribuées par agissant ?
Ou le skill de magie décide des magies disponibles (éventuellement conditionnées au niveau du skill) ?
Aucun impact sur le jeu je crois, mais ça change la façon de le créer.

#### Vols, lancer

Des skills utiles uniquement pour le build associé.

Il faudra voir comment calculer les succès des skills de vol en fonction de la priorité.

Il y aura aussi quelques paramètres nécessaires pour le lancer.

Des décors pourraient lancer des projectiles (façon piège, avec déclenchement conditionnel, ou en continu). Est-ce que ça a un rapport avec les skills ? Comment gérer ?

#### Alchimie, vente & achat

Des skills spécifiques à des PNJs. Seul ces PNJs peuvent les obtenir.

Pour l'alchimie, le niveau du skill détermine le niveau des items créés ?
Le skill aura besoin des recettes en paramètres.

Pour la vente et l'achat, le niveau du skill n'impacte rien ?
Le skill aura besoin des prix des items.

Il faut faire les skills avant les agissants, mais :
 - la vente/achat inclue les cadavres d'agissants (uniquement les non-humains ?) ;
 - les cadavres de monstres sont changés (hors du labyrinthe) en ingrédients ;
 - l'alchimie utilise les ingrédients dans les recettes.

Définir les prix, dépecages et recettes après les agissants ?

Définir les ingrédients en même temps que les items et les prix et dépecages dans les agissants ?

Est-ce que tous les gobelins se vendent/depecent pareil ? (Et idem pour les autres espèces.)

Comment faire pour les 3 ombriuls qui ont une autre espèce ? Pour les espèces mélangées de façon générale ?

À voir...

Des décors peuvent aussi faire de l'alchimie (proposent une liste de recette). Les décors ont un niveau qui détermine le niveau de l'item créé.

#### Skills raciaux

Merge, absorb, divide sont spécifiques aux slimes. Les taractects devront aussi avoir des skills spécifiques.

### Mélanger les types de skills

Est-ce qu'un skill pourrait avoir simultanément des effets passifs et actifs ?

Exemple : les manipulations d'arme pourraient contenir à la fois les boosts passifs à la manipulation et les attaques.

#### Pour

Regrouper les effets (passifs et actifs) relatif à un même sujet (les armes dans l'exemple) au même endroit.

Moins de noms à trouver.

#### Contre

Moins de skills à améliorer, expérience plus monotone.

Les classes sont déjà là pour regrouper les skills similaires.
