Les actions sont ce que font les agissants : se déplacer ; attaquer ; lancer une magie ; etc.
Le déplacement des items pourrait aussi s'en approcher.



Système actuel :

Chaque action augmente la latence de l'entitee.
La latence diminue à chaque tour, et l'action suivante est effectuée lorsque la latence de l'agissant atteint 0.

Pour les agissants, chaque action correspond à un skill.
La prochaine action (décidée par l'esprit ou commandée par le joueur) est stockée sous la forme d'un skill_courant.
Les informations complémentaires (magie spécifique pour le skill magie, projectile pour le skill lancer, cibles) sont aussi stockées.

Problèmes :
Les informations complémentaires peuvent être fausses au moment de l'action.
Chaque magie est lancée à un certain niveau déterminé par le niveau du skill magie. Si l'action ne se fait pas au tour où l'information complémentaire a été renseignée, le niveau du skill peut avoir changé (par exemple, si la classe parente gagne de l'xp par un autre skill (passif ou  déclenché) et en redistribue à ses skills en retour). La limite de cible, la portée etc. peuvent avoir augmenté.
Un projectile qu'on a choisi de lancer pourrait aussi avoir été volé.

Problématiques :
Comment renseigner les informations complémentaires (pour les magies, nom, classe ou objet ?), comment traiter les skills de créations de projectiles, etc.

Tout ça est lié au système tour-par-tour case-par-case.
On pourrait retirer le tour-par-tour, mais ça me semble compliqué.
Encore plus pour le case-par-case, en terme de génération et résolution des labyrinthes, décisions des esprits, collisions etc.
Le tour-par-tour case-par-case rendent le jeu plus sacadé mais ce serait moins le cas si les tours se faisait plus vite (acctuellement limité par les esprits), les espaces était plus grand (à la fois en termes de vision, portée, vitesse de déplacement (en mêeme temps, plus il y a de tours dans un déplacement d'une case, plus les différences de vitesses sembleront naturelles) etc.) ou les animations incluaient des étapes "intermédiaires".

Accessoirement, la latence est liée à l'élément de la glace qui ralentit les agissants (en augmentant leur latence restante, ce qui peut même potentiellement les figer).



Idée :

Avoir une "action en cours". L'action a une latence (durée restante) diminuée chaque tour et se termine lorsque la latence atteint 0. Plus de vitesse mais certains skills passifs peuvent faire diminer la latence plus rapidement.

La plupart des actions proviennent d'un skill (par exemple, le skill déplacement du joueur fournirait une action marche et une action course) et lui rendent des xp (quand ?). Les effets de type Magie deviendraient des actions.

Attente/interruption : que se passe-t-il si on change d'avis en cours d'action ? Pour le joueur et les autres agissants.
 - > Rien, l'action se termine (le plus logique).
 - > L'action est interrompue (problèmatique si certaines actions ont des effets (ou dans une moindre mesure des animations) progressifs, mais utile par exemple pour une fuite soudaine (possible stratégie de disruption de cast de magie, par exemple, quoique savoir un mage imobilisé peut faire aussi partie d'une stratégie) ou pour le joueur qui va vouloir plus de réactivité).

(Idée : interruptions possibles, la plupart des actions donne l'xp à la fin donc possibilité d'utiliser les interruptions pour ralentir son évolution (je pense en particulier à l'accomplissement de la paresse).)

L'agissant pourrait avoir une barre de chargement qui dénote la progression de son action en cours.

Certains agissants pourraient faire plusieurs actions en même temps (je pense à Kumoko, avec les parallel minds (body brain, magic brain, etc.) ou plus généralement à la possibilité de faire certaines actions en se déplaçant (lancer certaines magies, etc.)).

Les interactions avec l'inventaires seraient aussi des actions (pas reliées à des skills).

Certaines actions pourraient avoir des effets à différents moments. Par exemple, une attaque à l'épée qui touche le quart devant soi à droite, puis devant soi à gauche (aussi plus réaliste). Ou pour les magies qui attaquent à distance, d'abord placer l'attaque sur la case au tout début, puis la déclencher à la fin (justifierai mieux les attaque délayées aussi). Attention à deux choses : ne pas concentrer les effets au début, par risque que l'interruption permette d'ignorer la latence ; et s'assurer que la glace et son ralentissement excessif ne puisse pas ramener une action en arrière et, par exemple, permette de retaper le quart devant soi à droite.