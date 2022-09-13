Je vais essayer d'ajouter un système de versions. Pour voir la progression du jeu et convertir les sauvegardes.

Les numéros de versions correspondront aux étages du labyrinthe.
La version 0.0 sera celle où le tutoriel sera terminé, puis 1.0 pour les étages 1 à 10, 2.0 pour les étages 11 à 20, etc. jusqu'à 10.0 pour les étages 91 à 100.
Si besoin est, des versions intermédiaires seront ajoutées (lorsque je ne fais pas les 10 étages d'un coup, ou pour d'autres éléments comme les cinématiques, l'équilibrage, les interfaces, etc.).

L'information est stockée grâce au module pickle, qui se contente de mettre les attributs en mémoire. Je n'ai pas besoin de modifier les méthodes, ni les éléments définis globalement (les images, les constantes, etc.).
Les changements qui peuvent poser problème sont l'ajout d'attributs à une classe et la suppression/le remplacement d'une classe, uniquement si la classe est sauvegardée.
Les classes concernées sont:
Joueur
Controleur
Labyrinthe
Case
Mur
Entitee et toutes ses sous-classes
Inventaire et sa sous-classe
Esprit et toutes ses sous-classes
Effet et toutes ses sous-classes
Affichage
