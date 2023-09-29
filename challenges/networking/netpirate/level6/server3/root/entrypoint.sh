#!/bin/ash

IP=$(ip route | awk '/eth0 scope link/{print $7}')
HW=$(ifconfig eth0 | awk '/HWaddr/{print $5}')
IP_GATEWAY=$(ip route | awk '/default via/{print $3}')
IP_RANGE=$(ip -o -f inet addr show | awk '/eth0/ {print $4}')
IP_MAX=$(ipcalc "$IP_RANGE" | awk '/HostMax:/{print $2}')
IP_MIN=$(ipcalc "$IP_RANGE" | awk '/HostMin:/{print $2}')

# Shush the ARP requests
arptables -A OUTPUT -j DROP
arptables -A INPUT -j DROP

echo "$IP $HW" > /common/server3.lease
exec \
  dnsmasq \
    --no-daemon \
    --no-hosts \
    --no-negcache \
    --cache-size=0 \
    \
    --dhcp-authoritative \
    --dhcp-range="$IP_MIN,$IP_MAX,10m" \
    --dhcp-host="gateway,$IP_GATEWAY" \
    --dhcp-option="option:router,$IP_GATEWAY" \
    --dhcp-option="option:dns-server,$IP" \
    --dhcp-leasefile="/common/dnsmasq.leases" \
    --dhcp-script="/dhcp-script.sh"
