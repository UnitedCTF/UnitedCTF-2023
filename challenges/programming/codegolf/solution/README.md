# Pacific-Golfing

<hr>

## 1. Parcours de dictionaries :

#### Output attendu : 
    Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche

#### Paramètre de test : `Array = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]`

#### Consigne : `Afficher les 7 premiers éléments d'une liste de chaine de caractères nommé "Array" sous forme d'une chaine de caractère en séparant chaque élément par un espace.`

#### Limite de caractère : `22`

#### Code montré : `(117 caractères)`
    print(Array[0] + " " + Array[1] + " " + Array[2] + " " + Array[3] + " " + Array[4] + " " + Array[5] + " " + Array[6])

#### Exemple de réponse : `(22 caractères)`
    print(*Array, sep=" ")

#### Flag : flag-dico-run-0193747315584

<hr>

## 2. Conditions : opérateurs ternaires
#### Output attendu :
    0 : Paire
    1 : Impaire
    2 : Paire
    3 : Impaire
    4 : Paire
    5 : Impaire
    6 : Paire
    7 : Impaire
    8 : Paire
    9 : Impaire

#### Paramètre de test : `Boucle de 0 à 9 "for i in range (10):"`

#### Consigne : `Afficher une chaine de caractère qui suit le format suivant : "x : Paire" ou "x : Impaire" dans laquel vous remplacerez x par le numéro passé en paramettre nommé "N"`

#### Limite de caractères : `42`

#### Code montré : `(70 caractères)`
    print(N, end=" : ")
    if N%2 == 0: 
     print("Paire")
    else:
      print("Impaire")

#### Exemple de réponse : `(42 caractères)`
    print(N,":","Paire"if N%2==0else"Impaire")

#### Flag : flag-condition-799614805872988

<hr>

## 3. Listes : liste de compréhension
#### Output attendu :
    0 2 4 6 8 10 12 14 16 18 20

#### Paramètre de test : `2`

#### Consigne : `Afficher dans une chaine de caractère la table de multiplication d'un nombre N donnée en parametre. La fonction doit affiche du multiplicateur 0 au multiplicateur 10 (inclusivement).`

#### Limite de caractères : `41`

#### Code montré : `(252 caractères)`
    Table = []
    Table.append(0 * N)
    Table.append(1 * N)
    Table.append(2 * N)
    Table.append(3 * N)
    Table.append(4 * N)
    Table.append(5 * N)
    Table.append(6 * N)
    Table.append(7 * N)
    Table.append(8 * N)
    Table.append(9 * N)
    Table.append(10 * N)
    print(" ".join(map(str, Table)))

#### Exemple de réponse : `(41 caractères)`
    print(*[i*N for i in range(11)], sep=" ")

#### Flag : flag-comprehension-list-97421365486525

<hr>

## 4. Parcours de tableau :
#### Output attendu :
    true
    true
    false
    true
    false

#### Paramètre de test : `Words = ["radar", "kayak", "voiture", "rotor", "table"]`

#### Consigne : `Afficher "true" ou "false" selon si le mot "Word" donné en paramètre est un palindrome.`

#### Limite de caractères : `43`

#### Code montré : `(139 caractères)`
    reversed_string = ""
    for i in range(len(Word)-1, -1, -1): 
    reversed_string += Word[i]
    print("true" if Word == reversed_string else "false")

#### Exemple de réponse : `(43 caractères)`
    print("true"if Word==Word[::-1]else"false")

#### Flag : flag-reverse-array-984233315633063

<hr>

## 5. Standard function
#### Output attendu :
    2
    1
    0

#### Paramètre de test : `ToWords = ["toto", "tomate", "romarin"]`

#### Consigne : `Afficher le nombre d'apparitions de la chaine de caractère "to" dans le mot "Word" passé en paramètre.`

#### Limite de caractères : `23`

#### Code montré : `(144 caractères)`
    count = 0
    i = 0
    while i < len(Word):
        if Word[i:i+len("to")] == "to":
            count += 1
            i += len("to")
        else:
            i += 1
    print(count)

#### Exemple de réponse : `(23 caractères)`
    print(Word.count("to"))

#### Flag : flag-func-standard-3348912236750

<hr>

## 6. Set : Retirer tout les éléments dupliqués d'une liste
#### Output
    a
    b
    c

#### Paramètre de test : `MultiArray = ["a", "a", "b", "c", "c"]`

#### Consigne : `Afficher tous les éléments du tableau "Array" une seule fois. Les éléments dupliqués ne doivent pas être réaffichés.`

#### Limite de caractères : `29`

#### Code montré : `(118 caractères)`
    result = []
    for element in MultiArray:
        if element not in result:
            result.append(element)
            print(element)

#### Exemple de réponse : `(29 caractères)`
    [*map(print,set(MultiArray))]


#### Flag : flag-set-unique-712980012765345
