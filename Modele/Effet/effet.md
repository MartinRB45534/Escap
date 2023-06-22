# Effets

Que faire des effets ?

Problème :
Le type-checking strict n'aime pas les effets et leurs méthodes `execute` et `action` dont le type d'argument varie.

Les effets commencent déjà à se séparer en plusieurs groupes : sur les cases, les auras sont stockées à part ; les magies et la majeure partie des attaques ont été transformées en actions (les deux constituant une grande part des anciens effets).

Il n'y a pas d'effet qui puisse se placer à la fois sur un agissant et un item, ou un agissant et une case, on pourrait les distinguer sur ce critère pour commencer.

Par contre, il y a les `Enchantements` qui englobent des effets sur beaucoup d'éléments différents.

D'autres exemples ?
Les `Evenements`, `One_shot`, etc. peuvent être présents sur des choses très différentes.

Listons les effets actuels.

Par temps d'appel :
 - `On_need` (spécialement créé pour les réserves de mana, 1 agissant) ;
 - `On_tick` (à chaque tour, sans plus de précision) :
   - `On_debut_tour` (beaucoup d'enchantements, poison, obscurité, investissement, 2 items, 1 case, 13 agissants) ;
   - `On_post_decision` (maladie, confusion, 2 agissants) ;
   - `On_post_action` (blizzard, téléportation, instakill, protection, soin, 2 cases, 3 agissants) ;
   - `On_fin_tour` (enseignement, sursis, réanimation, résurection, antidote, médicament, purification, soin, 3 items, 5 agissants) ;
 - `On_attack` (appelé sur les attaques, protections, 1 agissant, 1 case).

Par durée d'appel :
 - `One_shot` (9 agissants, 1 item) ;
 - `Delaye` (comme `One_shot`, avec un délai, 1 case) ;
 - `Evenement` (sur plusieurs tours et hérite de `On_tick` (appelé à chaque tour), blizzard, obscurité, investissement, aura, 3 cases, 1 agissant) ;
 - `Enchantement` (hérite de `Evenement`, cas particulier, 12 agissants, 2 items) ;
 - `Time_limited` (sur plusieurs tours mais appelé irrégulièrement, dopage, protections, 2 agissants, 1 case).

Par source :
 - action (donc souvent skill actif) :
   - magie (certaines magies produisent des effets, dont les enchantements) ;
   - attaque (une attaque peut être aussi une magie) ;
   - protection (pareil, peut aussi être une magie) ;
   - consommation (l'effet était stocké dans un consommable, peut encore être une magie) ;
 - aura (skill passif) ;
 - autre effet :
   - attaques (une attaque sur la case cause une attaque sur son occupant, s'il y en a un) ;
   - maladies (se propagent par contagion) ;
 - automatique (sursis par exemple, pour les items).