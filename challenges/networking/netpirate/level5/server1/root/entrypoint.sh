#!/bin/ash
trap "exit" SIGTERM

# Configure DNS server to be server3
DNS_SERVER="server3"
while ! ping -c1 "$DNS_SERVER" &>/dev/null; do
  echo "info: waiting for '$DNS_SERVER'"
  sleep 1
done

IP=$(getent hosts "$DNS_SERVER" | awk '{print $1}')
echo "info: resolved '$DNS_SERVER' to '$IP'"
echo "nameserver $IP" >> /etc/_resolv.conf
cat /etc/_resolv.conf > /etc/resolv.conf && rm /etc/_resolv.conf

# Add server2 as a permanent ARP table entry
PERMANENT_ARP_HOST="server2"
while ! ping -c1 "$PERMANENT_ARP_HOST" &>/dev/null; do
  echo "info: waiting for '$PERMANENT_ARP_HOST'"
  sleep 1
done

IP=$(getent hosts "$PERMANENT_ARP_HOST" | awk '{print $1}')
MAC=$(ip neigh | grep "$IP" | awk '{print $5}')

arp -s "$IP" "$MAC"
echo "info: added static arp entry $PERMANENT_ARP_HOST -> $IP [$MAC]"

exec /entrypoint.py
