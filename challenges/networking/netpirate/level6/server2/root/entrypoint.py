#!/usr/bin/env python3

import os
import socket

from time import sleep
from string import hexdigits
from random import randint, choices


def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()


def dhcp_lease():
  system("""
    [ -f "/run/dhclient.eth0.pid" ] && exit 0

    dhclient -4 -i \
      -pf /run/dhclient.eth0.pid \
      -lf /var/lib/dhcp/dhclient.eth0.leases \
      eth0

    IP=""
    while [ -z "$IP" ]; do
      sleep 1
      IP=$(ifconfig eth0 | awk '/inet addr:/{print $2}' | cut -d: -f2)
    done

    arp -s $(cat /common/server3.lease)
    echo "$IP $(ifconfig eth0 | awk '/HWaddr/{print $5}')" > /common/server2.lease
  """)


def dhcp_release():
  system("""
    [ ! -f "/run/dhclient.eth0.pid" ] && exit 0

    dhclient -4 -r \
      -pf /run/dhclient.eth0.pid \
      -lf /var/lib/dhcp/dhclient.eth0.leases \
      eth0

    rm /var/lib/dhcp/dhclient.eth0.leases
    rm /common/server2.lease
  """)


def arp_lock(lease_path):
  while not os.path.exists(lease_path):
    sleep(0.3)

  with open(lease_path, "r") as f:
    ip, hw = f.read().strip().split(" ", 1)

  print(f"info: locking {ip} to {hw}")
  system(f"arp -d {ip} >/dev/null")
  system(f"arp -s {ip} {hw}")

  return (ip, hw)


FLAG_INTERVAL = int(os.getenv("FLAG_INTERVAL", 60))

socket.setdefaulttimeout(10)
if os.path.exists("/common/server2.lease"):
  os.remove("/common/server2.lease")
sleep(10)

print("info: started receive loop")
while True:
  try:
    dhcp_lease()

    port = randint(49152, 65535)
    code = "".join(choices(hexdigits[:16], k=16))

    with open("/common/handshake", "w") as f:
      f.write(f"{port}:{code}")

    arp_lock("/common/server1.lease")

    print(f"info: wrote code '{code}' and port '{port}'")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
      server.settimeout(10)
      server.bind(("0.0.0.0", port))
      server.listen(1)

      conn, addr = server.accept()

      print(f"info: sending code '{code}' on port '{port}'")
      conn.sendall(f"secret-{code}".encode())
      flag = conn.recv(4096).decode().strip()

      print(f"info: got flag {flag}")
      conn.close()
  except Exception as e:
    print(f"warning: exception occured {e}")
  finally:
    dhcp_release()

  sleep(FLAG_INTERVAL)
