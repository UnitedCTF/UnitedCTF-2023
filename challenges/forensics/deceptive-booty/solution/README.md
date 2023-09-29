# Deceptive Booty

## Write-up

Increase the JPG height. The marker is FFC0.

Find a tool to increase it easily, here : [imganalyzer](https://github.com/dgagn/imganalyzer)

1. Understanding JPG Headers
A JPEG file consists of several segments, and each segment starts with a marker. The marker to focus on here is FFC0, which is called the Start of Frame (SOF0) marker. This marker indicates the start of the frame parameters, which includes details like width, height, and precision.

Looking at the file with different tools. I will be using `identify`, but any tools works.

```
identify -verbose ./trimmed_pirate.jpg
...
Image:
  Filename: ./trimmed_pirate.jpg
  Permissions: rw-r--r--
  Format: JPEG (Joint Photographic Experts Group JFIF format)
  Mime type: image/jpeg
  Class: DirectClass
  Geometry: 700x380+0+0
  Resolution: 300x300
  Print size: 2.33333x1.26667
  Units: PixelsPerInch
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channels: 3.0
  Channel depth:
    Red: 8-bit
    Green: 8-bit
    Blue: 8-bit
  Channel statistics:
    Pixels: 266000
    Red:
      min: 0  (0)
      max: 249 (0.976471)
      mean: 89.4665 (0.350849)
      median: 88 (0.345098)
      standard deviation: 58.563 (0.229659)
      kurtosis: -0.879484
      skewness: 0.205563
      entropy: 0.952439
    Green:
      min: 0  (0)
      max: 255 (1)
      mean: 138.421 (0.542829)
      median: 154 (0.603922)
      standard deviation: 57.0906 (0.223885)
      kurtosis: -0.916644
      skewness: -0.418162
      entropy: 0.959019
    Blue:
      min: 0  (0)
      max: 255 (1)
      mean: 138.648 (0.543717)
      median: 155 (0.607843)
      standard deviation: 55.2313 (0.216593)
      kurtosis: -0.89771
      skewness: -0.45269
      entropy: 0.951089
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 122.179 (0.479132)
      median: 132.333 (0.518954)
      standard deviation: 56.9617 (0.223379)
      kurtosis: -1.02827
      skewness: -0.238059
      entropy: 0.954183
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33,0.03)
    green primary: (0.3,0.6,0.1)
    blue primary: (0.15,0.06,0.79)
    white point: (0.3127,0.329,0.3583)
  Matte color: grey74
  Background color: white
  Border color: srgb(223,223,223)
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 700x380+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: JPEG
  Quality: 70
  Orientation: Undefined
  Profiles:
    Profile-icc: 456 bytes
  Properties:
    date:create: 2023-08-27T05:30:25+00:00
    date:modify: 2023-08-27T05:30:25+00:00
    date:timestamp: 2023-08-27T05:31:04+00:00
    icc:copyright: Google Inc. 2016
    icc:description: sRGB
    jpeg:colorspace: 2
    jpeg:sampling-factor: 2x2,1x1,1x1
    signature: ea84b38d089a8d3278cabb881c17304b3116e1faf79b7792442cb6edbbf523bb
  Artifacts:
    verbose: true
  Tainted: False
  Filesize: 35922B
  Number pixels: 266000
  Pixel cache type: Memory
  Pixels per second: 24.2969MP
  User time: 0.000u
  Elapsed time: 0:01.010
  Version: ImageMagick 7.1.1-15 Q16-HDRI aarch64 21298 https://imagemagick.org
identify: Corrupt JPEG data: 1086 extraneous bytes before marker 0xd9 `./trimmed_pirate.jpg' @ warning/jpeg.c/JPEGWarningHandler/403.
```

We see the identify: Corrupt JPEG data. There's more bytes to the image. Weird...

To find hidden data or manipulate image dimensions, we need to locate this marker within the JPG file.

2. Finding the Appropriate Tool
Use the provided tool, imganalyzer, to make the task easier. This tool is designed to read and modify image headers, and it specifically supports modifications to JPG and PNG files. (PS. it is made by me)

Access the tool here: [imganalyzer](https://github.com/dgagn/imganalyzer)

You can look through the source code and find what it does.

3. Modifying the JPG Height
Once you have the imganalyzer tool:

Run the tool with the desired JPG file as input.
Use the -t flag to specify the file type as "jpg".
Specify the new height using the --height flag.
Here's a command example:

```
imganalyzer --image input.jpg -t jpg --height [new_height_value]
```

The imganalyzer program will then search for the `FFC0` marker, locate the height parameter in the header, and change it to the new value provided.

## Write-up (fr)

1. Comprendre les en-têtes JPG:
Un fichier JPEG se compose de plusieurs segments, et chaque segment commence par un marqueur. Ici, le marqueur d'intérêt est `FFC0`, également connu sous le nom de marqueur Start of Frame (SOF0). Ce marqueur signifie le début des paramètres du cadre, qui englobe des détails tels que la largeur, la hauteur et la précision.
En inspectant le fichier avec différents outils, j'ai choisi `identify`, mais n'importe quel outil ferait l'affaire.

```
...
identify: Corrupt JPEG data: 1086 extraneous bytes before marker 0xd9 `./trimmed_pirate.jpg' @ warning/jpeg.c/JPEGWarningHandler/403.
```

De manière notable, nous observons le message: identify: Corrupt JPEG data. Cela indique qu'il y a des octets supplémentaires présents dans l'image, ce qui est curieux.

Pour découvrir des données cachées ou ajuster les dimensions de l'image, il est essentiel de localiser ce marqueur dans le fichier JPG.

2. Trouver l'outil approprié:
Pour cette tâche, utilisez l'outil suggéré, `imganalyzer`. Cet outil a été conçu pour lire et ajuster les en-têtes d'image, avec un accent particulier sur la prise en charge des modifications pour les fichiers JPG et PNG. (Note: Je suis le créateur de cet outil)

L'outil est disponible ici : [imganalyzer](https://github.com/dgagn/imganalyzer)

N'hésitez pas à plonger dans le code source pour comprendre son fonctionnement.

3. Modifier la hauteur du JPG:
Après avoir obtenu l'outil imganalyzer :
- Lancez l'outil, en sélectionnant le fichier JPG souhaité comme entrée.
- Utilisez le drapeau -t pour désigner le type de fichier comme "jpg".
- Indiquez la nouvelle hauteur via le drapeau `--height`.

Voici un exemple de commande :

```
imganalyzer --image input.jpg -t jpg --height [new_height_value]
```

Le logiciel `imganalyzer` recherchera alors le marqueur `FFC0`, identifiera le paramètre de hauteur dans l'en-tête, et le modifiera à la nouvelle valeur fournie.

## Flag

`flag-St3g0_1n_Pl41n_S1ght`
