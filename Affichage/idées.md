séparer la forme du fond, i.e. se référer le moins possible aux objets qui dépendent de controleur

fait : garder en mémoire, par exemple si on ferme l'inventaire il se réouvrira au même point la prochaine fois

mettre à jour en temps réel, par exemple faire varier les PVs des agissants dans leur description

fait : pour la mise en mémoire, ne pas inclure les surfaces (pour pouvoir pickler)

si possible, textes par morceaux, pour pouvoir insérer les touches etc., cliquer sur les mots-clés et changer de langue  <-- important - peut aussi aider avec les PVs qui changent, etc.


Quelles actions sur les agissants ?
Version précédente :
 - allié : appeler
 - neutre : rien
 - ennemi : désigner comme ennemi important (augmenter sa priorité)
Possibilités :
 - allié :
   - appeler (déclenche un dialogue quand il arrive) ;
   - rejoindre (pareil mais c'est le joueur qui bouge automatiquement) ;
   - commander (autoriser les commandes à distances ?) ;
   - exclure (pour plus tard).
 - neutre :
   - rejoindre ;
   - désigner comme ennemi ;
 - ennemi :
   - rejoindre (et attaquer automatiquement ?) ;
   - désigner comme ennemi important ;



J'ai 2 types de relations de parentalité (pour la notion de courant) :
  - les parents qui contiennent leurs enfants (exemple : la zone de gauche, qui contient les stats, l'invnetaire et la classe)
  - les parents dont les enfants sont affichés à côté (exemple : dans une certaine mesure l'inventaire, puisque la vignette de l'item est le 'parent' de la description de l'item ; ou encore l'achat/vente, où les vignettes des items sont dans la zone du centre, et la description de l'item courant est dans la zone de droite)
(Il y a aussi les cas comme les classes, mais c'est plus ou moins le premier cas.)

Est-il grave que les relations de courant ne suivent pas le même arbre que les relations d'objet/contenu ?
Les relations de courant sautent déjà des intermédiaires. Même les fonctions recursives devraient fonctionner en séparant complètement les deux.

Les vignettes seraient essentiellement des placeholders. Elles devraient quand même réagir au survol etc. (donc visuellement fonctionner normalement) mais transférer le reste du boulot.

Il faut aussi un statut spécial pour l'endroit qui contient la description : il doit être accessible par le placeholder (donc lui être passé en paramètre ?) et pouvoir rajouter la description facilement.
À moins qu'un wrapper suffise ? On va essayer.


Placeholder : plus compliqué que prévu au final.

Exemple des items :
On a la liste des catégories à gauche. On clique sur une vignette. C'est la vignette de la catégorie courante.
On clique sur un item dans la liste des items de la catégorie : la vignette est toujours l'élément courant => mais l'action de cliquer a changé ça.
On clique ailleurs, puis sur un item de la liste à nouveau -> il faut remettre la vignette en élément courant de l'affichage de l'inventaire (or on n'a pas cliqué dessus du tout, donc sa fonction clique() ne sera pas appelée).
On est sur la liste des items, on utilise Tab pour passer à la catégorie suivante -> il faut changer le courant de la liste des catégories.
On utilise Backspace -> il faut que la liste des catégories soit courante.

Idée : si cliqué, le placeheldholder se renvoie lui-même. On revient à son parent, qui cherche récursivement un placeholder dont le placeheld soit le contenu du placeheldholder. Si on ne trouve pas, on ne renvoie pas le parent mais le placeheldholder, etc. donc il faut modifier clique() pour tous les Knot et ajouter une nouvelle fonction (qui réattribue le courant)





Comment gérer les éléments courants ?
Plusieurs problématiques :
  - remonter à l'élément actif depuis la racine
  - lorsqu'on change d'élément actif, conserver ses sous-éléments ouverts
  - marquer le survol (accessoirement peut-être ouvrir les sous-éléments par survol)
  - marquer l'élément actif
  - dans les choix, marquer les éléments sélectionnés (déjà géré actuellement)

marquage actif/survol : booléens réinitialisés à chaque frame
arborescence : objet (ou None)
actif : booléen

On peut remonter à l'élément actif en parcourant l'arborescence depuis la racine jusqu'à l'élément actif

On peut au passage marquer l'élément actif.
Qu'est-ce qu'on veut faire pour le survol exactement ? Marquer la présence de la souris ?




structure :

affichage global
 - stats
   ...
 - inventaire
   - liste vignettes catégories (les listes ont toujours un élément courant)
   - potions
     - liste potions
   - parchemins
     - liste parchemins
   ...
 - classe
   - liste skills
   - liste skills intrasecs
   - liste sous-classes
     - sous-classe 1
       - liste skills
       - liste skills intrasecs
       ...
     - sous-classe 2
       - liste skills
       - liste skills intrasecs
       ...
     ...
 - labyrinthe
 - esprit
   - liste alliés
   - liste neutres
   - liste ennemis
 - dialogue
   - phrase
   - liste répliques
 ...

Ces éléments ^ sont de l'ordre du fond, indépendant de l'écran et à stocker. Ils générent l'affichage
