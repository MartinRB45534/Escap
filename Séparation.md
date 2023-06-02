Comment séparer les choses ?

Le moteur (le controleur, etc. et même Joueur.py) sont complètement imbriqués. À part donc.

L'affichage observe des éléments du moteur (principalement dans le fichier Affichages.py). Peut-être à distinguer entre Affichage.py et Affichages.py ? (Il faudra séparer chaque fichier de toute façon.)
On pourrait mettre Affichages.py dans le moteur (appelé par Joueur.py de toute façon).
Le reste serait à part, à disposition aussi des menus.

Les menus appelleraient les deux.

Peut-être une version simplifiée du labyrinthe, utilisée dans le moteur pour définir le labyrinthe actuel ? Qu'est-ce qu'il y a dans le labyrinthe qui serve au déroulé du jeu ? Beaucoup de choses.

