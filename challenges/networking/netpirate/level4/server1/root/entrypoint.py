#!/usr/bin/env python3

import os
import socket
from time import sleep

def system(cmd):
  from os import popen
  with popen(f"{cmd} 2>&1") as p:
    return p.read().strip()

FLAG = os.getenv("FLAG")

socket.setdefaulttimeout(3)
system("touch /common/handshake")

print("info: started transmit loop")
while True:
  try:
    system("inotifywait -q -e modify /common/handshake")

    with open("/common/handshake", "r") as f:
      port, code = f.read().strip().split(":", 1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.settimeout(3)

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
