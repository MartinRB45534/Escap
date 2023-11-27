# Offenses
## Jusqu'à maintenant :
Les offenses servent à informer l'esprit de la dangerosité et de l'importance des ennemis.

Elles sont un `Tuple[Agissant,float,float]` (autrefois `Tuple[int,float,float]`) contenant l'agissant, la dangerosité et l'importance en question. Souvent générées par des attaques (ou des instakills ratés (les instakills n'ont encore jamais été testés)) et peut-être par des préjugés.

## À partir de maintenant :
Les notions de dangerosité et d'importance ont disparu. L'observation va être utilisée plus systématiquement donc on ne saura pas toujours de qui vient une attaque, ou qui a boosté quelqu'un.

Mais il faudra continuer à reporter ces informations, quand on les a, à l'esprit.

On peut probablement se contenter de la vision pour observer la capacité de l'ennemi à infliger des dégâts, la portée qu'il peut atteindre (les effets sur les cases) et les capacités à maintenir les autres en vie ou les booster (les effets sur les agissants). On peut collecter ces informations 

Pour la nuisance, elle sera constatée en analysant les effets sur nos propres agissants.

Donc plus besoin des offenses, du tout ?