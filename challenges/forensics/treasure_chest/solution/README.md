# Treasure chest

## Write-up (fr)

En utilisant l'outil [bkcrack](https://github.com/kimci86/bkcrack), il est possible d'extraire le flag sans savoir le mot de passe puisque l'archive est vulnérable à "ZipCrypto known plaintext attack" et on connait l'en-tête des fichiers PNG.

```bash
# Générer la partie connue de l'image PNG
#
# Même si l'en-tête est seulement 8 octets, on peut aussi ajouter les 8 octets du block IHDR qui doit être le premier block après l'en-tête. (voir https://en.wikipedia.org/wiki/PNG#Critical_chunks)
# Deux octets additionnels sont ajoutés de la largeur de l'image vu qu'on peut estimer que la largeur du flag est moins que 255^2 pixels de long.

#
# HEADER : 89 50 4E 47 OD OA 1A OA
#             ^-PNG--^ ^windows/linux validation de conversion
# IHDR   : 00 00 00 0d 49 48 44 52 00 00
#          ^len de 13^ ^--IHDR---^ ^deux octets "du haut"
#
# Pour un total de 18 octets
# 
convert xc:black -size 1x1 png:- | head -c18 > png_header

# Trouver les clés pour décoder le fichier zip, un minimum de 12 octets est requis
# Tandis que le nombre d'octets connu n'est pas le meilleur, ça devrait prendre environ 15 minutes maximum pour trouver la solution
bkcrack -C treasure_chest.zip -c flag.png -p png_header

# En utilisant les 3 clés trouvées à la dernière étape, extraire le flag
bkcrack -C treasure_chest.zip -c flag.png -k XXXXXXXX XXXXXXXX XXXXXXXX -d flag.png

# Voir le flag
xdg-open flag.png
```

## Write-up (en)

Using the tool [bkcrack](https://github.com/kimci86/bkcrack), it is possible to extract the flag without knowing the password since the archive is vulnerable to the ZipCrypto known plaintext attack and we know the header of the PNG file.

```bash
# Generate the known part of the PNG image
#
# Even though the header is only 8 bytes, we can also add 8 bytes from the IHDR block which must be the first block after the header. (see https://en.wikipedia.org/wiki/PNG#Critical_chunks)
# Two additional bytes are added from the image's width since we can guess that the flag's width is less than 255^2 pixels long.
#
# HEADER : 89 50 4E 47 OD OA 1A OA
#             ^-PNG--^ ^windows/linux conversion checks
# IHDR   : 00 00 00 0d 49 48 44 52 00 00
#          ^len of 13^ ^--IHDR---^ ^two higher width bytes
#
# For a total of 18 bytes.
# 
convert xc:black -size 1x1 png:- | head -c18 > png_header

# Find the keys to crack the zip file, a minimum of 12 bytes is required
# While the amount of known bytes is not the best, it should take 15 minutes maximum to crack
bkcrack -C treasure_chest.zip -c flag.png -p png_header

# Using the 3 keys found at the last step, extract the flag
bkcrack -C treasure_chest.zip -c flag.png -k XXXXXXXX XXXXXXXX XXXXXXXX -d flag.png

# View the flag
xdg-open flag.png
```

## Flag

`flag-YouDidntEvenNeedTheKey`
