Retirer les spécificités de la peureuse :
 - connaissances tribales (coennemis, dans Esprit_humain.get_offenses())
 - mémoire cartographique (pas d'oubli, dans Esprit_humain.oublie())
 - vérification de présence (dans Esprit_humain.peureuse())

Retirer la spécifité du paumé :
Dans deplace_pnj() et deplace_pj(), il n'est pas capable de chercher tout seul.

Chercher les différences entre deplace et deplace_pnj. Est-ce qu'on pourrait juste, pour déplace pnj, résoudre le chemin de déplacement (et mettre tout à 0 pour les autres) et mettre cette couche en plus importante ?

Il faudra modifier aussi les trucs spécifiques au joueur...