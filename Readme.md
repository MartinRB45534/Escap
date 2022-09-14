� l'attention du joueur :

Escap version 0 : le tutoriel

Quelques petites remarques :
1 - Le jeu s'arr�te avant la fin du tutoriel, au moment de vaincre le boss gobelin �  l'�tage 10. Il n'y a pas encore de moyen d'ouvrir la porte de l'�tage 10, mais le boss dropera la cl� quand j'aurai cod� les monstres derri�re la porte.
2 - Le jeu est TR�S d�s�quilibr� ! J'appr�cie beaucoup les retours, et l'�quilibrage peut �tre modifi� (voir plus bas).
3 - D�sol� pour les graphismes, je vais s�rement les am�liorer mais j'ai la flemme pour l'instant.
4 - Il reste quelques bugs dans le jeu. Je ne crois pas qu'il y ait de situation qui fasse planter le programme � l'heure actuelle, mais on peut se retrouv� bloqu�. Par exemple :
	- Si deux agissants s'affrontent et que chacun subit moins de d�gats qu'il ne r�cup�re de PV (les humains sont les seuls, avec le boss de fin, � r�cup�rer des PVs donc �a devrait aller).
	- Si un agissant avec peu de PVs s'enfuit (�a devrait moins arriver avec les limitations que j'ai plac�es sur la fuite, mais c'est toujours plus pratique d'attaquer � 2 pour encercler).
	- Si le joueur est dans une impasse avec tous les PNJs derri�re lui (les PNJs sont cod�s pour rester � une certaine distance du joueur, donc le plus loin refuserait de s'�loigner et tout le monde serait immobilis�) (on peut facilement �viter �a en demandant aux PNJs de suivre un autre PNJ qui lui suit le joueur, mais c'est plus difficile de v�rifier qui s'est perdu et en cas de mort du PNJ suivi on risque de perdre les autres PNJs).
	- Si un agissant de type Sentinelle s'arr�te sur l'escalier. Typiquement, un des gardes du boss. Sans humain dans la salle du boss, impossible de le faire bouger, et l'escalier restera condamn� � jamais.
    La meilleure solution dans ce cas est de consid�rer �a comme une d�faite et de recommencer, mais on peut aussi modifier le jeu (voir plus bas).
5 - Certaines commandes ne sont pas expliqu�s. A et E pour entrer et sortir d'un item d'un menu (pendant le jeu), ZQSD pour haut droite bas gauche dans ces m�me menus, et espace pour utiliser l'item de menu courant. Typiquement, Q pour passer de la zone centrale � la zone de gauche (un pourtour rouge indique la zone courante), puis A pour entrer dans la zone de gauche et Z/S pour s�l�ctionner l'inventaire/la classe principale, puis A pour entrer dans l'inventaire/la classe principale, de nouveau Z, S, A et E pour naviguer dans l'inventaire/la classe principale et enfin espace pour �quipper l'item s�l�ctionn�/boire la potion s�l�ctionn�e/lancer le projectile s�l�ctionn� (pas encore de projectiles � ce niveau)/utiliser le skill s�l�ctionn� (utile quand un skill s'utilise deux fois d'affil�e par les moyens normaux). Attention, les zones ne sont pas toutes cod�es et se d�placer ou sortir d'une zone non cod�e fait planter le jeu, donc se limiter aux skills et items est une bonne pratique.
6 - Le ramassage des objets n'est pas automatique. C'est une action dont la commande est expliqu�e en temps voulu. Cette action prend un certain temps pour chaque objet � ramasser, et ramasse tous les objets sur la case. De plus les cadavres de monstres, comme chaque pi�ce de leur �quippements, sont des objets, donc tuer plusieurs monstres sur la m�me case puis r�cup�rer la cl�e lach�e par le dernier peut prendre pas mal de temps et donner l'impression que le jeu ne r�pond plus. Il suffit d'�tre patient et de ne pas se faire attaquer par d'autres monstres au m�me moment.
7 - Les commandes sont expliqu�es au fur et � mesure qu'elles deviennent utiles, par les PNJs. Pour modifier ces commandes et/ou se les remettre en m�moire, appuyer sur la touche retour/entr�e.

Pour aller plus loin :

Modifier l'�quilibrage
Tout est dans Jeu/Systeme. Le fichier Constantes_stats.py contient un dictionnaire avec les stats de base de chaque agissant, ainsi que son �quippement et ses magies. Les skills sont cr��s dans le fichier Classe.py, dans la fonction __init__ de la Classe_principale, mais je vais probablement les d�placer dans le fichier Constantes_stats � l'occasion.
Les dossiers Constantes_items, Constantes_magies, Constantes_skills contiennent les stats pour les items, les magies, et les skills respectivement. La vitesse des frames se modifie dans la fonction attend (ou peut-�tre affiche ?) du fichier True_main, un pygame.wait() quelque part. Ces deux fichiers et trois dossiers devraient contenir toutes les valeur num�riques actuellement utilis�es par le jeu.

D�bloquer une situation
Premi�re �tape : Controle + C dans le shell pour interrompre l'ex�cution.
Deuxi�me �tape : depuis le shell, mains est une variable globale qui liste tous les objets Main en cours d'utilisation (les fichiers .p dans le r�pertoire � la derni�re v�rification). s'il y a un seul Main, mains[0][2] y acc�dera. Le controleur de la partie interrompue sauvagement devrait �tre mains[0][2].controleur, et le controleur donne acc�s � tous les �l�ments du jeu. Quelques exemple :
	- mains[0][2].controleur[2] est le joueur, donc :
	- mains[0][2].controleur[2].pv = 100 pour remettre les pvs du joueur � 100 , ou
	- mains[0][2].controleur[2].position = ('�tage 10 : Boss',0,0) pour d�placer le joueur � l'�tage du boss, dans le coin en haut � droite
	les ID de 1 � 10 sont r�serv�es aux humains, donc elles sont fixes, pour les autre :
	- mains[0][2].controleur.entitees donne le dictionnaire de toutes les entitees, (agissants et items) class�es par ID, ensuite, c'est de l'essai erreur pour trouver la bonne
	- mains[0][2].controleur.labs donne le dictionnaire de tous les labyrinthes (~= �tages pour l'instant) class�s par nom, ce qui aide pour la premi�re coordonn�e des positions
	- mains[0][2].controleur.esprits donne le dictionnaire des esprits, et :
	- mains[0][2].controleur[ID].esprit donne le nom de l'esprit de l'entit�e correspondant � ID, donc :
	- mains[0][2].controleur.esprits[mains[0][2].controleur[ID].esprit].ennemis pour le dictionnaire des ennemis de l'esprit de l'entit�e correspondant � l'identifiant ID
	- mains[0][2].controleur[mains[0][2].controleur[ID].position,mains[0][2].controleur[ID].dir_regard].effets donnerai la liste des effets du mur juste en face de l'entit�e correspondant � l'identifiant ID (probablement un Teleport qui conduit � la case voisine et �ventuellement un Mur ou une Porte qui bloque le passage)
	- mains[0][2].controleur.entitees_courantes pour la liste des IDs des entit�es en activit�, et
	- mains[0][2].controleur.labs_courants pour la liste des noms des labyrinthe actifs
Honn�tement la modification de position est la seule chose utile de ce que je viens de citer, d�s qu'on commence � ramener des entitees � la vie �a s'appelle tricher... Attention quand m�me quand on se rend dans un �tage inactif, penser � l'activer ou toute interraction avec l'environnement (les monstres ou les humains, par exemple) fera planter le jeu (prendre l'escalier pour sortir de l'�tage et y revenir r�active l'�tage, sinon mains[0][2].controleur.active_lab(nom_du_lab_�_activer) en rempla�ant nom_du_lab_�_activer par le nom du labyrinthe � activer.
Si le controleur (la "partie") n'est pas sur le premier Main de la liste, il faut remplacer le 0 dans mains[0][2] par l'indice du Main (bonne indication : quand mains[0][2].controleur renvoie None, c'est qu'on est pas sur le bon Main).
Troisi�me �tape : mains[0][2].boucle() et le jeu reprend imm�diatement, attention aux surprises quand l'affichage se met � jour pour prendre en compte les nouvelles modifications !














À mon attention :


TODO (pour ne pas oublier les problèmes que je découvre) :
 - Dialogues (consignes obsolètes, ingrédients et potions, ramassage complet)
 - On peut scroller une liste qui n'occupe pas toute la longueur de son contenant... (Vraiment bizarre...)
 - Ajouter un "message" lorsqu'on reçoit un item ! (Ou quand on ramasse.)
 - La vignette d'agissant ne se met pas à jour (barre de PV, direction, statuts) (corrigé, à vérifier)
 - Lorsqu'un humain quite la liste des neutres (en rejoignant le joueur), les éventuels autres agissants de la liste des neutres ne remontent pas au sommet (à la fois c'est cohérent, puisqu'ils gardent leur position, et en même temps bizarre visuellement) (corrigé, à vérifier)
 - Labyrinthe de sélection de la case pour "Tu vois là-bas ?" a le labyrinthe de jeu habituel en fond (mais pourquoi !?)
 - Validation de la sélection de la case pour "Tu vois là-bas ?" ne passe pas à la suite du dialogue





Comment insérer des variables dans les dialogues (touches, noms, etc.) ? Tant que j'y suis, comment gérer plusieurs langues ?




Concernant les PNJs, les monstres, le rôle du joueur :

L'objectif final est de sortir, il y a plusieurs chemins pour ça. Combattre n'est pas la seule option.
Options (je crois qu'elle sont détaillées autre part dans ce fichier) :
 - chemins dérobés (portes cachées et portails inter-étages qui mènent à la sortie du tutoriel, le joueur a besoin de scruter minutieusement chaque détail, d'un skill d'observation, de voir au travers des murs, d'items cachés, il peut accéder à des parties du labyrinthe qui sont d'ordinaire innaccessibles, récupérer des items dans des étages supérieurs pour vaincre des monstres dans des étages inférieurs)
 - fin cinématique (livre secret qui débloque la "vraie" fin (un peu trop semblable à l'option précédente, à retravailler))
 - destruction des murs (skill d'écrasement pour contourner le boss final et accéder à la sortie)
 - vol (skill de vol et skills associés pour dérober la clé de la dernière porte au boss final)
 - combat (différentes façon de combattre pour tuer le boss final et récupérer la clé de la dernière porte)

Deux sorties (dans le tutoriel, et à l'étage 100) en plus du livre secret.
La sortie du tutoriel et le livre sont cachés et difficiles d'accès.
La sortie de l'étage 100 est protégée par une porte.
La porte peut être détruite par le skill d'écrasement au niveau max, avec l'augmentation de priorité au niveau max.
Le boss final détient la clé le porte.
La clé peut lui être volée avec le skill de vol au niveau max, avec l'augmentation de priorité au niveau max.
Le boss final peut être tué pour récupérer la clé.
Les PNJs au niveau max sans le joueur ne peuvent en aucun cas vaincre le boss final (et l'atteindraient de toute façon difficilement tous en vie).
Comment s'assurer que chaque option est exclusive (i.e. le joueur ne peut pas partir sur un build écrasement et tuer le boss final) ? À voir.

Pour l'option combat :
Le joueur peut difficilement se passer des PNJs. Les PNJs peuvent à peu près se passer du joueur (en tout cas dans les étages inférieurs, la méchanique s'inverse ensuite).
Les PNJs consistuent un groupe où chaque rôle est utile.
Ces rôles sont :
 - DPS (tue les ennemis en leur infligeant des dégats), CàC et distance
 - tank (protège ses alliés en bloquant/recevant les attaques)
 - soutien (aide ses alliés de diverses façons)
 - soigneur (empêche ses alliés de mourir)
Il faut que chaque rôle soit important, c'est à dire qu'à nombre de membres égal, un groupe auquel il manque un rôle soit plus faible.
Mais il ne faut pas que la mort d'un seul PNJ dans les étages inférieurs guarantisse la défaite. Il y a déjà une certaine redondance dans le groupe :
 - 4 DPS avec le réceptionniste, l'encombrant, l'alchimiste (moins DPS que les autres mais quand même), la bombe atomique, mais le paumé et le marchand peuvent infliger quelques dégats aussi
 - 1 tank avec le paumé, mais le réceptionniste, l'encombrant et le marchand peuvent tanker un peu aussi
 - 1 soutien avec la peureuse, mais l'alchimiste et la peste peuvent au besoin soutenir un peu aussi, une fois qu'ils ont gagné quelques niveaux
 - 1 soigneur avec la peste, mais la peureuse et l'alchimiste peuvent au besoin soigner un peu aussi, une fois qu'ils ont gagné quelques niveaux
 - le marchand est particulièrement versatile avec son équipement changeant et peut s'adapter à la situation
 - le joueur, selon le build qu'il choisit, peut facilement tenir deux rôles à la fois (soutien + soin avec l'ange, soutien + DPS avec l'épéiste enchanteur, DPS + tank avec l'épéiste classique) ou un rôle avec une grande efficacité (pur DPS avec le lancier, l'archer ou la mage offensif).

Le joueur peut aussi se débrouiller seul (build nécromancien par exemple) mais c'est bien plus difficile dans les étages inférieurs.

Comment s'assurer que chaque rôle est nécessaire :
 - DPS : diminuer les dégats des autres rôles (déjà fait)
 - tank : bonne défense + bonne concentration des attaques ennemies (comment exactement ?)
 - soutien et soigneur : aide efficace là ou c'est nécessaire (plus ou moins déjà fait)

Pour le tank, idées de skills :
 - provocation (augmentation de l'importance aux yeux des ennemis) pour s'attirer les attaques
 - protection de zone (avec un bouclier ? ou laisser le bouclier uniquement pour le build correspondant du joueur ? peut-être un peu difficile de faire controler le bouclier intelligement par une IA de toute façon)
 - transmission de dégats (peut-être plus une magie qu'un skill, les dégats sont infligés au tank plutôt qu'aux autres, ce qui est avantageux si le tank a une plus grande affinité élémentaire)
 - transmission d'attaque (là aussi, peut-être plus une magie qu'un skill, les attaques sur les agissants protégés sont déplacées sur le tank, qui a une meilleure défense du fait de ses skills/équippements)
 - peut-être aussi un peu de CC (déplacement forcé, stun, immobilisation)





Jeter un oeil aux phases du controleur, il y a peut-être des trucs à retravailler

Phases :
TOUR - la phase ou le joueur joue 'normalement' (je me comprends)
DIALOGUE - lors des discussions (acutellement pas une phase)
TOUCHE - modification des touches (inclure dans un menu, genre paramètres, avec les réglages de son, vitesse, etc. ?)
LEVEL_UP - sélection du bonus de montée de niveau
RECETTE - sélection d'une recette d'alchimie (alchimiste ou chaudron)
MARCHAND - achat-vente auprès d'un marchand
IMPREGNATION - imprégnation d'un parchemin vierge
AGISSANT_DIALOGUE
CASE_DIALOGUE
AGISSANT_MAGIE
CASE_MAGIE
DIRECTION_MAGIE
COUT_MAGIE
AGISSANT_PARCHEMIN
CASE_PARCHEMIN
DIRECTION_PARCHEMIN
COUT_PARCHEMIN
CINEMATIQUE - pour plus tard



COMPLEMENTS - les différents compléments (sélection de cible/direction/cout etc.)
actuellement :
compléments aux dialogues (sélection de la cible de déplacement (agissant ou case), sélection magie à impregner, sélection recette, etc.)
compléments aux magies
compléments aux parchemins




À faire : rework affichage/menus
Objectifs : Marchand fonctionnel, meilleure alchimie, actions à la souris, affichage mouvant


Pour le nouvel affichage :
Modification importante par rapport à avant :
L'affichage, avec ses skins etc. (objets non picklables y compris) est stocké d'un tour sur l'autre.
Dans certains cas, il est supprimé/reconstruit :
	Sauvegarde. Tout est supprimé.
	Ouverture. Tout est créé.
	Ouverture/fermeture d'un sous-menu (inventaire, etc.).
	Lancement d'un menu (alchimie, vente, etc.).
Est-ce que l'affichage est un attribu du joueur ?
Arguments pour :
Les menus/touches/etc. sont des méthodes et attributs du joueur. <- Pourquoi ? Est-ce que ça fait vraiment sens ?
Arguments contre :
Si on prend le contrôle de Dev, qu'est-ce qui se passe ? <- Enfin... avant d'en arriver là, on a du temps.
Le joueur (tel qu'il est défini actuellement) n'est qu'un agissant. Il n'a pas de raison d'être traité à part.

Idée :
Séparer l'affichage et le contrôle du joueur.
En fait, les séparer aussi du controleur...
Sauf que les contrôles sont liés au joueur (skills et magies qu'il possède).
Avoir un set de contrôles pour chaque perso jouable ?

Conclusion :
Affichage & controle : attributs/méthodes du Joueur
Liste des touches de contrôles : attribut du joueur (et d'autres persos s'ils sont jouables (garder dev à part quand même))
Garder des touches de contrôle qui ne peuvent pas être modifiées pour chaque perso ?
Global : pause, modification des touches, quitter la partie
Perso : skills


Pour les contrôles :
Quand est-ce qu'un contrôle peut-être utilisé ?
Différents types de contrôles :
	Contrôle du perso (comme ce que ferait l'esprit) : modifier la direction du perso, choisir sa prochaine action (skill + infos complémentaires)
	Actions spécifiques au joueur : interractions
	^ restreints à la phase TOUR (jeu normal)
	Meta-contrôles (pause, sortie, mute, etc.)
	^ pas restreints
	Navigation de l'affichage au clavier/à la souris
	^ pas restreint, effets variés selon les phases

Idée : menus etc. gérés completement par l'affichage -> remis à 0 si interrompus (i.e. 'recréé') -> affichage gère aussi les limites de temps








Qu'est-ce qui compose l'affichage ?
Certains éléments contiennent d'autres éléments qui ne se superposent pas (Pavage).
Certains éléments sont limités en taille par leur contenant (max).
D'autres sont limités par leur contenu (min).
Il y a des listes verticales (suite d'éléments, verticaux, placés les uns à la suite des autres).
Il y a des listes horizontales.
Il y a les "menus" avec des éléments jusqu'à remplir la ligne, puis d'autres sur la ligne suivante, etc. jusqu'à avoir tout affiché.
Une liste qui est limitée par son contenant doit permettre de circuler (molette de la souris, etc.).
Il y a (en tous cas actuellement) des surfaces divisées de façon préétablie.

Idée : rentrer une "taille" de chaque élément. Si positive, à suivre absolument, si négative, représente une proportion par rapport aux autres négatifs.

Pour les trois zones, on veut faire en proportion de la largeur totale de la fenêtre.
Pour la zone de gauche, on veut afficher les éléments fermés en plein et l'élément actif sur ce qu'il reste.
Dans l'inventaire, on veut afficher les classes à gauche en plein et leur contenu sur ce qu'il reste à droite.








Le joueur doit pouvoir "créer" l'affichage. Partiellement en fonction de ses propres attributs. Faire aussi dépendre de variables (dictionnaires ?) de configuration pour placer chaque chose au bon endroit.



Comment organiser le nouvel affichage ?

On veut pouvoir accéder à :
L'inventaire
La classe principale
Les stats
Les alliés
Les ennemis
D'autres choses ?



Un bon nombre des éléments de l'affichage correspondent à un objet (inventaire, classe).
Est-ce que les deux sont liés pour que l'objet puisse modifier son affichage sans tout changer ?



Idée pour l'affichage :

L'affichage a une liste de tout ce qui s'affiche à un moment donné.
Lorsqu'on raffraichit l'écran, on parcourt la liste en affichant tout (superposition déterminée par l'ordre dans la liste).
Lorsqu'on clique, on parcourt la liste pour trouver l'élément cliqué.
Éventuellement, on réagit à la présence de la souris sur l'élément (ne réagir que pour un seul).
Les actions actuelles d'affichage sont remplacées par un renouvellement de la liste.

Les éléments de la liste sont des objets avec :
des paramètres qui indiquent la taille, etc.;
une méthode pour afficher;
une méthode pour vérifier s'il y a contact avec la souris;
éventuellement d'autres éléments à l'intérieur ?


Que retournent les éléments cliqués ?
Exemple :
Ouvrir l'inventaire (ou la classe principale, ou autre) (modification de l'affichage) (peut être fait directement par l'affichage ?)
Utiliser un item (ou un skill, ou autre) (équivalent de l'actual "utilise_courant" du joueur) (appel d'une méthode du joueur)
Choisir une réplique de dialogue (il y a une méthode du joueur qui transmet à l'interlocuteur, non ?)
Choisir une recette d'alchimie (ou un objet du marchand, ou autre) (probablement un méthode du joueur ?)
Choisir une case pour un déplacement (encore un méthode du joueur ?)
Donc :
Retourne l'argument à donner à une méthode du joueur, éventuellement la méthode aussi ?









Comment gérer tous les menus/choix de façon simple ?

Il y a :
Les choix de direction(s) (magies, magies de parchemins) (nécéssité d'affichage du labyrinthe/d'une zone ciblée, partie "interactive" sur la droite) 
Les choix de case(s) (magies, magies de parchemins, ordres) (nécéssité d'affichage du labyrinthe/d'une zone ciblée, partie "interactive" au centre, éventuellement décompte sur la droite)
Les choix d'agissant(s) (magies, magies de parchemins, ordres) (nécéssité d'affichage d'une liste d'agissants, possiblement nécessité d'affichage du labyrinthe, partie "interactive" sur la droite)
Les choix d'item(s) (magies, magies de parchemins) (nécéssité d'affichage d'une liste d'items, probablement description à droite)
Les choix de magie (ordre d'imprégnation de parchemins, utilisation du skill de magie) (nécéssité d'affichage d'une liste de magies, probablement description à droite)
Les choix d'objet (achat, vente) (nécéssité d'affichage d'une liste d'items, probablement description à droite)
Les choix de recettes (alchimie) (nécéssité d'affichage d'une liste de recettes, probablement description de la recette et des ingrédients à droite)

Pour les magies, on veut choisir au moment de la sélection de la magie (choix unique, possiblement plusieurs choix à faire)
Pour les magies de parchemins, on veut choisir au moment de l'utilisation du parchemin (choix unique, possiblement plusieurs choix à faire, possiblement plusieurs parchemins à la suite)
Pour les ordres, on veut choisir pendant un dialogue (choix unique)
Pour l'utilisation du skill magie, on veut choisir au moment de la sélection du skill (choix unique)
Pour l'achat et la vente, on veut choisir pendant un dialogue (autant de choix/transactions que voulu, possiblement dans un "magasin", possiblement regrouper l'achat et la vente)
Pour les recettes, on veut choisir pendant un dialogue (autant de choix que voulu)

(Je ne sais plus si je voulais que la simplicité soit au niveau de la structure du code (classes, méthodes, etc. impliquées) ou de l'interface. Probablement de la structure, mais j'y ai rejoué récemment et l'interface laisse un peu à désirer. Un gros bouton "Confirmer (entrer)" et la possibilité de sélectionner à la souris seraient les bienvenus.)



En cours (alchimiste) :
- Parchemins imprégnés de magie (fait)
- Parchemin de défense (placer un enchantement de défense sur les alliés)
- Parchemin de téléportation (fait)
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



Comment fonctionne l'alchimie ? (Pour l'instant en faisant tout planter (hein !? je viens d'y rejouer et ça ma l'air fonctionnel (je n'ai pas essayé l'alchimie mais tout le reste va bien), j'espère que je ne suis pas en train de commiter un truc beugué))
1 ou plusieurs ingrédients (+ mana (+ argent)) = potion ou parchemin
éventuellement le résultat final peut être une amélioration d'un item du joueur ?
Les ingrédients sont une catégorie d'items distincte des autres. On peut en trouver par terre ou les acheter au marchand (?)
Certains ingrédients proviennent de monstres (dents de gobelin, peau de gobelin, etc.) et peuvent être trouvés là où il y a beaucoup de ces monstres. Mais il n'y a personne dans le labyrinthe qui sache extraire ces ingrédients des cadavres, donc on est obligé de passer par le marchand.
Recettes simples (pas plus de deux ingrédient par recette dans le tutoriel)
Peau de gobelin -> Parchemin vierge
Peau de gobelin + pierre dure -> Parchemin de protection
Dent de gobelin -> Potion de force
Hypokute -> Potion de soin
Cristal transparent -> Potion d'invisibilité





À propos des déplacements
Différents objectifs :
- Attaquer
- Survivre
- (Explorer)

Pour ce qui est d'attaquer, on a besoin d'être à portée (éventuellement au corps-à-corps) et on veut privilégier certains ennemis (ceux qui sont responsable du plus de dégats).
Pour ce qui est de survivre, on veut ne pas être pris dans les attaques (pour les sorts délayés) et s'éloigner des ennemis qui font beaucoup de dégat au corps à corps (est-ce qu'on veut fuir aussi les mages offensifs ?)
Concrètement, on va sélectionner la case où l'on se déplace sur la base de plusieurs critères :
 + proximité avec des ennemis importants (responsables de beaucoup de dégats/haïts pour d'autres raisons genre racisme), ne concerne pas tout le monde
 - proximité avec des ennemis dangereux (capables d'infliger beaucoup de dégats en corps-à-corps)
 - attaque magique prévue à cet endroit
 - proximité avec un endroit où une attaque magique est prévue (on ne veut pas foncer dans les attaques magiques)
 + proximité avec un endroit où il n'y a pas d'attaque magique (puisque les attaques magiques ciblent plusieurs cases, il faut aller vers le 'bord' et sortir de la zone)
 + proximité avec un allié 'protecteur' (quelqu'un qui va prendre les coups à notre place, typiquement un tank, ou un dps cac si on est un dps distance)
 - proximité avec un endroit invisible (absence de vision = danger potentiel), surtout quand on est affaibli ou support
 + proximité avec un endroit invisible (exploration = possibilité de dénicher un soutien qui se cache à l'écart de la mélée), à nuancer pour prendre en compte l'emplacement supposé des agissants vus précédemment
 + proximité avec un endroit/agissant ciblé (comme pour les humains qui suivent le joueur)

Le choix dépend aussi de la situation dans laquelle se trouve l'agissant :
- En état d'attaquer au corps-à-corps (cherche à se rapprocher des combats)
- En état d'attaquer à distance (cherche à se rapprocher des combats, mais potentiellement en s'assurant un bouclier humain/une forte concentration d'ennemis/etc.)
- En état d'agir en support (cherche à être en sécurité, protégé par d'autres où loin)
- Blessé 'sévèrement' (cherche à être en sécurité)
- Dans la zone d'effet d'une attaque magique 'peu dangereuse' (sortir de la zone est secondaire, mais préférable toutes choses égales par ailleurs)
- Dans la zone d'effet d'une attaque magique 'dangereuse' par ses dégats (il faut sortir de la zone, mais plutôt vers la direction des ennemis)
- Dans la zone d'effet d'une attaque magique 'dangereuse' parce qu'on est faible/blessé (il faut sortir de la zone, plutôt en se mettant à l'abri)

Options :
- Une 'équation' pour chaque situation de l'agissant, qui regroupe tous les critères en une valeur de la case (dépend probablement des PVs de l'agissant et d'autres trucs, donc à recalculer à chaque fois)
- Un tri selon les critères, en appliquant le critère suivant si le premier ne permet pas de trancher (l'ordre des critères dépend de la situation de l'agissant, les critères peuvent être calculés pour tout le monde d'un coup, où presque)
- Une combinaison des deux (par exemple regrouper la proximité avec les ennemis dangereux et la proximité avec les alliés protecteurs en un critère de dangerosité de la case)

(Pourquoi améliorer les déplacements ? Pour que les actions des agissants (et surtout des humains) semblent 'intelligentes' au joueur. Pour apporter un challenge d'ordre stratégique au joueur. Pour éviter que les humains meurent 'par malchance'. Avec un système de déplacements efficace, il sera aussi possible de créer des esprits plus 'bêtes' (en faisant dépendre de la présence de stratèges par exemple) ou qui tomberont dans certains pièges/auront des tendances à commetre certaines erreurs. Par exemple, on peut supposer que les monstres du tutoriel soient moins bien organisés, ce qui les rendra plus facile à vaincre.)

Comment faire pour les attaques de zone ?

Parfois, un agissant est bloqué par un autre, pourrait le contourner pour se rapprocher plus, mais serait bloqué plus loin. Avec la résolution actuelle, il reste bloqué.
Comment faire ?

Et pour qu'un agissant sorte du passage si quelqu'un veut aller là où il est (le joueur par exemple)



Déplacements actuels :

Tout en tour par tour, i.e. à chaque tour chaque agissant détermine selon sa santé et ses ennemis ce qu'il veut faire.
C'est simple et rapide, mais pas forcément efficace sur le long terme.
Par exemple, la fuite est décidée en fonction de la dangerosité de la case, et les gobelins dans le couloir de la prison par exemple restent bloqué à distance du joueur.
Deux PNJs qui vont dans un sens contraire peuvent aussi se bloquer.

La "compréhension de l'espace" des IAs laisse à désirer.

Idées :

Décisions à long terme. Par exemple, un tank qui passe sous 20% de PVs se met en fuite, et y reste jusqu'à revenir au-dessus de 50%.

Espace simplifié sous forme de graphe. Un point du graphe est un couloir (sans intersection) ou une salle (ensemble de cases à définir) et ces points sont connectés par leurs intersections.
Les couloirs sont des espaces où l'on ne peut pas se croiser, les salles sont des espaces où l'on peut se croiser. En connaissant aussi la distance entre les différents accès de chaque salle/couloir, on peut plannifier assez simplement les trajets.




À l'occasion, jouer avec les paramètres de la génération



Imports : qu'est-ce qui a besoin de quoi ?
Joueur :
	Controleur
	Affichage

Affichage :
	Rien ?

Controleur :
	Entitee
	Agissant
	Item
	Labyrinthe (et assimilés)
	Vue
	Esprit
	Effet

Labyrinthe (et assimilés) :
	Agissant
	Item
	Effet

Vue :
	Rien

Esprit :
	Agissant
	Vue

Agissants :
	Vue
	Inventaire
	Effet

Inventaire :
	Item
	Effet

Item :
	Agissant ?
	Effet

Effet :
	Item
	Agissant

De quoi ont-ils besoin exactement ?

Inventaire :
	Potion, Parchemin, Cle, etc.

Item :
	






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

Note : sans la peureuse, les humains ne savent pas changer d'étage !

TODO (global) :
Étages (0/100)
Dialogues
Cinématiques
Menus/interfaces "hors-jeu" (images)
PNJs
Skills et classes
Ennemis

Plus précisément :
Donner au tank une compétence de provocation
Décider des ingrédients pour l'alchimiste et implémenter les recettes
Implémenter les achats/vente
Modification de la vitesse dans le menu des touches
Système de 'cible' pour indiquer qui les gens attaquent





Retours exp�rience Cl�ment :
Pour l'�quilibrage : premiers monstres one/two-shot, puis progression (cr�er des monstres sp�cialement affaiblis pour le tutoriel ? il faut que je le fasse pour le slime de toute fa�on)
Potions : pour quoi faire ? Permanent/non permanent, affecte le joueur/les ennemis... Peut-�tre la port�e
Archer (impossible, mais des mages qui attaquent � distance, c'est faisable. pour remplacer les mages actuels qui sont vraiment faibles ? comment rep�rer facilement qui est responsable d'une attaque ? un seul mage par �tage, par exemple ?)
Plus d'accompagnement du joueur, plus d'explications. Diminuer la difficult�. C'est juste un tutoriel !


Retours exp�rience Martin + id�e potions et parchemins :
Shaman + mage + guerrier/sentinelle = tr�s puissant (l'�tage des potions est devenu difficile)
Shamans + mages + guerriers/sentinelles = trop puissant (l'�tage des meutes est devenu quasi-impossible (et encore, il n'y a pas d'effet de surprise pour moi))
4 PNJs qui colent le joueur � travers tout l'�tage des potions = salles blind�es, d�placements difficiles
Donc :
Explication des controles de PNJs (les ordres qu'on peut leur donner, comment v�rifier leur �tat avec le rectangle de droite, comment les rappeler)
Explication de l'inventaire et de la pause (comment ouvrir l'inventaire, y aller, y s�lectionner une potion/un parchemin et l'utiliser, et comment mettre le jeu en pause avant de faire tout �a)
Potions de renforcement temporaire (renforcement de la d�fense principalement, de la vitesse aussi)
Parchemins d'attaque � distance puissante, pour �liminer les shamans (ingr�dients tr�s rares, donc � utiliser avec mod�ration)
"Protection sacr�e", utilis�e par la sainte lorsque tout le monde est full-health, qui bloque certaines attaques ?
Modifier les consignes de fuite (les PNJs prennent bien trop de risques actuellement)
2 shaman + 1 mage = une attaque � 40 d�gats. Pour des humains qui ont 50 � 150 PVs et bless�s par d'autres gobelin, c'est la mort instantann�e.


Idée pour plus tard :
Dans la branche de l'essence magique, proposer une magie que le joueur n'a pas assez de pm pour lancer.
Par contre, il a assez de pm pour en imprégner un parchemin, puis (après les avoir régénérés) assez de pm pour utiliser le parchemin.


Messages d'entr�e pour certains �tages ?

Id�e : l'une des am�liorations des fl�ches, voire de tous le projectiles pourrait consister � les faire traverser les alli�s sans les toucher


Id�es de lore � disperser dans les niveaux :

"Nombreux sont ceux qui pensent que la voie de la magie est aussi la voie de la connaissance. Mais la magie est avant tout la voie de l'imagination, du refus de la r�alit�."
pour guider les joueurs qui ont pris le hint de Dev vers la voie de la connaissance, donc avant la premi�re mont�e de niveau.

"Les attribus �l�mentaires sont un sujet complexe et myst�rieux. Prenons l'exemple des maladies :
   - Les maladies sont un instrument de mort. Dans le labyrinthe, o� voir ses ennemis peut faire toute la diff�rence, la mort est associ�e � l'ombre. On pourrait donc penser que les maladies sont associ�es � l'�l�ment ombre.
   - Mais les maladies se propagent par le biais de virus, qui sont une forme de vie. Invoquer une maladie revient donc � cr�er la vie, et dans le labyrinthe, la vie est associ�e � l'�l�ment terre.
   - Le caract�re contagieux, presque �ruptif des maladies les lient au contraire � l'�l�ment feu.
   - Mais la lente agonie que causent certaines maladies n'est pas sans rappeler l'engourdissement de la magie de cong�lation, li�e � l'�l�ment glace.
En r�alit�, l'affinit� �l�mentale des maladies d�pend de la maladie en question, mais aussi parfois du mage responsable de son apparition. Bien malin qui peut dire, sans l'avoir observ�, � quel �l�ment est rattach� tel ou tel ph�nom�ne."
pour informer les joueurs sur les maladies, et indiquer que l'observation permet de connaitre l'affinit� de quelquechose.



� r�flechir s�rieusement :
- Il serait bien de ne pas faire reposer tout le d�veloppement de personnage sur les choix des mont�es de niveau (les arbres). En particulier, le joueur doit pouvoir progresser apr�s avoir atteint le niveau 10.
- Les sous-classes obtenues � la fin vont bien-s�r ce d�velopper plus tardivement, et permettre au joueur de continuer � se d�velopper (mais sans changer d'orientation, puisqu'il ne peut plus faire de choix).
- Le joueur peut aussi se d�velopper gr�ce aux objets qu'il trouve (exemple : le personnage de type Tank, qui progresse en rempla�ant son armure par une nouvelle plus forte).
- Risque : un joueur centr� sur la magie peut r�cup�rer une armure destin�e � un joueur de type d�fensif, et obtenir une tr�s bonne d�fense qui d�s�quilibre son personnage (et le rend trop fort).
- Contre-mesure : modifier les items disponibles en fonction des choix du joueur ;
- Mais : je n'ai pas envie de faire �a comme �a, et ces items peuvent servir aux compagnons du joueur.
- Autre contre-mesure : un joueur qui n'a pas choisi le skill Lancer ne pourra jamais rien faire d'utile avec une fl�che. Cette contre-mesure est dificilement applicable au port d'armures.
- Aussi : un sort, aussi puissant soit-il, ne sert � rien si on n'a pas suffisament de mana pour le lancer. /!\ Faire attention � ce que l'on peut ou ne peut pas obtenir � l'aide d'objets.
- Je suis en mesure de cr�er des zones qui refusent tel ou tel type d'agissant, y compris sur des crit�res de classes. Mais le joueur avec une construction centr�e sur l'observation doit pouvoir tout explorer, donc pas de loots distincts.
- Attention aussi au voleur, qui pourra r�cup�rer beaucoup d'objets diff�rends. En m�me temps, c'est sa fa�on de gagner. Faire de la capacit� � voir et collecter les objets une strat�gie � part enti�re ?
- Id�e : certains objets sont n�cessaires � l'�volution de certaines classes ou skills. Par exemple, un objet poss�d� par l'un des humains du jeu est n�cessaire au d�veloppement d'un voleur.
- Aussi : avoir mont� une classe � un certain niveau, ou poss�der un certain objet est une condition de d�verouillage d'un choix de la classe principale.
- Ou encore : passer telle classe du niveau x au niveau y est un des choix de la classe principale.
- Sauf qu'il faut arriver au bon niveau de la classe principale au bon moment, peu probable. Une d�pendance � des objets uniques rend le jeu impossible pour un non-initi�, et les objets utiles � une autre construction de personnage sont d�j� suffisament ennuyeux en un seul exemplaire.
- Certaines classes ne peuvent pas se reposer non plus sur leurs alli�s humains. Tout �a fait beaucoup d'interd�pendances des �l�ments du jeu � g�rer, mais c'est ce qui le rend marrant !


Garder une trace du code couleur, pour faciliter les modifications futures.




Fonctionnement des dialogues/interractions :
Du point de vue d'un joueur, les pnjs ont un dialogue par d�faut (si le joueur les accoste sans raison) et des dialogues conditionn�s (indiqu�s par un ! ou ? au dessus de leur t�te).

Quelques objets/skills obtenus dans des qu�tes :
- La carte. Permet de consulter la vue de l'esprit (donc de tous les alli�s) en mettant le jeu en pause.
- La th�l�pathie. Permet de d�clencher un dialogue avec un pnj qui n'est pas sur une case voisine.
- La concentration de bataille. Quand elle est activ�e, le jeu se d�roule en tour par tour (au sens o� le joueur doit "terminer le tour" pour passer au suivant.
En combinant les trois, le joueur peut donner des ordres plus pr�cis aux pnjs ("d�place-toi d'une case � gauche" ou "utilise tel sort sur tel ennemi", au lieu de "suis-moi", "fuit", "combat" etc. o� les d�tails sont g�r�s par l'esprit)
