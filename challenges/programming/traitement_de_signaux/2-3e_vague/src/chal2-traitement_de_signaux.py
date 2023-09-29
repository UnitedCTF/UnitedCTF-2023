import os
import signal as os_signal
from scipy import signal
import numpy as np
# import matplotlib.pyplot as plt
import random


def chal2_tds():
    # frequence d'echantillonnage (Hz)
    fe = random.randint(256, 720)

    # debut du signal (secondes)
    t0 = 0
    # fin du signal (secondes)
    tf = 60

    # creer une liste de fe points entre t0 et tf
    t = np.linspace(t0, tf, fe)

    # frequence du signal (Hz)
    fr1 = 0.3   # C (sea)
    fr2 = 0.18  # R (arrr)
    fr3 = round(random.uniform(0.1, 0.9), 2)    # variation

    # parametres
    print(f'{fe}; {tf}; {fr3}')

    # creer les signaux
    x1 = np.sin(2 * np.pi * fr1 * t)
    x2 = np.sin(2 * np.pi * fr2 * t)
    x3 = np.sin(2 * np.pi * fr3 * t)

    # combiner les signaux
    s = x1 + x2 + x3

    # trouver les pics des signaux
    peaks, _ = signal.find_peaks(s)

    # creer le graphique (for fun)
    # plt.plot(t, s)
    # plt.plot(t[peaks], s[peaks], 'ro')
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.show()

    # 12e sommet = 11e element de la liste comme on commence a zero
    return s[peaks[12 - 1]]


def alarm_handler(signum, frame):
    print("The waves are too fast for your processing !")
    exit(0)

def flag_chal2_tds(ans):
    guess = input()
    if guess[:8] == str(ans)[:8]:
        print("flag-~Up~&~D0wn~B01$~p4$~L4~t4$$3~")
    else:
        print("Try again !")


if __name__ == '__main__':
    os_signal.signal(os_signal.SIGALRM, alarm_handler)
    os_signal.alarm(2) # 2 seconds
    ans = chal2_tds()
    flag_chal2_tds(ans)
