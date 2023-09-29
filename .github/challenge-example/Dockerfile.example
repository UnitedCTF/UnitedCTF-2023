# Bonjour et bienvenue dans le Dockerfile de l'exemple de défi.

# Garder en tête que ce ne sont pas tout les défi qui auront besoin d'un Dockerfile
# et que ce n'est pas tout les défi qui auront besoin d'un Dockerfile comme celui-ci.

# Garder aussi en tête que ce Dockerfile est un exemple et que vous n'avez pas à le
# suivre à la lettre. Vous pouvez faire ce que vous voulez tant que le défi fonctionne
# et que le Dockerfile est valide.

FROM node:alpine

WORKDIR /app

# Copier des fichiers du défi
# ---------------------------------------------------------------------------------------
# Copier les fichiers que vous aurez de besoin pour que le défi soit fonctionnel
# on copie de la manière suivante:
# COPY <chemin du fichier dans le repo> <chemin du fichier dans le conteneur>
# pour les chemins relatif, le chemin de base est le dossier du Dockerfile

# exemple pour un défi utilisant node.js qui aurait cettre structure:
# challenges/
#   web/
#     challenge-cool/
#       Dockerfile
#       index.js
#       package.json
#       package-lock.json

# on copierait les fichiers de la manière suivante:
COPY index.js .
COPY package.json .
COPY package-lock.json .

# installer les dépendances
# ---------------------------------------------------------------------------------------
# Faite ici les commandes pour installer les dépendances de votre défi.
# Pour exécuter une commande, nous devons faire:
# RUN <commande>

# exemple pour un défi utilisant node.js, on voudrais installer les dépendances
# on ferait la commande suivante:
RUN npm ci

# Lancement du défi
# ---------------------------------------------------------------------------------------
# Il est maintenant temps de lancer le défi !
# Pour lancer le défi, il faudra faire la commande suivante:
# CMD <commande>
# CMD prend un tableau de string en argument, donc il faut séparer les arguments
# par des virgules.

# exemple dans notre projet la commande à exécuter pour lancer le défi est:
# node index.js

# on ferait donc la commande suivante:
CMD ["node", "index.js"]
