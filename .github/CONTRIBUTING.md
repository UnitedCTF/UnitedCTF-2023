# Contributions à UnitedCTF 2023

Tout d'abord, merci de vouloir contribuer pour faire de cet événement un moment mémorable.


## Démarrage rapide

1. Forker le projet
![fork a repo](https://docs.github.com/assets/cb-79331/images/help/repository/fork_button.png)

2. Cloner le dépôt forké

```bash
git clone https://github.com/${your_username}/UnitedCTF2023
```

3. Configurer le dépôt distant (upstream)

```bash
git remote add upstream https://github.com/UnitedCTF/UnitedCTF2023.git
```

4. Assurez-vous de récupérer les dernières modifications de l'upstream

```bash
git pull upstream main
git push origin main # to update your remote fork
```

5. Crée une branche séparée

```bash
git checkout -b add-{category_name}-{challenge_name}
```

6. Effectuer les modifications pour votre défi localement

7. Ajouter les fichiers concernés

```bash
git add challenges/category/{challenge_name}
```

8. Effectuer un commit de vos modifications

```bash
git commit
```

9. Pousser vos modifications

```bash
git push origin add-{category_name}-{challenge_name}
```

10. Créer une pull request sur Github

### Note importante

**Toujours** effectuer une récupération de l'upstream avant de commencer à effectuer vos modifications locales

```bash
git checkout main
git pull upstream main
git push origin main # to update your remote fork 
```

## Comment contribuer

Vous pouvez contribuer de différentes manières :

### Concevoir un défi CTF

Vous avez une bonne idée de défi que vous souhaitez ajouter au dépôt ? C'est génial, mais avant de le faire, veuillez prendre en compte certaines règles et lignes directrices :

- **Qualité du défi** : Ce qu'il faut faire et ne pas faire :
  - **Ne pas** plagier et soumettre des défis provenant de concours CTF passés, votre défi doit être authentique. À la place, vous pouvez vous en inspirer.
  - **Ne pas** créer un défi qui implique :
    - Deviner
    - Une force brute excessive
    - L'utilisation d'exploits disponibles publiquement (CVE)
  - **Ne pas** utiliser d'espaces dans les noms de répertoire et de fichiers, utilisez des tirets (-) ou (de manière exclusive) des tirets bas (_) à la place.
  - **Faire** créer un répertoire distinct pour votre défi avec un nom cohérent, et placez-le à l'intérieur du dossier de catégorie approprié.
  - **Faire** initialiser chaque défi avec un fichier [`README.md`](./challenge-example/README.md).
  - **Faire** créer un répertoire `solution` dans le répertoire de votre défi avec un fichier [`README.md`](./challenge-example/solution/README.md) à l'intérieur (c'est là que vous pouvez mettre votre write-up).
  - **Faire** écrire un code propre pour le code source de votre défi, cela est très apprécié.
  - **Faire** créer un défi amusant qui enseignera ou rappellera au joueur un concept important.
  - **Faire** preuve de créativité dans le nom, la description et le flag de votre défi. Le flag devrait être lié d'une manière ou d'une autre au défi.

- **Soumission de votre défi** : Si votre défi respecte la section précédente, voici comment le soumettre :
  - Créez une branche distincte avec un nom cohérent (par exemple, add-{nom_de_la_catégorie}-{nom_du_challenge}).
  - Effectuez un commit et poussez les modifications vers le dépôt forké.
  - Ouvrez une Pull Request afin que le défi soit examiné et testé avant d'être fusionné dans la branche principale.

- **Optionnel mais apprécié** : Vous pouvez nous faciliter la tâche en :
  - Dockerisant votre défi (principalement s'il s'agit d'un défi pwn ou web).
  - Testant votre défi et vous assurant qu'il fonctionne comme prévu et qu'il n'y a pas de solution non intentionnelle facile.
  - Rédigeant un write-up pour la solution envisagée que vous aviez en tête lors de la conception du défi :
    - Il devrait être écrit en Markdown.
    - Il devrait être placé dans le fichier `solution/README.md` du défi.

Voici un tableau décrivant l'impact de la quantité de **travail** et d'**inspiration** sur la qualité d'un défi:

| Tâches nécessitant ⬇️+➡️ | Peu de travail        | Un peu de travail       | Beaucoup de travail  | Trop de travail       |
|---------------------------|-----------------------|-------------------------|----------------------|-----------------------|
| **Peu d'inspiration**     | _Très facile_         | Relaxant/Décevant       | Sans intérêt         | `Ennuyeux`            |
| **Un peu d'inspiration**  | Facile/Satisfaisant   | Amusant                 | Épuisant             | `Frustrant`           |
| **Beaucoup d'inspiration**| Surprenant/Instructif | Stimulant              | _Très difficile_      | `Très frustrant`      |
| **Trop d'inspiration**    | `Devinez`             | `Frustrant`             | `Très frustrant`      | `Déraisonnable`        |

Source : page 10 du document [ctf-design].

### Suggérer une idée de défi

Si vous avez une excellente idée de défi mais que vous n'avez pas la possibilité de la réaliser, ce n'est pas un problème ! Vous pouvez toujours suggérer l'idée pour que d'autres contributeurs la prennent, l'améliorent et en fassent un défi.
Pour ce faire, ouvrez une nouvelle issue et définissez le titre comme suit : `"idée de défi : brève description de l'idée"`. Dans la description, décrivez en détail votre idée de défi.

### Dockeriser les défis

Dans le cas où il y aurait des défis qui doivent être exécutés à l'intérieur d'un conteneur mais qui n'ont pas encore été dockerisés, vous pouvez rédiger un Dockerfile pour les défis et soumettre votre demande de pull request.

### Améliorations

Réviser les défis des autres contributeurs et suggérez des améliorations, par exemple :

- Nettoyer, refactorer et reformater le code source.
- Corriger les bugs du défi.
- Autres améliorations que vous jugez utiles.

### Tests des défis et write-ups

Vous pouvez également contribuer en testant les défis. Pour cela, vous devrez déployer localement le défi et le résoudre en boîte noire, comme si vous étiez un joueur de CTF n'ayant pas accès au code source. Après avoir résolu le défi, soumettez un write-up en syntaxe Markdown qui sera intégré à ce dépôt.


Ce document présenté se base sur la version anglaise du document présent [`ici`](https://github.com/UnitedCTF/UnitedCTF-2022/blob/master/.github/CONTRIBUTING.md)
