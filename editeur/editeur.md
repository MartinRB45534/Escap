Qu'est-ce que l'éditeur ?

Pour commencer, quelques onglets :

Espèces
Effets
Items
Skills
Agissants
Decors
Labyrinthe

Sous la forme d'une liste à gauche, avec possibilité d'en sélectionner un et d'ouvrir la fenêtre associée.

Comment sont stockées les données pendant l'édition ?

Classe Jeu avec :
- Liste d'espèces (classe Espece, a un nom et un nombre de doigts)
- Les effets (liste des informations : nom, niveau (optionel), classe, autres paramètres)
  (Pas d'exemple en tête pour l'instant, mais je verrai quand j'aurai à créer des parchemins et des potions)
- Les catégories d'items classiques :
  - Parchemins (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Par exemple pour l'instant il existe deux classes de parchemins : le parchemin vierge, qui prendra en paramètre ses taux de coût et de latence de caste et d'impregnation, et le parchemin préécrit, qui prendra en paramètre son effet, son coût et sa latence de caste)
  - Potions (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Correspond aux parchemins préécrits, mais sans coût de mana)
  - Clés (y revenir après la génération du labyrinthe)
  - Projectiles (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes de projectiles sont multiples, entre les flèches, les explosifs, les projectiles magiques, etc.)
  - Armes (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes d'armes se limitent aux épées et lances pour l'instant)
  - Boucliers (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes de boucliers correspondent aux différentes façons d'intercepter une attaque (une seule pour l'instant))
  - Anneau (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes d'anneaux correspondent aux différents effets qu'ils peuvent avoir actuellement uniquement des regens de pv et de mana)
  - Armures (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes d'armures sont à créer)
  - Heaumes (liste des informations : nom, niveau (optionel), classe, autres paramètres)
    (Les classes de heaumes sont à créer)
  (Les cadavres et les oeufs n'ont pas besoin d'être définis ici je pense)
- Les skills (liste des informations : nom, niveau, classe, autres paramètres)
- Les classes (liste des informations : nom, niveau, classe, autres paramètres)
- Les agissants (liste des informations : nom, niveau, espece(s), equipement, (autres items), classes, skills, stats, autres paramètres)

TODO : valeur par défaut
