# Precise Map

## Off by one

Il s'agit d'un buffer overflow très courant : un off-by-one.

On commence par utiliser Ghidra pour analyser le code. On remarque un scanf qui prend 33 caractères et les place dans un buffer de 32. Il est donc immédiatement évident que la variable suivante sur la pile (dans ce cas, la variable qui est comparée) peut être écrasée. On peut ainsi révéler le secret en l'écrasant avec la valeur `!`.
Donc la solution est simplement de rentrer :

`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!`

## Flag

`flag-0ff-by-0n3-4r3-fun-db0835`
