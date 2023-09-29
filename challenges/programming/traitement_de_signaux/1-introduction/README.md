# Ma première vague

**`Auteur.e`** [Granny](https://github.com/CloeD)

## Description (français)

Matelot !

Approche, je vais t'apprendre à lire les vagues grâce à Fred le Python. 
Tu peux aussi aller dans le laboratoire de mathématiques (Matlab) pour analyser ça si
tu es du type scientifique. 

Déjà, pour lire les vagues, il faut savoir comment en créer une ! Il est possible de
représenter une vague par une **onde sinusoïdale**.

Une onde sinusoïdale est une onde périodique, c'est-à-dire une onde qui effectue le même mouvement sur une période de
temps. Ainsi, il est possible de représenter une onde avec une liste de points dont la
valeur change à intervalle régulier. Cet interval se nomme la **fréquence d'échantillonnage**.
Par exemple, une fréquence d'échantillonnage de 10 Hz sur une période de temps d'une seconde (1s)
nous donnera 10 points. 

Ensuite, un autre composant clé des ondes est la **fréquence du signal**, exprimée en Hertz (Hz). C'est le nombre de 
fois que le cycle de l'onde se répète dans la période donnée. Par exemple, une fréquence de 4 Hz voudrait dire qu'une
onde sinusoïdale se répètera quatre fois, donc qu'il y aura quatre pics positifs et quatre pics négatifs.

Enfin, la trigonométrie t'aidera dans la création de vagues. Tu peux voir une onde sinusoïdale comme la **valeur en y** d'un
cercle trigonométrique. Cette valeur, c'est la hauteur de ta vague. C'est donc dire que ta vague prend la valeur `2 * pi * t`
si sa fréquence équivaut à 1 Hz.

Il faut que tu demandes au tableau de bord tes paramètres puis que tu les renvoies en deux seconde pour obtenir le drapeau.
Le format que tu recevras est le suivant : `fréquence d'échantilonnage (Hz); durée de la vague (s); fréquence (Hz); temps recherché (s)`.
Tu devras renvoyer la *hauteur* de ta vague au temps recherché. *Utilise `math.floor()` pour arrondir ton index.*

*Tu dois te connecter au serveur `123.456.789.012` au port `1337` avec *netcat* pour résoudre ce challenge.

## Description (english)

Sailor !

Come closer, I'll learn you how to read the waves with Python Fred. You can also go to the math lab (Matlab) to analyse 
the waves if you're more of an analytical type.

If you want to read the waves, you'll need to know how to create one first ! You can represent a wave with a sinusoidal wave.

A sinusoidal wave is a period wave, meaning a wave which repeats itself over a certain period of time. Knowing that, you
 can represent a wave with a list of points whose value change at regular interval. That interval is named the **sample rate**.
For example, a sample rate of 10 Hz on a acquisition period of 1 s gives us 10 points to work with.

Furthermore, another key component to signal processing is the **signals' frequency**, also in Hertz (Hz). It is how many 
time the waves cycle repeats itself in the given period. For example, a frequency of 4 Hz would mean that the sinusoidal 
wave repeats itself four times, thus generating four positive and four negative peaks.

Lastly, you'll need to remember your trigonometric circle to create your wave. Try to see the sinusoidal wave like the **y
value** in the trigonometric circle. The y gives you the height of the wave. In other terms, your wave takes the value 
`2 * pi * t` if its frequency is 1 Hz.

You'll need to ask your parameters to the dashboard and send back your result in two second to get your flag. Parameters 
format goes like this: `sampling rate (Hz); wave duration (s); frequency (Hz); searched time (s)`. You will need to send
back the *height* of your wave at the searched time. *Use `math.floor()` for your index value.*

*You must connect to the server `123.456.789.012`, port `1337`, with *netcat* to solve this challenge.

## Outils / Tools

Python: math, numpy, matplotlib (visualiser notre onde)
Matlab: Signal Processing Toolbox

## Solution

Solution of the challenge can be found [here](solution/).
