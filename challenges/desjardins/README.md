# Track Desjardins
Le diagramme indique l'ordre dans lequel les challenges devraient être débloqués. Ceux liés à `Début` devraient être disponible dès le début.
```mermaid
graph TD
    00{Début}
    01[Navire intelligent]
    02[Es-tu le capitaine?]
    03[Secret mal gardé]
    04[Point de pivot]
    05[Le drapeau perdu]
    06[Petit équipage]
    07[Marin anonyme]
    08[Code source]
    09[Rôles des marins]
    10[Coffre au trésor]
    et{et}

    00 --> 01
    01 --> 02
    01 --> 03
    01 --> 05
    02 --> et
    03 --> et
    et --> 04
    04 --> 06
    06 --> 07
    06 --> 08
    08 --> 09
    06 --> 10
```
## Challenges
Voici les différents challenges de la track Desjardins.
  - [01. Navire intelligent](./descriptions/01.%20Un%20navire%20intelligent.md)
  - [02. Es-tu le capitaine?](./descriptions/02.%20Es-tu%20le%20capitaine.md)
  - [03. Secret mal gardé](./descriptions/03.%20Un%20secret%20mal%20gardé.md)
  - [04. Point de pivot](./descriptions/04.%20Point%20de%20pivot.md)
  - [05. Le drapeau perdu](./descriptions/05.%20Le%20drapeau%20perdu.md)
  - [06. Petit équipage](./descriptions/06.%20Petit%20équipage.md)
  - [07. Marin anonyme](./descriptions/07.%20Marin%20anonyme.md)
  - [08. Code source](./descriptions/08.%20Code%20source.md)
  - [09. Rôles des marins](./descriptions/09.%20Rôles%20des%20marins.md)
  - [10. Coffre au trésor](./descriptions/10.%20Coffre%20au%20trésor.md)
