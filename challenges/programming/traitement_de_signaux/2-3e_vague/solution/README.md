# La 3e vague

## Write-up

#### 1 - Créer les vagues.
Il est possible de reprendre le même code que le défi d'introduction et de le dupliquer 
trois fois pour nos trois signaux.

#### 2 - Additionner les vagues.
Pour combiner les vagues, il suffit de les additionner avec le fabuleux ``+`` !

#### 3 - Trouver le 12e pic de la vague.
Pour ce faire, le plus facile est d'utiliser la fonction suivante provenant de la librairie de scipy : ``signal.find_peaks()``.
Ensuite, il faut regarder le 12e élément retourné par la fonction puis utiliser ce chiffre comme index pour notre vague
combinée afin d'avoir la valeur en y de notre 12e sommet.

#### Code Python
```python
import math
import numpy as np

# parametres (en ordre d'apparition)
# fe - frequence d'echantillonnage
# tf - fin du signal (secondes)
# fr3 - frequence du signal#3 (Hz)

# 1. creer les signaux
# on suppose qu'on commence a t0 = 0
t = np.linspace(t0, tf, fe)

# fr1 = 0.3 (C -> sea)
# fr2 = 0.18 (R -> arrr)
x1 = np.sin(2 * np.pi * fr1 * t)
x2 = np.sin(2 * np.pi * fr2 * t)
x3 = np.sin(2 * np.pi * fr3 * t)

# 2. combiner les signaux
s = x1 + x2 + x3

# 3. trouver les pics des signaux
peaks, _ = sig.find_peaks(s)

# 12e sommet = 11e element de la liste comme on commence a zero
solution = s[peaks[12 - 1]]
```

## Flag

`flag-~Up~&~D0wn~B01$~p4$~L4~t4$$3~`
