# Introduction au Reverse 2 (Autopilote)

## Write-up

Ce défi se concentre sur l'analyse statique où le participant doit trouver la ville vers laquelle l'autopilote se dirige. Le programme contient plusieurs villes en mémoire avec leurs coordonnées. On a la dernière commande que le capitaine a entrée et on peut donc déterminer quelle entrée est la bonne pour ensuite extraire l'endroit. On comprend que le deuxième paramètre donné (2) indique que la destination est donc le troisième élément du tableau de destinations présent en mémoire (Ocracoke Island).

Un autre moyen possible est de laisser l'autopilote rouler jusqu'à ce qu'il atteigne sa destination, mais ça peut être très long et le format de la réponse ne sera pas nécessairement le même que celui attendu. Note: Il est possible de croire que la destination est Port Royal puisque c'est ce que Ghidra affiche comme nom de variable étant donné que c'est la première chaîne de caractère qu'il voit, mais ce n'est pas la bonne réponse.

## Flag

`flag-Ocracoke_Island`