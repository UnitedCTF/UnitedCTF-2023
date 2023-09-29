#!/usr/bin/env python3

import os
import socket

from time import sleep
from string import hexdigits
from random import randint, choices

FLAG_INTERVAL = int(os.getenv("FLAG_INTERVAL", 60))

socket.setdefaulttimeout(10)
sleep(10)

print("info: started receive loop")
while True:
  try:
    port = randint(49152, 65535)
    code = "".join(choices(hexdigits[:16], k=16))

    with open("/common/handshake", "w") as f:
      f.write(f"{port}:{code}")

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

  sleep(FLAG_INTERVAL)
