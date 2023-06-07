Comment fonctionne le nouveau modèle ?

Il fournit les classes qui donnent l'état du jeu à un instant précis.

À quel point est-il séparé du moteur ?
Est-ce que le moteur est juste la boucle qui appelle les fonctions du modèle ?

Pour jouer :
 - initialisation (avec les json pour créer tout ce qu'il faut)
 - 


L'une des difficultés est le retrait du controleur.
À quoi sert le controleur ?
 - appliquer l'équilibrage -x (plus besoin car .json)
 - stocker les entitées, les esprits, les étages -> les étage deviennent le labyrinthe (et le reste ?)
 - accéder à une case ou un mur -> passer par le labyrinthe
 - créer tout -x (plus besoin car .json)
 - pause -> à gérer ailleurs (moteur)
 - phases -> à gérer ailleurs
 - activer/déseactiver -x (plus besoin car plus de controleur)
 - déplacer -x (plus besoin car plus d'activation)
 - contruire portes, barrières, escaliers -x (plus besoin car .json)
 - construire vue -> le labyrinthe peut le faire avec les outils de graphe
 - trouver les entitées quelque part -x (plus besoin car stocké sur les cases)
 - trouver les entitées touchées/potentiellement ciblées dans un rayon donné -> le labyrinthe peut faire les propagations
 - accéder à un esprit -x (plus besoin car les esprits ne sont plus stockés par leurs noms)
 - accéder à une entitée -x (plus besoin car les entitées ne sont plus stockées par leurs IDs)
 - accéder aux entitées/esprits/cases à faire agir -> à gérer ailleurs ?

Donc là où on appelait avant le controleur, on va maintenant avoir besoin du labyrinthe ?
Pour construire la vue
