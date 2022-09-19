Comment utiliser couloirs et salles pour optimiser les esprits :

1 - Simplification de la méthode actuelle
    Il n'y a pas toujours besoin de propager à chaque case des salles et des couloirs. On peut alors sauter d'une entrée à l'autre (on connait la distance qui les sépare).
    Cas où il faut propager dans les salles et les couloirs :
        quand la source est dans la salle ou le couloir
        quand on veut utiliser la valeur dans la salle ou le couloir (i.e. le corps qui veut se déplacer est dans la salle ou le couloir)
        et quand un obstacle est dans la salle ou le couloir ? (Souvent l'obstacle va être lui-même une source ou quelque chose qui a besoin de mesurer la valeur donc la question ne se pose pas.)
    Cas où il n'est pas nécessaire de propager :
        tout le reste du temps
    Actuellement, que propage-t-on ?
        les seuils de dangerosité d'effets, vers l'intérieur (utilisé par les corps)
        la dangerosité (effets et ennemis, utilisé par les corps)
        l'importance (ennemis, utilisé par les corps)
        la cible de déplacement d'un humain (allié, ennemi ou position)
    En résumé, lors de la propagation, il peut être utile de marquer les salles et couloirs à parcourir et de ne pas parcourir le reste.
    Un espace est à parcourir si la source se trouve dans l'espace (entrées exclues) ou si le recepteur se trouve dans l'espace (entrées inclues).

2 - Gérer mieux les déplacements
    Permettre aux corps de se croiser/contourner sans se bloquer, prioriser les déplacements.

