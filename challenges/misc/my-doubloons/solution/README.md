# Solutions

## Challenge 0

1. Utiliser `zip2john` pour permettre à `john` de cracker le mot de passe
2. Utiliser `john` pour brute force le mot de passe avec `rockyou.txt` (`moneypirate`)
3. Extraire le zip, le flag est dans `flag0.txt` (`flag-j0hnth3d3z1pp3r`)

## Challenge 1

1. Extraire tous les mots de passes contenant `pirate` de `rockyou.txt`
2. Utiliser `office2john` pour permettre à `john` de cracker le mot de passe
    - *Note: Ici, il faut trouver que le fichier est d'abord chiffré avec la fonctionnalité de chiffrement de Excel, à ne pas confondre avec « barrer » un fichier Excel. De plus, cette technique ne fonctionne que parce que le fichier a été chiffré avec Excel 2013.*
3. Utiliser `john` pour brute force le mot de passe avec la nouvelle wordlist (`i/love/pirates!`)
4. Débarrer le fichier zip, le flag est dans la première feuille (`flag-d0ntf0rg3ty0urp4ssw0rd`)

## Challenge 2

Pour le challenge 2, il y a plusieurs méthodes. On peut soit:
- Utiliser les macros pour brute force le mot de passe de la feuille (`myexcell3ntp4ssw0rd`)
- Renommer le fichier Excel en fichier zip, le dézipper et 
    - Le modifier pour le débarrer ***ou***
    - Trouver le flag directement dans les fichiers dézippés (`flag-l0ck1ngash33t1sntre4lpr0t3ct10n`)