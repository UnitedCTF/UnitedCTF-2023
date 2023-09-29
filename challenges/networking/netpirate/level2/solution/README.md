# Netpirate level 2 / UDP listen random port

**Author:** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Write-up

### Terminal 1

Listen all UDP traffic to receive the flag.

```python
from scapy.all import *

# Print the data contained in UDP packets
def sniff_udp(packet):
  print(f"[+] {packet[Raw].load.decode().strip()}")

print(f"[*] Listening for UDP packets")
sniff(prn=sniff_udp, filter="udp", store=False)
```

## Flag

`flag-359ec5f6fb5f875bd476121453c7071d0d4de24eb96cb51e5370a44fae4cd797`
