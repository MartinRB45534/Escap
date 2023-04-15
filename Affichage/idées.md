séparer la forme du fond, i.e. se référer le moins possible aux objets qui dépendent de controleur

fait : garder en mémoire, par exemple si on ferme l'inventaire il se réouvrira au même point la prochaine fois

mettre à jour en temps réel, par exemple faire varier les PVs des agissants dans leur description

fait : pour la mise en mémoire, ne pas inclure les surfaces (pour pouvoir pickler)

si possible, textes par morceaux, pour pouvoir insérer les touches etc., cliquer sur les mots-clés et changer de langue





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
