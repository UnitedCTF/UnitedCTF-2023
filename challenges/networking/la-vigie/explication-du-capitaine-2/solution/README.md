# Nom du défi

## Write-up

### FR

En observant le fichier pcap, on remarque que toutes les frames TCP contiennent `This is just some noise to make the challenge a bit harder.` sauf la frame 18 qui n'est pas de meme longueur et qui contient le flag.
On peut copier le contenu de la frame en faisant `clique droit` puis `Copie comme texte imprimable`

### EN

By observing the pcap file, we notice that all TCP frames contain `This is just some noise to make the challenge a bit harder.` except frame 18 which is not of the same length and which contains the flag.
We can copy the contents of the frame by doing `right click` then `Copy as printable text`

## Flag

`flag-Iswe4rTh3sh4rkT4lkEdT0m3`