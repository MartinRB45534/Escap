#Un fichier avec des constantes d'équilibrage.
#Pour modifier facilement l'équilibrage.


#Quelques constantes qui affectent tout le monde :
global LATENCE_DEPLACEMENT #La latence ajoutée à chaque utilisation du skill de déplacement. Augmenter cette valeur pour ralentir tout le monde
LATENCE_DEPLACEMENT =
global LATENCE_COURSE #La latence ajoutée à chaque utilisation du skill de course. Augmenter cette valeur pour ralentir le joueur
LATENCE_COURSE =
global LATENCE_STOMP #La latence ajoutée à chaque utilisation du skill de stomp (attaque sans arme). Affecte la fréquence d'attaque de certains humains
LATENCE_STOMP =
global LATENCE_ATTAQUE #La latence ajoutée à chaque utilisation du skill d'attaque. Affecte la fréquence d'attaque de presque tous les ennemis et certains humains
LATENCE_ATTAQUE =
global TAUX_STOMP #Le taux d'utilisation de la force de l'agissant lors d'un stomp. Augmenter cette valeur pour augmenter les dégats de stomp de tout le monde
TAUX_STOMP =
global TAUX_ATTAQUE #Le taux d'utilisation de la force de l'agissant lors d'une attaque. Augmenter cette valeur pour augmenter les dégats d'attaque de tout le monde
TAUX_ATTAQUE =


#Les constantes du joueur :
global FORCE_JOUEUR #La force du joueur. Augmenter cette valeur pour que le joueur cause plus de dégats
FORCE_JOUEUR =
global VITESSE_JOUEUR #La quantité de latence soustraite à chaque tour. Augmenter cette valeur pour accélèrer toutes les actions du joueur. /!\ Si la vitesse est supérieure à la latence de certains skills, le joueur risque d'utiliser le skill plusieurs fois dans un tour
VITESSE_JOUEUR =
global PV_JOUEUR #Le nombre maximum de PVs du joueur. Augmenter cette valeur pour que le joueur soit plus difficile à tuer
PV_JOUEUR =
global REGEN_JOUEUR #La quantité de PVs restaurés chaque tour. Augmenter cette valeur pour que le joueur se soigne plus vite
REGEN_JOUEUR =


#Queqlues constantes qui affectent plein de gobelins
global TAUX_LANCE #Le taux d'utilisation de la force de l'agissant lors d'une attaque à la lance. Augmenter cette valeur pour augmenter les dégats causés avec une lance (par les sentinelles gobelin ou le joueur)
TAUX_LANCE =
global TAUX_EPEE #Le taux d'utilisation de la force de l'agissant lors d'une attaque à l'épée. Augmenter cette valeur pour augmenter les dégats causés avec une épée (par les gobelins de base, le chef gobelin ou le joueur)
TAUX_EPEE =
global TAUX_CIMETERE #Le taux d'utilisation de la force de l'agissant lors d'une attaque au cimetère. Augmenter cette valeur pour augmenter les dégats causés avec un cimetère (par les guerriers gobelins)
TAUX_CIMETERE =
global TAUX_ARMURE_SENT #Le taux de dégats bloqués par une armure de sentinelle. Augmenter cette valeur pour que les sentinelles perdent moins de PVs.
TAUX_ARMURE_SENT =
global TAUX_HAUME #Le taux de dégats bloqués par un haume. Augmenter cette valeur pour que les sentinelles perdent moins de PVs.
TAUX_HAUME =
global TAUX_ARMURE_GUER #Le taux de dégats bloqués par une armure de guerrier. Augmenter cette valeur pour que les guerriers perdent moins de PVs.
TAUX_ARMURE_GUER =
global MANA_BANDEAU #La quantité de PMs restaurés par un bandeau à chaque tour. Augmenter cette valeur pour que les mages gobelins récupèrent plus vite leurs PMs (attaquent plus souvent). Ils seront quand même limités par la latence du sort.
MANA_BANDEAU =


#Les constantes du premier monstre :
global FORCE_PREMIER #La force du premier monstre. On veut qu'il soit spécialement affaibli puisque c'est le premier combat.
FORCE_PREMIER =
global VITESSE_PREMIER #La vitesse du premier monstre. On veut qu'il soit spécialement affaibli puisque c'est le premier combat.
VITESSE_PREMIER =
global PV_PREMIER #Les PVs du premier monstre. On veut qu'il meurt relativement facilement (c'est long, mais looooong, actuellement !)
PV_PREMIER =

#Les constantes du deuxième monstre :
global VITESSE_DEUXIEME #La vitesse du deuxième monstre. On ne veut pas qu'il tue le joueur avant que ce dernier se soit rapproché !
VITESSE_DEUXIEME =
global PV_DEUXIEME #Les PVs du deuxième monstre. On ne veut pas qu'il soit trop résistant
PV_DEUXIEME =
global PM_DEUXIEME #Les PMs du deuxième monstre. Permet de limiter sa capacité d'attaque
PM_DEUXIEME =
global REGEN_DEUXIEME #La régénération des PMs du deuxième monstre. On pourrait callibrer pour qu'il descende la moitié de la vie du joueur avant de tomber à court de mana et s'enfuir.
REGEN_DEUXIEME =

#Les constantes du paumé :
global FORCE_PAUME #La force du paume. On ne veut pas qu'il soit trop fort
FORCE_PAUME =
global VITESSE_PAUME #Le paumé doit être suffisament rapide pour manoeuvrer jusqu'en première ligne facilement
VITESSE_PAUME =
global PV_PAUME #Le paumé a besoin de beaucoup de PVs pour prendre des coups
PV_PAUME =
global REGEN_PAUME #On veut qu'il se régénère vite
REGEN_PAUME =
global TAUX_TUNIQUE #La tunique est à calibrer aussi en fonction du joueur (on peut augmenter les PVs pour réduire les stats de la tunique sans modifier les performances du paumé)
TAUX_TUNIQUE =

#Les constantes de la peureuse :
global FORCE_PEUREUSE #La peureuse est faible ! Très faible
FORCE_PEUREUSE =
global VITESSE_PEUREUSE #La peureuse doit être relativement rapide pour fuir
VITESSE_PEUREUSE =
global PV_PEUREUSE #La peureuse est fragile, mais on ne veut pas qu'elle meurt trop facilement non plus
PV_PEUREUSE =
global REGEN_PEUREUSE #On ne veut pas qu'elle se régénère trop vite (en même temps, vu ses PVs...)
REGEN_PEUREUSE =
global PM_PEUREUSE #Il lui en faut beaucoup... mais c'est combien, beaucoup
PM_PEUREUSE =
global REGEN_PM_PEUREUSE #Ce serait bien qu'elle ait presque toujours les PMs pour faire tout ce qu'elle veut
REGEN_PM_PEUREUSE =
global REGEN_PM_ROBE #Quelle portion de la regen attribuer à la robe ? La moitiée ?
REGEN_PM_ROBE =
global PM_BOOST #Le cout de la magie de boost. Affecte aussi les shamans. Vu que ça se fait de loin, donc sans vraiment de risque on pourrait avoir une efficacité inférieure à 1PV = 2PMs en se basant sur les dégats par attaque des autres agissants
PM_BOOST =
global TAUX_BOOST #Le taux de dégats supplémentaires pour la magie de boost. Le prendre ne compte dans le calcul des dégats des différents gobelins
TAUX_BOOST =
global LATENCE_BOOST #La latence de la magie de boost. On pourrait réduire la latence et le taux, pour éviter d'avoir un coup surpuissant au milieu d'un tas de faibles
LATENCE_BOOST =
global PM_MULTI_BOOST #Le cout de la magie de multi_boost. Rendre un peu plus cher que le boost, pour justifier de se rabbatre sur le boost quand on n'a pas assez d'xp pour le multi_boost
PM_MULTI_BOOST =
global TAUX_MULTI_BOOST #Le taux de dégats supplémentaires pour la magie de multi_boost. Faire des statistiques sur le nombre d'agissants boostés en moyenne pour déterminer comment calculer le taux de conversion PV/PM
TAUX_MULTI_BOOST
global LATENCE_MULTI_BOOST #La latence de la magie de multi_boost. Pas trop élevée car le coût est le véritable facteur limitant
LATENCE_MULTI_BOOST

#Les constantes du troisième monstre :
global FORCE_TROISIEME #Le troisième monstre pourrait être presque au niveau des sentinelles standards
FORCE_TROISIEME =
global VITESSE_TROISIEME
VITESSE_TROISIEME =
global PV_TROISIEME #Peut-être le faire mourir juste un peu plus vite.
PV_TROISIEME =

#Les constantes des sentinelles :
global FORCE_SENT #Les sentinelles ne sont pas très fortes
FORCE_SENT =
global VITESSE_SENT #Les sentinelles sont plutôt lentes, pour éviter qu'elles ne s'enfuit trop
VITESSE_SENT =
global PV_SENT #Les sentinelles ont beaucoup de PVs
PV_SENT =

#Les constantes des guerriers :
global FORCE_GUER #Les guerriers sont très forts
FORCE_GUER =
global VITESSE_GUER #Plutôt rapides aussi
VITESSE_GUER =
global PV_GUER #Mais assez fragiles
PV_GUER =

#Les constantes de l'encombrant :
global FORCE_ENCOMBRANT #On veut qu'il soit relativement fort
FORCE_ENCOMBRANT =
global TAUX_EPEE_ENCOMBRANT #Et qu'il ait une arme correcte au cas où le joueur la lui volerai
TAUX_EPEE_ENCOMBRANT =
global VITESSE_ENCOMBRANT #Qu'il soit correctement rapide
VITESSE_ENCOMBRANT =
global PV_ENCOMBRANT #Qu'il ait des PVs, mais pas trop
PV_ENCOMBRANT =
global REGEN_ENCOMBRANT #Qu'il ait une bonne regen
REGEN_ENCOMBRANT =
global TAUX_ARMURE_ENCOMBRANT #Et une armure pas trop puissante
TAUX_ARMURE_ENCOMBRANT =

#Les constantes de l'alchimiste :
global FORCE_ALCHIMISTE #L'alchimiste n'est pas bien fort
FORCE_ALCHIMISTE =
global VITESSE_ALCHIMISTE #Il n'est pas spécialement rapide
VITESSE_ALCHIMISTE =
global PV_ALCHIMISTE #Il a des PVs corrects
PV_ALCHIMISTE =
global REGEN_ALCHIMISTE #Une regen standard
REGEN_ALCHIMISTE =
global PM_ALCHIMISTE #Plutôt beaucoup de PMs
PM_ALCHIMISTE =
global REGEN_PM_ALCHIMISTE #Une regen de PM correcte mais inférieure aux autres mages
REGEN_PM_ALCHIMISTE =
global REGEN_PM_TUNIQUE #Est-ce que la tunique aide vraiment avec les PMs ?
REGEN_PM_TUNIQUE =
global COUT_SECOUSSE #Le cout de la magie de secousse. Pas très elevé
COUT_SECOUSSE =
global DEGATS_SECOUSSE #Pas beaucoup de dégats
DEGATS_SECOUSSE =
global PORTEE_SECOUSSE #Une grosse portée
PORTEE_SECOUSSE =
global LATENCE_SECOUSSE #Plutôt lent
LATENCE_SECOUSSE =

#Les constantes des mages :
global PV_MAGE #Les mages sont fragiles
PV_MAGE =
global VITESSE_MAGE #Plutôt lents ? Rapides ? À voir
VITESSE_MAGE =
global PM_MAGE #Les PMs détermine la durée de la première phase où ils peuvent faire beaucoup de dégats
PM_MAGE =
global COUT_MAGE #Le coût du sort des mages gobelins. On pourrait décider de 1 PM = 1 PV comme taux de conversion moyen
COUT_MAGE =
global DEGATS_MAGE #Les dégats causés par le sort des mages gobelin. Garder en tête qu'ils peuvent être boostés (multipliés par 2) et qu'on ne veut surtout pas de 1-shot
DEGATS_MAGE =
global LATENCE_MAGE #Le temps d'attente entre deux sorts d'un mage gobelin (pendant qu'ils ont assez de PMs)
LATENCE_MAGE =
global REGEN_MAGE #Calibrer leur régénération pour qu'ils fassent moins de dégats que les autres gobelins après un certain temps
REGEN_MAGE =

#Les constantes des shamans :
global PV_SHAMAN #Ils sont très fragiles
PV_SHAMAN =
global VITESSE_SHAMAN #Plutôt rapides
VITESSE_SHAMAN =
global PM_SHAMAN #Peut-être pas trop de PMs puisqu'ils ont d'autre avantages ?
PM_SHAMAN =
global REGEN_SHAMAN #Une regen correcte
REGEN_SHAMAN =

#Les constantes de la peste :
global FORCE_PESTE #Elle n'est pas forte
FORCE_PESTE =
global VITESSE_PESTE #Pas trop lente
VITESSE_PESTE =
global PV_PESTE #IElle a des PVs moyens
PV_PESTE =
global REGEN_PESTE #Une regen standard
REGEN_PESTE =
global PM_PESTE #Plutôt beaucoup de PMs
PM_PESTE =
global REGEN_PM_PESTE #Une bonne regen de PM
REGEN_PM_PESTE =
global DEGATS_SOUTANE #Le soutane limite les dégats par attaque à un plafond fixé. Moins utile contre les ennemis nombreux ou rapides, mais efficace pour éviter les one-shot
DEGATS_SOUTANE =
global PM_SOIN #Le cout de la magie de soin
PM_SOIN =
global PV_SOIN #Les PVs restaurés par chaque sort de soin. Essayer d'établir un taux de conversion PV/PM, peut-être semblable à ceux des attaques ?
PV_SOIN =
global LATENCE_SOIN #La latence de la magie de soin
LATENCE_SOIN =
global PM_MULTI_SOIN #Le cout de la magie de multi_soin. Légèrement plus cher que le soin
PM_MULTI_SOIN =
global PV_MULTI_SOIN #Les PVs restaurés par la magie de multi_soin. Au moins autant que la magie de soin
PV_MULTI_SOIN
global LATENCE_MULTI_SOIN #La latence de la magie de multi_soin
LATENCE_MULTI_SOIN

#Les constantes de la bombe atomique :
global FORCE_BOMBE #Elle n'est pas bien fort
FORCE_BOMBE =
global VITESSE_BOMBE #Pas spécialement rapide
VITESSE_BOMBE =
global PV_BOMBE #Elle a des PVs moyens
PV_BOMBE =
global REGEN_BOMBE #Une regen standard
REGEN_BOMBE =
global PM_BOMBE #Beaucoup de PMs
PM_BOMBE =
global REGEN_PM_BOMBE #Une bonne regen de PM
REGEN_PM_BOMBE =
global REGEN_PM_ROBE_SORCIERE #Et encore plus de regen de PMs
REGEN_PM_ROBE_SORCIERE =
global REGEN_PM_CHAPEAU_SORCIERE #Et encore plus de regen de PMs
REGEN_PM_CHAPEAU_SORCIERE =
global COUT_VOLCAN #Coût élevé
COUT_VOLCAN =
global DEGATS_VOLCAN #Beaucoup de dégats (genre, 2-shot un mage ou un gobelin de base ?)
DEGATS_VOLCAN =
global PORTEE_VOLCAN #Petite portée
PORTEE_VOLCAN =
global LATENCE_VOLCAN #Plutôt lent
LATENCE_VOLCAN =

#Les constantes des gobelins de base :
global FORCE_GOB #Les gobelins de base sont faibles
FORCE_GOB =
global VITESSE_GOB #Et lents
VITESSE_GOB =
global PV_GOB #Et fragiles
PV_GOB =

#Les constantes du marchand :
global FORCE_MARCHAND #Il est faible
FORCE_MARCHAND =
global TAUX_EPEE_MARCHAND #Mais son équippement est très bon
TAUX_EPEE_MARCHAND =
global VITESSE_MARCHAND #Il a une vitesse moyenne
VITESSE_MARCHAND =
global PV_MARCHAND #Peu de PVs
PV_MARCHAND =
global REGEN_MARCHAND #Une regen moyenne (peut-être qu'il a des potions de soin ?)
REGEN_MARCHAND =
global TAUX_ARMURE_MARCHAND #Et son armure réduit chaque attaque d'une valeur donnée. Les attaques plus faibles sont annulées.
TAUX_ARMURE_MARCHAND =

#Les constantes des gobelins de base :
global FORCE_CHEF #Le chef est fort
FORCE_CHEF =
global VITESSE_CHEF #Relativement rapide
VITESSE_CHEF =
global PV_CHEF #Mais surtour solide
PV_CHEF =
global REGEN_CHEF #Et se soigne
REGEN_CHEF =

#Les constantes du receptionniste :
global FORCE_RECEPTIONNISTE #On veut qu'il soit fort (plus que l'encombrant, mais avec la même arme)
FORCE_RECEPTIONNISTE =
global VITESSE_RECEPTIONNISTE #Qu'il soit correctement rapide
VITESSE_RECEPTIONNISTE =
global PV_RECEPTIONNISTE #Qu'il ait un peu plus de PVs que l'encombrant (et la même armure)
PV_RECEPTIONNISTE =
global REGEN_RECEPTIONNISTE #Qu'il ait une bonne regen
REGEN_RECEPTIONNISTE =
