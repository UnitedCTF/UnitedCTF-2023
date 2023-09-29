import random
import numpy as np
# import matplotlib.pyplot as plt
import math
import signal
import os


def chal1_tds():
    # frequence d'echantillonnage (Hz)
    fe = random.randint(256, 720)

    # debut du signal (secondes)
    t0 = 0
    # fin du signal (secondes)
    tf = 1

    # frequence du signal (Hz) - le nombre de fois que le sin se repete
    fr = random.randint(2, 16)

    # temps recherche
    tr = round(random.uniform(t0, tf), 4) # chiffre entre 0 et 1, arrondi a 4 decimales

    # parametres
    print(f'{fe}; {tf}; {fr}; {tr}')

    # creer une liste de fe points entre t0 et tf
    t = np.linspace(t0, tf, fe)

    # creer le signal
    x1 = np.sin(2 * np.pi * fr * t)

    # creer le graphique (for fun)
    # plt.plot(t, x1)
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.show()

    # trouver la hauteur de la vague
    #    la frequence d'echantillonnage est equivalente a fe = 1 / T (s)
    #    si tr = 0.7355 secondes et fe = 480
    #    on veut avoir l'index qui equivaut a 0.7355 secondes
    #    comme Hz = s^-1, on peut multiplier 0.7355 secondes a la frequence d'echantillonnage
    #    ainsi: 0.7355 * 480 = 353.04 ~ 353
    return x1[math.floor(fe * tr)]


def flag_intro_tds(ans):
    guess = input()
    if guess[:8] == str(ans)[:8]:
        print("flag-Cr3@t3y0uROwnWa@a@ave~!")
    else:
        print("Try again !")

def alarm_handler(signum, frame):
    print("The waves are too fast for your processing !")
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(2) # 2 seconds
    ans = chal1_tds()
    flag_intro_tds(ans)
