Contrôle automatique : plusieurs options
Version précédente : rien d'automatique
Version actuelle : on peut désigner un endroit ou un agissant comme cible et le joueur y va tout seul (approximativement).

Annulation ou pas de la commande quand on agit...

Idée : utiliser le clic droit. Clic gauche, commande approximative, clic droit, commande précise (ou inversement).

Clic gauche sur une case : on passe en mode 0 avec la case pour cible (on va traîner autour)
Clic droit sur une case : on passe en mode 2 avec la case pour cible (on y va et on n'en bouge plus)

Clic gauche sur un agissant : on le suit (on va traîner autour et agir dans la zone, comme les PNJs autour du joueur d'habitude)
Clic droit sur un agissant : on va au contact (si c'est un ennemi, on va probablement l'attaquer automatiquement (à vérifier), si c'est un PNJ on va lui parler (pareil pour un décors interactif))

Clic gauche sur soi-même : on passe en mode 1 (exploration) TODO: permettre le passage des portes dans ce mode
Clic droit sur soi-même : pilote automatique désactivé (on ne bouge pas, mais le joueur peut bien sûr se déplacer tout seul)


Que faire si pendant ce temps le joueur utilise les touches pour faire des trucs ?

Dépend de ce qu'il fait (s'il équippe des items ou lit des infos sur les ennemis on ne veut pas interférer, s'il demande à se déplacer il faut lui laisser la main).

Pour laisser la main, il faut arrêter de calculer la prochaine chose à faire.
Idée : au lieu de faire, indiquer ce qu'on ferait si on avait la main (facile ? sauf qu'il me faut plus d'affichage du coup.)

Laisser la main définitivement ? Si le joueur ne fait plus rien, on le laisse mourir ?
Actuellement, il y a interférence, il faudrait un temps minimal. (On peut décider que si le temps est -1, on attend indéfiniment, ou utiliser le clic droit sur soi-même comme seul moyen de désactiver. Probablement désactiver le contrôle automatique en début de jeu.)



Niveau structure :
Le joueur est un PNJ avec quelques trucs en plus. Les PNJs sont pour l'instant tous humains mais ce serait bien de distinguer (au niveau de l'esprit).

On va mettre la possibilité d'avoir des PNJs dans tous les esprits.