# Comment gérer les maladies ?

Deux questions :

## Effets

Quels genres d'effets je donne aux maladies ? Qu'est-ce que je veux avoir comme maladies différentes dans le jeu ?

### Idées actuelles :

#### Tirgnonose

Une maladie qui "grignote" l'agissant en lui retirant des pvs à chaque tour.

#### Fibaluse

Une maladie qui rend l'agissant "faible" en appliquant une modification à toutes ses stats.

#### Ibsutiomialgie

Une maladie de mort "subite" qui peut tuer l'agissant au moment où il la contracte.

### Combinaisons d'effets

Est-ce qu'on veut avoir des maladies qui combinent plusieurs effets ?

### Nombre de maladies

Les maladies sont un élément très secondaire du jeu, il vaudrait mieux ne pas trop en avoir.
D'autant plus si les maladies ont des niveaux (il y en tout de suite dix fois plus).

## Immunité

### Idées actuelles :

#### L'étage des vaccins

Une zone où une ou plusieurs maladies se propagent.
À l'entrée le joueur peut choisir parmi quatre "vaccins" (au plus un) à administrer à lui-même et ses alliés (et les vaccins protègent plus ou moins bien et ont plus ou moins d'effets indésirables).

Il faut donc des maladies qui soient punitives si le joueur n'a pas le vaccin parfait mais la zone doit quand-même être faisable avec le vaccin déficient qui n'a que des effets indésirables.

Les maladies pourraient avoir des séquelles durables qui handicaperaient le joueur sur les niveaux suivants (l'étage des vaccins est proche de la fin du jeu).

#### La stratégie du porteur sain

Le joueur s'immunise contre une maladie puis se l'inocule pour aller la porter aux ennemis. Il faut donc qu'on puisse être porteur sain d'une maladie.

#### La stratégie du lancer de maladie

Un build axé sur le lancer pourrait envoyer des potions contenant une maladie pour contaminer ses ennemis. Il resterait ensuite loin jusqu'à ce que les ennemis soient morts.

### PNJs

Il faut aussi prendre en compte que les PNJs ne partagent pas l'immunité du joueur. À moins de trouver un grand nombre de potions de maladie qui trainent, le joueur a besoin au moins du marchand ou de l'alchimiste, mais ils risquent de se faire contaminer s'il n'y a pas un système très efficace de commande des PNJs.

## Idées

### Maladies "spécistes"

Certaines maladies pourraient ne toucher que certaines espèces.

Les agissants d'autres espèces deviendraient naturellement des porteurs sains.

### Fibaluses ciblées

Une fibaluse par stat, plus une globale.

### Fibaluses avec sequelles

Les fibaluses pourraient optionnellement avoir des séquelles sur le long terme.

### Médicaments/purification/antidote ciblés/nivelés

Les effets de soin (au sens général) pourraient ne fonctionner que sur les effets négatifs de niveau inférieur ou égal.

### Immunité transposable

L'immunité à une maladie protégerait aussi des maladies similaire (peut-être pas aussi bien ?).

### Trois types d'immunité

- non contagieux (ne peut pas transmettre la maladie) ;
- non infectable (ne peut pas attrapper la maladie) ;
- non affectable (n'est pas affecté lorsqu'il l'a).

Un agissant pourrait avoir n'importe quelle combinaison de ces immunités pour chaque maladie.

Là encore, les niveaux, les similarités entre maladies et le temps pourraient mener à des immunités partielles.

## Comment stocker les immunités ?

### Dans les stats

Ce ne sont pas des stats au sens propre, mais l'objet des stats pourrait contenir un dictionnaire d'immunités.

Le dictionnaire préciserait de quel type d'immunité il s'agit, à quoi est l'immunité (maladie ou famille de maladie), et une sorte de priorité/niveau d'immunité.

## Comment appliquer les immunités

### Comme les médicaments

Ou plutôt les médicaments s'appliquent comme les immunités.

La maladie ciblé est informée de la priorité/du niveau d'immunité et s'affaiblie/disparaît en conséquence (pour les immunités de type "non affectable").

Pour la contagion et l'infection, la maladie consulte les immunités à ce moment-là.

## Comment modifier les immunités

### Par les maladies

Une maladie peut modifier les immunités de l'agissant (seulement les augmenter ?), à la fois à elle-même et à sa famille de maladies.

#### Maladies qui attaquent le système immunitaire, type sida ?

Ça part loin, on va s'en passer. Les stats s'assureront que toute modification d'une immunité l'augmente.

### Par des sorts/skills/items

Un sort ou un item pourraient placer sur l'agissant un effet d'immunité, que les stats iraient consulter pour connaitre les immunités à un instant donné.

Les stats consultent aussi les skills pour trouver un éventuel skill qui modifie les immunités de l'agissant.

#### Modification permanente

Est-ce qu'un item ou un skill pourraient modifier de façon permanente l'immunité d'un agissant ?

Je pense à la potion de "vaccin".

Pour le skill, il suffit que les stats aillent le consulter au besoin.

## Quels effets ont les immunités partielles ?

Qu'est-ce qui se passe lorsque l'un des type d'immunité n'est pas nul mais pas suffisant ?

### Non contagiosité

En l'absence de ce type d'immunité, la probabilité de contaminer un voisin est non-nulle (sinon on aurait juste mis un poison).

En présence d'un imunité suffisante, la probabilité de contaminer un voisin est nulle.

En présence d'une immunité insuffisante, il y a une plus faible chance de contagion.

Comment la calculer ?

En fait, puisque la priorité est prise en compte, l'absence totale d'immunité n'existe pas.

#### Idée : échelle de 1 à 10

(Puisque la priorité augmente avec le niveau, il suffirait d'être a niveau max, d'avoir une immunité au niveau max ou d'avoir pris toutes les améliorations de priorité pour être complêtement immunisé.)

#### Meilleure idée

Le calcul ressemblerait à immunité + priorité - contagiosité = probabilité de ne pas transmettre.

#### Idée : distance

La non-contagiosité pourrait diminuer la distance de contagion de la maladie.

# Résumé

## Immunités

Les immunités font partie des stats. Elles peuvent être affectées par divers éléments, les stats gèrent tout ça.

Les statistiques brutes d'immunité ne peuvent qu'augmenter.

Lorsque plusieurs immunités (maladie, groupe, item, effet, skill) sont valables, c'est la plus élevée qui compte.

## Maladies

Les maladies peuvent apartenir à des familles de maladies.

Les maladies peuvent avoir divers effets sur l'agissant.

À chaque tour, la maladie consulte l'immunité, puis potentiellement l'augmente et/ou s'arrête.
