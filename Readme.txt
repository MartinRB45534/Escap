Work in progress !

Attention /!\ les pnjs peuvent bloquer le joueur en essayant d'aller vers lui lorsqu'ils sont trop nombreux et que le joueur doit faire demi-tour !

Est-ce que les gens sont bless�s par leur propre stomp !? Le myst�re du mage gobelin...
La variable globale ID_MAX ne remplit pas du tout son r�le ! Qu'est-ce que je fais ?
L'autruche, en codant les pnjs




Pour la magie, la r�g�n�ration est ce qui d�termine la v�ritable puissance. Les pm max correspondent juste � une limitation sur les sorts qu'on peut utiliser, et sur le nombre de sorts qu'on peut balancer d'affil�e au d�but de la confrontation. Modifier les stats en cons�quence.



Objectif courant : recr�er le tutoriel
- PNJs
- Interractions PNJs-joueur
- Monstres
- Layout
Au passage :
- Fin du travail sur l'affichage (arbre �l�mental)
- Rendre fonctionnels tous les choix, puis les conditionner

Si j'ai le temps :
- Cr�er les premiers monstres (le tutoriel est un camp de gobelins)
- Faire de meilleurs skins pour les gobelins.



Quelques nouvelles magies � cr�er :
- Magies tribales (genre, qui varient selon l'esp�ce, comme un coup de poing magique qui n'est pas le m�me pour les gobelins et les orcs)
- Coup de poing magique (magie d'attaque des mages de combat)
- Boost complet (un boost qui affecte toutes les stats)
- Purification (la magie anti-monstres de la peste)


�tage combat : trois sentinelles aux trois points de passage
�tage monstres : une sentinelle, un gobelin de base, un mage, deux guerriers, dans un d�dale
�tage portes (prison) : sentinelles, guerrier de plus haut niveau dans une salle (c'est un pi�ge !), quelques monstres captur�s ?
�tage potions : guerriers, mages, un shaman, deux guerriers de plus haut niveau.
�tage meutes : guerriers, mages, deux shamans, plein de gobelins de base dans les couloirs.
�tage magie : tout !
�tage items : tout, mais un peu moins, plus quelques gobelins �quipp�s.
�tage boss : tout, mais un peu plus, plus un chef gobelin.


�quippements du tutoriel :
Armures (bloque 20%, r�duit les d�gats de 20, r�duit les d�gats � 20, annule les attaques de moins de 20 mais laisse passer les autres... pas toutes mais deux ou trois)
Armes (�p�e, lance, autre (une arme peut-�tre plus forte mais avec moins de skills de boosts �videmment))
Casques (comme les armures, + bandeau ou quelque chose, qui boost le mana)
Anneaux (plein d'effets possibles !)
Bouclier (sauf qu'il faut un skill pour s'en servir... peut-�tre un bouclier avec un effet passif semblable aux armures ?)


� l'occasion, faire le tri dans les constantes


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
- Allonger les temps pour les magies � choix de co�t.


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
