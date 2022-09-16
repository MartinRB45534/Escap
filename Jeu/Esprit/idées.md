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


    Salles :
        Successions de carrés (4 cases sans murs internes (mur internes ouverts au sens spatial, i.e. les téléporteurs, escaliers etc. ne sont pas ouverts)) qui partagent deux cases avec les carrés voisins. Chaque carré peut être repéré par sa case en haut à gauche.
        Les "entrées" sont toutes les cases dont un mur ouvert (au sens du passage, i.e. les téléporteurs, escaliers etc. sont ouverts) appartient à la frontière de la salle.
        Les entrées n'appartiennent pas à la salle. Ce seront des carrefours.

    Couloirs :
        Successions de cases à 2 ou 1 ouvertures (au sens spatial ?) qui partagent un mur avec les cases voisines. Chaque case peut être repérée par sa position.
        Les "entrées" sont les cases voisines des extrémités (i.e. les cases cibles des murs ouverts (au sens du passage) de la frontière du couloir). Il y en a une ou deux.

    Carrefours :
        Les cases restantes sont des carrefours (y compris les entrées des salles et des couloirs).



    Suppression des anciens éléments :
        1 - Lister les anciens carrés possibles (4 pour chaque ancienne case)
        2 - Trouver les carrés supprimés
        3 - Retirer les carrés aux salles (si un ancien carré est connecté à plusieurs autres carrés, vérifier qu'ils sont toujours connectés)
        4 - Lister les cases supprimées de chaque salle (potentiellement des cases non-supprimées, mais n'appartenant plus à la salle)
        5 - Retirer les cases restantes aux couloirs (en scindant les couloirs si les cases sont au milieu)
        6 - Retirer les carrefours supprimés

    Ajout des nouveaux éléments :
        1 - Lister les nouveaux carrés possibles (4 pour chaque nouvelle case)
        2 - Trouver les carrés (vérifier que les murs internes sont ouverts)
        3 - Ajouter les nouveaux carrés aux salles (pour chaque carré, créer une salle qui contient ce carré ; pour chacun des 4 carrés voisins potentiels, si le carré voisin appartient à une salle, fusionner avec la salle actuelle du carré actuel)
        4 - Lister les nouvelles cases de chaque salle (non-entrées) (potentiellement d'anciennes cases nouvellement dans la salle)
        5 - Ajouter les cases restantes aux couloirs (pour chaque case restante, si elle a 2 ou 1 ouverture, créer un couloir qui contient cette case ; pour chacun des 2 ou 1 cases voisines, si la case voisine appartient à un couloir, fusionner les couloirs)
        6 - Lister les cases restantes comme carrefours

    Faire la suppression avant l'ajout (calculs de connection des salles plus courts)

