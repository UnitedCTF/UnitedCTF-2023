# Are you blind ?

## Write-up (français)

Solution proposée en python 3.X avec les modules `Pillow` et `NumPy`.

Lors d'une première analyse de l'image, on peut se rendre compte qu'il n'y a pas d'informations supplémentaires dans l'encodage de l'image.

Si l'on imprime la valeur RGB de chaque pixel, on peut remarquer qu'à priori tous les pixels semblent être de la même couleur.

```py
import numpy as np
from PIL import Image
arr = np.array(Image.open('horizon.png'))
print(arr)

# [[[235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]
#   ...
#   [235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]]

#  [[235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]
#   ...
#   [235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]]
   
#   ...
```

Si l'on regarde les différentes couleurs dans l'image on se rend compte qu'il y a une autre couleur que le `rgb(235, 64, 52)`

```py
import numpy as np
from PIL import Image

arr = np.array(Image.open('horizon.png'))
colors = set()

for row in arr:
    for pixel in row:
        colors.add(tuple(pixel))

print(colors)

# {(235, 64, 52, 255), (234, 64, 52, 255)}
```

On peut créer un script qui réécrit chaque pixel de l'image en mettant l'accent sur les deux couleurs différentes.

```py
import numpy as np
from PIL import Image

arr = np.array(Image.open('horizon.png'))

target_value = [235, 64, 52, 255]

for row in arr:
    for pixel in row:
        if np.array_equal(pixel, target_value):
            print(".", end=" ")
        else:
            print("x", end=" ")
    print()
```

![flag revelation](./images/flag-revelation.png)

## Write-up (english)

Proposed solution in Python 3.X using the `Pillow` and `NumPy` modules.

During an initial analysis of the image, we can realize that there are no additional information in the image encoding.

If we print the RGB value of each pixel, we can observe that apparently all the pixels seem to be of the same color.

```py
import numpy as np
from PIL import Image
arr = np.array(Image.open('horizon.png'))
print(arr)

# [[[235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]
#   ...
#   [235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]]

#  [[235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]
#   ...
#   [235  64  52 255]
#   [235  64  52 255]
#   [235  64  52 255]]
   
#   ...
```

If we look at the different colors in the image, we realize that there is another color besides `rgb(235, 64, 52)`.

```py
import numpy as np
from PIL import Image

arr = np.array(Image.open('horizon.png'))
colors = set()

for row in arr:
    for pixel in row:
        colors.add(tuple(pixel))

print(colors)

# {(235, 64, 52, 255), (234, 64, 52, 255)}
```

We can create a script that rewrites each pixel of the image, emphasizing the two distinct colors.

```py
import numpy as np
from PIL import Image

arr = np.array(Image.open('horizon.png'))

target_value = [235, 64, 52, 255]

for row in arr:
    for pixel in row:
        if np.array_equal(pixel, target_value):
            print(".", end=" ")
        else:
            print("x", end=" ")
    print()
```

![flag revelation](./images/flag-revelation.png)


## Flag

`flag-d0ubl3EyeP@tCh`