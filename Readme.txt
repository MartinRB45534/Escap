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
	- mains[0][2].controleur.entitees[2] est le joueur, donc :
	- mains[0][2].controleur.entitees[2].pv = 100 pour remettre les pvs du joueur � 100 , ou
	- mains[0][2].controleur.entitees[2].position = ('�tage 10 : Boss',0,0) pour d�placer le joueur � l'�tage du boss, dans le coin en haut � droite
	les ID de 1 � 10 sont r�serv�es aux humains, donc elles sont fixes, pour les autre :
	- mains[0][2].controleur.entitees donne le dictionnaire de toutes les entitees, (agissants et items) class�es par ID, ensuite, c'est de l'essai erreur pour trouver la bonne
	- mains[0][2].controleur.labs donne le dictionnaire de tous les labyrinthes (~= �tages pour l'instant) class�s par nom, ce qui aide pour la premi�re coordonn�e des positions
	- mains[0][2].controleur.esprits donne le dictionnaire des esprits, et :
	- mains[0][2].controleur.entitees[ID].esprit donne le nom de l'esprit de l'entit�e correspondant � ID, donc :
	- mains[0][2].controleur.esprits[mains[0][2].controleur.entitees[ID].esprit].ennemis pour le dictionnaire des ennemis de l'esprit de l'entit�e correspondant � l'identifiant ID
	- mains[0][2].controleur.labs[mains[0][2].controleur.entitees[ID].position[0]].matrice_cases[mains[0][2].controleur.entitees[ID].position[1]][mains[0][2].controleur.entitees[ID].position[2]].murs[mains[0][2].controleur.entitees[ID].dir_regard].effets donnerai la liste des effets du mur juste en face de l'entit�e correspondant � l'identifiant ID (probablement un Teleport qui conduit � la case voisine et �ventuellement un Mur ou une Porte qui bloque le passage)
	- mains[0][2].controleur.entitees_courantes pour la liste des IDs des entit�es en activit�, et
	- mains[0][2].controleur.labs_courants pour la liste des noms des labyrinthe actifs
Honn�tement la modification de position est la seule chose utile de ce que je viens de citer, d�s qu'on commence � ramener des entitees � la vie �a s'appelle tricher... Attention quand m�me quand on se rend dans un �tage inactif, penser � l'activer ou toute interraction avec l'environnement (les monstres ou les humains, par exemple) fera planter le jeu (prendre l'escalier pour sortir de l'�tage et y revenir r�active l'�tage, sinon mains[0][2].controleur.active_lab(nom_du_lab_�_activer) en rempla�ant nom_du_lab_�_activer par le nom du labyrinthe � activer.
Si le controleur (la "partie") n'est pas sur le premier Main de la liste, il faut remplacer le 0 dans mains[0][2] par l'indice du Main (bonne indication : quand mains[0][2].controleur renvoie None, c'est qu'on est pas sur le bon Main).
Troisi�me �tape : mains[0][2].boucle() et le jeu reprend imm�diatement, attention aux surprises quand l'affichage se met � jour pour prendre en compte les nouvelles modifications !














� mon attention :




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





Comment g�rer tous les menus/choix de fa�on simple ?

Il y a :
Les choix de direction(s) (magies, magies de parchemins) (n�cessit� d'affichage du labyrinthe/d'une zone cibl�e, partie "interactive" sur la droite) 
Les choix de case(s) (magies, magies de parchemins, ordres) (n�cessit� d'affichage du labyrinthe/d'une zone cibl�e, partie "interactive" au centre, �ventuellement d�compte sur la droite)
Les choix d'agissant(s) (magies, magies de parchemins, ordres) (n�cessit� d'affichage d'une liste d'agissants, possiblement n�cessit� d'affichage du labyrinthe, partie "interactive" sur la droite)
Les choix d'item(s) (magies, magies de parchemins) (n�cessit� d'affichage d'une liste d'items, probablement description � droite)
Les choix de magie (ordre d'impr�gnation de parchemins, utilisation du skill de magie) (n�cessit� d'affichage d'une liste de magies, probablement description � droite)
Les choix d'objet (achat, vente) (n�cessit� d'affichage d'une liste d'items, probablement description � droite)
Les choix de recettes (alchimie) (n�cessit� d'affichage d'une liste de recettes, probablement description de la recette et des ingr�dients � droite)

Pour les magies, on veut choisir au moment de la s�lection de la magie (choix unique, possiblement plusieurs choix � faire)
Pour les magies de parchemins, on veut choisir au moment de l'utilisation du parchemin (choix unique, possiblement plusieurs choix � faire, possiblement plusieurs parchemins � la suite)
Pour les ordres, on veut choisir pendant un dialogue (choix unique)
Pour l'utilisation du skill magie, on veut choisir au moment de la s�lection du skill (choix unique)
Pour l'achat et la vente, on veut choisir pendant un dialogue (autant de choix/transactions que voulu, possiblement dans un "magasin", possiblement regrouper l'achat et la vente)
Pour les recettes, on veut choisir pendant un dialogue (autant de choix que voulu)

(Je ne sais plus si je voulais que la simplicit� soit au niveau de la structure du code (classes, m�thodes, etc. impliqu�es) ou de l'interface. Probablement de la structure, mais j'y ai rejou� r�cemment et l'interface laisse un peu � d�sirer. Un gros bouton "Confirmer (entrer)" et la possibilit� de s�lectionner � la souris seraient les bienvenus.)



En cours (alchimiste) :
- Parchemins impr�gn�s de magie (fait)
- Parchemin de d�fense (placer un enchantement de d�fense sur les alli�s)
- Parchemin de t�l�portation (fait)
- Parchemins divers
- Potions de soin (un peu redondant avec la peste et les parchemins impregn�s par la peste)
- Potions de boost (un peu redondant avec la peureuse et les parchemins impregn�s par la peureuse)
- Potions de vitesse (vraiment utile ? tout le monde se plaint d'aller trop vite)
- Potions diverses
- Ingr�dients (y compris les corps de monstres ?)
- Identification d'objets (via un skill d'observation ?) (le joueur 'm�morise' l'identification ?)
- Magie de sauvegarde temporelle
- Magie de r�activation de la sauvegarde
- Magies diverses
- Mon�tisation



Comment fonctionne l'alchimie ? (Pour l'instant en faisant tout planter (hein !? je viens d'y rejouer et �a ma l'air fonctionnel (je n'ai pas essay� l'alchimie mais tout le reste va bien), j'esp�re que je ne suis pas en train de commiter un truc beugu�))
1 ou plusieurs ingr�dients (+ mana (+ argent)) = potion ou parchemin
�ventuellement le r�sultat final peut �tre une am�lioration d'un item du joueur ?
Les ingr�dients sont une cat�gorie d'items distincte des autres. On peut en trouver par terre ou les acheter au marchand (?)
Certains ingr�dients proviennent de monstres (dents de gobelin, peau de gobelin, etc.) et peuvent �tre trouv�s l� o� il y a beaucoup de ces monstres. Mais il n'y a personne dans le labyrinthe qui sache extraire ces ingr�dients des cadavres, donc on est oblig� de passer par le marchand.
Recettes simples (pas plus de deux ingr�dient par recette dans le tutoriel)
Peau de gobelin -> Parchemin vierge
Peau de gobelin + pierre dure -> Parchemin de protection
Dent de gobelin -> Potion de force
Hypokute -> Potion de soin
Cristal transparent -> Potion d'invisibilit�


Travail � faire :
- Layout (prison, dialogues)
  Prison :
    - Petite salle avec une porte, cl� obtenue par dialogue
    - Petite salle avec deux portes, une cl� sur le sol
    - Couloir, deux sentinelles avec un passe-partout
    - Salles actuelles (plus d'innaccessibles)
    - Fin du couloir, escalier et salle du petit-ami (dialogue pour obtenir la cl� ?)
  Cuisine :
    - Salle avec le PNJ, une porte et des portails
    - "D�dale" de portails, avec quelques gobelins, des potions/parchemins/ingr�dients et la cl�
    - Grande salle , avec quelques gobelins et un shaman (des marmites ? pour introduire la notions d'objets inamovibles)
- Cr�ation (ombriuls)
(- Modifier la fuite pour ne fuir que si un alli� est accessible)
- �quilibrer ! (tours par secondes, combats, jeter un oeil � l'XP obtenu)

TODO (global) :
�tages (0/100)
Dialogues
Cin�matiques
Menus/interfaces "hors-jeu" (images)
PNJs
Skills et classes
Ennemis

Plus pr�cis�ment :
Donner au tank une comp�tence de provocation
D�cider des ingr�dients pour l'alchimiste et impl�menter les recettes
Impl�menter les achats/vente
Modification de la vitesse dans le menu des touches
Syst�me de 'cible' pour indiquer qui les gens attaquent





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
