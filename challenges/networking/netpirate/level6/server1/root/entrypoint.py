#!/usr/bin/env python3

import os
import socket

from time import sleep


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
    echo "$IP $(ifconfig eth0 | awk '/HWaddr/{print $5}')" > /common/server1.lease
  """)


def dhcp_release():
  system("""
    [ ! -f "/run/dhclient.eth0.pid" ] && exit 0

    dhclient -4 -r \
      -pf /run/dhclient.eth0.pid \
      -lf /var/lib/dhcp/dhclient.eth0.leases \
      eth0

    rm /var/lib/dhcp/dhclient.eth0.leases
    rm /common/server1.lease
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


FLAG = os.getenv("FLAG")

socket.setdefaulttimeout(5)
if os.path.exists("/common/server1.lease"):
  os.remove("/common/server1.lease")
system("touch /common/handshake")

print("info: started transmit loop")
while True:
  try:
    system("inotifywait -q -e modify /common/handshake")

    dhcp_lease()

    with open("/common/handshake", "r") as f:
      port, code = f.read().strip().split(":", 1)
    sleep(3)

    arp_lock("/common/server2.lease")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.settimeout(5)

      tries = 0
      while tries < 3:
        try:
          client.connect(("server2", int(port)))
          break
        except:
          tries = tries + 1
          sleep(3)

      if client.recv(4096).decode().strip() == f"secret-{code}":
        print("info: correct code, sending flag")
        client.sendall(FLAG.encode())
      else:
        print("warning: wrong code")

      client.close()
  except Exception as e:
    print(f"warning: exception occured {e}")
  finally:
    dhcp_release()
