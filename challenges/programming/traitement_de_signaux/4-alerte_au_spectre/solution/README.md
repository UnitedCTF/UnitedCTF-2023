# Alerte au spectre !

## Write-up

#### 1 - Récupérer le signal
On télécharge le fichier. Pour l'ouvrir, il est possible d'utiliser `wavfile.read()` de `scipy.io`.

#### 2 - Calculer le spectre / la transformée de Fourier
Le titre du défi parle de *spectre* et on mentionne que l'on ne sera pas *transformé*. Une recherche Google avec les 
mots `traitement de signaux spectre` et un peu de recherche permet de déterminer que l'on parle de spectre ou de la 
transformée de Fourier.

La documentation de numpy pour les transformées de Fourier nous redirige vers la fonction dans scipy. La [documentation](https://docs.scipy.org/doc/scipy/tutorial/fft.html) 
nous explique comment utiliser les fonctions:

>The example plots the FFT of the sum of two sines.
```python
from scipy.fft import fft, fftfreq
import numpy as np
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
```

Il suffit de reprendre ces lignes et de remplacer les variables par les valeurs que nous avons.

#### 3 - Trouver les valeurs manquantes au flag
Après avoir obtenu notre spectre, il faut prendre les valeurs en x de chaque pic. Ces valeurs représentent la valeur 
décimale des lettres, donc, leur valeur dans le tableau ASCII. Ces lettres sont aussi dans le même ordre que dans le 
tableau, ce qui nous permet de remplir les trous des paroles du spectre et d'avoir le drapeau.

#### Code Python
```python
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
from scipy.io import wavfile
import numpy as np

# 1. récupérer le signal
fr_signal, sound = wavfile.read('oOooOOo.wav')

# 2. calcul du spectre / transformee de fourier
# voir https://docs.scipy.org/doc/scipy/tutorial/fft.html#d-discrete-fourier-transforms
fourier_spectre = 2.0 / fr_signal * np.abs(fft(sound)[0: fr_signal // 2])
freq = fftfreq(fr_signal)[: fr_signal // 2] * fr_signal

# 3. trouver les pics
peaks, _ = find_peaks(fourier_spectre[: 125])
# afficher les valeurs des pics
print(peaks) 
```

## Flag

`flag-FOuR1ermEH4nt3`
