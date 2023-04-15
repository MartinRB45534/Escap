Ce fichier est un équivalent du readme, consacré aux questions et problémes qui concernent l'équilibre du jeu, créé pour limiter le readme aux questions et problémes de pure programmation (le systéme des classes, les mécaniques du jeu, les bugs et leur correction, etc.) et aux consignes d'utilisation. Il n'a aucune influence sur le fonctionnement du jeu et ses informations peuvent ne pas étre é jour.

Idée pour calibrer les "puissances" des monstres (juste les monstres qui combattent activement) et réajuster les capacités magiques :
Les "dégats par tour", rapport des dégats infligés en une attaque par l'intervalle entre deux attaques.
On pourrait facilement quotienter par les pvs pour prendre en compte la durée pendant laquelle le monstre peut infliger ces dégats, mais prendre en compte la régénération et les capacités défensives complique vraiment tout donc on va faire deux indicateurs séparés pour l'attaque et la défense.

Pour un monstre standard : dpt = dégats_de_l_attaque/latence_de_l_attaque

Pour les monstres qui utilisent la magie, un autre facteur entre en jeu
On aurait donc dpt1 = dégats_de_l_attaque/latence_de_l_attaque tant qu'il y a assez de magie, et dpt2 =  (dégats_de_l'attaque*régénération_du_mana)/cout_de_mana_de_l_attaque
On pourrait prendre en compte la capacité du monstre é faire une attaque physique pendant que sa magie se régénére dans le dpt2, mais flemme de calculer la formule

Pour deux monstres de niveau équivalent, l'un magique et l'autre non, on voudrait avoir dpt2<=dpt<dpt1 (il faut bien qu'il y ait un avantage pour les mages)

Par exemple pour les gobelins de niveau 1 du tutoriel :

Le gobelin de base n'est qu'é dpt_base

Le gobelin sentinelle est aussi é dpt_base, mais avec une meilleure défense

Le guerrier gobelin est é dpt_guerrier

Le mage gobelin est é dpt_mage1 ou dpt_mage2 selon les cas (peut fuir quand il manque de mana pour optimiser ses dégats totaux)

Avec dpt_mage1 > dpt_guerrier > dpt_base >= dpt_mage2.
L'idée est que le mage puisse vaincre un gobelin de base, mais pas un guerrier (et pour la sentinelle ?)

On aurait dpt_base légérement supérieur é la régénération du joueur, et le joueur (qui commence avec 100 pv parce que c'est un beau chiffre rond) soigne la moitié de sa vie en un temps raisonnable mais quand méme conséquent (plus que trois pas, mais moins qu'une quarantaine... é sa vitesse de début de partie). Tous les dpt du jeu seront calculés é partir de lé


On voudrait avoir des quantités de mana raisonables (un mage de bas rang a autant de pm max que de pv max, é peu prés). Pour les coéts, on se base sur le sort d'explosion de mana (celui dont on peut choisir le coét). Son taux de conversion au niveau 1 détermine le rapport "dégats par pm" de base, et tous les sorts doivent théoriquement faire mieux (difficile é dire pour une fléche ou un soin, évidemment)

On prend un peu au pif dpp_base = 1 et on verra ce que éa donne.






On veut que :
joueur > paume (sans équippement pour le joueur) donc :
temps de survie du joueur sous les coups du paumé > temps de survie du paumé sous les coups du joueur
pv du joueur//degats subits par le joueur > pv du paumé//degats subits par le paumé
pv_joueur//(degats du paumé - regen_joueur) > pv_paumé//(degats du joueur*defense_de_paumé - regen_paumé)
pv_joueur//(dpt_stomp_paumé - regen_joueur) > pv_paumé//(dpt_stomp_joueur*taux_degats_tunique - regen_paumé)
100//(2-1) > 150//(5*X-2)
100 > 150//(5*X-2)
5*X-2 > 1.5
X>0.7 avec X dans [0,1]
joueur > encomb (avec la tunique volée au paumé) donc :
temps de survie du joueur sous les coups de l'encomb > temps de survie de l'encomb sous les coups du joueur
pv du joueur//degats subits par le joueur > pv de l'encomb//degats subits par l'encomb
pv_joueur//(degats de l'encomb*defense_du_joueur - regen_joueur) > pv_encomb//(degats du joueur*defense_de_paumé - regen_paumé)
pv_joueur//(dpt_attaque_encomb*taux_degats_tunique - regen_joueur) > pv_encomb//(dpt_stomp_joueur*taux_degats_armure - regen_paumé)
100//(10*0.7-1) > 75//(5*x-1.5)
100//6 > 75//(5*x-2)
100*(5*x-2) > 75*6
500*x > 550
x>1.1 avec x dans [0,1]
joueur > tous individuellement, moyennant un équippement adéquat (volé sur des cadavres... humains)
sentinelle > guerrier
guerrier > 2~3 base
2~3 base > sentinelle
paume > sentinelle (parce que regen)
paume ~< guerrier
encomb > sentinelle
encomb > guerrier
march > sentinelle
march > guerrier
march > encomb (parce que stuff)
encomb > paume
paume = slime parce que regen pour les deux
encomb > slime
march > slime
guerrier >~ slime
sentinelle < slime


Stats stomp au niveau 1:
dpt_joueur = 5
dpt_recep = 5
dpt_paume = 2
dpt_encomb = 5
dpt_alchi = 1.5
dpt_peste = 1
dpt_bombe = 1.5
dpt_march = 3
dpt_gob = 2
dpt_gob_sent = 2
dpt_gob_guer = 5
dpt_gob_expl = 1
dpt_gob_mage = 2
dpt_gob_chef = 5
dpt_slime = 2

Stats attaque au niveau 1: (équippement standard de fin de tuto pour le joueur)
dpt_joueur = 8
dpt_recep = 10
dpt_encomb = 10
dpt_march = 8
dpt_gob = 3
dpt_gob_sent = 4
dpt_gob_guer = 10
dpt_gob_chef = 10

Stats attaque magique au niveau 1:
dpt_alchi1 = 3
dpt_alchi2 = 1
dpt_peste1 = 1.5
dpt_peste2 = 0.75
dpt_bombe1 = 10
dpt_bombe2 = 1
dpt_gob_mage1 = 3
dpt_gob_mage2 = 1



étages :
1 (tuto) pas de monstres
2 (tuto) pas de monstres
3 (tuto) gobelins lvl 1 (sentinelles)
4 (tuto) gobelins lvl 1 (sentinelle, mage, guerrier, base)
5 (tuto) gobelins lvl 1-2 (sentinelle, guerrier) slime lvl 1 ombriul lvl 1 (base)
6 (tuto) gobelins lvl 1-2 (guerriers, mages, shaman)
7 (tuto) gobelins lvl 1 (guerriers, mages, shamans, bases)
8 (tuto) gobelins lvl 1 (guerriers, sentinelles, mages, shamans, bases)
9 (tuto) gobelins lvl 1 (guerriers, sentinelles, mages, shamans, bases) (é partir d'ici les monstres sont pourvus de leur équippement)
10 (tuto) gobelins lvl 1-2 (guerriers, sentinelles, mages, shamans, bases, chef) ombriuls lvl 5-6 (variés, affaiblis)
1 pas de monstres

53 kumoko lvl 1 +araignée lvl 1-10 (vestige)

65 slime lvl 6 (noir)

70 slimes lvl 4-7 rimuru lvl 1

85-90 orcs lvl 9-10 gobelins lvl 10 etc lvl 9-10 ombriuls lvl 8-9

90-100 ombriuls lvl 9-10

