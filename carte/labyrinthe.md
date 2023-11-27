Qu'est-ce que le labyrinthe ?

Un graphe directionel qui contient toutes les cases et les liens qui les relient.

Comment est-il généré ?

 - à partir d'un .json qui contient les informations nécessaires (mais encore ?) ;
 - par extension (ajout ou agrandissement d'un étage dans l'éditeur) ;
 - par extraction d'un sous-graphe (vue de l'agissant) et combinaison/modification de sous-graphes (vue de l'esprit) ;
 - autre chose ?

Donc l'__init__ est une problèmatique pour les sous-classes.
La génération (aléatoire) ne concernera que le labyrinthe en temps de jeu (il faudra quand même pouvoir le faire dans l'éditeur).