# Captain Octavius

## Write-up (français)

Le nom du capitanie (`Octavius`) pouvait nous donner un indice sur ce que nous devions faire. Octavius ici fait référence à Gaius Julius **Caesar** Octavianus. Il fallait donc déchiffrer le texte qui a passé sur un chiffrement par césar. 

Dans le texte il est dit aussi qu'à l'aide de notre **cinquième clé** on parcours à carte de gauche à droite. Le symbole à gauche est `#` et à droite `|`. Nous avons donc toute les informations en mains: 

```
alphabet: "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|"
clé: 5
```
ℹ️ l'alphabet est constitué des caractères ASCII entre `#` et `|` inclusivement

Après avoir inversé le message que nous avions au début nous arrivons avec ceci:

```py
# exemple de code pour reverse
def caesar_decrypt(encrypted_message: str, key: int, alphabet: str) -> str:
    decrypted_message = ""
    for char in encrypted_message:
        if char in alphabet:
            idx = (alphabet.index(char) - key) % len(alphabet)
            decrypted_char = alphabet[idx]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

alphabet = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|"
message = "M8qq5 ymEwJ1 $5zsl xE6q5w3 Ns q6kJ1 s5y J{Jw$ym6sl 6x gJEzy6kzq3 YEpJ ymJ sErJ 5k r$ g5Ey1 ymJ HmEwq5yyJ [5lzJ R8w$1 k5w 8#EruqJ3 6y,x h8wyE6sq$ qEwlJ1 gzy zLq^3 YmJ KqEl 6x ymJ sErJ 5k ymJ g5Ey3 -qt\8wdhEXj + Fqumfg8y6h 6jyyJw + |6ym5zY xuEh8."
key = 5

print(caesar_decrypt(message, key, alphabet))
```

message d'origine:
```
H3ll0 th@rE, y0ung s@1l0r. In l1fE, n0t EvEryth1ng 1s bE@ut1ful. T@kE thE n@mE 0f my b0@t, thE Ch@rl0ttE V0guE M3ry, f0r 3x@mplE. 1t's c3rt@1nly l@rgE, but uGlY. ThE Fl@g 1s thE n@mE 0f thE b0@t. (loW3r_c@Se & Alphab3t1c 1ettEr & w1th0uT sp@c3)
```

En suivant les instruction du message nous arrions au flag `thecharlottevoguemery`

## Write-up (english)

ChatGPT

The name of the captaincy (Octavius) could give us a clue about what we had to do. Octavius here refers to Gaius Julius **Caesar** Octavianus. Therefore, we needed to decipher the text that underwent a Caesar cipher.

In the text, it is also mentioned that using our fifth key, we traverse the map from left to right. The symbol on the left is `#`, and on the right is `|`. So, we have all the information at hand:

```
alphabet: "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|"
key: 5
```
ℹ️ The alphabet consists of ASCII characters between `#` and `|` inclusively.

After reversing the original message, we end up with the following:

```py
# Example code for decryption
def caesar_decrypt(encrypted_message: str, key: int, alphabet: str) -> str:
    decrypted_message = ""
    for char in encrypted_message:
        if char in alphabet:
            idx = (alphabet.index(char) - key) % len(alphabet)
            decrypted_char = alphabet[idx]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

alphabet = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|"
message = "M8qq5 ymEwJ1 $5zsl xE6q5w3 Ns q6kJ1 s5y J{Jw$ym6sl 6x gJEzy6kzq3 YEpJ ymJ sErJ 5k r$ g5Ey1 ymJ HmEwq5yyJ [5lzJ R8w$1 k5w 8#EruqJ3 6y,x h8wyE6sq$ qEwlJ1 gzy zLq^3 YmJ KqEl 6x ymJ sErJ 5k ymJ g5Ey3 -qt\8wdhEXj + Fqumfg8y6h 6jyyJw + |6ym5zY xuEh8."
key = 5

print(caesar_decrypt(message, key, alphabet))
```

Original message:
```
H3ll0 th@rE, y0ung s@1l0r. In l1fE, n0t EvEryth1ng 1s bE@ut1ful. T@kE thE n@mE 0f my b0@t, thE Ch@rl0ttE V0guE M3ry, f0r 3x@mplE. 1t's c3rt@1nly l@rgE, but uGlY. ThE Fl@g 1s thE n@mE 0f thE b0@t. (loW3r_c@Se & Alphab3t1c 1ettEr & w1th0uT sp@c3)
```

Following the instructions in the message, we arrive at the flag thecharlottevoguemery

## Flag

`flag-thecharlottevoguemery`
