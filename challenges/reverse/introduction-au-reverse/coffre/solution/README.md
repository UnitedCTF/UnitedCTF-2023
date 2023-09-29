# Introduction au Reverse 3 (Coffre)

## Write-up

Le but ici est de donner la bonne clé afin d'ouvrir le coffre. La clé est le flag et celle-ci est calculée dynamiquement pour la comparer avec celle entrée par l'utilisateur. La solution attendue est d'utiliser gdb, mettre un breakpoint à l'endroit dans la fonction de vérification où la comparaison est effectuée et observer le flag en mémoire. Les instructions explicites pour y parvenir sont similaires à celles expliquées dans la solution du premier challenge de cette track (bases). L'offset dans la fonction peut être calculé à partir des adresses que l'on voit dans Ghidra. On obtient alors 418, ce qui nous permet d'ajouter un breakpoint à `check_key+418` (`b *check_key+418`) et de s'y rendre (`c`). Finalement, on peut observer le flag sur le stack avec `telescope $rbp-0x110`. On peut trouver que c'est à cette endroit que le flag est écrit en analysant le programme dans Ghidra ou en l'exécutant une instruction à la fois dans gdb.

## Flag

`flag-for_God_and_Liberty`