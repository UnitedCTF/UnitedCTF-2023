# Introduction au Reverse 1 (Les bases)

**`Erreur-404`**

## Description (français)

Aye moussaillon! J'ai entendu que tu veux apprendre la rétro-ingénierie? Viens avec moi, je vais te montrer.
On discerne généralement l'analyse statique de l'analyse dynamique en rétro-ingénierie. 
Le premier consiste à analyser le programme et étudier son fonctionnement sans l'exécuter alors que le second exécute le programme dans un débuggeur et étudie le comportement du code alors qu'il s'exécute.

Les outils `strings` (disponible dans tout environnement Linux), [Ghidra](https://ghidra-sre.org) (analyse statique) et `gdb` (analyse dynamique) sont alors très pratiques. Ce défi contient trois flags partiels, soit un pour chaque outil. Lorsque tu les as tous trouvés, concatènes les afin de former le flag final. Exemple: flag-abc, flag-def et flag-ghi donnerait flag-abcdefghi

#### Ghidra

Ghidra est un outil d'analyse de programme compilé. Il permet de désassembler le programme pour lire le code assembleur correspondant et offre aussi une fonctionnalité de décompilation qui permet de lire le pseudo-code C qui pourrait correspondre au code source du programme.

Lorsqu'on utilise ghidra, il est d'abord nécessaire de créer un projet ("non-partagé" convient), puis on peut démarrer l'outil CodeBrowser. Il suffit ensuite d'importer le fichier qu'on souhaite analyser avec la touche "i" (ou File > Import File).

Pour plus d'informations: https://www.varonis.com/blog/how-to-use-ghidra

#### GDB

`gdb` est un débuggeur en ligne de commande qui permet de réaliser de l'analyse dynamique sous Linux. L'extension [GEF](https://github.com/hugsy/gef) facilite son utilisation et est recommandée.
Voici une liste de commandes utiles:
- `start` : Démarrer le débuggage
- `b` : Ajouter un breakpoint
- `c` : Continuer l'exécution
- `ni` : Prochaine instruction machine (Step over)
- `si` : Prochaine instruction machine (Step into)
- `telescope <expression>` : Voir se qui se trouve en mémoire à l'expression donnée. Exemple: `telescope $rbp-0x70`

Pour plus d'informations: https://www.geeksforgeeks.org/gdb-step-by-step-introduction/

Note: Le fichier est compilé pour être executé sous un environnement Linux

## Description (english)

Ahoy there, young sailor! I heard you want to learn about reverse engineering? Come with me, and I'll show you.

In reverse engineering, there are generally two types of analysis: static analysis and dynamic analysis. The former involves analyzing the program and studying its operation without executing it, while the latter runs the program in a debugger and studies the behavior of the code as it executes.

The tools `strings` (available in every Linux environment), [Ghidra](https://ghidra-sre.org) (for static analysis), and `gdb` (for dynamic analysis) are quite handy in this regard. This challenge contains three partial flags, one for each tool. Once you find them all, concatenate them to form the final flag. For example, flag-abc, flag-def, and flag-ghi would become flag-abcdefghi.

#### Ghidra

Ghidra is a tool for analyzing compiled programs. It allows you to disassemble the program to read the corresponding assembly code and also provides a decompilation feature that allows you to read the C-like pseudo-code that could correspond to the program's source code.

When using Ghidra, you first need to create a project ("non-shared" should do), and then you can start the CodeBrowser tool. After that, simply import the file you want to analyze using the "i" key (or File > Import File).

For more informations: https://www.varonis.com/blog/how-to-use-ghidra

#### GDB

`gdb` is a command-line debugger that allows you to perform dynamic analysis under Linux. The [GEF](https://github.com/hugsy/gef) extension makes its usage more accessible and is recommended. Here's a list of useful commands:
- `start`: Start debugging
- `b`: Add a breakpoint
- `c`: Continue execution
- `ni`: Next instruction (Step over)
- `si`: Next instruction (Step into)
- `telescope <expression>`: View the memory contents at the given expression. For example, telescope $rbp-0x70.

For more informations: https://www.geeksforgeeks.org/gdb-step-by-step-introduction/

Note: The file is compiled to be executed under a Linux environment

## Fichiers

- `bases`

## Solution

La solution du défi peut être trouvée [ici](solution/).
