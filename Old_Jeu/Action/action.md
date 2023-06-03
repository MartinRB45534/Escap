Comment faire les magies/parchemins/potions ?

Actuellement une magie est un effet placé sur le joueur, qui ajoute d'autres effets, crée un agissant, etc.
Les consommables placent une effet (parfois une magie) sur le joueur.

En actions :
L'invocation d'une magie sera une action (remplace les effets de la classe Magie).
L'utilisation d'un item sera une action.
Dans le cas d'un parchemin de magie, il faut une seule action.



Au final, une magie c'est :
 - > Un effet (pas Effet) lorsqu'elle est lancée. Voire même plusieurs (attaque délayée par exemple) à des moments distincts.
 - > Un coût en mana (déjà partiellement payé dans le cas d'un parchemin imprégné).
 - > Une latence (peut-être différente dans le cas d'un parchemin imprégné).
 - > Un skill a qui rendre de l'xp (sauf peut-être pour les parchemins).
 - > Un niveau (niveau du skill lors de l'imprégnation du parchemin).



Conclusion :
Chaque magie est deux actions (version normale et parchemin).
Certaines potions ou parchemin ont simplement une action qui place un Effet (soin par exemple).
Une potion ou parchemin peut porter de nombreux types d'actions (en théorie).