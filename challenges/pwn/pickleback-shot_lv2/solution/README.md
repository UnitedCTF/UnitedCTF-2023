# Pickleback shot Lv2

## Write-up (français)

Dans ce défi, on souhaite utiliser le module `pickle` pour envoyer au serveur une certaine séquence d mouvements nous permettant d'ouvrir le cadena et ainsi avoir le whisky pour notre drink. 

Pour ce faire, il faut écrire un programme imprimant la séquence de mouvement à faire pour ouvrir le cadena.

```py
import pickle
import base64
from typing import Tuple

class Movement:
    def __init__(self, move: str):
        self.__move = move

    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__move,))
    
    def move(self) -> str:
        return self.__move

class Movements:
    def __init__(self, movements: list):
        self.__movements = movements

    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__movements,))
        
    def movements(self) -> list:
        return self.__movements

# sequence to do: 
# a -> k
# move right
# b -> r
# move right
# b -> a
# move right
# a -> k
# move right
# T -> e
# move right
# n -> n

movements =   [Movement('UP')]   * (ord('k') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('r') - ord('b')) + [Movement('RIGHT')] \
            + [Movement('DOWN')] * (ord('b') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('k') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('e') - ord('T')) + [Movement('RIGHT')] \
            + [Movement('STOP')]

if __name__ == '__main__':
    pickled = pickle.dumps(Movements(movements))
    print(base64.urlsafe_b64encode(pickled))
```

La chaîne de caractère en base64 résultante est la suivante: 
```
gASV_AAAAAAAAACMCF9fbWFpbl9flIwJTW92ZW1lbnRzlJOUXZQoaACMCE1vdmVtZW50lJOUjAJVUJSFlFKUaAhoCGgIaAhoCGgIaAhoCGgIaAWMBVJJR0hUlIWUUpRoBWgGhZRSlGgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgFaAmFlFKUaAWMBERPV06UhZRSlGgFaAmFlFKUaAVoBoWUUpRoFmgWaBZoFmgWaBZoFmgWaBZoBWgJhZRSlGgFaAaFlFKUaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoBWgJhZRSlGgFjARTVE9QlIWUUpRlhZRSlC4=
```

Lorsque l'on envoie ces données au serveur, on reçoit le flag.
```
curl -X GET -d "data=gASV_AAAAAAAAACMCF9fbWFpbl9flIwJTW92ZW1lbnRzlJOUXZQoaACMCE1vdmVtZW50lJOUjAJVUJSFlFKUaAhoCGgIaAhoCGgIaAhoCGgIaAWMBVJJR0hUlIWUUpRoBWgGhZRSlGgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgFaAmFlFKUaAWMBERPV06UhZRSlGgFaAmFlFKUaAVoBoWUUpRoFmgWaBZoFmgWaBZoFmgWaBZoBWgJhZRSlGgFaAaFlFKUaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoBWgJhZRSlGgFjARTVE9QlIWUUpRlhZRSlC4=" http://<IP>:<PORT>/get_whisky

flag-L0rdKr@k3N
```


## Write-up (english)

In this challenge, we aim to use the `pickle` module to send a specific sequence of movements to the server, allowing us to unlock the padlock and thus access the whiskey for our drink.

To achieve this, it is necessary to write a program that prints the sequence of movements required to unlock the padlock.

```py
import pickle
import base64
from typing import Tuple

class Movement:
    def __init__(self, move: str):
        self.__move = move

    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__move,))
    
    def move(self) -> str:
        return self.__move

class Movements:
    def __init__(self, movements: list):
        self.__movements = movements

    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__movements,))
        
    def movements(self) -> list:
        return self.__movements

# sequence to do: 
# a -> k
# move right
# b -> r
# move right
# b -> a
# move right
# a -> k
# move right
# T -> e
# move right
# n -> n

movements =   [Movement('UP')]   * (ord('k') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('r') - ord('b')) + [Movement('RIGHT')] \
            + [Movement('DOWN')] * (ord('b') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('k') - ord('a')) + [Movement('RIGHT')] \
            + [Movement('UP')]   * (ord('e') - ord('T')) + [Movement('RIGHT')] \
            + [Movement('STOP')]

if __name__ == '__main__':
    pickled = pickle.dumps(Movements(movements))
    print(base64.urlsafe_b64encode(pickled))
```

The resulting base64-encoded string is as follows:
```
gASV_AAAAAAAAACMCF9fbWFpbl9flIwJTW92ZW1lbnRzlJOUXZQoaACMCE1vdmVtZW50lJOUjAJVUJSFlFKUaAhoCGgIaAhoCGgIaAhoCGgIaAWMBVJJR0hUlIWUUpRoBWgGhZRSlGgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgFaAmFlFKUaAWMBERPV06UhZRSlGgFaAmFlFKUaAVoBoWUUpRoFmgWaBZoFmgWaBZoFmgWaBZoBWgJhZRSlGgFaAaFlFKUaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoBWgJhZRSlGgFjARTVE9QlIWUUpRlhZRSlC4=
```

When sending this data to the server, we receive the flag.
```
curl -X GET -d "data=gASV_AAAAAAAAACMCF9fbWFpbl9flIwJTW92ZW1lbnRzlJOUXZQoaACMCE1vdmVtZW50lJOUjAJVUJSFlFKUaAhoCGgIaAhoCGgIaAhoCGgIaAWMBVJJR0hUlIWUUpRoBWgGhZRSlGgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgNaA1oDWgFaAmFlFKUaAWMBERPV06UhZRSlGgFaAmFlFKUaAVoBoWUUpRoFmgWaBZoFmgWaBZoFmgWaBZoBWgJhZRSlGgFaAaFlFKUaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoGmgaaBpoBWgJhZRSlGgFjARTVE9QlIWUUpRlhZRSlC4=" http://<IP>:<PORT>/get_whisky

flag-L0rdKr@k3N
```

## Flag

```
flag-L0rdKr@k3N
```
