# Netpirate

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Description (français)

Il est temps de revisiter toutes les vulnérabilités réseau de base 😉. Le but est de résoudre toutes les épreuves en utilisant le cadriciel python [scapy](https://scapy.net/). Tu peux te connecter à une épreuve en utilisant la commande SSH `ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p2222 level{1..6}@XX.XX.XX.XX`, le mot de passe est le même que le nom de l'épreuve.

Tous les outils nécessaires pour résoudre l'épreuve sont déjà présents dans ton environment:

- Éditeurs de texte
  - [vim](https://linux.die.net/man/1/vim)
  - [nano](https://linux.die.net/man/1/nano)
- Multiplexeurs de terminal
  - [tmux](https://linux.die.net/man/1/tmux)
  - [screen](https://linux.die.net/man/1/screen)
- Outils réseau
  - [iptables](https://linux.die.net/man/8/iptables)
  - [tshark](https://linux.die.net/man/1/tshark)
  - [tcpdump](https://linux.die.net/man/8/tcpdump)
  - [nmap](https://linux.die.net/man/1/nmap)
- Python
  - [python3](https://linux.die.net/man/1/python)
  - [scapy](https://linux.die.net/man/1/scapy)
  - [libnetfilter_queue](https://www.netfilter.org/)

Pour chacune des épreuves, la machine dans laquelle tu es connecté(e) en SSH est appelée `entrypoint` et toutes les autres machines qui font partie de l'infrastructure sont appelées `serverX` où `X` est un nombre dans l'intervalle `[1,3]`.

- Le `server1` envoie toujours le flag.
- Le `server2`, si présent, reçoit toujours le flag.
- Le `server3`, si présent, valide ou assigne quelque chose...

Pour chacune des épreuves, un fichier `pcap` du traffic avec les flags caviardés est disponible en tant qu'indice.

Liste des épreuves
- [level1](./level1/README.md)
- [level2](./level2/README.md)
- [level3](./level3/README.md)
- [level4](./level4/README.md)
- [level5](./level5/README.md)
- [level6](./level6/README.md)

## Description (english)

Time to revisit all the basic network vulnerabilities 😉. The goal is to solve every challenges using the python framework [scapy](https://scapy.net/). You can connect to a challenge using the SSH command `ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p2222 level{1..6}@XX.XX.XX.XX`, the password is the same as the name of the level.

All the tools you need to solve the challenge are already present in your environment:

- Text editors
  - [vim](https://linux.die.net/man/1/vim)
  - [nano](https://linux.die.net/man/1/nano)
- Terminal multiplexers
  - [tmux](https://linux.die.net/man/1/tmux)
  - [screen](https://linux.die.net/man/1/screen)
- Network tools
  - [iptables](https://linux.die.net/man/8/iptables)
  - [tshark](https://linux.die.net/man/1/tshark)
  - [tcpdump](https://linux.die.net/man/8/tcpdump)
  - [nmap](https://linux.die.net/man/1/nmap)
- Python
  - [python3](https://linux.die.net/man/1/python)
  - [scapy](https://linux.die.net/man/1/scapy)
  - [libnetfilter_queue](https://www.netfilter.org/)

In every level, the machine where you SSH in is called `entrypoint` and the other machines part of the infrastructure are called `serverX` where `X` is a number in the interval `[1,3]`.

- The `server1` always sends the flag
- The `server2`, if present, always receives the flag
- The `server3`, if present, validates or assigns something...

For every level, a pcap file of the traffic with redacted flags is available as a hint.

Levels list
- [level1](./level1/README.md)
- [level2](./level2/README.md)
- [level3](./level3/README.md)
- [level4](./level4/README.md)
- [level5](./level5/README.md)
- [level6](./level6/README.md)

## Notes

Network access from the challenges should be blocked using the helper script `./level-network-isolation.sh enable`

## Solution

The solution for every challenge is in their respective directories

- [level1](./level1/solution/README.md)
- [level2](./level2/solution/README.md)
- [level3](./level3/solution/README.md)
- [level4](./level4/solution/README.md)
- [level5](./level5/solution/README.md)
- [level6](./level6/solution/README.md)
