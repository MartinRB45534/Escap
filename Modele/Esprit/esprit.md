# À quoi sert l'esprit ?

Origine : les meutes (ça me rajeunit pas...) qui permettaient à plusieurs ennemis de converger vers le joueur simultanément. C'était une vision partagée qui permettait une recherche du joueur commune.

Maintenant : l'esprit gère les vues des agissants (les regroupe et les mémorise), les ennemis (pour savoir qui attaquer) et donne les ordres.

Donc l'esprit sert à :
 - regrouper plusieurs agissant qui sont donc incapables de se nuir ;
 - mettre en commun l'information ;
 - coordonner les actions ;
 - établir les "stratégies".

Cela passe actuellement par :
 - l'appartenance ;
 - le regroupement des vues (en un ensemble cohérent) ;
 - les statuts (attaque, fuite, etc.) et les actions des supports ;
 - les ennemis, les calculs d'importance et de dangerosité des cases.

J'aimerais aussi y ajouter la gestion des embouteillages (surtout des croisements en fait).

D'un autre côté, l'IA parfaite n'est pas nécessaire. Pour les joueurs, il peut être plus intéressant d'avoir chez les monstres un pattern de mouvements simple et répétitif (c'est déjà un peu ce que j'essaye de faire avec les actions). Mais peut-être que je peux garder les IAs les plus efficaces sous le coude pour certains ennemis compliqués.

Ce que je voudrais mettre en place :
 - l'appartenance -> facile, revoir la structure exacte quand même ;
 - la vision -> en cours (blocage plus ou moins sur les informations contradictoires -> réfléchir à ce que je veux pouvoir cacher comme info exactement) ;
 - la mémoire -> lié à la vision, détailler l'oubli (y compris des infos contradictoires) ;
 - le retrait des statuts -> les actions suffisent amplement à indiquer ce que l'agissant va faire ensuite ;
 - les zones (-> connaissance imprécise des positions) et les espaces schématiques (-> couloirs et salles pour organiser les flots d'agissants) -> il faut probablement mieux distinguer les deux car ils n'ont rien en commun ;
 - les ennemis -> revoir avec peut-être un peu plus de complexité la caractérisation des ennemis.

## Appartenance

Actuellement, les corps sont stockés dans un dictionnaire. L'agissant sert de clé, la valeur est son statut.

Le statut sert à déterminer s'il peut agir et ce qu'il est en train de faire. Avec le retrait des statuts, on peut probablement les stocker maintenant dans un set.

Idée : ajouter une méthode `__contains__` à l'esprit.

## Informations contradictoires

Idées que j'ai eues jusqu'à maintenant :
 - item invisible (ne peut donc pas être ramassé car pas ciblé) ;
 - ouverture/porte invisible (possibilité d'interragir/de passer mais il faut que le joueur (le vrai, pas son personnage) sache qu'il y a une ouverture) ;
 - agissant invisible (on peut toujours le heurter ou l'attaquer) ;
 - agissant déguisé (donne de fausses informations sur ce qu'il est) ;
 - informations incomplètes (impossibilité de regarder dans l'inventaire d'un agissant, ou de voir les stats d'un item/agissant, etc.).

Comment fonctionne l'observation ?

Niveaux d'information de 0 à 10. Joueur de niveau 2 et monstre de niveau 2 -> information de niveau 0. Joueur de niveau 5 et monstre de niveau 1 -> information de niveau 4. Joueur de niveau 3 et monstre de niveau 10 -> information de niveau 0. Joueur de niveau 8 avec skill d'observation de niveau 7 et monstre de niveau 9 -> information de niveau 6. Le niveau d'information équivaut à niveau observateur + niveau skill observation - niveau observé, limité à 0-10.

Et la priorité dans tout ça ? Elle augmente avec le niveau ? Mais il y a des augmentations artificielles de la priorité. À réfléchir...

Bref.

Trois situations différentes :
 - invisibilité (item ou agissant dans le labyrinthe) - quelque chose est là, devrait être vu, mais ne l'est pas (de son propre fait) -> visible avec une observation suffisante ;
 - déguisement (agissant ou ouverture/porte dans un mur) - quelque chose apparait comme autre chose -> information correcte avec une observation suffisante ;
 - non-accès (stats ou inventaire) - une information dont on connait l'existence est dissimulée -> l'information est révélée avec une observation suffisante.

Dans le cas de l'invisibilité, un corps rapporte une information que les autres ne rapportent pas. Il suffit de toujours prendre toutes les présences rapportées par les corps (ne pas oublier de les retirer à la fin du tour).

Dans le cas du non-accès, les informations ne sont pas contradictoires. On peut conserver celles de l'observation la plus élevée. Les tours suivants, si une nouvelle information de niveau d'observation moins élevé est reçue, on peut mettre à jour les infos qu'on a et garder les anciennes (en les marquant comme telles) pour l'instant.

Dans le cas du déguisement, il doit y avoir contradiction (deux murs ou agissants différents au même endroit). On peut garder celui issu de l'observation la plus élevée et stocker l'autre comme un point d'accès au vrai (si on voit le déguisement d'un agissant quelque part, on sait que le vrai est là à sa place, même si le corps qui le voit ne sait pas les différencier). On peut ignorer le niveau du vrai (et sa résistance à l'observation) donc il vaut mieux se référer uniquement à la capacité d'observation de l'observateur au moment de l'observation.

## Oubli

Actuellement, chaque esprit a un temps d'oubli (rendu artificiellement infini pour les humains si ils comprennent la peureuse en vie) après lequel les cases sont effacées de sa mémoire. La caractérisation des ennemis est conservée définitivement mais réévaluée à  chaque tour.

Idée : la caractérisation et la vision sont à distinguer.

Les informations concernant un agissant (stats, équippement, appartenance) devraient être oubliées après un certain temps sans le voir. Conserve quand même l'idée approximative de sa position ? Probablement pas.

Temps d'oubli différent pour différentes infos ?

Pour l'oubli, on pourrait aussi modifier l'oubli des cases. Oublier moins vite (ou pas du tout) les cases proches (se souvenir d'une zone autour de la vision). Peut-être avoir une quantité de cases qu'on peut garder perpétuellement en mémoire ?

Pareil pour les agissants : garder perpetuellement les ennemis en mémoire, mais pas les neutres ? Avec la méchanique des zones, garder en mémoire les agissants qu'on sait être dans une zone délimitée, mais oublier ceux qui peuvent être n'importe où ?

Faire des esprits différents pour varier un peu ?

La variété c'est bien, mais il vaut peut-être mieux qu'elle se trouve dans des éléments plus tangible pour le joueur.

## Distinction des zones et des espaces schématiques

### Zones
Les zones servent à délimiter les emplacements possibles des neutres et des ennemis. La zone visible contient des informations complètes (ou presque, mais c'est pas la question ici). Les endroits mémorisés mais pas actuellement visibles peuvent être découpées en zones qui ne communiquent pas (pour ce qu'on en voit) : les zones inconnues. Les zones inconnues peuvent être fermées (une porte ouverte après qu'on y ait été peut fausser ça) auquel cas les agissants qu'on sait y être y restent. Elles peuvent aussi être ouvertes sur l'inconnu. Deux zones peuvent fusionner si on cesse de voir des cases qui les relient. Deux zones peuvent aussi communiquer en dehors de notre mémoire, donc si un agissant passe d'une zone à une autre on peut aussi les fusionner.

### Espaces schématiques
Les couloirs, les salles et les intersections servent à optimiser les calculs de trajets et de distances.

Deux agissants ne peuvent pas se croiser dans un couloir. Si chacun va à l'autre bout il convient que l'un des deux attende à l'entrée.

Lors des calculs de distance, on peut survoler les salles et les couloirs vides (sans obstacles, départ ou arrivée) si on connait déjà les distances entre leurs entrées. La problématique des temps de calcul se posera peut-être moins avec `networkx`.

## Caractérisation des ennemis
Actuellement, les ennemis sont caractérisés par leur dangerosité et leur importance. La dangerosité correspond à leur capacité à infliger des dégats (devrait idéalement représenter les dégats par tour, avec peut-être une augmentation avant qu'ils frappent et une diminution après, mais concrètement c'est juste la somme (ou peut-être le maximum) des dégats qu'ils ont infligé). L'importance représente leur participation aux dégats (inclus les supports, y compris les soigneurs) et devrait correspondre à la nécessité de les éliminer.

Là encore, pas besoin d'une IA parfaite. Mais il faut au minimum que le groupe du joueur soit résilient. Si les PNJs sont trop efficaces, le joueur n'a rien à faire. S'ils sont trop mauvais, le jeu ressemble à une quête d'escorte. Il faut à la fois qu'ils survivent, qu'ils soutiennent le joueur, qu'ils soient utiles, et que le joueur ait le rôle principal.

Avec la variété des builds que le joueur peut poursuivre, il faut faire attention qu'il ait toujours un rôle déterminant.

Petit rappel des builds (si je m'en souviens) :
 - Builds plus classiques :
   - Lancier/épéiste (DPS cac) ;
   - Skill défense et bouclier (Tank) ;
   - Archer/Skill lancer et explosifs (DPS distance) ;
   - Skill magie et magies offensives (DPS distance) ;
   - Skill magie et magies support/Ange (Support/Soin) ;
   - Enchanteur et magies CC (Support/Soutien/Buff/Debuff/CC) ;
   - Enchanteur et épéiste (DPS cac) ;
 - Builds plus originaux :
   - Skill écrasement et priorité (écraser les murs, les ennemis, tout) ;
   - Skill observation et sortie secrète (éviter les combats) ;
   - Skill vol et skill obseration et priorité (voler les clés, les stats, les skills, tout) ;
   - Fantome (traverser les murs et contourner les combats) ;
   - Nécromancien (constituer une gigantesque armée de monstres) ;
   - Élémentaliste (immunité aux trois éléments naturels + magies de ces trois éléments pour les ennemis de type ombre) ;

Les builds classiques s'inscrivent plus dans un groupe. La plupart des builds originaux se font plutôt en solo par nécessité (sauf l'élémentaliste, et peut-être l'écrasement).

Bref.

Pour que le groupe survive, il faut déterminer efficacement les zones de sécurité et de danger (en prenant en compte les éventuels tanks) et éliminer les menaces (chercher un contournement dans les étages où c'est possible).