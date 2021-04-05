Work in progress !

Attention /!\ les pnjs peuvent bloquer le joueur en essayant d'aller vers lui lorsqu'ils sont trop nombreux et que le joueur doit faire demi-tour !

Est-ce que les gens sont blessés par leur propre stomp !? Le mystère du mage gobelin...
La variable globale ID_MAX ne remplit pas du tout son rôle ! Qu'est-ce que je fais ?
L'autruche, en codant les pnjs




Pour la magie, la régénération est ce qui détermine la véritable puissance. Les pm max correspondent juste à une limitation sur les sorts qu'on peut utiliser, et sur le nombre de sorts qu'on peut balancer d'affilée au début de la confrontation. Modifier les stats en conséquence.



Objectif courant : recréer le tutoriel
- PNJs
- Interractions PNJs-joueur
- Monstres
- Layout
Au passage :
- Fin du travail sur l'affichage (arbre élémental)
- Rendre fonctionnels tous les choix, puis les conditionner

Si j'ai le temps :
- Créer les premiers monstres (le tutoriel est un camp de gobelins)
- Faire de meilleurs skins pour les gobelins.



Quelques nouvelles magies à créer :
- Magies tribales (genre, qui varient selon l'espèce, comme un coup de poing magique qui n'est pas le même pour les gobelins et les orcs)
- Coup de poing magique (magie d'attaque des mages de combat)
- Boost complet (un boost qui affecte toutes les stats)
- Purification (la magie anti-monstres de la peste)


Étage combat : trois sentinelles aux trois points de passage
Étage monstres : une sentinelle, un gobelin de base, un mage, deux guerriers, dans un dédale
Étage portes (prison) : sentinelles, guerrier de plus haut niveau dans une salle (c'est un piège !), quelques monstres capturés ?
Étage potions : guerriers, mages, un shaman, deux guerriers de plus haut niveau.
Étage meutes : guerriers, mages, deux shamans, plein de gobelins de base dans les couloirs.
Étage magie : tout !
Étage items : tout, mais un peu moins, plus quelques gobelins équippés.
Étage boss : tout, mais un peu plus, plus un chef gobelin.


Équippements du tutoriel :
Armures (bloque 20%, réduit les dégats de 20, réduit les dégats à 20, annule les attaques de moins de 20 mais laisse passer les autres... pas toutes mais deux ou trois)
Armes (épée, lance, autre (une arme peut-être plus forte mais avec moins de skills de boosts évidemment))
Casques (comme les armures, + bandeau ou quelque chose, qui boost le mana)
Anneaux (plein d'effets possibles !)
Bouclier (sauf qu'il faut un skill pour s'en servir... peut-être un bouclier avec un effet passif semblable aux armures ?)


À l'occasion, faire le tri dans les constantes


Messages d'entrée pour certains étages ?

Idée : l'une des améliorations des flèches, voire de tous le projectiles pourrait consister à les faire traverser les alliés sans les toucher


Idées de lore à disperser dans les niveaux :

"Nombreux sont ceux qui pensent que la voie de la magie est aussi la voie de la connaissance. Mais la magie est avant tout la voie de l'imagination, du refus de la réalité."
pour guider les joueurs qui ont pris le hint de Dev vers la voie de la connaissance, donc avant la première montée de niveau.

"Les attribus élémentaires sont un sujet complexe et mystérieux. Prenons l'exemple des maladies :
   - Les maladies sont un instrument de mort. Dans le labyrinthe, où voir ses ennemis peut faire toute la différence, la mort est associée à l'ombre. On pourrait donc penser que les maladies sont associées à l'élément ombre.
   - Mais les maladies se propagent par le biais de virus, qui sont une forme de vie. Invoquer une maladie revient donc à créer la vie, et dans le labyrinthe, la vie est associée à l'élément terre.
   - Le caractère contagieux, presque éruptif des maladies les lient au contraire à l'élément feu.
   - Mais la lente agonie que causent certaines maladies n'est pas sans rappeler l'engourdissement de la magie de congélation, liée à l'élément glace.
En réalité, l'affinité élémentale des maladies dépend de la maladie en question, mais aussi parfois du mage responsable de son apparition. Bien malin qui peut dire, sans l'avoir observé, à quel élément est rattaché tel ou tel phénomène."
pour informer les joueurs sur les maladies, et indiquer que l'observation permet de connaitre l'affinité de quelquechose.


Notes de trucs à améliorer :
- Réglage du nombre de tours par seconde. Please.
- Allonger les temps pour les magies à choix de coût.


À réflechir sérieusement :
- Il serait bien de ne pas faire reposer tout le développement de personnage sur les choix des montées de niveau (les arbres). En particulier, le joueur doit pouvoir progresser après avoir atteint le niveau 10.
- Les sous-classes obtenues à la fin vont bien-sûr ce développer plus tardivement, et permettre au joueur de continuer à se développer (mais sans changer d'orientation, puisqu'il ne peut plus faire de choix).
- Le joueur peut aussi se développer grâce aux objets qu'il trouve (exemple : le personnage de type Tank, qui progresse en remplaçant son armure par une nouvelle plus forte).
- Risque : un joueur centré sur la magie peut récupérer une armure destinée à un joueur de type défensif, et obtenir une très bonne défense qui déséquilibre son personnage (et le rend trop fort).
- Contre-mesure : modifier les items disponibles en fonction des choix du joueur ;
- Mais : je n'ai pas envie de faire ça comme ça, et ces items peuvent servir aux compagnons du joueur.
- Autre contre-mesure : un joueur qui n'a pas choisi le skill Lancer ne pourra jamais rien faire d'utile avec une flèche. Cette contre-mesure est dificilement applicable au port d'armures.
- Aussi : un sort, aussi puissant soit-il, ne sert à rien si on n'a pas suffisament de mana pour le lancer. /!\ Faire attention à ce que l'on peut ou ne peut pas obtenir à l'aide d'objets.
- Je suis en mesure de créer des zones qui refusent tel ou tel type d'agissant, y compris sur des critères de classes. Mais le joueur avec une construction centrée sur l'observation doit pouvoir tout explorer, donc pas de loots distincts.
- Attention aussi au voleur, qui pourra récupérer beaucoup d'objets différends. En même temps, c'est sa façon de gagner. Faire de la capacité à voir et collecter les objets une stratégie à part entière ?
- Idée : certains objets sont nécessaires à l'évolution de certaines classes ou skills. Par exemple, un objet possédé par l'un des humains du jeu est nécessaire au développement d'un voleur.
- Aussi : avoir monté une classe à un certain niveau, ou posséder un certain objet est une condition de déverouillage d'un choix de la classe principale.
- Ou encore : passer telle classe du niveau x au niveau y est un des choix de la classe principale.
- Sauf qu'il faut arriver au bon niveau de la classe principale au bon moment, peu probable. Une dépendance à des objets uniques rend le jeu impossible pour un non-initié, et les objets utiles à une autre construction de personnage sont déjà suffisament ennuyeux en un seul exemplaire.
- Certaines classes ne peuvent pas se reposer non plus sur leurs alliés humains. Tout ça fait beaucoup d'interdépendances des éléments du jeu à gérer, mais c'est ce qui le rend marrant !


Garder une trace du code couleur, pour faciliter les modifications futures.




Fonctionnement des dialogues/interractions :
Du point de vue d'un joueur, les pnjs ont un dialogue par défaut (si le joueur les accoste sans raison) et des dialogues conditionnés (indiqués par un ! ou ? au dessus de leur tête).

Quelques objets/skills obtenus dans des quètes :
- La carte. Permet de consulter la vue de l'esprit (donc de tous les alliés) en mettant le jeu en pause.
- La thélépathie. Permet de déclencher un dialogue avec un pnj qui n'est pas sur une case voisine.
- La concentration de bataille. Quand elle est activée, le jeu se déroule en tour par tour (au sens où le joueur doit "terminer le tour" pour passer au suivant.
En combinant les trois, le joueur peut donner des ordres plus précis aux pnjs ("déplace-toi d'une case à gauche" ou "utilise tel sort sur tel ennemi", au lieu de "suis-moi", "fuit", "combat" etc. où les détails sont gérés par l'esprit)
