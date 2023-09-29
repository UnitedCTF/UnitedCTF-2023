# Carte océanique 3

**`Auteur.e`** [Jersey591](https://github.com/Linden-Brochu)

![Graph](graph.png)

![Message](message.png)

## Description (français)

En arrivant sur les lieux indiqués par la carte, vous trouvez une épave sans
survivant(e)s. Vous n'y trouvez qu'une indication, « PARTEZ IMMÉDIATEMENT ! »,
suivi d'une nouvelle carte et d'un mystérieux message. N'ayant peur de rien,
vous ordonnez à votre équipage de déployer la grande voile.

**Format du flag**: `flag-{base64(valeur-max-en-parcourant-le-graphe)}`

Supposons un graphe de deux nœuds, A et B, avec un lien « + » de A vers B.
A ayant une valeur de 10 et B ayant une 5, la valeur maximale serait 15.

*Le graphe est représenté sous format texte sous le fichier `nodes.txt`
avec le premier nœud dans le fichier étant le nœud d'entrée.
La première ligne indique le nombre de nœuds.*

**Toutes les opérations sont des opérations entières, donc pas de nombre
à virgule**

**Indice optionnel** Infini représente un overflow et `NaN` représente
une opération invalide telle une division par 0 (et ces valeurs sont plus
basses que le plus petit nombre entier).

## Description (english)

When on the place indicated by the map, you found a wreck with no survivors.
You only found an indication, "GET OUT NOW !", with a new map and a mysterious
message. Without fear, you order your crew to deploy the mainsail.

**Flag format**: `flag-{base64(max-value-while-traversing-the-graph)}`

Suppose a graph with two nodes, A and B, with a link "+" from A to B.
A has a value of 10 and B has a value of 5, the max value is 15.

*The graph is represented in text under the `nodes.txt` file with the first
node in the file being the entry node. The first line indicate the number of
nodes.*

**All operations give integer, so no floating point number**

**Optional hint** Infinity represent an overflow and `NaN` represent
an invalid arithmetic operation such as a division by 0 (and those value are
lower than the lowest of integer).

## Solution

Solution of the challenge can be found [here](solution/).
