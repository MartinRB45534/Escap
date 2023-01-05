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

2 - Gérer mieux les zones inconnues (est-ce que ça utilise vraiment les couloirs et salles ?)
    On voudrait avoir un minimum d'informations sur les zones "inconnues" (hors de la vision active, mémorisées et non mémorisées).
    Informations à rechercher :
        possibilité d'ennemis
        possibilité d'alliés
        nécessité d'exploration/d'observation
    Par exemple, pour la possibilité que quelqu'un soit quelque part, on a quatre situations. Si on a vu quelqu'un partir dans une direction, on obtient une idée de là ou il doit être (par exemple, dans cette salle ou dans l'un des couloirs qui en partent ou dans les espaces derrières ces couloirs, etc.). Sinon, si on sait que la direction mène à un (ou plusieurs) cul-de-sac, on sait qu'il ne peut pas être là-bas. Enfin, une direction qui ne remplit aucune de ces deux conditions ne peut pas mener au quelqu'un si on l'a vu partir dans une autre direction qu'on sait être un cul-de-sac, et peut (de façon incertaine) mener au quelqu'un sinon.
    Dans l'ensemble, pour chaque agissant, on peut distinguer un ensemble d'endroit où il est assuré de se trouver, et un ensemble d'endroit où il ne peut pas être.
    Les agissants qui passent des portes, détruisent ou traversent des murs ou se téléportent (principalement le joueur) peuvent provoquer des erreurs dans ces informations.

    Pour cette compréhension, on va avoir besoin de nouveaux espaces, qui désignent chacun un ensemble de cases qu'on sait connectées hors de notre vision courante (dans notre mémoire ou au-delà).

    De ces cases, on ne connait que celles qui sont dans notre mémoire et à la limite.

    Cicle de vie d'une zone inconnue :
        Création. Une zone inconnue est créée quand on a une case inconnue accessible (i.e. case sans visibilité auquel une case visible mène) qui n'est pas liée à une zone inconnue existante.
        
        (Remplissage par mouvement. Un agissant disparait d'une case. S'il n'est pas visible sur une case voisine (ou mort...), et qu'il y a des cases voisines invisibles, il est sûrement là.)

        Remplissage par ajout. Un agissant sur une case qui est ajoutée à la zone inconnue lui est aussi ajouté.
        
        (Fusion par contenu. Si un agissant d'une zone réapparait d'une autre zone, on peut supposer que les deux zones sont connectées, i.e. ce sont la même zone.)
        
        Vidage. Un agissant qui sort d'une zone (entre dans le champ de vision) lui est retiré, ainsi qu'à toutes les autres zones où il été supposé être.
        
        Ajout de case. Une case nouvellement hors-vue est ajoutée aux zones inconnues voisines. Si il y en a plusieurs, elles sont donc connectées par la nouvelle case et donc fusionnées (la nouvelle zone contient les cases et les agissants des zones fusionnées).
        
        Retrait de case par oubli. Une case limite ou mémorisée qui, par oubli, n'est plus limite ni mémorisée, est retirée à sa zone inconnue. Éventuellement, la zone est coupée en plusieurs zones, qui contiennent chacunes les agissants de la zone originale.
        
        Retrait de case par vue. Une case nouvellement vue est retirée à sa zone inconnue. Éventuellement, la zone est coupée en plusieurs zones, qui contiennent chacunes les agissants de la zone originale.
        
        Suppression. Si la dernière case d'une zone est retirée (par vue), la zone est supprimée. (Si un agissant était censé se trouver dans cette zone, mais n'y est pas, on peut supposer qu'il peut se déplacer de façon non conventionnelle.)

    Pendant la vue :
        ajout/création + remplissage par ajout
        remplissage par mouvement
        vidage
        retrait par vue
        suppression

    Pendant l'oubli :
        retrait par oubli

    création et ajout : même chose ?
    Comme pour les couloirs et les salles, on crée et on lie aux voisins s'il y en a.

    ajout/création
    cases nouvellement hors-vue nécessite vision
    comment savoir qu'un case est "nouvellement" hors-vue ? parce qu'elle n'était dans aucune zone avant et qu'elle n'est pas dans la vision maintenant ?

    mouvement
    agissant qui n'est plus là où il était
    i.e. une case qui contenait un agissant ne le contient plus (au moment de la mise à jour)

3 - Gérer mieux les déplacements
    Permettre aux corps de se croiser/contourner sans se bloquer, prioriser les déplacements.

