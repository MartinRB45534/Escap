À l'attention du joueur :

Escap version 0 : le tutoriel

Quelques petites remarques :
1 - Le jeu s'arrête avant la fin du tutoriel, au moment de vaincre le boss gobelin à  l'étage 10. Il n'y a pas encore de moyen d'ouvrir la porte de l'étage 10, mais le boss dropera la clé quand j'aurai codé les monstres derrière la porte.
2 - Le jeu est TRÈS déséquilibré ! J'apprécie beaucoup les retours, et l'équilibrage peut être modifié (voir plus bas).
3 - Désolé pour les graphismes, je vais sûrement les améliorer mais j'ai la flemme pour l'instant.
4 - Il reste quelques bugs dans le jeu. Je ne crois pas qu'il y ait de situation qui fasse planter le programme à l'heure actuelle, mais on peut se retrouver bloqué. Par exemple :
	- Si deux agissants s'affrontent et que chacun subit moins de dégats qu'il ne récupère de PV (les humains sont les seuls, avec le boss de fin, à récupérer des PVs donc ça devrait aller).
	- Si un agissant avec peu de PVs s'enfuit (ça devrait moins arriver avec les limitations que j'ai placées sur la fuite, mais c'est toujours plus pratique d'attaquer à 2 pour encercler).
	- Si le joueur est dans une impasse avec tous les PNJs derrière lui (les PNJs sont codés pour rester à une certaine distance du joueur, donc le plus loin refuserait de s'éloigner et tout le monde serait immobilisé) (on peut facilement éviter ça en demandant aux PNJs de suivre un autre PNJ qui lui suit le joueur, mais c'est plus difficile de vérifier qui s'est perdu et en cas de mort du PNJ suivi on risque de perdre les autres PNJs).
	- Si un agissant de type Sentinelle s'arrète sur l'escalier. Typiquement, un des gardes du boss. Sans humain dans la salle du boss, impossible de le faire bouger, et l'escalier restera condamné à jamais.
    La meilleure solution dans ce cas est de considérer ça comme une défaite et de recommencer, mais on peut aussi modifier le jeu (voir plus bas).
5 - Certaines commandes ne sont pas expliqués. A et E pour entrer et sortir d'un item d'un menu (pendant le jeu), ZQSD pour haut droite bas gauche dans ces même menus, et espace pour utiliser l'item de menu courant. Typiquement, Q pour passer de la zone centrale à la zone de gauche (un pourtour rouge indique la zone courante), puis A pour entrer dans la zone de gauche et Z/S pour séléctionner l'inventaire/la classe principale, puis A pour entrer dans l'inventaire/la classe principale, de nouveau Z, S, A et E pour naviguer dans l'inventaire/la classe principale et enfin espace pour équipper l'item séléctionné/boire la potion séléctionnée/lancer le projectile séléctionné (pas encore de projectiles à ce niveau)/utiliser le skill séléctionné (utile quand un skill s'utilise deux fois d'affilée par les moyens normaux). Attention, les zones ne sont pas toutes codées et se déplacer ou sortir d'une zone non codée fait planter le jeu, donc se limiter aux skills et items est une bonne pratique.
6 - Le ramassage des objets n'est pas automatique. C'est une action dont la commande est expliquée en temps voulu. Cette action prend un certain temps pour chaque objet à ramasser, et ramasse tous les objets sur la case. De plus les cadavres de monstres, comme chaque pièce de leur équippements, sont des objets, donc tuer plusieurs monstres sur la même case puis récupérer la clée lachée par le dernier peut prendre pas mal de temps et donner l'impression que le jeu ne répond plus. Il suffit d'être patient et de ne pas se faire attaquer par d'autres monstres au même moment.
7 - Les commandes sont expliquées au fur et à mesure qu'elles deviennent utiles, par les PNJs. Pour modifier ces commandes et/ou se les remettre en mémoire, appuyer sur la touche retour/entrée.

Pour aller plus loin :

Modifier l'équilibrage
Tout est dans Jeu/Systeme. Le fichier Constantes_stats.py contient un dictionnaire avec les stats de base de chaque agissant, ainsi que son équippement et ses magies. Les skills sont créés dans le fichier Classe.py, dans la fonction __init__ de la Classe_principale, mais je vais probablement les déplacer dans le fichier Constantes_stats à l'occasion.
Les dossiers Constantes_items, Constantes_magies, Constantes_skills contiennent les stats pour les items, les magies, et les skills respectivement. La vitesse des frames se modifie dans la fonction attend (ou peut-être affiche ?) du fichier True_main, un pygame.wait() quelque part. Ces deux fichiers et trois dossiers devraient contenir toutes les valeur numériques actuellement utilisées par le jeu.

Débloquer une situation
Première étape : Controle + C dans le shell pour interrompre l'exécution.
Deuxième étape : depuis le shell, mains est une variable globale qui liste tous les objets Main en cours d'utilisation (les fichiers .p dans le répertoire à la dernière vérification). s'il y a un seul Main, mains[0][2] y accédera. Le controleur de la partie interrompue sauvagement devrait être mains[0][2].controleur, et le controleur donne accès à tous les éléments du jeu. Quelques exemple :
	- mains[0][2].controleur.entitees[2] est le joueur, donc :
	- mains[0][2].controleur.entitees[2].pv = 100 pour remettre les pvs du joueur à 100 , ou
	- mains[0][2].controleur.entitees[2].position = ('Étage 10 : Boss',0,0) pour déplacer le joueur à l'étage du boss, dans le coin en haut à droite
	les ID de 1 à 10 sont réservées aux humains, donc elles sont fixes, pour les autre :
	- mains[0][2].controleur.entitees donne le dictionnaire de toutes les entitees, (agissants et items) classées par ID, ensuite, c'est de l'essai erreur pour trouver la bonne
	- mains[0][2].controleur.labs donne le dictionnaire de tous les labyrinthes (~= étages pour l'instant) classés par nom, ce qui aide pour la première coordonnée des positions
	- mains[0][2].controleur.esprits donne le dictionnaire des esprits, et :
	- mains[0][2].controleur.entitees[ID].esprit donne le nom de l'esprit de l'entitée correspondant à ID, donc :
	- mains[0][2].controleur.esprits[mains[0][2].controleur.entitees[ID].esprit].ennemis pour le dictionnaire des ennemis de l'esprit de l'entitée correspondant à ID
	- mains[0][2].controleur.labs[mains[0][2].controleur.entitees[ID].position[0]].matrice_cases[mains[0][2].controleur.entitees[ID].position[1]][mains[0][2].controleur.entitees[ID].position[2]].murs[mains[0][2].controleur.entitees[ID].dir_regard].effets donnerai la liste des effets du mur juste en face de l'entitée correspondant à ID (probablement un Teleport qui conduit à la case voisine et éventuellement un Mur ou une Porte qui bloque le passage)
	- mains[0][2].controleur.entitees_courantes pour la liste des IDs des entitées en activité, et
	- mains[0][2].controleur.labs_courants pour la liste des noms des labyrinthe actifs
Honnêtement la modification de position est la seule chose utile de ce que je viens de citer, dès qu'on commence à ramener des entitees à la vie ça s'appelle tricher... Attention quand même quand on se rend dans un étage inactif, penser à l'activer ou toute interraction avec l'environnement (les monstres ou les humains, par exemple) fera planter le jeu (prendre l'escalier pour sortir de l'étage et y revenir réactive l'étage, sinon mains[0][2].controleur.active_lab(nom_du_lab_à_activer) en remplaçant nom_du_lab_à_activer par le nom du labyrinthe à activer.
Si le controleur (la "partie") n'est pas sur le premier Main de la liste, il faut remplacer le 0 dans mains[0][2] par l'indice du Main (bonne indication : quand mains[0][2].controleur renvoie None, c'est qu'on est pas sur le bon Main).
Troisième étape : mains[0][2].boucle() et le jeu reprend immédiatement, attention aux surprises quand l'affichage se met à jour pour prendre en compte les nouvelles modifications !














À mon attention :

En cours (alchimiste) :
- Parchemins imprégnés de magie (fait)
- Parchemins divers
- Potions de soin (un peu redondant avec la peste et les parchemins impregnés par la peste)
- Potions de boost (un peu redondant avec la peureuse et les parchemins impregnés par la peureuse)
- Potions de vitesse (vraiment utile ? tout le monde se plaint d'aller trop vite)
- Potions diverses
- Ingrédients (y compris les corps de monstres ?)
- Identification d'objets (via un skill d'observation ?) (le joueur 'mémorise' l'identification ?)
- Magie de sauvegarde temporelle
- Magie de réactivation de la sauvegarde
- Magies diverses
- Monétisation


Travail à faire :
- Layout (prison, dialogues)
  Prison :
    - Petite salle avec une porte, clé obtenue par dialogue
    - Petite salle avec deux portes, une clé sur le sol
    - Couloir, deux sentinelles avec un passe-partout
    - Salles actuelles (plus d'innaccessibles)
    - Fin du couloir, escalier et salle du petit-ami (dialogue pour obtenir la clé ?)
  Cuisine :
    - Salle avec le PNJ, une porte et des portails
    - "Dédale" de portails, avec quelques gobelins, des potions/parchemins/ingrédients et la clé
    - Grande salle , avec quelques gobelins et un shaman (des marmites ? pour introduire la notions d'objets inamovibles)
- Création (ombriuls)
(- Modifier la fuite pour ne fuir que si un allié est accessible)
- Équilibrer ! (tours par secondes, combats, jeter un oeil à l'XP obtenu)





Retours expérience Clément :
Pour l'équilibrage : premiers monstres one/two-shot, puis progression (créer des monstres spécialement affaiblis pour le tutoriel ? il faut que je le fasse pour le slime de toute façon)
Potions : pour quoi faire ? Permanent/non permanent, affecte le joueur/les ennemis... Peut-être la portée
Archer (impossible, mais des mages qui attaquent à distance, c'est faisable. pour remplacer les mages actuels qui sont vraiment faibles ? comment repérer facilement qui est responsable d'une attaque ? un seul mage par étage, par exemple ?)
Plus d'accompagnement du joueur, plus d'explications. Diminuer la difficulté. C'est juste un tutoriel !






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
