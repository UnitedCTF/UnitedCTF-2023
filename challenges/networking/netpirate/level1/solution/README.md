# Netpirate level 1 / TCP listen

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Write-up

### Terminal 1

Listen on port 1337 to receive the flag.

```python
import socket

# Create a TCP socket and listen on port 1337
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  server.bind(("0.0.0.0", 1337))
  server.listen(1)

  print(f"[*] Listening for TCP packets in port 1337")
  try:
    while True:
      conn, addr = server.accept()
      print(f"[+] {conn.recv(4096).decode().strip()}")
      conn.close()
  except KeyboardInterrupt: pass
```

## Flag

`flag-59c88a9e8a08907efb4cf67310b0b122430a07e7cfb0251fb04f08e27fde1d3a`
