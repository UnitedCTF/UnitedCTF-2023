# Lecture des vagues | Introduction au traitement de signaux

## Write-up
#### 1 - Créer notre liste de points selon notre fréquence d'échantillonnage.
Pour ce faire, il y a la fonction `numpy.linspace(t0, tf, fe)` qui permet de créer notre liste facilement.
Où t0, tf et fe sont respectivement le temps de début du signal (0 s), le temps de fin du signal (1 s) et la
fréquence d'échantillonnage du signal (480 Hz). Le retour de la fonction est sauvegardé dans une variable `t`.

#### 2 - Créer le signal.
Dans le défi, on parle d'onde sinusoïdale. C'est donc `numpy.sin()` qu'il faut utiliser. On donne aussi la 
formule à insérer dans cette fonction, soit `2 * pi * t`. Notre fréquence étant de 2 Hz,
nous obtenons `numpy.sin(2 * numpy.pi * fr * t)` que nous sauvegardons dans une variable `x`.

#### 3 - Trouver la hauteur de la vague.
Pour cette partie, il faut aller chercher la définition d'un Hertz et de son unité. Un Hertz, c'est aussi 1 / 1 seconde.
Ainsi, nous avons `Hz = 1 / s`. C'est le nombre de périodes par secondes.

Ici, nous avons 480 Hz comme fréquence 
d'échantillonnage et 2 Hz pour la fréquence du signal. Comme nous voulons savoir la valeur du signal à un instant précis,
nous devons utiliser la fréquence d'échantillonnage pour retrouver le point.

Donc, nous avons `480 Hz = 1 / ? s`. Le plus simple ici est de jouer avec les unités pour les annuler et obtenir notre index
qui équivaut à notre point à 0.7355 secondes. Ainsi: 
```
index = 0.7355 (secondes) * 480 (1/secondes)
index = 0.7355 * 480 
index = 353.04 
index ~ 353
```

En reprenant notre variable `x` qui représente le signal, nous allons chercher la hauteur de la vague à 0.7355 secondes 
avec notre index : `x[353] = 0.1632324975744533`.

#### Code Python
``` python
import math
import numpy as np

# parametres (en ordre d'apparition)
# fe - frequence d'echantillonnage
# tf - fin du signal (secondes)
# fr - frequence du signal (Hz)
# tr - temps recherche

# 1. creer une liste de fe points entre t0 et tf
# on suppose qu'on commence a t0 = 0
t = np.linspace(t0, tf, fe)

# 2. creer le signal
x1 = np.sin(2 * np.pi * fr * t)

# 3. trouver la hauteur
solution = x1[math.floor(fe * tr)]
```

## Flag

`flag-Cr3@t3y0uROwnWa@a@ave~!`
