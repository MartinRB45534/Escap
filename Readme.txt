Work in progress !


Note du 26/01:
J'ai r�gl� le probl�me avec les compl�ments d'enchantements (mauvaise classe), mais ils peuvent encore faire crasher le jeu si on les cast sur le mauvais item, par exemple.
Objectif pour demain matin : d�placer le choix des compl�ments chez le joueur, et au moment de l'utilisation de la touche, pour en finir avec le rework des inputs.
Bonus : adjoindre ces modifications au syst�me des held keys (m�thode recontrole() du joueur)



Nouvel objectif : l'organisation du main, la sauvegarde externe des parties
Travail en cours : la structure du main
- Penser et structurer le main
- Sauvegarder les �l�ments essentiels
- Uniformiser les inputs
- Num�rotation des frames pour les illustrations
Au passage :
- Fin du travail sur l'affichage (arbre �l�mental, attaques)
- Rendre fonctionnels tous les choix, puis les conditionner
Si j'ai le temps :
- Cr�er les premiers humains
- Cr�er les premiers monstres
- Faire utiliser les items par les pnjs


Structure du main :
- R�cup�ration des inputs 
  Dans quelle boucle les envoyer ? = Variable, dans le main ou le controleur ?
  - Boucle 'classique' (inputs rentrent vers le milieu du tour)
  - Boucle de choix d'action (vient du 'fait_agir')
  - Boucle de choix de niveaux/classes/etc. (fin du tour)
  - Boucle de modification des commandes




Probl�me d'input :
Pygame ne r�p�te qu'une touche � la fois ! Or on veut marche ET s'orrienter, ou attaquer ET s'orrienter
Pourquoi est-ce que get_pressed() ne convenait pas ?
Parce qu'on bougeait souvent de deux cases.

Id�e 3 :
Limiter le get_pressed() pour quand le joueur doit agir (l'esprit qui le contient appelle une fonction avec le get_pressed() ?)
Et continuer � utiliser le KEY_DOWN en permanence

Id�e 1 :
Simuler la r�p�tition des touches, pour que �a r�p�te plusieurs fois ;
Ou �diter le code de pygame, pour qu'il fonctionne correctement ;
Ou contacter les gens de pygame, pour qu'ils modifient �a dans leur prochain update.

Id�e 2 :
Garder un trace du dernier skill utilis� (ou de la derni�re touche dont le skill a effectivement �t� utilis�, mais c'est plus compliqu�) et surveiller les KEY_UP.
L'id�e �tant : la touche est appuy� pendant un temps tr�s court, on veut le savoir !
               la touche est relach�e pendant le tour, on ne veut pas le prendre en compte !
               la touche est r�appuy�e, on la reprend en compte m�me si elle est relach�e plus tard !
Donc : les KEY_DOWN comme d'habitude
       Les get_pressed() comme d'habitude
       les KEY_UP en combinaison avec une variable pour savoir si le skill a d�j� �t� utilis� au tour pr�c�dent, auquel cas on le lache juste un peu tard
       la variable est purg�e d�s que le KEY_UP est d�tect�, et ne se rerempli qu'� la prochaine action
       tout �a sans g�ner les autres inputs



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


Notes de trucs � am�liorer :
- R�glage du nombre de tours par seconde. Please.


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
