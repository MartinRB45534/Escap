Utiliser des enums pour les boucles

Où ?

Pour le joueur (continuer à réduire le controleur btw).
(Actuellement ce sont les phases du controleur, qui sont des constantes avec des valeurs d'entiers.)

Pour l'ensemble des menus.

Qu'est-ce que je veux en menus ?

Deux versions :
Version "commerciale", avec les sauvegardes, les joueurs, etc. et moins de sorties d'erreurs par exemple.
Version "dev", avec l'éditeur de niveux, des outils de visualisation (vues des esprits par exemple) et des accès rapides à des parties de test.

Faire un moteur unique pour le jeu. (Peut-être un module à part ? Si j'y arrive.) Avec quelques fonctions à appeler pour tout faire tourner. Et importer ce module depuis chaque version.

Pour revenir sur les enums :
Un pour chaque version. Un pour le moteur avec les phases du controleur.



On va commencer par la version dev.
Phases :
Initialisation (les imports principalement, je suppose).
Menu principal (ce serait cool de pouvoir réutiliser un bout de l'affichage pour faire mes boutons).
Préparation du jeu (création du joueur à partir du .json correspondant).
Jeu (en vrai c'est le moteur qui boucle).
Fin du jeu (mort ou abandon).
Editeur (étage par étage).
Vue d'esprit (quand je mets le jeu en pause pour regarder la vision, les zones, etc.) et parcourt des infos.
