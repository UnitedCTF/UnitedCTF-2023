# L'algorithme de Roland Sans-Argent

## Challenge 0

### Français

#### Description

Dans le cadre de la [célèbre compétition de *Scientifique de l'année de la Société Royale de Londres*](https://www.youtube.com/watch?v=XZwVmCBDcWg), ton rival, le capitaine Roland Sans-Argent, a « inventé » un « nouvel » algorithme de chiffrement.

Alors que tous sont ébahis par cette découverte (certains en perdent même connaissance), tu sais que ses implémentations sont truffées de failles.

La première place de la compétition de *Scientifique de l'année de la Société Royale de Londres* est à notre portée!

**Sauras-tu déjouer les implémentations du capitaine Roland Sans-Argent?**

Cette suite de défis porte sur l'[algorithme de chiffrement RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA), utilisé entre autres, pour sécuriser HTTPS, SSH, PGP et OpenVPN.

Les outils recommandés sont Python et la librairie de cryptographie [pycryptodome](https://pypi.org/project/pycryptodome/).

### English

#### Description

As part of the [famous *Scientist of the Year competition of the Royal Society of London*](https://www.youtube.com/watch?v=XZwVmCBDcWg), your rival, captain Roland Sans-Argent, has "invented" a "new" encryption algorithm.

While everyone is amazed by this discovery (some even faint), you know that his implementations are riddled with flaws.

The first place in the *Scientist of the Year competition of the Royal Society of London* is within our grasp!

**Will you be able to thwart the implementations of captain Roland Sans-Argent?**

This series of challenges focuses on the [RSA encryption algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), used among other things, to secure HTTPS, SSH, PGP, and OpenVPN.

The recommended tools are Python and the cryptography library [pycryptodome](https://pypi.org/project/pycryptodome/).

### Solution

[Script](solution/challenge0-solution.py)

[Explications](solution/README.md#challenge-0)

## Challenge 1

### Français

#### Description

Mais quelle erreur de débutant ! 

Avec toute l'arrogance qui vous es propre, vous démontrez à l'assemblée que le capitaine n'y connais rien à rien, tellement qu'il a fuité `p` dans la sortie de son programme ! Haha !

Le capitaine Roland Sans-Argent ne se fera pas avoir aussi facilement la prochaine fois.

Le capitaine a retiré `p` de la sortie de son programme et vous met au défi de briser sa nouvelle implémentation.

Bonne chance!

### English

#### Description

Such a rookie mistake!

With all the arrogance that is so characteristic of you, you show the assembly that the captain knows nothing at all, so much so that he leaked `p` in the output of his program! Haha!

Captain Roland Sans-Argent won't be caught off guard so easily next time.

The captain has removed `p` from the output of his program and challenges you to break his new implementation.

Good luck!

### Solution

[Script](solution/challenge1-solution.py)

[Explications](solution/README.md#challenge-1)

## Challenge 2

### Français

#### Description

Encore une autre victoire, et une défaite cuisante pour le capitaine!

Pauvre de lui qui ne sait pas compter jusqu'à plus de 10, il croyait que 64 était un nombre bien assez grand pour la longueur de `p` et `q`!

Mais le capitaine ne se laisse pas abattre aussi facilement! Il a augmenté la longueur de `p` et `q` à 512 bits! Par Neptune, il a même implémenté un `e` différent pour chaque encryption et tellement grand qu'il ne sait même pas comment ce nombre se nomme!

Bonne chance moussaillon. Tu en auras besoin!

### English

#### Description

Another victory, and a crushing defeat for the captain!

Poor him, who can't count past 10, thought that 64 was a large enough number for the length of `p` and `q`!

But the captain won't be brought down so easily! He has increased the length of `p` and `q` to 512 bits! By Neptune, he's even implemented a different `e` for each encryption, and it's so large he doesn't even know what to call it!

Good luck, sailor. You'll need it!

### Solution

[Script](solution/challenge2-solution.py)

[Explications](solution/README.md#challenge-2)

## Challenge 3

### Français

#### Description

Non seulement l'audience commence bien à mettre en question la « découverte » du capitaine, mais il semblerait que vos recherches sur le bris de RSA commencent à attirer l'attention de la foule!

On dirait bien que vous vous approchez du titre de *Scientifique de l'année de la Société Royale de Londres*!!

Mais le capitaine est convaincu qu'il arrivera à implémenter son algorythme de façon sécuritaire.

C'est assez changer le `e` à chaque encryption! À partir de maintenant, ce sera un seul `e` et des `p` et `q` différents pour chaque encryption!

En changeant les clés à chaque encryption, l'algorithmes est bien plus sécuritaire, non?

### English

#### Description

Not only is the audience starting to question the captain's so-called "discovery", but it seems your research on breaking RSA is starting to draw the crowd's attention!

It looks like you're closing in on the title of *Scientist of the Year of the Royal Society of London*!!

But the captain is convinced he'll be able to implement his algorithm securely.

Enough of changing the `e` with every encryption! From now on, it will be one consistent `e` and different `p` and `q` for each encryption!

By changing the keys with every encryption, the algorithm is much more secure, right?

### Solution

[Script](solution/challenge3-solution.py)

[Explications](solution/README.md#challenge-3)

## Challenge 4

### Français

#### Description

« C'est assez ! » s'écrie le capitaine Roland Sans-Argent.

La salle a perdu tout respect pour le capitaine, qui a maintenant perdu toute crédibilité. Déjà, les scientifiques les plus éminents de la salle se sont mis à rire de lui, et commencent à exiger que vous soyez gagnant de la compétition!

Le capitaine en est à sa dernière tentative.

Il a RTFM et a implémenté RSA de façon sécuritaire. Il a utilisé un `e` assez grand, un `p` et un `q` assez grand, il ne les change pas entre les encryptions.

**Malheureusement, parfois le sort ne nous est simplement pas favorable. Il existe des conditions spéciales où, même lorsque RSA est bien implémenté, les nombres générés alléatoirement ne sont pas sécuritaires. Dans ce cas particulier, vous avez l'implémentation, mais `p`, `q` et `e` ont été choisis de telle sorte qu'ils sont tout de même vulnérables.**

Le titre de *Scientifique de l'année de la Société Royale de Londres* est à ta portée !

Bonne chance !

### English

#### Description

"That's enough!" exclaims captain Roland Sans-Argent.

The room has lost all respect for the captain, who has now lost all credibility. Already, the most eminent scientists in the room have started laughing at him and are demanding that you be declared the winner of the competition!

The captain is on his last attempt.

He has RTFM and implemented RSA securely. He used a sufficiently large `e`, a large enough `p` and `q`, and he doesn't change them between encryptions.

**Unfortunately, sometimes luck just isn't on our side. There are special conditions where, even when RSA is properly implemented, the randomly generated numbers are not secure. In this particular case, you have the implementation, but `p`, `q`, and `e` have been chosen in such a way that they are still vulnerable.**

The title of *Scientist of the Year of the Royal Society of London* is within your grasp!

Good luck!

### Solution

[Script](solution/challenge4-solution.py)

[Explications](solution/README.md#challenge-4)