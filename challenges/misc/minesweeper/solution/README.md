# Minesweeper

**`Author:`** [Otaphoque](https://github.com/otaphoque)

## Write-up

Pour le premier flag, il faut juste déminer toutes les cells non-mines, c'est-à-dire:

```
A1 D1 E1 H1 I1 L1 O1 P1 Q1 T1 U1 V1 W1
B3 E3 F3 J3 K3 M3 P3 R3 T3 U3
A5 C5 D5 G5 H5 I5 K5 M5 N5 R5 S5 T5 W5
A7 D7 F7 H7 I7 L7 N7 P7 T7 U7
A9 B9 E9 F9 I9 J9 M9 O9 Q9 R9 S9 T9 U9 V9 
B11 C11 F11 H11 J11 K11 M11 N11 P11 V11 W11
C13 D13 G13 I13 L13 M13 N13 O13 Q13 S13 T13 U13 V13 W13
A15 D15 E15 H15 J15 L15 M15 O15 P15 Q15 T15 
```

On peut run la commande en une seule ligne:
`dig A1 D1 E1 H1 I1 L1 O1 P1 Q1 T1 U1 V1 W1 B3 E3 F3 J3 K3 M3 P3 R3 T3 U3 A5 C5 D5 G5 H5 I5 K5 M5 N5 R5 S5 T5 W5 A7 D7 F7 H7 I7 L7 N7 P7 T7 U7 A9 B9 E9 F9 I9 J9 M9 O9 Q9 R9 S9 T9 U9 V9 B11 C11 F11 H11 J11 K11 M11 N11 P11 V11 W11 C13 D13 G13 I13 L13 M13 N13 O13 Q13 S13 T13 U13 V13 W13 A15 D15 E15 H15 J15 L15 M15 O15 P15 Q15 T15`

Le minesweeper est résolu, on a le premier flag:
`flag-701_7u_5415_0u_p053r_l35_p13d5`

Pour la deuxième partie, il faut déchiffrer le binaire (chaque mine est un "1", le reste est un "0" et il faut enlever les lignes de "0"):

```
01100110011011000110000 
10110011100101101010011
01001100010100111000110
01101010011010101110011
00110011001101010000001
10011010100100101111100
11001101011000010100000
01100110101001000110111 
```

On met ça dans cyberchef pour décoder le tout et ça donne:
`flag-M1N3SW33P3R_3XP3R7`


