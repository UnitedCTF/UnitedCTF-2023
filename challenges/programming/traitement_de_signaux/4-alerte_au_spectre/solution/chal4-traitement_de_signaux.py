import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

from scipy.signal import find_peaks


def chal4_creation_signal():
    # encrypter les valeurs decimales du drapeau dans la frequence d'echantillonage (Hz)
    fe = 1000000    # une plus grande precision amene a un meilleur spectre (valeurs a 1)
    liste_fe = [70, 48, 000, 82, 00, 51, 000, 77, 00, 00, 00, 110, 116, 00]
    #           F   O   u    R   1   e   r    m   E   H   4   n    t    3
    # debut du signal (secondes)
    t0 = 0
    # fin du signal (secondes)
    tf = 1

    s = np.zeros(fe)

    # creer une liste de fe points entre t0 et tf
    t = np.linspace(t0, tf, fe)
    for i in liste_fe:
        # creer le signal et l'additionner
        s += np.sin(2 * np.pi * i * t)

    # creer le graphique du signal (for fun)
    # plt.plot(t, s)
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.show()

    # creation du fichier
    wavfile.write("oOooOOo.wav", fe, s)


def ans_chal4_tds():
    # importer le fichier
    fr_signal, sound = wavfile.read('oOooOOo.wav')

    # calcul du spectre / transformee de fourier
    # voir https://docs.scipy.org/doc/scipy/tutorial/fft.html#d-discrete-fourier-transforms
    fourier_spectre = 2.0 / fr_signal * np.abs(fft(sound)[0: fr_signal // 2])
    freq = fftfreq(fr_signal)[: fr_signal // 2] * fr_signal

    # trouver les pics
    peaks, _ = find_peaks(fourier_spectre[: 125])
    # voir le spectre
    plt.plot(freq, fourier_spectre)
    # voir les pics sur le spectre
    plt.plot(peaks, fourier_spectre[peaks], "x")
    plt.xlim(40, 125)
    plt.show()


if __name__ == '__main__':
    chal4_creation_signal()
    ans_chal4_tds()
