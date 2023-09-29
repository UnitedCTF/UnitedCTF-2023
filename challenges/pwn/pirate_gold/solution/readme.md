# Pirate Gold

## Analyse

L'application nous invite à acheter différents articles avec nos doubloons. L'objectif est d'acheter la carte au trésor légendaire pour obtenir le drapeau. Cependant, son coût est astronomique.

À l'analyse du code, on remarque qu'il y a une vulnérabilité liée à un dépassement d'entier lors de l'achat d'un article. Si le coût de l'article est supérieur à notre solde actuel, la vérification échoue comme prévu, mais s'il s'agit du coût d'une carte normale (1 doubloon), notre solde est quand même décrémenté, provoquant un débordement d'int.

## Exploitation

1. Lancez l'application.
2. Sélectionnez l'option 2 jusqu'à ce qu'on ne puisse plus.
3. Sélectionnez l'option 3 jusqu'à ce qu'on ne puisse plus.
4. Sélectionnez l'option 4 jusqu'à ce qu'on provoque un débordement d'entier (underflow) sur le uint.
5. Avec le solde devenu énorme, on peut acheter la carte légendaire.

Sinon regarder le script python : [solve.py](solve.py)

## Flag

`flag-p1r4t3801d_1s_e4sy_dc058c2c`
