# treasure-map

Phrase Secrète : `CaptainCrunch`

## Binary Ninja :

1. Commencez par identifier le main avec la signature : treasure_map::main::....
2. L'analyse révèle qu'une simple inversion de bytes est utilisée comme méthode d'encodage.
3. Plus spécifiquement, on identifie l'instruction :
`hex::BytesToHexChars::new::hd6244798dc00bee1(&var_a0, "10.1234,-50.1234flag-Enter the s…", 0x10, "0123456789abcdef")`
qui indique que le drapeau (flag) est affiché sous le format : flag-hex(10.1234,-50.1234). Ici, "10.1234,-50.1234" est représenté par 0x10 dans la chaîne.

## Ghidra ou autre

Lorsque nous soumettons le code à Ghidra et demandons une analyse, ChatGPT peut fournir une réponse pertinente :

```
Validation: The transformed input is compared to a predefined value (0xc27696862e0e86c2, and other bytes), possibly representing the correct passphrase.
- ChatGPT
``` 

```
*local_78 = 0xc27696862e0e86c2;
*(undefined4 *)(local_78 + 1) = 0xc676ae4e;
*(undefined *)((long)local_78 + 0xc) = 0x16;
```

CaptainCrunch = c2860e2e869676c24eae76c6

Sinon, on peux suivre les blocs logique du code et trouver que représente le code secret. Pour le confirmer, on peut exécuter l'application. En essayant différentes entrées, on remarque que l'on peut récupérer le code original :

```
reverse/treasure-map [treasure-map●] » ./dist/treasure-map
Enter the secret passphrase:
C
Wrong passphrase, no treasure for ye!
Here's your encoded value: c2
reverse/treasure-map [treasure-map●] » ./dist/treasure-map
Enter the secret passphrase:
a
Wrong passphrase, no treasure for ye!
Here's your encoded value: 86
reverse/treasure-map [treasure-map●] » ./dist/treasure-map
Enter the secret passphrase:
a
Wrong passphrase, no treasure for ye!
Here's your encoded value: 86
```
Cela suggère que si on entre la même valeur, le retour sera identique. On pourrait donc tenter de bruteforcer, soit manuellement, soit avec un script Python, pour déchiffrer le code secret en entier.

# Flag

`flag-31302e313233342c2d35302e31323334` (hex de "10.1234,-50.1234")
