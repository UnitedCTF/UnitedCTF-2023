# Passe pas tout droit !

## Write-up

#### 1 - Récupérer le signal
On télécharge le fichier. Pour l'ouvrir, il est possible d'utiliser `wavfile.read()` de `scipy.io`.

Ensuite, on mentionne bâbord. Parfois, les fichiers de sons contiennent deux signaux: l'un pour le stéréo de gauche puis
l'un pour le stéréo de droite. Ainsi, on sélectionne le premier stéréo avec `sound = sound[:, 0]`.

Les deux premières valeurs transmises par le serveur déterminent le segment de 2 000 points du signal à utiliser.

#### 2 - Créer le filtre passe-bande
Dans l'énoncé, on mentionne qu'*on ne sait pas combien de pirates iront* chercher le trésor. On observe aussi que le serveur
envoie deux autres valeurs après les valeurs d'intervalle pour le signal. De plus, le titre parle de *passe*. Ainsi, on peut déduire que ce sont les fréquences à 
utiliser pour faire notre passe-bande. Enfin, on parle de vérifier le chemin vingt (20) fois.

> Un passe-bande est un filtre qui laisse passer une intervalle de fréquence, 
contrairement à un filtre passe-bas qui laisse passer les basses fréquences et qui supprime les hautes ou un filtre 
passe-haut qui fait l'inverse.

Il y a une fonction dans scipy.signal qui permet d'appliquer le filtre:
```
sos = signal.butter(20, (min_pirates, max_pirates), 'bandpass', fs=fr_signal, output='sos')
filtered_signal = signal.sosfilt(sos, sound)
```

#### 3 - Trouver le Xe tournant vers la droite
Ici, on parle de sommets locaux. Ainsi, on réutilise la même fonction qu'auparavant pour trouver notre pic local puis 
on transmet la valeur au serveur (Karm).

#### Code Python
```python
from scipy import signal
from scipy.io import wavfile

# parametres (en ordre d'apparition)
# random_start - debut signal (secondes)
# random_end - fin du signal (secondes)
# min_pirates - valeur min du passe-bande
# max_pirates - valeur max du passe-bande
# random_peak - pic à trouver

# 1. récupérer le signal
fr_signal, sound = wavfile.read('chemin.wav')

# analyser que le premier stereo (stereo babord / de gauche)
sound = sound[:, 0]

# analyser qu'un certain segment du signal
sound = sound[random_start: random_end]

# 2. créer le filtre passe-bande
sos = signal.butter(20, (min_pirates, max_pirates), 'bandpass', fs=fr_signal, output='sos')
filtered_signal = signal.sosfilt(sos, sound)

# 3. trouver le Xe tournant vers la droite
peaks, _ = signal.find_peaks(filtered_signal)
solution = filtered_signal[peaks[random_peak - 1]]
```

## Flag

`flag-Y0uSh@llN0tP4$$!...0k,0n1y3xc3pt10nF0rY0u`
