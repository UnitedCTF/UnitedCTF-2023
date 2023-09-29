# Solutions

## Challenge 0

Pour le challenge 0, on reçoit le code source de l'implémentation ainsi qu'un fichier texte contenant:

```text
Encrypted flag: 109182686074643895722088709167365445141191810738607234946970995195565143126326639298491559811626362620220483542471203258202228523397762222029355647206906381060208234693414092826600022194387688047152133633811429546736922384247476585392163233601397539732454039673206946596526550154189673354003367398347349634094
Public key n: 118106226504529835290659902652862270441701393010670403198509548446116062754784895631742671553891360108121798535929655210243116833524376067469193671542849954883259855044690013131911919692051474090274864465256877576012025608338155331729238496718446874151099007504701896133602255803379182471499683549826883906919
Public key e: 65537
Prime p: 13190768637976984234302503932008034455266070327745092110641230246745710909943443108764691767934840058779236981577713301202898617832514492510549730373739809
```

Comme on a déjà le `p`, on peut donc calculer `q` en divisant `n` par `p`.

```python
q = n // p
```

Avec `p`, `q` et `e`, on peut calculer `phi`, puis `d`.

```python
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
```

Enfin, on peut décrypter le flag avec `d`.

```python
m = pow(c, d, n)
flag_bytes = long_to_bytes(m)
flag = flag_bytes.decode()
```

Flag : `flag-B4s1cM4thsG0Brrrrr`

## Challenge 1

Pour le challenge 1, on reçoit le code source de l'implémentation. Cependant, contrairement au challenge 0, cette fois-ci on ne reçoit pas `p` :

```text
Encrypted flag: 8963789834135020795224347902733157530
Public key n: 102812568668937980441364628030483631731
Public key e: 65537
```

On doit factoriser `n` pour obtenir `p` et `q`:

```python
factors = factorint(n)
p, q = factors.keys()
```

On peut ensuite calculer `phi` et `d`:

```python
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
```

Enfin, on peut décrypter le flag avec `d`.

```python
m = pow(c, d, n)
flag_bytes = long_to_bytes(m)
flag = flag_bytes.decode()
```

Flag : `flag-5oItB3g1n5`

## Challenge 2

Dans le challenge 2, on est confronté à une situation où deux messages ont été chiffrés avec le même `n` mais avec des `e` différents. C'est une faille classique dans le RSA, souvent appelée l'attaque à "Common Modulus". On reçoit donc deux messages chiffrés et deux `e` distincts :

```text
Encrypted flag with e1: 28689726464471984025059169318232993078460273209886442537464870355974888638991579001316909915559847253642039942889027715458785887921890991685913066623858066692141396439551507135272690248388212221527918351696136808930939577385332643551868515367824945746400992597126260275260567739704458504887250100888625810473
Encrypted flag with e2: 24634677217736560807813188301324517298313799143930696944427747965369289033302366913857008167212275254432873019849491141635221114106968228983207351990636024265662263907972116273086083369173798015942155844255927609366141240071769784268644137652683967545087600740334041265826459874456456744259034149466527145714
Common public key n: 114194021424602852676222775460979397798152619390680654104963537621902451831836470362082297540629391019670245824664746208852579273180992066701163543676800651644862472034165286115837997798371540779457218633396524675029078054172857587631842213823984073019202305126609289686879378066041784553293227296464240835267
Public key e1: 65537
Public key e2: 65539
```

Sachant que `a * e1 + b * e2 = GCD(e1, e2)`, on peut calculer `a` et `b` avec l'algorithme d'Euclide étendu.

```python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

# Compute values a and b
gcd, a, b = extended_gcd(e1, e2)
if gcd != 1:
    raise ValueError("e1 and e2 are not coprime!")
```

À partir de `a` et `b`, on peut calculer `part1` et `part2`:

```python
part1 = pow(ciphertext1, a, n) if a > 0 else inverse(pow(ciphertext1, -a, n), n)
part2 = pow(ciphertext2, b, n) if b > 0 else inverse(pow(ciphertext2, -b, n), n)
```

Enfin, on peut reconstruire le flag avec `part1` et `part2`:

```python
m = (part1 * part2) % n
flag_bytes = long_to_bytes(m)
flag = flag_bytes.decode()
```

Flag : `flag-c0primeM0r3l1k3c00lpr1me`

## Challenge 3

Dans le challenge 3, cette fois, on a le flag chiffré 3 fois avec 3 clés `n` différentes, mais avec un `e` de 3. Dans ce cas, on peut utiliser l'attaque de Hastad.

On a reçu trois messages chiffrés avec trois n distincts:

```text
Encrypted flag with n1: 199928678335129521534816117251372004243631951572839401449003279903518834100069571091320968982602868709474615401880863345470748243593464697149581
Encrypted flag with n2: 199928678335129521534816117251372004243631951572839401449003279903518834100069571091320968982602868709474615401880863345470748243593464697149581
Encrypted flag with n3: 199928678335129521534816117251372004243631951572839401449003279903518834100069571091320968982602868709474615401880863345470748243593464697149581
Public key n1: 54480211672318529261153737241124035909405101302574005959419904185222248701151580652707671645279203400268250230850163373439999964654951210831576161822801074258720709980982470969180223732290113077134400609498948804326517040971517807443980711683259961591714363583442680847697668518057560976362369259216420298403
Public key n2: 79382046464035940928644258582437766071470914181474425319211449180490173805795597095440054550108248272037290249573436385360342167379959811479161881876742176484736522996587026402732941596472990990289448382779421834570297876513900625037542798016936828602732299904413831180969316730354734634154066823621537653891
Public key n3: 131589491776947758958467592466915216674048211257187114474753725558999666809235578734561335457854072350593976835987917502308359338941227671362126329183956008051170900960406428487888159547194071559114213486260052310509275517428526522308881260964985238126236714133674530571333238981213723015011052845742132037563
Public exponent e: 3
```

Pour exploiter cette faiblesse, on utilise le Théorème des restes chinois (CRT). La première étape consiste à calculer les valeurs de N1, N2 et N3 où:

```python
N = n1 * n2 * n3
N1 = N // n1
N2 = N // n2
N3 = N // n3
```

Ensuite, on utilise le CRT pour combiner les trois ciphertexts en un seul nombre `C` :

```python
C = (c1 * N1 * inverse(N1, n1) + c2 * N2 * inverse(N2, n2) + c3 * N3 * inverse(N3, n3)) % N
```

Maintenant, `C` est équivalent au cube du plaintext original. La dernière étape est de calculer la racine cubique de `C` pour obtenir le plaintext :

```python
m = gmpy2.iroot(C, 3)[0]
```

Une fois la racine cubique trouvée, il ne reste plus qu'à la convertir en bytes pour découvrir le flag :

```python
flag_bytes = long_to_bytes(m)
flag = flag_bytes.decode()
```

Flag : `flag-d0n0tCh4ng3k3y5`

## Challenge 4

Pour le challenge 4, on est face à une situation similaire au challenge 1. Par contre, on remarque que `p` et `q` sont très proches un de l'autre. Alors que les autres challenges s'attaquaient à l'implémentation de RSA, dans ce cas, on s'attaque simplement au `p` et `q` générés (l'implémentation est bonne (`e` est assez grand, `p` et `q` aussi)).


```text
Encrypted flag: [value from the challenge]
Public key n: [value from the challenge]
Public key e: 65537
```

Lorsque `p` et `q` sont générés très proches l'un de l'autre, on peut tenter une factorisation de Fermat:

```python
def fermat_factorization(n):
    a = math.isqrt(n) + 1
    b2 = a * a - n
    iterations = 0
    max_iterations = 10000
    while not is_perfect_square(b2) and iterations < max_iterations:
        a += 1
        b2 = a * a - n
        iterations += 1
    if iterations == max_iterations:
        raise ValueError("La factorisation de Fermat a échoué. p et q pourraient ne pas être assez proches.")
    b = math.isqrt(b2)
    return a - b, a + b
```

En utilisant la fonction ci-dessus, on peut factoriser `n`:

```python
p, q = fermat_factorization(n)
```

Ensuite, on peut calculer `phi` et `d` comme pour le challenge 1:

```python
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
```

Enfin, on décrypte le flag avec `d`:

```python
m = pow(c, d, n)
flag_bytes = long_to_bytes(m)
flag = flag_bytes.decode()
```

Flag : `flag-50m3t1me5y0uju5tg3tun1ucky`