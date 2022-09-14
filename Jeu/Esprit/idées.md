Conception de l'espace :

    couloirs (succession de cases sans embranchement)
    carrefours (embranchement)
    salles (espace "ouvert", i.e. il y a toujours plusieurs chemins entre deux points)

    Chaque point de l'espace est dans un couloir, sur un carrefour ou dans une salle. Il est à une certaine distance des autres éléments du même couloir, carrefour ou salle et des entrées/sorties du couloir, carrefour ou salle. Théoriquement, tous les calculs actuels pourraient se faire avec ces informations et en ne propageant qu'au sein des couloirs, carrefours ou salles concernés.

Concrétement :

    Comment former les couloirs, carrefours et salles ?
    Option simple (mais probablement coûteuse) : recalculer à chaque fois (pourrait convenir pour les esprits avec peu de vision/beaucoup de changements de vision)
    Option compliquée : mettre à jour au fur et à mesure (sans-doute nécessaire au moins pour l'esprit du joueur qui mémorise l'intégralité du labyrinthe parcouru)

    Pour les couloirs : au minimum, c'est une case avec deux ouvertures (à moins que ce soit le coin d'une salle) (techniquement, un couloir de trois cases en coin peut en fait être une salle)
    À partir d'une première case, on ajoute les cases voisinnes si elles sont connectées et n'ont que deux ou une ouverture. Information à stocker : les extrémitées (pour tous les calculs) et les cases intermédiaires (dans l'ordre ?) pour les cas où il faut propager localement ou scinder le couloir parce qu'on en perd de vue le milieu.

    Pour les carrefours : ce sont toutes les cases qui ont trois ou quatre ouvertures (sauf celles qui appartiennent à une salle). Chaque carrefour ne comprend qu'une case.

    Pour les salles : tout le reste. Le plus difficile à définir et distinguer. Peut-être commencer par là ?

    Pour les connexions : garder en mémoire qu'est-ce qui est connecté à quoi ? Le retrouver à partir des positions ?