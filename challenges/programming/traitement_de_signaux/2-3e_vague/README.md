# La 3e vague

**`Auteur.e`** [Granny](https://github.com/CloeD)

## Description (français)

Matelot !

C'est bien de savoir créer une vague, mais, sur les mers, les vagues sont en fait une combinaison de plusieurs vagues !

Ton prochain défi est de créer trois vagues et de les additionner. Les fréquences des deux premières sont les deux lettres
de l'alphabet favorites des pirates et met cette valeur à la colonne des dixièmes *(ex: A->0.1 et Z->0.26)*. La troisième vague te sera donnée par
le tableau de bord. Voici les paramètres qui te sont fournis : ``frequence d'echantillonnage (Hz); duree de la vague (s); 
frequence de la 3e vague (Hz)``. Renvoie-moi la valeur du 12e sommet de ta vague.

*Tu dois te connecter au serveur `123.456.789.012` au port `1337` avec *netcat* pour résoudre ce challenge.


## Description (english)

Sailor !

It's nice to know how to create a wave, but, on the sea, waves are actually a combination of multiple waves !

Your next challenge is to create three waves and to add them up. The signal frequency for the first two waves are pirates' two 
favorite letters of the alphabet. Put that value in the decimal column *(ex: A->0.1 and Z->0.26)*.  The third wave frequency 
will be given to you by the dashboard. Here's the parameters you will receive: ``signal rate (Hz); wave duration (s); 
3rd wave frequency (Hz)``. Give me the value of the 12th peak of your wave.

*You must connect to the server `123.456.789.012`, port `1337`, with *netcat* to solve this challenge.

## Outils / Tools

Python: scipy, numpy, matplotlib (visualiser notre onde)
Matlab: Signal Processing Toolbox

## Solution

Solution of the challenge can be found [here](solution/).
