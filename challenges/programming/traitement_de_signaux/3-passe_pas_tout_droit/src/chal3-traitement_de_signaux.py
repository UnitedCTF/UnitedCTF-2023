import os
import signal as os_signal
from scipy import signal
from scipy.io import wavfile
# import matplotlib.pyplot as plt
import random


def chal3_tds():
    # importer le fichier
    fr_signal, sound = wavfile.read('chemin.wav')

    # analyser que le premier stereo (stereo babord / de gauche)
    sound = sound[:, 0]

    # analyser qu'un certain segment du signal
    random_start = random.randint(int(len(sound) / 20), int(len(sound) / 8))
    random_end = random_start + 2000
    sound = sound[random_start: random_end]
    # plt.plot(sound)
    # plt.title("Only sound")
    # plt.show()

    # valeurs pour le filtre passe-bande
    min_pirates = random.randint(10, 450)
    max_pirates = random.randint(500, 1000)

    sos = signal.butter(20, (min_pirates, max_pirates), 'bandpass', fs=fr_signal, output='sos')
    filtered_signal = signal.sosfilt(sos, sound)

    # trouver les pics
    peaks, _ = signal.find_peaks(filtered_signal)

    # creer le graphique (for fun)
    # plt.plot(filtered_signal)
    # plt.title("Filtered between " + str(min_pirates) + " and " + str(max_pirates))
    # plt.show()

    # valeur a trouver
    random_peak = random.randint(1, len(peaks))

    # imprimer les valeurs random pour le defi
    print(f'{random_start}; {random_end}; {min_pirates}; {max_pirates}; {random_peak}')

    return filtered_signal[peaks[random_peak - 1]]

def alarm_handler(signum, frame):
    print("The waves are too fast for your processing !")
    exit(0)

def flag_chal3_tds(ans):
    guess = input()
    if guess[:8] == str(ans)[:8]:
        print("flag-Y0uSh@llN0tP4$$!...0k,0n1y3xc3pt10nF0rY0u")
    else:
        print("Try again !")


if __name__ == '__main__':
    os_signal.signal(os_signal.SIGALRM, alarm_handler)
    os_signal.alarm(2) # 2 seconds
    ans = chal3_tds()
    flag_chal3_tds(ans)
