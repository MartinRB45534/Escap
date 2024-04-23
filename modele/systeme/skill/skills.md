Qu'est-ce qu'un skill ?
Capacité d'un agissant qui lui permet de faire des choses.

Quelles sont les différents types de skills ?
Intrasecs et autres. Les intrasecs sont plus intimement liés à une classe. Ils évoluent avec la classe, et non individuellement. Est-ce qu'un skill peut être ou non intrasec selon les circonstances, ou est-ce qu'un skill donné est forcément intrasec ou non intrasec ?
Actif/passif. Les skills actifs sont utilisés pour générer les Actions. Ils sont spécifiquement appelés par le joueur ou les esprits. Les autres skills sont recherchés et activés au besoin.

Sur les skills intrasecs :
Est-ce qu'un skill est intrasec définitivement, ou parfois pas ?
Est-ce qu'un même skill peut être intrasec chez quelqu'un et pas chez quelqu'un d'autre ?
Est-ce qu'un skill intrasec est lié à une classe spécifique ? Ou est-ce qu'un même skill intrasec peut se retrouver dans des classes différentes ?

#### (Après avoir retravailler pas mal d'autres classes, dont les actions et les effets)
# Qu'est-ce qu'un skill ?

Deux choses très différentes :

## Skills actifs

Les skills actifs sont des fournisseurs d'actions.

Ils répondent à une décision en donnant l'action correspondante.

Utiliser un skill, c'est obtenir l'action, puis l'instancier. Le reste se fait tout seul.

### Difficultées :

#### Signatures

La signature de la fonction qui renvoie l'action (en particulier ses arguments) risque de changer d'un skill à l'autre. Certains n'ont qu'une action, d'autres plusieurs et il faut choisir.

#### Actions multiples

Il faut que l'interface d'exécution des skills, et l'interface de choix des touches, gèrent le fait que certains skills actifs proposent plusieurs actions.

Il est aussi possible qu'un même skill passe d'une à plusieurs actions en augmentant de niveau.

## Skills passifs

Des effets permanents, en quelque sorte.

Les skills passifs peuvent avoir des effets très variés :
- modification de stat ;
- interaction avec les projectiles lancés ;
- interaction avec les attaques utilisées ;
- interaction avec les dégats reçus ;
- effets plus uniques (immortalité, essence magique, etc.) ;
- auras ;
- etc.

### Difficultés :

Il y en a beaucoup de très différents. L'ajout d'un nouveau skill requierra probablement souvent la modification du code existant...
